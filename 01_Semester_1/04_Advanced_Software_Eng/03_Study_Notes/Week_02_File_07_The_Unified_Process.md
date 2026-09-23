# File 07 — The Unified Process: Putting It All Together

> **Subject · Week · File:** 04_Advanced_Software_Eng · Week 02 · File 7 of 10 · The Unified Process (UP / RUP)
> **Sources:** Mall §8.3.1 p.475–476 (primary — phases, use-case-driven); Sommerville §2.4 p.67–70 (phases, six best practices, workflows, three perspectives).

---

## WHERE THIS SITS

**File 06 (Spiral)** closed on a limitation of its own: the spiral is a **powerful way of thinking about risk**, but it is *not a ready-made framework* a team can adopt on Monday morning. It tells you to attack risk each loop — it does not package the work into named phases, practices, and workflows.

**This file answers:** can the good ideas from every earlier model be combined into **one adoptable framework**? The Unified Process (UP, or RUP in its Rational flavour) is the attempt to do exactly that — it is, in Sommerville's words, **a hybrid model** that "brings together elements from all of the generic process models." [Foundational Knowledge / Standard Concept]

**The connective tissue:** UP reuses, in one package — prototyping (inception), iterative risk-reduction (elaboration ~ spiral), incremental delivery (construction), and deployment-as-part-of-process (transition). It is the "put it all together" chapter the narrative spine promised.

---

## 1. What the Unified Process Is

**Verbatim (Mall p.475):**

> Unified process is incremental in iterative process model for object-oriented software development that has gained acceptance among the practitioners and academicians. The first book to describe the unified process was titled "The Unified Software Development Process" and was published in 1999 by Ivar Jacobson, Grady Booch and James Rumbaugh.

**Verbatim (Mall p.475):**

> The two main characteristics of the unified process are: **use case-driven** and **iterative**.

**AR.** تعريفان أساسيان:
1. **موجّه بـuse cases** — الـuse cases (وجهة نظر العميل) هي **العرض المركزي والأهم**. كل النماذج اللاحقة لازم **تتوافق مع نموذج الـuse case**.
2. **تكراري (iterative)** — يتطوّر عبر تكرارات قصيرة مو دفعة واحدة.

**Verbatim (Mall p.475):**

> The use case model is the central model. All models that are constructed in the subsequent design activities must conform to the use case model.

**AR.** Mall يصرّح: نموذج الـuse case هو **المركزي** — وكل نماذج التصميم (class diagram، interaction، الخ) لازم **تلتزم بيه**. هذا يفرّق UP عن باقي النماذج اللي تبدأ بالمطلوبات النصية (SRS).

**Verbatim (Sommerville p.67):**

> The Rational Unified Process (RUP) (Krutchen, 2003) is an example of a modern process model... it is a good example of a **hybrid process model**. It brings together elements from all of the generic process models (Section 2.1), illustrates good practice in specification and design (Section 2.2) and supports prototyping and incremental delivery (Section 2.3).

**AR.** Sommerville يؤكد طبيعة UP كـ**نموذج هجين** — يجمع عناصر من كل النماذج العامة. هذي هي "put it all together" بالمعنى الحرفي.

**[THIN]** — Mall does not use the word "hybrid"; that framing is Sommerville's. Mall frames UP by its two characteristics (use-case-driven, iterative) and its OO focus. Both are correct cuts — recorded so a student does not read them as contradictions. [Source Difference]

### UP vs RUP — the naming

**Verbatim (Mall p.475):**

> authors affiliated with Rational Software Corporation have favoured the name rational unified process (RUP).

**AR.** **UP** = الاسم العام؛ **RUP** = النسخة المرتبطة بـRational Software. الامتحان قد يذكر أحدهما — كلاهما نفس النموذج.

---

## 2. The Four Phases — Mall and Sommerville Side by Side

**Per the agreed plan, the two accounts are shown side by side and NOT merged.** Both books name the same four phases; they weight the *content* of each differently. [Source Difference]

