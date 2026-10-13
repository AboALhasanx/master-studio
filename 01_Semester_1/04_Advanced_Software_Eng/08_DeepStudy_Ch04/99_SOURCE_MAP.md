# SOURCE MAP — Ch04 (Software Project Planning) — خريطة مرجعية سريعة
### اللي يربط السؤال بمصدره

## أين تجد الأشكال والجداول الأصلية

| الشكل/الجدول | الموضوع | سلايد |
|---|---|---|
| **Fig 1** | Activities during software project planning | 4 |
| **Fig 2** | Function for sorting an array (=18 LOC, مثال LOC) | 5 |
| **Fig 3** | FPA's functional units (System, User, Other apps) | 11 |
| **Table 1** | Functional units with weighting factors | 16 |
| **Table 2** | UFP calculation table (Low/Avg/High × 3/4/6, 4/5/7, 3/4/6, 7/10/15, 5/7/10) | 17 |
| **Table 3** | Computing function points (14 factors F1–F14، تقييم 0–5) | 21 |
| **Table 4** | Comparison of three COCOMO modes | 43 |
| **Table 4(a)** | Basic COCOMO coefficients (a_b, b_b, c_b, d_b) | 45 |
| **Table 5** | Multiplier values for effort (15 driver) | 56 |
| **Table 6** | Coefficients for intermediate COCOMO | 57 |
| **Table 7** | Effort & schedule fractions (phase distribution) | 62, 63, 71 |
| **Fig 4** | Categories of applications/projects (COCOMO II) | 73 |
| **Table 8** | Stages of COCOMO-II (4 categories × 3 stages) | 74 |
| **Fig 5** | Steps for estimation of effort in person-months (App. Composition) | 75 |
| **Table 9(a)(b)** | Complexity weights for screens / reports | 76, 77 |
| **Table 10** | Complexity weights for each level (object points) | 78 |
| **Table 11** | Productivity values (PROD) | 80 |
| **Table 12** | Scaling factors for calculation of B (5 factors) | 86, 87 |
| **Table 13** | Data for computation of B (numeric ratings) | 88 |
| **Table 14** | Mapping table (early ↔ post-architecture drivers) | 93 |
| **Table 15** | Early design parameters (7 cost drivers) | 101 |
| **Table 16** | Post-Architecture Cost Driver rating level summary (17 drivers) | 107–110 |
| **Table 17** | Module complexity ratings | 112–114 |
| **Table 18** | 17 cost drivers (numeric values) | 115, 116 |
| **Table 19** | Converting function points to lines of code | 118–120 |
| **Table 20** | Manpower versus development time (trade-off) | 150 |
| **Fig 6** | The Rayleigh manpower loading curve | 123 |
| **Fig 7** | Influence of parameter 'a' on manpower distribution | 129 |
| **Fig 8** | Project life cycle (dev + test/validation curves) | 151 |
| **Fig 9** | Risk Management Activities | 190 |

## الجداول الحاسمة (احفظها غيباً)

### الجدول A — UFP weights (سلايد 17 / كتاب ص.147)
| Functional Unit | Low | Average | High |
|---|---|---|---|
| External Inputs (EI) | 3 | 4 | 6 |
| External Outputs (EO) | 4 | 5 | 7 |
| External Inquiries (EQ) | 3 | 4 | 6 |
| Internal Logical Files (ILF) | 7 | 10 | 15 |
| External Interface Files (EIF) | 5 | 7 | 10 |

**المعادلات:**
- `UFP = ΣΣ (Zij × wij)`  — (i: صف الوحدة، j: مستوى التعقيد، Z: العدد، w: الوزن)
- `CAF = 0.65 + 0.01 × ΣFi`  —  (Fi من 14 عامل، كل واحد 0←5 ⇒ ΣFi من 0 إلى 70 ⇒ CAF من 0.65 إلى 1.35)
- `FP = UFP × CAF`

**مقاييس مشتقة من FP:** `Productivity = FP / person-months` · `Quality = Defects / FP` · `Cost = $ / FP` · `Documentation = pages of documentation / FP`

### الجدول B — Basic COCOMO coefficients (سلايد 45 / كتاب ص.152)
| Mode | a_b | b_b | c_b | d_b |
|---|---|---|---|---|
| Organic | 2.4 | 1.05 | 2.5 | 0.38 |
| Semidetached | 3.0 | 1.12 | 2.5 | 0.35 |
| Embedded | 3.6 | 1.20 | 2.5 | 0.32 |

