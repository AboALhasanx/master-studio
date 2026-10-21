# Chapter 4 — Software Project Planning (Canonical Index & Deliverables Matrix)

> **Status:** **CLOSED AFTER INDEPENDENT SOURCE, MATH, AND PDF AUDIT (2026-10-19)**  
> **Course:** Advanced Software Engineering (CS603) — Asst. Prof. Dr. Ali Fahim Ni'ma  
> **Primary Authority:** K.K. Aggarwal & Yogesh Singh, *Software Engineering* (3rd ed.), printed pp. 139–202 (spreads 75–107); Companion Slides 1–207.  
> **Published Deliverables:** Seven study-pack PDFs (110 pages total) plus the canonical index PDF (12 pages); all eight PDFs are current and passed the final integrity/layout gate.

---

## 1. Chapter Deliverables & Master Verification Matrix

Seven study packs and the canonical index are finalized; item counts, source dispositions, PDF pages, and final-gate results are summarized below:

| Deliverable Artifact | Source Markdown | Compiled PDF | Pages | Items Covered | Delivery Gate Status |
|:---|:---|:---|:---:|:---|:---:|
| **T1 — Multiple-Choice (MCQ)** | [`T1_MCQ.md`](T1_MCQ.md) | [`T1_MCQ.pdf`](T1_MCQ.pdf) | **12 pp** | 35 MCQs (25 official slide MCQs 4.1–4.25 + 10 synthesis MCQs) | **Closed** |
| **T2 — Descriptive & Explain** | [`T2_Descriptive.md`](T2_Descriptive.md) | [`T2_Descriptive.pdf`](T2_Descriptive.pdf) | **13 pp** | 16 items (10 exercises + 6 authored synthesis) | **Closed** |
| **T3 — Compare & Analyze** | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | [`T3_Compare_Analyze.pdf`](T3_Compare_Analyze.pdf) | **19 pp** | 16 items (13 exercises + 3 authored synthesis) | **Closed** |
| **T4 — Visual Models & Diagrams** | [`T4_Diagrams.md`](T4_Diagrams.md) | [`T4_Diagrams.pdf`](T4_Diagrams.pdf) | **11 pp** | 5 visual clusters | **Closed** |
| **T5 — Applied Scenarios & Tools** | [`T5_Apply_Scenarios.md`](T5_Apply_Scenarios.md) | [`T5_Apply_Scenarios.pdf`](T5_Apply_Scenarios.pdf) | **11 pp** | 8 items (4 textbook exercises + 4 authored scenarios) | **Closed** |
| **T7 — Numerical Calculations** | [`T7_Calculations.md`](T7_Calculations.md) | [`T7_Calculations.pdf`](T7_Calculations.pdf) | **28 pp** | 22 items: 10 textbook exercises, 8 authored practice problems, and 4 reproduced textbook examples | **Closed; math audited** |
| **V4 — Vocabulary Coverage** | [`V4_Vocabulary_Coverage.md`](V4_Vocabulary_Coverage.md) | [`V4_Vocabulary_Coverage.pdf`](V4_Vocabulary_Coverage.pdf) | **16 pp** | 18 instructor vocabulary terms mapped to primary sources; gaps checked selectively | **Closed** |
| **TOTAL CHAPTER OUTPUT** | **7 Markdown Packs** | **7 Academic PDFs** | **110 pp** (plus 12-page index) | Pack counts overlap; no unique-question total asserted | **Closed** |

---

## 2. Gate 1: Complete Course Question Inventory & Dispositions Ledger

The exercise and example entries were checked against the source chapter inventory and companion slides; their pack locations are cross-referenced below. Coverage disposition is explicit and is not inferred from artifact counts.

### A. Official Slide MCQs (25 items)

The 25 numbered course MCQs are preserved in source order. The answer letters below were checked against the publisher key; this index summarizes the actual stems in the pack rather than inferred topics.

