import re, sys, glob
from pathlib import Path

TOOLS = Path(r"C:/Users/gokoq/Master-Studio/90_Shared_Toolbox/tools")
sys.path.insert(0, str(TOOLS))
import pdf_exporter
import fitz

BASE = Path(r"C:/Users/gokoq/Master-Studio/01_Semester_1/04_Advanced_Software_Eng")
NOTES = BASE / "03_Study_Notes"
OUTDIR = BASE / "08_PDF_Exports"
OUTDIR.mkdir(exist_ok=True)

COURSE = "CS504 — Advanced Software Engineering"
PROF = "Asst. Prof. Dr. Ali Fahim Ni'ma"
TERM = "Fall 2026"

def strip_frontmatter(text):
    if text.startswith('---'):
        lines = text.split('\n')
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                return '\n'.join(lines[i + 1:])
    return text

def remove_retrieval_section(body, ui):
    # Keep ONLY Unit 10's consolidated retrieval set as the single QA partition point.
    if ui == 10:
        return body
    lines = body.split('\n')
    out = []
    skip = False
    for line in lines:
        if re.match(r'^##\s+.*retrieval\s*set', line, re.IGNORECASE):
            skip = True
            continue
        if skip:
            if re.match(r'^##\s+', line):  # the next top section (Page anchors)
                skip = False
                out.append(line)
                continue
            else:
                continue
        out.append(line)
    return '\n'.join(out)

def parse_headings(body):
    heads = []
    for line in body.split('\n'):
        m = re.match(r'^(#{1,4})\s+(.*)$', line)
        if m:
            heads.append((len(m.group(1)), m.group(2).strip()))
    return heads

def norm(t):
    return (t.replace('\u2019', "'").replace('\u2018', "'")
             .replace('\u2013', '-').replace('\u2014', '-'))

def make_pattern(text):
    # Normalize EXACTLY like pages_text: norm() converts —/– -> - and quotes,
    # and strip markdown emphasis (*/` ) that the PDF renderer drops.
    t = norm(text.strip()).replace('*', '').replace('`', '')
    m = re.match(r'^(\d+(?:\.\d+)*)\s+(.*)$', t)
    if m:
        # Allow an OPTIONAL trailing dot after the number: a heading numbered "11."
        # renders with the dot ("11. Source notes") but the match must also accept
        # the bare "11" form. re.escape keeps internal dots (e.g. "2.2") intact.
        num = re.escape(m.group(1)) + r'\.?'
        rest = m.group(2).split()
        words = rest[:2]
        pat = num + r'\s+' + r'\s+'.join(re.escape(w) for w in words)
    else:
        words = t.split()[:3]
        pat = r'\s+'.join(re.escape(w) for w in words)
    pat = pat.replace("'", r"['\u2019]")
    # Anchor to line start so mid-line recap/callout mentions are not matched.
    return re.compile(r"^\s*" + pat, re.IGNORECASE | re.MULTILINE)


def unit_pattern(n, title):
    """Line-start match for a unit H1 using only the first few words of the title
    (robust to title wrapping). Rejects TOC entries (… p.NNN) and sources lines (p.NN)."""
    rest = title.split('—', 1)[1].strip() if '—' in title else title
    words = rest.split()[:3]
    prefix = rf"Unit\s+{n:02d}\s*[—-]\s+" + r"\s+".join(re.escape(w) for w in words)
    return re.compile(rf"^{prefix}(?!.*(?:…|\.\.\.|\bp\.\d))", re.MULTILINE)

def resolve_out(path):
    """Return the file the exporter actually wrote. The PDF engine writes to
    <stem>_new<suffix> when the canonical path is locked by a viewer, so we must
    prefer the FRESHER of the two (stale locked files would poison measurement)."""
    p = Path(path)
    alt = p.with_name(p.stem + "_new" + p.suffix)
    if alt.exists() and (not p.exists() or alt.stat().st_mtime > p.stat().st_mtime):
        return alt
    return p if p.exists() else alt

def swap_to_canonical(actual, canonical):
    """Try to move the freshly rendered file onto the canonical name. Fails (and
    returns False) if the canonical is locked by an open viewer — that's fine,
    we just keep the actual file and report which one is current."""
    canonical = Path(canonical)
    if actual.resolve() == canonical.resolve():
        return True
    try:
        # If canonical exists and is unlocked, remove it first; otherwise rename fails.
        if canonical.exists():
            try:
                canonical.unlink()
            except OSError:
                return False  # locked
        actual.replace(canonical)
        return True
    except OSError:
        return False

# --- Resolve the 10 unit files in order ---
unit_files = []
for i in range(1, 11):
    matches = sorted(NOTES.glob(f"Week_02_File_{i:02d}_*.md"))
    assert matches, f"Missing unit {i}"
    unit_files.append(matches[0])

