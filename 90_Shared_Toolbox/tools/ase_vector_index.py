#!/usr/bin/env python3
"""Local bilingual semantic index for source-anchored ASE knowledge chunks.

The index stores selected PDF/Markdown passages and their provenance locally in
SQLite. Embeddings use multilingual-e5-small via Transformers; retrieval never
calls a hosted inference endpoint. The older ase_index.py stays metadata-only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import torch
import torch.nn.functional as F
from huggingface_hub import snapshot_download
from transformers import AutoModel, AutoTokenizer
import pymupdf


ROOT = Path(__file__).resolve().parents[2]
INDEX_DIR = ROOT / "00_STUDIO_HUB" / "indexes" / "04_Advanced_Software_Eng"
SOURCES_PATH = INDEX_DIR / "knowledge_sources.json"
DB_PATH = INDEX_DIR / "ase_knowledge_vectors.sqlite3"
MODEL_ID = "intfloat/multilingual-e5-small"
MODEL_REVISION = "614241f622f53c4eeff9890bdc4f31cfecc418b3"
MODEL_PATTERNS = [
    "config.json", "model.safetensors", "tokenizer.json",
    "tokenizer_config.json", "special_tokens_map.json",
    "sentencepiece.bpe.model",
]
MAX_CHARS = 1700
OVERLAP_CHARS = 180
BATCH_SIZE = 12


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def model_path() -> Path:
    return Path(snapshot_download(
        repo_id=MODEL_ID,
        revision=MODEL_REVISION,
        allow_patterns=MODEL_PATTERNS,
        local_files_only=True,
    ))


def load_encoder() -> tuple[Any, Any]:
    path = str(model_path())
    tokenizer = AutoTokenizer.from_pretrained(path, local_files_only=True)
    model = AutoModel.from_pretrained(path, local_files_only=True, use_safetensors=True)
    model.eval()
    model.to("cpu")
    return tokenizer, model


def encode(texts: list[str], tokenizer: Any, model: Any, prefix: str) -> np.ndarray:
    all_vectors: list[np.ndarray] = []
    with torch.inference_mode():
        for offset in range(0, len(texts), BATCH_SIZE):
            batch = [prefix + text for text in texts[offset:offset + BATCH_SIZE]]
            tokens = tokenizer(
                batch, padding=True, truncation=True, max_length=512,
                return_tensors="pt",
            )
            output = model(**tokens)
            mask = tokens["attention_mask"].unsqueeze(-1).to(output.last_hidden_state.dtype)
            pooled = (output.last_hidden_state * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1e-9)
            normalized = F.normalize(pooled, p=2, dim=1)
            all_vectors.append(normalized.cpu().numpy().astype(np.float32))
    return np.vstack(all_vectors) if all_vectors else np.empty((0, 384), dtype=np.float32)


def split_chunks(text: str, limit: int = MAX_CHARS) -> list[str]:
    cleaned = re.sub(r"\r\n?", "\n", text)
    cleaned = re.sub(r"[ \t]+", " ", cleaned)
    paras = [p.strip() for p in re.split(r"\n\s*\n", cleaned) if p.strip()]
    chunks: list[str] = []
    current = ""
    for para in paras:
        while len(para) > limit:
            if current:
                chunks.append(current.strip())
                current = ""
            cut = para.rfind(" ", 0, limit)
            if cut < limit // 2:
                cut = limit
            chunks.append(para[:cut].strip())
            para = para[max(0, cut - OVERLAP_CHARS):].strip()
        candidate = f"{current}\n\n{para}" if current else para
        if len(candidate) > limit and current:
            chunks.append(current.strip())
            current = para
        else:
            current = candidate
    if current.strip():
        chunks.append(current.strip())
    return chunks


def page_label(source: dict[str, Any], pdf_page: int) -> str:
    kind = source.get("page_kind", "PDF page")
    label = f"{kind} {pdf_page}"
    if source.get("printed_page_start") is not None:
        step = int(source.get("printed_page_step", 1))
        span = int(source.get("printed_page_span", 1))
        printed = int(source["printed_page_start"]) + (pdf_page - int(source["pdf_page_start"])) * step
        if span > 1:
            label += f"; printed pp. {printed}–{printed + span - 1}"
        else:
            label += f"; printed p. {printed}"
    return label


def _ocr_image(image_bytes: bytes, engine: Any) -> tuple[str, float | None]:
    result, _ = engine(image_bytes)
    if not result:
        return "", None
    lines: list[str] = []
    scores: list[float] = []
    for item in result:
        value = str(item[1]).strip()
        if value:
            lines.append(value)
            try:
                scores.append(float(item[2]))
            except (IndexError, TypeError, ValueError):
                pass
    return "\n".join(lines), (sum(scores) / len(scores) if scores else None)


def source_records(source: dict[str, Any], ocr_engine: Any = None) -> tuple[list[dict[str, Any]], int, int]:
    path = ROOT / source["path"]
    records: list[dict[str, Any]] = []
    pages_without_text = 0
    ocr_pages = 0
    if source["kind"] == "pdf":
        doc = pymupdf.open(path)
        start = int(source.get("pdf_page_start", 1))
        end = int(source.get("pdf_page_end", doc.page_count))
        if start < 1 or end < start or end > doc.page_count:
            raise ValueError(f"Invalid 1-based PDF range {start}-{end}: {path}")
        for pageno in range(start - 1, end):
            page = doc[pageno]
            text = page.get_text("text").strip()
            had_text_layer = bool(text)
            ocr_score = None
            did_ocr = False
            if source.get("page_terms_any") and (text or not source.get("ocr_scanned_pages")):
                terms = [str(term).casefold() for term in source["page_terms_any"]]
                if not any(term in text.casefold() for term in terms):
                    continue
            if not text:
                pages_without_text += 1
                if source.get("ocr_scanned_pages"):
                    if ocr_engine is None:
                        raise RuntimeError("OCR requested but RapidOCR engine is unavailable")
                    pix = page.get_pixmap(dpi=int(source.get("ocr_dpi", 200)), alpha=False)
                    text, ocr_score = _ocr_image(pix.tobytes("png"), ocr_engine)
                    if text:
                        ocr_pages += 1
                        did_ocr = True
                if not text:
                    continue
            elif source.get("ocr_visual_pages") is True or (source.get("ocr_visual_pages") and pageno + 1 in source["ocr_visual_pages"]):
                if ocr_engine is None:
                    raise RuntimeError("Visual OCR requested but RapidOCR engine is unavailable")
                pix = page.get_pixmap(dpi=int(source.get("ocr_dpi", 200)), alpha=False)
                visual_text, ocr_score = _ocr_image(pix.tobytes("png"), ocr_engine)
                if visual_text:
                    text += "\n\n[Visual OCR for labels embedded in diagrams; confirm from rendered page]\n" + visual_text
                    ocr_pages += 1
                    did_ocr = True
            for part, chunk in enumerate(split_chunks(text), 1):
                records.append({
                    "source_id": source["id"], "source_path": source["path"],
                    "source_title": source["title"], "source_kind": source.get("authority", "reference"),
                    "authority": source.get("authority", "reference"),
                    "chapter": str(source.get("chapter", "")),
                    "category": source.get("category", "uncategorized"),
                    "page_label": page_label(source, pageno + 1),
                    "chunk_part": part, "content": chunk,
                    "extraction": "PDF text + visual OCR (local; verify visually)" if did_ocr and had_text_layer else ("OCR (local; verify visually)" if did_ocr or ocr_score is not None else "PDF text layer"),
                    "ocr_mean_confidence": ocr_score,
                })
    elif source["kind"] == "image":
        if ocr_engine is None:
            raise RuntimeError("Image OCR requested but RapidOCR engine is unavailable")
        text, confidence = _ocr_image(path.read_bytes(), ocr_engine)
        if text:
            ocr_pages = 1
            records.append({
                "source_id": source["id"], "source_path": source["path"],
                "source_title": source["title"], "source_kind": source.get("authority", "reference"),
                "authority": source.get("authority", "reference"),
                "chapter": str(source.get("chapter", "")),
                "category": source.get("category", "uncategorized"),
                "page_label": source.get("page_label", "image OCR"), "chunk_part": 1,
                "content": text, "extraction": "OCR (local; verify visually)",
                "ocr_mean_confidence": confidence,
            })
    elif source["kind"] in {"markdown", "text"}:
        text = path.read_text(encoding="utf-8", errors="replace")
        sections = re.split(r"(?m)(?=^#{1,4}\s+)", text)
        for section_index, section in enumerate(sections, 1):
            for part, chunk in enumerate(split_chunks(section), 1):
                if len(chunk) < 40:
                    continue
                records.append({
                    "source_id": source["id"], "source_path": source["path"],
                    "source_title": source["title"], "source_kind": source.get("authority", "note"),
                    "authority": source.get("authority", "note"),
                    "chapter": str(source.get("chapter", "")),
                    "category": source.get("category", "uncategorized"),
                    "page_label": f"section {section_index}",
                    "chunk_part": part, "content": chunk,
                    "extraction": "source text", "ocr_mean_confidence": None,
                })
    else:
        raise ValueError(f"Unsupported source kind: {source['kind']}")

    for note in source.get("notes", []):
        content = str(note["content"]).strip()
        records.append({
            "source_id": source["id"], "source_path": source["path"],
            "source_title": note.get("title", source["title"]),
            "source_kind": source.get("authority", "note"),
            "authority": source.get("authority", "note"),
            "chapter": str(source.get("chapter", "")),
            "category": source.get("category", "uncategorized"),
            "page_label": note.get("page_label", "curated source map"),
            "chunk_part": 1, "content": content, "extraction": "curated note",
            "ocr_mean_confidence": None,
        })
    return records, pages_without_text, ocr_pages


def db_connect(path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA journal_mode=DELETE")
    conn.execute("PRAGMA synchronous=FULL")
    return conn


def build() -> None:
    config = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    sources = config["sources"]
    records: list[dict[str, Any]] = []
    source_report = []
    ocr_engine = None
    for source in sources:
        if source.get("include", True) is False:
            continue
        if source.get("ocr_scanned_pages") or source.get("ocr_visual_pages") or source["kind"] == "image":
            if ocr_engine is None:
                try:
                    from rapidocr_onnxruntime import RapidOCR
                except ImportError as exc:
                    raise RuntimeError("RapidOCR is required for configured scanned pages/figures") from exc
                ocr_engine = RapidOCR()
        made, no_text, ocr_pages = source_records(source, ocr_engine)
        records.extend(made)
        source_report.append({
            "id": source["id"], "path": source["path"],
            "chapter": str(source.get("chapter", "")),
            "category": source.get("category", "uncategorized"),
            "chunks": len(made), "pages_without_text_layer": no_text,
            "pages_ocr_extracted": ocr_pages,
        })
    if not records:
        raise RuntimeError("No source chunks were extracted")

    tokenizer, model = load_encoder()
    vectors = encode([r["content"] for r in records], tokenizer, model, "passage: ")
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix="ase_vectors_", suffix=".sqlite3", dir=INDEX_DIR)
    os.close(fd)
    Path(tmp_name).unlink(missing_ok=True)
    tmp_db = Path(tmp_name)
    try:
        conn = db_connect(tmp_db)
        conn.executescript("""
            CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
            CREATE TABLE chunks (
                id INTEGER PRIMARY KEY,
                source_id TEXT NOT NULL,
                source_path TEXT NOT NULL,
                source_title TEXT NOT NULL,
                source_kind TEXT NOT NULL,
                authority TEXT NOT NULL,
                chapter TEXT NOT NULL,
                category TEXT NOT NULL,
                page_label TEXT NOT NULL,
                chunk_part INTEGER NOT NULL,
                extraction TEXT NOT NULL,
                ocr_mean_confidence REAL,
                content TEXT NOT NULL,
                content_sha256 TEXT NOT NULL,
                embedding BLOB NOT NULL
            );
            CREATE INDEX chunks_source_idx ON chunks(source_id);
            CREATE VIRTUAL TABLE chunks_fts USING fts5(
                source_title, source_path, page_label, content,
                tokenize='unicode61 remove_diacritics 2'
            );
        """)
        for i, (record, vector) in enumerate(zip(records, vectors), 1):
            sha = hashlib.sha256(record["content"].encode("utf-8")).hexdigest()
            conn.execute(
                "INSERT INTO chunks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (i, record["source_id"], record["source_path"], record["source_title"],
                 record["source_kind"], record["authority"], record["chapter"],
                 record["category"], record["page_label"],
                 record["chunk_part"], record["extraction"], record["ocr_mean_confidence"],
                 record["content"], sha, vector.tobytes()),
            )
            conn.execute(
                "INSERT INTO chunks_fts(rowid,source_title,source_path,page_label,content) VALUES(?,?,?,?,?)",
                (i, record["source_title"], record["source_path"], record["page_label"], record["content"]),
            )
        metadata = {
            "built_at": utc_now(), "model_id": MODEL_ID, "model_revision": MODEL_REVISION,
            "embedding_dimension": str(vectors.shape[1]), "distance": "cosine (unit-normalized dot product)",
            "language_scope": "English and Arabic source text; local inference only",
            "sources": json.dumps(source_report, ensure_ascii=False),
            "chunk_count": str(len(records)),
        }
        conn.executemany("INSERT INTO metadata VALUES(?,?)", metadata.items())
        conn.commit()
        conn.close()
        tmp_db.replace(DB_PATH)
    except Exception:
        tmp_db.unlink(missing_ok=True)
        raise
    print(f"Built local semantic index: {DB_PATH}")
    print(f"Chunks: {len(records)}; embedding dimensions: {vectors.shape[1]}; model: {MODEL_ID}@{MODEL_REVISION}")
    for item in source_report:
        print(f"  {item['id']}: {item['chunks']} chunks; {item['pages_ocr_extracted']} pages OCRed; {item['pages_without_text_layer']} pages lacked a PDF text layer")


def status() -> None:
    if not DB_PATH.exists():
        print(f"Not built yet: {DB_PATH}")
        return
    conn = db_connect(DB_PATH)
    metadata = dict(conn.execute("SELECT key,value FROM metadata"))
    count = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    sources = conn.execute("SELECT source_id, COUNT(*) FROM chunks GROUP BY source_id ORDER BY source_id").fetchall()
    conn.close()
    print(f"Database: {DB_PATH}\nChunks: {count}\nModel: {metadata.get('model_id')}@{metadata.get('model_revision')}\nBuilt: {metadata.get('built_at')}")
    for source, n in sources:
        print(f"  {source}: {n}")


def search(query: str, top_k: int, chapter: str | None, category: str | None) -> None:
    if not DB_PATH.exists():
        raise RuntimeError("Build the index first")
    tokenizer, model = load_encoder()
    query_vector = encode([query], tokenizer, model, "query: ")[0]
    conn = db_connect(DB_PATH)
    where = []
    params: list[str] = []
    if chapter:
        where.append("chapter = ?")
        params.append(chapter)
    if category:
        where.append("category = ?")
        params.append(category)
    sql = "SELECT id,source_id,source_path,source_title,authority,chapter,category,page_label,extraction,ocr_mean_confidence,content,embedding FROM chunks"
    if where:
        sql += " WHERE " + " AND ".join(where)
    rows = conn.execute(sql, params).fetchall()
    fts_rows: set[int] = set()
    try:
        lexical = conn.execute(
            "SELECT rowid FROM chunks_fts WHERE chunks_fts MATCH ? LIMIT 100", (query,)
        ).fetchall()
        fts_rows = {row[0] for row in lexical}
    except sqlite3.OperationalError:
        pass
    conn.close()
    if not rows:
        print("No chunks match those chapter/category filters.")
        return
    vectors = np.vstack([np.frombuffer(row[11], dtype=np.float32) for row in rows])
    scores = vectors @ query_vector
    order = np.argsort(-scores)[:max(1, top_k)]
    for rank, idx in enumerate(order, 1):
        row = rows[int(idx)]
        bonus = " · lexical hit" if row[0] in fts_rows else ""
        excerpt = re.sub(r"\s+", " ", row[10])
        if len(excerpt) > 620:
            excerpt = excerpt[:617] + "..."
        print(f"{rank}. score={float(scores[idx]):.4f}{bonus}")
        print(f"   {row[3]} · {row[7]} · chapter {row[5]} · {row[6]} · {row[4]}")
        print(f"   {row[2]} [{row[0]}:{row[1]}] · {row[8]}" + (f" · OCR mean confidence {row[9]:.2f}" if row[9] is not None else ""))
        print(f"   {excerpt}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Local ASE bilingual semantic/vector index")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build", help="Build/rebuild the local SQLite vector index from the curated source manifest")
    sub.add_parser("status", help="Show indexed sources and model metadata")
    q = sub.add_parser("search", help="Search semantically using a local multilingual embedding model")
    q.add_argument("query")
    q.add_argument("--top-k", type=int, default=8)
    q.add_argument("--chapter", help="Limit semantic search to a chapter collection, e.g. 2")
    q.add_argument("--category", help="Limit search to a source class from knowledge_sources.json")
    args = parser.parse_args()
    try:
        if args.command == "build":
            build()
        elif args.command == "status":
            status()
        else:
            search(args.query, args.top_k, args.chapter, args.category)
    except Exception as exc:
        print(f"ase_vector_index: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
