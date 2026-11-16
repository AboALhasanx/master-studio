# Chapter 8 — Predictive Vocabulary and Branches

> **STATUS: PREDICTIVE / تنبؤي — NOT CONFIRMED BY THE INSTRUCTOR.**  
> This working list is inferred from the course-aligned Chapter 8 deck and a small set of candidate supporting-book sections. The student has not yet supplied Dr. Ali Fahim's Chapter 8 vocabulary list. These terms are preparation candidates, not official scope, exam probabilities, or marks. Keep this label until the instructor's actual list is received.

## A. Testing foundations — predictive, explicit teaching in the deck

1. **Software testing**
   - Meaning, purpose, and role in the software lifecycle.
   - Finding errors and building confidence that behavior matches requirements.
   - Who performs testing and why developer-only review has limits.
2. **What testing can establish**
   - Valid and invalid input conditions.
   - Exhaustive testing and why it is impractical.
   - Path explosion and the limits of test coverage.
3. **Failure-related terminology**
   - Mistake, error, bug, fault, defect, and failure as used in this chapter.
   - Fault activation and the relationship between a fault and zero, one, or several observed failures.
   - Check the source wording before treating these terms as a universal taxonomy.
4. **Test artifacts**
   - Test, test case, test suite, test data, expected result, and test-case template.
5. **Verification and validation**
   - Verification against specifications.
   - Validation against intended customer or user needs.
   - Behavioral specification as an input to validation.
6. **Acceptance-related testing**
   - Acceptance testing, alpha testing, and beta testing.
   - Participants, test site, and operating environment.
   - Keep the deck's distinctions separate; do not merge them with another book's terminology without a demonstrated need.

**Deck anchors:** PDF/deck pp. 2–12; acceptance and validation also pp. 170–179. Related MCQs: 8.1–8.3, 8.11, 8.14–8.23, 8.42–8.45, 8.50. Related exercises: 8.1–8.12, 8.38–8.39.

## B. Functional / black-box test design — predictive, explicit teaching

1. **Functional, behavioral, or black-box testing**
   - Input domain, output domain, and externally visible behavior.
2. **Boundary Value Analysis (BVA)**
   - Minimum, near-minimum, nominal, near-maximum, and maximum values.
   - Single-fault assumption and test-case count for n variables.
3. **Robustness testing**
   - Add values just outside valid boundaries.
   - Count and relation to ordinary BVA.
4. **Worst-case testing**
   - Combinations of extreme values across variables.
   - Growth in test count and contrast with ad hoc selection.
5. **Equivalence-class partitioning**
   - Valid and invalid input classes and representative values.
   - Output-domain classes where relevant.
   - Limits when combinations of input conditions matter.
6. **Decision-table testing**
   - Conditions, actions, rules, entries, condition stubs, and action stubs.
   - Deriving test cases from combinations of conditions.
7. **Cause-effect graphing**
   - Causes, effects, Boolean relations, and constraints.
   - Conversion to a limited-entry decision table and then test cases.
   - Constraint symbols are visually ambiguous in text extraction; inspect the original image before typesetting them.
8. **Repeated source examples**
   - Quadratic roots, previous-date/calendar, triangle, largest number, grading, and admission-rule programs.
   - Treat each as an example domain, not a separate vocabulary item unless the instructor includes it.

**Deck anchors:** PDF/deck pp. 13–103. Related MCQs: 8.3–8.6, 8.10, 8.12–8.13, 8.25–8.28, 8.47. Related exercises: 8.10, 8.12–8.26, 8.48–8.49.

## C. Structural / white-box testing and paths — predictive, explicit teaching

1. **Structural / white-box testing**
   - Internal control structure as the basis for test selection.
   - Contrast with functional / black-box testing.
2. **Flow graphs**
   - Nodes, edges, control flow, and construction from a program fragment.
3. **DD-path graphs**
   - Decision-to-decision paths, reduction, and node/path mapping.
4. **Independent paths and path coverage**
   - Meaning of an independent path.
   - Selecting paths and limits of claiming near-complete path coverage.
5. **Cyclomatic complexity**
   - V(G), edges E, nodes N, and connected components P.
   - The three source methods: E − N + 2P, predicate nodes + 1, and graph regions.
   - The predicate-node shortcut assumes two outgoing edges per predicate node.
6. **Graph and connection matrices**
   - Matrix dimensions and node correspondence.
   - Matrix entries and how powers relate to paths.
7. **Data-flow testing**
   - Definitions and uses; DEF and USE nodes.
   - Predicate use and computation use.
   - Definition-use (du) and definition-clear (dc) paths.
   - Data-flow anomalies and the source procedure for selecting paths.
   - Data-flow testing is not data-flow-diagram testing.
