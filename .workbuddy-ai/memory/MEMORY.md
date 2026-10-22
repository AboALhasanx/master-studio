# Master Studio — Curated Project Memory

> **Laws + pointers only.** Numbers, source maps, exporter detail, subsystem internals, grading detail, and the Cyber quiz-bank gate laws live in `DETAILS.md`. Live state lives in `00_STUDIO_HUB/ACTIVE_STATE.md`, never here.

## 0 · Read these first (canonical, always fresher than this file)
1. `00_STUDIO_HUB/ACTIVE_STATE.md` — semester / week / subject / todo / next focus.
2. `00_STUDIO_HUB/STUDENT_NOTES_LOG.md` — **N-001 … N-045**, append-only, his verbatim remarks + decision + scope. Every rule change lives there; read before touching a chapter pack.
3. `00_STUDIO_HUB/guides/ASE_QUESTION_PACK_PROTOCOL.md` — cross-agent protocol for ASE packs (N-021).
4. `00_STUDIO_HUB/guides/QUIZ_BANK_PROTOCOL.md` + `PORTAL_PUBLISH.md` — MCSQuiz bank authoring and publishing.
5. `<chapter>/ChNN_BUILD_PLAN.md` — per-chapter contract: scope, question→type map, closure gates.
6. `Ch01_Introduction/_VERIFICATION_PROTOCOL.md` — blind-verification method (N-010).
7. `.workbuddy-ai/memory/DETAILS.md` — frozen numbers, source maps, exporter detail, subsystem internals, grading detail, quiz gate laws (§11).

## A · Repo, env, delivery gate
- **Repo** `AboALhasanx/master-studio`, PUBLIC, branch `master` = the chatbot bridge. Never privatize, never break raw-file readability or GitHub Pages. `.workbuddy-ai/memory/` is public → keep it clean.
- **Vault = `C:\Users\gokoq\Master-Studio`** (off Google Drive since 2026-09-23). `G:\My Drive\Master-Studio` is STALE; `AGENTS.md` still points at `G:/` — out of date.
- **Push:** sandbox OFF; export `APPDATA="C:\Users\gokoq\AppData\Roaming"`, `HOME="/c/Users/gokoq"`; then `gh auth setup-git; git push origin master`.
- **pytest:** prefix `CODEBUDDY_SAFE_DELETE_ENABLED=0`, use system `Python312`. `curl` is proxied → use Python. Arabic console output → `-X utf8`.
- **Delivery gate (note → PDF), all three mandatory:** ① `note_linter.py "<note>.md" --fix --strict` exits 0 ② `pdf_exporter.py "<note>.md" -t study_pack` ③ **render with PyMuPDF and actually look at every page**. A successful export ≠ visual verification.
- **Diagrams:** `diagram_forge.py --width 1080 --scale 2`. Before judging a deck run `page.get_images()` per page — a slide can be an embedded image with an empty text layer.
- **Page counts:** count from the actual PDF, never from the plan/index (N-040: index numbers were 5 pp stale).

## B · Student rules (STANDING)
Zero-CLI — I run everything, he never sees a command. Recap at every transition; end each block with "هاي لو اكو بعد؟". Correct bluntly ("هاي غلط"). Arabic to him / formal academic English for anything leaving the vault. Go DEEP; never compress an already-condensed source without asking. Conflicting instructions → STOP and ask ("قرار مصيري"). Verify, never fabricate; tag guesses `[Foundational Knowledge / Standard Concept]`. Announce before deleting anything. Never invent deadlines.

## C · ASE authoring law (N-008 → N-045) — full text in `DETAILS.md` §12
**The law in one paragraph.** EN = stem/options/answer; brief AR (traps, warnings, concept notes) sits **outside** the English answer, never inside (N-020). **Bold** = source-grounded words · **plain** = our wording or a short label · **italic banned outright**. Answers carry **zero essay framing** — the book is named only in the source line (`**Aggarwal, §1.2.1, p.4.**`; the word `printed` is banned), the Arabic note cards and the frontmatter. **Direct-answer rule (N-012):** if one source sentence answers the question, quote it **whole and contiguous** — never halve it and stitch with connective prose; zero meta-discourse. **Answers are short** — answer + justify, no repetition, no exam-coaching filler. **Bold-ratio diagnostic (N-011):** low ratio = mostly my prose = where invention hides; a diagnostic, not a target — the job is catching **zero**. **Scope = the doctor's vocabulary list (N-025):** define the term, explain its mechanism, distinguish it from look-alikes — **no encyclopaedic sweep**. **Calculations (N-032):** Given → Required → Model → Equation → Substitution → Result → Check → independent source, all English; **never solve before reading the source pages**. **Fixed diagrams are extracted, never redrawn** (N-037/N-039); coverage-mapping tables are **print-hidden**. **Pack titles (N-045):** small blue chapter eyebrow + large black title, no duplicate H1/H2, no extra rule; stems left-aligned with natural wrap, "centred" = balanced block, not centred text (N-042→N-043). **`note_linter.py` DEFECT:** pattern C corrupts bold nested at the end of an italic quote — never end an italic quoted phrase with `**bold**`.

