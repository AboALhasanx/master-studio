# خريطة المصادر الخارجية — بنوك أسئلة ونماذج امتحانات مبنية على مادة الـAI

> **الغرض:** تتبّع أصل مواد مقرر الذكاء الاصطناعي (CS605) في المكتبة، ثم جرد المواقع والمستودعات المنشورة التي تنشر **أسئلة / نماذج امتحانات / بنوك تمارين** مبنية على نفس المصدر ونفس الموضوعات.
> **أُعدّ:** 2026-10-05 — بحث ويب مُتحقَّق منه (كل رابط أدناه فُتح فعلياً).
> **الخلاصة السريعة:** نعم — يوجد أكثر من مصدر رسمي مفتوح ينشر أسئلة وامتحانات محلولة على نفس الموضوعات بالضبط. أهمها **بنك تمارين AIMA الرسمي** و**امتحانات Berkeley CS188 بحلولها**.

---

## 1. أصل المادة (Origin) — من وين جاءت محاضرات الـAI في المكتبة؟

| العنصر | المصدر |
|:---|:---|
| **سلسلة المحاضرات** `l1.pptx … l10.pptx` | **Diane J. Cook** — مقرر **CptS 440 / 540: Artificial Intelligence**، جامعة **Washington State University**، قسم EECS، **خريف 2009** |
| **الكتاب المرجعي** | **Russell & Norvig** — *Artificial Intelligence: A Modern Approach* (AIMA) — محلياً: `AIMA_Russell_Norvig_4th_Edition.pdf` |
| **ملفات إضافية** (`chatbots.pptx`, `datamining.pptx`, `answer.pptx`, `lisp/`, `homework/`) | نفس مقرر Cook (مواد مساندة) |

