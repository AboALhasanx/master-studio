---
title: "ASE Week 02 — BUILD PLAN (the commitment document)"
subject: "04_Advanced_Software_Eng"
week: 2
type: "binding build plan — the agent returns to this file every session"
status: "LOCKED — agreed with the student 2026-09-23"
created: "2026-09-23"
---

# ASE Week 02 — BUILD PLAN

> **This file is the contract.** Every time the agent works on ASE Week 02, it opens this file **first**, before writing anything. If the agent's output cannot be traced to a row in this plan, the agent has drifted.
>
> **The student's one change to the agreed plan:** the retrieval sets carry **questions and answers together in the same file**, not questions with answers withheld. Everything else stands.

---

## 1. The narrative spine — read this before any file

The ten files are **not ten separate topics**. They are ten chapters of **one argument**, and the argument comes from the source itself.

Sommerville states the chapter's own objective as: *"I understand **why processes should be organized to cope with changes in the software requirements and design**"* (Sommerville p.44). That is the thread.

**The one sentence the whole series is about:**

> **Requirements always change. Every process model is an answer to that one problem — and the models differ only in *when* and *how* they absorb the change.**

So the series reads as a story with a single escalating problem:

```text
Software is built by teams, not individuals.
        ↓
So you need a process at all — otherwise the project fails.          (File 01)
        ↓
The first answer: decide everything up front.                        (File 02)
        ↓
But requirements change. The up-front answer breaks.                 (File 02)
        ↓
Four responses to the break, in historical order:
   learn the requirements by building      → Prototyping            (File 03)
   deliver in slices and absorb change     → Incremental            (File 04)
   let the system evolve                   → Evolutionary           (File 03)
   compress the whole timeline             → RAD                    (File 05)
        ↓
Make risk the driver instead of the schedule.                        (File 06)
        ↓
Put it all together in one phased, iterative framework.              (File 07)
        ↓
Change the philosophy: people over process, cycles of weeks.         (File 08)
        ↓
Accept that no model wins — so learn to CHOOSE.                      (File 09)
        ↓
Everything side by side, plus the exam bank.                         (File 10)
```

**Rule:** every file opens with a **"Where this sits"** line that names the *previous* file and states *what problem this file is answering*. No file starts cold. That is what makes it a story instead of a list.

---

## 2. The ten files — detailed stage plan

Each file follows the same six-part shape (§4). The table below fixes the **content**, the **sources**, and the **narrative hand-off**.

### File 01 — SDLC Fundamentals: why a process exists at all

| | |
|:---|:---|
| **Problem it opens with** | A team is building software. Why can't each person just write their own part? |
| **Narrative hand-off to 02** | "We now know a process is needed. What should the first process look like? The obvious answer is: decide everything up front." |
| **Sub-topics** | software process definition · the four fundamental activities (specification, design & implementation, validation, evolution) · what a process description contains (products, roles, pre/post-conditions) · why a life-cycle model is needed · plan-driven vs agile as the two poles |
| **Primary source** | Sommerville p.44–46 (definition, four activities, plan-driven/agile) |
| **Supporting** | Mall p.67–71 (why a model is needed; the ad-hoc failure argument; why document the process) |
| **Retrieval set** | 6 items |

### File 02 — Build & Fix, and the Waterfall Family: the first answer and its failure

| | |
|:---|:---|
| **Problem it opens with** | What did people do *before* there was a process, and what did the first real process look like? |
| **Narrative hand-off to 03** | "Waterfall works — but only when requirements are stable. Ours are not. So the next four models are all attempts to fix that one weakness." |
| **Sub-topics** | build and fix / exploratory / code and fix (and why it fails at team scale) · classical waterfall: origin (Royce, 1970), the five stages, the critique · **iterative waterfall** and phase containment of errors · **the V-model** |
| **Primary source** | Mall §1.1.1 p.28 (build and fix); Mall §2.2.1–2.2.3 p.73–91 (classical, iterative, V-model) |
| **Supporting** | Sommerville p.47–49 (origin, five stages, the critique verbatim) |
| **Retrieval set** | 8 items |
| **[THIN] flag** | the V-model — Sommerville has no V-model at all; Mall is the only source |

### File 03 — Prototyping and the Evolutionary Model: learning by building

| | |
|:---|:---|
| **Problem it opens with** | We cannot write down the requirements up front. What if we build something to *discover* them? |
| **Narrative hand-off to 04** | "A prototype teaches us the requirements. But a prototype is thrown away. What if instead we delivered the real thing in pieces?" |
| **Sub-topics** | prototype definition · its two uses (requirements elicitation/validation; design exploration and UI) · the "not used the same way as the final system" problem · the evolutionary model · **iterative vs evolutionary — the distinction** |
| **Primary source** | Sommerville §2.3.1 p.62–63 (definition, uses, problem) |
| **Supporting** | Mall §2.2.4 p.91 (prototyping in the taxonomy); Mall §2.2.6 p.97 (evolutionary); Mall Q52 p.131 (iterative vs evolutionary) |
| **Retrieval set** | 7 items |
| **[THIN] flag** | the evolutionary model — absent from Sommerville entirely; Mall alone |

