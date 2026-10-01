"""Subject catalog card — one message per subject that is the whole index.

Transplanted from the student's bachelor channels (``cs_stg4`` /
``cs_stg4_onefile``), where a subject is ONE message rather than one message
per asset. The card ships as the **caption of a document**: the first message
of every subject topic is a file (today a one-page placeholder, tomorrow the
merged official lectures), and its caption is the index to it.

The caption states, in this order:

* the subject name (Arabic, no ``01`` prefix);
* the instructor's full Arabic name **with the scientific title**, copied
  from the semester schedule ``.docx`` — ``ا.م.د`` (assistant professor) and
  ``ا.د`` (full professor) are different ranks, and a card that drops the
  rank misrepresents the course;
* an embedded link to a translated copy, **only if one exists** — omitted
  otherwise, never left as a placeholder;
* the chapter numbers contained in the merged file;
* ``● كل جابتر بملف :`` and then one ``【ordinal (link)】`` per chapter,
  three to a row, separated by a blank line.

What the caption must NOT carry is pinned as hard as what it must: no
``<blockquote>``, no vault path, no build footer, no descriptive chapter
titles inside the brackets, no per-link icon, and no address printed beside
its label. Every one of those was removed by request — the card is an index,
and an index that annotates itself stops being an index. A chapter's link is
therefore hidden inside the word it wraps: the reader taps ``الأول``, never
a URL, and :func:`check_rendered` refuses a card where one is on screen.

Two properties make the card *maintainable* rather than decorative:

**A chapter is a lecture file, not a calendar week.** Soft Computing's W02
spanned two weeks on the timetable but is one lecture in one file, so it is
one chapter here. Chapters are listed in the order the files landed, never
re-derived from dates.

**The card is edited in place.** The topic history is append-only; the card
is the mutable catalogue sitting at the top of it. Adding material means
merging a chapter into :mod:`telegram.catalog`'s JSON and re-pushing — the
gateway's idempotency key hashes the payload, so an unchanged card is a
harmless ``duplicate`` and a changed card is a real ``editMessageCaption``.

Layout lives in data, not in code: ``00_STUDIO_HUB/telegram/catalog/*.json``
(one file per registry subject) is the file you read and merge into.

Because the card is a caption, :data:`TELEGRAM_CAPTION_LIMIT` (1024) — not
the 4096 text limit — is the ceiling that decides whether it ships at all.
"""

from __future__ import annotations

import argparse
import io
import json
import re
import time
from contextlib import redirect_stdout
from dataclasses import dataclass
from html import escape
from pathlib import Path
from typing import Any

from .errors import RegistryError, UnboundTopic

__all__ = [
    "CATALOG_DIR",
    "DEFAULT_LIMIT",
    "ROW_WIDTH",
    "SUBJECT_KEYS",
    "Catalog",
    "CatalogError",
    "arabic_ordinal",
    "build_edit_argv",
    "build_parser",
    "build_publish_argv",
    "catalog_main",
    "check_rendered",
    "message_link",
    "pdf_path",
    "render",
]

TELEGRAM_TEXT_LIMIT = 4096
#: A document caption is capped far below a plain message. The card rides a
#: caption, so this — not 4096 — is the number that decides whether it ships.
TELEGRAM_CAPTION_LIMIT = 1024
DEFAULT_LIMIT = TELEGRAM_CAPTION_LIMIT

#: ``【ordinal (link)】`` cells per row. Three is what the bachelor model
#: uses, and a row is a blank line away from the next one so each cell stays
#: a distinct tap target on a phone.
ROW_WIDTH = 3

# The registry subjects that are *material* topics. 70/71/90/99 are meta
# topics with no inventory to index, and 00-Start-Here has no thread.
SUBJECT_KEYS: tuple[str, ...] = (
    "01-Cyber-Security",
    "02-English-Language",
    "03-Data-Mining",
    "04-Advanced-Software-Eng",
    "05-Soft-Computing",
    "06-Artificial-Intelligence",
)

