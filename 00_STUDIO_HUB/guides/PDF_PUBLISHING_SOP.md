# Master Studio Standard Operating Procedure (SOP): Academic PDF Publishing Engine

> **Mandatory Reading for All Incoming Agents:** This is the canonical operational manual for generating, exporting, and publishing publication-grade academic vector PDFs within Master Studio (`G:/My Drive/Master-Studio/`).
> **Authority:** Derived from `AGENTS.md` Root Directives.

---

## 1. Operating Philosophy: Why PDF is King in Master Studio

In postgraduate computer science studies at the University of Wasit, digital lecture notes must transition into permanent, immutable, high-aesthetic study deliverables.
- **Markdown** is the source of truth for editing and semantic analysis.
- **PDF** is the ultimate student-facing revision asset: it preserves exact page geometry, vector diagrams, mathematical formulas, and typography across mobile phones, tablets, and desktop printouts.

Any incoming AI agent operating in this vault must adhere to the **Zero-CLI Rule**:
The student will ask in plain conversational language (*"Make a PDF"*, *"Export this note to PDF"*, *"سوي بي دي اف"*, *"اطبع الملخص"*).
**YOU (the agent) must autonomously run the underlying exporter in the background.** Never ask the student to run CLI commands.

---

## 2. Tool Architecture & Engine Fundamentals

The publishing toolchain resides in `90_Shared_Toolbox/tools/`:
- **Core Engine:** `90_Shared_Toolbox/tools/pdf_exporter.py`
- **Windows Batch Wrapper:** `90_Shared_Toolbox/tools/export-pdf.bat`

```
Markdown Document (.md)
         │
         ▼
pdf_exporter.py Pipeline:
  1. Frontmatter Extraction (Course, Instructor, Week, Title, Term)
  2. Math Block Isolation (Protected as atomic @@MATH_N@@ tokens)
  3. Master Studio Callout Transformation ([!TRAP], [!FEYNMAN], [!CONCEPT], [!CALC], [!WARN])
  4. Markdown-to-HTML Compilation (tables, fenced code, toc)
  5. BiDi Language Engine (Auto-tags pure English blocks LTR, isolates mixed Latin tokens)
  6. Leading English Definition Protection (bdi wrapper on acronym expansions)
  7. Base64 Diagram & Image Inlining (Auto-resolves relative vault paths)
  8. Table Formatter (Enforces dir="ltr" on numbers, units, and Latin text cells)
  9. Math Restoration (Restores pristine untouched LaTeX)
 10. Academic Template Assembly (Injects into study_pack, booklet, exam_sheet, or glossary)
         │
         ▼
Local Headless Chromium (Playwright DirectWrite / HarfBuzz Engine)
         │
         ▼
Publication-Grade Vector PDF (With native vector running headers/footers)
```

---

## 3. Template Catalog & Selection Matrix

When executing `pdf_exporter.py`, choose the appropriate template preset using `-t <template_name>`:

| Template Preset | Use Case | Page Geometry & Visual Features | Command Example |
|---|---|---|---|
| **`study_pack`** *(Default)* | Weekly lecture study notes & revision guides (4–15 pages). | University of Wasit header banner, course chips, full callouts, alternating zebra tables, running header & footer with `Page X of Y`. | `python 90_Shared_Toolbox/tools/pdf_exporter.py "path/to/note.md" -t study_pack` |
| **`booklet`** | Multi-topic comprehensive revision books (15–40+ pages). | Dedicated formal cover sheet (University branding, course, instructor, student, date), page break, topic dividers, running headers/footers. | `python 90_Shared_Toolbox/tools/pdf_exporter.py "path/to/booklet.md" -t booklet` |
| **`exam_sheet`** | 1–2 page dense pre-exam review sheets. | 2-column high-density layout, 8.5pt typography, 10mm compact margins, compact tables and callouts. Designed for double-sided printing. | `python 90_Shared_Toolbox/tools/pdf_exporter.py "path/to/sheet.md" -t exam_sheet` |
| **`glossary`** | Academic glossary terms (`08_Academic_Glossary/`). | Card-based terminology definitions with canonical IEEE quotes, Arabic rationales, and Professor Exam Traps. | `python 90_Shared_Toolbox/tools/pdf_exporter.py "path/to/terms.md" -t glossary` |

---

## 4. Authoring Guidelines for Flawless Academic PDFs

To ensure the PDF compiles with 100% aesthetic perfection, agents authoring Markdown notes must follow these rules:

