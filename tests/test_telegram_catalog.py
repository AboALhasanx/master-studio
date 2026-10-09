"""Subject catalog card — one message per subject that carries the whole index.

Transplanted from the student's bachelor channels (``cs_stg4`` /
``cs_stg4_onefile``), where a subject is ONE message rather than one message
per asset. The card ships as the **caption of a document**: the first message
of every subject topic is a file (today a one-page placeholder, tomorrow the
merged official lectures), and its caption is the index.

The caption states, in this order:

* the subject name (Arabic, no ``01`` prefix);
* the instructor's full Arabic name **with the scientific title**, taken from
  the semester schedule ``.docx`` rather than transcribed — ``ا.م.د`` and
  ``ا.د`` are different ranks and a card that drops the rank misrepresents
  the course;
* an embedded link to a translated copy, **only if one exists** (omitted
  otherwise, never left as a placeholder);
* the chapter numbers contained in the merged file;
* ``● كل جابتر بملف :`` and then one ``【ordinal (link)】`` per chapter,
  three to a row.

What the caption must NOT carry is pinned as hard as what it must: no
``<blockquote>``, no vault path, no build footer, no descriptive chapter
titles inside the brackets, no per-link icon. Every one of those was removed
by request — the card is an index, and an index that annotates itself stops
being an index.

Because the card is a caption, ``TELEGRAM_CAPTION_LIMIT`` (1024) — not the
4096 text limit — is the ceiling that decides whether it ships at all.
"""

import json
import re
import sys
from pathlib import Path

import pytest

# Ensure 90_Shared_Toolbox is on sys.path (same pattern as test_telegram_gateway)
toolbox_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox"
if str(toolbox_path) not in sys.path:
    sys.path.insert(0, str(toolbox_path))

from telegram import cli as tg_cli  # noqa: E402
from telegram.catalog import (  # noqa: E402
    CATALOG_DIR,
    ROW_WIDTH,
    SUBJECT_KEYS,
    Catalog,
    CatalogError,
    arabic_ordinal,
    build_edit_argv,
    build_publish_argv,
    catalog_main,
    check_rendered,
    message_link,
    pdf_path,
    render,
)
from telegram.links import parse_message_link  # noqa: E402
from telegram.registry import Registry  # noqa: E402
from telegram.structure import COLOR_SUBJECT, STRUCTURE, topic_link  # noqa: E402

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
        "icon": "◆",
        "subject": "أمن المعلومات",
        "doctor": "أ.م.د. هدى لفتة مجيد",
        "schedule": "الأحد 08:30 — 10:30",
        "updated": "2026/10/1",
        "chapters": [101, 102],
        "pdf": "00_STUDIO_HUB/telegram/catalog/placeholders/01.pdf",
        "translation": None,
        "catalog_message_id": None,
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
        # two builders must never drift into two different link dialects
        assert topic_link(CHAT, 6) == message_link(CHAT, 6)


class TestOrdinals:
    def test_the_first_nine(self):
        got = [arabic_ordinal(i) for i in range(1, 10)]
        assert got == [
            "الأول", "الثاني", "الثالث", "الرابع", "الخامس",
            "السادس", "السابع", "الثامن", "التاسع",
        ]

    def test_the_tens_and_teens_carry_the_right_elision(self):
        assert arabic_ordinal(10) == "العاشر"
        assert arabic_ordinal(11) == "الحادي عشر"  # not "الأول عشر"
        assert arabic_ordinal(13) == "الثالث عشر"
        assert arabic_ordinal(20) == "العشرون"

    def test_compound_ordinals_join_with_waw(self):
        assert arabic_ordinal(21) == "الحادي والعشرون"
        assert arabic_ordinal(32) == "الثاني والثلاثون"

    def test_a_zero_ordinal_is_refused(self):
        with pytest.raises(ValueError):
            arabic_ordinal(0)


# ----------------------------------------------------------- structure ----


