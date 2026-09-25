# Master Studio — Curated Project Memory

## A. Repo & chatbot bridge (STANDING)
Repo `AboALhasanx/master-studio` MUST stay PUBLIC (branch `master`) — it is the bridge to free web chatbots (DeepSeek/Qwen/ChatGPT). Never privatize, never blanket-ignore notes, never break raw-file readability. No GitHub Pages. For chatbot digests use [Gitingest](https://gitingest.com) (swap `hub`→`ingest`; subpath per subject — whole repo ≈141k tok, too big). `.workbuddy-ai/memory/` is public; keep it clean.

## B. Env quirks
- **Push:** shell has `APPDATA` unset → `gh`/`git push` fail. Fix (sandbox OFF): `export APPDATA="C:\\Users\\gokoq\\AppData\\Roaming"; export HOME="/c/Users/gokoq"; cd "C:/Users/gokoq/Master-Studio"; gh auth setup-git; git push origin master`
- **Vault** = `C:\Users\gokoq\Master-Studio` (off Drive since 2026-09-23). `G:\My Drive\Master-Studio` is STALE — never use. Drive File Stream's `desktop.ini` corrupted `.git/`; moving to C: fixed it.

## C. Student rules
Zero-CLI (I run all). Recap at each transition; end every block with "is that it or more?". Correct him bluntly. Arabic to him / formal EN out. Go DEEP. Never compress an already-condensed source without asking (expand/keep/condense?). Conflicting instructions → STOP & ask (depth is his call = "قرار مصيري"). Verify before asserting; no fabrication; tag guesses `[Foundational Knowledge / Standard Concept]`. Announce before any delete. Follow up actively but as companion.

## D. Delivery Gate (learned 2026-09-24; fake-Q + leaked-bold shipped once)
1. `python "90_Shared_Toolbox/tools/note_linter.py" "<note>.md" --fix --strict` (exit 0)
2. `python "90_Shared_Toolbox/tools/pdf_exporter.py" "<note>.md" -t study_pack`
3. Render with PyMuPDF & LOOK at pages.
- Fake-Q: bold-numbered line above `>` outside `## Retrieval set` → avoid.
- Leaked bold: `***x**` forbidden; in `*"…"*` every bold span = exactly `**…**`.
- RS emerald card: `**[RS-XX-YY]** Q?` then `>` answer. No `Model Answer` label.
- Windows File Lock: open PDF → exporter writes `*_new.pdf`; tell him which is current.

## E. Verbatim label MUST be inside the `>` block (2026-09-24, "unforgivable unless recorded")
Never a standalone bold `**Verbatim (p.x):**` paragraph above the `>`. Defective-but-frozen (fix only if asked): `Week_02_File_06_The_Spiral_Model.md` L49,55; `Week_02_File_08_Agile_XP_Scrum.md` L294,298; `Week_02_Master_Lecture.pdf`.

## F. Authoring rules
**2026-09-24:** (1) No filler labels (`الشرح بالعربي:`/`**AR.**`/…) — Arabic (Pillar 3) woven, unlabelled. (2) Depth mandatory (ملزمة): spine→verbatim→Feynman→rationale→example/eq. (3) `&` double-escapes only in RS questions — avoid `&` there. (4) One unit≈15pp; good ملزمة 20–30pp.
**2026-09-25 (STANDING):** (1) YAML frontmatter w/ REAL title — exporter's "وثيقة المراجعة والتلخيص الأكاديمي" = حشو, banned; `title: ملزمة الويك N — <topic>` + `course:` + `subtitle:`, splits at `" — "`. (2) NO code/ASCII fences anywhere — tables/flows only; grep `^```` ` empty. (3) Title = my OWN grasp of the booklet, not literal docx title; `Week N` in Latin, never "الويk N". (4) Only reader-useful content in PDF — cut all meta ("بُني بواسطة Koko", "للفهم فقط", build logs).
**2026-09-25 (content-type structure — STANDING):** Deep-dive notes must be **classified by content type** with a `> **نوع المحتوى:** …` label per section, and English enumerations kept **separate** from Arabic. Four types: **شرح + تعريف** (definition-led) · **شرح + تعداد** (concept intro → clean enumerated table) · **تعداد فقط** (clean English list/table first; Arabic = 1-line intro + corrections in a SEPARATE blockquote AFTER the list, never wrapping it) · **نقاط + شرح**. The doctor's English lists ARE exam answers — never bury them in Arabic prose.
