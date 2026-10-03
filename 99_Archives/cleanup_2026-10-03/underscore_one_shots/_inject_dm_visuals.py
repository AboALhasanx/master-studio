# -*- coding: utf-8 -*-
"""Inject SVG visuals + real example data tables into the DM deep-dive reading."""
import io, sys

PATH = r"C:\Users\gokoq\Master-Studio\01_Semester_1\03_Data_Mining\03_Study_Notes\Week_02_03_DeepDive_Research_Reading.md"
DIAG = "../06_Diagrams_&_Mindmaps/03_Data_Mining"  # relative to note dir

def img(f, cap):
    return f"![{cap}]({DIAG}/{f})"

# Each: anchor (exact substring) -> block to insert AFTER the anchor
INS = []

# 2.1 Quantitative
INS.append((
"**الخصائص:** قيم مستمرة (أرقام حقيقية)، تمثّل على شكل متجه (vector)، استخداماتها: Regression, clustering, anomaly detection.",
img("dt_quantitative.svg", "شكل: بيانات كمية متعددة الأبعاد — كل سجل = متجه أرقام") + """

**جدول بيانات حقيقي (مجموعة طبية — كل صف متجه أرقام):**

| Patient | Age | Blood Pressure | Cholesterol | BMI |
|---|---:|---:|---:|---:|
| P1 | 25 | 120 | 190 | 22.1 |
| P2 | 41 | 135 | 210 | 26.4 |
| P3 | 33 | 118 | 175 | 23.0 |
| P4 | 58 | 150 | 240 | 29.8 |

> كل صف = نقطة بـ 4 أبعاد، مثلاً P1 = `[25, 120, 190, 22.1]`.
"""))

# 2.2 Categorical & Mixed
INS.append((
"**التحدي:** نحتاج تقنيات ترميز خاصة (مثل one-hot)، وقياس المسافة أصعب من الرقمي.",
img("dt_categorical.svg", "شكل: بيانات تصنيفية ومختلطة — فئات + أرقام") + """

**جدول بيانات حقيقي (سجلات طلاب — مختلطة رقمي + تصنيفي):**

| Student | Age | Gender | GPA | Major |
|---|---:|---|---:|---|
| S1 | 21 | Male | 3.4 | CS |
| S2 | 22 | Female | 3.1 | Math |
| S3 | 20 | Male | 2.9 | CS |
| S4 | 23 | Female | 3.7 | Physics |

> العمود `Gender` و `Major` تصنيفي (nominal)؛ الباقي رقمي. هذا بالضبط اللي يحتاج one-hot.
"""))

# 2.3 Binary & Set
INS.append((
"**التطبيقات:** Association rule mining، recommender systems.",
img("dt_binary_set.svg", "شكل: بيانات ثنائية (مصفوفة 0/1) وبيانات مجموعات (سلة)") + """

**جدول بيانات حقيقي (مصفوفة شرائية — كل صف binary set):**

| Customer | Milk | Bread | Eggs | Cheese |
|---|---:|---:|---:|---:|
| C1 | 1 | 1 | 1 | 0 |
| C2 | 0 | 1 | 0 | 1 |
| C3 | 1 | 0 | 1 | 0 |
| C4 | 0 | 0 | 0 | 0 |

> سلة C1 = {Milk, Bread, Eggs}. خوارزمية Apriori تبحث الأنماط بين هالسلات.
"""))

# 2.4 Text
INS.append((
"**التطبيقات:** Sentiment analysis, topic modeling, chatbots, search engines.",
img("dt_text.svg", "شكل: نص غير مهيكل ← تحويل لأرقام") + """

**جدول بيانات حقيقي (مستندات + تمثيلها):**

| Doc | Text (raw) | Bag-of-Words vector (cat, dog, mat, log, sat, the, on) |
|---|---|---|
| D1 | "The cat sat on the mat" | [1, 0, 1, 0, 1, 2, 1] |
| D2 | "The dog sat on the log" | [0, 1, 0, 1, 1, 2, 1] |

> النص الخام ما يقراه النموذج — نحوله لأرقام (BoW/TF-IDF) أولاً.
"""))

# 3.1 Time-Series
INS.append((
"**التطبيقات:** Forecasting, anomaly detection.",
img("dt_timeseries.svg", "شكل: سلسلة زمنية — قيم عبر الزمن") + """

**جدول بيانات حقيقي (سعر سهم عبر 8 أيام):**

| Day | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Price | 100 | 102 | 99 | 105 | 103 | 107 | 110 | 108 |

> الترتيب مهم: 100→102→99 له معنى، ما يصير نعيد ترتيبه عشوائي.
"""))

