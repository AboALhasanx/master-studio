# Chapter 3 Build Plan — Software Requirements: Analysis and Specifications

**Course:** Advanced Software Engineering (CS603)  
**Instructor:** Asst. Prof. Dr. Ali Fahim Ni'ma  
**Status:** All 6 Question & Answer packs are authored, cross-reviewed, strict-linted, and exported to current DirectWrite PDFs totaling 63 pages (excluding the index PDF). The six PDFs are also assembled as `Ch03_Complete_Print_Pack.pdf`. The coverage map accounts for Dr. Ali Fahim's 7 vocabulary areas, all 36 textbook exercises, all 25 slide MCQs, and 17 gap-closing synthesis items. Cross-review included targeted source checks and visual/layout corrections; it was not a blind claim-by-claim audit.
**Prepared:** 2026-10-17 by Codex & Antigravity (Chapter 3 source audit, vector indexing, pack authoring, and PDF publication)

## 1. Student decisions carried forward

- The instructor's vocabulary list defines the target. Add enough depth to explain terms and close demonstrated gaps; do not turn the chapter into a survey of every textbook.
- English questions and model answers; concise Arabic notes/traps kept outside the answer.
- Bold marks source-grounded material or a faithful source-based paraphrase. Plain text is our framing or synthesis. Do not add verbal inference labels.
- Answers directly answer the prompt. No “the book says”, “the author states”, or similar meta-prefaces. A source locator goes on its own line after the answer.
- Aggarwal & Singh is the default course-source family. Source precedence is chapter-specific: Chapter 2 explicitly used B.B. Agarwal et al. (2010); Chapter 3 is mapped first to the K.K. Aggarwal & Yogesh Singh scan and its matching official companion slides because their title, scope, exercises, and lecture vocabulary align. Keep B.B. Agarwal et al. (2010) clearly separate and use it selectively for a real gap or clearer treatment.
- Use the printed page visible on a book page. For a two-page scan, also record the local PDF spread when needed. A slide-only statement must be cited as a slide.
- Question-type counts are source-pattern counts, not exam marks or predictions.

## 2. Confirmed instructor scope

Source: Dr. Ali Fahim's cohort message dated **2026-09-30, 2:38 PM**, preserved in the student-supplied transcript at `.codex/attachments/47d04156-932c-4e5f-8296-76b36aac7c69/Pasted text.txt`.

| Instructor item | Planned coverage boundary |
|:---|:---|
| Requirements Engineering — crucial process steps; present state of practice | Definition/purpose, problem statement → elicitation → analysis → documentation/SRS → review; challenges listed by the course source |
| Types of requirements — functional/non-functional; user/system; interface specification | Keep these as distinct classification axes; do not conflate quality attributes with system-level requirements |
| Feasibility Study — purpose and focus | Purpose as evaluation of a proposed project's potential impact; technical feasibility examples; cost/schedule realism, business model, market, major risks, requirements stability, prototype agreement, and plan adequacy (slides 11–15) |
| Requirements Elicitation — interviews; brainstorming sessions; FAST; QFD; Use Case Approach | Give each instructor-listed technique a concise definition or purpose and include the source-native questions and modeling tasks |
| Requirements Analysis — DFDs; data dictionaries; ER diagrams; software prototyping | Definitions, notation, distinctions, and the source-native modeling/application tasks |
| Requirements Documentation — nature of SRS; good-SRS characteristics; organization | SRS purpose and boundary (“what”, not implementation “how”), listed characteristics, and structure/issues |
| Requirements Validation — requirements reviews | Validation objective, review process, common defect checks, and review follow-up |
| Risk appears in the Chapter 3 Feasibility Study material | Slide 14 asks whether major project risks have been identified and can be surmounted. Keep that point under feasibility; it is not a separate item in the instructor's Chapter 3 vocabulary and does not define a full risk-management lifecycle. |

### Not automatically in scope

The K.K. chapter also contains **decision tables and other elicitation material** beyond the instructor-listed techniques. Decision tables are not named in the instructor list or clearly emphasized by the Chapter 3 exercises; keep them optional/low-priority unless later evidence shows they were taught. K.K. slides 117–119 introduce Requirements Management, and B.B. Agarwal et al. (2010) treats it in its process; it is not on the confirmed instructor list, so do not expand it into a major pack section.

