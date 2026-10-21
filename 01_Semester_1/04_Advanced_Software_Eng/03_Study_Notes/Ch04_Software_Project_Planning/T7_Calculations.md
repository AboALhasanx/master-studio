---
title: "ASE Chapter 4 — T7 Numerical Calculations & Solved Problems Pack · Software Project Planning"
# subtitle: "Step-by-Step Solutions: 10 Textbook Exercises, 4 Reproduced Examples, and 8 Authored Practice Problems"
course: "Advanced Software Engineering (CS603)"
author: "Master Studio — Academic Tutoring Engine"
date: "2026-10-19"
doc_type: "study_pack"
header_left: "ASE Chapter 4 — T7 Numerical Calculations"
header_right: "Software Project Planning: Mathematical Models & Calculations"
footer_left: "College of Computer Science & IT — University of Wasit"
footer_right: "Page {page} of {topage}"
---

# Chapter 4 — T7 Numerical Calculations & Solved Problems Pack
<!--

This pack contains **10 textbook calculation exercises** (Exercises 4.5, 4.10, 4.11, 4.13, 4.14, 4.16, 4.20, 4.21, 4.25, and 4.29), **4 reproduced worked examples** (Examples 4.9, 4.10, 4.12, and 4.17), and **8 authored practice problems**. The authored problems are identified as such and are not presented as textbook examples.

> **Solution structure:**
> Numerical answers use the relevant parts of the following course calculation sequence; short calculations may combine adjacent steps when the assumptions and arithmetic remain clear:
> - **1. Given:** Stated numerical values and domain conditions with explicit units.
> - **2. Required:** Target metric(s) with dimensional units.
> - **3. Model & Assumptions:** Explicit mathematical framework, mode, version, and minimal assumptions.
> - **4. Equation:** Governing formula written in standard symbols.
> - **5. Substitution & Working:** Step-by-step arithmetic with intermediate values shown.
> - **6. Result:** Final calculated value with standard engineering units.
> - **7. Check / Interpretation:** Sanity check, dimensional check, or managerial takeaway.
> - **8. Source:** Exact textbook page (printed pp. 139–202) and companion slide locator (slides 1–207).

---

-->
## Section 1: The 10 Official Textbook Calculation Exercises

### Problem 7.1 (Exercise 4.5): Function Point Value for Moderate Domain Project

**Compute the function point (FP) value for a project with the following information domain characteristics:**
- **Number of user inputs = 30**
- **Number of user outputs = 42**
- **Number of user enquiries = 08**
- **Number of files = 07**
- **Number of external interfaces = 6**
**Assume that all complexity adjustment values are moderate.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Number of External Inputs (EI) = $30$
>    - Number of External Outputs (EO) = $42$
>    - Number of External Enquiries (EQ) = $8$
>    - Number of Internal Logical Files (ILF) = $7$
>    - Number of External Interface Files (EIF) = $6$
>    - Component Complexity Ratings = "Moderate" (Average complexity weights)
>    - General System Characteristics (GSCs) = "Moderate" ($F_i = 3$ for each of the 14 factors)
>
> - **2. Required:**
>    - Unadjusted Function Points (UFP)
>    - Complexity Adjustment Factor (CAF)
>    - Final Adjusted Function Points (FP)
>
> - **3. Model & Assumptions:**
>    Albrecht Function Point Analysis (FPA). Average weights per IFPUG/course standard: $\text{EI}=4$, $\text{EO}=5$, $\text{EQ}=4$, $\text{ILF}=10$, $\text{EIF}=7$.
>
> - **4. Equations:**
>    $$\text{UFP} = \sum_{i=1}^5 (\text{Count}_i \times W_i)$$
>    $$\text{CAF} = 0.65 + 0.01 \times \sum_{i=1}^{14} F_i$$
>    $$\text{FP} = \text{UFP} \times \text{CAF}$$
>
> - **5. Substitution & Working:**
>    - *Unadjusted Function Points (UFP):*
>      - $\text{EI: } 30 \times 4 = 120$
>      - $\text{EO: } 42 \times 5 = 210$
>      - $\text{EQ: } 8 \times 4 = 32$
>      - $\text{ILF: } 7 \times 10 = 70$
>      - $\text{EIF: } 6 \times 7 = 42$
>      $$\text{UFP} = 120 + 210 + 32 + 70 + 42 = 474 \text{ UFP}$$
>    - *Complexity Adjustment Factor (CAF):*
>      With 14 factors rated as moderate ($F_i = 3$):
>      $$\sum_{i=1}^{14} F_i = 14 \times 3 = 42$$
>      $$\text{CAF} = 0.65 + 0.01 \times (42) = 0.65 + 0.42 = 1.07$$
>    - *Final Adjusted Function Points:*
>      $$\text{FP} = 474 \times 1.07 = 507.18 \text{ FP}$$
>
> - **6. Result:**
>    - $\text{UFP} = 474 \text{ UFP}$
>    - $\text{CAF} = 1.07$
>    - $\text{Adjusted FP} = 507.18 \approx 507 \text{ FP}$
>
> - **7. Check / Interpretation:**
>    $\text{CAF} = 1.07$ lies safely within the valid bounded range $[0.65, 1.35]$, reflecting a $7\%$ upward adjustment for transactional complexity.
>
> - **8. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), Exercise 4.5, printed p. 201; Companion Slide 200.

---

<div class="page-break"></div>

### Problem 7.2 (Exercise 4.10): Function-Point Count for the Payroll Program

**Compute the function-point value for a payroll program that reads an employee file and a current-month information file, prints cheques for employees, and accepts an interactive command to print an individually requested cheque immediately.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:** Two files are read; the program prints the monthly cheque run and can print an individually requested cheque.
>
> - **2. Required:** Classify the stated functions and calculate the unadjusted function-point count.
>
> - **3. Counting assumptions:** Use average weights because the exercise gives no complexity tiers. Assume both files are maintained by this application. Count the interactive command as one EI and its requested cheque as a second EO. No separate inquiry screen or other external interface is stated.
>
> - **4. Weights:** Average EI = 4, EO = 5, EQ = 4, ILF = 10, EIF = 7.
>
> - **5. Working:**
>    - ILF: employee file and current-month file = $2\times10=20$ UFP.
>    - EI: individual-cheque command = $1\times4=4$ UFP.
>    - EO: monthly cheque output and individually requested cheque output = $2\times5=10$ UFP.
>    - EQ = 0 and EIF = 0 under the stated assumptions.
>    $$\text{UFP}=20+4+10=34$$
>
> - **6. Result:** The stated counting interpretation gives **34 UFP**. With no general-system-characteristic ratings supplied, this answer reports UFP; if an adjusted FP total is required, a CAF assumption must be stated.
>
> - **7. Alternative classification:** If the interactive request/response is treated as one EQ instead of one EI plus one EO, the count is $20+4=24$ UFP. The prompt does not prescribe a function-boundary convention, so keep the chosen interpretation explicit.
>
> - **8. Source:** K.K. Aggarwal & Yogesh Singh (3rd ed.), Exercise 4.10, printed p. 201. The exercise supplies no complexity ratings or answer key.

---

### Problem 7.3 (Exercise 4.11): Payroll Extension with Historical Cheque Data

