---
title: "ASE Chapter 7 — T7 Software Reliability Calculations Pack"
course: "Advanced Software Engineering (CS603)"
---

# ASE Chapter 7 — T7 Software Reliability Calculations Pack

<!--
Course: Advanced Software Engineering (CS603) — Asst. Prof. Dr. Ali Fahim Ni'ma
Source material and solution-format metadata retained for editing, not printing.
-->

---

### Problem 7.1 · Basic Execution Time Model — Current Failure Intensity Evaluation

Assume that the initial failure intensity is $\lambda_0 = 10 \text{ failures/CPU hr}$ and the total number of failures expected over infinite time is $v_0 = 100 \text{ failures}$.

**1.** Calculate the failure intensity after 10 failures have been experienced.

**2.** Calculate the failure intensity after 50 failures have been experienced.

1. **Given:**
    - Initial failure intensity: $\lambda_0 = 10 \text{ failures/CPU hr}$
    - Total expected failures: $v_0 = 100 \text{ failures}$
    - Failure counts experienced: $\mu_1 = 10 \text{ failures}$, $\mu_2 = 50 \text{ failures}$

2. **Required:**
    - Failure intensity $\lambda(10)$ in $\text{failures/CPU hr}$.
    - Failure intensity $\lambda(50)$ in $\text{failures/CPU hr}$.

3. **Model & Assumptions:**
    - **Musa Basic Execution Time Model.**
    - The model assumes a finite expected failure count and a linear reduction in failure intensity as failures are experienced.

4. **Equation:**
   $$\lambda(\mu) = \lambda_0 \left(1 - \frac{\mu}{v_0}\right)$$

5. **Substitution & Working:**
    - For $\mu_1 = 10 \text{ failures}$:
     $$\lambda(10) = 10 \times \left(1 - \frac{10}{100}\right) = 10 \times (1 - 0.10) = 10 \times 0.90 = 9.0 \text{ failures/CPU hr}$$
    - For $\mu_2 = 50 \text{ failures}$:
     $$\lambda(50) = 10 \times \left(1 - \frac{50}{100}\right) = 10 \times (1 - 0.50) = 10 \times 0.50 = 5.0 \text{ failures/CPU hr}$$

6. **Result:**
    - $\lambda(10) = 9.0 \text{ failures/CPU hr}$
    - $\lambda(50) = 5.0 \text{ failures/CPU hr}$

7. **Check / Interpretation:** When $\mu = 0$, $\lambda = 10 \text{ failures/CPU hr}$ ($\lambda_0$). When half the faults are removed ($\mu = 50 = v_0 / 2$), the failure intensity drops by exactly half to $5.0 \text{ failures/CPU hr}$, verifying the strictly linear property of the Basic Execution Time Model.

**Source:**
Aggarwal & Singh (3rd ed.), §7.3.1, Example 7.1, p. 334; companion slides 47–54.

---

### Problem 7.2 · Failure Intensity from Decay Parameter (Exercise 7.16)

Assume that the initial failure intensity is $\lambda_0 = 6 \text{ failures/CPU hr}$. The failure intensity decay parameter is $\theta = 0.02/\text{failure}$. We assume that 45 failures have been experienced. Calculate the current failure intensity.

1. **Given:**
    - Initial failure intensity: $\lambda_0 = 6 \text{ failures/CPU hr}$
    - Failure intensity decay parameter: $\theta = 0.02/\text{failure}$
    - Failures experienced: $\mu = 45 \text{ failures}$

2. **Required:**
    - Current failure intensity $\lambda(45)$ in $\text{failures/CPU hr}$.

3. **Model & Assumptions:**
    - **Logarithmic Poisson Execution Time Model (Musa–Okumoto).**
        - The decay parameter $\theta$ defines the exponential reduction in failure intensity per failure experienced.

4. **Equation (Logarithmic Poisson Model):**
   $$\lambda(\mu) = \lambda_0 \exp(-\theta \mu)$$

5. **Substitution & Working:**
   $$\lambda(45) = 6 \times \exp(-0.02 \times 45) = 6 \times \exp(-0.90)$$
   Since $\exp(-0.90) \approx 0.40656966$:
   $$\lambda(45) = 6 \times 0.40656966 \approx 2.4394 \text{ failures/CPU hr}$$

