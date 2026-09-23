---
title: "ASE Week 02 — Deep Term Analysis: which source is primary, and which is just repetition"
subject: "04_Advanced_Software_Eng"
week: 2
instructor: "Asst. Prof. Dr. Ali Fahim Ni'ma"
method: "verbatim extraction from the four staged textbooks, term by term, with a usefulness verdict per source"
created: "2026-09-23"
---

# ASE Week 02 — Deep Term Analysis

> **What this is.** You asked for the lecture's terms checked *deeply*: find the **primary** source literally, then judge what each **secondary** source actually adds — and which ones are only re-explaining. Every quotation below was pulled verbatim out of the PDFs in `02_Raw_Materials/`, with the page number. Nothing is paraphrased from memory.

---

## 0. The headline finding — the primary source is not the obvious one

I assumed Sommerville would be the backbone. **It is not.** The lecture's term list maps almost one-to-one onto **Mall, chapter 2** — and two of your terms do not exist in Sommerville *at all*.

| Your lecture term | Mall ch. 2 | Sommerville ch. 2 |
|:---|:---|:---|
| Build & Fix | **§1.1.1, p.28** | **absent — 0 hits in 790 pages** |
| Classical Waterfall | **§2.2.1, p.73** | p.47 |
| **Iterative** Waterfall | **§2.2.2, p.83** | absent as a named model |
| V-Model | **§2.2.3, p.88** | absent |
| Prototyping | **§2.2.4, p.91** | p.62 |
| Incremental | **§2.2.5, p.95** | p.50 |
| **Evolutionary** | **§2.2.6, p.97** | absent as a named model |
| **RAD + applicability** | **§2.3 / §2.3.2, p.100–104** | **absent — 0 relevant hits** |
| Agile | **§2.4, p.105** | ch.3, p.75 |
| Extreme Programming | **§2.4.3, p.110** | p.76 (name only) |
| Scrum | **§2.4.4, p.114** | p.76 (name only) |
| Spiral | **§2.5, p.114** | p.66 |
| **Comparison of all models** | **§2.6, p.118** | scattered |
| Unified Process phases | **§8.3.1, p.475–476** | §2.4, p.67–68 |

**Verdict: Mall chapter 2 is the primary source for this lecture.** Sommerville is the *secondary* — better on definitions, process theory, the agile manifesto, and RUP depth, but silent on Build & Fix, RAD, the V-Model, and the Evolutionary model.

**This is the single most useful thing in this document.** If you study only Sommerville, you will miss Build & Fix, RAD and its applicability conditions — and the lecture named both explicitly.

---

## 1. Term-by-term deep analysis

### 1.1 — SDLC / software process

**Primary — Sommerville p.45, verbatim:**
> "A **software process** is a set of related activities that leads to the production of a software product."

And the four activities every process must include (Sommerville p.45):
1. **Software specification** — "The functionality of the software and constraints on its operation must be defined."
2. **Software design and implementation** — "The software to meet the specification must be produced."
3. **Software validation** — "The software must be validated to ensure that it does what the customer wants."
4. **Software evolution** — "The software must evolve to meet changing customer needs."

Sommerville adds that a process description also carries **products, roles, and pre-/post-conditions** (p.45).

**Primary — Mall p.67–70:** the SDLC framing and *why* a life-cycle model is needed at all. Mall's argument is practical: a single programmer on a small program can succeed with build-and-fix, but *"use of a suitable SDLC is essential for a professional software development project involving team effort to succeed"* (p.71).

**Secondary verdict:**
| Source | Adds? |
|:---|:---|
| **Sommerville** | **Yes — essential.** The four fundamental activities are the backbone of the whole chapter. |
| **Mall** | **Yes — different angle.** Why you need a model at all, plus the "why document the process" argument (p.71). |
| **Pressman / Agarwal** | **No.** Both restate the same four phases with no new content. |

---

### 1.2 — Build & Fix

**Primary — Mall p.28, verbatim:**
> "The early programmers used an ad hoc programming style. This style of program development is now variously being referred to as **exploratory, build and fix, and code and fix** styles."
>
> "In a **build and fix** style, a program is quickly developed **without making any specification, plan, or design**. The different imperfections that are subsequently noticed are fixed."

Mall's judgement (p.70): *"ad hoc development turns out to be a sure way to have a failed project."*

**Secondary verdict:**
| Source | Adds? |
|:---|:---|
| **Sommerville** | **Nothing — the term does not appear once in 790 pages.** |
| **Pressman** | **Nothing — 0 hits.** |
| **Agarwal** | **Nothing — 0 hits.** |

