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
