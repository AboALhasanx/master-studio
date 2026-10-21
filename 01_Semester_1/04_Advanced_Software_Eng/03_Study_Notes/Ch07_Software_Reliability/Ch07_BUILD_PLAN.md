# ASE Chapter 7 — Software Reliability Build Plan

**Phase (2026-10-21):** chapter source audit, scope mapping, and local vector-memory setup. Final question packs and print PDFs have not started.

## Goal and scope

Build a compact, source-grounded question set that teaches the instructor's supplied vocabulary, with enough explanation to answer exam questions and modest depth where the lecture material is thin. The 19 supplied leaf terms in `V7_Doctor_Vocabulary.md` define the required scope. This does not mean reproducing every related topic in five textbooks, the student seminar, or current standards literature.

### Keep inside the scope when needed to answer a listed term

- Operational profile and input space under **Environment**.
- Failure, fault, failure intensity, execution time, calendar time, MTBF, and MTTF where they are needed to explain the listed reliability concepts or solve a listed model problem.
- The factors, criteria, attributes, levels, and relationships that are part of McCall, Boehm, ISO 9126, CMM, and the assigned ISO 9001 comparison.
- Model assumptions and limits only to the depth needed to choose, calculate, or interpret the five named reliability models.

### Keep outside unless a confirmed gap requires it

- Additional reliability models not named by the instructor.
- ISO 25010 or newer CMMI material as replacements for the historical syllabus models.
- Extended reliability metrics, software safety, quality-assurance programs, and system dependability as standalone units.
- The extra sections in the student seminar that are not needed to explain a listed term.

## Source hierarchy

1. **Course-primary prose:** K.K. Aggarwal & Yogesh Singh, *Software Engineering*, 3rd edition, represented in the vault by the scanned `AliFahim_Software_Engineering.pdf`. The scan's cover/title page is absent, so the edition identity is high-confidence from the matching table of contents and companion slides, but remains an inferred identity for the scan. Chapter 7 prose/exercises are provisionally printed pp. 308–364 / PDF spreads 160–188. Spread 188 contains printed p.364 (Chapter 7 exercises) and p.365 (the next chapter title/start); exclude the latter from Chapter 7 claims.
2. **Official companion slides:** the 126-slide Chapter 7 deck identifies K.K. Aggarwal & Yogesh Singh, 3rd ed., New Age International, 2007. Use it for lecture-specific emphasis and diagrams. The question prompts are also present in the primary book: MCQs on printed pp. 359–362 and exercises on pp. 363–364. Keep slide-only wording attributed to slides.
3. **Student-provided instructor vocabulary:** the exact list in `V7_Doctor_Vocabulary.md` sets the scope. It is a direct report from the student; no original announcement file is attached in this turn.
4. **Supporting textbooks:** use them as a comparison pool only when a term is absent, ambiguous, or materially clearer elsewhere. The catalog contains five supporting books; their identities and useful ranges are in `V7_SOURCE_COVERAGE_MAP.md`. Never conflate K.K. Aggarwal & Singh with B.B. Agarwal, Tayal & Gupta (2010).
5. **Existing seminar artifact and external question banks:** navigation or question-form references only; not answer authority, not scope authority, and not evidence of the instructor's exam marks. The existing OpenCode-produced `Reliability_Seminar/Ch7_Software_Reliability.pdf` is currently 62 pages (25,738 words in its Markdown source, 17 tables, 24 generated grayscale figures). Its structural `qa_check.py` currently passes, but its equation checker recognizes **zero** numbered equations because it only matches lines beginning with `*`; the empty-list sequence check passes vacuously, and the hard-coded numerical assertions do not compare against the source formula text. Treat its reported equation pass as unverified until that checker is repaired and the formulas are checked against the primary page images. The old session log's 56-page statement is stale. Do not copy its generated figures or answers into the new question packs without a fresh source comparison.

When prose and slides disagree, use the primary textbook for the explanation and preserve a slide-specific question as a slide source. Do not smooth over a real discrepancy without recording it. **Known conflict:** slide 115 item 7.34 asks about CMM process management, duplicating slide 116 item 7.35. The primary book p.361 gives 7.34 as process control and 7.35 as process management; use the book wording and document the slide discrepancy.

## Planned study-pack set

