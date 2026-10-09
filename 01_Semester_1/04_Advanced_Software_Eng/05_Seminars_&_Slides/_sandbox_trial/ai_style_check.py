#!/usr/bin/env python3
"""
Local AI-generated ("AI-ness" / slop) detector for the ASE Ch5 notes.
IMPORTANT: no output-only detector is a reliable proof of authorship. This tool gives an
*indicator* built from the signals the literature uses, and is meant to guide editing, not to accuse.

Signals:
  A. Perplexity (distilgpt2)         - low = predictable = more AI-like
  B. Perplexity burstiness           - low variation across sentences = more AI-like
  C. Sentence-length burstiness      - low = more AI-like
  D. AI/slop lexicon & phrase density
  E. Structural tells (em-dash, "not only X but Y", rule-of-three, transitions, hedges)
  F. Repetition (sentence openers, distinct-n)
  G. Readability & lexical diversity (context)
Aggregates A-F into a 0-100 "AI-likeness" score.
"""
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np
import torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import textstat
from lexicalrichness import LexicalRichness

HERE = Path(__file__).resolve().parent
DOC = HERE / "Ch5_Software_Design.md"
REPORT = HERE / "reports"
REPORT.mkdir(exist_ok=True)

LEXICON = ["delve", "tapestry", "intricate", "pivotal", "underscore", "underscores", "showcase",
           "showcasing", "foster", "fostering", "garner", "enduring", "vibrant", "nestled",
           "boasts", "seamless", "leverage", "robust", "holistic", "myriad", "realm",
           "landscape", "testament", "cornerstone", "meticulous", "multifaceted", "paramount"]
PHRASES = ["it is important to note", "it is worth noting", "it is crucial to", "in today's",
           "plays a crucial role", "plays a vital role", "a testament to", "in the realm of",
           "navigate the complexities", "unlock the potential", "at the end of the day",
           "when it comes to", "in conclusion", "not only", "but also", "stands as",
           "serves as a", "serves as", "highlighting the", "reflecting the", "contributing to",
           "in an era of", "the world of", "game-changer", "ever-evolving"]
TRANSITIONS = ["moreover", "furthermore", "additionally", "consequently", "therefore",
               "however", "nevertheless", "nonetheless", "in addition", "as a result"]
HEDGES = ["may", "might", "could", "can be", "often", "typically", "generally", "usually",
          "in general", "it seems", "arguably", "relatively"]


def load_doc_prose(path):
    paras = []
    for raw in path.read_text(encoding="utf-8").split("\n"):
        s = raw.strip()
        if (not s or s.startswith("#") or s.startswith("![") or s.startswith("*Figure")
                or s.startswith("|") or s.startswith(">") or s == "---"):
            continue
        if s.startswith("- "):
            s = s[2:]
        paras.append(s.replace("**", "").replace("*", ""))
    return "\n".join(paras)


def perplexities(text, tokenizer, model, chunk=400, stride=200):
    ids = tokenizer(text, return_tensors="pt").input_ids[0]
    nlls, total, counted = [], 0.0, 0
    for i in range(0, len(ids), stride):
        seg = ids[i:i + chunk]
        if len(seg) < 8:
            break
        with torch.no_grad():
            out = model(seg.unsqueeze(0), labels=seg.unsqueeze(0))
        loss = float(out.loss)
        nlls.append(loss)
        total += loss * len(seg); counted += len(seg)
        if i + chunk >= len(ids):
            break
    mean_loss = total / max(1, counted)
    return float(np.exp(mean_loss)), nlls


def per_sentence_ppl(sents, tokenizer, model):
    ppls = []
    for s in sents:
        ids = tokenizer(s, return_tensors="pt").input_ids[0]
        if len(ids) < 8:
            continue
        with torch.no_grad():
            out = model(ids.unsqueeze(0), labels=ids.unsqueeze(0))
        ppls.append(float(np.exp(float(out.loss))))
    return ppls