bodies = []
toc_entries = []
for ui, fpath in enumerate(unit_files, start=1):
    raw = fpath.read_text(encoding='utf-8')
    body = strip_frontmatter(raw)
    body = remove_retrieval_section(body, ui)
    bodies.append(body)
    heads = parse_headings(body)
    unit_h1 = next(((idx, txt) for idx, (lvl, txt) in enumerate(heads) if lvl == 1), None)
    assert unit_h1 is not None, f"No H1 in unit {ui}"
    toc_entries.append({'kind': 'unit', 'ui': ui,
                        'label': unit_h1[1].replace('*', '').replace('`', ''),
                        'measure': unit_h1[1], 'is_unit_h1': True, 'level': 0})
    i = unit_h1[0] + 1
    while i < len(heads):
        lvl, txt = heads[i]
        if lvl == 1:
            break
        low = txt.lower()
        if 'page anchors' in low:
            i += 1; continue
        # Skip the per-unit "(N items)" retrieval subsections from the index
        if re.search(r'\(\d+\s+items?\)', txt):
            i += 1; continue
        if 'source notes' in low:
            toc_entries.append({'kind': 'src', 'ui': ui, 'label': 'Source notes',
                                'measure': txt, 'is_unit_h1': False, 'level': 1})
            i += 1; continue
        if 'retrieval set' in low:
            toc_entries.append({'kind': 'ret', 'ui': ui,
                                'label': 'Retrieval set (consolidated bank, Units 01–09)',
                                # Stable short measure: the real heading begins "Retrieval set",
                                # so make_pattern matches it across the whole Unit-10 window.
                                'measure': 'Retrieval set', 'is_unit_h1': False, 'level': 1})
            i += 1; continue
        if lvl == 2:
            toc_entries.append({'kind': 'topic', 'ui': ui,
                                'label': txt.replace('*', '').replace('`', ''),
                                'measure': txt, 'is_unit_h1': False, 'level': 1})
        elif lvl == 3:
            toc_entries.append({'kind': 'sub', 'ui': ui,
                                'label': txt.replace('*', '').replace('`', ''),
                                'measure': txt, 'is_unit_h1': False, 'level': 2})
        elif lvl == 4:
            toc_entries.append({'kind': 'branch', 'ui': ui,
                                'label': txt.replace('*', '').replace('`', ''),
                                'measure': txt, 'is_unit_h1': False, 'level': 3})
        i += 1

def render_toc(entries, use_pages=False):
    lines = ["# Index of Topics, Sub-Topics & Branches", "",
             "> This index lists every topic (##), sub-topic (###) and branch (####) across the ten Week-02 units, with the printed page number on which each begins.",
             ""]
    for e in entries:
        indent = "  " * e['level']
        label = e['label']
        if e['kind'] in ('unit', 'topic'):
            label = f"**{label}**"
        elif e['kind'] in ('src', 'ret'):
            label = f"*{label}*"
        if use_pages and e.get('page') is not None:
            pg = f"{e['page']:03d}"
        else:
            pg = "000"
        lines.append(f"{indent}- {label} … p.{pg}")
    lines.append("")
    lines.append("END-OF-MASTER-INDEX")
    return "\n".join(lines)

FRONTMATTER = """---
title: "ASE Week 02 — Master Lecture: Software Process Models (Units 01–10)"
subtitle: "From Build-and-Fix to Agile — the complete Week-02 lecture series"
subject: "04_Advanced_Software_Eng"
course: "CS504 — Advanced Software Engineering"
instructor: "Asst. Prof. Dr. Ali Fahim Ni'ma"
term: "Fall 2026"
week: "Week 02"
type: "merged master lecture"
---
"""

def build_master(toc_md, bodies):
    return FRONTMATTER + "\n" + toc_md + "\n\n" + "\n\n".join(bodies) + "\n"

master_path = NOTES / "Week_02_Master_Lecture.md"

# ---- Pass 2: placeholder TOC (zero-padded 000) ----
master_md = build_master(render_toc(toc_entries, use_pages=False), bodies)
master_path.write_text(master_md, encoding='utf-8')

pass2_pdf = OUTDIR / "_master_pass2.pdf"
# NOTE: on this Windows box the safe-delete shim intercepts unlink() and routes it
# to a trash op that FAILS (fail-closed). Swallow it; the exporter overwrites pass2.
if pass2_pdf.exists():
    try:
        pass2_pdf.unlink()
    except OSError:
        pass
pdf_exporter.export_markdown_to_pdf(
    master_path, output_pdf_path=pass2_pdf, template="booklet", lang="ar",
    course_override=COURSE, prof_override=PROF, term_override=TERM
)
print(f"[*] Pass2 rendered: {pass2_pdf}")

# ---- Measure on pass2 (use the file the exporter ACTUALLY wrote) ----
pass2_pdf = resolve_out(pass2_pdf)
print(f"[*] Measuring from: {pass2_pdf}")
doc = fitz.open(pass2_pdf)
pages_text = [norm(doc[i].get_text()) for i in range(len(doc))]
total = len(doc)
sentinel_pat = re.compile(r"END-OF-MASTER-INDEX")
sentinel_idx = next((p for p in range(total) if sentinel_pat.search(pages_text[p])), None)
assert sentinel_idx is not None, "Sentinel not found!"
content_start = sentinel_idx + 1
print(f"[*] Cover=page1; TOC spans indices 1..{sentinel_idx} (pages 2..{sentinel_idx+1}); content starts index {content_start}")

