# تقرير جنائي — من وين جاءت مادة الـData Mining؟ (AI أم مصدر حقيقي؟)

> **التاريخ:** 2026-10-06 · **المادة:** Data Mining (CS602) — أ.د. أحمد شاكر عبد الرضا · **المكان:** `01_Semester_1/03_Data_Mining/`
> **السؤال:** هل مادة الـDM **مولّدة بالـAI** (بس ملخّص لمادة صحيحة)، أم لها أصل حقيقي؟
> **الجواب:** **مخلوطة** — **الملفات المكتوبة بخط اليد حقيقية ١٠٠٪**، بس **الملازم المطبوعة (DOCX) مولّدة بالـAI** (تلخيص صحيح للمصادر).

---

## 1. الحكم السريع

| المجموعة | الحكم |
|:---|:---|
| **الملفات المكتوبة بخط اليد** (8 ملفات PDF) | 🟩 **حقيقية ١٠٠٪** — خط يد بشري (مسح CamScanner) |
| **ملازم DOCX** (W02 · W03 · W04 · W05) | 🟥 **مولّدة بالـAI** (تلخيص صحيح) |
| **عرض Week 01 (PPTX)** | 🟡 بشري (2022) — محتوى عام/تعليمي |

---

## 2. الدليل — المجموعة الأولى: المكتوب بخط اليد (حقيقي)

- `DM_Handwritten_Clustering_KMeans / Hierarchical / DBSCAN` · `DM_Handwritten_Data_Preprocessing_Part1–3` · `DM_Handwritten_Data_in_ML` · `DM_Handwritten_Intro_to_ML`.
- **منتجها `Skia/PDF m128`** (طباعة من Chrome) و**بلا طبقة نصية** (0 حرف).
- عند رسم الصفحات: **خط يد حقيقي** — ورقة مسطّرة، كتابة حمراء/سوداء، **ختم CamScanner**. مثال: «Centroid-based Clustering (Partitioning method K-Mean)».
- **⇒ مادة بشرية حقيقية**، مو مولّدة.

## 3. الدليل — المجموعة الثانية: ملازم DOCX (مولّدة بالـAI)

| الملف | `creator` | وقت التحرير | كلمات | صفحات |
|:---|:---|:---:|:---:|:---:|
| `Week 02 - Basic Data Types (v2).docx` | PC-CIT | 8 د | 2664 | 20 |
| `Week 03 - Feature Extraction.docx` | **`python-docx`** | 23 د | 1617 | 13 |
| `Week4_Feature_Selection.docx` | PC-CIT | 54 د | 2258 | 17 |
| `Week5.docx` | PC-CIT | **3 د** | **3802** | 26 |

**بصمة الـAI (خمس إشارات):**
1. **`creator = python-docx`** (W03) → الملف **مولّد برمجياً** (سكربت/أداة)، مو مكتوب بيد.
2. **3802 كلمة بـ3 دقائق** (W05) — مستحيل كتابةً يدوية → نص ملصوق/مولّد.
3. **عناوين بأسلوب أسئلة (AI/SEO):** «**Why Do We Need Data Type Portability?**»، «**Why Not Simply Use A = 1, B = 2, O = 3?**»، «Why Do We Need Feature Extraction?».
4. **صفر مراجع** بكل الملفات الأربعة (لا `[n]`، لا قسم References، لا DOI).
5. **ما يطابق أي مصدر حرفياً** بالبحث (خلافاً للحوسبة اللي طابقت TutorialsPoint) → **صياغة/تلخيص**، مو نسخ.

**والمحتوى صحيح فعلاً** (هذا اللي خمّنته):
- `Week5.docx` بنيته: Association Pattern Mining → Frequent Itemset → Brute Force → **Apriori** → **FP-Growth** → Enumeration-Tree → Recursive Suffix-Based = **فصل 4 من Aggarwal**.
- `Week4` = Filter/Wrapper/Embedded = **Han & Kamber §3.4.4** (Attribute Subset Selection).

**⇒ يعني: نص صحيح، لكن مكتوب بـLLM ثم لُصق في Word.** — بالضبط فرضيتك.

## 4. الدليل — المجموعة الثالثة: عرض Week 01