_CATALOG_DIRNAME = ("00_STUDIO_HUB", "telegram", "catalog")
CATALOG_DIR: Path = Path(__file__).resolve().parents[2].joinpath(*_CATALOG_DIRNAME)
#: ``pdf`` paths in the JSON are vault-relative, so they resolve from here.
REPO_ROOT: Path = CATALOG_DIR.parents[2]

_REQUIRED = ("icon", "subject", "doctor", "schedule", "updated", "chapters", "pdf")
_TAG_RE = re.compile(r"<(/?)([A-Za-z][A-Za-z0-9-]*)((?:[^>])*)>")

# Arabic ordinals. Two shapes are needed: the standalone form for 1-10
# (الأول .. العاشر) and the compound form that joins to a ten with و
# (الحادي والعشرون). They differ at 1 — "الأول" stands alone, "الحادي" only
# ever precedes و — which is why they are not one tuple.
_STANDALONE = ("", "الأول", "الثاني", "الثالث", "الرابع", "الخامس",
               "السادس", "السابع", "الثامن", "التاسع", "العاشر")
_COMPOUND = ("", "الحادي", "الثاني", "الثالث", "الرابع", "الخامس",
             "السادس", "السابع", "الثامن", "التاسع")
_TENS = {2: "العشرون", 3: "الثلاثون", 4: "الأربعون", 5: "الخمسون",
         6: "الستون", 7: "السبعون", 8: "الثمانون", 9: "التسعون"}


class CatalogError(ValueError):
    """A catalog payload (or a card rendered from it) cannot be shipped."""


def message_link(chat_id: int, message_id: int) -> str:
    """Private-supergroup permalink: ``t.me/c/<chat>/<message>``.

    The ``-100`` supergroup prefix is stripped, the same way
    :func:`telegram.links.parse_message_link` puts it back.
    """
    internal = str(int(chat_id))
    if internal.startswith("-100"):
        internal = internal[4:]
    elif internal.startswith("-"):
        internal = internal[1:]
    return f"https://t.me/c/{internal}/{int(message_id)}"


def arabic_ordinal(n: int) -> str:
    """Arabic ordinal for a 1-based chapter number — ``الأول``, ``الثالث عشر``.

    Telegram renders the bracket text right-to-left; a wrong ordinal here is
    not a typo the reader skims past, it is the label of the wrong chapter.
    """
    n = int(n)
    if n < 1:
        raise ValueError(f"chapter numbers start at 1, got {n}")
    if n <= 10:
        return _STANDALONE[n]
    if n == 11:
        return "الحادي عشر"  # not "الأول عشر": 11 restarts the count
    if n < 20:
        return f"{_COMPOUND[n - 10]} عشر"
    tens, ones = divmod(n, 10)
    if tens not in _TENS:
        raise ValueError(f"ordinal {n} is beyond the supported range")
    if ones == 0:
        return _TENS[tens]
    return f"{_COMPOUND[ones]} و{_TENS[tens]}"


# ------------------------------------------------------------------ model --


