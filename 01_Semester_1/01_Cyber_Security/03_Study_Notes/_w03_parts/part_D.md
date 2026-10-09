### القسم 1 — Industry-Specific Cyber Risks

#### ① النص الأصلي

> Cyber risk manifests differently across industries, and understanding these differences helps illustrate the enterprise-wide importance of risk management.
>
> **4.1 Banking and Financial Services**
>
> Banks are prime targets due to the direct monetary value of their assets. Risks include:
>
> - **Fraud and Theft**: Cybercriminals exploit online banking systems to siphon funds.
> - **Payment System Attacks**: SWIFT network compromises.
> - **Data Breaches**: Exposure of customer financial data leads to identity theft.
>
> *Impact:* Loss of trust in financial institutions can destabilize entire economies.
>
> **4.2 Healthcare**
>
> Hospitals and healthcare providers hold sensitive medical data, which is highly valuable on the dark web. Risks include:
>
> - **HIPAA Violations**: Breaches result in multimillion-dollar fines.
> - **Ransomware Attacks**: Lock patient records and delay treatment (WannaCry crippled the UK NHS in 2017).
> - **IoT Device Exploits**: Pacemakers, insulin pumps, and MRI machines are attack vectors.
>
> *Impact:* Lives can be endangered directly, in addition to financial and legal costs.
>
> **4.3 Critical Infrastructure**
>
> Utilities, energy, and transportation systems are high-value targets for nation-state actors. Risks include:
>
> - **Industrial Control System (ICS) Attacks**: Stuxnet (2010) sabotaged Iranian nuclear centrifuges.
> - **Energy Grid Attacks**: Ukraine's power grid attack (2015) left 230,000 citizens without electricity.
> - **Transportation**: GPS spoofing and air traffic system disruptions.
>
> *Impact:* Beyond finances, these attacks affect national security and public safety.

#### ② الترجمة

> «المخاطر السيبرانية تظهر بشكل مختلف من صناعة لصناعة، وفهم هذي الاختلافات يساعد على توضيح أهمية إدارة المخاطر على مستوى المؤسسة كلها.
>
> **4.1 المصارف والخدمات المالية**
>
> المصارف أهداف رئيسية بسبب القيمة النقدية المباشرة لأصولها. والمخاطر تشمل:
>
> - **الاحتيال والسرقة (Fraud and Theft)**: المجرمون السيبرانيون يستغلون أنظمة الخدمات المصرفية الإلكترونية لسحب الأموال.
> - **هجمات أنظمة الدفع (Payment System Attacks)**: اختراقات شبكة SWIFT.
> - **اختراقات البيانات (Data Breaches)**: كشف بيانات العملاء المالية يؤدي إلى سرقة الهوية.
>
> *الأثر:* فقدان الثقة بالمؤسسات المالية ممكن يزعزع اقتصادات كاملة.
>
> **4.2 الرعاية الصحية**
>
> المستشفيات ومقدّمو الرعاية الصحية يمتلكون بيانات طبية حساسة، وهي عالية القيمة في الويب المظلم (dark web). والمخاطر تشمل:
>
> - **انتهاكات HIPAA**: الاختراقات تؤدي إلى غرامات بملايين الدولارات.
> - **هجمات الفدية (Ransomware Attacks)**: تقفل سجلات المرضى وتؤخر العلاج (WannaCry شلّت الـ NHS البريطانية سنة 2017).
> - **استغلال أجهزة IoT**: منظّمات ضربات القلب ومضخات الأنسولين وأجهزة الرنين المغناطيسي (MRI) هي نواقل هجوم.
>
> *الأثر:* حياة الناس ممكن تكون في خطر مباشرة، بالإضافة إلى التكاليف المالية والقانونية.
>
> **4.3 البنية التحتية الحيوية**
>
> المرافق والطاقة وأنظمة النقل هي أهداف عالية القيمة لفاعلين من الدول (nation-state actors). والمخاطر تشمل:
>
> - **هجمات أنظمة التحكم الصناعي (ICS Attacks)**: Stuxnet (2010) خرّب أجهزة الطرد المركزي النووية الإيرانية.
> - **هجمات شبكة الطاقة (Energy Grid Attacks)**: هجوم شبكة كهرباء أوكرانيا (2015) خلّى 230,000 مواطن بدون كهرباء.
> - **النقل (Transportation)**: التزييف بالـ GPS (GPS spoofing) وتعطيل أنظمة الملاحة الجوية.
>
> *الأثر:* ما يتوقف على المال فقط — هذي الهجمات تأثر على الأمن القومي والسلامة العامة.»

