"""Group structure: what topics exist, how they read, and the extras that make
the group self-describing (roadmap gate G2/G3, issues #8/#10/#19).

Derived from the **vault itself** (not invented):

* `01_Semester_1/` subject folders + the weekly schedule in
  `00_STUDIO_HUB/ACTIVE_STATE.md` (day/time/instructor) → one topic per subject.
* Discussion needs **no** topic of its own: every forum already has the
  non-deletable **General** topic (id=1, Telegram API), which the owner has
  named **محادثة** — it is the group's chat room, and because General
  messages carry no ``top_msg_id`` it can never be bound in the registry.
  The legacy ``99-Chat`` subject therefore stays seeded (so old references
  fail with a clear *unbound*, not *unknown*) but is not provisioned here.

Three cross-cutting topics once sat beside the subjects — Progress & Analytics
(`71-Progress-Analytics`), Toolbox (`90-Toolbox`) and Exams & MCQ
(`70-Exams-and-MCQ`). They were closed then **deleted on 2026-10-02**: every
subject is its own hub now and their material lives in the local dashboard,
not in the group. Their registry keys survive as ``registry.RETIRED_SUBJECTS``
so an old command fails as *unbound*, but ``STRUCTURE`` no longer provisions
them and nothing here may bring them back.

Topic titles are **Arabic only, monochrome, no emoji, no numbers** (student's
rule: «شيل الارقام من اسماء التوبكتات») — one ``◆``-prefixed name per taught
subject. Order comes from creation order, not from a prefix; General (محادثة)
needs no title of its own — Telegram owns it.

Extras that make topics organised (each is an action the gateway performs):
  1. **Stable titles** — Bot API cannot reorder or pin *topics*
     (MTProto only, ADR in playbook).
  2. **Icon colour chosen at creation** — the colour cannot be changed later.
     Falls back to Telegram's default when the API rejects a value.
  3. **Brief card per topic** — pinned first message carrying course code,
     instructor, schedule and vault path (Telegram has no topic description
     field, so the pinned card *is* the description).
  4. **Pinned index in General** — one message with buttons linking every
     topic (`https://t.me/c/<chat>/<thread_id>`).
"""

from __future__ import annotations

from dataclasses import dataclass, field

__all__ = ["TopicSpec", "STRUCTURE", "topic_link", "card_text", "index_payload"]

# Topic icon colours accepted by createForumTopic (RGB, fixed at creation).
COLOR_SUBJECT = 7322016      # blue-grey family for taught subjects
COLOR_META = 16749490        # warm family for cross-cutting topics — kept for
#                              the colour-picker contract even though the three
#                              utility topics were deleted on 2026-10-02.


@dataclass(frozen=True)
class TopicSpec:
    subject: str       # registry key (matches the vault folder semantics)
    name: str          # Telegram topic title (numbered => name order)
    card: str          # pinned brief card body (Arabic, brief)
    icon_color: int = COLOR_SUBJECT


STRUCTURE: list[TopicSpec] = [
    TopicSpec(
        "01-Cyber-Security", "◆ أمن المعلومات",
        "أ.م.د. هدى لفتة مجيد · الأحد 08:30 — 10:30\n"
        "المحتوى: المحاضرات، ملازم الحفظ، بنوك الأسئلة، واختبارات الأسابيع.",
    ),
    TopicSpec(
        "02-English-Language", "◆ اللغة الإنجليزية",
        "أ.م.د. حيدر عكاب علوان · الأحد 10:30 — 11:30\n"
        "المحتوى: الوحدات النحوية، المقالات، والتمارين.",
    ),
    TopicSpec(
        "03-Data-Mining", "◆ تنقيب البيانات",
        "أ.م.د. أحمد شاكر عبد الرضا · الاثنين 08:30 — 10:30\n"
        "المحتوى: ملاحظات الأسبوع، المعادلات، وبنوك الأسئلة.",
    ),
    TopicSpec(
        "04-Advanced-Software-Eng", "◆ هندسة البرمجيات المتقدمة",
        "أ.م.د. علي فاهم نعمة · الاثنين 10:30 — 13:30\n"
        "المحتوى: الوحدات، المخططات، والملخصات المدمجة.",
    ),
    TopicSpec(
        "05-Soft-Computing", "◆ الحوسبة الناعمة",
        "أ.د. عبد الهادي محمد عدخيل · الثلاثاء 08:30 — 10:30\n"
        "المحتوى: الفازي، ANFIS، والكتيبات الأسبوعية.",
    ),
    TopicSpec(
        "06-Artificial-Intelligence", "◆ الذكاء الاصطناعي",
        "أ.د. سيف علي السعيدي · الثلاثاء 10:30 — 13:30\n"
        "المحتوى: بانتظار المحاضرة الأولى.",
        # All six taught subjects share the subject colour: colour is fixed at
        # creation and cannot be changed later, so it must say "subject" from
        # day one — the pending state is what the card text is for.
    ),
]

# Retired 2026-10-02: the three utility topics (``70-Exams-and-MCQ``,
# ``71-Progress-Analytics``, ``90-Toolbox``) were closed then deleted — every
# subject is its own hub now, and progress/analytics live in the local
# dashboard, not in the group. They are deliberately absent from ``STRUCTURE``
# so a future ``structure`` run cannot recreate them. Their registry keys stay
# so an old command resolves to a clear "unbound" instead of "unknown".


def topic_link(chat_id: int, thread_id: int) -> str:
    """Private-supergroup deep link to a topic (thread root message)."""
    internal = str(chat_id)
    if internal.startswith("-100"):
        internal = internal[4:]
    elif internal.startswith("-"):
        internal = internal[1:]
    return f"https://t.me/c/{internal}/{thread_id}"


def card_text(spec: TopicSpec) -> str:
    """Pinned brief card — the topic's description (Telegram has no other).

    No gateway footer, no vault path, no emoji: the card is a student-facing
    deliverable and inherits the same zero-leakage rules as every other one.
    """
    return f"{spec.name}\n\n{spec.card}"


def index_payload(chat_id: int, bound: dict[str, int]) -> tuple[str, list[dict]]:
    """Index message + inline buttons for every bound subject.

    ``bound`` maps subject -> thread_id (only bound topics get a button).
    """
    lines = ["Master Studio — فهرس الكروب", "", "اختر التوبيك من الأزرار"]
    buttons = []
    for spec in STRUCTURE:
        thread_id = bound.get(spec.subject)
        if thread_id is None:
            continue
        buttons.append([{"label": spec.name, "url": topic_link(chat_id, thread_id)}])
    return "\n".join(lines), buttons