### 4.1. YAML Frontmatter Standards
Always open study notes with clean YAML metadata:
```markdown
---
subject: CS504 Advanced Software Engineering
course: CS504 Advanced Software Engineering
title: أزمة البرمجيات وحسابات خطأ الباتريوت
subtitle: Software Crisis, Dependability & Kinematics Drift (Week 01)
instructor: Asst. Prof. Dr. Ali Fahim Ni'ma
term: Fall 2026
week: Week 01
---
```

### 4.2. Mathematical Formulas (KaTeX Rules)
- **Always use standard LaTeX delimiters:**
  - Display Math (equations on their own line):
    ```latex
    $$ \Delta t_{\text{tick}} = 9.5367 \times 10^{-8} \text{ seconds} $$
    ```
  - Inline Math (variables inside sentences):
    ```latex
    السيرفر المحصّن ($V_j = 0$) لا يمثل خطراً، لذلك قيمة $AS = \sum (E_j \times V_j \times A_j)$.
    ```
- **The Raw String Invariant (When writing Python scripts):**
  Never use standard strings for LaTeX; always use `r"""..."""`. Standard strings eat backslashes (`\t` becomes a TAB character, corrupting `\text` to TAB+`ext`).

### 4.3. Pedagogical Callout Cards
Master Studio uses visual cards for cognitive reinforcement:
```markdown
> [!TRAP] هل يمكن للذكاء الاصطناعي القضاء على أزمة البرمجيات؟
> **الجواب الأكاديمي الحاسم:** كلا قطعاً. الذكاء الاصطناعي يعالج فقط التعقيد العرضي (Accidental Complexity)...

> [!FEYNMAN] تشبيه فاينمان للطفل بعمر 9 سنوات
> تخيل أن لديك ساعة يد تتأخر جزءاً من المليون من الثانية في كل دقة...

> [!CONCEPT] التعقيد الجوهري مقابل التعقيد العرضي
> يميز فريد بروكس (Fred Brooks, 1986) بين نوعين من الصعوبات...

> [!CALC] اشتقاق معادلة خطأ التتبع الراداري
> الإزاحة الكلية تساوي حاصل ضرب سرعة الصاروخ في الخطأ الزمني...
```

### 4.4. Diagram & Image Insertion, Sizing & Cropping
- **Directory Standard:** Store all subject images and diagrams in `<subject>/06_Diagrams_&_Mindmaps/`.
- **Custom Width & Sizing Syntax (Obsidian-Style):**
  To prevent small diagrams from blowing up to full width, or to scale large flowcharts:
  ```markdown
  ![Caption|320](01_Semester_1/01_Cyber_Security/06_Diagrams_&_Mindmaps/fig.png)   <!-- 320px max-width -->
  ![Caption|50%](01_Semester_1/01_Cyber_Security/06_Diagrams_&_Mindmaps/fig.png)   <!-- 50% width -->
  ```
- **Side-by-Side Dual Figures (Comparison Row):**
  To place two related diagrams or before/after matrices side by side in a balanced flexbox row:
  ```html
  <div class="fig-row">
    <img src="path/to/fig1.png" alt="Figure 1: Inherent Risk Matrix">
    <img src="path/to/fig2.png" alt="Figure 2: Residual Risk Matrix">
  </div>
  ```
- **Automatic Whitespace Cropping (Pillow Built-In):**
  Scanned diagrams or screenshots with thick white/blank borders are automatically trimmed by the engine before inlining, saving up to 20–30% of dead page space.
- **Vector SVG Support:**
  SVGs are fully supported and rendered as razor-sharp vector paths inside the PDF.
- **Page Break Control:**
  All figure boxes enforce `page-break-inside: avoid;` so an image and its caption are never sliced in half across a page boundary.
---

## 5. Critical Engineering Pitfalls & Windows Gotchas

