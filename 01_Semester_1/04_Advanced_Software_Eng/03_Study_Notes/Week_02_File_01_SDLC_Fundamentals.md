---
title: "ASE Week 02 — File 01 of 10: SDLC Fundamentals — why a process exists at all"
subject: "04_Advanced_Software_Eng"
week: 2
file: "01 of 10"
source: "Sommerville pp.44–46 · Mall pp.67–71"
created: "2026-09-23"
---

# File 01 of 10 — SDLC Fundamentals

> **Sources.** Sommerville, *Software Engineering* 9th ed., pp.44–46. Mall, *Fundamentals of Software Engineering* 4th ed., pp.67–71.
> **Page numbers are PDF page numbers**, not printed page numbers — the front-matter offset differs between the two books.

---

## Where this sits

**This is the first file. Nothing comes before it.**

The whole series rests on one fact: **software is built by teams, not by one person.** A single programmer writing a small program can succeed with no process at all. A team cannot — and that is the problem this file names.

**The question this file answers:** *why does a software team need a defined process in the first place?*

**The question it hands to File 02:** *fine — a process is needed. What should the first process look like?* The obvious answer is "decide everything up front", and that answer has a name: the waterfall model.

---

## 1. Software life cycle — the idea borrowed from biology

**EN.** Mall opens by borrowing an analogy rather than a definition. All living organisms undergo a life cycle: a seed germinates, grows into a full tree, and finally dies. The term **software life cycle** is defined on that model.

> **Verbatim (Mall p.67):** *"the term **software life cycle** has been defined to imply the different stages (or phases) over which a software evolves from an initial customer request for it, to a fully developed software, and finally to a stage where it is no longer useful to any user, and then it is discarded."*

And the crisp one-line version:

> **Verbatim (Mall p.68):** *"The **life cycle of a software** represents the series of identifiable stages through which it evolves during its life time."*

**AR.** Mall ما يبلش بتعريف — يبلش بتشبيه. كل كائن حي إله دورة حياة: بذرة تنبت، تكبر شجرة، وبالآخر تموت. والـ**software life cycle** معرَّف على هذا النموذج: من **طلب العميل الأول**، إلى **برنامج مكتمل**، إلى **مرحلة يصير ما يفيد أحد** فيُرمى.

**النقطة المهمة:** الدورة تبلش بـ**طلب** ومو ببرنامج. يعني البرنامج ما موجود بالسؤال الأصلي — العميل عنده **حاجة غامضة** مو مواصفات.

Mall يضيف (p.67): *"the customers are usually not clear about all the features that would be needed, neither can they completely describe the identified features in concrete terms, and can only vaguely describe what is needed."*

**AR.** وهذا **مفتاح السلسلة كلها**: العميل **مو واضح** شنو يريد بالضبط. احفظ هذه الجملة — منها راح تطلع كل مشكلة بكل الملفات الجاية.

---

## 2. Software process — the definition and the four activities

**EN.** Sommerville gives the working definition:

> **Verbatim (Sommerville p.45):** *"A **software process** is a set of related activities that leads to the production of a software product."*

And then the part that matters most — **four activities that every process must include, whatever its shape** (Sommerville p.45):

| # | Activity | Verbatim definition |
|:---:|:---|:---|
| 1 | **Software specification** | *"The functionality of the software and constraints on its operation must be defined."* |
| 2 | **Software design and implementation** | *"The software to meet the specification must be produced."* |
| 3 | **Software validation** | *"The software must be validated to ensure that it does what the customer wants."* |
| 4 | **Software evolution** | *"The software must evolve to meet changing customer needs."* |

Sommerville is explicit that this is the invariant: *"In some form, these activities are part of all software processes."*

**AR.** الـ**software process** = مجموعة أنشطة مترابطة تؤدي لمنتج برمجي. بس الأهم: **أربعة أنشطة موجودة بكل عملية مهما كان شكلها** — **specification** (شنو نريد)، **design & implementation** (نبني)، **validation** (نتأكد إنه يسوي اللي يريده العميل)، **evolution** (يتطوّر مع تغيّر الاحتياج).

**ليش هذا مهم؟** لأن من هنا تنقارن النماذج. كل نموذج بالملفات الجاية هو **طريقة مختلفة لترتيب هذه الأربعة** — بس. يعني: نموذجين مختلفين ممكن يكونون نفس الأنشطة بترتيب مختلف. هذا اللي يجعل المقارنة ممكنة.

