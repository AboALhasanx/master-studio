# Data Mining - Matched End-of-Chapter Questions (Local Chapters 1-8)

> **Purpose:** one combined question-and-solution pack of textbook end-of-chapter exercises that match the taught Data Mining material in local Chapters 01-08.
> **Sources:** Han, Kamber & Pei, *Data Mining: Concepts and Techniques*, 3rd ed.; Charu C. Aggarwal, *Data Mining: The Textbook*.
> **Use:** prompts below preserve the exercise task, supplied data, and conditions in concise source-faithful wording. They are paraphrased study prompts, not copied solution-manual text. The answers are independently derived from the local course notes/lectures and the textbooks. No instructor solution manual was available or used.

## How the match score was assigned

Each exercise or subpart is compared on four dimensions: (1) same concept/algorithm, (2) assumptions and notation taught locally, (3) required depth/calculation, and (4) no dependence on untaught material. Keep only parts estimated at **60-100%**. A mixed exercise is split; excluded subparts are named rather than silently treated as covered. Scores are screening estimates, not official course weights.

**Score bands:** 90-100% direct/strong match; 80-89% strong match with a small extension; 60-79% partial but answerable from the local material; below 60% excluded.

## Chapter map

| Local chapter | Main local material | Textbook sources represented |
|:--|:--|:--|
| 01 Introduction | KDD, mining tasks, applications, challenges | Han Ch1 |
| 02 Data Types & Preparation | data types, quality, cleaning, integration, normalization, discretization, reduction | Han Ch2-3; Aggarwal Ch2 |
| 03 Feature Extraction & Portability | heterogeneous data representation, vectors, similarity, text/time-series/spatial data | Aggarwal Ch2-3; Han Ch2 |
| 04 Feature Selection | subset search, forward/backward/combined search, split criteria as feature scoring | Han Ch3; Aggarwal Ch10 |
| 05 Association & Frequent Patterns | support/confidence, Apriori, FP-Growth, closed/maximal sets, rule measures | Han Ch6-7; Aggarwal Ch4-5 |
| 06 Classification Foundations | decision trees, split criteria, pruning, evaluation | Han Ch8; Aggarwal Ch10 |
| 07 Classification Methods | rules, Naive Bayes, logistic regression, ensemble concepts | Han Ch8; Aggarwal Ch10 |
| 08 Clustering | K-means, hierarchical, DBSCAN, GMM, cluster choice/evaluation | Han Ch10; Aggarwal Ch6 |

---

# Chapter 01 - Introduction

## Han Ch1, Exercises 1.1-1.10 - 80-100% match

### 1.1 - Data mining and KDD (90%)

**Question.** Explain what data mining contributes to KDD; relate it to database technology, statistics, machine learning, and pattern recognition; outline how these fields contributed to its development; and describe the KDD process.

**Answer.** Data mining is the step that discovers useful patterns/models from prepared data; KDD is the broader process of selecting, cleaning, transforming, mining, evaluating, and presenting knowledge. Databases provide storage/query/management; statistics provides estimation and inference; machine learning provides predictive and descriptive algorithms; pattern recognition contributes feature-based classification and discovery. The fields developed in parallel and converged as large digital repositories and practical computing made automated discovery useful. A safe KDD sequence is: data cleaning → integration → selection → transformation → data mining → pattern evaluation → knowledge presentation. It is iterative: evaluation can send the analyst back to earlier steps.

### 1.2 - Database versus data warehouse (90%)

**Question.** Distinguish a database from a data warehouse in purpose, data organization, and typical analysis.

**Answer.** Operational databases support current transactions and frequent inserts/updates; they are organized around applications and normalized records. A warehouse integrates historical, often subject-oriented data from multiple sources and is optimized for analytical queries, summaries, and decision support. A warehouse does not replace the operational database; it supports a different workload.

### 1.3 - Mining task definitions and examples (100%)

**Question.** Define characterization, discrimination, association/correlation analysis, classification, regression, clustering, and outlier analysis; give a plausible example for each.

**Answer.** Characterization summarizes a target group (typical buyers); discrimination contrasts target and reference groups (buyers versus non-buyers); association discovers co-occurring items (bread with milk); classification predicts a discrete class from labelled examples (fraud/not fraud); regression predicts a numeric value (house price); clustering groups unlabeled objects by similarity (customer segments); outlier analysis finds objects that differ substantially from the general pattern (unusual transaction). Examples are illustrative; the predicted target type distinguishes classification from regression.

### 1.4 - Business use and limits (80%)

**Question.** Give a business case for data mining, identify useful mining functions, and explain why mining is not simply database querying or conventional statistics.

**Answer.** A retailer can use purchase histories to segment customers, forecast demand, find product associations, and detect unusual transactions. A query returns records matching a specified condition; mining searches for previously unknown regularities or predictive structure. Statistics supplies principled summaries/inference and is one foundation, while data mining combines it with scalable algorithms, machine learning, database operations, and domain-driven discovery. Mining still requires sound sampling, validation, interpretation, and privacy controls.

### 1.5 - Distinguish related mining tasks (90%)

**Question.** Compare discrimination with classification, characterization with clustering, and classification with regression.

**Answer.** Discrimination describes differences between predefined groups; classification learns a model that assigns a class label to new records. Characterization summarizes one group; clustering creates groups from similarity without supplied labels. Classification predicts categorical outcomes; regression predicts continuous numeric outcomes. A task can combine descriptive and predictive stages, but their outputs differ.

### 1.6 - Propose a useful knowledge type (80%)

**Question.** Propose one useful knowledge type beyond the listed mining functions and explain its output and application.

**Answer.** A temporal change pattern is a defensible extension: it describes how a statistic or relationship changes over time, for example seasonal demand shifts. It needs time-stamped observations and produces trends, change points, or recurring temporal patterns. This is an open design prompt; other well-defined and useful patterns can earn full credit.

### 1.7 - Outlier detection applications (90%)

**Question.** Recommend outlier-detection approaches for fraud and for identifying unreliable measurements; discuss how confidence in the flagged cases differs.

**Answer.** For fraud, use validated historical labels if available, plus anomaly scores or peer-group comparisons to surface previously unseen behavior; investigate alerts before action because legitimate rare activity also looks unusual. For sensor/lab reliability, use physical bounds, replicate measurements, robust statistical residuals, and instrument-quality checks. Confidence depends on evidence: repeated independent signals and confirmed labels support stronger conclusions than a single distance-based flag. An outlier is a candidate for investigation, not proof of fraud or error.

### 1.8 - Methodology and interaction challenges (80%)

**Question.** Identify three challenges in mining methodology or user interaction and explain their effect.

**Answer.** (1) Mining diverse data types requires suitable representations and algorithms; otherwise relevant structure is lost. (2) User constraints and domain knowledge must be expressible without hiding unexpected patterns. (3) Pattern evaluation and presentation must control the number of results and make them interpretable. Other defensible challenges include privacy, data quality, scalability, and interactive exploration.

### 1.9 - Large versus small datasets (80%)

**Question.** Explain how large-scale mining changes the computational and statistical challenges compared with a small dataset.

**Answer.** Large data stresses memory, I/O, communication, runtime, and distributed coordination; algorithms need scalable scans, summaries, parallelism, or incremental updates. Small data is easier to process but estimates can have high variance and poor coverage; large data can improve precision while amplifying systematic bias, dependence, and data-quality problems. Size alone does not ensure representative or valid results.

### 1.10 - Domain-specific challenge (80%)

**Question.** Choose an application domain and describe a concrete mining challenge and a mitigation.

**Answer.** In medical prediction, missingness, class imbalance, changing measurement practices, privacy, and the high cost of false negatives can invalidate a seemingly accurate model. Use careful cohort definition, leakage-free validation, class-sensitive metrics, calibration, privacy safeguards, and clinical review. This is an open-response exercise; the answer must connect the challenge to the chosen domain.

---

### ملاحظات بالعربي - Chapter 01

- **KDD أوسع من Data Mining:** التنقيب مرحلة داخل مسار يبدأ بتجهيز البيانات وينتهي بتقييم الأنماط وعرض المعرفة؛ لذلك لا نساوي بين المصطلحين.
- **وصف المجموعات يختلف عن التنبؤ:** Characterization يلخص مجموعة، وDiscrimination يقارنها بغيرها، أما Classification فيتنبأ بفئة لسجل جديد.
- **الشذوذ إشارة للفحص وليس حكمًا:** قد تكون القيمة النادرة صحيحة؛ نحتاج قرائن إضافية قبل وصفها احتيالًا أو خطأً.

# Chapter 02 - Data Types & Preparation

## Han Ch2, Exercises 2.2 and 2.5 - 80-90% match

### 2.2 - Summary statistics and plots (80%)

**Question.** For the ordered values `13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70`, compute mean, median, mode(s), midrange, quartiles, and five-number summary; sketch/describe a boxplot and distinguish a quantile plot from a Q-Q plot.

**Answer.** There are 27 values; sum = 809, so mean = 809/27 = **29.963**; median = **25**; mode = **25 and 35**, each occurring four times; midrange = (13+70)/2 = **41.5**. Using the median-of-halves convention, Q1 = **20**, Q3 = **35**. Five-number summary: **(13, 20, 25, 35, 70)**. The box spans 20-35, median at 25, whiskers to the non-outlier limits; under Tukey 1.5×IQR fences, upper fence = 57.5, so 70 is plotted separately as a potential outlier. A quantile plot places one variable’s ordered values against cumulative probabilities; a Q-Q plot compares corresponding quantiles of two distributions, often sample versus theoretical.

### 2.1 - Additional dispersion measures (60%)

**Question.** Name three useful dispersion measures beyond those emphasized in the chapter and explain how they could be computed efficiently for a large database.

**Answer.** Examples: median absolute deviation (MAD), mean absolute deviation, and Gini mean difference. Mean absolute deviation can be accumulated around a chosen center in a scan; MAD requires selecting a median and then selecting the median of absolute deviations, which can use external-memory selection/approximation; Gini mean difference can use sorted values and prefix sums rather than enumerating all pairs. Approximate quantile sketches reduce memory when exact order statistics are unnecessary.

### 2.3 - Median from grouped frequencies (80%)

**Question.** Estimate the median age from grouped frequencies: 1-5: 200; 6-15: 450; 16-20: 300; 21-50: 1500; 51-80: 700; 81-110: 44.

**Answer.** Total N = **3194**; median position is N/2 = **1597**. Cumulative frequency before 21-50 is 950; after it is 2450, so the median class is **21-50**. Linear interpolation using continuous boundaries 20.5-50.5 gives 20.5 + ((1597-950)/1500)×30 = **33.44 years approximately**. Because ages are grouped, this is an estimate, not an exact sample median.

### 2.5 - Nominal and asymmetric binary dissimilarity (90%)

**Question.** Define dissimilarity for nominal attributes and asymmetric binary attributes, where joint absence is not informative.

**Answer.** For a single nominal attribute, dissimilarity is 0 for a match and 1 for a mismatch; over p attributes use the fraction of mismatches. For asymmetric binary attributes, ignore joint zeros and use Jaccard dissimilarity: `d = (b+c)/(a+b+c)`, where a counts joint 1s, b and c count mismatches, and d counts joint 0s. Similarity is `a/(a+b+c)`.

### 2.4 - Hospital age/body-fat sample (100%)

**Question.** For the 18 paired observations below, calculate mean, median, and standard deviation for age and body-fat percentage; describe the boxplots, scatterplot, and Q-Q plot.

| Age | 23 | 23 | 27 | 27 | 39 | 41 | 47 | 49 | 50 | 52 | 54 | 54 | 56 | 57 | 58 | 58 | 60 | 61 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Fat % | 9.5 | 26.5 | 7.8 | 17.8 | 31.4 | 25.9 | 27.4 | 27.2 | 31.2 | 34.6 | 42.5 | 28.8 | 33.4 | 30.2 | 34.1 | 32.9 | 41.2 | 35.7 |

**Answer.** Using population SD: age mean **46.444**, median **51**, SD **12.846**; fat mean **28.783**, median **30.7**, SD **8.994**. If the 18 adults are treated as a sample, sample SDs are **13.219** and **9.254** respectively. The paired covariance is **94.463** (population convention) and Pearson r = **0.8176**, indicating a strong positive linear association in this sample, not causation. The scatterplot should show an overall increasing trend; the Q-Q plot compares the two variables’ ordered quantiles and is not a plot of paired observations. Boxplot fences depend on the quartile convention, so state it when flagging outliers.

