---
title: "المنهج المقرر — Prescribed Curriculum (Master of Programming Science)"
course: "00_STUDIO_HUB"
subtitle: "المقررات + المفردات الأسبوعية + المصادر المقترحة — من استمارات الوصف الأكاديمي الرسمية 2024-2025"
last_updated: 2026-10-06
source: "official_curriculum/03_Academic_Description_FirstCourse_2024-2025.pdf (+ EN)"
status: "First Course extracted; Second Course (scanned) pending"
---

# المنهج المقرر — المقررات والمفردات والمصادر

> **المصدر:** استمارات **الوصف الأكاديمي** الرسمية (Academic Program & Course Description Guide, 2024-2025) —
> الصادرة عن **قسم البرامجيات، كلية علوم الحاسوب وتكنولوجيا المعلومات، جامعة واسط**، بإشراف
> **جهاز الإشراف العلمي / دائرة ضمان الجودة والاعتماد**، وفق إطار **مساري بولونيا + وزارة التعليم العالي**.
> **اسم البرنامج الرسمي:** *Master of Programming Science* (ماجستير علوم البرمجة).

---

## 1. هوية البرنامج

| البند | القيمة |
|:---|:---|
| الجامعة | جامعة واسط |
| الكلية | كلية علوم الحاسوب وتكنولوجيا المعلومات |
| القسم العلمي | **قسم البرامجيات (Software Department)** |
| اسم البرنامج | **Master of Programming Science** |
| الشهادة النهائية | Master of Programming Science |
| تاريخ إعداد الوصف | 10/9/2024 |
| أصل المنهاج | مسار **بولونيا** — كتاب قسم الدراسات **ت 312906** بتاريخ **15/3/2023** |
| الرؤية | برنامج أكاديمي بمعايير دولية في علوم البرمجيات (يستهدف اعتماد **ABET**) |
| معيار القبول | **معدل الطالب + امتحان التنافس** |

> **ملاحظة:** أسماء التدريسيين أدناه من نسخة **2024-2025** — وتدور سنوياً (أسماء دفعتك الحالية قد تختلف).

---

## 2. هيكل الكورس الأول (الفصل الأول) — 6 مقررات

| # | المقرر | الوحدات | التدريسي (2024-2025) |
|:--:|:---|:--:|:---|
| 1 | **Data Mining** — تنقيب البيانات | 2 | د. ضياء شهيد صابر |
| 2 | **Software Development Techniques** — تقنيات تطوير البرمجيات | 2 | د. سنان عدنان ديوان |
| 3 | **Cyber Security** — الأمن السيبراني | 2 | د. رياض رحيف نعيّا |
| 4 | **English** — الإنجليزية | 1 | د. حيدر علوان |
| 5 | **Advanced Software Engineering** — هندسة البرمجيات المتقدمة | 3 | (بلا استمارة مفصّلة في هذا الملف) |
| 6 | **Computer Vision** — الرؤية الحاسوبية | 2 | د. عبد الهادي محمد داخل (العليدي) |

> المجموع ≈ **12 وحدة**. (الموقع الرسمي يعرض أيضاً «Multimedia» بدل «Computer Vision» في نظام آخر — انظر قسم التعارض.)

---

## 3. المفردات الأسبوعية + المصادر — مقرر بمقرر

### 3.1 Computer Vision — الرؤية الحاسوبية (2 وحدة / 30 ساعة)
**الهدف:** أساسيات الكاميرات والبصريات، الضوء واللون، أهرام الصور، تحليل النطاق الترددي، والتطبيقات.
**المفردات الأسبوعية:**

| الأسبوع | المفردة |
|:---:|:---|
| 1 | Introduction to CV: تعريف ونطاق؛ التطوّر والتطبيقات؛ خط أنابيب الرؤية الحاسوبية |
| 2 | Image Formation & Preprocessing: الالتقاط، التمثيل، فضاءات الألوان |
| 3–7 | Image Enhancement: الترشيح (Filtering)، معادلة المدرّج (Histogram Equalization)، تعديل التباين |
| 8–11 | Segmentation & Feature Extraction: العتبة (Thresholding)، الطرق القائمة على المناطق؛ التحويلات الهندسية (Scaling/Rotation/Affine)؛ كشف الحواف (Canny)، تحليل النسيج، كشف نقاط المفتاح |
| 12–15 | Image Classification & Object Recognition: SVM، KNN، التجميع؛ **CNN** وتعلّم النقل (Transfer Learning)؛ التتبّع وتقدير الحركة (Optical Flow)؛ مرشّحات Kalman وParticle؛ رؤية ثلاثية الأبعاد (Stereo، عمق، إعادة بناء) |
| متقدّم | Generative Models، **Vision Transformers**، Self-Supervised Learning + مشروع نهائي |

