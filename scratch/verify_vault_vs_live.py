#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compare every live bank's Arabic options with the vault master.

The merge rule in publish_quizzes used to treat "no Arabic letters" as
"untranslated" and inject the portal's older string. That could silently
corrupt any option that is identical in both languages (numbers, acronyms,
standard names). This script proves, bank by bank, that what the portal
serves now matches the vault.
"""
import json
import re
import urllib.request
from pathlib import Path

VAULT = Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1")
src = open(r"C:\Users\gokoq\mcq-portal\js\supabase-config.js", encoding="utf-8").read()
url = re.search(r"url:\s*'([^']+)'", src).group(1)
key = re.search(r"key:\s*'([^']+)'", src).group(1)


def rpc(n, b):
    r = urllib.request.Request(url + "/rest/v1/rpc/" + n, data=json.dumps(b).encode(),
                               headers={"apikey": key, "Authorization": "Bearer " + key,
                                        "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=90))


banks = sorted(VAULT.glob("*/07_Quizzes_&_Anki/Quiz_*.json"))
checked = mismatched = missing = 0
bad = []
for f in banks:
    d = json.loads(f.read_text(encoding="utf-8"))
    quiz_id = d.get("quiz_id")
    if not quiz_id:
        continue
    try:
        live = rpc("content_bank", {"p_quiz_id": quiz_id})
    except Exception:
        missing += 1
        continue
    lq = live.get("questions") or []
    vq = d.get("questions") or []
    if len(lq) != len(vq):
        bad.append((quiz_id, "count %d live vs %d vault" % (len(lq), len(vq))))
        mismatched += 1
        continue
    checked += 1
    byid = {q.get("id"): q for q in lq}
    for q in vq:
        L = byid.get(q.get("id"))
        if not L:
            bad.append((quiz_id, "missing " + str(q.get("id"))))
            mismatched += 1
            continue
        vo = [str(x).strip() for x in (q.get("options_ar") or [])]
        lo = [str(o.get("ar") or "").strip() for o in L.get("options") or []]
        # the live bank is rotated, so compare as multisets
        if sorted(vo) != sorted(lo):
            mismatched += 1
            bad.append((quiz_id, "options_ar differ at " + str(q.get("id"))))

print("banks compared:", checked, " banks with a problem:", mismatched, " not found live:", missing)
for b in bad[:15]:
    print("   -", b[0], "|", b[1])
