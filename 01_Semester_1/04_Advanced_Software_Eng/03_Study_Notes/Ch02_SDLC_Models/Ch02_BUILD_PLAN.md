---
title: ASE Chapter 2 — Question-Pack Plan · Software Life-Cycle Models
course: Advanced Software Engineering
chapter: 2
status: CLOSED — source corrections, authored synthesis questions, and print gates completed (2026-10-17)
updated: 2026-10-17
---

# Chapter 2 — Software Life-Cycle Models

## Purpose and current status

This document records the chapter-specific plan, source hierarchy, confirmed instructor vocabulary, exercise mapping, and artifact status for printable question-and-answer packs.

**Current Status (2026-10-17): CLOSED for study and printing.** The six printable packs are authored and exported (54 PDF pages). Coverage includes all 20 B.B. Agarwal exercises, all 25 K.K. Aggarwal & Singh slide MCQs, and the professor’s eight vocabulary blocks. This closure pass corrected the Incremental/Iterative source distinction and source locators, aligned Scrum terms to Sommerville 9e, corrected the maintenance-cost locator to printed p.40, and added five concise authored synthesis questions for Agile response to change, Build & Fix, Incremental vs Iterative Enhancement, XP/TDD, and Scrum/XP. All six pack Markdown files pass strict lint; T2/V2 PDFs were regenerated and their affected pages visually reviewed. The closure record does not claim a blind audit or a fresh full-page visual review of every pack.

## Sources and authority

1. **Primary course textbook:** B.B. Agarwal, S.P. Tayal, and M. Gupta, *Software Engineering & Testing: An Introduction* (Jones & Bartlett, 2010), local searchable copy `02_Raw_Materials/Reference_Textbooks/CS_Agarwal_SW_Engineering_and_Testing_2010.pdf`. The title page and TOC were checked directly. Chapter 2 starts at printed p.29 and ends with its 20 exercises on p.52; the next chapter starts on p.53. This is the book the student identified as the course source and it controls textbook answers.
2. **Separate scanned textbook:** `02_Raw_Materials/Reference_Textbooks/AliFahim_Software_Engineering.pdf` is a 256-page double-page scan. Its cover/title page is missing. The TOC says “Preface to the Third Edition”; its Ch.1 starts at printed p.1, Ch.2 at p.20, and its chapter structure and pagination strongly match K.K. Aggarwal & Yogesh Singh, *Software Engineering*, 3rd ed. This identification is high-confidence from internal structure, not a visible author imprint. It is **not** the B.B. Agarwal et al. 2010 course textbook.
3. **Separate searchable slide/question source:** `02_Raw_Materials/Aggarwal_Singh_SE_3rd_ed_By_Chapter/Ch02_Software_Development_Life_Cycle_Models.pdf`. Its README and slide 1 identify 48 pages of slides for K.K. Aggarwal & Yogesh Singh, *Software Engineering*, 3rd ed. (New Age International, copyright 2007). These slides are not companion slides to the B.B. Agarwal et al. 2010 textbook. The 1,094-page full-source file and three files in `DUPLICATES_Review/` share SHA-256 `2bc72b3dc1e44057625a587408071b0eb7596c643103541e7b1957c0c471bd2f`; pages 82–129 of the full-source file have text identical to the 48-page Ch02 PDF, so the index stores the slide content once. The set provides 25 MCQs (slides 41–45) and 22 exercises (slides 46–48); label questions and claims as slide-derived.
4. **Additional archived lecture:** `02_Raw_Materials/Chapter_Extracts/SE_Lec02_Software_Life_Cycle_Models (archive).pdf` has 42 pages, 41 with visible content. Its pages do not name the author/lecturer. Use it as course-coverage evidence, not a verified professor-authored term list.
5. The Ch02 question bank in `Aggarwal_Singh_SE_3rd_ed_By_Chapter` is from the separate K.K. Aggarwal & Singh source. Do not merge its question counts into the 2010 textbook's exercise weights. The old analysis and `ASE_Ch1-3_Exercises_Aggarwal.md` need source-by-source verification before reuse.
6. `Week_02_BUILD_PLAN.md`, `Week_02_Study_Plan_and_Index.md`, `Week_02_Master_Lecture.md`, and `Week_02_SDLC_Terms_Deep_Analysis.md` are coverage maps, not proof that every item was officially assigned. Mall/Sommerville/Pressman may fill only a required gap confirmed in the course scope.

