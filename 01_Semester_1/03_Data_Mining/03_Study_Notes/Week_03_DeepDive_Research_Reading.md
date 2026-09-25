---
title: Week 3 — استخراج السمات وقابلية نقل الأنواع (كيف نجعل أي بيانات قابلة للتنقيب)
course: Data Mining
subtitle: فهمي للملزمة — من بيانات خام بأنواع مختلفة، إلى تمثيل مناسب لخوارزمية التنقيب، عبر استخراج سمات جديدة و/أو تحويل الأنواع
---

# قراءة بحثية عميقة — الويك 3: استخراج السمات وقابلية نقل أنواع البيانات (النسخة v1)

> **ملاحظة مهمة قبل تبدأ:** الدكتور ما يعلم — هو **يوزع بحث**. في هالملزمة، كل اقتباس إنكليزي معلَّم بـ `Wn Px` (الملزمة n، الصفحة x) هو **حرفياً من كلام الدكتور** بملزمة الويك 3 (الملف `Week 03 - Feature Extraction and Portability.docx`) — ما انجم من راسي. تحته مباشرة الشرح العربي الفهمي. باقي الملزمة كله عربي (والمصطلحات الإنكليزية كما هي بالمحاضرة).
>
> قراها كأنك باحث: كل قسم فيه **بطاقة بحث** تحتها ثلاثة خطوط — **شنو هو**، **شلون يشتغل** (مع مثال)، و**ارتباطه بالمحاضرة**.
>
> **المرجع العميق:** Aggarwal, *Data Mining: The Textbook* (Springer 2015) — الفصل 2 §2.2 "Feature Extraction and Portability" (كتاب ص 29–34). أي إضافة منه معلَّمة **[كتاب]**، ومو مفروضة للامتحان إلا إذا الدكتور طلبها.

---

## القسم 1 — استخراج السمات (Feature Extraction)

هذا أول موضوع بالمحاضرة، وهو **أساس** كل اللي بعده. الدكتور يعرّفه مباشرة:

> **W3 P1** "Feature extraction is the process of creating new features from existing data to represent its important characteristics in a form suitable for data mining or machine learning algorithms."
>
> **W3 P1** "Obtains useful characteristics from the data."

**التعريف:** استخراج السمات = **صناعة سمات جديدة** من البيانات الموجودة، تُمثّل خصائصها المهمة بشكل **مناسب** لخوارزميات التنقيب أو تعلّم الآلة. لاحظ كلمة **creating new** — يعني نبني شي جديد، مو بس نختار (هذا الفرق عن Feature Selection، راح نفصّله).

**نقطة مهمة:** "التمثيل المناسب" = مناسب **للخوارزمية المختارة**، مو بالضرورة جدول رقمي واحد. ممكن يكون متجه، تسلسل، أو graph.

### 1.1 مثال الدكتور — صورة الأشعة (X-ray)

الدكتور يشرحها بمخطط حرفي:

> **W3 P1** "Instead of giving the complete image directly to a traditional algorithm, we can represent it using useful features."

**المخطط (حرفي من الملزمة):**

X-ray Image → Feature Extraction → Texture, shape, edges, intensity → Numerical Features → Classification

**شنو يعني:** ما نعطي الصورة كاملة للخوارزمية الكلاسيكية (لأنها ضخمة ومعقّدة). بدالها، نستخرج منها **سمات رقمية** (قوام texture، شكل shape، حواف edges، شدة intensity) وندخلها للنموذج للتصنيف.

**جدول بيانات حقيقي (صورة أشعة → متجه سمات):**

| Image ID | Texture | Shape (area) | Edge density | Mean intensity | Class |
|---|---|---:|---:|---:|---|
| X1 | 0.82 | 0.64 | 0.41 | 128 | Malignant |
| X2 | 0.31 | 0.22 | 0.18 | 96 | Benign |
| X3 | 0.77 | 0.59 | 0.38 | 141 | Malignant |
| X4 | 0.28 | 0.19 | 0.15 | 88 | Benign |

> كل صف = صورة تحوّلت لمتجه أرقام (features) → ياكله النموذج ويصنّفها.

### 1.2 ليش نستخرج السمات؟ (Why)

الدكتور يعطي قائمة حرفية:

> **W3 P1** "Raw data can be: very large, complex, difficult to process, high-dimensional, unsuitable for some algorithms."

> **W3 P1** "Reduce the amount of data. Remove unnecessary information. Represent important characteristics of the data."

> **W3 P2** "Make data easier for algorithms to process. Sometimes improve prediction or classification performance."

**الخلاصة:** البيانات الخام ممكن تكون **كبيرة، معقّدة، صعبة المعالجة، عالية الأبعاد، وغير مناسبة** لبعض الخوارزميات. فالاستخراج: **يقلّل** كمية البيانات، **يشيل** المعلومة غير الضرورية، **يمثّل** الخصائص المهمة، **يسهّل** الشغل على الخوارزمية، وأحياناً **يحسّن** دقة التنبؤ/التصنيف.

> [!CONCEPT] بطاقة بحث: Feature Extraction (استخراج السمات)
> - **شنو هو:** تحويل البيانات الخام إلى مجموعة سمات جديدة أكثر إفادة (عادةً متجه رقمي أصغر). يصير **قبل** أو **داخل** خط التنقيب.
> - **شلون يشتغل (مثال):** صورة أشعة 512×512 (=262,144 بكسل) → نستخرج منها 4–50 سمة (قوام، شكل، حواف) → متجه صغير يدخل المصنّف.
> - **ارتباطه بالمحاضرة:** هو الموضوع الأول والأساس — كل التحويلات اللي بعدها (رقمي/رمزي/رسم) هي أشكال مختلفة من "نمثّل البيانات بشكل يفيد الخوارزمية".

