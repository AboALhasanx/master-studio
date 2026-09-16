# 🗺️ 16-Week Syllabus & Progress Roadmap: Artificial Intelligence

> **Course Code:** CS605  
> **Course Title:** Artificial Intelligence & Intelligent Agents / *الذكاء الاصطناعي والأنظمة الذكية*  
> **Instructor:** Prof. Dr. Saif Ali Al-Saidi (*أ.د. سيف علي الساعدي*)  
> **Credit Hours:** 3 Units | Weekly Time: Tuesday 10:30 AM – 01:30 PM (3 Contact Hours)  
> **Repository Directory:** `01_Semester_1/06_Artificial_Intelligence/`

---

## 1. Course Overview & Master Competency Matrix

Anchored in **Stuart Russell and Peter Norvig's** world-standard reference (*Artificial Intelligence: A Modern Approach*), this flagship 3-credit core course provides rigorous mathematical and algorithmic mastery of intelligent agent systems. The curriculum spans formal problem formulation, classical state-space search (uninformed and heuristic), memory-bounded optimization, game-theoretic adversarial decision making, constraint satisfaction, automated theorem proving, and classical planning.

```
+=======================================================================================================+
|                                    16-WEEK PROGRESS TRACKER OVERVIEW                                  |
+=======================================================================================================+
| Completed Weeks: [ 0 / 16 ] | Progress: 0.0% | Status: Initializing Semester 1                        |
+=======================================================================================================+
```

---

## 2. Detailed 16-Week Chronological Roadmap

### 🤖 Phase 1: Rational Agents & State Space Search Foundations (Weeks 1–4)

- [ ] **Week 01: Introduction to Modern AI & The Rational Agent Paradigm**
  - **Topics:** What is AI? Four historical definitions (Thinking Humanly, Thinking Rationally, Acting Humanly: Turing Test, Acting Rationally: Rational Agents). The Agent Function $f: P^* \rightarrow A$ and Agent Program. Rationality vs. Omniscience. Foundations of AI (Philosophy, Mathematics, Economics, Neuroscience, Cybernetics).
  - **Primary Materials:** Russell & Norvig (AIMA) Chapter 1.
  - **Deliverables:** AI Foundations & Agent Philosophy summary in `03_Study_Notes/Week_01_AI_Foundations.md`.
  - **Self-Assessment:** Distinguish between a rational agent and an omniscient agent using a concrete navigation example.

- [ ] **Week 02: Intelligent Agent Architectures & PEAS Task Environments**
  - **Topics:** The PEAS framework (Performance measure, Environment, Actuators, Sensors). Seven environment dimensions (Observable, Deterministic, Episodic, Static, Discrete, Single-agent, Known). Five Agent Architectures: Simple Reflex Agents, Model-Based Reflex Agents, Goal-Based Agents, Utility-Based Agents, Learning Agents.
  - **Primary Materials:** Russell & Norvig (AIMA) Chapter 2.
  - **Deliverables:** Complete PEAS Specification Matrix for 6 diverse autonomous systems in `03_Study_Notes/Week_02_PEAS_Environments.md`.
  - **Self-Assessment:** Specify the complete PEAS and 7 environment properties for an Autonomous Medical Diagnosis Agent.

- [ ] **Week 03: Problem Formulation & Uninformed State Space Search**
  - **Topics:** Problem-solving agents, Formulating problems as 5-tuples: $\langle S_0, Actions(s), Result(s, a), GoalTest(s), PathCost(c) \rangle$. State space vs. Search tree vs. Search graph. Uninformed search algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), Depth-Limited Search (DLS), Iterative Deepening Search (IDS).
  - **Primary Materials:** Russell & Norvig (AIMA) Chapter 3 (Sections 3.1–3.4).
  - **Deliverables:** Uninformed search algorithm trace worksheets in `03_Study_Notes/Week_03_Uninformed_Search.md`.
  - **Self-Assessment:** Trace node expansion for BFS and DFS on a 10-node graph; compare time $O(b^d)$ vs space $O(bd)$ complexities.

