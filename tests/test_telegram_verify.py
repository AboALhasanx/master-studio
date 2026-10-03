"""Tests for the live verification gate (``telegram/verify.py``).

The judgement is pure on purpose: every invariant the playbook promises is
checked here against synthetic topic records, so a regression fails in CI even
though the *reading* needs the network. The one CLI case that can run offline —
``verify_main`` refusing without ``--live`` — is checked too, because a gate
that silently touches the group when asked not to is worse than none.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

toolbox_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox"
if str(toolbox_path) not in sys.path:
    sys.path.insert(0, str(toolbox_path))

from telegram.catalog import Catalog, message_link, render  # noqa: E402
from telegram.verify import (  # noqa: E402
    Check,
    TopicMessage,
    TopicReport,
    report_lines,
    verify_main,
    verify_topic,
)

CHAT = -1003710711332
THREAD = 86
CARD = 190
CH_ONE, CH_TWO = 191, 192
REF = 214
BOOKLET = "تنقيب البيانات - Data Mining.pdf"


def spec(**over):
    base = {
        "icon": "◆",
        "subject": "تنقيب البيانات",
        "doctor": "أ.م.د. أحمد شاكر عبد الرضا",
        "schedule": "الاثنين 08:30 — 10:30",
        "updated": "2026/10/2",
        "chapters": [CH_ONE, CH_TWO],
        "pdf": f"00_STUDIO_HUB/telegram/catalog/files/{BOOKLET}",
        "translation": None,
        "catalog_message_id": CARD,
        "references": [
            {"message_id": REF, "source": "Data Mining: The Textbook — "
                                          "Charu C. Aggarwal",
             "edition": "2015 (Springer)"},
        ],
    }
    base.update(over)
    return base


def catalog(**over) -> Catalog:
    return Catalog.from_dict("03-Data-Mining", spec(**over))


def card_message(cat: Catalog, **over) -> TopicMessage:
    fields = {
        "message_id": CARD,
        "text": render(cat, CHAT),
        "pinned": True,
        "links": tuple(message_link(CHAT, mid) for mid in cat.chapters),
        "file_name": Path(cat.pdf).name,
    }
    fields.update(over)
    return TopicMessage(**fields)


def valid_messages(cat: Catalog | None = None) -> list[TopicMessage]:
    cat = cat or catalog()
    return [
        TopicMessage(message_id=THREAD, service=True),      # topic creation
        card_message(cat),
        TopicMessage(message_id=CH_ONE,
                     file_name="تنقيب البيانات - الجابتر الاول.pdf",
                     links=(message_link(CHAT, CARD),)),
        TopicMessage(message_id=CH_TWO,
                     file_name="تنقيب البيانات - الجابتر الثاني.pdf",
                     links=(message_link(CHAT, CARD),)),
        TopicMessage(message_id=REF),                       # a source post
    ]


def labels(report: TopicReport) -> list[str]:
    return [c.label for c in report.checks]


# ------------------------------------------------------------------ passing --
class TestValidTopic:
    def test_a_healthy_topic_passes_every_check(self):
        report = verify_topic(catalog(), valid_messages())
        assert report.ok, report.failures
        assert report.order == (CARD, CH_ONE, CH_TWO, REF)

    def test_the_service_message_is_not_content(self):
        # It is always the lowest id; counting it would make "card is first"
        # impossible for every topic in the group.
        report = verify_topic(catalog(), valid_messages())
        assert THREAD not in report.order

    def test_report_lines_read_like_the_playbook_sample(self):
        lines = report_lines(verify_topic(catalog(), valid_messages()))
        assert lines[0] == f"=== 03-Data-Mining (topic {CARD}) ==="
        assert lines[1] == f"  order: {[CARD, CH_ONE, CH_TWO, REF]}"
        assert any(line.startswith("  PASS  card is pinned") for line in lines)
        assert not any("FAIL" in line for line in lines)


# ------------------------------------------------------------------ failing --
class TestFailures:
    def _fail(self, messages, needle: str):
        report = verify_topic(catalog(), messages)
        assert not report.ok
        assert any(needle in label for label in labels(report)), labels(report)
        return report

    def test_a_card_that_is_not_first_is_caught(self):
        msgs = valid_messages()
        msgs.append(TopicMessage(message_id=CARD - 5, text="x"))
        self._fail(msgs, "first content message")

    def test_an_unpinned_card_is_caught(self):
        cat = catalog()
        msgs = [card_message(cat, pinned=False), *valid_messages(cat)[2:]]
        self._fail(msgs, "card is pinned")

    def test_a_missing_card_is_caught(self):
        msgs = [m for m in valid_messages() if m.message_id != CARD]
        self._fail(msgs, "card is the first content message")

    def test_a_wrong_subject_or_doctor_is_caught(self):
        cat = catalog()
        bad = card_message(cat, text=render(cat, CHAT)
                           .replace(cat.subject, "موضوع اخر"))
        self._fail([bad, *valid_messages(cat)[2:]], "names the subject")

        bad = card_message(cat, text=render(cat, CHAT)
                           .replace(cat.doctor, "دكتور اخر"))
        self._fail([bad, *valid_messages(cat)[2:]], "names the doctor")

    def test_a_missing_ordinal_is_caught(self):
        cat = catalog()
        bad = card_message(cat, text=render(cat, CHAT).replace("الثاني", ""))
        self._fail([bad, *valid_messages(cat)[2:]], "every ordinal")

    def test_a_chapter_link_that_points_nowhere_is_caught(self):
        cat = catalog()
        bad = card_message(cat, links=(message_link(CHAT, CARD),))
        self._fail([bad, *valid_messages(cat)[2:]], "chapter links")

    def test_a_wrong_booklet_is_caught(self):
        cat = catalog()
        bad = card_message(cat, file_name="something-else.pdf")
        self._fail([bad, *valid_messages(cat)[2:]], "attaches the booklet")

    def test_a_missing_chapter_post_is_caught(self):
        msgs = [m for m in valid_messages() if m.message_id != CH_TWO]
        self._fail(msgs, f"chapter post {CH_TWO}")

    def test_a_missing_reference_post_is_caught(self):
        msgs = [m for m in valid_messages() if m.message_id != REF]
        self._fail(msgs, f"reference post {REF}")

    def test_a_filename_over_the_byte_budget_is_caught(self):
        cat = catalog()
        msgs = valid_messages(cat)
        msgs[2] = TopicMessage(message_id=CH_ONE,
                               file_name="ا" * 40)          # 80 bytes
        self._fail(msgs, "<= 62")

    def test_a_bare_url_on_screen_is_caught(self):
        cat = catalog()
        bad = card_message(cat, text=render(cat, CHAT)
                           + "\nhttps://t.me/c/3710711332/190")
        self._fail([bad, *valid_messages(cat)[2:]], "bare URL")

    def test_the_failure_list_names_what_broke(self):
        msgs = [m for m in valid_messages() if m.message_id != REF]
        report = verify_topic(catalog(), msgs)
        assert any("reference" in label for label in
                   [c.label for c in report.failures])


# --------------------------------------------------------------------- CLI --
class TestCliRefusesWithoutLive:
    def test_no_live_is_exit_5_and_no_network(self, capsys, monkeypatch):
        # Even with human mode on, the missing --live must stop it first: this
        # capability reads the real group and must never surprise anyone.
        monkeypatch.setenv("TELEGRAM_HUMAN_ENABLED", "1")
        code = verify_main(["--json"])
        assert code == 5
        assert "--live" in capsys.readouterr().out
