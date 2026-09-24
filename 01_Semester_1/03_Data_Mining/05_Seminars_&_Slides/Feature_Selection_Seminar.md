<!-- _class: lead -->

# Feature Selection Techniques
## اختيار الميزات — Data Mining (CS602)

Candidate: Master of Computer Science Student
Instructor: Asst. Prof. Dr. Ahmed Shakir Abd Al-Rida
Institution: College of Computer Science & IT — University of Wasit
Date: September 2026

---

# The One Problem

- A real table can carry hundreds of attributes — and most do not earn their place.
- Two different diseases (never merge them):
  - Irrelevant: no relationship to the target (e.g. a customer's telephone number).
  - Redundant: duplicates information already carried by another (age vs date of birth).
- Keeping them is actively harmful:
  - Poor-quality patterns — the algorithm fits noise.
  - Slow mining — every extra dimension costs computation.
- We cannot simply ask the expert — the data's behaviour is often not known.

---

# What Feature Selection Is — and What It Is Not

- Feature selection keeps a subset of the existing attributes and discards the rest.
- The family tree — memorise the direction of each:
  - Select: remove — keep a subset of existing columns (drop Phone).
  - Construct: add — build a new column from existing ones (area = height x width).
  - Extract: transform — build a new representation, new axes (PCA components).
  - Reduce: the umbrella — any strategy that shrinks the data.
- Exam sentence: selection picks from the shelf; extraction builds a new shelf.

---

# The Formal Goal

> "The goal of attribute subset selection is to find a minimum set of attributes such that the resulting probability distribution of the data classes is as close as possible to the original distribution obtained using all attributes." — Han, Kamber & Pei, p.104

- Unpack it into three testable pieces:
  - Minimum set: we minimise the fewest columns.
  - Class distribution preserved: we are constrained, not free.
  - Together: a trade-off, not a one-sided goal.
- Second, quieter benefit: interpretability — fewer attributes in the patterns makes them easier to read.

---

# Why It Is Hard — The 2-to-the-n Explosion

- For n attributes there are 2-to-the-n possible subsets.
- The numbers make "prohibitively expensive" concrete:
  - 20 features = 1,048,576 subsets.
  - 30 features = over a billion.
  - 50 features = over a quadrillion.
- So we use heuristic, greedy search:
  - Locally optimal choice at each step, hoping for a near-global optimum.
  - Greedy is not wrong — it is near-optimal with no guarantee.
- Exam line: exhaustive = optimal but impossible; greedy = possible but unguaranteed.

---

# How We Score a Feature — The Classical View

- Tests of statistical significance:
  - Best attributes are those whose link to the class is unlikely to be chance.
  - Key assumption: the attributes are independent — which breaks when two are redundant.
- Information gain (the decision-tree measure):
  - Gain(A) = H(C) minus the weighted entropy after splitting on A.
  - It measures how much uncertainty the attribute removes — higher is better.
  - It is exactly what a decision tree uses to split.
- Classification demands a class-sensitive criterion.

---

# The Filter Measures — Gini and Entropy

- Gini index (Eq. 10.1): G(v) = 1 minus the sum of squared class fractions.
  - 0 = perfect separation; 1 minus 1/k = maximum confusion (0.5 for two classes).
  - Lower is better.
- Entropy (Eq. 10.3): E(v) = minus the sum of p log2 p.
  - Range 0 to log2 k; 0 = perfect separation; higher = more mixing.
  - Lower is better.
- Why the logarithm: rare events carry more information; entropy is expected surprise.
- Both trace the same arch — 0 at the ends, peak at an even split.

---

# Fisher Score and Fisher's Linear Discriminant

- Fisher score (Eq. 10.5): the ratio of interclass separation to intraclass spread.
  - Numerator: how far the class means sit from the global mean.
  - Denominator: how wide each class is.
  - Higher is better — the opposite direction to Gini and entropy.
- Fisher's linear discriminant — the cousin that builds instead of selects:
  - It builds a new direction W (a linear combination), not a subset.
  - Supervised dimensionality reduction — not PCA.
  - The most discriminating direction is not the highest-variance direction.

---

# The Four Search Methods

- Stepwise forward selection: start from the empty set, add the best each step.
- Stepwise backward elimination: start from the full set, remove the worst each step.
- Combination: at each step, add the best and remove the worst.
- Decision tree induction (ID3, C4.5, CART):
  - The attributes that appear in the tree form the reduced subset.
  - Attributes that never earned a split are assumed irrelevant.
- All four converge on the same example subset {A1, A4, A6} — greedy searches agree.
- Stopping rule: a threshold on the evaluation measure — a design choice.

---

# Filter vs Wrapper vs Embedded

| Model | Who scores the feature? | Needs a classifier? |
|---|---|---|
| Filter | a fixed mathematical criterion | No — model-agnostic |
| Wrapper | the classifier's own accuracy | Yes — model-tied |
| Embedded | the model reveals it while training | Yes — built in |

- Wrapper: iteratively add features, train the classifier, keep or reject by accuracy.
- Embedded: a small weight in a linear model marks a weak feature; also Lasso and RFE.
- Which to use: speed and generality gives a filter; one specific classifier gives a wrapper; free selection during training gives embedded.

---

# Selection by Task — Classification vs Clustering

- Classification (supervised): a label exists, so the score is class-sensitive.
- Clustering (unsupervised): no label, so the score measures clustering tendency.
  - Distance distribution: uniform data gives one bell curve; clustered data gives two peaks.
  - Pick the subset that minimises the distance-distribution entropy.
- Three named clustering measures:
  - Term strength: P(t in Y given t in X) — for sparse text data.
  - Classification-based relevance: predict an attribute from the rest; accuracy is relevance.
  - Hopkins statistic: 0.5 = uniform; closer to 1 = clustered.

---

# Attribute Construction — The Cousin

> "In some cases, we may want to create new attributes based on others. Such attribute construction can help improve accuracy and understanding of structure in high-dimensional data." — Han, Kamber & Pei, p.105

- Sometimes the right move is to build a feature, not pick one.
  - area = height x width — a new column, same axes.
- Keep the three operations distinct:
  - Selection removes; Construction adds a column; Extraction changes the axes.
- Benefit: it can expose missing information about relationships between attributes.

---

# Exam Traps

- Selection chooses existing; extraction and construction create.
- Gini and entropy: lower is better; Fisher score: higher is better.
- Filter is model-free; wrapper is model-tied.
- Fisher score selects a feature; Fisher's discriminant builds a direction.
- Hopkins near 1 means clustered; 0.5 means uniform.

---

# The Whole Topic in Five Lines

- Too many features hurt — noise and redundancy.
- We want the smallest subset that preserves class information.
- There are 2-to-the-n subsets, so we score and search greedily.
- The score is a filter, or model-tied (wrapper or embedded).
- Selection chooses; construction and extraction create.

---

# References

- Han, Jiawei; Kamber, Micheline; Pei, Jian. Data Mining: Concepts and Techniques, 3rd ed. Morgan Kaufmann, 2011. Section 3.4.4 Attribute Subset Selection (pp. 103-105).
- Aggarwal, Charu C. Data Mining: The Textbook. Springer, 2015. Section 10.2 Feature Selection for Classification (pp. 287-293); Section 6.2 Feature Selection for Clustering (pp. 155-158).
- Figures used in the accompanying note: Fig 3.6 (Han, Kamber & Pei, p.104); Fig 10.1, 10.2 (Aggarwal, pp. 289, 291); Fig 6.1 (Aggarwal, p.156).
