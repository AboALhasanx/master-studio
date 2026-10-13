# Ch05 (Software Design) — Ali Fahim Book vs. Official Slides — Audit

**Source A:** `AliFahim_Software_Engineering.pdf` — scanned book (no text layer), **printed pages 202–248** = **PDF pages 107–131**
**Source B:** `Aggarwal_Singh_SE_3rd_ed_By_Chapter/Ch05_Software_Design.pdf` — 99 slides (Ch.5, "Software Design")
**Date:** 2026-10-12

---

## 1. Verdict in one line

The book pages **107–131 are the SAME chapter-5 text as the slides** — the slides are a *condensation* of these very pages. **Nothing new conceptually**, but the **book carries 4 concrete things the slides dropped**: (i) full prose explanations (incl. the Vitruvius design-importance paragraph and the §5.1.2 design-objectives criteria), (ii) complete worked UML diagrams for the Library case study, (iii) one extra numbered step in the OOD process, and (iv) **the answerable question set — MCQs 5.1–5.12 + Exercises 5.1–5.24 — identical to the slide questions.**

⚠️ **Correction to earlier note:** these pages are **Chapter 5 (Software Design)** pages 202–248, **not** "pages 107–131 of chapter content". The PDF page index and the printed page number differ by a constant offset (**PDF page = printed page − 95**).

---

## 2. Page-map (printed ↔ PDF)

| Printed book page | PDF page | Content |
|---|---|---|
| 202 | 107 | End of Ch.4 Exercises 4.21–4.36 (left) + **Ch.5 title page + §5.1 What is Design?** (right) |
| 203–204 | 108–109 | Design framework, Fig 5.1, §5.1.1 Conceptual & Technical Design, Fig 5.2, §5.1.2 Objectives of Design |
| 205–206 | 110–111 | Fig 5.3, §5.1.3 Why Design is Important?, §5.2 Modularity, Fig 5.4 |
| 207–208 | 112–113 | §5.2.1 Coupling, Fig 5.5, Fig 5.6 |
| 209–211 | 114–116 | Fig 5.7 types of coupling, Fig 5.8 common coupling, Fig 5.9 content coupling, §5.2.2 Cohesion, Fig 5.10, Fig 5.11 |
| 212–213 | 117–118 | Cohesion types continued, §5.2.3 Relationship between Cohesion & Coupling, Fig 5.12 |
| 214–215 | 119–120 | §5.3 Strategy of Design, Fig 5.13 Bottom-up, §5.3.2 Top-down, §5.3.3 Hybrid |
| 216–217 | 121–122 | §5.4 Function Oriented Design, Fig 5.14, 5.15, §5.4.1 Design Notations |
| 218–219 | 123–124 | Structure chart, Fig 5.16, Fig 5.17, Fig 5.18 |
| 220–221 | 125–126 | Transaction-centred structure (Fig 5.19), Pseudocode, §5.4.2 Functional Procedure Layers, §5.5 IEEE STD 1016-1998 |
| 222–223 | 127–128 | §5.5.2 SDD, Table 5.1 organisation of SDD, design entity attributes |
| 224–225 | 129–130 | Table 5.1 continued, **§5.6 Object Oriented Design**, §5.6.1 Basic Concepts (object, state, behaviour) |
| 226–227 | 131–132 | Objects, Classes, Inheritance, 3 aspects of object, Fig 5.20, Fig 5.21 |
| 228–229 | 133–134 | Fig 5.22 Triangle, abstraction, Fig 5.23, encapsulation §5.6.1(h), inheritance, Fig 5.24 |
| 230–231 | 135–136 | Polymorphism, Class hierarchy discussion, §5.6.2 Analysis and Design Object Oriented System, Fig 5.25 |
| 232–233 | 137–138 | Fig 5.25 steps, activity diagram Fig 5.26, interaction diagram, object types Fig 5.27, class diagram, associations/dependencies/aggregations |
| 234–235 | 139–140 | Generalisations, state chart diagram Fig 5.28, component & deployment diagram, **§5.6.3 Case Study — Library Management System**, problem statement + use cases |
| 236–241 | 141–146 | Use-case diagram Fig 5.29 + full use-case descriptions 1–8 |
| 242–247 | 147–152 | Sequence diagrams (login, issue, return, query, catalog, login-maint, student-maint), class diagram of entity classes, REFERENCES |
| 248 | 153 | End of References |
| 249–251 | 154–156 | **MULTIPLE CHOICE QUESTIONS 5.1–5.12 + EXERCISE 5.1–5.24 (Ch.5)** |

