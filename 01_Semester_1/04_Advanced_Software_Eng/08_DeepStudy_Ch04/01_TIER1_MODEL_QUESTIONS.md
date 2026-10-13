---
title: ASE الفصل الرابع — الطبقة النموذجية (Tier 1) — Software Project Planning
course: Advanced Software Engineering
subtitle: الأسئلة الرسمية للفصل (MCQ 4.1–4.25 + Exercises 4.1–4.36) محلولة ومصدرها موثّق
---

# Tier 1 — الأسئلة النموذجية (Ch04 · Software Project Planning)

> **شنو هذا الملف؟** الأسئلة **الرسمية** مال الفصل (من سلايدات الدكتور = سلايدات الكتاب) محلولة، مع مصدر كل جواب.
> هذي **الطبقة الأدنى** — لازم تضمن 100% عليها، لأن امتحان الدكتور = هذي بالضبط + إعادة صياغة.
> **المصدر:** سلايدات 194–199 (MCQ) و 200–207 (Exercises). الجواب ما موجود بالسلايد — استخرجته من نص الفصل وجداوله.

---

## الجزء أ — MCQ 4.1 ← 4.25 (الأجوبة الرسمية)

| # | السؤال (مختصر) | الجواب | السبب/المصدر |
|---|---|---|---|
| **4.1** | بعد تثبيت الـSRS، شنو نقدر نقدّر؟ (Size / Cost / Dev.time / All) | **(d) All of the above** | الثلاثة تُقدَّر بعد SRS — سلايد 3 + Fig 1 |
| **4.2** | أي واحد **مو** مقياس حجم؟ (LOC / Function Count / Cyclomatic Complexity / Halstead) | **(c) Cyclomatic Complexity** | CC = مقياس تعقيد/اختبار، مو حجم |
| **4.3** | Function count طوّرها مَن؟ | **(d) Alan Albrecht** | سلايد 9 ("Alan Albrecht while working for IBM") |
| **4.4** | عدد الـfunctional units بـFPA | **(b) 5** | ILF, EIF, EI, EO, EQ — سلايد 12–13 |
| **4.5** | IFPUG = ؟ | **(c) International Function Point User group** | سلايد 15 |
| **4.6** | FP تُحسب بـ؟ | **(a) UFP × CAF** | سلايد 19 |
| **4.7** | Putnam model مبني على؟ | **(b) Norden/Rayleigh curve** | سلايد 123–125 |
| **4.8** | Manpower build-up بـPutnam = ؟ | **(b) K/td³ persons/year²** | سلايد 143 (`D₀ = K/td³`) — تحقّقت بصرياً سلايد 195 |
| **4.9** | COCOMO طوّرها مَن؟ | **(a) B.W. Boehm** | سلايد 41 ("B.W. Boehm's through his book 1981") |
| **4.10** | COCOMO = ؟ | **(b) Constructive Cost Estimation model** | سلايد 41 |
| **4.11** | Effort للـorganic بـCOCOMO = ؟ | **(a) E = 2.4(KLOC)^1.05** | سلايد 45 (جدول المعاملات) |
| **4.12** | تقدير الحجم يعتمد على؟ (Cost/Schedule/Time/None) | **(d) None of the above** | الحجم يُقدَّر **قبل** cost/schedule — يُشتق من المتطلبات، مو منهم |
| **4.13** | عدد الـcomplexity adjustment factors = ؟ | **(c) 14** | سلايد 21 (F1–F14) |
| **4.14** | COCOMO-II مبني على؟ | **(b) Algorithm approach** | نموذج خوارزمي (algorithmic) — يقارن بBottom-up/Top-down كبدائل خاطئة |
| **4.15** | Cost estimation يشمل؟ | **(d) All of the above** | software + hardware + personnel — سلايد 33 |
| **4.16** | حجم 2–50 KLOC ⇒ أي mode؟ | **(a) Organic** | سلايد 43 (Organic = صغير، مألوف) |
| **4.17** | COCOMO-II طوّرت وين؟ | **(b) University of Southern California** | USC (Boehm انتقل لـUSC) — [خارجي/معياري] |
| **4.18** | أي واحد **مو** فئة COCOMO-II؟ | **(c) Requirement Sector** | الفئات: End-user programming, Infrastructure, Application generators, System integration — سلايد 73 |
| **4.19** | أي واحد **مو** infrastructure software؟ | **(d) Result management system** | OS/DBMS/Compilers = infrastructure؛ نظام إدارة نتائج = تطبيقي |
| **4.20** | عدد مراحل COCOMO-II = ؟ | **(b) 3** | Application Composition / Early Design / Post-Architecture — سلايد 74 |
| **4.21** | أي واحد **مو** مرحلة COCOMO-II؟ | **(d) Comprehensive cost estimation model** | مو مرحلة — سلايد 74 |
| **4.22** | معادلة Rayleigh curve = ؟ | **(c) m(t) = 2Kat·e^(−at²)** | سلايد 125 حرفياً: `m(t) = 2·k·a·t·e^(−a·t²)` (تحقّقت بصرياً) |
| **4.23** | Technology factor `C` = ؟ | **(a) C = S·K^(−1/3)·td^(−4/3)** | من `S = C·K^(1/3)·td^(4/3)` ⇒ `C = S/(K^(1/3)·td^(4/3))` — سلايد 149 (تحقّقت بصرياً) |
| **4.24** | Risk management activities تُقسَّم إلى كم فئة؟ | **(b) 2 Categories** | Risk Assessment + Risk Control — Fig 9 سلايد 190 |
| **4.25** | أي واحد **مو** نشاط risk management؟ | **(c) Risk generation** | الأنشطة: assessment + control (الموجود غير "generation") |