**المعادلات:** `E = a_b(KLOC)^b_b` · `D = c_b(E)^d_b` · متوسط الفريق `SS = E/D` · `P = KLOC/E`

**اختيار الموديل (سلايد 43):** Organic = مشروع صغير/فريق صغير/بيئة مألوفة · Semidetached = وسط (حجم متوسط، خبرة متوسطة) · Embedded = معقّد، قيود صارمة (hardware/tight constraints)، حجم كبير.

### الجدول C — Intermediate COCOMO coefficients (سلايد 57 / كتاب ص.156)
| Mode | a_i | b_i | c_i | d_i |
|---|---|---|---|---|
| Organic | 3.2 | 1.05 | 2.5 | 0.38 |
| Semidetached | 3.0 | 1.12 | 2.5 | 0.35 |
| Embedded | 2.8 | 1.20 | 2.5 | 0.32 |

**المعادلة:** `E = a_i(KLOC)^b_i × EAF` · `D = c_i(E)^d_i`

**⚠️ انتبه:** a في Intermediate **مختلف** عن a في Basic (3.2 vs 2.4 للـorganic، 2.8 vs 3.6 للـembedded) — لأن الـEAF يعوّض الفرق.

**15 cost driver (سلايد 53–56) — 4 مجموعات:**
| المجموعة | Drivers |
|---|---|
| Product | RELY (reliability) · DATA (database size) · CPLX (complexity) |
| Hardware/Computer | TIME (execution time) · STOR (main storage) · VIRT (virtual machine volatility) · TURN (turnaround time) |
| Personnel | ACAP (analyst capability) · AEXP (application experience) · PCAP (programmer capability) · VEXP (VM experience) · LEXP (language experience) |
| Project | MODP (modern programming practices) · TOOL (use of tools) · SCED (required schedule) |

### الجدول D — Putnam / Norden-Rayleigh (سلايد 123–156)
| الحد | الصيغة |
|---|---|
| Rayleigh curve `m(t)` | `m(t) = 2·K·a·t·e^(-a·t²)` (مع a = 1/(2td²) ⇒ `m(t)= (2K·t/td²)·e^(-t²/td²)`) — **شكل السلايد 128** |
| Cumulative `y(t)` | `y(t) = K[1 − e^(-a·t²)]` = `K[1 − e^(-t²/td²)]` |
| Peak time | `td = 1/√(2a)` |
| Peak manning | `m₀ = K/(td·e)`  (e=2.71828) |
| Difficulty | `D = K/td²`  [person/year] |
| Manpower build-up | `D₀ = K/td³`  [person/year²] |
| D₀ values | **8** = جديد بتفاعلات كثيرة · **15** = جديد standalone · **27** = إعادة بناء من موجود |
| Size/technology | `S = C·K^(1/3)·td^(4/3)` · `C = S·K^(-1/3)·td^(-4/3)` |
| Productivity vs difficulty | `P ∝ D^(-2/3)` |
| Dev. sub-cycle | `Kd = K/6` · `tod = td/√6` · 95% rule: `yd(td)=0.95·Kd` |
| Average rate | `m₀/td` |
| Technology factor C range | 610 – 57314 |

**MCQ المرتبطة:** 4.7 (Putnam based on Norden/Rayleigh) · 4.8 (manpower buildup = **K/td³ persons/year²** = option b) · 4.22 (Rayleigh eq = **2Kat·e^(−at²)** = option c — سلايد 125 حرفياً) · 4.23 (technology factor = **SK^(−1/3)·td^(−4/3)** = option a).

### الجدول E — COCOMO II (سلايد 73–120)
- **4 فئات** (Fig 4): End-user programming · Infrastructure · Application generators · System integration
- **3 مراحل** (Table 8): ① Application Composition ② Early Design ③ Post-Architecture
- **Application Composition:** `NOP = (object points) × (100 − %reuse)/100` · `Effort = NOP/PROD` (PROD من Table 11)
- **Early Design:** `PM_nominal = 2.5 × size^B` · `B = 0.91 + 0.01 × Σ(rating of 5 scale factors)` ← **النطاق 0.91←1.23**
  - 5 scale factors: Precedentness · Development flexibility · Architecture/risk resolution · Team cohesion · Process maturity
  - `PM_adjusted = PM_nominal × Π(7 EMs)` — 7 early design drivers: RCPX, RUSE, PDIF, PERS, PREX, FCIL, SCED