## D · Exporter / RTL pitfalls — essentials (full text in `DETAILS.md` §9)
**NO ASCII CODE in ملازم** (2026-10-13, his explicit order, said twice): zero fenced code blocks in any study note — calc/derivation → plain paragraphs (one line each, blank line between); step lists & folder trees → two-column text tables. **NO TABLES in student-facing packs** (2026-10-16: «كجدول وبس أشوفها شكل بدائي») — answer → callout card; question → bold stem line + one options line separated by `·`; comparison → bold-lead-in paragraphs. **Callouts:** every body line prefixed `>`, **blank `>` between paragraphs or they merge into a run-on**; `attr_list` does **not** work inside callout bodies. **TABLE PARSING LAW** (32 broken tables in Ch04): a table is skipped if it touches the neighbouring line without a blank line, if separator cell count ≠ header count, or if it sits inside a list item — blank line before **and** after · equal counts · never in a list; detector = literal `|` in the PDF text layer; unclosed backticks swallow the row. **RTL is mandatory, never inherited (N-009):** `dir="rtl"` is set by the exporter for Arabic-dominant blocks (≥25 % Arabic letters) and for every callout title/body; **never add `flex-direction: row-reverse`** to `.callout-title[dir="rtl"]` — it flips twice and the icon returns to the left. **Q/A cohesion (N-003/N-015):** `{: .keep-next }` → `break-after: avoid` so stem + answer jump pages whole (page-foot whitespace is acceptable to him); `attr_list` is flaky on letter stems → `apply_keep_next(html)` consumes leftovers. **Frontmatter** always carries a real `title:` + `course:` + `subtitle:` — never the exporter default.

## E · Discipline
Never cite a commit hash before it is on `origin/master`. Test counts only true via `--collect-only`. `gh issue close` → `--comment "$(cat f)"`. Telegram live gate: read `MessageEntityTextUrl`. Independent verification is standing: **System 1 drafts; a blind verifier decides** (atomic claims → SUPPORTED / PARTIAL / NOT FOUND / CONTRADICTED, quoted sentence + page read off the image; every round states its page range — a `NOT FOUND` can mean "outside the pages reviewed").

## F · Subsystems — one line each (internals in `DETAILS.md` §7)
- **Telegram** `00_STUDIO_HUB/telegram/` — bot `cs_mscbot` + spare human account `8404964768`. **Solutions decks go out via the spare/human account, never the bot.** D14 never writes `MEMORY.md`.
- **MCSQuiz portal** app at `C:\Users\gokoq\mcq-portal` (Vercel `mcq-portal-jade.vercel.app`); banks in vault `01_Semester_1/*/07_Quizzes_&_Anki/`; `portal_content.py status|sync|pull`. Authoring skill = `00_STUDIO_HUB/skills/mcq-portal-pipeline/` (canonical), exposed to WorkBuddy by a **directory junction** at `~/.workbuddy-ai/skills/mcq-portal-pipeline` (2026-10-22) — never copy it, the vault file is the only source. **Gate laws: `DETAILS.md` §11.**
- **Quiz (live, legacy):** only for an actual sitting (QR, score read back). "يلا كوز" defaults to the **portal**, not a server. Flask `91_Dashboard/app.py` + `_wait_quiz_result.py`, then kill both; trust `curl /api/health`. Skill `master-studio-quiz-session` §0 has the routing table.
- **Mirror translation** (gitignored sandbox): facsimile → literal Arabic → comprehension. Unit = TOPIC. Skill `master-studio-mirror-translation`.
- **Phone sync** `phone_sync.py` v2 — `adb push --sync`, **exit 1 = real failure**.
- **ASE indexes** `00_STUDIO_HUB/indexes/04_Advanced_Software_Eng/` — local vector DB + FTS5. **Retrieval is navigation, not verification.**

## G · Grading law — essentials (detail in `DETAILS.md` §8)
**تعليمات 27/1982**, Art.24(1): **floor 60, not 50** (مقبول 60–69 / راسب ≤59). Year average ≥70 or re-sit; **69 ⇒ dismissal**. His split = 30 % سعي / 70 % نهائي. **Levers = the two 3-credit subjects (25 % combined).** Canonical `00_STUDIO_HUB/ACADEMIC_REGULATIONS.md` §3.4. `SEM1_FOCUS_AND_MARKS_PLAN.md` roster is WRONG.

## H · ASE source identity — essentials (map in `DETAILS.md` §1)
Question origin = **K.K. Aggarwal & Singh, *Software Engineering*, 3rd ed.** The book itself = the **scan** `AliFahim_Software_Engineering.pdf` (256 pp, 2-up, **no text layer**, drifting page offset → render + vision). `CS_Agarwal_..._2010.pdf` is a **different book** (B. B. Agarwal et al.) — never the citation source. The `By_Chapter` PDFs and `00_SOURCE_Full_1094pp_Slides.pdf` are **publisher slides, not prose**. **The official answer key exists** (printed pp.497–500; Ch1 key p.498).

## I · Chapter packs — shape (status lives in ACTIVE_STATE + each `ChNN_BUILD_PLAN.md`, not here)
`03_Study_Notes/ChNN_<Name>/` = `ChNN_BUILD_PLAN.md` (Arabic, internal) + one `.md`+`.pdf` per type `T1…T7` (+ `V`/`00_INDEX`). Supersedes `08_DeepStudy_ChNN/` for **new** chapters; Ch04/Ch05 sandboxes stay as-is. **Pack language = English only.** Export `pdf_exporter.py <f>.md -t study_pack --lang en`.
**Tier law:** Tier1 = official style (Remember/Understand); Tier2 = Apply/Analyze/Evaluate/Create; never mix in one file. Dr. Ali Fahim delivers Aggarwal slides at surface depth → **Tier2 depth is the differentiator**. Per-chapter page counts and frozen numbers: `DETAILS.md` §3–§5.

## K · AI course (CS605, Dr. Saif Al-Saidi) — ACTIVE
Swarm Intelligence delivered 2026-10-20; next = student-led presentation on Supervised ML (KNN, SVM, Naive Bayes). Banks and lecture origin in `DETAILS.md` §10.
