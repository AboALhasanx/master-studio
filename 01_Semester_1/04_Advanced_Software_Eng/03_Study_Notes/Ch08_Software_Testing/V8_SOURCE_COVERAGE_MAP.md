# ASE Chapter 8 — Predictive Source and Coverage Map

> **Scope status:** predictive pending the instructor's actual Chapter 8 term list. This map locates likely topic coverage; it does not prove that final question packs cover the instructor's scope.

## Primary course-source map

| Candidate topic group | Canonical deck pages | Presence | Notes for later verification |
|---|---:|---|---|
| Testing purpose, limits, terminology, V&V, acceptance | 2–12 | Explicit teaching | Check source uses of mistake/error/bug/fault/defect/failure before giving a universal taxonomy. |
| Black-box overview and domains | 13 | Explicit teaching | Distinguish behavior/function testing from structural testing. |
| BVA, robustness, worst-case | 14–60 | Explicit teaching and worked examples | Verify formulas and superscripts visually. |
| Equivalence classes | 61–76 | Explicit teaching and examples | Input and output classes; inspect repeated O1 labels in source figures. |
| Decision tables | 77–91 | Explicit teaching and examples | Conditions/actions/rules, table parts, and test-case derivation. |
| Cause-effect graphs | 92–103 | Explicit teaching and examples | Inspect constraint symbols and the triangle conditions in the page image. |
| Flow graphs, DD paths, independent paths | 104–131 | Explicit teaching and worked examples | Several diagrams are low-resolution embedded rasters. |
| Cyclomatic complexity | 132–146 | Explicit teaching and worked calculations | Three methods; predicate-node shortcut requires two outgoing edges. |
| Graph and connection matrices | 147–154 | Explicit teaching and examples | Verified against scan §8.4.3, printed pp. 427–429, and rendered deck pages; matrix dimensions, labels, connection counts, and A²/A³ examples inspected. |
| Data-flow testing | 155–166 | Explicit teaching and examples | Verified against scan §8.4.4, printed pp. 430–434; DEF/USE, p-use/c-use, du/dc paths, anomaly patterns, and quadratic/triangle worked examples inspected. Distinguish the course's loose du-path from definition-clear DU chains in support texts. |
| Mutation testing | 167–169 | Explicit teaching, short section | Verified against scanned text §8.4.5, printed pp. 434–435: mutant, mutation operator, first-/second-order mutation, reachability, killed/live/equivalent mutants, mutation score, and test-suite-size caveat. The course source does not state the competent-programmer or coupling-effect hypotheses. |
| Unit/integration/system/validation | 170–182 | Explicit teaching | Unit testing is slides171–173; original Fig.29 on slide173. Integration §8.5.2 covers pp.437–439 and slides174–175; original Fig.30 is slide175. System testing §8.5.3 is pp.439–440 and slides176–177, with the five-attribute checklist in original Fig.31 on slide177. |
| Debugging | 180–185 | Explicit teaching | Figure 33 caption conflicts with its deductive steps. |
| Testing tools | 186–188 | Explicit teaching | Static/dynamic tools and their named categories. |
| MCQs | 189–200 | Question bank | 50 items; no publisher key located; page order is not always numeric. |
| Written exercises | 201–212 | Question bank | 50 items; no solutions in the deck; page 203 has a malformed extracted year predicate. |

## Scanned book status

- Candidate book file: Reference_Textbooks/AliFahim_Software_Engineering.pdf.
- Likely identity: K.K. Aggarwal and Yogesh Singh, Software Engineering, 3rd edition; the scan lacks its title/author page, so record the identity as high-confidence but inferred.
- Prior chapter boundary note places printed p. 365 at the beginning of Chapter 8. The Chapter 7 endpoint is printed p. 364.
- **The direct locators verified so far include §8.4.3, printed pp. 427–429; §8.4.4, pp. 430–434; and §8.4.5, pp. 434–435.** Other topic locators and full book-versus-deck differences remain open; do not infer their page anchors from these verified sections.

## Supporting-book candidates for predictive gaps

These are targeted candidate pages. They are not required scope until a real instructor term or a demonstrated explanation gap calls for them.

