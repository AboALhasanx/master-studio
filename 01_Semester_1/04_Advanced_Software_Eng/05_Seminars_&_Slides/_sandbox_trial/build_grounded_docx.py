#!/usr/bin/env python3
"""
Build the grounded Chapter-5 Word document from Ch5_grounded_notes.md.
Grounded pipeline: source-anchored markdown -> docx with figures/tables/TOC.
Clean academic English (Times New Roman), numbered headings, editable.
"""
import re
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
MD = HERE / "Ch5_grounded_notes.md"
OUT = HERE / "Ch5_Software_Design_GROUNDED.docx"

FONT = "Times New Roman"
NAVY = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x44, 0x44, 0x44)
ANCHOR = RGBColor(0x8A, 0x2B, 0x2B)


def set_base(doc):
    n = doc.styles["Normal"]
    n.font.name = FONT
    n.font.size = Pt(10.5)
    n.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
    n.paragraph_format.space_after = Pt(6)
    n.paragraph_format.line_spacing = 1.13
    rpr = n.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), FONT)


def add_field(p, instr):
    r = p.add_run()
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin")
    i = OxmlElement("w:instrText"); i.set(qn("xml:space"), "preserve"); i.text = instr
    s = OxmlElement("w:fldChar"); s.set(qn("w:fldCharType"), "separate")
    t = OxmlElement("w:t"); t.text = "Update field (right-click > Update Field / F9)"
    e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end")
    for el in (b, i, s, t, e):
        r._r.append(el)


def runs_with_anchor(p, text, base_size=10.5, italic=False):
    """Write text, rendering [S:n] anchors in red italic and **bold** / *italic*."""
    # split on bold, italic, and anchors
    tokens = re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*|\[S:[^\]]+\])', text)
    for tok in tokens:
        if not tok:
            continue
        if re.fullmatch(r'\[S:[^\]]+\]', tok):
            r = p.add_run(tok)
            r.font.color.rgb = ANCHOR
            r.italic = True
            r.font.size = Pt(base_size - 0.5)
            r.font.name = FONT
        elif tok.startswith("**") and tok.endswith("**") and len(tok) >= 4:
            r = p.add_run(tok[2:-2]); r.bold = True
            r.font.size = Pt(base_size); r.font.name = FONT; r.italic = italic
        elif tok.startswith("*") and tok.endswith("*") and len(tok) >= 2:
            r = p.add_run(tok[1:-1]); r.italic = True
            r.font.size = Pt(base_size); r.font.name = FONT
        else:
            r = p.add_run(tok)
            r.font.size = Pt(base_size); r.font.name = FONT; r.italic = italic
    return p


def heading(doc, text, level):
    h = doc.add_heading(level=level)
    runs_with_anchor(h, text, base_size=15 if level == 1 else 12.5 if level == 2 else 11)
    for r in h.runs:
        r.font.color.rgb = NAVY
        r.bold = True
        r.font.name = FONT
    h.paragraph_format.space_before = Pt(13 if level == 1 else 9)
    h.paragraph_format.space_after = Pt(5)
    return h


def add_image(doc, fname, width_in, caption):
    path = FIG / fname
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(2)
    if path.exists():
        p.add_run().add_picture(str(path), width=Inches(width_in))
    else:
        runs_with_anchor(p, f"[missing figure: {fname}]")
    cap = doc.add_paragraph(); cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_after = Pt(11)
    runs_with_anchor(cap, caption, base_size=9, italic=True)
    for r in cap.runs:
        r.font.color.rgb = GREY
    return caption


def add_table(doc, rows):
    if not rows:
        return
    ncol = max(len(r) for r in rows)
    t = doc.add_table(rows=0, cols=ncol)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(rows):
        cells = t.add_row().cells
        for c in range(ncol):
            val = row[c] if c < len(row) else ""
            cell = cells[c]
            cell.text = ""
            para = cell.paragraphs[0]
            para.paragraph_format.space_after = Pt(1)
            runs_with_anchor(para, val, base_size=8.8)
            if i == 0:
                shade = OxmlElement("w:shd"); shade.set(qn("w:fill"), "1F3A5F")
                cell._element.get_or_add_tcPr().append(shade)
                for r in para.runs:
                    r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)


