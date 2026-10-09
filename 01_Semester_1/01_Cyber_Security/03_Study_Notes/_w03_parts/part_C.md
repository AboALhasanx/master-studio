### القسم 1 — Understanding Risk in the Cybersecurity Context

#### ① النص الأصلي

> Risk in cybersecurity is not an abstract concept — it is the quantifiable possibility that a threat actor exploits a vulnerability to damage organizational assets. Such risk could result in financial loss, operational disruption, reputational damage, or legal liability.
>
> In formal terms, risk is expressed as:
>
> $$Risk = Threat \times Vulnerability \times Impact$$
>
> Where:
>
> - **Likelihood**: Probability that a threat will exploit a vulnerability.
> - **Impact**: Potential damage (financial, reputational, operational).
>
> This simple equation is foundational in cybersecurity. It illustrates that risk can be minimized in two ways:
>
> - **Reduce likelihood**: through preventive measures (patching, firewalls, training).
> - **Reduce impact**: through resilience (backups, incident response, cyber insurance).
>
> **Extended Mathematical Framing** — Risk can also be aggregated across multiple threats:
>
> $$Risk = \sum_{i=1}^{n} P_i \cdot I_i$$
>
> Where:
>
> - $P_i$: probability of attack $i$.
> - $I_i$: impact of attack $i$.
>
> For example, a phishing campaign ($P_1$) might have a high likelihood but low impact per event, while a zero-day exploit ($P_2$) may have a low likelihood but catastrophic impact. Risk management requires balancing both dimensions. This quantitative framing therefore provides organizations with a rational basis for decision-making in resource allocation and security investments.

#### ② الترجمة

> «المخاطرة في الأمن السيبراني مو مفهوم مجرّد — هي الاحتمال القابل للقياس أن يستغلّ جهة تهديد (threat actor) ثغرة (vulnerability) لإلحاق الضرر بأصول المؤسسة. وهذي المخاطرة قد تنتج خسارة مالية، أو تعطّلًا تشغيليًا، أو ضررًا في السمعة، أو مسؤولية قانونية.
>
> بالصيغة الرسمية، تُعبَّر المخاطرة عن:
>
> $$Risk = Threat \times Vulnerability \times Impact$$
>
> حيث:
>
> - **Likelihood (الاحتمالية)**: احتمال أن يستغلّ التهديد ثغرة معينة.
> - **Impact (الأثر)**: الضرر المحتمل (مالي، سمعة، تشغيلي).
>
> هذي المعادلة البسيطة أساسية في الأمن السيبراني، وهي توضّح أن المخاطرة يمكن تقليلها بطريقتين:
>
> - **تقليل الاحتمالية (Reduce likelihood)**: عبر إجراءات وقائية (patching، firewalls، تدريب).
> - **تقليل الأثر (Reduce impact)**: عبر المرونة (backups، الاستجابة للحوادث، التأمين السيبراني).
>
> **الإطار الرياضي الموسّع (Extended Mathematical Framing)** — يمكن أيضًا تجميع المخاطرة عبر تهديدات متعددة:
>
> $$Risk = \sum_{i=1}^{n} P_i \cdot I_i$$
>
> حيث:
>
> - $P_i$: احتمال الهجوم $i$.
> - $I_i$: أثر الهجوم $i$.
>
> مثلًا، حملة تصيّد (phishing campaign) ($P_1$) قد يكون احتمالها عاليًا لكن أثرها لكل حدث منخفض، بينما ثغرة يوم الصفر (zero-day exploit) ($P_2$) قد يكون احتمالها منخفضًا لكن أثرها كارثي. إدارة المخاطر تتطلّب موازنة البعدين. ولهذا، هذي الصياغة الكمّية توفّر للمؤسسات أساسًا عقلانيًا لاتخاذ القرار في تخصيص الموارد والاستثمارات الأمنية.»

#### ③ الشرح الفهمي

الفكرة الأساسية هنا إنه المخاطرة مو شي "معنوي" أو مجرد خوف — هي **شي يُقاس**. التعريف: احتمال أن جهة تهديد (threat actor) تستغل ثغرة (vulnerability) وتأذي أصول المؤسسة. والنتيجة ممكن تكون: خسارة مالية، تعطّل تشغيلي، ضرر سمعة، أو مسؤولية قانونية.

المعادلة الأولى (الأساسية):

$$Risk = Threat \times Vulnerability \times Impact$$

