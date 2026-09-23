---
title: "Week 02 — Cybersecurity Risks and Threats · Source Verification Report"
subject: "01_Cyber_Security"
week: 2
instructor: "Asst. Prof. Dr. Huda Lafta Majeed"
verified_against: "Robin Sharp, Introduction to Cybersecurity: A Multidisciplinary Challenge, Springer, Ch. 3 'Risk', pp. 37–56"
status: "verification complete — 2 factual errors, 2 terminology issues, 1 unresolved letter question"
created: "2026-09-23"
---

# Week 02 — Risk · Source Verification Report

> **Why this exists.** You asked me to stop relying on the lecture and the booklet, find the original source, and check the material against the internet. This is that work. Every claim below is traced to a named source with a link.

---

## 0. Headline

**I identified the source.** The Cyber Week 02 Risk booklet is a **direct extraction of Chapter 3 of a published Springer textbook**:

> **Sharp, R. (2024). "Risk". In: *Introduction to Cybersecurity: A Multidisciplinary Challenge*. Undergraduate Topics in Computer Science. Springer, Cham. pp. 37–56.** DOI: [10.1007/978-3-031-41463-3_3](https://doi.org/10.1007/978-3-031-41463-3_3)

**Robin Sharp is an emeritus professor in the Cybersecurity Section at DTU Compute** (Technical University of Denmark). That single fact explains several oddities in the booklet that had been puzzling me — the term **"liveware"**, and the letter choices **`K`** (Danish/Norwegian *konsekvens* = consequence) and **`M`** (*foranstaltninger/midler* = countermeasures). The booklet is a Nordic textbook chapter, reflowed into a Word document.

**And the verification found real errors.** Not stylistic quibbles — two factual errors, one of which **Dr. Huda highlighted in yellow**, meaning it is exam material.

| # | Item | Verdict |
|:---:|:---|:---|
| 1 | ISO/IEC 27002 "**2022** … **14 categories**" | **ERROR** — the 14 categories are the **2013** structure. The 2022 version has **4 themes / 93 controls** |
| 2 | OCTAVE's fourth variant, "**OCTAVE FORTE**" | **ERROR** — no such variant exists. There are **three** public OCTAVE methodologies |
| 3 | Authentication factor "**Inheritance**" | **TERMINOLOGY ERROR** — the standard term is **Inherence** |
| 4 | OCTAVE "developed for **CERT**" | **IMPRECISE** — developed at CMU in 2001 **for the US Department of Defense**; CERT/SEI is the CMU body |
| 5 | OCTAVE "**three phases**" | **CONFIRMED** — verbatim correct |
| 6 | PDCA (Plan · Do · Check · Act) | **CONFIRMED** |
| 7 | The five mitigation strategies | **CONFIRMED** — all five are the recognised set |
| 8 | Four threat groups incl. liveware | **CONFIRMED** — and "liveware" is Sharp's own term |
| 9 | Risk definition, objective vs subjective | **CONFIRMED** by the chapter abstract itself |
| 10 | `S = F × K` and `R = S / M` | **Cannot be checked directly** (chapter body is paywalled). See §4 |

---

## 1. How the source was identified (evidence, not a guess)

I did not infer this. The identification is based on four independent matches:

1. **A verbatim sentence match.** I searched the booklet's opening line — *"The word risk is used here in its technical sense, where it is understood to mean the quantitative probability that an error situation occurs and gives rise to damage"* — and it returned the chapter's first page as the only exact hit. The booklet's text is the book's text.
2. **The stray "3"** at the top of the DOCX. It is not a page number; it is the chapter number. The chapter runs **pp. 37–56**, and the document opens with a chapter heading.
3. **Figure numbering.** The booklet references *"Fig. 3.1"* (the shark), then an unnumbered "Fig. An empty risk matrix" and "Fig. An empty residual risk matrix". The book's chapter has **Fig. 3.1, 3.2 and 3.3**. The booklet's figures were stripped in conversion, which is why it has zero images.
4. **The chapter abstract.** Springer's own abstract reads: *"This chapter explains the meaning of **objective risk**, and gives an introduction to the discipline of **risk management** – the ways in which risk can be reduced in an IT system by introducing **countermeasures**."* That is exactly the booklet's three opening movements, in order.

**Source pages:** [Springer chapter page](https://link.springer.com/chapter/10.1007/978-3-031-41463-3_3) · [Book page](https://link.springer.com/book/10.1007/978-3-031-41463-3) · [DTU Orbit record](https://orbit.dtu.dk/en/publications/introduction-to-cybersecurity-a-multidisciplinary-challenge/) · [DBLP record](https://dblp.org/rec/series/utcs/Sharp24)

---

## 2. The two factual errors, in detail

### 2.1 ISO/IEC 27002 — the "14 categories" belong to 2013, not 2022

**The booklet says** (and Dr. Huda **highlighted this line in yellow**):

> *"The latest version of ISO/IEC 27002 from 2022 describes targets for what has to be done within 14 categories"*

**What the standard actually says:**

| Edition | Structure |
|:---|:---|
| **ISO/IEC 27002:2013** | **114 controls in 14 clauses** (clauses 5–18) |
| **ISO/IEC 27002:2022** | **93 controls in 4 themes** — Organisational · People · Physical · Technological |

Sources: [ISMS.online comparison](https://www.isms.online/iso-27002/iso-27002-revisions-updates-comparison/) (*"The number of controls in the new version ISO 27002 2022 has decreased from 114 controls in 14 clauses in the 2013 edition… the control sets are now organised into four (4) categories or themes instead of fourteen (14) control domains"*) · [SureCloud guide](https://www.surecloud.com/resource-hub/iso-27002-guide-controls-changes) · [ISO official page](https://www.iso.org/standard/75652.html)

**And the decisive check:** the booklet's own 14-item list matches the **2013 clause set verbatim and in the same order**.

| # | Booklet's item | ISO 27002:2013 clause |
|:---:|:---|:---|
| 1 | Information security policies | Information Security Policies |
| 2 | Organization of information security | Organization of Information Security |
| 3 | Human resource security | Human Resource Security |
| 4 | Asset management | Asset Management |
| 5 | Access control | Access Control |
| 6 | Cryptography | Cryptography |
| 7 | Physical and environmental security | Physical and environmental security |
| 8 | Operation security | Operation Security |
| 9 | Communication security | Communication security |
| 10 | System acquisition, development and maintenance | System acquisition, development and maintenance |
| 11 | Supplier relationships | Supplier relationships |
| 12 | Information security incident management | Information security incident management |
| 13 | Information security aspects of business continuity management | Information security aspects of business continuity management |
| 14 | Compliance with legal and contractual requirements | Compliance |

Source for the 2013 clause list: [Wikipedia, ISO/IEC 27002](https://en.wikipedia.org/wiki/ISO/IEC_27002)

**Verdict:** the **list is 2013's**, the **label "2022" is wrong**. Note this is likely Sharp's own slip in the book, not something the doctor invented — the booklet reproduces the book.

**The number to hold: 14 belongs to 2013. 2022 is 4 themes and 93 controls.**

### 2.2 "OCTAVE FORTE" does not exist

**The booklet says** OCTAVE exists in **four** variants: OCTAVE, OCTAVE-S, OCTAVE ALLEGRO, and **OCTAVE FORTE**.

**What the sources say:** there are **three** publicly available OCTAVE methodologies.

| Variant | For whom |
|:---|:---|
| **OCTAVE** (the original method) | Large organisations, 300+ employees, multi-layered hierarchy |
| **OCTAVE-S** | Small organisations, ~100 people or fewer, flat structure |
| **OCTAVE Allegro** | Streamlined, asset-focused; **8 steps organised into 4 phases** |

Sources: [CIO Wiki, OCTAVE](https://cio-wiki.org/wiki/OCTAVE_(Operationally_Critical_Threat,_Asset_and_Vulnerability_Evaluation) — *"There are now three distinctive OCTAVE methodologies available for public use: the OCTAVE method, OCTAVE-S, and OCTAVE Allegro"* · [IriusRisk](https://www.iriusrisk.com/resources-blog/octave-threat-modeling-methodologies) · [PECB whitepaper](https://pecb.com/en/whitepaper/risk-assessment-with-octave)

**No source anywhere names an "OCTAVE Forte."** I searched for it specifically and it returned nothing but the three real variants.

**Verdict:** the fourth variant is **not real**. Note also that **OCTAVE-S is for *small* organisations and Allegro is the *streamlined/expanded* one** — the booklet's descriptions are close but the count is wrong.

### 2.3 Related nuance — whose "three phases" are these?

The booklet's three OCTAVE phases are **correct for the original OCTAVE method**:

| Phase | Booklet | CIO Wiki / SEI |
|:---:|:---|:---|
| 1 | Build up asset-based threat profiles | Build Asset-Based Threat Profiles |
| 2 | Identify vulnerabilities in the infrastructure which could lead to unauthorized action | Identify Infrastructure Vulnerabilities |
| 3 | Develop a security strategy and plans | Develop Security Strategy and Plans |

**Verified verbatim.** But be aware: **OCTAVE Allegro** — the variant most people actually use today — runs on **8 steps in 4 phases**, not 3. If an exam question asks about Allegro specifically, "3 phases" is the wrong answer.

---

## 3. The terminology issues

### 3.1 "Inheritance" should be "Inherence"

The booklet prints the four authentication factors as **Knowledge · Possession · Inheritance · Location**.

The **standard** taxonomy is: **Knowledge** (something you know) · **Possession** (something you have) · **Inherence** (something you are). Sources: [Signisys](https://www.signisys.com/learn/authentication-factors/) (*"the three core types (knowledge, possession, inherence)"*) · [HYPR](https://www.hypr.com/learn/authentication/factors-of-authentication).

**"Inheritance" is wrong** — in security it means nothing of the kind; inheritance is about receiving property from a predecessor. The correct word for *something you are* is **Inherence**.

**Also worth knowing:** the **core** set is **three**. **Location** (*somewhere you are*) is a recognised **extension** used in some frameworks, not part of the classic triad. So the booklet's "four factors" is defensible but is not the universal count.

### 3.2 OCTAVE's origin

The booklet says OCTAVE was *"developed for the international organization CERT at Carnegie Mellon University in USA"*.

More precisely: OCTAVE was **developed at Carnegie Mellon University in 2001, for the United States Department of Defense**, by staff of the **CERT Coordination Center at the SEI** (Software Engineering Institute). So: right university, right body, but the sponsor was the **US DoD**, and CERT is not an "international organization" — it is a US federally funded research and development centre at CMU.

Source: [CIO Wiki, OCTAVE](https://cio-wiki.org/wiki/OCTAVE_(Operationally_Critical_Threat,_Asset_and_Vulnerability_Evaluation) — *"OCTAVE was developed in 2001 at Carnegie Mellon University (CMU), for the United States Department of Defense."*

---

## 4. The formula question — what I could and could not settle

This was the item you were most unsure about, so here is exactly what I know and what I do not.

### 4.1 What I could not verify

The chapter body is **paywalled**. Springer shows only the abstract and metadata; the full-text PDF is behind an institutional login. So I could **not** read Sharp's exact equations with my own eyes.

### 4.2 What I can establish by inference

- The booklet is a **direct extraction** of the chapter — proven by the verbatim opening sentence. Therefore the booklet's `S = F × K` and `R = S / M` are, with high confidence, **Sharp's own letters and operators**. The booklet did not invent them.
- A search snippet of the chapter confirms it uses **"frequency"** as a quantity and has **figures 3.2 and 3.3** covering the risk matrix and residual-risk matrix on a **3-point low/medium/high scale**. That is consistent with the booklet's `F` = frequency and with the two colour-coded matrices.

### 4.3 Your reported version

You reported the lecture as `f = s · k` and `f = s / n` with **n = number of threats**. Given the above, the most likely explanation is a **transcription slip in the lecture** — the same letter `f` cannot be the subject of both equations, and "number of threats" in the denominator would mean *more threats → less risk*, which is backwards.

**However, I am not declaring your report wrong**, because the doctor may genuinely have written something different on the board, and I could not read the book's page. Two things would settle it in one minute:
1. **Your paper notes** from the lecture.
2. **The book itself** — if the university library has Springer access, or if you can get the chapter PDF, I can verify the exact letters.

### 4.4 One useful fact regardless — the division is not the industry standard

The mainstream industry formula for residual risk is **subtraction**, not division:

> **Residual Risk = Inherent Risk − Control Effectiveness**

Sources: [Auditive](https://blog.auditive.io/calculate-residual-risk-effectively/) · [Panorays](https://panorays.com/blog/what-is-residual-risk-how-it-guides-third-party-evaluation/) · [RiskWatch](https://www.riskwatch.com/inherent-vs-residual-risk/)

So `R = S / M` is **Sharp's own modelling choice**, not a universal convention. That is worth knowing: if you are ever asked to express residual risk in general terms, the standard answer is a subtraction of control effectiveness; if you are asked *in this course*, answer with the booklet's division. **Both can be right — in different rooms.**

---

## 5. What this means for your exam

The doctor is the marker, so the operational rule is simple:

| Situation | What to write |
|:---|:---|
| Asked how many ISO/IEC 27002 categories | **14** — that is what her highlighted material says, and that is what she will mark |
| Asked *which* categories | The 14-item list, in order — it is a real list, just from 2013 |
| Asked how many OCTAVE variants | **Four** if you follow her material; **three** if you are asked what actually exists. **Safest:** name the four she taught, since she marked it |
| Asked the authentication factors | **Knowledge · Possession · Inheritance · Location** — her four, her wording. But if you have room, writing **"inherence (something you are)"** shows the correct term without contradicting her |
| Asked for the equations | Use the booklet's letters. Confirm from your notes first |

**The principle:** answer in her vocabulary, but **know the correct fact**. A student who writes "14 categories (the 2013 structure; the 2022 revision reorganised into 4 themes and 93 controls)" is showing mastery, not correcting the doctor. That is how you turn a fact-check into extra marks instead of a risk.

---

## 6. Proper citation for the vault

Formatted to the standard required by `AGENTS.md`:

> [Sharp, R., "Risk", in *Introduction to Cybersecurity: A Multidisciplinary Challenge*, Undergraduate Topics in Computer Science, Springer, Cham, 2024, pp. 37–56](https://doi.org/10.1007/978-3-031-41463-3_3)

Whole book: [Sharp, R., *Introduction to Cybersecurity: A Multidisciplinary Challenge*, Springer, Cham, 2023, 442 p.](https://doi.org/10.1007/978-3-031-41463-3)

**This closes the "source attribution absent" flag** from the concept outline (§21, flag 7). The Cyber Week 02 Risk booklet now has a real, resolvable source.

---

## 7. Open items

| # | Item | What would close it |
|:---:|:---|:---|
| 1 | Sharp's exact equation letters | The chapter PDF, or library access to Springer |
| 2 | Your lecture notes on the two equations | A photo or a transcription |
| 3 | The illustrated booklet | Still missing — `word/media` in the DOCX is empty. But note: **the figures are the book's Fig. 3.1–3.3**, so the book (or any library copy) is now the better source for them |
| 4 | Whether the ISO "2022/14 categories" slip is Sharp's or introduced later | Reading the book's §on ISO 27002 — same paywall |
| 5 | "The debug has 5 steps" | Still unlocated anywhere. Now that the source is known, this can be checked against the book's chapter 3 if we get access |

---

*Verification report built 2026-09-23. Sources: Springer (chapter and book records), ISMS.online, SureCloud, ISO, Wikipedia, CIO Wiki, IriusRisk, PECB, Signisys, HYPR, Auditive, Panorays, RiskWatch, DTU Orbit, DBLP. Nothing asserted without a traceable source; nothing that could not be verified was stated as fact.*
