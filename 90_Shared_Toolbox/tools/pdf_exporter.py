# -*- coding: utf-8 -*-
"""Master Studio Academic PDF Exporter.

Local-first, high-fidelity academic PDF generator optimized for Arabic/BiDi,
LaTeX math, embedded diagrams, and Master Studio pedagogical callouts.
Powered by Playwright Headless Chromium (DirectWrite / HarfBuzz).

Usage:
    python pdf_exporter.py path/to/note.md [options]

Options:
    -o, --output PATH       Destination PDF path (defaults to same name as input)
    -t, --template NAME     Template preset: study_pack (default), booklet, exam_sheet, glossary
    --lang {ar,en,bilingual} Document primary language (default: auto-detected)
    --course NAME           Course title / code override
    --prof NAME             Instructor name override
    --term NAME             Academic term (default: Fall 2026)
    --open                  Open generated PDF in system viewer upon completion
"""

import argparse
import asyncio
import base64
import html as H
import mimetypes
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import markdown

# ---------------------------------------------------------------------------
# Browser Discovery
# ---------------------------------------------------------------------------

def find_chromium_binary() -> str:
    """Finds a working Chromium or Edge executable on the local system."""
    # 1. Playwright installed Chromium in LOCALAPPDATA
    local_app = os.environ.get("LOCALAPPDATA", "")
    if local_app:
        pw_dir = Path(local_app) / "ms-playwright"
        if pw_dir.exists():
            for chrome_exe in pw_dir.glob("chromium-*/chrome-win64/chrome.exe"):
                if chrome_exe.exists():
                    return str(chrome_exe)

    # 2. Windows EdgeCore / Edge / Chrome standard locations
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

    # 3. Search PATH
    for name in ["msedge", "chrome", "google-chrome", "chromium"]:
        p = shutil.which(name)
        if p and Path(p).exists():
            return p

    raise RuntimeError(
        "No Chromium or Edge binary found. Please install Playwright browsers or Microsoft Edge."
    )


# ---------------------------------------------------------------------------
# Arabic & BiDi Text Processing
# ---------------------------------------------------------------------------

ARABIC_RE = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]")

def has_arabic(text: str) -> bool:
    """Checks if text contains Arabic characters."""
    return bool(ARABIC_RE.search(text))


def isolate_english_tokens_in_arabic(text: str) -> str:
    """Wraps isolated English technical terms inside Arabic sentences in <bdi dir='ltr'>.
    
    Prevents BiDi punctuation flipping (e.g. periods, parentheses, brackets, colons).
    Does NOT touch HTML tags, attributes, math blocks ($...$), or code spans (`...`).
    """
    if not has_arabic(text):
        return text

    split_pat = re.compile(
        r"("
        r"@@MATH_[A-Z0-9_]+@@|"
        r"<span class=[\"']math-inline[\"'][^>]*>.*?</span>|"
        r"<div class=[\"']math-block[\"'][^>]*>.*?</div>|"
        r"<[^>]+>|"
        r"&[a-zA-Z0-9#]+;|"
        r"`[^`]+`|"
        r"\$\$[\s\S]+?\$\$|"
        r"(?<!\$)\$[^\$\n]+?\$(?!\$)"
        r")",
        re.DOTALL
    )
    tokens = split_pat.split(text)
    result = []
    en_phrase_re = re.compile(r"\b([A-Za-z][A-Za-z0-9_\-\.\s/\'’]{1,50}[A-Za-z0-9])\b")

    for token in tokens:
        if split_pat.fullmatch(token):
            result.append(token)
        else:
            def _replace_en(m):
                word = m.group(1).strip()
                if word.startswith("&") or word.isdigit():
                    return m.group(0)
                return f'<bdi class="en-token" dir="ltr">{word}</bdi>'

            transformed = en_phrase_re.sub(_replace_en, token)
            result.append(transformed)
    return "".join(result)

def tag_bilingual_blocks(html_text: str) -> str:
    """Tags block elements (headings, paragraphs, blockquotes, lists) as LTR if they contain no Arabic."""
    def _fix_tag(m):
        tag = m.group(1)
        attrs = m.group(2) or ""
        content = m.group(3)
        closing = m.group(4)
        if 'dir=' in attrs:
            return m.group(0)
        inner_text = re.sub(r'<[^>]+>', '', content)
        if inner_text.strip() and not has_arabic(inner_text):
            return f'<{tag}{attrs} dir="ltr" class="ltr-block">{content}{closing}'
        return m.group(0)

    pattern = r'<(h[1-6]|p|blockquote|li|table)(\s*[^>]*)>(.*?)(</\1>)'
    return re.sub(pattern, _fix_tag, html_text, flags=re.DOTALL)


# ---------------------------------------------------------------------------
# Callout Card Transformation (Obsidian / Master Studio Syntax)
# ---------------------------------------------------------------------------

