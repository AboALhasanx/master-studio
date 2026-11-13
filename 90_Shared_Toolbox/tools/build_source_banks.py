#!/usr/bin/env python3
"""Import reviewed source MCQs without rewriting, guessing or permuting choices.

The prepared bilingual items and the independently reviewed original-text
manifest are separate inputs. All banks validate before any bank is written.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path

from quiz_source_gate import validate_source_bank

VAULT = Path(__file__).resolve().parents[2]


def split_into_batches(items, min_batch=10, max_batch=15):
    if not items:
        raise ValueError("chapter has no source questions")
    count = math.ceil(len(items) / max_batch)
    if len(items) < count * min_batch:
        raise ValueError("cannot split this chapter into approved 10-15 question batches")
    base, extra = divmod(len(items), count)
    batches, start = [], 0
    for index in range(count):
        size = base + (index < extra)
        batches.append(items[start:start+size])
        start += size
    return batches


def scaffold_source_bank(subject_id, subject_title, instructor_ar, instructor_en,
                         chapter_num, batch_num, items):
    questions = []
    for idx, original in enumerate(items, 1):
        q = copy.deepcopy(original)
        source = q.get("source")
        if not isinstance(source, dict) or not source.get("id") or not source.get("reference"):
            raise ValueError("each item requires explicit source provenance")
        if "answer" not in q or "correct" not in q:
            raise ValueError(f"{source['id']}: missing explicit answer/correct; guessing is forbidden")
        if not isinstance(q.get("options_en"), list) or len(q["options_en"]) != 4:
            raise ValueError(f"{source['id']}: exactly four original options are required")
        if q.get("options") != q["options_en"]:
            raise ValueError(f"{source['id']}: options and options_en differ")
        q["id"] = f"q{idx}"
        q["bank_kind"] = "source"
        if not q.get("concept_id"):
            raise ValueError(f"{source['id']}: missing stable chapter-wide concept id")
        q.pop("source_id", None)
        questions.append(q)
    return {
        "schema_version": 2, "bank_kind": "source", "subject_id": subject_id,
        "subject_title": subject_title, "subject": subject_id,
        "semester": 1, "semester_label": "كورس أول",
        "instructor_ar": instructor_ar, "instructor": instructor_en,
        "quiz_id": f"Quiz_Ch{chapter_num:02d}_S{batch_num:02d}_Source_MCQs",
        "topic": f"Source MCQs — Batch {batch_num}",
        "topic_ar": f"أسئلة المصدر — الدفعة {batch_num}",
        "questions": questions,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--items", required=True, type=Path, help="prepared {chapters:[{chapter_no,questions}]} JSON")
    ap.add_argument("--manifest", required=True, type=Path, help="independently reviewed source-text manifest")
    ap.add_argument("--subject", default="04_Advanced_Software_Eng")
    ap.add_argument("--output-dir", required=True, type=Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    out = args.output_dir.resolve()
    manifest_path = args.manifest.resolve()
    if not manifest_path.is_relative_to(out):
        ap.error("manifest must be inside output-dir (normally source_manifests/)")
    try:
        prepared = json.loads(args.items.read_text(encoding="utf-8-sig"))
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        canonical_dir = VAULT / "01_Semester_1" / args.subject / "07_Quizzes_&_Anki"
        identity = next(json.loads(p.read_text(encoding="utf-8")) for p in sorted(canonical_dir.glob("Quiz_*.json"))
                        if "_Source_MCQs" not in p.name)
        plan, seen_chapters, seen_sources, seen_concepts = [], set(), set(), set()
        for chapter in prepared["chapters"]:
            ch = chapter["chapter_no"]
            if type(ch) is not int or ch < 1 or ch in seen_chapters:
                raise ValueError("invalid or repeated chapter number")
            seen_chapters.add(ch)
            for q in chapter["questions"]:
                sid = q["source"]["id"]
                concept = q["concept_id"]
                if sid in seen_sources or concept in seen_concepts:
                    raise ValueError(f"duplicate source/concept identity: {sid}")
                seen_sources.add(sid)
                seen_concepts.add(concept)
            for batch_no, items in enumerate(split_into_batches(chapter["questions"]), 1):
                bank = scaffold_source_bank(args.subject, identity["subject_title"], identity["instructor_ar"],
                                            identity["instructor"], ch, batch_no, items)
                bank["source_manifest"] = manifest_path.relative_to(out).as_posix()
                path = out / (bank["quiz_id"] + ".json")
                ok, errors, _ = validate_source_bank(bank, path=path, manifest=manifest, check_publish=True)
                if not ok:
                    raise ValueError("\n".join(errors))
                if path.exists() and json.loads(path.read_text(encoding="utf-8")) != bank:
                    raise ValueError(f"refusing to overwrite different existing bank: {path}")
                plan.append((path, bank))
        if not plan:
            raise ValueError("no chapters to import")
        for path, bank in plan:
            if not args.dry_run and not path.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"{'CHECK' if args.dry_run else 'READY'} {path.name}: {len(bank['questions'])} questions")
        print(f"Validated {len(plan)} source banks; {'no files written' if args.dry_run else 'original text/order preserved'}")
        return 0
    except (OSError, ValueError, KeyError, TypeError, StopIteration) as exc:
        print(f"REFUSED: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
