import sys, json, urllib.parse
sys.path.insert(0, r'C:\Users\gokoq\Master-Studio\90_Shared_Toolbox\tools')
from portal_content import Rest

KEEP_USER = "dfebceba-5ea6-4a70-9adf-8959345983c5"   # the tablet: طالب التابلت
KEEP_LEAGUE = ["dfebceba-5ea6-4a70-9adf-8959345983c5", "tg:5664798395"]  # + ابـوالــحسن

rest = Rest()

def count(table, query=""):
    s, rows = rest.select("/%s?select=*&limit=1000%s" % (table, query))
    return s, (len(rows) if isinstance(rows, list) else rows)

for t in ("portal_users", "portal_data", "league_xp", "login_links", "content_banks", "content_publishes"):
    print("%-18s %s" % (t, count(t)))

# what will go
s, users = rest.select("/portal_users?select=id,handle&limit=1000")
drop_users = [u["id"] for u in users if u["id"] != KEEP_USER]
print("delete users:", len(drop_users), "keep:", [u["handle"] for u in users if u["id"] == KEEP_USER])
s, rows = rest.select("/league_xp?select=user_id,username&limit=1000")
drop_league = [r for r in rows if r["user_id"] not in KEEP_LEAGUE]
print("delete league rows:", len(drop_league))

import os
if os.environ.get("APPLY") != "1":
    print("dry run - set APPLY=1 to delete")
    raise SystemExit(0)

s, err = rest.call("DELETE", "/portal_users?id=neq." + KEEP_USER, prefer="return=minimal")
print("delete portal_users:", s, err)
s, err = rest.call("DELETE", "/portal_data?user_id=neq." + KEEP_USER, prefer="return=minimal")
print("delete portal_data:", s, err)
s, err = rest.call("DELETE", "/league_xp?user_id=neq.%s&user_id=neq.%s" % (KEEP_LEAGUE[0], urllib.parse.quote(KEEP_LEAGUE[1])), prefer="return=minimal")
print("delete league_xp:", s, err)
s, err = rest.call("DELETE", "/login_links?code=not.is.null", prefer="return=minimal")
print("delete login_links:", s, err)

for t in ("portal_users", "portal_data", "league_xp", "login_links", "content_banks", "content_publishes"):
    print("%-18s %s" % (t, count(t)))
print("kept users:", rest.select("/portal_users?select=handle,name&limit=50"))
print("kept league:", rest.select("/league_xp?select=username,name,xp,answered&limit=50"))
