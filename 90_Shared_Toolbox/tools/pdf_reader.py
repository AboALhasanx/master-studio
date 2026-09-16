#!/usr/bin/env python3
"""
Master Studio PDF-to-Markdown & OCR Reader
------------------------------------------
Converts academic PDFs (digital or scanned) into clean, structured Markdown for AI agents.

Features:
- Digital PDFs: High-speed layout-aware Markdown extraction via PyMuPDF4LLM.
- Scanned PDFs (CamScanner / Phone Photos): Automatic fallback to local RapidOCR (ONNX Runtime).
- Vision Mode: Optional rendering of pages to high-resolution PNG images for Multimodal Vision AI.
- 100% offline, local, private, and zero API costs.
"""

import sys
import argparse
from pathlib import Path
import pymupdf
import pymupdf4llm

try:
    from rapidocr_onnxruntime import RapidOCR
    HAS_RAPID_OCR = True
except ImportError:
    HAS_RAPID_OCR = False


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


def run_ocr_on_pdf(pdf_path, page_list=None, dpi=150):
    """Runs RapidOCR on selected pages of a scanned PDF."""
    if not HAS_RAPID_OCR:
        return "[Error] RapidOCR is not installed. Install via: pip install rapidocr-onnxruntime"

    doc = pymupdf.open(str(pdf_path))
    engine = RapidOCR()
    total_pages = len(doc)
    target_pages = page_list if page_list is not None else list(range(total_pages))

    output_lines = []
    output_lines.append(f"# Scanned Document OCR: {pdf_path.name}")
    output_lines.append(f"> Extracted via Master Studio RapidOCR (Local ONNX Runtime)\n")

    for pno in target_pages:
        if pno < 0 or pno >= total_pages:
            continue
        page = doc[pno]
        pix = page.get_pixmap(dpi=dpi)
        img_bytes = pix.tobytes("png")
        
        result, _ = engine(img_bytes)
        output_lines.append(f"## Page {pno + 1}")
        if result:
            for item in result:
                text_line = item[1].strip()
                if text_line:
                    output_lines.append(text_line)
        else:
            output_lines.append("*(No text recognized on this page)*")
        output_lines.append("")

    return "\n".join(output_lines)


def render_pdf_images(pdf_path, out_dir, page_list=None, dpi=150):
    """Renders PDF pages to high-res PNG images for Multimodal Vision agents."""
    doc = pymupdf.open(str(pdf_path))
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    total_pages = len(doc)
    target_pages = page_list if page_list is not None else list(range(total_pages))

    rendered_files = []
    for pno in target_pages:
        if pno < 0 or pno >= total_pages:
            continue
        page = doc[pno]
        pix = page.get_pixmap(dpi=dpi)
        img_name = f"page_{pno + 1:03d}.png"
        target_file = out_path / img_name
        pix.save(str(target_file))
        rendered_files.append(target_file)

    return rendered_files


def main():
    parser = argparse.ArgumentParser(description="Master Studio PDF Reader (PDF -> Clean Markdown + OCR)")
    parser.add_argument("pdf", help="Path to input PDF file")
    parser.add_argument("-o", "--output", help="Path to output Markdown file (default: stdout)")
    parser.add_argument("-p", "--pages", help="Pages to extract, e.g. '1-5' or '1,3,5' (1-based)")
    parser.add_argument("--ocr", action="store_true", help="Force OCR mode even if digital text is present")
    parser.add_argument("--render-images", help="Directory path to save high-res PNGs for Vision AI")
    parser.add_argument("--dpi", type=int, default=150, help="DPI for rendering images/OCR (default: 150)")
    parser.add_argument("--margins", type=float, nargs=4, default=[0, 0, 0, 0],
                        help="Margins to ignore [top, left, bottom, right] in points")

    args = parser.parse_args()
    pdf_path = Path(args.pdf)

    if not pdf_path.exists():
        print(f"Error: File '{pdf_path}' not found.", file=sys.stderr)
        sys.exit(1)

    page_list = parse_pages(args.pages)

    # Optional: Render images for Vision AI
    if args.render_images:
        rendered = render_pdf_images(pdf_path, args.render_images, page_list=page_list, dpi=args.dpi)
        print(f"Rendered {len(rendered)} page images to: {args.render_images}", file=sys.stderr)

    md_text = ""
    # 1. Try digital text extraction first (unless --ocr is forced)
    if not args.ocr:
        try:
            md_text = pymupdf4llm.to_markdown(
                str(pdf_path),
                pages=page_list,
                page_chunks=False,
                margins=args.margins
            )
        except Exception as e:
            print(f"[Notice] Digital extraction error: {e}. Falling back to OCR...", file=sys.stderr)
            md_text = ""

    # 2. If no digital text (scanned PDF) or --ocr forced, run RapidOCR
    if not md_text.strip():
        print(f"[Notice] Scanned PDF detected (no digital text layer). Running RapidOCR...", file=sys.stderr)
        md_text = run_ocr_on_pdf(pdf_path, page_list=page_list, dpi=args.dpi)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_text)
        print(f"Successfully saved Markdown to: {out_path} ({len(md_text)} chars)", file=sys.stderr)
    else:
        print(md_text)


if __name__ == "__main__":
    main()
