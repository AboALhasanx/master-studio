# 🗺️ 16-Week Syllabus & Progress Roadmap: Soft Computing

> **Course Code:** CS604  
> **Course Title:** Soft Computing & Neuro-Fuzzy Systems / *الحوسبة المرنة والأنظمة العصبية الضبابية*  
> **Instructor:** Prof. Dr. Abdul Hadi Mohammed Adkhil (*أ.د. عبد الهادي محمد ادخيل*)  
> **Credit Hours:** 2 Units | Weekly Time: Tuesday 08:30 AM – 10:30 AM  
> **Repository Directory:** `01_Semester_1/05_Soft_Computing/`

---

## 1. Course Overview & Master Competency Matrix

This postgraduate course explores computational intelligence paradigms capable of exploiting the tolerance for imprecision, uncertainty, and partial truth to achieve tractability, robustness, and low solution cost. Anchored in the seminal texts of **Jang, Sun, & Mizutani** and **Sivanandam & Deepa**, the curriculum integrates fuzzy logic, neuro-fuzzy modeling (ANFIS), evolutionary computing, and digital shape analysis via Freeman chain codes.

```
+=======================================================================================================+
|                                    16-WEEK PROGRESS TRACKER OVERVIEW                                  |
+=======================================================================================================+
| Completed Weeks: [ 0 / 16 ] | Progress: 0.0% | Status: Initializing Semester 1                        |
+=======================================================================================================+
```

---

## 2. Detailed 16-Week Chronological Roadmap

### 🌫️ Phase 1: Fuzzy Mathematics, Relations & Composition (Weeks 1–4)

- [ ] **Week 01: Introduction to Soft Computing Paradigm vs. Hard Computing**
  - **Topics:** Hard (Classical) Computing vs. Soft (Computational Intelligence) Computing, Key pillars of Soft Computing (Fuzzy Logic, Neural Networks, Evolutionary Algorithms, Probabilistic Reasoning), Tolerance for imprecision and uncertainty, Real-world applications in control systems, pattern recognition, and decision support.
  - **Primary Materials:** Sivanandam & Deepa Chapter 1 (`02_Raw_Materials/Principles of Soft Computing - S N Sivanandam and Deepa S N.pdf`) + `Week 01 - Introduction to Soft Computing.pptx`.
  - **Deliverables:** Hard vs. Soft Computing Comparative Matrix in `03_Study_Notes/Week_01_Soft_Computing_Foundations.md`.
  - **Self-Assessment:** Articulate 4 concrete computer science domains where hard computing fails due to combinatorial explosion or noisy inputs.

- [ ] **Week 02: Classical (Crisp) Sets vs. Fuzzy Sets & Membership Geometries**
  - **Topics:** Crisp sets, Characteristic functions, Fuzzy sets, Membership functions ($\mu_A(x) \in [0, 1]$), Support, Core, Boundaries, $\alpha$-cuts and Strong $\alpha$-cuts, Convexity, Normal fuzzy sets. Geometries of membership functions: Triangular, Trapezoidal, Gaussian, Generalized Bell, Sigmoidal, S-curve.
  - **Primary Materials:** Jang, Sun, Mizutani Chapter 2 (`02_Raw_Materials/Neuro-Fuzzy and Soft Computing - Jang Sun Mizutani (Slides).pdf`) + Sivanandam Chapter 2.
  - **Deliverables:** Mathematical definitions and Python plot generators for standard membership functions in `03_Study_Notes/Week_02_Fuzzy_Sets.md`.
  - **Self-Assessment:** Given a triangular membership function $\text{trimf}(x; 10, 20, 30)$, compute the $\alpha$-cut for $\alpha = 0.4$ and $\alpha = 0.8$.

