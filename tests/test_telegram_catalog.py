"""Subject catalog cards — one message per subject that holds the whole
inventory as links (the ordering transplant).

The model comes from the student's bachelor channels (``cs_stg4`` /
``cs_stg4_onefile``): a subject is ONE card, never one message per asset. The
card carries fixed header fields, ``【...】`` link sections, a freshness stamp
and a uniform footer, and it is **edited in place** when material drops — the
catalogue is mutable while the topic history stays append-only.

Two invariants are asserted against the real shipped files, not only against
fixtures:

* the card message id is smaller than every message it links to, so the index
  always sits at the top of its topic;
* every rendered card fits a Telegram message (4096 chars) with balanced HTML.
"""

import io
import json
import re
import sys
from contextlib import redirect_stdout
from pathlib import Path

import pytest

# Ensure 90_Shared_Toolbox is on sys.path (same pattern as test_telegram_gateway)
toolbox_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox"
if str(toolbox_path) not in sys.path:
    sys.path.insert(0, str(toolbox_path))

from telegram import cli as tg_cli  # noqa: E402
from telegram.catalog import (  # noqa: E402
    CATALOG_DIR,
    SUBJECT_KEYS,
    Catalog,
    CatalogError,
    build_edit_argv,
    catalog_main,
    check_rendered,
    message_link,
    render,
)
from telegram.links import parse_message_link  # noqa: E402
from telegram.registry import Registry  # noqa: E402
from telegram.structure import topic_link  # noqa: E402

CHAT = -1003710711332
OWNER = 5664798395
INTERNAL = "3710711332"  # chat id with the -100 supergroup prefix stripped


@pytest.fixture(autouse=True)
def _gate(monkeypatch):
    """The ACL is fail-closed: no owners, or no allowlist, denies everything."""
    monkeypatch.setenv("TELEGRAM_OWNER_IDS", str(OWNER))
    monkeypatch.setenv("TELEGRAM_CHAT_ALLOWLIST", str(CHAT))


def spec(**over):
    """A minimal, valid catalog payload — every test overrides one field."""
    base = {
        "icon": "📗",
        "subject": "أمن المعلومات",
        "doctor": "د. هدى لفتة مجيد",
        "schedule": "الأحد 08:30 — 10:30",
        "vault": "01_Semester_1/01_Cyber_Security",
        "updated": "2026/10/1",
        "card_message_id": 7,
        "units": [
            {
                "label": "الأول",
                "title": "أساسيات الأمن السيبراني",
                "links": [
                    {"id": 60, "text": "ملزمة W01", "icon": "📎"},
                    {"id": 61, "text": "كويز W01", "icon": "🎯"},
                ],
            },
            {
                "label": "الثاني",
                "title": "تقييم المخاطر",
                "links": [{"id": 70, "text": "ملزمة W02", "icon": "📎"}],
            },
        ],
        "notes": ["كل ملزمة مع كويزها في نفس الموضوع."],
    }
    base.update(over)
    return base


def build(**over):
    return Catalog.from_dict("01-Cyber-Security", spec(**over))


# ---------------------------------------------------------------- links ----


class TestMessageLink:
    def test_the_supergroup_prefix_is_stripped(self):
        assert message_link(CHAT, 60) == f"https://t.me/c/{INTERNAL}/60"

    def test_it_round_trips_through_the_existing_parser(self):
        ref = parse_message_link(message_link(CHAT, 28))
        assert (ref.chat_id, ref.message_id) == (CHAT, 28)

    def test_it_agrees_with_the_topic_link_builder(self):
        # structure.topic_link() already builds the same shape for thread ids;
        # two builders must never drift into two different link dialects.
        assert topic_link(CHAT, 6) == message_link(CHAT, 6)


# ----------------------------------------------------------- structure ----


