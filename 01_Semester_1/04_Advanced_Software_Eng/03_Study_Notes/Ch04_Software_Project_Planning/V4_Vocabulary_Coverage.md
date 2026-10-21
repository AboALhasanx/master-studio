---
title: "ASE Chapter 4 — V4 Academic Vocabulary & Syllabus Ledger · Software Project Planning"
# subtitle: "Complete Course Terminology & Examination Ledger (18/18 Confirmed Curriculum Terms)"
course: "Advanced Software Engineering (CS603)"
author: "Master Studio — Academic Tutoring Engine"
date: "2026-10-19"
doc_type: "study_pack"
header_left: "ASE Chapter 4 — V4 Vocabulary Ledger"
header_right: "Software Project Planning: 18/18 Confirmed Terms"
footer_left: "College of Computer Science & IT — University of Wasit"
footer_right: "Page {page} of {topage}"
---

# Chapter 4 — V4 Academic Vocabulary & Syllabus Ledger
<!--

This ledger organizes the **18 listed instructor subtopics across 6 modules** for Chapter 4: *Software Project Planning*. Coverage and source-verification status are recorded separately in the chapter index; inclusion here alone does not certify a term as fully verified.

For each term, the ledger records the candidate primary-book pages (K.K. Aggarwal & Yogesh Singh, 3rd ed., printed pp. 139–202) and companion-slide locators (slides 1–207); see the index for the live source-verification status.
Each entry provides an English definition, relevant equations or mechanisms, a concise Arabic rationale, and an exam distinction where useful.

---

-->
## Module 1: Software Size Estimation

### Term 01. Lines of Code (LOC)

> **Academic Definition & Technical Specification:**
> **Lines of Code (LOC) is a code-based measure of software size, expressed as a count of source-code lines under a stated counting convention.**
>
> **Core Mechanisms & Standards:**
>
> - **1. Counting Conventions:**
>    - Physical-line and logical-statement counts can differ. A reported count should identify its convention; treatment of blank lines, comments, and language syntax may vary.
> - **2. Critical Engineering Limitations:**
>    - **Language Dependence:** Expressing the exact same algorithm requires significantly fewer lines in high-level languages (e.g., Python, SQL) than in low-level languages (e.g., Assembly, C).
>    - LOC is language- and implementation-dependent, so a larger count alone does not establish greater user functionality or better productivity.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.3.1, pp. 143–145; Companion Slides 6–8.*

<!--
> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** مقياس يعتمد على حجم الشيفرة، وقد يعبّر عنه بآلاف الأسطر (KLOC).
> - **نقطة تمييز:** تتأثر النتيجة باللغة وطريقة العد، لذلك لا تكفي وحدها لمقارنة الوظائف التي يحصل عليها المستخدم.
-->

---

<div class="page-break"></div>

### Term 02. Function Count and Its Relation to Function Point Analysis

> **Academic Definition & Technical Specification:**
> **The course lists Function Count as a size-estimation topic. The chapter explains Albrecht's Function Point method: it classifies five types of functional units by complexity and weights them to calculate unadjusted and adjusted Function Points. Keep the course term Function Count distinct from the calculated measures UFP and FP.**
>
> **Mathematical Formulation & Pipeline:**
>
> - **1. The 5 Information Domain Characteristics:**
>    - **External Inputs (EI):** Transactions entering the system that alter internal state (Weights: Low=3, Average=4, High=6).
>    - **External Outputs (EO):** Data or information leaving the system as an output (Weights: Low=4, Average=5, High=7).
>    - **External Inquiries (EQ):** On-demand searches that display data without altering internal state (Weights: Low=3, Average=4, High=6).
>    - **Internal Logical Files (ILF):** User-identifiable logical data groups maintained entirely inside the application boundary (Weights: Low=7, Average=10, High=15).
>    - **External Interface Files (EIF):** Reference data files maintained by external systems across interfaces (Weights: Low=5, Average=7, High=10).
> - **2. Unadjusted Function Points (UFP):**
>    $$\text{UFP} = \sum_{i=1}^5 \sum_{j=1}^3 W_{ij} \cdot Z_{ij}$$
> - **3. Complexity Adjustment Factor (CAF):**
>    $$\text{CAF} = 0.65 + 0.01 \times \sum_{i=1}^{14} F_i \quad (0.65 \leq \text{CAF} \leq 1.35)$$
> - **4. Final Adjusted Function Points:**
>    $$\text{FP} = \text{UFP} \times \text{CAF}$$
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.3.2, pp. 145–148; Companion Slides 9–30.*

