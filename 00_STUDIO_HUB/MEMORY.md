---
title: "Master Studio Persistent Memory"
type: "persistent-semantic-memory"
last_updated: "2026-09-18"
version: "1.1.0"
token_budget: "< 400 tokens"
---

# Master Studio: Persistent Semantic Memory Hub

> **Role:** Universal cross-agent persistent memory. Automatically loaded by any tool (OMP, OpenCode, MiMo Studio, FreeBuff, Cursor, Claude Code) upon session boot.
> **Philosophy:** Vendor-neutral, tool-free, 100% offline, local Git-versioned Markdown.

---

## 1. Student Identity & Cognitive Working Style
- **Name:** Abu Al-Hasan (ابو الحسن) — GitHub `AboALhasanx`. From **Wasit, Iraq**.
- **Degree Track:** Master of Computer Science (Coursework Stage, 2026–2027), College of CS & IT, University of Wasit.
- **Background:** BSc Computer Science, graduated 2025–2026. Never worked — went straight into master's preparation. **Placed first in his cohort** on the master's differential exam, cumulative **83.46**.
- **Current Goal:** **Simply finish the master's.** No PhD / research track at this stage — do not build research scaffolding he did not ask for.
- **Cognitive Style:** Architecture-first, systems-oriented, formal mathematical derivations, zero filler.
- **Language:** Explain in his Iraqi Arabic, keep technical terms in English. Deliverables that leave the vault go out in formal academic English.

---

## 2. Agent Identity
- **I am Koko** 🐨 (named by Abu Al-Hasan, 2026-09-18). Full identity: `~/.workbuddy-ai/{SOUL,IDENTITY,USER}.md`.

---

## 3. Working Rules (learned the hard way — do not violate)
- **Zero-CLI.** He speaks; the agent runs every command. Never ask him to run anything.
- **Correct him bluntly.** He chose the direct option — say "هاي غلط" plainly, then give the fix.
- **Never assume we are done.** At the end of each block ask: is that it, or is there more?
- **Recap at every section transition.** What we covered, what is solved, where we are.
- **Go topic-by-topic, in order.** He will stop you if you jump ahead.
- **Professor statements are authoritative.** Record them verbatim. Never flag one as "needing clarification" or suggest challenging it.
- **Only record deadlines he reports.** Never infer one from a syllabus. Reminders stay soft.
- **Announce before deleting anything**, anywhere — including agent config folders.
- **Verify before asserting.** He asked for this explicitly and catches real errors.
- **Don't over-abbreviate.** He wants detail, not compression.

---

## 4. Repository & External Access (standing constraint)
- Repo `https://github.com/AboALhasanx/master-studio` must stay **PUBLIC** — it is the transport layer for feeding free web chatbots.
- **Gitingest** is the digest tool: swap `hub` → `ingest`. Per subject/folder only, never the whole repo (~141k tokens).
- Full details: `.workbuddy-ai/memory/MEMORY.md`.

---

## 5. Universal Output Invariants (Zero-Tolerance Rules)
- **Emoji Policy:** Strictly zero decorative emojis in academic study notes, seminar slides, diagrams, and technical docs.
- **PowerPoint Presentation Standard:**
  - Titles **31pt–34pt Bold Navy** (`#1E3A8A`), Primary Bullets **21pt** (line spacing 1.35), Sub-bullets **17.5pt Slate**, Slide Numbers **14pt Bold**.
  - **100% Native Vector Shapes:** zero raster screenshot slides; all shapes native OpenXML, editable in OnlyOffice / WPS / Canva.
- **Word Document Standard (`.docx`):** native OpenXML BiDi (`<w:bidi/>`, `dir="rtl"`) on Arabic text to prevent inverted punctuation; zero raw YAML frontmatter leaks on page 1.
- **Visual Diagram Standard:** rendered via code (Matplotlib / DirectWrite); no browser-screenshot scrollbars; Arabic reshaped with `arabic_reshaper` + `python-bidi`; padded solid bounding boxes, no lines cutting through text.
- **Scanned PDFs — CORRECTED 2026-09-18:** the old instruction to parse scans via `rapidocr-onnxruntime` is **stale — RapidOCR is NOT installed** in the managed venv. The working method is: render pages with `pymupdf` (`page.get_pixmap(dpi=150)`) and read them **as images**. For a PDF that has a text layer, just extract the text — and check `page.annots()` for the student's own annotations, which is often the most valuable content on the page.

---

## 6. Instructor Dossiers & Exam Focus Points
- **Asst. Prof. Dr. Huda Lafta Majeed (`01_Cyber_Security` - 2 Credits):** 🔴 **Head of the Postgraduate Studies Department (مقررة القسم)** — her word is the reference; record her statements as given.
  - **Exam format (student-verified 2026-09-18):** numbers given → apply the formula; no numbers → **analytical scenario** answered as **step → CIA pillar → (techniques in parentheses)**.
  - **Daily quiz:** written/essay (not MCQ), ~10 min, start of lecture, **soft stakes** — a reading-compliance check.
  - Case-study chapter (Stuxnet / Colonial Pipeline / GDPR) is **excluded**.
  - The **CIA Triad + its technique lists must be memorised cold** — they are the vocabulary of every scenario answer.
