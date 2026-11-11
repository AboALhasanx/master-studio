---
title: "ASE Chapter 7 — T1 Multiple-Choice Questions Pack"
subtitle: "60 MCQs"
course: "Advanced Software Engineering (CS603)"
instructor: "Asst. Prof. Dr. Ali Fahim Ni'ma"
author: "Master Studio Engine"
date: "2026-10-21"
lang: "en"
---

# Chapter 7: Software Reliability — Multiple-Choice Questions Pack

<!-- Internal inventory: 50 course-slide MCQs (Q7.1–Q7.50) and 10 authored practice MCQs (Q7.51–Q7.60). -->

---

## Section 1: Official Course-Slide MCQs (50 Items)

<div class="no-break">

### Q7.1. Which one is not a phase of "bath tub curve" of hardware reliability?
(a) Burn-in · (b) Useful life · (c) Wear-out · (d) Test-out
{: .keep-next }
> **(d) Test-out**
>
> **The classical hardware reliability "bathtub curve" depicts failure rate over time across three distinct operational phases:**
>
> 1. **Burn-in phase (Infant mortality):** **Characterized by an initially high failure rate that decreases rapidly as manufacturing defects and marginal components are identified and replaced.**
> 2. **Useful life phase:** **Characterized by a low, relatively constant failure rate driven by random, unpredictable environmental stresses.**
> 3. **Wear-out phase:** **Characterized by a steadily increasing failure rate caused by physical deterioration, fatigue, oxidation, and mechanical friction.**
>
> **"Test-out" is not a recognized operational phase of the bathtub curve.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 308; companion slides 3, 108.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - المراحل الثلاث لمنحنى الحوض (Bathtub curve) في عتاد الأجهزة هي: مرحلة البداية (Burn-in)، ثم العمر النافع المستقر (Useful life)، ثم مرحلة الاهتراء والتقادم (Wear-out).
> - لا توجد مرحلة باسم «Test-out»، فالبرمجيات لا تهترئ مادياً (No wear-out) بعكس الهاردوير.

</div>

---

<div class="no-break">

### Q7.2. Software reliability is:
(a) The probability of failure free operation of a program for a specified time in a specified environment · (b) The probability of failure of a program for a specified time in a specified environment · (c) The probability of success of a program for a specified time in any environment · (d) None of the above
{: .keep-next }
> **(a) The probability of failure free operation of a program for a specified time in a specified environment**
>
> **Software reliability is the probability of failure-free operation of a program for a specified time in a specified environment.**
>
> The definition specifies four dimensions:
>
> - **Probability:** A mathematical quantification bounded in $[0, 1]$.
> - **Failure-free operation:** The absence of dynamic non-conformances with user expectations.
> - **Specified time:** Measured in execution (CPU) time, clock time, or operational units.
> - **Specified environment:** The input space and operational profile under which the software executes.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 308–309; companion slides 6, 108.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - احفظ أركان تعريف اعتمادية البرمجيات الأربعة: الاحتمالية (Probability) ← التشغيل الخالي من الفشل (Failure-free) ← في زمن محدد (Specified time) ← في بيئة تشغيلية محددة (Specified environment).

</div>

---

<div class="no-break">

### Q7.3. Fault is:
(a) Defect in the program · (b) Mistake in the program · (c) Error in the program · (d) All of the above
{: .keep-next }
> **(d) All of the above**
>
> **In IEEE standard terminology and software reliability foundations, a fault is an internal manifestation of a human mistake or error that introduces a defect into the program source code, design, or documentation.** While rigorous taxonomies distinguish the developer's cognitive error (mistake) from the static code defect (fault) and the runtime event (failure), the terms defect, mistake, and error are commonly used interchangeably in introductory reliability literature to characterize a fault.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 310; companion slides 8, 108.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - تسلسل الأعطال القياسي: الخطأ البشري (Error/Mistake) يُنتج عيباً داخلياً في الكود يسمى العلة أو الخلل (Fault/Defect)، والذي يسبب عند تنفيذه الفشل التشغيلي الخارجي (Failure).

</div>

---

<div class="no-break">

### Q7.4. One fault may lead to:
(a) One failure · (b) Two failures · (c) Many failures · (d) All of the above
{: .keep-next }
> **(d) All of the above**
>
> **There is no strict one-to-one mapping between static faults and dynamic failures:**
>
> - **A single fault may manifest as a single failure** under a specific test case.
> - **A single fault may trigger multiple recurring failures** across different user transactions or continuous iterations.
> - **A single fault may cause an entire cascade of failures** in downstream distributed components.
> - Conversely, **multiple distinct faults may combine to trigger a single observable failure.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 310; companion slides 8, 108.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - العلاقة بين العيب المصدري (Fault) والفشل التشغيلي (Failure) هي علاقة (One-to-Many)؛ عيب برمجي واحد في حلقة تكرار قد يسبب آلاف الانهيارات، وقد لا يظهر أبداً إذا لم يُنفذ مساره.

</div>

---

<div class="no-break">

### Q7.5. Which "time" unit is not used in reliability studies?
(a) Execution time · (b) Machine time · (c) Clock time · (d) Calendar time
{: .keep-next }
> **(b) Machine time**
>
> **Software reliability engineering characterizes system behavior across three specific, well-defined time concepts:**
>
> 1. **Execution time ($\tau$):** **The actual processor (CPU) time spent by the computer system executing the instructions of the software under study.**
> 2. **Calendar time ($t$):** **The ordinary chronological time experienced in calendar days, weeks, or months**, including idle time and off-shift hours.
> 3. **Clock time:** **The total elapsed wall-clock running time during which the system is operational.**
>
> **"Machine time" is an ambiguous, non-standard term not formally recognized as a time dimension in reliability modeling.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 310–311; companion slides 11, 109.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - المقاييس الزمنية المعتمدة في دراسات الاعتمادية هي ثلاثة: زمن التنفيذ الفعلي للمعالج (Execution time $\tau$)، والزمن التقويمي الطبيعي (Calendar time $t$)، وزمن الساعة الجدارية (Clock time). مصطلح «Machine time» مستبعد.

</div>

---

<div class="no-break">

### Q7.6. Failure occurrences can be represented as:
(a) Time to failure · (b) Time interval between failures · (c) Failures experienced in a time interval · (d) All of the above
{: .keep-next }
> **(d) All of the above**
>
> **In stochastic reliability modeling, the random failure process can be mathematically formulated in three mathematically equivalent representations:**
>
> 1. **Time to failure:** The elapsed time from the start of execution until failure occurrence.
> 2. **Time interval between failures:** The incremental operational duration separating successive failure events ($t_i - t_{i-1}$).
> 3. **Failures experienced in a time interval:** The cumulative or incremental count of failures observed over a given operational duration ($M(\tau)$ or $\Delta \mu$).
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 311; companion slides 12, 109.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - يمكن تمثيل حدوث الانهيارات بثلاث طرق إحصائية متكافئة: زمن حدوث الفشل، أو الفاصل الزمني بين فشلين، أو عدد الإخفاقات خلال فترة محددة.

