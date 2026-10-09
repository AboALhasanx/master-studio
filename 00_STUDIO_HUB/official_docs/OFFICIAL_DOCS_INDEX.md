---
title: "Official Documents Index — Department / College / Ministry"
course: "00_STUDIO_HUB"
subtitle: "Complete catalogue of every official postgraduate document pulled from University of Wasit + MoHESR sources"
last_updated: 2026-10-06
status: LIVING (append as new official docs are found)
---

# Official Documents Index — فهرس الوثائق الرسمية

> **Purpose.** This file is the single index of **every official document** harvested for the
> Master Studio vault from three authority tiers:
> **① Ministry (MoHESR)** → **② College (CS&IT, University of Wasit)** → **③ Department (Software / قسم البرامجيات)**.
> Each row carries its source URL, page count, whether it has a text layer, and what it actually is.
> The companion narrative analysis lives in `00_STUDIO_HUB/CURRICULUM_MAP.md` — **this file is the file-level catalogue; that file is the analysis.**

---

## 0. Headline

| Question | Short answer |
|:---|:---|
| Who writes the curriculum? | **MoHESR** (via دائرة البحث والتطوير, letter **ت 312906 dated 15/3/2023**) sets the *framework*; the college/department writes the *course-by-course forms*. Bologna Process alignment. |
| Who issues the admission rules? | **MoHESR / Research & Development Directorate** — one letter per academic year (e.g. `ضوابط التقديم والقبول 2025-2026` and `2026-2027`). |
| Who issues day-to-day PG regulations? | The college republishes MoHESR instructions on its PG page (`cit.uowasit.edu.iq/ar/تعليمات-الدراسات-العليا/`) — 21 PDFs catalogued below. |
| What is the department's own programme called? | Officially **"Master of Programming Science"** under the **Software Department** (per the Academic Description forms). |
| Competitive-exam weighting (canonical) | **30 % written exam + 70 % bachelor grade**, minimum total **65 %** (per Instructions No. 26 of 1990, Art. 5). |

---

## 1. Folder layout

```
00_STUDIO_HUB/
├── official_curriculum/         ← the *study plan* + competitive exam + admission (named, cleaned)
│   ├── 01_Competitive_Exam_Materials_2025-2026.pdf
│   ├── 02_Admission_Rules_2025-2026.pdf
│   ├── 03_Academic_Description_FirstCourse_2024-2025.pdf      (+ _AR.txt)
│   ├── 03b_Academic_Description_FirstCourse_2024-2025_EN.pdf  (+ _EN.txt)
│   └── 04_Academic_Description_SecondCourse_2024-2025.pdf
│
├── official_docs/               ← the raw harvest (provenance preserved)
│   ├── 01_postgrad_regulations/ ← 21 college/MoHESR PG regulation PDFs (+ txt/ for the text-bearing ones)
│   ├── 03_department_296/       ← files served from the Software-department page (uowasit.edu.iq/colleges/department/296)
│   ├── 04_academic_description/ ← files served from the Academic-Description page (uowasit.edu.iq/colleges/apd/273)
│   └── OFFICIAL_DOCS_INDEX.md   ← this file
```

> **Note on duplication:** `official_curriculum/` holds *renamed* copies of some documents that also exist under
> `official_docs/` under their original server filenames (storage IDs). Section 5 flags every duplicate.

---

## 2. Tier ① — Ministry (MoHESR / وزارة التعليم العالي والبحث العلمي)

| File | What it is | Pages | Text? | Source |
|:---|:---|:---:|:---:|:---|
| `01_postgrad_regulations/تعليمات-1990-1.pdf` | **Instructions No. 26 of 1990** — the *founding* PG framework law (how PG programmes are created, applicant conditions, supervision ranks). Canonical. | 5 | ✅ 209 lines | cit PG page |
| `01_postgrad_regulations/ضوابط-التقديم-والقبول-2026_2027-1.pdf` | **Admission & Registration Rules 2026-2027** — newest year; MoHESR R&D letter, 5 condition pages + 6 forms + Health-Ministry letter. | 37 | ✅ 4372 lines | cit PG page |
| `01_postgrad_regulations/ضوابط-التقديم-والقبول-للدراسات-العليا-٢٠٢٥-٢٠٢٦-1.pdf` | **Admission & Registration Rules 2025-2026** — *the year Abu Al-Hasan was admitted*. | 32 | ⚠️ scanned (1 text page) | cit PG page |
| `01_postgrad_regulations/اعمام-ضوابط-عودة-1.pdf` | **Return of suspended PG students to study seats** — MoHESR R&D circular (ت 5118/8, 2024/3/4), signed by أ.د. لبنى خميس هذي. Covers second-attempt failures returning to seats. | 9 | ✅ 698 lines | cit PG page |
| `01_postgrad_regulations/الدراسة-اثناء-التوظيف-قانون-20-لسنة-2020-1.pdf` | **Law 20 of 2020** — studying while employed. | 11 | ✅ 460 lines | cit PG page |
| `01_postgrad_regulations/قانون-اسس-تعادل-الشهادات-...-1.pdf` | **Law 20 of 2020 — equivalence of Arab/foreign scientific certificates** (Iraqi Gazette No. 4608, 21/12/2020). Defines MoHESR dept structure. | 11 | ✅ 460 lines | cit PG page |
| `03_department_296/eQCcTWQP4HKONwxx_1763881884.pdf` | **MoHESR R&D letter No. ب ت 1724/7, dated 5/5/2024** — grants colleges permission to **extend the PG admission window for 2024-2025**. Signed: أ.د. غسان حميد مجهول, DG of Research & Development. Explains why the admission timeline stretched. | 29 | ⚠️ scanned | dept page (296) |
| `03_department_296/B7fKxcyIpLZuh14h_1773497002.pdf` | **دليل منصة IQ Learn** — MoHESR smart-learning-platform user guide (1st ed., March 2026). Platform tool, not curriculum. | 53 | ✅ text | dept page + apd/273 |