@dataclass(frozen=True)
class Catalog:
    """The parsed, validated source of one subject's card."""

    key: str
    icon: str
    subject: str
    doctor: str
    schedule: str
    updated: str
    chapters: tuple[int, ...]
    pdf: str
    translation: str | None = None
    catalog_message_id: int | None = None

    # -- construction ----------------------------------------------------
    @classmethod
    def from_dict(cls, key: str, data: Any) -> Catalog:
        if not isinstance(data, dict):
            raise CatalogError(f"{key}: catalog payload must be a JSON object")
        for name in _REQUIRED:
            if name not in data:
                raise CatalogError(f"{key}: missing required field {name!r}")

        chapters = tuple(
            _positive(key, "chapters[]", mid)
            for mid in _list(key, "chapters", data["chapters"])
        )

        translation = data.get("translation")
        if translation in (None, ""):
            translation = None
        else:
            translation = _text(key, "translation", translation)

        message_id = data.get("catalog_message_id")
        if message_id in (None, ""):
            message_id = None
        else:
            message_id = _positive(key, "catalog_message_id", message_id)

        return cls(
            key=key,
            icon=_text(key, "icon", data["icon"]),
            subject=_text(key, "subject", data["subject"]),
            doctor=_text(key, "doctor", data["doctor"]),
            schedule=_text(key, "schedule", data["schedule"]),
            updated=_text(key, "updated", data["updated"]),
            chapters=chapters,
            pdf=_text(key, "pdf", data["pdf"]),
            translation=translation,
            catalog_message_id=message_id,
        )

    @classmethod
    def load(cls, path: Path | str) -> Catalog:
        path = Path(path)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            raise CatalogError(f"no catalog file: {path}") from None
        except json.JSONDecodeError as exc:
            raise CatalogError(f"{path}: not valid JSON ({exc})") from None
        return cls.from_dict(path.stem, data)


def pdf_path(cat: Catalog) -> Path:
    """Absolute path of the file this card carries (vault-relative in JSON)."""
    path = Path(cat.pdf)
    return path if path.is_absolute() else REPO_ROOT / path


def _list(key: str, name: str, value: Any) -> list[Any]:
    if not isinstance(value, list):
        raise CatalogError(f"{key}: {name!r} must be a list")
    return value