| MCQ | Actual stem | Pack location | Keyed answer | Disposition |
|:---:|:---|:---|:---|:---|
| **4.1** | After the finalization of SRS, we may like to estimate: | [`T1_MCQ.md#Q41`](T1_MCQ.md) | **(d) All of the above** | **Matched to slide question and publisher key** |
| **4.2** | Which one is not a size measure for software? | [`T1_MCQ.md#Q42`](T1_MCQ.md) | **(c) Cyclomatic Complexity** | **Matched to slide question and publisher key** |
| **4.3** | Function count method was developed by: | [`T1_MCQ.md#Q43`](T1_MCQ.md) | **(d) Alan Albrecht** | **Matched to slide question and publisher key** |
| **4.4** | Function point analysis (FPA) method decomposes the system into functional units. The total number of functional units are: | [`T1_MCQ.md#Q44`](T1_MCQ.md) | **(b) 5** | **Matched to slide question and publisher key** |
| **4.5** | IFPUG stands for: | [`T1_MCQ.md#Q45`](T1_MCQ.md) | **(c) International function point user group** | **Matched to slide question and publisher key** |
| **4.6** | Function points can be calculated by: | [`T1_MCQ.md#Q46`](T1_MCQ.md) | **(a) UFP * CAF** | **Matched to slide question and publisher key** |
| **4.7** | Putnam resource allocation model is based on: | [`T1_MCQ.md#Q47`](T1_MCQ.md) | **(b) Norden/Rayleigh curve** | **Matched to slide question and publisher key** |
| **4.8** | Manpower buildup for Putnam resource allocation model is: | [`T1_MCQ.md#Q48`](T1_MCQ.md) | **(b) $D_0 = K / t_d^3$** | **Matched to slide question and publisher key** |
| **4.9** | COCOMO was developed initially by: | [`T1_MCQ.md#Q49`](T1_MCQ.md) | **(a) B. W. Boehm** | **Matched to slide question and publisher key** |
| **4.10** | A COCOMO model is: | [`T1_MCQ.md#Q410`](T1_MCQ.md) | **(b) Constructive Cost Estimation model** | **Matched to slide question and publisher key** |
| **4.11** | Estimation of software development effort for organic software in COCOMO is: | [`T1_MCQ.md#Q411`](T1_MCQ.md) | **(a) $E = 2.4(\text{KLOC})^{1.05} \text{ PM}$** | **Matched to slide question and publisher key** |
| **4.12** | Estimation of size for a project is dependent on: | [`T1_MCQ.md#Q412`](T1_MCQ.md) | **(d) None of the above** | **Matched to slide question and publisher key** |
| **4.13** | In function point analysis, number of Complexity Adjustment Factors are: | [`T1_MCQ.md#Q413`](T1_MCQ.md) | **(c) 14** | **Matched to slide question and publisher key** |
| **4.14** | COCOMO-II estimation model is based on: | [`T1_MCQ.md#Q414`](T1_MCQ.md) | **(b) Algorithmic approach** | **Matched to slide question and publisher key** |
| **4.15** | Cost estimation for a project may include: | [`T1_MCQ.md#Q415`](T1_MCQ.md) | **(d) All of the above** | **Matched to slide question and publisher key** |
| **4.16** | In COCOMO model, if project size is typically 2–50 KLOC, then which mode is to be selected? | [`T1_MCQ.md#Q416`](T1_MCQ.md) | **(a) Organic** | **Matched to slide question and publisher key** |
| **4.17** | COCOMO-II was developed at: | [`T1_MCQ.md#Q417`](T1_MCQ.md) | **(b) University of Southern California** | **Matched to slide question and publisher key** |
| **4.18** | Which one is not a Category of COCOMO-II? | [`T1_MCQ.md#Q418`](T1_MCQ.md) | **(c) Requirement Sector** | **Matched to slide question and publisher key** |
| **4.19** | Which one is not an infrastructure software? | [`T1_MCQ.md#Q419`](T1_MCQ.md) | **(d) Result management system** | **Matched to slide question and publisher key** |
| **4.20** | How many stages are in COCOMO-II? | [`T1_MCQ.md#Q420`](T1_MCQ.md) | **(b) 3** | **Matched to slide question and publisher key** |
| **4.21** | Which one is not a stage of COCOMO-II? | [`T1_MCQ.md#Q421`](T1_MCQ.md) | **(d) Comprehensive cost estimation model** | **Matched to slide question and publisher key** |
| **4.22** | In Putnam resource allocation model, Rayleigh curve is modeled by the equation: | [`T1_MCQ.md#Q422`](T1_MCQ.md) | **(c) $m(t) = 2Kat \cdot e^{-at^2}$** | **Matched to slide question and publisher key** |
| **4.23** | In Putnam resource allocation model, technology factor 'C' is defined as: | [`T1_MCQ.md#Q423`](T1_MCQ.md) | **(a) $C = S \cdot K^{-1/3} \cdot t_d^{-4/3}$** | **Matched to slide question and publisher key** |
| **4.24** | Risk management activities are divided in: | [`T1_MCQ.md#Q424`](T1_MCQ.md) | **(b) 2 Categories** | **Matched to slide question and publisher key** |
| **4.25** | Which one is not a risk management activity? | [`T1_MCQ.md#Q425`](T1_MCQ.md) | **(c) Risk generation** | **Matched to slide question and publisher key** |