unit_idx = [None] * 10
# Start at the sentinel page itself: Unit 01's real H1 shares the sentinel page,
# so content_start (= sentinel_idx+1) would skip it.
last = sentinel_idx
for e in toc_entries:
    if not e.get('is_unit_h1'):
        continue
    ui = e['ui']
    pat = unit_pattern(ui, e['measure'])
    found = next((p for p in range(last, total) if pat.search(pages_text[p])), None)
    unit_idx[ui - 1] = found
    if found is not None:
        last = found + 1
print("[*] Unit start pages (1-based):", [(u + 1) if u is not None else None for u in unit_idx])

for e in toc_entries:
    ui = e['ui']
    start = unit_idx[ui - 1]
    end = unit_idx[ui] if (ui < 10 and unit_idx[ui] is not None) else total
    if e['is_unit_h1']:
        e['page'] = (start + 1) if start is not None else None
    else:
        pat = make_pattern(e['measure'])
        s = start if start is not None else content_start
        fp = next((p for p in range(s, end) if pat.search(pages_text[p])), None)
        e['page'] = (fp + 1) if fp is not None else None

print("\n[*] TOC page map:")
for e in toc_entries:
    print(f"  [{e['kind']:5}] {e['label'][:62]:62} -> p.{e.get('page')}")

# ---- Pass 3: final with real page numbers ----
master_md_final = build_master(render_toc(toc_entries, use_pages=True), bodies)
master_path.write_text(master_md_final, encoding='utf-8')
final_pdf = OUTDIR / "Week_02_Master_Lecture.pdf"
# Safe-delete shim may fail on this box; swallow and let the exporter overwrite.
if final_pdf.exists():
    try:
        final_pdf.unlink()
    except OSError:
        pass
pdf_exporter.export_markdown_to_pdf(
    master_path, output_pdf_path=final_pdf, template="booklet", lang="ar",
    course_override=COURSE, prof_override=PROF, term_override=TERM
)
# The exporter writes to <stem>_new.pdf when the canonical is locked by a viewer.
# Resolve the file it actually produced, then try to swap it onto the canonical name.
final_pdf = resolve_out(final_pdf)
canon_name = OUTDIR / "Week_02_Master_Lecture.pdf"
swapped = False
if final_pdf.resolve() != canon_name.resolve():
    swapped = swap_to_canonical(final_pdf, canon_name)
    if swapped:
        final_pdf = canon_name
print(f"[*] Final rendered: {final_pdf}")
if not swapped and final_pdf.resolve() != canon_name.resolve():
    print(f"[!] NOTICE: canonical {canon_name.name} is locked by a viewer; "
          f"current verified render kept at {final_pdf.name}")

# ---- Verify ----
doc2 = fitz.open(final_pdf)
tot2 = len(doc2)
cover_text = norm(doc2[0].get_text())
assert "UNIVERSITY OF WASIT" in cover_text, "Cover missing!"
pages_text2 = [norm(doc2[i].get_text()) for i in range(tot2)]
sentinel_idx2 = next((p for p in range(tot2) if sentinel_pat.search(pages_text2[p])), None)
cs2 = sentinel_idx2 + 1
unit_idx2 = [None] * 10
# Start at the sentinel page itself (Unit 01's H1 shares it with the sentinel).
last2 = sentinel_idx2
unit_titles = [e['measure'] for e in toc_entries if e.get('is_unit_h1')]
for ui, title in enumerate(unit_titles, start=1):
    pat = unit_pattern(ui, title)
    found = next((p for p in range(last2, tot2) if pat.search(pages_text2[p])), None)
    unit_idx2[ui - 1] = found
    if found is not None:
        last2 = found + 1
mismatch = 0
for e in toc_entries:
    if e['is_unit_h1']:
        exp = (unit_idx2[e['ui'] - 1] + 1) if unit_idx2[e['ui'] - 1] is not None else None
    else:
        ui = e['ui']; start = unit_idx2[ui - 1]
        end = unit_idx2[ui] if (ui < 10 and unit_idx2[ui] is not None) else tot2
        pat = make_pattern(e['measure'])
        s = start if start is not None else cs2
        fp = next((p for p in range(s, end) if pat.search(pages_text2[p])), None)
        exp = (fp + 1) if fp is not None else None
    if exp != e['page']:
        mismatch += 1
        print(f"  [MISMATCH] {e['label'][:50]} final={exp} pass2={e['page']}")
print(f"[*] Total pages (final): {tot2}")
print(f"[*] Pagination mismatches vs Pass2: {mismatch}")
print("[*] Unit start pages (final, 1-based):", [(u + 1) if u is not None else None for u in unit_idx2])

none_pages = [e['label'] for e in toc_entries if e.get('page') is None]
if none_pages:
    print(f"[!] WARNING: {len(none_pages)} TOC entries have NO measured page (would render p.000):")
    for n in none_pages:
        print(f"      - {n}")
else:
    print("[OK] Every TOC entry resolved to a confirmed page number (no p.000 left).")

try:
    pass2_pdf.unlink()
except Exception:
    pass
print("[*] Done.")