6. **Result:**
    - $\lambda(45) \approx 2.44 \text{ failures/CPU hr}$.

7. **Check / Interpretation:**
    - Because earlier failures have a greater impact on reducing failure intensity in the logarithmic model than later ones, 45 failures reduce intensity from 6 down to $\approx 2.44$, which represents a $\approx 59.3\%$ reduction.

**Source:**
Aggarwal & Singh (3rd ed.), Exercise 7.16, p. 363; companion slide 122.

---

### Problem 7.3 · Multi-Stage Basic Execution Time Evaluation (Exercise 7.18)

Assume that a program will experience 150 failures in infinite time. It has now experienced 80 failures. The initial failure intensity was 10 failures/CPU hr.

**1.** Determine the current failure intensity.

**2.** Calculate the failures experienced and failure intensity after 25 and 40 CPU hrs of execution from time zero.

**3.** Compute additional failures and additional execution time required to reach the failure intensity objective of 2 failures/CPU hr from the current state.

1. **Given:**
    - Total failures over infinite time: $v_0 = 150 \text{ failures}$
    - Initial failure intensity: $\lambda_0 = 10 \text{ failures/CPU hr}$
    - Failures experienced currently: $\mu_P = 80 \text{ failures}$
    - Evaluation execution times: $\tau_1 = 25 \text{ CPU hrs}$, $\tau_2 = 40 \text{ CPU hrs}$
    - Target failure intensity objective: $\lambda_F = 2 \text{ failures/CPU hr}$

2. **Required:**
    - (i) Current failure intensity $\lambda_P$.
    - (ii) Failures experienced $\mu(25)$, $\mu(40)$ and failure intensity $\lambda(25)$, $\lambda(40)$.
    - (iii) Additional failures $\Delta \mu$ and additional execution time $\Delta \tau$ to reach $\lambda_F = 2 \text{ failures/CPU hr}$.

3. **Model & Assumptions:**
    - **Musa Basic Execution Time Model.**
    - All relations express failures experienced $\mu$ and failure intensity $\lambda$ as functions of execution time $\tau$.

4. **Equations:**
    - Current intensity from experienced failures:
     $$\lambda(\mu) = \lambda_0 \left(1 - \frac{\mu}{v_0}\right)$$
    - Intensity and failures as functions of execution time $\tau$:
     $$\lambda(\tau) = \lambda_0 \exp\left(-\frac{\lambda_0}{v_0}\tau\right)$$
     $$\mu(\tau) = v_0 \left[1 - \exp\left(-\frac{\lambda_0}{v_0}\tau\right)\right]$$
    - Increments between present state ($\lambda_P$) and target objective ($\lambda_F$):
     $$\Delta \mu = \frac{v_0}{\lambda_0}(\lambda_P - \lambda_F)$$
     $$\Delta \tau = \frac{v_0}{\lambda_0} \ln\left(\frac{\lambda_P}{\lambda_F}\right)$$

