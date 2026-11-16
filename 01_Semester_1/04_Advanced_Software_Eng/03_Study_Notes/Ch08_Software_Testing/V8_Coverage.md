# ASE Chapter 8 — V8 Predictive Vocabulary Coverage Ledger

> **Course:** Advanced Software Engineering (CS603) — Asst. Prof. Dr. Ali Fahim Ni'ma  
> **Source Material:** K.K. Aggarwal & Yogesh Singh, *Software Engineering* (3rd ed.), Chapter 8: Software Testing (printed pp. 365–458 / official companion slides 1–212)  
> **STATUS:** **PREDICTIVE / تنبؤي — NOT CONFIRMED BY THE INSTRUCTOR.**  
> This working vocabulary ledger is inferred from the course-aligned Chapter 8 deck and textbook scan. The student has not yet supplied Dr. Ali Fahim's official Chapter 8 vocabulary list. These terms are preparation candidates, not official scope, exam probabilities, or marks. Keep this label until the instructor's actual list is received.

---

## Section A: Testing Foundations & Life-Cycle Governance

### Leaf A.01 · Definition and Purpose of Software Testing
- **Core Concepts:** Executing software with the intent of finding errors (Myers, 1979); consuming 30%–50% of total lifecycle effort; establishing operational confidence.
- **Pack Locations:**
  - `T1_MCQ.md`: Question 8.1
  - `T2_Descriptive.md`: Questions 8.1, 8.2, 8.3
- **Source Locators:** Textbook §8.1 & §8.1.1, pp. 365–366; Slides 4–7.

### Leaf A.02 · Who Performs Testing & Developer Psychology
- **Core Concepts:** Independence of testers; developer psychological blind spots toward own defects; separation of development and verification teams.
- **Pack Locations:**
  - `T2_Descriptive.md`: Questions 8.2, 8.38, 8.43
- **Source Locators:** Textbook §8.1.1 & §8.6.2, pp. 366, 440; Slides 7–8, 178.

### Leaf A.03 · Impossibility of Complete / Exhaustive Testing
- **Core Concepts:** Input domain infinity; execution path explosion ($3^{20}$ paths); missing specifications; Dijkstra's invariant (testing proves presence, not absence of bugs).
- **Pack Locations:**
  - `T2_Descriptive.md`: Question 8.6
  - `T3_Compare_Analyze.md`: Question 8.8
  - `T5_Apply_Design.md`: Question 8.17
- **Source Locators:** Textbook §8.1.3, pp. 367–368; Slides 10–12.

### Leaf A.04 · Failure Taxonomy (Mistake, Bug, Fault, Failure)
- **Core Concepts:** Human error/mistake $\to$ fault/bug in code $\to$ failure during dynamic runtime execution; failure propagation and masking.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.2, 8.21, 8.42
  - `T2_Descriptive.md`: Questions 8.4, 8.11, 8.39
- **Source Locators:** Textbook §8.1.2, pp. 366–367; Slides 8–9.

### Leaf A.05 · Test Artifacts (Test, Test Case, Test Suite, Test Harness)
- **Core Concepts:** Test case definition (inputs, execution conditions, expected outputs); test suite aggregation; test harness / scaffolding components (drivers, stubs).
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.22, 8.40
  - `T2_Descriptive.md`: Questions 8.7, 8.23
- **Source Locators:** Textbook §8.1.4, pp. 368–369; Slides 13–15.

### Leaf A.06 · Verification vs. Validation (V&V)
- **Core Concepts:** Verification ("Are we building the product right?") vs. Validation ("Are we building the right product?"); customer requirements alignment.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.14, 8.15, 8.16, 8.44, 8.45
  - `T2_Descriptive.md`: Question 8.7
- **Source Locators:** Textbook §8.1.5, pp. 369–370; Slides 16–17.

---

## Section B: Functional / Black-Box Test Design Techniques

