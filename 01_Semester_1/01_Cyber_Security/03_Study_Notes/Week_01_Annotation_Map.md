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

✅ **Confirmed by the student (2026-09-18):** the doctor said she does not want it — *"هي كالت ما تريده ما داخل"*.
**→ Chapter 7 is OUT of exam scope. Do not spend time on it.**

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

## 6. ✅ DECODED — how Dr. Huda actually tests (student-confirmed, 2026-09-18)

### 6.1 The source document
This PDF **is the doctor's own lecture material** — *not* the student's summary. His marks were written *during* the lecture, recording what she said. **So these 7 chapters = the official Week 01 content.**

### 6.2 Formulas: numbers → compute. No numbers → scenario.
> *"مرات مستقبلا تطيك الارقام والسؤال بيه ارقام وانت تعرف هاي معادلة... اذا ماكو ارقام او ماكو مطلوب وياه كرقم يعني تريد سيناريو تحليلي"*

| Situation | What she wants |
|:---|:---|
| The question **contains numbers** | Plug them into the formula and **compute** |
| **No numbers**, or nothing asked *as a number* | **Analytical scenario** — explain what happened using the concepts |

→ This resolves the page-3 confusion. The formulas are **not** for blind memorisation; they exist so you can tell *"this is a formula question"* apart from *"this is a scenario question"*.

### 6.3 The scenario answer format — THE key pattern ⭐
The student's own worked example:

> A bank customer sees his account drop by **$100,000** at once. He calls the manager. The manager investigates, finds it was just a program crash, fixes it, and returns the money.

**How to answer it:**

| Step | What happened | Label it | In parentheses |
|:--:|:---|:---|:---|
| 1 | The user saw his data had changed | **Integrity** | (hashing SHA-256, digital signatures, version control) |
| 2 | We called, found the system had a problem | **Availability** | (redundancy, load balancing, DDoS mitigation) |
| 3 | Fixed and restored | — | — |

**The rule:**
> Walk the scenario **step by step**; at each step name the **CIA pillar** involved — then **in parentheses write the techniques** from the CIA triad that would fix it.

✅ **Both depths are accepted:** deep step-by-step analysis **or** analysing the whole scenario at once — *"الاجابتين صح"*.

### 6.4 The "100" threshold (page 1)
> *"اذا الناتج ازداد عن ال 100 يعني اكو استثمار واذا اقل من 100 يعني مفيش استثمار"*

✅ **The doctor said this herself** — it is not the student's inference.
⚠️ *Koko's note:* mathematically $\min R$ is unbounded, so "100" is almost certainly a **baseline / index reference** rather than an output of that sum — possibly a return-on-security-investment style comparison. **Ask the doctor to clarify; do not assume.** Flagged, not guessed.

### 6.5 The daily quiz (امتحان يومي) — real format
| Aspect | Answer |
|:---|:---|
| Format | **Written, with solutions — essay type (مقالي).** *Not* MCQ. |
| Length | **~10 minutes** |
| When | Probably **at the start of the lecture** |
| Stakes | **Soft.** She said: *"if I see you've answered, I won't count it; if I see you haven't answered, I'll count it against you as a grade. I'll help you — but I want you to read, even if you're forced to."* |
| Real purpose | A **reading-compliance check**, not a hard assessment |

**→ Strategic conclusion: low risk.** Show up having read, write something structured, and you are fine. Don't lose sleep — but don't skip it either.

### 6.6 The $R(t)$ formula
> *"اي علمود هيج بس نعرف هذا القانون هنا يستخدم"* — she only wants you to know that this law is used here. **Superficial awareness only.** Matches the student's margin note (*"مو مفيد… غير مستخدم"*).

### 6.7 What this means for how we study this subject
The `00_Doctor_Profile.md` claim ("analytical, not rote memorization") is **correct — but incomplete.** The full picture:

1. **Concept first**, in her own words.
2. **The CIA Triad and its technique lists must be memorised cold** — they are the *vocabulary* you write inside the parentheses of every scenario answer.
3. **Formulas: recognise, don't worship.** Compute only when numbers are given.
4. **Chapter 7 is out.**
5. **Practice = scenarios**, answered as: step → CIA pillar → (techniques).

---

*Captured 2026-09-18 by Koko, from the student's own answers.*
