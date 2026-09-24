# Master Studio Standard Operating Procedure (SOP): Academic Research, Note Authoring & Publishing Lifecycle

> **Scope:** Universal Master Studio Protocol — Mandatory across **ALL 6 Postgraduate Coursework Subjects** (`01_Cyber_Security`, `02_English_Language`, `03_Data_Mining`, `04_Advanced_Software_Eng`, `05_Soft_Computing`, `06_Artificial_Intelligence`) and Thesis Modules for all AI agents (Oh My Pi, OpenCode, MiMo, Codex, Cursor, WorkBuddy).
> **Authority:** Root Behavioral Governance Directive (`AGENTS.md`).

---

## 1. Executive Philosophy: True Pedagogical Learning vs. AI-Slop Compression

In postgraduate Master of Computer Science coursework at the University of Wasit, dry summaries and bulleted glossaries are actively harmful.
Academic research (*IJERT 15(5), DOI 10.5281/zenodo.20522459*) proves that AI-generated summaries produce **high student confidence paired with significantly lower exam performance**, particularly on deep analytical and scenario-based questions where professors grade most strictly.

### The Inviolable Master Studio Principle:
> **We do not write summaries. We build deep pedagogical instruments that teach from first principles.**
> Every deliverable must deconstruct the architectural "why", provide intuitive mental models before formal definitions, quote authoritative textbooks verbatim with page anchors, explain engineering rationales bilingually, and provide active recall self-assessment.

---

## 2. The 5-Stage Authoring & Publishing Lifecycle

Every lecture note and study artifact must progress through this standardized five-stage pipeline:

```
+-----------------------------------------------------------------------------------------------+
|                             MASTER STUDIO 5-STAGE ARTIFACT LIFECYCLE                          |
|                                                                                               |
|  [Stage 1: Ingest & Triangulate]  -->  [Stage 2: Modular Unit Partitioning]                   |
|  - Sift primary vs secondary book      - 10-Unit Ingestion Architecture                       |
|  - Cross-reference Web & Standards     - Zero-Leakage Academic Naming (Unit 01 vs File 01)    |
|                                                                                               |
|  [Stage 3: Deep Pedagogical Author] --> [Stage 4: High-Res Vector Assets]                     |
|  - Narrative Spine ("The Why")         - 2x Retina PNG/SVG in 06_Diagrams_&_Mindmaps/         |
|  - Feynman 9-Year-Old + Verbatim Quote - Strictly ZERO ASCII Code-Box Art                     |
|  - Bilingual Iraqi-Arabic Engineering                                                         |
|  - Active Recall Q&A Cards                                                                    |
|                                                                                               |
|  [Stage 5: Autonomous 1-Click Publishing]                                                     |
|  - DirectWrite Chromium PDF Exporter   - Centered 3-Tier Header (Eyebrow + Main + Subtitle)   |
|  - Direction-Sensitive Borders (LTR/RTL)- Iterative Multi-Viewer Windows File Lock Resolver   |
+-----------------------------------------------------------------------------------------------+
```

---

## 3. Stage 1: Ingestion, Sifting & Triangulation (Books + Web + Standards)

Agents must never blindly ingest or regurgitate an entire textbook chapter. You must act as an expert research aide who sifts gold from noise.

### 3.1. Authority Hierarchy
1. **Primary Course Textbooks:** Identify which textbook is the *literal* primary source for the lecture terms (e.g. Mall for SDLC models, Sommerville for general process theory and Agile, Sharp for Cyber Risk, Han & Kamber for Data Mining).
2. **Canonical Standards:** ISO/IEC/IEEE (e.g., ISO/IEC 12207, IEEE 1012), NIST Special Publications (SP 800-30, SP 800-53), SWEBOK v4.
3. **Targeted Web & Expert Consensus:** IEEE Xplore, ACM Digital Library, ArXiv, verified university lecture notes to clarify discrepancies or ambiguous lecture slides.

### 3.2. The Sifting Matrix: What to Keep vs. What to Skip

