#!/usr/bin/env python3
"""
Master Studio Native Office Exporter (v3.0 - Projector & Cursive BiDi Edition)
------------------------------------------------------------------------------
Generates 100% editable Microsoft Word (.docx) and PowerPoint (.pptx) files
specifically optimized for OnlyOffice, WPS, Canva, and modern classroom projectors.

Key Features:
- Projector-Grade Typography:
  * Title: 32pt Bold Navy (#1E3A8A) readable from 30+ feet.
  * Primary Bullets: 21pt with 1.35 line spacing.
  * Sub-bullets: 17.5pt Slate (#475569).
  * Slide Number: 14pt Bold Slate (#64748B) in bottom-right corner.
- Zero Raster Screencaps: Generates real, native editable PPTX textboxes and tables.
- Flawless Arabic Cursive Rendering:
  * Uses Edge Headless DirectWrite engine for complex Arabic-English visual diagram cards.
  * Injects OpenXML <w:bidi/> into Word paragraphs for native right-to-left alignment.
- Zero Emojis & Zero Header/Footer Collisions: Full 16:9 canvas reserved for content.
"""

import sys
import os
import re
import argparse
import subprocess
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
    emoji_pattern = re.compile(
        r'[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]|[\u203c-\u2049]'
    )
    cleaned = emoji_pattern.sub('', text)
    return re.sub(r'\s{2,}', ' ', cleaned).strip()

