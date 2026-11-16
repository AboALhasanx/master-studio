#!/usr/bin/env python3
"""
OCR / VLM Transcription Benchmark Harness
------------------------------------------
Measures transcription fidelity of any engine (VLM web transcript, PDF search
layer, local OCR) against a gold reference set, so that "which engine is
better" becomes a number instead of an impression.

Design rules (do not break them, or scores stop being comparable):

1. ONE normalization pipeline feeds every system. Gold text and hypothesis text
   go through the exact same function, so a measured difference reflects the
   engine, not the preprocessing.
2. Metrics are reported on a whitespace-collapsed page string (case and
   punctuation preserved), so line wrapping and paragraph reflow are ignored.
3. Omission and hallucination rates are derived from the character alignment
   (deletions / insertions), not from a separate fuzzy pass.
4. `drift` counts *normalization drift*: positions where the source prints a
   misspelling and the engine silently emits the dictionary-correct spelling.
   That failure mode is invisible to plain CER and is the one that matters for
   faithful transcription.
5. No book text is stored in this file. Gold and hypothesis corpora live under
   the gitignored raw-materials tree and are passed in as directories.

Subcommands
    gold          build gold reference pages from chapter Markdown transcripts
    search-layer  dump the PDF's embedded OCR text layer as a hypothesis
    rapidocr      run local RapidOCR over rendered page images as a hypothesis
    score         score one hypothesis directory against the gold directory
    triage        cross-system agreement table (for human-review budgeting)

Usage
    python ocr_bench.py gold --chapter 1 --pages 1-19 --md New/Ch01_Introduction.md
    python ocr_bench.py search-layer --pdf book.pdf --pages 1-19 --pdf-offset 20 --out DIR
    python ocr_bench.py rapidocr --manifest MANIFEST.json --out DIR
    python ocr_bench.py score --gold DIR --hyp DIR --name vlm_web
    python ocr_bench.py triage --gold DIR --hyp-a DIR --hyp-b DIR
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import time
from pathlib import Path
from typing import Any, Iterable

import numpy as np

# --------------------------------------------------------------------------
# Repository layout
# --------------------------------------------------------------------------

TOOLS_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLS_DIR.parents[1]
RAW_ROOT = VAULT_ROOT / "01_Semester_1/04_Advanced_Software_Eng/02_Raw_Materials"
BOOK_ROOT = RAW_ROOT / "Aggarwal_SE_3rdEd_COMPLETE"
BENCH_ROOT = BOOK_ROOT / "_digitizer/bench"

# --------------------------------------------------------------------------
# Normalization (shared by every system)
# --------------------------------------------------------------------------

PAGE_HEADING = re.compile(r"(?m)^#{2,6}\s*Printed page (\d+)\s*$")

# Running headers, folios, and their split-line forms.
_FURNITURE_NAMES = (
    r"Introduction to Software Engineering|Software Life Cycle Models|Software Engineering"
)
FURNITURE = re.compile(
    rf"^(?:(?:\d+\s*)?(?:{_FURNITURE_NAMES})(?:\s*\d+)?|\d+)$"
)
BULLET = re.compile(r"^(?:[-*+]\s+|\(?\d+[.)]\s+|\(?[ivxIVX]{1,4}[.)]\s+)")
TABLE_SEP = re.compile(r"^\|(?:\s*[-:]+(?:\s*\|\s*[-:]+)*\s*\|)$")
IMAGE_LINE = re.compile(r"^\[Image:")
HYPHEN_BREAK = re.compile(r"(?<=\w)-\s*\n\s*(?=\w)")
WORD = re.compile(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)*")
CHAR = re.compile(r"\S")


def _table_row(line: str) -> str:
    """Render a Markdown table row as pipe-joined cells (structure preserved)."""
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return " | ".join(c for c in cells if c)


def _clean_block(block: str) -> str:
    """Clean one paragraph block: strip markdown furniture, keep the words."""
    out_lines: list[str] = []
    for raw_line in block.split("\n"):
        line = raw_line.strip()
        if not line:
            continue
        if IMAGE_LINE.match(line):
            continue
        if TABLE_SEP.match(line):
            continue
        if line.startswith("|"):
            line = _table_row(line)
        line = re.sub(r"^#{1,6}\s*", "", line)
        line = BULLET.sub("", line)
        line = line.replace("**", "").replace("__", "").replace("`", "")
        line = line.replace("[unclear]", "")
        line = line.replace("*", "").replace("_", "")
        if not line.strip():
            continue
        if FURNITURE.match(line.strip()):
            continue
        out_lines.append(line.strip())
    if not out_lines:
        return ""
    joined = "\n".join(out_lines)
    joined = HYPHEN_BREAK.sub("", joined)
    return " ".join(joined.split())


def normalize_page(raw: str) -> str:
    """Whole-page normalized string used for every character/word metric."""
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    blocks = re.split(r"\n\s*\n", text)
    kept = [b for b in (_clean_block(b) for b in blocks) if b]
    return " ".join(kept)


def normalize_lines(raw: str) -> list[str]:
    """Paragraph-level units, used for optional line-level diagnostics."""
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    blocks = re.split(r"\n\s*\n", text)
    return [b for b in (_clean_block(b) for b in blocks) if b]


# --------------------------------------------------------------------------
# Edit distance with alignment breakdown (numpy DP, exact Levenshtein)
# --------------------------------------------------------------------------


def levenshtein_seq(a: Sequence[str], b: Sequence[str]) -> int:
    """Exact Levenshtein distance over two sequences of items."""
    n, m = len(a), len(b)
    if n == 0:
        return m
    if m == 0:
        return n
    if m > n:  # keep the inner dimension short
        a, b = b, a
        n, m = m, n
    idx = np.arange(m + 1, dtype=np.int32)
    arr_a = np.array(list(a), dtype="<U4")
    arr_b = np.array(list(b), dtype="<U4")
    prev = idx.copy()
    for i in range(1, n + 1):
        cost = (arr_a[i - 1] != arr_b).astype(np.int32)
        base = np.empty(m + 1, dtype=np.int32)
        base[0] = i
        base[1:] = np.minimum(prev[1:] + 1, prev[:-1] + cost)
        prev = np.minimum.accumulate(base - idx) + idx
    return int(prev[m])


def levenshtein(a: str, b: str) -> int:
    """Exact Levenshtein distance over characters."""
    return levenshtein_seq(list(a), list(b))


def diff_breakdown(a: Sequence[str], b: Sequence[str]) -> dict[str, int]:
    """Alignment breakdown via difflib opcodes: equal / sub / ins / del."""
    matcher = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    equal = sub = ins = dele = 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            equal += i2 - i1
        elif tag == "replace":
            len_a, len_b = i2 - i1, j2 - j1
            common = min(len_a, len_b)
            sub += common
            dele += len_a - common
            ins += len_b - common
        elif tag == "delete":
            dele += i2 - i1
        elif tag == "insert":
            ins += j2 - j1
    return {"equal": equal, "sub": sub, "ins": ins, "del": dele}


def align_counts(a: str, b: str) -> dict[str, int]:
    """Exact Levenshtein distance plus a diff-based alignment breakdown (chars)."""
    counts = diff_breakdown(list(a), list(b))
    counts["distance"] = levenshtein(a, b)
    return counts


def token_ops(a: str, b: str) -> dict[str, int]:
    """Word-level alignment counts: one token = one unit of edit distance."""
    ta = WORD.findall(a.lower())
    tb = WORD.findall(b.lower())
    counts = diff_breakdown(ta, tb)
    counts["distance"] = levenshtein_seq(ta, tb)
    return counts


# --------------------------------------------------------------------------
# Normalization-drift dictionary (verified printed typos)
# --------------------------------------------------------------------------

# (printed_form, dictionary_form) pairs confirmed by reading the book scans.
DRIFT_PAIRS: list[tuple[str, str]] = [
    ("complier", "compiler"),
    ("possiple", "possible"),
    ("PRESOI", "PRES01"),
    ("Mangement", "Management"),
    ("Interal", "Internal"),
    ("Evalution", "Evolution"),
    ("embarrasing", "embarrassing"),
    ("forcast", "forecast"),
    ("accomodate", "accommodate"),
    ("accomodated", "accommodated"),
    ("accomodating", "accommodating"),
    ("interative", "iterative"),
    ("interative", "interactive"),
    ("Turnout", "turnout"),
]


def drift_events(gold: str, hyp: str) -> dict[str, Any]:
    """Count printed typos that the engine silently 'corrected'."""
    events: list[dict[str, str]] = []
    faithful = 0
    for printed, corrected in DRIFT_PAIRS:
        if printed not in gold:
            continue
        if printed in hyp:
            faithful += 1
        elif corrected in hyp:
            events.append({"printed": printed, "emitted": corrected})
    return {
        "drift_events": events,
        "drift_count": len(events),
        "faithful_typo_count": faithful,
    }


# --------------------------------------------------------------------------
# Scoring
# --------------------------------------------------------------------------


def score_text(gold: str, hyp: str) -> dict[str, Any]:
    c = align_counts(gold, hyp)
    w = token_ops(gold, hyp)
    gold_chars = max(1, len(gold))
    hyp_chars = max(1, len(hyp))
    gold_words = max(1, len(WORD.findall(gold.lower())))
    hyp_words = max(1, len(WORD.findall(hyp.lower())))
    result = {
        "gold_chars": len(gold),
        "hyp_chars": len(hyp),
        "gold_words": gold_words,
        "hyp_words": hyp_words,
        "char_edits": c["distance"],
        "cer": c["distance"] / gold_chars,
        "word_edits": w["distance"],
        "wer": w["distance"] / gold_words,
        "omission_rate": c["del"] / gold_chars,
        "substitution_rate": c["sub"] / gold_chars,
        "insertion_rate": c["ins"] / hyp_chars,
        "word_omission_rate": w["del"] / gold_words,
        "word_insertion_rate": w["ins"] / hyp_words,
    }
    result.update(drift_events(gold, hyp))
    return result


def _read_corpus(directory: Path) -> dict[str, str]:
    corpus: dict[str, str] = {}
    for path in sorted(directory.glob("*.txt")):
        corpus[path.stem] = path.read_text(encoding="utf-8")
    return corpus


def cmd_score(args: argparse.Namespace) -> int:
    gold_dir = Path(args.gold)
    hyp_dir = Path(args.hyp)
    gold = {k: normalize_page(v) for k, v in _read_corpus(gold_dir).items()}
    hyp = {k: normalize_page(v) for k, v in _read_corpus(hyp_dir).items()}
    keys = sorted(set(gold) & set(hyp))
    missing = sorted(set(gold) - set(hyp))
    extra = sorted(set(hyp) - set(gold))

    rows: list[dict[str, Any]] = []
    for key in keys:
        row = {"page": key}
        row.update(score_text(gold[key], hyp[key]))
        rows.append(row)

    agg = {
        "pages": len(rows),
        "gold_chars": sum(r["gold_chars"] for r in rows),
        "hyp_chars": sum(r["hyp_chars"] for r in rows),
        "gold_words": sum(r["gold_words"] for r in rows),
        "hyp_words": sum(r["hyp_words"] for r in rows),
        "char_edits": sum(r["char_edits"] for r in rows),
        "word_edits": sum(r["word_edits"] for r in rows),
    }
    agg["cer"] = agg["char_edits"] / max(1, agg["gold_chars"])
    agg["wer"] = agg["word_edits"] / max(1, agg["gold_words"])
    agg["omission_rate"] = sum(r["omission_rate"] * r["gold_chars"] for r in rows) / max(1, agg["gold_chars"])
    agg["insertion_rate"] = sum(r["insertion_rate"] * r["hyp_chars"] for r in rows) / max(1, agg["hyp_chars"])
    agg["drift_events"] = sum(r["drift_count"] for r in rows)

    payload = {
        "system": args.name,
        "gold_dir": str(gold_dir),
        "hyp_dir": str(hyp_dir),
        "aggregate": agg,
        "per_page": rows,
        "pages_missing_hypothesis": missing,
        "pages_missing_gold": extra,
    }
    out_json = Path(args.out_json) if args.out_json else None
    if out_json:
        out_json.parent.mkdir(parents=True, exist_ok=True)
        out_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    lines = [
        f"# OCR benchmark — {args.name}",
        "",
        f"- Gold: `{gold_dir}`  ({len(gold)} pages)",
        f"- Hypothesis: `{hyp_dir}`  ({len(hyp)} pages, {len(rows)} scored)",
        "",
        "## Aggregate",
        "",
        "| metric | value |",
        "|---|---|",
        f"| pages scored | {agg['pages']} |",
        f"| CER (character edit distance / gold chars) | {agg['cer'] * 100:.3f}% |",
        f"| WER (word edit distance / gold words) | {agg['wer'] * 100:.3f}% |",
        f"| omission rate (deleted chars / gold chars) | {agg['omission_rate'] * 100:.3f}% |",
        f"| insertion rate (inserted chars / hyp chars) | {agg['insertion_rate'] * 100:.3f}% |",
        f"| normalization-drift events (source typos silently corrected) | {agg['drift_events']} |",
        f"| gold characters | {agg['gold_chars']} |",
        f"| hypothesis characters | {agg['hyp_chars']} |",
        "",
        "## Per page",
        "",
        "| page | CER | WER | omission | insertion | drift |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['page']} | {row['cer'] * 100:.2f}% | {row['wer'] * 100:.2f}% | "
            f"{row['omission_rate'] * 100:.2f}% | {row['insertion_rate'] * 100:.2f}% | {row['drift_count']} |"
        )
    if missing:
        lines += ["", f"## Pages with no hypothesis", ""] + [f"- {k}" for k in missing]
    report = "\n".join(lines) + "\n"
    out_md = Path(args.out_md) if args.out_md else None
    if out_md:
        out_md.parent.mkdir(parents=True, exist_ok=True)
        out_md.write_text(report, encoding="utf-8")
    print(report)
    return 0


# --------------------------------------------------------------------------
# Corpus builders
# --------------------------------------------------------------------------


def split_pages_by_heading(text: str) -> dict[int, str]:
    """Split a transcript into printed pages.

    A page section ends at the next printed-page heading *or* at the next
    level-2/3 heading (batch headers, the correction log). Without the second
    rule the last page of a chapter silently swallows the audit log.
    """
    pages: dict[int, str] = {}
    matches = list(PAGE_HEADING.finditer(text))
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        section = text[match.end():end]
        stop = re.search(r"(?m)^#{1,3}\s+\S", section)
        if stop:
            section = section[:stop.start()]
        pages[int(match.group(1))] = section
    return pages


def cmd_gold(args: argparse.Namespace) -> int:
    md_path = Path(args.md)
    text = md_path.read_text(encoding="utf-8")
    pages = split_pages_by_heading(text)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    written = 0
    for printed in range(args.pages[0], args.pages[1] + 1):
        if printed not in pages:
            print(f"WARN: printed page {printed} not found in {md_path}", file=sys.stderr)
            continue
        key = f"ch{args.chapter:02d}_p{printed:03d}"
        (out_dir / f"{key}.txt").write_text(pages[printed], encoding="utf-8")
        written += 1
    print(f"gold: wrote {written} pages to {out_dir}")
    return 0


def cmd_search_layer(args: argparse.Namespace) -> int:
    import pymupdf

    doc = pymupdf.open(args.pdf)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    written = 0
    for printed in range(args.pages[0], args.pages[1] + 1):
        # pdf_offset is the 1-based PDF page of the first printed page
        index = printed + args.pdf_offset - 1
        if index < 0 or index >= doc.page_count:
            print(f"WARN: PDF index {index} out of range", file=sys.stderr)
            continue
        key = f"ch{args.chapter:02d}_p{printed:03d}"
        text = doc[index].get_text("text")
        (out_dir / f"{key}.txt").write_text(text, encoding="utf-8")
        written += 1
    print(f"search-layer: wrote {written} pages to {out_dir}")
    return 0


def cmd_rapidocr(args: argparse.Namespace) -> int:
    try:
        from rapidocr_onnxruntime import RapidOCR
    except ImportError as exc:  # pragma: no cover
        print(f"rapidocr_onnxruntime not available: {exc}", file=sys.stderr)
        return 2

    engine = RapidOCR()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    timings: list[tuple[str, float]] = []
    for manifest_path in args.manifest:
        manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
        for item in manifest["pages"]:
            printed = item["printed_page"]
            chapter = args.chapter if isinstance(args.chapter, int) else (1 if printed <= 19 else 2)
            image = Path(manifest_path).parent / item["image"]
            started = time.perf_counter()
            result, _ = engine(str(image))
            elapsed = time.perf_counter() - started
            key = f"ch{chapter:02d}_p{printed:03d}"
            timings.append((key, elapsed))
            boxes = []
            for entry in result or []:
                box, text = entry[0], entry[1]
                xs = [pt[0] for pt in box]
                ys = [pt[1] for pt in box]
                boxes.append((min(ys), min(xs), text))
            boxes.sort(key=lambda b: (round(b[0] / 12), b[1]))
            joined = "\n".join(b[2] for b in boxes)
            (out_dir / f"{key}.txt").write_text(joined, encoding="utf-8")
    total = sum(t for _, t in timings)
    print(f"rapidocr: wrote {len(timings)} pages to {out_dir}; {total:.1f}s total, {total / max(1, len(timings)):.1f}s/page")
    (out_dir / "_timings.json").write_text(json.dumps(dict(timings), indent=2), encoding="utf-8")
    return 0


def cmd_df(args: argparse.Namespace) -> int:
    """Document frequency of layer tokens over a PDF page range (cache for repair rules)."""
    import pymupdf

    doc = pymupdf.open(args.pdf)
    counts: dict[str, int] = {}
    for index in range(args.pdf_first - 1, args.pdf_last):
        if index < 0 or index >= doc.page_count:
            continue
        for token in WORD.findall(doc[index].get_text("text").lower()):
            counts[token] = counts.get(token, 0) + 1
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(counts, ensure_ascii=False), encoding="utf-8")
    print(f"df: {len(counts)} distinct tokens over PDF pages {args.pdf_first}-{args.pdf_last} -> {args.out}")
    return 0


def cmd_hybrid(args: argparse.Namespace) -> int:
    """Repair a VLM transcript against the PDF search layer.

    Rule (source-anchored, no external word list):
      align hypothesis words with layer words; where the layer offers a RARE
      source token that is one edit away from a COMMON hypothesis token, the
      hypothesis token is a dictionary normalization of a printed misspelling,
      so restore the printed form.
    """
    df = json.loads(Path(args.df).read_text(encoding="utf-8"))
    layer_dir = Path(args.layer)
    hyp_dir = Path(args.hyp)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    repaired_total = 0
    detail: list[dict[str, Any]] = []
    for path in sorted(hyp_dir.glob("*.txt")):
        key = path.stem
        layer_path = layer_dir / f"{key}.txt"
        hyp_text = path.read_text(encoding="utf-8")
        if not layer_path.is_file():
            (out_dir / f"{key}.txt").write_text(hyp_text, encoding="utf-8")
            continue
        hyp_spans = [(m.group(0), m.start(), m.end()) for m in WORD.finditer(hyp_text)]
        hyp_words = [s[0] for s in hyp_spans]
        layer_words = WORD.findall(layer_path.read_text(encoding="utf-8").lower())
        matcher = difflib.SequenceMatcher(a=hyp_words, b=layer_words, autojunk=False)
        repairs: list[tuple[int, str, str]] = []
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag != "replace":
                continue
            for offset in range(i2 - i1):
                hyp_token = hyp_words[i1 + offset]
                hyp_df = df.get(hyp_token, 0)
                if hyp_df < args.min_df:
                    continue
                if len(hyp_token) < args.min_len:
                    continue
                best: tuple[int, str] | None = None
                for cand in layer_words[j1:j2]:
                    cand_df = df.get(cand, 0)
                    if cand_df > args.max_df:
                        continue
                    if args.require_df_one and cand_df != 1:
                        continue
                    if args.same_length and len(cand) != len(hyp_token):
                        continue
                    if args.no_substring and cand in hyp_token:
                        continue
                    if args.no_digit and any(ch.isdigit() for ch in cand):
                        continue
                    distance = levenshtein_seq(list(hyp_token), list(cand))
                    if distance <= args.max_edit and (best is None or distance < best[0]):
                        best = (distance, cand)
                if best and best[1] != hyp_token:
                    repairs.append((i1 + offset, hyp_token, best[1]))
        # apply repairs on the original text so punctuation and spacing survive
        repaired = hyp_text
        for index, old, new in sorted(repairs, key=lambda r: -r[0]):
            start = hyp_spans[index][1]
            end = hyp_spans[index][2]
            repaired = repaired[:start] + new + repaired[end:]
        (out_dir / f"{key}.txt").write_text(repaired, encoding="utf-8")
        if repairs:
            repaired_total += len(repairs)
            detail.append({"page": key, "repairs": [{"from": o, "to": n} for _, o, n in repairs]})
    print(f"hybrid: {len(list(out_dir.glob('*.txt')))} pages, {repaired_total} tokens repaired")
    for item in detail:
        pairs = ", ".join(f"{r['from']}->{r['to']}" for r in item["repairs"])
        print(f"  {item['page']}: {pairs}")
    if args.out_json:
        Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out_json).write_text(json.dumps(detail, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


def cmd_funnel(args: argparse.Namespace) -> int:
    """Does agreement between two independent engines predict human-review need?

    Production has no gold set, so the triage signal must be self-referential:
    how much do two independent systems agree on a page? This validates that
    proxy against a gold set: for each agreement bucket it reports the true
    error of system A, so we can state how many pages may be auto-accepted.
    """
    gold = {k: normalize_page(v) for k, v in _read_corpus(Path(args.gold)).items()}
    a = {k: normalize_page(v) for k, v in _read_corpus(Path(args.hyp_a)).items()}
    b = {k: normalize_page(v) for k, v in _read_corpus(Path(args.hyp_b)).items()}
    keys = sorted(set(gold) & set(a) & set(b))

    rows = []
    for key in keys:
        agree = 1.0 - (levenshtein(a[key], b[key]) / max(1, len(a[key])))
        truth = score_text(gold[key], a[key])
        rows.append({"page": key, "agreement": agree, "true_cer": truth["cer"], "true_wer": truth["wer"]})

    edges = [0.0, 0.90, 0.95, 0.99, 0.999, 1.0]
    buckets: list[dict[str, Any]] = []
    for lo, hi in zip(edges, edges[1:]):
        members = [r for r in rows if lo <= r["agreement"] < hi or (hi == 1.0 and r["agreement"] >= 1.0)]
        if not members:
            continue
        buckets.append({
            "agreement_band": f"[{lo:.3f}, {hi:.3f})",
            "pages": len(members),
            "mean_true_cer": sum(m["true_cer"] for m in members) / len(members),
            "worst_true_cer": max(m["true_cer"] for m in members),
            "pages_true_cer_over_1pct": sum(1 for m in members if m["true_cer"] > 0.01),
        })

    threshold = args.threshold
    accepted = [r for r in rows if r["agreement"] >= threshold]
    bad = [r for r in accepted if r["true_cer"] > args.max_true_cer]
    payload = {
        "pages": len(rows),
        "threshold": threshold,
        "auto_accepted": len(accepted),
        "auto_accepted_share": len(accepted) / max(1, len(rows)),
        "auto_accepted_beyond_max_true_cer": len(bad),
        "escaped_pages": [r["page"] for r in bad],
        "buckets": buckets,
        "per_page": rows,
    }
    print(f"# Review funnel — {args.hyp_a} vs {args.hyp_b}\n")
    print(f"- pages: {len(rows)}")
    print(f"- auto-accept rule: agreement >= {threshold:.3%} and true CER <= {args.max_true_cer:.2%}")
    print(f"- auto-accepted: {len(accepted)} ({len(accepted) / max(1, len(rows)):.1%})")
    print(f"- auto-accepted pages that would have been wrong: {len(bad)} ({[r['page'] for r in bad]})\n")
    print("| agreement band | pages | mean true CER | worst true CER | pages over 1% CER |")
    print("|---|---:|---:|---:|---:|")
    for bucket in buckets:
        print(
            f"| {bucket['agreement_band']} | {bucket['pages']} | {bucket['mean_true_cer'] * 100:.2f}% | "
            f"{bucket['worst_true_cer'] * 100:.2f}% | {bucket['pages_true_cer_over_1pct']} |"
        )
    if args.out_json:
        Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out_json).write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


def cmd_triage(args: argparse.Namespace) -> int:
    gold = {k: normalize_page(v) for k, v in _read_corpus(Path(args.gold)).items()}
    a = {k: normalize_page(v) for k, v in _read_corpus(Path(args.hyp_a)).items()}
    b = {k: normalize_page(v) for k, v in _read_corpus(Path(args.hyp_b)).items()}
    keys = sorted(set(gold) & set(a) & set(b))
    buckets = {"auto_accept": 0, "review": 0, "blocked": 0}
    rows = []
    for key in keys:
        sa = score_text(gold[key], a[key])
        sb = score_text(gold[key], b[key])
        worst = max(sa["cer"], sb["cer"])
        if worst <= args.auto_threshold:
            bucket = "auto_accept"
        elif worst <= args.review_threshold:
            bucket = "review"
        else:
            bucket = "blocked"
        buckets[bucket] += 1
        rows.append({"page": key, "bucket": bucket, "cer_a": sa["cer"], "cer_b": sb["cer"]})
    print(f"# Triage — {len(keys)} pages\n")
    print("| bucket | pages | rule |")
    print("|---|---:|---|")
    print(f"| auto_accept | {buckets['auto_accept']} | worst CER <= {args.auto_threshold:.1%} |")
    print(f"| review | {buckets['review']} | worst CER <= {args.review_threshold:.1%} |")
    print(f"| blocked | {buckets['blocked']} | worst CER > {args.review_threshold:.1%} |")
    print("\n| page | bucket | CER a | CER b |")
    print("|---|---|---:|---:|")
    for row in rows:
        print(f"| {row['page']} | {row['bucket']} | {row['cer_a'] * 100:.2f}% | {row['cer_b'] * 100:.2f}% |")
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def _pages(value: str) -> tuple[int, int]:
    if "-" in value:
        start, end = value.split("-", 1)
        return int(start), int(end)
    number = int(value)
    return number, number


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_gold = sub.add_parser("gold", help="build gold reference pages from a chapter transcript")
    p_gold.add_argument("--chapter", type=int, required=True)
    p_gold.add_argument("--pages", type=_pages, required=True)
    p_gold.add_argument("--md", required=True)
    p_gold.add_argument("--out", required=True)
    p_gold.set_defaults(func=cmd_gold)

    p_layer = sub.add_parser("search-layer", help="dump the PDF OCR text layer as a hypothesis")
    p_layer.add_argument("--pdf", required=True)
    p_layer.add_argument("--chapter", type=int, default=1)
    p_layer.add_argument("--pages", type=_pages, required=True)
    p_layer.add_argument("--pdf-offset", type=int, default=0, help="1-based PDF page of the first printed page (e.g. 20 => printed 1 is PDF page 20)")
    p_layer.add_argument("--out", required=True)
    p_layer.set_defaults(func=cmd_search_layer)

    p_rapid = sub.add_parser("rapidocr", help="run local RapidOCR over rendered page images")
    p_rapid.add_argument("--manifest", nargs="+", required=True)
    p_rapid.add_argument("--chapter", default="auto", help="chapter number, or 'auto' (1 for pages<=19, else 2)")
    p_rapid.add_argument("--out", required=True)
    p_rapid.set_defaults(func=cmd_rapidocr)

    p_score = sub.add_parser("score", help="score a hypothesis corpus against gold")
    p_score.add_argument("--gold", required=True)
    p_score.add_argument("--hyp", required=True)
    p_score.add_argument("--name", required=True)
    p_score.add_argument("--out-md")
    p_score.add_argument("--out-json")
    p_score.set_defaults(func=cmd_score)

    p_df = sub.add_parser("df", help="document frequency of layer tokens over a PDF range")
    p_df.add_argument("--pdf", required=True)
    p_df.add_argument("--pdf-first", type=int, required=True)
    p_df.add_argument("--pdf-last", type=int, required=True)
    p_df.add_argument("--out", required=True)
    p_df.set_defaults(func=cmd_df)

    p_hybrid = sub.add_parser("hybrid", help="repair a VLM transcript against the search layer")
    p_hybrid.add_argument("--hyp", required=True)
    p_hybrid.add_argument("--layer", required=True)
    p_hybrid.add_argument("--df", required=True)
    p_hybrid.add_argument("--out", required=True)
    p_hybrid.add_argument("--min-df", type=int, default=5)
    p_hybrid.add_argument("--max-df", type=int, default=3)
    p_hybrid.add_argument("--max-edit", type=int, default=1)
    p_hybrid.add_argument("--min-len", type=int, default=1)
    p_hybrid.add_argument("--same-length", action="store_true")
    p_hybrid.add_argument("--require-df-one", action="store_true")
    p_hybrid.add_argument("--no-substring", action="store_true")
    p_hybrid.add_argument("--no-digit", action="store_true")
    p_hybrid.add_argument("--out-json")
    p_hybrid.set_defaults(func=cmd_hybrid)

    p_funnel = sub.add_parser("funnel", help="validate cross-engine agreement as a review-triage proxy")
    p_funnel.add_argument("--gold", required=True)
    p_funnel.add_argument("--hyp-a", required=True)
    p_funnel.add_argument("--hyp-b", required=True)
    p_funnel.add_argument("--threshold", type=float, default=0.99)
    p_funnel.add_argument("--max-true-cer", type=float, default=0.01)
    p_funnel.add_argument("--out-json")
    p_funnel.set_defaults(func=cmd_funnel)

    p_triage = sub.add_parser("triage", help="agreement buckets across two systems")
    p_triage.add_argument("--gold", required=True)
    p_triage.add_argument("--hyp-a", required=True)
    p_triage.add_argument("--hyp-b", required=True)
    p_triage.add_argument("--auto-threshold", type=float, default=0.01)
    p_triage.add_argument("--review-threshold", type=float, default=0.05)
    p_triage.set_defaults(func=cmd_triage)

    args = parser.parse_args(list(argv) if argv is not None else None)
    return int(args.func(args) or 0)


if __name__ == "__main__":
    raise SystemExit(main())
