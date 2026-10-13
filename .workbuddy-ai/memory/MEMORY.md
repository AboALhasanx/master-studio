# Master Studio — Curated Project Memory

## A. Repo, env, delivery gate
- **Repo** `AboALhasanx/master-studio` PUBLIC, branch `master` = chatbot bridge. Never privatize / break raw-file readability / GitHub Pages. `.workbuddy-ai/memory/` is public → keep clean.
- **Push:** sandbox OFF, APPDATA must be exported: `export APPDATA="C:\\Users\\gokoq\\AppData\\Roaming"; export HOME="/c/Users/gokoq"; cd "C:/Users/gokoq/Master-Studio"; gh auth setup-git; git push origin master`.
- **Vault** = `C:\Users\gokoq\Master-Studio` (off Google Drive since 2026-09-23; `G:\My Drive\Master-Studio` is STALE — Drive `desktop.ini` corrupted `.git/`).
- **pytest:** prefix `CODEBUDDY_SAFE_DELETE_ENABLED=0`; use system `Python312`. `curl` is proxied → use Python. Arabic output → `-X utf8`.
- **Delivery gate (note→PDF):** ① `note_linter.py "<note>.md" --fix --strict` (must exit 0) ② `pdf_exporter.py "<note>.md" -t study_pack` ③ render with PyMuPDF and LOOK at it.
- **Diagrams:** `diagram_forge.py --width 1080 --scale 2` (SVG→PNG). ALWAYS `page.get_images()` per page before judging a deck — a slide can be an embedded image with an empty text layer.

## B. Student rules (STANDING)
Zero-CLI (I run everything). Recap at every transition; end each block with "is that it or more?". Correct bluntly ("هاي غلط"). Arabic to him / formal academic English for anything leaving the vault. Go DEEP, never compress an already-condensed source without asking. Conflicting instructions → STOP and ask ("قرار مصيري"). Verify, never fabricate; tag guesses `[Foundational Knowledge / Standard Concept]`. Announce before deleting anything. Never invent deadlines.

## C. Authoring + RTL pitfalls
- YAML frontmatter with a REAL title (`title: ملزمة الويك N — <topic>` + `course:` + `subtitle:`); never the exporter default title.
- Content-type label per section; **EN lists SEPARATE from Arabic**; verbatim label INSIDE `>` block; "صفحة صفحة" = ① verbatim ② literal translation ③ my understanding.
- **RTL pitfalls (check every render):** ordered lists scramble → use `| # | … |` table; consecutive bold Q/A lines merge → `| السؤال | الجواب |` table or blank line; `inline code` containing `_` or `/` reverses in Arabic → name the file in prose; trailing `(ص 103)` jumps to line start → drop it; a standalone Latin paragraph between two RTL blocks flips even when bold → safe forms are a Latin `####` heading, a table, or a blockquote.
- Image-heavy slides: composite 4–6 pp/sheet at 150–200 DPI; zoom 380–400 DPI on digits/equations.

## D. Discipline
Never cite a commit hash before it is on `origin/master`. Test counts only true via `--collect-only`. `gh issue close` → `--comment "$(cat f)"`. Telegram live gate: read `MessageEntityTextUrl`.

## E. Subsystems
- **Telegram** (committed `edb503f`): D14 owns `00_STUDIO_HUB/telegram/`, reads memory, never writes `MEMORY.md`; D15 = ONE bounded session, fail-closed, `update_id` persisted; D16 admin verbs → owner approval. Bot `cs_mscbot`. Contract `proposals/TELEGRAM_INTERACTIVE_ARCHITECTURE.md`.
- **Quiz (LIVE):** "يلا" → Flask (`start-quiz-server.bat`) + QR (`show-quiz-qr.bat <Sub> <Quiz>`) + `_wait_quiz_result.py`; kill both; trust `curl /api/health`. Skill `master-studio-quiz-session`.
- **Mirror translation** (sandbox `99_Archives/sandbox_mirror_translate/`, gitignored): ① facsimile (≥150 DPI screenshot) ② literal Arabic ③ comprehension. Unit = TOPIC, not pages. Skill `master-studio-mirror-translation`.
- **Phone sync** `90_Shared_Toolbox/tools/phone_sync.py` v2: `adb push --sync` incremental; **exit 1 = real failure**. Flags `--dry-run/--all/--full/--prune/--clean --yes/--pull/--wifi/--serial/--json/--no-repair`. Tests `tests/test_phone_sync_plan.py` (33). adb facts: push summary goes to **stderr**; `--sync` compares **timestamps only** (size-verify + force re-push is mandatory); `adb push src/. dst` needs raw `"/."`; typical full run ≈ 3 min.

