---
title: "Chapter 9 — Software Maintenance: Master Index & Verification Matrix"
subtitle: "Canonical Deliverables Ledger, Question Inventory, Equation Register & Audit Matrix"
course: "Advanced Software Engineering (CS603)"
instructor: "Asst. Prof. Dr. Ali Fahim Ni'ma"
author: "Master Studio Engine"
date: "2026-10-23"
lang: "en"
---

# Chapter 9: Software Maintenance — Master Index & Verification Matrix

> **Master Chapter Governance Index:** Maps the publisher inventory (25 MCQs and 40 exercises) to six authored packs. Dr. Ali Fahim’s official Chapter 9 vocabulary/notes have not been supplied, so the current coverage map remains predictive rather than confirmed exam scope.

---

## 1. Master Deliverables Ledger

All deliverables adhere strictly to the **Zero-Defect Delivery Gate** (`note_linter.py --fix --strict` $\to$ Code 0) and DirectWrite typography standards.

| Deliverable ID | Markdown Source | Publication PDF | Scope & Description | Items | Status |
|:---|:---|:---|:---|:---:|:---:|
| **T1_MCQ** | `T1_MCQ.md` | `T1_MCQ.pdf` | All 25 Publisher MCQs (Q9.1–Q9.25) checked 100% against textbook printed answer key (pp. 499–500) | 25 MCQs | **KEY MATCHED · PRINT QA PASSED** |
| **T2_Descriptive** | `T2_Descriptive.md` | `T2_Descriptive.pdf` | Direct conceptual definitions, categories, maintenance models, documentation, SCM (CCA), and maintainability | 25 Exercises | **REVISED · STRICT GATE PASSED** |
| **T3_Compare_Analyze** | `T3_Compare_Analyze.md` | `T3_Compare_Analyze.pdf` | Structured analytical evaluations (Manageability, Development vs Maintenance, Ripple Effect & Stability, Dev vs Regression Testing, RTS, SESE control flow, Coupling) | 12 Exercises | **STRICT GATE PASSED** |
| **T4_Diagrams** | `T4_Diagrams.md` | `T4_Diagrams.pdf` | Complete source-extracted figures (Process, Boehm, Taute, 18-field Change Request Form with CCA, reverse-engineering levels and domain mapping) | 5 prompts / 6 figures | **SOURCE CROPS CHECKED · PRINT QA PASSED** |
| **T5_Apply_Select** | `T5_Apply_Select.md` | `T5_Apply_Select.pdf` | Realistic engineering scenarios (Model Selection Matrix, Ex 9.29 8 Canonical Legacy Code Recommendations, Selective Regression Deltas, SCM Workflow, Re-engineer vs New Dev Economics) | 5 Scenarios | **PRINT NOTES SUPPRESSED · STRICT GATE PASSED** |
| **T7_Calculations** | `T7_Calculations.md` | `T7_Calculations.pdf` | Rigorous 8-part quantitative models (Belady-Lehman effort, Familiarity sensitivity, Boehm ACT/AME/10-Yr Total with slide typo correction, Very High EAF Cost Drivers, Life-cycle Cost) [pp. 490–491] | 5 Problems | **PRINT NOTES SUPPRESSED · STRICT GATE PASSED** |
| **Complete Print Pack** | — | `Ch09_Software_Maintenance_Print.pdf` | Unified comprehensive study volume compiling T1, T2, T3, T4, T5, and T7 with hierarchical bookmarks | **42 Pages** | **REBUILT · PRINT QA PASSED** |

---

## 2. Publisher Exercise Inventory Mapping (Exercises 9.1 – 9.40)

This table records the current mapping of the companion-slide exercise inventory (pp. 70–75) to the study packs:

