# Student Notes Log — Master Studio

> **What this file is.** A running, append-only log of the student's own remarks about the work, and the decision each remark produced. Written so that *any* harness — WorkBuddy, Codex, OpenCode, OMP, MiMo, or a future agent — can read one file and know what was discussed and what was settled, without re-litigating it.
>
> **Rules.**
> 1. **Append only.** Never rewrite or delete an earlier entry. If a decision is reversed, add a new entry that supersedes it and say so explicitly.
> 2. **Quote the student verbatim** in his own Arabic, then state the decision in plain terms.
> 3. **Name the scope.** A remark may apply to one file, one chapter, one subject, or the whole vault. Say which.
> 4. **Record the consequence, not just the instruction** — especially when a rule invalidates an older rule.
> 5. If a remark contradicts a standing rule elsewhere (`AGENTS.md`, `.workbuddy-ai/memory/MEMORY.md`, a build plan), the entry must name the conflict and which side won.

---

## 2026-10-16 — ASE Chapter 1 packs (build in progress)


**Context.** Building one folder per chapter inside `03_Study_Notes/`, with one PDF per question type. The `T1_MCQ` pilot had been delivered and reviewed.

---

### N-001 · Language: English only

> «اللغة انكليزية تماما... الترجمة اني اتجرم عليها بالورقة والقلم لما اطبع الملف بالاخير»

**Decision.** Every chapter pack is written in **English only** — questions, answers, explanations. No Arabic, no bilingual sidebars, no Arabic rationale layer.
**Scope.** All ASE chapter packs built under this structure.
**Consequence.** The student translates by hand on the printed sheet. Because the files carry no Arabic, the vault's RTL/bidi authoring laws (arrow direction, digit-first cells, ordered-list scrambling) **stop applying to these files**. Latin-only text renders LTR cleanly.
**Conflicts with:** the shared study-day plan `ASE_Study_Day_2026-10-16.md` — which also asked for English-only, so no conflict there — but it **does** conflict with the established house style of `08_DeepStudy_Ch04/ByType/*` and `08_DeepStudy_Ch05/ByType/*`, which are Arabic. Those existing files are **not** to be rewritten.

---

### N-002 · No tables, ever

> «رغم اني ما احبذ الجداول جدا صراحة.... كجدول وبس اشوفها شكل بدائي... حاول تشوف طريقة احسن من الحدول التيبل»

**Decision.** **No Markdown tables** in student-facing chapter packs. The replacement is the exporter's **callout cards** (`> [!NOTE]`, `> [!TRAP]`, `> [!WARN]`, `> [!CONCEPT]`, `> [!CALC]`, `> [!FEYNMAN]`) plus one-line option rows separated by `·`.
**Scope.** All new chapter packs. Existing Ch04/Ch05 files keep their tables.
**Consequence.** Comparison content must be written as bold-lead-in paragraphs, not as `| … |` rows. This overrides the vault's older "table parsing law", which existed only to make tables render under Arabic.
**Verified.** The card format was rendered and inspected in `T1_MCQ.pdf` — the student's reaction: «واو برافووو».

---

### N-003 · Question and answer must never be separated by a page break

> «السؤال والاجابة ما اريد تنقطع ابدا... اريدها بشكل متلاصق دوما»
> «حاول تلاقي احسن حل ممكن... حتى لو يفحص العدد ويقفز وياه لغير صفحة ويبقا فراغ بالصفحة عادي جدا»

**Decision.** A question stem, its option row and its answer card must travel together as one block. If the block does not fit at the bottom of a page, the whole block moves to the next page and **leaves whitespace** — that is explicitly acceptable.
**Scope.** All packs.
**Implementation.** `pdf_exporter.py` gained a `.keep-next` rule (`break-after: avoid-page`). Each stem line and each option line carries `{: .keep-next }` (via the already-enabled `attr_list` extension).
**Verified empirically.** A controlled probe reproduced the split at two filler lengths without the rule, and the unit stayed whole with it. On the real `T1_MCQ.pdf`: **28 stem→answer pairs checked, 0 splits.**
**Superseded belief.** Before this, only the answer *card* was protected (`page-break-inside: avoid`), which is exactly why the stem could be stranded alone at a page foot.

---

### N-004 · Answers come from the book, not the slides

> «ما راح نعتمد كلام السلايد كجاوب صراحة.... راح نعتمد الكتاب.... مال اغرويل»

**Decision.** The **Aggarwal & Singh textbook is the authority for every answer**. Publisher slides are used to check lecture coverage only, never as the answer source.
**Scope.** All ASE chapter packs, retroactively including `T1_MCQ`.
**Consequence — significant.** `T1_MCQ` was built with slide anchors ("Source: slide 22"). It must be re-anchored to **printed book page numbers**.
**Also:** the student asked whether the other book copies carry answers —

> «مو بس المطبوع هميمن شوف الكتاب العادي اكيد تلاقي عليه اجوبه»

**Finding.** Checked every Aggarwal-related PDF in `02_Raw_Materials`: `DUPLICATES_Review/Aggarwal_Singh_SE_3rd_ed_Book.pdf`, `Aggarwal_Singh_Full_Notes_NCIT.pdf`, `_REAL_Aggarwal_Singh_Textbook.pdf`, `Aggarwal_Singh_SE_3rd_ed_By_Chapter/00_SOURCE_Full_1094pp_Slides.pdf`, `Ch01_Introduction.pdf`, and `Reference_Textbooks/CS_Agarwal_SW_Engineering_and_Testing_2010.pdf`. **None of them contains an answer key** — the first five are the same slide series, and the last is a different book (*Software Engineering & Testing: An Introduction*, B. B. Agarwal, S. P. Tayal, M. Gupta, Jones & Bartlett) with no MCQ or answers section at all.
**The only answer key in the vault** is inside the scanned 3rd-edition prose book `Reference_Textbooks/AliFahim_Software_Engineering.pdf`, printed page **497** ("Answers", Chapter 1 block). It was located and read.

---

### N-005 · T7 stays, with a note

> «خليه مع ملاحظة يعني ال t7.. اقتراحك..نعم»

**Decision.** Chapter 1 still gets a `T7_Apply_Calc` file, but it opens with an explicit statement that the chapter has no computational spine — the only applied relationship is `productivity = output / effort` with effort in person-months.
**Scope.** Ch1.

---

### N-006 · Sources added in full now, trimmed later

> «المصادر نضيفها حتة بعدين ممكن نقصقص منها اكيد مو كل الكتاب لهذا نقصقص»

**Decision.** Cite every source in full as the packs are built. Trimming is a later pass, not a build-time concern.
**Scope.** All packs.

---

### N-007 · Keep this log

> «هاي الملاحضات الي اكولها الك خليها بالسجل مال ملاحضات الي بعدين انت وغير ايجنتات يعرفون شحجينا وشقررنا قرارات»

**Decision.** This file exists. Every future student remark that changes how the work is done gets an entry here, at the time it is made.
**Scope.** Vault-wide.

---

## Reference — Aggarwal & Singh 3rd ed. scan: PDF page ↔ printed page

Established 2026-10-16 by reading page headers, not assumed.

**Formula:** for scan PDF page `N`, the left printed page is `2N − 12` and the right printed page is `2N − 11`.

| Chapter | Printed pages | Scan PDF pages |
|:---|:---|:---|
| 1 Introduction | 1–19 | 7–16 |
| 1 — Multiple Choice Questions | 17–18 | 14 (right) – 15 (left) |
| 1 — Exercise | 19 | 15 (right) |
| 2 SDLC Models | 20–39 | 16–25 |
| 3 Requirements | 40–138 | 26–75 |
| 4 Project Planning | 139–202 | 76–107 |
| 5 Software Design | 203–249 | 108–130 |
| 6 Software Metrics | 250–307 | 131–159 |
| 10 Software Certification | 492–507 | 252–256 |
| **Answers** | **497–500** | **255–256** |

**Chapter 1 official answer key** (printed p.497, transcribed from the scan):

`1.1 (a) · 1.2 (c) · 1.3 (d) · 1.4 (a) · 1.5 (b) · 1.6 (c) · 1.7 (b) · 1.8 (a) · 1.9 (b) · 1.10 (d) · 1.11 (a) · 1.12 (d) · 1.13 (a) · 1.14 (a) · 1.15 (b) · 1.16 (d) · 1.17 (b) · 1.18 (d) · 1.19 (d) · 1.20 (a)`

**Cross-check result:** the book's MCQ order on printed pp.17–18 is identical to the slide deck's order, and the answers derived independently from the chapter content matched the official key **20/20**.

**Note on the two Ch1 decks in the vault** — they are the same 64-slide series with *different* internal ordering, so a slide anchor is meaningless unless the filename is named:
`Aggarwal_Singh_Slides/chapter_1_introduction.pdf` (MCQ on slides 57–60) vs `Aggarwal_Singh_SE_3rd_ed_By_Chapter/Ch01_Introduction.pdf` (MCQ on slides 40–43).

