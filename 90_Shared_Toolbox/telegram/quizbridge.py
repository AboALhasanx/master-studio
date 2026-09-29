"""MCQ publishing bridge — deep links into the existing Flask quiz engine (issue #18).

Scope (deliberate, Phase A **only**): the gateway *composes and publishes a door*
to the quiz subsystem that already exists in the vault. It does **not**:

* re-implement a quiz engine — `91_Dashboard/app.py` owns `/quiz/<subject>/<quiz>`
  and `/api/quiz/submit`, and `90_Shared_Toolbox/tools/quiz_balancer.py` owns the
  shared JSON schema;
* read quiz answers or results — those already flow through
  `/api/quiz/history`, which the dashboard exposes;
* ingest anything from Telegram — that would break the one-directional doctrine
  (ADR D2/D4) and is exactly why the *native* `sendPoll` quiz mode is **Phase B,
  deferred** (see the module docstring note at the bottom).

Why a deep link and not a poll: Telegram `poll` answers arrive as `poll_answer`
updates, which requires a `getUpdates` loop the gateway is architecturally
forbidden from running in production (D2). A URL button is a plain
``sendMessage`` payload, so it is pure outbound and needs no new capability.

The URL shape mirrors the dashboard route table exactly::

    /quiz/<subject_id>/<quiz_id>?mode=exam&shuffle=true

``subject_id`` is the *vault folder* name (``01_Cyber_Security``), which is a
different namespace from the Telegram registry subject key
(``01-Cyber-Security``): folders use underscores, registry keys use dashes.
:func:`subject_folder` is the one place that translation happens, so a mismatch
is caught in one spot instead of silently producing a 404 in the group.
"""

from __future__ import annotations

from pathlib import Path

__all__ = [
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "MODES",
    "subject_folder",
    "quiz_url",
    "quiz_message",
    "quiz_payload",
]

#: Where the Flask dashboard listens by default (see AGENTS.md §1.1).
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5000

#: The two dashboard modes; `exam` is the default because that is what a
#: published "go take this" link should open.
MODES = ("exam", "study")


def subject_folder(subject_key: str) -> str:
    """Map a registry subject key to its vault folder name.

    ``"01-Cyber-Security"`` -> ``"01_Cyber_Security"``. The numeric prefix and
    the subject words are preserved; only the separator changes. A key that is
    already a folder name passes through unchanged, so the function is
    idempotent and safe to call on either namespace.
    """
    return str(subject_key).strip().replace("-", "_")


def quiz_url(
    subject_key: str,
    quiz_id: str,
    *,
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
    mode: str = "exam",
    shuffle: bool = False,
    scheme: str = "http",
) -> str:
    """Build the deep link to the dashboard quiz route.

    Validation is deliberately strict: a malformed ``quiz_id`` or ``mode`` would
    otherwise be published and only fail *after* the student taps it, which is
    the worst place to discover a typo.
    """
    clean_quiz = str(quiz_id).strip()
    if not clean_quiz:
        raise ValueError("quiz_id must not be empty")
    if "/" in clean_quiz or "?" in clean_quiz or "#" in clean_quiz:
        raise ValueError(f"quiz_id contains a path/query separator: {quiz_id!r}")
    if ".." in clean_quiz:
        raise ValueError(f"quiz_id must not traverse: {quiz_id!r}")

    clean_mode = str(mode).strip().lower()
    if clean_mode not in MODES:
        raise ValueError(f"unknown quiz mode {mode!r} (expected one of: {', '.join(MODES)})")

    if not 0 < int(port) < 65536:
        raise ValueError(f"port out of range: {port}")

    query = f"mode={clean_mode}"
    if shuffle:
        query += "&shuffle=true"

    return (
        f"{scheme}://{host}:{int(port)}"
        f"/quiz/{subject_folder(subject_key)}/{clean_quiz}?{query}"
    )


def quiz_message(subject_key: str, quiz_id: str, *, title: str | None = None) -> str:
    """The message body that carries the link (Arabic, brief, no filler labels).

    Kept here rather than in the executor so the wording is testable in
    isolation and stays consistent for every caller.
    """
    heading = title or quiz_id
    return (
        f"🎯 اختبار جديد: {heading}\n"
        f"المادة: {subject_folder(subject_key)}\n\n"
        "اضغط الزر للدخول مباشرة، أو افتح الرابط من أي جهاز على نفس الشبكة."
    )


def quiz_payload(
    subject_key: str,
    quiz_id: str,
    *,
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
    mode: str = "exam",
    shuffle: bool = False,
    title: str | None = None,
    extra_buttons: list[tuple[str, str]] | None = None,
) -> tuple[str, list[dict[str, str]]]:
    """``(text, buttons)`` for the publish step — buttons are URL-shaped.

    The returned button list matches the dashboard's history route so a student
    can always reach their results in the same tap-level from the same topic.

    Phase B note (kept explicit so it is not "lost" as the issue requires):
    a native Telegram ``quiz`` poll would need ``correct_option_id`` plus
    ``poll_answer`` ingestion; both are deferred until the no-ingestion rule
    (D2) is revisited, and neither is built here.
    """
    url = quiz_url(
        subject_key, quiz_id, host=host, port=port, mode=mode, shuffle=shuffle
    )
    buttons: list[dict[str, str]] = [{"label": "▶️ ابدأ الاختبار", "url": url}]
    if mode != "study":
        buttons.append(
            {
                "label": "📖 وضع الدراسة",
                "url": quiz_url(
                    subject_key, quiz_id, host=host, port=port, mode="study",
                    shuffle=shuffle,
                ),
            }
        )
    for label, link in extra_buttons or []:
        buttons.append({"label": label, "url": link})
    return quiz_message(subject_key, quiz_id, title=title), buttons
