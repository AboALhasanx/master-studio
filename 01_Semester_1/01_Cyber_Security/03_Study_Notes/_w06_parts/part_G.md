### القسم 1 — 1. Introduction

#### ① النص الأصلي

> Reliability and business continuity in web application security transcend technical uptime; they encapsulate the strategic resilience of digital infrastructures against adversarial, operational, and systemic threats. Reliability ensures applications deliver consistent and trustworthy services, while business continuity guarantees sustained operations even under disruption — whether caused by cyberattacks, infrastructure failures, or natural disasters.
>
> In modern economies where digital services underpin financial systems, healthcare delivery, and government administration, an application's inability to maintain reliability and continuity carries systemic implications. Cybersecurity threats such as distributed denial-of-service (DDoS) attacks, ransomware campaigns, and supply chain compromises directly intersect with operational continuity, making the two domains inseparable.

#### ② الترجمة

> «الموثوقية (Reliability) واستمرارية العمل (Business Continuity) في أمن تطبيقات الويب تتجاوزان مجرّد الجهوزية التقنية (uptime)؛ فهما تجسّدان الصمود الاستراتيجي للبنى التحتية الرقمية في مواجهة التهديدات العدائية والتشغيلية والمنظومية. تضمن الموثوقية أن تقدّم التطبيقات خدمات متّسقة وجديرة بالثقة، بينما تضمن استمرارية العمل استدامة العمليات حتى في ظلّ الاضطراب — سواء سبّبته الهجمات السيبرانية أو أعطال البنية التحتية أو الكوارث الطبيعية.
>
> وفي الاقتصادات الحديثة حيث تسند الخدمات الرقمية الأنظمة المالية والرعاية الصحية والإدارة الحكومية، فإن عجز تطبيق ويب عن الحفاظ على الموثوقية والاستمرارية يحمل تداعيات منظومية. فالتهديدات السيبرانية مثل هجمات حجب الخدمة الموزّعة (DDoS)، وحملات برامج الفدية (ransomware)، واختراقات سلسلة التوريد تتقاطع مباشرةً مع الاستمرارية التشغيلية، ما يجعل المجالين غير قابلين للفصل.»

#### ③ الشرح الفهمي

هذا الفصل مو عن "السيرفر شغّال لو واقف" بس — هو عن **الصمود** بمعنى أوسع. الفرق بين المفهومين:

| المفهوم | شنو يعالج | السؤال اللي يجاوب عليه |
|---|---|---|
| **Reliability** (الموثوقية) | الأداء المتّسق والثقة بالخدمة | هل التطبيق يشتغل صح باستمرار؟ |
| **Business Continuity** (استمرارية العمل) | استدامة العمليات وقت وبعد الاضطراب | هل الخدمة تستمر حتى وقت الكارثة؟ |

نقطة مهمة: الموثوقية والاستمرارية **مو موضوع تقني بحت**. لأن بالاقتصاد الحديث، الخدمات الرقمية تسند أنظمة مالية وصحية وحكومية ← فأي تعطّل صار عند تطبيق ويب يتحوّل لـ **تداعيات منظومية (systemic implications)**.

وأهم استنتاج بالفصل: الأمن السيبراني مو مجال منفصل عن الاستمرارية. لأن DDoS و ransomware و supply chain compromise ← تضرب الموثوقية والاستمرارية بنفس الوقت. لهذا الكورس يعتبرهم **مجالين غير قابلين للفصل (inseparable domains)**، وهذي هي الفكرة اللي يبني عليها باقي الأقسام.

---

### القسم 2 — 2. Conceptual Foundation

#### ① النص الأصلي

> **2.1 Reliability in Web Applications**
>
> Reliability denotes the probability that an application performs its intended function under stated conditions for a specified period. In web applications this translates into consistent performance across traffic surges, resistance to malicious payloads, and resilience under stress conditions.
>
> Formally, reliability is expressed as a decaying exponential, where the reliability function at time t depends on the system failure rate. In security-sensitive contexts, the failure rate is influenced not only by random failures but also by adversarial activity, making resilience both a technical and a security concern.
>
> **2.2 Business Continuity**
>
> Business continuity extends reliability into organizational strategy, ensuring critical services are maintained during and after disruptions. It encompasses disaster recovery, redundancy planning, incident response, and regulatory compliance, with the objective of minimizing downtime, financial loss, and reputational damage.

#### ② الترجمة

