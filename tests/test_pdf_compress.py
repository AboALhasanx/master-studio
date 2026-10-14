"""Contract tests for the local PDF compressor and its verification gate.

The point of `pdf_compress.py` is that it may *only* win size by re-encoding
oversized images — never by dropping pages, text, links or visual fidelity. These
tests pin exactly that: a compressed scanned-style PDF stays the same document,
and the gate refuses a candidate that is not the same document.

A scanned-style page is synthesised here: a 300-DPI raster of the page plus a real
text layer, which is the shape of the lecture scans the tool was written for.
"""

import sys
from pathlib import Path

import pymupdf

BASE_DIR = Path(__file__).resolve().parent.parent
TOOLS = BASE_DIR / "90_Shared_Toolbox" / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import pdf_compress  # noqa: E402


def _scanned_like_pdf(path, pages=2, dpi=300):
    """Build a page-image + text-layer PDF, mimicking a phone scan."""
    rendered = pymupdf.open()
    for i in range(pages):
        page = rendered.new_page(width=595, height=842)
        page.insert_text((72, 120), f"Page {i + 1} searchable text", fontsize=14)
        page.draw_rect(pymupdf.Rect(60, 60, 535, 782), color=(0, 0, 0), width=1)

    doc = pymupdf.open()
    for i in range(pages):
        pix = rendered[i].get_pixmap(dpi=dpi)
        page = doc.new_page(width=595, height=842)
        page.insert_image(page.rect, pixmap=pix)
        page.insert_text((72, 120), f"Page {i + 1} searchable text", fontsize=14)
    doc.save(str(path))
    doc.close()
    rendered.close()
    return path


def test_compression_shrinks_the_file_and_keeps_the_document(tmp_path):
    src = _scanned_like_pdf(tmp_path / "scan.pdf")
    out = tmp_path / "scan-light.pdf"

    report = pdf_compress.compress(src, out, quality=85)

    assert report["accepted"], report["failed"]
    assert report["images_downsampled"] >= 1, "no oversized image was touched"
    assert report["after_bytes"] < report["before_bytes"], "compression saved nothing"
    assert all(check["passed"] for check in report["checks"])

    before = pymupdf.open(str(src))
    after = pymupdf.open(str(out))
    assert after.page_count == before.page_count
    assert [after[i].get_text() for i in range(after.page_count)] == \
           [before[i].get_text() for i in range(before.page_count)]
    before.close()
    after.close()


def test_gate_rejects_a_candidate_that_is_not_the_same_document(tmp_path):
    src = _scanned_like_pdf(tmp_path / "scan.pdf", pages=2)

    other = pymupdf.open(str(src))
    other.new_page(width=595, height=842)          # an extra page: not the same file
    other.save(str(tmp_path / "tampered.pdf"))
    other.close()

    checks, _worst, _pages = pdf_compress.verify(src, tmp_path / "tampered.pdf")
    failed = [name for name, passed, _ in checks if not passed]
    assert "page count unchanged" in failed


def test_gate_rejects_an_over_shrunk_candidate(tmp_path):
    """Regression: Pixmap.shrink(n) divides by 2**n, which once turned 244-DPI
    scans into 61-DPI mush that still passed a coarse check. The gate must catch
    a candidate whose images fall below the requested target DPI."""
    src = _scanned_like_pdf(tmp_path / "scan.pdf", pages=2)
    over_shrunk = tmp_path / "over-shrunk.pdf"

    pdf_compress._image_pass(src, over_shrunk, 170, 75, 85)      # 75 dpi: far too low

    checks, _worst, _pages = pdf_compress.verify(src, over_shrunk, 1.5, 5.0, dpi_target=150)
    failed = [name for name, passed, _ in checks if not passed]
    assert any("image resolution honoured" in name for name in failed), failed


def test_compressed_images_keep_the_requested_resolution(tmp_path):
    src = _scanned_like_pdf(tmp_path / "scan.pdf", pages=2)
    out = tmp_path / "scan-light.pdf"

    report = pdf_compress.compress(src, out, dpi_target=150, quality=85)
    assert report["accepted"], report["failed"]

    src_doc = pymupdf.open(str(src))
    out_doc = pymupdf.open(str(out))
    pairs = pdf_compress._resolution_pairs(src_doc, out_doc, 170)
    src_doc.close()
    out_doc.close()

    assert pairs, "the fixture should have oversized images"
    assert all(after is not None and after >= 150 * 0.9 for _page, _before, after in pairs), pairs


def test_images_below_the_threshold_are_left_alone(tmp_path):
    """A file whose images are already light must survive untouched in size."""
    src = _scanned_like_pdf(tmp_path / "scan.pdf", pages=1, dpi=100)
    out = tmp_path / "scan-light.pdf"

    report = pdf_compress.compress(src, out, quality=85)

    assert report["accepted"], report["failed"]
    assert report["images_downsampled"] == 0
    assert report["after_mb"] <= report["before_mb"] + 0.05


def test_inspect_lists_every_image(tmp_path):
    src = _scanned_like_pdf(tmp_path / "scan.pdf", pages=3)
    doc = pymupdf.open(str(src))
    rows = pdf_compress.image_report(doc)
    doc.close()

    assert len(rows) == 3
    assert {row["page"] for row in rows} == {1, 2, 3}
    assert all(row["dpi"] >= 250 for row in rows), "fixture should look like a 300-DPI scan"
