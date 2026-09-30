"""Interactive layer — **mention-driven replies, on demand** (ADR D15).

The gateway has always been outbound-only (ADR D2). This module adds the
smallest possible inbound capability: a **one-shot listening session** that
reads new updates for a bounded window, picks out the ones that actually
address the bot, and replies to them through the existing outbound path.

It deliberately does **not** run a persistent ``getUpdates`` loop:

* no always-on service,
* no reading the whole group,
* only what arrived between the session opening and its deadline.

Hard rails (all fail-closed):

* **allowlist required** — no ``TELEGRAM_CHAT_ALLOWLIST`` means the session
  refuses to open at all (an empty allowlist denies every chat).
* **bounded** — ``--for <seconds>`` and ``--max <n>``; a session cannot run
  forever or drain an unbounded backlog.
* **offset persisted** — the last processed ``update_id`` lives in the gateway
  memory folder, so a message is never handled twice and never lost.
* **administrative verbs never auto-run** — anything destructive becomes a
  *pending approval* for the admin (ADR D16), never an immediate action.

The module is pure logic + one transport call. It has no dependency on the
executor, so a bug here cannot corrupt publishing.
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

from .errors import GatewayError, TransportError
from .transport import Transport

__all__ = [
    "Mention",
    "SessionLimits",
    "ListenResult",
    "extract_mentions",
    "build_reply",
    "run_session",
    "PENDING_APPROVAL_PATH",
    "ADMIN_VERBS",
]

_REPO_ROOT = Path(__file__).resolve().parents[2]
#: Pending admin approvals live with the gateway's own memory (D14/D16).
PENDING_APPROVAL_PATH = _REPO_ROOT / "00_STUDIO_HUB" / "telegram" / "pending_approval.json"

#: Verbs that an incoming message may *request* but never auto-execute (D16).
ADMIN_VERBS = frozenset(
    {"delete", "pin", "unpin", "unpin-all", "close", "reopen", "topic-delete", "ban"}
)

#: Words that, when they are the whole message, mean "help".
_HELP_WORDS = frozenset({"help", "مساعدة", "مساعدة؟", "؟", "?"})

#: A conservative command shape: ``/verb`` optionally followed by args.
_COMMAND_RE = re.compile(r"^/(?P<verb>[a-zA-Z][\w-]*)\s*(?P<args>.*)$")


@dataclass(frozen=True)
class SessionLimits:
    """Bounds for one listening session — both are required to be finite."""

    seconds: float = 60.0
    max_messages: int = 20

    def __post_init__(self) -> None:  # noqa: D105
        if self.seconds <= 0:
            raise ValueError("session seconds must be > 0")
        if self.max_messages <= 0:
            raise ValueError("session max_messages must be > 0")


@dataclass
class Mention:
    """One incoming message that addresses the bot."""

    update_id: int
    message_id: int | None
    chat_id: int | None
    actor: int | None
    text: str
    thread_id: int | None = None
    reply_to: int | None = None
    raw: dict[str, Any] = field(default_factory=dict)

    @property
    def stripped(self) -> str:
        """The message with a leading ``@bot`` mention removed.

        ``@cs_mscbot help`` and ``help`` mean the same thing to the bot, so the
        mention has to come off before any intent check.
        """
        return re.sub(r"^\s*@\w+\s*", "", self.text.strip())

    @property
    def command(self) -> str | None:
        """The ``/verb`` at the start of the message, if any (lower-cased)."""
        match = _COMMAND_RE.match(self.stripped)
        return match.group("verb").lower() if match else None

    @property
    def args(self) -> str:
        match = _COMMAND_RE.match(self.stripped)
        return (match.group("args") or "").strip() if match else ""

    @property
    def wants_help(self) -> bool:
        return self.stripped.lower() in _HELP_WORDS or self.command == "help"


@dataclass
class ListenResult:
    """Outcome of one session: what was seen, what was answered, what awaits."""

    status: str
    seen: list[Mention] = field(default_factory=list)
    replied: int = 0
    queued_approval: int = 0
    refused: list[Mention] = field(default_factory=list)
    next_offset: int = 0
    error: str | None = None

    def summary(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "seen": len(self.seen),
            "replied": self.replied,
            "queued_approval": self.queued_approval,
            "refused": len(self.refused),
            "next_offset": self.next_offset,
            "error": self.error,
        }


# ------------------------------------------------------------------ parsing
def _iter_updates(payload: Any) -> Iterable[dict[str, Any]]:
    if isinstance(payload, list):
        for item in payload:
            if isinstance(item, dict):
                yield item
    elif isinstance(payload, dict):
        # some callers may hand back {"result": [...]}
        for item in payload.get("result", []) or []:
            if isinstance(item, dict):
                yield item


def _message_from_update(update: dict[str, Any]) -> dict[str, Any] | None:
    msg = update.get("message") or update.get("edited_message")
    if not isinstance(msg, dict):
        return None
    return msg


def _text_of(msg: dict[str, Any]) -> str:
    return str(msg.get("text") or msg.get("caption") or "")


def _bot_mentioned(msg: dict[str, Any], bot_username: str | None, entities_key: str = "entities") -> bool:
    """True if the message @-mentions the bot, or is a command for it."""
    text = _text_of(msg)
    if text.lstrip().startswith("/"):
        return True
    if not bot_username:
        return False
    needle = f"@{bot_username.lstrip('@').lower()}"
    if needle in text.lower():
        return True
    for ent in msg.get(entities_key, []) or []:
        if not isinstance(ent, dict):
            continue
        if ent.get("type") == "mention":
            chunk = text[ent.get("offset", 0): ent.get("offset", 0) + ent.get("length", 0)]
            if chunk.lower() == needle:
                return True
    return False


def extract_mentions(
    updates: Iterable[dict[str, Any]],
    *,
    bot_username: str | None = None,
    allowed_chats: frozenset[int] | set[int] | None = None,
    min_update_id: int = 0,
) -> tuple[list[Mention], list[Mention], int]:
    """Split updates into ``(addressed, refused, highest_update_id_seen)``.

    ``addressed`` are mentions/commands inside an allow-listed chat;
    ``refused`` are mentions from chats off the allowlist (kept so the caller
    can audit them). ``min_update_id`` filters already-processed updates.
    """
    allowed = None if allowed_chats is None else {int(c) for c in allowed_chats}
    addressed: list[Mention] = []
    refused: list[Mention] = []
    highest = min_update_id

    for update in updates:
        uid = update.get("update_id")
        if isinstance(uid, int):
            highest = max(highest, uid)
        else:
            continue
        if uid < min_update_id:
            continue
        msg = _message_from_update(update)
        if msg is None:
            continue
        if not (_bot_mentioned(msg, bot_username) or _bot_mentioned(msg, bot_username, "caption_entities")):
            continue
        chat = msg.get("chat") or {}
        chat_id = chat.get("id")
        sender = msg.get("from") or {}
        mention = Mention(
            update_id=uid,
            message_id=msg.get("message_id"),
            chat_id=chat_id,
            actor=sender.get("id"),
            text=_text_of(msg),
            thread_id=msg.get("message_thread_id"),
            reply_to=(msg.get("reply_to_message") or {}).get("message_id"),
            raw=msg,
        )
        if allowed is not None and (chat_id is None or int(chat_id) not in allowed):
            refused.append(mention)
        else:
            addressed.append(mention)
    return addressed, refused, highest


# ------------------------------------------------------------------- replies
def build_reply(
    mention: Mention,
    *,
    owner_ids: frozenset[int] | set[int] = frozenset(),
    subject_hint: str | None = None,
) -> dict[str, Any]:
    """Decide the bot's response to one mention — a *plan*, not a send.

    Returns a small dict the caller turns into a Bot API call::

        {"action": "reply", "text": "..."}            # plain answer
        {"action": "approval", "text": "..."}         # admin action awaits
        {"action": "ignore"}                          # nothing to say

    The bot's competence is intentionally narrow (see the architecture doc):
    help, greetings, and a pointer to the subject materials. **It never runs a
    command from message text** — administrative requests only ever become an
    approval item (ADR D16).
    """
    owners = {int(o) for o in owner_ids}
    is_owner = mention.actor is not None and int(mention.actor) in owners

    if mention.wants_help:
        return {"action": "reply", "text": _help_text()}

    command = mention.command
    if command is not None:
        if command in ADMIN_VERBS:
            # never auto-run — the owner must approve (D16)
            return {
                "action": "approval",
                "text": f"طلب إداري `{command}` — بانتظار موافقة الأدمن.",
            }
        return {"action": "reply", "text": _unknown_command_text(command)}

    if subject_hint:
        return {
            "action": "reply",
            "text": f"لقيت سؤالك عن `{subject_hint}` — تريد رابط المادة، ولا شرح مختصر؟",
        }

    return {
        "action": "reply",
        "text": "هلا! أنا بوت المواد — اكتب /help تشوف شنو أقدر أسوي.",
    }


def _help_text() -> str:
    return (
        "أهلاً 👋\n"
        "أقدر أساعدك بـ:\n"
        "• /help — هذه القائمة\n"
        "• سؤال عن مادة → أدلّك على الرابط\n"
        "• الأوامر الإدارية (حذف/تثبيت) تمرّ بموافقة الأدمن\n"
        "اكتب سؤالك بشكل عادي وسأرد."
    )


def _unknown_command_text(command: str) -> str:
    return f"ما أعرف الأمر `/{command}` — اكتب /help تشوف المتاح."


# ------------------------------------------------------------------- session
def _record_refusals(refused: list[Mention], audit) -> None:
    for mention in refused:
        if audit is not None:
            audit("interactive", "denied", actor=mention.actor, chat_id=mention.chat_id,
                  detail=f"chat not allow-listed (update {mention.update_id})")


def _record_approval(path: Path, mention: Mention, plan: dict[str, Any]) -> None:
    """Append an admin request to the pending-approval ledger (D16)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
            items = existing if isinstance(existing, list) else []
        except (OSError, json.JSONDecodeError):
            items = []
    else:
        items = []
    items.append({
        "ts": time.time(),
        "update_id": mention.update_id,
        "actor": mention.actor,
        "chat_id": mention.chat_id,
        "message_id": mention.message_id,
        "command": mention.command,
        "args": mention.args,
        "text": plan.get("text"),
    })
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def run_session(
    transport: Transport,
    *,
    bot_username: str | None,
    allowed_chats: frozenset[int] | set[int] | None,
    owner_ids: frozenset[int] | set[int] = frozenset(),
    limits: SessionLimits | None = None,
    offset: int = 0,
    now: Any = time.time,
    sleep: Any = time.sleep,
    audit=None,
    approval_path: Path | None = None,
    subject_hint: str | None = None,
) -> ListenResult:
    """Read updates once, reply to the addressed ones, then stop.

    ``offset`` is the last processed ``update_id`` (exclusive lower bound);
    callers persist ``result.next_offset`` back to the gateway memory. The
    session never exceeds ``limits`` and never raises on a refused chat — a
    refusal is logged, not fatal.
    """
    limits = limits or SessionLimits()
    if not allowed_chats:
        return ListenResult(
            status="refused", next_offset=offset,
            error="no chat allowlist configured — the interactive layer fails closed",
        )

    deadline = float(now()) + limits.seconds
    seen: list[Mention] = []
    refused: list[Mention] = []
    replied = 0
    queued = 0
    cursor = int(offset)
    approval_path = approval_path or PENDING_APPROVAL_PATH

    while int(now()) < deadline and len(seen) < limits.max_messages:
        try:
            payload = transport.call("getUpdates", {
                "offset": cursor + 1,
                "timeout": 0,
                "allowed_updates": json.dumps(["message", "edited_message"]),
            })
        except GatewayError as exc:
            return ListenResult(status="error", seen=seen, refused=refused,
                                replied=replied, queued_approval=queued,
                                next_offset=cursor, error=str(exc))

        batch = list(_iter_updates(payload))
        if not batch:
            # nothing new — back off briefly so we do not hot-loop
            sleep(min(2.0, max(0.0, deadline - float(now()))))
            if float(now()) >= deadline:
                break
            continue

        addressed, refused_batch, cursor = extract_mentions(
            batch, bot_username=bot_username, allowed_chats=allowed_chats,
            min_update_id=cursor + 1,
        )
        seen.extend(addressed)
        refused.extend(refused_batch)

        for mention in addressed:
            plan = build_reply(mention, owner_ids=owner_ids, subject_hint=subject_hint)
            if plan.get("action") == "ignore":
                continue
            if plan.get("action") == "approval":
                _record_approval(approval_path, mention, plan)
                queued += 1
            params: dict[str, Any] = {"chat_id": mention.chat_id, "text": plan["text"]}
            if mention.thread_id is not None:
                params["message_thread_id"] = mention.thread_id
            if mention.message_id is not None:
                params["reply_to_message_id"] = mention.message_id
            try:
                transport.call("sendMessage", params)
                replied += 1
            except GatewayError as exc:
                if audit is not None:
                    audit("interactive", "error", actor=mention.actor,
                          chat_id=mention.chat_id, detail=str(exc))

    _record_refusals(refused, audit)
    return ListenResult(
        status="ok", seen=seen, refused=refused, replied=replied,
        queued_approval=queued, next_offset=cursor,
    )