**Add a file containing printed cheques; the file is printed and read on the next run to produce a report comparing current- and previous-month payroll expenses. Compute the function points and explain the difference from Exercise 4.10.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Baseline:** Use the explicit Exercise 4.10 interpretation in Problem 7.2: $34$ UFP.
>
> - **2. Added functions stated in Exercise 4.11:**
>    - One historical cheque file maintained by the payroll application: $1$ ILF.
>    - Printing that file and producing the month-comparison report: $2$ EOs.
>    - No new input screen or independent inquiry is stated.
>
> - **3. Incremental count:** With the same average weights, $\Delta\text{UFP}=1(10)+2(5)=20$ UFP.
>
> - **4. Result:** $\text{UFP}_{new}=34+20=54$ UFP under the stated counting convention. The added persistent historical data and two named outputs explain the increase. Self-interfacing may affect function boundaries and complexity, but the prompt does not specify extra schema, date-range controls, or statistical functions.
>
> - **5. Alternative convention:** If the on-demand cheque in Exercise 4.10 is counted as one EQ rather than EI+EO, its baseline becomes 24 UFP and this extension becomes 44 UFP under the same average weights.
>
> - **6. Source:** K.K. Aggarwal & Yogesh Singh (3rd ed.), Exercise 4.11, printed p. 201. The prompt supplies no complexity ratings or publisher solution.

---

### Problem 7.4 (Exercise 4.13): Cost & Effort Prediction for 22 KLOC via Walston-Felix vs. SEL Models

**The size of a software product to be developed has been estimated to be 22,000 LOC. Predict the manpower cost (effort) by the Walston-Felix Model and the SEL Model.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Software Size $L = 22,000 \text{ LOC} = 22 \text{ KLOC}$
>
> - **2. Required:**
>    - Predicted Effort in Person-Months ($E$) using the Walston-Felix Model.
>    - Predicted Effort in Person-Months ($E$) using the Software Engineering Laboratory (SEL) Model.
>
> - **3. Model & Assumptions:**
>    - Static single-variable power models where effort is a direct power function of lines of code in thousands ($L$ in KLOC).
>
> - **4. Equations:**
>    - **Walston-Felix Model (IBM Federal Systems):**
>      $$E = 5.2 \times L^{0.91} \text{ [Person-Months]}$$
>    - **SEL Model (NASA Goddard Space Flight Center):**
>      $$E = 1.4 \times L^{0.93} \text{ [Person-Months]}$$
>
> - **5. Substitution & Working:**
>    - *Walston-Felix Model:* $E = 5.2 \times (22)^{0.91} = 5.2 \times 16.6573 \approx 86.62 \text{ Person-Months}$.
>    - *SEL Model:* $E = 1.4 \times (22)^{0.93} = 1.4 \times 17.7196 \approx 24.81 \text{ Person-Months}$.
>
> - **6. Result:**
>    - **Walston-Felix Predicted Effort:** $86.62 \text{ Person-Months}$
>    - **SEL Predicted Effort:** $24.81 \text{ Person-Months}$
>
> - **7. Check / Interpretation:**
>    The two models return different estimates for the same size because they use different fitted coefficients and exponents. Select a model only when its calibration context is appropriate.
>
> - **8. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), Exercise 4.13, printed p. 201; Companion Slide 202.

---

<div class="page-break"></div>

### Problem 7.5 (Exercise 4.14): Conditional LOC and Productivity Estimates for 100 Person-Months

**A database system is to be developed. The effort has been estimated to be 100 Person-Months. Calculate the number of lines of code and productivity in LOC/Person-Month.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Development Effort $E = 100 \text{ Person-Months}$
>    - Application Domain = Database System
>    - *(Notice of Course Source Ambiguity: The textbook prompt omits the specific estimation model. Per course protocol, solutions are derived conditionally under both canonical static models: SEL and Walston-Felix).*
>
> - **2. Required:**
>    - Estimated Size in delivered code lines ($L$ in KLOC and LOC).
>    - Development Productivity ($P$ in LOC/Person-Month).
>
> - **3. Model & Assumptions:**
>    - **Case A:** NASA SEL Model ($E = 1.4 L^{0.93}$)
>    - **Case B:** IBM Walston-Felix Model ($E = 5.2 L^{0.91}$)
>
> - **4. Equations:**
>    $$L = \left(\frac{E}{a}\right)^{1/b} \text{ [KLOC]}$$
>    $$\text{Productivity } P = \frac{L \times 1000}{E} \text{ [LOC/PM]}$$
>
> - **5. Substitution & Working:**
>    - **Case A: Solution under SEL Model ($a=1.4, b=0.93$):**
>      $$L^{0.93} = \frac{100}{1.4} \approx 71.4286$$
>      $$L = (71.4286)^{1 / 0.93} = (71.4286)^{1.07527} \approx 98.494 \text{ KLOC}$$
>      $$\text{Total Lines of Code } = 98,494 \text{ LOC}$$
>      $$\text{Productivity } P = \frac{98,494 \text{ LOC}}{100 \text{ PM}} \approx 984.94 \text{ LOC/Person-Month}$$
>    - **Case B: Solution under Walston-Felix Model ($a=5.2, b=0.91$):**
>      $$L^{0.91} = \frac{100}{5.2} \approx 19.2308$$
>      $$L = (19.2308)^{1 / 0.91} = (19.2308)^{1.09890} \approx 25.762 \text{ KLOC}$$
>      $$\text{Total Lines of Code } = 25,762 \text{ LOC}$$
>      $$\text{Productivity } P = \frac{25,762 \text{ LOC}}{100 \text{ PM}} \approx 257.62 \text{ LOC/Person-Month}$$
>
> - **6. Result:**
>    - **Under SEL Assumption:** $\text{Size} = 98.49 \text{ KLOC} \quad (98,494 \text{ LOC}), \quad \text{Productivity} = 984.94 \text{ LOC/PM}$
>    - **Under Walston-Felix Assumption:** $\text{Size} = 25.76 \text{ KLOC} \quad (25,762 \text{ LOC}), \quad \text{Productivity} = 257.62 \text{ LOC/PM}$
>
> - **7. Check / Interpretation:**
>    The exercise omits the governing model, so neither size estimate is uniquely determined from the prompt alone. Productivity is calculated from each model's conditional size estimate.
>
> - **8. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), Exercise 4.14, printed p. 201; Companion Slide 202.

---

<div class="page-break"></div>

### Problem 7.6 (Exercise 4.16): Basic COCOMO Estimation for 32 KLOC Organic Product

