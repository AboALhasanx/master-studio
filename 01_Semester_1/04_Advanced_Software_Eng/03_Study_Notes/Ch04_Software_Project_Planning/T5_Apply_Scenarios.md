---
title: "ASE Chapter 4 — T5 Applied Scenarios & Case Problems Pack · Software Project Planning"
# subtitle: "Applied Engineering Scenarios, Tool Specifications & Case Studies (8 Comprehensive Units)"
course: "Advanced Software Engineering (CS603)"
author: "Master Studio — Academic Tutoring Engine"
date: "2026-10-19"
doc_type: "study_pack"
header_left: "ASE Chapter 4 — T5 Applied Scenarios"
header_right: "Software Project Planning: Engineering Scenarios & Tool Design"
footer_left: "College of Computer Science & IT — University of Wasit"
footer_right: "Page {page} of {topage}"
---

# Chapter 4 — T5 Applied Scenarios & Case Problems Pack
<!--

This pack contains answers to applied source exercises (4.4, 4.19, 4.30, and 4.36) plus clearly identified authored practice scenarios. Hypothetical data and design choices are labeled; they are not presented as empirical findings or course rules.

> **Academic & Invariant Standard:**
>
> - Problem statements and engineering solutions are presented in **100% formal academic English**.
> - Core source principles and textbook relationships are highlighted in **bold**; pedagogical framing remains in plain text.
> - Detailed Arabic analysis (*الشرح المفاهيمي، التعليلات الهندسية، والفخاخ الامتحانية*) is placed in dedicated callouts strictly outside the model solutions.
> - Directional typography is strictly maintained: rightwards arrows (`→`) for English workflows and leftwards arrows (`←`) for Arabic notes.
> - Citations distinguish primary textbook printed pages (pp. 139–202) from companion slide numbers (slides 1–207).

---

-->
## Section 1: Applied Tool Design & Estimation Practice

### Unit 5.1 (Exercise 4.4): Automated LOC Counter Design, Language Dependencies & Boundary Parsing Limitations

**Design a Line of Code (LOC) counter for counting software size automatically. Is such a tool language-dependent? What are the fundamental limitations and parsing challenges of an automated LOC counter?**
{: .keep-next }