| Exercise | Canonical Topic / Stem | Study Pack | Question ID | Focus & Notes |
|:---:|:---|:---:|:---:|:---|
| **9.1** | What is software maintenance? Describe various categories of maintenance. Which category consumes maximum effort and why? | `T2_Descriptive` | Q9.D1 | IEEE 610.12 definition, 4 categories, Perfective 50% |
| **9.2** | What are the implication of maintenance for a one person software production organisation? | `T2_Descriptive` | Q9.D2 | 100% time absorption, lack of independent review, bus factor 1 |
| **9.3** | Some people feel that "maintenance is manageable". What is your opinion about this issue? | `T3_Compare_Analyze` | Q9.A1 | Disciplined engineering vs legacy realities |
| **9.4** | Discuss various problems during maintenance. Describe some solutions to these problems. | `T2_Descriptive` | Q9.D3 | Unstructured code, turnover, ripple effect; CCA, regression testing |
| **9.5** | Why do you think that the mistake is frequently made of considering software maintenance inferior to software development? | `T3_Compare_Analyze` | Q9.A2 | Clean-slate bias, cognitive asymmetry, intellectual difficulty |
| **9.6** | Explain the importance of maintenance. Which category consumes maximum effort and why? | `T2_Descriptive` | Q9.D4 | Capital preservation, business continuity; Perfective 50% |
| **9.7** | Explain the steps of software maintenance with help of a diagram. | `T4_Diagrams` / `T2` | Q9.F1 / Q9.D5 | Fig 9.2: 4 phases, quality attributes, Pass testing? gate |
| **9.8** | What is self descriptiveness of a program? Explain the effect of this parameter on maintenance activities. | `T2_Descriptive` | Q9.D6 | Meaningful identifiers, comment density, program understanding speed |
| **9.9** | What is ripple effect? Discuss the various aspects of ripple effect and how does it affect the stability of a program? | `T3_Compare_Analyze` | Q9.A3 | Book p. 465 definition: resistance to change amplification |
| **9.10** | What is maintainability? What is its role during maintenance? | `T2_Descriptive` | Q9.D7 | IEEE 610.12 definition; synthesis of attributes across all 4 phases |
| **9.11** | Describe Quick-fix model. What are the advantage and disadvantage of this model? | `T2_Descriptive` / `T5` | Q9.D8 / Scen 1 | Speed in emergency vs architectural decay and lost sync |
| **9.12** | How iterative enhancement model is helpful during maintenance? Explain the various stage cycles of this model. | `T2_Descriptive` / `T5` | Q9.D9 / Scen 1 | Fig 9.4: Analysis $\to$ Redesign $\to$ Implementation cycle |
| **9.13** | Explain the Boehm's maintenance model with the help of a diagram. | `T4_Diagrams` | Q9.F2 | Fig 9.6: Understand, Strategy, Validate, Verify, Retest |
| **9.14** | State the various steps of reuse oriented model. Is it a recommended model in object oriented design? | `T2_Descriptive` / `T5` | Q9.D10 / Scen 1 | Identify, Analyze, Modify, Integrate; highly recommended in OO |
| **9.15** | Describe the Taute maintenance model. What are various phases of this model? | `T2_Descriptive` / `T4` | Q9.D11 / Q9.F3 | Fig 9.7: 8 phases (Change request, Estimate, Schedule, Program, Test, Documentation, Release, Operation) |
| **9.16** | Write a short note on Belady and Lehman model for the calculation of maintenance effort. | `T2_Descriptive` | Q9.D12 | $M = P + K \cdot e^{c - d}$; exponential complexity vs familiarity |
| **9.17** | Describe various maintenance cost estimation models. | `T2_Descriptive` | Q9.D13 | Defect ratio (1:10:100), Belady-Lehman, Boehm ACT/AME |
| **9.18** | The development effort for a project is 600 PMs. The empirically determined constant (K) of Belady and Lehman model is 0.5. The complexity of code is quite high and is equal to 7. Calculate the total effort expended (M) if maintenance team has reasonable level of understanding of the project (d=0.7). | `T7_Calculations` | Q9.C1 | Scanned book printed p. 491: $M = 600 + 0.5 e^{6.3} = 872.29\text{ PM}$ |
| **9.19** | Annual change traffic (ACT) in a software system is 25% per year. The initial development cost was Rs. 20 lacs. Total life time for software is 10 years. What is the total cost of the software system? | `T7_Calculations` | Q9.C5 | Scanned book printed p. 491: $AMC=5\text{ lacs}, M_{10}=50\text{ lacs}, Total=70\text{ lacs}$ |
| **9.20** | What is regression testing? Differentiate between regression and development testing? | `T3_Compare_Analyze` | Q9.A4 | Multi-dimensional comparison: objective, suite dynamics, automation |
| **9.21** | What is the importance of regression test selection? Discuss with help of examples. | `T3_Compare_Analyze` | Q9.A5 | Computational expense of Retest-All; delta trace selection example |
| **9.22** | What are selective retest techniques? How are they different from "retest-all" techniques? | `T3_Compare_Analyze` | Q9.A6 | Retest-all vs Selective retest trade-offs and safety criteria |
| **9.23** | Explain the various categories of retest techniques. Which one is not useful and why? | `T3_Compare_Analyze` | Q9.A7 | Coverage vs Minimization vs Safe; minimization is non-safe |
| **9.24** | What are the categories to evaluate regression test selection techniques? Why do we use such categorisation? | `T3_Compare_Analyze` | Q9.A8 | Rothermel & Harrold: Inclusiveness, Precision, Efficiency, Generality |
| **9.25** | What is reverse engineering? Discuss levels of reverse engineering. | `T2_Descriptive` / `T4` | Q9.D14 / Q9.F5 | Fig 9.11: Implementation, Design, Specification levels; Redocumentation, Recovery |
| **9.26** | What are the appropriate reverse engineering tools? Discuss any two tools in detail. | `T2_Descriptive` | Q9.D15 | Parsers (AST generation) and Call-Graph Extractors (control flow) |
| **9.27** | Discuss reverse engineering and re-engineering. | `T3_Compare_Analyze` | Q9.A9 | Analysis/comprehension vs full transformation lifecycle |
| **9.28** | What is re-engineering? Differentiate between re-engineering and new development. | `T3_Compare_Analyze` | Q9.A10 | Fig 9.12: System Spec vs Existing System trajectory; Sneed's rule |
| **9.29** | Discuss the suggestions that may be useful for the modification of the legacy code. | `T5_Apply_Select` / `T2` | Scen 2 / Q9.D16 | 8 canonical textbook suggestions (Slide 49 / Book p. 480) |
| **9.30** | Explain various types of restructuring techniques. How does restructuring help in maintaining a program? | `T2_Descriptive` | Q9.D17 | Control flow driven, Efficiency driven, Adaption driven (Slides 51–53) |
| **9.31** | Explain why single entry, single exit modules make testing easier during maintenance. | `T3_Compare_Analyze` | Q9.A11 | Structured control flow, predictable preconditions/postconditions |
| **9.32** | What are configuration management activities? Draw the performa of change request form. | `T2` / `T4` / `T5` | Q9.D18 / Q9.F4 / Scen 4 | 4 SCM activities, CCA authority, 18-field Form (Book p. 485) |
| **9.33** | Explain why the success of a system depends heavily on the quantity of the documentation generated during system development. | `T2_Descriptive` | Q9.D19 | Documentation preserves system knowledge; maintenance uses about 40–70% of life-cycle cost (printed p. 459) |
| **9.34** | What is an appropriate set of tools and documents required to maintain large software product? | `T2_Descriptive` | Q9.D20 | SRS, SDD, code, test suites; SCM, cross-ref, call-graphs |
| **9.35** | Explain why a high degree of coupling among modules can make maintenance very difficult. | `T3_Compare_Analyze` | Q9.A12 | Amplifies ripple effect, destroys module isolation, forces Retest-All |
| **9.36** | Is it feasible to specify maintainability in the SRS? If yes, how would we specify it? | `T2_Descriptive` | Q9.D21 | Quantitative metrics: MTTR $\le 2$h, complexity ceilings, modularity limits |
| **9.37** | What tools and techniques are available for software maintenance? Discuss any two of them. | `T2_Descriptive` | Q9.D22 | Program slicing (isolating variable state) and automated restructuring |
| **9.38** | Why is maintenance programming becoming more challenging than new development? What are desirable characteristics of a maintenance programmer? | `T2_Descriptive` | Q9.D23 | Cognitive constraints, regression risks; reverse engineering aptitude |
| **9.39** | Why little attention is paid to maintainability during design phase? | `T2_Descriptive` | Q9.D24 | Schedule pressure, separate cost centers, lack of immediate visibility |
| **9.40** | List out system documentation and also explain their purpose. | `T2_Descriptive` | Q9.D25 | Seven Table 9.6 categories: system rationale, SRS, specification/design, implementation, system test plan, acceptance test plan, data dictionaries |