| الرمز | المعنى |
|---|---|
| $Risk$ | المخاطرة الكلية |
| $Threat$ | التهديد — وجود جهة قادرة على الهجوم |
| $Vulnerability$ | الثغرة — نقطة ضعف قابلة للاستغلال |
| $Impact$ | الأثر — حجم الضرر لو نجح الهجوم |

ليش الضرب (multiplication) مهم مو الجمع؟ لأن لو أي عامل = صفر، المخاطرة كلها = صفر. يعني لو ماكو تهديد، أو ماكو ثغرة، أو الأثر = صفر ← ماكو مخاطرة أصلًا.

المعادلة الثانية (الموسّعة — تجميع عدة تهديدات):

$$Risk = \sum_{i=1}^{n} P_i \cdot I_i$$

| الرمز | المعنى |
|---|---|
| $Risk$ | المخاطرة المجمّعة (aggregated risk) |
| $P_i$ | احتمال الهجوم $i$ |
| $I_i$ | أثر الهجوم $i$ |
| $n$ | عدد التهديدات المحتملة |
| $\sum$ | مجموع كل التهديدات من $1$ إلى $n$ |

مثال النص يوضّح ليش لازم نوازن: **phishing** ($P_1$) احتمال عالي بس أثر منخفض لكل حدث، بينما **zero-day** ($P_2$) احتمال منخفض بس أثر كارثي. فإدارة المخاطر لازم توازن بين البعدين، مو بس تشوف الاحتمال.

⚠️ **ملاحظة أمينة (مهمة للفهم):** هالفصل يعرّف المخاطرة **مرّتين**: مرة بصيغة $Threat \times Vulnerability \times Impact$، ومرة بصيغة $\sum P_i \cdot I_i$ — والمادة تتعامل مع الاثنتين كأنهم **نفس الفكرة**، مو تعريفين متضادين. عمليًا: الـ $P_i$ تشتغل مكان (Threat × Vulnerability) لأنها احتمال صير الهجوم، والـ $I_i$ تشتغل مكان الـ Impact. كذلك انتبه: قائمة "Where:" تحت المعادلة الأولى تذكر **Likelihood** و**Impact** بس (مو Threat/Vulnerability) — هذي صياغة المادة نفسها، فخذها كما هي.

🎯 **تأشيرة الدكتورة:** البوليتين «Reduce likelihood…» و«Reduce impact…» **مشطوبين بالأحمر = مو مطلوبين للامتحان** (مندرجة هنا للفهم بس، مو للحفظ).

---

### القسم 2 — Cybersecurity as an Enterprise-Wide Responsibility

#### ① النص الأصلي

> Traditionally, cybersecurity was relegated to the IT department: firewalls were configured, antivirus was installed, and risk was assumed to be managed. However, as the Equifax, Target, and Colonial Pipeline breaches demonstrated, cybersecurity failures affect the entire enterprise ecosystem.
>
> **Why It Is Not Only IT's Concern:**
>
> 1. **Enterprise Assets Are Diverse**: Customer data, intellectual property, financial systems, and operational technologies (OT) extend beyond IT servers into HR, finance, R&D, and the supply chain.
> 2. **Business Processes Depend on IT**: From payroll to logistics, all processes are IT-dependent, so a ransomware attack on IT halts business operations enterprise-wide.
> 3. **Regulatory Compliance Is Enterprise-Wide**: Laws like GDPR (Europe) or HIPAA (U.S.) place accountability at the organizational level, not just on IT departments.
> 4. **Reputation and Trust Are Corporate Assets**: Cyber incidents tarnish brand reputation, directly impacting sales and shareholder value.
>
> **Governance Integration** — Cybersecurity must therefore be integrated into:
>
> - **Corporate governance frameworks**: Boards must understand and oversee cyber risk.
> - **Enterprise risk management (ERM)**: Cyber risk is now ranked among the top five global business risks (World Economic Forum, 2023).
> - **Cross-departmental policies**: HR enforces insider threat controls, legal ensures compliance, finance budgets for security, and IT implements technical controls.
>
> This shift requires executives, managers, and employees alike to internalize cybersecurity as part of their roles.

#### ② الترجمة

