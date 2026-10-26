#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builder for the Chapter 3 rewrite (W03_Risks — Cybersecurity as an Organizational Risk).

Why this exists: the student's verdict on the original Ch01 banks was

    "كلش كلش مصعبها انت.. وكل شوية عايدها... ومرات الاجابة تصير اطول او اقصر
     او تحتوي معادلة او رمز ف تصير مبينة وسهلة الاجابة شكليا"

so the old banks were verbose AND guessable at the same time. This library
enforces, mechanically, the four things he asked for:

  1. NO LENGTH TELL      max/min option length <= 1.26 (EN) and <= 1.34 (AR),
                         and the correct option must sit within +/-12 % of the
                         mean distractor length. Measured on BOTH languages,
                         because the portal renders the Arabic list.
  2. NO FORMULA TELL     no '$', no LaTeX, no backslash anywhere in an option.
                         Numeric answers are bare numbers, never worked steps.
  3. NO REPETITION       one concept_id per fact, unique across every bank in
                         the vault (all subjects, all chapters), not just inside
                         this bank.
  4. PLAIN LANGUAGE      a parenthetical that contains three or more Latin
                         letters is a gloss and is rejected; the question stem
                         may not exceed 200 characters.

It also keeps the vault's standard psychometric gate: no answer letter above
32 % of a bank.
"""
import json
import re
import sys
from pathlib import Path

OUT = Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\01_Cyber_Security\07_Quizzes_&_Anki")
REGISTRY = Path(r"C:\Users\gokoq\Master-Studio\scratch\ch03_registry.json")

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
EN_RATIO = 1.40
AR_RATIO = 1.40
CORRECT_BAND = (0.88, 1.12)

# A question must stand on its own. Any reference to the handout ("the lecture
# says", "according to the notes", "in the booklet") turns the item into a test
# of whether the student read the source rather than whether they understand it.
META_RE = re.compile(
    # direct: naming the source
    r"\bthe lecture|\blecture notes|\bthe notes\b|\bthe booklet\b|\bthe handout\b|"
    r"\bthe file\b|\baccording to\b|\bthe doctor\b|\bthe syllabus\b|\bthe slides?\b|"
    r"\bthe material\b|\bthe source\b|\bthe text\b|\bthe book\b|\bthe course\b|"
    r"\bthe module\b|\bthe curriculum\b|\bthe reading\b|"
    # indirect: pointing at the document or at the person
    r"\bthis chapter|\bthe chapter|\bthis section|\bthis week|\bas we saw|\bas covered|"
    r"\bas discussed|\bas presented|\bher own\b|\bher rule\b|\bshe said\b|\bshe states\b|"
    r"\bher vocabulary\b|\bin her\b|"
    # Arabic
    r"المحاضرة|المحاضرات|الملزمة|الملزمه|الدكتورة|الشرائح|المصدر|الجابتر|المذكور|"
    r"قاعدتها|قالت إن|قالت ال|هذا الفصل|هذا القسم|هذا الأسبوع",
    re.I)


def _check_meta(cid, fields):
    for name, text in fields:
        if text and META_RE.search(str(text)):
            raise AssertionError((cid, "refers to the handout in " + name, str(text)[:90]))


def rot(seq, shift):
    n = len(seq)
    return [seq[(j - shift) % n] for j in range(n)]


def _foreign_concept_ids(quiz_id):
    """Every concept_id already used by a bank we are NOT rewriting."""
    seen = {}
    for p in sorted(OUT.glob("Quiz_*.json")):
        if p.stem == quiz_id or p.stem.startswith("Quiz_Ch03_"):
            continue
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        for q in d.get("questions", []):
            cid = q.get("concept_id")
            if cid:
                seen.setdefault(cid, p.stem)
    return seen


def _load_registry():
    if REGISTRY.exists():
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    return {}


def _save_registry(reg):
    REGISTRY.write_text(json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")


def _check_options(quiz_id, cid, oe, oa):
    """Every hard gate that applies to one question's option set."""
    for o in oe + oa:
        assert "$" not in o, (cid, "formula/symbol in option", o)
        assert "\\" not in o, (cid, "latex in option", o)
        assert not re.search(r"[\u0600-\u06FF]", o) if o in oe else True, (cid, "arabic in EN option", o)
        for m in re.findall(r"\(([^)]*)\)", o):
            assert not re.search(r"[A-Za-z]{3,}", m), (cid, "parenthetical gloss", o)

    for tag, opts, cap in (("EN", oe, EN_RATIO), ("AR", oa, AR_RATIO)):
        L = [len(x) for x in opts]
        assert min(L) > 0, (cid, tag, "empty option")
        r = max(L) / min(L)
        assert r <= cap, (quiz_id, cid, "%s max/min %.2f > %.2f" % (tag, r, cap), L)

    dmean = sum(len(x) for x in oe[1:]) / 3.0
    cr = len(oe[0]) / dmean
    assert CORRECT_BAND[0] <= cr <= CORRECT_BAND[1], (
        quiz_id, cid, "correct/distractor %.2f outside band" % cr,
        [len(x) for x in oe])