- [ ] **Week 03: Fuzzy Set Operations (T-Norms, S-Norms, Complements & Aggregations)**
  - **Topics:** Standard Complement, Standard Union (Max / S-norm), Standard Intersection (Min / T-norm). Generalized T-norms (Algebraic product, Bounded difference, Drastic product) and S-norms (Algebraic sum, Bounded sum, Drastic sum). De Morgan’s Laws, Excluded Middle Law and Contradiction Law (and why they do NOT hold in standard fuzzy logic).
  - **Primary Materials:** Jang, Sun, Mizutani Chapter 2 (Sections 2.3–2.4).
  - **Deliverables:** Fuzzy operations derivation and solved problem sheets in `03_Study_Notes/Week_03_Fuzzy_Operations.md`.
  - **Self-Assessment:** Prove algebraically that the Law of Excluded Middle ($A \cup \bar{A} = U$) does not hold for a fuzzy set with $\mu_A(x) = 0.7$.

- [ ] **Week 04: Fuzzy Relations, Cylindrical Extensions & Composition Matrices**
  - **Topics:** Crisp vs. Fuzzy Relations, Cartesian Product, Projection and Cylindrical Extension of fuzzy sets, Fuzzy Composition operators: Max-Min Composition ($R \circ S$), Max-Product Composition ($R \circ_{prod} S$), Max-Average Composition. Transitivity, Reflexivity, and Symmetry in fuzzy relations.
  - **Primary Materials:** Sivanandam Chapter 3 + Jang, Sun, Mizutani Chapter 3.
  - **Deliverables:** Max-Min and Max-Product matrix composition calculation drills in `03_Study_Notes/Week_04_Fuzzy_Relations.md`.
  - **Self-Assessment:** Compute the $3 \times 3$ Max-Min composition matrix $T = R \circ S$ for two given fuzzy relation matrices.

---

### ⚙️ Phase 2: Fuzzy Inference Systems & Defuzzification (Weeks 5–8)

- [ ] **Week 05: Linguistic Variables, Fuzzy Propositions & Fuzzy IF-THEN Rules**
  - **Topics:** Linguistic variables (Name, Term set, Universe of discourse, Base variable, Semantic rule), Linguistic hedges (*very, somewhat, slightly, extremely*), Fuzzy propositions (Canonical forms), Fuzzy IF-THEN Rules (Fuzzy implication operators: Mamdani Minimum, Larsen Product, Zadeh Arithmetic, Gödel implication).
  - **Primary Materials:** Jang, Sun, Mizutani Chapter 3 (Sections 3.2–3.4).
  - **Deliverables:** Linguistic hedge transformation tables in `03_Study_Notes/Week_05_Fuzzy_Rules.md`.
  - **Self-Assessment:** Express the rule *"IF Temperature is Very High AND Pressure is Slightly Low THEN Valve is Wide Open"* using formal fuzzy relations.

- [ ] **Week 06: Fuzzy Inference Systems (FIS) — The Mamdani Architecture**
  - **Topics:** Structure of an FIS (Fuzzification, Rule Base, Database, Inference Engine, Defuzzification), Mamdani FIS: Min/Product rule firing strength, Clipping vs. Scaling aggregation of output membership functions, Multi-input multi-output (MIMO) decomposition into MISO systems.
  - **Primary Materials:** Jang, Sun, Mizutani Chapter 4 (Section 4.2).
  - **Deliverables:** Step-by-step Mamdani FIS numerical solver in `03_Study_Notes/Week_06_Mamdani_FIS.md`.
  - **Self-Assessment:** Trace a 2-rule Mamdani FIS for inputs $x_0 = 4, y_0 = 7$ and sketch the aggregated output polygon.

- [ ] **Week 07: Takagi-Sugeno-Kang (TSK) Fuzzy Models & Defuzzification Mathematics**
  - **Topics:** First-order and zero-order Sugeno fuzzy models: Linear consequence functions ($z = p x + q y + r$), Weighted Average defuzzification. Defuzzification methods for Mamdani models: Centroid / Center of Gravity (COG), Center of Largest Area, Bisector of Area (BOA), Mean of Maxima (MOM), Smallest/Largest of Maxima (SOM/LOM).
  - **Primary Materials:** Jang, Sun, Mizutani Chapter 4 (Section 4.3).
  - **Deliverables:** Defuzzification methods mathematical comparison matrix in `03_Study_Notes/Week_07_Defuzzification.md`.
  - **Self-Assessment:** Calculate the defuzzified crisp output using both Centroid (COG) and MOM methods for an asymmetric piecewise linear output set.