</div>

---

<div class="no-break">

### Q7.7. Maximum possible value of reliability is:
(a) 100 · (b) 10 · (c) 1 · (d) 0
{: .keep-next }
> **(c) 1**
>
> **Because reliability $R(t)$ is mathematically defined as a probability, its values are strictly bounded by the probability axioms within the closed real interval:**
>
> $$0 \le R(t) \le 1$$
>
> **A reliability value of $R(t) = 1.0$ represents a 100% mathematical probability of failure-free operation over the specified interval.** (While percentages such as $100\%$ are colloquial, the raw mathematical maximum is $1$).
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 309; companion slides 7, 109.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - الاعتمادية هي دالة احتمالية رياضية (Probability)، وبالتالي فإن قيمتها الصغرى هي 0 وقيمتها العظمى هي 1 (ولا يُختار 100 إلا إذا وُضعت علامة النسبة المئوية %).

</div>

---

<div class="no-break">

### Q7.8. Minimum possible value of reliability is:
(a) 100 · (b) 10 · (c) 1 · (d) 0
{: .keep-next }
> **(d) 0**
>
> **The lower bound of the probability distribution for software reliability is $0$, representing complete operational failure where failure-free operation over the specified duration cannot occur.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 309; companion slides 7, 109.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - القيمة الصغرى المطلقة للاعتمادية هي 0.

</div>

---

<div class="no-break">

### Q7.9. As the reliability increases, failure intensity:
(a) Decreases · (b) Increases · (c) No effect · (d) None of the above
{: .keep-next }
> **(a) Decreases**
>
> **Reliability $R(t)$ and failure intensity $\lambda(t)$ share an inverse exponential relationship:**
>
> $$R(t) = \exp\left(-\int_0^t \lambda(u) \, du\right)$$
>
> **When failure intensity $\lambda$ decreases (indicating fewer failures occurring per unit of execution time), the probability of failure-free operation $R(t)$ increases toward 1.** Conversely, high failure intensity rapidly drives reliability toward zero.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 312, 321; companion slides 21, 109.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - العلاقة عكسية صريحة: كلما انخفضت شدة الفشل (Failure Intensity $\lambda$)، ارتفعت موثوقية واعتمادية النظام ($R$).

</div>

---

<div class="no-break">

### Q7.10. If failure intensity is 0.005 failures/hour during 10 hours of operation of a software, its reliability can be expressed as:
(a) 0.10 · (b) 0.92 · (c) 0.95 · (d) 0.98
{: .keep-next }
> **(c) 0.95**
>
> **Under the constant failure intensity assumption over operational duration $t$, reliability is calculated using the exponential reliability formula:**
>
> $$R(t) = e^{-\lambda t}$$
>
> **Substituting $\lambda = 0.005 \text{ failures/hour}$ and $t = 10 \text{ hours}$:**
>
> $$R(10) = e^{-(0.005 \times 10)} = e^{-0.05} \approx 0.951229 \approx 0.95$$
>
> **Therefore, the probability of failure-free operation during the 10-hour interval is approximately 0.95 (or 95.1%).**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 312; companion slides 22, 110.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - القانون الرياضي المباشر: $R = e^{-\lambda t} = e^{-(0.005 \times 10)} = e^{-0.05} \approx 0.9512$. التقريب الصحيح هو 0.95.

</div>

---

<div class="no-break">

### Q7.11. Software Quality is:
(a) Conformance to requirements · (b) Fitness for the purpose · (c) Level of satisfaction · (d) All of the above
{: .keep-next }
> **(d) All of the above**
>
> **Software quality is a multidimensional concept synthesizing several canonical engineering perspectives:**
>
> - **Crosby's definition:** "Conformance to requirements" (meeting specified functional and non-functional specifications).
> - **Juran's definition:** "Fitness for purpose / use" (satisfying customer operational needs in real production).
> - **IEEE / ISO definition:** The degree to which a software system satisfies user requirements and produces a high level of stakeholder satisfaction.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 321; companion slides 24, 110.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - جودة البرمجيات تشمل التوافق مع المتطلبات المحددة (Crosby)، والملاءمة للغرض التشغيلي (Juran)، وتحقيق رضا المستخدم (ISO/IEEE).

</div>

---

<div class="no-break">

### Q7.12. Defect rate is:
(a) Number of defects per million lines of source code · (b) Number of defects per function point · (c) Number of defects per unit of size of software · (d) All of the above
{: .keep-next }
> **(d) All of the above**
>
> **Defect rate (or defect density) is defined as the total number of identified defects normalized against a standardized measure of software size.** Industry and academic standards compute defect rate per KLOC (thousands of lines of code), per million lines of code (in telecommunications/avionics), or per Function Point (in business IT systems). Therefore, any metric normalizing defects per unit of size represents defect rate.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 322; companion slides 27, 110.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - معدل أو كثافة العيوب (Defect rate) هو مقياس منسوب لوحدة الحجم، سواء قيس بعدد العيوب لكل KLOC أو لكل Function Point.

</div>

---

<div class="no-break">

### Q7.13. How many product quality factors have been proposed in McCall quality model?
(a) 2 · (b) 3 · (c) 11 · (d) 6
{: .keep-next }
> **(c) 11**
>
> **In Jim McCall's seminal software quality model (1977), software quality is decomposed into exactly 11 product quality factors organized across three operational perspectives:**
>
> 1. **Product Operation (5 factors):** Correctness, Reliability, Efficiency, Integrity, Usability.
> 2. **Product Revision (3 factors):** Maintainability, Flexibility, Testability.
> 3. **Product Transition (3 factors):** Portability, Reusability, Interoperability.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 323–324; companion slides 30–35, 110.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - نموذج ماكول (McCall) يقسم الجودة إلى **3 أبعاد رئيسية** تضم بداخلها **11 عاملاً نوعياً (Factors)**: 5 للتشغيل + 3 للمراجعة والتعديل + 3 للانتقال وقابلية النقل.

</div>

---

<div class="no-break">

### Q7.14. Which one is not a product quality factor category of McCall quality model?
(a) Product revision · (b) Product operation · (c) Product specification · (d) Product transition
{: .keep-next }
> **(c) Product specification**
>
> **McCall's triangular quality framework categorizes its 11 factors into three broad operational categories:**
>
> - **Product Operation:** Using the software to perform real-world tasks.
> - **Product Revision:** Modifying and debugging the software code.
> - **Product Transition:** Porting and adapting the software to new platforms.
>
> **"Product specification" is an engineering phase, not one of McCall's three quality categories.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 323; companion slides 30, 111.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - أبعاد ماكول الثلاثة الشهيرة هي: Product Operation وProduct Revision وProduct Transition. لا يوجد بعد باسم «Product specification».

</div>

---

<div class="no-break">