## Han Ch3, Exercises 3.1-3.9, 3.12(a), 3.13 - 60-100% match

### 3.1 - Data quality dimensions (80%)

**Question.** Explain accuracy, completeness, and consistency as data-quality dimensions; name additional dimensions and why they matter.

**Answer.** Accuracy is closeness to the real value; completeness is whether required values/records are present; consistency is absence of contradictions across fields or sources. Additional dimensions include timeliness, validity, uniqueness, and interpretability. A dataset can be complete but inaccurate, or accurate but stale; quality must be assessed against the mining task.

### 3.2 - Missing-value treatment (90%)

**Question.** Give practical methods for handling missing values and indicate when each is reasonable.

**Answer.** Delete a row only when missingness is limited and deletion will not bias the sample; fill with a constant when “unknown” is meaningful; use a mean/median/mode or class-conditional estimate when a simple imputation is justified; predict from other attributes when sufficient signal exists; or use models that handle missing values directly. Preserve a missingness indicator when absence itself may be informative. Fit imputation on training data only to prevent leakage.

### 3.3 - Binning and outlier check (80%; part c excluded at 40%)

**Question.** Using the 27 ages listed in Han Ch2 Exercise 2.2: (a) smooth by bin means with bin depth 3; (b) propose a way to identify outliers; (c) describe alternative smoothing methods.

**Answer (a).** The nine equal-depth bins and means are: `[13,15,16]→14.6667`; `[16,19,20]→18.3333`; `[20,21,22]→21`; `[22,25,25]→24`; `[25,25,30]→26.6667`; `[33,33,35]→33.6667`; `[35,35,35]→35`; `[36,40,45]→40.3333`; `[46,52,70]→56`. Replace each member by its bin mean.

**Answer (b).** With median-of-halves quartiles Q1=20 and Q3=35, IQR=15; Tukey fences are -2.5 and 57.5. Thus 70 is a **potential** high outlier. This rule flags for review; it does not prove an error.

**Part (c) fit: 40%, excluded.** Median/boundary smoothing are textbook alternatives, but they are not developed enough in the local notes to count as a matched question.

### 3.4 - Data integration (80%)

**Question.** Identify issues that arise when integrating data from multiple sources and how to address them.

**Answer.** Resolve schema and naming conflicts, units and value encodings, duplicate entities, inconsistent keys, different granularity/time periods, missingness, and contradictory values. Use metadata and entity resolution, standardize units/codes, define precedence or reconciliation rules, deduplicate, and retain provenance. Validate integrated totals and key distributions before mining.

### 3.5 - Ranges of normalization methods (90%)

**Question.** State the output-range behavior of min-max, z-score, MAD-based z-score, and decimal-scaling normalization.

**Answer.** Min-max maps the observed minimum and maximum to the selected interval, commonly [0,1]. Z-score `(x-μ)/σ` has mean 0 and standard deviation 1 under the chosen population/sample convention, with no fixed bounds. MAD-z uses `(x-μ)/mean(|x-μ|)` and has no fixed bounds. Decimal scaling divides by `10^j` chosen so the largest absolute scaled value is below 1; it preserves relative decimal scale but does not force a common minimum/maximum.

### 3.6 - Normalize five values (100%)

**Question.** Normalize `{200, 300, 400, 600, 1000}` by min-max to [0,1], z-score, mean-absolute-deviation z-score, and decimal scaling.

**Answer.** Min-max: **0, 0.125, 0.25, 0.5, 1**. Mean = 500; population σ = √80000 = 282.8427; z-scores: **-1.0607, -0.7071, -0.3536, 0.3536, 1.7678**. Mean absolute deviation = 240; MAD-z: **-1.25, -0.8333, -0.4167, 0.4167, 2.0833**. Decimal scaling uses j=4 because 1000/10³ is not below 1; outputs **0.02, 0.03, 0.04, 0.06, 0.10**.

### 3.7 - Normalize age 35 (90%)

**Question.** For age 35 with minimum 13, maximum 70, mean 809/27 and σ=12.94, calculate min-max, z-score, and decimal scaling; recommend a method.

**Answer.** Min-max: `(35-13)/(70-13)=**0.3860**`. Mean=29.9630, so z=`(35-29.9630)/12.94=**0.3893**`. Decimal scaling uses j=2, giving **0.35**. No method is universally best: choose z-score when standardized inputs are required; choose min-max when a bounded range is required, noting sensitivity to the maximum 70.

### 3.8 - Age/body-fat analysis (80%)

**Question.** For the 18 age/body-fat pairs in the book, calculate means and standard deviations, inspect boxplots and the scatterplot, and discuss Pearson correlation/covariance and their signs.

**Answer.** Use the 18 age/fat pairs printed with Han Ch2 Exercise 2.4. These are the same data summarized above: means **46.444** and **28.783**; population SDs **12.846** and **8.994**; population covariance **94.463**; Pearson r **0.8176**. Boxplots show the marginal distributions; the scatterplot retains paired order and shows a positive trend. The Q-Q plot compares sorted age quantiles with sorted fat quantiles and therefore does not show the original pairing. A correlation does not establish causation.

### 3.9 - Discretize prices three ways (90%)

**Question.** Partition sorted prices `5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215` into three bins by equal-frequency, equal-width, and clustering-based discretization.

**Answer.** Equal-frequency: `[5,10,11,13]`, `[15,35,50,55]`, `[72,92,204,215]` (12 values / 3). Equal-width range=210, width=70: intervals `[5,75)`, `[75,145)`, `[145,215]`, yielding `[5,10,11,13,15,35,50,55,72]`, `[92]`, `[204,215]`. A clustering-based solution is not unique; a valid three-cluster partition should group nearby values and report its algorithm/initialization. One plausible 1-D partition is `[5,10,11,13,15]`, `[35,50,55,72,92]`, `[204,215]`; verify against the specified clustering method if one is required by the course.

### 3.11 - Histogram and sampling designs (80%)

**Question.** For the age values in Exercise 2.2, construct a histogram with bin width 10 and compare simple random sampling with/without replacement, cluster sampling, and stratified sampling for a sample of five. Define youth, middle-aged, and senior strata.

**Answer.** Histogram counts for decade bins [10,20), [20,30), [30,40), [40,50), [50,60), [60,70), [70,80] are **5, 9, 8, 3, 1, 0, 1** (the final bin includes the maximum 70). SRSWOR selects five distinct records; SRSWR may repeat a record. Cluster sampling selects whole natural groups and is efficient when groups are accessible, but can have higher variance. Stratified sampling samples within each age stratum and ensures representation. The exact stratum cutoffs are not uniquely fixed by the prompt; choose nonoverlapping intervals and state them, e.g. youth <30, middle 30-49, senior ≥50, then allocate five proportionally or equally.

### 3.12(a) - ChiMerge (60%)

**Question.** Explain how ChiMerge merges adjacent numeric intervals and apply its stopping/maximum-interval condition to the supplied Iris attributes.

**Answer.** Start with one interval per distinct ordered value. For each pair of adjacent intervals, compare class distributions with a χ² statistic; merge the pair with the smallest statistic (least evidence of different class distributions). Recompute neighboring statistics and continue until the significance/stopping condition or the maximum of six intervals is reached. Exact final intervals require the original Iris table and stated significance threshold; without both, no numeric interval list is asserted. **The separate request to obtain/process external Iris data is excluded** as not part of the local chapter question.

### 3.13 - Generate concept hierarchies (70%)

**Question.** Design a procedure that creates a concept hierarchy for a nominal attribute using distinct-value counts and for a numeric attribute using equal-width discretization.

**Answer.** For nominal values, count distinct levels and group them using domain metadata or a coarser-to-finer mapping; do not invent semantic order for nominal values. For numeric values, divide `[min,max]` into k equal-width intervals, label each interval, and connect interval labels to the original attribute. Store the mapping and missing/unknown category explicitly so roll-up is reproducible.

## Aggarwal Ch2, Exercises 1, 3, 10, 13 - 60-80% match

### 2.1 - Missing time-series point (70%)

**Question.** Estimate the missing final value in the series `-3, -1, 1, 3, 5, 7, ?` using a window of three observations.

**Answer.** The sequence has constant first difference +2, so linear continuation gives **9**. A trailing-window mean of the previous three values is `(3+5+7)/3=5`, which is not appropriate for this clear trend. State the interpolation/forecasting assumption; for evenly spaced linear data, 9 is the defensible estimate.

### 2.3 - Normalize and discretize mixed dataset (60%)

**Question.** For the Arrhythmia dataset, standardize numeric attributes to mean 0 and standard deviation 1, then discretize each numeric attribute into 10 equal-width and 10 equal-depth bins.

**Answer.** For each numeric training attribute, compute μ and σ and transform `z=(x-μ)/σ`, handling zero-variance columns separately. Equal-width uses width `(max-min)/10`; equal-depth sorts values and partitions them into ten groups of nearly equal counts. Apply learned boundaries/statistics to held-out data without refitting. **No dataset-specific numbers are supplied here** because the external dataset file is not bundled with the textbook exercise.

### 2.10 - Wavelet decomposition (60%)

**Question.** Apply a one-level Haar wavelet decomposition to `1,1,3,3,3,3,1,1` and count nonzero coefficients.

**Answer.** Under the standard orthonormal Haar transform, the first-level details are all zero because each adjacent pair is constant. The next detail level has two nonzero coefficients (the pair means differ), the final detail is zero, and the final approximation coefficient is nonzero. Thus **3 coefficients are nonzero** (one approximation plus two details). Scaling changes their magnitudes, not the zero/nonzero count.

### 2.13 - Sampling error versus sample size (60%)

**Question.** Draw samples of sizes 1, 10, 100, 1000, and 10000 from the referenced dataset and compare sample-mean errors across repeated trials.

**Answer.** For each n, repeat sampling, calculate `z_i = sample_mean_i - population_mean` (or the book’s stated standardized error), and compare the distribution/variance of errors. Under independent sampling with finite variance, standard error scales approximately as `σ/√n`; increasing n reduces typical error, though an individual sequence need not improve monotonically. Exact plotted values require the referenced dataset and random seed.

---

### ملاحظات بالعربي - Chapter 02

- **اذكر اتفاقية الحساب:** الانحراف المعياري والربيعات قد يختلفان حسب اعتبار البيانات مجتمعًا أو عينة وطريقة تقسيم القيم؛ اكتب الاتفاقية قبل المقارنة.
- **التطبيع لا يضمن إزالة أثر القيم المتطرفة:** Min-max حساس للحدين، بينما Z-score غير محدود بمدى ثابت؛ اختيار الطريقة مرتبط بالخوارزمية وبطبيعة البيانات.
- **القيمة المفقودة ليست صفرًا تلقائيًا:** الصفر قد يحمل معنى حقيقيًا. اختر المعالجة بحسب سبب الفقد، وتعلّم معاملات التعويض من بيانات التدريب فقط.
- **نتيجة التجميع العمري تقديرية:** الوسيط المحسوب من الفئات يعتمد على الاستيفاء وافتراض توزع القيم داخل الفئة.

# Chapter 03 - Feature Extraction & Portability

## Aggarwal Ch2, Exercises 2, 4-6, 10-12 - 60-80% match

### 3.1 - Represent personality from documents (70%)

**Question.** Given documents describing people, identify a suitable representation for finding personality-related patterns.

**Answer.** Clean/tokenize text, map documents to a sparse bag-of-words or TF-IDF vector, optionally add lexicon-derived or learned semantic features, and retain document/person identifiers as metadata rather than predictive features. Normalize if the chosen distance/model requires it. Validate that labels or personality claims are ethically and empirically supported; the representation alone cannot establish a psychological trait.

### 3.2 - Convert heterogeneous values for clustering (80%)

**Question.** Design a common feature representation from mixed object types and explain how the converted objects can be clustered.

**Answer.** Choose type-appropriate features: normalized numeric values, one-hot or ordinal encoding where justified, text vectors, time-series summaries/embeddings, and image/sequence features. Align features into a vector or define a mixed-type distance; scale numeric dimensions so large units do not dominate. Document information loss and missing-value handling before applying clustering.

### 3.3 - Spatial temperature grids plus text (70%)

**Question.** Convert 10×10 temperature grids with associated text descriptions into a representation suitable for multidimensional analysis.

**Answer.** Flatten each grid into 100 location-indexed measurements or extract spatial summaries (mean, variance, gradients, local texture); encode associated text with a vocabulary/TF-IDF or text embedding. Concatenate only after scaling and preserving modality boundaries, or use a mixed/kernel distance. Keep grid coordinate order consistent across objects.