5. **Substitution & Working:**
    - **Part (i): Current failure intensity:**
     $$\lambda_P = 10 \times \left(1 - \frac{80}{150}\right) = 10 \times \left(1 - \frac{8}{15}\right) = 10 \times \frac{7}{15} = \frac{70}{15} \approx 4.6667 \approx 4.67 \text{ failures/CPU hr}$$
    - **Part (ii): Values at $\tau = 25$ and $\tau = 40$ CPU hrs:**
     Ratio $\frac{\lambda_0}{v_0} = \frac{10}{150} = \frac{1}{15} \approx 0.066667 \text{ hr}^{-1}$.
        - At $\tau = 25 \text{ CPU hrs}$:
       $$\frac{\lambda_0}{v_0} \tau = \frac{25}{15} = \frac{5}{3} \approx 1.66667$$
       $$\lambda(25) = 10 \times \exp\left(-\frac{5}{3}\right) \approx 10 \times 0.188876 = 1.8888 \approx 1.89 \text{ failures/CPU hr}$$
       $$\mu(25) = 150 \times \left[1 - \exp\left(-\frac{5}{3}\right)\right] = 150 \times (1 - 0.188876) = 150 \times 0.811124 = 121.669 \approx 121.67 \text{ failures}$$
        - At $\tau = 40 \text{ CPU hrs}$:
       $$\frac{\lambda_0}{v_0} \tau = \frac{40}{15} = \frac{8}{3} \approx 2.66667$$
       $$\lambda(40) = 10 \times \exp\left(-\frac{8}{3}\right) \approx 10 \times 0.069483 = 0.6948 \approx 0.69 \text{ failures/CPU hr}$$
       $$\mu(40) = 150 \times \left[1 - \exp\left(-\frac{8}{3}\right)\right] = 150 \times (1 - 0.069483) = 150 \times 0.930517 = 139.578 \approx 139.58 \text{ failures}$$
    - **Part (iii): Additional failures and execution time to reach $\lambda_F = 2 \text{ failures/CPU hr}$:**
        - Using current state $\lambda_P = \frac{70}{15} \approx 4.6667 \text{ failures/CPU hr}$ and $\mu_P = 80$:
       $$\Delta \mu = \frac{150}{10} \times \left(\frac{70}{15} - 2\right) = 15 \times \left(\frac{40}{15}\right) = 40 \text{ failures}$$
       *(Direct cross-check: Target failures $\mu_F = 150 \times (1 - 2/10) = 150 \times 0.8 = 120$; $\Delta \mu = 120 - 80 = 40$ failures).*
        - **Additional execution time:** $\Delta \tau = \frac{150}{10} \times \ln\left(\frac{4.6667}{2}\right) = 15 \times \ln(2.33333) = 15 \times 0.847298 \approx 12.7095 \approx 12.71 \text{ CPU hrs}$

6. **Result:**
    - (i) $\lambda_P \approx 4.67 \text{ failures/CPU hr}$
    - (ii) At $\tau = 25$: $\lambda(25) \approx 1.89 \text{ failures/CPU hr}$, $\mu(25) \approx 121.67 \text{ failures}$;  
     At $\tau = 40$: $\lambda(40) \approx 0.69 \text{ failures/CPU hr}$, $\mu(40) \approx 139.58 \text{ failures}$.
    - (iii) $\Delta \mu = 40 \text{ failures}$, $\Delta \tau \approx 12.71 \text{ CPU hrs}$.

<div class="no-break" markdown="1">

**7. Check / Interpretation:** Target intensity $2 \text{ failures/CPU hr}$ is reached at total execution time $\tau_F = 15\ln(10/2) \approx 24.14$ CPU hours. The current state ($\mu_P=80$, $\lambda_P=70/15$) occurs at $\tau_P=15\ln(10/(70/15)) \approx 11.43$ CPU hours, so the additional time is $\Delta\tau=\tau_F-\tau_P\approx12.71$ CPU hours, consistent with the result above.

</div>

**Source:**
Aggarwal & Singh (3rd ed.), Exercise 7.18, p. 363; companion slide 123.

---

### Problem 7.4 · Release Objective Evaluation with Unit Conversion (Exercise 7.24)

A program is expected to have 250 faults. It is also assumed that one fault may lead to one failure. The initial failure intensity is 5 failures/CPU hr. The program is released with a failure intensity objective of 4 failures per 10 CPU hours. Calculate the number of failures experienced before release.

1. **Given:**
    - Total faults / failures over infinite time: $v_0 = 250$ failures (1 fault = 1 failure assumption).
    - Initial failure intensity: $\lambda_0 = 5 \text{ failures/CPU hr}$.
    - Release objective: 4 failures per 10 CPU hours.

2. **Required:**
    - Number of failures experienced before release ($\mu_F$).

3. **Model & Assumptions:**
    - **Musa Basic Execution Time Model.**
    - Units must be strictly normalized to $\text{failures/CPU hr}$ before substitution.

4. **Unit Normalization & Equation:**
   $$\lambda_F = \frac{4 \text{ failures}}{10 \text{ CPU hrs}} = 0.40 \text{ failures/CPU hr}$$
   $$\lambda(\mu) = \lambda_0 \left(1 - \frac{\mu}{v_0}\right) \implies \mu = v_0 \left(1 - \frac{\lambda_F}{\lambda_0}\right)$$

5. **Substitution & Working:**
   $$\mu_F = 250 \times \left(1 - \frac{0.40}{5.0}\right) = 250 \times (1 - 0.08) = 250 \times 0.92 = 230 \text{ failures}$$

6. **Result:**
    - $\mu_F = 230 \text{ failures experienced before release}$.

