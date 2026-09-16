#!/usr/bin/env python3
"""
Master Studio Native Office Exporter (v2.0)
------------------------------------------
Generates 100% editable Microsoft Word (.docx) and PowerPoint (.pptx) files
tailored specifically for OnlyOffice, WPS, Canva, and Microsoft Office 2016+.

Key Improvements:
- True Native PPTX: Uses python-pptx to generate editable text boxes, native tables,
  and vector shapes. ZERO raster screenshot frames. Fully selectable in OnlyOffice & Canva.
- Clean Layouts: Zero "AI-slop" emojis, NO overlapping headers/footers, generous in-page margins.
- Clean Frontmatter: Strips YAML metadata blocks so they never leak into page 1.
- Native Arabic BiDi / RTL: Auto-detects Arabic text and injects Word OpenXML <w:bidi/>
  and <w:rtl/> properties so mixed Arabic-English flows with correct punctuation.
"""

import sys
import os
import re
import argparse
from pathlib import Path

# Word libraries
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

# PowerPoint libraries
import pptx
from pptx import Presentation
from pptx.util import Inches as PptInches, Pt as PptPt
from pptx.dml.color import RGBColor as PptRGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def strip_emojis(text):
    """Strips decorative emojis and symbols to keep documents academic and clean."""
    if not text:
        return ""
    # Unicode ranges for emojis, pictographs, transport symbols
    emoji_pattern = re.compile(
        r'[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]|[\u203c-\u2049]'
    )
    cleaned = emoji_pattern.sub('', text)
    # Clean up double spaces left after emoji removal
    return re.sub(r'\s{2,}', ' ', cleaned).strip()