### 3.4 - Protein sequences with annotations (70%)

**Question.** Represent protein sequences and their textual annotations together for mining.

**Answer.** Encode sequences with k-mer frequency, domain/motif indicators, or a sequence embedding; vectorize annotations separately; normalize/weight the modalities and concatenate or combine their similarities. Preserve sequence length and missing-annotation indicators where relevant. Do not treat amino-acid symbols as ordinary numeric magnitudes.

### 3.5 - PCA on Musk data (60%)

**Question.** Apply PCA to the Musk dataset and report eigenvectors/eigenvalues.

**Answer.** Center numeric features; compute covariance (or use SVD); solve `Σv_i=λ_i v_i`; sort eigenvalues descending; report the corresponding normalized eigenvectors and explained-variance ratios. Exact numeric values depend on the dataset version, missing-value handling, and whether covariance or correlation PCA is used. No dataset-specific results are fabricated here.

### 3.6 - SVD on Musk data (60%)

**Question.** Repeat the Musk reduction using singular value decomposition.

**Answer.** For centered data matrix X, compute `X=UΣVᵀ`; columns of V are principal directions and squared singular values divided by the appropriate sample denominator yield covariance eigenvalues. Sign flips of singular vectors are equivalent solutions. Exact outputs require the same data and preprocessing as 3.5.

### 3.7 - Wavelet representation for reduction (60%)

**Question.** Apply wavelet decomposition to the specified sequence and identify nonzero coefficients.

**Answer.** Use a stated wavelet family and boundary convention, recursively split approximation/detail coefficients, and count nonzeros after each transform. For the Haar example in Aggarwal Ch2 Exercise 10, all first-level pair differences are zero because each pair is constant; subsequent coefficients depend on normalization and whether the final approximation is counted. The prompt is only partially matched because local notes do not fix a wavelet convention.

### 3.8 - Time-series and sensor-data features (60%)

**Question.** Apply wavelet transformation to (a) the temperature series of the first sensor in the Intel Research Berkeley dataset, and (b) each quantitative variable in the KDD Cup 1999 intrusion dataset treated as a time series.

**Answer.** For each extracted ordered series, handle missing observations and choose/document a wavelet family, level, and boundary rule. Apply the discrete wavelet transform, retain approximation/detail coefficients appropriate to the task, and compare reduction ratio and reconstruction error. For KDD quantitative variables, sort/interpret records in the prescribed dataset order before treating rows as time; otherwise the temporal assumption is artificial. The exercise requires the separately downloaded Intel/KDD files, so exact coefficient tables are not claimed here.

## Aggarwal Ch3, Exercises 1-8 and 15; Han Ch2, Exercise 2.5 - 60-100% match

### 3.9 - Lp distances (90%)

**Question.** Compute L1, L2, and L∞ distances between points (1,2) and (3,4).

**Answer.** Differences are (2,2): `L1=|2|+|2|=**4**`; `L2=√(4+4)=**√8≈2.8284**`; `L∞=max(2,2)=**2**`.

### 3.10 - Mahalanobis distance after PCA scaling (70%)

**Question.** Show that Mahalanobis distance becomes Euclidean distance after transforming to principal-component coordinates and dividing each component by its standard deviation.

**Answer.** Let covariance `Σ=VΛVᵀ`. Transform x to `z=Λ^(-1/2)Vᵀx`. Then `||z_x-z_y||²=(x-y)ᵀVΛ^(-1)Vᵀ(x-y)=(x-y)ᵀΣ^(-1)(x-y)`, which is squared Mahalanobis distance. Zero-eigenvalue components require dropping the null directions or using a pseudoinverse.

### 3.10a - Cosine formula derivation (90%)

**Question.** Derive the cosine similarity formula for two nonzero vectors X and Y.

**Answer.** By the dot-product identity, `X·Y=||X||||Y||cosθ`; hence `cosθ=(X·Y)/(||X||||Y||)`. It is undefined if either vector is zero. For sparse text, it compares direction and is invariant to multiplying either vector by a positive scalar.

### 3.10b - Ionosphere distance contrast (60%)

**Question.** On the UCI Ionosphere dataset, calculate all-pairs L1, L2, and L∞ distances and the book-defined contrast; repeat using the first r dimensions as r increases.

**Answer.** For each r, compute each pairwise distance over dimensions 1…r, summarize the minimum and maximum nonzero distances using the contrast definition in the chapter, and plot contrast against r for each p. Distance concentration is indicated when nearest and farthest distances become relatively similar. The exercise depends on the downloaded dataset version; no numeric curve is claimed without the source file.

### 3.10 - Set similarity (100%)

**Question.** For A={A,B,C} and B={A,C,D,E}, calculate overlap-based similarity measures taught locally.

**Answer.** Intersection size=2; union size=5. Jaccard=`2/5=**0.4**`; Jaccard distance=`**0.6**`. On the five-element union vocabulary, simple matching has 2 shared presences and 0 shared absences, so similarity=`2/5=**0.4**`. Cosine on binary vectors is `2/√(3×4)=**0.5774**`.

### 3.11 - Bag-of-words cosine (100%)

**Question.** Find cosine similarity between “The sly fox jumped over the lazy dog” and “The dog jumped at the intruder,” using a bag-of-words representation.

**Answer.** With lowercase token counts and no stop-word removal, vector norms are √8 and √6; shared tokens are `the` twice plus `dog` and `jumped`, dot product=4. Cosine=`4/√48=**0.5774**`. If stop words are removed, the vocabulary and score change; state preprocessing.

### 3.12 - Mixed data representation (80%)

**Question.** Explain how to combine categorical and quantitative attributes for nearest-neighbor comparison.

**Answer.** Normalize numeric dimensions and use an appropriate nominal mismatch or binary similarity for categorical attributes; combine per-attribute distances with explicit weights. For asymmetric binary features, ignore joint absence (Jaccard); for symmetric binary features, matching can count both presences and absences. The final distance must respect feature type and scale.

### 3.13 - Categorical nearest neighbors (60%)

**Question.** On the categorical-only KDD Cup intrusion dataset, find each record’s nearest neighbor using simple matching and inverse occurrence frequency; compare class labels.

**Answer.** For each pair, count categorical matches; choose the maximum. For inverse-frequency matching, weight a matching value inversely to its corpus frequency, so rare matches contribute more. Exclude self-neighbors; define tie handling; then count label agreement. Exact agreement counts depend on the downloaded dataset version and preprocessing, which the exercise does not bundle.

### 3.14 - Quantitative nearest neighbors (60%)

**Question.** Repeat the nearest-neighbor/class-label comparison on quantitative-only KDD data using L1, L2, and L∞ distances.

**Answer.** Normalize numeric columns first if units differ. For each record choose the closest other record under each norm, apply a fixed tie rule, and count whether its class matches. Exact counts depend on the dataset version and preprocessing; the exercise is a computational project, so no unsupported numeric result is claimed.

### 3.15 - Mixed-attribute nearest neighbors (70%)

**Question.** Repeat the nearest-neighbor comparison using all KDD Cup attributes and combine the categorical and quantitative distance functions in different ways.

**Answer.** Compute one type-appropriate distance per modality (matching/inverse frequency for categorical attributes, normalized Lp for quantitative attributes), then combine with declared weights, for example `d=αd_cat+(1-α)d_num`. Normalize component ranges so neither type dominates by scale; compare class-label agreement across α choices. Exact counts require a specified KDD version, preprocessing, and tie rule.

---

### ملاحظات بالعربي - Chapter 03

- **التمثيل يسبق حساب التشابه:** لازم نحول النص أو السلسلة الزمنية أو البيانات المكانية إلى تمثيل مناسب قبل تطبيق المسافة أو التشابه.
- **انتبه لاتجاه المقياس:** المسافة الأصغر تعني تقاربًا أكبر، بينما التشابه أو cosine الأكبر يعني تقاربًا أكبر.
- **وحّد المقاييس عند الحاجة:** اختلاف وحدات السمات قد يجعل السمة ذات الأرقام الأكبر تهيمن على المسافة، حتى لو لم تكن أهم.
- **Mahalanobis يأخذ الترابط والتباين بالحسبان:** لذلك قد يختلف عن Euclidean، لكنه يحتاج تقديرًا صالحًا لمصفوفة التغاير.

# Chapter 04 - Feature Selection

## Han Ch3, Exercise 3.10 - 100% match

### 4.1 - Forward, backward, and combined search (100%)

**Question.** Describe forward selection, backward elimination, and a combined strategy for selecting an attribute subset.

**Answer.** Forward selection starts with no features, repeatedly adds the feature that most improves the evaluation criterion, and stops when improvement is insufficient or the budget is reached. Backward elimination starts with all features and repeatedly removes the least useful feature. Combined search alternates additions and removals (or allows a recently removed feature to re-enter) to reduce greedy path dependence. Evaluate each candidate using training-only validation to avoid leakage. Forward is cheaper when the final subset is small; backward is natural when most features are useful; neither guarantees a global optimum.

## Aggarwal Ch10, Exercises 1-2 - 60% partial match

### 4.2 - Gini and entropy as feature scores (60%)

**Question.** For the following donation-training sample, compute Gini and entropy for the full set and for the records with age≥50.

<div class="no-break">

| Person | Age | Salary ($000) | Donor? |
|:--|--:|--:|:--:|
| Nancy | 21 | 37 | N |
| Jim | 27 | 41 | N |
| Allen | 43 | 61 | Y |
| Jane | 38 | 55 | N |
| Steve | 44 | 30 | N |
| Peter | 51 | 56 | Y |
| Sayani | 53 | 70 | Y |
| Lata | 56 | 74 | Y |
| Mary | 59 | 25 | N |
| Victor | 61 | 68 | Y |
| Dale | 63 | 51 | Y |

</div>

**Answer.** Whole sample: Y=6, N=5; Gini=`1-(6/11)²-(5/11)²=**60/121≈0.4959**`; entropy=`-(6/11)log₂(6/11)-(5/11)log₂(5/11)=**0.9940 bits**`. For age≥50, Y=5, N=1; Gini=`1-(5/6)²-(1/6)²=**5/18≈0.2778**`; entropy=`-(5/6)log₂(5/6)-(1/6)log₂(1/6)=**0.6500 bits**`. For a full split, weight each child impurity by its fraction of records and subtract from the parent impurity; choose the split with the largest reduction. This partially belongs to Feature Selection because it scores candidate attributes, and directly belongs to local Chapter 6 tree induction.

### 4.3 - Subspace clustering and wrapper selection (60%)

**Question.** Discuss how high-dimensional subspace clustering methods such as PROCLUS/ORCLUS relate to wrapper feature-selection methods.

**Answer.** Both seek a subset of dimensions that makes a target task perform well. A wrapper evaluates candidate subsets through the downstream clustering result; subspace methods search for locally relevant dimensions as part of cluster discovery, allowing different clusters to use different subspaces. This is a conceptual connection only; PROCLUS/ORCLUS mechanics are not part of the local chapter.

---

### ملاحظات بالعربي - Chapter 04

- **اختيار السمات يبحث عن مجموعة فرعية مفيدة:** Forward يبدأ بلا سمات ويضيف، وBackward يبدأ بكل السمات ويحذف؛ والبحث الجشع لا يضمن الحل الأمثل عالميًا.
- **درجة الانقسام تقيس نقاء الفئات بعد التقسيم:** نقارن الانخفاض الموزون في Gini أو Entropy، ولا نختار الفرع الأقل impurity وحده من دون وزنه.
- **لا تخلط بين Feature Selection وFeature Extraction:** الأول ينتقي السمات الموجودة، والثاني يبني تمثيلًا أو سمات جديدة.

# Chapter 05 - Association & Frequent Patterns

## Han Ch6, Exercises 6.1-6.8, 6.13-6.14 - 70-100% match

### 5.1 - Recover counts from closed itemsets (70%)

**Question.** Explain how frequent-itemset support information can be recovered from a complete collection of frequent closed itemsets.

**Answer.** Find all frequent closed sets C containing X and return the largest support count among them. The closure of X is a closed superset with exactly X’s transaction extent, so it has the same support; any other superset has support no greater. If no frequent closed superset contains X, X is infrequent.

### 5.2 - Generator and closed itemset (70%)

**Question.** Define a generator itemset and relate it to closed frequent itemsets.

