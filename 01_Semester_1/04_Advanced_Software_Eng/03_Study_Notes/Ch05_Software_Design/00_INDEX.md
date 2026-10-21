# Chapter 5 — Software Design (Canonical Index & Deliverables Matrix)

> **Status:** **READY FOR STUDENT REVIEW AFTER TARGETED CROSS-AUDIT (2026-10-19)**  
> **Course:** Advanced Software Engineering (CS603) — Asst. Prof. Dr. Ali Fahim Ni'ma  
> **Primary Authority:** K.K. Aggarwal & Yogesh Singh, *Software Engineering* (3rd ed.), printed pp. 203–249 (spreads 107–130); Companion Slides 1–99.  
> **Published Deliverables:** Six study-pack PDFs plus the canonical index PDF. Final content and diagram corrections are exported and checked; audit scope and limits are recorded in Section 5.

---

## 1. Chapter Deliverables & Master Verification Matrix

Six study packs and the canonical index are print-ready; targeted source/diagram checks and final gates are recorded below:

| Deliverable Artifact | Source Markdown | Compiled PDF | Pages | Items Covered | Delivery Gate Status |
|:---|:---|:---|:---:|:---|:---:|
| **T1 — Multiple-Choice (MCQ)** | [`T1_MCQ.md`](T1_MCQ.md) | [`T1_MCQ.pdf`](T1_MCQ.pdf) | **11 pp** | 25 MCQs (12 publisher slide MCQs 5.1–5.12 + 13 synthesis MCQs) | **Closed** |
| **T2 — Descriptive & Explain** | [`T2_Descriptive.md`](T2_Descriptive.md) | [`T2_Descriptive.pdf`](T2_Descriptive.pdf) | **16 pp** | 17 items (12 textbook exercises + 5 seminar gap items) | **Closed** |
| **T3 — Compare & Analyze** | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | [`T3_Compare_Analyze.pdf`](T3_Compare_Analyze.pdf) | **10 pp** | 13 items (11 textbook exercises + 2 seminar gap items) | **Closed** |
| **T4 — Visual Models & Diagrams** | [`T4_Diagrams.md`](T4_Diagrams.md) | [`T4_Diagrams.pdf`](T4_Diagrams.pdf) | **8 pp** | 5 selected figures (6 semantic-contract entries; 2× PNG redraws) | **Closed** |
| **T5 — Applied Scenarios & Tools** | [`T5_Apply_Scenarios.md`](T5_Apply_Scenarios.md) | [`T5_Apply_Scenarios.pdf`](T5_Apply_Scenarios.pdf) | **12 pp** | 7 items (direct textbook Ex 5.12 + 6 applied scenarios & diagnostics) | **Closed** |
| **V5 — Vocabulary Coverage** | [`V5_Vocabulary_Coverage.md`](V5_Vocabulary_Coverage.md) | [`V5_Vocabulary_Coverage.pdf`](V5_Vocabulary_Coverage.pdf) | **13 pp** | 24 terms from the student-provided professor vocabulary list; provenance is recorded in V5_Doctor_Vocabulary.md | **Closed** |
| **TOTAL CHAPTER OUTPUT** | **6 Markdown Packs** | **6 pack PDFs + index PDF** | **70 pack pages + 6 index pages = 76 pages** | **Final gates passed; bounded review** | **Ready for student review** |

> [!NOTE]
> **Zero Calculation Pack Invariant:**
> Unlike Chapter 4, Chapter 5 contains no computational formulas or numerical estimation models. Structural metrics (such as Fan-In and Fan-Out) are structural heuristics evaluated qualitatively in analytical and applied scenarios (`T3` and `T5`). In accordance with `Ch05_BUILD_PLAN.md`, no artificial calculation pack (`T7`) was fabricated.

---

## 2. Complete Course Question Inventory & Dispositions Ledger

### A. Official Slide MCQs (12 Items)

All 12 publisher-slide MCQ stems and answer keys were cross-checked against slides 94–96 and the cited course pages, then accounted for in `T1_MCQ.md`.

