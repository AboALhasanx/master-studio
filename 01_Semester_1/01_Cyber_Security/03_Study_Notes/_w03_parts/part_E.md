### القسم 1 — Definition of Security Policies in Cybersecurity
#### ① النص الأصلي
> A security policy is a high-level organizational document that sets out rules, expectations, and guidelines for securing information assets. It is not a technical manual but a governance tool, ensuring that people, processes, and technologies work together toward the same security objectives.
>
> Characteristics of Security Policies:
>
> - High-Level Guidance: Focuses on "what" must be done, not necessarily "how."
> - Alignment with Risk: Derived from risk assessments to address actual threats.
> - Organization-Wide: Applies across departments, employees, contractors, and even third parties.
> - Living Document: Policies evolve as threats, technologies, and regulations change.
>
> Examples:
>
> - Acceptable Use Policy (AUP): Defines what employees can/cannot do on corporate systems.
> - Data Handling Policy: Specifies rules for classifying, storing, and transmitting data.
> - Incident Response Policy: Outlines responsibilities and escalation steps during a cyber incident.
>
> Thus, policies bridge strategic objectives with operational controls, making them indispensable for effective cybersecurity governance.
#### ② الترجمة
> «السياسة الأمنية (security policy) هي وثيقة تنظيمية عالية المستوى تحدّد القواعد والتوقّعات والإرشادات لحماية أصول المعلومات (information assets). وهي ليست دليلاً تقنياً بل أداة حوكمة (governance tool)، تضمن أن يعمل الأفراد والعمليات والتقنيات معاً نحو نفس أهداف الأمان.»
>
> «خصائص السياسات الأمنية (Characteristics of Security Policies):»
>
> - «إرشاد عالي المستوى (High-Level Guidance): تركّز على "ماذا" يجب أن يُفعَل، وليس بالضرورة "كيف".»
> - «التوافق مع المخاطر (Alignment with Risk): مستمدّة من تقييمات المخاطر (risk assessments) لمعالجة التهديدات الفعلية.»
> - «شاملة للمنظمة (Organization-Wide): تنطبق على الأقسام والموظفين والمتعاقدين وحتى الأطراف الثالثة.»
> - «وثيقة حيّة (Living Document): تتطوّر السياسات مع تغيّر التهديدات والتقنيات واللوائح.»
>
> «أمثلة (Examples):»
>
> - «سياسة الاستخدام المقبول (AUP): تحدّد ما يجوز للموظفين فعله أو عدم فعله على أنظمة الشركة.»
> - «سياسة التعامل مع البيانات (Data Handling Policy): تحدّد قواعد تصنيف البيانات وتخزينها ونقلها.»
> - «سياسة الاستجابة للحوادث (Incident Response Policy): تبيّن المسؤوليات وخطوات التصعيد أثناء حادث سيبراني.»
>
> «وهكذا، تربط السياسات الأهداف الاستراتيجية بالضوابط التشغيلية (operational controls)، ما يجعلها لا غنى عنها لحوكمة أمن سيبراني فعّالة.»
#### ③ الشرح الفهمي
السياسة الأمنية مو "برنامج" ولا "فايروول" — هي **وثيقة حوكمة**. يعني كلام مكتوب يقول: شنو القواعد، وشنو المتوقّع من الناس، وشنو الإرشادات لحماية أصول المعلومات. الفكرة المهمة: هي تخلّي الناس + العمليات + التقنيات يمشون بنفس الاتجاه (نفس أهداف الأمان)، بدل كل واحد يسوي شي من راسه.

نقطة أساسية بالتعريف: هي **مو technical manual** — يعني ما تشرح لك خطوة بخطوة كيف تضبط الجهاز، بس تقول "شنو" المطلوب. الجدول يوضّح شنو تعني كل خاصية:

| الخاصية | المعنى بالمختصر |
|---|---|
| High-Level Guidance | تقول "شنو" المطلوب، مو "كيف" تفنّياً |
| Alignment with Risk | مبنية على risk assessments حتى تعالج تهديدات حقيقية |
| Organization-Wide | تشمل الكل: أقسام، موظفين، متعاقدين، أطراف ثالثة |
| Living Document | تتحدّث باستمرار مع تغيّر التهديدات والتقنيات واللوائح |

