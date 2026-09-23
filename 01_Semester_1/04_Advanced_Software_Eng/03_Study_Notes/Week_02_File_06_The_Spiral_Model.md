# File 06 — The Spiral Model and Risk-Driven Development

> **Subject · Week · File:** 04_Advanced_Software_Eng · Week 02 · File 6 of 10 · The Spiral Model
> **Sources:** Sommerville §2.3.3 p.65–67 (primary); Mall §2.5–§2.5.1 p.114–116; Pressman §2.7.2 p.64–66 (deepest, six-task-region variation).

---

## WHERE THIS SITS

**File 05 (RAD)** closed on a hard limit: RAD buys speed by cutting planning and reusing code, but **it has no mechanism for deciding *which* risk to attack first**. Every model before this — Waterfall, Incremental, RAD, Evolutionary, Prototyping — optimised for *something* (schedule, change, reuse), but **none made risk the driver**.

**This file answers:** what if you optimised the process for *what could go wrong*? That is exactly what Boehm's spiral model does — it makes **risk** the variable that controls the shape of the project. [Foundational Knowledge / Standard Concept]

**The connective tissue (recap from earlier files):**
- From **File 03**: prototyping reduces risk — but only risks *identified up front*. Mall now sharpens this: the spiral builds a prototype at the start of **every** phase, not just the first.
- From **File 02**: Sommerville's "change avoidance vs change tolerance" axis. Sommerville **explicitly** places the spiral on both axes: *"The spiral model combines change avoidance with change tolerance."* (Sommerville p.65) — the only model so far to score on both.
- From **File 05**: RAD = schedule-driven; Spiral = **risk-driven**. The spiral is what RAD is missing.

---

## 1. What the Spiral Model Is — The Definition

**Verbatim (Sommerville p.65):**

> A risk-driven software process framework (the spiral model) was proposed by Boehm (1988). This is shown in Figure 2.11. Here, the software process is represented as a spiral, rather than a sequence of activities with some backtracking from one activity to another. Each loop in the spiral represents a phase of the software process. Thus, the innermost loop might be concerned with system feasibility, the next loop with requirements definition, the next loop with system design, and so on.

**AR.** يعني: بدل ما تكون المراحل **سلسلة خطية** (زي Waterfall) أو **تكرارات منفصلة** (زي Incremental)، الـSpiral يمثّلها كـ**حلزون** — و**كل لفة = مرحلة**. اللفة الأعمق (الداخلية) = الجدوى (feasibility)، واللي بعدها = تعريف المطلوبات، واللي بعدها = التصميم، وهكذا **نبتعد للخارج**.

**Verbatim (Mall p.114):**

> This model gets its name from the appearance of its diagrammatic representation that looks like a spiral with many loops... The exact number of loops of the spiral is not fixed and can vary from project to project.

**AR.** النقطة المهمة: **عدد اللفات مو ثابت** — مدير المشروع يحدده حسب المخاطر. هذا يفرّقه جذرياً عن Waterfall (المراحل خمسة ثابتة) وIncremental (زيادات معدودة).

**Verbatim (Mall p.114):**

> A prominent feature of the spiral model is handling unforeseen risks that can show up much after the project has started.

**AR.** أهم ميزة: يتعامل مع **مخاطر ما انكشفت ببداية المشروع**، وتظهر **بعد** ما يبلش الشغل. هذا هو الفرق الجوهري عن Prototyping (اللي يفترض كل المخاطر تُعرف قبل البدء).

---

## 2. The Core Idea — Risk as the Driver

**Verbatim (Sommerville p.65):**

> The spiral model combines change avoidance with change tolerance. It assumes that changes are a result of project risks and includes explicit risk management activities to reduce these risks.

**AR.** هذا يربط بإطار File 02/03: الـSpiral **يجمع المحورين** — يتجنّب التغيير (بإدارة المخاطر قبل ما تكلّف إعادة العمل) **ويتحمّل التغيير** (عبر لفات متكررة). ويفترض إن **مصدر التغيير = المخاطر** (changes are a result of project risks) — مو تغيّر رأي العميل بس.

