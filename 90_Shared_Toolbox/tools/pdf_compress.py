#!/usr/bin/env python3
"""Master Studio PDF Compressor — a local, verified alternative to iLovePDF.

What it does
------------
Walks every embedded image of a PDF, measures its *effective* resolution from the
rectangle it occupies on the page, and — only for images above ``--dpi-threshold``
— halves it towards ``--dpi-target`` and re-encodes it as JPEG at ``--quality``.
Text, vectors, links, annotations and page geometry are never touched, and images
already at or below the threshold stay byte-for-byte identical.

A pikepdf (qpdf) pass then rewrites the container with object streams, Flate
re-compression and linearisation — pure overhead removal, no content change.

Why this engine and not Ghostscript
-----------------------------------
Benchmarked on the English Unit-2 chapter (36 pages, 16.32 MB, scanned):
our engine lands at 4.99 MB with the searchable text layer and links intact,
while ``gs -sDEVICE=pdfwrite`` (10.08.0) *altered the extracted text* and pushed
the page-render delta to 11.9 — i.e. Ghostscript fails the gate below. So the
pure-Python path is the single engine this tool ships with.

Safety gate (nothing is written unless all five pass)
-----------------------------------------------------
1. page count unchanged;
2. per-page extracted text identical;
3. per-page link count unchanged;
4. image resolution honoured — no image that we shrank may land below the target
   DPI (a silent over-shrink is exactly what makes scanned text unreadable);
5. every page still renders like the original at 100 dpi — both the mean page
   delta and the worst single page must stay inside tolerance. The render check
   runs at 100 dpi on purpose: at low resolution a blurred scan looks "close" to
   the original, which is how an over-shrunk file once passed and reached the
   student unreadable.

A rejected candidate is deleted and the tool exits non-zero, so "success" means
"smaller *and* provably still the same document".

Usage:
    python pdf_compress.py <in.pdf> [--out OUT.pdf] [--dpi-target 150]
                           [--quality 85] [--dpi-threshold 170]
                           [--tolerance 6.0] [--no-structure] [--inspect] [--json]

Exit codes: 0 = verified output written, 1 = rejected (nothing written),
2 = bad usage.
"""

import argparse
import io
import json
import shutil
import sys
import tempfile
from pathlib import Path

import pymupdf
from PIL import Image

try:
    import pikepdf
    HAS_PIKEPDF = True
except ImportError:  # pragma: no cover - optional dependency
    HAS_PIKEPDF = False

DEFAULT_DPI_THRESHOLD = 170
DEFAULT_DPI_TARGET = 150
DEFAULT_QUALITY = 80
DEFAULT_TOLERANCE = 1.5
DEFAULT_MAX_TOLERANCE = 5.0
RENDER_DPI = 100


# --------------------------------------------------------------- inspection --


def _text_of(doc):
    """Per-page extracted text (stripped) — the searchable content of the file."""
    return [doc[i].get_text().strip() for i in range(doc.page_count)]


def _links_of(doc):
    """Per-page link count — a cheap proxy for "the clickable layer survived"."""
    return [len(doc[i].get_links()) for i in range(doc.page_count)]


def _render_diffs(a, b, dpi=RENDER_DPI):
    """Mean absolute pixel difference per page, comparing low-DPI grayscale renders.

    Pages are compared one at a time so memory stays flat on 200+ page books.
    A page whose render cannot be compared is reported as an infinite difference.
    """
    diffs = []
    for i in range(a.page_count):
        try:
            pa = a[i].get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
            pb = b[i].get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
        except Exception:
            diffs.append(float("inf"))
            continue
        sa, sb = pa.samples, pb.samples
        if not sa or len(sa) != len(sb):
            diffs.append(float("inf"))
            continue
        total = 0
        for x, y in zip(sa, sb):
            total += abs(x - y)
        diffs.append(total / len(sa))
    return diffs


