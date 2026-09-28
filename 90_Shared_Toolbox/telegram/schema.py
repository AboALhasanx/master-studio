"""Pydantic action schema — the single contract between agents and Telegram.

Every gateway invocation is first shaped into a JSON-ish dict and validated by
:func:`parse_action`. Nothing touches the network before validation succeeds
(roadmap gate G1, issues #15/#16).

Verbs
-----
``publish``  send text/file into a topic (issue #11)
``topic``    create / rename / close / reopen / delete topics (issue #10)
``reply``    reply to a message addressed by link or id (issue #12)
``edit``     edit an existing message (issue #12)
``delete``   delete one or many messages (issue #12)
``pin``      pin / unpin a message (issue #12)
``react``    add a reaction (issue #12)
``queue``    inspect / drain the local job queue (issue #14)
``status``   local health report — no Telegram target at all
"""

from __future__ import annotations

import hashlib
import json
from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from .errors import ActionValidationError

__all__ = [
    "VERBS",
    "Button",
    "Target",
    "Action",
    "PublishAction",
    "TopicAction",
    "ReplyAction",
    "EditAction",
    "DeleteAction",
    "PinAction",
    "ReactAction",
    "QueueAction",
    "StructureAction",
    "StatusAction",
    "parse_action",
]

VERBS = (
    "publish", "topic", "reply", "edit", "delete", "pin", "react",
    "queue", "structure", "status",
)


class _Base(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Button(_Base):
    """Inline keyboard button (URL / Mini App deep link)."""

    label: str = Field(min_length=1, max_length=64)
    url: str = Field(min_length=1, max_length=1024)


class Target(_Base):
    """Where an action lands.

    ``subject`` is resolved through the topic registry (preferred: the agent
    speaks "01-Cyber-Security", never raw ids). ``chat_id``/``thread_id`` allow
    explicit addressing, which the registry bootstrap at G2/G5 uses.
    """

    subject: str | None = None
    chat_id: int | None = None
    thread_id: int | None = None

    @model_validator(mode="after")
    def _needs_a_destination(self) -> "Target":
        if self.subject is None and self.chat_id is None:
            raise ValueError("target requires 'subject' or 'chat_id'")
        return self


class Action(_Base):
    """Common envelope shared by every verb."""

    verb: str
    actor: int | None = None  # Telegram user id driving the command (issue #16)
    confirm: bool = False  # gate for destructive verbs (ADR D7)

    def destructive(self) -> bool:
        """True when the action can destroy data irreversibly."""
        return False


class PublishAction(Action):
    verb: Literal["publish"] = "publish"
    target: Target
    text: str | None = None
    file: str | None = None
    caption: str | None = None  # media caption (issue #11)
    parse_mode: Literal["HTML"] | None = None  # rich text for text/caption (issue #11)
    buttons: list[Button] = Field(default_factory=list)
    reply_to: int | None = None  # anchor to an already-published message

    @model_validator(mode="after")
    def _exactly_one_payload(self) -> "PublishAction":
        if (self.text is None) == (self.file is None):
            raise ValueError("publish needs exactly one of: 'text', 'file'")
        if self.caption is not None and self.file is None:
            raise ValueError("caption requires a 'file' payload")
        if self.parse_mode is not None and not (self.text or self.caption):
            raise ValueError("parse_mode requires 'text' or 'caption'")
        return self


class TopicAction(Action):
    verb: Literal["topic"] = "topic"
    target: Target
    op: Literal["create", "rename", "close", "reopen", "delete"]
    name: str | None = None
    icon_color: int | None = None  # fixed at creation; cannot be changed later

    @model_validator(mode="after")
    def _op_rules(self) -> "TopicAction":
        if self.op in ("create", "rename") and not self.name:
            raise ValueError(f"topic op '{self.op}' requires 'name'")
        if self.op != "create" and self.target.thread_id is None and self.target.subject is None:
            raise ValueError(f"topic op '{self.op}' requires 'subject' or 'thread_id'")
        return self

    def destructive(self) -> bool:
        # Deleting a topic wipes every message inside it (ADR D7).
        return self.op == "delete"


class ReplyAction(Action):
    verb: Literal["reply"] = "reply"
    target: Target
    to: str = Field(min_length=1)  # t.me link or bare message id (issue #12)
    text: str = Field(min_length=1)


class EditAction(Action):
    verb: Literal["edit"] = "edit"
    target: Target
    message_id: int = Field(gt=0)
    text: str = Field(min_length=1)


class DeleteAction(Action):
    verb: Literal["delete"] = "delete"
    target: Target
    message_ids: list[int] = Field(min_length=1)

    @model_validator(mode="after")
    def _positive_ids(self) -> "DeleteAction":
        if any(mid <= 0 for mid in self.message_ids):
            raise ValueError("message_ids must be positive")
        return self

    def destructive(self) -> bool:
        # A single delete stays cheap; bulk delete must be confirmed.
        return len(self.message_ids) > 1


class PinAction(Action):
    verb: Literal["pin"] = "pin"
    target: Target
    message_id: int = Field(gt=0)
    pinned: bool = True


class ReactAction(Action):
    verb: Literal["react"] = "react"
    target: Target
    message_id: int = Field(gt=0)
    emoji: str = Field(min_length=1, max_length=16)


class QueueAction(Action):
    verb: Literal["queue"] = "queue"
    op: Literal["list", "run", "pending"] = "list"
    limit: int = Field(default=50, ge=1, le=500)


class StructureAction(Action):
    """Composite: provision the whole group layout (issues #8/#10/#19)."""

    verb: Literal["structure"] = "structure"
    target: Target
    cards: bool = True  # pinned brief card per topic
    index: bool = True  # pinned index message in General with topic buttons
    only: list[str] = Field(default_factory=list)  # subset of subject keys


class StatusAction(Action):
    verb: Literal["status"] = "status"


ActionUnion = Union[
    PublishAction,
    TopicAction,
    ReplyAction,
    EditAction,
    DeleteAction,
    PinAction,
    ReactAction,
    QueueAction,
    StructureAction,
    StatusAction,
]

_BY_VERB = {
    "publish": PublishAction,
    "topic": TopicAction,
    "reply": ReplyAction,
    "edit": EditAction,
    "delete": DeleteAction,
    "pin": PinAction,
    "react": ReactAction,
    "queue": QueueAction,
    "structure": StructureAction,
    "status": StatusAction,
}


def parse_action(data: object) -> Action:
    """Validate a raw dict into a typed action.

    Raises :class:`ActionValidationError` (CLI exit 2) on any mismatch — the
    caller must treat that as "nothing executed".
    """
    if not isinstance(data, dict):
        raise ActionValidationError("action must be a JSON object")
    verb = data.get("verb")
    if verb not in _BY_VERB:
        known = ", ".join(VERBS)
        raise ActionValidationError(f"unknown verb {verb!r} (expected one of: {known})")
    try:
        return _BY_VERB[verb].model_validate(data)
    except ValidationError as exc:  # pragma: no cover - message asserted in tests
        raise ActionValidationError(str(exc)) from exc


def idempotency_key(action: Action) -> str:
    """Stable key so re-running a command never double-posts (issue #14).

    ``actor`` and ``confirm`` are metadata about *who* asked, not *what* is
    asked, so they must not change the key: retrying with the same intent has
    to collide with the original job.
    """
    payload = action.model_dump(mode="json", exclude={"actor", "confirm"})
    canonical = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:32]
