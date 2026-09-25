# -*- coding: utf-8 -*-
"""Full geometry audit of ALL 16 DM diagrams. Flags out-of-bounds rects and
small-rect overlaps (the two defect classes that bit us). Evidence, not claims."""
import glob, xml.etree.ElementTree as ET

NS = "{http://www.w3.org/2000/svg}"
DIR = "C:/Users/gokoq/Master-Studio/01_Semester_1/03_Data_Mining/06_Diagrams_&_Mindmaps/03_Data_Mining"

def parse(p):
    t = ET.parse(p); r = t.getroot()
    rects, texts = [], []
    for el in r.iter():
        tag = el.tag.replace(NS, "")
        if tag == "rect":
            rects.append((float(el.get("x")), float(el.get("y")),
                          float(el.get("width")), float(el.get("height"))))
        elif tag == "text":
            texts.append((float(el.get("x")), float(el.get("y")), el.text))
    return rects, texts, float(r.get("viewBox").split()[2])

def overlap(a, b):
    ax, ay, aw, ah = a; bx, by, bw, bh = b
    return not (ax+aw <= bx or bx+bw <= ax or ay+ah <= by or by+bh <= ay)

problems = 0
for f in sorted(glob.glob(f"{DIR}/*.svg")):
    rects, texts, vbw = parse(f)
    oob = [r for r in rects if r[0] < -0.5 or r[1] < -0.5 or r[0]+r[2] > vbw+0.5]
    bg = [(x,y,w,h) for (x,y,w,h) in rects if w > 200 and h > 100]
    others = [(x,y,w,h) for (x,y,w,h) in rects if (x,y,w,h) not in bg]
    ov = 0
    for i in range(len(others)):
        for j in range(i+1, len(others)):
            if overlap(others[i], others[j]):
                ov += 1
    status = "OK"
    if oob or ov:
        status = f"DEFECT oob={len(oob)} overlap={ov}"
        problems += 1
        for r in oob: print(f"    OOB {r}")
        for i in range(len(others)):
            for j in range(i+1, len(others)):
                if overlap(others[i], others[j]):
                    print(f"    OVERLAP {others[i]} <> {others[j]}")
    print(f"  {f.split(chr(92))[-1]:24} rects={len(rects):2} texts={len(texts):2} vbw={vbw:5.0f} -> {status}")
print(f"\nTOTAL DEFECTS = {problems}")