**Verdict: Mall is the only source you have.** Note the three synonyms — *exploratory · build and fix · code and fix* — because a question could use any of them.

---

### 1.3 — Waterfall

**Primary — Sommerville p.47, verbatim:**
> "The first published model of the software development process was derived from more general system engineering processes **(Royce, 1970)**. Because of the cascade from one phase to another, this model is known as the **'waterfall model' or software life cycle**. The waterfall model is an example of a **plan-driven process** — in principle, you must plan and schedule all of the process activities before starting work on them."

The five stages (Sommerville p.48): Requirements analysis and definition · System and software design · Implementation and unit testing · Integration and system testing · Operation and maintenance.

**And the critique, verbatim (p.49):**
> "Its major problem is the **inflexible partitioning of the project into distinct stages**. Commitments must be made at an early stage in the process, which makes it difficult to respond to changing customer requirements. In principle, the waterfall model should only be used when the **requirements are well understood and unlikely to change radically**."

**Primary — Mall §2.2.2, p.83: the Iterative Waterfall Model.** This is a **separate named model in Mall** and Sommerville does not have it. Your lecture said *"Incremental and **Iterative** Enhancement"* — so this section is on your syllabus and **Sommerville cannot teach it to you**.

**Secondary verdict:**
| Source | Adds? |
|:---|:---|
| **Sommerville** | **Yes** — the definition, the origin (Royce 1970), the five stages, and the critique. |
| **Mall** | **Yes — and irreplaceable** — the **iterative waterfall** variant, plus Mall's exercise Q45: *"What are the major shortcomings of the iterative waterfall model?"* |
| **Pressman** | **Thin** — only 4 pages mention waterfall, versus 17 in Sommerville. |
| **Agarwal** | **Partial** — 13 pages, but it is an introductory text and repeats Sommerville. |

---

### 1.4 — Incremental and Iterative

**Primary — Sommerville p.47, verbatim definition:**
> "**Incremental development** — This approach **interleaves the activities of specification, development, and validation**. The system is developed as a **series of versions (increments)**, with each version adding functionality to the previous version."

**Three benefits, verbatim (p.50):**
1. "The cost of accommodating changing customer requirements is reduced."
2. "It is easier to get customer feedback on the development work that has been done."
3. "More rapid delivery and deployment of useful software to the customer is possible, even if all of the functionality has not been included."

**Two management problems, verbatim (p.51):**
1. "The process is **not visible**. Managers need regular deliverables to measure progress."
2. "**System structure tends to degrade** as new increments are added. Unless time and money is spent on refactoring to improve the software, regular change tends to corrupt its structure."

**Secondary verdict:**
| Source | Adds? |
|:---|:---|
| **Sommerville** | **Yes — the best source.** Definition, 3 benefits, 2 problems, and the note that it "is now the most common approach for the development of application systems" (p.51). |
| **Mall §2.2.5, p.95** | **Yes — and this is the gap Sommerville leaves:** Mall's exercise Q52 asks *"Identify the major differences between the **iterative** and **evolutionary** SDLCs."* Sommerville does not draw that distinction. **You need Mall for it.** |
| **Pressman / Agarwal** | **No.** Both repeat the benefits list. |

---

### 1.5 — RAD (and applicability conditions)

**Primary — Mall §2.3, p.100–104.** Your lecture's phrase *"RAD and applicability conditions"* maps **exactly** onto Mall's §2.3.2 **"Applicability of RAD Model"** (p.102). This is not a coincidence — the doctor is reading from Mall here.

Mall's RAD in its own words:
- **How it works:** *"The decrease in development time and cost, and at the same time an increased flexibility to incorporate changes are achieved in the RAD model in two main ways — **minimal use of planning** and **heavy reuse of any existing code** through **rapid prototyping**."* (p.102)
- **The tools RAD advocates:** *"Visual style of development"* and *"Use of reusable components"* (p.102)
- **Applicability (p.102–103):** suitability is signalled by characteristics such as **customised software** — *"a customised software is developed for one or two customers only by adapting an existing software"* — and Mall adds more characteristics after this.
- **Time box:** discussed at Mall p.101, and it is an exam question (Q48a: *"What is a time box in a RAD model?"*).

