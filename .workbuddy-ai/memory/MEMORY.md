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

## I. ASE deep-study sandboxes (Ch05 + Ch04, BUILT + 5-ROUND VERIFIED)
- **Engine (both):** Bloom (Anderson & Krathwohl 2001) depth ladder + KG-MuLQA axes. Pipeline CHUNK→TAG→GENERATE→VERIFY→TIER→BALANCE. **Tier law:** Tier1 = official style (Remember+Understand); Tier2 = Apply/Analyze/Evaluate/Create — never mix tiers in one file. **His Dr (Ali Fahim):** delivers Aggarwal slides at surface depth → exam = official questions + rephrasing → **Tier2 depth is the differentiator.** Iron rule: never solve questions before reading. Question origin = **Aggarwal & Singh, *Software Engineering*, 3rd ed.**
- **Ch05** `08_DeepStudy_Ch05/` (note `03_Study_Notes/Week_03_Ch05_Software_Design_Solved.md`): coupling best→worst data>stamp>control>external>common>content; cohesion functional>sequential>communicational>procedural>temporal>logical>coincidental; strategies top-down/bottom-up/**hybrid (most practical)**; SDD = IEEE 1016. **OOD = SIX steps** (not 7). **Vitruvius = THREE attributes** (durability/utility/charm). Book Ch5 Qs = slides 94–99 verbatim. Exam axes: coupling&cohesion ★★★ · OOD process ★★★ · architecture · design concepts · UI · data design. `ByType/` T1–T7 (180 Qs) + `_diagrams/`; `ByType_Visio_Compare/` = accepted Visio UML variant (22 pp, editable `.vsdx`).
- **Ch04** `08_DeepStudy_Ch04/` (Software Project Planning, 207 slides, numeric/formula-heavy): 14 root notes + `ByType/` T1–T7 + 7 diagrams + `_pdf/` + `_pdf_verified/`. **5-round campaign COMPLETE** (protocol `_VERIFICATION_PROTOCOL.md`): Round 3 fixed 3 wrong MCQs (4.14 b, 4.22 c, 4.23 a) + missing Example 4.2 + fabricated Example 4.5 table + Q7.8 phase split. **Round-3 arithmetic audit (2026-10-13) fixed 7 wrong-power errors:** `200^1.12=377.71`·`50^1.12=79.96`·`600^1.05/1.12/1.20=826.15/1292.79/2156.66`·`22^0.91=16.6573`·`22^0.93=17.7196`·`32^1.05=38.0546`·`7^1.05=7.7153`. Frozen facts: `FP=UFP×CAF`, `CAF=0.65+0.01ΣFi`; Basic a=2.4/3.0/3.6, b=1.05/1.12/1.20; Intermediate a_i=3.2/3.0/**2.8**; drivers 15/7/17, scale factors 5; `B=0.91+0.01ΣSF`; `m₀=K/(td·e)`, `D=K/td²`, `D₀=K/td³` (8/15/27), `Kd=K/6`, `tod=td/√6`, `S=C·K^(1/3)·td^(4/3)`; Risk = 2 groups/6 activities, Jones 5 categories. Committed `66aef51`.

## J. Visio COM (for ASE diagrams)
`Visio.InvisibleApp` 16.0. `Documents.OpenEx(path, 2|8)` requires the stencil copied OUT of `C:\Program Files\...` into a writable dir. `page.Drop(master,x,y)`; `DrawLine`+`EndArrow` beats dynamic connectors. Artifacts: collapses space before a digit, reorders commas, `<<include>>`→`>>include<<`, labels auto-rotate. UML stencils: `UUSEME_M.VSSX`, `USEQME_M.VSSX`, `UML_CLASS_M.VSTX`, `ASSOCIATIONS_UML_CLASS_M.VSTX`. **No dedicated DFD stencil.** Lab: `08_DeepStudy_Ch05/_visio_lab/`.
