# Chapter 9 Software Maintenance — Word Seminar Source and Style Plan

**Status:** Predictive Chapter 9 Word seminar, items 1–9 expanded from the course scan/deck, Agarwal et al., and selective audits of Sommerville, Pressman, Mall, and Leach; 56-page Word render visually reviewed; official vocabulary/lecture notes remain pending.  
**Date:** 2026-10-24  
**Scope status:** Predictive. Dr. Ali Fahim's official Chapter 9 vocabulary and lecture notes have not been located.  
**Deliverable type:** Microsoft Word seminar, following the existing Chapter 5 Design and Chapter 7 Reliability Word work. The six-pack, 42-page Chapter 9 study-print PDF is a separate artifact, not the seminar.

## 1. Decision boundary

This file records the source evidence and current seminar decisions. The predictive vocabulary is a navigation aid, not an instructor-approved syllabus. When the official list arrives, map its exact terms first and reconcile the draft. Until then, retain the predictive label, do not claim confirmed coverage or infer exam weights, and let source evidence—not a page target—determine the depth.

The linked shared chat contains prior authorization to create Chapter 9 study packs from available course sources while the instructor list was missing. That authorization explains the existing six packs; it does not turn the predictive list into confirmed scope. The seminar is a separate Word deliverable; the six-pack print PDF is retained as a distinct artifact.

## 2. Shared-session review and current local state

The supplied shared ChatGPT session was read through its rendered conversation text: 440,651 characters across 6,720 lines. Its useful Chapter 9 history includes the predictive vocabulary forecast; explicit source and figure verification instructions; multiple rounds of T1–T7 audit and repair; the 42-page merged-print result; and the repeated warning that instructor vocabulary remains pending. The latest shared-session report describes Chapter 9 study packs as ready for the student's print review, not methodologically closed.

Some numerical memory in that conversation is historical and must not be reused as current state: 310 Chapter 9 chunks / 4,007 total and later 4,155 total were superseded. The live local index reports 4,140 chunks, built 2026-10-23T17:19:24Z, using `intfloat/multilingual-e5-small`. Its source inventory includes Chapter 9 plan/index/atlas and T1–T5/T7 files, the course scan and answer-key OCR, the canonical companion deck, all four targeted supporting books, and practice-only question-bank material. A focused semantic search returned source passages from the official deck, scanned book, and Mall; those results were treated as navigation, then checked against primary page images where possible.

Current local state:

- `Ch09_Software_Maintenance_Print.pdf` is the six-pack, 42-page print volume. It is not a Chapter 9 seminar.
- `Ch09_BUILD_PLAN.md`, `V9_Predictive_Vocabulary.md`, and `V9_SOURCE_ATLAS.md` are internal preparation artifacts.
- The Chapter 9 Word seminar covers the nine-cluster predictive map in `05_Seminars_&_Slides/Ch09_Software_Maintenance_Seminar.docx` (56 pages including cover and contents after the source expansion below).
- The official Chapter 9 vocabulary/notes are still pending.
- The atlas header still said 55 pages even though the current build plan, live state, and PDF identify 42 pages; this stale count is corrected with this plan.

## 3. Source authority and use

| Rank | Source | Verified boundary | Planned role and limits |
|:--|:--|:--|:--|
| 1 | Scanned course text, `AliFahim_Software_Engineering.pdf` | Chapter 9, printed pp. 459–491; PDF spreads 235–251. The scan cover is absent, so the Aggarwal & Singh 3rd-edition identity is a high-confidence inference, not a directly visible title-page fact. | Primary narrative authority. OCR is for navigation. Inspect the original image for figures, numbers, tables, equations, and any disputed wording. Exclude p.458 (Chapter 8) and p.492 onward (Chapter 10). |
| 2 | Canonical Aggarwal & Singh companion deck, `Ch09_Software_Maintenance.pdf` | 75 pages; content pp. 2–63, publisher MCQs pp.64–69, exercises pp.70–75. | Course-aligned organization, diagrams, prompts, and corroboration. It is a separate companion source, not an independent textbook edition. Use the source image for figure meaning. |
| 3 | Sommerville, *Software Engineering*, 9th ed., Ch.9 | Printed pp. 235–260 / PDF pp. 251–276. | Selective support for evolution/change processes, maintenance, and legacy systems when a confirmed term needs more explanation. |
| 4 | Pressman, *Software Engineering: A Practitioner's Approach*, 5th ed., Ch.30 | Printed pp. 799–822 / PDF pp. 827–850; its maintenance taxonomy also appears in Ch.2, p.23 / PDF p.51. | Selective support for reverse engineering, reengineering, restructuring, forward engineering, and economics. Keep taxonomy and old cost statistics contextualized; do not merge taxonomies. |
| 5 | Rajib Mall, *Fundamentals of Software Engineering*, 4th ed., Ch.13 | TOC printed pp. 494–502 / chapter body PDF pp. 659–667. The converted copy does not show reliable printed folios throughout. | Selective process/model/reverse-engineering support. Cite stable PDF locators where printed-page mapping is unavailable; verify each specific passage before use. |
| 6 | Ronald J. Leach, *Introduction to Software Engineering*, 2nd ed., Ch.8 | Printed pp. 335–352 / PDF pp. 363–380. | Selective support for maintenance/evolution, request-response handling, system understanding, and life-cycle cost. Its three-category taxonomy omits perfective maintenance; never substitute it for the course's four-category account. |

