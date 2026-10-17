"""The personal bot library — a manifest-driven publish into the student's DM.

The group topics are the **public shelf**: chapters, sources and solutions
decks, each anchored to its subject card and read by the spare account. This is
the other shelf: the student's own chat with the bot, holding the same final
files in a form he can *search*.

Why hashtags: Telegram tags are per-chat, so the global tag soup — every
channel posting ``#ذكاء_اصطناعي`` — is exactly what he does not want. Inside
his own chat, tapping ``#أمن_المعلومات`` lists his own material and nothing
else, which is the whole point of putting the library there.

Two rules make it safe to run:

* **Nothing goes out without an approved manifest.** ``--send`` is explicit;
  the default prints the proposal, sizes included, and sends nothing.
* **The caption keeps the published shape** (the ``●`` bullets the topics use)
  and only appends the tags, so the library reads like the topics rather than
  inventing a second dialect.
"""

from __future__ import annotations

import json
import os
import shutil
import tempfile
from pathlib import Path

__all__ = [
    "SUBJECT_LABELS",
    "SUBJECT_TAGS",
    "KIND_TAGS",
    "CAPTION_LIMIT",
    "NAME_BUDGET",
    "build_caption",
    "kind_tag",
    "library_chat_from_env",
    "load_manifest",
    "resolve_file",
    "stage_copy",
    "subject_tag",
    "summary_table",
    "unstage",
    "validate_items",
]

#: Display names are capped by Telegram at 62 *bytes*, not characters.
NAME_BUDGET = 62

#: Caption ceiling Telegram enforces.
CAPTION_LIMIT = 1024

#: One label per registry subject — the exact words the published subject cards
#: carry, so the library and the topics read the same (a test keeps them in
#: sync with the catalog JSON, which is the source of truth).
#: ``00-University`` has no card: university documents get a shelf of their own
#: so they validate as items instead of being rejected as "unknown subject".
SUBJECT_LABELS = {
    "00-University": "وثائق الجامعة",
    "01-Cyber-Security": "أمن المعلومات",
    "02-English-Language": "اللغة الإنجليزية",
    "03-Data-Mining": "تنقيب البيانات",
    "04-Advanced-Software-Eng": "هندسة البرمجيات المتقدمة",
    "05-Soft-Computing": "الحوسبة الناعمة",
    "06-Artificial-Intelligence": "الذكاء الاصطناعي",
}

#: Hashtags carry no spaces, so multi-word subjects use underscores. They are
#: Arabic on purpose: they are read by a human tapping them, not by a parser.
SUBJECT_TAGS = {
    "00-University": "#وثائق_الجامعة",
    "01-Cyber-Security": "#أمن_المعلومات",
    "02-English-Language": "#انكليزي",
    "03-Data-Mining": "#تنقيب_البيانات",
    "04-Advanced-Software-Eng": "#هندسة_البرمجيات",
    "05-Soft-Computing": "#حوسبة_ناعمة",
    "06-Artificial-Intelligence": "#ذكاء_اصطناعي",
}

#: The second tag says *what kind* of thing this is, so a subject view can be
#: narrowed to lectures only, or to solutions decks only.
KIND_TAGS = {
    "lecture": "#محاضرة",
    "chapter": "#محاضرة",
    "source": "#مصدر",
    "summary": "#ملخص",
    "book": "#كتاب",
    "solutions": "#حلول",
    "quiz": "#كويز",
    "exam": "#امتحان",
    "paper": "#بحث",
    "slides": "#شرائح",
    "diagram": "#مخطط",
    "rules": "#لائحة",
    "card": "#بطاقة",
    "other": "#ملف",
}

ENV_LIBRARY_CHAT = "TELEGRAM_LIBRARY_CHAT"


def library_chat_from_env(raw: str | None = None) -> int | None:
    """The DM that holds the library, or None when it was never configured."""
    if raw is None:
        raw = os.environ.get(ENV_LIBRARY_CHAT, "")
    text = str(raw).strip()
    if not text:
        return None
    try:
        return int(text)
    except ValueError:
        return None


def subject_tag(subject: str) -> str:
    return SUBJECT_TAGS.get(subject, "#مادة")


def kind_tag(kind: str | None) -> str:
    """Unknown kinds still get *a* tag — the tag line is never allowed to be blank."""
    return KIND_TAGS.get(str(kind or "lecture").lower(), "#ملف")


