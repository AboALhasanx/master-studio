#!/usr/bin/env python3
"""
Local plagiarism + style checker for the ASE Ch5 notes.
No network, no external corpus: compares the written document against the local
source corpus (the extracted textbook/slide texts) using:
  1) k-gram shingle overlap   (verbatim reuse)
  2) TF-IDF cosine similarity (document-level)
  3) sentence-level fuzzy match (near-verbatim / lightly-reworded reuse)
  4) style metrics            (burstiness, lexical richness, readability, AI-phrase hits)
Outputs a Markdown report. Epistemic note: similarity != plagiarism; it shows textual
overlap with THIS corpus only.
"""
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np
from rapidfuzz import fuzz, process
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import textstat
from lexicalrichness import LexicalRichness

HERE = Path(__file__).resolve().parent
DOC = HERE / "Ch5_Software_Design.md"
CORPUS = HERE / "corpus"
REPORT = HERE / "reports"
REPORT.mkdir(exist_ok=True)

STOP = set("a an the of in on to for and or is are was were be been being this that these those as at by with from it its their there here we our you your they them he she his her not no do does did done can could should would may might must will shall than then so such into over under more most other some any each both few many much own same own s t just also very".split())
AI_PHRASES = [
    "it is important to note", "it is worth noting", "in today's", "plays a crucial role",
    "a testament to", "in the realm of", "navigate the complexities", "unlock the potential",
    "delve into", "in conclusion", "not only", "when it comes to", "at the end of the day",
    "game-changer", "seamless", "leverage", "robust", "furthermore", "moreover", "tapestry",
    "stands as", "underscores", "showcasing", "vibrant", "pivotal",
]


