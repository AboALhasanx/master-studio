# Chapter 4 Build Plan — Software Project Planning

**Status:** **CLOSED (2026-10-19)** · independent source, math, vocabulary, and PDF audit complete; limitations are recorded below.  
**Prepared:** 2026-10-18 by Codex (review/study coordinator).  
**Shared rules:** `00_STUDIO_HUB/guides/ASE_QUESTION_PACK_PROTOCOL.md`; latest recorded student decisions through N-031.

**Print-economy rebuild (2026-10-20):** Applied the student's Chapter 1 print preferences to the seven packs: suppressed generic opening text, subtitles, answer labels, and only Arabic notes that repeated the answer, retaining suppressed source text in Markdown comments. Re-exported all seven packs and the index: **110 pack pages + 12 index pages = 122**. Strict lint passed; all PDFs are current, contain no checked print-only leaks or text-empty pages, and retain all checked question IDs. Targeted visual checks covered the first pages, all T4 diagram pages, and T7 calculation pages. Existing T3 page splits were left for the student's manual page-flow review. This is a print/layout pass, not a new source audit.

## 1. Goal and boundary

Build a reliable, printable Chapter 4 question set that is deep enough to teach the missing mechanisms and calculations, but whose scope follows the instructor's actual vocabulary and source questions. Keep the source book, companion slides, support books, external references, and practice banks separate. Do not inflate the work into every topic found in every textbook.

The student directly confirmed on 2026-10-18 that the instructor gave the class the exact Chapter 4 vocabulary preserved in `V4_Doctor_Vocabulary.md`. Treat its hierarchy and wording as the governing scope. The original instructor post/date has not been supplied. The older `5-word.json` transcript called the same list a possible future list and carried a Chapter 5/Design title; preserve that mismatch as historical context, but use the latest direct confirmation. Map every listed term to exact book pages and slide numbers before claiming coverage. Keep **Function Count** distinct from **Function Points** unless the course source establishes their relationship. The existing `08_DeepStudy_Ch04` bundle is a legacy draft: it is useful for locating topics and candidate questions, but its “verification” labels do not override the errors documented here.

## 2. Source hierarchy

1. **Working primary:** K.K. Aggarwal & Yogesh Singh, *Software Engineering*, 3rd ed. The local scan is `02_Raw_Materials/Reference_Textbooks/AliFahim_Software_Engineering.pdf`. Identity is high confidence from structure/pagination, but the scan lacks its title/author page. Chapter 4 is printed pp. 139–202, scan PDF spreads 75–107.
2. **Companion course material:** `02_Raw_Materials/Aggarwal_Singh_Slides/chapter_4_software_project_planning.pdf` (207 slides). Its footer identifies K.K. Aggarwal & Yogesh Singh, 3rd ed. Keep slide wording, slide-only questions, and slide figures attributed to the deck. The 207-page `By_Chapter` copy is a duplicate mirror, not a prose textbook.
3. **Gap-filling books only:** B.B. Agarwal, S.P. Tayal & M. Gupta (2010), Pressman, Sommerville 9e, Rajib Mall 4e, and Leach. Select a source after a concrete gap is identified, then verify its edition, section, printed page, and exact support. Do not merge their models or coefficients into Aggarwal's answer silently.
4. **Technical references:** COCOMO II manual, Putnam-estimation note, ICEAA Rayleigh tutorial, and scanned Basili models/metrics paper. Use to check technical derivations or explain a real ambiguity; label the source, and do not let these references replace course-specific notation.
5. **External questions and exam papers:** pattern practice only. They do not establish instructor scope, answer keys, or exam marks.

### Targeted supporting-book map (navigation leads, not answer evidence)

The following ranges were found in the books' contents and targeted text search on 2026-10-18. They identify where to look if the primary source leaves a real gap; no answer should cite a range merely because it appears here.

