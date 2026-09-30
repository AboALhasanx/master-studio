from pypdf import PdfReader
from pathlib import Path
import re

books = {
    "Sommerville9": Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\Software-Engineering-9th-Edition-by-Ian-Sommerville.pdf"),
    "Pressman5": Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\Software Engineering by Roger Pressman.pdf"),
    "Agarwal2010": Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\2010 SW_Engineering_and_Testing_An_Introduction_CS_Agarwal.pdf"),
    "Mall4": Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\fundamentals_of_software_engineering_fourth_edition_rajib_mall_1.pdf"),
}

CLUSTERS = {
    "size_loc": r"lines of code|\bLOC\b|loc count",
    "function_count": r"function point|function count|function-point|fp count",
    "static_single": r"single.variable|single variable model|static.single",
    "static_multi": r"multivariable|multi.variable",
    "cocomo": r"\bCOCOMO\b|constructive cost",
    "cocomo_basic": r"basic COCOMO|basic model",
    "cocomo_inter": r"intermediate COCOMO|intermediate model",
    "cocomo_detailed": r"detailed COCOMO",
    "cocomo2": r"COCOMO II|cocomo ii",
    "app_composition": r"application composition",
    "early_design": r"early design model",
    "post_arch": r"post.architecture|post architecture",
    "putnam": r"\bPutnam\b",
    "rayleigh": r"Norden|Rayleigh",
    "difficulty_metric": r"difficulty metric|difficulty factor|\\bD\\b difficulty",
    "prod_vs_diff": r"productivity.*difficulty|difficulty.*productivity",
    "time_cost": r"time.*cost|cost.*time trade|trade.?off",
    "dev_subcycle": r"development sub.?cycle|sub.?cycle",
    "risk_what": r"\brisk\b is|risk is the|risk is a",
    "typical_risks": r"typical.*risk|software risks|risk category|project risks",
    "risk_mgmt": r"risk management|risk identification|risk assessment|risk mitigation|risk monitoring",
    "effort_estimation": r"effort estimation|cost estimation|estimate effort",
    "estimation_models": r"estimation model|cost model",
}

SAMPLES = {
    "cocomo": r"cocomo",
    "putnam": r"putnam|rayleigh|norden",
    "function_count": r"function point",
    "size_loc": r"lines of code",
    "risk_mgmt": r"risk management",
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
    if not path.exists():
        print("MISSING", name)
        continue
    r = PdfReader(str(path))
    texts = []
    for p in r.pages:
        try:
            texts.append((p.extract_text() or ""))
        except Exception:
            texts.append("")
    print("=" * 70)
    print(f"BOOK {name}  pages={len(texts)}")
    for key, pat in CLUSTERS.items():
        pages = []
        for i, t in enumerate(texts):
            if re.search(pat, t, re.I):
                pages.append(i + 1)
        uniq = sorted(set(pages))
        rg = ranges_of(uniq)
        print(f"\n-- {key} | n={len(uniq)} | ranges={rg[:15]}")
        # snippets
        shown = 0
        for i, t in enumerate(texts):
            if shown >= 2:
                break
            m = re.search(pat, t, re.I)
            if m:
                a = max(0, m.start() - 55)
                b = min(len(t), m.end() + 100)
                sn = t[a:b].replace("\n", " ")
                print(f"   p{i+1}: ...{sn}...")
                shown += 1
