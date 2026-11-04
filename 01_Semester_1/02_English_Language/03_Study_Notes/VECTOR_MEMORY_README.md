---
subject: "02_English_Language"
artifact: "English local vector memory"
updated: "2026-11-04"
---

# English Local Vector Memory

This subject has a small, local hybrid retrieval index for the four Unit 1–2 solution sources. It is deliberately CPU-light and self-contained: Python standard library + SQLite FTS5, with no model download, hosted API, vector database server, or third-party package.

## Retrieval design

1. **Exercise-sized chunks:** Markdown sections and individual New Headway Unit 2 slides remain separate, with source, edition, unit, title, and source path preserved. Sections longer than 1800 characters are split at sentence boundaries and marked `(cont. n)` so a single oversized section cannot drown the ranking.
2. **Tables are indexed.** Answer keys in these solution files are mostly markdown tables, so table rows are flattened into `cell · cell · cell` text and indexed instead of skipped. Before this fix, roughly half of each solution file was invisible to search.
3. **Multi-label metadata:** skill, task type, learning mode, classroom mode, and answer-evidence status are attached to each chunk. Arabic and English query aliases help retrieve common labels across both languages.
4. **Lexical ranking:** SQLite FTS5 ranks exact terms with BM25. This is useful for exercise IDs, grammar names, vocabulary, and quoted phrases.
5. **Sparse vector ranking:** each chunk has a normalized TF-IDF word vector stored as sparse JSON; cosine similarity is computed directly. For this compact collection exact comparison is simple and avoids ANN index overhead.
6. **Rank fusion:** Reciprocal Rank Fusion combines three ranked lists: BM25, sparse cosine, and an IDF-weighted coverage list (a chunk that contains the distinctive query terms ranks higher than one that only repeats a generic word; a title match counts triple).

This is a sparse vector memory, not a neural dense-embedding index. It intentionally spends almost no inference compute. Its semantic reach is weaker than a multilingual transformer, so use source/unit/skill filters and open the cited answer source before relying on a result.

## Behaviour guarantees

- A query with no searchable content word (only `the/of/and`, or a word that is not in the corpus at all) now **fails loudly** with `No searchable terms` / `No matching chunks`. Earlier it silently returned the last-inserted chunks with a plausible-looking score, which could be mistaken for a real hit.
- Stop words cover grammatical function words only. Pedagogical terms — `listening`, `exercise`, `answer`, `page`, `unit`, `read`, `write` — stay searchable, because they are what a learner actually types.
- Arabic queries expand the definite article, so `تمارين` also matches `التمارين`.
- Nothing is invented: every hit prints its source file and chunk ordinal, and the answer text itself is returned verbatim.

## Exam scope filter

The English exam tests **grammar, vocabulary, collocations, matching and multiple choice**. It does **not** test listening, long reading passages, writing, speaking, or verbatim memorization. Pass `--exam` to restrict retrieval to that scope, for example: `search "articles a an the" --exam`.

Scope membership: skill contains `grammar`, `vocabulary` or `collocation`, **or** task type is `matching` / `multiple_choice`. Of the 183 chunks, **62** fall inside this scope; the rest are listening (47), reading (44), writing (33) and speaking (29) material that is useful for the course but not for the exam. Use `--exam` for revision, omit it when checking a full exercise.

## Build and use

Run from the Master-Studio root:

```powershell
python "01_Semester_1/02_English_Language/03_Study_Notes/english_vector_memory.py" build
python "01_Semester_1/02_English_Language/03_Study_Notes/english_vector_memory.py" status
python "01_Semester_1/02_English_Language/03_Study_Notes/english_vector_memory.py" search "تمارين الاستماع" --source new_headway --unit U02 --skill listening
python "01_Semester_1/02_English_Language/03_Study_Notes/english_vector_memory.py" search "articles a an the" --source q_skills --unit U02 --skill grammar
```

The generated database is `english_vector_memory.sqlite3` in this folder. Rebuild after editing any of its four source artifacts. Search is local; it does not modify the source answers.

## Indexed sources

- New Headway Upper-Intermediate, Unit 1: `Unit_01_No_Place_Like_Home_Solutions.md`.
- New Headway Upper-Intermediate, Unit 2: `NH_U2_Wide_Slides/NH_U2_Wide_Slides.html` (the 59-slide source from which the companion PDF is rendered).
- Q: Skills for Success 4, Unit 1: `Unit_01_What_Makes_Someone_a_Hero_Solutions.md`.
- Q: Skills for Success 4, Unit 2: `Unit_02_What_Makes_You_Want_to_Buy_Something_Solutions.md`.

The detailed exercise labels, edition cautions, missing-audio notes, and answer-status limits are in `Exercise_Vector_Map.md`.

## Technical references

- SQLite, [FTS5 full-text search](https://www.sqlite.org/fts5.html) — built-in full-text index and BM25 ranking.
- Cormack, Clarke & Büttcher, [“Reciprocal Rank Fusion outperforms Condorcet and individual rank learning methods,” SIGIR 2009](https://doi.org/10.1145/1571941.1572114) — rank-list fusion method.
- Sentence Transformers, [Retrieve & Re-Rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) — describes lexical/dense candidate retrieval and why cross-encoder reranking costs more; this collection does not need that costly stage.

## Review log

**2026-11-04 — review and repair.** The first build indexed 161 chunks. Verification found three real defects, all fixed and re-tested:

| Defect | Evidence | Fix |
|:--|:--|:--|
| Table content never indexed | 1,472 words existed only inside markdown tables; 1,062 of them (72%) were absent from the index. These tables are the answer keys. | Table rows are flattened and indexed. Coverage of table-only vocabulary is now 100%. |
| Empty query returned fake hits | `search "listening"` and `search "zzzqqq"` produced identical output — the last chunks, with a plausible RRF score. Caused by stop-listing `listening` plus a zero-score dense list that still ranked. | Zero-score vectors are dropped; a query with no content word exits with a clear message. |
| Weak precision / recall | `تمارين الاستماع` returned a vocabulary appendix; Arabic `تمارين` missed `التمارين`. | Added IDF- and title-weighted coverage as a third RRF list, plus Arabic article expansion. |

Chunk count after the repair: **183** (New Headway U1 35, New Headway U2 59, Q: Skills U1 46, Q: Skills U2 43), `PRAGMA integrity_check = ok`.

Known limit that remains: a multi-word Arabic query whose first word is generic (e.g. `تمارين`) still ranks chunks that merely contain both words above the specific exercise. Use `--skill` and `--source`/`--unit` to constrain, and always open the cited chunk.