| MCQ | Actual Question Stem | Pack Location | Verified Key | Source Disposition |
|:---:|:---|:---|:---|:---|
| **5.1** | The most desirable form of coupling is: | [`T1_MCQ.md#Q5.1`](T1_MCQ.md) | **(b) Data Coupling** | Verified: Book p. 208; Slide 16, 94. |
| **5.2** | The worst type of coupling is: | [`T1_MCQ.md#Q5.2`](T1_MCQ.md) | **(a) Content coupling** | Verified: Book p. 210; Slide 24, 94. |
| **5.3** | The most desirable form of cohesion is: | [`T1_MCQ.md#Q5.3`](T1_MCQ.md) | **(c) Functional cohesion** | Verified: Book p. 212; Slide 30, 94. |
| **5.4** | The worst type of cohesion is: | [`T1_MCQ.md#Q5.4`](T1_MCQ.md) | **(b) Coincidental cohesion** | Verified: Book p. 211; Slide 26, 94. |
| **5.5** | Which one is not a strategy for design? | [`T1_MCQ.md#Q5.5`](T1_MCQ.md) | **(c) Embedded design** | Verified: Book pp. 213–215; Slide 32, 95. |
| **5.6** | If all task must be executed in the same time-frame, what type of cohesion is being exhibited? | [`T1_MCQ.md#Q5.6`](T1_MCQ.md) | **(c) Cohesion with respect to time** | Verified: Book p. 211; Slide 28, 95. |
| **5.7** | In functional cohesion, each software module performs: | [`T1_MCQ.md#Q5.7`](T1_MCQ.md) | **(a) Single functional task in same procedure** | Verified: Book p. 212; Slide 30, 95. |
| **5.8** | Two modules are said to be ... if they refer to the same global data area: | [`T1_MCQ.md#Q5.8`](T1_MCQ.md) | **(d) Common coupled** | Verified: Book p. 209; Slide 22, 95. |
| **5.9** | What elements of processing are grouped together in a module, in procedural cohesion? | [`T1_MCQ.md#Q5.9`](T1_MCQ.md) | **(c) Procedural cohesion** | Verified: Book p. 211; Slide 28, 96. |
| **5.10** | The relationship of data elements in a module is called: | [`T1_MCQ.md#Q5.10`](T1_MCQ.md) | **(b) Cohesion** | Verified: Book p. 210; Slide 25, 96. |
| **5.11** | A system that does not interact with external environment is: | [`T1_MCQ.md#Q5.11`](T1_MCQ.md) | **(a) Closed system** | Verified: Book p. 204; Slide 2, 96. |
| **5.12** | The extent to which different modules are dependent upon each other is called: | [`T1_MCQ.md#Q5.12`](T1_MCQ.md) | **(a) Coupling** | Verified: Book p. 207; Slide 15, 96. |

---

### B. Textbook Exercises (24 Items)

The publisher exercises are mapped across the pack suite; answer wording was corrected in a targeted cross-audit against the cited material. The review was not a blind audit of every sentence:

| Exercise | Core Topic & Task | Pack Destination | Primary Question ID |
|:---:|:---|:---|:---|
| **5.1** | Define design; contrast conceptual vs technical design | `T2_Descriptive`, `T3_Compare_Analyze`, `T4_Diagrams` | `Q5.D01`, `Q5.D02`, `Q5.C01`, `Q5.V01` |
| **5.2** | Explain design objectives; informal to detailed design | `T2_Descriptive` | `Q5.D03` |
| **5.3** | Distinguish between design and coding; anti-patterns | `T2_Descriptive` | `Q5.D04` |
| **5.4** | Define modularity; Bertrand Meyer's five criteria | `T2_Descriptive`, `T5_Apply_Scenarios` | `Q5.D05`, `Q5.S03` |
| **5.5** | Define coupling; explain six coupling levels | `T2_Descriptive`, `T5_Apply_Scenarios` | `Q5.D06`, `Q5.S04` |
| **5.6** | Define cohesion; explain seven cohesion levels | `T2_Descriptive`, `T5_Apply_Scenarios` | `Q5.D07`, `Q5.S04` |
| **5.7** | Analyze cohesion-coupling duality and quality trade-offs | `T3_Compare_Analyze` | `Q5.C04` |
| **5.8** | Analyze why logical cohesion induces control coupling | `T3_Compare_Analyze` | `Q5.C05` |
| **5.9** | Analyze operational consequences of high coupling | `T3_Compare_Analyze`, `T5_Apply_Scenarios` | `Q5.C06`, `Q5.S04` |
| **5.10** | Analyze architectural consequences of low cohesion | `T3_Compare_Analyze`, `T5_Apply_Scenarios` | `Q5.C07`, `Q5.S04` |
| **5.11** | Compare Top-Down, Bottom-Up, and Hybrid strategies | `T3_Compare_Analyze` | `Q5.C02` |
| **5.12** | Reuse strategy selection (Bottom-Up direct answer + Hybrid scenario) | `T5_Apply_Scenarios` | `Q5.S01`, `Q5.S02` |
| **5.13** | Compare Flowcharts vs Structure Charts | `T3_Compare_Analyze` | `Q5.C03` |
| **5.14** | Explain why different design notations are required | `T2_Descriptive` | `Q5.D08` |
| **5.15** | List function-oriented design techniques & procedure layers | `T2_Descriptive` | `Q5.D09` |
| **5.16** | Define OOD concepts (object, message, abstraction, class, etc.) | `T2_Descriptive` | `Q5.D10` |
| **5.17** | Compare Abstract Data Types (ADTs) and Classes | `T3_Compare_Analyze` | `Q5.C09` |
| **5.18** | Evaluate inheritance without polymorphism | `T3_Compare_Analyze` | `Q5.C10` |
| **5.19** | Explain improvements of OOD over FOD | `T2_Descriptive` | `Q5.D11` |
| **5.20** | Guidelines for reusable, high-quality classes (God Class fix) | `T2_Descriptive`, `T5_Apply_Scenarios` | `Q5.D12`, `Q5.S05` |
| **5.21** | Outline simplified OOAD step-by-step process | `T2_Descriptive` | `Q5.D13` |
| **5.22** | Comprehensive comparison: FOD vs OOD | `T3_Compare_Analyze` | `Q5.C11` |
| **5.23** | Documents produced upon design completion; IEEE 1016 SDD | `T2_Descriptive`, `T5_Apply_Scenarios` | `Q5.D14`, `Q5.S07` |
| **5.24** | Critical evaluation: Complete decoupling ($Coupling=0$) | `T3_Compare_Analyze` | `Q5.C08` |

---

### C. Professor-Seminar Gap Coverage

The specific topics highlighted in the instructor seminar review are fully resolved with primary page anchors:

| Seminar Topic | Source & Anchor | Pack Location | Question ID |
|:---|:---|:---|:---|
| **Abstraction Forms (Procedural, Data, Control)** | Pressman 5e §13.4.1 (printed pp. 342–343) | `T2_Descriptive` | `Q5.D15` |
| **Stepwise Refinement (Wirth)** | Pressman 5e §13.4.2 (printed pp. 343–344) | `T2_Descriptive` | `Q5.D16` |
| **Information Hiding (Parnas)** | Pressman 5e §13.4.4 (printed p. 352) | `T2_Descriptive` | `Q5.D16` |
| **Meyer's Five Modularity Criteria** | Pressman 5e §13.4.3 (printed p. 345) | `T2_Descriptive`, `T5_Apply_Scenarios` | `Q5.D05`, `Q5.S03` |
| **Fan-In / Fan-Out Metrics & Depth/Width** | Pressman 5e §13.4.5; Mall 4e §5.4 | `T3_Compare_Analyze`, `T5_Apply_Scenarios` | `Q5.C12`, `Q5.S06` |
| **Formal Design Review Protocol** | Rajib Mall 4e §6.7 (printed pp. 350–351) | `T2_Descriptive`, `T5_Apply_Scenarios` | `Q5.D17`, `Q5.S07` |
| **DFD Transform vs Transaction Analysis** | Rajib Mall 4e §6.4.1 (printed pp. 344–349) | `T3_Compare_Analyze`, `T4_Diagrams` | `Q5.C13`, `Q5.V05` |

