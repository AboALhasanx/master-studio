#!/usr/bin/env python3
"""
Master Studio PDF-to-Markdown Reader
-------------------------------------
Converts complex academic PDFs (two-column papers, textbooks, lecture slides)
into clean, structured GitHub-flavored Markdown for AI agents.

Powered by PyMuPDF4LLM:
- Preserves multi-column reading order
- Converts tabular data into Markdown tables
- Extracts headings, bold, italics, and code blocks
- 100% local, offline, and free (no API keys, zero cloud costs)
"""

import sys
import argparse
from pathlib import Path
import pymupdf4llm

def parse_pages(pages_str):
    """Parses page strings like '1-5', '1,3,5', or '10' into 0-indexed page list."""
    if not pages_str:
        return None
    pages = set()
    parts = pages_str.split(',')
    for part in parts:
        part = part.strip()
        if '-' in part:
            start, end = part.split('-')
            for p in range(int(start), int(end) + 1):
                pages.add(p - 1)
        else:
            pages.add(int(part) - 1)
    return sorted(list(pages))

def main():
    parser = argparse.ArgumentParser(description="Master Studio PDF Reader (PDF -> Clean Markdown)")
    parser.add_argument("pdf", help="Path to input PDF file")
    parser.add_argument("-o", "--output", help="Path to output Markdown file (default: stdout)")
    parser.add_argument("-p", "--pages", help="Pages to extract, e.g. '1-5' or '1,3,5' (1-based)")
    parser.add_argument("--margins", type=float, nargs=4, default=[0, 0, 0, 0],
                        help="Margins to ignore [top, left, bottom, right] in points")

    args = parser.parse_args()
    pdf_path = Path(args.pdf)

    if not pdf_path.exists():
        print(f"Error: File '{pdf_path}' not found.", file=sys.stderr)
        sys.exit(1)

    page_list = parse_pages(args.pages)

    # Extract Markdown
    md_text = pymupdf4llm.to_markdown(
        str(pdf_path),
        pages=page_list,
        page_chunks=False,
        margins=args.margins
    )

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_text)
        print(f"✅ Successfully extracted Markdown to: {out_path} ({len(md_text)} chars)")
    else:
        # Print directly to stdout for agent consumption
        print(md_text)

if __name__ == "__main__":
    main()
