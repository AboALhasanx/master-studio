# -*- coding: utf-8 -*-
"""Post-process a Master Studio booklet PDF.

Two jobs, each optional:

  --map     Find the invisible @@key@@ anchors emitted by the booklet builder and
            write a JSON map of section key -> PDF page number. Used to fill the
            contents page with real page numbers (two-pass build).

  --stamp   Draw a page number at the foot of every page except the cover.

Usage:
    python booklet_postprocess.py --map   --pdf X.pdf --out pagemap.json
    python booklet_postprocess.py --stamp --pdf X.pdf --out X_numbered.pdf
"""
import argparse
import json
import re
import sys
from pathlib import Path

import pymupdf


def find_anchors(pdf, skip_first=1):
    """Return {key: page_number} for every @@key@@ anchor in the document."""
    doc = pymupdf.open(pdf)
    found = {}
    pat = re.compile(r"@@([^@]+)@@")
    for i in range(skip_first, doc.page_count):
        for key in pat.findall(doc[i].get_text()):
            found.setdefault(key, i + 1)
    return found, doc.page_count


def stamp(pdf, out, start=1, skip_first=1, label="Week 02 · Cybersecurity Risks and Threats"):
    """Write a page number at the foot of each page. Cover is left unnumbered."""
    doc = pymupdf.open(pdf)
    for i in range(skip_first, doc.page_count):
        page = doc[i]
        r = page.rect
        txt = f"{label}   ·   {i + 1 - skip_first + start}"
        page.insert_text(
            pymupdf.Point(r.width / 2, r.height - 22),
            txt,
            fontname="helv",
            fontsize=7.5,
            color=(0.58, 0.62, 0.66),
            render_mode=0,
        )
    doc.save(out, garbage=4, deflate=True)
    return doc.page_count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--map", action="store_true")
    ap.add_argument("--stamp", action="store_true")
    ap.add_argument("--skip-first", type=int, default=1)
    a = ap.parse_args()

    if a.map:
        found, total = find_anchors(a.pdf, a.skip_first)
        Path(a.out).write_text(json.dumps(found, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"anchors found: {len(found)}  (document has {total} pages)")
        print(json.dumps(found, ensure_ascii=False))
    if a.stamp:
        n = stamp(a.pdf, a.out, skip_first=a.skip_first)
        print(f"stamped {n - a.skip_first} pages -> {a.out}")


if __name__ == "__main__":
    sys.exit(main())
