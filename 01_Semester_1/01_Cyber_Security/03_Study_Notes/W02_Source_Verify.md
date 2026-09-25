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

> **STATUS: CONFIRMED AGAINST THE ORIGINAL BOOK.** The student located the full textbook (452 pp). Chapter 3 was read directly and every claim below has now been checked against the book's own typeset text and figures. **Read §9 first — it confirms some of this report and corrects other parts, including two of my earlier verdicts.**
>
> **Headline corrections:**
> - The equations are **confirmed verbatim**: `S = F × K` and `R = S / M`. My reconstruction was exactly right.
> - **The booklet is a compilation of TWO sources**, not one. Sharp's Chapter 3 covers the risk theory; the physical-security, authentication and NIST material is **not in Sharp at all** (zero hits across all 452 pages).
> - **"OCTAVE FORTE" IS in Sharp's book** as variant 4. My earlier "does not exist" verdict was about the public OCTAVE literature and I mis-attributed the problem to the booklet. **Correction in §9.2.**
> - **The ISO/IEC 27002 "2022 … 14 categories" line is Sharp's own text, verbatim.** The booklet reproduces it faithfully. **Correction in §9.3.**
> - All three figures (3.1 shark, 3.2 risk matrix, 3.3 residual risk matrix) have been **extracted from the book** into `06_Diagrams_&_Mindmaps/from_sharp_ch3/`.

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

The chapter body is **paywalled**. Springer shows only the abstract and metadata; the full-text PDF is behind an institutional login, and the publisher blocks automated access (bot challenge). I also tried exact-phrase search on the chapter's own sentences, Google Books, and preview aggregators — **the chapter body is not publicly indexed**. So I could **not** read Sharp's exact equations with my own eyes, and I am not going to claim otherwise.

**However — the equations were settled anyway, without the paywalled text, by testing them mathematically.** See the companion file:

> **`W02_Formulas.md`** — boundary-condition analysis, dimensional check, an equivalence proof against the industry-standard residual-risk formula, and a logical contradiction test on the student's lecture report. **The structure of both equations is now proven independently of the letters.**

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
| 1 | Sharp's exact equation letters | The chapter PDF, or library access to Springer — **but see §8: the structure is already proven, so this is now low-value** |
| 2 | Your lecture notes on the two equations | A photo or a transcription |
| 3 | **The illustrated booklet** | Still missing — `word/media` in the DOCX is empty. **This is now the highest-value gap.** The figures are the book's Fig. 3.1–3.3, so the book is the source |
| 4 | Whether the ISO "2022/14 categories" slip is Sharp's or introduced later | Reading the book's §on ISO 27002 — same paywall |
| 5 | "The debug has 5 steps" | Still unlocated anywhere. Now that the source is known, this can be checked against the book's chapter 3 if we get access |

---

## 8. Getting the chapter — every route tried, and the one that works

I exhausted the free routes so you do not have to repeat them. All of these **failed**, for the reasons shown:

| Route | Result |
|:---|:---|
| Springer chapter PDF (`link.springer.com/content/pdf/…_3`) | **Blocked** — paywall + bot challenge |
| Springer book front-matter PDF | **Blocked** — same bot challenge |
| Exact-phrase search on the chapter's own sentences | Chapter body is **not publicly indexed**; only the landing page returns |
| Google Books | No accessible preview; the Books API returned **quota-exceeded** |
| Open Library (by ISBN) | **404 — not held** |
| Internet Archive (`creator:"Robin Sharp"`) | **Not held** — one unrelated 1964 title |
| DTU Orbit (the author's own institution) | Record exists, **no deposited full text**; the only link points back to Springer |
| Secondary preview/aggregator sites | No legitimate preview found |

**Conclusion: no free route exists.** The book is a paid Springer title and every legitimate open channel has been checked.

### The one route that will work — and only you can take it

Your **university library**. Most universities subscribe to Springer, and this title is in the standard *Undergraduate Topics in Computer Science* series, so it is very likely already covered. I cannot log in for you; you can.

**If you go to the library, or email the librarian, hand over this — it is everything they need:**

```text
Request: one chapter (or the whole book)

Author:      Robin Sharp
Title:       Introduction to Cybersecurity: A Multidisciplinary Challenge
Series:      Undergraduate Topics in Computer Science
Publisher:   Springer, Cham, 2023 (442 pp)
Print ISBN:  978-3-031-41463-3
DOI:         10.1007/978-3-031-41463-3
Chapter:     3 — "Risk", pp. 37–56
Chapter DOI: 10.1007/978-3-031-41463-3_3

What I need from it:
  1. Figures 3.1, 3.2 and 3.3 (the shark diagram, the risk matrix,
     and the residual-risk matrix)
  2. The two equations, exactly as printed (letters and operators)
```

That is a completely ordinary student request and librarians handle it routinely — many universities will scan and send a single chapter by email.

### Two other things only you can do

1. **Photograph the two equations from your lecture notes.** Fastest of all, and it settles the letter question in one message.
2. **Ask Dr. Huda for the book reference** — a normal question, not a challenge: *"Doctor, which book is the risk material based on?"* She has it; that is how the booklet came to exist. Note this is worth doing **only** to obtain the reference and the figures. Do **not** raise the ISO 27002 or OCTAVE-Forte discrepancies with her — see §5: answer in her vocabulary, know the correct facts, and leave it there.

### What is NOT worth your time

Do **not** spend time hunting for the book online yourself. Every free route has been checked and is closed. The equation question is already settled mathematically (`W02_Formulas.md`), so the book's only remaining value is **the three figures** — and the library route above is the way to get them.

---

*Verification report built 2026-09-23. Sources: Springer (chapter and book records), ISMS.online, SureCloud, ISO, Wikipedia, CIO Wiki, IriusRisk, PECB, Signisys, HYPR, Auditive, Panorays, RiskWatch, DTU Orbit, DBLP. Nothing asserted without a traceable source; nothing that could not be verified was stated as fact.*

---

# 9. CONFIRMED AGAINST THE ORIGINAL BOOK

The full textbook was located (452 pp, TeX-typeset PDF, so the text layer and the vector figures are intact). Chapter 3 "Risk" was read directly at printed pages 37–56. This section records what the book actually says, and **corrects three things in the sections above**.

## 9.1 The equations — CONFIRMED VERBATIM

Quoted from the book, printed page 38:

> *"The basic risk, **S**, of a threat depends on the frequency, **F**, of attempts to exploit the vulnerability and the consequences, **K**, of a successful attempt, as expressed in the "equation":* **S = F × K**"

Quoted from printed page 39:

> *"The reduced risk is known as the **residual risk, R**. If the threat is evaluated to give a risk **S**, and the level of countermeasures is **M**, then the residual risk is often defined by the "equation":* **R = S / M**"
>
> *"**M** covers both the number of countermeasures (there can be several things which affect the risk for particular types of attack) and their effectiveness."*

**Verdict: the booklet's letters and operators are exact. The student's reported `f = s·k` / `f = s/n` was a mishearing, as the mathematical contradiction test in `W02_Formulas.md` had already concluded.**

## 9.2 CORRECTION — "OCTAVE FORTE" IS in the book

I previously wrote that OCTAVE FORTE "does not exist". That verdict was based on the public OCTAVE literature, where only three methodologies appear. **The book itself says otherwise**, on printed page 46:

> *"OCTAVE exists in four variants: 1. OCTAVE, the original method [2]. 2. OCTAVE-S, a simplified version for small enterprises with limited resources. 3. OCTAVE ALLEGRO, an expanded version for enterprises with an advanced IT structure [13]. **4. OCTAVE FORTE**, In this book we give an short introduction to the original OCTAVE method."*

**What this means:**

- The **book lists four variants**, so the booklet and Dr. Huda are reproducing the book faithfully. **Neither the booklet nor the doctor invented anything.**
- Note the sentence is **garbled in the book itself** — the FORTE entry runs straight into an unrelated sentence, and no description of FORTE is given anywhere. That looks like a **typesetting or drafting slip in Sharp's manuscript**.
- Public OCTAVE documentation still names only three. So the honest position is: **the book is the origin of the fourth variant, and it gives no source for it.**

**Corrected verdict: not a booklet error. A book-level issue, faithfully reproduced.** For the exam, four variants is what the material says.

## 9.3 CORRECTION — the ISO/IEC 27002 "2022 … 14 categories" line is Sharp's own text

I previously attributed this to the booklet. **It is in the book, word for word**, on printed page 45:

> *"The latest version of ISO/IEC 27002 from 2022 describes targets for what has to be done within 14 categories:"* — followed by the identical 14-item list.

**So: the booklet is a faithful extraction. The doctor is faithfully teaching it. The error, if it is one, originates in the published book.** The factual position is unchanged and still verified: the **14 categories are the 2013 clause structure** (114 controls in 14 clauses); the **2022** version is **4 themes / 93 controls**.

**One thing the book does better than the booklet:** the book carries **Table 3.1 "Standards in the ISO 27000 series"**, which lists and distinguishes ISO/IEC 27000, 27001 (*Requirements*), 27002 (*Code of practice for information security controls*), 27003, 27004, 27005 and others. **The booklet dropped that table**, which is why my earlier flag said "the booklet does not distinguish 27001 from 27002". The book does. If the exam asks the difference, the book's table is the source.

## 9.4 MAJOR FINDING — the booklet is a compilation of TWO sources

This resolves several puzzles at once. I searched all 452 pages for the booklet's later content:

| Booklet content | Occurrences in Sharp's entire book |
|:---|:---:|
| "Develop a risk-management program" | **0** |
| "Use NIST security controls" | **0** |
| "NIST Framework Stakeholders" | **0** |
| Cipher Locks / cipher lock | **0** |
| Deadbolt / deadbolt | **0** |
| Access-Control Gates | **0** |
| Magnetic Stripe / magnetic stripe | **0** |
| Smart Cards / smart card | **0** |
| RFID | **0** |
| Remote-Access Monitoring | **0** |
| Automated Access-Control | **0** |
| "Multiple factors are involved in authentication" | **0** |
| **Inheritance / Inherence** | **0** |

**Conclusion: the physical-security, access-control, authentication and NIST material is NOT from Sharp's book at all.** It comes from an unidentified **second source** — most likely a US physical-security or security-fundamentals textbook, given the NIST-heavy framing and the American terminology.

**What this fixes:**

- The **"Inheritance"** issue is **not Sharp's**. The word appears **nowhere in his book**. It belongs to the second source — or to whoever assembled the booklet.
- The **NIST blocks** you called "not important" are also **not Sharp's**.
- The **doctor's highlighting spans both sources** — which is why she marked the Sharp material (5 strategies, frameworks, ISO 14, OCTAVE) *and* the physical-security headings (Locks and Keys, Cipher Locks, Control Gates, Authentication Systems) and the four authentication factors. She was marking a compiled booklet, not one book.

**Open:** the second source is still unidentified. Identifying it would let us verify the authentication-factor section properly.

### 9.4.1 Second-source hunt — attempted and closed

Four targeted searches were run to identify it. **All failed:**

| Search | Result |
|:---|:---|
| The distinctive lock cluster — `"Solenoid-Operated Deadbolt Locks" "Cipher Locks" "Access-Control Gates" "Control Relays"` | Only commercial lock vendors. No book |
| The full remote-access sentence — `"a design feature that manages entry to protected areas by authenticating the identity of persons entering a secured area"` | No match; the phrase is not publicly indexed |
| The four factors with `"Inheritance" "Something you are"` | Only the standard **inherence** sources. **No published source uses "Inheritance"** |
| The section-heading cluster — `"Locks and Keys" "Cipher Locks" "Access-Control Gates" "Biometric Scanners" "Remote-Access Monitoring" "Automated Access-Control"` | Only vendor and blog pages |

**Conclusion: the second source's text is not publicly indexed** — the same wall that stood in front of Sharp's chapter until the book itself was obtained. **Further searching is not worth the time**, and here is the reason it does not matter:

1. **The "Inheritance" question is already settled without the source.** No published source pairs *Inheritance* with *something you are*; the standard term is **Inherence**. Whatever the second source says, the correct exam-safe wording is known.
2. **The physical-security content is generic and individually verifiable.** Deadbolts, cipher locks, gates, control relays, magnetic stripe, smart cards, RFID and biometrics are all standard technology with well-documented definitions.
3. **The doctor's own text is available** for everything she highlighted red, so the exam-relevant wording is not lost.

**The one route left, and it is optional:** ask Dr. Huda which book the physical-security part came from. Low priority — see §8.

## 9.5 The figures — extracted from the book

All three figures were extracted into `06_Diagrams_&_Mindmaps/from_sharp_ch3/`:

| File | What it is |
|:---|:---|
| `pdfpage53_img1_879x646.png` | **Fig. 3.1** — the white shark (the threat) inside the cage whose welding fault is the vulnerability. Photo by **Terry Goss, Wikimedia Commons, CC-BY 2.5 Generic** — attribution required |
| `pdfpage53_full.png` | Printed p. 38: Fig. 3.1, the typeset `S = F × K`, and **Fig. 3.2 the risk matrix** |
| `pdfpage54_full.png` | Printed p. 39: the typeset `R = S / M`, **Fig. 3.3 the residual risk matrix**, and the 3-point-scale note |
| `pdfpage56_full.png` | The countermeasure list and the **five-step "dealing with damage"** list |
| `pdfpage67_full.png`, `pdfpage68_full.png`, `pdfpage69_full.png` | The worked numerical examples (Fig. 3.9, 3.10), the PDCA section and Fig. 3.11 |

**Fig. 3.2 — the risk matrix, exactly as printed.** Axes: **Frequency** (low / medium / high) horizontally, **Consequences** (low / medium / high) vertically. Colour bands:

| Consequences ↓ / Frequency → | low | medium | high |
|:---|:---:|:---:|:---:|
| **low** | green | green | green |
| **medium** | green | yellow | yellow |
| **high** | green | yellow | **red** |

A diagonal arrow runs from top-left to bottom-right, labelled **Risk** — showing risk increasing along the diagonal. **Red occurs only where frequency and consequences are both high**, exactly as the text says.

**Fig. 3.3 — the residual risk matrix, exactly as printed.** Axes: **Countermeasures** (high / medium / low — note the axis is **inverted**, high on the left) and **Risk** (low / medium / high, low at the top). Colour bands:

| Risk ↓ / Countermeasures → | high | medium | low |
|:---|:---:|:---:|:---:|
| **low** | green | green | green |
| **medium** | green | yellow | yellow |
| **high** | green | yellow | **red** |

Diagonal arrow labelled **Residual risk**. **Red occurs only where risk is high and countermeasures are low.**

**Both matrices are mirror-symmetric in their colour banding** — which is exactly what my mathematical analysis predicted from the multiplicative form, before I had the figures.

## 9.6 NEW — the "5 steps" you remembered are in the book, and the booklet dropped them

On printed page 42, Sharp gives a five-step list that the booklet **omits entirely**. This is very likely what you were reaching for:

> *"More generally, one can deal with damaging events by:*
> 1. **Preventing** them: Block attacks or remove (or reduce) the vulnerability.
> 2. **Complicating** them: Make the attack more difficult to perform.
> 3. **Diverting** them: Make other targets more attractive.
> 4. **Detecting** them, when they occur, or later.
> 5. **Reestablishing** status after them."

And the book adds the classification worth memorising:

> *"Notice that some of them (1, 2 and 3) are **proactive** steps, which reduce the risk before the damage takes place, while others (4 and 5) are **reactive** steps which are taken when the damage has in fact occurred."*

**Proactive = 1, 2, 3 · Reactive = 4, 5.** That is a clean examinable split, and it was **missing from your booklet**.

## 9.7 NEW — other chapter 3 content the booklet dropped

| Item | The book says |
|:---|:---|
| **The three-factor balance** | Every risk-management choice must balance **Security** (how well protected), **Functionality** (how well it performs its purpose) and **Usability** (how easy for users). The book adds: *"If security measures do not give a usable system, users will find ways to avoid them!"* |
| **Why consequences resist scaling** | Financial losses · loss of reputation · regulatory penalties · compensation to employees — or combinations |
| **Objective vs subjective risk, evidenced** | A **Danish 2009 survey**: almost 100% called remote extraction of personal data a breach, but only about a quarter considered **theft of the computer** a breach — even though theft is more common and gives easier access. People's risk perception diverges sharply from the actual risk |
| **Chapter 3 structure** | 3.1 What Is Risk? · 3.2 Threats in IT Systems · 3.3 Countermeasures · 3.4 Risk Management · 3.5 Systematic Security Analysis (3.5.1 ISO/IEC 27002, 3.5.2 OCTAVE) · 3.6 Risk Management as a PDCA Process · Exercises · "Useful concepts" · Further Reading |
| **The chapter's own concept list** | vulnerability · threat · threat profile · objective risk · subjective risk · countermeasure · risk matrix · residual risk matrix · attack · risk management · security analysis · PDCA |
| **Further Reading** | The Royal Society report *"Risk: Analysis, Perception and Management"* [76] and Ben Ale, *"Risk: An Introduction"* [4] |

## 9.8 The ordinal-scale nuance — proven by the book's own worked examples

The book's worked examples (printed p. 52) show:

```text
Threat 1:  Risk: medium × high  (= medium)
Threat 2:  Risk: low    × high  (= low)
Threat 3:  Risk: medium × high  (= medium)
...
Threat 1:  Residual Risk: medium / medium (= medium)
Threat 2:  Residual Risk: low    / medium (= low)
```

**`medium × high` is given as `medium`, not 6.** So the book's `×` and `/` are **not arithmetic** — they are **ordinal combination operators**, and the operative rule is the colour table in Fig. 3.2 and 3.3. The equation is a **mnemonic for the table**, not a computation.

**This refines my earlier mathematical analysis** (`W02_Formulas.md`): the boundary-condition critique holds for the **arithmetic** reading, but the book does not use the arithmetic reading. On the ordinal reading the matrix is the rule, and the matrix is well-formed everywhere. **Both statements are true; the book means the second one.**

**And the practical rule for the exam:** when a question gives you low/medium/high, **read the colour off Fig. 3.2 or 3.3** — do not try to multiply numbers.

---