class TestPayloadShape:
    def test_a_missing_required_key_is_a_structural_error(self):
        for key in ("subject", "doctor", "schedule", "vault", "updated",
                    "card_message_id", "units"):
            bad = spec()
            bad.pop(key)
            with pytest.raises(CatalogError) as exc:
                Catalog.from_dict("01-Cyber-Security", bad)
            assert key in str(exc.value)

    def test_a_link_must_name_a_positive_message(self):
        bad = spec()
        bad["units"][0]["links"][0]["id"] = 0
        with pytest.raises(CatalogError):
            Catalog.from_dict("01-Cyber-Security", bad)

    def test_the_card_itself_must_have_a_positive_id(self):
        with pytest.raises(CatalogError):
            Catalog.from_dict("01-Cyber-Security", spec(card_message_id=0))

    def test_a_unit_without_links_is_allowed_for_a_subject_just_announced(self):
        cat = Catalog.from_dict("06-Artificial-Intelligence", spec(units=[]))
        assert cat.units == ()


# -------------------------------------------------------------- render ----


class TestRenderedCard:
    def test_the_header_carries_no_ordinal_prefix(self):
        # "ما اريد مال 01" -- the card opens on the emoji and the Arabic name.
        first = render(build(), CHAT).splitlines()[0]
        assert first == "📗 أمن المعلومات"

    def test_the_doctor_is_rendered_in_arabic(self):
        assert "د. هدى لفتة مجيد" in render(build(), CHAT)

    def test_the_unit_numbers_are_derived_from_the_unit_list(self):
        assert "🏷 الوحدات : 1,2" in render(build(), CHAT)

    def test_an_empty_subject_renders_a_dash_for_the_unit_field(self):
        body = render(Catalog.from_dict("x", spec(units=[])), CHAT)
        assert "🏷 الوحدات : —" in body

    def test_every_link_is_built_from_the_chat_and_its_message_id(self):
        body = render(build(), CHAT)
        assert f"https://t.me/c/{INTERNAL}/60" in body
        assert f"https://t.me/c/{INTERNAL}/70" in body

    def test_links_are_wrapped_in_an_anchor(self):
        assert f'<a href="https://t.me/c/{INTERNAL}/61">كويز W01</a>' in render(
            build(), CHAT
        )

    def test_at_most_two_links_share_one_line(self):
        wide = spec()
        wide["units"] = [
            {"label": "الأول", "title": "كبير", "links": [
                {"id": n, "text": f"ملزمة {n}", "icon": "📎"} for n in range(10, 16)
            ]}
        ]
        body = render(Catalog.from_dict("x", wide), CHAT)
        for line in body.splitlines():
            assert line.count("<a ") <= 2, line

    def test_the_freshness_stamp_comes_before_the_footer(self):
        lines = [ln for ln in render(build(), CHAT).splitlines() if ln.strip()]
        stamp = next(i for i, ln in enumerate(lines) if "آخر تحديث" in ln)
        assert lines[stamp].endswith("2026/10/1")
        assert lines[-1] == "— يُحدَّث تلقائياً بواسطة Master Studio gateway"

    def test_user_supplied_text_is_html_escaped(self):
        cat = Catalog.from_dict("x", spec(notes=["a <b> & c"]))
        assert "a &lt;b&gt; &amp; c" in render(cat, CHAT)

    def test_the_rendered_body_fits_a_telegram_message(self):
        assert check_rendered(render(build(), CHAT)) == []

    def test_render_refuses_a_body_that_would_be_chopped_by_telegram(self):
        cat = Catalog.from_dict("x", spec(notes=["x" * 5000]))
        with pytest.raises(CatalogError) as exc:
            render(cat, CHAT)
        assert "4096" in str(exc.value)

    def test_check_rendered_flags_unbalanced_html(self):
        # the renderer owns the markup, so this guards the guard: a stray tag
        # would render as literal text in Telegram and break every link after it
        assert check_rendered('<a href="x">y') == ["unclosed <a>"]


# ------------------------------------------------------------ collapse ----


