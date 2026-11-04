# Quiz Bank Runbook — from gate to publish

> **For the next agent, whoever you are.** This is the operational half. The *laws* (what a question
> may and may not be) live in `AGENT_HANDOFF_QUIZ_BANKS.md` — read that first, then come back here.
> This file is the exact sequence of commands, in order, with the expected output of each and what
> each failure means. Every command below has been run in this form; nothing here is theoretical.
>
> Written **2026-10-26** by Koko; state references corrected **2026-11-04**.
> The command sequence is version-independent. **No live number belongs in this file**:
> current content version, shell version, bank counts and per-chapter gate results
> all live in the generated `00_STUDIO_HUB/QUIZ_BANK_STATE.md` (see §7).

---

## 0. Environment

| Thing | Value |
|---|---|
| Vault | `C:\Users\gokoq\Master-Studio` |
| Portal repo | `C:\Users\gokoq\mcq-portal` |
| Banks | `01_Semester_1/01_Cyber_Security/07_Quizzes_&_Anki/Quiz_ChNN_TNN_*.json` |
| Builders | `scratch/chNN_lib.py` + `scratch/chNN_tNN.py` |
| Tools | `90_Shared_Toolbox/tools/` |
| Live site | https://mcq-portal-jade.vercel.app |
| Supabase project | `gywniovuupjmllbmjmai` (key is in `mcq-portal/js/supabase-config.js`, public by design) |

**Always prefix Python with `CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8`.**
The `-X utf8` is not optional: the Arabic in these banks breaks the default Windows codec.

> **`scratch/` is gitignored (since `23cfa7f`).** The helper scripts referenced below
> (`preflight.py`, `find_meta.py`, `report_len.py`, `chNN_lib.py`) exist **on this machine
> only** and will be absent after a fresh checkout. If you are a second agent on another
> machine, do not assume they are there. The tracked, always-available tools are in
> `90_Shared_Toolbox/tools/`: `quiz_balancer.py`, `quiz_quality_gate.py`,
> `publish_quizzes.py`, `portal_content.py`, `quiz_meta_pattern.py` (canonical handout
> regex + self-test) and `quiz_bank_state.py` (state + drift gate). **Never make a tracked
> tool import from `scratch/`.**

**Git pushes need the sandbox off**, plus:

```bash
export APPDATA="C:\Users\gokoq\AppData\Roaming"
export HOME="/c/Users/gokoq"
gh auth setup-git
git push origin master
```

### Two traps that cost real time

1. **Bash eats backslashes in `python -c "..."` and in heredocs.** `re.search(r"url:\s*'([^']+)'", s)`
   arrives at Python as `url:/s*` and silently returns `None`. **Any script containing a regex must be
   written to a file first** and run as `python file.py`. The heredoc form is only safe for plain
   string replacement with no `\`.
2. **`npx --yes vercel@latest` can hang indefinitely** (27 minutes, no output, observed 2026-10-26).
   When it does, call the cached CLI directly:

```bash
node "C:/Users/gokoq/AppData/Local/npm-cache/_npx/69f9afb961c37556/node_modules/vercel/dist/vc.js" --prod --yes
```

---

## 1. The pipeline, in order

Do not skip a step and do not reorder them. Each one catches a class of defect the next one cannot.

```text
 write builder  ->  report_len  ->  build  ->  balancer  ->  quality gate  ->  validate  ->  dry-run
                                                                                             |
   commit  <-  live-site verify  <-  deploy  <-  CI  <-  release  <-  live audit  <-  sync + pull
