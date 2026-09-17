# Master Studio

Agent-native personal university environment for a Master of Computer Science (MCS) candidate at the College of Computer Science & Information Technology, University of Wasit.

This vault is designed to be operated entirely through natural-language chat with AI agents — no CLI commands required from the student.

---

## Repository Structure

```
Master-Studio/
├── 00_STUDIO_HUB/              # Runtime state, learner model, GPA tracker, agent personas
│   ├── ACTIVE_STATE.md         #   Fast-boot session pointer (current week, subject, todos)
│   ├── LEARNER_MODEL.md        #   Cognitive profile, mastered concepts, spaced-repetition queue
│   ├── PROGRESS_ANALYTICS.md   #   Longitudinal quiz log and mastery radar
│   ├── GPA_TRACKER.md          #   Credit-weighted GPA calculator with threshold alerts
│   ├── ACADEMIC_REGULATIONS.md #   MOHESR / University of Wasit postgraduate rules
│   ├── agents/                 #   Detailed persona definitions (@tutor, @examiner, @seminar, @scout)
│   └── templates/              #   Markdown templates for notes, seminars, and quiz banks
│
├── 01_Semester_1/              # Fall 2026 — 6 courses, 13 credit hours
│   ├── 01_Cyber_Security/
│   ├── 02_English_Language/
│   ├── 03_Data_Mining/
│   ├── 04_Advanced_Software_Eng/
│   ├── 05_Soft_Computing/
│   └── 06_Artificial_Intelligence/
│
├── 02_Semester_2/              # Spring 2027 (placeholder)
├── 03_Thesis_&_Research_Transition/  # Committee guidelines & supervisor intelligence
│
├── 90_Shared_Toolbox/tools/    # Python utilities (office export, PDF reader, quiz runner)
├── 99_Archives/                # Personal documents (gitignored)
└── .mimocode/skills/           # Agent skills auto-loaded by MiMo Desktop
```

### Per-Subject Folder Convention

Every course follows the same layout:

| Folder | Purpose |
|:---|:---|
| `00_Doctor_Profile.md` | Instructor intelligence, exam patterns, grading tendencies |
| `01_Syllabus_&_Roadmap.md` | 16-week chronological syllabus with progress tracker |
| `02_Raw_Materials/` | Textbooks, lecture PDFs (gitignored — stored in Google Drive) |
| `03_Study_Notes/` | Bilingual master study notes (Markdown + Word) |
| `04_Academic_Papers/` | Verified literature with real DOIs |
| `05_Seminars_&_Slides/` | Marp seminar decks (Markdown + PDF + PPTX) |
| `06_Diagrams_&_Mindmaps/` | Architecture diagrams and visual summaries |
| `07_Quizzes_&_Anki/` | Scenario MCQ banks and spaced-repetition cards |

---

## Agent Skills

Four specialized agents operate inside this vault. They are defined in `.mimocode/skills/` and auto-loaded by MiMo Desktop.

