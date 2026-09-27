from docx import Document
from docx.oxml.ns import qn
import re

path = r"C:\Users\gokoq\Master-Studio\01_Semester_1\03_Data_Mining\02_Raw_Materials\Week4_Feature_Selection.docx"
d = Document(path)

# Extract OMML math (m:oMath) as readable approximation
maths = []
for i, p in enumerate(d.paragraphs):
    xml = p._p.xml
    if "oMath" in xml or "m:oMath" in xml:
        # pull m:t text nodes
        texts = re.findall(r"<m:t[^>]*>([^<]*)</m:t>", xml)
        joined = "".join(texts).strip()
        if joined:
            maths.append((i, p.text.strip()[:60], joined))

print("OMML equations found:", len(maths))
for i, ctx, eq in maths:
    print(f"[para {i}] ctx={ctx!r}")
    print(f"  EQ: {eq}")
    print()
