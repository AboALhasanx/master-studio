# موارد مؤلف الكتاب الأساسي — Jiawei Han + أسلوب الأسئلة الرسمي

> **التاريخ:** 2026-10-06 · **المادة:** Data Mining (CS602) — أ.د. أحمد شاكر · **المصدر الأساسي:** Han, Kamber & Pei, *Data Mining: Concepts and Techniques*, Morgan Kaufmann.
> **الغرض:** التعرّف على مؤلف الكتاب الأساسي، والوصول لموارده التعليمية الرسمية، واستخراج **أسلوب الأسئلة** الحقيقي من مقرره.

---

## 1. المؤلف — Jiawei Han (韩家炜)

- **أستاذ** في **University of Illinois Urbana-Champaign (UIUC)**، قسم علوم الحاسوب (Siebel School).
- **مؤلف** الكتاب المرجعي عالمياً *Data Mining: Concepts and Techniques* (مع Micheline Kamber و Jian Pei).
- **موقعه الرسمي:** `https://hanj.cs.illinois.edu/` — يدرّس **CS412** (مقدمة) و **CS512** (متقدم).
- **الكتاب الآن في طبعته الرابعة (2023)** — Han, Pei & Tong، Morgan Kaufmann، **ISBN 978-0-12-811760-6**.

---

## 2. الموارد الرسمية المجانية (كنز)

| المورد | الرابط | المحتوى |
|:---|:---|:---|
| **شرائح 4th ed (2023)** ⭐ | `hanj.cs.illinois.edu/bk4/bk4_slidesindex.htm` | **12 فصل** كامل بصيغة `.pptx` — مجانية |
| **شرائح 3rd ed (2011)** | `hanj.cs.illinois.edu/bk3/bk3_slidesindex.htm` | **13 فصل** بصيغة `.ppt` — تطابق نسختك |
| **امتحان Midterm نموذجي** ⭐⭐ | `hanj.cs.illinois.edu/cs412/exams/sample_midterm.pdf` | 3 صفحات، 100 علامة |
| **امتحان Final نموذجي** ⭐⭐ | `hanj.cs.illinois.edu/cs412/exams/00sample.pdf` | 14 صفحة، 100 علامة |
| **مقرر CS412** | `hanj.cs.illinois.edu/cs412/` | المقرر الرسمي المبني على الكتاب |
| **كتاب الحلول** | studylib.net / docsity (3rd & 4th ed) | حلول تمارين الكتاب |

**⚠️ ملاحظة:** نسختك المحلية هي **3rd ed (2011)**. الطبعة **4th ed (2023)** أحدث بـ12 سنة، وبعض ترقيم الفصول تغيّر (مثلاً: 3rd Ch.3 = Data Preprocessing منفصل؛ 4th Ch.2 = Data + Preprocessing مدمجين).

---

## 3. 🎯 أسلوب الأسئلة الرسمي (من امتحانات Han نفسه)

### امتحان Midterm (90 دقيقة، 100 علامة)

| السؤال | العلامات | الموضوع |
|:---|:---:|:---|
| Q1 | **[35]** | Data and data preprocessing |
| Q2 | **[17]** | Data Warehousing and OLAP |
| Q3 | **[22]** | Data cube technology |
| Q4 | **[23]** | Frequent pattern and association mining |
| Q5 | [3] | Opinion (تقييم الطالب للامتحان) |

**أمثلة حرفية على صيغة الأسئلة:**
- «**Name** four methods that perform effective **dimensionality reduction** and four methods that perform effective **numerosity reduction**.» → سؤال **تعداد**.
- «**What are the value ranges** of: χ² · Jaccard coefficient · covariance?» → سؤال **قيم/مدى**.
- «**Calculate** its mean and variance. **Normalize** ... by min-max ... In **z-score** normalization, what value should 100 be transformed to?» → سؤال **حساب**.
- «**Explain** the major differences among the three measures, and **give one example** for each case.» → سؤال **مقارنة + مثال**.
- «Given an **FP-tree** (Fig. 1) with min_sup=0.5, min_conf=0.8: **show** c's conditional database, all frequent k-itemsets, two strong association rules.» → سؤال **تتبّع**.
- «**Outline the design** of a cube structure to support such a search engine.» → سؤال **تصميم**.

### امتحان Final (180 دقيقة، 100 علامة)

| السؤال | العلامات | الموضوع |
|:---|:---:|:---|
| Q1 | **[14]** | Data preprocessing (χ² · Pearson · Kulczynski) |
| Q2 | **[14]** | Data Warehousing, OLAP & Cube Computation |
| Q3 | **[12]** | Frequent pattern and association mining |
| Q4 | **[34]** | Classification and Prediction |
| Q5 | **[26]** | Clustering |

### ✅ البصمة المميزة لأسلوب Han

1. **أسئلة مرقّمة بتوزيع علامات صريح** `[35]`, `[17]`… — كل سؤال له وزن واضح.
2. **تقسيم متعدد (a, b, c, d, e)** — كل جزء صغير ومستقل.
3. **إجابات قصيرة (brief answers)** — مو مقالات.
4. **خمسة أنواع متكررة:**
   - **تعداد** (Name four methods…)
   - **حساب** (Calculate mean/variance · normalize · z-score)
   - **مقارنة/فرق** (Explain the differences…)
   - **تتبّع** (Given an FP-tree, show…)
   - **تصميم/رأي** (Outline the design… · Opinion)