## Current depth and source-war rule (student clarification, 2026-10-16)

The professor supplies vocabulary rather than a full lecture account. His Chapter 2 list is now confirmed and preserved in [`V2_Doctor_Vocabulary.md`](V2_Doctor_Vocabulary.md): SDLC/Build & Fix/Waterfall; Incremental and Iterative Enhancement; RAD and applicability; Evolutionary and Prototyping; Spiral and risk-driven development; Unified Process phases; model selection by requirements and risk; Agile/XP/Scrum. The archived lecture and companion slides are supporting coverage sources, not substitutes for this scope list.

For each confirmed term, explain enough to define it, show its main mechanism/conditions, preserve important distinctions, and read or reproduce a relevant figure where needed. Add **modest depth** to repair omissions or make a slide point understandable. Do not produce an exhaustive survey or inflate a term into a chapter-length treatment.

Triangulate source by source and term by term: prefer the course-aligned B.B. Agarwal et al. 2010 book when it adequately covers the term; otherwise choose the single clearest/strongest supporting source for the missing point. Do not concatenate every source or import every taxonomy. Keep lecture-only and external exam-bank material labeled separately. The user's `Downloads/5-word.json` is prior-method evidence from Chapter 5/6 work, not a Chapter 2 term list or new direct statement from the professor.

## Shared local Chapter 2 knowledge collection

Chapter 2 source chunks are registered in `00_STUDIO_HUB/indexes/04_Advanced_Software_Eng/knowledge_sources.json` and stored in `ase_knowledge_vectors.sqlite3`. The collection keeps the 2010 course book, K.K. Aggarwal & Singh scan/slides, supporting books, archived lecture, study notes, selected practice-bank pages, and figure OCR in separate source classes. Use semantic hits to find a candidate passage, then verify the original page/slide. OCR and figure-image hits are navigation aids and may misread words or diagram relationships.

Agents should run `python "90_Shared_Toolbox/tools/ase_vector_index.py" status`, then search with `--chapter 2` and the needed `--category`. An index result is not itself evidence that a term is on the professor's list or that a claim is correct. Search in `primary_book` first; query a `supporting_book` only for a mapped gap; use `question_bank` / `exam_example` only for separate practice patterns.

## Vocabulary and coverage map

The professor's exact list is confirmed in `V2_Doctor_Vocabulary.md` and is the scope. The B.B. Agarwal et al. book's Chapter 2 TOC covers SDLC (printed p.29), Waterfall (p.36), Prototyping (p.41), Spiral (p.44), Evolutionary Development (p.46), Iterative Enhancement (p.47), RAD (p.49), and a process-model comparison (p.50). Its exercise set is printed p.52. Use that book as the answer authority where it covers the term; use the source-war map in V2 to fill only demonstrated gaps and keep slide-only topics visibly attributed to slides.