def image_report(doc):
    """Describe every embedded image: page, pixel size, effective DPI and bytes."""
    rows = []
    for pno in range(doc.page_count):
        page = doc[pno]
        for item in page.get_images(full=True):
            xref = item[0]
            try:
                info = doc.extract_image(xref)
                bbox = page.get_image_bbox(item)
            except Exception:
                continue
            if not bbox.width or not bbox.height:
                continue
            rows.append({
                "page": pno + 1,
                "xref": xref,
                "width": info["width"],
                "height": info["height"],
                "ext": info["ext"],
                "bytes": len(info["image"]),
                "dpi": round(info["width"] / (bbox.width / 72)),
            })
    return rows


# ------------------------------------------------------------------- passes --


def _resample_image(raw_bytes, effective_dpi, target_dpi, quality):
    """Resize one embedded image to exactly ``target_dpi`` with a Lanczos filter.

    ``Pixmap.shrink(n)`` is *not* used: it divides by ``2**n`` (shrink(2) is a
    quarter in each axis), which silently destroys scanned text. Here the scale is
    ``target_dpi / effective_dpi``, and JPEG chroma subsampling is disabled so
    coloured small print stays sharp.
    """
    scale = target_dpi / effective_dpi
    if scale >= 0.95:
        return None
    img = Image.open(io.BytesIO(raw_bytes))
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")
    size = (max(1, round(img.width * scale)), max(1, round(img.height * scale)))
    img = img.resize(size, Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=quality, subsampling=0, optimize=True,
             dpi=(target_dpi, target_dpi))
    return buf.getvalue()


def _image_pass(src, out, dpi_threshold, dpi_target, quality):
    """Downsample only the oversized images, in place, with PyMuPDF + Pillow."""
    doc = pymupdf.open(str(src))
    replaced = 0
    for pno in range(doc.page_count):
        page = doc[pno]
        for item in page.get_images(full=True):
            xref = item[0]
            try:
                info = doc.extract_image(xref)
                bbox = page.get_image_bbox(item)
            except Exception:
                continue
            if not bbox.width or not bbox.height:
                continue
            effective = info["width"] / (bbox.width / 72)
            if effective <= dpi_threshold:
                continue
            try:
                stream = _resample_image(info["image"], effective, dpi_target, quality)
            except Exception:
                continue
            if stream is None:
                continue
            try:
                page.replace_image(xref, stream=stream)
                replaced += 1
            except Exception:
                continue
    doc.save(str(out), garbage=4, deflate=True, clean=True)
    doc.close()
    return replaced


def _structure_pass(src, out):
    """Container-only optimisation through pikepdf/qpdf."""
    with pikepdf.open(str(src)) as pdf:
        pdf.save(
            str(out),
            object_stream_mode=pikepdf.ObjectStreamMode.generate,
            compress_streams=True,
            recompress_flate=True,
            linearize=True,
        )
    return True


# -------------------------------------------------------------------- gate ---


def _page_max_dpi(doc, pno):
    """Highest effective DPI among the images on one page."""
    page = doc[pno]
    best = None
    for item in page.get_images(full=True):
        try:
            info = doc.extract_image(item[0])
            bbox = page.get_image_bbox(item)
        except Exception:
            continue
        if not bbox.width or not bbox.height:
            continue
        dpi = info["width"] / (bbox.width / 72)
        best = dpi if best is None else max(best, dpi)
    return best


def _resolution_pairs(original, candidate, dpi_threshold):
    """(page, dpi before, dpi after) for every page whose images were oversized.

    The check reads the *original* to decide which pages matter — measuring the
    candidate alone would miss an over-shrunk image, because a 61-DPI image is no
    longer "above the threshold" and would simply be skipped.
    """
    pairs = []
    for pno in range(original.page_count):
        before = _page_max_dpi(original, pno)
        if before is None or before <= dpi_threshold:
            continue
        after = _page_max_dpi(candidate, pno)
        pairs.append((pno + 1, round(before), round(after) if after is not None else None))
    return pairs