### Leaf B.01 · Boundary Value Analysis (BVA) & Single Fault Assumption
- **Core Concepts:** Testing extrema $\{min, min^+, nom, max^-, max\}$; single fault assumption; $4n + 1$ test cases for $n$ variables.
- **Pack Locations:**
  - `T1_MCQ.md`: Question 8.4
  - `T5_Apply_Design.md`: Questions 8.12, 8.13, 8.16, 8.21, 8.25
  - `T7_Calculations.md`: Computational Module 1
- **Source Locators:** Textbook §8.2.1, pp. 375–377; Slides 20–25.

### Leaf B.02 · Robustness Testing
- **Core Concepts:** Incorporating out-of-boundary invalid test points ($min^-, max^+$); error handling verification; $6n + 1$ test cases.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.5, 8.6
  - `T5_Apply_Design.md`: Questions 8.13, 8.25
  - `T7_Calculations.md`: Computational Module 1
- **Source Locators:** Textbook §8.2.1, pp. 377–378; Slides 25–26.

### Leaf B.03 · Worst-Case Testing & Multi-Variable Boundary Interactions
- **Core Concepts:** Rejecting single fault assumption; full Cartesian combinations of extreme points; $5^n$ test cases.
- **Pack Locations:**
  - `T3_Compare_Analyze.md`: Question 8.14
  - `T5_Apply_Design.md`: Question 8.13
  - `T7_Calculations.md`: Computational Module 1
- **Source Locators:** Textbook §8.2.1, pp. 378–380; Slides 27–34.

### Leaf B.04 · Equivalence Class Partitioning (Valid & Invalid Classes)
- **Core Concepts:** Partitioning input domain into disjoint classes; representative testing; weak/strong normal/robust testing criteria.
- **Pack Locations:**
  - `T1_MCQ.md`: Question 8.12
  - `T3_Compare_Analyze.md`: Question 8.15
  - `T5_Apply_Design.md`: Questions 8.16, 8.24, 8.25
- **Source Locators:** Textbook §8.2.2, pp. 380–384; Slides 35–46.

### Leaf B.05 · Decision Table Testing & Logic Combinations
- **Core Concepts:** Conditions, actions, rules, stubs; handling complex boolean dependencies; rule reduction using "Don't Care" ($-$).
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.10, 8.26
  - `T3_Compare_Analyze.md`: Question 8.18
  - `T5_Apply_Design.md`: Questions 8.16, 8.26
- **Source Locators:** Textbook §8.2.3, pp. 384–388; Slides 47–60.

### Leaf B.06 · Cause-Effect Graphing Technique
- **Core Concepts:** Transforming specifications into Boolean graphs; basic relations (AND, OR, NOT); constraints ($E, I, O, R, M$); synthesizing decision tables.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.13, 8.28
  - `T4_Diagrams.md`: Questions 8.19, 8.20
- **Source Locators:** Textbook §8.2.4, pp. 388–397; Slides 91–103.

---

## Section C: Structural / White-Box Testing & Path Metrics

### Leaf C.01 · Control Flow Graph (CFG) Construction & DD-Paths
- **Core Concepts:** Mapping statements to nodes and branches to edges; Decision-to-Decision paths (DD-paths); graph reduction.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.8, 8.9, 8.29
  - `T2_Descriptive.md`: Question 8.30
  - `T4_Diagrams.md`: Question 8.27
- **Source Locators:** Textbook §8.3, pp. 403–405; Slides 103–115.

### Leaf C.02 · Basis Path Testing & Independent Paths
- **Core Concepts:** Linearly independent paths introducing new edges; basis set size; guaranteed 100% statement and branch coverage.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.30, 8.36
  - `T2_Descriptive.md`: Question 8.31
  - `T3_Compare_Analyze.md`: Question 8.28
  - `T4_Diagrams.md`: Question 8.27
- **Source Locators:** Textbook §8.3.1, pp. 405–408; Slides 116–122.

