# -*- coding: utf-8 -*-
"""
Build script for ASE Chapter 8: T5 Applied Test Design & Case Studies Pack
Aggarwal & Singh (3rd ed.), Exercises 8.12, 8.13, 8.16, 8.17, 8.21, 8.24, 8.25, 8.26, 8.44, 8.48, 8.49
"""
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

OUT_PATH = r"01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch08_Software_Testing\T5_Apply_Design.md"

header = """---
title: "ASE Chapter 8 — T5 Applied Test Design & Case Studies Pack"
course: "Advanced Software Engineering (CS603)"
instructor: "Asst. Prof. Dr. Ali Fahim Ni'ma"
author: "Master Studio Engine"
date: "2026-10-22"
lang: "en"
---

# ASE Chapter 8 — T5 Applied Test Design & Case Studies Pack

<!-- Print-hidden metadata: 11 applied engineering and test-design exercises from Aggarwal & Singh (3rd ed., pp. 455–458). -->
"""

items = [
    {
        "id": "8.12",
        "title": "Boundary Value Analysis Technique & Two-Variable Worked Example (Exercise 8.12)",
        "prompt": "Explain the boundary value analysis testing techniques with the help of an example.",
        "answer": """> **Foundations of Boundary Value Analysis (BVA) and Concrete Worked Application:**
>
> **1. Theoretical Principles of BVA:**
> - **Empirical Justification:** Decades of software engineering research establish that **programming defects cluster with disproportionate density at the extreme boundaries of input variables** rather than in their nominal interior ranges (off-by-one loops, relational operators `<` vs. `<=`, array bounds).
> - **The Single Fault Assumption:** Standard BVA operates on the reliability theory principle that software failures are almost exclusively caused by a single variable reaching its extreme value while all other variables remain at nominal values.
> - **Boundary Values Evaluated:** For each input variable with valid domain $[min, max]$, five critical test points are evaluated:
>   - **$min$:** Exactly at the minimum boundary.
>   - **$min^+$:** Just above the minimum ($min + 1$ or $min + \\epsilon$).
>   - **$nom$:** A typical nominal interior value.
>   - **$max^-$:** Just below the maximum ($max - 1$ or $max - \\epsilon$).
>   - **$max$:** Exactly at the maximum boundary.
> - **Total Test Case Count:** For a program with $n$ independent input variables, standard BVA requires exactly **$4n + 1$ test cases**.
>
> **2. Concrete Worked Example (Two-Variable Arithmetic Function):**
> Consider a function $f(x_1, x_2)$ calculating rectangle area, where $1 \\le x_1 \\le 100$ and $1 \\le x_2 \\le 50$.
> - For $x_1$: $min=1, min^+=2, nom=50, max^-=99, max=100$.
> - For $x_2$: $min=1, min^+=2, nom=25, max^-=49, max=50$.
>
> **Generated Test Suite ($4(2) + 1 = 9$ Test Cases):**
> - **Test Case 1 (Nominal baseline):** $x_1 = 50, x_2 = 25$ $\\implies$ Expected: 1250
> - **Test Case 2 ($x_1 = min$):** $x_1 = 1, x_2 = 25$ $\\implies$ Expected: 25
> - **Test Case 3 ($x_1 = min^+$):** $x_1 = 2, x_2 = 25$ $\\implies$ Expected: 50
> - **Test Case 4 ($x_1 = max^-$):** $x_1 = 99, x_2 = 25$ $\\implies$ Expected: 2475
> - **Test Case 5 ($x_1 = max$):** $x_1 = 100, x_2 = 25$ $\\implies$ Expected: 2500
> - **Test Case 6 ($x_2 = min$):** $x_1 = 50, x_2 = 1$ $\\implies$ Expected: 50
> - **Test Case 7 ($x_2 = min^+$):** $x_1 = 50, x_2 = 2$ $\\implies$ Expected: 100
> - **Test Case 8 ($x_2 = max^-$):** $x_1 = 50, x_2 = 49$ $\\implies$ Expected: 2450
> - **Test Case 9 ($x_2 = max$):** $x_1 = 50, x_2 = 50$ $\\implies$ Expected: 2500""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> يعتمد فحص القيم الحدية (BVA) على فرضية العيب المنفرد (Single Fault Assumption) التي تنص على أن الأخطاء تنتج عن وصول متغير واحد إلى حده الأقصى أو الأدنى بينما تبقى باقي المتغيرات في قيمها الطبيعية (Nominal). عدد حالات الفحص لـ $n$ متغير هو دائماً $4n+1$.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2.1, pp. 375–377; companion slides 20–25, 202."
    },
    {
        "id": "8.13",
        "title": "NextDate Calendar Problem: BVA, Robust & Worst-Case Suites (Exercise 8.13)",
        "prompt": "Consider the program for the determination of next date in a calendar. Its input is a triple of day, month and year with the following range:\n1 ≤ month ≤ 12\n1 ≤ day ≤ 31\n1900 ≤ year ≤ 2025\nThe possible outputs would be Next date or invalid date. Design boundary value, robust and worst test cases for this programs.",
        "answer": """> **Comprehensive Test Suite Design for the NextDate Calendar Function:**
>
> **1. Variable Input Domains ($n = 3$ variables):**
> - **$month$ ($M$):** $1 \\le M \\le 12$ $\\implies$ $\\{min=1, min^+=2, nom=6, max^-=11, max=12\\}$
> - **$day$ ($D$):** $1 \\le D \\le 31$ $\\implies$ $\\{min=1, min^+=2, nom=15, max^-=30, max=31\\}$
> - **$year$ ($Y$):** $1900 \\le Y \\le 2025$ $\\implies$ $\\{min=1900, min^+=1901, nom=1962, max^-=2024, max=2025\\}$
>
> **2. Boundary Value Analysis Test Cases ($4n + 1 = 13$ cases):**
> Holding two variables at nominal ($D=15, M=6, Y=1962$) while varying the third across 5 boundary points:
> - **Case 1 (Nominal):** $(15, 6, 1962) \\implies$ Expected: $16/6/1962$
> - **Cases 2–5 (Varying $D$):**
>   - $(1, 6, 1962) \\to 2/6/1962$ (Beginning of month)
>   - $(2, 6, 1962) \\to 3/6/1962$
>   - $(30, 6, 1962) \\to 1/7/1962$ (Valid end of 30-day month; advances to July 1)
>   - $(31, 6, 1962) \\to \\text{Invalid Date}$ (June has only 30 days)
> - **Cases 6–9 (Varying $M$):** $(15, 1, 1962) \\to 16/1/1962$; $(15, 2, 1962) \\to 16/2/1962$; $(15, 11, 1962) \\to 16/11/1962$; $(15, 12, 1962) \\to 16/12/1962$
> - **Cases 10–13 (Varying $Y$):** $(15, 6, 1900) \\to 16/6/1900$; $(15, 6, 1901) \\to 16/6/1901$; $(15, 6, 2024) \\to 16/6/2024$; $(15, 6, 2025) \\to 16/6/2025$
>
> **3. Robustness Testing Cases ($6n + 1 = 19$ cases):**
> Adds $min^- = min - 1$ and $max^+ = max + 1$ out-of-boundary values to verify robust error-handling:
> - **Includes all 13 BVA cases above, plus 6 boundary exception cases:**
> - **Case 14 ($D = min^-$):** $(0, 6, 1962) \\implies$ Expected: **Invalid Date**
> - **Case 15 ($D = max^+$):** $(32, 6, 1962) \\implies$ Expected: **Invalid Date**
> - **Case 16 ($M = min^-$):** $(15, 0, 1962) \\implies$ Expected: **Invalid Date**
> - **Case 17 ($M = max^+$):** $(15, 13, 1962) \\implies$ Expected: **Invalid Date**
> - **Case 18 ($Y = min^-$):** $(15, 6, 1899) \\implies$ Expected: **Invalid Date**
> - **Case 19 ($Y = max^+$):** $(15, 6, 2026) \\implies$ Expected: **Invalid Date**
>
> **4. Worst-Case Testing Design ($5^n = 5^3 = 125$ cases):**
> Rejects the Single Fault Assumption and evaluates the full Cartesian product of the 5 boundary points across all 3 variables simultaneously:
> - **Cartesian Factor Sets:**
>   - $D \\in \\{1, 2, 15, 30, 31\\}$
>   - $M \\in \\{1, 2, 6, 11, 12\\}$
>   - $Y \\in \\{1900, 1901, 1962, 2024, 2025\\}$
> - Total test cases = $5 \\times 5 \\times 5 = 125$ distinct vectors.
> - **Representative Vectors Drawn Strictly from the 125 Cartesian Combinations:**
>   - $(1, 1, 1900) \\implies 2/1/1900$ (Triple minimum: $min, min, min$)
>   - $(15, 6, 1962) \\implies 16/6/1962$ (Triple nominal: $nom, nom, nom$)
>   - $(30, 6, 1962) \\implies 1/7/1962$ (Valid 30-day month roll-over)
>   - $(31, 6, 1962) \\implies \\text{Invalid Date}$ (30-day month evaluated with $D=31$)
>   - $(31, 12, 2024) \\implies 1/1/2025$ (Year roll-over at $max^-$ year)
>   - $(31, 12, 2025) \\implies 1/1/2026$ (Triple maximum: $max, max, max$. The input $(31, 12, 2025)$ is within the valid input domain $1900 \\le Y \\le 2025$; the resulting next date is $1/1/2026$)
> - **Domain-Specific Testing Supplement (February & Leap Years):**
>   Because pure 5-point BVA uses only $\\{1, 2, 15, 30, 31\\}$, days 28 and 29 are NOT members of the 125 Cartesian set. Verifying February leap-year logic (e.g., $28/2/1900 \\to 1/3/1900$ vs. $29/2/2024 \\to 1/3/2024$) requires **Special Value Testing (§8.3.5)** or Equivalence Class Partitioning rather than standard 5-point BVA.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> انتبه لثلاث نقاط أساسية في مسألة NextDate:
> 1. إدخال $(30, 6, 1962)$ هو تاريخ صالح تماماً لأن شهر حزيران يحتوي 30 يوماً، والناتج هو الانتقال إلى $1/7/1962$. أما $(31, 6, 1962)$ فهو غير صالح.
> 2. شبكة أسوأ الحالات ($5^3 = 125$) تتكون حصراً من الجداء الديكارتي لقيم الأيام الخمسة $\\{1, 2, 15, 30, 31\\}$. لذلك فإن تواريخ 28 و 29 شباط لا تنتمي إلى مجموعة الـ 125 بل يتم فحصها عبر تقنية القيم الخاصة (Special Value Testing).
> 3. الإدخال $(31, 12, 2025)$ إدخال صالح تماماً وضمن حدود النطاق المعطى ($1900 \\le Y \\le 2025$)، والناتج هو اليوم التالي $1/1/2026$.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2.1, pp. 377–380; companion slides 27–34, 203."
    },
    {
        "id": "8.16",
        "title": "Largest of Three Numbers: BVA, Statement Coverage & Decision Table (Exercise 8.16)",
        "prompt": "Consider a program given below for the selection of the largest of numbers:\n(i) Design the set of test cases using boundary value analysis technique and equivalence class testing technique.\n(ii) Select a set of test cases that will provide 100% statement coverage.\n(iii) Develop a decision table for this program.",
        "answer": """> **Multi-Method Applied Test Suite Design for the Largest of Three Numbers Program:**
>
> **(i) Boundary Value Analysis & Equivalence Class Test Cases:**
> - **Domain & Equivalence Classes:** Assuming floating-point input domain $[-100.0, 100.0]$:
>   - Valid Class 1 ($A$ is strictly largest): $A > B$ and $A > C$ (e.g., $A=50, B=20, C=10$).
>   - Valid Class 2 ($B$ is strictly largest): $B \\ge A$ and $B \\ge C$ (e.g., $A=20, B=50, C=10$).
>   - Valid Class 3 ($C$ is strictly largest): $C \\ge A$ and $C > B$ (e.g., $A=10, B=20, C=50$).
>   - Boundary Equality Classes: $A = B > C$, $B = C > A$, $A = C > B$, and $A = B = C$.
> - **BVA Extreme Boundary Vectors:** Test vectors testing extreme limits: $(-100, 0, 0)$, $(100, 0, 0)$, $(0, -100, 0)$, $(0, 100, 0)$, $(0, 0, -100)$, $(0, 0, 100)$.
>
> **(ii) Test Suite for 100% Statement Coverage:**
> To execute every executable C statement (Nodes 1, 2, 3, 4, 5, 6, 7, 8, 9), exactly 4 test cases corresponding to McCabe's basis paths are required:
> - **Test 1 ($A > B$ True, $A > C$ True):** $A = 10.0, B = 5.0, C = 2.0$ $\\implies$ Executes Nodes 1, 2, 3, 4, 9 $\\implies$ Outputs $A = 10.0$
> - **Test 2 ($A > B$ True, $A > C$ False):** $A = 10.0, B = 5.0, C = 15.0$ $\\implies$ Executes Nodes 1, 2, 3, 5, 9 $\\implies$ Outputs $C = 15.0$
> - **Test 3 ($A > B$ False, $C > B$ True):** $A = 5.0, B = 10.0, C = 15.0$ $\\implies$ Executes Nodes 1, 2, 6, 7, 9 $\\implies$ Outputs $C = 15.0$
> - **Test 4 ($A > B$ False, $C > B$ False):** $A = 5.0, B = 10.0, C = 8.0$ $\\implies$ Executes Nodes 1, 2, 6, 8, 9 $\\implies$ Outputs $B = 10.0$
>
> **(iii) Decision Table Derivation:**
> - **Conditions:**
>   - $C_1$: $A > B$
>   - $C_2$: $A > C$
>   - $C_3$: $C > B$
> - **Actions:**
>   - $A_1$: Print $A$
>   - $A_2$: Print $B$
>   - $A_3$: Print $C$
> - **Decision Rules:**
>   - **Rule 1:** $C_1 = T, C_2 = T, C_3 = -$ $\\implies$ Action: Print $A$ (Test: $10, 5, 2$)
>   - **Rule 2:** $C_1 = T, C_2 = F, C_3 = -$ $\\implies$ Action: Print $C$ (Test: $10, 5, 15$)
>   - **Rule 3:** $C_1 = F, C_2 = -, C_3 = T$ $\\implies$ Action: Print $C$ (Test: $5, 10, 15$)
>   - **Rule 4:** $C_1 = F, C_2 = -, C_3 = F$ $\\implies$ Action: Print $B$ (Test: $5, 10, 8$)""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> لتغطية جميع جمل البرنامج 100% نحتاج بالضبط إلى 4 حالات فحص تطابق المسارات المستقلة الأربعة المشتقة في التمرين 8.27. جدول القرار يوضح استخدام Don't Care (-) لتقليص القواعد من 8 إلى 4 قواعد تنفيذية حاسمة.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2.1, §8.2.3, §8.3.1, pp. 375–388, 403–410; companion slides 204–205."
    },
    {
        "id": "8.17",
        "title": "Mathematical Proof of the Impossibility of Exhaustive Testing (Exercise 8.17)",
        "prompt": "Consider a small program and show, why is it practically impossible to do exhaustive testing?",
        "answer": """> **Mathematical Demonstration of the Impracticality of Exhaustive Testing:**
>
> **1. Concrete Program Structure:**
> Consider a compact loop-based validation routine consisting of only 15 lines of source code:
> ```c
> int process_data(int record[20]) {
>     for (int i = 0; i < 20; i++) {
>         if (record[i] < 0)        handle_negative(record[i]);
>         else if (record[i] == 0)  handle_zero(record[i]);
>         else                      handle_positive(record[i]);
>     }
> }
> ```
>
> **2. Execution Path Combinatorial Explosion:**
> - In each iteration of the loop, the control flow evaluates a 3-way selection branch ($<0$, $==0$, $>0$).
> - The loop executes exactly 20 times.
> - The total number of distinct, possible execution paths through this simple loop is:
>   $$\\text{Total Paths} = 3^{20} = 3,486,784,401 \\approx 3.49 \\times 10^9 \\text{ paths}$$
> - **Execution Time Calculation:** If an ultra-fast hardware simulator executes and verifies 1,000 paths per second, testing this 15-line program would require:
>   $$\\frac{3.49 \\times 10^9 \\text{ seconds}}{1,000 \\times 3,600 \\times 24} \\approx 40.4 \\text{ days of non-stop testing!}$$
>
> **3. Input Domain Combinatorial Explosion:**
> - If an integer input variable is a standard 32-bit signed integer, its domain contains $2^{32} \\approx 4.29 \\times 10^9$ values.
> - A function taking just two 32-bit integers has $2^{32} \\times 2^{32} = 2^{64} \\approx 1.84 \\times 10^{19}$ possible input pairs.
> - Testing at a speed of 1 billion ($10^9$) test cases per second:
>   $$\\frac{1.84 \\times 10^{19}}{10^9 \\times 3600 \\times 24 \\times 365.25} \\approx 584.5 \\text{ years!}$$
>
> **4. Engineering Conclusion:**
> Complete exhaustive testing is mathematically impossible for real-world software. Software testing must therefore rely on **partitioning, sampling heuristics, and coverage criteria (BVA, equivalence partitioning, basis path testing)** to maximize fault discovery within feasible economic limits.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> هذا المثال الرياضي نموذجي في الامتحانات: حلقة تكرارية بسيطة تدور 20 مرة وبداخلها اختيار ثلاثي تولد $3^{20} \\approx 3.49$ مليار مسار تحتاج أكثر من 40 يوماً لفحصها! وإذا كان البرنامج يستقبل متغيرين بحجم 32-bit فإن فضاء المدخلات يتطلب 584 سنة بسرعة مليار فحص في الثانية.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.1.3, pp. 367–368; companion slides 10–12, 205."
    },
    {
        "id": "8.21",
        "title": "Extended Triangle Problem Including Right-Angled Triangles (Exercise 8.21)",
        "prompt": "Determine the boundary value test cases the extended triangle problem that also considers right angle triangles.",
        "answer": """> **Boundary Value Test Case Design for the Extended Triangle Problem:**
>
> **1. Problem Formulation & Geometric Constraints:**
> - **Input:** Three integer side lengths $a, b, c$ with operational domain $[1, 100]$.
> - **Triangle Validity Invariant (Triangle Inequality Theorem):**
>   - $a + b > c$ AND $a + c > b$ AND $b + c > a$.
> - **Right-Angled Triangle Criterion (Pythagorean Theorem):**
>   - A valid triangle is right-angled if and only if:
>     $$a^2 + b^2 = c^2 \\quad \\lor \\quad a^2 + c^2 = b^2 \\quad \\lor \\quad b^2 + c^2 = a^2$$
> - **Classification Categories:** Not a Triangle, Scalene, Isosceles, Equilateral, Right-Angled Scalene, and Right-Angled Isosceles ($a=b, c = a\\sqrt{2}$, impossible with pure integers).
>
> **2. Standard BVA Test Cases on Domain Boundaries ($[1, 100]$, $4n+1 = 13$ cases):**
> Holding two sides at nominal $nom=50$ while varying the third across $\\{1, 2, 50, 99, 100\\}$:
> - $(1, 50, 50)$ $\\implies$ Isosceles ($1 + 50 > 50$)
> - $(2, 50, 50)$ $\\implies$ Isosceles
> - $(50, 50, 50)$ $\\implies$ Equilateral
> - $(99, 50, 50)$ $\\implies$ Isosceles ($50 + 50 = 100 > 99$)
> - $(100, 50, 50)$ $\\implies$ **Boundary Boundary Case: NOT A TRIANGLE** ($50 + 50 = 100$, violates $a+b > c$!)
>
> **3. Dedicated Boundary Test Cases for Right-Angled Triangles (Pythagorean Triples):**
> - **Minimal Pythagorean Triple:** $(3, 4, 5)$ $\\implies$ $3^2 + 4^2 = 9 + 16 = 25 = 5^2$ $\\implies$ **Right-Angled Scalene Triangle**
> - **Permutations of Right-Angled Boundaries:**
>   - $(5, 3, 4)$ $\\implies$ Right-Angled
>   - $(4, 5, 3)$ $\\implies$ Right-Angled
> - **Non-Right-Angled Boundary Perturbations (Off-by-one near-misses):**
>   - $(3, 4, 6)$ $\\implies$ $9 + 16 = 25 \\ne 36$ $\\implies$ Obtuse Scalene (Non-Right-Angled)
>   - $(3, 4, 4)$ $\\implies$ Acute Isosceles (Non-Right-Angled)
> - **Larger Primitive Pythagorean Boundary Triples within $[1, 100]$:**
>   - $(5, 12, 13)$ $\\implies$ $25 + 144 = 169 = 13^2$ $\\implies$ Right-Angled
>   - $(6, 8, 10)$ $\\implies$ $36 + 64 = 100 = 10^2$ $\\implies$ Right-Angled
>   - $(20, 21, 29)$ $\\implies$ $400 + 441 = 841 = 29^2$ $\\implies$ Right-Angled
> - **Upper Boundary Pythagorean Triple:** $(28, 96, 100)$ $\\implies$ $784 + 9216 = 10000 = 100^2$ $\\implies$ **Upper Boundary Right-Angled Triangle**""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> في مسألة المثلث الموسع: انتبه للحد الحرج $50+50=100$ حيث يعطي الناتج "ليس مثلثاً" لأن مجموع الضلعين لا يزيد عن الثالث. ولاختبار المثلث القائم الزاوية، يجب تضمين الثلاثيات الفيثاغورسية الشهيرة $(3,4,5)$ و $(5,12,13)$ والحد الأقصى $(28,96,100)$، بالإضافة لاختبار الحالات القريبة (Near-miss) مثل $(3,4,6)$ للتأكد من عدم تصنيفها خطأً كمثلث قائم.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2.1, pp. 375–380; companion slides 20–25, 205."
    },
    {
        "id": "8.24",
        "title": "Academic Student Grading Rules Equivalence Partitioning (Exercise 8.24)",
        "prompt": "Let us consider an example of grading the students in an academic institution. The grading is done according to the following rules:\n80–100: Distinction\n60–79: First division\n50–59: Second division\n40–49: Third division\n0–39: Fail\nGenerate test cases using equivalence class testing technique.",
        "answer": """> **Equivalence Class Test Suite Derivation for Student Grading System:**
>
> **1. Identification of Valid Equivalence Classes (Input Domain $[0, 100]$):**
> - **$EC_1$ (Distinction):** $80 \\le \\text{Marks} \\le 100$ $\\implies$ Expected Output: **Distinction**
> - **$EC_2$ (First Division):** $60 \\le \\text{Marks} \\le 79$ $\\implies$ Expected Output: **First division**
> - **$EC_3$ (Second Division):** $50 \\le \\text{Marks} \\le 59$ $\\implies$ Expected Output: **Second division**
> - **$EC_4$ (Third Division):** $40 \\le \\text{Marks} \\le 49$ $\\implies$ Expected Output: **Third division**
> - **$EC_5$ (Fail):** $0 \\le \\text{Marks} \\le 39$ $\\implies$ Expected Output: **Fail**
>
> **2. Identification of Invalid Equivalence Classes (Error Handling):**
> - **$EC_6$ (Negative Marks):** $\\text{Marks} < 0$ $\\implies$ Expected Output: **Error: Invalid Marks (Negative)**
> - **$EC_7$ (Excess Marks):** $\\text{Marks} > 100$ $\\implies$ Expected Output: **Error: Invalid Marks (Exceeds Maximum)**
> - **$EC_8$ (Non-Numeric Data):** Character / String input $\\implies$ Expected Output: **Error: Type Mismatch**
>
> **3. Robust Equivalence Class Test Suite:**
> - **Test 1 ($EC_1$ Representative):** $\\text{Marks} = 88$ $\\implies$ Expected Output: **Distinction**
> - **Test 2 ($EC_2$ Representative):** $\\text{Marks} = 72$ $\\implies$ Expected Output: **First division**
> - **Test 3 ($EC_3$ Representative):** $\\text{Marks} = 54$ $\\implies$ Expected Output: **Second division**
> - **Test 4 ($EC_4$ Representative):** $\\text{Marks} = 45$ $\\implies$ Expected Output: **Third division**
> - **Test 5 ($EC_5$ Representative):** $\\text{Marks} = 22$ $\\implies$ Expected Output: **Fail**
> - **Test 6 ($EC_6$ Robust Invalid):** $\\text{Marks} = -10$ $\\implies$ Expected Output: **Error: Invalid Marks**
> - **Test 7 ($EC_7$ Robust Invalid):** $\\text{Marks} = 105$ $\\implies$ Expected Output: **Error: Invalid Marks**
> - **Test 8 ($EC_8$ Robust Invalid):** $\\text{Marks} = \\text{\"AB\"}$ $\\implies$ Expected Output: **Error: Type Mismatch**
>
> **4. Recommended Boundary Integration Test Points:**
> Combining with BVA along partition boundaries: $0, 39, 40, 49, 50, 59, 60, 79, 80, 100$.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> فئات التكافؤ تشمل 5 فئات صالحة تعطي التقديرات الرسمية، بالإضافة إلى 3 فئات غير صالحة ضرورية جداً لاختبار متانة النظام (الدرجات السالبة، والدرجات الأعلى من 100، والمدخلات غير الرقمية). الفحص القوي (Robust Equivalence) يلزم باختبار الفئات غير الصالحة.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2.2, pp. 380–384; companion slides 35–46, 206."
    },
    {
        "id": "8.25",
        "title": "Odd/Even Integer Program: Boundary Value & Equivalence Testing (Exercise 8.25)",
        "prompt": "Consider a program to determine whether a number is ‘odd’ or ‘even’ and print the message NUMBER IS EVEN or NUMBER IS ODD. The number may be any valid integer. Design boundary value and equivalence class test cases.",
        "answer": """> **BVA and Equivalence Class Test Design for Odd/Even Classification:**
>
> **1. Input Domain Specification:**
> - The input is a signed standard integer $N$.
> - For a standard 16-bit integer architecture: domain is $[-32768, 32767]$.
> - For a standard 32-bit integer architecture: domain is $[-2,147,483,648, 2,147,483,647]$.
>
> **2. Equivalence Class Partitioning:**
> - **Valid Equivalence Classes:**
>   - **$EC_1$ (Positive Even Integer):** $N > 0$ and $N \\pmod 2 == 0$ (e.g., $N = 42$) $\\implies$ **NUMBER IS EVEN**
>   - **$EC_2$ (Positive Odd Integer):** $N > 0$ and $N \\pmod 2 \\ne 0$ (e.g., $N = 37$) $\\implies$ **NUMBER IS ODD**
>   - **$EC_3$ (Zero - Critical Boundary Even):** $N = 0$ ($0 \\pmod 2 == 0$) $\\implies$ **NUMBER IS EVEN**
>   - **$EC_4$ (Negative Even Integer):** $N < 0$ and $N \\pmod 2 == 0$ (e.g., $N = -28$) $\\implies$ **NUMBER IS EVEN**
>   - **$EC_5$ (Negative Odd Integer):** $N < 0$ and $N \\pmod 2 \\ne 0$ (e.g., $N = -19$) $\\implies$ **NUMBER IS ODD**
> - **Invalid Equivalence Classes:**
>   - **$EC_6$ (Floating-Point Real Number):** Non-integer decimal (e.g., $N = 12.5$) $\\implies$ **Error: Integer Required**
>   - **$EC_7$ (Non-Numeric String):** Alphabetic text (e.g., $N = \\text{\"hello\"}$) $\\implies$ **Error: Type Mismatch**
>   - **$EC_8$ (Integer Overflow):** Magnitude exceeding architectural limits (e.g., $N = 10^{15}$) $\\implies$ **Error: Overflow**
>
> **3. Boundary Value Analysis (BVA) Test Cases (16-bit reference):**
> - **Test 1 ($min$):** $N = -32768$ $\\implies$ Expected: **NUMBER IS EVEN**
> - **Test 2 ($min^+$):** $N = -32767$ $\\implies$ Expected: **NUMBER IS ODD**
> - **Test 3 (Negative transition to zero):** $N = -1$ $\\implies$ Expected: **NUMBER IS ODD**
> - **Test 4 (Zero boundary):** $N = 0$ $\\implies$ Expected: **NUMBER IS EVEN**
> - **Test 5 (Positive transition from zero):** $N = +1$ $\\implies$ Expected: **NUMBER IS ODD**
> - **Test 6 ($max^-$):** $N = 32766$ $\\implies$ Expected: **NUMBER IS EVEN**
> - **Test 7 ($max$):** $N = 32767$ $\\implies$ Expected: **NUMBER IS ODD**
> - **Test 8 (Robust Underflow $min^-$):** $N = -32769$ $\\implies$ Expected: **Error: Underflow**
> - **Test 9 (Robust Overflow $max^+$):** $N = 32768$ $\\implies$ Expected: **Error: Overflow**""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> في برمجة C/C++، عملية باقي القسمة `%` للأرقام السالبة قد تعطي نتيجة سالبة (مثلاً `-5 % 2 == -1` وليس `1`). لذلك فإن تقسيم فئات التكافؤ إلى زوجي موجب، وفردي موجب، وزوجي سالب، وفردي سالب، مع اعتبار الصفر حالة حدية مستقلة، هو المفتاح الهندسي لكشف أخطاء معالجة الأرقام السالبة.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2.1 & §8.2.2, pp. 375–384; companion slides 20–46, 207."
    },
    {
        "id": "8.26",
        "title": "Professional Course Admission Rules: Decision Table Test Suite (Exercise 8.26)",
        "prompt": "Admission to a professional course is subject to the following conditions:\n(a) Marks in Mathematics >= 60\n(b) Marks in Physics >= 50\n(c) Marks in Chemistry >= 40\n(d) Total in all three subjects >= 200 OR Total in Mathematics and Physics >= 150\nIf aggregate marks of an eligible candidate are more than 225, he/she will be eligible for honors course, otherwise he/she will be eligible for pass course.\nThe program reads the marks in the three subjects and generates the following outputs:\n(a) Not Eligible\n(b) Eligible to Pass Course\n(c) Eligible to Honors Course\nDesign test cases using decision table testing technique.",
        "answer": """> **Decision Table Test Design for Professional Course Admission:**
>
> **1. Formal Condition Stub Formulation:**
> - **$C_1$ (Subject Cutoffs):** $M \\ge 60$ AND $P \\ge 50$ AND $C \\ge 40$
> - **$C_2$ (Total Threshold):** $M + P + C \\ge 200$
> - **$C_3$ (Math+Physics Threshold):** $M + P \\ge 150$
> - **$C_4$ (Honors Aggregate Cutoff):** $M + P + C > 225$
> - **Eligibility Rule:** Candidate is eligible if $C_1$ is True AND ($C_2$ is True OR $C_3$ is True).
>
> **2. Action Stub:**
> - **$A_1$:** Output: **Not Eligible**
> - **$A_2$:** Output: **Eligible to Pass Course**
> - **$A_3$:** Output: **Eligible to Honors Course**
>
> **3. Consolidated Decision Table Rules and Test Cases:**
>
> - **Rule 1 (Subject Failure):**
>   - Conditions: $C_1 = F, C_2 = -, C_3 = -, C_4 = -$
>   - Action: **$A_1$ (Not Eligible)**
>   - **Test Case 1:** $M = 55, P = 80, C = 90$ ($M < 60$; Total = 225). Result: **Not Eligible**.
>
> - **Rule 2 (Cutoffs Met, but Both Total Thresholds Fail):**
>   - Conditions: $C_1 = T, C_2 = F, C_3 = F, C_4 = -$
>   - Action: **$A_1$ (Not Eligible)**
>   - **Test Case 2:** $M = 65, P = 55, C = 45$ (Total = 165 < 200; $M+P = 120 < 150$). Result: **Not Eligible**.
>
> - **Rule 3 (Eligible via Total Threshold, Aggregate $\\le 225$):**
>   - Conditions: $C_1 = T, C_2 = T, C_3 = F, C_4 = F$
>   - Action: **$A_2$ (Eligible to Pass Course)**
>   - **Test Case 3:** $M = 70, P = 60, C = 80$ (Total = 210 $\\ge 200$; $M+P = 130 < 150$; Aggregate $\\le 225$). Result: **Eligible to Pass Course**.
>
> - **Rule 4 (Eligible via Math+Physics Threshold, Aggregate $\\le 225$):**
>   - Conditions: $C_1 = T, C_2 = F, C_3 = T, C_4 = F$
>   - Action: **$A_2$ (Eligible to Pass Course)**
>   - **Test Case 4:** $M = 80, P = 75, C = 40$ (Total = 195 < 200; $M+P = 155 \\ge 150$; Aggregate $\\le 225$). Result: **Eligible to Pass Course**.
>
> - **Rule 5 (Eligible with Both Thresholds Met, Aggregate $\\le 225$):**
>   - Conditions: $C_1 = T, C_2 = T, C_3 = T, C_4 = F$
>   - Action: **$A_2$ (Eligible to Pass Course)**
>   - **Test Case 5:** $M = 80, P = 75, C = 65$ (Total = 220 $\\ge 200$; $M+P = 155 \\ge 150$; Aggregate $\\le 225$). Result: **Eligible to Pass Course**.
>
> - **Rule 6 (Eligible and Aggregate $> 225$):**
>   - Conditions: $C_1 = T, C_2 = T, C_3 = -, C_4 = T$
>   - Action: **$A_3$ (Eligible to Honors Course)**
>   - **Test Case 6:** $M = 85, P = 80, C = 75$ (Total = 240 > 225). Result: **Eligible to Honors Course**.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> قواعد القبول تحتوي شرطين بديلين للأهلية (مجموع المواد $\\ge 200$ أو مجموع الرياضيات والفيزياء $\\ge 150$) بشرط اجتياز الحدود الدنيا لكل مادة. جدول القرار يضمن تغطية الطالب الذي يحقق أحد الشرطين دون الآخر، والطالب الذي يفشل بمادة واحدة رغم تفوق مجموعه الكلي (فخ عدم الأهلية).""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2.3, pp. 384–388; companion slides 47–60, 207–208."
    },
    {
        "id": "8.44",
        "title": "Practical Program Fault Localization & Table 8.8 Debugging Guidelines (Exercise 8.44)",
        "prompt": "Test a program of your choice, and uncover several program errors. Localise the main route of these errors, and explain how you found the courses. Did you use the techniques of Table 8? Explain why or why not.",
        "answer": """> **Practical Case Study: Fault Localization and Application of Table 8.8 Debugging Guidelines:**
>
> **1. Target Program Case Study (Binary Search Algorithm):**
> An implementation of standard iterative binary search `binary_search(int arr[], int n, int key)`:
> ```c
> int low = 0, high = n; // Fault 1: Incorrect upper bound (should be n - 1)
> while (low <= high) {
>     int mid = (low + high) / 2; // Fault 2: Integer overflow vulnerability for large n
>     if (arr[mid] == key) return mid;
>     else if (arr[mid] < key) low = mid; // Fault 3: Infinite loop (should be mid + 1)
>     else high = mid - 1;
> }
> return -1;
> ```
>
> **2. Testing & Uncovering Program Errors:**
> - **Failure 1 (Out-of-Bounds Crash):** Executing test vector `key = 99` (element absent, greater than all items) causes array index out-of-bounds crash because `high = n` allowed `arr[n]` to be inspected.
> - **Failure 2 (Infinite Hang):** Executing test vector where `key` is present at an upper index causes the program to enter an infinite loop when `low == mid`.
>
> **3. Root Cause Localization:**
> - Using interactive symbolic debugging with execution trace logging, variable states `(low, mid, high)` were recorded at each iteration.
> - When `low = 2, high = 3`, `mid = (2+3)/2 = 2`. When `arr[2] < key`, executing `low = mid` leaves `low = 2`, creating a non-terminating cycle.
>
> **4. Application and Evaluation of Table 8.8 Debugging Principles:**
> - **Did we use Table 8.8 principles? YES.**
> - **Table 8.8 Guidelines Applied:**
>   - **Principle 1 (\"Think before making changes\"):** Rather than blindly inserting trial-and-error statements, we mathematically proved the loop invariant termination condition ($high - low$ must strictly decrease).
>   - **Principle 2 (\"Do not fix the symptom, fix the underlying defect\"):** Correcting `low = mid + 1` resolves the fundamental progress requirement of binary search rather than adding an ad-hoc loop counter break.
>   - **Principle 3 (\"Regression test the modification\"):** Re-running the complete test suite confirmed that existing cases (first element, middle element, last element) continue to pass.
>   - **Principle 4 (\"Look for similar faults\"):** Examining `mid = (low + high) / 2` revealed the classic numerical overflow bug when $low + high > 2^{31}-1$, which was preemptively refactored to `mid = low + (high - low) / 2`.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> يشير السؤال في الأصل إلى الجدول 8.8 في كتاب Aggarwal & Singh (صفحة 448) الخاص بقواعد وإرشادات تصحيح الأخطاء (Myers' Debugging Principles). جوهر هذه القواعد: فكر بعمق وحلل السبب الجذري قبل التعديل، لا تعالج العَرَض بل أصلح العيب البرمجي، وافحص بحثاً عن أخطاء مماثلة في باقي أجزاء الكود.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.7 & Table 8.8, pp. 446–450; companion slides 183–188, 211."
    },
    {
        "id": "8.48",
        "title": "Comprehensive Hybrid Multi-Tier Testing Strategy Proposal (Exercise 8.48)",
        "prompt": "Researchers and practitioners have proposed several mixed testing strategies intended to combine advantages of various techniques discussed in this chapter. Propose your own combination, perhaps also using some kind of random testing at selected points.",
        "answer": """> **Proposed 4-Tier Hybrid Testing Strategy (Combining Structural, Functional & Fuzzing):**
>
> **1. Rationale for a Hybrid Testing Strategy:**
> No single testing technique can uncover all classes of software defects. Functional techniques (BVA, Equivalence Partitioning) miss internal path anomalies; structural techniques (Basis Path, Data Flow) miss specification omissions; random testing misses subtle boundary thresholds. A rigorous hybrid strategy synergistically cascades techniques across development phases.
>
> **2. The 4-Tier Hybrid Architecture:**
>
> - **Tier 1: Specification-Based Functional Boundary Testing (Smoke & Sanity Phase)**
>   - **Techniques:** Boundary Value Analysis ($min, min^+, nom, max^-, max$) and Robust Equivalence Partitioning.
>   - **Objective:** Rapidly eliminate catastrophic interface mismatches, basic arithmetic edge-case bugs, and invalid parameter handling before investing in costly code instrumentation.
>
> - **Tier 2: Business Logic & Combinatorial Decision Table Testing (Core Logic Phase)**
>   - **Techniques:** Cause-Effect Graphing transformed into Reduced Decision Tables.
>   - **Objective:** Exhaustively verify complex boolean interactions, interdependent business policies, and multi-variable constraints that single-variable BVA cannot test.
>
> - **Tier 3: White-Box Structural Basis Path & Data Flow Testing (Adequacy Verification)**
>   - **Techniques:** McCabe's Cyclomatic Basis Path testing ($V(G)$ independent paths for 100% statement/branch coverage) combined with Data Flow Analysis targeting all $du$-paths that are NOT $dc$-paths.
>   - **Objective:** Force execution down hidden, error-prone exception branches, verify loop iterations, and eliminate data lifecycle hazards.
>
> - **Tier 4: Guided Random Testing / Fuzzing with Invariant Oracles (Stress & Security)**
>   - **Techniques:** Property-Based Random Testing (QuickCheck-style) and Automated Greybox Fuzzing (AFL-style) directed at high-complexity modules ($V(G) > 10$).
>   - **Objective:** Generate millions of semi-random, unexpected input sequences to uncover buffer overflows, race conditions, memory leaks, and unhandled exceptions that structured human-designed test suites overlooked.
>
> **3. Continuous Feedback and Regression Closure:**
> Mutation Testing is applied on a 10% representative sample of modules to calculate the Mutation Score ($MS$), validating that the test suite is genuinely sensitive to real code mutations.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> الإستراتيجية الهجينة المقترحة تدمج: (1) BVA للحدود الخارجية، (2) جداول القرار للقواعد المعقدة، (3) فحص المسارات وتدفق البيانات للكود الداخلي، و (4) الفحص العشوائي الموجه (Fuzzing) لكشف الثغرات الأمنية وتسريب الذاكرة. هذا المزيج يسد ثغرات كل تقنية منفردة.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2, §8.3, §8.4, §8.5, pp. 374–438; companion slides 211."
    },
    {
        "id": "8.49",
        "title": "Spell Checker Test Set Design & Systematic Inadequacy Evaluation (Exercise 8.49)",
        "prompt": "Design a test set for a spell checker. Then run it on a word processor having a spell checker, and report on possible inadequacies with respect to your requirements.",
        "answer": """> **Systematic Test Set Design & Inadequacy Analysis for Word Processor Spell Checkers:**
>
> **1. Structured Spell Checker Test Suite Taxonomy:**
>
> - **Category 1: Valid Word Acceptance (False Alarm Prevention):**
>   - Standard lexicon words (e.g., `algorithm`, `engineering`).
>   - Capitalized proper nouns and abbreviations (e.g., `IEEE`, `Baghdad`, `NASA`).
>   - Standard morphological inflections (plurals: `matrices`, `indices`; verb tenses: `running`, `quantized`).
>   - Hyphenated and compound words (e.g., `state-of-the-art`, `white-box`).
>
> - **Category 2: Classical Typographical Error Classes (Damerau-Levenshtein Metrics):**
>   - **Transposition of adjacent letters:** `teh` $\\to$ `the`, `recieve` $\\to$ `receive`.
>   - **Single-letter omission:** `comuter` $\\to$ `computer`, `sofware` $\\to$ `software`.
>   - **Single-letter insertion:** `proggam` $\\to$ `program`, `testting` $\\to$ `testing`.
>   - **Single-letter substitution:** `defenite` $\\to$ `definite`, `seperate` $\\to$ `separate`.
>
> - **Category 3: Phonetic / Sound-Alike Errors:**
>   - Words matching acoustic phonetic representations but misspelled: `fysics` $\\to$ `physics`, `neumaonia` $\\to$ `pneumonia`, `kat` $\\to$ `cat`.
>
> - **Category 4: Structural & Formatting Edge Cases:**
>   - Apostrophes and contractions: `don't`, `it's` vs. `its`.
>   - Mixed alphanumeric strings and code tokens: `var_name2`, `UTF8`, `HTML5`.
>   - Accented / diacritical characters and foreign loanwords: `résumé`, `naïve`.
>
> **2. Systematic Inadequacies Identified in Real-World Word Processors:**
> - **Inadequacy 1 (Contextual / Real-Word Spelling Errors):** Word-level spell checkers are completely blind to valid words used in the wrong syntactic or semantic context (e.g., *\"Their going to there house with they're car\"*, or *\"The whether was very cold\"*). Such errors require statistical Language Models or NLP parsers.
> - **Inadequacy 2 (Domain-Specific Technical Terminology):** Standard spell checkers aggressively flag valid postgraduate computer science terms (`cyclomatic`, `heuristics`, `mutant`, `CFG`, `heuristics`) as errors, inducing user alarm fatigue.
> - **Inadequacy 3 (Ranking of Suggested Replacements):** For severe phonetic corruptions, the replacement recommendation engine frequently buries the intended word deep in the candidate list or fails to suggest it entirely.""",
        "note": """> [!NOTE]
> **ملاحظة الطالب والفخ الامتحاني:**
>
> تصميم فحص المدقق الإملائي يغطي 4 فئات: الكلمات الصحيحة، الأخطاء الطباعية الكلاسيكية (إبدال، حذف، إضافة، تبديل متجاورين)، والأخطاء الصوتية، والحالات الهيكلية. أهم قصور (Inadequacy) يطلب في الامتحان هو عجز المدقق عن كشف الأخطاء السياقية (Real-word spelling errors مثل خلط their و there) لأن الكلمة بحد ذاتها صحيحة معجمياً.""",
        "source": "Aggarwal & Singh (3rd ed.), §8.2, pp. 374–388; companion slides 211."
    }
]

retrieval_set = """<!-- Print-hidden study guidance retained for screen use.
## Retrieval Set & Active Recall Self-Test

1. For a function with n independent input variables, state the exact test-case count required by Boundary Value Analysis (BVA), Robustness testing, and Worst-Case testing.
2. In the NextDate calendar problem, what are the five test points for the Day variable, and what outputs are expected for out-of-boundary inputs?
3. How many test cases are required to achieve 100% statement coverage for the Largest of Three Numbers program, and to what structural property do they correspond?
4. Using a simple 20-iteration loop with 3 selection branches, mathematically demonstrate why exhaustive testing is impossible.
5. In the Extended Triangle problem, state the Pythagorean Theorem criterion and provide two valid right-angled test vectors.
6. Detail the valid and invalid equivalence classes for the Student Grading system.
7. Explain why negative integers require specialized testing attention when determining Odd/Even status in C/C++.
8. In the Professional Course Admission problem, explain how Decision Tables handle candidates with high aggregate marks who fail a single subject cutoff.
9. Summarize the core debugging philosophy codified in Myers' Table 8.8.
10. Describe the four tiers of the proposed hybrid testing strategy and the unique defect profile targeted by each tier.
11. What is a \"real-word spelling error\", and why do standard dictionary-based spell checkers fail to detect it?
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
