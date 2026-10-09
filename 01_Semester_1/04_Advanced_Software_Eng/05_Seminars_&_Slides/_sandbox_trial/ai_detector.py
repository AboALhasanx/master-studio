#!/usr/bin/env python3
"""
Strong local AI-text detector v2 for the ASE Ch5 notes.
- Fast-DetectGPT conditional probability curvature (arXiv 2310.05130)
- Binoculars score PPL/X-PPL (arXiv 2401.12070)
- reference calibration against a KNOWN-HUMAN baseline (a source-textbook passage)
- per-sentence curvature to flag the most AI-like sentences (actionable)
- stylometric tells
CAUTION: an indicator for editing, not proof of authorship.
"""
import argparse
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer
import textstat
from lexicalrichness import LexicalRichness

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("doc", nargs="?", default=str(HERE / "Ch5_Software_Design.md"))
ap.add_argument("--observer", default="gpt2")
ap.add_argument("--performer", default="gpt2")
ap.add_argument("--baseline", default=str(HERE / "corpus" / "sommerville_ch6.txt"))
ARGS = ap.parse_args()
DOC = Path(ARGS.doc)
REPORT = HERE / "reports"; REPORT.mkdir(exist_ok=True)

LEXICON = ["delve", "tapestry", "intricate", "pivotal", "underscore", "showcase", "foster",
           "garner", "enduring", "vibrant", "nestled", "boasts", "seamless", "leverage",
           "robust", "holistic", "myriad", "realm", "landscape", "testament", "cornerstone",
           "meticulous", "multifaceted", "paramount"]
PHRASES = ["it is important to note", "it is worth noting", "it is crucial to", "in today's",
           "plays a crucial role", "a testament to", "in the realm of", "navigate the complexities",
           "unlock the potential", "at the end of the day", "when it comes to", "in conclusion",
           "serves as a", "highlighting the", "reflecting the", "contributing to"]


def load_prose(path):
    paras = []
    for raw in path.read_text(encoding="utf-8", errors="ignore").split("\n"):
        s = raw.strip()
        if (not s or s.startswith("#") or s.startswith("![") or s.startswith("*Figure")
                or s.startswith("|") or s.startswith(">") or s == "---"):
            continue
        if s.startswith("- "):
            s = s[2:]
        paras.append(s.replace("**", "").replace("*", ""))
    return "\n".join(paras)


def clean_corpus_text(path, max_chars=4000):
    t = Path(path).read_text(encoding="utf-8", errors="ignore")
    t = re.sub(r'\\n==.*?==\\n', ' ', t)
    t = re.sub(r'\*+ebook converter.*', ' ', t)
    t = re.sub(r'\s+', ' ', t)
    return t[:max_chars]


@torch.no_grad()
def curvature(text, tok, model, chunk=480, stride=240):
    ids = tok(text, return_tensors="pt").input_ids[0]
    if len(ids) < 8:
        return np.array([np.nan])
    dev = next(model.parameters()).device
    curvs = []
    for i in range(0, len(ids) - 4, stride):
        seg = ids[i:i + chunk].unsqueeze(0).to(dev)
        if seg.shape[1] < 6:
            break
        logits = model(seg).logits[0]
        logp = F.log_softmax(logits[:-1], dim=-1)
        p = logp.exp()
        targets = seg[0, 1:]
        a = logp.gather(1, targets.unsqueeze(1)).squeeze(1)
        mu = (p * logp).sum(-1)
        var = (p * logp.pow(2)).sum(-1) - mu.pow(2)
        curvs.append(((a - mu) / torch.sqrt(var.clamp_min(1e-6))).cpu())
        if i + chunk >= len(ids):
            break
    return torch.cat(curvs).numpy()


@torch.no_grad()
def binoculars(text, tok, observer, performer, max_len=1024, stride=512):
    ids = tok(text, return_tensors="pt").input_ids[0]
    if len(ids) < 8:
        return float("nan")
    do = next(observer.parameters()).device
    dp = next(performer.parameters()).device
    P, X = [], []
    for i in range(0, len(ids), stride):
        seg = ids[i:i + max_len].unsqueeze(0)
        if seg.shape[1] < 6:
            break
        lo = observer(seg.to(do)).logits[0]
        lp = performer(seg.to(dp)).logits[0]
        logp_o = F.log_softmax(lo[:-1], dim=-1)
        targets = seg[0, 1:]
        P.append(-logp_o.gather(1, targets.unsqueeze(1)).squeeze(1).mean().cpu())
        p_p = F.softmax(lp[:-1], dim=-1)
        X.append(-(p_p * logp_o).sum(-1).mean().cpu())
        if i + max_len >= len(ids):
            break
    ppl = float(torch.stack(P).mean()); xppl = float(torch.stack(X).mean())
    return ppl / xppl


