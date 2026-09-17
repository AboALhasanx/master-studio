#!/usr/bin/env python3
"""
Master Studio Column-Aware OCR Reader
-------------------------------------
Extracts text from scanned two-column PDFs (textbooks, teacher handbooks, answer
keys) while preserving the correct reading order: all of the left column, then all
of the right column.

Why this exists: `pdf_reader.py` dumps RapidOCR text boxes in the engine's own
order, which zig-zags between the two columns of a scanned textbook page and makes
answer keys unreadable. This tool sorts every recognized box into its column by
horizontal center, then by vertical position.

It also detokenizes the common OCR artifacts produced by RapidOCR, which frequently
drops the space between words ("Answerswill vary.Possible answers:").

100% local (RapidOCR / ONNX Runtime), no API calls, no cost.

Usage:
    python pdf_ocr_columns.py "book.pdf" --pages 88-116 -o answer_key.md
    python pdf_ocr_columns.py "book.pdf" --pages 89 --dpi 200
"""

import argparse
import re
import sys
from pathlib import Path

import pymupdf

try:
    from rapidocr_onnxruntime import RapidOCR
    HAS_RAPID_OCR = True
except ImportError:
    HAS_RAPID_OCR = False


def parse_pages(pages_str, total_pages):
    """Parses '1-5', '1,3,5' or '10' (1-based) into a sorted 0-indexed list."""
    if not pages_str:
        return list(range(total_pages))
    pages = set()
    for part in pages_str.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = part.split("-")
            pages.update(range(int(start) - 1, int(end)))
        else:
            pages.add(int(part) - 1)
    return sorted(p for p in pages if 0 <= p < total_pages)


def detokenize(text):
    """
    Re-inserts spaces that RapidOCR commonly drops between words and after
    punctuation. Deliberately conservative: it only inserts a space at
    boundaries that are unambiguously word boundaries in English.
    """
    text = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)      # "AnswerswillVary" -> "Answerswill Vary"
    text = re.sub(r"(?<=[.!?:;])(?=[A-Za-z0-9])", " ", text)  # "1.We" -> "1. We"
    text = re.sub(r"(?<=,)(?=\S)", " ", text)              # "A,p.3" -> "A, p.3"
    text = re.sub(r"(?<=[a-z])(?=\()", " ", text)          # "answer(paragraph 2)"
    return re.sub(r"[ \t]{2,}", " ", text).strip()


def page_to_lines(engine, doc, pno, dpi, columns):
    """Renders one page and returns its lines in column-major reading order."""
    pix = doc[pno].get_pixmap(dpi=dpi)
    result, _ = engine(pix.tobytes("png"))
    if not result:
        return []

    boxes = []
    for box, text, _score in result:
        xs = [pt[0] for pt in box]
        ys = [pt[1] for pt in box]
        text = text.strip()
        if not text:
            continue
        boxes.append({
            "cx": (min(xs) + max(xs)) / 2.0,
            "cy": sum(ys) / 4.0,
            "w": max(xs) - min(xs),
            "text": text,
        })

    if columns < 2:
        return [detokenize(b["text"]) for b in sorted(boxes, key=lambda b: b["cy"])]

    # A box wider than ~85% of the page spans both columns (page titles, rules);
    # it belongs to neither, so it is emitted before the columns it introduces.
    page_w = pix.width
    spanning = [b for b in boxes if b["w"] > 0.85 * page_w]
    body = [b for b in boxes if b["w"] <= 0.85 * page_w]
    mid = page_w / 2.0

    lines = [detokenize(b["text"]) for b in sorted(spanning, key=lambda b: b["cy"])]
    for is_left in (True, False):
        column = [b for b in body if (b["cx"] < mid) == is_left]
        lines.extend(detokenize(b["text"]) for b in sorted(column, key=lambda b: b["cy"]))
    return lines


def main():
    parser = argparse.ArgumentParser(
        description="Column-aware OCR for scanned two-column PDFs (local RapidOCR)."
    )
    parser.add_argument("pdf", help="Path to the scanned PDF")
    parser.add_argument("-o", "--output", help="Output Markdown file (default: stdout)")
    parser.add_argument("-p", "--pages", help="Pages to OCR, e.g. '88-116' or '89,91' (1-based)")
    parser.add_argument("--dpi", type=int, default=150, help="Render DPI for OCR (default: 150)")
    parser.add_argument("--columns", type=int, default=2, help="Page columns: 2 (default) or 1")
    parser.add_argument("--no-page-markers", action="store_true",
                        help="Omit the '<!-- printed page N -->' markers")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"Error: file not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)
    if not HAS_RAPID_OCR:
        print("Error: RapidOCR not installed. Install via: pip install rapidocr-onnxruntime",
              file=sys.stderr)
        sys.exit(1)

    doc = pymupdf.open(str(pdf_path))
    pages = parse_pages(args.pages, len(doc))
    engine = RapidOCR()

    out = [
        f"# OCR: {pdf_path.name}",
        f"> Column-aware local extraction (RapidOCR, {args.dpi} DPI, "
        f"{args.columns} column{'s' if args.columns > 1 else ''})\n",
    ]
    for pno in pages:
        lines = page_to_lines(engine, doc, pno, args.dpi, args.columns)
        if not args.no_page_markers:
            out.append(f"<!-- printed page {pno + 1} -->")
        out.extend(lines)
        out.append("")
        print(f"  page {pno + 1}: {len(lines)} lines", file=sys.stderr)

    md = re.sub(r"\n{3,}", "\n\n", "\n".join(out))

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")
        print(f"Saved {len(md)} chars to: {out_path}", file=sys.stderr)
    else:
        print(md)


if __name__ == "__main__":
    main()
