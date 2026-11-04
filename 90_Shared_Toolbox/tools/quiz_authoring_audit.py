#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Authoring audit for quiz banks — the checks that keep biting us.

Every defect below was found by hand on real banks (Data Mining Ch01/Ch07,
Cyber Security risk equations, Soft Computing explanations) and cost hours to
repair. This tool turns them into one gate so a future bank cannot ship with
them.

HARD (always fail the run):
  H1  a purely numeric option                 (arithmetic in disguise)
  H2  a formula symbol in an option           ($ or backslash / LaTeX)
  H3  a handout reference                     ("the lecture", "according to", "المصدر")
  H4  an English explanation written in Arabic (portal shows it in English mode)
  H5  an exact duplicate stem inside a subject
  H6  answer letter disagrees with the correct index
  H7  options != options_en
  H8  empty explanation
  H9  options_ar not four non-empty strings   (non-English banks only)
  H10 empty question_ar                        (non-English banks only)

SOFT (warn; become HARD with --strict):
  S1  a stem that points at something it never states
      ("in the example", "those categories", "the marked cases")
  S2  explanation shorter than 35 characters
  S3  one answer letter above 32 % inside a bank
  S4  two stems with Jaccard similarity >= 0.80

Usage:
    python quiz_authoring_audit.py <dir-or-file> [...] [--strict] [--json]
Exit code 0 = clean, 1 = at least one failure.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from quiz_meta_pattern import META  # noqa: E402

NUMERIC_OPT = re.compile(r"^[\s\d.,%+\-/=~≈^()]+$")
FORMULA_CHARS = ("$", "\\")
ARABIC = re.compile(r"[\u0600-\u06FF]")
LETTERS = "ABCD"

# Stems that point outside themselves.
CONTEXT_PATTERNS = [
    r"\bin the example\b", r"\bthis example\b", r"\bthe example\b",
    r"\bthe listed\b", r"\blisted above\b", r"\blisted below\b",
    r"\bthe above\b", r"\bthe following (?:list|table|figure)\b",
    r"\bthe previous\b", r"\bthe same (?:equation|model|sets?|table)\b",
    r"\b(?:those|these) (?:categories|classes|challenges|metrics|perspectives|cases)\b",
    r"\bthis model\b", r"\bsuch a model\b", r"\bthe marked\b", r"\bmarked (?:cases?|perspectives?)\b",
    r"\baccording to\b", r"\bthe slide\b", r"\bthe lecture\b", r"\bthe booklet\b",
    r"\bthe source\b", r"\bthe handout\b",
]
CONTEXT_RE = re.compile("|".join(CONTEXT_PATTERNS), re.I)
# Legitimate MCQ phrasing that looks like a demonstrative but is self-contained.
CONTEXT_ALLOW = re.compile(r"\bwhich of (?:these|the following)\b", re.I)

TOKEN_RE = re.compile(r"[A-Za-z]{2,}|[\u0600-\u06FF]{2,}")


def tokens(text: str) -> set[str]:
    return {t.lower() for t in TOKEN_RE.findall(text or "")}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def iter_banks(paths):
    seen = set()
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            files = sorted(p.glob("Quiz_*.json"))
            if not files:
                files = sorted(p.glob("07_Quizzes_&_Anki/Quiz_*.json"))
            if not files:
                files = sorted(p.glob("*/07_Quizzes_&_Anki/Quiz_*.json"))
        else:
            files = [p]
        for f in files:
            f = f.resolve()
            if f in seen:
                continue
            seen.add(f)
            yield f


