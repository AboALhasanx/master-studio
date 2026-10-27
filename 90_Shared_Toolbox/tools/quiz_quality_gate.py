#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Read-only structural and editorial QA for one or more MCSQuiz v2 banks.

The portal schema and psychometric balancer remain authoritative for those
checks. This gate adds cross-bank checks that they do not provide: duplicate
IDs/concepts/stems, answer-index drift, option-array drift, bilingual option
shape, repeated formulas, and near-duplicate question warnings.

Examples:
    python quiz_quality_gate.py path/to/Quiz_Ch04_T01.json path/to/Quiz_Ch04_T02.json
    python quiz_quality_gate.py --shape-gate path/to/chapter/banks/*.json

Default mode fails only on deterministic structural defects. Editorial and
near-duplicate findings are reported as warnings. --shape-gate additionally
enforces the published option-spread and answer-position thresholds. This tool
never edits banks, reorders options, or publishes content.
"""

from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path


LETTERS = "ABCD"
SPREAD_CAPS = {"options": 1.40, "options_ar": 1.30}
KEY_RATIO_MIN = 0.88
KEY_RATIO_MAX = 1.12
MATH_RE = re.compile(r"\$\$.*?\$\$|\$(?!\$).*?\$", re.S)
WORD_RE = re.compile(r"[a-z0-9]+|[\u0600-\u06ff]+", re.I)
STOP_WORDS = {
    "what", "which", "why", "how", "does", "do", "the", "a", "an", "is", "are",
    "in", "on", "to", "of", "for", "and", "or", "with", "that", "this", "from",
    "ما", "ماذا", "كيف", "ليش", "لماذا", "هو", "هي", "في", "من", "على", "إلى",
    "عن", "و", "او", "أو", "ال", "هذا", "هذه", "الذي", "التي", "منه", "لـ",
}


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "").casefold()
    text = text.replace("ـ", "")
    text = re.sub(r"[\u064B-\u065F\u0670]", "", text)
    text = re.sub(r"[أإآ]", "ا", text)
    text = re.sub(r"ى", "ي", text)
    return " ".join(WORD_RE.findall(text))


def exact_key(text: str) -> str:
    """Normalize prose but retain operators/digits so distinct formulas stay distinct."""
    text = unicodedata.normalize("NFKC", text or "").casefold()
    text = text.replace("ـ", "").replace("−", "-").replace("×", "*e").replace("÷", "/")
    text = re.sub(r"[\u064B-\u065F\u0670]", "", text)
    text = re.sub(r"[أإآ]", "ا", text).replace("ى", "ي")
    text = re.sub(r"[^\w\u0600-\u06ff=+\-*/^_{}()\[\]]+", "", text)
    return text


def tokens(text: str) -> set[str]:
    return {t for t in norm(text).split() if len(t) > 1 and t not in STOP_WORDS}


