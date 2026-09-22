# W03 Audit — Source & Precision Verification Addendum

> **Against:** `W03_Logical_Mathematical_Audit.md` (Codex)  
> **Method:** Direct extraction from lecture DOCX + Aggarwal Ch.2 text (equations read from source, not OCR).  
> **Verdict on Codex audit:** **PASS overall** — no critical math error. All **6 precision warnings are valid** and supported by source wording.  
> **This file does not change the lecture note history**; it locks the qualifications to use in final teaching/answers.

---

## A. Heat kernel & similarity graph — CONFIRMED from Aggarwal (local PDF)

**Source:** Aggarwal, *Data Mining: The Textbook*, Ch. 2 §2.2 (local scan ~p.60 / book p.34)

| Claim | Source evidence | Status |
|:---|:---|:---|
| Edge if $d(O_i,O_j) < \varepsilon$ | *“An edge exists between Oi and Oj, if the distance d(Oi,Oj) is less than a particular threshold ε.”* | **PASS** |
| kNN alternative; asymmetric → directed; drop directions/parallel edges | Same section | **PASS** |
| Heat kernel weight | $$w_{ij} = e^{-d(O_i,O_j)^2/t^2}$$ *“(2.1) Here, t is a user-defined parameter.”* | **PASS** |
| Larger weight = more similar | *“larger weights indicate greater similarity”* | **PASS** |
| Any type → graph is **conditional** | *“as long as an **appropriate distance function can be defined**”* + Table 2.1 *“Similarity graph (Restricted applicability)”* | **PASS — Codex #4 right** |
| Only for similarity/distance-based tasks | *“useful only for applications that are based on the notion of similarity or distances”* | **PASS** |

---

## B. Lecture DOCX checks (Week 03 booklet)

### 1. Equal-Width bins — Codex #1 **CONFIRMED valid**

**Lecture text:**
> Equal-Width Discretization — The numerical range is divided into intervals of approximately equal numerical size.  
> Example: Age 0–80 divided into: **0–20, 21–40, 41–60, 61–80**

**Assessment:** Lecture example is **integer-inclusive** (gaps at 20.5-style boundaries are not specified). Continuous case needs explicit interval convention.

**Safe wording to teach:**
> Integer ages: 0–20, 21–40, 41–60, 61–80.  
> Continuous: state half-open intervals, e.g. $[0,20), [20,40), \ldots$ (endpoint rule must be fixed).

**ML companion doc** uses `[0–20], [21–40], …` on Age 0–100 — same integer style.

---

### 2. Time series → symbols — Codex #2 **CONFIRMED valid**

**Lecture text:**
> Low = A · Medium = B · High = C  
> 20, 22, 21, 25, 27, 30 may become: **A, A, A, B, B, C**

**Assessment:** Mapping is **not** implied by the numbers alone. It depends on **Low/Medium/High cut-points**. Different thresholds ⇒ different symbol strings.

**Safe wording:**
> Given lecture labels Low/Medium/High (and their cutoffs), `20,22,21,25,27,30 → A,A,A,B,B,C`. Without cutoffs, symbolization is not unique.

---

### 3. Grayscale 0/255 — Codex #3 **CONFIRMED valid**

**Lecture text:**
> A grayscale image can be represented as a matrix of pixel intensities.  
> For a grayscale image: **0 → Black · 255 → White**

**Assessment:** This is the **common 8-bit** convention. Not universal (16-bit medical, float, etc.).

**Safe wording:**
> Under the common **8-bit** grayscale convention, 0 = black, 255 = white.

*(W02 structures note already used `H×W` matrix + 0–255 style; qualify the same way if written formally.)*

---

### 4. Any type → Graph — Codex #4 **CONFIRMED valid**

**Lecture text:**
> If distance(P1, P2) < threshold → Connect P1 and P2  
> Aggarwal Table 2.1: Any type → Graphs = Similarity graph **(Restricted applicability)**  
> Aggarwal: *“as long as an appropriate distance function can be defined”*

**Safe wording (exam):**
> Any type can become a **similarity graph only if** a suitable distance/similarity function exists **and** the task is similarity-based.

---

### 5. “Remove unnecessary information” — Codex #5 **CONFIRMED valid (lecture wording is loose)**

**Lecture text (Feature extraction can):**
> Reduce the amount of data.  
> **Remove unnecessary information.**  
> Represent important characteristics of the data.  
> Make data easier for algorithms to process.  
> Sometimes improve prediction or classification performance.

**Assessment:** Lecture **does** say “remove unnecessary information.” Formally, extraction mainly **transforms / summarizes / builds new features**; guaranteed removal of irrelevant columns is closer to **feature selection** / reduction.

**Safe wording (keep lecture meaning, add precision):**
> Feature extraction reduces/transforms representation and retains task-relevant characteristics; it may drop information judged unnecessary for the task (not the same as feature selection).

---

### 6. “One suitable form” / pipeline — Codex #6 **CONFIRMED valid**

**Lecture text:**
> Different Data Types → Data Type Conversion → **Suitable Representation** → Data Mining Algorithm

**Assessment:** “Suitable representation” is **algorithm-relative** (table, vector, sequence, graph, …) — not one universal numeric table.

**Safe wording:**
> … → a **representation compatible with the chosen algorithm** → mining algorithm.

---

## C. Formula sheet — locked for answers

```text
Similarity graph edge:   d(O_i, O_j) < ε
Heat kernel weight:      w_ij = exp( -d(O_i,O_j)^2 / t^2 ),  t user-defined
kNN graph:               directed possible; ignore direction; drop parallel edges
Condition:               appropriate distance function must exist (restricted applicability)
```

---

## D. Codex scorecard

| # | Point | Verdict | Source lock |
|:-:|:---|:---:|:---|
| 1 | Equal-Width integer vs continuous | **AGREE** | lecture 0–20,21–40… |
| 2 | TS symbols need thresholds | **AGREE** | Low=A, Medium=B, High=C |
| 3 | Grayscale 0–255 = 8-bit | **AGREE** | lecture 0→Black, 255→White |
| 4 | Any→Graph conditional | **AGREE** | Aggarwal restricted + distance fn |
| 5 | Extraction ≠ guaranteed remove | **AGREE** | lecture phrase vs selection |
| 6 | Suitable form = algo-fit repr. | **AGREE** | lecture pipeline wording |

**Heat kernel / ε rule / information-loss example:** Codex **PASS** — independently confirmed from Aggarwal text.

---

## E. Files

| File | Role |
|:---|:---|
| `W03_Logical_Mathematical_Audit.md` | Codex audit (unchanged) |
| `W03_Audit_Source_Verification.md` | This addendum (source locks) |
| `Week_03_Feature_Extraction_and_Portability.md` | Main note (historical content kept) |
| `Week_03_Hard_Points_Review.md` | Teaching map — use §F precision lines there |

---

*2026-09-22 · Source verification addendum · Koko*