---

### B. Written Textbook Exercises (36 unique exercises)

Every numbered exercise is listed once below. Exercise 4.36 appears in two packs with distinct treatments; it remains one source exercise, not two unique exercises.

| Exercise | Source-aligned topic | Pack location | Pack item |
|:---:|:---|:---|:---|
| **4.1** | Project-planning activities | [`T2_Descriptive.md`](T2_Descriptive.md) | Exercise 4.1 |
| **4.2** | Two software size-estimation techniques | [`T2_Descriptive.md`](T2_Descriptive.md) | Exercise 4.2 |
| **4.3** | Semicolon counting versus LOC in C | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | Exercise 4.3 |
| **4.4** | Design a LOC counter; language dependence and limitations | [`T5_Apply_Scenarios.md`](T5_Apply_Scenarios.md) | Exercise 4.4 |
| **4.5** | Function-point calculation from domain counts and CAF | [`T7_Calculations.md`](T7_Calculations.md) | Problem 7.1 |
| **4.6** | Function points and industry acceptance | [`T2_Descriptive.md`](T2_Descriptive.md) | Exercise 4.6 |
| **4.7** | Size metrics and FP versus LOC | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | Exercise 4.7 |
| **4.8** | Feasibility of estimating size before coding | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | Exercise 4.8 |
| **4.9** | Albrecht's function-count method and example | [`T2_Descriptive.md`](T2_Descriptive.md) | Exercise 4.9 |
| **4.10** | Function-point calculation for payroll system | [`T7_Calculations.md`](T7_Calculations.md) | Problem 7.2 |
| **4.11** | Expanded payroll system with historical self-interface | [`T7_Calculations.md`](T7_Calculations.md) | Problem 7.3 |
| **4.12** | Walston-Felix versus SEL estimation | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | Exercise 4.12 |
| **4.13** | Estimate 22 KLOC with static models | [`T7_Calculations.md`](T7_Calculations.md) | Problem 7.4 |
| **4.14** | Infer size/productivity from 100 person-months | [`T7_Calculations.md`](T7_Calculations.md) | Problem 7.5 |
| **4.15** | COCOMO modes and phase distribution | [`T2_Descriptive.md`](T2_Descriptive.md) | Exercise 4.15 |
| **4.16** | Basic COCOMO for 32 KLOC organic project | [`T7_Calculations.md`](T7_Calculations.md) | Problem 7.6 |
| **4.17** | Productivity relation across COCOMO modes | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | Exercise 4.17 |
| **4.18** | Phase distribution under changed cost-driver ratings | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | Exercise 4.18 |
| **4.19** | Design a COCOMO estimation program and extend its use | [`T5_Apply_Scenarios.md`](T5_Apply_Scenarios.md) | Exercise 4.19 |
| **4.20** | Five-module office-automation system; estimate cost, schedule, and phases | [`T7_Calculations.md`](T7_Calculations.md) | Problem 7.7 |
| **4.21** | Compare all three COCOMO modes for 600 KLOC | [`T7_Calculations.md`](T7_Calculations.md) | Problem 7.8 |
| **4.22** | COCOMO II details and project categories | [`T2_Descriptive.md`](T2_Descriptive.md) | Exercise 4.22 |
| **4.23** | COCOMO II infrastructure sector | [`T2_Descriptive.md`](T2_Descriptive.md) | Exercise 4.23 |
| **4.24** | COCOMO II stages and the evidence limits of a popularity claim | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | Exercise 4.24 |
| **4.25** | COCOMO II calculation for 100 KLOC with supplied drivers | [`T7_Calculations.md`](T7_Calculations.md) | Problem 7.9 |
| **4.26** | Putnam model and limitations | [`T2_Descriptive.md`](T2_Descriptive.md) | Exercise 4.26 |
| **4.27** | Putnam time-cost trade-off | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | Exercise 4.27 |
| **4.28** | Putnam software-equation derivation | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | Exercise 4.28 |
| **4.29** | Putnam numerical problem with S=100,000, C=5000, D0=15 | [`T7_Calculations.md`](T7_Calculations.md) | Problem 7.10 |
| **4.30** | Gather productivity data and compare estimation models | [`T5_Apply_Scenarios.md`](T5_Apply_Scenarios.md) | Exercise 4.30 |
| **4.31** | Planning before detailed requirements/design | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | Exercise 4.31 |
| **4.32** | Risks and staff turnover | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | Exercise 4.32 |
| **4.33** | Risk-management activities and prioritization | [`T2_Descriptive.md`](T2_Descriptive.md) | Exercise 4.33 |
| **4.34** | Risk exposure and control techniques | [`T2_Descriptive.md`](T2_Descriptive.md) | Exercise 4.34 |
| **4.35** | Risk definition, management economics, and project cost | [`T3_Compare_Analyze.md`](T3_Compare_Analyze.md) | Exercise 4.35 |
| **4.36** | Risk analysis of a student project | [`T3_Compare_Analyze.md and T5_Apply_Scenarios.md`](T3_Compare_Analyze.md and T5_Apply_Scenarios.md) | Exercise 4.36; complementary broad taxonomy / RMMM case |