CALLOUT_CONFIGS = {
    "TRAP": {
        "class": "trap",
        "title_ar": "فخ الامتحان مع أ.م.د. علي فاهم (Professor's Exam Trap)",
        "title_en": "Professor's Exam Trap",
        "icon": "⚠️",
        "color": "#dc2626"
    },
    "EXAM": {
        "class": "trap",
        "title_ar": "فخ الامتحان مع الأستاذ (Professor's Exam Trap)",
        "title_en": "Professor's Exam Trap",
        "icon": "⚠️",
        "color": "#dc2626"
    },
    "FEYNMAN": {
        "class": "feynman",
        "title_ar": "تبسيط فاينمان للطفل بعمر 9 سنوات (Feynman 9-Year-Old Analogy)",
        "title_en": "Feynman 9-Year-Old Analogy",
        "icon": "💡",
        "color": "#0d9488"
    },
    "CONCEPT": {
        "class": "concept",
        "title_ar": "المفهوم الأكاديمي التأسيسي (Foundational Concept)",
        "title_en": "Foundational Concept",
        "icon": "📘",
        "color": "#2563eb"
    },
    "NOTE": {
        "class": "concept",
        "title_ar": "ملاحظة أكاديمية هامة (Academic Note)",
        "title_en": "Academic Note",
        "icon": "📝",
        "color": "#2563eb"
    },
    "CALC": {
        "class": "calc",
        "title_ar": "الاشتقاق والحسابات الرياضية (Mathematical Derivation)",
        "title_en": "Mathematical Derivation",
        "icon": "📐",
        "color": "#d97706"
    },
    "MATH": {
        "class": "calc",
        "title_ar": "النموذج الرياضي والبرهان (Mathematical Proof)",
        "title_en": "Mathematical Proof",
        "icon": "📐",
        "color": "#d97706"
    },
    "WARN": {
        "class": "warn",
        "title_ar": "تحذير ومغالطة شائعة (Common Fallacy / Warning)",
        "title_en": "Common Fallacy / Warning",
        "icon": "⚡",
        "color": "#b91c1c"
    },
    "WARNING": {
        "class": "warn",
        "title_ar": "تحذير ومغالطة شائعة (Common Fallacy / Warning)",
        "title_en": "Common Fallacy / Warning",
        "icon": "⚡",
        "color": "#b91c1c"
    },
    "TIP": {
        "class": "feynman",
        "title_ar": "إضاءة سريعة وتلميح هندسي (Engineering Tip)",
        "title_en": "Engineering Tip",
        "icon": "✨",
        "color": "#0d9488"
    }
}


def transform_callouts(md_text: str, default_lang: str = "ar") -> str:
    """Transforms blockquote callouts (> [!TYPE] Title) into styled HTML cards."""
    lines = md_text.splitlines()
    output_lines = []
    in_callout = False
    callout_type = ""
    callout_custom_title = ""
    callout_body: List[str] = []

    callout_start_re = re.compile(r"^>\s*\[!([A-Za-z0-9_-]+)\](?:\s*(.*))?$")

    for line in lines:
        m = callout_start_re.match(line)
        if m:
            # If already in a callout, flush it
            if in_callout:
                output_lines.append(_render_callout(callout_type, callout_custom_title, callout_body, default_lang))
                callout_body = []
            in_callout = True
            callout_type = m.group(1).upper()
            callout_custom_title = (m.group(2) or "").strip()
            continue

        if in_callout:
            if line.startswith(">"):
                # strip leading '>' and optional space
                content = re.sub(r"^>\s?", "", line)
                callout_body.append(content)
            elif not line.strip():
                # blank line might be inside callout
                callout_body.append("")
            else:
                # end of callout block
                output_lines.append(_render_callout(callout_type, callout_custom_title, callout_body, default_lang))
                in_callout = False
                callout_body = []
                output_lines.append(line)
        else:
            output_lines.append(line)

    if in_callout:
        output_lines.append(_render_callout(callout_type, callout_custom_title, callout_body, default_lang))

    return "\n".join(output_lines)


def _render_callout(kind: str, custom_title: str, body_lines: List[str], lang: str) -> str:
    cfg = CALLOUT_CONFIGS.get(kind, CALLOUT_CONFIGS["NOTE"])
    default_title = cfg["title_ar"] if lang == "ar" else cfg["title_en"]
    title = custom_title if custom_title else default_title
    
    # Process markdown inside callout body
    body_md = "\n".join(body_lines).strip()
    body_html = markdown.markdown(body_md, extensions=["tables", "fenced_code"])
    
    return f"""
<div class="callout {cfg['class']}">
  <div class="callout-title">
    <span class="callout-icon">{cfg['icon']}</span>
    <span>{H.escape(title)}</span>
  </div>
  <div class="callout-body">
    {body_html}
  </div>
</div>
"""


def transform_qa_cards(html_text: str, default_lang: str = "ar") -> str:
    """Transforms active recall Q&A pairs into dedicated assessment cards distinct from quotes."""
    qa_pattern = re.compile(
        r"<p><strong>((?:Q\d*[:\.\)]|\d+[\.\)]|س\d*[:\.\)]|سؤال[:\.\)]).*?)</strong></p>\s*<blockquote(?:\s*[^>]*)>(.*?)</blockquote>",
        re.DOTALL
    )

    def _replace_qa(m):
        q_raw = m.group(1).strip()
        ans_raw = m.group(2).strip()

        # Extract number if present
        num_m = re.match(r"^((?:Q\d*|\d+|س\d*))[\.\):\-]\s*(.*)$", q_raw)
        if num_m:
            badge_text = num_m.group(1)
            q_text = num_m.group(2)
        else:
            badge_text = "Q"
            q_text = q_raw

        # Determine language/direction of question and answer
        ans_inner = re.sub(r'<[^>]+>', '', ans_raw)
        ans_has_ar = has_arabic(ans_inner)
        ans_dir = "rtl" if ans_has_ar else "ltr"
        ans_class = "rtl-ans" if ans_has_ar else "ltr-ans"

        q_has_ar = has_arabic(q_text)
        q_dir = "rtl" if q_has_ar else "ltr"
        badge_ans_label = "نموذج الإجابة (Model Answer)" if ans_has_ar else "Model Answer"

        return f"""
<div class="qa-card">
  <div class="qa-question-box" dir="{q_dir}">
    <span class="qa-badge-q">{H.escape(badge_text)}</span>
    <div class="qa-question-text">{q_text}</div>
  </div>
  <div class="qa-answer-box {ans_class}" dir="{ans_dir}">
    <div class="qa-answer-content">{ans_raw}</div>
  </div>
</div>
"""

    return qa_pattern.sub(_replace_qa, html_text)