> [!CONCEPT] بطاقة بحث: Feature Extraction مقابل Feature Selection (الاستخراج مقابل الاختيار)
> - **شنو هو:** **الاختيار** ياخذ **مجموعة فرعية من السمات الموجودة** (Pick). **الاستخراج** **يبني سمات جديدة** (Build).
> - **شلون يشتغل (مثال):** عندك (الطول، الوزن، العمر): الاختيار = "خلي الطول والوزن واحذف العمر". الاستخراج = "سوِّ سمة جديدة BMI = الوزن/الطول²".
> - **ارتباطه بالمحاضرة:** الدكتور يذكر "creating **new** features" — يعني يقصد **الاستخراج**. لا تخلط بينهن بالامتحان: كلمة **new** = استخراج.

> [!CONCEPT] بطاقة بحث: Deep Features (السمات العميقة)
> - **شنو هو:** بدل ما نصمّم السمات يدوياً، نخلّي شبكة عصبية (CNN) **تتعلّمها** من الصور تلقائياً.
> - **شلون يشتغل:** طبقات CNN الأولى تتعلّم حواف/خطوط، والأعمق تتعلّم أشكالاً معقّدة، وآخر طبقة تعطي متجه سمات جاهز.
> - **ارتباطه بالمحاضرة:** الدكتور يذكر "Deep Features" كخيار حديث جنب السمات اليدوية (shape/texture/edges) بمخطط الصورة→متجه.

### 1.3 جدول المحاضرة — سمات لكل نوع بيانات

الدكتور يذكر:

> **W3 P2** "Different types of data require different extraction methods."

وبعدها الجدول الحرفي (Table):

| Data Type | Possible Extracted Features |
|:---|:---|
| **Image** | Shape, texture, edges, color |
| **Text** | Word frequency, TF-IDF, embeddings |
| **Time Series** | Mean, variance, frequency components |
| **Audio** | Frequency, energy, spectral features |
| **Spatial** | Distance, density, location features |
| **Sequence** | Symbol frequencies, patterns |
| **Graph** | Degree, centrality, connectivity |

> احفظ هذا الجدول زين — يجي بصيغة "شنو السمات الممكن استخراجها من النوع الفلاني؟".

---

## القسم 2 — قابلية نقل نوع البيانات (Data Type Portability)

الدكتور ينتقل للموضوع الثاني — وهو **قلب الويك 3**.

### 2.1 المشكلة أولاً

> **W3 P3** "In Data Mining, data can appear in many different forms."

أمثلة الملزمة الحرفية: Numerical (Age=25) · Categorical (Gender) · Text (reports/emails) · Time-series (heart rate) · Image (X-rays/CT) · Spatial (locations) · Sequence (DNA) · Graph (social networks).

> **W3 P3** "A dataset may contain several types of information at the same time. For example, a medical dataset may contain age, gender, medical reports, and heart-rate measurements."

> **W3 P3** "Different algorithms are designed to work with different forms of data. Therefore, some data may need to be converted into a suitable representation before applying a data mining algorithm."

**المعنى:** مجموعة بيانات وحدة ممكن تجمع أنواع مختلفة (مريض: عمر + جنس + تقارير نصية + نبض زمني). والخوارزميات مصمّمة لأنواع محددة، فلازم **نحوّل** البيانات لتمثيل مناسب قبل ما نشتغل.

### 2.2 التعريف + العملية (نص المحاضرة)

> **W3 P3** "Data Type Portability means converting data from one representation or type into another representation so that it can be processed by a data mining algorithm."

**العملية الأساسية (حرفي):**

Different Data Types → Data Type Conversion → Suitable Representation → Data Mining Algorithm

> **ملاحظة دقيقة:** "Suitable Representation" = تمثيل مناسب **للخوارزمية المختارة** (جدول، متجه، تسلسل، رسم…) — مو بالضرورة جدول رقمي واحد. هاي نقطة يختلط فيها الطلاب.

> [!CONCEPT] بطاقة بحث: Data Type Portability (قابلية نقل نوع البيانات)
> - **شنو هو:** تحويل البيانات من تمثيل/نوع إلى تمثيل آخر حتى تصير **قابلة للمعالجة** بخوارزمية تنقيب. تسمى أيضاً **data type porting** [كتاب].
> - **شلون يشتغل (مثال):** دمج بيانات مريض: العمر (رقمي) + الجنس (تصنيفي) + التقرير (نصي) + النبض (زمني) → نحوّل كلهن لتمثيل واحد مناسب → خوارزمية.
> - **ارتباطه بالمحاضرة:** هو عنوان الموضوع الثاني، والجسر لكل التحويلات اللي بعده.

> [!CONCEPT] بطاقة بحث: Heterogeneous Data (بيانات غير متجانسة)
> - **شنو هو:** مجموعة بيانات تحتوي أنواعاً مختلفة معاً (رقمية + نصية + صور + سلاسل…).
> - **شلون يشتغل:** معظم الخوارزميات تريد نوعاً واحداً متجانساً؛ فالـ portability وظيفتها توحّد هالتنوّع [كتاب].
> - **ارتباطه بالمحاضرة:** من مزايا الـ portability إنها "Make heterogeneous data easier to process" (راح نشوفها بالمزايا).

---

## القسم 3 — جدول التحويلات الشامل (قلب المادة)

الدكتور يذكر القائمة الحرفية:

> **W3 P4** "Numerical → Categorical: Discretization. Categorical → Numerical: Encoding. Text → Numerical: Vectorization. Time Series → Sequence: Symbolic representation. Time Series → Numerical features: DFT / DWT or feature extraction. Image → Numerical features: Feature extraction. Graph → Numerical representation: Graph embedding. Any data type → Graph: Similarity graph."

