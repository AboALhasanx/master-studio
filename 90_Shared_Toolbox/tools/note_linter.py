#!/usr/bin/env python3
"""Master Studio: Academic Study Note Pre-Flight Linter & Auto-Fixer (System 1 Gate).

Enforces structural invariants, syntax balancing, and zero-leakage policies
on Markdown study notes before PDF compilation.
Designed to guarantee 100% aesthetic perfection even from cheap or small LLMs.

Usage:
    python note_linter.py <path_to_note.md> [--fix] [--strict]
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple, Dict

def lint_and_fix_markdown(file_path: Path, auto_fix: bool = False) -> Tuple[int, List[str], List[str]]:
    """Lints a Markdown study note and optionally applies deterministic auto-repairs.
    
    Returns:
        (error_count, list_of_errors, list_of_fixes)
    """
    if not file_path.exists():
        return 1, [f"File not found: {file_path}"], []

    content = file_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    errors: List[str] = []
    fixes: List[str] = []
    repaired_lines: List[str] = []
    
    # Flags & tracking
    in_code_fence = False
    fence_lang = ""
    has_retrieval_set = False
    first_heading_seen = False
    
    for idx, line in enumerate(lines):
        line_num = idx + 1
        orig_line = line
        
        # Track code fences
        fence_m = re.match(r"^```(\w*)", line)
        if fence_m:
            if not in_code_fence:
                in_code_fence = True
                fence_lang = fence_m.group(1).lower()
            else:
                in_code_fence = False
                fence_lang = ""
            repaired_lines.append(line)
            continue
            
        # Inside code fences: check for forbidden ASCII art
        if in_code_fence:
            if fence_lang in ["text", "txt", ""] and re.search(r"[↓↑←→|│─┌┐└┘├┤┼▼▲◄►]", line):
                errors.append(f"Line {line_num}: Prohibited ASCII diagram detected in ```{fence_lang} fence. Replace with a 2x vector graphic in 06_Diagrams_&_Mindmaps/.")
            repaired_lines.append(line)
            continue

        # Check for retrieval set heading
        if re.match(r"^##\s+.*?(?:retrieval|active\s*recall|أسئلة|الاسترجاع)", line, re.IGNORECASE):
            has_retrieval_set = True

        # 1. Unbalanced / Broken Asterisks inside blockquotes or text
        # Pattern A: ***Text** (3 opened, 2 closed)
        if re.search(r"\*\*\*([^*\n]+?)\*\*(?!\*)", line):
            errors.append(f"Line {line_num}: Unbalanced bold/italic asterisks (***Text**).")
            line = re.sub(r"\*\*\*([^*\n]+?)\*\*(?!\*)", r"**\1**", line)
            fixes.append(f"Line {line_num}: Auto-balanced ***Text** -> **Text**")

        # Pattern B: ***Text* (3 opened, 1 closed)
        if re.search(r"\*\*\*([^*\n]+?)\*(?!\*)", line):
            errors.append(f"Line {line_num}: Unbalanced bold/italic asterisks (***Text*).")
            line = re.sub(r"\*\*\*([^*\n]+?)\*(?!\*)", r"*\1*", line)
            fixes.append(f"Line {line_num}: Auto-balanced ***Text* -> *Text*")

        # Pattern C: Broken trailing quote/asterisk combos (*."* or *"* or ."*)
        if re.search(r'\*\."\*|\*"\*|\."\*', line):
            errors.append(f"Line {line_num}: Corrupted quote/asterisk punctuation.")
            line = re.sub(r'\*\."\*|\."\*', '."', line)
            line = re.sub(r'\*"\*', '"', line)
            fixes.append(f"Line {line_num}: Cleaned trailing quote/asterisk delimiter.")

        # 2. Leaked Agent Scaffolding & Prompt Markers
        # Language markers: **EN.** or **AR.**
        if re.match(r"^\s*(?:\*{1,2})?(?:EN|AR)\.?(?:\*{1,2})?\s*$", line):
            errors.append(f"Line {line_num}: Leaked standalone language marker ('{line.strip()}').")
            fixes.append(f"Line {line_num}: Stripped standalone language marker.")
            continue  # Drop line completely

        if re.match(r"^\s*(?:\*{1,2})?(?:EN|AR)\.?(?:\*{1,2})?\s+", line):
            errors.append(f"Line {line_num}: Leaked inline language marker at start of line.")
            line = re.sub(r"^\s*(?:\*{1,2})?(?:EN|AR)\.?(?:\*{1,2})?\s+", "", line)
            fixes.append(f"Line {line_num}: Stripped leading language marker prefix.")

        # Internal scaffolding tags: [THIN], [VERIFY]
        if "[THIN]" in line:
            errors.append(f"Line {line_num}: Leaked internal benchmark tag '[THIN]'.")
            line = re.sub(r"\|\s*`?\[THIN\]`?\s*\|", "| Note: Primary Coverage |", line)
            line = re.sub(r"`?\[THIN\]`?", "*(In-depth note)*", line)
            fixes.append(f"Line {line_num}: Replaced '[THIN]' with academic note.")

        # Internal cross-file talk: (الملف 02), اربط هذا بالملف 02
        if re.search(r"بالملف\s+0?\d+|\(الملف\s+0?\d+[^)]*\)", line):
            errors.append(f"Line {line_num}: Leaked internal file scaffolding ('الملف XX').")
            line = re.sub(r"\(الملف\s+0?\d+[^)]*\)", "", line)
            line = re.sub(r"اربط هذا بالملف\s+0?\d+", "اربط هذا بالمفهوم السابق", line)
            line = re.sub(r"بالملف\s+0?\d+", "بالمفهوم السابق", line)
            fixes.append(f"Line {line_num}: Sanitized internal file reference to academic terminology.")

        # Backend build footers: File XX of YY. Built under...
        if re.search(r"^\s*\*?File\s+\d+\s+of\s+\d+\.\s*Built\s+\d{4}-\d{2}-\d{2}", line, re.IGNORECASE):
            errors.append(f"Line {line_num}: Leaked backend build ledger footer.")
            fixes.append(f"Line {line_num}: Stripped backend build footer.")
            continue  # Drop line

        # 3. Clean top H1 duplicate heading if present
        if not first_heading_seen and re.match(r"^#\s+(?:File\s+0?\d+\s+of\s+\d+|Unit\s+0?\d+)", line):
            first_heading_seen = True
            # Check if title has 'File 01 of 10'
            if "File" in line and "of" in line:
                errors.append(f"Line {line_num}: H1 heading contains 'File XX of YY' instead of 'Unit XX'.")
                line = re.sub(r"^#\s+File\s+0?(\d+)\s+of\s+\d+[\s:—–-]+", r"# Unit \1 — ", line)
                fixes.append(f"Line {line_num}: Renamed H1 heading to 'Unit XX'.")

        repaired_lines.append(line)

    # Global document checks
    if not has_retrieval_set:
        errors.append("Document lacks a '## Retrieval set' active recall section!")

    if auto_fix and fixes:
        file_path.write_text("\n".join(repaired_lines), encoding="utf-8")

    return len(errors), errors, fixes


def main():
    if len(sys.argv) < 2:
        print("Usage: python note_linter.py <path_to_note.md> [--fix] [--strict]")
        sys.exit(1)

    target_path = Path(sys.argv[1]).resolve()
    auto_fix = "--fix" in sys.argv
    strict_mode = "--strict" in sys.argv

    err_count, errors, fixes = lint_and_fix_markdown(target_path, auto_fix=auto_fix)

    print(f"\n=======================================================")
    print(f"Master Studio System 1 Pre-Flight Linter: {target_path.name}")
    print(f"=======================================================")

    if fixes:
        print(f"\n[+] Applied {len(fixes)} Automatic System 1 Repairs:")
        for f in fixes:
            print(f"    • {f}")

    if errors:
        print(f"\n[-] Detected {err_count} Invariant Violations:")
        for e in errors:
            print(f"    x {e}")
    else:
        print("\n[+] 100% CLEAN: All structural and typographical invariants passed.")

    if auto_fix and target_path.exists():
        # Re-lint after fix to check remaining unfixable issues
        remaining_errs, _, _ = lint_and_fix_markdown(target_path, auto_fix=False)
        if remaining_errs == 0:
            print("\n[+] POST-FIX STATUS: PRISTINE (0 remaining errors). Gate: PASSED.")
            sys.exit(0)
        else:
            print(f"\n[-] POST-FIX STATUS: {remaining_errs} manual issues remain (e.g. missing diagrams).")
            if strict_mode:
                sys.exit(1)
            sys.exit(0)

    if err_count > 0 and strict_mode:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
