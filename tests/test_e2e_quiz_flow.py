import sys
import json
import uuid
import shutil
from pathlib import Path
from datetime import datetime
from tempfile import TemporaryDirectory
import pytest

# Ensure 91_Dashboard and 90_Shared_Toolbox/tools are in sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
dashboard_path = BASE_DIR / "91_Dashboard"
toolbox_path = BASE_DIR / "90_Shared_Toolbox" / "tools"

if str(dashboard_path) not in sys.path:
    sys.path.insert(0, str(dashboard_path))
if str(toolbox_path) not in sys.path:
    sys.path.insert(0, str(toolbox_path))

import app as dashboard_app
from app import app
from quiz_engine import SEEN_UUIDS


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


@pytest.fixture
def isolated_hub(monkeypatch):
    """
    Creates an isolated copy of 00_STUDIO_HUB in a TemporaryDirectory
    and patches dashboard_app.HUB so real repository files are not mutated.
    """
    with TemporaryDirectory() as tmpdir:
        tmp_hub = Path(tmpdir) / "00_STUDIO_HUB"
        tmp_hub.mkdir(parents=True, exist_ok=True)
        
        real_hub = BASE_DIR / "00_STUDIO_HUB"
        if (real_hub / "PROGRESS_ANALYTICS.md").exists():
            shutil.copy2(real_hub / "PROGRESS_ANALYTICS.md", tmp_hub / "PROGRESS_ANALYTICS.md")
        if (real_hub / "LEARNER_MODEL.md").exists():
            shutil.copy2(real_hub / "LEARNER_MODEL.md", tmp_hub / "LEARNER_MODEL.md")
        
        # Point dashboard HUB to temporary hub
        monkeypatch.setattr(dashboard_app, "HUB", tmp_hub)
        
        # Ensure SEM1 points to the real 01_Semester_1 folder
        monkeypatch.setattr(dashboard_app, "SEM1", BASE_DIR / "01_Semester_1")
        
        yield tmp_hub


def test_e2e_fetch_real_quiz(client):
    """
    Test 1: Fetch the real quiz '04_Advanced_Software_Eng/Quiz_01_Software_Crisis'
    via the Flask test client and verify status 200, valid structure, and questions.
    """
    res = client.get("/api/quiz/04_Advanced_Software_Eng/Quiz_01_Software_Crisis")
    assert res.status_code == 200
    
    quiz_data = res.get_json()
    assert quiz_data is not None
    assert quiz_data.get("subject") == "04_Advanced_Software_Eng"
    assert "Software Crisis" in quiz_data.get("topic", "") or "Foundations" in quiz_data.get("topic", "")
    assert "questions" in quiz_data
    assert len(quiz_data["questions"]) >= 5

    # Check question schema
    first_q = quiz_data["questions"][0]
    assert "question" in first_q
    assert "options" in first_q
    assert "answer" in first_q
    assert "explanation" in first_q
    assert "Patriot" in first_q["question"] or "clock" in first_q["question"]

    # Also test with explicit .json suffix
    res_json = client.get("/api/quiz/04_Advanced_Software_Eng/Quiz_01_Software_Crisis.json")
    assert res_json.status_code == 200
    assert res_json.get_json()["subject"] == "04_Advanced_Software_Eng"


