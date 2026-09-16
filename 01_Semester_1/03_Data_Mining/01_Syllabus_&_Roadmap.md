# 🗺️ 16-Week Syllabus & Progress Roadmap: Data Mining

> **Course Code:** CS602  
> **Course Title:** Data Mining & Knowledge Discovery / *التنقيب عن البيانات واستخراج المعرفة*  
> **Instructor:** Asst. Prof. Dr. Ahmed Shakir Abd Al-Rida (*أ.م.د. أحمد شاكر عبد الرضا*)  
> **Credit Hours:** 2 Units | Weekly Time: Monday 08:30 AM – 10:30 AM  
> **Repository Directory:** `01_Semester_1/03_Data_Mining/`

---

## 1. Course Overview & Master Competency Matrix

Anchored in the classic Morgan Kaufmann curriculum by **Han, Kamber, and Pei**, this course guides postgraduate students through the complete Knowledge Discovery in Databases (KDD) lifecycle: from raw heterogeneous data ingestion, cleaning, and multidimensional OLAP reduction to advanced pattern mining, classification induction, and density-based clustering.

```
+=======================================================================================================+
|                                    16-WEEK PROGRESS TRACKER OVERVIEW                                  |
+=======================================================================================================+
| Completed Weeks: [ 0 / 16 ] | Progress: 0.0% | Status: Initializing Semester 1                        |
+=======================================================================================================+
```

---

## 2. Detailed 16-Week Chronological Roadmap

### 📊 Phase 1: Data Foundations, Attribute Math & Preprocessing (Weeks 1–4)

- [ ] **Week 01: Introduction to Data Mining, KDD Architecture & Motivating Challenges**
  - **Topics:** Why Data Mining? Data explosion problem, The Knowledge Discovery in Databases (KDD) multi-step lifecycle, Data Mining as the core algorithmic step in KDD, Database/Warehouse/Stream data sources, Major challenges in big data analytics.
  - **Primary Materials:** Han & Kamber Chapter 1 (`02_Raw_Materials/Data Mining Textbook.pdf`) + `Week 01 - Introduction to Data Mining.pptx`.
  - **Deliverables:** KDD Lifecycle flow diagram (Mermaid) in `03_Study_Notes/Week_01_KDD_Lifecycle.md`.
  - **Self-Assessment:** Contrast OLTP database querying with exploratory data mining along 4 operational dimensions.

- [ ] **Week 02: Getting to Know Your Data — Data Objects & Attribute Taxonomy**
  - **Topics:** Data Objects (records, tuples), Formal Attribute Definitions: Nominal, Binary (Symmetric vs. Asymmetric), Ordinal, Numeric (Interval-Scaled vs. Ratio-Scaled), Discrete vs. Continuous attributes.
  - **Primary Materials:** Han & Kamber Chapter 2 + `Week 02 - Basic Data Types in Data Mining (v2).docx` + Arabic Translation Doc.
  - **Deliverables:** Complete Attribute Classification Matrix in `03_Study_Notes/Week_02_Attribute_Taxonomy.md`.
  - **Self-Assessment:** Classify 15 real-world computer science variables into their exact attribute tier with formal justification.

- [ ] **Week 03: Statistical Data Descriptions & Measuring Similarity/Dissimilarity**
  - **Topics:** Measuring Central Tendency (Mean, Median, Mode, Midrange), Dispersion (Range, Quartiles, IQR, Variance, Standard Deviation), Boxplots, Quantile plots, Scatter plots. Proximity metrics: Euclidean, Manhattan, Minkowski ($L_p$), Supremum ($L_\infty$), Cosine similarity for document vectors, Jaccard coefficient.
  - **Primary Materials:** Han & Kamber Chapter 2 (Sections 2.2–2.4).
  - **Deliverables:** Distance Metric derivation and computation worksheet in `03_Study_Notes/`.
  - **Self-Assessment:** Compute Euclidean, Manhattan, and Cosine similarity across a 4-object, 3-dimensional vector set.

- [ ] **Week 04: Data Preprocessing — Data Cleaning Strategies & Noise Smoothing**
  - **Topics:** Why preprocess data? Dirty data consequences. Handling Missing Values (Ignore tuple, manual fill, global constant, attribute mean/median, most probable Bayesian value). Smoothing Noisy Data: Binning methods (Equal-width, Equal-frequency, Smoothing by bin means/medians/boundaries), Regression, Clustering for outlier detection.
  - **Primary Materials:** Han & Kamber Chapter 3 (Section 3.2).
  - **Deliverables:** Binning and Noise Smoothing step-by-step calculation notes.
  - **Self-Assessment:** Perform Equal-frequency binning and boundary smoothing on a 12-value dataset.

---

### ⚙️ Phase 2: Integration, Reduction & Transformation Mathematics (Weeks 5–8)

