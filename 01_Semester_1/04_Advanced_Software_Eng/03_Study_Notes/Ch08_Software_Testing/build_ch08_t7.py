# -*- coding: utf-8 -*-
"""
Build script for ASE Chapter 8: T7 Computational Models & Metric Derivations Pack
Aggarwal & Singh (3rd ed.), Exercise 8.32 and foundational computational testing models
"""
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

OUT_PATH = r"01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch08_Software_Testing\T7_Calculations.md"

header = """---
title: "ASE Chapter 8 — T7 Computational Models & Metric Derivations Pack"
course: "Advanced Software Engineering (CS603)"
instructor: "Asst. Prof. Dr. Ali Fahim Ni'ma"
author: "Master Studio Engine"
date: "2026-10-22"
lang: "en"
---

# ASE Chapter 8 — T7 Computational Models & Metric Derivations Pack

<!-- Print-hidden metadata: Core computational models, complexity metrics, matrix powers, and reliability calculations from Aggarwal & Singh (3rd ed., pp. 375–458). -->
"""

items = [
    {
        "id": "8.32",
        "title": "Cyclomatic Complexity Mathematical Framework & Tri-Method Derivation (Exercise 8.32)",
        "prompt": "What is cyclomatic complexity? Explain with the help of an example.",
        "answer": """> **Mathematical Foundations and Tri-Method Derivation of Cyclomatic Complexity:**
>
> **1. Theoretical Definition and Core Significance:**
> - **Cyclomatic Complexity $V(G)$** is a quantitative structural metric developed by Thomas J. McCabe (1976) based on graph theory.
> - It measures the **amount of decision logic in a source code module** and provides a mathematical upper bound on the **number of linearly independent paths** forming a basis set for testing.
> - Executing all $V(G)$ basis paths guarantees 100% Statement Coverage and 100% Branch Coverage.
>
> **2. The Three Formal Mathematical Methods for Calculating $V(G)$:**
>
> - **Method 1: Graph Theoretic (Euler Characteristic) Formula:**
>   $$V(G) = e - n + 2P$$
>   where:
>   - $e$ = Total number of directed edges in the Control Flow Graph (CFG).
>   - $n$ = Total number of nodes (vertices) in the CFG.
>   - $P$ = Number of **connected components** of the flow graph ($P = 1$ for a standard single-entry, single-exit program module).
>   - When a main program and subroutines are evaluated as a collection of $K$ separate connected graphs, $V(C) = \\sum_{i=1}^K V(C_i) = e - n + 2K$ (textbook pp. 423–424).
>   - For a single program module ($P = 1$), the equation simplifies to:
>     $$V(G) = e - n + 2$$
>
> - **Method 2: Predicate Decision Nodes Formula:**
>   $$V(G) = \\Pi + 1$$
>   where:
>   - $\\Pi$ = Number of predicate (decision) nodes in the flow graph.
>   - **Strict Structural Restriction (Textbook p. 424):** This formula requires that **every predicate node has exactly two outgoing edges** (one for True, one for False). If a decision structure has more than two outgoing edges (e.g., a multi-way `switch`/`case`), it must be converted into equivalent binary decision nodes; otherwise, $\\Pi + 1$ is not directly applicable.
>   - **Compound Condition Rule:** If a predicate contains compound boolean operators with $k$ conditions (e.g., `if (A && B)`), it decomposes into $k$ simple binary decision points.
>
> - **Method 3: Planar Enclosed Regions Formula:**
>   $$V(G) = \\text{Number of Planar Regions} = R_{\\text{bounded}} + 1$$
>   where:
>   - In a planar flow graph, each closed geometric area bounded by edges forms an internal region.
>   - Adding 1 accounts for the single unbounded region exterior to the graph.
>
> **3. Canonical Worked Example (Textbook Example 8.15, pp. 424–425, Fig. 8.23):**
> Consider the canonical program flow graph from Example 8.15 (Fig. 8.23):
> - **Graph Topology Metrics:**
>   - Total Nodes: $n = 10$
>   - Total Directed Edges: $e = 13$
>   - Connected Components: $P = 1$
>   - Predicate Decision Nodes: $\\Pi = 4$ (each strictly with 2 outgoing edges)
>   - Planar Regions: 4 internal bounded regions $+ 1$ exterior region = 5 regions
> - **Verification via Method 1 (Edges and Nodes):**
>   $$V(G) = e - n + 2P = 13 - 10 + 2(1) = 3 + 2 = 5$$
> - **Verification via Method 2 (Predicate Nodes):**
>   $$V(G) = \\Pi + 1 = 4 + 1 = 5$$
> - **Verification via Method 3 (Planar Regions):**
>   $$V(G) = \\text{Number of Regions} = 4 + 1 = 5$$
> - **Conclusion:** All three independent mathematical methods converge identically on **$V(G) = 5$**, proving that exactly 5 linearly independent basis paths must be executed to guarantee full structural coverage.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> احفظ التفاصيل الدقيقة لمعادلات McCabe:
> 1. الرمز $P$ في معادلة $e - n + 2P$ يعني **Connected Components** (المكونات المتصلة) وليس Strongly Connected. للبرنامج المنفرد $P=1$ فتصبح $e - n + 2$. إذا كان المخطط يضم برنامجاً رئيسياً مع دوال فرعية منفصلة كالمثال في ص.424، تُحسب $P$ بعدد الدوال المنفصلة.
> 2. صيغة $\\Pi + 1$ مقيدة بشرط صريح في الكتاب: أن تمتلك كل عقدة شرطية **مخرجين اثنين فقط** (True و False). في حال وجود تفرع متعدد مثل `switch`، يلزم تحويله لعقد ثنائية قبل تطبيق الصيغة.
> 3. مثال الكتاب المنهجي (Example 8.15، ص.425، شكل 8.23) يمتلك $n=10, e=13, \\Pi=4, \\text{Regions}=5$ ويعطي $V(G)=5$ بالطرق الثلاث.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.4.2, pp. 422–425; companion slides 120–139, 209."
    },
    {
        "id": "Module 1",
        "title": "Boundary Value Analysis Test-Case Counting Equations",
        "prompt": "Formulate and prove the test-case volume equations for Standard BVA, Robustness, Worst-Case, and Robust Worst-Case testing for n independent variables.",
        "answer": """> **Mathematical Derivation and Proof of BVA Test-Case Volume Equations:**
>
> **1. Standard Boundary Value Analysis (Single Fault Assumption):**
> - **Formula:**
>   $$T_{\\text{BVA}} = 4n + 1$$
> - **Mathematical Derivation:**
>   - Under the Single Fault Assumption, only one variable takes an extreme boundary value at a time, while all other $n-1$ variables remain fixed at their nominal ($nom$) values.
>   - For each variable $x_i$, exactly 4 boundary points are evaluated: $\\{min, min^+, max^-, max\\}$.
>   - For $n$ variables: $4 \\times n = 4n$ boundary test cases.
>   - Exactly 1 baseline test case evaluates all $n$ variables simultaneously at nominal values: $(nom, nom, \\dots, nom)$.
>   - Total test cases: $4n + 1$.
>
> **2. Robustness Testing (Single Fault Assumption with Error Bounds):**
> - **Formula:**
>   $$T_{\\text{Robust}} = 6n + 1$$
> - **Mathematical Derivation:**
>   - Extends standard BVA by testing 2 additional out-of-boundary invalid points per variable: $min^- (min - \\epsilon)$ and $max^+ (max + \\epsilon)$.
>   - Each variable now contributes 6 boundary points: $\\{min^-, min, min^+, max^-, max, max^+\\}$.
>   - For $n$ variables: $6 \\times n = 6n$ test cases.
>   - Adding the single all-nominal baseline case: $6n + 1$.
>
> **3. Worst-Case Testing (Rejection of Single Fault Assumption):**
> - **Formula:**
>   $$T_{\\text{Worst}} = 5^n$$
> - **Mathematical Derivation:**
>   - Rejects the Single Fault Assumption to detect concurrent multi-variable boundary faults.
>   - Each variable can independently assume any of its 5 standard boundary points: $\\{min, min^+, nom, max^-, max\\}$.
>   - By the Fundamental Counting Principle of Combinatorics, the total number of Cartesian combinations across $n$ independent variables is:
>     $$5 \\times 5 \\times \\dots \\times 5 = 5^n$$
>
> **4. Robust Worst-Case Testing (Combinatorial Extreme Bounds):**
> - **Formula:**
>   $$T_{\\text{RobustWorst}} = 7^n$$
> - **Mathematical Derivation:**
>   - Combines robustness (7 points per variable: $\\{min^-, min, min^+, nom, max^-, max, max^+\\}$) with full combinatorial worst-case testing:
>     $$7 \\times 7 \\times \\dots \\times 7 = 7^n$$
>
> **5. Quantitative Comparative Scaling for $n = 1, 2, 3, 4$ Variables:**
> - For $n = 1$: Standard BVA = 5; Robust = 7; Worst-Case = 5; Robust Worst-Case = 7.
> - For $n = 2$: Standard BVA = 9; Robust = 13; Worst-Case = 25; Robust Worst-Case = 49.
> - For $n = 3$: Standard BVA = 13; Robust = 19; Worst-Case = 125; Robust Worst-Case = 343.
> - For $n = 4$: Standard BVA = 17; Robust = 25; Worst-Case = 625; Robust Worst-Case = 2,401.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> لاحظ النمو الخطي مقابل النمو الأسي:
> - في فرضية العيب المنفرد (Single Fault)، ينمو عدد الحالات خطياً ($4n+1$ و $6n+1$) مما يجعل الفحص سريعاً واقتصادياً.
> - عند رفض فرضية العيب المنفرد، يقفز النمو أسياً ($5^n$ و $7^n$)، حيث يتطلب فحص 4 متغيرات فقط 625 حالة لأسوأ الحالات و 2,401 حالة للرصانة القصوى!""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2.1, pp. 375–380; companion slides 20–34, 189–190."
    },
    {
        "id": "Module 2",
        "title": "Graph Matrix, Connection Matrix & Path Power Arithmetic",
        "prompt": "Explain the mathematical formulation of a Graph Matrix, its derivation of Cyclomatic Complexity via row weights, and how matrix powers calculate k-hop paths.",
        "answer": """> **Mathematical Framework of Graph Matrices and Adjacency Path Arithmetic:**
>
> **1. Formal Definition of a Graph Matrix:**
> - A **Graph Matrix** is a square matrix of dimension $N \\times N$, where $N$ is the total number of nodes in the Control Flow Graph.
> - Rows represent starting/source nodes, and columns represent terminal/destination nodes.
> - Matrix entry $A[i, j]$ denotes the directed edge connecting node $i$ to node $j$:
>   - In a **Connection Matrix**: $A[i, j] = 1$ if a directed edge exists from node $i$ to node $j$; otherwise $A[i, j] = 0$.
>   - In an **Edge-Labeled Graph Matrix**: $A[i, j] = e_k$ where $e_k$ is the unique letter token of the connecting edge.
>
> **2. Derivation of Cyclomatic Complexity via Row Weights:**
> - **Row Weight Definition:** The weight of row $i$ is defined as the total number of outgoing directed edges from node $i$ (the out-degree of node $i$).
>   $$\\text{Weight}(i) = \\sum_{j=1}^N A[i, j]$$
> - **McCabe's Cyclomatic Complexity Formula via Row Weights:**
>   $$V(G) = \\sum_{i=1}^N (\\text{Weight}(i) - 1) + 1 \\quad \\text{for all nodes with } \\text{Weight}(i) > 1$$
> - **Mathematical Equivalence Proof:**
>   - Nodes with $\\text{Weight}(i) = 1$ have a contribution of $1 - 1 = 0$ (sequential nodes).
>   - Terminal/Exit nodes have $\\text{Weight}(exit) = 0$ and do not contribute.
>   - Nodes with $\\text{Weight}(i) > 1$ are predicate decision nodes. For a binary predicate node, $\\text{Weight}(i) = 2$, giving $(2 - 1) = 1$.
>   - Summing over all predicate nodes yields $\\sum 1 = P$. Adding the trailing $+1$ gives $P + 1$, perfectly matching McCabe's Predicate Node Formula!
>
> **3. Calculation of $k$-Hop Paths via Matrix Powers:**
> Let $A$ be the binary $N \\times N$ connection matrix of a flow graph:
> - **Power $A^1$ (1-Hop Paths):** Entry $A^1[i, j]$ gives the number of direct paths of length 1 (single edges) from node $i$ to node $j$.
> - **Power $A^2 = A \\times A$ (2-Hop Paths):** Entry $A^2[i, j] = \\sum_{k=1}^N A[i, k] \\times A[k, j]$ gives the exact number of distinct paths of length 2 from node $i$ to node $j$.
> - **Power $A^k$ ($k$-Hop Paths):** Entry $A^k[i, j]$ gives the exact number of paths of length $k$ traversing exactly $k$ edges from node $i$ to node $j$.
> - **Transitive Closure Matrix $T$:**
>   $$T = A^1 + A^2 + A^3 + \\dots + A^{N-1}$$
>   Entry $T[i, j] > 0$ proves that node $j$ is reachable from node $i$ through at least one valid path. If $T[entry, j] == 0$, node $j$ is **unreachable dead code**.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> مصفوفة الرسم (Graph Matrix) مصفوفة مربعة بحجم $N \\times N$. لحساب التعقيد السايكلوماتي منها: اطرح 1 من وزن كل صف يزيد وزنه عن 1، واجمع النواتج، ثم أضف 1 في النهاية. ورفع مصفوفة الاتصال للقوة $k$ يعطي عدد المسارات بطول $k$ قفزة بين كل عقدتين. إذا كانت الخلية المقابلة لعقدة النهاية في مصفوفة $T$ تساوي صفراً، فهذا إثبات رياضي على وجود كود ميت (Dead Code).""",
        "source": "Aggarwal & Singh (3rd ed.), §8.3.2, pp. 410–415; companion slides 147–155, 196–197."
    },
    {
        "id": "Module 3",
        "title": "Mutation Testing Adequacy & Mutation Score (MS) Formulation",
        "prompt": "Formulate the Mutation Score (MS) metric. Explain equivalent mutants, and solve a concrete numerical problem evaluating test suite adequacy.",
        "answer": """> **Mathematical Formulation of Mutation Testing Adequacy & Concrete Problem Solving:**
>
> **1. Theoretical Principles of Mutation Testing:**
> - Mutation Testing is a fault-based structural testing technique based on two fundamental hypotheses:
>   - **Competent Programmer Hypothesis:** Programmers generally author code that is close to correct; faults consist of minor syntactic slips.
>   - **Coupling Effect Hypothesis:** Complex faults are coupled to simple faults; a test suite capable of detecting simple faults will detect complex faults.
>
> **2. The Mutation Score ($MS$) Mathematical Formulation:**
> $$MS = \\frac{D}{N - E} \\times 100\\%$$
> where:
> - **$D$ (Dead / Killed Mutants):** The number of mutants that produced an observable output failure when executed against the test suite.
> - **$N$ (Total Mutants):** The total number of artificial program mutants generated by applying mutation operators (e.g., replacing `+` with `-`, changing `<` to `<=`).
> - **$E$ (Equivalent Mutants):** The number of mutants that are syntactically distinct from the original program but **semantically identical in behavior** (they produce identical outputs for all possible inputs and can never be killed).
> - **Adequacy Criterion:** A test suite is defined as **mutation-adequate** if and only if **$MS = 100\\%$**.
>
> **3. Concrete Worked Numerical Problem:**
> A testing team generates 250 mutants for a critical financial calculation module. Executing the existing test suite yields the following results:
> - Mutants killed by test cases: $D = 184$
> - Mutants surviving: $S = 66$ (since $N = D + S = 184 + 66 = 250$)
> - Upon formal semantic analysis, 20 of the surviving mutants are proven to be **Equivalent Mutants** ($E = 20$).
>
> **Step-by-Step Numerical Solution:**
> - **Step 1: Calculate the denominator (Non-equivalent mutants):**
>   $$\\text{Effective Mutants} = N - E = 250 - 20 = 230$$
> - **Step 2: Calculate the unkilled non-equivalent mutants:**
>   $$\\text{Surviving Non-Equivalent} = 66 - 20 = 46$$
> - **Step 3: Calculate the Mutation Score ($MS$):**
>   $$MS = \\frac{D}{N - E} \\times 100\\% = \\frac{184}{230} \\times 100\\% = 0.80 \\times 100\\% = 80.0\\%$$
> - **Step 4: Engineering Adequacy Evaluation:**
>   The test suite achieves an 80.0% mutation score. Because $MS < 100\\%$, the test suite is **NOT mutation-adequate**. The 46 surviving non-equivalent mutants reveal specific test gaps. The test team must augment the suite with targeted test cases designed to kill the remaining mutants; note that a single well-designed test case can kill multiple mutants simultaneously.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> أخطر فخ في حساب نسبة الطفرات ($MS$) هو نسيان طرح الطفرات المتكافئة ($E$) من المقام! إذا قسمت $D$ على $N$ مباشرة دون استبعاد $E$ ستكون النتيجة خاطئة ودرجة الامتحان ملغاة. الطفرات المتكافئة تطابق البرنامج الأصلي سلوكياً ومستحيل قتلها بأي مدخل، لذلك تُحذف من المقام. كما يجب تذكر أن وجود 46 طفرة حية لا يعني بالضرورة كتابة 46 حالة اختبار جديدة، لأن حالة الاختبار الواحدة يمكن أن تقتل عدة طفرات في وقت واحد.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.4.5, pp. 430–435; companion slides 167–172, 198."
    },
    {
        "id": "Module 4",
        "title": "Error Seeding & Mills' Hypergeometric Latent Defect Estimation",
        "prompt": "Explain Harlan Mills' Error Seeding model. Derive the estimation formula for total latent faults, and solve a concrete numerical defect prediction scenario.",
        "answer": """> **Harlan Mills' Error Seeding Model and Mathematical Defect Estimation:**
>
> **1. Theoretical Model and Assumptions:**
> - **Error Seeding (Fault Seeding)** is a statistical reliability technique developed by Harlan Mills to estimate the number of latent (undiscovered) real faults remaining in a software system.
> - **Foundational Assumptions:**
>   - Seeded artificial faults ($S$) are inserted randomly into the program.
>   - Seeded faults have the same difficulty of detection and follow the same probability distribution as native (real) faults ($N$).
>   - Testers operate blind: they do not know the identities, locations, or quantity of the seeded faults.
>
> **2. Mathematical Formulation:**
> Let:
> - $S$ = Total number of seeded artificial faults.
> - $s$ = Number of seeded faults discovered during testing.
> - $N$ = Total number of native (real) faults originally present in the software (unknown).
> - $n$ = Number of native (real) faults discovered during testing.
>
> By the principle of proportional capture-recapture (hypergeometric sampling):
> $$\\frac{s}{S} \\approx \\frac{n}{N}$$
> Solving for the total native faults $N$:
> $$\\hat{N} = \\frac{S \\times n}{s}$$
> The estimated number of **remaining latent undiscovered real faults** ($\\hat{N}_{\\text{rem}}$) is:
> $$\\hat{N}_{\\text{rem}} = \\hat{N} - n = \\frac{S \\times n}{s} - n = n \\left( \\frac{S}{s} - 1 \\right)$$
>
> **3. Concrete Worked Numerical Problem:**
> A quality assurance manager seeds 30 artificial faults ($S = 30$) into a newly compiled subsystem prior to testing. Independent testing is conducted, uncovering:
> - Seeded faults detected: $s = 20$
> - Native (real) faults detected: $n = 50$
>
> **Step-by-Step Numerical Solution:**
> - **Step 1: Estimate total native faults originally present in the code:**
>   $$\\hat{N} = \\frac{S \\times n}{s} = \\frac{30 \\times 50}{20} = \\frac{1500}{20} = 75 \\text{ native faults}$$
> - **Step 2: Estimate remaining undiscovered native faults:**
>   $$\\hat{N}_{\\text{rem}} = \\hat{N} - n = 75 - 50 = 25 \\text{ latent faults remaining}$$
> - **Step 3: Calculate the Fault Detection Efficiency ($FDE$):**
>   $$FDE = \\frac{s}{S} \\times 100\\% = \\frac{20}{30} \\times 100\\% = 66.67\\%$$
> - **Step 4: Release Decision Recommendation:**
>   Because an estimated 25 latent defects remain undiscovered, the software fails the institutional target floor and must not be signed off for production deployment without additional targeted testing.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> نموذج بذر الأخطاء (Error Seeding) لهارلان ميلز يشبه تقنية صيد واسترجاع الأسماك في علم البيئة. النسبة بين الأخطاء المغروسة المكتشفة ($s$) إلى إجمالي المغروس ($S$) تساوي نسبة الأخطاء الحقيقية المكتشفة ($n$) إلى إجمالي الأخطاء الحقيقية ($N$). لحساب العيوب المتبقية، احسب أولاً $\\hat{N} = \\frac{S \\times n}{s}$ ثم اطرح $n$.""",
        "source": "Aggarwal & Singh (3rd ed.), §7.3.5, pp. 345–347 (The Bug Seeding Model); Harlan D. Mills (1972)."
    }
]

retrieval_set = """<!-- Print-hidden study guidance retained for screen use.
## Retrieval Set & Active Recall Self-Test

1. Formulate the three mathematical methods used to calculate McCabe's Cyclomatic Complexity V(G).
2. For a module with 14 edges, 11 nodes, and 4 predicate nodes, calculate V(G) using all applicable formulas.
3. State the exact test case count formulas for Standard BVA, Robustness, Worst-Case, and Robust Worst-Case testing.
4. Calculate the total number of test cases required by Worst-Case testing for a function with 5 independent input variables.
5. In a Graph Matrix, define Row Weight and state the formula that calculates V(G) from row weights.
6. What mathematical property is represented by entry (i, j) of matrix power A^3?
7. Write the formula for Mutation Score (MS) and explain why equivalent mutants must be subtracted from the denominator.
8. If 120 mutants are generated, 12 are equivalent, and 90 are killed, calculate the Mutation Score.
9. State Harlan Mills' formula for estimating total native faults N from seeded faults.
10. If 40 faults are seeded, 25 seeded faults are found, and 60 native faults are found, how many undiscovered native faults remain?
-->
"""

def generate():
    content_str = header.strip() + "\n\n---\n\n"
    for item in items:
        block = f"""<div class="no-break">

### {item['id']} · {item['title']}

{item['prompt']}
{{: .keep-next }}
{item['answer']}

{item['note']}

**Source:**
{item['source']}

</div>

---
"""
        content_str += block + "\n"
    
    content_str += retrieval_set.strip() + "\n"
    
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(content_str)
    
    print(f"Generated {OUT_PATH} successfully. Total items: {len(items)}")

if __name__ == "__main__":
    generate()