**الجدول المرجعي (احفظه — يجي مباشرة):**

| من (From) | إلى (To) | التقنية |
|:---|:---|:---|
| Numerical | Categorical | **Discretization** (التقطيع) |
| Categorical | Numerical | **Encoding** (One-Hot) |
| Text | Numerical | **Vectorization** (BoW / TF-IDF / embeddings) |
| Time Series | Sequence | **Symbolic representation** |
| Time Series | Numerical | **DFT / DWT** أو feature extraction |
| Image | Numerical | **Feature extraction** |
| Graph | Numerical | **Graph embedding** |
| **أي نوع** | **Graph** | **Similarity graph** |

> **انتبه للسطر الأخير** — هو الاتجاه **المعاكس** (بدل ما نحوّل كل شي لأرقام، نحوّل كل شي لـ graph). هذا اللي وقفت عنده، ونفصّله بالقسم 10.

> [!CONCEPT] بطاقة بحث: Representation (التمثيل)
> - **شنو هو:** الشكل اللي تكون عليه البيانات وقت تدخل الخوارزمية (جدول، متجه، تسلسل رمزي، رسم بياني).
> - **شلون يشتغل:** نفس البيانات ممكن تُمثّل بأشكال مختلفة، وكل شكل يناسب خوارزميات معينة.
> - **ارتباطه بالمحاضرة:** الهدف النهائي من كل تحويل هو الوصول لـ "Suitable Representation".

---

## القسم 4 — Numerical → Categorical: التقطيع (Discretization)

> **W3 P4** "Discretization converts continuous numerical values into a small number of categories or intervals."

**مثال الملزمة (bins):**

| Interval | Label |
|:---|:---|
| 0–17 | Young |
| 18–40 | Adult |
| 41–60 | Middle-aged |
| 61+ | Older |

**القيم بعد التحويل:** `25 → Adult` · `45 → Middle-aged` · `67 → Older`

**المزايا (حرفي):** "Makes numerical data easier to understand. Can make data suitable for algorithms that require categorical values."

**العيب (حرفي):**

> **W3 P4** "Some information can be lost. For example, ages 21 and 39 may both become 'Adult,' so their exact difference is no longer represented."

### 4.1 نوعا التقطيع (حرفي من الملزمة)

> **W3 P5** "Equal-Width Discretization — The numerical range is divided into intervals of approximately equal numerical size. Example: Age 0–80 divided into: 0–20, 21–40, 41–60, 61–80."

> **W3 P5** "Equal-Frequency Discretization — Each interval contains approximately the same number of observations. Example: 10, 12, 15, 18, 20, 30, 35, 40. Two groups: Group 1 → 10, 12, 15, 18; Group 2 → 20, 30, 35, 40."

**الفرق الجوهري:**

| النوع | القاعدة | مثال |
|:---|:---|:---|
| **Equal-Width** | نفس **المدى الرقمي** لكل فترة | Age 0–80 → [0–20][21–40][41–60][61–80] |
| **Equal-Frequency** | نفس **عدد السجلات** بكل فترة | 10,12,15,18 \| 20,30,35,40 |

> **دقة امتحانية:** مثال الملزمة أعداد صحيحة (0–20، 21–40…). للبيانات المستمرة، لازم تحدّد قاعدة الحدود، مثلاً `[0,20), [20,40), …`.

![شكل: تقطيع رقمي → فئات (Discretization)](../06_Diagrams_&_Mindmaps/03_Data_Mining/op_discretization.svg)

**جدول بيانات حقيقي (Numeric → Categorical):**

| Age | Bin (Equal-Width=20) |
|---:|---|
| 15 | Teen (0–20) |
| 18 | Teen (0–20) |
| 22 | Young (21–40) |
| 35 | Young (21–40) |
| 42 | Middle-aged (41–60) |
| 63 | Senior (61–80) |

> العمر 21 و39 كلهن "Young" — الفرق الدقيق ضاع (هذا هو العيب).

> [!CONCEPT] بطاقة بحث: Discretization (التقطيع)
> - **شنو هو:** تحويل قيم رقمية مستمرة إلى عدد صغير من الفئات/الفترات (bins).
> - **شلون يشتغل (مثال):** العمر (مستمر) → فئات (Young/Adult/…). أو الدخل → (Low/Mid/High).
> - **ارتباطه بالمحاضرة:** أول تحويل بالقائمة (Numerical → Categorical)، ومثال فقدان المعلومة يجي منه.

> [!CONCEPT] بطاقة بحث: Equal-Width مقابل Equal-Frequency
> - **شنو هو:** طريقتان لتحديد الفترات. Width = نفس العرض الرقمي؛ Frequency = نفس العدد.
> - **شلون يشتغل (مثال):** بيانات ملتوية (skewed): Equal-Width تعطي فترات فاضية/ممتلئة، Equal-Frequency توزّع السجلات بالتساوي.
> - **ارتباطه بالمحاضرة:** الدكتور يسمّيهن حرفياً كـ "Types of Discretization".

> [!CONCEPT] بطاقة بحث: Supervised vs Unsupervised Discretization [كتاب]
> - **شنو هو:** **Unsupervised** = نختار الفترات من التوزيع فقط (بدون label). **Supervised** = نستعمل الـ class label لتحديد الحدود (مثلاً نفصل "مقبول قرض" عن "مرفوض").
> - **شلون يشتغل:** Entropy-based discretization يقيس أي حد يفصل الأصناف أحسن.
> - **ارتباطه بالمحاضرة:** إضافة من الكتاب — الدكتور ما ذكرها صراحةً، بس مفيدة لو سأل "شلون نختار الحدود؟".