class TestCollapse:
    def test_notes_live_inside_an_expandable_blockquote(self):
        body = render(build(), CHAT)
        assert "<blockquote expandable>" in body
        assert "كل ملزمة مع كويزها" in body
        start = body.index("<blockquote expandable>")
        assert body.index("كل ملزمة مع كويزها") > start

    def test_no_notes_means_no_blockquote(self):
        assert "<blockquote" not in render(build(notes=[]), CHAT)

    def test_notes_can_be_kept_plain(self):
        body = render(build(collapse=[]), CHAT)
        assert "<blockquote" not in body

    def test_units_can_be_collapsed_when_a_subject_grows(self):
        body = render(build(collapse=["notes", "units"]), CHAT)
        assert body.count("<blockquote expandable>") == 2
        start, end = body.index("<blockquote"), body.index("</blockquote>")
        assert f"https://t.me/c/{INTERNAL}/60" in body[start:end]

    def test_the_header_and_the_footer_never_collapse(self):
        body = render(build(collapse=["notes", "units"]), CHAT)
        assert body.startswith("📗")
        assert body.rstrip().endswith("gateway")


# ------------------------------------------------------- pending subject ---


class TestPendingSubject:
    def test_an_empty_subject_says_it_is_waiting(self):
        cat = Catalog.from_dict(
            "06-Artificial-Intelligence",
            spec(subject="الذكاء الاصطناعي", units=[], notes=[],
                 pending="بانتظار المحاضرة الأولى"),
        )
        body = render(cat, CHAT)
        assert "بانتظار المحاضرة الأولى" in body
        assert "ملزمة" not in body
        assert "🏷 الوحدات : —" in body


# ------------------------------------------------------- shipped cards ----


def shipped():
    """(key, Catalog, chat_id) for every real catalog file."""
    registry = Registry(seed=False)
    out = []
    for path in sorted(CATALOG_DIR.glob("*.json")):
        cat = Catalog.load(path)
        out.append((path.stem, cat, int(registry.get(path.stem)["chat_id"])))
    return out


class TestShippedCards:
    def test_every_material_subject_has_a_catalog_file(self):
        keys = {p.stem for p in CATALOG_DIR.glob("*.json")}
        assert keys == set(SUBJECT_KEYS), keys ^ set(SUBJECT_KEYS)

    def test_every_shipped_card_renders_clean(self):
        for key, cat, chat_id in shipped():
            problems = check_rendered(render(cat, chat_id))
            assert problems == [], f"{key}: {problems}"

    def test_every_shipped_card_opens_on_an_arabic_subject_name(self):
        for key, cat, _chat in shipped():
            first = render(cat, CHAT).splitlines()[0]
            assert re.match(r"^\S+\s+\S", first), f"{key}: {first!r}"
            assert not first[0].isdigit(), f"{key} still opens on its ordinal"

    def test_the_card_sits_above_every_message_it_links_to(self):
        # the index must be the first thing you scroll to in its topic
        for key, cat, chat_id in shipped():
            for unit in cat.units:
                for link in unit.links:
                    assert link.message_id > cat.card_message_id, (
                        f"{key}: card {cat.card_message_id} is below "
                        f"message {link.message_id}"
                    )

    def test_card_ids_are_unique_across_subjects(self):
        ids = [cat.card_message_id for _k, cat, _c in shipped()]
        assert len(ids) == len(set(ids))

    def test_every_shipped_link_points_into_the_registry_chat(self):
        for key, cat, chat_id in shipped():
            body = render(cat, chat_id)
            for href in re.findall(r'href="([^"]+)"', body):
                assert href.startswith(f"https://t.me/c/{str(chat_id)[4:]}/"), key

    def test_a_shipped_card_is_never_missing_its_freshness_stamp(self):
        for key, cat, chat_id in shipped():
            assert "📮 آخر تحديث" in render(cat, chat_id), key


# ------------------------------------------------------------ push tool ----