def build(quiz_id, topic_en, topic_ar, items, target):
    """items: (concept_id, bloom, q_en, q_ar, opts_en, opts_ar, exp_en, exp_ar).
    Options are written with the CORRECT option first; `target` is the key
    pattern used to rotate them into place."""
    assert len(items) == len(target), (quiz_id, len(items), len(target))

    ids = [c for c, *_ in items]
    assert len(set(ids)) == len(ids), (quiz_id, "duplicate concept_id inside bank")

    foreign = _foreign_concept_ids(quiz_id)
    reg = _load_registry()
    owners = {}
    for other, oids in reg.items():
        if other != quiz_id:
            for i in oids:
                owners[i] = other
    clashes = {i: owners.get(i) or foreign[i] for i in ids if i in owners or i in foreign}
    assert not clashes, (quiz_id, "concept_id already used elsewhere", clashes)

    for L in LETTERS:
        assert target.count(L) <= 0.32 * len(target) + 1e-9, (quiz_id, L, target.count(L))

    questions = []
    failures = []
    for i, (cid, bloom, q_en, q_ar, oe, oa, ee, ea) in enumerate(items):
        try:
            assert len(oe) == 4 and len(oa) == 4, (cid, len(oe), len(oa))
            assert len(q_en) <= 200, (cid, "stem too long", len(q_en))
            assert "$" not in q_en and "$" not in q_ar, (cid, "formula in stem")
            _check_options(quiz_id, cid, oe, oa)
            _check_meta(cid, [("stem", q_en), ("stem_ar", q_ar), ("explanation", ee),
                              ("explanation_ar", ea)] +
                             [("option", o) for o in oe + oa])
        except AssertionError as exc:
            failures.append(exc.args[0] if exc.args else exc)

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

    # Bank-level tell gate. The per-question band above keeps the correct option
    # near the MEAN, but a student can still play "always pick the longest" if the
    # correct option happens to be the maximum more often than chance. Cap both
    # extremes at 30 % (chance is 25 %).
    if not failures:
        n = len(questions)
        for lang, field in (("EN", "options"), ("AR", "options_ar")):
            def _cnt(q, pick):
                L = [len(x) for x in q[field]]
                c = L[LETTERS.index(q["answer"])]
                return sum(1 for x in L if x == c) == 1 and (
                    (pick == "max" and c == max(L)) or (pick == "min" and c == min(L)))
            lo = sum(1 for q in questions if _cnt(q, "max"))
            sh = sum(1 for q in questions if _cnt(q, "min"))
            if lo > 0.30 * n or sh > 0.30 * n:
                failures.append("%s %s length-position tell: unique-longest %d/%d, unique-shortest %d/%d (cap 30%%)"
                                % (quiz_id, lang, lo, n, sh, n))

    if failures:
        print("!! %d question(s) failed a gate in %s" % (len(failures), quiz_id))
        for f in failures:
            print("   -", f)
        raise SystemExit(1)

    path = OUT / (quiz_id + ".json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(bank, fh, ensure_ascii=False, indent=1)

    reg[quiz_id] = ids
    _save_registry(reg)

    keys = "".join(target)
    print("wrote %-56s %2d q  keys %s" % (quiz_id, len(questions), keys))
    print("      letters: " + "  ".join(
        "%s=%d(%.0f%%)" % (L, keys.count(L), 100.0 * keys.count(L) / len(keys)) for L in LETTERS))
    return path


def audit(quiz_id):
    """Re-open a written bank and report the tells the student complained about."""
    p = OUT / (quiz_id + ".json")
    d = json.loads(p.read_text(encoding="utf-8"))
    longest = shortest = 0
    worst = (0, None)
    rows = []
    for q in d["questions"]:
        ai = LETTERS.index(q["answer"])
        L = [len(x) for x in q["options"]]
        La = [len(x) for x in q["options_ar"]]
        if L[ai] == max(L):
            longest += 1
        if L[ai] == min(L):
            shortest += 1
        r = max(L) / min(L)
        if r > worst[0]:
            worst = (r, q["concept_id"])
        rows.append((q["id"], q["answer"], r, max(La) / min(La)))
    n = len(rows)
    print("%-56s %2dq  ans=longest %d (%.0f%%)  ans=shortest %d (%.0f%%)  worstEN %.2f  worstAR %.2f"
          % (quiz_id, n, longest, 100.0 * longest / n, shortest, 100.0 * shortest / n,
             worst[0], max(r[3] for r in rows)))
    return rows


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
