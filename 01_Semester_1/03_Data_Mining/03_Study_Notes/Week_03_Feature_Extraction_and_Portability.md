# Data Mining — Week 03: COMPREHENSIVE Notes
## Feature Extraction and Portability — استخراج الميزات وقابلية تحويل أنواع البيانات

> **Instructor:** Asst. Prof. Dr. Ahmed Shakir Abd Al-Rida
> **Course:** `03_Data_Mining` (CS602) — 2 Credit Hours
> **Lecture:** Monday 2026-09-21 · Week 03
> **Sources:**
> 1. `Week 03 - Feature Extraction and Portability.docx` — lecture core
> 2. Aggarwal, *Data Mining: The Textbook* (Springer, 2015) — **Ch 2.2 Feature Extraction and Portability** (source of lecture framing)
> 3. Doctor Profile exam prototype: feature-extraction pipeline (e.g. CT/X-ray → features → classification)
> 4. Cross-links to `Week_02_Data_Types_and_Preparation.md`
>
> **Purpose:** lighter companion to Week 02 — focuses on what is **new** here. Discretization, one-hot, text vectors, and basic structures are **not re-taught**; they are cross-referenced.
>
> **Related standing material:** Week 02 note already covers attribute taxonomy, 8 data structures, data preparation pipeline, Feature Selection vs Feature Extraction, and URL = Nominal.

---

## المحتويات