---

### C. Textbook Worked Examples — 19-item Inventory and Coverage Disposition

Source topics and example numbers below were checked against the scanned chapter pages. “Reproduced” means the original worked example's inputs and calculation are represented; “covered by equivalent” means the same method or learning objective is practiced with different inputs; neither label claims verbatim copying.

| Example | Source locator and topic | Pack disposition |
|:---:|:---|:---|
| **4.1** | p. 147 — FPA counts with average complexity | Covered by equivalent FPA calculations in T7 P7.1/P7.11; different inputs. |
| **4.2** | pp. 147–148 — adjusted and unadjusted FP example | Covered by equivalent FPA calculations in T7 P7.1/P7.11; different inputs. |
| **4.3** | pp. 148–149 — mixed low/average/high FPA counts | Covered by mixed-rating practice in T7 P7.11; not an exact reproduction. |
| **4.4** | pp. 151–152 — SEL and Walston-Felix inverse/effort estimates | Covered by T7 P7.4/P7.5/P7.12; different inputs and requested outputs. |
| **4.5** | pp. 154–155 — Basic COCOMO, 400 KLOC across three modes | Covered by the all-mode comparison in T7 P7.8 with a different size. |
| **4.6** | pp. 155–156 — 200 KLOC semidetached effort, time, staffing, productivity | Covered across T7 P7.6/P7.8 and the COCOMO comparisons; not an exact reproduction. |
| **4.7** | p. 160 — Intermediate COCOMO, embedded project and developer-pool alternatives | Driver sensitivity is practiced in T7 P7.7; the original embedded scenario is not reproduced. |
| **4.8** | pp. 160–161 — Detailed COCOMO and phase-wise effort/schedule | Concepts and phase allocation are covered in T2/T3 and T7 P7.7; no separate detailed-model numerical reproduction. |
| **4.9** | pp. 166–167 — Application Composition / Object Points | Reproduced in T7 P7.20. |
| **4.10** | pp. 172–173 — COCOMO II Early Design | Reproduced in T7 P7.21. |
| **4.11** | pp. 180–181 — COCOMO II Post-Architecture effort adjustment | Post-Architecture calculation is covered in T7 P7.9 with different inputs. |
| **4.12** | p. 184 — Rayleigh peak manning | Reproduced in T7 P7.15. |
| **4.13** | pp. 184–185 — manpower cost at elapsed times and peak time | Staffing curve is applied at selected times in T7 P7.15–P7.16; different inputs. |
| **4.14** | p. 186 — difficulty and manpower build-up | Metric practice appears in T7 P7.17 with different inputs; not an exact reproduction. |
| **4.15** | pp. 190–191 — development sub-cycle effort, peak time, difficulty/build-up | Covered across T7 P7.15/P7.19; the source's combined scenario is not reproduced. |
| **4.16** | p. 191 — avionics project and technology factor | Schedule/effort trade-off is practiced in T7 P7.18; original avionics case is not reproduced. |
| **4.17** | p. 191 — software size from development effort, time, and technology factor | Reproduced in T7 P7.22. |
| **4.18** | pp. 191–192 — real-time project and schedule reduction | Schedule-compression effect is covered in T7 P7.18 with a different duration assumption. |
| **4.19** | pp. 192–193 — integrated Putnam minimum-time, effort, staffing, and productivity calculation | Its component metrics are covered across T7 P7.10/P7.15–P7.19/P7.22; the full integrated case is not reproduced as one item. |

