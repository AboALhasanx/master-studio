# Chapter 5 Build Plan — Software Design

> **State:** **AUTHORED; TARGETED CROSS-AUDIT COMPLETE; READY FOR STUDENT REVIEW (2026-10-19)**  
> Six question-pack files and the index are authored, corrected, and exported. Three read-only reviews plus Codex source/page and visual checks found and corrected the listed issues. This is a targeted cross-audit, not blind verification of every sentence or every source figure. The 24-term scope list is student-attributed, and diagram selections are not exhaustive. Final PDFs: 76 pages total (70 across six packs + 6 index pages), zero text-empty pages.

> **Print-economy rebuild (2026-10-20):** Applied the student's Chapter 1 print preferences to the six packs: suppressed generic opening text, subtitles, answer labels, and only Arabic notes that repeated the answer, retaining suppressed source text in Markdown comments. Re-exported all six packs and the index: **70 pack pages + 6 index pages = 76**. Strict lint passed; all PDFs are current, contain no checked print-only leaks or text-empty pages, and retain all checked question IDs. Targeted visual checks covered first pages and all T4 diagram pages. Existing sparse/split pages in T3 were left for the student's manual page-flow review. This is a print/layout pass, not a new source audit.

## 1. Target and source boundary

The professor-supplied vocabulary defines the minimum chapter scope. It does not define marks or exam probability. Add the concepts the professor explicitly identified as missing from the earlier seminar, then add only the explanation needed to make those concepts usable. Do not turn this into an exhaustive survey of software design.

The confirmed vocabulary is recorded in `V5_Doctor_Vocabulary.md` (24 leaf items across six blocks). `V5_SOURCE_COVERAGE_MAP.md` maps all 24 terms, 12 publisher MCQs, 24 textbook exercises, professor-feedback gaps, question forms, and diagram families. Its proposed question-form percentages allocate practice-authoring effort only; they are not exam marks or probability. The professor's seminar feedback is a separate coverage signal: abstraction (procedural, data, control), stepwise refinement, information hiding, fan-in/fan-out, depth/width, design review, and DFD-to-structure-chart transformation (transform and transaction analysis). The student confirmed on 2026-10-19 that the seminar's “properties” means Meyer's five modularity criteria. Treat this as clarification of the existing modularity/Exercise 5.4 scope, not an extra vocabulary-list term. Pressman 5th ed. §13.4.3, printed p.345 / PDF p.373, visibly lists and explains all five.

## 2. Source hierarchy and identity controls

1. **Course-aligned source family:** K.K. Aggarwal and Yogesh Singh, *Software Engineering*, third edition. The local `AliFahim_Software_Engineering.pdf` scan has no title page, so the bibliographic identity remains high-confidence from its internal structure, pagination, and the matching publisher deck—not directly visible on the scan.
2. **Companion source:** `Ch05_Software_Design.pdf`, 99 publisher slides. Its footer identifies K.K. Aggarwal and Yogesh Singh, third edition, New Age International Publishers, 2007. Cite slide-only prompts/figures as slides; do not call the deck the prose textbook.
3. **Instructor-feedback gap sources:** Follow the existing professor profile: Pressman, fifth edition, for procedural/data/control abstraction, stepwise refinement, information hiding, fan-in/fan-out and hierarchy width/depth; Rajib Mall, fourth edition, for fan-in/fan-out, DFD-to-structure-chart transform/transaction analysis and design review. Candidate page anchors are recorded in the doctor profile and source catalog; verify printed labels and full claims before citing. B.B. Agarwal et al. (2010) was term-screened as an alternative but is not selected or indexed for this chapter because no unique gap requires it and the professor profile points to Pressman/Mall.
4. **IEEE SDD edition:** course material names IEEE Std 1016-1998. Preserve that version in course answers. The official IEEE page for 1016-2009 is a newer revision and may be used only to explain standard lineage or confirm the general role of SDD; never silently substitute its edition or content for the course's 1998 reference.
5. **Not interchangeable:** `CS_Agarwal_SW_Engineering_and_Testing_2010.pdf` is a different book and is not the prose source for the K.K. Aggarwal–Singh slides.

### Candidate locators to verify at answer-writing time