**Verbatim (Sommerville p.67):**

> The main difference between the spiral model and other software process models is its explicit recognition of risk.

**AR.** هذي الجملة **امتحانية** — الفرق الوحيد بين Spiral وباقي النماذج هو **الاعتراف الصريح بالمخاطر** (explicit recognition of risk). باقي النماذج يتعاملون مع المخاطر بشكل ضمني أو أبداً.

**Verbatim (Sommerville p.67):**

> Informally, risk simply means something that can go wrong. For example, if the intention is to use a new programming language, a risk is that the available compilers are unreliable or do not produce sufficiently efficient object code. Risks lead to proposed software changes and project problems such as schedule and cost overrun, so risk minimization is a very important project management activity.

**AR.** تعريف المخاطر بشكل غير رسمي: **«أي شي ممكن يغلط»**. مثال Sommerville: تريد تستخدم لغة جديدة → المخاطرة إن المترجمات (compilers) **غير موثوقة** أو **تنتج كود غير فعّال**. والمخاطر تؤدي لتغييرات بالبرنامج **وتجاوزات بالجدول والكلفة** → فتقليل المخاطر = نشاط إداري حرج.

**Verbatim (Mall p.115):**

> A risk is essentially any adverse circumstance that might hamper the successful completion of a software project. As an example, consider a project for which a risk can be that data access from a remote database might be too slow to be acceptable by the customer. This risk can be resolved by building a prototype of the data access subsystem and experimenting with the exact access rate.

**AR.** Mall يقّرّب التعريف بسؤال أداء: الوصول لقاعدة بيانات بعيدة **ممكن يكون بطيء جداً**. والحل = **نموذج أولي (prototype)** للوصول للبيانات نختبر بيه السرعة الفعلية قبل ما نلتزم بالتصميم. هذا يربط للـPrototyping من File 03.

---

## 3. The Three Views of One Loop — DO NOT MERGE

The three books describe the content of **one loop** differently. These are **three views of the same Boehm spiral, at different granularities** — not contradictions, but they are structured differently and a student must recognise all three. [Source Difference]

### View A — Sommerville's Four Sectors (p.66)

**Verbatim:**

> Each loop in the spiral is split into four sectors:
> 1. **Objective setting** — Specific objectives for that phase of the project are defined. Constraints on the process and the product are identified and a detailed management plan is drawn up. Project risks are identified. Alternative strategies, depending on these risks, may be planned.
> 2. **Risk assessment and reduction** — For each of the identified project risks, a detailed analysis is carried out. Steps are taken to reduce the risk. For example, if there is a risk that the requirements are inappropriate, a prototype system may be developed.
> 3. **Development and validation** — After risk evaluation, a development model for the system is chosen. For example, throwaway prototyping may be the best development approach if user interface risks are dominant. If safety risks are the main consideration, development based on formal transformations may be the most appropriate process, and so on. If the main identified risk is sub-system integration, the waterfall model may be the best development model to use.
> 4. **Planning** — The project is reviewed and a decision made whether to continue with a further loop of the spiral. If it is decided to continue, plans are drawn up for the next phase of the project.

**AR.** القطاع الثالث (Development and validation) مهم جداً: **يختار نموذج تطوير مختلف حسب نوع الخطر**. هذا يعني الـSpiral **يحتوي نماذج ثانية جوه** — زي ما Incremental يحتوي Iterative Waterfall (من File 04). لو الخطر بالـUI → prototyping؛ لو السلامة → formal transformations؛ لو التكامل → waterfall. **النماذج مو متنافية — الـSpiral يختار بينها حسب الخطر.**

### View B — Mall's Four Quadrants (p.116)

**Verbatim:**