## 3. Source identity and precedence

| Tier | Source | Verified location | Use and limit |
|:---|:---|:---|:---|
| Course primary | K.K. Aggarwal & Yogesh Singh, *Software Engineering*, 3rd ed. (bibliographic match is high-confidence; the local scan has no cover/title page) | `02_Raw_Materials/Reference_Textbooks/AliFahim_Software_Engineering.pdf`; printed Ch.3 pp. **40–138**; scan PDF spreads **26–75**. PDF spread 26 visibly shows printed pp.40–41; spread 75 ends at p.138, with Chapter 4 beginning on p.139. | Primary answer source for the instructor-aligned chapter. Verify scan claims on page images; OCR is navigation only. Cite the printed page. The similarly named 1,094-page file under `DUPLICATES_Review/` is the merged slide series, not this book scan. |
| Official companion slides | K.K. Aggarwal & Yogesh Singh, *Software Engineering* (3rd ed.), New Age International Publishers, 2007; identity appears on the slide pages | `Ch03_Software_Requirements.pdf`, 140 slides. Core teaching slides 2–120; MCQs 121–133; written exercises 134–140. Process: 2–5; feasibility: 10–15; interviews: 16–19; use cases: 27–81; analysis models: 82–100; SRS: 101–110; review/validation: 111–115; prototype: 116. | Course terminology, examples, diagrams, and slide-only details. Cite slide number when the exact item is slide-only. The MCQ slides have **no verified official answer key yet**. |
| Supporting textbook | B.B. Agarwal, S.P. Tayal & M. Gupta, *Software Engineering & Testing: An Introduction*, 2010 | Ch.3 printed pp. **53–84**, local PDF pp. **66–97**. Searchable text. | Selective gap-fill and cross-check only. Its process includes Requirements Management and uses **RDD** terminology in places; do not merge those differences into the K.K. course model without labeling the source. |
| Supplementary question patterns | `ASE_Ch1-3_Exercises_Aggarwal.md/.pdf`; MAIT tutorials; MRCET, GitHub/KPRIT, NRCMEC, and SEPM question banks | The compiled Ch.3 source-native exercises are printed pp. 134–138 in the K.K. book. Other files are separate sources. | The compiled exercise file mirrors the publisher exercises; cross-check against the book before answer writing. Other banks are pattern examples, not the instructor's bank and not authority for textbook claims. |
| SRS examples | Student-management template and project-report samples | `02_Raw_Materials/Aggarwal_Singh_Slides/SRS_and_Project_Samples/` | Illustrate document shape only; do not treat a sample's structure or requirements as a standard or as the course answer. |

### Source differences to preserve

