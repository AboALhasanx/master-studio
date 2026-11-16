# Advanced Software Engineering — Chapter 9: Software Maintenance
## T7: Calculations & Quantitative Models

### Q9.C1 (Exercise 9.18): Belady-Lehman Maintenance Effort Estimation

**Question:**
Assume that the effort for development of a software system is $P = 600\text{ PM}$. Calculate the maintenance effort using the **Belady and Lehman model** if complexity $c = 7$, degree of familiarity $d = 0.7$, and empirical constant $K = 0.5$.

**Solution:**

- **1. Given Data:**
  - Initial development effort ($P$): $600\text{ PM}$
  - Software complexity rating ($c$): $7$
  - Degree of familiarity ($d$): $0.7$
  - Empirical calibration constant ($K$): $0.5$

- **2. Required:**
  - Total maintenance effort ($M$) in person-months ($\text{PM}$).

- **3. Model & Assumptions:**
  - **Model:** Belady and Lehman empirical maintenance effort model (1972).
  - **Assumptions:** Maintenance effort grows exponentially with system complexity ($c$) and decreases as development familiarity/documentation quality ($d$) increases. The base development effort ($P$) represents foundational architectural mass.

- **4. Governing Equation:**
  $$M = P + K \cdot e^{c - d}$$

- **5. Step-by-Step Substitution & Calculation:**
  - Calculate net exponent:
    $$c - d = 7 - 0.7 = 6.3$$
  - Calculate exponential term:
    $$e^{6.3} \approx 544.5719$$
  - Multiply by empirical constant $K$:
    $$K \cdot e^{c - d} = 0.5 \times 544.5719 = 272.2859\text{ PM}$$
  - Add initial development effort $P$:
    $$M = 600 + 272.2859 = 872.2859\text{ PM}$$

- **6. Final Result:**
  - **Estimated Maintenance Effort ($M$):** **$872.29\text{ PM}$** (or $872.3\text{ PM}$).

- **7. Sanity Check & Architectural Interpretation:**
  - **Effort Ratio:** Maintenance effort adds $272.29\text{ PM}$ to the initial $600\text{ PM}$ base, representing a $45.4\%$ increase over initial development.
  - **Dimensional Consistency:** All terms are expressed in person-months ($\text{PM}$).
  - **Behavioral Validity:** Because $c > d$ ($7 > 0.7$), complexity dominates lack of familiarity, driving positive exponential growth in maintenance overhead.

<!-- PRINT-HIDDEN ACADEMIC NOTE (verbatim content retained in Markdown):
> [!NOTE]
> **ملاحظة امتحانية:** يعتمد نموذج (Belady & Lehman) على قياس التعقيد الفعلي مقابل درجة الألفة والتوثيق. القيمة الأسية الموجبة الكبيرة $(c - d = 6.3)$ تعكس أن صيانة نظام معقد بتوثيق متوسط تستهلك جهداً إضافياً كبيراً يتجاوز $45\%$ من تكلفة التطوير الأصلية.
-->

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, Exercise 9.18, p. 491; Slides 24–25.

---

### Q9.C2 (Example 9.1): Sensitivity Analysis of Familiarity ($d$) in Belady-Lehman Model

**Question:**
Assume that the effort for development of a software is $P = 500\text{ PM}$, complexity $c = 8$, and constant $K = 0.3$. Perform a sensitivity analysis by calculating the maintenance effort $M$ for two contrasting scenarios:
1. When the degree of familiarity is high: $d = 0.9$ (well-structured, fully documented system maintained by the original team).
2. When the degree of familiarity is low: $d = 0.1$ (poorly documented legacy system maintained by a novice team).
Compare the results and state the architectural implication.

**Solution:**

- **1. Given Data:**
  - Initial development effort ($P$): $500\text{ PM}$
  - System complexity ($c$): $8$
  - Constant ($K$): $0.3$
  - Scenario 1 familiarity ($d_1$): $0.9$
  - Scenario 2 familiarity ($d_2$): $0.1$