---

## 3. Publisher MCQ Master Register (Questions 9.1 – 9.25)

All 25 publisher MCQs are verified 100% against the official publisher answer key in the scanned reference textbook (printed pp. 499–500, PDF spreads 254–255):

| MCQ ID | Topic / Question Stem | Verified Key | Source Option Text | Locators |
|:---:|:---|:---:|:---|:---|
| **9.1** | Re-engineering is also known as | **(c)** | Reverse Engineering | Book pp. 476, 488, 499; Slide 64 |
| **9.2** | Retesting the software after changes is called | **(d)** | Maintenance testing | Book pp. 473, 488, 499; Slide 64 |
| **9.3** | Maintenance is NOT classified as | **(b)** | Effective maintenance | Book pp. 460, 488, 499; Slide 64 |
| **9.4** | Rectifying errors identified during operation | **(a)** | Corrective maintenance | Book pp. 460, 488, 499; Slide 65 |
| **9.5** | Quick-fix model may be used for | **(a)** | Emergency fixes | Book pp. 466, 488, 499; Slide 65 |
| **9.6** | Adaptive maintenance is modification to | **(d)** | Match changes in ever-changing environment | Book pp. 460, 488, 499; Slide 65 |
| **9.7** | Maintenance process includes | **(d)** | All of the above | Book pp. 463, 488, 499; Slide 65 |
| **9.8** | Modification to enhance performance/maintainability | **(c)** | Perfective | Book pp. 460, 488, 499; Slide 66 |
| **9.9** | Modification to detect/correct latent faults | **(d)** | Preventive | Book pp. 460, 488, 499; Slide 66 |
| **9.10** | Maintenance model NOT based on | **(a)** | CMM | Book pp. 466, 489, 499; Slide 66 |
| **9.11** | Model where changes are made without updating docs | **(b)** | Quick-fix model | Book pp. 466, 489, 499; Slide 66 |
| **9.12** | Iterative enhancement model is a | **(a)** | Three stage model | Book pp. 466, 489, 499; Slide 67 |
| **9.13** | Taute maintenance model consists of | **(c)** | Eight phases | Book pp. 469, 489, 499; Slide 67 |
| **9.14** | ACT stands for | **(c)** | Annual change traffic | Book pp. 472, 489, 499; Slide 67 |
| **9.15** | Regression testing is | **(a)** | Retesting modified parts of software | Book pp. 473, 489, 499; Slide 67 |
| **9.16** | Regression testing techniques are | **(d)** | All of the above | Book pp. 474, 489, 499; Slide 68 |
| **9.17** | Selective retest technique is | **(c)** | Both (a) and (b) | Book pp. 474, 489, 499; Slide 68 |
| **9.18** | Regression test selection technique NOT based on | **(d)** | Maximization technique | Book pp. 475, 490, 499; Slide 68 |
| **9.19** | Evaluation criteria for RTS techniques include | **(d)** | All of the above | Book pp. 475, 490, 499; Slide 68 |
| **9.20** | Legacy software systems are | **(a)** | Old systems | Book pp. 479, 490, 499; Slide 69 |
| **9.21** | Reverse engineering tools include | **(d)** | All of the above | Book pp. 478, 490, 499; Slide 69 |
| **9.22** | Restructuring is NOT performed on | **(c)** | SRS | Book pp. 483, 490, 499; Slide 69 |
| **9.23** | Configuration management does NOT include | **(d)** | System administration | Book pp. 484, 490, 499; Slide 69 |
| **9.24** | BPR stands for | **(b)** | Business process re-engineering | Book pp. 481, 490, 499; Slide 69 |
| **9.25** | The process of software development from requirements is | **(b)** | Forward engineering | Book pp. 480, 490, 499; Slide 69 |