**Answer.** A frequent-generator list alone is insufficient to determine whether an arbitrary X is infrequent: it has no information about the support of extensions that drop below minsup. When X is frequent, a minimal generator G⊆X with `support(G)=support(X)` witnesses its support; the closure/extent mapping or additional support counts are needed to identify that witness in general. A generator has no proper subset with equal support; a closed set has no proper superset with equal support. They are opposite sides of a same-support equivalence class, and can be paired with identical support.

### 5.3 - Apriori properties and partitioning (90%)

**Question.** Prove: every subset of a frequent itemset is frequent; support is anti-monotone; confidence is nondecreasing when the antecedent grows while the union stays fixed; and a globally frequent itemset is frequent in at least one partition.

**Answer.** If A⊆B, every transaction containing B contains A, so `support(A)≥support(B)`. Thus if B meets minsup, each subset A also meets it. For fixed union L and antecedents A⊆B, `conf(A→L-A)=support(L)/support(A)` and `conf(B→L-B)=support(L)/support(B)`; the denominator cannot increase from A to B, so confidence cannot decrease. For partitions with weights wᵢ and local supports pᵢ, global support is `Σwᵢpᵢ`; if every pᵢ were below minsup, their weighted average would also be below it. Therefore some partition meets the global threshold.

### 5.4 - Improve Apriori pruning (80%)

**Question.** Explain how Apriori rejects a candidate when a subset is infrequent and how subset checking can be implemented more efficiently.

**Answer.** A k-candidate survives only if every (k-1)-subset is in Lₖ₋₁. Generate subsets by deleting one item and test membership in a hash/tree structure; stop at the first missing subset. Keep candidates sorted/canonical to avoid duplicate generation. This applies the downward-closure property before counting candidates against the database.

### 5.5 - Generate rules efficiently (80%)

**Question.** Use the confidence monotonicity property to reduce the number of association rules that must be tested.

**Answer.** Start with single-item consequents of a frequent itemset. If a consequent fails minconf, every larger consequent formed by adding items also fails, because its antecedent becomes smaller and confidence cannot increase. Join only consequents that passed, then test the next size. This prunes the rule search without changing the set of strong rules.

### 5.6 - Apriori/FP-Growth worked database (100%)

**Question.** For the five transactions below, find all itemsets with support count at least 3 (60%) using Apriori and FP-Growth, then list rules with two items on the left and one on the right that meet 80% confidence.

`T1={M,O,N,K,E,Y}`; `T2={D,O,N,K,E,Y}`; `T3={M,A,K,E}`; `T4={M,U,C,K,Y}`; `T5={C,O,K,I,E}`.

**Answer.** Frequent singletons (count): K:5, E:4, M:3, O:3, Y:3. Frequent pairs: KE:4, KM:3, KO:3, KY:3, EO:3. Frequent triple: KEO:3. No larger set meets count 3. Apriori reaches these by level-wise join/prune; FP-Growth reaches the same family through conditional pattern bases, without broad candidate generation. From KEO, rules and confidence are KE→O=3/4=75% (fails); KO→E=3/3=100% (passes); EO→K=3/3=100% (passes). Both passing rules have support 3/5=60%. Repeated O within a transaction is counted once because a transaction is a set.

### 5.7 - Market baskets at two category granularities (70%)

**Question.** Four baskets, minsup=60%, minconf=80%: T1 `{King’s-Crab, Sunset-Milk, Dairyland-Cheese, Best-Bread}`; T2 `{Best-Cheese, Dairyland-Milk, Goldenfarm-Apple, Tasty-Pie, Wonder-Bread}`; T3 `{Westcoast-Apple, Dairyland-Milk, Wonder-Bread, Tasty-Pie}`; T4 `{Wonder-Bread, Sunset-Milk, Dairyland-Cheese}`. At category level, find the largest frequent itemset and all strong rules with two items on the left. Repeat at brand-category level and report the largest frequent itemset.

**Answer.** Relative minsup 60% of four means count≥3. Category baskets: T1 `{Crab,Milk,Cheese,Bread}`; T2 `{Cheese,Milk,Apple,Pie,Bread}`; T3 `{Apple,Milk,Bread,Pie}`; T4 `{Bread,Milk,Cheese}`. Largest frequent triple is `{Cheese,Milk,Bread}`, count3, support75%. Its rules: `{Cheese,Milk}→Bread` confidence 3/3=100%; `{Cheese,Bread}→Milk` 3/3=100%; `{Milk,Bread}→Cheese` 3/4=75%, so only the first two meet 80%. At brand-category granularity, only `{Wonder-Bread}` meets count3; thus the largest frequent set has k=1, support75%.

### 5.7a - Algorithm performance project (70%)

**Question.** Compare Apriori, FP-Growth, and Eclat over datasets varying in size, distribution, minsup, and pattern density; explain when each may perform better.

**Answer.** Apriori is simple but may generate many candidates and rescan transactions; FP-Growth avoids broad candidate generation and benefits from shared prefixes; Eclat uses vertical TID sets and fast intersections, often effective when those sets fit memory. Dense data/low minsup can make all methods output-bound; sparse data can reduce tree sharing or make vertical lists efficient depending on representation. Benchmark the same inputs, implementation language, hardware, preprocessing, and support thresholds; report runtime and peak memory. No universal winner exists.

### 5.8 - Correlation despite a strong rule (80%)

**Question.** Give an example where a rule has high confidence but the antecedent and consequent are negatively associated.

**Answer.** Let support(Y)=0.95 and confidence(X→Y)=0.90. Then lift=`0.90/0.95=**0.9474<1**`, so Y is less likely given X than overall and the association is negative despite 90% confidence. Confidence alone is insufficient; compare against the base rate.

### 5.9 - 2×2 transaction measures (80%)

**Question.** For the five-thousand-transaction table, rows indicate hamburger purchase and columns hot-dog purchase: both=2000, hamburger only=500, hot-dog only=1000, neither=1500. Test rule `hot dogs→hamburgers` at minsup 25% and minconf 50%; assess independence/correlation and compare the named measures.

**Answer.** Support=`2000/5000=**40%**`; confidence=`2000/3000=**66.67%**`; the rule is strong at both thresholds. Under independence the expected both count is `3000×2500/5000=1500`, below the observed 2000, so the items are positively associated. Lift=`0.40/(0.60×0.50)=**1.3333**`; φ correlation=`(2000×1500-1000×500)/√(3000×2000×2500×2500)=**0.4082**`; all-confidence=`2000/max(3000,2500)=**0.6667**`; max-confidence=`max(2000/3000,2000/2500)=**0.8**`; Kulczynski=`(0.6667+0.8)/2=**0.7333**`; cosine=`2000/√(3000×2500)=**0.7303**`. Lift and φ show positive association relative to independence; the other measures summarize overlap without using the same baseline in the same way.

## Aggarwal Ch4, Exercises 1-22 - 70-100% match

### 5.10 - Support counts, frequent and maximal sets (90%)

**Question.** For the database below, compute supports for {a,e,f} and {d,f}; list all frequent and maximal itemsets at minsup counts 2, 3, and 4.

`T1={a,b,c,d}; T2={b,c,e,f}; T3={a,d,e,f}; T4={a,e,f}; T5={b,d,f}`.

**Answer.** Support counts: `{a,e,f}=2` (T3,T4); `{d,f}=2` (T3,T5); relative support is 2/5 = **40%** for each. For minsup 2, frequent singletons are a:3,b:3,c:2,d:3,e:3,f:4; frequent pairs are ad:2, ae:2, af:2, bc:2, bd:2, bf:2, df:2, ef:3; triple aef:2. Maximal sets: **{a,d}, {a,e,f}, {b,c}, {b,d}, {b,f}, {d,f}**. For minsup 3, frequent sets are singletons a,b,d,e,f and pair ef; maximal sets **{a},{b},{d},{e,f}**. At minsup 4, only f is frequent, so maximal set **{f}**.

### 5.10a - Vertical representation (90%)

**Question.** Convert the five-basket database in Exercise 1 to a vertical item-to-transaction-ID representation.

**Answer.** `a:{1,3,4}; b:{1,2,5}; c:{1,2}; d:{1,3,5}; e:{2,3,4}; f:{2,3,4,5}`. A pair support is the size of the intersection of its two TID sets.

### 5.10b - Eight-basket database (90%)

**Question.** For the second database, list all frequent itemsets and maximal frequent itemsets at minimum support counts 3, 4, and 5.

`T1={a,c,d,e}; T2={a,d,e,f}; T3={b,c,d,e,f}; T4={b,d,e,f}; T5={b,e,f}; T6={c,d,e}; T7={c,e,f}; T8={d,e,f}`.

**Answer.** At minsup 3, all frequent sets are `{b}:3,{c}:4,{d}:6,{e}:8,{f}:6; {b,e}:3,{b,f}:3,{c,d}:3,{c,e}:4,{d,e}:6,{d,f}:4,{e,f}:6; {b,e,f}:3,{c,d,e}:3,{d,e,f}:4`. Maximal: **{b,e,f}, {c,d,e}, {d,e,f}**. At minsup 4, frequent sets are `{c}:4,{d}:6,{e}:8,{f}:6; {c,e}:4,{d,e}:6,{d,f}:4,{e,f}:6; {d,e,f}:4`; maximal: **{c,e}, {d,e,f}**. At minsup 5, frequent sets are `{d}:6,{e}:8,{f}:6,{d,e}:6,{e,f}:6`; maximal: **{d,e}, {e,f}**. Itemset `{d,e,f}` has count 4 and therefore does not meet minsup 5.

### 5.10c - Vertical representation for eight baskets (90%)

**Question.** Convert the eight-basket database above to vertical format.

**Answer.** `a:{1,2}; b:{3,4,5}; c:{1,3,6,7}; d:{1,2,3,4,6,8}; e:{1,2,3,4,5,6,7,8}; f:{2,3,4,5,7,8}`. Intersect TID sets to count any itemset.

### 5.11 - Maximal versus closed (90%)

**Question.** For the same five-transaction database, identify closed itemsets at support thresholds 2, 3, and 4 and distinguish them from maximal frequent itemsets.

**Answer.** A set is closed if no proper superset has equal support; maximal frequent means no proper superset is frequent. For database 1, closed sets at minsup 2 are `{a}:3, {a,d}:2, {a,e,f}:2, {b}:3, {b,c}:2, {b,d}:2, {b,f}:2, {d}:3, {d,f}:2, {e,f}:3, {f}:4`; at minsup 3: `{a}:3, {b}:3, {d}:3, {e,f}:3, {f}:4`; at minsup 4: `{f}:4`. Every listed set is frequent and has no equal-support proper superset. A maximal set can have no frequent extension; closedness only rules out an equal-support extension.

### 5.11a - Closed sets in the eight-basket database (90%)

**Question.** For the eight baskets in Exercise 5.10b, list closed itemsets at support counts 3, 4, and 5.

**Answer.** At minsup 3: `{b,e,f}:3, {c,d,e}:3, {c,e}:4, {d,e}:6, {d,e,f}:4, {e}:8, {e,f}:6`. At minsup 4: `{c,e}:4, {d,e}:6, {d,e,f}:4, {e}:8, {e,f}:6`. At minsup 5: `{d,e}:6, {e}:8, {e,f}:6`. Each has no strict superset with the same support.

### 5.12 - Apriori candidate levels (90%)

**Question.** Generate candidate and frequent itemsets level by level for the five-transaction database at minsup count 2; repeat on the eight-transaction database in Aggarwal Exercise 5 using minsup 3.

**Answer.** Database 1 at minsup 2: `C1=L1={a:3,b:3,c:2,d:3,e:3,f:4}`. `C2` contains all 15 pairs; `L2={ad:2,ae:2,af:2,bc:2,bd:2,bf:2,df:2,ef:3}`. After subset pruning, `C3={adf,aef,bdf}`; counting leaves `L3={aef:2}` and `C4=∅`. For database 2 at minsup 3, `C1={a:2,b:3,c:4,d:6,e:8,f:6}` and `L1={b:3,c:4,d:6,e:8,f:6}`; `L2={cd:3,ce:4,de:6,df:4,ef:6,be:3,bf:3}`; `C3=L3={cde:3,def:4,bef:3}`; no 4-itemset survives. Candidates are generated by joining same-prefix sets and pruning any with a nonfrequent immediate subset.

### 5.13 - Rule support and confidence (90%)

**Question.** For the book’s two basket datasets, calculate support/confidence for {a}→{f} and {a,e}→{f} (first database), then evaluate the listed rule(s) for the second database.