### Q7.15. The second level of quality attributes in McCall quality model are termed as:
(a) Quality criteria · (b) Quality factors · (c) Quality guidelines · (d) Quality specifications
{: .keep-next }
> **(a) Quality criteria**
>
> **McCall's quality model is structured in a strict hierarchical decomposition:**
>
> 1. **Top Level (High-level Factors):** External quality factors representing management and customer viewpoints (e.g., Maintainability, Reliability).
> 2. **Second Level (Quality Criteria):** **Intermediate software attributes representing software engineering viewpoints that directly affect the factors** (e.g., modularity, conciseness, consistency, fault tolerance).
> 3. **Third Level (Quality Metrics):** Quantitative direct measurements used to calculate the criteria.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 323–324; companion slides 31, 111.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - الهرمية في نموذج ماكول: العوامل (Factors) في القمة ← تليها المعايير الهندسية (Criteria) في المستوى الثاني ← تليها المقاييس الكمية المباشرة (Metrics).

</div>

---

<div class="no-break">

### Q7.16. Which one is not a level in Boehm software quality model?
(a) Primary uses · (b) Intermediate constructs · (c) Primitive constructs · (d) Final constructs
{: .keep-next }
> **(d) Final constructs**
>
> **Barry Boehm's hierarchical quality model (1978) structures quality across three explicit levels:**
>
> 1. **Primary uses / high-level characteristics:** The figure links General Utility directly to Portability and Maintainability. As-is Utility links to Reliability, Efficiency, and Human Engineering; Maintainability links to Testability, Understandability, and Modifiability.
> 2. **Intermediate constructs:** Seven constructs, including Portability, Reliability, Efficiency, Human Engineering, Testability, Understandability, and Modifiability.
> 3. **Primitive constructs:** The model lists 12 lower-level characteristics.
>
> **"Final constructs" is not a level in Boehm's taxonomy.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 324–326; companion slides 40, 111.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - مستويات نموذج بويم (Boehm) الثلاثة هي: Primary uses ← تليها Intermediate constructs ← ثم Primitive constructs. لا توجد طبقة تسمى «Final constructs».

</div>

---

<div class="no-break">

### Q7.17. Which one is not a software product quality model?
(a) McCall model · (b) Boehm model · (c) ISO 9000 · (d) ISO 9126
{: .keep-next }
> **(c) ISO 9000**
>
> **McCall's model, Boehm's model, and ISO 9126 are product quality models that evaluate the internal attributes and external runtime characteristics of the software artifact itself.**
>
> **In contrast, ISO 9000 (and ISO 9001) is a Quality Management System (QMS) standard focused strictly on organizational development processes, management commitment, and procedural compliance**, rather than evaluating software product attributes directly.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 321, 354–355; companion slides 29, 111.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - فرق جوهري: نماذج جودة المنتج البرمجي تشمل McCall وBoehm وISO 9126. أما ISO 9000 فهو معيار إدارة عمليات المنشأة (Process Standard) وليس مقياساً لجودة المنتج البرمجي ذاته.

</div>

---

<div class="no-break">

### Q7.18. Basic execution time model was developed by:
(a) Bev. Littlewood · (b) J.D. Musa · (c) Barry Boehm · (d) Jim McCall
{: .keep-next }
> **(b) J.D. Musa**
>
> **The Basic Execution Time Model was formulated and published by John D. Musa at Bell Laboratories in 1979.** It represents one of the foundational Non-Homogeneous Poisson Process (NHPP) software reliability growth models based on execution time.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 329; companion slides 47, 111.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - نموذج زمن التنفيذ الأساسي (Basic Execution Time Model) وضعه جون موسى (J.D. Musa) في مختبرات بيل عام 1979.

</div>

---

<div class="no-break">

### Q7.19. NHPP stands for:
(a) Non Homogeneous Poisson Process · (b) Non Heterogeneous Poisson Process · (c) Non Homogeneous Poisson Product · (d) Non Heterogeneous Poisson Product
{: .keep-next }
> **(a) Non Homogeneous Poisson Process**
>
> **NHPP stands for Non-Homogeneous Poisson Process.** In software reliability growth modeling, an NHPP is a generalized Poisson stochastic process whose failure rate (intensity function $\lambda(t)$) varies dynamically over execution time rather than remaining constant.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 329; companion slides 47, 112.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - مصطلح NHPP يعني عملية بواسون غير المتجانسة (Non-Homogeneous Poisson Process)، وتتميز بأن معدل حدوث الأخطاء فيها يتغير مع تقدم زمن الاختبار.

</div>

---

<div class="no-break">

### Q7.20. In the Basic execution time model, failure intensity is given by:
(a) $\lambda(\mu) = \lambda_0 \left(1 - \frac{\mu}{v_0^2}\right)$ · (b) $\lambda(\mu) = \lambda_0 \left(1 - \frac{\mu}{v_0}\right)$ · (c) $\lambda(\mu) = \lambda_0 \left(1 - \frac{v_0}{\mu}\right)$ · (d) $\lambda(\mu) = \lambda_0 \left(1 - \frac{\mu^2}{v_0}\right)$
{: .keep-next }
> **(b) $\lambda(\mu) = \lambda_0 \left(1 - \frac{\mu}{v_0}\right)$**
>
> **In Musa's Basic Execution Time Model, the failure intensity $\lambda(\mu)$ decreases linearly as a function of the cumulative failures experienced ($\mu$):**
>
> $$\lambda(\mu) = \lambda_0 \left(1 - \frac{\mu}{v_0}\right)$$
>
> **Where:**
>
> - **$\lambda_0$:** **Initial failure intensity at the beginning of execution ($\mu = 0$).**
> - **$v_0$:** **Total number of failures that would be experienced in infinite execution time.**
> - **$\mu$:** **Cumulative number of failures experienced up to that point.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 330; companion slides 48, 112.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - دالة شدة الفشل في النموذج الأساسي دالة خطية تنازلية: $\lambda(\mu) = \lambda_0 (1 - \mu/v_0)$. تنخفض الشدة خطياً مع ازدياد الأعطال المكتشفة والمصلحة.

</div>

---

<div class="no-break">

### Q7.21. In the Basic execution time model, the additional number of failures required to achieve a failure intensity objective is expressed as:
(a) $\Delta \mu = \frac{v_0}{\lambda_0} (\lambda_F - \lambda_P)$ · (b) $\Delta \mu = \frac{v_0}{\lambda_0} (\lambda_P - \lambda_F)$ · (c) $\Delta \mu = \frac{\lambda_0}{v_0} (\lambda_P - \lambda_F)$ · (d) $\Delta \mu = \frac{\lambda_0}{v_0} (\lambda_F - \lambda_P)$
{: .keep-next }
> **(b) $\Delta \mu = \frac{v_0}{\lambda_0} (\lambda_P - \lambda_F)$**
>
> **Rearranging the linear failure intensity relationship for the present intensity ($\lambda_P$) and objective intensity ($\lambda_F$):**
>
> $$\lambda_P = \lambda_0 \left(1 - \frac{\mu_P}{v_0}\right), \quad \lambda_F = \lambda_0 \left(1 - \frac{\mu_F}{v_0}\right)$$
>
> **Subtracting the two equations yields:**
>
> $$\lambda_P - \lambda_F = \frac{\lambda_0}{v_0} (\mu_F - \mu_P) = \frac{\lambda_0}{v_0} \Delta \mu$$
>
> **Solving for $\Delta \mu$ gives:**
>
> $$\Delta \mu = \frac{v_0}{\lambda_0} (\lambda_P - \lambda_F)$$
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 331; companion slides 51, 112.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - عدد الأعطال الإضافية اللازمة للوصول إلى هدف الاعتمادية هو: $\Delta \mu = \frac{v_0}{\lambda_0} (\lambda_P - \lambda_F)$. انتبه لطرح الهدف المنخفض من الشدة الحالية $(\lambda_P - \lambda_F)$.