**Disposition summary:** 4/19 source examples reproduced with their original inputs (4.9, 4.10, 4.12, 4.17); the other 15 have an explicit equivalent/partial coverage location above. Four examples (4.7, 4.8, 4.15, 4.19) are explicitly marked partial at the scenario level; the core model concepts are covered elsewhere in the packs. No source example is silently counted as an exact reproduction.

---

## 3. Selective Supporting-Source Use

The question packs cite the primary course textbook and its companion slides. The current audit found no used answer claim that needed a supporting-book source; therefore, no claims from B.B. Agarwal et al., Pressman, Sommerville, Rajib Mall, or Leach are incorporated. A blanket five-book-by-18-term matrix is outside the course-source audit and is not a closure gate. If a primary-source gap is found later, record the specific gap and verify only the relevant supporting passage before using it.

## 4. Equation Register (Reconciled to Live Packs)

The register below was reconciled against the live packs and chapter source images/OCR, then calculation-bearing items were independently recalculated. It lists formulas used or directly tested in the packs; “shown calculations” refers to the finite examples mapped in the final column, not every possible application of that formula:

| Eq # | Formula Name | Formula as previously recorded | Claimed source locator | Symbols & units as previously recorded | Audit status | Live-pack mapping |
|:---:|:---|:---|:---:|:---|:---:|:---|
| **1** | Three-Point PERT Size Estimate | $S_e = \frac{S_{opt} + 4 S_m + S_{pess}}{6}$ | p. 144; Slide 7 | $S_{opt}$: optimistic, $S_m$: most likely, $S_{pess}$: pessimistic (LOC) | **Formula checked; authored application algebraically checked** | T3 synthesis Q3.2 |
| **2** | Unadjusted Function Points | $\text{UFP} = \sum_{i=1}^5 \sum_{j=1}^3 W_{ij} Z_{ij}$ | p. 146; Slide 16 | $W_{ij}$: complexity weight, $Z_{ij}$: element count | **Formula/source checked; all shown calculations recalculated** | T1 Q4.6; T7 P7.1–P7.3, P7.11 |
| **3** | Complexity Adjustment Factor | $\text{CAF} = 0.65 + 0.01 \sum_{i=1}^{14} F_i$ | p. 147; Slide 21 | $F_i$: degree of influence ($0 \le F_i \le 5$) | **Formula/source checked; all shown calculations recalculated** | T1 Q4.1, Q4.6, Q4.13; T7 P7.1–P7.3, P7.11 |
| **4** | Adjusted Function Points | $\text{FP} = \text{UFP} \times \text{CAF}$ | p. 147; Slide 21 | $\text{FP}$: final functional size | **Formula/source checked; all shown calculations recalculated** | T1 Q4.1, Q4.6; T7 P7.1–P7.3, P7.11 |
| **5** | Walston-Felix Effort | $E = 5.2 \times L^{0.91} \text{ PM}$ | p. 150; Slide 36 | $L$: size in KLOC; $E$: effort in person-months | **Formula/source checked; all shown calculations recalculated** | T3 Ex 4.12; T7 P7.4, P7.5, P7.12 |
| **6** | Walston-Felix Schedule | $D = 4.1 \times L^{0.36} \text{ Months}$ | p. 150; Slide 36 | $L$: size in KLOC; $D$: duration in months | **Formula/source checked; all shown calculations recalculated** | T3 Ex 4.12; T7 P7.4, P7.12 |
| **7** | Average Staffing | $S = E / D \text{ Persons}$ | pp. 150, 153; Slides 34, 44 | $S$: average team size | **Definition and shown calculations checked** | T7 P7.4, P7.6, P7.8, P7.12–P7.13 |
| **8** | Size-Based Productivity | $P = \text{LOC} / E \text{ LOC/PM}$ | pp. 150, 153; Slide 34 | $P$: developer output rate | **Definition and shown calculations checked** | T7 P7.5, P7.8, P7.12–P7.13 |
| **9** | NASA SEL Effort | $E = 1.4 \times L^{0.93} \text{ PM}$ | p. 150; Slide 35 | $L$: size in KLOC; $E$: effort in person-months | **Formula/source checked; all shown calculations recalculated** | T3 Ex 4.12; T7 P7.4, P7.5, P7.12 |
| **10** | NASA SEL Schedule | $D = 4.6 \times L^{0.26} \text{ Months}$ | p. 150; Slide 35 | $L$: size in KLOC; $D$: duration in months | **Formula/source checked; all shown calculations recalculated** | T3 Ex 4.12; T7 P7.4, P7.12 |
| **11** | Basic COCOMO Effort | $E = a_b (\text{KLOC})^{b_b} \text{ PM}$ | p. 153; Slide 43 | Org: $2.4, 1.05$; Semi: $3.0, 1.12$; Emb: $3.6, 1.20$ | **Formula/source checked; all shown calculations recalculated** | T1 Q4.11; T7 P7.6, P7.8, P7.13 |
| **12** | Basic COCOMO Schedule | $D = c_b (E)^{d_b} \text{ Months}$ | p. 153; Slide 43 | $c_b=2.5$; Org: $0.38$; Semi: $0.35$; Emb: $0.32$ | **Formula/source checked; all shown calculations recalculated** | T7 P7.6, P7.8, P7.13 |
| **13** | Basic COCOMO Staffing | $\text{SS} = E / D \text{ Persons}$ | p. 153; Slide 44 | $\text{SS}$: staff size | **Definition and shown calculations checked** | T7 P7.6, P7.8, P7.13 |
| **14** | Basic COCOMO Productivity | $P = \text{KLOC} / E \text{ KLOC/PM}$ | p. 153; Slide 44 | $P$: monthly productivity | **Definition and shown calculations checked** | T7 P7.8, P7.13 |
| **15** | Intermediate COCOMO EAF | $\text{EAF} = \prod_{i=1}^{15} \text{EM}_i$ | pp. 156–159; Slides 51–62 | $\text{EM}_i$: 15 cost driver multipliers | **Formula/source checked; shown calculations and separate phase allocation recalculated** | T7 P7.7, P7.14 |
| **16** | Intermediate COCOMO Effort | $E = a_i (\text{KLOC})^{b_i} \times \text{EAF} \text{ PM}$ | pp. 156–159; Slides 51–62 | Org: $3.2, 1.05$; Semi: $3.0, 1.12$; Emb: $2.8, 1.20$ | **Formula/source checked; shown calculations recalculated** | T7 P7.7, P7.14 |
| **17** | COCOMO II New Object Points | $\text{NOP} = \text{OP} \times \frac{100 - \% \text{reuse}}{100}$ | pp. 162–167; Slides 73–84 | $\text{OP}$: raw object points count | **Formula/source checked; example recalculated** | T7 P7.20 |
| **18** | COCOMO II Application Effort | $E = \text{NOP} / \text{PROD} \text{ PM}$ | pp. 162–167; Slides 73–84 | $\text{PROD}$: developer capability rating | **Formula/source checked; example recalculated** | T7 P7.20 |
| **19** | COCOMO II Scale Exponent | $B = 0.91 + 0.01 \sum_{j=1}^5 \text{SF}_j$ | pp. 168–169; Slide 88 | $\text{SF}_j$: 5 scale factors ($[0, 5]$) | **Formula and worked use checked; arithmetic independently recalculated** | T1 Q4.29; T7 P7.9, P7.21 |
| **20** | COCOMO II Early Design Effort | $E = 2.5 \times (\text{Size})^B \times \prod_{i=1}^7 \text{EM}_i$ (as used in textbook Example 4.10) | pp. 172–173; Example 4.10 | 7 aggregated cost drivers | **Source and pack formula matched; arithmetic recalculated** | T7 P7.21 |
| **21** | COCOMO II Post-Architecture Effort | $E = 2.94 \times (\text{Size})^B \times \prod_{i=1}^{17} \text{EM}_i$ | pp. 168–181; Slides 90–120 | 17 detailed cost drivers | **Formula and worked use checked; arithmetic independently recalculated** | T7 P7.9 |
| **22** | Norden/Rayleigh Curve | $m(t) = \frac{K}{t_d^2} \cdot t \cdot e^{-t^2 / (2 t_d^2)}$ | pp. 182–183; Slide 128 | $K$: total life-cycle effort (PY), $t_d$: duration (yr) | **Formula and worked use checked; numerical answers independently recalculated** | T1 Q4.22, Q4.26; T4 D04; T5 Unit 5.6; T7 P7.15–P7.16 |
| **23** | Rayleigh Peak Manning | $m_0 = \frac{K}{t_d \sqrt{e}} \approx 0.6065 \frac{K}{t_d}$ | p. 184; Slides 130, 139 | $m_0$: peak staff (Persons); evaluated at $t = t_d$ | **Formula and worked use checked; numerical answers independently recalculated** | T1 Q4.26; T4 D04; T5 Unit 5.6; T7 P7.15 |
| **24** | Putnam Software Equation | $S = C_k \cdot K^{1/3} \cdot t_d^{4/3}$ | p. 187; Slide 166 | $S$: LOC, $C_k$: technology constant | **Formula and worked use checked; numerical answers independently recalculated** | T1 Q4.23, Q4.27; T3 Ex 4.27–4.28; T7 P7.10, P7.17–P7.19, P7.22 |
| **25** | Putnam Effort-Time Trade-off | $K \cdot t_d^4 = \frac{S^3}{C_k^3} = \text{Constant}$ | pp. 187–188; Slide 166 | Fourth-power schedule trade-off | **Algebra and worked use checked** | T1 Q4.27; T3 Ex 4.27; T7 P7.18 |
| **26** | Putnam Difficulty Metric | $D = K / t_d^2$ | p. 186; Slide 137 | $D$: difficulty, persons/year | **Formula and worked use checked; numerical answers independently recalculated** | T1 Q4.8; T7 P7.17–P7.18 |
| **27** | Putnam Manpower Build-Up Metric | $D_0 = K / t_d^3$ | pp. 186–187; Slides 140, 143 | $D_0$: persons/year$^2$ | **Formula and worked use checked; numerical answers independently recalculated** | T1 Q4.8; T7 P7.10, P7.17 |
| **28** | Development Sub-Cycle Relation | $K=6K_d$; hence $K_d=K/6$ | pp. 189–191; Slides 155–156 | Full-project effort $K$ vs development-sub-cycle effort $K_d$ | **Formula and worked use checked; numerical answers independently recalculated** | T7 P7.10, P7.19 |
| **29** | Effort accumulated by release | $E(t_d)=K(1-e^{-1/2})\approx0.3935K$ | p. 183; Slide 151 | Integral of full-project curve to release; distinct from $K_d$ | **Integral and source distinction checked** | T2, T4 D04, T7 P7.10, V4 |
| **30** | Risk Exposure | $\text{RE} = P \times L$ | printed p. 197; Slide 191 | $P$: probability of incurring a loss; $L$: potential magnitude of loss | **Source checked** | T1 Q4.33; T2/T4/T5/V4 risk items |