| # | القسم | جديد أم ربط؟ |
|:--:|:---|:---|
| 0 | [Where this sits in the course map](#0) | ربط |
| 1 | [Feature Extraction — التعريف والمثال](#1) | **جديد** |
| 2 | [Why Feature Extraction + Features by Data Type](#2) | **جديد** (جدول المحاضرة) |
| 3 | [Data Type Portability — التعريف والبصيغة](#3) | **جديد** |
| 4 | [Master Conversion Matrix](#4) | **قلب المادة** |
| 5 | [Conversions one-by-one](#5) | أمثلة المحاضرة + ربط Week 02 |
| 6 | [Any Type → Graph (Similarity Graph)](#6) | **جديد** |
| 7 | [Information Loss — المبدأ الامتحاني](#7) | **جديد** |
| 8 | [Portability vs Data Mining](#8) | **جديد** (تمييز) |
| 9 | [Advantages & Limitations](#9) | **جديد** |
| 10 | [Dr. Ahmed exam lens — X-ray / CT pipeline](#10) | **جديد** |
| 11 | [Anchors & Safe Answers](#11) | حفظ |
| 12 | [Exam Quick Table](#12) | مُجمّع |
| 13 | [Question Bank](#13) | ~30 سؤال |
| 14 | [Cross-links to Week 02](#14) | ربط |

---

<a name="0"></a>
# 0. Where This Sits

```
Week 01  Introduction / KDD / why mine
Week 02  Data objects · attribute types · 8 structures · Data Preparation
Week 03  Feature Extraction · Data Type Portability   ← WE ARE HERE
Week 04+ Deeper preprocessing math (cleaning detail, integration, reduction...)
Later    Patterns · Classification · Clustering
```

**One-line bridge from Week 02:**
Week 02 asked *what type is this attribute / how is data organized / how do we clean it?*  
Week 03 asks *how do we **represent** raw/heterogeneous data so an algorithm can run on it?*

---

<a name="1"></a>
# 1. Feature Extraction — Definition & Core Example

## 1.1 Definition (نص المحاضرة)

> *"Feature extraction is the process of **creating new features from existing data** to represent its important characteristics in a form suitable for data mining or machine learning algorithms."*

> *"**Obtains useful characteristics** from the data."*

## 1.2 The Lecture Pipeline — X-ray (نموذج امتحان د. أحمد)

```
X-ray Image
    ↓
Feature Extraction
    ↓
Texture, shape, edges, intensity
    ↓
Numerical Features
    ↓
Classification
```

> *"Instead of giving the **complete image directly** to a traditional algorithm, we can represent it using **useful features**."*

**AR:** ما نمدّ الصورة كاملة للخوارزمية الكلاسيكية — نستخرج منها **سمات رقمية** (قوام، شكل، حواف، شدة) وبعدها نصنّف.

**Keywords:** `Raw → Extract → Feature vector → Classify`

## 1.3 Link to Week 02 (لا تعيد — اربط)

| Week 02 | Week 03 |
|:---|:---|
| Feature **Selection** = Pick existing | Feature **Extraction** = **Build new** |
| Image structure = pixels `H×W` / `H×W×3` | We do **not** always mine every pixel — we extract shape/texture/edges |
| Prep pipeline includes transformation | Feature extraction is a **representation** step before/inside mining |

---

<a name="2"></a>
# 2. Why Extract + Features by Data Type

## 2.1 Why? (نص المحاضرة)

**Raw data can be:**
- Very large
- Complex
- Difficult to process
- High-dimensional
- Unsuitable for some algorithms

**Feature extraction can:**
1. **Reduce** the amount of data
2. **Remove** unnecessary information
3. **Represent** important characteristics
4. Make data **easier for algorithms** to process
5. Sometimes **improve** prediction / classification performance

**مرساة Why:**
> `Too big / too complex → extract → smaller useful vector → algorithm works better`

## 2.2 Quick Reference — Data Type → Possible Extracted Features

> **من جدول المحاضرة (Table 0) — احفظه**

| Data Type | Possible Extracted Features |
|:---|:---|
| **Image** | Shape, texture, edges, color |
| **Text** | Word frequency, TF-IDF, embeddings |
| **Time Series** | Mean, variance, frequency components |
| **Audio** | Frequency, energy, spectral features |
| **Spatial** | Distance, density, location features |
| **Sequence** | Symbol frequencies, patterns |
| **Graph** | Degree, centrality, connectivity |

> **ملاحظة:** نص المحاضرة يذكر تحت *Examples of Feature Extraction* فقط: *"Different types of data require different extraction methods."* — التفصيل **فوق بالجدول**، مو بالفقرة السردية.

**🧠 Features Anchor:**
> `Image shape/text · Text TF-IDF · TS mean/freq · Audio spectral · Spatial density · Sequence symbols · Graph degree`

---

<a name="3"></a>
# 3. Data Type Portability — Definition

## 3.1 The Problem (نص المحاضرة)

Data can appear in many forms at once:
- Numerical — Age = 25, Salary = 800,000
- Categorical — Gender = Male/Female
- Text — medical reports, emails, reviews
- Time-series — heart rate every second
- Image — X-rays, CT
- Spatial — locations/maps
- Sequence — DNA
- Graph — social networks

> *"A dataset may contain **several types of information at the same time**."*  
> Example medical set: age + gender + medical reports + heart-rate.

> *"Different algorithms are designed to work with **different forms** of data."*

## 3.2 Definition + Process (نص المحاضرة)

> *"**Data Type Portability** means converting data from one representation or type into another representation so that it can be processed by a data mining algorithm."*

```
Different Data Types
    → Data Type Conversion
    → Suitable Representation
    → Data Mining Algorithm
```

**[Textbook / Aggarwal]:** this is also called **data type porting** — transform heterogeneous features into a **uniform representation** when no off-the-shelf analytical approach fits the mix.

**مرساة Portability:**
> `Mixed types → Convert → One suitable form → Algorithm`

---

<a name="4"></a>
# 4. Master Conversion Matrix (قلب المادة)

> **من جدول المحاضرة (Table 1) — هذا اللي تحفظه**

| From | To | Technique |
|:---|:---|:---|
| Numerical | Categorical | **Discretization** |
| Categorical | Numerical | **One-hot encoding** (Encoding / Binarization) |
| Text | Numerical | **TF-IDF / embeddings** (Vectorization) |
| Time Series | Numerical | **Feature extraction** |
| Time Series | Sequence | **Symbolic representation** |
| Image | Numerical | **Feature extraction** |
| Sequence | Numerical | **Sequence encoding** |
| Graph | Numerical | **Graph embedding** |
| **Any type** | **Graph** | **Similarity graph** |

**Also listed in lecture “Common Data Type Conversions”:**
- Time Series → Numerical features: DFT / DWT or feature extraction
- Graph → Numerical: Graph embedding
- Any data type → Graph: Similarity graph

**[Textbook / Aggarwal Table 2.1 — labeled expansion, not required for basic exam unless doctor asks]:**

| Source | Destination | Methods (Aggarwal) |
|:---|:---|:---|
| Numeric | Categorical | Discretization |
| Categorical | Numeric | Binarization |
| Text | Numeric | Latent Semantic Analysis (LSA) |
| Time series | Discrete sequence | **SAX** |
| Time series | Numeric multi-dim | **DWT, DFT** |
| Discrete sequence | Numeric multi-dim | DWT, DFT |
| Spatial | Numeric multi-dim | 2-d DWT |
| Graphs | Numeric multi-dim | **MDS, spectral** |
| Any type | Graphs | Similarity graph *(restricted applicability)* |

**🧠 Matrix Anchor (lecture level):**
> `Discretize · One-hot · Vectorize · Extract · Symbolize · Embed · Similarity-graph`

---

<a name="5"></a>
# 5. Conversions One-by-One — Lecture Text + Keywords

## 5.1 Numerical → Categorical : Discretization

**Definition:** converts continuous numerical values into a **small number of categories/intervals**.

**Lecture bins:**
| Interval | Label |
|:---|:---|
| 0–17 | Young |
| 18–40 | Adult |
| 41–60 | Middle-aged |
| 61+ | Older |

**Mapped values:** `25 → Adult` · `45 → Middle-aged` · `67 → Older`

**Advantages (lecture):**
- Easier to understand
- Suitable for algorithms that need categorical values

**Disadvantage (lecture):**
> Information can be lost — ages **21 and 39** may both become **Adult**; exact difference disappears.

### Types of Discretization (lecture)

| Type | Rule | Lecture example |
|:---|:---|:---|
| **Equal-Width** | intervals of approximately equal **numerical size** | Age 0–80 → `0–20, 21–40, 41–60, 61–80` |
| **Equal-Frequency** | each interval ~same **number of observations** | `10,12,15,18` \| `20,30,35,40` |

**Week 02 cross-link:** same idea as preparation §Discretization; Week 03 adds **equal-width vs equal-frequency** naming and the loss warning as a first-class point.

**Keywords:** `Bins/categories` + `Equal-width vs equal-frequency` + `Info loss`

---

## 5.2 Categorical → Numerical : Encoding / One-hot

**Why:** many ML algorithms require **numerical input**.

**Lecture blood-type example:**
- Categories: `A, B, O`
- P1 A → `[1, 0, 0]`
- P2 B → `[0, 1, 0]`
- P3 O → `[0, 0, 1]`

> `1 = category present` · `0 = category absent`

### Why not A=1, B=2, O=3?

> *"Using A = 1, B = 2, O = 3 may **incorrectly suggest** that the categories have a numerical order."*
> *"For **nominal** categories such as blood type, there is **no meaningful order**."*
> *"Therefore, **one-hot encoding** is usually more appropriate for nominal categorical data."*

**Week 02 cross-link:** same warning as Gender=1/0 and Red/Blue/Green one-hot. Blood type is the cleaner exam example.

**Keywords:** `One binary column per category` + `No fake order`

---

## 5.3 Text → Numerical : Vectorization

**Text sources listed:** emails · news · reviews · medical reports · social posts

> *"Many numerical algorithms cannot directly process raw text."*

**Lecture mini-example:**
- D1: `"good product"`
- D2: `"good service"`
- Vocabulary: `good, product, service`
- D1 → `[1, 1, 0]`
- D2 → `[1, 0, 1]`

**Common approaches (lecture):**
- Bag of Words
- TF-IDF
- Word embeddings
- Document embeddings

```
Text → Numerical Representation → Machine Learning / Data Mining
```

Example vector shape: `[0.12, 0.45, 0.08, 0.71, …]`

**[Textbook]:** Aggarwal highlights **LSA** after vector-space text, plus length scaling — deeper than the lecture; know the **name** if asked, not the full math yet.

**Keywords:** `BoW / TF-IDF / embeddings` + `Count vector example`

---

## 5.4 Time Series → Numerical Features

```
Original time series
    → Feature extraction
    → Mean, standard deviation, frequency features, wavelet features
    → Numerical vector
```

Then the vector can feed ML algorithms.

**Keywords:** `Mean / std / frequency / wavelet → vector`

---

## 5.5 Time Series → Symbolic Sequence

**Mapping idea:** Low=A · Medium=B · High=C

**Lecture series:** `20, 22, 21, 25, 27, 30` → `A, A, A, B, B, C`

> Numerical time series converted into a **symbolic sequence**.

**[Textbook]:** formal method name **SAX** (Symbolic Aggregate Approximation) — window averaging + equi-depth symbolization. Lecture uses the idea without the formal algorithm.

**Keywords:** `Symbols instead of numbers` + `Order kept`

---

## 5.6 Image Data (context) + Image → Features

**Images are already numeric:**
- Grayscale = matrix of pixel intensities
- Example matrix from lecture:

```
0    25   80  120
10   40  100  150
20   60  130  200
```

- Grayscale: `0 → Black` · `255 → White`
- Color RGB: three channels Red, Green, Blue

**Image → Numerical Features:**

```
Image
  → Feature Extraction
  → Shape, Texture, Edges, Color, Deep Features
  → Numerical Vector
  → classifier / clustering algorithm
```

> *"Instead of using **every pixel**, useful features can be extracted."*

**Keywords:** `Not every pixel` + `Shape/texture/edges/color/deep`

---

## 5.7 Spatial Data

**Describes objects by location.** Examples: GPS · maps · geographic info · satellite · hospital locations.

**Lecture example:**
- Hospital H1 → lat 32.50, lon 45.82
- Hospital H2 → lat 32.48, lon 45.85

> Spatial info can be transformed into **numerical features** that mining algorithms can process.

**Keywords:** `Location-linked` + `Coordinates → features`

---

## 5.8 Sequence Data

> *"A sequence is an **ordered collection of elements**."*

Examples:
- DNA: `A C G T A C G`
- Customer actions: `Login → Search → Product → Purchase`
- Web: `Home → Products → Laptop → Checkout`

> *"The **order of elements is important**. Sequence data can sometimes be transformed into numerical features."*

**Week 02 cross-link:** structure definition already known; Week 03 adds **conversion to numeric** as an option.

**Keywords:** `Order matters` + `Encode to numeric when needed`

---

## 5.9 Graph Data

**Graph consists of:** Nodes (vertices) · Edges (connections)

Lecture sketch:
```
A ----- B
|       |
|       |
C ----- D
```

A,B,C,D may be users; edges = relationships.

**Conversion example (lecture):**
- Node A → `[0.21, 0.75, 0.43]`
- Node B → `[0.19, 0.81, 0.39]`

> Graph data can be transformed into **numerical representations** (embeddings).

**Keywords:** `Nodes+edges` + `Node embedding vector`

---

<a name="6"></a>
# 6. Any Type → Graph (Similarity Graph)

## 6.1 The Idea (نص المحاضرة)

> *"Instead of converting everything into numerical data, relationships between objects can be represented using a **graph**."*

Example: five patients — if two patients are **sufficiently similar**, connect them.
- **Nodes** = objects
- **Edges** = similarity

## 6.2 Construction Rule

> *"A similarity graph can be created using a **similarity or distance measure**."*

```
If distance(P1, P2) < threshold
    → Connect P1 and P2
```

> The graph represents **which objects are similar** to each other.

## 6.3 Applications (lecture list)

- Clustering
- Classification
- Nearest-neighbor analysis
- Outlier detection

## 6.4 [Textbook expansion — labeled]

Aggarwal formalizes a **neighborhood graph**:
1. One node per object
2. Edge if `d(Oi,Oj) < ε`, **or** use **k-nearest neighbors**
3. k-NN relation is not symmetric → directed graph; directions often ignored
4. Edge weight via kernel of distance, e.g. heat kernel  
   $w_{ij} = e^{-d(O_i,O_j)^2/t^2}$

> Useful when problems are **similarity/distance-based**. *"Distance function design is so important for virtually any data type."* (Aggarwal Ch 3 is the deep dive.)

**Keywords:** `distance < threshold → edge` + `Any type can become a graph`

---

<a name="7"></a>
# 7. Information Loss — Exam Principle

> **نص المحاضرة:** *"Data type conversion is useful, but it may result in **information loss**."*

**Example:**
- Original ages: `21, 22, 39`
- After discretization: `Adult, Adult, Adult`
- *"The exact ages have disappeared."*

> *"A good conversion should **preserve the important information** needed for the mining task."*

**[Textbook agreement]:** discretization loses variation within ranges; porting *"does lose representational accuracy and expressiveness in some cases."*

**Safe exam line:**
> *"Conversion may lose information; the method must preserve what the mining task needs."*

**Keywords:** `21/22/39 → Adult` + `Preserve task-critical info`

---

<a name="8"></a>
# 8. Portability vs Data Mining (تمييز)

> **نص المحاضرة:**

| | Focus question |
|:---|:---|
| **Data Type Portability** | *"How can we **represent** data in a form suitable for an algorithm?"* |
| **Data Mining** | *"How can we **discover** useful patterns or knowledge from the data?"* |

**Full pipeline (lecture):**
```
Raw Data
  → Data Preparation
  → Data Type Conversion
  → Mining Algorithm
  → Patterns / Prediction / Knowledge
```

**Safe exam line:**
> *"Portability prepares **representation**; mining discovers **patterns**."*

**Keywords:** `Represent vs Discover`

---

<a name="9"></a>
# 9. Advantages & Limitations

## 9.1 Advantages (5 — نص المحاضرة)

1. Make **heterogeneous** data easier to process
2. Allow **existing algorithms** to work with different data types
3. Convert **complex** data into suitable representations
4. Facilitate **integration** of different data sources
5. Make ML / data mining algorithms **easier to apply**

## 9.2 Limitations (6 — نص المحاضرة)

1. Information loss
2. Loss of original structure
3. Possible distortion of relationships
4. High-dimensional representations
5. Additional computational cost
6. Converted representation may **not suit every algorithm**

> *"Therefore, the conversion method should be selected according to the **data and the mining task**."*

**🧠 Advantages Anchor:**
> `Heterogeneous OK · Reuse algorithms · Simplify complex · Integrate sources · Apply ML easier`

**🧠 Limitations Anchor:**
> `Lose info · Lose structure · Distort relations · High-dim · Cost · Maybe wrong for algo`

---

<a name="10"></a>
# 10. Dr. Ahmed Exam Lens

## 10.1 Doctor-Profile Prototype (High Yield)

From `00_Doctor_Profile.md`:

> *"Illustrate the complete **feature extraction and data preparation pipeline** for classifying **lung nodule malignancy** from **2D CT scans**."*

### Model answer skeleton (Week 03 style)

```
Raw CT / X-ray image
  → (optional) preprocessing: noise, normalization
  → Feature Extraction
       texture · shape · edges · intensity / deep features
  → Numerical feature vector
  → Classification algorithm
       (Decision Tree / Naïve Bayes / k-NN / ...)
  → Output: malignant vs benign (or class labels)
```

**Doctor answering protocol still applies:**
1. Draw/name the pipeline stages in order
2. Name features in textbook terms
3. Name the algorithm family
4. State what the final decision is
5. No filler

## 10.2 Other Likely Question Shapes

| Shape | How to answer |
|:---|:---|
| Define feature extraction | Lecture definition + X-ray one-liner |
| Why not feed raw image? | Large/complex/high-dim → extract useful features |
| Convert Age to categories | Discretization + example bins + note info loss |
| Blood type to numbers | One-hot; **not** 1/2/3 because nominal |
| Convert any data for clustering | Similarity graph if distance defined |
| Portability vs mining | Represent vs discover |
| List conversion techniques | Master matrix (Table 1) |

---

<a name="11"></a>
# 11. Anchors & Safe Answers

## 11.1 Anchors Pack

| Topic | Anchor |
|:---|:---|
| Feature extraction flow | `Raw → Extract → Feature vector → Classify` |
| Why extract | `Too big / complex → extract → algorithm-ready vector` |
| Features by type | `Image shape/text · Text TF-IDF · TS mean/freq · Audio spectral · Spatial density · Seq symbols · Graph degree` |
| Portability process | `Mixed types → Convert → Suitable form → Algorithm` |
| Matrix | `Discretize · One-hot · Vectorize · Extract · Symbolize · Embed · Similarity-graph` |
| Info loss | `21/22/39 → Adult` + preserve task info |
| Portability vs mining | `Represent vs Discover` |
| Advantages | `Heterogeneous · Reuse · Simplify · Integrate · Apply` |
| Limitations | `Info · Structure · Distort · High-dim · Cost · Wrong algo` |

## 11.2 Safe Exam Sentences

1. **Definition:**  
   *"Feature extraction creates **new features** from existing data so algorithms receive a compact, useful representation."*

2. **X-ray pipeline:**  
   *"Extract texture, shape, edges, and intensity → numerical vector → classification."*

3. **Portability definition:**  
   *"Converting data from one representation/type to another so a mining algorithm can process it."*

4. **Discretization loss:**  
   *"Discretization may merge distinct values (21, 22, 39 → Adult); important differences can disappear."*

5. **One-hot rationale:**  
   *"One-hot avoids implying a false numerical order on nominal categories such as blood type."*

6. **Similarity graph:**  
   *"If distance between two objects is below a threshold, connect them; edges represent similarity."*

7. **Portability vs mining:**  
   *"Portability focuses on suitable **representation**; mining focuses on **discovering patterns**."*

8. **Choosing a conversion:**  
   *"Select the conversion according to the data type and the mining task, balancing information loss and algorithm requirements."*

---

<a name="12"></a>
# 12. Exam Quick Table

| Section | Memorize | Priority |
|:---|:---|:---:|
| Feature extraction definition | create **new** features from existing data | 🔴 |
| X-ray pipeline | image → texture/shape/edges/intensity → vector → classify | 🔴🔴 |
| Why extract | 5 reasons (large, complex, reduce, easier, maybe better perf) | 🔴 |
| Features-by-type table | 7 rows | 🔴 |
| Portability definition + process | mixed → convert → suitable → algorithm | 🔴 |
| Master conversion matrix | 9 rows From/To/Technique | 🔴🔴 |
| Discretization types | equal-width vs equal-frequency + examples | 🔴 |
| One-hot + blood type | not 1/2/3 | 🔴 |
| Text vector example | good product / good service counts | 🟡 |
| TS → numeric vs symbolic | mean/std/freq vs A/B/C | 🔴 |
| Similarity graph rule | distance < threshold → edge | 🔴 |
| Information loss | 21,22,39 → Adult | 🔴 |
| Portability vs mining | represent vs discover | 🔴 |
| Advantages 5 / Limitations 6 | anchors above | 🟡 |
| Doctor CT/X-ray pipeline | full ordered answer | 🔴 |

### Answer Recipes

**Pipeline question:** draw stages top→bottom; name features; name algorithm; name output.  
**Conversion question:** From → technique name → To + one example + loss note if relevant.  
**Why one-hot:** nominal + no order + binary columns per category.  
**Any-type clustering idea:** similarity graph + threshold/kNN.

---

<a name="13"></a>
# 13. Question Bank

## 13.1 Feature Extraction

**Q1.** Define feature extraction.
<details><summary>الجواب</summary>

The process of **creating new features from existing data** to represent important characteristics in a form suitable for data mining / ML algorithms.
</details>

**Q2.** Draw the lecture X-ray pipeline.
<details><summary>الجواب</summary>

X-ray → Feature Extraction → Texture, shape, edges, intensity → Numerical Features → Classification
</details>

**Q3.** Why not give the complete image directly to a traditional algorithm?
<details><summary>الجواب</summary>

Raw images are large, complex, high-dimensional, and often unsuitable; extracted features give a smaller useful representation.
</details>

**Q4.** List five things feature extraction can do.
<details><summary>الجواب</summary>

Reduce data amount · remove unnecessary info · represent important characteristics · make data easier for algorithms · sometimes improve prediction/classification performance
</details>

**Q5.** Match data type to typical extracted features (Image / Text / Time Series / Graph).
<details><summary>الجواب</summary>

Image: shape, texture, edges, color  
Text: word frequency, TF-IDF, embeddings  
Time Series: mean, variance, frequency components  
Graph: degree, centrality, connectivity
</details>

**Q6.** What features might be extracted from audio? From spatial data?
<details><summary>الجواب</summary>

Audio: frequency, energy, spectral features  
Spatial: distance, density, location features
</details>

---

## 13.2 Portability — Core

**Q7.** Define data type portability.
<details><summary>الجواب</summary>

Converting data from **one representation or type** into **another** so it can be processed by a data mining algorithm.
</details>

**Q8.** Write the basic portability process.
<details><summary>الجواب</summary>

Different Data Types → Data Type Conversion → Suitable Representation → Data Mining Algorithm
</details>

**Q9.** Why might a medical dataset need portability?
<details><summary>الجواب</summary>

It may mix age, gender, medical reports (text), and heart-rate (time series); algorithms expect a suitable single representation.
</details>

**Q10.** 🔴 List the common conversions from the lecture table.
<details><summary>الجواب</summary>

Numerical→Categorical: Discretization  
Categorical→Numerical: One-hot encoding  
Text→Numerical: TF-IDF / embeddings  
Time Series→Numerical: Feature extraction  
Time Series→Sequence: Symbolic representation  
Image→Numerical: Feature extraction  
Sequence→Numerical: Sequence encoding  
Graph→Numerical: Graph embedding  
Any→Graph: Similarity graph
</details>

---

## 13.3 Conversions Detail

**Q11.** Discretize ages using 0–17 Young, 18–40 Adult, 41–60 Middle-aged, 61+ Older: 25, 45, 67.
<details><summary>الجواب</summary>

Adult · Middle-aged · Older
</details>

**Q12.** Distinguish equal-width vs equal-frequency discretization.
<details><summary>الجواب</summary>

Equal-width: intervals of similar **numerical size** (0–20, 21–40…).  
Equal-frequency: each interval has ~same **number of records**.
</details>

**Q13.** Equal-frequency example groups from lecture?
<details><summary>الجواب</summary>

`10,12,15,18` | `20,30,35,40`
</details>

**Q14.** 🔴 What is lost when 21, 22, 39 are discretized?
<details><summary>الجواب</summary>

All become **Adult**; exact ages and their differences disappear — **information loss**.
</details>

**Q15.** 🔴 Encode blood types A, B, O with one-hot for patients A, B, O.
<details><summary>الجواب</summary>

A → [1,0,0] · B → [0,1,0] · O → [0,0,1]
</details>

**Q16.** Why not A=1, B=2, O=3?
<details><summary>الجواب</summary>

Blood type is **nominal** — numeric codes incorrectly imply an order. One-hot is more appropriate.
</details>

**Q17.** Convert documents D1 "good product" and D2 "good service" to count vectors.
<details><summary>الجواب</summary>

Vocab: good, product, service → D1 [1,1,0] · D2 [1,0,1]
</details>

**Q18.** Name four text vectorization approaches from the lecture.
<details><summary>الجواب</summary>

Bag of Words · TF-IDF · Word embeddings · Document embeddings
</details>

**Q19.** How do we convert a time series to numerical features?
<details><summary>الجواب</summary>

Extract mean, standard deviation, frequency features, wavelet features → numerical vector.
</details>

**Q20.** Convert time series 20,22,21,25,27,30 using Low=A, Medium=B, High=C.
<details><summary>الجواب</summary>

A, A, A, B, B, C
</details>

**Q21.** How is a grayscale image represented? What about RGB?
<details><summary>الجواب</summary>

Grayscale: matrix of pixel intensities (0 black … 255 white). RGB: three channels Red, Green, Blue.
</details>

**Q22.** Image → features pipeline?
<details><summary>الجواب</summary>

Image → Feature Extraction → Shape, Texture, Edges, Color, Deep Features → Numerical Vector → classifier/clustering
</details>

**Q23.** Give spatial example coordinates from the lecture.
<details><summary>الجواب</summary>

Hospital H1 → (32.50, 45.82); H2 → (32.48, 45.85) — location features can be numericized.
</details>

**Q24.** Why is order important in sequence data? Give two examples.
<details><summary>الجواب</summary>

Sequences are ordered collections; reordering changes meaning. Examples: DNA `ACGT...`; `Login→Search→Product→Purchase`.
</details>

**Q25.** Graph embedding example from the lecture?
<details><summary>الجواب</summary>

Node A → [0.21, 0.75, 0.43]; Node B → [0.19, 0.81, 0.39] — numeric vectors representing nodes.
</details>

---

## 13.4 Similarity Graph + Distinctions + Pros/Cons

**Q26.** 🔴 How do you build a similarity graph from any data type?
<details><summary>الجواب</summary>

Define distance/similarity; **if distance(Pi,Pj) < threshold**, connect nodes; edges represent similarity.
</details>

**Q27.** Name four applications of similarity graphs.
<details><summary>الجواب</summary>

Clustering · Classification · Nearest-neighbor analysis · Outlier detection
</details>

**Q28.** 🔴 Distinguish data type portability from data mining.
<details><summary>الجواب</summary>

Portability: **how to represent** data suitably for an algorithm.  
Mining: **how to discover** useful patterns/knowledge.
</details>

**Q29.** Write the full lecture pipeline including conversion.
<details><summary>الجواب</summary>

Raw Data → Data Preparation → Data Type Conversion → Mining Algorithm → Patterns / Prediction / Knowledge
</details>

**Q30.** List five advantages of portability.
<details><summary>الجواب</summary>

Easier heterogeneous processing · reuse existing algorithms · simplify complex data · integrate sources · easier application of ML/DM algorithms
</details>

**Q31.** List six limitations of conversion.
<details><summary>الجواب</summary>

Information loss · loss of original structure · possible distortion of relationships · high-dimensional representations · extra computational cost · may not suit every algorithm
</details>

**Q32.** 🧠 Recite the conversion-matrix anchor.
<details><summary>الجواب</summary>

`Discretize · One-hot · Vectorize · Extract · Symbolize · Embed · Similarity-graph`
</details>

**Q33.** Doctor-style: outline CT/X-ray malignancy classification pipeline.
<details><summary>الجواب</summary>

CT/X-ray → feature extraction (texture, shape, edges, intensity/deep) → numerical vector → classification algorithm → malignant vs benign (or class label). State stages in order; use textbook feature names.
</details>

**Q34.** Why must conversion method depend on data and task?
<details><summary>الجواب</summary>

Because conversions trade suitability vs information loss/structure distortion; the wrong representation can hurt the mining task.
</details>

**Q35.** Week 02 link: Selection vs Extraction in one line each.
<details><summary>الجواب</summary>

Selection = **pick existing** attributes. Extraction = **create new** features from original data.
</details>

---

## 13.5 Rapid Oral Drill

1. Feature extraction definition?
2. X-ray pipeline stages?
3. Master matrix — name 6 techniques?
4. Blood type encoding + why not 1/2/3?
5. 21,22,39 after discretization?
6. Similarity graph construction rule?
7. Portability vs mining?
8. Five advantages / six limitations anchors?
9. Equal-width vs equal-frequency?
10. Doctor CT pipeline in order?

---

<a name="14"></a>
# 14. Cross-links to Week 02

| Topic | Full treatment | Week 03 use |
|:---|:---|:---|
| Attribute taxonomy | Week 02 §1 | Nominal reason for one-hot |
| 8 data structures | Week 02 §3 | Image/sequence/graph context |
| Data preparation 5 steps | Week 02 §4 | Portability sits beside transformation |
| Discretization | Week 02 §6.4 | Types + loss emphasized here |
| Encoding / one-hot | Week 02 §6.2 | Blood-type exam example |
| Feature Selection vs Extraction | Week 02 §7 | Week 03 is extraction + portability |
| Min-Max / Z-score | Week 02 §6.2 | Scaling remains transformation; not re-derived here |
| URL = Nominal | Week 02 §1.2 | Stays in Week 02 note |

---

# خاتمة سريعة

| Layer | One-line takeaway |
|:---|:---|
| **Feature Extraction** | Raw → new feature vector (X-ray: texture/shape/edges/intensity) |
| **Portability** | Convert types so algorithms can run |
| **Matrix** | Discretize · One-hot · Vectorize · Extract · Symbolize · Embed · Similarity-graph |
| **Risk** | Conversion can lose information — preserve what the task needs |
| **Distinction** | Portability = represent · Mining = discover patterns |
| **Doctor** | Ordered pipeline + textbook feature names + no filler |

---

*Built by Koko for Abu Al-Hasan — Week 03 comprehensive note (lighter companion to Week 02).*
*Lecture DOCX preserved in spirit; Aggarwal Ch 2.2 expansions labeled [Textbook]; Gemini method templates applied without re-compressing sources.*
*Next lecture material already staged; Cyber Sunday quiz remains first calendar priority.*