> «**2.1 الموثوقية في تطبيقات الويب**
>
> الموثوقية تعني الاحتمال بأن يؤدي التطبيق وظيفته المقصودة في ظروف محدّدة ولمدة زمنية معيّنة. وفي تطبيقات الويب، يتمثّل هذا في أداء متّسق خلال ذُرى حركة المرور (traffic surges)، ومقاومة الحمولات الخبيثة (malicious payloads)، وصمود تحت ظروف الإجهاد (stress).
>
> وصياغةً، تُعبَّر الموثوقية كدالة أسّية متلاشية (decaying exponential)، حيث تعتمد دالة الموثوقية عند الزمن t على معدّل فشل النظام. وفي السياقات الحسّاسة أمنيًا، يتأثّر معدّل الفشل ليس بالأعطال العشوائية فقط بل أيضًا بالنشاط العدائي (adversarial activity)، ما يجعل الصمود مسألة تقنية وأمنية في آنٍ واحد.
>
> **2.2 استمرارية العمل**
>
> استمرارية العمل توسّع الموثوقية إلى الاستراتيجية التنظيمية، فتضمن الحفاظ على الخدمات الحرجة أثناء الاضطرابات وبعدها. وتشمل التعافي من الكوارث (disaster recovery)، وتخطيط التكرار (redundancy planning)، والاستجابة للحوادث (incident response)، والامتثال التنظيمي (regulatory compliance)، بهدف تقليل التوقّف المالي والسمعة إلى أدنى حد.»

$$R(t) = e^{-\lambda t}$$

| الرمز | المعنى |
|---|---|
| $R(t)$ | دالة الموثوقية (reliability function) عند الزمن $t$ |
| $\lambda$ | معدّل الفشل (failure rate) للنظام |
| $t$ | الزمن |
| $e$ | أساس اللوغاريتم الطبيعي |

#### ③ الشرح الفهمي

**2.1 الموثوقية** — ما هي "كلمة"، هي **رقم بين 0 و 1**. المعادلة تقول إن الموثوقية تتلاشى أُسّيًا مع الزمن:

$$R(t) = e^{-\lambda t}$$

معنى المعادلة ببساطة: كل ما كبر معدّل الفشل $\lambda$، أو كل ما زاد الزمن $t$، صارت النتيجة أصغر ← يعني الموثوقية تنزل. ولو $\lambda = 0$ عند الزمن صفر، تكون $R = 1$ (موثوقية كاملة).

بس **النقطة الأهم بالسياق الأمني** (وهي اللي يعتمد عليها الفصل): $\lambda$ مو محرّكه الأعطال العشوائية (random failures) فقط — مثل عطل هاردوير أو باگ سوفتوير. **النشاط العدائي (adversarial activity)** يرفع $\lambda$ بعد. يعني هجوم DDoS أو ransomware يزيد معدّل الفشل، فتنزل $R(t)$ بسرعة. لهذا الصمود **مسألة أمنية مو تقنية بس** — هذي بالضبط الجملة اللي يعقّد عليها النص.

وبتطبيقات الويب، الموثوقية تترجم عمليًا لثلاث قدرات: أداء ثابت وقت **ذُرى الترافيك (traffic surges)**، ومقاومة **الحمولات الخبيثة (malicious payloads)**، وصمود تحت **الإجهاد (stress)**.

**2.2 استمرارية العمل** — هنا نطلع من "التطبيق" لـ "المؤسسة". استمرارية العمل تضم أربع ركائز:

| الركيزة | المعنى |
|---|---|
| Disaster recovery | التعافي من الكوارث |
| Redundancy planning | تخطيط التكرار |
| Incident response | الاستجابة للحوادث |
| Regulatory compliance | الامتثال التنظيمي |

والهدف واحد: تقليل **التوقّف (downtime)** و**الخسارة المالية** و**الضرر السمعي** لأدنى حد. يعني الموثوقية = بُعد تقني، والاستمرارية = بُعد تنظيمي/استراتيجي يبني فوقه.

---

### القسم 3 — 3. Intersection of Reliability, Continuity, and Cybersecurity

#### ① النص الأصلي

> Web applications face three classes of risks impacting continuity:
>
> 1. Operational Risks: Hardware failures, software bugs, misconfigurations.
> 2. Cybersecurity Risks: DDoS, ransomware, supply chain exploits.
> 3. Environmental Risks: Natural disasters, power outages.
>
> The intersection occurs where adversarial threats amplify operational vulnerabilities — for example, a misconfigured load balancer exploited to trigger service outages. Thus modern perspectives treat cybersecurity as integral to continuity planning.