---

### Quantitative Mathematical Validation Metrics

- The register contains 30 formula or relationship rows reconciled against the live packs. It marks source formulas, definitions, and derived relations separately and maps each used relationship to the applicable item.
- T7 contains 22 worked items: 10 assigned textbook exercises, 8 authored practice questions, and 4 source examples reproduced with original inputs. Their displayed numerical results were recalculated independently, including units, model/stage selection, rating multipliers, intermediate precision, and rounding.
- The 19-source-example inventory distinguishes exact reproduction from equivalent or partial coverage. Partial coverage is disclosed for integrated source scenarios not reproduced as one full problem. The formula register is a finite-pack audit, not a claim to validate every formula in every companion book.
- **Putnam notation correction:** $D=K/t_d^2$ is difficulty; $D_0=K/t_d^3$ is manpower build-up. The full-curve cumulative effort at release is $E(t_d)=0.3935K$, whereas the book separately defines development-sub-cycle effort by $K=6K_d$. Earlier materials conflated these quantities; corrected T2/T3/T4/T7/V4 and the formula register.
- **Source discrepancies explicitly documented without silent alteration:**
  - Book Table 4.7 (printed p. 159; 106% effort / 110% schedule) faithfully documented alongside normalized 100% allocation.
  - Ex 4.14 dual-model interpretation (Walston-Felix vs SEL).
  - Ex 4.20 sensitivity under the prompt's ambiguous single “programmer experience” rating: baseline AEXP $\approx 43.91$ PM; alternatives LEXP $\approx 44.29$ PM and VEXP $\approx 42.74$ PM. The wording does not justify multiplying all three experience drivers as low.
  - Ex 4.25 domain description ("application generator") reconciled with mandatory Post-Architecture mathematical inputs.