- **2. Required:**
  - Maintenance effort for Scenario 1 ($M_1$).
  - Maintenance effort for Scenario 2 ($M_2$).
  - Quantitative comparison and architectural deduction.

- **3. Model & Assumptions:**
  - Belady-Lehman equation: $M = P + K \cdot e^{c - d}$.
  - System complexity ($c$) and initial development mass ($P$) remain constant; only team familiarity and document intelligibility ($d$) vary.

- **4. Governing Equation:**
  $$M = P + K \cdot e^{c - d}$$

- **5. Step-by-Step Substitution & Calculation:**
  - **Scenario 1 ($d = 0.9$ — High Familiarity):**
    $$c - d_1 = 8 - 0.9 = 7.1$$
    $$e^{7.1} \approx 1211.967$$
    $$M_1 = 500 + 0.3 \times 1211.967 = 500 + 363.59 = 863.59\text{ PM}$$
  - **Scenario 2 ($d = 0.1$ — Low Familiarity):**
    $$c - d_2 = 8 - 0.1 = 7.9$$
    $$e^{7.9} \approx 2697.282$$
    $$M_2 = 500 + 0.3 \times 2697.282 = 500 + 809.18 = 1309.18\text{ PM}$$
  - **Variance Calculation:**
    $$\Delta M = M_2 - M_1 = 1309.18 - 863.59 = 445.59\text{ PM}$$
    $$\text{Ratio of Maintenance Overhead} = \frac{809.18\text{ PM}}{363.59\text{ PM}} \approx 2.23$$
    $$\text{Percentage Increase in Maintenance Overhead} = \frac{809.18 - 363.59}{363.59} \times 100\% \approx 122.55\%$$
    $$\text{Percentage Increase in Total Effort} = \frac{1309.18 - 863.59}{863.59} \times 100\% \approx 51.60\%$$

- **6. Final Result:**
  - **High Familiarity Effort ($M_1$):** **$863.59\text{ PM}$**
  - **Low Familiarity Effort ($M_2$):** **$1309.18\text{ PM}$**
  - **Overhead Growth Factor:** **$2.23\times$** (an increase of $+122.55\%$ in maintenance overhead, $+445.59\text{ PM}$)

- **7. Sanity Check & Architectural Interpretation:**
  - **Exponential Penalty:** A drop of $0.8$ in the familiarity index ($0.9 \to 0.1$) multiplies the maintenance overhead by $2.23$ times ($363.59\text{ PM} \to 809.18\text{ PM}$).
  - **Architectural Takeaway:** High-quality documentation, clean modular architectures, and structured knowledge transfer are quantitatively proven to save hundreds of person-months during system evolution.

<!-- PRINT-HIDDEN ACADEMIC NOTE (verbatim content retained in Markdown):
> [!NOTE]
> **الاستنتاج الهندسي:** انخفاض مؤشر الألفة والفهم $(d)$ من $0.9$ إلى $0.1$ يضاعف الجهد الإضافي للصيانة بنحو $2.23$ مرة (زيادة بنسبة $122.5\%$)، مما يثبت رياضياً أن إهمال التوثيق والمعايير الهندسية يفرض ضريبة أسية باهظة في مرحلة الصيانة.
-->

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, Example 9.1, p. 471; Slide 26.

---

### Q9.C3 (Example 9.2): Boehm Annual Maintenance Effort (AME) and 10-Year Life-Cycle Total

**Question:**
Assume that the initial development effort for a software system is $SDE = 600\text{ PM}$. If the Annual Change Traffic is $ACT = 15\%$, calculate:
1. The Annual Maintenance Effort ($AME$).
2. The total maintenance effort over an anticipated operational lifetime of $10\text{ years}$.
3. The total life-cycle effort (development plus maintenance).

**Solution:**

