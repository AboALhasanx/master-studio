# ASE Chapter 7 — V7 Instructor Vocabulary Coverage Ledger

> **Course:** Advanced Software Engineering (CS603) — Asst. Prof. Dr. Ali Fahim Ni'ma  
> **Source Material:** K.K. Aggarwal & Yogesh Singh, *Software Engineering* (3rd ed.), Chapter 7: Software Reliability (pp. 308–364 / official companion slides 1–126)  
> **Purpose:** Internal navigation ledger mapping the 19 instructor vocabulary leaves to live question-pack locations and source locators. These mappings were checked against current question stems and answers; they are not a claim that every answer has passed source verification.

**Reconciled 2026-11-11:** current pack pointers and superseded pre-correction warnings below were checked against the local Markdown. Codex's 2026-10-21 journal records the prior content/figure corrections and bounded visual review; this update does not repeat that source audit. Source locators remain inherited navigation aids, not newly recertified citations. This is an internal ledger with no separate PDF; use [00_INDEX.md](00_INDEX.md) for the six exported question packs and combined print file. Student final visual review remains pending.

---

### Leaf 01 · What is Software Reliability?
- **Syllabus Category:** Basic Concepts
- **Definition & Concepts:** Probability of failure-free software operation for a specified period of time in a specified environment. Dynamic operational existence vs hardware wear-out.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 7.2 & 7.48
  - `T2_Descriptive.md`: Question 7.1 (Exercise 7.1)
  - `T3_Compare_Analyze.md`: Comparison 7.2 (quality vs reliability)
- **Source Locators:**
  - Textbook (3rd ed.): §7.1 & §7.1.1, pp. 308–310
  - Companion Slides: Slides 6–8
- **Pack Mapping Status:** Direct definition and comparison coverage is present; source verification is a separate review.

---

### Leaf 02 · Software Reliability and Hardware Reliability
- **Syllabus Category:** Basic Concepts
- **Core Concepts:** Hardware physical wear-out and Bathtub curve vs software design defects, absence of physical wear-out, and maintenance-induced regression spikes.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 7.1 & 7.47
  - `T3_Compare_Analyze.md`: Comparison 7.1 (Exercise 7.3)
  - `T4_Diagrams.md`: Q7.V01 (Figs. 7.1 & 7.2)
  - `T5_Apply_Interpret.md`: Scenario 7.5
- **Source Locators:**
  - Textbook (3rd ed.): §7.1.1, pp. 308–310
  - Companion Slides: Slides 2–5, Figs. 7.1 & 7.2
- **Pack Mapping Status:** Direct comparison coverage is present. The current T4 answer distinguishes the hardware wear-out phase from the software curve's obsolescence phase. Prior figure/print review is recorded in the 2026-10-21 journal; no new visual audit is claimed here.

---

### Leaf 03 · Failures and Faults
- **Syllabus Category:** Basic Concepts
- **Core Concepts:** Failure as an observable dynamic runtime departure vs fault as a static internal defect. Time characterizations: time of failure, inter-arrival time, cumulative failures, and failure intensity.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 7.3, 7.4, 7.6, 7.30, 7.46
  - `T2_Descriptive.md`: Questions 7.2, 7.3, 7.4 (Exercises 7.4, 7.5, 7.6)
- **Source Locators:**
  - Textbook (3rd ed.): §7.1.2 & §7.1.3, pp. 310–314
  - Companion Slides: Slides 8–15
- **Pack Mapping Status:** Direct coverage is present. The terminology explanation in T1 Q7.3 should be checked separately for taxonomy accuracy.

---

### Leaf 04 · Environment
- **Syllabus Category:** Basic Concepts
- **Core Concepts:** Operational profile, input space, failure domain, and operational environment shift between testing and field use.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 7.2 & 7.52
  - `T2_Descriptive.md`: Questions 7.1 & 7.4
  - `T4_Diagrams.md`: Q7.V02 (input space/failure domain; Fig. 7.4)
  - `T5_Apply_Interpret.md`: Scenarios 7.1 & 7.3