#### ③ الشرح الفهمي

الفكرة الأساسية: المخاطر السيبرانية مو نفس الشي بكل صناعة — كل قطاع عنده حاجاته ومخاطره، وفهم هذي الفروقات يبيّن ليش إدارة المخاطر مهمة على مستوى المؤسسة كلها مو بس قسم واحد.

| القطاع | ليش هدف؟ | أهم المخاطر | الأثر |
|---|---|---|---|
| **Banking & Financial** | قيمة نقدية مباشرة بالأصول | Fraud & Theft، هجمات SWIFT، Data Breaches | فقدان الثقة ← زعزعة الاقتصاد كله |
| **Healthcare** | بيانات طبية حساسة غالية بالـ dark web | انتهاكات HIPAA، Ransomware، استغلال أجهزة IoT | خطر مباشر على حياة المريض + تكاليف |
| **Critical Infrastructure** | أهداف عالية القيمة لفاعلين دوليين | هجمات ICS (Stuxnet)، شبكة الطاقة، النقل | تمس الأمن القومي والسلامة العامة |

نقطة مهمة: كل قطاع من هذي الثلاثة الأثر عنده يتعدّى المال — بالمصارف يوصل للاقتصاد كله، بالصحة يوصل لحياة المريض، وبالبنية التحتية يوصل للأمن القومي. وهاي بالضبط تثبت إن إدارة المخاطر شأن مؤسسي.

أمثلة تحفظها للامتحان: **WannaCry (2017)** ← الـ NHS البريطانية، **Stuxnet (2010)** ← أجهزة الطرد المركزي الإيرانية، **هجوم شبكة كهرباء أوكرانيا (2015)** ← 230,000 مواطن بلا كهرباء.

🎯 **تأشيرة الدكتورة:** عناوين «4. Industry-Specific Cyber Risks» و«4.1 Banking and Financial Services» مظلّلة بالأصفر (yellow) = مهمة للامتحان.

---

### القسم 2 — Example — Scenario: Quantifying Cyber Risk for a Hospital

#### ① النص الأصلي

