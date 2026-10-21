---
title: "Chapter 6 — Software Metrics: Master Index & Verification Matrix"
subtitle: "Canonical Deliverables Ledger, Question Inventory, Equation Register & Audit Matrix"
course: "Advanced Software Engineering (CS603)"
instructor: "Asst. Prof. Dr. Ali Fahim Ni'ma"
author: "Master Studio Engine"
date: "2026-10-20"
lang: "en"
---

# Chapter 6: Software Metrics — Master Index & Verification Matrix

> **Master Chapter Governance Index:** Canonical ledger for Chapter 6: Software Metrics. It maps 20 official course-slide MCQs, 28 textbook exercises, 12 curriculum vocabulary axes, 15 calculation problems, diagrams, and equations under `ASE_QUESTION_PACK_PROTOCOL.md` and student decisions N-034 through N-036. The packs have passed the current bounded source/content review, strict Markdown lint, PDF export, text/page checks, and visual layout inspection. **Ready for the student's final visual review.** Known source gaps and ambiguities remain explicitly documented; they are not presented as verified coverage.

---

## 1. Chapter Deliverables & Master Verification Matrix

| Deliverable Artifact | Source Markdown | Items Covered | Delivery Status |
|:---|:---|:---|:---:|
| **T1 — Multiple-Choice (MCQ)** | [`T1_MCQ.md`](T1_MCQ.md) | 35 MCQs (20 official course-slide questions + 15 authored practice questions) · PDF 17 pp. | **Markdown + PDF gates passed; visual review pending** |
| **T2 — Descriptive & Explain** | [`T2_Descriptive.md`](T2_Descriptive.md) | 19 questions · PDF 18 pp. | **Markdown + PDF gates passed; visual review pending** |
| **T3 — Compare & Analyze** | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | 10 comparative evaluations · PDF 10 pp. | **Markdown + PDF gates passed; visual review pending** |
| **T4 — Structural Diagrams & Traces** | [`T4_Diagrams.md`](T4_Diagrams.md) | 7 diagram/trace questions with 6 rendered PNG assets · PDF 10 pp. | **Markdown + PDF gates passed; visual review pending** |
| **T5 — Applied Scenarios & Diagnostics** | [`T5_Apply_Scenarios.md`](T5_Apply_Scenarios.md) | 7 applied scenarios · PDF 6 pp. | **Markdown + PDF gates passed; visual review pending** |
| **T7 — Numerical Calculations & Solutions** | [`T7_Calculations.md`](T7_Calculations.md) | 15 worked problems · PDF 12 pp. | **Markdown + PDF gates passed; visual review pending** |
| **V6 — Vocabulary Coverage Ledger** | [`V6_Vocabulary_Coverage.md`](V6_Vocabulary_Coverage.md) | 12 curriculum axes and 48 leaves; source gaps and partial coverage are marked · PDF 15 pp. | **Markdown + PDF gates passed; visual review pending** |
| **TOTAL CHAPTER OUTPUT** | **6 question packs + 1 vocabulary-coverage file** | **93 pack entries before cross-pack deduplication · 88 PDF pages** | **Bounded audit complete; student visual review remains** |

> [!NOTE]
> **Review boundary:** The 88 exported pages have passed strict Markdown lint, text extraction/page cohesion checks, sparse-page checks, and visual layout inspection. This prepares the packet for student review; it does not replace the student's own visual approval or close the documented source gaps.

---

## 2. Complete Course Question Inventory & Dispositions Ledger

### A. Official Course-Slide MCQs (20 Items, Slides 96–100)

