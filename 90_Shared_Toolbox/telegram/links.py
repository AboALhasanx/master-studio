"""Message-link parsing — how the gateway targets a message without reading
the group (outbound-only doctrine: the agent supplies the link).

Supported forms::

    https://t.me/c/1234567890/42     private supergroup (chat id -1001234567890)
    https://t.me/master_studio/42    public username + message id
    t.me/... / http://t.me/...       scheme optional
    "42"                             bare message id (chat comes from target)

Issue #12.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .errors import ActionValidationError

__all__ = ["MessageRef", "parse_message_link"]

_PRIVATE_RE = re.compile(
    r"^(?:https?://)?t\.me/c/(?P<chat>\d{6,})/(?P<message>\d+)(?:\?.*)?(?:#.*)?$"
)
_USERNAME_RE = re.compile(
    r"^(?:https?://)?t\.me/(?P<username>[A-Za-z][A-Za-z0-9_]{4,})/(?P<message>\d+)(?:\?.*)?(?:#.*)?$"
)
_BARE_RE = re.compile(r"^\d+$")


@dataclass(frozen=True)
class MessageRef:
    """Resolved reference to an existing message."""

    message_id: int
    chat_id: int | None = None  # set for t.me/c links (-100 + value)
    username: str | None = None


def parse_message_link(raw: str) -> MessageRef:
    """Parse a Telegram message link (or bare id) into a :class:`MessageRef`.

    Raises :class:`ActionValidationError` when the input identifies nothing.
    """
    value = (raw or "").strip()
    if not value:
        raise ActionValidationError("empty message link")

    match = _PRIVATE_RE.match(value)
    if match:
        # t.me/c/<internal chat id>/<message id> -> full supergroup id
        chat_id = int("-100" + match.group("chat"))
        return MessageRef(message_id=int(match.group("message")), chat_id=chat_id)

    match = _USERNAME_RE.match(value)
    if match:
        return MessageRef(
            message_id=int(match.group("message")), username=match.group("username")
        )

    if _BARE_RE.match(value):
        return MessageRef(message_id=int(value))

    raise ActionValidationError(
        f"unrecognised message link: {value!r} (expected t.me/c/<chat>/<id>, "
        "t.me/<username>/<id>, or a numeric message id)"
    )