**Secondary verdict:**
| Source | Adds? |
|:---|:---|
| **Mall** | **Irreplaceable.** The only source with RAD, the applicability conditions, the comparison, and the time box. |
| **Sommerville** | **Nothing.** Sommerville's two "rapid application development" hits are on p.398 and p.760, in unrelated contexts. **Sommerville will not teach you RAD.** |
| **Pressman p.60, p.76** | **Marginal** — two mentions, no treatment. |
| **Agarwal p.62** | **Marginal** — one mention. |

---

### 1.6 — Evolutionary

**Primary — Mall §2.2.6, p.97.** A named model in Mall's taxonomy, sitting between Incremental (§2.2.5) and RAD (§2.3).

**Secondary verdict:**
| Source | Adds? |
|:---|:---|
| **Sommerville** | **Nothing — there is no "evolutionary model" as a named model.** Sommerville covers incremental development and prototyping separately and never groups them as "evolutionary". |
| **Mall** | **The only source.** And note Q52 again — the **iterative vs evolutionary** distinction is an exam-shaped question that only Mall sets up. |

---

### 1.7 — Prototyping

**Primary — Sommerville §2.3.1, p.62, verbatim definition:**
> "A **prototype** is an **initial version of a software system** that is used to **demonstrate concepts, try out design options, and find out more about the problem and its possible solutions**."

Two uses (p.62):
1. "In the requirements engineering process, a prototype can help with the **elicitation and validation of system requirements**."
2. "In the system design process, a prototype can be used to **explore particular software solutions** and to support **user interface design**."

**And the general problem, verbatim (p.63):** *"a general problem with prototyping is that the prototype may not necessarily be used in the same way as the final system."*

**Secondary verdict:**
| Source | Adds? |
|:---|:---|
| **Sommerville** | **Yes — the crispest definition and the sharpest caveat.** |
| **Mall §2.2.4, p.91** | **Yes** — it places prototyping correctly in the model taxonomy, which is what the lecture's ordering implies. |
| **Agarwal p.54–58** | **Partial** — the longest prototyping treatment (22 pages of hits) but an introductory level. Useful only if you want more examples. |

---

### 1.8 — Spiral (and risk-driven development)

**Primary — Sommerville p.66–67.** Boehm's spiral (©IEEE 1988), and the four sectors of each loop, verbatim:
1. **Objective setting** — "Specific objectives for that phase of the project are defined… Project risks are identified."
2. **Risk assessment and reduction** — "For each of the identified project risks, a detailed analysis is carried out. Steps are taken to reduce the risk."
3. **Development and validation** — "After risk evaluation, a development model for the system is chosen."
4. **Planning** — "The project is reviewed and a decision made whether to continue with a further loop of the spiral."

**The sentence that carries the marks (p.67):**
> "The **main difference between the spiral model and other software process models is its explicit recognition of risk**."

**Secondary verdict:**
| Source | Adds? |
|:---|:---|
| **Sommerville** | **Yes — the four sectors and the one-line differentiator.** Best for the exam. |
| **Pressman p.64–68** | **Yes — the most detail** (20 pages of hits). Read this if you want depth beyond the exam. |
| **Mall §2.5 / §2.5.1, p.114–116** | **Yes — and it supplies an exam question Sommerville does not:** Q41 *"Explain why it may not be prudent to use the spiral model in the development of any large software."* |

---

### 1.9 — Unified Process phases — **the sources disagree**

Both of your books give the four phases. **They describe them differently.** This is a real finding, not a detail.

| Phase | **Mall p.476** | **Sommerville p.68** |
|:---|:---|:---|
| **Inception** | "the **scope of the project** is defined and **prototypes** may be developed to form a clear idea about the project" | business case — *"assess the contribution that the system makes to the business. If this contribution is minor, then the project may be cancelled after this phase"* |
| **Elaboration** | "the **functional and non-functional requirements are captured**. The **preliminary use case and the domain model** are developed" | "develop an understanding of the **problem domain**, establish an **architectural framework**, develop the **project plan**, and identify **key project risks**" |
| **Construction** | "the **design and implementation** activities are carried out… features implemented in a series of short iterations and tested. Each iteration results in an **executable release**" | "**system design, programming, and testing**. Parts of the system are developed **in parallel** and integrated during this phase" |
| **Transition** | "the product is **installed in the user's environment and maintained**" | "moving the system from the **development community to the user community**… something that is **ignored in most software process models** but is, in fact, an expensive and sometimes problematic activity" |