**⚠️ ملاحظة ترقيم:** سلايد 194 فيه 4.1–4.4، وسلايد 195 يبدأ بـ4.5 **بعد** 4.6/4.7 (انقلاب تنسيقي). الترتيب الصحيح أعلاه.

### الأجوبة الحرجة اللي يغلط بها الطالب (ركّز)
- **4.12 = (d) None** — فخ شائع؛ يحسبها الطالب "Cost" لكن الحجم مستقل.
- **4.18 = (c)** و **4.19 = (d)** و **4.21 = (d)** — أسئلة "أي واحد **مو**" — انتبه للنفي.
- **4.8 = (b)** و **4.22 = (c)** و **4.23 = (a)** — معادلات؛ إذا حفظتها خطأ تخسر. **احفظها رمزياً** (شوف الجدول D بـ`99_SOURCE_MAP.md`).
- **4.24 = (b) فئتان** (مو 5 — الـ5 هي تصنيفات **المخاطر** مال Jones، مو أنشطة الإدارة). هذا فخ خطير!

---

## الجزء ب — Exercises 4.1 ← 4.36 (الرسمية)

> التمارين مو كلها "اسألة نصية" — منها حسابي. الحسابيات راح تنحل بالتفصيل بـ`ByType/T7_Apply_Calc.md`، وهنا أعطيك **خطة الجواب + الجواب المختصر** لكل تمرين.

### ب-1) تمارين مفاهيمية (نصية)