> Each phase in this model is split into four sectors (or quadrants) as shown in Figure 2.10.
> - **Quadrant 1:** The objectives are investigated, elaborated, and analysed. Based on this, the risks involved in meeting the phase objectives are identified. In this quadrant, alternative solutions possible for the phase under consideration are proposed.
> - **Quadrant 2:** During the second quadrant, the alternative solutions are evaluated to select the best possible solution. To be able to do this, the solutions are evaluated by developing an appropriate prototype.
> - **Quadrant 3:** Activities during the third quadrant consist of developing and verifying the next level of the software. At the end of the third quadrant, the identified features have been implemented and the next version of the software is available.
> - **Quadrant 4:** Activities during the fourth quadrant concern reviewing the results of the stages traversed so far (i.e. the developed version of the software) with the customer and planning the next iteration of the spiral.
> - **The radius of the spiral at any point represents the cost incurred in the project so far, and the angular dimension represents the progress made so far in the current phase.**

**AR.** Mall يضيف تفصيلين مو موجودين بـSommerville:
1. **نصف القطر (radius) = التكلفة المتراكمة**، و**البعد الزاوي (angular) = التقدّم بالمرحلة الحالية**. هذا يجعل الشكل الهندسي للحلزون **مقياساً بصرياً** للكلفة والتقدّم.
2. الربع الرابع يشمل **مراجعة مع العميل** (review with the customer) — وهذا يقرّب الـSpiral من Incremental (تسليم للتعليق).

**Verbatim (Mall p.116):**

> In the spiral model of development, the project manager dynamically determines the number of phases as the project progresses. Therefore, in this model, the project manager plays the crucial role of tuning the model to...

**AR.** دور مدير المشروع **محوري** — هو اللي يحدد عدد اللفات ديناميكياً. هذا يفرّقه عن النماذج الجاهزة.

### View C — Pressman's Six Task Regions (p.64)

**Verbatim:**

> A spiral model is divided into a number of framework activities, also called task regions. Typically, there are between three and six task regions. Figure 2.8 depicts a spiral model that contains six task regions:
> - **Customer communication** — tasks required to establish effective communication between developer and customer.
> - **Planning** — tasks required to define resources, timelines, and other project-related information.
> - **Risk analysis** — tasks required to assess both technical and management risks.
> - **Engineering** — tasks required to build one or more representations of the application.
> - **Construction and release** — tasks required to construct, test, install, and provide user support (e.g., documentation and training).
> - **Customer evaluation** — tasks required to obtain customer feedback based on evaluation of the software representations created during the engineering stage and implemented during the installation stage.

**Verbatim (Pressman p.65):**

> Framework activities apply to every software project you undertake, regardless of size or complexity.

**AR.** Pressman يصرّح إن هاذي **«variation»** على نموذج Boehm الأصلي (footnote p.64: *"The spiral model discussed in this section is a variation on the model proposed by Boehm"*). يعني **الست مناطق = تكييف Pressman، مو النص الأصلي**. وهو يضيف نشاطين ما عند Sommerville/Mall: **Customer communication** و**Customer evaluation** — يعني يقرّب النموذج من Agile (تواصل وتغذية راجعة مستمرة).

### The Correspondence Map (how the three views align)

| **Sommerville (4 sectors)** | **Mall (4 quadrants)** | **Pressman (6 task regions)** | **What happens** |
|:---|:---|:---|:---|
| Objective setting | Q1 (objectives + risks + alternatives) | Customer communication + Planning | Set goals, find risks, plan |
| Risk assessment and reduction | Q2 (evaluate via prototype) | Risk analysis + Engineering | Attack the risk, often by prototyping |
| Development and validation | Q3 (develop & verify next level) | Engineering + Construction and release | Build the increment |
| Planning | Q4 (review with customer + plan next) | Customer evaluation + Planning | Review, decide to continue, plan next loop |

**The rule:** all three describe the **same clockwise loop**: *set objectives → attack the risk → build → review and plan the next loop*. The granularity differs. If an exam question says "according to Sommerville," use the 4-sector wording; if it says "according to Pressman," use the 6-task-region wording. [Source Difference]