---

## 3. Supporting-Source Gap-Check Ledger (24 Terms x 5 Candidate Sources)

In accordance with Section 2.5 of `AGENTS.md`, the 24 terms attributed by the student to the professor were mapped against the course source and candidate supporting books. This ledger records intended/useful coverage; it is not a claim that every cell received an exhaustive page-level audit:

| # | Vocabulary Leaf Term | Primary: Aggarwal & Singh | Cand 1: Pressman 5e | Cand 2: Mall 4e | Cand 3: Sommerville | Cand 4: B.B. Agarwal |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| **1** | What is Design? | **Sufficient (pp. 203–204)** | Confirmed | Confirmed | Confirmed | Redundant |
| **2** | Conceptual vs Technical Design | **Sufficient (pp. 204–205)** | Confirmed | Not used | Confirmed | Redundant |
| **3** | Objectives of Design | **Sufficient (pp. 203, 206)** | Confirmed | Confirmed | Confirmed | Redundant |
| **4** | Why Design is Important? | **Sufficient (pp. 203–204)** | Confirmed | Confirmed | Confirmed | Redundant |
| **5** | Modularity | **Gap filled by Pressman** | **Primary Gap Source (§13.4.3)** | Confirmed | Confirmed | Redundant |
| **6** | Module Coupling | **Sufficient (pp. 207–210)** | Confirmed | Confirmed | Confirmed | Redundant |
| **7** | Module Cohesion | **Sufficient (pp. 210–213)** | Confirmed | Confirmed | Confirmed | Redundant |
| **8** | Cohesion-Coupling Relationship | **Sufficient (pp. 212–213)** | Confirmed | Confirmed | Confirmed | Redundant |
| **9** | Strategy of Design | **Sufficient (pp. 213–215)** | Confirmed | Confirmed | Confirmed | Redundant |
| **10** | Bottom-Up Design | **Sufficient (pp. 213–214)** | Confirmed | Confirmed | Confirmed | Redundant |
| **11** | Top-Down Design | **Sufficient (pp. 214–215)** | Confirmed | Confirmed | Confirmed | Redundant |
| **12** | Hybrid Design | **Sufficient (p. 215)** | Confirmed | Confirmed | Confirmed | Redundant |
| **13** | Function Oriented Design | **Sufficient (pp. 216–220)** | Confirmed | Confirmed | Confirmed | Redundant |
| **14** | Design Notations | **Sufficient (pp. 216–221)** | Confirmed | Confirmed | Confirmed | Redundant |
| **15** | Functional Procedure Layers | **Sufficient (pp. 220–221)** | Confirmed | Confirmed | Confirmed | Redundant |
| **16** | IEEE SDD Recommended Practice | **Sufficient (pp. 221–224)** | Not used | Not used | Confirmed | Redundant |
| **17** | SDD Scope | **Sufficient (p. 221)** | Not used | Not used | Confirmed | Redundant |
| **18** | SDD Definitions | **Sufficient (pp. 221–222)** | Not used | Not used | Confirmed | Redundant |
| **19** | Purpose of an SDD | **Sufficient (p. 222)** | Not used | Not used | Confirmed | Redundant |
| **20** | SDD Information Content | **Sufficient (pp. 222–223)** | Not used | Not used | Confirmed | Redundant |
| **21** | SDD Organisation | **Sufficient (pp. 223–225)** | Not used | Not used | Confirmed | Redundant |
| **22** | Object Oriented Design | **Sufficient (pp. 225–226)** | Confirmed | Confirmed | Confirmed | Redundant |
| **23** | Basic Concepts | **Sufficient (pp. 226–230)** | Confirmed | Confirmed | Confirmed | Redundant |
| **24** | Steps to Analyze & Design OOS | **Sufficient (pp. 231–233)** | Confirmed | Confirmed | Confirmed | Redundant |