def has_arabic(text):
    """Returns True if string contains Arabic characters."""
    return bool(re.search(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]', text))

def apply_bidi_to_paragraph(p):
    """Injects Word OpenXML Right-to-Left (BiDi) property into paragraph properties."""
    pPr = p._p.get_or_add_pPr()
    bidi = parse_xml(f'<w:bidi {nsdecls("w")}/>')
    pPr.append(bidi)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

def apply_rtl_to_run(run):
    """Injects RTL property to text run."""
    rPr = run._r.get_or_add_rPr()
    rtl = parse_xml(f'<w:rtl {nsdecls("w")}/>')
    rPr.append(rtl)
    run.font.name = 'Arial'

def set_cell_background(cell, hex_color):
    """Sets background color of a Word table cell."""
    tc_pr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tc_pr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets internal cell margins in Word tables."""
    tc_pr = cell._element.get_or_add_tcPr()
    tc_mar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tc_pr.append(tc_mar)

# ---------------------------------------------------------------------------
# DOCX Generation
# ---------------------------------------------------------------------------

def add_styled_paragraph(doc, raw_text, style='Normal', space_after=6, line_spacing=1.15):
    """Adds a paragraph with inline tokens (bold, italic, code) and BiDi handling."""
    text = strip_emojis(raw_text)
    if not text:
        return None

    p = doc.add_paragraph(style=style)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing

    is_ar = has_arabic(text)
    if is_ar:
        apply_bidi_to_paragraph(p)

    tokens = re.split(r'(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*)', text)
    for token in tokens:
        if not token:
            continue
        if token.startswith('`') and token.endswith('`') and len(token) >= 2:
            run = p.add_run(token[1:-1])
            run.font.name = 'Consolas'
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(180, 40, 40)
        elif token.startswith('**') and token.endswith('**') and len(token) >= 4:
            run = p.add_run(token[2:-2])
            run.bold = True
            if is_ar and has_arabic(token):
                apply_rtl_to_run(run)
        elif token.startswith('*') and token.endswith('*') and len(token) >= 2:
            run = p.add_run(token[1:-1])
            run.italic = True
            if is_ar and has_arabic(token):
                apply_rtl_to_run(run)
        else:
            run = p.add_run(token)
            if is_ar and has_arabic(token):
                apply_rtl_to_run(run)

    return p

def convert_markdown_to_docx(md_path, docx_path):
    """Converts Markdown to a clean, professional DOCX for OnlyOffice/Word."""
    with open(md_path, 'r', encoding='utf-8') as f:
        raw_lines = f.readlines()

    # Step 1: Strip YAML Frontmatter completely
    lines = []
    in_frontmatter = False
    frontmatter_handled = False

    for idx, line in enumerate(raw_lines):
        stripped = line.strip()
        if idx == 0 and stripped == '---':
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == '---':
                in_frontmatter = False
                frontmatter_handled = True
            continue
        lines.append(line)

    doc = Document()

    # Page Margins (1 inch clean)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Base Styling
    normal = doc.styles['Normal']
    normal.font.name = 'Segoe UI'
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = RGBColor(30, 41, 59)

    in_code_block = False
    code_lines = []
    in_table = False
    table_rows = []

    def flush_table():
        nonlocal table_rows, in_table
        if not table_rows:
            in_table = False
            return
        col_count = max(len(r) for r in table_rows)
        table = doc.add_table(rows=len(table_rows), cols=col_count)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER

        for r_idx, r_data in enumerate(table_rows):
            is_header = (r_idx == 0)
            row = table.rows[r_idx]
            for c_idx in range(col_count):
                cell = row.cells[c_idx]
                val = strip_emojis(r_data[c_idx] if c_idx < len(r_data) else "")
                cell.text = val
                set_cell_margins(cell, top=80, bottom=80, left=120, right=120)

                if is_header:
                    set_cell_background(cell, "1E3A8A") # Navy
                    for p in cell.paragraphs:
                        for run in p.runs:
                            run.font.name = 'Segoe UI'
                            run.font.bold = True
                            run.font.size = Pt(9.5)
                            run.font.color.rgb = RGBColor(255, 255, 255)
                else:
                    bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
                    set_cell_background(cell, bg)
                    for p in cell.paragraphs:
                        if has_arabic(val):
                            apply_bidi_to_paragraph(p)
                        for run in p.runs:
                            run.font.name = 'Segoe UI'
                            run.font.size = Pt(9.5)
                            run.font.color.rgb = RGBColor(30, 41, 59)

        doc.add_paragraph().paragraph_format.space_after = Pt(4)
        table_rows = []
        in_table = False

    def flush_code_block():
        nonlocal code_lines, in_code_block
        if not code_lines:
            in_code_block = False
            return
        code_text = "".join(code_lines).rstrip()
        
        # Check if ASCII art box (avoid ugly formatting)
        if re.search(r'\+[-=]{3,}\+', code_text):
            # Clean monospaced box with compact font
            font_size = 7.5
        else:
            font_size = 9.0

        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = table.cell(0, 0)
        cell.text = code_text
        set_cell_background(cell, "F1F5F9")
        set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
        for p in cell.paragraphs:
            for run in p.runs:
                run.font.name = 'Consolas'
                run.font.size = Pt(font_size)
                run.font.color.rgb = RGBColor(15, 23, 42)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)
        code_lines = []
        in_code_block = False

    for line in lines:
        stripped = line.strip()

        # Handle code blocks
        if stripped.startswith('```'):
            if in_table:
                flush_table()
            if in_code_block:
                flush_code_block()
            else:
                in_code_block = True
            continue

        if in_code_block:
            code_lines.append(line)
            continue

        # Handle Markdown Tables
        if '|' in stripped and stripped.startswith('|') and stripped.endswith('|'):
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                continue
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            table_rows.append(cells)
            in_table = True
            continue
        elif in_table:
            flush_table()

        if not stripped:
            continue

        # Headings
        if stripped.startswith('# '):
            text = strip_emojis(stripped[2:])
            h = doc.add_heading(level=1)
            h.paragraph_format.space_before = Pt(18)
            h.paragraph_format.space_after = Pt(6)
            if has_arabic(text): apply_bidi_to_paragraph(h)
            run = h.add_run(text)
            run.font.name = 'Segoe UI Semibold'
            run.font.size = Pt(17)
            run.font.color.rgb = RGBColor(15, 23, 42)
        elif stripped.startswith('## '):
            text = strip_emojis(stripped[3:])
            h = doc.add_heading(level=2)
            h.paragraph_format.space_before = Pt(14)
            h.paragraph_format.space_after = Pt(4)
            if has_arabic(text): apply_bidi_to_paragraph(h)
            run = h.add_run(text)
            run.font.name = 'Segoe UI Semibold'
            run.font.size = Pt(13.5)
            run.font.color.rgb = RGBColor(30, 58, 138)
        elif stripped.startswith('### '):
            text = strip_emojis(stripped[4:])
            h = doc.add_heading(level=3)
            h.paragraph_format.space_before = Pt(10)
            h.paragraph_format.space_after = Pt(3)
            if has_arabic(text): apply_bidi_to_paragraph(h)
            run = h.add_run(text)
            run.font.name = 'Segoe UI Semibold'
            run.font.size = Pt(11.5)
            run.font.color.rgb = RGBColor(51, 65, 85)
        elif stripped.startswith('> '):
            text = strip_emojis(stripped[2:])
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            p.paragraph_format.space_after = Pt(6)
            if has_arabic(text): apply_bidi_to_paragraph(p)
            run = p.add_run(text)
            run.italic = True
            run.font.color.rgb = RGBColor(71, 85, 105)
        elif stripped.startswith('- ') or stripped.startswith('* '):
            add_styled_paragraph(doc, stripped[2:], style='List Bullet', space_after=3)
        elif re.match(r'^\d+\.\s', stripped):
            prefix_match = re.match(r'^\d+\.\s', stripped)
            add_styled_paragraph(doc, stripped[prefix_match.end():], style='List Number', space_after=3)
        else:
            add_styled_paragraph(doc, stripped)

    if in_table: flush_table()
    if in_code_block: flush_code_block()

    doc.save(docx_path)
    print(f"✅ Successfully exported clean, BiDi-aware Word doc to: {docx_path}")

# ---------------------------------------------------------------------------
# True Native PowerPoint (python-pptx)
# ---------------------------------------------------------------------------

def parse_markdown_slides(md_path):
    """Splits markdown into individual slide dictionaries."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by horizontal rule slides separator '---'
    raw_slides = re.split(r'\n---\n', content)
    slides = []

    for raw in raw_slides:
        raw = raw.strip()
        if not raw:
            continue
        # Skip marp frontmatter
        if raw.startswith('marp:') or 'paginate:' in raw:
            continue

        lines = raw.split('\n')
        slide_title = ""
        body_lines = []
        is_lead = '<!-- _class: lead -->' in raw

        for line in lines:
            stripped = line.strip()
            if '<!--' in stripped and '-->' in stripped:
                continue
            if not slide_title and (stripped.startswith('# ') or stripped.startswith('## ')):
                slide_title = strip_emojis(re.sub(r'^#+\s*', '', stripped))
            else:
                body_lines.append(line)

        slides.append({
            "title": slide_title,
            "body": body_lines,
            "is_lead": is_lead
        })

    return slides

def convert_markdown_to_native_pptx(md_path, pptx_path):
    """Constructs true native, 100% editable PowerPoint slides with genuine textboxes and tables."""
    slides_data = parse_markdown_slides(md_path)

    prs = Presentation()
    # 16:9 Widescreen standard
    prs.slide_width = PptInches(13.333)
    prs.slide_height = PptInches(7.5)
    blank_layout = prs.slide_layouts[6]

    for idx, s in enumerate(slides_data, 1):
        slide = prs.slides.add_slide(blank_layout)

        # Background subtle tone
        bg_shape = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, PptInches(0), PptInches(0), PptInches(13.333), PptInches(7.5)
        )
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = PptRGBColor(248, 250, 252) # Slate 50
        bg_shape.line.fill.background()

        # Discreet slide number
        num_box = slide.shapes.add_textbox(PptInches(12.0), PptInches(6.8), PptInches(1.0), PptInches(0.4))
        num_tf = num_box.text_frame
        np = num_tf.paragraphs[0]
        np.text = f"{idx}"
        np.font.size = PptPt(10)
        np.font.name = 'Segoe UI'
        np.font.color.rgb = PptRGBColor(148, 163, 184)
        np.alignment = PP_ALIGN.RIGHT

        if s["is_lead"]:
            # Title slide layout
            tb = slide.shapes.add_textbox(PptInches(1.2), PptInches(2.0), PptInches(10.9), PptInches(3.5))
            tf = tb.text_frame
            tf.word_wrap = True

            p0 = tf.paragraphs[0]
            p0.text = s["title"]
            p0.font.name = 'Segoe UI'
            p0.font.size = PptPt(36)
            p0.font.bold = True
            p0.font.color.rgb = PptRGBColor(30, 58, 138)
            p0.space_after = PptPt(16)

            for bline in s["body"]:
                clean = strip_emojis(bline.strip().lstrip('#').strip())
                if not clean: continue
                p = tf.add_paragraph()
                p.text = clean
                p.font.name = 'Segoe UI'
                p.font.size = PptPt(16)
                p.font.color.rgb = PptRGBColor(71, 85, 105)
                p.space_after = PptPt(8)
            continue

        # Standard Content Slide
        # 1. Native Title Box (Top 0.6", Height 0.9", NO headers/footers collision)
        if s["title"]:
            title_box = slide.shapes.add_textbox(PptInches(0.8), PptInches(0.5), PptInches(11.7), PptInches(0.9))
            title_tf = title_box.text_frame
            title_tf.word_wrap = True
            tp = title_tf.paragraphs[0]
            tp.text = s["title"]
            tp.font.name = 'Segoe UI'
            tp.font.size = PptPt(26)
            tp.font.bold = True
            tp.font.color.rgb = PptRGBColor(30, 58, 138)

        # 2. Content Area
        # Check if slide contains a markdown table
        has_table = any('|' in l and l.strip().startswith('|') for l in s["body"])
        
        if has_table:
            # Parse table lines
            t_rows = []
            pre_lines = []
            for l in s["body"]:
                stripped = l.strip()
                if '|' in stripped and stripped.startswith('|') and stripped.endswith('|'):
                    if re.match(r'^\|[\s\-:|]+\|$', stripped): continue
                    cells = [strip_emojis(c.strip()) for c in stripped.split('|')[1:-1]]
                    t_rows.append(cells)
                elif not t_rows and stripped:
                    pre_lines.append(strip_emojis(stripped))

            # Add pre-table text if any
            top_y = 1.6
            if pre_lines:
                pre_box = slide.shapes.add_textbox(PptInches(0.8), PptInches(top_y), PptInches(11.7), PptInches(1.0))
                ptf = pre_box.text_frame
                ptf.word_wrap = True
                ptf.paragraphs[0].text = " ".join(pre_lines)
                ptf.paragraphs[0].font.size = PptPt(14)
                ptf.paragraphs[0].font.name = 'Segoe UI'
                top_y += 1.1

            # Build REAL Native PowerPoint Table
            if t_rows:
                col_cnt = max(len(r) for r in t_rows)
                row_cnt = len(t_rows)
                tbl_shape = slide.shapes.add_table(
                    row_cnt, col_cnt, PptInches(0.8), PptInches(top_y), PptInches(11.7), PptInches(4.5)
                )
                tbl = tbl_shape.table
                for r_idx, r_data in enumerate(t_rows):
                    for c_idx in range(col_cnt):
                        val = r_data[c_idx] if c_idx < len(r_data) else ""
                        cell = tbl.cell(r_idx, c_idx)
                        cell.text = val
                        cell_p = cell.text_frame.paragraphs[0]
                        cell_p.font.name = 'Segoe UI'
                        if r_idx == 0:
                            cell.fill.solid()
                            cell.fill.fore_color.rgb = PptRGBColor(30, 58, 138)
                            cell_p.font.bold = True
                            cell_p.font.size = PptPt(13)
                            cell_p.font.color.rgb = PptRGBColor(255, 255, 255)
                        else:
                            cell.fill.solid()
                            bg_col = PptRGBColor(241, 245, 249) if r_idx % 2 == 1 else PptRGBColor(255, 255, 255)
                            cell.fill.fore_color.rgb = bg_col
                            cell_p.font.size = PptPt(12)
                            cell_p.font.color.rgb = PptRGBColor(30, 41, 59)
        else:
            # Native Bullet / Text Frame
            content_box = slide.shapes.add_textbox(PptInches(0.8), PptInches(1.5), PptInches(11.7), PptInches(5.0))
            ctf = content_box.text_frame
            ctf.word_wrap = True
            
            p_idx = 0
            in_code = False
            for line in s["body"]:
                stripped = line.strip()
                if stripped.startswith('```'):
                    in_code = not in_code
                    continue
                if not stripped:
                    continue

                clean = strip_emojis(stripped)
                if in_code or re.search(r'^\+[-=]{3,}\+', stripped):
                    # Monospaced diagram line
                    p = ctf.paragraphs[0] if p_idx == 0 else ctf.add_paragraph()
                    p.text = clean
                    p.font.name = 'Consolas'
                    p.font.size = PptPt(11)
                    p.font.color.rgb = PptRGBColor(30, 41, 59)
                    p_idx += 1
                    continue

                p = ctf.paragraphs[0] if p_idx == 0 else ctf.add_paragraph()
                p_idx += 1

                # Detect list items
                if clean.startswith('- ') or clean.startswith('* '):
                    p.text = "•  " + clean[2:]
                    p.level = 0
                    p.font.size = PptPt(16)
                    p.space_after = PptPt(10)
                elif re.match(r'^\d+\.\s', clean):
                    p.text = clean
                    p.font.size = PptPt(16)
                    p.space_after = PptPt(10)
                elif clean.startswith('> '):
                    p.text = "“ " + clean[2:] + " ”"
                    p.font.size = PptPt(15)
                    p.font.italic = True
                    p.font.color.rgb = PptRGBColor(71, 85, 105)
                    p.space_after = PptPt(12)
                else:
                    p.text = clean
                    p.font.size = PptPt(16)
                    p.space_after = PptPt(8)

                p.font.name = 'Segoe UI'
                p.font.color.rgb = PptRGBColor(30, 41, 59)

    prs.save(pptx_path)
    print(f"✅ Successfully exported 100% editable native PowerPoint presentation to: {pptx_path}")

# ---------------------------------------------------------------------------
# CLI Entrypoint
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Master Studio Native Office Exporter v2.0")
    parser.add_argument("format", choices=["docx", "pptx", "both"], help="Target format")
    parser.add_argument("input", help="Path to input Markdown file")
    parser.add_argument("-o", "--output", help="Path to output file")

    args = parser.parse_args()
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' not found.", file=sys.stderr)
        sys.exit(1)

    if args.format in ["docx", "both"]:
        out_docx = Path(args.output) if (args.output and args.format == "docx") else input_path.with_suffix(".docx")
        convert_markdown_to_docx(input_path, out_docx)

    if args.format in ["pptx", "both"]:
        out_pptx = Path(args.output) if (args.output and args.format == "pptx") else input_path.with_suffix(".pptx")
        convert_markdown_to_native_pptx(input_path, out_pptx)

if __name__ == "__main__":
    main()