| # | المطلوب | خطة الجواب | المصدر |
|---|---|---|---|
| **4.1** | Activities during software project planning | اذكر: size estimation ← cost estimation ← development time ← resource allocation ← risk management. (Fig 1) | سلايد 4، كتاب ص.140 |
| **4.2** | Any two size estimation techniques | LOC (Conte) + Function Points (Albrecht). اشرح كل واحدة + عيوبها/محاسنها | سلايد 5–19 |
| **4.3** | عدّ الـ`;` بـC مقابل LOC — قيّم | **قوة:** أدق من LOC (تتجاهل الفراغات/التنسيق) · **ضعف:** لا تميّز بين `;` بالسلاسل النصية، ولا تعكس التعقيد المنطقي، لغة-معتمدة | سلايد 8 (Conte) + [تحليل] |
| **4.4** | صمّم LOC counter — لغة-معتمدة؟ | خطة: صفّح الملف، استثنِ comments/blank lines، عدّ الأسطر. **نعم لغة-معتمدة** (تعريف السطر يختلف). **قيود:** السلاسل النصية، continuation lines، التعريفات تختلف بين اللغات | سلايد 5–8 |
| **4.6** | Concept of FP + ليش مقبولة بالصناعة؟ | FP = قياس الوظائف من منظور المستخدم مستقل عن اللغة. مقبولة لأنها: مستقلة عن اللغة/التقنية، تُحسب من المتطلبات بدري، تخدم الأنظمة الـnon-procedural | سلايد 9–15 |
| **4.7** | Size metrics + محاسن FP على LOC | Size metrics: LOC, FP, object points. FP أفضل لأنها **لغة-مستقلة** وتحسب من مرحلة المتطلبات | سلايد 15 |
| **4.8** | يمكن تقدير الحجم قبل الكود؟ | نعم — FP تُحسب من SRS (المدخلات/المخرجات/الملفات) قبل أي سطر كود | سلايد 10–16 |
| **4.9** | Albrecht's function count + مثال | اشرح الخطوات: عدّ الوحدات ← صنّف التعقيد ← UFP ← CAF ← FP. مثال: استخدم example 4.1 (سلايد 23) | سلايد 23–24 |
| **4.12** | Walston-Felix مقابل SEL | جدول: W-F `E=5.2L^0.91`, `D=4.1L^0.36`؛ SEL `E=1.4L^0.93`, `D=4.6L^0.26`, `DOC=30.4L^0.90`. **الفرق الجوهري:** W-F أكثر تحفظاً (a أعلى ⇒ LOC أقل لنفس الجهد) | سلايد 36–40 |
| **4.15** | COCOMO modes + phase distribution | 3 modes + نسبة الجهد لكل مرحلة (تصميم 16–18%، برمجة 48–68%…). سلايد 60 | سلايد 43, 60 |
| **4.16** | كل مستويات COCOMO + احسب organic 32KLOC | Basic/Intermediate/Detailed. الحساب: `E=2.4(32)^1.05`, `D=2.5·E^0.38` | سلايد 41, 45 |
| **4.17** | علاقة LOC/PM لكل المودات + معقوليتها | اشتق: `LOC/E = KLOC·1000/E`. لاحظ إن كلما كبّر الموديل، الـproductivity تنخفض (embedded أقل) | سلايد 45 [تحليل] |
| **4.18** | كيف تتغير phase distribution لو غيّرنا drivers؟ | **Analyst capability↑** ⇒ جهد كلي↓ · **Modern PL↑** ⇒ جهد↓ · **Reliability↑** ⇒ جهد↑ · **Requirements volatility↑** ⇒ جهد↑ (إعادة عمل) | سلايد 56, 60 |
| **4.19** | برنامج يطبّق COCOMO | مشروع برمجي — خطة: input KLOC+mode ⇒ output E, D, SS | [تطبيقي] |
| **4.22** | COCOMO-II بالتفصيل + الفئات | 4 فئات + 3 مراحل | سلايد 73–74 |
| **4.23** | Infrastructure Sector بـCOCOMO-II | OS, DBMS, compilers, communications — يُبنى بـpost-architecture | سلايد 73, 106 |
| **4.24** | مراحل COCOMO-II — أيها الأشهر ولماذا؟ | 3 مراحل. **Early Design** الأشهر لأنها تخدم mid-size قبل اكتمال الـarchitecture، وتوازن الدقة/السرعة | سلايد 85 [تحليل] |
| **4.26** | Putnam model + قيوده | اشرح Rayleigh + القيود: يفترض منحنى مثالي، لا يصمد للمشاريع الصغيرة، حساسية عالية للـtd | سلايد 123–156 |
| **4.27** | Time–cost trade-off بـPutnam | Table 20: قلّل td ⇒ K يزيد بشكل حاد (غير خطي). `S=C·K^(1/3)·td^(4/3)` | سلايد 149–150 |
| **4.28** | اشتق معادلات time & effort | اشتق `S=C·K^(1/3)·td^(4/3)` من `P=φD^(−2/3)` (سلايد 147) | سلايد 147 |
| **4.30** | قارن بيانات productivity مع الموديلات | تمرين ميداني — يطلب بيانات حقيقية | [ميداني] |
| **4.31** | ليش نقدّر بدري؟ ومتى لا؟ | نقدّر بدري للتخطيط/العقود/الجدولة. **لا** نقدّر بدري إذا المتطلبات ما زالت تتغيّر جذرياً | سلايد 33–34 [تحليل] |
| **4.32** | مخاطر نموذجية + أثر staff turnover | Jones' top-5 + turnover = خطر عالي (فقدان معرفة). سلايد 189 | سلايد 184–189 |
| **4.33** | أنشطة risk management + هل تُرتَّب؟ | Assessment (id/analysis/prioritization) + Control (planning/monitoring/resolution). نعم تُرتَّب حسب risk exposure = prob × loss | سلايد 190–191 |
| **4.34** | Risk exposure + كيف تسيطر على كل خطر | RE = prob × magnitude. تقنيات: avoidance, transfer, mitigation, acceptance | سلايد 191–192 |
| **4.35** | Risk؟ هل الإدارة اقتصادية؟ أثرها على الكلفة؟ | الإدارة تقلل "surprise factor" ← تقلل كلفة الطوارئ الكبيرة (الاستثمار الوقائي أرخص من الإصلاح) | سلايد 180–183 |
| **4.36** | مخاطر مشروع طالب | عدّد: وقت ضيق، خبرة قليلة، متطلبات غامضة، أدوات جديدة، فقدان عضو فريق | سلايد 184–189 [تطبيقي] |

