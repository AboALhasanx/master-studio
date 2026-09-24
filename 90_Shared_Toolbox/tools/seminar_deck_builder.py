#!/usr/bin/env python3
"""
Seminar Deck Builder — native editable PPTX with IMAGES + SPEAKER NOTES
------------------------------------------------------------------------
Extends the Master Studio deck house-style (16:9, navy titles, slate ground,
projector-tuned fonts) with two things office_exporter.py does not support:

  * ![caption](relative/or/abs/path.png)   -> an embedded image (evidence)
  * ::: notes ... :::                      -> PowerPoint speaker notes (the
                                              "شرح على الجهة الثانية")

Markdown contract (Marp-style, split on a line that is exactly '---'):
  * Slide title   : a single '# ...' line (write it as a full-sentence assertion)
  * Bullets       : '- text'  (21pt)   and '  - text' (17.5pt sub-bullet)
  * Numbered      : '1. text' (20pt)
  * Quote         : '> text'  (18pt italic)
  * Image         : '![caption](path.png)'  (one per slide; caption shown under it)
  * Speaker notes : a fenced '::: notes' ... ':::' block
  * Title slide   : add '<!-- _class: lead -->'

Layout: if a slide has an image it becomes two-column (text left, image right);
otherwise the text spans the full width.

Usage:  python seminar_deck_builder.py <deck.md> [-o <deck.pptx>]
"""
import re, sys, argparse
from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

try:
    from PIL import Image
except Exception:
    Image = None

# ---- house style ----
BG        = RGBColor(248, 250, 252)
NAVY      = RGBColor(30, 58, 138)
INK       = RGBColor(15, 23, 42)
SUB       = RGBColor(71, 85, 105)
NUMLINE   = RGBColor(100, 116, 139)
CAPTION   = RGBColor(100, 116, 139)
FONT      = 'Segoe UI'

SW, SH = 13.333, 7.5   # inches


def strip_emojis(t: str) -> str:
    return re.sub(r'[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF]', '', t).strip()


def parse_deck(md_path: Path):
    text = md_path.read_text(encoding='utf-8')
    raw_slides = re.split(r'\n---\n', text)
    slides = []
    for raw in raw_slides:
        raw = raw.strip()
        if not raw:
            continue
        if raw.startswith('marp:') or 'paginate:' in raw:
            continue
        is_lead = '<!-- _class: lead -->' in raw
        lines = raw.split('\n')
        title = ""
        body = []
        notes = []
        in_notes = False
        for line in lines:
            s = line.strip()
            if s.startswith('::: notes'):
                in_notes = True
                continue
            if in_notes:
                if s == ':::':
                    in_notes = False
                else:
                    notes.append(line)
                continue
            if '<!--' in s and '-->' in s:
                continue
            if not title and (s.startswith('# ') or s.startswith('## ')):
                title = strip_emojis(re.sub(r'^#+\s*', '', s))
            else:
                body.append(line)
        slides.append({
            "title": title,
            "body": [b for b in body if b.strip()],
            "notes": "\n".join(notes).strip(),
            "is_lead": is_lead,
        })
    return slides


def add_bg(slide):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(SW), Inches(SH))
    sh.fill.solid(); sh.fill.fore_color.rgb = BG; sh.line.fill.background()
    sh.shadow.inherit = False


def add_slide_number(slide, n):
    box = slide.shapes.add_textbox(Inches(11.8), Inches(6.62), Inches(1.2), Inches(0.5))
    p = box.text_frame.paragraphs[0]
    p.text = str(n); p.font.size = Pt(14); p.font.name = FONT
    p.font.bold = True; p.font.color.rgb = NUMLINE; p.alignment = PP_ALIGN.RIGHT


def add_title(slide, title, size=31):
    box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1.05))
    tf = box.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = title
    p.font.size = Pt(size); p.font.bold = True; p.font.name = FONT; p.font.color.rgb = NAVY


def fill_text(tf, body_lines, first_is_new=False):
    idx = 0
    for line in body_lines:
        s = strip_emojis(line.strip())
        if not s:
            continue
        p = tf.paragraphs[0] if (idx == 0 and not first_is_new) else tf.add_paragraph()
        idx += 1
        if s.startswith('- ') or s.startswith('* '):
            p.text = "•  " + s[2:]; p.font.size = Pt(21); p.space_after = Pt(12)
            p.font.color.rgb = INK
        elif s.startswith('  - ') or s.startswith('  * ') or s.startswith('    - '):
            p.text = "–  " + s.lstrip(' -*'); p.font.size = Pt(17.5); p.space_after = Pt(8)
            p.font.color.rgb = SUB
        elif re.match(r'^\d+\.\s', s):
            p.text = s; p.font.size = Pt(20); p.space_after = Pt(10); p.font.color.rgb = INK
        elif s.startswith('> '):
            p.text = "“ " + s[2:] + " ”"; p.font.size = Pt(18); p.font.italic = True
            p.font.color.rgb = SUB; p.space_after = Pt(14)
        else:
            p.text = s; p.font.size = Pt(21); p.space_after = Pt(10); p.font.color.rgb = INK
        p.font.name = FONT