External question banks remain practice-pattern material only. They do not establish course scope, answer authority, or likely marks. New external literature or standards should be added only if an instructor-confirmed term leaves a real gap; any such academic reference must be verified and carry a resolvable DOI per the vault policy.

## 4. Primary-page visual review completed

The original scan was visually reviewed spread by spread across PDF spreads 235–251, covering printed pp. 459–491 (spread 235 also contains p.458, the end of Chapter 8). The table below records selected high-risk details from that complete visual pass; it is not the full inventory of observed content.

| PDF spread | Printed pages | Directly observed |
|:--:|:--:|:--|
| 235 | 458 / 459 | Mixed boundary: the left side ends Chapter 8 at p.458; Chapter 9 starts on the right at p.459. |
| 237 | 462–463 | §9.1.3 describes maintenance as manageable; Table 9.1 distributes effort across eight named activity types; Table 9.2 lists request types; §9.1.4 discusses budget/effort reallocation, replacement, and maintenance of the existing system. These survey figures need their original context and must not be presented as universal current rates. |
| 242 | 472–473 | The ACT example visibly computes `10 × 90 = 900 PM` and total effort `600 + 900 = 1500 PM`; the companion slide's `90 PM` is a typo. Regression-testing material begins on p.473. |
| 243 | 474–475 | Selective retest, regression-suite selection, coverage/minimization/safe categories, and evaluation criteria are present. |
| 248 | 484–485 | Software versions distinguish revisions from variations; §9.8.3 describes change control through a Change Control Authority (CCA), QA revalidation, and configuration incorporation; Fig.9.14 is the change-request form. The inspected original form has 18 labeled fields and names CCA. The existing `CH09_FIG14_Change_Request_Form.png` crop matches the source form's field labels. |
| 251 | 490–491 | The chapter's exercise set begins on p.490 and continues through 9.40 on p.491; the same spread also contains publisher MCQs. This confirms the exercise boundary and guards against the prior p.490/p.491 locator mix-up. |

The scan review also covered the maintenance definition and effort ranges, the four maintenance types, problems and management responses, four-phase maintenance process, five models, estimation examples, regression selection, reverse engineering, tools, legacy systems, restructuring, SCM, the 18-field Change Request form, documentation tables, and end-of-chapter questions. Two high-risk corrections were verified directly on the page images: preserve the 900 PM ACT intermediate calculation and retain the four phases shown in the maintenance-process diagram. Figure 9.8 on printed p.481 was also checked directly; its comparison image is captioned as Figure 9.8, not Figure 9.12.

## 4.1 Agarwal Chapter 9 visual review

The assigned textbook *Software Engineering and Testing: An Introduction* by B. B. Agarwal, S. P. Tayal, and M. Gupta was visually reviewed on PDF pp.206–220 (printed pp.193–207). Its maintenance discussion runs through printed p.206; printed p.207 begins §9.9, Software Project Estimation, and was checked to establish the boundary. The pass covered Lehman’s laws; SCM activities, controlled/pre-controlled/uncontrolled items, reservation and baselines, status accounting, configuration audit, versions/releases, change-control questions, maintenance task lists and examples, cost shares, ten effort factors, Belady–Lehman/ACT/AME estimation, and regression testing. Figures 9.1, 9.2, 9.5 and 9.6 were extracted from their original pages and checked against the page images. Figure references in the seminar preserve Agarwal’s printed locators and are not merged with the scanned course chapter’s taxonomy.

