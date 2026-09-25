---
title: "Week 02 — Risk · Mathematical & Logical Verification of the Two Equations"
subject: "01_Cyber_Security"
week: 2
source_under_test: "Sharp, R., 'Risk', Introduction to Cybersecurity, Springer, 2024, pp. 37–56 (DOI 10.1007/978-3-031-41463-3_3)"
method: "independent mathematical analysis — boundary conditions, dimensional check, equivalence proof, logical contradiction test"
status: "verdict reached without needing the paywalled text"
created: "2026-09-23"
---

# The Two Equations — Mathematical and Logical Verification

> **UPDATE — the book has now been read directly. The analysis below is confirmed, with one refinement.**
>
> - **`S = F × K` and `R = S / M` are confirmed verbatim** from Sharp's typeset text (printed pp. 38–39), including `M` covering *number of countermeasures + effectiveness*. My reconstruction was exact.
> - **Both figures confirm the structural predictions:** Fig. 3.2 (risk matrix) and Fig. 3.3 (residual-risk matrix) are **mirror-symmetric in their colour banding**, which is what the multiplicative form predicts. Red appears **only** at (high frequency, high consequences) and at (high risk, low countermeasures) — exactly as the boundary analysis implied.
> - **REFINEMENT — the book does not use the equations arithmetically.** Its own worked examples print `medium × high (= medium)`, not `6`. So `×` and `/` are **ordinal combination operators**, and the operative rule is the colour table in Figs. 3.2/3.3. The equation is a **mnemonic for the table**.
> - **Consequence for §3 below:** the boundary-condition critique (`M = 0` divides by zero; `0 < M < 1` gives `R > S`) is correct **for the arithmetic reading**, but the book does not take that reading. On the ordinal reading the matrix is the rule, and the matrix is well-formed in every cell. **Both statements are true; the book means the second.** See `W02_Source_Verify.md` §9.8.
> - **Practical exam rule:** given low/medium/high, **read the colour off Fig. 3.2 or 3.3** — do not multiply numbers.

> **Purpose.** You asked me to verify the formulas "mathematically and logically" and to try published page images. This file does both: it reports honestly what the image search could and could not reach, and then **proves** what the equations must be from their own internal behaviour — which does not depend on the paywall at all.

---

## 1. The image search — what I tried and what it returned

You suggested looking for published images of the pages. I tried the following routes:

| Route | Result |
|:---|:---|
| Exact-phrase search on the chapter's own sentences | Returned the Springer chapter landing page only — **the chapter body is not publicly indexed** |
| Springer's chapter PDF and book front-matter PDF | **Blocked** — "verifying your browser" bot protection; the PDFs are paywalled |
| Google Books | No accessible preview record surfaced for this ISBN |
| Secondary preview/aggregator sites | No legitimate preview found |
| The chapter's figure captions | One partial snippet surfaced: *"In the two figures, 3.2 and 3.3, we have here used a 3-point scale (low, medium, high) for all quantities (frequency, …)"* — enough to confirm the book uses **frequency** as a quantity and has **two colour-coded matrices**, but not enough to read the equations |

**Honest conclusion: I could not obtain the page images.** The chapter is behind a paywall and the publisher blocks automated access. I am not going to pretend otherwise, and I am not going to state Sharp's letters as verified fact on the strength of a search snippet.

**Routes that would actually work, and that I cannot take for you:**
1. **University library** — most university libraries hold the Springer *Undergraduate Topics in Computer Science* series. With library access the chapter PDF is a two-click download. This is the cleanest route and costs nothing.
2. **The physical book** — ISBN 978-3-031-41463-3, 442 pp. Chapter 3 is pp. 37–56.
3. **Your paper notes** from the lecture.

**But none of that is needed to answer the question**, because the equations can be tested on their own terms. That is the rest of this file.

---

## 2. Equation 1 — `S = F × K` (basic risk)

### 2.1 What form is this?