**أدوات مفاهيمية إضافية (من أهداف المقرر):** Hough Transform · RANSAC · **SIFT / SURF** · المورفولوجيا (Erosion/Dilation/Opening/Closing) · نماذج توليدية/تمييزية.
**المصادر:**
- **مقرر رئيسي:** Szeliski, R., *Computer Vision: Algorithms and Applications*, Springer, 2010.
- **مقترحة:** Forsyth & Ponce, *Computer Vision: A Modern Approach*, 2nd ed., Prentice Hall, 2011 · Prince, *Computer Vision: Models, Learning, and Inference*, Cambridge UP, 2012 · Davies, *Computer and Machine Vision*, 4th ed., Academic Press, 2012 · Nixon & Aguado, *Feature Extraction and Image Processing for Computer Vision*, Academic Press, 2012.

---

### 3.2 Software Development Techniques — تقنيات تطوير البرمجيات (2 وحدة / 30 ساعة)
**الهدف:** تعلّم تقنيات تطوير البرمجيات ومبادئها.
**المفردات الأسبوعية:**

| الأسبوع | المفردة |
|:---:|:---|
| 1 | Introduction to Software Development |
| 2 | Agile Methodology |
| 3 | Extreme Programming (XP) Model |
| 4 | Scrum Model |
| 5 | Lean Software Development / Kanban Model |
| 7 | Project Planning / Task Estimate |
| 8 | Requirements of Project |
| 9 | Software Architecture |
| 10 | Design Principles |
| 11 | Code Construction |
| 12 | Smart Programming by Python |
| 13 | Functions by Python |
| 14 | Recursion by Python |

**المصادر:** لم تُطبع قائمة مراجع صريحة في الاستمارة (المرجع = محاضرات المقرر + كتب مكتبة الكلية).

---

### 3.3 Data Mining — تنقيب البيانات (2 وحدة / 30 ساعة)
**الهدف:** دراسة تفصيلية لمفهوم تنقيب البيانات وأساليبه.
**المفردات الأسبوعية:**

| الأسبوع | المفردة |
|:---:|:---|
| 1 | Introduction: مفهوم التنقيب، تنقيب المعرفة المتعدد، التنقيب والدراسات، التطبيقات، والمجتمع |
| 2 | Data, Measurements & Processors: أنواع البيانات، إحصاءاتها، مقاييس التشابه والاختلاف، البيانات الكمّية، التنظيف والدمج، التحويل، تقليل الأبعاد |
| 3 | Data Warehousing & OLAP: مستودع البيانات، معمارية وتنصيب، **Data Lake** |
| 4 | Data Warehouse Modeling: البنية والمقاييس، **Data Cube**، النماذج متعددة الأبعاد، التسلسلات الهرمية، عمليات **OLAP**، إسناد قيم المكعبات |
| 5 | Basic Methods & Concepts: المفاهيم الأساسية، طرق تعدين الأنماط المتكررة، تقييم الأنماط |
| 7 | Cluster Analysis (Advanced): التجميع الاحتمالي، التجميع متعدد الأبعاد، تقليل الأبعاد، تجميع المخططات والشبكات |
| 8 | Deep Learning: المفاهيم الأساسية، نماذج وطرق التحسين، **CNN**، **RNN** |

**المصدر:** Han, Pei & Tong, *Data Mining: Concepts and Techniques*, **4th Edition**, Morgan Kaufmann, **2023**. *(تطابق كتابك الحالي.)*

---

### 3.4 Cyber Security — الأمن السيبراني (2 وحدة / 30 ساعة)
**الهدف:** فهم شامل للأمن السيبراني وتطبيقاته المتقدمة.
**المفردات (بالكتل الزمنية):**

