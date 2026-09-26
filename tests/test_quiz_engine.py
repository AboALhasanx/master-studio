import pytest
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from datetime import datetime
import sys

# Ensure 90_Shared_Toolbox/tools is in path
toolbox_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox" / "tools"
if str(toolbox_path) not in sys.path:
    sys.path.insert(0, str(toolbox_path))

from quiz_engine import process_quiz_telemetry, calculate_bkt_update, SEEN_UUIDS


def test_bkt_lucky_guess_prevents_mastery():
    # Normal correct answer should increase mastery
    prior = 0.5
    updated_normal = calculate_bkt_update(prior, is_correct=True, is_lucky_guess=False, reflection_reason=None)
    assert updated_normal > prior

    # Lucky guess should not increase mastery
    updated_lucky = calculate_bkt_update(prior, is_correct=True, is_lucky_guess=True, reflection_reason=None)
    assert updated_lucky <= prior + 0.01


def test_bkt_slip_preserves_prior_and_concept_gap_drops():
    prior = 0.8
    # Calculation slip preserves high prior
    updated_slip = calculate_bkt_update(prior, is_correct=False, is_lucky_guess=False, reflection_reason="Calculation Slip")
    assert updated_slip >= 0.75

    # Misread question preserves high prior
    updated_misread = calculate_bkt_update(prior, is_correct=False, is_lucky_guess=False, reflection_reason="Misread Question")
    assert updated_misread >= 0.75

    # Standard wrong (Concept Gap or unspecified) drops significantly
    updated_wrong = calculate_bkt_update(prior, is_correct=False, is_lucky_guess=False, reflection_reason="Concept Gap")
    assert updated_wrong < 0.5


def test_bkt_clamping():
    # Extreme low
    low = calculate_bkt_update(0.0, is_correct=False, is_lucky_guess=False)
    assert 0.01 <= low <= 0.99

    # Extreme high
    high = calculate_bkt_update(1.0, is_correct=True, is_lucky_guess=False)
    assert 0.01 <= high <= 0.99


def test_process_quiz_telemetry_idempotency():
    with TemporaryDirectory() as tmpdir:
        hub = Path(tmpdir)
        sessions_dir = hub / "sessions"
        sessions_dir.mkdir()

        payload = {
            "submission_uuid": "test-uuid-1234",
            "subject_id": "01_Cyber_Security",
            "quiz_id": "Quiz_01_Cyber_Security",
            "topic": "Week 01 Scenario Drills",
            "timestamp": "2026-09-19T23:00:00Z",
            "summary": {
                "total": 5,
                "correct": 4,
                "wrong": 1,
                "skipped": 0,
                "percentage": 80.0,
                "total_time_seconds": 90,
                "avg_dwell_time_seconds": 18.0,
                "attempt_number": 1,
            },
            "questions": [
                {
                    "id": "q1",
                    "selected": "B",
                    "correct": "B",
                    "is_correct": True,
                    "dwell_time_seconds": 12,
                    "reflection": None,
                    "is_lucky_guess": False,
                },
                {
                    "id": "q2",
                    "selected": "C",
                    "correct": "A",
                    "is_correct": False,
                    "dwell_time_seconds": 25,
                    "reflection": {"reason": "Calculation Slip", "note": "Arithmetic error"},
                    "is_lucky_guess": False,
                },
                {
                    "id": "q3",
                    "selected": "D",
                    "correct": "D",
                    "is_correct": True,
                    "dwell_time_seconds": 8,
                    "reflection": None,
                    "is_lucky_guess": True,
                },
            ],
        }

        # First ingestion: writes a simple "Saved" marker to today's journal
        res1 = process_quiz_telemetry(payload, hub)
        assert res1["status"] == "success"
        assert res1["percentage"] == 80.0

        today_str = datetime.now().strftime("%Y-%m-%d")
        journal_text = (sessions_dir / f"{today_str}.md").read_text(encoding="utf-8")
        assert "**[Quiz WebUI]** Saved `01_Cyber_Security`" in journal_text
        assert "Week 01 Scenario Drills" in journal_text
        assert "80%, 4/5" in journal_text
        assert "`test-uuid-1234`" in journal_text
        assert 'Wrong: q2 [Calculation Slip] "Arithmetic error"' in journal_text
        assert "Lucky: q3" in journal_text
        assert "Avg dwell: 18.0s" in journal_text

        # No analytics/learner writes should happen
        assert not (hub / "PROGRESS_ANALYTICS.md").exists()
        assert not (hub / "LEARNER_MODEL.md").exists()

        # Second ingestion with same UUID (in-memory idempotency check)
        res2 = process_quiz_telemetry(payload, hub)
        assert res2["status"] == "already_ingested"

        # Verify journal did not double-log
        journal_text_2 = (sessions_dir / f"{today_str}.md").read_text(encoding="utf-8")
        assert journal_text_2.count("test-uuid-1234") == 1