### ب-2) تمارين حسابية (الجواب الكامل في T7)

| # | المطلوب (مختصر) | نوع الحساب |
|---|---|---|
| **4.5** | FP لمشروع (user inputs=30, outputs=42, enquiries=8, files=7, ext.interfaces=6، كل التعقيدات moderate) | FP/CAF |
| **4.10** | FP لبرنامج payroll (ملف موظفين + ملف شهري + طباعة شيكات + أمر تفاعلي) | FP/CAF |
| **4.11** | FP للـpayroll بعد إضافة ملف إضافي (مقارنة شهرين) + فسّر الفرق | FP/CAF + تحليل |
| **4.13** | حجم 22000 LOC — احسب الجهد بـW-F وSEL | Empirical |
| **4.14** | جهد 100 PM — احسب LOC والـproductivity | Empirical |
| **4.16** | organic 32 KLOC — احسب E وD | COCOMO basic |
| **4.20** | 5 modules (0.5+1.5+2+1+2=7 KLOC)، تعقيد وموثوقية عالية، قدرة مبرمج منخفضة — احسب cost & schedule + phase-wise | COCOMO basic + phase |
| **4.21** | 600 KLOC — احسب E وD لكل المودات الثلاثة | COCOMO basic |
| **4.25** | 100 KLOC application generator، B عالي precedentness+flexibility، drivers: high reliability, medium DB, high PCAP+ACAP — احسب E | COCOMO II early design |
| **4.29** | Putnam: S=100,000, C=5000, Do=15 — احسب td وKd | Putnam |

---

## الجزء ج — أسئلة إعادة صياغة بنمط الدكتور (على نفس المستوى)

