---
title: ASE الفصل الرابع — بنك أنماط الامتحان — Software Project Planning
course: Advanced Software Engineering
subtitle: أين يركّز الدكتور + الأنماط المتكررة + خطة المراجعة
---

# 04 — بنك أنماط الامتحان (Ch04 · Software Project Planning)

> **شنو هذا الملف؟** استخلاص **الأنماط المتكررة** اللي يُبنى عليها امتحان الفصل، مع وزن كل نمط.
> **الأساس:** أسلوب الدكتور = أسئلة الكتاب/السلايدات + إعادة صياغة. فكل نمط هنا = "سؤال محتمل جداً".

---

## 1. محاور الامتحان مرتّبة حسب الأهمية

| المحور | الوزن | ليش | نوع السؤال المتوقع |
|---|---|---|---|
| **① حساب التقدير (Estimation Calc)** | ★★★ | 9 أمثلة محلولة + 10 تمارين حسابية | "Compute the effort/FP/LOC for…" |
| **② COCOMO (كل مستوياته)** | ★★★ | 5 تمارين + نظري ثقيل | "Calculate E & D" / "Explain levels" |
| **③ Function Points** | ★★☆ | 3 تمارين + 2 مثال | "Compute FP with CAF" |
| **④ Putnam / Rayleigh** | ★★☆ | 1 مثال + عدة تمارين | "Calculate td, Kd, m₀, D, D₀" |
| **⑤ Risk Management** | ★★☆ | §4.7 + 5 تمارين | "Discuss risks / risk activities" |
| **⑥ Size Estimation (LOC vs FP)** | ★☆☆ | تمارين مفاهيمية | "Compare size measures" |
| **⑦ Empirical models (W-F/SEL)** | ★☆☆ | تمرينان | "Compare W-F with SEL" |

**[القراءة الاستراتيجية]:** هالفصل **60% حساب**. لو حفظت المعادلات والجداول وحلّيت الأمثلة — ضمنت الأغلبية. النصّي (risk + مقارنات) سهل إذا قريت الفصل مرة.

---

## 2. الأنماط المتكررة (قالب كل نمط + جوابه النموذجي)

### النمط 1 — "احسب FP" ★★★
**القالب:** "Consider a project with: Number of user inputs = X, outputs = Y, enquiries = Z, files = W, external interfaces = V. Compute FP."
**الخطوات:**
| الخطوة | التفصيل |
|---|---|
| أولاً | صنّف كل وحدة (low / avg / high) وخذ الوزن من جدول UFP |
| ثانياً | UFP = Σ(count × weight) |
| ثالثاً | CAF = 0.65 + 0.01 × ΣFi |
| رابعاً | FP = UFP × CAF |
**فخ:** التعقيدات المعطاة مختلطة (مثل Exercise 4.3) ⇒ لا تخلط الأوزان. **تدرّب على:** Exercise 4.5, 4.10, 4.11.

### النمط 2 — "احسب E وD بـCOCOMO" ★★★
**القالب:** "A project of X KLOC is to be developed in [mode]. Calculate effort and development time."
**الخطوات:**
| الخطوة | التفصيل |
|---|---|
| أولاً | اختر الموديل (organic / semidetached / embedded) من الحجم + البيئة |
| ثانياً | E = a_b(KLOC)^b_b — خذ a,b من جدول المعاملات |
| ثالثاً | D = c_b(E)^d_b |
| رابعاً | (اختياري) SS = E/D · P = KLOC/E |
**فخ:** جداول **Basic ≠ Intermediate** (a مختلف!). إذا السؤال ذكر cost drivers ⇒ Intermediate (استخدم a_i).
**تدرّب على:** Exercise 4.16, 4.20, 4.21 + Example 4.5.

### النمط 3 — "احسب EAF ثم E" ★★☆
**القالب:** "A project has [drivers ratings]. Use intermediate COCOMO to estimate effort."
**الخطوات:**
| الخطوة | التفصيل |
|---|---|
| أولاً | EAF = حاصل ضرب قيم كل الـ15 driver (1.0 للـnominal) |
| ثانياً | E = a_i(KLOC)^b_i × EAF |
**فخ:** اضرب **كل** الـ15 driver (الـnominal = 1.0، فما تأثر لكن لا تنساها).

### النمط 4 — "احسب COCOMO II" ★★☆
**القالب:** "A project of [category] with X KLOC has scale factors [ratings]. Cost drivers [ratings]. Calculate effort."
**الخطوات:**
| الخطوة | التفصيل |
|---|---|
| أولاً | B = 0.91 + 0.01 × Σ(scale factor ratings) — 5 factors |
| ثانياً | PM_nominal = 2.5 × (size)^B |
| ثالثاً | EM = حاصل ضرب الـ7 (early) أو الـ17 (post-arch) driver |
| رابعاً | PM_adjusted = PM_nominal × EM |
**فخ:** عدد الـscale factors = **5**؛ عدد الـearly drivers = **7**؛ عدد الـpost-arch drivers = **17**. **احفظ الأرقام.**

