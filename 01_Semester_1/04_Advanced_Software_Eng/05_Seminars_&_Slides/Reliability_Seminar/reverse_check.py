"""Reverse extraction check (tolerant to OCR noise): how much of each paragraph
is literally traceable to the sources?"""
import difflib
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = Path(__file__).resolve().parent
MD = BASE / "ch7_part1.md"
CORPUS_FILES = [
    BASE / "sources" / "book_ch7_ocr.txt",
    BASE / "SOURCE_ch7_slides.txt",
    BASE / "_reliab_sources.txt",
    BASE / "_quality_sources.txt",
]


def words(s):
    return re.findall(r"[a-z0-9]+", s.lower())


# ---- corpus chunks -------------------------------------------------------
chunks = []
for f in CORPUS_FILES:
    if not f.exists():
        continue
    txt = f.read_text(encoding="utf-8", errors="replace")
    for part in re.split(r"#####[^\n]*#####", txt):
        w = words(part)
        if len(w) > 40:
            chunks.append(w)
print(f"corpus chunks: {len(chunks)}  words: {sum(len(c) for c in chunks):,}")

chunk_sets = [set(c) for c in chunks]

# ---- paragraphs ----------------------------------------------------------
md = MD.read_text(encoding="utf-8").split("\n")
section = "(front)"
rows = []
for line in md:
    s = line.strip()
    if s.startswith("## "):
        section = s[3:].strip()
        continue
    if (not s or s[0] in "#|!*-" or s.startswith("1.") or s.startswith("2.")
            or s.startswith("3.") or s.startswith("**Table")):
        continue
    w = words(s)
    if len(w) < 12:
        continue
    rows.append((section, s, w))

print(f"paragraphs: {len(rows)}")

results = []
for section, s, w in rows:
    # candidate chunks by content-word overlap
    content = {t for t in w if len(t) > 3}
    scored = sorted(((len(content & cs), i) for i, cs in enumerate(chunk_sets)), reverse=True)[:3]
    best = 0.0
    for _, i in scored:
        sm = difflib.SequenceMatcher(None, w[:220], chunks[i], autojunk=False)
        matched = sum(b.size for b in sm.get_matching_blocks())
        best = max(best, matched / min(len(w), 220))
    results.append((best, section, s))

mean = sum(r[0] for r in results) / len(results)
print(f"mean literal coverage: {mean:.1%}")

by = {}
for h, sec, _ in results:
    by.setdefault(sec, []).append(h)
print("\nper-section:")
for sec, v in by.items():
    print(f"  {sum(v)/len(v):5.1%}  n={len(v):3d}  {sec}")

low = sorted([r for r in results if r[0] < 0.35])
print(f"\nbelow 35%: {len(low)}")
for h, sec, s in low[:12]:
    print(f"  {h:5.0%} [{sec[:18]}] {s[:80]}")

with open(BASE / "reverse_report.txt", "w", encoding="utf-8") as fh:
    fh.write(f"mean {mean:.3f} | paragraphs {len(results)}\n\n")
    for h, sec, s in sorted(results):
        fh.write(f"{h:.3f}\t{sec}\t{s}\n")
print("\nreport -> reverse_report.txt")