| Source | Candidate local locator | Intended use | Evidence limit |
|---|---|---|---|
| Scanned K.K. Aggarwal–Singh book | Scan spreads 107–130; recorded printed span 203–249 | Core design concepts, examples, SDD, OOD | Spread 107 also contains the prior chapter's printed p.202; verify visible printed page labels and crop/ignore the neighboring page. OCR is navigation, never final evidence. |
| K.K. Aggarwal–Singh publisher deck | Slides 1–99 | Vocabulary mapping, source questions, figures | It is a companion slide deck, not a second independent book. |
| Pressman, 5th ed. | PDF pp.370–380 / printed pp.342–352, especially §13.4.3, printed p.345 / PDF p.373 | Meyer’s five modularity criteria; abstraction, refinement, information hiding, and hierarchy concepts | Edition verified from local title pages; page 373 was visually checked for the exact five criteria. Confirm each other claim on its printed page image before citation. |
| Mall, 4th ed. | PDF pp.301–302; 342–349; 350–351 | Fan-in/fan-out; DFD transformation; design review | Use only the pages that answer a confirmed gap; verify printed page labels if cited in final answers. |

## 3. Source-question inventory

The companion deck's final slides contain **12 MCQs (slides 94–96)** and **24 written exercises (slides 97–99)**; the original scan visibly confirms this inventory on printed pp.248–249. Keep these as separate source inventories while classifying them; overlapping actions are not extra questions. These counts do not predict examination marks.

Initial format allocation (final counts follow item-by-item classification):

| Section in the consolidated chapter pack | Material that belongs there |
|---|---|
| MCQ | The 12 source MCQs, answer-checked; only add authored MCQs for a confirmed uncovered term. |
| Short answer | Definitions, lists, distinctions, design objectives, SDD terms, and brief explanations. |
| Compare and analyze | Design strategies; function-oriented vs object-oriented; coupling/cohesion; design vs coding; complete decoupling and related claims. |
| Interpret diagrams | Explain the purpose, notation, structure, and meaning of source figures; distinguish DFD, structure chart, flowchart, UML activity, class, sequence/interaction, state, component/deployment, and use-case diagrams. |
| Apply/design | Classify a stated module relationship; assess a small design; produce a justified module/class decomposition; transform a DFD into a structure chart only when the task supplies enough information. |
| Vocabulary coverage | Short answerable prompts for all 24 leaf terms, placed in the same consolidated file without duplicate definitions. |

There is no separate calculation pack unless the source inventory yields a real, in-scope numerical task. Fan-in/fan-out may be applied to a supplied structure, but this alone does not justify inventing a new calculation chapter.

## 4. Diagram-source and generation plan

The diagram register is `V5_DIAGRAM_ATLAS.md`. It maps the source figures to their *meaning and notation*, not only their appearance. Selected source-slide renders and all 24 scanned book spreads are linked in `source_figures/README.md`; the first spread visually distinguishes prior-chapter p.202 from Chapter 5 p.203. Each generated redraw must retain editable source code and use `V5_DIAGRAM_CONTRACT_TEMPLATE.json` as its semantic specification.

| Diagram family | Ch05 examples | Authoring route |
|---|---|---|
| UML structural/behavioral diagrams | Use case, class, activity, sequence/interaction, state, component, deployment | PlantUML as the first candidate; validate against the OMG UML semantics and the source figure. Mermaid may be used for a simple subset, not as a claim of full UML conformance. |
| Structure charts | Module hierarchy, call/control relations, data couples, transaction/transform structure | Graphviz DOT or hand-authored SVG with the chapter's structure-chart symbols; do not substitute a generic flowchart. |
| DFD | Context/levelled data flow and the input-transform-output or transaction view | Use a declared notation (Yourdon/DeMarco or Gane–Sarson) with explicit entity/process/store/flow rules; preserve balancing and flow semantics. Use a custom SVG/Graphviz renderer if a general diagram engine cannot express the required symbols faithfully. |
| Conceptual design/process figures | Design framework, conceptual vs technical design, refinement, OOD steps | PlantUML activity when it is a workflow; otherwise a typed SVG/Graphviz concept model. Do not label every box-and-arrow picture “UML.” |
| Curves and quantitative figures | Modularity/cost curve | Generate from a numeric plotting script with verified axes, units, labels, and marked minimum; no hand-placed approximate curve. |
| Tables and notational legends | Coupling/cohesion order, SDD information, structure-chart notation | Rebuild as readable tables/legends when the source is tabular; do not force them into a diagram. |