def test_e2e_submit_telemetry_with_reflection_and_lucky_guess(client, isolated_hub):
    """
    Test 2: Submit a full telemetry payload with unique UUID, 1 lucky guess,
    1 wrong answer with metacognitive reflection ('Calculation Slip' + note),
    and summary metrics. Verify 200 OK and success status.
    """
    sub_uuid = f"e2e-sub-{uuid.uuid4()}"
    payload = {
        "submission_uuid": sub_uuid,
        "subject_id": "04_Advanced_Software_Eng",
        "topic": "Lecture 01: Foundations, Patriot Failure, Brooks & Ethics",
        "summary": {
            "total": 5,
            "correct": 4,
            "wrong": 1,
            "percentage": 80.0,
            "avg_dwell_time_seconds": 14.5
        },
        "questions": [
            {
                "id": "q0",
                "question_index": 0,
                "is_correct": True,
                "is_lucky_guess": True,
                "dwell_time_seconds": 8.0
            },
            {
                "id": "q1",
                "question_index": 1,
                "is_correct": False,
                "is_lucky_guess": False,
                "dwell_time_seconds": 24.5,
                "reflection": {
                    "reason": "Calculation Slip",
                    "note": "Confused essential complexity with accidental compiler optimization"
                }
            },
            {
                "id": "q2",
                "question_index": 2,
                "is_correct": True,
                "is_lucky_guess": False,
                "dwell_time_seconds": 12.0
            },
            {
                "id": "q3",
                "question_index": 3,
                "is_correct": True,
                "is_lucky_guess": False,
                "dwell_time_seconds": 15.0
            },
            {
                "id": "q4",
                "question_index": 4,
                "is_correct": True,
                "is_lucky_guess": False,
                "dwell_time_seconds": 13.0
            }
        ]
    }

    res = client.post("/api/quiz/submit", json=payload)
    assert res.status_code == 200
    
    data = res.get_json()
    assert data.get("status") == "success"
    assert data.get("percentage") == 80.0


def test_e2e_idempotency_on_resubmission(client, isolated_hub):
    """
    Test 3: Verify idempotency when submitting the same UUID multiple times.
    The first submission returns 'success', subsequent submissions return 'already_ingested'.
    """
    sub_uuid = f"e2e-idemp-{uuid.uuid4()}"
    payload = {
        "submission_uuid": sub_uuid,
        "subject_id": "04_Advanced_Software_Eng",
        "topic": "Lecture 01: Foundations, Patriot Failure, Brooks & Ethics",
        "summary": {
            "total": 5,
            "correct": 5,
            "wrong": 0,
            "percentage": 100.0,
            "avg_dwell_time_seconds": 10.0
        },
        "questions": [
            {
                "id": "q0",
                "is_correct": True,
                "is_lucky_guess": False,
                "dwell_time_seconds": 10.0
            }
        ]
    }

    # First submission
    res1 = client.post("/api/quiz/submit", json=payload)
    assert res1.status_code == 200
    assert res1.get_json().get("status") == "success"

    # Second submission (in-memory deduplication)
    res2 = client.post("/api/quiz/submit", json=payload)
    assert res2.status_code == 200
    assert res2.get_json().get("status") == "already_ingested"

    # Clear in-memory set to verify journal-file based deduplication
    if sub_uuid in SEEN_UUIDS:
        SEEN_UUIDS.remove(sub_uuid)

    res3 = client.post("/api/quiz/submit", json=payload)
    assert res3.status_code == 200
    assert res3.get_json().get("status") == "already_ingested"


