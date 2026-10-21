import re, sys
from pathlib import Path
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass
from rapidfuzz import fuzz, process

HERE = Path(__file__).resolve().parent
md = (HERE / "ch7_part1.md").read_text(encoding="utf-8")
src = (HERE / "SOURCE_ch7_slides.txt").read_text(encoding="utf-8")

def paras(t):
    out = []
    for p in re.split(r'\n\s*\n', t):
        p = p.strip()
        if not p or p.startswith("#") or p.startswith("![") or p.startswith("*Figure") or p.startswith("|"):
            continue
        p = re.sub(r'^\s*[-*]\s+', '', p, flags=re.M)
        p = re.sub(r'^\s*\d+\.\s+', '', p, flags=re.M)
        p = p.replace("**", "").replace("*", "")
        for s in re.split(r'(?<=[.!?])\s+', p):
            if len(s.split()) >= 5:
                out.append(s.strip())
    return out

ours = paras(md)
src_s = re.split(r'(?<=[.!?])\s+', src.replace("\n", " "))
src_s = [s.strip() for s in src_s if len(s.split()) >= 4]
print(f"our sentences: {len(ours)} | source sentences: {len(src_s)}")
bad = []
for s in ours:
    best, score, _ = process.extractOne(s, src_s, scorer=fuzz.token_set_ratio)
    if score < 80:
        bad.append((score, s, best))
print(f"flagged <80: {len(bad)}")
for score, s, best in sorted(bad)[:12]:
    print(f"  {score:.0f}  ours: {s[:90]}")
    print(f"       src : {str(best)[:90]}")
