#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit the LIVE v3 payloads of Chapter 1 as Supabase serves them."""
import json
import re
import urllib.request

src = open(r"C:\Users\gokoq\mcq-portal\js\supabase-config.js", encoding="utf-8").read()
url = re.search(r"url:\s*'([^']+)'", src).group(1)
key = re.search(r"key:\s*'([^']+)'", src).group(1)


def rpc(name, body):
    req = urllib.request.Request(
        url + "/rest/v1/rpc/" + name, data=json.dumps(body).encode(),
        headers={"apikey": key, "Authorization": "Bearer " + key,
                 "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=60))


m = rpc("content_manifest", {})
ch1 = sorted([c for s in m["subjects"] if s["subject_id"] == "01_Cyber_Security"
              for c in s["chapters"] if c.get("chapter_no") == 1],
             key=lambda x: x["quiz_id"])

BLOOM = {"Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"}
tot = 0
probs = []
cids = []
longest = shortest = 0
for c in ch1:
    b = rpc("content_bank", {"p_quiz_id": c["quiz_id"]})
    qs = b.get("questions") or b.get("payload", {}).get("questions") or []
    for q in qs:
        tot += 1
        qid = q.get("id")
        st = q.get("stem") or {}
        if not st.get("ar") or not st.get("en"):
            probs.append("stem:" + str(qid))
        opts = q.get("options") or []
        if len(opts) != 4:
            probs.append("optcount:%s=%d" % (qid, len(opts)))
        for i, o in enumerate(opts):
            if not isinstance(o, dict) or not o.get("ar") or not o.get("en"):
                probs.append("opt:%s[%d]" % (qid, i))
        a = q.get("answer")
        if not isinstance(a, int) or not (0 <= a < len(opts)):
            probs.append("answer:%s=%r" % (qid, a))
        if q.get("bloom") not in BLOOM:
            probs.append("bloom:%s=%r" % (qid, q.get("bloom")))
        if "bloom_level" in q:
            probs.append("legacy-bloom:%s" % qid)
        ex = q.get("explanation") or {}
        if not ex.get("ar") or not ex.get("en"):
            probs.append("expl:" + str(qid))
        if not q.get("concept_id"):
            probs.append("concept:" + str(qid))
        cids.append(q.get("concept_id"))
        for o in opts:
            for t in (o.get("en"), o.get("ar")):
                if "$" in t or "\\" in t:
                    probs.append("formula:%s" % qid)
        if isinstance(a, int) and len(opts) == 4:
            L = [len(o["en"]) for o in opts]
            if L[a] == max(L) and L.count(L[a]) == 1:
                longest += 1
            elif L[a] == min(L) and L.count(L[a]) == 1:
                shortest += 1

print("live questions audited:", tot)
print("problems:", len(probs))
for p in probs[:8]:
    print("   -", p)
print("unique concept_ids:", len(set(cids)), "of", len(cids))
print("EN answer unique-longest: %d (%.0f%%)   unique-shortest: %d (%.0f%%)"
      % (longest, 100.0 * longest / tot, shortest, 100.0 * shortest / tot))