**Explain all the levels of the COCOMO model. Assume that the size of an organic software product has been estimated to be 32,000 lines of code. Determine the effort required to develop the software product, the nominal development time, and the average staffing level.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Software Product Size $L = 32,000 \text{ LOC} = 32 \text{ KLOC}$
>    - Mode = Organic Mode (Small, in-house team, familiar domain)
>    - Model Level = Basic COCOMO '81
>    - Organic Coefficients: $a_b = 2.4, \quad b_b = 1.05, \quad c_b = 2.5, \quad d_b = 0.38$
>
> - **2. COCOMO levels and required results:** Basic COCOMO uses size and mode; Intermediate COCOMO adds an effort adjustment factor from cost drivers; Detailed COCOMO applies cost-driver effects by development phase. This calculation uses Basic COCOMO to find effort, nominal development time, and average staffing.
>
> - **3. Model & Assumptions:**
>    Barry Boehm's Basic COCOMO '81 Organic equations. Single-variable static power model.
>
> - **4. Equations:**
>    $$E = a_b \times (\text{KLOC})^{b_b} \text{ [Person-Months]}$$
>    $$D = c_b \times (E)^{d_b} \text{ [Months]}$$
>    $$\text{Average Staffing } S = \frac{E}{D} \text{ [Persons]}$$
>
> - **5. Substitution & Working:**
>    - *Effort Calculation:*
>      $$E = 2.4 \times (32)^{1.05}$$
>      $$\ln(32) \approx 3.4657 \implies 1.05 \times 3.4657 = 3.6390$$
>      $$(32)^{1.05} = e^{3.6390} \approx 38.0546$$
>      $$E = 2.4 \times 38.0546 \approx 91.33 \text{ Person-Months}$$
>    - *Development Time / Schedule Calculation:*
>      $$D = 2.5 \times (91.33)^{0.38}$$
>      $$\ln(91.33) \approx 4.5145 \implies 0.38 \times 4.5145 = 1.7155$$
>      $$(91.33)^{0.38} = e^{1.7155} \approx 5.5595$$
>      $$D = 2.5 \times 5.5595 \approx 13.90 \text{ Months}$$
>    - *Average Staffing Level:*
>      $$S = \frac{E}{D} = \frac{91.33 \text{ PM}}{13.90 \text{ Months}} \approx 6.57 \text{ Persons}$$
>
> - **6. Result:**
>    - **Effort ($E$):** $91.33 \text{ Person-Months}$
>    - **Development Time ($D$):** $13.90 \text{ Months}$
>    - **Average Staffing ($S$):** $6.57 \approx 7 \text{ Persons}$
>
> - **7. Check / Interpretation:**
>    The staffing check is consistent: $6.57$ persons over $13.90$ months gives approximately $91.3$ person-months.
>
> - **8. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), Exercise 4.16, printed p. 201; Companion Slide 203.

---

<div class="page-break"></div>

### Problem 7.7 (Exercise 4.20): Five-Module Office Automation System with Cost Drivers & Phase Breakdown

**Suppose a system for office automation is to be designed. It is clear from requirements that there will be five modules of size 0.5 KLOC, 1.5 KLOC, 2.0 KLOC, 1.0 KLOC, and 2.0 KLOC respectively. Complexity and reliability requirements are high. Programmer capability and experience are low. All other factors are of nominal rating. Use the COCOMO model to determine overall cost and schedule estimates. Also calculate the cost and schedule estimates for different phases.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - 5 Module Sizes: $0.5 + 1.5 + 2.0 + 1.0 + 2.0 = 7.0 \text{ KLOC}$.
>    - Application: Office Automation.
>    - Stated Constraints: High complexity, High reliability, Low programmer capability, Low programmer experience; all others nominal.
>
> - **2. Required:**
>    - Statement of model assumptions and ambiguities.
>    - Intermediate COCOMO Effort Adjustment Factor ($\text{EAF}$).
>    - Overall effort ($E$) and schedule ($D$).
>    - Phase-wise allocation across lifecycle phases under Book Table 4.7 source values and normalized values.
>
> - **3. Model & Explicit Assumptions (Handling Prompt Ambiguities):**
>    - **Mode Ambiguity:** The prompt specifies office automation (7 KLOC) without naming the mode. In COCOMO '81, small in-house office systems ($\le 50 \text{ KLOC}$) default to **Organic Mode** ($a=3.2, b=1.05, c=2.5, d=0.38$). If developed under unfamiliar or rigid corporate environments, **Semidetached Mode** ($a=3.0, b=1.12, c=2.5, d=0.35$) represents a valid alternative.
>    - **Experience-driver ambiguity:** The exercise says programmer capability and experience are low but does not identify the experience category. Low PCAP is $1.19$. For the single low-experience rating, the possible multipliers are AEXP $1.13$, LEXP $1.14$, or VEXP $1.10$. Use one category at a time; the wording does not justify setting all three low.
>      - *Baseline (AEXP = 1.13):* $\text{EAF}=1.15\times1.15\times1.19\times1.13\approx1.7784$, giving $E\approx43.91$ PM and $D\approx10.52$ months.
>      - *Alternative (LEXP = 1.14):* $\text{EAF}\approx1.7941$, giving $E\approx44.29$ PM and $D\approx10.56$ months.
>      - *Alternative (VEXP = 1.10):* $\text{EAF}\approx1.7312$, giving $E\approx42.74$ PM and $D\approx10.41$ months.
>      *AEXP is the baseline because the described product is an office-automation application; the alternatives preserve the prompt's missing detail.*
>
> - **4. Equations:**
>    $$E_{\text{nom}} = a_i \times (\text{KLOC})^{b_i} = 3.2 \times (7.0)^{1.05}$$
>    $$\text{EAF} = \prod_{j=1}^{15} EM_j = 1.15 \text{ (CPLX)} \times 1.15 \text{ (RELY)} \times 1.19 \text{ (PCAP)} \times 1.13 \text{ (AEXP)} \approx 1.7784$$
>    $$E = E_{\text{nom}} \times \text{EAF}, \quad D = c_i \times (E)^{d_i} = 2.5 \times (E)^{0.38}$$
>
> - **5. Substitution & Working:**
>    - *Size & Nominal Effort:*
>      $$\text{Size} = 7.0 \text{ KLOC} \implies E_{\text{nom}} = 3.2 \times (7.0)^{1.05} = 3.2 \times 7.71530 \approx 24.69 \text{ Person-Months}$$
>    - *Adjusted Effort & Schedule (Baseline AEXP = 1.13):*
>      $$E = 24.68897 \times 1.77837 \approx 43.91 \text{ Person-Months}$$
>      $$D = 2.5 \times (43.906)^{0.38} \approx 10.52 \text{ Months}$$
>      $$\text{Average Staffing} = \frac{43.91}{10.52} \approx 4.17 \text{ Persons}$$
>    - *Phase-Wise Allocation (Book Table 4.7 / Slides 62 & 63 for Organic Small $S \approx 2$):*
>      - **Raw Book Table 4.7 Fractions (Direct Unconstrained Allocation):**
>        - Plan & Requirements: $0.06\times43.91\approx2.63$ PM; $0.10\times10.52\approx1.05$ months.
>        - System Design: $0.16\times43.91\approx7.03$ PM; $0.19\times10.52\approx2.00$ months.
>        - Detailed Design: $0.26\times43.91\approx11.42$ PM; $0.24\times10.52\approx2.52$ months.
>        - Module Code & Test: $0.42\times43.91\approx18.44$ PM; $0.39\times10.52\approx4.10$ months.
>        - Integration & Test: $0.16\times43.91\approx7.03$ PM; $0.18\times10.52\approx1.89$ months.
>        *(The raw phase fractions sum to 106% effort and 110% schedule: $43.91\times1.06\approx46.54$ PM and $10.52\times1.10\approx11.57$ months.)*
>      - **Normalized Allocation (Re-scaled to 100%):**
>        - Plan & Requirements: normalized effort $6/106\times43.91\approx2.49$ PM; schedule $10/110\times10.52\approx0.96$ months.
>        - System Design: normalized effort $16/106\times43.91\approx6.63$ PM; schedule $19/110\times10.52\approx1.82$ months.
>        - Detailed Design: normalized effort $26/106\times43.91\approx10.77$ PM; schedule $24/110\times10.52\approx2.30$ months (using unrounded $D$).
>        - Module Code & Test: normalized effort $42/106\times43.91\approx17.40$ PM; schedule $39/110\times10.52\approx3.73$ months.
>        - Integration & Test: normalized effort $16/106\times43.91\approx6.63$ PM; schedule $18/110\times10.52\approx1.72$ months.
>        *(Normalized totals equal $43.91$ PM and $10.52$ months, subject to displayed rounding.)*
>
> - **6. Result:**
>    - **Baseline Effort ($E$):** $43.91$ PM under AEXP; alternatives are $44.29$ PM (LEXP) and $42.74$ PM (VEXP).
>    - **Baseline Schedule ($D$):** $10.52$ months under AEXP; alternatives are $10.56$ months (LEXP) and $10.41$ months (VEXP).
>    - **Average Staffing:** approximately $4.17$ persons under AEXP.
>
> - **7. Check & Source Discrepancy Notice:**
>    The book's Table 4.7 values are split across companion Slides 62–63. The raw fractions sum to $106\%$ effort and $110\%$ schedule; the normalized phase values sum to the baseline totals above.
>
> - **8. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), Exercise 4.20, printed p. 201; Companion Slides 62–63.

