---
marp: true
theme: gaia
paginate: true
header: "Advanced Software Engineering (CS603) — University of Wasit"
footer: "Lecture 01: Foundations, Failures & Software Crisis | Asst. Prof. Dr. Ali Fahim Ni'ma"
style: |
  section {
    font-family: 'Segoe UI', Arial, sans-serif;
    background-color: #f8fafc;
    color: #0f172a;
  }
  h1 { color: #1e3a8a; }
  h2 { color: #1e40af; }
  table { font-size: 0.72em; }
  th { background-color: #1e3a8a; color: white; }
---

<!-- _class: lead -->
# 🏗️ Foundations of Software Engineering & The Software Crisis
## Lecture 01: Systems Evolution, Catastrophic Failures, and Academic Taxonomy

**Candidate:** Master of Computer Science Student  
**Instructor:** Asst. Prof. Dr. Ali Fahim Ni'ma  
**Institution:** College of Computer Science & IT — University of Wasit  
**Date:** September 2026

---

## 🎯 The Dual Role & Socio-Technical Nature of Software

* **Dual Essence of Modern Software:**
  1. **Software as a Product:** Transforms data, executes business logic, and powers cyber-physical devices.
  2. **Software as a Vehicle:** Acts as the operational platform controlling hardware, operating systems, and communications infrastructure.
* **The Socio-Technical Reality (Sommerville):**
  * Software does not operate in an abstract mathematical bubble.
  * A complete system includes **code**, **operational processes**, and **human psychology**.
  * Organizational misalignments cause catastrophic system collapses just as easily as runtime exceptions.

---

## 💥 Case Study: Dhahran Patriot Missile Failure (1991)

* **The Disaster:** On Feb 25, 1991, an Iraqi Scud missile struck US barracks in Dhahran, killing 28 soldiers after the Patriot battery failed to engage.
* **The Mathematical Root Cause:**
  * System clock incremented in integer tenths of a second ($0.1\text{ s}$).
  * Converted to seconds by multiplying by a **24-bit fixed-point register** truncation of $1/10$.
  * Truncation error: $\Delta t \approx 0.000000095\text{ seconds per tick}$.
* **Cumulative Drift over 100 Hours:**
  $$\text{Total Drift} = 3,600,000 \times 0.000000095367\text{ s} \approx \mathbf{0.3433\text{ seconds}}$$
* **Tracking Consequence:**
  Scud traveling at Mach 5 ($1,676\text{ m/s}$) $\rightarrow$ Radar Range Gate shifted by **~687 meters**! The radar looked where the missile was half a kilometer earlier.

---

## 🐺 Brooks' Thesis: "No Silver Bullet" (1986)

> *"There is no single development, in either technology or management technique, which by itself promises even one order of magnitude ($10\times$) improvement in productivity, in reliability, in simplicity, within a decade."*

```
                           SOFTWARE COMPLEXITY
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
   ESSENTIAL COMPLEXITY                             ACCIDENTAL COMPLEXITY
(Inherent to the problem domain)               (Associated with implementation tools)
- Complexity (non-linear scaling)              - Clumsy language syntax
- Conformity (arbitrary human rules)           - Slow manual compilers & linkers
- Changeability (malleability pressure)        - Manual memory management
- Invisibility (unvisualizable topology)       - Primitive debuggers
```

* High-level languages and IDEs eliminated **accidental** complexity.
* The remaining core difficulty is **essential** complexity, which tools cannot automate away.

---

## 📦 What Software Truly Is: The Tripartite Asset

Software is **not** merely executable code written by a programmer.

$$\mathbf{Software} = \mathbf{Programs} + \mathbf{Data\ Structures} + \mathbf{Documentation}$$

1. **Programs (Code):**
   * High-quality, modular, testable, and maintainable source code and build scripts.
2. **Data Structures:**
   * Schemas, state representations, relational and in-memory data representations.
3. **Comprehensive Documentation:**
   * **System / Architecture:** Requirements (SRS), Architectural Views (IEEE 42010), ADRs.
   * **Operations:** Deployment pipelines, disaster recovery runbooks, telemetry specifications.
   * **User:** Operational manuals, training guides, and API contracts.

---

## 🏛️ Defining Software Engineering & The Software Process

* **IEEE Standard 610.12 Definition:**
  > *"The application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering to software."*

* **The Four Universal Process Activities:**
  1. **Specification:** Defining system capabilities and operational boundaries.
  2. **Development:** Architectural design, decomposition, and component coding.
  3. **Validation:** Verification (*Building the product right?*) & Validation (*Building the right product?*).
  4. **Evolution:** Adapting software to changing operational, security, and market requirements.

---

## ⚠️ The Software Crisis: Genesis & The IBM OS/360 Lessons

* **Coined at NATO Conference (Garmisch, 1968):**
  * Software projects chronically over budget ($200\%\text{--}500\%$), years behind schedule, and untrustworthy.
  * Maintenance costs escalating to consume $70\%\text{--}80\%$ of total IT budgets.
* **The IBM System/360 Experience (Fred Brooks):**
  * Consumed **5,000+ man-years** and over **$50,000,000**.
  * Suffered years of schedule delays and thousands of latent defect releases.
* **Brooks' Law:**
  > *"Adding human resources to a late software project makes it later."*
  * New developers require training from existing experts.
  * Inter-team communication channels grow quadratically: $C = \frac{N(N-1)}{2}$.

---

## 🎭 Debunking Software Myths

| Category | Persistent Industry Myth | Empirical Software Engineering Reality |
|---|---|---|
| **Management** | *"If we fall behind schedule, we can just hire more programmers."* | **Brooks' Law:** Increases communication overhead and training drag, causing further delay. |
| **Customer** | *"A vague general objective is enough; we can work out details later."* | Ambiguous requirements are the #1 cause of software failure and architectural rework. |
| **Developer** | *"Once the code compiles and runs, our job as engineers is complete."* | Post-delivery maintenance accounts for $60\%\text{--}80\%$ of the entire system lifecycle cost. |
| **Developer** | *"The working program is the only deliverable that matters."* | Code without documentation is a maintenance disaster that guarantees technical bankruptcy. |

---

## 🔬 Core Terminology Taxonomy: Dependability Chain

Under formal IEEE 610.12 and Laprie / Avižienis standards:

```
[Human Action]             [Static Artifact]            [Runtime State]           [Observable Service]
┌─────────────┐            ┌────────────────┐           ┌──────────────┐          ┌───────────────────┐
│    ERROR    │   causes   │ FAULT / DEFECT │ activates │INTERNAL ERROR│ manifests│      FAILURE      │
│(Mental slip)│ ─────────> │ (Dormant flaw) │ ────────> │(Invalid state│ ───────> │(Deviation from    │
└─────────────┘            └────────────────┘           └──────────────┘          │ specified service)│
                                                                                  └───────────────────┘
```

* **Error:** Cognitive human mistake or oversight.
* **Fault / Defect:** Static flaw residing silently in code or documentation.
* **Failure:** Dynamic event where delivered service deviates from expected specification during execution.

---

## ⚖️ Professional Ethics & Open Defense Viva Questions

* **ACM/IEEE Code of Ethics (8 Core Principles):**
  1. Public &middot; 2. Client/Employer &middot; 3. Product &middot; 4. Judgment &middot; 5. Management &middot; 6. Profession &middot; 7. Colleagues &middot; 8. Self.

### ❓ Open Viva Defense Questions (Dr. Ali Fahim):
1. *"How does the Patriot missile failure demonstrate that software maintenance is often more hazardous than initial greenfield development?"*
2. *"Why does Brooks argue that solving accidental complexity (e.g. AI code generation, higher-level frameworks) will never eliminate the software crisis?"*
3. *"Under the ACM/IEEE code of ethics, what is an engineer's professional duty when pressured by management to ship software with known latent faults?"*
