---
current_semester: "Semester 1 (Fall 2026)"
active_week: 1
active_subject: "04_Advanced_Software_Eng"
active_subject_code: "CS-MCS-504"
immediate_todo: "Work Buddy: Thursday step of PLAN_2026-09-23_to_27.md is DONE (Week_02_Risk_Bilingual_Concept_Outline.md). Next per plan: Friday - finish the Risk booklet's core content and connect both Cyber booklets. Needs the student: the illustrated booklet (figures are absent from the delivered DOCX) and the confirmed quiz date."
next_session_focus: "Work Buddy follows the dated plan through Sunday 2026-09-27, records verified study progress, and attends to actual student reports. Cyber quiz date remains unconfirmed."
last_updated: "2026-09-23"
status: "WEEK_01_ACTIVE"
---

# Master Studio: Active Session State

> **Purpose:** Fast-boot runtime state file. Agents read this file at session start to restore context in $< 50$ tokens.

```
+-------------------------------------------------------------------------------+
|                            FAST-BOOT CURRENT POINTER                          |
|                                                                               |
|  Semester: Semester 1 (Fall 2026)      Active Week: Week 01                   |
|  Subject:  04_Advanced_Software_Eng    Target Path: 01_Semester_1/04_...      |
|  Status:   Initialized & Operational   Date: 2026-09-16                       |
+-------------------------------------------------------------------------------+
```

## 1. Current Session Context

| Key | Current Value | Notes / Description |
|:---|:---|:---|
| **Current Semester** | `Semester 1 (Fall 2026)` | First Course / Preparatory Coursework Phase |
| **Active Week** | `1` | Week 1: Introduction, Architecture Overview & Standards |
| **Active Subject** | `04_Advanced_Software_Eng` | Asst. Prof. Dr. Ali Fahim Ni'ma (3 Credit Hours) |
| **Last Updated** | `2026-09-23` | Student's latest lecture report is recorded in the 2026-09-23 shared session journal. |

---

## 2. Immediate Tasks & Roadmap