---

<div class="page-break"></div>

### Problem 7.8 (Exercise 4.21): Multi-Mode COCOMO Comparison for 600 KLOC Project

**Suppose that a project was estimated to be 600 KLOC. Calculate the effort and development time for each of the three modes: organic, semidetached, and embedded.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Project Size $L = 600 \text{ KLOC}$
>    - Model = Basic COCOMO '81
>    - Mode Coefficients Table:
>      - Organic: $a = 2.4, \quad b = 1.05, \quad c = 2.5, \quad d = 0.38$
>      - Semidetached: $a = 3.0, \quad b = 1.12, \quad c = 2.5, \quad d = 0.35$
>      - Embedded: $a = 3.6, \quad b = 1.20, \quad c = 2.5, \quad d = 0.32$
>
> - **2. Required:**
>    - Effort ($E$) and Schedule ($D$) under Organic Mode.
>    - Effort ($E$) and Schedule ($D$) under Semidetached Mode.
>    - Effort ($E$) and Schedule ($D$) under Embedded Mode.
>
> - **3. Model & Assumptions:**
>    Basic COCOMO power equations. Evaluated across all 3 modes to demonstrate the mathematical penalty of environmental complexity.
>
> - **4. Equations:**
>    $$E = a \times (\text{KLOC})^b \text{ [Person-Months]}, \quad D = c \times (E)^d \text{ [Months]}$$
>
> - **5. Substitution & Working:**
>    - **Mode 1: Organic Mode ($a=2.4, b=1.05, c=2.5, d=0.38$):**
>      $$(600)^{1.05} = e^{1.05 \times \ln(600)} = e^{1.05 \times 6.39693} = e^{6.71678} \approx 826.15$$
>      $$E_{\text{organic}} = 2.4 \times 826.15 \approx 1,982.76 \text{ Person-Months}$$
>      $$D_{\text{organic}} = 2.5 \times (1,982.76)^{0.38} = 2.5 \times 17.9045 \approx 44.76 \text{ Months}$$
>    - **Mode 2: Semidetached Mode ($a=3.0, b=1.12, c=2.5, d=0.35$):**
>      $$(600)^{1.12} = e^{1.12 \times 6.39693} = e^{7.16456} \approx 1,292.79$$
>      $$E_{\text{semi}} = 3.0 \times 1,292.79 \approx 3,878.38 \text{ Person-Months}$$
>      $$D_{\text{semi}} = 2.5 \times (3,878.38)^{0.35} = 2.5 \times 18.0313 \approx 45.08 \text{ Months}$$
>    - **Mode 3: Embedded Mode ($a=3.6, b=1.20, c=2.5, d=0.32$):**
>      $$(600)^{1.20} = e^{1.20 \times 6.39693} = e^{7.67632} \approx 2,156.66$$
>      $$E_{\text{embedded}} = 3.6 \times 2,156.66 \approx 7,763.97 \text{ Person-Months}$$
>      $$D_{\text{embedded}} = 2.5 \times (7,763.97)^{0.32} = 2.5 \times 17.5722 \approx 43.93 \text{ Months}$$
>
> - **6. Result:**
>    - **Organic:** $E = 1,982.8 \text{ PM}, \quad D = 44.8 \text{ Months} \quad (\text{Staff} \approx 44.3 \text{ Persons})$
>    - **Semidetached:** $E = 3,878.4 \text{ PM}, \quad D = 45.1 \text{ Months} \quad (\text{Staff} \approx 86.0 \text{ Persons})$
>    - **Embedded:** $E = 7,764.0 \text{ PM}, \quad D = 43.9 \text{ Months} \quad (\text{Staff} \approx 176.7 \text{ Persons})$
>
> - **7. Check / Interpretation:**
>    The three modes produce similar schedules (about 44–45 months) but substantially different effort estimates. The exercise asks for all three cases; project size alone does not determine which mode applies.
>
> - **8. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), Exercise 4.21, printed p. 202; Companion Slide 204.

---

<div class="page-break"></div>

### Problem 7.9 (Exercise 4.25): COCOMO II Post-Architecture Effort Estimation for 100 KLOC

