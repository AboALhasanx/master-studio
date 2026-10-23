import json, re, urllib.request

src = open(r"C:\Users\gokoq\mcq-portal\js\supabase-config.js", encoding="utf-8").read()
url = re.search(r"url:\s*'([^']+)'", src).group(1)
key = re.search(r"key:\s*'([^']+)'", src).group(1)


def rpc(name, body):
    req = urllib.request.Request(
        url + "/rest/v1/rpc/" + name,
        data=json.dumps(body).encode(),
        headers={"apikey": key, "Authorization": "Bearer " + key, "Content-Type": "application/json"},
    )
    return json.load(urllib.request.urlopen(req, timeout=60))


m = rpc("content_manifest", {})
print("manifest version:", m.get("version"))

for s in m["subjects"]:
    if s.get("subject_id") != "01_Cyber_Security":
        continue
    chs = s["chapters"]
    c5 = [c for c in chs if c.get("chapter_no") == 5]
    print("cyber banks:", len(chs), " chapters:", sorted({c.get("chapter_no") for c in chs}))
    print("chapter 5 banks:", len(c5), " questions:", sum(c["count"] for c in c5))
    print()
    ids = set()
    for c in sorted(c5, key=lambda x: x["quiz_id"]):
        ids.add(c["quiz_id"])
        t = c.get("topic") or {}
        print("  %-56s %3d q  v%s" % (c["quiz_id"], c["count"], c.get("version")))
        print("      EN: %s" % t.get("en"))
        print("      AR: %s" % t.get("ar"))

    # retired bank must be absent from the whole subject
    allids = {c["quiz_id"] for c in chs}
    print()
    print("Quiz_02_Risk_Assessment still present?", "Quiz_02_Risk_Assessment" in allids)
    print("ModelB still present?", any("Ch04_ModelB" in i for i in allids))