| Dimension | KEEP & EXPAND (Essential Gold) | SKIP & DISCARD (Dead Weight) |
|:---|:---|:---|
| **Definitions** | • Word-for-word authoritative quotations with exact page numbers.<br>• Competing definitions when authors disagree (e.g. Mall vs. Sommerville). | • Vague, generic dictionary summaries.<br>• Unattributed paraphrasing. |
| **Architectural Rationale** | • Why this model/algorithm was invented.<br>• What exact failure in the previous paradigm it resolves. | • Promotional marketing talk or generic vendor claims. |
| **Mechanics & Boundaries** | • Mathematical formulations, state transitions, runtime bounds.<br>• Boundary conditions where the model breaks (e.g. requirements instability). | • Historical trivia that has no technical or exam bearing. |
| **Exam Pitfalls** | • Professor's Exam Traps (*مصائد الامتحان*).<br>• Countable lists and categorical classifications professors memorize. | • Repetitive restatements across multiple secondary textbooks that add no new technical distinction. |

### 3.3. Evaluation of Figures and Tables
- **When to Convert to Markdown Tables:** Tabular comparisons, multi-factor trade-offs, attribute matrices, and numerical thresholds. Ensure table columns wrap cleanly (`white-space: normal`).
- **When to Create Vector Graphics:** High-consequence structural hierarchies, state transition diagrams, kinematics, and process workflows.
  - **Standard:** Render at 2x retina sharpness using Playwright/HTML/SVG or Pillow into `<subject>/06_Diagrams_&_Mindmaps/<slug>.png`.
  - **Prohibition:** NEVER insert low-resolution blurry PDF screenshots or ASCII text art inside ` ```text ` blocks!
- **When to Omit:** Decorative clip-art, generic photos, unreadable microscopic scans that do not convey system kinematics.

---

## 4. Stage 2: Modular Unit Partitioning (Architecture vs. Presentation)

### 4.1. Why 10 Modular Units?
When an LLM attempts to synthesize 10 complex software models or 15 cyber security domains in a single pass, it suffers cognitive drift, hallucinates citations, and produces shallow summaries.
Partitioning the professor's syllabus into **modular unit files** (e.g. 10 files for ASE Week 02) isolates cognitive context and guarantees 100% textbook verification.

### 4.2. The Inviolable Zero-Leakage Law
**Backend chunking must NEVER leak into the student-facing deliverables:**
- **Prohibited:** `File 01 of 10`, `File XX of YY`, `Built under Week_02_BUILD_PLAN.md`, `[THIN]`, `[VERIFY]`, `**EN.**`, `**AR.**`.
- **Mandatory:** Use clean academic titles: `Unit 01: SDLC Fundamentals`, `Unit 02: Waterfall Family`, etc.
- The student reads an academic compendium, not an agent worklog!

---

## 5. Stage 3: Deep Pedagogical Authoring (The 4-Pillar Method)

Every section must follow the Master Studio 4-Pillar Pedagogical Anatomy:

### 5.1. Pillar 1: The Narrative Spine ("The Why")
Every file must open with a **"Where this sits"** section:
- What did the previous unit solve?
- What problem broke down that makes this new concept necessary?
- *Example Spine:* Requirements always change. Waterfall fails because it freezes requirements; Prototyping explores requirements; Incremental delivers slices; Spiral mitigates risk.

### 5.2. Pillar 2: Verbatim Canonical Anchor
Always provide the word-for-word textbook definition quoted directly before explaining it:
```markdown
> **Verbatim (Mall p.67):** *"It is well known that all living organisms undergo a life cycle. For example when a seed is planted, it germinates, grows into a full tree, and finally dies..."*
```
*(Rendered in PDF as a crisp slate card with a 3.5px Royal Blue accent border on the LEFT for English citations, or on the RIGHT for Arabic).*

### 5.3. Pillar 3: Feynman Intuition & Bilingual Engineering Rationale
Pair English technical terminology with deep, intuitive Iraqi-Arabic conceptual rationales (*الشرح المفاهيمي والتعليلات الهندسية*):
- **English technical terms:** Write cleanly in English without awkward literal translation or parenthetical clutter.
- **Arabic conceptual rationale:** Explain the mechanical cause-and-effect, why the system behaves this way, and how the professor tests this in oral viva or essay exams.

### 5.4. Pillar 4: Active Recall Retrieval Set (End of Unit)
Every unit MUST conclude with 10–12 demanding analytical, scenario-based questions with model answers.
Format in Markdown using bold numbered questions followed by blockquote answers:
```markdown
## Retrieval set