- `creator = Ah-PC`، تاريخ الإنشاء **2022-08-26**، `TotalTime = 609` دقيقة، 25 سلايد.
- المحتوى: «What Is Data Mining? / Advantages / Disadvantages / Applications (Healthcare · Market Basket · Education · Manufacturing · CRM)» — قائمة تطبيقات عامة.
- **ما طابق أي مصدر حرفياً** — محتوى عام/تعليمي. الحكم: **بشري**، بس عام.

---

## 5. المقارنة بين المواد الثلاث

| المادة | الطبيعة | الدليل الحاسم |
|:---|:---|:---|
| 🟥 **الأمن السيبراني** | **مولّد بالـAI (~94%)** | هيكل LLM + معادلات ملفّقة + صفر مراجع |
| 🟩 **الحوسبة الناعمة** | **منسوخ من مصادر حقيقية** | TutorialsPoint حرفياً + مراجع Haykin/Sivanandam |
| 🟨 **Data Mining** | **مخلوط: خط يد حقيقي + ملازم AI** | خط يد CamScanner + `python-docx` وعناوين أسئلة |

**الخلاصة:** ثلاث مواد، ثلاث مشاكل مختلفة. الـDM نصّه **صحيح لكنه تلخيص AI** — فرضيتك **صحيحة**.

---

## 6. توصيات عملية

1. **الملفات المكتوبة بخط اليد = كنزك الحقيقي** — هي الأصل البشري. اعتمد عليها كمرجع.
2. **الملازم DOCX = مفيدة للمحتوى، بس:** لا تعتمد عليها كمرجع نهائي — ارجع لـ**Han & Kamber** و**Aggarwal** (الموجودين عندك بالـ`02_Raw_Materials`).
3. **قاعدة عامة:** إذا احتجت دقة بمادة DM — اذهب للكتاب الأصلي.

---

## 7. ✅ التحقق المصدرى — المحتوى **من الكتاب (المنهج)**، مو مُختَرَع

**الدليل القاطع:** عناوين `Week5.docx` تطابق **فصل 4 §4.4 من Aggarwal** حرفياً، عنواناً بعنوان:

| عنوان الملزمة (Week5.docx) | Aggarwal Ch.4 §4.4 |
|:---|:---|
| Brute Force Algorithm | **§4.4.1 Brute Force Algorithms** |
| Apriori Algorithm | **§4.4.2 The Apriori Algorithm** |
| Enumeration-Tree Algorithms | **§4.4.3 Enumeration-Tree Algorithms** |
| Recursive Suffix-Based Pattern Growth Methods | **§4.4.4 Recursive Suffix-Based Pattern Growth Methods** |
| The FP-Growth Algorithm | §4.4.4 (FP-Tree implementation) |

**⇒ الملزمة = تلخيص أمين للكتاب، مو محتوى ملفّق.**

### خريطة كل ملزمة لمصدرها

| الملزمة | المصدر |
|:---|:---|
| `Week 02 - Basic Data Types` | **Han & Kamber §2.1** (Attribute Types: nominal · binary · ordinal · interval/ratio · discrete/continuous) |
| `Week 03 - Feature Extraction` | **Han & Kamber §3.4** (Data Reduction / Feature Extraction) |
| `Week4_Feature_Selection` | **Han & Kamber §3.4.4** + **Aggarwal §2.4 / §6.2 / §10.2** (filter/wrapper/embedded) |
| `Week5` | **Aggarwal Ch.4 §4.4** (Association Pattern Mining — تطابق حرفي) |

### ✅ لا أخطاء واقعية
راجعت: أنواع السمات (W02)، استخراج/اختيار السمات (W03/W04)، خاصية Apriori (الانغلاق التنازلي) و FP-Growth (W05) — **كلها صحيحة ومطابقة للكتابين**.

**⇒ الفرق الجوهري عن الأمن السيبراني:** هناك المحتوى **مُختَرَع** (معادلات ملفّقة بلا مصدر)؛ هنا المحتوى **تلخيص أمين لمصدر حقيقي**. **المادة موثوقة.**

---

*فُحص بـ: بيانات وصفية (zipfile core.xml/app.xml + PyMuPDF)، تحليل بنيوي آلي، فحص بصمات AI، رسم الصفحات بصرياً، مقارنة عناوين مع الكتبين صفحة-بصفحة، وبحث ويب للعبارات المميزة. كل الأدلة قابلة للتكرار.*
**⚠️ تنبيه أداة:** البحث بمقارنة نص الكتاب كامل بنص واحد (`' '.join`) **يرجع صفر نتائج زوراً** — لازم البحث **صفحة بصفحة**.
