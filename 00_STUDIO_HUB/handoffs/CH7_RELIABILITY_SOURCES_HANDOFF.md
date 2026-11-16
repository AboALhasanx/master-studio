# Handoff — Sourcing the four examiner notes for Chapter 7 (Software Reliability)

> **Who reads this:** any capable research harness — Gemini (Antigravity), ChatGPT, a second OpenCode/Codex session, or a scout persona — that is asked to find **authoritative, citable sources** for four examiner remarks on the Reliability chapter.
> **Who hands it over:** the student, or any vault harness that received the request in chat.
> **Rule of the house:** `AGENTS.md` §2.1 (Anti-Hallucination & Citation Verification) is binding. **Every DOI in the output must be resolvable and re-verified by you, the reader.** If this handoff and the root directives disagree, the root directives win.

---

## 0. The prompt the student sends (fill the brackets)

```
اقرأ الملف التالي كاملاً ونفّذ المهمة بالكامل:
00_STUDIO_HUB/handoffs/CH7_RELIABILITY_SOURCES_HANDOFF.md

أريد مصادر موثوقة (مع DOI حقيقية قابلة للفتح) تدعم ملاحظات الدكتور الأربع.
اكتب النتيجة في: 00_STUDIO_HUB/handoffs/CH7_RELIABILITY_SOURCES_REPORT.md
ولا تعدّل أي ملف من ملفات الفصل بدون أمر صريح مني.
```

---

## 1. Read first

| # | file | why |
|---|---|---|
| 1 | `00_STUDIO_HUB/AGENTS.md` §2.1 | zero citation invention; DOI mandatory; authority hierarchy |
| 2 | `01_Semester_1/04_Advanced_Software_Eng/05_Seminars_&_Slides/Reliability_Seminar/ch7_part1.md` | the chapter source of truth (Markdown, 19 tables, 24 figures) |
| 3 | `.../Reliability_Seminar/sources/book_ch7_ocr.txt` | OCR of the scanned book, Ch.7 (book pp. 308–366) |
| 4 | `.../Reliability_Seminar/_reliab_sources.txt` and `_quality_sources.txt` | extracted text from CS Agarwal 2010, Pressman, Mall, Sommerville, Leach |
| 5 | `.../Reliability_Seminar/SOURCE_ch7_slides.txt` | Aggarwal & Singh lecture slides for Ch.7 (126 slides) |

Deliverable PDF/DOCX for context only (do **not** edit):
`Ch7_Software_Reliability_v3.docx` / `.pdf` (87 pages).

---

## 2. The four examiner notes — what is missing and where

The examiner sent four remarks. Status was verified **today** against all five sources.

### Note 1 — "Name the Goel–Okumoto model explicitly"

| source | occurrences |
|---|---|
| our chapter (`ch7_part1.md`) | **0** |
| book OCR | **0** (`Okumoto` appears only inside a bibliography entry: Musa, Iannino & Okumoto, 1987) |
| Ch.7 slides | **0** |
| CS Agarwal / Pressman / Mall / Sommerville | **0** (`Okumoto` only in references) |

**Gap:** the model is nowhere named in our sources. The chapter says "non-homogeneous Poisson process (NHPP)" once and never names the canonical NHPP model.

**Research job:**
1. Identify the **original paper** (title, venue, volume, issue, pages, year) — a preliminary search suggests *IEEE Transactions on Reliability*, vol. R-28, no. 3, 1979, "Time-Dependent Error-Detection Rate Model for Software Reliability and Other Performance Measures" — **you must confirm the exact title, venue and pages yourself; do not trust this line.**
2. Find its **resolvable DOI** (format `https://doi.org/10.xxxx/xxxxx`) by opening the DOI page and confirming it resolves to that paper.
3. Find 1–2 **secondary sources** (textbook or review chapter, IEEE/ACM where possible) that (a) name the model "Goel–Okumoto" and (b) give its equations: m(t) = a(1 − e^(−bt)) and λ(t) = ab·e^(−bt).
4. Optional but valuable: a source that states the family plainly — *the Goel–Okumoto model is the canonical NHPP model* — because the examiner says the lecture talks about NHPP without naming its most famous member.

### Note 2 — "Bathtub curve and software curve on the same page"

| item | current state |
|---|---|
| Fig. 7.1 Bath tub curve | **page 5** of `v3.pdf` |
| Fig. 7.2 Software reliability curve | **page 6** |
| burn-in / useful life / wear-out concepts | present in §7.1 text |

**Gap:** concepts exist, but the two curves are on consecutive pages, not the same page.

