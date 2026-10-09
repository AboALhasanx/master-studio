### القسم 1 — Cybersecurity as an Organizational Risk, Not Just a Technical Problem

#### ① النص الأصلي

> For much of its early history, cybersecurity was framed as a technical challenge: firewalls, antivirus software, and intrusion detection systems were considered sufficient to secure enterprise systems, and security problems were assumed to be "fixed" by deploying the right technological solution. However, the last two decades have demonstrated that cybersecurity failures are fundamentally organizational threats, often leading to financial loss, reputational damage, regulatory penalties, and even systemic risks to national security. It is critical to recognize that cybersecurity cannot be isolated within the IT department. Instead, it is a boardroom-level concern, requiring governance structures, risk management practices, and integration with organizational strategy.
>
> Why?
>
> - **Pervasive Digitization**: Every business process today depends on IT systems (finance, healthcare, supply chains), so cybersecurity failures can halt operations.
> - **Ecosystem Dependence**: Organizations rely on third-party vendors, cloud services, and global supply chains; a breach in one weak link (e.g., a vendor) can cascade into enterprise-level crises.
> - **Adversarial Nature**: Unlike natural risks (fires, floods), cyber risks are caused by adaptive, intelligent adversaries (hackers, nation-states, insiders).
> - **Legal/Regulatory Context**: Compliance obligations (GDPR, HIPAA, PCI-DSS) directly tie cybersecurity failures to legal liabilities and financial penalties.
>
> Thus, cybersecurity risks must be understood as enterprise-wide risks. Technical tools are only one layer in a larger governance and risk management framework.

#### ② الترجمة

> «على مدى معظم تاريخه المبكر، كان الأمن السيبراني يُصاغ كتحدٍّ تقني: كانت الجدران النارية (firewalls) وبرامج مكافحة الفيروسات وأنظمة كشف التسلل تُعدّ كافية لتأمين أنظمة المؤسسة، وكان يُفترض أن المشاكل الأمنية يمكن "إصلاحها" بنشر الحل التقني الصحيح. لكن العقدين الماضيين أثبتا أن إخفاقات الأمن السيبراني هي تهديدات تنظيمية بالأساس، كثيرًا ما تؤدي إلى خسائر مالية وضرر في السمعة وعقوبات تنظيمية وحتى مخاطر نظامية على الأمن القومي. من الضروري إدراك أن الأمن السيبراني لا يمكن عزله داخل قسم تقنية المعلومات (IT). بل هو شأن على مستوى مجلس الإدارة، يتطلب هياكل حوكمة وممارسات إدارة مخاطر ودمجًا مع استراتيجية المؤسسة.
>
> لماذا؟
>
> - **الرقمنة الشاملة (Pervasive Digitization)**: كل عملية تجارية اليوم تعتمد على أنظمة تقنية المعلومات (المالية، الرعاية الصحية، سلاسل التوريد)، لذا قد تُوقف إخفاقات الأمن السيبراني العمليات.
> - **الاعتماد على المنظومة (Ecosystem Dependence)**: تعتمد المؤسسات على موردين خارجيين وخدمات سحابية وسلاسل توريد عالمية؛ واختراق في حلقة ضعيفة واحدة (مثل مورّد) قد يتسلسل إلى أزمات على مستوى المؤسسة.
> - **الطبيعة العدائية (Adversarial Nature)**: على عكس المخاطر الطبيعية (الحرائق والفيضانات)، تُسبَّب المخاطر السيبرانية من خصوم متكيّفين وأذكياء (قراصنة، دول، عناصر داخلية).
> - **السياق القانوني/التنظيمي (Legal/Regulatory Context)**: تُربط التزامات الامتثال (GDPR، HIPAA، PCI-DSS) إخفاقات الأمن السيبراني مباشرة بالمسؤوليات القانونية والعقوبات المالية.
>
> وبالتالي، يجب فهم مخاطر الأمن السيبراني كمخاطر على مستوى المؤسسة بأكملها. الأدوات التقنية ليست سوى طبقة واحدة داخل إطار أوسع للحوكمة وإدارة المخاطر.»

#### ③ الشرح الفهمي

