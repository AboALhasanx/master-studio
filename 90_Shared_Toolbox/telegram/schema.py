"""Pydantic action schema — the single contract between agents and Telegram.

Every gateway invocation is first shaped into a JSON-ish dict and validated by
:func:`parse_action`. Nothing touches the network before validation succeeds
(roadmap gate G1, issues #15/#16).

Verbs
-----
``publish``  send text/file into a topic (issue #11)
``topic``    create / rename / close / reopen / delete topics (issue #10)
``reply``    reply to a message addressed by link or id (issue #12)
``forward``  re-post a message keeping the original sender (issue #11)
``copy``     re-post a message as our own, optionally re-captioned (issue #11)
``edit``     edit an existing message: text or caption (issue #12)
``delete``   delete one or many messages (issue #12)
``pin``      pin / unpin a message, or unpin a whole topic (issue #12)
``react``    add a reaction (issue #12)
``action``   transient presence signal — typing, upload_document ... (issue #12)
``queue``    inspect / drain the local job queue (issue #14)
``pipeline`` export a vault file if it is stale, then publish it (issue #13)
``quiz``     publish a deep link into the existing Flask quiz engine (issue #18)
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
    "ForwardAction",
    "CopyAction",
    "EditAction",
    "DeleteAction",
    "PinAction",
    "ReactAction",
    "ChatAction",
    "QueueAction",
    "StructureAction",
    "PipelineAction",
    "QuizAction",
    "StatusAction",
    "parse_action",
]

VERBS = (
    "publish", "topic", "reply", "forward", "copy", "edit", "delete", "pin",
    "react", "action", "queue", "structure", "pipeline", "quiz", "status",
)

#: The Bot API's ``sendChatAction`` vocabulary, verbatim (issue #12).
CHAT_ACTIONS = (
    "typing",
    "upload_photo",
    "record_video",
    "upload_video",
    "record_voice",
    "upload_voice",
    "upload_document",
    "find_location",
    "record_video_note",
    "upload_video_note",
    "choose_sticker",
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
    #: 2-10 uploads posted as ONE album (Telegram ``sendMediaGroup``, #11).
    files: list[str] = Field(default_factory=list)
    caption: str | None = None  # media caption (issue #11)
    parse_mode: Literal["HTML"] | None = None  # rich text for text/caption (issue #11)
    #: Which ``send*`` method carries the file (issue #11). The default is
    #: ``document`` — a byte-exact upload — because Telegram recompresses
    #: anything that goes through ``sendPhoto``.
    kind: Literal["document", "photo", "video", "audio", "voice",
                  "animation", "sticker", "auto"] = "document"
    buttons: list[Button] = Field(default_factory=list)
    reply_to: int | None = None  # anchor to an already-published message

    @model_validator(mode="after")
    def _exactly_one_payload(self) -> "PublishAction":
        if self.files:
            if self.text is not None or self.file is not None:
                raise ValueError("publish: 'files' cannot be combined with 'text' or 'file'")
            if not 2 <= len(self.files) <= 10:
                raise ValueError("media group needs 2-10 files (Telegram sendMediaGroup)")
            if self.kind == "document":
                # the default is byte-exact; an album of documents buys nothing
                # over separate sends, so picking a shape has to be deliberate
                raise ValueError(
                    "media group needs an explicit --kind: auto (type from each "
                    "file's suffix) or photo/video/audio/document"
                )
            if self.kind in {"voice", "animation", "sticker"}:
                raise ValueError("media groups accept only photo/video/audio/document")
            if self.buttons:
                raise ValueError("media groups cannot carry buttons")
        elif (self.text is None) == (self.file is None):
            raise ValueError("publish needs exactly one of: 'text', 'file'")
        if self.caption is not None and not (self.file or self.files):
            raise ValueError("caption requires a 'file' payload")
        if self.parse_mode is not None and not (self.text or self.caption):
            raise ValueError("parse_mode requires 'text' or 'caption'")
        if not (self.file or self.files) and self.kind != "document":
            raise ValueError("publish 'kind' requires a 'file' payload")
        if self.kind == "sticker" and self.caption is not None:
            raise ValueError("stickers do not carry a caption")
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


class ForwardAction(Action):
    """Re-post somebody else's message into a topic (issue #11).

    ``forwardMessage`` keeps the original sender attached — that is the whole
    point of forwarding, and it is also why the link alone is enough: nothing
    is written to the source chat, so the allowlist gate (D8) stays on the
    destination.
    """

    verb: Literal["forward"] = "forward"
    target: Target
    source: str = Field(min_length=1)  # t.me link or bare message id
    source_chat: int | None = None  # explicit from_chat_id (bare id / cross-check)


class CopyAction(Action):
    """Re-post a message as if the bot had written it (issue #11).

    ``copyMessage`` drops the original attribution, so this is the verb for
    "put that announcement into the new topic". Unlike ``forward`` it can carry
    a replacement caption; leaving it out keeps whatever the original said.
    """

    verb: Literal["copy"] = "copy"
    target: Target
    source: str = Field(min_length=1)
    source_chat: int | None = None
    caption: str | None = None  # omitted => keep the original caption
    parse_mode: Literal["HTML"] | None = None

    @model_validator(mode="after")
    def _parse_mode_needs_caption(self) -> "CopyAction":
        if self.parse_mode is not None and self.caption is None:
            raise ValueError("parse_mode requires 'caption'")
        return self


class EditAction(Action):
    """Edit an existing message: ``editMessageText`` **or** ``editMessageCaption``.

    Which one is decided purely by which payload you supply (issue #12).
    """

    verb: Literal["edit"] = "edit"
    target: Target
    message_id: int = Field(gt=0)
    text: str | None = None  # editMessageText
    caption: str | None = None  # editMessageCaption
    parse_mode: Literal["HTML"] | None = None
    #: Inline URL buttons — `editMessageText` carries them as ``reply_markup``,
    #: which is the only way to repoint the keyboard of a message the Bot API
    #: refuses to delete (older than 48 hours).
    buttons: list[Button] = Field(default_factory=list)

    @model_validator(mode="after")
    def _exactly_one_payload(self) -> "EditAction":
        if (self.text is None) == (self.caption is None):
            raise ValueError("edit needs exactly one of: 'text', 'caption'")
        if self.parse_mode is not None and not (self.text or self.caption):
            raise ValueError("parse_mode requires 'text' or 'caption'")
        if self.buttons and self.caption is not None:
            raise ValueError(
                "buttons need a text edit: editMessageCaption has no keyboard"
            )
        return self


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
    message_id: int | None = None
    pinned: bool = True
    unpin_all: bool = False  # unpin every message in the topic (#10 / #12)

    @model_validator(mode="after")
    def _pin_shape(self) -> "PinAction":
        if self.unpin_all:
            if self.message_id is not None:
                raise ValueError("unpin_all does not take 'message_id'")
        elif self.message_id is None:
            raise ValueError("pin/unpin requires 'message_id'")
        elif self.message_id <= 0:
            raise ValueError("message_id must be positive")
        return self

    def destructive(self) -> bool:
        # One unpin is cheap; sweeping a whole topic is a bulk operation (ADR D7).
        return self.unpin_all


class ReactAction(Action):
    verb: Literal["react"] = "react"
    target: Target
    message_id: int = Field(gt=0)
    emoji: str = Field(min_length=1, max_length=16)


class ChatAction(Action):
    """Presence signal (``sendChatAction``) — "typing", "upload_document" ...

    Not persisted anywhere: Telegram discards it after a few seconds, so it
    exists purely to make the bot feel alive (issue #12, consumed by #17).
    """

    verb: Literal["action"] = "action"
    target: Target
    kind: str  # validated against CHAT_ACTIONS below

    @model_validator(mode="after")
    def _known_kind(self) -> "ChatAction":
        if self.kind not in CHAT_ACTIONS:
            raise ValueError(
                f"unknown chat action {self.kind!r} (expected one of: "
                f"{', '.join(CHAT_ACTIONS)})"
            )
        return self


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


class PipelineAction(Action):
    """Composite: export a vault file when stale, then publish it (issue #13)."""

    verb: Literal["pipeline"] = "pipeline"
    target: Target
    source: str = Field(min_length=1)  # vault-relative path, e.g. 03_Study_Notes/W01.md
    caption: str | None = None
    parse_mode: Literal["HTML"] | None = None

    @model_validator(mode="after")
    def _parse_mode_needs_a_caption(self) -> "PipelineAction":
        if self.parse_mode is not None and not self.caption:
            raise ValueError("pipeline parse_mode requires 'caption'")
        return self


class StatusAction(Action):
    verb: Literal["status"] = "status"


class QuizAction(Action):
    """Publish a deep link into the existing dashboard quiz engine (issue #18).

    Phase A of the MCQ bridge: the gateway only *composes the door*. Nothing
    here reads answers, results or the quiz JSON — the dashboard owns the
    engine, the shared schema and ``/api/quiz/submit``. Phase B (a native
    Telegram ``quiz`` poll) is deliberately **not** modelled, because poll
    answers require ``getUpdates`` ingestion (ADR D2/D4).
    """

    verb: Literal["quiz"] = "quiz"
    target: Target
    quiz_id: str = Field(min_length=1, max_length=128)
    title: str | None = Field(default=None, max_length=256)
    #: Host/port of the dashboards LAN address — the link has to be reachable
    #: from the phone that taps the button, not from the agent's machine.
    host: str = Field(default="127.0.0.1", min_length=1, max_length=255)
    port: int = Field(default=5000, gt=0, lt=65536)
    mode: Literal["exam", "study"] = "exam"
    shuffle: bool = False
    text: str | None = None  # override the generated caption entirely

    @model_validator(mode="after")
    def _no_path_separators(self) -> "QuizAction":
        # A separator here would publish a broken link and only fail once the
        # student tapped it — refuse at schema time instead.
        for bad in ("/", "?", "#", ".."):
            if bad in self.quiz_id:
                raise ValueError(f"quiz_id must not contain {bad!r}")
        return self


ActionUnion = Union[
    PublishAction,
    TopicAction,
    ReplyAction,
    ForwardAction,
    CopyAction,
    EditAction,
    DeleteAction,
    PinAction,
    ReactAction,
    ChatAction,
    QueueAction,
    StructureAction,
    PipelineAction,
    QuizAction,
    StatusAction,
]

_BY_VERB = {
    "publish": PublishAction,
    "topic": TopicAction,
    "reply": ReplyAction,
    "forward": ForwardAction,
    "copy": CopyAction,
    "edit": EditAction,
    "delete": DeleteAction,
    "pin": PinAction,
    "react": ReactAction,
    "action": ChatAction,
    "queue": QueueAction,
    "structure": StructureAction,
    "pipeline": PipelineAction,
    "quiz": QuizAction,
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
