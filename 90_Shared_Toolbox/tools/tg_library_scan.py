#!/usr/bin/env python3
"""tg_library_scan — build the personal-library manifests from the vault.

`tg.py library` sends what a manifest lists; this tool *writes* those
manifests, so "publish everything in the folders" is one reproducible command
instead of a hand-kept list. It is the curation half of the shelf: it decides
what belongs, tags it, and proves what it left out.

The rules, in one place (each one was a real decision, not a default):

* ``01_Semester_1/<subject>/``  -> ``all.json``      (the six subject shelves)
* ``00_STUDIO_HUB/`` outside ``telegram/`` -> ``official.json`` (university
  documents: regulations, curricula, the rules-and-plan pair)
* ``00_STUDIO_HUB/telegram/`` is publish **staging** — the card documents, the
  chapter PDFs, the placeholder pages, ``_work`` copies and the compressed
  library copies. Every file there is hashed and *reserved*, so nothing already
  sent can be sent twice; only ``catalog/files/*.pdf`` (the per-subject
  documents the cards point at) are also queued, because the card booklet is
  real material the shelf should carry.
* Internal scaffolding never ships: ``_sandbox_trial``, ``_superseded``,
  ``_leakscan``, ``_build``, ``_backup``, ``00_INDEX``, ``99_SOURCE_MAP``,
  ``- Copy``, ``LOCKED_OLD``, ``biditest``.
* Exact duplicates (same sha256) ship once; so do same-size same-name twins
  across folders (the same build exported twice).
* Display names are fitted to Telegram's **62-byte** budget, and files that
  share a name are told apart by the folders above them (Ch01's ``T1_MCQ.pdf``
  from Ch02's). The file bytes are never touched: ``library --send`` stages a
  byte-identical copy under the display name and drops it after the upload.
* Files over the Bot API's **50 MB** upload ceiling are reported, not queued.
  Compressing them first is a separate, explicit act (``pdf_compress.py``) —
  the scan never silently drops material, and never silently keeps it either.

Usage:
    python tg_library_scan.py [--root DIR] [--out-dir DIR] [--chat ID] [--json]

Exit codes: 0 = manifests written, 2 = bad usage.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

BOT_LIMIT = 50 * 1000 * 1000
NAME_BUDGET = 62
EXTS = (".pdf", ".pptx")

#: subject folder on disk -> subject key (the catalog JSON filenames)
SUBJECT_DIRS = {
    "01_Cyber_Security": "01-Cyber-Security",
    "02_English_Language": "02-English-Language",
    "03_Data_Mining": "03-Data-Mining",
    "04_Advanced_Software_Eng": "04-Advanced-Software-Eng",
    "05_Soft_Computing": "05-Soft-Computing",
    "06_Artificial_Intelligence": "06-Artificial-Intelligence",
}

#: first folder under the subject -> kind (the second hashtag)
FOLDER_KIND = {
    "01_Lectures": "lecture",
    "02_Raw_Materials": "source",
    "03_Study_Notes": "summary",
    "04_Academic_Papers": "paper",
    "05_Seminars_&_Slides": "slides",
    "06_Diagrams_&_Mindmaps": "diagram",
    "07_Quizzes_&_Anki": "quiz",
}

INTERNAL_PARTS = ("_sandbox_trial", "_superseded", "_leakscan", "_build", "_backup")
INTERNAL_NAMES = ("00_index", "99_source_map", "- copy", "locked_old", "biditest")

#: catalog/files/<name>.pdf -> subject, by the words the cards themselves use
STAGING_PREFIXES = (
    ("أمن المعلومات", "01-Cyber-Security"),
    ("انكليزي", "02-English-Language"),
    ("اللغة الإنجليزية", "02-English-Language"),
    ("تنقيب البيانات", "03-Data-Mining"),
    ("03-Data-Mining", "03-Data-Mining"),
    ("هندسة البرمجيات", "04-Advanced-Software-Eng"),
    ("حوسبة ناعمة", "05-Soft-Computing"),
    ("الحوسبة الناعمة", "05-Soft-Computing"),
    ("ذكاء اصطناعي", "06-Artificial-Intelligence"),
    ("الذكاء الاصطناعي", "06-Artificial-Intelligence"),
)

DEFAULT_CHAT = "3710711332"  # the group id without its -100 prefix


def repo_root() -> Path:
    """The vault root — two levels above ``90_Shared_Toolbox/tools/``."""
    return Path(__file__).resolve().parents[2]


def catalog_cards(root: Path) -> dict[str, int]:
    """subject key -> card message id, read from the catalog JSON (the source
    of truth for what the topics actually published)."""
    cards: dict[str, int] = {}
    for path in sorted((root / "00_STUDIO_HUB/telegram/catalog").glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        message_id = data.get("catalog_message_id")
        if isinstance(message_id, int):
            cards[path.stem] = message_id
    return cards


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fit_name(name: str, budget: int = NAME_BUDGET) -> str:
    """Telegram caps display names at ``budget`` *bytes*.

    Drop trailing words until it fits, then hard-cut at a UTF-8 boundary if a
    single long word remains (Arabic titles are usually hyphen-joined, so there
    are no spaces to drop). The file itself is never touched.
    """
    if len(name.encode("utf-8")) <= budget:
        return name
    stem, ext = os.path.splitext(name)
    words = stem.replace("-", " ").replace("_", " ").split(" ")
    while words and len((" ".join(words) + ext).encode("utf-8")) > budget:
        words.pop()
    out = " ".join(words).strip(" .-_")
    while len((out + ext).encode("utf-8")) > budget and out:
        out = out[:-1].rstrip(" .-_")
    return (out + ext) if out else (name[:12] + ext)


def classify(rel: Path):
    """-> ``(subject, kind)`` when the file belongs on a shelf, else
    ``(None, reason)`` naming why it does not."""
    parts = rel.parts
    name = rel.name.lower()
    if any(part.lower().startswith(INTERNAL_PARTS) for part in parts):
        return None, "internal-folder"
    if any(marker in name for marker in INTERNAL_NAMES):
        return None, "internal-name"

    if parts[0] == "00_STUDIO_HUB":
        if "telegram" in parts:
            if parts[2:4] == ("catalog", "files") and len(parts) == 5:
                for prefix, key in STAGING_PREFIXES:
                    if rel.stem.startswith(prefix):
                        return (key, "card"), None
                return None, "unmapped-staging"
            return None, "publish-staging"      # lectures, placeholders, _work
        if parts[1:2] in (("official_docs",), ("official_curriculum",)) or len(parts) == 2:
            return ("00-University", "rules"), None
        return None, "outside-scope"

    if parts[0] == "01_Semester_1" and parts[1] in SUBJECT_DIRS:
        subject = SUBJECT_DIRS[parts[1]]
        folder = parts[2] if len(parts) > 3 else ""
        if folder.startswith("08_DeepStudy"):
            return (subject, "exam"), None
        return (subject, FOLDER_KIND.get(folder, "other")), None
    return None, "outside-scope"


def folder_token(path: Path, levels: int) -> str:
    """The ``levels`` folder names directly above a file, space-joined."""
    return " ".join(path.parts[-(levels + 1):-1])


def disambiguate(items: list) -> None:
    """Two files may share a display name (Ch01's ``T1_MCQ.pdf`` vs Ch02's).

    Telegram shows only the name, so tell them apart with the folders above
    them, and with the size when even that is not enough.
    """
    by_name: dict[str, list] = {}
    for item in items:
        by_name.setdefault(item["display"], []).append(item)
    for display, group in by_name.items():
        if len(group) < 2:
            continue
        levels, tokens = 1, []
        while levels <= 4:
            tokens = [folder_token(Path(i["file"]), levels) for i in group]
            distinct = len(set(tokens)) == len(group)
            readable = all(token and token != Path(i["display"]).stem
                           for token, i in zip(tokens, group))
            if distinct and readable:
                break
            levels += 1
        for item, token in zip(group, tokens):
            if token:
                item["display"] = fit_name(f"{token} {Path(item['display']).name}")
            else:
                size_mb = Path(item["_abs"]).stat().st_size / 1e6
                item["display"] = fit_name(
                    f"{Path(display).stem} ({size_mb:.1f}MB).pdf")


def scan(root: Path, chat: str = DEFAULT_CHAT):
    """Walk the vault and return ``(manifests, rows)`` — the queued items per
    manifest plus the full inventory, including what was left out and why."""
    cards = catalog_cards(root)
    rows: list[dict] = []
    for base in (root / "01_Semester_1", root / "00_STUDIO_HUB"):
        for ext in EXTS:
            for path in sorted(base.rglob(f"*{ext}")):
                rel = path.relative_to(root)
                tag, skip = classify(rel)
                rows.append({
                    "path": str(rel).replace("\\", "/"),
                    "size": path.stat().st_size,
                    "name_bytes": len(path.name.encode("utf-8")),
                    "subject": tag[0] if tag else None,
                    "kind": tag[1] if tag else None,
                    "skip": skip,
                })

    # every file is hashed once: staging is reserved against re-sending
    for row in rows:
        row["sha"] = sha256(root / row["path"])
    reserved = {r["sha"]: r["path"] for r in rows
                if "telegram" in r["path"].split("/") and r["skip"] is not None}

    blocked: list[dict] = []
    kept: list[dict] = []
    seen_twin: dict[tuple, str] = {}
    for row in rows:
        if row["skip"]:
            blocked.append(row)
            continue
        if row["sha"] in reserved and reserved[row["sha"]] != row["path"]:
            row["skip"] = f"duplicate of {reserved[row['sha']]}"
            blocked.append(row)
            continue
        twin = (row["size"], Path(row["path"]).name.lower())
        if twin in seen_twin:
            row["skip"] = f"duplicate of {seen_twin[twin]}"
            blocked.append(row)
            continue
        seen_twin[twin] = row["path"]
        if row["size"] > BOT_LIMIT:
            row["skip"] = f"over {BOT_LIMIT // 1_000_000} MB (Bot API limit)"
            blocked.append(row)
            continue
        kept.append(row)

    manifests: dict[str, list] = {"all": [], "official": []}
    for row in kept:
        path = Path(row["path"])
        bucket = "official" if row["subject"] == "00-University" else "all"
        item = {
            "file": row["path"],
            "subject": row["subject"],
            "title": path.stem,
            "kind": row["kind"],
            "display": fit_name(path.name),
            "_abs": str(root / row["path"]),
        }
        if row["subject"] in cards:
            item["catalog_link"] = f"https://t.me/c/{chat}/{cards[row['subject']]}"
        manifests[bucket].append(item)
        row["bucket"] = bucket

    for items in manifests.values():
        disambiguate(items)
    for row in kept:
        item = next(i for i in manifests[row["bucket"]] if i["file"] == row["path"])
        row["display"] = item["display"]
    for items in manifests.values():
        for item in items:
            item.pop("_abs", None)
    return manifests, rows


def report(manifests: dict, rows: list, out_dir: Path) -> None:
    """Print what would go and what would not — the honest half of the tool."""
    kept = [r for r in rows if not r["skip"]]
    for bucket, items in manifests.items():
        grid = defaultdict(lambda: [0, 0])
        for row in kept:
            if row.get("bucket") != bucket:
                continue
            cell = grid[(row["subject"], row["kind"])]
            cell[0] += 1
            cell[1] += row["size"]
        total = sum(r["size"] for r in kept if r.get("bucket") == bucket)
        print(f"=== {bucket.upper()}: {len(items)} files, {total / 1e6:.1f} MB ===")
        for (subject, kind), (count, size) in sorted(grid.items()):
            print(f"  {str(subject):26} {str(kind):8} {count:4} files "
                  f"{size / 1e6:8.1f} MB")

    print("=== NOT QUEUED ===")
    by_skip = defaultdict(lambda: [0, 0])
    for row in rows:
        if row["skip"]:
            key = row["skip"].split(" of ")[0]
            by_skip[key][0] += 1
            by_skip[key][1] += row["size"]
    for key, (count, size) in sorted(by_skip.items()):
        print(f"  {count:4} files {size / 1e6:8.1f} MB  {key}")

    renamed = [r for r in kept if r["display"] != Path(r["path"]).name]
    print(f"=== RENAMED FOR THE 62-BYTE BUDGET OR TO TELL FILES APART: "
          f"{len(renamed)} ===")
    for row in renamed:
        print(f"  {row['name_bytes']:3} -> {len(row['display'].encode('utf-8')):2} B  "
              f"{Path(row['path']).name[:40]:42} => {row['display']}")
    print("manifests ->",
          ", ".join(f"{name}.json ({len(items)})" for name, items in manifests.items()),
          "in", out_dir)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build the personal-library manifests from the vault.")
    parser.add_argument("--root", help="vault root (default: the repo this tool lives in)")
    parser.add_argument("--out-dir", help="where the manifests go "
                                          "(default: <root>/00_STUDIO_HUB/telegram/library)")
    parser.add_argument("--chat", default=DEFAULT_CHAT,
                        help=f"chat id for catalog links (default {DEFAULT_CHAT})")
    parser.add_argument("--json", action="store_true", help="print a JSON summary too")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve() if args.root else repo_root()
    out_dir = Path(args.out_dir) if args.out_dir else root / "00_STUDIO_HUB/telegram/library"
    if not (root / "01_Semester_1").is_dir():
        print(f"error: {root} does not look like the vault (no 01_Semester_1)",
              file=sys.stderr)
        return 2

    manifests, rows = scan(root, args.chat)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, items in manifests.items():
        (out_dir / f"{name}.json").write_text(
            json.dumps({"items": items}, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8")
    report(manifests, rows, out_dir)

    if args.json:
        kept = [r for r in rows if not r["skip"]]
        reasons: dict[str, dict] = {}
        for row in rows:
            if not row["skip"]:
                continue
            key = row["skip"].split(" of ")[0]
            cell = reasons.setdefault(key, {"files": 0, "mb": 0.0})
            cell["files"] += 1
            cell["mb"] = round(cell["mb"] + row["size"] / 1e6, 2)
        print(json.dumps({
            "manifests": {name: len(items) for name, items in manifests.items()},
            "queued": {"files": len(kept),
                       "mb": round(sum(r["size"] for r in kept) / 1e6, 2)},
            "not_queued": reasons,
        }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
