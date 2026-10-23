import json, re, urllib.request, datetime

src = open(r"C:\Users\gokoq\mcq-portal\js\supabase-config.js", encoding="utf-8").read()
url = re.search(r"url:\s*'([^']+)'", src).group(1)
key = re.search(r"key:\s*'([^']+)'", src).group(1)

req = urllib.request.Request(
    url + "/rest/v1/rpc/content_manifest",
    data=b"{}",
    headers={"apikey": key, "Authorization": "Bearer " + key, "Content-Type": "application/json"},
)
m = json.load(urllib.request.urlopen(req, timeout=30))
print("manifest version   :", m.get("version"))
print("manifest updated_at:", m.get("updated_at"))
print("utc now            :", datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"))
