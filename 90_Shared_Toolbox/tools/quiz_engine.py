#!/usr/bin/env python3
"""
Master Studio Cognitive Ingestion & Vault Synchronization Engine
-----------------------------------------------------------------
Processes quiz telemetry payloads with Bayesian Knowledge Tracing,
slip/guess calibration, and idempotent markdown updates.
"""

from pathlib import Path
from datetime import datetime, timedelta
import json
import re

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
    Ingests telemetry into PROGRESS_ANALYTICS.md, LEARNER_MODEL.md, and sessions/.

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
    avg_dwell = float(summary.get("avg_dwell_time_seconds", 0.0))
    questions = payload.get("questions", [])

    # 1. Update PROGRESS_ANALYTICS.md
    analytics_file = hub_path / "PROGRESS_ANALYTICS.md"
    if analytics_file.exists():
        text = analytics_file.read_text(encoding="utf-8")
        existing_ids = [int(m) for m in re.findall(r"^\|\s*#(\d+)\b", text, re.MULTILINE)]
        next_num = max(existing_ids) + 1 if existing_ids else 1
        new_id = f"#{next_num:03d}"
        now_ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        status = "🟢 Mastered" if percentage >= 80 else ("🟡 Borderline" if percentage >= 60 else "🔴 Review Needed")
        result = "PASS" if percentage >= 60 else "FAIL"

        row = f"| {new_id} | {now_ts} | `{subject}` | {topic} | {score_str} ({percentage:.0f}%) | {result} | {status} |\n"

        lines = text.splitlines(keepends=True)
        new_lines = []
        appended = False
        for line in lines:
            new_lines.append(line)
            # Match table separator row
            if line.strip().startswith("|:---:|:---:|:---|:---|:---:|") and not appended:
                new_lines.append(row)
                appended = True
        if not appended:
            new_lines.append(row)
        analytics_file.write_text("".join(new_lines), encoding="utf-8")

    # 2. Update LEARNER_MODEL.md
    learner_file = hub_path / "LEARNER_MODEL.md"
    if learner_file.exists():
        l_text = learner_file.read_text(encoding="utf-8")
        review_entries = []
        now_date = datetime.now().strftime("%Y-%m-%d")
        due_date = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")

        for q in questions:
            if not q.get("is_correct"):
                ref = q.get("reflection") or {}
                reason = ref.get("reason", "Concept Gap")
                note = ref.get("note", "").strip()
                desc = f"{topic}: Q_{q.get('id', '')} ({reason}{' - ' + note if note else ''})"
                review_entries.append(f"| `{subject}` | {desc} | {now_date} | Error Reflection | High | {due_date} |\n")
            elif q.get("is_lucky_guess"):
                desc = f"{topic}: Q_{q.get('id', '')} (Lucky Guess / Fluke)"
                review_entries.append(f"| `{subject}` | {desc} | {now_date} | Fluke Confirmation | Medium | {due_date} |\n")

        if review_entries:
            lines = l_text.splitlines(keepends=True)
            out_lines = []
            inserted = False
            for line in lines:
                out_lines.append(line)
                if line.strip().startswith("|:---|:---|:---|:---|:---:|:---|") and not inserted:
                    out_lines.extend(review_entries)
                    inserted = True
            if not inserted:
                out_lines.extend(review_entries)
            learner_file.write_text("".join(out_lines), encoding="utf-8")

    # 3. Append to today's session journal
    lucky_count = sum(1 for q in questions if q.get("is_lucky_guess"))
    wrong_count = summary.get("wrong", sum(1 for q in questions if not q.get("is_correct")))
    journal_entry = (
        f"\n- **[Quiz WebUI]** Completed `{subject}` - {topic} ({percentage:.0f}%, {score_str}).\n"
        f"  - Avg Dwell Time: {avg_dwell:.1f}s | UUID: `{sub_uuid}`\n"
        f"  - Recorded {wrong_count} error reflections and {lucky_count} lucky guesses.\n"
    )
    with open(today_session, "a", encoding="utf-8") as f:
        f.write(journal_entry)

    return {"status": "success", "percentage": percentage}