7. **Check / Interpretation:**
    - The remaining unmanifested faults at release are $v_0 - \mu_F = 250 - 230 = 20 \text{ faults}$.
    - The fraction of faults removed is $230 / 250 = 92\%$, which corresponds to an intensity reduction from 5.0 to 0.40 ($92\%$ reduction).

**Source:**
Aggarwal & Singh (3rd ed.), Exercise 7.24, p. 364; companion slide 125.

---

### Problem 7.5 · Logarithmic Poisson Model — Failures Experienced after 20 CPU Hours

Assume that the initial failure intensity is $\lambda_0 = 20 \text{ failures/CPU hr}$ and the failure intensity decay parameter is $\theta = 0.02/\text{failure}$. Determine the number of failures experienced after 20 CPU hours of execution.

1. **Given:**
    - Initial failure intensity: $\lambda_0 = 20 \text{ failures/CPU hr}$
    - Failure intensity decay parameter: $\theta = 0.02/\text{failure}$
    - Execution time: $\tau = 20 \text{ CPU hrs}$

2. **Required:**
    - Expected number of failures experienced $\mu(20)$.

3. **Model & Assumptions:**
    - **Musa–Okumoto Logarithmic Poisson Execution Time Model.**
    - The failure intensity decreases exponentially with failures experienced.

4. **Equation:**
   $$\mu(\tau) = \frac{1}{\theta} \ln(\lambda_0 \theta \tau + 1)$$

5. **Substitution & Working:**
    - Inner dimensionless term:
     $$\lambda_0 \theta \tau + 1 = 20 \times 0.02 \times 20 + 1 = 8 + 1 = 9$$
    - Logarithm evaluation:
     $$\ln(9) \approx 2.19722458$$
    - Multiplication:
     $$\mu(20) = \frac{1}{0.02} \times 2.19722458 = 50 \times 2.19722458 = 109.8612 \approx 109.86 \text{ failures}$$

6. **Result:**
    - $\mu(20) = 109.86 \text{ failures} \approx 110 \text{ failures}$.
    - The displayed worked integer is 109; direct substitution into the stated equation gives 109.86.

7. **Check / Interpretation:**
    - The result follows from $\lambda_0\theta\tau+1=9$ and is consistent with the logarithmic-model equation.

**Source:**
Aggarwal & Singh (3rd ed.), §7.3.2, Example 7.2, pp. 336–337; companion slide 62.

---

### Problem 7.6 · Logarithmic Poisson Model — Failure Intensity at Specific Execution Time

Using the parameters of Problem 7.5 ($\lambda_0 = 20 \text{ failures/CPU hr}$, $\theta = 0.02/\text{failure}$), calculate the failure intensity after 20 CPU hours of execution.

1. **Given:**
    - Initial failure intensity: $\lambda_0 = 20 \text{ failures/CPU hr}$
    - Failure intensity decay parameter: $\theta = 0.02/\text{failure}$
    - Execution time: $\tau = 20 \text{ CPU hrs}$

2. **Required:**
    - Failure intensity $\lambda(20)$ in $\text{failures/CPU hr}$.

3. **Model & Assumptions:**
    - **Musa–Okumoto Logarithmic Poisson Execution Time Model.**

4. **Equations:**
    - Method 1 (Direct function of execution time $\tau$):
     $$\lambda(\tau) = \frac{\lambda_0}{\lambda_0 \theta \tau + 1}$$
    - Method 2 (Function of failures experienced $\mu$):
     $$\lambda(\mu) = \lambda_0 \exp(-\theta \mu)$$

5. **Substitution & Working:**
    - **Method 1 (Direct from $\tau = 20$):**
     $$\lambda(20) = \frac{20}{20 \times 0.02 \times 20 + 1} = \frac{20}{9} \approx 2.2222 \text{ failures/CPU hr}$$
    - **Method 2 (using the unrounded $\mu(20)=109.8612$ from Problem 7.5):**
     $$\lambda(20) = 20\exp(-0.02 \times 109.8612) \approx 2.2222 \text{ failures/CPU hr}$$

6. **Result:**
    - $\lambda(20) \approx 2.22 \text{ failures/CPU hr}$.

7. **Check / Interpretation:**
    - The two equivalent forms agree: $\lambda(20)=\lambda_0/(\lambda_0\theta\tau+1)=\lambda_0e^{-\theta\mu(20)}$.