| Skill | Trigger | Role |
|:---|:---|:---|
| `@tutor` | Conceptual learning | 3-tier bilingual explanations (Arabic intuition → formal English → Master's rigor) |
| `@examiner` | Quizzes & oral defense | High-discrimination scenario MCQs and viva simulation |
| `@seminar` | Slide decks | 10-slide academic Marp presentations |
| `@scout` | Literature search | IEEE/ACM papers with verified, clickable DOIs |

---

## Toolchain

All tools are local, free, and run offline:

| Tool | Purpose |
|:---|:---|
| `office_exporter.py` | Converts Markdown to native editable `.docx` / `.pptx` (projector-tuned) |
| `pdf_reader.py` | Extracts academic PDFs to Markdown (preserves two-column layout) |
| `quiz_runner.py` | Interactive terminal quiz with auto-grading and analytics logging |
| `pack_subject.py` | Bundles a subject folder for mobile / ChatGPT offline study |

---

## Academic Thresholds

| Threshold | Value | Meaning |
|:---|:---:|:---|
| Subject pass minimum | 60% | Below this = immediate failure (2nd attempt required) |
| Ministerial GPA floor | 70% | Legal minimum to transition to thesis phase |
| Studio target | 75% | Competitive standing for supervisor selection |
| Mastery buffer | 80% | Target score for concept validation |

---

## Current Status

- **Active semester:** Semester 1 (Fall 2026)
- **Active subject:** Advanced Software Engineering (CS603 / Dr. Ali Fahim Ni'ma)
- **Week:** 1 — Software Foundations & The Software Crisis
- **Content produced:** Study notes, seminar deck, diagrams, and quiz for Lecture 01

Other subjects are staged with syllabi and doctor profiles; study content is produced as lectures are delivered.

---

## Git Policy

- **Tracked:** Markdown notes, diagrams (PNG), quizzes (JSON), final `.docx` study notes, final `.pptx` seminar decks
- **Gitignored:** Textbooks and raw lecture PDFs (`02_Raw_Materials/`), personal archives, OS artifacts
- Large binary materials live in Google Drive; this repo holds the processed, agent-ready knowledge layer

---

## Feeding the Vault to a Free External Chatbot

This vault is built to be read by **any free web chatbot** — DeepSeek, Qwen, ChatGPT free tier, Gemini free tier — with nothing installed on the student's side. The GitHub repository is the transport layer between the vault and the model.

> **Hard requirement:** the repository must stay **PUBLIC**. A private repository cannot be ingested by a third-party service.

### Option 1 — Gitingest (web, zero install) ⭐ recommended

[Gitingest](https://gitingest.com) turns any Git repository into a single prompt-friendly text digest. Its signature trick is URL rewriting: **replace `hub` with `ingest`** in any GitHub URL.

| What you want to feed the chatbot | URL to open |
|:---|:---|
| The whole vault | `https://gitingest.com/AboALhasanx/master-studio` |
| One subject | `https://gitingest.com/AboALhasanx/master-studio/tree/master/01_Semester_1/02_English_Language` |
| One folder | `https://gitingest.com/AboALhasanx/master-studio/tree/master/01_Semester_1/02_English_Language/03_Study_Notes` |

Open the link → **Copy** (or *Download*) → paste into the chatbot.

**Measured sizes for this vault** (re-measure as content grows):

| Scope | Files | Digest size | Est. tokens | Practical for a free chatbot? |
|:---|:---:|:---:|:---:|:---|
| Whole repository | 71 | ~594 KB | ~141.5k | Only large-context models |
| One subject (`02_English_Language`) | 10 | ~129 KB | ~31.2k | ✅ Yes |
| One folder (`03_Study_Notes`) | 6 | ~98 KB | ~24.4k | ✅ Comfortable |

**Rule of thumb: ingest at subject or folder level, never the whole repo at once.**

### Option 2 — Gitingest CLI (local, offline, private)

Identical output, generated on your own machine — nothing is uploaded to a third party. Already installed in this vault's managed Python environment.

```bash
pip install gitingest
gitingest https://github.com/AboALhasanx/master-studio -o digest.txt
gitingest "https://github.com/AboALhasanx/master-studio/tree/master/01_Semester_1/02_English_Language" -o english.txt
```

Useful flags: `-o -` (print to stdout), `-i/--include-pattern`, `-e/--exclude-pattern`, `-s/--max-size`, `-t/--token` (private repos), `--include-gitignored`. Full list via `gitingest --help`.
Running it against the **local** folder (`gitingest "G:/My Drive/Master-Studio"`) automatically skips everything in `.gitignore` — so raw textbooks and archives are excluded for free.

### Option 3 — Repomix and DeepWiki (alternatives)

- **[Repomix](https://repomix.com)** — packs a repository into one LLM-friendly file; also runs locally via `npx repomix`. This repo's `.gitignore` already excludes its output (`repomix-output.*`).
- **[DeepWiki](https://deepwiki.com/AboALhasanx/master-studio)** — auto-generates an explorable wiki with Q&A from the repository. Best when you want to *browse and ask* rather than paste a prompt.

### Option 4 — Per-subject digest pack (built into this vault)

`90_Shared_Toolbox/tools/pack_subject.py` bundles one subject folder into a single self-contained digest tuned to this vault's structure. Generated packs are gitignored (`*digest*.md`).

### The Zero-CLI contract

The student never runs any of the above. In chat, just ask:

> *"Bundle the English subject for a chatbot."*
> *"Give me a digest of Unit 1 that I can paste into DeepSeek."*

The agent runs the tool in the background and hands back the file or the ready-to-paste text.
