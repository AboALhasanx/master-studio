# Data Mining — Week 02: COMPREHENSIVE Notes
## Data Types & Data Preparation — أنواع البيانات وإعدادها كامل

> **Instructor:** Asst. Prof. Dr. Ahmed Shakir Abd Al-Rida
> **Course:** `03_Data_Mining` (CS602) — 2 Credit Hours
> **Sources:**
> 1. `Week 02 - Basic Data Types in Data Mining (v2).docx` — lecture core (attributes, structures, full data preparation)
> 2. `Week 02 - Data Types - Arabic Line-by-Line Translation.docx` — official bilingual walkthrough
> 3. `Week 02 - Basic Data Types in Data Mining and ML.docx` — extended ML framing (nondependency/dependency + portability)
> 4. Han, Kamber & Pei — *Data Mining: Concepts and Techniques* (textbook expansion, clearly labeled)
> 5. Gemini Smart Memorisation Framework method (same templates used on Week 01)
>
> **Purpose of this file:** a single, complete, exam-ready reference. You should not need to reopen the weird-format DOCX files for review. Original lecture text is preserved; Gemini-style frameworks are built **on top of it**, never instead of it.
>
> **Standing answer recorded:** Dr. Ahmed's Week 02 question — *data type of a URL* → **Nominal**.

---

## المحتويات

