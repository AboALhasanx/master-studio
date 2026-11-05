# Master Studio — Curated Project Memory

> **Laws + pointers only, no live state.** Details → `DETAILS.md` §1–§14. Academic state →
> `00_STUDIO_HUB/ACTIVE_STATE.md`. Quiz-bank counts/versions → generated
> `00_STUDIO_HUB/QUIZ_BANK_STATE.md` — **never hand-copy a number out of it.**

## 0 · Read first
`ACTIVE_STATE.md` · `QUIZ_BANK_STATE.md` (any bank/version number) ·
`STUDENT_NOTES_LOG.md` (**N-001…N-045**, append-only; read before any chapter pack) ·
`guides/ASE_QUESTION_PACK_PROTOCOL.md` · `guides/QUIZ_BANK_PROTOCOL.md` + `PORTAL_PUBLISH.md` ·
`<chapter>/ChNN_BUILD_PLAN.md` · `Ch01_Introduction/_VERIFICATION_PROTOCOL.md` · `DETAILS.md`.
Bank work: `AGENT_HANDOFF_QUIZ_BANKS.md` (laws) → `QUIZ_PUBLISH_RUNBOOK.md` (sequence) →
`QUIZ_BANK_STATE.md` (state), in that order.

## A · Repo / env / gates
- `AboALhasanx/master-studio` PUBLIC, `master` = chatbot bridge. Never privatize or break raw-file readability / Pages. `.workbuddy-ai/memory/` is public → keep clean.
- Vault = `C:\Users\gokoq\Master-Studio` (off Drive since 2026-09-23). `G:\My Drive\Master-Studio` STALE; `AGENTS.md` still says `G:/`.
- Push: sandbox OFF; `APPDATA="C:\Users\gokoq\AppData\Roaming"`, `HOME="/c/Users/gokoq"`; `gh auth setup-git; git push origin master`.
- Python: `CODEBUDDY_SAFE_DELETE_ENABLED=0`, system Python312, `-X utf8`. `curl` is proxied → use Python.
- **Note → PDF gate, all three:** `note_linter.py --fix --strict` exit 0 → `pdf_exporter.py -t study_pack` → **render with PyMuPDF and look at every page**. Export ≠ visual verification.
- `diagram_forge.py --width 1080 --scale 2`; run `page.get_images()` per page (a slide can be an image with an empty text layer). Page counts from the real PDF, never from plan/index (N-040).
- Browser: **Thorium** (`...\AppData\Local\Thorium\Application\thorium.exe`) via `playwright-core`; beats bot detection. Chain open+eval in ONE bash call. Throwaway profile only — real one locked (EBUSY).

## B · Student rules (STANDING)
Zero-CLI. Recap at every transition; end each block "هاي لو اكو بعد؟". Correct bluntly ("هاي غلط"). Arabic to him / formal academic English for anything leaving the vault. Go DEEP; never compress an already-condensed source without asking. Conflicting instructions → STOP and ask ("قرار مصيري"). Verify, never fabricate; tag guesses `[Foundational Knowledge / Standard Concept]`. Announce before deleting. Never invent deadlines.

## C · ASE authoring law (N-008→N-045; **full text `DETAILS.md` §12, read before writing**)
EN stem/options/answer; brief AR **outside** the answer (N-020). **Bold** = sourced · plain = ours · **italic banned**. Zero essay framing — book only in the source line (`**Aggarwal, §1.2.1, p.4.**`, `printed` banned). **Direct-answer (N-012):** one source sentence answers → quote whole, contiguous, no stitching. Short answers, no filler. **Bold-ratio (N-011)** = diagnostic for invention. **Scope = doctor's vocabulary list (N-025):** define / mechanism / distinguish look-alikes, no sweep. **Calcs (N-032):** Given→Required→Model→Equation→Substitution→Result→Check + independent source, all English; never solve before reading the source pages. **Diagrams extracted, never redrawn** (N-037/39). **Titles (N-045):** blue eyebrow + black title, no dup H1/H2; stems left-aligned; "centred" = balanced block (N-042→43). **`note_linter.py` DEFECT:** pattern C corrupts bold at the end of an italic quote.

