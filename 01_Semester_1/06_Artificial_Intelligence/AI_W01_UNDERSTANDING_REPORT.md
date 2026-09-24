# Artificial Intelligence — Week-01 Lecture: Understanding Report

> **Subject:** `06_Artificial_Intelligence` (CS605) — Prof. Dr. Saif Ali Al-Saidi
> **Purpose:** understand the two files the student provided before any study work begins.
> **Date:** 2026-09-25 · Koko

---

## 1. The textbook — confirmed title, edition and number

The professor assigned **Russell & Norvig, *Artificial Intelligence: A Modern Approach* (AIMA)**. Verified against the **publisher (Pearson)** and the **official AIMA site** (`aima.cs.berkeley.edu`):

| Field | Value |
|:--|:--|
| **Full title** | **Artificial Intelligence: A Modern Approach** |
| **Authors** | **Stuart Russell** (UC Berkeley) and **Peter Norvig** |
| **Edition (current)** | **4th edition** |
| **Publisher** | **Pearson** (Pearson Series in Artificial Intelligence) |
| **Year** | **2020** (US 4th ed.) · **Global Edition 2021–22** |
| **ISBN-13** | **978-0-13-461099-3** (US 4th ed.) · **978-1-292-40113-3** (Global 4th ed.) |
| **Editions so far** | 1st 1995 · 2nd 2003 · 3rd 2010 · **4th 2020/21** ← current |

**Why the 4th is the right one for this course:** the official table of contents opens with **Part I — Artificial Intelligence: Ch.1 Introduction (p.1)** and **Ch.2 Intelligent Agents (p.36)** — exactly the two chapters the Week-01 lecture covers.

⚠️ **Note on the first file you downloaded:** the file named `Artificial intelligence_ a modern approach.pdf` is **not** AIMA — by its title page and metadata it is **Michael Negnevitsky — *Artificial Intelligence: A Guide to Intelligent Systems*, 3rd Edition**, a different book. (Kept only as a secondary reference.)

✅ **You now have the correct book.** `Artificial Intelligence_ A Modern Approach (1).pdf` was verified and **is the real AIMA, 4th edition**:
- title page: *"Artificial Intelligence — A Modern Approach — Fourth Edition — Stuart J. Russell and Peter Norvig"* (with the contributing writers: Ming-Wei Chang, Jacob Devlin, Anca Dragan, David Forsyth, Ian Goodfellow, Jitendra M. Malik, Vikash Mansinghka, Judea Pearl, Michael Wooldridge);
- copyright page: *"© 2021, 2010, 2003 by Pearson Education, Inc."*;
- series: *Pearson Series in Artificial Intelligence*;
- **2145 pages**; contents opens with **1 Introduction (p.1)** and **2 Intelligent Agents (p.36)** — exactly the Week-01 lecture's scope.

> **Storage rule:** the full book PDF is **copyrighted** — it stays **local only** in `02_Raw_Materials/` (which is git-ignored), and is **never** committed to the public repository. Only page-anchored quotations and the official free figures go into the deliverables.

**Free, official companions** (no purchase needed) on `aima.cs.berkeley.edu`: the full table of contents, the preface, the bibliography, all **figures**, the **pseudocode**, the **exercises**, and the **code** (`github.com/aimacode`). These are extremely useful for building the ملزمة even before you have the physical book.

## 2. The lecture file you found (`ai-w1.pdf`) — **source identified exactly**

- **What it is:** **Lecture 1 ("Introduction") of `CptS 440 / 540 Artificial Intelligence`**, taught in the **School of Electrical Engineering and Computer Science (EECS), Washington State University (WSU)**.
- **Author:** **Prof. Diane J. Cook** — Regents Professor, School of EECS, WSU (her homepage is `eecs.wsu.edu/~cook/`; the slides live at `eecs.wsu.edu/~cook/ai/lectures/l1.pptx`). PDF metadata: title *"CptS 440 / 540 Artificial Intelligence"*, author *"EECS"*.
- **Verified by direct comparison:** the original `l1.pptx` was downloaded and it has **67 slides with titles identical to the PDF** — so `ai-w1.pdf` is a PDF export of that exact file. **This is one complete lecture**, not two.
- **What it covers:** the AIMA opening — **Chapter 1 (Introduction) *and* the first part of Chapter 2 (Intelligent Agents)** — in a single lecture.
- It is a **found reference lecture**, not the doctor's own slides (the doctor has still posted no material). It is a clean, standard treatment of the same content.