#### ② الترجمة

> «تواجه تطبيقات الويب ثلاث فئات من المخاطر تؤثّر على الاستمرارية:
>
> 1. المخاطر التشغيلية (Operational Risks): أعطال العتاد، وأخطاء البرمجيات، وسوء التهيئة.
> 2. المخاطر السيبرانية (Cybersecurity Risks): هجمات DDoS، وبرامج الفدية، واختراقات سلسلة التوريد.
> 3. المخاطر البيئية (Environmental Risks): الكوارث الطبيعية، وانقطاعات الطاقة.
>
> ويحدث التقاطع حيث تضخّم التهديدات العدائية مواطن الضعف التشغيلية — فمثلًا، موازن حمل (load balancer) سيّئ التهيئة يُستغَل لإحداث انقطاعات في الخدمة. لهذا تتعامل المنظورات الحديثة مع الأمن السيبراني كجزء لا يتجزّأ من تخطيط الاستمرارية.»

#### ③ الشرح الفهمي

هذا القسم يجمع الخيوط بجدول واحد — ثلاث فئات مخاطر تهدّد الاستمرارية:

| الفئة | أمثلة | طبيعتها |
|---|---|---|
| **Operational** (تشغيلية) | أعطال عتاد، أخطاء برمجيات، سوء تهيئة | داخلية / غير مقصودة |
| **Cybersecurity** (سيبرانية) | DDoS، ransomware، supply chain exploits | عدائية / مقصودة |
| **Environmental** (بيئية) | كوارث طبيعية، انقطاع طاقة | خارجية / غير مقصودة |

بس الفكرة الحلوة هي كلمة **"التقاطع" (intersection)**. التقاطع مو مجرد إن الفئات الثلاث موجودة — التقاطع هو إن **التهديد العدائي يضخّم موطن الضعف التشغيلي**. المثال بالنص: موازن حمل (load balancer) سيّئ التهيئة ← هذا أصلاً موطن ضعف **تشغيلي** (misconfiguration)، بس المهاجم يستغله ليسبّب **انقطاع خدمة** ← فصار مشكلة **سيبرانية + استمرارية** بنفس الوقت.

لهذا الاستنتاج: الأمن السيبراني **جزء لا يتجزّأ من تخطيط الاستمرارية (integral to continuity planning)**، مو شي يضاف جنب. أي خطة استمرارية تتجاهل العدائي تكون ناقصة.

---

### القسم 4 — 4. Reliability Engineering in Web Applications

#### ① النص الأصلي

> **4.1 Redundancy Strategies**
>
> Redundancy ensures no single point of failure disrupts operations. Strategies include:
>
> - N+1 Redundancy: One additional component beyond required capacity.
> - Active-Active Clustering: Multiple servers handling requests simultaneously.
> - Geo-Redundancy: Distribution of services across geographical regions.
>
> System reliability for components in parallel is modeled as a parallel-reliability expression, where each component's reliability is denoted. This demonstrates how strategic redundancy exponentially increases reliability.
>
> **4.2 Reliability Metrics**
>
> Key metrics include:
>
> - Mean Time Between Failures (MTBF): Average operational uptime between failures.
> - Mean Time To Repair (MTTR): Average time to restore service after disruption.
> - Availability (A): expressed as the ratio of MTBF to the sum of MTBF and MTTR.
>
> High availability (above 99.99%) requires not only robust infrastructure but also proactive cybersecurity measures.

#### ② الترجمة

> «**4.1 استراتيجيات التكرار (Redundancy Strategies)**
>
> يضمن التكرار ألّا يُعطّل أي موطن فشل منفرد (single point of failure) العمليات. وتشمل الاستراتيجيات:
>
> - تكرار N+1: مكوّن إضافي واحد فوق السعة المطلوبة.
> - العنقدة النشطة-النشطة (Active-Active Clustering): خوادم متعدّدة تخدم الطلبات في الوقت نفسه.
> - التكرار الجغرافي (Geo-Redundancy): توزيع الخدمات عبر مناطق جغرافية.
>
> وتُنمذَج موثوقية النظام للمكوّنات المتوازية (parallel) بتعبير الموثوقية المتوازية، حيث يُرمز لموثوقية كل مكوّن. وهذا يبيّن كيف يرفع التكرار الاستراتيجي الموثوقية أُسّيًا.
>
> **4.2 مقاييس الموثوقية (Reliability Metrics)**
>
> تشمل المقاييس الرئيسية:
>
> - متوسط الزمن بين الأعطال (MTBF): متوسط زمن التشغيل بين الأعطال.
> - متوسط الزمن للإصلاح (MTTR): متوسط الزمن لاستعادة الخدمة بعد الاضطراب.
> - التوفّر (Availability - A): يُعبَّر عنه بنسبة MTBF إلى مجموع MTBF و MTTR.
>
> والتوفّر العالي (فوق 99.99%) يتطلّب ليس بنية تحتية متينة فقط بل أيضًا إجراءات أمنية سيبرانية استباقية.»

