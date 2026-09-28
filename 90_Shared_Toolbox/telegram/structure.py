"""Group structure: what topics exist, how they read, and the extras that make
the group self-describing (roadmap gate G2/G3, issues #8/#10/#19).

Derived from the **vault itself** (not invented):

* `01_Semester_1/` subject folders + the weekly schedule in
  `00_STUDIO_HUB/ACTIVE_STATE.md` (day/time/instructor) → one topic per subject.
* `00_STUDIO_HUB/` analytics artifacts (LEARNER_MODEL, PROGRESS_ANALYTICS)
  → a Progress & Analytics topic.
* `90_Shared_Toolbox/` + `91_Dashboard/` → a Toolbox topic.
* The quiz subsystem (`/quiz/...` routes) → an Exams & MCQ topic.
* The legacy `TOPICS` list in `telegram_publisher.py` → `99-Chat` for discussion.

Extras that make topics organised (each is an action the gateway performs):
  1. **Numbered names** (`01 🛡 Cyber Security`) — ordering by name, because
     Bot API cannot reorder or pin *topics* (MTProto only, ADR in playbook).
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
COLOR_META = 16749490        # warm family for cross-cutting topics


@dataclass(frozen=True)
class TopicSpec:
    subject: str       # registry key (matches the vault folder semantics)
    name: str          # Telegram topic title (numbered => name order)
    card: str          # pinned brief card body (Arabic, brief)
    icon_color: int = COLOR_SUBJECT


STRUCTURE: list[TopicSpec] = [
    TopicSpec(
        "01-Cyber-Security", "01 🛡 Cyber Security",
        "📗 CS501 · Dr. Huda Lafta · الأحد 08:30\n"
        "المحتوى: المحاضرات، ملازم الحفظ، بنوك الأسئلة، واختبارات الأسابيع.\n"
        "المسار بالـ vault: 01_Semester_1/01_Cyber_Security",
    ),
    TopicSpec(
        "02-English-Language", "02 🗣 English Language",
        "📘 CS502 · Dr. Haidar Akab · الأحد 10:30\n"
        "المحتوى: الوحدات النحوية، المقالات، والتمارين.\n"
        "المسار بالـ vault: 01_Semester_1/02_English_Language",
    ),
    TopicSpec(
        "03-Data-Mining", "03 ⛏ Data Mining",
        "📙 Dr. Ahmed Shakir · الاثنين 08:30\n"
        "المحتوى: ملاحظات الأسبوع، المعادلات، وبنوك الأسئلة.\n"
        "المسار بالـ vault: 01_Semester_1/03_Data_Mining",
    ),
    TopicSpec(
        "04-Advanced-Software-Eng", "04 ⚙️ Software Engineering",
        "📕 CS504 · Dr. Ali Fahim · الاثنين 10:30 (3 ساعات)\n"
        "المحتوى: الوحدات، المخططات، والملخصات المدمجة.\n"
        "المسار بالـ vault: 01_Semester_1/04_Advanced_Software_Eng",
    ),
    TopicSpec(
        "05-Soft-Computing", "05 🧠 Soft Computing",
        "📗 Prof. Dr. Abdul Hadi · الثلاثاء 08:30\n"
        "المحتوى: الفازي، ANFIS، والكتيبات الأسبوعية.\n"
        "المسار بالـ vault: 01_Semester_1/05_Soft_Computing",
    ),
    TopicSpec(
        "06-Artificial-Intelligence", "06 🤖 Artificial Intelligence",
        "📘 Dr. Saif Al-Saidi · الثلاثاء 10:30 — **معلّق لسا مواد**\n"
        "المحتوى: (بانتظار المحاضرة الأولى).\n"
        "المسار بالـ vault: 01_Semester_1/06_Artificial_Intelligence",
        icon_color=COLOR_META,
    ),
    TopicSpec(
        "70-Exams-and-MCQ", "📚 Exams & MCQ",
        "🎯 روابط الاختبارات، كتيّبات الامتحانات، ونتائج MCQ.\n"
        "النتائج تُرحّل أوتوماتيكياً لـ LEARNER_MODEL.\n"
        "المسار بالـ vault: */07_Quizzes_&_Anki/",
        icon_color=COLOR_META,
    ),
    TopicSpec(
        "71-Progress-Analytics", "📊 Progress & Analytics",
        "📈 تقارير أسبوعية: التقدم، نسب الإتقان، وقائمة المراجعة.\n"
        "المسار بالـ vault: 00_STUDIO_HUB/PROGRESS_ANALYTICS.md",
        icon_color=COLOR_META,
    ),
    TopicSpec(
        "90-Toolbox", "🧰 Toolbox",
        "🛠 أدوات التصدير والمزامنة ولوحة الاختبارات (Dashboard).\n"
        "المسار بالـ vault: 90_Shared_Toolbox/ · 91_Dashboard/",
        icon_color=COLOR_META,
    ),
    TopicSpec(
        "99-Chat", "💬 Chat",
        "🗨 نقاش عام بلا تصنيف. المحتوى المنظّم يروح لتوبيكات المواد.",
        icon_color=COLOR_META,
    ),
]


def topic_link(chat_id: int, thread_id: int) -> str:
    """Private-supergroup deep link to a topic (thread root message)."""
    internal = str(chat_id)
    if internal.startswith("-100"):
        internal = internal[4:]
    elif internal.startswith("-"):
        internal = internal[1:]
    return f"https://t.me/c/{internal}/{thread_id}"


def card_text(spec: TopicSpec) -> str:
    """Pinned brief card — the topic's description (Telegram has no other)."""
    return f"{spec.name}\n\n{spec.card}\n\n— يُحدَّث تلقائياً بواسطة Master Studio gateway"


def index_payload(chat_id: int, bound: dict[str, int]) -> tuple[str, list[dict]]:
    """Index message + inline buttons for every bound subject.

    ``bound`` maps subject -> thread_id (only bound topics get a button).
    """
    lines = ["🗂 Master Studio — فهرس الكروب", "", "اختر التوبيك من الأزرار 👇"]
    buttons = []
    for spec in STRUCTURE:
        thread_id = bound.get(spec.subject)
        if thread_id is None:
            continue
        buttons.append([{"label": spec.name, "url": topic_link(chat_id, thread_id)}])
    return "\n".join(lines), buttons
