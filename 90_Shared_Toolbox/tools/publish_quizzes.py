# -*- coding: utf-8 -*-
"""Publish the vault's quiz banks into the student portal.

    python 90_Shared_Toolbox/tools/publish_quizzes.py --dry-run
    python 90_Shared_Toolbox/tools/publish_quizzes.py --subject 01_Cyber_Security
    python 90_Shared_Toolbox/tools/publish_quizzes.py --deploy --announce

What it does, in order:
  1. reads the canonical banks from 01_Semester_1/<subject>/07_Quizzes_&_Anki/
  2. validates them (the vault's schema gate + the portal's v3 gate + the
     LaTeX check, so a broken formula never reaches a student)
  3. MERGES them with what the portal already has: the vault is the master for
     the content, but an Arabic translation that only exists in the portal is
     never dropped. With --write-back the merged bank also goes back to the
     vault, so the translation work accumulates in the master copy.
  4. writes mcq-portal/data/banks/*.json in the portal's Canonical Schema v3
     (one bilingual shape) and rebuilds data/index.json with a version per
     chapter, bumped only when the content really changed
  5. with --deploy: commit + push + Vercel deploy
  6. with --announce: post the notice into the subject's Telegram topic

The portal picks the new chapters up on the next open, shows the student a
"new questions" notice and marks the chapter as seen once it is opened.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parent.parent
sys.path.insert(0, str(HERE))

from quiz_balancer import normalize_quiz_schema, validate_schema_v2  # noqa: E402

DEFAULT_PORTAL = Path(r"C:\Users\gokoq\mcq-portal")
# the Telegram user id that drives the owner commands (the vault's pacing.json)
OWNER_ID = int(os.environ.get("TG_OWNER_ID", "5664798395"))
SEMESTER_DIR = VAULT / "01_Semester_1"
QUIZ_DIR_NAME = "07_Quizzes_&_Anki"

AR_RE = re.compile(r"[\u0600-\u06FF]")


def load_portal_schema(portal: Path):
    sys.path.insert(0, str(portal / "tools"))
    import portal_schema  # noqa: E402
    return portal_schema


def has_ar(text) -> bool:
    return bool(AR_RE.search(str(text or "")))


# --------------------------------------------------------------------------- #
# discovery
# --------------------------------------------------------------------------- #
def discover_vault_banks(subject=None):
    out = {}
    if not SEMESTER_DIR.is_dir():
        return out
    for subject_dir in sorted(SEMESTER_DIR.iterdir()):
        if not subject_dir.is_dir():
            continue
        sid = subject_dir.name
        if subject and sid != subject:
            continue
        quiz_dir = subject_dir / QUIZ_DIR_NAME
        if not quiz_dir.is_dir():
            continue
        banks = []
        for path in sorted(quiz_dir.glob("Quiz_*.json")):
            try:
                with open(path, encoding="utf-8") as fh:
                    banks.append((path, json.load(fh)))
            except Exception as exc:
                print("  ! could not read %s: %s" % (path.name, exc))
        if banks:
            out[sid] = banks
    return out


def read_index(portal: Path) -> dict:
    path = portal / "data" / "index.json"
    if not path.exists():
        return {"version": 0, "subjects": []}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def index_chapters(index: dict):
    out = {}
    for sub in index.get("subjects", []):
        for ch in sub.get("chapters", []):
            out[ch.get("quiz_id")] = (
                sub.get("subject_id"),
                sub.get("subject_title"),
                int(ch.get("chapter_no") or 1),
                ch.get("bank") or ("banks/%s.json" % ch.get("quiz_id")),
            )
    return out


def existing_bank(portal: Path, bank_path: str):
    path = portal / "data" / bank_path
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------------------- #
# merge: the vault is the master, but nothing already translated is lost
# --------------------------------------------------------------------------- #
def portal_flat(q: dict) -> dict:
    """Flatten a portal question (v3 pairs or v2 flat) to the v2 field names."""
    if not q:
        return {}
    stem = q.get("stem") if isinstance(q.get("stem"), dict) else {}
    expl = q.get("explanation") if isinstance(q.get("explanation"), dict) else {}
    opts = q.get("options") if isinstance(q.get("options"), list) else []
    opts_ar = q.get("options_ar") or []
    if not opts_ar and opts and isinstance(opts[0], dict):
        opts_ar = [o.get("ar") or "" for o in opts]
    explanation = q.get("explanation") if isinstance(q.get("explanation"), str) else ""
    explanation_ar = q.get("explanation_ar") or expl.get("ar") or ""
    if not explanation and expl.get("en"):
        explanation = expl.get("en")
    return {
        "question_ar": q.get("question_ar") or stem.get("ar") or "",
        "text": q.get("text") or q.get("question") or "",
        "options_ar": opts_ar,
        "explanation": explanation,
        "explanation_ar": explanation_ar,
    }


def merge_question(vault_q: dict, portal_q: dict) -> dict:
    """Take the vault question and fill the gaps from the portal question."""
    out = dict(vault_q)
    if not portal_q:
        return out
    p = portal_flat(portal_q)

    # the arabic stem
    if not has_ar(out.get("question_ar")) and has_ar(p["question_ar"]):
        out["question_ar"] = p["question_ar"]
    if not out.get("text") and p["text"]:
        out["text"] = p["text"]
    # the arabic options
    oa = out.get("options_ar") or []
    pa = p["options_ar"] or []
    if len(oa) == len(pa):
        for i in range(len(oa)):
            if not has_ar(oa[i]) and has_ar(pa[i]):
                oa[i] = pa[i]
        out["options_ar"] = oa
    # the explanation (the vault sometimes has none at all)
    if not out.get("explanation") and p["explanation"]:
        out["explanation"] = p["explanation"]
    if not out.get("explanation_ar") and p["explanation_ar"]:
        out["explanation_ar"] = p["explanation_ar"]
    if not has_ar(out.get("explanation")) and has_ar(p["explanation_ar"]) and not out.get("explanation"):
        out["explanation"] = p["explanation_ar"]
    return out


def merge_bank(vault_bank: dict, portal_bank: dict) -> dict:
    if not portal_bank:
        return vault_bank
    by_id = {q.get("id"): q for q in portal_bank.get("questions") or []}
    merged = dict(vault_bank)
    merged["questions"] = [
        merge_question(q, by_id.get(q.get("id"))) for q in vault_bank.get("questions") or []
    ]
    # the Arabic topic title lives in the portal (the vault only carries the
    # English one); never lose it on a publish
    p_topic = portal_bank.get("topic") if isinstance(portal_bank.get("topic"), dict) else {}
    p_ar = (p_topic.get("ar") if p_topic else "") or portal_bank.get("topic_ar") or ""
    v_topic = merged.get("topic") if isinstance(merged.get("topic"), dict) else {}
    v_ar = (v_topic.get("ar") if v_topic else "") or merged.get("topic_ar") or ""
    if p_ar and has_ar(p_ar) and not has_ar(v_ar):
        merged["topic_ar"] = p_ar
        if isinstance(merged.get("topic"), dict):
            merged["topic"]["ar"] = p_ar
    return merged


# --------------------------------------------------------------------------- #
# validation
# --------------------------------------------------------------------------- #
def validate_bank(schema, raw: dict, label: str):
    problems = []
    try:
        ok, errs = validate_schema_v2(raw)
        if not ok:
            problems.extend("vault:%s" % e for e in errs)
    except Exception as exc:
        problems.append("vault-check-failed:%s" % exc)
    try:
        v3 = schema.to_v3(raw)
        problems.extend("v3:%s" % e for e in schema.validate_v3(v3))
    except Exception as exc:
        problems.append("v3-failed:%s" % exc)
    return problems


# --------------------------------------------------------------------------- #
# publish
# --------------------------------------------------------------------------- #
def publish(args) -> int:
    portal = Path(args.portal).resolve()
    schema = load_portal_schema(portal)
    index = read_index(portal)
    known = index_chapters(index)
    banks_by_subject = discover_vault_banks(args.subject)
    if not banks_by_subject:
        print("no banks found in %s" % SEMESTER_DIR)
        return 1

    written = []
    problems_total = []
    chapter_meta = {}
    store = {}
    write_back = []

    for sid, entries in banks_by_subject.items():
        subject_title = sid
        for subj in index.get("subjects", []):
            if subj.get("subject_id") == sid:
                subject_title = subj.get("subject_title") or sid
        next_chapter = max([c[2] for c in known.values() if c[0] == sid] or [0]) + 1
        for path, raw in entries:
            quiz_id = raw.get("quiz_id") or path.stem
            label = "%s / %s" % (sid, path.name)

            if quiz_id in known:
                _sid, subject_title, chapter_no, bank_path = known[quiz_id]
            else:
                chapter_no = next_chapter
                next_chapter += 1
                bank_path = "banks/%s_%s.json" % (sid, quiz_id)

            old = existing_bank(portal, bank_path)
            merged = merge_bank(raw, old)
            problems = validate_bank(schema, merged, label)
            if problems:
                problems_total.append((label, problems))
                print("  x %s" % label)
                for p in problems[:6]:
                    print("      - %s" % p)
                continue

            v3 = schema.to_v3(merged)
            v3["subject_id"] = sid
            v3["subject_title"] = v3.get("subject_title") or subject_title
            if not v3.get("topic", {}).get("ar"):
                v3["topic"]["ar"] = raw.get("topic") or ""

            old_version = int((old or {}).get("version") or 1)
            material_url = (old or {}).get("material_url") or ""
            v3["version"] = old_version + 1
            v3["updated_at"] = schema.now_iso()
            v3["material_url"] = material_url
            v3["question_count"] = len(v3["questions"])

            def fingerprint(bank):
                # only what the student actually sees: the questions themselves
                if not bank:
                    return ""
                parts = []
                # the topic is the title the student reads on the card, so it
                # counts as content too
                parts.append({"topic": bank.get("topic")})
                for q in bank.get("questions") or []:
                    parts.append({
                        "id": q.get("id"),
                        "stem": q.get("stem"),
                        "options": q.get("options"),
                        "answer": q.get("answer"),
                        "explanation": q.get("explanation"),
                    })
                return json.dumps(parts, ensure_ascii=False, sort_keys=True)

            old_v3 = schema.to_v3(old) if old else None
            changed = fingerprint(old_v3) != fingerprint(v3)
            if getattr(args, "bump", False) and old is not None:
                # force every device to re-download (used when a fix changes how
                # existing content renders, not what it says)
                changed = True
            if not changed and old is not None:
                v3["version"] = old_version
                v3["updated_at"] = old.get("updated_at") or v3["updated_at"]
                print("  = %s (no change, v%d)" % (label, old_version))
            else:
                print("  + %s -> v%d (%d questions%s)" % (
                    label, v3["version"], len(v3["questions"]),
                    ", math" if v3.get("has_math") else ""))
            # every bank is written in the v3 shape (that is the migration);
            # only a real content change moves the version
            written.append((bank_path, v3, label, changed))
            # the merged content (vault + the portal's translations) always
            # goes back to the vault, so the master copy keeps the Arabic
            write_back.append((path, merged))

            chapter_meta[quiz_id] = {
                "subject_id": sid,
                "subject_title": subject_title,
                "chapter_no": chapter_no,
                "bank": bank_path,
            }
            store[quiz_id] = v3

    if problems_total:
        print("\n%d bank(s) have problems - they were left untouched." % len(problems_total))
        if not args.force:
            return 2

    if args.dry_run:
        print("\n(dry run: nothing written)")
        return 0

    # ---- write the banks
    for bank_path, v3, label, changed in written:
        target = portal / "data" / bank_path
        target.parent.mkdir(parents=True, exist_ok=True)
        schema.write_json(str(target), v3)

    # ---- the unchanged ones keep their file, only the metadata is refreshed
    for quiz_id, v3 in store.items():
        meta = chapter_meta[quiz_id]
        target = portal / "data" / meta["bank"]
        if target.exists() and not any(w[0] == meta["bank"] for w in written):
            with open(target, encoding="utf-8") as fh:
                old = json.load(fh)
            if int(old.get("version") or 1) != int(v3.get("version") or 1):
                old["version"] = v3["version"]
                old["updated_at"] = v3["updated_at"]
                schema.write_json(str(target), old)

    # ---- write the merged banks back to the vault (the translations live there)
    if args.write_back:
        for path, merged in write_back:
            with open(path, encoding="utf-8") as fh:
                old = json.load(fh)
            old_q = {q.get("id"): q for q in old.get("questions") or []}
            new_q = []
            for q in merged.get("questions") or []:
                keep = dict(q)
                src = old_q.get(q.get("id"))
                if src:
                    for key in ("question_ar", "options_ar", "explanation_ar"):
                        cur = keep.get(key)
                        alt = src.get(key)
                        if alt and (not cur or (has_ar(alt) and not has_ar(cur))):
                            keep[key] = alt
                new_q.append(keep)
            old["questions"] = new_q
            schema.write_json(str(path), old)
            print("  ^ merged back into the vault: %s" % path.name)

    # ---- rebuild the index
    new_index = schema.build_index(index, store, chapter_meta)
    schema.write_json(str(portal / "data" / "index.json"), new_index)
    print("\nindex version %s -> %s (%d subjects)" % (
        index.get("version"), new_index["version"], len(new_index["subjects"])))

    if args.deploy:
        return deploy(portal, written, new_index, announce_too=args.announce)
    if args.announce:
        announce(written)
    return 0


# --------------------------------------------------------------------------- #
# deploy + announce
# --------------------------------------------------------------------------- #
def deploy(portal: Path, written, new_index, announce_too=False) -> int:
    print("\n-- deploying")
    def run(cmd):
        return subprocess.run(cmd, cwd=str(portal), shell=True)
    run("git add -A")
    label = ", ".join(w[2] for w in written[:4]) or "content update"
    run('git commit -m "Publish content: %s"' % label.replace('"', "'"))
    run("git push")
    r = run("npx -y vercel@latest --prod --yes")
    if r.returncode != 0:
        print("deploy failed")
        return 3
    print("deployed")
    if announce_too:
        announce(written)
    return 0


def announce(written):
    if not written:
        return
    print("\n-- announcing")
    for _path, v3, label, changed in written:
        if not changed:
            continue
        subject = v3.get("subject_id") or ""
        text = ("\U0001F195 \u0646\u0632\u0644\u062a \u0623\u0633\u0626\u0644\u0629 \u062c\u062f\u064a\u062f\u0629: %s (%d \u0633\u0624\u0627\u0644)" % (
            v3.get("topic", {}).get("ar") or subject,
            len(v3.get("questions") or []),
        ))
        # the actor is a global flag, it goes before the subcommand
        # the vault's topic keys use hyphens (01-Cyber-Security)
        cmd = [sys.executable, str(HERE / "tg.py"), "--actor", str(OWNER_ID),
               "publish", "--confirm", "--subject", subject.replace("_", "-"), "--text", text]
        print("  " + " ".join(cmd[2:]))
        subprocess.run(cmd, cwd=str(VAULT))


def main() -> int:
    ap = argparse.ArgumentParser(description="Publish the vault's quiz banks into the portal")
    ap.add_argument("--subject", default=None, help="only this subject id (default: all)")
    ap.add_argument("--portal", default=str(DEFAULT_PORTAL), help="the mcq-portal repository")
    ap.add_argument("--dry-run", action="store_true", help="validate only, write nothing")
    ap.add_argument("--deploy", action="store_true", help="commit, push and deploy the portal")
    ap.add_argument("--announce", action="store_true", help="post the notice into Telegram")
    ap.add_argument("--write-back", action="store_true", help="merge the result back into the vault")
    ap.add_argument("--force", action="store_true", help="write even if some banks fail the gate")
    ap.add_argument("--bump", action="store_true", help="force a new version for every bank (re-download)")
    args = ap.parse_args()
    return publish(args)


if __name__ == "__main__":
    raise SystemExit(main())