---

## القسم 5 — Categorical → Numerical: One-Hot Encoding

> **W3 P5** "Many machine learning algorithms require numerical input."

**مثال فصائل الدم (حرفي):**

> **W3 P5** "Suppose the categories are: A, B, O. One-hot encoding creates one binary column for each category. Patient P1: A → [1, 0, 0]. Patient P2: B → [0, 1, 0]. Patient P3: O → [0, 0, 1]. Here: 1 = category is present, 0 = category is absent."

**ليش ما نكتب A=1, B=2, O=3؟ (نص المحاضرة الحرفي — مهم جداً):**

> **W3 P5** "Using A = 1, B = 2, O = 3 may incorrectly suggest that the categories have a numerical order. For nominal categories such as blood type, there is no meaningful order. Therefore, one-hot encoding is usually more appropriate for nominal categorical data."

![شكل: One-Hot Encoding (Categorical → Numeric)](../06_Diagrams_&_Mindmaps/03_Data_Mining/op_onehot.svg)

**جدول بيانات حقيقي (فصائل دم → One-Hot):**

| Patient | Blood Type | A | B | O |
|---|---|---:|---:|---:|
| P1 | A | 1 | 0 | 0 |
| P2 | B | 0 | 1 | 0 |
| P3 | O | 0 | 0 | 1 |
| P4 | A | 1 | 0 | 0 |

> ثلاثة أعمدة بدل رقم واحد — عمداً ما كتبنا A=1,B=2,O=3.

> [!CONCEPT] بطاقة بحث: One-Hot Encoding (الترميز الساخن الواحد)
> - **شنو هو:** لكل فئة نسوي عموداً ثنائياً (0/1)؛ الفئة الموجودة = 1، الباقي = 0.
> - **شلون يشتغل:** {A,B,O} → 3 أعمدة؛ A → [1,0,0]، B → [0,1,0]، O → [0,0,1].
> - **ارتباطه بالمحاضرة:** هو تقنية "Categorical → Numerical" بالقائمة، والدكتور يشرح ليش مو A=1,B=2,O=3.

> [!CONCEPT] بطاقة بحث: Nominal vs Ordinal (اسمي مقابل ترتيبي)
> - **شنو هو:** **Nominal** = فئات بلا ترتيب (فصيلة دم، مدينة). **Ordinal** = فئات بترتيب (Small<Medium<Large).
> - **شلون يشتغل:** للـ nominal → one-hot (لا ترتيب). للـ ordinal → ممكن ترميز ترتيبي (1,2,3 مقبول).
> - **ارتباطه بالمحاضرة:** سبب رفض A=1,B=2,O=3 هو إنها **nominal** (بلا ترتيب حقيقي).

> [!CONCEPT] بطاقة بحث: Binarization / Label Encoding
> - **شنو هو:** **Label Encoding** = كل فئة برقم (0,1,2…) — مناسبة للـ ordinal فقط. **Binarization** = تحويل قيمة لعتبة 0/1.
> - **شلون يشتغل:** Label Encoding سريع بس يخلق ترتيباً وهمياً للـ nominal — هنا مشكلته.
> - **ارتباطه بالمحاضرة:** "Encoding" بالقائمة تشمل هذه الطرق؛ one-hot هي الأكثر أماناً للـ nominal.

---

## القسم 6 — Text → Numerical: Vectorization

> **W3 P6** "Many numerical algorithms cannot directly process raw text. Therefore, text is converted into numerical features."

**مثال الملزمة (حرفي):**

> **W3 P6** "Document 1: 'good product'. Document 2: 'good service'. Vocabulary: good, product, service. Numerical representation: D1 → [1, 1, 0], D2 → [1, 0, 1]."

**الطرق الشائعة (حرفي):** Bag of Words · TF-IDF · Word embeddings · Document embeddings.

**العملية:** `Text → Numerical Representation → Machine Learning / Data Mining` — والنتيجة متجه مثل `[0.12, 0.45, 0.08, 0.71, …]`.

![شكل: TF-IDF (Text → Numeric) — الكلمة النادرة وزنها أعلى](../06_Diagrams_&_Mindmaps/03_Data_Mining/op_tfidf.svg)

**جدول بيانات حقيقي (Term–Document بأوزان TF-IDF):**

| Term | Doc1 | Doc2 | ملاحظة |
|---|---:|---:|---|
| the | 0.10 | 0.08 | شائعة → وزن منخفض |
| good | 0.12 | 0.11 | شائعة نسبياً |
| product | 0.88 | 0.04 | نادرة بـ Doc1 → وزن عالي |
| service | 0.05 | 0.86 | نادرة بـ Doc2 → وزن عالي |

> كل خلية = وزن الكلمة بالمستند — هذا هو التمثيل الرقمي اللي ياكله النموذج.

> [!CONCEPT] بطاقة بحث: Bag of Words (BoW — حقيبة الكلمات)
> - **شنو هو:** تمثيل النص كمتجه من **عدد مرات كل كلمة** (بدون ترتيب).
> - **شلون يشتغل (مثال):** قاموس [good, product, service]: "good product" → [1,1,0]، "good service" → [1,0,1].
> - **ارتباطه بالمحاضرة:** أول طريقة بالمثال؛ بس تتجاهل الترتيب والمعنى وتؤدي لـ sparsity.

> [!CONCEPT] بطاقة بحث: TF-IDF (Term Frequency – Inverse Document Frequency)
> - **شنو هو:** وزن إحصائي يرفع الكلمات **النادرة المميزة** ويخفض **الشائعة التافهة**.
> - **شلون يشتغل:** `TF-IDF(t,d) = TF(t,d) × IDF(t)`، حيث `IDF(t) = log(N / (1 + df(t)))`. "cancer" بورقة طبية أهم من "the" رغم إن "the" أكثر.
> - **ارتباطه بالمحاضرة:** ثاني طريقة بالقائمة؛ تحسين على BoW.