### Active Work Queue
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
- [x] **`01_Cyber_Security` Week 02 Risk — bilingual concept outline delivered** — `03_Study_Notes/Week_02_Risk_Bilingual_Concept_Outline.md` (570 lines, 24 sections, EN concept + AR explanation). Full coverage of the booklet; formula card (`S = F × K`, `R = S / M`); terminology table; 8 `[VERIFY]` flags; 10 Week 01 closed-book recall prompts; exam-method mapping. **Two blockers found:** the delivered DOCX has **zero images** (all figures referenced but absent) and the **formula operators are missing** from the text layer.
- [x] **`01_Cyber_Security` Week 02 Risk — exam-focus sheet delivered (lecture-driven)** — `03_Study_Notes/Week_02_Risk_Exam_Focus.md`. Built from the **doctor's own 30 highlight runs + 27 coloured runs** recovered from the DOCX (my first pass had missed the formatting layer entirely) plus the student's 2026-09-23 lecture report. Contains the emphasis map, all numbered sets with counts, the acronym table, the two equations with a comparison table, the "influencing factors" answer, per-item verdicts, and the coverage boundary. **5 open items flagged for the student — none resolved silently.**
- [x] **`01_Cyber_Security` Week 02 Risk — SOURCE IDENTIFIED + fact-checked** — the booklet is a direct extraction of **Sharp, R., "Risk", in *Introduction to Cybersecurity: A Multidisciplinary Challenge*, Springer, 2024, pp. 37–56** ([DOI 10.1007/978-3-031-41463-3_3](https://doi.org/10.1007/978-3-031-41463-3_3)). Verification report: `03_Study_Notes/Week_02_Risk_Source_Verification.md`. **Two verified factual errors in the booklet:** (1) the "ISO/IEC 27002 **2022** … 14 categories" line — the 14 categories are the **2013** structure, 2022 is **4 themes / 93 controls** (and Dr. Huda highlighted this line yellow); (2) **"OCTAVE FORTE" does not exist** — only three public OCTAVE methodologies. Plus "Inheritance" → **Inherence**. Chapter body is paywalled, so Sharp's exact equation letters remain unverified.
- [x] **`01_Cyber_Security` Week 02 Risk — equations verified mathematically** — `03_Study_Notes/Week_02_Risk_Formula_Mathematical_Verification.md`. `S = F × K` proven sound (multiplication required, not addition). `R = S / M` proven sound **only on `M ≥ 1`** — at `M = 0` it divides by zero and for `0 < M < 1` it gives residual risk greater than inherent risk, so **`M` is a protective factor, not a count** (which is why the booklet's "number *and* effectiveness" wording is necessary). Substituting `M = 1/(1 − CE)` collapses it to the industry-standard `R = S(1 − CE)` — **the division form is the mainstream model re-parameterised**. The student's reported `f = s·k` / `f = s/n` (n = threats) **fails a logical contradiction test**. Chapter PDF remains paywalled — page images could not be obtained.
- [x] **`01_Cyber_Security` Week 02 Risk — CLEAN BOOKLET delivered** — `03_Study_Notes/Week_02_Risk_Booklet.pdf` (**34 pages**, English only, 27 sections, 6 embedded figures, contents page with real page numbers). Built from the original book + the doctor's marking, with every correction carried in a "Corrected" box. Builder: `90_Shared_Toolbox/tools/build_cyber_w02_booklet.py`; page numbering via the new `booklet_postprocess.py`. **This is now the primary revision document for the Cyber quiz.**
- [x] **`01_Cyber_Security` — 2-page EXAM SHEET delivered** — `03_Study_Notes/Cyber_Exam_Sheet.pdf`. **Covers BOTH booklets** (the postponed quiz tests both): page 1 Week 01 (Ch. 1–6, six equations, CIA triad with bracketed techniques, domain weights, Ch. 7 exclusion); page 2 Week 02 Risk (two equations, both matrices, the five lists, 13 traps, corrected facts). English, print-ready. Builder: `90_Shared_Toolbox/tools/build_cyber_exam_sheet.py`. **This is the last-minute revision document.**
- [x] **`04_Advanced_Software_Eng` Week 02 — deep term analysis delivered** — `03_Study_Notes/Week_02_SDLC_Terms_Deep_Analysis.md`. **Key finding: Mall chapter 2 (pp.73–135) is the PRIMARY source for this lecture, not Sommerville** — Sommerville has **0 hits** for Build & Fix, **0 relevant hits** for RAD, and no V-Model or named Evolutionary model. Sommerville is the secondary (best on process theory, waterfall's critique, incremental's benefits/problems, the spiral's sectors, and the agile manifesto). Pressman is the weakest fit; Agarwal mostly restates Sommerville. Also recovered **Mall's exercise set (pp.130–131)** — exam-shaped questions covering every lecture term, including Q54 which is a full paper on RAD alone. **No lecture slides exist for W02 — the term list came from the student's report, so the mapping is an inference (recorded as such).**
- [ ] **`04_Advanced_Software_Eng` Week 02 — study note not yet written.** The deep analysis maps the sources; the actual note is the next step if the student wants it.
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
- [x] Create a cross-subject current-status mind map to help the student stay oriented across all six subjects.
- [x] Split the Wednesday–Sunday workload into a dated plan, keeping English and Soft Computing parked and Data Mining Feature Selection recorded but inactive.
- Data Mining next lecture: Feature Selection Techniques, from professor-provided sources. Record only for now; do not prepare/study it yet.
- Cyber Security Week 02 booklet on Risk is available; quiz covers two booklets, but exact date remains unconfirmed.
- English and Soft Computing are deferred for now.
- Artificial Intelligence lecture moved from Tuesday to Sunday because the dean was unavailable.
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
