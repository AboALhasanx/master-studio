# Master Studio — Curated Project Memory

## A. Repo & bridge (STANDING)
`AboALhasanx/master-studio` PUBLIC, branch `master` — chatbot bridge. Never privatize / break raw-file readability / GitHub Pages. Gitingest digest (`hub`→`ingest`). `.workbuddy-ai/memory/` public → keep clean.

## B. Env quirks
- **Push** (sandbox OFF, APPDATA unset): `export APPDATA="C:\\Users\\gokoq\\AppData\\Roaming"; export HOME="/c/Users/gokoq"; cd "C:/Users/gokoq/Master-Studio"; gh auth setup-git; git push origin master`
- **Vault** = `C:\Users\gokoq\Master-Studio` (off Drive 2026-09-23; `G:\My Drive\Master-Studio` STALE — Drive `desktop.ini` corrupted `.git/`).
- **pytest:** safe-delete shim → prefix `CODEBUDDY_SAFE_DELETE_ENABLED=0`; use system `Python312`. `curl` proxied → use Python. Arabic → `-X utf8`.

## C. Student rules
Zero-CLI (I run all). Recap at each transition; end block "is that it or more?". Correct bluntly. Arabic to him / formal EN out. Go DEEP; never compress an already-condensed source w/o asking. Conflicting instructions → STOP & ask ("قرار مصيري"). Verify, no fabrication, tag guesses `[Foundational Knowledge / Standard Concept]`. Announce before deleting.

## D. Delivery Gate (note→PDF) + RTL/image pitfalls
Gate: 1. `note_linter.py "<note>.md" --fix --strict` (exit 0)  2. `pdf_exporter.py "<note>.md" -t study_pack`  3. Render w/ PyMuPDF & LOOK.
**RTL pitfalls (check every render):** ordered lists scramble → `| # | … |` table; consecutive Q/A bold lines merge → `| السؤال | الجواب |` table or blank line; `inline code` with `_`/`/` reverses in Arabic → name file in prose; trailing `(ص 103)` jumps to line start → drop it.
**Image-heavy slides:** `get_text()` thin → render visually; composite 4–6 pp/sheet 150–200 DPI, zoom 380–400 DPI on digits/eq. ALWAYS `page.get_images()` per page before judging a deck (text layer can be empty while slides are embedded images).

## E. Authoring rules
No filler labels; Arabic woven. YAML frontmatter w/ REAL title (`title: ملزمة الويك N — <topic>` + `course:` + `subtitle:`); ban exporter default title. Content-type label per section; EN lists SEPARATE from Arabic. Verbatim label INSIDE `>` block. "صفحة صفحة": ①نص verbatim ②ترجمة حرفية ③شرح فهمي. Source of truth = raw `02_Raw_Materials/`.

## F. Discipline
Never cite a commit hash before `origin/master`. Test count only true via `--collect-only`. `gh issue close` → `--comment "$(cat f)"`. Telegram live gate: read `MessageEntityTextUrl`.

## G–I. Telegram / Quiz / Mirror
- **Telegram** (committed `edb503f`): D14 owns `00_STUDIO_HUB/telegram/`, reads memory, never writes `MEMORY.md`; D15 = ONE bounded session, fail-closed, `update_id` persisted; D16 admin verbs → owner approval. Bot `cs_mscbot`. Contract `proposals/TELEGRAM_INTERACTIVE_ARCHITECTURE.md`.
- **Quiz** = LIVE: "يلا" → Flask (`start-quiz-server.bat`) + QR (`show-quiz-qr.bat <Sub> <Quiz>`) + `_wait_quiz_result.py`; kill both; trust `curl /api/health`. Skill `master-studio-quiz-session`.
- **Mirror translation** (sandbox `99_Archives/sandbox_mirror_translate/`, gitignored): ① facsimile (≥150DPI screenshot) ② literal Arabic ③ comprehension. Unit = TOPIC, not pages. Skill `master-studio-mirror-translation`.