**النتيجة:** المحاضرات مو من إعداد د. سيف — هي **مجموعة محاضرات جامعية أمريكية مفتوحة** استُخدمت كمصدر موازٍ ريثما يبدأ الطبيب بإلقاء المقرر. المقرر الأصلي فيه **امتحانان** (Exam #1 الأسبوع 13، Exam #2 الأسبوع 27) — لكن **أوراق الامتحان نفسها غير منشورة** على موقع Cook.

**موقع Cook الأصلي (حيّ حتى 2025):**
- الصفحة الرئيسية: https://eecs.wsu.edu/~cook/ai/
- الجدول الدراسي: https://eecs.wsu.edu/~cook/ai/schedule.html
- الواجبات: https://eecs.wsu.edu/~cook/ai/hw/hw.html
- المنهج: https://eecs.wsu.edu/~cook/ai/syllabus.pdf

---

## 2. بنوك الأسئلة والتمارين المنشورة (Question Banks)

### ① بنك تمارين AIMA الرسمي — الأهم ⭐
> **هذا هو المرجع الرسمي** لتمارين الكتاب اللي يعتمده الطبيب. وفي الإصدار الرابع، التمارين صارت **أونلاين فقط** (مو مطبوعة في الكتاب).

| | |
|:---|:---|
| **الموقع** | https://aimacode.github.io/aima-exercises/ · https://nalinc.github.io/aima-exercises/ |
| **المستودع** | https://github.com/aimacode/aima-exercises |
| **المحتوى** | تمارين لكل فصول الكتاب الـ27 — **26 فصل مُنفَّذ** |
| **الفصول المهمة لنا** | Ch.3 Search (**40 تمرين** — 3.1…3.40) · Ch.4 Beyond Classical Search · Ch.5 Adversarial Search · Ch.6 CSP · Ch.7–9 Logic/FOL/Inference |
| **الحلول** | فيه مجلد `answers/` لكل فصل — حلول مجتمعية (مو كلها محلولة) |
| **البحث** | الموقع فيه **محرك بحث** (lunr.js) — تكتب مصطلح ويطلعلك التمرين |

**أمثلة على التمارين الفعلية (Ch.3):**
- `3.1` — «Explain why problem formulation must follow goal formulation.»
- `3.11` — مسألة **المبشّرون وآكلي لحوم البشر** (Missionaries & Cannibals) — صياغة فضاء الحالة.
- `3.27` — **«Trace A\* search applied to getting to Bucharest from Lugoj»** — نفس نمط الطبيب (تتبّع يدوي).
- `3.31` — دالة تقييم Pohl: `f(n)=(2−w)g(n)+wh(n)` — لأي قيم `w` تكون كاملة؟

> **ملاحظة مهمة:** التمارين **بلا حلول رسمية كاملة** — بس فيها تلميحات داخل بعض الأسئلة، ومجلد answers مجتمعي جزئي.

### ② كتاب الحلول الرسمي (Solutions Manual)
| المصدر | الرابط | الملاحظة |
|:---|:---|:---|
| حلول AIMA 4th ed (مجتمعية) | https://github.com/goughbry/AIMA-Exercises | حلول بعض التمارين |
| Solution Manual (4th ed) | https://studylib.net/doc/27633000/ | دليل الحلول — تحقّق من الحقوق قبل التوزيع |

### ③ مستودع WSU CptS 540 (طالب سابق) — فيه **امتحان نهائي حقيقي** ⭐
| | |
|:---|:---|
| **الرابط** | https://github.com/angelxd84130/WSU-cpts-540-ArtificialIntelligence |
| **المحتوى** | **واجبات HW1–HW12** (نسختان: أسئلة فقط + أسئلة مع أجوبة) + **`FinalExam_Yu-Chieh_Wang.pdf`** |
| **الأهمية** | هذا **نفس المقرر** (CptS 540 = نسخة الدراسات العليا من 440) — الأسئلة مبنية حرفياً على محاضرات Cook |

**واجبات Cook الرسمية (من موقعها):** HW1–HW6، مع ملفات مساندة: `h2.c`، `h3.c`، `grammar2.pl`، Netica، dictionary — https://eecs.wsu.edu/~cook/ai/hw/hw.html

### ④ امتحانات Berkeley CS188 — بحلولها، على صفحة Russell نفسه ⭐⭐
> **أقوى مصدر امتحانات**: مؤلف الكتاب نفسه (Stuart Russell) ينشر **امتحانات + حلول** لسنوات متعددة.

| | |
|:---|:---|
| **الرابط (الأرشيف)** | https://people.eecs.berkeley.edu/~russell/classes/cs188/f14/exams.html |
| **المحتوى** | **Midterm 1 + Midterm 2 + Final** لكل من: Spring 2014 · Fall 2013 · Spring 2013 · Fall 2012 · Spring 2012 · Fall 2011 · Spring 2011 — **كل امتحان مع ملف الحلول** |
| **الحديث** | https://inst.eecs.berkeley.edu/~cs188/fa24/resources/ (+ الامتحانات السابقة) |
| **الميزة** | أسئلة **تتبّع خوارزميات** (A*, alpha-beta) بنفس نمط امتحانات الطبيب المتوقّع |

### ⑤ امتحانات University of Wisconsin–Madison CS540 — بحلولها
| | |
|:---|:---|
| **الرابط** | https://pages.cs.wisc.edu/~dyer/cs540/exams-toc.html |
| **المحتوى** | Midterm (`exam1-f19.pdf` + الحلول) + Final — تغطية AIMA Ch.3.1–3.6، 4.1، 5.1–5.3، 5.5 |
| **أرشيف إضافي** | https://pages.cs.wisc.edu/~skrentny/cs540/exams.html |
| **الميزة** | أسئلة مرتبطة صراحةً بأرقام فصول AIMA |

### ⑥ مصادر تمارين إضافية (متفرقة)
| المصدر | الرابط |
|:---|:---|
| Alberto Metelli — AI Exercises (Politecnico di Milano) | https://albertometelli.github.io/files/2021-fai/exercises.pdf |
| fran-galic — Intro to AI (search, resolution, decision) | https://github.com/fran-galic/Introduction-to-Artificial-Intelligence |
| AIMA الرسمي — موقع الكتاب | https://aima.cs.berkeley.edu/ |

---

## 3. المواد الرسمية المجانية من موقع AIMA (أساس الكتاب)

من https://aima.cs.berkeley.edu/ (بلا شراء):
- **Exercises (website)** → https://aimacode.github.io/aima-exercises/
- **Figures (pdf)** → https://aima.cs.berkeley.edu/figures.pdf
- **Code (website)** → https://github.com/aimacode
- **Pseudocode (pdf)** → https://aima.cs.berkeley.edu/algorithms.pdf
- **Bibliography + LaTeX .bib** → للاقتباس

---

## 4. شنو المفيد للطالب (Student)

| الأولوية | المورد | ليش |
|:-:|:---|:---|
| 1 | **بنك تمارين AIMA** (Ch.3, 5, 6) | نفس الكتاب اللي يعتمده الطبيب — أسئلة رسمية |
| 2 | **امتحانات Berkeley CS188 بحلولها** | تتبّع A*/alpha-beta بنمط الامتحان — مع الحل للمقارنة |
| 3 | **مستودع WSU CptS 540** (HW1–12 + الامتحان النهائي) | نفس مقرر Cook حرفياً — أسئلة وأجوبة |
| 4 | **امتحانات Wisconsin CS540** | أسئلة مربوطة بأرقام فصول AIMA |
| 5 | `answer.pptx` المحلي (مجلد extras) | مفتاح إجابات من مقرر Cook الأصلي |

## 5. شنو المفيد للأستاذ (Professor)

| المورد | الاستخدام |
|:---|:---|
| **بنك تمارين AIMA** | سحب أسئلة جاهزة مصنّفة حسب الفصل + إضافة أسئلة جديدة |
| **امتحانات Berkeley CS188** | نماذج امتحانات مصمّمة بعناية + معايير تصحيح (الحلول) |
| **موقع AIMA الرسمي** | شرائح، أشكال، شيفرة، وشبه-كود جاهزة للتدريس |
| **WSU CptS 540** | واجبات كاملة مع ملفات بدء (`h2.c`, `h3.c`) و`grammar2.pl` |
| **Netica** (https://www.norsys.com) | أداة شبكات بايزية — مستخدمة في HW#5 |
| **SWI-Prolog** (https://www.swi-prolog.org) | لتمارين Prolog |

---

## 6. تنبيهات مهمة

1. **الامتحانات المنشورة مو امتحانات د. سيف** — هي من مقررات أجنبية على **نفس الكتاب ونفس الموضوعات**. مفيدة للتدريب، مو «تسريب».
2. **Cook Fall 2009 قديم** (قبل عصر التعلّم العميق) — لسا ممتاز لـ agents/search/logic/ML الكلاسيكي، بس لازم يُضاف **AIMA 4th ed** للفصول الحديثة.
3. **حقوق النشر:** كتاب الحلول والكتاب نفسه محميان — للاستخدام الشخصي/الدراسي فقط، مو للنشر.
4. **لا تبنِ ملازم الآن** — مقرر الـAI موقوف لحد ما يبدأ الطبيب (قاعدة: تسجيل فقط).

---

*أُعدّ هذا الملف من بحث ويب مُتحقَّق منه — كل رابط رئيسي فُتح وتم التأكد من محتواه.*