**Answer.** Use `support(X→Y)=support(X∪Y)` and `confidence=support(X∪Y)/support(X)`. In database 1, `{a,f}` and `{a,e,f}` each occur in T3,T4; `{a}` occurs T1,T3,T4 and `{a,e}` occurs T3,T4. Thus `{a}→{f}` has support 2/5=40%, confidence 2/3=66.7%; `{a,e}→{f}` has support 2/5=40%, confidence 2/2=100%. In database 2, `{a,f}` and `{a,e,f}` each occur only in T2; `{a}` and `{a,e}` each occur in T1,T2. Both rules have support 1/8=12.5% and confidence 1/2=50%.

### 5.14 - Prefix enumeration and FP-Growth (80%)

**Question.** Build the prefix-enumeration tree and FP-tree for the textbook basket datasets under the stated item ordering and minsup; compare their search structure.

**Answer.** Sort items consistently (lexicographic or reverse as requested), enumerate only frequent prefixes, and attach conditional counts. An FP-tree orders each filtered transaction by global frequency and shares common prefixes; conditional pattern bases recursively enumerate suffix-conditioned patterns. Both return the same frequent itemsets; tree shape depends on tie ordering. Exact node labels/counts require the source basket table and specified ordering.

### 5.14a - Prefix tree and FP-tree node paths (80%)

**Question.** For each of the two basket databases, construct prefix-enumeration trees in lexicographic and reverse-lexicographic order, show frequent suffixes for pattern-growth recursion, and construct FP-trees under the same orders.

**Answer.** Database 1 at minsup 2 has frequent sets `a, b, c, d, e, f; ad, ae, af, bc, bd, bf, df, ef; aef`. Its lexicographic prefix branches are `a→{d,e,f}`, `a→e→f`; `b→{c,d,f}`; `d→f`; `e→f`. Reverse-lexicographic branches are formed from the same itemsets with descending item order; the frequent family is unchanged. FP-tree transaction paths (after sorting each basket) are:

| Dataset | Order | Transaction paths |
|:--|:--|:--|
| Exercise 1 | a<b<c<d<e<f | `a-b-c-d`; `b-c-e-f`; `a-d-e-f`; `a-e-f`; `b-d-f` |
| Exercise 1 | f>e>d>c>b>a | `d-c-b-a`; `f-e-c-b`; `f-e-d-a`; `f-e-a`; `f-d-b` |
| Exercise 5 (drop infrequent a) | a<b<c<d<e<f | `c-d-e`; `d-e-f`; `b-c-d-e-f`; `b-d-e-f`; `b-e-f`; `c-d-e`; `c-e-f`; `d-e-f` |
| Exercise 5 (drop infrequent a) | f>e>d>c>b>a | `e-d-c`; `f-e-d`; `f-e-d-c-b`; `f-e-d-b`; `f-e-b`; `e-d-c`; `f-e-c`; `f-e-d` |

Insert paths into a shared-prefix tree and annotate each node with the number of transactions reaching it. Prefix-enumeration and pattern-growth return the same frequent sets; one groups by canonical prefixes, the other recursively conditions on suffix items.

### 5.14b - Depth-first Apriori pruning (80%)

**Question.** Explain how to apply Apriori’s subset pruning in a depth-first itemset search.

**Answer.** When a node represents itemset X, test every immediate subset of a proposed extension X∪{i} against a stored frequent-set hash/trie. If any subset is absent, prune that extension and its descendants. A depth-first traversal can keep a canonical item order and cache frequent subsets so the breadth-first property is not required for correctness.

### 5.14c - Pattern-growth representations (70%)

**Question.** Outline implementations of pattern growth using (a) arrays, (b) pointer structures without an FP-tree, and (c) a pointer-based FP-tree; describe prefix-growth with suffix mining.

**Answer.** Arrays store sorted item IDs/counts and use index ranges for conditional bases; pointer lists store nodes/links directly but add allocation and traversal overhead; an FP-tree shares common prefixes and a header table links equal items for conditional mining. Prefix-growth partitions patterns by canonical prefix and mines suffixes in each conditional database. Unit tests should compare all outputs/supports across representations; runtime depends on compression and allocation overhead.

### 5.15 - Association measures from a contingency table (80%)

**Question.** For the item pair {d,f} in the textbook database, calculate correlation coefficient, interest/lift, cosine, and Jaccard.

**Answer.** Let n_df be joint count, n_d and n_f marginal counts, N total. `lift=N n_df/(n_d n_f)`; cosine=`n_df/√(n_d n_f)`; Jaccard=`n_df/(n_d+n_f-n_df)`; φ correlation=`(n_df n_00-n_d¬f n_¬df)/√((n_d n_¬d)(n_f n_¬f))`. Insert the book’s exact contingency counts. The same formulas are verified, but the numeric vector is intentionally not guessed.

### 5.15a - Numeric association measures and duplicated source item (90%)

**Question.** For `{d,f}` in the five-basket database, compute φ correlation, interest/lift, cosine, and Jaccard. The source prints this same exercise twice as Exercises 20 and 21.

**Answer.** Counts: n_df=2, n_d=3, n_f=4, n_10=1, n_01=2, n_00=0, N=5. Lift=`5·2/(3·4)=**0.8333**`; cosine=`2/√12=**0.5774**`; Jaccard=`2/(3+4-2)=**0.4**`; φ=`(2·0-1·2)/√(3·2·4·1)=**-0.4082**`. The negative φ and lift<1 indicate negative association. Exercises 20 and 21 are exact duplicates in this edition of the source.

### 5.15b - Compare mining algorithms (70%)

**Question.** Compare TreeProjection, DepthProject, VerticalApriori, and FP-Growth in representation, traversal, and candidate counting.

**Answer.** TreeProjection partitions projected transaction data by prefixes; DepthProject explores projected databases depth-first; VerticalApriori intersects transaction-ID sets and applies Apriori pruning; FP-Growth compresses ordered transactions into a prefix tree and mines conditional pattern bases without broad candidate generation. Their shared goal is complete frequent-itemset enumeration; memory use and work depend on data density, prefix sharing, and TID-set sizes. The local chapter directly covers Apriori/FP-Growth; the other implementations receive a partial-match comparison only.

## Aggarwal Ch5, Exercises 1-5 - 80-100% match

### 5.16 - Maximal patterns (90%)

**Question.** For the five-basket database in Aggarwal Ch4 Exercise 1, list maximal frequent itemsets at support counts 2, 3, and 4.

**Answer.** At support 2: `{a,d}`, `{a,e,f}`, `{b,c}`, `{b,d}`, `{b,f}`, `{d,f}`. At support 3: `{a}`, `{b}`, `{d}`, `{e,f}`. At support 4: `{f}`. This is the same computed database as Chapter 5.10; the printed source question repeats the dataset.

### 5.17 - Extract maximal sets from frequent sets (80%)

**Question.** Give an algorithm to select maximal patterns from a complete frequent-pattern collection.

**Answer.** Sort frequent sets by decreasing cardinality. For each set X, test whether any already-retained larger set contains X; if none does, retain X as maximal. A trie/bitset index accelerates subset checks. The result is correct only if the input contains the complete frequent-set family at the selected threshold.

### 5.18 - Closed pattern enumeration (90%)

**Question.** For the first database, list closed patterns at support counts 2, 3, and 4; explain the test for closedness.

**Answer.** At support 2: `{a}:3,{a,d}:2,{a,e,f}:2,{b}:3,{b,c}:2,{b,d}:2,{b,f}:2,{d}:3,{d,f}:2,{e,f}:3,{f}:4`. At support 3: `{a}:3,{b}:3,{d}:3,{e,f}:3,{f}:4`. At support 4: `{f}:4`. A frequent set is closed when no strict superset has the same support.

### 5.19 - Extract closed sets from frequent sets (80%)

**Question.** Give an algorithm to identify closed frequent itemsets from a complete frequent-itemset collection.

**Answer.** For each frequent X, inspect its strict supersets. Retain X only if every strict frequent superset has strictly smaller support. Sort by cardinality and use a subset index to avoid comparing unrelated sets. If the input omits some frequent supersets, closedness cannot be certified.

### 5.20 - Frequent, maximal, and closed patterns (100%)

**Question.** For the eight baskets in Aggarwal Ch4 Exercise 5, report frequent itemsets and maximal and closed patterns at support counts 3, 4, and 5.

**Answer.** At minsup 3, frequent singletons are `b:3,c:4,d:6,e:8,f:6`; pairs `be:3,bf:3,cd:3,ce:4,de:6,df:4,ef:6`; triples `bef:3,cde:3,def:4`. Maximal: **bef, cde, def**. Closed: **bef:3, cde:3, ce:4, de:6, def:4, e:8, ef:6**.

At minsup 4, frequent singletons are `c:4,d:6,e:8,f:6`; pairs `ce:4,de:6,df:4,ef:6`; triple `def:4`. Maximal: **ce, def**. Closed: **ce:4, de:6, def:4, e:8, ef:6**.

At minsup 5, frequent singletons are `d:6,e:8,f:6`; pairs `de:6,ef:6`. Maximal: **de, ef**. Closed: **de:6, e:8, ef:6**.

## Han Ch7, Exercises 7.5, 7.6(a-b), 7.10 - 60-70% partial match

### 5.16 - Negatively correlated patterns (60%)

**Question.** Given two frequent itemsets X and Y, define the negative-correlation condition using the average of `P(X|Y)` and `P(Y|X)`, then outline a pattern-growth method to mine such unions.

**Answer.** First mine frequent itemsets with the local minsup rule. For candidate pairs X,Y, compute both conditional probabilities and retain the union when their mean is below the specified ε threshold. A pattern-growth implementation can maintain support counts for extensions and evaluate the negative-correlation condition after both sides are frequent. Frequency alone does not imply positive association; lift below 1 is a simpler local indicator of negative association. The pruning details depend on the exact ε constraint, so do not assume ordinary Apriori anti-monotonicity applies to the negative-correlation test.

### 5.17 - Constraint properties (70%)

**Question.** Prove the pattern-constraint classifications for (a) `v∈S` and (b) `S⊆V`: determine whether each is anti-monotone, monotone, or succinct.

**Answer.** For `v∈S`, once a set contains v, adding items preserves the condition: monotone. The satisfying sets can be generated directly as `{v}∪T`, so it is succinct; it is not anti-monotone because a subset may omit v. For `S⊆V`, every subset of a satisfying set also satisfies it: anti-monotone. It is succinct because items can be restricted to V before mining; it is not monotone because adding an item outside V violates the condition. The remaining table rows about min, range, and variance are excluded because their constraint taxonomy is not taught locally.

### 5.18 - Compressing frequent patterns (80%)

**Question.** Design an efficient way to compress a large collection of frequent patterns into a smaller, interpretable representation and discuss robustness to the similarity measure.

**Answer.** Use closed itemsets to preserve exact support information compactly; use maximal itemsets for an even smaller representation when subset supports are not needed. Deduplicate equivalent patterns and optionally cluster the remaining patterns by a stated Jaccard/TID-set similarity. Different similarity definitions can change the clusters, so report the measure and test stability under alternatives. This combines the local closed/maximal material with local similarity measures.

---

### ملاحظات بالعربي - Chapter 05

- **Support يقيس شيوع النمط، وConfidence يقيس موثوقية القاعدة الشرطية:** ارتفاع الثقة وحده لا يثبت وجود ارتباط؛ قارنه بمعدل ظهور النتيجة أو استخدم مقياس ارتباط مناسبًا.
- **Apriori يعتمد على خاصية الاحتواء:** إذا كانت مجموعة غير متكررة، فلا يمكن لأي مجموعة أكبر تحتويها أن تكون متكررة.
- **Closed وMaximal ليسا مترادفين:** كل maximal متكرر هو closed، لكن قد توجد مجموعة closed ولها امتداد متكرر، فلا تكون maximal.
- **في بيانات السلال، راجع تعريف الدعم والحد الأدنى وطريقة عدّ العناصر:** هذه التفاصيل تغيّر مجموعات العناصر والقواعد الناتجة.
- **FP-Growth يتجنب توليد المرشحين بالطريقة نفسها التي يستخدمها Apriori،** لكن بناء الشجرة والمسارات الشرطية يجب أن يحافظا على العدّ الأصلي.

# Chapter 06 - Classification Foundations

## Han Ch8, Exercises 8.1-8.5, 8.10-8.13 - 70-100% match

### 6.1 - Decision-tree construction and pruning (90%)

**Question.** Explain the main steps for building a decision tree, converting it into rules, controlling overfitting, and analyzing its computational cost.

