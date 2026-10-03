"""Live verification gate — proves a topic still says what the catalog says.

Why this module exists
----------------------
``TELEGRAM_PUBLISHING_PLAYBOOK.md`` §7 makes a live topic check the first gate
before any commit, and for a while it printed ``ALL CHECKS PASSED`` — but the
script that printed it lived in a temp folder and was deleted by the next
cleanup. A gate whose tool does not exist is not a gate: nobody could re-run
it, and nothing failed when the promise was broken (found 2026-10-03).

The design keeps the *judgement* pure and the *reading* separate:

* :func:`verify_topic` takes the catalog and a list of
  :class:`TopicMessage` records and returns a :class:`TopicReport`. It touches
  no network, so every invariant is unit-tested in
  ``tests/test_telegram_verify.py`` and a regression fails in CI.
* :meth:`telegram.human.TelethonGateway.topic` does the only thing that needs
  the network: read one forum topic as the spare account. The Bot API has no
  method to read a topic's history or its pinned message, which is why this is
  the MTProto path.
* :func:`verify_main` wires the two together for ``tools/tg_verify.py``.

Read-only by construction: it builds no request that writes, so it can never
change the group it inspects.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from html import escape
from pathlib import Path
from typing import Any

from .catalog import (CATALOG_DIR, SUBJECT_KEYS, Catalog, arabic_ordinal,
                      visible_url_problems)

__all__ = [
    "Check",
    "TopicMessage",
    "TopicReport",
    "build_parser",
    "report_lines",
    "verify_main",
    "verify_topic",
]

#: Telegram caps a document's display name at 62 *bytes*, not characters: an
#: Arabic filename pays two bytes per letter, so a 22-letter name that looks
#: short can still be refused. The gate measures bytes.
FILENAME_BUDGET = 62


# --------------------------------------------------------------------- model --
@dataclass(frozen=True)
class TopicMessage:
    """One message as the reader saw it — the minimum the checks need.

    ``service`` marks the topic's creation message (``action`` in Telethon):
    it is always the lowest id in a topic, so leaving it in would make "the
    card is the first message" impossible by construction.
    """

    message_id: int
    text: str = ""
    pinned: bool = False
    service: bool = False
    file_name: str | None = None
    links: tuple[str, ...] = ()


@dataclass(frozen=True)
class Check:
    ok: bool
    label: str


@dataclass(frozen=True)
class TopicReport:
    subject: str
    thread_id: int
    order: tuple[int, ...]
    checks: tuple[Check, ...] = field(default_factory=tuple)

    @property
    def ok(self) -> bool:
        return all(check.ok for check in self.checks)

    @property
    def failures(self) -> tuple[Check, ...]:
        return tuple(check for check in self.checks if not check.ok)


def _trailing_id(url: str) -> int | None:
    """The message id a ``t.me/c/<chat>/<id>`` link points at."""
    tail = str(url).rstrip("/").rsplit("/", 1)[-1]
    return int(tail) if tail.isdigit() else None


def _chapter_numbers(cat: Catalog) -> str:
    return ",".join(str(i) for i in range(1, len(cat.chapters) + 1)) or "—"


def _has_bare_url(text: str) -> bool:
    """True when a URL is on screen rather than hidden inside a label.

    Telegram's ``MessageEntityTextUrl`` links cover the *label* (``الأول``),
    never the address, so a URL the reader can see survives taking the anchors
    out — the same predicate ``catalog.check_rendered`` applies to a card
    before it ships, reused so the gate and the renderer cannot disagree.
    """
    return bool(visible_url_problems(text))


# ------------------------------------------------------------------- checks --
def verify_topic(cat: Catalog, messages: list[TopicMessage], *,
                 limit_bytes: int = FILENAME_BUDGET) -> TopicReport:
    """Every invariant of one subject topic, in one pass. Pure."""
    content = sorted(
        (m for m in messages if not m.service), key=lambda m: m.message_id)
    order = tuple(m.message_id for m in content)
    by_id = {m.message_id: m for m in content}
    card = by_id.get(cat.catalog_message_id) if cat.catalog_message_id else None

    checks: list[Check] = []

    def check(ok: bool, label: str) -> None:
        checks.append(Check(bool(ok), label))

    check(cat.catalog_message_id is not None,
          "catalog records which message is the card")
    check(card is not None, "card message exists in the topic")
    check(bool(content) and cat.catalog_message_id == order[0],
          "card is the first content message")
    check(bool(card and card.pinned), "card is pinned")

    caption = card.text if card else ""
    check(escape(cat.subject) in caption,
          f"card names the subject ({cat.subject})")
    check(escape(cat.doctor) in caption,
          f"card names the doctor ({cat.doctor})")
    check(f"الجابتر : {_chapter_numbers(cat)}" in caption,
          "card carries the verbatim chapter line")
    check(all(arabic_ordinal(i) in caption
              for i in range(1, len(cat.chapters) + 1)),
          "card lists every ordinal")
    check(card is not None and card.file_name == Path(cat.pdf).name,
          f"card attaches the booklet ({Path(cat.pdf).name})")

    linked = {_trailing_id(url) for url in (card.links if card else ())}
    check(all(mid in linked for mid in cat.chapters),
          f"card chapter links point at the published files "
          f"({list(cat.chapters)})")
    check(not _has_bare_url(caption), "card shows no bare URL")

    for mid in cat.chapters:
        check(mid in by_id, f"chapter post {mid} exists in the topic")
    for ref in cat.references:
        check(ref.message_id in by_id,
              f"reference post {ref.message_id} exists in the topic")

    for mid in cat.chapters:
        post = by_id.get(mid)
        if post is None or post.file_name is None:
            check(False, f"chapter {mid} carries a file")
            continue
        size = len(post.file_name.encode("utf-8"))
        check(size <= limit_bytes,
              f"{post.file_name} = {size} B (<= {limit_bytes})")
        check(not _has_bare_url(post.text),
              f"chapter {mid} shows no bare URL")

    return TopicReport(subject=cat.key, thread_id=cat.catalog_message_id,
                       order=order, checks=tuple(checks))


def report_lines(report: TopicReport) -> list[str]:
    lines = [f"=== {report.subject} (topic {report.thread_id}) ===",
             f"  order: {list(report.order)}"]
    for check in report.checks:
        lines.append(f"  {'PASS' if check.ok else 'FAIL'}  {check.label}")
    return lines


# --------------------------------------------------------------------- live --
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tg_verify",
        description="Read the live subject topics and verify the catalog "
                    "contract (card first + pinned, chapters, references, "
                    "62-byte filenames).",
    )
    parser.add_argument("--catalog-dir", type=Path, default=CATALOG_DIR,
                        help="folder holding one JSON file per subject")
    parser.add_argument("--registry", help="path to the topic registry JSON")
    parser.add_argument("--subject", action="append", dest="subjects",
                        help="subject to verify (repeatable, default: all)")
    parser.add_argument("--limit", type=int, default=200,
                        help="messages to read per topic (default 200)")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="machine-readable output")
    parser.add_argument("--live", action="store_true",
                        help="required: the check reads the real group")
    return parser


def _emit(payload: dict[str, Any], as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    if payload.get("status") == "error":
        print(f"error: {payload.get('error')}")
        return
    for report in payload.get("reports", []):
        for line in report["lines"]:
            print(line)
        print()
    print(payload.get("verdict"))


def verify_main(argv: list[str] | None = None) -> int:
    """``tg_verify`` entry point — the permanent form of playbook §7's gate."""
    from .human import ENV_ENABLED, TelethonGateway, human_enabled
    from .store import load_dotenv

    load_dotenv()  # the kill switch and credentials live in .env

    args = build_parser().parse_args(argv)
    as_json = bool(args.as_json)

    if not args.live:
        _emit({"status": "error", "error":
               "verification reads the real group — pass --live"}, as_json)
        return 5
    if not human_enabled():
        _emit({"status": "error", "error":
               f"human mode is disabled — set {ENV_ENABLED}=1 in .env "
               "to read the group"}, as_json)
        return 5

    from .registry import Registry  # local to keep import cycles out

    registry = Registry(args.registry, seed=False)
    cat_dir = Path(args.catalog_dir)
    keys = list(args.subjects) if args.subjects else list(SUBJECT_KEYS)

    gateway = TelethonGateway.from_env()
    reports: list[dict[str, Any]] = []
    failed: list[str] = []
    error: str | None = None

    for key in keys:
        path = cat_dir / f"{key}.json"
        if not path.exists():
            error = f"unknown catalog subject {key!r}"
            break
        cat = Catalog.load(path)
        row = registry.get(key)
        chat_id, thread_id = row.get("chat_id"), row.get("thread_id")
        if chat_id is None or thread_id is None:
            error = (f"{key}: not bound to a topic — bind it before "
                     "verifying")
            break
        messages = [TopicMessage(**item) for item in gateway.topic(
            int(chat_id), int(thread_id), limit=int(args.limit))]
        report = verify_topic(cat, messages)
        reports.append({"subject": report.subject,
                        "thread_id": thread_id,
                        "order": list(report.order),
                        "ok": report.ok,
                        "failures": [c.label for c in report.failures],
                        "lines": report_lines(report)})
        if not report.ok:
            failed.append(report.subject)

    if error is not None:
        _emit({"status": "error", "error": error, "reports": reports},
              as_json)
        return 2

    verdict = "ALL CHECKS PASSED" if not failed else \
        f"CHECKS FAILED ({', '.join(failed)})"
    _emit({"status": "ok" if not failed else "error",
           "verdict": verdict, "failed": failed, "reports": reports}, as_json)
    return 1 if failed else 0
