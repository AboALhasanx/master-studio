"""Side-by-side: source slide figure vs our drawing, in 5 batches."""
import re
import sys
from pathlib import Path

import pymupdf
from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = Path(__file__).resolve().parent
FIG = BASE / "figures"
MD = BASE / "ch7_part1.md"
SLIDES = BASE.parents[1] / "02_Raw_Materials" / "Aggarwal_Singh_Slides" / "chapter_7_software_reliability.pdf"

refs = {int(re.search(r"fig7_(\d+)", f).group(1)): f
        for f, w in re.findall(r"!\[([^\]]+?)\|([\d.]+)\]", MD.read_text(encoding="utf-8"))}

slide_map = {}
d = pymupdf.open(SLIDES) if SLIDES.exists() else None
if d:
    for i, page in enumerate(d):
        for m in re.findall(r"Fig\.?\s*7\.(\d+)", page.get_text()):
            slide_map.setdefault(int(m), i)

nums = sorted(refs)
chunks = [nums[0:5], nums[5:10], nums[10:14], nums[14:18], nums[18:22]]

cell_w = 620
for b, group in enumerate(chunks, 1):
    rows = []
    for n in group:
        mine = Image.open(FIG / refs[n]).convert("RGB")
        mine = mine.resize((cell_w, max(1, int(mine.height * cell_w / mine.width))), Image.LANCZOS)
        src = None
        if d and n in slide_map:
            pix = d[slide_map[n]].get_pixmap(dpi=150)
            src = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            src = src.resize((cell_w, max(1, int(src.height * cell_w / src.width))), Image.LANCZOS)
        rows.append((n, src, mine))
    head, pad = 28, 26
    total_h = sum(max(r[1].height if r[1] else 0, r[2].height) + head + pad for r in rows) + 10
    sheet = Image.new("RGB", (cell_w * 2 + 40, total_h), "white")
    dr = ImageDraw.Draw(sheet)
    y = 5
    for n, src, mine in rows:
        dr.text((10, y), f"Fig 7.{n}   |   source (slide)          |          our drawing", fill="black")
        y += head
        if src:
            sheet.paste(src, (10, y))
        sheet.paste(mine, (cell_w + 30, y))
        y += max(src.height if src else 0, mine.height) + pad
    sheet.save(BASE / f"_cmp{b}.png")
    print(f"_cmp{b}.png", sheet.size, "figs", group)
