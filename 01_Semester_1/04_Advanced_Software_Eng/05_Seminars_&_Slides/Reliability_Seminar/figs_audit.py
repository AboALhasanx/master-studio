#!/usr/bin/env python3
"""Audit: does every figure need to be redrawn, or does a usable original exist?"""
import re
import sys
from pathlib import Path

import pymupdf
import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = Path(__file__).resolve().parent
MD = BASE / "ch7_part1.md"
FIG = BASE / "figures"
SLIDES = BASE.parents[1] / "02_Raw_Materials" / "Aggarwal_Singh_Slides" / "chapter_7_software_reliability.pdf"

md = MD.read_text(encoding="utf-8")
refs = re.findall(r"!\[([^\]]+?)\|([\d.]+)\]", md)
caps = dict(re.findall(r"\*Figure (7\.\d+)\.", md) and
            [(m.group(1), m.group(0)) for m in re.finditer(r"\*Figure (7\.\d+)\..*?\*", md)])

print("=== CYCLE 1: inventory of sources (textual) ===")
print(f"{'fig':<8}{'file':<32}{'px':>10}{'in':>6}{'dpi':>6}{'slide':>7}{'slide_px':>10}{'eff_dpi':>8}")
rows = []
slide_map = {}
if SLIDES.exists():
    d = pymupdf.open(SLIDES)
    for i, page in enumerate(d):
        for m in re.findall(r"Fig\.?\s*7\.(\d+)", page.get_text()):
            imgs = page.get_images(full=True)
            if imgs and int(m) not in slide_map:
                slide_map[int(m)] = (i + 1, imgs[0][2], imgs[0][3])
else:
    print("  slides not found")

for fname, w in refs:
    n = int(re.search(r"fig7_(\d+)", fname).group(1))
    im = Image.open(FIG / fname)
    px_w, px_h = im.size
    dpi = px_w / float(w)
    sp = slide_map.get(n)
    if sp:
        eff = sp[1] / float(w)
        print(f"7.{n:<6}{fname:<32}{px_w:>5}x{px_h:<4}{w:>6}{dpi:>6.0f}{sp[0]:>7}{sp[1]:>5}x{sp[2]:<4}{eff:>8.0f}")
        rows.append((n, eff, dpi, sp[0]))
    else:
        print(f"7.{n:<6}{fname:<32}{px_w:>5}x{px_h:<4}{w:>6}{dpi:>6.0f}{'-':>7}{'-':>10}{'-':>8}")
        rows.append((n, None, dpi, None))

better = [r for r in rows if r[1] and r[1] > r[2]]
print("\n  originals that would beat the drawing (higher effective dpi):",
      [(f"7.{r[0]}", round(r[1]), round(r[2])) for r in better] or "NONE")

print("\n=== CYCLE 2: text consistency ===")
nums = [int(re.search(r"fig7_(\d+)", f).group(1)) for f, _ in refs]
print("  figure order sequential:", "PASS" if nums == sorted(nums) == list(range(1, len(nums) + 1)) else f"FAIL {nums}")
cap_lines = re.findall(r"^\*Figure 7\.(\d+)\..*\*$", md, re.M)
print("  captions found:", len(cap_lines), "unique:", len(set(cap_lines)))
dup = [c for c in set(cap_lines) if cap_lines.count(c) > 1]
print("  duplicate captions:", "PASS" if not dup else f"FAIL {dup}")
body = re.sub(r"!\[[^\]]+\]", "", md)
refs_in_text = set(re.findall(r"[Ff]ig(?:ure|\.)\s*7\.(\d+)", body))
missing = sorted(set(map(str, nums)) - refs_in_text, key=int)
print("  figures never cited in the text:", "PASS" if not missing else f"WARN {missing}")

print("\n=== CYCLE 3: per-figure visual metrics ===")
bad = []
for fname, w in refs:
    im = Image.open(FIG / fname).convert("RGB")
    a = np.asarray(im).astype(int)
    dev = np.max(np.abs(a - a.mean(axis=2, keepdims=True)), axis=2)
    colour = int((dev > 8).sum())
    ink = float((a.mean(axis=2) < 200).mean())
    if colour > 30:
        bad.append((fname, "colour"))
    if ink < 0.005:
        bad.append((fname, "blank"))
    if ink > 0.55:
        bad.append((fname, "too dark"))
print("  defects:", "PASS" if not bad else bad)

print("\n=== CYCLE 4: contact sheet ===")
cols, thumb_w = 4, 520
thumbs = []
for fname, w in refs:
    im = Image.open(FIG / fname).convert("RGB")
    r = thumb_w / im.width
    thumbs.append(im.resize((thumb_w, max(1, int(im.height * r))), Image.LANCZOS))
row_h = [max(t.height for t in thumbs[i:i + cols]) for i in range(0, len(thumbs), cols)]
sheet = Image.new("RGB", (cols * thumb_w, sum(row_h) + 20 * len(row_h)), "white")
y = 0
for r_i, h in enumerate(row_h):
    for c_i, t in enumerate(thumbs[r_i * cols:(r_i + 1) * cols]):
        sheet.paste(t, (c_i * thumb_w, y))
    y += h + 20
sheet.save(BASE / "_contact_sheet.png")
print("  saved _contact_sheet.png", sheet.size)

print("\n=== CYCLE 5: verdict ===")
if better:
    print("  REPLACE these with the original:", [f"7.{r[0]}" for r in better])
else:
    print("  PASS  no existing original reaches the resolution of the drawn version")