- **Source Locators:**
  - Textbook (3rd ed.): §7.1.4 & §7.1.5, pp. 314–318
  - Companion Slides: Slides 16–20, Figs. 7.4–7.6
- **Pack Mapping Status:** Direct text/application coverage is present. The former visual warning is superseded by the current T4 wording: Q7.V02 explicitly says Fig. 7.4 does not mark a failure domain; Q7.V03 uses Fig. 7.5 as a probability portion, not a branching tree. This checks the corrected text/pointer, not a fresh source-image audit.

---

### Leaf 05 · Uses of Reliability Studies
- **Syllabus Category:** Basic Concepts
- **Core Concepts:** Release readiness certification, tracking testing progress, projecting resource/calendar requirements, monitoring operational performance.
- **Pack Locations:**
  - `T2_Descriptive.md`: Question 7.5 (Exercise 7.7)
  - `T5_Apply_Interpret.md`: Scenario 7.2 (release certification)
- **Source Locators:**
  - Textbook (3rd ed.): §7.1.8, pp. 320–322
  - Companion Slides: Slides 21–23, Fig. 7.7
- **Pack Mapping Status:** Direct coverage is present through the uses list and release-certification application.

---

### Leaf 06 · McCall Software Quality Model
- **Syllabus Category:** Software Quality
- **Core Concepts:** 11 product quality factors organized under 3 operational perspectives (Operation, Revision, Transition); the current T3/T4 answers use 25 quality criteria. The source-specific count correction is recorded in Codex's 2026-10-21 McCall addendum.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 7.13, 7.14, 7.15, 7.37, 7.42, 7.56
  - `T2_Descriptive.md`: Questions 7.8 & 7.9 (Exercises 7.10 & 7.11)
  - `T3_Compare_Analyze.md`: Comparisons 7.3 & 7.4
  - `T4_Diagrams.md`: Q7.V04 (Fig. 7.10)
- **Source Locators:**
  - Textbook (3rd ed.): §7.2.2, pp. 323–325
  - Companion Slides: Slides 30–39, Figs. 7.9 & 7.10
- **Pack Mapping Status:** Direct coverage is present across definition, factor structure, comparison, and figure-based review.

---

### Leaf 07 · Boehm Software Quality Model
- **Syllabus Category:** Software Quality
- **Core Concepts:** General Utility links directly to Portability and Maintainability; As-is Utility links to Reliability, Efficiency, and Human Engineering; Maintainability links to Testability, Understandability, and Modifiability. The model shows 7 intermediate constructs and 12 primitive characteristics.
- **Pack Locations:**
  - `T1_MCQ.md`: Question 7.16
  - `T3_Compare_Analyze.md`: Comparison 7.4
  - `T4_Diagrams.md`: Q7.V05 (Fig. 7.11)
- **Source Locators:**
  - Textbook (3rd ed.): §7.2.2, pp. 324–325
  - Companion Slides: Slides 40–41, Fig. 7.11
- **Pack Mapping Status:** Direct coverage is present in the MCQ, comparison, and diagram pack. The prior Boehm topology check is recorded in Codex's 2026-10-21 audit; this reconciliation does not repeat its source-image comparison.

---

### Leaf 08 · ISO 9126
- **Syllabus Category:** Software Quality
- **Core Concepts:** The current course-figure answer in T4 lists 6 characteristics (Functionality, Reliability, Usability, Efficiency, Maintainability, Portability) and 20 subcharacteristics. This is the assigned historical figure's formulation, not a universal count across later ISO editions.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 7.17, 7.40 & 7.41
  - `T2_Descriptive.md`: Question 7.10 (Exercise 7.13)
  - `T3_Compare_Analyze.md`: Comparison 7.3 (Exercise 7.14)
  - `T4_Diagrams.md`: Q7.V06 (Fig. 7.12)
- **Source Locators:**
  - Textbook (3rd ed.): §7.2.4, pp. 326–328
  - Companion Slides: Slides 41–46, Fig. 7.12
