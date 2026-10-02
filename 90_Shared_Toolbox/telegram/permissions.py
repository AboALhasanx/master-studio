"""Permission model — urgent vs. restricted (agent bridge, ADR D16 companion).

The gateway's hard gate stays in :mod:`telegram.acl` (owner allowlist +
destructive ``--confirm``). This module is the *policy* layer the agent bridge
uses to decide **how** an owner request travels:

* **urgent** — executes immediately (single-message, reversible or
  append-only): publish a file, edit a card in place, reply, react ...
* **restricted** — never executes on first sight. The bot sends an approval
  request to the private chat; the owner replies "yes" (or taps approve) and
  only then does the agent run the verb with ``--confirm``.

Rules
-----
1. Anything :meth:`Action.destructive` reports is restricted, no exceptions.
2. ``topic`` / ``delete`` / ``pin`` / ``structure`` are always restricted —
   they rewrite group state irreversibly (topic delete wipes every message
   inside; a delete past 48 h cannot be undone by re-posting the same id).
3. Everything else from an owner is urgent.
4. Requests from non-owners are neither — the bridge marks them ``denied``.

Approval replies accept Iraqi/Arabic/English affirmatives
(``نعم``, ``موافق``, ``اي``, ``yes``, ``approve`` ...) and negatives
(``لا``, ``لاا``, ``no``, ``reject``, ``رفض`` ...). Anything else is ``None``
(not a decision — keep waiting).
"""

from __future__ import annotations

from typing import Any

from .schema import Action

__all__ = [
    "URGENT_VERBS",
    "RESTRICTED_VERBS",
    "classify",
    "needs_approval",
    "format_approval_request",
    "parse_approval_reply",
    "APPROVE_WORDS",
    "REJECT_WORDS",
]

#: Verbs that rewrite group state — always go through the private-chat approval.
RESTRICTED_VERBS = frozenset({"topic", "delete", "pin", "structure"})

#: Everything else an owner may ask for runs immediately.
URGENT_VERBS = frozenset({
    "publish", "reply", "forward", "copy", "edit",
    "react", "action", "queue", "pipeline", "quiz", "status",
})

APPROVE_WORDS = frozenset({
    "نعم", "موافق", "اي", "إي", "تمام", "اكيد", "أكيد",
    "yes", "y", "approve", "approved", "ok", "okay", "confirm",
})

REJECT_WORDS = frozenset({
    "لا", "لأ", "رفض", "مرفوض", "الغي", "ألغي", "cancel",
    "no", "n", "reject", "rejected", "deny", "denied",
})


def classify(action: Action) -> str:
    """Return ``"urgent"`` or ``"restricted"`` for an owner action.

    Destructive actions are restricted even when their verb is otherwise
    urgent — :meth:`Action.destructive` is the load-bearing check, the verb
    table is the default.
    """
    if action.destructive():
        return "restricted"
    if action.verb in RESTRICTED_VERBS:
        return "restricted"
    return "urgent"


def needs_approval(action: Action) -> bool:
    """True when the action must wait for a private-chat approval."""
    return classify(action) == "restricted"


def _describe(action: Action) -> str:
    """One-line Arabic description of the proposed action for the approval card."""
    verb = getattr(action, "verb", "?")
    target = getattr(action, "target", None)
    where = ""
    if target is not None:
        subject = getattr(target, "subject", None)
        thread = getattr(target, "thread_id", None)
        chat = getattr(target, "chat_id", None)
        if subject:
            where = f" — المادة `{subject}`"
        elif thread is not None:
            where = f" — توبيك `{thread}`"
        elif chat is not None:
            where = f" — جات `{chat}`"
    extra = ""
    if verb == "topic":
        extra = f" (عملية: `{getattr(action, 'op', '?')}`)"
    elif verb == "delete":
        ids = getattr(action, "message_ids", []) or []
        extra = f" ({len(ids)} رسالة)"
    elif verb == "edit":
        extra = f" (رسالة `{getattr(action, 'message_id', '?')}`)"
    elif verb == "pin":
        if getattr(action, "unpin_all", False):
            extra = " (فك تثبيت الكل)"
        else:
            extra = f" (رسالة `{getattr(action, 'message_id', '?')}`)"
    return f"`{verb}`{extra}{where}"


def format_approval_request(
    action: Action,
    *,
    actor: int | None = None,
    chat_id: int | None = None,
) -> dict[str, Any]:
    """Build the private-chat approval card for a restricted action.

    Returns a plain dict (no network): ``{"text": ..., "action": ..., ...}``.
    The caller sends ``text`` to the owner's private chat; the owner's reply
    is later fed to :func:`parse_approval_reply`.
    """
    lines = [
        "طلب موافقة — إجراء مقيّد",
        "",
        f"الإجراء: {_describe(action)}",
    ]
    if actor is not None:
        lines.append(f"الطالب: `{actor}`")
    if chat_id is not None:
        lines.append(f"الجات المستهدف: `{chat_id}`")
    lines += [
        "",
        "رد بـ `نعم` للتنفيذ (مع `--confirm`) أو `لا` للإلغاء.",
    ]
    return {
        "text": "\n".join(lines),
        "action": action.model_dump(mode="json"),
        "kind": "restricted",
        "actor": actor,
    }


def parse_approval_reply(text: str | None) -> bool | None:
    """Parse an owner's approval reply: True / False / None (not a decision)."""
    if not text or not text.strip():
        return None
    norm = text.strip().lower()
    # Strip common punctuation / quotes the mobile keyboard adds.
    norm = norm.strip(" \t\n\r\"'“”‘’`.,!؟?ـ")
    if norm in APPROVE_WORDS:
        return True
    if norm in REJECT_WORDS:
        return False
    return None