- **Software life cycle and life-cycle models** — B.B. Agarwal et al. §2.1, printed pp.29–35; the slide set provides a different overview and model taxonomy.
- **Build & Fix Model** — K.K. Aggarwal & Singh slides 4–5 and the matching scanned book Ch.2; absent from the B.B. Agarwal et al. Ch.2 TOC. Attribute any question/answer on it to the lecture/secondary source unless another primary-book location is verified.
- **Waterfall Model** — B.B. Agarwal et al. §2.2, beginning printed p.36; diagrams, phases, assumptions, and limitations. Confirm each exact page from the book before answering.
- **Incremental Process Models** — K.K. Aggarwal & Singh slide 9; not a named B.B. Agarwal et al. section. Keep it distinct from that book's Evolutionary Development and Iterative-Enhancement sections.
- **Iterative-Enhancement Model** — B.B. Agarwal et al. §2.6, printed p.47 onward, plus slides 10–11. Do not rename it **Iterative Waterfall**.
- **Rapid Application Development (RAD)** — B.B. Agarwal et al. §2.7, printed p.49 onward; slides 12–15 additionally show the IBM-style activity sequence Requirements Planning, User Design, Construction, Cutover. The slide-specific names must not be attributed to the book unless verified there.
- **Evolutionary Development Model** — B.B. Agarwal et al. §2.5, printed p.46 onward, plus slides 16–17. Preserve the book's distinction from Iterative Enhancement.
- **Prototyping Model** — B.B. Agarwal et al. §2.3, printed p.41 onward, plus slides 18–19.
- **Spiral Model** — B.B. Agarwal et al. §2.4, printed p.44 onward, plus slides 20–23; keep the book's spiral quadrants distinct from the lecture slide labels if they differ.
- **Unified Process (UP) / Rational Unified Process (RUP)** — slides 24–36 and the separate K.K. Aggarwal & Singh scan; not listed as a named model in the B.B. Agarwal et al. Ch.2 TOC. Keep “phase” distinct from “workflow”; cite slide/scan when required by the course.
- **Selection of a Life-Cycle Model** — slides 37–41 and the separate K.K. Aggarwal & Singh source. The B.B. Agarwal et al. book has a comparison table at printed p.51, but do not claim it contains the same four selection matrices unless directly checked.

### Additional confirmed terms from the professor's list

The confirmed list explicitly includes Agile / XP / Scrum and the Unified Process. They do not all appear as named sections in the B.B. Agarwal et al. 2010 Chapter 2 contents. Their source routing is recorded term by term in `V2_Doctor_Vocabulary.md`; use only enough material from the mapped supporting source to explain the listed concepts. Do not add V-Model, Iterative Waterfall, Agile Manifesto, or other unlisted terms to the core scope merely because they occur in another source.

## Source war for possible gaps

The Ch02 source review found the primary 2010 text and the separate K.K. Aggarwal & Singh slides/books cover overlapping but different content. The slide bank is not the primary textbook. The confirmed list and its source-war decisions are summarized in `V2_Doctor_Vocabulary.md`; the decisions below retain only the relevant boundaries:

- **Incremental delivery → Sommerville Ch.2 §2.3.2, pp. 47–48; keep it distinct from B.B. Agarwal’s Iterative Enhancement.** The instructor explicitly lists Incremental separately from Iterative Enhancement; preserve that distinction.
- **Build & Fix → Mall Ch.1 §1.1.1, pp. 4, 12–13, and K.K. slides 4–5.** Use Mall as the gap-filler because it is not a named section in the B.B. 2010 Ch.2 contents.
- **Unified Process → Sommerville Ch.2 §2.4.** Use it as the single explanatory source for the missing named topic, with K.K. slides 24–36 as separately attributed course diagrams.
- **Agile / XP / Scrum → Sommerville Ch.3** as the default supporting source. Use Mall Ch.2 §§2.4.1–2.4.4 only when a question follows Mall's life-cycle-model framing.
- **Other books:** Pressman and Leach are not default sources for this list. Reopen them only if a specific listed concept remains unclear or unsupported after checking the course book and mapped source in V2. Keep the B.B. Agarwal 2010 text, K.K. Aggarwal & Singh materials, and supplementary books distinct in citations.

These locator ranges are planning leads. Confirm the exact printed page from the selected book before an answer is written. The older term-analysis file used PDF page positions for some references; do not copy its page numbers as printed pages without checking.

### Working term ledger for coverage checks

