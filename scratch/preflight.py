#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Preflight: run every gate that must be green before a chapter is published.

Usage:
    python preflight.py 4          # chapter 4
    python preflight.py 3 --strict # also fail on any handout reference

Exit 0 = every gate passed, safe to run `portal_content.py sync`.
Exit 1 = at least one gate failed; the summary says which.

It deliberately does NOT publish anything. Publishing is a separate, explicit step.
"""
import glob
import json
import os
import re
import subprocess
import sys

VAULT = r"C:\Users\gokoq\Master-Studio"
BANKS = os.path.join(VAULT, r"01_Semester_1\01_Cyber_Security\07_Quizzes_&_Anki")
TOOLS = os.path.join(VAULT, r"90_Shared_Toolbox\tools")
PY = [sys.executable, "-X", "utf8"]

ch = sys.argv[1]
strict = "--strict" in sys.argv
pattern = os.path.join(BANKS, "Quiz_Ch%02d_*.json" % int(ch))
files = sorted(glob.glob(pattern))
if not files:
    print("no banks matched", pattern)
    sys.exit(1)

print("=" * 66)
print("PREFLIGHT  chapter %s  —  %d bank(s)" % (ch, len(files)))
print("=" * 66)

results = []


def gate(name, ok, detail=""):
    results.append((name, ok, detail))
    print("%-28s %s%s" % (name, "PASS" if ok else "FAIL", ("  " + detail) if detail else ""))


# ---- 1. handout references ------------------------------------------------
sys.path.insert(0, os.path.join(VAULT, "scratch"))
import importlib.util
spec = importlib.util.spec_from_file_location("fm", os.path.join(VAULT, "scratch", "find_meta.py"))
# find_meta.py is a script, so re-implement the scan here to keep this file standalone
META = re.compile(
    r"\bthe lecture|\blecture notes|\bthe notes\b|\bthe booklet\b|\bthe handout\b|"
    r"\bthe file\b|\baccording to\b|\bthe doctor\b|\bthe syllabus\b|\bthe slides?\b|"
    r"\bthe material\b|\bthe source\b|\bthe text\b|\bthe book\b|\bthe course\b|"
    r"\bthe module\b|\bthe curriculum\b|\bthe reading\b|"
    r"\bthis chapter|\bthe chapter|\bthis section|\bthis week|\bas we saw|"
    r"\bas covered|\bas discussed|\bas presented|\bher own\b|\bher rule\b|"
    r"\bshe said\b|\bshe states\b|\bher vocabulary\b|\bin her\b|"
    r"المحاضرة|المحاضرات|الملزمة|الملزمه|الدكتورة|الشرائح|المصدر|الجابتر|المذكور|"
    r"قاعدتها|قالت إن|قالت ال|هذا الفصل|هذا القسم|هذا الأسبوع", re.I)

refs = 0
for f in files:
    d = json.loads(open(f, encoding="utf-8").read())
    for q in d.get("questions", []):
        blob = [q.get("question"), q.get("question_ar"),
                q.get("explanation"), q.get("explanation_ar")]
        blob += (q.get("options") or []) + (q.get("options_ar") or [])
        if any(t and META.search(t) for t in blob):
            refs += 1
gate("handout references", refs == 0, "%d question(s)" % refs)

# ---- 2. option-length tells ----------------------------------------------
longest = shortest = total = 0
spread_bad = []
for f in files:
    d = json.loads(open(f, encoding="utf-8").read())
    for q in d.get("questions", []):
        ai = "ABCD".index(q["answer"])
        for field, cap, tag in (("options", 1.40, "EN"), ("options_ar", 1.30, "AR")):
            L = [len(x) for x in q[field]]
            if max(L) / min(L) > cap:
                spread_bad.append("%s %s %s" % (tag, q["id"], L))
        L = [len(x) for x in q["options"]]
        c = L[ai]
        total += 1
        if c == max(L) and L.count(c) == 1:
            longest += 1
        elif c == min(L) and L.count(c) == 1:
            shortest += 1
gate("EN unique-longest", longest <= 0.30 * total, "%d/%d" % (longest, total))
gate("EN unique-shortest", shortest <= 0.30 * total, "%d/%d" % (shortest, total))
gate("option spread", not spread_bad, "; ".join(spread_bad[:3]))

# ---- 2b. supplementary structural + bilingual quality gate ----------------
quality_cmd = PY + [
    os.path.join(TOOLS, "quiz_quality_gate.py"), BANKS,
    "--chapter", str(int(ch)), "--shape-gate", "--max-warnings", "0",
]
quality = subprocess.run(quality_cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
quality_lines = [line for line in quality.stdout.splitlines() if line.startswith(("Structural errors:", "Shape-gate failures:", "SHAPE:", "RESULT:"))]
gate("deep quality gate", quality.returncode == 0, "; ".join(quality_lines[:5]))

# ---- 3. the vault balancer ------------------------------------------------
bal_fail = []
for f in files:
    env = dict(os.environ, CODEBUDDY_SAFE_DELETE_ENABLED="0")
    r = subprocess.run(PY + [os.path.join(TOOLS, "quiz_balancer.py"), f, "--check", "--strict"],
                       capture_output=True, text=True, env=env)
    if r.returncode != 0:
        bal_fail.append(os.path.basename(f))
gate("quiz_balancer --strict", not bal_fail, ", ".join(bal_fail))

# ---- 4. schema v2 + v3 ----------------------------------------------------
sys.path.insert(0, TOOLS)
import publish_quizzes as pq
schema = pq.load_portal_schema(pq.DEFAULT_PORTAL)
schema_bad = []
for f in files:
    b = json.loads(open(f, encoding="utf-8").read())
    p = pq.validate_bank(schema, b, f)
    if p:
        schema_bad.append("%s: %s" % (b["quiz_id"], p[0]))
gate("validate_bank v2+v3", not schema_bad, "; ".join(schema_bad[:2]))

# ---- 5. canonical dry run -------------------------------------------------
env = dict(os.environ, CODEBUDDY_SAFE_DELETE_ENABLED="0")
r = subprocess.run(PY + [os.path.join(TOOLS, "publish_quizzes.py"), "--dry-run"],
                   capture_output=True, text=True, env=env)
gate("publish_quizzes --dry-run", r.returncode == 0, "exit %d" % r.returncode)

# ---- summary --------------------------------------------------------------
failed = [n for n, ok, _ in results if not ok]
print("-" * 66)
if failed:
    print("NOT READY — failed: " + ", ".join(failed))
    print("Do not run `portal_content.py sync` until these are green.")
    sys.exit(1)
print("ALL GATES PASSED — safe to publish (sync -> pull -> live audit -> release -> deploy).")
print("Publishing is still your decision; this script never writes to the portal.")
sys.exit(0)