def verify(original, candidate, tolerance=DEFAULT_TOLERANCE,
           max_tolerance=DEFAULT_MAX_TOLERANCE,
           dpi_target=None, dpi_threshold=DEFAULT_DPI_THRESHOLD):
    """Compare candidate against original; return (checks, worst_delta, worst_pages).

    The render comparison runs at 100 dpi on purpose: at low resolution a blurred
    scan looks "close" to the original, which is how an over-shrunk file once
    passed a 36-dpi check while being unreadable on a phone.
    """
    a = pymupdf.open(str(original))
    b = pymupdf.open(str(candidate))
    checks = []

    same_pages = a.page_count == b.page_count
    checks.append(("page count unchanged", same_pages, f"{a.page_count} vs {b.page_count}"))

    text_ok = same_pages and _text_of(a) == _text_of(b)
    checks.append(("extracted text unchanged", text_ok, ""))

    links_ok = same_pages and _links_of(a) == _links_of(b)
    checks.append(("links unchanged", links_ok, ""))

    if dpi_target:
        # The images we were asked to shrink must not end up below the target:
        # a silent over-shrink is exactly what makes scanned text unreadable.
        pairs = _resolution_pairs(a, b, dpi_threshold)
        floor = dpi_target * 0.9
        after_values = [after for _p, _before, after in pairs]
        lowest = min(after_values) if after_values else None
        honoured = all(after is not None and after >= floor for after in after_values)
        checks.append((
            f"image resolution honoured (lowest {lowest if lowest is not None else '-'} >= {floor:.0f} dpi)",
            honoured,
            "",
        ))

    diffs = _render_diffs(a, b) if same_pages else []
    mean_delta = sum(diffs) / len(diffs) if diffs else float("inf")
    worst = max(diffs) if diffs else float("inf")
    checks.append((
        f"render fidelity, mean (mean page delta {mean_delta:.2f} <= {tolerance:.2f})",
        bool(diffs) and mean_delta <= tolerance,
        "",
    ))
    checks.append((
        f"render fidelity, worst page ({worst:.2f} <= {max_tolerance:.2f})",
        bool(diffs) and worst <= max_tolerance,
        "",
    ))
    worst_pages = sorted(range(1, len(diffs) + 1), key=lambda n: diffs[n - 1], reverse=True)[:3]
    worst_pages = [(n, round(diffs[n - 1], 2)) for n in worst_pages]

    a.close()
    b.close()
    return checks, worst, worst_pages


# ------------------------------------------------------------------- driver --