<!--
> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** تقدير للحجم الوظيفي من منظور الوظائف التي يطلبها المستخدم، ويمكن استخدامه قبل اكتمال الشيفرة.
> - **نقطة تمييز:** احسب UFP من الأنواع الخمسة وأوزان تعقيدها، ثم احسب CAF من عوامل النظام الأربعة عشر؛ مجال CAF في هذه الصيغة شامل للحدين $0.65$ و$1.35$.
-->

---

## Module 2: Cost Estimation Models

### Term 03. Static, Single Variable Models

> **Academic Definition & Technical Specification:**
> **Static Single-Variable Models are empirical cost estimation equations that predict total development effort as a mathematical power function of a single project parameter—predominantly software size in thousands of lines of code (KLOC).**
>
> **Mathematical Formulation & Canonical Variants:**
>
> - **1. General Power Equation:**
>    $$E = a \times L^b \text{ [Person-Months]}$$
>    Where $a$ is an organization-specific baseline constant, $L$ is size in KLOC, and $b$ is the scaling exponent.
> - **2. IBM Walston-Felix Model (Federal Systems Division):**
>    $$E = 5.2 \times L^{0.91}$$
> - **3. NASA Software Engineering Laboratory (SEL) Model (Goddard Space Flight Center):**
>    $$E = 1.4 \times L^{0.93}$$
>
> **Scope:** These equations use one project-size variable, $L$ in KLOC, to estimate effort. Their coefficients and calibration contexts differ; do not infer which model is more accurate for a new project from the equations alone.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.3.3, pp. 149–151; Companion Slides 34–35, 37–40.*

> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** نماذج تجريبية تستخدم متغيراً وحيداً فقط (الحجم $L$) لتقدير الجهد.
> - **نقطة تمييز:** للنموذجين معاملات وأسس مختلفة؛ اختلاف الناتج لا يثبت وحده أيهما أدق لمشروع جديد. قارن عند الحجم نفسه وبوحدة KLOC.

---

<div class="page-break"></div>

### Term 04. Static, Multivariable Models

> **Academic Definition & Technical Specification:**
> **Static multivariable models estimate software effort using size together with other project or environment variables. The specific equation depends on the model.**
>
> **Mathematical Formulation & Canonical Variants:**
>
> - **1. Basili and Freburger Multivariable Model:**
>    $$E = a_0 + \sum_{i=1}^n a_i X_i$$
>    Effort is expressed as a multi-factor regression equation incorporating lines of code, program complexity, staffing experience, and memory constraints.
> - **2. Walston-Felix productivity index:**
>    $$I = \sum_{i=1}^{29} W_i X_i, \qquad X_i \in \{-1,0,+1\}$$
>    The 29 assessed factors contribute weighted values to an index used with the source's productivity-index chart. Do not replace this procedure with a product of 29 multipliers.
>
> **Distinction from Single-Variable Models:**
> - Multivariable approaches use project or environment factors in addition to size; the calculation depends on the specific model.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.3.4, pp. 151–152; Companion Slides 34, 36–40.*

<!--
> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** نماذج تأخذ بالحسبان عدة عوامل في آن واحد (مثل خبرة الفريق، قيود الذاكرة، التوثيق) إلى جانب الحجم.
> - **نقطة تمييز:** لا تختزل كل النماذج متعددة المتغيرات في معادلة واحدة؛ اتبع متغيرات وطريقة النموذج المحدد في السؤال.
-->

---

## Module 3: The Constructive Cost Model (COCOMO '81)

### Term 05. Basic COCOMO Model

> **Academic Definition & Technical Specification:**
> **Basic COCOMO is a size-based cost-estimation model that calculates effort and development time from KLOC using different coefficients for the Organic, Semidetached, and Embedded modes.**
>
> **Mathematical Formulations & Mode Equations:**
>
> - **1. The Three Operating Modes:**
>    - **Organic Mode:** Typically smaller projects with experienced teams, familiar domains, and relatively flexible constraints.
>      $$E = 2.4 (\text{KLOC})^{1.05} \text{ PM}, \quad D = 2.5 (E)^{0.38} \text{ Months}$$
>    - **Semidetached Mode:** Typically intermediate projects with mixed team experience and constraints.
>      $$E = 3.0 (\text{KLOC})^{1.12} \text{ PM}, \quad D = 2.5 (E)^{0.35} \text{ Months}$$
>    - **Embedded Mode:** Projects operating under tight hardware, software, or operational constraints.
>      $$E = 3.6 (\text{KLOC})^{1.20} \text{ PM}, \quad D = 2.5 (E)^{0.32} \text{ Months}$$
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.4.1, pp. 152–156; Companion Slides 41–50.*

> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** المستوى التأسيسي الأول من COCOMO، يعتمد على الحجم ونمط بيئة المشروع فقط.
> - **نقطة تمييز:** استعمل معاملات الحجم والجهد والوقت الخاصة بالنمط المختار؛ أوصاف الأنماط تساعد على الاختيار ولا تجعل حدود الحجم وحدها قاعدة مطلقة.

---

### Term 06. Intermediate COCOMO Model

> **Academic Definition & Technical Specification:**
> **Intermediate COCOMO extends the basic model by adjusting nominal effort using an Effort Adjustment Factor (EAF) derived from 15 cost-driver attributes spanning product, computer, personnel, and project dimensions.**
>
> **Mathematical Formulation:**
>
> - **1. Governing Equations:**
>    $$E = a_i (\text{KLOC})^{b_i} \times \text{EAF} \text{ [Person-Months]}$$
>    $$\text{EAF} = \prod_{j=1}^{15} EM_j$$
> - **2. Intermediate Leading Coefficients ($a_i$):**
>    - Organic: $a_i = 3.2, \quad b_i = 1.05$
>    - Semidetached: $a_i = 3.0, \quad b_i = 1.12$
>    - Embedded: $a_i = 2.8, \quad b_i = 1.20$
> - **3. The 15 Cost Drivers (4 Categories):**
>    - **Product Attributes:** Reliability (RELY), Database Size (DATA), Product Complexity (CPLX).
>    - **Computer Attributes:** Execution Time Constraint (TIME), Main Storage Constraint (STOR), Virtual Machine Volatility (VIRT), Turnaround Time (TURN).
>    - **Personnel Attributes:** Analyst Capability (ACAP), Applications Experience (AEXP), Programmer Capability (PCAP), Virtual Machine Experience (VEXP), Programming Language Experience (LEXP).
>    - **Project Attributes:** Modern Programming Practices (MODP), Use of Software Tools (TOOL), Required Development Schedule (SCED).
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.4.2, pp. 156–158; Companion Slides 51–57.*

> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** النموذج المتوسط الذي يدمج تأثير العوامل البيئية الـ 15 عبر ضرب معاملاتها للحصول على معامل التعديل (EAF).
> - **فخ الامتحان الأكبر:** المعامل الأساسي $a_i$ في Intermediate يختلف عن Basic: في النمط العضوي (Organic) يرتفع من 2.4 إلى 3.2! بينما في Semidetached يبقى 3.0، وفي Embedded ينخفض من 3.6 إلى 2.8. تذكر أن EAF ينتج عن ضرب جميع المعاملات معاً (وليس جمعها).

---

<div class="page-break"></div>

### Term 07. Detailed COCOMO Model

> **Academic Definition & Technical Specification:**
> **Detailed COCOMO incorporates all characteristics of the intermediate model while acknowledging that cost drivers impact individual development lifecycle phases unevenly, utilizing phase-sensitive effort multipliers and phase-specific effort/schedule distribution percentages.**
>
> **Core Mechanisms & Lifecycle Phase Breakdown:**
>
> - **1. Phase-sensitive cost drivers:**
>    Detailed COCOMO applies cost-driver effects across five lifecycle phases:
>    $$\text{Plan \& Requirement} \rightarrow \text{System Design} \rightarrow \text{Detail Design} \rightarrow \text{Module Code \& Test} \rightarrow \text{Integration \& Test}$$
> - **2. Three-Level Hierarchical Structure:**
>    - **Module Level:** Individual code units characterized by specific complexity and personnel assignments.
>    - **Subsystem Level:** Aggregations of modules sharing common platform constraints.
>    - **System Level:** Global project integration and overall management.
> - **3. Curriculum Book Table 4.7 Phase Distribution (Aggarwal & Singh p. 159 / Slides 62–63):**
>    - Organic Small ($S\approx2$): Plan & Requirement (6%), System Design (16%), Detail Design (26%), Module Code & Test (42%), Integration & Test (16%) for effort; the corresponding schedule fractions are 10%, 19%, 24%, 39%, and 18%.
>    *(Audit Notice: Course source percentages sum to 106% for effort and 110% for schedule; preserved per course standard).*
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.4.3, pp. 158–161; Companion Slides 57–65.*

> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** يوزع النموذج أثر عوامل الكلفة وتقديرات الجهد والوقت على مراحل التطوير؛ استعمل أسماء المراحل كما يوردها الجدول.
> - **نقطة تدقيق:** جدول Organic Small يعرض مجموع جهد $106\%$ ومجموع وقت $110\%$؛ اذكر القيم المطبوعة كما هي عند السؤال عنها.

---

## Module 4: COCOMO II

### Term 08. Application Composition Estimation Model

> **Academic Definition & Technical Specification:**
> **The Application Composition model is a COCOMO II stage for estimating applications assembled with reusable components, screens, reports, and 3GL modules.**
>
> **Mathematical Formulation & Sizing Method:**
>
> - **1. Sizing Metric — Object Points (OP):**
>    Decomposes the system into Screens, Reports, and 3GL Modules.
> - **2. Object Point Accounting:**
>    $$\text{NOP} = \text{Object Points} \times \left(1 - \frac{\% \text{Reuse}}{100}\right)$$
> - **3. Effort Computation via Productivity Rate (PROD):**
>    $$\text{Effort} = \frac{\text{NOP}}{\text{PROD}} \text{ [Person-Months]}$$
>    Where Developer Capability (PROD) ranges from Very Low ($4 \text{ NOP/PM}$), Nominal ($13 \text{ NOP/PM}$), to Very High ($50 \text{ NOP/PM}$).
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.5.1, printed pp. 162–167; Companion Slides 73–84.*

> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** المرحلة الأولى من COCOMO II، وتستخدم للمشاريع المبنية بأدوات التوليد السريع (مثل Visual Basic و Oracle Forms) ونماذج الواجهات الأولية.
> - **فخ الامتحان:** المقياس هنا هو **نقاط الكائنات (Object Points)** وليس Function Points ولا أسطر الكود. يتم احتساب الشاشات والتقارير ومكونات 3GL، ويتم خصم نسبة إعادة الاستخدام لحساب النتيجة الصافية (NOP).

---

### Term 09. The Early Design Model

> **Academic Definition & Technical Specification:**
> **The Early Design model is a COCOMO II stage used before a detailed architecture and its full cost-driver information are available. It estimates effort with seven aggregated cost drivers and five scale factors.**
>
> **Mathematical Formulation:**
>
> - **1. Governing Equation:**
>    $$E_{\text{nom}} = A \times (\text{Size})^B \times \prod_{i=1}^7 EM_i$$
> - **2. Sizing Metric:** Size is expressed in KSLOC, typically derived by converting Unadjusted Function Points (UFP) using language gear ratios.
> - **3. The 7 Aggregated Cost Drivers:**
>    Product Reliability and Complexity (RCPX), Required Reuse (RUSE), Platform Difficulty (PDIF), Personnel Capability (PERS), Personnel Experience (PREX), Facilities and Tools (FCIL), and Schedule (SCED).
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.5.2, printed pp. 167–173; Companion Slides 85–89.*

