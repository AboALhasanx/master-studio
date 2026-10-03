# -*- coding: utf-8 -*-
"""Extract raw text (paragraphs + table cells, in document order) from one or more .docx
files, preserving structure, so we can quote the doctor's English verbatim.
Usage: _extract_docx.py out.txt doc1.docx doc2.docx ..."""
import sys
from docx import Document

out = sys.argv[1]
paths = sys.argv[2:]
with open(out, "w", encoding="utf-8") as f:
    for p in paths:
        f.write("\n\n========== FILE: " + p.split("\\")[-1] + " ==========\n\n")
        doc = Document(p)
        # paragraphs
        for para in doc.paragraphs:
            t = para.text.strip()
            if t:
                style = para.style.name if para.style else ""
                prefix = f"[{style}] " if style else ""
                f.write(prefix + t + "\n")
        # tables
        for ti, table in enumerate(doc.tables):
            f.write(f"\n--- TABLE {ti+1} ---\n")
            for row in table.rows:
                cells = [c.text.strip().replace("\n", " | ") for c in row.cells]
                f.write(" || ".join(cells) + "\n")
        f.write("\n")
print("extracted", len(paths), "file(s) ->", out)
