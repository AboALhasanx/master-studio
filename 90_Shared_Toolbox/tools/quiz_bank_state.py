#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Single source of truth for MCSQuiz bank state.

Problem this solves
-------------------
Bank counts, content versions and shell versions used to be hand-copied into
ACTIVE_STATE.md, AGENT_HANDOFF_QUIZ_BANKS.md and QUIZ_PUBLISH_RUNBOOK.md. A
table keyed only by "ChNN" (no subject column) then received rows from two
different subjects, so Cyber Ch02/Ch03 displayed Data Mining's 69/7 and 55/7
while the live portal served 92/8 and 103/9. Four documents claimed to be
current and none of them was.

Fix: this script MEASURES the vault, the live manifest and the portal shell,
then writes 00_STUDIO_HUB/QUIZ_BANK_STATE.md. Every other document points at
that file; none of them carries a live number. Run --check before publishing:
it exits 1 if the committed snapshot no longer matches reality.

Usage (from anywhere):
    python -X utf8 90_Shared_Toolbox/tools/quiz_bank_state.py          # regenerate
    python -X utf8 90_Shared_Toolbox/tools/quiz_bank_state.py --check  # drift gate

No network is required for --check to be useful: if Supabase is unreachable it
falls back to the portal's local mirror and labels the column accordingly.
"""
import argparse
import datetime
import glob
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", ".."))
PORTAL = r"C:\Users\gokoq\mcq-portal"
BANKS_GLOB = os.path.join(VAULT, "01_Semester_1", "*", "07_Quizzes_&_Anki", "*.json")
OUT = os.path.join(VAULT, "00_STUDIO_HUB", "QUIZ_BANK_STATE.md")
MIRROR = os.path.join(PORTAL, "data", "index.json")
CONFIG = os.path.join(PORTAL, "js", "supabase-config.js")

# Caps from the five authoring laws (AGENT_HANDOFF_QUIZ_BANKS.md §2).
RANK_CAP = 0.30          # correct option may be unique-longest/shortest in <=30%
SPREAD_EN = 1.40
SPREAD_AR = 1.30

# Canonical pattern lives in the tracked toolchain, NOT in scratch/ (gitignored
# since 23cfa7f). A fresh checkout must be able to run this tool standalone.
sys.path.insert(0, HERE)
from quiz_meta_pattern import META, self_test  # noqa: E402

self_test()   # never trust an untested validator — this one broke twice before


def _chapter_of(d, path):
    qid = d.get("quiz_id") or ""
    m = re.search(r"Ch(\d+)_", qid) or re.search(r"Ch(\d+)_", os.path.basename(path))
    if m:
        return int(m.group(1))
    m = re.match(r"Quiz_(\d+)_", os.path.basename(path))
    return int(m.group(1)) if m else 0


def read_vault():
    """Every active bank, any filename, any subject. _retired/ is a sibling."""
    rows = {}
    for path in sorted(glob.glob(BANKS_GLOB)):
        try:
            d = json.loads(open(path, encoding="utf-8").read())
        except (ValueError, OSError):
            continue
        if "questions" not in d:
            continue
        subj = os.path.basename(os.path.dirname(os.path.dirname(path)))
        ch = _chapter_of(d, path)
        key = (subj, ch)
        slot = rows.setdefault(key, {"banks": 0, "q": 0, "refs": 0,
                                    "long_en": 0, "short_en": 0,
                                    "long_ar": 0, "short_ar": 0,
                                    "formula": 0, "spread": 0})
        slot["banks"] += 1
        for q in d["questions"]:
            slot["q"] += 1
            blob = [q.get("question"), q.get("question_ar"),
                    q.get("explanation"), q.get("explanation_ar")]
            blob += (q.get("options") or []) + (q.get("options_ar") or [])
            if any(t and META.search(str(t)) for t in blob):
                slot["refs"] += 1
            for o in (q.get("options") or []) + (q.get("options_ar") or []):
                if "$" in str(o) or "\\" in str(o):
                    slot["formula"] += 1
            ai = "ABCD".index(q["answer"])
            for field, cap, lp, sp in (("options", SPREAD_EN, "long_en", "short_en"),
                                       ("options_ar", SPREAD_AR, "long_ar", "short_ar")):
                o = q.get(field) or []
                if len(o) != 4:
                    continue
                L = [len(str(x)) for x in o]
                c = L[ai]
                if c == max(L) and L.count(c) == 1:
                    slot[lp] += 1
                elif c == min(L) and L.count(c) == 1:
                    slot[sp] += 1
                if min(L) and max(L) / min(L) > cap:
                    slot["spread"] += 1
    return rows


def read_live():
    """Return (rows, version, source_label). Tries Supabase, then the mirror."""
    try:
        lines = open(CONFIG, encoding="utf-8").read().splitlines()
        url = [l.split("'")[1] for l in lines if l.strip().startswith("url:")][0]
        key = [l.split("'")[1] for l in lines if l.strip().startswith("key:")][0]
        req = urllib.request.Request(
            url + "/rest/v1/rpc/content_manifest", data=b"{}",
            headers={"apikey": key, "Authorization": "Bearer " + key,
                     "Content-Type": "application/json"})
        m = json.load(urllib.request.urlopen(req, timeout=25))
        rows = {}
        for s in m.get("subjects", []):
            for c in s.get("chapters", []):
                k = (s["subject_id"], int(c.get("chapter_no") or 0))
                slot = rows.setdefault(k, {"banks": 0, "q": 0})
                slot["banks"] += 1
                slot["q"] += int(c.get("count") or 0)
        return rows, m.get("version"), "Supabase content_manifest (live)"
    except Exception as exc:                                  # noqa: BLE001
        label = "local mirror (Supabase unreachable: %s)" % type(exc).__name__
    try:
        m = json.loads(open(MIRROR, encoding="utf-8").read())
        rows = {}
        for s in m.get("subjects", []):
            for c in s.get("chapters", []):
                k = (s["subject_id"], int(c.get("chapter_no") or 0))
                slot = rows.setdefault(k, {"banks": 0, "q": 0})
                slot["banks"] += 1
                slot["q"] += int(c.get("count") or 0)
        return rows, m.get("version"), label
    except Exception:                                         # noqa: BLE001
        return {}, None, "UNAVAILABLE"


def shell_version():
    try:
        return open(os.path.join(PORTAL, "VERSION"), encoding="utf-8").read().strip()
    except OSError:
        return "?"


def render(vault, live, content_v, live_label, stamp=True):
    L = []
    A = L.append
    A("# MCSQuiz — Bank State")
    A("")
    A("> **AUTO-GENERATED — DO NOT EDIT BY HAND.**")
    A("> Source: `90_Shared_Toolbox/tools/quiz_bank_state.py`.")
    A("> Regenerate: `python -X utf8 90_Shared_Toolbox/tools/quiz_bank_state.py`")
    A("> Drift gate: `python -X utf8 90_Shared_Toolbox/tools/quiz_bank_state.py --check`")
    A(">")
    A("> This is the **only** place live bank numbers, chapter counts and versions are")
    A("> recorded. `ACTIVE_STATE.md`, `AGENT_HANDOFF_QUIZ_BANKS.md` and")
    A("> `QUIZ_PUBLISH_RUNBOOK.md` must point here, never copy numbers out of it.")
    A("> A table keyed only by `ChNN` is forbidden — every row carries its subject id.")
    A("")
    if stamp:
        A("> Generated at: %s" % datetime.datetime.now().astimezone().isoformat(timespec="seconds"))
        A("")
    A("## Current versions")
    A("")
    A("| Thing | Value |")
    A("|---|---|")
    A("| Live content version | **%s** |" % (content_v if content_v is not None else "unavailable"))
    A("| Portal shell `VERSION` | **%s** |" % shell_version())
    A("| Live manifest source | %s |" % live_label)
    A("")
    A("> No git hash is recorded here on purpose: a commit would change it and make")
    A("> `--check` report a false drift. Hashes belong in commit messages and session")
    A("> logs, and must never be cited before they are on `origin/master`.")
    A("")
    tv_b = sum(v["banks"] for v in vault.values())
    tv_q = sum(v["q"] for v in vault.values())
    tl_b = sum(v["banks"] for v in live.values())
    tl_q = sum(v["q"] for v in live.values())
    A("**Totals:** vault %d banks / %d questions · live %d banks / %d questions · %s" % (
        tv_b, tv_q, tl_b, tl_q,
        "MATCH" if (tv_b, tv_q) == (tl_b, tl_q) else "**MISMATCH — investigate before publishing**"))
    A("")
    A("## By subject (vault = live)")
    A("")
    A("| Subject | Chapters | Banks | Questions | Live banks | Live questions | Drift |")
    A("|---|---:|---:|---:|---:|---:|---|")
    subjects = sorted({k[0] for k in set(vault) | set(live)})
    for s in subjects:
        vs = [vault[k] for k in vault if k[0] == s]
        ls = [live[k] for k in live if k[0] == s]
        vb, vq = sum(x["banks"] for x in vs), sum(x["q"] for x in vs)
        lb, lq = sum(x["banks"] for x in ls), sum(x["q"] for x in ls)
        A("| `%s` | %d | %d | %d | %d | %d | %s |" % (
            s, len({k[1] for k in set(vault) | set(live) if k[0] == s}),
            vb, vq, lb, lq, "—" if (vb, vq) == (lb, lq) else "**DIFF**"))
    A("")
    A("## By subject and chapter — measured quality gates")
    A("")
    A("`refs` = questions naming the handout (must be 0). `long/short` = correct option is the")
    A("unique longest / shortest, EN then AR (cap %.0f%% each). `fx` = options containing a" % (RANK_CAP * 100))
    A("formula or backslash (must be 0). `spr` = option-length spread violations")
    A("(EN > %.2f, AR > %.2f). `local audit` is a measured snapshot, **not** a substitute for" % (SPREAD_EN, SPREAD_AR))
    A("`preflight.py N --strict` and `quiz_quality_gate.py --shape-gate`.")
    A("")
    A("| Subject | Ch | Banks | Q | refs | long EN/AR | short EN/AR | fx | spr | local audit |")
    A("|---|---:|---:|---:|---:|---|---|---:|---:|---|")
    for (s, ch), v in sorted(vault.items()):
        n = max(v["q"], 1)
        bad = (v["refs"] > 0 or v["formula"] > 0 or v["spread"] > 0
               or max(v["long_en"], v["long_ar"], v["short_en"], v["short_ar"]) / n > RANK_CAP)
        A("| `%s` | %02d | %d | %d | %d | %d/%d | %d/%d | %d | %d | %s |" % (
            s, ch, v["banks"], v["q"], v["refs"],
            v["long_en"], v["long_ar"], v["short_en"], v["short_ar"],
            v["formula"], v["spread"], "needs work" if bad else "clean"))
    A("")
    A("## What remains")
    A("")
    todo = []
    for (s, ch), v in sorted(vault.items()):
        n = max(v["q"], 1)
        issues = []
        if v["refs"]:
            issues.append("%d handout refs" % v["refs"])
        if v["formula"]:
            issues.append("%d formula options" % v["formula"])
        if v["spread"]:
            issues.append("%d spread violations" % v["spread"])
        if max(v["long_en"], v["long_ar"]) / n > RANK_CAP:
            issues.append("answer-length tell")
        if issues:
            todo.append("- `%s` Ch%02d — %s" % (s, ch, "; ".join(issues)))
    A("\n".join(todo) if todo else "Nothing: every chapter passes the measured gates.")
    A("")
    A("**Not measured here (deliberate):** whether a chapter's source is annotated,")
    A("whether crossed-out material was excluded, and whether answers are factually")
    A("correct. Those need `W0N_Annotation_Map.md` and source review, not a counter.")
    A("")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the committed snapshot is stale (never writes)")
    args = ap.parse_args()
    vault = read_vault()
    live, content_v, label = read_live()
    text = render(vault, live, content_v, label)
    if args.check:
        if not os.path.exists(OUT):
            print("FAIL  %s does not exist — run without --check" % OUT)
            return 1
        old = open(OUT, encoding="utf-8").read()
        strip = lambda t: "\n".join(          # noqa: E731
            l for l in t.splitlines() if not l.startswith("> Generated at:"))
        if strip(old) == strip(text):
            print("PASS  quiz bank state is current (%d banks / %d questions)" % (
                sum(v["banks"] for v in vault.values()), sum(v["q"] for v in vault.values())))
            return 0
        print("FAIL  quiz bank state is STALE. Regenerate with:")
        print("      python -X utf8 90_Shared_Toolbox/tools/quiz_bank_state.py")
        import difflib
        for line in list(difflib.unified_diff(
                strip(old).splitlines(), strip(text).splitlines(),
                fromfile="committed", tofile="measured", lineterm=""))[:30]:
            print("   " + line)
        return 1
    open(OUT, "w", encoding="utf-8", newline="\n").write(text)
    print("wrote %s" % OUT)
    print("vault %d banks / %d questions | live content v%s | shell %s" % (
        sum(v["banks"] for v in vault.values()),
        sum(v["q"] for v in vault.values()), content_v, shell_version()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
