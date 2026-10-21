# ASE Chapter 6 — Software Metrics Build Plan

**Phase (2026-10-20):** Bounded source/content audit and remediation are complete; all seven PDFs are exported and have passed text, page-cohesion, and visual-layout checks. The chapter is ready for the student's visual review. Documented source gaps remain visible and are not claimed as verified coverage.

**Print-economy rebuild (2026-10-20):** Applied the student's Chapter 1 print preferences to the seven packs: suppressed generic opening text, subtitles, answer labels, and only Arabic notes that repeated the answer, retaining suppressed source text in Markdown comments. Re-exported all seven packs: **88 pages** (the index remains Markdown-only). Strict lint passed; all PDFs are current, contain no checked print-only leaks or text-empty pages, and retain all checked question IDs. Targeted visual checks covered first pages, all T4 diagram pages, and T7 calculation pages. Five missing diagram PNGs were safely recovered from the pre-edit PDF backup and confirmed embedded in the rebuilt T4 PDF (six assets total). This is a print/layout pass, not a new source audit.

## Goal and depth

Cover every leaf in `V6_Doctor_Vocabulary.md` with a focused exam-practice set. Use Aggarwal's Chapter 6 course materials first. Add modest depth beyond them only where a supplied vocabulary item is missing, ambiguous, or too thin to answer. Use the four locally available supporting textbooks selectively; avoid repeating material already adequately taught by Aggarwal.

“Complete coverage” means all supplied terms have a verified anchor or an explicit gap note. It does not mean reproducing all four textbooks or predicting all examination questions.

## Source policy

1. K.K. Aggarwal & Yogesh Singh, *Software Engineering*, 3rd ed., is the course-primary source family: scanned prose Ch.6 pp.250–307 and its separately attributed companion slides. Keep book and slide claims distinct.
2. The supplied vocabulary draws terms from outside book Chapter 6: LOC/Function Count/FP in Chapter 4, MTBF in Chapter 7, and Cyclomatic Complexity in Chapter 8. Include only the specified cross-chapter ranges needed for these terms.
3. For each demonstrated gap, choose the clearest of the locally available Pressman, Sommerville, Mall or Leach sources. Do not add all four when one source suffices. Do not cite OCR/search output without opening the actual page.
4. The seminar PDF is an outline/navigation aid only and is excluded as answer authority. Use only sources available in the vault; if no support is found, record the gap rather than infer.
5. Keep the two Aggarwal source families separate. Do not conflate K.K. Aggarwal & Singh with B.B. Agarwal, Tayal & Gupta.

## Student-facing answer format

- Questions and model answers are in English. Any student note or trap is concise Arabic and sits outside the answer.
- Put source-grounded answer content in **bold** and our synthesis in plain text, following the shared ASE question-pack protocol. Exact quotation is optional.
- Give the answer directly. Do not write “the book says,” mention the author inside the model answer, or label normal reasoning “inference.” Put a compact source line separately after the answer.
- Keep answers complete enough to explain the point without turning them into essays. Do not add long Arabic explanations or repetitive source narration.
- The student will write personal calculation notes by hand. The model solution itself follows the labeled mathematical contract below.

## Current study-pack organization

- **T1 — MCQ and concept checks:** source MCQs 6.1–6.20, corrected only when source-backed; add nonredundant MCQs for vocabulary gaps. Keep course-source questions distinct from agent-authored ones.
- **T2 — Short answer and explanation:** definitions, distinctions, lists, metric purpose, assumptions, strengths/limitations, and brief comparisons.
- **T3 — Calculation and worked examples:** LOC/FP/UCP/quality/productivity as supported; full Halstead; data-structure; information-flow; cyclomatic complexity; selected OO computations. Every numerical answer gets an independent recomputation.
- **T4 — Diagrams and tracing:** source-faithful flow graphs, control-flow graphs, data cross-reference/live-variable/span traces, metric tables and GQM/measurement maps when source-supported.
- **T5 — Application and interpretation:** classify a metric, choose a suitable measure, interpret a small result set, identify denominator/scale problems, and explain misuse/ethics.
- **V6 — Vocabulary coverage ledger:** exact term → source → page/slide → coverage status → question IDs. This is a coverage aid, not a sixth study pack unless the final chapter workflow requires it.