- **Core lifecycle words:** software life cycle, life-cycle model, process model, phase, iteration, release/version, maintenance, and retirement.
- **Named models in the archived deck / K.K. slide set:** Build & Fix (also called ad hoc on slide 5), Waterfall, Incremental Process Model, Iterative Enhancement, Rapid Application Development (RAD), Evolutionary Process Model, Prototyping, Spiral, Unified Process (UP), and Rational Unified Process (RUP). This is not identical to the primary B.B. Agarwal et al. 2010 textbook's Ch.2 TOC.
- **Waterfall phase vocabulary:** requirements, design, implementation, integration/testing, operation/maintenance. Preserve the slide's sequence and the textbook's wording when writing a “list/name the phases” answer.
- **RAD activity labels:** Requirements Planning, User Design, Construction, Cutover; user participation, reusable components, and skilled developers are related conditions, not extra phases.
- **Spiral activity labels:** planning, risk analysis, development, assessment. Do not confuse the four sectors with the phases/loops or with the spiral's radial cost dimension.
- **UP phase names:** Inception, Elaboration, Construction, Transition. The deck separately shows workflows and phase outcomes; keep these three categories distinct.
- **Model-selection dimensions:** requirements, development-team status, user participation, and project type/associated risk. These are selection factors, not lifecycle models.
- **Distinctions to test explicitly:** Incremental vs Iterative Enhancement vs Evolutionary; prototype vs delivered product; a UP phase vs a workflow; model suitability vs a universal ranking. “Iterative Waterfall” remains a separate pending term and must not be substituted for “Iterative Enhancement.”

### Vocabulary deliverable

The instructor's list is confirmed and preserved in `V2_Doctor_Vocabulary.md`. `V2_Vocabulary_Coverage.md/.pdf` is the completed study deliverable: each listed English term has a concise answer, a separate brief Arabic note where useful, and a source locator. Five authored synthesis Q&A items directly test source-gap concepts and distinctions without inflating the packs into essays.

## Figure assets extracted for planning

Rendered 21 high-value pages from the searchable Aggarwal & Singh companion-slide PDF at 2× to preserve its vector diagrams and tables as clear PNG references. These are source-page renders, not newly drawn or altered diagrams; their slide numbers remain the citation anchors. They are stored in `source_figures/`:

- Slides 4, 6, 11–13: Build & Fix, Waterfall, Iterative Enhancement, RAD examples and RAD activities.
- Slides 16–17, 19–21: Evolutionary process, its flow, Prototyping, Spiral diagram, and Spiral-sector explanation (`S21_Spiral_ReadingKey.png`).
- Slides 25, 27–28, 30, 32, 34, 36: UP phases, release/evolution cycles, workflows, and the outcomes of each phase.
- Slides 38–41: four model-selection matrices (requirements, development team, user participation, project type/risk).

The Spiral drawing itself is on **slide 20**; slide 21 explains its radial/angular dimensions and activities. Retain both, since the figure and its reading key are separate. Before including any page in a student-facing PDF, crop or embed it only if the labels stay legible and cite the companion slide separately from Aggarwal's printed-book page.

## Question-type weights by source

Neither textbook assigns marks for the Ch.2 exercises, so these are **practice-volume shares by item count**, never exam-mark predictions. Keep the two books' question banks separate.

### Primary course textbook — B.B. Agarwal, Tayal & Gupta (2010)

Chapter 2 has **20 written exercises** on printed p.52 and no separate MCQ section in its Ch.2 contents. A mutually exclusive classification by the main requested action gives:

- **14 explain/list/define/describe** (70%): Q1–6, Q8, Q10–12, Q14–16, Q18.
- **3 compare/evaluate trade-offs** (15%): Q17, Q19, Q20.
- **1 apply/select a model and justify** (5%): Q13, which contains four application scenarios inside one exercise.
- **2 draw/diagram** (10%): Q7 and Q9. Q8 also requests a diagram as a secondary requirement, so add diagram skills beyond the two primary-tagged prompts.
- **Calculation: 0** in this 20-exercise set.

This is the primary source-weighting for the study pack. It is a count of exercise stems, not subparts or marks.

### Separate K.K. Aggarwal & Singh companion slides

The different book's slide deck contains **25 MCQs + 22 written exercises = 47 slide-source items**. By item count, that is 53.2% MCQ and 46.8% written. Its written tasks classify as 14 direct explain/list/define/describe (63.6%), 3 compare (13.6%), 4 analyze/interpret/risk (18.2%), and 1 explicit draw (4.5%). Six of the 25 MCQs (24%) ask about model fit/selection: 2.11–2.15 and 2.17. No calculation items were found. These are a **separate supplemental slide-bank distribution**, not the primary book's official exercise mix.