def resolve_file(item: dict, root: Path | None = None) -> Path:
    """Absolute path for an item, relative paths resolved against the vault."""
    raw = str(item.get("file", ""))
    path = Path(raw)
    if path.is_absolute():
        return path
    base = root or Path(__file__).resolve().parents[2]
    return base / raw


def stage_copy(path: Path, display: str | None) -> Path | None:
    """A byte-identical copy under the manifest's *display* name.

    Telegram names a file after the path it was uploaded from and caps the
    display name at 62 **bytes**, so a long vault name has to be shortened
    before the first send — renaming afterwards means re-uploading the whole
    file (per the official docs). Returns ``None`` when the real name already
    fits, so the common case touches no disk at all.
    """
    if not display or display == path.name:
        return None
    folder = Path(tempfile.mkdtemp(prefix="tglib_"))
    target = folder / display
    shutil.copy2(path, target)
    return target


def unstage(staged: Path | None) -> None:
    """Remove a staged copy (and its throwaway folder). Safe to call always."""
    if staged is not None:
        shutil.rmtree(staged.parent, ignore_errors=True)


def build_caption(item: dict) -> str:
    """The published shape, plus the tags that make the library searchable.

    Deliberately the same ``●`` bullets and the same trailing ``الفهرس`` line the
    topic captions use: the library is a second shelf, not a second dialect.
    """
    label = SUBJECT_LABELS.get(str(item.get("subject", "")), str(item.get("subject", "")))
    lines = [f"● {label}", f"● {item.get('title', '')}"]
    if item.get("note"):
        lines.append(f"● {item['note']}")
    lines.append("")
    if item.get("catalog_link"):
        lines.append(f'الفهرس : <a href="{item["catalog_link"]}">كتالوج المادة</a>')
    if item.get("link"):
        lines.append(f'الجابتر بملف : <a href="{item["link"]}">اضغط هنا</a>')
    lines.append(f"{subject_tag(str(item.get('subject', '')))} · {kind_tag(item.get('kind'))}")
    return "\n".join(lines)


def validate_items(items: list[dict], root: Path | None = None) -> list[str]:
    """Every reason this manifest must not be sent — empty means it is clean."""
    problems: list[str] = []
    for index, item in enumerate(items, start=1):
        where = f"item {index} ({item.get('title') or item.get('file') or '?'})"
        if not str(item.get("file", "")).strip():
            problems.append(f"{where}: no file")
            continue
        path = resolve_file(item, root)
        if not path.is_file():
            problems.append(f"{where}: file not found: {path}")
        subject = str(item.get("subject", ""))
        if subject not in SUBJECT_LABELS:
            problems.append(f"{where}: unknown subject {subject!r}")
        if not str(item.get("title", "")).strip():
            problems.append(f"{where}: no title")
        display = str(item.get("display") or path.name)
        size = len(display.encode("utf-8"))
        if size > NAME_BUDGET:
            problems.append(f"{where}: display name {size} B > {NAME_BUDGET} B")
        caption = build_caption(item)
        if len(caption) > CAPTION_LIMIT:
            problems.append(f"{where}: caption {len(caption)} > {CAPTION_LIMIT}")
    return problems


def load_manifest(path: Path | str) -> list[dict]:
    """Read a manifest: either a bare list or ``{"items": [...]}``."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("items", [])
    if not isinstance(data, list):
        raise ValueError("manifest must be a list of items, or {'items': [...]}")
    return [dict(item) for item in data]


def summary_table(items: list[dict], root: Path | None = None) -> str:
    """The proposal a human approves: what, how big, and under which tag."""
    rows = []
    total = 0
    for index, item in enumerate(items, start=1):
        path = resolve_file(item, root)
        size = path.stat().st_size if path.is_file() else 0
        total += size
        display = str(item.get("display") or path.name)
        rows.append((
            index,
            SUBJECT_LABELS.get(str(item.get("subject", "")), "?"),
            str(item.get("title", "")),
            f"{size / 1e6:.2f}",
            str(len(display.encode('utf-8'))),
            subject_tag(str(item.get("subject", ""))),
        ))
    head = f"{'#':>3}  {'subject':<16} {'title':<18} {'MB':>6} {'nameB':>5}  tag"
    body = "\n".join(
        f"{i:>3}  {subject:<16} {title:<18} {mb:>6} {nb:>5}  {tag}"
        for i, subject, title, mb, nb, tag in rows
    )
    foot = f"{len(items)} file(s) · {total / 1e6:.2f} MB"
    return "\n".join([head, body, foot])
