# -*- coding: utf-8 -*-
"""Scan a PDF for leaked markup / entities and confirm diagram presence via pixel color sampling.
Read-only diagnostic. Run with the managed venv python (has pymupdf)."""
import sys, os

PDF = sys.argv[1] if len(sys.argv) > 1 else None
PNGDIR = sys.argv[2] if len(sys.argv) > 2 else None
if not PDF:
    print("usage: _scan_pdf_leaks.py <pdf> [pngdir]"); sys.exit(2)

try:
    import fitz  # PyMuPDF
except ImportError:
    print("NEED_PYMUPDF"); sys.exit(3)

LEAK_TOKENS = ["&amp;", "&lt;", "&gt;", "&quot;", "&nbsp;", "```", "<svg", "</svg>",
               "]]>]", "{{", "}}", "data:image/svg", "<text", "<rect", "\\n", "NoneType"]

doc = fitz.open(PDF)
print(f"PAGES={doc.page_count} FILE={os.path.basename(PDF)}")
leak_hits = 0
for pno in range(doc.page_count):
    page = doc[pno]
    txt = page.get_text("text")
    hits = [t for t in LEAK_TOKENS if t in txt]
    if hits:
        leak_hits += 1
        print(f"  [LEAK] p{pno+1}: {hits}")
    pix = page.get_pixmap(dpi=110)
    if PNGDIR:
        os.makedirs(PNGDIR, exist_ok=True)
        png = os.path.join(PNGDIR, f"p{pno+1:02d}.png")
        pix.save(png)
    blu = red = org = pur = grn = 0
    srgb = pix.samples
    w, h = pix.width, pix.height
    n = pix.n
    step = max(1, (w * h) // 5000)
    for i in range(0, w * h, step):
        r = srgb[i * n]; g = srgb[i * n + 1]; b = srgb[i * n + 2]
        if b > 140 and r < 130 and g < 160: blu += 1
        if r > 150 and g < 120 and b < 120: red += 1
        if r > 170 and 80 < g < 190 and b < 120: org += 1
        if r > 90 and b > 150 and g < 120: pur += 1
        if g > 120 and r < 140 and b < 160: grn += 1
    print(f"  p{pno+1:02d} blu={blu} red={red} org={org} pur={pur} grn={grn}")
print("LEAK_TOTAL=", leak_hits)