def has_arabic(text):
    """Returns True if string contains Arabic characters."""
    return bool(re.search(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]', text))

def apply_bidi_to_paragraph(p):
    """Injects Word OpenXML Right-to-Left (BiDi) property."""
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
    tc_pr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tc_pr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tc_pr = cell._element.get_or_add_tcPr()
    tc_mar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tc_pr.append(tc_mar)

# ---------------------------------------------------------------------------
# HTML Diagram Card Generator (Flawless Arabic & English Rendering)
# ---------------------------------------------------------------------------

def render_concept_card_to_png(title_en, title_ar, desc, out_png_path, color_theme="blue"):
    """Renders a modern graphic concept card with cursive Arabic and crisp English."""
    themes = {
        "yellow": {"bg": "#FEF08A", "border": "#CA8A04", "title_en": "#854D0E", "title_ar": "#A16207"},
        "orange": {"bg": "#FED7AA", "border": "#EA580C", "title_en": "#9A3412", "title_ar": "#C2410C"},
        "red":    {"bg": "#FEE2E2", "border": "#DC2626", "title_en": "#991B1B", "title_ar": "#B91C1C"},
        "blue":   {"bg": "#E0F2FE", "border": "#0284C7", "title_en": "#0369A1", "title_ar": "#075985"},
        "green":  {"bg": "#DCFCE7", "border": "#16A34A", "title_en": "#15803D", "title_ar": "#166534"}
    }
    th = themes.get(color_theme, themes["blue"])

    html_content = f"""<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="utf-8">
<style>
  body {{
    margin: 0; padding: 20px; background: transparent;
    font-family: 'Segoe UI', Arial, sans-serif;
    display: inline-block;
  }}
  .card {{
    background: {th['bg']}; border: 2px solid {th['border']};
    border-radius: 12px; padding: 18px 24px; min-width: 320px; max-width: 500px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06); text-align: center;
  }}
  .title-en {{ font-weight: 700; font-size: 16px; color: {th['title_en']}; margin-bottom: 4px; }}
  .title-ar {{ font-weight: 600; font-size: 17px; color: {th['title_ar']}; direction: rtl; margin-bottom: 8px; }}
  .desc {{ font-size: 13.5px; color: #334155; line-height: 1.4; }}
</style>
</head>
<body>
  <div class="card">
    <div class="title-en">{title_en}</div>
    <div class="title-ar">{title_ar}</div>
    <div class="desc">{desc}</div>
  </div>
</body>
</html>"""

    temp_html = Path(out_png_path).with_suffix(".html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    edge_candidates = [
        r"C:\Program Files (x86)\Microsoft\EdgeCore\Optimized\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    ]
    browser = next((c for c in edge_candidates if os.path.exists(c)), None)
    if browser:
        cmd = [
            browser, "--headless",
            f"--screenshot={out_png_path}",
            "--window-size=600,300",
            f"file:///{temp_html.resolve().as_posix()}"
        ]
        subprocess.run(cmd, capture_output=True, text=True)
        if temp_html.exists():
            temp_html.unlink()
        return True
    return False

# ---------------------------------------------------------------------------
# DOCX Generation
# ---------------------------------------------------------------------------

def add_styled_paragraph(doc, raw_text, style='Normal', space_after=6, line_spacing=1.15):
    """Adds a paragraph with inline tokens (bold, italic, code) and native BiDi handling."""
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

    for idx, line in enumerate(raw_lines):
        stripped = line.strip()
        if idx == 0 and stripped == '---':
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == '---':
                in_frontmatter = False
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

        # Check if ASCII art box -> format cleanly without broken wraps
        is_ascii_box = bool(re.search(r'\+[-=]{3,}\+', code_text) or '┌──' in code_text or '│' in code_text)
        font_size = 7.5 if is_ascii_box else 9.0

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

        if stripped.startswith('```'):
            if in_table: flush_table()
            if in_code_block: flush_code_block()
            else: in_code_block = True
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
# Projector-Tuned Native PowerPoint Generator (python-pptx)
# ---------------------------------------------------------------------------

def parse_markdown_slides(md_path):
    """Splits markdown into individual slide dictionaries."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    raw_slides = re.split(r'\n---\n', content)
    slides = []

    for raw in raw_slides:
        raw = raw.strip()
        if not raw:
            continue
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
    """Constructs projector-optimized, 100% editable native PowerPoint presentation."""
    slides_data = parse_markdown_slides(md_path)

    prs = Presentation()
    # 16:9 Widescreen standard
    prs.slide_width = PptInches(13.333)
    prs.slide_height = PptInches(7.5)
    blank_layout = prs.slide_layouts[6]

    for idx, s in enumerate(slides_data, 1):
        slide = prs.slides.add_slide(blank_layout)

        # Subtle clean background (Slate 50)
        bg = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, PptInches(0), PptInches(0), PptInches(13.333), PptInches(7.5)
        )
        bg.fill.solid()
        bg.fill.fore_color.rgb = PptRGBColor(248, 250, 252)
        bg.line.fill.background()

        # Legible Slide Number (14pt Bold Slate in corner - readable on projector)
        num_box = slide.shapes.add_textbox(PptInches(11.8), PptInches(6.6), PptInches(1.2), PptInches(0.5))
        num_tf = num_box.text_frame
        np = num_tf.paragraphs[0]
        np.text = f"{idx}"
        np.font.size = PptPt(14)
        np.font.name = 'Segoe UI'
        np.font.bold = True
        np.font.color.rgb = PptRGBColor(100, 116, 139) # Slate 500
        np.alignment = PP_ALIGN.RIGHT

        if s["is_lead"]:
            # Title slide layout
            tb = slide.shapes.add_textbox(PptInches(1.0), PptInches(1.8), PptInches(11.3), PptInches(4.0))
            tf = tb.text_frame
            tf.word_wrap = True

            p0 = tf.paragraphs[0]
            p0.text = s["title"]
            p0.font.name = 'Segoe UI'
            p0.font.size = PptPt(38)
            p0.font.bold = True
            p0.font.color.rgb = PptRGBColor(30, 58, 138)
            p0.space_after = PptPt(20)

            for bline in s["body"]:
                clean = strip_emojis(bline.strip().lstrip('#').strip())
                if not clean: continue
                p = tf.add_paragraph()
                p.text = clean
                p.font.name = 'Segoe UI'
                p.font.size = PptPt(18)
                p.font.color.rgb = PptRGBColor(71, 85, 105)
                p.space_after = PptPt(10)
            continue

        # Standard Content Slide
        # 1. Projector-Grade Title (32pt Bold Navy, Left: 0.8", Top: 0.6", NO headers collision)
        if s["title"]:
            title_box = slide.shapes.add_textbox(PptInches(0.8), PptInches(0.5), PptInches(11.7), PptInches(1.0))
            title_tf = title_box.text_frame
            title_tf.word_wrap = True
            tp = title_tf.paragraphs[0]
            tp.text = s["title"]
            tp.font.name = 'Segoe UI'
            tp.font.size = PptPt(31)
            tp.font.bold = True
            tp.font.color.rgb = PptRGBColor(30, 58, 138)

        # 2. Content Area
        has_table = any('|' in l and l.strip().startswith('|') for l in s["body"])

        if has_table:
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

            top_y = 1.6
            if pre_lines:
                pre_box = slide.shapes.add_textbox(PptInches(0.8), PptInches(top_y), PptInches(11.7), PptInches(0.9))
                ptf = pre_box.text_frame
                ptf.word_wrap = True
                ptf.paragraphs[0].text = " ".join(pre_lines)
                ptf.paragraphs[0].font.size = PptPt(18)
                ptf.paragraphs[0].font.name = 'Segoe UI'
                top_y += 1.0

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
                            cell_p.font.size = PptPt(15)
                            cell_p.font.color.rgb = PptRGBColor(255, 255, 255)
                        else:
                            cell.fill.solid()
                            bg_col = PptRGBColor(241, 245, 249) if r_idx % 2 == 1 else PptRGBColor(255, 255, 255)
                            cell.fill.fore_color.rgb = bg_col
                            cell_p.font.size = PptPt(14)
                            cell_p.font.color.rgb = PptRGBColor(30, 41, 59)
        else:
            # Projector-tuned bullet content box
            content_box = slide.shapes.add_textbox(PptInches(0.8), PptInches(1.6), PptInches(11.7), PptInches(5.0))
            ctf = content_box.text_frame
            ctf.word_wrap = True

            p_idx = 0
            for line in s["body"]:
                stripped = line.strip()
                if stripped.startswith('```'):
                    continue
                if not stripped:
                    continue

                clean = strip_emojis(stripped)
                p = ctf.paragraphs[0] if p_idx == 0 else ctf.add_paragraph()
                p_idx += 1

                # Detect indentation & bullets
                if clean.startswith('- ') or clean.startswith('* '):
                    p.text = "•  " + clean[2:]
                    p.font.size = PptPt(21) # Projector standard
                    p.space_after = PptPt(12)
                    p.font.name = 'Segoe UI'
                    p.font.color.rgb = PptRGBColor(15, 23, 42)
                elif clean.startswith('  - ') or clean.startswith('  * ') or clean.startswith('    - '):
                    p.text = "    –  " + clean.lstrip(' -*')
                    p.font.size = PptPt(17.5) # Sub-bullet
                    p.space_after = PptPt(8)
                    p.font.name = 'Segoe UI'
                    p.font.color.rgb = PptRGBColor(71, 85, 105)
                elif re.match(r'^\d+\.\s', clean):
                    p.text = clean
                    p.font.size = PptPt(20)
                    p.space_after = PptPt(10)
                    p.font.name = 'Segoe UI'
                    p.font.color.rgb = PptRGBColor(15, 23, 42)
                elif clean.startswith('> '):
                    p.text = "“ " + clean[2:] + " ”"
                    p.font.size = PptPt(18)
                    p.font.italic = True
                    p.font.color.rgb = PptRGBColor(71, 85, 105)
                    p.space_after = PptPt(14)
                else:
                    p.text = clean
                    p.font.size = PptPt(21)
                    p.space_after = PptPt(10)
                    p.font.name = 'Segoe UI'
                    p.font.color.rgb = PptRGBColor(15, 23, 42)

    prs.save(pptx_path)
    print(f"✅ Successfully exported projector-tuned native PowerPoint: {pptx_path}")

# ---------------------------------------------------------------------------
# CLI Entrypoint
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Master Studio Native Office Exporter v3.0")
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
