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
def extract_embedded_images(pdf_path, out_dir, min_dim=80):
    """
    Extracts embedded figures, charts, and diagrams from the PDF into out_dir.
    Filters out tiny decorative lines/dots (<80px).
    """
    doc = pymupdf.open(str(pdf_path))
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    extracted_files = []
    seen_xrefs = set()

    for pno in range(len(doc)):
        page = doc[pno]
        image_list = page.get_images(full=True)

        for img_idx, img_info in enumerate(image_list):
            xref = img_info[0]
            if xref in seen_xrefs:
                continue
            seen_xrefs.add(xref)

            try:
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                width = base_image["width"]
                height = base_image["height"]

                # Filter out tiny decorative icons/dots
                if width < min_dim or height < min_dim:
                    continue

                img_name = f"fig_p{pno + 1:02d}_{img_idx + 1:02d}_{width}x{height}.{image_ext}"
                target_file = out_path / img_name
                with open(target_file, "wb") as f:
                    f.write(image_bytes)
                extracted_files.append(target_file)
            except Exception:
                continue

    return extracted_files


def main():
    parser = argparse.ArgumentParser(description="Master Studio PDF Reader (PDF -> Clean Markdown + OCR)")
    parser.add_argument("pdf", help="Path to input PDF file")
    parser.add_argument("-o", "--output", help="Path to output Markdown file (default: stdout)")
    parser.add_argument("-p", "--pages", help="Pages to extract, e.g. '1-5' or '1,3,5' (1-based)")
    parser.add_argument("--ocr", action="store_true", help="Force OCR mode even if digital text is present")
    parser.add_argument("--render-images", help="Directory path to save high-res PNGs for Vision AI")
    parser.add_argument("--extract-images", help="Directory path to extract all embedded figures, charts, and diagrams")
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
    # Optional: Extract embedded figures and charts
    if args.extract_images:
        extracted = extract_embedded_images(pdf_path, args.extract_images)
        print(f"Extracted {len(extracted)} embedded figures/diagrams to: {args.extract_images}", file=sys.stderr)

    md_text = ""
    # 1. Try digital text extraction first (unless --ocr is forced)
    if not args.ocr:
        try:
            extra_kwargs = {}
            if args.extract_images:
                extra_kwargs["write_images"] = True
                extra_kwargs["image_path"] = args.extract_images

            md_text = pymupdf4llm.to_markdown(
                str(pdf_path),
                pages=page_list,
                page_chunks=False,
                margins=args.margins,
                **extra_kwargs
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
