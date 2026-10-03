from pypdf import PdfReader
from pathlib import Path
import re

base = Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\Aggarwal_Singh_SE_PPT_Chapters\exam_papers\planning_refs")

PATS = {
    "difficulty": r"difficulty",
    "subcycle": r"sub.?cycle|development cycle",
    "rayleigh": r"rayleigh",
    "putnam": r"putnam|software equation",
    "app_comp": r"application composition",
    "early": r"early design",
    "post": r"post.architecture",
    "static": r"static model|single variable|multivariable",
    "CK": r"\bCk\b|technology constant|SLOC",
    "productivity": r"productivity",
}

for p in sorted(base.glob("*.pdf")):
    try:
        r = PdfReader(str(p))
    except Exception as e:
        print("ERR", p.name, e)
        continue
    texts = []
    for pg in r.pages:
        try:
            texts.append(pg.extract_text() or "")
        except Exception:
            texts.append("")
    print("=" * 60)
    print(p.name, "pages", len(texts))
    for key, pat in PATS.items():
        pages = [i + 1 for i, t in enumerate(texts) if re.search(pat, t, re.I)]
        if not pages:
            continue
        print(f"  {key}: pages={pages[:12]}")
        # one snippet from first hit
        for i, t in enumerate(texts):
            m = re.search(pat, t, re.I)
            if m:
                a = max(0, m.start() - 40)
                b = min(len(t), m.end() + 120)
                print(f"     p{i+1}: {t[a:b].replace(chr(10),' ')[:180]}")
                break