def parse_md(doc, md_path=None):
    lines = (md_path or MD).read_text(encoding="utf-8").split("\n")
    fig_no = 0
    i = 0
    pending_caption = None
    toc_added = False
    figures = []
    while i < len(lines):
        line = lines[i].rstrip()
        s = line.strip()
        i += 1

        # figure line: ![file|width]
        m = re.match(r'^!\[(.+?)\|([\d.]+)\]\s*$', s)
        if m:
            fname, w = m.group(1), float(m.group(2))
            # next non-empty line is the caption if it starts with *Figure
            cap = ""
            if i < len(lines) and lines[i].strip().startswith("*Figure"):
                cap = lines[i].strip().strip("*")
                i += 1
            fig_no += 1
            add_image(doc, fname, w, cap)
            figures.append(cap)
            continue

        if not s:
            continue
        if s == "---":
            continue

        if s.startswith("# "):
            heading(doc, s[2:].strip(), 1)
        elif s.startswith("## "):
            heading(doc, s[3:].strip(), 2)
        elif s.startswith("### "):
            heading(doc, s[4:].strip(), 3)
        elif s.startswith("> "):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.35)
            runs_with_anchor(p, s[2:], base_size=9.5, italic=True)
            for r in p.runs:
                r.font.color.rgb = GREY
        elif s.startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.space_after = Pt(2)
            runs_with_anchor(p, s[2:])
        elif re.match(r'^\d+\.\s', s):
            p = doc.add_paragraph(style="List Number")
            p.paragraph_format.space_after = Pt(2)
            runs_with_anchor(p, re.sub(r'^\d+\.\s', '', s))
        elif s.startswith("|") and s.endswith("|"):
            # collect table block
            block = [s]
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i].strip())
                i += 1
            rows = []
            for br in block:
                if re.match(r'^\|[\s\-:|]+\|$', br):
                    continue
                cells = [c.strip() for c in br.split("|")[1:-1]]
                rows.append(cells)
            add_table(doc, rows)
        else:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_after = Pt(7)
            runs_with_anchor(p, s)
    return figures


def cover_and_front(doc, figures):
    for _ in range(3):
        doc.add_paragraph()
    t = doc.add_paragraph(); t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run("Software Design")
    r.font.name = FONT; r.font.size = Pt(30); r.bold = True; r.font.color.rgb = NAVY
    st = doc.add_paragraph(); st.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = st.add_run("Chapter 5 — Source-Grounded Study Notes")
    r.font.name = FONT; r.font.size = Pt(14); r.font.color.rgb = GREY
    doc.add_paragraph()
    meta = [
        ("Course", "Advanced Software Engineering (CS603), 3 Credit Hours"),
        ("Instructor", "Asst. Prof. Dr. Ali Fahim Ni'ma"),
        ("Institution", "College of Computer Science & Information Technology, University of Wasit"),
        ("Source", "Aggarwal & Singh, Software Engineering, 3rd ed., Ch.5 companion slides (99 slides)"),
        ("Method", "Every paragraph anchored to its source slide as [S:n]"),
        ("Status", "Draft for review — verify anchors before final use"),
    ]
    for k, v in meta:
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(f"{k}:  "); r1.bold = True; r1.font.name = FONT; r1.font.size = Pt(10.5)
        r2 = p.add_run(v); r2.font.name = FONT; r2.font.size = Pt(10.5)

    doc.add_page_break()
    heading(doc, "Table of Contents", 1)
    p = doc.add_paragraph(); add_field(p, r'TOC \o "1-3" \h \z \u')
    n = doc.add_paragraph()
    r = n.add_run("(In Word: select all and press F9, or right-click > Update Field.)")
    r.italic = True; r.font.size = Pt(8.5); r.font.color.rgb = GREY

    if figures:
        doc.add_page_break()
        heading(doc, "List of Figures", 1)
        for cap in figures:
            p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
            runs_with_anchor(p, cap, base_size=9.5)


def main():
    import sys
    md_path = Path(sys.argv[1]) if len(sys.argv) > 1 else MD
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else OUT
    md_text = md_path.read_text(encoding="utf-8")

    doc = Document()
    set_base(doc)
    for s in doc.sections:
        s.top_margin = Inches(1.0); s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0); s.right_margin = Inches(1.0)

    figures_preview = []
    for ln in md_text.split("\n"):
        if ln.strip().startswith("*Figure"):
            figures_preview.append(ln.strip().strip("*"))

    cover_and_front(doc, figures_preview)
    doc.add_page_break()
    figures = parse_md(doc, md_path)

    # make Word update fields (TOC) automatically on open
    try:
        uf = OxmlElement("w:updateFields"); uf.set(qn("w:val"), "true")
        doc.settings.element.append(uf)
    except Exception:
        pass

    doc.save(out_path)
    print(f"Saved: {out_path}")
    print(f"Paragraphs: {len(doc.paragraphs)}  Tables: {len(doc.tables)}  Figures: {len(figures)}")
    return out_path


if __name__ == "__main__":
    main()