> [!CONCEPT] بطاقة بحث: Word Embeddings (Word2Vec / GloVe / FastText)
> - **شنو هو:** تمثيل كل كلمة بمتجه **كثيف** (dense) صغير، والكلمات المتقاربة بالمعنى تكون متقاربة بالفضاء.
> - **شلون يشتغل (مثال):** `king − man + woman ≈ queen` — النموذج التقط العلاقة الدلالية.
> - **ارتباطه بالمحاضرة:** ثالث طريقة؛ تفهم المعنى والسياق بدل العدّ فقط.

> [!CONCEPT] بطاقة بحث: Document Embeddings (Doc2Vec)
> - **شنو هو:** امتداد الـ embeddings من **الكلمة** إلى **المستند كامل** (متجه واحد للمستند).
> - **شلون يشتغل:** Doc2Vec يتعلّم متجهاً للمستند ككل من كلماته.
> - **ارتباطه بالمحاضرة:** رابع طريقة بالقائمة الحرفية "Document embeddings".

---

## القسم 7 — Time Series: تحويلان مختلفان

الدكتور يعطي **اتجاهين** للسلسلة الزمنية — وهذا يختلط كثير:

### 7.1 → Numerical Features

> **W3 P7** "Sometimes we extract numerical characteristics from a time series."

Original time series → Feature extraction → Mean, standard deviation, frequency features, wavelet features → Numerical vector

### 7.2 → Symbolic Sequence

> **W3 P7** "A time series can also be represented using symbols. For example: Low = A, Medium = B, High = C. A numerical series such as: 20, 22, 21, 25, 27, 30 may become: A, A, A, B, B, C."

![شكل: سلسلة زمنية → سلسلة رمزية (SAX)](../06_Diagrams_&_Mindmaps/03_Data_Mining/op_ts_sequence.svg)

**جدول بيانات حقيقي (Time-Series → Symbolic Sequence):**

| Time | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| Heart Rate | 75 | 77 | 80 | 60 | 58 | 90 |
| Symbol | N | N | H | L | L | H |

> بدل الأرقام الخام، صارت رموز — أسهل لاكتشاف الأنماط. **بس انتبه:** الرموز تعتمد على **حدود** Low/Medium/High؛ بدونها الرمز مو وحيد.

> [!CONCEPT] بطاقة بحث: Statistical Features (السمات الإحصائية)
> - **شنو هو:** ملخّصات رقمية للسلسلة: mean, std, min/max, skewness, kurtosis.
> - **شلون يشتغل:** سلسلة 1000 نقطة → 6 أرقام تمثلها. أسرع وأخف للنموذج.
> - **ارتباطه بالمحاضرة:** "Mean, standard deviation" حرفياً بمخطط TS → Numerical.

> [!CONCEPT] بطاقة بحث: DFT / DWT (تحويلات التردد/الموجة)
> - **شنو هو:** **DFT** (Discrete Fourier Transform) يفكّك السلسلة لمكونات ترددية؛ **DWT** (Discrete Wavelet Transform) يفكّكها لمكوّنات بموقع زمني (موجة).
> - **شلون يشتغل:** سلسلة نغمة موسيقية → DFT يعطي الترددات المكوّنة. DWT أحسن للإشارات المتغيرة (ECG).
> - **ارتباطه بالمحاضرة:** الدكتور يذكر "DFT / DWT" حرفياً كطريقة Time Series → Numerical.

> [!CONCEPT] بطاقة بحث: SAX (Symbolic Aggregate Approximation)
> - **شنو هو:** الطريقة الرسمية لتحويل السلسلة الرقمية لرموز: تقسيم + متوسط + رموز بحدود.
> - **شلون يشتغل:** Normalize → قطّع لفترات متساوية → احسب متوسط كل فترة → حوّله لرمز حسب breakpoints.
> - **ارتباطه بالمحاضرة:** مثال "20,22,21,25,27,30 → A,A,A,B,B,C" هو نسخة مبسّطة من SAX [كتاب].

---

## القسم 8 — Image → Numerical

> **W3 P7** "Images are naturally represented using numerical values. A grayscale image can be represented as a matrix of pixel intensities."

**مثال المصفوفة (حرفي — 3 صفوف × 4 أعمدة):**

| Row | C1 | C2 | C3 | C4 |
|---|---:|---:|---:|---:|
| R1 | 0 | 25 | 80 | 120 |
| R2 | 10 | 40 | 100 | 150 |
| R3 | 20 | 60 | 130 | 200 |

> **W3 P8** "For a grayscale image: 0 → Black, 255 → White. A color RGB image normally contains three channels: Red, Green, and Blue."

**Image → Numerical Features (حرفي):**

Image → Feature Extraction → Shape, Texture, Edges, Color, Deep Features → Numerical Vector

> **W3 P8** "Instead of using every pixel, useful features can be extracted."

> [!CONCEPT] بطاقة بحث: Image Features (HOG / SIFT / Texture)
> - **شنو هو:** سمات يدوية للصور: **HOG** (اتجاهات الحواف)، **SIFT** (نقاط مميزة)، **GLCM** (قوام).
> - **شلون يشتغل:** HOG يقسّم الصورة لخلايا ويحسب اتجاه التدرّج بكل خلية → متجه.
> - **ارتباطه بالمحاضرة:** تطبيق مباشر لـ "shape, texture, edges, color" من مخطط الصورة.

