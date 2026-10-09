---
title: "Week 2 (Risk) — الجابتر الثالث: المخاطر كتهديد مؤسسي"
course: Cyber Security
subtitle: فهمي للملزمة — المخاطر المؤسسية، الخسائر المالية/التشغيلية/السمعية، دورة إدارة المخاطر، والسياسات الأمنية
---

# المخاطر كتهديد مؤسسي — Cybersecurity Risks as Organizational Threats

> كل اقتباس إنكليزي معلَّم بـ `W2b Pn` هو من مادة الدكتورة (ملف W03، صفحة n). والباقي شرح عربي فهمي.
> **قاعدة الملف:** نشرح **بلغة الدكتورة** حتى تجاوب بامتحانها. استخدم **مفرداتها** بالإمتحان.

> **دليل القراءة:** كل قسم موسوم — **شرح + تعريف** / **شرح + تعداد** / **تعداد فقط** / **نقاط + شرح**.

> **⚠️ ملاحظة مهمة:** هذا الملف (W03) **مادة AI مولّدة** (مو من كتاب Sharp). معادلاته (`EFL`, `PCI`) **مُختَرَعة**. بس الدكتورة تستخدمها — فاحفظها **بمفرداتها** للامتحان.

---

## القسم 1 — الأمن مو مشكلة تقنية فقط
> **نوع المحتوى:** شرح + تعداد

> **W2b P1** "For much of its early history, cybersecurity was framed as a technical challenge… However, the last two decades have demonstrated that cybersecurity failures are fundamentally organizational threats."

**المعنى:** زمان كانوا يفكرون الأمن = Firewalls + Antivirus (مشكلة **تقنية**). اليوم واضح إنها **مشكلة مؤسسية** — تسبب خسائر مالية، ضرر سمعة، عقوبات قانونية، وحتى خطر على الأمن الوطني.

**الأربعة «Why» (تُحفظ):**
| # | السبب | شرح |
|:--:|:---|:---|
| 1 | **Pervasive Digitization** | كل العمليات التجارية/الصحية/سلاسل التوريد تعتمد IT |
| 2 | **Ecosystem Dependence** | الاعتماد على **Cloud services + Outsourcing** |
| 3 | **Adversarial Nature** | الخطر **ذكي ومتطور** (مهاجمون، دول، مُبلّغون داخليون) |
| 4 | **Legal/Regulatory Context** | الامتثال (GDPR · HIPAA · PCI-DSS) يربط الفشل بمسؤولية قانونية |

**⚠️ تنبيه (الدكتورة خلطت):** قالت «**IT = Cyber Security**» — **هذا غلط**. الأمن السيبراني **جزء من** IT (مجموعة جزئية)، مو مساوياً لها. إذا سُئلت، قل: **«Cybersecurity is a part of IT, not equal to it»**.

---

## القسم 2 — ليش إدارة المخاطر ضرورة استراتيجية
> **نوع المحتوى:** شرح + تعداد + معادلة

**الأبعاد الثلاثة (تُحفظ):** **Financial · Operational · Reputational**.

### 2.1 المخاطر المالية (Financial Risk)
**مصادر الخسارة:** Incident Response Costs · Business Disruption · Legal Penalties · Ransom Payments · Litigation.

> **W2b P1** "Mathematical framing of Expected Financial Loss (EFL):"

$$EFL = \sum_{i=1}^{n} P_i \cdot I_i$$

| الرمز | المعنى |
|:---|:---|
| $P_i$ | احتمال الحدث السيبراني $i$ |
| $I_i$ | التأثير المالي للحدث $i$ |

**بالعربي:** الخسارة المالية المتوقعة = مجموع (احتمال كل خطر × تأثيره). كل ما قلّلنا $P$ أو $I$، قلّت الخسارة. **وهذا اللي تكرره الدكتورة: «صفّر أو قلّل أحد الطرفين».**

### 2.2 المخاطر التشغيلية (Operational Risk)
> **W2b P1** "Cybersecurity failures often result in operational paralysis."

**المعنى:** فشل الأمن = **شلل تشغيلي**. إدارة المخاطر تضمن استمرارية العمل حتى تحت الهجوم (backups · redundancy · incident response).

### 2.3 مخاطر السمعة (Reputational Risk)
> **W2b P1** "Reputation once lost is hard to restore."

**المعنى:** الثقة = أهم أصل. خرق واحد يدمّر ثقة العملاء (مصارف · صحة · تجارة إلكترونية). **من أكبر المخاطر** على أي مؤسسة.

---

## القسم 3 — جسر بين الضوابط التقنية والحوكمة
> **نوع المحتوى:** شرح + تعداد