| Topic candidate | Best initial source | Printed-page anchor | PDF-page anchor for local retrieval | Use limit |
|---|---|---:|---:|---|
| Mutation testing | Mall 4e, §10.7.8 | 426–427 | 573–574 | Direct support for mutation operators, equivalent/dead/live mutants, automation, and computational cost; no competent-programmer or coupling-effect hypotheses found. |
| TDD | Sommerville 9e, §8.2 | 221–223 | 238–240 | Candidate only; not taught as a main deck section. |
| Performance and user testing context | Sommerville 9e, §§8.3.3–8.4 | 227–230 | 244–247 | Alpha/beta/acceptance overlap may already be adequate in deck. |
| Testability | Pressman 5e, §17.1.3 | 440–441 | 468–469 | Add only if a listed term needs a clear definition. |
| Condition testing | Pressman 5e, §17.5.1 | 454–455 | 482–483 | Targeted structural-coverage gap. |
| Loop testing | Pressman 5e, §17.5.3 | 458–459 | 486–487 | Targeted structural-coverage gap. |
| Regression and smoke testing | Pressman 5e, §§18.4.3–18.4.4 | 491–493 | 519–521 | Regression also appears in the deck question bank. |

## Completed supporting-book audit — Unit Testing

| Book | Verified printed locator | Direct contribution / limit |
|---|---|---|
| Pressman 5e | §§18.3–18.3.2, pp. 485–487 | Unit scope, five unit-test concerns, test-case sequence, driver/stub roles and overhead, parallel work, and cohesion/testability. |
| Mall 4e | §10.5, p. 413 | Module preparation and test environment, called procedures/non-local data, and the interface/behavior of stubs and drivers. |
| Sommerville 9e | §8.1, pp. 211–213 | Units as program units/classes, method tests, setup/call/assert structure, automation, and mock objects; not the course's classic driver/stub definition. |
| Leach 2e | §§6.1–6.3, pp. 269–276; §6.8, pp. 288–289 | Module black-/white-box context, finite-test limits, test scripts/harnesses/planning; no distinct classic driver/stub definition in these sections. |

## Completed supporting-book audit — Integration Testing

| Book | Verified printed locator | Direct contribution / limit |
|---|---|---|
| Pressman 5e | §18.4, pp.488–494 | Interface failures, incremental construction, top-down/bottom-up, regression and smoke testing, integration documentation. |
| Mall 4e | §§10.10–10.10.1, pp.430–431 | Dependency-graph planning, big-bang/top-down/bottom-up/sandwich, driver/stub needs, and phased versus incremental integration. |
| Sommerville 9e | §8.1.3, pp.216–218 | Component-interface testing; parameter, shared-memory, procedural, and message-passing interfaces; misuse, misunderstanding, and timing faults; limits of integration evidence. |
| Leach 2e | §6.9, pp.290–296 | Big-bang, bottom-up, top-down, stubs/drivers/mocks, and architecture-dependent trade-offs. |

## Completed supporting-book audit — System Testing

| Book | Verified printed locator | Direct contribution / limit |
|---|---|---|
| Pressman 5e | §18.6, pp.496–498 | System-level exercise of the integrated computer-based system; recovery, security, stress, and performance testing; fault-handling/interface evidence. |
| Mall 4e | §§10.12–10.12.2, pp.435–437 | SRS-based functionality and performance testing; smoke, stress, volume, configuration, compatibility, recovery, usability, documentation, and security examples. Alpha/beta/acceptance are excluded from this term because the next term covers validation/acceptance. |
| Sommerville 9e | §8.1.4, pp.219–220 | Complete-system tests for compatibility, interactions, data transfer, and emergent behaviour; distinguishes system-level effects from component checks. |
| Leach 2e | §6.12, pp.300–301 | Performance profiling and stress beyond expected workload, with emphasis on graceful handling rather than dropped or lost work; not a full system-test taxonomy. |
| Stress/performance testing | Pressman 5e, §§18.6.3–18.6.4 | 498–499 | 526–527 | Do not add both books if one source is enough. |
| Testability and test-case rationale | Mall 4e, §10.4 | 405–412 | 553–560 | Compact cross-check; choose one source per term. |
| Multiple-condition coverage | Mall 4e, §10.7.4 | 420 | 568 | Candidate depth beyond the deck's primary named methods. |
| Static/dynamic program-analysis tools | Mall 4e, §§10.9.1–10.9.2 | 428–429 | 576–577 | Compare terminology with the deck's tools section. |
| OO/grey-box, smoke, performance, error seeding | Mall 4e, §§10.11–10.12.3 | 432–439 | 580–587 | Use only for a confirmed instructor term. |
| Regression/testing documentation | Mall 4e, §10.13 | 439–440 | 587–588 | Candidate only. |
| Test scripts, harnesses, and plans | Leach 2e, §6.8 | 288–290 | 316–318 | Deck already has test harnesses/scaffolding, but plans/scripts may be a gap. |
| Performance/stress testing | Leach 2e, §6.12 | 300–301 | 328–329 | Candidate alternative; avoid duplicate expansion. |
| Managerial testing practices/tools | Leach 2e, §6.15 | 305–307 | 333–335 | The tool list is in §6.15, not §6.14. |