</div>

---

<div class="no-break">

### Q7.22. In the Basic execution time model, the additional execution time required to achieve a failure intensity objective is given as:
(a) $\Delta \tau = \frac{v_0}{\lambda_0} \ln\left(\frac{\lambda_F}{\lambda_P}\right)$ · (b) $\Delta \tau = \frac{\lambda_0}{v_0} \ln\left(\frac{\lambda_P}{\lambda_F}\right)$ · (c) $\Delta \tau = \frac{v_0}{\lambda_0} \ln\left(\frac{\lambda_P}{\lambda_F}\right)$ · (d) $\Delta \tau = \frac{\lambda_0}{v_0} \ln\left(\frac{\lambda_F}{\lambda_P}\right)$
{: .keep-next }
> **(c) $\Delta \tau = \frac{v_0}{\lambda_0} \ln\left(\frac{\lambda_P}{\lambda_F}\right)$**
>
> **In the Basic execution time model, failure intensity decays exponentially with execution time $\tau$:**
>
> $$\lambda(\tau) = \lambda_0 \exp\left(-\frac{\lambda_0}{v_0} \tau\right)$$
>
> **Evaluating between current intensity $\lambda_P$ and target intensity $\lambda_F$:**
>
> $$\frac{\lambda_P}{\lambda_F} = \exp\left(\frac{\lambda_0}{v_0} \Delta \tau\right)$$
>
> **Taking the natural logarithm of both sides and solving for $\Delta \tau$:**
>
> $$\Delta \tau = \frac{v_0}{\lambda_0} \ln\left(\frac{\lambda_P}{\lambda_F}\right)$$
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 331; companion slides 52, 113.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - زمن التنفيذ الإضافي المطلوب للوصول لهدف الاختبار: $\Delta \tau = \frac{v_0}{\lambda_0} \ln(\lambda_P / \lambda_F)$. النسبة داخل اللوغاريتم هي القيمة الأكبر على الأصغر $(\lambda_P / \lambda_F)$ لضمان ناتج موجب.

</div>

---

<div class="no-break">

### Q7.23. The failure intensity function of the Logarithmic Poisson execution time model is given as:
(a) $\lambda(\mu) = \lambda_0 \ln(-\theta \mu)$ · (b) $\lambda(\mu) = \lambda_0 \exp(-\theta \mu)$ · (c) $\lambda(\mu) = \lambda_0 \exp(\theta \mu)$ · (d) $\lambda(\mu) = \lambda_0 \log(\theta \mu)$
{: .keep-next }
> **(b) $\lambda(\mu) = \lambda_0 \exp(-\theta \mu)$**
>
> **In the Logarithmic Poisson execution time model (Musa–Okumoto, 1984), failure intensity decreases exponentially with respect to cumulative failures experienced ($\mu$):**
>
> $$\lambda(\mu) = \lambda_0 \exp(-\theta \mu)$$
>
> **Where $\theta$ is the failure intensity decay parameter. This exponential decay captures the realistic observation that early faults contribute much more heavily to failure intensity than subtle faults discovered late in testing.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 335; companion slides 59, 113.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - دالة شدة الفشل في نموذج بواسون اللوغاريتمي تنخفض أسياً مع عدد الأخطاء: $\lambda(\mu) = \lambda_0 \exp(-\theta \mu)$.

</div>

---

<div class="no-break">

### Q7.24. In the Logarithmic Poisson execution time model, "$\theta$" is known as:
(a) Failure intensity function parameter · (b) Failure intensity decay parameter · (c) Failure intensity measurement · (d) Failure intensity increment parameter
{: .keep-next }
> **(b) Failure intensity decay parameter**
>
> **In the Logarithmic Poisson formulation, $\theta$ is explicitly termed the failure intensity decay parameter (measured in $\text{failure}^{-1}$).** It quantifies the relative reduction in failure intensity per failure experienced:
>
> $$\theta = -\frac{d\lambda / d\mu}{\lambda}$$
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 335; companion slides 59, 113.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - الرمز $\theta$ في نموذج بواسون اللوغاريتمي يمثل معامل تلاشي شدة الفشل (Failure intensity decay parameter).

</div>

---

<div class="no-break">

### Q7.25. In the Jelinski–Moranda model, failure intensity is defined as:
(a) $\lambda(t_i) = \phi [N - (i - 1)]$ · (b) $\lambda(t_i) = \phi [N + (i - 1)]$ · (c) $\lambda(t_i) = \phi [N - i]$ · (d) $\lambda(t_i) = \phi [N / i]$
{: .keep-next }
> **(a) $\lambda(t_i) = \phi [N - (i - 1)]$**
>
> **The Jelinski–Moranda model (1972) assumes that software contains an initial total of $N$ faults, each contributing an equal hazard rate $\phi$.** When the $i$-th failure occurs, $(i - 1)$ faults have already been completely and perfectly removed without introducing new faults. Thus, during the interval between the $(i-1)$-th and $i$-th failure, the failure intensity is:
>
> $$\lambda(t_i) = \phi [N - (i - 1)]$$
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 345; companion slides 90, 114.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - معادلة جيلينسكي-موراندا: شدة الفشل عند العطل رقم $i$ تتناسب مع عدد الأخطاء المتبقية: $\phi [N - (i - 1)]$.

</div>

---

<div class="no-break">

### Q7.26. CMM Level 1 has:
(a) 6 KPAs · (b) 2 KPAs · (c) 0 KPAs · (d) None of the above
{: .keep-next }
> **(c) 0 KPAs**
>
> **In the Capability Maturity Model (CMM), Level 1 (Initial) has exactly zero Key Process Areas (KPAs).** At Level 1, processes are ad-hoc, chaotic, and undefined; project success depends solely on individual heroism and crisis management rather than repeatable institutional practices. KPAs appear beginning at Level 2 (which has 6 KPAs).
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 348; companion slides 95, 114.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - المستوى الأول في نموذج CMM (المستوى الابتدائي Initial) يحتوي على **صفر من مناطق العمليات الرئيسية (0 KPAs)** لأن العمل فيه فوضوي وغير خاضع لمعايير مؤسسية.

</div>

---

<div class="no-break">