**الفرق (سؤال امتحاني — يُحفظ):**
| | **Technical Controls** | **Governance Structures** |
|:---|:---|:---|
| شنو | Firewalls · IDS · Antivirus · Patching | Policies · Compliance · Executive oversight |
| الطبيعة | **IT بحتة** | **IT + سياسة/إدارة** |

**المعنى:** إدارة المخاطر **تترجم** الثغرة التقنية إلى **خطر تجاري** يفهمه المدير التنفيذي ← يوزّع الموارد صح.

---

## القسم 4 — إدارة المخاطر كعملية مستمرة
> **نوع المحتوى:** تعداد فقط (تُحفظ)

**دورة إدارة المخاطر (Risk Management Cycle) — 5 خطوات:**
1. **Identify** — الأصول · الثغرات · التهديدات.
2. **Assess** — الاحتمالية + التأثير.
3. **Prioritize** — ترتيب حسب الخطورة.
4. **Mitigate** — ضوابط تقنية + تنظيمية.
5. **Monitor** — مراجعة مستمرة.

**⚠️ مصيدة (الدكتورة قالتها):** بملزمة المخاطر (Sharp) الأربع خطوات هي **PDCA** (Plan · Do · Check · Act) = **4 مراحل**. لا تخلط بين **PDCA (4)** و**دورة إدارة المخاطر (5)**.

**المعايير المرتبطة:** **ISO/IEC 27005** (إدارة مخاطر أمن المعلومات) · **NIST SP 800-37** (RMF).

---

## القسم 5 — التحديات المستقبلية
> **نوع المحتوى:** تعداد فقط (تُحفظ)

1. **Cloud Security Risks** — سوء إعداد السحابة (S3 buckets مفتوحة).
2. **IoT & OT Risks** — مليارات الأجهزة توسّع سطح الهجوم؛ ICS بلا أمن متين.
3. **AI-Driven Attacks** — برمجيات خبيثة متعددة الأشكال + deepfake phishing.
4. **Quantum Computing** — يكسر RSA/ECC ← لازم post-quantum cryptography.

---

## القسم 6 — أهمية إدارة المخاطر (تكرار المادة)
> **نوع المحتوى:** شرح + معادلات

> **W2b P2** "Risk in cybersecurity is not an abstract concept—it is the quantifiable possibility that a threat actor exploits a vulnerability to damage organizational assets."

**التعريف:** المخاطرة = الاحتمال القابل للقياس إن **مهاجم يستغل ثغرة** ويلحق ضرراً.

$$Risk = Threat \times Vulnerability \times Impact$$

$$Risk = \sum_{i=1}^{n} P_i \cdot I_i \qquad (\text{نفس } EFL)$$

**⚠️ لاحظ:** الملف يعرّف المخاطرة **مرتين** بنفس المعنى (مرة `Threat×Vuln×Impact`، ومرة `Σ P_i·I_i`). هذا **تكرار بالمادة** — للامتحان: اكتب الصيغة اللي تعرفها، واذكر إن الاثنين يعطون نفس المعنى.

**مثال الملف (يُفهم لا يُحفظ):** مستشفى Al-Rahma — يحسب EAL لكل خطر (Ransomware $2M · Insider $0.5M · Power $0.1M = $2.6M) ثم يقارن بورتوفوليو الضوابط وROI. **الفكرة:** `Σ P_i·I_i` يحوّل التهديدات الغامضة إلى **قرارات ميزانية مرتّبة**.

---

## القسم 7 — إنشاء وتطبيق السياسات الأمنية
> **نوع المحتوى:** شرح + تعريف + معادلة

> **W2b P3** "A security policy is a high-level organizational document that sets out rules, expectations, and guidelines for securing information assets."

**خصائص السياسة (تُحفظ — 4):**
- **High-Level Guidance** — «شنو» لازم يصير، مو بالضرورة «شلون».
- **Alignment with Risk** — مشتقّة من تقييم المخاطر.
- **Organization-Wide** — تشمل الكل (موظفين، متعاقدين، أطراف ثالثة).
- **Living Document** — تتطور مع تغيّر التهديدات.

**أمثلة:** Acceptable Use Policy (AUP) · Data Handling Policy · Incident Response Policy.

**سياسة vs تقنية (سؤال):** السياسة = **توجيه**؛ التقنية = **إنفاذ**. الاثنان لازم.
- سياسة بلا تقنية ← موظف يحط «123456».
- تقنية بلا سياسة ← تنبيهات تُتجاهل.

**معادلة فعّالية السياسة:**
$$PE = \frac{Incidents_{before} - Incidents_{after}}{Incidents_{before}}$$

**مثال:** 200 محاولة قبل ← 20 بعد MFA ← $PE = (200-20)/200 = 0.9 = 90\%$.

**دورة حياة السياسة (5 خطوات — تُحفظ):** Draft ← Approval ← Communication ← Enforcement ← Review & Update.