- **1. Given Data:**
  - Software Development Effort ($SDE$): $600\text{ PM}$
  - Annual Change Traffic ($ACT$): $15\% = 0.15$
  - Operational Lifetime ($L$): $10\text{ years}$

- **2. Required:**
  - Annual Maintenance Effort ($AME$).
  - Cumulative $10\text{-year}$ Maintenance Effort ($M_{10}$).
  - Total Life-Cycle Effort ($E_{\text{total}}$).

- **3. Model & Assumptions:**
  - **Model:** Boehm COCOMO Maintenance Effort Model without cost-driver adjustments ($EAF = 1.0$).
  - **Assumptions:** The Annual Change Traffic remains steady at $15\%$ per annum over the entire $10\text{-year}$ operational life.

- **4. Governing Equations:**
  $$AME = ACT \times SDE$$
  $$M_{10} = L \times AME$$
  $$E_{\text{total}} = SDE + M_{10}$$

- **5. Step-by-Step Substitution & Calculation:**
  - Calculate Annual Maintenance Effort ($AME$):
    $$AME = 0.15 \times 600 = 90\text{ PM/year}$$
  - Calculate Cumulative $10\text{-year}$ Maintenance Effort ($M_{10}$):
    $$M_{10} = 10 \times 90 = 900\text{ PM}$$
  - Calculate Total Life-Cycle Effort ($E_{\text{total}}$):
    $$E_{\text{total}} = 600 + 900 = 1500\text{ PM}$$

- **6. Final Result:**
  - **Annual Maintenance Effort ($AME$):** **$90\text{ PM/year}$**
  - **$10\text{-Year}$ Maintenance Effort ($M_{10}$):** **$900\text{ PM}$**
  - **Total Life-Cycle Effort ($E_{\text{total}}$):** **$1500\text{ PM}$**

- **7. Sanity Check & Architectural Interpretation:**
  - **Maintenance Share:** Maintenance represents $\frac{900}{1500} = 60.0\%$ of the total life-cycle effort, validating Boehm's classical observation that long-term maintenance costs routinely exceed original construction costs.
  - **Slide Discrepancy Note:** Companion Slide 28 contains an arithmetic printing error stating $10 \times 90 = 90\text{ PM}$. The scanned textbook at printed page 472 gives the correct verified arithmetic: $10 \times 90 = 900\text{ PM}$ and $600 + 900 = 1500\text{ PM}$.

<!-- PRINT-HIDDEN ACADEMIC NOTE (verbatim content retained in Markdown):
> [!NOTE]
> **تنبيه حول خطأ مطبعي في السلايدات:** شريحة المحاضرة (Slide 28) تحتوي خطأً مطبعياً يكتب $10 \times 90 = 90\text{ PM}$! الحساب الصحيح المعتمد في الكتاب المطبوع ص 472 هو $10 \times 90 = 900\text{ PM}$، والمجموع الكلي لدورة الحياة هو $600 + 900 = 1500\text{ PM}$.
-->

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, Example 9.2, p. 472; Slide 28.

---

### Q9.C4 (Example 9.3): Boehm Maintenance Effort Adjusted by Cost Drivers (EAF)

**Question:**
A software development project required $SDE = 500\text{ PM}$. The annual change traffic is estimated at $ACT = 10\%$. Due to stringent operating conditions, the maintenance phase is evaluated with the following COCOMO cost driver ratings:
- Required Software Reliability ($RELY$): High ($1.15$)
- Database Size ($DATA$): High ($1.08$)
- Analyst Capability ($ACAP$): High ($0.86$)
- Applications Experience ($AEXP$): **Very High** ($0.82$)
- Programming Language Experience ($LEXP$): High ($0.95$)
- All other cost drivers: Nominal ($1.00$)
Calculate the composite Effort Adjustment Factor ($EAF$) and the adjusted Annual Maintenance Effort ($AME$).

**Solution:**