$$R_{system} = 1 - \prod_{i=1}^{n}(1 - R_i)$$

| الرمز | المعنى |
|---|---|
| $R_{system}$ | موثوقية النظام ككل |
| $R_i$ | موثوقية المكوّن $i$ |
| $n$ | عدد المكوّنات المتوازية |
| $\prod$ | حاصل الضرب على كل المكوّنات |

$$A = \frac{MTBF}{MTBF + MTTR}$$

| الرمز | المعنى |
|---|---|
| $A$ | التوفّر (Availability) |
| $MTBF$ | متوسط الزمن بين الأعطال |
| $MTTR$ | متوسط الزمن للإصلاح |

#### ③ الشرح الفهمي

**4.1 التكرار** — الفكرة: ما نخلّي **موطن فشل منفرد (single point of failure)**، يعني أي مكوّن واحد يوقع يوقّف كل شي. الثلاث استراتيجيات:

| الاستراتيجية | الفكرة | تحمي من |
|---|---|---|
| **N+1** | مكوّن زائد واحد فوق الحاجة | فشل مكوّن واحد |
| **Active-Active** | عدة خوادم تخدم الطلبات بنفس الوقت | فشل خادم + توزيع الحمل |
| **Geo-Redundancy** | توزيع الخدمات جغرافيًا | كارثة تشلّ منطقة كاملة |

والمعادلة الرياضية للمكوّنات المتوازية:

$$R_{system} = 1 - \prod_{i=1}^{n}(1 - R_i)$$

المنطق: عندنا طريقتين للربط —
- **Series (تسلسلي):** نضرب الموثوقيات $R_1 \times R_2$ ← كل ما زادت المكوّنات **نزلت** الموثوقية (لأن أي واحد يوقع يوقّف الكل).
- **Parallel (متوازي):** نستخدم المكمّل. احتمال إن **كل** المكوّنات تفشل = $\prod(1-R_i)$، فاحتمال إن **واحد على الأقل** يشتغل = $1$ ناقص هذا الحاصل.

مثال يوضّح الفرق: مكوّنين كل واحد $R = 0.9$:
- Series: $0.9 \times 0.9 = 0.81$
- Parallel: $1 - (0.1 \times 0.1) = 1 - 0.01 = 0.99$

يعني التكرار يرفع الموثوقية **أُسّيًا** — لهذا هو أساس هندسة الموثوقية.

**4.2 مقاييس الموثوقية** — ثلاثة مقاييس:

| المقياس | المعنى |
|---|---|
| **MTBF** | متوسط الزمن بين الأعطال (كل ما زاد أحسن) |
| **MTTR** | متوسط الزمن للإصلاح (كل ما قلّ أحسن) |
| **A** | التوفّر = نسبة الزمن اللي الخدمة شغّالة |

ومعادلة التوفّر:

$$A = \frac{MTBF}{MTBF + MTTR}$$

معناها واضح: كل ما زاد $MTBF$ (الخدمة تشتغل مدة أطول) أو قلّ $MTTR$ (نصلّح أسرع)، صار التوفّر أقرب لـ 1. والتوفّر العالي (>99.99%، وتسمى "four nines") ما توصلها بالبنية القوية بس — تحتاج **إجراءات أمنية استباقية** بعد، لأن الهجوم يقلّل $MTBF$ ويرفع $MTTR$ بنفس الوقت.

---

### القسم 5 — 5. Business Continuity in Web Application Security

#### ① النص الأصلي

