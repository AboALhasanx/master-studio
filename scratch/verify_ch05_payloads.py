import json, re, urllib.request

src = open(r"C:\Users\gokoq\mcq-portal\js\supabase-config.js", encoding="utf-8").read()
url = re.search(r"url:\s*'([^']+)'", src).group(1)
key = re.search(r"key:\s*'([^']+)'", src).group(1)

BLOOM = {"Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"}


def rpc(name, body):
    req = urllib.request.Request(
        url + "/rest/v1/rpc/" + name,
        data=json.dumps(body).encode(),
        headers={"apikey": key, "Authorization": "Bearer " + key, "Content-Type": "application/json"},
    )
    return json.load(urllib.request.urlopen(req, timeout=60))


m = rpc("content_manifest", {})
ids = []
for s in m["subjects"]:
    if s.get("subject_id") == "01_Cyber_Security":
        ids = [c["quiz_id"] for c in s["chapters"] if c.get("chapter_no") == 5]

grand = 0
problems = 0
concepts = {}
for qid in sorted(ids):
    b = rpc("content_bank", {"p_quiz_id": qid})
    qs = b.get("questions") or []
    errs = []
    for q in qs:
        st = q.get("stem") or {}
        if not st.get("en") or not st.get("ar"):
            errs.append("stem:" + str(q.get("id")))
        a = q.get("answer")
        opts = q.get("options") or []
        if not isinstance(a, int) or not (0 <= a < len(opts)):
            errs.append("answer-range:" + str(q.get("id")))
        if len(opts) != 4:
            errs.append("optcount:" + str(q.get("id")))
        for o in opts:
            if not isinstance(o, dict) or not o.get("en") or not o.get("ar"):
                errs.append("optlang:" + str(q.get("id")))
        ex = q.get("explanation") or {}
        if not ex.get("en") or not ex.get("ar"):
            errs.append("expl:" + str(q.get("id")))
        if q.get("bloom") not in BLOOM:
            errs.append("bloom:" + str(q.get("id")))
        cid = q.get("concept_id")
        if not cid:
            errs.append("concept:" + str(q.get("id")))
        else:
            concepts.setdefault(cid, []).append(qid)
    grand += len(qs)
    problems += len(errs)
    print("%-56s %2d q  %s" % (qid, len(qs), "OK" if not errs else "FAIL " + str(set(errs))[:80]))

dupes = {k: v for k, v in concepts.items() if len(v) > 1}
print()
print("live questions:", grand, " problems:", problems)
print("unique concept_ids:", len(concepts), " duplicates:", dupes if dupes else "none")