### Leaf C.03 · McCabe's Cyclomatic Complexity V(G) Derivations
- **Core Concepts:** Three derivation methods ($e - n + 2P$, $P + 1$, and regions $R$); module threshold $V(G) \le 10$; cognitive complexity.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.31, 8.32, 8.33
  - `T3_Compare_Analyze.md`: Question 8.33
  - `T4_Diagrams.md`: Question 8.27
  - `T7_Calculations.md`: Question 8.32
- **Source Locators:** Textbook §8.3.1, pp. 408–410; Slides 120–139.

### Leaf C.04 · Graph Matrices, Connection Matrices & Path Powers
- **Core Concepts:** $N \times N$ square matrix representation; row weight complexity formula; matrix powers $A^k$ calculating $k$-hop paths; reachability.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.34, 8.35
  - `T7_Calculations.md`: Computational Module 2
- **Source Locators (verified from page images):** Textbook §8.4.3, pp. 427–429; companion slides 147–154. MCQ anchors: slides 196–197. The earlier §8.3.2 / pp. 410–415 locator was incorrect.

### Leaf C.05 · Data Flow Testing (du-Paths & dc-Paths)
- **Core Concepts:** Definitions ($\text{DEF}$), computational uses ($c$-use), predicate uses ($p$-use); definition-use paths ($du$); definition-clear paths ($dc$); anomaly detection.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.37, 8.38
  - `T2_Descriptive.md`: Question 8.35
  - `T4_Diagrams.md`: Question 8.34
- **Source Locators (verified from page images):** Textbook §8.4.4, printed pp. 430–434; companion slides 155–166. The deck distinguishes course-defined du-path and dc-path, predicate and computation uses, and its worked quadratic/triangle examples.

---

## Section D: Mutation Testing & Fault-Based Reliability

### Leaf D.01 · Mutation Testing Principles & Fault-Based Testing
- **Core Concepts:** Artificial fault injection; mutant generation; Competent Programmer Hypothesis; Coupling Effect Hypothesis.
- **Pack Locations:**
  - `T1_MCQ.md`: Question 8.39
  - `T3_Compare_Analyze.md`: Question 8.36
  - `T7_Calculations.md`: Computational Module 3