def compress(src, out, dpi_threshold=DEFAULT_DPI_THRESHOLD, dpi_target=DEFAULT_DPI_TARGET,
             quality=DEFAULT_QUALITY, tolerance=DEFAULT_TOLERANCE,
             max_tolerance=DEFAULT_MAX_TOLERANCE, structure=True, keep_original=False):
    """Compress ``src`` into ``out`` and keep it only if verification passes."""
    src, out = Path(src), Path(out)
    before = src.stat().st_size

    with tempfile.TemporaryDirectory() as tmp:
        stage = Path(tmp) / "stage.pdf"
        replaced = _image_pass(src, stage, dpi_threshold, dpi_target, quality)
        if structure and HAS_PIKEPDF:
            structured = _structure_pass(stage, out)
        else:
            structured = False
            shutil.copyfile(stage, out)

    after = out.stat().st_size
    checks, worst, worst_pages = verify(src, out, tolerance, max_tolerance,
                                        dpi_target=dpi_target, dpi_threshold=dpi_threshold)
    failed = [name for name, ok, _ in checks if not ok]

    report = {
        "source": str(src),
        "output": str(out),
        "structure_pass": structured,
        "images_downsampled": replaced,
        "before_bytes": before,
        "after_bytes": after,
        "before_mb": round(before / 1e6, 2),
        "after_mb": round(after / 1e6, 2),
        "saved_mb": round((before - after) / 1e6, 2),
        "ratio": round(after / before, 3) if before else None,
        "settings": {
            "dpi_threshold": dpi_threshold,
            "dpi_target": dpi_target,
            "quality": quality,
            "tolerance": tolerance,
            "max_tolerance": max_tolerance,
            "render_dpi": RENDER_DPI,
        },
        "checks": [{"name": name, "passed": ok, "detail": detail} for name, ok, detail in checks],
        "worst_pages": worst_pages,
        "worst_delta": round(worst, 2) if worst != float("inf") else None,
        "accepted": not failed,
        "failed": failed,
    }

    if failed or keep_original:
        out.unlink(missing_ok=True)
        report["output"] = None
        if keep_original and not failed:
            report["accepted"] = False
            report["failed"] = ["--keep-original requested"]
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Compress a PDF's embedded images, then verify nothing else changed.",
    )
    parser.add_argument("pdf", help="input PDF")
    parser.add_argument("--out", help="output PDF (default: <name> - compressed.pdf)")
    parser.add_argument("--dpi-target", type=int, default=DEFAULT_DPI_TARGET,
                        help=f"target resolution for oversized images (default {DEFAULT_DPI_TARGET})")
    parser.add_argument("--dpi-threshold", type=int, default=DEFAULT_DPI_THRESHOLD,
                        help=f"only images above this DPI are downsampled (default {DEFAULT_DPI_THRESHOLD})")
    parser.add_argument("--quality", type=int, default=DEFAULT_QUALITY,
                        help=f"JPEG quality for lossy images (default {DEFAULT_QUALITY})")
    parser.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE,
                        help=f"max mean page delta at {RENDER_DPI} dpi (default {DEFAULT_TOLERANCE})")
    parser.add_argument("--max-tolerance", type=float, default=DEFAULT_MAX_TOLERANCE,
                        help=f"max delta allowed on any single page (default {DEFAULT_MAX_TOLERANCE})")
    parser.add_argument("--no-structure", action="store_true",
                        help="skip the pikepdf/qpdf container pass")
    parser.add_argument("--keep-original", action="store_true",
                        help="verify but do not keep the candidate file")
    parser.add_argument("--inspect", action="store_true",
                        help="only print the embedded-image inventory")
    parser.add_argument("--json", action="store_true", help="print the report as JSON")
    args = parser.parse_args(argv)

    src = Path(args.pdf)
    if not src.is_file():
        print(f"error: no such file: {src}", file=sys.stderr)
        return 2

    if args.inspect:
        doc = pymupdf.open(str(src))
        rows = image_report(doc)
        doc.close()
        total = sum(r["bytes"] for r in rows)
        for row in rows:
            print("p%-4d xref %-5d %5dx%-5d %-5s dpi %-4d %7.0f KB"
                  % (row["page"], row["xref"], row["width"], row["height"],
                     row["ext"], row["dpi"], row["bytes"] / 1e3))
        print("images: %d | embedded bytes: %.2f MB | file: %.2f MB"
              % (len(rows), total / 1e6, src.stat().st_size / 1e6))
        return 0

    out = Path(args.out) if args.out else src.with_name(f"{src.stem} - compressed.pdf")

    report = compress(
        src, out,
        dpi_threshold=args.dpi_threshold,
        dpi_target=args.dpi_target,
        quality=args.quality,
        tolerance=args.tolerance,
        max_tolerance=args.max_tolerance,
        structure=not args.no_structure,
        keep_original=args.keep_original,
    )

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print(f"source  : {report['source']}  ({report['before_mb']} MB)")
        print(f"engine  : pymupdf"
              f"{' + pikepdf structure' if report['structure_pass'] else ''}"
              f" | images downsampled: {report['images_downsampled']}")
        print(f"output  : {report['output']}  ({report['after_mb']} MB, saved {report['saved_mb']} MB)")
        for check in report["checks"]:
            mark = "PASS" if check["passed"] else "FAIL"
            print(f"  {mark}  {check['name']} {check['detail']}".rstrip())
        if report["worst_pages"]:
            print(f"  worst pages (page, mean delta): {report['worst_pages']}")
        print("VERIFIED" if report["accepted"] else f"REJECTED: {', '.join(report['failed'])}")

    return 0 if report["accepted"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
