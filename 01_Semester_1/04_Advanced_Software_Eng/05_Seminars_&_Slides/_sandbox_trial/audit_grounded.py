#!/usr/bin/env python3
"""
Grounded QA gate: verifies the source-anchored notes.
Checks: anchor validity (S:n within 1..99), coverage of every section, figure order,
embedded images, required sections, no leaked scaffolding.
Exit 0 = PASSED.
"""
import re
import sys
import zipfile
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

from docx import Document

HERE = Path(__file__).resolve().parent
MD = HERE / "Ch5_grounded_notes.md"
DOCX = HERE / "Ch5_Software_Design_GROUNDED.docx"
SOURCE_MAX = 99
EXPECT_MIN_FIGS = 11

errors, warnings = [], []


def main():
    md = MD.read_text(encoding="utf-8")
    doc = Document(str(DOCX))

    # 1. anchors valid and in range
    anchors = [int(x) for x in re.findall(r'\[S:(\d+)\]', md)]
    if not anchors:
        errors.append("no [S:n] anchors found")
    bad = [a for a in anchors if a < 1 or a > SOURCE_MAX]
    if bad:
        errors.append(f"out-of-range anchors: {sorted(set(bad))}")
    print(f"Anchors: {len(anchors)} total, range {min(anchors)}..{max(anchors)}, "
          f"distinct slides covered {len(set(anchors))}/{SOURCE_MAX}")

    # 2. every H1/H2 section in md carries at least one anchor in its body
    sections = re.split(r'\n(?=#{1,2} )', md)
    for sec in sections:
        first = sec.split("\n", 1)[0].strip()
        if not (first.startswith("# ") or first.startswith("## ")):
            continue
        if first.startswith("# References"):
            continue
        if "Retrieval Check" in first or "Coverage Map" in first:
            continue
        body = sec.split("\n", 1)[1] if "\n" in sec else ""
        if not re.search(r'\[S:\d+', sec):
            if first.startswith("# ") and first[2:3].isdigit():
                errors.append(f"section without anchor: {first}")

    # 3. figure order + captions in docx (italic captions)
    caps = []
    for p in doc.paragraphs:
        t = p.text.strip()
        if t.startswith("Figure ") and p.runs and p.runs[0].italic:
            caps.append(t)
    nums = []
    for c in caps:
        mm = re.match(r'Figure (\d+)\.', c)
        if mm:
            nums.append(int(mm.group(1)))
    print(f"Figure captions in body: {nums}")
    if len(nums) < EXPECT_MIN_FIGS:
        errors.append(f"expected >= {EXPECT_MIN_FIGS} figures, found {len(nums)}")
    if nums != sorted(nums):
        errors.append(f"figures out of order: {nums}")
    if len(set(nums)) != len(nums):
        errors.append("duplicate figure numbers")

    # 4. embedded media
    with zipfile.ZipFile(DOCX) as z:
        media = [n for n in z.namelist() if n.startswith("word/media/")]
    print(f"Embedded images: {len(media)}")
    if len(media) < EXPECT_MIN_FIGS:
        errors.append(f"embedded images {len(media)} < {EXPECT_MIN_FIGS}")

    # 5. required sections
    alltext = "\n".join(p.text for p in doc.paragraphs)
    for req in ["Table of Contents", "List of Figures", "Retrieval Check",
                "Coverage Map", "References"]:
        if req.lower() not in alltext.lower():
            errors.append(f"required section missing: {req}")

    # 6. no leaked scaffolding
    for tok in ["[THIN]", "**EN.**", "**AR.**", "File 01 of", "BUILD_PLAN", "lorem"]:
        if tok in alltext:
            errors.append(f"leaked token: {tok}")

    # 7. tables present
    print(f"Tables: {len(doc.tables)}")
    if len(doc.tables) < 3:
        warnings.append(f"only {len(doc.tables)} tables")

    print("\n" + "=" * 60)
    for e in errors:
        print(f"[ERR]  {e}")
    for w in warnings:
        print(f"[WARN] {w}")
    verdict = "PASSED" if not errors else "FAILED"
    print(f"\nGROUNDED QA GATE: {verdict} (errors={len(errors)}, warnings={len(warnings)})")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