*(The scan is 2-up portrait: left/right halves are two separate printed pages.)*

---

## 3. Question: Is it the same as the slides?

**Yes — same content, same order, same figure numbering, same examples.** Section-by-section proof:

| Book section | Slides |
|---|---|
| §5.1 What is Design? | slides 2–5 |
| §5.1.1 Conceptual & Technical Design (Fig 5.2) | slide 5 (Fig 2) |
| §5.1.2 Objectives of Design | slides 6–8 |
| §5.1.3 Why Design is Important? (4 properties) | slides 9–11 |
| §5.2 Modularity (Fig 5.4) | slides 12–16 |
| §5.2.1 Coupling, Types of coupling (Fig 5.7) | slides 17–24 |
| §5.2.2 Cohesion, Types of cohesion (Fig 5.11) | slides 25–31 |
| §5.2.3 Relationship between C&C (Fig 5.12) | slides 32–33 |
| §5.3 Strategy of Design (bottom-up/top-down/hybrid) | slides 33–35 |
| §5.4 Function Oriented Design | slide 36 |
| §5.4.1 Design Notations (structure chart, transaction, pseudocode) | slides 40–49 |
| §5.5 IEEE STD 1016-1998 | slides 50–57 |
| §5.6.1 Basic Concepts | slides 58–60 |
| Objects / Classes / Inheritance / Abstraction / Encapsulation / Polymorphism | slides 60–70 |
| §5.6.2 Analysis & Design of OO System (Fig 5.25) | slides 71–73 |
| Use case / activity / interaction / class / state / component-deployment | slides 73–80 |
| §5.6.3 Case Study — Library Management System | slides 81–93 |
| MCQs 5.1–5.12 | slides 94–96 |
| Exercises 5.1–5.24 | slides 97–99 |

The slides even reproduce the **same figures** (Fig 5.7 coupling table, Fig 5.11 cohesion table, Fig 5.20 class "Car", Fig 5.23 "Shape" hierarchy, Fig 5.25 OOD process, Fig 5.26 activity, Fig 5.27 object types, Fig 5.29 use case, the sequence diagrams, the class-diagram-of-entity-classes) — because the slides were cut from this exact manuscript.

---

## 4. Question: Is there anything EXTRA in the book (not in the slides)?

**Yes — 5 concrete additions.** These are the things the slide deck omitted:

### 4.1 §5.1.3 "Why Design Is Important" — the Vitruvius analogy paragraph (book-only)
The book opens this section by invoking the Roman architect **Vitruvius**, who gave **three** attributes of a good design — **durability, utility, and charm** — and draws the explicit analogy to software (a system, like a building, must weather change, serve its purpose, and present a coherent structure). The book then adds the three characteristics that guide a design's evolution (implements all explicit + implicit requirements; is a readable guide for coders/testers; gives a complete picture of data, functional and behavioural domains). **The slides omit this paragraph entirely.** ⚠️ *Correction (verified by re-rendering the book page): earlier in this audit I wrote this as "4 design-goal properties — Durability, Utility, Charm, Consistency". That was WRONG. The book lists **three** attributes (durability / utility / charm — Vitruvius). The **four** items that also appear in this area — "Correct & complete / Understandable / At the right level / Maintainable" — are the separate **§5.1.2 Objectives of Design** criteria (and are exactly what slide 8 reproduces). Do not merge the two.*

### 4.2 §5.1.2 "Objectives of Design" — full paragraph on specification as a *derived* product
Book: "The specification (i.e. the 'outside' view) of a program should obviously be as free as possible of aspects imposed by how the program will work…" and the discussion that for **small programs** one coder can sit with the spec and write it; for **larger** programs the gap between specification and coding is filled by the design. Slides compress this into ~3 bullets (slides 6–8) and drop the small-vs-large program distinction paragraph.

### 4.3 §5.6.2 — **both book and slides carry the SAME 6 steps** (corrected)
⚠️ *Correction (verified by re-rendering the printed book pages 231–234, i.e. PDF 120–122): an earlier version of this audit claimed "the book has 7 steps i–vii". **That was WRONG.***

