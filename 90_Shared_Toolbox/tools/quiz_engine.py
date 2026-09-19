#!/usr/bin/env python3
"""
Master Studio Quiz Tracking Engine
-----------------------------------
Receives quiz telemetry from the WebUI and records a simple "saved"
marker in the day's session journal (the single artifact surfaced to
agents). No PROGRESS_ANALYTICS.md / LEARNER_MODEL.md writes happen here —
analysis is the agent's job at session time, not the UI's.

Also exposes the BKT (Bayesian Knowledge Tracing) update used by agents
to calibrate mastery from correct/wrong/lucky-guess/reflection signals.
"""

from pathlib import Path
from datetime import datetime

SEEN_UUIDS = set()


def calculate_bkt_update(
    prior_knowledge: float,
    is_correct: bool,
    is_lucky_guess: bool,
    reflection_reason: str = None
) -> float:
    """
    Calculates posterior mastery using BKT with slip/guess calibration.

    Parameters:
        prior_knowledge (float): Prior mastery probability P(L_prior).
        is_correct (bool): True if student answered correctly.
        is_lucky_guess (bool): True if student flagged answer as lucky guess.
        reflection_reason (str): Error reflection reason for wrong answers.

    Returns:
        float: Posterior mastery probability clamped between 0.01 and 0.99.
    """
    p_l = max(0.01, min(0.99, float(prior_knowledge)))
    # If lucky guess, no transition learning credit is awarded
    p_t = 0.0 if is_lucky_guess else 0.1

    if is_correct:
        p_g = 1.0 if is_lucky_guess else 0.25
        p_s = 0.1
        # P(L|Correct)
        numerator = p_l * (1.0 - p_s)
        denominator = numerator + ((1.0 - p_l) * p_g)
        p_l_obs = numerator / denominator if denominator > 0 else p_l
    else:
        # Slip calibration: calculation/misread errors preserve high prior
        p_s = 0.9 if reflection_reason in ["Calculation Slip", "Misread Question"] else 0.1
        p_g = 0.25
        # P(L|Wrong)
        numerator = p_l * p_s
        denominator = numerator + ((1.0 - p_l) * (1.0 - p_g))
        p_l_obs = numerator / denominator if denominator > 0 else p_l

    # Posterior including transition
    p_next = p_l_obs + ((1.0 - p_l_obs) * p_t)
    return round(max(0.01, min(0.99, p_next)), 3)


def process_quiz_telemetry(payload: dict, hub_path: Path) -> dict:
    """
    Records quiz telemetry as a simple "saved" marker in the day's
    session journal (00_STUDIO_HUB/sessions/YYYY-MM-DD.md). Idempotent
    per submission UUID, both in-memory and against the journal on disk.

    Parameters:
        payload (dict): Structured quiz telemetry payload.
        hub_path (Path): Path to the Master Studio hub (or root vault path).

    Returns:
        dict: Ingestion result status and summary metrics.
    """
    if not isinstance(payload, dict):
        return {"status": "error", "message": "Payload must be a dictionary"}

    sub_uuid = payload.get("submission_uuid")
    if not sub_uuid:
        return {"status": "error", "message": "Missing submission_uuid"}

    # Idempotency check against memory
    if sub_uuid in SEEN_UUIDS:
        return {"status": "already_ingested"}

    today_str = datetime.now().strftime("%Y-%m-%d")
    sessions_dir = hub_path / "sessions"
    sessions_dir.mkdir(parents=True, exist_ok=True)
    today_session = sessions_dir / f"{today_str}.md"

    # Idempotency check against today's session journal on disk
    if today_session.exists():
        session_text = today_session.read_text(encoding="utf-8")
        if sub_uuid in session_text:
            SEEN_UUIDS.add(sub_uuid)
            return {"status": "already_ingested"}

    SEEN_UUIDS.add(sub_uuid)

    subject = payload.get("subject_id", "Unknown_Subject")
    topic = payload.get("topic", "Quiz")
    summary = payload.get("summary", {})
    percentage = float(summary.get("percentage", 0.0))
    correct_count = summary.get("correct", 0)
    total_count = summary.get("total", 0)
    score_str = f"{correct_count}/{total_count}"

    # Simple "saved" marker in the session journal (agent-facing log)
    journal_entry = (
        f"\n- **[Quiz WebUI]** Saved `{subject}` - {topic} ({percentage:.0f}%, {score_str}) | UUID: `{sub_uuid}`\n"
    )
    with open(today_session, "a", encoding="utf-8") as f:
        f.write(journal_entry)

    return {"status": "success", "percentage": percentage}