**Source:**
Aggarwal & Singh (3rd ed.), §7.3.2, Example 7.2, p. 336; companion slide 62.

---

### Problem 7.7 · Logarithmic Model Execution Progress at 25 and 50 CPU Hours (Exercise 7.20)

Assume that the initial failure intensity is $\lambda_0 = 10 \text{ failures/CPU hr}$ and the failure intensity decay parameter is $\theta = 0.03/\text{failure}$. We have experienced 75 failures up to this time. Find the failures experienced and failure intensity after 25 and 50 CPU hours of execution.

1. **Given:**
    - Initial failure intensity: $\lambda_0 = 10 \text{ failures/CPU hr}$
    - Failure intensity decay parameter: $\theta = 0.03/\text{failure}$
    - Failures experienced at the stated current point: $\mu_P = 75 \text{ failures}$
    - Requested intervals: $\Delta\tau = 25$ and $50$ CPU hours

2. **Required:**
    - Failures experienced and failure intensity at each requested point.

3. **Model & Assumptions:**
    - **Logarithmic Poisson Execution Time Model.** The main calculation treats 25 and 50 CPU hours as additional execution time from the stated current point. The alternate cumulative-time reading is also shown because the wording does not specify the reference point.

4. **Equations:**
   $$\lambda_P = \lambda_0 e^{-\theta\mu_P}, \qquad \mu(\tau_P+\Delta\tau)=\mu_P+\frac{1}{\theta}\ln(1+\theta\lambda_P\Delta\tau)$$
   $$\lambda(\tau_P+\Delta\tau)=\frac{\lambda_P}{1+\theta\lambda_P\Delta\tau}, \qquad \tau_P=\frac{e^{\theta\mu_P}-1}{\lambda_0\theta}$$
    - If the requested times are cumulative from the start: $\mu(\tau)=\frac{1}{\theta}\ln(\lambda_0\theta\tau+1)$ and $\lambda(\tau)=\frac{\lambda_0}{\lambda_0\theta\tau+1}$.

5. **Substitution & Working:**
    - Current state: $\lambda_P=10e^{-0.03(75)}\approx1.05399$ failures/CPU hr and $\tau_P=(e^{2.25}-1)/0.30\approx28.29$ CPU hours.
    - **After an additional 25 CPU hours:** $\mu=75+\frac{1}{0.03}\ln(1+0.03(1.05399)(25))\approx94.42$ failures; $\lambda=\frac{1.05399}{1+0.03(1.05399)(25)}\approx0.589$ failures/CPU hr.
    - **After an additional 50 CPU hours:** $\mu=75+\frac{1}{0.03}\ln(1+0.03(1.05399)(50))\approx106.61$ failures; $\lambda=\frac{1.05399}{1+0.03(1.05399)(50)}\approx0.408$ failures/CPU hr.
    - **If 25 and 50 hours mean cumulative time from the start:** $\mu(25)\approx71.34$, $\lambda(25)\approx1.176$; $\mu(50)\approx92.42$, $\lambda(50)=0.625$. However, the stated 75 failures correspond to $\tau_P\approx28.29$ hours, so the 25-hour point precedes the stated current state.

6. **Result:**
    - Main reading (25 and 50 additional CPU hours): $(\mu,\lambda)\approx(94.42,0.589)$ and $(106.61,0.408)$, respectively.
    - Cumulative-from-start reading: $(\mu(25),\lambda(25))\approx(71.34,1.176)$ and $(\mu(50),\lambda(50))\approx(92.42,0.625)$; this conflicts with the stated current point at 75 failures for $\tau=25$.

7. **Check / Interpretation:**
    - Under the main reading, both requested times follow the present state and failure intensity decreases as execution time increases.

**Source:**
Aggarwal & Singh (3rd ed.), Exercise 7.20, p. 363; companion slide 123.
---

### Problem 7.8 · Comparative Calculation: Basic vs Logarithmic Poisson Model (Exercise 7.21)

The following parameters for the Basic Execution Time Model and the Logarithmic Poisson Execution Time Model are given:

- **Basic Model:** $\lambda_0 = 5 \text{ failures/CPU hr}$, $v_0 = 125 \text{ failures}$
- **Logarithmic Poisson Model:** $\lambda_0 = 25 \text{ failures/CPU hr}$, $\theta = 0.30/\text{failure}$