### النمط 5 — "احسب Putnam" ★★☆
**القالب:** "Assuming the Putnam model with S=…, C=…, Do=…, compute td and Kd." أو "K=… PY, td=… years — calculate peak manning and difficulty."
**الخطوات:**
| المصدر | الصيغ |
|---|---|
| من S و C و D₀ | td = [ (S/C)³ / D₀ ]^(1/7) · K = D₀ × td³ |
| من K و td | m₀ = K/(td·e) · D = K/td² · D₀ = K/td³ · Kd = K/6 · tod = td/√6 |

**فخ:** التمييز بين `K` (الكلي) و`Kd` (development sub-cycle) — اقرأ السؤال بعناية.

### النمط 6 — "قارن الموديلات" ★★☆
**القالب:** "Compare Walston-Felix with SEL" / "Compare the three COCOMO modes" / "Basic vs Intermediate vs Detailed".
**الجواب:** جدول مقارنة + الفرق الجوهري + متى تستخدم كل واحد.

### النمط 7 — "اشرح Risk" ★★☆
**القالب:** "What is risk? Discuss risk management activities." / "What are typical software risks?"
**الجواب:** تعريف + أنشطة (2 فئات / 6 أنشطة) + تصنيفات Jones + risk exposure.

### النمط 8 — "ليش نقدّر بدري؟" ★☆☆
**القالب:** "Why estimate cost/size during planning, before requirements analysis?"
**الجواب:** لأن التخطيط/العقود/الجدولة/توزيع الموارد كلها تحتاج تقدير مبدئي. *(Exercise 4.31)*

---

## 3. الأسئلة اللي **متوقع جداً** يجيبها الدكتور (تنبؤ)

| # | السؤال | نوعه | مصدره |
|---|---|---|---|
| E1 | Compute the function point for a project with [domain characteristics] | حساب | Exercise 4.5/4.10 |
| E2 | Suppose a project was estimated to be X KLOC — calculate effort & time (3 modes) | حساب | Exercise 4.21 |
| E3 | Explain all levels of COCOMO + calculate for [KLOC] | نظري+حساب | Exercise 4.16 |
| E4 | Describe the stages of COCOMO-II | نظري | Exercise 4.24 |
| E5 | Explain the Putnam model + its limitations | نظري | Exercise 4.26 |
| E6 | What are risk management activities? | نظري | Exercise 4.33 |
| E7 | Compare Walston-Felix with SEL model | مقارنة | Exercise 4.12 |
| E8 | Compute effort for application generator project (COCOMO II) | حساب | Exercise 4.25 |

---

## 4. خطة المراجعة (مرتّبة)

| اليوم | المهام |
|---|---|
| الأول | الفصل كامل قراءة أولى + جدول FP + جدول COCOMO basic (حفظ) |
| الثاني | حل Exercise 4.5, 4.10, 4.11 (FP) + Example 4.1, 4.3 |
| الثالث | حل Example 4.5, 4.6 + Exercise 4.16, 4.21 (COCOMO basic) |
| الرابع | حل Example 4.7, 4.10, 4.11 + Exercise 4.20, 4.25 (COCOMO II + intermediate) |
| الخامس | حل Example 4.12–4.18 + Exercise 4.29 (Putnam) — الجداول D |
| السادس | المراجعة النصية: risk + مقارنات + MCQs 4.1–4.25 |
| السابع | محاكاة امتحان: حل من الذاكرة بلا نظر + تصحيح |


**قاعدة ذهبية:** بعد كل جلسة، **اكتب المعادلة من الذاكرة** قبل ما تنتقل. إذا ما تكدر — ما حفظتها.

---

## ✅ قائمة التحقق
- [ ] أعرف المحاور الـ7 ووزنها
- [ ] أحفظ قوالب الأنماط الـ8
- [ ] أحفظ الأرقام الحرجة (5 units, 14 factors, 15 drivers, 5 scale factors, 7/17 drivers, 2 فئات risk)
- [ ] أكتب خطة المراجعة وألتزمها
- [ ] أتنبأ بالأسئلة E1–E8


---

## Retrieval set (active recall)

| السؤال | الجواب |
|---|---|
| أثقل محورين بالامتحان؟ | ① حساب التقدير ② COCOMO |
| شنو نسبة الحساب بالامتحان؟ | ~**60%** |
| قالب "احسب FP"؟ | عدّ ← أوزان ← UFP ← CAF ← FP |
| قالب "احسب E,D"؟ | اختر mode ← E=a(KLOC)^b ← D=c(E)^d |
| الأرقام الحرجة؟ | 5 units · 14 factors · 15 drivers · 5 SF · 7/17 EM · 2 risk cats |

---
*بُني 2026-10-12 — بناءً على تحليل 207 سلايد + 25 MCQ + 36 تمرين + 19 ورقة امتحان خارجية*