class TestPayloadShape:
    def test_a_missing_required_key_is_a_structural_error(self):
        for key in ("icon", "subject", "doctor", "schedule", "updated",
                    "chapters", "pdf"):
            bad = spec()
            bad.pop(key)
            with pytest.raises(CatalogError) as exc:
                Catalog.from_dict("01-Cyber-Security", bad)
            assert key in str(exc.value)

    def test_a_chapter_must_point_at_a_positive_message(self):
        with pytest.raises(CatalogError):
            Catalog.from_dict("x", spec(chapters=[101, 0]))

    def test_chapters_may_be_empty_but_must_be_a_list(self):
        assert Catalog.from_dict("x", spec(chapters=[])).chapters == ()
        with pytest.raises(CatalogError):
            Catalog.from_dict("x", spec(chapters="101"))

    def test_a_catalog_message_id_is_optional_until_the_card_exists(self):
        assert Catalog.from_dict("x", spec()).catalog_message_id is None
        assert Catalog.from_dict("x", spec(catalog_message_id=9)).catalog_message_id == 9
        with pytest.raises(CatalogError):
            Catalog.from_dict("x", spec(catalog_message_id=0))

    def test_a_translation_may_be_absent_but_never_empty(self):
        assert Catalog.from_dict("x", spec()).translation is None
        assert Catalog.from_dict("x", spec(translation="")).translation is None
        with pytest.raises(CatalogError):
            Catalog.from_dict("x", spec(translation=" "))

    def test_references_default_to_empty_for_every_older_card(self):
        # The field was added after the first cards shipped; absence must mean
        # "no sources recorded", never a structural error.
        assert Catalog.from_dict("x", spec()).references == ()
        assert Catalog.from_dict("x", spec(references=[])).references == ()

    def test_a_reference_records_the_post_and_its_edition(self):
        cat = Catalog.from_dict("x", spec(references=[
            {"message_id": 210, "source": "Software Engineering — Ian "
                                          "Sommerville", "edition": "9th Edition"},
        ]))
        assert len(cat.references) == 1
        ref = cat.references[0]
        assert ref.message_id == 210
        assert ref.source.endswith("Sommerville")
        assert ref.edition == "9th Edition"

    def test_a_reference_must_be_a_list_of_objects(self):
        with pytest.raises(CatalogError):
            Catalog.from_dict("x", spec(references="210"))
        with pytest.raises(CatalogError):
            Catalog.from_dict("x", spec(references=[210]))

    def test_a_reference_missing_a_field_is_a_structural_error(self):
        for drop in ("message_id", "source", "edition"):
            entry = {"message_id": 210, "source": "S", "edition": "E"}
            entry.pop(drop)
            with pytest.raises(CatalogError) as exc:
                Catalog.from_dict("x", spec(references=[entry]))
            assert drop in str(exc.value)

    def test_a_reference_must_point_at_a_positive_post(self):
        with pytest.raises(CatalogError):
            Catalog.from_dict("x", spec(references=[
                {"message_id": 0, "source": "S", "edition": "E"}]))


# -------------------------------------------------------------- render ----