- **Pack Mapping Status:** Direct coverage is present. Q7.41 follows the course/source formulation and should not be read as a claim about later ISO editions.

---

### Leaf 09 · Basic Execution Time Model
- **Syllabus Category:** Software Reliability Models
- **Core Concepts:** John Musa's model; linear relationship between failure intensity and failures experienced; finite failures $v_0$; exponential decay over execution time.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 7.18, 7.20–7.22
  - `T2_Descriptive.md`: Question 7.11 (Exercise 7.15)
  - `T3_Compare_Analyze.md`: Comparisons 7.5 & 7.6
  - `T4_Diagrams.md`: Q7.V07 (Fig. 7.13, failure intensity against mean failures experienced)
  - `T5_Apply_Interpret.md`: Scenario 7.2 (release-intensity objective)
  - `T7_Calculations.md`: Problems 7.1, 7.3, 7.4 & 7.8
- **Source Locators:**
  - Textbook (3rd ed.): §7.3.1, pp. 329–334
  - Companion Slides: Slides 47–58, Figs. 7.13–7.17
- **Pack Mapping Status:** Direct conceptual and calculation coverage is present. The current T4 pointer is Fig. 7.13, and its explanation explicitly plots λ against μ, not execution time. The old figure/axis warning no longer describes the current text; this is not a new pixel/source audit.

---

### Leaf 10 · Logarithmic Poisson Execution Time Model
- **Syllabus Category:** Software Reliability Models
- **Core Concepts:** Musa–Okumoto NHPP model; exponential decay with failures experienced; infinite failures $v_0 = \infty$; inverse decay with execution time; failure intensity decay parameter $\theta$.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 7.23, 7.24 & 7.57
  - `T2_Descriptive.md`: Question 7.12 (Exercise 7.19)
  - `T3_Compare_Analyze.md`: Comparison 7.5 (Exercise 7.17)
  - `T4_Diagrams.md`: Q7.V07 (Fig. 7.18, failure intensity against mean failures experienced)
  - `T7_Calculations.md`: Problems 7.2, 7.5–7.8
- **Source Locators:**
  - Textbook (3rd ed.): §7.3.2, pp. 335–339
  - Companion Slides: Slides 59–71, Figs. 7.18 & 7.19
- **Pack Mapping Status:** Direct conceptual and calculation coverage is present. The current T4 pointer is Fig. 7.18, and its explanation explicitly plots λ against μ. The old figure/axis warning no longer describes the current text; this is not a new pixel/source audit.

---

### Leaf 11 · Calendar Time Component
- **Syllabus Category:** Software Reliability Models
- **Core Concepts:** Converting CPU execution time ($\tau$) to calendar time ($t$); resource usage model $\chi_k = \theta_k \tau + \mu_k \mu$; three resource-limited segments (Computer time, Identification personnel, Correction personnel).
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 7.5, 7.53 & 7.59
  - `T2_Descriptive.md`: Question 7.13 (Exercise 7.23)
  - `T4_Diagrams.md`: Q7.V08 (Fig. 7.21)
  - `T7_Calculations.md`: Problem 7.9
- **Source Locators:**
  - Textbook (3rd ed.): §7.3.3, pp. 339–344
  - Companion Slides: Slides 72–88, Figs. 7.20 & 7.21
- **Pack Mapping Status:** Direct text and calculation coverage is present. T4 Q7.V08 labels the calendar/execution-time ratio and resource-limited segments; prior figure/print review is recorded in the 2026-10-21 journal, not repeated here.

---

### Leaf 12 · The Jelinski–Moranda Model
- **Syllabus Category:** Software Reliability Models
- **Core Concepts:** Stepwise hazard rate $\lambda(t_i) = \phi [N - (i - 1)]$; constant hazard rate during inter-failure intervals; discrete staircase reliability growth.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 7.25 & 7.43
  - `T2_Descriptive.md`: Question 7.14 (Exercise 7.25)
  - `T3_Compare_Analyze.md`: Comparison 7.6
  - `T4_Diagrams.md`: Q7.V09 (Fig. 7.22)
  - `T7_Calculations.md`: Problem 7.10 (Part A)