1. **Requirements Engineering steps:** the K.K. course figure/text presents four steps—elicitation, analysis, documentation, review—with the problem statement as input and SRS as output. B.B. Agarwal et al. (2010) describes a five-part process that additionally names requirements management. Keep each model tied to its source; the four-step course sequence controls this chapter's answer unless the question explicitly asks for the 2010 text.
2. **Requirements document name:** K.K. course material uses SRS; the 2010 book uses RDD in parts of its requirements-process discussion. Do not silently treat the labels as interchangeable in a source-specific answer.
3. **Requirements types:** “known / undreamed / unknown”, functional/non-functional, and user/system requirements are separate distinctions. Do not turn them into one flat taxonomy.
4. **Historical standard:** course material names IEEE 830-1998. Preserve that as the course-era answer, but do not present it as the current standard. ISO reports ISO/IEC/IEEE 29148:2018 as current after its 2024 review; IEEE SA identifies the 29148 family as replacing IEEE 830-1998. This modern note is context only, not a reason to rewrite the exam answer. Sources: [ISO 29148:2018](https://www.iso.org/standard/72089.html), [IEEE SA 29148-2011 history](https://standards.ieee.org/ieee/29148/5289/).
5. **Feasibility content and historical statistic:** slides 11–15 support technical feasibility examples, realistic cost/schedule and business assumptions, market, major project risks, specification stability, prototype agreement, and plan adequacy. Slide 10 attributes 31% cancellations, 53% cost overruns averaging 189%, and 94 restarts per 100 projects to an IBM report, but gives no report citation/date. Do not present these as current universal rates; omit unless a question specifically asks about the slide's historical claim, then attribute it to slide 10.
6. **Slide numbering anomaly:** slides 132–133 repeat question label **3.23**; the last item is an API acronym MCQ. Preserve the source label in the audit record and use an internal unique identifier such as `MCQ-25`; do not silently claim the slide's printed number is 3.25.
7. **Written-exercise source discrepancy:** the companion slides and compiled exercise PDF list **35 stems** and jump from 3.24 to 3.26. The scanned textbook printed p.138 visibly contains **Exercise 3.25**: “Explain why, for large software systems development, is it recommended that prototypes should be ‘throw-away’ prototype?” Use the page image as its authority; include this book-only item in the 36-item textbook exercise inventory and do not claim it appears in the slides/compiled PDF.

## 4. Native material and question-type distribution

The companion slides contain **25 MCQ items** (slides 121–133; one duplicated printed label) and **35 written stems** (slides 134–140 / printed pp. 134–138). The scanned textbook adds Exercise 3.25 on printed p.138, giving **36 textbook exercise stems**. The distribution below counts the full 36-item textbook set; Exercise 3.25 is classified by its dominant “explain why” output.

| Dominant requested output | Stems | Share of 36 | Example source items |
|:---|---:|---:|:---|
| Define / explain / discuss / list / short note | 16 | 44.4% | 3.1, 3.5, 3.7, 3.10–3.11, 3.22, 3.25, 3.30–3.33, 3.35 |
| Compare / analyze / evaluate | 10 | 27.8% | 3.2, 3.4, 3.9, 3.16, 3.18, 3.27–3.29, 3.33, 3.36 |
| Draw a named model/diagram | 3 | 8.3% | 3.3, 3.12, 3.19 |
| Apply modeling to a stated system/case | 6 | 16.7% | 3.13–3.14, 3.20–3.21, 3.23–3.24 |
| Construct an example/specification | 1 | 2.8% | 3.34 |

Classification is exclusive by **dominant output**, not a count of every verb; several questions are multi-part. The percentages are not exam weights. Separate from this distribution, the 25 slide MCQs warrant a dedicated T1 pack. The written pattern supports a compact set of packs rather than a separate file for every verb:

1. **T1 MCQ** — all source items with independently checked answers; do not call the key official unless a publisher key is located.
2. **T2 Descriptive / Short Answer** — direct definitions, process steps, characteristics, lists, and “why/how”.
3. **T3 Compare / Analyze / Evaluate** — distinctions, communication breakdown, ambiguity, feasibility judgment, and prototype reasoning.
4. **T4 Diagrams / Modeling** — requirements-engineering process, use-case diagrams, DFD, data dictionary structures, and ER diagrams where the source asks for them.
5. **T5 Apply / Create** — library/railway/result/resource/hotel/airline scenarios, assumptions, and one inconsistent-SRS construction task. Fold low-count create tasks into the applied pack rather than making a thin standalone file.
6. **V3 Vocabulary Coverage** — instructor list, one usable answer per item, source pointers, and concise Arabic notes.

## 5. Diagram and visual inventory

Prioritize diagrams that explain or answer an in-scope item:

- Requirements-engineering process (K.K scan Figure 3.1, printed p. 41; slides 2–3).
- Feasibility checklist/focus (slides 13–15; risk identification is on slide 14).
- Use-case elements and examples (slides 28–35; worked system/use-case narratives continue through slide 81).
- DFD symbols/rules (slides 84–85), Level-0 context (slide 83), and decomposition/balancing example (slide 86); DFD exercise prompts on slides 137–138.
- Data-dictionary notation (slides 87–88).
- ER concepts and source diagrams for degree, binary, and ternary relationships (slides 89–95); exercises 3.15–3.19 and 3.24.
- SRS structure/characteristics (slides 101–110); validation/review (slides 111–115); prototyping (slide 116).

Do not copy text-only OCR as a substitute for reading diagram relations. For each selected visual, record source page/slide, meaning, redraw/extract decision, and render check.

## 6. Source-war and build sequence

1. Finish the per-topic coverage matrix in `00_INDEX.md`, using the instructor list as rows and the K.K printed pages/slides as evidence. Mark any source-only extras out of scope.
2. Finish a targeted scan of the 25 MCQs, all 36 textbook exercise stems (35 represented in slides/compiled handout, plus book-only 3.25), source-native figures, and relevant external question-bank patterns. Check the official K.K scan against the companion slides and retain the numbering anomalies above.
3. OCR the K.K. scan spreads locally for retrieval. Colab had no connected MCP and the CPU runtime was interrupted before completion; the local OCR completed on 2026-10-17 at 180 dpi. OCR is navigation only; scan images control claims and citations. The mixed final spread was clipped to the left half (printed p.138) to exclude Chapter 4 p.139.
4. Triangulate only confirmed gaps with one clearest supporting source. Candidate: B.B. Agarwal et al. (2010), especially SRS validation/characteristics and modeling; Pressman/Sommerville only if a named gap remains.
5. Author T1–T5 and V3 in source-native order, keeping answers complete but compact and omitting unrelated textbook depth.
6. For each printable pack, run the strict linter, export PDF, check answer cohesion and source leakage, and visually inspect changed pages/diagrams. Content verification, coverage, and visual checks are recorded separately.
7. Update this plan, `00_INDEX.md`, the local ASE source catalog/vector index, student decision log, daily session, and `ACTIVE_STATE.md` only as each state is genuinely reached. The index was merged locally without replacing Chapter 2: 296 Chapter 3 chunks added (91 scan OCR, 142 slides, 47 supporting textbook, 6 exercises, 10 vocabulary); total collection is 1,726 chunks across Chapters 2 and 3.

## 7. Resolution of open checks & verification gates

- **Printed-page mapping:** Confirmed across the complete K.K. scan printed pp. 40–138 (PDF spreads 26–75). Every exercise and section locator is tied directly to its physical printed page number.
- **Answer key verification:** Verified that neither the slide set nor the textbook provides an official solution key. All 25 slide MCQs were solved from first principles and triangulated against K.K. text and figures; 10 synthesis MCQs were added with full evidentiary rationales.
- **MCQ audit & numbering anomaly:** Audited all 25 slide options against high-resolution companion slide images. Slide 132 contains source item 3.24 (the flawed “not a functional requirement” question with three defensible non-functional options); slide 133 repeats label 3.23 for the API acronym item, internally identified as `MCQ-25`. Do not describe MCQ-24 as the Data Dictionary item.
- **“Risk Management Activities”:** Mapped to its exact course manifestation under Feasibility Study (slide 14: identifying and surmounting major project risks early) and highlighted in V3 Unit 06 and T2 Item 19.
- **Diagrams & Visuals (2026-10-21 print refresh):** The companion-slide PDF contains vector pages (zero embedded raster images on the inspected pages); selected originals were rendered at 4× into `source_figures/hires/` for sharper printing. T4 now uses original slides 3, 36, 83–86, 93–95, and 113–115 for fixed source diagrams. The custom use-case stereotype composite and M:N relational-mapping illustration remain because they address constructed relationships/mapping not presented as one matching source figure. Corrected stale labels: slide 82 is Requirements Analysis Steps, slide 87 is Data Dictionaries, and slide 91 is binary relationships—not the previously assigned DFD/ERD figure. A web search found the same third-edition source material hosted as a course PDF; it did not provide a distinct higher-quality figure file, so the local vector source was rerendered instead.
- **Delivery Gates & Cohesion:** All 6 Markdown deliverables pass `note_linter.py --strict`; their current PDFs are newer than the Markdown and total 63 pages, with no blank pages or leaked build directives. The combined print pack preserves the six-pack order and excludes the index. All 36 textbook exercises and 25 slide MCQs are mapped, all 7 instructor vocabulary areas are present, and seven applied drawing exercises have diagrams. T5 diagrams and the corrected Level-0/Level-1 DFD boundaries were visually reviewed. This cross-review is not a blind claim-by-claim audit of every statement. The 2026-10-21 direct-answer cleanup removed source-meta phrasing from T2/T4/T5/V3; it was a wording and print-economy pass, not a new source audit.