### Pack-volume recommendation

Build the primary book's 20 exercises into T2–T4 by their tags, including Q13's four selection scenarios and the draw prompts. Keep the slide deck's 25 MCQs as a clearly attributed supplemental T1 bank, and the extra 22 slide exercises as comparison/coverage practice; do not combine their counts into the primary-book percentages. Add further drawing/interpretation practice only where the lecture's figures justify it and label it authored practice. No mark weights can be assigned without a professor rubric or past graded exams.

## Recommended question-pack structure

| Pack | Include | Reason |
|:---|:---|:---|
| `T1_MCQ` | The 25 MCQs from the K.K. Aggarwal & Singh slide deck, explicitly identified as supplemental slide-source questions. | Separate slide bank only; 6/25 ask model fit/selection. Verify keys against that slide deck. |
| `T2_Descriptive` | Primary 2010-book direct exercises Q1–6, Q8, Q10–12, Q14–16, Q18. | 14/20 primary exercises (70%). |
| `T3_Compare_Analyze` | Primary 2010-book Q17, Q19, Q20; optionally add separate tagged K.K. slide prompts without merging counts. | 3/20 primary exercises (15%). |
| `T4_Diagrams` | Primary 2010-book Q7 and Q9, with Q8 diagram as a secondary task; add slide-based label/interpret practice in a separate subsection. | 2/20 primary exercises have drawing as their main verb (10%); Q8 also requires a diagram. |
| `T5_Apply_Select` | Primary 2010-book Q13 (four scenarios); optional K.K slide MCQ model-fit set remains separately sourced. | One exercise stem (5%) with four application subparts. |
| `V2_Vocabulary_Coverage` | Confirmed terms from the deck plus any student-supplied professor list. | Ensures each term has an answer, not just a source pointer. |

**No separate calculation pack is planned** unless source exercises reveal a genuine numerical task. No standalone “Create/Evaluate” pack is assumed; add question types only if the chapter's material makes them useful.

## Build order and checks

1. Use the confirmed professor list in `V2_Doctor_Vocabulary.md` as scope; consult companion slides and the archived lecture as separately attributed course material.
2. Re-read Aggarwal Ch.2 pages and visually verify the exercise/MCQ stems and printed page numbers. Check the answer key before solving official MCQs.
3. Freeze the pack inventory and map every lecture term/exercise to an answer location before authoring.
4. Build `T1_MCQ` and `T2_Descriptive`; then diagrams; then comparison/selection scenarios; then V2 vocabulary and the index.
5. For each pack, run content/source review, lecture-coverage review, linter, PDF export, question-answer cohesion check, and visual inspection as separate gates. Do not claim a blind audit unless the reviewer did not see the answers.

## Artifact delivery status
 
- All five question packs (`T1` through `T5`), `V2_Vocabulary_Coverage`, and `V2_Doctor_Vocabulary` are authored, critically revised, and published on disk in both Markdown and PDF formats.
- Master index `00_INDEX.md` provides file mappings, source cross-references, and verification summaries. Total volume: 54 PDF pages across the 6 printable deliverables.
- Status: CLOSED — source/citation corrections and authored synthesis coverage completed on 2026-10-17; current pack PDFs pass the publication gates recorded in `00_INDEX.md`.

## Remaining verification limits (non-blocking)

- The K.K. Aggarwal & Singh 3rd edition narrative textbook scan (`AliFahim_Software_Engineering.pdf`) contains the official Chapter 2 answer key on printed p. 499, confirming all 25 MCQs (2.1 to 2.25).
- Question 2.18's assertion regarding "Specifications accounting for the maximum percentage of project errors" is confirmed as the official key on p. 499, but lacks an independent empirical statistics table or survey in Chapter 2 textbook prose; it is documented with its evidentiary limits.
- Primary textbook exercises (B.B. Agarwal et al., 2010, p. 52, Q1–Q20) do not assign individual numerical marks or exam point weights; exercise shares represent practice item proportions only.