Determine the additional failures ($\Delta \mu$) and additional execution time ($\Delta \tau$) required to reach the failure intensity objective of $\lambda_F = 0.10 \text{ failure/CPU hr}$ for both models (from their initial states $\lambda_0$).

1. **Given:**
    - Basic Model: $\lambda_{0,B} = 5 \text{ failures/CPU hr}$, $v_0 = 125 \text{ failures}$
    - Logarithmic Model: $\lambda_{0,L} = 25 \text{ failures/CPU hr}$, $\theta = 0.30/\text{failure}$
    - Common target failure intensity: $\lambda_F = 0.10 \text{ failure/CPU hr}$

2. **Required:**
    - For Basic Model: $\Delta \mu_B$ and $\Delta \tau_B$.
    - For Logarithmic Model: $\Delta \mu_L$ and $\Delta \tau_L$.

3. **Model & Assumptions:**
    - Comparison evaluated from initial state ($\lambda_P = \lambda_0$, $\mu_P = 0$) to target release objective ($\lambda_F$).

4. **Equations:**
    - **Basic Execution Time Model:**
     $$\Delta \mu_B = \frac{v_0}{\lambda_{0,B}} (\lambda_{0,B} - \lambda_F) = v_0 \left(1 - \frac{\lambda_F}{\lambda_{0,B}}\right)$$
     $$\Delta \tau_B = \frac{v_0}{\lambda_{0,B}} \ln\left(\frac{\lambda_{0,B}}{\lambda_F}\right)$$
    - **Logarithmic Poisson Model:**
     $$\Delta \mu_L = \frac{1}{\theta} \ln\left(\frac{\lambda_{0,L}}{\lambda_F}\right)$$
     $$\Delta \tau_L = \frac{1}{\theta} \left(\frac{1}{\lambda_F} - \frac{1}{\lambda_{0,L}}\right)$$

5. **Substitution & Working:**
    - **Case 1: Basic Model Calculations:**
        - Scaling factor: $\frac{v_0}{\lambda_{0,B}} = \frac{125}{5} = 25 \text{ CPU hrs}$.
        - Additional failures:
       $$\Delta \mu_B = 125 \times \left(1 - \frac{0.10}{5}\right) = 125 \times (1 - 0.02) = 125 \times 0.98 = 122.5 \text{ failures}$$
        - **Additional execution time:** $\Delta \tau_B = 25 \times \ln\left(\frac{5}{0.10}\right) = 25 \times \ln(50) = 25 \times 3.912023 \approx 97.8006 \approx 97.80 \text{ CPU hrs}$
    - **Case 2: Logarithmic Poisson Model Calculations:**
        - Scaling factor: $\frac{1}{\theta} = \frac{1}{0.30} = \frac{10}{3} \approx 3.3333$.
        - Ratio: $\frac{\lambda_{0,L}}{\lambda_F} = \frac{25}{0.10} = 250$.
        - Additional failures:
       $$\Delta \mu_L = \frac{10}{3} \times \ln(250) = \frac{10}{3} \times 5.521461 = 18.40487 \approx 18.40 \text{ failures}$$
        - **Additional execution time:** $\Delta \tau_L = \frac{1}{0.30} \times \left(\frac{1}{0.10} - \frac{1}{25}\right) = \frac{10}{3} \times (10 - 0.04) = \frac{10}{3} \times 9.96 = 33.20 \text{ CPU hrs}$

6. **Result:**
    - **Basic Model:** $\Delta \mu_B = 122.5 \text{ failures}$, $\Delta \tau_B \approx 97.80 \text{ CPU hrs}$.
    - **Logarithmic Model:** $\Delta \mu_L \approx 18.40 \text{ failures}$, $\Delta \tau_L = 33.20 \text{ CPU hrs}$.

7. **Check / Interpretation:**
    - Although the Logarithmic Poisson model starts at a higher initial intensity ($\lambda_0 = 25$ vs $5$), its high decay parameter ($\theta = 0.30/\text{failure}$) drops failure intensity far more rapidly per observed failure, requiring only $\approx 18.4$ failures and $33.2$ CPU hours compared to $122.5$ failures and $97.8$ CPU hours under the Basic model.

**Source:**
Aggarwal & Singh (3rd ed.), Exercise 7.21, p. 364; companion slide 124.