@torch.no_grad()
def sentence_curvatures(sents, tok, model):
    out = []
    for s in sents:
        ids = tok(s, return_tensors="pt").input_ids[0]
        if len(ids) < 8:
            out.append(np.nan); continue
        logits = model(ids.unsqueeze(0).to(next(model.parameters()).device)).logits[0]
        logp = F.log_softmax(logits[:-1], dim=-1)
        p = logp.exp()
        a = logp.gather(1, ids[1:].unsqueeze(1)).squeeze(1)
        mu = (p * logp).sum(-1)
        var = (p * logp.pow(2)).sum(-1) - mu.pow(2)
        d = ((a - mu) / torch.sqrt(var.clamp_min(1e-6))).mean().item()
        out.append(d)
    return out


def main():
    text = load_prose(DOC)
    low = text.lower()
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if len(s.split()) >= 5]
    words = re.findall(r"[a-zA-Z']+", text); n = len(words)

    print(f"Loading observer={ARGS.observer}, performer={ARGS.performer} ...")
    tok = AutoTokenizer.from_pretrained(ARGS.observer)
    observer = AutoModelForCausalLM.from_pretrained(ARGS.observer).eval()
    performer = AutoModelForCausalLM.from_pretrained(ARGS.performer).eval()

    d_curv = curvature(text, tok, observer)
    d_mean, d_med = float(np.nanmean(d_curv)), float(np.nanmedian(d_curv))
    d_bino = binoculars(text, tok, observer, performer)

    baseline = clean_corpus_text(ARGS.baseline)
    b_curv = curvature(baseline, tok, observer)
    b_mean = float(np.nanmean(b_curv))
    b_bino = binoculars(baseline, tok, observer, performer)

    sc = sentence_curvatures(sents, tok, observer)
    order = sorted(range(len(sents)), key=lambda i: -(sc[i] if not np.isnan(sc[i]) else -9))
    top = [(sc[i], sents[i]) for i in order[:10]]

    lens = [len(s.split()) for s in sents]
    burst = float(np.std(lens) / max(1e-6, np.mean(lens)))
    sd = len(sents); sdv = float(np.std(sc) / max(1e-6, np.mean(sc)))
    em = text.count(chr(0x2014)) + text.count(chr(0x2013))
    triads = len(re.findall(r'\b\w+[^,.!?]*,\s+\w+[^,.!?]*,\s+and\s+\w+', text))
    fk = textstat.flesch_kincaid_grade(text)
    ttr = len(set(w.lower() for w in words)) / max(1, n)

    def verdict(c, b):
        if c > 2.0: return "AI-like"
        if c > 1.0: return "borderline"
        return "human-like"

    L = ["# AI-text detection report v2 (calibrated)\n"]
    L.append(f"- Document: `{DOC.name}` ({n} words, {sd} sentences)")
    L.append(f"- Models: observer `{ARGS.observer}`, performer `{ARGS.performer}`")
    L.append(f"- Human baseline: `{Path(ARGS.baseline).name}`")
    L.append("- CAUTION: an indicator for editing, not proof of authorship.\n")
    L.append("## Detectors (document vs known-human baseline)\n")
    L.append("| Metric | Document | Human baseline | Reference |")
    L.append("|:--|--:|--:|:--|")
    L.append(f"| Fast-DetectGPT curvature (mean) | **{d_mean:.2f}** | {b_mean:.2f} | machine~3, human~0 |")
    L.append(f"| Binoculars score | **{d_bino:.3f}** | {b_bino:.3f} | AI<0.85, human>0.9 |")
    L.append("")
    L.append(f"**Verdict (curvature): {verdict(d_mean, b_mean)}** : document curvature is "
             f"{'close to' if abs(d_mean-b_mean)<1 else 'different from'} the human baseline.\n")
    L.append("## Per-sentence curvature (most AI-like first)\n")
    for c, s in top:
        L.append(f"- {c:+.2f}  `{s[:120]}`")
    L.append("")
    L.append("## Stylometric signals\n")
    L.append(f"- Sentence-length burstiness: {burst:.2f} (higher = more human)")
    L.append(f"- Sentence-curvature burstiness: {sdv:.2f}")
    L.append(f"- Em-dashes: {em} | Rule-of-three triads: {triads}")
    L.append(f"- TTR {ttr:.3f} | Flesch-Kincaid {fk:.1f}")
    out = "\n".join(L)
    (REPORT / "ai_detection_report.md").write_text(out, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

