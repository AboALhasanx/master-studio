---
name: mcq-portal-pipeline
description: Author, validate, publish, mirror and verify MCSQuiz question banks end to end. Use when writing or editing any 01_Semester_1/<Subject>/07_Quizzes_&_Anki/Quiz_*.json file, when running quiz_balancer or portal_content.py (sync, status, hide, show, pull), when naming chapters/topics or retiring a bank, and when verifying the catalogue, a quiz, the offline copy or the content version in the app.
---

# MCSQuiz portal pipeline

> The vault owns the banks. Supabase (`content_banks`) is the live copy the app reads.
> `mcq-portal/data/` is only the offline fallback. The binding rules live in
> `00_STUDIO_HUB/guides/QUIZ_BANK_PROTOCOL.md` — this skill is the executable
> shortcut: the exact commands, in order, with the gates that block a bad publish.

## 0. Boot (every run)

1. Read `00_STUDIO_HUB/ACTIVE_STATE.md`, `HARNESS_REGISTRY.md`, today's
   `sessions/YYYY-MM-DD.md`. Sign in by name before editing (root `AGENTS.md` §8).
2. The live truth is `python 90_Shared_Toolbox/tools/portal_content.py status`
   plus `01_Semester_1/*/07_Quizzes_&_Anki/`. Never invent a second map.

## 1. Scaffold the file — do not hand-type the envelope

```bash
cd C:\Users\gokoq\Master-Studio
python 00_STUDIO_HUB/skills/mcq-portal-pipeline/scripts/new_bank.py \
  --subject 03_Data_Mining --chapter 2 --kind model --model B \
  --slug Data_Types --title-ar "أنواع البيانات وتحضيرها" \
  --title-en "Data types and preparation" --questions 5
```

The script picks the file name and `quiz_id`, copies the instructor pair and
`subject_title` from a live bank of the same subject, and refuses bad input:

- `topic_ar` must **not** contain the subject name (the app's subject chip
  already says it);
- a `model` bank title must end with `— النموذج أ/ب`; a `topic` bank title
  must be plain (no suffix — the app renders the `موضوع: N` badge itself);
- chapter is the **book's** number (`04_Advanced_Software_Eng` uses 1, 2, 5).

Fill the `TODO` questions afterwards. The scaffold alone never passes the gates,
so it can never be published by accident.

## 2. Fill the questions (the rules that actually fail reviews)

- Arabic-first, MSA, no dialect; technical terms stay in clean English with no
  parenthetical echo; `←` inside Arabic lines, `→` inside English lines.
- 4 options, plausible distractors within ±25 % of the correct option's length;
  the key must never be the longest or the most qualified option.
- `concept_id` unique across **every bank of the chapter** (not just the file).
- Math only as `$…$` / `$$…$$`, never with Arabic inside; KaTeX renders it.
- Every claim traceable to the subject's study notes. Nothing invented —
  no definitions, numbers, authors, pages or DOIs from memory.

## 3. Run the gates (all three, in this order, paste the output)

```bash
cd C:\Users\gokoq\Master-Studio
python "90_Shared_Toolbox/tools/quiz_balancer.py" "01_Semester_1/<Subject>/07_Quizzes_&_Anki/<file>.json"
python "90_Shared_Toolbox/tools/quiz_balancer.py" "01_Semester_1/<Subject>/07_Quizzes_&_Anki/<file>.json" --check --strict
python -c "import sys,json,io; sys.path.insert(0,r'90_Shared_Toolbox/tools'); from quiz_balancer import validate_schema_v2; sys.path.insert(0,r'C:\Users\gokoq\mcq-portal\tools'); import portal_schema as ps; p=r'<file>'; b=json.load(io.open(p,encoding='utf-8')); print(validate_schema_v2(b), ps.validate_v3(ps.to_v3(b)))"
```

- `--strict` without `--check` **writes** the file (it balances after the gate).
  Audit read-only with `--check --strict`; balance once, on purpose.
- After any balance pass, re-open the file and re-check every `answer`/`correct`
  pair — `"ABCD"[correct] === answer` must hold with the intended text as key.
- Exit 0 and two empty lists, or the bank does not ship. No exceptions.

## 4. Publish, then mirror

```bash
python "90_Shared_Toolbox/tools/portal_content.py" status
python "90_Shared_Toolbox/tools/portal_content.py" sync            # validate -> merge -> publish -> version -> log
python "90_Shared_Toolbox/tools/portal_content.py" pull           # refresh mcq-portal/data + the SW precache list
```

- Content needs no deploy: the next visit pulls the new manifest and the bell
  counts the unread chapters.
- `pull` only rewrites the bundled fallback. Deploy the shell
  (`cd C:\Users\gokoq\mcq-portal; npx -y vercel@latest --prod --yes`) only when
  it reports a precache change.
- Retire, never delete: move the dead file to `07_Quizzes_&_Anki/_retired/`,
  delete its portal row (`sync` drops rows whose file is gone), and say so.
  (The vault `.gitignore` ignores `_archive/` — use `_retired/`.)
- Never `git add -A` in the vault. Stage only your files.

## 5. Verify in the app (JSON passing is not done)

1. Subject chips list the subject; the chapter bar lists each chapter **number
   once**; a chapter shows its cards with the `موضوع: N` badge, أ before ب.
2. Start the new quiz twice: the question order **and** the option order must
   differ between runs while the correct **text** stays the key
   (Fisher–Yates per launch, `correct` remapped — see
   `references/runtime.md`). The ع/EN (translation-icon) toggle must translate
   stem, options and explanation.
3. Offline: block the portal (or kill the network) — the chapter must still
   open from the cached manifest, then from the bundled fallback.
4. Report the evidence: the exact commands and their output, plus what you saw.

## 6. Hand back

```
FILES   : <path> (one line per file)
BANK    : subject_id | chapter | model-or-topic | quiz_id | questions
CONCEPTS: q1 … qN (one line each, no repeats across the chapter)
KEYS    : A n | B n | C n | D n
GATES   : balancer / --check --strict / v2+v3 output (paste it)
APP     : what you opened, answered and saw (portal version included)
OPEN    : anything the source did not settle
```

Retiring, renaming, or touching another harness's bank: name it with the date
(*"found work from OpenCode 2026-10-22, left intact"*) in the session log.