- **Source Locators:**
  - Textbook (3rd ed.): §7.3.4, pp. 343–346
  - Companion Slides: Slides 89–92, Fig. 7.22
- **Pack Mapping Status:** Direct coverage is present across model definition, comparison, and application.

---

### Leaf 13 · The Bug Seeding Model
- **Syllabus Category:** Software Reliability Models
- **Core Concepts:** Harlan Mills model; capture-recapture sampling; seeding $S$ artificial bugs; estimating indigenous population $\hat{N} = \frac{S \cdot n}{s}$; equal detectability assumption.
- **Pack Locations:**
  - `T1_MCQ.md`: Question 7.51
  - `T2_Descriptive.md`: Question 7.15 (Exercise 7.26)
  - `T3_Compare_Analyze.md`: Comparison 7.7
  - `T7_Calculations.md`: Problem 7.10 (Part B)
- **Source Locators:**
  - Textbook (3rd ed.): §7.3.5, pp. 346–347
  - Companion Slides: Slide 93
- **Pack Mapping Status:** Direct coverage is present. The former T1 references to Q7.32–7.33 were CMM questions and did not cover bug seeding.

---

### Leaf 14 · CMM Maturity Levels
- **Syllabus Category:** Capability Maturity Model
- **Core Concepts:** 5 staged evolutionary levels: 1. Initial, 2. Repeatable, 3. Defined, 4. Managed, 5. Optimizing; continuous process improvement philosophy.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 7.26, 7.28, 7.29, 7.33–7.35, 7.44 & 7.60
  - `T2_Descriptive.md`: Questions 7.16 & 7.17
  - `T4_Diagrams.md`: Q7.V10 (Figs. 7.23 & 7.24)
  - `T5_Apply_Interpret.md`: Scenario 7.4 (Level 2 readiness)
- **Source Locators:**
  - Textbook (3rd ed.): §7.4 & §7.4.1, pp. 347–350
  - Companion Slides: Slides 94–96, Figs. 7.23 & 7.24
- **Pack Mapping Status:** Direct coverage is present for the five levels and their progression. The 2026-10-21 journal records the final CMM-figure sizing/layout correction; student final visual approval remains pending.

---

### Leaf 15 · CMM Key Process Areas (KPAs)
- **Syllabus Category:** Capability Maturity Model
- **Core Concepts:** 18 total KPAs (Level 1: 0; Level 2: 6; Level 3: 7; Level 4: 2; Level 5: 3); Peer Reviews and Software Product Engineering at Defined Level.
- **Pack Locations:**
  - `T1_MCQ.md`: Questions 7.26, 7.33, 7.44, 7.45 & 7.58
  - `T2_Descriptive.md`: Questions 7.17 & 7.18 (Exercises 7.28 & 7.33)
  - `T4_Diagrams.md`: Q7.V10 (five-level structure)
  - `T5_Apply_Interpret.md`: Scenario 7.4 (Level 2 KPA appraisal)
- **Source Locators:**
  - Textbook (3rd ed.): §7.4.2, pp. 350–353
  - Companion Slides: Slides 97–101
- **Pack Mapping Status:** Direct coverage is present. The former T1 Q7.36 reference was only about where CMM was developed and did not cover KPAs.

---

### Leaf 16 · CMM Common Features
- **Syllabus Category:** Capability Maturity Model
- **Core Concepts:** 5 structural common features organizing practices in every KPA: Commitment to Perform, Ability to Perform, Activities Performed, Measurement and Analysis, Verifying Implementation.
- **Pack Locations:**
  - `T1_MCQ.md`: Question 7.54 (direct question listing all five common features)
- **Source Locators:**
  - Textbook (3rd ed.): §7.4.2, pp. 353–354
  - Companion Slides: Slide 102
- **Pack Mapping Status:** Directly tested by one MCQ. No separate descriptive or application answer explicitly explains the five features in the current packs.

---