| MCQ | Topic & Focus | Pack Location | Verified Key | Source Disposition & Defect Status |
|:---:|:---|:---|:---|:---|
| **6.1** | Metric Categories | [`T1_MCQ.md#Q6.1`](T1_MCQ.md) | **(d) People metrics** | Verified: Book scan p. 254; Slides 9–10, 96. |
| **6.2** | Software Science Attribution | [`T1_MCQ.md#Q6.2`](T1_MCQ.md) | **(a) M.Halstead** | Verified: Book scan p. 255; Slide 11, 96. |
| **6.3** | Vocabulary Formula | [`T1_MCQ.md#Q6.3`](T1_MCQ.md) | **(a) $\eta = \eta_1 + \eta_2$** | Verified: Book scan p. 304; Slide 12, 96. |
| **6.4** | Unit of Volume ($V$) | [`T1_MCQ.md#Q6.4`](T1_MCQ.md) | **(b) Actual size under uniform binary encoding** | Verified: Book scan p. 257; Slide 14, 96. |
| **6.5** | Unit of Effort ($E$) | [`T1_MCQ.md#Q6.5`](T1_MCQ.md) | **(c) Elementary Mental Discriminations** | Verified: Book scan p. 259; Slide 19, 97. |
| **6.6** | Language Level Relationship | [`T1_MCQ.md#Q6.6`](T1_MCQ.md) | **(d) $\lambda = L \times V^* = L^2 V$** | Verified: Book scan p. 260; Slide 23, 97. |
| **6.7** | Program Weakness | [`T1_MCQ.md#Q6.7`](T1_MCQ.md) | **(d) None of the above** (literal stem); (a) is the likely intended key if “Module” was meant | **Source defect:** Stem asks $WP$, options offer $WM$, and slide duplicates a label. |
| **6.8** | Fan-In Definition | [`T1_MCQ.md#Q6.8`](T1_MCQ.md) | **(a) Count of components calling module** | Verified: Book scan p. 282; Slide 69, 97. |
| **6.9** | Fan-Out Definition | [`T1_MCQ.md#Q6.9`](T1_MCQ.md) | **(c) Components called by module** | Verified: Book scan p. 282; Slide 69, 98. |
| **6.10** | Non-Size Metric | [`T1_MCQ.md#Q6.10`](T1_MCQ.md) | **(d) Cyclomatic complexity** | Verified: Book scan pp. 250, 422; Slide 5, 98. |
| **6.11** | Non-Software Science Metric | [`T1_MCQ.md#Q6.11`](T1_MCQ.md) | **(d) Logic** | Verified: Book scan pp. 255–262; Slide 98. |
| **6.12** | Stroud Number Meaning | [`T1_MCQ.md#Q6.12`](T1_MCQ.md) | **(a) 5 to 20** | Verified: Book scan p. 260; Slide 20, 98. |
| **6.13** | Minimal Volume Implementation | [`T1_MCQ.md#Q6.13`](T1_MCQ.md) | **(b) Potential volume** | Verified: Book scan p. 257; Slide 15, 99. |
| **6.14** | Program Volume Equation | [`T1_MCQ.md#Q6.14`](T1_MCQ.md) | **(a) $V = N \log_2 \eta$** | Verified: Book scan p. 257; Slide 14, 99. |
| **6.15** | “International standard” for size | [`T1_MCQ.md#Q6.15`](T1_MCQ.md) | **No unique key verified**; (b) may be intended | **Ambiguous source item:** wording/options do not establish what “international standard” means; no publisher key found. |
| **6.16** | Non-OO Metric Member | [`T1_MCQ.md#Q6.16`](T1_MCQ.md) | **(d) OBC** | Verified: Book scan pp. 288–293; Slide 99. |
| **6.17** | Direct and Indirect Method Cohesion | [`T1_MCQ.md#Q6.17`](T1_MCQ.md) | **(b) Loose Class Cohesion (LCC)** | Verified: Book scan pp. 292–293; Slide 85, 100. |
| **6.18** | DIT Definition | [`T1_MCQ.md#Q6.18`](T1_MCQ.md) | **(a) Number of ancestors classes** | Verified: Book scan p. 289; Slide 81, 100. |
| **6.19** | Dynamic Web Page | [`T1_MCQ.md#Q6.19`](T1_MCQ.md) | **(b) Content dependent on user actions** | Verified: Companion Slide 91, 100. |
| **6.20** | Non-Size Software Attribute | [`T1_MCQ.md#Q6.20`](T1_MCQ.md) | **(c) Cyclomatic Complexity** | Verified: Companion Slide 98, 100. |

