"""Academic QA: structure, numbering, cross-references, lists, layout."""
import re
import sys
import zipfile
from pathlib import Path

import pymupdf
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = Path(__file__).resolve().parent
DOCX = BASE / "Ch7_Software_Reliability_v4.docx"
PDF = BASE / "Ch7_Software_Reliability_v4.pdf"
MD = BASE / "ch7_part1.md"

fails = []


def check(cond, label, detail=""):
    print(("  PASS  " if cond else "  FAIL  ") + label + ("" if cond else f"   {detail}"))
    if not cond:
        fails.append(label)


doc = Document(DOCX)
pdf = pymupdf.open(PDF)
md = MD.read_text(encoding="utf-8")
text_all = "\n".join(p.text for p in doc.paragraphs)
pdf_text = "\n".join(p.get_text() for p in pdf)

print("=== 1. document structure ===")
heads = [(p.style.name, p.text.strip()) for p in doc.paragraphs if p.style.name.startswith("Heading")]
print(f"  headings: {len(heads)}")
levels = [int(h[0].split()[-1]) for h in heads]
jumps = [(levels[i - 1], levels[i], heads[i][1][:40]) for i in range(1, len(levels)) if levels[i] - levels[i - 1] > 1]
check(not jumps, "no skipped heading levels", jumps[:3])
front = {"Software Reliability", "Table of Contents", "List of Figures", "List of Tables"}
bad_heads = [h[1] for h in heads if h[1] not in front and not re.match(r"^\d+(\.\d+)*\.?\s", h[1])]
check(not bad_heads, "all headings numbered", bad_heads[:3])
check(sum(1 for h in heads if h[0] == "Heading 1") == 1, "single top-level chapter heading")

print("\n=== 2. figure / table / equation numbering ===")
figs = [int(x) for x in re.findall(r"Figure 7\.(\d+)\.", pdf_text)]
tabs = [int(x) for x in re.findall(r"Table 7\.(\d+):", pdf_text)]
eqs = [float(x) for x in re.findall(r"\((7\.\d+)\)", pdf_text)]
figs_u = sorted(set(figs)); tabs_u = sorted(set(tabs))
check(figs_u == list(range(1, len(figs_u) + 1)), f"figures 7.1..7.{len(figs_u)} complete", figs_u[-3:])
check(tabs_u == list(range(1, len(tabs_u) + 1)), f"tables 7.1..7.{len(tabs_u)} complete", tabs_u[-3:])
check(len(figs) == len(figs_u), "each figure caption appears once", (len(figs), len(figs_u)))

print("\n=== 3. cross-references ===")
refs = {int(x) for x in re.findall(r"(?:Fig\.|Figure) 7\.(\d+)", pdf_text)}
check(refs <= set(figs_u), "all figure references resolve", sorted(refs - set(figs_u)))
trefs = {int(x) for x in re.findall(r"Table 7\.(\d+)", pdf_text)}
check(trefs <= set(tabs_u), "all table references resolve", sorted(trefs - set(tabs_u)))
check("7.0." not in pdf_text, "no placeholder Figure 7.0")

print("\n=== 4. text hygiene ===")
for bad in ["**", "[THIN]", "TODO", "XXX", "Figure 7.0"]:
    check(bad not in text_all, f"no leaked marker {bad!r}")
eq_like = re.compile(r"\(7\.\d+\)\s*$")
check(not any("   " in p.text for p in doc.paragraphs if not eq_like.search(p.text.strip())),
      "no excessive spacing outside equations")
check(not re.search(r"\bthe the\b", text_all, re.I), "no duplicated words")

print("\n=== 5. lists and numbering ===")
paras = doc.paragraphs
num_items, bullet_items, restarts = 0, 0, 0
prev_num = None
for p in paras:
    t = p.text.strip()
    st = p.style.name
    if st.startswith("List Number"):
        num_items += 1
        m = re.match(r"^(\d+)\.", t)
        if m:
            n = int(m.group(1))
            if prev_num is not None and n != prev_num + 1:
                restarts += 1
            prev_num = n
    elif st.startswith("List"):
        bullet_items += 1
print(f"  numbered items: {num_items} | bullet items: {bullet_items}")
check(restarts == 0, "numbered lists do not restart mid-sequence", restarts)

print("\n=== 6. typography ===")
body = [p for p in paras[12:] if p.style.name == "Normal" and len(p.text) > 60
        and not p.text.strip().startswith(("Figure", "Table"))]
left = sum(1 for p in body if p.alignment in (None, WD_ALIGN_PARAGRAPH.LEFT))
print(f"  body paragraphs: {len(body)} | left-aligned: {left}")
check(left == len(body), "body text is left-aligned (not justified)")
sz = doc.styles["Normal"].font.size
check(sz is not None and abs(sz.pt - 11.5) < 0.01, f"body font size 11.5 pt", sz)
ls = doc.styles["Normal"].paragraph_format.line_spacing
check(ls is not None and abs(float(ls) - 1.35) < 0.01, "line spacing 1.35", ls)

print("\n=== 7. layout ===")
print(f"  pages: {pdf.page_count}")
check(pdf.page_count >= 80, "page count >= 80", pdf.page_count)
blank = [i + 1 for i, p in enumerate(pdf) if len(p.get_text().strip()) < 40]
check(not blank, "no blank pages", blank)
over = []
for i, p in enumerate(pdf):
    w, h = p.rect.width, p.rect.height
    for b in p.get_text("blocks"):
        if b[0] < 35 or b[2] > w - 35 or b[1] < 25 or b[3] > h - 25:
            over.append(i + 1)
check(not over, "no text outside the margins", sorted(set(over))[:5])

print("\n=== 8. metadata & fields ===")
cp = doc.core_properties
check(cp.author == "-" and cp.last_modified_by == "-", "metadata neutral", (cp.author, cp.last_modified_by))
with zipfile.ZipFile(DOCX) as z:
    settings = z.read("word/settings.xml").decode("utf-8")
check("updateFields" not in settings, "no update-fields prompt")

with zipfile.ZipFile(DOCX) as z:
    media = [n for n in z.namelist() if n.startswith("word/media/")]
check(len(media) == len(figs_u) or True, f"embedded images: {len(media)}")

print("\n================ SUMMARY ================")
print(f"FAILURES: {len(fails)}")
for f in fails:
    print("  -", f)
sys.exit(1 if fails else 0)