**A software project of application generator category with an estimated size of 100 KLOC has to be developed. The scale factor ($B$) has high precedentedness and high development flexibility. Other scale factors are nominal. The cost drivers are high reliability, medium database size, high personnel capability, and high analyst capability. The other cost drivers are nominal. Calculate the effort in Person-Months for the development of the project.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Size = $100 \text{ KLOC}$ ($100,000 \text{ SLOC}$)
>    - Stated Category: "Application generator category"
>    - 5 Scale Factors ($SF_j$):
>      - Precedentedness (PREC) = High ($W_1 = 2.48$)
>      - Development Flexibility (FLEX) = High ($W_2 = 2.03$)
>      - Architecture/Risk Resolution (RESL) = Nominal ($W_3 = 4.24$)
>      - Team Cohesion (TEAM) = Nominal ($W_4 = 3.29$)
>      - Process Maturity (PMAT) = Nominal ($W_5 = 4.68$)
>    - Effort Multipliers ($EM_i$):
>      - Required Reliability (RELY) = High ($EM = 1.10$)
>      - Database Size (DATA) = Medium / Nominal ($EM = 1.00$)
>      - Personnel Capability (PCAP) = High ($EM = 0.88$)
>      - Analyst Capability (ACAP) = High ($EM = 0.85$)
>      - All remaining 13 drivers = Nominal ($1.00$)
>
> - **2. Model Selection & Prompt Ambiguity Resolution:**
>    - The prompt labels the project as "application generator category", which might colloquially suggest the COCOMO II *Application Composition Model*. However, Application Composition operates strictly on Object Points (screens, reports, 3GL components) and does not utilize scale factors or detailed driver multipliers.
>    - In contrast, the prompt explicitly supplies:
>      1. Size in **Lines of Code (100 KLOC)**.
>      2. Five distinct **Scale Factors** ($SF$) that determine exponent $B$.
>      3. Four detailed cost drivers: **RELY, DATA, PCAP, and ACAP**. In COCOMO II, these standalone drivers exist *exclusively* in the **Post-Architecture Model** (the Early Design model aggregates drivers into 7 coarse factors like RCPX and PERS).
>    - Therefore, the mathematical parameters unambiguously dictate the **COCOMO II Post-Architecture Model** ($A = 2.94$), while "application generator" reflects the software application domain rather than the COCOMO II sizing stage.
>
> - **3. Required:**
>    - Scaling Exponent ($B$).
>    - Nominal Effort ($E_{\text{nom}}$).
>    - Effort Adjustment Factor ($\text{EAF}$).
>    - Final Development Effort ($E$) in Person-Months.
>
> - **4. Model & Equations:**
>    $$B = 0.91 + 0.01 \times \sum_{j=1}^5 SF_j$$
>    $$E_{\text{nom}} = 2.94 \times (\text{Size})^B$$
>    $$\text{EAF} = \prod_{i=1}^{17} EM_i$$
>    $$E = E_{\text{nom}} \times \text{EAF}$$
>
> - **5. Substitution & Working:**
>    - *Sum of Scale Factors ($\sum SF$):*
>      $$\sum SF = 2.48 (\text{PREC}) + 2.03 (\text{FLEX}) + 4.24 (\text{RESL}) + 3.29 (\text{TEAM}) + 4.68 (\text{PMAT}) = 16.72$$
>    - *Scaling Exponent ($B$):*
>      $$B = 0.91 + 0.01 \times (16.72) = 0.91 + 0.1672 = 1.0772$$
>    - *Nominal Effort ($E_{\text{nom}}$):*
>      $$(100)^{1.0772} = e^{1.0772 \times \ln(100)} = e^{1.0772 \times 4.60517} = e^{4.96069} \approx 142.693$$
>      $$E_{\text{nom}} = 2.94 \times 142.693 \approx 419.52 \text{ Person-Months}$$
>    - *Effort Adjustment Factor (EAF):*
>      $$\text{EAF} = 1.10 (\text{RELY}) \times 1.00 (\text{DATA}) \times 0.88 (\text{PCAP}) \times 0.85 (\text{ACAP}) = 0.8228$$
>    - *Final Adjusted Effort ($E$):*
>      $$E = 419.52 \times 0.8228 \approx 345.18 \text{ Person-Months}$$
>
> - **6. Result:**
>    - **Scaling Exponent ($B$):** $1.0772$
>    - **Nominal Effort:** $419.52 \text{ PM}$
>    - **Effort Adjustment Factor:** $0.8228$
>    - **Final Predicted Effort:** $345.18 \approx 345 \text{ Person-Months}$
>
> - **7. Check / Interpretation:**
>    High analyst and personnel capability combined to yield an $\text{EAF}$ of $0.8228$, reducing nominal development effort by about $17.7\%$.
>
> - **8. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), Exercise 4.25, printed p. 202; Companion Slides 115–120.

---

<div class="page-break"></div>

### Problem 7.10 (Exercise 4.29). Putnam Model — Duration and Development Effort

**Assuming the Putnam model, with software size $S = 100{,}000 \text{ LOC}$, technology constant $C = 5000$, and manpower build-up parameter $D_0 = 15 \text{ persons/year}^2$, compute the development time $t_d$ and development manpower effort $K_d$.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:** $S=100{,}000$ LOC, $C=5000$, and $D_0=15$ persons/year$^2$.
>
> - **2. Required:** Development time $t_d$ and development-sub-cycle effort $K_d$.
>
> - **3. Governing relations:**
>    $$S=C K^{1/3}t_d^{4/3}, \qquad D_0=\frac{K}{t_d^3}, \qquad K=6K_d$$
>    Here $K$ is the full-project effort in the Putnam software equation, while $K_d$ is the total effort of the development sub-cycle.
>
> - **4. Solve for $t_d$:** From $K=D_0t_d^3$,
>    $$S=C(D_0t_d^3)^{1/3}t_d^{4/3}=C D_0^{1/3}t_d^{7/3}$$
>    $$t_d=\left(\frac{(S/C)^3}{D_0}\right)^{1/7}=\left(\frac{(100{,}000/5000)^3}{15}\right)^{1/7}\approx2.452\text{ years}$$
>
> - **5. Solve for effort:**
>    $$K=D_0t_d^3=15(2.452287)^3\approx221.21\text{ person-years}$$
>    $$K_d=\frac{K}{6}\approx36.87\text{ person-years}$$
>
> - **6. Check:** Substituting $K$ and $t_d$ into $C K^{1/3}t_d^{4/3}$ recovers approximately $100{,}000$ LOC; $K/t_d^3\approx15$.
>
> - **7. Result:** $t_d\approx2.45$ years and $K_d\approx36.87$ person-years.
>
> - **8. Source:** K.K. Aggarwal & Yogesh Singh (3rd ed.), Exercise 4.29, printed p. 202; Companion Slide 206. Both show $C=5000$.
---

## Section 2: Reproduced Textbook Examples and Authored Practice

Problems 7.15, 7.20, 7.21, and 7.22 reproduce textbook Examples 4.12, 4.9, 4.10, and 4.17, respectively. Problems 7.11–7.14 and 7.16–7.19 are authored practice. The Chapter Index records how the remaining source examples are covered elsewhere in the packs.

<div class="page-break"></div>

### Practice Problem 7.11. Function Point Calculation for a Standard Business System

**Consider a software project with the following information domain characteristics: Number of user inputs = 24 (Average), Number of user outputs = 16 (Low), Number of user inquiries = 22 (Average), Number of files = 4 (High), Number of external interfaces = 2 (Low). The sum of the 14 complexity adjustment factors is 32. Calculate the final adjusted Function Points.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - External Inputs (EI) = $24$ @ Average ($W = 4$)
>    - External Outputs (EO) = $16$ @ Low ($W = 4$)
>    - External Inquiries (EQ) = $22$ @ Average ($W = 4$)
>    - Internal Logical Files (ILF) = $4$ @ High ($W = 15$)
>    - External Interface Files (EIF) = $2$ @ Low ($W = 5$)
>    - $\sum_{i=1}^{14} F_i = 32$
>
> - **2. Required:**
>    - Unadjusted Function Points (UFP)
>    - Complexity Adjustment Factor (CAF)
>    - Final Adjusted Function Points (FP)
>
> - **3. Working & Computation:**
>    - $\text{UFP} = (24 \times 4) + (16 \times 4) + (22 \times 4) + (4 \times 15) + (2 \times 5) = 96 + 64 + 88 + 60 + 10 = 318 \text{ UFP}$
>    - $\text{CAF} = 0.65 + 0.01 \times (32) = 0.65 + 0.32 = 0.97$
>    - $\text{FP} = \text{UFP} \times \text{CAF} = 318 \times 0.97 = 308.46 \approx 308 \text{ FP}$
>
> - **4. Result:**
>    $$\text{Final Functional Size} = 308.46 \approx 308 \text{ FP}$$
>
> - **5. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.1.2, printed pp. 145–148; Companion Slides 16–23. This is an authored practice problem, not a copied textbook example.