def add_image_fit(slide, img_path: Path, caption: str, box):
    """Insert an image centred inside `box` (l,t,w,h inches), preserving aspect."""
    l, t, w, h = box
    iw, ih = None, None
    if Image is not None:
        try:
            with Image.open(img_path) as im:
                iw, ih = im.size
        except Exception:
            iw = ih = None
    if not iw or not ih:
        iw, ih = 4, 3
    ar = iw / ih
    box_ar = w / h
    if ar >= box_ar:
        dw = w; dh = w / ar
    else:
        dh = h; dw = h * ar
    left = l + (w - dw) / 2
    top = t + (h - dh) / 2
    slide.shapes.add_picture(str(img_path), Inches(left), Inches(top), Inches(dw), Inches(dh))
    if caption:
        cap = slide.shapes.add_textbox(Inches(l), Inches(t + h - 0.34), Inches(w), Inches(0.34))
        cp = cap.text_frame.paragraphs[0]
        cp.text = strip_emojis(caption); cp.font.size = Pt(11.5); cp.font.name = FONT
        cp.font.italic = True; cp.font.color.rgb = CAPTION; cp.alignment = PP_ALIGN.CENTER


def build(md_path: Path, pptx_path: Path):
    slides_data = parse_deck(md_path)
    base = md_path.parent
    prs = Presentation()
    prs.slide_width = Inches(SW); prs.slide_height = Inches(SH)
    blank = prs.slide_layouts[6]

    for idx, s in enumerate(slides_data, 1):
        slide = prs.slides.add_slide(blank)
        add_bg(slide)
        add_slide_number(slide, idx)

        # speaker notes
        if s["notes"]:
            slide.notes_slide.notes_text_frame.text = s["notes"]

        if s["is_lead"]:
            tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(11.3), Inches(4.2))
            tf = tb.text_frame; tf.word_wrap = True
            p0 = tf.paragraphs[0]; p0.text = s["title"]
            p0.font.size = Pt(38); p0.font.bold = True; p0.font.name = FONT
            p0.font.color.rgb = NAVY; p0.space_after = Pt(20)
            for bl in s["body"]:
                c = strip_emojis(bl.strip().lstrip('#').strip())
                if not c:
                    continue
                p = tf.add_paragraph(); p.text = c; p.font.size = Pt(18)
                p.font.name = FONT; p.font.color.rgb = SUB; p.space_after = Pt(10)
            continue

        add_title(slide, s["title"])

        # split out the image (if any)
        img = None
        text_lines = []
        for bl in s["body"]:
            m = re.match(r'^!\[(.*?)\]\((.*?)\)\s*$', bl.strip())
            if m and img is None:
                img = (m.group(1), m.group(2))
            else:
                text_lines.append(bl)

        if img:
            cap, path = img
            ip = Path(path)
            if not ip.is_absolute():
                ip = (base / path).resolve()
            # two-column: text left, image right
            tb = slide.shapes.add_textbox(Inches(0.8), Inches(1.65), Inches(5.9), Inches(4.95))
            fill_text(tb.text_frame, text_lines)
            tb.text_frame.word_wrap = True
            if ip.exists():
                add_image_fit(slide, ip, cap, (7.0, 1.65, 5.5, 4.95))
            else:
                miss = slide.shapes.add_textbox(Inches(7.0), Inches(3.4), Inches(5.5), Inches(1.0))
                mp = miss.text_frame.paragraphs[0]; mp.text = f"[missing image: {path}]"
                mp.font.size = Pt(12); mp.font.color.rgb = RGBColor(220, 38, 38)
        else:
            tb = slide.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0))
            fill_text(tb.text_frame, text_lines)
            tb.text_frame.word_wrap = True

    prs.save(str(pptx_path))
    print(f"[+] Deck written: {pptx_path}  ({len(slides_data)} slides)")


def main():
    ap = argparse.ArgumentParser(description="Seminar Deck Builder (images + notes)")
    ap.add_argument("deck", help="path to the deck markdown")
    ap.add_argument("-o", "--output", help="output .pptx path")
    a = ap.parse_args()
    md = Path(a.deck)
    if not md.exists():
        print(f"Error: {md} not found", file=sys.stderr); sys.exit(1)
    out = Path(a.output) if a.output else md.with_suffix(".pptx")
    build(md, out)


if __name__ == "__main__":
    main()