def norm_words(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return [w for w in text.split() if w]


def load_doc_prose(path):
    """Extract body prose from the markdown, dropping headings/figures/tables."""
    out_paras, paras = [], []
    for raw in path.read_text(encoding="utf-8").split("\n"):
        s = raw.strip()
        if (not s or s.startswith("#") or s.startswith("![") or s.startswith("*Figure")
                or s.startswith("|") or s.startswith(">") or s == "---"):
            if paras:
                out_paras.append(" ".join(paras)); paras = []
            continue
        if s.startswith("- "):
            s = s[2:]
        s = s.replace("**", "").replace("*", "")
        paras.append(s)
    if paras:
        out_paras.append(" ".join(paras))
    return out_paras


def load_corpus(dirpath):
    docs = {}
    for f in sorted(dirpath.glob("*.txt")):
        docs[f.stem] = f.read_text(encoding="utf-8", errors="ignore")
    return docs


def shingles(words, k):
    return {tuple(words[i:i + k]) for i in range(len(words) - k + 1)}


def matched_phrases(doc_words, corpus_words, k):
    """Longest runs of the doc that appear verbatim in the corpus (via k-shingles)."""
    cset = shingles(corpus_words, k)
    flags = [tuple(doc_words[i:i + k]) in cset for i in range(len(doc_words) - k + 1)]
    spans, i, n = [], 0, len(flags)
    while i < n:
        if flags[i]:
            j = i
            while j + 1 < n and flags[j + 1]:
                j += 1
            start, end = i, j + k
            spans.append(" ".join(doc_words[start:end]))
            i = j + 1
        else:
            i += 1
    spans.sort(key=len, reverse=True)
    return spans


def main():
    prose_paras = load_doc_prose(DOC)
    doc_text = "\n".join(prose_paras)
    doc_words = norm_words(doc_text)
    doc_sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', doc_text) if len(s.split()) >= 6]

    corpus = load_corpus(CORPUS)
    corpus_all = "\n".join(corpus.values())
    corpus_words = norm_words(corpus_all)
    corpus_sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', corpus_all) if len(s.split()) >= 6]

    lines = []
    lines.append("# Local Plagiarism & Style Report\n")
    lines.append(f"- Document: `{DOC.name}` ({len(doc_words)} words, {len(doc_sents)} sentences)")
    lines.append(f"- Corpus: {len(corpus)} sources, {len(corpus_words)} words")
    lines.append("- Note: similarity != plagiarism; this shows overlap with THIS local corpus only.\n")

    # 1) k-gram shingle overlap
    lines.append("## 1. Verbatim overlap (k-gram shingles)\n")
    lines.append("| k | doc shingles | matched in corpus | overlap |")
    lines.append("|:--|--:|--:|--:|")
    for k in (6, 8, 10):
        ds = shingles(doc_words, k); cs = shingles(corpus_words, k)
        m = len(ds & cs)
        pct = (100.0 * m / len(ds)) if ds else 0.0
        lines.append(f"| {k} | {len(ds)} | {m} | {pct:.1f}% |")

    # longest matched phrases (k=8)
    spans = matched_phrases(doc_words, corpus_words, 8)
    lines.append(f"\n**Longest verbatim-matched phrases (>= 8 words): {len(spans)} found**\n")
    if spans:
        for ph in spans[:15]:
            lines.append(f"- ({len(ph.split())} words) `{ph[:160]}`")
    else:
        lines.append("- none")
    lines.append("")

    # 2) TF-IDF cosine per source
    lines.append("## 2. TF-IDF cosine similarity (document vs each source)\n")
    keys = list(corpus)
    vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=1)
    X = vec.fit_transform([doc_text] + [corpus[k] for k in keys])
    sims = cosine_similarity(X[0:1], X[1:]).ravel()
    lines.append("| Source | Cosine |")
    lines.append("|:--|--:|")
    for k, s in sorted(zip(keys, sims), key=lambda t: -t[1]):
        lines.append(f"| {k} | {s:.3f} |")
    lines.append("")

    # 3) sentence-level fuzzy match
    lines.append("## 3. Sentence-level near-match (rapidfuzz, best match >= 80)\n")
    flagged = 0
    rows = []
    for sent in doc_sents:
        best, score, _ = process.extractOne(sent, corpus_sents, scorer=fuzz.token_set_ratio)
        if score >= 80:
            flagged += 1
            rows.append((score, sent, best))
    rows.sort(key=lambda r: -r[0])
    lines.append(f"Sentences with a >=80 token-set match: **{flagged} / {len(doc_sents)}**\n")
    for score, sent, best in rows[:15]:
        lines.append(f"- **{score:.0f}**  doc: `{sent[:110]}`")
        lines.append(f"   — closest source: `{best[:110]}`")
    lines.append("")

    # 4) style metrics
    lines.append("## 4. Style metrics\n")
    lens = [len(s.split()) for s in doc_sents]
    mean = float(np.mean(lens)); std = float(np.std(lens))
    ttr = len(set(norm_words(doc_text))) / max(1, len(norm_words(doc_text)))
    try:
        mldt = LexicalRichness(doc_text).msttr(segment_window=25)
    except Exception:
        mldt = float("nan")
    fk = textstat.flesch_kincaid_grade(doc_text)
    fre = textstat.flesch_reading_ease(doc_text)
    ai_hits = []
    low = doc_text.lower()
    for p in AI_PHRASES:
        c = low.count(p)
        if c:
            ai_hits.append((p, c))
    lines.append(f"- Sentence length: mean {mean:.1f}, std {std:.1f}, **burstiness (std/mean) {std/mean:.2f}**")
    lines.append(f"- Type-Token Ratio: {ttr:.3f}")
    lines.append(f"- MTLD/MSTTR: {mldt:.3f}")
    lines.append(f"- Flesch-Kincaid grade: {fk:.1f} | Flesch reading ease: {fre:.1f}")
    lines.append(f"- AI/slop phrase hits: {sum(c for _, c in ai_hits)}  " + (", ".join(f"`{p}`×{c}" for p, c in ai_hits) if ai_hits else "(none)"))
    lines.append("")

    out = "\n".join(lines)
    (REPORT / "plagiarism_report.md").write_text(out, encoding="utf-8")
    print(out)
    print(f"\nSaved: reports/plagiarism_report.md")


if __name__ == "__main__":
    main()