def test_e2e_vault_update_verification(client, isolated_hub):
    """
    Test 4: Verify quiz submissions record a journal-only 'Saved' marker
    (sessions/YYYY-MM-DD.md) without touching PROGRESS_ANALYTICS.md or
    LEARNER_MODEL.md — analysis is the agent's job, not the WebUI's.
    """
    sub_uuid = f"e2e-vault-{uuid.uuid4()}"
    payload = {
        "submission_uuid": sub_uuid,
        "subject_id": "04_Advanced_Software_Eng",
        "topic": "Lecture 01: Foundations, Patriot Failure, Brooks & Ethics",
        "summary": {
            "total": 5,
            "correct": 4,
            "wrong": 1,
            "percentage": 80.0,
            "avg_dwell_time_seconds": 16.2
        },
        "questions": [
            {
                "id": "Patriot_Drift_Q0",
                "is_correct": True,
                "is_lucky_guess": True,
                "dwell_time_seconds": 9.0
            },
            {
                "id": "Brooks_Complexity_Q1",
                "is_correct": False,
                "is_lucky_guess": False,
                "dwell_time_seconds": 25.0,
                "reflection": {
                    "reason": "Calculation Slip",
                    "note": "Mistook accidental tooling for essential complexity"
                }
            },
            {
                "id": "Brooks_Law_Q2",
                "is_correct": True,
                "is_lucky_guess": False,
                "dwell_time_seconds": 14.0
            },
            {
                "id": "Dependability_Q3",
                "is_correct": True,
                "is_lucky_guess": False,
                "dwell_time_seconds": 15.0
            },
            {
                "id": "Ethics_Q4",
                "is_correct": True,
                "is_lucky_guess": False,
                "dwell_time_seconds": 18.0
            }
        ]
    }

    res = client.post("/api/quiz/submit", json=payload)
    assert res.status_code == 200
    assert res.get_json().get("status") == "success"

    # Verify the journal-only "Saved" marker in today's session file
    today_str = datetime.now().strftime("%Y-%m-%d")
    session_file = isolated_hub / "sessions" / f"{today_str}.md"
    assert session_file.exists()
    session_content = session_file.read_text(encoding="utf-8")
    assert "**[Quiz WebUI]** Saved `04_Advanced_Software_Eng`" in session_content
    assert "Lecture 01: Foundations, Patriot Failure, Brooks & Ethics" in session_content
    assert "80%, 4/5" in session_content
    assert f"uuid: `{sub_uuid}`" in session_content
    assert 'Wrong: Brooks_Complexity_Q1 [Calculation Slip] "Mistook accidental tooling for essential complexity"' in session_content
    assert "Lucky: Patriot_Drift_Q0" in session_content
    assert "Avg dwell: 16.2s" in session_content

    # Analytics/learner files must remain untouched by the WebUI pipeline
    for fname in ["PROGRESS_ANALYTICS.md", "LEARNER_MODEL.md"]:
        f = isolated_hub / fname
        if f.exists():
            assert sub_uuid not in f.read_text(encoding="utf-8")


def test_e2e_full_lifecycle_journey(client, isolated_hub):
    """
    Test 5: Full lifecycle user journey:
    1. Fetch real quiz from server
    2. Answer questions (some correct, 1 lucky, 1 wrong with reflection)
    3. Submit telemetry and verify success
    4. Confirm immediate re-submission returns 'already_ingested'
    5. Verify state consistency in all vault markdown files
    """
    # Step 1: Fetch real quiz
    fetch_res = client.get("/api/quiz/04_Advanced_Software_Eng/Quiz_01_Software_Crisis")
    assert fetch_res.status_code == 200
    quiz_data = fetch_res.get_json()
    questions = quiz_data["questions"]
    assert len(questions) == 5

    # Step 2: Build simulated telemetry
    sub_uuid = f"e2e-lifecycle-{uuid.uuid4()}"
    simulated_questions = [
        {
            "id": "q0",
            "is_correct": True,
            "is_lucky_guess": True,
            "dwell_time_seconds": 7.5
        },
        {
            "id": "q1",
            "is_correct": False,
            "is_lucky_guess": False,
            "dwell_time_seconds": 30.0,
            "reflection": {
                "reason": "Calculation Slip",
                "note": "Re-read question too fast"
            }
        },
        {
            "id": "q2",
            "is_correct": True,
            "is_lucky_guess": False,
            "dwell_time_seconds": 12.0
        },
        {
            "id": "q3",
            "is_correct": True,
            "is_lucky_guess": False,
            "dwell_time_seconds": 10.0
        },
        {
            "id": "q4",
            "is_correct": True,
            "is_lucky_guess": False,
            "dwell_time_seconds": 15.0
        }
    ]

    payload = {
        "submission_uuid": sub_uuid,
        "subject_id": quiz_data["subject"],
        "topic": quiz_data["topic"],
        "summary": {
            "total": 5,
            "correct": 4,
            "wrong": 1,
            "percentage": 80.0,
            "avg_dwell_time_seconds": 14.9
        },
        "questions": simulated_questions
    }

    # Step 3: Submit telemetry
    submit_res = client.post("/api/quiz/submit", json=payload)
    assert submit_res.status_code == 200
    assert submit_res.get_json().get("status") == "success"

    # Step 4: Re-submit same payload -> already ingested
    resub_res = client.post("/api/quiz/submit", json=payload)
    assert resub_res.status_code == 200
    assert resub_res.get_json().get("status") == "already_ingested"

    # Step 5: Verify journal-only "Saved" marker (agent-facing log)
    today_str = datetime.now().strftime("%Y-%m-%d")
    session_text = (isolated_hub / "sessions" / f"{today_str}.md").read_text(encoding="utf-8")
    assert sub_uuid in session_text
    assert f"**[Quiz WebUI]** Saved `{quiz_data['subject']}`" in session_text
    assert "80%, 4/5" in session_text
    assert 'Wrong: q1 [Calculation Slip] "Re-read question too fast"' in session_text
    assert "Lucky: q0" in session_text

    # Analytics/learner files must remain untouched by the WebUI pipeline
    for fname in ["PROGRESS_ANALYTICS.md", "LEARNER_MODEL.md"]:
        f = isolated_hub / fname
        if f.exists():
            assert sub_uuid not in f.read_text(encoding="utf-8")