def test_process_quiz_telemetry_journal_idempotency():
    with TemporaryDirectory() as tmpdir:
        hub = Path(tmpdir)
        sessions_dir = hub / "sessions"
        sessions_dir.mkdir()

        # Simulate cold restart: clear SEEN_UUIDS
        SEEN_UUIDS.clear()

        # Create today's session journal containing the UUID
        today_str = datetime.now().strftime("%Y-%m-%d")
        today_session = sessions_dir / f"{today_str}.md"
        today_session.write_text(
            "- **[Quiz WebUI]** Saved `01_Cyber_Security` - Week 01 (80%, 4/5) | uuid: `cold-uuid-9999`\n",
            encoding="utf-8",
        )

        payload = {
            "submission_uuid": "cold-uuid-9999",
            "subject_id": "01_Cyber_Security",
            "quiz_id": "Quiz_01_Cyber_Security",
            "topic": "Week 01 Scenario Drills",
            "summary": {"percentage": 80.0, "correct": 4, "total": 5},
            "questions": [],
        }

        res = process_quiz_telemetry(payload, hub)
        assert res["status"] == "already_ingested"
        assert "cold-uuid-9999" in SEEN_UUIDS


def test_process_quiz_telemetry_missing_uuid():
    with TemporaryDirectory() as tmpdir:
        hub = Path(tmpdir)
        res = process_quiz_telemetry({}, hub)
        assert res["status"] == "error"
        assert "Missing submission_uuid" in res["message"]


def test_process_quiz_telemetry_invalid_payload():
    with TemporaryDirectory() as tmpdir:
        hub = Path(tmpdir)
        res = process_quiz_telemetry("invalid_payload", hub)
        assert res["status"] == "error"
        assert "Payload must be a dictionary" in res["message"]


def test_process_quiz_telemetry_enriched_journal_format():
    """Agent-facing journal line must carry quiz_id, wrong ids with
    concepts + reflections, lucky ids, Bloom gaps, and session metrics."""
    with TemporaryDirectory() as tmpdir:
        hub = Path(tmpdir)
        sessions_dir = hub / "sessions"
        sessions_dir.mkdir()

        payload = {
            "submission_uuid": "enriched-uuid-777",
            "subject_id": "04_Advanced_Software_Eng",
            "quiz_id": "Quiz_01_Software_Crisis",
            "topic": "Lecture 01: Foundations",
            "finished_at": "2026-09-19 22:40",
            "session_duration_seconds": 82,
            "summary": {
                "total": 5,
                "correct": 3,
                "wrong": 2,
                "percentage": 60.0,
                "avg_dwell_time_seconds": 14.5,
            },
            "questions": [
                {
                    "id": "q1",
                    "concept_id": "patriot_clock_drift",
                    "is_correct": True,
                    "is_lucky_guess": False,
                    "dwell_time_seconds": 8.0,
                    "bloom_level": "Apply",
                },
                {
                    "id": "q2",
                    "concept_id": "brooks_law",
                    "is_correct": False,
                    "is_lucky_guess": False,
                    "dwell_time_seconds": 25.0,
                    "bloom_level": "Understand",
                    "reflection": {"reason": "Concept Gap", "note": "Forgot O(N^2) channels"},
                },
                {
                    "id": "q3",
                    "concept_id": "se_ethics_public",
                    "is_correct": True,
                    "is_lucky_guess": True,
                    "dwell_time_seconds": 6.0,
                    "bloom_level": "Evaluate",
                },
            ],
        }

        res = process_quiz_telemetry(payload, hub)
        assert res["status"] == "success"

        today_str = datetime.now().strftime("%Y-%m-%d")
        text = (sessions_dir / f"{today_str}.md").read_text(encoding="utf-8")
        assert "**[Quiz WebUI]** Saved `04_Advanced_Software_Eng`" in text
        assert "60%, 3/5" in text
        assert "quiz: `Quiz_01_Software_Crisis`" in text
        assert "uuid: `enriched-uuid-777`" in text
        assert 'Wrong: q2(brooks_law) [Concept Gap] "Forgot O(N^2) channels"' in text
        assert "Lucky: q3" in text
        assert "Bloom gaps: Understand" in text
        assert "Avg dwell: 14.5s" in text
        assert "Session: 82s" in text
        assert "Finished: 2026-09-19 22:40" in text


