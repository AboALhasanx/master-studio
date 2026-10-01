"""Subject catalog cards — one message per subject that carries the whole
inventory as links (the ordering transplant).

The model is lifted from the student's bachelor channels (``cs_stg4`` /
``cs_stg4_onefile``), where a subject is ONE card rather than one message per
asset:

* fixed header fields (icon + Arabic name, instructor, meeting slot, unit
  numbers) — optional fields are dropped, never left as placeholders;
* one ``【label — title】`` line per unit, then that unit's links, two per line;
* an expandable ``<blockquote>`` for the prose nobody scrolls for;
* ``📮 آخر تحديث`` as a freshness stamp that is independent of the post date;
* a uniform footer, so every card ends the same way.

Two properties make the card *maintainable* rather than decorative:

**The unit is a lecture file, not a calendar week.** Soft Computing's W02
spanned two weeks on the timetable but is one lecture in one file, so it is
one unit here. Units are listed in the order the files landed, never
re-derived from dates.

**The card is edited in place.** The topic history is append-only; the card
is the mutable catalogue sitting at the top of it. Adding material means
merging a unit into :mod:`telegram.catalog`'s JSON and re-pushing — the
gateway's idempotency key hashes the payload, so an unchanged card is a
harmless ``duplicate`` and a changed card is a real ``editMessageText``.

Layout lives in data, not in code: ``00_STUDIO_HUB/telegram/catalog/*.json``
(one file per registry subject) is the file you read and merge into.
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

__all__ = [
    "CATALOG_DIR",
    "SUBJECT_KEYS",
    "Catalog",
    "CatalogError",
    "Link",
    "Unit",
    "build_edit_argv",
    "catalog_main",
    "check_rendered",
    "message_link",
    "render",
]

# Telegram chops a text message at 4096 characters — a card that overflows
# would silently lose its footer and every link after the cut.
TELEGRAM_TEXT_LIMIT = 4096

# Links-per-line. One long run of anchors is impossible to tap accurately on
# a phone, and two per line is what keeps every link a distinct target.
LINKS_PER_LINE = 2

FOOTER = "— يُحدَّث تلقائياً بواسطة Master Studio gateway"

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

_COLLAPSIBLE = frozenset({"notes", "units"})
_REQUIRED = ("icon", "subject", "doctor", "schedule", "vault", "updated",
             "card_message_id", "units")
_TAG_RE = re.compile(r"<(/?)([A-Za-z][A-Za-z0-9-]*)((?:[^>])*)>")


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


# ------------------------------------------------------------------ model --


@dataclass(frozen=True)
class Link:
    """One tappable pointer into the topic (a lecture file, a quiz, a key)."""

    message_id: int
    text: str
    icon: str = "📎"


@dataclass(frozen=True)
class Unit:
    """One lecture file and everything hanging off it."""

    label: str
    title: str
    links: tuple[Link, ...] = ()


@dataclass(frozen=True)
class Catalog:
    """The parsed, validated source of one subject's card."""

    key: str
    icon: str
    subject: str
    doctor: str
    schedule: str
    vault: str
    updated: str
    card_message_id: int
    units: tuple[Unit, ...] = ()
    notes: tuple[str, ...] = ()
    pending: str | None = None
    collapse: tuple[str, ...] = ("notes",)

    # -- construction ----------------------------------------------------
    @classmethod
    def from_dict(cls, key: str, data: Any) -> Catalog:
        if not isinstance(data, dict):
            raise CatalogError(f"{key}: catalog payload must be a JSON object")
        for name in _REQUIRED:
            if name not in data:
                raise CatalogError(f"{key}: missing required field {name!r}")

        card_id = _positive(key, "card_message_id", data["card_message_id"])
        units = tuple(_unit(key, raw) for raw in _list(key, "units", data["units"]))

        collapse = data.get("collapse", ["notes"])
        if not isinstance(collapse, list):
            raise CatalogError(f"{key}: 'collapse' must be a list")
        for section in collapse:
            if section not in _COLLAPSIBLE:
                raise CatalogError(
                    f"{key}: collapse section {section!r} is not one of "
                    f"{sorted(_COLLAPSIBLE)}"
                )

        return cls(
            key=key,
            icon=_text(key, "icon", data["icon"]),
            subject=_text(key, "subject", data["subject"]),
            doctor=_text(key, "doctor", data["doctor"]),
            schedule=_text(key, "schedule", data["schedule"]),
            vault=_text(key, "vault", data["vault"]),
            updated=_text(key, "updated", data["updated"]),
            card_message_id=card_id,
            units=units,
            notes=tuple(_text(key, "notes[]", n) for n in _list(key, "notes", data.get("notes", []))),
            pending=None if data.get("pending") in (None, "") else _text(key, "pending", data["pending"]),
            collapse=tuple(collapse),
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


def _unit(key: str, raw: Any) -> Unit:
    if not isinstance(raw, dict):
        raise CatalogError(f"{key}: every unit must be an object")
    for name in ("label", "title", "links"):
        if name not in raw:
            raise CatalogError(f"{key}: unit is missing {name!r}")
    links = []
    for raw_link in _list(key, "links", raw["links"]):
        if not isinstance(raw_link, dict) or "id" not in raw_link or "text" not in raw_link:
            raise CatalogError(f"{key}: every link needs an 'id' and a 'text'")
        links.append(
            Link(
                message_id=_positive(key, "link id", raw_link["id"]),
                text=_text(key, "link text", raw_link["text"]),
                icon=_text(key, "link icon", raw_link.get("icon", "📎")),
            )
        )
    return Unit(
        label=_text(key, "unit label", raw["label"]),
        title=_text(key, "unit title", raw["title"]),
        links=tuple(links),
    )


# ----------------------------------------------------------------- render --


def check_rendered(text: str) -> list[str]:
    """Problems that would make Telegram mangle or chop the card."""
    problems: list[str] = []
    if len(text) > TELEGRAM_TEXT_LIMIT:
        problems.append(
            f"rendered card is {len(text)} characters — Telegram caps a message "
            f"at {TELEGRAM_TEXT_LIMIT}"
        )
    problems.extend(_tag_problems(text))
    return problems


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


def _anchor(link: Link, chat_id: int) -> str:
    href = message_link(chat_id, link.message_id)
    return f'<a href="{href}">{escape(link.text)}</a>'


def _link_lines(unit: Unit, chat_id: int) -> list[str]:
    rendered = [f"{unit.links[i].icon} {_anchor(unit.links[i], chat_id)}"
                for i in range(len(unit.links))]
    return [
        " · ".join(rendered[i:i + LINKS_PER_LINE])
        for i in range(0, len(rendered), LINKS_PER_LINE)
    ]


def _units_section(cat: Catalog, chat_id: int) -> str | None:
    if not cat.units:
        return None
    blocks = ["● كل وحدة بملف كامل :"]
    for index, unit in enumerate(cat.units, start=1):
        heading = f"【{unit.label} — {escape(unit.title)}】"
        body = _link_lines(unit, chat_id) or [f"لقطة بعدد {index}"]
        blocks.append("\n".join([heading, *body]))
    return "\n\n".join(blocks)


def _notes_section(cat: Catalog) -> str | None:
    if not cat.notes:
        return None
    lines = ["ملاحظات", *(f"• {escape(note)}" for note in cat.notes)]
    return "\n".join(lines)


def _collapse(section: str, cat: Catalog) -> bool:
    return section in cat.collapse


def render(cat: Catalog, chat_id: int) -> str:
    """Build the card body as Telegram HTML, or refuse to ship it."""
    numbers = ",".join(str(i) for i in range(1, len(cat.units) + 1)) or "—"
    header = "\n".join(
        [
            f"{cat.icon} {escape(cat.subject)}",
            "",
            f"🧑‍🏫 الدكتور : {escape(cat.doctor)}",
            f"🗓 المحاضرة : {escape(cat.schedule)}",
            f"🏷 الوحدات : {numbers}",
        ]
    )

    sections = [header]

    units = _units_section(cat, chat_id)
    if units is not None and _collapse("units", cat):
        sections.append(f"<blockquote expandable>\n{units}\n</blockquote>")
    elif units is not None:
        sections.append(units)
    elif cat.pending:
        sections.append(f"● {escape(cat.pending)}")

    notes = _notes_section(cat)
    if notes is not None and _collapse("notes", cat):
        sections.append(f"<blockquote expandable>\n{notes}\n</blockquote>")
    elif notes is not None:
        sections.append(notes)

    sections.append(
        "\n".join(
            [
                f"📮 آخر تحديث : {escape(cat.updated)}",
                f"📂 المسار : {escape(cat.vault)}",
                FOOTER,
            ]
        )
    )

    body = "\n\n".join(sections)
    problems = check_rendered(body)
    if problems:
        raise CatalogError(f"{cat.key}: {'; '.join(problems)}")
    return body


# ------------------------------------------------------------------- push --


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
    """CLI argv for one card push.

    The global flags must precede the subcommand — ``tg.py edit --live`` would
    land ``--live`` on the subparser and be ignored. ``actor`` is the owner id
    the ACL asks for on every non-local verb; without it the dry run comes back
    ``denied`` rather than ``authorized``.
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
    argv += [
        "edit",
        "--subject", subject,
        "--message-id", str(message_id),
        "--text", body,
        "--html",
    ]
    return argv


def _default_actor() -> int | None:
    """First configured owner — who the ACL believes is driving the push."""
    from .acl import owner_ids_from_env

    owners = sorted(owner_ids_from_env())
    return owners[0] if owners else None


def _build_parser() -> argparse.ArgumentParser:
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
                        help="actually edit the pinned card (default: dry run)")
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


def _push_one(cat_dir: Path, registry: Any, key: str, *,
              live: bool, dry_run: bool, actor: int | None) -> dict[str, Any]:
    cat = _load(cat_dir, key)
    chat_id = int(registry.get(key)["chat_id"])
    body = render(cat, chat_id)

    from .cli import main as tg_main  # local: cli imports the world, not catalog

    buf = io.StringIO()
    with redirect_stdout(buf):
        code = tg_main(build_edit_argv(key, cat.card_message_id, body,
                                       live=live, dry_run=dry_run, as_json=True,
                                       actor=actor))
    try:
        payload = json.loads(buf.getvalue())
    except json.JSONDecodeError:
        payload = {"status": "unparsed", "raw": buf.getvalue()[:400]}

    if dry_run:
        status = "authorized" if payload.get("authorized") else payload.get(
            "error") or "denied"
        return {"subject": key, "dry_run": True, "status": status,
                "characters": len(body), "card_message_id": cat.card_message_id}
    return {"subject": key, "dry_run": False,
            "status": payload.get("status", f"exit:{code}"),
            "characters": len(body), "card_message_id": cat.card_message_id}


# execute() answers "sent" for a message that left the process, "ok" for a
# method with no message id, "duplicate" when the payload is byte-identical to
# a previous push, and "queued" when pacing deferred it — none is a failure.
_OK = {"sent", "ok", "authorized", "duplicate", "queued"}


def catalog_main(argv: list[str] | None = None) -> int:
    """``tg_catalog`` entry point — the Zero-CLI way to refresh the cards."""
    from dotenv import load_dotenv

    load_dotenv()  # the owner allowlist lives in .env, and we read it below

    args = _build_parser().parse_args(argv)
    from .registry import Registry  # local to keep import cycles out

    registry = Registry(args.registry, seed=False)
    cat_dir = Path(args.catalog_dir)
    actor = args.actor if args.actor is not None else _default_actor()

    if args.listing:
        rows = []
        for path in sorted(cat_dir.glob("*.json")):
            cat = Catalog.load(path)
            rows.append({"subject": path.stem, "title": cat.subject,
                         "units": len(cat.units),
                         "card_message_id": cat.card_message_id,
                         "updated": cat.updated})
        _emit({"status": "ok", "subjects": [r["subject"] for r in rows],
               "cards": rows, "catalog_dir": str(cat_dir)}, args.as_json)
        return 0

    if args.print_subject:
        try:
            cat = _load(cat_dir, args.print_subject)
        except CatalogError as exc:
            _emit({"status": "error", "error": str(exc)}, args.as_json)
            return 2
        print(render(cat, int(registry.get(cat.key)["chat_id"])))
        return 0

    keys = list(args.push) if args.push else list(SUBJECT_KEYS)
    live = bool(args.live)
    dry_run = bool(args.dry_run) or not live  # no --live means offline, always

    results: list[dict[str, Any]] = []
    error: str | None = None
    for index, key in enumerate(keys):
        if index and args.pace > 0:
            time.sleep(args.pace)
        try:
            results.append(_push_one(cat_dir, registry, key,
                                     live=live, dry_run=dry_run, actor=actor))
        except CatalogError as exc:
            error = str(exc)
            break

    if error is not None:
        _emit({"status": "error", "error": error, "results": results},
              args.as_json)
        return 2

    failed = [row for row in results if row["status"] not in _OK]
    _emit({"status": "error" if failed else "ok", "live": live,
           "dry_run": dry_run, "results": results,
           "failed": [row["subject"] for row in failed]}, args.as_json)
    return 1 if failed else 0