def test_e2e_bundle_offline_sync_lifecycle(client, isolated_hub):
    """
    E2E Test: 1-click bundle download, offline submission queuing,
    and server queue flushing upon reconnection.
    """
    # 1. Fetch entire semester bundle in 1 HTTP call
    res_bundle = client.get("/api/quiz/bundle?semester=1")
    assert res_bundle.status_code == 200
    bundle = res_bundle.get_json()
    assert bundle["bundle_version"] == 2
    assert bundle["total_quizzes"] == 6

    # 2. Pick a quiz from the bundle (e.g. 05_Soft_Computing)
    target_quiz = next(q for q in bundle["quizzes"] if q["subject_id"] == "05_Soft_Computing" and q["quiz_id"] == "Quiz_01_Soft_Computing_Foundations")
    assert target_quiz["schema_version"] == 2
    assert len(target_quiz["questions"]) == 5

    # 3. Simulate offline attempt: student takes quiz completely offline
    sub_uuid = f"offline_e2e_{uuid.uuid4().hex[:8]}"
    simulated_questions = []
    for idx, q in enumerate(target_quiz["questions"]):
        simulated_questions.append({
            "id": q["id"],
            "selected": q["answer"],
            "correct": q["answer"],
            "concept_id": q["concept_id"],
            "bloom_level": q["bloom_level"],
            "is_correct": True,
            "is_lucky_guess": False,
            "reflection": None,
            "dwell_time_seconds": 12.5,
            "answered_at": datetime.now().isoformat()
        })

    offline_payload = {
        "submission_uuid": sub_uuid,
        "quiz_id": target_quiz["quiz_id"],
        "instructor": target_quiz["instructor_ar"],
        "subject_id": target_quiz["subject_id"],
        "topic": target_quiz["topic"],
        "finished_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "session_duration_seconds": 65,
        "summary": {
            "total": 5,
            "correct": 5,
            "wrong": 0,
            "percentage": 100.0,
            "avg_dwell_time_seconds": 12.5
        },
        "questions": simulated_questions
    }

    # 4. Connection restored: auto-flush trigger POSTs to /api/quiz/submit
    flush_res = client.post("/api/quiz/submit", json=offline_payload)
    assert flush_res.status_code == 200
    assert flush_res.get_json()["status"] == "success"

    # 5. Verify ingestion in session journal
    today_str = datetime.now().strftime("%Y-%m-%d")
    session_file = isolated_hub / "sessions" / f"{today_str}.md"
    assert session_file.exists()
    content = session_file.read_text(encoding="utf-8")
    assert sub_uuid in content
    assert "100%, 5/5" in content
    assert f"Saved `{target_quiz['subject_id']}`" in content
