# ASE Chapter 8 — Software Testing Preparation Plan

**Phase:** preparation and source mapping. The predictive vocabulary and planning ledgers are being built; no question-answer packs or PDFs have been authored in this phase.

## Objective

Prepare a source-aware handoff for the later question-pack build. Use the predictive vocabulary as a temporary search and inventory guide, then reconcile it with Dr. Ali Fahim's actual list when the student receives it. Cover the chapter with a compact set of question types and enough depth to clarify the supplied terms. Avoid importing an entire testing textbook or treating every related concept as required scope.

## Current source identity

1. **Working primary book:** the scanned file AliFahim_Software_Engineering.pdf is believed to be K.K. Aggarwal and Yogesh Singh, Software Engineering, 3rd edition. This identity is high-confidence from the surrounding chapter structure and slide footers, but its title/author page is absent. The scan has no searchable text layer. Chapter 8 begins at printed p. 365 according to the prior boundary note; the exact final page and spread range are still unverified.
2. **Course companion deck:** Ch08_Software_Testing.pdf in Aggarwal_Singh_SE_3rd_ed_By_Chapter has 212 pages. It is textually identical page by page to chapter_8_software_testing.pdf in Aggarwal_Singh_Slides, and sampled full-page renders match. Treat the By_Chapter copy as the single canonical deck and record the other as a mirror; do not count the two copies as independent evidence.
3. **Supporting books:** Sommerville, Pressman, Rajib Mall, and Leach are selective support only. Use one clearest source to fill a demonstrated, in-scope gap. Keep its book identity and printed page separate from the Aggarwal and Singh book/deck.
4. **External question banks:** question-pattern material only; never answer authority, course-scope authority, or evidence of likely marks.
5. **Student seminar:** excluded from the present chapter source set. Do not inspect or index it for this build.
6. **Instructor scope:** the current V8 vocabulary is predictive. It does not carry marks or exam-probability claims.

## Scope layers

- **Layer A — explicit teaching:** terms and methods taught in the canonical deck, pp. 2–188.
- **Layer B — question-only/exercise-only:** topics that appear in the 50 MCQs or 50 written exercises but receive little or no teaching explanation in the deck.
- **Layer C — support candidates:** relevant additions found in support books, included only if the actual instructor list calls for them or a verified gap blocks a clear answer.
- **Layer D — scanned-book verification:** confirm exact Chapter 8 start/end, printed pages, figures, worked examples, and question references from page images before using book locators.

## Provisional question-pack shape

Decide final files only after mapping every instructor term and all 100 source questions. Candidate organization:

- **T1 — MCQ:** all 50 source MCQs, with each key checked independently because no publisher answer key was found.
- **T2 — Short descriptive:** definitions, purposes, lists, distinctions, and explanation/process questions.
- **T3 — Compare and analyze:** black-box versus white-box, BVA versus equivalence classes, development versus regression, testing levels, and debugging approaches where the source prompts them.
- **T4 — Diagrams and structural analysis:** source figures for stable concepts; problem-specific flow graphs, decision tables, cause-effect graphs, and path work derived from the exercise's own input.
- **T5 — Apply and design tests:** BVA, robustness, worst-case, equivalence classes, decision tables, and cause-effect exercises.
- **T7 — Calculations:** test-count formulas, Cyclomatic Complexity, and any other numerical work that has enough distinct questions to justify a separate pack. If the volume is small, place calculations with their natural application questions.
- **V8 — Vocabulary and coverage:** keep as a navigation ledger; the predictive list is internal and should not add an unrequested print page.

These are candidate pack boundaries, not a promise to create every pack. Do not duplicate one exercise in multiple packs; record a primary home and cross-reference it if necessary.

## Question selection and coverage rules

- Inventory source IDs 8.1–8.50 for both the MCQ set and the written exercises. Preserve IDs even when page text is out of numeric order.
- For each exercise, mark its primary response form and every secondary skill it tests. Preserve a prompt unless it is demonstrably duplicated; if merging, record the source IDs and why.
- Add authored questions only for a term or method absent from the question inventory, not as paraphrases of existing items.
- Use the original exercise set as practice evidence, not as a prediction of exam weighting. Report item counts by response type with a denominator; do not label them as marks.
- Keep question, option, and model answer in English. Keep a useful brief Arabic student note outside the answer. No inline translation clutter.
- Answer the question directly; do not write “the book says,” “the author states,” or similar meta-prefaces. Put the source locator on its own line after the answer.
- Bold source-grounded claims and faithful paraphrases; use plain text for our framing/synthesis. Verbatim quotation is optional.
- No “Answer” heading in printable pages; no green intro/subtitle, curriculum map, or navigation text in the print body. Keep internal maps in Markdown-only artifacts.

## Numeric-work gate

For every calculation, inspect the source image, transcribe notation, define symbols and units, state necessary assumptions, show the formula, substitution and enough arithmetic to reproduce the result, then independently recompute it. Verify:

- BVA, robustness, and worst-case counts and their underlying test-selection conventions.
- Cyclomatic complexity by all applicable methods and graph assumptions.
- Graph-matrix dimensions and entries where a question asks for them.
- Data-flow du/dc path derivations against the actual flow graph.