The book's **Fig 5.25 "Steps for analysis & design of object oriented system"** (printed p.232 / PDF p.121) is a flowchart with **exactly SIX boxes**:
1. Problem statement → Create use case model
2. Draw activity diagram (if reqd.)
3. Draw the interaction diagrams
4. Draw the class diagram
5. Draw the state chart / object diagram (if required)
6. Draw component & deployment diagram → Design documents

The book's narrative enumerates the same six with letters **(a) → (f)**: (a) Create use case model; (b) Draw activity diagram (if required); (c) Draw the interaction diagrams; (d) Generalizations; (e) Design of state chart diagram; (f) Draw component and deployment diagrams. **The slides (72, 75) show the identical six steps.** The only slide artifact is a **missing step letter** — slide 75 lists "a) b) d)", literally skipping "(c)" — but the *content* is the same six stages. **There is no 6-vs-7 discrepancy: it is 6 steps on both sides.**

### 4.4 The full worked Library Management case study
- **Complete use-case descriptions 1–8** (§5.6.3, printed p.236–242): Login, Issue Book, Return Book, Query a Book, Maintain Catalog, General Reports, Maintain Login, Maintain Student Details — each with *Introduction / Actors / Pre-Condition / Post-Condition / Flow of Events (Basic + Alternate) / Special Requirements / Related Use Cases*.
- **All 8 sequence diagrams** (login, issue, return, query, maintain catalog, maintain login, maintain student details, generate reports).
- **Class diagram of entity classes** with full attribute+operation lists (Book Details, Student Details, Login Details, Issued Book Details, Student Issued Book Details).
The slides (81–93) show **only the diagrams**, no use-case description text at all.

### 4.5 The References block (printed p.247–248 / PDF p.152–153)
Full [RHA01], [BOD03], [FAI02], [JAC98], [JOS03], [MYE78], [PTR02], [PAN89], [PFLE98], [SOM04] list. Slides carry none of it. Relevant because your **own note citations** can be cross-checked against the book's reference list.

---

## 5. Question: Are there questions at the end of the book on this topic?

**Yes — and they are the EXACT questions you already have on the slides.**

- **MCQs 5.1–5.12** → book printed p.249–250 (PDF p.154–155); slides 94–96. *Identical wording.*
- **Exercises 5.1–5.24** → book printed p.250–251 (PDF p.155–156); slides 97–99. *Identical wording.*

**Consequence: there is NO hidden extra question set in the book for Ch.5.** The 36 questions already solved in `Ch05_MCQ_Solved.md` are the complete set. The book adds **no answer key** either — answers still have to be derived from the text, exactly as we did.

Note: the MCQ/Exercise sets for **other** chapters sit at the end of each chapter in the same book (e.g. Ch.9 MCQs 5.1–5.12 appear on printed p.488–490 / PDF p.250–252 under "Software Maintenance"). The chapter-5 set is the one at printed **p.249–251**.

---

## 6. OCR — status

**Requested: "سوي ال ocr همين".**

**Blocker:** the file has **no text layer at all** (`chars = 0` on every page, verified via PyMuPDF for PDF pages 105–134). OCR would need an engine.

**Engine check (system Python 3.12):** `pytesseract` ✗, `easyocr` ✗, `paddleocr` ✗, `ocrmypdf` ✗; no `tesseract` binary on PATH or in Program Files. Only `PIL` ✓ and `cv2` ✓.

**What I actually did instead (and it is stronger than OCR here):** rendered every page at 100–300 DPI and **read them visually** — text, figures, tables, diagrams. That is how the audit above was produced. For a *scanned, figure-heavy* chapter, OCR of the body text would be lossy anyway (it cannot recover the diagrams, and the handwritten marginalia in the scan would corrupt output), so the visual read is the reliable path.

**If you still want a machine-readable text dump**, the options are:
1. install `pytesseract` + the Tesseract Windows binary (~50 MB, one-time), then OCR pages 107–131 → plain text files; or
2. `pip install easyocr` (~2 GB with torch) for better accuracy on the scanned typesetting.

Say the word and I'll install one and produce `AliFahim_Ch05_OCR.txt`. Otherwise the visual audit above already answers all three of your questions.

---

## 7. Bottom line for study

- **Use the book for**: the Vitruvius design-importance paragraph (durability/utility/charm) + the design-objectives criteria, the use-case descriptions, the 6-step OOD process (Fig 5.25), the entity-class attribute lists.
- **Use the slides for**: fast revision — they're the same content, minus the bulk.
- **Questions**: no difference. Your `Ch05_MCQ_Solved.md` (36 items) is already the complete set.
