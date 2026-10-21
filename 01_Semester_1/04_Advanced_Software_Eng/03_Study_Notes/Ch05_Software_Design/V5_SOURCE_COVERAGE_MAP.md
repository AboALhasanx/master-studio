# Chapter 5 — Source and Coverage Map

> **Purpose:** lock the scope, question inventory, diagram families, and gaps before authoring the final consolidated English Q&A pack. This is a preparation map, not a closed answer pack. “Coverage” means a planned place to answer a topic; source verification still requires the original page or slide.

## 1. Confirmed scope and source boundaries

- **Student-attributed instructor list:** 24 terms in `V5_Doctor_Vocabulary.md`. The transcript `5-word.json` messages 273/284 preserves the list, but the original instructor group post is not attached.
- **Primary course-aligned prose source:** K.K. Aggarwal & Yogesh Singh, *Software Engineering*, 3rd edition, high-confidence identity inferred because the scanned file lacks its title page. Chapter 5 is printed pp.203–249. The visual anchor is `source_figures/book-spread-107.png`: p.202 on the left belongs to Chapter 4; Chapter 5 begins on the right at p.203.
- **Companion publisher slides:** same authors/title/edition family, separate evidence type; 99 slides. Cite slide-only content as slides.
- **Official question inventory:** source MCQs 5.1–5.12 on printed pp.248–249 / slides 94–96; 24 exercises 5.1–5.24 on printed p.249 / slides 97–99. The book scan visually confirms the same inventory. These counts describe supplied questions only; they are not exam marks or probability.
- **Targeted gap sources:** follow the doctor profile's Pressman 5e (PDF pp.370–380 / printed pp.342–352) for abstraction, refinement, information hiding, and hierarchy metrics; Rajib Mall 4e (PDF pp.300–301, 344–349 and 350–352) for fan-in/fan-out, DFD transformation, and design review. These are gap-only candidates, not the course primary; inspect exact pages before final citation. B.B. Agarwal et al. 2010, Sommerville and Leach received a term-hit scan but are not selected/indexed because no unique gap has yet been established. External question banks are practice-only.

## 2. Instructor vocabulary → planned coverage

The slide ranges below are navigational anchors from the 99-slide deck, not textbook page citations. The scanned book text is indexed locally; exact printed subsection/page anchors must be confirmed before a final answer is cited.

| # | Instructor wording | Initial course-source route | Exercise/MCQ anchors | Planned question form |
|---:|---|---|---|---|
| 1 | What is Design? | Book pp.203–206; slides 2–9 | Ex 5.1, 5.3 | Define; distinguish design from coding |
| 2 | Conceptual and Technical Designs | Book pp.203–206; slides 4–5 | Ex 5.1 | Compare with purpose and outputs |
| 3 | Objectives of Design | Book pp.203–206; slides 2–14 | Ex 5.2, 5.7 | List and explain; connect to quality |
| 4 | Why Design is Important? | Book pp.203–206; slides 2–14 | Ex 5.2–5.3 | Explain design as bridge from requirements to implementation |
| 5 | Modularity | Book pp.206–213; slides 14–18 | Ex 5.4, 5.7, 5.24 | Define; assess modularity and trade-offs |
| 6 | Module Coupling | Book pp.207–210; slides 15–24 | MCQ 5.1–5.2, 5.8, 5.12; Ex 5.5, 5.8–5.9, 5.24 | Define; rank/classify; analyze impact |
| 7 | Module Cohesion | Book pp.210–213; slides 25–30 | MCQ 5.3–5.4, 5.6–5.7, 5.9–5.10; Ex 5.6–5.8, 5.10 | Define; distinguish/rank seven forms; diagnose |
| 8 | Relationship between Cohesion & Coupling | Book pp.212–213; slide 31 | Ex 5.7–5.10, 5.24 | Explain target relation and analyze consequences |
| 9 | Strategy of Design | Book pp.213–215; slides 32–35 | MCQ 5.5; Ex 5.11–5.12 | Compare strategies; choose with rationale |
| 10 | Bottom-Up Design | Book pp.213–215; slide 33 | Ex 5.11–5.12 | Explain with a hierarchy/reuse example |
| 11 | Top-Down Design | Book pp.213–215; slide 34 | Ex 5.11–5.12 | Explain decomposition direction and trade-offs |
| 12 | Hybrid Design | Book pp.213–215; slide 35 | Ex 5.11–5.12 | Explain how top-down decomposition uses existing lower-level modules |
| 13 | Function Oriented Design | Book pp.216–220; slides 36–45 | Ex 5.15, 5.22 | Explain decomposition; compare with OOD |
| 14 | Design Notations | Book pp.216–221; slides 41–49 | Ex 5.13–5.15 | Identify and compare notations; select by view |
| 15 | Functional Procedure Layers | Book pp.220–221; slides 47–49 | Ex 5.15 and feedback gap set | Explain layer purpose and what each reveals |
| 16 | IEEE Recommended Practice for Software Design Descriptions | Book pp.221–224; slides 50–57 | Ex 5.23 | Purpose, structure, views, and information content; retain IEEE 1016-1998 course edition |
| 17 | Scope | IEEE SDD material, p.221; slide 50 | Ex 5.23 | State what SDD guidance covers; verify against course edition |
| 18 | Definitions | IEEE SDD material, pp.221–222; slide 51 | Ex 5.23 | Identify defined terms only where the source lists them |
| 19 | Purpose of an SDD | IEEE SDD material, p.222; slide 52 | Ex 5.23 | Explain audience/use and design communication |
| 20 | Design Description Information Content | IEEE SDD material, pp.222–223; slides 52–53 | Ex 5.23 | List information elements/views without inventing mandatory fields |
| 21 | Design Description Organisation | IEEE SDD material, pp.223–225; slides 54–57 | Ex 5.23 | Explain organization/views; distinguish content from arrangement |
| 22 | Object Oriented Design | Book pp.225–249; slides 58–93 | Ex 5.19–5.22 | Explain and compare against function-oriented design |
| 23 | Basic Concepts | Book pp.225–230; slides 59–71 | Ex 5.16–5.20 | Define object, message, class, abstraction, inheritance, polymorphism; reason about class quality/reuse |
| 24 | Steps to Analyze and Design Object Oriented System | Book pp.231–249; slides 72–93 | Ex 5.21, 5.23 | Order steps and identify outputs/conditional steps |

