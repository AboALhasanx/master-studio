#!/usr/bin/env python3
"""
Master Studio Curriculum Quiz Bundle Packager
--------------------------------------------
Bundles all normalized Canonical Schema v2 quiz files for a semester into
a single curriculum bundle JSON file for offline phone transfer, direct ADB push,
or 1-click batch browser import.

Usage:
  python pack_quiz_bundle.py
  python pack_quiz_bundle.py --semester 1 -o 00_STUDIO_HUB/curriculum_quiz_bundle_sem1.json
"""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

# Ensure tools directory is in sys.path
_current_dir = Path(__file__).resolve().parent
if str(_current_dir) not in sys.path:
    sys.path.insert(0, str(_current_dir))

from quiz_balancer import normalize_quiz_schema, validate_schema_v2


def create_quiz_bundle(semester: int = 1, base_dir: Path = None) -> dict:
    """
    Compiles all canonical quiz banks in the specified semester into a single bundle.
    """
    if base_dir is None:
        base_dir = _current_dir.parent.parent

    sem_name = f"0{semester}_Semester_{semester}"
    sem_path = base_dir / sem_name
    if not sem_path.is_dir():
        candidates = sorted([d for d in base_dir.glob(f"0{semester}_Semester_*") if d.is_dir()])
        sem_path = candidates[0] if candidates else (base_dir / "01_Semester_1")

    quiz_files = sorted(sem_path.glob("*/07_Quizzes_&_Anki/Quiz_*.json"))
    quizzes = []

    for qf in quiz_files:
        try:
            content = json.loads(qf.read_text(encoding="utf-8"))
            subj = qf.parent.parent.name
            normalized = normalize_quiz_schema(content, subject_id=subj, quiz_id=qf.stem)
            is_valid, errors = validate_schema_v2(normalized)
            if not is_valid:
                print(f"⚠️ Warning: Quiz {qf.name} had schema validation warnings: {errors}", file=sys.stderr)
            quizzes.append(normalized)
        except Exception as e:
            print(f"❌ Error loading {qf}: {e}", file=sys.stderr)

    bundle = {
        "bundle_version": 2,
        "exported_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "semester": semester,
        "total_quizzes": len(quizzes),
        "quizzes": quizzes,
    }
    return bundle


def main():
    parser = argparse.ArgumentParser(description="Master Studio Curriculum Quiz Packager")
    parser.add_argument("--semester", type=int, default=1, help="Semester number (default: 1)")
    parser.add_argument("-o", "--output", help="Output path (defaults to 00_STUDIO_HUB/curriculum_quiz_bundle_sem<semester>.json)")
    parser.add_argument("--minified", action="store_true", help="Output minified JSON without indentation")
    args = parser.parse_args()

    repo_root = _current_dir.parent.parent
    hub_dir = repo_root / "00_STUDIO_HUB"

    default_output = hub_dir / f"curriculum_quiz_bundle_sem{args.semester}.json"
    out_path = Path(args.output) if args.output else default_output

    print(f"📦 Packaging Curriculum Quiz Bundle for Semester {args.semester}...")
    bundle = create_quiz_bundle(semester=args.semester, base_dir=repo_root)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    indent = None if args.minified else 2
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=indent)

    print(f"✅ Successfully packaged {bundle['total_quizzes']} quizzes into: {out_path}")
    print(f"   Bundle Version: {bundle['bundle_version']} | Total Questions: {sum(len(q.get('questions', [])) for q in bundle['quizzes'])}")


if __name__ == "__main__":
    main()