Incoming agents must memorize these five hard-won lessons to prevent recurring bugs:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    THE 9 LAWS OF MASTER STUDIO PDF ENGINE                               │
├───────────────────────────────┬─────────────────────────────────────────────────────────────────────────┤
│ 1. Windows File Lock Law      │ If the student has a PDF open in Adobe Acrobat or Edge, Windows locks   │
│                               │ the file exclusively. The engine catches PermissionError and safely     │
│                               │ writes to `filename_new.pdf`. Never crash or abandon the turn!          │
├───────────────────────────────┼─────────────────────────────────────────────────────────────────────────┤
│ 2. Math Protection Law        │ Never apply regex replacements (BiDi isolation, text substitutions) on  │
│                               │ restored math! Math must remain protected as atomic `@@MATH_N@@` tokens │
│                               │ until the absolute final step before template wrapping.                 │
├───────────────────────────────┼─────────────────────────────────────────────────────────────────────────┤
│ 3. Table Attribute Regex Law  │ Aligned Markdown tables (|:---|) generate `<td style="...">`. Matcher   │
│                               │ regexes must use `<td(\s*[^>]*)>(.*?)</td>`. Pure `<td>` matchers will   │
│                               │ silently fail on all styled tables.                                     │
├───────────────────────────────┼─────────────────────────────────────────────────────────────────────────┤
│ 4. Table Cell Text Wrapping   │ `white-space: nowrap;` is strictly reserved for pure numbers, dates,    │
│    & Direction Law            │ and short badges (`td.num-cell`). All text cells MUST have `white-space:│
│                               │ normal !important; word-wrap: break-word;` so descriptions wrap cleanly!│
│                               │ Pure English tables in RTL docs must be tagged `dir="ltr"`!             │
├───────────────────────────────┼─────────────────────────────────────────────────────────────────────────┤
│ 5. Leading Definition Law     │ If an Arabic paragraph starts with an English definition (e.g.          │
│                               │ `CVSS = Common Vulnerability... — معيار...`), the entire English formula│
│                               │ must be wrapped in `<bdi dir="ltr">` so BiDi won't invert word order.   │
├───────────────────────────────┼─────────────────────────────────────────────────────────────────────────┤
│ 6. Zero Backend Leakage Law   │ NEVER leak agent prompt scaffolding (`File 01 of 10`, `**EN.**`,        │
│                               │ `**AR.**`, `[THIN]`, or build footers) into student deliverables!       │
│                               │ Use academic titles (`Unit 01: SDLC Fundamentals`).                     │
├───────────────────────────────┼─────────────────────────────────────────────────────────────────────────┤
│ 7. Zero ASCII Art Law         │ ASCII code-box diagrams are strictly forbidden in PDFs! Render real     │
│                               │ vector PNG/SVG diagrams into `06_Diagrams_&_Mindmaps/` and inline them. │
├───────────────────────────────┼─────────────────────────────────────────────────────────────────────────┤
│ 8. BiDi Typography & Arrow Law│ Inline English tokens must be `display: inline; color: inherit;`. Never │
│                               │ turn English paragraphs blue or space-distorted! Sequence arrows (→)    │
│                               │ must be wrapped in LTR containers so BiDi never inverts the sequence.   │
├───────────────────────────────┼─────────────────────────────────────────────────────────────────────────┤
│ 9. Citation vs Q&A Card Law   │ Textbook quotations use `#f8fafc` background with a Royal Blue border   │
│                               │ (`#2563eb`). Active recall Q&A pairs MUST NEVER look like quotes; they  │
│                               │ render as dedicated `.qa-card`s with an emerald green (`#10b981`) answer│
│                               │ box. Borders are strictly language-sensitive (LEFT for LTR, RIGHT for   │
│                               │ RTL), regardless of document-level direction!                           │
└───────────────────────────────┴─────────────────────────────────────────────────────────────────────────┘
---

## 6. Pre-Delivery Verification Checklist (The Agent Gate)

Before claiming a PDF is generated and delivered to the student, the agent MUST run this 4-point verification check:

- [ ] **1. File Existence & Size:** Verify the output `.pdf` exists on disk and has a non-trivial size ($> 50 \text{ KB}$).
- [ ] **2. File Lock Notice:** Check stderr output. If `[*] Notice: ... is currently open in a PDF viewer. Writing to ..._new.pdf` was printed, inform the student: *"The original PDF was open in your viewer, so I saved the updated edition as `<filename>_new.pdf`."*
- [ ] **3. Page Count Sanity:** Ensure page count matches expectations (PyMuPDF `len(doc)` $> 0$).
- [ ] **4. Zero Delimiter Leak:** Ensure raw LaTeX symbols (`$E_j$`, `\sum`) or raw HTML tags (`<h1>`, `<bdi>`) did NOT leak as literal text in the rendered output.
- [ ] **5. Zero Backend Prompt Artifacts:** Verify that `File X of Y`, `**EN.**`, `**AR.**`, `[THIN]`, ASCII boxes, or internal build ledger footers do NOT appear in the final PDF.
- [ ] **6. Table Text Wrapping:** Inspect rendered tables to confirm text wraps properly inside cells with zero horizontal overflow or clipping.
- [ ] **7. Citation vs Q&A Differentiation:** Confirm textbook quotations use royal blue borders and Q&A answers use emerald green cards, with borders on the left for English and right for Arabic.