## D · Exporter / RTL (**full text `DETAILS.md` §9, render-verified**)
**NO ASCII CODE in ملازم** (2026-10-13, twice): zero fenced blocks — derivations → plain paragraphs, step lists/trees → two-column text tables. **NO TABLES in student packs** (2026-10-16 «كجدول وبس أشوفها شكل بدائي»): answer → callout card, question → bold stem + one options line with `·`. **Callouts:** every line prefixed `>`, blank `>` between paragraphs; `attr_list` dead inside bodies. **Table parsing:** blank line before **and** after, separator count = header count, never inside a list; detector = literal `|` in the PDF text layer; unclosed backticks swallow the row. **RTL (N-009):** `dir="rtl"` at ≥25 % Arabic and on callout title/body; **never** `flex-direction: row-reverse` on `.callout-title[dir="rtl"]` (double flip). **Q/A cohesion (N-003/15):** `{: .keep-next }` → `break-after: avoid`; `apply_keep_next(html)`. Frontmatter: real `title:`/`course:`/`subtitle:`. Engine fixes 10-28/11-02: Law 10 list-marker clipping (SOP), arrow-in-attribute, `keep_small_tables_together()`, placeholder-aware direction tagging.

## E · Discipline
Never cite a commit hash before it is on `origin/master`. Test counts only via `--collect-only`. `gh issue close --comment "$(cat f)"`. Telegram gate: read `MessageEntityTextUrl`. **System 1 drafts; a blind verifier decides** (SUPPORTED / PARTIAL / NOT FOUND / CONTRADICTED + quoted sentence + page; every round states its page range).

## F · Subsystems (internals `DETAILS.md` §7)
- **Telegram** `00_STUDIO_HUB/telegram/` — bot `cs_mscbot` + spare human `8404964768`; **solutions decks via the human account, never the bot**; D14 never writes `MEMORY.md`.
- **MCSQuiz portal** `C:\Users\gokoq\mcq-portal` (Vercel `mcq-portal-jade.vercel.app`); banks `01_Semester_1/*/07_Quizzes_&_Anki/`; `portal_content.py status|sync|pull`. Skill `00_STUDIO_HUB/skills/mcq-portal-pipeline/`, exposed by a **directory junction** at `~/.workbuddy-ai/skills/mcq-portal-pipeline` — never copy. Gates `DETAILS.md` §11.
- **STATE-NUMBER LAW (2026-11-04):** counts/versions live **only** in generated `00_STUDIO_HUB/QUIZ_BANK_STATE.md` (`90_Shared_Toolbox/tools/quiz_bank_state.py`; `--check` exits 1 on drift). No hand-written document carries a live number. State tables always carry a **subject column** — a bare `ChNN` row mixed Cyber with Data Mining. Count banks with `*.json`, not `Quiz_ChNN_*` (four subjects use other names).
- **Legacy live quiz** only for a real sitting; "يلا كوز" → portal. Flask `91_Dashboard/app.py` + `_wait_quiz_result.py`, then kill both.
- **Mirror translation** (gitignored sandbox): facsimile → literal Arabic → comprehension; unit = TOPIC. **Phone sync** `phone_sync.py` v2 — `adb push --sync`, **exit 1 = real failure**. **ASE indexes** `00_STUDIO_HUB/indexes/04_Advanced_Software_Eng/` — vector + FTS5; retrieval is navigation, not verification.

## G · Grading (`DETAILS.md` §8)
تعليمات 27/1982 Art.24(1): **floor 60, not 50** (مقبول 60–69 / راسب ≤59); year average ≥70 or re-sit; **69 ⇒ dismissal**. Split 30 % سعي / 70 % نهائي. Levers = the two 3-credit subjects (25 %). Canonical `ACADEMIC_REGULATIONS.md` §3.4. `SEM1_FOCUS_AND_MARKS_PLAN.md` roster is WRONG.

## H · ASE source identity — CLOSED, do not re-hunt
**Full record `DETAILS.md` §13.** Origin = K.K. Aggarwal & Singh, *Software Engineering*, 3rd ed.;
`CS_Agarwal_..._2010.pdf` is a different book; `By_Chapter` = publisher slides. One file to hand
him: `02_Raw_Materials/Aggarwal_SE_3rdEd_COMPLETE/Aggarwal_SE_3rdEd_COMPLETE_Ch1-10_OCR.pdf`
(452 pp, OCR, bookmarked). Printed answer key pp.497–500 absent from every scan. §13 has the
Ch1–Ch10 page map and OCR toolchain.

