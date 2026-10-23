#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared builder for Ch04 (W04_Cryptography) quiz banks."""
import json, sys
from pathlib import Path

OUT = Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\01_Cyber_Security\07_Quizzes_&_Anki")

HEADER = {
    "schema_version": 2,
    "subject_id": "01_Cyber_Security",
    "subject_title": "الأمن السيبراني",
    "semester": 1,
    "semester_label": "كورس أول",
    "instructor_ar": "أ.م.د. هدى لفتة مجيد",
    "instructor": "Asst. Prof. Dr. Huda Lafta Majeed",
    "subject": "01_Cyber_Security",
}

LETTERS = "ABCD"


def rot(seq, shift):
    n = len(seq)
    return [seq[(j - shift) % n] for j in range(n)]


def build(quiz_id, topic_en, topic_ar, items, target):
    """items: list of (concept_id, bloom, q_en, q_ar, opts_en, opts_ar, exp_en, exp_ar)
    opts_* are written with the CORRECT option first. target = key pattern string."""
    assert len(items) == len(target), (quiz_id, len(items), len(target))
    assert len(set(c for c, *_ in items)) == len(items), "duplicate concept_id"
    # key-balance gate
    for L in LETTERS:
        assert target.count(L) <= 0.32 * len(target) + 1e-9, (quiz_id, L, target.count(L))

    questions = []
    for i, (cid, bloom, q_en, q_ar, oe, oa, ee, ea) in enumerate(items):
        assert len(oe) == 4 and len(oa) == 4, (cid, len(oe), len(oa))
        # length-tell gate, measured PRE-rotation where index 0 is the correct option
        clen = len(oe[0])
        dlen = sum(len(x) for x in oe[1:]) / 3.0
        ratio = clen / dlen if dlen else 0
        assert ratio <= 1.30, (quiz_id, cid, "len ratio %.2f" % ratio)
        # parenthetical-gloss gate: (x + k) is math and allowed; (Rivest-Shamir-Adleman) is not
        import re as _re
        for o in oe + oa:
            for m in _re.findall(r"\(([^)]*)\)", o):
                assert not _re.search(r"[a-z]{3,}", m), (cid, "parenthetical gloss", o)
        shift = LETTERS.index(target[i])
        en = rot(oe, shift)
        ar = rot(oa, shift)
        questions.append({
            "id": "q%d" % (i + 1),
            "concept_id": cid,
            "bloom_level": bloom,
            "question": q_en,
            "question_ar": q_ar,
            "options": en,
            "options_ar": ar,
            "options_en": en,
            "answer": target[i],
            "correct": shift,
            "explanation": ee,
            "explanation_ar": ea,
        })
    bank = dict(HEADER)
    bank["quiz_id"] = quiz_id
    bank["topic"] = topic_en
    bank["topic_ar"] = topic_ar
    bank["questions"] = questions
    path = OUT / (quiz_id + ".json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(bank, fh, ensure_ascii=False, indent=1)
    keys = "".join(target)
    print("wrote %-56s %2d q  keys %s" % (quiz_id, len(questions), keys))
    for L in LETTERS:
        print("    %s = %d (%.1f%%)" % (L, keys.count(L), 100.0 * keys.count(L) / len(keys)))
    return path


def blooms(items):
    from collections import Counter
    c = Counter(b for _, b, *_ in items)
    return dict(c)