> [!CONCEPT] بطاقة بحث: Deep Features (CNN)
> - **شنو هو:** سمات مستخرجة تلقائياً من طبقات CNN بدل التصميم اليدوي.
> - **شلون يشتغل:** الصورة تدخل الشبكة، وطبقة وسطية تعطي متجه سمات غني — يُستخدم للنقل (transfer learning).
> - **ارتباطه بالمحاضرة:** الدكتور يذكر "Deep Features" كخيار حديث بمخطط Image → Features.

---

## القسم 9 — Spatial / Sequence / Graph → Numerical

### 9.1 Spatial Data

> **W3 P8** "Spatial data describes objects according to their location."

أمثلة: GPS · Maps · Geographic info · Satellite · Hospital locations. مثال: H1 → (32.50, 45.82) · H2 → (32.48, 45.85).

> **W3 P8** "Spatial information can be transformed into numerical features that data mining algorithms can process."

> [!CONCEPT] بطاقة بحث: Spatial Features (السمات المكانية)
> - **شنو هو:** إحداثيات (lat/long)، مسافات لنقاط مرجعية، أو سمات شكل (area, perimeter).
> - **شلون يشتغل:** موقع مستشفى → (خط عرض، خط طول) → ممكن نحسب أقرب مستشفى لكل نقطة.
> - **ارتباطه بالمحاضرة:** مثال الإحداثيات حرفي بالمحاضرة.

### 9.2 Sequence Data

> **W3 P8** "A sequence is an ordered collection of elements."

أمثلة (حرفي): DNA `A C G T A C G` · Customer actions `Login → Search → Product → Purchase` · Web `Home → Products → Laptop → Checkout`.

> **W3 P9** "The order of elements is important. Sequence data can sometimes be transformed into numerical features."

> [!CONCEPT] بطاقة بحث: Sequence Encoding (k-mer / One-hot)
> - **شنو هو:** تحويل التسلسل لأرقام: one-hot لكل رمز، أو **k-mer counts** (نكسر التسلسل لقطع طول k ونعدّها).
> - **شلون يشتغل (مثال):** DNA "ATCGA" بـ k=3 → {ATC, TCG, CGA} → متجه عددها.
> - **ارتباطه بالمحاضرة:** "Sequence → Numerical: Sequence encoding" بالقائمة، والترتيب مهم.

### 9.3 Graph Data

> **W3 P9** "A graph consists of: Nodes (vertices), Edges (connections)."

مثال حرفي: A,B,C,D عقد؛ الحواف علاقات. وتحويل رقمي:

> **W3 P9** "Graph data can be transformed into numerical representations. For example: Node A → [0.21, 0.75, 0.43], Node B → [0.19, 0.81, 0.39]."

![شكل: Graph → Numeric (Graph Embedding)](../06_Diagrams_&_Mindmaps/03_Data_Mining/op_graph_embedding.svg)

**جدول بيانات حقيقي (شبكة تواصل — قائمة روابط → متجهات):**

| Edge | From | To | Relation |
|---|---|---|---|
| e1 | Ahmed | Sara | friend |
| e2 | Sara | Omar | friend |
| e3 | Omar | Ahmed | friend |
| e4 | Lina | Omar | colleague |

> كل عقدة تنتهي بمتجه أرقام (embedding) — النموذج يقدر يشتغل عليه.

> [!CONCEPT] بطاقة بحث: Graph Embedding (Node2Vec / GNN)
> - **شنو هو:** تحويل عقد الرسم لمتجهات كثيفة تحفظ البنية.
> - **شلون يشتغل:** **Node2Vec/DeepWalk**: مشي عشوائي على الرسم → يُعالَج كجُمل → Word2Vec يعطي متجهات العقد. **GNN**: تجميع سمات الجيران.
> - **ارتباطه بالمحاضرة:** "Graph → Numerical: Graph embedding" بالقائمة.

---

## القسم 10 — ★ التحويل إلى Graph (Similarity Graph) — النقطة اللي وقفت عندها

**هذا هو سبب التشتت:** كل الأقسام اللي فاتت كانت "حوّل كل شي إلى **أرقام**". هنا الدكتور **يقلب الاتجاه**: "بدل ما نحوّل كل شي أرقام، نمثّل **العلاقات** كـ graph".

> **W3 P9** "Instead of converting everything into numerical data, relationships between objects can be represented using a graph."
>
> **W3 P9** "Suppose we have five patients. If two patients are sufficiently similar, we connect them. The nodes represent objects, and the edges represent similarity."

> **W3 P10** "A similarity graph can be created using a similarity or distance measure. For example: If distance(P1, P2) < threshold → Connect P1 and P2. The graph represents which objects are similar to each other."
>
> **W3 P10** "Applications: Clustering. Classification. Nearest-neighbor analysis. Outlier detection."

### شنو يعني (What)؟

بدل التمثيل الرقمي، نمثّل **الأغراض كـ nodes** و**العلاقات كـ edges**. أشهر شكل: **Similarity Graph** — نربط كل غرضين متشابهين بحافة.

### شلون يشتغل (How) — الخطوات والمثال:

1. عندنا 5 مرضى، كل واحد عنده سمات رقمية (عمر، ضغط، كوليسترول).
2. نختار **مقياس مسافة** (مثلاً Euclidean).
3. لكل زوج: **إذا** `distance(P_i, P_j) < threshold` **إذن** نربطهم بحافة.
4. النتيجة: graph يمثّل أي مريض يشبه أي مريض.

**شكل الرسم (بالكلمات):** P1,P2,P3,P4 متصلين ببعض فيتشكّل عنقود واحد، بينما P5 **معزولة** (مسافتها فوق الـ threshold).

![شكل: Similarity Graph — 5 مرضى، 4 عنقود + P5 معزول (outlier)](../06_Diagrams_&_Mindmaps/03_Data_Mining/op_similarity_graph.svg)