- **T1 — MCQ:** transcribe and check the 50 publisher-slide questions. The inspected deck ends at the exercises and contains no publisher answer key; solve each item independently against the source material. Add new MCQs only for a demonstrated coverage or practice gap, without reworded duplicates.
- **T2 — Short answer:** direct definitions, lists, explanations, model descriptions, CMM common features, and ISO 9000 requirements. Answers stay concise, in English, with only short Arabic notes where useful.
- **T3 — Compare and analyze:** hardware/software reliability; quality/reliability; McCall/ISO 9126; the five reliability models where comparison is useful; and CMM/ISO 9001 mapping and contrast. Keep each source prompt in one primary pack to avoid duplication.
- **T4 — Figures:** source-faithful curves and quality/process-model figures. Prefer clear crops from the original book or official slides. A figure should contain the figure itself; put the explanation in the separate answer. Do not redraw a stable source figure unless a documented legibility or question-specific need requires it.
- **T5 — Apply and interpret:** a small set of non-redundant applications based on operational profiles, reliability measures, release objectives, model assumptions, and standards comparisons. Do not invent an unrelated scenario bank.
- **T7 — Calculations:** worked source examples and numerical exercises for the named models. Do not make a separate calculation pack for a model if the course material gives no numerical task for it.
- **V7 — Vocabulary coverage:** exact term → answer location → source locator → coverage status. This is a navigation ledger, not a substitute for the answers.
- **No separate T6 is planned** unless source tagging shows a genuinely distinct creation task that cannot be placed naturally in T4 or T5.

### Source exercise mix and authored practice

The 35 written source exercises are tagged in `V7_QUESTION_INVENTORY.md`: 13 definition/explanation/list (37.1%), 9 comparison/evaluation (25.7%), 7 quantitative calculations (20.0%), 3 diagram/table construction (8.6%), 2 applied monitoring/KPA-description tasks (5.7%), and 1 model-relation interpretation (2.9%). These are response-form counts, not exam marks. The separate source bank has 50 MCQs. Use this mix to keep any additional practice proportional, and add questions only for a real coverage or retrieval gap; do not manufacture exam probabilities.

## Equation and worked-example gate

Create an equation register before accepting any numerical answer. It must cover every equation actually used from:

- Basic Execution Time Model — source examples 7.1 and written tasks 7.15, 7.18, 7.24 as applicable.
- Logarithmic Poisson Execution Time Model — examples 7.2–7.3 and tasks 7.16, 7.19–7.21 as applicable.
- Calendar Time Component — examples 7.4–7.6 and task 7.23.
- Jelinski–Moranda — example 7.7 and task 7.25.
- Bug Seeding — explain the source model and its assumptions; do not invent a numeric exercise unless the primary source supplies enough data and an unambiguous method.

For each equation, inspect the original source page image, transcribe notation, define symbols and units, identify model assumptions, independently derive/check the expression, and recalculate every result. OCR and slide text extraction are navigation aids; they are not proof for subscripts, symbols, or arithmetic. Use the shared numerical answer format in `ASE_QUESTION_PACK_PROTOCOL.md`.

## Figure and standards gate

- The official slides provide numbered figures 7.1–7.24. `V7_DIAGRAM_ATLAS.md` records the slide locations and likely role.
- Compare the original slide and scanned-book figure before choosing an image. Extract the clearest complete original for stable diagrams and preserve its source locator. Inspect small labels at print scale.
- Use no ASCII diagrams. For a necessary redraw, retain the original, record a semantic checklist, and validate both meaning and visual legibility.
- Keep the syllabus's ISO 9126 and ISO 9001/CMM comparison in its source-era form. Do not silently replace those topics with newer standards or import modern clause counts into the answer.

## Authoring sequence

1. Finish the Chapter 7 OCR/vector refresh and verify the source index with targeted searches.
2. Inspect scanned-book pages 160 and 188 plus the intervening section starts to confirm the printed-page map and boundaries. Inspect each page image used for formulas, tables, and figures.
3. Tag all 50 MCQs and 35 exercises by vocabulary leaf, response type, model, calculation/diagram need, and source locator. Preserve the original item IDs and flag corrupted or ambiguous slide text.
4. Finalize the pack split and answer-count inventory from those tags; remove duplicates before drafting.
5. Author answers, diagrams, and calculations from primary pages. Add one named supporting book only where the map records a real gap or a materially better explanation.
6. Run the question-pack protocol's content, equation, coverage, PDF, cohesion, and visual gates. Update the index, plan, student decision log, daily session, and runtime state to match the actual artifacts.

## Current open facts and risks

- The book and deck have 50 numbered MCQs and 35 numbered exercises. The slide text layer sometimes separates formulas or mixes nearby columns, and at least one slide stem (7.34) conflicts with the book. Check the rendered source before transcribing items.
- **Example 7.2 rounding:** the scanned book p.337 prints μ(20)=109, while direct substitution into its displayed logarithmic-model equation gives 109.861... . In a worked answer, state the computed value and make the source's integer truncation/rounding visible; do not silently call 109.86 equal to 109.
- No answer key or solutions section appears in the inspected Chapter 7 book pages or companion deck; solve the MCQs independently and review them against the primary chapter.
- The scanned-book range is identified by OCR and checked visually at the chapter start and end; final answer citations must use the visible printed page labels. The last scan spread mixes Chapter 7 p.364 with the Chapter 8 title/start on p.365.
- The existing seminar artifact includes substantial material beyond the requested study scope and is excluded from the study-pack source hierarchy. Its current PDF has 62 pages; older session counts are stale. Its structure check passed, but the equation checker has the vacuous-pass defect described above.
- No exam-score weighting evidence has been found. All proposed percentages are practice-writing allocation only.