**Remaining MoHESR regulation PDFs** (all from the cit PG page, all currently **scanned / no text layer** — need OCR before quoting):

| File | Subject | Pages |
|:---|:---|:---:|
| `التدريس-والإشراف-على-طلبة-الدراسات-العليا-داخل-وخارج-العراق-1-1.pdf` | Teaching & supervision of PG students, inside/outside Iraq | 4 |
| `ضوابط-الامتحان-الشامل-1.pdf` | **Comprehensive exam (الامتحان الشامل)** — ⭐ high value | 9 |
| `ضوابط-الانتقال-إلى-مرحلة-البحث-1.pdf` | Transition to the research stage | 3 |
| `ضوابط-الاعادة-إلى-مقاعد-الدراسة-2.pdf` | Reinstatement to study seats | 5 |
| `ضوابط-تأجيل-الدراسة-1.pdf` | Study deferral | 4 |
| `ضوابط-انهاء-العلاقة-بالدراسة-1.pdf` | Termination of study relationship | 10 |
| `ضوابط-التمديدات-1.pdf` | Extensions | 2 |
| `ضوابط-نقل-الدراسة-1.pdf` | Transfer of study | 1 |
| `ضوابط-استيفاء-الاجور-الدراسية-1.pdf` | Tuition-fee collection | 5 |
| `ضوابط-تخفيض-الاجور-الدراسية-1.pdf` | Tuition-fee reduction | 6 |
| `ضوابط-الاحتفاظ-بالمقعد-دون-مسمى-التأجيل-1.pdf` | Seat retention without the "deferral" label | 1 |
| `لجان-المناقشة-1.pdf` | Discussion committees | 3 |
| `لجنة-مناقشة-رسائل-الماجستير-واطاريح-الدكتوراه-1.pdf` | MSc-thesis / PhD-dissertation defence committee | 4 |
| `2023-04-06-No.2714-استمارة-لجنة-المناقشة-...-1-1.pdf` | Defence-committee form No. 2714 (2023-04-06) | 3 |
| `الدراسة-اثناء-التوظيف-قانون-٢٠-لسنة-٢٠٢٠-1.pdf` | Study-while-employed (Arabic-numeral duplicate) | 5 |

---

## 3. Tier ② — College (كلية علوم الحاسوب وتكنولوجيا المعلومات، جامعة واسط)

- **PG regulations page:** `https://cit.uowasit.edu.iq/ar/تعليمات-الدراسات-العليا/` → the 21 PDFs above.
- **PG hub:** `https://cit.uowasit.edu.iq/ar/الدراسات-العليا/` (hub page; PDFs are behind JS / announcement pages).
- **Announcement pages (live, change yearly):** `.../نتائج-القبول-النهائي-في-الدراسات-العليا/`, `.../إعلان-أسماء-المقبولين-في-الدراسات-العليا/`.
- **Academic-Description page (English URL):** `https://uowasit.edu.iq/colleges/apd/273` → the study-plan forms + IQ-Learn guide (see §4).

> **Fetch note.** The Arabic `cit.uowasit.edu.iq` sub-pages return a 32–81 byte error to plain `urllib`
> (bot/CDN protection); the college *homepage* and the `uowasit.edu.iq/colleges/...` pages fetch fine.
> If the Arabic hub content is ever needed, use a rendered browser (Playwright) rather than raw HTTP.

---

## 4. Tier ③ — Department (قسم البرامجيات / Software) — the study plan