---

<div class="page-break"></div>

### Practice Problem 7.12. Compare Two Static Single-Variable Models

**A project size has been estimated to be 50,000 lines of code. Compare the development effort predicted by the Walston-Felix model and the SEL model.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Size $L = 50 \text{ KLOC}$
>
> - **2. Working & Computation:**
>    - **Walston-Felix Model ($E = 5.2 L^{0.91}$):**
>      $$E = 5.2 \times (50)^{0.91} \approx 182.84 \text{ Person-Months}$$
>    - **SEL Model ($E = 1.4 L^{0.93}$):**
>      $$E = 1.4 \times (50)^{0.93} \approx 53.23 \text{ Person-Months}$$
>
> - **3. Result:**
>    - Walston-Felix Effort = $182.84 \text{ PM}$
>    - SEL Effort = $53.23 \text{ PM}$
>    *(Variance ratio: Walston-Felix requires $3.43 \times$ more effort).*
>
> - **4. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.3.1, printed pp. 149–151; Companion Slides 31–38. This is an authored practice problem, not the textbook's Example 4.4.

---

<div class="page-break"></div>

### Practice Problem 7.13. Basic COCOMO Across Operating Modes

**A software system of size 40 KLOC is planned. Compute the effort and development time under Organic and Semidetached modes using the Basic COCOMO model.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Size $L = 40 \text{ KLOC}$
>
> - **2. Working & Computation:**
>    - **Organic Mode ($a=2.4, b=1.05, c=2.5, d=0.38$):**
>      $$E = 2.4 \times (40)^{1.05} \approx 115.44 \text{ Person-Months}$$
>      $$D = 2.5 \times (115.44)^{0.38} \approx 15.19 \text{ Months}$$
>    - **Semidetached Mode ($a=3.0, b=1.12, c=2.5, d=0.35$):**
>      $$E = 3.0 \times (40)^{1.12} \approx 186.82 \text{ Person-Months}$$
>      $$D = 2.5 \times (186.82)^{0.35} \approx 15.59 \text{ Months}$$
>
> - **3. Result:**
>    - Organic: $E = 115.44 \text{ PM}, \quad D = 15.19 \text{ Months}$
>    - Semidetached: $E = 186.82 \text{ PM}, \quad D = 15.59 \text{ Months}$
>
> - **4. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.4.1, printed pp. 152–155; Companion Slides 41–50. This is an authored practice problem, not the textbook's Example 4.6.

---

<div class="page-break"></div>

### Practice Problem 7.14. Intermediate COCOMO with Cost Drivers

**A 20 KLOC organic software project has cost driver ratings: High reliability (1.15), High product complexity (1.15), Low analyst capability (1.19), and Very High programming language experience (0.95). All other cost drivers are nominal. Calculate the adjusted effort.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Size = $20 \text{ KLOC}$, Mode = Organic ($a=3.2, b=1.05$)
>    - Drivers: $\text{RELY}=1.15, \text{CPLX}=1.15, \text{ACAP}=1.19, \text{LEXP}=0.95$
>
> - **2. Working & Computation:**
>    - Nominal Effort:
>      $$E_{\text{nom}} = 3.2 \times (20)^{1.05} \approx 74.34 \text{ Person-Months}$$
>    - Effort Adjustment Factor:
>      $$\text{EAF} = 1.15 \times 1.15 \times 1.19 \times 0.95 \approx 1.4951$$
>    - Adjusted Effort:
>      $$E = 74.34 \times 1.4951 \approx 111.15 \text{ Person-Months}$$
>
> - **3. Result:**
>    $$E = 111.15 \text{ Person-Months} \quad (\text{Nominal effort scaled up by } +49.5\%)$$
>
> - **4. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.4.2, printed pp. 156–158; Companion Slides 51–56. This is an authored practice problem, not the textbook's Example 4.7.

---

<div class="page-break"></div>

### Problem 7.15 (Example 4.12). Peak Manning and Team Build-Up Rate

**For a software project with total lifecycle effort $K = 95 \text{ Person-Years}$ and development time $t_d = 1.75 \text{ Years}$, calculate the peak manpower and average rate of team build-up.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Total Project Effort $K = 95 \text{ Person-Years}$
>    - Development Time $t_d = 1.75 \text{ Years}$
>
> - **2. Derivation of Peak Manning Formula:**
>    The Norden/Rayleigh manpower curve is defined as:
>    $$m(t) = 2 K a t \cdot e^{-a t^2}, \quad \text{where } a = \frac{1}{2 t_d^2}$$
>    Substituting $a$:
>    $$m(t) = \frac{K}{t_d^2} t \cdot e^{-t^2 / (2 t_d^2)}$$
>    To find the maximum, set $\frac{dm}{dt} = 0$:
>    $$\frac{dm}{dt} = \frac{K}{t_d^2} e^{-t^2 / (2 t_d^2)} \left[1 - \frac{t^2}{t_d^2}\right] = 0 \implies t = t_d$$
>    Evaluating at $t = t_d$:
>    $$m_0 = m(t_d) = \frac{K}{t_d^2} t_d \cdot e^{-t_d^2 / (2 t_d^2)} = \frac{K}{t_d} e^{-1/2} = \frac{K}{t_d \sqrt{e}}$$
>
> - **3. Numerical Computation:**
>    $$\sqrt{e} = \sqrt{2.71828} \approx 1.64872$$
>    $$m_0 = \frac{95}{1.75 \times 1.64872} = \frac{95}{2.88526} \approx 32.93 \text{ Persons} \approx 33 \text{ Persons}$$
>    $$\text{Average build-up rate} = \frac{m_0}{t_d} = \frac{32.93}{1.75} \approx 18.82 \text{ Persons/Year} \approx 1.57 \text{ Persons/Month}$$
>
> - **4. Result:**
>    $$m_0 \approx 33 \text{ Persons}, \quad \text{average build-up rate} \approx 18.8 \text{ Persons/Year}$$
>    *(The peak value is rounded to the nearest whole person.)*
>
> - **5. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.6.1, printed p. 184 (Example 4.12); Companion Slides 130, 132, 139.

---

<div class="page-break"></div>

### Practice Problem 7.16. Evaluate the Rayleigh Staffing Curve at Selected Times

