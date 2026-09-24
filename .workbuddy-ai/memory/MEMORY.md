# Master Studio — Curated Project Memory

## 1. Repository & External-Chatbot Access (STANDING CONSTRAINT)
- **The GitHub repo must stay PUBLIC.** The student's workflow is: open the GitHub link and feed it to a **free web chatbot** (DeepSeek / Qwen / ChatGPT free tier) as *external support / knowledge*. The repo is the transport layer between this vault and any free web LLM.
- Repo: `https://github.com/AboALhasanx/master-studio` — visibility **PUBLIC**, branch `master`.
- Therefore: **never** make the repo private, never add blanket ignore rules that hide study notes, and never break raw-file readability. Study `.md` notes are intentionally public — the student has explicitly confirmed that study markdown being public is fine.
- GitHub Pages is **not** enabled; there is no hosted web UI. Access is file browsing + `raw.githubusercontent.com` links.
- Digest packs for chatbot ingestion: `90_Shared_Toolbox/tools/pack_subject.py` → `*digest*.md` / `repomix-output.*` are **gitignored** (generated on demand, not committed).
- **External digest service = [Gitingest](https://gitingest.com).** Trick: replace `hub` with `ingest` in any GitHub URL. Use the **subpath** form for a subject/folder: `https://gitingest.com/AboALhasanx/master-studio/tree/master/01_Semester_1/02_English_Language`. Whole-repo digest is ~141.5k tokens (too big for most free chatbots); a subject is ~31k, a folder ~24k. **Always ingest per subject/folder, never the whole repo.**
- `gitingest` CLI is installed in the managed venv. Prefer the URL-subpath form; `-i "folder/*"` gets glob-expanded by Git Bash and fails. Alternatives: `repomix.com`, `deepwiki.com/AboALhasanx/master-studio`. Do **not** recommend `uithub.com` (now returns 401).
- `.workbuddy-ai/memory/` **is tracked and therefore public** — it is an agent work-log, not personal documents. Keep it free of anything private.

## 2. Pushing to GitHub (non-obvious environment quirk)
The agent shell has **`APPDATA` unset**, which breaks `gh` (it cannot find `%APPDATA%\GitHub CLI\hosts.yml`) and makes `git push` fail with `could not read Username`. The working recipe (requires sandbox disabled, since the sandbox hides the Windows keyring):
```bash
export APPDATA="C:\\Users\\gokoq\\AppData\\Roaming"
export HOME="/c/Users/gokoq"
cd "C:/Users/gokoq/Master-Studio"
gh auth setup-git
git push origin master
```
`gh` is authenticated as `AboALhasanx` via keyring token.

## 3. Vault location — CANONICAL PATH = `C:\Users\gokoq\Master-Studio` (moved off Drive 2026-09-23)
- **The vault now lives at `C:\Users\gokoq\Master-Studio`** (moved here on 2026-09-23 from Google Drive File Stream). This is the ONLY current working copy. All source notes, the git repo (`.git`), tooling (`90_Shared_Toolbox`), and agent memory (`.workbuddy-ai/memory`) are here.
- **`G:\My Drive\Master-Studio` is now a STALE/ORPHANED copy — do NOT work there.** Any work done in G: is in the wrong place and must be moved to C:. (This bit us on 2026-09-24: the PDF exports were accidentally created in G: and had to be moved to C:.)
- **Historical Drive hazard (now avoided):** Google Drive File Stream injects `desktop.ini` into every folder including `.git/`, corrupting git (`fatal: bad object refs/desktop.ini`) and able to wipe `.git/refs/remotes/`. Moving the vault to a plain local path (C:) eliminates this. Cleanup tool remains if ever needed: `90_Shared_Toolbox/tools/fix_git_drive_desktop_ini.py`.
- The safe-delete guard refuses to delete from the G: Drive path (trash op fails there — fail-closed, files preserved), so G: duplicates may linger. That is harmless; just ensure the canonical C: copy is correct.

## 4. Student operating rules
- **Zero-CLI policy:** the student speaks plain Arabic/English; the agent runs all tools, commits, and pushes autonomously. Never ask him to run commands.
- **Recap at every section transition** (standing instruction) — restate what was covered, what is solved, where we are.
- Exam strategy: prioritize **fixed/memorizable** items (vocabulary, grammar, fixed phrases); deprioritize story comprehension and skills sections.
- Anti-hallucination: never fabricate citations/DOIs; tag unverifiable claims `[Foundational Knowledge / Standard Concept]`.

## 5. The Delivery Gate — MANDATORY, NO EXCEPTIONS (learned the hard way 2026-09-24)

**I once delivered five PDFs that rendered with fake "Q" boxes and leaked bold. The student had to fix them with another agent. Do not repeat it.** The gate now exists; run it.

**Read before authoring, in this order:** `AGENTS.md` (§6.0.1 is the gate) → `00_STUDIO_HUB/STUDY_NOTE_MANIFESTO.md` (the 7 Laws) → `00_STUDIO_HUB/guides/ACADEMIC_STUDY_NOTE_SOP.md` → `00_STUDIO_HUB/guides/PDF_PUBLISHING_SOP.md` (the 9 Engine Laws + §6 checklist) → `00_STUDIO_HUB/templates/template-study-unit.md`.

**Run before delivery, in this order — never skip step 1:**
```bash
python "90_Shared_Toolbox/tools/note_linter.py" "<note>.md" --fix --strict   # MUST exit 0
python "90_Shared_Toolbox/tools/pdf_exporter.py" "<note>.md" -t study_pack
```
Then render the pages with PyMuPDF and **look at them**. The linter cannot see a fake Q box or a leaked bold — only eyes on the page catch those.

**The two defect classes that bit me, and their authoring rules:**
1. **Fake "Q" cards in the lecture body.** Cause was an unscoped `re.DOTALL` QA regex in `transform_qa_cards()` that matched any bold numbered line followed by a blockquote anywhere in the document. **Now fixed engine-side** — the transform is partitioned at the `## Retrieval set` heading and the body is immune. **Still: never put a bold numbered line directly above a blockquote outside the retrieval set.**
2. **Bold leaking across a whole page.** Cause: I wrote `***Change avoidance**` — three opening asterisks, two closing. **Manifesto Law 5: never `***`.** Inside a `*"…"*` verbatim quote every bold span must open and close with exactly `**`.

**Retrieval-set format that renders as emerald cards:** `**[RS-XX-YY]** Question?` on its own line, answer in a `>` blockquote directly beneath. A leading `Answer:` is stripped automatically; do not add a `Model Answer` label.

**Windows File Lock Law (Engine Law 1):** if a PDF is open in a viewer, the exporter writes `*_new.pdf` instead of failing. That is a *notice*, not an error — but it means the canonical filename still holds the **old** content. Always tell the student, and check which file is actually current.

## 6. Verbatim-callout authoring rule — the label MUST live INSIDE the quote block (LEARNED 2026-09-24, student-flagged)

**The slip (student caught it in the rendered PDF):** I attached the source label to a verbatim quote as a **standalone bold paragraph** sitting *above* the quote. The renderer then draws that label **outside** the callout, as a bold line over an empty-looking box — visually broken. The label belongs **within** the quotation, never outside it. The student's words: *"المفروض تشوف زين أنو الاسم يجي ضمن الاقتباس وليس خارجه."* He marked this **unforgivable unless I record it properly.** So: recorded, and it is now a hard authoring law.

**WRONG (label outside — renders as a bold line above a separate callout):**
```markdown
**Verbatim (Mall p.114):**

> This model gets its name from the appearance of its diagrammatic representation ...
```

**RIGHT (label inside — one `>` block, label and quote on the same line):**
```markdown
> **Verbatim (Mall p.67):** *"At this stage, the customers are usually **not clear about all the features that would be needed** ..."*
```

**The rule, generalised:** *any* label bound to a blockquote — `Verbatim`, `Source`, `Note`, `Quoted`, `المصدر`, `اقتباس` — must be **inside the `>` block on the same line as the quote** (or at minimum inside the same `>` block as its own `>` line, never as a bare paragraph above it). Never let a bold label escape the blockquote.

**Where the defect currently exists (DO NOT fix now — student said leave it, we built and finished; fix only when he asks):**
- `03_Study_Notes/Week_02_File_06_The_Spiral_Model.md` — lines **49** and **55** (`**Verbatim (Mall p.114):**` followed by a blank line then `> …`).
- `03_Study_Notes/Week_02_File_08_Agile_XP_Scrum.md` — lines **294** and **298** (same pattern).
- Propagated into the merged `Week_02_Master_Lecture.md` (≈ lines 2534, 2540, 3318, 3322) → visible in `08_PDF_Exports/Week_02_Master_Lecture.pdf`.

**Why my eye missed it:** both forms look identical in *raw markdown preview* — the difference only appears in the rendered callout box. This is exactly the "render the page and actually look at it" step of the Delivery Gate (§5); a structural check of "is every `**Verbatim…**` line prefixed with `>`?" would have caught it mechanically. Add that grep to the pre-delivery sweep.

## 7. Authoring rules learned 2026-09-24 (student-flagged; Manifesto Law 6 + Pillar 3)

1. **No filler labels.** Never write `الشرح بالعربي:` / `**AR.**` / `**EN.**` / `(ترجمة)` as a *label* above the Arabic. The Arabic rationale is **Pillar 3** — it must be **woven in, unlabelled**, directly after the English it explains (and it should **decode the hard English terms** and connect back to the preceding paragraph). A label is scaffolding and violates Manifesto Law 6.
2. **Depth is mandatory, not a summary.** The student wants a **ملزمة** (deep pedagogical instrument), never a compressed summary. Per section: narrative spine → verbatim anchor → Feynman intuition → bilingual rationale → and where possible a **worked example** and **equations**. Padding is banned; *genuine* explanation is required.
3. **The linter + exporter were fixed 2026-09-24 by the other agent.** `*"…"*` italic verbatim quotes and `&` / apostrophes are allowed again — **but the fix does NOT cover the `.qa-card` text path** in `transform_qa_cards()` (still double-escapes `&` → `&amp;`). Workaround: avoid `&` **inside retrieval-set questions** only.
4. **Page-count sanity:** the ASE master lecture (146 pp) merged **ten units**; a single-topic ملزمة should be compared to **one unit** (~15 pp), and a good one runs **20–30 pp**.