- [ ] **Week 08: Midterm Examination & Fuzzy Modeling Synthesis**
  - **Exam Focus:** Comprehensive examination covering Weeks 1–7 (Fuzzy operations, Max-Min compositions, Mamdani/Sugeno FIS manual execution, Defuzzification derivations).
  - **Weight:** 30% of coursework grade.
  - **Deliverables:** Midterm review debrief and error updates in `LEARNER_MODEL.md`.

---

### 🖋️ Phase 3: Digital Contour Chain Codes & Pattern Recognition (Weeks 9–11)

- [ ] **Week 09: Digital Pattern Representation — Freeman Chain Codes (4 & 8-Connectivity)**
  - **Topics:** Boundary representation in digital image processing, Freeman 4-directional and 8-directional chain codes, Coordinate tracking, Grid intersection and boundary quantization algorithms, Chain code storage efficiency compared to raw pixel arrays.
  - **Primary Materials:** `Digital Recognition - The Power of Chain Code.pdf` + Primary Freeman (1961) papers.
  - **Deliverables:** Chain code generation guide & trace diagrams in `03_Study_Notes/Week_09_Chain_Codes.md`.
  - **Self-Assessment:** Trace the 8-directional Freeman chain code for a digital closed binary contour on an $8 \times 8$ grid.

- [ ] **Week 10: Invariant Contour Encoding — First Difference, Derivatives & Shape Numbers**
  - **Topics:** Rotation invariance of chain codes: Modulo-8 first difference (derivative chain code) $d_i = (c_i - c_{i-1} + 8) \pmod 8$. Scale invariance: Re-sampling grid resolution. Normalization: Finding the minimum magnitude integer sequence (Shape Number). Applications in signature verification, OCR, and medical shape analysis.
  - **Primary Materials:** Research papers on Freeman Chain Code normalization.
  - **Deliverables:** Solved chain code normalization drills in `03_Study_Notes/Week_10_Chain_Code_Normalization.md`.
  - **Self-Assessment:** Compute the First Difference and normalized Shape Number for the chain sequence `01234567`.

- [ ] **Week 11: Foundations of Artificial Neural Networks — Perceptrons & MLP**
  - **Topics:** Biological neuron analogy, McCulloch-Pitts neuron model, Single-Layer Perceptron and Perceptron Learning Rule, The Linear Separability problem (XOR limitation), Multi-Layer Perceptrons (MLP), Activation functions (Sigmoid, Tanh, ReLU, Softmax).
  - **Primary Materials:** Sivanandam Chapter 5 + Jang, Sun, Mizutani Chapter 8.
  - **Deliverables:** Neural network architectures summary in `03_Study_Notes/Week_11_Neural_Networks.md`.
  - **Self-Assessment:** Prove algebraically why a single-layer perceptron cannot solve the XOR logic function.

---

### 🧬 Phase 4: ANFIS, Neuro-Fuzzy & Evolutionary Hybridization (Weeks 12–16)

- [ ] **Week 12: Backpropagation Learning Algorithm & Feedforward Networks**
  - **Topics:** Multi-layer feedforward architecture, Error backpropagation algorithm (Gradient Descent on sum of squared errors), Chain rule derivation for output and hidden layer weight updates, Momentum term, Learning rate tuning, Overfitting and regularization.
  - **Primary Materials:** Jang, Sun, Mizutani Chapter 9 + Sivanandam Chapter 6.
  - **Deliverables:** Backpropagation mathematical derivation step-by-step notes in `03_Study_Notes/Week_12_Backpropagation.md`.
  - **Self-Assessment:** Derive the weight update formula $\Delta w_{jk} = \eta \delta_k o_j$ for an output neuron with sigmoid activation.