- **1. Given Data:**
  - Software Development Effort ($SDE$): $500\text{ PM}$
  - Annual Change Traffic ($ACT$): $10\% = 0.10$
  - Multipliers: $RELY = 1.15$ (High), $DATA = 1.08$ (High), $ACAP = 0.86$ (High), $AEXP = 0.82$ (**Very High**), $LEXP = 0.95$ (High)

- **2. Required:**
  - Composite Effort Adjustment Factor ($EAF$).
  - Adjusted Annual Maintenance Effort ($AME$).

- **3. Model & Assumptions:**
  - **Model:** Boehm COCOMO Detailed Maintenance Model.
  - **Assumptions:** Cost drivers apply multiplicatively to determine the net environmental productivity multiplier ($EAF$).

- **4. Governing Equations:**
  $$EAF = \prod_{i=1}^{n} \text{Multiplier}_i$$
  $$AME = ACT \times SDE \times EAF$$

- **5. Step-by-Step Substitution & Calculation:**
  - Calculate product of non-nominal cost drivers:
    $$EAF = 1.15 \times 1.08 \times 0.86 \times 0.82 \times 0.95$$
    $$1.15 \times 1.08 = 1.242$$
    $$1.242 \times 0.86 = 1.06812$$
    $$1.06812 \times 0.82 = 0.875858$$
    $$0.875858 \times 0.95 = 0.832065 \approx 0.832$$
  - Calculate unadjusted annual maintenance effort:
    $$AME_{\text{nominal}} = 0.10 \times 500 = 50\text{ PM}$$
  - Calculate adjusted Annual Maintenance Effort ($AME$):
    $$AME = 50 \times 0.832 = 41.6\text{ PM}$$

- **6. Final Result:**
  - **Effort Adjustment Factor ($EAF$):** **$0.832$**
  - **Adjusted Annual Maintenance Effort ($AME$):** **$41.6\text{ PM/year}$**

- **7. Sanity Check & Architectural Interpretation:**
  - **Productivity Gain:** Because high staff capabilities ($ACAP=0.86$, $AEXP=0.82$ Very High) more than compensate for high product constraints ($RELY=1.15$, $DATA=1.08$), the composite multiplier is below unity ($0.832 < 1.0$), resulting in a net $16.8\%$ reduction in annual maintenance effort (saving $8.4\text{ PM/year}$).

<!-- PRINT-HIDDEN ACADEMIC NOTE (verbatim content retained in Markdown):
> [!NOTE]
> **التحليل الهندسي:** على الرغم من أن متطلبات الاعتمادية العالية وحجم البيانات ترفع الجهد المطلوب، إلا أن كفاءة المحللين وخبرتهم العالية جداً بالتطبيق ($AEXP=0.82$) خفضت معامل الجهد الإجمالي إلى $0.832$، مما وفر $8.4$ شخص/شهر سنوياً.
-->

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, Example 9.3, pp. 472–473; Slide 29.

---

### Q9.C5 (Exercise 9.19): 10-Year Life-Cycle Financial Cost Estimation

**Question:**
A software system was developed at an initial expenditure of $20\text{ lacs}$. If the Annual Change Traffic ($ACT$) is determined to be $25\%$, calculate:
1. The Annual Maintenance Cost ($AMC$).
2. The cumulative maintenance cost over an estimated operational lifespan of $10\text{ years}$.
3. The total life-cycle expenditure of the software system.
State what percentage of the total life-cycle budget is consumed by post-delivery maintenance.

**Solution:**

- **1. Given Data:**
  - Initial Development Cost ($C_{\text{dev}}$): $20\text{ lacs}$ ($2,000,000$ currency units)
  - Annual Change Traffic ($ACT$): $25\% = 0.25$
  - Operational Lifespan ($L$): $10\text{ years}$

- **2. Required:**
  - Annual Maintenance Cost ($AMC$).
  - Cumulative $10\text{-Year}$ Maintenance Cost ($C_{\text{maint}}$).
  - Total Life-Cycle Cost ($C_{\text{total}}$).
  - Percentage of total cost allocated to maintenance.