---

### B. Textbook Exercises (28 Items, Slides 101–106)

| Exercise | Core Topic & Task | Pack Destination | Primary Question ID |
|:---:|:---|:---|:---|
| **6.1** | Define metrics; justify why measurement is needed | `T2_Descriptive` | `Q6.D01` |
| **6.2** | Explain application areas and implementation problems | `T2_Descriptive` | `Q6.D02` |
| **6.3** | Describe metric categories with examples | `T2_Descriptive` | `Q6.D03` |
| **6.4** | Software Science relevance to CBD; evaluation | `T2_Descriptive`, `T3_Compare_Analyze` | `Q6.D10`, `Q6.C02` |
| **6.5** | Explain language level's role in software science | `T2_Descriptive`, `T7_Calculations` | `Q6.D08`, `Problem 7.3` |
| **6.6** | List named Halstead measures and formulas | `T2_Descriptive`, `T7_Calculations` | `Q6.D08`, `Problem 7.1` |
| **6.7** | Calculate metrics from given vocabulary ($\eta_1=20, \eta_2=40$) | `T7_Calculations` | `Problem 7.2` |
| **6.8** | Design source-code analysis tool for Halstead metrics | `T2_Descriptive`, `T5_Apply_Scenarios` | `Q6.D09`, `Q6.S06` |
| **6.9** | Compare C and Pascal under Software Science metrics | `T3_Compare_Analyze` | `Q6.C04` |
| **6.10** | Apply token-counting rules to C identifier procedures | `T2_Descriptive` | `Q6.D09` |
| **6.11** | Recalculate Payroll System Function Points after scope expansion | `T7_Calculations` | `Problem 7.10` |
| **6.12** | Define data-structure metrics and amount-of-data counting | `T2_Descriptive` | `Q6.D11` |
| **6.13** | Explain Module Weakness and Program Weakness aggregation | `T2_Descriptive`, `T7_Calculations` | `Q6.D11`, `Problem 7.5` |
| **6.14** | Construct Variable Cross-Reference list from code | `T4_Diagrams` | `Q6.DGM03` |
| **6.15** | Trace relationship between Span and Live Variables | `T4_Diagrams`, `T7_Calculations` | `Q6.DGM04`, `Problem 7.4` (authored trace) |
| **6.16** | Explain relevance of data-structure metrics to testing | `T2_Descriptive` | `Q6.D11` |
| **6.17** | Explain Information Flow model and Fan-in/Fan-out | `T2_Descriptive`, `T4_Diagrams` | `Q6.D12`, `Q6.DGM05` |
| **6.18** | Discuss metric data problems, regression and outliers | `T5_Apply_Scenarios` | `Q6.S07` |
| **6.19** | Explain process improvement and productivity impacts | `T2_Descriptive`, `T7_Calculations` | `Q6.D01`, `Problem 7.15` |
| **6.20** | Explain limitations of LOC regarding nesting and control logic | `T2_Descriptive`, `T3_Compare_Analyze` | `Q6.D07`, `Q6.C01` |
| **6.21** | Evaluate whether data metrics relate to complexity or quality | `T3_Compare_Analyze` | `Q6.C09` |
| **6.22** | Compare reusing library components vs developing new code | `T3_Compare_Analyze` | `Q6.C08` |
| **6.23** | Compare Halstead and FP for project cost prediction | `T3_Compare_Analyze` | `Q6.C03` |
| **6.24** | Analyze operational impact of diverging size estimates | `T5_Apply_Scenarios` | `Q6.S01` |
| **6.25** | Select suitable sizing and estimation techniques | `T5_Apply_Scenarios` | `Q6.S02` |
| **6.26** | Describe OO metrics role in managing system complexity | `T2_Descriptive`, `T3_Compare_Analyze` | `Q6.D15`, `Q6.C05` |
| **6.27** | Define RFC, CBO, DAC, TCC, LCC, and DIT | `T2_Descriptive`, `T3_Compare_Analyze` | `Q6.D15`, `Q6.C06`, `Q6.C07` |
| **6.28** | Explain purpose and importance of Use-Case oriented metrics | `T2_Descriptive`, `T7_Calculations` | `Q6.D17`, `Problem 7.13` |

