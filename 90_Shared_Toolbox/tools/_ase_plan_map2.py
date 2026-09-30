from pypdf import PdfReader
from pathlib import Path
import re

books = {
    "Agarwal2010": Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\2010 SW_Engineering_and_Testing_An_Introduction_CS_Agarwal.pdf"),
    "Mall4": Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\fundamentals_of_software_engineering_fourth_edition_rajib_mall_1.pdf"),
}

CLUSTERS = {
    "cocomo": r"\bCOCOMO\b|constructive cost",
    "cocomo_sub": r"basic COCOMO|intermediate COCOMO|detailed COCOMO|basic model|intermediate model",
    "cocomo2": r"COCOMO II|cocomo ii",
    "app_early_post": r"application composition|early design|post.architecture",
    "putnam_rayleigh": r"Putnam|Norden|Rayleigh",
    "difficulty": r"difficulty metric|productivity index",
    "time_cost": r"trade.?off|time versus cost|cost versus time",
    "loc_fp": r"lines of code|\bLOC\b|function point",
    "static_models": r"single.variable|multivariable|static model",
    "risk_all": r"risk management|risk identification|risk mitigation|typical risk|software risk",
    "size_est": r"size estimation|size estimate|estimation of size",
    "cost_est": r"cost estimation|effort estimation|estimation model",
}

def ranges_of(pages):
    if not pages:
        return []
    out = []
    s = prev = pages[0]
    for x in pages[1:]:
        if x == prev + 1:
            prev = x
        else:
            out.append((s, prev))
            s = prev = x
    out.append((s, prev))
    return out

for name, path in books.items():
    r = PdfReader(str(path))
    texts = []
    for p in r.pages:
        try:
            texts.append((p.extract_text() or ""))
        except Exception:
            texts.append("")
    print("=" * 60, name, "pages", len(texts))
    for key, pat in CLUSTERS.items():
        pages = [i + 1 for i, t in enumerate(texts) if re.search(pat, t, re.I)]
        uniq = sorted(set(pages))
        print(f"-- {key} n={len(uniq)} ranges={ranges_of(uniq)[:12]}")
        shown = 0
        for i, t in enumerate(texts):
            if shown >= 2:
                break
            m = re.search(pat, t, re.I)
            if m:
                a = max(0, m.start() - 50)
                b = min(len(t), m.end() + 110)
                print(f"   p{i+1}: ...{t[a:b].replace(chr(10),' ')}...")
                shown += 1
