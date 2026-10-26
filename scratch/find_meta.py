#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""List every question that talks ABOUT the handout instead of about the subject.

This is the reliable version. An earlier draft included loose words ("above",
"earlier", bare "القسم") that produced false positives on legitimate text such
as "a result above 100" and "القسم A" (department A). Those are gone: a scanner
that cries wolf gets ignored, and then the real hits get ignored with it.

Usage:
    python find_meta.py                       # every chapter
    python find_meta.py <file> [<file> ...]   # just those banks
"""
import glob
import json
import re
import sys

META = re.compile(
    # direct: naming the source
    r"\bthe lecture|\blecture notes|\bthe notes\b|\bthe booklet\b|\bthe handout\b|"
    r"\bthe file\b|\baccording to\b|\bthe doctor\b|\bthe syllabus\b|\bthe slides?\b|"
    r"\bthe material\b|\bthe source\b|\bthe text\b|\bthe book\b|\bthe course\b|"
    r"\bthe module\b|\bthe curriculum\b|\bthe reading\b|"
    # indirect: pointing at the document or at the person
    r"\bthis chapter|\bthe chapter|\bthis section|\bthis week|\bas we saw|"
    r"\bas covered|\bas discussed|\bas presented|\bher own\b|\bher rule\b|"
    r"\bshe said\b|\bshe states\b|\bher vocabulary\b|\bin her\b|"
    # Arabic
    r"المحاضرة|المحاضرات|الملزمة|الملزمه|الدكتورة|الشرائح|المصدر|الجابتر|المذكور|"
    r"قاعدتها|قالت إن|قالت ال|هذا الفصل|هذا القسم|هذا الأسبوع",
    re.I)

files = sys.argv[1:] or sorted(glob.glob(
    r"C:\Users\gokoq\Master-Studio\01_Semester_1\01_Cyber_Security\07_Quizzes_&_Anki\Quiz_Ch0*.json"))

per_chapter = {}
for f in files:
    d = json.loads(open(f, encoding="utf-8").read())
    ch = d["quiz_id"].split("_")[1]
    for q in d.get("questions", []):
        where = []
        for name, t in (("stem", q.get("question")), ("stem_ar", q.get("question_ar")),
                        ("expl", q.get("explanation")), ("expl_ar", q.get("explanation_ar"))):
            if t and META.search(t):
                where.append("%s:'%s'" % (name, META.search(t).group(0)))
        for o in (q.get("options") or []) + (q.get("options_ar") or []):
            if o and META.search(o):
                where.append("option:'%s'" % META.search(o).group(0))
        if where:
            per_chapter.setdefault(ch, []).append((q["id"], q["concept_id"], where))

total = 0
for ch in sorted(per_chapter):
    rows = per_chapter[ch]
    total += len(rows)
    print("%s  %d question(s) with a handout reference" % (ch, len(rows)))
    for qid, cid, where in rows:
        print("    %-4s %-30s %s" % (qid, cid[:30], " ".join(where)))
print("\ntotal questions with a reference: %d" % total)