class TestPush:
    def test_global_flags_precede_the_subcommand(self):
        # `tg.py --live edit ...` -- a trailing --live lands on the subparser
        argv = build_edit_argv("01-Cyber-Security", 7, "body", live=True,
                               dry_run=False, as_json=True)
        assert argv.index("--live") < argv.index("edit")

    def test_the_edit_targets_the_pinned_card_and_forces_html(self):
        argv = build_edit_argv("05-Soft-Computing", 15, "hello")
        assert argv[argv.index("edit") + 1] == "--subject"
        assert argv[argv.index("--message-id") + 1] == "15"
        assert argv[argv.index("--text") + 1] == "hello"
        assert "--html" in argv

    def test_the_actor_travels_as_a_global_flag(self):
        # the ACL needs a driver id on every non-local verb; without one the
        # push comes back `denied` instead of `authorized`
        argv = build_edit_argv("01-Cyber-Security", 7, "hi", actor=OWNER)
        assert argv[argv.index("--actor") + 1] == str(OWNER)
        assert argv.index("--actor") < argv.index("edit")

    def test_no_actor_means_the_acl_denies_the_push(self, capsys):
        code = tg_cli.main(
            build_edit_argv("01-Cyber-Security", 7, "hi", dry_run=True,
                            as_json=True, actor=None)
        )
        payload = json.loads(capsys.readouterr().out)
        assert code != 0
        assert payload["authorized"] is False
        assert "actor" in payload["reason"]

    def test_the_push_payload_is_parsed_by_the_real_cli(self, capsys):
        # proves build_edit_argv() produces something the gateway accepts
        code = tg_cli.main(
            build_edit_argv("01-Cyber-Security", 7, "hi", dry_run=True,
                            as_json=True, actor=OWNER)
        )
        out = json.loads(capsys.readouterr().out)
        assert code == 0
        assert out["dry_run"] is True
        assert out["action"]["verb"] == "edit"
        assert out["action"]["message_id"] == 7

    def test_a_dry_run_never_builds_a_transport(self, monkeypatch, capsys):
        def explode(**_kw):
            raise AssertionError("the network was reached on a dry run")

        monkeypatch.setattr(tg_cli, "build_transport", explode)
        code = catalog_main(["--push", "01-Cyber-Security", "--dry-run", "--json"])
        payload = json.loads(capsys.readouterr().out)
        assert code == 0
        assert payload["status"] == "ok"
        assert payload["results"][0]["status"] == "authorized"

    def test_the_default_push_is_a_dry_run(self, monkeypatch, capsys):
        def explode(**_kw):
            raise AssertionError("a push without --live must stay offline")

        monkeypatch.setattr(tg_cli, "build_transport", explode)
        assert catalog_main(["--push", "01-Cyber-Security", "--json"]) == 0
        payload = json.loads(capsys.readouterr().out)
        assert payload["results"][0]["dry_run"] is True

    def test_an_unknown_subject_lists_the_known_ones(self, capsys):
        code = catalog_main(["--push", "07-Nothing", "--dry-run", "--json"])
        payload = json.loads(capsys.readouterr().out)
        assert code != 0
        assert "01-Cyber-Security" in payload["error"]

    def test_list_shows_every_shipped_card(self, capsys):
        assert catalog_main(["--list", "--json"]) == 0
        payload = json.loads(capsys.readouterr().out)
        assert set(payload["subjects"]) == set(SUBJECT_KEYS)


class TestTheWorkflowIsDiscoverable:
    """The next agent has to find this without re-deriving it.

    "ضيفها" is a recurring request, not a one-off. If the skill stops naming
    the launcher or the merge target, the cards drift back into being hand-
    edited Telegram messages with no file behind them — and hand edits are
    exactly what the file exists to prevent.
    """

    SKILL = (
        Path(__file__).resolve().parent.parent
        / ".mimocode" / "skills" / "telegram" / "SKILL.md"
    )

    def _text(self) -> str:
        assert self.SKILL.is_file(), f"skill file missing: {self.SKILL}"
        return self.SKILL.read_text(encoding="utf-8")

    def test_the_launcher_is_named(self):
        assert "tg_catalog" in self._text()

    def test_the_merge_target_is_named(self):
        assert "00_STUDIO_HUB/telegram/catalog" in self._text()

    def test_the_unit_rule_is_named(self):
        # a unit is a lecture FILE, never a calendar week
        assert "lecture file, not a calendar week" in self._text()