> «تقليديًا، كان الأمن السيبراني محصورًا بقسم تقنية المعلومات (IT): تُضبَط الجدران النارية (firewalls)، ويُثبَّت مضاد الفيروسات، ويُفترض أن المخاطرة مُدارة. لكن، كما أثبتت اختراقات Equifax وTarget وColonial Pipeline، فإن إخفاقات الأمن السيبراني تؤثر على منظومة المؤسسة بأكملها.
>
> **ليش هو مو شأن الـ IT لحاله (Why It Is Not Only IT's Concern):**
>
> 1. **أصول المؤسسة متنوّعة (Enterprise Assets Are Diverse)**: بيانات العملاء، الملكية الفكرية، الأنظمة المالية، والتقنيات التشغيلية (OT) — كلها تمتد أبعد من سيرفرات الـ IT لتصل إلى HR والمالية والبحث والتطوير وسلسلة التوريد.
> 2. **عمليات الأعمال تعتمد على الـ IT (Business Processes Depend on IT)**: من الرواتب إلى اللوجستيات، كل العمليات تعتمد على الـ IT، فهجوم فدية (ransomware) على الـ IT يوقف عمليات المؤسسة بأكملها.
> 3. **الامتثال التنظيمي على مستوى المؤسسة (Regulatory Compliance Is Enterprise-Wide)**: قوانين مثل GDPR (أوروبا) أو HIPAA (أمريكا) تضع المسؤولية على مستوى المؤسسة، مو على قسم الـ IT بس.
> 4. **السمعة والثقة أصول مؤسسية (Reputation and Trust Are Corporate Assets)**: الحوادث السيبرانية تلطّخ سمعة العلامة التجارية، وتؤثر مباشرة على المبيعات وقيمة المساهمين.
>
> **دمج الحوكمة (Governance Integration)** — لذلك يجب دمج الأمن السيبراني داخل:
>
> - **أطر الحوكمة المؤسسية (Corporate governance frameworks)**: على مجالس الإدارة أن تفهم وتشرف على المخاطر السيبرانية.
> - **إدارة مخاطر المؤسسة (Enterprise risk management — ERM)**: المخاطر السيبرانية اليوم مصنّفة ضمن أعلى خمس مخاطر أعمال عالمية (المنتدى الاقتصادي العالمي، 2023).
> - **السياسات المشتركة بين الأقسام (Cross-departmental policies)**: الـ HR يفرض ضوابط التهديد الداخلي، والقانوني يضمن الامتثال، والمالية تخصّص ميزانية الأمن، والـ IT ينفّذ الضوابط التقنية.
>
> هذا التحوّل يتطلّب من المدراء التنفيذيين والمدراء والموظفين على حدّ سواء أن يستوعبوا الأمن السيبراني كجزء من أدوارهم.»

#### ③ الشرح الفهمي

البداية: زمان كانوا يعتبرون الأمن السيبراني شغلة قسم الـ IT وبس — يضبطون firewall، يثبتون antivirus، ويقولون "خلصنا". لكن اختراقات كبيرة مثل **Equifax** و**Target** و**Colonial Pipeline** أثبتت إن الفشل الأمني ما يوقف عند الـ IT، بل يضرب **منظومة المؤسسة كلها**.

الأربع نقاط اللي تفسّر ليش مو شغلة الـ IT لحاله:

| # | النقطة | المعنى البسيط |
|---|---|---|
| 1 | **Enterprise Assets Are Diverse** | الأصول مو بس سيرفرات — بيانات عملاء، IP، أنظمة مالية، OT — موزّعة على HR والمالية وR&D والتوريد |
| 2 | **Business Processes Depend on IT** | كل شي (رواتب، لوجستيات) معلّق على الـ IT ← ransomware واحد يوقف المؤسسة كلها |
| 3 | **Regulatory Compliance Is Enterprise-Wide** | GDPR / HIPAA تحاسب **المؤسسة** مو قسم الـ IT |
| 4 | **Reputation and Trust Are Corporate Assets** | الاختراق يكسر السمعة ← يأثر على المبيعات وقيمة المساهمين |

الخلاصة اللي تربط كل شي: الأمن السيبراني = **enterprise-wide responsibility**، يعني مسؤولية موزّعة على المؤسسة كلها (executives + managers + employees)، مو مسؤولية فريق تقني واحد.

🎯 **تأشيرة الدكتورة:** عنوان «Why It Is Not Only IT's Concern» **مظلّل بالأصفر = مهم للامتحان**. أما بوليتات «Governance Integration» الثلاثة **مشطوبة بالأحمر = مو مطلوبة للامتحان** (مندرجة هنا للفهم بس).

---

### القسم 3 — Balancing Cost of Controls vs. Potential Damage

#### ① النص الأصلي

> One of the key functions of risk management is to rationalize investments in cybersecurity. No organization has unlimited resources, so it must determine:
>
> - Which risks are worth mitigating?
> - Which can be transferred (e.g., cyber insurance)?
> - Which can be accepted?
>
> This requires balancing the cost of security controls against the potential cost of damage.
>
> **Example: The Firewall Dilemma**
>
> - Annual firewall upgrade cost: $250,000.
> - Probability of network intrusion without the upgrade: 10%.
> - Potential impact of an intrusion: $5M.
>
> Expected Loss without the upgrade:
>
> $$EFL = P \cdot I = 0.10 \times 5{,}000{,}000 = 500{,}000$$
>
> Since $500,000 (expected loss) > $250,000 (control cost), the upgrade is justified.
>
> **Over-Control vs. Under-Control:**
>
> - **Over-Control**: Spending excessively on low-impact threats → wasted resources.
> - **Under-Control**: Ignoring high-impact risks → catastrophic failures.
> - **Balanced Approach**: Use quantitative and qualitative methods to align controls with risk appetite.

#### ② الترجمة

> «من أهم وظائف إدارة المخاطر أنها تعقلن (rationalize) الاستثمارات في الأمن السيبراني. ما كو مؤسسة عندها موارد لا محدودة، فلازم تحدّد:
>
> - أي مخاطر تستحق التخفيف؟
> - أي مخاطر يمكن نقلها (transfer) (مثل التأمين السيبراني)؟
> - أي مخاطر يمكن قبولها (accept)؟
>
> وهذا يتطلّب موازنة كلفة ضوابط الأمن مقابل الكلفة المحتملة للضرر.
>
> **مثال: معضلة الجدار الناري (The Firewall Dilemma)**
>
> - كلفة ترقية الجدار الناري السنوية: $250,000.
> - احتمال اختراق الشبكة بدون الترقية: 10%.
> - الأثر المحتمل للاختراق: $5M.
>
> الخسارة المتوقعة بدون الترقية:
>
> $$EFL = P \cdot I = 0.10 \times 5{,}000{,}000 = 500{,}000$$
>
> وبما أن $500,000 (الخسارة المتوقعة) > $250,000 (كلفة الضابط)، فالترقية مبرَّرة.
>
> **الإفراط مقابل التقصير في الضبط (Over-Control vs. Under-Control):**
>
> - **الإفراط في الضبط (Over-Control)**: صرف مبالغ مفرطة على تهديدات منخفضة الأثر ← موارد مهدرة.
> - **التقصير في الضبط (Under-Control)**: تجاهل المخاطر عالية الأثر ← إخفاقات كارثية.
> - **النهج المتوازن (Balanced Approach)**: استخدام أساليب كمّية ونوعية لمواءمة الضوابط مع شهية المخاطرة (risk appetite).»

#### ③ الشرح الفهمي

الفكرة: إدارة المخاطر ما هدفها "نشتري كل شي أمني"، هدفها **نعقلن الصرف** — لأن الموارد محدودة. فلازم نجاوب على ثلاث أسئلة: شنو نخفّف؟ شنو ننقل (تأمين)؟ وشنو نقبل؟ والجواب يجي من موازنة **كلفة الضابط** مقابل **الكلفة المحتملة للضرر**.

مثال معضلة الجدار الناري:

| العنصر | القيمة |
|---|---|
| كلفة ترقية الـ firewall سنويًا | $250,000 |
| احتمال الاختراق بدون ترقية ($P$) | 10% (0.10) |
| الأثر المحتمل للاختراق ($I$) | $5M |

نحسب الخسارة المتوقعة:

$$EFL = P \cdot I = 0.10 \times 5{,}000{,}000 = 500{,}000$$

| الرمز | المعنى |
|---|---|
| $EFL$ | الخسارة المالية المتوقعة (Expected Financial Loss) |
| $P$ | احتمال وقوع الحدث |
| $I$ | الأثر المالي للحدث |

القاعدة الحاسمة: **لو $EFL > كلفة الضابط ← الضابط مبرَّر**. هنا $500,000 > $250,000، يعني الترقية تستاهل.

بعدها النص يقارن حالتين متطرفتين:

| الحالة | المشكلة | النتيجة |
|---|---|---|
| **Over-Control** | صرف مفرط على تهديدات منخفضة الأثر | موارد مهدرة |
| **Under-Control** | تجاهل المخاطر عالية الأثر | إخفاقات كارثية |
| **Balanced Approach** | موازنة الضوابط مع risk appetite بأساليب كمّية ونوعية | الوضع الصحيح |

يعني الحل مو "أضبط أكثر" ولا "أضبط أقل"، بل **الضبط المناسب حسب المخاطرة**.

🎯 **تأشيرة الدكتورة:** ⚠️ **هذا القسم كامل مشطوب بالأحمر = مو مطلوب للامتحان** (مندرجة هنا للفهم والشمولية بس، مو للحفظ).