---

## 4. Diagram Registry & Verification Status

Five selected figures are embedded in T4. Six contract entries cover those figures, with RMS represented by separate DFD and structure-chart contracts. This is a selected visual set, not exhaustive coverage of every figure in the chapter:

| Figure ID | Formal Title & Notation | Source Anchor | Editable HTML Source | Rendered 2× Asset | Semantic Gate |
|:---:|:---|:---|:---|:---|:---:|
| **FIG-02** | Two-Part Design Process (What vs How) | Slide 5, Fig. 2 | [`CH05-FIG02_Two-Part-Design-Process.html`](diagrams/CH05-FIG02_Two-Part-Design-Process.html) | [`CH05-FIG02_Two-Part-Design-Process.png`](diagrams/CH05-FIG02_Two-Part-Design-Process.png) | **Passed** |
| **FIG-04** | Modularity and Software Cost Curve | Slide 14, Fig. 4 | [`CH05-FIG04_Modularity-and-Software-Cost.html`](diagrams/CH05-FIG04_Modularity-and-Software-Cost.html) | [`CH05-FIG04_Modularity-and-Software-Cost.png`](diagrams/CH05-FIG04_Modularity-and-Software-Cost.png) | **Passed** |
| **FIG-19** | Transaction-Centered Structure Chart | Slides 42, 44 | [`CH05-FIG19_Transaction-Centered-Structure-Chart.html`](diagrams/CH05-FIG19_Transaction-Centered-Structure-Chart.html) | [`CH05-FIG19_Transaction-Centered-Structure-Chart.png`](diagrams/CH05-FIG19_Transaction-Centered-Structure-Chart.png) | **Passed** |
| **FIG-23** | UML Class Generalization (`Shape`) | Slide 68, Fig. 23 | [`CH05-FIG23_Shape-Inheritance.html`](diagrams/CH05-FIG23_Shape-Inheritance.html) | [`CH05-FIG23_Shape-Inheritance.png`](diagrams/CH05-FIG23_Shape-Inheritance.png) | **Passed** |
| **GAP-RMS**| RMS DFD Transform Analysis to Structure Chart | Mall 4e §6.4.1 | [`CH05-GAP_RMS_DFD-to-Structure-Chart.html`](diagrams/CH05-GAP_RMS_DFD-to-Structure-Chart.html) | [`CH05-GAP_RMS_DFD-to-Structure-Chart.png`](diagrams/CH05-GAP_RMS_DFD-to-Structure-Chart.png) | **Passed** |

---

## 5. Audit Status and Quality Gates

The chapter is ready for student review after a targeted, multi-agent cross-audit and remediation. Three read-only reviews covered source claims, diagrams/vocabulary, and print delivery; Codex then checked source pages, corrected the substantiated issues, re-exported the packs, and visually inspected changed pages. This was not a blind claim-by-claim verification of every sentence or every source figure.

- All six study-pack Markdown files and this index pass `note_linter.py --strict`.
- All seven PDFs were freshly exported; the total is **76 pages**, with zero text-empty pages.
- The changed pages and corrected FIG-02, FIG-04, and FIG-19 redraws were visually inspected. Other selected figures retain prior review; the atlas lists chapter figures not reproduced in T4.
- The 24-term list is attributed to the professor by the student; the original group post is not in the vault.
- No claim is made that question counts equal exam weighting or that every sentence received exhaustive independent verification.

## Retrieval set

1. **What do the four Functional Procedure Layers represent?** Four increasing levels of detail for specifying a procedure, from purpose and relationships to a procedure body.
2. **Which modules are conditional alternatives in FIG-19?** Module 1, Module 2, and Module 3; Input and Output are direct calls from MAIN.
3. **What are the four SDD design views listed in the course material?** Decomposition, Dependency, Interface, and Detail Description.

---
*Current status: ready for student review; close the study loop with your own reading and corrections.*