---

## N-008 · Language split by function · short answers · the book is never my voice

> «الأسئلة والأجوبة النموذجية تبقى بالإنكليزي، أما ملاحظات الطالب والتنبيهات والفخاخ فتكون بالعربي وباختصار. اختصر الأجوبة إلى القدر الكافي للإجابة والتعليل من أغروال، واحذف التكرار وعبارات التوجيه الامتحاني الزائدة. ميّز أي استنتاج من عندك عن كلام الكتاب، ولا تعرضه كأنه موقف أغروال.»

**Decision — four rules, binding on every chapter pack.**

**1. Language is split by function, not by document.**
- **English:** the question stem, the options, and the **model answer**.
- **Arabic (brief):** student notes, warnings, traps, and anything addressed to the student about how to use or remember the material.

**Scope.** All chapter packs, including the already-built `T1_MCQ` and `T2_Descriptive`.
**Consequence.** This does **not** reopen N-001 — the pack is still English-first and the student still hand-translates the answer text. What changes is that the **advisory layer** (traps, warnings, "remember this") is written in Arabic instead of English, so it reads faster and does not compete with the answer for attention.
**Supersedes:** the part of N-001 that implied *everything* in the pack is English, and the part of N-002 that implied the callout cards are English-only. **N-002's no-table rule itself stands unchanged.**

**2. Answers are shortened to the minimum that answers the question and justifies it from Aggarwal.** Delete repetition, cross-referencing between answers, and exam-coaching filler.
**Consequence.** The first T2 ran to several paragraphs per answer (24 pages); under this rule the same 25 exercises are cut to what each question actually requires. Content appearing in two answers is written once and referenced, not repeated.

**3. Exam-guidance phrases are deleted from the answer text** — formulations such as *"the exam-ready conclusion"*, *"why this matters for marks"*, *"the framing to reproduce"*, *"the one-line test to carry into the exam"*.

**4. My inference is marked, and is never presented as Aggarwal's position.**
> «ميّز أي استنتاج من عندك عن كلام الكتاب، ولا تعرضه كأنه موقف أغروال.»

**Consequence — the strongest rule in this log.** Every answer separates three things: **(a)** what the book says — quoted and page-anchored; **(b)** what follows from it, presented as the student's own reasoning; **(c)** anything supplied that the book does not contain. Category **(c)** is tagged in Arabic as `استنتاجي — مو نص أغروال` and is never placed in the same voice as the book's text.
**Why it matters here specifically.** Two items in `T1_MCQ` were first tagged `[Foundational Knowledge / Standard Concept]` and later turned out to be in the book after all. The opposite error is the dangerous one: a plausible sentence of mine reading as though Aggarwal had written it. This rule makes that impossible to do by accident.

**Also from the same message:** update the build plan and this log to reflect the decision, then produce a fresh test version. The test version is **`T2_Descriptive` rebuilt under N-008**.

---

## N-009 · RTL is mandatory on Arabic text · cite the book by name, and write the page plainly

> «اني لمن اكلك عربي المفروض تعرف انو لازم تتطبق عليها ال rtl اجباري في حقل الكتابة العربي»
> «شنو قصدك بال printed? قصدك علي فاهم سورس لو الكتاب القابل للبحث؟ وهمين اكتب اسم الكتاب عادي.... اكتب اسم الكتاب اغرويل بس او سمورفل او مال بس... واكتب الصفحة عادي... مو برنتد»

**Decision 1 — RTL is mandatory on every Arabic block.**
Arabic text must carry an explicit right-to-left direction; it must never inherit it from the page. An Arabic paragraph left untagged inside an English pack inherits `ltr`, which reverses the word order inside the line and flips trailing punctuation and percent signs — the screenshot showed **`80%` printing as `%80`**.
**Implementation.** `pdf_exporter.py` — `tag_bilingual_blocks()` now tags Arabic-dominant blocks (`≥ 25 %` Arabic letters) with `dir="rtl"`, mirroring the existing `dir="ltr"` tagging of pure-English blocks. Callout titles and bodies get the same treatment in `_render_callout()`. CSS: `[dir="rtl"] { direction: rtl; text-align: right; }`.
**Scope.** Every file in the vault, not only the ASE packs — this was a toolchain-level defect, not a chapter-level one.
**Trap found while fixing it:** adding `flex-direction: row-reverse` to `.callout-title[dir="rtl"]` flips the flex axis a *second* time and puts the icon back on the left. `dir="rtl"` alone is correct. Verified against the render.

**Decision 2 — cite the book by name; write the page plainly.**
- **Drop the word "printed".** Write the page number as it is: `p.4`, `pp.4–5`.
- **Name the book.** The citation carries the author's name — `Aggarwal`, `Sommerville`, `Mall` — because more than one textbook sits in the subject folder and a bare "the book" is ambiguous.
- **Format used:** `**Aggarwal, §1.2.1, p.4.**` — name, section, page.

**His question, answered.** "printed page" meant *the page number printed at the top of the book's own page*, as opposed to the PDF/scan page index — necessary because the scan is a two-page-spread file whose PDF numbering does not match the book's. The source is **the Aggarwal & Singh 3rd-edition book**, which is present in the vault as a scan (`AliFahim_Software_Engineering.pdf`). It is **not** the searchable `CS_Agarwal_SW_Engineering_and_Testing_2010.pdf` — that is a *different* book (B. B. Agarwal, S. P. Tayal, M. Gupta, Jones & Bartlett) with a different chapter arrangement and no MCQ section.
**Since the book's own page numbers are what the citation gives, the word "printed" was redundant and is now removed everywhere.**

**Scope.** All packs; applied retroactively to `T1_MCQ` and `T2_Descriptive`. Both were also re-gated: linter exit 0, zero page splits, zero pipes, zero stray asterisks, and zero occurrences of the word "printed".

---

## N-010 · Review pass: seven corrections, a style rule, and independent verification

> «راجعت حلول T1 وT2 مع صفحات الفصل ومفتاح الإجابات... ما أعتبر النسخة خالية من أخطاء جوهرية بعد.»
> «System 1 يكتب المسودة؛ التحقق المستقل هو اللي يقرر شنو يبقى.»
> «لا تخلي عبارة استنتاجي — مو نص أغروال [بولد]... خليها بشكل عادي والنص مال كتاب خليه بشكل بولد... لا تخليه مائل ابدا.»

**Style rule (immediate, applied).**
- The book's quoted text is **bold**, never italic. All 118 italic quoted spans across `T1_MCQ` and `T2_Descriptive` were converted.
- The tag `استنتاجي — مو نص أغروال` is **plain text** — no bold, no backticks. It marks my reasoning, so it must not compete visually with the book's words.

**Wording discipline (applied).** Verbatim → `Aggarwal states: "…"` + section/page. Faithful paraphrase → `In §…, Aggarwal explains that …`. Inference → the Arabic tag. **Never** write "The book answers…" when the book does not settle the question. ~25 attribution phrases across both files were normalised from "the chapter/the book says" to "Aggarwal states/explains".

**The seven corrections — every one verified against the source before being accepted.**

1. **Management factor order — I WAS WRONG; the review was right.** I had People → Process → Product → Project. **Fig. 1.8 on printed p.15** numbers them **People (1) → Product (2) → Process (3) → Project (4)**, and §1.6 opens by naming them in that same sequence. §1.6.3, printed p.16, states it outright: *"The process priority is after people and product, however, it plays very critical role for the success of the project."* Fixed in `T1` Q1.13, `T2` Q1.24 and the T2 self-test.
2. **`T2` 1.25 attributed an inference to the book.** "The book answers process-first" was too strong — the book gives a dependency, not a ranking, and its own order puts product ahead of process. Rewritten: Aggarwal's sentences first, then the weighting tagged as inference.
3. **`T1` 1.6 gave an incomplete metric list.** §1.5.4, printed p.13: *"Examples of product metrics are size, reliability, complexity, functionality etc."* — I had omitted **functionality**. Fixed; the answer now quotes the list in full.
4. **`T2` 1.13 asked for a diagram and only described one.** A real figure was drawn (`_diagrams/d1_wearout.png`, rendered via `diagram_forge`) showing failure intensity against time — the hardware bath-tub curve against the software descending curve — and inlined into the answer.
5. **`T1` B.4 conflated two separate sections.** The absence of CASE tooling not being a cause of process-improvement failure (§1.2.3) is a *different* question from why CASE tools cannot end the crisis (§1.1.2). The answer now separates them explicitly.
6. **Answers were not self-contained.** `T2` 1.10 and 1.13 referred back to earlier answers; both now carry their own definitions and lists. `T2` 1.15's open-source addition — not asked for by the question — was removed.
7. **The answer-key page number was wrong — the review was right.** I had p.497. **The key page bears 498 at its foot** (p.497 is still Chapter 10). Corrected in `T1` and in `Ch01_BUILD_PLAN.md`.