def test_process_quiz_telemetry_perfect_score_marker():
    with TemporaryDirectory() as tmpdir:
        hub = Path(tmpdir)
        (hub / "sessions").mkdir()

        payload = {
            "submission_uuid": "perfect-uuid-100",
            "subject_id": "02_English_Language",
            "topic": "Unit 01 Grammar",
            "summary": {"percentage": 100.0, "correct": 5, "total": 5},
            "questions": [],
        }

        res = process_quiz_telemetry(payload, hub)
        assert res["status"] == "success"

        today_str = datetime.now().strftime("%Y-%m-%d")
        text = (hub / "sessions" / f"{today_str}.md").read_text(encoding="utf-8")
        assert "Perfect score" in text

def test_process_quiz_telemetry_structured_history():
    from quiz_engine import get_quiz_history
    with TemporaryDirectory() as tmpdir:
        hub = Path(tmpdir)
        (hub / "sessions").mkdir()

        payload = {
            "submission_uuid": "struct-uuid-1",
            "subject_id": "04_Advanced_Software_Eng",
            "quiz_id": "Quiz_01_Software_Crisis",
            "topic": "Software Crisis",
            "summary": {"percentage": 80.0, "correct": 4, "total": 5, "avg_dwell_time_seconds": 15.0},
            "questions": [
                {"id": "q1", "is_correct": True, "concept_id": "brooks_law"}
            ],
        }

        res = process_quiz_telemetry(payload, hub)
        assert res["status"] == "success"

        history_file = hub / "quiz_history.json"
        assert history_file.is_file()

        data = get_quiz_history(hub)
        assert len(data["history"]) == 1
        assert data["history"][0]["submission_uuid"] == "struct-uuid-1"
        assert "Quiz_01_Software_Crisis" in data["summary"]
        assert data["summary"]["Quiz_01_Software_Crisis"]["best_percentage"] == 80.0


def test_corrupt_history_file_refuses_overwrite():
    """P1: a corrupt quiz_history.json must surface as an error, never be clobbered."""
    from quiz_engine import record_structured_history
    with TemporaryDirectory() as tmpdir:
        hub = Path(tmpdir)
        corrupted = "{ this is not valid json"
        (hub / "quiz_history.json").write_text(corrupted, encoding="utf-8")

        payload = {"submission_uuid": "corrupt-guard-1", "summary": {"percentage": 50.0}}
        with pytest.raises(RuntimeError):
            record_structured_history(payload, hub, [], [], [])

        # The corrupt file must survive byte-for-byte (recoverable by the user)
        assert (hub / "quiz_history.json").read_text(encoding="utf-8") == corrupted
        # No temp file left behind
        assert not list(hub.glob("*.tmp"))


def test_failed_persistence_allows_clean_retry():
    """P1: a failed write must NOT poison SEEN_UUIDS, so the retry succeeds."""
    with TemporaryDirectory() as tmpdir:
        hub = Path(tmpdir)
        (hub / "sessions").mkdir()
        (hub / "quiz_history.json").write_text("{ corrupt", encoding="utf-8")

        payload = {
            "submission_uuid": "retry-after-fail-1",
            "subject_id": "01_Cyber_Security",
            "quiz_id": "Quiz_01_Cyber_Security",
            "topic": "Retry Drill",
            "summary": {"percentage": 75.0, "correct": 3, "total": 4, "avg_dwell_time_seconds": 10.0},
            "questions": [{"id": "q1", "is_correct": True}],
        }

        with pytest.raises(RuntimeError):
            process_quiz_telemetry(payload, hub)

        # Operator repairs the file -> same submission must now ingest cleanly
        (hub / "quiz_history.json").write_text("[]", encoding="utf-8")
        res = process_quiz_telemetry(payload, hub)
        assert res["status"] == "success"

        from quiz_engine import get_quiz_history
        data = get_quiz_history(hub)
        assert len(data["history"]) == 1


def test_concurrent_submissions_all_persist():
    """P1: concurrent submissions must never lose entries (thread lock around RMW)."""
    from concurrent.futures import ThreadPoolExecutor
    with TemporaryDirectory() as tmpdir:
        hub = Path(tmpdir)
        (hub / "sessions").mkdir()

        def make_payload(i):
            return {
                "submission_uuid": f"conc-uuid-{i}-{datetime.now().timestamp()}",
                "subject_id": "01_Cyber_Security",
                "quiz_id": f"Quiz_Conc_{i}",
                "topic": f"Concurrency Drill {i}",
                "summary": {"percentage": 60.0, "correct": 3, "total": 5, "avg_dwell_time_seconds": 9.0},
                "questions": [{"id": "q1", "is_correct": True}],
            }

        payloads = [make_payload(i) for i in range(6)]
        with ThreadPoolExecutor(max_workers=6) as pool:
            results = list(pool.map(lambda p: process_quiz_telemetry(p, hub), payloads))

        assert all(r["status"] == "success" for r in results)

        data = json.loads((hub / "quiz_history.json").read_text(encoding="utf-8"))
        assert len(data) == 6