الفرق اللي تربطه بالجملة الأخيرة: السياسات هي **الجسر** بين الأهداف الاستراتيجية (اللي يريدها الإدارة) والضوابط التشغيلية (اللي تنفّذها التقنية)، ولهذا هي indispensable للـ governance.

🎯 **تأشيرة الدكتورة:** «Characteristics of Security Policies» مظلّلة = **مطلوبة للامتحان**. أما فقرة التعريف وقائمة «Examples» فمشطوبة بالأحمر = **غير مطلوبة للامتحان** (مذكورة هنا للمرجعية فقط).

### القسم 2 — Policy vs. Technology: Complementary Roles
#### ① النص الأصلي
> Students often assume that deploying advanced security tools (firewalls, IDS, EDR systems) guarantees security. However, technology without policy is directionless.
>
> Policy as Guidance: Policies define the objectives, scope, and acceptable practices. Example: "All passwords must be at least 12 characters, with complexity requirements."
>
> Technology as Enforcement — tools implement and enforce policy:
>
> - Password managers enforce length/complexity.
> - Firewalls enforce network segmentation policies.
> - SIEM systems enforce monitoring policies.
>
> Why Both Are Needed:
>
> - Policy without Technology: A strong password policy written on paper but no enforcement → employees set "123456."
> - Technology without Policy: A sophisticated SIEM system but no defined policy on incident escalation → alerts ignored.
>
> This symbiosis illustrates why cybersecurity is socio-technical, involving both human governance and technological enforcement.
#### ② الترجمة
> «كثيراً ما يفترض الطلبة أن نشر أدوات أمنية متقدّمة (firewalls, IDS, EDR systems) يضمن الأمان. لكن التقنية بدون سياسة تكون بلا اتجاه.»
>
> «السياسة كإرشاد (Policy as Guidance): تحدّد السياسات الأهداف والنطاق والممارسات المقبولة. مثال: "يجب أن تكون كل كلمات المرور 12 حرفاً على الأقل، مع متطلبات تعقيد (complexity requirements)."»
>
> «التقنية كتنفيذ (Technology as Enforcement) — الأدوات تُنفّذ السياسة وتفرضها:»
>
> - «مديرو كلمات المرور (Password managers) يفرضون الطول والتعقيد.»
> - «الجدران النارية (Firewalls) تفرض سياسات تقسيم الشبكة (network segmentation).»
> - «أنظمة SIEM تفرض سياسات المراقبة (monitoring policies).»
>
> «لماذا نحتاج الاثنين معاً (Why Both Are Needed):»
>
> - «سياسة بدون تقنية (Policy without Technology): سياسة كلمات مرور قوية على ورق لكن بلا تنفيذ ← الموظفون يضعون "123456".»
> - «تقنية بدون سياسة (Technology without Policy): نظام SIEM متطوّر لكن بلا سياسة محدّدة للتصعيد عند الحوادث ← التنبيهات تُتجاهَل.»
>
> «هذا التكافل (symbiosis) يوضّح لماذا الأمن السيبراني اجتماعي-تقني (socio-technical)، لأنه يشمل الحوكمة البشرية والتنفيذ التقني معاً.»
#### ③ الشرح الفهمي
القسم هذا يرد على فكرة غلط شائعة عند الطلبة: "إذا جبت أدوات أمنية قوية خلاص صرت آمن". الجواب: **لأ**. التقنية لحالها بلا سياسة تكون بلا اتجاه (directionless)، لأن الأداة ما تعرف شنو المفروض تسوي إلا إذا فيه سياسة تحدّد الهدف.

التقسيم واضح:
- **Policy** = إرشاد (Guidance) ← تحدّد الهدف والنطاق والممارسة المقبولة.
- **Technology** = تنفيذ (Enforcement) ← الأدوات تجيب النتيجة وتفرض القاعدة.

والنقطة الأهم هي جدول "ليش الاثنين ضروريين":

