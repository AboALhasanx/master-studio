#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Map the red strikethroughs in the annotated Week-3 PDF to the text they cover."""
import pymupdf

PDF = r"C:\Users\gokoq\Downloads\Telegram Desktop\W02_Risks.pdf"
doc = pymupdf.open(PDF)

for pno, page in enumerate(doc, 1):
    # collect red vector strokes
    reds = []
    for d in page.get_drawings():
        col = d.get("color") or d.get("fill")
        if not col:
            continue
        r, g, b = col[:3]
        if r > 0.6 and g < 0.45 and b < 0.45:
            reds.append(d["rect"])
    if not reds:
        continue

    # merge red rects into bands, then ask which text sits inside them
    covered = []
    words = page.get_text("words")  # x0,y0,x1,y1,word,block,line,word_no
    for x0, y0, x1, y1, w, *_ in words:
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        for r in reds:
            if r.x0 - 2 <= cx <= r.x1 + 2 and r.y0 - 2 <= cy <= r.y1 + 2:
                covered.append((round(y0, 1), round(x0, 1), w))
                break

    if not covered:
        continue
    # rebuild lines in reading order
    covered.sort()
    lines, cur, last_y = [], [], None
    for y, x, w in covered:
        if last_y is not None and abs(y - last_y) > 4:
            lines.append(" ".join(cur))
            cur = []
        cur.append(w)
        last_y = y
    if cur:
        lines.append(" ".join(cur))

    print("### page %d — %d red stroke(s)" % (pno, len(reds)))
    for ln in lines:
        print("   X ", ln[:160])
    print()
