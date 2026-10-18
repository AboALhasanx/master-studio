#!/usr/bin/env python3
"""Push one Master-Studio quiz bank to the student portal (mcq-portal).

The single command every agent uses (see 00_STUDIO_HUB/PORTAL_MEMORY.md):

    python 90_Shared_Toolbox/tools/portal_push.py "<Quiz.json>" --subject <ID> --chapter <N> [--dry-run]

What it does:
  1. Validates structure (4 options per language, answer<->correct sync).
  2. Converts (chapter_no, demo:false) and writes data/banks/<subj>_ChNN_<stem>.json.
  3. Replaces any demo banks of that subject (first real push exits test content).
  4. Rebuilds the subject/chapter entry in data/index.json (test_mode auto-flips
     to false once no demo bank remains), refreshes sw.js cache list + version.

Privacy: refuses any source that is not a Quiz_*.json bank.
Exit: 0 ok · 1 structural failure (bank skipped, nothing written) · 2 usage error.
"""
import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

TOOLBOX = Path(__file__).resolve().parent
VAULT = TOOLBOX.parent.parent
SEM1 = VAULT / "01_Semester_1"
PORTAL_DEFAULT = Path("C:/Users/gokoq/mcq-portal")

SUBJECT_TITLES = {
    "01_Cyber_Security": "الأمن السيبراني",
    "02_English_Language": "اللغة الإنجليزية",
    "03_Data_Mining": "تنقيب البيانات",
    "04_Advanced_Software_Eng": "هندسة البرمجيات",
    "05_Soft_Computing": "الحوسبة اللينة",
}


def fail(msg, code=1):
    print(f"portal_push: ERROR: {msg}", file=sys.stderr)
    return code


def structural_errors(bank):
    errs = []
    qs = bank.get("questions")
    if not isinstance(qs, list) or not qs:
        return ["no questions array"]
    for q in qs:
        qid = q.get("id", "?")
        for key in ("options", "options_ar", "options_en"):
            v = q.get(key)
            if not isinstance(v, list) or len(v) != 4:
                errs.append(f"{qid}:{key} len!=4")
        ans, cor = q.get("answer"), q.get("correct")
        if not (isinstance(cor, int) and 0 <= cor <= 3 and "ABCD"[cor] == ans):
            errs.append(f"{qid}:answer/correct mismatch ({ans}/{cor})")
    return errs


def psychometric_warnings(bank):
    warns = []
    qs = bank.get("questions", [])
    dist = {L: 0 for L in "ABCD"}
    for q in qs:
        dist[q.get("answer")] = dist.get(q.get("answer"), 0) + 1
        opts = q.get("options", [])
        cor = q.get("correct", 0)
        if len(opts) == 4:
            cl = len(str(opts[cor]))
            dl = sum(len(str(o)) for i, o in enumerate(opts) if i != cor) / 3
            if dl > 0 and cl / dl > 1.35:
                warns.append(f"{q.get('id')}:correct {cl/dl:.2f}x longer than distractors")
    n = len(qs)
    if n >= 8:
        for L, c in dist.items():
            if c == 0:
                warns.append(f"positional bias: {L}=0/{n}")
            elif c / n > 0.40:
                warns.append(f"positional bias: {L}={c}/{n} ({c/n:.0%})")
    if any(not q.get("explanation") for q in qs):
        warns.append("some questions lack explanation")
    return warns


def refresh_sw(portal, bank_files):
    sw = portal / "sw.js"
    text = sw.read_text(encoding="utf-8")
    static_entries = [
        "'./'", "'./index.html'", "'./manifest.json'",
        "'./css/quiz.css'", "'./css/portal.css'",
        "'./js/app.js'", "'./js/analytics.js'", "'./js/quiz-vault.js'",
        "'./js/lucide.min.js'", "'./js/pwa.js'",
        "'./data/index.json'",
    ]
    data_entries = [f"'./data/banks/{p.name}'" for p in sorted(bank_files)]
    sound_entries = [
        "'./sounds/correct.mp3'", "'./sounds/wrong.mp3'",
        "'./sounds/completed.mp3'", "'./sounds/fail.mp3'",
    ]
    new_core = "[\n  " + ",\n  ".join(static_entries + data_entries + sound_entries) + ",\n]"
    text, n = re.subn(r"\[.*?\]", new_core, text, count=1, flags=re.S)
    if n != 1:
        return fail("CORE array not found in sw.js"), None
    m = re.search(r"mcq-portal-v(\d+)", text)
    if not m:
        return fail("CACHE version not found in sw.js"), None
    ver = int(m.group(1)) + 1
    text = text.replace(m.group(0), f"mcq-portal-v{ver}")
    sw.write_text(text, encoding="utf-8")
    return 0, ver