**Verdict:** Mall is *requirements-and-use-case* framed; Sommerville is *risk-and-architecture* framed. **Read both.** If the doctor asks "what happens in Elaboration", the two books give you different answers — and Sommerville's version ties Elaboration to **risk**, which matches the lecture's emphasis on risk-driven development.

Mall also gives the one-line definition (p.475): *"Unified process is incremental [and] iterative process model for object-oriented software development."* And Sommerville's framing (p.67): *"a good example of a **hybrid** process model. It brings together elements from all of the generic process models."*

---

### 1.10 — Life-cycle selection by requirements and risk

**Primary — Mall §2.6, p.118: "A Comparison of Different Life Cycle Models."** This section exists to answer exactly this question.

**And Mall's exercise Q53 states the exam question outright:**
> *"Explain how the characteristics of the **product**, the **development team**, and the **customer** influence the selection of an appropriate SDLC for a project."*

Plus Q40 (choose a model for a payroll project and justify), Q55 (*"the important factors that influence the choice of a suitable SDLC model"*), and Q46 (which projects suit the V-model).

**Primary — Sommerville p.46, verbatim:**
> "Sometimes, software processes are categorized as either **plan-driven** or **agile** processes… As Boehm and Turner (2003) discuss, **each approach is suitable for different types of software**. Generally, you need to find a balance."

And p.46: *"For critical systems, a very structured development process is required. For business systems, with rapidly changing requirements, a less formal, flexible process is likely to be more effective."*

**Verdict:** **Sommerville gives you the principle; Mall gives you the comparison table and the exam question.** Use Mall §2.6 as the spine, Sommerville p.46 for the plan-driven/agile framing.

---

### 1.11 — Agile

**Primary — Sommerville ch.3 p.75, verbatim definition:**
> "**Agile methods are incremental development methods in which the increments are small** and, typically, new releases of the system are created and made available to customers **every two or three weeks**. They involve customers in the development process to get rapid feedback on changing requirements. They **minimize documentation** by using informal communications rather than formal meetings with written documents."

**The manifesto, verbatim (p.76)** — worth memorising because it is quotable:
> - **Individuals and interactions** over processes and tools
> - **Working software** over comprehensive documentation
> - **Customer collaboration** over contract negotiation
> - **Responding to change** over following a plan

Sommerville adds the qualifier: *"while there is value in the items on the right, we value the items on the left more."*

**Secondary verdict:**
| Source | Adds? |
|:---|:---|
| **Sommerville** | **Yes — the manifesto is here and nowhere else.** Best source for the definition and the values. |
| **Mall §2.4.1–2.4.2, p.107–109** | **Yes — "Agile versus Other Models"** is the comparison your lecture's structure implies. |
| **Pressman / Agarwal** | **No.** |

---

### 1.12 — Extreme Programming (XP)

**Primary — Mall §2.4.3, p.110–113** (4 pages of substantive treatment).
**Sommerville p.76** — names it only: *"Probably the best-known agile method is **extreme programming** (Beck, 1999; Beck, 2000)"*, then defers to a later chapter.

**Secondary verdict:**
| Source | Adds? |
|:---|:---|
| **Mall** | **Yes — the substantive source.** |
| **Sommerville** | **Marginal for XP** — one sentence plus a pointer. |
| **Pressman** | **Nothing — 0 hits for "extreme programming".** Pressman's edition predates the agile content. |

---

### 1.13 — Scrum

**Primary — Mall §2.4.4, p.114.**
**Sommerville p.76** — names it only: *"Other agile approaches include **Scrum** (Cohn, 2009; Schwaber, 2004; Schwaber and Beedle, 2001), Crystal…"*

**Secondary verdict:**
| Source | Adds? |
|:---|:---|
| **Mall** | **Yes — the substantive source.** |
| **Sommerville** | **Marginal** — the name and the references. |
| **Pressman** | **Nothing — 0 hits for "scrum".** |

---

## 2. The noise list — sources that only re-explain

Ranked by how little they add for *this* lecture:

| Source | Verdict |
|:---|:---|
| **Pressman** | **The weakest fit.** Zero hits for Build & Fix, Scrum and Extreme Programming. Only 4 pages on waterfall. It is a strong general text, but for **this** topic list it is mostly repetition. Use it only for the Spiral (p.64–68), where it is genuinely the deepest. |
| **Agarwal** | **An introductory text.** 529 pages, thinner treatment throughout. Useful only as a third opinion on prototyping (p.54–58). Otherwise it restates Sommerville. |
| **Sommerville on Build & Fix, RAD, V-Model, Evolutionary** | **Silent.** Not a criticism of the book — those are simply not its taxonomy. But it means Sommerville alone cannot cover your lecture. |
| **Mall on the agile manifesto** | **Silent.** Mall covers agile methods and the XP/Scrum detail, but the four manifesto statements are Sommerville's. |