## F. Postgrad grading law (VERIFIED + FIELD-CONFIRMED 2026-10-04)
- Rules = **تعليمات 27/1982** (Art.17 of 26/1990 keeps it alive). **Art.24(1)** scale: ممتاز/جيد جداً/جيد 70–79/**مقبول 60–69**/راسب ≤59 — **floor 60, not 50**. **24(4)** dismissal if failing >half of S1. **24(5)** needs مقبول everywhere AND year avg ≥70; else re-sit at start of next academic year in failed + chosen courses; fail again ⇒ dismissal. **24(6)** weighted by credit units. **25** one re-sit.
- **Field practice:** «متوسط» low band exists; prep-year avg = ONE figure over BOTH semesters; failing any course pulls متوسط courses into re-sit; **69 ⇒ dismissal (ترقين قيد)**; parking a subject is the worst move → ≥60 in every course + protect year avg ≥70.
- **His split:** **30% سعي / 70% نهائي**; his continuous ≈ **18–22/30**. Passing (≥60 total) needs only ~54–60% on the final; جيد (≥70) needs ~69–74%.
- **Real curriculum:** prep year = 2 courses × 6 subjects = 12 subjects / 24 units. Course 1: Cyber(2), Software-dev-techniques(2), Data-mining(2), Multimedia(2), **Adv-SE(3)**, English(1). Course 2: Adv-AI(2), Adv-algorithms(2), **Software-architecture(3)**, Web-dev(2), Cloud(2), Research-methodology(1). Year avg = one weighted figure (Art.24/6). **Levers = the two 3-credit subjects (Adv SE + Software architecture = 25% combined).** Canonical: `00_STUDIO_HUB/ACADEMIC_REGULATIONS.md` §3.4. The old `SEM1_FOCUS_AND_MARKS_PLAN.md` roster is wrong — needs rewriting.

## G. AI course (CS605, Dr. Saif Al-Saidi) — ON HOLD
Lectures origin = **Diane J. Cook**, *CptS 440/540 AI*, WSU EECS Fall 2009; textbook AIMA (Russell & Norvig). Banks: `aimacode.github.io/aima-exercises/` · Berkeley CS188 exams · WSU `angelxd84130/WSU-cpts-540-ArtificialIntelligence` · UW-Madison CS540. Report `06_Artificial_Intelligence/AI_EXTERNAL_QUESTION_BANKS.md`.

## H. ASE — source-of-truth map
- **source of truth = `02_Raw_Materials/`.** Question origin = **Aggarwal & Singh, *Software Engineering*, 3rd ed.** official slides in `Aggarwal_Singh_Slides/` + `Aggarwal_Singh_SE_3rd_ed_By_Chapter/`. The file `Aggarwal_Singh_SE_3rd_ed_Book.pdf` (1094 pp, MD5 d154ed3d…) is **concatenated slides, NOT the narrative textbook**.
- **AliFahim `Reference_Textbooks/AliFahim_Software_Engineering.pdf`** (256 pp) = **2-up portrait SCAN of the SAME Aggarwal & Singh 3rd-ed book**, **no text layer** (chars=0) → cite only via high-DPI render + vision (2× matrix ≈ 144 DPI sufficed). **Page offset DRIFTS** (≈ PDF = printed − 95 early in a chapter, − 116 later) — never assume one constant.
- Other textbooks WITH text: RajibMall 4th (strongest for Aggarwal terms), Pressman, CS Agarwal 2010, Sommerville 9th (weak for Aggarwal terms), Leach 2nd.
- **Question banks:** `02_Raw_Materials/Question_Banks/` = SEPM ModuleWise · NRCMEC UnitWise (with Bloom BT) · GitHub KPRIT (Part A/B/C).
- **Exam papers:** `Aggarwal_Singh_Slides/exam_papers/02_Exam_Question_Papers/MRCET_SE_EndTerm_Paper_2022Dec.pdf` = **19 real MRCET papers (R17/R18/R20)**; `01_MAIT_ETCS252_Tutorials/` = MCQs.
- `05_Seminars_&_Slides/_sandbox_trial/` = pre-existing grounded Ch5 notes (303 lines, `[S:n]` anchors, 6-book `corpus/`) — **always sweep before building any chapter's material**.