> **Architectural Specification & Engineering Analysis:**
>
> - **1. Modular Architecture of an Automated LOC Counter:**
>    An automated LOC counter cannot function as a naive line-splitter; it must operate as a multi-stage lexical processing pipeline:
>    - **Stage 1 — Source Ingestion & Normalization:** Strips platform-specific carriage returns (`CRLF` vs `LF`), normalizes Unicode encoding, and filters out completely empty lines.
>    - **Stage 2 — Lexical Scanner & State Machine:** Employs a deterministic finite automaton (DFA) tracking the active lexical state:
>      - `NORMAL_CODE`: Emitting executable or declarative tokens.
>      - `IN_STRING_LITERAL`: Neutralizing syntax characters (e.g., ignoring `//` or `/*` inside `"http://api.domain"`).
>      - `IN_SINGLE_COMMENT`: Scanning until newline (`//` in C/Java/C#, `#` in Python/Shell, `--` in Ada/SQL).
>      - `IN_MULTI_COMMENT`: Scanning until closing delimiter (`/* ... */` in C/Java, `{- ... -}` in Haskell, `'''` in Python).
>    - **Stage 3 — Line Classification & Metric Accounting:** Separates counts into three distinct ledgers:
>      - **Physical LOC (LOC):** Total newline count minus blanks and pure comments.
>      - **Logical Statements (SLOC):** Terminated executable/declarative constructs (e.g., semicolons in C/Java).
>      - **Comment Lines:** Explanatory documentation, noting hybrid lines containing both code and comments.
>
> - **2. Language Dependence Analysis:**
>    **Language dependence depends on the LOC definition.** A physical-line counter can count line breaks without parsing a language; a logical-statement counter or a counter that excludes comments needs language-specific rules.
>    - **Comment Syntax Diversity:** Different languages employ distinct comment delimiters. A universal tool must load language-specific grammar definition files.
>    - **Block Delimitation & Formatting:** In free-format languages (C, C++, Java), statement terminators (`;`) define logical lines, meaning multiple statements can occupy a single physical line, or one statement can span multiple physical lines. Conversely, in indentation-sensitive languages (Python), indentation level and newline characters define block semantics.
>    - **Preprocessor & Macro Expansions:** In C/C++, preprocessor directives (`#define`, `#ifdef`) alter line counts dramatically; expanding macros can convert a 5-line program into a 500-line preprocessed translation unit.
>
> - **3. Critical Engineering Limitations:**
>    - **Lack of Semantic Insight:** LOC treats a trivial variable initialization (`int x = 0;`) identically to a complex bitwise mathematical operation.
>    - **Coding Style Vulnerability:** Formatting conventions (e.g., K&R bracing vs Allman bracing) alter physical line counts by 20%–40% without changing software functionality.
>    - **Auto-Generated Boilerplate:** GUI builders and ORM frameworks generate thousands of lines of boilerplate code, inflating size metrics without reflecting human development effort.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.3.1, pp. 143–144; Companion Slides 6–8.*

> [!NOTE]
> **ملاحظة الطالب:**
>
> - عدّ الأسطر الفيزيائية ممكن بدون فهم اللغة؛ أمّا عدّ التعليمات المنطقية أو استثناء التعليقات فيحتاج قواعد خاصة باللغة وتعريفاً واضحاً لما يُحسب.

---

<div class="page-break"></div>

### Unit 5.2 (Exercise 4.19): Specification, Architecture & Planning Extension for a COCOMO Estimation Tool

**Specify, design, and develop a software system that implements Barry Boehm's COCOMO estimation model. Using standard software engineering principles as a guide, explain how to extend this basic calculation engine into an interactive project planning and decision-support tool.**
{: .keep-next }

> **Proposed Tool Design:**
>
> - **Inputs:** project size, the selected COCOMO ’81 mode and model tier, and any cost-driver ratings required by that tier.
> - **Calculation flow:** Basic COCOMO estimates effort from size and mode. Intermediate COCOMO applies the 15-driver EAF. Detailed COCOMO additionally allocates effort and schedule across lifecycle phases using phase-sensitive multipliers.
> - **Outputs:** estimated effort and schedule, with the selected mode, inputs, equations, and assumptions displayed so the estimate can be reviewed.
> - **Useful extensions:** sensitivity analysis can show how changing a supplied rating affects an estimate. A planning view may show phase allocations, but must preserve the source table's conceptual Plan & Requirement phase and its printed totals (106% effort and 110% schedule) or explicitly state a normalization method.
> - **Optional uncertainty feature:** scenario ranges or simulations may be added only when the user supplies defensible input ranges and distributions. They are extensions to the calculator, not outputs guaranteed by COCOMO.
>
> *Source for COCOMO inputs and equations: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.4, pp. 152–160; Companion Slides 41–65. The proposed interface and extensions are authored design choices.*

> [!NOTE]
> **ملاحظة الطالب:**
>
> - افصل بين متطلبات النموذج الأساسية والخصائص التي تقترحها أنت للأداة. لا تضف حداً مثل 75% أو «منطقة مستحيلة» ما لم يسنده مصدر محدد.

---

<div class="page-break"></div>

### Unit 5.3 (Exercise 4.30): Comparing Cost Models with Hypothetical Data

**Using the following hypothetical data for two software projects, apply Basic COCOMO, Walston-Felix, and SEL. Compare the estimates with the stated effort values. What can and cannot be concluded from this comparison?**
{: .keep-next }

> **Illustrative data only (not collected project measurements):**
> - Project Alpha: $25$ KLOC; stated comparison effort $65$ PM; assume Organic mode.
> - Project Beta: $100$ KLOC; stated comparison effort $520$ PM; assume Semidetached mode.
>
> **Effort estimates:**
> - **Basic COCOMO:** Alpha $2.4(25)^{1.05}\approx70.5$ PM; Beta $3.0(100)^{1.12}\approx521.3$ PM.
> - **Walston-Felix:** Alpha $5.2(25)^{0.91}\approx97.3$ PM; Beta $5.2(100)^{0.91}\approx343.6$ PM.
> - **SEL:** Alpha $1.4(25)^{0.93}\approx27.9$ PM; Beta $1.4(100)^{0.93}\approx101.4$ PM.
>
> Against the hypothetical comparison values, the relative errors differ by model and project. These two constructed cases do not establish that one model is generally superior, nor do they validate the comparison efforts as actual observations. A real calibration study needs consistently defined project boundaries, measured size and effort, justified mode selection, and more than two comparable projects.
>
> *Source for the equations: K.K. Aggarwal & Yogesh Singh (3rd ed.), §§4.3–4.4, pp. 149–156; Companion Slides 31–43. The project data are synthetic practice inputs.*

> [!NOTE]
> **ملاحظة الطالب:**
>
> - هذه بيانات تدريبية افتراضية، وليست قياسات لمشاريع حقيقية. مثالان لا يكفيان لإثبات أن نموذجاً أفضل دائماً أو لبناء معايرة موثوقة.

---

<div class="page-break"></div>

### Unit 5.4 (Exercise 4.36): Risk Categories in a Student Project

**Analyze a student software project, list representative risks, group them using the chapter’s five risk categories, and indicate how the chapter’s assessment and control activities apply.**
{: .keep-next }

> **Risk list for a hypothetical student project:**
>
> - **Dependencies on outside agencies or factors:** delayed access to a required service, dataset, or supervisor decision.
> - **Requirement issues:** unclear acceptance criteria or changing requested features.
> - **Management issues:** underestimated tasks, missed coordination, or unbalanced ownership.
> - **Lack of knowledge:** unfamiliar tools or missing domain knowledge.
> - **Other risk categories:** loss of a key contributor, unavailable test equipment, or performance targets that prove difficult to meet.
>
> **Risk handling using the chapter's activity groups:**
> - **Assessment:** identify each risk, analyze its probability and potential loss, then prioritize by exposure ($RE=P\times L$).
> - **Control:** plan a response for significant risks, monitor their indicators during the project, and resolve or adjust the plan when a risk occurs.
>
> Example: for a changing requirement, record the affected deliverable and decision owner, agree how changes are reviewed, track new requests, and re-estimate affected work before accepting a change. These are proposed student-project actions, not universal probabilities or prescribed tools.
>
> *Source for risk categories and activities: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.7, pp. 194–198; Companion Slides 180–193. The examples and handling actions are authored applications.*

> [!NOTE]
> **ملاحظة الطالب:**
>
> - استخدم فئات المخاطر الخمس، ثم طبّق التسلسل: تحديد ← تحليل ← ترتيب الأولوية، وبعدها التخطيط والمراقبة والمعالجة.

---

## Section 2: Advanced Practical Case Studies

<div class="page-break"></div>

### Unit 5.5: Real-World Function Point Extraction Case Study (Hospital Portal)

**For this hypothetical hospital portal, classify the listed functions and data stores. Use the explicit Low/Average/High complexity assumptions in the answer to calculate UFP; the prompt does not provide enough DET/FTR/RET detail to derive complexity independently.**
{: .keep-next }

> **Hospital Portal Functional Specification:**
> 1. *Patient Admission Form (Screen 1):* Enters patient demographics, room assignment, and insurance carrier; writes directly to the internal Patient Database.
> 2. *Doctor Treatment Entry (Screen 2):* Records daily medication, doctor visits, and surgical procedures; updates internal Inpatient Ledger.
> 3. *Discharge Checkout Transaction (Screen 3):* Validates medical clearance and locks the patient's billing account.
> 4. *Consolidated Billing Invoice (Report 1):* Calculates bed charges, pharmaceutical totals, doctor fees, applies insurance deductibles, and generates a printable invoice.
> 5. *Daily Bed Census Summary (Report 2):* Aggregates occupancy rates across hospital departments with departmental statistics.
> 6. *Real-Time Bed Availability Query (Inquiry 1):* Interactive search allowing staff to locate empty beds by ward without altering database state.
> 7. *Patient Billing Status Lookup (Inquiry 2):* Interactive query displaying current accrued charges without modifying account state.
> 8. *Internal Data Stores:* The system maintains a *Patient Master File* and an *Inpatient Treatment Ledger*.
> 9. *External Data Stores:* The system reads eligibility tables from an *External National Insurance Provider Database*.

> **Information Domain Classification & UFP Computation:**
>
> **Assumption:** The prompt omits DET/FTR/RET counts, so it cannot determine transaction/file complexity. The Low/Average/High ratings below are explicit practice assumptions, not deductions from the screen descriptions.
>
> - **1. Component Classification & Complexity Assignment:**
>    - **External Inputs (EI):** 3 transactions that alter internal state:
>      - Patient Admission Form (Average Complexity: Weight = $4$).
>      - Doctor Treatment Entry (Average Complexity: Weight = $4$).
>      - Discharge Checkout Transaction (Low Complexity: Weight = $3$).
>      $$\text{Total EI Weight} = 4 + 4 + 3 = 11$$
>    - **External Outputs (EO):** 2 transactions generating derived mathematical calculations:
>      - Consolidated Billing Invoice (High Complexity due to multi-source aggregation and insurance calculation: Weight = $7$).
>      - Daily Bed Census Summary (Average Complexity: Weight = $5$).
>      $$\text{Total EO Weight} = 7 + 5 = 12$$
>    - **External Inquiries (EQ):** 2 interactive lookups retrieving data without state changes:
>      - Real-Time Bed Availability Query (Low Complexity: Weight = $3$).
>      - Patient Billing Status Lookup (Average Complexity: Weight = $4$).
>      $$\text{Total EQ Weight} = 3 + 4 = 7$$
>    - **Internal Logical Files (ILF):** 2 major internal relational entities maintained inside the system boundary:
>      - Patient Master File (High Complexity: Weight = $15$).
>      - Inpatient Treatment Ledger (High Complexity: Weight = $15$).
>      $$\text{Total ILF Weight} = 15 + 15 = 30$$
>    - **External Interface Files (EIF):** 1 reference data store maintained externally:
>      - External National Insurance Database (Average Complexity: Weight = $7$).
>      $$\text{Total EIF Weight} = 7$$
>
> - **2. Unadjusted Function Points (UFP) Summation:**
>    $$\text{UFP} = \sum \text{EI} + \sum \text{EO} + \sum \text{EQ} + \sum \text{ILF} + \sum \text{EIF}$$
>    $$\text{UFP} = 11 + 12 + 7 + 30 + 7 = 67 \text{ UFP}$$
>
> - **3. Application of Complexity Adjustment Factor (CAF):**
>    Assuming the hospital environment assesses the 14 General System Characteristics (GSCs) with $\sum F_i = 42$ (reflecting high data communication, performance, and transactional volume):
>    $$\text{CAF} = 0.65 + 0.01 \times (42) = 0.65 + 0.42 = 1.07$$
>    $$\text{Adjusted FP} = \text{UFP} \times \text{CAF} = 67 \times 1.07 = 71.69 \approx 72 \text{ FP}$$
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.3.2, pp. 145–148; Companion Slides 10–29.*

> [!NOTE]
> **ملاحظة الطالب:**
>
> - أوزان التعقيد هنا افتراضات تدريبية؛ تحديدها فعلياً يحتاج تفاصيل عن الملفات والمعاملات والبيانات الداخلية والخارجية.

---

<div class="page-break"></div>

### Unit 5.6: Rayleigh Staffing and a Proposed Schedule Recovery

**A hypothetical project has a planned duration $t_d=12$ months and whole-project effort $K=95$ person-years. At month 8, a manager proposes adding 25 developers to recover a two-month delay. Use the Rayleigh curve to estimate planned staffing at month 8 and the peak. What can the model establish about the proposed change, and what additional information is needed?**
{: .keep-next }

> **Rayleigh estimates for the original plan:**
>
> - $t_d=12$ months $=1$ year; $K=95$ person-years.
> - Peak staffing at $t=t_d$:
>   $$m_0=\frac{K}{t_d\sqrt e}=\frac{95}{1\times\sqrt e}\approx57.62\text{ persons}.$$
> - Planned staffing at month 8 ($t=8/12=2/3$ years):
>   $$m(t)=\frac{K}{t_d^2}t e^{-t^2/(2t_d^2)}\approx50.71\text{ persons}.$$
>
> **What the model does and does not establish:**
> The curve describes the original planned staffing profile. It does not model the effect of adding 25 people or predict the revised completion date. If the 25 people are added to a roughly 51-person team, the theoretical number of pairwise communication links rises from $51(50)/2=1{,}275$ to $76(75)/2=2{,}850$; this is a graph count, not a direct measure of communication effort or schedule delay.
>
> A defensible recovery decision needs task dependencies, remaining work, which tasks can be parallelized, onboarding needs, and the team's actual staffing. Re-estimate the schedule and effort with those inputs before deciding whether to add people or change scope/date.
>
> *Source for the Rayleigh equations: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.6.1, printed pp. 182–185; Companion Slides 123–140. The proposed recovery analysis is authored practice.*

> [!NOTE]
> **ملاحظة الطالب:**
>
> - معادلة رالي تصف منحنى التوظيف المخطط. عدد قنوات الاتصال لا يساوي مقدار التأخير الفعلي، لذلك لا تستنتج وحده نتيجة مؤكدة لإضافة موظفين.

---

<div class="page-break"></div>

### Unit 5.7: Risk Assessment and Control for an Embedded-System Scenario

**For a hypothetical embedded controller, analyze the risk that delayed sensor data may cause a processing deadline to be missed. Apply the chapter’s risk-assessment and risk-control activities.**
{: .keep-next }

> **Hypothetical risk statement:** Delayed sensor data may cause a controller to miss a required processing deadline. The scenario does not specify a real device, deadline, probability, or clinical response.
>
> **Risk assessment:**
> 1. **Identify:** record the delayed-data event, its causes, affected operation, and possible loss.
> 2. **Analyze:** estimate probability and loss only after project evidence or an explicitly stated classroom scale is provided.
> 3. **Prioritize:** use $RE=P\times L$ when compatible, defined scales for probability and loss are available. No numeric exposure can be calculated from the prompt as written.
>
> **Risk control:**
> - **Plan:** define a verification approach for timing assumptions and an owner for resolving a missed deadline.
> - **Monitor:** measure response time under the specified operating conditions and review deadline misses.
> - **Resolve:** if a deadline is missed, follow the system's approved safety requirements, investigate the cause, and revise the design or plan before release.
>
> This is a classroom risk-analysis example, not a medical-device safety specification.
>
> *Source for the assessment/control structure and exposure equation: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.7, pp. 194–198; Companion Slides 190–193. The sensor scenario is authored.*

> [!NOTE]
> **ملاحظة الطالب:**
>
> - لا تضع احتمالاً أو أثراً رقمياً قبل تحديد مقياسهما. اربط الخطر أولاً بالتحديد والتحليل والأولوية، ثم بخطة ومؤشرات متابعة واستجابة.

---

<div class="page-break"></div>

### Unit 5.8: Checking Incomplete Multi-Model Estimates

**A systems integration enterprise prepares a competitive tender for a National e-Governance Tax Portal. In a hypothetical bid, Team A reports $120 \text{ KLOC}$ and $280 \text{ PM}$ under Organic Basic COCOMO. Team B reports $850 \text{ FP}$ and $440 \text{ PM}$ under Intermediate COCOMO, but omits some conversion and driver inputs. Determine whether the estimates can be reconciled from the supplied information and identify what must be verified.**
{: .keep-next }

> **First check whether the estimates can be compared:**
>
> - Team A reports 120 KLOC and 280 PM under Basic COCOMO Organic. Recomputing the stated model gives $2.4(120)^{1.05}\approx366$ PM, so the reported 280 PM does not follow from those inputs and equation.
> - Team B reports 850 FP and 440 PM from Intermediate COCOMO, but the prompt does not provide a language conversion, the resulting KLOC, selected mode, complete driver ratings, or multiplier values. Its effort cannot be reproduced from the information given.
> - Function Points and KLOC describe size differently. Do not convert between them using a universal ratio; a conversion needs a stated language and an applicable conversion table or measured local data.
>
> **Conclusion:** The two estimates cannot yet be reconciled into one defensible bid. First align project scope and boundaries, verify each size estimate, document the model/mode and all driver ratings, then recalculate both estimates. If uncertainty ranges are needed, state their basis separately; do not invent a PERT range or choose a final bid from incomplete inputs.
>
> *Source for COCOMO equations and sizing approaches: K.K. Aggarwal & Yogesh Singh (3rd ed.), §§4.3–4.4, pp. 140–165; Companion Slides 9–71. The scenario values are hypothetical; required inputs are intentionally omitted so you can identify the evidence needed before making a bid.*

> [!NOTE]
> **ملاحظة الطالب:**
>
> - لا تحوّل FP إلى KLOC بنسبة عامة. قبل جمع تقديرين، وحّد حدود المنتج والمدخلات والنموذج والمضاعفات، ثم أعد الحسابات.

---

<div class="page-break"></div>

## Topic-to-Question Map

| Topic Area | Questions Covering Item | Primary Course Sources | Key Concepts & Frameworks Covered |
|:---|:---|:---|:---|
| **1. Size Estimation (LOC & Tool Design)** | Unit 5.1 (Ex 4.4), Unit 5.8 | K.K. Aggarwal pp. 143–145; Slides 6–8 | Lexical scanning DFA, Physical vs Logical LOC, comment syntax, macro expansion, language dependence. |
| **2. COCOMO Tool Design** | Unit 5.2 (Ex 4.19) | K.K. Aggarwal pp. 152–160; Slides 41–65 | Tier-specific inputs and equations; optional sensitivity and phase-allocation views. |
| **3. Comparing Estimation Models** | Unit 5.3 (Ex 4.30) | K.K. Aggarwal pp. 149–156; Slides 31–43 | A worked comparison using explicitly hypothetical data; limits on conclusions from small samples. |
| **4. Student Project Risks** | Unit 5.4 (Ex 4.36) | K.K. Aggarwal pp. 194–198; Slides 180–193 | The five risk categories and the assessment/control activities, applied to an example. |
| **5. Real-World Function Point Extraction** | Unit 5.5 (Applied Case Study) | K.K. Aggarwal pp. 145–148; Slides 10–29 | Hospital portal case study: classifying EI, EO, EQ, ILF, EIF; complexity weights; UFP & CAF calculation. |
| **6. Rayleigh Staffing and Schedule Recovery** | Unit 5.6 (Applied Scenario) | K.K. Aggarwal printed pp. 182–185; Slides 123–140 | Planned staffing at a given time, peak staffing, and the limits of inferring the effect of new hires. |
| **7. Risk Assessment and Control** | Unit 5.7 (Authored Scenario) | K.K. Aggarwal pp. 194–198; Slides 180–193 | Risk identification, analysis, prioritization, planning, monitoring, and resolution; no real-device prescription. |
| **8. Multi-Model Estimate Reconciliation** | Unit 5.8 (Authored Scenario) | K.K. Aggarwal pp. 140–165; Slides 9–71 | Check model inputs and assumptions before trying to reconcile incompatible estimates. |

---

<!--
## Retrieval Set & Active Recall Self-Test

Use the applied scenarios and system specifications in this pack for active recall and engineering practice:
-->
1. Walk through the lexical scanner DFA states for an automated LOC counter without consulting the text.
2. Identify which inputs differ between Basic, Intermediate, and Detailed COCOMO.
3. Compute Rayleigh staffing at month 8 and at the planned peak for the given project.
4. List the course risk-assessment and risk-control activities.
5. State why incomplete model inputs prevent a unique reconciliation of two estimates.

