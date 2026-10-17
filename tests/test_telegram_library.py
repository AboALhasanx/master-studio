"""Contract tests for the personal bot library (no network, no Telegram).

The library publishes into the student's own DM, so the parts worth pinning are
the ones that keep it safe and consistent: the caption keeps the published
shape, the tags are per-subject, a bad manifest is blocked before anything
leaves the machine, and **nothing is sent without --send**.
"""

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "90_Shared_Toolbox"))

from telegram import cli, library  # noqa: E402


def _item(tmp_path, **over):
    doc = tmp_path / "lesson.pdf"
    doc.write_bytes(b"%PDF-1.4 test")
    item = {
        "file": str(doc),
        "subject": "01-Cyber-Security",
        "title": "الجابتر الثاني",
        "kind": "lecture",
        "display": "أمن المعلومات - الجابتر الثاني.pdf",
    }
    item.update(over)
    return item


def test_caption_keeps_the_published_shape_and_adds_tags(tmp_path):
    caption = library.build_caption(_item(
        tmp_path, catalog_link="https://t.me/c/3710711332/181"))
    lines = caption.splitlines()
    assert lines[0] == "● أمن المعلومات"
    assert lines[1] == "● الجابتر الثاني"
    assert lines[2] == ""
    assert 'الفهرس : <a href="https://t.me/c/3710711332/181">كتالوج المادة</a>' in lines
    assert lines[-1] == "#أمن_المعلومات · #محاضرة"


def test_every_subject_gets_its_own_tag():
    tags = {library.subject_tag(k) for k in library.SUBJECT_LABELS}
    assert len(tags) == len(library.SUBJECT_LABELS), "subject tags must not collide"
    assert all(tag.startswith("#") and " " not in tag for tag in tags)


def test_subject_labels_match_the_published_cards():
    """The library must speak the same words as the topic cards."""
    catalog = ROOT / "00_STUDIO_HUB/telegram/catalog"
    for path in catalog.glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        key = path.stem
        if key in library.SUBJECT_LABELS:
            assert library.SUBJECT_LABELS[key] == data["subject"], key


def test_validation_blocks_bad_items(tmp_path):
    good = _item(tmp_path)
    assert library.validate_items([good]) == []

    long_name = "ح" * 40 + ".pdf"          # 80 bytes, past the 62-byte budget
    problems = library.validate_items([
        _item(tmp_path, file=str(tmp_path / "missing.pdf")),
        _item(tmp_path, subject="99-Nope"),
        _item(tmp_path, title="   "),
        _item(tmp_path, display=long_name),
    ])
    joined = "\n".join(problems)
    assert "file not found" in joined
    assert "unknown subject" in joined
    assert "no title" in joined
    assert "display name" in joined and "62 B" in joined


def test_load_manifest_accepts_both_shapes(tmp_path):
    items = [{"file": "a.pdf", "subject": "01-Cyber-Security", "title": "x"}]
    bare = tmp_path / "bare.json"
    bare.write_text(json.dumps(items), encoding="utf-8")
    wrapped = tmp_path / "wrapped.json"
    wrapped.write_text(json.dumps({"items": items}), encoding="utf-8")
    assert library.load_manifest(bare) == items
    assert library.load_manifest(wrapped) == items

    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps({"items": "not a list"}), encoding="utf-8")
    with pytest.raises(ValueError):
        library.load_manifest(bad)


def test_summary_counts_files_and_size(tmp_path):
    table = library.summary_table([_item(tmp_path)])
    assert "1 file(s)" in table
    assert "أمن المعلومات" in table
    assert "#أمن_المعلومات" in table


def test_library_chat_comes_from_env(monkeypatch):
    monkeypatch.setenv(library.ENV_LIBRARY_CHAT, "12345")
    assert library.library_chat_from_env() == 12345
    monkeypatch.setenv(library.ENV_LIBRARY_CHAT, "")
    assert library.library_chat_from_env() is None
    monkeypatch.setenv(library.ENV_LIBRARY_CHAT, "not-a-number")
    assert library.library_chat_from_env() is None


def test_the_cli_exposes_the_library_command():
    subs = cli.build_parser()._subparsers._group_actions[0].choices
    assert "library" in subs
    flags = {opt for a in subs["library"]._actions for opt in a.option_strings}
    assert {"--manifest", "--send", "--chat", "--subject"} <= flags


def test_a_proposal_never_touches_the_transport(tmp_path, monkeypatch, capsys):
    """Without --send the command must stop at the proposal — no transport."""
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps({"items": [_item(tmp_path)]}), encoding="utf-8")

    def explode(*_a, **_kw):
        raise AssertionError("the transport must not be built for a proposal")

    monkeypatch.setattr(cli, "build_transport", explode)
    monkeypatch.setenv(library.ENV_LIBRARY_CHAT, "999")

    code = cli.main(["library", "--manifest", str(manifest)])
    out = capsys.readouterr().out
    assert code == 0
    assert "proposal only" in out
