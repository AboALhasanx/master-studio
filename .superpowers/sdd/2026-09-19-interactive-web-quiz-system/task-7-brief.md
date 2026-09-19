# Task 7 Brief: End-to-End System Verification

**Files:**
- Create: `tests/test_e2e_quiz_flow.py`

**Scope of E2E Test:**
1. Use Flask test client to fetch real quiz `04_Advanced_Software_Eng/Quiz_01_Software_Crisis`. Verify status 200 and questions.
2. Submit a full telemetry payload with:
   - Unique `submission_uuid`.
   - 1 correct answer flagged with `is_lucky_guess: True`.
   - 1 wrong answer with metacognitive reflection (`Calculation Slip` + note).
   - Summary metrics (dwell times, score, percentage).
3. Verify:
   - Submission endpoint returns 200 and `status: "success"`.
   - Resubmitting the same payload returns `status: "already_ingested"`.
   - Verify that `PROGRESS_ANALYTICS.md` was updated.
   - Verify that `LEARNER_MODEL.md` has the new review entries.
   - Verify that `sessions/YYYY-MM-DD.md` contains the session log.
4. Execute the full test suite across all tests:
   `python -m pytest tests/`
   and verify 100% pass rate.
5. Write execution report to `.superpowers/sdd/2026-09-19-interactive-web-quiz-system/task-7-report.md`.
