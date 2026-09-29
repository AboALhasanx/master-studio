"""Human-like behaviour pack — pacing, presence and persona (issue #17).

An admin that dumps 4 000 characters instantly reads as a machine, and a batch
of twenty posts arriving in the same second reads as a spam bot. The bot stays
an **official bot** (zero ban risk, ADR D1) but behaves like a person:

* **Presence first.** A ``sendChatAction`` (``typing`` / ``upload_document``)
  precedes a long send, so the topic shows "typing…" the way a human would.
* **Human pacing.** Batch items are separated by a short, *deterministic-but-
  unequal* delay instead of firing back-to-back.
* **Reply in context.** Posts anchor to the message they answer
  (``reply_to_message_id``) rather than floating as bare broadcasts.
* **Edit, don't re-post.** A correction edits the original.
* **Iraqi persona.** A documented tone, so every harness writes the same way.

Why the delays live here rather than in the transport
-----------------------------------------------------
Pacing is a *policy*; the transport is a *mechanism*. The executor reads these
values and sleeps between calls; the transport stays a dumb HTTP layer that the
tests mock. That split is what lets the suite assert the pacing **without
actually waiting** (see ``test_persona_pacing_is_bounded_and_observable``).

Why the delay is deterministic
------------------------------
A random delay makes a test suite flaky and an audit log irreproducible. The
sequence below is a fixed, coprime-stepped pattern with the *shape* of human
pacing (never identical, never zero) while remaining fully predictable. It can
be switched off entirely (``pacing=0``) for tests and for the dry run.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field

__all__ = [
    "PERSONA",
    "Persona",
    "TYPING_THRESHOLD",
    "TYPING_PARAM",
    "pacing_seconds",
    "presence_for",
    "estimate_read_seconds",
]

#: A send longer than this gets a presence signal first (a one-liner does not
#: need "typing…" — nobody types a single line for a second first).
TYPING_THRESHOLD = 120

#: Chars-per-second a person plausibly types — used to size the delay, not to
#: fake a stopwatch. Telegram itself drops a chat action after ~5 s.
ESTIMATED_CHARS_PER_SECOND = 28


@dataclass(frozen=True)
class Persona:
    """The bot's human-like defaults.

    All values are **bounded**: pacing is capped so a batch can never turn into
    an accidental throttle, and the cap is deliberately below Telegram's
    per-chat limit.
    """

    name: str = "Koko"
    #: Tone, kept short so it can be pasted into the skill verbatim.
    tone: str = (
        "ودّي ومباشر، بلا حشو وبلا مجاملة زايدة. يكتب بالعراقي الطبيعي، "
        "ويخلّي المصطلح التقني بالإنجليزي."
    )
    #: Pacing between batch items, in seconds.
    min_pace: float = 0.8
    max_pace: float = 2.6
    #: Hard ceiling for a single batch, so a 50-item run cannot stall for minutes.
    max_total_pace: float = 25.0
    typing_threshold: int = TYPING_THRESHOLD

    def clamp(self, seconds: float) -> float:
        return max(0.0, min(float(seconds), self.max_pace))


PERSONA = Persona()

#: ``action`` value -> the ``sendChatAction`` vocabulary entry, per noun.
#: Every value is validated against ``schema.CHAT_ACTIONS`` by the caller.
TYPING_PARAM = "typing"


def estimate_read_seconds(text: str, *, persona: Persona = PERSONA) -> float:
    """A plausible "typing" duration for ``text``, clamped to the persona cap.

    Deliberately conservative: this is not a simulation, only enough of a pause
    that the message does not appear the same instant the command returns.
    """
    length = len(text or "")
    seconds = length / ESTIMATED_CHARS_PER_SECOND
    return persona.clamp(seconds)


def pacing_seconds(index: int, *, persona: Persona = PERSONA) -> float:
    """Delay **before** batch item ``index`` (0-based); 0 for the first item.

    Uses a small fixed pattern so the log is reproducible: 0.8, 2.0, 1.4, 2.6,
    then repeating — unequal (human) but never random (testable).
    """
    if index <= 0:
        return 0.0
    pattern = (persona.min_pace, 2.0, 1.4, persona.max_pace)
    return persona.clamp(pattern[(index - 1) % len(pattern)])


def presence_for(
    text: str | None = None,
    *,
    uploading: bool = False,
    persona: Persona = PERSONA,
) -> str | None:
    """The ``sendChatAction`` value to fire first, or ``None`` if none is needed.

    An upload always signals (the file takes real time); text only signals when
    it is long enough that a person would visibly pause.
    """
    if uploading:
        return "upload_document"
    if text and len(text) >= persona.typing_threshold:
        return TYPING_PARAM
    return None


def pause(seconds: float) -> None:
    """Sleep, unless there is nothing to wait for.

    Isolated so a test can monkeypatch exactly one symbol instead of touching
    ``time.sleep`` globally.
    """
    if seconds and seconds > 0:
        time.sleep(seconds)