```

### Step 1 — write the builder

Copy `scratch/ch03_lib.py` to `scratch/chNN_lib.py` and change three things:

```python
REGISTRY = Path(r"C:\Users\gokoq\Master-Studio\scratch\chNN_registry.json")
# inside _foreign_concept_ids():
if p.stem == quiz_id or p.stem.startswith("Quiz_ChNN_"):   # skip the chapter being rebuilt
```

Then one builder per bank. The item tuple is:

```python
(concept_id, bloom, q_en, q_ar, opts_en, opts_ar, exp_en, exp_ar)
```

**Write the correct option at index 0.** The key pattern rotates it into place:

```python
KEY = "ABCDACBDABCD"          # 12 questions -> 12 letters
build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
```

`topic_en` / `topic_ar` become the card title. **Do not repeat the subject name in it** — the live
verifier fails a card title containing "الأمن السيبراني".

### Step 2 — check lengths BEFORE writing the bank

```bash
cd /c/Users/gokoq/Master-Studio/scratch
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 report_len.py ch03_t01.py
```

It prints EN and AR option lengths per question and flags `EN-LONG / AR-LONG / EN-SPREAD /
AR-SPREAD / EN-BAND / AR-BAND`, plus the bank's unique-longest percentage. Fix until clean, then
build. This is the whole reason the loop takes one pass instead of five.

### Step 3 — build

```bash
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 ch03_t01.py
```

Success prints `wrote <quiz_id>  N q  keys ...` and the key distribution. On failure it prints
`!! N question(s) failed a gate` and **writes nothing** — the old bank stays untouched. That is
deliberate: a failed build never leaves a half-written file.

The library enforces, at build time:

- max/min option spread (EN 1.40, AR **1.30** — Arabic is more compact, so 1.33 is visible there and
  invisible in English)
- correct ÷ mean(distractors) inside 0.88–1.12, **in both languages**
- correct is the unique longest in ≤ 30 % of the bank, unique shortest in ≤ 30 %
- no `$` or `\` in any option
- no parenthetical gloss inside an option
- `concept_id` unique against every other bank in the vault
- **no reference to the handout** (`META_RE`) in stem, options, or explanations — see §5

### Step 4 — the gates

**One command runs all of them** (recommended — it cannot forget a step):

```bash
cd /c/Users/gokoq/Master-Studio/scratch
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 preflight.py 3
```

It checks, in this order, and prints a pass/fail line for each:

```text
handout references           PASS  0 question(s)
EN unique-longest            PASS  2/103
EN unique-shortest           PASS  6/103
option spread                PASS
deep quality gate            PASS  Structural errors: 0; Shape-gate failures: 0
quiz_balancer --strict       PASS
validate_bank v2+v3          PASS
publish_quizzes --dry-run    PASS  exit 0
```

Exit 0 = safe to publish. Exit 1 = `NOT READY — failed: ...` and names them. **It never writes to the
portal**, so it is safe to run at any time. Careful: if you pipe it (`| tail`), `$?` becomes the pipe's
status — read the summary line instead of the exit code.

The output above is a historical green example. On 2026-10-27, the newly added shape audit found one
Arabic key-to-distractor-average violation in the currently active Ch3 banks. No active bank was
changed during that audit; repair it the next time Ch3 is revised or proposed for release.

A real example on an uncleaned chapter (Ch04, before work):

```text
handout references           FAIL  49 question(s)
EN unique-longest            FAIL  73/180
option spread                FAIL  EN q2 [62, 64, 41, 58]; AR q2 [53, 50, 35, 52]
```

The individual gates, if you need to run one alone:

```bash
# 4a. chapter-scoped structural, duplicate, formula, and bilingual shape audit (read-only)
cd /c/Users/gokoq/Master-Studio
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 90_Shared_Toolbox/tools/quiz_quality_gate.py \
  01_Semester_1/01_Cyber_Security/07_Quizzes_\&_Anki --chapter 3 --shape-gate
