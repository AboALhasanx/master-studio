# Master Studio Study Note & Formatting Manifesto: The 100% Zero-Defect Gate

> **The Sovereign Law:** In Master Studio, **99.9% is a failure**. A study deliverable is either 100% mathematically, visually, and structurally pristine, or it is rejected.
> **Scope:** Universal Master Studio Directive — Mandatory across ALL 6 Postgraduate Coursework Subjects:
>   1. `01_Cyber_Security` (CS501 — Asst. Prof. Dr. Huda Lafta Majeed)
>   2. `02_English_Language` (CS502 — Asst. Prof. Dr. Haidar Akab Alwan)
>   3. `03_Data_Mining` (CS503 — Asst. Prof. Dr. Ahmed Shakir Abd Al-Rida)
>   4. `04_Advanced_Software_Eng` (CS504 — Asst. Prof. Dr. Ali Fahim Ni'ma)
>   5. `05_Soft_Computing` (CS505 — Prof. Dr. Abdul Hadi Mohammed Adkhil)
>   6. `06_Artificial_Intelligence` (CS506 — Prof. Dr. Saif Ali Al-Saidi)
>   And all subsequent Year 2 Master's Thesis & Research Transition Modules.
---

## 1. The Mathematical Formulations & Equation Guarantee
**Question:** *Do these updates support mathematical formulas and LaTeX equations?*
**Short Answer:** **YES, 100% natively.**

### How the Engine Protects Math:
1. **Atomic Token Isolation:** Display math (`$$...$$`) and inline math (`$...$`) are extracted into immutable `@@MATH_N@@` tokens *before* any linter, regex, or HTML sanitizer touches the text.
2. **Untouched Restoration:** Math blocks are restored immediately prior to DOM rendering, guaranteeing that backslashes (`\Delta`, `\sum`, `\mathcal{O}`), subscripts (`_i`), and multiplication symbols (`\times`) are never corrupted.
3. **KaTeX + DirectWrite Rendering:** Display math is wrapped in `<div class="math-block" dir="ltr">` and inline math in `<span class="math-inline" dir="ltr">`, rendered with sub-pixel DirectWrite typography that never flips in Arabic RTL text.
4. **Empirically Proven Across All Curricular Subjects:**
   - **Cyber Security (CS501):** Risk formulation pipeline $S = F \times K$ and $R = S / M$.
   - **Data Mining (CS503):** Minkowski distances $D(x, y) = (\sum |x_i - y_i|^p)^{1/p}$, cosine similarities, and entropy calculations.
   - **Advanced Software Eng (CS504):** 24-bit fixed-point clock drift kinematics $\Delta t_{\text{drift}} = 9.5367 \times 10^{-8} \text{ s}$.
   - **Soft Computing (CS505):** Fuzzy membership functions $\mu_{\tilde{A}}(x) \in [0, 1]$, triangular norms ($t$-norms, $s$-norms), and Cartesian relations.
   - **Artificial Intelligence (CS506):** Heuristic search evaluation functions $f(n) = g(n) + h(n)$ and probability distributions.
---

## 2. The 7 Inviolable Formatting Invariants

Every Markdown note and compiled PDF must satisfy these seven laws without exception:

### Law 1: Centered 3-Tier Minimalist Header
- **Top of Document:** Centered Eyebrow (`{{COURSE_ABBR}} WEEK {{WW}} — UNIT {{UU}}`), Centered Main Title (`21pt bold navy`), and Centered Subtitle (`11pt teal core thesis`).
  - *Universal Examples Across Courses:*
    - `CYBER WEEK 02 — UNIT 01` · `Inherent & Residual Risk Mechanics`
    - `DATA MINING WEEK 03 — UNIT 01` · `Feature Portability & Distance Metrics`
    - `SOFT COMPUTING WEEK 02 — UNIT 01` · `Fuzzy Membership & Set Operations`
    - `AI WEEK 01 — UNIT 01` · `State Space Search & Heuristic Formulation`
    - `ENGLISH UNIT 01` · `Grammar Invariants & Tense Distinctions`
    - `ASE WEEK 02 — UNIT 01` · `SDLC Fundamentals`
- **Zero Clutter:** No side university-metadata box (`University of Wasit...`) and no blue badge chip at the top. The running header already carries institution metadata on every page.
- **No Duplicate Headings:** The markdown body must not print a duplicate `# Unit XX` immediately beneath the header banner.
### Law 2: Direction-Sensitive Accent Borders (Language-Aware)
- If a blockquote, citation, or Q&A answer is in **English (LTR)**: the accent border is strictly on the **LEFT**.
- If a blockquote, citation, or Q&A answer is in **Arabic (RTL)**: the accent border is strictly on the **RIGHT**.
- The border direction is determined by the language of the content itself, regardless of whether the document root is RTL or LTR.

### Law 3: Visual Distinction Between Quotes & Q&A Cards
- **Textbook Citations (Verbatim Quotes):** Render on a `#f8fafc` slate background with a **3.5px Royal Blue border** (`#2563eb`).
- **Active Recall Q&A Cards (Retrieval Set):** Render as dedicated assessment cards:
  - Header: Slate `#f8fafc` with a deep navy question number badge (`1`, `2`, `RS-05-01`).
  - Answer Box: Soft mint-green `#f0fdf4` with a **4px Emerald Green border** (`#10b981`).
  - Zero label clutter: No redundant `Model Answer` or `Answer:` text.

### Law 4: Table Text Wrapping & Direction
- `white-space: nowrap;` is strictly prohibited on textual cells. All descriptions, citations, and notes MUST have `white-space: normal !important; word-wrap: break-word;`.
- Pure English tables in bilingual notes must be tagged `dir="ltr"` so columns and apostrophes never flip.

### Law 5: Balanced Markdown Syntax (The Asterisk Invariant)
- **Zero Unclosed Asterisks:** Never write `***Heading:**` or `***Text.*`.
- Bold headings inside quotes must be `**Heading:**`. Trailing punctuation must be `."` not `*."*`.
- Unclosed asterisks leak out of blockquotes and turn entire pages bold; this is an immediate gate failure.

### Law 6: Zero Backend Scaffolding / Prompt Leakage
- **Banned Tokens:** `File 01 of 10`, `File XX of YY`, `Built under Week_02_BUILD_PLAN.md`, `[THIN]`, `[VERIFY]`, `**EN.**`, `**AR.**`.
- **Banned Cross-File Chatter:** Never write `اربط هذا بالملف 02` or `(الملف 03 §4.5)` in student deliverables. Use academic references (`اربط هذا بالمفهوم السابق` or named models).

### Law 7: Strict Prohibition of ASCII Art (Real Vector Graphics Only)
- Never insert ASCII tree diagrams or boxes inside code fences (` ```text ... ↓ ... ``` `).
- All system kinematics, hierarchies, and transitions must be rendered as high-resolution 2x retina vector PNG/SVG graphics in `<subject>/06_Diagrams_&_Mindmaps/` and inlined via `![Caption|720](path.png)`.

---

## 3. The Inviolable Delivery Gate (Mandatory Pre-Flight Check)

NO STUDY NOTE OR PDF ARTIFACT MAY BE DELIVERED, ANNOUNCED, OR COMMITTED WITHOUT PASSING:

```bash
# Step 1: Deterministic Pre-Flight Linter & Auto-Fixer
python "90_Shared_Toolbox/tools/note_linter.py" "<path_to_note>.md" --fix --strict

# Step 2: Autonomous PDF Compilation
python "90_Shared_Toolbox/tools/pdf_exporter.py" "<path_to_note>.md" -t study_pack
```

### Strict Enforcement Protocol:
- If Step 1 exits with **Code 1 (FAILED)**:
  YOU MUST NOT deliver the note or PDF to the student or conclude your turn.
  Resolve all remaining manual issues, re-run, and **repeat until it exits with Code 0**.
- Zero exceptions across all models (Claude, GPT, DeepSeek, Qwen, WorkBuddy, or local LLMs).
