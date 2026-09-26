---
current_semester: "Semester 1 (Fall 2026)"
active_week: 2
active_subject: "02_English_Language"
active_subject_code: "CS502"
immediate_todo: "English (CS502) - explain-a-paper assignment. SELECTED (documented, DOI): Christakis & Fowler, 'Social Network Sensors for Early Detection of Contagious Outbreaks', PLOS ONE 5(9):e12948 (2010), 8 pp, DOI 10.1371/journal.pone.0012948, free PDF in 02_Raw_Materials. Next: build the student's explanation/summary + presentation."
next_session_focus: "English (CS502) - produce the paper-explanation deliverable for 'Social Network Sensors for Early Detection of Contagious Outbreaks' (PLOS ONE 2010): structured summary, key-contribution analysis, and a short spoken presentation outline."
last_updated: "2026-09-26"
status: "ENGLISH_PAPER_ASSIGNMENT_ACTIVE"
---

# Master Studio: Active Session State

> **Purpose:** Fast-boot runtime state file. Agents read this file at session start to restore context in $< 50$ tokens.

```
+-------------------------------------------------------------------------------+
|                            FAST-BOOT CURRENT POINTER                          |
|                                                                               |
|  Semester: Semester 1 (Fall 2026)      Active Week: Week 02                   |
|  Subject:  02_English_Language  Target Path: 01_Semester_1/02_English_Language      |
|  Status:  QUIZ ARCHITECTURE V2 COMPLETE  Date: 2026-09-26                       |
+-------------------------------------------------------------------------------+
```

## 1. Current Session Context

| Key | Current Value | Notes / Description |
|:---|:---|:---|
| **Current Semester** | `Semester 1 (Fall 2026)` | First Course / Preparatory Coursework Phase |
| **Active Week** | `2` | ASE Week 02 complete (10 units + merged Master Lecture) |
| **Active Subject** | `02_English_Language` | Asst. Prof. Dr. Haidar Akab Alwan (1 Credit Hour) — CS502 |
| **Last Updated** | `2026-09-25` | Data Mining Feature Selection COMPLETE (source report + 24-page ملزمة + V1/V2 seminar decks). AI opened: AIMA 4th ed. verified + Week-01 lecture identified; Lecture-01 ملزمة ready to start. |

---

## 2. Immediate Tasks & Roadmap