```

```bash
# 4a-bis. authoring audit — the defect classes that actually reached production
#   H1 numeric option (arithmetic in disguise)     H2 formula symbol in an option
#   H3 handout reference ("the lecture")           H4 English explanation written in Arabic
#   H5 duplicate stem                              H6 answer/correct mismatch
#   H7 options != options_en                       H8 empty explanation
#   H9 options_ar incomplete                       H10 question_ar empty
#   S1 stem pointing outside itself ("in the example", "those categories")
#   S2 short explanation   S3 letter bias   S4 near-duplicate stem
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 90_Shared_Toolbox/tools/quiz_authoring_audit.py \
  01_Semester_1/01_Cyber_Security 01_Semester_1/02_English_Language \
  01_Semester_1/03_Data_Mining 01_Semester_1/05_Soft_Computing
# exit 0 = clean, 1 = at least one H defect. `--strict` also fails on S findings.
# Any H defect blocks handoff. It is also wired into preflight.py as "authoring audit".
```

Near-duplicate stem, repeated-formula, and short-explanation findings are advisory and need a
source-based decision. Structural errors and shape-gate failures block handoff. The gate is read-only
and cannot verify factual truth or semantic equivalence between Arabic and English; inspect those
against the source.

```bash
# 4b. the vault's own balancer, per bank
for f in 01_Semester_1/01_Cyber_Security/07_Quizzes_\&_Anki/Quiz_Ch03_*.json; do
  CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 90_Shared_Toolbox/tools/quiz_balancer.py "$f" --check --strict \
    && echo "ok $(basename $f)" || echo "FAIL $(basename $f)"
done
```

```bash
# 4c. v2 + v3 schema validation over every bank
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 -c "
import json, glob, sys
sys.path.insert(0, r'90_Shared_Toolbox/tools')
import publish_quizzes as pq
schema = pq.load_portal_schema(pq.DEFAULT_PORTAL)
bad = 0
for f in sorted(glob.glob(r'01_Semester_1/01_Cyber_Security/07_Quizzes_&_Anki/Quiz_Ch03_*.json')):
    b = json.load(open(f, encoding='utf-8'))
    p = pq.validate_bank(schema, b, f)
    if p: bad += len(p); print('FAIL', b['quiz_id'], p[:2])