| الحالة | النتيجة |
|---|---|
| Policy بدون Technology | سياسة قوية مكتوبة بس بلا فرض ← الناس تكتب "123456" |
| Technology بدون Policy | نظام SIEM قوي بس بلا سياسة تصعيد ← التنبيهات تُتجاهَل |

الخلاصة: الاثنين يعتمدون على بعض (symbiosis)، ولهذا نقول الأمن **socio-technical** — نص بشر (governance) ونص تقنية (enforcement). يعني الاثنين لا يتجزّون.

🎯 **تأشيرة الدكتورة:** هذا القسم **كامل مشطوب بالأحمر = غير مطلوب للامتحان**. مذكور هنا للفهم والمرجعية فقط، مو ضمن مادة الامتحان.

### القسم 3 — Challenges in Policy Creation and Enforcement
#### ① النص الأصلي
> Developing policies is straightforward. Enforcing and maintaining them across organizations is the real challenge.
>
> 3.1 User Resistance:
>
> - Employees often view security policies as burdensome (e.g., frequent password changes).
> - Resistance increases when policies reduce convenience without clear communication of benefits.
>
> 3.2 Lack of Enforcement:
>
> - Policies are ineffective without technical and administrative enforcement.
> - Many organizations have well-written policies that remain unenforced due to weak monitoring or lack of executive backing.
>
> 3.3 Outdated Policies:
>
> - Technology evolves rapidly, but policies often lag behind.
> - Example: An outdated AUP may not address risks from cloud services or personal mobile devices.
>
> 3.4 Cultural Barriers:
>
> - In some organizations, especially those with legacy IT practices, employees treat security as "IT's job" rather than a shared responsibility.
>
> Lesson: Policy enforcement must be practical, consistent, and continuously updated.
#### ② الترجمة
> «كتابة السياسات أمر مباشر وسهل. لكن فرضها والحفاظ عليها عبر المنظمة هو التحدّي الحقيقي.»
>
> «3.1 مقاومة المستخدمين (User Resistance):»
>
> - «غالباً ما يرى الموظفون السياسات الأمنية عبئاً (مثل التغيير المتكرّر لكلمات المرور).»
> - «تزداد المقاومة عندما تقلّل السياسات الراحة دون توضيح الفوائد بشكل واضح.»
>
> «3.2 غياب التنفيذ (Lack of Enforcement):»
>
> - «السياسات غير فعّالة بدون فرض تقني وإداري.»
> - «كثير من المنظمات لديها سياسات مكتوبة جيداً لكنها تبقى غير مُنفَّذة بسبب ضعف المراقبة أو غياب دعم الإدارة التنفيذية.»
>
> «3.3 السياسات القديمة (Outdated Policies):»
>
> - «تتطوّر التقنية بسرعة، لكن السياسات غالباً تتأخّر عنها.»
> - «مثال: سياسة AUP قديمة قد لا تعالج مخاطر الخدمات السحابية (cloud services) أو الأجهزة المحمولة الشخصية.»
>
> «3.4 الحواجز الثقافية (Cultural Barriers):»
>
> - «في بعض المنظمات، وخاصة ذات الممارسات التقنية القديمة (legacy IT)، يعتبر الموظفون الأمن "شغل قسم IT" وليس مسؤولية مشتركة.»
>
> «الدرس (Lesson): يجب أن يكون فرض السياسة عملياً ومتّسقاً ومحدَّثاً باستمرار.»
#### ③ الشرح الفهمي
المعنى بالمختصر: **كتابة السياسة سهلة، بس فرضها هو المشكلة**. أربع عقبات أساسية، وكل واحدة إلها سبب:

| التحدّي | شنو يصير |
|---|---|
| User Resistance | الموظف يشوف السياسة عبء (خصوصاً تغيير كلمة المرور المتكرّر)، والمقاومة تزيد إذا قلّلت الراحة بلا شرح الفائدة |
| Lack of Enforcement | سياسة مكتوبة حلو بس ما تنفرض ← ضعف المراقبة أو ما فيه دعم من الإدارة العليا |
| Outdated Policies | التقنية تتطوّر والسياسة تتأخّر ← سياسة AUP قديمة ما تعالج cloud أو الأجهزة الشخصية |
| Cultural Barriers | الموظف يقول "هذا شغل IT مو شغلي" ← الأمن مسؤولية مشتركة مو حصرية على قسم |