### Mutation-testing source-audit note

- Pressman 5e was searched in full. §23.4.3 discusses fault-based testing for object-oriented classes, but no direct mutant-generation, equivalent-mutant, or mutation-score treatment was found; do not present it as a mutation-testing chapter source.
- Sommerville 9e and Leach 2e were searched in full; no direct mutation-testing treatment was found. Leach has an index-level “fault seeding” entry, which is not a mutation-testing method explanation.
- The local Mall source §10.7.8, printed pp. 426–427, supports the operator/mutant lifecycle, equivalent/dead/live mutants, automation, and computational cost. Its treatment does not give the course's mutation-score formula or name the two hypotheses.
- For the predictive vocabulary's Competent Programmer and Coupling Effect hypotheses, the verified foundational source is [DeMillo, Lipton, and Sayward, “Hints on Test Data Selection: Help for the Practicing Programmer,” IEEE Computer, 1978](https://doi.org/10.1109/C-M.1978.218136). Treat both as theoretical assumptions, not guarantees. A recent empirical study reports that the hypothesis's evidence remains qualified and that generic operators may miss representative real faults: [Ahmed et al., “A New Perspective on the Competent Programmer Hypothesis Through the Reproduction of Real Faults with Repeated Mutations,” Software Testing, Verification and Reliability, 2024](https://doi.org/10.1002/stvr.1874).

## Question-bank and seminar handling

- The publisher companion deck's 50 MCQs and 50 exercises are the primary question inventory; neither includes a publisher answer key or worked solutions.
- Three local external question banks contain generic overlapping test prompts. Keep any selected pages tagged as practice patterns only, with no authority over answers, course scope, or marks.
- Do not include the student seminar PDF in the current source collection. It is a separate later task.

## Confidence legend

- **Explicit teaching:** topic appears in the main body with explanation or examples.
- **Question-only:** appears in an MCQ or exercise but is not developed in the teaching body.
- **Support candidate:** found in a named supporting book and not yet confirmed in instructor scope.
- **Open:** needs source-image or scan-boundary inspection.



### Completed supporting-book audit — Validation testing and customer-involvement paths

| Source | Verified locator | Direct contribution and scope limit |
|---|---|---|
| Aggarwal & Singh course scan and canonical companion deck | §8.6, printed pp.440–441; slides178–179 (PDF pages178–179) | Primary authority. Validation follows unit and integration testing and examines the complete product from the customer perspective against expected needs and the SRS validation-criteria section. The scan notes that real usage is difficult to predict and that users may try unusual inputs/combinations or misunderstand results; customer involvement can expose these blind spots. It presents acceptance, alpha, and beta as ways of involving customers. The scan distinguishes alpha at the developer site under developer guidance in a controlled environment, beta at customer sites in a real environment without developer control, and acceptance for customized software against customer expectations. It also discusses an IEEE V&V guide for planning/documentation and project-specific quality attributes. Do not mistake this broad validation purpose for only an end-of-contract acceptance decision. |
| Pressman 5e | §18.5–§18.5.3, printed pp.495–497 | Directly supports validation at the requirements level, the SRS validation criteria, black-box demonstration, separate test-plan/test-procedure roles, requirement classes, deficiencies and customer negotiation, configuration review, custom-software acceptance, and alpha/beta distinctions. Its alpha/beta descriptions align substantially with the course scan. |
| Mall 4e | §10.12, printed pp.435–437 | Direct system-test context: cases derived solely from SRS, functionality versus performance, and participant-based classifications. Its terminology differs: alpha = test team inside the development organization; beta = selected friendly customers; acceptance = customer deciding whether to accept delivery. It says the same test cases may be used, while case design and execution participants differ. Preserve this as an explicit source variation rather than silently merging it with the course definition. |
| Sommerville 9e | §§8.3–8.4, printed pp.224–230 | Adds a useful separation between release testing (independent team; requirement validation rather than defect discovery) and user testing. Describes realistic-environment limits, user testing types, beta as an early release tried by users, and a six-stage acceptance process from criteria through decision. Adds negotiation and conditional acceptance realities. Its XP usage calls an embedded user an alpha tester and treats automated story-acceptance tests as part of development; explicitly identify this as an Agile context if mentioned, not as a replacement for the course's alpha/beta definitions. Figure 8.11 is an original acceptance-process diagram already reproduced earlier in this seminar; cross-reference it rather than duplicate it. |
| Leach 2e | §6.15, printed pp.305–307 | Inspected as adjacent management/testing-process context: QA-team practice, planning and metrics, and regression/testing resources. It does not directly define validation, acceptance, alpha, or beta testing; do not use it to define these terms or force a citation into this item. |

**Pre-authoring outline for seminar item 25:** (1) connect the course's one-sentence validation definition to its operational meaning, distinguishing testing level/system test from the customer-oriented purpose of validation; (2) derive checkable criteria from user-visible SRS entries while recording the difference between requirement conformance and real-world suitability; (3) explain why usage profiles and unusual combinations matter without replacing representative use with exotic-only cases; (4) develop the acceptance path through criteria, planning, test derivation, execution, deficiency negotiation, and accept/reject/conditional decision, cross-referencing existing Figure1.4; (5) compare course-defined alpha, beta, and acceptance by product context, participant, site, developer control, and decision purpose, and transparently note Mall/Sommerville terminology variants; (6) work a distinct illustrative case with a criteria-to-test-to-evidence-to-decision matrix; (7) finish with a validation record/checklist and limits of inference. Sections 5–6 already introduce V&V and acceptance; this term must add process detail and source reconciliation rather than repeat those introductory definitions. Preserve the requested no-inline-source-links style in Word prose.


## Completed seminar audit — Validation testing and customer-involvement paths

Item 25 has been authored in the Word seminar and rendered through COM to **132 total pages**. It occupies pages **127–132**. The final PDF passed the Office export QA gate; pages127–132 were visually reviewed, including the repeated header and split of Table25.3, the existing acceptance-flow figure cross-reference, the criteria/evidence matrices, and the last-page checklist. A redundant concluding paragraph was removed after the first review stranded it on a near-empty page; the final version ends cleanly on page132. No inline source links were added to the Word body.

The term adds operational validation criteria, the distinction between requirement conformance/user suitability/customer delivery decision, test plan versus procedure, user-context case selection, course-defined alpha/beta/acceptance, and a worked registration-service trace. It attributes source-term variation and explicitly limits Leach’s adjacent managerial/QA contribution. This avoids simply repeating introductory §§5–6.


### Completed source audit and pre-authoring plan — Debugging, induction, deduction

| Source | Verified locator | Direct contribution and limit |
|---|---|---|
| Aggarwal & Singh course scan and canonical companion deck | §8.7–§8.7.3, printed pp.441–446; slides180–185; scan spreads226–229 | Primary authority. Testing yields symptoms; debugging investigates their cause/location. The scan lists eight symptom clues, compares core dumps/traces/print statements/debugging programs, and discusses trial-and-error, backward tracking/backtracking, forward tracking, binary partition, watch points, induction, and deduction. It details four induction and four deduction steps. Scan p.446 labels Fig.8.33 “deductive”; companion slide185’s caption says “inductive,” though the diagram itself is deductive. The scan resolves the deck-caption inconsistency. Preserve source figures32–33 and correct the figure33 seminar caption with a note explaining the mismatch. |
| Pressman 5e | §§18.7.1–18.7.3, printed pp.499–502 | Strong direct support: debugging follows testing and matches symptoms to causes; eight bug clues; brute force, backtracking, and cause elimination; cause elimination uses inductive or deductive hypotheses; tools, fresh review, iterative evidence, and checks that a fix has not introduced/repeated faults. Its taxonomy is related but not identical to the course’s list of trial/error, backtracking, forward tracking, binary partition, induction, and deduction; keep the course sequence authoritative and identify the Pressman categories as a supporting lens. |
| Mall 4e | Chapter10 summary, PDF p591; Exercise93, PDF p594 (printed folio is not legible in this converted copy) | The summary distinguishes code review (identifies errors) from testing (identifies failures) and says debugging locates/fixes the errors after failures. Exercise93 asks about symbolic debuggers and other techniques. This is context/question support only; no teaching exposition of the course’s induction/deduction procedures was located. |
| Sommerville 9e | §8.1.1, printed p.211; supporting mention in §8.2, p.223 | Defines debugging as fixing problems discovered through testing, using language knowledge and intended outcomes, often with interactive execution tools. Development testing and debugging are interleaved. TDD can make a failed change easier to localise, but this is a specific workflow benefit, not a general inductive/deductive taxonomy. |
| Leach 2e | Testing chapter §6, targeted review of §§6.1, 6.8, 6.12, 6.15 | These sections address testing, harnesses/planning, performance, and QA/manager practice; no direct inductive/deductive debugging procedure was located. It will not be forced into the technical explanation. |

**Pre-authoring outline for seminar item26:** (1) delimit testing, observed failure/symptom, root cause, correction, and regression evidence; cross-reference the early overview instead of repeating it; (2) organize the course’s eight symptom clues into diagnostic risks without flattening the original list; (3) explain the source’s four common techniques and the limits of brute force/backtracking/forward tracking/binary search/watch points; (4) reproduce original Fig.8.32 and Fig.8.33, treating the scan’s deductive label for Fig.8.33 as controlling and documenting the companion-slide caption error; (5) work the four inductive stages (collect/location, organize, relate, hypothesize/prove) and the four deductive stages (enumerate, eliminate, refine, prove), including loops when evidence is insufficient; (6) apply both methods to a distinct reproducible incident using competing hypotheses and observations; (7) cover tools as aids, careful fix review, test-case reproduction, and regression while reserving the dedicated tool taxonomy for its own later item; (8) end with a diagnosis record and concise checklist. Existing §1.1.7 only introduces the process; item26 must add the methodological depth.


## Completed seminar audit — Debugging and its reasoning approaches

Item26 has been authored and rendered to **139 total pages**; item26 occupies pages **133–139**. The final Word COM export passed the PDF QA gate. All seven final pages were visually reviewed before the final pagination adjustment; the final revised last page139 was rechecked. The tables and figures are legible; the original Fig.8.32 induction image and Fig.8.33 deduction image are included, the caption error on slide185 is explicitly corrected, and the diagnosis record closes the item on page139 without a stranded continuation. The table on practical debugging techniques repeats its header after the split. No inline source links were added to the Word body.

The support-source mapping preserves scope: Pressman supplies a related but non-identical debugging taxonomy; Mall offers only a chapter-summary distinction and question prompt; Sommerville provides a definition/tool context and TDD-specific observation; Leach yielded no direct induction/deduction method and is not forced into the prose. Next explicit teaching group: Testing Tools (static/dynamic distinction and named tools); the single-question Thread Testing candidate remains unconfirmed and question-only.


### Completed source audit and pre-authoring plan — Testing tools

| Source | Verified locator | Direct contribution and limit |
|---|---|---|
| Aggarwal & Singh course scan and canonical companion deck | §8.8–§8.8.2, printed pp.447–449; slides186–188; scan spreads229–230 | Primary catalogue: static/dynamic categories; static analyzers, code inspectors, standards enforcers, and source-formatting/generation utilities; dynamic coverage analyzers, output comparators, test-file/data generators, test harnesses, test-archiving systems. The dynamic support-tool workflow includes input setting, stub processing, results display, coverage measurement, and test planning. It warns that automatic data generation faces long/nonlinear/illegal path constraints, while derived data from near paths can be practical. The scan’s “85–90% CI coverage” statement is historical and must not be presented as a universal modern threshold or proof of correctness. |
| Pressman 5e | §17.6.4, printed pp.465–466; adjacent §18.7.3, pp.501–502 | Comparison testing gives a concrete output-comparison use: independent redundant versions run on the same data and outputs are checked for agreement. The debugging section lists dumps, traces, debugging aids, automatic test-case generators, and cross-reference maps. Pressman does not supply a full catalogue matching the course’s eight tools; use only for these narrow examples. |
| Mall 4e | §10.9.1–§10.9.2, printed pp.428–429 | Direct static/dynamic program-analysis distinction. Static tools analyse source without execution, check coding standards and certain programming faults, and cannot access runtime pointer/dynamic-memory behaviour. Dynamic tools collect instrumented execution traces, compute statement/branch/path coverage, report results, and can guide added or redundant test-case selection. Coverage is evidence about exercised structure, not proof of requirement correctness. |
| Sommerville 9e | §8.1, printed pp.210–212 | Adds practical automation framing: manual tests compare observed results with expectations; encoded tests can rerun quickly, especially for regression; unit-test frameworks such as JUnit provide generic classes and pass/fail reporting. Automation has limits where visual appearance or absence of unwanted side effects requires human judgement. Do not imply the named framework is universally appropriate. |
| Leach 2e | §6.15, printed pp.305–306; §6.16 p.307 | The manager’s minimum tool list includes test drivers, stub generators, test harnesses, test-data management, regression testers, path analyzers, and static analyzers; fault-injection tools are additionally useful for suitable systems. The adjacent Agile case reports automated tests run in harnesses and experience-related process observations. This is a pragmatic management list, not a formal static/dynamic taxonomy. |

**Pre-authoring outline for seminar item27:** (1) distinguish source inspection from execution-based evidence and note hybrid/overlapping tools; (2) explain static analyzer, code inspector, and standards enforcer without treating warnings as confirmed defects; (3) explain dynamic coverage analyzers with instrumentation overhead and limits of percentages, especially the scan’s historical 85–90% statement; (4) explain output comparators and the need for a trustworthy expected-result oracle and tolerances; (5) distinguish test-file generation from data generation and explain constraint/search limits; (6) detail harness functions—input setup, stubs, run control, result display, coverage, planning—and distinguish a harness from a test case or archive; (7) explain test archives as reproducible evidence with build/data/environment identity; (8) work an illustrative invoice-processing harness and map each need to a tool, output, and human review; (9) close with selection criteria and an evidence checklist. Avoid recommending current commercial products; this term concerns source categories and functions. No authoring yet.


## Completed seminar audit — Software Testing Tools

Item27 has been authored and exported through Office COM; the final seminar renders to **144 pages**, with item27 on pages **140–144**. The PDF QA gate passed and all five final pages were visually reviewed. The static-tools table remains together, the test-harness table stays intact, the dynamic tool taxonomy and worked invoice chain are legible, and the earlier single-word/sentence splits and near-empty continuation page were removed by tightening redundant text. The final page ends with the selection/interpretation conclusion; it has no orphan checklist page. The course’s historical 85–90% coverage statement is explicitly disclaimed as a universal threshold. No inline source links appear in the Word prose.

The item uses the course taxonomy, Mall’s static/dynamic analysis, Sommerville’s test-framework and automation limits, Leach’s practical manager tool set, and Pressman’s narrow comparator example with explicit scope boundaries. It differentiates test files from generated values, harnesses from test cases/drivers/stubs, and archives from correctness guarantees.


### Completed source audit and pre-authoring plan — Regression testing

| Source | Verified locator | Direct contribution and limit |
|---|---|---|
| Aggarwal & Singh course scan/deck and publisher questions | §8.5.3, printed p.440 (scan spread226); exercise8.5(ii); MCQ8.7 on slide190, publisher answer key p.499 | The main teaching text says after modifying an existing product, established capabilities on which users rely should be tested as well as new ones, but does not give a named regression-test process. Exercise8.5(ii) asks students to distinguish development and regression testing. Publisher MCQ8.7 keys regression testing to “maintenance testing”; the item has no explanatory teaching slide. Preserve the keyed answer for the question, while explaining the broader cross-phase usage evidenced by the supporting books. |
| Pressman 5e | §18.4.3, printed pp.491–492; §18.4.5 p.493 | Defines regression in integration as rerunning a subset of completed tests after change to detect unintended side effects, then generalizes to changes made after any testing/correction. Gives manual versus capture/playback execution and a three-part suite (representative function sample, likely-affected functions, changed components); warns that rerunning everything after every change becomes impractical. Critical-module focus appears in §18.4.5. |
| Mall 4e | §10.13, printed p.440 | Explicitly states regression spans unit, integration, and system testing and is a separate dimension rather than a fourth level. Reruns an old suite after change or bug fix; impact selection may avoid a full rerun when only a small change is made. Also gives the test-summary-report fields immediately before the regression discussion. |
| Sommerville 9e | §8.2, printed p.223 | Defines regression as rerunning previously successful test sets after changes to check old behaviour and new interactions. Manual regression can be prohibitively costly; automated TDD suites reduce rerun cost, but the claim is specific to that workflow and has limits with legacy systems and nondeterministic threaded behaviour. |
| Leach 2e | §6.15, printed pp.305–306; §6.16 p.307 | Management requires regression checks during iterative testing/integration and uses metrics to find troublesome modules. The chapter also describes harness-based automation in Agile. It is process support, not a detailed regression-selection algorithm. |

**Pre-authoring outline for seminar item28:** (1) distinguish development testing, maintenance testing, and regression as testing purpose/timing versus a cross-level change-checking activity; preserve the official MCQ key’s maintenance label with its limitation; (2) explain how changes can affect previously passing behaviour through control, data, interface, or configuration dependencies; (3) compare new-feature tests and regression tests; (4) derive Pressman’s representative, likely-affected, and changed-component suite classes, with risk/impact selection and why exhaustive reruns are costly; (5) describe a controlled change→impact analysis→suite selection→execution/comparison→failure diagnosis→suite update workflow; (6) explain automated capture/playback and TDD suites without claiming automation removes oracle, flaky-test, or maintenance problems; (7) work an illustrative payroll-rounding change with explicit retained-behaviour cases; (8) close with records, limits, and the exam distinction. Existing §§23, 24, 26 mention regression in passing; item28 should explain the strategy rather than restate those mentions. Item28 is now authored, Word-rendered, visually reviewed, and documented in the completion record below.


### Completed seminar item28 — Regression Testing

The seminar now contains **28. Regression Testing and Change Verification**, rendered on pages **145–149** in the 149-page Word document after the TOC update. The section distinguishes development, maintenance, and regression; explains why previously passing behaviour is retested; derives a selected suite from representative, likely-affected, and changed-component cases; provides a six-step evidence workflow; discusses capture/playback, automated suites, flaky tests, and suite maintenance; works a payroll-rounding change; distinguishes regression at unit, integration, and system levels; and closes with reporting fields and limits. The publisher key associating regression with maintenance is preserved as the answer to that keyed MCQ while the four supporting sources support broader cross-phase usage. All five final pages were visually reviewed after Word COM rendering. The initially orphaned reporting conclusion was consolidated and a cross-level table added; the final page ends cleanly. The Word TOC was updated and now lists item28 at p.145. No inline source links were added to the Word body.

## Candidate item29 — Test planning and test-case design audit

**Decision:** Include one integrated seminar item, while keeping its scope on planning and the design/documentation lifecycle. The course exercises explicitly ask why testing needs planning and what test-case design means, what its objectives are, and which steps it involves. Existing item4 already defines test/test-case/test-suite/test-harness artifacts, while items7–19 teach the concrete black-box and structural selection techniques. Item29 should therefore explain how a project turns a testing objective into an organized, traceable, executable and reviewable body of evidence; it should refer back to the earlier techniques rather than re-teach them.

| Source | Verified locator | Contribution and limit |
|---|---|---|
| Aggarwal & Singh course scan and canonical companion deck | §8.1.4, printed pp.368–369; slides13–15; exercises 8.22–8.23 on companion slide206 | Primary course source. §8.1.4 defines testing artifacts and the test case's input/execution-condition/expected-result role; the companion questions establish that planning rationale and test-case-design objectives/steps are examinable prompts. They do not provide worked answers to exercises 8.22–8.23 or a complete planning workflow. Keep the generated T2 answer text out of the evidence base unless independently supported. The course scan/deck are treated as one source family. |
| Pressman 5e | §18.3–§18.3.2, printed pp.485–487; previously verified during item22 audit | Supports unit-level test-case sequences, the five check dimensions, expected results, driver/stub constraints, and testability/cohesion. This is a bounded case-design and execution-support contribution, not evidence for a universal project-wide planning template or a fixed testing-budget percentage. The book file is not currently available in the subject's Reference_Textbooks folder or Downloads for fresh visual recheck. |
| Mall 4e | §10.4, printed pp.405–412; previously mapped as testability/test-case rationale; also §10.10–§10.10.1, pp.430–431 for integration planning | Supports the relationship between observable/controllable software and effective test design; the integration sections show that planning can depend on module dependencies and the selected build-up strategy. Do not treat integration planning as the whole test plan. The book file is not currently available in the subject's Reference_Textbooks folder or Downloads for fresh visual recheck. |
| Sommerville 9e | §8.1, printed pp.209–210 (PDF pp.226–227) | Freshly rechecked against the local PDF and page image. Test planning schedules and allocates resources, defines the testing process in view of available staff/time, and identifies what is tested, the predicted schedule, and how results are recorded; critical-system plans may detail the tests. Figure8.3 models design cases → prepare data → execute → compare/report. A test case specifies inputs, expected results, and what is tested; test data are the concrete inputs. People who understand intended behaviour must define expected results, although execution/comparison can be automated. It does not prescribe one exhaustive case-design algorithm. |
| Leach 2e | §6.8, printed pp.288–290 (PDF pp.316–318); previously verified in the Chapter 8 source audit | Supports practical test scripts, harnesses, and planning resources. Use for repeatability and preparation needs only; do not attribute Sommerville's four-stage process or a universal case schema to Leach. The book file is not currently available in the subject's Reference_Textbooks folder or Downloads for fresh visual recheck. |

**Evidence and limits:** The five sources are not five interchangeable explanations. The course scan/deck supplies course scope and artifact terminology; Sommerville supplies the clearest explicit end-to-end process model; Pressman, Mall, and Leach provide previously verified supporting details with the bounds above. The three supporting PDFs are absent from the current local reference/download locations, so their prior verified locators are retained without claiming a fresh re-read in this session. Do not reuse the unsupported 30–50% cost figure, stage-gate criteria, fixed coverage targets, or generated six-step procedure from the existing T2 answer as source facts.

**Pre-authoring outline:** (1) explain why planning coordinates objectives, scope, people, time, environment, dependencies, records, risks, and decisions without inventing a fixed cost ratio; (2) distinguish a testing strategy/policy, project or level-specific test plan, test design/specification, procedure/script, data, run record, and summary; (3) show a plan skeleton with scope/exclusions, approach and referenced techniques, responsibilities/resources, schedule/dependencies, environment/data, entry/exit/decision conditions where project-defined, risks/contingencies, records and change control; (4) define a test case as an objective-linked specification with preconditions, controlled inputs, actions, expected results/oracle, and cleanup/postconditions as appropriate, separating logical case from concrete test data and execution script; (5) present a traceable design workflow from requirement/objective to oracle, selection technique, case set, review, data/procedure, execution and evidence; (6) use a worked student-registration example and a compact requirement-to-case matrix; (7) explain automation's useful boundary: run/compare/archive may be automated, but oracle adequacy, requirement interpretation, risk choice, and some visual/side-effect judgements need human ownership; (8) cross-reference prior BVA, equivalence, decision-table, path, unit and integration items rather than repeat them; (9) close with a plan-review and case-quality checklist and explicit limits of inference. Reproduce Sommerville Figure8.3 from the source PDF as the process model, with a new seminar figure number and a separate explanatory caption.

### Completed seminar item29 — Test Planning and Test-Case Design

Item29 is complete in the Word seminar. The final Word-rendered PDF has **154 pages**; item29 occupies pages **149–154**. The refreshed table of contents lists item29 at p.149, and the figure is listed in the front matter. The six item pages were visually reviewed: Sommerville Figure8.3 is clear and captioned as Figure29.1; tables retain readable text and repeated column headers across page breaks; the worked registration matrix, automation boundary, review checklist, and limits are legible; the last page ends with the complete conclusion. Front matter pages2–4 were checked after the TOC/figure-list adjustment. One optional repagination attempt to move a split table to the next page stalled before Word opened the document; that process was stopped, and the canonical DOCX remains the successfully rendered and reviewed 154-page version. No source links were added to seminar prose.

Coverage includes scope/resources/schedule/environment/risk/result planning; distinct strategy, plan, test specification, case, data, procedure, run record, and summary artifacts; a traceable objective-to-oracle-to-case workflow; a reproducible case record; a worked student-registration matrix; human ownership of expected-result adequacy alongside automation of repeatable execution; review/change control; and explicit limits. The five-source audit remains nuanced: course scan/deck establishes the prompts and artifact vocabulary; Sommerville provides the freshly verified workflow and figure; Pressman, Mall, and Leach are supporting prior-verified locators with the availability limits recorded above. The seminar is predictive pending instructor confirmation of the official vocabulary. Continue by auditing the next evidence-supported candidate before adding prose; thread testing remains MCQ-only absent stronger course evidence.

## Draft hold — Chapter 8 Software Testing Word seminar

On 2026-10-24 the student explicitly placed Chapter 8 on hold until Dr. Ali Fahim supplies the official vocabulary/notes. The current 154-page, 29-item Word file is a prepared predictive working draft, not a confirmed-scope final. See `03_Study_Notes/Ch08_Software_Testing/CH08_SEMINAR_DRAFT_STATUS.md` for exact artifact, resume steps, and the 80–90 pages as approximate guidance. Do not continue adding Chapter 8 terms until official vocabulary arrives; reconcile the existing sections first when it does.

## Next deliverable focus — Chapter 9 Software Maintenance seminar

Chapter 9 has a 42-page question-pack print volume and six pack PDFs/Markdown sources, but no dedicated Word seminar in `05_Seminars_&_Slides`. Its official instructor vocabulary/notes remain pending; current V9 scope is predictive. Before drafting the seminar, audit the Chapter 9 course source, source atlas, current packs and figures, and Chapter 7 Reliability Word style; prepare the source coverage plan first. The Chapter 9 question-pack print volume is not itself the seminar.
