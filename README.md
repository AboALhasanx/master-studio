# 🎓 Master Studio — Personal Academic Operating System

[![Academic Year](https://img.shields.io/badge/Academic%20Year-Preparatory%20(1st%20Year)-blue.svg)](#)
[![Degree](https://img.shields.io/badge/Degree-Master%20of%20Computer%20Science-success.svg)](#)
[![Institution](https://img.shields.io/badge/Institution-University%20of%20Wasit-orange.svg)](#)
[![Zero-SaaS](https://img.shields.io/badge/Toolchain-Zero--SaaS%20%2F%20Local-purple.svg)](#)
[![Free-Model Ready](https://img.shields.io/badge/Models-100%25%20Free%20%26%20Open-brightgreen.svg)](#)

An agent-native, file-driven personal university knowledge vault designed for the preparatory (coursework) stage of the **Master of Computer Science (MCS)** program at the **College of Computer Science & Information Technology, University of Wasit**.

---

## 🆓 Free-Model & Vendor-Agnostic Architecture

Master Studio is deliberately built to have **zero lock-in** to any proprietary model or vendor. You can operate this entire studio for $0 using:

| Harness | Command | Default Free Model Engine | Context File |
|---|---|---|---|
| **Freebuff** | `freebuff` | DeepSeek V4 Flash / MiMo 2.5 / MiniMax | `knowledge.md` |
| **OpenCode** | `opencode` | `free-router/free-default` / DeepSeek V4 | `opencode.json` |
| **OMP** | `omp` | Open / Free endpoints or local models | `AGENTS.md` |
| **Cursor / Cline** | *(open workspace)* | Local Ollama / Groq / Free API tiers | `skills/` & `AGENTS.md` |

Every prompt in this vault uses **strict markdown structural contracts**, tables, and code blocks rather than vendor-specific tags. This guarantees that fast, free, open-weights models (DeepSeek, Qwen, MiMo, LLaMA) generate accurate notes, diagrams, and slide decks without hallucinations.

### 💬 Talk-Only Student Experience (Zero CLI Memorization)

**You never need to remember command-line commands, python arguments, or tool flags.**

Whenever you launch **Freebuff**, **OpenCode**, or **OMP**, you simply talk in natural conversation. The AI agent automatically detects your intent and executes all tools in the background:
* *"Read the new lecture PDF Dr. Ali sent"* $\rightarrow$ Agent runs `pdf_reader.py` and produces the note.
* *"Export my notes to Word / PowerPoint for OnlyOffice"* $\rightarrow$ Agent runs `office_exporter.py` in the background.
* *"Quiz me on this week"* $\rightarrow$ Agent conducts an interactive oral exam in chat and logs your score to `PROGRESS_ANALYTICS.md`.
* *"Save and sync to GitHub"* $\rightarrow$ Agent commits and pushes your work automatically.


### 🌐 Studying on the Go with Free Web/Mobile Chatbots (ChatGPT, Qwen, DeepSeek, Gemini)

If you are away from your PC and using free web/mobile chatbots on your phone, you can feed your Master Studio context into any chatbot in seconds:

1. **Instant Repository Ingestion via GitIngest (Zero Install):**
   * Replace `github.com` with `gitingest.com` in your browser:  
     👉 **[https://gitingest.com/AboALhasanx/master-studio](https://gitingest.com/AboALhasanx/master-studio)**
   * Or ingest a specific course:  
     👉 **[https://gitingest.com/AboALhasanx/master-studio/tree/master/01_Semester_1/04_Advanced_Software_Eng](https://gitingest.com/AboALhasanx/master-studio/tree/master/01_Semester_1/04_Advanced_Software_Eng)**
   * Click **"Copy"** and paste the entire structured course context directly into **ChatGPT Free**, **Qwen Chat**, **DeepSeek**, or **Gemini**.

2. **Direct Web Browsing via Raw GitHub URLs:**
   * Paste the public raw URL of any study note directly into the chat:
     ```text
     https://raw.githubusercontent.com/AboALhasanx/master-studio/master/01_Semester_1/04_Advanced_Software_Eng/03_Study_Notes/Week_01_Architecture_Tactics.md
     ```
   * Prompt: *"Read this URL and quiz me on the architecture tactics as my academic examiner."*

3. **Local Subject Packer (`pack_subject.py`):**
   * Bundle an entire course into a single compact file (< 20k tokens):
     ```bash
     python "90_Shared_Toolbox/tools/pack_subject.py" 04
     ```
   * Drag-and-drop the generated `chatbot_digest.md` into ChatGPT or Qwen!

---

## 🏛️ Academic Framework & Regulations

In accordance with Iraqi Ministry of Higher Education and University of Wasit postgraduate statutes:
* **Degree Duration:** 2 Years (Year 1: Preparatory Coursework across two 16-week terms; Year 2: Research & Thesis).
* **Coursework Passing Standard:** Minimum **60%** in every individual subject.
* **Transition GPA Floor:** Minimum cumulative GPA of **70%** (ministerial baseline) or **75%** (institutional target) required to register the thesis research topic.
* **Transition Milestone:** Defense of thesis proposal before a 3-member departmental committee (*اللجنة الثلاثية*).

---

## 📂 Architecture Overview

```text
Master-Studio/
├── AGENTS.md                            <-- Master directives & anti-hallucination rules
├── knowledge.md                         <-- Freebuff / Codebuff project context & routing
├── opencode.json                        <-- OpenCode free-router configuration
│
├── 00_STUDIO_HUB/                       <-- Continuous Memory & Core Governance
│   ├── ACTIVE_STATE.md                  <-- Fast-boot session state (< 100 lines)
│   ├── LEARNER_MODEL.md                 <-- Cognitive profile & mastery tracker (< 100 lines)
│   ├── ACADEMIC_REGULATIONS.md          <-- Full ministerial & university statute dossier
│   ├── GPA_TRACKER.md                   <-- Live cumulative GPA calculation matrix
│   ├── templates/                       <-- Standardized templates (Notes, Marp, MCQs)
│   └── agents/                          <-- Personas (@tutor, @examiner, @seminar, @scout)
│
├── 01_Semester_1/                       <-- Current Coursework Term
│   ├── 00_Semester1_Schedule.md         <-- Official weekly lecture schedule
│   ├── 01_Cyber_Security/               <-- Dr. Huda Lafta Majeed
│   ├── 02_English_Language/             <-- Dr. Haidar Akab Alwan
│   ├── 03_Data_Mining/                  <-- Dr. Ahmed Shakir Abd Al-Rida
│   ├── 04_Advanced_Software_Eng/        <-- Dr. Ali Fahim Ni'ma (3 credit hours)
│   ├── 05_Soft_Computing/               <-- Dr. Abdul Hadi Mohammed Adkhil
│   └── 06_Artificial_Intelligence/      <-- Dr. Saif Ali Al-Saidi (3 credit hours)
│
├── 02_Semester_2/                       <-- Spring Term (Scaffolded)
├── 03_Thesis_&_Research_Transition/     <-- Year 2 Gateway (Committee Guidelines & Topics)
├── skills/                              <-- Open Agent Skills standard (tutor, examiner, seminar, scout)
└── 90_Shared_Toolbox/                   <-- Shared Marp presentation themes & CSL styles
```

---

## 🤖 Specialized Agent Skills (`skills/`)

All agents implement the open [Agent Skills specification](https://agentskills.io) and run natively in any compatible tool:

* **`tutor` (The Socratic Instructor):** Deconstructs complex topics using a 3-tier progressive delivery: Intuitive Mental Model (Arabic analogy) $\rightarrow$ Formal Undergraduate Foundations $\rightarrow$ Master's-Level Rigor.
* **`examiner` (The Rigorous Assessor):** Generates high-discrimination scenario MCQs with nuanced distractors and conducts mock viva defense drills.
* **`seminar` (The Presentation Architect):** Ingests notes or primary papers and produces structured 10-slide [Marp](https://marp.app) presentations that compile directly to presentation-ready PDFs.
* **`scout` (The Academic Literature Scout):** Locates primary literature from IEEE, ACM, and arXiv with verified, clickable DOIs (`https://doi.org/...`).

---

## 🛠️ Toolchains (Zero Paid SaaS)

* **Slides & Seminars (PDF & PPTX):**
  - **PDF Export:** `npx @marp-team/marp-cli seminar.md -o seminar.pdf --allow-local-files`
  - **PowerPoint (.pptx for OnlyOffice / MS Office):**
    ```bash
    python "90_Shared_Toolbox/tools/office_exporter.py" pptx seminar.md
    ```
* **Word Documents (.docx for OnlyOffice / MS Office):**
  - Compile study notes or research reports directly to styled Word documents:
    ```bash
    python "90_Shared_Toolbox/tools/office_exporter.py" docx note.md
    ```
* **PDF-to-Markdown Extraction (100% Local & Free):**
  - Convert dense academic PDFs, slides, and textbooks into clean Markdown:
    ```bash
    python "90_Shared_Toolbox/tools/pdf_reader.py" path/to/paper.pdf -o path/to/note.md
    ```
    Extracts multi-column research papers, tables, and mathematical formulas in milliseconds on CPU with zero cloud APIs.
* **Interactive Terminal Quizzing & Mastery Analytics:**
  - Run interactive exam simulations in your terminal with automated score tracking:
    ```bash
    python "90_Shared_Toolbox/tools/quiz_runner.py" path/to/quiz.json
    ```
    Grades choices live, gives bilingual explanations, and automatically appends your score and weak spots to `00_STUDIO_HUB/PROGRESS_ANALYTICS.md` and `00_STUDIO_HUB/LEARNER_MODEL.md`.
* **Architectural Diagrams:** Rendered natively via **Mermaid.js** C4 blocks.
* **Concept Mindmaps:** Interactive trees rendered with **Markmap**.
* **Spaced Repetition:** Flashcard blocks structured for direct Anki import.
---

## 📱 Multi-Device Experience

The vault is designed for seamless continuous synchronization:
1. **Desktop:** Agents (Freebuff, OpenCode, OMP) synthesize notes, search literature, and compile slides.
2. **Google Drive Sync:** Propagates file changes in near real-time.
3. **Android Tablet & Phone:** Open the folder directly in **Obsidian Mobile** for offline knowledge graph navigation during lectures, and view compiled seminar PDFs in any native viewer.