| الأسابيع | المفردة |
|:---:|:---|
| 1–4 | Introduction to Cybersecurity (16 ساعة) |
| 5–8 | Risk Management, Security Policies & Cryptography (16 ساعة) |
| 9–15 | Network Security, Web Application Security & Malware (28 ساعة) |
| 16–17 | Malware Detection & Cloud Security Challenges (8 ساعة) |
| 18–19 | Mobile Security & Internet of Things (IoT) (8 ساعة) |
| 20–25 | Penetration Testing & Incident Response (24 ساعة) |
| 26–30 | **AI & Blockchain in Cybersecurity** + المشروع النهائي (20 ساعة) |

**المصادر:**
- Robin Sharp, *Introduction to Cybersecurity: A Multidisciplinary Challenge*.
- Dr Kutub Thakur & Dr Al-Sakib Khan Pathan, *Cybersecurity Fundamentals: A Real-World Perspective*.
- Charles J. Brooks et al., *Cybersecurity Essentials*, 1st ed.

---

### 3.5 English — الإنجليزية (1 وحدة / 15 ساعة)
**الهدف:** القراءة والكتابة، المفردات، القواعد، الاستماع والتحدّث.
**المفردات الأسبوعية:** It's a wonderful world (Tenses) · Auxiliary Verb · Reading Skills · Present Simple/Continuous · Passive Voice · Sport & Leisure vocab · Past Simple · Art & Literature vocab · Reading/Speaking · Giving Opinion · Modal Verb · Obligation & Permission · How to Behave Abroad · Good Manners / Nationality Words · Request & Offers.
**التقييم:** **30 علامة سعي** (تحضير يومي، امتحانات يومية/شفهية/شهرية) + **70 امتحان نظري نهائي**.

---

### 3.6 Advanced Software Engineering — هندسة البرمجيات المتقدمة (3 وحدات)
**لا توجد استمارة مفصّلة للمقرر داخل ملف الكورس الأول** — مُدرَج في الهيكل بـ3 وحدات فقط.
**المصدر المعروف من مادة التنافسي:** **Sommerville** (وليس Aggarwal & Singh اللي عليه سلايدات الصف).
**ملاحظة:** هذا **أكبر مادة في الفصل (3 وحدات = ~23% من المعدل التراكمي)** — أولوية دراسة عالية.

---

## 4. التعارض مع مقرراتك الفعلية ⚠️

| | المقررات الرسمية (الوصف الأكاديمي) | **مقرراتك الفعلية (الفصل الأول)** |
|:---|:---|:---|
| متطابقة | Data Mining · Cyber Security · English · Advanced SE | ✅ نفسها |
| مختلفة | Software Development Techniques · **Computer Vision** | **Soft Computing · Artificial Intelligence** |

> **خلاصة:** 4 من 6 متطابقة. دفعتك تستبدل (Software Dev Tech + Computer Vision) بـ(Soft Computing + AI).
> التفسير المرجّح: **Soft Computing** نسخة-دفعة من **Computer Vision** (كلاهما للدكتور عبد الهادي)، و**AI** نُقل للفصل الأول.

**مصادر مقرراتك الفعلية (من خارج الوثيقة الرسمية):**
- **Artificial Intelligence:** Luger, *AI: Structures and Strategies* (6th ed.) — مرجع التنافسي · AIMA (Russell & Norvig) — مرجع السلايدات (Cook/WSU).
- **Soft Computing:** Mitchell, *An Introduction to Genetic Algorithms* · Sivanandam & Deepa, *Principles of Soft Computing*.

---

## 5. الكورس الثاني (الفصل الثاني) — قيد الاستخراج

الوصف الأكاديمي للكورس الثاني **2024-2025** موجود لكنه **سكانيد بلا طبقة نصية** (35 صفحة).
المقررات المتوقعة (من الخطة المنشورة): Advanced AI · Advanced Algorithms Design · Software Architecture · Web Development · Cloud Computing · Research Methodology.
**الإجراء التالي:** رندر الصفحات + قراءة بصرية لاستخراج المفردات والمصادر (جاهز إذا تريد).

---

## 6. المراجع
- الملفات: `official_curriculum/03_Academic_Description_FirstCourse_2024-2025.pdf` (+ `_AR.txt`, `03b_..._EN.pdf`) · `04_Academic_Description_SecondCourse_2024-2025.pdf`.
- الفهرس الكامل: `00_STUDIO_HUB/official_docs/OFFICIAL_DOCS_INDEX.md`.
- التحليل التنظيمي: `00_STUDIO_HUB/CURRICULUM_MAP.md`.