الفكرة الأساسية هنا إنه الأمن السيبراني مو مجرد "مشكلة تقنية" تنحلّ بالجدار الناري والأنتي فايرس. هاي كانت النظرة القديمة، وطلع خطأ كبير. الإخفاق الأمني اليوم هو **threat على مستوى المؤسسة**، يعني يوصل للمالية والسمعة والعقوبات القانونية وحتى الأمن القومي.

ليش صار هيك؟ لأن المؤسسة صارت مبنية على الـ IT من رأسها لرجلها، وكل عملية تجارية (payroll، logistics، finance) معلّقة على الأنظمة. فلمّا يخترقونها، العمليات توقف مو بس الأجهزة.

أهم نقطة في القسم: **الأمن السيبراني ما ينعزل داخل قسم الـ IT** — هو شأن على مستوى **مجلس الإدارة (boardroom)**, يحتاج حوكمة وإدارة مخاطر وربطه بالاستراتيجية.

نلخّص الأسباب الأربعة بهذا الجدول:

| السبب | المعنى بالفهم البسيط | مثال من النص |
|---|---|---|
| Pervasive Digitization | كل شي صار معلّق على الـ IT | finance, healthcare, supply chains |
| Ecosystem Dependence | نعتمد على طرف ثالث وسحابة وسلاسل توريد | اختراق مورّد واحد ← أزمة على مستوى المؤسسة |
| Adversarial Nature | الخصم ذكي ومتكيّف، مو مخاطرة طبيعية | hackers, nation-states, insiders |
| Legal/Regulatory Context | الامتثال يربط الفشل بالمسؤولية القانونية | GDPR, HIPAA, PCI-DSS |

الخلاصة اللي لازم تحفظها: الخطر السيبراني هو **enterprise-wide risk**، والأدوات التقنية طبقة وحدة فقط داخل إطار الحوكمة وإدارة المخاطر.

🎯 **تأشيرة الدكتورة:** محدّدة بالـ yellow = مهمة للامتحان: جملة "It is critical to recognize that cybersecurity cannot be isolated within the IT department…" + كلمة "Why?" + تسميات البوليتات الأربعة (Pervasive Digitization · Ecosystem Dependence · Adversarial Nature · Legal/Regulatory Context).

---

### القسم 2 — Why Risk Management is a Strategic Necessity

#### ① النص الأصلي

> Risk management in cybersecurity ensures organizations can anticipate, prioritize, and mitigate risks before they escalate into crises. Its necessity can be explained through three main dimensions: financial, operational, and reputational.
>
> **2.1 Financial Risk** — The direct financial cost of cyberattacks has grown exponentially.
>
> Sources of Financial Loss:
>
> - Incident Response Costs.
> - Business Disruption.
> - Legal Penalties.
> - Ransom Payments.
> - Litigation.
>
> Mathematical framing of Expected Financial Loss (EFL):
>
> $$EFL = \sum_{i=1}^{n} P_i \cdot I_i$$
>
> This model allows CISOs and executives to prioritize investments in cybersecurity controls.
>
> **2.2 Operational Risk** — Cybersecurity failures often result in operational paralysis, which is why cybersecurity must integrate with business continuity planning. Risk management ensures organizations can keep functioning even under attack, through backups, redundancies, and incident response planning.
>
> **2.3 Reputational Risk** — Trust is one of the most valuable assets for organizations, and a cybersecurity breach can irreparably damage customer confidence; reputation once lost is hard to restore. For financial institutions, healthcare providers, or e-commerce companies, reputation directly correlates with customer retention and revenue streams.

#### ② الترجمة