**Source line to cite:** *Diane J. Cook, "CptS 440/540 Artificial Intelligence — Lecture 1: Introduction", School of EECS, Washington State University.* `https://eecs.wsu.edu/~cook/ai/lectures/l1.pptx`

## 3. Where this sits in the vault's AI syllabus

The vault already holds the AI syllabus (CS605, Prof. Dr. Saif — who is also the College Dean):

| Week | Topic | AIMA |
|:--|:--|:--|
| **Week 01** | Introduction to Modern AI & the Rational Agent Paradigm — the four definitions, Turing Test, rationality, foundations | **Ch. 1** |
| **Week 02** | Intelligent Agent Architectures & PEAS — PEAS, the 7 environment dimensions, the 5 agent types | **Ch. 2** |

**Key observation:** this is **one single lecture**, and it carries the whole AIMA opening — the definitions and philosophy (Ch.1) *and* the agents/PEAS material (Ch.2). So it maps onto the vault's Week 01 **and** the start of Week 02, but it should be treated as **one unit of study**.

## 4. What the lecture actually covers (content map)

| Block | Slides | Content |
|:--|--:|:--|
| Why AI | 2–3 | motivation |
| **What is AI?** | 4–15 | the **four definitions grid**: think humanly · think rationally · act humanly · act rationally |
| Acting humanly | 16–19 | **Turing Test**, what it demands, the **Chinese Room** argument, Loebner Prize |
| The other three approaches | 20–22 | thinking humanly, thinking rationally, acting rationally |
| Foundations & history | 23–24 | philosophy, mathematics, economics, neuroscience; the historical arc |
| Components / rationality | 29–30 | parts of an AI system; **rationality vs omniscience** |
| **PEAS** | 31–32 | Performance · Environment · Actuators · Sensors (taxi example) |
| **Environment properties** | 33–48 | the 7 dimensions: observable, deterministic, episodic, static, discrete, single-agent, known |
| **Agent types** | 49–57 | Simple Reflex · Reflex with State · Goal-Based · Utility-Based · **Learning Agents** |
| Worked AI systems | 58–67 | Xavier, Pathfinder, TDGammon, Alvinn, robot soccer, softbots |

## 5. What we will do (proposed plan)

Following the exact method we used for Software Engineering and Data Mining:

1. **Lock the source.** Get the real **AIMA 4th ed.** (the file you have is Negnevitsky, not AIMA). The vault will hold it in `02_Raw_Materials/` (not published). The WSU Lecture 1 is already in the vault at `02_Raw_Materials/AI_W01_Introduction_Lecture_CptS440.pdf`.
2. **One ملزمة for this lecture** (as you said — it is a single complete lecture). A deep bilingual note covering everything it teaches: the four AI definitions, the Turing Test and the Chinese Room, the foundations and history, rationality vs omniscience, **PEAS**, the 7 environment dimensions, and the 5 agent architectures — with verbatim AIMA page anchors and the exam lens. → `03_Study_Notes/Lecture_01_AI_Introduction.md`.
3. **Seminar deck** — the same assertion-evidence deck we built for Feature Selection (images + speaker notes), if the doctor asks for a seminar.
4. **Deliver through the Delivery Gate** (`note_linter --strict` → export → render and inspect).

**Not doing yet:** anything beyond this lecture (search, CSP, games) — we go topic-by-topic.

## 6. Open questions for you

1. Do you have the **real AIMA 4th edition** anywhere (Drive, Telegram, a friend)? If not, I can look for a legitimate path.
2. `ai-w1.pdf` is **Prof. Diane Cook's WSU Lecture 1** (confirmed). Is that the material the doctor pointed you to, or a resource you found yourself? It matters for how strictly we follow it.
