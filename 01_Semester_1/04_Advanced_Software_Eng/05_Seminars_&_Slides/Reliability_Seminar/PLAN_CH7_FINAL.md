# PLAN — Integrating the four examiner notes into Chapter 7

**Subject:** Advanced Software Engineering · Chapter 7 (Software Reliability)
**Deliverable:** `Ch7_Software_Reliability_v3.docx` / `.pdf` (87 pp, 24 figures, 19 tables)
**Source of truth for text:** `ch7_part1.md` → `build_doc.py` → `finalize_docx.py` → `office_to_pdf.py`

---

## 0. Prerequisites (done)

- [x] Four notes verified against the chapter and all five local sources.
- [x] Nine DOIs resolved and matched via Crossref; one bad DOI rejected.
- [x] Two Musa full texts downloaded and stored in `sources/`.
- [x] Verified register written: `sources/CH7_REFERENCES.md`.

---

## 1. Note 1 — Goel–Okumoto model, named

**Where:** new subsection at the end of §7.3.1 (after the basic-model material, before §7.3.2), because the model belongs to the same NHPP family.

**What is added (≈ 180 words + 2 equations):**
- name, family (NHPP), mean value function `m(t) = a(1 − e^(−bt))`, intensity `λ(t) = ab e^(−bt)`;
- one sentence on parameter meaning (`a` = expected eventual failures, `b` = detection rate);
- a marker `[Foundational Knowledge / Standard Concept]` **only if** the student wants the chapter to stay strictly source-only; otherwise cite Goel–Okumoto 1979 in the references register.

**Evidence:** Goel & Okumoto 1979 (DOI verified); NRC 2015 ch. 9 names it.

**Risk:** external to the five local sources — flagged, not hidden.

---

## 2. Note 2 — the two curves on one page

**Where:** §7.1, immediately after the bath-tub paragraph.

**What is added:** replace the two separate image blocks with one paired block:

```
![fig7_1_bathtub.png|3.05]   ![fig7_2_sw_reliability.png|3.05]
```
plus a single caption: "Figure 7.1. Hardware bathtub curve (left) and software failure-rate curve (right)."

**Then:** renumber the remaining figures (script already exists) and update references.

**Risk:** none to content; the two images are our own.

---

## 3. Note 3 — two-model comparison table

**Where:** §7.3.2, at the end of the logarithmic-model subsection.

**What is added:** Table "Basic execution-time model versus logarithmic Poisson model" with the four columns:
assumption · shape of λ(μ) · finite cumulative-mean asymptote? · when to use.

**Content is already verified** against the Springer chapter (held locally):
- basic: λ(μ)=λ₀(1−μ/V₀), μ(τ)→V₀;
- logarithmic: λ(μ)=λ₀e^(−θμ), μ(τ)→∞;
- the finite/infinite distinction is a published classification attribute in that chapter.

**Renumbering:** the new table takes the next free number; all later table references shift by one (script exists).

---

## 4. Note 4 — operational profile, explicit

**Where:** §7.3.9 (statistical testing), one paragraph after the profile definition.

**What is added (≈ 90 words):** the explicit statement that the same program version, under two different operational profiles, can have two different reliabilities, because the profiles weight operations differently; reliability must be reported with the profile it refers to.

**Evidence:** NRC 2015 (verbatim), Musa 1993, Özekici & Soyer 2003.

---

## 5. Rebuild pipeline (no manual editing of the docx)

1. Edit `ch7_part1.md` only.
2. `python build_doc.py "_new.docx"`
3. replace `Ch7_Software_Reliability_v3.docx` (or a new version name if locked)
4. `python finalize_docx.py <file>` → TOC
5. reset metadata to `-`
6. `python office_to_pdf.py <file>` → PDF
7. `python academic_qa.py` → 0 failures
8. `python eq_check.py` → 0 failures
9. visual pass on the pages that changed

---

## 6. Acceptance gates

| Gate | Criterion |
|:--|:--|
| Structure | headings numbered, no skipped level |
| Figures | 23 after the merge (7.1 paired), all captions on the same page |
| Tables | 20 after the new table, sequential |
| Equations | 22 after the Goel–Okumoto pair, sequential |
| References | every figure/table reference resolves |
| Typography | left-aligned, 11.5 pt, 1.35 spacing |
| Length | ≥ 87 pages (expected 88–90) |
| QA | `academic_qa` 0, `eq_check` 0 |

---

## 7. Open decisions for the student

1. Note 1: cite the 1979 DOI in the register, or mark the paragraph `[Foundational Knowledge]`?
2. Figures 7.1/7.2: side-by-side (two columns) or stacked with a shared axis?
3. Keep the chapter at 87–90 pages, or push to 90+ by adding the reference list as an appendix?

---

## 8. Files this plan will touch

| File | Change |
|:--|:--|
| `ch7_part1.md` | four insertions + figure/table renumbering |
| `build_doc.py` | no change expected |
| `Ch7_Software_Reliability_v3.docx/.pdf` | rebuilt |
| `sources/CH7_REFERENCES.md` | already written; may receive the final citation block |
