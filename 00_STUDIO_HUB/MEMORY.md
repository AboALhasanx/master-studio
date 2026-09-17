---
title: "Master Studio Persistent Memory"
type: "persistent-semantic-memory"
last_updated: "2026-09-17"
version: "1.0.0"
token_budget: "< 400 tokens"
---

# Master Studio: Persistent Semantic Memory Hub

> **Role:** Universal cross-agent persistent memory. Automatically loaded by any tool (OMP, OpenCode, MiMo Studio, FreeBuf, Cursor, Claude Code) upon session boot.
> **Philosophy:** Vendor-neutral, tool-free, 100% offline, local Git-versioned Markdown.

---

## 1. Student Identity & Cognitive Working Style
- **Degree Track:** Master of Computer Science (Coursework & Research Stage, 2026–2027), College of CS & IT, University of Wasit.
- **Target Cumulative GPA:** $\ge 85.0\%$ (Target Distinction; well above the legal ministerial transition floor of $70.0\%$).
- **Cognitive Style:** Architecture-first, systems-oriented, formal mathematical derivations, zero filler.

---

## 2. Universal Output Invariants (Zero-Tolerance Rules)
- **Emoji Policy:** Strictly zero decorative emojis in academic study notes, seminar slides, diagrams, and technical docs.
- **PowerPoint Presentation Standard:**
  - Sizing tuned for 30+ ft projector readability: Titles **31pt–34pt Bold Navy** (`#1E3A8A`), Primary Bullets **21pt** (line spacing 1.35), Sub-bullets **17.5pt Slate**, Slide Numbers **14pt Bold**.
  - **100% Native Vector Shapes:** Zero raster screenshot slides. All text boxes, titles, and tables must be native OpenXML shapes clickable and editable in OnlyOffice, WPS, and Canva.
- **Word Document Standard (`.docx`):**
  - Native OpenXML BiDi support (`<w:bidi/>` and `dir="rtl"`) on all Arabic text to prevent inverted periods and parentheses.
  - Zero raw YAML frontmatter leaks on Page 1. Clean navy headers and auto-fitting tables.
- **Visual Diagram Standard:**
  - Rendered via code (Python Matplotlib / DirectWrite); zero browser screenshot scrollbars (horizontal or vertical rollers).
  - Arabic script must be reshaped using `arabic_reshaper` + `python-bidi` so letters are connected right-to-left.
  - Bounding boxes must be padded and solid; zero dashed or connecting lines cutting through the interior of text boxes.
- **Token & Resource Protection:**
  - Scanned PDFs (CamScanner, phone scans) must be parsed **locally via CPU RapidOCR (`rapidocr-onnxruntime`)** into Markdown before agent ingestion. Never feed raw multi-page scan images directly to multimodal LLMs to protect token and rate limits.

---

## 3. Instructor Dossiers & Exam Focus Points
- **Asst. Prof. Dr. Ali Fahim Ni'ma (`04_Advanced_Software_Eng` - 3 Credits):**
  - Demands exact numerical and kinematic modeling of failure case studies (e.g., Dhahran Patriot Missile: 24-bit fixed-point representation of $0.1\text{s}$, losing $0.000000095\text{s}/\text{tick}$, drifting $0.3433\text{s}$ over 100 hours $\rightarrow 687\text{m}$ gate shift at Mach 5).
  - Rigorous focus on Brooks' *No Silver Bullet* (Essential vs. Accidental complexity), the Dependability chain (Error $\rightarrow$ Fault $\rightarrow$ Failure), and the 8 ACM/IEEE Code of Ethics principles.
- **Asst. Prof. Dr. Haidar Akab Alwan (`02_English_Language` - 1 Credit):**
  - Emphasizes the Oxford Headway Upper-Intermediate tense matrix (Simple vs. Continuous vs. Perfect aspect).
  - Strictly penalizes conversational contractions (*'cause*, *I'm*) and ellipsis (*Been here two days*) in formal academic writing.
  - Focuses on time adverbial constraints (e.g., Present Perfect cannot take closed past time anchors like *in 2024* or *ages ago*).

---

## 4. Active Research Vectors (Thesis Candidate Areas)
- **Vector A:** Distributed consensus and fault tolerance under network partitioning.
- **Vector B:** Local-first, private AI agent architectures and verifiable execution environments.
- **Vector C:** Autonomous document parsing and semantic synthesis for academic knowledge graphs.

---

## 5. Hub Navigation Pointers
- **Active State Pointer:** `00_STUDIO_HUB/ACTIVE_STATE.md`
- **Cognitive Model:** `00_STUDIO_HUB/LEARNER_MODEL.md`
- **GPA Ledger:** `00_STUDIO_HUB/GPA_TRACKER.md`
- **Progress Radar:** `00_STUDIO_HUB/PROGRESS_ANALYTICS.md`
- **Local Dashboard:** `http://127.0.0.1:5000` (Flask service in `91_Dashboard/`)
- **College Buddy Ledger:** `00_STUDIO_HUB/COLLEGE_BUDDY.md` (Tracks deadlines, interactive debriefs, and professor announcements).