الـ **Lesson** هو الخلاصة العملية: الفرض لازم يكون **practical** (واقعي)، **consistent** (ثابت على الكل)، و**continuously updated** (يتحدّث باستمرار).

### القسم 4 — Policy Lifecycle
#### ① النص الأصلي
> A security policy is not static — it must follow a lifecycle approach to remain relevant.
>
> Step 1: Draft (Based on Risk Assessments):
>
> - Drafting begins with identifying risks from frameworks (OCTAVE, NIST SP 800-30).
> - Example: A university detects rising phishing attempts → drafts an email security policy.
>
> Step 2: Approval (Executive Buy-In):
>
> - Policies require endorsement from senior leadership (CIO, CISO, Board).
> - Executive buy-in ensures policies are treated as strategic, not optional.
>
> Step 3: Communication (Training and Awareness):
>
> - Policies must be communicated to all stakeholders.
> - Training ensures employees understand not only "what" the rules are but also "why" they matter.
> - Example: Simulated phishing campaigns raise awareness of email security policies.
>
> Step 4: Enforcement (Monitoring and Disciplinary Measures):
>
> - Enforcement mechanisms include technical controls (firewalls, access controls) and administrative measures (warnings, HR interventions).
> - Example: Enforcing acceptable use policy through web proxies blocking non-work-related sites.
>
> Step 5: Review & Update:
>
> - Policies must be regularly reviewed to reflect evolving threats, regulations, and technologies.
> - Example: Updates to GDPR in Europe required revising data handling policies across many organizations.
>
> Lifecycle Principle: A policy is effective only if it is dynamic and cyclical, not one-time.
#### ② الترجمة
> «السياسة الأمنية ليست ثابتة — يجب أن تتبع نهج دورة حياة (lifecycle approach) حتى تبقى ذات صلة.»
>
> «الخطوة 1: الصياغة (Draft) — بناءً على تقييمات المخاطر:»
>
> - «تبدأ الصياغة بتحديد المخاطر من أطر عمل (frameworks) مثل OCTAVE و NIST SP 800-30.»
> - «مثال: جامعة تلاحظ تصاعد محاولات التصيّد (phishing) ← تصوغ سياسة أمن البريد الإلكتروني.»
>
> «الخطوة 2: الموافقة (Approval) — تأييد الإدارة التنفيذية:»
>
> - «تتطلّب السياسات تأييد القيادة العليا (CIO, CISO, Board).»
> - «تأييد الإدارة التنفيذية يضمن أن تُعامَل السياسات كاستراتيجية وليست اختيارية.»
>
> «الخطوة 3: التواصل (Communication) — التدريب والتوعية:»
>
> - «يجب إيصال السياسات إلى جميع أصحاب المصلحة (stakeholders).»
> - «التدريب يضمن أن يفهم الموظفون ليس فقط "ماذا" هي القواعد بل أيضاً "لماذا" هي مهمّة.»
> - «مثال: حملات التصيّد المحاكاة (simulated phishing) ترفع الوعي بسياسات أمن البريد.»
>
> «الخطوة 4: الفرض (Enforcement) — المراقبة والإجراءات التأديبية:»
>
> - «تشمل آليات الفرض ضوابط تقنية (firewalls, access controls) وإجراءات إدارية (إنذارات، تدخّل الموارد البشرية).»
> - «مثال: فرض سياسة الاستخدام المقبول عبر وكلاء الويب (web proxies) التي تحجب المواقع غير المتعلّقة بالعمل.»
>
> «الخطوة 5: المراجعة والتحديث (Review & Update):»
>
> - «يجب مراجعة السياسات بانتظام لتعكس التهديدات واللوائح والتقنيات المتطوّرة.»
> - «مثال: تحديثات GDPR في أوروبا استلزمت تعديل سياسات التعامل مع البيانات في منظمات كثيرة.»
>
> «مبدأ دورة الحياة (Lifecycle Principle): السياسة تكون فعّالة فقط إذا كانت ديناميكية ودورية (dynamic and cyclical)، وليست لمرة واحدة.»
#### ③ الشرح الفهمي
الفكرة الأساسية: السياسة **مو وثيقة تكتبها مرة وتنساها** — هي دورة مستمرة. خمس خطوات لازم تمر بها بالترتيب:

| الخطوة | شنو يصير فيها |
|---|---|
| 1. Draft | الصياغة تبدأ من تحديد المخاطر باستعمال frameworks مثل OCTAVE و NIST SP 800-30 |
| 2. Approval | لازم تأييد من القيادة العليا (CIO/CISO/Board) حتى تُعامَل كاستراتيجية مو اختيارية |
| 3. Communication | إيصال السياسة للكل + تدريب يشرح "شنو" و"ليش" — مثال: simulated phishing |
| 4. Enforcement | فرض تقني (firewalls, access controls) + إداري (إنذارات، تدخّل HR) |
| 5. Review & Update | مراجعة دورية تعكس التهديدات واللوائح الجديدة — مثال: تحديثات GDPR |

لاحظ الترتيب المنطقي: أول شي **تكتبها** (Draft)، بعدين **توافق عليها** (Approval)، بعدين **تفهّم الناس** (Communication)، بعدين **تفرضها** (Enforcement)، وأخيراً **تراجعها** (Review). والـ **Lifecycle Principle** هي الزبدة: السياسة لازم تكون dynamic + cyclical، يعني تدور الدورة من جديد، مو شي one-time.

🎯 **تأشيرة الدكتورة:** عنوان «6. Policy Lifecycle» **مظلّل بالأصفر = مطلوب للامتحان** (احفظ الخطوات الخمس بالترتيب).

![دورة حياة السياسة — 5 خطوات|760](../06_Diagrams_&_Mindmaps/cy_w3_policy_lifecycle.svg)

### القسم 5 — Mathematical Model: Policy Effectiveness
#### ① النص الأصلي
> The success of policies must be measurable. One approach is to evaluate the reduction in security incidents after policy enforcement.
>
> $$PE = \frac{Incidents_{before} - Incidents_{after}}{Incidents_{before}}$$
>
> Where:
>
> - $Incidents_{before}$ is the number of incidents before policy enforcement.
> - $Incidents_{after}$ is the number of incidents after enforcement.
> - $PE$ is the Policy Effectiveness, expressed as a percentage.
>
> Example Calculation:
>
> - Brute-force login attempts: 200 incidents (before policy).
> - After enforcing MFA: 20 incidents.
> - $PE = \frac{200 - 20}{200} = 0.9 = 90\%$
>
> This demonstrates that the MFA policy reduced brute-force incidents by 90%. Such models allow CISOs to justify policy investments with quantifiable evidence.
#### ② الترجمة
> «يجب أن يكون نجاح السياسات قابلاً للقياس. ومن الأساليب المتبعة تقييم مقدار الانخفاض في الحوادث الأمنية بعد فرض السياسة.»
>
> $$PE = \frac{Incidents_{before} - Incidents_{after}}{Incidents_{before}}$$
>
> «حيث (Where):»
>
> - «$Incidents_{before}$ هو عدد الحوادث قبل فرض السياسة.»
> - «$Incidents_{after}$ هو عدد الحوادث بعد الفرض.»
> - «$PE$ هي فعالية السياسة (Policy Effectiveness)، وتُعبَّر عنها كنسبة مئوية.»
>
> «مثال حسابي (Example Calculation):»
>
> - «محاولات تسجيل الدخول بالقوة الغاشمة (brute-force): 200 حادثة (قبل السياسة).»
> - «بعد فرض MFA: 20 حادثة.»
> - «$PE = \frac{200 - 20}{200} = 0.9 = 90\%$»
>
> «يوضّح هذا أن سياسة MFA قلّلت حوادث القوة الغاشمة بنسبة 90%. ومثل هذه النماذج تمكّن مديري أمن المعلومات (CISOs) من تبرير الاستثمار في السياسات بأدلّة قابلة للقياس.»
#### ③ الشرح الفهمي
هنا القسم يجاوب على سؤال: **شلون نعرف إن السياسة نجحت؟** الجواب: نقيس الانخفاض بحوادث الأمان قبل وبعد الفرض. النسبة تسمّى فعالية السياسة (Policy Effectiveness, PE).

