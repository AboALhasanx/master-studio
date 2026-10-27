#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify live Data Mining Chapter 1 against the vault after publication."""
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(r"C:\Users\gokoq\Master-Studio")
PORTAL = Path(r"C:\Users\gokoq\mcq-portal")
QUIZZES = ROOT / "01_Semester_1/03_Data_Mining/07_Quizzes_&_Anki"
EXPECTED = {
    "Quiz_Ch01_T01_What_Is_Data_Mining",
    "Quiz_Ch01_T02_Advantages_of_Data_Mining",
    "Quiz_Ch01_T03_Disadvantages_of_Data_Mining",
    "Quiz_Ch01_T04_Data_Mining_Applications",
    "Quiz_Ch01_T05_Implementation_Challenges",
}
RETIRED = {
    "Quiz_01_Introduction_to_Data_Mining",
    "Quiz_Ch01_ModelB_Introduction_to_Data_Mining",
}
BLOOM = {"Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"}

config = (PORTAL / "js/supabase-config.js").read_text(encoding="utf-8")
url = re.search(r"url:\s*'([^']+)'", config).group(1)
key = re.search(r"key:\s*'([^']+)'", config).group(1)

def rpc(name, body):
    req = urllib.request.Request(
        url + "/rest/v1/rpc/" + name,
        data=json.dumps(body).encode("utf-8"),
        headers={"apikey": key, "Authorization": "Bearer " + key,
                 "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.load(response)

manifest = rpc("content_manifest", {})
cards = [card for subject in manifest.get("subjects", [])
         if subject.get("subject_id") == "03_Data_Mining"
         for card in subject.get("chapters", []) if card.get("chapter_no") == 1]
live_ids = {card.get("quiz_id") for card in cards}
errors = []
if live_ids != EXPECTED:
    errors.append("chapter-1 IDs mismatch: live=%r expected=%r" % (sorted(live_ids), sorted(EXPECTED)))
if live_ids & RETIRED:
    errors.append("retired Model A/B IDs are still visible")

concepts = set()
total = 0
for quiz_id in sorted(EXPECTED & live_ids):
    bank_path = QUIZZES / (quiz_id + ".json")
    vault = json.loads(bank_path.read_text(encoding="utf-8"))
    live = rpc("content_bank", {"p_quiz_id": quiz_id})
    questions = live.get("questions") or live.get("payload", {}).get("questions") or []
    expected_questions = {q.get("id"): q for q in vault.get("questions", [])}
    by_id = {q.get("id"): q for q in questions}
    if len(by_id) != len(expected_questions):
        errors.append("%s count live=%d vault=%d" % (quiz_id, len(by_id), len(expected_questions)))
    for qid, expected in expected_questions.items():
        actual = by_id.get(qid)
        if actual is None:
            errors.append("%s missing %s" % (quiz_id, qid))
            continue
        total += 1
        concept = actual.get("concept_id")
        if not concept or concept in concepts:
            errors.append("%s/%s missing or duplicate concept_id" % (quiz_id, qid))
        concepts.add(concept)
        stem = actual.get("stem") or {}
        explanation = actual.get("explanation") or {}
        options = actual.get("options") or []
        correct = expected.get("correct")
        if stem.get("en") != expected.get("question") or stem.get("ar") != expected.get("question_ar"):
            errors.append("%s/%s stem differs" % (quiz_id, qid))
        if len(options) != 4:
            errors.append("%s/%s option count=%d" % (quiz_id, qid, len(options)))
        elif not (0 <= correct < 4) or actual.get("answer") != correct:
            errors.append("%s/%s answer index differs" % (quiz_id, qid))
        else:
            en = [o.get("en", "") for o in options]
            ar = [o.get("ar", "") for o in options]
            if en != expected.get("options_en") or ar != expected.get("options_ar"):
                errors.append("%s/%s options differ from vault" % (quiz_id, qid))
            if en[correct] != expected.get("options_en", [])[correct]:
                errors.append("%s/%s correct answer text differs" % (quiz_id, qid))
        if explanation.get("en") != expected.get("explanation") or explanation.get("ar") != expected.get("explanation_ar"):
            errors.append("%s/%s explanation differs" % (quiz_id, qid))
        if actual.get("bloom") != expected.get("bloom_level"):
            errors.append("%s/%s bloom differs" % (quiz_id, qid))
        if not stem.get("ar") or not stem.get("en") or not explanation.get("ar") or not explanation.get("en"):
            errors.append("%s/%s incomplete bilingual fields" % (quiz_id, qid))

print("live Ch1 banks:", len(cards), " expected:", len(EXPECTED))
print("live Ch1 questions:", total, " unique concepts:", len(concepts))
print("retired Model A/B IDs visible:", len(live_ids & RETIRED))
print("problems:", len(errors))
for error in errors[:20]:
    print("  -", error)
if errors:
    sys.exit(1)
print("ALL-LIVE-CHECKS-PASSED")