### File 04 — Incremental Development: delivering in slices

| | |
|:---|:---|
| **Problem it opens with** | What if we delivered working software early, in slices, and let each slice absorb change? |
| **Narrative hand-off to 05** | "Incremental absorbs change well — but it is slow and it degrades structure. If the deadline is the real constraint, you need a different answer." |
| **Sub-topics** | the definition (interleaves specification, development, validation) · the **three benefits** · the **two management problems** (process not visible; structure degrades) · incremental development vs incremental **delivery** · why it is the foundation of agile |
| **Primary source** | Sommerville p.47 (definition), p.50 (benefits), p.51 (problems, delivery distinction) |
| **Supporting** | Mall §2.2.5 p.95 |
| **Retrieval set** | 7 items |

### File 05 — RAD: compressing the timeline

| | |
|:---|:---|
| **Problem it opens with** | The schedule is the binding constraint. How do you go fast without going ad hoc? |
| **Narrative hand-off to 06** | "RAD buys speed by cutting planning and reusing code. But it has no mechanism for deciding *which* risk to attack first. That is what the spiral adds." |
| **Sub-topics** | motivation and goals · how RAD works (minimal planning + heavy reuse through rapid prototyping) · the specialised tools (visual development, reusable components) · **the time box** · **applicability conditions** — what suits RAD and what does not · comparison with other models · advantages/disadvantages vs prototyping and vs evolutionary |
| **Primary source** | **Mall §2.3–§2.3.3, p.100–104** — the only source |
| **Supporting** | Pressman p.60/76 and Agarwal p.62 (passing mentions only) |
| **Retrieval set** | 8 items |
| **[THIN] flag** | **Sommerville has nothing on RAD** — 0 relevant hits in 790 pages. This file cannot be checked against Sommerville at all |

### File 06 — The Spiral Model: making risk the driver

| | |
|:---|:---|
| **Problem it opens with** | Every model so far optimises for something — schedule, change, reuse. What if you optimised for *what could go wrong*? |
| **Narrative hand-off to 07** | "The spiral is powerful but it is a way of thinking, not a ready-made framework. The Unified Process tries to package that thinking into something a team can adopt." |
| **Sub-topics** | Boehm's spiral · the **four sectors** of each loop (objective setting; risk assessment and reduction; development and validation; planning) · the phases · risk-driven development, and what "risk" means informally · when **not** to use it · the deeper treatment |
| **Primary source** | Sommerville p.66–67 (four sectors; the "explicit recognition of risk" sentence) |
| **Supporting** | Mall §2.5–§2.5.1 p.114–116; Pressman p.64–68 (deepest); Mall Q41 p.130 |
| **Retrieval set** | 8 items |

### File 07 — The Unified Process: putting it together

| | |
|:---|:---|
| **Problem it opens with** | We have four good ideas. Can they be combined into one adoptable framework? |
| **Narrative hand-off to 08** | "UP is disciplined and complete — and it is heavy. For a small team with fast-changing requirements, even that is too much process." |
| **Sub-topics** | what UP is (incremental and iterative, for object-oriented development) · why it is a **hybrid** model · **the four phases — Mall's account and Sommerville's account shown side by side** · RUP's six best practices · the static workflows |
| **Primary source** | Mall §8.3.1 p.475–476 |
| **Supporting** | Sommerville §2.4 p.67–69 (phases, six best practices, workflows) |
| **Retrieval set** | 7 items |
| **Disagreement to preserve** | The two books describe **Elaboration differently**. Mall: requirements + preliminary use case + domain model. Sommerville: problem domain + architectural framework + project plan + **key project risks**. **Show both; do not merge.** |

### File 08 — Agile, XP and Scrum: changing the philosophy

| | |
|:---|:---|
| **Problem it opens with** | What if the problem is not the process but the assumption that we can plan at all? |
| **Narrative hand-off to 09** | "Agile is not the final answer either — it fails on critical systems. So the last question is not 'which is best' but 'which fits'." |
| **Sub-topics** | the agile definition (small increments, releases every two to three weeks, customer involvement, minimal documentation) · **the four manifesto statements** · agile vs other models · **Extreme Programming** · **Scrum** |
| **Primary source** | Sommerville p.75–76 (definition + manifesto) for the philosophy; Mall §2.4–§2.4.4 p.105–114 for XP and Scrum |
| **Retrieval set** | 9 items |
| **[THIN] flag** | Sommerville names XP and Scrum in one sentence each and defers; Mall is the substantive source for both |

### File 09 — Choosing a Model: no winner, only fit

| | |
|:---|:---|
| **Problem it opens with** | Ten models, no winner. So how does anyone actually decide? |
| **Narrative hand-off to 10** | "Now that we can choose, put them all side by side and check what you actually retained." |
| **Sub-topics** | the comparison of all models · the three factors that drive selection — **product, development team, customer** · requirements and risk as the two drivers · worked selection scenarios (the payroll case) · why final documentation is written as if waterfall had been used |
| **Primary source** | Mall §2.6 p.118 + exercises Q40, Q53, Q55 p.130–131 |
| **Supporting** | Sommerville p.46 (plan-driven vs agile; critical vs business systems) |
| **Retrieval set** | 9 items |