## I · Chapter packs
`03_Study_Notes/ChNN_<Name>/` = `ChNN_BUILD_PLAN.md` (AR, internal) + `.md`+`.pdf` per type T1…T7 (+ `V`/`00_INDEX`). Supersedes `08_DeepStudy_ChNN/` for **new** chapters; Ch04/Ch05 sandboxes stay. English only; `pdf_exporter.py <f>.md -t study_pack --lang en`. Tier1 = Remember/Understand; Tier2 = Apply/Analyze/Evaluate/Create; never mix. Tier2 depth is the differentiator.

## K · AI course CS605 (Dr. Saif Al-Saidi)
Swarm Intelligence 2026-10-20; next = student-led Supervised ML presentation (KNN, SVM, Naive Bayes). Banks/origin `DETAILS.md` §10. AI W01/W02/W03 study packs delivered 2026-10-28; recall-sheet proofs held for student approval.

## L · Faculty roster — full `DETAILS.md` §14
College = **College of Computer Science & IT, University of Wasit**. Read
`FACULTY_PRACTICAL_INTEL.md` + `FACULTY_FORENSIC_AUDIT.md`; `01_Supervisor_Intelligence.md`
is **agent-inferred, unverified** — never cite as fact. Two laws to keep visible: faculty are
indexed **only** under Latin transliteration (Arabic-only search = false negatives); **RTL PDF
law** — mixed Arabic + Latin in one paragraph gets reversed, so each Latin name/title gets its
own paragraph. §14 has OpenAlex numbers, patent 7858, the IEEE Notice of Violation, working
sources and `alaidi.net` (Abdul Hadi's own Soft Computing syllabus).

## M · English exam scope (2026-11-04)
English is **not** an MCQ-everything subject. Exam tests: grammar · vocabulary ·
collocations · matching · multiple choice. Exam does **NOT** test: listening, long reading
passages, writing, speaking, verbatim memorization. So: never turn listening/reading/writing/
speaking material into question banks; retrieval/quiz work filters to the exam scope
(`english_vector_memory.py search ... --exam`, 62 of 183 chunks). The course material still
covers all four skills — the exam does not.

## N · Quiz bank shape (2026-11-05) — the numbers are not sacred
**One bank per instructor vocabulary item; 8–16 questions; never below 8.** The count must be
whatever the material honestly supports — no fixed target, no "12 is the standard". The old
"one bank per topic" split is superseded wherever the instructor's own scope ledger exists.
- **Scope source of truth = the vector index**, `00_STUDIO_HUB/indexes/<subject>/…sqlite3`,
  `chunks` table (`chapter`, `source_title`, `content`). The *vocabulary* chunks are the
  instructor's scope ledger; diff those terms against the banks' text and every uncovered term
  is a bank to write. The index is a **scope-gap checker, not a question source**.
  ASE: `ase_knowledge_vectors.sqlite3`, 4140 chunks; Ch03 299, Ch06/07/08 ledgers readable.
- **Official MCQs are the spine** (T1 pack per chapter); the T2/T3 prose packs fill the gaps.
- **Numeric and formula options are rewritten as words** — digits and LaTeX are banned in options.
- **The builder assumes the CORRECT option is FIRST** and rotates it into place. Writing options
  in textbook order ships **wrong answers while every gate passes** (gates check length, never
  truth). Always: explicit `CORRECT` map + `put_correct_first()` before `L.build(...)`, then
  spot-check the built JSON against the printed key.
- **Never run the option rebalancer bank-wide** — it broke 31 of 49 DM banks in one run.
  Restrict it to the new questions; and pad the *correct* option when it is the shortest,
  otherwise the band never closes.
- **META (no self-reference to the handout) false-positives**: `the module`, `the source`,
  `the chapter`, `the handout`, Arabic `المصدر`, `المذكورة`. Reword, do not disable.
- Subject floor status 2026-11-05: Cyber 711 · English 200 · DM 531 · **ASE 407 (47 banks)** ·
  SC 158 — all banks ≥ 8. AI 4×5 left below the floor on purpose.