**Answer.** Recursively choose a split that improves class purity (e.g., information gain/gain ratio/Gini); partition records; stop when a node is sufficiently pure, too small, or no useful split remains; assign a leaf class. Prune using a validation set or a complexity penalty to reduce overfitting. Each root-to-leaf path becomes an IF-THEN rule; simplify rules and resolve overlaps/default class. For p attributes and N records, naïve split evaluation scans data per node; sorting numeric attributes can reduce repeated work, while depth and number of candidate attributes affect cost.

**Tree-pruning note.** Pruning reduces overfitting and improves generalization. A separate pruning set reduces training data available to grow the tree; cross-validation or a complexity penalty can mitigate that cost. Pruning rules after converting a tree can simplify each rule independently, while pruning the tree first can retain structural decisions shared across branches.

**Complexity note.** Sorting each of n attributes costs `O(nN log N)` overall; once sorted, split evaluation can be updated in a linear scan per attribute. This yields the stated upper-bound form `O(nN log N)` under the book’s sorting-based analysis.

**Large-data note.** For 5 GB with only 512 MB RAM, process records in memory-sized partitions and accumulate attribute-value-class counts, then choose splits from these summaries (RainForest-style AVC sets). A rough table for 50 attributes × 100 values × 2 classes is 10,000 counters; at 8 bytes each this is about 80 KB, excluding keys and tree overhead. Stream partitions from disk rather than holding all 5 GB in RAM.

### 6.2 - Weighted tree prediction versus Naive Bayes (70%)

**Question.** Each row below is a generalized employee record with a multiplicity count. Use counts in a decision tree, then predict status for a systems employee aged 26-30 earning 46-50K with Naive Bayes.

| Department | Status | Age | Salary | Count |
|:--|:--|:--|:--|--:|
| sales | senior | 31-35 | 46-50K | 30 |
| sales | junior | 26-30 | 26-30K | 40 |
| sales | junior | 31-35 | 31-35K | 40 |
| systems | junior | 21-25 | 46-50K | 20 |
| systems | senior | 31-35 | 66-70K | 5 |
| systems | junior | 26-30 | 46-50K | 3 |
| systems | senior | 41-45 | 66-70K | 3 |
| marketing | senior | 36-40 | 46-50K | 10 |
| marketing | junior | 31-35 | 41-45K | 4 |
| secretary | senior | 46-50 | 36-40K | 4 |
| secretary | junior | 26-30 | 26-30K | 6 |

**Answer.** Expand each row by its count when calculating split statistics. One valid tree is: split on salary; categories 26-30K, 31-35K, and 41-45K predict junior; 36-40K and 66-70K predict senior; for 46-50K, split on department, with systems→junior and sales/marketing→senior. This classifies the supplied grouped records. For Naive Bayes, totals are senior=52, junior=113. Without smoothing, the senior likelihood is zero because no senior record has age 26-30; junior has positive likelihood for systems, age 26-30, and salary 46-50K, so predict **junior**. Laplace smoothing also predicts junior (using cardinalities 4 departments, 6 age ranges, and 6 salary ranges).

### 6.3 - Derive accuracy from sensitivity/specificity (100%)

**Question.** Derive overall accuracy in terms of sensitivity, specificity, and class prevalence.

**Answer.** Let prevalence P=`(TP+FN)/N`. Sensitivity=`TP/(TP+FN)` and specificity=`TN/(TN+FP)`. Then `TP/N=Sensitivity×P` and `TN/N=Specificity×(1-P)`. Therefore `Accuracy=Sensitivity·P + Specificity·(1-P)`.

### 6.4 - F-measure family (90%)

**Question.** Derive F1 and Fβ from the harmonic mean of precision and recall.

**Answer.** `F1=2PR/(P+R)`. Weighting recall β times as strongly as precision gives `Fβ=(1+β²)PR/(β²P+R)`. For β>1 recall receives more weight; for β<1 precision receives more weight. If P or R is zero, the corresponding F score is zero (using the usual convention).

### 6.5 - Build ROC points from scored cases (90%)

**Question.** The classifier scores these tuples in descending order; compute cumulative confusion counts and ROC coordinates.

| Rank | Class | Score |
|--:|:--:|--:|
|1|P|0.95|
|2|N|0.85|
|3|P|0.78|
|4|P|0.66|
|5|N|0.60|
|6|P|0.55|
|7|N|0.53|
|8|N|0.52|
|9|N|0.51|
|10|P|0.40|

| Rank | TP | FP | TN | FN | TPR | FPR |
|--:|--:|--:|--:|--:|--:|--:|
|1|1|0|5|4|0.2|0.0|
|2|1|1|4|4|0.2|0.2|
|3|2|1|4|3|0.4|0.2|
|4|3|1|4|2|0.6|0.2|
|5|3|2|3|2|0.6|0.4|
|6|4|2|3|1|0.8|0.4|
|7|4|3|2|1|0.8|0.6|
|8|4|4|1|1|0.8|0.8|
|9|4|5|0|1|0.8|1.0|
|10|5|5|0|0|1.0|1.0|

There are five positive and five negative records. Each table row gives the cumulative state after the threshold passes that score; the ROC coordinates are `(FPR, TPR)`. Before any score is accepted, the curve starts at `(0,0)`.

### 6.6 - Multiclass evaluation (80%)

**Question.** Explain how to evaluate a classifier with more than two classes.

**Answer.** Use a K×K confusion matrix, per-class precision/recall/F1, and macro-, micro-, or support-weighted averages. One-vs-rest ROC can be computed for each class when scores are available. Report class prevalence and the averaging convention; a single accuracy can hide poor performance on a rare class.

### 6.6a - Multi-label classification (80%)

**Question.** Explain how to compare classifiers when an object may belong to multiple classes simultaneously.

**Answer.** Use example-based measures (exact-match accuracy, example-wise precision/recall/F1) and label-based measures (per-label precision/recall/F1, micro/macro averages). Exact match is strict because every label must be correct; Hamming loss counts individual label errors. State how missing labels and imbalance are handled.

### 6.6b - Boosting (90%)

**Question.** Define boosting and explain why it can improve decision-tree accuracy.

**Answer.** Boosting sequentially trains base classifiers, increasing attention/weight on examples previous models misclassified, then combines their predictions. It can reduce bias and/or variance by forming a stronger ensemble from weak trees. It can also overfit noisy labels or be sensitive to outliers; validate the ensemble.

## Aggarwal Ch10, Exercises 1-3, 9-12, 19 - 60-90% match

### 6.8 - Rule classifier and decision tree (80%)

**Question.** Construct a rule classifier that perfectly classifies the training records when no two records share the same feature vector; compare its generalization to a tree.

**Answer.** A memorizing classifier can create one conjunction matching each training vector and assign its label, with a default for unseen vectors. It achieves 100% training accuracy by construction but can generalize poorly. A tree shares tests across records and can be simpler, but may also overfit; evaluate on held-out data and prune.

### 6.9 - Rule-set exclusivity/completeness (80%)

**Question.** Explain mutual exclusivity and exhaustiveness for classification rules; check the supplied overlapping age rules.

**Answer.** Rules are mutually exclusive when no record satisfies more than one rule; exhaustive when every possible record is covered. Conditions `Age>40→Donor` and `Age≤50→¬Donor` overlap for `40<Age≤50` and assign conflicting labels, so they are not mutually exclusive; they are not exhaustive if age is missing or outside the assumed domain. Add an explicit priority/order or redesign disjoint ranges and a default rule.

### 6.10 - Class priors and conditionals (70%)

**Question.** From the supplied Table 10.1, calculate class priors and conditional probabilities for the age≥50 subset.

**Answer.** Same donation example: class priors `P(Y)=6/11`, `P(N)=5/11`; conditional probabilities `P(age≥50|Y)=5/6`, `P(age≥50|N)=1/5`. This exercise duplicates the numeric request included above; it is retained once in the combined solution to avoid an unnecessary repeat.

### 6.13 - Cross-validation evidence on two datasets (70%)

**Question.** Classifier A beats B by 3 percentage points on one dataset with SD 7 points across 100 folds; B beats A by 1 point on another dataset with SD 0.1 across 100 folds. Which is preferable?

**Answer.** The datasets are distinct, so the effects should not be pooled without a target-population weighting. On dataset 1, the estimated standard error is 7/√100=0.7 points, so A’s 3-point advantage is about 4.3 SE. On dataset 2, SE=0.1/√100=0.01 points, so B’s 1-point advantage is about 100 SE. Prefer B only if dataset 2 is the relevant deployment distribution; otherwise the evidence is not enough to choose a universal winner. Compare on a representative target set and consider costs.

### 6.14 - Paired cross-validation comparison (90%)

**Question.** For ten paired rounds, compare errors `M1=(30.5,32.2,20.7,20.6,31.0,41.0,27.7,26.0,21.5,26.0)` and `M2=(22.4,14.5,22.4,19.6,20.7,20.4,22.1,19.4,16.2,35.0)` at significance level 1%.

**Answer.** Paired differences M1-M2 are `(8.1,17.7,-1.7,1.0,10.3,20.6,5.6,6.6,5.3,-9.0)`. Their mean is **6.45** points, sample SD **8.7001**, so paired t=`6.45/(8.7001/√10)=**2.344**` with 9 degrees of freedom. The two-sided 1% critical value is about 3.25, so the difference is **not significant at α=0.01**. M2’s observed mean error is lower, but the test does not establish a reliable difference at that strict level.

---

### ملاحظات بالعربي - Chapter 06

- **اختيار الانقسام لا يساوي تقييم النموذج النهائي:** قد تنمو الشجرة على بيانات التدريب جيدًا ثم تفرط في التخصيص؛ لذلك نستخدم التقليم وتقييمًا منفصلًا.
- **Accuracy قد تكون مضللة مع الفئات غير المتوازنة:** افحص الحساسية والنوعية وPrecision وF-measure، وحدد أي فئة تعدّها موجبة.
- **ROC يتغير مع العتبة:** المحور الأفقي FPR والعمودي TPR؛ احسبهما من أعداد TP وFP وTN وFN عند كل عتبة.
- **في المقارنة بين الطرائق على الطيات نفسها،** استخدم فروقًا مزدوجة بين النتائج بدل التعامل معها كعينات مستقلة.

# Chapter 07 - Classification Methods

## Han Ch8, Exercises 8.6-8.8 - 70-90% match

### 7.1 - Naive Bayes assumptions (100%)

**Question.** Describe the Naive Bayes classifier and its conditional-independence assumption.

**Answer.** Choose class c maximizing `P(c)∏ᵢP(xᵢ|c)`. The model assumes features are conditionally independent given the class; this is often false, yet the classifier can still work well. Use Laplace smoothing to prevent zero likelihoods for unseen categorical values. For numeric features, specify a distribution model such as Gaussian.

### 7.2 - Scalable Naive Bayes and boosting (70%)

**Question.** Explain how Naive Bayes can be updated from a data stream and how boosting changes a classifier.

**Answer.** Maintain class and feature sufficient counts/probability parameters and update them as each example arrives; use forgetting or windows if the distribution drifts. Boosting trains a sequence of weak learners with increased emphasis on previous errors and combines their votes. This is a partial match because streaming maintenance and ensemble details exceed the core local Chapter 7 depth.

## Aggarwal Ch10, Exercises 5, 7-8, 12 - 60-90% match

### 7.3 - Rule-based versus tree classifier (80%)

**Question.** Give advantages of rule-based classifiers over decision trees and explain how ordering/default classes affect interpretation.

**Answer.** Rules can be modular, directly inspectable, and allow domain rules to be added or removed; a tree gives a single hierarchical path and naturally partitions the feature space. Overlapping rules require ordering, voting, or conflict resolution; incomplete rules require a default class. State coverage and accuracy for each rule set.

### 7.4 - Naive Bayes with Laplace smoothing (90%)

**Question.** Outline an implementation of the categorical Naive Bayes classifier, including smoothing for unseen values.

**Answer.** During training, count class frequencies and each feature-value/class co-occurrence. For a query, score each class with `log P(c)+Σᵢ log[(n_{i,v,c}+α)/(n_c+αK_i)]`, where Kᵢ is the number of values for feature i and α=1 for Laplace smoothing. Predict the class with the highest score; normalize scores with log-sum-exp only when posterior probabilities are needed. This avoids numeric underflow and zero likelihoods.

### 7.4a - Associative classification (70%)

**Question.** Outline an associative classifier that uses only maximal patterns; when multiple rules fire, predict the majority consequent class.