> **Setting.** Al-Rahma General Hospital wants a numeric view of cyber risk to guide a limited mitigation budget.
>
> **Framing.** Use the basic model $Risk = Likelihood \times Impact$ and the aggregate model $Aggregate\ Risk = \sum_{i=1}^{n} P_i \cdot I_i$.
>
> **1) Baseline risk register (annualized expected loss)**
>
> - **Ransomware**: $P=0.20$, $I=\$10\text{M}$ → $EAL = 0.20 \times 10 = \$2.00\text{M}$.
> - **Insider data theft**: $P=0.10$, $I=\$5\text{M}$ → $EAL = 0.10 \times 5 = \$0.50\text{M}$.
> - **Power outage**: $P=0.05$, $I=\$2\text{M}$ → $EAL = 0.05 \times 2 = \$0.10\text{M}$.
>
> Total baseline aggregate risk $= \$2.6\text{M}$ per year.
>
> **2) Control options (with costs and modeled effect)**
>
> - **C1 — Ransomware hardening package** (segmentation + immutable backups + EDR): Cost $\$0.90\text{M}$; adjust to $P=0.08$, $I=\$6\text{M}$ → residual $EAL = 0.08 \times 6 = \$0.48\text{M}$. Benefit vs baseline $= \$2.00\text{M} - \$0.48\text{M} = \$1.52\text{M}$ (ROI $\approx 1.69$).
> - **C2 — Insider/DLP + IAM tightening** (DLP, PAM, JIT access, stronger joiner–mover–leaver): Cost $\$0.40\text{M}$; adjust to $P=0.05$, $I=\$3\text{M}$ → residual $EAL = 0.05 \times 3 = \$0.15\text{M}$. Benefit $= \$0.50\text{M} - \$0.15\text{M} = \$0.35\text{M}$ (ROI $\approx 0.88$).
> - **C3 — Power resilience** (UPS refresh + genset testing + failover runbooks): Cost $\$0.30\text{M}$; adjust to $P=0.02$, $I=\$1.5\text{M}$ → residual $EAL = 0.02 \times 1.5 = \$0.03\text{M}$. Benefit $= \$0.10\text{M} - \$0.03\text{M} = \$0.07\text{M}$ (ROI $\approx 0.23$).
> - **C4 — Human-layer boost** (targeted phishing drills + admin opsec coaching): Cost $\$0.20\text{M}$; assumed to further trim ransomware likelihood from $0.08$ to $0.07$ after C1. Incremental benefit $= (0.08 - 0.07) \times \$6\text{M} = \$0.06\text{M}$ (ROI $\approx 0.30$).
>
> **3) Budgeted decision ($\$1.5\text{M}$ cap) — two viable portfolios:**
>
> - **Portfolio A (risk-minimizing under budget): C1 + C2 + C4.** Cost $= \$0.90\text{M} + \$0.40\text{M} + \$0.20\text{M} = \$1.50\text{M}$. Residual EALs: ransomware $\$0.42\text{M}$ (with C1+C4), insider $\$0.15\text{M}$, power $\$0.10\text{M}$. Aggregate residual $= \$0.42\text{M} + \$0.15\text{M} + \$0.10\text{M} = \$0.67\text{M}$. Annual risk reduction $= \$2.60\text{M} - \$0.67\text{M} = \$1.93\text{M}$. ROI $= 1.93 / 1.50 \approx 1.29$; payback $\approx 0.78$ years (~9.3 months).
> - **Portfolio B (higher ROI but higher residual risk): C1 + C3.** Cost $= \$0.90\text{M} + \$0.30\text{M} = \$1.20\text{M}$. Residual EALs: ransomware $\$0.48\text{M}$, insider $\$0.50\text{M}$, power $\$0.03\text{M}$. Aggregate residual $= \$1.01\text{M}$; reduction $= \$1.59\text{M}$. ROI $= 1.59 / 1.20 \approx 1.33$; payback $\approx 0.76$ years.
>
> **Recommendation.** For a hospital, Portfolio A better aligns with patient-safety and regulatory exposure: it minimizes total residual risk ($\$0.67\text{M}$) while staying on budget, even if Portfolio B's ROI is marginally higher. Prioritize ransomware first, then insider risk; address power as a next wave when budget allows.
>
> **4) Takeaways for managers**
>
> - The simple $\sum P_i I_i$ framing turns vague threats into budget-ranked actions.
> - Controls act by lowering $P$, $I$, or both; quantify each to compare apples to apples.
> - Re-run this calculator quarterly with fresh incident intel and control efficacy to keep priorities current.

#### ② الترجمة