---

### Problem 7.9 · Calendar Time Component — Resource-Limited Execution Time Ratio (Examples 7.4–7.6)

During a software testing phase, resource usage is modeled as $\chi_k = \theta_k \tau + \mu_k \mu$. For the failure identification personnel resource ($k = I$):

- $\theta_I = 15 \text{ person-hrs/CPU hr}$
- $\mu_I = 2 \text{ person-hrs/failure}$
- Available personnel: $P_I = 2 \text{ persons}$
- Utilization factor: $\rho_I = 0.80$
If an interval requires an additional execution time of $\Delta \tau = 10 \text{ CPU hrs}$ and experiences $\Delta \mu = 25 \text{ failures}$, calculate:
1. The total resource usage $\Delta \chi_I$ in person-hours.
2. The calendar time $\Delta t$ required to complete this testing phase (in calendar hours and 8-hour work days).

**1. Given:**

- Execution time increment: $\Delta \tau = 10 \text{ CPU hrs}$
- Failure increment: $\Delta \mu = 25 \text{ failures}$
- Effort parameters: $\theta_I = 15 \text{ person-hrs/CPU hr}$, $\mu_I = 2 \text{ person-hrs/failure}$
- Staffing and utilization: $P_I = 2$, $\rho_I = 0.80$

**2. Required:**

- Total resource requirement $\Delta \chi_I$ in person-hours.
- Calendar time $\Delta t$ in calendar hours and working days.

**3. Model & Assumptions:**

- **Musa Calendar Time Component Model.**
- Testing is conducted in the Failure Identification Personnel Limited segment.
- 1 working day equals 8 productive calendar hours.

**4. Equations:**

$$\Delta \chi_I = \theta_I \Delta \tau + \mu_I \Delta \mu$$
$$\Delta t = \frac{\Delta \chi_I}{P_I \rho_I}$$

**5. Substitution & Working:**

- **Resource Usage:**
  $$\Delta \chi_I = (15 \times 10) + (2 \times 25) = 150 + 50 = 200 \text{ person-hrs}$$
- **Calendar Time:**
  $$\Delta t = \frac{200}{2 \times 0.80} = \frac{200}{1.60} = 125.0 \text{ calendar hrs}$$
- In 8-hour working days:
  $$\Delta t_{\text{days}} = \frac{125}{8} = 15.625 \text{ work days} \approx 16 \text{ work days}$$

**6. Result:**
{: .keep-next }

- $\Delta \chi_I = 200 \text{ person-hrs}$
- $\Delta t = 125.0 \text{ calendar hrs } (15.6 \text{ working days})$

**7. Check / Interpretation:**

- The interval-average ratio is $\Delta t/\Delta\tau = 125/10 = 12.5$ calendar hours per CPU hour. This agrees with average resource use of $200/10 = 20$ person-hours per CPU hour divided by available utilized capacity $P_I\rho_I = 1.6$ persons.

**Source:**
Aggarwal & Singh (3rd ed.), §7.3.3, Examples 7.4–7.6, pp. 340–342; companion slides 72–82.

---

### Problem 7.10 · Jelinski–Moranda Model & Bug Seeding Population Estimation (Example 7.7 & Exercise 7.26)

1. **Part A (Jelinski–Moranda Model):** A software system has an estimated initial fault count of $N = 50$, with a fault failure rate constant of $\phi = 0.002/\text{hr}$. Calculate the failure hazard rate $\lambda(t_i)$ when debugging starts ($i = 1$), after 10 faults have been removed ($i = 11$), and after 40 faults have been removed ($i = 41$).
2. **Part B (Harlan Mills Bug Seeding):** An organization seeds $S = 20$ artificial bugs into a software program before testing. Testing discovers a total of 30 bugs, of which $s = 12$ are seeded bugs and $n = 18$ are indigenous bugs. Estimate the total original indigenous bug population $\hat{N}$ and the number of unmanifested indigenous bugs remaining in the code.

#### Part A: Jelinski–Moranda Evaluation

1. **Given:**
    - Initial fault count: $N = 50$
    - Proportionality constant: $\phi = 0.002/\text{hr}$
    - Indices: $i = 1$ (first failure), $i = 11$ (11th failure / 10 removed), $i = 41$ (41st failure / 40 removed)