**جدول بيانات حقيقي (5 مرضى + مسافات → روابط):**

| Pair | Distance | Connected? |
|---|---:|---|
| P1–P2 | 0.12 | ✓ (نفس العنقود) |
| P2–P4 | 0.18 | ✓ |
| P4–P3 | 0.15 | ✓ |
| P3–P1 | 0.20 | ✓ |
| P5–الكل | 0.95 | ✗ (معزول → outlier) |

> المسافة < threshold → نربط. P5 بعيدة عن الكل → ما انربطت → شذوذ. وهذا يربطنا بـ Anomaly Detection.

### التطبيقات (ليش نسويها؟):
- **Clustering:** كل مكوّن متصل = عنقود.
- **Classification:** ننشر صنف العقد المعروفة لباقي العقد.
- **Nearest-neighbor analysis:** الجيران = العقد المتصلة.
- **Outlier detection:** العقدة المعزولة = شاذة.

> **الفكرة الجوهرية:** التحويل لـ graph **يعكس الاتجاه** — هنا نحوّل **إلى** graph (من أي نوع)، بينما بقسم 9 حولنا **من** graph إلى أرقام. الدكتور يدرّس الاتجاهين.

> [!CONCEPT] بطاقة بحث: Similarity Graph (رسم التشابه)
> - **شنو هو:** graph عقدها الأغراض وحوافها التشابه، تُبنى بمقياس مسافة/تشابه.
> - **شلون يشتغل:** `d(Oi,Oj) < ε` → حافة. أو k-nearest neighbors.
> - **ارتباطه بالمحاضرة:** قلب القسم الأخير؛ مثال "5 مرضى" حرفي.

> [!CONCEPT] بطاقة بحث: kNN Graph (رسم الجيران الأقرب) [كتاب]
> - **شنو هو:** بدل عتبة ε، نربط كل عقدة بأقرب k جيران لها.
> - **شلون يشتغل:** علاقة الجوار غير متناظرة (A جار B بس B مو بالضرورة جار A) → ممكن graph موجّه؛ عادةً نتجاهل الاتجاه.
> - **ارتباطه بالمحاضرة:** بديل العتبة اللي يذكره Aggarwal §2.2؛ نفس فكرة Similarity Graph.

> [!CONCEPT] بطاقة بحث: Heat Kernel (نواة الحرارة) [كتاب]
> - **شنو هو:** دالة تحوّل المسافة إلى **وزن** للحافة (كل ما تقاربوا، زاد الوزن).
> - **شلون يشتغل:** `w_ij = exp( -d(Oi,Oj)² / t² )` حيث t معامل يحدده المستخدم؛ الوزن الأكبر = تشابه أكثر.
> - **ارتباطه بالمحاضرة:** تفصيل من Aggarwal §2.2 (كتاب ص 30) — الدكتور ذكر الفكرة بدون المعادلة. اعرف الاسم لو سأل.

> [!CONCEPT] بطاقة بحث: Spectral Clustering (التجميع الطيفي) [كتاب]
> - **شنو هو:** تجميع يعتمد على الـ graph (eigenvectors لمصفوفة Laplacian) بدل مراكز النقاط.
> - **شلون يشتغل:** نبني Similarity Graph → نحسب Laplacian → نأخذ eigenvectors → نجمّع.
> - **ارتباطه بالمحاضرة:** ليش الدكتور يبني graph أصلاً — لأن بعض خوارزميات التجميع تشتغل على البنية العلاقاتية أحسن من المتجهات.

---

## القسم 11 — فقدان المعلومة (Information Loss)

> **W3 P10** "Data type conversion is useful, but it may result in information loss."

**المثال الحرفي:**

> **W3 P11** "Original ages: 21, 22, 39. After discretization: Adult, Adult, Adult. The exact ages have disappeared."

> **W3 P11** "A good conversion should preserve the important information needed for the mining task."

**الجدول:**

| Original | After Discretization |
|---|---|
| 21 | Adult |
| 22 | Adult |
| 39 | Adult |

> الأعمار الدقيقة (والفرق بينها) ضاعت — **هذا الثمن** اللي ندفعه مقابل التبسيط.

> [!CONCEPT] بطاقة بحث: Information Loss (فقدان المعلومة)
> - **شنو هو:** أي تحويل تقريباً يخسر جزءاً من التفاصيل الأصلية (بينما يكسب قابلية للمعالجة).
> - **شلون يشتغل (مثال):** 21,22,39 → Adult: صاروا نفس الفئة، والفرق 17 سنة اختفى.
> - **ارتباطه بالمحاضرة:** مبدأ امتحاني — "A good conversion should preserve the important information needed for the mining task".

> [!CONCEPT] بطاقة بحث: Task-Relative Preservation (حفظ المعلومة حسب المهمة)
> - **شنو هو:** المعلومة "المهمة" تعتمد على **المهمة**، مو ثابتة.
> - **شلون يشتغل:** لمهمة "شخص بالغ/قاصر"، الفئات كافية (21=22=39 Adult ما يضر). لمهمة "تنبؤ دقيق بالعمر"، الفئات تضر.
> - **ارتباطه بالمحاضرة:** لهذا الدكتور يقول "preserve the important information **needed for the mining task**".

---

## القسم 12 — المزايا، القيود، وتمييز Portability عن Data Mining

### 12.1 المزايا (5 — حرفي)

> **W3 P11** "Data Type Portability can: 1. Make heterogeneous data easier to process. 2. Allow existing algorithms to work with different data types. 3. Convert complex data into suitable representations. 4. Facilitate integration of different data sources. 5. Make machine learning and data mining algorithms easier to apply."