> «**الإطار (Setting).** مستشفى الرحمة العام يريد رؤية رقمية للمخاطر السيبرانية حتى يوجّه ميزانية تخفيف محدودة.
>
> **التأطير (Framing).** نستخدم النموذج الأساسي $Risk = Likelihood \times Impact$ والنموذج التجميعي $Aggregate\ Risk = \sum_{i=1}^{n} P_i \cdot I_i$.
>
> **1) سجل المخاطر الأساسي (الخسارة المتوقعة السنوية)**
>
> - **Ransomware (الفدية)**: $P=0.20$، $I=\$10\text{M}$ ← $EAL = 0.20 \times 10 = \$2.00\text{M}$.
> - **سرقة بيانات داخلية (Insider data theft)**: $P=0.10$، $I=\$5\text{M}$ ← $EAL = 0.10 \times 5 = \$0.50\text{M}$.
> - **انقطاع الكهرباء (Power outage)**: $P=0.05$، $I=\$2\text{M}$ ← $EAL = 0.05 \times 2 = \$0.10\text{M}$.
>
> إجمالي المخاطر الأساسية التجميعية $= \$2.6\text{M}$ سنويًا.
>
> **2) خيارات الضبط (مع التكاليف والأثر المُنمذَج)**
>
> - **C1 — حزمة تحصين ضد الفدية** (تقسيم الشبكة + نسخ احتياطية غير قابلة للتغيير + EDR): التكلفة $\$0.90\text{M}$؛ نعدّل إلى $P=0.08$، $I=\$6\text{M}$ ← $EAL = 0.08 \times 6 = \$0.48\text{M}$. الفائدة مقابل الأساس $= \$2.00\text{M} - \$0.48\text{M} = \$1.52\text{M}$ (ROI $\approx 1.69$).
> - **C2 — تشديد Insider/DLP + IAM** (DLP، PAM، وصول JIT، تقوية joiner–mover–leaver): التكلفة $\$0.40\text{M}$؛ نعدّل إلى $P=0.05$، $I=\$3\text{M}$ ← $EAL = 0.05 \times 3 = \$0.15\text{M}$. الفائدة $= \$0.50\text{M} - \$0.15\text{M} = \$0.35\text{M}$ (ROI $\approx 0.88$).
> - **C3 — مرونة الطاقة** (تجديد UPS + فحص المولّد + runbooks للتحويل الاحتياطي): التكلفة $\$0.30\text{M}$؛ نعدّل إلى $P=0.02$، $I=\$1.5\text{M}$ ← $EAL = 0.02 \times 1.5 = \$0.03\text{M}$. الفائدة $= \$0.10\text{M} - \$0.03\text{M} = \$0.07\text{M}$ (ROI $\approx 0.23$).
> - **C4 — تعزيز الطبقة البشرية** (تدريبات تصيّد مستهدفة + توعية opsec للمدراء): التكلفة $\$0.20\text{M}$؛ يُفترض أنه يقلّل احتمال الفدية من $0.08$ إلى $0.07$ بعد C1. الفائدة الإضافية $= (0.08 - 0.07) \times \$6\text{M} = \$0.06\text{M}$ (ROI $\approx 0.30$).
>
> **3) القرار ضمن الميزانية (سقف $\$1.5\text{M}$) — محفظتان قابلتان للتنفيذ:**
>
> - **المحفظة A (الأقل مخاطرة ضمن الميزانية): C1 + C2 + C4.** التكلفة $= \$0.90\text{M} + \$0.40\text{M} + \$0.20\text{M} = \$1.50\text{M}$. الـ EAL المتبقية: الفدية $\$0.42\text{M}$ (مع C1+C4)، الداخلي $\$0.15\text{M}$، الكهرباء $\$0.10\text{M}$. المخاطر التجميعية المتبقية $= \$0.67\text{M}$. تخفيض المخاطر السنوي $= \$2.60\text{M} - \$0.67\text{M} = \$1.93\text{M}$. ROI $= 1.93 / 1.50 \approx 1.29$؛ فترة الاسترداد $\approx 0.78$ سنة (~9.3 شهر).
> - **المحفظة B (ROI أعلى لكن مخاطرة متبقية أعلى): C1 + C3.** التكلفة $= \$0.90\text{M} + \$0.30\text{M} = \$1.20\text{M}$. الـ EAL المتبقية: الفدية $\$0.48\text{M}$، الداخلي $\$0.50\text{M}$، الكهرباء $\$0.03\text{M}$. المخاطر التجميعية المتبقية $= \$1.01\text{M}$؛ التخفيض $= \$1.59\text{M}$. ROI $= 1.59 / 1.20 \approx 1.33$؛ فترة الاسترداد $\approx 0.76$ سنة.
>
> **التوصية (Recommendation).** بالنسبة لمستشفى، المحفظة A تتوافق أكثر مع سلامة المريض والتعرض التنظيمي: فهي تقلّل إجمالي المخاطر المتبقية ($\$0.67\text{M}$) وتبقى ضمن الميزانية، حتى لو كان ROI للمحفظة B أعلى بشكل طفيف. رتّب الفدية أولًا، ثم المخاطر الداخلية؛ وعالج الكهرباء كموجة تالية لما تسمح الميزانية.
>
> **4) خلاصات للمدراء (Takeaways for managers)**
>
> - صيغة $\sum P_i I_i$ البسيطة تحوّل التهديدات المبهمة إلى إجراءات مرتّبة بالميزانية.
> - الضوابط تشتغل بتخفيض $P$ أو $I$ أو الاثنين؛ قِس كل واحد حتى تقارن تفاحة بتفاحة.
> - أعد تشغيل هذي الحاسبة كل ثلاثة أشهر مع معلومات حوادث جديدة وفعالية الضوابط حتى تبقى الأولويات محدّثة.»