| Book | Candidate sections/pages | Best use if needed | Boundary |
|---|---|---|---|
| B.B. Agarwal, S.P. Tayal & M. Gupta (2010) | §§9.9–9.11, printed pp. 207, 211, 215 | Project estimation, COCOMO, and software-risk analysis | A separate book from the K.K. Aggarwal–Singh course source; use only after checking the exact passage. |
| Pressman, *Software Engineering: A Practitioner's Approach* | Ch. 5, pp. 113–144; Ch. 6, pp. 145–164 | Planning/estimation and risk-management gap checks | Its planning taxonomy and model wording may differ from the course deck. |
| Rajib Mall, *Fundamentals of Software Engineering*, 4th ed. | Ch. 3, pp. 85–153; §§3.4, 3.7, 3.9, 3.13 (notably pp. 101–119 and 136–138) | Size estimation, COCOMO/COCOMO II, Norden/Putnam staffing, risk | Strong topic match, but do not treat its exercises or ordering as course scope. |
| Sommerville, *Software Engineering*, 9th ed. | Ch. 22, pp. 593–617; Ch. 23, pp. 618–650 | Risk process; planning, scheduling, estimation | Strong conceptual cross-check; its model set is not identical to Aggarwal–Singh. |
| Leach, *Introduction to Software Engineering*, 2nd ed. | Ch. 2, pp. 55–86; §§2.4–2.6, pp. 65–78 | Estimation, scheduling, project measurement | Selective conceptual check only; not the authority for course formulas. |

These are verified navigation anchors from table-of-contents/page-text screening, not a claim that the listed pages have already been read line by line or are needed in the final pack. Keep the primary-book/slide evidence distinct from any supporting-book addition.

## 3. Source and artifact inventory

### Course sources

- Scanned primary book: printed pp. 139–202 / spreads 75–107. It is image-only; OCR is for navigation, never final evidence. Boundary spreads contain adjacent-chapter pages: spread 75 includes printed p. 138 on the left and p. 139 on the right; spread 107 includes p. 202 on the left and p. 203 on the right. Any OCR/indexing must crop or exclude the neighboring half.
- Companion deck: 207 slides, including 19 worked examples (4.1–4.19), 25 MCQs (slides 194–199), and 36 exercises (slides 200–207).
- Duplicate deck: `02_Raw_Materials/Aggarwal_Singh_SE_3rd_ed_By_Chapter/Ch04_Software_Project_Planning.pdf`, 207 pages and text-matched to the companion deck. Do not count it as a second independent source.
- Supporting and external files are indexed in `00_INDEX.md`; exact page ranges must be verified before answer citations are written.

### Existing Chapter 4 draft

`08_DeepStudy_Ch04/` contains a study-system note, model/deep question files, seven question-type packs, a source map, verification protocol, seven diagrams, and exported PDFs. Keep these files intact as legacy material while the new canonical set is built. The old pages, counts, equations, “all checked” statements, and PDFs are not self-validating evidence.

## 4. Coverage and question architecture

The source exercise inventory has 36 tasks with the following main requested action: 10 calculations; 10 explain/define/list/describe; 3 comparisons; 11 analysis/justification/evaluation/derivation/discussion; 2 design/programming; and 0 explicit drawing tasks. Fifteen exercises have an overlapping case/data tag. The 25 slide MCQs and 19 worked examples are separate inventories. These are **source counts only**, not predicted exam weights.

### Visual-source inspection queue

Slide-text search located five high-value visual clusters. Render and inspect the original before drawing or extracting: (1) function-point categories/tables/examples, slides 9–30; (2) COCOMO 81 equations, modes, driver and phase tables, slides 41–71; (3) COCOMO II stages, scale factors, driver tables and language sizing, slides 73–120; (4) the full Putnam/Norden–Rayleigh topic sequence, slides 123–179 (Rayleigh/derivation 123–135; difficulty 136–145; productivity 146–148 and 174–179; time/cost 149–150 and 166–173; development sub-cycle 151–165); (5) risk taxonomy and risk-management workflow/plan, slides 180–193. These are text-navigation anchors; render and inspect each relevant original before drawing or extracting, and do not assume every slide in a range is a diagram.

A representative original-slide set was rendered and visually checked on 2026-10-18: slides 16–17, 21, 23, 29, 44–45, 58, 62, 74, 85, 115, 123, 125, 128, 130, 139, 142, and 190. It confirms the primary deck visibly uses `√e` in the Rayleigh peak-manning formula (slides 130 and 139), shows the phase-allocation table on slide 62, COCOMO-II stages on slide 74, and risk-management activities on slide 190. This was a representative source-figure inspection, not a visual sign-off of all 207 slides or all PDF pages.

Confirmed scope and source map (18/18 instructor terms mapped to primary-book pages and companion-slide ranges; exact locators are in V4 and the index):