# 3.2 Discrete Sequences
INS.append((
"**التطبيقات:** Bioinformatics، web usage mining، NLP.",
img("dt_sequence.svg", "شكل: سلسلة رموز منفصلة — ترتيب مهم") + """

**جدول بيانات حقيقي (سلاسل منفصلة):**

| ID | Type | Sequence |
|---|---|---|
| S1 | DNA | A → T → C → G → A → C → G |
| S2 | Clickstream | Home → Search → Product → Cart |
| S3 | DNA | A → T → G → G → A → C → T |

> تبديل رمز واحد يغير المعنى (مثل الطفرة بالـ DNA) — لذلك الترتيب أساسي.
"""))

# 3.3 Spatial
INS.append((
"**التطبيقات:** GIS، مراقبة المرور، النمذجة البيئية.",
img("dt_spatial.svg", "شكل: بيانات مكانية — إحداثيات على شبكة") + """

**جدول بيانات حقيقي (مواقع مستشفيات — lat/long):**

| Hospital | Latitude | Longitude | Type |
|---|---:|---:|---|
| H1 | 32.50 | 45.82 | General |
| H2 | 32.48 | 45.85 | Children |
| H3 | 32.55 | 45.79 | Cardiac |
| H4 | 32.46 | 45.90 | General |

> نحسب "المسافة" بينها بالإحداثيات — أقرب مستشفى = الأهم للتحليل المكاني.
"""))

# 3.4 Network & Graph
INS.append((
"**التطبيقات:** تحليل التواصل الاجتماعي، كشف الاحتيال، recommender systems.",
img("dt_graph.svg", "شكل: شبكة/رسم بياني — عقد + روابط") + """

**جدول بيانات حقيقي (شبكة تواصل — قائمة روابط):**

| Edge | From (node) | To (node) | Relation |
|---|---|---|---|
| e1 | Ahmed | Sara | friend |
| e2 | Sara | Omar | friend |
| e3 | Omar | Ahmed | friend |
| e4 | Lina | Omar | colleague |

> الجدول يحتوي عقد (From/To) وروابط — هذا تمثيل "edge list" لـ graph.
"""))

# Section 4 pipeline
INS.append((
"6. **Data Splitting** — تقسيم لـ training / validation / test (بمهام ML).",
img("op_pipeline.svg", "شكل: خطوة تجهيز البيانات (pipeline)") + """

> كل خطوة تأخذ مخرجات السابقة — هذا هو "الأنبوب" قبل ما تدخل البيانات للنموذج.
"""))

# 6.1 Discretization
INS.append((
"**العيب:** ضياع معلومة (21 و39 يصيرون نفس الفئة \"Adult\").",
img("op_discretization.svg", "شكل: تقطيع رقمي ← فئات (Discretization)") + """

**جدول بيانات حقيقي (Numeric → Categorical):**

| Age | Bin (Equal-Width=20) |
|---:|---|
| 15 | Teen (0–20) |
| 18 | Teen (0–20) |
| 22 | Young (21–40) |
| 35 | Young (21–40) |
| 42 | Middle (41–60) |
| 50 | Middle (41–60) |
| 63 | Senior (61–80) |
| 70 | Senior (61–80) |

> العمر 21 و 39 كلهن "Young" — الفرق الدقيق ضاع (هذا هو العيب).
"""))

# 6.2 One-Hot
INS.append((
"(غطيناه بالقسم 2.2 — راجع بطاقة One-Hot. النقطة الإضافية من المحاضرة 3: **لا تكتب A=1,B=2,O=3** للـ nominal لأنه يختلق ترتيب مو موجود.)",
img("op_onehot.svg", "شكل: One-Hot Encoding (Categorical → Numeric)") + """

**جدول بيانات حقيقي (فصائل دم → One-Hot):**

| Patient | Blood Type | A | B | O |
|---|---|---:|---:|---:|
| P1 | A | 1 | 0 | 0 |
| P2 | B | 0 | 1 | 0 |
| P3 | O | 0 | 0 | 1 |
| P4 | A | 1 | 0 | 0 |

> ثلاثة أعمدة بدل رقم واحد — ما كتبنا A=1,B=2,O=3 عمداً.
"""))

