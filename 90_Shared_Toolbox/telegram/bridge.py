"""Agent bridge — Pull model: the user talks to the agent through the bot.

The gateway is outbound-only (ADR D2). This module adds the smallest possible
**inbound** leg that keeps that promise: a **one-shot poll** the agent runs
when it runs (Windows workstation — no always-on service):

1. ``getUpdates`` once (bounded ``limit``), starting after the persisted
   ``update_offset`` — pending messages wait in Telegram until the agent polls.
2. Split into *addressed* vs *refused* with
   :func:`interactive.extract_mentions` (allowlist gate, fail closed).
3. Map each addressed mention to a **proposal** — a plan, never a send:

   * owner + ordinary text ......... ``note`` (the agent reads it later)
   * owner + ``/publish``|``/edit`` . ``urgent`` action proposal
   * owner + admin command ......... ``restricted`` (private-chat approval first)
   * non-owner ..................... ``denied`` (audited, never executed)

Hard rails (all fail-closed):

* **empty allowlist refuses before any network call** (exit 3 upstream);
* **non-owners are denied**, even for harmless text;
* **restricted actions never auto-run** — the proposal carries the
  :mod:`telegram.permissions` approval card instead of parameters;
* **offset advances past every seen update**, so a message is never handled
  twice — including denied ones (otherwise a stranger could wedge the queue).

The module is pure logic + one transport call and never touches the executor,
so a bug here cannot publish, delete, or pin anything by itself.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

from . import interactive
from .errors import GatewayError
from .permissions import RESTRICTED_VERBS

__all__ = [
    "BridgeProposal",
    "BridgeResult",
    "COMMAND_TO_VERB",
    "proposal_for_mention",
    "pull_once",
]

#: Owner ``/commands`` the bridge maps to urgent gateway verbs. Everything
#: else an owner writes is a ``note``; admin verbs from
#: :data:`interactive.ADMIN_VERBS` become ``restricted`` proposals.
COMMAND_TO_VERB = {
    "publish": "publish",
    "edit": "edit",
    "quiz": "quiz",
    "reply": "reply",
    "react": "react",
    "pin": "pin",
    "delete": "delete",
}


@dataclass
class BridgeProposal:
    """One inbound message turned into a plan."""

    update_id: int
    actor: int | None
    chat_id: int | None
    thread_id: int | None = None
    kind: str = "note"  # urgent | restricted | note | denied
    text: str = ""
    action: dict[str, Any] | None = None
    approval: dict[str, Any] | None = None
    raw: dict[str, Any] = field(default_factory=dict)

    def summary(self) -> dict[str, Any]:
        out: dict[str, Any] = {
            "update_id": self.update_id,
            "kind": self.kind,
            "actor": self.actor,
            "chat_id": self.chat_id,
        }
        if self.thread_id is not None:
            out["thread_id"] = self.thread_id
        if self.action is not None:
            out["action"] = self.action
        return out


@dataclass
class BridgeResult:
    """Outcome of one poll: proposals, refusals, and the next offset."""

    status: str  # ok | refused | error
    proposals: list[BridgeProposal] = field(default_factory=list)
    refused: list[interactive.Mention] = field(default_factory=list)
    next_offset: int = 0
    error: str | None = None

    def summary(self) -> dict[str, Any]:
        kinds: dict[str, int] = {}
        for proposal in self.proposals:
            kinds[proposal.kind] = kinds.get(proposal.kind, 0) + 1
        return {
            "status": self.status,
            "proposals": len(self.proposals),
            "kinds": kinds,
            "refused": len(self.refused),
            "next_offset": self.next_offset,
            "error": self.error,
        }


def proposal_for_mention(
    mention: interactive.Mention,
    *,
    owner_ids: frozenset[int] | set[int] = frozenset(),
) -> BridgeProposal:
    """Turn one addressed mention into a proposal (no network, no sends)."""
    owners = {int(o) for o in owner_ids}
    is_owner = mention.actor is not None and int(mention.actor) in owners
    if not is_owner:
        return BridgeProposal(
            update_id=mention.update_id,
            actor=mention.actor,
            chat_id=mention.chat_id,
            thread_id=mention.thread_id,
            kind="denied",
            text="non-owner — never executed",
            raw={"message_id": mention.message_id},
        )

    command = mention.command
    if command is None:
        return BridgeProposal(
            update_id=mention.update_id,
            actor=mention.actor,
            chat_id=mention.chat_id,
            thread_id=mention.thread_id,
            kind="note",
            text=mention.stripped,
            raw={"message_id": mention.message_id},
        )

    if command in interactive.ADMIN_VERBS:
        action = {"verb": command, "args": mention.args}
        return BridgeProposal(
            update_id=mention.update_id,
            actor=mention.actor,
            chat_id=mention.chat_id,
            thread_id=mention.thread_id,
            kind="restricted",
            text=f"طلب إداري `{command}` — بانتظار موافقة الجات الخاص.",
            action=action,
            approval={
                "text": (
                    "طلب موافقة — إجراء مقيّد\n\n"
                    f"الأمر: `{command}` {mention.args}\n"
                    f"الطالب: `{mention.actor}`\n\n"
                    "رد بـ `نعم` للتنفيذ أو `لا` للإلغاء."
                ),
                "kind": "restricted",
                "actor": mention.actor,
            },
            raw={"message_id": mention.message_id},
        )

    verb = COMMAND_TO_VERB.get(command)
    if verb is None:
        if mention.wants_help:
            return BridgeProposal(
                update_id=mention.update_id,
                actor=mention.actor,
                chat_id=mention.chat_id,
                thread_id=mention.thread_id,
                kind="note",
                text="help — رد بقائمة الأوامر",
                raw={"message_id": mention.message_id},
            )
        return BridgeProposal(
            update_id=mention.update_id,
            actor=mention.actor,
            chat_id=mention.chat_id,
            thread_id=mention.thread_id,
            kind="note",
            text=mention.stripped,
            raw={"message_id": mention.message_id},
        )

    target: dict[str, Any] = {"chat_id": mention.chat_id}
    if mention.thread_id is not None:
        target["thread_id"] = mention.thread_id
    action_dict: dict[str, Any] = {
        "verb": verb,
        "actor": mention.actor,
        "target": target,
        "args": mention.args,
    }
    # Single source of truth: the policy table in permissions.py decides
    # which verbs need a private-chat approval — never a second literal set.
    kind = "restricted" if verb in RESTRICTED_VERBS else "urgent"
    approval = None
    if kind == "restricted":
        approval = {
            "text": (
                "طلب موافقة — إجراء مقيّد\n\n"
                f"الإجراء: `{verb}` {mention.args}\n"
                f"الطالب: `{mention.actor}`\n\n"
                "رد بـ `نعم` للتنفيذ (مع `--confirm`) أو `لا` للإلغاء."
            ),
            "kind": "restricted",
            "actor": mention.actor,
        }
    return BridgeProposal(
        update_id=mention.update_id,
        actor=mention.actor,
        chat_id=mention.chat_id,
        thread_id=mention.thread_id,
        kind=kind,
        text=mention.args,
        action=action_dict,
        approval=approval,
        raw={"message_id": mention.message_id},
    )


def pull_once(
    transport,
    *,
    bot_username: str | None,
    allowed_chats: frozenset[int] | set[int] | None,
    owner_ids: frozenset[int] | set[int] = frozenset(),
    offset: int = 0,
    limit: int = 20,
) -> BridgeResult:
    """Poll ``getUpdates`` once and propose — never send.

    ``limit`` caps how many updates one poll may consider (the backlog beyond
    it waits for the next agent run — Pull, not Push). Returns ``refused``
    without touching the network when the allowlist is empty.
    """
    if not allowed_chats:
        return BridgeResult(
            status="refused",
            next_offset=int(offset),
            error="no chat allowlist configured — the bridge fails closed",
        )
    try:
        payload = transport.call("getUpdates", {
            "offset": int(offset) + 1,
            "timeout": 0,
            "limit": max(1, min(int(limit), 100)),
            "allowed_updates": json.dumps(["message", "edited_message"]),
        })
    except GatewayError as exc:
        return BridgeResult(status="error", next_offset=int(offset), error=str(exc))

    batch = list(interactive._iter_updates(payload))
    if not batch:
        return BridgeResult(status="ok", next_offset=int(offset))

    addressed, refused_batch, cursor = interactive.extract_mentions(
        batch, bot_username=bot_username, allowed_chats=allowed_chats,
        min_update_id=int(offset) + 1,
    )
    proposals = [
        proposal_for_mention(mention, owner_ids=owner_ids)
        for mention in addressed
    ]
    # Belt and suspenders: extract_mentions already advances past every
    # update it saw, but a batch of only non-addressed messages (plain chat
    # with no mention) would otherwise leave the cursor behind and re-fetch
    # forever — advance past the batch's own max update_id too.
    batch_max = cursor
    for update in batch:
        uid = update.get("update_id") if isinstance(update, dict) else None
        if isinstance(uid, int):
            batch_max = max(batch_max, uid)
    return BridgeResult(
        status="ok",
        proposals=proposals,
        refused=refused_batch,
        next_offset=int(batch_max),
    )