1. **Size Estimation:** Lines of Code (LOC); Function Count. Preserve the professor's exact term. The companion deck directly connects it to Albrecht's Function Point Analysis: slides 9–10 introduce the method, MCQ 4.3 identifies Alan Albrecht as its developer, and Exercise 4.9 asks about Albrecht's function-count method. Verify the original page images and primary-book wording before finalizing the explanation; do not broaden this into every Function Point variant.
2. **Cost Estimation Models:** static, single-variable models; static, multivariable models.
3. **COCOMO:** Basic, Intermediate, and Detailed models.
4. **COCOMO II:** Application Composition Estimation, Early Design, and Post-Architecture models.
5. **Putnam Resource Allocation Model:** Norden/Rayleigh curve; difficulty metric; productivity versus difficulty; time-versus-cost trade-off; development sub-cycle.
6. **Software Risk Management:** what risk is; typical software risks; risk-management activities.

Use model modes, cost drivers, equations, schedule/phase allocation, risk exposure, and similar details only where they explain a listed term or solve a source exercise. They are supporting depth, not new instructor terms by default.

**Pack choice:** use only question formats supported by the material. Calculation/application and model-selection analysis are likely major work forms because the source provides many calculations and cases; this is a study-design observation, not an exam prediction. Diagrams will be included as learning/reference visuals where useful, not turned into mandatory “draw this” questions without source or pedagogical need.

### Proposed question-pack mix (coverage plan, not predicted exam weighting)

| Pack/form | Source-backed inventory | What the pack should cover |
|---|---:|---|
| T1 · MCQ | 25 slide MCQs (slides 194–199) | Preserve original stems/options where usable, independently verify the answer, and add only non-duplicate MCQs for uncovered confirmed terms. |
| T2 · Short descriptive | 10 explain/define/list/describe exercises | Project-planning activities, LOC/Function Count, model stages, and risk vocabulary; keep answers concise but complete. |
| T3 · Compare/analyze | 3 comparisons + 11 analytical/derivation/discussion exercises | Compare estimation models and COCOMO stages; analyze assumptions, effort/schedule trade-offs, source-table inconsistencies, and risk responses. |
| T4 · Visuals | Five identified visual clusters; 0 exercises explicitly command “draw” | Teach/interpret verified diagrams and tables. Add a draw/reconstruct prompt only if the source or confirmed vocabulary justifies it. |
| T5 · Apply/case | 15 exercises have an overlapping scenario/data tag | Use the cases to select a model, calculate from stated inputs, or justify a risk response; do not count these as 15 additional exercises. |
| T6 · Design/create | 2 design/programming exercises | Retain only if relevant to the confirmed scope; do not expand into unrelated implementation detail. |
| T7 · Calculation | 10 calculation/estimation exercises + 19 worked examples as a separate reference set | Rebuild from source with formulas, units, assumptions, model/stage selection, and precision checked independently. |

Counts overlap by design: scenarios may also be calculations or analysis. They describe the source inventory and our coverage needs; they are not exam probabilities, mark weights, or a guarantee of what will be tested.

### Coverage and source-completeness gate (required before closure)

Do not claim “100% complete” until the following finite scope has been audited and every row has a disposition. Here, 100% means complete coverage of the student's confirmed instructor vocabulary and all directly relevant course-source material for this chapter; it does **not** mean reproducing every topic in every textbook or predicting every possible exam question.

1. **Instructor vocabulary:** all 18 listed subtopics must have a usable answer, a verified primary-book page and companion-slide locator (or an explicit, evidence-based “not present” result for that source), and a coverage status. No blank or unmapped term is allowed at closure.
2. **Course question inventory:** account for all 25 slide MCQs, all 36 written exercises, and all 19 worked examples. For each item, record its related vocabulary term(s), audit status, and disposition: included in a pack, represented by a non-duplicate equivalent, retained as optional/source practice, excluded as outside the confirmed boundary, or unresolved. An unresolved item blocks closure; an exclusion needs a short reason.
3. **Selective supporting-source use:** consult a named supporting source only after a specific primary-source gap or material ambiguity is identified. Record and verify the exact passage for any supporting claim used. Do not perform a blanket book-by-term survey. No supporting-book claim is used in the current chapter packs.
4. **Depth boundary:** each term is covered at the depth needed to define it, explain its essential mechanism/conditions, distinguish it from a nearby concept, and solve a relevant source-backed task when one exists. Add no extra layer when the sources and listed exercises do not justify it.
5. **Separate coverage from verification:** coverage is 100% only when every in-scope row is accounted for. Source verification is complete only when every factual answer claim, numerical result, and diagram used in the final packs has been checked against its cited source. Report these as separate gates; one cannot substitute for the other.
6. **Equation and numerical correctness:** create an equation register for every distinct formula actually used in the final packs. At minimum, audit the used formulas for LOC/static models; function counts/Function Point calculation; COCOMO 81; each included COCOMO II stage; and Putnam/Rayleigh, difficulty, productivity, time-cost, and development sub-cycle. For each formula, record the source page/slide, exact model/version/stage, symbol meanings and units/domain, independent algebraic or technical validation, and every worked example that uses it. Inspect the original page image for scanned equations; do not validate from OCR alone. Independently recalculate every numerical answer and check units, model selection, driver ratings, intermediate precision, and rounding. A source's printed answer is a comparison point, not proof of correctness. Any mismatch or source ambiguity stays visible and blocks a clean “verified” claim until resolved or explicitly bounded.

