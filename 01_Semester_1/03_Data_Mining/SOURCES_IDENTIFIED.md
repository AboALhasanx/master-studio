# Data Mining — Source Identification Report

> **Subject:** `03_Data_Mining` (CS602) — Asst. Prof. Dr. Ahmed Shakir Abd Al-Rida
> **Purpose:** identify the available sources *before* starting the Feature Selection seminar.
> **Date:** 2026-09-24 · Koko

---

## 1. The two textbooks (the "two sources")

### Source A — the classic textbook (name obvious from the filename)
- **Han, Jiawei; Kamber, Micheline; Pei, Jian — *Data Mining: Concepts and Techniques*, 3rd Edition.** The Morgan Kaufmann Series in Data Management Systems, 2011. **740 pp.**
- **File:** `02_Raw_Materials/The_Morgan_Kaufmann_Series_in_Data_Management_Systems_Jiawei_Han.pdf`
- **Confirmed** from the PDF metadata: title = *"Data Mining. Concepts and Techniques, 3rd Edition (The Morgan Kaufmann Series in Data Management Systems)"*, authors = *"Jiawei Han, Micheline Kamber, Jian Pei"*, publisher = *"Morgan Kaufmann 2011"*.
- **Role:** the **primary textbook**. The syllabus roadmap maps every week to a Han & Kamber chapter/section (e.g. W06 → Ch. 3 §3.4).

### Source B — the source whose name was unknown ⭐
- **Aggarwal, Charu C. — *Data Mining: The Textbook*.** Springer, Cham, 2015. **746 pp.** ISBN 978-3-319-14141-1 (eBook 978-3-319-14142-8), DOI 10.1007/978-3-319-14142-8.
- **File:** `02_Raw_Materials/Data Mining Textbook.pdf`
- **Why it was unknown:** the file is named generically *"Data Mining Textbook.pdf"* and carries **no PDF metadata** (title/author blank). Its identity was recovered from the title page (pp. 3–4): *"Charu C. Aggarwal — IBM T.J. Watson Research Center, Yorktown Heights, New York, USA — Springer International Publishing Switzerland 2015"*.
- **Role:** the **secondary / supplementary textbook** — deeper, algorithm-heavy. Already used in the vault: `W03_Audit_Source_Verification.md` locks the heat-kernel and similarity-graph claims to **Aggarwal, Ch. 2 §2.2**.

---

## 2. The doctor's own materials (lecture handouts — not textbooks)

| Week | File | Content |
|:--|:--|:--|
| W01 | `Week 01 - Introduction to Data Mining.pptx` | Course introduction (slides) |
| W02 | `Week 02 - Basic Data Types in Data Mining (v2).docx` | Data objects, attributes, attribute types |
| W02 | `Week 02 - Basic Data Types in Data Mining and ML.docx` | Same topic — extended ML version |
| W02 | `Week 02 - Data Types - Arabic Line-by-Line Translation.docx` | Arabic line-by-line translation of the W02 file |
| W03 | `Week 03 - Feature Extraction and Portability.docx` | Feature extraction (e.g. X-ray → texture features) |

- These are the **professor's handouts** — the closest thing to "the lecture". **None of them names a textbook source** (checked the W03 docx: no reference to Aggarwal / Han / any book).
- **Numbering caveat:** the doctor's delivered numbering ≠ the syllabus numbering. The delivered W03 ("Feature Extraction") is mapped by the syllabus to **Week 06** (Data Reduction & Feature Engineering). Treat week numbers as provisional until the doctor confirms.

---

## 3. Not a source (a revision aid)

- `Gemini - Smart Memorisation Framework (Data Mining).pdf` (11 pp) — an **AI-generated memorisation aid** (from a Gemini chat link, Arabic + English). Useful for revision, but it is **not** a textbook and carries no primary content.

---

## 4. Feature Selection — where it actually lives (the next seminar topic)

The doctor announced: *"next week's lecture will be about Feature Selection Techniques — you will do a seminar on it."*

| Source | Exact location | Depth |
|:--|:--|:--|
| **Han & Kamber** | **§3.4.4 "Attribute Subset Selection"** (inside §3.4 *Data Reduction*, Ch. 3) — book pp. ≈ **100–105** (PDF pp. **140–142**). Index refs: *attribute subset selection, 100, 103–105*. | The exam-level core: **forward selection · backward elimination · decision-tree induction · stepwise**, plus the heuristic-search framing. |
| **Aggarwal** | **§2.4 "Data Reduction and Transformation"** (Ch. 2 *Data Preparation*) — PDF pp. **63–83**; plus dedicated sections **§6.2 "Feature Selection for Clustering"** (PDF p. 179+) and **§10.2 "Feature Selection for Classification"** (PDF p. 309+). | The deeper/algorithmic treatment: filter vs wrapper vs embedded views, relevance/entropy measures, and how selection differs by task. |
| **Syllabus** | **Week 06 — Data Reduction & Feature Engineering** — *"Feature Selection / Attribute Subset Selection (Forward selection, Backward elimination, Decision tree induction)"*. Primary Materials listed: Han & Kamber §3.4 + the doctor's W03 docx. | Ties the topic to the weekly plan. |

> **Note:** the doctor's **W03 handout covers Feature *Extraction***, not selection — and it explicitly distinguishes the two ("Feature selection chooses a subset of existing attributes; feature extraction constructs new attributes"). That distinction is already in the vault's W02 note §7 and is a flagged exam point.

---

## 5. Verdict

1. **The "two sources" are:** **Han & Kamber (3rd ed., 2011)** — the textbook — and **Aggarwal, *Data Mining: The Textbook* (Springer, 2015)** — the one whose name was unknown.
2. **For the Feature Selection seminar, the anchor source is Han & Kamber §3.4.4**; **Aggarwal §2.4 (and §6.2 / §10.2)** supplies the deeper algorithmic layer.
3. **The doctor's handouts** (W01–W03) are the lecture materials and contain **no named textbook source**; the syllabus is the bridge that maps each week to a Han & Kamber section.