## 3. Official MCQ and exercise inventory

### Source MCQs (12)

`5.1` desirable coupling · `5.2` worst coupling · `5.3` desirable cohesion · `5.4` worst cohesion · `5.5` non-strategy distractor · `5.6` temporal cohesion · `5.7` functional cohesion · `5.8` common coupling · `5.9` procedural cohesion · `5.10` cohesion definition · `5.11` closed system · `5.12` coupling definition.

**Answer-key status:** the publisher deck/book inventory supplies stems and options, not a publisher answer key. Verify each correct answer independently from the course source; mark any ambiguous or defective item before adopting a key. Slide 96 visually orders 5.12 before 5.11; preserve the question numbers.

### Source exercises (24)

| Exercise | Dominant task | Main coverage |
|---:|---|---|
| 5.1 | Compare | design; conceptual vs technical |
| 5.2 | Explain/process | objectives; informal-to-detailed design |
| 5.3 | Explain/distinguish | design vs coding |
| 5.4 | Define/list | modularity + Meyer’s five modularity criteria (decomposability, composability, understandability, continuity, protection) |
| 5.5 | Define/explain | coupling forms |
| 5.6 | Define/explain | cohesion forms |
| 5.7 | Explain/analyze | objectives; effects of coupling/cohesion |
| 5.8 | Analyze | logical cohesion and likely coupling |
| 5.9 | Analyze | high-coupling consequences |
| 5.10 | Analyze | low-cohesion consequences |
| 5.11 | Compare/evaluate | design strategies; popularity/practicality |
| 5.12 | Apply/justify | reuse and strategy selection |
| 5.13 | Compare | flowchart vs structure chart |
| 5.14 | Explain | why design notations differ |
| 5.15 | List | established function-oriented techniques |
| 5.16 | Define | objects, messages, abstraction, class, inheritance, polymorphism |
| 5.17 | Compare | abstract data types and classes |
| 5.18 | Evaluate/explain | inheritance without polymorphism |
| 5.19 | Explain | claimed improvement through OOD |
| 5.20 | Explain/list | good-quality/reusable class guidelines |
| 5.21 | List/order | simplified design process |
| 5.22 | Compare | object-oriented vs function-oriented design |
| 5.23 | List/explain | documents after design completion; SDD scope |
| 5.24 | Evaluate | possibility/limits of complete decoupling |

The dominant-task grouping is a planning aid only: the same exercise may require more than one response action. It must not be turned into an exam-weight claim.

## 4. Professor-feedback additions not to lose

These are separate coverage signals, not extra instructor-list entries. Add only short, useful question(s) or diagram drills where the seminar feedback supports them:

- **Abstraction:** procedural, data, and control abstraction. Pressman 5e, candidate printed pp.342–343.
- **Stepwise refinement:** Pressman §13.4.2, candidate PDF p.371; confirm the printed-page label.
- **Information hiding:** Pressman 5e, candidate printed p.352 (PDF p.380); verify exact wording in the page image.
- **Fan-in/fan-out** and **design hierarchy depth/width:** Pressman §13.4.5, candidate PDF p.375; Mall §5.4, PDF pp.300–301 provides the alternate treatment.
- **Design review**: purpose, participants, and review concerns.
- **DFD → structure chart:** transform analysis and transaction analysis, with a small fully specified example. Use Mall §6.4.1 candidate pages (PDF 344–349) only after printed-page/section verification.
- **“Properties” is resolved:** the student confirmed on 2026-10-19 that it means Meyer’s five modularity criteria. Cover them within the existing modularity/properties scope and Exercise 5.4; do not count them as a new vocabulary-list leaf. Verified support: Pressman, 5th ed., §13.4.3, printed p.345 / PDF p.373. Keep distinct from unrelated properties of architectural design.

## 5. Question-form effort mix (not exam marks)

The 36 source prompts give the chapter's baseline: 12 publisher MCQs (one-third of the supplied prompt count) plus 24 written exercises (two-thirds). Within the exercises, direct comparison, explanation, definition/list, and analysis/evaluation all recur; no source exercise explicitly asks for a full UML drawing or a numerical calculation. The final pack should therefore preserve all 36 source prompts, then add a small non-duplicative practice set for the identified diagram and seminar-feedback gaps.

Initial authoring allocation for the **additional practice set only** (adjust after mapping the official questions and the professor's list):

| Form | Suggested share of added practice | Why it belongs |
|---|---:|---|
| Short answer / define / list / explain | 25% | Most vocabulary items and several exercises require direct responses |
| Compare / classify / analyze | 20% | Coupling/cohesion, strategies, notations, and OOD/functional contrasts |
| Source-diagram interpretation | 20% | Slides contain many notations and semantically distinct diagrams |
| Diagram construction / transformation | 20% | Practice structure charts, UML views, and the professor-requested DFD transformation |
| Scenario selection / evaluation | 15% | Reuse choices, class quality, decoupling, and design review |
| Calculation | 0% unless primary source inventory reveals a genuine in-scope numerical task | Avoid inventing math where the chapter has no calculation spine |

These percentages allocate **practice-authoring effort**, not marks, examination likelihood, or the percentage of chapter content.

## 6. Diagram families to map and teach

1. Conceptual design/process framework and conceptual-vs-technical view.
2. Qualitative modularity/cost curve (no invented numeric coordinates).
3. Coupling example diagrams and the six-level coupling taxonomy.
4. Seven-level cohesion taxonomy and the coupling/cohesion target.
5. Bottom-up, top-down, hybrid, function-decomposition and structure charts.
6. Structure-chart symbols, data/control couples, update-file and transaction-centered examples.
7. Functional procedure layers and design-notation/document-view tables.
8. UML/OOD: object instance vs class; classes/abstraction/generalization; activity; interaction/sequence/collaboration; entity/boundary/control roles; class relationships; state; component vs deployment; use case and library case.
9. Feedback-only DFD → structure-chart transformation: preserve data-flow vs module-call semantics and the chosen DFD notation.

Use `V5_DIAGRAM_ATLAS.md`, `V5_DIAGRAM_CONTRACT_TEMPLATE.json`, and the source renders under `source_figures/` as a bundled visual grounding layer.

## 7. Open checks before final pack authoring

- OCR and inspect scan spreads 107–130; verify textbook section/page locators for each vocabulary group and every answer claim.
- Independently solve all 12 MCQs; distinguish original source wording from any corrected/clarified note.
- Check all 24 exercises in the scan against slides 97–99; record omissions or wording differences.
- Inspect slides 50–57 and the exact course IEEE 1016-1998 content before claiming SDD fields are mandatory.
- Verify targeted B.B. Agarwal, Pressman, and Mall printed-page labels and ensure each fills a documented hole in the primary material.
- Review external bank items for non-redundancy only; do not copy unsupported answer claims.
- The UML-class, transaction-centered structure-chart, and DFD-to-structure-chart pilots are complete and source-image compared. This verifies the workflow only; add further diagram contracts only when the final pack requires those diagram families.

---
*Prepared by Codex on 2026-10-19; scope map and proposed mix remain subject to source checking and student review.*
