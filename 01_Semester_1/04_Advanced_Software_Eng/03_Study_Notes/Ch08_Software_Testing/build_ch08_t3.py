# -*- coding: utf-8 -*-
"""
Build script for ASE Chapter 8: T3 Compare & Analyze Pack
Aggarwal & Singh (3rd ed.), Exercises 8.5, 8.8, 8.14, 8.15, 8.18, 8.28, 8.29, 8.33, 8.36, 8.37, 8.41
"""
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

OUT_PATH = r"01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch08_Software_Testing\T3_Compare_Analyze.md"

header = """---
title: "ASE Chapter 8 — T3 Comparative & Analytical Evaluation Pack"
course: "Advanced Software Engineering (CS603)"
instructor: "Asst. Prof. Dr. Ali Fahim Ni'ma"
author: "Master Studio Engine"
date: "2026-10-22"
lang: "en"
---

# ASE Chapter 8 — T3 Comparative & Analytical Evaluation Pack

<!-- Print-hidden metadata: 11 analytical & comparative exercises from Aggarwal & Singh (3rd ed., pp. 455–458). -->
"""

items = [
    {
        "id": "8.5",
        "title": "Three Fundamental Testing Dichotomies (Exercise 8.5)",
        "prompt": "What is the difference between:\n(i) Alpha testing & beta testing\n(ii) Development & regression testing\n(iii) Functional & structural testing",
        "answer": """> **Comparative analysis of the three core software testing dichotomies:**
>
> **(i) Alpha Testing vs. Beta Testing:**
> - **Environment & Location:** **Alpha testing is conducted at the developer's site** in a controlled laboratory environment. **Beta testing is conducted at end-user customer sites** in real-world, uncontrolled production environments.
> - **Executing Actors:** Alpha testing is performed by internal staff, quality assurance engineers, or invited representative users closely monitored by developers. Beta testing is performed autonomously by external end-users without developer intervention.
> - **Lifecycle Timing:** **Alpha testing precedes beta testing** as the initial acceptance verification milestone before wider pre-release deployment.
> - **Primary Objective:** Alpha testing evaluates internal system stability, core functional completeness, and catches fatal crashes. Beta testing evaluates usability, real-world workflow compatibility, performance across heterogeneous hardware configurations, and unexpected operational quirks.
>
> **(ii) Development Testing vs. Regression Testing:**
> - **Execution Focus:** **Development testing is conducted during the active construction of the software** to discover defects in newly authored code (encompassing unit, integration, and system testing). **Regression testing is conducted after code modifications** (bug fixes, patches, refactoring, or requirement enhancements).
> - **Primary Objective:** Development testing aims to demonstrate that new features satisfy specification requirements. **Regression testing aims to verify that modifications have not introduced unintended defects or side-effects into previously working functionality.**
> - **Test Suite Construction:** Development tests are newly authored alongside code. Regression tests are drawn from an existing, accumulated baseline repository of reusable test suites (often prioritized or automated).
>
> **(iii) Functional Testing vs. Structural Testing:**
> - **Perspective & Knowledge:** **Functional testing (Black-Box testing) treats the software as an opaque box**, deriving test scenarios solely from external requirement specifications without knowledge of internal source code. **Structural testing (White-Box testing) derives test cases from internal program logic**, examining control flow graphs, statements, branches, conditions, and data structures.
> - **Defect Detection Target:** Functional testing excels at detecting missing functionality, interface mismatches, and specification deviations. Structural testing excels at discovering unreachable (dead) code, logic errors, unhandled boundary paths, and state violations within loops.
> - **Coverage Criteria:** Functional coverage is measured against input domain partitions (equivalence classes, boundaries). Structural coverage is measured against code traversal metrics (statement coverage, branch coverage, cyclomatic basis path coverage).""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> في الفحص المقارن:
> - فحص ألفا (Alpha) يكون في موقع المطور وتحت إشرافه، بينما فحص بيتا (Beta) يكون في موقع المستخدم النهائي في بيئة حقيقية غير منضبطة.
> - فحص التطوير (Development) يبحث عن الأخطاء في الكود الجديد، بينما فحص الانحدار (Regression) يضمن أن التعديل أو إصلاح العيوب لم يكسر أجزاء سابقة كانت تعمل بنجاح.
> - الفحص الوظيفي (Functional) يعتمد على المواصفات فقط دون النظر للكود، بينما الفحص الهيكلي (Structural) يعتمد بالكامل على قراءة المسارات والتعليمات البرمجية الداخلية.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.1.5, §8.2, §8.3, §8.6.4, pp. 368–370, 374–375, 442–445; companion slides 16–17, 201."
    },
    {
        "id": "8.8",
        "title": "Limitations of Exhaustive Testing & Proof of Correctness (Exercise 8.8)",
        "prompt": "Will exhaustive testing (even if possible for every small programs) guarantee that the program is 100% correct?",
        "answer": """> **No. Even if exhaustive testing were computationally feasible for small programs, it CANNOT guarantee 100% correctness.**
>
> **Core theoretical and practical justifications:**
> - **Missing Path & Specification Errors:** Exhaustive testing executes only the code that has actually been written. If a critical requirement or specification constraint was completely omitted from the design and source code, no execution of existing paths will detect the missing feature.
> - **Flawed Specification Oracle:** Testing evaluates actual output against expected output defined by the specification. If the specification itself contains ambiguities, logical errors, or invalid requirements, exhaustive testing merely confirms that the program faithfully implements an erroneous specification.
> - **Concurrency & Temporal Non-Determinism:** In multi-threaded, asynchronous, or distributed environments, program correctness depends on execution timing, scheduling sequences, shared memory race conditions, and hardware interrupts. Exhaustive testing of static input combinations fails to explore all dynamic temporal interleavings.
> - **Hardware & Environmental Vulnerabilities:** A software system interacts with operating systems, third-party libraries, device drivers, and physical memory. Failures arising from platform anomalies, stack overflow, or compiler optimization bugs cannot be ruled out by input testing.
> - **Dijkstra's Fundamental Invariant:** As formulated by Edsger W. Dijkstra: **\"Program testing can be used to show the presence of bugs, but never to show their absence!\"** Complete mathematical correctness can only be established through formal mathematical verification, not empirical testing.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> فخ امتحاني حاسم: حتى لو فحصت كل المدخلات الممكنة لبرنامج صغير، فهذا لا يثبت صحة البرنامج 100%. السبب الأساسي: الفحص الشامل لا يكشف المسارات المفقودة (إذا نسي المبرمج كتابة متطلب معين أصلاً)، ولا يكشف أخطاء وثيقة المتطلبات نفسها، فضلاً عن مشاكل التزامن وتداخل الخيوط (Concurrency).""",
        "source": "Aggarwal & Singh (3rd ed.), §8.1.3, pp. 367–368; companion slides 10–12, 202."
    },
    {
        "id": "8.14",
        "title": "Worst-Case vs. Ad-Hoc Test Evaluation & Real Boundary Verification (Exercise 8.14)",
        "prompt": "Discuss the difference between worst test case and adhoc test case performance evaluation by means of testing. How can we be sure that the real worst case has actually been observed?",
        "answer": """> **Comparative evaluation of Worst-Case Testing vs. Ad-Hoc Testing:**
>
> **1. Structural Comparison:**
> - **Theoretical Rigor & Methodology:** **Worst-case testing is a systematic, mathematically deterministic boundary value technique** that rejects the Single Fault Assumption. It evaluates concurrent boundary values by forming Cartesian combinations of five distinct points per variable: $\\{min, min^+, nom, max^-, max\\}$. For $n$ independent input variables, it exhaustively generates exactly **$5^n$ test cases**. In contrast, **ad-hoc testing relies purely on informal tester intuition**, random inputs, or unguided exploratory heuristics without systematic domain stratification.
> - **Repeatability & Traceability:** Worst-case test sets are fully reproducible, traceable to mathematical domain boundaries, and auditable against interface specifications. Ad-hoc tests are unscripted, non-reproducible, and lack formal adequacy metrics.
> - **Defect Detection Profile:** Worst-case testing systematically forces multi-variable boundary collisions, edge-case arithmetic overflows, and compound boundary faults. Ad-hoc testing uncovers serendipitous defects, unexpected user interface behaviors, and usability quirks that structured specifications overlooked.
>
> **2. Verifying Observation of the Real Worst Case:**
> To ensure that the genuine operational worst-case behavior has been observed rather than an arbitrary stress condition:
> - **Formal Domain Boundary Verification:** All physical, logical, arithmetic, and hardware memory boundaries must be rigorously analyzed to identify genuine discontinuity thresholds.
> - **Non-Linear Interaction Proof:** The underlying mathematical transfer function must be evaluated to confirm whether extrema occur strictly at variable boundaries or at interior non-linear inflection points (e.g., saddle points, resonance frequencies).
> - **Stress & Resource Saturation Limits:** Operational worst-case performance requires demonstrating system behavior under maximum boundary concurrency: peak transactional load, minimal available memory, maximum buffer capacities, and worst-case algorithmic complexity paths (e.g., $O(n^2)$ input distributions).""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> الفحص بأسوأ الحالات (Worst-case) فحص منهجي رياضي يولد $5^n$ حالة عبر دمج القيم الحدية لجميع المتغيرات معاً رافضاً فرضية العيب المنفرد. أما الفحص العشوائي (Ad-hoc) فهو فحص استكشافي ارتجالي. للتأكد من رصد أسوأ حالة حقيقية، يجب إثبات أن النظام تم اختباره عند أقصى استهلاك للذاكرة وأسوأ تعقيد خوارزمي وتزامن حدي.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2.1, pp. 377–380; companion slides 27–32, 203."
    },
    {
        "id": "8.15",
        "title": "Equivalence Class Partitioning vs. Boundary Value Analysis (Exercise 8.15)",
        "prompt": "Describe the equivalence class testing method. Compare this with boundary value analysis techniques.",
        "answer": """> **Description and systematic comparison of Equivalence Class Partitioning and Boundary Value Analysis:**
>
> **1. Description of Equivalence Class Testing:**
> - **Core Concept:** Equivalence partitioning divides the input domain of a program into disjoint sub-domains called **equivalence classes**, such that **all data elements within a given class are treated equivalently by the program logic**.
> - **Fundamental Assumption:** If a single test case chosen from an equivalence class exposes an error, all other members of that class will expose the same error. Conversely, if one test case succeeds, all members of that class are assumed to succeed.
> - **Class Stratification:** The input domain is partitioned into:
>   - **Valid Equivalence Classes:** Representing valid, expected operational inputs that the program must process successfully.
>   - **Invalid Equivalence Classes:** Representing invalid, erroneous, or out-of-range inputs that must trigger proper error handling and exception routines.
> - **Test Selection Strategy:**
>   - **Weak Normal:** One test case from each valid equivalence class.
>   - **Strong Normal:** Cartesian product of all valid equivalence classes.
>   - **Weak Robust:** One test case from each valid and invalid equivalence class.
>   - **Strong Robust:** Cartesian product of all valid and invalid equivalence classes.
>
> **2. Systematic Comparison with Boundary Value Analysis (BVA):**
> - **Input Selection Target:** **Equivalence partitioning selects representative values typically from the interior** (nominal center) of each partition. **BVA focuses exclusively on the extreme boundaries and edges** of these partitions ($min, min^+, nom, max^-, max$).
> - **Empirical Justification:** Equivalence partitioning ensures broad functional domain coverage and prevents redundant interior testing. BVA exploits the empirical observation that **programming faults occur with disproportionate frequency at boundaries** (e.g., off-by-one errors, `<` vs. `<=`, array index limits).
> - **Test Case Volume:** Standard single-variable BVA generates exactly **$4n + 1$ test cases** for $n$ variables. Weak normal equivalence testing generates tests proportional to the maximum number of partitions per variable $\max(k_i)$.
> - **Synergistic Application:** BVA and equivalence partitioning are inherently complementary: equivalence partitioning identifies the valid and invalid partitions, while BVA determines the critical test boundaries along the borders of those exact partitions.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> تجزئة فئات التكافؤ تختار عنصراً ممثلاً واحداً من داخل كل فئة (صالحة أو غير صالحة) لتقليل حجم الفحص. أما تحليل القيم الحدية (BVA) فيركز حصراً على حواف ونقاط التماس ($min, min^+, nom, max^-, max$) لأن معظم أخطاء المبرمجين تقع عند الحدود (مثل أخطاء Off-by-one).""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2.1 & §8.2.2, pp. 375–384; companion slides 20–46, 203."
    },
    {
        "id": "8.18",
        "title": "Usefulness & Practical Effectiveness of Decision Table Testing (Exercise 8.18)",
        "prompt": "Explain the usefulness of decision table during testing. Is it really effective? Justify your answer.",
        "answer": """> **Analytical justification of the usefulness and effectiveness of Decision Table Testing:**
>
> **1. Usefulness of Decision Tables in Software Testing:**
> - **Modeling Complex Boolean Interactions:** While BVA and equivalence partitioning treat input variables independently under the single-fault assumption, **decision tables excel at modeling complex combinations and logical interdependencies between multiple input conditions**.
> - **Formal Specification Verification:** A decision table forces the requirements engineer and tester to explicitly state every logical condition ($C_1, C_2, \dots, C_k$) and map it directly to resultant actions ($A_1, A_2, \dots, A_m$).
> - **Detection of Completeness Gaps & Ambiguities:** Constructing a complete decision table with $2^k$ rules systematically exposes missing specification cases (conditions for which no action is defined) and contradictory requirements (identical conditions triggering mutually exclusive actions).
> - **Systematic Test Case Derivation:** **Each non-redundant column (decision rule) translates directly into a distinct, executable test case**, providing 100% decision rule coverage.
>
> **2. Practical Effectiveness Evaluation & Justification:**
> - **High Effectiveness for Business Logic & Transactional Systems:** Decision tables are exceptionally effective in banking, taxation, insurance, e-commerce pricing engines, and safety-critical avionics where behavior is strictly governed by compound boolean policies.
> - **Combating Combinatorial Blind Spots:** Traditional test design techniques often miss combinatorial defects (e.g., when Condition A is true AND Condition B is false, a rare exception occurs). Decision tables eliminate these blind spots by enumerating all valid condition interactions.
> - **Limitations in Continuous / Algorithmic Domains:** Decision tables are less effective for computationally intensive numerical processing, continuous signal streams, or loop-heavy structural code where control flow is dictated by dynamic state iterations rather than discrete boolean rules.
> - **Rule Explosion Management:** For $k$ boolean conditions, the raw table contains $2^k$ rules. Testers effectively mitigate this complexity through **rule reduction and \"Don't Care\" ($-$) notation**, consolidating redundant rules without sacrificing fault detection.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> جداول القرار (Decision Tables) هي أقوى تقنية لاختبار القواعد المنطقية المعقدة وحالات التفاعل المشترك بين المتغيرات التي تفشل فيها تقنيات BVA المنفردة. تمثل كل قاعدة (عمود) حالة فحص مستقلة. عيبها الوحيد هو انفجار القواعد ($2^k$) ويتم حله عبر دمج القواعد برموز Don't Care (-).""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2.3, pp. 384–388; companion slides 47–60, 205."
    },
    {
        "id": "8.28",
        "title": "Significance of Independent Paths & Automated Tool Necessity for >100 LOC (Exercise 8.28)",
        "prompt": "Explain the significance of independent paths. Is it necessary to look for a tool for flow graph generation, if program size increases beyond 100 source lines?",
        "answer": """> **Analytical examination of Independent Paths and tool automation thresholds:**
>
> **1. Significance of Independent Paths in Software Testing:**
> - **Linear Independence & Basis Set:** **An independent path is any program execution path that introduces at least one edge (statement or condition) that has not been traversed by any other path.**
> - **Theoretical Foundation:** Based on graph theory and McCabe's cyclomatic complexity, **the cyclomatic complexity $V(G)$ defines the exact size of the basis set of linearly independent paths**.
> - **Guaranteed Baseline Coverage:** Executing a complete basis set of independent paths guarantees that:
>   - **100% of all executable statements** in the module are executed at least once (Statement Coverage).
>   - **100% of all decision outcomes** (True and False branches) are evaluated at least once (Branch Coverage).
> - **Efficiency & Redundancy Minimization:** Testing all possible paths in a program with loops is impossible. Testing a basis set of independent paths provides the maximum structural error discovery with a mathematically bounded, minimal number of test cases.
>
> **2. Necessity of Automated Tools for Programs Exceeding 100 LOC:**
> - **Yes, automated static analysis tools become an absolute necessity when program size exceeds 100 source lines.**
> - **Combinatorial Explosion of Visual Complexity:** Manual construction of Control Flow Graphs (CFG) for modules with $>100$ lines is highly error-prone. Nested conditional statements (`if-else`, `switch-case`) and loops (`while`, `for`, `do-while`) generate complex graph topologies where human testers frequently miscount edges, miss predicate nodes, or draw invalid edge crossings.
> - **Identification of Infeasible Paths:** In large programs, semantic dependencies between variables create **infeasible paths** (syntactically valid graph paths that can never be executed under any real input data due to contradictory predicates, e.g., $x > 5$ followed by $x < 2$). Automated symbolic execution and SMT solvers are required to prune infeasible paths from the basis set.
> - **Maintenance & Continuous Integration:** Software code changes frequently. Manually redrawing flow graphs and recalculating basis sets on every commit is unsustainable; automated CI/CD tools calculate $V(G)$ and extract basis paths instantaneously.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> المسار المستقل (Independent Path) هو مسار يقدم حافة (Edge) جديدة واحدة على الأقل لم يسبق المرور بها. عدد هذه المسارات يساوي بالضبط التعقيد السايكلوماتي $V(G)$. للبرامج التي تتجاوز 100 سطر، تصبح الأدوات الآلية ضرورة حتمية بسبب تعقيد الرسم اليدوي، وظهور المسارات غير القابلة للتنفيذ (Infeasible Paths) التي تتطلب أدوات تحليل رمزي لكشفها.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.3.1, pp. 403–410; companion slides 103–122, 208."
    },
    {
        "id": "8.29",
        "title": "Structural Testing vs. Functional Testing: Paradigms, Metrics & Boundaries (Exercise 8.29)",
        "prompt": "Discuss the structure testing. How is it different form functional testing?",
        "answer": """> **Comprehensive analysis of Structural Testing and its distinction from Functional Testing:**
>
> **1. Detailed Discussion of Structural Testing (White-Box Testing):**
> - **Underlying Paradigm:** Structural testing views the software from an internal engineering perspective, deriving test cases directly from the architectural structure and implementation logic of the source code.
> - **Core Techniques:**
>   - **Control Flow Testing:** Constructing Control Flow Graphs (CFGs) to achieve Statement Coverage, Decision/Branch Coverage, Condition Coverage, and McCabe's Basis Path Testing.
>   - **Data Flow Testing:** Tracking the lifecycle of variables from definition ($d$) through computational usage ($c$-use) or predicate usage ($p$-use) to ensure proper data transformations along $du$-paths.
>   - **Mutation Testing:** Injecting artificial syntactical faults (mutants) into the source code to assess the fault-revealing adequacy of the test suite.
>
> **2. Systematic Differences Between Structural and Functional Testing:**
> - **Source of Information:** **Structural testing relies entirely on the internal source code, control flow graphs, and data architectures.** **Functional testing relies strictly on external requirements specifications, design documents, and user use cases.**
> - **Access Level & Visibility:** Structural testing requires full source code access and compiler/debugger tooling (Glass-Box/Clear-Box). Functional testing treats the application as an opaque black box with zero visibility into internal code.
> - **Primary Objective:** Structural testing aims to verify internal implementation integrity, uncover logic bugs, exercise boundary conditions in loops, and eliminate dead code. Functional testing aims to verify that the software delivers the exact functional behavior expected by the user.
> - **Measurement Metrics:** Structural testing progress is quantified via code traversal percentages (Statement, Branch, Path, MC/DC coverage). Functional testing progress is quantified via specification requirements coverage, feature completeness, and passed test cases.
> - **Defect Blind Spots:**
>   - Structural testing cannot detect **omission errors** (features specified in requirements but completely forgotten by the programmer).
>   - Functional testing cannot detect **extraneous code**, hidden backdoors, or logic paths that are never exercised by standard operational input data.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> الفحص الهيكلي (Structural/White-box) ينظر للكود الداخلي وتدفق التحكم والبيانات ويقاس بنسب التغطية (Statements, Branches, Paths). الفحص الوظيفي (Functional/Black-box) ينظر للمواصفات والواجهات الخارجية فقط. الفحص الهيكلي عاجز عن كشف المتطلبات المنسية (Omission)، بينما الفحص الوظيفي عاجز عن كشف الكود الزائد أو الأبواب الخلفية.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2 vs. §8.3, pp. 374–375, 403–404; companion slides 16–18, 103–105, 208."
    },
    {
        "id": "8.33",
        "title": "Reasonableness of Software Module Complexity Thresholds (V(G) <= 10) (Exercise 8.33)",
        "prompt": "Is it reasonable to define “thresholds” for software modules? For example, is a module acceptable if its V(G) ≤ 10? Justify your answer.",
        "answer": """> **Critical evaluation of complexity thresholds and McCabe's $V(G) \le 10$ guideline:**
>
> **1. Is it Reasonable to Define Complexity Thresholds?**
> - **Yes, defining complexity thresholds is reasonable and highly beneficial as an engineering quality governance heuristic, but it must not be applied as a rigid, dogmatic law.**
>
> **2. Detailed Justification for $V(G) \le 10$ Acceptance Threshold:**
> - **Cognitive Comprehension Limits:** Thomas McCabe proposed $V(G) = 10$ based on psychological studies of human cognitive capacity (Miller's Law of Short-Term Memory: $7 \pm 2$ chunks of information). A module with cyclomatic complexity exceeding 10 strains human working memory, significantly increasing the probability of mental missteps during maintenance.
> - **Empirical Correlation with Defect Density:** Decades of empirical software engineering research demonstrate a strong positive correlation between high cyclomatic complexity and elevated defect rates. Modules with $V(G) > 10$ exhibit higher failure frequencies, longer debugging times, and greater regression risks.
> - **Testability & Basis Path Economics:** Since $V(G)$ represents the exact number of basis paths required for branch coverage, keeping $V(G) \le 10$ ensures that unit test suites remain compact, economically maintainable, and mathematically manageable.
>
> **3. Caveats and Exceptions (When the Threshold Must Be Relaxed):**
> - **Multi-Way Selection Structures (`switch` / `case`):** A module containing a clean, single multi-way selection statement (e.g., dispatching 25 distinct command tokens) will register $V(G) = 25$. However, because the control flow consists of independent, parallel, non-nested branches, the cognitive complexity and maintenance risk are minimal. Refactoring such a structure merely to satisfy $V(G) \le 10$ fragments the code and harms maintainability.
> - **System Context & Criticality:** In safety-critical systems (e.g., medical devices, flight controllers), a lower threshold ($V(G) \le 5$) may be mandated. In legacy or algorithmic code, thresholds should serve as **triggers for mandatory peer review and deep risk analysis** rather than automatic code rejection.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> تحديد عتبة $V(G) \le 10$ أمر منطقي ومبرر نفسياً وهندسياً لضمان قابلية الفهم والفحص وتقليل كثافة الأخطاء. لكن لا يجوز تطبيقه كقانون أعمى، لأن عبارات الاختيار المتعددة (`switch/case`) غير المتداخلة قد ترفع $V(G)$ إلى 20 أو 30 مع بقاء الكود بسيطاً وقليل المخاطر. لذلك يعتبر تجاوز العتبة جرس إنذار للمراجعة وليس حكماً قاطعاً بالرفض.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.3.1, pp. 409–410; companion slides 121–123, 209."
    },
    {
        "id": "8.36",
        "title": "Value Perturbation Analysis, Mutation Testing & Test Design Precautions (Exercise 8.36)",
        "prompt": "If we perturb a value, changing the current value of 100 by 1000, what is the effect of this change? What precautions are required while designing the test cases?",
        "answer": """> **Analysis of Value Perturbation (Mutation / Fault Injection) and Test Case Precautions:**
>
> **1. Effect of Perturbing a Value from 100 to 1000:**
> - **Perturbation Concept:** In software testing, intentionally altering a constant, variable, or operator is the foundational mechanism of **Mutation Testing (Fault-based Testing)**. The original program is modified to produce a mutant $P'$.
> - **Three Possible Behavioral Outcomes (The RIP Model):**
>   - **Reachability (Execution):** The mutated code statement must be reached and executed by the test case.
>   - **Infection (State Corruption):** Executing the perturbed value must corrupt the internal program state (e.g., intermediate calculation produces 1000 instead of 100).
>   - **Propagation (Failure Manifestation):** The corrupted internal state must propagate all the way to the program's observable output.
> - **Mutant Evaluation:**
>   - If the test suite detects the altered behavior and fails, the mutant is **killed** (demonstrating test suite adequacy).
>   - If the test suite passes despite the value being altered from 100 to 1000, the mutant **survives**. This indicates a critical deficiency in the test suite: inadequate assertion checks, unexercised dead code, or masked variables.
>
> **2. Precautions Required While Designing Test Cases:**
> - **Rigorous Output Assertions (Avoid Weak Oracles):** Test cases must not merely assert non-null or return codes. They must assert exact computed values. If an output depends on the perturbed variable, the assertion must catch the ten-fold magnitude difference.
> - **Masking Prevention:** Ensure that intermediate computations do not mask or absorb the perturbation (e.g., if a subsequent statement performs `x = min(x, 50)`, a perturbation of 100 to 1000 will be completely masked and unobservable).
> - **Boundary Sensitivity:** Test cases must be designed around decision predicates that evaluate the perturbed variable. If the variable is evaluated in `if (x > 500)`, the original value (100) and the perturbed value (1000) will take different control paths, successfully exposing the mutation.
> - **Equivalent Mutant Awareness:** Testers must verify that the perturbation does not accidentally create a syntactically different but semantically identical program (an equivalent mutant), which cannot be killed by any test case.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> تغيير قيمة من 100 إلى 1000 يمثل فحص الطفرات (Mutation Testing). إذا نجحت حزمة الفحص ولم تكتشف التغيير، فهذا يعني أن الطفرة عاشت (Mutant survived) وأن الفحص ضعيف وغير كافٍ. لقتل الطفرة يجب تطبيق نموذج RIP: الوصول للكود، وتلويث الحالة الداخلية، وضمان انتقال الخطأ (Propagation) للخرج عبر تأكيدات (Assertions) دقيقة تمنع إخفاء القيمة (Masking).""",
        "source": "Aggarwal & Singh (3rd ed.), §8.5, pp. 433–438; companion slides 167–172, 209."
    },
    {
        "id": "8.37",
        "title": "White-Box vs. Black-Box Derivation Difficulty & 100% Path Coverage Critique (Exercise 8.37)",
        "prompt": "What is the difference between white and black box testing? Is determining test cases easier in back or white box testing? Is it correct to claim that if white box testing is done properly, it will achieve close to 100% path coverage?",
        "answer": """> **Analysis of White-Box vs. Black-Box derivation complexity and critique of the 100% Path Coverage claim:**
>
> **1. Difference Between White-Box and Black-Box Testing:**
> - **White-Box (Structural) Testing:** Test cases are derived from the internal source code logic, control flow graph, conditions, and data structures. It requires source code visibility, programming expertise, and knowledge of internal architectures.
> - **Black-Box (Functional) Testing:** Test cases are derived strictly from external requirements specifications, use cases, and interface definitions without any access to or knowledge of the underlying source code.
>
> **2. Is Determining Test Cases Easier in Black-Box or White-Box Testing?**
> - **Determining test cases is generally significantly easier in Black-Box testing.**
> - **Reasons:**
>   - Black-box test design (such as BVA and Equivalence Partitioning) requires only an understanding of input/output domain boundaries and functional specifications. It does not require code compilation, complex graph construction, or mathematical basis path calculations.
>   - White-box test design requires in-depth code reading, tracing complex control flow graphs, solving predicate constraints to force execution down specific paths, identifying infeasible paths, and instrumenting code with coverage profilers.
>
> **3. Is It Correct to Claim That Proper White-Box Testing Achieves Close to 100% Path Coverage?**
> - **No, this claim is fundamentally FALSE and practically impossible.**
> - **Combinatorial / Infinite Path Explosion:** Any program containing loops or iterative constructs has an astronomically large, and potentially infinite, number of possible execution paths. For example, a simple loop executing between 1 and 20 times containing 4 nested `if-else` statements contains $4^{20} \approx 10^{12}$ distinct paths. Exhaustive path coverage cannot be achieved even with supercomputing resources.
> - **Basis Path Coverage vs. Exhaustive Path Coverage:** White-box testing aims for **100% Basis Path Coverage** (executing McCabe's $V(G)$ linearly independent paths), which guarantees that every statement and branch is executed. However, basis path coverage covers only a microscopic fraction of all possible execution path combinations.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> توليد حالات الفحص أسهل بكثير في Black-box لأنه يعتمد على المواصفات فقط دون الحاجة لقراءة الكود وتتبع المسارات. والادعاء بتحقيق 100% تغطية مسارات (Path coverage) هو ادعاء باطل ومستحيل عملياً بسبب وجود الحلقات التكرارية (Loops) التي تولد مسارات لا نهائية. الفحص الهيكلي يكتفي بتحقيق تغطية المسارات المستقلة $V(G)$ وليس كل المسارات التوافقية.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2, §8.3, §8.3.1, pp. 374–375, 403–408; companion slides 16–18, 103–120, 210."
    },
    {
        "id": "8.41",
        "title": "Integration Testing vs. System Testing: Objectives, Scope & Fault Types (Exercise 8.41)",
        "prompt": "Differentiate between integration testing and system testing.",
        "answer": """> **Systematic comparative differentiation between Integration Testing and System Testing:**
>
> **1. Scope and Target of Evaluation:**
> - **Integration Testing:** Focuses specifically on the **interfaces, interactions, data exchange, and communication protocols between integrated modules or subsystems**. It evaluates how individual software units collaborate.
> - **System Testing:** Evaluates the **complete, fully integrated software application as a unified entity** within its actual operating environment.
>
> **2. Testing Perspective and Artifact Grounding:**
> - **Integration Testing:** Grounded primarily in the **High-Level Design (HLD), software architecture, and interface specifications**. It employs both structural (white-box interface coverage) and functional (black-box service contract) approaches.
> - **System Testing:** Grounded strictly in the **System Requirements Specification (SRS)** and business use cases. It is almost exclusively functional (black-box) testing conducted from the perspective of the end user or client.
>
> **3. Characteristic Fault Types Detected:**
> - **Integration Testing Detects:**
>   - Incompatible parameter types, incorrect argument ordering, or mismatched data structures across module boundaries.
>   - Buffer overflows or data truncation across API interfaces.
>   - Protocol mismatches, incorrect handshake sequences, and race conditions in shared global memory.
>   - Misinterpreted function return codes and unhandled exception propagation.
> - **System Testing Detects:**
>   - Complete omission or incorrect implementation of high-level functional requirements.
>   - Performance bottlenecks under heavy transactional loads, memory leaks, and throughput degradation.
>   - Security vulnerabilities, authorization loopholes, and data leakage.
>   - System recovery failures after hardware crashes, network disconnects, or power interruptions.
>   - Platform incompatibility across operating systems, browsers, and hardware devices.
>
> **4. Execution Strategies:**
> - **Integration Testing:** Executed incrementally using architectural strategies: **Top-Down** (requiring stubs), **Bottom-Up** (requiring drivers), **Sandwich/Hybrid**, or Non-incremental (Big Bang).
> - **System Testing:** Executed comprehensively across specialized testing categories: Functional testing, Stress testing, Load testing, Security testing, Recovery testing, and Usability testing.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> فحص التكامل (Integration) يفحص الواجهات ونقل البيانات والتواصل بين المودولات ويعتمد على وثيقة التصميم (HLD) ويستخدم Stubs و Drivers. أما فحص النظام (System) فيفحص المنظومة كاملة ككيان واحد في بيئتها التشغيلية للتأكد من مطابقتها لوثيقة المتطلبات (SRS)، ويشمل الفحوصات غير الوظيفية كالأداء والأمان والتعافي.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.6.1 & §8.6.2, pp. 439–445; companion slides 173–182, 210."
    }
]

retrieval_set = """<!-- Print-hidden study guidance retained for screen use.
## Retrieval Set & Active Recall Self-Test

1. What are the three core testing dichotomies covered in Exercise 8.5, and what are their respective operational environments?
2. Formulate Dijkstra's theorem on testing and explain why exhaustive testing cannot prove 100% program correctness.
3. Why does worst-case testing reject the Single Fault Assumption, and what formula defines its test-case count?
4. Contrast the input selection target and empirical justification of Equivalence Partitioning versus Boundary Value Analysis.
5. In what specific operational domains do Decision Tables outperform single-variable BVA?
6. Define an independent path, state how its count relates to McCabe's $V(G)$, and justify tool necessity beyond 100 LOC.
7. What are omission errors, and why can structural testing never discover them?
8. Why is McCabe's $V(G) \\le 10$ rule of thumb reasonable, and in what specific code structure should it be relaxed?
9. Explain the RIP model in mutation testing and what surviving mutants signify.
10. Mathematically refute the claim that proper white-box testing achieves close to 100% path coverage.
11. Contrast the primary fault types uncovered by Integration Testing versus System Testing.
-->
"""

def generate():
    content = header.strip() + "\n\n---\n\n"
    for item in items:
        block = f"""<div class="no-break">

### Question {item['id']} · {item['title']}

{item['prompt']}
{{: .keep-next }}
{item['answer']}

{item['note']}

**Source:**
{item['source']}

</div>

---
"""
        content += block + "\n"
    
    content += retrieval_set.strip() + "\n"
    
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Generated {OUT_PATH} successfully. Total items: {len(items)}")

if __name__ == "__main__":
    generate()
