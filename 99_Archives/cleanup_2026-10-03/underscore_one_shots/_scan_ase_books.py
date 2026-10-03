from pypdf import PdfReader
from pathlib import Path

paths = list(Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng").rglob("*.pdf"))
paths += list(Path(r"C:\Users\gokoq\Downloads\Telegram Desktop").glob("*Ali*"))
seen = set()
for p in paths:
    key = (p.name, p.stat().st_size)
    if key in seen:
        continue
    seen.add(key)
    if p.stat().st_size < 100000 and "Fahem" not in p.name and "Fahim" not in p.name:
        continue
    if "chapter_" in p.name or "SE_TUTORIAL" in p.name or "mrcet" in p.name:
        continue
    try:
        r = PdfReader(str(p))
        meta = r.metadata or {}
        t = (r.pages[0].extract_text() or "")[:120].replace("\n", " ")
        t2 = (r.pages[2].extract_text() or "")[:120].replace("\n", " ") if len(r.pages) > 2 else ""
        print("=" * 60)
        print(p.name)
        print("  path:", p)
        print("  size:", p.stat().st_size, "pages:", len(r.pages))
        print("  meta:", dict(meta) if meta else None)
        print("  p1:", t)
        print("  p3:", t2)
    except Exception as e:
        print("=" * 60)
        print(p.name, "ERR", type(e).__name__, e)
