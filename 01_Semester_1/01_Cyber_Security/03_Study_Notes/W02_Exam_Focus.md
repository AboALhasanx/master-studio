---
title: "Week 02 — Cybersecurity Risks and Threats · Exam Focus (lecture-driven)"
subject: "01_Cyber_Security"
week: 2
instructor: "Asst. Prof. Dr. Huda Lafta Majeed"
source_file: "../02_Raw_Materials/W02_Risks_DrHuda_Booklet2.docx"
built_from: "doctor's own highlights in the DOCX + student's 2026-09-23 lecture report"
status: "exam-focus sheet — two items flagged for student confirmation"
created: "2026-09-23"
---

# Week 02 — Risk · Exam Focus Sheet

> **What this is.** The comprehensive reference is `W02_Concept_Outline.md`. **This sheet is the memorisation list** — what the doctor marked and what she said mattered, in the order she covered it. Nothing here replaces the outline; it tells you what to drill.

**Two inputs, kept separate on purpose**

| Input | Nature | Trust level |
|:---|:---|:---|
| **The doctor's highlights** inside the delivered DOCX | Mechanical extraction from the file — 30 highlight runs + 27 coloured runs | Objective. It is her own marking, not an interpretation |
| **The student's lecture report** (2026-09-23) | What she said and how she weighted it in class | Authoritative as a report of the lecture, but recorded as reported — see the conflicts in §8 |

