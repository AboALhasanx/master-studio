#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Canonical handout-reference pattern for MCSQuiz banks.

This lives in `90_Shared_Toolbox/tools/` (tracked in git) because `scratch/` is
gitignored since 23cfa7f. Anything a second agent needs after a fresh checkout
must not depend on a file that only exists on this machine.

The scratch scripts (`find_meta.py`, `preflight.py`) import from here when they
can and fall back to their local copy otherwise. The generated state tool always
uses this one.

Two bugs are deliberately guarded against, both of which happened before:
  * a stray leading `|` created an empty alternative matching EVERY string;
  * bare `قالت` matched inside `استقالته` (resignation).
"""
import re

META = re.compile(
    # direct: naming the source
    r"\bthe lecture|\blecture notes|\bthe notes\b|\bthe booklet\b|\bthe handout\b|"
    r"\bthe file\b|\baccording to\b|\bthe doctor\b|\bthe syllabus\b|\bthe slides?\b|"
    r"\bthe material\b|\bthe source\b(?![\s-]+(?:code|file|program|codebase|directory)\b)|\bthe text\b|\bthe book\b|\bthe course\b|"
    r"\bthe module\b(?!['’]s)|\bthe curriculum\b|\bthe reading\b|"
    # indirect: pointing at the document or at the person
    r"\bthis chapter|\bthe chapter|\bthis section|\bthis week|\bas we saw|"
    r"\bas covered|\bas discussed|\bas presented|\bher own\b|\bher rule\b|"
    r"\bshe said\b|\bshe states\b|\bher vocabulary\b|\bin her\b|"
    # Arabic
    r"(?<![\u0600-\u06FF])(?:المحاضرة|المحاضرات|الملزمة|الملزمه|الدكتورة|الشرائح|شرائح|"
    r"المصدر(?=\s+(?:يعرّف|يعرف|يقول|يذكر|يوضح|يعرض|يشير|يحدد))|وفق المصدر|حسب المصدر|"
    r"كما ورد في المصدر|كما يذكر المصدر|الجابتر|المذكور|قاعدتها|قالت إن|قالت ال|هذا الفصل|هذا القسم|هذا الأسبوع)"
    r"(?![\u0600-\u06FF])",
    re.I)


def has_reference(texts):
    """True if any of the supplied strings names the handout. None/empty ignored."""
    return any(t and META.search(str(t)) for t in texts)


def self_test():
    """A validator that has not been tested on valid input is not evidence."""
    good = [
        "Which techniques enforce confidentiality?",
        "How is risk defined?",
        "Threat A has probability 0.2 and impact 500.",
        "A result above 100 means there is investment.",
        "القسم A يستقبل الطلبات",
        "وحدة تقيس حجم الشيفرة المصدرية",
        "أسطر المصدر المقاسة ضمن حجم المنتج",
        "The source code's size is a software attribute.",
        "The source file, its comments, and its release date",
        "Late discovery automatically reduces the source-code size.",
        "Comments determine the module's measured complexity.",
        "موظف ينسخ قائمة العملاء قبل استقالته.",
        "If F(50) equals 0.85, what is the probability that loss exceeds 50?",
    ]
    bad = [
        "Which techniques does the lecture list under confidentiality?",
        "According to the notes, what is risk?",
        "This chapter names four domains.",
        "Her rule is that above 100 means investment.",
        "المحاضرة تقول إن العدد يزيد.",
        "المصدر يعرّف المقياس بأنه خاصية للمنتج.",
        "قالت إن التصنيف أربعة مجموعات.",
    ]
    false_pos = [t for t in good if META.search(t)]
    missed = [t for t in bad if not META.search(t)]
    assert not false_pos, "false positives: %r" % false_pos
    assert not missed, "missed references: %r" % missed
    return True


if __name__ == "__main__":
    self_test()
    print("META self-test: PASS")
