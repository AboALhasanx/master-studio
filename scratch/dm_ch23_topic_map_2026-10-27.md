# Data Mining Chapters 2–3 topic-bank rebuild

Source set read: `Week 02 - Basic Data Types in Data Mining (v2).docx`, its Arabic line-by-line translation, and `Week 03 - Feature Extraction and Portability.docx`. Week 2's embedded equations are in Word Math: min–max normalization, its worked example, and z-score normalization. Preserve them as formulas rather than treating the blank text extraction as missing material.

The student requested Cyber Security-style topic banks instead of Model A/B. Bank boundaries follow the named material sections. Question counts are targets, to be adjusted to verified source coverage and quality rather than forced.

## Chapter 2 — Basic Data Types and Data Preparation

| Bank | Material coverage | Final questions |
|---|---|---:|
| T01 Data Objects, Attributes, and Attribute Types | Data object, attribute, nominal, ordinal, binary, numerical, discrete, continuous | 10 |
| T02 Data Structures and Mining Tasks | Record, transaction, text/document, sequence, temporal, spatial, image/multimedia, graph/network | 10 |
| T03 Data Preparation Foundations and Workflow | Definition, real-world quality conditions, five main steps, process order, task dependence, preparation vs preprocessing, medical example | 7 |
| T04 Missing Values and Noise | Why missing values matter, six missing-value methods and examples, noise definition/example, noise methods, binning and smoothing | 12 |
| T05 Outliers, Duplicates, Inconsistency, and Integration | Outlier meaning/handling, duplicate effects, standardizing inconsistent values, integration definition/use, five integration problems and unit example | 12 |
| T06 Data Transformation and Normalization | Transformation, scale, min–max formula/range/worked example, z-score formula/symbols, encoding and ordinal-code risk | 10 |
| T07 Data Reduction, Feature Selection, and Discretization | Reduction purpose and techniques, feature-selection example and distinction, PCA example/benefits, discretization and end-to-end medical workflow | 8 |

## Chapter 3 — Feature Extraction and Data Type Portability

| Bank | Material coverage | Final questions |
|---|---|---:|
| T01 Feature Extraction | Definition, raw-data difficulties, X-ray flow, distinct processing/performance benefits | 5 |
| T02 Data Type Portability Foundations | Definition, heterogeneous data, algorithm input forms, conversion map, full process, portability vs mining | 8 |
| T03 Numerical-to-Categorical Conversion | Discretization, examples, benefits, information loss, equal-width and equal-frequency methods/examples | 8 |
| T04 Categorical and Text Representations | One-hot encoding example/semantics, false order from numeric labels, text vectorization, document example, four approaches | 7 |
| T05 Time-Series Representations | Numerical feature extraction, feature list, symbolic mapping and example, DFT/DWT mapping | 7 |
| T06 Image, Spatial, Sequence, and Graph Representations | Pixel/RGB representations, image features, location features, sequence, graph embedding, similarity graph rule/applications | 12 |
| T07 Portability Benefits, Limitations, and Choice | Distinct benefits, limitations, and algorithm suitability | 8 |

## Final duplicate audit, gates, and release

- Final bank set: Ch2 **69 questions across 7 topic banks**; Ch3 **55 across 7**; **124 total**. Counts follow source coverage and distinct concepts, not a fixed target.
- Chapter-wide review found **124 unique concept IDs**, no exact English or Arabic stem duplicates, and no near-duplicate English stems at similarity ≥0.82. Both chapter quality gates pass with **0 structural errors, 0 editorial warnings, and 0 shape failures**.
- All 14 banks pass `quiz_balancer.py --check --strict`; v2/v3 validation, answer-index alignment, and `options == options_en` checks pass. The publisher dry-run found five unchanged Ch1 banks plus 14 new topic banks and no rejected files.
- The four previous Model A/B files were moved intact to `07_Quizzes_&_Anki/_retired/topic-bank-migration-2026-10-27/`, then hidden in the portal. Chapter 1 was not changed.
- Published and mirrored: portal content version **52**; Data Mining now has **19 banks across Chapters 1–3**. Pull updated the precache, so shell **1.7.12** was released and deployed. Portal CI passed **220 checks, 0 failed**. Live UI verification passed for both Ch2 and Ch3, including seven topic cards, numbered badges, language switching, launch shuffling, and stable correct-answer text.
- Source scope: Week 02 data types/preparation and Week 03 feature extraction/portability. The min–max expression uses the source's min/max form; graph roles follow the source's nodes/objects and edges/relationships mapping.