**Verbatim (Sommerville p.67):**

> The RUP is a phased model that identifies four discrete phases in the software process. However, unlike the waterfall model where phases are equated with process activities, the phases in the RUP are more closely related to **business rather than technical concerns**.

**AR.** نقطة Sommerville الجوهرية: مراحل UP **متعلقة بالأعمال (business) مو بالتقنية** — عكس Waterfall اللي يربط كل مرحلة بنشاط تقني. وهذا يعني **المرحلة ≠ النشاط** — نفس النشاط (مثل المتطلبات) ممكن يصير بأكثر من مرحلة.

### 2.1 Inception

| **Mall p.476** | **Sommerville p.67** |
|:---|:---|
| "the scope of the project is defined and **prototypes may be developed** to form a clear idea about the project." | "The goal of the inception phase is to **establish a business case** for the system. You should identify all external entities (people and systems) that will interact with the system and define these interactions... assess the contribution that the system makes to the business. If this contribution is minor, then the project may be cancelled after this phase." |

**AR.** Mall يركّز على **النطاق + النماذج الأولية**؛ Sommerville يركّز على **الحالة التجارية (business case)** — ولهذا قد **يُلغى المشروع** إذا كان مساهمته ضئيلة. التكامل: النموذج الأولي يساعد بتوضيح النطاق اللي بدوره يبرر الحالة التجارية.

### 2.2 Elaboration — THE FLAGGED DISAGREEMENT (shown, not merged)

**Verbatim (Mall p.476):**

> In this phase, the functional and the non-functional requirements are captured. **The preliminary use case and the domain model are developed** during this phase.

**Verbatim (Sommerville p.68):**

> The goals of the elaboration phase are to **develop an understanding of the problem domain, establish an architectural framework for the system, develop the project plan, and identify key project risks**. On completion of this phase you should have a requirements model for the system, which may be a set of **UML use-cases**, an architectural description, and a development plan for the software.

**AR.** **هذا هو الاختلاف المعلّم بالخطة** — والاثنان **مو متناقضين**، بل يشدّان على جوانب مختلفة:
- **Mall:** المطلوبات (وظيفية + غير وظيفية) + **use case مبدئي** + **domain model**.
- **Sommerville:** فهم مجال المشكلة + **الإطار المعماري** + **خطة المشروع** + **المخاطر الرئيسية** + (عند الإنجاز) نموذج مطلوبات (UML use-cases) + وصف معماري + خطة تطوير.

**القاعدة:** كلاهما يذكر **use cases**، بس Sommerville يضيف **الإطار المعماري والمخاطر** (يربط بـFile 06!)، بينما Mall يضيف **الـdomain model** (يربط بـOOAD). لو السؤال گال «حسب Mall» — جاوب بمطلوبات + use case + domain model. لو گال «حسب Sommerville» — جاوب بمجال + إطار معماري + خطة + مخاطر. [Source Difference]

### 2.3 Construction

| **Mall p.476** | **Sommerville p.68** |
|:---|:---|
| "the design and implementation activities are carried out. **Full text descriptions of use cases are written** and each use case is taken up for the start of a new iteration. System features are implemented in a series of **short iterations** and are tested. **Each iteration results in an executable release** of the software." | "The construction phase involves **system design, programming, and testing. Parts of the system are developed in parallel and integrated** during this phase. On completion of this phase, you should have a **working software system and associated documentation** that is ready for delivery to users." |

**AR.** اتفاق واسع: تصميم + برمجة + اختبار + **إصدار تنفيذي (executable release) بكل تكرار**. Mall يشدّ على **الـuse case الكامل النصي** كوحدة تكرار؛ Sommerville يشدّ على **التطوير المتوازي + الدمج**.

### 2.4 Transition

| **Mall p.476** | **Sommerville p.68** |
|:---|:---|
| "the product is **installed in the user's environment and maintained**." | "The final phase of the RUP is concerned with **moving the system from the development community to the user community and making it work in a real environment**. This is something that is ignored in most software process models but is, in fact, an **expensive and sometimes problematic activity**. On completion... a documented software system that is working correctly in its operational environment." |