---

## القسم 8 — دور السياسة في أمن المؤسسة (تكرار)
> **نوع المحتوى:** شرح + معادلة

**السياسة = «الغراء الاستراتيجي»** بين IT + الإدارة + الامتثال.
**الوظائف:** تحديد المسؤوليات · مواءمة الأمن بأهداف العمل · الامتثال القانوني · تقليل التهديدات الداخلية.

**الاتجاهات الحديثة:** Zero Trust policies («Never Trust, Always Verify») · AI-driven compliance auditing · ESG.

**معادلة مؤشر الامتثال (PCI):**
$$PCI = \frac{\sum_{k=1}^{n} w_k \cdot c_k}{\sum_{k=1}^{n} w_k}$$

| الرمز | المعنى |
|:---|:---|
| $c_k$ | مستوى الامتثال للمتطلب $k$ (0–1) |
| $w_k$ | وزن/أهمية المتطلب $k$ |

**مثال الملف (بنك):** $c_1=0.9, w_1=5$ · $c_2=0.7, w_2=3$ · $c_3=0.6, w_3=2$ ← $PCI = (4.5+2.1+1.2)/10 = 0.78 = 78\%$ (Yellow).
**⚠️ لاحظ:** `PCI` معرّف **مرتين** بنفس المثال — تكرار بالمادة.

---

## 🎯 مصائد الامتحان (Exam Traps)

| # | المصيدة | الجواب الآمن |
|:--:|:---|:---|
| 1 | «IT = Cyber Security؟» | ❌ الأمن **جزء من** IT |
| 2 | «كم مرحلة PDCA؟» | **4** (Plan/Do/Check/Act) |
| 3 | «كم خطوة دورة إدارة المخاطر؟» | **5** (Identify/Assess/Prioritize/Mitigate/Monitor) |
| 4 | فرق Technical vs Governance | تقني = IT بحتة؛ حوكمة = IT + سياسة |
| 5 | `EFL` و `Risk = Σ P_i·I_i` | **نفس الشي** (المادة تسميهما مختلفين) |

---

## Retrieval set — أسئلة استرجاع

**1. ليش الأمن السيبراني مشكلة مؤسسية مو تقنية فقط؟**
> لأنه يسبب خسائر مالية، ضرر سمعة، عقوبات قانونية، وخطر على الأمن الوطني — مو مجرد مشكلة IT. الأسباب الأربعة: Pervasive Digitization · Ecosystem Dependence · Adversarial Nature · Legal/Regulatory Context.

**2. شنو الأبعاد الثلاثة لضرورة إدارة المخاطر؟**
> **Financial** (خسائر مالية) · **Operational** (شلل تشغيلي) · **Reputational** (ضرر السمعة).

**3. اكتب معادلة الخسارة المالية المتوقعة واشرحها.**
> $EFL = \sum P_i \cdot I_i$ — مجموع (احتمال كل حدث × تأثيره المالي). نقلّلها بتقليل $P$ أو $I$.

**4. شنو الفرق بين Technical Control و Governance Structure؟**
> Technical = ضوابط IT بحتة (Firewalls/IDS/patching). Governance = IT + سياسة/إدارة (Policies/compliance/executive oversight).

**5. عدّد خطوات دورة إدارة المخاطر.**
> Identify → Assess → Prioritize → Mitigate → Monitor.

**6. شنو التحديات المستقبلية الأربعة؟**
> Cloud security · IoT/OT · AI-driven attacks · Quantum computing.

**7. اكتب معادلة الخطر بالصيغتين.**
> $Risk = Threat \times Vulnerability \times Impact$ و $Risk = \sum P_i \cdot I_i$. (نفس المعنى.)

**8. شنو خصائص السياسة الأمنية؟**
> High-Level Guidance · Alignment with Risk · Organization-Wide · Living Document.

**9. اكتب معادلة فعّالية السياسة (PE) واشرحها.**
> $PE = (before − after)/before$ — نسبة تقليل الحوادث بعد تطبيق السياسة. مثال: 200←20 = 90%.

**10. اكتب معادلة مؤشر الامتثال (PCI) واشرحها.**
> $PCI = \sum w_k c_k / \sum w_k$ — متوسط مرجّح لمستوى الامتثال. مثال بنك: 0.78 = 78%.

**11. شنو دورة حياة السياسة؟**
> Draft → Approval → Communication → Enforcement → Review & Update.

**12. شنو يعني Zero Trust؟**
> «Never Trust, Always Verify» — كل طلب يُصادق ويُصرّح له على حدة، حتى داخل الشبكة.

---
*المصدر: `02_Raw_Materials/W03_Risks.pdf`. للنسخة الحقيقية (Sharp): `W02_DeepDive.md` و `W02_Source_Verify.md`.*