"""Durable job store: idempotency, audit trail, rate limiting (issue #14).

Everything lives in SQLite (stdlib only) so the gateway survives restarts and
leaves a forensic record of every attempted action.

Rate policy mirrors Telegram's published limits: ~1 message/second and ~20
messages/minute **per chat** (see roadmap risk register).
"""

from __future__ import annotations

import json
import os
import sqlite3
import time
from collections import defaultdict, deque
from pathlib import Path
from typing import Any, Iterable

__all__ = ["Store", "ChatRateLimiter", "backoff_delay", "DEFAULT_DB_PATH"]

DEFAULT_DB_PATH = Path(__file__).with_name("gateway.db")

PER_CHAT_PER_MINUTE = 20
PER_CHAT_MIN_INTERVAL = 1.0


def backoff_delay(attempt: int, base: float = 2.0, cap: float = 60.0) -> float:
    """Exponential backoff: 2, 4, 8, ... capped at ``cap`` seconds."""
    attempt = max(0, int(attempt))
    return min(cap, base * (2 ** attempt))


class Store:
    """SQLite-backed job queue + audit log."""

    def __init__(self, path: Path | str | None = None):
        self.path = Path(path) if path else DEFAULT_DB_PATH
        if str(self.path) != ":memory:":
            self.path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(str(self.path))
        self.db.row_factory = sqlite3.Row
        self._create_schema()

    def _create_schema(self) -> None:
        self.db.executescript(
            """
            CREATE TABLE IF NOT EXISTS jobs (
                idempotency_key TEXT PRIMARY KEY,
                verb            TEXT NOT NULL,
                chat_id         INTEGER,
                thread_id       INTEGER,
                payload         TEXT NOT NULL,
                status          TEXT NOT NULL DEFAULT 'queued',
                attempts        INTEGER NOT NULL DEFAULT 0,
                message_id      INTEGER,
                last_error      TEXT,
                created_at      REAL NOT NULL,
                updated_at      REAL NOT NULL
            );
            CREATE TABLE IF NOT EXISTS audit (
                id               INTEGER PRIMARY KEY AUTOINCREMENT,
                ts               REAL NOT NULL,
                actor            INTEGER,
                verb             TEXT NOT NULL,
                chat_id          INTEGER,
                thread_id        INTEGER,
                idempotency_key  TEXT,
                result           TEXT NOT NULL,
                detail           TEXT
            );
            """
        )
        self.db.commit()

    # -- jobs ------------------------------------------------------------
    def enqueue(
        self,
        key: str,
        verb: str,
        chat_id: int | None,
        thread_id: int | None,
        payload: dict[str, Any],
    ) -> bool:
        """Insert a job. Returns ``False`` when the key already exists (idempotency)."""
        now = time.time()
        cur = self.db.execute(
            "INSERT OR IGNORE INTO jobs "
            "(idempotency_key, verb, chat_id, thread_id, payload, status, created_at, updated_at) "
            "VALUES (?, ?, ?, ?, ?, 'queued', ?, ?)",
            (key, verb, chat_id, thread_id, json.dumps(payload, ensure_ascii=False), now, now),
        )
        self.db.commit()
        return cur.rowcount == 1

    def find(self, key: str) -> dict[str, Any] | None:
        row = self.db.execute("SELECT * FROM jobs WHERE idempotency_key = ?", (key,)).fetchone()
        return dict(row) if row else None

    def mark_sent(self, key: str, message_id: int | None = None) -> None:
        self.db.execute(
            "UPDATE jobs SET status='sent', message_id=?, updated_at=? WHERE idempotency_key=?",
            (message_id, time.time(), key),
        )
        self.db.commit()

    def mark_error(self, key: str, error: str) -> None:
        self.db.execute(
            "UPDATE jobs SET status='error', attempts=attempts+1, last_error=?, updated_at=? "
            "WHERE idempotency_key=?",
            (str(error)[:500], time.time(), key),
        )
        self.db.commit()

    def mark_queued(self, key: str) -> None:
        """Keep the job queued (e.g. rate limited) — it is retried later."""
        self.db.execute(
            "UPDATE jobs SET status='queued', attempts=attempts+1, updated_at=? WHERE idempotency_key=?",
            (time.time(), key),
        )
        self.db.commit()

    def pending(self, limit: int = 50) -> list[dict[str, Any]]:
        rows = self.db.execute(
            "SELECT * FROM jobs WHERE status IN ('queued', 'error') ORDER BY created_at LIMIT ?",
            (int(limit),),
        ).fetchall()
        return [dict(r) for r in rows]

    def counts(self) -> dict[str, int]:
        rows = self.db.execute("SELECT status, COUNT(*) AS n FROM jobs GROUP BY status").fetchall()
        return {r["status"]: r["n"] for r in rows}

    # -- audit -----------------------------------------------------------
    def audit(
        self,
        verb: str,
        result: str,
        *,
        actor: int | None = None,
        chat_id: int | None = None,
        thread_id: int | None = None,
        idempotency_key: str | None = None,
        detail: str | None = None,
    ) -> None:
        self.db.execute(
            "INSERT INTO audit (ts, actor, verb, chat_id, thread_id, idempotency_key, result, detail) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                time.time(),
                actor,
                verb,
                chat_id,
                thread_id,
                idempotency_key,
                result,
                None if detail is None else str(detail)[:1000],
            ),
        )
        self.db.commit()

    def audit_rows(self, limit: int = 100) -> list[dict[str, Any]]:
        rows = self.db.execute(
            "SELECT * FROM audit ORDER BY id DESC LIMIT ?", (int(limit),)
        ).fetchall()
        return [dict(r) for r in rows]

    def close(self) -> None:
        self.db.close()


class ChatRateLimiter:
    """Sliding-window limiter: <= N messages/minute and >= interval seconds apart."""

    def __init__(
        self,
        per_minute: int = PER_CHAT_PER_MINUTE,
        min_interval: float = PER_CHAT_MIN_INTERVAL,
    ):
        self.per_minute = int(per_minute)
        self.min_interval = float(min_interval)
        self._stamps: dict[int, deque[float]] = defaultdict(deque)

    def allow(self, chat_id: int, now: float | None = None) -> bool:
        now = time.time() if now is None else float(now)
        stamps = self._stamps[int(chat_id)]
        cutoff = now - 60.0
        while stamps and stamps[0] <= cutoff:
            stamps.popleft()
        if stamps and (now - stamps[-1]) < self.min_interval:
            return False
        if len(stamps) >= self.per_minute:
            return False
        return True

    def record(self, chat_id: int, now: float | None = None) -> None:
        now = time.time() if now is None else float(now)
        self._stamps[int(chat_id)].append(now)


def load_dotenv(path: Path | str | None = None) -> dict[str, str]:
    """Minimal ``.env`` reader (no dependency): KEY=VALUE lines, ``#`` comments.

    Added at gate G1 so the CLI can read ``TELEGRAM_OWNER_IDS`` from the local
    ``.env``; the token itself is only consumed once the live transport lands
    at gate G2. Values already present in ``os.environ`` always win.
    """
    env_path = Path(path) if path else Path(__file__).resolve().parents[2] / ".env"
    loaded: dict[str, str] = {}
    if not env_path.exists():
        return loaded
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value
        loaded[key] = value
    return loaded
