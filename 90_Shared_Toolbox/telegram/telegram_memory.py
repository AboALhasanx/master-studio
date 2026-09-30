"""Gateway memory — the D14 interface to ``00_STUDIO_HUB/telegram/``.

The gateway is a *layer* inside Master Studio, not a scatter of writes into the
project's shared memory. This module is the only sanctioned way it touches its
own memory folder:

    from telegram.telegram_memory import record_post, last_state, append_log

Design rules (ADR D14):
  * **Own memory folder** — ``00_STUDIO_HUB/telegram/``; the gateway writes
    here freely.
  * **No direct writes to the parent memory** — ``00_STUDIO_HUB/MEMORY.md`` is
    the project's, and the agent is the only intermediary into it.
  * **Atomic writes** — every write goes temp-file → ``os.replace``, so a
    crash never leaves a half-written ledger.
  * **Stdlib only** — same constraint as the rest of the package.

Everything is best-effort: a memory write must never break a real publish, so
:func:`record_post` and :func:`append_log` swallow filesystem errors by default.
"""

from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

__all__ = [
    "memory_root",
    "record_post",
    "append_log",
    "read_state",
    "set_state",
    "read_prefs",
    "last_state",
]

#: ``90_Shared_Toolbox/telegram/`` → repo root is three parents up.
_REPO_ROOT = Path(__file__).resolve().parents[2]
#: The gateway's own memory folder (ADR D14).
DEFAULT_MEMORY_ROOT = _REPO_ROOT / "00_STUDIO_HUB" / "telegram"

_STATE_HEADER = "# حالة البوابة\n\n"
_STATE_FOOTER = "\n<!-- المنطقة أعلاه JSON آلي. لا تكتب فوق السطر الأول. -->\n"


def memory_root() -> Path:
    """Return the gateway memory folder's path (creating it if absent)."""
    root = DEFAULT_MEMORY_ROOT
    root.mkdir(parents=True, exist_ok=True)
    return root


def _atomic_write(path: Path, text: str) -> None:
    """Write ``text`` to ``path`` atomically (temp file then ``os.replace``)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + f".tmp{os.getpid()}")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


# --------------------------------------------------------------------- state
def read_state() -> dict[str, Any]:
    """Read ``STATE.md``'s JSON block. Missing/corrupt file -> ``{}``."""
    path = memory_root() / "STATE.md"
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end < start:
        return {}
    try:
        data = json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def set_state(**fields: Any) -> dict[str, Any]:
    """Merge ``fields`` into ``STATE.md`` and return the new state."""
    state = read_state()
    state.update(fields)
    _atomic_write(
        memory_root() / "STATE.md",
        _STATE_HEADER + json.dumps(state, ensure_ascii=False, indent=2) + "\n" + _STATE_FOOTER,
    )
    return state


# ----------------------------------------------------------------------- log
def append_log(text: str, *, when: str | None = None) -> Path:
    """Append one line to today's log (append-only) and return its path.

    Never raises on a normal filesystem error — a memory note is bookkeeping
    and must not take a publish down with it.
    """
    path = memory_root() / "log" / f"{when or _today()}.md"
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        prefix = "" if path.exists() else f"# سجل البوابة — {when or _today()}\n\n"
        with path.open("a", encoding="utf-8") as fh:
            if prefix:
                fh.write(prefix)
            fh.write(f"- `{_stamp()}` — {text}\n")
    except OSError:
        pass
    return path


# ---------------------------------------------------------------------- post
def record_post(
    subject: str,
    message_id: int | None,
    *,
    kind: str = "post",
    detail: str | None = None,
    error: bool = False,
) -> None:
    """Record a publish in the log and update ``STATE.md``.

    ``kind`` is a free label (``post``, ``quiz``, ``file``, ``reply`` ...).
    ``error=True`` logs it as a failed attempt and does **not** advance
    ``last_post``.
    """
    arrow = "✗" if error else "✓"
    line = f"{arrow} نشر `{kind}` → {subject}"
    if message_id is not None:
        line += f" (رسالة {message_id})"
    if detail:
        line += f" — {detail}"
    append_log(line)

    if not error:
        set_state(last_post={"subject": subject, "message_id": message_id,
                             "kind": kind, "ts": _stamp()})


# --------------------------------------------------------------------- prefs
def read_prefs() -> str:
    """Return the prefs/decisions memory verbatim (or ``""`` if absent)."""
    path = memory_root() / "TELEGRAM_MEMORY.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def last_state() -> dict[str, Any]:
    """Alias for :func:`read_state` — reads better at call sites."""
    return read_state()


def _self_check() -> dict[str, Any]:
    """Tiny smoke helper: write a heartbeat and return the state."""
    return set_state(last_self_check=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))


if __name__ == "__main__":  # pragma: no cover - manual probe
    print(json.dumps(_self_check(), ensure_ascii=False, indent=2))
