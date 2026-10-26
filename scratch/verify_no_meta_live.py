#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confirm the LIVE payloads never mention the handout."""
import json
import re
import urllib.request

src = open(r"C:\Users\gokoq\mcq-portal\js\supabase-config.js", encoding="utf-8").read()
url = re.search(r"url:\s*'([^']+)'", src).group(1)
key = re.search(r"key:\s*'([^']+)'", src).group(1)

META = re.compile(
    r"\bthe lecture|lecture notes|\bthe notes\b|\bthe booklet\b|\bthe handout\b|"
    r"\baccording to\b|\bthe doctor\b|\bthe syllabus\b|\bher own\b|"
    r"المحاضرة|الملزمة|الملزمه|الدكتورة|الشرائح|المصدر", re.I)


def rpc(n, b):
    r = urllib.request.Request(url + "/rest/v1/rpc/" + n, data=json.dumps(b).encode(),
                               headers={"apikey": key, "Authorization": "Bearer " + key,
                                        "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=60))


m = rpc("content_manifest", {})
bad = 0
total = 0
for ch in (1, 2):
    banks = sorted([c for s in m["subjects"] if s["subject_id"] == "01_Cyber_Security"
                    for c in s["chapters"] if c.get("chapter_no") == ch],
                   key=lambda x: x["quiz_id"])
    for c in banks:
        b = rpc("content_bank", {"p_quiz_id": c["quiz_id"]})
        for q in (b.get("questions") or []):
            total += 1
            texts = [q["stem"]["en"], q["stem"]["ar"],
                     q["explanation"]["en"], q["explanation"]["ar"]]
            for o in q["options"]:
                texts += [o["en"], o["ar"]]
            for t in texts:
                if META.search(t or ""):
                    bad += 1
                    print("  META", c["quiz_id"][-6:], q["id"], "|", t[:100])
print("live questions checked:", total, " meta references found:", bad)
