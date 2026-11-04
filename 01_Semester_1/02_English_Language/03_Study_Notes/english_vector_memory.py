#!/usr/bin/env python3
"""Build and query a tiny, fully local hybrid vector memory for English exercises.

Uses only Python's standard library and SQLite FTS5. Sparse TF-IDF vectors,
SQLite BM25, and Reciprocal Rank Fusion keep indexing and search CPU-light.
"""
from __future__ import annotations

import argparse
import html
from html.parser import HTMLParser
import json
import math
import re
import sqlite3
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUBJECT = HERE.parent
DB = HERE / "english_vector_memory.sqlite3"
SOURCES = [
    ("new_headway", "third_edition", "U01", "Unit_01_No_Place_Like_Home_Solutions.md", "md"),
    ("q_skills", "third_edition_metadata_check", "U01", "Unit_01_What_Makes_Someone_a_Hero_Solutions.md", "md"),
    ("q_skills", "first_edition_2011", "U02", "Unit_02_What_Makes_You_Want_to_Buy_Something_Solutions.md", "md"),
    ("new_headway", "third_edition", "U02", "NH_U2_Wide_Slides/NH_U2_Wide_Slides.html", "html"),
]
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z'-]{1,}|[\u0600-\u06ff]{2,}|\d+(?:\.\d+)?", re.UNICODE)
# Only grammatical function words. Pedagogical terms (listening, exercise, answer,
# page, unit, ...) stay searchable: they are exactly what a learner types.
STOP = set("the and for with from that this these those what when where which have has into about after before under over your their they them then than also each a an of to in is are was were be been being it its as at by or not on do does did you we i he she my our his her but if so up out".split())
ALIASES = {
    "listening": "استماع listen track audio", "grammar": "قواعد tense article passive", "vocabulary": "مفردات كلمات word meaning", "collocation": "تلازم لفظي تركيب كلمات collocations", "matching": "توصيل وصل match", "memorization": "حفظ احفظ حفظية", "class_discussion": "قاعة صف نقاش مشاركة pair speaking", "reading": "قراءة فهم نص comprehension", "writing": "كتابة موضوع انشاء essay", "pronunciation": "نطق stress rhythm صوت",
}
# The English exam does not test listening, long reading passages, writing or
# speaking. It tests grammar, vocabulary, collocations, matching and choices.
EXAM_SKILLS = {"grammar", "vocabulary", "collocation"}
EXAM_TASKS = {"matching", "multiple_choice"}