- **Post-Architecture:** `PM_adjusted = PM_nominal × Π(17 EMs)` — 17 drivers (Table 18)
- **Schedule:** `TDEV = [φ × (PM_adjusted)^(0.28+0.2×(B−0.91))] × SCED%` — φ = 3.67
- **FP→LOC** (Table 19): 128 C · 29 C++ · 91 Pascal · 80 Report Generator · 6 Spreadsheet · 53 Ada · 71 AI Shell…

### الجدول F — Empirical models (سلايد 36 / كتاب ص.??)
| Model | Effort | Duration | Docs |
|---|---|---|---|
| Walston-Felix | `E = 5.2·L^0.91` | `D = 4.1·L^0.36` | — |
| SEL / Doty | `E = 1.4·L^0.93` | `D = 4.6·L^0.26` | `DOC = 30.4·L^0.90` |
(L = KLOC، E = person-months)

**ملاحظة:** لاحظ الفرق — Walston-Felix يعطي **LOC أقل لنفس الجهد** (لأن a=5.2 أكبر)، SEL أكثر تفاؤلاً.

### الجدول G — Risk Management (سلايد 180–193 / كتاب §4.7)
- **تعريف:** "Risk is a problem that may cause some loss or threaten the success of the project, but which has not happened yet."
- **تصنيفات Jones الخمسة:** ① Dependencies on outside agencies ② Requirement issues ③ Management issues ④ Lack of knowledge ⑤ Other (testing facilities, staff turnover, unachievable performance…)
- **الأنشطة** (Fig 9): 2 فئات كبيرة:
  - **Risk Assessment:** Identification → Analysis → Prioritization
  - **Risk Control:** Management Planning → Monitoring → Resolution
- **Risk exposure** = (probability of loss) × (magnitude of loss)
- **Risk avoidance** = لا تسوي الشغلة الخطرة (لا تختار المشروع الخطر / استخدم تقنية مُثبتة)

## ⚠️ فخاخ ترقيم بالسلايدات (تم التحقق بصرياً)

- **MCQ:** سلايد 194 فيه 4.1–4.4، وبعدها سلايد 195 يبدأ بـ4.5 **مطبوع بعد 4.6/4.7** (انقلاب تنسيقي — الرقم 4.5 يظهر بين 4.7 و4.8). الترتيب الصحيح: 4.1←4.25.
- **MCQ 4.8 / 4.22 / 4.23:** الخيارات **معادلات** (المستخرج النصي يخربطها) — تحققت بصرياً (render).
- **Exercises:** ترقيم سلايد 205–206 **مبعثر** (4.24, 4.25, 4.27, 4.26, 4.23, 4.28…). الرقم 4.23 يظهر متأخراً. الترتيب الصحيح 4.1←4.36.
- **ماكو تمرين 4.23 بالوحل** — التمارين مو كلها متسلسلة على السلايد.

## مسار المجلدات

```
04_Advanced_Software_Eng/
├── 02_Raw_Materials/
│   ├── Aggarwal_Singh_Slides/chapter_4_software_project_planning.pdf   (207 سلايد)
│   ├── Aggarwal_Singh_SE_3rd_ed_By_Chapter/Ch04_Software_Project_Planning.pdf
│   ├── Aggarwal_Singh_Slides/exam_papers/03_Planning_References/  (4 مراجع)
│   └── Reference_Textbooks/AliFahim_Software_Engineering.pdf  (سكان، فصل Planning = PDF 76–130 = مطبوع 140–196)
└── 08_DeepStudy_Ch04/                          (هذا المجلد — الساندبوكس)
    ├── 00_STUDY_SYSTEM.md
    ├── 01_TIER1_MODEL_QUESTIONS.md
    ├── 02_TIER2_DEEP_QUESTIONS.md
    ├── 03_EXTERNAL_QUESTIONS_AND_DEEPER_CONTENT.md
    ├── 04_EXAM_PATTERN_BANK.md
    ├── 99_SOURCE_MAP.md
    └── ByType/  (T1..T7 + 00_INDEX)
```


---

## Retrieval set (active recall)

| السؤال | الجواب |
|---|---|
| جدول UFP (ILF)؟ | 7/10/15 |
| معاملات basic COCOMO (organic)؟ | a=2.4 b=1.05 c=2.5 d=0.38 |
| معاملات intermediate (organic)؟ | a=3.2 b=1.05 (a مختلف!) |
| قيم D₀؟ | 8 / 15 / 27 |
| عدد scale factors / EM early / EM post؟ | 5 / 7 / 17 |
| مدى technology factor C؟ | 610 – 57314 |
| فصل Planning بالكتاب؟ | مطبوع 140–196 = PDF 76–130 |

---
*بُني 2026-10-12*