class TestRenderedCard:
    def test_the_header_carries_no_ordinal_prefix(self):
        assert render(build(), CHAT).splitlines()[0] == "◆ أمن المعلومات"

    def test_the_doctor_is_rendered_in_arabic_with_her_scientific_rank(self):
        body = render(build(), CHAT)
        assert "الدكتور : أ.م.د. هدى لفتة مجيد" in body

    def test_the_chapter_numbers_state_what_is_inside_the_merged_file(self):
        assert "الجابتر : 1,2" in render(build(), CHAT)

    def test_an_empty_subject_renders_a_dash_for_the_chapter_field(self):
        body = render(Catalog.from_dict("x", spec(chapters=[])), CHAT)
        assert "الجابتر : —" in body

    def test_the_chapter_heading_is_verbatim(self):
        assert "● كل جابتر بملف : —" not in render(build(), CHAT)
        assert "● كل جابتر بملف :" in render(build(), CHAT)

    def test_a_chapter_is_an_ordinal_wrapped_around_a_link(self):
        # the word is the link: ``الأول`` opens the lecture
        body = render(build(), CHAT)
        assert f'【<a href="https://t.me/c/{INTERNAL}/101">الأول</a>】' in body
        assert f'【<a href="https://t.me/c/{INTERNAL}/102">الثاني</a>】' in body

    def test_no_address_is_ever_shown_to_the_reader(self):
        """The card is an index, not a wall of addresses.

        Telegram prints verbatim what it is given, so a URL typed next to the
        ordinal shows as a URL — the exact thing the student asked to stop
        seeing. Every address has to sit inside the label that carries it.
        """
        body = render(build(), CHAT)
        visible = re.sub(r'<a href="[^"]+">[^<]*</a>', "", body)
        assert "http" not in visible, visible

    def test_a_chapter_carries_no_description(self):
        # "بدون تفاصيل اسم الجابتر او اي شي" — the bracket holds ordinal+link,
        # never the "الوحدة — العنوان" subtitle the earlier cards carried
        brackets = re.findall(r"【([^】]*)】", render(build(), CHAT))
        assert brackets
        for bracket in brackets:
            link = re.fullmatch(r'<a href="([^"]+)">([^<]+)</a>', bracket)
            assert link, bracket
            href, label = link.groups()
            assert href.startswith(f"https://t.me/c/{INTERNAL}/"), bracket
            assert "—" not in label and ":" not in label, label

    def test_chapters_are_grouped_three_to_a_row(self):
        wide = spec(chapters=list(range(101, 110)))
        body = render(Catalog.from_dict("x", wide), CHAT)
        rows = [ln for ln in body.splitlines() if "】" in ln]
        assert ROW_WIDTH == 3
        assert len(rows) == 3
        for row in rows:
            assert row.count("【") == ROW_WIDTH

    def test_rows_are_separated_by_a_blank_line(self):
        wide = spec(chapters=list(range(101, 110)))
        lines = render(Catalog.from_dict("x", wide), CHAT).splitlines()
        indexes = [i for i, ln in enumerate(lines) if "】" in ln]
        for a, b in zip(indexes, indexes[1:]):
            assert lines[a + 1] == "", "chapter rows must not run together"

    def test_the_translation_link_appears_only_when_one_exists(self):
        body = render(build(translation="https://example.org/ar"), CHAT)
        assert f'<a href="https://example.org/ar">اضغط هنا</a>' in body
        assert render(build(), CHAT).find("مترجمة") == -1

    def test_the_translation_line_uses_the_bachelor_field_word(self):
        body = render(build(translation="https://example.org/ar"), CHAT)
        assert "المادة مترجمة" in body

    def test_the_freshness_stamp_closes_the_card(self):
        lines = [ln for ln in render(build(), CHAT).splitlines() if ln.strip()]
        assert lines[-1].startswith("آخر تحديث")
        assert lines[-1].endswith("2026/10/1")

    def test_user_supplied_text_is_html_escaped(self):
        body = render(build(subject="a <b> & c"), CHAT)
        assert "a &lt;b&gt; &amp; c" in body

    def test_the_rendered_body_fits_a_document_caption(self):
        assert check_rendered(render(build(), CHAT)) == []

    def test_render_refuses_a_caption_telegram_would_chop(self):
        # a caption is capped at 1024, not 4096 — overflow truncates the card
        with pytest.raises(CatalogError) as exc:
            render(build(schedule="x" * 2000), CHAT)
        assert "1024" in str(exc.value)

    def test_check_rendered_flags_unbalanced_html(self):
        assert check_rendered('<a href="x">y') == ["unclosed <a>"]

    def test_check_rendered_flags_an_address_printed_as_text(self):
        # the invariant this card shipped without: an href is hidden behind
        # its label, a URL written anywhere else is on screen for the reader
        body = (
            f'<a href="https://t.me/c/{INTERNAL}/101">الأول</a>\n'
            f"https://t.me/c/{INTERNAL}/102"
        )
        assert check_rendered(body) == [
            f"https://t.me/c/{INTERNAL}/102 is printed as text instead of "
            "being hidden in its label"
        ]

    def test_a_longer_limit_can_be_asked_for_explicitly(self):
        body = "x" * 1500
        assert check_rendered(body) != []
        assert check_rendered(body, limit=4096) == []


class TestWhatTheCardMustNotCarry:
    """The removals are pinned as hard as the additions.

    Each assertion names the thing it forbids, because a future pass that
    "helpfully" re-adds a footer or wraps the index in a quote is exactly
    the regression this class exists to catch.
    """

    def test_no_blockquote(self):
        assert "<blockquote" not in render(build(), CHAT)

    def test_no_vault_path(self):
        body = render(build(), CHAT)
        assert "📂" not in body
        assert "00_STUDIO_HUB" not in body

    def test_no_build_footer(self):
        assert "gateway" not in render(build(), CHAT)

    def test_no_per_link_icons(self):
        body = render(build(), CHAT)
        assert "📎" not in body and "🎯" not in body

    def test_no_notes_or_observations_section(self):
        assert "ملاحظات" not in render(build(), CHAT)

    def test_the_card_carries_no_emoji_at_all(self):
        # "ولا تستعمل ايموجيات" — the whole card is monochrome: the header
        # marker (◆), the section head (●) and the brackets (【】) are text
        # glyphs, and every other line is a plain Arabic label.
        body = render(build(), CHAT)
        emoji = [
            ch for ch in body
            if 0x1F300 <= ord(ch) <= 0x1FAFF or 0x2600 <= ord(ch) <= 0x27BF
            or 0x2B00 <= ord(ch) <= 0x2BFF or ord(ch) == 0xFE0F
        ]
        assert emoji == [], f"emoji leaked into the card: {emoji}"


# ------------------------------------------------------- pending subject ---


class TestEmptySubject:
    def test_no_chapters_renders_an_em_dash_row(self):
        body = render(Catalog.from_dict("x", spec(chapters=[])), CHAT)
        assert "● كل جابتر بملف : —" in body

    def test_an_empty_subject_still_carries_its_file(self):
        # a subject with no lectures ships the blank placeholder, not a
        # card with nothing attached — "المهم ملف"
        assert Catalog.from_dict("x", spec(chapters=[])).pdf


