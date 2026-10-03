"""Contract between LEARNER_MODEL.md schema and the dashboard parsers,
plus vault-write guards for the mobile import endpoint.

`parse_learner_model()` and `get_folder_stats()` in 91_Dashboard/app.py use
regex/glob conventions over hub markdown. If the learner schema drifts
(new columns, renamed anchors), the dashboard silently shows zeros — this
file pins the contract. The import tests prove a mobile re-import can never
silently clobber an existing bank (P1 fix).
"""

import json
import sys
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parent.parent
dashboard_path = BASE_DIR / "91_Dashboard"
if str(dashboard_path) not in sys.path:
    sys.path.insert(0, str(dashboard_path))

import app as dashboard_app  # noqa: E402
from app import app  # noqa: E402


@pytest.fixture
def client():
    app.config["TESTING"] = True
    limiter = getattr(dashboard_app, "limiter", None)
    if limiter is not None:
        limiter.reset()
    with app.test_client() as test_client:
        yield test_client
    if limiter is not None:
        limiter.reset()


# ------------------------------------------------- learner-model contract
def test_mastered_rows_parse_with_scores_and_dates():
    learner = dashboard_app.parse_learner_model()
    assert len(learner["mastered"]) >= 8, "mastered concepts vanished from dashboard parse"
    for row in learner["mastered"]:
        assert 0 <= row["score"] <= 100
        assert len(row["date"]) == 10 and row["date"][4] == "-" and row["date"][7] == "-"
        assert row["concept"] and row["concept"] != "Concept"
        assert row["subject"].startswith("0")


def test_review_rows_parse_with_logged_dates():
    learner = dashboard_app.parse_learner_model()
    assert len(learner["review"]) >= 20, "review queue vanished from dashboard parse"
    for row in learner["review"]:
        assert row["concept"] and row["concept"] not in ("Concept / Error", "Concept")
        assert len(row["added"]) == 10
        assert row["priority"]


def test_emoji_flagged_priority_still_parses():
    """R11 carries a 🔴 flag before High — the top-priority Integrity item
    must never go invisible on the dashboard."""
    learner = dashboard_app.parse_learner_model()
    integrity = [r for r in learner["review"] if "Integration" in r["concept"]]
    assert integrity, "Integrity-not-Integration row missing from parse"
    assert integrity[0]["priority"] == "High"


def test_table_headers_never_parsed_as_data():
    learner = dashboard_app.parse_learner_model()
    concepts = [r["concept"] for r in learner["mastered"]]
    concepts += [r["concept"] for r in learner["review"]]
    banned = {"Concept", "Concept / Error", "ID", "Subject"}
    assert not (set(concepts) & banned), "parser swallowed a markdown header row"


def test_summary_stats_parse_as_sane_numbers():
    learner = dashboard_app.parse_learner_model()
    assert 0 <= learner["accuracy"] <= 100
    assert 0.0 <= learner["confidence"] <= 5.0
    assert learner["quizzes_taken"] >= 2


def test_folder_stats_excludes_scaffolding_notes():
    stats = dashboard_app.get_folder_stats()
    ase_notes_dir = BASE_DIR / "01_Semester_1" / "04_Advanced_Software_Eng" / "03_Study_Notes"
    total_md = len(list(ase_notes_dir.glob("*.md")))
    assert stats["04_Advanced_Software_Eng"]["notes"] < total_md, (
        "scaffolding (BUILD_PLAN / Study_Plan_and_Index) must be excluded from notes count"
    )


def test_opencode_guide_renders_without_hardcoded_version(client):
    res = client.get("/opencode")
    assert res.status_code == 200
    body = res.get_data(as_text=True)
    assert "V2.0.15" not in body, "hardcoded version badge must be dynamic or neutral"


# ------------------------------------------------- import collision guard
def _quiz_payload(subject_id, quiz_id, marker):
    return {
        "subject_id": subject_id,
        "quiz_id": quiz_id,
        "topic": "collision probe",
        "questions": [
            {
                "question": "probe?",
                "question_ar": "probe?",
                "options": ["a", "b", "c", "d"],
                "options_ar": ["a", "b", "c", "d"],
                "options_en": ["a", "b", "c", "d"],
                "answer": "A",
                "correct": 0,
                "concept_id": "probe",
                "bloom_level": "Understand",
                "explanation": marker,
            }
        ],
    }


@pytest.fixture
def isolated_base(monkeypatch, tmp_path):
    quiz_dir = tmp_path / "01_Semester_1" / "Subj" / "07_Quizzes_&_Anki"
    quiz_dir.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(dashboard_app, "BASE", tmp_path)
    return tmp_path


def test_import_identical_payload_is_idempotent(client, isolated_base):
    first = client.post("/api/quiz/import", json=_quiz_payload("Subj", "Quiz_Probe", "v1"))
    assert first.status_code == 200
    second = client.post("/api/quiz/import", json=_quiz_payload("Subj", "Quiz_Probe", "v1"))
    assert second.status_code == 200
    files = list((isolated_base / "01_Semester_1" / "Subj" / "07_Quizzes_&_Anki").glob("*.json"))
    assert len(files) == 1, "identical re-import must not duplicate the bank"
    assert second.get_json()["imported"][0]["quiz_id"] == "Quiz_Probe"


def test_import_differing_payload_never_overwrites(client, isolated_base):
    client.post("/api/quiz/import", json=_quiz_payload("Subj", "Quiz_Probe", "v1"))
    res = client.post("/api/quiz/import", json=_quiz_payload("Subj", "Quiz_Probe", "v2-CHANGED"))
    assert res.status_code == 200
    entry = res.get_json()["imported"][0]
    assert entry["quiz_id"] == "Quiz_Probe_2", "clashing import must take a suffixed slot"
    assert "note" in entry
    quiz_dir = isolated_base / "01_Semester_1" / "Subj" / "07_Quizzes_&_Anki"
    original = json.loads((quiz_dir / "Quiz_Probe.json").read_text(encoding="utf-8"))
    texts = json.dumps(original, ensure_ascii=False)
    assert "v1" in texts and "v2-CHANGED" not in texts, "original bank must survive intact"