**AR.** اتفاق: النقل للبيئة الحقيقية + الصيانة. Sommerville يضيف نقطة مهمة: **النشر متجاهَل بأغلب النماذج** لكنه **مكلف ومشكلة أحياناً** — وهذا «الابتكار» الأساسي بـUP (انظر §5).

---

## 3. Two-Level Iteration (Sommerville-only depth)

**Verbatim (Sommerville p.68):**

> Iteration within the RUP is supported in two ways. Each phase may be enacted in an iterative way with the results developed incrementally. In addition, the whole set of phases may also be enacted incrementally, as shown by the looping arrow from Transition to Inception in Figure 2.12.

**AR.** تكرار **بمستويين**:
1. **داخل كل مرحلة** — المرحلة نفسها تُنفّذ تكرارياً.
2. **عبر كامل المجموعة** — المراحل كلها تتكرر (سهم Transition → Inception)، يعني **دورة كاملة جديدة** بعد التسليم.

**[THIN]** — Mall describes construction as "a series of short iterations" but does not describe the *whole-set* iteration (looping back from Transition to Inception). That second level is Sommerville-only. [Source Difference]

---

## 4. The Three Perspectives (Sommerville-only)

**Verbatim (Sommerville p.67):**

> The RUP is normally described from three perspectives: 1. A **dynamic perspective**, which shows the phases of the model over time. 2. A **static perspective**, which shows the process activities that are enacted. 3. A **practice perspective**, which suggests good practices to be used during the process.

**AR.** ثلاث زوايا لفهم UP:
- **ديناميكية** = المراحل عبر الزمن (Inception → Elaboration → Construction → Transition).
- **ساكنة** = الأنشطة التقنية (workflows) — تشتغل بكل المراحل.
- **ممارسة** = أفضل الممارسات (الست اللي بالقسم 5).

**[THIN]** — Mall presents UP only through the dynamic/phase lens (and the use-case lens); the three-perspective decomposition is Sommerville's. Recorded so a student knows Mall alone will not supply "three perspectives." [Source Difference]

---

## 5. The Six Best Practices (Sommerville-only)

**Verbatim (Sommerville p.69):**

> Six fundamental best practices are recommended:
> 1. **Develop software iteratively** — Plan increments of the system based on customer priorities and develop the highest-priority system features early in the development process.
> 2. **Manage requirements** — Explicitly document the customer's requirements and keep track of changes to these requirements. Analyze the impact of changes on the system before accepting them.
> 3. **Use component-based architectures** — Structure the system architecture into components, as discussed earlier in this chapter.
> 4. **Visually model software** — Use graphical UML models to present static and dynamic views of the software.
> 5. **Verify software quality** — Ensure that the software meets the organizational quality standards.
> 6. **Control changes to software** — Manage changes to the software using a change management system and configuration management procedures and tools.

**AR.** الست ممارسات — **كلها من Sommerville**؛ Mall ما يذكرها. وهي تلخّص فلسفة UP:
1. **تطوير تكراري** — حسب أولوية العميل.
2. **إدارة المطلوبات** — توثيق + تتبّع التغيير + تحليل الأثر.
3. **معمارية قائمة على المكونات** (component-based).
4. **نمذجة بصرية بـUML**.
5. **التحقق من الجودة**.
6. **ضبط التغييرات** (configuration management).

**[THIN]** — Mall's account of UP has no "best practices" list. If an exam asks "name the six best practices of RUP," the answer is Sommerville's. [Source Difference]

---

## 6. The Static Workflows (Sommerville-only)

**Verbatim (Sommerville p.69):**

> The core engineering and support workflows are described in Figure 2.13. [Six core process workflows:] Business modelling, Requirements, Analysis and design, Implementation, Testing, Deployment. [Three supporting workflows:] Configuration and change management, Project management, Environment.

**AR.** الـ**workflows** (الأنشطة الساكنة) — ستة أساسية + ثلاثة داعمة. النقطة المهمة (Sommerville p.69–70):