**1. Why does the software life cycle begin with a request rather than with software?**
> Because the term is defined on the biological analogy: it runs from *"an initial customer request"* to the point where the software is *"no longer useful to any user, and then it is discarded."* The request is the seed. (Mall p.67)
```
The PDF engine automatically transforms this into dedicated `.qa-card` assessment units (emerald green border, soft mint background, question number badge, zero `Model Answer` clutter).

---

## 6. Stage 4: Visual Vector Assets & Sizing Standards

1. **Storage Location:** `<subject>/06_Diagrams_&_Mindmaps/`.
2. **Obsidian Sizing Syntax:**
   - Single Centered Figure: `![Caption|720](relative/path/to/diagram.png)`
   - Compact Diagram: `![Caption|450](relative/path/to/diagram.png)`
   - Dual Side-by-Side Comparison:
     ```html
     <div class="fig-row">
       <img src="path/to/fig1.png" alt="Inherent Risk Matrix">
       <img src="path/to/fig2.png" alt="Residual Risk Matrix">
     </div>
     ```
3. **Whitespaces:** The engine automatically auto-crops white borders via Pillow, but always author clean margins.

---

## 7. Stage 5: Autonomous 1-Click Publishing (Zero-CLI Policy)

Whenever the student requests a PDF or when a unit is finished:
**YOU (the agent) must run the exporter autonomously in the background:**

```bash
python "90_Shared_Toolbox/tools/pdf_exporter.py" "<path_to_note>.md" -t study_pack
```

### 7.1. Frontmatter Contract for Clean Centered Headers
```yaml
---
title: "ASE Week 02 — Unit 01: SDLC Fundamentals"
subtitle: "The software life cycle, the process, its four activities, and why a team cannot work without one"
subject: "04_Advanced_Software_Eng"
week: 2
sources:
  - "Sommerville, Software Engineering, 9th ed., pp.44–46"
  - "Mall, Fundamentals of Software Engineering, 4th ed., pp.67–71"
type: "study compendium — source-derived"
---
```
### 7.2. Automated Layout Guarantees in `pdf_exporter.py`
- **Centered 3-Tier Header:** Displays Eyebrow (`ASE WEEK 02 — UNIT 01`), Main Title (`SDLC Fundamentals`), and Subtitle (`The software life cycle...`) centered at the top. Zero side-metadata clutter.
- **Top Heading Sanitization:** Automatically strips leading `# Title` from the body to eliminate duplicate headings.
- **Table Cell Text Wrapping:** Enforces `white-space: normal !important;` so table text wraps cleanly without overflow or clipping. Pure English tables in RTL notes get `dir="ltr"`.
- **Direction-Sensitive Borders:**
  - Royal Blue citation border is on the **LEFT** for English, **RIGHT** for Arabic.
  - Emerald Green Q&A border is on the **LEFT** for English, **RIGHT** for Arabic.
- **Multi-Viewer Windows File Lock Resolver:** Iteratively finds unlocked filenames (`_new.pdf`, `_v2.pdf`, `_v3.pdf`) if open in Adobe Acrobat or Edge.

---

## 8. Summary Checklist for Incoming Agents

Before concluding your turn or presenting a study note to the student, verify:

- [ ] **1. Canonical Sifting:** Primary source identified with exact page numbers; tangential padding discarded.
- [ ] **2. No Summary Slop:** The note *teaches* the narrative "why", provides Feynman intuition, verbatim quotes, and bilingual engineering rationales.
- [ ] **3. Clean Unit Title:** No `File 01 of 10` or backend build metadata visible to the student.
- [ ] **4. Zero Prompt Markers:** No `**EN.**`, `**AR.**`, `[THIN]`, or `[VERIFY]` in the text or tables.
- [ ] **5. High-Res Vector Diagrams:** No ASCII art in code blocks. High-DPI PNG/SVG used.
- [ ] **6. Differentiated Q&A Cards:** Retrieval Set formatted for `.qa-card` rendering with emerald borders.
- [ ] **7. Autonomous Compilation:** `pdf_exporter.py` executed in the background; verified output delivered with zero CLI friction for the candidate.
