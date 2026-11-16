# ASE Chapter 9 — Software Maintenance: Build Plan

**State:** Six course-source packs authored; print remediation completed and merged (2026-10-23). T2 D19 now states the scanned textbook’s 40–70% life-cycle cost share (printed p. 459), and D25 presents the seven Table 9.6 categories with direct wording and clean 1–7 numbering. T4 contains five concise prompts and six complete source-extracted figures; the Boehm and domain-mapping crops were corrected. T5/T7 Arabic academic notes remain in Markdown comments and do not print. All six packs pass `note_linter.py --fix --strict`; the rebuilt combined volume is 42 pages. **Scope remains provisional:** V9 is predictive until the instructor’s vocabulary/notes arrive, and student visual review remains open. Chapter 8 is tracked independently.

**Prepared:** 2026-10-23 · Codex-led parallel source review

## 1. Scope and authority

1. When received, Dr. Ali Fahim's exact vocabulary and lecture notes define the required scope. Keep their provenance and wording. Until then, use the predictive map only as a source-navigation aid.
2. The working course text is the scanned `AliFahim_Software_Engineering.pdf`, Chapter 9, printed pp. 459–491 (PDF spreads 235–251). Its title page is absent; identifying it as K.K. Aggarwal & Yogesh Singh, *Software Engineering*, 3rd ed. is a high-confidence inference from its structure and the matching publisher material, not a visible scan-cover fact. The scan has no text layer; OCR is navigation only. Inspect the page image for claims, page labels, equations, tables, and figure details.
3. The separate 75-page K.K. Aggarwal & Yogesh Singh publisher companion deck is not the narrative book. It is the course-aligned slide source and includes its own MCQs and exercises. Use the canonical file listed in `knowledge_sources.json`; do not index its identical mirror as independent evidence.
4. The scanned book's publisher answer key contains MCQ 9.1–9.25 on printed pp. 499–500 (PDF spreads 255–256), separate from the chapter text; printed p.492 already begins Ch10. Verify each option against the question before using the key; the answer letters alone do not explain a distractor.
5. Sommerville, Pressman, Mall, and Leach are selective support sources. Use only the clearest one for a confirmed in-scope gap or a materially clearer explanation. Do not combine different maintenance taxonomies as if they were identical.
6. External question banks are practice-pattern evidence only. They do not establish this instructor's scope, answer authority, or exam marks. No dedicated student seminar on Chapter 9 was found.

## 2. Source map

### Course text and companion slides

- **Scanned text:** printed pp. 459–491; PDF spreads 235–251. PDF spread 235 is mixed: its left page is the end of Ch08 (p.458), and its right page begins Ch09 (p.459). The last Ch09 spread contains pp.490–491. Printed p.492 begins Chapter 10. Do not treat p.458 or p.492 as Chapter 9.
- **Companion deck:** PDF/slide pp. 2–9 fundamentals, categories, effort and request distributions, maintenance problems and management; pp. 10–12 process; pp. 13–21 maintenance models; pp. 22–31 cost estimation; pp. 32–39 regression testing; pp. 40–53 reverse engineering/reengineering; pp. 54–58 configuration management; pp. 59–63 documentation; pp. 64–69 MCQs 9.1–9.25; pp. 70–75 exercises 9.1–9.40.
- **Question inventory:** 25 publisher MCQs, with a scanned publisher answer key; 40 publisher exercises. These are source counts, not exam weighting.

### Targeted supporting sources

- Sommerville 9e, Ch.9 *Software Evolution*, printed pp. 234–259 / PDF pp. 251–276: evolution/change process, Lehman dynamics, maintenance and legacy-system management.
- Pressman 5e, Ch.30, printed pp. 799–822 / PDF pp. 827–850: reengineering, reverse engineering, restructuring, forward engineering, and economics. Its taxonomy also appears in Ch.2, printed p.23 / PDF p.51. Treat old cost statistics as historical, not current.
- Rajib Mall 4e, Ch.13, TOC printed pp. 494–502 / PDF pp. 659–669: maintenance characteristics, reverse engineering, process models and cost estimation. The converted PDF has no visible printed page labels; do not infer a one-to-one offset.
- Leach 2e, Ch.8, printed pp. 335–352 / PDF pp. 363–380: maintenance/evolution, request-response handling, understanding and life-cycle cost. Its three-category taxonomy omits perfective maintenance; do not substitute it for the course taxonomy.

## 3. Predicted vocabulary use

See `V9_Predictive_Vocabulary.md`. The strong predictions follow the course deck's major headings and exercise clusters. Lower-confidence branches are separated. No predicted term is an official requirement until the instructor list arrives.

The student has authorized construction using the available chapter material while the actual instructor list is unavailable. Use the following provisional pack set; if the official list arrives during construction, reconcile it before exporting. Keep counts proportional to real coverage, not to a target page count:

- **T1 MCQ:** the 25 publisher questions; key check against scanned pp. 499–500.
- **T2 Descriptive:** definitions, process steps, categories, models, tools, documentation, and short explanations from the 40 exercises.
- **T3 Compare/Analyze:** only distinct comparisons and causal questions; merge overlaps rather than repeat one idea across packs.
- **T4 Diagrams/Forms:** selected source figures and the change-request form, if required by the vocabulary or exercise coverage.
- **T5 Apply/Select:** maintenance decisions, regression-test selection, legacy-change recommendations, and configuration/document choices where a prompt supports them.
- **T7 Calculations:** Belady–Lehman and Boehm ACT/AME work if those models remain in scope. Use the shared numerical-answer protocol and an equation register.
- **V9 coverage:** replace the predictive status with the received instructor list and map every item to an actual answer, not merely a source locator.
- **T6 Create:** do not create a separate pack unless the instructor list or a genuine unique task requires one.
- **No duplicate-by-format rule:** assign each distinct learning target a primary home; repeat a source question in another pack only when it tests a genuinely different action or working form. Add original questions only for uncovered, source-supported concepts; mark publisher wording and authored wording distinctly in Markdown metadata/source lines.

No percentage of likely exam marks is inferred. Exercise counts and proposed pack types are coverage inventory only.

## 4. Diagram and figure policy

The slide deck identifies these source-figure candidates: maintenance-effort distribution (slide 5); maintenance process (10); quick-fix (13); iterative-enhancement cycle (15); reuse model (17); Boehm model (19); Taute model (20); regression code/test examples (35–36); reverse-engineering application/domain and abstraction-level figures (42, 45); new-development versus reengineering (48); restructuring (52); and change-request form (58).

Before selecting a figure, inspect both the original book scan and companion slide at print size; retain the clearest complete source version and cite its actual book page or slide. Fixed figures should be extracted, not redrawn. If a prompt requires a new case-specific diagram/form, draw only the requested model using its proper notation and place any explanation in the answer outside the figure. OCR captions do not validate diagram meaning.

## 5. High-risk verification items

- **Taxonomy drift:** the course sources and support texts use different category groupings. Preserve the course wording when it appears; explicitly distinguish secondary terminology instead of merging labels.
- **Effort distributions:** the deck's four-category chart and the scanned book's Lientz–Swanson survey table measure different things. Attribute each figure/table to its source; do not combine or generalize the percentages.
- **Numerical example 9.2:** companion slide 28 states `10 × 90 = 90 PM`, but the scan image (printed p.472, PDF spread 242) clearly states `10 × 90 = 900 PM` and `600 + 900 = 1500 PM`. The scan resolves the slide typo and arithmetic. Preserve 900 PM if this example is used; do not copy the slide's wrong intermediate result.
- **Formula rendering:** the deck's text layer loses superscript layout in `M = P + K e^(c-d)`. Confirm the exponent and every variable from the source image. Check units, assumptions, and arithmetic independently; record the formulas used and affected examples.
- **Historical claims:** maintenance-effort percentages, survey figures, and old cost claims need their original sample/context. Do not state them as current universal facts.
- **Question wording:** preserve the student's direct-answer style. No “the book says/author says” inside answers; put locators on a separate source line. English questions/answers, brief Arabic notes only when useful.

## 6. Compact print rules carried forward

- Do not print curriculum-mapping tables, obvious “how to use this file” notes, long introductions, or redundant answer labels. Keep such navigation in Markdown comments or planning files.
- Do not add obvious trap/fact callouts; keep only a short Arabic note when the question itself is genuinely ambiguous or a common misconception materially matters.
- Minimize forced page breaks and excess whitespace. Keep the answer directly under its question in the same pack; visual page-flow choices can be reviewed by the student.
- Build individual PDFs for the justified packs, then produce one combined Chapter 9 print PDF in the established chapter order. Do not merge internal source maps, curriculum-coverage tables, or obvious-use instructions into the print bundle. Keep the full coverage map in Markdown for navigation; a standalone vocabulary-coverage PDF may be printed only after the real instructor list arrives.

## 7. Handoff and completion gates

Before pack construction: check once for the instructor's exact Chapter 9 terms/notes. They are not currently available; do not block the work waiting for them. Use the predicted map only as a provisional navigation aid, build from the actual course text/slides/exercises, and leave V9 labeled predictive. If the official terms arrive before export, reconcile the packs against them. Inspect the scan and relevant slides; choose support sources only for demonstrated gaps; finalize the source/question/figure map.

Before calling the chapter ready for the student's visual review: every selected predictive/course topic has a usable English answer; publisher questions are not duplicated without a reason; formula solutions are independently recalculated; fixed diagrams are original-source extracts with verified semantics; all sources/pages are distinct and correct; compact component PDFs and the combined print PDF match Markdown and are visually checked. Describe scope as course-source coverage with provisional instructor-vocabulary coverage, not as confirmed completeness. The student retains the final visual review. Chapter 8 remains open independently of Chapter 9.