**احفظ الأربعة بترتيبها** — هي العمود الفقري للمحاضرة.

### 2.1 What else a process description carries

**EN.** Sommerville adds that a process is not only its activities. A process description also contains (p.45):

| Element | Verbatim |
|:---|:---|
| **Products** | *"which are the outcomes of a process activity. For example, the outcome of the activity of architectural design may be a model of the software architecture."* |
| **Roles** | *"which reflect the responsibilities of the people involved in the process. Examples of roles are project manager, configuration manager, programmer, etc."* |
| **Pre- and post-conditions** | *"which are statements that are true before and after a process activity has been enacted or a product produ[ced]."* |

**AR.** العملية مو بس أنشطة. بيها هم **products** (المخرجات — مثلاً موديل معماري)، و**roles** (مسؤوليات الناس — مدير مشروع، مدير تهيئة، مبرمج)، و**pre/post-conditions** (شروط صحيحة قبل وبعد النشاط).

**ليش يذكرها؟** لأنه لو سألك «شنو يوصف العملية؟» — الجواب **مو الأنشطة بس**. ثلاثة عناصر + الأنشطة.

---

## 3. SDLC model — and the distinction from a process

**EN.** Mall's term is **SDLC model** (software development life cycle model), and he notes the synonyms:

> **Verbatim (Mall p.68):** *"A **software development life cycle (SDLC) model** (also called **software life cycle model** and **software development process model**) describes the different activities that need to be carried out for t[he software to evolve from one stage to the next]."*

> **Verbatim (Mall p.69):** *"An **SDLC** graphically depicts the different phases through which a software evolves. It is usually accompanied by a textual description of the different activities that need to be carried out during each phase."*

**AR.** الـ**SDLC model** — وهو نفسه **software life cycle model** و**software development process model** (ثلاث تسميات لنفس الشي، احفظهن لأن السؤال ممكن يجي بأي وحدة). يعرّفه Mall من جهتين: **رسم بياني** يبيّن المراحل والانتقالات، **+ وصف نصي** للأنشطة بكل مرحلة.

**النقطة:** الـSDLC **مرسوم** — وإلا صار وصف نصي بس. الرسم جزء من التعريف مو زينة.

### 3.1 Process versus methodology — Mall's subtle distinction

**EN.** This is a distinction worth having, because the two words are used loosely:

> **Verbatim (Mall p.69):** *"the term **process** has a broader scope and addresses either all the activities taking place during software development, or certain coarse grained activities such as design (e.g. design process), testing (test process), etc. Further, a software process not only identifies the specific activities that need to be carried out, but may also prescribe certain **methodology** for carrying out each activity."*

> **Verbatim (Mall p.69):** *"A **methodology**, on the other hand, prescribes a set of steps for carrying out a **specific life cycle activity**. It may also include the rationale and philosophical assumptions behind the set of steps through which the activity is accomplished."*

> **Verbatim (Mall p.69):** *"A software development **process** has a much broader scope as compared to a software development **methodology**."*

**AR.** **Process** أوسع — يغطي كل الأنشطة أو أنشطة كبيرة الحجم (عملية التصميم، عملية الاختبار)، **وقد** يوصي بمنهجية لكل نشاط. أما **Methodology** فهي **مجموعة خطوات لنشاط واحد محدد**، ويمكن تشمل المبرّر والافتراضات الفلسفية وراها.

**المثال اللي يعطيه Mall:** عملية التصميم ممكن توصي إن مرحلة التصميم العالي تُسوّى بـ*Hatley and Pirbhai's structured analysis and design methodology*.

**قاعدة الحفظ:** **Process = الإطار الأوسع · Methodology = خطوات نشاط واحد.** لو سألك «شنو الفرق؟» — الأوسع مقابل الأخص.

Mall يضيف جملة مهمة: *"several development processes may fit the same SDLC"* (p.69).

**AR.** يعني **الـSDLC واحد وممكن أكثر من عملية تنسجم وياه**. الـSDLC هو **الهيكل**، والعملية هي **التنفيذ**.

---

## 4. Why a life-cycle model is needed at all

**EN.** This is the argument that makes the whole lecture necessary. Mall sets it up with a contrast.

**Case one — one programmer, a small program.** Mall's example is a student doing a classroom assignment:

> **Verbatim (Mall p.70):** *"The student might succeed even when he does not strictly follow a specific development process and adopts a **build and fix** style of development."*