### 12.2 القيود (6 — حرفي)

> **W3 P11** "Data type conversion may have several limitations: 1. Information loss. 2. Loss of original structure. 3. Possible distortion of relationships. 4. High-dimensional representations. 5. Additional computational cost. 6. The converted representation may not be suitable for every algorithm."

> **W3 P11** "Therefore, the conversion method should be selected according to the data and the mining task."

**الجدول (لا تخلط بينهن):**

| المزايا (5) | القيود (6) |
|:---|:---|
| heterogeneous data أسهل | فقدان معلومة |
| إعادة استخدام الخوارزميات الموجودة | فقدان البنية الأصلية |
| تبسيط البيانات المعقّدة | تشويه محتمل للعلاقات |
| دمج مصادر مختلفة | تمثيلات عالية الأبعاد |
| تطبيق ML/DM أسهل | كلفة حسابية إضافية |
| — | التمثيل الجديد قد لا يناسب كل خوارزمية |

### 12.3 Portability مقابل Data Mining (تمييز)

> **W3 P11** "Data Type Portability focuses on: 'How can we represent data in a form suitable for an algorithm?'"

> **W3 P12** "Data Mining focuses on: 'How can we discover useful patterns or knowledge from the data?'"

**السلسلة الكاملة (حرفي):**

Raw Data → Data Preparation → Data Type Conversion → Mining Algorithm → Patterns / Prediction / Knowledge

| | السؤال الجوهري |
|:---|:---|
| **Data Type Portability** | كيف **نمثّل** البيانات بشكل مناسب للخوارزمية؟ |
| **Data Mining** | كيف **نكتشف** أنماطاً/معرفة مفيدة من البيانات؟ |

> [!CONCEPT] بطاقة بحث: Portability مقابل Mining (التمييز)
> - **شنو هو:** Portability = **تمثيل** (represent). Mining = **اكتشاف** (discover).
> - **شلون يشتغل:** Portability تجهّز البيانات؛ Mining يطلع الأنماط/التنبؤات/المعرفة.
> - **ارتباطه بالمحاضرة:** تمييز صريح بالملزمة — لو سأل "شنو Portability؟" الجواب = **تمثيل**، مو "اكتشاف أنماط".

---

## خاتمة — ملخص سريع للمراجعة

1. **Feature Extraction:** صناعة سمات **جديدة** من البيانات (مو اختيار) — مثال X-ray.
2. **Data Type Portability:** تحويل الأنواع لتمثيل مناسب للخوارزمية (Represent ≠ Discover).
3. **جدول التحويلات (8):** Discretization · Encoding · Vectorization · Symbolic · DFT/DWT · Image FE · Graph Embedding · **Any→Graph**.
4. **Discretization:** Equal-Width (نفس العرض) مقابل Equal-Frequency (نفس العدد) + **فقدان معلومة** (21,22,39 → Adult).
5. **One-Hot:** لكل فئة عمود ثنائي؛ ما نكتب A=1,B=2,O=3 (nominal بلا ترتيب).
6. **Text → Numeric:** BoW / TF-IDF / embeddings / document embeddings.
7. **★ التحويل إلى Graph:** Similarity Graph = نربط كل غرضين `distance < threshold` — الاتجاه المعاكس (into graph).

> **نصيحة للدكتور:** هو "يوزع بحث" — فكل مصطلح (HOG, SAX, Node2Vec, Heat kernel…) هو **بطاقة بحث** بهالوثيقة. راجع البطاقة قبل أي محاضرة جاية.

---

## Retrieval Set (بطاقات للمراجعة السريعة — للامتحان)

**[RS-01]** شنو الفرق بين Feature Extraction و Feature Selection؟
> Extraction **تبني سمات جديدة** (BMI من الوزن/الطول). Selection **تختار** من السمات الموجودة. كلمة "new" بالمحاضرة = Extraction.

**[RS-02]** عرّف Data Type Portability.
> تحويل البيانات من تمثيل/نوع إلى آخر حتى تقدر خوارزمية التنقيب تعالجها. (Represent، مو Discover.)

**[RS-03]** اذكر جدول التحويلات الشائع (8).
> Numerical→Cat: Discretization · Cat→Num: Encoding · Text→Num: Vectorization · TS→Seq: Symbolic · TS→Num: DFT/DWT · Image→Num: FE · Graph→Num: Graph embedding · Any→Graph: Similarity graph.

**[RS-04]** شنو الفرق بين Equal-Width و Equal-Frequency؟
> Equal-Width: فترات بنفس **العرض الرقمي** (0–20,21–40…). Equal-Frequency: كل فترة بنفس **عدد السجلات**.

**[RS-05]** ليش ما نكتب A=1, B=2, O=3 للفصائل؟
> لأنها **nominal** بلا ترتيب حقيقي؛ الأرقام توهم النموذج بترتيب عددي غير موجود. الصح = One-Hot.

**[RS-06]** شلون نبني Similarity Graph؟
> نحدد مقياس مسافة/تشابه؛ لكل زوج `distance(P1,P2) < threshold` → نربطهم بحافة. العقد = أغراض، الحواف = تشابه. التطبيقات: clustering · classification · NN · outlier detection.

**[RS-07]** شنو مثال فقدان المعلومة بالتقطيع؟
> 21, 22, 39 → كلهن "Adult"؛ الأعمار الدقيقة والفرق بينها ضاع. القاعدة: التحويل لازم يحفظ المعلومة المهمة للمهمة.

**[RS-08]** اذكر 3 من قيود التحويل.
> فقدان معلومة · فقدان البنية الأصلية · تشويه العلاقات · أبعاد عالية · كلفة حسابية · قد لا يناسب كل خوارزمية.