**Answer.** Mine frequent maximal itemsets from labelled training data, attach class consequents to patterns, and retain rules meeting support/confidence criteria. At prediction time, find fired rules whose antecedents are contained in the test record; vote by consequent class, using the majority label. Specify tie-breaking and a default class for no fired rules. This reuses local association-pattern and rule-classification concepts.

### 7.5 - Manhattan class densities (70%)

**Question.** Classify using class-conditional densities proportional to `exp(-||X-μᵢ||₁)`.

**Answer.** For each class, compute the Manhattan distance from X to μᵢ, then score `priorᵢ × exp(-distanceᵢ)`; choose the larger posterior-proportional score. If μᵢ is unknown, estimate it by the class-wise coordinate median under L1 loss (or jointly maximize the stated class likelihood); estimate class priors from class frequencies. This gives greater likelihood to the closer class under the stated Laplace-like density.

---

### ملاحظات بالعربي - Chapter 07

- **Naive Bayes يفترض استقلال السمات شرطيًا على الفئة؛** هذا افتراض حسابي قد لا يطابق الواقع تمامًا، لكنه لا يمنع أن يعطي المصنف أداءً جيدًا.
- **Laplace smoothing يمنع الاحتمال الصفري:** أضف قيمة التنعيم إلى العدّات، ولا تنسَ تعديل المقام بعدد القيم الممكنة.
- **قواعد التصنيف تحتاج معالجة التعارض والتغطية:** تأكد ماذا يحدث إذا انطبق أكثر من شرط، وإذا لم ينطبق أي شرط.
- **تمييز prior عن likelihood مهم:** prior هو احتمال الفئة قبل رؤية السمات، وlikelihood هو احتمال السمات عند معرفة الفئة.

# Chapter 08 - Clustering

## Han Ch10, Exercises 10.1-10.8, 10.12-10.17 - 60-100% match

### 8.1 - Compare clustering families (100%)

**Question.** Compare partitioning, hierarchical, density-based, and grid-based clustering by output, assumptions, strengths, and limitations.

**Answer.** Partitioning methods (K-means) produce k groups and need k/initialization; efficient for compact numeric clusters but sensitive to scale/outliers/shape. Hierarchical methods build nested merges/splits and offer multiple resolutions, but early merge decisions can be irreversible and cost can be high. Density methods (DBSCAN) find dense regions/noise and arbitrary shapes without k, but depend on ε/MinPts and struggle with varying density. Grid methods quantize space and can be fast for many points, but results depend on grid resolution and high-dimensional sparsity.

### 8.2 - K-means trace (100%)

**Question.** Run K-means on A1(2,10), A2(2,5), A3(8,4), B1(5,8), B2(7,5), B3(6,4), C1(1,2), C2(4,9), with initial centers A1, B1, C1. Assign points, recompute means, and iterate to convergence.

**Answer.** Nearest-center assignments by squared Euclidean distance, followed by mean updates:

| Iteration | Cluster A | Cluster B | Cluster C | Updated centers (A, B, C) |
|:--:|:--|:--|:--|:--|
| 1 | {A1} | {A3,B1,B2,B3,C2} | {A2,C1} | (2,10), (6,6), (1.5,3.5) |
| 2 | {A1,C2} | {A3,B1,B2,B3} | {A2,C1} | (3,9.5), (6.5,5.25), (1.5,3.5) |
| 3 | {A1,B1,C2} | {A3,B2,B3} | {A2,C1} | (11/3,9), (7,13/3), (1.5,3.5) |

The assignments are unchanged on the next pass, so the algorithm converges to those three clusters and centers. The named initial points are centers, not fixed assignments; every point is reassigned by distance.

### 8.3 - K-means local optimum (80%)

**Question.** Construct or explain a case where K-means converges to a locally optimal but globally inferior partition.

**Answer.** K-means monotonically reduces within-cluster sum of squared errors for its current assignments/centroids, but it does not search all partitions. Poor initial centers can lead to a stable partition whose SSE exceeds another valid partition. Use multiple initializations/K-means++ and compare final SSE; this reduces but does not eliminate local-optimum risk.

### 8.4 - K-means++ seeding (80%)

**Question.** Explain K-means++ initialization and why it can improve clustering.

**Answer.** Choose the first center randomly; choose each next point with probability proportional to its squared distance from the nearest existing center. This spreads seeds across the data and often improves initial coverage and final SSE relative to arbitrary seeds. It does not guarantee a global optimum.

### 8.5 - PAM reassignment (70%)

**Question.** Give pseudocode for assigning objects to the nearest medoid and updating medoids in PAM.

**Answer.** Initialize k observed objects as medoids. Assign each object to its nearest medoid; for each cluster, test candidate member swaps and choose the swap with the greatest decrease in total dissimilarity. Repeat assignment and improving swaps until no swap reduces cost. Unlike K-means, each medoid is an actual data object and the distance need not be Euclidean.

### 8.5a - K-means and K-medians representatives (70%)

**Question.** Describe a modular k-representative algorithm where distance and representative updates can be exchanged for K-means and K-medians.

**Answer.** Shared loop: initialize k representatives; assign each object to its closest representative; update each representative; repeat until assignments stop changing. K-means uses squared Euclidean distance and the arithmetic mean. K-medians uses Manhattan distance and the coordinate-wise median. Keep assignment and update routines separate so variants share the loop.

### 8.5b - Mahalanobis K-means (60%)

**Question.** Outline K-means using Mahalanobis distance.

**Answer.** Estimate a nonsingular covariance matrix Σ, use `d²(x,μ)=(x-μ)ᵀΣ⁻¹(x-μ)` for assignments, and update cluster means. If Σ is fixed globally, whitening transforms the data so ordinary Euclidean distance corresponds to Mahalanobis distance. If covariance is re-estimated per cluster, assignments and covariance updates must be alternated; regularize near-singular matrices. This is a partial extension of the locally taught distance metrics.

### 8.6 - DBSCAN definitions (100%)

**Question.** Define directly density-reachable, density-reachable, and density-connected points and state the role of ε and MinPts.

**Answer.** The ε-neighborhood contains points within distance ε. A point is core if its ε-neighborhood has at least MinPts points (including itself under the common convention). q is directly density-reachable from core p if q lies in p’s ε-neighborhood; density-reachability is a chain of such steps; two points are density-connected if both are density-reachable from a common point. Density-connectedness is symmetric; density-reachability need not be. On the set of points belonging to DBSCAN clusters (excluding noise), density-connectedness is reflexive and transitive as well, so it partitions cluster members into equivalence classes.

### 8.6a - DBSCAN cluster nesting as ε grows (90%)

**Question.** For fixed MinPts and ε₁<ε₂, explain why each cluster under ε₁ is contained in some cluster under ε₂.

**Answer.** Every ε₁-neighborhood is contained in the corresponding ε₂-neighborhood, so any ε₁ core point remains core at ε₂. Every density-reachability chain at ε₁ is still a valid chain at ε₂. Thus all members of an ε₁ cluster remain density-connected at ε₂; clusters may expand or merge, and the containing ε₂ cluster need not be unique if multiple smaller clusters merge.

### 8.7 - When density-based clustering is useful (90%)

**Question.** Give situations where density-based clustering is preferable to K-means and explain the benefit.

**Answer.** Use DBSCAN when clusters have irregular shapes, noise/outliers should remain unassigned, and a meaningful local density scale exists. K-means imposes centroid/Voronoi-shaped regions and assigns every point. DBSCAN’s limitations include varying-density clusters and sensitivity to ε/MinPts.

### 8.8 - Hybrid clustering use (70%)

**Question.** Propose a hybrid workflow combining clustering methods and explain why each stage is used.

**Answer.** One valid design: use a coarse scalable partition or grid summary to reduce the data, then refine candidate groups with DBSCAN to recover irregular dense structures and noise. Validate that the first stage does not discard boundary points. Another justified hybrid is acceptable; specify data properties and each stage’s role.

### 8.9 - Cluster analysis as task or preprocessing (80%)

**Question.** Contrast clustering as a primary analysis goal with clustering used to support another mining task.

**Answer.** As a primary goal, clusters are the findings and must be interpreted/validated for domain meaning. As preprocessing, cluster labels, distances, or prototypes become features for classification, summarization, or anomaly detection; validate the downstream task and avoid fitting clusters on test data when that would leak information.

### 8.10 - Algorithm comparisons and cluster visualization (60-80%)

**Question.** Compare K-means, K-medoids, hierarchical clustering, and DBSCAN for the stated dataset; explain how to inspect clusters in 3D/high dimensions.

**Answer.** Match the method to geometry, scale, noise, and desired output: K-means for compact numeric groups; K-medoids for robust representative objects/general dissimilarity; hierarchical for nested structure; DBSCAN for dense irregular shapes/noise. In high dimensions, use feature projections (PCA/UMAP only if taught), pairwise-distance summaries, cluster stability, and internal measures; a 2D projection can distort separation, so do not treat a plot as proof. Untaught algorithms in the book’s comparison list (e.g., BIRCH/CHAMELEON/CLARA) are excluded from the scored comparison.

## Aggarwal Ch6, Exercises 1-11, 14, 17-19 - 60-90% match

### 8.11 - One-dimensional K-means (90%)

**Question.** Cluster values {1,…,10} into k=2 for three iterations, first using seeds {1,2}; repeat using {2,9} and compare.

**Answer.** With seeds (1,2), first assignment by nearest center gives {1} and {2,…,10}; means become 1 and 6. With centers 1 and 6, assignments are {1,2,3} and {4,…,10}; means become 2 and 7. Reassignment with 2 and 7 gives {1,2,3,4} and {5,…,10}; means 2.5 and 7.5; next assignment is unchanged, so converged. For seeds (2,9), initial boundary is 5.5, yielding {1,…,5} and {6,…,10}, means 3 and 8; reassignment boundary 5.5 remains unchanged. Compare SSE: first partition `{1,2,3,4}|{5,…,10}` has SSE=5+17.5=22.5; second `{1,…,5}|{6,…,10}` has SSE=10+10=20, so the second is better for this initialization/data.

### 8.12 - Hierarchical linkage (80%)

**Question.** Perform the first six AGNES merges on points {1,…,10} using single, complete, and average linkage.

**Answer.** Begin with ten singleton clusters. At each step merge the pair with smallest intercluster distance: minimum pairwise distance for single linkage, maximum for complete, mean pairwise distance for average. For equally spaced 1D points, ties among adjacent singleton pairs require a stated tie-break; after merges, complete/average may diverge. Report the tie rule and cluster membership after each of six merges. The source prompt’s exact distance convention should be followed before giving a unique merge sequence.

### 8.13 - Initialization sensitivity (90%)

**Question.** For values {1,…,5}, {8,…,12}, {24,28,32,36,40}, compare K-means outcomes from seeds {1,11,28} and {1,2,3}; explain whether the intended groups are recovered.

**Answer.** With seeds (1,11,28), assignment gives `{1,2,3,4,5}`, `{8,9,10,11,12}`, `{24,28,32,36,40}` with means **3, 10, 32**, unchanged on the next pass. With seeds (1,2,3), the first assignment is `{1}`, `{2}`, `{3,4,5,8,9,10,11,12,24,28,32,36,40}`; successive mean updates are (1,2,17.0769), then (1,5.1667,24.125), then (2,8.4286,32), then (3,10,32). It reaches the same three natural clusters, but takes extra iterations. This example shows initialization changes the trajectory; it does not show that this particular bad initialization fails to reach the intended result.

### 8.11a - Agglomerative linkage on ten ordered points (80%)

**Question.** For points {1,…,10}, report the first six AGNES merges under single, complete, and average linkage.

**Answer.** All three linkages first merge adjacent points at distance 1, but ties make the exact sequence nonunique unless a tie-break is specified. Under a deterministic leftmost-tie rule, single linkage successively grows the left cluster: `{1,2}`, then `{1,2,3}`, …, through `{1,…,7}` after six merges. Complete and average linkage first merge adjacent singleton pairs; a valid leftmost tie sequence is `{1,2}`, `{3,4}`, `{5,6}`, `{7,8}`, `{9,10}`, then merge `{1,2}` with `{3,4}`. State the tie rule; other equally valid sequences can occur.

### 8.11b - Single-linkage graph implementation (70%)

**Question.** Describe a single-link hierarchical merging algorithm using a weighted k-nearest-neighbor similarity graph.

**Answer.** Treat graph vertices as objects and edge weights as similarities. Sort edges from highest similarity to lowest; use union-find to merge the components joined by each edge, recording the merge weight. For a distance graph, process edges in ascending distance. A sparse k-NN graph approximates full single linkage and may omit a needed edge, so graph construction affects the result.