**Verbatim (Sommerville p.70):**

> The advantage in presenting dynamic and static views is that **phases of the development process are not associated with specific workflows**. In principle at least, all of the RUP workflows may be active at all stages of the process. In the early phases of the process, most effort will probably be spent on workflows such as business modelling and requirements and, in the later phases, in testing and deployment.

**AR.** **المرحلة ≠ الـworkflow.** كل الـworkflows ممكن تكون نشطة بكل المراحل — بس التركيز يختلف (بداية = مطلوبات، نهاية = اختبار + نشر). هذي هي «separation of phases and workflows» اللي Sommerville يسميها ابتكار UP الأساسي.

**[THIN]** — Mall does not describe workflows at all; this is entirely Sommerville. [Source Difference]

---

## 7. The Two Key Innovations — and When UP Does NOT Fit

**Verbatim (Sommerville p.70):**

> The most important innovations in the RUP are the **separation of phases and workflows**, and the **recognition that deploying software in a user's environment is part of the process**.

**AR.** ابتكاران: (1) فصل المراحل عن الأنشطة؛ (2) **اعتبار النشر جزء من العملية** (مو شي خارجها). هذا يجاوب على قصور كل النماذج السابقة اللي كانت تنهي عند التسليم.

**Verbatim (Sommerville p.70):**

> The RUP is not a suitable process for all types of development, e.g., **embedded software development**. However, it does represent an approach that potentially combines the three generic process models discussed in Section 2.1.

**AR.** **الضعف/الحد:** UP **مو مناسب لكل شي** — مثال Sommerville: **الأنظمة المضمّنة (embedded)**. و"يجمع النماذج العامة الثلاثة" = Waterfall + Incremental + Reuse-oriented (من §2.1).

**[THIN]** — Mall does not state a "when not suitable" limitation for UP; the embedded-software caveat is Sommerville-only. [Source Difference]

---

## 8. Source Notes

| **Source** | **Role** | **What it adds** | **What it omits** |
|:---|:---|:---|:---|
| **Mall p.475–476** | **Primary** | UP definition (OO, use-case-driven, iterative); the four phases with Mall's wording; the domain-model emphasis in Elaboration; UP vs RUP naming | No "hybrid" framing; no six best practices; no workflows; no "when not suitable" |
| **Sommerville p.67–70** | Supporting | Hybrid framing; business-not-technical phase nature; **Elaboration with architecture+risks**; two-level iteration; three perspectives; **six best practices**; **static workflows**; **embedded-software limitation** | No domain-model emphasis in Elaboration |

**The decision rule applied (per student instruction):** all sources were read in full before writing. Where Mall and Sommerville describe the four phases, **both accounts are shown side by side** (§2) and the Elaboration difference is presented explicitly (§2.2), not merged. Where Sommerville alone supplies material (six best practices, workflows, three perspectives, the limitation), it is marked `[THIN]` so a student knows Mall will not supply it. Rule 3 (show both, never merge) and Rule 6 ([THIN] flags) honoured. [Source Difference]

---

## 9. Retrieval Set — 16 Items

**[RS-07-01]** What is the Unified Process, and who originated it?
> **Answer:** An incremental and iterative process model for object-oriented software development. First described in *The Unified Software Development Process* (1999) by Jacobson, Booch, and Rumbaugh. "RUP" is the Rational-flavoured name. [Mall p.475]

**[RS-07-02]** What are the two main characteristics of the UP?
> **Answer:** **Use-case-driven** and **iterative**. The use-case model is the central model; all other models must conform to it. [Mall p.475]

**[RS-07-03]** Why is the UP called a "hybrid process model"?
> **Answer:** It brings together elements from all the generic process models (waterfall, incremental, reuse-oriented) and supports prototyping and incremental delivery. [Sommerville p.67]

**[RS-07-04]** Name the four phases of the UP.
> **Answer:** Inception, Elaboration, Construction, Transition. [Mall p.476; Sommerville p.67–68]