## 5. Provisional topic architecture for planning only

These nine clusters are the current predictive map, not a confirmed list of seminar headings:

1. Maintenance meaning, purpose, categories, effort, and manageability.
2. Maintenance problems, management responses, and maintenance-versus-replacement decisions.
3. Maintenance process, program understanding, maintainability, ripple effects, coupling, and testability.
4. Maintenance models: quick-fix, iterative enhancement, reuse-oriented, Boehm, and Taute.
5. Maintenance effort/cost estimation: defect-repair ratios, Belady–Lehman, ACT/AME, and EAF examples.
6. Regression testing, selective retest, and test-selection evaluation criteria.
7. Reverse engineering, reengineering, legacy systems, and restructuring.
8. Software configuration management, versions, change control, CCA, and the source change-request form.
9. Software documentation and maintenance tools.

When the instructor list arrives, retain only its confirmed terms and necessary explanatory branches, while keeping source-supported corrections and distinctions. Until then, do not promise that these clusters are the doctor's scope.

## 6. Figure and table candidates

Potential source assets from the scan/deck maps include the maintenance-process diagram; quick-fix, iterative-enhancement, reuse, Boehm, and Taute models; regression-selection examples; reverse-engineering abstraction/domain-mapping diagrams; new-development versus reengineering; program restructuring; and the Change Request Form. The existing diagram folder contains crops for several candidates, but their presence alone is not proof of source fidelity. For each selected asset:

1. inspect the exact textbook page and companion slide;
2. verify caption, labels, arrows, stage count, and branch direction against the original;
3. use the clearest complete source extraction instead of redrawing a fixed source figure;
4. add a concise figure caption and keep source attribution in the caption or the seminar's agreed front matter, not as repeated inline reference links;
5. omit any figure that does not directly support confirmed vocabulary or a required exercise.

The seminar uses selected course figures and the Agarwal configuration-control, status-accounting, version-evolution, and deployment-environment figures after visual comparison with their source pages. A final layout pass caught and corrected image defects: the Taute crop included stray neighboring caption text; the course Figure 9.8 comparison crop was clipped and its seminar caption had separated from the image; and the Agarwal Figure 9.5 crop cut off the rightmost version node. The corrected direct-source crops preserve the complete figures, and the builder keeps each caption with its image. The expanded 56-page render also includes complete Leach request/response forms, Leach concurrency figures, and Sommerville maintenance-prediction, reengineering, and legacy-assessment figures; source-page locators remain in figure captions.

## 7. Word seminar style and production workflow

The deliverable is a Word document, following the established Design/Reliability seminar rather than Marp/PPT. The reviewed Word work uses a formal English academic narrative, a cover and navigation front matter, a table of contents, section numbering beginning at 1, embedded source figures/tables, and deliberate page distribution. It avoids source hyperlinks and repetitive citations in the body; source checks and full locators stay in this internal coverage plan, with concise figure attribution where a fixed figure is reproduced.

Before authoring, inspect the current Ch.7 `build_doc.py`/`finalize_docx.py` workflow and the canonical Ch.8 Word file's structure rather than assuming the old exporter still has the same behavior. Build from one editable source, refresh Word fields/TOC, export a PDF, and visually inspect the whole rendered document for section order, figure/table integrity, page flow, headings, and final-page completeness. Keep any intermediate outputs clearly marked and preserve the canonical source until a new render passes review. This file is the internal source/coverage plan; the seminar itself is the separate Word artifact.

## 8. Pre-draft gates

- Check once for the official Chapter 9 term list/lecture notes and record the result. If absent, preserve predictive scope explicitly; item 1 is authorized as a predictive draft and must not be represented as confirmed scope.
- Map each confirmed vocabulary item to the course scan and canonical slide/page before writing; note exactly what the primary material does and does not cover.
- Check all four support books selectively for only demonstrated explanatory gaps; do not blend conflicting terms or taxonomies.
- Keep source claims separate from original examples/interpretation in the internal source ledger.
- Independently recalculate every included model/example, verify variables/units/assumptions from source images, and disclose the slide-28 arithmetic typo if that example is used.
- Compare every fixed diagram/form with its original source and validate labels/stages. No trace of an unverified crop is treated as verified content.
- The student has now reviewed the plan and authorized predictive item 1. For each next item, map the instructor vocabulary if it has arrived; otherwise use the predictive map transparently, verify the primary-page coverage and supporting-source value, and let the evidence determine length.