def clean_markup(text: str) -> str:
    text = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", text)
    text = re.sub(r"(?i)</(p|div|tr|li|h[1-6]|section|br|td|th)>|<br\s*/?>", "\n", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()

class Slides(HTMLParser):
    def __init__(self):
        super().__init__(); self.in_slide = False; self.depth = 0; self.buf = []; self.rows = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section" and "slide" in attrs.get("class", "").split():
            self.in_slide = True; self.depth = 1; self.buf = []
        elif self.in_slide and tag == "section": self.depth += 1
        if self.in_slide and tag in {"br", "p", "div", "tr", "li", "h1", "h2", "h3", "td", "th"}: self.buf.append(" ")
    def handle_endtag(self, tag):
        if not self.in_slide: return
        if tag == "section":
            self.depth -= 1
            if self.depth == 0:
                value = re.sub(r"\s+", " ", html.unescape(" ".join(self.buf))).strip()
                if value: self.rows.append(value)
                self.in_slide = False
        elif tag in {"p", "div", "tr", "li", "h1", "h2", "h3", "td", "th"}: self.buf.append(" ")
    def handle_data(self, data):
        if self.in_slide: self.buf.append(data)

def classify(title: str, text: str) -> dict:
    s = (title + " " + text[:220]).lower()
    tags = []
    rules = {
        "listening": r"listen|listening|track|t\d+\.\d+|audio|tapescript|استماع|السماع",
        "grammar": r"grammar|tense|article|relative clause|passive|verb|قواعد|الأدوات",
        "vocabulary": r"vocab|word list|glossary|meaning|word.?form|مفردات|كلمات",
        "collocation": r"collocation|make / do|make and do|توصيلات|كولوكيشن",
        "reading": r"reading|read the|main ideas|details|comprehension|قراءة",
        "writing": r"writing|essay|paragraph|outline|write a|كتابة|مقال",
        "speaking": r"speaking|discuss|discussion|talking about you|pair|نقاش|قاعة",
        "pronunciation": r"pronunciation|stress|rhythm|sounds|نطق",
        "everyday_english": r"everyday english|social expressions|exclamations",
        "study_skill": r"preview|annotat|highlight|peer review|study skill|outline",
    }
    for tag, pattern in rules.items():
        if re.search(pattern, s): tags.append(tag)
    task = []
    for tag, pattern in [("matching", r"match|matching|وصل|توصيل"),("gap_fill",r"gap|fill|complete|blank|فراغ"),("multiple_choice",r"multiple choice|choose|select"),("ordering",r"order|sequence|arrange|رتّب"),("true_false_correction",r"true|false|correct the|صحّح"),("model_response",r"model|sample answer|answers will vary|نموذج"),("free_response",r"discuss|personal|your own|write a|what do you think")]:
        if re.search(pattern, s): task.append(tag)
    learning = ["memorization"] if any(x in tags for x in ("vocabulary", "collocation", "pronunciation")) else []
    if any(x in tags for x in ("grammar", "reading", "study_skill")): learning.append("understanding")
    if task: learning.append("practice")
    if any(x in tags for x in ("writing", "speaking")): learning.append("production")
    mode = ["class_discussion"] if any(x in tags for x in ("speaking",)) else ["individual"]
    status = "model_only" if "model_response" in task or "free_response" in task else "source_solution"
    return {"skill": tags or ["general"], "task_type": task or ["exercise_cluster"], "learning_mode": list(dict.fromkeys(learning or ["understanding"])), "classroom_mode": mode, "answer_status": status}

MAX_CHUNK = 1800

def _row_to_text(line: str) -> str:
    """Flatten a markdown table row into readable text.

    Answer keys in these solution files live inside tables, so rows must be
    indexed rather than skipped.
    """
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    cells = [c for c in cells if c and not re.fullmatch(r":?-{2,}:?", c)]
    return " · ".join(cells)

def _split_body(title: str, body: str):
    body = re.sub(r"\s+", " ", body).strip()
    if not body:
        return []
    if len(body) <= MAX_CHUNK:
        return [(title, body)]
    parts, cur = [], ""
    for piece in re.split(r"(?<=[.!?؟])\s+", body):
        if cur and len(cur) + len(piece) + 1 > MAX_CHUNK:
            parts.append(cur); cur = piece
        else:
            cur = (cur + " " + piece).strip()
    if cur:
        parts.append(cur)
    return [(title if i == 0 else f"{title} (cont. {i + 1})", p) for i, p in enumerate(parts)]

def markdown_chunks(text: str):
    title = "document"
    buf = []
    out = []
    for line in text.splitlines():
        s = line.strip()
        m = re.match(r"^(#{1,4})\s+(.+)", s)
        if m:
            out.extend(_split_body(title, " ".join(buf)))
            title, buf = m.group(2).strip(), [m.group(2).strip()]
        elif s.startswith("---"):
            continue
        elif s.startswith("|"):
            row = _row_to_text(s)
            if row:
                buf.append(row)
        elif s:
            buf.append(s)
    out.extend(_split_body(title, " ".join(buf)))
    return out

def source_chunks():
    records = []
    for source, edition, unit, rel, kind in SOURCES:
        path = HERE / rel
        if not path.is_file(): raise FileNotFoundError(path)
        raw = path.read_text(encoding="utf-8", errors="replace")
        if kind == "md": chunks = list(markdown_chunks(raw))
        else:
            parser = Slides(); parser.feed(raw)
            chunks = []
            for i, body in enumerate(parser.rows, 1):
                title = (re.search(r"(?:^|\s)(\d{2})\s+(.{5,100}?)(?:\s+SB p|\s+الحل|$)", body) or [None, f"slide_{i:02d}", ""])[2].strip()
                chunks.append((f"slide {i:02d}: {title}", body))
        for i, (title, body) in enumerate(chunks, 1):
            if len(body) < 45: continue
            meta = classify(title, body)
            labels = " ".join(meta["skill"] + meta["task_type"] + meta["learning_mode"] + [source, unit, edition])
            expansion = " ".join(ALIASES.get(t, "") for t in meta["skill"])
            records.append({"source":source,"edition":edition,"unit":unit,"path":rel,"title":title,"ordinal":i,"content":body,"labels":labels+" "+expansion,"metadata":meta})
    return records

def terms(text: str) -> Counter:
    return Counter(t.lower() for t in TOKEN_RE.findall(text) if t.lower() not in STOP)

def build():
    records = source_chunks()
    dfs = Counter()
    for r in records: dfs.update(set(terms(r["title"]+" "+r["content"]+" "+r["labels"])))
    n = len(records)
    conn = sqlite3.connect(DB)
    conn.executescript("DROP TABLE IF EXISTS chunks; DROP TABLE IF EXISTS chunks_fts; CREATE TABLE chunks(id INTEGER PRIMARY KEY,source TEXT,edition TEXT,unit TEXT,path TEXT,title TEXT,ordinal INTEGER,content TEXT,labels TEXT,metadata TEXT,vector TEXT); CREATE VIRTUAL TABLE chunks_fts USING fts5(title,content,labels, tokenize='unicode61');")
    for r in records:
        counts=terms(r["title"]+" "+r["content"]+" "+r["labels"]); weights={}
        norm=math.sqrt(sum((tf*(math.log((n+1)/(dfs[t]+1))+1))**2 for t,tf in counts.items())) or 1
        for t,tf in counts.items(): weights[t]=round((tf*(math.log((n+1)/(dfs[t]+1))+1))/norm,7)
        cur=conn.execute("INSERT INTO chunks(source,edition,unit,path,title,ordinal,content,labels,metadata,vector) VALUES(?,?,?,?,?,?,?,?,?,?)",(r["source"],r["edition"],r["unit"],r["path"],r["title"],r["ordinal"],r["content"],r["labels"],json.dumps(r["metadata"],ensure_ascii=False),json.dumps(weights,ensure_ascii=False)))
        conn.execute("INSERT INTO chunks_fts(rowid,title,content,labels) VALUES(?,?,?,?)",(cur.lastrowid,r["title"],r["content"],r["labels"]))
    conn.execute("CREATE INDEX chunk_filter ON chunks(source,unit)"); conn.commit()
    print(f"Built {n} chunks from {len(SOURCES)} curated answer sources; SQLite FTS5 + sparse TF-IDF vectors; model downloads: 0")
    print("SQLite integrity:",conn.execute("PRAGMA integrity_check").fetchone()[0]); conn.close()

def search(query, top_k=8, source=None, unit=None, skill=None, exam=False):
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row
    where=[]; params=[]
    if source: where.append("source=?"); params.append(source)
    if unit: where.append("unit=?"); params.append(unit)
    sql="SELECT * FROM chunks"+(" WHERE "+" AND ".join(where) if where else "")
    rows=conn.execute(sql,params).fetchall()
    if skill:
        rows=[r for r in rows if skill in json.loads(r["metadata"])["skill"]]
    if exam:
        kept=[]
        for r in rows:
            m=json.loads(r["metadata"])
            if set(m["skill"]) & EXAM_SKILLS or set(m["task_type"]) & EXAM_TASKS:
                kept.append(r)
        rows=kept
    alias_text=ALIASES.get(skill,"") if skill else ""
    qterms=terms(query+" "+alias_text)
    if not qterms:
        conn.close()
        raise SystemExit("No searchable terms: every word in the query is a stop word or too short. Use a content word (e.g. listening, articles, collocation).")
    allow={r["id"] for r in rows}
    if not allow:
        conn.close(); print("No chunks match those filters."); return
    haystack={r["id"]:(r["title"]+" "+r["content"]+" "+r["labels"]).lower() for r in rows}

    # Rank list 3: IDF-weighted coverage of the query. Plain OR matching lets one
    # very common word dominate (e.g. a generic word like "exercises" outranking
    # the distinctive term the learner actually asked for).
    df={t:sum(1 for r in rows if t in haystack[r["id"]]) for t in qterms}
    idf={t:math.log((len(rows)+1)/(df[t]+1))+1 for t in qterms}
    tot_idf=3*sum(idf.values()) or 1
    coverage=[]
    for r in rows:
        head=r["title"].lower()
        hit=sum(idf[t]*(3 if t in head else 1) for t in qterms if t in haystack[r["id"]])
        if hit: coverage.append((hit/tot_idf,r["id"]))
    coverage_ids=[i for _,i in sorted(coverage,key=lambda x:(-x[0],x[1]))][:max(top_k*5,30)]

    qnorm=math.sqrt(sum(v*v for v in qterms.values())) or 1
    qvec={k:v/qnorm for k,v in qterms.items()}
    dense=[]
    for r in rows:
        vec=json.loads(r["vector"]); score=sum(v*vec.get(k,0) for k,v in qvec.items())
        if score>0: dense.append((score,r["id"]))
    dense_ids=[i for _,i in sorted(dense,reverse=True)[:max(top_k*5,30)]]

    query_terms=[t for t in qterms if len(t)>1]
    # Arabic definite article changes the FTS token, so "تمارين" would miss
    # "التمارين". Add the variant so both forms are searched.
    variants=[]
    for t in query_terms:
        variants.append(t)
        if re.match(r"[\u0600-\u06ff]", t):
            variants.append(t[2:] if t.startswith("ال") and len(t) > 4 else "ال"+t)
    fts_ids=[]
    if variants:
        match=" OR ".join('"'+v.replace('"','')+'"' for v in dict.fromkeys(variants))
        try:
            filters=" AND ".join(where)
            fsql="SELECT c.id FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH ?"+(" AND "+filters if filters else "")+" ORDER BY bm25(chunks_fts,4.0,1.0,2.5) LIMIT ?"
            fts_ids=[x[0] for x in conn.execute(fsql,[match,*params,max(top_k*5,30)]) if x[0] in allow]
        except sqlite3.OperationalError: pass
    if not (fts_ids or dense_ids or coverage_ids):
        conn.close(); print("No matching chunks."); return
    fused=Counter()
    for ranking in (fts_ids,dense_ids,coverage_ids):
        for rank,identity in enumerate(ranking,1): fused[identity]+=1/(60+rank)
    byid={r["id"]:r for r in rows}; out=0
    for identity,score in fused.most_common():
        r=byid.get(identity)
        if not r: continue
        m=json.loads(r["metadata"])
        print(f"{score:.5f} | {r['source']} {r['edition']} {r['unit']} | {','.join(m['skill'])} | {r['title']} | {r['path']}#{r['ordinal']}")
        print(re.sub(r"\s+"," ",r["content"])[:500]+"\n"); out+=1
        if out>=top_k: break
    conn.close()

def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    ap=argparse.ArgumentParser(description=__doc__); sub=ap.add_subparsers(dest="cmd",required=True)
    sub.add_parser("build")
    st=sub.add_parser("search"); st.add_argument("query"); st.add_argument("--top-k",type=int,default=8); st.add_argument("--source",choices=["new_headway","q_skills"]); st.add_argument("--unit",choices=["U01","U02"]); st.add_argument("--skill",choices=sorted(ALIASES)); st.add_argument("--exam",action="store_true",help="exam scope only: grammar/vocabulary/collocation plus matching and multiple-choice items")
    sub.add_parser("status")
    args=ap.parse_args()
    if args.cmd=="build": build()
    elif args.cmd=="status":
        if not DB.exists(): print("Index not built"); return
        c=sqlite3.connect(DB); print("chunks:",c.execute("select count(*) from chunks").fetchone()[0]); print("sources:",c.execute("select source,unit,count(*) from chunks group by source,unit").fetchall()); print("integrity:",c.execute("pragma integrity_check").fetchone()[0]); c.close()
    else:
        if not DB.exists(): raise SystemExit("Build the index first")
        search(args.query,args.top_k,args.source,args.unit,args.skill,args.exam)
if __name__=="__main__": main()