> هذي مو رسمية — أنا ولّدتها بنفس نمط MCQ 4.1–4.25. جوابها من نفس الجداول.

### ج-1) MCQ إضافية (نفس النمط)

| # | السؤال | الجواب |
|---|---|---|
| R1 | FP formula: `CAF = 0.65 + 0.01·ΣFi` — أقصى قيمة للـΣFi = ؟ | **70** (14×5) ⇒ CAF أقصى = **1.35** |
| R2 | أي weighted factor أكبر بـUFP للـILF عالية التعقيد؟ | **15** |
| R3 | بـbasic COCOMO، لو تضاعف الحجم (KLOC)، الـeffort تزيد؟ | أكثر من الضعف (لأن الأس b>1) |
| R4 | أي mode يعطي أعلى b_b؟ | **Embedded (1.20)** ⇒ أسرع نمو للجهد مع الحجم |
| R5 | الـ15 cost driver بالـintermediate COCOMO مقسّمة على؟ | **4 مجموعات** (product, hardware, personnel, project) |
| R6 | D₀=27 معناها؟ | **إعادة بناء software من موجود** |
| R7 | عدد الـscale factors بـCOCOMO II early design = ؟ | **5** |
| R8 | عدد الـcost drivers بـPost-Architecture = ؟ | **17** |

### ج-2) أسئلة "اشرح/قارن" (نمط تمارين الدكتور)

| # | السؤال | المفاصل |
|---|---|---|
| R9 | اشرح علاقة LOC بـproductivity عبر المودات الثلاثة | كلما كبّر الموديل ⇒ productivity تنخفض |
| R10 | قارن Basic vs Intermediate vs Detailed COCOMO | Basic: فقط الحجم · Intermediate: +15 driver/EAF · Detailed: +phase-sensitive |
| R11 | اشرح ليش FP أكثر "إنصافاً" للغات high-level من LOC | LOC تعاقب اللغات المختصرة (سطر واحد بـC++ = عدة أسطر بـassembly) |
| R12 | اشرح معنى "risk exposure" وكيف نرتّب المخاطر بيها | RE = probability × magnitude ⇒ الأولوية للـRE الأعلى |

---

## ✅ قائمة التحقق (Self-check)
- [ ] أذكر الـ5 functional units وأوزانها (Low/Avg/High) من ذاكرتي
- [ ] أكتب `FP = UFP × CAF` و `CAF = 0.65 + 0.01ΣFi` بدون النظر
- [ ] أحفظ جدول basic COCOMO (2.4/1.05/2.5/0.38 للـorganic…) بدون النظر
- [ ] أعرف الفرق: a_b (2.4) ≠ a_i (3.2) للـorganic
- [ ] أذكر الفرق بين مسطرة Putnam: D=K/td² و D₀=K/td³
- [ ] أحفظ أنشطة risk = 2 فئات (مو 5)
- [ ] أعرف الـ4 فئات و3 مراحل COCOMO II


---

## Retrieval set (active recall)

| السؤال | الجواب |
|---|---|
| 4.8 manpower build-up = ؟ | **K/td³ persons/year²** (b) |
| 4.12 الحجم يعتمد على؟ | **(d) None** — مستقل |
| 4.13 عدد CAF = ؟ | **14** |
| 4.16 حجم 2–50 KLOC ⇒ ؟ | **Organic** |
| 4.18 مو فئة COCOMO-II؟ | **Requirement Sector** |
| 4.22 Rayleigh eq = ؟ | **2Kat·e^(−at²)** (c) |
| 4.23 technology factor C = ؟ | **SK^(−1/3)td^(−4/3)** (a) |
| 4.24 أنشطة risk = ؟ | **2 فئات** (b) |
| 4.25 مو نشاط risk؟ | **Risk generation** (c) |

---
*المصدر: `chapter_4_software_project_planning.pdf` (207 سلايد) + كتاب AliFahim ص.140–196 — بُني 2026-10-12*