# ------------------------------------------------------- shipped cards ----


def shipped():
    """(key, Catalog, chat_id) for every real catalog file.

    ``chat_id`` is ``None`` when the subject is not bound: the registry is
    gitignored local state, so a fresh checkout has no bindings in it, and
    callers that genuinely need one must say so rather than hit ``int(None)``.
    """
    registry = Registry(seed=False)
    known = set(registry.subjects())
    out = []
    for path in sorted(CATALOG_DIR.glob("*.json")):
        cat = Catalog.load(path)
        row = registry.get(path.stem) if path.stem in known else {}
        chat = row.get("chat_id")
        out.append((path.stem, cat, None if chat is None else int(chat)))
    return out


# Real booklets are rebuilt from `02_Raw_Materials`, which `.gitignore` already
# keeps out of the public repo (copyrighted textbook pages); only their merged
# and split copies live here, and they follow the same rule.
BOOKLET_DIRS = ("telegram/catalog/files/", "telegram/lectures/")


def _booklet_kept_out_of_git(path: Path) -> bool:
    """True only for an absent booklet inside a dir `.gitignore` reserves."""
    posix = str(path).replace("\\", "/")
    return any(marker in posix for marker in BOOKLET_DIRS)


class TestShippedCards:
    def test_every_material_subject_has_a_catalog_file(self):
        keys = {p.stem for p in CATALOG_DIR.glob("*.json")}
        assert keys == set(SUBJECT_KEYS), keys ^ set(SUBJECT_KEYS)

    def test_every_attachment_filename_fits_telegrams_safe_byte_budget(self):
        """Telegram slugifies an uploaded filename that runs past ~64 UTF-8 bytes.

        Probed against the live group: 59 B and 62 B kept their spaces, 67 B
        came back ``هندسة_البرمجيات_...`` with every run of punctuation turned
        into an underscore. Arabic charges 2 bytes per letter, so the bilingual
        ``عربي - إنجليزي`` names blow the budget first.
        """
        for key, cat, _chat in shipped():
            name = Path(cat.pdf).name
            size = len(name.encode("utf-8"))
            assert size <= 62, (
                f"{key}: {name!r} is {size} bytes — Telegram will replace its "
                "spaces with underscores; shorten the Latin half"
            )

    def test_no_attachment_filename_carries_a_numeric_prefix(self):
        """Names are ``عربي - إنجليزي`` only — never ``01-``/``02-``."""
        for key, cat, _chat in shipped():
            name = Path(cat.pdf).name
            assert not re.match(r"^\d+[-_ .]", name), f"{key}: {name!r}"

    def test_every_shipped_card_renders_clean(self):
        for key, cat, chat_id in shipped():
            # unbound checkouts (CI) still have a group to build links against
            problems = check_rendered(render(cat, chat_id if chat_id else CHAT))
            assert problems == [], f"{key}: {problems}"

    def test_every_shipped_card_opens_on_an_arabic_subject_name(self):
        for key, cat, _chat in shipped():
            first = render(cat, CHAT).splitlines()[0]
            assert not first.split(" ", 1)[1][0].isdigit(), f"{key} opens on a number"

    def test_every_shipped_doctor_carries_a_scientific_rank(self):
        # the ranks come from "Weekly Schedule.docx": ا.م.د for four subjects,
        # ا.د for two — a card that loses the rank misstates the course
        for key, cat, _chat in shipped():
            assert re.match(r"^(أ\.م\.د\.|أ\.د\.)\s", cat.doctor), (
                f"{key}: {cat.doctor!r} has no rank"
            )

    def test_chapter_ids_are_strictly_increasing_and_unique(self):
        for key, cat, _chat in shipped():
            assert list(cat.chapters) == sorted(set(cat.chapters)), key

    def test_the_declared_number_range_matches_the_chapter_count(self):
        for key, cat, _chat in shipped():
            match = re.search(r"الجابتر : ([\d,]+|—)", render(cat, CHAT))
            assert match, key
            if not cat.chapters:
                assert match.group(1) == "—", key
            else:
                expected = ",".join(str(i) for i in range(1, len(cat.chapters) + 1))
                assert match.group(1) == expected, key

    def test_every_shipped_link_points_into_the_registry_chat(self):
        """A card must point at the group its subject is actually bound to.

        `registry.json` is gitignored local state, so a CI checkout has no
        bindings in it: there is nothing to compare against, and inventing a
        group would only assert that a number equals itself. Where the
        subject *is* bound, render for the canonical group and require the
        links to land in that binding.
        """
        rows = [(k, c, chat) for k, c, chat in shipped() if chat is not None]
        if not rows:
            pytest.skip("registry.json is local-only: no subject is bound here")
        for key, cat, chat_id in rows:
            body = render(cat, CHAT)
            for href in re.findall(r'href="([^\"]+)"', body):
                assert href.startswith(f"https://t.me/c/{str(chat_id)[4:]}/"), key

    def test_every_shipped_card_names_an_existing_placeholder_pdf(self):
        # "المهم ملف" — a subject with nothing merged yet still ships a file,
        # so the first message of the topic is never a bare caption
        for key, cat, _chat in shipped():
            assert cat.pdf.endswith(".pdf"), key
            path = pdf_path(cat)
            if path.is_file():
                assert path.stat().st_size > 0, f"{key}: empty PDF at {cat.pdf}"
                continue
            assert _booklet_kept_out_of_git(path), (
                f"{key}: no PDF at {cat.pdf} and it is not a gitignored booklet"
            )

    def test_only_the_two_booklet_dirs_are_tolerated_when_absent(self):
        """A fresh clone has no booklets — but nothing else may go missing.

        Booklets are rebuilt from ``02_Raw_Materials``, which ``.gitignore``
        already keeps out of the public repo (copyrighted textbook pages).
        """
        assert _booklet_kept_out_of_git(
            Path("00_STUDIO_HUB/telegram/catalog/files/booklet.pdf")
        )
        assert _booklet_kept_out_of_git(
            Path("00_STUDIO_HUB/telegram/lectures/chapter.pdf")
        )
        for absent in (
            Path("00_STUDIO_HUB/telegram/catalog/placeholders/gone.pdf"),
            Path("01_Semester_1/03_Data_Mining/03_Study_Notes/gone.pdf"),
            Path("somewhere/else/file.pdf"),
        ):
            assert not _booklet_kept_out_of_git(absent), absent

    def test_placeholder_chapters_are_off_the_group_s_real_range(self):
        # real traffic stops in the 80s; 100+ cannot collide with a live id
        for key, cat, _chat in shipped():
            assert all(mid >= 100 for mid in cat.chapters), key

    def test_an_unbound_registry_reports_none_instead_of_crashing(
        self, tmp_path, monkeypatch
    ):
        """`registry.json` is gitignored local state — a CI checkout has none.

        A subject that is merely unbound must surface as `chat_id is None`
        so callers can say so; surfacing as `int(None)` instead took out
        every shipped-card check with a TypeError unrelated to its subject.
        """
        import telegram.registry as registry_mod

        empty = tmp_path / "registry.json"
        empty.write_text(json.dumps({"subjects": {}}), encoding="utf-8")
        monkeypatch.setattr(registry_mod, "DEFAULT_REGISTRY_PATH", empty)

        rows = shipped()
        assert rows, "the shipped cards themselves are the fixture"
        assert all(chat is None for _key, _cat, chat in rows)