def main():
    ap = argparse.ArgumentParser(description="Push a quiz bank to mcq-portal")
    ap.add_argument("quiz", help="Vault Quiz_*.json path (abs or relative to 01_Semester_1)")
    ap.add_argument("--subject", required=True, help="Portal subject id, e.g. 01_Cyber_Security")
    ap.add_argument("--chapter", required=True, type=int, help="Chapter number (1-based)")
    ap.add_argument("--portal", default=str(PORTAL_DEFAULT))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    src = Path(args.quiz)
    if not src.is_absolute():
        src = SEM1 / args.quiz
    if src.name.startswith("Quiz_") is False or src.suffix != ".json":
        return fail(f"refuses non-bank source: {src} (only Quiz_*.json cross the boundary)")
    if not src.exists():
        return fail(f"source not found: {src}")
    if args.chapter < 1:
        return fail("--chapter must be >= 1", 2)

    try:
        bank = json.loads(src.read_text(encoding="utf-8"))
    except Exception as e:
        return fail(f"unparsable JSON: {e}")

    errs = structural_errors(bank)
    if errs:
        print(f"portal_push: SKIPPED {src.name}: structural errors:")
        for e in errs[:10]:
            print(f"  - {e}")
        return 1
    for w in psychometric_warnings(bank):
        print(f"portal_push: warn: {w}")

    portal = Path(args.portal)
    banks_dir = portal / "data" / "banks"
    if not (portal / "data" / "index.json").exists():
        return fail(f"not a portal repo: {portal}")

    bank = json.loads(json.dumps(bank, ensure_ascii=False))
    bank["chapter"] = f"Chapter {args.chapter}"
    bank["chapter_no"] = args.chapter
    bank["demo"] = False
    fname = f"{args.subject}_Ch{args.chapter:02d}_{src.stem}.json"

    index_path = portal / "data" / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))

    if args.dry_run:
        print(f"portal_push: dry-run OK: {src.name} -> banks/{fname}")
        print(f"  subject={args.subject} chapter={args.chapter} questions={len(bank['questions'])}")
        return 0

    # prune demo banks of this subject (first real push clears test content).
    # Match by filename prefix AND by index entries (old demo names may differ).
    subj0 = next((s for s in index["subjects"] if s["subject_id"] == args.subject), None)
    if subj0 is None:
        subj0 = {"subject_id": args.subject,
                 "subject_title": SUBJECT_TITLES.get(args.subject, args.subject),
                 "chapters": []}
        index["subjects"].append(subj0)
    for p in banks_dir.glob(f"{args.subject}_*.json"):
        try:
            old = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            old = {}
        if old.get("demo") and not bank.get("demo"):
            p.unlink()
            print(f"portal_push: pruned demo {p.name}")
    for c in list(subj0.get("chapters", [])):
        bp = portal / "data" / c.get("bank", "")
        drop = False
        if not bp.exists():
            drop = True
        else:
            try:
                demo_flag = bool(json.loads(bp.read_text(encoding="utf-8")).get("demo"))
            except Exception:
                demo_flag = False
            if demo_flag and not bank.get("demo"):
                try:
                    bp.unlink()
                except OSError:
                    pass
                print(f"portal_push: pruned demo {bp.name}")
                drop = True
        if drop:
            subj0["chapters"].remove(c)
    (banks_dir / fname).write_text(json.dumps(bank, ensure_ascii=False, indent=1), encoding="utf-8")

    subj = subj0
    subj["chapters"] = [c for c in subj["chapters"] if c.get("chapter_no") != args.chapter]
    subj["chapters"].append({
        "chapter_no": args.chapter,
        "quiz_id": bank["quiz_id"],
        "topic": bank.get("topic", ""),
        "bank": f"banks/{fname}",
    })
    subj["chapters"].sort(key=lambda c: c["chapter_no"])

    remaining_demo = False
    referenced = {c.get("bank", "") for s in index["subjects"] for c in s.get("chapters", [])}
    for p in banks_dir.glob("*.json"):
        rel = f"banks/{p.name}"
        try:
            is_demo = bool(json.loads(p.read_text(encoding="utf-8")).get("demo"))
        except Exception:
            is_demo = False
        if rel not in referenced and is_demo:
            p.unlink()
            print(f"portal_push: pruned orphan demo {p.name}")
        elif is_demo:
            remaining_demo = True
    index["test_mode"] = bool(remaining_demo)
    index["updated"] = str(date.today())
    index["version"] = int(index.get("version", 1)) + 1
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")

    rc, ver = refresh_sw(portal, list(banks_dir.glob("*.json")))
    if rc:
        return rc
    print(f"portal_push: OK {src.name} -> {fname} (ch{args.chapter}, sw=v{ver}, test_mode={index['test_mode']})")
    print("portal_push: verify locally, then: cd C:/Users/gokoq/mcq-portal && vercel --prod --yes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