---

## 3. Master Equation Register

| Metric Name | Governing Formula | Symbol Definitions | Source Anchor | Verification & Domain Scope |
|:---|:---|:---|:---|:---|
| **Halstead Vocabulary** | $\eta = \eta_1 + \eta_2$ | $\eta_1$: unique operators; $\eta_2$: unique operands | Aggarwal p. 256; Slide 12 | Exact integer sum ($\eta \ge 2$) |
| **Halstead Total Length** | $N = N_1 + N_2$ | $N_1$: total operators; $N_2$: total operands | Aggarwal p. 256; Slide 13 | Exact integer count ($N \ge \eta$) |
| **Length Estimator** | $\hat{N} = \eta_1 \log_2 \eta_1 + \eta_2 \log_2 \eta_2$ | Theoretical length from vocabulary | Aggarwal p. 256; Slide 13 | Token distribution approximation |
| **Program Volume** | $V = N \log_2 \eta$ | Information storage size in bits | Aggarwal p. 257; Slide 14 | Physical unit: bits |
| **Potential Volume** | $V^* = (2 + \eta_2^*) \log_2 (2 + \eta_2^*)$ | Minimal ideal algorithm implementation | Aggarwal p. 257; Slide 15 | Physical unit: bits |
| **Program Level** | $L = V^* / V \approx \frac{2}{\eta_1} \times \frac{\eta_2}{N_2}$ | Implementation conciseness ratio | Aggarwal p. 258; Slide 17 | Dimensionless ($0 < L \le 1$) |
| **Program Difficulty** | $D = 1 / L \approx \frac{\eta_1}{2} \times \frac{N_2}{\eta_2}$ | Mental comprehension resistance | Aggarwal p. 259; Slide 18 | Dimensionless ($D \ge 1$) |
| **Halstead Effort** | $E = D \times V = V / L$ | Mental discriminations required | Aggarwal p. 259; Slide 19 | Elementary mental discriminations |
| **Development Time** | $T = E / 18 \text{ seconds}$ | Stroud neurological conversion | Aggarwal p. 260; Slide 20 | Time in seconds ($S = 18 \text{ s}^{-1}$) |
| **Language Level** | $\lambda = L \times V^* = L^2 V$ | Invariant language expressive power | Aggarwal p. 260; Slide 23 | Dimensionless |
| **Average Live Variables** | $\overline{LV} = \frac{1}{n} \sum LV(S_i)$ | Mean active variables across $n$ statements | Aggarwal p. 277; Slide 53 | Real number |
| **Average Variable Life** | $\gamma = \frac{1}{\text{total vars}} \sum LV(S_i)$ | Average lifespan of variables across statements | Aggarwal p. 278; Slide 68 | Real number |
| **Variable Span** | $SP = b - a - 1$ | Intervening statements between references | Aggarwal p. 277; Slide 54 | Non-negative integer |
| **Module Weakness** | $WM = \overline{LV} \times \gamma$ | Modular data vulnerability index | Aggarwal pp. 278–280; Slide 68 | Real number |
| **Program Weakness** | $WP = \frac{1}{m} \sum WM_i$ | Arithmetic mean of module weaknesses | Aggarwal p. 280; Slide 64 | System-wide mean |
| **Henry–Kafura Metric** | $HKM = \text{LOC} \times [fin + fout]^2$ | Information flow structural complexity | Pressman 5e §19.4.2, p. 524 | Quadratic communication growth |
| **McCabe Complexity** | $V(G) = E - N + 2P = P_{pred} + 1 = R$ | Linearly independent path basis | Aggarwal p. 422; Slide 132 | Integer ($V(G) \ge 1$) |
| **Albrecht Function Points** | $FP = UFP \times (0.65 + 0.01 \sum F_i)$ | Functional size normalized by 14 GSCs | Aggarwal p. 145; Ch.4 | $VAF \in [0.65, 1.35]$ |
| **Unadjusted Use Case Points** | $UUCP = UAW + UUCW$ | Actor and use-case weights in course material | Aggarwal pp. 295–296; slides 89–90 | Unadjusted points; TCF/ECF/effort conversion: gap in inspected local sources |
| **Defect Removal Efficiency** | $DRE = E / (E + D)$ | Pre-release internal defect filtering | Pressman 5e, p. 98; Slide 10 | Percentage ($0.0 \le DRE \le 1.0$) |

