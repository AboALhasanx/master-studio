#!/usr/bin/env python3
"""Local, metadata-only full-text index for Advanced Software Engineering.

The scanner is intentionally pinned to one subject directory. It reads paths
and filesystem metadata only; it never extracts PDF/Office/document contents.
Explicit keywords are maintained separately in the adjacent index directory.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SUBJECT_REL = Path("01_Semester_1") / "04_Advanced_Software_Eng"
SUBJECT_ROOT = PROJECT_ROOT / SUBJECT_REL
INDEX_DIR = PROJECT_ROOT / "00_STUDIO_HUB" / "indexes" / "04_Advanced_Software_Eng"
DB_PATH = INDEX_DIR / "ase_index.sqlite3"
KEYWORDS_PATH = INDEX_DIR / "keywords.json"
MANIFEST_PATH = INDEX_DIR / "manifest.json"

CHAPTER_RE = re.compile(
    r"(?i)(?:^|[^a-z0-9])(?:chapter|ch)[ _-]*0*(10|[1-9])(?:[^0-9]|$)"
)
QA_PARTS = {
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", "node_modules",
    "build", "dist", "cache", "caches", "qa", "qa_artifacts", "qa-artifacts",
    "leakscan", "leak_scan", "leak-scan",
}
QA_NAME_RE = re.compile(
    r"(?i)(?:^|[._ -])(?:leakscan|leak_scan|leak-scan|qa[-_ ]?(?:report|artifact|result|output)|"
    r"lint[-_ ]?(?:report|result|output)|test[-_ ]?(?:report|result|output)|coverage)(?:[._ -]|$)"
)
SKIP_DIRS = {".git", ".svn", ".hg"}


def utc_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(timespec="seconds")


def chapter_for(rel: Path) -> int | None:
    match = CHAPTER_RE.search(rel.as_posix())
    return int(match.group(1)) if match else None


def title_for(path: Path) -> str:
    stem = path.stem
    stem = re.sub(r"[_-]+", " ", stem)
    stem = re.sub(r"\s+", " ", stem).strip()
    return stem or path.name


def category_for(rel: Path, is_qa: bool) -> str:
    if is_qa:
        return "qa_only"
    parts = [p.lower() for p in rel.parts]
    if "02_raw_materials" in parts:
        return "raw_material"
    categories = {
        "03_study_notes": "study_note",
        "04_academic_papers": "academic_paper",
        "05_seminars_&_slides": "seminar_or_slides",
        "06_diagrams_&_mindmaps": "diagram_or_mindmap",
        "07_quizzes_&_anki": "quiz_or_flashcards",
        "08_academic_glossary": "glossary",
        "08_deepstudy_ch04": "deep_study",
        "08_deepstudy_ch05": "deep_study",
    }
    for part in parts:
        if part in categories:
            return categories[part]
    ext = rel.suffix.lower()
    if ext in {".md", ".txt", ".rst"}:
        return "text_or_document"
    if ext in {".pdf", ".ppt", ".pptx", ".doc", ".docx"}:
        return "document_or_slides"
    if ext in {".py", ".js", ".ts", ".json", ".html", ".css"}:
        return "code_or_data"
    return "other"


def is_qa_only(rel: Path) -> bool:
    if any(part.lower() in QA_PARTS for part in rel.parts[:-1]):
        return True
    return bool(QA_NAME_RE.search(rel.name))


def walk_subject() -> list[tuple[Path, Path]]:
    """Return (absolute, relative) regular files below the pinned subject root."""
    if not SUBJECT_ROOT.is_dir():
        raise RuntimeError(f"Subject directory not found: {SUBJECT_ROOT}")
    rows: list[tuple[Path, Path]] = []
    for current, dirs, files in os.walk(SUBJECT_ROOT, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d.lower() not in SKIP_DIRS)
        base = Path(current)
        for name in files:
            path = base / name
            try:
                if path.is_symlink() or not path.is_file():
                    continue
                rel = path.relative_to(SUBJECT_ROOT)
                rows.append((path, rel))
            except (OSError, ValueError):
                continue
    rows.sort(key=lambda pair: pair[1].as_posix().casefold())
    return rows


def read_keywords() -> dict[str, dict[str, object]]:
    if not KEYWORDS_PATH.exists():
        return {}
    try:
        data = json.loads(KEYWORDS_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Cannot read {KEYWORDS_PATH}: {exc}") from exc
    if not isinstance(data, dict):
        raise RuntimeError("keywords.json must be a JSON object keyed by subject-relative path")
    result: dict[str, dict[str, object]] = {}
    for key, value in data.items():
        if not isinstance(key, str):
            continue
        if isinstance(value, list):
            terms, source = value, "source not recorded (legacy entry)"
        elif isinstance(value, dict) and isinstance(value.get("terms", []), list):
            terms, source = value.get("terms", []), str(value.get("verified_from", "source not recorded"))
        else:
            continue
        result[key.replace("\\", "/")] = {
            "terms": sorted({str(term).strip() for term in terms if str(term).strip()}),
            "verified_from": source,
        }
    return result


def atomic_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def connect_db(path: Path = DB_PATH) -> sqlite3.Connection:
    try:
        conn = sqlite3.connect(path)
        conn.execute("CREATE VIRTUAL TABLE IF NOT EXISTS fts_probe USING fts5(value)")
        conn.execute("DROP TABLE fts_probe")
        return conn
    except sqlite3.OperationalError as exc:
        raise RuntimeError(f"This Python SQLite build needs FTS5 support: {exc}") from exc


def build() -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    keywords = read_keywords()
    scanned = walk_subject()
    tmp_fd, tmp_name = tempfile.mkstemp(prefix="ase_index_", suffix=".sqlite3", dir=INDEX_DIR)
    os.close(tmp_fd)
    tmp_db = Path(tmp_name)
    manifest_files: list[dict[str, object]] = []
    try:
        conn = connect_db(tmp_db)
        conn.executescript(
            """
            CREATE TABLE files (
                path TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                extension TEXT NOT NULL,
                size_bytes INTEGER NOT NULL,
                mtime_utc TEXT NOT NULL,
                category TEXT NOT NULL,
                chapter INTEGER,
                keywords TEXT NOT NULL,
                qa_only INTEGER NOT NULL CHECK (qa_only IN (0,1))
            );
            CREATE VIRTUAL TABLE file_search USING fts5(
                path, title, keywords,
                tokenize='unicode61 remove_diacritics 2'
            );
            CREATE INDEX files_chapter_idx ON files(chapter);
            CREATE INDEX files_category_idx ON files(category);
            """
        )
        records = []
        searchable = []
        for path, rel in scanned:
            rel_text = rel.as_posix()
            try:
                stat = path.stat()
            except OSError:
                continue
            title = title_for(path)
            chapter = chapter_for(rel)
            qa = is_qa_only(rel)
            category = category_for(rel, qa)
            terms = keywords.get(rel_text, {}).get("terms", [])
            if not isinstance(terms, list):
                terms = []
            row = (
                rel_text, title, path.suffix.lower(), stat.st_size,
                datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(timespec="seconds"),
                category, chapter, " ".join(terms), int(qa),
            )
            records.append(row)
            manifest_files.append({
                "path": rel_text, "title": title, "extension": path.suffix.lower(),
                "size_bytes": stat.st_size, "mtime_utc": row[4], "category": category,
                "chapter": chapter, "qa_only": qa,
            })
            if not qa:
                searchable.append((rel_text, title, " ".join(terms)))
        conn.executemany("INSERT INTO files VALUES (?,?,?,?,?,?,?,?,?)", records)
        conn.executemany("INSERT INTO file_search VALUES (?,?,?)", searchable)
        conn.commit()
        conn.close()
        os.replace(tmp_db, DB_PATH)
        atomic_json(MANIFEST_PATH, {
            "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "subject_root": SUBJECT_REL.as_posix(),
            "scanner_scope": "files below subject root only; metadata and explicit keywords only",
            "files": manifest_files,
        })
    except Exception:
        try:
            tmp_db.unlink(missing_ok=True)
        except OSError:
            pass
        raise
    print(f"Built metadata index: {DB_PATH}")
    print(f"Scanned {len(manifest_files)} files ({sum(1 for x in manifest_files if not x['qa_only'])} searchable, "
          f"{sum(1 for x in manifest_files if x['qa_only'])} QA-only).")


def status() -> None:
    if not DB_PATH.exists():
        print(f"Index not built yet: {DB_PATH}")
        return
    conn = connect_db()
    total, qa = conn.execute("SELECT COUNT(*), COALESCE(SUM(qa_only),0) FROM files").fetchone()
    print(f"Database: {DB_PATH}")
    print(f"Scope: {SUBJECT_REL.as_posix()}")
    print(f"Files: {total} total; {total - qa} searchable; {qa} QA-only")
    print("Categories:")
    for name, count in conn.execute("SELECT category, COUNT(*) FROM files GROUP BY category ORDER BY category"):
        print(f"  {name}: {count}")
    print("Chapters (heuristic from path/name; '?' means not identified):")
    for chapter, count in conn.execute("SELECT chapter, COUNT(*) FROM files GROUP BY chapter ORDER BY chapter"):
        label = f"Ch{chapter:02d}" if chapter is not None else "?"
        print(f"  {label}: {count}")
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        print(f"Manifest: {MANIFEST_PATH} ({manifest.get('generated_at_utc', 'unknown build time')})")
    except (OSError, json.JSONDecodeError):
        print("Manifest: missing or unreadable")
    conn.close()


def search(query: str, chapter: int | None, limit: int) -> None:
    if not DB_PATH.exists():
        raise RuntimeError("Index not built; run the build command first")
    tokens = [word for word in query.split() if word]
    if not tokens:
        raise RuntimeError("Search query is empty")
    match = " AND ".join('"' + token.replace('"', '""') + '"' for token in tokens)
    conn = connect_db()
    sql = """
        SELECT f.path, f.title, f.chapter, f.category, f.extension, f.size_bytes, f.mtime_utc
        FROM file_search s JOIN files f ON f.path=s.path
        WHERE file_search MATCH ? AND f.qa_only=0
    """
    args: list[object] = [match]
    if chapter is not None:
        sql += " AND f.chapter=?"
        args.append(chapter)
    sql += " ORDER BY rank LIMIT ?"
    args.append(max(1, min(limit, 100)))
    rows = conn.execute(sql, args).fetchall()
    if not rows:
        print("No matches. Search covers path/title/category and explicitly curated keywords only.")
    for path, title, ch, category, ext, size, mtime in rows:
        c = f"Ch{ch:02d}" if ch is not None else "chapter unknown"
        print(f"{c} | {category} | {ext or '[no extension]'} | {size} B | {mtime}\n  {title}\n  {path}")
    print(f"Results: {len(rows)}")
    conn.close()


def safe_rel_path(value: str) -> str:
    path = Path(value.replace("\\", "/"))
    if path.is_absolute() or ".." in path.parts:
        raise RuntimeError("Use a subject-relative path without '..'")
    rel = path.as_posix()
    candidate = SUBJECT_ROOT / Path(rel)
    try:
        candidate.resolve().relative_to(SUBJECT_ROOT.resolve())
    except ValueError as exc:
        raise RuntimeError("Path must stay inside the ASE subject folder") from exc
    return rel


def keyword_command(action: str, path_value: str | None, terms: list[str] | None,
                    source: str | None) -> None:
    current = read_keywords()
    if action == "list":
        if not current:
            print("No curated keywords yet. Add only terms verified against a source.")
        for path, values in sorted(current.items()):
            print(f"{path}: {', '.join(values['terms'])} | verified from: {values['verified_from']}")
        return
    if not path_value:
        raise RuntimeError("A subject-relative file path is required")
    rel = safe_rel_path(path_value)
    if action == "show":
        record = current.get(rel, {"terms": [], "verified_from": "not recorded"})
        print(f"{rel}: {', '.join(record['terms']) or '(no curated keywords)'} | verified from: {record['verified_from']}")
        return
    values = [t.strip() for t in (terms or []) if t.strip()]
    record = current.get(rel, {"terms": [], "verified_from": "not recorded"})
    existing = list(record["terms"])
    if action == "set":
        if not source:
            raise RuntimeError("set requires --source with a page, slide, exercise, or other verification anchor")
        current[rel] = {"terms": sorted(set(values)), "verified_from": source}
    elif action == "add":
        if not source:
            raise RuntimeError("add requires --source with a page, slide, exercise, or other verification anchor")
        current[rel] = {"terms": sorted(set(existing + values)), "verified_from": source}
    elif action == "remove":
        remove = set(values)
        current[rel] = {"terms": [term for term in existing if term not in remove],
                        "verified_from": str(record["verified_from"])}
    atomic_json(KEYWORDS_PATH, current)
    print(f"Updated {KEYWORDS_PATH} for {rel}. Run `ase_index.py build` to refresh FTS5.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Metadata-only local ASE file index (SQLite FTS5)")
    subs = parser.add_subparsers(dest="command", required=True)
    subs.add_parser("build", help="Rebuild index from metadata below the ASE subject directory")
    subs.add_parser("status", help="Show indexed file counts and heuristic coverage")
    p_search = subs.add_parser("search", help="Search filenames/titles and curated keywords")
    p_search.add_argument("query", help="Terms are ANDed; quoted phrases are not required")
    p_search.add_argument("--chapter", type=int, choices=range(1, 11))
    p_search.add_argument("--limit", type=int, default=20)
    p_kw = subs.add_parser("keywords", help="Manage source-verified keywords; then rebuild")
    p_kw.add_argument("action", choices=["list", "show", "set", "add", "remove"])
    p_kw.add_argument("path", nargs="?", help="Path relative to the ASE subject folder")
    p_kw.add_argument("terms", nargs="*", help="Curated terms; never copied from full source text")
    p_kw.add_argument("--source", help="Verification anchor for set/add, e.g. 'Aggarwal Ch.1, p. 12'")
    args = parser.parse_args()
    try:
        if args.command == "build":
            build()
        elif args.command == "status":
            status()
        elif args.command == "search":
            search(args.query, args.chapter, args.limit)
        else:
            keyword_command(args.action, args.path, args.terms, args.source)
    except (RuntimeError, sqlite3.Error, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