## 9. Source limits and pending scope

- The course scan title page is missing. The Aggarwal & Singh bibliographic identity is high-confidence inferred from the chapter structure and matching publisher companion materials.
- OCR is not an authority for the scan's equations, diagram semantics, exact numerals, or page boundaries.
- The scanned course chapter and Agarwal maintenance pages described above were visually reviewed in full. The four other assigned textbooks were consulted selectively for demonstrated explanatory gaps; this record does not claim a page-by-page visual audit of their complete chapters.
- The linked shared session and the vector index are navigation/history aids. They do not replace current source-file/page verification.
- Official Chapter 9 vocabulary and lecture notes remain unreceived.

## 10. Predictive item 1 drafted and checked

**Item:** Software Maintenance — meaning, purpose, categories, effort, and manageability. The student authorized beginning with the first predictive vocabulary item on 2026-10-24; this does not confirm the remaining prediction map or replace the pending instructor vocabulary.

**Coverage:** The six-page Word file begins with section `1` and develops the post-delivery scope, maintenance triggers, four course-aligned purposes, taxonomy differences across the four supporting texts, the primary effort-distribution figure, the separate eight-row activity survey, the chapter's manageability argument, a careful survey-statistic qualification, an operational synthesis, and an original classification example. It separates the textbook's treatment of preventive maintenance as an “other type” from the companion slides' four-category presentation. The extracted Figure 9.1 is a direct crop from the original scanned course page (printed p. 461); the visual's percentages and labels were checked against the source image.

**Source audit for this item:** Primary scan pp. 459–463; companion deck maintenance slides; selected passages from Sommerville 9e Ch. 9, Pressman 5e Ch. 2, Mall 4e Ch. 13, and Leach 2e Ch. 8. Their non-identical taxonomies were kept distinct. Course sources govern the seminar. The scan lacks its title page; bibliographic identity remains unasserted in the deliverable.

**Style and verification:** Compared the established Chapter 7 builder and Chapter 8 Word heading hierarchy. The item follows their formal English, Times New Roman body, 1-inch side margins, numbered hierarchy starting at 1, source figure captioning, and Word format. LibreOffice is unavailable on this Windows host, so Word itself exported the review PDF; every one of the six rendered pages was visually inspected after the final edit. The source DOCX remains editable; the separate PDF/PNGs are QA-only and are not deliverables.

**Next at the time of that audit:** Continue with predictive item 2, maintenance problems, management responses, and maintenance-versus-replacement decisions. This was superseded by the completed full predictive draft below.

## 11. Predictive items 1–9 assembled and visually reviewed (first draft, superseded)

**Coverage:** The Word draft now includes all nine predictive clusters: (1) maintenance fundamentals; (2) maintenance problems and management responses; (3) the maintenance process and maintainability; (4) Quick-Fix, Iterative Enhancement, Reuse-Oriented, Boehm process, and Taute models; (5) relative repair effort, Belady–Lehman, ACT/AME, and EAF examples; (6) regression and selective retesting; (7) reverse engineering, reengineering, legacy code, and restructuring; (8) SCM, versions, CCA, and the original 18-field change-request form; and (9) user/system documentation and course-named tools.

**Source corrections preserved:** ACT uses additions plus deletions; Example 9.2 computes 10 × 90 = 900 PM; Belady–Lehman M remains total effort; Boehm process and ACT/AME models remain distinct; regression selection limits are qualified; and source taxonomies are not merged. The one-person-organization exercise is bounded because the course prompt does not provide a separate model answer.

**Figures and layout:** Direct course-text figures used include 9.1, 9.2–9.9, and 9.10–9.14 as applicable to the predictive clusters. Crops were checked against the available scanned pages; the iterative, reuse, Taute, and regression-test-case crops were tightened to exclude surrounding page text. Section heading/list numbering starts at 1 and consecutive lists restart at each new list. The Word TOC was refreshed with Microsoft Word.