### Q7.27. MTBF stands for:
(a) Mean time between failure · (b) Maximum time between failures · (c) Minimum time between failures · (d) Many time between failures
{: .keep-next }
> **(a) Mean time between failure**
>
> **MTBF stands for Mean Time Between Failures.** It represents the average elapsed operational time separating successive system failures in repairable systems, calculated as the sum of Mean Time To Failure (MTTF) and Mean Time To Repair (MTTR):
>
> $$MTBF = MTTF + MTTR$$
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 312; companion slides 13, 114.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - مصطلح MTBF يعني متوسط الزمن بين الانهيارات (Mean Time Between Failures) في الأنظمة القابلة للإصلاح.

</div>

---

<div class="no-break">

### Q7.28. CMM model is a technique to:
(a) Improve the software process · (b) Automatically develop the software · (c) Test the software · (d) All of the above
{: .keep-next }
> **(a) Improve the software process**
>
> **The Capability Maturity Model (SEI CMM) is an organizational framework designed specifically to assess the maturity of software processes and guide organizations through evolutionary stages of software process improvement.** It does not automatically generate source code or function as an automated testing engine.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 347; companion slides 94, 114.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - هدف CMM الأساسي هو تحسين نضج العملية البرمجية للمؤسسة (Improve the software process)، وليس توليد كود آلياً.

</div>

---

<div class="no-break">

### Q7.29. Total number of maturity levels in CMM are:
(a) 1 · (b) 3 · (c) 5 · (d) 7
{: .keep-next }
> **(c) 5**
>
> **The SEI Capability Maturity Model defines exactly five evolutionary maturity levels:**
>
> 1. **Level 1 — Initial:** Chaotic, ad-hoc performance.
> 2. **Level 2 — Repeatable:** Basic project management controls.
> 3. **Level 3 — Defined:** Standardized, institutionalized engineering processes.
> 4. **Level 4 — Managed:** Quantitative process measurement and product quality metrics.
> 5. **Level 5 — Optimizing:** Continuous process improvement through feedback and technological innovation.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 348; companion slides 95, 114.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - مستويات CMM الخمسة بالترتيب: 1- Initial ← 2- Repeatable ← 3- Defined ← 4- Managed ← 5- Optimizing.

</div>

---

<div class="no-break">

### Q7.30. Reliability of a software is dependent on number of errors:
(a) Removed · (b) Remaining · (c) Both (a) & (b) · (d) None of the above
{: .keep-next }
> **(b) Remaining**
>
> **Software reliability is determined strictly by the latent faults currently remaining in the code that can be encountered during execution, combined with the frequency of their activation under the operational profile.** The historical count of faults removed during past debugging sessions does not dictate current system stability; a system from which 1,000 faults were removed may still fail immediately if critical residual faults remain in frequently executed pathways.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 309, 313; companion slides 9, 115.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - فخ امتحاني شهير: اعتمادية النظام تعتمد حصراً على عدد الأخطاء المتبقية (Remaining) في الكود أثناء التشغيل، ولا تعتمد على عدد الأخطاء التي تم إصلاحها في الماضي.

</div>

---

<div class="no-break">