## I. ASE Ch05 deep-study (BUILT + 5-ROUND VERIFIED 2026-10-12)
- Note: `03_Study_Notes/Week_03_Ch05_Software_Design_Solved.md`; audit `Ch05_AliFahim_vs_Slides_Audit.md`.
- Sandbox `01_Semester_1/04_Advanced_Software_Eng/08_DeepStudy_Ch05/` (6 files): `00_STUDY_SYSTEM.md` (Bloom+KG method, 6-phase protocol) · `01_TIER1_MODEL_QUESTIONS.md` (12 MCQ + 24 essays) · `02_TIER2_DEEP_QUESTIONS.md` (27 deep) · `03_EXTERNAL_QUESTIONS_AND_DEEPER_CONTENT.md` · `04_EXAM_PATTERN_BANK.md` · `99_SOURCE_MAP.md`.
- **Engine:** Bloom (Anderson & Krathwohl 2001) depth ladder + KG-MuLQA axes (multi-hop / set-ops / plurality). Pipeline CHUNK→TAG→GENERATE→VERIFY→TIER→BALANCE. **Tier law:** Tier1 = official style (Remember+Understand); Tier2 = Apply/Analyze/Evaluate/Create — never mix tiers in one file.
- **His Dr (Ali Fahim):** delivers the Aggarwal slides at surface depth → exam = official questions + rephrasing → **Tier2 depth is the differentiator**. 6-phase study protocol (read → Tier1 → close gaps → Tier2 → redraw figures → self-explain). Iron rule: never solve questions before reading.
- **Ch05 hard facts:** coupling best→worst data>stamp>control>external>common>content; cohesion best→worst functional>sequential>communicational>procedural>temporal>logical>coincidental; strategies top-down/bottom-up/**hybrid (most practical)**; SDD = IEEE 1016. **OOD = SIX steps** (book Fig 5.25 + slides 72/73/75) — the earlier "7 steps" claim was WRONG. **Vitruvius = THREE attributes** (durability/utility/charm); the 4 (correct&complete/understandable/right-level/maintainable) are the separate §5.1.2 objectives — never merge. Book Ch5 questions = slides 94–99 word-for-word; no hidden set.
- **Exam pattern bank (Ch5) = 6 recurring axes:** coupling&cohesion ★★★ · OOD process+merits ★★★ · architecture+styles ★★☆ · design concepts ★★☆ · UI golden rules ★☆☆ · data design ★☆☆.
- **Per-type files** `08_DeepStudy_Ch05/ByType/` (7 files, 180 Qs, all exported to PDF with SVG diagrams in `_diagrams/`): `00_INDEX_BY_TYPE.md` · `T1_MCQ.md` (37) · `T2_Essay_Descriptive.md` (44) · `T3_Understand.md` (35) · `T4_Analyze.md` (15) · `T5_Evaluate.md` (15) · `T6_Create_Design.md` (16) · `T7_Apply_Calc.md` (18). No official MCQ answer key exists — derived from chapter text. `ByType_Visio_Compare/` holds the accepted Visio UML variant (`T6_Create_Design_UML.md/pdf`, 22 pp) with editable `.vsdx` (use-case/class/sequence).

## J. Visio COM (for ASE diagrams)
`Visio.InvisibleApp` 16.0. `Documents.OpenEx(path, 2|8)` **requires the stencil copied OUT of `C:\Program Files\...`** into a writable dir, else "File not found". `page.Drop(master, x, y)`; `DrawLine`+`EndArrow` beats dynamic connectors. **Text artifacts:** collapses space between a Latin word and a following digit; reorders a comma before a word; `<<include>>` renders as `>>include<<`; connector labels auto-rotate unless placed in separate text rectangles; the `Class` master packs compartment text → hand-draw 3-compartment class boxes. UML stencils: `UUSEME_M.VSSX`, `USEQME_M.VSSX`, `UML_CLASS_M.VSTX`, `ASSOCIATIONS_UML_CLASS_M.VSTX`, `DBUML_M.VSSX`, `SDL_M.VSSX`. **No dedicated DFD stencil** in this install. Lab: `08_DeepStudy_Ch05/_visio_lab/` (`visio_uml_render.py`).
