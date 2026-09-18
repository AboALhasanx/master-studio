# 🔐 Cyber Security — Week 01: Annotation Map

> **Source PDF:** `02_Raw_Materials/Week 01 - ANNOTATED (student) - Introduction to Cybersecurity.pdf`
> (original kept at `C:\Users\gokoq\Downloads\1st week.pdf` — untouched)
> **5 pages · 7 chapters · 6 mathematical models**
> **Captured:** 2026-09-18 by Koko, from the student's own handwriting/highlights/notes in the PDF.

---

## 1. What the document contains

| Chapter | Title | Mathematical model |
|:--|:--|:--|
| 1 | Introduction to Cybersecurity | $\min R = \sum_{i=1}^{n} P_i \cdot I_i - \sum_{j=1}^{m} C_j$ |
| 2 | Importance & Scope | $R(t) = \sum_{i=1}^{n} P_i(t) \cdot I_i(t)$ |
| 3 | The CIA Triad | $U(C, I, A) = \alpha C + \beta I + \gamma A$ |
| 4 | Threat Landscape | $AS = \sum_{j=1}^{m} (E_j \cdot V_j \cdot A_j)$ |
| 5 | Risks, Vulnerabilities, Exploits | $P(R > r) = 1 - F(r)$ |
| 6 | Evolution & Policy Overview | $PCI = \dfrac{\sum_{k=1}^{n} w_k \cdot c_k}{\sum_{k=1}^{n} w_k}$ |
| 7 | Case Studies (Stuxnet, Colonial Pipeline, GDPR) | — |

---

## 2. 🟥 Circled in RED — the student marked these as **the important ones**

| Page | Formula | Meaning |
|:--:|:--|:--|
| 1 | $\min R = \sum P_i I_i - \sum C_j$ | Cybersecurity as an **optimization problem** — minimise risk while maximising investment |
| 2 | $R(t) = \sum P_i(t) \cdot I_i(t)$ | **Cyber risk exposure** — expected risk across multiple threats, at time $t$ |
| 3 | $U(C,I,A) = \alpha C + \beta I + \gamma A$ | **Security utility function** — weighted CIA |
| 4 | $AS = \sum (E_j \cdot V_j \cdot A_j)$ | **Attack surface metric** — "how attackable is the system" |

**Pattern: 4 of the 6 formulas are circled. These are the ones to be able to explain and use.**

---

## 3. 🟨 Highlighted in YELLOW — memorisation targets

The **entire CIA Triad block**, including every technique list:

| Pillar | Definition | Techniques |
|:--|:--|:--|
| **Confidentiality** | Preventing unauthorized access to data | encryption · access controls · VPNs |
| **Integrity** | Ensuring data is accurate and unaltered | hashing (SHA-256) · digital signatures · version control |
| **Availability** | Ensuring resources are accessible when needed | redundancy · load balancing · DDoS mitigation |

Also in red type in the source (the doctor's own emphasis):
> *"Why 'In healthcare, confidentiality (α) has higher weight than availability.'"*

→ The point: **α, β, γ are not fixed** — they change with the domain. Healthcare weights α (confidentiality) higher.

---

## 4. ❌ Crossed out in RED — Chapter 7 (Case Studies)

The whole of **Chapter 7** — Stuxnet (2010), Colonial Pipeline Ransomware (2021), GDPR Enforcement — is **struck through with heavy red X marks.**

*Needs confirming: was this the doctor saying "not required", or the student's own call?*

---

## 5. 📝 The student's own annotations (verbatim, Iraqi Arabic)

| Pg | Next to | Annotation | Reading |
|:--:|:--|:--|:--|
| 1 | Historical Evolution | *مراحل تطوير السايبر سكيروتي* | stages of cyber-security development |
| 1 | (beside $\min R$) | *معنى* + *اذا الناتج ازداد عن ال 100 يعني اكو استثمار واذا اقل من 100 يعني مفيش استثمار* | "meaning" — if the result exceeds 100 there's investment; below 100 there isn't |
| 2 | top of page | *عدد مجالات السايبر قابلة للزيادة* | the number of cyber domains can grow |
| 2 | Key Domains | *المجالات الاساسية للسايبر* | the core cyber domains |
| 2 | Chapter 3 heading | *السيناريو* | "the scenario" |
| 2 | $R(t)$ | *السؤال مالته بيه وقت بس مو مفيد ترا مجرد هيج... غير مستخدم بس علمود نعرف انو هو هذا القانون* | "his question has time in it but it's not useful, just like that… unused — only so we know this law exists" |
| 3 | scenario/evidence | *هنا يعني بالسيناريو لمن يكون الشي يحتاج دليل evidence* | in the scenario, when something needs evidence |
| 3 | $U(C,I,A)$ | *ما اعرف شنو هذا بس شنوووو المفروض..... انو يكون السؤال ارقام ونطبق المعادلة... او تفكير نقدي ذهني فما يحتاج معادلة* | **"I don't know what this is — but what's it supposed to be? Is the question numbers where we apply the equation… or critical thinking, so no equation needed?"** |
| 3 | Global Trends | *ترندات الاختراقات بـ 2023 2024* | breach trends 2023–2024 |
| 4 | $AS$ | *دراسة الثغرات* | studying vulnerabilities |
| 4 | $P(R>r)=1-F(r)$ | *ال f(r) محصورة بين 0 و 1* | F(r) is bounded between 0 and 1 |
| 5 | PCI | *الالتزام بالسياسة او القوانين اووالمدري شنو* | compliance with policy or laws, or… I don't know what |

---

## 6. ⚠️ The gap worth noticing

`00_Doctor_Profile.md` describes Dr. Huda's exams as **"analytical diagnostic competence rather than rote memorization"** — scenario-driven, enterprise incident triage, mitigation matrices.

But **this material is formula-heavy**: 6 mathematical models in 5 pages.

**These two pictures don't match.** Which is exactly why the student said *"طريقة دراستها غريبة"* — the way this subject is studied is strange.

**The open question that decides everything:**
> Does Dr. Huda test these formulas **numerically** (give numbers → plug into the equation), or **conceptually** (explain what the model means / use it in a scenario)?

*Pending the student's answers — see §7.*

---

## 7. Open questions for the student

1. Where did this PDF come from — the doctor's own slides, or your own summary?
2. Does she test the formulas numerically, or conceptually?
3. Why is Chapter 7 crossed out?
4. Where does the "100" threshold on page 1 come from?
5. What does the **daily quiz (امتحان يومي)** actually look like?
6. How does she use **scenarios**?

---

*Captured 2026-09-18. Will be updated once the student answers §7.*