| File | What it is | Pages | Text? | Source |
|:---|:---|:---:|:---:|:---|
| `official_curriculum/03_Academic_Description_FirstCourse_2024-2025.pdf` | **Academic Description forms — Postgraduate, First Course 2024-2025** (Arabic). The official course-by-course study plan. | 33 | ✅ | apd/273 |
| `official_curriculum/03b_..._EN.pdf` | English rendering of the First-Course description. | 35 | ✅ | apd/273 |
| `official_curriculum/04_Academic_Description_SecondCourse_2024-2025.pdf` | **Academic Description forms — Second Course 2024-2025** (Arabic, scanned). | 35 | ⚠️ scanned | apd/273 |
| `official_curriculum/01_Competitive_Exam_Materials_2025-2026.pdf` | **Competitive-exam syllabus 2025-2026** — AI (Luger 6e), Networks, OOP. | — | ✅ | dept/apd |
| `official_curriculum/02_Admission_Rules_2025-2026.pdf` | Admission rules 2025-2026 (scanned, large). | — | ⚠️ scanned | dept |
| `03_department_296/r6YG5EmCFqXpZyqF_1763881494.pdf` | **Competitive-exam materials (1-page condensed)** — confirms AI reference = **Luger, 6th ed.** (same content as `official_curriculum/01_…`). | 1 | ✅ | dept page (296) |
| `04_academic_description/7vryHdFKYy3KEdaa.pdf` | ⚠️ **byte-identical duplicate** of `03_Academic_Description_FirstCourse_2024-2025.pdf`. | 33 | ✅ | apd/273 |
| `04_academic_description/ifKq1e3YGS1tf2rJ.pdf` | ⚠️ **byte-identical duplicate** of `04_Academic_Description_SecondCourse_2024-2025.pdf`. | 35 | ⚠️ scanned | apd/273 |

---

## 5. Duplicates (candidate cleanup — ⚠️ NOT deleted yet)

These are **bit-identical** (same size, same text) — zero information gain in keeping both. I have **not deleted anything**; awaiting your decision.

| Keep (clean name) | Redundant copy (raw storage name) | Identical? |
|:---|:---|:---|
| `official_curriculum/03_Academic_Description_FirstCourse_2024-2025.pdf` | `official_docs/04_academic_description/7vryHdFKYy3KEdaa.pdf` | ✅ 18,601 KB both |
| `official_curriculum/04_Academic_Description_SecondCourse_2024-2025.pdf` | `official_docs/04_academic_description/ifKq1e3YGS1tf2rJ.pdf` | ✅ 11,852 KB both |
| `official_curriculum/01_Competitive_Exam_Materials_2025-2026.pdf` | `official_docs/03_department_296/r6YG…pdf` (1-page variant) | ~ same content, different rendering |

Also inside `01_postgrad_regulations/`: `الدراسة-اثناء-التوظيف-قانون-٢٠-لسنة-٢٠٢٠-1.pdf` (Arabic-numeral) appears to duplicate `الدراسة-اثناء-التوظيف-قانون-20-لسنة-2020-1.pdf` — one is scanned, one has text.

---

## 6. Key facts extracted (verified against the sources above)

1. **Framework origin.** MoHESR letter **ت 312906 (15/3/2023)** + Bologna Process → curriculum rewritten; reviewed annually via the External-Examiner Programme. Programme officially named **"Master of Programming Science"** (Software Dept). *(See `CURRICULUM_MAP.md` §8.)*
2. **Competitive-exam weighting (canonical).** Instructions No. 26 of 1990, Art. 5: admission = **70 % bachelor grade + 30 % written exam**, minimum total **65 %**. Language exam required. Full-time dedication required.
3. **Ministry structure (from Law 20/2020).** MoHESR → *دائرة البحث والتطوير* (R&D — writes PG instructions & admission rules) and *دائرة البعثات والعلاقات الثقافية* (certificate equivalence); *هيئة الرأي* approves; *قسم معادلة الشهادات* executes equivalence.
4. **Admission timeline.** MoHESR letter **ب ت 1724/7 (5/5/2024)** authorised extending the 2024-2025 PG admission window — explains the stretched timeline.
5. **Return-to-seats rule.** MoHESR circular **ت 5118/8 (2024/3/4)**: a student who failed the *second attempt* (الدور الثاني) may return to a study seat the following year only, by written request within 10 working days of the second-attempt results, and is re-examined in failed + grade-"متوسط" courses.

---

## 7. Gaps / still missing

| Gap | Why it matters | Next step |
|:---|:---|:---|
| **Comprehensive-exam regulations (ضوابط-الامتحان-الشامل)** is scanned (no text) | Directly defines the MSc comprehensive exam | OCR pass, or read visually page-by-page |
| 2025-2026 admission rules (his year) mostly scanned | His actual admission conditions | OCR / visual read |
| Arabic `cit` hub + announcement pages unfetchable via raw HTTP | May hold year-specific notices | Playwright render if needed |
| Actual **admitted-students list** for 2025-2026 | Confirms cohort composition | Optional; fetch announcement page via browser |

---

## 8. Provenance

- Harvested 2026-10-06 with the managed Python venv (`pymupdf`) over `urllib` (proxy-safe).
- Every file kept under its **original server filename** (storage IDs) inside `official_docs/` for forensic traceability; the *named* copies live in `official_curriculum/`.
- Source hosts: `cit.uowasit.edu.iq`, `uowasit.edu.iq`, `rdd.edu.iq` (referenced), `student.alsuhuhadaa.gov.iq` (referenced).

---

*Companion analysis: `00_STUDIO_HUB/CURRICULUM_MAP.md`. Live state: `00_STUDIO_HUB/ACTIVE_STATE.md`.*
