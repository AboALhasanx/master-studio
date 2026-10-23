import json, re, urllib.request

src = open(r"C:\Users\gokoq\mcq-portal\js\supabase-config.js", encoding="utf-8").read()
url = re.search(r"url:\s*'([^']+)'", src).group(1)
key = re.search(r"key:\s*'([^']+)'", src).group(1)

req = urllib.request.Request(
    url + "/rest/v1/rpc/content_manifest",
    data=b"{}",
    headers={"apikey": key, "Authorization": "Bearer " + key, "Content-Type": "application/json"},
)
m = json.load(urllib.request.urlopen(req, timeout=30))
print("SUPABASE content_manifest version:", m.get("version"))

for s in m["subjects"]:
    if s.get("subject_id") == "01_Cyber_Security":
        chs = s["chapters"]
        c4 = [c for c in chs if c.get("chapter_no") == 4]
        print("Cyber Security banks:", len(chs), " chapters:",
              sorted({c.get("chapter_no") for c in chs}))
        print("chapter 4 banks:", len(c4), " questions:", sum(c["count"] for c in c4))
        print()
        for c in c4:
            print("  %-52s %3d q  v%s" % (c["quiz_id"], c["count"], c["version"]))