def audit(paths, strict=False):
    hard, soft = [], []
    stems = {}          # (subject, normalised stem) -> concept_id
    by_subject = defaultdict(list)
    bank_count = q_count = 0

    for f in iter_banks(paths):
        try:
            bank = json.loads(f.read_text(encoding="utf-8"))
        except Exception as exc:
            hard.append(("H0", f.name, "-", f"unreadable JSON: {exc}"))
            continue
        bank_count += 1
        subject = bank.get("subject_id") or f.parent.parent.name
        en_only = str(bank.get("lang") or "").lower() == "en"
        qs = bank.get("questions") or []
        if not qs:
            hard.append(("H0", f.name, "-", "bank has no questions"))
            continue

        letters = Counter()
        stem_list = []
        for q in qs:
            q_count += 1
            cid = q.get("concept_id") or "<no-id>"
            where = f"{f.name}/{q.get('id', '?')}"
            opts = [str(o) for o in (q.get("options") or [])]
            opts_en = [str(o) for o in (q.get("options_en") or [])]
            opts_ar = [str(o) for o in (q.get("options_ar") or [])]
            stem = str(q.get("question") or "")
            expl = str(q.get("explanation") or "")
            expl_ar = str(q.get("explanation_ar") or "")

            letters[q.get("answer", "?")] += 1

            # H1 numeric option
            bad_num = [o for o in opts if NUMERIC_OPT.match(o) and re.search(r"\d", o)]
            if bad_num:
                hard.append(("H1", where, cid, f"numeric option(s): {bad_num[:3]}"))

            # H2 formula symbols in options
            bad_form = [o for o in opts if any(c in o for c in FORMULA_CHARS)]
            if bad_form:
                hard.append(("H2", where, cid, f"formula in option: {bad_form[0][:40]!r}"))

            # H3 handout reference
            for field, text in (("question", stem), ("explanation", expl), ("explanation_ar", expl_ar)):
                m = META.search(text)
                if m:
                    hard.append(("H3", where, cid, f"{field} names the handout: {m.group(0)!r}"))

            # H4 English explanation in Arabic
            if len(ARABIC.findall(expl)) > 10:
                hard.append(("H4", where, cid, "English explanation contains Arabic text"))

            # H5 duplicate stem
            key = (subject, " ".join(stem.lower().split()))
            if key in stems:
                hard.append(("H5", where, cid, f"duplicate stem, also {stems[key]}"))
            else:
                stems[key] = cid

            # H6 answer vs correct
            ans, corr = q.get("answer"), q.get("correct")
            if isinstance(corr, int) and ans in LETTERS and LETTERS.index(ans) != corr:
                hard.append(("H6", where, cid, f"answer {ans} but correct={corr}"))

            # H7 options vs options_en
            if opts_en and opts != opts_en:
                hard.append(("H7", where, cid, "options and options_en differ"))

            # H8 empty explanation
            if not expl.strip():
                hard.append(("H8", where, cid, "empty explanation"))

            # H9 / H10 Arabic side
            if not en_only:
                if len(opts_ar) != 4 or any(not o.strip() for o in opts_ar):
                    hard.append(("H9", where, cid, "options_ar is not four non-empty strings"))
                if not str(q.get("question_ar") or "").strip():
                    hard.append(("H10", where, cid, "empty question_ar"))

            # S1 context-dependent stem
            if CONTEXT_RE.search(stem) and not CONTEXT_ALLOW.search(stem):
                soft.append(("S1", where, cid, f"stem points outside itself: {CONTEXT_RE.search(stem).group(0)!r}"))

            # S2 short explanation
            if 0 < len(expl.strip()) < 35:
                soft.append(("S2", where, cid, f"explanation only {len(expl.strip())} chars"))

            stem_list.append((cid, tokens(stem), where))

        # S3 letter bias per bank. A bank of 5 or 6 cannot satisfy 32 % at all
        # (four letters, five questions: one letter must repeat), so the floor
        # is two occurrences.
        n = len(qs)
        cap = max(2, int(0.32 * n))
        for letter, c in letters.items():
            if c > cap:
                soft.append(("S3", f.name, "-", f"letter {letter} = {c}/{n} ({100*c/n:.0f}%) over {cap}"))

        # S4 near-duplicate stems inside the bank
        for i in range(len(stem_list)):
            for j in range(i + 1, len(stem_list)):
                sim = jaccard(stem_list[i][1], stem_list[j][1])
                if sim >= 0.80:
                    soft.append(("S4", stem_list[i][2], stem_list[i][0],
                                 f"near-duplicate with {stem_list[j][0]} ({sim:.2f})"))
        by_subject[subject].append((f.name, n))

    return hard, soft, bank_count, q_count, by_subject


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", help="subject folder, quiz folder, or bank file")
    ap.add_argument("--strict", action="store_true", help="treat the soft checks as failures too")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--max-print", type=int, default=25, help="how many rows to print per section")
    args = ap.parse_args()

    hard, soft, banks, questions, by_subject = audit(args.paths, args.strict)

    if args.json:
        print(json.dumps({"banks": banks, "questions": questions,
                          "hard": [list(x) for x in hard],
                          "soft": [list(x) for x in soft]}, ensure_ascii=False, indent=1))
        return 1 if hard or (args.strict and soft) else 0

    print(f"banks: {banks}   questions: {questions}")
    for subj, rows in sorted(by_subject.items()):
        print(f"  {subj}: {len(rows)} banks / {sum(n for _, n in rows)} questions")

    if hard:
        print(f"\nFAIL — {len(hard)} hard defect(s):")
        for code, where, cid, msg in hard[:args.max_print]:
            print(f"  [{code}] {where} {cid}: {msg}")
        if len(hard) > args.max_print:
            print(f"  ... and {len(hard) - args.max_print} more")
    if soft:
        label = "FAIL (strict)" if args.strict else "warn"
        print(f"\n{label} — {len(soft)} soft finding(s):")
        for code, where, cid, msg in soft[:args.max_print]:
            print(f"  [{code}] {where} {cid}: {msg}")
        if len(soft) > args.max_print:
            print(f"  ... and {len(soft) - args.max_print} more")

    if not hard and not soft:
        print("\nRESULT: CLEAN")
    elif hard or (args.strict and soft):
        print("\nRESULT: FAIL")
    else:
        print("\nRESULT: PASS (soft findings are advisory)")

    return 1 if hard or (args.strict and soft) else 0


if __name__ == "__main__":
    sys.exit(main())