# ------------------------------------------------------- reference ledger --


class TestReferenceLedger:
    """Every published source book is tracked by the post it lives in.

    The 13 textbooks were posted into topics 86/87/88/89 on 2026-10-02, and the
    two English course books (New Headway Upper-Intermediate + Q Skills 4) into
    topic 85 on 2026-10-09; each catalog records the post ids beside the source
    and edition from its caption, so the JSON — not a chat scroll — is the
    inventory. The editions were read out of each PDF, so a mismatch here is a
    real defect, not a cosmetic one.
    """

    def test_the_five_subjects_that_received_sources_carry_them(self):
        by_key = {key: cat for key, cat, _chat in shipped()}
        for key in ("02-English-Language", "03-Data-Mining",
                    "04-Advanced-Software-Eng", "05-Soft-Computing",
                    "06-Artificial-Intelligence"):
            assert by_key[key].references, f"{key} lost its sources"
        # ...and a subject with no published source says so honestly.
        for key in ("01-Cyber-Security",):
            assert by_key[key].references == ()

    def test_the_ledger_covers_all_fifteen_posts(self):
        ids = [ref.message_id for _k, cat, _c in shipped()
               for ref in cat.references]
        assert len(ids) == 15, f"expected 15 source posts, got {len(ids)}"
        assert len(set(ids)) == len(ids), "a post is listed twice"

    def test_every_reference_is_traceable(self):
        for key, cat, _chat in shipped():
            for ref in cat.references:
                assert ref.message_id > 0, key
                assert ref.source.strip() and ref.edition.strip(), key
                assert "<" not in ref.source, key          # never HTML-leaking
                assert "\n" not in ref.source + ref.edition, key


# ------------------------------------------------------------ topic titles --