**Case two — a team, professional software.** Mall describes what happens when team members are given freedom:

> **Verbatim (Mall p.70):** *"It is possible that one member might start writing the code for his part while making assumptions about the input results required from the other parts, another might decide to prepare the test documents first, and some other developer might start to carry out the design for the part assigned to him. In this case, severe problems can arise in **interfacing the different parts** and in **managing the overall development**."*

And the verdict:

> **Verbatim (Mall p.70):** *"Therefore, ad hoc development turns out to be is a sure way to have a failed project. Believe it or not, this is exactly what has caused many project failures in the past!"*

> **Verbatim (Mall p.71):** *"use of a suitable SDLC is essential for a professional software development project involving team effort to succeed."*

**AR.** Mall يقابل حالتين:
1. **مبرمج واحد، برنامج صغير** — ممكن ينجح حتى بلا عملية (بأسلوب **build and fix**). مثاله: طالب يحل واجب صف.
2. **فريق، برنامج احترافي** — لو أعطيت كل واحد حرية، واحد يبلش يكتب كود بافتراضات عن مخرجات الأجزاء الثانية، وواحد يبلش بمستندات الاختبار، وواحد بالتصميم. النتيجة: **مشاكل شديدة بالواجهات بين الأجزاء وبإدارة التطوير ككل**.

**والحكم:** التطوير العشوائي = **طريق مضمون لمشروع فاشل**، و**هذا بالضبط سبب كثير من فشل المشاريع بالماضي**.

**الجملة اللي تنحفظ:** *"use of a suitable SDLC is essential for a professional software development project involving team effort to succeed."*

**يعني:** الـSDLC مو ترف. هو شرط نجاح لما يكون الشغل **فريق**.

---

## 5. The two poles — plan-driven and agile

**EN.** Before the models, Sommerville gives the axis they sit on:

> **Verbatim (Sommerville p.46):** *"Sometimes, software processes are categorized as either **plan-driven** or **agile** processes. **Plan-driven processes** are processes where **all of the process activities are planned in advance** and progress is measured against this plan. In **agile processes** … **planning is incremental** and it is easier to change the process to reflect changing customer requirements."*

And the crucial qualifier — there is no universal winner:

> **Verbatim (Sommerville p.46):** *"As Boehm and Turner (2003) discuss, **each approach is suitable for different types of software**. Generally, you need to find a balance between plan-driven and agile processes."*

Sommerville then gives the rule of thumb (p.46): *"For critical systems, a very structured development process is required. For business systems, with rapidly changing requirements, a less formal, flexible process is likely to be more effective."*

**AR.** قبل ما نبلش بالنماذج، Sommerville يعطينا **المحور** اللي تترتب عليه:

| | Plan-driven | Agile |
|:---|:---|:---|
| التخطيط | **كل الأنشطة مخططة مسبقاً**، والتقدّم يُقاس على الخطة | **تخطيط تزايدي**، وأسهل تغيّر العملية |
| يناسب | الأنظمة الحرجة | أنظمة العمل سريعة التغيّر |

**والنقطة الأهم:** *"each approach is suitable for different types of software"* — **ما موجود فائز واحد**. تحتاج توازن. وهذي الجملة هي **بذرة الملف 09** (اختيار النموذج).

---

## 6. The thread the whole series hangs on

**EN.** Sommerville states this chapter's own learning objective as (p.44):

> **Verbatim:** *"I understand **why processes should be organized to cope with changes in the software requirements and design**."*

And Mall states the same thing in a different place — when explaining where agile came from (p.67):

> **Verbatim:** *"The genesis of the agile model can be traced to the **radical changes to the types of project that are being undertaken at present**, rather than to any radical innovations to the life cycle models themselves. The projects have changed from **large multi-year product development projects to small services projects** now."*

**AR.** **هذا أهم شي بالملف كله.** Sommerville يقول صراحة إن هدف الفصل: **نفهم ليش لازم تنظَّم العمليات حتى تتحمّل التغيّرات بالمطلوبات والتصميم.**

وMall يقول شي أعمق: **ظهور Agile ما جاء من اختراع جديد** — جاء من **تغيّر نوع المشاريع نفسها**، من مشاريع منتج كبيرة تدوم سنوات إلى مشاريع خدمات صغيرة.

**يعني الخيط اللي يربط الملفات العشرة:**