**Independent verification — the review's proposed workflow, implemented.**
Protocol written: `_VERIFICATION_PROTOCOL.md`. Method: the writer drafts from the source; then a **blind verifier** receives the source page images plus a list of **atomic claims** — never the writer's prose — and marks each claim SUPPORTED / PARTIAL / NOT FOUND / CONTRADICTED, quoting the supporting sentence and reading the printed page number off the image itself. Basis: Chain-of-Verification (Dhuliawala et al., arXiv:2309.11495) and OpenAI's "treat the answer as a first draft" guidance. **System 1 drafts; verification decides.**

**First round result (2026-10-16):** 25 claims vs printed pp.1–19 → **24 SUPPORTED** (each with a quoted sentence and page), 0 PARTIAL, 0 CONTRADICTED, **1 NOT FOUND** — `C03`, the answer key, which lies outside that page range (it is on p.498) and was verified separately at 20/20.
Two catches by the verifier, both re-checked by me:
- **`C06`** — it read the source as "The CMM process priority is after people and product" and flagged my quote for dropping "CMM". At 520 DPI the page shows the CMM sentence **ends**, and the next sentence begins "The process priority is after people and product" ⇒ **my quote is correct**; the verifier had merged two sentences. Still worth quoting both sentences together to prevent the same misreading.
- **`C15`** — it noticed the source spells **`overtime`** as one word where I had written `over time`. **Correct, and fixed** — the quote now follows the printed spelling with a note.

**Also confirmed independently:** the scan page mapping. The verifier read the printed page number off each image and returned `book_p01 → 1` … `book_p19 → 19` — an exact match for the derived formula.

**Limits recorded:** this protocol *reduces* hallucination, it does not eliminate it; a `NOT FOUND` verdict can mean "outside the pages reviewed" rather than "false", so each round must state its page range; and one round does not cover a whole chapter.

---

## N-011 · The answer carries no essay framing — and a bold-ratio check to police it

> «اريد الحل جاهز ما اهتم انو افهم او اقرا اغرول شيريد او شيحجي... ف نسوي هيج ونشوف اذا كملنا التيستات لو لا.»
> «مجرد النص الحرفي يكون بولد.. والنص العادي الي احنا نحجيه يكون عادي بدون اي شي لا مائل ولا بولد ولا مختلف.»

**Decision 1 — strip the framing.** Answers no longer open with *"Aggarwal states…"*, *"In §…, Aggarwal explains…"*, *"The book answers…"*, *"the chapter gives…"*. The answer **is** the content: the source's words in bold, plus the minimum plain connective text needed to make it read. 33 framing phrases were removed across `T1_MCQ` and `T2_Descriptive`; **no answer text now names Aggarwal or "the chapter" at all.**

**Decision 2 — the bold/plain split carries the attribution, so nothing is lost.**
- **Bold** = the source's words.
- **Plain** = our words.
- **Italic is banned everywhere** — 9 stray italics were removed.

This is why the change does not weaken N-008's honesty rule: the reader can still see instantly which text is Aggarwal's. The rule moved from prose to typography.

**The guardrail I proposed, and he accepted.** If bold = the source and plain = us, then **an answer that is mostly plain is an answer I mostly wrote** — which is exactly where invention hides. So each answer now gets a **bold ratio**, measured mechanically. It is a diagnostic, not a target: a low ratio is a prompt to look, not automatically an error.
- **The check immediately found 5 answers with 0–5 % bold** — i.e. answers built entirely from my own prose. They were rewritten to lead with the source's wording (T1 1.2, 1.7, 1.12, 1.17, B.1), and T2 1.10's seven bridge-versus-program contrasts were replaced with the table's own row text.
- **Result:** `T1_MCQ` mean bold **39 % → 48 %**; `T2_Descriptive` mean **62 % → 64 %**.
- **Honest reading of the number:** a multiple-choice answer is mostly *reasoning about why an option is right*, so a lower ratio there is structural, not suspicious. The remaining sub-30 % answers are the **authored** MCQs (B.1, B.2, B.4, B.5, B.7) plus three short official ones — all of which are explanation by nature. The diagnostic's real job is to catch **zero**, and it did.

**Scope.** All packs, retroactively applied to `T1_MCQ` and `T2_Descriptive`. Both re-gated: linter exit 0, zero page splits, zero pipes, zero stray asterisks, zero italics, zero unbalanced bold.

---

## N-012 · The answer is a direct answer — one contiguous quotation, no glue

> «واني كلتلك ما اريد تذكر الكتاب بالاجابة ابدا... هي الاجابة اجابة ما يهم اكتب من الكتاب حرفيا THE BOOK ما اريد هيج... موجود سؤال... اكتب الجواب مباشرة.»

**What he was objecting to.** N-011 removed the words "Aggarwal states…" — but the answer still *talked about* the source. The concrete case he quoted:

> The change is **"due to increase in cost of maintaining software"**, so the objective is now to produce **"quality software that is maintainable, delivered on time, within budget, and also satisfies its requirements."**

That is **one sentence of the book cut in half and stitched back together with my own connecting words.** Removing the name Aggarwal did not remove the meta-discourse — it was still me narrating what the source says.

**Decision — three rules, applied to all packs.**

**1. If the source sentence answers the question, quote it whole.** No splitting, no connective text between fragments.
> **"Due to increase in cost of maintaining software, objective is now shifting to produce quality software that is maintainable, delivered on time, within budget, and also satisfies its requirements."**

**2. No meta-discourse anywhere in an answer.** Banned: *"The change is…"*, *"so the objective is now to produce…"*, *"The premise:"*, *"A worked example from §…"*, *"Note what he then adds…"*, *"The same page offers…"*, *"The book's own contrast:"*, *"The book's summary:"*, *"It records the industry's own verdict:"*, *"The reason is where he locates the difficulty —"*. Only two kinds of text remain: **the source's words (bold)** and **a short label or link (plain)** such as *"Nine myths:"* or *"Two examples:"*.

**3. No name and no self-reference in an answer.** No "Aggarwal", no "he", no "the book", no "the chapter". (Verified mechanically: **0 occurrences in either pack** — the only remaining mentions are the source line, the Arabic note cards, and the frontmatter.)

**Scope.** Applied across `T1_MCQ` and `T2_Descriptive`: 23 replacements in T2, 6 in T1, plus 8 question-stem cleanups.

**Result.**
| File | mean bold, before | after |
|:---|:---:|:---:|
| `T1_MCQ` | 48 % | **52 %** |
| `T2_Descriptive` | 64 % | **69 %** |

**Gate:** both linter exit 0 · 28/28 and 25/25 stem→answer pairs · 0 page splits · 0 pipes · 0 stray asterisks · 0 italics · 0 unbalanced bold.

**Also fixed:** the stale `T2_Descriptive.pdf` was replaced once the preview released its write lock; the temporary `T2_Descriptive_new.pdf` fallback has been deleted.

---

## N-013 · Final limited audit + the simplification convention

> «اني ما اتفق انو ناخذ حرفيا حرف بحرف... الكلمات الصعبة الاكاديمية ممكن نبدلها ترا بكلمات اسهل... يحتاج فحص ودورات فحص اكثر تقدم... هسه يلا بينا ننطلق»

**Decision 1 — the simplification convention (new, formal).** Together with N-011's bold/plain split, the typography now carries a three-way contract:

| What the writer is doing | How it looks on the page | Example |
|:---|:---|:---|
| Quoting the source exactly, word-for-word | **bold + between straight quotation marks** | **"If the process is weak, the end product will undoubtedly suffer…"** |
| Source content, with hard academic words replaced by simpler ones | **bold, no quotation marks** | **"Because the cost of maintaining software increased, the objective is now to produce software that is maintainable, delivered on time, within budget, and that satisfies its requirements."** |
| A short label or link the writer added | plain (no bold, no italic) | *"Nine myths:"* · *"Two examples:"* |
| The writer's inference or addition | plain Arabic tag on its own line | استنتاجي — مو نص أغروال |

**Why it is safe.** N-011 already bound **bold = the source's words** and **plain = our words**. The simplification rule keeps that contract — a bold span is still the source — but admits that *how the source's idea is phrased* may be simplified when the original wording is academic. Italic remains banned. The reader can still tell at a glance which spans are sourced.

**Scope.** All packs. The `T2_Descriptive` CONCEPT card was rewritten to state the three layers in this new wording; `T1_MCQ` carries the same convention by inheritance.

---

**Decision 2 — the final limited audit. Four review points + one I caught myself.**

The review and Codex raised four specific points. Each was fixed and re-verified mechanically and visually:

1. **T2 1.1 — the "Due to" wording vs source "However, due to".** Per the simplification convention, the answer is now **bold without quotation marks** and paraphrases the source's idea in plain English. No "The change is… so the objective is now to produce…" glue. Contiguous, single span.
2. **T1 — "He adds:" / "He gives the reason:" violations of N-012.** A fresh capital-`He` scan caught `T1 1.5` ("The same page adds the counterweight —") in addition to the B.3 / B.6 fixes. 1.5 now carries two contiguous bold quotes back-to-back, no connective meta-discourse.
3. **Plan — Answer key was 497, should be 498.** Plan and `T2_Descriptive` frontmatter both corrected to **p.498** (verified by reading the printed foot of scan PDF 255L/255R/256L = 498/499/500). The full range is **498–500** at PDF 255–256.
4. **T1 B.4 — duplicate source line.** Two identical `**Aggarwal, §1.2.3, pp.6–7.**` lines collapsed to one. The two questions (why process improvement fails vs why CASE tools can't end the crisis) are now kept separate in the answer.

**Verification (mechanical + visual).**

| Check | T1_MCQ | T2_Descriptive |
|:---|:---:|:---:|
| Linter (`note_linter.py --fix --strict`) | exit 0, PRISTINE | exit 0, PRISTINE |
| Pages | 10 | 14 |
| Question stems detected | 28 | 25 |
| Orphaned stems (stem on a page, no answer) | **0** | **0** |
| `**Aggarwal, §1.2.3, pp.6–7.**` count (B.4 dedup) | **1** | n/a |
| `He ` / `he ` / `the book` / `the chapter` / `printed` inside answers | **0** | **0** |
| Meta-discourse phrasings ("The same page…", "The book…", "Note what he then…", etc.) | **0** | **0** |
| "However, due to" / "Due to" wording used | n/a | simplified form |

**Visual spot-check (rendered pages 1, 3, 8, 13):** Arabic frontmatter and callout cards are right-aligned (RTL honoured); simplification-convention card on T2 p1 reads correctly; 1.1 leads with the simplified bold span; 1.5 has two clean quotes; B.4 has one source anchor; 1.24 uses the numbered management order (1→2→3→4) with no author references; 1.25 carries the Arabic inference tag in RTL.

**Result.** T1 and T2 pass all three gates of the build-plan delivery checklist (linter, exporter, visual). The first two packs of Chapter 1 are **ready for closure**, pending the student's final review.

---
*Log opened 2026-10-16.*


---

## N-014 · تثبيت القرارات النهائية لجابتر 1 (مرحلة «الرضا») + معايير السؤال والجواب والتدقيق

> «طيب وصلنا للمرحلة الرضا... هسه اريدك ثبّت قراراتنا النهائية لجابتر 1 في خطة البناء والسجل... معيار السؤال والجواب: السؤال والجواب بالإنجليزي وملاحظات الطالب والفخاخ بالعربي · لا يشترط نقل الإجابة حرفياً بسّط الكلمات الأكاديمية الصعبة · الاقتباس الحرفي فقط بين تنصيص وصياغة المعنى بكلمات أسهل بولد بلا تنصيص وأي استنتاج يُوسم بالعربي · إجابة واضحة ومكتملة بلا حشو وارفق مرجع المصدر ورقم الصفحة · أغروال الطبعة الثالثة هو المصدر الأساسي ونستخدم الكتب الأخرى فقط لنقطة ناقصة... معيار التدقيق: نجاح الـlinter أو الفحص البصري يثبت سلامة التنسيق فقط وما يثبت صحة المحتوى · راجع كل سؤال وجوابه ومطالباته المهمة مقابل صفحات المصدر وميّز الاقتباس الحرفي عن التبسيط والاستنتاج ولا تكتفِ بعيّنة صغيرة ولا بنسبة الـbold · حافظ على تنسيق السؤال وجوابه معاً وافحص الـPDF النهائي بصرياً... T1 وT2 موجودان ولا تعِد بناءهما، حدّث عدد صفحات T2 إلى 14 ووحّد وصف حالته، سجّل أن تدقيق المطالبات لكل جواب ما زال مطلوباً... أنشئ 00_INDEX ثم ابدأ بـT3.»

**Decision — the format is now LOCKED as the binding contract (N-014).**

**1. The two standards are written into `Ch01_BUILD_PLAN.md` as the final law** (the student called it the «رضا» / satisfaction milestone):

- **§5.10 معيار السؤال والجواب** — five points: (a) EN question + EN model answer, AR notes/traps; (b) literal copying not required — simplify hard academic words while keeping meaning, accuracy, and important detail; (c) typography-of-evidence contract — literal quote = bold + quotation marks, simplified meaning = bold without quotation marks, our inference/addition = clearly tagged in Arabic; (d) answer clear and complete, no padding or meaning-losing abbreviation, with source reference + page number; (e) Aggarwal 3rd ed. is the primary source, other books only for a required point missing in it, with its source stated.
- **§5.11 معيار التدقيق** — three points: (a) linter pass or visual check proves *format* only, not *content* truth; (b) audit every pack by reviewing **every** question, its answer, and its important claims against the source pages, distinguishing literal / simplified / inference — never a small sample, never the bold ratio alone; (c) keep question+answer together on print and inspect the final PDF visually.

**These consolidate and supersede the scattered N-001 … N-013 notes into one binding pair of standards.** They are the template for every future chapter pack.

**2. Plan housekeeping (N-014).** §4 structure table updated: T2 row now **14 pages** with status unified to «مطابق لكل القرارات النهائية N-001…N-013»; T1 unchanged (10 pp); `00_INDEX` marked building; T3–T7 marked «مطلوب». A warning box records that **claim-level verification of every answer against source pages is STILL REQUIRED** before declaring Chapter 1 complete. §6 deferred items updated accordingly. Footer → N-014.

**3. Work status (explicit).** T1_MCQ and T2_Descriptive **exist in their current form — do NOT rebuild from scratch.** Chapter 1 closure is **NOT declared** until: all required packs exist (T3–T7 + 00_INDEX) AND per-answer claim verification is done AND the final PDF is visually inspected.

**4. Next step (in progress).** Build `00_INDEX` as a clear map of all Ch1 question types/files/status, then start `T3_Understand` (Q1.1, 1.3, 1.6, 1.11, 1.18) strictly per §5.10/§5.11.

**Scope.** All ASE chapter packs, and the standing contract for other agents/harnesses that open this vault.

---

## N-015 · إنجاز 00_INDEX وT3 + إصلاح خلل ترابط السؤال/جواب في المُصدِّر (vault-wide)

**Context.** Executing N-014's next step: built `00_INDEX` (the Ch1 file/status/weight/source map) and `T3_Understand` (5 understanding-level why/how questions U.1–U.5), then verified them per §5.11.

**🔴 Toolchain defect found + fixed (affects every pack, not just Ch1).** The `keep-next` cohesion rule (N-003: stem + answer must never split across a page) was **silently broken for letter-badged stems**. Root cause, isolated empirically:
- `transform_qa_cards` is inert on the real packs — it only matches `<blockquote>` answers, but answers are `> [!NOTE]` **callout `<div>`s**, so it produces 0 qa-cards for T1/T2 *and* T3.
- The class is actually applied by the **`attr_list` extension**, which is flaky: it works for T2's numeric `1.N` stems (25/25) but **fails silently for T3's `U.N` stems** → 5 literal `<p>{: .keep-next }</p>` leaked into the PDF and 5 stems orphaned across page breaks.

**Fix (additive, idempotent, safe).** Added `apply_keep_next(html)` to `90_Shared_Toolbox/tools/pdf_exporter.py`, run right after `transform_qa_cards`: consumes any leftover `{: .keep-next }` paragraph and attaches `class="keep-next"` to the immediately preceding single-paragraph `<p>`. Uses `(?:(?!</p>).)*` to keep the match to one paragraph (a first draft used `.*?</p>` which backtracked across paragraphs and tagged the wrong `<p>` — caught by printing match spans). T1/T2 already handled by attr_list → untouched.

**Verified.** PyMuPDF text layer: literal `keep-next` = **0** in T1/T2/T3; T3 **5/5** stems share a page with their answers; T1/T2 unchanged (10/14 pp, byte-identical PDF sizes → no regression); both linter exit 0 PRISTINE. Temp debug scripts removed.

**Work status (N-015).** T1 ✅ (10 pp) · T2 ✅ (14 pp) · T3 ✅ (4 pp) · INDEX ✅ (2 pp). Chapter 1 closure **still NOT declared**: T4–T7 outstanding, and **per-answer claim-level verification of T1/T2/T3 against source pages is still required** (N-014 §5.11b).

**Scope.** Vault-wide — fixes Q&A cohesion for every current and future chapter pack.

---

## N-016 · تفويض OpenCode لإكمال Ch1 (T4–T7 + V1) وقرارات أسلوب الجواب النهائية

> «استلمت هذا العمل من WorkBuddy… هدفي إكمال جابتر 1 من حيث وصل، من دون إعادة ما اكتمل… لا تعِد T1–T3 إذا كانت موجودة وسليمة… تابع العمل من أول عنصر ناقص… انطلق بالتنفيذ… امشِ على الخطوات بالترتيب من T4 إلى T7، ثم ملف المفردات V1، ثم تحديث الفهرس والخطة والحالة… لا تعمل commit أو push.»

**Context.** The ASE Ch1 pack (T1/T2/T3 + 00_INDEX) was built by WorkBuddy (Koko 🐨, 2026-10-16, N-001…N-015) and handed off with an uncommitted vault-wide `pdf_exporter.py` `apply_keep_next()` fix. The student handed the unfinished part to **OpenCode (DeepSeek V4.1 Flash)**: build **T4_Analyze → T5_Evaluate → T6_Create → T7_Apply_Calc**, then **V1_Vocabulary_Coverage**, then update `00_INDEX`, `Ch01_BUILD_PLAN.md` and `ACTIVE_STATE.md`.

**Decision 1 — vocabulary deliverable is a separate file.** `V1_Vocabulary_Coverage.md` / `.pdf` inside `Ch01_Introduction/` (not a block inside `00_INDEX`). It maps every Lecture-1 term (2026-09-16 list) to where it is covered (`file → §, p.`), with a one-line Arabic note per term.

**Decision 2 — Aggarwal stays the primary source.** A **named** supporting book is allowed to fill a **real gap**, with its source stated explicitly as a supporting source. Nothing is promoted over Aggarwal.

**Decision 3 — no unsourced facts.** *Shuttle* is added to T4 **only if** a reliable support is found in the subject materials or a suitable source; otherwise it is recorded as **not documented** — no invented detail. **IBM OS/360 numbers must NOT be fixed/asserted before they are documented.** (This supersedes any earlier stated OS/360 figures in older vault notes for the purpose of these packs.)

**Decision 4 — newest preferences override older rules (esp. N-012's "quote it whole").** The student no longer requires **verbatim** book answers: *he wants the answer to come from the source, but not necessarily word-for-word, and with no long essay-style wording inside the answer.* The answer must still be **grounded in the source** (no generation/hallucination), English, **clear and concise**, with hard academic words simplified where the meaning is preserved. Arabic student notes / traps stay **brief**. The N-013 typography-of-evidence contract still stands (bold+quotes = literal · bold no quotes = simplified source · plain = our label · `استنتاجي — مو نص أغروال` = inference), and italics remain banned.

**Scope.** ASE Chapter 1 packs, and the standing contract for future packs.

**Consequence.** T4–T7 and V1 are built under this; T1–T3 are **not** rebuilt. No `commit`/`push` unless the student asks. The open claim-level verification gate (N-014 §5.11b) still stands before Chapter 1 closure.

---

## N-017 · جولة الإغلاق المختصرة: الجواب المباشر + تأجيل التدقيق الشامل حتى جابتر 2

> «راجع أجوبة T1–T7 وV1 مروراً سريعاً. داخل الجواب النموذجي احذف أي صياغة مثل "the book says" أو "the author states" أو "the book does not classify it"، واكتب الجواب مباشرة. أبقِ مرجع المصدر بسطر مستقل بعد الإجابة… إذا كان الجواب استنتاجاً، اكتب الجواب مباشرة واترك وسم استنتاجي — مو نص أغروال بملاحظة عربية خارجه… حدّث الخطة والفهرس والحالة: حزمة جابتر 1 جاهزة للدراسة والطباعة، والتدقيق الشامل مؤجّل بقراري حتى ننتقل لجابتر 2. لا تسجّل أن كل الادعاءات خضعت لتدقيق شامل.»

**Decision 1 — direct answers (extends N-012).** Inside a model answer, remove source-reference phrasing — «the book says/states», «the author states», «the book does not classify it» — and state the answer directly. The `**Aggarwal, §x.y, p.N.**` line stays **on its own line after the answer**; naming the source there is required. An inference answer is written directly and carries only the Arabic tag `استنتاجي — مو نص أغروال` outside it.

**Decision 2 — T4 A.2 rewritten.** The question no longer asks «why the book calls it…» and the answer no longer says «because the book calls it…». It now covers the **cause, the description, and the handling cost**: using the two digits caused the problem, it was described as **"practically non-existent"**, and handling it cost **"millions of rupees"** — no extra interpretation of the description.

**Decision 3 — short round, no rewrite / no new audit.** Only the changed files were re-exported and visually checked (T1, T4, T5); no file was rewritten wholesale and no new comprehensive audit was opened.

**Decision 4 — closure status.** The Chapter 1 pack is **ready for study and printing**. The **comprehensive claim-level audit is DEFERRED by the student's decision until Chapter 2 begins** — it has **not** been run. It must **not** be recorded that all claims passed a comprehensive audit: N-014 §5.11b stays a **deferred** (not completed) item.

**Applied.** T4 A.2 (question + answer) · T4 A.7 · T5 E.1 · T1's module item (the phrase «and then states» removed). Re-gate: linter PRISTINE (T1/T4/T5/`00_INDEX`) · exports OK · **T1 28/28 · T4 7/7 · T5 3/3 stems share their page with the answer** · 0 `keep-next`.

**Scope.** ASE Chapter 1 packs; the deferral applies to the Ch1 audit gate.

---

## N-018 · رفع التأجيل — التدقيق الشامل لجابتر 1: التقرير والحدود والتصحيحات

> «نفّذ الآن التدقيق النهائي الشامل لجابتر 1… لا تعلن أن جابتر 1 مغلق إلا بعد… لا تكتب أن الحزمة «موثقة بالكامل» إذا بقي ادعاء غير محسوم… وفي التقرير النهائي أعطني نتيجة كل ملف، عدد الادعاءات… والتصحيحات… وما بقي غير محسوم.»

**Context.** N-017 كان قد أجّل هذا التدقيق؛ الطلب الحالي **يرفع التأجيل** ويأذن بتنفيذه. **إعلان إغلاق جابتر 1 لم يحدث** — القرار الرسمي يبقى للطالب.

**النطاق.** كل جواب في `T1_MCQ` · `T2_Descriptive` · `T3_Understand` · `T4_Analyze` · `T5_Evaluate` · `T6_Create` · `T7_Apply_Calc` = **73 وحدة سؤال/جواب** + **13 مدخلاً** في `V1_Vocabulary_Coverage` + اتساق `00_INDEX`/الخطة/الحالة.

**المنهج — ثلاث طبقات:**
1. **مراجعة متقاطعة للمصادر** (كاتب/مراجع منفصل) — وجدت **9 نقاط جزئية** من أصل 73 وحدة في T1–T7، ومدخلاً جزئياً في V1، وصُحّحت كلها (مسجّلة في `_VERIFICATION_PROTOCOL.md` §6).
2. **تدقيق الكاتب (OpenCode)** بقراءة مباشرة لسكان أغروال (المطبوع **1–19 = PDF 6–15**، مفتاح الأجوبة **ص.498 = PDF 255L**) + الشرائح الرسمية (الشاتل 14–15 · تجميع الخرافات 36–46) + **Sommerville** §11.2 ص.297 و§1.2 ص.15–16 + **Pressman** §8.4.1 ص.203 — نتجت **5 تصحيحات مستقلة إضافية:** T1 B.5 · T1 B.6 · T2 1.16 · V1 بند 2 · V1 بند 8.
3. **مدقق ثانٍ مستقل (نموذج منفصل)** استلم **صور صفحات المصدر + 20 مطالبة ذرّية مجرّدة فقط** (بلا نصوص الكاتب) وأعاد **20/20 SUPPORTED** باقتباس ورقم صفحة مطبوعة، بضمنها تأكيد **غياب** عبارة «concerned with all aspects of software production» من الكتاب (أساس تصحيح T1 1.19). قوبلت النتائج بنداً ببند مع قراءة الكاتب: **لا خلاف**.

**التصحيحات الكلية — 17 موضعاً (اتحاد الجولتين، و T1 1.19 لمسَته كلتا الجولتين):**
T1: **1.19** (نص شرائح كان منسوباً للكتاب → تعريفا §1.2.1 + مرجع المفتاح ص.498 + وسم الاستنتاج) · **B.5** (الخُرافة من الشرائح سلايد 45 لا §1.4) · **B.6** (النص الحرفي من سلايد 46 → خُرافة الكتاب 9، §1.4 ص.12).
T2: **1.7 · 1.8 · 1.16 · 1.22 · 1.25** (إجابات مباشرة/جذوع موحّدة؛ حذف سطر ميتا).
T3: **U.2** (صياغة حذرة: تزامن العتاد ≠ إثبات سببية).
T4: **A.1 · A.7** (صياغة مباشرة؛ إزالة نسبة الاستنتاج للكتاب).
T5: **E.3** (حكم مباشر متوازن).
V1: **بند 2 · بند 8 · مداخل 11–13** (إسناد §1.3 ص.10–11؛ حذف دعوى «الشرائح تذكر أقل»؛ إكمال المداخل الثلاثة بأجوبة مصدر مساند).
**لا تصحيح في T6 أو T7** (فُحصا وثبتا).

**نتيجة كل ملف (الوحدات المدقّقة · التصحيحات):** T1 **28 · 3** (مفتاح 20/20 ✓) · T2 **25 · 5** · T3 **5 · 1** · T4 **7 · 2** · T5 **3 · 1** · T6 **2 · 0** · T7 **3 · 0** · V1 **13 · 5**.

**البوابات النهائية:** `note_linter --fix --strict` PRISTINE لكل ملف تغيّر · تصدير كامل و**كل PDF أحدث من MD المطابق** · تماسك السؤال/الجواب: **73/73 وحدة بلا انقسام** (T1 28/28 · T2 25/25 · T3 5/5 · T4 7/7 · T5 3/3 · T6 2/2 · T7 3/3) · صفر بقايا وسم في طبقة النص · فحص بصري للصفحات المتغيّرة.

**غير محسوم / حدود:** لا ادعاء جوهري باقٍ `PARTIAL/NOT FOUND/CONTRADICTED` ضمن النطاق المفحوص. الحدود الواجب ذكرها: (أ) «غير موجود» محدود بالصفحات والشرائح والكتب المفحوصة (المطبوع 1–19 + ص.498 + الشرائح + Sommerville/Pressman)؛ (ب) المدقق المستقل **نموذج لا إنسان**؛ (ج) نجاح الـlinter والفحص البصري يثبتان **التنسيق** لا صحة المحتوى؛ (د) التدقيق لا يثبت أن كل سؤال امتحاني محتمل مغطى؛ (هـ) المداخل 11–13 **بلا سند عند أغروال Ch1** وهي مغطاة بمصدر مساند مسمّى. **إعلان إغلاق جابتر 1 ما صار — القرار للطالب.**

**Scope.** ASE Chapter 1 packs.

---
*Log opened 2026-10-16.*

## N-020 · قاعدة الإسناد بالتنسيق وإغلاق جابتر 1

**القاعدة الحالية التي تعتمد في الملفات القادمة:** الكلام المبني على المصدر يُكتب **بولد**، والصياغة أو الاستنتاج العادي يبقى بنص عادي. لا نضيف عبارة «استنتاجي — مو نص أغروال»؛ لا يهم أن يكون الاستنتاج موجوداً ما دام السؤال يسمح بحكم معلّل، وتبقى الملاحظات العربية مختصرة وخارج جواب الإنجليزية. الاقتباس الحرفي ليس مطلوباً، والكلمات الأكاديمية الصعبة يمكن تبسيطها مع حفظ المعنى.

**إغلاق Ch01:** أُنجزت مراجعة متقاطعة لجميع أسئلة T1–T7 (73 سؤالاً) ومداخل V1 الـ13 مقابل صفحات المصادر ذات الصلة؛ صُحّحت الحالات الجزئية. هذه مراجعة متقاطعة وليست تدقيقاً أعمى. ثبتت بوابات الملفات: linter، تصدير PDF، تماسك السؤال/الجواب، وفحص بصري للصفحات المتغيرة. صحّح Codex في الجولة الأخيرة جواب T1 1.19 بإخراج الملاحظة العربية من جواب الإنجليزية، وأزال تكرار التنبيه في T5 E.2، وعدّل صيغة سؤال E.2 إلى مشاريع التطوير، ونقل قراءة T6 D.2 التحليلية إلى بطاقة عربية خارج الجواب. الحالة: **جاهز للدراسة والطباعة**. لا commit/push.

## N-021 · بروتوكول موحّد لحزم أسئلة ASE عبر الوكلاء

لتجنب تكرار أخطاء Ch01 في الفصول التالية، صار المرجع المشترك `00_STUDIO_HUB/guides/ASE_QUESTION_PACK_PROTOCOL.md`، وربطه Codex بتوجيهات `AGENTS.md` حتى يقرأه كل harness يعمل على حزم ASE. يكمّل البروتوكول قرارات N-019/N-020: يحدد النطاق قبل الإنشاء، يميّز الكتاب عن الشرائح، يتطلب إجابة فعلية للمفردات، يجيب فعل السؤال، يراجع الادعاءات والوحدات والسببية، يفصل تدقيق المحتوى عن التغطية والتصدير والتنسيق، ويمنع ادعاء مراجعة عمياء أو إغلاق أوسع مما حصل فعلاً. حُدّثت مهارة Codex `ase-study-lead` لتقرأ البروتوكول، مع تسوية تناقض اللغة القديم في خطة Ch01. لا تغيير على قرار الإغلاق الرسمي لـCh01.

## N-022 · إغلاق جابتر 1 رسمياً وبدء تخطيط جابتر 2

أعلن الطالب إغلاق جابتر 1 رسمياً بتاريخ **2026-10-16**. النطاق الذي أُغلق: T1–T7 (73 سؤالاً/جواباً) وV1 (13 مفردة)، مع مراجعة متقاطعة للمصادر، فحص OpenCode لصفحات المصدر، ومدقق مستقل لـ20 مطالبة ذرّية؛ صُحّحت النقاط الجزئية، واجتازت الملفات بوابات linter والتصدير وتماسك 73/73 والفحص البصري للصفحات المتغيرة. الحدود: المراجعة المتقاطعة ليست عمياء، والمراجعة المستقلة غطت 20 مطالبة فقط، ولا يثبت ذلك تغطية كل سؤال امتحاني محتمل. تحدّثت حالة Ch01 في الفهرس والخطة و`ACTIVE_STATE.md`.

**ملاحظة مفردات Ch02:** ملف `SE_Lec02_Software_Life_Cycle_Models (archive).pdf` موجود في مواد المادة ويحتوي 42 صفحة، منها 41 صفحة محتوى معنونة. يغطي Build & Fix، Waterfall، Incremental Process Models، Iterative Enhancement، RAD، Evolutionary Models، Prototyping، Spiral، Unified Process، واختيار النموذج. لا يظهر فيه V-Model أو Agile/XP/Scrum. هو مفيد لتثبيت تغطية المحاضرة، لكن اسم المدرّس/المؤلف غير مثبت في الصفحات؛ لذلك قائمة Ch02 الرسمية تُعد مؤقتة حتى مطابقتها مع مفردات الدكتور التي يرسلها الطالب. يجب الحفاظ على الفرق بين **Iterative Enhancement** و**Iterative Waterfall**.

## N-023 · تخطيط جابتر 2: الرسومات، مصادر المفردات، وأنواع الأسئلة وأوزانها

في 2026-10-16 راجع Codex نسخة Ch02 المصوّرة من كتاب Aggarwal & Singh وملفات المحاضرة والكتب المساندة. تصحيح هوية المصدر: ملف Aggarwal القابل للبحث (48 صفحة) هو شرائح مرافقة للكتاب، وليس متن الكتاب؛ متن الكتاب المحلي نسخة ممسوحة. استُخرجت 21 صورة مرجعية عالية الدقة من الشرائح لتخطيط الشرح، ولم يُنشأ أي ملف أسئلة للفصل الثاني.

ثبتت الخطة أنواع الأسئلة بأعداد بنك المصدر: 25 MCQ و22 سؤالاً تحريرياً. الأوزان 53.2% و46.8% هي **حصة بعدد الأسئلة للتدريب فقط، وليست درجات امتحان**. التحريري: 14 شرح/تعريف/تعداد/وصف، 3 مقارنة، 4 تحليل/تفسير/مخاطر، ورسم واحد. لا توجد مسائل حسابية في البنك المفحوص، و6 من 25 MCQ عن ملاءمة/اختيار النموذج. مفردات V-Model وIterative Waterfall وAgile/XP/Scrum تبقى معلّقة إلى تأكيد دخولها بالمقرر. صُححت كذلك ادعاءات قديمة عن تغطية Mall وSommerville؛ راجع خطة Ch02 المصدرية قبل الاستشهاد. لا يوجد دليل على توزيع درجات الدكتور.

## N-024 · حسم هوية كتاب Aggarwal الممسوح مقابل كتاب Agarwal 2010

سأل الطالب عن احتمال أن تكون نسخة `AliFahim_Software_Engineering.pdf` كتاب *Software Engineering & Testing: An Introduction* (B.B. Agarwal, S.P. Tayal, M. Gupta؛ Jones & Bartlett، 2010). فحص Codex صفحة عنوان الكتاب القابل للبحث وفهرسه، وقارنها بفهرس السكان المزدوجة وبالشريحة الأولى وفهرس شرائح K.K. Aggarwal & Yogesh Singh. النتيجة: **ليسا الكتاب نفسه**. كتاب 2010 يبدأ Chapter 1 في ص.3 وChapter 2 في ص.29 وبترتيب عناوين مختلف؛ السكان يبدأ Ch1 في ص.1 وCh2 في ص.20، وفهرسه يذكر “Preface to the Third Edition”، ويطابق بنية ومواضع كتاب K.K. Aggarwal & Yogesh Singh، الطبعة الثالثة، الذي تنتمي إليه شرائح الـ48 صفحة. لذلك السكان والشرائح من مرجع K.K. Aggarwal & Singh، وليس من كتاب B.B. Agarwal et al. 2010. **حدّ الدليل:** صفحة عنوان/اسم مؤلفي السكان مفقودة، لذا تعيينه إلى K.K. Aggarwal & Singh عالي الثقة من الفهرس والترقيم وتطابق المصدر، لكنه ليس قراءة مباشرة لاسم المؤلف على غلاف السكان. حُدّثت خطة Ch02 لتبيّن هذا الحد.

## N-025 · قاعدة معرفة محلية للفصل 2 ومعايرة العمق

بناءً على توضيح الطالب في 2026-10-16: قائمة مفردات الدكتور هي نطاق التغطية؛ المطلوب شرح أعمق قليلاً من السلايدات بالقدر الذي يعرّف المصطلح ويشرح آليته أو شروطه ويميّزه عن المصطلحات المشابهة. لا نوسّع إلى مسح موسوعي للكتب. عند وجود نقص، نقارن المصادر لذلك المصطلح ونختار أوضح مصدر مساند واحد، بدلاً من جمع كل ما تقوله الكتب. سجل `5-word.json` (جلسة Ch5/Ch6) قرينة على منهج مطابقة المفردات بالمصادر، وليس قائمة مفردات Ch2 ولا قولاً مباشراً جديداً للدكتور عن هذا الفصل.

أُنشئت قاعدة مشتركة محلية `00_STUDIO_HUB/indexes/04_Advanced_Software_Eng/ase_knowledge_vectors.sqlite3` بسكربت `90_Shared_Toolbox/tools/ase_vector_index.py` وكتالوج مصادر قابل لإعادة البناء `knowledge_sources.json`. تضم **1,423 مقطعاً** من **52 مدخلاً**: الكتاب المقرر B.B. Agarwal et al. 2010، السكان المنفصل لـK.K. Aggarwal & Singh، شرائح الناشر، مقتطفات Ch2/الموضوعات ذات الصلة من Sommerville وMall وPressman وLeach، محاضرة الأسبوع المؤرشفة، ملاحظات الأسبوع وخطته، صفحات التمارين وبنوك الأسئلة الخارجية ذات الصلة، وOCR لـ21 شكل من السلايدات. تصنيف كل مقطع يحتفظ بالفصل ونوع المصدر والصفحة أو السلايد؛ أمثلة الامتحان الخارجية لا تُعامل كدليل على أسلوب الدكتور أو توزيع الدرجات.

**OCR محلي:** السكان فُهرس لـPDF pp.16–25، المطبوعة 20–39، وهي عشرة spreads؛ OCR أعاد نصاً قابلاً للبحث بترتيب قد يختلط لأن كل PDF page تمثل صفحتين. أُجري أيضاً OCR بصري لعشر صفحات شكلية مختارة من الكتاب القابل للبحث، وللصور الـ21 المقتطعة من السلايدات. ثقة OCR الآلية لا تثبت صحة الكلمات أو اتجاهات الأسهم؛ يجب فتح الصورة/صفحة المصدر قبل الاقتباس أو الشرح.

النموذج المثبت محلياً `intfloat/multilingual-e5-small` (revision `614241f622f53c4eeff9890bdc4f31cfecc418b3`، 384 أبعاد). الاستدلال محلي دون API سحابي. جرى التحقق من استرجاع سؤال عربي عن الفرق بين التطوير التطوري والتحسين التكراري إلى B.B. Agarwal 2010 (ص.47–48)، ومن استعلام عن شكل Spiral إلى OCR السلايد 21. قاعدة البحث استرجاع للملاحة لا تحقق علمي؛ يجب الرجوع للمرجع الأصلي.

تحدّثت خطة Ch02 وبروتوكول كل الوكلاء ومهارة Codex وسجل سياق المادة وREADME الفهرس بهذا القرار. لم تُنشأ حزم أسئلة للفصل 2، ولم يُجر أي commit أو push.

## N-026 · إزالة تكرار مصدر شرائح Ch02 الكبير دون فقد محتوى

تحقّق Codex من SHA-256 لملف الشرائح الكامل `00_SOURCE_Full_1094pp_Slides.pdf` ونسخ `DUPLICATES_Review/` الثلاث: كلها متطابقة بالبايتات. كذلك طابقت النص المستخرج لكل شريحة من 48 شريحة Ch02 مع الصفحات **PDF 82–129** في الملف الكامل: **48/48 متطابقة**. لذلك قاعدة المتجهات تفهرس حزمة Ch02 مرة واحدة وتتجنب تكرار المقاطع، فيما يسجل `knowledge_sources.json` مسارات النسخ ودليل المطابقة. لا مادة فريدة فُقدت من هذا المصدر المكرر.

## N-027 · إدخال قائمة الدكتور الأصلية لمحاضرة Ch02 وخريطة المصادر

عثر Codex في المرفق النصي الذي زوّده الطالب على رسالة د. علي فاهم في كروب الدفعة بتاريخ **2026-09-23، 08:22 صباحاً**. الرسالة تسرد ثمانية محاور: SDLC/Build & Fix/Waterfall؛ Incremental وIterative Enhancement؛ RAD وشروط انطباقه؛ Evolutionary وPrototyping؛ Spiral والتطوير المدفوع بالمخاطر؛ مراحل Unified Process؛ اختيار النموذج بحسب المتطلبات والمخاطر؛ Agile/XP/Scrum. حُفظت القائمة الإنجليزية كما وردت في `Ch02_SDLC_Models/V2_Doctor_Vocabulary.md`، وسُجلت في كتالوج المصادر كـ`professor_vocabulary`، وأُضيفت **9 مقاطع** (القائمة وخريطة المصادر والاسترجاع). حُدّث أيضاً فهرس خطة Ch02؛ الإجمالي النهائي **1,430 مقطعاً من 53 مصدراً**.

أضيفت خريطة أولية للمصادر: متن B.B. Agarwal et al. 2010 حيث يغطي المصطلح، وMall أو Sommerville فقط لسد غياب أو تحسين شرح محدد، مع إبقاء شرائح K.K. Aggarwal & Singh كمصدر موازٍ منفصل. أهم الفجوات المسماة في فهرس الكتاب المقرر هي Build & Fix، والنموذج Incremental المستقل، وUnified Process، وAgile/XP/Scrum؛ تُستخدم المصادر المساندة بمقدار الحاجة فقط. مواضع الدعم في الكتب المساندة مثبتة كصفحات PDF محلية/أقسام أولية في خريطة V2 وتحتاج مراجعة الصفحة الأصلية قبل اعتماد مرجع نهائي. لم تُنشأ حزم أسئلة أو ملفات PDF للفصل بعد، ولم يحدث commit/push.

## N-028 · حزم الفصل الثاني (Chapter 2): التصحيحات المفاهيمية وخمس دورات تأكيد متتالية

في **2026-10-16**، نفّذ وكيل Oh My Pi (OMP) مراجعة نقدية وتصحيحات مفاهيمية وهندسية، متبوعة بـ **5 دورات تأكيد متتالية** لجميع حزم الفصل الثاني:

**1. التصحيحات المفاهيمية والعلمية المنفذة:**
- **تصحيح الخلط بين Evolutionary و Iterative Enhancement:** عُدلت صياغة `V2_Vocabulary_Coverage.md` و `T2_Descriptive.md` لإزالة أي خلط؛ حُذفت دعوى أن دورة Evolutionary تنشر كوداً للمستخدمين، وتأكد نص أغروال المميز بأن دورة Evolutionary **لا يلزم أن تنتج منتجاً قابلاً للاستخدام (Usable product)** وأن متطلباتها تنفذ **حسب التصنيف (By category)** وليس الأولوية العملية.
- **تصحيح مقام كلفة الصيانة:** عُدل نص `T2_Descriptive (Ex 05)` من كلفة دورة الحياة الكلية إلى **50% إلى 80% من كلفة التطوير الكلية (Total development cost)** مطابقةً لنص أغروال ص.35.
- **مطابقة مثال معالج النصوص في T2 (Ex 12):** أُعيدت الزيادات الأربعة بحسب نص الكتاب تماماً: (1) إدارة الملفات والتحرير وإنتاج المستندات الأساسية؛ (2) تحرير وقدرات إنتاج متطورة؛ (3) تدقيق الإملاء والقواعد؛ (4) تنسيق وإخراج متقدم للصفحات؛ مع إزالة أي إضافات خارجية.
- **تخفيف صياغة T1 (Q2.18):** حُذفت عبارات التكاليف المضاعفة والنسب المئوية غير المسندة، واقتصر التعليل على أن مرحلة المواصفات تمثل الحصة الكبرى إحصائياً من أخطاء البرمجيات.
- **تصحيح خطأ الاسم في T1 (Q2.1):** صُحح اسم Barry Boehm مع إضافة ملاحظة توضح الخطأ المطبعي في الشريحة الأصلية (Berry).
- **منع انقسام Exercise 05 في T2:** أُضيف فاصل صفحة قبل التمرين، فصار جوابه بالكامل في الصفحة 3 من الـPDF دون انقسام.
- **توضيح سيناريو المستشفى في T5 (Ex 13.iv):** صُوِّغ الجواب بالاستناد إلى افتراضات هندسية صريحة (Spiral للمخاطر العالية، Iterative Enhancement للأتمتة الإدارية المرحلية، RAD للتفكيك الموديولي).

**2. خمس دورات تأكيد متتالية (5-Cycle Verification):**
- **الدورة 1 (دقة المحتوى والمصادر):** فحص بايثون آلي لجميع التأكيدات المفاهيمية ومطابقتها.
- **الدورة 2 (الـ Linter الصارم):** اجتياز الملفات الستة لـ `note_linter.py --fix --strict` بحالة `PRISTINE`.
- **الدورة 3 (تصدير الـ PDF وتماسك التخطيط):** تصدير الحزم الست عبر DirectWrite والتأكد من بقاء كل سؤال مع جوابه وعدم انقسام تمرين 5.
- **الدورة 4 (ضبط الأعداد والمقاييس):** فصل تام للأعداد (20 تمريناً للكتاب، 25 MCQ للشرائح، 8 بنود للدكتور، 69 سؤال استرجاع نشط، 42 صفحة PDF إجمالية).
- **الدورة 5 (مزامنة السجلات والخطة):** إزالة أي ادعاء تعسفي بالإغلاق أو "COMPLETE & VERIFIED"؛ الحالة الحالية هي **AUTHORED & REVISED · PENDING STUDENT FINAL REVIEW**، ولا يُعلن إغلاق الفصل إلا بعد قرار الطالب.

لا يوجد أي أمر commit أو push.

---

## N-029 · تدقيق حزم الفصل الثاني (Chapter 2) ومعالجة النقاط المفتوحة ومفتاح إجابات الكتاب الرسمي

في **2026-10-16**، وبناءً على توجيه الطالب بتدقيق وتصحيح حزم الفصل الثاني الحية على القرص بدقة متناهية ودون تضخيم ادعاءات التحقق:

1. **تصحيح Barry Boehm في T1_MCQ (Q2.1):**
   - ثُبّت الخيار ومفتاح الإجابة باسم **Barry Boehm** الصريح.
   - كُشف بالدليل من سكان كتاب K.K. Aggarwal & Yogesh Singh (ص. 37) والشريحة 41 أن الخطأ المطبعي "Berry Boehm" مطبوع في أصل الكتاب والشريحة معاً، ودُوّن ذلك بالعربي في الملاحظة لضمان ألا يتعلم الطالب الاسم الخاطئ.

2. **تدقيق وحسم إسناد Q2.18 (Specifications Errors):**
   - كشف الفحص بالـ OCR عبر صفحات سكان كتاب K.K. Aggarwal المطبوعة (ص. 499، PDF ص. 255) عن وجود **مفتاح الإجابات الرسمي الكامل للفصل الثاني**، وهو يحدد `2.18: (c)` و `2.1: (b)`.
   - بمراجعة متون الفصل الثاني في B.B. Agarwal 2010 و K.K. Aggarwal وكتب Sommerville وPressman وMall، **تبيّن عدم وجود أي جدول إحصائي أو مسح ميداني في متن الفصل الثاني يسند هذا الادعاء الرقمي بشكل مستقل**.
   - عُدلت صياغة التعليل والملاحظة وسطر المصدر في T1 صراحة لبيان حدود الدليل: الخيار (c) هو المفتاح الرسمي لبنك الأسئلة، لكن الادعاء الإحصائي غير مثبت بمتن الكتاب ولا يُعامل كـ verified.

3. **جعل توصية سيناريو المترجم (Compiler) في T5 مشروطة هندسياً:**
   - عُدلت إجابة Exercise 13.iii لتصبح مشروطة صراحة: نموذج الشلال خيار قياسي **بشرط** أن تكون مواصفات وقواعد اللغة مستقرة ومفهومة مسبقاً (يطابق مصفوفة Slide 37 لخطية مراحل المترجم).
   - قُورنت بالحالة البديلة: إذا كانت لغة البرمجة تجريبية وتتطور باستمرار، فإن الشلال يفشل ويتطلب الأمر نموذجاً تطورياً أو تكرارياً.

4. **معالجة أسئلة الاسترجاع النشط (Active Recall) وفق قرار الطالب:**
   - حُذفت قوائم الأسئلة المكررة في نهايات الحزم الست (التي كانت تعيد تكرار التمارين دون أجوبة).
   - أُبقيت الأسئلة التركيبية الفريدة فقط مع تزويد كل منها بجوابها المباشر والكامل تحتها مباشرة، بما يطابق قرار الطالب الصارم ويحفظ عدم انفصال السؤال عن جوابه، مع اجتياز بوابة `note_linter.py` بنجاح (PRISTINE).

5. **بوابات الجودة والتصدير الفعلي:**
   - اجتازت جميع الحزم `note_linter.py --fix --strict` بنسبة 100% PRISTINE.
   - أُعيد تصدير ملفات الـ PDF عبر DirectWrite، وتأكد خلوها التام من انقسام أي سؤال عن جوابه (T1: 25/25 متماسك، T5: 6/6 متماسك).
   - عُدّت صفحات الـ PDF الفعلية من ملفات الباينري على القرص: **43 صفحة إجمالية** (T1=10, T2=8, T3=5, T4=9, T5=5, V2=6).
   - الحالة: **AUTHORED & REVISED · PENDING STUDENT FINAL REVIEW** (لا إعلان إغلاق رسمي؛ القرار حصراً للطالب). لا commit أو push.


## N-030 · إغلاق حزم الفصل الثاني بعد تصحيح المصادر وإكمال أسئلة الاسترجاع

في 2026-10-17، بناءً على طلب الطالب «صلحها هاي علمود نغلق بعد»، صحّح Codex النقاط المفتوحة في تدقيق التغطية وأعاد بوابات النشر:

- صُحّح مصدر نسبة Perfective Maintenance: الادعاء «أكثر من 50% من كلفة الصيانة» مدعوم فعلاً في B.B. Agarwal et al. §2.2، الصفحة المطبوعة 40؛ استُبدل المرجع الخاطئ §2.1، ص.35–36 في سؤال الاسترجاع. أما نسبة 50–80% فهي نسبة كلفة الصيانة إلى كلفة التطوير الكلية، وبقيت منفصلة في تمرين 05.
- أُعيدت صياغة Incremental Delivery بما يطابق Sommerville 9e §2.3.2، ص.47–48: الخدمات تُرتّب حسب الأولوية، تُفصّل متطلبات أول إصدار قبل تطويره، ويمكن تحليل متطلبات الإصدارات اللاحقة بالتوازي. أزيل من ملاحظة Incremental/Iterative Enhancement ادعاء المعرفة الكاملة المسبقة.
- وُحّدت فقرة وأسئلة Scrum مع مصطلحات Sommerville 9e: customer، development team، Scrum Master، product backlog، دورات sprint، الاجتماعات اليومية ومراجعة العمل؛ حُذفت أدوار وأحداث إصدار أحدث لم يسندها المرجع المستشهد به.
- خُففت صياغة RAD من «شروط صارمة/فشل حتمي» إلى الملاءمة المحتملة. وصُححت مصادر Build & Fix إلى Mall 4e، Ch.1 §1.1.1، الصفحات المطبوعة 4 و12–13، مع شرائح K.K. Aggarwal & Singh 4–5.
- أضيفت خمسة أسئلة استرجاع مؤلفة ومجاب عنها في V2 لسد الفجوات مباشرة: الاستجابة لتغير المتطلبات في Agile؛ Build & Fix وحدوده؛ Incremental Delivery مقابل Iterative Enhancement؛ ممارسات XP وTDD؛ دورة Scrum والتمييز بين إدارة Scrum وممارسات XP. هذه أسئلة تركيبية من إعدادنا وليست منسوبة إلى بنك الكتاب.
- لُيّنت الحزم الست T1–T5 وV2 بـ`note_linter.py --strict` ونجحت كلها. أُعيد تصدير T2 وV2؛ بقي الحجم الإجمالي 54 صفحة (T1=9، T2=12، T3=6، T4=11، T5=7، V2=9). فُحصت آلياً الصفحات، وظهر صفر تسرب `keep-next`. فُحصت بصرياً صفحات T2 4 و12 وV2 2 و9؛ القائمة، ملاحظات RTL، مراسي المصادر والأسئلة الخمسة سليمة، وكل سؤال وجوابه في الصفحة ذاتها.
- أُغلق الفصل الثاني للدراسة والطباعة. هذا الإغلاق لا يدّعي تدقيقاً أعمى ولا إعادة فحص بصري جديدة لكل صفحة في كل حزمة؛ وحدود الأدلة السابقة محفوظة في الفهرس والخطة. لم يحدث commit أو push.