---

## 4. The Prototype-at-Every-Phase Distinction (the bridge from File 03)

**Verbatim (Mall p.114–115):**

> please recollect that the prototyping model can be used effectively only when the risks in a project can be identified upfront before the development work starts. As we shall discuss, this model achieves this by incorporating much more flexibility compared to SDLC other models. While the prototyping model does provide explicit support for risk handling, the risks are assumed to have been identified completely before the project start. This is required since the prototype is constructed only at the start of the project. In contrast, in the spiral model prototypes are built at the start of every phase. Each phase of the model is represented as a loop in its diagrammatic representation. Over each loop, one or more features of the product are elaborated and analysed and the risks at that point of time are identified and are resolved through prototyping.

**AR.** هذا هو **الجسر الحرج** مع File 03:
- **Prototyping:** نموذج أولي **واحد ببداية المشروع** → يفترض كل المخاطر معروفة مسبقاً.
- **Spiral:** نموذج أولي **ببداية كل لفة/مرحلة** → يكتشف ويعالج المخاطر **اللي تظهر لاحقاً**.

**القاعدة:** Prototyping = كشف المطلوبات. Spiral = **إدارة المخاطر المستمرة**. والـSpiral يستخدم Prototyping كأداة جوه اللفة، مو كنموذج بديل.

**Verbatim (Pressman p.66):**

> The spiral model uses prototyping as a risk reduction mechanism but, more important, enables the developer to apply the prototyping approach at any stage in the evolution of the product. It maintains the systematic stepwise approach suggested by the classic life cycle but incorporates it into an iterative framework that more realistically reflects the real world.

**AR.** Pressman يؤكد نفس الفكرة: الـSpiral **يحافظ على المنهج المنهجي (systematic) للـWaterfall** لكنه **يدمجه بإطار تكراري** — يعني يجمع انضباط الخطي مع مرونة التكرار.

---

## 5. How the Spiral Relates to Earlier Models — A Summary

| **Earlier model** | **What the Spiral borrows** |
|:---|:---|
| **Waterfall** (File 02) | Used *inside* a loop when the dominant risk is sub-system integration (Sommerville p.66, sector 3) |
| **Prototyping** (File 03) | The risk-reduction mechanism — but applied at *every* phase, not just once |
| **Incremental** (File 04) | Delivers "incremental versions" (Pressman p.64); reviews with customer at each loop (Mall Q4) |
| **Evolutionary** (File 03) | Pressman calls it "an evolutionary software process model" (p.64) — evolves over loops |
| **RAD** (File 05) | RAD is schedule-driven; Spiral adds the *risk-prioritisation* RAD lacks |

**The one-line summary:** the spiral is the **first model that makes risk the control variable**, and it does so by reusing every earlier model as a tool inside its loop. [Foundational Knowledge / Standard Concept]

---

## 6. When the Spiral Fits — and When It Does NOT

### 6.1 When It Fits

**Verbatim (Pressman p.66):**

> The spiral model is a realistic approach to the development of large-scale systems and software. Because software evolves as the process progresses, the developer and customer better understand and react to risks at each evolutionary level.

**AR.** يناسب **الأنظمة الكبيرة** و**عالية المخاطر** — لأنه يجبر الفريق والعميل على **فهم وردّة فعل تجاه المخاطر بكل مستوى تطوّري**.

**Verbatim (Pressman p.65):**

> Unlike classical process models that end when software is delivered, the spiral model can be adapted to apply throughout the life of the computer software... the spiral, when characterized in this way, remains operative until the software is retired.

**AR.** ميزة فريدة: النماذج الكلاسيكية **تنتهي عند التسليم**، لكن الـSpiral **يبقى شغّال طول عمر البرنامج** — حتى بعد التقاعد (retirement). يعني يغطّي **الصيانة والتطوير المستمر** مو بس التطوير الأولي. هذا يربط بصورة Sommerville File 03: *"development and maintenance as a continuum"*.