| # | القسم | المصدر |
|:--:|:---|:---|
| 0 | [Data Object vs Attribute](#0) | المحاضرة |
| 1 | [Attribute Taxonomy — الأنواع الأربعة](#1) | المحاضرة + قالب القرار + Han expansion |
| 2 | [Numerical Deep Split — Discrete / Continuous / Interval / Ratio](#2) | المحاضرة + Doctor/Textbook layer |
| 3 | [The 8 Data Structures](#3) | المحاضرة + 2-Keyword Matrix |
| 4 | [Data Preparation — Pipeline والخطوات الخمس](#4) | المحاضرة + 3-Element Formula |
| 5 | [Data Cleaning بالتفصيل](#5) | المحاضرة (Missing 6 methods + Noise + Outliers + Duplicates + Inconsistency) |
| 6 | [Integration · Transformation · Reduction · Discretization](#6) | المحاضرة + صيغ د. أحمد |
| 7 | [Feature Selection vs Feature Extraction](#7) | المحاضرة + تمييز امتحاني |
| 8 | [Medical Dataset Walkthrough](#8) | المحاضرة |
| 9 | [Preparation vs Preprocessing](#9) | المحاضرة |
| 10 | [Gemini Anchors & Safe Answers](#10) | أسلوب الحفظ |
| 11 | [Exam Quick Table](#11) | مُجمّع |
| 12 | [Question Bank](#12) | مُستخرج من الكل |

---

<a name="0"></a>
# 0. Data Object vs Attribute

## 0.1 Definitions (نص المحاضرة)

**Data Object**
> *"A data object represents an **entity about which information is collected**."*

Examples from the lecture:
- Patient · Student · Customer
- Transaction · Document · Image · Geographic location

**Attribute**
> *"An attribute is a **property or characteristic** of a data object."*

Examples from the lecture:
- Age · Gender · BMI · Blood pressure · Diabetes status

## 0.2 The Table Mental Model

| Patient | Age | Gender | BMI | Diabetes |
|:---|:---:|:---:|:---:|:---:|
| P1 | 45 | Male | 28.5 | Yes |
| P2 | 32 | Female | 24.1 | No |

- **Each ROW** = one **data object** (one patient)
- **Each COLUMN** = one **attribute** (a property collected about every object)

> **قاعدة سريعة:** Object = **who/what we study**. Attribute = **what we measure/record about it**.

## 0.3 Why this matters before mining (نص المحاضرة)

Before applying a data-mining technique, understand:
1. What the **data objects** are
2. What the **attributes** are
3. What **type of values** the attributes contain
4. How the data is **organized / structured**

> *"The type and structure of data **influence which data-mining technique** should be used."*

**مرساة:** `Object → Attribute → Value Type → Structure → Technique`

---

<a name="1"></a>
# 1. Attribute Taxonomy — Basic Types of Attributes

> **المصدر:** المحاضرة §3 (3.1–3.4) + قالب القرار + طبقة Han & Kamber (معلَّمة)

## 1.1 The Four Lecture Types — Original Text

### 1.1.1 Nominal Attributes

> *"A nominal attribute contains **categories with no natural order**."*

Lecture examples:
- Gender: Male, Female
- Color: Red, Blue, Green
- Country: Iraq, Jordan, Egypt
- Department: CS, IT, Mathematics

> *"There is **no meaningful ranking** between the categories."*
> *"Male > Female **does not make sense**."*

### 1.1.2 Ordinal Attributes

> *"An ordinal attribute contains categories with a **meaningful order**, but the **difference between categories is not necessarily measurable**."*

Lecture examples:
- Low, Medium, High
- Poor, Good, Excellent
- Small, Medium, Large
- Disease severity: Mild, Moderate, Severe

> *"Low < Medium < High — the order is meaningful, but we cannot say that the difference between Low and Medium is exactly the same as the difference between Medium and High."*

### 1.1.3 Binary Attributes

> *"A binary attribute has **only two possible values**."*

Lecture examples:
- Yes / No
- True / False
- 0 / 1
- Disease / No Disease
- Purchased / Not Purchased

Example table:

| Patient | Diabetes |
|:---|:---:|
| P1 | 1 |
| P2 | 0 |

> *"Binary attributes are very common in **classification and association analysis**."*

### 1.1.4 Numerical Attributes

> *"Numerical attributes contain **quantitative numerical values**."*

Lecture examples:
- Age · Height · Weight · Temperature · Salary · Blood pressure

Split by the lecture into:
- **Discrete:** countable — number of children / transactions / students / visits (`0, 1, 2, 3, ...`)
- **Continuous:** many values in a range — Height `175.5 cm` · Weight `72.4 kg` · Temperature `36.7°C` · Blood glucose `125.6 mg/dL`

---

## 1.2 Gemini Framework — Decision Template (قالب القرار)

بدال ما تحفظ أربع فقرات سردية، مرّ كل متغير بثلاثة أسئلة:

| Decision Question | Nominal | Ordinal | Binary | Numerical |
|:---|:---:|:---:|:---:|:---:|
| Is there a **natural order** between categories? | No | Yes | — | — |
| Is the **gap between values measurable**? | — | **Not necessarily** | — | Yes |
| Are there **only two values**? | No | No | Yes | No |
| Is the value a **quantity** (count/measure)? | No | No | No | Yes |

### Classification Algorithm (خطوات التصنيف)

```
1. Only two possible values?
   YES → Binary
   NO  → continue
2. Quantitative numbers (count or measure)?
   YES → Numerical (then: Discrete vs Continuous; optionally Interval vs Ratio)
   NO  → continue
3. Categories with meaningful ranking?
   YES → Ordinal   (order yes, gap unknown)
   NO  → Nominal   (labels only, no order)
```

### Mental Anchor (مرساة الأنواع)

> `No order → Order, unknown gap → Two values → Quantity`
>
> بالعربي: **اسمي بلا ترتيب** → **ترتيب بلا قياس** → **صفر/واحد** → **عدد**

### Quick-Check Examples

| Variable | Decision Path | Type |
|:---|:---|:---|
| Gender {Male, Female} | No order, not numeric | **Nominal** |
| Country / Department / Color | Labels only | **Nominal** |
| **URL** (web address string) | Categories/labels, no natural order | **Nominal** |
| Satisfaction {Poor, Good, Excellent} | Order yes, gaps unknown | **Ordinal** |
| Disease severity {Mild, Moderate, Severe} | Order yes, gaps unknown | **Ordinal** |
| Diabetes {Yes/No} or {0/1} | Exactly two values | **Binary** |
| Purchased / Not Purchased | Two values | **Binary** |
| Age = 45 | Quantity, countable years | **Numerical (Discrete-ish / integer)** |
| Height = 175.5 cm | Continuous measure | **Numerical (Continuous)** |
| Number of children = 0,1,2… | Countable | **Numerical (Discrete)** |
| Salary / Blood pressure | Quantitative measure | **Numerical** |

### 🔴 Dr. Ahmed Standing Question — URL

**السؤال:** *What is the data type of a URL?*

**الجواب:** **Nominal attribute.**

**التعليل (بالعربي):** الرابط مثل `https://example.com/page` هو **وسم/فئة (label)** يعرّف موقعاً أو مورداً. ما بينه وبين رابط ثاني **ترتيب طبيعي** (`url1 > url2` ما له معنى)، وما بينه وبين غيره **فجوة قابلة للقياس**. لذلك يصنّف في تصنيف الدكتور تحت **Nominal**.

> Safe exam sentence: *"A URL is a Nominal attribute: categories/identifiers with **no natural order** and **no meaningful distance** between values."*

---

<a name="2"></a>
# 2. Numerical Deep Split — Discrete / Continuous + Interval / Ratio

## 2.1 From the Lecture

| Subtype | Meaning | Lecture Examples |
|:---|:---|:---|
| **Discrete** | Values are generally **countable** | Number of children, transactions, students, visits → `0,1,2,3,...` |
| **Continuous** | Values can take **many values within a range** | Height 175.5 · Weight 72.4 · Temp 36.7°C · Glucose 125.6 |

## 2.2 Textbook / Doctor Expansion — Interval vs Ratio

> **[Foundational Knowledge / Han & Kamber + Doctor Profile]**
> هذا الجزء مو مفصول بنفس الصيغة بملف المحاضرة v2، لكنه **أساسي لامتحان د. أحمد** ومسجل بـ `00_Doctor_Profile.md`.

| Subtype | Zero means | Distance ratios meaningful? | Examples |
|:---|:---|:---|:---|
| **Interval-scaled** | **Arbitrary** reference point — لا يوجد “عدم وجود” حقيقي | No — 20°C is **not** “twice as hot” as 10°C | Celsius temperature, calendar years |
| **Ratio-scaled** | **Absolute physical zero** — يعني عدم وجود الخاصية | Yes — 20kg **is** twice 10kg | Kelvin, salary, weight, height, blood pressure |

### Doctor Exam Rule (من بروفايل الدكتور)

1. Write the **symbolic formula first**
2. Define every symbol
3. Show intermediate arithmetic
4. State final value **and** the range (`[0,1]` vs `[-1,1]`)

### Formulas You Must Know Cold (د. أحمد — Manual Calculations)

**Min-Max Normalization**

$$
v' = \frac{v - \min_A}{\max_A - \min_A}\,(new\_max_A - new\_min_A) + new\_min_A
$$

Simple form into $[0,1]$ (lecture worked example):

$$
x' = \frac{x - \min}{\max - \min}
$$

**Lecture example:**
- min age = 20, max age = 60, age = 40
- $x' = (40-20)/(60-20) = 20/40 = 0.5$
- **40 years → 0.5**

**Z-Score (standard deviation)**

$$
v' = \frac{v - \bar{A}}{\sigma_A}
$$

**Z-Score with Mean Absolute Deviation**

$$
v' = \frac{v - \bar{A}}{s_A}, \quad s_A = \frac{1}{n}\sum_{i=1}^{n}|x_i - \bar{A}|
$$

**Decimal Scaling**

$$
v' = \frac{v}{10^j}
$$
where $j$ is the smallest integer such that $\max(|v'|) < 1$.

### Arithmetic Discipline (نفس درس Cyber — لا تتكرر الغلطة)

- Always divide by the **correct count** (missing-value mean example: 4 values present → divide by 4, not 5)
- Write the formula **before** numbers
- State the output range explicitly

**مرساة Interval vs Ratio:**
> `Interval: zero is a ruler mark · Ratio: zero is nothing left`
>
> مئوية = علامة على المسطرة · كلفن/راتب/وزن = صفر يعني “ماكو”

---

<a name="3"></a>
# 3. The 8 Basic Data Structures

> **المصدر:** المحاضرة §4 + القاعدة الفاصلة §5 + Gemini 2-Keyword Matrix

## 3.1 The Hard Separation (احفظها — سؤال تمييز)

> **نص المحاضرة (Summary):**
> *"It is useful to distinguish between **attribute types** and **data structures**:*
> - *Nominal, ordinal, binary, and numerical describe **attributes**.*
> - *Record, transaction, text, sequence, temporal, spatial, image, and graph data describe **how the data is organized or represented**."*

| Layer | Question it answers | Members |
|:---|:---|:---|
| **Attribute types** | What kind of **value** is this column? | Nominal · Ordinal · Binary · Numerical |
| **Data structures** | How is the **whole dataset shaped**? | Record · Transaction · Text · Sequence · Temporal · Spatial · Image · Graph |

---

## 3.2 Master Matrix — 2-Keyword Rule (احفظ الجدول، مو النصوص)

| # | Structure | Core Form | Canonical Example | What Mining Discovers | Mining Family |
|:--:|:---|:---|:---|:---|:---|
| 1 | **Record** | Collection of records; each record = set of attributes | Patient/Student table | classification, clustering, regression, outliers | General DM |
| 2 | **Transaction** | Each transaction = **set of items** | T1={Bread,Milk,Eggs} | Association rules `Bread → Milk` | Association mining |
| 3 | **Text / Document** | Unstructured documents | Emails, reviews, papers, posts | frequent words, topics, sentiment, similarity, text classification | **Text Mining** |
| 4 | **Sequence** | Elements in a **specific order** | `Login → Search → Product → Purchase` | ordered patterns | Sequence mining |
| 5 | **Temporal / Time-Series** | Observations tied to **time** | Stock prices, weather, ECG | trends, seasonal/periodic patterns, anomalies | Temporal mining |
| 6 | **Spatial** | Objects with **geographic/physical location** | GPS `(32.48°, 45.82°)` | location-based relationships | Spatial DM |
| 7 | **Image / Multimedia** | Pixels: Gray `H×W`, RGB `H×W×3` | X-ray, MRI, CT, satellite | objects, shapes, patterns, textures, regions | Image mining (CNN etc.) |
| 8 | **Graph / Network** | **Nodes** (objects) + **Edges** (relationships) | Social/citation/road nets | communities, important nodes, relationships, structures, paths | Graph mining |

**🧠 Structure Anchor:**
> `Row → Basket → Document → Path → Clock → Map → Picture → Network`
>
> بالعربي: **صف** → **سلة** → **مستند** → **مسار** → **ساعة** → **خريطة** → **صورة** → **شبكة**

**🛡️ Safe answer sentence (ثابتة):**
> *"The dataset is organized as [structure]. Data mining techniques are selected according to this structure — for example association rules for transactions, text mining for documents, or graph mining for networks."*

---

## 3.3 Structures One-by-One — Original + Arabic + Keywords

### 3.3.1 Record Data

**EN (lecture):**
> *"Record data consists of a collection of records, where each record contains a set of attributes."*

**Example table:**

| Student | Age | GPA | Department |
|:---|:---:|:---:|:---|
| S1 | 20 | 3.1 | CS |
| S2 | 22 | 3.6 | IT |
| S3 | 21 | 2.9 | CS |

**Applications listed:** Classification · Clustering · Regression · Outlier detection

**AR:** بيانات السجلات = مجموعة سجلات، كل سجل يحوي مجموعة خصائص (صف = كائن).

**Keywords:** `Attribute table` + `Classification / Clustering`

---

### 3.3.2 Transaction Data

**EN:**
> *"Each transaction contains a set of items."*
> Example: Transaction 1 = `{Bread, Milk, Eggs}`; T2 = `{Bread, Butter}`; T3 = `{Milk, Eggs, Juice}`
> *"Commonly used in **Association Rule Mining**."*
> Example rule: **Bread → Milk** — customers who buy bread often buy milk.

**AR:** كل معاملة = **مجموعة عناصر** (مو صف خصائص عادية). الاستخدام المركزي: قواعد الارتباط.

**Keywords:** `Set of items` + `Association rules`

---

### 3.3.3 Text and Document Data

**EN:**
> Includes documents, emails, news, research papers, customer reviews, social media posts.
> Example: *"This product is excellent and easy to use."*
> Mining can identify: frequent words · topics · sentiment · document similarity · text classification.
> *"This area is commonly called **Text Mining**."*

**AR:** نصوص غير مهيكلة → نستخرج منها كلمات/مواضيع/مشاعر/تشابه/تصنيف.

**Keywords:** `Unstructured text` + `Text Mining`

---

### 3.3.4 Sequence Data

**EN:**
> *"Sequence data contains elements in a **specific order**."*
> Example: `A → B → C → D`
> Includes: DNA sequences · customer purchasing sequences · web click sequences · user activity sequences.
> *"The **order is important**."*
> `Login → Search → Product → Purchase` may represent browsing behavior.

**AR:** الترتيب **ليس اختيارياً** — هو جزء من المعلومة نفسها.

**Keywords:** `Ordered elements` + `Order matters`

---

### 3.3.5 Time-Series / Temporal Data

**EN:**
> *"Temporal data contains observations associated with **time**."*

| Month | Temperature |
|:---|:---:|
| January | 12°C |
| February | 15°C |
| March | 19°C |

> Examples: stock prices · weather · rainfall · electricity consumption · patient monitoring · sensor measurements.
> Mining can discover: **Trends · Seasonal patterns · Periodic patterns · Anomalies**

**AR:** كل ملاحظة مقرونة بختم زمني.

**Keywords:** `Time-linked` + `Trends / seasonality / anomalies`

---

### 3.3.6 Spatial Data

**EN:**
> *"Spatial data represents objects or observations associated with **geographic or physical locations**."*
> Examples: maps · satellite images · GPS coordinates · roads · population distributions · environmental measurements.
> Example: Location A → `(32.48°, 45.82°)`
> *"Spatial Data Mining can discover **relationships between objects based on their locations**."*

**AR:** الكائن له إحداثيات/مكان؛ العلاقات تُقرأ جغرافياً.

**Keywords:** `Location-linked` + `Spatial relationships`

---

### 3.3.7 Image and Multimedia Data

**EN:**
> *"Image data contains information represented as **pixels**."*
> Grayscale: `Height × Width` (2D matrix)
> Color RGB: `Height × Width × 3`
> Examples: X-ray · MRI · CT · satellite · facial · histopathology images.
> Image mining can identify: objects · shapes · patterns · textures · regions.
> *"Common methods include **CNNs** and other deep-learning models."*

**AR:** الصورة = مصفوفة بكسلات؛ التنقيب يقرأ أشكال/أنسجة/مناطق.

**Keywords:** `Pixel matrix` + `CNN / textures / regions`

---

### 3.3.8 Graph and Network Data

**EN:**
> *"Graph data represents **relationships between objects**."*
> A graph consists mainly of:
> - **Nodes (vertices)** → objects
> - **Edges** → relationships
>
> Example: Student A → Student B could represent friendship.
> Examples: social networks · computer networks · citation networks · transportation · financial networks · knowledge graphs.
> Graph mining can discover: communities · important nodes · relationships · frequent structures · paths.

**AR:** الرسم البياني = عقد + حواف. التنقيب يقرأ المجتمعات والعقد المهمة والمسارات.

**Keywords:** `Nodes + Edges` + `Communities / important nodes / paths`

---

<a name="4"></a>
# 4. Data Preparation — Pipeline والخطوات الخمس

## 4.1 Definition (نص المحاضرة)

> *"**Data Preparation** is the process of preparing **raw data** so that it can be used **effectively** by Data Mining algorithms."*

**Real-world data is often:**
- Incomplete · Noisy · Inconsistent · Duplicated
- In different formats
- Containing irrelevant attributes
- Containing different scales of numerical values

## 4.2 The Core Pipeline

```
Raw Data → Data Preparation → Data Mining → Knowledge / Patterns
```

> *"The quality of the prepared data can **strongly affect** the quality of the discovered patterns and the performance of the mining model."*

**مرساة البايبلاين الكامل (lecture order):**
```
Raw Data
  → Data Cleaning
  → Data Integration
  → Data Transformation
  → Data Reduction
  → Data Discretization
  → Prepared Data
  → Data Mining Algorithm
  → Patterns / Knowledge
```

> **ملاحظة المحاضرة المهمة:** *"These steps are **not necessarily performed in exactly the same order** for every dataset."* والترتيب ليس إجبارياً دائماً — يعتمد على البيانات ومهمة التنقيب.

## 4.3 The Five Main Steps — 3-Element Formula

| Step | Nature (شنو) | Action / Cause (شنو نسوي) | Output / Consequence (الناتج) |
|:---|:---|:---|:---|
| **1. Cleaning** | missing · noise · outliers · duplicates · inconsistencies | detect + correct/handle each problem type | trustworthy records |
| **2. Integration** | multiple sources, schemas, units | merge (e.g. on Student_ID), unify names/units | one coherent dataset |
| **3. Transformation** | incompatible scales / non-numeric labels | normalize · encode · aggregate · generalize | algorithm-ready representation |
| **4. Reduction** | too large / too many attributes | feature selection · PCA · sampling · aggregation | smaller, information-preserving data |
| **5. Discretization** | continuous values hard to use directly | convert to intervals/categories | interpretable bins/classes |

**🧠 Prep Anchor:**
> `Clean → Integrate → Transform → Reduce → Discretize`
>
> بالعربي: **نظّف → ادمج → حوّل → قلّل → صنّف فترات**

## 4.4 Lecture Teaching Point (احفظها)

> *"Data Preparation is **not simply 'removing missing values.'** It is the **complete process** of making raw data suitable for discovering useful patterns and knowledge."*

> *"Good data preparation → Better quality data → More reliable data-mining results."*

---

<a name="5"></a>
# 5. Data Cleaning بالتفصيل

> **نص المحاضرة:** *"Data Cleaning is the process of **detecting and correcting problems** in the data."*

**Common problems:** Missing values · Noisy data · Outliers · Duplicate records · Inconsistent data

---

## 5.1 Missing Values

> *"A missing value occurs when information for an attribute is **not available**."*

**Lecture table:**

| Patient | Age | Weight | Blood Pressure |
|:---|:---:|:---:|:---:|
| P1 | 45 | 72 | 120 |
| P2 | 38 | **?** | 130 |
| P3 | 51 | 80 | **?** |

> Weight for P2 and Blood Pressure for P3 are missing.
> *"Many Data Mining algorithms **cannot directly work** with missing values, or their performance may be affected."*

### The 6 Handling Methods (اسمح — امتحان د. أحمد يحب التعداد + الحساب)

| # | Method | When / Note | Worked Example from Lecture |
|:--:|:---|:---|:---|
| 1 | **Ignore the record** | OK only if **very few** records missing; else lose information | Remove row |
| 2 | **Fill manually** | Domain expert (e.g. doctor) | Expert sets value from other medical info |
| 3 | **Use the mean** | Numerical data | Values `60, 70, 80, ?, 90` → mean $=(60+70+80+90)/4=75$ → `? → 75` |
| 4 | **Use the median** | When data has **extreme values** | `60, 65, 70, 75, 200` — **200 is extreme** → median preferred over mean |
| 5 | **Use the mode** | Categorical data (most frequent) | Gender: Male, Female, Male, Male, **?** → **Male** |
| 6 | **Predict the value** | DM/ML model | Regression · Decision tree · k-NN · other predictive models |

### Mean Arithmetic Trap (لا تطيح بها)

$$
\text{mean} = \frac{\text{sum of observed values}}{\text{count of observed values}}
$$

- In `60,70,80,?,90` the **observed** count is **4**, not 5.
- $300/4 = 75$ ✓  
- If someone divides by 5 → wrong.

**مرساة الطرق الست:**
> `Ignore → Expert → Mean → Median → Mode → Predict`
>
> بالعربي: **احذف · اسأل خبير · وسّط · وسِّط (median) · منوال · تنبّأ**

---

## 5.2 Noisy Data

> *"Noise refers to **random errors or unwanted variation** in the data."*

**Lecture example:**
- Actual ages: `21, 22, 23, 24, 25`
- Dataset contains: `21, 22, **223**, 24, 25`
- **223** may be a data-entry error

**Handling approaches (lecture):**
- **Binning**
- Regression
- Clustering
- Outlier detection

### Binning (lecture)

> *"Binning divides numerical values into groups called **bins**."*

Example values: `10, 12, 13, 20, 22, 25, 30, 31`

Possible bins:
- Bin 1: 10–13
- Bin 2: 20–25
- Bin 3: 30–31

> *"Binning can help **smooth** noisy numerical data."*

**Keywords:** `Random error` + `Binning / smooth`

---

## 5.3 Outliers — Critical Exam Point

> *"An outlier is a data object whose value is **significantly different** from most other observations."*

Example: `65, 67, 68, 70, 69, **300**` → 300 is potentially an outlier.

### 🔴 The Point Students Miss

> *"However, an important point is: **An outlier is not necessarily an error.**"*
> *"For example, a patient's blood pressure may be unusually high because the patient **actually has a medical condition**."*
> *"Therefore, outliers should be **investigated before removing** them."*

**Detection methods listed:**
- Statistical methods
- Distance-based methods
- Clustering
- Visualization
- Machine Learning methods

**Safe exam line:**
> *"Outliers are investigated before removal because they may be valid extreme observations, not errors."*

**Keywords:** `Not necessarily error` + `Investigate first`

---

## 5.4 Duplicate Data

> *"Duplicate data occurs when the **same data object appears more than once**."*

| ID | Name | Age |
|:---:|:---|:---:|
| 101 | Ahmed | 45 |
| 102 | Ali | 38 |
| **101** | **Ahmed** | **45** |

> First and third records may represent the same object.

**Harms listed:**
- Increase dataset size unnecessarily
- Bias the analysis
- Affect frequency calculations
- Affect model performance

→ Therefore duplicates must be **identified and handled appropriately**.

**Keywords:** `Same object twice` + `Bias / frequency / performance`

---

## 5.5 Inconsistent Data

> Data can contain inconsistencies — same categories, **different formats**.

| Student | Gender |
|:---|:---|
| S1 | Male |
| S2 | M |
| S3 | male |
| S4 | Female |

**Standardize to:** `Male` · `Female`

Similarly: `Iraq, IRAQ, iraq` → **`Iraq`**

**Keywords:** `Format mismatch` + `Standardize`

---

<a name="6"></a>
# 6. Integration · Transformation · Reduction · Discretization

---

## 6.1 Data Integration

> *"Data Integration **combines data from multiple sources** into a single dataset."*

**University example:**
- Database 1 — Student information: ID | Name | Department
- Database 2 — Student grades: Student_ID | GPA
- Integrated **using the student ID**

**Problems in integration (lecture list):**
1. Different attribute names
2. Different data formats
3. Duplicate records
4. Different units
5. Different database schemas

**Unit example:** one DB `Weight = kg`, another `Weight = pounds` → must convert to a **consistent unit**.

**3-Element:** Sources differ → merge on key + unify schema/units → one dataset

---

## 6.2 Data Transformation

> *"Data Transformation converts data into a **suitable format** for Data Mining algorithms."*

**Common techniques (lecture):**
- Normalization
- Aggregation
- Generalization
- Encoding
- Feature construction

### Why normalize? (lecture)

Attributes can have very different ranges:

| Attribute | Range |
|:---|:---|
| Age | 0–100 |
| Salary | 300–10,000 |
| Income | 1,000–100,000 |

> *"A **large numerical range can dominate** some algorithms."*

### Min-Max — Worked Example (exam-style)

Given: min = 20, max = 60, $x = 40$, target range $[0,1]$

$$
x' = \frac{x - \min}{\max - \min} = \frac{40-20}{60-20} = \frac{20}{40} = 0.5
$$

**Result:** 40 years → **0.5**

**Doctor protocol on this calculation:**
1. Write formula symbolically
2. Substitute
3. Show intermediate `20/40`
4. State final `0.5` in $[0,1]$

### Z-Score

$$
z = \frac{x - \mu}{\sigma}
$$

where $x$ = original value, $\mu$ = mean, $\sigma$ = standard deviation.

> After transformation, data is represented **relative to its mean and standard deviation**.

### Encoding Categorical Data

> *"Many Data Mining and Machine Learning algorithms **require numerical input**."*

Simple encoding example:
- Male = 1, Female = 0

> **تحذير المحاضرة:** *"this approach should be used **carefully** because numerical codes can **incorrectly imply an order**."*

For categories like `Red, Blue, Green` → **One-hot encoding** is often more appropriate:

| Red | Blue | Green |
|:---:|:---:|:---:|
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 1 |

**3-Element Transformation:** Wrong scale/labels → normalize + encode carefully → model-ready numbers

---

## 6.3 Data Reduction

> *"Data Reduction attempts to **reduce the size or complexity** of the data while **preserving important information**."*

**Common techniques (lecture):**
- Dimensionality reduction
- Feature selection
- Sampling
- Aggregation
- Numerosity reduction

### Feature Selection example (lecture)

Dataset attributes:
`Age, Gender, BMI, Blood Pressure, Patient Name, Phone Number, Address`

If the goal is **disease prediction**, some attributes are irrelevant.

**Might retain:** `Age, Gender, BMI, Blood Pressure`  
**Might remove:** name, phone, address (no useful signal for the task)

---

## 6.4 Data Discretization

> *"Discretization converts **continuous numerical values** into **intervals or categories**."*

**Lecture example ages:** `18, 25, 32, 47, 65, 72`

| Interval | Category |
|:---|:---|
| 0–17 | Child |
| 18–35 | Young Adult |
| 36–60 | Adult |
| 61+ | Senior |

> *"Discretization can make some datasets **easier to analyze**."*

**مرساة Discretization:**
> `Continuous number → named interval/bin`

---

<a name="7"></a>
# 7. Feature Selection vs Feature Extraction

> **تمييز امتحاني متكرر — احفظه حرفياً**

| | Feature **Selection** | Feature **Extraction** |
|:---|:---|:---|
| **What it does** | **Select existing** features | **Create new** features from original ones |
| **Lecture example** | Selecting `Age` | **PCA** creating new components |
| **Also in materials** | Keep BMI, drop Phone | BMI from weight/height; embeddings; etc. |
| **Mnemonic** | **Pick** | **Build** |

**Safe exam sentence:**
> *"Feature selection chooses a subset of existing attributes; feature extraction constructs new attributes (e.g. PCA components) from the original data."*

**Why reduction matters (lecture / ML file):**
- Computational cost ↓
- Storage requirements ↓
- Model complexity ↓
- May help visualization
- Example: **100 original features → 10 principal components**

---

<a name="8"></a>
# 8. Medical Dataset Walkthrough (نص المحاضرة)

**Diabetes dataset:**

| Age | Glucose | BMI | Gender | Diabetes |
|:---:|:---:|:---:|:---|:---|
| 45 | 140 | 31.5 | Female | Yes |
| 32 | **?** | 24.2 | Male | No |
| 51 | 180 | 35.1 | Female | Yes |
| 29 | 110 | 22.8 | Male | No |

**Before classification, the lecture steps are:**

| Step | Action |
|:--:|:---|
| 1 | **Handle missing values** — Glucose for patient 2 is missing → replace with an appropriate method |
| 2 | **Check for outliers** — glucose / BMI unusual values? |
| 3 | **Encode categorical data** — Gender → numerical representation |
| 4 | **Normalize numerical attributes** — if the algorithm requires it: Age, Glucose, BMI |
| 5 | **Select useful features** — remove irrelevant attributes if necessary |
| 6 | **Apply Data Mining** — Decision Tree · Naïve Bayes · k-NN · Logistic Regression · Random Forest |

**مرساة الـ 6 خطوات:**
> `Missing → Outliers → Encode → Normalize → Select → Mine`

---

<a name="9"></a>
# 9. Data Preparation vs Data Preprocessing

> *"These terms are sometimes used interchangeably, but there is a useful distinction."*

| Term | Scope | Typical contents |
|:---|:---|:---|
| **Data Preparation** | **Broader** process preparing data for analysis/mining | Cleaning · Integration · Transformation · Reduction · Discretization |
| **Data Preprocessing** | Often **narrower** — operations just before modeling | missing values · noise · encoding · scaling/normalization · feature selection |

> *"Data preprocessing can be considered an **important part of** the broader data preparation process."*
> *"The exact terminology can **vary between textbooks and research papers**."*

**Safe exam line:**
> *"Preprocessing is a core subset of the broader data preparation pipeline."*

---

<a name="10"></a>
# 10. Gemini Anchors & Safe Answers

## 10.1 Full Anchors Pack

| Topic | Anchor |
|:---|:---|
| Object chain | `Object → Attribute → Value Type → Structure → Technique` |
| Attribute types | `No order → Order, unknown gap → Two values → Quantity` |
| Numerical zero | `Interval: zero is a ruler mark · Ratio: zero is nothing left` |
| 8 structures | `Row → Basket → Document → Path → Clock → Map → Picture → Network` |
| Prep pipeline | `Clean → Integrate → Transform → Reduce → Discretize` |
| Missing methods | `Ignore → Expert → Mean → Median → Mode → Predict` |
| Medical prep | `Missing → Outliers → Encode → Normalize → Select → Mine` |
| Selection vs Extraction | `Pick vs Build` |
| Outlier rule | `Not necessarily error → Investigate first` |

## 10.2 Safe Exam Sentences (لا AI slop)

1. **Attribute type:**  
   *"[Variable] is a **Nominal/Ordinal/Binary/Numerical** attribute because [no natural order / meaningful order with unmeasurable gaps / two values / quantitative measure]."*

2. **URL (Dr. Ahmed):**  
   *"A URL is a **Nominal** attribute: identifiers/categories with no natural order and no meaningful distance between values."*

3. **Structure:**  
   *"The dataset is organized as **[record/transaction/.../graph]**; technique choice follows this structure."*

4. **Outliers:**  
   *"Outliers are investigated before removal because they may be valid extremes, not errors."*

5. **Selection vs Extraction:**  
   *"Feature selection chooses existing attributes; feature extraction constructs new ones."*

6. **Preparation importance:**  
   *"Good data preparation → better quality data → more reliable mining results."*

7. **Normalization (if numbers given):**  
   Write $x'=(x-\min)/(\max-\min)$, substitute, state range $[0,1]$.

---

<a name="11"></a>
# 11. Exam Quick Table — شنو تحفظ بالضبط

| Section | What to memorize | Priority |
|:---|:---|:---:|
| Object vs Attribute | Row=object, column=attribute | 🟡 |
| Attribute taxonomy | 4 types + decision questions + anchors | 🔴 |
| URL | **Nominal** + one-line justification | 🔴 |
| Numerical split | Discrete/Continuous + Interval vs Ratio (zero meaning) | 🔴 |
| Formulas | Min-Max worked example `40→0.5`; Z-score symbols | 🔴 |
| 8 structures | Master matrix + anchor + one example each | 🔴 |
| Attribute vs Structure separation | Lecture summary sentence | 🔴 |
| Prep pipeline | 5 steps + “order not always fixed” | 🔴 |
| Missing values | **6 methods** + mean=75 example + median when extreme | 🔴🔴 |
| Outlier | Not necessarily error | 🔴 |
| Cleaning problems | missing/noise/outlier/duplicate/inconsistent | 🔴 |
| Integration problems | names, formats, duplicates, units, schemas | 🟡 |
| Transformation | why normalize + one-hot warning | 🔴 |
| Reduction | Selection vs Extraction + PCA 100→10 | 🔴 |
| Discretization | Age bins example | 🟡 |
| Prep vs Preprocess | broader vs narrower | 🟡 |
| Medical walkthrough | 6 steps in order | 🟡 |

### Answering Recipes

**لو سؤال "Classify this attribute":**
1. Name the type
2. Give the criterion (order / gap / two values / quantity)
3. One concrete example

**لو سؤال "Given numbers, normalize":**
1. Formula first
2. Identify min/max or μ/σ
3. Intermediate arithmetic
4. Final value + range

**لو سؤال "How do you handle missing data?":**
1. List the 6 methods
2. Choose method by data type (numeric mean/median, categorical mode)
3. Mention extreme-value preference for median
4. Mention predictive models as advanced option

**لو سؤال "Describe data preparation":**
1. Definition + pipeline
2. Name 5 steps with one phrase each
3. Closing line: preparation ≠ only removing missing values

---

<a name="12"></a>
# 12. Question Bank

## 12.1 Objects & Attributes

**Q1.** What is a data object? Give four examples.
<details><summary>الجواب</summary>

An **entity about which information is collected**.
Examples: patient, student, customer, transaction (also document, image, geographic location).
</details>

**Q2.** What is an attribute?
<details><summary>الجواب</summary>

A **property or characteristic** of a data object (e.g. Age, Gender, BMI).
</details>

**Q3.** In a patient table, what does a row represent? What does a column represent?
<details><summary>الجواب</summary>

Row = **data object** (one patient). Column = **attribute** (one property).
</details>

---

## 12.2 Attribute Taxonomy

**Q4.** Define a Nominal attribute and give three examples.
<details><summary>الجواب</summary>

Categories with **no natural order**. Examples: Gender, Color, Country/Department.
`Male > Female` does not make sense.
</details>

**Q5.** 🔴 What is the data type of a **URL**? Justify.
<details><summary>الجواب</summary>

**Nominal.** A URL is an identifier/category with **no natural order** and **no meaningful measurable distance** between values.
</details>

**Q6.** Define Ordinal. Why can we not treat Low/Medium/High as numerical distances?
<details><summary>الجواب</summary>

Meaningful **order**, but gaps are **not necessarily measurable**. We know Low < Medium < High, but not that (Medium−Low) equals (High−Medium).
</details>

**Q7.** Give five binary examples from the lecture.
<details><summary>الجواب</summary>

Yes/No · True/False · 0/1 · Disease/No Disease · Purchased/Not Purchased
</details>

**Q8.** Distinguish Discrete vs Continuous numerical attributes with lecture examples.
<details><summary>الجواب</summary>

- **Discrete:** countable — number of children/transactions/students/visits
- **Continuous:** many values in a range — height 175.5, weight 72.4, temp 36.7°C, glucose 125.6
</details>

**Q9.** What is the difference between Interval-scaled and Ratio-scaled attributes?
<details><summary>الجواب</summary>

- **Interval:** zero is **arbitrary** (Celsius); ratios not meaningful
- **Ratio:** zero is **absolute physical zero** (Kelvin, salary, weight); ratios meaningful
</details>

**Q10.** Classify: (a) Department (b) Disease severity (c) Diabetes Yes/No (d) Salary (e) Number of visits (f) URL
<details><summary>الجواب</summary>

(a) Nominal (b) Ordinal (c) Binary (d) Numerical/Ratio (e) Numerical Discrete (f) **Nominal**
</details>

**Q11.** 🧠 State the attribute-type decision anchor.
<details><summary>الجواب</summary>

`No order → Order, unknown gap → Two values → Quantity`
</details>

---

## 12.3 Data Structures

**Q12.** State the lecture rule separating attribute types from data structures.
<details><summary>الجواب</summary>

Nominal/ordinal/binary/numerical describe **attributes**.  
Record/transaction/text/sequence/temporal/spatial/image/graph describe **how data is organized**.
</details>

**Q13.** List the 8 basic data structures.
<details><summary>الجواب</summary>

Record · Transaction · Text · Sequence · Temporal · Spatial · Image · Graph
</details>

**Q14.** Transaction data example T1={Bread,Milk,Egries} — what mining task is this used for?
<details><summary>الجواب</summary>

**Association rule mining** (e.g. Bread → Milk). *(Note: lecture example is Eggs, not "Egries" — watch spelling in written answers.)*
</details>

**Q15.** Why is order critical in sequence data?
<details><summary>الجواب</summary>

Because elements are stored in a **specific order**; `Login → Search → Product → Purchase` encodes behavior that the same items in another order would not.
</details>

**Q16.** How is a grayscale image represented? How is an RGB image represented?
<details><summary>الجواب</summary>

Grayscale: `Height × Width` (2D matrix). RGB: `Height × Width × 3`.
</details>

**Q17.** What are nodes and edges in graph data?
<details><summary>الجواب</summary>

**Nodes (vertices)** = objects. **Edges** = relationships. Example: students + friendship links.
</details>

**Q18.** Name four things temporal mining can discover.
<details><summary>الجواب</summary>

Trends · Seasonal patterns · Periodic patterns · Anomalies
</details>

**Q19.** 🧠 State the 8-structure anchor chain.
<details><summary>الجواب</summary>

`Row → Basket → Document → Path → Clock → Map → Picture → Network`
</details>

---

## 12.4 Data Preparation

**Q20.** Define Data Preparation.
<details><summary>الجواب</summary>

The process of preparing **raw data** so it can be used **effectively** by data mining algorithms.
</details>

**Q21.** Write the basic pipeline.
<details><summary>الجواب</summary>

`Raw Data → Data Preparation → Data Mining → Knowledge/Patterns`
</details>

**Q22.** List the five main preparation steps.
<details><summary>الجواب</summary>

Cleaning · Integration · Transformation · Reduction · Discretization
</details>

**Q23.** Are these five steps always executed in the same order for every dataset?
<details><summary>الجواب</summary>

**No.** The lecture states they are **not necessarily** performed in exactly the same order for every dataset; it depends on the data and the mining task.
</details>

**Q24.** Why is data preparation not "just removing missing values"?
<details><summary>الجواب</summary>

Because it is the **complete process** of making raw data suitable for discovering patterns — cleaning, integration, transformation, reduction, discretization.
</details>

---

## 12.5 Cleaning

**Q25.** List the common data cleaning problems.
<details><summary>الجواب</summary>

Missing values · Noisy data · Outliers · Duplicate records · Inconsistent data
</details>

**Q26.** 🔴 List the six methods for handling missing values.
<details><summary>الجواب</summary>

1. Ignore the record  
2. Fill manually (domain expert)  
3. Use the mean  
4. Use the median  
5. Use the mode  
6. Predict the missing value (regression, decision tree, k-NN, …)
</details>

**Q27.** 🔴 Compute the missing value in `60, 70, 80, ?, 90` using the mean.
<details><summary>الجواب</summary>

Observed values sum = 300, count = **4**  
mean = $300/4 = 75$ → `? = 75`
</details>

**Q28.** When is median preferred over mean for missing values?
<details><summary>الجواب</summary>

When data contains **extreme values** (e.g. `60,65,70,75,200` — 200 is extreme).
</details>

**Q29.** What mode value fills the missing gender in Male, Female, Male, Male, ?
<details><summary>الجواب</summary>

**Male** (most frequent category).
</details>

**Q30.** 🔴 An outlier is always an error — true or false? Justify with the lecture example.
<details><summary>الجواب</summary>

**False.** *"An outlier is not necessarily an error."* Example: unusually high blood pressure may reflect a real medical condition. **Investigate before removing.**
</details>

**Q31.** Name methods for detecting outliers.
<details><summary>الجواب</summary>

Statistical · Distance-based · Clustering · Visualization · Machine Learning methods
</details>

**Q32.** What harms can duplicate records cause?
<details><summary>الجواب</summary>

Increase size unnecessarily · bias analysis · affect frequency calculations · affect model performance
</details>

**Q33.** How do we fix Male / M / male inconsistency?
<details><summary>الجواب</summary>

**Standardize** all variants to one format, e.g. `Male`. Same idea for `Iraq/IRAQ/iraq → Iraq`.
</details>

**Q34.** What is binning? Show one bin partition of `10,12,13,20,22,25,30,31`.
<details><summary>الجواب</summary>

Binning groups numerical values into bins to smooth noise. Example: Bin1 10–13 · Bin2 20–25 · Bin3 30–31.
</details>

---

## 12.6 Integration / Transformation / Reduction

**Q35.** What is data integration? How did the university example join tables?
<details><summary>الجواب</summary>

Combines data from multiple sources into one dataset. University example joins student info and grades **using student ID**.
</details>

**Q36.** List five problems in data integration.
<details><summary>الجواب</summary>

Different attribute names · different formats · duplicate records · different units · different schemas
</details>

**Q37.** Why do we normalize? Use the Age/Salary/Income example.
<details><summary>الجواب</summary>

Because very different ranges (Age 0–100 vs Salary 300–10,000 vs Income up to 100,000) let large-range attributes **dominate** some algorithms.
</details>

**Q38.** 🔴 Min-Max normalize age 40 into [0,1] given min=20, max=60.
<details><summary>الجواب</summary>

$x' = (40-20)/(60-20) = 20/40 = 0.5$ → **0.5**
</details>

**Q39.** Write the Z-score formula and define symbols.
<details><summary>الجواب</summary>

$z = (x - \mu)/\sigma$  
$x$ = original value, $\mu$ = mean, $\sigma$ = standard deviation
</details>

**Q40.** Why can Male=1, Female=0 be dangerous? What alternative for Red/Blue/Green?
<details><summary>الجواب</summary>

Numeric codes may **incorrectly imply order**. For unordered colors, use **one-hot encoding**.
</details>

**Q41.** In disease prediction, which attributes might feature selection keep or drop from the medical list?
<details><summary>الجواب</summary>

Keep: Age, Gender, BMI, Blood Pressure. Drop: Patient Name, Phone Number, Address (irrelevant to the task).
</details>

**Q42.** 🔴 Distinguish Feature Selection from Feature Extraction.
<details><summary>الجواب</summary>

- **Selection:** choose **existing** features (e.g. keep Age)
- **Extraction:** **create new** features from originals (e.g. PCA components; BMI from weight/height)
</details>

**Q43.** What can dimensionality reduction achieve? Give the lecture PCA example.
<details><summary>الجواب</summary>

Reduce computational cost, storage, model complexity; help visualization. Example: **100 original features → 10 principal components**.
</details>

**Q44.** Discretize ages 18,25,32,47,65,72 using the lecture bins.
<details><summary>الجواب</summary>

0–17 Child · 18–35 Young Adult · 36–60 Adult · 61+ Senior  
→ Young, Young, Adult, Adult, Senior, Senior
</details>

---

## 12.7 Full Pipeline & Distinctions

**Q45.** Walk through the medical diabetes example — six steps before mining.
<details><summary>الجواب</summary>

1. Handle missing (Glucose ?)  
2. Check outliers  
3. Encode Gender  
4. Normalize Age/Glucose/BMI if needed  
5. Select useful features  
6. Apply classifier (DT, Naïve Bayes, k-NN, …)
</details>

**Q46.** Distinguish Data Preparation from Data Preprocessing.
<details><summary>الجواب</summary>

Preparation = **broader** (cleaning, integration, transformation, reduction, discretization).  
Preprocessing = often **narrower pre-modeling ops** (missing, noise, encoding, scaling, feature selection). Preprocessing ⊂ Preparation.
</details>

**Q47.** State the main idea / closing teaching point of data preparation.
<details><summary>الجواب</summary>

Good data preparation → better quality data → more reliable mining results. Preparation is not merely removing missing values.
</details>

**Q48.** 🧠 Recite the prep-pipeline anchor and the missing-values anchor.
<details><summary>الجواب</summary>

Prep: `Clean → Integrate → Transform → Reduce → Discretize`  
Missing: `Ignore → Expert → Mean → Median → Mode → Predict`
</details>

**Q49.** A written exam item gives numbers and asks for Min-Max. What is Dr. Ahmed's answering protocol?
<details><summary>الجواب</summary>

1. Write symbolic formula first  
2. Define symbols  
3. Show intermediate calculations  
4. Final value + conceptual interpretation / range $[0,1]$  
Use Han & Kamber terminology; do not invent ad-hoc terms.
</details>

**Q50.** Name three mining algorithms listed at the end of the medical example.
<details><summary>الجواب</summary>

Any three: Decision Tree · Naïve Bayes · k-NN · Logistic Regression · Random Forest
</details>

---

## 12.8 Rapid Oral Drill (Self-test)

Ask yourself without looking:
1. URL type? → **Nominal**
2. Six missing-value methods in order?
3. Outlier always error? → **No**
4. Selection vs Extraction?
5. Eight structures in anchor order?
6. Five prep steps?
7. Min-Max of 40 with min20 max60? → **0.5**
8. Interval vs Ratio zero meaning?
9. Attribute layer vs structure layer rule?
10. Prep vs preprocess relationship?

---

# خاتمة سريعة للمراجعة

| Layer | One-line takeaway |
|:---|:---|
| **Attributes** | Value kind — Nominal / Ordinal / Binary / Numerical (+ Interval/Ratio) |
| **Structures** | Dataset shape — 8 forms; technique follows structure |
| **Preparation** | Raw → clean/integrate/transform/reduce/discretize → mine |
| **Cleaning core** | 6 missing methods; outlier ≠ automatic error; standardize formats |
| **Math core** | Min-Max & Z-score with formula-first protocol |
| **Dr. Ahmed** | URL = Nominal; formulas symbolically first; Han terminology |

---

*Built by Koko for Abu Al-Hasan — Week 02 comprehensive note.*
*Sources: Dr. Ahmed Shakir lecture DOCX files + bilingual translation + Gemini Smart Memorisation method (Week 01 templates reused, source text preserved, not re-compressed) + Han & Kamber / Doctor Profile expansions clearly labeled.*
*Standing answer: URL data type = Nominal.*
