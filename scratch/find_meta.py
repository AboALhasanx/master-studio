#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Broad sweep: any reference to the source, the course, the chapter or the book."""
import glob
import json
import re
import sys

META = re.compile(
    # English
    r"\bthe lecture|\blecture\b|\bthe notes\b|\bthe booklet\b|\bthe handout\b|\bthe file\b|"
    r"\baccording to\b|\bthe doctor\b|\bthe syllabus\b|\bthe slides?\b|\bthe material\b|"
    r"\bthe source\b|\bthe text\b|\bthe book\b|\bthe course\b|\bthis course\b|\bthe module\b|"
    r"\bthis chapter\b|\bthe chapter\b|\bthis section\b|\bthe section\b|\bthis week\b|\bthe week\b|"
    r"\bas we saw\b|\bas covered\b|\bas discussed\b|\bas presented\b|\bwe saw\b|\bwe covered\b|"
    r"\bthe reading\b|\bthe curriculum\b|\bthe subject notes\b|\bin these notes\b|"
    r"\bmentioned above\b|\bdescribed above\b|\bearlier\b|\babove\b"
    # Arabic
    r"|المحاضرة|المحاضرات|الملزمة|الملزمه|المادة\b|المصدر|الدكتورة|الشرائح|الكتاب|"
    r"هذا الفصل|الفصل\b|هذا الجابتر|الجابتر|هذا القسم|القسم\b|هذا الأسبوع|الأسبوع\b|"
    r"كما رأينا|كما ذُكر|المذكور|سابقاً|أعلاه",
    re.I)

files = sys.argv[1:] or sorted(glob.glob(
    r"C:\Users\gokoq\Master-Studio\01_Semester_1\01_Cyber_Security\07_Quizzes_&_Anki\Quiz_Ch0[12]_*.json"))

found = 0
for f in files:
    d = json.loads(open(f, encoding="utf-8").read())
    for q in d.get("questions", []):
        spots = []
        for name, t in (("stem", q.get("question")), ("stem_ar", q.get("question_ar")),
                        ("expl", q.get("explanation")), ("expl_ar", q.get("explanation_ar"))):
            if t and META.search(t):
                spots.append((name, META.search(t).group(0), t))
        for o in (q.get("options") or []) + (q.get("options_ar") or []):
            if META.search(o):
                spots.append(("option", META.search(o).group(0), o))
        if spots:
            found += 1
            print("%s %-4s %s" % (d["quiz_id"].split("_")[1], q["id"], q["concept_id"]))
            for name, hit, t in spots:
                print("    [%s] '%s' -> %s" % (name, hit, t[:120]))
print("questions with a reference:", found)
