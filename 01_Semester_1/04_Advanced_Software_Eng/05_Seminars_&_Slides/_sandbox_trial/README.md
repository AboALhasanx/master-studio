# Sandbox Trial — Chapter 5 Software Design (Source-Grounded)

> **Status:** TRIAL. Open for review.
> **Date:** 2026-10-05 · OpenCode (Muse Spark 1.3)
> **Supersedes:** the earlier `Ch5_Software_Design_Study_Notes.docx` (written from model knowledge = "slop"). Kept only for comparison.

## What this is

A **source-grounded** study document. It is not generated from the model's memory — it is reconstructed
from the extracted text of the source slide deck, and **every paragraph carries an anchor `[S:n]`** that
points to the exact slide that supports it. The structure (topics, headings, subtopics, branches) is taken
from the source; the density is expanded from the source's own wording, not invented.

**Deliverable (editable):** `Ch5_Software_Design_GROUNDED.docx` (24 pp)
- Cover · Table of Contents (press F9) · List of Figures
- 17 numbered sections with subsections, 11 code-authored figures, 3 tables (MCQ answers, exercises, coverage map)
- Section 16 = retrieval check (answers withheld), Section 17 = coverage map (term → slide)

## The grounding method

```
source slides (99) ──extract text──> SOURCE_extract_ch5.txt   (pymupdf, page-marked)
      │
      ├── read in full by the agent (not paraphrased from memory)
      ▼
Ch5_grounded_notes.md   ← every claim written as: sentence ... [S:slide]
      │                         titles/subtitles/branches = source outline
      ▼
build_grounded_docx.py  ──> Ch5_Software_Design_GROUNDED.docx (+ 11 figures)
      ▼
audit_grounded.py       ──> verifies: anchors in range 2..99, every section anchored,
                            figure order ascending, 11 images embedded, no leaked tokens
```

## QA result (grounded gate)

`audit_grounded.py` → **PASSED (errors=0, warnings=0)**
- 138 anchors, range 2..98, **59/99 slides explicitly cited** (the rest are figure-only slides)
- 11 figures, ascending order, 11 embedded images, 3 tables

## Figures (all authored as code — no slide images copied)

| Doc Fig | Content | Engine | Source |
|:--|:--|:--|:--|
| 1 | Design framework | Graphviz | S:3 Fig.1 |
| 2 | Conceptual vs technical | matplotlib | S:5 Fig.2 |
| 3 | Modularity vs cost | matplotlib | S:14 Fig.4 |
| 4 | High vs low coupling | matplotlib | S:15–16 Fig.5 |
| 5 | Coupling spectrum | matplotlib | S:19 Fig.7 |
| 6 | Common coupling | matplotlib | S:22 Fig.8 |
| 7 | Cohesion ladder | matplotlib | S:27 Fig.11 |
| 8 | Structure chart (update file) | Graphviz | S:43 Fig.18 |
| 9 | Class inheritance (Shape) | PlantUML | S:68 Fig.23 |
| 10 | OO pipeline | Graphviz | S:71–72 Fig.25 |
| 11 | Sequence (issue book) | PlantUML | S:81–83 case |

## Reproduce

```powershell
$env:PATH += ";C:\Program Files\Graphviz\bin"
python build_figures.py          # -> figures/*.png (11)
python build_grounded_docx.py    # md -> Ch5_Software_Design_GROUNDED.docx
python audit_grounded.py         # grounded QA gate (exit 0 = PASSED)
python "..\..\..\90_Shared_Toolbox\tools\office_to_pdf.py" Ch5_Software_Design_GROUNDED.docx -o Ch5_Software_Design_GROUNDED.pdf
```

## What a human should review

1. Press **F9** in Word to build the TOC.
2. Skim the red `[S:n]` anchors — they are the verification trail; each claim should match its slide.
3. The **MCQ answers (section 14)** are inferred from the source's orderings (Fig.7/Fig.11); the source prints no key. Confirm.
4. Figures 1, 3, 8, 9, 10, 11 are redrawn from the source figures; compare side-by-side with the PDF slides.

## Honest limits

- Anchors are added by the agent while writing; the audit checks they are *in range and present*, not that the
  prose is a perfect paraphrase of each slide. Human spot-check is still required.
- Slides 84–93 are figure-only (the library UML set); they are covered by redrawn figures 9–11, not by new prose.
- Numbers/definitions are faithful to the source wording; where the source is a figure, the figure is described.