### Active Work Queue
- [x] **Industrial-Grade Quiz Ingestion, Packaging & Offline Sync Architecture DONE (2026-09-26).** Canonical Schema v2 deployed across all 6 active subjects; `quiz_balancer.py` upgraded with `normalize_quiz_schema()` & `validate_schema_v2()`; `GET /api/quiz/bundle` & `pack_quiz_bundle.py` implemented; native IndexedDB `QuizVault` engine deployed in `quiz-vault.js` with zero dependencies; smart multi-file & bundle importer in `quiz.html`/`quiz.js` with dynamic catalog DOM injection & `"مستورد محلياً"` badges; write-ahead offline queue & auto-flushing sync; PWA bumped to `master-studio-v10`; native signed APK built (`MSCQuiz_Signed.apk`, 422.8 KB) via `build_mscquiz_apk.py` and 100% verified on physical tablet via ADB; Telegram direct-open intent & Web Share Target verified; 99/99 tests passing.
- [x] **ASE Week 02 Units 01–05 — zero-leakage cleanup + vector diagrams + clean bilingual PDFs (2026-09-24).** All backend scaffolding was stripped from student-facing text in Units 02–05 (`File NN of 10` cross-references, `[THIN]` flags, `**EN.**`/`**AR.**` markers, `BUILD_PLAN` build footers, the `file:` frontmatter key). `[THIN]` coverage notes were **rewritten as prose** (`ملاحظة تغطية:` / `Coverage note`) rather than deleted, so no information was lost. Unit 05 gained frontmatter, a **Where this sits** narrative spine, an English Feynman intuition section and a closing footer — it previously had none. Four new 2x-retina vector diagrams were built (waterfall classical vs iterative; prototyping vs evolutionary; incremental interleaving; RAD timeline compression), each inlined with an Arabic "how to read this figure" table. New tool: `90_Shared_Toolbox/tools/diagram_forge.py` (HTML/SVG → 2x PNG via Playwright; resolves `chromium-*/chrome-win64/chrome.exe`). PDFs re-exported with `study_pack` + `--lang ar`: **01 = 17 pp, 02 = 24 pp, 03 = 20 pp, 04 = 18 pp, 05 = 10 pp** — all verified with **zero leakage**, one embedded figure each, Arabic layer intact. Superseded exports moved to `99_Archives/2026-09-24_ASE_W02_superseded_exports/` (gitignored). Pushed as commits `7787ab1`, `8ba5bf2`.
- [x] **ASE Week 02 Units 06–10 — clean manifesto rebuild DONE (2026-09-24).** Zero-leakage, one diagram each, frontmatter + the 4-part "Where this sits" spine added; page counts **06 = 13, 07 = 11, 08 = 15, 09 = 11, 10 = 29**. Unit 10 carried a §2.5-before-§2 ordering bug, caught only by rendering and fixed. Committed `c8b9206`.
- [x] **ASE Week 02 MASTER LECTURE — ten units merged into one paginated booklet DONE (2026-09-24).** `08_PDF_Exports/Week_02_Master_Lecture.pdf` — **146 pages**: cover (p1) + index of topics/sub-topics/branches with **confirmed page numbers** (pp2–7) + the ten units with **continuous re-numbered pagination**. Builder `90_Shared_Toolbox/tools/build_week02_master.py` (two-pass measure→re-render). Verified **0 pagination mismatches**; unit starts at pages **[7, 21, 41, 57, 70, 78, 88, 96, 108, 118]**. One known blemish left by request: Unit 08's "Source notes" index line renders `p.000`.
- [ ] **`03_Data_Mining` — NOW THE ACTIVE SUBJECT.** W01–W03 notes exist in `03_Study_Notes/`. Next lecture topic: **Feature Selection Techniques** (professor-provided sources). Record only until the student directs study.
- [x] **Ingest 4 Canonical Textbooks for `04_Advanced_Software_Eng`** (Sommerville, Pressman, Mall, Agarwal)
- [x] **Synthesize Week 01 Lecture 01 Master Study Note** (33.9 KB Markdown, DOCX for OnlyOffice)
- [x] **Generate & Compile Lecture 01 Marp Seminar Deck** (10 slides, PDF + PPTX for OnlyOffice)
- [x] **Ingest Scanned Materials & Synthesize Unit 01 for `02_English_Language`** (Grammar & Tenses Study Note, Clean DOCX, Quiz Bank)
- [x] **Interactive WebUI Quiz Subsystem Deployed** — Flask web app with Study Mode (recitation) & Exam Mode (simulated exam), question & option shuffle, custom floating reason picker, multi-semester discovery, and telemetry sync into session journals.
- [x] **Complete New Headway Unit 1 "No place like home" (SB pp.6–15)** — full walkthrough, TB-verified (ISBN 978-0-19-439300-3), + Exam Index
- [x] **Establish agent identity (Koko) + student profile** — `SOUL.md` / `IDENTITY.md` / `USER.md`
- [x] **Decode Dr. Huda's exam method + build `01_Cyber_Security` Week 01 master note & question bank**
- [x] **Build the 6-subject inventory + rolling `STUDY_PLAN.md`**
- [x] **Put `06_Artificial_Intelligence` on hold** — the professor has delivered no material
- [x] **Correct `COLLEGE_BUDDY.md`** — removed two agent-inferred fake deadlines
- [x] **Add the external free-chatbot ingestion guide to `README.md`** (Gitingest, with measured digest sizes)
- [x] **`01_Cyber_Security` Week 01 — all theory Topics 1–6 covered** (master note + question bank + formula deep-dives); Chapter 7 excluded by the doctor
- [x] **`01_Cyber_Security` Week 02 Risk — bilingual concept outline delivered** — `03_Study_Notes/W02_Concept_Outline.md` (570 lines, 24 sections, EN concept + AR explanation). Full coverage of the booklet; formula card (`S = F × K`, `R = S / M`); terminology table; 8 `[VERIFY]` flags; 10 Week 01 closed-book recall prompts; exam-method mapping. **Two blockers found:** the delivered DOCX has **zero images** (all figures referenced but absent) and the **formula operators are missing** from the text layer.
- [x] **`01_Cyber_Security` Week 02 Risk — exam-focus sheet delivered (lecture-driven)** — `03_Study_Notes/W02_Exam_Focus.md`. Built from the **doctor's own 30 highlight runs + 27 coloured runs** recovered from the DOCX (my first pass had missed the formatting layer entirely) plus the student's 2026-09-23 lecture report. Contains the emphasis map, all numbered sets with counts, the acronym table, the two equations with a comparison table, the "influencing factors" answer, per-item verdicts, and the coverage boundary. **5 open items flagged for the student — none resolved silently.**
- [x] **`01_Cyber_Security` Week 02 Risk — SOURCE IDENTIFIED + fact-checked** — the booklet is a direct extraction of **Sharp, R., "Risk", in *Introduction to Cybersecurity: A Multidisciplinary Challenge*, Springer, 2024, pp. 37–56** ([DOI 10.1007/978-3-031-41463-3_3](https://doi.org/10.1007/978-3-031-41463-3_3)). Verification report: `03_Study_Notes/W02_Source_Verify.md`. **Two verified factual errors in the booklet:** (1) the "ISO/IEC 27002 **2022** … 14 categories" line — the 14 categories are the **2013** structure, 2022 is **4 themes / 93 controls** (and Dr. Huda highlighted this line yellow); (2) **"OCTAVE FORTE" does not exist** — only three public OCTAVE methodologies. Plus "Inheritance" → **Inherence**. Chapter body is paywalled, so Sharp's exact equation letters remain unverified.
- [x] **`01_Cyber_Security` Week 02 Risk — equations verified mathematically** — `03_Study_Notes/W02_Formulas.md`. `S = F × K` proven sound (multiplication required, not addition). `R = S / M` proven sound **only on `M ≥ 1`** — at `M = 0` it divides by zero and for `0 < M < 1` it gives residual risk greater than inherent risk, so **`M` is a protective factor, not a count** (which is why the booklet's "number *and* effectiveness" wording is necessary). Substituting `M = 1/(1 − CE)` collapses it to the industry-standard `R = S(1 − CE)` — **the division form is the mainstream model re-parameterised**. The student's reported `f = s·k` / `f = s/n` (n = threats) **fails a logical contradiction test**. Chapter PDF remains paywalled — page images could not be obtained.
- [x] **`01_Cyber_Security` Week 02 Risk — CLEAN BOOKLET delivered** — `03_Study_Notes/W02_Risks_Basic.pdf` (**34 pages**, English only, 27 sections, 6 embedded figures, contents page with real page numbers). Built from the original book + the doctor's marking, with every correction carried in a "Corrected" box. Builder: `90_Shared_Toolbox/tools/build_cyber_w02_booklet.py`; page numbering via the new `booklet_postprocess.py`. **This is now the primary revision document for the Cyber quiz.**
- [x] **`01_Cyber_Security` — 2-page EXAM SHEET delivered** — `03_Study_Notes/Cyber_Exam_Sheet.pdf`. **Covers BOTH booklets** (the postponed quiz tests both): page 1 Week 01 (Ch. 1–6, six equations, CIA triad with bracketed techniques, domain weights, Ch. 7 exclusion); page 2 Week 02 Risk (two equations, both matrices, the five lists, 13 traps, corrected facts). English, print-ready. Builder: `90_Shared_Toolbox/tools/build_cyber_exam_sheet.py`. **This is the last-minute revision document.**
- [x] **Master Studio Academic PDF Publishing Engine Operational** — Built `90_Shared_Toolbox/tools/pdf_exporter.py` powered by Playwright Headless Chromium (DirectWrite/HarfBuzz). Resolves the long-standing agent PDF generation problem: native Arabic connected cursive typography, pristine KaTeX math isolation, inlined vector diagrams, attribute-aware table cell LTR formatting (`dir="ltr"`, `white-space: nowrap`), Windows file-lock detection (safe fallback to `_new.pdf`), and 4 academic presets (`study_pack`, `booklet`, `exam_sheet`, `glossary`). Verified on ASE Lecture 01 (8pp) and Cyber Security Week 01 (11pp). Batch wrapper `export-pdf.bat`, agent skill `pdf-exporter`, and full SOP guide `00_STUDIO_HUB/guides/PDF_PUBLISHING_SOP.md` active.
- [x] **`04_Advanced_Software_Eng` Week 02 — deep term analysis delivered** — `03_Study_Notes/Week_02_SDLC_Terms_Deep_Analysis.md`. **Key finding: Mall chapter 2 (pp.73–135) is the PRIMARY source for this lecture, not Sommerville** — Sommerville has **0 hits** for Build & Fix, **0 relevant hits** for RAD, and no V-Model or named Evolutionary model. Sommerville is the secondary (best on process theory, waterfall's critique, incremental's benefits/problems, the spiral's sectors, and the agile manifesto). Pressman is the weakest fit; Agarwal mostly restates Sommerville. Also recovered **Mall's exercise set (pp.130–131)** — exam-shaped questions covering every lecture term, including Q54 which is a full paper on RAD alone. **No lecture slides exist for W02 — the term list came from the student's report, so the mapping is an inference (recorded as such).**
- [x] **`04_Advanced_Software_Eng` Week 02 — study plan + methodology report delivered** — `03_Study_Notes/Week_02_Study_Plan_and_Index.md`. Answers the student's question about his proposed workflow (index → numbered per-topic files → merge). **Verdict: structure agreed, one part disagreed.** The evidence (IJERT 2026, DOI 10.5281/zenodo.20522459) shows AI-summary study produces **higher confidence and lower scores**, with the gap widest on **analytical** questions — exactly where Dr. Ali Fahim grades. So four requirements are now built into every file: a **retrieval set with answers withheld**, **page anchors**, **`[THIN]` flags**, and the merged document reserved for review rather than first contact. **Ten-file build plan included, awaiting the student's answers to four questions before writing file 01.**
- [ ] **`04_Advanced_Software_Eng` Week 02 — the ten topic files are NOT yet written.** Blocked on: retrieval-set format, language (English-only vs English+Arabic), and starting order.
- [x] **`04_Advanced_Software_Eng` Week 02 — BUILD PLAN locked + File 01 written.** Plan: `03_Study_Notes/Week_02_BUILD_PLAN.md` (**the binding commitment document — open it before every ASE Week 02 session**; it carries the narrative spine, per-file detail, ten binding rules, the file template, and a progress table). File 01: `03_Study_Notes/Week_02_File_01_SDLC_Fundamentals.md` — English exposition + Arabic explanation, page-anchored, with the retrieval set **Q and A together** per the student's change. **The spine: requirements always change; every model is an answer to that one problem.** Files 02–10 not started; merge only after all ten exist.
- [ ] **`01_Cyber_Security` daily quiz** — postponed; covers two booklets. Exact date not confirmed. **Still open: the identity of the booklet's second source (physical-security / NIST half).**
- [x] **`03_Data_Mining` Week 02 comprehensive note built** — `03_Study_Notes/Week_02_Data_Types_and_Preparation.md` (lecture text preserved + Gemini frameworks + Dr. Ahmed formula layer + 50-question bank)
- [x] **`03_Data_Mining` Week 03 comprehensive note built** — `03_Study_Notes/Week_03_Feature_Extraction_and_Portability.md` (feature extraction + portability matrix + similarity graph + ~35Q; cross-linked to Week 02)
- [x] **`03_Data_Mining` — Monday delivered Feature Extraction and Portability content** — note and logical/mathematical audit are in the vault. **Week numbering remains subject to doctor confirmation; Weeks 01–03 have study notes.**
- [x] **Answer Dr. Ahmed Shakir's Week 02 question** — *"what is the data type of a URL?"* → **Nominal** (recorded in Week 02 comprehensive note §1.2)
- [ ] English research-paper presentation — deferred by student; not an active focus now.
- [x] **`05_Soft_Computing` official syllabus synced from alaidi.net** — course window 8/9/2026–**8/12/2026**; Midterm **20/10/2026 Weeks 1–6 fuzzy** (provisional — doctor may renumber); chain codes/ANFIS are NOT official weekly topics this term
- [x] **`05_Soft_Computing` Week 01 comprehensive note REBUILT** — `03_Study_Notes/Week_01_Introduction_to_Soft_Computing.md` in Data Mining method (full lecture text + Arabic conceptual layer + decoded images + long doctor answers + 35Q bank). **Not AI-slop compression.**
- [x] **`05_Soft_Computing` Week 2 source staged + local OCR** — PDF pages 1–66 only; searchable OCR at `02_Raw_Materials/W02_Fuzzy_Logic_Systems_OCR.md`; equations still require source-PDF validation
- [x] **`05_Soft_Computing` Week 02 FINAL BOOKLET delivered** — `03_Study_Notes/w02-fuzzy-logic-systems-booklet.{html,pdf}` (**29pp = cover + 28 sections, this is the canonical version — student decided to keep one-topic-per-page**, English, MathJax). Math from `W02_Fuzzy_Math_Vision_Verified.md`; LaTeX-escape corruption repaired; **Cartesian-product bridge corrected to "ambient space, not the set"**; source-verified against pp. 33/59/60/65/66 page images. A shorter mobile edition would be a separate artefact, not a replacement.
- [x] **`05_Soft_Computing` Week 02 QUIZ BANK delivered** — `07_Quizzes_&_Anki/Quiz_02_Fuzzy_Logic_Systems.json` (12 bilingual scenario MCQs). Balanced 3/3/3/3, **passed `quiz_balancer.py --strict` (100%)**, all keys semantically re-verified. Q12 rewritten after external review to state the precise Cartesian-product relationship.
- [ ] **`06_Artificial_Intelligence`** — Tuesday lecture did not take place because the dean had other commitments; lecture postponed to Sunday. No material reported; do not proactively check the group.

### Next Session Focus
- **ASE Week 02 is COMPLETE** — ten unit PDFs + the 146-page merged Master Lecture. No further ASE work queued until the student asks.
- **Data Mining is now the active subject.** Next lecture topic: Feature Selection Techniques, from professor-provided sources. Record only; do not prepare/study it until the student directs.
- [x] Cross-subject current-status mind map (`00_STUDIO_HUB/CURRENT_MATERIALS_MAP.md`) — delivered.
- [x] Wednesday–Sunday dated plan (`PLAN_2026-09-23_to_27.md`) — delivered.
- Cyber Security Week 02 booklet on Risk is available; the postponed quiz covers two booklets, exact date unconfirmed.
- English and Soft Computing are deferred for now.
- Artificial Intelligence lecture moved from Tuesday to Sunday (dean unavailable).
- **Correction 2026-09-18 (student-confirmed):** the previously listed "Week 01 viva defense drill with Dr. Ali Fahim" was **agent-inferred and is not a real event**. The Patriot-drift / Brooks material stays valid *study* content, but it is not tied to any scheduled assessment.
- **Deliverables Ready:** `Week_01_Lecture01_Software_Foundations_and_Crisis.docx` & `seminar_lecture01_software_crisis.pptx`.
---

## 3. Weekly Course Schedule Quick-Reference

| Day | Time | Subject | Instructor | Credits |
|:---|:---|:---|:---|:---:|
| **Sunday** | 08:30 – 10:30 | 01_Cyber_Security | Asst. Prof. Dr. Huda Lafta Majeed | 2 |
| **Sunday** | 10:30 – 11:30 | 02_English_Language | Asst. Prof. Dr. Haidar Akab Alwan | 1 |
| **Monday** | 08:30 – 10:30 | 03_Data_Mining | Asst. Prof. Dr. Ahmed Shakir Abd Al-Rida | 2 |
| **Monday** | 10:30 – 01:30 | **04_Advanced_Software_Eng** (Active) | Asst. Prof. Dr. Ali Fahim Ni'ma | 3 |
| **Tuesday** | 08:30 – 10:30 | 05_Soft_Computing | Prof. Dr. Abdul Hadi Mohammed Adkhil | 2 |
| **Tuesday** | 10:30 – 01:30 | 06_Artificial_Intelligence | Prof. Dr. Saif Ali Al-Saidi | 3 |

---

## 4. College Buddy Pointer
- **Interactive Ledger:** `00_STUDIO_HUB/COLLEGE_BUDDY.md` (Tracks upcoming professor dates, oral defense rehearsals, and post-event debrief check-ins).