Pack boundaries may be merged at final assembly so the student can print fewer files. Export PDFs only when the student authorizes it; the current 2026-10-20 visual-review request authorized export of this chapter's seven packs.

## Question-form allocation (authoring effort, not exam weighting)

Use this as an initial planning budget after the source exercise inventory is tagged; adjust from actual coverage and avoid duplicate variants:

| Form | Initial share | What it should assess |
|---|---:|---|
| Numerical calculation / trace | 35% | Correct counting convention, formula choice, units, arithmetic and interpretation. |
| Define / explain / distinguish | 25% | Core concepts and vocabulary gaps, answered directly without meta phrases about a book. |
| Classify / compare / correct a claim | 15% | Metric category, scale, measure role, model variant and common misconceptions. |
| Diagram / table / code-fragment analysis | 15% | Structural understanding and faithful visual/trace reconstruction. |
| Scenario / result interpretation / evaluation | 10% | Selection, limitations, validity, ethics, and evidence-aware conclusions. |

These shares allocate practice-writing effort only. They are not expected exam marks or probabilities. Use three difficulty bands within each form: foundations (about half), standard application (about one third), and a small stretch set (remainder), without deep excursions beyond the supplied terms.

## Mathematical solution contract

For every numerical item, keep the student-facing problem and answer in English. Use a consistent answer key structure:

1. **Given** — values, counting rules, classification assumptions and units explicitly supplied.
2. **Required** — the exact metric(s) to find.
3. **Model and assumptions** — only assumptions needed to make the problem determinate.
4. **Formula** — source-checked formula, with symbols defined once.
5. **Substitution and working** — visible intermediate steps; no unexplained jump.
6. **Result** — appropriate precision and unit.
7. **Check / interpretation** — range, denominator and meaning check when applicable.
8. **Source** — separate line after the answer.

The student writes his own handwritten setup notes. Do not add long Arabic calculation commentary. Before accepting any calculation, verify formula version, metric stage/variant, denominator, units, rounding and an independent recomputation. A worked example must never silently mix conventions from different books.

## Visual and diagram contract

- Use original Aggarwal slide/book figures as semantic references, not as a reason to redraw every figure.
- For each selected figure, record source page, nodes/labels, edges/direction, grouping, legend and intended interpretation before generating editable SVG/HTML or another clean vector.
- Never use ASCII art. Preserve formula symbols and directed relationships. Check the rendered image against the source image, not extracted text alone.
- `V6_DIAGRAM_ATLAS.md` lists candidate visual families and what must be verified before reconstruction.

## Coverage and verification gates for the later authoring phase

1. Map every vocabulary leaf to an inspected source anchor or mark the gap honestly.
2. Use `V6_SOURCE_QUESTION_INVENTORY.md` to preserve the 20 source MCQs and 28 source exercises by topic/action; verify slide images for flagged formula/OCR ambiguities and keep counts separate from weights.
3. Add original questions only for uncovered learning objectives or useful nonredundant practice; label internally as authored (no citation in the question unless copied verbatim) and cite the answer's evidence.
4. Check every answer against the original page/slide, using the primary Aggarwal source first; supporting-book content is gap-limited and explicitly sourced.
5. Recompute each quantitative solution independently. Maintain a formula ledger with source anchor, symbol definitions, unit, variant and check result.
6. Inspect every selected diagram at source resolution, then inspect the rendered reconstruction visually.
7. Run the shared protocol/linter, export only when authorized, verify PDF text and page cohesion, and visually inspect every page before delivery.
8. Mark the chapter ready for student review only after every gate passes. Student review remains a separate final acceptance step.

