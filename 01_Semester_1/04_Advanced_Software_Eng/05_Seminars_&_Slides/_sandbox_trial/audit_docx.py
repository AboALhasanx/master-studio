#!/usr/bin/env python3
"""
Sandbox trial -- structural QA gate for the generated DOCX (read-back audit).
Mirrors the vault's *_linter.py contract: prints findings, exits non-zero on failure.
"""
import sys
import zipfile
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn

HERE = Path(__file__).resolve().parent
DOCX = HERE / "Ch5_Software_Design_Study_Notes.docx"
FIG = HERE / "figures"

EXPECTED_FIGURES = 10
errors, warnings, notes = [], [], []


def add(kind, msg):
    (errors if kind == "ERR" else warnings if kind == "WARN" else notes).append(msg)


def main():
    if not DOCX.exists():
        print(f"[ERR] missing output: {DOCX}")
        return 2

    doc = Document(str(DOCX))

    # --- 1. headings hierarchy
    heads = [(p.style.name, p.text.strip())
             for p in doc.paragraphs
             if p.style.name.startswith("Heading") and p.text.strip()]
    levels = [int(h[0].split()[-1]) for h in heads]
    print(f"Heading count: {len(heads)}  |  levels: {levels}")
    prev = 0
    for (style, text), lvl in zip(heads, levels):
        if prev and lvl > prev + 1:
            add("ERR", f"heading jump {prev}->{lvl}: '{text}'")
        prev = lvl
    if not heads:
        add("ERR", "no headings found")

    # --- 2. images embedded in the package
    with zipfile.ZipFile(DOCX) as z:
        media = [n for n in z.namelist() if n.startswith("word/media/")]
    print(f"Embedded media files: {len(media)}")
    if len(media) != EXPECTED_FIGURES:
        add("ERR", f"expected {EXPECTED_FIGURES} images, found {len(media)}")

    # --- 3. caption integrity: real captions are italic; List-of-Figures entries are not
    caps = []
    for p in doc.paragraphs:
        t = p.text.strip()
        if t.startswith("Figure ") and "." in t[:12] and p.runs and p.runs[0].italic:
            caps.append(t)
    cap_nums = []
    for c in caps:
        try:
            cap_nums.append(int(c.split()[1].rstrip(".")))
        except (IndexError, ValueError):
            add("WARN", f"caption not parseable: {c[:50]}")
    uniq = sorted(set(cap_nums))
    print(f"Captions: {len(caps)}  numbers: {uniq}")
    for n in range(1, EXPECTED_FIGURES + 1):
        if n not in uniq:
            add("ERR", f"missing caption for Figure {n}")
    if len(cap_nums) != len(uniq):
        add("WARN", "duplicate figure caption numbers detected")
    if cap_nums != sorted(cap_nums):
        add("ERR", f"figures out of order in document: {cap_nums}")

    # --- 4. every figure file actually exists and is referenced
    for fn, _, _ in __import__("build_docx").FIGURES:
        if not (FIG / fn).exists():
            add("ERR", f"figure file missing on disk: {fn}")

    # --- 5. tables
    print(f"Tables: {len(doc.tables)}")
    for i, t in enumerate(doc.tables):
        if len(t.rows) < 2:
            add("WARN", f"table {i} has < 2 rows")
        if len(t.columns) < 2:
            add("WARN", f"table {i} has < 2 columns")

    # --- 6. required sections present
    text_all = "\n".join(p.text for p in doc.paragraphs)
    for required in ["Table of Contents", "List of Figures", "References", "Summary"]:
        if required.lower() not in text_all.lower():
            add("ERR", f"required section missing: {required}")

    # --- 7. no leaked scaffolding tokens
    for token in ["[THIN]", "**EN.**", "**AR.**", "File 01 of", "BUILD_PLAN"]:
        if token in text_all:
            add("ERR", f"leaked scaffolding token: {token}")

    # --- report
    print("\n" + "=" * 60)
    for e in errors:
        print(f"[ERR]  {e}")
    for w in warnings:
        print(f"[WARN] {w}")
    for n in notes:
        print(f"[INFO] {n}")
    verdict = "PASSED" if not errors else "FAILED"
    print(f"\nQA GATE: {verdict}  (errors={len(errors)}, warnings={len(warnings)})")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