### Q7.31. Reliability of software is usually estimated at:
(a) Analysis phase · (b) Design phase · (c) Coding phase · (d) Testing phase
{: .keep-next }
> **(d) Testing phase**
>
> **Dynamic software reliability models (such as Musa's models and Jelinski–Moranda) require executing the software under an operational profile and collecting dynamic failure timestamps and counts.** Consequently, statistical estimation and measurement of software reliability take place primarily during system and integration **testing**, once an executable system exists.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 312–313; companion slides 10, 115.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - تقدير الاعتمادية إحصائياً يحتاج إلى تشغيل الكود وتسجيل أزمنة الفشل، ولذلك يتم قياسها في مرحلة الاختبار (Testing phase).

</div>

---

<div class="no-break">

### Q7.32. CMM stands for:
(a) Capacity maturity model · (b) Capability maturity model · (c) Cost management model · (d) Comprehensive maintenance model
{: .keep-next }
> **(b) Capability maturity model**
>
> **CMM stands for Capability Maturity Model**, developed by the Software Engineering Institute (SEI) at Carnegie Mellon University.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 347; companion slides 94, 115.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - CMM اختصار لـ Capability Maturity Model.

</div>

---

<div class="no-break">

### Q7.33. Which level of CMM is for basic project management?
(a) Initial · (b) Repeatable · (c) Defined · (d) Managed
{: .keep-next }
> **(b) Repeatable**
>
> **Level 2 (Repeatable) of the Capability Maturity Model establishes fundamental project management controls**, focusing on project planning, requirements management, project tracking, subcontract management, quality assurance, and configuration management to ensure realistic commitments based on past project successes.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 348; companion slides 95, 115.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - المستوى الثاني (Repeatable) هو المستوى المسؤول عن إدارة المشاريع الأساسية (Basic project management).

</div>

---

<div class="no-break">

### Q7.34. Which level of CMM is for process control?
(a) Initial · (b) Repeatable · (c) Defined · (d) Managed
{: .keep-next }
> **(d) Managed**
>
> **Level 4 (Managed) uses quantitative measures to control process and product quality.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 361; companion slide 115.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - ضبط والتحكم في العمليات (Process control) كمياً هو ميزة المستوى الرابع (Managed).
> - الشريحة 115 تكرر صياغة سؤال 7.35؛ صيغة هذا السؤال عن Process control.

</div>

---

<div class="no-break">

### Q7.35. Which level of CMM is for process management?
(a) Initial · (b) Defined · (c) Managed · (d) Optimizing
{: .keep-next }
> **(b) Defined**
>
> **At Level 3 (Defined), standard software engineering and management processes are documented, standardized, and integrated into an organization-wide standard software process (institutional process management).** Projects tailor these standard organizational processes to develop approved, managed project processes.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 348–349, 361; companion slide 116.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - توثيق وإدارة العمليات المؤسسية القياسية (Process management) هو عنوان المستوى الثالث (Defined).

</div>

---

<div class="no-break">

### Q7.36. CMM was developed at:
(a) Harvard University · (b) Cambridge University · (c) Carnegie Mellon University · (d) Maryland University
{: .keep-next }
> **(c) Carnegie Mellon University**
>
> **The Capability Maturity Model (CMM) was developed by the Software Engineering Institute (SEI), a federally funded research and development center established at Carnegie Mellon University (CMU) in Pittsburgh, Pennsylvania.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 347; companion slides 94, 116.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - طور معهد SEI نموذج CMM في جامعة كارنيغي ميلون (Carnegie Mellon University).

</div>

---

<div class="no-break">

### Q7.37. McCall has developed a:
(a) Quality model · (b) Process model · (c) Reliability model · (d) None of the above
{: .keep-next }
> **(a) Quality model**
>
> **Jim McCall and his associates developed a landmark Software Quality Model in 1977 for the US Air Force**, pioneering the decomposition of software quality into factors, criteria, and metrics.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 323; companion slides 30, 116.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - وضع ماكول (McCall) نموذجاً لجودة البرمجيات (Quality model).

</div>

---

<div class="no-break">

### Q7.38. The model to measure software process improvement is called:
(a) ISO 9000 · (b) ISO 9126 · (c) CMM · (d) Spiral model
{: .keep-next }
> **(c) CMM**
>
> **The Capability Maturity Model (CMM) provides a structured metric and staging framework specifically designed to evaluate organizational process capability and track continuous process improvement.** ISO 9126 measures product quality, ISO 9000 is a baseline certification standard, and the Spiral model is a life-cycle methodology.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 347; companion slides 94, 116.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - الموديل المخصص لقياس تحسين نضج العملية البرمجية وتدرجها هو CMM.

</div>

---

<div class="no-break">

### Q7.39. The number of clauses used in ISO 9001 are:
(a) 15 · (b) 25 · (c) 20 · (d) 10
{: .keep-next }
> **(c) 20**
>
> **ISO 9001:1994 organized its quality-system requirements into 20 clauses, numbered 4.1 through 4.20.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 355; companion slides 103, 116.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - اعتمدت مواصفة ISO 9001 (إصدار 1994 المنهجي في الكتاب) على **20 بنداً أو فقرة متطلبات (20 clauses)** تم ربطها مع متطلبات CMM.

</div>

---

<div class="no-break">

### Q7.40. ISO 9126 contains definitions of:
(a) Quality characteristics · (b) Quality factors · (c) Quality attributes · (d) All of the above
{: .keep-next }
> **(a) Quality characteristics**
>
> **The ISO/IEC 9126 standard formally structures software product quality into six top-level quality characteristics:** Functionality, Reliability, Usability, Efficiency, Maintainability, and Portability. Each characteristic is further refined into subcharacteristics and measurable metrics.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 326–327; companion slides 41, 117.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - في معيار ISO 9126، يسمى المستوى الأعلى بخصائص الجودة (Quality characteristics)، وعددها 6 خصائص رئيسية.

</div>

---

<div class="no-break">

### Q7.41. In ISO 9126, each characteristic is related to:
(a) One attribute · (b) Two attributes · (c) Three attributes · (d) Four attributes
{: .keep-next }
> **No single option is correct for all six characteristics.** The listed ISO 9126 table gives different numbers of subcharacteristics: Reliability has three, Efficiency has two, and Functionality has four.
>
> The MCQ is therefore inconsistent as worded.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 327; companion slides 41, 117.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - يرتبط كل بعد رئيسي في سلايدات أغروال بصفات فرعية محددة (Subcharacteristics) تمثل السمات المشتقة.
> - الشريحة 117 تضع الخيار (c)، لكن جدول الكتاب يبيّن أن العدد يختلف حسب الخاصية؛ لذلك لا يوجد خيار واحد يصح للجميع.

</div>

---

<div class="no-break">

### Q7.42. In McCall quality model, product revision quality factor consists of:
(a) Maintainability, Flexibility, Testability · (b) Portability, Reusability, Interoperability · (c) Correctness, Reliability, Efficiency · (d) Usability, Integrity, Efficiency
{: .keep-next }
> **(a) Maintainability, Flexibility, Testability**
>
> **Under McCall's framework, Product Revision focuses on how easily the software can be inspected, repaired, and enhanced. It consists of exactly three factors:**
>
> 1. **Maintainability:** Effort required to locate and fix defects.
> 2. **Flexibility:** Effort required to modify the software for new operational needs.
> 3. **Testability:** Effort required to validate that the software performs its intended functions.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 323; companion slides 33, 117.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - عوامل مراجعة المنتج (Product Revision) في نموذج ماكول هي ثلاثية الصيانة: سهولة الصيانة (Maintainability) + المرونة (Flexibility) + القابلية للاختبار (Testability).

</div>

---

<div class="no-break">

### Q7.43. Which is not a software reliability model?
(a) The Jelinski–Moranda Model · (b) Basic execution time model · (c) Spiral model · (d) None of the above
{: .keep-next }
> **(c) Spiral model**
>
> **The Spiral model is an iterative, risk-driven Software Development Life Cycle (SDLC) process model formulated by Barry Boehm.** It is not a statistical software reliability growth model. Jelinski–Moranda and Musa's Basic execution time model are established reliability models.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 329, 345; companion slides 47, 117.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - النموذج الحلزوني (Spiral model) هو نموذج دورة حياة لتطوير البرمجيات (SDLC) يعتمد على إدارة المخاطر، وليس نموذجاً رياضياً لقياس الاعتمادية.

</div>

---

<div class="no-break">

### Q7.44. Each maturity level in CMM has:
(a) One KPA · (b) Equal KPAs · (c) Several KPAs · (d) No KPA
{: .keep-next }
> **(c) Several KPAs**
>
> **With the exception of Level 1 (which has 0 KPAs), each mature level in the CMM comprises multiple Key Process Areas (KPAs):** Level 2 has 6 KPAs, Level 3 has 7 KPAs, Level 4 has 2 KPAs, and Level 5 has 3 KPAs.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 350–352; companion slides 97–101, 117.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - يضم كل مستوى من مستويات CMM الناضجة عدة مناطق عمليات رئيسية (Several KPAs)، تتراوح بين 2 و7 مجالات.

</div>

---

<div class="no-break">

### Q7.45. KPA in CMM stands for:
(a) Key Process Area · (b) Key Product Area · (c) Key Principal Area · (d) Key Performance Area
{: .keep-next }
> **(a) Key Process Area**
>
> **KPA stands for Key Process Area.** In CMM, a Key Process Area identifies a cluster of related activities that, when performed collectively, achieve a set of goals considered critical for establishing process capability at that maturity level.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 350; companion slides 97, 118.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - مصطلح KPA يعني منطقة العملية الرئيسية (Key Process Area).

</div>

---

<div class="no-break">

### Q7.46. In reliability models, our emphasis is on:
(a) Errors · (b) Faults · (c) Failures · (d) Bugs
{: .keep-next }
> **(c) Failures**
>
> **Dynamic software reliability models model the observable behavior of the software from the user's perspective; hence, the primary modeling emphasis is on failures (dynamic departure from required operation).** Users experience failures, not passive latent faults residing silently in unexecuted source code.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 310, 329; companion slides 8, 118.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - تركز نماذج الاعتمادية على حالات الفشل (Failures) لأنها الحدث الديناميكي الحقيقي الذي يواجهه المستخدم ويؤثر على الخدمة في الواقع.

</div>

---

<div class="no-break">

### Q7.47. Software does not break or wear out like hardware. What is your opinion?
(a) True · (b) False · (c) Partially True · (d) Cannot say
{: .keep-next }
> **(a) True**
>
> **True in the physical sense: software does not wear out through physical aging.** It may become obsolete or fail when its environment or requirements change, but those changes are different from hardware wear-out.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 308; companion slides 4, 118.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - العبارة صحيحة تماماً (True): البرمجيات لا تهترئ ولا تبلى مادياً (Does not wear out) لأنها كيان منطقي غير خاضع لقوانين الاحتكاك والفيزياء.

</div>

---

<div class="no-break">

### Q7.48. Software reliability is defined with respect to:
(a) Time · (b) Speed · (c) Quality · (d) None of the above
{: .keep-next }
> **(a) Time**
>
> **Software reliability is mathematically defined as a time-dependent probability distribution $R(t)$ measuring the likelihood of failure-free operation over a specified operational time interval.** Without specifying a temporal baseline (execution time, clock time, or calendar time), reliability has no mathematical meaning.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 309; companion slides 6, 118.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - دالة الاعتمادية تُعرّف رياضياً بالنسبة إلى الزمن (Time).

</div>

---

<div class="no-break">

### Q7.49. MTTF stands for:
(a) Mean time to failure · (b) Maximum time to failure · (c) Minimum time to failure · (d) None of the above
{: .keep-next }
> **(a) Mean time to failure**
>
> **MTTF stands for Mean Time To Failure.** It is the expected statistical value of the operational execution time of a software system before its next failure event occurs, defined as the integral of the reliability function:
>
> $$MTTF = \int_0^\infty R(t) \, dt$$
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 312; companion slides 13, 118.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - اختصار MTTF يعني متوسط زمن حدوث الفشل (Mean Time To Failure).

</div>

---

<div class="no-break">

### Q7.50. ISO 9000 is a series of standards for quality management systems and has:
(a) 2 related standards · (b) 5 related standards · (c) 10 related standards · (d) 25 related standards
{: .keep-next }
> **(b) 5 related standards**
>
> **The original ISO 9000 series comprises five related standards:**
>
> 1. **ISO 9000:** Quality management and quality assurance standards — Guidelines for selection and use.
> 2. **ISO 9001:** Model for quality assurance in design, development, production, installation, and servicing.
> 3. **ISO 9002:** Model for quality assurance in production, installation, and servicing.
> 4. **ISO 9003:** Model for quality assurance in final inspection and test.
> 5. **ISO 9004:** Quality management and quality system elements — Guidelines.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 354; companion slides 103, 119.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - تتكون سلسلة معايير ISO 9000 الأصلية من **5 مواصفات مرتبطة** شهيرة (ISO 9000, 9001, 9002, 9003, 9004).

</div>

---

## Section 2: Syllabus Gap-Closing Synthesis MCQs (10 Items)

<div class="no-break">

### Q7.51. In Harlan Mills' Bug Seeding Model, if $S$ artificial faults are seeded into a program, and testing subsequently uncovers $s$ seeded faults and $n$ original unseeded faults, the estimated number of latent unseeded faults $\hat{N}$ is:
(a) $\hat{N} = \frac{S \cdot n}{s}$ · (b) $\hat{N} = \frac{s \cdot n}{S}$ · (c) $\hat{N} = \frac{S \cdot s}{n}$ · (d) $\hat{N} = S \cdot n \cdot s$
{: .keep-next }
> **(a) $\hat{N} = \frac{S \cdot n}{s}$**
>
> **The Bug Seeding (or Tag-Recapture) model developed by Harlan Mills assumes that seeded artificial faults and intrinsic unseeded faults have equal probability of discovery.** Therefore, the ratio of caught seeded faults to total seeded faults equals the ratio of caught unseeded faults to total unseeded faults:
>
> $$\frac{s}{S} = \frac{n}{\hat{N}} \implies \hat{N} = \frac{S \cdot n}{s}$$
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 346–347; companion slide 93.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - معادلة بذر الأخطاء (Bug Seeding) لميلز تعتمد على التناسب المتساوي لصيد الأخطاء: $\hat{N} = (S \times n) / s$.

</div>

---

<div class="no-break">

### Q7.52. In software reliability engineering, what is an "Operational Profile"?
(a) The compiler optimization configuration · (b) A quantitative set of operational run types and their associated probabilities of occurrence · (c) The hardware specification of the deployment server · (d) The developer's daily work schedule
{: .keep-next }
> **(b) A quantitative set of operational run types and their associated probabilities of occurrence**
>
> **An Operational Profile is a complete set of operations that a software system performs, together with their individual probabilities of occurrence during actual field usage.** Testing according to the operational profile gives more testing effort to frequently executed operations.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 318–320; companion slides 16–20.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - ملف التشغيل (Operational Profile) يحدد أنواع العمليات في النظام مع احتمالية تشغيل كل منها في الواقع، لتوجيه الاختبار نحو المسارات الأكثر استخداماً.

</div>

---

<div class="no-break">

### Q7.53. In Musa's Calendar Time Component modeling, during which operational phase does testing progress slow down primarily due to personnel limitations rather than compute constraints?
(a) Test-limiting phase · (b) Failure-identification personnel limited phase · (c) Data-entry limiting phase · (d) Overclocked phase
{: .keep-next }
> **(b) Failure-identification personnel limited phase**
>
> **Musa's Calendar Time Component models testing progress under three resource constraints:**
>
> 1. **Failure identification personnel:** Bounded by available system test engineers.
> 2. **Failure resolution personnel:** Bounded by development debugging staff.
> 3. **Computer execution resources:** Bounded by available CPU test-bench time.
>
> **Early in testing when failure intensity is very high, progress is constrained strictly by the finite hours that test and debugging personnel can devote to analyzing crashes.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 339–344; companion slides 72–77.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - مكون الزمن التقويمي (Calendar time) يقسم الموارد إلى: موظفي تشخيص الفشل، وموظفي الإصلاح، وزمن المعالج. في بداية الاختبار عندما تتساقط الأخطاء بكثرة، يكون المورد الحاكم المقيد هو كادر التحقيق والإصلاح.

</div>

---

<div class="no-break">

### Q7.54. In the Capability Maturity Model (CMM), what are the "Common Features" that characterize every Key Process Area?
(a) Input, Process, Output, Storage · (b) Commitment to Perform, Ability to Perform, Activities Performed, Measurement & Analysis, Verifying Implementation · (c) Goals, Metrics, Actions, Feedback · (d) Planning, Execution, Review, Retirement
{: .keep-next }
> **(b) Commitment to Perform, Ability to Perform, Activities Performed, Measurement & Analysis, Verifying Implementation**
>
> **In SEI CMM, each KPA is organized across five structural Common Features:**
>
> 1. **Commitment to Perform:** Organizational policies and management leadership.
> 2. **Ability to Perform:** Resources, funding, tools, and training preconditions.
> 3. **Activities Performed:** Specific engineering and management tasks.
> 4. **Measurement and Analysis:** Basic metrics used to track process performance.
> 5. **Verifying Implementation:** Objective reviews and audits by SQA and executive management.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 353–354; companion slide 102.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - السمات المشتركة (Common Features) الخمس التي تبني أي KPA في CMM هي: الالتزام بالأداء ← القدرة على الأداء ← الأنشطة المنفذة ← القياس والتحليل ← التحقق من التنفيذ.

</div>

---

<div class="no-break">

### Q7.55. What is the main difference in emphasis between ISO 9001 and CMM?
(a) ISO 9001 emphasizes continuous software-process improvement; CMM defines only minimum quality-system criteria · (b) CMM emphasizes continuous process improvement, while ISO 9001 defines minimum criteria for an adequate quality-management system · (c) ISO 9001 applies only to software; CMM applies to all industries · (d) CMM concerns documentation only, while ISO 9001 provides a staged software-improvement path
{: .keep-next }
> **(b) CMM emphasizes continuous process improvement, while ISO 9001 defines minimum criteria for an adequate quality-management system**
>
> **CMM places greater emphasis on continuous process improvement. ISO 9001 defines minimum criteria for an adequate quality-management system.**
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), §7.5.2–§7.5.3, pp. 356–357; companion slide 107.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - الفرق المحوري هو أن CMM يركز أكثر على التحسين المستمر للعمليات، بينما يحدد ISO 9001 الحد الأدنى لنظام إدارة جودة مقبول.