---

## 5. Chapter Closure Readiness Status — CLOSED

The source inventory covers all 25 official slide MCQs, all 36 numbered textbook exercises, the 18 instructor terms, and all 19 numbered worked examples. Exercise/example coverage does not imply every original example is reproduced exactly: the disposition ledger distinguishes four exact reproductions, equivalent practice, and explicitly partial scenario coverage. No supplementary-book claim is used without a demonstrated primary-source gap.

The equation register is reconciled to 30 used or directly tested relationships. The 22 T7 worked items were independently recalculated; the index records formula/source mappings and the chapter's known interpretation limits. The Putnam section uses corrected printed-page anchors and distinguishes full-project cumulative effort from development-sub-cycle effort.

**Final gate passed (2026-10-19):** all eight Markdown files pass strict lint; all eight PDFs were re-exported after the corrections and are newer than their Markdown sources; PyMuPDF found zero blank-like pages and zero leaked build markers; the final PDF total is 122 pages (110 across the seven study packs plus 12 index pages). MCQ, calculation, diagram, vocabulary, and affected index pages were visually inspected. Long worked solutions flow across pages where needed, with the prompt and solution start kept together. Scope boundary: this closes the course chapter pack and its stated coverage inventory; it does not claim every page of every supporting textbook or all 207 source slides was visually inspected. The primary chapter, its 36 numbered exercises, 25 official slide MCQs, 19 source examples, and 18 instructor terms have explicit coverage records.


<div class="page-break"></div>

## Retrieval set

1. **Which source governs chapter answers, and when may a supporting text be used?**
   - K.K. Aggarwal & Yogesh Singh, *Software Engineering* (3rd ed.) is the primary authority. Use a supporting text only to resolve a specific gap or ambiguity in that source.
2. **What do the example dispositions mean?**
   - “Reproduced” keeps the source example's original inputs; “equivalent” practices the same method with different inputs; “partial” means the original integrated scenario is not fully reproduced.
3. **How are the two Putnam effort quantities distinguished?**
   - Full-curve effort accumulated by $t_d$ is approximately $0.3935K$; the separate development-sub-cycle effort is $K_d=K/6$.