## Source coverage, known gaps, and review status

- Completed: OCR and page-boundary verification for selected Chapter 6 and cross-chapter scan ranges; OCR remains a locator and must be checked against the original image when a specific answer is authored.
- Completed: targeted checks in all four locally available support books. Verified source anchors are recorded per topic; unresolved terms are explicitly listed rather than silently completed. Newly verified: Pressman 5e §19.4.2, PDF p.552 / printed p.524, for Henry–Kafura. IF4/Shepperd, Mark II FP, essential/design complexity, and knot count/nesting depth remain bounded gaps. Measurement-scale theory and ethics use verified Fenton (1994) and Sommerville (9th ed.) anchors recorded in the packs.
- Completed visual audit of high-risk source MCQs: 6.3, 6.6, 6.7, 6.14–6.18. Preserve source defects/ambiguities in the inventory: 6.7 stem/options mismatch and duplicate option label; 6.15 underspecified “international standard.” MCQ 6.17 is verified as LCC from slide 85's exact definition and slide 100's key. Exercise 6.7 gives η₁=20 and η₂=40 only; determine from its full prompt and source formulas whether requested measures are identifiable before solving.
- Completed: visually checked slide 74's fan-in/fan-out boundary conventions. These are conventions of that slide procedure, not universal definitions; Henry–Kafura is separately sourced.
- Completed: indexed all 19/19 catalogued Chapter 6 sources (353 chunks) in the existing local database. Ch2–Ch5 counts were preserved; SQLite integrity check passed. This adds only the single Pressman Henry–Kafura page source (3 chunks). The initial 425-chunk count was reduced after narrowing support spans to gap-only pages (Mall PDF pp.165–166; Pressman targeted spans).
- Index use boundary: semantic retrieval is a locator, not evidence of coverage or correctness. The Mark II Function Points query surfaced Leach's unrelated moth anecdote; the source map correctly records this as an unresolved gap instead of treating the hit as support.
- Handoff readiness: source inventory, vocabulary, coverage map, question-form plan, mathematical contract and diagram atlas are synchronized. Gemini may continue Chapter 6 work under the shared ASE protocol, but must inspect the live source pages for each answer and update coverage statuses; it must not claim completion until each vocabulary leaf has a verified anchor or an explicit gap decision. This preparation step does not authorize final PDFs.

## Remediation record (Codex, 2026-10-20)

> The dated notes below record the state at each remediation point. The latest delivery status is at the top of this plan: seven PDFs exported, bounded audit and PDF QA complete, student visual review pending.

- MCQ 6.7 now records the literal answer to the printed stem as `(d) None of the above`; `(a)` is described only as the likely intended answer if the stem meant Module Weakness. The duplicate source label remains documented.
- MCQ 6.15 is left without a unique verified key; no external ISO claim is used to manufacture certainty.
- Live-variable examples in T2/T4/T7 use one stated after-statement convention. The authored trace and FIG03 data now agree: LV counts `[1,2,2,2,1,0]`, sum 8, $\overline{LV}=8/6$, $\gamma=8/4$, $WM\approx2.67$, and $SP_{avg}=1$ for the single observed span.
- TCF/ECF and effort-per-UCP formulas are now documented gaps because they were not verified in the approved local sources. Problem 7.13 calculates only $UAW$, $UUCW$, and $UUCP$.
- The FP payroll example is explicitly conditional on illustrative average complexity weights; it no longer presents a unique exact count or an arbitrary 5% adjustment.
- $V(G)$ practice no longer states universal defect cutoffs, untestability, or automatic merge rules. GQM diagram targets are labelled project-specific.
- Chapter 6 remains an authored draft with unresolved/partial source coverage and no PDF export. The linter, source audit, and visual review are separate gates; this record does not declare the chapter closed.