- [ ] **Week 13: Radial Basis Function Networks (RBFN) & Self-Organizing Maps (SOM)**
  - **Topics:** Radial Basis Function Networks: Architecture, Gaussian receptive fields, Exact interpolation vs. Approximate RBFN, Clustering-based center selection. Kohonen Self-Organizing Maps (SOM): Unsupervised competitive learning, Topological neighborhood updates.
  - **Primary Materials:** Jang, Sun, Mizutani Chapters 10 & 11.
  - **Deliverables:** RBFN vs. MLP comparative matrix in `03_Study_Notes/Week_13_RBFN_and_SOM.md`.
  - **Self-Assessment:** Contrast the global approximation property of MLPs with the localized receptive field property of RBFNs.

- [ ] **Week 14: Adaptive Neuro-Fuzzy Inference Systems (ANFIS) — 5-Layer Blueprint**
  - **Topics:** Synergy of Neural Networks (learning capability) and Fuzzy Logic (interpretability), Architecture of ANFIS: Layer 1 (Premise membership), Layer 2 (Firing strength / T-norm), Layer 3 (Normalized firing strength), Layer 4 (Consequent first-order Sugeno polynomials), Layer 5 (Summation output).
  - **Primary Materials:** Jang, Sun, Mizutani Chapter 12.
  - **Deliverables:** 5-Layer ANFIS Architectural Blueprint Diagram (Mermaid) in `06_Diagrams_&_Mindmaps/`.
  - **Self-Assessment:** Formulate the mathematical node functions for all 5 layers of a 2-rule, 2-input ANFIS model.

- [ ] **Week 15: ANFIS Hybrid Learning Algorithm & Evolutionary Optimization**
  - **Topics:** The Hybrid Learning Algorithm: Forward pass (Fix premise parameters, optimize linear consequent parameters via Least Squares Estimation LSE), Backward pass (Fix consequent parameters, optimize nonlinear premise parameters via Gradient Descent / Backpropagation). Genetic Algorithms (GA) overview: Chromosome representation, Selection, Crossover, Mutation for fuzzy parameter optimization.
  - **Primary Materials:** Jang, Sun, Mizutani Chapters 12 & 15.
  - **Deliverables:** ANFIS Hybrid Learning & Optimization notes in `03_Study_Notes/Week_15_ANFIS_Hybrid_Learning.md`.
  - **Self-Assessment:** Explain why combining LSE with Gradient Descent converges orders of magnitude faster than pure backpropagation in ANFIS.

- [ ] **Week 16: Comprehensive Course Review & Final Examination**
  - **Activities:** Comprehensive mock examination covering all aspects of Fuzzy Logic, Chain Codes, Neural Networks, and ANFIS; Professor exam pattern review.
  - **Deliverables:** 100-Question Soft Computing Master Anki deck in `07_Quizzes_&_Anki/`.
  - **Final Target:** Score $\ge 90\%$ (Distinction / *امتياز*).

---

## 3. Assessment & Grading Criteria

| Component | Weight | Target Score | Description |
|:---|:---:|:---:|:---|
| **Homework Problem Sets & Calculation Drills** | 10% | 10% | Weekly manual matrix, chain code, and fuzzy inference exercises |
| **Applied ANFIS / Chain Code Research Assignment** | 15% | 14% | Technical report on contour recognition or neuro-fuzzy modeling |
| **Oral Research Seminar Presentation (Marp)** | 15% | 14% | 10-slide presentation on hybrid soft computing architectures |
| **Midterm Examination (Week 08)** | 20% | 19% | Written examination on Fuzzy Mathematics, Relations & FIS |
| **Final Semester Examination (Week 16)** | 40% | 36% | Comprehensive written examination |
| **Total Course Grade** | **100%** | **$\ge 93\%$** | **Grade Target: High Distinction (امتياز مرتفع)** |
