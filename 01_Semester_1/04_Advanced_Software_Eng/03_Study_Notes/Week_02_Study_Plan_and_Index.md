---
title: "ASE Week 02 — Study Method Report + Build Plan & Index"
subject: "04_Advanced_Software_Eng"
week: 2
type: "methodology report + plan"
created: "2026-09-23"
---

# Part A — Methodology report: is this approach sound?

You proposed: **index first → numbered per-topic files → merge into one document at the end**, with each file standalone and a consistent cover. You asked whether the method is good, and you asked me to research it rather than opine.

**Short answer: the structure is right, and one thing is missing. Without that one thing, the plan becomes a false-confidence machine — and there is direct evidence for that, with numbers.**

---

## A.1 What the evidence supports

**1. Plan/index first — supported.** This is Ausubel's **advance organizer**, and it has a 2025 systematic review behind it. The mechanism is that new information is linked to a pre-existing cognitive structure; giving the structure *before* the content gives the material something to attach to. Your instinct to build the فهرست first is correct and evidence-backed.

**2. Splitting into per-topic chunks — supported.** Segmenting content into learner-controlled parts is a long-standing finding in multimedia-learning research (Mayer's segmenting principle) and it is consistent with cognitive load theory: a smaller working set per sitting, with the learner controlling the pace. **[Foundational Knowledge / Standard Concept]** — the segmenting principle itself is well established, but I did not retrieve a single clean citable study for it in this session, so I am tagging it rather than quoting a number.

**3. Merging at the end — supported, for a specific reason.** A merged document is the right artefact for **spaced review** later, and the spacing effect is one of the two most robust findings in the learning literature. Per-topic files are for *learning*; the merged document is for *revisiting*. Your plan has both. Good.

---

## A.2 What the evidence says is missing — and it is not a small thing

There is a 2026 study specifically on your exact risk: *"The Illusion of Mastery in AI-Assisted Learning: Do AI-Generated Summaries Create False Confidence?"* (IJERT Vol. 15 Issue 5, DOI 10.5281/zenodo.20522459).

It compared students who studied from AI-generated summaries against students who studied from the book. **The AI group did worse and felt better.**

| Metric | AI-summary group | Book group |
|:---|:---:|:---:|
| Confidence (out of 10) | **8.0** | 6.5 |
| Actual score (out of 30) | **15.5** | 20.0 |
| **Calibration gap** (confidence minus reality) | **8.75** | 3.5 |

And the performance gap **widens as the questions get harder** — which is the part that should worry you:

| Question type | AI group | Book group | Gap |
|:---|:---:|:---:|:---:|
| Factual recall (/10) | 7.0 | 7.5 | **small** |
| Procedural (/10) | 5.0 | 7.0 | moderate |
| **Analytical (/10)** | **3.5** | **5.5** | **largest** |

**Read that third row again.** AI summaries were nearly as good as the book for **factual recall** — and clearly worse for **analytical** questions. Your ASE exam, by Dr. Ali Fahim's known style, is built on **exact numerical modelling and analytical reasoning**, not recall. The study predicts the plan as stated would hurt you most exactly where you are graded hardest.

**The authors' own framing is fair, and worth quoting:** *"The problem is not simply the AI tool itself, but the way people use it."* AI summaries are fine **for gaining an overview or preparing before deeper study**. The harm starts *"when students replace actual learning and active engagement with only reading AI-generated summaries."*

**And the single most useful finding for us:** the AI-group students who **followed the citations back to the source material scored higher** — the two top scorers in that group followed the most source links. Source engagement partially compensates.

---

## A.3 So here is my verdict on your plan

| Your proposal | Verdict |
|:---|:---|
| Index/plan first | **Agree** — evidence-backed (advance organizer) |
| Numbered per-topic files | **Agree** — segmenting; also matches how the vault already works |
| Consistent cover, not a different design per file | **Agree** — and it makes the merge trivial |
| Merge everything at the end | **Agree** — that is the spaced-review artefact |
| **"You write the notes, I read them"** | **Disagree as stated.** This is the one place the evidence is against us |

**The fix is small and it has to be built into the files, not bolted on at the end:**

1. **Every topic file ends with retrieval questions, with the answers withheld.** Not optional. The study recommends post-reading retrieval quizzes specifically as a *calibration intervention* — they correct inflated confidence.
2. **Every file carries page anchors to the sources**, so you can and should go back to the book on the contested or high-stakes items. This is the finding that the top AI-group students scored higher by doing exactly this.
3. **Every file flags where compression loses information.** The study recommends "confidence tagging — flag high-complexity or contested areas unlikely to be captured in a brief summary." I will mark those `[THIN]` where my summary is thinner than the source.
4. **The merged document is for review, not first contact.** Learn from the numbered files; revisit with the merged one.

---

## A.4 On your hallucination worry

You are right to raise it, and you are right about why. The controls I will apply, stated up front so you can hold me to them:

- **Every claim carries a page anchor.** No anchor, no claim.
- **Quotations stay verbatim** and are marked as quotations. If I paraphrase, I say so.
- **Where two sources disagree, both are shown** — as with the Unified Process Elaboration phase, where Mall and Sommerville give different accounts.
- **Where I could not verify something, it is labelled unverified**, not smoothed over.
- **No invented citations.** If a claim is foundational rather than sourced, it gets `[Foundational Knowledge / Standard Concept]` — as used in §A.1 above.

---

# Part B — The build plan

## B.1 Division

**Ten numbered files**, following the lecture's own division. One deviation, flagged: your lecture bundled *"Evolutionary and Prototyping"* into one item, but the sources treat them as **two different models** (Mall has Prototyping at §2.2.4 and the Evolutionary Model separately at §2.2.6). I split them, because the distinction between them is itself an exam question (Mall Q52).

| # | File | Sub-topics | Primary source |
|:---:|:---|:---|:---|
| **01** | SDLC Fundamentals | software process definition · the four fundamental activities · products/roles/pre-post-conditions · why a life-cycle model is needed · plan-driven vs agile | Sommerville p.45–46; Mall p.67–71 |
| **02** | Build & Fix, and the Waterfall Family | build and fix / exploratory / code and fix · classical waterfall (origin, 5 stages, critique) · **iterative waterfall** · **V-model** | Mall §1.1.1 p.28, §2.2.1–2.2.3 p.73–91; Sommerville p.47–49 |
| **03** | Prototyping and the Evolutionary Model | prototype definition · its two uses · the "not used the same way" problem · evolutionary model · **iterative vs evolutionary** | Sommerville p.62–63; Mall §2.2.4 p.91, §2.2.6 p.97 |
| **04** | Incremental Development | definition · 3 benefits · 2 management problems · incremental delivery vs development · why it underpins agile | Sommerville p.47, 50–51; Mall §2.2.5 p.95 |
| **05** | RAD | motivation and goals · how RAD works · **time box** · **applicability conditions** · comparison with other models · advantages/disadvantages vs prototyping and vs evolutionary | **Mall §2.3–2.3.3, p.100–104** |
| **06** | Spiral Model | Boehm's spiral · the four sectors · phases · risk-driven development · when **not** to use it · deeper treatment | Sommerville p.66–67; Mall §2.5–2.5.1 p.114–116; Pressman p.64–68 |
| **07** | Unified Process | what UP is · **the four phases — Mall's version and Sommerville's side by side** · RUP's six best practices · static workflows | Mall §8.3.1 p.475–476; Sommerville p.67–69 |
| **08** | Agile, XP and Scrum | agile definition · **the four manifesto statements** · agile vs other models · XP · Scrum | Sommerville p.75–76; Mall §2.4–2.4.4 p.105–114 |
| **09** | Life-Cycle Selection | the comparison of all models · the three factors (product · team · customer) · requirements and risk as drivers · worked selection scenarios | Mall §2.6 p.118 + Q40/53/55 p.130–131; Sommerville p.46 |
| **10** | Master Comparison + Exam Bank | all models in one table · Mall's exercises mapped to the topics · the retrieval set | all |

## B.2 File template — every file, same shape

```text
1. Cover block        — subject, week, topic number, source line
2. Where this sits    — one line linking back to the index (the advance organizer)
3. The content        — deepest detail, page-anchored, quotations marked
4. Source notes       — which source is primary, which merely repeats, [THIN] flags
5. Retrieval set      — 5-10 questions, ANSWERS WITHHELD
6. Page anchors       — the exact pages to revisit in the books
```

**Sections 5 and 6 are the ones that make this method work.** They are not decoration; they are the difference between learning and the illusion of it.

## B.3 Build order

Same as your proposal: **01 → 10, one file at a time**, then a merged document (cover + index + all topics) as the review artefact. I would not merge until all ten exist.

---

# Part C — What I need from you

| # | Question | Why it matters |
|:---:|:---|:---|
| 1 | **Do you accept the retrieval-set requirement?** | It is the one change to your plan. Without it, the evidence says the files will make you confident and worse at analytical questions. |
| 2 | **Do you want the retrieval sets as questions only, or questions plus a separate answer key at the very end of the merged document?** | Questions-only forces recall. A key at the back is more convenient but easier to peek at. |
| 3 | **Language** — the Cyber booklet you approved was English-only. Do you want these ASE files English-only too, or English term + Arabic explanation (your documented standing preference)? | It changes every file. |
| 4 | **Start with file 01, or do you want file 05 (RAD) first** because it is the biggest gap — Sommerville has nothing on it, so it is the topic you cannot get from the book you would naturally reach for? | Sequencing only. |

---

## Sources used in this report

- IJERT, *The Illusion of Mastery in AI-Assisted Learning: Do AI-Generated Summaries Create False Confidence?*, Vol. 15 Issue 5, 2026. DOI: [10.5281/zenodo.20522459](https://doi.org/10.5281/zenodo.20522459) — the confidence/performance table, the cognitive-level breakdown, the citation-following finding, and the recommendations. **Note the study's own limitation: n = 8, single session, no delayed post-test.** Treat it as indicative, not settled.
- Ausubel's advance organizer — 2025 systematic review of empirical studies (Scopus/Google Scholar indexed).
- Spacing and retrieval practice — *Nature Reviews Psychology* review (2022) and a 2025 meta-analytic review in *Educational Psychology Review*, DOI [10.1007/s10648-025-10035-1](https://doi.org/10.1007/s10648-025-10035-1).
- Segmenting principle — tagged `[Foundational Knowledge / Standard Concept]`; no clean single citation retrieved this session.
- Note-taking (provided vs learner-generated) — *Educational Research Review* 2023 and a 2024 *Educational Psychology Review* review of 24 studies, DOI [10.1007/s10648-024-09914-w](https://doi.org/10.1007/s10648-024-09914-w).

*Report and plan built 2026-09-23. The evidence is quoted with its numbers and its limitations; where I could not verify something it is tagged rather than asserted.*
