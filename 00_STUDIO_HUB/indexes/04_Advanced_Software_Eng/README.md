# ASE Local Metadata Index

**Shared ASE work day · 2026-10-16 · prepared by Codex**

This is a small, rebuildable local search index for the Advanced Software Engineering subject. It uses Python's built-in `sqlite3` with FTS5; it downloads no models, uses no cloud service, and installs no packages.

## What it indexes

The scanner is pinned to `01_Semester_1/04_Advanced_Software_Eng` and walks files below that folder only. It records each file's relative path, filename-derived title, extension, size, modification time, heuristic category, and a chapter number when the path or filename contains a clear `Ch1` / `Chapter_1`-style marker. FTS5 searches relative paths, filename-derived titles, and manually curated keywords; the other fields stay as structured metadata for filtering and status reports.

It does **not** extract PDF, book, Word, PowerPoint, or other file contents. It does not duplicate textbook text. Search is lexical over paths, filenames/titles, and explicit keywords; it is not semantic search. Use `--chapter` to filter using the heuristic chapter metadata. If an answer needs source content, open the cited source and read the relevant pages separately.

Category and chapter labels inferred from folder names and filenames are heuristics, not verified subject metadata. `status` shows the unresolved chapter count. Files recognized as QA/build/cache artifacts are retained in `manifest.json` with `qa_only: true`, but are excluded from FTS search. Keyword entries should be added only after checking their source; their verification anchor is stored alongside them.

The first verified instructor-keyword entries cover **Lectures 1–3**. They are tied to the student's supplied vocabulary post (2026-09-16, 2026-09-23, and 2026-09-30) and associated with the matching publisher slide decks. The term post—not these heuristic chapter labels—is the authority for lecture scope. Later lecture terms have not yet been added to the index.

The reference-books folder contains two different books that must not be conflated. For Chapter 2, `CS_Agarwal_SW_Engineering_and_Testing_2010.pdf` is the selected course textbook: *Software Engineering & Testing: An Introduction*, B.B. Agarwal, S.P. Tayal, and M. Gupta, Jones & Bartlett, 2010. Chapter 3 follows its own source map: the companion slides identify K.K. Aggarwal and Yogesh Singh's *Software Engineering*, 3rd edition; `AliFahim_Software_Engineering.pdf` is a matching scanned book with missing cover/title page, so that bibliographic identity is high-confidence but not directly printed on the scan. Keep the two source families, chapter-specific precedence, question counts, and citations separate.

## Local semantic knowledge index

`ase_index.py` remains the lightweight lexical file/keyword index. It is **not** a vector database and does not extract source content. The separate `ase_vector_index.py` stores source-anchored bilingual text chunks and local embeddings in `ase_knowledge_vectors.sqlite3`. It uses the locally cached `intfloat/multilingual-e5-small` model; query and passage embeddings are computed on this machine. Source pages, slide numbers, and authority tier are stored with every chunk. No source text is sent to a cloud service.

`knowledge_sources.json` is the editable catalog for a **chapter-partitioned subject collection**. Each record has a chapter number, source class, authority, source location, and page/slide range. Chapter 2's catalog includes the B.B. Agarwal et al. 2010 text, separate K.K. Aggarwal & Singh sources, selective support books, lecture/study files, question banks, and OCR from 21 slide figures. Chapter 3 is now indexed with its instructor vocabulary, K.K. scan/spread range, 140-slide companion deck, the relevant B.B. 2010 section, and publisher exercise pages. The combined SQLite database holds 1,726 chunks: 1,430 for Chapter 2 and 296 for Chapter 3. Chapter 3 includes local OCR from all 50 scanned spreads at 180 dpi; the final mixed spread was clipped to printed p.138 to exclude Chapter 4 p.139. OCR remains a navigation aid and must be checked against the page image. The scan visually confirms textbook Exercise 3.25 on printed p.138, although the companion slides and compiled question PDF omit it; the full textbook exercise inventory is therefore 36, not 35. The source class lets agents filter `primary_book`, `supporting_book`, `course_study_note`, `question_bank`, `exam_example`, `course_archive_lecture`, `diagram_ocr`, and other source types separately.

The four `DUPLICATES_Review` / full-source 1,094-page slide files share SHA-256 `2bc72b3dc1e44057625a587408071b0eb7596c643103541e7b1957c0c471bd2f`. Their Chapter 2 slice at PDF pp. 82–129 has page-for-page identical extracted text to the 48-page chapter slide PDF. The index stores that chapter once; its mirror paths and evidence are recorded on the slide entry in `knowledge_sources.json`.