- **3. Model & Assumptions:**
  - **Model:** Linear Annual Change Traffic Cost Model.
  - **Assumptions:** Annual maintenance expenditure is directly proportional to the original capital development budget scaled by annual change volume. Constant monetary baseline (inflation neutral).

- **4. Governing Equations:**
  $$AMC = ACT \times C_{\text{dev}}$$
  $$C_{\text{maint}} = L \times AMC$$
  $$C_{\text{total}} = C_{\text{dev}} + C_{\text{maint}}$$
  $$\%\text{ Maintenance} = \left( \frac{C_{\text{maint}}}{C_{\text{total}}} \right) \times 100\%$$

- **5. Step-by-Step Substitution & Calculation:**
  - Calculate Annual Maintenance Cost ($AMC$):
    $$AMC = 0.25 \times 20 = 5\text{ lacs/year}$$
  - Calculate $10\text{-Year}$ Maintenance Cost ($C_{\text{maint}}$):
    $$C_{\text{maint}} = 10 \times 5 = 50\text{ lacs}$$
  - Calculate Total Life-Cycle Expenditure ($C_{\text{total}}$):
    $$C_{\text{total}} = 20 + 50 = 70\text{ lacs}$$
  - Calculate Maintenance Share:
    $$\%\text{ Maintenance} = \left( \frac{50}{70} \right) \times 100\% \approx 71.43\%$$

- **6. Final Result:**
  - **Annual Maintenance Cost ($AMC$):** **$5\text{ lacs/year}$**
  - **$10\text{-Year}$ Maintenance Expenditure:** **$50\text{ lacs}$**
  - **Total Life-Cycle Cost:** **$70\text{ lacs}$**
  - **Maintenance Budget Fraction:** **$71.43\%$**

- **7. Sanity Check & Architectural Interpretation:**
  - **Budget Dominance:** Over a 10-year period at $25\%$ change volume, maintenance costs are $2.5\text{ times}$ the original capital development investment ($50\text{ lacs}$ vs $20\text{ lacs}$).
  - **Empirical Confirmation:** Consuming $71.4\%$ of the total life-cycle budget matches industry empirical data where maintenance accounts for $60\% - 80\%$ of software total cost of ownership (TCO).

<!-- PRINT-HIDDEN ACADEMIC NOTE (verbatim content retained in Markdown):
> [!NOTE]
> **خلاصة اقتصاديات البرمجيات:** تُظهر هذه المسألة بوضوح أن تكلفة الصيانة على مدار 10 سنوات تبلغ ضعفين ونصف من كلفة التطوير الأصلية ($50$ لاك مقابل $20$ لاك)، وتمثل أكثر من $71\%$ من إجمالي ميزانية دورة الحياة.
-->

**Source:** Aggarwal & Singh, *Software Engineering* (3rd Ed.), Chapter 9, Exercise 9.19, p. 491; Slides 27–28.

---

<!-- The following retrieval set provides active recall verification for quantitative formulas -->
## Retrieval Set & Active Recall Self-Test

1. In the Belady-Lehman model $M = P + K \cdot e^{c - d}$, state what each parameter ($P, K, c, d$) represents and explain why maintenance effort grows exponentially rather than linearly.
2. Based on the sensitivity analysis in Example 9.1, what is the exact factor of increase in maintenance overhead when familiarity drops from $d = 0.9$ to $d = 0.1$, and what is the architectural takeaway?
3. In Boehm's baseline maintenance model $AME = ACT \times SDE$, how is Annual Change Traffic ($ACT$) defined, and what does an $ACT = 15\%$ indicate?
4. Explain the companion slide discrepancy in Example 9.2: why is $10 \times 90 = 900\text{ PM}$ the verified textbook calculation, and what was the typographical error on Slide 28?
5. In Example 9.3, why is $AEXP = 0.82$ classified as Very High, and how did superior personnel attributes mathematically compensate for product constraints in the composite $EAF$?