2. **Required:**
    - Hazard rate $\lambda(t_1)$, $\lambda(t_{11})$, and $\lambda(t_{41})$ in $\text{failures/hr}$.

3. **Model & Equation:**
   $$\lambda(t_i) = \phi [N - (i - 1)]$$

4. **Working:**
    - For $i = 1$:
     $$\lambda(t_1) = 0.002 \times [50 - (1 - 1)] = 0.002 \times 50 = 0.10 \text{ failures/hr}$$
    - For $i = 11$:
     $$\lambda(t_{11}) = 0.002 \times [50 - (11 - 1)] = 0.002 \times 40 = 0.08 \text{ failures/hr}$$
    - For $i = 41$:
     $$\lambda(t_{41}) = 0.002 \times [50 - (41 - 1)] = 0.002 \times 10 = 0.02 \text{ failures/hr}$$

5. **Result (Part A):**
    - $\lambda(t_1) = 0.10 \text{ failures/hr}$
    - $\lambda(t_{11}) = 0.08 \text{ failures/hr}$
    - $\lambda(t_{41}) = 0.02 \text{ failures/hr}$

---

<div class="no-break" markdown="1">

#### Part B: Bug Seeding Estimation

1. **Given:**
    - Seeded artificial bugs: $S = 20$
    - Discovered seeded bugs: $s = 12$
    - Discovered indigenous bugs: $n = 18$

2. **Required:**
    {: .keep-next }
    - Estimated total indigenous bugs $\hat{N}$.
      {: .keep-next }
    - Estimated remaining unmanifested indigenous bugs $N_{\text{rem}}$.

3. **Model & Assumptions:**
    - **Mills Bug Seeding Model (Capture–Recapture Analogy).**
    - Indigenous bugs and seeded bugs have identical detection probabilities and are randomly distributed throughout the code.

4. **Equation:**
   $$\frac{s}{S} = \frac{n}{\hat{N}} \implies \hat{N} = \frac{S \times n}{s}$$
   $$N_{\text{rem}} = \hat{N} - n$$

5. **Working:**
   $$\hat{N} = \frac{20 \times 18}{12} = \frac{360}{12} = 30 \text{ indigenous bugs}$$
   $$N_{\text{rem}} = 30 - 18 = 12 \text{ indigenous bugs remaining}$$

6. **Result (Part B):**
    - Estimated total indigenous bugs: $\hat{N} = 30 \text{ bugs}$.
    - Estimated remaining indigenous bugs: $N_{\text{rem}} = 12 \text{ bugs}$.

7. **Check / Interpretation:**
    - Recovery ratio for seeded bugs is $12 / 20 = 60\%$. Under equal detectability, the 18 discovered indigenous bugs also represent $60\%$ of total indigenous bugs ($18 / 0.60 = 30$). Arithmetic is completely consistent.

**Source:**
Aggarwal & Singh (3rd ed.), §7.3.4 & §7.3.5, Example 7.7, pp. 343–346; companion slides 89–93.

</div>


---

<!--
## Retrieval Practice Set & Self-Test Exercises

1. **Basic Execution Time Linearity:** Write down the formula for failure intensity $\lambda(\mu)$ in the Basic model. If a program has $v_0 = 200$ and initial intensity $\lambda_0 = 10 \text{ failures/CPU hr}$, what is the failure intensity after 150 failures have occurred?
2. **Logarithmic Poisson Intensity Drop:** In the Logarithmic Poisson model, write down the formula for additional execution time $\Delta \tau$ required to decrease failure intensity from $\lambda_P$ to $\lambda_F$. How does this differ from the Basic model formula?
3. **Calendar Time Limiting Resources:** Identify the three resource categories that determine calendar time progression in Musa's calendar time component model ($k = C, I, F$).
4. **Jelinski–Moranda vs Musa Basic:** What is the primary conceptual similarity between the Jelinski–Moranda model hazard rate $\lambda(t_i) = \phi [N - (i - 1)]$ and Musa's Basic Execution Time Model $\lambda(\mu) = \lambda_0 (1 - \mu/v_0)$?
5. **Mills Bug Seeding Estimation:** If 25 artificial bugs are seeded into a codebase, and testing uncovers 15 seeded bugs along with 30 indigenous bugs, how many total indigenous bugs are estimated to have been present originally?
-->
