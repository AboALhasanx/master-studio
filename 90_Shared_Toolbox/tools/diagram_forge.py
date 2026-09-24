#!/usr/bin/env python3
"""
diagram_forge.py — Master Studio High-Resolution Vector Diagram Renderer
========================================================================

Renders a self-contained HTML/SVG diagram into a crisp 2x-retina PNG for
embedding in academic study notes and PDFs.

Why this exists
---------------
The Academic Study Note SOP forbids ASCII art and blurry PDF screenshots.
Every structural hierarchy, state transition, or process workflow must be
rendered as a clean vector graphic at 2x retina scale.

Usage
-----
    python diagram_forge.py <input.html> <output.png> [--width 1080] [--scale 2]

    # or render straight from a heredoc / pipe
    python diagram_forge.py - <output.png> --width 1080 < diagram.html

Requirements
------------
Playwright + Chromium (already present for pdf_exporter.py). This script
auto-discovers the Chromium binary the same way pdf_exporter.py does.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

DEFAULT_WIDTH = 1080
DEFAULT_SCALE = 2


def find_chromium_binary() -> str | None:
    """Locate a full Chromium binary, mirroring pdf_exporter.py's resolver.

    Note: Playwright's *headless shell* build cannot be launched via
    `chromium.launch()` in every version, so we prefer the full
    `chromium-*/chrome-win64/chrome.exe` build and fall back to Edge/Chrome.
    """
    local_app = os.environ.get("LOCALAPPDATA", "")
    if local_app:
        pw_dir = Path(local_app) / "ms-playwright"
        if pw_dir.exists():
            for chrome_exe in sorted(pw_dir.glob("chromium-*/chrome-win64/chrome.exe"), reverse=True):
                if chrome_exe.exists():
                    return str(chrome_exe)

    pf = os.environ.get("ProgramFiles", r"C:\Program Files")
    pf86 = os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")
    candidates = [
        Path(pf86) / "Microsoft" / "EdgeCore" / "Optimized" / "msedge.exe",
        Path(pf86) / "Microsoft" / "Edge" / "Application" / "msedge.exe",
        Path(pf) / "Microsoft" / "Edge" / "Application" / "msedge.exe",
        Path(pf) / "Google" / "Chrome" / "Application" / "chrome.exe",
        Path(pf86) / "Google" / "Chrome" / "Application" / "chrome.exe",
    ]
    for c in candidates:
        if c.exists():
            return str(c)

    for name in ["msedge", "chrome", "google-chrome", "chromium"]:
        p = shutil.which(name)
        if p and Path(p).exists():
            return p
    return None


def render(html: str, out_path: Path, width: int, scale: int) -> None:
    from playwright.sync_api import sync_playwright

    out_path.parent.mkdir(parents=True, exist_ok=True)
    chromium = find_chromium_binary()

    with sync_playwright() as p:
        launch_kwargs: dict = {"args": ["--font-render-hinting=none", "--force-color-profile=srgb"]}
        if chromium:
            launch_kwargs["executable_path"] = chromium
        browser = p.chromium.launch(**launch_kwargs)
        page = browser.new_page(
            viewport={"width": width, "height": 800},
            device_scale_factor=scale,
        )
        page.set_content(html, wait_until="networkidle")
        page.wait_for_timeout(450)  # let webfonts / layout settle
        el = page.query_selector("#diagram") or page.query_selector("body")
        assert el is not None
        el.screenshot(path=str(out_path), omit_background=False)
        browser.close()

    size_kb = out_path.stat().st_size / 1024
    print(f"[diagram_forge] wrote {out_path}  ({size_kb:.1f} KB @ {scale}x)")


def main() -> int:
    ap = argparse.ArgumentParser(description="Render HTML/SVG diagram to 2x-retina PNG")
    ap.add_argument("input", help="Path to HTML file, or '-' to read stdin")
    ap.add_argument("output", help="Destination .png path")
    ap.add_argument("--width", type=int, default=DEFAULT_WIDTH, help="Viewport width in CSS px")
    ap.add_argument("--scale", type=int, default=DEFAULT_SCALE, help="Device scale factor")
    args = ap.parse_args()

    if args.input == "-":
        html = sys.stdin.read()
    else:
        html = Path(args.input).read_text(encoding="utf-8")

    render(html, Path(args.output), args.width, args.scale)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