Each figure needs a **diagram contract**: `figure_id`, source/page, intended question/learning purpose, formal type and notation, element inventory, relation/arrow direction, labels/cardinalities, assumptions, editable code path, output path, and checks. Validate three layers independently: (1) semantic invariants in the contract, (2) successful parsing/rendering by the chosen engine, (3) visual comparison against the source at print size. Pixel similarity can flag layout drift; it cannot prove the model is semantically correct.

## 5. Vector database and memory scope

Add Chapter 5 as chapter `5` in `00_STUDIO_HUB/indexes/04_Advanced_Software_Eng/knowledge_sources.json`, then rebuild the local SQLite vector index. The live catalog currently has 14 Chapter 5 sources. Include:

- the exact instructor vocabulary ledger;
- the scanned chapter spreads with OCR explicitly labelled as OCR and the boundary spread called out;
- all 99 companion slides, with visual OCR on the diagram-bearing slides and a diagram atlas note;
- only the relevant Pressman and Mall page ranges for the professor-identified gaps;
- selected external question-bank pages under `external_question_bank` / practice-only authority, never as evidence of this course's scope or answer key.

The current vector database embeds text/OCR chunks; it is **not a multimodal image embedding store**. To make figures retrievable, keep the visual reference PNGs on disk, index each figure's label/source/notation/semantic contract and image path as text, and require the agent to open the linked source image before redrawing it. Do not send course files to Colab or another cloud processor for this local index; the available local pipeline already performs OCR and embeddings locally.

## Diagram pipeline pilot status

Three editable diagram pilots are now rendered and source-compared: UML class/generalization (course slide 68), transaction-centred structure chart (slides 42/44), and Mall RMS DFD-to-structure-chart transform analysis. Each has a semantic contract. The RMS DFD boundary arrows were corrected to match source direction. The local renderer produces images; it does not prove notation correctness. These pilots validate a workflow, not every Chapter 5 diagram.

## 6. Build and closure sequence

1. Confirm the working tree and preserve the existing `08_DeepStudy_Ch05/` sandbox; it contains extensive historical drafts and is not an approved final pack.
2. Verify the instructor-list provenance and exact wording from `5-word.json`; preserve the 24-item hierarchy.
3. Verify scan boundaries and printed page numbers from page images; OCR the Chapter 5 spreads locally and label its limitations.
4. Map each vocabulary item, all 12 MCQs, all 24 exercises, and every selected figure to a source locator and a final section. Record exact/equivalent/optional/excluded dispositions without duplicate coverage.
5. Review the external question-bank candidates and include only non-redundant patterns that add practice; keep their authority separate.
6. **Completed preparation gate:** one UML class, one transaction-centered structure chart, and one DFD-to-structure transformation have editable SVG-in-HTML sources, contracts, 2× PNGs, and source-image visual checks. `diagram_forge.py` renders but does not validate semantics. Re-run the source-specific checks on any later edits and extend pilots to other diagram families when the actual question pack needs them.
7. Author one concise consolidated English Q&A pack with Arabic notes/traps outside answers; source-grounded wording in bold, our synthesis in plain text, no “the book says” prefaces, direct answers, and separate locators.
8. Independently check every meaningful claim, answer the question verb, verify diagrams semantically, and check any numerical result if one is genuinely in scope.
9. Run strict lint, export one chapter PDF, check question-answer cohesion and build-marker leaks, and visually inspect all changed/generated diagrams and affected PDF pages.
10. Close only after coverage and source verification are separately complete. State their denominators and limits; do not call linter success or vector retrieval proof of correctness.

## 7. External diagram references

- [OMG UML 2.5.1 specification](https://www.omg.org/spec/UML/2.5.1/PDF) — normative UML semantics and notation.
- [PlantUML language documentation](https://plantuml.com/sitemap-language-specification) — text source for UML diagram families; use current syntax for new diagrams.
- [Mermaid official guide](https://mermaid.js.org/landing/) — supported text-defined diagram types and syntax.
- [Graphviz DOT language](https://www.graphviz.org/content/dot-language/) and [layout documentation](https://graphviz.org/docs/layouts/dot/) — directed graph structure and hierarchical layout.
- [IEEE 1016-2009 overview](https://standards.ieee.org/ieee/1016/4502/) — SDD information content/organization and edition history; it is not a replacement for the course's 1998 citation.

---
*Audit close record — 2026-10-19: strict linter passed on all six packs and the index; all seven PDFs re-exported; zero text-empty pages; corrected FIG-02/04/19 visually compared with their source slides; final count 76 pages. Ready for student review. Not a claim of blind or sentence-by-sentence independent verification.*