</div>

---

<div class="no-break">

### Q7.56. In McCall's Software Quality Model, which factor belongs to the "Product Transition" dimension?
(a) Correctness · (b) Flexibility · (c) Portability · (d) Usability
{: .keep-next }
> **(c) Portability**
>
> **Product Transition encompasses three factors concerned with moving the software to new operating environments: Portability, Reusability, and Interoperability.** Correctness and Usability belong to Product Operation; Flexibility belongs to Product Revision.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 323; companion slides 30–35.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - عوامل الانتقال (Product Transition) الثلاثة في ماكول هي: القابلية للنقل (Portability) وإعادة الاستخدام (Reusability) والتشغيل البيني (Interoperability).

</div>

---

<div class="no-break">

### Q7.57. In the Logarithmic Poisson execution time model, how does total failures experienced behave as execution time $\tau \to \infty$?
(a) It reaches a finite upper limit $v_0$ · (b) It grows logarithmically without an infinite upper bound ($\mu \to \infty$) · (c) It drops immediately to zero · (d) It becomes negative
{: .keep-next }
> **(b) It grows logarithmically without an infinite upper bound ($\mu \to \infty$)**
>
> **A distinguishing mathematical attribute of the Musa–Okumoto Logarithmic Poisson model is that it models an infinite-failure category:**
>
> $$\mu(\tau) = \frac{1}{\theta} \ln(\lambda_0 \theta \tau + 1)$$
>
> **As $\tau \to \infty$, $\mu(\tau) \to \infty$ logarithmically.** Unlike the Basic model (which posits a finite total fault count $v_0$), the Logarithmic Poisson model assumes that software will continue to generate failures indefinitely at increasingly tiny failure intensities as software complexity and operational duration grow unbounded.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 335–336; companion slides 59–60.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - فرق جوهري بين النموذجين: النموذج الأساسي يفترض سقفاً نهائياً لعدد الأعطال ($v_0$)، بينما نموذج بواسون اللوغاريتمي يفترض أن الأعطال المتوقعة تتزايد لوغاريتمياً دون سقف أعلى محدود مع الزمن اللانهائي.