def trim_image_whitespace(img_bytes: bytes, pad: int = 6) -> bytes:
    """Auto-trims solid white or near-white margins from an image before inlining."""
    try:
        from io import BytesIO
        from PIL import Image, ImageChops
        im = Image.open(BytesIO(img_bytes))
        im_rgb = im.convert("RGB")
        bg = Image.new("RGB", im_rgb.size, (255, 255, 255))
        diff = ImageChops.difference(im_rgb, bg)
        bbox = diff.getbbox()
        if bbox:
            w, h = im.size
            # Only crop if at least 15px of whitespace exists on any side
            if (bbox[0] > 15 or bbox[1] > 15 or (w - bbox[2]) > 15 or (h - bbox[3]) > 15):
                x0 = max(0, bbox[0] - pad)
                y0 = max(0, bbox[1] - pad)
                x1 = min(w, bbox[2] + pad)
                y1 = min(h, bbox[3] + pad)
                trimmed = im_rgb.crop((x0, y0, x1, y1))
                out_io = BytesIO()
                trimmed.save(out_io, format="PNG", optimize=True)
                return out_io.getvalue()
    except Exception:
        pass
    return img_bytes


def inline_images_in_html(html_text: str, base_dir: Path) -> str:
    """Finds image tags and Markdown images, replacing local file paths with base64 data URIs.
    
    Supports:
      - Pipe width syntax: ![Caption|400](img.png) or ![Caption|60%](img.png)
      - HTML width/style attributes: <img src="..." width="350">
      - Whitespace auto-trimming (via Pillow)
      - Side-by-side figures via <div class="fig-row">
    """
    vault_root = Path(__file__).resolve().parents[2]

    def _replace_img(match):
        full_tag = match.group(0)
        src_match = re.search(r'src=["\']([^"\']+)["\']', full_tag)
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', full_tag)
        width_match = re.search(r'width=["\']([^"\']*)["\']', full_tag)

        if not src_match:
            return full_tag

        src = H.unescape(src_match.group(1).strip())
        alt_raw = alt_match.group(1).strip() if alt_match else ""

        # Parse pipe sizing syntax e.g. "Figure 1|350" or "Figure 1|50%"
        caption = alt_raw
        custom_width = ""
        if "|" in alt_raw:
            parts = alt_raw.rsplit("|", 1)
            caption = parts[0].strip()
            spec = parts[1].strip()
            if spec.isdigit():
                custom_width = f"max-width: {spec}px;"
            elif any(spec.endswith(unit) for unit in ["%", "px", "mm", "cm", "in", "pt"]):
                custom_width = f"max-width: {spec};"

        if not custom_width and width_match:
            w = width_match.group(1).strip()
            custom_width = f"max-width: {w if not w.isdigit() else w + 'px'};"

        # Skip already-inlined data URIs or remote URLs
        if src.startswith("data:") or src.startswith("http://") or src.startswith("https://"):
            return full_tag

        # Resolve image path:
        img_path = (base_dir / src).resolve()
        if not img_path.exists():
            alt_path = (vault_root / src).resolve()
            if alt_path.exists():
                img_path = alt_path
            else:
                direct_path = Path(src).resolve()
                if direct_path.exists():
                    img_path = direct_path

        if img_path.exists() and img_path.is_file():
            raw_b = img_path.read_bytes()
            # Trim dead white margins for bitmap images
            if img_path.suffix.lower() in [".png", ".jpg", ".jpeg"]:
                raw_b = trim_image_whitespace(raw_b)

            mime, _ = mimetypes.guess_type(str(img_path))
            if not mime:
                mime = "image/png"
            try:
                b64_data = base64.b64encode(raw_b).decode("ascii")
                data_uri = f"data:{mime};base64,{b64_data}"
                caption_html = f'<div class="figure-caption">{H.escape(caption)}</div>' if caption else ""
                box_style = f' style="{custom_width}"' if custom_width else ''
                return f'<div class="figure-box"{box_style}><img src="{data_uri}" alt="{H.escape(caption)}"/>{caption_html}</div>'
            except Exception as e:
                sys.stderr.write(f"Warning: Failed to encode image {img_path}: {e}\n")
        else:
            sys.stderr.write(f"Warning: Image file not found: {src} (resolved to {img_path})\n")

        return full_tag

    # Replace <p><img ...></p> or standalone <img ...>
    html_text = re.sub(r'<p>\s*(<img[^>]+>)\s*</p>', r'\1', html_text)
    return re.sub(r'<img[^>]+>', _replace_img, html_text)


def format_table_cells(html_text: str) -> str:
    """Detects table cells with numbers, units, metrics, or pure English text, and applies LTR with clean wrapping."""
    def _fix_td(m):
        attrs = m.group(1) or ""
        content = m.group(2).strip()
        inner_text = re.sub(r'<[^>]+>', '', content)

        # If dash or empty
        if inner_text in ["—", "-", "–"]:
            return '<td style="text-align: center;">—</td>'

        # Pure numerical cell
        if re.search(r'^\s*[-+]?[\d\.,\s/%]+\s*$', inner_text):
            return f'<td class="num-cell" dir="ltr">{content}</td>'

        # If cell has NO Arabic text and has Latin chars
        if not has_arabic(inner_text) and re.search(r'[A-Za-z]', inner_text):
            return f'<td class="ltr-cell" dir="ltr" style="text-align: left;">{content}</td>'

        return f'<td{attrs}>{content}</td>'

    return re.sub(r"<td(\s*[^>]*)>(.*?)</td>", _fix_td, html_text, flags=re.DOTALL)


def isolate_english_leading_phrases(html_text: str) -> str:
    """Wraps leading English equations/definitions in Arabic paragraphs with <bdi dir='ltr'>."""
    def _fix_p(m):
        content = m.group(1)
        if not has_arabic(content):
            return m.group(0)

        # Match leading English content before an em-dash or Arabic letter
        match = re.match(r"^(\s*(?:<[^>]+>|[A-Za-z0-9_\-\.\s/=:,\(\)\+])+?)(\s*—|\s*:\s*[\u0600-\u06FF]|[\u0600-\u06FF])", content)
        if match:
            leading = match.group(1).strip()
            rest = content[len(match.group(1)):]
            inner_lead = re.sub(r'<[^>]+>', '', leading)
            if len(re.findall(r'[A-Za-z]', inner_lead)) >= 3 and not has_arabic(leading):
                return f'<p><bdi class="en-token" dir="ltr">{leading}</bdi>{rest}</p>'
        return m.group(0)

    return re.sub(r"<p>(.*?)</p>", _fix_p, html_text, flags=re.DOTALL)
