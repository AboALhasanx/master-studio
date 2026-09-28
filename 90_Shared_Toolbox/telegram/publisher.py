"""Publishing primitives: safe escaping and API-length chunking (issue #11).

Telegram's ``sendMessage``/``sendCaption`` reject anything past 4096 characters,
and a naive slice destroys exactly the things our deliverables are made of:

* an HTML entity (``&amp;``) cut at the ``&`` renders as literal garbage,
* a ``**bold**`` or ```` `code` ```` span cut in the middle changes the meaning
  of everything after it.

:func:`split_once` therefore finds the *safest* boundary at or before the limit
and :func:`split_message` repeats it. Splitting is lossless apart from the
whitespace that was used as the cut point.

This module has no imports from the rest of the package on purpose: it is pure
string arithmetic, so it can be reasoned about (and tested) in isolation.
"""

from __future__ import annotations

from pathlib import Path

__all__ = [
    "TEXT_LIMIT",
    "CAPTION_LIMIT",
    "MEDIA_KINDS",
    "escape_html",
    "split_once",
    "split_message",
    "send_method",
    "media_param",
    "supports_caption",
]

#: Maximum length of a Telegram text message (Bot API ``sendMessage``).
TEXT_LIMIT = 4096

#: Maximum length of a media caption (Bot API ``sendDocument``/``sendPhoto``).
CAPTION_LIMIT = 1024

#: The media shapes ``publish --kind`` accepts (issue #11). ``auto`` is the
#: only "magic" value; everything else names the Bot API method explicitly.
MEDIA_KINDS = ("document", "photo", "video", "audio", "voice", "animation",
               "sticker", "auto")

_SEND_METHOD = {
    "document": "sendDocument",
    "photo": "sendPhoto",
    "video": "sendVideo",
    "audio": "sendAudio",
    "voice": "sendVoice",
    "animation": "sendAnimation",
    "sticker": "sendSticker",
}

#: method -> the request field that carries the file.
_SEND_PARAM = {method: kind for kind, method in _SEND_METHOD.items()}

#: ``kind=auto``: file suffix -> kind. Unknown suffixes stay documents.
_AUTO_KIND = {
    ".jpg": "photo", ".jpeg": "photo", ".png": "photo", ".bmp": "photo",
    ".gif": "animation",
    ".mp4": "video", ".mov": "video", ".mkv": "video", ".webm": "video",
    ".mp3": "audio", ".m4a": "audio", ".flac": "audio", ".wav": "audio",
    ".ogg": "voice", ".opus": "voice",
    ".tgs": "sticker",
}


def send_method(kind: str, file: str | None) -> str:
    """Resolve a media kind to the Bot API method that carries ``file``.

    ``auto`` reads the suffix; an unknown suffix falls back to
    ``sendDocument``, because a document upload is byte-exact while
    ``sendPhoto`` lets Telegram recompress the image.
    """
    resolved = kind
    if kind == "auto":
        resolved = _AUTO_KIND.get(Path(str(file or "")).suffix.lower(), "document")
    return _SEND_METHOD[resolved]


def media_param(method: str) -> str:
    """The request field name that carries the file for a ``send*`` method."""
    return _SEND_PARAM[method]


def supports_caption(method: str) -> bool:
    """Stickers are the one upload shape Telegram gives no ``caption`` field."""
    return method != "sendSticker"

_AMP = "&"
_SPAN_MARKERS = ("**", "`")


def escape_html(text: str) -> str:
    """Escape user/vault text for safe interpolation inside an HTML payload.

    Order matters: ``&`` first, otherwise ``&lt;`` would become ``&amp;lt;``.
    """
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def _repair(window: str, cut: int) -> int:
    """Pull ``cut`` back so it never lands inside an entity or a span."""
    n = len(window)
    cut = max(1, min(cut, n))

    amp = window.rfind(_AMP, 0, cut)
    if amp != -1 and ";" not in window[amp:cut]:
        cut = amp if amp > 0 else cut

    for marker in _SPAN_MARKERS:
        while cut > 1 and window[:cut].count(marker) % 2 == 1:
            at = window.rfind(marker, 0, cut)
            if at <= 0:
                break
            cut = at
    return max(1, cut)


def split_once(text: str, limit: int = TEXT_LIMIT) -> tuple[str, str]:
    """Split ``text`` into ``(head, tail)`` at the safest boundary <= ``limit``.

    Preference order: paragraph break, then line break, then word boundary,
    then a repaired hard cut (never inside ``&entity;`` or ``**span**``).
    """
    if len(text) <= limit:
        return text, ""

    window = text[:limit]
    n = len(window)

    cut = n
    pos = window.rfind("\n\n")
    if pos > n // 2:
        cut = pos + 2
    else:
        pos = window.rfind("\n")
        if pos > n // 2:
            cut = pos + 1
        else:
            pos = window.rfind(" ")
            if pos > n // 2:
                cut = pos + 1

    cut = _repair(window, cut)
    # always make progress, even on a single pathologically long token
    cut = max(1, min(cut, limit))
    return text[:cut], text[cut:]


def split_message(text: str, limit: int = TEXT_LIMIT) -> list[str]:
    """Split ``text`` into as many chunks as needed, each within ``limit``."""
    if not text:
        return []
    chunks: list[str] = []
    rest = text
    while len(rest) > limit:
        head, tail = split_once(rest, limit)
        chunks.append(head)
        rest = tail.lstrip()
    if rest:
        chunks.append(rest)
    return chunks
