#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""What the portal is actually serving right now."""
import json
import re
import urllib.request

src = open(r"C:\Users\gokoq\mcq-portal\js\supabase-config.js", encoding="utf-8").read()
url = re.search(r"url:\s*'([^']+)'", src).group(1)
key = re.search(r"key:\s*'([^']+)'", src).group(1)
req = urllib.request.Request(
    url + "/rest/v1/rpc/content_manifest", data=b"{}",
    headers={"apikey": key, "Authorization": "Bearer " + key,
             "Content-Type": "application/json"})
m = json.load(urllib.request.urlopen(req, timeout=30))
print("LIVE content version:", m.get("version"))
for s in m["subjects"]:
    if s["subject_id"] != "01_Cyber_Security":
        continue
    for ch in (1, 2, 3):
        rows = [c for c in s["chapters"] if c.get("chapter_no") == ch]
        print("  chapter %d: %2d banks, %3d questions"
              % (ch, len(rows), sum(c["count"] for c in rows)))