# ---------------------------------------------------------------------------
# Frontmatter Parser
# ---------------------------------------------------------------------------

def parse_frontmatter(md_content: str) -> Tuple[Dict[str, str], str]:
    """Extracts YAML frontmatter from Markdown if present."""
    meta: Dict[str, str] = {}
    content = md_content

    if md_content.startswith("---"):
        parts = md_content.split("---", 2)
        if len(parts) >= 3:
            raw_meta = parts[1].strip()
            content = parts[2]
            for line in raw_meta.splitlines():
                if ":" in line:
                    key, val = line.split(":", 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    meta[key] = val

    return meta, content
def sanitize_markdown_for_publication(md_text: str, meta: Dict[str, str]) -> str:
    """Strips internal agent scaffolding, backend work notes, and language markers before publication."""
    # Clean frontmatter meta titles of 'File 01 of 10' patterns
    if "title" in meta:
        meta["title"] = re.sub(r"File\s+0?(\d+)\s+of\s+\d+[\s:—–-]+", r"Unit \1: ", meta["title"])
        meta["title"] = re.sub(r"File\s+0?(\d+)\s+of\s+\d+", r"Unit \1", meta["title"])
    if "file" in meta:
        del meta["file"]

    lines = md_text.splitlines()
    clean_lines = []
    found_first_heading = False
    for line in lines:
        # 1. Strip leading top-level title from body to avoid duplicate title under doc-header
        if not found_first_heading and re.match(r"^#\s+.*", line):
            found_first_heading = True
            continue
        if line.strip():
            found_first_heading = True
        # 2. Strip standalone language markers like **EN.**, **AR.**, EN., AR.
        if re.match(r"^\s*(?:\*{1,2})?(?:EN|AR)\.?(?:\*{1,2})?\s*$", line):
            continue

        # 3. Strip leading **EN.** or **AR.** prefixes from paragraph starts
        line = re.sub(r"^\s*(?:\*{1,2})?(?:EN|AR)\.?(?:\*{1,2})?\s+", "", line)

        # 4. Strip internal backend footers
        if re.search(r"^\s*\*?File\s+\d+\s+of\s+\d+\.\s*Built\s+\d{4}-\d{2}-\d{2}", line, re.IGNORECASE):
            continue
        if re.search(r"under\s+`?Week_\w+\.md`?", line, re.IGNORECASE) and re.search(r"\[THIN\]", line):
            continue

        # 5. Clean [THIN] markers inside table rows or text
        line = re.sub(r"\|\s*`?\[THIN\]`?\s*\|", "| Note: Primary Coverage |", line)
        line = re.sub(r"`?\[THIN\]`?", "*(In-depth note)*", line)

        clean_lines.append(line)

    return "\n".join(clean_lines)


def wrap_flow_arrows(html_text: str) -> str:
    """Wraps sequence flow arrows in explicit LTR containers so BiDi doesn't reverse them."""
    def _arrow_rep(m):
        return f'<span class="flow-arrow" dir="ltr">{m.group(0)}</span>'
    return re.sub(r"(?<![<A-Za-z0-9])([→←]|->)(?![>A-Za-z0-9])", _arrow_rep, html_text)

# ---------------------------------------------------------------------------
# Math & KaTeX Preprocessing
# ---------------------------------------------------------------------------

def protect_math_blocks(md_text: str) -> Tuple[str, Dict[str, str]]:
    """Extracts math blocks ($$...$$ and $...$) and replaces them with placeholders.
    
    Prevents Python Markdown parser and BiDi regex from corrupting backslashes,
    underscores, or asterisks inside LaTeX formulas.
    """
    placeholders: Dict[str, str] = {}
    count = 0

    # 1. Protect Display Math ($$...$$)
    def _save_display_math(m):
        nonlocal count
        key = f"@@MATH_DISPLAY_{count}@@"
        count += 1
        formula = m.group(1).strip()
        placeholders[key] = f'<div class="math-block" dir="ltr">$${formula}$$</div>'
        return key

    text = re.sub(r"\$\$([\s\S]+?)\$\$", _save_display_math, md_text)

    # 2. Protect Inline Math ($...$)
    def _save_inline_math(m):
        nonlocal count
        key = f"@@MATH_INLINE_{count}@@"
        count += 1
        formula = m.group(1).strip()
        placeholders[key] = f'<span class="math-inline" dir="ltr">${formula}$</span>'
        return key

    text = re.sub(r"(?<!\$)\$([^\$\n]+?)\$(?!\$)", _save_inline_math, text)

    return text, placeholders


def restore_math_blocks(html_text: str, placeholders: Dict[str, str]) -> str:
    """Restores protected math placeholders into the final HTML document."""
    for key, val in placeholders.items():
        html_text = html_text.replace(key, val)
    return html_text


# ---------------------------------------------------------------------------
# Academic CSS & Layout Templates
# ---------------------------------------------------------------------------

SHARED_CSS = r"""
@page {
  size: A4 portrait;
  margin: 22mm 15mm 22mm 15mm;
}
* { box-sizing: border-box; }
html, body {
  margin: 0;
  padding: 0;
  color: #1e293b;
  font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
  font-size: 10.2pt;
  line-height: 1.6;
  background: #ffffff;
  -webkit-font-smoothing: antialiased;
}

/* Page Break Policies */
.page-break { page-break-after: always; }
.no-break { page-break-inside: avoid; }

.ltr-block {
  direction: ltr !important;
  text-align: left !important;
  unicode-bidi: isolate;
}
/* Bidirectional & Math Isolation */
.katex-display, .katex, math {
  direction: ltr !important;
  unicode-bidi: isolate !important;
  text-align: center;
}
.math-block {
  margin: 12px 0;
  text-align: center;
  direction: ltr !important;
  unicode-bidi: isolate;
  page-break-inside: avoid;
}
.math-inline {
  direction: ltr !important;
  display: inline-block;
  unicode-bidi: isolate;
  white-space: nowrap !important;
}
.en-token {
  font-family: 'Segoe UI', Arial, sans-serif;
  direction: ltr;
  display: inline;
  color: inherit;
  font-weight: inherit;
  unicode-bidi: isolate;
}

/* Headings */
h1 {
  color: #1e3a8a;
  font-size: 20pt;
  margin: 8px 0 4px 0;
  font-weight: 700;
  line-height: 1.3;
}
h2 {
  color: #1e3a8a;
  font-size: 14pt;
  margin: 18px 0 8px 0;
  font-weight: 700;
  border-bottom: 1.5px solid #e2e8f0;
  padding-bottom: 4px;
  page-break-after: avoid;
}
h3 {
  color: #0f766e;
  font-size: 12pt;
  margin: 14px 0 6px 0;
  font-weight: 600;
  page-break-after: avoid;
}
p {
  margin: 0 0 10px 0;
  line-height: 1.6;
}
[dir="ltr"] p, .ltr-block {
  text-align: left !important;
}
[dir="rtl"] p {
  text-align: justify;
  text-justify: inter-word;
}

/* Blockquotes (Verbatim Citations & Formal Quotations) */
blockquote {
  margin: 12px 0;
  padding: 8px 16px;
  background: #f8fafc;
  border-radius: 4px;
  color: #1e293b;
  font-style: normal;
  page-break-inside: avoid;
}
/* LTR Blockquote: ALWAYS border on the LEFT */
blockquote[dir="ltr"], blockquote.ltr-block, [dir="ltr"] blockquote:not([dir="rtl"]):not(.rtl-block) {
  border-left: 3.5px solid #2563eb !important;
  border-right: none !important;
  text-align: left !important;
}
/* RTL Blockquote: ALWAYS border on the RIGHT */
blockquote[dir="rtl"], blockquote.rtl-block, [dir="rtl"] blockquote:not([dir="ltr"]):not(.ltr-block) {
  border-right: 3.5px solid #2563eb !important;
  border-left: none !important;
  text-align: right !important;
}
blockquote p {
  margin: 4px 0;
  text-align: inherit;
}

/* Active Recall Q&A Cards (Distinct from Quotes) */
.qa-card {
  margin: 14px 0;
  page-break-inside: avoid;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  background: #ffffff;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
}
.qa-question-box {
  padding: 8px 14px;
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
  display: flex;
  align-items: flex-start;
  gap: 10px;
}
.qa-question-box[dir="rtl"] {
  text-align: right;
}
.qa-question-box[dir="ltr"] {
  text-align: left;
}
.qa-badge-q {
  background: #1e3a8a;
  color: #ffffff;
  font-size: 8.5pt;
  font-weight: 800;
  padding: 2px 7px;
  border-radius: 4px;
  letter-spacing: 0.5px;
  flex-shrink: 0;
  margin-top: 1px;
}
.qa-question-text {
  font-weight: 700;
  font-size: 10pt;
  color: #0f172a;
  line-height: 1.45;
}
.qa-answer-box {
  padding: 10px 14px;
  background: #f0fdf4;
  position: relative;
}
/* Direction-sensitive emerald border for Q&A answers! */
.qa-answer-box.ltr-ans, .qa-answer-box[dir="ltr"] {
  border-left: 4px solid #10b981 !important;
  border-right: none !important;
  text-align: left !important;
}
.qa-answer-box.rtl-ans, .qa-answer-box[dir="rtl"] {
  border-right: 4px solid #10b981 !important;
  border-left: none !important;
  text-align: right !important;
}
.qa-badge-ans {
  font-size: 7.5pt;
  font-weight: 750;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #059669;
  margin-bottom: 5px;
}
.qa-answer-content {
  font-size: 9.5pt;
  line-height: 1.55;
  color: #1e293b;
}
.qa-answer-content p {
  margin: 4px 0 !important;
  text-align: inherit !important;
}

/* Flow Arrows */
.flow-arrow {
  direction: ltr !important;
  display: inline-block;
  unicode-bidi: isolate;
  padding: 0 3px;
  color: #0f766e;
  font-weight: 700;
}

/* Academic Header & Metadata Banner */
.doc-header {
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 18px;
  margin-bottom: 22px;
  text-align: center;
  page-break-after: avoid;
  direction: ltr !important;
}
.unit-eyebrow {
  color: #2563eb;
  font-size: 11pt;
  font-weight: 750;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 6px;
  text-align: center;
}
.doc-main-title {
  color: #0f172a;
  font-size: 21pt;
  font-weight: 800;
  margin: 0 0 6px 0;
  line-height: 1.25;
  letter-spacing: -0.3px;
  text-align: center;
}
.sub-title {
  color: #0f766e;
  font-size: 11pt;
  font-weight: 600;
  margin: 4px auto 0 auto;
  line-height: 1.5;
  text-align: center;
  max-width: 88%;
}
/* Pedagogical Callout Cards */
.callout {
  border-radius: 6px;
  padding: 10px 14px;
  margin: 12px 0;
  page-break-inside: avoid;
  border-right: 4.5px solid #1e3a8a;
  background: #f8fafc;
}
.callout.trap {
  border-right-color: #dc2626;
  background: #fef2f2;
}
.callout.feynman {
  border-right-color: #0d9488;
  background: #f0fdfa;
}
.callout.concept {
  border-right-color: #2563eb;
  background: #eff6ff;
}
.callout.calc {
  border-right-color: #d97706;
  background: #fffbeb;
}
.callout.warn {
  border-right-color: #b91c1c;
  background: #fff1f2;
}
.callout-title {
  font-weight: 700;
  font-size: 10.5pt;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.callout.trap .callout-title { color: #b91c1c; }
.callout.feynman .callout-title { color: #0f766e; }
.callout.concept .callout-title { color: #1d4ed8; }
.callout.calc .callout-title { color: #b45309; }
.callout.warn .callout-title { color: #9f1239; }
.callout-icon { font-size: 11pt; }
.callout-body p:last-child { margin-bottom: 0; }

/* Figures & Diagram Inlining */
.figure-box, figure {
  margin: 14px 0;
  text-align: center;
  page-break-inside: avoid;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 10px;
  background: #ffffff;
}
.figure-box img, figure img {
  max-width: 100%;
  max-height: 115mm;
  height: auto;
  border-radius: 4px;
  display: block;
  margin: 0 auto 8px auto;
}
.figure-caption, figcaption {
  font-size: 9pt;
  color: #475569;
  font-weight: 600;
  margin-top: 4px;
}
.fig-row {
  display: flex;
  gap: 14px;
  justify-content: center;
  align-items: stretch;
  margin: 14px 0;
  page-break-inside: avoid;
}
.fig-row .figure-box {
  flex: 1;
  margin: 0;
}

/* Academic Tables */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0;
  font-size: 9pt;
  page-break-inside: auto;
  table-layout: auto;
}
thead {
  display: table-header-group;
}
tr {
  page-break-inside: avoid;
}
th, td {
  border: 1px solid #cbd5e1;
  padding: 6px 10px;
  line-height: 1.45;
  vertical-align: top;
  word-wrap: break-word;
  overflow-wrap: break-word;
}
th {
  background: #f1f5f9;
  color: #0f172a;
  font-weight: 700;
}
[dir="rtl"] th, [dir="rtl"] td {
  text-align: right;
}
[dir="ltr"] th, [dir="ltr"] td {
  text-align: left;
}
td.num-cell, th.num-cell {
  direction: ltr !important;
  text-align: center !important;
  font-family: Consolas, 'Segoe UI', monospace;
  unicode-bidi: isolate;
  white-space: nowrap;
}
td.ltr-cell, th.ltr-cell {
  direction: ltr !important;
  text-align: left !important;
  unicode-bidi: isolate;
  white-space: normal !important;
}
tr:nth-child(even) td {
  background: #f8fafc;
}

/* Code Blocks */
pre, code {
  font-family: Consolas, 'Fira Code', 'Courier New', monospace;
}
pre {
  background: #0f172a;
  color: #f8fafc;
  border: 1px solid #1e293b;
  padding: 11px 15px;
  border-radius: 6px;
  direction: ltr;
  text-align: left;
  font-size: 8.5pt;
  line-height: 1.5;
  overflow-x: auto;
  page-break-inside: avoid;
}
pre code {
  color: #38bdf8;
  background: transparent;
  padding: 0;
}
"""

def generate_header_footer_templates(course_name: str, doc_title: str) -> Tuple[str, str]:
    """Generates Chromium header and footer templates with vector page numbers."""
    header = f"""
<div style="font-size: 7.5pt; width: 100%; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px; margin: 0 15mm; display: flex; justify-content: space-between; color: #64748b; font-family: 'Segoe UI', Arial, sans-serif;">
  <span style="direction: ltr;">Master Studio · {H.escape(course_name)}</span>
  <span style="direction: rtl;">{H.escape(doc_title)}</span>
</div>
"""
    footer = """
<div style="font-size: 7.5pt; width: 100%; border-top: 1px solid #e2e8f0; padding-top: 4px; margin: 0 15mm; display: flex; justify-content: space-between; color: #64748b; font-family: 'Segoe UI', Arial, sans-serif;">
  <span style="direction: rtl;">كلية علوم الحاسوب وتكنولوجيا المعلومات — جامعة واسط</span>
  <span style="direction: ltr;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
</div>
"""
    return header, footer


# ---------------------------------------------------------------------------
# Template Renderers
# ---------------------------------------------------------------------------

def render_study_pack_html(body_html: str, meta: Dict[str, str], lang: str) -> str:
    """Builds standard lecture study pack layout."""
    raw_title = meta.get("title", "وثيقة المراجعة والتلخيص الأكاديمي")
    subtitle = meta.get("subtitle", meta.get("description", ""))

    # Parse eyebrow and main title if present (e.g. "ASE Week 02 — Unit 01: SDLC Fundamentals")
    eyebrow = ""
    main_title = raw_title
    if ":" in raw_title:
        parts = raw_title.split(":", 1)
        eyebrow = parts[0].strip()
        main_title = parts[1].strip()
    elif " — " in raw_title:
        parts = raw_title.split(" — ", 1)
        eyebrow = parts[0].strip()
        main_title = parts[1].strip()

    dir_attr = "rtl" if lang == "ar" else "ltr"

    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{dir_attr}">
<head>
<title>{H.escape(raw_title)}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>
<style>
{SHARED_CSS}
</style>
</head>
<body>

<div class="doc-header">
  {f'<div class="unit-eyebrow">{H.escape(eyebrow)}</div>' if eyebrow else ''}
  <h1 class="doc-main-title">{H.escape(main_title)}</h1>
  {f'<div class="sub-title">{H.escape(subtitle)}</div>' if subtitle else ''}
</div>

{body_html}

</body>
</html>
"""


def render_booklet_html(body_html: str, meta: Dict[str, str], lang: str) -> str:
    """Builds a multi-page booklet with a formal cover page."""
    course = meta.get("course", meta.get("subject", "Master of Computer Science"))
    title = meta.get("title", "دراسة شاملة ودليل مراجعة")
    subtitle = meta.get("subtitle", "Comprehensive Academic Study Guide")
    instructor = meta.get("instructor", meta.get("prof", "Faculty of CS & IT"))
    term = meta.get("term", "Fall 2026")
    week = meta.get("week", "Week 01")

    dir_attr = "rtl" if lang == "ar" else "ltr"

    cover_html = f"""
<div class="cover-page" style="min-height: 250mm; display: flex; flex-direction: column; justify-content: space-between; text-align: center; padding: 20mm 10mm 15mm 10mm;">
  <div>
    <div style="font-size: 11pt; letter-spacing: 2px; color: #64748b; font-weight: 700; text-transform: uppercase;">
      جامعة واسط · كلية علوم الحاسوب وتكنولوجيا المعلومات
    </div>
    <div style="font-size: 9.5pt; color: #94a3b8; margin-top: 3px;">
      UNIVERSITY OF WASIT · COLLEGE OF COMPUTER SCIENCE & INFORMATION TECHNOLOGY
    </div>
    <div style="width: 40mm; height: 3px; background: #1e3a8a; margin: 15mm auto;"></div>
  </div>

  <div>
    <div style="display: inline-block; background: #1e3a8a; color: white; padding: 4px 14px; border-radius: 999px; font-size: 10pt; font-weight: 700; margin-bottom: 12px;">
      {H.escape(course)} · {H.escape(week)}
    </div>
    <h1 style="font-size: 26pt; color: #1e3a8a; margin: 6px 0; font-weight: 800; line-height: 1.3;">
      {H.escape(title)}
    </h1>
    <div style="font-size: 14pt; color: #0f766e; font-weight: 600; margin-top: 6px;">
      {H.escape(subtitle)}
    </div>
  </div>

  <div style="border-top: 1.5px solid #e2e8f0; padding-top: 15mm; display: flex; justify-content: space-around; font-size: 10pt; color: #475569;">
    <div>
      <div style="font-weight: 750; color: #0f172a;">أستاذ المادة (Instructor)</div>
      <div>{H.escape(instructor)}</div>
    </div>
    <div>
      <div style="font-weight: 750; color: #0f172a;">الفصل الدراسي (Term)</div>
      <div>{H.escape(term)}</div>
    </div>
    <div>
      <div style="font-weight: 750; color: #0f172a;">إعداد الطالب (Student)</div>
      <div>Master Studio Candidate</div>
    </div>
  </div>
</div>
<div class="page-break"></div>
"""

    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{dir_attr}">
<head>
<meta charset="utf-8">
<title>{H.escape(title)}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>
<style>
{SHARED_CSS}
</style>
</head>
<body>

{cover_html}

{body_html}

</body>
</html>
"""


def render_exam_sheet_html(body_html: str, meta: Dict[str, str], lang: str) -> str:
    """Builds a dense, 2-column exam sheet layout."""
    title = meta.get("title", "ورقة المراجعة الامتحانية المركزة (Exam Cheat Sheet)")
    course = meta.get("course", meta.get("subject", "Master Studio"))
    dir_attr = "rtl" if lang == "ar" else "ltr"

    dense_css = SHARED_CSS + """
@page {
  size: A4 portrait;
  margin: 12mm 10mm 12mm 10mm;
}
body {
  font-size: 8.5pt;
  line-height: 1.4;
}
.sheet-columns {
  column-count: 2;
  column-gap: 8mm;
  column-rule: 1px solid #e2e8f0;
}
h1 { font-size: 14pt; margin: 0 0 4px 0; }
h2 { font-size: 10.5pt; margin: 8px 0 4px 0; padding-bottom: 2px; }
h3 { font-size: 9.5pt; margin: 6px 0 2px 0; }
.callout { padding: 6px 8px; margin: 6px 0; font-size: 8pt; }
table { font-size: 8pt; margin: 6px 0; }
th, td { padding: 3px 6px; }
pre { padding: 6px 8px; font-size: 7.5pt; }
"""

    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{dir_attr}">
<head>
<meta charset="utf-8">
<title>{H.escape(title)}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>
<style>
{dense_css}
</style>
</head>
<body>

<div style="border-bottom: 2px solid #1e3a8a; padding-bottom: 6px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
  <div>
    <h1 style="color: #1e3a8a; margin: 0;">{H.escape(title)}</h1>
    <div style="font-size: 8.5pt; color: #0f766e; font-weight: 600;">{H.escape(course)} · University of Wasit</div>
  </div>
  <div style="font-size: 8pt; color: #64748b; text-align: left; direction: ltr;">
    <b>Master Studio Exam Sheet</b><br>Fall 2026
  </div>
</div>

<div class="sheet-columns">
  {body_html}
</div>

</body>
</html>
"""


# ---------------------------------------------------------------------------
# Core Compilation Engine
# ---------------------------------------------------------------------------

async def export_html_to_pdf_async(
    html_content: str,
    output_pdf_path: Path,
    course_name: str,
    doc_title: str,
    browser_path: Optional[str] = None
) -> Path:
    """Asynchronously renders an HTML string to a PDF file via Playwright Chromium."""
    from playwright.async_api import async_playwright

    exe = browser_path or find_chromium_binary()
    output_pdf_path = Path(output_pdf_path).resolve()
    output_pdf_path.parent.mkdir(parents=True, exist_ok=True)

    header_tpl, footer_tpl = generate_header_footer_templates(course_name, doc_title)

    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=exe, headless=True)
        page = await browser.new_page()
        
        await page.set_content(html_content, wait_until="networkidle")
        # Explicitly trigger KaTeX auto-render in DOM
        await page.evaluate("""
        () => {
            if (typeof renderMathInElement === 'function') {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ],
                    throwOnError: false
                });
            }
        }
        """)
        # Give KaTeX and local fonts 800ms to settle rendering
        await page.wait_for_timeout(800)
        await page.pdf(
            path=str(output_pdf_path),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template=header_tpl,
            footer_template=footer_tpl,
            margin={"top": "24mm", "bottom": "24mm", "left": "15mm", "right": "15mm"}
        )
        await browser.close()

    return output_pdf_path


def export_markdown_to_pdf(
    input_md_path: Path,
    output_pdf_path: Optional[Path] = None,
    template: str = "study_pack",
    lang: Optional[str] = None,
    course_override: Optional[str] = None,
    prof_override: Optional[str] = None,
    term_override: Optional[str] = None,
    open_viewer: bool = False
) -> Path:
    """Main synchronous entry point: transforms a Markdown note into an academic PDF."""
    input_md_path = Path(input_md_path).resolve()
    if not input_md_path.exists():
        raise FileNotFoundError(f"Source markdown file not found: {input_md_path}")

    if not output_pdf_path:
        output_pdf_path = input_md_path.with_suffix(".pdf")
    else:
        output_pdf_path = Path(output_pdf_path).resolve()

    # Check if target file is locked by an external PDF viewer on Windows
    orig_target = output_pdf_path
    candidate = output_pdf_path
    counter = 1
    while candidate.exists():
        try:
            with open(candidate, "a+b"):
                output_pdf_path = candidate
                break
        except PermissionError:
            candidate = orig_target.with_name(f"{orig_target.stem}_v{counter}.pdf" if counter > 1 else f"{orig_target.stem}_new.pdf")
            counter += 1
    if candidate != orig_target:
        sys.stderr.write(f"[*] Notice: {orig_target.name} is currently open in a PDF viewer. Writing to {candidate.name}\n")
        output_pdf_path = candidate
    raw_text = input_md_path.read_text(encoding="utf-8")
    meta, body_md = parse_frontmatter(raw_text)

    # Overrides
    if course_override:
        meta["course"] = course_override
    if prof_override:
        meta["instructor"] = prof_override
    if term_override:
        meta["term"] = term_override

    # Auto-detect language if not specified
    if not lang:
        lang = "ar" if has_arabic(body_md) else "en"

    # Step 0: Sanitize Markdown for Publication (strip backend markers, File 01 of 10, etc.)
    sanitized_md = sanitize_markdown_for_publication(body_md, meta)

    # Step 1: Protect Math Blocks ($$...$$ and $...$)
    protected_md, math_placeholders = protect_math_blocks(sanitized_md)

    # Step 2: Transform Callouts (> [!TRAP], > [!FEYNMAN]...)
    callouts_md = transform_callouts(protected_md, default_lang=lang)

    # Step 3: Markdown to HTML conversion
    extensions = ["tables", "fenced_code", "toc", "def_list", "attr_list"]
    raw_html = markdown.markdown(callouts_md, extensions=extensions)

    # Step 3.5: Transform Active Recall Q&A Cards (Distinguishes Q&A from Quotes)
    qa_transformed_html = transform_qa_cards(raw_html, default_lang=lang)

    # Step 4: BiDi English Token Isolation in Arabic text (while math is safely protected as @@MATH...@@)
    if lang == "ar":
        bidi_html = isolate_english_tokens_in_arabic(qa_transformed_html)
    else:
        bidi_html = qa_transformed_html

    # Step 5: Tag Pure English Blocks as LTR
    tagged_html = tag_bilingual_blocks(bidi_html)

    # Step 6: Isolate Leading English Equations / Definitions in Arabic Paragraphs
    isolated_leading_html = isolate_english_leading_phrases(tagged_html)

    # Step 7: Base64 Image Inlining
    inlined_html = inline_images_in_html(isolated_leading_html, input_md_path.parent)

    # Step 7.5: Wrap Flow Arrows
    arrow_wrapped_html = wrap_flow_arrows(inlined_html)

    # Step 8: Format Table Numerical and English Cells for BiDi/LTR
    table_formatted_html = format_table_cells(arrow_wrapped_html)

    # Step 8.5: Restore Math Blocks as pure, untouched LaTeX
    math_restored_html = restore_math_blocks(table_formatted_html, math_placeholders)

    # Step 9: Select & Render Layout Template
    if template == "booklet":
        final_html = render_booklet_html(math_restored_html, meta, lang)
    elif template == "exam_sheet":
        final_html = render_exam_sheet_html(math_restored_html, meta, lang)
    else:
        final_html = render_study_pack_html(math_restored_html, meta, lang)
    course_name = meta.get("course", meta.get("subject", "Master of Computer Science"))
    doc_title = meta.get("title", input_md_path.stem.replace("_", " "))

    # Run Playwright rendering safely across CLI, background threads, and active async loops (Jupyter / eval)
    import concurrent.futures
    coro = export_html_to_pdf_async(final_html, output_pdf_path, course_name, doc_title)
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(asyncio.run, coro)
            future.result()
    else:
        asyncio.run(coro)

    if open_viewer and sys.platform.startswith("win"):
        os.startfile(str(output_pdf_path))

    return output_pdf_path


# ---------------------------------------------------------------------------
# CLI Interface
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Master Studio Academic PDF Exporter")
    parser.add_argument("input", help="Path to input Markdown note (.md)")
    parser.add_argument("-o", "--output", help="Path to destination PDF (.pdf)")
    parser.add_argument(
        "-t", "--template",
        choices=["study_pack", "booklet", "exam_sheet", "glossary"],
        default="study_pack",
        help="Template preset (default: study_pack)"
    )
    parser.add_argument("--lang", choices=["ar", "en"], help="Document language (auto-detected by default)")
    parser.add_argument("--course", help="Course name / code override")
    parser.add_argument("--prof", help="Instructor name override")
    parser.add_argument("--term", help="Academic term override (default: Fall 2026)")
    parser.add_argument("--open", action="store_true", help="Open PDF after compilation")

    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output) if args.output else None

    print(f"[*] Compiling academic PDF from: {in_path.name}")
    print(f"[*] Template preset: {args.template}")

    t0 = asyncio.get_event_loop().time() if asyncio.get_event_loop().is_running() else 0
    import time
    start_time = time.time()

    pdf = export_markdown_to_pdf(
        in_path,
        output_pdf_path=out_path,
        template=args.template,
        lang=args.lang,
        course_override=args.course,
        prof_override=args.prof,
        term_override=args.term,
        open_viewer=args.open
    )

    elapsed = time.time() - start_time
    print(f"[+] Successfully generated: {pdf} ({pdf.stat().st_size / 1024:.1f} KB) in {elapsed:.2f}s")


if __name__ == "__main__":
    main()