- **Source Locators:** Textbook §8.4.5, printed pp. 434–435; Slides 167–169. The named hypotheses are absent from the inspected course section; use DeMillo et al. (1978), [DOI](https://doi.org/10.1109/C-M.1978.218136), and qualify them with Ahmed et al. (2024), [DOI](https://doi.org/10.1002/stvr.1874).

### Leaf D.02 · Mutation Score (MS) & Equivalent Mutants
- **Core Concepts:** Killed vs surviving mutants; equivalent mutants ($E$) semantically identical to original; formula $MS = \frac{D}{N - E} \times 100\%$.
- **Pack Locations:**
  - `T7_Calculations.md`: Computational Module 3
- **Source Locators:** Textbook §8.4.5, printed p. 435; Slides 169. The score definition and test-suite-size caveat are visible in the primary source page image.

### Leaf D.03 · Error Seeding & Mills' Defect Estimation Model
- **Core Concepts:** Hypergeometric sampling; capture-recapture estimation of latent defects: $\hat{N} = \frac{S \times n}{s}$.
- **Pack Locations:**
  - `T7_Calculations.md`: Computational Module 4
- **Source Locators:** Textbook §8.5, pp. 433–435; Slide 198.

---

## Section E: Testing Levels & Integration Strategies

### Leaf E.01 · Unit Testing & Test Scaffolding
- **Core Concepts:** Isolated module testing; drivers (calling simulation) vs stubs (called simulation); desirability and limitations.
- **Pack Locations:**
  - `T1_MCQ.md`: Question 8.40
  - `T2_Descriptive.md`: Question 8.42
  - `T3_Compare_Analyze.md`: Question 8.37
- **Source Locators:** Textbook §8.5.1, printed pp. 436–437; companion slides 171–173. The scan contains the unit-testing rationale, isolation constraints, driver/stub scaffolding, harness alternative, and original Fig. 8.29; slide 173 reproduces the scaffolding figure.

### Leaf E.02 · Integration Testing Strategies
- **Core Concepts:** Testing module interfaces; Top-Down (stubs required, early architectural verification); Bottom-Up (drivers required, early utility verification); Sandwich/Hybrid; Big Bang.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.46, 8.48, 8.49
  - `T2_Descriptive.md`: Question 8.40
  - `T3_Compare_Analyze.md`: Question 8.41
- **Source Locators (verified from page images):** Course scan §8.5.2, printed pp. 437–439; companion slides 174–175. Integration begins at the foot of printed p. 437; Fig. 8.30 and strategy-selection guidance are on pp. 438–439; slide 175 reproduces the original three-strategy figure. The earlier §8.6.2 / pp. 440–442 / slides 175–177 locator was stale.

### Leaf E.03 · System Testing & Non-Functional Evaluation
- **Core Concepts:** Full system evaluation against SRS; functional, stress, load, security, and recovery testing; independent testing teams.
- **Pack Locations:**
  - `T2_Descriptive.md`: Question 8.43
  - `T3_Compare_Analyze.md`: Question 8.41
- **Source Locators (verified from page images):** Course scan §8.5.3, printed pp. 439–440; companion slides 176–177. The scan identifies five user-critical attributes and continues with operational-profile, modified-capability, performance, resource, availability, and recovery-time considerations; slide177 reproduces original Fig.31. The earlier §8.6.3 / pp.442–443 / slides177–179 locator was stale.

### Leaf E.04 · Acceptance Testing, Alpha & Beta Testing
- **Core Concepts:** Formal validation by users; Alpha testing at developer site; Beta testing at user sites; operational environment.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.11, 8.17, 8.18, 8.19, 8.20, 8.43, 8.50
  - `T2_Descriptive.md`: Questions 8.7, 8.9
  - `T3_Compare_Analyze.md`: Question 8.5
- **Source Locators:** Textbook §8.6.4, pp. 443–445; Slides 179–182.

### Leaf E.05 · Regression Testing
- **Core Concepts:** Re-testing modified software; preventing adverse side-effects; selective vs comprehensive re-testing; test suite prioritization.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 8.7, 8.24, 8.25, 8.41
  - `T3_Compare_Analyze.md`: Question 8.5
- **Source Locators:** Textbook §8.6.5, pp. 445–446; Slides 181–183.

---

## Section F: Debugging & Advanced Practical Testing

### Leaf F.01 · Debugging Paradigms (Inductive & Deductive)
- **Core Concepts:** Inductive debugging (data gathering $\to$ pattern formulation $\to$ hypothesis); Deductive debugging (elimination of hypotheses $\to$ refinement); Myers' process models.
- **Pack Locations:**
  - `T2_Descriptive.md`: Question 8.47
- **Source Locators:** Textbook §8.7, pp. 446–448; Slides 183–186.

### Leaf F.02 · Debugging Guidelines & Myers' Principles (Table 8.8)
- **Core Concepts:** Thinking before changing code; fixing root defects rather than symptoms; regression testing fixes; searching for identical defects.
- **Pack Locations:**
  - `T2_Descriptive.md`: Questions 8.45, 8.46
  - `T5_Apply_Design.md`: Question 8.44
- **Source Locators:** Textbook §8.7 & Table 8.8, p. 448; Slides 186–188.

### Leaf F.03 · Automated Testing Tools & 4GL Impact
- **Core Concepts:** Static vs dynamic testing tools; test data generators; execution monitors; 4th generation languages (4GLs) advantages, disadvantages, and testing cost justification.
- **Pack Locations:**
  - `T2_Descriptive.md`: Question 8.50
  - `T3_Compare_Analyze.md`: Questions 8.28, 8.41
- **Source Locators:** Textbook §8.8 & §8.9, pp. 448–450; Slides 187–188.