$$PE = \frac{Incidents_{before} - Incidents_{after}}{Incidents_{before}}$$

| الرمز | المعنى |
|---|---|
| $PE$ | فعالية السياسة (Policy Effectiveness)، تُعبَّر عنها كنسبة مئوية |
| $Incidents_{before}$ | عدد الحوادث قبل فرض السياسة |
| $Incidents_{after}$ | عدد الحوادث بعد فرض السياسة |

المثال: كان عندك 200 حادثة brute-force، وبعد ما فرضت MFA صارت 20 حادثة:

$$PE = \frac{200 - 20}{200} = \frac{180}{200} = 0.9 = 90\%$$

يعني سياسة MFA خفّضت الحوادث بـ 90%. الفائدة العملية: هذا الرقم يعطي الـ CISO دليل رقمي (quantifiable evidence) يقنع فيه الإدارة إن الاستثمار بالسياسة كان يستحق.

### القسم 6 — The Strategic Role of Policies in Cybersecurity
#### ① النص الأصلي
> Policies serve as the translation layer between:
>
> - Technical Controls: Firewalls, IDS, VPNs.
> - Organizational Governance: Risk management, compliance, board oversight.
>
> They provide:
>
> 1. Consistency: Standardizing practices across the enterprise.
> 2. Accountability: Defining responsibilities (who can access what, and under which conditions).
> 3. Compliance: Ensuring alignment with external regulations (GDPR, HIPAA, PCI-DSS).
> 4. Culture: Embedding security into everyday behavior.
>
> In an enterprise context, policies shift cybersecurity from a reactive IT function into a proactive organizational strategy.
#### ② الترجمة
> «تعمل السياسات كطبقة ترجمة (translation layer) بين:»
>
> - «الضوابط التقنية (Technical Controls): الجدران النارية، أنظمة كشف التسلل (IDS)، الشبكات الافتراضية الخاصة (VPNs).»
> - «الحوكمة التنظيمية (Organizational Governance): إدارة المخاطر، الامتثال، إشراف مجلس الإدارة.»
>
> «وهي توفّر:»
>
> 1. «الاتساق (Consistency): توحيد الممارسات عبر المنظمة.»
> 2. «المساءلة (Accountability): تحديد المسؤوليات (من يستطيع الوصول إلى ماذا، وتحت أي شروط).»
> 3. «الامتثال (Compliance): ضمان التوافق مع اللوائح الخارجية (GDPR, HIPAA, PCI-DSS).»
> 4. «الثقافة (Culture): دمج الأمن في السلوك اليومي.»
>
> «وفي سياق المنظمة، تنقل السياسات الأمن السيبراني من وظيفة IT تفاعلية (reactive) إلى استراتيجية تنظيمية استباقية (proactive).»
#### ③ الشرح الفهمي
الفكرة الأساسية: السياسة هي **translation layer** — يعني المترجم بين عالمين: من جهة الضوابط التقنية (firewalls, IDS, VPNs)، ومن جهة الحوكمة التنظيمية (risk management, compliance, board oversight). بدون هذا المترجم، كل جهة تشتغل لحالها.

و"شنو توفّر" هي القائمة المهمة — أربع أشياء:

| ما توفّره | المعنى |
|---|---|
| Consistency | توحيد الممارسات على مستوى المنظمة كلها |
| Accountability | تحديد من مسؤول عن شنو، ومن يوصل لشنو وبأي شروط |
| Compliance | التوافق مع اللوائح الخارجية (GDPR, HIPAA, PCI-DSS) |
| Culture | دمج الأمن بالسلوك اليومي للناس |

الخلاصة بالجملة الأخيرة: وجود السياسات يحوّل الأمن السيبراني من **reactive** (رد فعل داخل قسم IT) إلى **proactive** (استراتيجية على مستوى المنظمة).