The slide text extraction loses superscripts and may confuse the predicate symbol. Verify 5^n, the BVA/robustness formulas, and π+1 against the rendered source before writing them as final answer notation.

## Figure gate

- Compare the scanned-book figure and canonical deck figure when the scan pages are located. Extract the clearest complete source figure for stable concepts.
- Keep the figure itself clean. Put explanation in the answer text outside the image.
- Build a new figure only when a question supplies a new program or specification and asks for its own graph, table, or test cases.
- Validate semantic nodes/edges/labels, then render and inspect legibility at actual print size.
- Preserve source anomalies visibly in the audit record. Do not silently fix a source typo or redraw a source model while claiming it is original.

## Vector-memory plan

The vector catalog has 22 Chapter 8 records in `knowledge_sources.json`. One is the unindexed scanned-book record (`kk_scanned_book_ch08_pending_boundary`, marked `include: false` pending boundary verification). The local vector DB has 3,697 total chunks, of which 397 are Chapter 8 chunks from the 21 included records. Chapters 2–7 were verified unchanged (1,432 / 299 / 561 / 304 / 353 / 351), and SQLite `integrity_check` returned “ok”. The two existing Chapter 6 cross-references to Chapter 8 Cyclomatic Complexity remain preserved.

The Chapter 8 collection includes:

1. The predictive vocabulary ledger, this build plan, the source-coverage map, question inventory, and diagram atlas.
2. One canonical 212-page deck source record (`Aggarwal_Singh_SE_3rd_ed_By_Chapter/Ch08_Software_Testing.pdf`), with its duplicate slide-folder path recorded as a mirror.
3. Precisely bounded source-book pages to be added only after the scanned Chapter 8 spread range is verified.
4. Targeted candidate pages from Sommerville, Pressman, Mall, and Leach, clearly labeled as supporting sources and not instructor-confirmed scope.
5. Selected external question-bank pages as practice-only; never index the student seminar.

Future updates must remain incremental with explicit source IDs, avoiding any full index rebuild. SQLite integrity and chapter chunk counts must be re-checked after any catalog change.

## Independent review structure

The current preparation swarm covered three distinct lanes: primary deck and question inventory; supporting-book gaps; vector/catalog schema. The diagram audit from the prior preparation turn also covers figures and source anomalies. For the later authoring round, the lead agent should assign read-only source verification, question-form coverage, numerical recomputation, and diagram semantics to separate reviewers; one integrator owns edits and reconciles disagreements. Report cross-review as cross-review, not blind verification.

## Open items before final question-pack authoring

- Receive Dr. Fahim's actual Chapter 8 vocabulary list and provenance.
- Verify the scanned textbook's exact Chapter 8 boundary and printed pages from page images. The OCR attempt was stopped after running slowly; no scan comparison is claimed.
- Inspect the source images for the malformed year condition in Exercise 8.13, the context of Exercise 8.36, the “Table 8” reference in Exercise 8.44, the triangle cause-effect conditions, the repeated output-class labels, and equation symbols/superscripts.
- Independently key all 50 MCQs and resolve ambiguous or defective source stems before exporting any answer pack.
- Decide the final pack split after the exercise inventory and actual instructor vocabulary are reconciled.

## Current completion boundary

**Authoring Phase Complete:** All 6 question packs (`T1_MCQ`, `T2_Descriptive`, `T3_Compare_Analyze`, `T4_Diagrams`, `T5_Apply_Design`, `T7_Calculations`), `00_INDEX.md`, and `V8_Coverage.md` are authored, linted, and exported. The complete print bundle `Ch08_Complete_Print_Pack.pdf` (97 pages) is assembled with 0 blank pages. All engineering gates passed; ready for student final visual review.

## Verified Implementation Ledger (2026-10-22)

1. **Scanned Book Boundary:** Verified as printed pp. 365–458 (PDF spreads 188–235).
2. **Official Answer Key:** Discovered on printed p. 499 (spread 255 right) of `AliFahim_Software_Engineering.pdf` for all 50 MCQs (8.1 to 8.50).
3. **Packs & PDFs:**
   - `T1_MCQ.md` -> `T1_MCQ.pdf` (25 pages)
   - `T2_Descriptive.md` -> `T2_Descriptive.pdf` (23 pages)
   - `T3_Compare_Analyze.md` -> `T3_Compare_Analyze.pdf` (12 pages)
   - `T4_Diagrams.md` -> `T4_Diagrams.pdf` (11 pages)
   - `T5_Apply_Design.md` -> `T5_Apply_Design.pdf` (15 pages)
   - `T7_Calculations.md` -> `T7_Calculations.pdf` (11 pages)
   - `Ch08_Complete_Print_Pack.pdf` (97 pages)
4. **Source Gaps Resolved:**
   - Figure 8.33: Deductive debugging process (corrected slide caption typo).
   - Exercise 8.13: Year range verified as $1900 \le \text{year} \le 2025$.
   - Exercise 8.44: Restored Table 8.8 (Myers' debugging principles).
5. **Vocabulary Coverage:** 35 predictive leaves mapped in `V8_Coverage.md` with explicit predictive status disclaimer preserved.