<!--
> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** المرحلة الثانية التي تُستخدم عندما تصبح المتطلبات واضحة لكن المعمارية الدقيقة لم تُحسم بعد.
> - **فخ الامتحان:** احفظ عدد عوامل الكلفة هنا: **7 عوامل مجمعة** فقط (وليس 17 كما في Post-Architecture ولا 15 كما في COCOMO '81). يتم دمج مهارات الفريق في PERS وخبراتهم في PREX لتقليل عبء التقدير المبكر.
-->

---

<div class="page-break"></div>

### Term 10. Post-Architecture Model

> **Academic Definition & Technical Specification:**
> **The Post-Architecture Model is used when the software architecture is available and project sizing and cost-driver information can be assessed in detail. It uses 17 effort multipliers and 5 scale factors.**
>
> **Mathematical Formulation & Scale Factors:**
>
> - **1. Governing Effort Equation:**
>    $$E = A \times (\text{Size})^B \times \prod_{i=1}^{17} EM_i \quad (A = 2.94)$$
> - **2. Scaling Exponent ($B$) from 5 Scale Factors ($SF_j$):**
>    $$B = 0.91 + 0.01 \times \sum_{j=1}^5 SF_j$$
>    - **Precedentedness (PREC):** Domain novelty ($0.00 \text{ to } 6.20$).
>    - **Development Flexibility (FLEX):** Constraint rigidity ($0.00 \text{ to } 5.07$).
>    - **Architecture / Risk Resolution (RESL):** Risk mitigation depth ($0.00 \text{ to } 7.07$).
>    - **Team Cohesion (TEAM):** Stakeholder synchronization ($0.00 \text{ to } 5.48$).
>    - **Process Maturity (PMAT):** CMM/CMMI rating ($0.00 \text{ to } 7.80$).
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.5.3, printed pp. 168–181; Companion Slides 90–120.*

> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** يستخدم النموذج عندما تتوفر تفاصيل المعمارية ومدخلات المشروع بدرجة تسمح بتقدير أدق.
> - **نقطة تمييز:** لا تخلط بين عوامل القياس الخمسة التي تحسب الأس $B$ ومضاعفات الجهد السبعة عشر التي تعدّل الجهد.

---

## Module 5: The Putnam Resource Allocation Model

<div class="page-break"></div>

### Term 11. The Norden/Rayleigh Curve

> **Academic Definition & Technical Specification:**
> **The Norden/Rayleigh curve models the rate of manpower use over project time; its peak occurs at the development-time parameter $t_d$ in the chapter's formulation.**
>
> **Mathematical Formulation & Peak Manning Formula:**
>
> - **1. Instantaneous Manpower Equation:**
>    $$m(t) = 2 K a t \cdot e^{-a t^2} = \frac{K}{t_d^2} t \cdot e^{-t^2 / (2 t_d^2)} \text{ [Persons]}$$
>    Where $K$ is total lifecycle effort in Person-Years, $t_d$ is development time (time of peak manpower), and $a = \frac{1}{2 t_d^2}$.
> - **2. Verified Peak Manning ($m_0$ at $t = t_d$):**
>    $$m_0 = \frac{K}{t_d \sqrt{e}} \approx 0.6065 \frac{K}{t_d} \text{ [Persons]}$$
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.6.1, printed pp. 182–185; Companion Slides 123–135.*

<!--
> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** يصف المنحنى تغير معدل استخدام القوى العاملة بمرور الزمن، ويصل إلى الذروة عند $t_d$ وفق هذه الصيغة.
> - **نقطة تمييز:** عند التعويض في صيغة الذروة، العامل هو $\sqrt{e}$.
-->

---

<div class="page-break"></div>

### Term 12. Difficulty and Manpower Build-Up Metrics ($D$, $D_0$)

> **Academic Definition & Technical Specification:**
> **The difficulty metric $D$ is defined as total effort divided by the square of development time; the distinct manpower build-up metric $D_0$ is total effort divided by the cube of development time.**
>
> **Mathematical Formulation:**
>
> - **1. Difficulty Index:**
>    $$D = \frac{K}{t_d^2} \text{ [Persons/Year]}$$
> - **2. Manpower Build-Up Metric:**
>    $$D_0 = \frac{K}{t_d^3} \text{ [Persons/Year}^2\text{]}$$
> - **3. Empirical Values shown in the course:**
>    - $D_0=8$: new software with many interfaces/interactions.
>    - $D_0=15$: new standalone software.
>    - $D_0=27$: rebuilding existing software.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.6.2, printed pp. 185–187; Companion Slides 136–145.*

<!--
> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** الصعوبة $D$ تقسم الجهد على مربع الزمن، أما مؤشر بناء القوى العاملة $D_0$ فيقسمه على مكعب الزمن.
> - **فخ الامتحان:** لا تبدّل الرمزين: $D=K/t_d^2$ بوحدة persons/year، و$D_0=K/t_d^3$ بوحدة persons/year$^2$. قيم 8 و15 و27 أمثلة يوردها المصدر وليست حدود خطر عامة.
-->

---

<div class="page-break"></div>

### Term 13. Productivity Versus Difficulty

> **Academic Definition & Technical Specification:**
> **Productivity Versus Difficulty represents Putnam's empirical derivation demonstrating that overall software productivity is inversely related to project difficulty, scaled by an organizational technology factor.**
>
> **Mathematical Formulation:**
>
> - **1. Putnam's Productivity Relation:**
>    $$P = \frac{S}{K} = C_k \cdot D^{-2/3}$$
>    Where $S$ is delivered source lines of code, $K$ is total effort, $C_k$ is the technology factor, and $D$ is project difficulty.
> - **2. Engineering Implication:**
>    At fixed size and technology, the Putnam equations relate higher difficulty $D$ to lower modeled productivity $P$.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.6.3, printed pp. 186–187; Companion Slides 146–148, 174–179.*

> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** في علاقة النموذج، ومع تثبيت عامل التقنية، ترتبط زيادة مقياس الصعوبة بانخفاض الإنتاجية المقدّرة.
> - **نقطة تمييز:** الأس في العلاقة هو $-2/3$؛ لا تستنتج من المعادلة وحدها أسباباً سلوكية أو إدارية.

---

<div class="page-break"></div>

### Term 14. The Trade-off Between Time Versus Cost

> **Academic Definition & Technical Specification:**
> **The Putnam time–effort relation gives a fourth-power trade-off: for fixed size and technology factor, required effort varies inversely with the fourth power of development time.**
>
> **Mathematical Formulation:**
>
> - **1. The Invariant Relationship:**
>    From Putnam's software equation $S = C_k K^{1/3} t_d^{4/3}$:
>    $$K \cdot t_d^4 = \left(\frac{S}{C_k}\right)^3 = \text{Constant}$$
> - **2. The Fourth-Power Law of Schedule Compression:**
>    $$K \propto \frac{1}{t_d^4}$$
>    Reducing development time to $0.80t_d$ changes modeled effort by a factor of $\frac{1}{(0.80)^4} \approx 2.441$, an increase of about $144.1\%$ under these fixed conditions.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.6.4, printed pp. 187–188; Companion Slides 149–150, 166–173.*

<!--
> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** القانون الحاكم للمقايضة بين الوقت والجهد في هندسة البرمجيات؛ الوقت ليس خطياً، ومحاولة توفير القليل من الوقت تكلف الكثير جداً من الجهد.
> - **نقطة تمييز:** إذا خُفّض الزمن إلى النصف مع ثبات الشروط، يتضاعف الجهد المقدر بمعامل $2^4=16$ وفق علاقة النموذج؛ هذه نتيجة رياضية وليست ضماناً تجريبياً لمشروع واقعي.
-->

---

<div class="page-break"></div>

### Term 15. Development Sub-Cycle

> **Academic Definition & Technical Specification:**
> **The Development Sub-Cycle is the separate development curve used to model effort through delivery; the source relates its total effort $K_d$ to full-project effort by $K=6K_d$. The full-project Rayleigh curve's cumulative effort at $t_d$ is a different quantity, approximately $0.3935K$.**
>
> **Mathematical Formulation:**
>
> - **1. Mathematical Integration:**
>    $$E(t_d)=\int_0^{t_d}m(t)dt=K(1-e^{-1/2})\approx0.3935K$$
> - **2. Development Sub-Cycle Effort:**
>    $$K=6K_d \quad \Longrightarrow \quad K_d=K/6$$
> - **3. Development-Curve Timing:**
>    $$t_{od}=t_d/\sqrt6$$
> - The cumulative effort $E(t_d)$ on the full-project curve and the separately defined development-sub-cycle effort $K_d$ are different quantities.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.6.5, printed pp. 188–191; Companion Slides 151–165.*

> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** التمييز بين مرحلة التطوير ومرحلة الصيانة في دورة حياة النظام؛ لا تساوِ بين الجهد التراكمي على منحنى المشروع حتى $t_d$ ($\approx0.3935K$) وبين جهد دورة التطوير $K_d=K/6$.
> - **فخ الامتحان:** انتبه للتفريق في الرموز: $K$ هو الجهد الكلي لدورة الحياة الكاملة، بينما $K_d$ هو جهد مرحلة التطوير فقط. عند حساب ذروة مرحلة التطوير، تأكد من استخدام $K_d$ في المعادلة.

---

## Module 6: Software Risk Management

<div class="page-break"></div>

### Term 16. What is Risk?

> **Academic Definition & Technical Specification:**
> **A software risk is a potential future problem involving uncertainty and possible loss to project objectives such as cost, schedule, or technical performance.**
>
> **Mathematical Formulation — Risk Exposure (RE):**
>
> - **1. Quantitative Risk Exposure:**
>    $$RE = P \times L \quad (\text{or } RE = \text{Probability} \times \text{Impact})$$
>    Where $P$ is probability ($0.0 \text{ to } 1.0$) and $L$ is financial or schedule loss.
> - **2. Known vs. Predictable vs. Unpredictable Risks:**
>    - **Known Risks:** Uncovered after careful evaluation of project plan and constraints (e.g., unrealistic delivery date).
>    - **Predictable Risks:** Extrapolated from past project history (e.g., staff turnover).
>    - **Unpredictable Risks:** Events that cannot reasonably be identified in advance from available project information.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.7, printed p. 194; Companion Slides 180–183.*

<!--
> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** الخطر احتمال لمشكلة مستقبلية قد تلحق خسارة بأهداف المشروع.
> - **نقطة تمييز:** يستخدم الفصل $RE=P\times L$ لتمثيل التعرض للخطر؛ لا تختزل قرار الأولوية في رقم واحد إذا كان السؤال يطلب مناقشة السياق.
-->

---

### Term 17. Typical Software Risks

> **Academic Definition & Technical Specification:**
> **Typical Software Risks are recurring threats that may prevent a software project from meeting its objectives. The chapter groups examples into five categories.**
>
> **The five categories and examples are:**
>
> - **Dependencies on outside agencies or factors:** Availability of trained, experienced people; customer-furnished items or information.
> - **Requirement issues:** Lack of clear product vision; unprioritized or changing requirements.
> - **Management issues:** Inadequate planning; unclear project ownership; poor communication.
> - **Lack of knowledge:** Inadequate training or application-domain experience.
> - **Other risk categories:** Turnover of essential personnel; inadequate testing facilities; unachievable performance requirements.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.7.2, printed pp. 195–196; Companion Slides 184–189.*

> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** أمثلة على فئات مخاطر قد تظهر في مشاريع البرمجيات.
> - **فخ الامتحان:** هذه هي فئات الفصل الخمس؛ لا تستبدلها بقائمة مخاطر من تصنيف أو كتاب آخر.

---

<div class="page-break"></div>

### Term 18. Risk Management Activities

> **Academic Definition & Technical Specification:**
> **The chapter groups risk-management activities into Risk Assessment and Risk Control. Assessment consists of Risk Identification, Risk Analysis, and Risk Prioritization; Control consists of Risk Management Planning, Risk Resolution, and Risk Monitoring.**
>
> **The Two-Phase Framework:**
>
> - **1. Risk Assessment:**
>    - **Risk Identification:** Uncovering project hazards using checklists, interviews, and taxonomies.
>    - **Risk Analysis:** Estimating probability ($P$) and loss ($L$).
>    - **Risk Prioritization:** Ranking hazards via Risk Exposure ($RE = P \times L$).
> - **2. Risk Control:**
>    - **Risk Management Planning:** Preparing a plan for dealing with each significant risk.
>    - **Risk Resolution:** Executing the plan for dealing with a risk.
>    - **Risk Monitoring:** Tracking risks during the project.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.7.3, printed pp. 196–198; Companion Slides 188–193.*

<!--
> [!NOTE]
> **الشرح المفاهيمي وفخ الامتحان:**
>
> - **مفهوم المصطلح:** يقسم الفصل أنشطة إدارة المخاطر إلى **Risk Assessment** و**Risk Control**.
> - **نقطة تمييز:** Assessment يشمل identification وanalysis وprioritization؛ Control يشمل planning وresolution وmonitoring.
-->

---

<div class="page-break"></div>

<!--
## Retrieval Set & Active Recall Self-Test

Use this ledger for structured active recall:
-->
1. State the exact difference between Physical LOC and Logical SLOC, citing why LOC is language-dependent.
2. Write down the 5 information domain characteristics of Albrecht's FPA and their Average complexity weights from memory.
3. Compare the leading coefficients and exponents of Basic COCOMO across Organic, Semidetached, and Embedded modes.
4. Explain how COCOMO II calculates its scaling exponent $B$ from the 5 scale factors ($B = 0.91 + 0.01 \sum SF$).
5. Re-derive the Rayleigh peak manpower equation $m_0 = \frac{K}{t_d \sqrt{e}}$ and state Putnam's fourth-power law of time-effort trade-off ($K \propto t_d^{-4}$).
6. Define Risk Exposure ($RE = P \times L$) and contrast Risk Assessment with Risk Control.