**Verification at that stage:** Word exported a 31-page review PDF and it was inspected in rendered contact sheets. This first draft lacked the full Agarwal Chapter 9 expansion described below and is superseded by the 38-page expanded draft and then the final 39-page image-corrected version. The source chapter and deck govern the predictive draft; support-text taxonomies remain distinct.

**Next at that stage:** Hold Chapter 9 as a prepared predictive draft pending official vocabulary. This is superseded by the latest record below.

## 12. Full visual audit and first expanded Word draft

The student challenged whether Agarwal and the scanned chapter had actually been inspected visually and asked for much greater textual depth. In response, the scanned course chapter was reviewed across every physical spread from 235 through 251 (printed pp.459–491, with p.458 excluded from Chapter 9). Agarwal et al.’s Chapter 9 maintenance coverage was reviewed across PDF pp.206–220 / printed pp.193–207; the beginning of §9.9 on p.207 establishes the chapter boundary. OCR or extracted text was used for navigation only; diagrams, examples, tables, labels, and page boundaries were verified on the rendered page images.

The seminar was expanded from 31 to **39 pages**. The added source-grounded discussion covers Agarwal’s three Lehman laws and maintenance task/reason lists; distinct maintenance effort ranges; the ten maintenance-effort factors; test-case status and selective retesting; Rigi/ReFine tool functions; legacy-system and restructuring distinctions; SCM’s three-activity organization versus the course’s four activities; controlled-item status, reservation, baselines, accounting, audit, versions/releases, CCA versus CCB, and change-management questions; configuration figures; and user/operator/maintenance documentation audiences. These are academic restatements grounded in the sources rather than long copied passages. The course chapter remains the controlling source for course terms; differences between the two books are stated rather than blended.

**Verification at that stage:** Microsoft Word exported a 39-page review PDF. This stage was superseded by the source expansion in §13; its image fixes remain in the current builder.

**Current status:** Predictive vocabulary only. Dr. Ali Fahim’s official Chapter 9 vocabulary and lecture notes remain pending. When received, reconcile the exact list against the nine clusters and preserve verified source distinctions and calculations.

## 13. Cross-source expansion and 56-page Word render

The student requested deeper source-first development and allowed the document to exceed the earlier approximate 70-page ceiling only if the source content justified it. The seminar was expanded where distinct material was available, without padding repeated explanations. Added material includes: Sommerville's evolution/servicing/phaseout distinction, eight scoped Lehman observations, maintainability economics, change-demand indicators and four operational prediction metrics, and legacy-system portfolio matrix; Leach's twelve maintenance triggers, its taxonomy mismatch, problem triage and the complete request, response, and combined forms, the bounded 44% parser case, race conditions, and non-atomic resource access; Pressman's process/data/interface recovery, reengineering activity boundaries and economic variables; Mall's behavior-preserving cleanup before recovery, two process models and context-qualified ~15% rework observation; and Leach's IMP-8 case with the source's operational, code-size, module, complexity, and duplicate-file figures. Source categories and disagreements remain explicitly separate.

**Source-specific visual review:** the four support books were audited selectively, not page-by-page in their entirety. Leach Figures 8.2–8.4 were extracted from rendered pages 340–342 and checked as complete forms; Figures 8.5–8.6 were checked on printed pp.345–346. Sommerville Figures 9.10, 9.11, and 9.13 were extracted from rendered source pages and checked for all labels, arrows, and quadrants. Pressman and Mall additions were checked against their local chapter extractions and the audit notes; no claim is made that every page or figure in those books was visually reviewed.

**Current QA:** the DOCX builder is `03_Study_Notes/Ch09_Software_Maintenance/build_ch09_seminar.py`. Microsoft Word refreshed the TOC and exported the latest review PDF; the PDF reports 56 Letter-size pages including cover and contents. Rendered page PNGs and contact sheets cover all 56 pages in `Ch09_QA_expanded_v1/` for internal QA only. Every page was reviewed in the complete contact-sheet pass; pages with newly added figures, tables, and source forms received closer inspection. The original course and Agarwal figures retained from the 39-page version remain in place. Page count is below 70, but it is not a target. The seminar text is source-grounded academic restatement with selected exact technical labels and values; it does not reproduce long copyrighted passages verbatim.

**Pending:** official vocabulary/lecture notes; reconcile the predictive headings and scope when Dr. Ali Fahim provides them. No inference about confirmed coverage or exam weighting is made.