#### ③ الشرح الفهمي

القصة بسيطة: مستشفى (الرحمة) عنده ميزانية تخفيف محدودة ويريد يعرف وين يصرفها. بدل ما يقول "التهديدات خطيرة" بشكل عام، يحوّلها لأرقام.

المعادلتان اللي يعتمد عليهم:

$$Risk = Likelihood \times Impact \qquad Aggregate\ Risk = \sum_{i=1}^{n} P_i \cdot I_i$$

يعني الخطر الفردي هو الاحتمالية مضروبة بالأثر، والخطر الكلي هو مجموع كل الاحتمالات مضروبة بآثارها (رمز الجمع $\sum$).

| الرمز | المعنى |
|---|---|
| $P_i$ | احتمال حدوث التهديد رقم $i$ (Likelihood) |
| $I_i$ | الأثر المالي للتهديد رقم $i$ (Impact) |
| $EAL$ | الخسارة السنوية المتوقعة (Expected Annual Loss) $= P \times I$ |
| $ROI$ | العائد على الاستثمار $=$ الفائدة $\div$ التكلفة |

**شنو صار بالضبط (بالفكرة، بدون تعقيد الحسابات):**

1. حسبوا المخاطر الحالية ← طلع الإجمالي $\$2.6\text{M}$ سنويًا (أكبر بند هو الـ Ransomware بـ $\$2.0\text{M}$).
2. جرّبوا أربع ضوابط C1–C4، وكل ضابط يخفض الـ $P$ أو الـ $I$ أو الاثنين ← يقلّل الخسارة المتوقعة، بس عنده تكلفة.
3. عندهم سقف ميزانية $\$1.5\text{M}$، فكوّنوا محفظتين:
   - **A (C1+C2+C4)** ← تكلفة $\$1.50\text{M}$، مخاطر متبقية $\$0.67\text{M}$، تخفيض $\$1.93\text{M}$.
   - **B (C1+C3)** ← تكلفة $\$1.20\text{M}$، مخاطر متبقية $\$1.01\text{M}$، تخفيض $\$1.59\text{M}$.
4. القرار: **اختاروا A** — لأن المستشفى حساسية عنده عالية (سلامة المريض + امتثال)، فالأولوية تقليل المخاطرة الكلية مو أعلى ROI. الـ B الـ ROI ماله أعلى شوية ($1.33$ مقابل $1.29$) بس مخاطرته المتبقية أعلى.

| | التكلفة | المخاطر المتبقية | التخفيض | ROI |
|---|---|---|---|---|
| **Portfolio A** (C1+C2+C4) | $\$1.50\text{M}$ | $\$0.67\text{M}$ | $\$1.93\text{M}$ | $\approx 1.29$ |
| **Portfolio B** (C1+C3) | $\$1.20\text{M}$ | $\$1.01\text{M}$ | $\$1.59\text{M}$ | $\approx 1.33$ |