### 6.2 When It Does NOT Fit (the weaknesses)

**Verbatim (Pressman p.66):**

> It may be difficult to convince customers (particularly in contract situations) that the evolutionary approach is controllable. It demands considerable risk assessment expertise and relies on this expertise for success. If a major risk is not uncovered and managed, problems will undoubtedly occur. Finally, the model has not been used as widely as the linear sequential or prototyping paradigms.

**AR.** ثلاثة عيوب:
1. **صعوبة إقناع العميل** (خاصة بعقود حكومية) إن النهج التطوّري **قابل للضبط** — يذكّر بتعارض الشراء من Files 04/05.
2. **يتطلب خبرة عالية بتقييم المخاطر** — لو ما انكشف خطر كبير → مشاكل حتمية.
3. **أقل انتشاراً** من الخطي أو Prototyping → خبرة أقل بالسوق.

**[THIN]** — Sommerville and Mall do not list explicit "when not to use" weaknesses; Pressman is the only source that does. If an exam asks "disadvantages of the spiral," the answer comes from Pressman. Recorded so a student does not assume Mall/Sommerville supply it.

### 6.3 The WINWIN Extension (Pressman, optional depth)

**Verbatim (Pressman p.66–67):**

> Boehm's WINWIN spiral model [BOE98] defines a set of negotiation activities at the beginning of each pass around the spiral... 1. Identification of the system or subsystem's key "stakeholders." 2. Determination of the stakeholders' "win conditions." 3. Negotiation of the stakeholders' win conditions to reconcile them into a set of win-win conditions for all concerned.

**AR.** نسخة مطوّرة (WINWIN) تضيف **تفاوض مع أصحاب المصلحة** ببداية كل لفة، وتستخدم **ثلاث نقاط ارتكاز (anchor points)**: LCO (Life Cycle Objectives) · LCA (Life Cycle Architecture) · IOC (Initial Operational Capability). هذي **تفصيل متقدم** — مذكور للعمق، مو مطلوب كأساس. [THIN]

---

## 7. Source Notes

| **Source** | **Role** | **What it adds** | **What it omits** |
|:---|:---|:---|:---|
| **Sommerville p.65–67** | **Primary** | The four sectors; the "explicit recognition of risk" sentence; the change-avoidance + change-tolerance placement; the risk = "something that can go wrong" definition | No weaknesses list; no radius/angle detail |
| **Mall p.114–116** | Supporting | Four quadrants; **prototype-at-every-phase** distinction (bridge from File 03); **radius = cost, angle = progress**; project-manager-dynamically-sets-phases | No explicit "when not to use" |
| **Pressman p.64–66** | Deepest | Six-task-region variation; "evolutionary model" framing; **applies throughout software life**; **the only weaknesses list**; WINWIN extension | Explicitly a *variation* on Boehm, not the original |

**The decision rule applied (per student instruction):** the three books describe the loop at different granularities. They were **not merged** — they are shown as three views with a correspondence map (§3). Where they agree (risk is the driver; prototype reduces risk; loop = set→attack→build→review), the agreement is stated. Where they differ in structure (4 sectors vs 4 quadrants vs 6 task regions), both are shown. [Source Difference]

---

## 8. Retrieval Set — 16 Items

**[RS-06-01]** Who proposed the spiral model and in what year?
> **Answer:** Boehm, 1988. [Sommerville p.65]

**[RS-06-02]** What makes the spiral model different from all other process models?
> **Answer:** Its **explicit recognition of risk**. [Sommerville p.67]

**[RS-06-03]** What does "risk" mean informally, according to Sommerville?
> **Answer:** "Something that can go wrong" — e.g., a new language whose compilers are unreliable or produce inefficient object code. Risks cause schedule/cost overruns. [Sommerville p.67]

**[RS-06-04]** How does the spiral model relate to Sommerville's change-avoidance / change-tolerance axis?
> **Answer:** It **combines both** — it assumes changes result from project risks and includes explicit risk-management activities. It is the only model so far to score on both axes. [Sommerville p.65]