### 8.11c - EM for spherical and general GMMs (70%)

**Question.** Outline EM for two equal-radius spherical Gaussian clusters, compare its centroids with K-means from the same seeds, then explain the extension to general Gaussian components.

**Answer.** E-step: compute soft responsibilities `γᵢk ∝ πk exp(-||xᵢ-μk||²/(2σ²))`. M-step: update `πk=Σᵢγᵢk/N` and `μk=Σᵢγᵢk xᵢ/Σᵢγᵢk`; update common σ² if it is estimated. K-means uses hard assignments and unweighted means, while EM uses soft weights, so early centroids can differ; equal spherical variance links the objectives but does not make every iteration identical. For general Gaussians, update each covariance `Σk=Σᵢγᵢk(xᵢ-μk)(xᵢ-μk)ᵀ/Σᵢγᵢk`, with regularization. Exact Ionosphere trajectories require the dataset and random seeds.

### 8.14 - Gaussian mixtures versus K-means (70%)

**Question.** Fit two spherical Gaussian components of common radius to the specified Ionosphere data with EM; compare convergence and assignments to K-means from the same seeds.

**Answer.** EM alternates responsibilities `γᵢk ∝ πk N(xᵢ|μk,σ²I)` and weighted updates for πk and μk until likelihood change is small. K-means gives hard assignments and minimizes within-cluster squared distance; spherical equal-variance Gaussian EM has a close relationship but uses soft memberships. Exact iterations/quality require the dataset, initialization, radius, and stopping tolerance; those numerical results are not invented.

### 8.15 - Internal validation and algorithm bias (70%)

**Question.** Explain how internal cluster-validity criteria can favor some clustering algorithms over others.

**Answer.** Measures such as SSE favor compact spherical clusters and therefore align with K-means’ objective; density connectivity may value irregular shapes differently. Silhouette balances within-cluster cohesion and nearest-cluster separation but can penalize non-convex structures. Choose a criterion that reflects the intended geometry and corroborate with stability/domain review.

### 8.16 - Oriented Gaussian clusters (60%)

**Question.** Discuss how sum-of-squared-error clustering behaves on elongated, arbitrarily oriented Gaussian groups and what model family could fit better.

**Answer.** Euclidean K-means favors spherical/convex partitions and may split an elongated group or merge nearby oriented groups. A Gaussian mixture with full covariance can represent orientation and differing spreads, provided enough data and careful regularization/model selection. The course covers GMM at a conceptual level; detailed covariance estimation is beyond the local notes, so this is a partial-match conceptual answer.

### 8.17 - Choose algorithms for oriented synthetic clusters (70%)

**Question.** Select clustering algorithms likely to perform well on arbitrarily oriented Gaussian clusters and justify the choices.

**Answer.** A Gaussian mixture with full covariance is a direct model for elliptical, oriented Gaussian components. Spectral or suitable graph-based methods can also capture non-spherical separation, but are more computationally demanding and require additional choices. Plain K-means/SSE is less suitable because it favors spherical clusters. Assess with a metric compatible with the data geometry and held-out/stability checks.

### 8.18 - K-means versus K-medoids and hierarchy (80%)

**Question.** Compare K-means and K-medoids with each other and with AGNES in robustness, supported distances, parameters, and output.

**Answer.** K-means is fast for numeric Euclidean data but uses means and is sensitive to outliers; K-medoids uses observed representatives and arbitrary dissimilarities, usually with greater computational cost. Both require k. AGNES builds a hierarchy and can be cut at different k values, but merge choices are irreversible and linkage changes shape sensitivity. K-means optimizes squared-error compactness; medoids optimize dissimilarity to representatives; AGNES has no single fixed objective across linkages.

### 8.19 - Mahalanobis distance in BIRCH (60%)

**Question.** Explain the change needed for BIRCH to use Mahalanobis distance between points and cluster centroids, with cluster diameter defined as RMS Mahalanobis radius.

**Answer.** Replace Euclidean distance-to-centroid with `(x-μ)ᵀΣ⁻¹(x-μ)` and maintain sufficient statistics to estimate each cluster’s covariance (or use a fixed global covariance). Define RMS radius as the square root of the mean squared Mahalanobis distance. Covariance updates and regularization are required; BIRCH’s own tree mechanics are beyond the locally taught algorithms, so this is a partial method transfer.

### 8.20 - K-means seed choice and purity (60%)

**Question.** On the quantitative KDD intrusion data, seed K-means with one point from each class and compare cluster purity against random seeding.

**Answer.** Normalize quantitative features; choose one labelled representative per class only for the experiment’s initialization; run K-means with fixed k and stopping rule; assign each cluster its majority label and compute purity `Σ_k max_j |C_k∩class_j|/N`. Repeat random initialization many times and compare mean/spread. Because using labels to choose seeds is supervised initialization, describe it as an experimental comparison, not fully unsupervised clustering. Exact purity requires the specified KDD dataset version.

---

### ملاحظات بالعربي - Chapter 08

- **K-means يقلل مجموع مربعات المسافات إلى المتوسطات،** لذا يتأثر بالبدايات والقيم المتطرفة، ونتيجته قد تكون حلًا محليًا.
- **DBSCAN يميز بين core وborder وnoise بحسب ε وMinPts:** تغيير ε قد يدمج المكونات الكثيفة، فلا نفسر ازدياد الترابط كتحسن تلقائي.
- **اختيار خوارزمية التجميع مرتبط بشكل المجموعات وكثافتها ومقياس المسافة:** لا توجد خوارزمية واحدة تناسب كل البيانات.
- **مقاييس التحقق الداخلي قد تفضل أشكالًا معينة من العناقيد؛** اجمع بين المقياس، والرسم أو معرفة المجال، وفحص حساسية الإعدادات.

## Coverage register by source exercise number

| Local chapter | Included source exercises (book chapter.exercise) | Excluded matching extensions / reason |
|:--|:--|:--|
| 01 | Han 1.1-1.10 | Aggarwal Ch1 has no end-of-chapter exercise block in this edition. |
| 02 | Han 2.1-2.5; Han 3.1-3.13 except 3.3(c); Aggarwal 2.1, 2.3, 2.10, 2.13 | Han 3.3(c) below fit threshold; Aggarwal 2.9, 2.14-2.15 require untaught matrix proofs. |
| 03 | Aggarwal 2.2, 2.4-2.8, 2.11-2.12; Aggarwal 3.1-3.8, 3.15 | Aggarwal 3.9-3.11 and 3.12-3.14 are edit/LCSS/DTW programming/proofs beyond local material; external-data calculations are method-only. |
| 04 | Han 3.10; Aggarwal 10.1-10.2 (split-scoring overlap); Aggarwal 7.4 | Advanced clustering-specific feature-selection methods are included only as a conceptual bridge. |
| 05 | Han 6.1-6.8, 6.13-6.14; Han 7.5, 7.6(a-b), 7.10; Aggarwal 4.1-4.22; Aggarwal 5.1-5.5 | Aggarwal 5.6-5.8 are not central to the taught algorithms; Han 6.9-6.12, 6.15 and Han 7.1-7.4, 7.7-7.9 rely on distributed, incremental, multiplicity, cube, or constraint machinery beyond local coverage. |
| 06 | Han 8.1-8.5, 8.10-8.15; Aggarwal 10.1-10.3, 10.9-10.12, 10.19 | Aggarwal 10.4, 10.6, 10.13-10.18, 10.20-10.21 require untaught SVM/LDA or advanced proofs. |
| 07 | Han 8.6-8.8; Aggarwal 10.5, 10.7-10.8, 10.12 | Stream-specific methods and SVM derivations are outside the local lecture depth. |
| 08 | Han 10.1-10.8, 10.12-10.17; Aggarwal 6.1-6.8, 6.9-6.11, 6.14, 6.17-6.19; Aggarwal 7.3-7.4, 7.6 | OPTICS/CLIQUE/BIRCH/ROCK internals, constrained clustering and advanced matrix-factorization proofs are excluded; external KDD/Ionosphere projects have method keys but no dataset-specific output. |

The register includes source exercises even when a project’s numeric output depends on a separately downloaded dataset. Such entries are clearly marked as **method/procedure only** in the answer section; no fabricated dataset result is supplied.

## Items intentionally excluded (below 60% or missing indispensable source data)

- Han Ch3 Exercise 3.3(c): alternative smoothing methods, 40% match.
- Han Ch6 distributed/incremental mining, duplicate-item multiplicity, advanced tree implementation, and coauthor-data project: not in the local association chapter.
- Han Ch7 multilevel/multidimensional cubes, advanced pattern constraints, and PatternFusion topics: insufficient local coverage.
- Han Ch8 stream-specific Naive Bayes variants and full SVM Lagrangian derivations: beyond local treatment.
- Aggarwal Ch10 SVM/XOR and hyperplane-separability exercises: excluded because the local Ch01-Ch08 notes do not teach SVMs or linear-separability proofs.
- Han Ch10 OPTICS, CLIQUE, BIRCH/CHAMELEON-specific internals, constrained/privacy-preserving clustering: not taught in local Chapter 8.
- Aggarwal Ch2 PCA/SVD and external-dataset exercises are retained only as partial conceptual/procedure matches; dataset-specific numeric keys are not claimed without the exact data/preprocessing.
- Aggarwal Ch3 long coding projects for edit distance/LCSS/DTW are excluded; the local portability chapter does not teach those algorithms.
- The Aggarwal Ch4/5 numeric basket tables included in this pack were read from the local textbook pages and independently recounted; exercises requiring separately downloaded UCI/KDD/Musk/Intel files remain procedure-only.
- Aggarwal Ch7 exercises on K-modes, ROCK, must-link/cannot-link constraints, and incremental cluster-feature covariance are excluded; its Mahalanobis transfer, wrapper-selection connection, and K-means seed comparison are retained as partial matches.

## Five-pass review record

1. **Chapter-fit:** screened against the local syllabus, lecture notes, feature-selection seminar, and chapter quiz topics; mixed exercises were split and below-60% parts excluded.
2. **Source identity:** preserved each book’s own chapter/exercise numbering; course chapter labels are kept separate because the two numbering systems do not correspond one-to-one.
3. **Prompt wording:** normalized OCR only in paraphrase; supplied values, thresholds, and task conditions are retained in the paraphrased prompts. Exercises requiring separately downloaded datasets are presented as procedures only, without unsupported numeric outputs.
4. **Solution audit:** recomputed the numeric results included here: grouped median, quartile fences, bin means, normalization values, set similarities, association supports/confidences, K-means trace, and 1D K-means SSE. Conceptual solutions were checked against the local definitions and algorithms.
5. **Delivery audit:** checked prompt-to-answer mapping, formulas, stated assumptions, exclusions, and source provenance. This is an independently derived study pack, not an official answer key. Source-table exercises with supplied local book tables have numeric results; exercises requiring separate UCI/KDD/Intel data are labeled procedure-only, with no invented outputs.

## Retrieval questions

1. **What separates KDD from data mining?** KDD is the full preparation-to-presentation process; data mining is its pattern-discovery step.
2. **Why is 70 only a potential outlier in the 27-age example?** The IQR fence flags it statistically, but domain evidence is needed to decide whether it is erroneous.
3. **What is Apriori’s pruning basis?** Every subset of a frequent itemset must itself be frequent.
4. **Why can a 90% confidence rule still be negatively associated?** If the consequent’s base rate exceeds 90%, its lift can be below 1.
5. **What does K-means++ improve?** It spreads initial centers using squared distance, often improving the starting configuration; it does not guarantee a global optimum.
6. **Can DBSCAN’s density-reachability be symmetric?** Not necessarily; density-connectedness is symmetric.

## Provenance

- Local syllabus and topic mapping: `01_Syllabus_&_Roadmap.md`.
- Local preparation and data-type methods: `03_Study_Notes/Week_02_Data_Types_and_Preparation.md`.
- Local feature extraction/portability: `03_Study_Notes/Week_03_Feature_Extraction_and_Portability.md`.
- Local feature selection: `03_Study_Notes/Feature_Selection_Techniques.md`.
- Local numeric and association definitions: `03_Study_Notes/DM_Numeric_Drills.md`.
- Local source PDFs: Han, Kamber & Pei, *Data Mining: Concepts and Techniques*, 3rd ed.; Aggarwal, *Data Mining: The Textbook*. Printed page numbers and book exercise numbers should be read from the matching exercise section in each source PDF; the course chapter numbers above are not textbook chapter numbers.

