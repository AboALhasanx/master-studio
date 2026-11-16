# V9 Predictive Vocabulary — Software Maintenance

> **PREDICTIVE · NOT CONFIRMED BY THE INSTRUCTOR.** No official Chapter 9 vocabulary list or notes were found in the current vault as of 2026-10-23. This is a navigation forecast from the course text, companion slides, and exercise headings. It is not a syllabus, exam-weight estimate, or permission to include every branch in the final study pack. Replace/reconcile it when Dr. Ali Fahim's actual list arrives.

## A. Likely Core Headings from Course Material & Authored Pack Locators

### 1. Software Maintenance — Basic Concepts
- Meaning, purpose, importance, and scope of software maintenance `[T1: Q9.1, Q9.2; T2: Q9.D1, Q9.D4]`
- Maintenance versus new software development `[T3: Q9.A2, Q9.A10]`
- Corrective, adaptive, perfective, and preventive maintenance `[T1: Q9.3, Q9.4, Q9.6, Q9.8, Q9.9; T2: Q9.D1, Q9.D4]`
- Maintenance effort distribution (50% Perfective, 25% Adaptive, 21% Corrective, 4% Preventive) `[T1: Q9.8; T2: Q9.D1, Q9.D4]`
- Maintenance manageability and common misconceptions `[T3: Q9.A1, Q9.A2]`

### 2. Maintenance Problems and Management
- Common technical and organizational problems during maintenance `[T2: Q9.D3]`
- Causes of maintenance difficulty and engineering responses `[T2: Q9.D3; T3: Q9.A1]`
- Maintenance in a one-person software-production organization `[T2: Q9.D2]`
- Budget and effort reallocation; replacement versus continued maintenance `[T3: Q9.A10; T5: Scenario 5]`

### 3. The Maintenance Process and Maintainability
- 4-phase maintenance process workflow (Input objectives, Phases 1–4, Pass testing? gate) `[T2: Q9.D5; T4: Q9.F1]`
- Program understanding and self-descriptiveness `[T2: Q9.D5, Q9.D6]`
- Generating particular maintenance proposal and extensibility `[T2: Q9.D5; T4: Q9.F1]`
- Ripple-effect accounting and program stability (resistance to change amplification) `[T2: Q9.D5; T3: Q9.A3; T4: Q9.F1]`
- Modified-program testing and testability `[T2: Q9.D5; T4: Q9.F1]`
- Single-Entry Single-Exit (SESE) modules as testing/maintenance factor `[T3: Q9.A11]`
- High module coupling as a maintenance bottleneck `[T3: Q9.A12]`
- Specifying maintainability in an SRS `[T2: Q9.D21]`

### 4. Software Maintenance Models
- Quick-fix model (emergency patching, architectural decay) `[T1: Q9.5, Q9.11; T2: Q9.D8; T5: Scenario 1]`
- Iterative-enhancement model and its 3-stage cycle (Analysis $\to$ Redesign $\to$ Implementation) `[T1: Q9.12; T2: Q9.D9; T5: Scenario 1]`
- Reuse-oriented model and OO design `[T2: Q9.D10; T5: Scenario 1]`
- Boehm maintenance model and decision-driven workflow `[T4: Q9.F2; T5: Scenario 1]`
- Taute maintenance model and its 8 sequential phases `[T1: Q9.13; T2: Q9.D11; T4: Q9.F3; T5: Scenario 1]`

### 5. Maintenance Cost Estimation
- Defect-repair cost ratios across development phases (Analysis : Design : Implementation = 1 : 10 : 100) `[T2: Q9.D13]`
- Belady–Lehman maintenance-effort model ($M = P + K \cdot e^{c - d}$) `[T2: Q9.D12; T7: Q9.C1, Q9.C2]`
- Boehm's Annual Change Traffic (ACT) and Annual Maintenance Effort (AME) `[T1: Q9.14; T2: Q9.D13; T7: Q9.C3, Q9.C4]`
- Very High Effort Adjustment Factor (EAF) cost multipliers `[T7: Q9.C4]`
- Worked maintenance-effort and 10-year life-cycle cost calculations `[T7: Q9.C1–Q9.C5]`

### 6. Regression Testing
- Definition, purpose, and distinction from development testing `[T1: Q9.2, Q9.15; T3: Q9.A4]`
- Regression-test selection and selective retesting vs Retest-All `[T1: Q9.16, Q9.17; T3: Q9.A5, Q9.A6; T5: Scenario 3]`
- Coverage-based, minimization, and safe techniques (hazards of minimization) `[T1: Q9.18; T3: Q9.A7; T5: Scenario 3]`
- Rothermel & Harrold evaluation criteria (Inclusiveness, Precision, Efficiency, Generality) `[T1: Q9.19; T3: Q9.A8]`

### 7. Reverse Engineering, Reengineering, and Legacy Software
- Reverse engineering: meaning, purpose, levels of abstraction, and tools `[T1: Q9.1, Q9.21; T2: Q9.D14, Q9.D15; T4: Q9.F5]`
- Redocumentation (horizontal) vs Design/Specification Recovery (vertical) `[T2: Q9.D14; T4: Q9.F5]`
- Reverse engineering versus reengineering and forward engineering `[T1: Q9.24, Q9.25; T3: Q9.A9, Q9.A10]`
- Reengineering versus new software development economics (Sneed's rule) `[T3: Q9.A10; T5: Scenario 5]`
- 8 Canonical textbook recommendations for modifying legacy code `[T1: Q9.20; T2: Q9.D16; T5: Scenario 2]`
- Restructuring techniques (Control flow, Efficiency, Adaption) `[T1: Q9.22; T2: Q9.D17]`

### 8. Software Configuration Management
- 4 SCM activities (Identification, Change Control, Auditing, Status Accounting) `[T1: Q9.23; T2: Q9.D18]`
- Governing authority: Configuration Control Authority (CCA) `[T2: Q9.D18; T4: Q9.F4; T5: Scenario 4]`
- 18-Field Change-Request Form performa `[T4: Q9.F4; T5: Scenario 4]`
- Software versions: Revisions versus Variations `[T2: Q9.D18; T5: Scenario 4]`

### 9. Software Documentation and Maintenance Tools
- User, system, and programmer documentation categories `[T2: Q9.D25]`
- Essential documents and tools to maintain large software `[T2: Q9.D20]`
- Documentation impact on system success and maintenance outcomes `[T2: Q9.D19; T3: Q9.A1]`
- Maintenance programmer characteristics and cognitive challenges `[T2: Q9.D23, Q9.D24]`

## B. Lower-Confidence Branches (Excluded Unless Confirmed by Dr. Ali Fahim)

- Secondary survey statistics and historical 1970s mainframe request breakdowns beyond the textbook.
- Third-party tool taxonomies outside textbook-cited categories.
- Detailed maintainability metrics beyond MTTR, cyclomatic ceiling, and coupling constraints.
- Business Process Reengineering (BPR) deep organizational theory outside the definition in Q9.24.

## C. Evidence and Confidence Boundary

- **Strong Source Evidence:** Grounded directly in `AliFahim_Software_Engineering.pdf` (pp. 459–491) and companion slides `Ch09_Software_Maintenance.pdf` (Slides 1–75).
- **Provisional Label Retained:** Because Dr. Ali Fahim's official vocabulary and lecture notes have not been delivered, this vocabulary remains predictive and subject to reconciliation once official notes arrive.