- [ ] **Week 05: Data Integration & Redundancy Analysis ($\chi^2$, Pearson, Covariance)**
  - **Topics:** Handling schema integration & entity identification, Correlation analysis for categorical attributes: Chi-Square ($\chi^2$) test for independence, Correlation analysis for numeric attributes: Pearson Correlation Coefficient ($r_{A,B}$), Covariance ($\text{Cov}(A,B)$), Detecting duplicate records.
  - **Primary Materials:** Han & Kamber Chapter 3 (Section 3.3).
  - **Deliverables:** Chi-Square and Pearson correlation solved problem sets in `03_Study_Notes/`.
  - **Self-Assessment:** Calculate $\chi^2$ statistic for a $2 \times 2$ contingency table and verify statistical independence at $p = 0.05$.

- [ ] **Week 06: Data Reduction & Feature Engineering (PCA & Wavelet Compression)**
  - **Topics:** Dimensionality Reduction: Principal Component Analysis (PCA), Discrete Wavelet Transforms (DWT), Feature Selection / Attribute Subset Selection (Forward selection, Backward elimination, Decision tree induction). Numerosity Reduction: Parametric (Regression, Log-Linear models) vs. Non-parametric (Histograms, Clustering, Sampling). Feature extraction from signals (e.g. X-ray texture, Haralick features).
  - **Primary Materials:** Han & Kamber Chapter 3 (Section 3.4) + `Week 03 - Feature Extraction and Portability.docx`.
  - **Deliverables:** Feature engineering and PCA workflow summary in `03_Study_Notes/`.
  - **Self-Assessment:** Outline the 5 mathematical steps of PCA from covariance matrix computation to eigenvalue sorting.

- [ ] **Week 07: Data Transformation & Discretization (Min-Max, Z-score, Decimal Scaling)**
  - **Topics:** Normalization techniques: Min-Max normalization, Z-score normalization (standard deviation vs. mean absolute deviation $s_A$), Normalization by decimal scaling. Data discretization: Concept hierarchy generation for numeric (binning, histogram analysis, cluster analysis) and categorical data.
  - **Primary Materials:** Han & Kamber Chapter 3 (Section 3.5).
  - **Deliverables:** Data Normalization Solved Drills in `03_Study_Notes/Week_07_Normalization_Drills.md`.
  - **Self-Assessment:** Transform a raw attribute vector using Min-Max, Z-score ($s_A$), and Decimal scaling; compare outlier sensitivity.

- [ ] **Week 08: Midterm Examination & Data Preparation Synthesis**
  - **Exam Focus:** Comprehensive examination on Weeks 1–7 (Attribute classification, distance metrics, data cleaning, Chi-square tests, manual normalization calculations).
  - **Weight:** 30% of coursework grade.
  - **Deliverables:** Midterm exam debrief and error log updates in `LEARNER_MODEL.md`.

---

### 🛒 Phase 3: Frequent Pattern Mining & Association Rules (Weeks 9–11)

- [ ] **Week 09: Frequent Pattern Mining — Basic Concepts, Support & Confidence**
  - **Topics:** Market Basket Analysis, Itemsets, Support count $\sigma(X)$, Minimum support threshold $minsup$, Minimum confidence threshold $minconf$, Mathematical definition of Association Rules: $A \Rightarrow B$ where $A \cap B = \emptyset$. Support: $P(A \cup B)$, Confidence: $P(B|A) = \frac{\text{support}(A \cup B)}{\text{support}(A)}$.
  - **Primary Materials:** Han & Kamber Chapter 6 (Section 6.1).
  - **Deliverables:** Association rule formulation notes in `03_Study_Notes/`.
  - **Self-Assessment:** Calculate support and confidence for all 2-item candidate rules in a 5-transaction database.

- [ ] **Week 10: The Apriori Algorithm — Join, Prune & Strong Rule Extraction**
  - **Topics:** The Apriori Principle (Downward closure property of support), Apriori algorithm step-by-step: Candidate generation $C_k = L_{k-1} \bowtie L_{k-1}$, Pruning non-frequent subsets, Generating strong association rules exceeding $minconf$, Improving Apriori efficiency (Hash-based itemset counting, Transaction reduction, Partitioning, Dynamic itemset counting).
  - **Primary Materials:** Han & Kamber Chapter 6 (Section 6.2).
  - **Deliverables:** Full manual trace of Apriori algorithm across 4 iterations in `03_Study_Notes/Apriori_Trace.md`.
  - **Self-Assessment:** Trace candidate generation $C_3$ and pruning from $L_2 = \{\{1,2\}, \{1,3\}, \{1,4\}, \{2,3\}, \{2,4\}\}$.

- [ ] **Week 11: Advanced Frequent Pattern Mining — FP-Growth & Closed/Maximal Itemsets**
  - **Topics:** Why Apriori bottlenecks (multiple database scans, candidate explosion). The FP-Growth (Frequent Pattern Growth) algorithm: Constructing the FP-Tree, Mining frequent itemsets without candidate generation via conditional pattern bases. Closed itemsets vs. Maximal frequent itemsets.
  - **Primary Materials:** Han & Kamber Chapter 6 (Section 6.3) & Chapter 7.
  - **Deliverables:** FP-Tree construction diagram in `06_Diagrams_&_Mindmaps/`.
  - **Self-Assessment:** Construct an FP-tree for a transactional dataset and extract conditional pattern bases.