الفكرة اللي تريدها الدكتورة: هذا المثال يعلّمك كيف تحوّل تهديدات مبهمة إلى **إجراءات مرتّبة بالميزانية** — الضوابط تخفّض $P$ أو $I$، وقيس كل واحد حتى تقارن صح، وأعد الحساب دوريًا.

🎯 **تأشيرة الدكتورة:** «المثال داخل» — المثال نفسه مطلوب في الامتحان.

---

### القسم 3 — Risk Management in Modern Cybersecurity Strategy

#### ① النص الأصلي

> Risk management today is not static; emerging challenges require dynamic, adaptive approaches:
>
> 1. **Cloud Computing**: Misconfiguration of cloud services (open S3 buckets) is the top cause of cloud breaches.
> 2. **AI-Driven Threats**: Polymorphic malware uses AI to evade detection.
> 3. **Supply Chain Risks**: Attacks on trusted vendors (SolarWinds breach, 2020).
> 4. **Quantum Computing**: A future threat to RSA and ECC encryption.
>
> **Enterprise Response**
>
> - Adoption of Zero Trust Architecture ("Never trust, always verify").
> - Investment in cyber risk quantification models (CRQ).
> - Alignment with global standards: ISO 27001, NIST CSF, and the FAIR model for financial quantification.

#### ② الترجمة

> «إدارة المخاطر اليوم مو ثابتة. التحديات الناشئة تتطلب مناهج ديناميكية ومتكيّفة:
>
> 1. **الحوسبة السحابية (Cloud Computing)**: سوء إعداد الخدمات السحابية (دلاء S3 مفتوحة) هو السبب الأول لاختراقات السحابة.
> 2. **التهديدات المدفوعة بالذكاء الاصطناعي (AI-Driven Threats)**: البرمجيات الخبيثة متعددة الأشكال تستخدم الـ AI لتتفادى الكشف.
> 3. **مخاطر سلسلة التوريد (Supply Chain Risks)**: هجمات على موردين موثوقين (اختراق SolarWinds سنة 2020).
> 4. **الحوسبة الكمومية (Quantum Computing)**: تهديد مستقبلي لتشفير RSA و ECC.
>
> **استجابة المؤسسات (Enterprise Response)**
>
> - تبنّي معمارية الثقة الصفرية (Zero Trust Architecture) — «لا تثق أبدًا، تحقّق دائمًا».
> - الاستثمار في نماذج التحديد الكمّي لمخاطر السيبرانية (CRQ).
> - التوافق مع المعايير العالمية: ISO 27001، NIST CSF، ونموذج FAIR للتحديد الكمّي المالي.»

#### ③ الشرح الفهمي

الفكرة: إدارة المخاطر ما توقف عند حل مشاكل اليوم — التقنية تتغير، فالمخاطر تتغير، فلازم منهج **dynamic** (يتحرك) و**adaptive** (يتكيّف). أربع تحديات ناشئة:

| التحدي | المشكلة | المثال من النص |
|---|---|---|
| **Cloud Computing** | سوء إعداد الخدمات السحابية | دلاء S3 مفتوحة |
| **AI-Driven Threats** | برمجيات خبيثة تتطور وتتفادى الكشف | Polymorphic malware |
| **Supply Chain Risks** | هجوم على مورد موثوق | SolarWinds (2020) |
| **Quantum Computing** | يكسر التشفير الحالي | RSA و ECC |

والرد المؤسسي عليهن ثلاث نقاط:

1. **Zero Trust Architecture** ← «لا تثق أبدًا، تحقّق دائمًا» (Never trust, always verify).
2. **CRQ** ← الاستثمار بنماذج التحديد الكمّي لمخاطر السيبرانية (Cyber Risk Quantification).
3. **المعايير العالمية** ← ISO 27001، NIST CSF، ونموذج FAIR للتحديد الكمّي المالي.

خلاصة تربط كل شي: كل تحدّي من الأربعة يبيّن إن إدارة المخاطر لازم تكون **forward-looking** — تستعد للمستقبل (مثلًا التشفير ما بعد الكمومي) مو بس تتعامل مع الحاضر.