> **SOURCE FOUND — AND NOW READ DIRECTLY.** The booklet is a direct extraction of **Sharp, R., "Risk", in *Introduction to Cybersecurity: A Multidisciplinary Challenge*, Springer, 2023, pp. 37–56** ([DOI 10.1007/978-3-031-41463-3_3](https://doi.org/10.1007/978-3-031-41463-3_3)). The full book was located, and chapter 3 was read page by page. What that changed:
>
> - **The equations are confirmed exactly**: `S = F × K` and `R = S / M`, with `M` covering **number of countermeasures + effectiveness**. Your lecture report was a mishearing; the structure is settled.
> - **The booklet is a compilation of TWO sources.** Sharp supplies the risk theory. The physical-security, authentication and NIST material is **not in Sharp at all** (zero hits in 452 pages) — it comes from an unidentified second source. **The "Inheritance" wording is from that second source, not from Sharp.**
> - **"OCTAVE FORTE" IS in Sharp's book** as variant 4, though with no description and a garbled sentence. So the booklet and the doctor reproduce the book faithfully. My earlier "does not exist" verdict was about the public OCTAVE literature — **the book is the origin, not the booklet**.
> - **The ISO/IEC 27002 "2022 … 14 categories" line is Sharp's own text, verbatim.** The booklet is faithful; the doctor is faithful. The factual position is unchanged (14 categories = the **2013** structure; 2022 = **4 themes / 93 controls**).
> - **All three figures were extracted** into `06_Diagrams_&_Mindmaps/from_sharp_ch3/` — the shark, the risk matrix and the residual-risk matrix. **Your booklet had none of them.**
> - **Content the booklet dropped, recovered from the book:** the **five-step "dealing with damaging events"** list (§2A), the **security / functionality / usability balance** (§2B), and the **Danish 2009 survey** on objective vs subjective risk (§5.1).
>
> **Full evidence and corrections: `W02_Source_Verify.md` §9.** Exam rule unchanged and in that file §5: answer in her vocabulary, know the correct fact.

---

## 1. The doctor's emphasis map (extracted from the file, not inferred)

Her marking uses two devices: **highlight colour** and **font colour**. They are not the same signal.

### Yellow highlight — the "know this list" marker

| # | Highlighted text | What it marks |
|:---:|:---|:---|
| 1 | Risk avoidance | Mitigation strategy 1 |
| 2 | Risk reduction | Mitigation strategy 2 |
| 3 | Risk retention | Mitigation strategy 3 |
| 4 | Risk transfer | Mitigation strategy 4 |
| 5 | Risk sharing | Mitigation strategy 5 |
| 6 | COBIT | Analysis framework |
| 7 | COSO | Analysis framework |
| 8 | FAIR | Analysis framework |
| 9 | OCTAVE | Analysis framework |
| 10–11 | "The latest version of ISO/IEC 27002 from 2022 describes targets for what has to be done within **14 categories**" | The ISO number **14** |
| 12 | ", threats and vulnerabilities in **three phases**" | OCTAVE's phase count |

### Red highlight — the "be able to explain this" marker

| # | Highlighted text | What it marks |
|:---:|:---|:---|
| 13 | Build up asset-based threat profiles | OCTAVE phase 1 |
| 14 | Identify vulnerabilities in the infrastructure which could lead to | OCTAVE phase 2 |
| 15 | Develop a security strategy and plans | OCTAVE phase 3 |
| 16 | Plan | PDCA element 1 |
| 17 | Do | PDCA element 2 |
| 18 | Check | PDCA element 3 |
| 19 | Act | PDCA element 4 |
| 20 | Locks and Keys | Physical security control |
| 21 | Locking Deadbolts | Physical security control |
| 22 | Cipher Locks | Physical security control |
| 23 | Control Gates | Physical security control |
| 24 | Authentication Systems | Physical security control |
| 25 | Multiple factors are involved in authentication | The authentication enumeration |
| 26 | Knowledge | Authentication factor 1 |
| 27 | Possession | Authentication factor 2 |
| 28 | Inheritance | Authentication factor 3 |
| 29 | Location | Authentication factor 4 |

### Coloured text (not highlighted) — the "these are the categories" marker

| Colour | Text | What it marks |
|:---|:---|:---|
| Red `FF0000` | `3` · `What Is Risk?` | Section heading |
| Red `FF0000` | `S` · `F` · `K` | **The risk-equation letters** — the only equation variables she coloured |
| Red `FF0000` | `Threats in IT Systems` · `Hardware related threats` · `Software related threats` · `Data related threats` | The threat-group taxonomy |
| Dark red `C00000` | `Liveware related threats` | Threat-group 4 |
| Red `FF0000` | `Countermeasures` + `Threats such as vandalism` / `Threats such as unauthorized` | The countermeasure-to-threat matching |
| Dark red `C00000` | `Threats from attackers` · `Threats from malware` · `Threats such as unauthorized access to data` · `Threats from personnel` | The countermeasure-to-threat matching |
| Blue `548DD4` | `Risk Management` | Section heading |

**Reading of the map.** Yellow marks **countable lists to memorise**. Red marks **things to be able to say out loud**. Coloured text marks **the taxonomies**. Nothing else in the 66-paragraph booklet is marked at all — which is itself information.

---

## 2. The numbered sets — memorise the count first, then the items

| Set | Count | The items | Marked? |
|:---|:---:|:---|:---|
| Risk equations | **2** | Basic risk; residual risk | Red letters `S F K` |
| Threat groups | **4** | Hardware · Software · Data · Liveware | Red + dark red |
| Risk-mitigation strategies | **5** | Avoidance · Reduction · Retention · Transfer · Sharing | **Yellow** |
| Systematic analysis frameworks | **5** | COBIT · COSO · FAIR · ISO/IEC 27002 · OCTAVE | **Yellow** (4 of 5) |
| ISO/IEC 27002 categories (2022) | **14** | See §5.9 | **Yellow** |
| OCTAVE phases | **3** | Asset-based threat profiles · Infrastructure vulnerabilities · Security strategy and plans | **Red** |
| PDCA elements | **4** | Plan · Do · Check · Act | **Red** |
| Authentication factors | **4** | Knowledge · Possession · Inheritance · Location | **Red** |
| Cyber risk-assessment components | **4** | Identification · Evaluation · Mitigation · Monitoring and Review | Not marked |
| Countermeasure examples | **6** | Firewalls · Antivirus · Secure room · Backups · Encryption/access control · Personnel checks and training | Coloured text |

**Order matters in two places only:** the **five mitigation strategies** and the **four PDCA elements**. The rest are sets, not sequences.

---

## 2A. Recovered from the book — the five-step damage list (this was missing from your booklet)

On printed page 42, Sharp gives a list the Word conversion **dropped entirely**. This is almost certainly the "5 steps" you remembered:

> *"More generally, one can deal with damaging events by:*
> 1. **Preventing** them — block attacks or remove (or reduce) the vulnerability.
> 2. **Complicating** them — make the attack more difficult to perform.
> 3. **Diverting** them — make other targets more attractive.
> 4. **Detecting** them — when they occur, or later.
> 5. **Reestablishing** status after them."

And the split that makes it examinable, in the book's own words:

> *"Notice that some of them (1, 2 and 3) are **proactive** steps, which reduce the risk before the damage takes place, while others (4 and 5) are **reactive** steps which are taken when the damage has in fact occurred."*

**Proactive = 1, 2, 3 · Reactive = 4, 5.** That is the memorisable structure. Note it is a **different list** from the five risk-mitigation strategies (§5.3) — do not mix them up.

## 2B. Recovered from the book — the three-factor balance

Every risk-management decision must balance three factors, and the book is emphatic about the third:

| Factor | The question it answers |
|:---|:---|
| **Security** | How well is the IT system protected against unwanted events? |
| **Functionality** | How well does the system perform its intended functions? |
| **Usability** | How easy is it for users to make use of the system? |

The book's warning, worth quoting: *"This last factor is unfortunately often forgotten by system designers… **If security measures do not give a usable system, users will find ways to avoid them!**"*

---

---

## 3. The two equations

### 3.1 Basic risk

**As the delivered file states it:** `S = F × K`
- `S` = basic risk of the threat
- `F` = frequency of attempts to exploit the vulnerability
- `K` = consequences of a successful attempt

Visualised as the **risk matrix**, whose two axes are **frequency × consequences**. Red = high consequences **and** high frequency.

### 3.2 Residual risk (risk reduction)

**As the delivered file states it:** `R = S / M`
- `R` = residual risk
- `S` = the risk of the threat
- `M` = level of countermeasures — and the file is explicit that `M` covers **both the number of countermeasures and their effectiveness**

Visualised as the **residual-risk matrix**, whose two axes are **risk ÷ countermeasures**. Red = high risk **and** low countermeasures.

### 3.3 "The influencing factors" — your question answered

You asked what the *influencing factors* in the risk-reduction equation are. The file answers it directly in the paragraph right after the equation:

> *"M covers both the number of countermeasures (there can be several things which affect the risk for particular types of attack) and their effectiveness."*

So the influencing factors are **two**: **(1) how many countermeasures, (2) how effective they are**. Note the wording *"several things which affect the risk"* — that phrase is what the lecture called the influencing factors.

### 3.4 Comparison between the two equations

| | Basic risk | Residual risk |
|:---|:---|:---|
| Formula (file) | `S = F × K` | `R = S / M` |
| Answers | How big is the risk before defence? | How much risk is left after defence? |
| Operation | multiplication | division |
| Factors | frequency, consequences | risk, countermeasures |
| Matrix axes | frequency × consequences | risk ÷ countermeasures |
| Red corner | high frequency **and** high consequences | high risk **and** low countermeasures |
| Direction | both factors up → risk up | countermeasures up → residual risk **down** |

**The relationship between them:** the second equation **consumes the output of the first**. `S` is computed once, then fed into `R = S / M`. They are not alternatives — they are two stages.

`[CONFLICT]` — see §8.1. Your lecture report gives different letters for both equations. Do not drill the letters until that is settled.

---

## 4. Acronym shortcats — full name, and what it means

You asked for the chapter's abbreviations, to be memorised as **meaning + full name**. These are all stated in the file.

| Acronym | Full name | What it is |
|:---|:---|:---|
| **COBIT** | **C**ontrol **O**bjectives for **I**nformation and related **T**echnology | Objectives for measures that can be used to manage risk |
| **COSO** | **C**ommittee of **S**ponsoring **O**rganizations | Describes the internal processes a company must follow to reach a suitably low risk |
| **FAIR** | **F**actor **A**nalysis of **I**nformation **R**isk | A taxonomy of risk factors + a standard for naming risk quantities + a model for calculating risk |
| **OCTAVE** | **O**perationally **C**ritical **T**hreat, **A**sset and **V**ulnerability **E**valuation | A risk-analysis method; 3 phases; 4 variants |
| **PDCA** | **P**lan · **D**o · **C**heck · **A**ct | The cyclic form risk management takes |
| **ISO** | **I**nternational **O**rganization for **S**tandardization | Co-publisher of the 27002 series |
| **IEC** | **I**nternational **E**lectrotechnical **C**ommission | Co-publisher of the 27002 series |
| **CERT** | **C**omputer **E**mergency **R**esponse **T**eam | The body OCTAVE was developed for (Carnegie Mellon University, USA) |
| **NIST** | **N**ational **I**nstitute of **S**tandards and **T**echnology | Source of the security-control families |
| **SP 800-53** | **S**pecial **P**ublication 800-53 | The NIST reference for security controls |
| **RFID** | **R**adio **F**requency **ID**entification | Hands-free badge technology |
| **CSF** | **C**ybersecurity **F**ramework (NIST) | Named in the file's importance list |
| **NCSC** | **N**ational **C**yber **S**ecurity **C**entre (UK) | Named as a country-specific guideline source |
| **CIA** | **C**onfidentiality · **I**ntegrity · **A**vailability | Carried over from Week 01 — the vocabulary of every scenario answer |

**The two the file spells out fully inside the text** (so they are the likeliest to be asked as "what does X stand for") are **COBIT** and **OCTAVE** — both are written out long-form in the booklet.

---

## 5. Your checklist, item by item

### 5.1 Risk definition + "people's opinions" + its forms
**In the file, in the opening section.** Risk is defined in its **technical sense**: the **quantitative probability that an error situation occurs and gives rise to damage**, where damage = a **breach of the security policy**.

The "people's opinion" part you remembered is the file's next move: it contrasts this with **subjective risk**, which **does take human factors into account — public attitudes, trust, and personality**. So the two forms are:
- **Objective risk** — the technical, quantitative definition
- **Subjective risk** — the same situation as people perceive it (attitudes, trust, personality)

### 5.2 Threat groups — count and examples
**Four**, and the examples are given in the file:

| Group | Examples in the file |
|:---|:---|
| **Hardware related** | Harmful surroundings · natural disasters (storms) · physical attacks such as theft · faults in the infrastructure |
| **Software related** | Unauthorized modification or deletion of software · malware (viruses, worms, trojan horses, logic bombs) · poorly designed programs containing vulnerabilities · incorrect or out-of-date versions · theft or unauthorized copying |
| **Data related** | Unwanted storage, modification, disclosure or deletion · **inference** · **masquerading**, unauthorized access |
| **Liveware related** | Social engineering, phishing · IT fraud, forgery and other computer-assisted criminality |

### 5.3 Risk-management strategies, in sequence
**Five, in this order** (yellow-highlighted, and order is examinable):
1. **Risk avoidance** — keep the target system away from given risks
2. **Risk reduction** — proactive steps to prevent loss or reduce its extent
3. **Risk retention** — allow a certain, agreed amount of residual risk
4. **Risk transfer** — transfer the risk to others
5. **Risk sharing** — agree with other parties to deal with risks jointly

### 5.4 Physical security controls
All red-highlighted as section headings: **Locks and Keys** · **Locking Deadbolts** · **Cipher Locks** · **Control Gates** · **Authentication Systems**.

The distinction the file draws and that is worth having ready: the **door** is the physical barrier and *"will only keep honest people out"*; the **lock** provides the **authentication function** through its **key**.

### 5.5 Authentication — enumeration with explanation
**Four factors** (all red-highlighted), each in the file's own pattern — *something you…*:

| Factor | File's wording |
|:---|:---|
| **Knowledge** | Something you **know**, or that only the designated person should know |
| **Possession** | Something you **have**, or that only the designated person should have |
| **Inheritance** | Something you **are**, or that only the designated person is |
| **Location** | Somewhere you **are**, or somewhere only the designated person is |

Also from the file, and this is the sentence that makes the whole section answerable: **"authorization is based on authentication"**, and **limiting the access of unauthorized personnel to important assets is the most fundamental security step you can take**.

`[TERM]` — the file prints **"Inheritance"**. The standard English term for this factor is **Inherence**; *inheritance* normally means receiving property from a predecessor. Recorded verbatim as the file writes it. One clarifying question in class would settle it.

### 5.6 PDCA — acronym, elements, explanation
- **Shortcat:** **P**lan · **D**o · **C**heck · **A**ct
- **Plan** — threats are identified, risks are analyzed, countermeasures are planned
- **Do** — the countermeasures or other risk-management measures are implemented
- **Check** — the implemented solution is monitored, to check the desired security level is maintained
- **Act** — the solution is adjusted so it continues to give the desired level, **or** a decision is taken to start a completely new Plan phase

**Why it is PDCA at all:** risk management is **not a one-time activity** — the risk profile changes as new attack forms appear, so it must be re-evaluated at regular intervals. That is the sentence to lead with if asked "why PDCA".

### 5.7 OCTAVE — 3 phases, count only
1. Build up **asset-based threat profiles**
2. Identify **vulnerabilities in the infrastructure** which could lead to unauthorized action
3. Develop a **security strategy and plans**

Plus: developed for **CERT** at **Carnegie Mellon University, USA**; four variants — **OCTAVE**, **OCTAVE-S** (small enterprises, limited resources), **OCTAVE ALLEGRO** (advanced IT structure), **OCTAVE FORTE**.

`[CONFLICT]` — see §8.2. You listed OCTAVE once as "3 steps, count without explanation" and later as "not important".

### 5.8 ISO/IEC 27002 — the 14-category enumeration
**Why it matters as a project:** it is part of a series developed **jointly by ISO and IEC**, currently **44 complete or planned standards**, covering information security in general and in specific areas (finance, energy supply, digital evidence, cloud computing).

**The number to remember: 14.** The **2022** version describes targets within **14 categories**:

| # | Category | # | Category |
|:---:|:---|:---:|:---|
| 1 | Information security policies | 8 | Operation security |
| 2 | Organization of information security | 9 | Communication security |
| 3 | Human resource security | 10 | System acquisition, development and maintenance |
| 4 | Asset management | 11 | Supplier relationships |
| 5 | Access control | 12 | Information security incident management |
| 6 | Cryptography | 13 | Information security aspects of business continuity management |
| 7 | Physical and environmental security | 14 | Compliance with legal and contractual requirements |

The list is **logically ordered** — policies → organization → people → assets → access → crypto → physical → operations → communications → development → suppliers → incidents → continuity → compliance. Learn the logic and the 14 fall out in order.

### 5.9 The analysis frameworks — five, and how they differ
| Framework | Its distinguishing offer |
|:---|:---|
| **COBIT** | Objectives for measures used to **manage risk** |
| **COSO** | The **internal processes** a company must follow for suitably low risk |
| **FAIR** | A **taxonomy** of risk factors + a **standard for naming** risk quantities + a **model for calculating** risk — the only one with a calculation model |
| **ISO/IEC 27002** | A **checklist** of what must be considered for a secure system |
| **OCTAVE** | The **process** of analysing threats and risks and finding countermeasures |

### 5.10 Cyber risk assessment — the four components
You said you do not remember her discussing these; they are in the file as a numbered list:
1. **Risk Identification** — pinpointing potential cyber threats (malware, phishing, ransomware, data breaches…)
2. **Risk Evaluation** — analysing the likelihood of each risk materialising and the severity of its impact
3. **Risk Mitigation** — strategies to reduce or manage risks; controls such as firewalls, encryption, user education, backup systems
4. **Monitoring and Review** — continuously observing the cyber landscape, updating defences, reassessing as new threats emerge

---

## 6. Not important (your verdict, recorded)

| Item | Your call |
|:---|:---|
| **Develop a risk-management program** (NIST block) | Not important |
| **Use NIST security controls** (NIST block) | Not important |
| **OCTAVE** (second mention) | Not important — **conflicts with §5.7, flagged in §8.2** |

---

## 7. Coverage boundary — where the lecture stopped

Your report: she **finished explaining up to Authentication** and did not complete the rest. On that reading, the following sections exist in the file but were **not covered in the lecture**:

- Magnetic stripe readers · Smart cards · RFID badges · Biometric scanners
- Remote-access monitoring · Automated access-control systems
- Security policy (the closing section) · Cyber security policy
- **Cyber risk assessment and management** (the four components in §5.10)

`[CONFLICT]` — you also said she *did* talk about "1. Risk Identification and the rest", which sits in that uncovered block. See §8.3.

---

## 8. Open items — please confirm

### 8.1 The equation letters do not match the file
| | Basic risk | Risk reduction |
|:---|:---|:---|
| **The delivered file says** | `S = F × K` | `R = S / M` |
| **Your lecture report says** | `f = s · k` | `f = s / n`, with `n` = number of threats |

**The structure is now settled — independently of the letters.** `W02_Formulas.md` proves both equations on their own terms:

- **`S = F × K`** — sound. Orthodox likelihood × consequence form; **multiplication is required, not addition**, because it enforces that *both* factors must matter (a huge frequency cannot compensate for zero consequence).
- **`R = S / M`** — sound **provided `M` is a protective factor ≥ 1**, not a raw count. Proof: at `M = 0` the formula divides by zero, and for `0 < M < 1` it gives residual risk *greater* than inherent risk — impossible. On the reading `M ≥ 1` it is **algebraically identical** to the industry-standard `R = S × (1 − Control Effectiveness)`.
- **Your reported version fails a logical test.** If `f` is the subject of both equations, the symbol `s` must mean "frequency" in one and "risk" in the other — a contradiction. And a denominator of *number of threats* fails twice: more threats would mean *less* risk, and zero threats would divide by zero. **A defensive quantity belongs in the denominator; a threat quantity does not.**

**Carry this into the exam:**

```text
risk          = frequency × consequences     (both must matter → multiply)
residual risk = risk ÷ protection factor     (protection ≥ 1; never divides by zero)
```

That holds whatever letters the book prints. **Still worth one look at your paper notes** — if they show `S`, `F`, `K` and `R`, `S`, `M`, the booklet is reproducing the book exactly and you can drill it as printed.

### 8.2 OCTAVE — important or not?
You said both. My reading of her highlighting is that she marked OCTAVE **yellow** (framework list) and its **three phases red** (explain them) — which points to *important*. But you were in the room. Which is it?

### 8.3 Where exactly did she stop?
You said she stopped at Authentication, but also that she discussed the Risk Identification list, which comes after it in the file. Did she skip ahead to the risk-assessment components, or was that a different part of the session?

### 8.4 "Debug" — I cannot find it
You mentioned *"the debug has 5 steps."* I searched the file: the word **debug does not appear anywhere in this booklet**, and there is no 5-step list other than the **five risk-mitigation strategies** (which you listed separately). A search across the whole Cyber Security subject folder found nothing either.

Candidates, so you can just point:
- the **five risk-management strategies** (§5.3)?
- the **four PDCA elements** (§5.6)?
- something she wrote on the board that is **not in this booklet** — in which case I need the notes or a photo?

### 8.5 The illustrated booklet
Still needed. The delivered DOCX contains **zero images** — every figure is referenced in the text but absent from the file.

---

*Exam-focus sheet built 2026-09-23. Highlight map extracted mechanically from `word/document.xml`; every other item traced to the delivered booklet. Lecture report recorded as reported. Nothing resolved silently — see §8.*
