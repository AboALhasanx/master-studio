# Task 2 Brief: Backend REST Endpoints & LAN IP Helper

**Files:**
- Modify: `91_Dashboard/app.py`
- Test: `tests/test_dashboard_quiz_api.py`

**Interfaces:**
- Consumes: `process_quiz_telemetry` from `90_Shared_Toolbox/tools/quiz_engine.py`
- Produces:
  - `get_lan_ip() -> str`: Detects host Wi-Fi LAN IP (falls back to `127.0.0.1`).
  - `GET /quiz`: Hub landing page (renders `quiz.html` with `direct_mode=False`, `lan_ip`).
  - `GET /quiz/<subject_id>/<quiz_id>`: Direct quiz view (renders `quiz.html` with `direct_mode=True`, `subject_id`, `quiz_id`, `lan_ip`).
  - `GET /api/quiz/<subject_id>/<quiz_id>`: Returns quiz JSON from `01_Semester_1/<subject_id>/07_Quizzes_&_Anki/<quiz_id>.json`. Returns 404 if not found.
  - `POST /api/quiz/submit`: Accepts JSON telemetry, calls `process_quiz_telemetry(payload, HUB)`, returns result JSON. Returns 400 on invalid payload.
  - `GET /api/quiz/bookmarks`: Returns JSON list of bookmarked question IDs from `00_STUDIO_HUB/quiz_bookmarks.json`.
  - `POST /api/quiz/bookmarks`: Saves JSON list of bookmarked question IDs to `00_STUDIO_HUB/quiz_bookmarks.json`.
  - Ensure Flask runs on `0.0.0.0` with port `5000` when `__main__` is executed.

**TDD Workflow:**
1. Write `tests/test_dashboard_quiz_api.py` with unit tests for `/quiz`, `/api/quiz/...`, and `/api/quiz/submit`.
2. Run `pytest tests/test_dashboard_quiz_api.py` (verify failure).
3. Extend `91_Dashboard/app.py`.
4. Run `pytest tests/test_dashboard_quiz_api.py` (verify pass).
5. Write execution report to `.superpowers/sdd/2026-09-19-interactive-web-quiz-system/task-2-report.md`.
