# Task 1 Brief: Cognitive Ingestion & Vault Synchronization Engine

**Files:**
- Create: `90_Shared_Toolbox/tools/quiz_engine.py`
- Test: `tests/test_quiz_engine.py`

**Interfaces:**
- Produces:
  - `calculate_bkt_update(prior_knowledge: float, is_correct: bool, is_lucky_guess: bool, reflection_reason: str = None) -> float`: Calculates posterior concept mastery using BKT with slip/guess calibration.
  - `process_quiz_telemetry(payload: dict, hub_path: Path) -> dict`: Ingests telemetry, updates `PROGRESS_ANALYTICS.md`, `LEARNER_MODEL.md`, and `sessions/`, returning execution summary.

**Requirements & Logic:**
1. `calculate_bkt_update`:
   - If `is_correct` is True:
     - If `is_lucky_guess` is True: $P(G) = 1.0$, $P(S) = 0.1$. The update must NOT award false mastery credit ($P(L_{next}) \le P(L_{prior}) + 0.01$).
     - If normal correct: $P(G) = 0.25$, $P(S) = 0.1$. Mastery increases.
   - If `is_correct` is False:
     - If `reflection_reason` in `["Calculation Slip", "Misread Question"]`: $P(S) = 0.9$, $P(G) = 0.25$. Preserves high prior.
     - Otherwise: $P(S) = 0.1$, $P(G) = 0.25$. Standard failure update.
   - Clamp mastery between 0.01 and 0.99, rounded to 3 decimal places.
2. `process_quiz_telemetry`:
   - Enforce idempotency: verify `submission_uuid` against in-memory `SEEN_UUIDS` set and today's session journal file (`hub_path / "sessions" / "YYYY-MM-DD.md"`). If present, return `{"status": "already_ingested"}` immediately without duplicate file writes.
   - `PROGRESS_ANALYTICS.md`: Find table header, generate next `#XXX` ID, append row:
     `| #XXX | YYYY-MM-DD HH:MM | <subject> | <topic> | <correct>/<total> (<pct>%) | <PASS/FAIL> | <status> |\n`
   - `LEARNER_MODEL.md`:
     - Wrong answers: append to `## 4. Active Review Queue` with reflection reason and note.
     - Lucky guesses: append to `## 4. Active Review Queue` with `Fluke Confirmation`.
   - `sessions/YYYY-MM-DD.md`: Append structured journal entry with UUID, score, dwell time, and reflection counts.
   - Return `{"status": "success", "percentage": percentage}`.

**TDD Workflow:**
1. Create `tests/test_quiz_engine.py` with tests for BKT lucky guess behavior and telemetry idempotency.
2. Run `pytest tests/test_quiz_engine.py` (verify failure).
3. Implement `90_Shared_Toolbox/tools/quiz_engine.py`.
4. Run `pytest tests/test_quiz_engine.py` (verify pass).
5. Write execution report to `.superpowers/sdd/2026-09-19-interactive-web-quiz-system/task-1-report.md`.