---

## 4. Quantitative Models & Formula Register

All equations are verified against textbook image scans and companion slides:

| Model / Metric | Verified Mathematical Formula | Variables & Units | Verified Invariants / Warnings | Pack Locator |
|:---|:---|:---|:---|:---:|
| **Belady-Lehman Maintenance Effort** | $$M = P + K \cdot e^{c - d}$$ | $P$: base dev effort (PM)<br>$c$: complexity index<br>$d$: familiarity index<br>$K$: constant | $c > d$ drives positive exponential cost penalty. Sensitivity analysis proves documentation saves hundreds of PM ($2.23\times$ overhead increase). | `T7_Calculations` (Q9.C1, Q9.C2) |
| **Boehm Annual Change Traffic (ACT)** | $$ACT = \frac{\text{KLOC}_{\text{added}} + \text{KLOC}_{\text{modified}}}{\text{KLOC}_{\text{total}}}$$ | Dimensionless fraction / percentage of code modified per year | Excludes simple deletions from maintenance payload. | `T2_Descriptive` (Q9.D13), `T7` |
| **Boehm Annual Maintenance Effort (AME)** | $$AME = ACT \times SDE \times EAF$$ | $AME$: effort (PM/yr)<br>$SDE$: dev effort (PM)<br>$EAF$: composite multiplier | Companion Slide 28 contains typo $10 \times 90 = 90\text{ PM}$. Textbook p. 472 proves $10 \times 90 = 900\text{ PM}$. $AEXP=0.82$ is classified as Very High. | `T7_Calculations` (Q9.C3, Q9.C4) |
| **10-Year Life-Cycle Cost Model** | $$C_{\text{total}} = C_{\text{dev}} + (L \times ACT \times C_{\text{dev}})$$ | Currency units (e.g., lacs)<br>$L$: years of operational life | Long-term maintenance accounts for $60\% - 80\%$ of total life-cycle budget ($71.43\%$ in Ex 9.19). | `T7_Calculations` (Q9.C5) |