The scan's Chapter 2 spreads (local PDF pp. 16–25) are OCRed locally and carry a printed-spread locator. Chapter 3's scanned spreads (PDF pp. 26–75) have local OCR in the vector database; the final spread includes p.138 from Ch.3 and p.139 from Ch.4, so OCR was clipped to p.138 only. Searchable textbook pages and slide figures may also receive targeted visual OCR for labels. OCR is marked as OCR, may scramble Arabic or diagram layout, and must be checked against the image. No OCR text is represented as verified book wording merely because it is searchable.

The content policy follows the student's latest decision: the professor's vocabulary list defines the target scope. Add modest depth to clarify a term or fill a demonstrated gap. Do not combine every book or treat every source heading as exam scope. Use the chapter plan's source precedence and one best supporting source only for a gap; keep slide-only claims, student study notes, and external question banks visibly distinct. Dr. Ali Fahem's Chapter 2 and Chapter 3 lists (messages dated 2026-09-23 and 2026-09-30) are preserved in their chapter folders and indexed as `professor_vocabulary`; Chapter 3's detailed page-level source map remains in progress.

Search results are retrieval hints, not proof; open the cited page or slide before writing or checking an answer. Use the chapter and source-class filters to avoid mixing authority levels:

```powershell
python "90_Shared_Toolbox/tools/ase_vector_index.py" status
python "90_Shared_Toolbox/tools/ase_vector_index.py" build
python "90_Shared_Toolbox/tools/ase_vector_index.py" search "waterfall phases" --chapter 2 --category primary_book
python "90_Shared_Toolbox/tools/ase_vector_index.py" search "الفرق بين التطوير التطوري والتحسين التكراري" --chapter 2 --top-k 8
python "90_Shared_Toolbox/tools/ase_vector_index.py" search "spiral model" --chapter 2 --category supporting_book
```

To add another chapter later, append its source records to `knowledge_sources.json` with that chapter number, source class, and inspected page ranges, then rebuild. Do not place whole unrelated books or unrelated exam-bank pages into a chapter collection just because they exist in the vault.

## Commands

Run these from the Master-Studio root. They use the workspace's normal Python installation and require no extra packages.

```powershell
python "90_Shared_Toolbox/tools/ase_index.py" build
python "90_Shared_Toolbox/tools/ase_index.py" status
python "90_Shared_Toolbox/tools/ase_index.py" search "software crisis" --chapter 1
python "90_Shared_Toolbox/tools/ase_index.py" search "requirements" --chapter 3
```

Search terms are combined with AND. `--chapter` narrows the results. Searches return paths and metadata so agents can open the original file; they do not return excerpts.

## Updating verified keywords

The first build has no manually curated keywords. After verifying a term in a source, add it for that source file and rebuild:

```powershell
python "90_Shared_Toolbox/tools/ase_index.py" keywords add "02_Raw_Materials/Aggarwal_Singh_Slides/chapter_1_introduction.pdf" software-crisis "software failure" --source "Aggarwal Ch. 1 slides, verified pages 3-8"
python "90_Shared_Toolbox/tools/ase_index.py" build
```

Other keyword commands:

```powershell
python "90_Shared_Toolbox/tools/ase_index.py" keywords list
python "90_Shared_Toolbox/tools/ase_index.py" keywords show "02_Raw_Materials/Aggarwal_Singh_Slides/chapter_1_introduction.pdf"
python "90_Shared_Toolbox/tools/ase_index.py" keywords set "relative/path/to/source.pdf" term-one term-two --source "Book Ch. 1, p. 12"
python "90_Shared_Toolbox/tools/ase_index.py" keywords remove "relative/path/to/source.pdf" term-one
```

`keywords.json` is the small editable source of curated terms and verification anchors. `ase_index.sqlite3` and `manifest.json` are generated outputs; `build` safely replaces them from the current filesystem metadata and keyword list. No source files are changed.

## Agent handoff

OpenCode, WorkBuddy, Codex, and other local agents can use the same `build`, `status`, and `search` commands. Start with `status`; if the index is absent or stale, run `build`, then search by chapter and topic. Treat classifications as navigation hints, and treat Aggarwal's book as the content authority. Add source-verified keywords through the CLI so the index remains auditable and shared.