- [ ] **Week 04: Uniform-Cost Search (UCS) & Algorithmic Complexity Evaluation**
  - **Topics:** Uniform-Cost Search (Dijkstra's algorithm on trees/graphs), Handling arbitrary non-negative step costs, Priority Queue management. Rigorous evaluation of search criteria: Completeness, Optimality, Time Complexity, Space Complexity across BFS, DFS, DLS, IDS, UCS ($b, d, m, C^*, \epsilon$). Bidirectional Search principles.
  - **Primary Materials:** Russell & Norvig (AIMA) Chapter 3 (Section 3.4).
  - **Deliverables:** Search Complexity Master Comparison Matrix in `03_Study_Notes/Week_04_Search_Complexities.md`.
  - **Self-Assessment:** Trace UCS on a weighted road network graph; prove why UCS is optimal when all step costs are $\ge \epsilon > 0$.

---

### 🔍 Phase 2: Informed (Heuristic) Search & Optimization (Weeks 5–8)

- [ ] **Week 05: Informed Heuristic Search — Greedy Best-First & The A* Algorithm**
  - **Topics:** Heuristic functions $h(n)$, Greedy Best-First Search ($f(n) = h(n)$) and its vulnerabilities (suboptimality, incompleteness in loopy graphs), The A* Search Algorithm ($f(n) = g(n) + h(n)$), Priority queue frontier management, Graph Search vs. Tree Search duplicates.
  - **Primary Materials:** Russell & Norvig (AIMA) Chapter 3 (Sections 3.5–3.6).
  - **Deliverables:** Step-by-step A* Graph Search trace guide in `03_Study_Notes/Week_05_A_Star_Algorithm.md`.
  - **Self-Assessment:** Trace A* search on the Romania map problem from Arad to Bucharest with explicit frontier state tracking.

- [ ] **Week 06: Heuristic Properties — Admissibility, Consistency & Dominance Proofs**
  - **Topics:** Mathematical condition for Admissibility in Tree Search ($0 \le h(n) \le h^*(n)$), Mathematical condition for Consistency (Monotonicity) in Graph Search ($h(n) \le c(n, a, n') + h(n')$), Triangle inequality geometric proof, Proof that Consistency implies Admissibility, Heuristic Dominance ($h_2 \ge h_1$), Inventing admissible heuristics (Relaxed problems, Pattern databases).
  - **Literature:** Russell & Norvig Chapter 3 (Section 3.6) + Pearl — *Heuristics: Intelligent Search Strategies*.
  - **Deliverables:** Mathematical Heuristic Proofs Sheet in `03_Study_Notes/Week_06_Heuristic_Proofs.md`.
  - **Self-Assessment:** Construct an algebraic proof that A* Graph Search using a consistent heuristic never reopens an explored node.

- [ ] **Week 07: Memory-Bounded Search & Local Search Optimization**
  - **Topics:** Memory bottlenecks in A*. Memory-bounded algorithms: Iterative Deepening A* (IDA*), Recursive Best-First Search (RBFS), Simplified Memory-Bounded A* (SMA*). Local Search in continuous/discrete spaces: Hill-Climbing (Local maxima, Ridges, Plateaux), Simulated Annealing ($P = e^{\Delta E / T}$), Local Beam Search, Genetic Algorithms (GA).
  - **Primary Materials:** Russell & Norvig (AIMA) Chapter 3 (Section 3.6) & Chapter 4.
  - **Deliverables:** Memory-Bounded Search & Optimization Guide in `03_Study_Notes/Week_07_Local_Search.md`.
  - **Self-Assessment:** Trace SMA* with a memory limit of 3 nodes and illustrate node dropping and ancestor $f$-cost backup.

- [ ] **Week 08: Midterm Examination & State Space Search Synthesis**
  - **Exam Focus:** Comprehensive examination covering Weeks 1–7 (PEAS formulation, uninformed search traces, A* execution, admissibility/consistency mathematical proofs, local search mechanics).
  - **Weight:** 30% of coursework grade.
  - **Deliverables:** Midterm exam debrief and error log updates in `LEARNER_MODEL.md`.

---

### ♟️ Phase 3: Adversarial Games & Constraint Satisfaction (Weeks 9–12)

- [ ] **Week 09: Adversarial Search — Game Trees & The Minimax Algorithm**
  - **Topics:** Games as search problems, Zero-sum games of perfect information, Game tree formulation (MAX and MIN players), The Minimax value definition, Minimax algorithm recursion, Properties of Minimax (Completeness, Optimality vs. optimal opponent, Time $O(b^m)$, Space $O(bm)$), Evaluation functions for state cutoff ($v(s) = w_1 f_1(s) + w_2 f_2(s)$).
  - **Primary Materials:** Russell & Norvig (AIMA) Chapter 5 (Sections 5.1–5.2).
  - **Deliverables:** Minimax Game Tree manual calculation notes in `03_Study_Notes/Week_09_Minimax_Algorithm.md`.
  - **Self-Assessment:** Trace the minimax value backup on a 4-ply game tree with 16 terminal leaf payoffs.

- [ ] **Week 10: Alpha-Beta Pruning & Monte Carlo Tree Search (MCTS)**
  - **Topics:** The Alpha-Beta pruning optimization, Exact meaning of $\alpha$ (highest value for MAX) and $\beta$ (lowest value for MIN), Pruning condition ($\alpha \ge \beta$), Move ordering impact ($O(b^{m/2})$ optimal time complexity), Horizon effect and Quiescence search, Modern Monte Carlo Tree Search (MCTS): Selection (UCT formula), Expansion, Simulation / Rollout, Backpropagation.
  - **Primary Materials:** Russell & Norvig (AIMA) Chapter 5 (Sections 5.3–5.6) + Silver et al., "Mastering the game of Go with deep neural networks and tree search" (*Nature*, `https://doi.org/10.1038/nature16961`).
  - **Deliverables:** Alpha-Beta Pruning step-by-step trace diagram in `06_Diagrams_&_Mindmaps/`.
  - **Self-Assessment:** Execute Alpha-Beta pruning on a 3-ply tree showing exact $(\alpha, \beta)$ intervals at all internal nodes.

- [ ] **Week 11: Constraint Satisfaction Problems (CSP) & Arc Consistency (AC-3)**
  - **Topics:** Standard CSP definition: Variables $X$, Domains $D$, Constraints $C$. Constraint Graph representation. Types of constraints (Unary, Binary, Higher-order, Global: AllDiff). Constraint Propagation: Node Consistency, Arc Consistency (AC-3 algorithm pseudocode and queue tracking), Path Consistency, $k$-consistency.
  - **Primary Materials:** Russell & Norvig (AIMA) Chapter 6 (Sections 6.1–6.2).
  - **Deliverables:** AC-3 Algorithm Trace Walkthrough in `03_Study_Notes/Week_11_CSP_and_AC3.md`.
  - **Self-Assessment:** Trace the AC-3 algorithm queue for the Australia Map Coloring problem until arc consistency is established.

- [ ] **Week 12: CSP Backtracking Search Heuristics**
  - **Topics:** Backtracking Search as depth-first search for CSPs. Variable ordering heuristics: Minimum Remaining Values (MRV / Most Constrained Variable), Degree Heuristic (Tie-breaker). Value ordering heuristic: Least Constraining Value (LCV). Interleaving search and inference: Forward Checking, Maintaining Arc Consistency (MAC).
  - **Primary Materials:** Russell & Norvig (AIMA) Chapter 6 (Sections 6.3–6.5).
  - **Deliverables:** CSP Backtracking with MRV/LCV trace drills in `03_Study_Notes/Week_12_CSP_Backtracking.md`.
  - **Self-Assessment:** Solve an 8-Queens problem instance using Backtracking search with Forward Checking and MRV.

---

### 🧠 Phase 4: Logic, Knowledge Representation & Planning (Weeks 13–16)

- [ ] **Week 13: Knowledge Representation & Propositional Logic Inference**
  - **Topics:** Knowledge-Based Agents, Propositional Logic syntax and semantics, Entailment ($\alpha \models \beta$), Models and Truth Tables, Inference rules (Modus Ponens, Resolution), Conjunctive Normal Form (CNF) conversion, Resolution Refutation proof procedure for propositional logic.
  - **Primary Materials:** Russell & Norvig (AIMA) Chapter 7.
  - **Deliverables:** Propositional CNF Conversion & Resolution Refutation notes in `03_Study_Notes/Week_13_Propositional_Logic.md`.
  - **Self-Assessment:** Convert a complex propositional knowledge base to CNF and prove an entailment query via Resolution Refutation.

- [ ] **Week 14: First-Order Logic (FOL), Unification & Automated Reasoning**
  - **Topics:** Limitations of Propositional Logic, First-Order Logic syntax: Objects, Relations, Functions, Predicates, Quantifiers ($\forall, \exists$), Universal/Existential Instantiation, Generalized Modus Ponens, The Most General Unifier (MGU) algorithm, Forward Chaining and Backward Chaining algorithms in Datalog/Prolog knowledge bases.
  - **Primary Materials:** Russell & Norvig (AIMA) Chapters 8 & 9.
  - **Deliverables:** First-Order Logic Unification and Chaining guide in `03_Study_Notes/Week_14_First_Order_Logic.md`.
  - **Self-Assessment:** Compute the Most General Unifier $\text{UNIFY}(P(x, f(g(y))), P(a, f(z)))$ step-by-step.

- [ ] **Week 15: Classical Planning (STRIPS / PDDL) & Probabilistic Reasoning**
  - **Topics:** Classical Planning: State representation, Action schemas (Preconditions, Add Effects, Delete Effects) in PDDL / STRIPS, Forward state-space search (Progression) vs. Backward search (Regression), Planning graphs and Graphplan. Introduction to Probabilistic Reasoning: Bayesian Networks, Conditional Probability Tables (CPTs), Exact inference by enumeration.
  - **Primary Materials:** Russell & Norvig (AIMA) Chapters 10 & 13.
  - **Deliverables:** PDDL Domain/Problem definitions & Bayesian Network notes in `03_Study_Notes/Week_15_Planning_and_Bayesian_Networks.md`.
  - **Self-Assessment:** Write a complete PDDL domain and problem definition for the classic Blocks World planning domain.

- [ ] **Week 16: Comprehensive Course Review & Final Examination Preparation**
  - **Activities:** Comprehensive mock exam covering the full Russell & Norvig syllabus: state-space search traces, heuristic consistency proofs, Alpha-Beta game tree pruning, AC-3 constraint propagation, and FOL resolution refutation.
  - **Deliverables:** 100-Question AI Master Anki deck export in `07_Quizzes_&_Anki/`.
  - **Final Target:** Score $\ge 90\%$ (Distinction / *امتياز*).

---

## 3. Assessment & Grading Criteria

| Component | Weight | Target Score | Description |
|:---|:---:|:---:|:---|
| **Homework Problem Sets & Search Traces** | 10% | 10% | Weekly manual priority queue, game tree, and CSP trace assignments |
| **Applied Heuristic Search Project** | 15% | 14% | Algorithm implementation and benchmark report on heuristic optimization |
| **Oral Research Seminar Presentation (Marp)** | 15% | 14% | 10-slide presentation on modern autonomous agent algorithms |
| **Midterm Examination (Week 08)** | 20% | 19% | Written examination on Agents, Search, Heuristics & Proofs |
| **Final Semester Examination (Week 16)** | 40% | 36% | Comprehensive written examination |
| **Total Course Grade** | **100%** | **$\ge 93\%$** | **Grade Target: High Distinction (امتياز مرتفع)** |
