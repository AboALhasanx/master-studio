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


ids = [
    "Quiz_Ch04_T01_Classical_Ciphers_And_Unicity",
    "Quiz_Ch04_T02_Symmetric_Encryption",
    "Quiz_Ch04_T03_Asymmetric_Encryption",
    "Quiz_Ch04_T04_Hybrid_Cryptography_And_Work_Factor",
    "Quiz_Ch04_T05_Hash_Functions",
    "Quiz_Ch04_T06_Digital_Signatures",
    "Quiz_Ch04_T07_Certificates_PKI_And_Trust_Model",
    "Quiz_Ch04_T08_HTTPS_TLS_And_Applications",
    "Quiz_Ch04_T09_Economic_Model_And_Challenges",
]

grand = 0
problems = 0
for qid in ids:
    b = rpc("content_bank", {"p_quiz_id": qid})
    qs = b.get("questions") or []
    errs = []
    for q in qs:
        st = q.get("stem") or {}
        if not st.get("en") or not st.get("ar"):
            errs.append("stem")
        a = q.get("answer")
        opts = q.get("options") or []
        if not isinstance(a, int) or not (0 <= a < len(opts)):
            errs.append("answer")
        if len(opts) != 4:
            errs.append("optcount")
        for o in opts:
            if not isinstance(o, dict) or not o.get("en") or not o.get("ar"):
                errs.append("optlang")
        ex = q.get("explanation") or {}
        if not ex.get("en") or not ex.get("ar"):
            errs.append("expl")
        if q.get("bloom") not in BLOOM:
            errs.append("bloom")
    grand += len(qs)
    problems += len(errs)
    print("%-52s %2d q  %s" % (qid[:52], len(qs), "OK" if not errs else "FAIL " + str(set(errs))))

print()
print("live questions fetched:", grand, " problems:", problems)