def similarity(a: str, b: str) -> float:
    na, nb = norm(a), norm(b)
    seq = SequenceMatcher(None, na, nb).ratio()
    ta, tb = tokens(a), tokens(b)
    jac = len(ta & tb) / len(ta | tb) if ta | tb else 1.0
    return max(seq, jac)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("banks", nargs="+", type=Path, help="Bank JSON paths; shell globs are accepted")
    ap.add_argument("--chapter", help="Limit directory input to this chapter number")
    ap.add_argument("--shape-gate", action="store_true", help="Fail on option spread and answer-length shape thresholds")
    ap.add_argument("--near-duplicate-threshold", type=float, default=0.88)
    ap.add_argument("--max-warnings", type=int, default=60, help="Maximum warning lines to print")
    args = ap.parse_args()

    paths: list[Path] = []
    for path in args.banks:
        if path.is_dir():
            paths.extend(sorted(path.glob("Quiz_*.json")))
        elif path.exists():
            paths.append(path)
        else:
            print(f"ERROR: bank path does not exist: {path}")
            return 2
    paths = sorted(dict.fromkeys(p.resolve() for p in paths))
    if not paths:
        print("ERROR: no bank files matched")
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    seen_concepts: dict[tuple[str, str], tuple[Path, str]] = {}
    seen_stems: dict[tuple[str, str], tuple[Path, str]] = {}
    records: list[tuple[Path, dict, str]] = []
    formula_map: dict[tuple[str, str], list[tuple[Path, str]]] = defaultdict(list)
    chapter_shape: dict[str, dict[str, Counter]] = defaultdict(
        lambda: {lang: Counter() for lang in SPREAD_CAPS}
    )
    chapter_counts: Counter = Counter()
    processed_banks = 0

    for path in paths:
        try:
            bank = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path.name}: invalid JSON ({exc})")
            continue
        if not isinstance(bank, dict) or not isinstance(bank.get("questions"), list):
            errors.append(f"{path.name}: missing questions array")
            continue
        raw_chapter = bank.get("chapter")
        if raw_chapter is None:
            match = re.search(r"(?:^|_)Ch(?:apter)?0*(\d+)(?:_|$)", path.stem, re.I)
            chapter = match.group(1) if match else "?"
        else:
            chapter = str(raw_chapter).lstrip("0") or "0"
        if args.chapter is not None and chapter != str(args.chapter):
            continue
        processed_banks += 1
        chapter_counts[chapter] += len(bank["questions"])
        local_ids: set[str] = set()

        for q in bank["questions"]:
            if not isinstance(q, dict):
                errors.append(f"{path.name}: non-object question")
                continue
            qid = str(q.get("id", "<missing-id>"))
            label = f"{path.name}/{qid}"
            if qid in local_ids:
                errors.append(f"{label}: duplicate question id in bank")
            local_ids.add(qid)

            concept = str(q.get("concept_id", "")).strip()
            if not concept:
                errors.append(f"{label}: missing concept_id")
            elif (chapter, concept) in seen_concepts:
                old_path, old_qid = seen_concepts[(chapter, concept)]
                errors.append(f"{label}: duplicate concept_id {concept!r} (also {old_path.name}/{old_qid})")
            else:
                seen_concepts[(chapter, concept)] = (path, qid)

            stem = q.get("question")
            stem_ar = q.get("question_ar")
            if not isinstance(stem, str) or not stem.strip():
                errors.append(f"{label}: empty English stem")
            if not isinstance(stem_ar, str) or not stem_ar.strip():
                errors.append(f"{label}: empty Arabic stem")
            if isinstance(stem, str) and isinstance(stem_ar, str):
                key = (chapter, exact_key(stem))
                if key in seen_stems:
                    old_path, old_qid = seen_stems[key]
                    errors.append(f"{label}: exact duplicate English stem (also {old_path.name}/{old_qid})")
                else:
                    seen_stems[key] = (path, qid)
                if stem.count("?") > 1 or stem_ar.count("؟") > 1:
                    warnings.append(f"{label}: multiple question marks; inspect for a compound stem")

            correct = q.get("correct")
            answer = q.get("answer")
            if not isinstance(correct, int) or isinstance(correct, bool) or correct not in range(4):
                errors.append(f"{label}: correct must be integer 0..3")
                correct = None
            if answer not in LETTERS:
                errors.append(f"{label}: answer must be A/B/C/D")
            elif correct is not None and LETTERS[correct] != answer:
                errors.append(f"{label}: answer/correct mismatch ({answer} vs {correct})")

            for field in ("options", "options_en", "options_ar"):
                opts = q.get(field)
                if not isinstance(opts, list) or len(opts) != 4 or any(not isinstance(x, str) or not x.strip() for x in opts):
                    errors.append(f"{label}: {field} must contain four non-empty strings")
                    continue
                normalized = [exact_key(x) for x in opts]
                if len(set(normalized)) != 4:
                    errors.append(f"{label}: duplicate choices in {field}")
            if isinstance(q.get("options"), list) and isinstance(q.get("options_en"), list):
                if q["options"] != q["options_en"]:
                    errors.append(f"{label}: options and options_en differ")

            if correct is not None:
                for field, cap in SPREAD_CAPS.items():
                    opts = q.get(field)
                    if isinstance(opts, list) and len(opts) == 4 and all(isinstance(x, str) for x in opts):
                        lengths = [len(x.strip()) for x in opts]
                        if min(lengths) == 0:
                            continue
                        chapter_shape[chapter][field]["longest"] += int(lengths[correct] == max(lengths) and lengths.count(lengths[correct]) == 1)
                        chapter_shape[chapter][field]["shortest"] += int(lengths[correct] == min(lengths) and lengths.count(lengths[correct]) == 1)
                        chapter_shape[chapter][field]["spread"] += int(max(lengths) / min(lengths) > cap)
                        chapter_shape[chapter][field]["total"] += 1
                        if max(lengths) / min(lengths) > cap:
                            warnings.append(f"{label}: {field} spread {max(lengths)}/{min(lengths)} exceeds {cap:.2f}")
                        distractor_avg = (sum(lengths) - lengths[correct]) / 3
                        answer_ratio = lengths[correct] / distractor_avg if distractor_avg else 0
                        if not KEY_RATIO_MIN <= answer_ratio <= KEY_RATIO_MAX:
                            chapter_shape[chapter][field]["key_ratio"] += 1
                            warnings.append(f"{label}: {field} key/distractor-average ratio {answer_ratio:.2f} is outside {KEY_RATIO_MIN:.2f}..{KEY_RATIO_MAX:.2f}")

            for field in ("question", "question_ar", "explanation", "explanation_ar"):
                text = q.get(field)
                if not isinstance(text, str) or not text.strip():
                    errors.append(f"{label}: missing {field}")
                elif field.startswith("explanation") and len(text.strip()) < 35:
                    warnings.append(f"{label}: {field} is very short; check that it teaches the reasoning")
                if isinstance(text, str):
                    for math in MATH_RE.findall(text):
                        formula = re.sub(r"\s+", "", math.strip("$ "))
                        if len(formula) >= 5:
                            formula_map[(chapter, formula)].append((path, qid))

            records.append((path, q, chapter))

    # Near-duplicate analysis is advisory. It catches paraphrases without
    # pretending lexical similarity proves conceptual duplication.
    for (pa, qa, ca), (pb, qb, cb) in itertools.combinations(records, 2):
        if ca != cb:
            continue
        if pa == pb and qa.get("id") == qb.get("id"):
            continue
        if not isinstance(qa.get("question"), str) or not isinstance(qb.get("question"), str):
            continue
        score = similarity(qa["question"], qb["question"])
        if score >= args.near_duplicate_threshold:
            warnings.append(
                f"near-duplicate stems {score:.2f}: {pa.name}/{qa.get('id')}"
                f" [{qa.get('concept_id')}] vs {pb.name}/{qb.get('id')} [{qb.get('concept_id')}]"
            )

    for (chapter, formula), occurrences in formula_map.items():
        if len(occurrences) > 1:
            locations = ", ".join(f"{p.name}/{qid}" for p, qid in occurrences[:5])
            warnings.append(f"chapter {chapter}: formula repeated {len(occurrences)} times ({formula[:45]}): {locations}")

    if not processed_banks:
        print("ERROR: no bank files matched the requested chapter")
        return 2

    shape_errors: list[str] = []
    for chapter, fields in chapter_shape.items():
        for field, counts in fields.items():
            total = counts["total"]
            if not total:
                continue
            for kind in ("longest", "shortest"):
                share = counts[kind] / total
                if share > 0.30:
                    shape_errors.append(f"chapter {chapter}: {field} correct {kind} {counts[kind]}/{total} ({share:.1%}) exceeds 30%")
            if counts["spread"]:
                shape_errors.append(f"chapter {chapter}: {field} spread violations={counts['spread']}/{total}")
            if counts["key_ratio"]:
                shape_errors.append(f"chapter {chapter}: {field} key/distractor-average ratio violations={counts['key_ratio']}/{total}")

    print(f"QUIZ QUALITY GATE — read-only — {processed_banks} bank(s), {sum(chapter_counts.values())} question(s)")
    print(f"Structural errors: {len(errors)} | Editorial warnings: {len(warnings)}")
    categories = Counter()
    for warning in warnings:
        if warning.startswith("near-duplicate stems"):
            categories["near-duplicate stems"] += 1
        elif "formula repeated" in warning:
            categories["repeated formulas"] += 1
        elif "explanation_" in warning:
            categories["short explanations"] += 1
        elif "multiple question marks" in warning:
            categories["compound stems"] += 1
        elif " spread " in warning:
            categories["option spread"] += 1
        elif "key/distractor-average" in warning:
            categories["key/option length ratio"] += 1
    if categories:
        print("Warning categories:", "; ".join(f"{k}={v}" for k, v in sorted(categories.items())))
    for err in errors[:100]:
        print("ERROR:", err)
    if args.shape_gate:
        print(f"Shape-gate failures: {len(shape_errors)}")
        for err in shape_errors:
            print("SHAPE:", err)
    if warnings:
        print("Warnings:")
        for warning in warnings[: args.max_warnings]:
            print("WARN:", warning)
        if len(warnings) > args.max_warnings:
            print(f"WARN: ... {len(warnings) - args.max_warnings} additional warning(s) suppressed")
    if errors or (args.shape_gate and shape_errors):
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS (warnings are advisory; review them before release)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