> «إدارة المخاطر في الأمن السيبراني تضمن أن المؤسسات تستطيع أن تتوقّع المخاطر وتحدّد أولوياتها وتخفّفها قبل أن تتصاعد إلى أزمات. وتُفسَّر ضرورتها من خلال ثلاثة أبعاد رئيسية: المالي والتشغيلي والسمعة.
>
> **2.1 المخاطر المالية** — التكلفة المالية المباشرة للهجمات السيبرانية نمت نموًّا أُسّيًّا.
>
> مصادر الخسارة المالية:
>
> - تكاليف الاستجابة للحوادث (Incident Response Costs).
> - تعطُّل الأعمال (Business Disruption).
> - العقوبات القانونية (Legal Penalties).
> - مدفوعات الفدية (Ransom Payments).
> - التقاضي (Litigation).
>
> الصياغة الرياضية للخسارة المالية المتوقعة (EFL):
>
> $$EFL = \sum_{i=1}^{n} P_i \cdot I_i$$
>
> هذا النموذج يمكّن مديري أمن المعلومات (CISOs) والمديرين التنفيذيين من ترتيب أولويات الاستثمار في ضوابط الأمن السيبراني.
>
> **2.2 المخاطر التشغيلية** — كثيرًا ما تؤدي إخفاقات الأمن السيبراني إلى شلل تشغيلي، ولهذا يجب أن يتكامل الأمن السيبراني مع تخطيط استمرارية الأعمال. إدارة المخاطر تضمن أن المؤسسات تبقى قادرة على العمل حتى تحت الهجوم، عبر النسخ الاحتياطية والتكرارية وتخطيط الاستجابة للحوادث.
>
> **2.3 مخاطر السمعة** — الثقة من أثمن أصول المؤسسة، وقد يُلحق اختراق أمني ضررًا لا يُصلَح بثقة العملاء؛ والسمعة متى ما ضاعت يصعب استرجاعها. بالنسبة للمؤسسات المالية أو مزوّدي الرعاية الصحية أو شركات التجارة الإلكترونية، ترتبط السمعة مباشرة بالاحتفاظ بالعملاء وتدفقات الإيرادات.»

#### ③ الشرح الفهمي

ليش إدارة المخاطر "ضرورة استراتيجية" مو مجرد كماليات؟ لأنها تخلي المؤسسة **تتوقّع وترتّب وتخفّف** قبل ما تصير الأزمة. والضرورة تنجلي بثلاث أبعاد: **financial, operational, reputational**.

**البُعد المالي (Financial)** — التكلفة تكبر بشكل أُسّي. النص يعدّ خمس مصادر للخسارة:

| المصدر | شنو يعني |
|---|---|
| Incident Response Costs | تكاليف الاستجابة للحادث (تحقيق، استرجاع) |
| Business Disruption | توقف الأعمال عن العمل |
| Legal Penalties | عقوبات قانونية / غرامات |
| Ransom Payments | دفع الفدية للقراصنة |
| Litigation | الدعاوى القضائية |

ويجي أهم شي: الصيغة الرياضية للـ **Expected Financial Loss**:

$$EFL = \sum_{i=1}^{n} P_i \cdot I_i$$

| الرمز | المعنى |
|---|---|
| $EFL$ | الخسارة المالية المتوقعة (Expected Financial Loss) |
| $P_i$ | احتمال وقوع الحدث السيبراني $i$ |
| $I_i$ | التأثير المالي للحدث $i$ |
| $n$ | عدد الأحداث المحتملة |

يعني: نضرب احتمال كل حدث بتأثيره المالي، ونجمعهم. هذا يخلي الـ CISO يقنع الإدارة وين يصرف الفلوس على الضوابط.

**البُعد التشغيلي (Operational)** — الفشل الأمني يسبّب **operational paralysis** (شلل تشغيلي). الحل: نربط الأمن السيبراني بـ **business continuity planning** — backups, redundancies, incident response planning — حتى المؤسسة تكمّل شغل حتى وهي تحت الهجوم.

**البُعد السمعة (Reputational)** — **الثقة (trust)** رأس مال ما يُقدّر بثمن. الاختراق يكسر ثقة العميل، والسمعة **مرة تروح صعب ترجع**. وعند البنوك والمستشفيات وشركات الـ e-commerce، السمعة مرتبطة مباشرة بالاحتفاظ بالعملاء والإيرادات.

الخلاصة: الأبعاد الثلاثة مترابطة — ضربة أمنية وحدة تضرب المال والتشغيل والسمعة بنفس الوقت.

![الأبعاد الثلاثة لضرورة إدارة المخاطر|560](../06_Diagrams_&_Mindmaps/cy_w3_risk_dimensions.svg)