---

### 🌲 Phase 4: Classification, Clustering & Advanced Mining (Weeks 12–16)

- [ ] **Week 12: Classification Foundations — Decision Tree Induction**
  - **Topics:** What is classification? Supervised vs. Unsupervised learning. Decision Tree Induction: Attribute Selection Measures (ASM), Information Gain (ID3 / Shannon Entropy), Gain Ratio (C4.5), Gini Index (CART). Tree pruning (Pre-pruning vs. Post-pruning), Handling continuous attributes and missing values.
  - **Primary Materials:** Han & Kamber Chapter 8 (Sections 8.1–8.2).
  - **Deliverables:** Decision Tree induction calculation sheet in `03_Study_Notes/`.
  - **Self-Assessment:** Calculate Entropy $Info(D)$ and Information Gain $Gain(A)$ for a candidate split attribute.

- [ ] **Week 13: Advanced Classification — Naive Bayes, Rule-Based & Ensemble Methods**
  - **Topics:** Bayes' Theorem: $P(H|X) = \frac{P(X|H)P(H)}{P(X)}$, Naive Bayesian Classifier (Class-conditional independence assumption), Zero-probability problem and Laplace correction. Rule-Based classification (IF-THEN rules, Coverage & Accuracy). Ensemble methods: Bagging, Boosting (AdaBoost), Random Forests. Model evaluation metrics (Accuracy, Precision, Recall, F1-Score, ROC curves).
  - **Primary Materials:** Han & Kamber Chapter 8 (Sections 8.3–8.6).
  - **Deliverables:** Naive Bayes probability calculation drills in `03_Study_Notes/`.
  - **Self-Assessment:** Classify a test instance using Naive Bayes with Laplacian smoothing on categorical features.

- [ ] **Week 14: Cluster Analysis Foundations — Partitioning Methods (K-Means & K-Medoids)**
  - **Topics:** What is Cluster Analysis? Requirements for cluster analysis in data mining. Partitioning methods: K-Means algorithm (Centroid updating, Sum of Squared Errors SSE convergence), Strengths and limitations of K-Means (sensitivity to outliers and initialization). K-Medoids / PAM (Partitioning Around Medoids) and CLARA for scalability.
  - **Primary Materials:** Han & Kamber Chapter 10 (Sections 10.1–10.2).
  - **Deliverables:** K-Means manual trace and convergence plot in `03_Study_Notes/`.
  - **Self-Assessment:** Execute 2 iterations of K-Means clustering on 8 2D coordinate points.

- [ ] **Week 15: Advanced Clustering & Outlier Detection (Hierarchical & Density-Based)**
  - **Topics:** Hierarchical clustering: Agglomerative (AGNES) vs. Divisive (DIANA), Linkage criteria (Single, Complete, Average). Density-Based clustering: DBSCAN (Core points, Border points, Noise, $\epsilon$-neighborhood, $MinPts$). Outlier detection: Density-based local outlier factor (LOF) vs. Statistical distance-based approaches.
  - **Primary Materials:** Han & Kamber Chapter 10 (Sections 10.3–10.4) & Chapter 12.
  - **Deliverables:** Clustering algorithm comparison matrix in `03_Study_Notes/`.
  - **Self-Assessment:** Trace DBSCAN cluster expansion and distinguish noise points from border points.

- [ ] **Week 16: Comprehensive Review & Final Semester Examination**
  - **Activities:** Comprehensive mock exam covering the full Han & Kamber syllabus: data preprocessing calculations, Apriori traces, Information Gain derivations, and clustering mechanics.
  - **Deliverables:** 100-Question Data Mining Anki deck export in `07_Quizzes_&_Anki/`.
  - **Final Target:** Score $\ge 90\%$ (Distinction / *امتياز*).

---

## 3. Assessment & Grading Criteria

| Component | Weight | Target Score | Description |
|:---|:---:|:---:|:---|
| **Homework Problem Sets & Mathematical Drills** | 10% | 10% | Weekly step-by-step arithmetic and normalization assignments |
| **Applied Feature Engineering Assignment** | 15% | 14% | Domain data preprocessing and feature extraction report |
| **Oral Seminar Presentation (Marp Delivery)** | 15% | 14% | 10-slide academic presentation on advanced mining algorithm |
| **Midterm Examination (Week 08)** | 20% | 19% | Written exam on Weeks 1–7 (Math & Definitions) |
| **Final Semester Examination (Week 16)** | 40% | 36% | Comprehensive written examination |
| **Total Course Grade** | **100%** | **$\ge 93\%$** | **Grade Target: High Distinction (امتياز مرتفع)** |