def main():
    text = load_doc_prose(DOC)
    low = text.lower()
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if len(s.split()) >= 4]
    words = re.findall(r"[a-zA-Z']+", text)
    n = len(words)

    print("Loading distilgpt2 ...")
    tok = GPT2TokenizerFast.from_pretrained("distilgpt2")
    model = GPT2LMHeadModel.from_pretrained("distilgpt2")
    model.eval()

    ppl, nlls = perplexities(text, tok, model)
    sent_ppl = per_sentence_ppl(sents, tok, model)
    ppl_burst = float(np.std(sent_ppl) / max(1e-6, np.mean(sent_ppl))) if sent_ppl else 0.0

    lens = [len(s.split()) for s in sents]
    len_burst = float(np.std(lens) / max(1e-6, np.mean(lens)))

    lex_hits = {w: low.count(w) for w in LEXICON if low.count(w)}
    ph_hits = {p: low.count(p) for p in PHRASES if low.count(p)}
    tr_hits = {t: low.count(t) for t in TRANSITIONS if low.count(t)}
    hd_hits = {h: low.count(h) for h in HEDGES if low.count(h)}
    lex_per_100 = 100.0 * sum(lex_hits.values()) / max(1, n)
    ph_per_100 = 100.0 * sum(ph_hits.values()) / max(1, n)
    tr_per_100 = 100.0 * sum(tr_hits.values()) / max(1, n)
    emdash = text.count("—") + text.count("–")
    emdash_per_100 = 100.0 * emdash / max(1, n)
    # rule-of-three: sentences with three comma-separated items in a row
    triads = len(re.findall(r'\b\w+[^,.!?]*,\s+\w+[^,.!?]*,\s+and\s+\w+', text))
    openers = [ " ".join(s.split()[:2]).lower() for s in sents ]
    rep_open = sum(1 for o in set(openers) if openers.count(o) > 2)

    ttr = len(set(w.lower() for w in words)) / max(1, n)
    try:
        msttr = LexicalRichness(text).msttr(segment_window=25)
    except Exception:
        msttr = float("nan")
    fk = textstat.flesch_kincaid_grade(text)
    fre = textstat.flesch_reading_ease(text)

    # ---- scoring (heuristic, transparent; thresholds from the AI-writing literature) ----
    def band(v, lo_ai, hi_ai, invert=False):
        """map value to 0..1 where 1 = more AI-like."""
        if invert:
            v = -v
            lo_ai, hi_ai = -lo_ai, -hi_ai
        return float(np.clip((v - lo_ai) / (hi_ai - lo_ai), 0, 1))

    s_ppl = band(ppl, 60, 18, invert=False)          # very low ppl => AI-like (ppl<18 =>1)
    s_pplb = band(ppl_burst, 1.2, 0.5, invert=False) # low burst => AI-like
    s_lenb = band(len_burst, 0.55, 0.30, invert=False)
    s_lex = band(lex_per_100, 0.0, 1.5)
    s_ph = band(ph_per_100, 0.0, 2.5)
    s_tr = band(tr_per_100, 0.0, 2.0)
    s_em = band(emdash_per_100, 0.0, 1.5)
    s_tri = band(triads, 0, 6)
    s_open = band(rep_open, 0, 5)
    weights = {"ppl": 0.28, "pplburst": 0.10, "lenburst": 0.10, "lex": 0.12, "ph": 0.14,
               "transitions": 0.08, "emdash": 0.06, "triads": 0.06, "openers": 0.06}
    score = 100 * (
        weights["ppl"] * s_ppl + weights["pplburst"] * s_pplb + weights["lenburst"] * s_lenb +
        weights["lex"] * s_lex + weights["ph"] * s_ph + weights["transitions"] * s_tr +
        weights["emdash"] * s_em + weights["triads"] * s_tri + weights["openers"] * s_open)
    verdict = ("LOW (reads human)" if score < 30 else
               "MODERATE (some AI-ish signals)" if score < 55 else
               "HIGH (reads AI-generated)")

    L = []
    L.append("# AI-likeness / slop report\n")
    L.append(f"- Document: `{DOC.name}` ({n} words, {len(sents)} sentences)")
    L.append("- Engine: distilgpt2 perplexity + burstiness + stylometric tells")
    L.append("- CAUTION: an indicator for editing, not proof of authorship.\n")
    L.append(f"## AI-likeness score: **{score:.0f} / 100** — {verdict}\n")
    L.append("| Signal | Value | AI-like? | Weight |")
    L.append("|:--|--:|:--:|--:|")
    L.append(f"| Perplexity (distilgpt2) | {ppl:.1f} | lower = AI | 0.28 |")
    L.append(f"| Perplexity burstiness | {ppl_burst:.2f} | lower = AI | 0.10 |")
    L.append(f"| Sentence-length burstiness | {len_burst:.2f} | lower = AI | 0.10 |")
    L.append(f"| Slop-lexicon /100w | {lex_per_100:.2f} | higher = AI | 0.12 |")
    L.append(f"| Slop-phrases /100w | {ph_per_100:.2f} | higher = AI | 0.14 |")
    L.append(f"| Transitions /100w | {tr_per_100:.2f} | higher = AI | 0.08 |")
    L.append(f"| Em-dashes /100w | {emdash_per_100:.2f} | higher = AI | 0.06 |")
    L.append(f"| Rule-of-three triads | {triads} | higher = AI | 0.06 |")
    L.append(f"| Repeated sentence openers | {rep_open} | higher = AI | 0.06 |")
    L.append("")
    L.append("## Context metrics")
    L.append(f"- TTR {ttr:.3f} | MSTTR {msttr:.3f} | Flesch-Kincaid {fk:.1f} | reading ease {fre:.1f}")
    L.append(f"- Slop lexicon hits: {lex_hits if lex_hits else 'none'}")
    L.append(f"- Slop phrase hits: {ph_hits if ph_hits else 'none'}")
    L.append(f"- Transition hits: {tr_hits if tr_hits else 'none'}")
    L.append("")
    out = "\n".join(L)
    (REPORT / "ai_likeness_report.md").write_text(out, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