**[RS-07-05]** How does the UP differ from the waterfall in how phases relate to activities?
> **Answer:** In the waterfall, phases are equated with process activities; in the UP, phases are related to **business** rather than technical concerns, and the same workflow (e.g., requirements) can be active in multiple phases. [Sommerville p.67]

**[RS-07-06]** What happens in the Inception phase, per Mall vs Sommerville?
> **Answer:** Mall: scope defined, prototypes may be built. Sommerville: establish the **business case**; project may be **cancelled** if its business contribution is minor. [Mall p.476; Sommerville p.67]

**[RS-07-07]** Describe Elaboration — and note the source difference.
> **Answer:** **Mall:** functional + non-functional requirements captured; preliminary use case + domain model developed. **Sommerville:** understand problem domain, establish architectural framework, develop project plan, identify key project risks; deliver a requirements model (UML use-cases), architectural description, development plan. Both mention use cases; they weight different facets. Do not merge. [Mall p.476; Sommerville p.68; Source Difference]

**[RS-07-08]** What happens in Construction?
> **Answer:** Design + implementation + testing; features implemented in short iterations, each yielding an executable release. Sommerville adds: parts developed in parallel and integrated. [Mall p.476; Sommerville p.68]

**[RS-07-09]** What happens in Transition, and why does Sommerville call it an innovation?
> **Answer:** Product installed in the user's environment and maintained. Sommerville: moving the system to the user community is "ignored in most models" yet "expensive and sometimes problematic" — so recognising deployment as *part of the process* is a key UP innovation. [Mall p.476; Sommerville p.68, p.70]

**[RS-07-10]** What are the two levels of iteration in the RUP?
> **Answer:** (1) Each phase enacted iteratively; (2) the whole set of phases enacted incrementally, looping from Transition back to Inception. [Sommerville p.68]

**[RS-07-11]** What are the three perspectives from which the RUP is described?
> **Answer:** Dynamic (phases over time), Static (activities/workflows enacted), Practice (good practices). [Sommerville p.67]

**[RS-07-12]** List the six best practices of the RUP.
> **Answer:** (1) Develop iteratively; (2) Manage requirements; (3) Use component-based architectures; (4) Visually model software (UML); (5) Verify software quality; (6) Control changes to software. [Sommerville p.69]

**[RS-07-13]** What are the RUP workflows (static view)?
> **Answer:** Six core: Business modelling, Requirements, Analysis and design, Implementation, Testing, Deployment. Three supporting: Configuration and change management, Project management, Environment. [Sommerville p.69]

**[RS-07-14]** What is the key innovation of the RUP, according to Sommerville?
> **Answer:** The **separation of phases and workflows**, and the **recognition that deploying software is part of the process**. [Sommerville p.70]

**[RS-07-15]** When is the RUP NOT suitable?
> **Answer:** Not for all development types — e.g., **embedded software development**. [Sommerville p.70; THIN — Mall does not state this]

**[RS-07-16]** If an exam says "according to Mall" vs "according to Sommerville" for the UP, what differs?
> **Answer:** Mall = use-case-driven + iterative, OO focus, four phases with domain-model emphasis, no best-practices/workflows list. Sommerville = hybrid framing, business-not-technical phases, Elaboration with architecture+risks, six best practices, static workflows, embedded limitation. Show both; never merge. [Source Difference]

---

## 10. Page Anchors — Revisit These

- **Mall:** p.475 (UP definition, OO, use-case-driven + iterative, UP vs RUP, use-case model central) · p.476 (four phases: inception/prototypes, elaboration/requirements+use case+domain model, construction/short iterations+executable release, transition/install+maintain)
- **Sommerville:** p.67 (RUP hybrid, four phases business-not-technical, three perspectives, inception business case) · p.68 (elaboration architecture+risks, construction parallel+integrated, transition deployment, two-level iteration) · p.69 (six best practices, static workflows table) · p.70 (key points, two innovations, embedded limitation)

---

**End of File 07.**