</div>

---

<div class="no-break">

### Q7.58. Which Key Process Area (KPA) belongs to CMM Level 2 (Repeatable)?
(a) Organization Process Definition · (b) Software Configuration Management (SCM) · (c) Quantitative Process Management · (d) Defect Prevention
{: .keep-next }
> **(b) Software Configuration Management (SCM)**
>
> **Level 2 (Repeatable) comprises exactly six KPAs focused on project-level tracking and discipline:**
>
> 1. Requirements Management
> 2. Software Project Planning
> 3. Software Project Tracking and Oversight
> 4. Software Subcontract Management
> 5. Software Quality Assurance
> 6. **Software Configuration Management**
>
> Organization Process Definition is Level 3; Quantitative Process Management is Level 4; Defect Prevention is Level 5.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), p. 350; companion slides 97, 101.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - مناطق العمليات الست للمستوى الثاني (Level 2): إدارة المتطلبات، تخطيط المشاريع، التتبع والرقابة، إدارة التعاقدات الفرعية، ضمان جودة البرمجيات (SQA)، وإدارة التكوين (SCM).

</div>

---

<div class="no-break">

### Q7.59. The relationship between execution time $\tau$ and calendar time $t$ in software reliability is mediated by:
(a) The compiler execution clock · (b) Resource allocation parameters representing available personnel, compute time, and their utilization ratios · (c) The lines of source code · (d) Function point complexity adjustment
{: .keep-next }
> **(b) Resource allocation parameters representing available personnel, compute time, and their utilization ratios**
>
> **Execution time measures CPU usage; calendar time also depends on the resources available and how fully each resource can be utilized. The limiting resource determines the calendar-time to execution-time ratio:**
>
> $$\frac{dt}{d\tau} = \max_{r\in\{I,F,C\}}\left(\frac{1}{P_r p_r}\frac{d\chi_r}{d\tau}\right) = \max_{r\in\{I,F,C\}}\left(\frac{\theta_r + \mu_r\lambda}{P_r p_r}\right)$$
>
> Here, $P_r$ is the available quantity of resource $r$, $p_r$ is its utilization fraction, and $\chi_r$ is its cumulative usage. The terms $\theta_r$ and $\mu_r$ are resource usage per CPU hour and per failure, respectively; $\lambda$ is failure intensity.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 339–344; companion slides 72–77.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - التحويل من زمن التنفيذ ($\tau$) إلى الزمن التقويمي ($t$) يتحكم به توفر الموارد البشرية (كادر الفحص وكادر الإصلاح) وقدرات أجهزة المعالجة.

</div>

---

<div class="no-break">

### Q7.60. In CMM process maturity staging, which level introduces statistical process control (SPC) and quantitative process capability baselines?
(a) Level 2 · (b) Level 3 · (c) Level 4 · (d) Level 5
{: .keep-next }
> **(c) Level 4**
>
> **Level 4 (Managed) introduces quantitative management and statistical process control (SPC).** Productivity and quality metrics are measured across all process activities, establishing statistical process capability baselines that allow management to distinguish common cause variation from special cause variation.
>
> *Source: K.K. Aggarwal & Yogesh Singh (3rd ed.), pp. 348–349; companion slides 95, 100.*

> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> - الضبط الإحصائي للعمليات (Statistical Process Control) والقياس الكمي الدقيق يبدأ حصراً في المستوى الرابع (Level 4: Managed).

</div>

---

<!-- Print-hidden study guidance retained for screen use.
## Retrieval Set & Active Recall Self-Test

Use the questions in this pack for active recall:
- Cover the model answer and notes for each question.
- Articulate the correct option and the technical justification before revealing the key.
- Verify distinguishing criteria between hardware bathtub curves and software reliability curves.
- Test retention of the linear failure intensity decay equation for the Basic model versus the exponential decay in Logarithmic Poisson.
- Recite the five maturity levels of CMM and the distinct role of KPAs versus Common Features.
-->