- **Asst. Prof. Dr. Ali Fahim Ni'ma (`04_Advanced_Software_Eng` - 3 Credits):**
  - Exact numerical/kinematic modelling of failure cases (Dhahran Patriot Missile: 24-bit fixed-point of $0.1\text{s}$ → $0.3433\text{s}$ drift over 100 h → $687\text{m}$ gate shift at Mach 5).
  - Brooks' *No Silver Bullet* (Essential vs. Accidental complexity), the Dependability chain (Error → Fault → Error State → Failure), the 8 ACM/IEEE Code of Ethics principles.
- **Asst. Prof. Dr. Haidar Akab Alwan (`02_English_Language` - 1 Credit):**
  - Oxford Headway Upper-Intermediate tense matrix; time-adverbial constraints (Present Perfect cannot take closed past anchors).
  - Strictly penalises contractions and ellipsis in formal academic writing.
- **Prof. Dr. Saif Ali Al-Saidi (`06_Artificial_Intelligence` - 3 Credits):** ⏸️ **Course NOT started** — no material delivered as of 2026-09-18 (only a Telegram group and a request to use real names). He is also **Dean of the College**. AI is excluded from the active study plan until material appears.
- **Asst. Prof. Dr. Ahmed Shakir Abd Al-Rida (`03_Data_Mining` - 2 Credits):** attribute-type taxonomy (Nominal / Ordinal / Binary / Numerical) and data structures (Record / Transaction / Text / Sequence / Temporal / Spatial / Image / Graph).

---

## 7. Active Research Vectors (Thesis Candidate Areas — future, not current)
- **Vector A:** Distributed consensus and fault tolerance under network partitioning.
- **Vector B:** Local-first, private AI agent architectures and verifiable execution environments.
- **Vector C:** Autonomous document parsing and semantic synthesis for academic knowledge graphs.

---

## 8. Hub Navigation Pointers
- **Active State Pointer:** `00_STUDIO_HUB/ACTIVE_STATE.md`
- **Rolling Study Plan:** `00_STUDIO_HUB/STUDY_PLAN.md`
- **Cognitive Model:** `00_STUDIO_HUB/LEARNER_MODEL.md`
- **GPA Ledger:** `00_STUDIO_HUB/GPA_TRACKER.md`
- **Progress Radar:** `00_STUDIO_HUB/PROGRESS_ANALYTICS.md`
- **College Buddy Ledger:** `00_STUDIO_HUB/COLLEGE_BUDDY.md`
- **Session Journal:** `00_STUDIO_HUB/sessions/`
- **Local Dashboard:** `http://127.0.0.1:5000` (Flask service in `91_Dashboard/`)

- **Added 2026-09-19:** Data Mining Week 02 note: Week_02_Data_Types_and_Preparation.md — Gemini templates on lecture text, not a re-compression. URL data type = Nominal.

- **Added 2026-09-19:** Week 03 note: Week_03_Feature_Extraction_and_Portability.md — conversion matrix + similarity graph + info loss + doctor CT/X-ray pipeline. Cross-linked to Week 02, not a re-compression.

- **Added 2026-09-19:** GitHub push recipe 2026-09-19: if 403 Permission denied, clear Env:GITHUB_TOKEN (fine-grained PAT may lack write), then gh auth switch to keyring account (gho with repo scope) + gh auth setup-git + push. APPDATA still required.

- **Added 2026-09-19:** Soft Computing official Fall 2026: alaidi.net 8/9-8/12/2026; midterm 20/10 Weeks 1-6 fuzzy only; NO chain codes/ANFIS as weekly topics; only Lecture 1 posted online; Week 2 (15/9) materials not uploaded; next class Tue 22/9 Week 3 Fuzzy relations/propositions.

- **Added 2026-09-19:** SC Week 01 note rebuilt 2026-09-19 with student permission: Data Mining style — no AI-slop compression. File Week_01_Introduction_to_Soft_Computing.md. Calendar provisional (W1 intro-only in class; W2 unposted).

- **Added 2026-09-20:** Cyber W01 bilingual PDF: Week_01_Cybersecurity_Bilingual_EN_AR.pdf (11pp). Build via HTML + Edge headless print-to-pdf because MIMO_SOFFICE fails with 0xC0000135 missing DLL.

- **Added 2026-09-20:** 2026-09-20 Cyber quiz POSTPONED by Dr. Huda to next week; covers 2 booklets; booklet 2 NOT delivered to students yet (not Week 02); wait for student materials before new Cyber notes. English exam after Unit 1 Q Skills + Headway; research paper talk next week with academic vocabulary questions.

- **Added 2026-09-20:** 2026-09-20 clarifications: Huda booklet 2 still NOT delivered — random notes only; build notes AFTER booklet arrives (together). English research paper = any CS field + rich academic terminology. Headway grammar + Language Focus flagged important by student; today English lecture added little new.