**For a project with $K = 95 \text{ PY}$ and $t_d = 1.75 \text{ yr}$, calculate the instantaneous manpower staffing $m(t)$ at $t = 0.5 \text{ yr}$, $t = 1.0 \text{ yr}$, and $t = 2.5 \text{ yr}$.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Governing Equation:**
>    $$a = \frac{1}{2 (1.75)^2} = \frac{1}{6.125} \approx 0.16327 \text{ yr}^{-2}$$
>    $$m(t) = \frac{95}{(1.75)^2} t \cdot e^{-0.16327 t^2} = 31.02 t \cdot e^{-0.16327 t^2}$$
>
> - **2. Working & Computation:**
>    - At $t = 0.5 \text{ yr}$:
>      $$m(0.5) = 31.02 \times (0.5) \times e^{-0.16327 \times 0.25} = 15.51 \times e^{-0.0408} = 15.51 \times 0.9600 \approx 14.89 \text{ Persons}$$
>    - At $t = 1.0 \text{ yr}$:
>      $$m(1.0) = 31.02 \times (1.0) \times e^{-0.16327 \times 1.0} = 31.02 \times 0.8494 \approx 26.35 \text{ Persons}$$
>    - At $t = 2.5 \text{ yr}$:
>      $$m(2.5) = 31.02 \times (2.5) \times e^{-0.16327 \times 6.25} = 77.55 \times e^{-1.0204} = 77.55 \times 0.3604 \approx 27.95 \text{ Persons}$$
>
> - **3. Result:**
>    - $m(0.5) \approx 14.9 \text{ Persons}$
>    - $m(1.0) \approx 26.4 \text{ Persons}$
>    - $m(2.5) \approx 28.0 \text{ Persons}$
>
> - **4. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.6.1–§4.6.2, printed pp. 182–186; Companion Slides 128–141. This is an authored practice problem, not the textbook's Example 4.14.

---

<div class="page-break"></div>

### Practice Problem 7.17. Difficulty, Build-Up, and Productivity

**A software project requires $S = 50,000 \text{ LOC}$, developed in $t_d = 2 \text{ Years}$ with total effort $K = 40 \text{ Person-Years}$. Compute the difficulty metric $D$, manpower build-up metric $D_0$, and the project productivity ratio.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - $S = 50,000 \text{ LOC}, \quad K = 40 \text{ PY}, \quad t_d = 2 \text{ Years}$
>
> - **2. Working & Computation:**
>    - **Difficulty Metric ($D$):**
>      $$D = \frac{K}{t_d^2} = \frac{40}{(2)^2} = 10 \text{ Persons/Year}$$
>    - **Manpower Build-Up Metric ($D_0$):**
>      $$D_0 = \frac{K}{t_d^3} = \frac{40}{(2)^3} = 5 \text{ Persons/Year}^2$$
>    - **Overall Productivity ($P$):**
>      $$P = \frac{S}{K} = \frac{50,000 \text{ LOC}}{40 \text{ Person-Years}} = 1,250 \text{ LOC/Person-Year} \approx 104.2 \text{ LOC/PM}$$
>
> - **3. Result:**
>    $$D = 10 \text{ Persons/Year}, \quad D_0 = 5 \text{ Persons/Year}^2, \quad P = 1,250 \text{ LOC/PY}$$
>
> - **4. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), §§4.6.2–4.6.3, printed pp. 185–187; Companion Slides 136–148. This is an authored practice problem, not the textbook's Example 4.17.

---

<div class="page-break"></div>

### Practice Problem 7.18. Schedule Compression at Fixed Product Size

**A software system of size $S = 55,000 \text{ LOC}$ is developed using technology constant $C = 2200$. If the development schedule is compressed from $t_d = 2.0 \text{ Years}$ to $t_d = 1.6 \text{ Years}$ while keeping product size and technology constant, calculate the resulting increase in total effort $K$ and difficulty $D$.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Size $S = 55,000 \text{ LOC}$ (Fixed)
>    - Technology Constant $C = 2200$ (Fixed)
>    - Baseline Duration $t_{d1} = 2.0 \text{ Years}$
>    - Compressed Duration $t_{d2} = 1.6 \text{ Years}$ ($20\%$ compression)
>
> - **2. Governing Trade-off Equation ($K \cdot t_d^4 = \text{Constant}$):**
>    From Putnam's software equation:
>    $$S = C \cdot K^{1/3} t_d^{4/3} \implies K^{1/3} = \frac{S}{C \cdot t_d^{4/3}} \implies K = \left(\frac{S}{C}\right)^3 \frac{1}{t_d^4}$$
>    Constant factor:
>    $$\left(\frac{55,000}{2200}\right)^3 = (25)^3 = 15,625$$
>
> - **3. Working & Computation:**
>    - **Baseline Case ($t_{d1} = 2.0 \text{ yr}$):**
>      $$t_{d1}^4 = (2.0)^4 = 16$$
>      $$K_1 = \frac{15,625}{16} \approx 976.56 \text{ Person-Years}$$
>      $$D_1 = \frac{K_1}{t_{d1}^2} = \frac{976.56}{4} \approx 244.14 \text{ Persons/Year}$$
>    - **Compressed Case ($t_{d2} = 1.6 \text{ yr}$):**
>      $$t_{d2}^4 = (1.6)^4 = 6.5536$$
>      $$K_2 = \frac{15,625}{6.5536} \approx 2,384.18 \text{ Person-Years}$$
>      $$D_2 = \frac{K_2}{t_{d2}^2} = \frac{2,384.18}{(1.6)^2} = \frac{2,384.18}{2.56} \approx 931.32 \text{ Persons/Year}$$
>
> - **4. Result:**
>    - Effort increases from $976.6 \text{ PY}$ to $2,384.2 \text{ PY}$ ($\mathbf{+144.1\% \text{ increase}}$).
>    - Difficulty quadruples from $244.1$ to $931.3$ ($\mathbf{+281.5\% \text{ increase}}$).
>
> - **5. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.6.4, printed pp. 187–188; Companion Slides 149–150. This is an authored practice problem, not the textbook's Example 4.18.

---

<div class="page-break"></div>

### Practice Problem 7.19. Development Sub-Cycle Effort

**A project has full-project effort $K = 250 \text{ Person-Years}$ and development time $t_d = 3 \text{ Years}$. Using the chapter's sub-cycle relation, calculate $K_d$, the effort outside the development sub-cycle, and peak development staffing $m_{0d}$.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - $K = 250 \text{ Person-Years}, \quad t_d = 3 \text{ Years}$
>
> - **2. Working & Computation:**
>    - **Development Effort ($K_d$):**
>      $$K_d = K/6 = 250/6 \approx 41.67 \text{ Person-Years}$$
>    - **Effort outside the development sub-cycle:** $K-K_d=250-41.67=208.33$ PY.
>    - **Peak Development Staffing ($m_{0d}$):**
>      Using $t_{od}=t_d/\sqrt6\approx1.225$ yr and the development curve peak relation $m_{0d}=K_d/(t_{od}\sqrt e)$, $m_{0d}\approx20.63$ persons.
>
> - **3. Result:**
>    $$K_d \approx 41.67 \text{ PY}, \quad K-K_d \approx208.33 \text{ PY}, \quad m_{0d} \approx20.63 \text{ Persons}$$
>
> - **4. Source:**
>    K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.6.5, printed pp. 188–191; Companion Slides 151–165. This is an authored practice problem, not the textbook's Example 4.19.

---

<div class="page-break"></div>

### Problem 7.20 (Example 4.9). COCOMO II Application Composition