def _text(key: str, name: str, value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CatalogError(f"{key}: {name!r} must be a non-empty string")
    return value.strip()


def _positive(key: str, name: str, value: Any) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise CatalogError(f"{key}: {name!r} must be a positive message id, got {value!r}")
    return int(value)


# ----------------------------------------------------------------- render --


def check_rendered(text: str, *, limit: int = DEFAULT_LIMIT) -> list[str]:
    """Problems that would make Telegram mangle or chop the card."""
    problems: list[str] = []
    if len(text) > limit:
        problems.append(
            f"rendered card is {len(text)} characters — Telegram caps a "
            f"caption at {limit}"
        )
    problems.extend(_tag_problems(text))
    problems.extend(_visible_url_problems(text))
    return problems


def _visible_url_problems(text: str) -> list[str]:
    """A link has to live inside its label, never beside it.

    Telegram prints verbatim what it is given: an ``href`` shows as the word
    it wraps, while a URL typed next to that word shows as the URL — which
    turns the index into the wall of addresses it was meant to replace.
    Whatever survives taking the anchors out is on screen for the reader.
    """
    visible = re.sub(r'<a href="[^"]+">[^<]*</a>', "", text)
    return [
        f"{url} is printed as text instead of being hidden in its label"
        for url in re.findall(r"https?://\S+", visible)
    ]


def _tag_problems(text: str) -> list[str]:
    stack: list[str] = []
    problems: list[str] = []
    for closing, name, _attrs in _TAG_RE.findall(text):
        tag = name.lower()
        if closing:
            if not stack:
                problems.append(f"stray </{tag}>")
            elif stack[-1] != tag:
                problems.append(f"</{tag}> closes <{stack[-1]}>")
            else:
                stack.pop()
        else:
            stack.append(tag)
    problems.extend(f"unclosed <{tag}>" for tag in stack)
    return problems


def _chapter_rows(cat: Catalog, chat_id: int) -> list[str]:
    rows: list[str] = []
    for start in range(0, len(cat.chapters), ROW_WIDTH):
        chunk = cat.chapters[start:start + ROW_WIDTH]
        cells = [
            f'【<a href="{message_link(chat_id, mid)}">'
            f"{arabic_ordinal(index + 1)}</a>】"
            for index, mid in enumerate(chunk, start=start)
        ]
        rows.append("".join(cells))
    return rows


def render(cat: Catalog, chat_id: int, *, limit: int = DEFAULT_LIMIT) -> str:
    """Build the card body as Telegram HTML, or refuse to ship it."""
    numbers = ",".join(str(i) for i in range(1, len(cat.chapters) + 1)) or "—"

    # No emoji anywhere: the header marker is the subject's monochrome glyph
    # (``◆``), the section head keeps the verbatim ``●`` the student dictated,
    # and the metadata lines are plain labels — colour-free text is easier on
    # the eye and renders identically in every client.
    lines = [
        f"{cat.icon} {escape(cat.subject)}",
        "",
        f"الدكتور : {escape(cat.doctor)}",
        f"المحاضرة : {escape(cat.schedule)}",
    ]
    if cat.translation:
        href = escape(cat.translation, quote=True)
        lines.append(f'المادة مترجمة : <a href="{href}">اضغط هنا</a>')
    lines += [f"الجابتر : {numbers}", ""]

    if cat.chapters:
        lines += ["● كل جابتر بملف :", ""]
        rows = _chapter_rows(cat, chat_id)
        for position, row in enumerate(rows):
            lines.append(row)
            if position + 1 < len(rows):
                lines.append("")
    else:
        lines.append("● كل جابتر بملف : —")

    lines += ["", f"آخر تحديث : {escape(cat.updated)}"]

    body = "\n".join(lines)
    problems = check_rendered(body, limit=limit)
    if problems:
        raise CatalogError(f"{cat.key}: {'; '.join(problems)}")
    return body


# ------------------------------------------------------------------- push --


def _global_argv(*, live: bool, dry_run: bool, as_json: bool,
                 actor: int | None) -> list[str]:
    """Flags that must precede the subcommand.

    ``tg.py publish --live`` would land ``--live`` on the subparser and be
    ignored, so every global flag is assembled before the verb is named.
    """
    argv: list[str] = []
    if as_json:
        argv.append("--json")
    if live:
        argv.append("--live")
    if dry_run:
        argv.append("--dry-run")
    if actor is not None:
        argv += ["--actor", str(int(actor))]
    return argv


def build_publish_argv(
    subject: str,
    file: str,
    caption: str,
    *,
    live: bool = False,
    dry_run: bool = True,
    as_json: bool = True,
    actor: int | None = None,
) -> list[str]:
    """CLI argv for the *first* push: the message that does not exist yet.

    ``actor`` is the owner id the ACL asks for on every non-local verb;
    without it the dry run comes back ``denied`` rather than ``authorized``.
    """
    argv = _global_argv(live=live, dry_run=dry_run, as_json=as_json, actor=actor)
    argv += [
        "publish",
        "--subject", subject,
        "--file", file,
        "--caption", caption,
        "--html",
    ]
    return argv


def build_edit_argv(
    subject: str,
    message_id: int,
    body: str,
    *,
    live: bool = False,
    dry_run: bool = True,
    as_json: bool = True,
    actor: int | None = None,
) -> list[str]:
    """CLI argv for pushing an existing card.

    ``--caption``, not ``--text``: the card is a document, so an in-place
    update must go through ``editMessageCaption``. Sending ``editMessageText``
    at a media message fails, and re-publishing would drop a second copy at
    the bottom of the topic — breaking "the first message is the catalog".
    """
    argv = _global_argv(live=live, dry_run=dry_run, as_json=as_json, actor=actor)
    argv += [
        "edit",
        "--subject", subject,
        "--message-id", str(message_id),
        "--caption", body,
        "--html",
    ]
    return argv


def _default_actor() -> int | None:
    """First configured owner — who the ACL believes is driving the push."""
    from .acl import owner_ids_from_env

    owners = sorted(owner_ids_from_env())
    return owners[0] if owners else None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tg_catalog",
        description="Render and push the one-message-per-subject catalog cards.",
    )
    parser.add_argument("--catalog-dir", type=Path, default=CATALOG_DIR,
                        help="folder holding one JSON file per subject")
    parser.add_argument("--registry", help="path to the topic registry JSON")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="machine-readable output")
    parser.add_argument("--live", action="store_true",
                        help="actually publish/edit the card (default: dry run)")
    parser.add_argument("--dry-run", action="store_true",
                        help="validate and print the plan; no network")
    parser.add_argument("--pace", type=float, default=1.5,
                        help="seconds to wait between two pushes")
    parser.add_argument("--actor", type=int,
                        help="owner id driving the push (defaults to the first "
                             "TELEGRAM_OWNER_IDS entry)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true", dest="listing",
                       help="show every shipped card")
    group.add_argument("--print", metavar="SUBJECT", dest="print_subject",
                       help="render one card to stdout without pushing it")
    group.add_argument("--push", action="append", metavar="SUBJECT", dest="push",
                       help="push a subject card (repeatable)")
    group.add_argument("--push-all", action="store_true",
                       help="push every shipped subject card")
    return parser