### File 10 — Master Comparison and Exam Bank

| | |
|:---|:---|
| **Problem it opens with** | Everything at once. |
| **Sub-topics** | every model in one comparison table · the complete retrieval bank (all files' sets, consolidated) · Mall's exercises mapped to the topics that answer them |
| **Source** | consolidation of Files 01–09 |
| **Retrieval set** | the consolidated bank |

---

## 3. Rules the agent commits to

These are binding. The student can hold the agent to any of them by quoting this section.

| # | Rule |
|:---:|:---|
| 1 | **Every claim carries a page anchor.** No anchor, no claim. |
| 2 | **Quotations stay verbatim** and are marked as quotations. Paraphrase is labelled as paraphrase. |
| 3 | **Where two sources disagree, both are shown.** Never merged, never silently picked. |
| 4 | **Unverified items are labelled unverified.** Never smoothed over. |
| 5 | **No invented citations.** Foundational claims are tagged `[Foundational Knowledge / Standard Concept]`. |
| 6 | **`[THIN]` flags** wherever the summary is thinner than the source. |
| 7 | **Every file opens with a "Where this sits" line** linking it to the previous file. |
| 8 | **Every file ends with its retrieval set, questions and answers together.** |
| 9 | **Page numbers are PDF page numbers**, not printed page numbers. The front-matter offset differs per book; stated once per file. |
| 10 | **No file is written without re-reading this plan first.** |

---

## 4. The file template

```text
┌─ COVER BLOCK ──────────────────────────────────────────────
│  Subject · Week · File N of 10 · Topic title
│  Source line (books + page range)
└────────────────────────────────────────────────────────────
┌─ WHERE THIS SITS ──────────────────────────────────────────
│  Previous file → the problem this file answers (2-3 lines)
└────────────────────────────────────────────────────────────
┌─ THE CONTENT ──────────────────────────────────────────────
│  English exposition, Arabic explanation beneath each concept
│  Terms stable across both languages
│  Page anchors inline. [THIN] flags where relevant.
└────────────────────────────────────────────────────────────
┌─ SOURCE NOTES ─────────────────────────────────────────────
│  Primary source · what each secondary adds · what adds nothing
└────────────────────────────────────────────────────────────
┌─ RETRIEVAL SET ────────────────────────────────────────────
│  N questions, each with its answer directly beneath
└────────────────────────────────────────────────────────────
┌─ PAGE ANCHORS ─────────────────────────────────────────────
│  The exact pages to revisit in the books
└────────────────────────────────────────────────────────────
```

**Language rule:** English carries the exposition and the exam-facing wording. Arabic carries the explanation of the idea. **Key terms appear in English and stay in English in both languages** — never translated inconsistently. The student's standing preference: *Arabic for the idea, English for the term.*

**Why both languages:** dual coding — the same concept reached through two encodings. And the exam is answered in English, so the English wording has to be the one that gets drilled.

---

## 5. Build order and progress

| # | File | Status |
|:---:|:---|:---|
| — | **This plan** | **done** |
| 01 | SDLC Fundamentals | **DONE** — `Week_02_File_01_SDLC_Fundamentals.md` |
| 02 | Build & Fix and the Waterfall Family | **DONE** — `Week_02_File_02_BuildFix_and_Waterfall_Family.md` |
| 03 | Prototyping and the Evolutionary Model | **DONE** — `Week_02_File_03_Prototyping_and_Evolutionary.md` |
| 04 | Incremental Development | **DONE** — `Week_02_File_04_Incremental_Development.md` |
| 05 | RAD | **DONE** — `Week_02_File_05_RAD.md` |
| 06 | The Spiral Model | **DONE** — `Week_02_File_06_The_Spiral_Model.md` |
| 07 | The Unified Process | **DONE** — `Week_02_File_07_The_Unified_Process.md` |
| 08 | Agile, XP and Scrum | **next** |
| 09 | Choosing a Model | not started |
| 10 | Master Comparison and Exam Bank | not started |
| — | **Merged document** | only after all ten exist |

---

## 6. What is deliberately NOT in this plan

| Excluded | Why |
|:---|:---|
| The V-model as a *separate file* | It is in Mall §2.2.3 but the lecture did not name it separately; it lives inside File 02. If the student wants it promoted to its own file, that is one line of change. |
| Cleanroom software engineering | Sommerville p.49 has it, but the lecture did not name it. Not in scope. |
| The full agile family (Crystal, DSDM, FDD, Adaptive Software Development) | Sommerville p.76 names them; the lecture named only XP and Scrum. Mentioned in passing in File 08, not taught. |
| Week 01 material | Separate file already exists. |

---

*Binding plan written 2026-09-23, agreed with the student. The agent opens this file before every ASE Week 02 session. If output cannot be traced to a row above, the agent has drifted and the student should say so.*
