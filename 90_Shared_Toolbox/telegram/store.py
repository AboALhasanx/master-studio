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

    #: A job is retried at most this many times before it is parked as ``dead``
    #: (roadmap G3 / issue #14 -- bounded retries, no infinite loop).
    MAX_ATTEMPTS = 8

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
                available_at    REAL NOT NULL DEFAULT 0,
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
        self._ensure_columns({"available_at": "REAL NOT NULL DEFAULT 0"})
        self.db.commit()

    def _ensure_columns(self, wanted: dict[str, str]) -> None:
        """Migrate pre-existing databases (the queue landed before available_at)."""
        have = {row[1] for row in self.db.execute("PRAGMA table_info(jobs)")}
        for name, decl in wanted.items():
            if name not in have:
                self.db.execute(f"ALTER TABLE jobs ADD COLUMN {name} {decl}")

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

    def mark_error(
        self,
        key: str,
        error: str,
        *,
        retry_in: float = 0.0,
        now: float | None = None,
    ) -> None:
        """Record a failed attempt and schedule its retry.

        The job stays ``error`` (hence retryable) until it exhausts
        :attr:`MAX_ATTEMPTS`, then it is parked as ``dead`` and drops out of
        :meth:`pending`. ``retry_in`` is the cooldown: a 429 passes the
        ``retry_after`` Telegram sent, other failures use ``backoff_delay``.
        """
        now = time.time() if now is None else float(now)
        row = self.find(key)
        attempts = (int(row["attempts"]) if row else 0) + 1
        status = "dead" if attempts >= self.MAX_ATTEMPTS else "error"
        self.db.execute(
            "UPDATE jobs SET status=?, attempts=attempts+1, last_error=?, "
            "available_at=?, updated_at=? WHERE idempotency_key=?",
            (status, str(error)[:500], now + max(0.0, float(retry_in)), now, key),
        )
        self.db.commit()

    def mark_queued(self, key: str, *, delay: float = 0.0, now: float | None = None) -> None:
        """Keep the job queued (e.g. rate limited) — it is retried later."""
        now = time.time() if now is None else float(now)
        self.db.execute(
            "UPDATE jobs SET status='queued', attempts=attempts+1, available_at=?, updated_at=? WHERE idempotency_key=?",
            (now + max(0.0, float(delay)), now, key),
        )
        self.db.commit()

    def requeue_payload(
        self, key: str, payload: dict[str, Any], *, delay: float = 0.0, now: float | None = None
    ) -> None:
        """Swap in a new payload and keep the job queued (issue #11 chunking).

        Deliberately does **not** bump ``attempts``: a multi-chunk message makes
        progress on every hop and must not burn the retry budget.
        """
        now = time.time() if now is None else float(now)
        self.db.execute(
            "UPDATE jobs SET payload=?, status='queued', available_at=?, updated_at=? "
            "WHERE idempotency_key=?",
            (
                json.dumps(payload, ensure_ascii=False),
                now + max(0.0, float(delay)),
                now,
                key,
            ),
        )
        self.db.commit()

    def pending(self, limit: int = 50, now: float | None = None) -> list[dict[str, Any]]:
        """Jobs eligible to run: queued/errored **and** past their cooldown."""
        now = time.time() if now is None else float(now)
        rows = self.db.execute(
            "SELECT * FROM jobs WHERE status IN ('queued', 'error') AND available_at <= ? "
            "ORDER BY created_at LIMIT ?",
            (now, int(limit)),
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

    def stamps(self) -> dict[int, list[float]]:
        """A copy of the retained timestamps, for persistence.

        The limiter lives in memory, so without a way out and back in every
        new process starts with an empty ledger and the ceiling never blocks
        anything (issue #22, found live on 2026-09-30).
        """
        return {chat: list(ts) for chat, ts in self._stamps.items()}

    def seed(self, stamps) -> None:
        """Load timestamps a previous process recorded."""
        for chat_id, ts in (stamps or {}).items():
            self._stamps[int(chat_id)].extend(float(t) for t in ts)


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