The final closure report must state the denominators and results explicitly (for example, `18/18 vocabulary`, plus separate disposition totals for `25 MCQs`, `36 exercises`, and `19 examples`), list any source gaps/conflicts and their resolutions, and name anything deliberately outside scope. Never report 100% based only on file completion, a vector-index match, linter output, or an agent's handoff summary.

For mathematical reliability, also report `distinct formulas used / distinct formulas independently validated` and `numerical results checked / numerical results included`. Both must be complete for the final packs before describing their calculations as verified. The target is complete verification of the finite set actually used—not every equation appearing anywhere in all candidate books.

### Standard format for numerical answers (planning rule)

Use one repeatable solution structure so different agents produce compatible, inspectable work. The question and worked answer stay in English. Do not add Arabic coaching notes to a numerical solution; the student will add personal formula, given/required, and reminder notes by hand.

**Default answer sequence:**

1. **Given:** list only the values and conditions stated in the question, each with its unit. Do not silently add missing inputs.
2. **Required:** name the quantity or quantities requested, with the expected unit.
3. **Model and case:** identify the model, version/stage, and mode when applicable. If the prompt does not determine them, state the smallest necessary assumption before calculating; if more than one reading is reasonable, show separate conditional results or explain why a unique result is unavailable.
4. **Equation:** write the governing equation in symbols and identify any symbol whose meaning is not obvious from the question.
5. **Substitution and working:** substitute the stated values visibly; show material intermediate arithmetic and keep units attached. Do not hide the calculation behind a calculator result, code, or a final number.
6. **Result:** give each requested result clearly with its unit. Carry precision through the working and round only at the end, using precision appropriate to the input/source.
7. **Check or interpretation:** add at most one short sentence when it checks units, plausibility, a model comparison, or the meaning of the result. Omit filler when it adds nothing.
8. **Source:** put the source locator on a separate line after the complete answer. Distinguish textbook pages from slide numbers and flag a source inconsistency without silently correcting the printed data.

**Model-specific controls:**

- **Function-count / Function Point calculations:** preserve the source's unit categories and complexity weights; show the count-to-weight calculation and adjustment-factor step separately. Do not substitute a category, weight, or rating that the prompt does not provide.
- **Static estimation and COCOMO:** state which equation family and COCOMO version/stage are being used; distinguish KLOC, effort (person-months/person-years), development time, and average staffing. For multi-mode questions, solve each requested mode separately.
- **Intermediate/Detailed COCOMO and COCOMO II:** show the nominal estimate before adjustment, then list or reproduce the applicable driver ratings and multipliers from the relevant source table, then calculate the adjusted result. Never mix early-design and post-architecture drivers or phase-allocation tables.
- **Putnam/Rayleigh:** state whether values refer to the whole project or the development sub-cycle; keep `K`, `Kd`, `td`, and `tod` distinct. Show the chosen equation before substitution and preserve the correct square-root factor in peak-manning work.
- **Source ambiguity or defect:** separate the source's stated inputs/result from the agent's recalculation. If the exercise is under-specified, do not present an assumed answer as uniquely required; state the assumption or provide the supported alternatives.

Use aligned equations or a short numbered list rather than a prose paragraph. Preserve a source table when the calculation depends on its rows; do not create a generic table just to display a few values. A worked example is complete only when another student can reproduce the result from the shown inputs, model, equation, units, and arithmetic.

## 5. Closure-audit findings (2026-10-19)

The previous checkpoint overstated the evidence. The following corrections are now reflected in the study packs and index:

- The scanned textbook's **Table 4.7 is printed on p. 159**. For Organic Small ($S\approx2$), effort fractions are $(0.06,0.16,0.26,0.42,0.16)$ and schedule fractions are $(0.10,0.19,0.24,0.39,0.18)$; the sums are 106% and 110%. The source does not state a cause for these totals. Do not label this as Table 7 in the book or infer a $\le50$ KLOC row from $S\approx2$.
- T7 Problems 7.15, 7.20, 7.21, and 7.22 reproduce textbook Examples 4.12, 4.9, 4.10, and 4.17, respectively; the other eight Section 2 items are authored practice. The index inventories all 19 worked examples with a printed-page locator and explicit exact/equivalent/partial disposition.
- The prior 28-formula/38-result verification totals and 90-cell supporting-book screen have no item-level evidence ledger; they are retired. The current finite-pack register maps 30 formula/relationship rows to the live artifacts, and the 22 T7 worked items were independently recalculated.
- The current audit recalculated the 22 displayed T7 items, checked the model/stage and unit choices, reconciled the formula register, and recorded ambiguity/rounding limits. All 19 source examples and 36 exercises have explicit dispositions; four source examples are exact reproductions, with the rest marked equivalent or partial.

The chapter is closed after all final delivery gates passed. The source inventory, 30-row finite-pack equation register, 22-item T7 numerical recalculation, instructor vocabulary mapping, and affected PDF pages are reconciled. Known partial source-example coverage and visual-inspection limits are documented in the index.

## 6. Visual plan

The five current chapter diagrams (`d01`–`d05`) were visually reviewed at original PNG resolution; the five diagram pages embedded in T4 and selected calculation pages in T7 were also inspected. The corrected Rayleigh diagram uses $m_0=K/(t_d\sqrt e)$, separates $0.3935K$ from $K_d=K/6$, and has no visible clipping or overlap. The older seven legacy images are superseded working assets and are not referenced by the final T4 pack.

Before publishing replacement visuals:

1. Verify the relationship and labels against the original slide/page image.
2. Recompute every formula and numeric annotation independently.
3. Check bounds, text overlap, legibility at print size, and page integration.
4. Keep original-source diagrams distinct from newly drawn explanatory diagrams.

## 7. Build sequence

1. Map all 18 listed subtopics to exact scanned-book pages and companion-slide numbers. OCR scanned pages locally with cropped boundary spreads; preserve printed-page labels and OCR caveats.
2. Compare primary-book and slide coverage term by term. Make uncovered or unclear terms visible; select one supporting book only for a demonstrated gap and record why the primary course source was insufficient.
3. Map every instructor term, source exercise, MCQ, and worked example to an answer location. Keep slide-only prompts and textbook prompts separately attributed.
4. Audit/rebuild each MCQ and written response from the source; make the answer directly answer the question and keep concise Arabic notes outside English answers.
5. Recalculate all numeric examples independently, including units, model choice, driver stage, and assumptions. Preserve source-table inconsistencies explicitly.
6. Rebuild necessary diagrams and formula references from verified content; keep Function Count/Function Points terminology source-led.
7. Run the pack protocol's linter/export/cohesion/visual gates for each changed pack. Report content audit, coverage, PDF checks, and limits separately.
8. Update the chapter index, daily journal, and `ACTIVE_STATE.md`. Do not mark the chapter closed until the student decides and the agreed checks are done.

## 8. Current Checkpoint (2026-10-19 — Independent Closure Audit)

**Verified:** The 25 numbered MCQ stems and keyed answers match their source sequence/key; all 36 numbered exercises have a pack disposition; the 18-term instructor vocabulary artifact exists; and the Organic Small Table 4.7 row has been checked against the scanned source image.

**Corrected in Markdown during this audit:** T2, T3, and V4 now use the exact Table 4.7 phases/fractions and source page; T3 no longer invents a cause for the 106%/110% sums; T7 distinguishes its eight authored numerical practice items from the four reproduced source examples (4.9, 4.10, 4.12, 4.17); the index records exact/equivalent/partial coverage and the recalculated 22-item numerical set.

**Closure evidence:** all eight Markdown artifacts passed strict lint; all eight PDFs were freshly exported, checked for blank pages and build-marker leaks, and verified newer than their Markdown; selected affected pages were visually inspected. Final output is 110 pages across seven study packs plus a 12-page index (122 pages total). No commit or push was performed.