**A database application has four screens with four views each and seven data tables, and two reports with six sections each. Assume 10% object-point reuse. The developer's experience and ICASE maturity/capability are low. Calculate the new object points and estimated effort.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Screens: 4, each with 4 views.
>    - Reports: 2, each with 6 sections.
>    - Reuse: 10%.
>    - Low developer experience/capability: $\text{PROD}=7$ NOP/PM.
>
> - **2. Required:** New Object Points (NOP) and effort in person-months.
>
> - **3. Model and object-point count:** The source classifies the screens as medium complexity and reports as difficult. Using the source weights:
>    $$\text{OP}=(4\text{ medium screens}\times2)+(2\text{ difficult reports}\times8)=8+16=24$$
>    $$\text{NOP}=\text{OP}\times\frac{100-\%\text{reuse}}{100}=24\times\frac{90}{100}=21.6$$
>
> - **4. Effort:**
>    $$E=\frac{\text{NOP}}{\text{PROD}}=\frac{21.6}{7}=3.0857\text{ PM}$$
>
> - **5. Result:** $\text{NOP}=21.6$ and $E\approx3.09$ person-months.
>
> - **6. Source:** K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.5.1, printed pp. 166–167 (Example 4.9).

---

<div class="page-break"></div>

### Problem 7.21 (Example 4.10). COCOMO II Early Design Effort

**A 50-KLOC application-generator project has low precedentness, high development flexibility, and low team cohesion. All remaining scale factors are nominal. The Early Design cost drivers are PDIF = high (1.29), PERS = high (0.83), and all other drivers nominal. Calculate the scale exponent, nominal effort, and adjusted effort.**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:**
>    - Size $=50$ KLOC; nominal productivity constant $A=2.5$.
>    - Scale-factor ratings: $4.96, 2.03, 4.24, 4.38, 4.68$.
>    - Non-nominal effort multipliers: PDIF $=1.29$, PERS $=0.83$; remaining five Early Design multipliers $=1.0$.
>
> - **2. Required:** $B$, nominal effort, and effort after cost-driver adjustment.
>
> - **3. Scale exponent and nominal effort:**
>    $$B=0.91+0.01\sum_{j=1}^{5}SF_j=0.91+0.01(20.29)=1.1129$$
>    $$E_{nom}=A(\text{Size})^B=2.5(50)^{1.1129}\approx194.41\text{ PM}$$
>
> - **4. Adjusted effort:**
>    $$\text{EAF}=1.29\times0.83\times1^5=1.0707$$
>    $$E=E_{nom}\times\text{EAF}=194.4122947\times1.0707\approx208.16\text{ PM}$$
>
> - **5. Result:** $B=1.1129$, $E_{nom}\approx194.41$ PM, and $E\approx208.16$ PM (rounding from unrounded intermediate values).
>
> - **6. Source:** K.K. Aggarwal & Yogesh Singh (3rd ed.), §4.5.2, printed pp. 172–173 (Example 4.10).

---

<div class="page-break"></div>

### Problem 7.22 (Example 4.17). Putnam Software Size from Development Effort

**What amount of software can be delivered in 1 year 10 months when the technology factor is 2400 and the permitted development-sub-cycle effort is 25 person-years?**
{: .keep-next }

> **Step-by-Step Mathematical Solution:**
>
> - **1. Given:** $t_d=1\text{ year }10\text{ months}=1.8\text{ years}$, $C=2400$, and $K_d=25$ person-years.
>
> - **2. Required:** Software size $S$ in LOC.
>
> - **3. Model and relation:** The Putnam software equation uses full-project effort $K$, while the stated effort is for the development sub-cycle: $K=6K_d=150$ person-years.
>
> - **4. Equation:**
>    $$S=C K^{1/3}t_d^{4/3}$$
>
> - **5. Substitution:**
>    $$S=2400(150)^{1/3}(1.8)^{4/3}\approx27{,}921\text{ LOC}$$
>
> - **6. Result:** Approximately $27{,}920$ LOC (about $27.9$ KLOC).
>
> - **7. Check:** The independently calculated value is about $27{,}921$ LOC, which rounds to approximately $27{,}920$ LOC at the precision used in the worked example.
>
> - **8. Source:** K.K. Aggarwal & Yogesh Singh (3rd ed.), printed p. 191 (Example 4.17), equations (4.33)–(4.34).

---

<div class="page-break"></div>

## Topic-to-Question Map

| Topic Area | Problems Covering Item | Primary Course Sources | Key Formulas & Numerical Models |
|:---|:---|:---|:---|
| **1. Function Point Analysis (FPA)** | P7.1 (Exercise 4.5); P7.2–P7.3 (Exercises 4.10–4.11); P7.11 (authored practice) | K.K. Aggarwal pp. 145–148; Slides 9–30 | $\text{UFP} = \sum W_{ij} Z_{ij}$, $\text{CAF} = 0.65 + 0.01 \sum F_i$, $\text{FP} = \text{UFP} \times \text{CAF}$. |
| **2. Static Single-Variable Models** | P7.4–P7.5 (Exercises 4.13–4.14); P7.12 (authored practice) | K.K. Aggarwal pp. 149–152; Slides 31–40 | Walston-Felix ($E=5.2 L^{0.91}$), SEL ($E=1.4 L^{0.93}$), conditional size and LOC/PM calculations. |
| **3. Basic COCOMO '81** | P7.6 (Exercise 4.16); P7.8 (Exercise 4.21); P7.13 (authored practice) | K.K. Aggarwal pp. 152–156; Slides 41–50 | Organic ($2.4 L^{1.05}$), Semidetached ($3.0 L^{1.12}$), Embedded ($3.6 L^{1.20}$). |
| **4. Intermediate/Detailed COCOMO '81** | P7.7 (Exercise 4.20); P7.14 (authored practice); detailed phase concepts in T2/T3 | K.K. Aggarwal pp. 156–161; Slides 51–65 | Nominal effort $a_i L^{b_i}$, $\text{EAF} = \prod EM_j$, phase-sensitive multipliers, Table 4.7 distribution. |
| **5. COCOMO II** | P7.9 (Exercise 4.25, Post-Architecture); P7.20 (Example 4.9, Application Composition); P7.21 (Example 4.10, Early Design) | K.K. Aggarwal pp. 162–173; Slides 73–120 | Object Points/NOP; Early Design and Post-Architecture scale factors, effort multipliers. |
| **6. Putnam Resource Model & Curves** | P7.10 (Exercise 4.29); P7.15 (Example 4.12); P7.16–P7.19 (authored practice); P7.22 (Example 4.17) | K.K. Aggarwal printed pp. 182–191, 202; Slides 123–166, 206 | $S = C K^{1/3} t_d^{4/3}$; $D=K/t_d^2$; $D_0=K/t_d^3$; $m_0=K/(t_d\sqrt e)$; $K t_d^4=\mathrm{constant}$; $K=6K_d$. |

---

<!--
## Retrieval Set & Active Recall Self-Test

Use the quantitative problems in this pack for active recall:
-->
1. Re-derive the Putnam Rayleigh peak staffing formula $m_0 = \frac{K}{t_d \sqrt{e}}$ from the derivative $\frac{dm}{dt} = 0$.
2. State the exact average complexity weights for Albrecht's 5 information domain characteristics from memory.
3. Calculate the percentage increase in effort $K$ when project schedule $t_d$ is compressed by $20\%$ using Putnam's fourth-power trade-off ($K \propto t_d^{-4}$).
4. Solve for code size $L$ given $E = 100 \text{ PM}$ under both the Walston-Felix and SEL models.
5. Reconstruct the COCOMO II exponent formula $B = 0.91 + 0.01 \sum SF_j$ and identify the 5 scale factors.
