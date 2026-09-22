---
current_semester: "Semester 1 (Fall 2026)"
active_week: 1
active_subject: "04_Advanced_Software_Eng"
active_subject_code: "CS-MCS-504"
immediate_todo: "Tuesday preparation: read and review Soft Computing Week 01 for Prof Dr Abdul Hadi. Data Mining W03 remains unfinished; do not revise W02/W03 summaries yet. Artificial Intelligence remains empty and on hold."
next_session_focus: "Complete the Soft Computing Week 01 review for Tuesday, then capture the actual lecture outcome. Keep AI on hold until the dean sends material."
last_updated: "2026-09-22"
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
| **Last Updated** | `2026-09-19` | DM W02+03 done; SC syllabus synced + **Week 01 note rebuilt in DM method**; Cyber Sunday quiz pending |

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
- [ ] **`01_Cyber_Security` Week 01 — scenario drills** — the only thing left before Sunday's quiz
- [ ] **Prepare for the `01_Cyber_Security` daily quiz (امتحان يومي)** — Sunday 2026-09-20, 08:30 lecture, on Week 01 material
- [x] **`03_Data_Mining` Week 02 comprehensive note built** — `03_Study_Notes/Week_02_Data_Types_and_Preparation.md` (lecture text preserved + Gemini frameworks + Dr. Ahmed formula layer + 50-question bank)
- [x] **`03_Data_Mining` Week 03 comprehensive note built** — `03_Study_Notes/Week_03_Feature_Extraction_and_Portability.md` (feature extraction + portability matrix + similarity graph + ~35Q; cross-linked to Week 02)
- [x] **`03_Data_Mining` — Monday delivered Feature Extraction and Portability content** — note and logical/mathematical audit are in the vault. **Week numbering remains subject to doctor confirmation; Weeks 01–03 have study notes.**
- [x] **Answer Dr. Ahmed Shakir's Week 02 question** — *"what is the data type of a URL?"* → **Nominal** (recorded in Week 02 comprehensive note §1.2)
- [ ] *(Low stakes)* English presentation — Sunday 2026-09-27: a short research-style paper on any computer/software field in English, presented on the Data Show (~5 min)
- [x] **`05_Soft_Computing` official syllabus synced from alaidi.net** — course window 8/9/2026–**8/12/2026**; Midterm **20/10/2026 Weeks 1–6 fuzzy** (provisional — doctor may renumber); chain codes/ANFIS are NOT official weekly topics this term
- [x] **`05_Soft_Computing` Week 01 comprehensive note REBUILT** — `03_Study_Notes/Week_01_Introduction_to_Soft_Computing.md` in Data Mining method (full lecture text + Arabic conceptual layer + decoded images + long doctor answers + 35Q bank). **Not AI-slop compression.**
- [x] **`05_Soft_Computing` Week 2 source staged + local OCR** — PDF pages 1–66 only; searchable OCR at `02_Raw_Materials/W02_Fuzzy_Logic_Systems_OCR.md`; equations still require source-PDF validation
- [x] **`05_Soft_Computing` Week 02 FINAL BOOKLET delivered** — `03_Study_Notes/w02-fuzzy-logic-systems-booklet.{html,pdf}` (29pp = cover + 28 sections, English, MathJax). Math from `W02_Fuzzy_Math_Vision_Verified.md`; LaTeX-escape corruption repaired and rebuilt; source-verified against pp. 59/60/65/66 page images. Commit `a8cd34e`, pushed. **Layout density question open with the student** (one-topic-per-page ≈ 45% fill; could compress 29pp → ~18pp).
- [ ] **`06_Artificial_Intelligence`** — waiting. **Abu Al-Hasan will report it himself when Dr. Saif posts material — do not proactively check the group.**

### Next Session Focus
- **Topic:** Soft Computing Week 02 — Fuzzy Logic Systems, starting with the staged pages 1–66.
- **Topic:** Week 01 Cyber Security revision for the Sunday daily quiz, plus the Data Mining "URL data type" question.
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