**Research job (light):** find a source that explicitly places the hardware bathtub curve against the software failure-rate curve in one figure or one comparison (a textbook chapter or an IEEE/ACM survey is ideal). This is mainly a **layout request**, so the deliverable here is a *reference and a one-sentence justification*, not new content.

### Note 3 — "One-page table: basic vs logarithmic models, four columns"

What we have today: **Table 7.13 "Comparison of the reliability models"** — 5 models × columns `Model | Basic assumption | Behaviour | Main use`.

What the examiner wants: **only two models** (Basic execution time vs Logarithmic Poisson), four columns:
1. assumption,
2. shape of λ(μ),
3. is there an asymptote (finite V₀ or not),
4. when do you use each.

**Research job:**
1. Confirm the four-column content against **Musa's original sources** (basic execution time model; logarithmic Poisson execution time model, Musa & Okumoto, ICSE 1984) — verify equation forms, asymptote behaviour, and the "when to use" guidance.
2. Return the table content in Markdown, ready to paste, with a DOI for each supporting source.

### Note 4 — "Reliability depends on the operational profile"

Current coverage in our chapter:
- §7.1.10: *"perceived reliability depends on the execution profile of the user, not only on the number of latent defects"* + the library example (librarian vs members).
- §7.3.9: statistical testing + operational profile.
- Missing: the **explicit** statement — *the same program under two different operational profiles yields two different reliabilities*.

**Research job:** find the canonical statement, ideally **Musa, "Operational Profiles in Software-Reliability Engineering," IEEE Software, 1993** (a search already surfaced DOI bookmark `10.1109/52.199724` on IEEE Computer Society — **you must open the DOI and confirm**). Also find a source stating that reliability = f(program, profile) explicitly.

---

## 3. Authority hierarchy (AGENTS.md §2.1.4)

Search and prefer in this order:
1. IEEE Transactions / ACM Digital Library (IEEE Xplore, dl.acm.org)
2. Top-tier conferences (ICSE, FSE, ASE, ISSRE, ReliabilityWeek)
3. Canonical standards (ISO/IEC/IEEE, SWEBOK, NIST)
4. Verified seminal textbooks (Pressman, Sommerville, Musa/Iannino/Okumoto 1987, Shooman)

If a claim rests only on general textbook knowledge, tag it `[Foundational Knowledge / Standard Concept]` — **never invent a DOI.**

---

## 4. Output format — `CH7_RELIABILITY_SOURCES_REPORT.md`

One section per note, each containing:

```markdown
### Note N — <short title>
**Status in our chapter:** missing / partial / present (with file + section + page)
**Candidate source(s):**
- Author, "Title", Venue, vol(issue), pages, Year. DOI: https://doi.org/10.xxxx/xxxxx   ← RESOLVED BY ME (I opened the link)
**Evidence (verbatim quote, ≤ 40 words):** "..."
**What we would add to the chapter:** 2–5 sentences or a table, in formal academic English
**Risk:** citation verified / partially verified / not verified — do not ship unverified
```

Hard requirements:
- At least **two independent sources per note** where they exist (one primary, one secondary).
- Every DOI opened and confirmed to land on the right paper.
- Nothing written in Arabic in the report body except the examiner's wording.
- **No edits to any chapter file.** The report file is the only file you may write.

---

## 5. Constraints (do not violate)

1. **Do not modify** `ch7_part1.md`, `build_doc.py`, `Ch7_*.docx`, `Ch7_*.pdf`, `figures/` — the student must order any change explicitly.
2. No citation invention (AGENTS.md §2.1.1) — a DOI you have not opened does not exist in your report.
3. No SaaS links as evidence (LinkedIn posts, Medium, random blogs) — a commercial calculator page may *support* a number but never *carry* a claim.
4. Keep the chapter's existing conventions if your proposed text is accepted later: no inline citation noise was used in the chapter body, so your "what we would add" should be **citation-ready text**, and the DOI list goes in a separate block for the harness to insert.

---

## 6. Verification gate (run before you declare done)

- [ ] 4 notes each have ≥1 verified DOI (opened, right paper).
- [ ] Every quote is verbatim from the source you opened.
- [ ] No claim in the report appears in `ch7_part1.md` unless flagged as "already present".
- [ ] Report saved at `00_STUDIO_HUB/handoffs/CH7_RELIABILITY_SOURCES_REPORT.md`.
- [ ] No chapter file modified (git diff clean for the Reliability_Seminar folder).

---

## 7. Hand-back

When the report exists, the vault harness (or the student) returns here and either:
- orders the four insertions into `ch7_part1.md` and rebuilds via `build_doc.py` → `finalize_docx.py` → `academic_qa.py`, or
- rejects any note as out of scope (Note 1 may be rejected if the student insists on source-only content, because the model name is absent from all five local sources).
