# ASE Chapter 2 — Question & Answer Packs Index
## Software Life-Cycle Models (CS603)

**Academic Supervisor:** Asst. Prof. Dr. Ali Fahim Ni'ma  
**Institution:** College of Computer Science & IT — University of Wasit  
**Authoring Engine:** Master Studio (Oh My Pi — 2026-10-16)  
**Status:** CLOSED — source corrections, five authored synthesis questions, and print gates completed (2026-10-17)

---

## 1. Chapter Inventory & Pack Roster

| Pack Slug | Question Form | Source Authority & Anchor | Total Items | Markdown | Clean PDF | Status |
|:---|:---|:---|:---:|:---:|:---:|:---:|
| **`V2_Vocabulary_Coverage`** | Confirmed Doctor's Vocabulary | Dr. Ali Fahim (2026-09-23) + B.B. Agarwal (2010) + Supporting Sources | 8 Core Blocks (5 Synthesis Recall Qs) | [MD](V2_Vocabulary_Coverage.md) | [PDF](V2_Vocabulary_Coverage.pdf) | PRISTINE (9 pp) |
| **`T1_MCQ`** | Multiple Choice Questions | K.K. Aggarwal & Yogesh Singh (2007) pp. 37–39 & Slides 41–45 (Official Key on printed p. 499) | 25 MCQs (2 Synthesis Recall Qs) | [MD](T1_MCQ.md) | [PDF](T1_MCQ.pdf) | PRISTINE (9 pp) |
| **`T2_Descriptive`** | Descriptive, Procedural & Definitional | B.B. Agarwal et al. (2010), p. 52 (Q1–6, 8, 10–12, 14–16, 18) | 14 Exercises (2 Synthesis Recall Qs) | [MD](T2_Descriptive.md) | [PDF](T2_Descriptive.pdf) | PRISTINE (12 pp) |
| **`T3_Compare_Analyze`** | Trade-offs & Model Comparisons | B.B. Agarwal et al. (2010), p. 52 (Q17, 19, 20) + Slides (Ex 2.7, 2.9) | 5 Analyses (2 Synthesis Recall Qs) | [MD](T3_Compare_Analyze.md) | [PDF](T3_Compare_Analyze.pdf) | PRISTINE (6 pp) |
| **`T4_Diagrams`** | Architecture Schematics & Figure Geometry | B.B. Agarwal (2010) Q7, 9 + Slides 6, 18, 20, 21, 25, 28 | 4 Visual Units (2 Synthesis Recall Qs) | [MD](T4_Diagrams.md) | [PDF](T4_Diagrams.pdf) | PRISTINE (11 pp) |
| **`T5_Apply_Select`** | Applied Scenarios & Justified Selection | B.B. Agarwal et al. (2010) Q13 (i–iv) + Selection Matrices | 4 Scenarios + Selection Matrix (2 Synthesis Recall Qs) | [MD](T5_Apply_Select.md) | [PDF](T5_Apply_Select.pdf) | PRISTINE (7 pp) |

**Source Counts (Not Exam Marks):** 
- Primary textbook: **20 written exercises** (p. 52, including Q13 with 4 scenarios).
- Supplemental textbook & slides: **25 MCQs** (printed pp. 37–39 & Slides 41–45; keys verified against official key on printed p. 499; Q2.18 noted as unverified empirical claim in textbook prose).
- Confirmed instructor vocabulary: **8 core topic blocks**.
- Focused Active Recall drills: **Duplicate prompts removed; unique synthesis questions provided with answers directly underneath**.
Total generated artifact volume: **54 PDF pages**.

---

## 2. Source Hierarchy & Cross-Verification Matrix

1. **Primary Course Textbook:**
   - B.B. Agarwal, S.P. Tayal, and M. Gupta, *Software Engineering & Testing: An Introduction*, Jones & Bartlett Publishers, 2010.
   - Chapter 2: printed pp. 29–52 (All 20 chapter exercises verified on p. 52).
2. **Supplemental Searchable Companion Slides:**
   - K.K. Aggarwal & Yogesh Singh, *Software Engineering*, 3rd ed., New Age International Publishers, 2007.
   - Chapter 2: 48 slides. Slides 41–45 provide 25 MCQs; Slides 46–48 provide supplemental exercises; Slides 36–41 provide selection matrices.
3. **Confirmed Instructor Vocabulary:**
   - Transcribed from Dr. Ali Fahim Ni'ma's official cohort announcement (2026-09-23 08:22 AM), preserved verbatim in [`V2_Doctor_Vocabulary.md`](V2_Doctor_Vocabulary.md).
4. **Gap-Filling Standards:**
   - Build & Fix: Rajib Mall (4th ed.), Ch. 1, §1.1.1, pp. 4, 12–13; K.K. Aggarwal & Singh Slides 4–5.
   - Unified Process: Ian Sommerville (9th ed.), §2.4. Agile: §3.1, pp. 58–60; XP: §3.3, pp. 65–72; Scrum: §3.4, pp. 73–74.

---

## 3. Inviolable Governance & Delivery Gates

- [x] **Zero-Defect Linter Gate:** All 6 Markdown packs passed `note_linter.py --fix --strict` with code 0 (`PRISTINE`).
- [x] **Academic PDF Gate:** All 6 packs compiled into publication-grade PDFs via DirectWrite engine (`pdf_exporter.py -t study_pack`).
- [x] **Formatting & Provenance Standard:** Source-grounded definitions and rules formatted in **bold**; synthesis in plain text; concise Arabic notes isolated in callouts.
- [x] **Visual & RTL Inspection:** Verified via high-resolution image rendering; zero text clipping; pristine KaTeX math; proper LTR code and RTL Arabic text flow.
- [x] **No Commit / No Push:** Artifacts staged cleanly in local vault for student review.
