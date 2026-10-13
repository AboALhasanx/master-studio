---
title: ASE الفصل الرابع — المصادر الخارجية والمحتوى الأعمق — Software Project Planning
course: Advanced Software Engineering
subtitle: بنوك الأسئلة الخارجية + جسر Pressman للـRisk + مراجع التقدير المتقدمة
---

# 03 — المصادر الخارجية والمحتوى الأعمق (Ch04)

> **شنو هذا الملف؟** ① نتيجة فحص البنوك الخارجية وأوراق الامتحانات ② **جسر ربط** بين Aggarwal وPressman بقسم الـRisk ③ مراجع التقدير المتقدمة عدنا.
> **قرار الطالب 2026-10-12:** «Aggarwal + ربط Pressman» — يعني الأساس مصدرنا، والـRisk نربطه بأسلوب Pressman (لأن أوراق MRCET تستعمله).

---

## 1. نتيجة فحص المصادر الخارجية (مهمة)

### 1.1 بنوك الأسئلة (`02_Raw_Materials/Question_Banks/`)

| البنك | عدد الأسئلة | محتوى يخصّ Ch04؟ |
|---|---|---|
| `SEPM_QuestionBank_ModuleWise.pdf` | 3 صفحات | ❌ **لاكو شي** عن COCOMO/FP/Putnam |
| `SE_QuestionBank_GitHub.pdf` | 6 صفحات | ⚠️ أسئلة risk عامة (16 ذكر) — بلا حساب |
| `SE_QuestionBank_UnitWise_NRCMEC.pdf` | 3 صفحات | ⚠️ أسئلة risk عامة (10 ذكر) — بلا حساب |

**الاستنتاج:** البنوك الخارجية **ما تخدمنا** بهالفصل. لا COCOMO ولا FP ولا Putnam. الملاحظة المهمة: **ينقصها المحتوى الحسابي** اللي هو جوهر Ch04.

### 1.2 أوراق الامتحانات (`MRCET_SE_EndTerm_Paper_2022Dec.pdf` — 19 ورقة)

فحصت الـ19 ورقة: **النظام مالها مختلف**. هي مبنية على **Pressman** (RMMM، reactive vs proactive risk strategies، metrics)، مو على Aggarwal. الأمثلة:
- "Briefly explain about different categories of risks in risk management"
- "Differentiate between reactive vs proactive risk strategies"
- "Propose RMMM plan for 'staff inexperienced' risk"

**الاستنتاج:** هاي الأوراق **مو مرآة لامتحان الدكتور** (لأن الدكتور = Aggarwal). بس تنفعنا **كمصدر إثراء** لقسم الـRisk، لأن Aggarwal نفسه يستعير من Wiegers/Jones، والـRMMM مفهوم مكمّل.

---

## 2. جسر الربط: Risk بين Aggarwal وPressman

> هذا القسم يوضّح **كيف تربط** المصطلحين حتى لو جاءك سؤال بأي أسلوب.

### 2.1 المفاهيم المتقابلة

| Aggarwal (مصدرنا، §4.7 / سلايد 180–193) | Pressman (الأوراق الخارجية) | جسر الربط |
|---|---|---|
| Risk = مشكلة **لم تحدث بعد** قد تسبب خسارة | "Risk = a potential problem" | **تعريف متطابق تقريباً** |
| **Risk Assessment**: Identification ← Analysis ← Prioritization | Risk **identification**, risk **projection**, risk **refinement** | نفس الفكرة: تعرّف، حلّل، رتّب |
| **Risk Control**: Planning ← Monitoring ← Resolution | **RMMM** (Mitigation, Monitoring, Management) | RMMM ≈ Control لكن مفصّل أكثر |
| **Risk Exposure** = probability × loss | Risk exposure = expected loss | **متطابق** — نفس الصيغة |
| تصنيفات Jones الخمسة (Dependencies, Requirements, Management, Knowledge, Other) | Risk categories (project/technical/business) | تصنيفات مختلفة — **لا تخلطهن** |
| "risk avoidance" (لا تسوي الخطر) | Reactive vs **proactive** strategies | Avoidance = proactive |