## J. Postgrad grading law (VERIFIED + FIELD-CONFIRMED 2026-10-04)
Rules = **تعليمات 27/1982** (Art.17 of 26/1990 keeps 27 alive). **Art.24(1)** scale: ممتاز/جيد جداً/جيد 70–79/**مقبول 60–69**/راسب ≤59; **floor 60 not 50**. **24(4)** dismissal if failing >half of S1 (6 subj ⇒ line 4). **24(5)** needs مقبول everywhere AND avg جيد=**70**; else re-sit at start of next academic year in failed + chosen courses; fail again ⇒ dismissal. **24(6)** weighted by credit units. **25** one re-sit. MOHESR 21 Jul 2026 adopted **60** prep-year threshold.
**FIELD PRACTICE (FB 260k group):** «متوسط» low band DOES exist (corrects strict reading); prep-year avg = ONE figure over BOTH semesters (grade×units); failing any course pulls متوسط courses into re-sit; **69 ⇒ dismissal (ترقين قيد)**; deliberately parking a subject is worst move → ≥60 every course + protect year avg ≥70. 3-credit courses (ASE, AI) are levers; English (1cr) cheap weak spot.
Canonical: `00_STUDIO_HUB/ACADEMIC_REGULATIONS.md` §3.4; plan `SEM1_FOCUS_AND_MARKS_PLAN.md`.

## K. AI course (CS605, Dr. Saif Al-Saidi) — origin + banks
**ON HOLD** (Dean delivered nothing). Lectures origin = **Diane J. Cook**, *CptS 440/540 AI*, WSU EECS Fall 2009; textbook AIMA (Russell & Norvig). Banks: `aimacode.github.io/aima-exercises/` · Berkeley CS188 `people.eecs.berkeley.edu/~russell/classes/cs188/f14/exams.html` · WSU repo `github.com/angelxd84130/WSU-cpts-540-ArtificialIntelligence` · UW-Madison CS540 `pages.cs.wisc.edu/~dyer/cs540/exams-toc.html`. Report `06_Artificial_Intelligence/AI_EXTERNAL_QUESTION_BANKS.md`.

## L. ASE material audit (2026-10-06)
Source = **Aggarwal & Singh, *Software Engineering*, 3rd ed.** Official publisher companion slides Ch.1–10 in `02_Raw_Materials/Aggarwal_Singh_SE_PPT_Chapters/`. The downloaded "book" `Aggarwal_Singh_SE_3rd_ed_Book.pdf` (1094pp, MD5 d154ed3d…) is actually **CONCATENATED SLIDES** (chapter-page counts sum to 1094; each chapter restarts p.1) — NOT the narrative textbook; real narrative textbook NOT found (all links resolve to same slides PDF). Other raw files: `SE_Ali_Fahim_Source_Textbook` (76MB, different author), `SE_Ref_Intro_to_SE_Leach_Textbook` (28MB), Pressman & Sommerville refs, `SE_Software_Testing_Slides`. Community banks in `_community_resources/`. Links split forbidden outside subject → `ASE_LINKS_BY_CHAPTER/` deleted.

## M. Phone sync tool (rewritten 2026-10-07)
`90_Shared_Toolbox/tools/phone_sync.py` (v2) = the phone↔PC transport. `adb push --sync` incremental, **exit 1 = real failure** (never report success on exit 1). Flags: `--dry-run` · `--all` · `--full` · `--prune` (list stale phone files) · `--clean --yes` (delete → exact mirror) · `--pull` → `_inbox_from_phone/` (gitignored) · `--wifi IP` · `--serial` · `--json` · `--no-repair`. Exclusions apply at **any depth**; only *directory* exclusions trigger a descent (file noise rides along and is purged on-device — purge patterns are **derived from the exclusion sets**, never hand-written). Tests: `tests/test_phone_sync_plan.py` (33, adb stubbed + synthetic vault).

**Hard-won adb facts (2026-10-07, verified on the Infinix X6878):**
1. `adb push` prints its `N files pushed / skipped / bytes` summary on **stderr**, not stdout.
2. **`--sync` compares timestamps only.** A device copy that is newer-but-different is *never* corrected — the phone held a 31,188 B `AGENTS.md` against the vault's 25,697 B and `--sync` answered "0 pushed, 1 skipped" every run. Hence size-verification + forced re-push (`repair_mismatches`) is mandatory, not optional.
3. `adb push -n` genuinely does not write (probe file never appeared) → `--dry-run` is safe.
4. `adb push src/. dst` needs the raw string `"/."` — `pathlib` normalises `Path / "."` away and adb then nests folders. Use `str(child) + "/."`.
5. `find -exec stat -c '%s|%n' {} +` works on this device (one call for all sizes); `-exec … +` on toybox is fine but the code keeps a `\;` fallback.
6. Launcher `sync-phone.bat` forwards `%*`. Typical full run ≈ 3 min; a no-change run ≈ 50 s.

**Undecided (his call, do not assume):** whether `02_Raw_Materials` should sync at all (97 files / 428 MB; the legacy `.stignore` deliberately kept them PC-only).