---

## 4. Documented Bounded Gaps & Verification Limits

| Topic / Item | Source Status | Explicit Limitation & Evidence Boundary | Handling in Question Packs |
|:---|:---|:---|:---|
| **MCQ 6.7 Stem Mismatch** | Defective in Source | Stem asks for Program Weakness; all options give Module Weakness ($WM$); slide duplicates option label `(a)`. | Literal key recorded as (d); option (a) identified only as the likely intended formula if the stem meant Module Weakness. |
| **MCQ 6.15 Standard Size** | Ambiguous in Source | The wording and options do not establish a unique interpretation or a publisher key. | No unique key asserted; likely intended classroom concept is separated from what the wording proves. |
| **Exercise 6.7 Data Limits** | Partial Inputs Given | Gives $\eta_1 = 20, \eta_2 = 40$ only; omits $N_1, N_2$. | Strictly solves for $\hat{N} \approx 299.32$; explicitly explains why actual $N, V, D, E$ cannot be fabricated. |
| **UCP adjustments and effort conversion** | Documented bounded gap | Supplied Aggarwal pages/slides support actor and use-case weights; the inspected approved source set did not verify TCF/ECF rules or an hours/UCP conversion. | `T2`, `T7`, and `V6` now stop at $UUCP$ and mark the extensions as gaps. |
| **Complexity Bounds & Testability** | Source-bounded | $V(G)$ gives the size of an independent basis-path set; no universal defect cutoff or mandatory CI threshold is established here. | Corrected in `T2_Descriptive` and `T5_Apply_Scenarios`; team thresholds are labelled as local policy. |
| **Mark II Function Points** | Documented Bounded Gap | Leach p. 39 hit is a historical anecdote regarding the Mark II computer, not Symons' Mark II FP. | Documented as bounded gap in `V6_Vocabulary_Coverage`; not fabricated. |
| **IF4 & Shepperd Refinements** | Documented Bounded Gap | Detailed variant formulas not validated in current local textbook scans. | Recorded as bounded gap; Henry–Kafura verified via Pressman §19.4.2. |
| **Essential / Design Complexity; Knot Count / Nesting Depth** | Documented bounded gaps | Definitions and calculation rules were not verified in the approved local sources inspected for this pack. | Explicitly marked as gaps in `T2_Descriptive` and `V6_Vocabulary_Coverage`; no unsupported definitions or numeric cutoffs retained. |

---

## Retrieval Set & Active Recall Self-Test

Use this master index for active recall:
- For each of the 20 official MCQs, identify its location and distinguish verified keys from source ambiguities or defects recorded in `T1_MCQ.md`.
- Explain why Exercise 6.7's solution in `T7_Calculations` refrains from calculating actual effort $E$.
- Trace the source anchor for Henry–Kafura's formula to Pressman 5e §19.4.2 printed page 524.
- Recite the mathematical formula for Albrecht's Value Adjustment Factor ($VAF$) and its minimum and maximum values.