> **5.1 Disaster Recovery Planning (DRP)**
>
> DRP ensures recovery from catastrophic events. In web application contexts, it involves:
>
> - Data replication across sites.
> - Recovery Time Objective (RTO): Maximum tolerable downtime.
> - Recovery Point Objective (RPO): Maximum acceptable data loss in time.
>
> **5.2 Incident Response Integration**
>
> Business continuity strategies incorporate security incident response, ensuring rapid containment of breaches. For example, continuity depends on whether a ransomware infection triggers full downtime or isolated containment.
>
> **5.3 Regulatory Alignment**
>
> Continuity strategies must adhere to frameworks such as ISO 22301 for business continuity management, integrated with ISO 27001 for information security.

#### ② الترجمة

> «**5.1 تخطيط التعافي من الكوارث (DRP)**
>
> يضمن الـ DRP التعافي من الأحداث الكارثية. وفي سياق تطبيقات الويب، يشمل:
>
> - تكرار البيانات عبر المواقع (data replication across sites).
> - هدف زمن التعافي (RTO): أقصى زمن توقّف يمكن تحمّله.
> - هدف نقطة التعافي (RPO): أقصى فقدان بيانات مقبول زمنيًا.
>
> **5.2 تكامل الاستجابة للحوادث**
>
> تدمج استراتيجيات استمرارية العمل الاستجابة للحوادث الأمنية، بما يضمن الاحتواء السريع للاختراقات. فمثلًا، تعتمد الاستمرارية على ما إذا كانت عدوى برامج الفدية تُسبّب توقّفًا كاملًا أم احتواءً معزولًا.
>
> **5.3 الامتثال التنظيمي**
>
> يجب أن تلتزم استراتيجيات الاستمرارية بأطر مثل ISO 22301 لإدارة استمرارية العمل، متكاملةً مع ISO 27001 لأمن المعلومات.»

#### ③ الشرح الفهمي

**5.1 تخطيط التعافي من الكوارث (DRP)** — الـ DRP هو الخطة اللي ترجّعك بعد الكارثة الكبرى. وعنده ثلاثة عناصر، أهمهم مصطلحين لازم ما يختلطون:

| المصطلح | التعريف | السؤال اللي يجاوب عليه |
|---|---|---|
| **RTO** (Recovery Time Objective) | أقصى زمن تعطّل يمكن تحمّله — يعني قدّيش نقدر نخلي الخدمة واقفة قبل ما نرجّعها | "شكد نتحمّل بدون خدمة؟" |
| **RPO** (Recovery Point Objective) | أقصى فقدان بيانات مقبول زمنيًا — يعني لأي نقطة زمنية نرجّع النسخة | "شكد بيانات نقدر نخسر؟" |

الفرق الجوهري بينهم: **RTO بُعد زمني للخدمة** (كم نتحمّل downtime)، و**RPO بُعد بياناتي** (لأي نقطة نرجّع). مثال يوضّح: لو $RPO = 1$ ساعة، لازم النسخ الاحتياطي (backup) يصير كل ساعة على الأقل — لأن أي بيانات بعد آخر نسخة راح تُفقد. ولو $RTO = 4$ ساعات، لازم نظام التعافي يرجّع الخدمة خلال 4 ساعات. أما العنصر الثالث فهو **تكرار البيانات عبر المواقع** (data replication across sites) اللي يسند الاثنين.

**5.2 تكامل الاستجابة للحوادث** — الاستمرارية مو منفصلة عن الاستجابة للحوادث الأمنية؛ لازم **الاحتواء (containment)** يصير سريع. المثال بالنص ذكي: لما تصير عدوى ransomware، الاستمرارية تعتمد على **مسار الحادثة** — هل تسحب النظام لتوقّف كامل (full downtime)؟ أو تحتوي العدوى معزولة (isolated containment) وتبقى باقي الخدمات شغّالة؟ الفرق بين الاثنين هو الفرق بين كارثة وعطل محدود.

**5.3 الامتثال التنظيمي** — الخطط مو "مزاج"؛ لازم تلتزم بأطر معيارية، وأهمها اثنين متكاملين:

| الإطار | يغطّي |
|---|---|
| **ISO 22301** | إدارة استمرارية العمل (Business Continuity Management) |
| **ISO 27001** | أمن المعلومات (Information Security) |

النقطة إنهم **متكاملين**: ISO 22301 يعطيك هيكل الاستمرارية، و ISO 27001 يعطيك الضوابط الأمنية ← فالمؤسسة الجدّية تجمع الاثنين لأن الاستمرارية بلا أمن ناقصة، والأمن بلا استمرارية ما ينفع وقت الكارثة.

---

![الصمود واستمرارية العمل|720](../06_Diagrams_&_Mindmaps/cy_w6_resilience.svg)
