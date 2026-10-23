#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The content portal: the agent publishes here, the app reads from here.

    python 90_Shared_Toolbox/tools/portal_content.py sync
    python 90_Shared_Toolbox/tools/portal_content.py status
    python 90_Shared_Toolbox/tools/portal_content.py hide  Quiz_Ch02_DrHuda_20MCQ
    python 90_Shared_Toolbox/tools/portal_content.py show  Quiz_Ch02_DrHuda_20MCQ
    python 90_Shared_Toolbox/tools/portal_content.py pull

What sync does:
  1. reads the canonical banks from 01_Semester_1/<subject>/07_Quizzes_&_Anki/
  2. validates them (the vault gate + the portal v3 gate + the LaTeX check)
  3. merges with what is already published (an Arabic translation or a topic
     title that only exists in the portal is never dropped)
  4. upserts them into Supabase (content_banks) — the runtime copy the PWA reads
  5. moves the global content version (only when something really changed)
  6. logs the publish (content_publishes)

The app pulls `content_manifest()` (tiny) and then only the banks whose version
changed, and keeps them in a local cache so everything works offline.

Secrets: the service key is fetched at run time with the Supabase Management
token. It never ships in the app.
"""
from __future__ import annotations

import argparse
import datetime
import io
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parent.parent
sys.path.insert(0, str(HERE))

# the vault-side helpers already know how to read, validate and merge a bank
from publish_quizzes import (  # noqa: E402
    discover_vault_banks,
    index_chapters,
    load_portal_schema,
    merge_bank,
    read_index,
    validate_bank,
    DEFAULT_PORTAL,
)

PROJECT = os.environ.get("SUPABASE_PROJECT", "gywniovuupjmllbmjmai")
API = "https://api.supabase.com/v1"

# one credential chain for every tool: env -> PAT file -> refreshed OAuth token
from supabase_auth import CredentialError, access_token, describe, service_key  # noqa: E402,F401


class Rest:
    def __init__(self):
        self.key = service_key(PROJECT)
        self.base = "https://%s.supabase.co/rest/v1" % PROJECT

    def call(self, method, path, body=None, prefer=None):
        data = json.dumps(body).encode("utf-8") if body is not None else None
        headers = {
            "apikey": self.key,
            "Authorization": "Bearer " + self.key,
            "Content-Type": "application/json",
        }
        if prefer:
            headers["Prefer"] = prefer
        req = urllib.request.Request(self.base + path, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as r:
                raw = r.read().decode("utf-8")
                return r.status, (json.loads(raw) if raw.strip() else None)
        except urllib.error.HTTPError as exc:
            return exc.code, exc.read().decode("utf-8")[:300]

    def select(self, path):
        return self.call("GET", path)

    def upsert(self, table, rows):
        return self.call("POST", "/" + table, rows,
                         prefer="resolution=merge-duplicates,return=minimal")

    def patch(self, path, patch):
        return self.call("PATCH", path, patch, prefer="return=minimal")


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def chapter_number(quiz_id, raw, path, repo_index):
    """Where this chapter sits. The repo index is the authority, then the bank
    itself, then the file name (Quiz_Ch03_ / Quiz_03_)."""
    if quiz_id in repo_index:
        return int(repo_index[quiz_id][2])
    for key in ("chapter_no", "chapterNo"):
        try:
            if raw.get(key):
                return int(raw[key])
        except (TypeError, ValueError):
            pass
    m = re.search(r"(?:Ch|Quiz_)(\d+)", Path(path).stem)
    if m:
        return int(m.group(1))
    m = re.search(r"(\d+)", str(raw.get("chapter") or ""))
    if m:
        return int(m.group(1))
    return 0


def current_meta(rest: Rest):
    status, rows = rest.select("/content_meta?id=eq.1&select=version,updated_at")
    if status != 200 or not isinstance(rows, list) or not rows:
        return {"version": 0, "updated_at": None}
    return rows[0]


def current_banks(rest: Rest):
    status, rows = rest.select("/content_banks?select=quiz_id,subject_id,chapter_no,payload,version,hidden,topic_ar,topic_en,updated_at,published_at")
    if status != 200 or not isinstance(rows, list):
        return {}
    return {r["quiz_id"]: r for r in rows}


def log_publish(rest: Rest, actor, action, quiz_id=None, version=None):
    rest.upsert("content_publishes", [{
        "actor": actor, "action": action, "quiz_id": quiz_id, "version": version,
    }])


def retire_candidates(published, vault_ids, scanned_subjects):
    """Portal rows that are still live but have no file in the vault any more."""
    out = []
    for quiz_id, row in sorted(published.items()):
        row = row or {}
        if quiz_id in vault_ids or row.get("hidden"):
            continue
        # a subject whose folder vanished is not proof of retirement
        if row.get("subject_id") not in scanned_subjects:
            continue
        out.append(quiz_id)
    return out


# --------------------------------------------------------------------------- #
# sync
# --------------------------------------------------------------------------- #
def sync(args) -> int:
    portal = Path(args.portal).resolve()
    schema = load_portal_schema(portal)
    rest = Rest()
    published = current_banks(rest)
    meta = current_meta(rest)
    repo_index = index_chapters(read_index(portal))
    # the Arabic subject titles live in the portal index, not in every bank
    repo_titles = {}
    for sub in read_index(portal).get("subjects", []):
        if sub.get("subject_id"):
            repo_titles[sub["subject_id"]] = sub.get("subject_title") or ""
    published_titles = {}
    status, rows = rest.select("/content_banks?select=subject_id,subject_title")
    if status == 200 and isinstance(rows, list):
        for r in rows:
            if r.get("subject_title"):
                published_titles[r["subject_id"]] = r["subject_title"]
    banks_by_subject = discover_vault_banks(args.subject)
    if not banks_by_subject:
        print("no banks found in the vault")
        return 1

    rows = []
    changed = 0
    problems = 0
    vault_ids = set()
    for sid, entries in banks_by_subject.items():
        subject_title = sid
        for path, raw in entries:
            quiz_id = raw.get("quiz_id") or path.stem
            vault_ids.add(quiz_id)
            label = "%s / %s" % (sid, path.name)
            existing = published.get(quiz_id)
            old_payload = existing.get("payload") if existing else None
            merged = merge_bank(raw, old_payload)

            issues = validate_bank(schema, merged, label)
            if issues:
                problems += 1
                print("  x %s" % label)
                for p in issues[:5]:
                    print("      - %s" % p)
                continue

            v3 = schema.to_v3(merged)
            v3["subject_id"] = sid
            old_version = int((existing or {}).get("version") or 0)

            def fingerprint(bank):
                if not bank:
                    return ""
                parts = [{"topic": bank.get("topic")}]
                for q in bank.get("questions") or []:
                    parts.append({"id": q.get("id"), "stem": q.get("stem"),
                                  "options": q.get("options"), "answer": q.get("answer"),
                                  "explanation": q.get("explanation")})
                return json.dumps(parts, ensure_ascii=False, sort_keys=True)

            old_v3 = schema.to_v3(old_payload) if old_payload else None
            really_changed = fingerprint(old_v3) != fingerprint(v3)
            if args.bump and existing:
                really_changed = True
            version = old_version + 1 if really_changed else max(old_version, 1)
            # an untouched bank keeps its stamps, so publishing one chapter does
            # not rewrite the mirror of all 74 banks
            stamp = schema.now_iso()
            if existing and not really_changed:
                v3["updated_at"] = (old_v3 or {}).get("updated_at") or stamp
                row_updated = existing.get("updated_at") or stamp
                row_published = existing.get("published_at") or stamp
            else:
                row_updated = row_published = stamp
            if really_changed:
                changed += 1
                print("  + %s -> v%d (%d questions%s)" % (
                    label, version, len(v3["questions"]),
                    ", math" if v3.get("has_math") else ""))
            else:
                print("  = %s (v%d)" % (label, version))

            chapter_no = int((existing or {}).get("chapter_no") or 0) or chapter_number(quiz_id, raw, path, repo_index)
            if not chapter_no:
                had = [int((published[q] or {}).get("chapter_no") or 0)
                       for q in published if (published[q] or {}).get("subject_id") == sid]
                chapter_no = max(had + [0]) + 1
            topic = v3.get("topic") or {}
            # the portal repo's index carries the Arabic title: it wins
            subject_title = (repo_titles.get(sid) or published_titles.get(sid)
                             or v3.get("subject_title") or subject_title or sid)

            rows.append({
                "quiz_id": quiz_id,
                "subject_id": sid,
                "subject_title": subject_title,
                "chapter_no": chapter_no,
                "topic_ar": topic.get("ar") or "",
                "topic_en": topic.get("en") or "",
                "version": version,
                "question_count": len(v3.get("questions") or []),
                "has_math": bool(v3.get("has_math")),
                "material_url": (existing or {}).get("material_url") or v3.get("material_url") or "",
                "hidden": bool((existing or {}).get("hidden", False)),
                "payload": v3,
                "updated_at": row_updated,
                "published_at": row_published,
            })

    if problems and not args.force:
        print("\n%d bank(s) failed the gate - nothing was written." % problems)
        return 2

    # a bank whose file left the vault (moved to _retired/) must stop being
    # offered, otherwise the vault and the portal disagree. Only a full scan
    # may retire, and never a whole subject whose folder merely failed to read.
    stale = retire_candidates(published, vault_ids, set(banks_by_subject)) if not args.subject else []

    if args.dry_run:
        for quiz_id in stale:
            print("  - %s would be retired (no vault file)" % quiz_id)
        print("\n(dry run: nothing written)")
        return 0

    if rows:
        status, err = rest.upsert("content_banks", rows)
        if status not in (200, 201, 204):
            print("upsert failed:", status, err)
            return 3
        print("\nwrote %d banks" % len(rows))

    if stale:
        for quiz_id in stale:
            status, err = rest.patch("/content_banks?quiz_id=eq." + urllib.parse.quote(quiz_id), {"hidden": True})
            if status not in (200, 204):
                print("  ! could not retire %s: %s %s" % (quiz_id, status, err))
                problems += 1
                continue
            log_publish(rest, args.actor, "retire", quiz_id, None)
            print("  - %s retired (hidden, no vault file)" % quiz_id)
        changed += len(stale)

    if changed:
        new_version = int(meta.get("version") or 0) + 1
        rest.patch("/content_meta?id=eq.1", {"version": new_version, "updated_at": schema.now_iso()})
        print("content version -> %d" % new_version)
        for row in rows:
            log_publish(rest, args.actor, "sync", row["quiz_id"], row["version"])
    else:
        print("content version unchanged (nothing new for the students)")

    if args.notify and changed:
        notify(rows)
    return 0


def notify(rows):
    sys.path.insert(0, str(HERE))
    import subprocess
    for row in rows:
        text = "🆕 نزلت أسئلة جديدة: %s (%d سؤال)" % (row["topic_ar"] or row["subject_id"], row["question_count"])
        cmd = [sys.executable, str(HERE / "tg.py"), "--actor", os.environ.get("TG_OWNER_ID", "5664798395"),
               "publish", "--confirm", "--subject", row["subject_id"].replace("_", "-"), "--text", text]
        print("  " + " ".join(cmd[2:]))
        subprocess.run(cmd, cwd=str(VAULT))


# --------------------------------------------------------------------------- #
# status / hide / show / pull
# --------------------------------------------------------------------------- #
def status(args) -> int:
    rest = Rest()
    meta = current_meta(rest)
    published = current_banks(rest)
    print("content version: %s   updated: %s" % (meta.get("version"), meta.get("updated_at")))
    print("%-40s %-6s %-8s %-6s %s" % ("quiz_id", "ch", "version", "count", "topic"))
    for row in sorted(published.values(), key=lambda r: (r.get("subject_id") or "", r.get("quiz_id") or "")):
        status_code, detail = rest.select("/content_banks?select=subject_id,chapter_no,version,question_count,topic_ar,hidden&quiz_id=eq.%s" %
                                          urllib.parse.quote(row["quiz_id"]))
        info = (detail[0] if isinstance(detail, list) and detail else {})
        print("%-40s %-6s %-8s %-6s %s%s" % (
            row["quiz_id"], info.get("chapter_no", "?"), row.get("version"),
            info.get("question_count", "?"), (info.get("topic_ar") or "")[:40],
            "  [hidden]" if info.get("hidden") else ""))
    return 0


def set_hidden(args, hidden: bool) -> int:
    rest = Rest()
    status, err = rest.patch("/content_banks?quiz_id=eq." + urllib.parse.quote(args.quiz_id), {"hidden": hidden})
    if status not in (200, 204):
        print("failed:", status, err)
        return 1
    log_publish(rest, args.actor, "hide" if hidden else "show", args.quiz_id, None)
    if hidden:
        meta = current_meta(rest)
        rest.patch("/content_meta?id=eq.1", {"version": int(meta.get("version") or 0) + 1})
    print("%s %s" % ("hidden" if hidden else "published", args.quiz_id))
    return 0


def now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def refresh_sw_list(portal: Path) -> tuple:
    """Point the service worker's precache list at the banks that exist now.

    Returns (changed, cache). The cache name follows the release version
    (mcq-portal-<version>), so a release is what invalidates the old shell.
    """
    sw = portal / "sw.js"
    if not sw.exists():
        return False, ""
    text = io.open(sw, encoding="utf-8").read()
    banks = sorted(p.name for p in (portal / "data" / "banks").glob("*.json"))
    lines = text.split("\n")
    try:
        first = next(i for i, l in enumerate(lines) if l.strip().startswith("'./data/banks/"))
    except StopIteration:
        return False, ""
    last = first
    while last < len(lines) and lines[last].strip().startswith("'./data/banks/"):
        last += 1
    block = ["  './data/banks/%s'," % n for n in banks]
    version = ""
    vm = re.search(r"const VERSION = '([^']+)'", text)
    if vm:
        version = vm.group(1)
    new_cache = ("mcq-portal-" + version) if version else ""
    if lines[first:last] == block:
        return False, new_cache
    out = "\n".join(lines[:first] + block + lines[last:])
    io.open(sw, "w", encoding="utf-8", newline="\n").write(out)
    return True, new_cache


def pull(args) -> int:
    """Refresh the bundled fallback copy in the portal repo from what is live.

    The app reads the portal first; this mirror is what a device falls back to
    when the portal is unreachable and nothing is cached yet. It keeps the real
    chapter numbers, prunes banks that were retired, and re-points the service
    worker's precache list.
    """
    portal = Path(args.portal).resolve()
    rest = Rest()
    status, rows = rest.select("/content_banks?select=payload,quiz_id,subject_id,subject_title,"
                               "chapter_no,version,hidden,has_math,question_count")
    if status != 200 or not isinstance(rows, list):
        print("pull failed:", status, rows)
        return 1
    rows = [r for r in rows if not r.get("hidden") and (r.get("payload") or {}).get("questions")]

    data = portal / "data"
    banks_dir = data / "banks"
    banks_dir.mkdir(parents=True, exist_ok=True)
    subjects = {}
    keep = set()
    for row in rows:
        bank = row.get("payload") or {}
        sid = row.get("subject_id") or bank.get("subject_id") or "00"
        chapter = int(row.get("chapter_no") or 1)
        name = "%s_Ch%02d_%s.json" % (sid, chapter, row.get("quiz_id"))
        bank["subject_id"] = sid
        (banks_dir / name).write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        keep.add(name)
        subj = subjects.setdefault(sid, {
            "subject_id": sid,
            "subject_title": row.get("subject_title") or bank.get("subject_title") or sid,
            "chapters": [],
        })
        subj["chapters"].append({
            "chapter_no": chapter,
            "quiz_id": row.get("quiz_id"),
            "bank": "banks/" + name,
            "topic": bank.get("topic") or {},
            "count": int(row.get("question_count") or len(bank.get("questions") or [])),
            "version": int(row.get("version") or 1),
            "updated_at": bank.get("updated_at") or "",
            "has_math": bool(row.get("has_math") or bank.get("has_math")),
            "material_url": bank.get("material_url") or "",
        })
    pruned = 0
    for old in banks_dir.glob("*.json"):
        if old.name not in keep:
            old.unlink()
            pruned += 1

    index = {
        "portal": "MCQ Portal",
        "test_mode": False,
        "version": int(current_meta(rest).get("version") or 1),
        "updated_at": now_iso(),
        "subjects": [],
    }
    for sid in sorted(subjects):
        subj = subjects[sid]
        subj["chapters"].sort(key=lambda c: (c["chapter_no"], c["quiz_id"] or ""))
        index["subjects"].append(subj)
    (data / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    changed, cache = (False, "")
    if not getattr(args, "no_sw", False):
        changed, cache = refresh_sw_list(portal)

    print("pulled %d banks into %s (%d pruned)" % (len(keep), data, pruned))
    for sid in sorted(subjects):
        chs = subjects[sid]["chapters"]
        print("  %-28s %2d banks, chapters %s" % (sid, len(chs), sorted({c["chapter_no"] for c in chs})))
    if changed:
        print("service worker precache list updated -> %s (deploy the shell)" % cache)
    elif not getattr(args, "no_sw", False):
        print("service worker precache list already current")
    return 0

def main() -> int:
    ap = argparse.ArgumentParser(description="The content portal (agent side)")
    ap.add_argument("command", choices=["sync", "status", "hide", "show", "pull"])
    ap.add_argument("quiz_id", nargs="?", help="for hide / show")
    ap.add_argument("--subject", default=None, help="only this subject id")
    ap.add_argument("--portal", default=str(DEFAULT_PORTAL), help="the mcq-portal repo (pull target)")
    ap.add_argument("--actor", default="agent", help="who is publishing")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--bump", action="store_true", help="force a new version for every bank")
    ap.add_argument("--notify", action="store_true", help="post the Telegram notice")
    ap.add_argument("--force", action="store_true", help="write even if some banks fail the gate")
    ap.add_argument("--write-back", action="store_true", help="merge the result into the vault files")
    ap.add_argument("--no-sw", action="store_true", help="pull only: do not touch the service worker list")
    args = ap.parse_args()

    if args.command == "sync":
        return _guard(sync, args)
    if args.command == "status":
        return _guard(status, args)
    if args.command == "pull":
        return _guard(pull, args)
    if not args.quiz_id:
        print("hide/show needs a quiz_id")
        return 1
    return _guard(lambda a: set_hidden(a, args.command == "hide"), args)


def _guard(command, args) -> int:
    """A missing/expired credential is a message, never a traceback."""
    try:
        return command(args)
    except CredentialError as exc:
        print("\n%s" % exc)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