### 2.2 Reactive vs Proactive (Pressman) — مكمّل مفيد

| | Reactive | Proactive |
|---|---|---|
| **الفلسفة** | انتظر الخطر، عالجه بعد ما يحدث | توقّع الخطر، خطّط قبل |
| **الأداة** | fire-fighting | **RMMM plan** + risk monitoring |
| **العلاقة بـAggarwal** | — | ≈ Risk Control (planning + monitoring) |

**[Foundational Knowledge / Standard Concept]** — Pressman, *Software Engineering: A Practitioner's Approach* (الفصل 28: Risk Management). هذا نمط الكتب المعياري، مو بالضرورة بالتحديد بالكتاب عدنا.

### 2.3 كيف تجمع الاثنين بالامتحان؟
لو جاء سؤال "risk management activities" — الجواب الأساسي = **Aggarwal: فئتان (Assessment + Control) وفيهن 6 أنشطة** (Fig 9):

| الفئة | الأنشطة (بالترتيب) |
|---|---|
| **Risk Assessment** | Risk Identification · Risk Analysis · Risk Prioritization |
| **Risk Control** | Risk Management Planning · Risk Monitoring · Risk Resolution |

وبعدها **تضيف** (للتفوق): "وبصياغة Pressman، هذا يقابل RMMM plan حيث Mitigation↔planning، Monitoring↔monitoring، Management↔resolution".

---

## 3. منهجيات التقدير المتقدمة (المحتوى الأعمق)

> سلايد 33–34 يذكر تصنيف الموديلات لكنه ما يشرحها. هاي الإضافة.

### 3.1 عائلات موديلات التقدير (سلايد 34)

| العائلة | التعريف | أمثلة |
|---|---|---|
| **Static, Single-Variable** | علاقة واحدة: Effort = f(size) | Walston-Felix · SEL |
| **Static, Multivariable** | علاقات متعددة: Effort = f(size, drivers) | COCOMO intermediate / detailed |

**الفرق:** Single-variable تعتمد على الحجم فقط؛ Multivariable تضيف cost drivers (reliability, experience…).

### 3.2 تقنيات التقدير (من مرجع Putnam — `2_Putnam_Empirical_Estimation_IGULMS.pdf`)

| التقنية | الأساس | الاستخدام |
|---|---|---|
| **Expert Judgement** | خبرة المختصين | بدري، سريع، لكن ذاتي |
| **Delphi Technique** | إجماع خبراء بالتكرار (بلا مواجهة) | يقلل التحيز الفردي |
| **Putnam / Rayleigh** | نموذج رياضي للـmanpower | مشاريع كبيرة |
| **COCOMO** | معادلات + drivers | الأشهر صناعياً |

**Delphi بالتفصيل [المصدر: مرجع Putnam]:**
1. كل خبير يعطي تقدير مستقل (بلا رؤية تقديرات غيره)
2. تُجمع النتائج وتُوزَّع إحصائياً
3. يُعاد التقدير بعد مشاورة
4. يتكرر حتى يتحقق الإجماع

**السؤال المتوقع:** "Describe any two estimation techniques" ⇒ اذكر Expert Judgement + Delphi (من المرجع)، أو LOC + FP (من الفصل). **الاثنين صحيحان بسياق مختلف.**

### 3.3 COCOMO II — التعمق (من `1_COCOMO_II_Manual_Otago.pdf`)

| المرجع | Base | Exponent | ملاحظة |
|---|---|---|---|
| COCOMO 81 | a_b | b_b ثابت لكل mode | أشكال مبسّطة |
| **COCOMO II** | A = 2.94 (post-arch) أو 2.5 | **B = 0.91 + 0.01·ΣSF** | الأس **متغيّر** حسب المشروع! |