It is the **likelihood × consequence** convention — the standard shape in risk analysis (the ISO 31000 / IEC 31010 lineage, AS/NZS 4360, and the same family as FMEA's RPN = Severity × Occurrence × Detection). So the **form is orthodox**, not idiosyncratic.

### 2.2 Why multiplication and not addition — the test that decides it

This is testable, and it is the same argument that governs Week 01's attack-surface equation.

Take two cases:
- **Case A:** attacks are extremely frequent, but each one causes negligible harm.
- **Case B:** attacks are extremely rare, but each one is catastrophic.

Under **multiplication**: both cases collapse toward a low product, because one factor is near zero. That matches reality — a nuisance that happens constantly is not a catastrophe, and a catastrophe that never happens is not a threat.

Under **addition**: a very large frequency could **compensate** for a zero consequence and produce a large "risk" — which is nonsense, because an event with no consequence cannot be a risk.

**Verdict: multiplication is correct, and it is correct for a specific reason — it enforces "both factors must matter".** Addition cannot do that.

### 2.3 What the multiplication actually does to a 3-point scale

The book confirms (via the figure snippet) that all quantities use a **3-point scale: low / medium / high**. Encode that as {1, 2, 3}. Then the product `F × K` can only take these values:

```text
F×K over {1,2,3} × {1,2,3}  →  1, 2, 3, 4, 6, 9
```

Nine cells, but only **six distinct products**. Two consequences follow, and both are worth knowing:

1. The risk matrix is **symmetric** — cell (F=1, K=3) and cell (F=3, K=1) give the same value (3). So the matrix is mirror-symmetric across the main diagonal, and a threat at high frequency / low consequence scores identically to one at low frequency / high consequence.
2. The levels are **non-uniformly spaced** (1, 2, 3, 4, 6, 9 — gaps of 1, 1, 1, 2, 3). That is exactly why the matrix needs **colour banding** (red / yellow / green) rather than a single number: the numeric output is not on a linear scale, so it is banded into ordinal levels.

**This is a check that the booklet's description is internally consistent** — it says the multiplication result "is indicated by a color code", which is precisely what a non-linear multiplicative scale requires.

---

## 3. Equation 2 — `R = S / M` (residual risk) — the rigorous test

This is the equation that needed the real work. I tested it by **boundary conditions**, which is the standard way to check whether a model is well-posed.

### 3.1 Direction of effect

Differentiate with respect to the denominator:

```text
R = S / M        ∂R/∂M = −S / M²
```

Since `S > 0` and `M² > 0`, the derivative is **strictly negative**. So **R decreases monotonically as M increases.** That is the correct direction: more or better countermeasures must lower residual risk.

**Pass.**

### 3.2 Boundary conditions — where the model breaks

| Case | What the formula gives | What reality requires | Verdict |
|:---|:---|:---|:---|
| **M → ∞** (perfect, unlimited protection) | `R → 0⁺` — approaches zero but never reaches it | Residual risk should approach zero but never be zero | **PASS** |
| **M = 1** (neutral protection) | `R = S` — residual equals inherent | A neutral defence should leave risk unchanged | **PASS**, but only if M is normalised so that 1 = neutral |
| **M = 0** (no countermeasures at all) | **`R = S/0` — undefined, division by zero** | With no defence, residual risk must **equal** the inherent risk S | **FAIL** |
| **0 < M < 1** (weak defence) | `R > S` — residual risk **exceeds** inherent risk | Residual risk can never exceed inherent risk; you cannot end up with *more* risk after defending | **FAIL** |

### 3.3 What the two failures prove

The formula is well-formed **only on the domain `M ≥ 1`**. Two hard consequences:

1. **`M` cannot be a raw count of countermeasures.** A count is naturally `0` when there are none, and the formula explodes at exactly that point — the one case where the answer is trivially known (`R = S`). So `M` is not a count.
2. **`M` must be a dimensionless protective factor, normalised so that `M = 1` means "no net protection" and `M ≥ 1` always.**

**And this is exactly why the booklet's own wording matters.** It says:

> *"M covers both the number of countermeasures … and their effectiveness."*

Read carefully, that sentence is not padding — it is the book telling you that `M` is a **combined** quantity. The "number" alone cannot be the divisor (proved above). It is the **number combined with effectiveness** that yields a protective factor ≥ 1. The maths forces that reading, and the book's sentence supplies it. **The two agree.**

### 3.4 The decisive test — is the division form even legitimate?

Here is the strongest check. The mainstream industry formula for residual risk is **multiplicative, not divisive**:

```text
Industry convention:   Residual Risk = Inherent Risk × (1 − Control Effectiveness)
                       R = S (1 − CE),      with 0 ≤ CE < 1
```

Substitute `M = 1 / (1 − CE)`. Then:

```text
S / M  =  S / (1/(1−CE))  =  S (1 − CE)  =  R      ✓
```

**The two forms are algebraically identical.** `R = S / M` is not a different model from the industry standard — it is the **same model with the protection expressed as a factor instead of as a percentage reduction**.

Check the mapping at both ends:

| Control effectiveness `CE` | Protection factor `M` | Residual risk |
|:---|:---|:---|
| `CE = 0` (no control) | `M = 1` | `R = S` ✓ |
| `CE = 0.5` (half effective) | `M = 2` | `R = S/2` ✓ |
| `CE → 1` (perfect control) | `M → ∞` | `R → 0` ✓ |

Every boundary matches. **Verdict: the division form is legitimate — but only on the reading `M ≥ 1` as a protective factor, which is precisely the reading the booklet's own sentence supports.**

### 3.5 Dimensional check

```text
[R] = [risk]        [S] = [risk]        [M] = dimensionless
R = S / M  →  [risk] = [risk] / 1   ✓ dimensionally consistent
S = F × K  →  [risk] = [frequency] × [risk per event]   ✓ consistent
```

Both equations are dimensionally sound, and `S` carries the same dimension in both — which is required, since equation 1's output is equation 2's input.

---

## 4. Testing your lecture report — `f = s · k` and `f = s / n` (n = number of threats)

You reported the lecture as two equations both beginning with `f`. I tested that report on its own terms, without reference to the book.

### 4.1 Internal consistency test

If `f` is the subject of both equations, then `f` must denote the same quantity in both. But:

- In equation 1, `f` is built from `s` and `k`.
- In equation 2, `f` is built from `s` and `n`.

For the system to be coherent, `s` must mean the same thing in both. Test it:

| | Equation 1 | Equation 2 |
|:---|:---|:---|
| Subject `f` would be | risk | residual risk |
| Then `s` must be | one of the two risk factors (frequency) | the risk itself |

**`s` = frequency in one equation and `s` = risk in the other. That is a contradiction.** The same symbol cannot carry two different meanings in the same two-line model.

**Conclusion: the report cannot be literally correct. At least one letter is misheard or mis-transcribed.** This is established by logic alone — no access to the book required.

### 4.2 The independent test on "n = number of threats"

Set the letters aside entirely and test the *claim* that the divisor is the **number of threats**.

| Scenario | Under `R = S / N` with N = number of threats | Reality |
|:---|:---|:---|
| A system with **1** threat vs a system with **100** threats, same frequency and consequence each | The 100-threat system has **lower** risk | More threats must mean **more** risk, not less |
| A system with **0** threats | `R = S/0` — **undefined** | No threats must mean **no risk** |

Both rows fail. **The divisor cannot be the number of threats.** A defensive quantity must be in the denominator; a threat quantity must not be.

**Verdict: the booklet's `M` (countermeasures) is the only coherent reading. The report's `n` (threats) is not.**

### 4.3 What the mishearing most likely was

Two symbols are easy to confuse aloud, and both appear in this model:

- **`M`** (the countermeasure factor) and **`N`** — a listener hearing "em" can write "n".
- **`F`** (frequency) and **`S`** (risk) — the two letters that swap positions between the two equations.

Either way, the *structure* is settled by §3 and §4.2: **risk = frequency × consequence, then residual risk = risk divided by a protective factor ≥ 1.**

---

## 5. Cross-check against the matrix structure

The book has **two** matrices, and the booklet describes their axes:

| Matrix | Axes per the booklet | Consistent? |
|:---|:---|:---|
| **Risk matrix** | frequency × consequences | ✓ — these are exactly `F` and `K`, the inputs of equation 1 |
| **Residual-risk matrix** | risk ÷ countermeasures | ✓ — these are exactly `S` and `M`, the inputs of equation 2 |

**This is a strong structural confirmation.** The output of equation 1 (`S`) becomes an axis of the second matrix, which is why the booklet can say `S` is *"the risk of the threat"* when discussing equation 2 — `S` is already defined by then. The two-equation, two-matrix model is **internally coherent as a pipeline**:

```text
F, K  ──[ S = F × K ]──►  S  ──[ R = S / M ]──►  R
 │                              │
 └── risk matrix                └── residual-risk matrix
     (axes F, K)                    (axes S, M)
```

If the second matrix's axes had instead been (risk, number of threats), the model would carry a redundant threat-counting step that no other part of the chapter uses — and it would break at zero threats, as shown in §4.2. The booklet's version is the coherent one.

---

## 6. Final verdict

| Item | Verdict | Basis |
|:---|:---|:---|
| **`S = F × K`** | **Sound.** Orthodox likelihood × consequence form; multiplication is required (not addition) because it enforces that both factors must matter; produces a symmetric, non-uniform scale, which is exactly why colour banding is used | Mathematical + structural |
| **`R = S / M`** | **Sound, with one necessary condition: `M` must be a protective factor `≥ 1`, not a raw count.** On that reading it is algebraically identical to the industry standard `R = S(1 − CE)` | Boundary conditions + equivalence proof |
| **The booklet's wording on `M`** | **Correct and necessary.** "Number *and* effectiveness" is the only description that makes the divisor well-posed | Proved by the M = 0 failure |
| **Your reported `f = s·k` / `f = s/n`** | **Not internally coherent.** The symbol `s` would need two meanings; and "number of threats" in the denominator fails both the direction test and the zero case | Logical contradiction test |
| **Sharp's exact letters** | **Still unverified** — paywalled. But the *structure* is now settled independently of the letters | Honest limitation |

**The practical upshot for you:** the structure you should carry into the exam is

```text
risk              = frequency × consequences          (both must matter → multiply)
residual risk     = risk ÷ protection factor          (protection ≥ 1; never divides by zero)
```

and that holds regardless of which letters the book prints. If your notes show `S`, `F`, `K` and `R`, `S`, `M`, the booklet is reproducing the book and you can drill it as printed. **If your notes show something else, tell me and I will re-open this.**

---

## 7. What would close this completely

| # | Action | Who |
|:---:|:---|:---|
| 1 | Photograph the two equations from your lecture notes | You |
| 2 | Pull the chapter PDF via university library Springer access (ISBN 978-3-031-41463-3, chapter 3, pp. 37–56) | You, or me if you can get the file into the vault |
| 3 | If you can obtain the chapter PDF, drop it in `02_Raw_Materials/` and I will verify Sharp's exact letters and the two figures in one pass | Me |

---

*Mathematical and logical verification built 2026-09-23. The analysis in §2–§5 is independent of the paywalled source and stands on its own; §1 records the image-search attempts honestly, including the routes that failed and why.*
