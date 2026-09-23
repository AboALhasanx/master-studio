---
name: pdf_exporter
description: "Master Studio Academic PDF Publishing Engine. Converts Markdown study notes, lecture summaries, booklets, and exam sheets into publication-grade vector PDFs with native Arabic/BiDi DirectWrite text shaping, KaTeX math, embedded diagrams, and Master Studio pedagogical callouts."
---

# Master Studio Academic PDF Exporter (`pdf_exporter`)

Use this skill whenever the student asks to generate, export, compile, or produce a PDF document, booklet, lecture summary, or exam sheet.

## Trigger Phrases
- *"Make a PDF of this note"* / *"Export to PDF"* / *"Create a PDF booklet"*
- *"سوي بي دي اف"* / *"حول الملاحظة الى PDF"* / *"اطبع الملخص بي دي اف"* / *"سويه كتيب"*
- *"Generate an exam sheet"* / *"ورقة مراجعة امتحانية"*

---

## Autonomous Execution Directive (Zero-CLI for Student)

Whenever the student requests a PDF, **YOU (the agent) must autonomously run the exporter in the background**:

```bash
python "90_Shared_Toolbox/tools/pdf_exporter.py" "<path_to_note.md>"
```
Or via the Windows batch wrapper:
```cmd
"90_Shared_Toolbox/tools/export-pdf.bat" "<path_to_note.md>"
```

---

## Academic Templates (`--template` / `-t`)

1. **`study_pack` (Default):**
   - Standard lecture revision pack.
   - Includes University of Wasit + College of CS & IT header, course badge chip, large bilingual title, running headers, and running footers with `Page X of Y`.
   ```bash
   python "90_Shared_Toolbox/tools/pdf_exporter.py" "01_Semester_1/04_Advanced_Software_Eng/03_Study_Notes/W01_Lecture.md" -t study_pack
   ```

2. **`booklet`:**
   - Multi-page comprehensive study guide (10–40 pages).
   - Generates a full-page formal cover sheet (University branding, course, instructor, student, date) followed by topic sections.
   ```bash
   python "90_Shared_Toolbox/tools/pdf_exporter.py" "path/to/booklet.md" -t booklet
   ```

3. **`exam_sheet`:**
   - High-density 2-column revision sheet for 1–2 page pre-exam crunching.
   - Compact margins (10mm), 8.5pt font, compact tables and callouts.
   ```bash
   python "90_Shared_Toolbox/tools/pdf_exporter.py" "path/to/cheat_sheet.md" -t exam_sheet
   ```

4. **`glossary`:**
   - Formatted terminology cards with canonical IEEE definitions, Arabic conceptual rationales, and exam traps.

---

## Pedagogical Callout Syntax

The exporter automatically renders Master Studio callout cards:

| Markdown Syntax | Visual Card Output |
|---|---|
| `> [!TRAP]` or `> [!EXAM]` | **Red Caution Box:** *فخ الامتحان مع الدكتور (Professor's Exam Trap)* |
| `> [!FEYNMAN]` | **Teal Box:** *تبسيط فاينمان للطفل بعمر 9 سنوات (Feynman Analogy)* |
| `> [!CONCEPT]` or `> [!NOTE]` | **Blue Box:** *المفهوم الأكاديمي التأسيسي (Foundational Concept)* |
| `> [!CALC]` or `> [!MATH]` | **Amber Box:** *الاشتقاق والحسابات الرياضية (Mathematical Derivation)* |
| `> [!WARN]` or `> [!WARNING]` | **Deep Rose Box:** *تحذير ومغالطة شائعة (Common Fallacy / Warning)* |

---

## Image & Diagram Inlining

- Relative Markdown image links (e.g. `![Alt](06_Diagrams_&_Mindmaps/diagram.png)`) are automatically resolved, base64-encoded, and embedded inside `<div class="figure-box">` with centered captions and `page-break-inside: avoid;`.
- Never let images break across page boundaries.

---

## Math & Formula Formatting

- Always use standard LaTeX syntax:
  - Display math: `$$...$$`
  - Inline math: `$..$`
- The engine enforces strict `direction: ltr !important; unicode-bidi: isolate;` so math notation ($E = mc^2$, $\Delta t$, fractions) is never flipped in RTL text.
- When generating Markdown via Python, **always use raw strings `r"""..."""`** to prevent `\t` from eating LaTeX backslashes (`\text` $\rightarrow$ TAB + `ext`).