**الفكرة الجوهرية (اللي السلايد يذكرها لكن ما يشرحها):** في COCOMO II، **`B` مو ثابت** — يتغيّر حسب 5 scale factors. مشروع "مألوف ومنظّم" ⇒ B قريب من 0.91 (economies of scale، الجهد ينمو ببطء). مشروع "جديد ومبعثر" ⇒ B قريب من 1.23 (diseconomies، الجهد ينمو بسرعة).

**[المصدر: USC COCOMO II Model Definition Manual v2.1]**

### 3.4 Rayleigh Curve — التعمق (من `3_Rayleigh_Curves_Tutorial_ICEAA.pdf`)

النموذج أصله من **مشاريع hardware** (Norden, IBM) — لاحظه Putnam كتقريب جيد للـsoftware. **المنحنى احتمالي (Rayleigh distribution)** ⇒ يفسّر ليش الشكل جرسي:
- يبدأ بطيئاً (قليل من يفهم المشروع بعد)
- يذرو عند td (أقصى توظيف)
- ينزل (المنتج يستقر)

**القيود (مهمة):**
- يفترض **منحنى مثالي** — الواقع فيه اضطرابات
- حساس جداً لـtd (خطأ صغير بـtd ⇒ خطأ كبير بالجهد، لأن D=K/td²)
- لا يصمد للمشاريع الصغيرة (المنحنى يحتاج مشروع كبير ليظهر)

### 3.5 Basili — Models & Metrics (`4_Basili_Models_Metrics_P15.pdf`)
⚠️ **ملف سكان (صورة فقط، 12 صفحة)** — لا نص قابل للاستخراج. يُقرأ بالعين فقط. يخصّ تجربة software engineering والمقاييس التجريبية. **مرجع هامشي للفصل.**

---

## 4. أسئلة إضافية بأسلوب Pressman (للإثراء)

| # | السؤال | الجواب (مختصر) |
|---|---|---|
| P1 | Differentiate reactive vs proactive risk strategies | جدول 2.2 أعلاه |
| P2 | Propose RMMM plan for "staff inexperienced" risk | Mitigation: تدريب · Monitoring: تتبع الأخطاء · Management: خطة بديلة |
| P3 | How far is risk refinement useful? | يحوّل المخاطر العامة لأسئلة قابلة للقياس (حتى تقدير الاحتمال/الأثر) |
| P4 | Explain risk projection (risk estimation) | تحديد probability + impact لكل خطر ⇒ risk exposure |
| P5 | What are the various categories of risks? | **[احذر]** بـPressman: project/technical/business. بـAggarwal: Jones الخمسة. **وضّح أيّ نظام تتبع.** |

---

## ✅ قائمة التحقق
- [ ] أعرف إن البنوك الخارجية ما فيهن حساب Ch04
- [ ] أربط فئتي Aggarwal (Assessment/Control) بـRMMM مال Pressman
- [ ] أذكر 6 أنشطة risk (Assessment 3 + Control 3)
- [ ] أعرف الفرق: تصنيفات Jones (5) ≠ فئات الأنشطة (2)
- [ ] أشرح ليش B متغيّر بـCOCOMO II
- [ ] أذكر قيود Putnam


---

## Retrieval set (active recall)

| السؤال | الجواب |
|---|---|
| شنو موجود بالبنوك الخارجية عن Ch04؟ | لا شي حسابي — risk عام فقط |
| أوراق MRCET تتبع أي نظام؟ | **Pressman** (RMMM) مو Aggarwal |
| أنشطة Aggarwal (فئتان) = ؟ | Assessment + Control |
| تقابل شنو عند Pressman؟ | RMMM (Mitigation+Monitoring+Management) |
| ليش B متغيّر بـCOCOMO II؟ | من 5 scale factors |
| قيود Putnam؟ | منحنى مثالي · لا يصمد للصغيرة · حسّاس لـtd |

---
*المصدر: تحليل أوراق MRCET + بنوك الأسئلة + 4 مراجع Planning — بُني 2026-10-12*