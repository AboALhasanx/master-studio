from docx import Document
from pathlib import Path
import re

base = Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\03_Data_Mining\02_Raw_Materials")
files = [
    base / "Week 02 - Basic Data Types in Data Mining (v2).docx",
    base / "Week 02 - Basic Data Types in Data Mining and ML.docx",
    base / "Week 03 - Feature Extraction and Portability.docx",
    base / "Week4_Feature_Selection.docx",
]

for path in files:
    if not path.exists():
        print("MISSING", path.name)
        continue
    d = Document(str(path))
    paras = [p.text.strip() for p in d.paragraphs if p.text.strip()]
    print("=" * 70)
    print(f"FILE: {path.name}")
    print(f"paras={len(d.paragraphs)} nonempty={len(paras)} tables={len(d.tables)}")
    # headings + first lines
    heads = [(p.style.name, p.text.strip()) for p in d.paragraphs if p.text.strip() and p.style and 'Heading' in p.style.name]
    print(f"HEADINGS ({len(heads)}):")
    for s, t in heads[:40]:
        print(f"  [{s}] {t[:100]}")
    # style distribution
    styles = {}
    for p in d.paragraphs:
        if p.text.strip():
            sn = p.style.name if p.style else "?"
            styles[sn] = styles.get(sn, 0) + 1
    print("STYLES:", styles)
    # word count
    words = sum(len(p.split()) for p in paras)
    print(f"approx_words={words}")
    # math
    xml_all = "\n".join(p._p.xml for p in d.paragraphs)
    omml = len(re.findall(r"<m:oMath", xml_all))
    print(f"omml_blocks={omml}")
    # first 15 nonempty
    print("OPENING:")
    for t in paras[:12]:
        print("  ", t[:140])
    print()
