# V9 Source Atlas and Question Inventory — Planning & Verification Matrix

**Status:** Chapter 9 question and evidence mapping ledger. Authored packs: `T1_MCQ.md`, `T2_Descriptive.md`, `T3_Compare_Analyze.md`, `T4_Diagrams.md`, `T5_Apply_Select.md`, `T7_Calculations.md`, and merged volume `Ch09_Software_Maintenance_Print.pdf` (42 pages; current as of 2026-10-24). Earlier 55-page count is superseded. Instructor vocabulary remains unreceived; this atlas maps course textbook and companion slide coverage.

## 1. Course sources and verified boundaries

| Source | Verified location | Use / limit |
|---|---|---|
| Scanned course text, `AliFahim_Software_Engineering.pdf` | Ch09 printed pp. 459–491; PDF spreads 235–251. Printed pp. 499–500 contain publisher answer key for MCQ 9.1–9.25. Printed p. 490 begins exercises 9.1–9.16; printed p. 491 contains exercises 9.17–9.40. Printed p. 492 begins Chapter 10. | High-confidence K.K. Aggarwal & Yogesh Singh 3rd-ed identity from internal structure and matching companion slides; scan cover/title page is absent. Image-only; verified by OCR and visual inspection. |
| K.K. Aggarwal & Yogesh Singh companion slides | Canonical `Ch09_Software_Maintenance.pdf`, 75 pp. | Official companion slide source containing 25 MCQs (Slides 64–69) and 40 Exercises (Slides 70–75). |

## 2. Companion-Slide Map

- Slides 2–9: definition, purpose, categories, effort distribution (50% Perfective, 25% Adaptive, 21% Corrective, 4% Preventive), problems, manageability.
- Slides 10–12: maintenance process (Fig. 9.2: 4 phases, quality attributes, Pass testing? feedback gate).
- Slides 13–21: quick-fix (Fig. 9.3), iterative enhancement (Fig. 9.4), reuse model (Fig. 9.5), Boehm model (Fig. 9.6), and Taute 8-phase model (Fig. 9.7).
- Slides 22–31: defect repair cost ratios (1:10:100), Belady–Lehman ($M = P + K e^{c-d}$), Boehm ACT/AME with EAF, examples 9.1–9.3.
- Slides 32–39: regression testing, development vs regression testing, selective retest, Rothermel & Harrold evaluation criteria.
- Slides 40–53: reverse engineering levels of abstraction (Fig. 9.11), domain mapping (Fig. 9.10), reengineering vs new development (Fig. 9.12), legacy code modification suggestions (Slide 49), restructuring types (Slide 51).
- Slides 54–58: configuration management activities (4 categories), CCA authority, change request form (Fig. 9.14).
- Slides 59–63: user and system documentation (Tables 9.5 & 9.6).
- Slides 64–69: 25 publisher MCQs (9.1–9.25); answer key on scanned book pp. 499–500.
- Slides 70–75: 40 publisher exercises (9.1–9.40).

## 3. Publisher Exercise Coverage Inventory (Exercises 9.1 – 9.40)

Every one of the 40 publisher exercises is accounted for and mapped to its primary deliverable pack and question ID:

| Exercise | Core Topic Stem | Assigned Study Pack | Question ID | Verified Source Grounding |
|:---:|:---|:---:|:---:|:---|
| **9.1** | What is software maintenance? Categories & maximum effort | `T2_Descriptive` | Q9.D1 | Book p. 459, Slide 4; Perfective 50% |
| **9.2** | Implication of maintenance for one person organisation | `T2_Descriptive` | Q9.D2 | Book p. 461, Slide 6; resource exhaustion |
| **9.3** | "Maintenance is manageable" opinion | `T3_Compare_Analyze` | Q9.A1 | Book p. 462, Slide 7; engineering vs chaos |
| **9.4** | Problems during maintenance & solutions | `T2_Descriptive` | Q9.D3 | Book p. 462, Slide 7; SCM, regression test |
| **9.5** | Mistake of considering maintenance inferior to development | `T3_Compare_Analyze` | Q9.A2 | Book p. 463, Slide 8; cognitive difficulty |
| **9.6** | Importance of maintenance & maximum effort category | `T2_Descriptive` | Q9.D4 | Book p. 460, Slide 5; Perfective 50% |
| **9.7** | Steps of software maintenance with diagram | `T4_Diagrams` / `T2` | Q9.F1 / Q9.D5 | Fig 9.2: 4 phases, attributes, test gate |
| **9.8** | Self descriptiveness of a program & maintenance effect | `T2_Descriptive` | Q9.D6 | Book p. 464, Slide 11; understanding speed |
| **9.9** | Ripple effect & effect on program stability | `T3_Compare_Analyze` | Q9.A3 | Book p. 465 definition: resistance to change |
| **9.10** | Maintainability & role during maintenance | `T2_Descriptive` | Q9.D7 | Book p. 465, Slide 12; holistic attribute |
| **9.11** | Quick-fix model advantages & disadvantages | `T2_Descriptive` / `T5` | Q9.D8 / Scen 1 | Fig 9.3: emergency speed vs entropy |
| **9.12** | Iterative enhancement model & three-stage cycle | `T2_Descriptive` / `T5` | Q9.D9 / Scen 1 | Fig 9.4: Analysis $\to$ Redesign $\to$ Implement |
| **9.13** | Boehm's maintenance model with diagram | `T4_Diagrams` | Q9.F2 | Fig 9.6: Understand, Strategy, Validate |
| **9.14** | Reuse oriented model steps & OO design | `T2_Descriptive` / `T5` | Q9.D10 / Scen 1 | Fig 9.5: Identify, Analyze, Modify, Integrate |
| **9.15** | Taute maintenance model & 8 phases | `T2_Descriptive` / `T4` | Q9.D11 / Q9.F3 | Fig 9.7: 8 phases (Request $\to$ Release) |
| **9.16** | Belady and Lehman model short note | `T2_Descriptive` | Q9.D12 | Book p. 470, Slide 23; $M = P + K e^{c-d}$ |
| **9.17** | Various maintenance cost estimation models | `T2_Descriptive` | Q9.D13 | Defect ratio (1:10:100), Belady, Boehm ACT |
| **9.18** | Belady-Lehman calculation (600 PM, K=0.5, c=7, d=0.7) | `T7_Calculations` | Q9.C1 | Scanned book printed p. 491: $M = 872.29\text{ PM}$ |
| **9.19** | 10-Year Life-cycle cost (ACT 25%, 20 lacs) | `T7_Calculations` | Q9.C5 | Scanned book printed p. 491: $70\text{ lacs}$ total |
| **9.20** | Regression testing vs development testing | `T3_Compare_Analyze` | Q9.A4 | Book p. 473, Slide 33; multi-dimensional |
| **9.21** | Importance of regression test selection with examples | `T3_Compare_Analyze` | Q9.A5 | Book p. 474, Slide 35; delta execution |
| **9.22** | Selective retest techniques vs retest-all | `T3_Compare_Analyze` | Q9.A6 | Book p. 474, Slide 36; safety vs cost |
| **9.23** | Categories of retest techniques; why minimization not useful | `T3_Compare_Analyze` | Q9.A7 | Book p. 475, Slide 38; minimization non-safe |
| **9.24** | Evaluation categories for RTS techniques | `T3_Compare_Analyze` | Q9.A8 | Inclusiveness, Precision, Efficiency, Generality |
| **9.25** | Reverse engineering definition & levels | `T2_Descriptive` / `T4` | Q9.D14 / Q9.F5 | Fig 9.11: Implementation, Design, Spec |
| **9.26** | Reverse engineering tools & discuss two | `T2_Descriptive` | Q9.D15 | Parsers (AST) and Call-Graph Extractors |
| **9.27** | Reverse engineering and re-engineering | `T3_Compare_Analyze` | Q9.A9 | Comprehension vs mutating lifecycle |
| **9.28** | Re-engineering vs new development | `T3_Compare_Analyze` | Q9.A10 | Fig 9.12; risk, tacit knowledge, Sneed's rule |
| **9.29** | Suggestions for modifying legacy code | `T5_Apply_Select` / `T2` | Scen 2 / Q9.D16 | 8 canonical textbook points (Slide 49 / p. 480) |
| **9.30** | Types of restructuring techniques | `T2_Descriptive` | Q9.D17 | Control flow, Efficiency, Adaption (Slides 51–53) |
| **9.31** | Why single entry, single exit modules make testing easier | `T3_Compare_Analyze` | Q9.A11 | Structured control flow, predictable conditions |
| **9.32** | Configuration management activities & Change Request Form | `T2` / `T4` / `T5` | Q9.D18 / Q9.F4 / Scen 4 | 4 SCM activities, CCA authority, 18-field Form |
| **9.33** | Documentation quantity/quality & system success | `T2_Descriptive` | Q9.D19 | Rebuilding mental models, reducing reverse-eng tax |
| **9.34** | Tools and documents to maintain large software | `T2_Descriptive` | Q9.D20 | SRS, SDD, code, test suites; SCM, cross-ref |
| **9.35** | High degree of coupling makes maintenance difficult | `T3_Compare_Analyze` | Q9.A12 | Amplifies ripple effect, destroys module isolation |
| **9.36** | Specifying maintainability in SRS | `T2_Descriptive` | Q9.D21 | Quantitative MTTR $\le 2$h, complexity limits |
| **9.37** | Tools and techniques available for maintenance | `T2_Descriptive` | Q9.D22 | Program slicing and automated restructuring |
| **9.38** | Maintenance challenges vs new dev & programmer profile | `T2_Descriptive` | Q9.D23 | Cognitive constraints, reverse-eng aptitude |
| **9.39** | Why little attention is paid to maintainability during design | `T2_Descriptive` | Q9.D24 | Schedule pressure, separate cost centers |
| **9.40** | List out system documentation and explain purpose | `T2_Descriptive` | Q9.D25 | SRS, SDD, code listings, test plans (Table 9.6) |

## 4. Publisher MCQ Master Key (Q9.1 – Q9.25)

All 25 MCQs are verified 100% against printed pp. 499–500 in `T1_MCQ.md`.

## 5. Quantitative Models & Form Details Verified

- **Belady-Lehman:** $M = P + K \cdot e^{c - d}$; verified printed p. 470; Example 9.1 sensitivity: $2.23\times$ increase in overhead ($809.18\text{ PM}$ vs $363.59\text{ PM}$).
- **Boehm ACT/AME:** $AME = ACT \times SDE \times EAF$; Example 9.2 Slide 28 typo resolved: $10 \times 90 = 900\text{ PM}$, Total $= 1500\text{ PM}$. Example 9.3 $AEXP = 0.82$ confirmed **Very High**.
- **Exercise 9.18 & 9.19:** Confirmed printed on **page 491** (not 490).
- **SCM Change Request Form:** Fig. 9.14 confirmed on **page 485**, 18 fields, governed by **CCA** (Configuration Control Authority).