**The useful rule that falls out of this:** for this lecture, **Mall is the model taxonomy and Sommerville is the theory and the quotable definitions.** They are complementary, not redundant. Pressman and Agarwal are optional.

---

## 3. The hidden exam bank — Mall's exercise set, pp.130–131

This is the most valuable single find in the whole analysis. Mall's end-of-chapter exercises are **written in exactly the form a professor would ask**, and they cover your lecture's terms:

| Q | Question (verbatim, abbreviated) | Covers |
|:---:|:---|:---|
| 40 | A company experienced in payroll software gets a request from a customer still processing payroll manually. *"Which life cycle model should be used? Justify your answer."* | **Life-cycle selection** |
| 41 | *"Explain why it may not be prudent to use the **spiral** model in the development of any large software."* | Spiral |
| 44 | *"why is it necessary for the final documents to describe the software as if it were developed using the classical waterfall model?"* | Waterfall |
| 45 | *"What are the major shortcomings of the **iterative waterfall** model? Name the life cycle models that overcome any of the specific shortcomings."* | Iterative waterfall |
| 46 | *"For which types of development projects is the **V-model** appropriate? … point out its strengths and weaknesses."* | V-Model |
| 47 | *"Identify the main motivation and goals behind the development of the **RAD** model. How does the model help achieve the identified goals?"* | RAD |
| 48 | *"Explain… **What is a time box in a RAD model?** How does RAD facilitate…"* | RAD |
| 52 | *"Identify the major differences between the **iterative** and **evolutionary** SDLCs."* | Iterative vs Evolutionary |
| 53 | *"Explain how the characteristics of the **product**, the **development team**, and the **customer** influence the selection of an appropriate SDLC."* | Life-cycle selection |
| 54 | RAD: life-cycle activities · late change requests · faster development · two suitable projects · **advantages and disadvantages vs prototyping and vs evolutionary** · one disadvantage vs iterative waterfall · characteristics that suit / do not suit RAD | **RAD, exhaustively** |
| 55 | *"the important factors that influence the choice of a suitable SDLC model"* | Life-cycle selection |

**Q54 alone is a full exam paper on RAD.** If the doctor's question on RAD looks anything like this, Mall pp.100–104 answers it.

---

## 4. What to actually read, in order

| Priority | Read | Why |
|:---:|:---|:---|
| **1** | **Mall §2.2 → §2.6, pp.73–135** | The model taxonomy, in the lecture's own order. Covers everything except the agile manifesto. |
| **2** | **Mall §2.3.2, p.102–103** | The RAD **applicability conditions** — a phrase straight out of your lecture. |
| **3** | **Mall §2.6, p.118 + exercises Q40/53/55, p.130–131** | Life-cycle selection, in exam form. |
| **4** | **Sommerville p.45–51** | The process definition, the four fundamental activities, waterfall's five stages and its critique, incremental's 3 benefits and 2 problems. |
| **5** | **Sommerville p.66–67** | The spiral's four sectors and the "explicit recognition of risk" sentence. |
| **6** | **Sommerville p.75–76** | Agile definition + the manifesto — quotable, and not in Mall. |
| **7** | **Mall §8.3.1, p.475–476 + Sommerville p.67–68** | Unified Process phases — read **both**, they differ. |
| **8** | **Pressman p.64–68** | Only if you want spiral depth beyond the exam. |
| — | **Skip for this lecture** | Pressman and Agarwal generally; Sommerville for Build & Fix / RAD / V-Model / Evolutionary (they are not there). |

---

## 5. Two cautions

1. **No lecture slides were delivered for Week 02.** The nine-term list came from your own report, not from a file the doctor distributed. So the mapping above is *my* inference from the term wording to the books — a strong inference, since phrases like "applicability of RAD" and "iterative waterfall" are Mall's own section headings, but still an inference.
2. **Page numbers are PDF page numbers**, not printed page numbers. They will be off by the front-matter offset in each book.

---

*Deep term analysis built 2026-09-23. Every quotation above was extracted verbatim from the PDFs in `02_Raw_Materials/`; every "absent / 0 hits" claim is a full-text search over the whole book, not an impression.*