class TestTopicTitles:
    """Topic names are Arabic, monochrome and ordered (the layout contract).

    "اسماء بالعربية فقط للتوبكات واسمء المواد" — a topic title is what the eye
    scans first, so the rule is pinned here rather than left to whoever
    re-provisions the group next time.
    """

    def test_the_general_room_is_not_provisioned_twice(self):
        # General (id=1) is non-deletable and already named محادثة — the owner
        # renamed it (service message 39). A second chat topic would only
        # duplicate the room Telegram gives every forum for free.
        keys = {s.subject for s in STRUCTURE}
        assert "99-Chat" not in keys
        assert len(STRUCTURE) == 6

    def test_the_retired_utility_topics_are_not_provisioned(self):
        """The three utility topics were closed then deleted on 2026-10-02.

        Keeping them out of ``STRUCTURE`` is what stops a future ``structure``
        run from recreating them. The other half of the promise — that their
        registry keys still resolve to a clear *unbound* — lives in
        ``registry.RETIRED_SUBJECTS`` and is enforced and tested in
        ``test_telegram_gateway.py``.
        """
        keys = {s.subject for s in STRUCTURE}
        for retired in ("70-Exams-and-MCQ", "71-Progress-Analytics",
                        "90-Toolbox"):
            assert retired not in keys, retired

    def test_every_title_is_arabic_only(self):
        # "اسماء بالعربية فقط للتوبكات واسمء المواد" — a Latin word in a title
        # is exactly what made the old layout unreadable
        for spec_ in STRUCTURE:
            letters = [ch for ch in spec_.name if ch.isalpha()]
            assert letters and all(not ch.isascii() for ch in letters), spec_.name
            assert not any(ch.isascii() and ch.isalpha() for ch in spec_.name), spec_.name

    def test_every_title_is_emoji_free(self):
        emoji = lambda s: [                          # noqa: E731
            ch for ch in s
            if 0x1F300 <= ord(ch) <= 0x1FAFF or 0x2600 <= ord(ch) <= 0x27BF
            or 0x2B00 <= ord(ch) <= 0x2BFF or ord(ch) == 0xFE0F
        ]
        for spec_ in STRUCTURE:
            assert emoji(spec_.name) == [], f"{spec_.subject}: {spec_.name}"

    def test_taught_subjects_carry_no_numbers(self):
        # «شيل الارقام من اسماء التوبكتات ما اريد ال 01 ولا يم اي مادة» — the
        # prefix was noise: order is creation order, and Telegram lets the
        # owner drag topics into any order anyway
        taught = [s for s in STRUCTURE if s.icon_color == COLOR_SUBJECT]
        assert len(taught) == 6
        for spec_ in taught:
            assert not any(ch.isdigit() for ch in spec_.name), spec_.name
            assert spec_.name.split(" ", 1)[0] == "◆", spec_.name
            label = spec_.name.split(" ", 1)[1]
            assert label and not label[0].isascii(), spec_.name

    def test_no_utility_topics_remain_in_the_layout(self):
        # Every subject is its own hub now; the three utility topics were
        # retired, so the layout is exactly the six taught subjects (all of
        # them subject-coloured).
        utility = [s for s in STRUCTURE if s.icon_color != COLOR_SUBJECT]
        assert utility == []

    def test_titles_do_not_carry_vault_paths_or_english_course_names(self):
        for spec_ in STRUCTURE:
            assert "vault" not in spec_.card and "01_Semester" not in spec_.card
            assert "Dr." not in spec_.card and "CS5" not in spec_.card

    def test_the_pinned_card_has_no_gateway_footer(self):
        from telegram.structure import card_text

        text = card_text(STRUCTURE[0])
        assert "gateway" not in text and "يُحدَّث" not in text
        assert text.splitlines()[0] == STRUCTURE[0].name


# ------------------------------------------------------------ push tool ----


