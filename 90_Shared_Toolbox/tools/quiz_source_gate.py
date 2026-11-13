#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""quiz_source_gate.py — Standalone quality and fidelity gate for Source-mode MCQs.

Validates:
  1. bank_kind == "source" and Quiz_ChNN_SNN_Source_MCQs naming
  2. Isolated concept namespace (e.g. ase_source_chNN_qXX)
  3. Structural bilingual completeness (stems, 4 options, explanations)
  4. Provenance metadata (source.id, source.reference, source.key_status, source.note)
  5. Answer key rules & explicit UNGRADED disputed handling:
     - confirmed/derived: valid letter A-D, int 0-3, synchronized
     - disputed: MUST have answer: null and correct: null (ungraded), plus
       nonempty bilingual note explaining ambiguity. Guessed keys are rejected.
  6. Source manifest fidelity & tamper verification:
     - Verifies original English stem and options against authoritative source manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

LETTERS = "ABCD"
BLOOM_LEVELS = {"Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"}
SOURCE_ID_PATTERN = re.compile(r"^Quiz_Ch(?:\d+)_S(?:\d+)_Source_MCQs(?:\.json)?$", re.I)
SOURCE_CONCEPT_PATTERN = re.compile(r"^[a-z0-9_]+_source_ch(?:\d+)_q(?:\d+)$", re.I)
VAULT = Path(__file__).resolve().parents[2]


def norm_str(s: str) -> str:
    if not isinstance(s, str):
        return ""
    s = unicodedata.normalize("NFKC", s).strip().casefold()
    return re.sub(r"\s+", " ", s)


def hash_text(text: str) -> str:
    return hashlib.sha256(norm_str(text).encode("utf-8")).hexdigest()[:16]


