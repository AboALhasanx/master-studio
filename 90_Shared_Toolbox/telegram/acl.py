"""Access control — enforced in code, never in a prompt (issue #16, ADR fail-closed).

Rules
-----
1. Local-only verbs (``status``, ``queue``) touch nothing remote → no gate.
2. Everything else requires an explicit ``actor`` that is on the allowlist.
3. An **empty** allowlist denies everyone: a mis-configured deployment must
   fail closed, not open.
4. Destructive verbs additionally require ``confirm=True`` (ADR D7).
5. Every refusal raises — the executor writes it to the audit log.
"""

from __future__ import annotations

import os
from typing import Iterable

from .errors import AccessDenied, ConfirmationRequired
from .schema import Action

__all__ = [
    "ACL",
    "LOCAL_VERBS",
    "owner_ids_from_env",
    "chat_allowlist_from_env",
]

# Verbs that never reach Telegram and therefore need no actor gate.
LOCAL_VERBS = frozenset({"status", "queue"})

ENV_OWNERS = "TELEGRAM_OWNER_IDS"
ENV_CHATS = "TELEGRAM_CHAT_ALLOWLIST"


def owner_ids_from_env(raw: str | None = None) -> frozenset[int]:
    """Parse ``TELEGRAM_OWNER_IDS`` ("42,43") into a set of ints.

    Unparsable entries are skipped silently only if *some* valid id remains;
    an unusable value yields an empty set, which the ACL then denies.
    """
    if raw is None:
        raw = os.environ.get(ENV_OWNERS, "")
    owners: set[int] = set()
    for chunk in str(raw).replace(";", ",").split(","):
        chunk = chunk.strip()
        if chunk.lstrip("-").isdigit():
            owners.add(int(chunk))
    return frozenset(owners)


def chat_allowlist_from_env(raw: str | None = None) -> frozenset[int]:
    """Parse ``TELEGRAM_CHAT_ALLOWLIST`` ("-100123,-100456") into chat ids.

    Gate G2: the **live** transport may only post to chats on this list, and an
    empty list denies every chat (fail closed) — a mis-configured deployment
    must not broadcast into the wrong group.
    """
    if raw is None:
        raw = os.environ.get(ENV_CHATS, "")
    chats: set[int] = set()
    for chunk in str(raw).replace(";", ",").split(","):
        chunk = chunk.strip()
        if chunk.lstrip("-").isdigit():
            chats.add(int(chunk))
    return frozenset(chats)


class ACL:
    """Owner allowlist + destructive-confirmation gate."""

    def __init__(self, owners: Iterable[int] = ()):
        self.owners = frozenset(int(o) for o in owners)

    @classmethod
    def from_env(cls, raw: str | None = None) -> "ACL":
        return cls(owner_ids_from_env(raw))

    @property
    def configured(self) -> bool:
        return bool(self.owners)

    def authorize(self, action: Action) -> None:
        """Raise :class:`AccessDenied` / :class:`ConfirmationRequired` on refusal."""
        if action.verb in LOCAL_VERBS:
            return

        if not self.owners:
            raise AccessDenied(
                "no owners configured — fail closed (set TELEGRAM_OWNER_IDS in .env)"
            )
        if action.actor is None:
            raise AccessDenied(f"verb '{action.verb}' requires an actor id (--actor)")
        if action.actor not in self.owners:
            raise AccessDenied(f"actor {action.actor} is not on the owner allowlist")

        if action.destructive() and not action.confirm:
            detail = _destructive_detail(action)
            raise ConfirmationRequired(
                f"destructive action requires --confirm ({detail})"
            )


def _destructive_detail(action: Action) -> str:
    verb = getattr(action, "verb", "")
    if verb == "topic":
        return "deleting a topic wipes every message inside it"
    if verb == "delete":
        return f"bulk delete of {len(getattr(action, 'message_ids', []))} messages"
    return verb
