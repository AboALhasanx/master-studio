# -*- coding: utf-8 -*-
"""
Build script for ASE Chapter 8: 00_INDEX.md Master Index & Verification Matrix
"""
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

OUT_PATH = r"01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch08_Software_Testing\00_INDEX.md"

header = """---
title: "Chapter 8 — Software Testing: Master Index & Verification Matrix"
subtitle: "Canonical Deliverables Ledger, Question Inventory, Equation Register & Audit Matrix"
course: "Advanced Software Engineering (CS603)"
instructor: "Asst. Prof. Dr. Ali Fahim Ni'ma"
author: "Master Studio Engine"
date: "2026-10-22"
lang: "en"
---

# Chapter 8: Software Testing — Master Index & Verification Matrix

> **Master Chapter Governance Index:** Canonical ledger for Chapter 8: Software Testing. It maps 50 official course-slide MCQs, 50 textbook exercises, 35 predictive vocabulary leaves, diagrams, and computational models under `ASE_QUESTION_PACK_PROTOCOL.md` and student governance decisions. The packs have passed bounded source/content review, strict Markdown lint, PDF export, text/page checks, and visual layout inspection. **Ready for the student's final visual review.**

---

## 1. Chapter Deliverables & Master Verification Matrix

| Deliverable Artifact | Source Markdown | Items Covered | PDF Extent | Delivery Status |
|:---|:---|:---|:---:|:---:|
| **T1 — Multiple-Choice (MCQ)** | [`T1_MCQ.md`](T1_MCQ.md) | 50 official course MCQs (8.1–8.50) with verified publisher keys | 25 pages (2 items/page) | **Pristine (Gate PASSED)** |
| **T2 — Descriptive & Short-Answer** | [`T2_Descriptive.md`](T2_Descriptive.md) | 23 official descriptive exercises | 23 pages (1 item/page) | **Pristine (Gate PASSED)** |
| **T3 — Compare & Analyze** | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | 11 analytical & comparative exercises | 12 pages | **Pristine (Gate PASSED)** |
| **T4 — Structural Models & Visual Diagrams** | [`T4_Diagrams.md`](T4_Diagrams.md) | 4 diagram/structural exercises with 9 vector/high-res assets | 12 pages | **Pristine (Gate PASSED)** |
| **T5 — Applied Test Design & Case Studies** | [`T5_Apply_Design.md`](T5_Apply_Design.md) | 11 applied engineering & test-design exercises | 16 pages | **Pristine (Gate PASSED)** |
| **T7 — Computational Models & Derivations** | [`T7_Calculations.md`](T7_Calculations.md) | Exercise 8.32 + 4 core computational modules | 11 pages | **Pristine (Gate PASSED)** |
| **V8 — Predictive Vocabulary Coverage** | [`V8_Coverage.md`](V8_Coverage.md) | 35 predictive leaves mapped across all packs | Reference Ledger | **Complete (Predictive)** |
| **TOTAL CHAPTER OUTPUT** | **6 question packs + [Ch08_Complete_Print_Pack.pdf](Ch08_Complete_Print_Pack.pdf)** | **100 source items (50 MCQs + 50 Exercises) · 99 PDF pages** | **Ready for Student Review** |

---

## 2. Complete Question Inventory & Dispositions Ledger

### A. Official Course-Slide MCQs (50 Items, Slides 189–200 & Book pp. 451–455)
All 50 MCQs verified against the official publisher answer key on printed p. 499 (PDF spread 255 right) of `AliFahim_Software_Engineering.pdf`:

| MCQ | Topic & Focus | Pack Location | Verified Key | Source Disposition |
|:---:|:---|:---|:---:|:---|
| **8.1** | Software testing purpose | [`T1_MCQ.md#Question 8.1`](T1_MCQ.md) | **(d)** | Myers' definition: executing with intent of finding errors. |
| **8.2** | Coding mistake terminology | [`T1_MCQ.md#Question 8.2`](T1_MCQ.md) | **(c)** | Mistake in coding is a bug/fault. |
| **8.3** | Functional testing type | [`T1_MCQ.md#Question 8.3`](T1_MCQ.md) | **(b)** | Functional testing is Black-box testing. |
| **8.4** | BVA count for n variables | [`T1_MCQ.md#Question 8.4`](T1_MCQ.md) | **(b)** | Single fault assumption: $4n + 1$. |
| **8.5** | Robustness count for 2 variables | [`T1_MCQ.md#Question 8.5`](T1_MCQ.md) | **(b)** | Formula $6n + 1 = 6(2) + 1 = 13$. |
| **8.6** | Robustness count for n variables | [`T1_MCQ.md#Question 8.6`](T1_MCQ.md) | **(c)** | General formula: $6n + 1$. |
| **8.7** | Regression testing focus | [`T1_MCQ.md#Question 8.7`](T1_MCQ.md) | **(d)** | Retesting software after modifications. |
| **8.8** | Flow-graph source node | [`T1_MCQ.md#Question 8.8`](T1_MCQ.md) | **(a)** | In-degree 0, out-degree > 0. |
| **8.9** | Flow-graph destination node | [`T1_MCQ.md#Question 8.9`](T1_MCQ.md) | **(c)** | In-degree > 0, out-degree 0. |
| **8.10** | Decision-table quadrants | [`T1_MCQ.md#Question 8.10`](T1_MCQ.md) | **(a)** | Four quadrants (Condition/Action Stubs & Entries). |
| **8.11** | Beta-test participants | [`T1_MCQ.md#Question 8.11`](T1_MCQ.md) | **(a)** | Potential customers at customer sites. |
| **8.12** | Equivalence-class testing family | [`T1_MCQ.md#Question 8.12`](T1_MCQ.md) | **(b)** | Blackbox testing (verified against printed p. 499 key). |
| **8.13** | Cause-effect graphing family | [`T1_MCQ.md#Question 8.13`](T1_MCQ.md) | **(c)** | Functional / black-box technique. |
| **8.14** | Validation target / actor | [`T1_MCQ.md#Question 8.14`](T1_MCQ.md) | **(d)** | The customer checks the product (verified against printed p. 499 key). |
| **8.15** | Verification definition | [`T1_MCQ.md#Question 8.15`](T1_MCQ.md) | **(b)** | Building the product right (against specification). |
| **8.16** | Validation definition | [`T1_MCQ.md#Question 8.16`](T1_MCQ.md) | **(a)** | Building the right product (fulfilling user needs). |
| **8.17** | Alpha-test participants | [`T1_MCQ.md#Question 8.17`](T1_MCQ.md) | **(a)** | Customer (verified against printed p. 499 key). |
| **8.18** | Alpha-test site | [`T1_MCQ.md#Question 8.18`](T1_MCQ.md) | **(a)** | Developer's site under controlled conditions. |
| **8.19** | Beta-test site | [`T1_MCQ.md#Question 8.19`](T1_MCQ.md) | **(b)** | User's / customer's site. |
| **8.20** | Acceptance-test participant | [`T1_MCQ.md#Question 8.20`](T1_MCQ.md) | **(b)** | End users / customers. |
| **8.21** | Fault-to-failure relationship | [`T1_MCQ.md#Question 8.21`](T1_MCQ.md) | **(d)** | Fault may produce zero, one, or several failures. |
| **8.22** | Test-suite definition | [`T1_MCQ.md#Question 8.22`](T1_MCQ.md) | **(a)** | Set of test cases. |
| **8.23** | Behavioral specifications | [`T1_MCQ.md#Question 8.23`](T1_MCQ.md) | **(b)** | Verification (verified against printed p. 499 key). |
| **8.24** | Development testing approach | [`T1_MCQ.md#Question 8.24`](T1_MCQ.md) | **(d)** | Acceptance testing (verified against printed p. 499 key). |
| **8.25** | Functional vs regression technique | [`T1_MCQ.md#Question 8.25`](T1_MCQ.md) | **(c)** | Equivalence class testing is functional. |
| **8.26** | Decision-table application | [`T1_MCQ.md#Question 8.26`](T1_MCQ.md) | **(b)** | Complex boolean condition combinations. |
| **8.27** | Limits of BVA and equivalence | [`T1_MCQ.md#Question 8.27`](T1_MCQ.md) | **(b)** | Do not evaluate combinations of input conditions. |
| **8.28** | Cause/effect relationship | [`T1_MCQ.md#Question 8.28`](T1_MCQ.md) | **(a)** | Causes represent inputs; effects represent outputs. |
| **8.29** | DD-path expansion | [`T1_MCQ.md#Question 8.29`](T1_MCQ.md) | **(d)** | Decision to decision Path graph (verified against printed p. 499 key). |
| **8.30** | Independent-path definition | [`T1_MCQ.md#Question 8.30`](T1_MCQ.md) | **(a)** | Path introducing at least one new edge. |
| **8.31** | Cyclomatic-complexity origin | [`T1_MCQ.md#Question 8.31`](T1_MCQ.md) | **(b)** | Thomas J. McCabe (1976). |
| **8.32** | Cyclomatic-complexity formulas | [`T1_MCQ.md#Question 8.32`](T1_MCQ.md) | **(d)** | All of the above ($e-n+2P$, $P+1$, regions). |
| **8.33** | Predicate node assumption | [`T1_MCQ.md#Question 8.33`](T1_MCQ.md) | **(a)** | Binary predicates (out-degree 2). |
| **8.34** | Graph-matrix dimensions | [`T1_MCQ.md#Question 8.34`](T1_MCQ.md) | **(b)** | Square matrix of dimension $N \\times N$. |
| **8.35** | Node representation in matrix | [`T1_MCQ.md#Question 8.35`](T1_MCQ.md) | **(a)** | Rows = source nodes, Columns = target nodes. |
| **8.36** | Cyclomatic complexity & paths | [`T1_MCQ.md#Question 8.36`](T1_MCQ.md) | **(a)** | Equals the number of independent basis paths. |
| **8.37** | Data-flow testing nature | [`T1_MCQ.md#Question 8.37`](T1_MCQ.md) | **(d)** | White-box data lifecycle testing (not DFDs). |
| **8.38** | du vs dc path objective | [`T1_MCQ.md#Question 8.38`](T1_MCQ.md) | **(c)** | Focus on du-paths that are NOT dc-paths. |
| **8.39** | Mutation testing classification | [`T1_MCQ.md#Question 8.39`](T1_MCQ.md) | **(a)** | Fault-based structural testing. |
| **8.40** | Unit-test scaffolding | [`T1_MCQ.md#Question 8.40`](T1_MCQ.md) | **(c)** | Drivers and stubs. |
| **8.41** | Debugging vs regression | [`T1_MCQ.md#Question 8.41`](T1_MCQ.md) | **(d)** | Debugging isolates/repairs faults; testing reveals them. |
| **8.42** | Failure terminology | [`T1_MCQ.md#Question 8.42`](T1_MCQ.md) | **(b)** | Departure of operational behavior from requirements. |
| **8.43** | Alpha/beta testing relation | [`T1_MCQ.md#Question 8.43`](T1_MCQ.md) | **(c)** | Subsets / phases of Acceptance Testing. |
| **8.44** | Verification activity | [`T1_MCQ.md#Question 8.44`](T1_MCQ.md) | **(d)** | Reviews, inspections, walkthroughs, unit tests. |
| **8.45** | Testing as V&V | [`T1_MCQ.md#Question 8.45`](T1_MCQ.md) | **(c)** | Encompasses both verification and validation. |
| **8.46** | Integration-testing approaches | [`T1_MCQ.md#Question 8.46`](T1_MCQ.md) | **(d)** | Top-down, bottom-up, sandwich, big bang. |
| **8.47** | Visible functionality testing | [`T1_MCQ.md#Question 8.47`](T1_MCQ.md) | **(b)** | Black-box / functional testing. |
| **8.48** | Top-down stubs requirement | [`T1_MCQ.md#Question 8.48`](T1_MCQ.md) | **(b)** | Requires stubs to simulate lower-level modules. |
| **8.49** | Thread testing nature | [`T1_MCQ.md#Question 8.49`](T1_MCQ.md) | **(d)** | Integration testing of functional threads / use cases. |
| **8.50** | Actual data / beta testing | [`T1_MCQ.md#Question 8.50`](T1_MCQ.md) | **(b)** | Beta testing in actual operational environment. |

---

### B. Official Textbook Exercises (50 Items, Slides 201–212 & Book pp. 455–458)
All 50 exercises are mapped and solved in the question packs:

| Exercise | Core Topic & Task | Pack Destination | Primary Question ID |
|:---:|:---|:---|:---|
| **8.1** | Testing definition, life-cycle role & difficulty | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.1`](T2_Descriptive.md) |
| **8.2** | Why test and who should test | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.2`](T2_Descriptive.md) |
| **8.3** | What should we test & testing importance | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.3`](T2_Descriptive.md) |
| **8.4** | Define fault, failure, bug, mistake | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.4`](T2_Descriptive.md) |
| **8.5** | Compare Alpha/Beta, Dev/Regression, Functional/Structural | `T3_Compare_Analyze` | [`T3_Compare_Analyze.md#Question 8.5`](T3_Compare_Analyze.md) |
| **8.6** | Limitations of testing & impossible complete testing | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.6`](T2_Descriptive.md) |
| **8.7** | Test case/suite, V&V, Alpha/Beta/Acceptance | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.7`](T2_Descriptive.md) |
| **8.8** | Does exhaustive testing guarantee 100% correctness? | `T3_Compare_Analyze` | [`T3_Compare_Analyze.md#Question 8.8`](T3_Compare_Analyze.md) |
| **8.9** | Why software fails after acceptance testing | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.9`](T2_Descriptive.md) |
| **8.10** | Kinds of functional testing & detail of one | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.10`](T2_Descriptive.md) |
| **8.11** | Failure necessary & sufficient conditions | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.11`](T2_Descriptive.md) |
| **8.12** | Boundary value analysis technique with example | `T5_Apply_Design` | [`T5_Apply_Design.md#Question 8.12`](T5_Apply_Design.md) |
| **8.13** | NextDate calendar problem (BVA, Robust, Worst-Case) | `T5_Apply_Design` | [`T5_Apply_Design.md#Question 8.13`](T5_Apply_Design.md) |
| **8.14** | Worst-case vs ad hoc performance evaluation | `T3_Compare_Analyze` | [`T3_Compare_Analyze.md#Question 8.14`](T3_Compare_Analyze.md) |
| **8.15** | Equivalence class testing compared with BVA | `T3_Compare_Analyze` | [`T3_Compare_Analyze.md#Question 8.15`](T3_Compare_Analyze.md) |
| **8.16** | Largest of three numbers (BVA, Coverage, Decision Table) | `T5_Apply_Design` | [`T5_Apply_Design.md#Question 8.16`](T5_Apply_Design.md) |
| **8.17** | Impracticality of exhaustive testing proof | `T5_Apply_Design` | [`T5_Apply_Design.md#Question 8.17`](T5_Apply_Design.md) |
| **8.18** | Decision table usefulness & effectiveness justification | `T3_Compare_Analyze` | [`T3_Compare_Analyze.md#Question 8.18`](T3_Compare_Analyze.md) |
| **8.19** | Cause-effect graph for largest of three numbers | `T4_Diagrams` | [`T4_Diagrams.md#Question 8.19`](T4_Diagrams.md) |
| **8.20** | Cause-effect graphing technique with full example | `T4_Diagrams` | [`T4_Diagrams.md#Question 8.20`](T4_Diagrams.md) |
| **8.21** | Extended triangle problem with right-angle cases | `T5_Apply_Design` | [`T5_Apply_Design.md#Question 8.21`](T5_Apply_Design.md) |
| **8.22** | Why software testing needs extensive planning | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.22`](T2_Descriptive.md) |
| **8.23** | Test case design objectives and steps | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.23`](T2_Descriptive.md) |
| **8.24** | Student grading equivalence class testing | `T5_Apply_Design` | [`T5_Apply_Design.md#Question 8.24`](T5_Apply_Design.md) |
| **8.25** | Odd/even integer BVA and equivalence testing | `T5_Apply_Design` | [`T5_Apply_Design.md#Question 8.25`](T5_Apply_Design.md) |
| **8.26** | Professional course admission decision table | `T5_Apply_Design` | [`T5_Apply_Design.md#Question 8.26`](T5_Apply_Design.md) |
| **8.27** | Flow graph & independent basis paths for Largest of 3 | `T4_Diagrams` | [`T4_Diagrams.md#Question 8.27`](T4_Diagrams.md) |
| **8.28** | Significance of independent paths & tools for >100 LOC | `T3_Compare_Analyze` | [`T3_Compare_Analyze.md#Question 8.28`](T3_Compare_Analyze.md) |
| **8.29** | Structural testing vs functional testing | `T3_Compare_Analyze` | [`T3_Compare_Analyze.md#Question 8.29`](T3_Compare_Analyze.md) |
| **8.30** | Structural testing techniques illustration | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.30`](T2_Descriptive.md) |
| **8.31** | Importance of path testing in structural testing | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.31`](T2_Descriptive.md) |
| **8.32** | Cyclomatic complexity definition & tri-method derivation | `T7_Calculations` | [`T7_Calculations.md#Question 8.32`](T7_Calculations.md) |
| **8.33** | Thresholds for software modules ($V(G) \\le 10$) | `T3_Compare_Analyze` | [`T3_Compare_Analyze.md#Question 8.33`](T3_Compare_Analyze.md) |
| **8.34** | Data flow testing du-paths vs dc-paths | `T4_Diagrams` | [`T4_Diagrams.md#Question 8.34`](T4_Diagrams.md) |
| **8.35** | Steps of data flow testing | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.35`](T2_Descriptive.md) |
| **8.36** | Value perturbation (100 to 1000) & test precautions | `T3_Compare_Analyze` | [`T3_Compare_Analyze.md#Question 8.36`](T3_Compare_Analyze.md) |
| **8.37** | White vs Black box; 100% path coverage critique | `T3_Compare_Analyze` | [`T3_Compare_Analyze.md#Question 8.37`](T3_Compare_Analyze.md) |
| **8.38** | Testing objectives & tester psychology | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.38`](T2_Descriptive.md) |
| **8.39** | Failure after testing & contrast with hardware wear-out | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.39`](T2_Descriptive.md) |
| **8.40** | Integration testing purpose and methodology | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.40`](T2_Descriptive.md) |
| **8.41** | Integration testing vs system testing | `T3_Compare_Analyze` | [`T3_Compare_Analyze.md#Question 8.41`](T3_Compare_Analyze.md) |
| **8.42** | Unit testing feasibility and desirability | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.42`](T2_Descriptive.md) |
| **8.43** | Independent system test team justification | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.43`](T2_Descriptive.md) |
| **8.44** | Practical fault localization & Table 8.8 debugging | `T5_Apply_Design` | [`T5_Apply_Design.md#Question 8.44`](T5_Apply_Design.md) |
| **8.45** | How design attributes facilitate debugging | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.45`](T2_Descriptive.md) |
| **8.46** | Debugging statement problems and remedies | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.46`](T2_Descriptive.md) |
| **8.47** | Debugging approaches (Inductive vs Deductive) | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.47`](T2_Descriptive.md) |
| **8.48** | Hybrid multi-tier testing strategy proposal | `T5_Apply_Design` | [`T5_Apply_Design.md#Question 8.48`](T5_Apply_Design.md) |
| **8.49** | Spell checker test set design and inadequacies | `T5_Apply_Design` | [`T5_Apply_Design.md#Question 8.49`](T5_Apply_Design.md) |
| **8.50** | 4GL impact, advantages/disadvantages & cost justification | `T2_Descriptive` | [`T2_Descriptive.md#Question 8.50`](T2_Descriptive.md) |

---

## 3. Evidence Boundaries, Source Gaps & Errata Resolved

1. **Scanned Textbook Boundary Verified:**
   - Primary textbook scan (`Reference_Textbooks/AliFahim_Software_Engineering.pdf`) verified as K.K. Aggarwal & Yogesh Singh (*Software Engineering*, 3rd ed.).
   - **Chapter 8 starts:** printed p. 365 at PDF spread 188 (right page).
   - **Chapter 8 ends:** printed p. 458 at PDF spread 235 (left page).
   - **Spread range:** Spreads 188–235 (48 PDF spreads = 94 book pages: 365–458).
   - **Chapter 9 starts:** printed p. 459 at PDF spread 235 (right page).

2. **Official Publisher MCQ Answer Key Located & Verified:**
   - Discovered on printed p. 499 (PDF spread 255 right) of `AliFahim_Software_Engineering.pdf`.
   - Confirms exact publisher answers for all 50 MCQs (8.1 to 8.50), eliminating all previous answer key ambiguities.

3. **Slide Errata and Source Discrepancies Resolved:**
   - **Figure 8.33 (Slide 185):** Slide caption mislabeled the process as \"inductive\"; the book (p. 446) and content correctly establish it as \"deductive debugging\".
   - **Exercise 8.13 (Slide 203):** OCR artifact in year range corrected to $1900 \\le \\text{year} \\le 2025$ per textbook p. 456.
   - **Exercise 8.44 (Slide 211):** Truncated label \"Table 8\" restored to \"Table 8.8\" (Myers' Debugging Principles, textbook p. 448).

4. **Predictive Vocabulary Status Preserved:**
   - All 35 vocabulary terms remain explicitly designated as **PREDICTIVE** until Dr. Ali Fahim's official Chapter 8 vocabulary list is provided by the student.

5. **Student Audit Corrections Applied & Verified:**
   - **T1 MCQ Alignment:** Aligned all 50 MCQs directly to the literal printed text of the publisher answer key on p. 499, correcting 6 mislabeled option descriptions (Q8.12, 8.14, 8.17, 8.23, 8.24, 8.29).
   - **T4 Visual Diagrams & Notation:** Added missing effect $e_5$ (\"Impossible stage\") to the Triangle Problem; aligned Causes $c_1..c_6$ and Effects $e_1..e_5$ with textbook Example 8.12 (p. 405); separated Figure 8.10 (Constraint symbols $E, I, O, R$) from Figure 8.11 (Masks constraint $M$); eliminated visual clipping in CFG (Exit node callout overlap removed, False branch label properly placed).
   - **T5 Calendar Date Logic & Cartesian Grid Integrity:** In NextDate (Exercise 8.13), corrected $(30, 6, 1962) \\to 1/7/1962$ as a valid date; strictly enforced the 125 Cartesian worst-case set as $\\{1, 2, 15, 30, 31\\} \\times \\{1, 2, 6, 11, 12\\} \\times \\{1900, 1901, 1962, 2024, 2025\\}$, documenting Feb 28/29 as Special Value / Domain testing; affirmed $(31, 12, 2025)$ as a valid input within bounds advancing to $1/1/2026$.
   - **T7 Mathematical Rigor & Grounding:** Corrected $P$ in $e - n + 2P$ as connected components (not strongly connected); replaced quadratic values with canonical textbook Example 8.15 ($n=10, e=13, \\Pi=4, V(G)=5$); added textbook restriction that $\\Pi+1$ strictly requires binary decision nodes (2 outgoing edges); corrected Mutation Testing adequacy to note a single test case can kill multiple mutants; fixed citation of Error Seeding to Chapter 7 (§7.3.5, pp. 345–347).

<!-- Print-hidden study guidance retained for screen use.
## Retrieval Set & Active Recall Self-Test

1. How many total items and PDF pages comprise the Chapter 8 print pack?
2. What are the six question packs covering Chapter 8 software testing?
3. Where is the official publisher answer key for MCQs located in the textbook?
-->
"""

def generate():
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(header.strip() + "\n")
    print(f"Generated {OUT_PATH} successfully.")

if __name__ == "__main__":
    generate()