print('schema problems:', bad)
"
```

```bash
# 4d. canonical multi-bank dry run (no network write)
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 90_Shared_Toolbox/tools/publish_quizzes.py --dry-run
echo "EXIT=$?"     # must be 0
```

Expected: `9 passed / 0 failed`, `schema problems: 0`, `EXIT=0`.
**A green balancer does not mean the content is right** — it only bounds lengths and key spread. The
content laws are separate.

### Step 5 — publish to Supabase

```bash
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 90_Shared_Toolbox/tools/portal_content.py sync
```

Expected: `wrote N banks` (N = the current total in `QUIZ_BANK_STATE.md`, which grows
as subjects are added — it was 86 in October, 121 by November) and
`content version -> N+1`. **Never assert a fixed bank total**; read it from the
generated state file.

`sync` also **retires** any live bank whose vault file has disappeared, and says so:

```text
- Quiz_Ch03_T07_Risk_Quantification_Method retired (hidden, no vault file)
```

That is how a bank is removed: delete/move the file, run `sync`. No separate `hide` needed.

If it prints `content version unchanged (nothing new for the students)`, the bytes were identical —
usually because the build failed and the old file is still there. Check step 3.

### Step 6 — refresh the local mirror

```bash
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 90_Shared_Toolbox/tools/portal_content.py pull
```

This rewrites `mcq-portal/data/` and the service-worker precache list. If the list changes it prints
`deploy the shell`; if not, `already current`.

### Step 7 — audit what is actually live

Structural audit (shape, 4 options both languages, integer answer, bloom, explanations, unique
concept ids, length tell on the live payload):

```bash
cd scratch
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 verify_ch03_live.py
```

Handout-reference audit across the live chapters (edit the chapter tuple inside to widen it):

```bash
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 verify_no_meta_live.py
```

Vault-vs-live comparison — **every** bank, options_ar compared as a multiset because the live bank
is rotated:

```bash
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 verify_vault_vs_live.py
```

Expected: `problems: 0`, `meta references found: 0`, `N banks, 0 diffs` where N is the
current total in `QUIZ_BANK_STATE.md`. A non-zero diff almost always means the
`merge_question` translation bug has come back — see §6.

Then regenerate the state snapshot (§7) and confirm `--check` passes. The publish is
not finished until the committed state matches what you just shipped.

### Step 8 — release the shell

Content reaches students through Supabase **without a deploy**. The shell bump exists for the
offline cache (`sw.js` derives `CACHE` from `VERSION`).

```bash
cd /c/Users/gokoq/mcq-portal
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 tools/release.py patch --note "content: ..."
CODEBUDDY_SAFE_DELETE_ENABLED=0 "/c/Users/gokoq/AppData/Local/Programs/Python/Python312/python.exe" -X utf8 tools/ci.py
```

`tools/ci.py` **must** run on system Python 3.12 — playwright lives there, not in the managed
interpreter. Expected: `CI: green`.

### Step 9 — deploy

```bash
export APPDATA="C:\Users\gokoq\AppData\Roaming"; export HOME="/c/Users/gokoq"
node "C:/Users/gokoq/AppData/Local/npm-cache/_npx/69f9afb961c37556/node_modules/vercel/dist/vc.js" --prod --yes
```

### Step 10 — verify the live site, not the local one

```bash
cd /c/Users/gokoq/Master-Studio
PORTAL_URL="https://mcq-portal-jade.vercel.app" \
SUBJECT="01_Cyber_Security" CHAPTER=3 \
QUIZ="Quiz_Ch03_T02_Three_Dimensions_And_EFL" \
EXPECT=9 \
node 90_Shared_Toolbox/tools/qa/web_chapter_verify.js
```

`QUIZ` must be a **full quiz_id**, not a bank prefix — a short id makes the verifier time out at the
translation step with a misleading `waitForFunction` error.

Expected: `ALL-CHECKS-PASSED`. It asserts card count, `موضوع: N` badges, no card title repeating the
subject name, the retired bank absent, the translation toggle, and **question and option order
differing between two launches while the correct answer text stays identical**.

### Step 11 — commit both repos

```bash
cd /c/Users/gokoq/Master-Studio && git add <banks> <builders> <scripts>
git -c user.name="Abu Al-Hasan" -c user.email="aboalhasanx@users.noreply.github.com" commit -m "..."
cd /c/Users/gokoq/mcq-portal && git add -A && git commit -m "Release x.y.z: ..."
```

Then push the vault (sandbox off, env as in §0). **Never cite a commit hash before it is on
`origin/master`** — verify with `git rev-parse --short origin/master`.

---

## 2. What "done" means

A chapter is finished only when **all** of these are true. Anything less is a draft.

- [ ] every bank built by a builder, not hand-edited JSON
- [ ] `preflight.py N` exits 0 (it runs every gate below in one shot)
- [ ] `report_len` clean, balancer `--strict` green on every bank
- [ ] `validate_bank` 0 problems, `--dry-run` exit 0
- [ ] live payload audited question by question (`verify_chNN_live.py`)
- [ ] `verify_no_meta_live.py` returns 0 references
- [ ] `verify_vault_vs_live.py` returns 0 diffs
- [ ] `web_chapter_verify.js` ALL-CHECKS-PASSED **against the live URL**
- [ ] content version bumped, shell bumped, CI green, deployed
- [ ] `quiz_bank_state.py` regenerated **and** `--check` exits 0
- [ ] no live number copied into any hand-written document
- [ ] vault and portal both committed **and pushed**
- [ ] session log + memory + `AGENT_HANDOFF_QUIZ_BANKS.md` §4 updated

---

## 3. Failure modes, and what each one means

| Symptom | Cause | Fix |
|---|---|---|
| `!! N question(s) failed a gate` and no file written | a build-time gate refused it | read the tuple it prints: `(concept_id, reason, offending text)` |
| `EN-SPREAD > 1.40` | one option much longer than the rest | lengthen the short one, not shorten the long one |
| `AR-BAND outside band` | correct option too far from the AR distractor mean | lengthen one AR distractor |
| `unique-longest 4/11` | correct option is the max too often | lengthen a distractor in 2 of them |
| `refers to the handout in stem` | `META_RE` matched | rewrite the stem to ask about the subject |
| `validate_bank` complains about `bloom_level` | v3 wants `bloom`; the publisher converts | don't hand-edit the live shape |
| `pull` says `deploy the shell` | precache list changed | bump `VERSION`, CI, deploy |
| live payload Arabic differs from vault | the `merge_question` bug returned (§6) | see §6 |
| `npx vercel` hangs | package re-resolution stalls | use the cached CLI (§0) |
| `waitForFunction Timeout` in the live verifier | wrong/short `QUIZ` id | pass the full quiz_id |

---

## 4. Starting a NEW chapter — the part that matters most

**Before writing a single question, find the doctor's annotated copy.** Chapter 3 was rebuilt twice
because this was skipped: 90 of 146 questions were about material she had struck out.

### How to prove whether a PDF is annotated

```python
b = open(path, "rb").read()
print(b.count(b"/Annots"), b.count(b"/Highlight"), b.count(b"/Ink"))
```

- `W01_Intro_Annotated.pdf` → `8 / 18 / 20` → genuinely annotated.
- `W03_Risks.pdf` → `0 / 0 / 0` → **clean**, despite being in the vault.

If the vault copy is clean, the marked copy is usually **outside the vault** (the student keeps them
in `~/Downloads/Telegram Desktop/`). Ask him for it; do not guess.

### If the marks are flattened into the page (no annotation objects)

`scratch/w03_crossings.py` detects red strokes and maps them to the words underneath:

```bash
"/c/Users/gokoq/.workbuddy-ai/binaries/python/envs/ocr/Scripts/python.exe" -X utf8 scratch/w03_crossings.py
```

That interpreter has PyMuPDF; the default one does not. The same script renders pages to PNG
(`scratch/w03_annot/pNN.png`) if you want to look with your own eyes — which you should, at least on
the pages the stroke detector flags.

### Then write the map down

`03_Study_Notes/W03_Annotation_Map.md` is the template: crossed-out table, highlighted table, what
survives in one list, and an honest note about anything contradictory (for Ch03: two of the four
"exam-critical" equations are themselves crossed out).

**Never build a bank on crossed-out material, and never silently drop a section either** — say what
you dropped and why, so the student can overrule you.

---

## 5. The handout-reference gate, in detail

`META_RE` in `chNN_lib.py`. It is not about the word "ملزمة" — it is the whole class:

```text
direct    the lecture · lecture notes · the notes · the booklet · the handout · the file
          according to · the doctor · the syllabus · the slides · the material · the source
          the text · the book · the course · the module · the curriculum · the reading
