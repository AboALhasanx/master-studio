#!/usr/bin/env python3
"""
Master Studio Office Exporter
-----------------------------
Converts Markdown study notes, reports, and slide decks into professional
Microsoft Word (.docx) and PowerPoint (.pptx) files tailored for OnlyOffice
and Microsoft Office 2016+.

Features:
- DOCX: Formatted headings (H1-H4), tables with styled headers and borders,
        code blocks in shaded callouts, bullet/numbered lists, bold/italics.
- PPTX: Multi-slide compilation via local Marp CLI with automated browser detection.
"""

import sys
import os
import re
import argparse
import subprocess
from pathlib import Path

# Python-docx for Word document creation
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    """Sets the background color of a table cell."""
    tc_pr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tc_pr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets internal padding for a table cell."""
    tc_pr = cell._element.get_or_add_tcPr()
    tc_mar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tc_pr.append(tc_mar)

def add_styled_paragraph(doc, text, style='Normal', space_after=6, line_spacing=1.15):
    """Adds a paragraph with custom inline formatting (bold, italic, code)."""
    p = doc.add_paragraph(style=style)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing

    # Regex for inline markdown tokens: `code`, **bold**, *italic*
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
        elif token.startswith('*') and token.endswith('*') and len(token) >= 2:
            run = p.add_run(token[1:-1])
            run.italic = True
        else:
            p.add_run(token)
    return p

def convert_markdown_to_docx(md_path, docx_path):
    """Parses markdown and produces an OnlyOffice/Word 2016+ compatible DOCX."""
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    doc = Document()

    # Document Geometry
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Base Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Segoe UI'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = RGBColor(30, 41, 59) # Slate 800

    in_code_block = False
    code_block_lines = []
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

        for row_idx, row_data in enumerate(table_rows):
            is_header = (row_idx == 0)
            row = table.rows[row_idx]
            for col_idx in range(col_count):
                cell = row.cells[col_idx]
                text = row_data[col_idx] if col_idx < len(row_data) else ""
                cell.text = text.strip()

                # Formatting
                set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
                if is_header:
                    set_cell_background(cell, "1E3A8A") # Navy Blue
                    for p in cell.paragraphs:
                        for run in p.runs:
                            run.font.name = 'Segoe UI'
                            run.font.bold = True
                            run.font.size = Pt(9.5)
                            run.font.color.rgb = RGBColor(255, 255, 255)
                else:
                    bg = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
                    set_cell_background(cell, bg)
                    for p in cell.paragraphs:
                        for run in p.runs:
                            run.font.name = 'Segoe UI'
                            run.font.size = Pt(9.5)
                            run.font.color.rgb = RGBColor(30, 41, 59)

        doc.add_paragraph().paragraph_format.space_after = Pt(4)
        table_rows = []
        in_table = False

    def flush_code_block():
        nonlocal code_block_lines, in_code_block
        if not code_block_lines:
            in_code_block = False
            return
        code_text = "".join(code_block_lines)
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = table.cell(0, 0)
        cell.text = code_text.rstrip()
        set_cell_background(cell, "F1F5F9")
        set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
        for p in cell.paragraphs:
            for run in p.runs:
                run.font.name = 'Consolas'
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(15, 23, 42)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)
        code_block_lines = []
        in_code_block = False

    # Process lines
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Handle Code Block fences
        if stripped.startswith('```'):
            if in_table:
                flush_table()
            if in_code_block:
                flush_code_block()
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_block_lines.append(line)
            i += 1
            continue

        # Handle Tables
        if '|' in stripped and stripped.startswith('|') and stripped.endswith('|'):
            # Check if separator row
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                i += 1
                continue
            cells = [c for c in stripped.split('|')[1:-1]]
            table_rows.append(cells)
            in_table = True
            i += 1
            continue
        elif in_table:
            flush_table()

        # Empty line
        if not stripped:
            i += 1
            continue

        # Headings
        if stripped.startswith('# '):
            h = doc.add_heading(level=1)
            h.paragraph_format.space_before = Pt(16)
            h.paragraph_format.space_after = Pt(6)
            run = h.add_run(stripped[2:])
            run.font.name = 'Segoe UI Semibold'
            run.font.size = Pt(18)
            run.font.color.rgb = RGBColor(15, 23, 42)
        elif stripped.startswith('## '):
            h = doc.add_heading(level=2)
            h.paragraph_format.space_before = Pt(12)
            h.paragraph_format.space_after = Pt(4)
            run = h.add_run(stripped[3:])
            run.font.name = 'Segoe UI Semibold'
            run.font.size = Pt(14)
            run.font.color.rgb = RGBColor(30, 58, 138) # Deep Blue
        elif stripped.startswith('### '):
            h = doc.add_heading(level=3)
            h.paragraph_format.space_before = Pt(8)
            h.paragraph_format.space_after = Pt(3)
            run = h.add_run(stripped[4:])
            run.font.name = 'Segoe UI Semibold'
            run.font.size = Pt(12)
            run.font.color.rgb = RGBColor(51, 65, 85)
        elif stripped.startswith('> '):
            # Blockquote
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            p.paragraph_format.space_after = Pt(6)
            run = p.add_run("“ " + stripped[2:] + " ”")
            run.italic = True
            run.font.color.rgb = RGBColor(71, 85, 105)
        elif stripped.startswith('- ') or stripped.startswith('* '):
            # Bullet list
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_after = Pt(3)
            tokens = re.split(r'(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*)', stripped[2:])
            for token in tokens:
                if not token: continue
                if token.startswith('`') and token.endswith('`'):
                    run = p.add_run(token[1:-1])
                    run.font.name = 'Consolas'
                    run.font.size = Pt(9.5)
                elif token.startswith('**') and token.endswith('**'):
                    run = p.add_run(token[2:-2])
                    run.bold = True
                elif token.startswith('*') and token.endswith('*'):
                    run = p.add_run(token[1:-1])
                    run.italic = True
                else:
                    p.add_run(token)
        elif re.match(r'^\d+\.\s', stripped):
            # Numbered list
            prefix_match = re.match(r'^(\d+\.\s)', stripped)
            prefix = prefix_match.group(1)
            content = stripped[len(prefix):]
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.space_after = Pt(3)
            tokens = re.split(r'(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*)', content)
            for token in tokens:
                if not token: continue
                if token.startswith('`') and token.endswith('`'):
                    run = p.add_run(token[1:-1])
                    run.font.name = 'Consolas'
                elif token.startswith('**') and token.endswith('**'):
                    run = p.add_run(token[2:-2])
                    run.bold = True
                else:
                    p.add_run(token)
        else:
            add_styled_paragraph(doc, stripped)

        i += 1

    if in_table:
        flush_table()
    if in_code_block:
        flush_code_block()

    doc.save(docx_path)
    print(f"✅ Successfully exported Word document to: {docx_path}")

def convert_markdown_to_pptx(md_path, pptx_path):
    """Compiles Marp markdown into a PowerPoint presentation (.pptx)."""
    edge_candidates = [
        r"C:\Program Files (x86)\Microsoft\EdgeCore\Optimized\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    ]
    browser_path = None
    for candidate in edge_candidates:
        if os.path.exists(candidate):
            browser_path = candidate
            break

    env = os.environ.copy()
    if browser_path:
        env["CHROME_PATH"] = browser_path

    cmd = [
        "npx", "-y", "@marp-team/marp-cli",
        str(md_path),
        "--pptx",
        "-o", str(pptx_path),
        "--allow-local-files"
    ]
    result = subprocess.run(cmd, env=env, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        print(f"✅ Successfully exported PowerPoint presentation to: {pptx_path}")
    else:
        print(f"❌ PowerPoint compilation failed:\n{result.stderr}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Master Studio Office Exporter (.docx & .pptx)")
    parser.add_argument("format", choices=["docx", "pptx", "both"], help="Target format")
    parser.add_argument("input", help="Path to input Markdown file")
    parser.add_argument("-o", "--output", help="Path to output file")

    args = parser.parse_args()
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file {input_path} does not exist.")
        sys.exit(1)

    if args.format in ["docx", "both"]:
        out_docx = Path(args.output) if (args.output and args.format == "docx") else input_path.with_suffix(".docx")
        convert_markdown_to_docx(input_path, out_docx)

    if args.format in ["pptx", "both"]:
        out_pptx = Path(args.output) if (args.output and args.format == "pptx") else input_path.with_suffix(".pptx")
        convert_markdown_to_pptx(input_path, out_pptx)

if __name__ == "__main__":
    main()