def validate_source_bank(bank: dict, path: Path | None = None, manifest: dict | None = None, check_publish: bool = False) -> tuple[bool, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(bank, dict):
        return False, ["source bank must be an object"], []
    label = path.name if path else (bank.get("quiz_id") or "<source-bank>")
    if not isinstance(bank.get("subject_id"), str) or not re.fullmatch(r"\d{2}_[A-Za-z0-9_]+", bank["subject_id"]):
        return False, [f"{label}: invalid subject_id"], []

    # 1. bank_kind check
    bank_kind = bank.get("bank_kind")
    if not bank_kind:
        errors.append(f"{label}: missing 'bank_kind'; must be explicitly 'source'")
    elif bank_kind != "source":
        errors.append(f"{label}: invalid bank_kind {bank_kind!r}; quiz_source_gate only validates 'source' banks")

    # 2. Schema envelope
    if bank.get("schema_version") != 2:
        errors.append(f"{label}: schema_version must be 2, got {bank.get('schema_version')!r}")

    quiz_id = bank.get("quiz_id") or ""
    if not quiz_id:
        errors.append(f"{label}: missing 'quiz_id'")
    elif not isinstance(quiz_id, str) or not SOURCE_ID_PATTERN.match(quiz_id):
        errors.append(f"{label}: quiz_id {quiz_id!r} does not follow 'Quiz_ChNN_SNN_Source_MCQs' pattern")

    if path and not SOURCE_ID_PATTERN.match(path.stem):
        errors.append(f"{label}: file name does not follow 'Quiz_ChNN_SNN_Source_MCQs.json' convention")
    if path and path.stem != quiz_id:
        errors.append(f"{label}: quiz_id must equal file stem")

    if check_publish and manifest is None:
        relative = bank.get("source_manifest")
        if not isinstance(relative, str) or not relative.strip():
            errors.append(f"{label}: source_manifest is required for publication")
        else:
            base = path.resolve().parent if path else VAULT / "01_Semester_1" / bank["subject_id"] / "07_Quizzes_&_Anki"
            candidate = (base / relative).resolve()
            if Path(relative).is_absolute() or not candidate.is_relative_to(base.resolve()):
                errors.append(f"{label}: source_manifest must remain inside the bank directory")
            else:
                try:
                    manifest = json.loads(candidate.read_text(encoding="utf-8"))
                except (OSError, ValueError) as exc:
                    errors.append(f"{label}: source_manifest cannot be read: {exc}")

    manifest_items = None
    if manifest is not None:
        if not isinstance(manifest, dict):
            errors.append(f"{label}: source manifest must be an object")
        else:
            manifest_items = manifest.get("items")
            if not isinstance(manifest_items, dict) or not manifest_items:
                errors.append(f"{label}: source manifest requires a nonempty items map")
                manifest_items = {}
            if check_publish:
                if manifest.get("schema_version") != 1 or not str(manifest.get("review") or "").strip():
                    errors.append(f"{label}: source manifest lacks the reviewed schema/review stamp")
                if manifest.get("subject_id") != bank.get("subject_id"):
                    errors.append(f"{label}: source manifest subject mismatch")
                sources = manifest.get("sources")
                if not isinstance(sources, dict) or not sources:
                    errors.append(f"{label}: source manifest requires original-file hashes")
                else:
                    subject_root = VAULT / "01_Semester_1" / bank["subject_id"]
                    for rel, digest in sources.items():
                        original = (subject_root / rel).resolve()
                        if Path(rel).is_absolute() or not original.is_relative_to(subject_root.resolve()):
                            errors.append(f"{label}: original source path escapes subject directory")
                            continue
                        try:
                            actual = hashlib.sha256(original.read_bytes()).hexdigest()
                            if actual != digest:
                                errors.append(f"{label}: original source file changed: {rel}")
                        except OSError:
                            errors.append(f"{label}: original source file missing: {rel}")
    elif not check_publish:
        warnings.append(f"{label}: structural checks only; no source manifest supplied")

    for req_top in ("subject_id", "subject_title", "semester", "semester_label", "topic", "instructor_ar"):
        val = bank.get(req_top)
        if val is None or (isinstance(val, str) and not val.strip()):
            errors.append(f"{label}: missing or empty top-level property '{req_top}'")

    questions = bank.get("questions")
    if not isinstance(questions, list) or len(questions) == 0:
        errors.append(f"{label}: 'questions' must be a non-empty array")
        return False, errors, warnings

    if len(questions) < 4:
        errors.append(f"{label}: bank has only {len(questions)} questions (minimum 4 required)")
    elif not (10 <= len(questions) <= 15):
        (errors if check_publish else warnings).append(f"{label}: student approved batch size is 10-15 questions per chapter; bank has {len(questions)}")

    # 3. Question-level checks
    local_ids: set[str] = set()
    local_concepts: set[str] = set()
    local_sources: set[str] = set()
    source_order: list[int] = []
    quiz_chapter = re.search(r"Ch(\d+)_", quiz_id)

    for idx, q in enumerate(questions):
        if not isinstance(q, dict):
            errors.append(f"{label}: question {idx+1} must be an object")
            continue
        qid = str(q.get("id") or f"q{idx+1}")
        q_label = f"{label}#{qid}"

        if qid in local_ids:
            errors.append(f"{q_label}: duplicate question id")
        local_ids.add(qid)
        if q.get("id") != f"q{idx+1}":
            errors.append(f"{q_label}: question ids must be sequential q1..qN")

        q_kind = q.get("bank_kind") or bank_kind
        if q_kind != "source":
            errors.append(f"{q_label}: question bank_kind mismatch (expected 'source', got {q_kind!r})")

        # Concept id
        concept = str(q.get("concept_id") or "").strip()
        if not concept:
            errors.append(f"{q_label}: missing concept_id")
        else:
            if not SOURCE_CONCEPT_PATTERN.match(concept):
                errors.append(f"{q_label}: concept_id {concept!r} must follow '[subject]_source_chNN_qXX' convention")
            if concept in local_concepts:
                errors.append(f"{q_label}: duplicate concept_id {concept!r} within bank")
            local_concepts.add(concept)

        # Bloom level
        bloom = q.get("bloom_level")
        if bloom not in BLOOM_LEVELS:
            errors.append(f"{q_label}: invalid bloom_level {bloom!r}; expected one of {sorted(BLOOM_LEVELS)}")

        # Stems
        stem_en = q.get("question")
        stem_ar = q.get("question_ar")
        if not isinstance(stem_en, str) or not stem_en.strip():
            errors.append(f"{q_label}: missing or empty English stem ('question')")
        if not isinstance(stem_ar, str) or not stem_ar.strip():
            errors.append(f"{q_label}: missing or empty Arabic stem ('question_ar')")

        # Options
        for opt_key in ("options", "options_en", "options_ar"):
            opts = q.get(opt_key)
            if not isinstance(opts, list) or len(opts) != 4 or any(not isinstance(x, str) or not x.strip() for x in opts):
                errors.append(f"{q_label}: '{opt_key}' must be an array of exactly 4 non-empty strings")
        if isinstance(q.get("options"), list) and isinstance(q.get("options_en"), list):
            if q["options"] != q["options_en"]:
                errors.append(f"{q_label}: 'options' and 'options_en' must be identical")

        # Explanations
        expl_en = q.get("explanation")
        expl_ar = q.get("explanation_ar")
        if not isinstance(expl_en, str) or not expl_en.strip():
            errors.append(f"{q_label}: missing or empty English explanation")
        if not isinstance(expl_ar, str) or not expl_ar.strip():
            errors.append(f"{q_label}: missing or empty Arabic explanation ('explanation_ar')")

        # Provenance metadata
        src = q.get("source")
        if not isinstance(src, dict):
            errors.append(f"{q_label}: missing required 'source' metadata object")
            continue

        src_id = str(src.get("id") or "").strip()
        src_ref = str(src.get("reference") or "").strip()
        k_status = src.get("key_status")
        note = src.get("note")

        if not src_id:
            errors.append(f"{q_label}: missing 'source.id'")
        if src_id in local_sources:
            errors.append(f"{q_label}: duplicate source.id {src_id!r}")
        local_sources.add(src_id)
        order_match = re.match(r"\d+\.(\d+)$", src_id)
        if order_match:
            source_order.append(int(order_match.group(1)))
        path_chapter = re.search(r"Ch(\d+)_", str(src.get("path") or ""))
        if quiz_chapter and path_chapter and int(path_chapter.group(1)) != int(quiz_chapter.group(1)):
            errors.append(f"{q_label}: source file belongs to another chapter")
        if not src_ref:
            errors.append(f"{q_label}: missing 'source.reference'")
        if k_status not in ("confirmed", "derived", "disputed"):
            errors.append(f"{q_label}: invalid 'source.key_status' {k_status!r}; expected 'confirmed', 'derived', or 'disputed'")

        if not isinstance(note, dict) or "ar" not in note or "en" not in note:
            errors.append(f"{q_label}: 'source.note' must be an object with 'ar' and 'en' keys")

        # Answer key rules & Ungraded disputed items
        ans = q.get("answer")
        corr = q.get("correct")

        if k_status == "disputed":
            # Disputed source item MUST be explicit UNGRADED (answer: null, correct: null)
            if "answer" not in q or "correct" not in q or ans is not None or corr is not None:
                errors.append(f"{q_label}: disputed source item must have answer: null and correct: null (ungraded). Guessing a key is forbidden (got answer={ans!r}, correct={corr!r})")
            if not (isinstance(note, dict) and str(note.get("ar", "")).strip() and str(note.get("en", "")).strip()):
                errors.append(f"{q_label}: disputed source item requires nonempty bilingual 'source.note' explaining ambiguity")
        else:
            # Confirmed or derived key
            if not isinstance(ans, str) or len(ans) != 1 or ans not in LETTERS:
                errors.append(f"{q_label}: 'answer' must be one of {LETTERS}, got {ans!r}")
            if type(corr) is not int or corr not in range(4):
                errors.append(f"{q_label}: 'correct' must be an integer 0..3, got {corr!r}")
            if isinstance(ans, str) and len(ans) == 1 and ans in LETTERS and type(corr) is int and 0 <= corr < 4:
                if LETTERS[corr] != ans:
                    errors.append(f"{q_label}: answer/correct mismatch ({ans} vs {corr})")

        # 4. Manifest verification against separate source manifest (tamper detection)
        if manifest_items is not None:
            m_item = manifest_items.get(src_id)
            if not isinstance(m_item, dict):
                errors.append(f"{q_label}: missing source manifest item {src_id!r}")
            else:
                m_stem = m_item.get("question")
                m_opts = m_item.get("options")
                if not isinstance(m_stem, str) or not isinstance(m_opts, list) or len(m_opts) != 4:
                    errors.append(f"{q_label}: incomplete source manifest item {src_id!r}")
                    continue
                if stem_en != m_stem:
                    errors.append(f"{q_label}: English stem does not match source manifest for item {src_id!r} (tamper/alteration detected)")
                if isinstance(m_opts, list) and len(m_opts) == 4:
                    q_opts = q.get("options_en") or []
                    for opt_i in range(4):
                        if opt_i < len(q_opts) and q_opts[opt_i] != m_opts[opt_i]:
                            errors.append(f"{q_label}: Option [{opt_i}] does not match source manifest for item {src_id!r} (tamper/alteration detected)")
                if check_publish:
                    for field, actual in (("answer", ans), ("correct", corr), ("key_status", k_status)):
                        if field not in m_item or m_item[field] != actual:
                            errors.append(f"{q_label}: {field} differs from reviewed source manifest")
                    if not m_item.get("source_path") or m_item["source_path"] not in manifest.get("sources", {}):
                        errors.append(f"{q_label}: manifest item lacks a hashed original source anchor")
                    if type(m_item.get("source_line")) is not int or m_item["source_line"] < 1:
                        errors.append(f"{q_label}: manifest item requires an original source line")
                    if src.get("path") != m_item.get("source_path") or src.get("line") != m_item.get("source_line"):
                        errors.append(f"{q_label}: source provenance anchor differs from reviewed manifest")
                    if src_ref != m_item.get("reference"):
                        errors.append(f"{q_label}: source reference differs from reviewed manifest")

    if source_order != sorted(source_order):
        errors.append(f"{label}: source question order is not ascending")
    is_valid = len(errors) == 0
    return is_valid, errors, warnings


def validate_source_collection(entries) -> list[str]:
    """Reject the same reviewed source item in more than one bank."""
    errors: list[str] = []
    seen: dict[str, str] = {}
    for path, bank in entries:
        if not isinstance(bank, dict) or bank.get("bank_kind") != "source":
            continue
        for q in bank.get("questions") or []:
            src = q.get("source") if isinstance(q, dict) else None
            sid = str((src or {}).get("id") or "").strip()
            if not sid:
                continue
            label = getattr(path, "name", str(path))
            if sid in seen:
                errors.append(f"{label}: source.id {sid!r} already used by {seen[sid]}")
            else:
                seen[sid] = label
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Standalone source MCQ quality and fidelity gate.")
    parser.add_argument("banks", nargs="+", type=Path, help="Path(s) to source quiz bank JSON files")
    parser.add_argument("--manifest", type=Path, help="Path to authoritative source manifest for text verification")
    parser.add_argument("--check-publish", action="store_true", help="Enforce publication readiness checks")
    args = parser.parse_args()

    manifest_data = None
    if args.manifest:
        if not args.manifest.exists():
            print(f"ERROR: manifest file not found: {args.manifest}", file=sys.stderr)
            return 2
        try:
            with open(args.manifest, "r", encoding="utf-8") as f:
                manifest_data = json.load(f)
        except Exception as exc:
            print(f"ERROR: failed to parse manifest: {exc}", file=sys.stderr)
            return 2

    paths = []
    for p in args.banks:
        if p.is_dir():
            paths.extend(sorted(p.glob("Quiz_*_Source_MCQs*.json")))
        elif p.exists():
            paths.append(p)
        else:
            print(f"ERROR: path does not exist: {p}", file=sys.stderr)
            return 2

    if not paths:
        print("ERROR: no source bank files matched", file=sys.stderr)
        return 2

    all_ok = True
    total_questions = 0

    for path in paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                bank = json.load(f)
        except Exception as exc:
            print(f"FAIL: {path.name}: JSON parse error ({exc})")
            all_ok = False
            continue

        ok, errs, warns = validate_source_bank(bank, path=path, manifest=manifest_data, check_publish=args.check_publish)
        total_questions += len(bank.get("questions") or [])

        print(f"Checking {path.name} ({len(bank.get('questions') or [])} questions)...")
        for w in warns:
            print(f"  [WARN] {w}")
        for e in errs:
            print(f"  [ERROR] {e}")

        if not ok:
            all_ok = False
            print(f"RESULT: FAIL ({len(errs)} error(s))\n")
        else:
            print("RESULT: PASS\n")

    if all_ok:
        print(f"ALL SOURCE BANKS PASSED ({len(paths)} banks, {total_questions} questions)")
        return 0
    else:
        print(f"SOURCE GATE FAILED on one or more banks", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