def _emit(payload: dict[str, Any], as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    if payload.get("status") != "ok":
        print(f"error: {payload.get('error')}")
        return
    for row in payload.get("results", []):
        print(f"{row['subject']:<26} {row['status']}")
    for row in payload.get("subjects", []):
        print(row)


def _load(cat_dir: Path, key: str) -> Catalog:
    path = cat_dir / f"{key}.json"
    if not path.exists():
        known = ", ".join(sorted(p.stem for p in cat_dir.glob("*.json"))) or "<none>"
        raise CatalogError(f"unknown catalog subject {key!r} (known: {known})")
    return Catalog.load(path)


def _persist_message_id(cat_dir: Path, key: str, message_id: int) -> None:
    """Write a freshly published card's id back into its JSON.

    Without this the file still says ``null`` and the next push would post a
    **second** card at the bottom of the topic, breaking the one invariant the
    catalog exists for: the first message of the subject is the index. Only a
    real, positive id is ever written — a failed or deferred push leaves the
    file exactly as it was.
    """
    path = cat_dir / f"{key}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("catalog_message_id") == int(message_id):
        return
    data["catalog_message_id"] = int(message_id)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def _bound_chat(registry: Any, key: str) -> int:
    """The group a subject's card points at.

    Every link in a card is ``t.me/c/<internal>/...``, so a card cannot be
    rendered without a chat id — and ``registry.json`` is gitignored local
    state, so a checkout that never ran a binding has none to give. Report
    that as the registry's own error, naming the subject, rather than letting
    ``int(None)`` escape a CLI as a traceback.
    """
    row = registry.get(key)  # RegistryMiss for a subject the file lacks
    if row.get("chat_id") is None:
        raise UnboundTopic(
            f"{key}: not bound to any group — bind it first, the card's "
            "links need a chat id"
        )
    return int(row["chat_id"])


def _push_one(cat_dir: Path, registry: Any, key: str, *,
              live: bool, dry_run: bool, actor: int | None) -> dict[str, Any]:
    cat = _load(cat_dir, key)
    chat_id = _bound_chat(registry, key)
    body = render(cat, chat_id)

    file = pdf_path(cat)
    if not file.is_file():
        raise CatalogError(f"{key}: no catalog file at {cat.pdf}")

    if cat.catalog_message_id is None:
        mode = "publish"
        argv = build_publish_argv(key, str(file), body, live=live,
                                  dry_run=dry_run, as_json=True, actor=actor)
    else:
        mode = "edit"
        argv = build_edit_argv(key, cat.catalog_message_id, body, live=live,
                               dry_run=dry_run, as_json=True, actor=actor)

    from .cli import main as tg_main  # local: cli imports the world, not catalog

    buf = io.StringIO()
    with redirect_stdout(buf):
        code = tg_main(argv)
    try:
        payload = json.loads(buf.getvalue())
    except json.JSONDecodeError:
        payload = {"status": "unparsed", "raw": buf.getvalue()[:400]}

    row: dict[str, Any] = {
        "subject": key,
        "dry_run": dry_run,
        "mode": mode,
        "status": ("authorized" if dry_run and payload.get("authorized")
                   else payload.get("status") or payload.get("error")
                   or f"exit:{code}"),
        "characters": len(body),
        "file": cat.pdf,
        "catalog_message_id": cat.catalog_message_id,
    }
    if not dry_run:
        row["message_id"] = payload.get("message_id") or payload.get("result", {}).get("message_id")
        mid = row["message_id"]
        if isinstance(mid, int) and mid > 0:
            _persist_message_id(cat_dir, key, mid)
    return row


# execute() answers "sent" for a message that left the process, "ok" for a
# method with no message id, "duplicate" when the payload is byte-identical to
# a previous push, and "queued" when pacing deferred it — none is a failure.
_OK = {"sent", "ok", "authorized", "duplicate", "queued"}


def catalog_main(argv: list[str] | None = None) -> int:
    """``tg_catalog`` entry point — the Zero-CLI way to refresh the cards."""
    # `store.load_dotenv`, not the third-party `dotenv`: the vault ships its
    # own dependency-free reader (G1) and `python-dotenv` is not in
    # requirements.txt — importing that one only worked where pip had put it
    # there by hand, and died with ModuleNotFoundError on a bare CI checkout.
    from .store import load_dotenv

    load_dotenv()  # the owner allowlist lives in .env, and we read it below

    args = build_parser().parse_args(argv)
    from .registry import Registry  # local to keep import cycles out

    registry = Registry(args.registry, seed=False)
    cat_dir = Path(args.catalog_dir)
    actor = args.actor if args.actor is not None else _default_actor()

    if args.listing:
        rows = []
        for path in sorted(cat_dir.glob("*.json")):
            cat = Catalog.load(path)
            rows.append({"subject": path.stem, "title": cat.subject,
                         "chapters": len(cat.chapters),
                         "catalog_message_id": cat.catalog_message_id,
                         "updated": cat.updated})
        _emit({"status": "ok", "subjects": [r["subject"] for r in rows],
               "cards": rows, "catalog_dir": str(cat_dir)}, args.as_json)
        return 0

    if args.print_subject:
        try:
            cat = _load(cat_dir, args.print_subject)
            chat_id = _bound_chat(registry, cat.key)
        except CatalogError as exc:
            _emit({"status": "error", "error": str(exc)}, args.as_json)
            return 2
        except RegistryError as exc:
            _emit({"status": "error", "error": str(exc)}, args.as_json)
            return exc.code
        print(render(cat, chat_id))
        return 0

    keys = list(args.push) if args.push else list(SUBJECT_KEYS)
    live = bool(args.live)
    dry_run = bool(args.dry_run) or not live  # no --live means offline, always

    results: list[dict[str, Any]] = []
    error: str | None = None
    error_code = 2  # CatalogError; a registry problem reports its own code
    for index, key in enumerate(keys):
        if index and args.pace > 0:
            time.sleep(args.pace)
        try:
            results.append(_push_one(cat_dir, registry, key,
                                     live=live, dry_run=dry_run, actor=actor))
        except CatalogError as exc:
            error = str(exc)
            break
        except RegistryError as exc:
            error, error_code = str(exc), exc.code
            break

    if error is not None:
        _emit({"status": "error", "error": error, "dry_run": dry_run,
               "live": live, "results": results}, args.as_json)
        return error_code

    failed = [row for row in results if row["status"] not in _OK]
    _emit({"status": "error" if failed else "ok", "live": live,
           "dry_run": dry_run, "results": results,
           "failed": [row["subject"] for row in failed]}, args.as_json)
    return 1 if failed else 0