> **المطلوبات تتغيّر دائماً. كل نموذج هو جواب على هذه المشكلة — والنماذج تختلف فقط في *متى* و*كيف* تتحمّل التغيّر.**

**AR.** وهذا اللي يجعل الملفات العشرة **حكاية واحدة** مو عشر مواضيع مفترقة. كل نموذج جاي هو **رد على ضعف النموذج اللي قبله**.

---

## Source notes

| Source | Verdict for this file |
|:---|:---|
| **Sommerville p.44–46** | **Primary for §2 and §5.** The four fundamental activities, the products/roles/pre-post-conditions list, and the plan-driven/agile axis are all his, and all verbatim. |
| **Mall p.67–71** | **Primary for §1, §3 and §4.** The life-cycle definition, the SDLC definition, the process-vs-methodology distinction, and the team-failure argument are his, and Sommerville does not have them. |
| **Pressman / Agarwal** | **Add nothing here.** Both restate the four phases without the definitional precision or the team argument. |
| `[THIN]` | **The process-versus-methodology distinction rests on Mall alone.** I could not check it against Sommerville, who does not draw it. If the doctor asks about it, Mall p.69 is the only authority you have. |
| Note | Mall also carries an important line at p.67: *"several development processes may fit the same SDLC."* I have not verified how Mall develops that claim later in the chapter. |

---

## Retrieval set

> Answers are given directly beneath each question, as agreed. **Cover the answer, produce your own, then compare.**

**1. Define the software life cycle, and name both ends of it.**
> The series of identifiable stages through which software evolves during its lifetime. It begins with an **initial customer request** and ends when the software is **no longer useful to any user** and is discarded. (Mall p.67–68)

**2. Name the four fundamental activities of a software process, in order.**
> **Specification · design and implementation · validation · evolution.** Sommerville states that in some form these are part of *all* software processes. (Sommerville p.45)

**3. A process description is not only its activities. What else does it contain?**
> **Products** (the outcomes of an activity — e.g. an architecture model), **roles** (responsibilities — e.g. project manager, configuration manager, programmer), and **pre- and post-conditions** (statements true before and after an activity is enacted). (Sommerville p.45)

**4. What is the difference between a process and a methodology?**
> **Process** has the broader scope — it covers all the activities of development, or coarse-grained activities such as the design process or test process, and it may prescribe a methodology for each activity. **Methodology** prescribes a set of steps for carrying out one specific life-cycle activity, and may include the rationale and assumptions behind those steps. (Mall p.69)

**5. Why can one programmer succeed without a process while a team cannot?**
> Because the team failure is not about individual skill — it is about **coordination**. If each member works by their own assumptions, the failures land in **interfacing the different parts** and in **managing the overall development**. Mall's verdict: *"ad hoc development turns out to be is a sure way to have a failed project."* (Mall p.70)

**6. Define plan-driven and agile processes, and say which one wins.**
> **Plan-driven:** all process activities are planned in advance and progress is measured against the plan. **Agile:** planning is incremental and the process is easier to change. **Neither wins** — each suits different types of software, and a balance is needed. Critical systems need structure; business systems with rapidly changing requirements need flexibility. (Sommerville p.46)

**7. State the one problem that the whole series of models is trying to solve.**
> That **requirements change**. Sommerville states the chapter objective as understanding *why processes should be organised to cope with changes in requirements and design*; every model that follows is a different answer to *when* and *how* the change is absorbed. (Sommerville p.44; Mall p.67)

---

## Page anchors

| Revisit | For |
|:---|:---|
| **Sommerville p.44** | The chapter objectives — including the "cope with change" thread |
| **Sommerville p.45** | Software process definition · the four activities · products/roles/pre-post-conditions |
| **Sommerville p.46** | Software process model definition · plan-driven vs agile · the Boehm and Turner balance point |
| **Mall p.67** | The biological analogy · the life-cycle definition · the agile genesis (project types changed) |
| **Mall p.68** | The one-line life-cycle definition · the SDLC model definition and its synonyms |
| **Mall p.69** | The graphical SDLC definition · **process vs methodology** · "several processes may fit the same SDLC" |
| **Mall p.70–71** | The team-failure argument · the build-and-fix contrast · why a documented process is needed |

---

*File 01 of 10. Built 2026-09-23 under `Week_02_BUILD_PLAN.md`. Every claim is page-anchored; quotations are verbatim; the `[THIN]` flag marks where the summary is thinner than the source.*