@pytest.fixture
def bound_registry(tmp_path, monkeypatch):
    """Bind every subject to this group for the duration of one test.

    `registry.json` is gitignored local state (`.gitignore:119`), so a CI
    checkout starts with nothing bound — anything that renders a card or
    resolves a topic must not depend on this machine's history to run.
    """
    import telegram.registry as registry_mod

    path = tmp_path / "registry.json"
    path.write_text(
        json.dumps(
            {
                "subjects": {
                    key: {
                        "description": "",
                        "chat_id": CHAT,
                        "thread_id": 7100 + index,
                        "topic_name": None,
                    }
                    for index, key in enumerate(SUBJECT_KEYS, start=1)
                }
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(registry_mod, "DEFAULT_REGISTRY_PATH", path)
    return path


@pytest.fixture
def unbound_registry(tmp_path, monkeypatch):
    """The other side of the same coin: a registry nothing is bound in."""
    import telegram.registry as registry_mod

    path = tmp_path / "registry.json"
    path.write_text(
        json.dumps(
            {
                "subjects": {
                    key: {
                        "description": "",
                        "chat_id": None,
                        "thread_id": None,
                        "topic_name": None,
                    }
                    for key in SUBJECT_KEYS
                }
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(registry_mod, "DEFAULT_REGISTRY_PATH", path)
    return path


class TestPush:
    def test_global_flags_precede_the_subcommand(self):
        # `tg.py --live publish ...` -- a trailing --live lands on the subparser
        argv = build_publish_argv("01-Cyber-Security", "x.pdf", "body",
                                  live=True, dry_run=False, as_json=True)
        assert argv.index("--live") < argv.index("publish")

    def test_the_publish_targets_the_subject_and_forces_html(self):
        argv = build_publish_argv("05-Soft-Computing", "a.pdf", "hello")
        assert argv[argv.index("publish") + 1] == "--subject"
        assert argv[argv.index("--file") + 1] == "a.pdf"
        assert argv[argv.index("--caption") + 1] == "hello"
        assert "--html" in argv

    def test_an_existing_card_is_edited_not_re_posted(self):
        # re-publishing a card that already exists would put a second copy at
        # the bottom of the topic and break "the first message is the catalog"
        argv = build_edit_argv("05-Soft-Computing", 15, "hello")
        assert argv[argv.index("edit") + 1] == "--subject"
        assert argv[argv.index("--message-id") + 1] == "15"
        assert argv[argv.index("--caption") + 1] == "hello"
        assert "--html" in argv

    def test_the_actor_travels_as_a_global_flag(self):
        # the ACL needs a driver id on every non-local verb; without one the
        # push comes back `denied` instead of `authorized`
        argv = build_edit_argv("01-Cyber-Security", 7, "hi", actor=OWNER)
        assert argv[argv.index("--actor") + 1] == str(OWNER)
        assert argv.index("--actor") < argv.index("edit")

    def test_no_actor_means_the_acl_denies_the_push(self, capsys, bound_registry):
        code = tg_cli.main(
            build_edit_argv("01-Cyber-Security", 7, "hi", dry_run=True,
                            as_json=True, actor=None)
        )
        payload = json.loads(capsys.readouterr().out)
        assert code != 0
        assert payload["authorized"] is False
        assert "actor" in payload["reason"]

    def test_the_push_payload_is_parsed_by_the_real_cli(
        self, capsys, bound_registry
    ):
        code = tg_cli.main(
            build_edit_argv("01-Cyber-Security", 7, "hi", dry_run=True,
                            as_json=True, actor=OWNER)
        )
        out = json.loads(capsys.readouterr().out)
        assert code == 0
        assert out["dry_run"] is True
        assert out["action"]["verb"] == "edit"
        assert out["action"]["message_id"] == 7

    def test_a_dry_run_never_builds_a_transport(
        self, monkeypatch, capsys, bound_registry
    ):
        def explode(**_kw):
            raise AssertionError("the network was reached on a dry run")

        monkeypatch.setattr(tg_cli, "build_transport", explode)
        code = catalog_main(["--push", "01-Cyber-Security", "--dry-run", "--json"])
        payload = json.loads(capsys.readouterr().out)
        assert code == 0
        assert payload["dry_run"] is True
        assert payload["results"][0]["status"] == "authorized"

    def test_a_dry_run_survives_a_fresh_clone_without_its_booklet(
        self, monkeypatch, capsys, tmp_path, bound_registry
    ):
        """Booklets are gitignored build artifacts — a CI checkout has none.

        A dry run only renders the card, so it must not demand the file;
        it flags the absence in the row instead. A live push still refuses,
        because there would be nothing to upload.
        """
        from telegram import catalog as catalog_mod

        src = CATALOG_DIR / "01-Cyber-Security.json"
        data = json.loads(src.read_text(encoding="utf-8"))
        data["pdf"] = "00_STUDIO_HUB/telegram/catalog/files/not-here-yet.pdf"
        (tmp_path / src.name).write_text(
            json.dumps(data, ensure_ascii=False), encoding="utf-8"
        )

        def explode(**_kw):
            raise AssertionError("the network was reached on a dry run")

        monkeypatch.setattr(tg_cli, "build_transport", explode)
        code = catalog_main([
            "--catalog-dir", str(tmp_path),
            "--push", "01-Cyber-Security", "--dry-run", "--json",
        ])
        payload = json.loads(capsys.readouterr().out)
        assert code == 0
        assert payload["results"][0]["file_missing"] is True

        with pytest.raises(CatalogError, match="no catalog file"):
            catalog_mod._push_one(
                tmp_path, Registry(str(bound_registry), seed=False),
                "01-Cyber-Security", live=True, dry_run=False, actor=OWNER,
            )

    def test_the_default_push_is_a_dry_run(
        self, monkeypatch, capsys, bound_registry
    ):
        def explode(**_kw):
            raise AssertionError("a push without --live must stay offline")

        monkeypatch.setattr(tg_cli, "build_transport", explode)
        catalog_main(["--push", "01-Cyber-Security", "--json"])
        payload = json.loads(capsys.readouterr().out)
        assert payload["dry_run"] is True

    def test_the_entry_point_needs_no_third_party_dotenv(self, monkeypatch, capsys):
        """`python-dotenv` is not in requirements.txt — and need not be.

        The vault ships its own dependency-free reader in `store`; importing
        the other one inside `catalog_main` is what turned a bare CI checkout
        into `ModuleNotFoundError` on every push test.
        """
        monkeypatch.setitem(sys.modules, "dotenv", None)  # any `import dotenv` fails
        assert catalog_main(["--list", "--json"]) == 0
        rows = json.loads(capsys.readouterr().out)
        assert rows, "the shipped cards are the fixture"

    @staticmethod
    def _card_with_message_id(tmp_path, message_id):
        """A copy of a real card with a chosen ``catalog_message_id``.

        The shipped JSONs now carry the ids of the live push, so asserting on
        them directly would test the deployment state instead of the code.
        """
        src = CATALOG_DIR / "06-Artificial-Intelligence.json"
        data = json.loads(src.read_text(encoding="utf-8"))
        data["catalog_message_id"] = message_id
        (tmp_path / src.name).write_text(
            json.dumps(data, ensure_ascii=False), encoding="utf-8"
        )
        return str(tmp_path)

    def test_a_card_without_a_message_id_is_published_not_edited(
        self, capsys, tmp_path, bound_registry
    ):
        # the first push creates the message; every later one edits it in place
        catalog_main(["--catalog-dir", self._card_with_message_id(tmp_path, None),
                      "--push", "06-Artificial-Intelligence", "--dry-run", "--json"])
        payload = json.loads(capsys.readouterr().out)
        assert payload["results"][0]["mode"] == "publish"

    def test_a_card_with_a_message_id_is_edited_in_place(
        self, capsys, tmp_path, bound_registry
    ):
        catalog_main(["--catalog-dir", self._card_with_message_id(tmp_path, 104),
                      "--push", "06-Artificial-Intelligence", "--dry-run", "--json"])
        payload = json.loads(capsys.readouterr().out)
        row = payload["results"][0]
        # a card that was already published is edited in place, never re-posted
        assert row["mode"] == "edit"
        assert row["catalog_message_id"] == 104

    def test_an_unknown_subject_lists_the_known_ones(self, capsys):
        code = catalog_main(["--push", "07-Nothing", "--dry-run", "--json"])
        payload = json.loads(capsys.readouterr().out)
        assert code != 0
        assert "01-Cyber-Security" in payload["error"]

    def test_list_shows_every_shipped_card(self, capsys):
        assert catalog_main(["--list", "--json"]) == 0
        payload = json.loads(capsys.readouterr().out)
        assert set(payload["subjects"]) == set(SUBJECT_KEYS)

    def test_print_renders_a_card_without_pushing_it(
        self, capsys, bound_registry
    ):
        assert catalog_main(["--print", "03-Data-Mining"]) == 0
        out = capsys.readouterr().out
        assert "تنقيب البيانات" in out
        assert "أ.م.د. أحمد شاكر عبد الرضا" in out

    def test_printing_an_unbound_subject_is_a_registry_problem(
        self, capsys, unbound_registry
    ):
        """`registry.json` is gitignored local state, so a fresh checkout has
        no binding: the card's links then have no group to point at.

        That is the registry's own error (exit 6, with a sentence saying
        which subject is missing) — not `TypeError: int() argument ...
        not 'NoneType'` thrown out of a CLI at the user.
        """
        code = catalog_main(["--print", "01-Cyber-Security", "--json"])
        payload = json.loads(capsys.readouterr().out)
        assert code == 6, payload
        assert payload["status"] == "error"
        assert "not bound" in payload["error"]

    def test_pushing_an_unbound_subject_is_a_registry_problem(
        self, capsys, unbound_registry
    ):
        # the same guard on the publish path, where `_push_one` used to
        # crash before it could report anything at all
        code = catalog_main(["--push", "01-Cyber-Security", "--json"])
        payload = json.loads(capsys.readouterr().out)
        assert code == 6, payload
        assert payload["status"] == "error"
        assert "not bound" in payload["error"]


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

    def test_the_skill_does_not_describe_a_removed_element(self):
        # §4.11 documented a blockquote and a vault path; both were cut
        text = self._text()
        section = text.split("### 4.11", 1)[1].split("\n## ", 1)[0]
        assert "<blockquote" not in section
        assert "📂 المسار" not in section