# 6.3 Text → Num
INS.append((
"(غطيناه بالقسم 2.4 — BoW, TF-IDF, embeddings. هذا أهم تحويل عند الدكتور.)",
img("op_tfidf.svg", "شكل: TF-IDF (Text → Numeric) — الكلمة النادرة وزنها أعلى") + """

**جدول بيانات حقيقي (مصفوفة Term–Document بأوزان TF-IDF):**

| Term | Doc1 | Doc2 | ملاحظة |
|---|---:|---:|---|
| the | 0.10 | 0.08 | شائعة → وزن منخفض |
| cat | 0.91 | 0.05 | نادرة بـ Doc1 → وزن عالي |
| dog | 0.04 | 0.88 | نادرة بـ Doc2 → وزن عالي |

> الجدول **هو** التمثيل الرقمي اللي ياكله النموذج — كل خلية = وزن الكلمة بالمستند.
"""))

# 6.4 Time Series → Seq
INS.append((
"- **→ Sequence (رمزي):** نحول الأرقام لرموز. مثال: `[75,77,80,60,58,90]` → `[N,N,H,L,L,H]` (Normal/High/Low). تقنية شهيرة: **SAX** (Symbolic Aggregate Approximation) — تطبيع، تقسيم لقطاعات، أخذ المتوسط، ربطه برمز.",
img("op_ts_sequence.svg", "شكل: سلسلة زمنية ← سلسلة رمزية (SAX)") + """

**جدول بيانات حقيقي (Time-Series → Symbolic Sequence):**

| Time | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| Heart Rate | 75 | 77 | 80 | 60 | 58 | 90 |
| Symbol | N | N | H | L | L | H |

> بدل الأرقام الخام، صارت رموز — أسهل لاكتشاف الأنماط والشذوذ.
"""))

# 6.8 Graph Embedding
INS.append((
"> **ارتباطه بالمحاضرة:** الدكتور يذكر Node2Vec/GNN كحل لمشكلة \"الخوارزميات تريد أرقام والـ graph مو أرقام\".",
img("op_graph_embedding.svg", "شكل: Graph → Numeric (Graph Embedding)") + """

**جدول بيانات حقيقي (Graph → Numeric vector):**

| Node | Embedding (dense vector) |
|---|---|
| A | [0.21, 0.75, 0.43] |
| B | [0.19, 0.81, 0.39] |
| C | [0.24, 0.70, 0.51] |
| D | [0.22, 0.78, 0.44] |

> كل عقدة صارت متجه أرقام — النموذج يقدر يشتغل عليه.
"""))

# 6.9 Similarity Graph (replace textual shape description with the real diagram)
INS.append((
"**شكل الرسم الناتج (بالكلمات):** العقد P1,P2,P3,P4 متصلين ببعض (P1—P2، P2—P4، P4—P3، P3—P1) فيتشكل عنقود واحد، بينما P5 عقدة **معزولة** ما انربطت بأحد لأن مسافتها عن الكل فوق الـ threshold.",
img("op_similarity_graph.svg", "شكل: Similarity Graph — 5 مرضى، 4 عنقود + P5 معزول (outlier)") + """

**جدول بيانات حقيقي (5 مرضى + مسافات ← روابط):**

| Pair | Distance | Connected? |
|---|---:|---|
| P1–P2 | 0.12 | ✓ (نفس العنقود) |
| P2–P4 | 0.18 | ✓ |
| P4–P3 | 0.15 | ✓ |
| P3–P1 | 0.20 | ✓ |
| P5–الكل | 0.95 | ✗ (معزول → outlier) |

> المسافة < threshold → نربط. P5 بعيدة عن الكل → ما انربطت → شذوذ.
"""))

# 7.2 Scaling
INS.append((
"- **Max Abs / Robust / Decimal Scaling:** بدائل حسب الحالة.",
img("op_scaling.svg", "شكل: التحجيم — Min-Max مقابل Z-Score") + """

**جدول بيانات حقيقي (Scaling على ميزة واحدة):**

| Raw | Min-Max (0–1) | Z-Score |
|---:|---:|---:|
| 10 | 0.00 | -1.22 |
| 20 | 0.50 | 0.00 |
| 30 | 1.00 | 1.22 |

> بدون التحجيم، القيمة 30 تسيطر على الخوارزمية — بعده كل الميزات بمدى متقارب.
"""))

# ---- apply ----
with io.open(PATH, "r", encoding="utf-8") as f:
    txt = f.read()

missing = []
for anchor, block in INS:
    if anchor not in txt:
        missing.append(anchor[:40])
        continue
    txt = txt.replace(anchor, anchor + "\n" + block, 1)

if missing:
    print("MISSING ANCHORS:", missing)
else:
    with io.open(PATH, "w", encoding="utf-8") as f:
        f.write(txt)
    print("OK: injected", len(INS), "visuals + tables")