5. **أسئلة «أيها أفضل/أسوأ»** (list one method which is the best and another which is the worst).
6. **أسئلة تربط النظرية بالواقع** (WalMart data cube · Sears chain store · web search engine).

**⇒ هذه هي البصمة اللي تشبه أسلوب د. أحمد المتوقّع (من ملفه: normalization، χ²، Apriori traces).**

---

## 4. شنو نزّلنا محلياً

`02_Raw_Materials/_han_resources/` (محلي، متجاهَل بالـgit):
- `Han_CS412_sample_midterm.pdf` + `Han_CS412_sample_final.pdf` — **الامتحانان الرسميان**.
- `slides_4th_ed/` — **12 فصل** شرائح رسمية (2023).
- `slides_3rd_ed/` — **13 فصل** شرائح رسمية (2011) — تطابق نسختك.

---

## 5. توصيات عملية

1. **اقرأ الامتحانين النموذجيين أولاً** — يعطونك البصمة الكاملة لأسلوب الأسئلة.
2. **الشرائح الرسمية = مرجع سريع** لكل فصل (مطابقة للكتاب).
3. **عند الحساب:** اكتب الصيغة أولاً، ثم الخطوات، ثم القيمة النهائية (زي ما نصح ملف الطبيب).
4. **راجع القيم/المدى:** χ² ∈ [0, ∞)، Jaccard ∈ [0,1]، Pearson ∈ [−1,1] — نوع سؤال متكرر عند Han.

---

## 6. موارد الطلاب والمجتمع (مو الموقع الرسمي)

### 🎯 بنوك امتحانات جامعية مع حلول
| المورد | الرابط | المحتوى |
|:---|:---|:---|
| **Fordham — Practice Final + Solutions** ⭐ | `storm.cis.fordham.edu/~gweiss/classes/cisc4631/` | امتحان نهائي + حلول كاملة (نزّلناه) |
| **Leiden — Example Questions** | `datamining.liacs.nl/DM2014etc/example.pdf` | أسئلة نموذجية |
| **Studylib — Practice Final** | `studylib.net/doc/25668371/` | امتحان تدريبي بحلول |
| **KnowledgeGate — Solved MCQs** | `knowledgegate.ai/blog/data-mining-techniques-mcqs-solved-questions` | 12 MCQ بحلول |
| **Stuvia — Test Bank** | `stuvia.com` (2nd ed) | بنك أسئلة الكتاب |

### 📄 ملخصات (Cheat Sheets) — نزّلناها كلها
| المورد | الوصف |
|:---|:---|
| **Stanford CS145 Midterm Cheat Sheet** (4ص) | ملخص مكثّف — كل الخوارزميات |
| **Data Mining Algorithms — summary** (24ص) | ملخص شامل: DW · classification · clustering · patterns |
| **Kaggle Data Mining Cheat Sheet** (6ص) | ملخص سريع |

### 🎥 كورسات فيديو كاملة (مجانية)
| المورد | الرابط |
|:---|:---|
| **NPTEL — Data Mining (IIT Kharagpur)** ⭐ | `nptel.ac.in/courses/106105174` (+ على YouTube) |
| **KDDmUe — KDD with Exercises** | `fau-cs6.github.io/KDD/` (محاضرات + **تمارين**) |

### 💻 مستودعات GitHub
| المورد | الرابط | المحتوى |
|:---|:---|:---|
| **sclfnc/dm-notes** | `github.com/sclfnc/dm-notes` | ملاحظات محاضرات MSc (2024/25) |
| **chatox/data-mining-course** | `github.com/chatox/data-mining-course` | مقرر 12 أسبوع كامل |
| **aditisingh2912/Data-Mining** | `github.com/aditisingh2912/Data-Mining` | تنفيذ Apriori · FP-Growth · Naive Bayes |
| **Jimachin/Data-Mining-Concepts-and-Techniques** | `github.com/Jimachin/...` | مواد الكتاب |
| **anassbelcaid/datamining** | `anassbelcaid.github.io/datamining/lectures/` | محاضرات Fall 2024 |

---

## 7. الملخص النهائي — شنو نزّلنا (محدّث، متحقَّق منه)

```
_han_resources/
├── Han_CS412_sample_midterm.pdf        ← امتحان Han الرسمي
├── Han_CS412_sample_final.pdf          ← امتحان Han الرسمي
├── slides_4th_ed/   (12 ملف .pptx)     ← شرائح 2023
├── slides_3rd_ed/   (13 ملف .ppt)      ← شرائح 2011
└── community_resources/
    ├── Fordham_practice_final.pdf + _solutions.pdf
    ├── CheatSheet_Stanford_CS145.pdf
    ├── CheatSheet_DataMining_Algorithms_summary.pdf
    └── CheatSheet_Kaggle_DataMining.pdf
```

---

*فُحص بـ: بحث ويب، فتح صفحات المقرر الرسمية، وتنزيل + قراءة + التحقق من كل ملف. كل الروابط رسمية أو مجانية.*