### Leaf 17 · Mapping ISO 9001 to the CMM
- **Syllabus Category:** ISO 9000
- **Core Concepts:** The relationship between ISO 9001:1994 clauses and CMM practices is not one-to-one: some clauses correspond to practices across KPAs, while some ISO requirements (such as Clause 4.15) have no corresponding KPA in the mapping.
- **Pack Locations:**
  - `T1_MCQ.md`: Question 7.39 (20-clause context)
  - `T3_Compare_Analyze.md`: Comparison 7.10 (Exercises 7.29 & 7.30)
- **Source Locators:**
  - Textbook (3rd ed.): §7.4.3, pp. 353–357
  - Companion Slides: Slides 103–107
- **Pack Mapping Status:** The clause-to-practice relationship is directly addressed in T3 Comparison 7.10, and Q7.39 supplies the clause-count context. The current comparison no longer asserts a numerical degree of coverage; it lists historical clause correspondences, explains exceptions and warns against converting overlap into a compliance percentage. The former quantitative-claim warning is superseded by that text; this ledger remains a navigation aid, not a source audit.

---

### Leaf 18 · Contrasting ISO 9001 and the CMM
- **Syllabus Category:** ISO 9000
- **Core Concepts:** ISO 9001 sets general quality-management-system requirements, while CMM focuses on software process capability and staged continuous improvement. Both rely on documented processes; one distinction is ISO certification versus a CMM maturity appraisal/score, not a claimed binary audit mechanism.
- **Pack Locations:**
  - `T1_MCQ.md`: Question 7.55 (direct conceptual contrast)
  - `T3_Compare_Analyze.md`: Comparisons 7.8 & 7.9
  - `T5_Apply_Interpret.md`: Scenario 7.6
- **Source Locators:**
  - Textbook (3rd ed.): §7.4.4, pp. 356–358
  - Companion Slides: Slides 103–107
- **Pack Mapping Status:** Direct comparison and scenario coverage is present. The mapped distinction is ISO certification versus a CMM maturity appraisal/score; the ledger does not establish a binary evaluation rule, and the answer’s source support remains a separate audit.

---

### Leaf 19 · Conclusion (Standards & Reliability Engineering Synthesis)
- **Syllabus Category:** ISO 9000
- **Core Concepts:** Synthesis of software reliability engineering and international standards; disciplined processes as a prerequisite for predictable, high-reliability software products.
- **Pack Locations:**
  - `T2_Descriptive.md`: Question 7.7 (standards and benefits)
  - `T3_Compare_Analyze.md`: Comparison 7.9, Conclusion subsection (standards improvement guidance); Comparisons 7.8 & 7.10 (supporting contrasts/mapping)
  - `T5_Apply_Interpret.md`: Scenario 7.6 (standards selection)
- **Source Locators:**
  - Textbook (3rd ed.): §7.5.3, p. 357; §7.4.5 & §7.5, pp. 358–359
  - Companion Slides: Slide 107
- **Pack Mapping Status:** Direct mapping to the chapter’s standards conclusion is present in T3 Comparison 7.9. This ledger verifies the question-to-term pointer against the current pack text; it is not a separate source audit. The conclusion addresses CMM improvement guidance, ISO 9001 certification needs, and process improvement over scores/certificates; it does not itself synthesize reliability models. The former T1 Q7.49, 7.59, and 7.60 references were isolated MTTF, calendar-time, and maturity questions, not a conclusion answer.

---

## Retrieval Practice Set & Self-Test Questions

1. Which question pack and problem numbers provide the complete 8-step numerical solution for Musa's Basic Execution Time Model?
2. Where in the study packs can a student find the visual interpretation and high-resolution diagrams of the McCall, Boehm, and ISO 9126 models?
3. Which leaf term covers the mapping of the 20 clauses of ISO 9001 to CMM Key Process Areas, and where is its primary comparative analysis located?
4. How many Key Process Areas are defined under CMM Level 2 and Level 3, and which leaf term tracks their syllabus coverage?
5. Where is the Example 7.2 discrepancy (source value 109 vs exact 109.86) documented and solved?