indirect  this chapter · the chapter · this section · this week · as we saw · as covered
          as discussed · as presented
person    her own · her rule · she said · she states · her vocabulary · in her
Arabic    المحاضرة · الملزمات · الملزمة · الدكتورة · الشرائح · المصدر · الجابتر · المذكور
          قاعدتها · قالت إن · قالت ال · هذا الفصل · هذا القسم · هذا الأسبوع
```

It runs over the stem, **both** option lists, and **both** explanations.

Two bugs this gate has already had, both caught only by testing it against known-good text:

1. a stray **leading `|`** created an empty alternative that matched every string and rejected 12
   valid questions;
2. **`قالت`** matched inside **`استقالته`** ("his resignation").

**Before trusting a validator, run it on text you know is fine.** A validator that has never been
tested on valid input is not evidence.

---

## 6. The translation-merge bug (watch for this one)

`publish_quizzes.merge_question` used to treat any option **without Arabic letters** as untranslated
and inject the portal's older string over it. Numbers (`0.15`), acronyms and standard names
(`OCTAVE, FAIR, and NIST RMF.`) all trip it, so freshly authored answers silently reverted — English
looked right, Arabic was stale, and `answer` pointed at the wrong Arabic text. 133 options across 23
banks were exposed before it was found.

The rule is now **blank-only**: `if not str(oa[i] or "").strip()`. A non-empty value is deliberate and
is never overwritten.

**Regression test:** `scratch/verify_vault_vs_live.py` compares every bank's `options_ar` between
vault and portal as a multiset. If it reports a diff on a bank you did not touch, this bug is back.

---

## 7. Current state — one generated file

The table that used to sit here was the source of a real contradiction. It was a
**2026-10-26 snapshot** (Ch04/05/06 "not started", content v36, shell 1.7.8) that
stayed in place after Codex cleaned those chapters on 2026-10-27 and after Data
Mining Ch04–07 shipped on 2026-10-28. A reader could not tell a dated snapshot
from a current claim, and other files disagreed with it.

> **Current numbers, versions and per-chapter gate results:
> `00_STUDIO_HUB/QUIZ_BANK_STATE.md`.**
>
> Regenerate: `python -X utf8 90_Shared_Toolbox/tools/quiz_bank_state.py`
> Verify: the same command with `--check` (exit 1 = stale, do not publish).

Run `--check` at the start of a bank session and again after any bank edit. It reads
**every** bank file in **all six** subjects (not just `Quiz_ChNN_*`), compares vault to
the live manifest and the portal `VERSION`, and measures the shape gates per chapter.
It never writes to the portal.

Two rules this incident paid for:

1. **A state table always carries a subject column.** A bare `ChNN` row is ambiguous
   once two subjects have banks. The old handoff table displayed Data Mining's
   `69/7` and `55/7` under Cyber Ch02/Ch03.
2. **Hand-copied numbers are prohibited.** If a file is not the generated state file,
   it points at it. Historical counts belong in `sessions/YYYY-MM-DD.md`, dated.

**The annotation-map warning still stands.** Cyber Ch04, Ch05 and the chapters of the
other subjects have no doctor-marked copy in the vault. Ch04/Ch05/Ch06 were cleaned
as *unmarked sources* — that is a scope caveat, not a clean bill of health. Before
rebuilding any of them, get the marked copy, or say explicitly that the source is
unmarked rather than implying exam scope.

### Open items left deliberately

- **The "150 questions" figure for Ch03.** A previous agent reported that the student had confirmed a
  150-question target. No such confirmation exists in the log, and the surviving material supports
  ~103. Do not pad a chapter to hit a round number — that reintroduces exactly the repetition the
  rewrite removed.
- **Arabic spread cap is 1.30 only in `ch03_lib.py`.** Ch01 and Ch02 libs still allow 1.40. If you
  touch them, tighten to 1.30 and rebuild; expect a handful of AR-SPREAD failures to fix.
- **`scratch/` is not tidied.** It holds builders for Ch01–Ch03, several one-off patch scripts, and
  the verification scripts. Treat `chNN_lib.py`, `chNN_tNN.py`, `report_len.py`, `find_meta.py`,
  `verify_*.py`, `live_state.py`, `w03_crossings.py` as the real toolchain; the `patch_*.py` files are
  history, not tools.

---

## 8. Boundaries

**You may** read the source notes and exam-focus sheets, author or reword questions, run every local
gate, and propose a new bank split.

**You must not** publish (`sync` / `pull` / deploy) without telling him first — it changes what he
sees on his phone; weaken or bypass a gate to make a bank pass; invent a citation, a page number, or
a claim about what the doctor marked; or mark a chapter done because the JSON was written.

When something is a scope decision — dropping a section, changing a bank count, retargeting the
question total — **stop and ask.** He calls those *"قرار مصيري"* and he wants to make them himself.