8. **Mutation testing**
   - Mutants, altered statements, test data, killed/live/equivalent mutants, and adequacy.
   - Verify exact source terminology and any score formula from the page image before use.

**Deck anchors:** PDF/deck pp. 104–169. Related MCQs: 8.8–8.9, 8.29–8.39. Related exercises: 8.16, 8.19, 8.27–8.37.

## D. Testing levels and integration — predictive, explicit teaching

1. **Unit testing**
   - Isolating a module and supporting it with test scaffolding.
   - Drivers and stubs.
2. **Integration testing**
   - Testing interactions and interfaces while combining modules.
   - Top-down, bottom-up, and sandwich approaches.
3. **System testing**
   - Whole-system testing and operational attributes such as usability, security, compatibility, dependability, and documentation.
4. **Validation testing**
   - Testing the integrated product against user/customer expectations.
   - Link to acceptance, alpha, and beta testing.
5. **Thread testing**
   - Appears in MCQ 8.49, but the main teaching body does not explain it. Keep it question-only until confirmed by the instructor or supported by a verified gap source.

**Deck anchors:** PDF/deck pp. 170–179; MCQs 8.24, 8.40, 8.43, 8.46, 8.48–8.50; exercises 8.40–8.44.

## E. Debugging — predictive, explicit teaching

1. **Debugging**
   - Tracing an observed failure symptom to a cause and location.
   - Why symptoms can differ from causes and why failures can be hard to reproduce.
2. **Inductive debugging**
   - Gather and organize observations, form a hypothesis, and test it.
3. **Deductive debugging**
   - Enumerate possible causes, eliminate/refine them, and prove the remaining hypothesis.
   - The deck's Figure 33 caption appears mislabeled; see the diagram atlas and source-issue register.

**Deck anchors:** PDF/deck pp. 180–185; MCQ 8.41; exercises 8.45–8.47.

## F. Testing tools — predictive, explicit teaching

- Static analyzers.
- Code inspectors.
- Standards enforcers.
- Coverage analyzers.
- Output comparators.
- Test-data generators.
- Test harnesses.
- Test-archiving systems.
- Static versus dynamic analysis as the deck presents it.

**Deck anchors:** PDF/deck pp. 186–188; related scaffolding material pp. 171–173 and exercise 8.44.

## G. Terms that appear mainly in questions or exercises — predictive, lower confidence

- Regression testing and development testing versus regression testing: MCQ 8.7 and exercise 8.5(ii).
- Extensive test planning and test-case-design objectives/steps: exercises 8.22–8.23.
- Tester psychology and failure after testing: exercises 8.38–8.39.
- Mixed testing strategies and optional random testing: exercise 8.48.
- Thread testing: MCQ 8.49 only.
- Practical test-reporting and table reference: exercise 8.44; inspect its “Table 8” reference.
- Four-generation-language testing costs: exercise 8.50.

These are not described to the same depth as the main teaching sections. Keep the distinction when deciding answer length.

## H. Supporting-book candidates — predictive expansion only

Do not turn these into required scope unless the instructor's list includes them or the primary course material has a demonstrated gap that matters to a listed term.

- Test-driven development (TDD): Sommerville 9e, §8.2, printed pp. 221–223.
- Testability: Pressman 5e, §17.1.3, pp. 440–441; Mall 4e, §10.4, pp. 405–412.
- Condition and loop testing: Pressman 5e, §§17.5.1 and 17.5.3, pp. 454–455 and 458–459.
- Multiple-condition coverage: Mall 4e, §10.7.4, p. 420.
- Static/dynamic program-analysis tools: Mall 4e, §§10.9.1–10.9.2, pp. 428–429.
- Regression and smoke testing: Pressman 5e, §§18.4.3–18.4.4, pp. 491–493; Mall 4e, §§10.12–10.13, pp. 435–440.
- Performance and stress testing: Sommerville 9e, §8.3.3, p. 227; Pressman 5e, §§18.6.3–18.6.4, pp. 498–499; Leach 2e, §6.12, pp. 300–301.
- Test scripts, harnesses, and plans: Leach 2e, §6.8, pp. 288–290.
- Error seeding and object-oriented/grey-box testing: Mall 4e, §§10.11–10.12, pp. 432–439.

## Status and conversion rule

- Current state: predictive candidate list based on the course deck and a targeted support-book scan.
- The instructor's actual V8 list has not been supplied.
- When it arrives, create a separately attributed instructor-scope record and mark each prediction as confirmed, outside scope, or unresolved. Do not rename this file as an instructor list or silently promote a prediction to confirmed scope.
- The original scanned textbook's Chapter 8 boundary and page-by-page comparison are still open. Do not attach printed-book page claims to a term until the actual spread is checked.
