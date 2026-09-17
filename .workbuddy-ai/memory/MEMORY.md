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
cd "G:/My Drive/Master-Studio"
gh auth setup-git
git push origin master
```
`gh` is authenticated as `AboALhasanx` via keyring token.

## 3. Google Drive File Stream + `.git` hazard
The vault lives on `G:` (Drive File Stream). Drive injects `desktop.ini` into **every** folder including `.git/`, which corrupts git (`fatal: bad object refs/desktop.ini`) and can wipe `.git/refs/remotes/`. Cleanup tool: `90_Shared_Toolbox/tools/fix_git_drive_desktop_ini.py`. If git refs misbehave, suspect Drive write-lag and retry the write.

## 4. Student operating rules
- **Zero-CLI policy:** the student speaks plain Arabic/English; the agent runs all tools, commits, and pushes autonomously. Never ask him to run commands.
- **Recap at every section transition** (standing instruction) — restate what was covered, what is solved, where we are.
- Exam strategy: prioritize **fixed/memorizable** items (vocabulary, grammar, fixed phrases); deprioritize story comprehension and skills sections.
- Anti-hallucination: never fabricate citations/DOIs; tag unverifiable claims `[Foundational Knowledge / Standard Concept]`.