---

## 5. Vector Asset & Diagram Register

All 11 diagrams were tightly cropped at 300 DPI, excluding slide margins and extraneous text:

| Asset ID | Filename | Source Locator | Subject / Flow Represented | Pack Locator |
|:---:|:---|:---:|:---|:---:|
| **FIG 9.2** | `CH09_FIG02_Maintenance_Process.png` | Slide 10 / Book p. 464 | 4 phases, quality attributes, Pass testing? feedback loop | `T4_Diagrams` (Q9.F1) |
| **FIG 9.3** | `CH09_FIG03_Quick_Fix_Model.png` | Slide 13 / Book p. 467 | Code patching without document synchronization | `T2_Descriptive` (Q9.D8) |
| **FIG 9.4** | `CH09_FIG04_Iterative_Enhancement.png` | Slide 15 / Book p. 467 | Analysis $\to$ Redesign $\to$ Implementation cycle | `T2_Descriptive` (Q9.D9) |
| **FIG 9.5** | `CH09_FIG05_Reuse_Model.png` | Slide 17 / Book p. 468 | Component identification, analysis, modification, integration | `T2_Descriptive` (Q9.D10) |
| **FIG 9.6** | `CH09_FIG06_Boehms_Model_complete.png` | Slide 19 / Book p. 468 | Boehm's decision-driven maintenance workflow | `T4_Diagrams` (Q9.F2) |
| **FIG 9.7** | `CH09_FIG07_Taute_Model.png` | Slide 20 / Book p. 469 | 8-phase sequential governance maintenance lifecycle | `T4_Diagrams` (Q9.F3) |
| **FIG 9.10** | `CH09_FIG10_Domain_Mapping_complete.png` | Slide 42 / Book p. 477 | Application vs domain mapping in reverse engineering | `T4_Diagrams` (Q9.F5) |
| **FIG 9.11** | `CH09_FIG11_Reverse_Eng_Levels.png` | Slide 45 / Book p. 477 | Abstraction levels: Implementation $\to$ Design $\to$ Spec | `T4_Diagrams` (Q9.F5) |
| **FIG 9.12** | `CH09_FIG12_New_Dev_vs_Reeng.png` | Slide 48 / Book p. 481 | New Development vs Re-engineering lifecycles | `T3_Compare_Analyze` (Q9.A10) |
| **FIG 9.13** | `CH09_FIG13_Program_Restructuring.png` | Slide 52 / Book p. 483 | Source restructuring into structured representations | `T2_Descriptive` (Q9.D17) |
| **FIG 9.14** | `CH09_FIG14_Change_Request_Form.png` | Slide 58 / Book p. 485 | 18-field SCM Change Request Form governed by CCA | `T4_Diagrams` (Q9.F4) |

---

## 6. Verification & Governance Audit Trail

- **Authoring lead:** Gemini Lead Integrator. **Remediation coordinator:** Codex, with three scoped Codex audit/fix agents.
- **Canonical Session Journal:** `00_STUDIO_HUB/sessions/2026-10-23.md`.
- **Delivery Gate Status:** Passed `note_linter.py --fix --strict` across all 6 study packs with 0 errors.
- **Authority Boundary:** Answers draw on the scanned course textbook and companion slides; cited source locators are retained. Chapter 9 vocabulary coverage remains provisional until the instructor’s actual list/notes arrive. Chapter 8 remains open independently.