**[RS-06-05]** Name Sommerville's four sectors of a spiral loop.
> **Answer:** (1) Objective setting; (2) Risk assessment and reduction; (3) Development and validation; (4) Planning. [Sommerville p.66]

**[RS-06-06]** In sector 3 (Development and validation), how is the development model chosen?
> **Answer:** By the dominant risk — UI risk → throwaway prototyping; safety risk → formal transformations; sub-system integration risk → waterfall. The spiral *contains* other models. [Sommerville p.66]

**[RS-06-07]** What are Mall's four quadrants, and what does the radius/angle represent?
> **Answer:** Q1 objectives+risks+alternatives; Q2 evaluate via prototype; Q3 develop & verify next level; Q4 review with customer + plan next. **Radius = cost so far; angular dimension = progress in current phase.** [Mall p.116]

**[RS-06-08]** How does the spiral's use of prototyping differ from the stand-alone prototyping model (File 03)?
> **Answer:** Stand-alone prototyping builds one prototype at project start (assumes all risks known up front); the spiral builds a prototype at the start of **every** phase, catching risks that emerge later. [Mall p.114–115]

**[RS-06-09]** How many task regions does Pressman's spiral variation have, and what are they?
> **Answer:** Typically 3–6; the six shown are: Customer communication, Planning, Risk analysis, Engineering, Construction and release, Customer evaluation. [Pressman p.64]

**[RS-06-10]** How does Pressman characterise the spiral's relationship to the classic lifecycle?
> **Answer:** It "maintains the systematic stepwise approach suggested by the classic life cycle but incorporates it into an iterative framework." [Pressman p.66]

**[RS-06-11]** Does the spiral model end at software delivery?
> **Answer:** No. Unlike classical models, it "can be adapted to apply throughout the life of the computer software" and remains operative until retirement. [Pressman p.65]

**[RS-06-12]** List the weaknesses of the spiral model (only one source covers these).
> **Answer:** (1) Hard to convince customers (esp. in contract situations) it is controllable; (2) Demands high risk-assessment expertise — undiscovered risk = certain problems; (3) Less widely used than linear or prototyping. [Pressman p.66]

**[RS-06-13]** What is special about the number of loops/phases in the spiral?
> **Answer:** Not fixed — the project manager **dynamically determines** the number of phases as the project progresses. [Mall p.114, p.116]

**[RS-06-14]** What is the WINWIN spiral model?
> **Answer:** Boehm's extension adding stakeholder-negotiation activities at the start of each loop (identify stakeholders → their win conditions → negotiate win-win), with three anchor points (LCO, LCA, IOC). [Pressman p.66–67; THIN depth]

**[RS-06-15]** Why is the spiral particularly suited to large-scale systems?
> **Answer:** Because software evolves as the process progresses, developer and customer better understand and react to risks at each evolutionary level. [Pressman p.66]

**[RS-06-16]** If an exam says "according to Sommerville" vs "according to Pressman," which loop structure do you cite?
> **Answer:** Sommerville → four sectors (objective setting / risk assessment / development & validation / planning). Pressman → six task regions (customer communication / planning / risk analysis / engineering / construction & release / customer evaluation). Do not merge them. [Source Difference]

---

## 9. Page Anchors — Revisit These

- **Sommerville:** p.65 (Boehm, spiral = phase loops, change axis) · p.66 (four sectors, the sector-3 model choice) · p.67 (explicit recognition of risk, risk definition)
- **Mall:** p.114 (name, variable loops, unforeseen risks, prototype-at-every-phase bridge) · p.115 (risk definition, remote-DB example) · p.116 (four quadrants, radius/angle, PM role)
- **Pressman:** p.64 (Boehm 1988, evolutionary + linear coupling, six task regions) · p.65 (framework activities universal, life-long applicability) · p.66 (large-scale fit, weaknesses) · p.66–67 (WINWIN, anchor points)

---

**End of File 06.**
