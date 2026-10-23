#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared builder for Ch05 (W05_Network_Security) quiz banks.

Adds a CROSS-BANK concept_id registry on top of the Ch04 library: the student
noted that the W05 source repeats itself in places, so the same concept must
never become two questions in two different banks. The registry is keyed by
quiz_id, so re-running one builder is fine; a clash with a *different* bank
fails loudly.
"""
import json
import re as _re
import sys
from pathlib import Path

OUT = Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\01_Cyber_Security\07_Quizzes_&_Anki")
REGISTRY = Path(r"C:\Users\gokoq\Master-Studio\scratch\ch05_registry.json")

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


def _load_registry():
    if REGISTRY.exists():
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    return {}


def _save_registry(reg):
    REGISTRY.write_text(json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")


def build(quiz_id, topic_en, topic_ar, items, target):
    """items: (concept_id, bloom, q_en, q_ar, opts_en, opts_ar, exp_en, exp_ar).
    opts_* are written with the CORRECT option first. target = key pattern."""
    assert len(items) == len(target), (quiz_id, len(items), len(target))

    ids = [c for c, *_ in items]
    assert len(set(ids)) == len(ids), (quiz_id, "duplicate concept_id inside bank")

    # cross-bank uniqueness
    reg = _load_registry()
    owners = {}
    for other, oids in reg.items():
        if other == quiz_id:
            continue
        for i in oids:
            owners[i] = other
    clashes = {i: owners[i] for i in ids if i in owners}
    assert not clashes, (quiz_id, "concept_id already used by another bank", clashes)

    # key-balance gate
    for L in LETTERS:
        assert target.count(L) <= 0.32 * len(target) + 1e-9, (quiz_id, L, target.count(L))

    questions = []
    for i, (cid, bloom, q_en, q_ar, oe, oa, ee, ea) in enumerate(items):
        assert len(oe) == 4 and len(oa) == 4, (cid, len(oe), len(oa))

        # length-tell gate, measured PRE-rotation (index 0 is the correct option)
        clen = len(oe[0])
        dlen = sum(len(x) for x in oe[1:]) / 3.0
        ratio = clen / dlen if dlen else 0
        assert ratio <= 1.30, (quiz_id, cid, "len ratio %.2f" % ratio)

        # parenthetical-gloss gate: (x + k) is math and allowed; (Rivest-Shamir-Adleman) is not
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

    reg[quiz_id] = ids
    _save_registry(reg)

    keys = "".join(target)
    print("wrote %-56s %2d q  keys %s" % (quiz_id, len(questions), keys))
    for L in LETTERS:
        print("    %s = %d (%.1f%%)" % (L, keys.count(L), 100.0 * keys.count(L) / len(keys)))
    return path


def blooms(items):
    from collections import Counter
    return dict(Counter(b for _, b, *_ in items))


def registry_report():
    reg = _load_registry()
    total = sum(len(v) for v in reg.values())
    print("banks registered: %d   total concept_ids: %d" % (len(reg), total))
    seen = {}
    for qid, ids in reg.items():
        for i in ids:
            seen.setdefault(i, []).append(qid)
    dupes = {k: v for k, v in seen.items() if len(v) > 1}
    print("cross-bank duplicates:", dupes if dupes else "none")
    return dupes
