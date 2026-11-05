# Handoff — ASE chapter question banks (Codex)

> **Read this before writing any `Quiz_*.json` under
> `01_Semester_1/04_Advanced_Software_Eng/07_Quizzes_&_Anki/`.**
>
> Written 2026-11-05 by Koko for a second agent (Codex or anything else) picking up the
> Advanced Software Engineering bank work. The **laws** live in
> `00_STUDIO_HUB/AGENT_HANDOFF_QUIZ_BANKS.md` — read that first, then this file, then
> `00_STUDIO_HUB/QUIZ_PUBLISH_RUNBOOK.md` for the gate→publish command sequence.
>
> This file is the **work stream**: what the student asked for, the method that produced the
> last seven chapters, the tooling, and the exact next steps.

---

## 1. What the student asked for, in his words

The work changed twice during one session, and the current rules are the ones he stated last.

**First ask (2026-11-04, evening).** He noticed the question counts were uneven across subjects
— *"ليش الاسئلة المولدة من 7 الى 10 بس والامن السيبراني توصل ل 16 و 14؟"* — and asked for a
**fairness investigation**. He wanted to know why the generated banks were thin while Cyber was
fat, and he was right to ask: the cause was not subject difficulty, it was that ASE had been built
from the official MCQ list only, while Cyber had been authored from prose.

**Second ask, after the investigation.** He ruled the old banks *"العينات"* (the samples) and set
the shape rule:

> **One bank per instructor vocabulary item. 8 to 16 questions each. The number is not sacred —
> it must be whatever the material honestly supports, and never below 8.**

He said this three times in a row because earlier banks had been given arbitrary counts. Do not
reintroduce a fixed number anywhere: **no "12 is the standard", no "one bank per topic".** If a
vocabulary block genuinely supports nine questions, write nine. If it supports sixteen, write
sixteen. If a block can only support five, that is a **gap to report, not a bank to ship**.

**Third ask.** ASE is a **three-unit course and it matters more than the cyber material** —
*"هذي هندسة يعني 3 وحدات يعني مهمة يعني مركزة وليس السايبر اهم منها ابدا"*. When in doubt,
depth beats speed on this subject.

---

## 2. The method that produced Ch01–Ch07

### 2.1 The instructor's vocabulary ledger is the scope — find it in the vector index

`00_STUDIO_HUB/indexes/04_Advanced_Software_Eng/ase_knowledge_vectors.sqlite3`
(4140 chunks; Ch03 alone has 299). Table `chunks` carries `chapter`, `source_title`, `content`.

```sql
-- the instructor's own scope ledger for a chapter
select page_label, content from chunks
where chapter = '3' and source_title like '%vocabulary%' order by page_label;
```

Those `vocabulary` chunks are the doctor's confirmed term list — the chapter boundary. Diff
those terms against the text of the existing banks and **every term with no coverage is a bank
you must write**. Doing this for Ch01 found 8 of 13 lecture-1 terms uncovered; for Ch03 it found
4 (brainstorming sessions, software prototyping, present state of practice, organisation of the
SRS). The index is a **scope-gap checker, not a question source** — never lift answers from it.

### 2.2 The official MCQ list is the spine; the prose packs fill the gaps

Each chapter folder under `03_Study_Notes/` holds `T1_MCQ.md` (official MCQs), `T2_Descriptive.md`,
`T3_Compare_Analyze.md`, `T4_Diagrams.md`, `T5_Apply_Select.md` and a `V*_Vocabulary_Coverage.md`.

`T1_MCQ.md` comes in two layouts — options on one line separated by `·`, or one option per line.
Parse both:

```python
blocks = re.split(r"### Q6\.(\d+)\.?\s*", text)[1:]
line = next(l.strip() for l in body.splitlines() if l.strip().startswith("(a)"))
if "·" in line:
    opts = [o[1] for o in re.findall(r"\(([a-d])\)\s*([^·]+)", line)]
else:
    opts = [o[1] for o in re.findall(r"^\(([a-d])\)\s*(.+?)\s*$", body, re.M)]
ans = re.search(r"^>\s*\*\*\(([a-d])\)", body, re.M)      # the printed key
```

The count of `### Q…` headings is the chapter's official pool: Ch02 25 · Ch03 35 (34 numbered,
Q3.25 absent) · Ch04 35 · Ch05 25 · Ch06 35 · Ch07 60 · Ch08 50 · Ch09 25.

### 2.3 Numeric and formula options are rewritten as words

L3 of the general handoff bans digits and LaTeX inside an option. Official items therefore need
rewording, not deletion — keep the tested fact, change the surface:

| Official option | Bank option |
|---|---|
| `V = N log₂ η` | "length times the base-two logarithm of the vocabulary" |
| `D = 1 / L` | "the reciprocal of level" |
| `DRE = E / (E + D)` | "errors found divided by errors found plus later defects" |
| `2 / 5 / 4 / 1` (FPA types) | "two types / three types / four types / five types" |
| `0.65 to 1.35` | "sixty five hundredths to one and thirty five hundredths" |

### 2.4 The builder assumes the CORRECT option is FIRST

This is the single most expensive trap in this workstream, and it is documented in
`AGENT_HANDOFF_QUIZ_BANKS.md` §3 — repeat it here because it cost three chapters.

```python
# items: (concept_id, bloom, q_en, q_ar, opts_en, opts_ar, exp_en, exp_ar)
# options are written with the CORRECT option at index 0; key_pattern rotates them into place
```

If you write the options in textbook order, the builder rotates them and the **published answer
letter no longer matches the intended option** — and **every gate still passes**, because the
gates measure length, never truth. It shipped 18 wrong answers on Ch02 before it was caught.

Always:

```python
CORRECT = {"ch5_best_coupling": "Data Coupling here", ...}

def put_correct_first(items):
    out = []
    for (cid, bl, qe, qa, oe, oa, ee, ea) in items:
        i = oe.index(CORRECT[cid])
        out.append((cid, bl, qe, qa, [oe[i]] + [x for j, x in enumerate(oe) if j != i],
                    [oa[i]] + [x for j, x in enumerate(oa) if j != i], ee, ea))
    return out
```

**Then spot-check the built JSON against the printed key** — read the built file back and confirm
the option at `answer` is the one the key names. A green gate is not evidence.

### 2.5 `rebalance()` — fix option length without breaking the shape

`scratch/ase_lib.py` carries the gates. The length helper lives in every build script
(`scratch/build_ase_ch0*.py`, `scratch/build_ase_ch07.py`):

```python
def rebalance(items):
    """Pad the shortest option until spread and band both sit in range."""
    for arr, sufs in ((oe, SE), (oa, SA)):
        for k in range(40):
            Ln = [len(x) for x in arr]
            band = Ln[0] / ((sum(Ln) - Ln[0]) / 3)
            if max(Ln) / min(Ln) <= 1.25 and 0.92 <= band <= 1.09:
                break
            i = min(range(4), key=lambda j: len(arr[j]))
            arr[i] = arr[i] + sufs[k % len(sufs)]
        # break the "correct is uniquely longest" tell
        for _ in range(4):
            Ln = [len(x) for x in arr]
            if not (Ln[0] == max(Ln) and Ln.count(max(Ln)) == 1):
                break
            j = max(range(1, 4), key=lambda i: len(arr[i]))
            arr[j] = arr[j] + sufs[0]
            if not (0.90 <= Ln[0] / ((sum(Ln) - Ln[0]) / 3) <= 1.10):
                arr[j] = arr[j][:-len(sufs[0])]
                break
```

**Never run it bank-wide.** Applied to all 49 Data Mining banks in one pass it broke 31 of them
(options grew to 57 characters). Restrict it to the questions you just wrote. Note the padding
must be allowed to hit the **correct** option too — when the correct answer is the shortest, the
band never closes otherwise.

`balance_letters()` (same scripts) rotates options so no letter exceeds 32 % of a bank.

### 2.6 The META filter rejects ordinary English

L1 forbids a question from referring to its own handout. The filter over-fires on:

`the module` · `the source` · `the chapter` · `the handout` · `the course`
Arabic: `المصدر` · `المذكورة` · `المذكورة`

Reword, never disable the gate: `a module` · `the finished code` · `one unit` · `known`.
Some false positives only appear *after* `rebalance()` has appended a suffix — fix the string in
the build script and rebuild, do not patch the published JSON by hand.

---

## 3. Toolchain

```text
# gates
python -X utf8 90_Shared_Toolbox/tools/quiz_quality_gate.py --shape-gate <bank>.json
python -X utf8 90_Shared_Toolbox/tools/quiz_balancer.py --check --strict <bank>.json
python -X utf8 90_Shared_Toolbox/tools/quiz_authoring_audit.py 01_Semester_1/04_Advanced_Software_Eng

# state (the only place counts live)
python -X utf8 90_Shared_Toolbox/tools/quiz_bank_state.py           # regenerate
python -X utf8 90_Shared_Toolbox/tools/quiz_bank_state.py --check   # exits 1 on drift

# publish (see QUIZ_PUBLISH_RUNBOOK.md for the full sequence)
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 90_Shared_Toolbox/tools/portal_content.py sync
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 90_Shared_Toolbox/tools/portal_content.py pull
CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 scratch/verify_vault_vs_live.py
cd C:/Users/gokoq/mcq-portal && CODEBUDDY_SAFE_DELETE_ENABLED=0 python -X utf8 tools/release.py patch --note "..."
node "C:/Users/gokoq/AppData/Local/npm-cache/_npx/67eb4586ca667318/node_modules/vercel/dist/vc.js" --prod --yes
```

Build scripts live in `scratch/` — `build_ase_ch01_extra.py` · `build_ase_ch02_t05.py` ·
`build_ase_ch03_t05.py` · `build_ase_ch04.py` · `build_ase_ch05.py` · `build_ase_ch06.py` ·
`build_ase_ch07.py`, plus `rebuild_ase_ch02.py` and `rebuild_ase_ch04.py` which **redistribute**
existing questions into per-vocabulary banks without rewriting them. `scratch/ase_lib.py` holds the
gates; `scratch/ch02_mcq.json`, `ch03_mcq.json`, `ch04_mcq.json`, `ch05_mcq.json`, `ch06_mcq.json`,
`ch07_mcq.json` hold the parsed official pools.

---

## 4. Current state and publication record

Live bank counts, chapter coverage, question totals, content version, shell version, and measured
quality gates are recorded only in the generated `00_STUDIO_HUB/QUIZ_BANK_STATE.md`. Do not copy
those values into this handoff. Use `quiz_bank_state.py --check` to verify that generated state
matches the vault and live portal.

### Chapter 4 draft — 2026-11-05

- The local Chapter 4 MCSQuiz banks have been rebuilt as concise formula, model-meaning, assumption, distinction, and key-note MCQs, following the student's instruction not to turn them into long numerical-result exercises.
- The Chapter 4 shape/anti-padding gate, strict per-bank schema and balance checks, strict authoring audit scoped to these banks, canonical publish dry run, and generated bank-state drift check passed.
- Scope mapping and source limitations are recorded in `01_Semester_1/04_Advanced_Software_Eng/07_Quizzes_&_Anki/Ch04_Bank_Coverage_Audit.md`. The source set in the vault has no doctor-annotated Chapter 4 copy.
- This is still a local draft. Do not run content sync, pull, deploy, or commit the Chapter 4 release until the student reviews and authorizes publication.

### Publication follow-up after student approval — 2026-11-05

- The student approved publication after reviewing the Chapter 4 coverage summary. A live handout scan then caught technical Arabic uses of “source” inside software terminology; those few phrases were clarified in the builder, the banks were rebuilt, and the scoped strict gates passed again.
- Published the corrected Chapter 4 content globally and refreshed the local portal mirror. The service-worker precache list was already current, so a shell release and deployment were unnecessary.
- The live vault comparison found no question or Arabic-option differences; the live keyed-answer, stem, and explanation audit found no mismatches; and the live handout-reference scan found none.
- Production browser review confirmed the Chapter 4 catalogue entries, quiz launch, Arabic/English toggle, and question/option reshuffling across launches. The generated bank-state snapshot was regenerated and its drift check passed.
- Coverage and source limits are documented in `01_Semester_1/04_Advanced_Software_Eng/07_Quizzes_&_Anki/Ch04_Bank_Coverage_Audit.md`. The scoped release commit and push are complete; the shared session log records the remote revisions.

### Chapter 5 replacement published — 2026-11-05

- Prepared a vocabulary-aligned bilingual question set using the Chapter 5 scope ledger, the source map, course MCQs, descriptive/compare packs, and the Aggarwal–Singh course text and companion slides. Questions stay concise and conceptual; no long numeric-result exercises were introduced.
- The coverage pass includes the supplementary material gaps identified in the source map: fan-in/fan-out, the structural/procedural layer distinction, information hiding, logical cohesion/control coupling, design review, OO class quality, and inheritance without polymorphic overriding.
- The student explicitly approved replacing the old Chapter 5 set. The approved review sheet is `01_Semester_1/04_Advanced_Software_Eng/07_Quizzes_&_Anki/Ch05_Draft_Review.md`; evidence and source limits are in `Ch05_Bank_Coverage_Audit.md`.
- The active schema-v2 banks match the instructor vocabulary coverage map. All Chapter 5 structural, shape, anti-padding, strict schema, key-balance, authoring-audit, portal-schema, and publish dry-run gates passed. The generated bank-state drift check passed.
- The previous active banks were moved to `_retired/` and hidden from the portal. The replacement content was synced globally, then pulled into the bundled portal mirror and offline precache.
- A direct live audit compared stems, bilingual options, keyed answers, explanations, concepts, and Bloom levels with the vault. It found no mismatches, meta references, or visible retired Chapter 5 rows.
- Production browser checks confirmed the chapter catalogue, quiz launch, translation toggle, question/option reshuffling, and stable correct-answer text. The offline check confirmed the new shell cache and Chapter 5 quiz launch with the network unavailable.
- Portal CI completed with no failures; the production deployment is available at https://mcq-portal-jade.vercel.app. The published vault and portal mirror hold the scoped source changes.

---

## 5. Deferred to the future — student decision 2026-11-05

> **The student said, verbatim: "لا تبني شي — سويها بالهاندوف ضيفها كاشياء مستقبلية."**
> Ch08 and Ch09 are **not** to be banked now. They are recorded here as future work only.
> Do not create a single `Quiz_Ch08_*.json` or `Quiz_Ch09_*.json` until the trigger below fires.

### 5.1 ASE Ch08 — Software Testing — **FUTURE / DO NOT BUILD YET**

- **Status:** study notes complete; **portal banks do not exist and must not be created now.**
- **Why deferred:** `V8_Predictive_Vocabulary.md` is marked
  `STATUS: PREDICTIVE — NOT CONFIRMED BY THE INSTRUCTOR`. Banking an inferred scope would bake a
  guess into 8+ banks.
- **Already done (do not redo):** `T1_MCQ` (50 official MCQs 8.1–8.50, printed key on p. 499),
  `T2_Descriptive`, `T3_Compare_Analyze`, `T4_Diagrams`, `T5_Apply_Design`, `T7_Calculations`,
  `V8_Coverage.md`, and `Ch08_Complete_Print_Pack.pdf` (97 pages). Six predictive sections (A–F)
  are mapped in `V8_Predictive_Vocabulary.md`.
- **Resume trigger:** Dr. Ali Fahim supplies the real Ch08 vocabulary → reconcile against V8 →
  build **one bank per confirmed block, 8–16 questions each**, with the 50 official MCQs as the
  spine and generated questions filling only genuine gaps.
- **If the list never arrives:** leave Ch08 bankless and say so. Never infer scope.

### 5.2 ASE Ch09 — Software Maintenance — **FUTURE / DO NOT BUILD YET**

- **Status:** study notes complete; **no portal banks, and none to be created now.**
- **Why deferred:** `V9_Predictive_Vocabulary.md` is predictive and unconfirmed.
- **Already done:** six packs authored/exported (combined print PDF, 42 pages); `T1_MCQ` holds the
  25 official MCQs 9.1–9.25 (printed key pp. 499–500); nine predictive sections are mapped in
  `V9_Predictive_Vocabulary.md`.
- **Source fix to preserve:** slide 28 prints `10 × 90 = 90 PM`; the scan (p. 472) says `900 PM`,
  total `1500 PM` — use the scan, not the slide.
- **Resume trigger:** confirmed Ch09 vocabulary arrives → same one-bank-per-block build.

> **Git note:** both `03_Study_Notes/Ch08_Software_Testing/` and `Ch09_Software_Maintenance/` are
> currently **untracked** (~8.5 MB and ~64 MB). The bulk of Ch09 is QA render/audit intermediates
> (`source_visual_audit/` 29 MB, `Ch09_QA_expanded_v1/` 22 MB, `Ch09_QA_final_v1/` 9.5 MB). Commit
> the **source** — the `T*_*.md`, `T*_*.pdf`, `V9_*`, `00_INDEX.md`, `BUILD_PLAN`, build scripts and
> `diagrams/` — and skip the render folders. That is preserving finished work, not a new build.

### 5.3 Remaining work that is NOT deferred

1. **Restructure Ch01 into one bank per instructor vocabulary item**, the way the completed
   chapter sets are organized. Ch01's ledger is in
   `03_Study_Notes/Ch01_Introduction/V1_Vocabulary_Coverage.md`; use the chapter plan and index
   to verify its scope before building.
2. **Soft Computing** is done but was **merged rather than restructured** — legacy banks were
   retired and their unique questions moved into the topic banks, after checking for semantic
   duplicates by hand. The machine check only catches lexical overlap
   (Jaccard ≥ 0.60); `fuzzy_union_max` vs `c4_union_max` and `de_morgan_law` vs `c4_de_morgan`
   were duplicates that only a human reading would catch. **Do that read.**
3. **AI** is deliberately below the agreed floor at the student's instruction. Leave it unless
   he says otherwise.

---

## 6. Boundaries for the delegated agent

**May:** read the source notes, the vocabulary ledger and the index; author or reword stems,
options and explanations; write new banks; restructure existing banks by topic; run the local
gates; report gaps.

**Must not:**
- publish (`sync` / `pull` / deploy) without saying so — it touches what students read;
- weaken or bypass a gate to make a bank pass — fix the wording instead;
- invent a citation, a page number, or a claim about what the doctor marked; tag guesses
  `[Foundational Knowledge / Standard Concept]`;
- invent a question whose answer you cannot source — an authored question is fine, an
  unsourceable *answer* is not;
- **delete a legacy bank before its unique questions have been moved** — the SC merge lost two
  questions to a semantic-duplicate check that ran after the delete;
- publish a chapter as done on the strength of the JSON existing: done means gates green, the live
  payload audited question by question, and `web_chapter_verify.js` passed against the live URL;
- bank Ch08 before the instructor confirms its scope.

---

## 7. The student, in his own rules

- **Zero-CLI.** He writes plain Iraqi Arabic and never runs a command. You run everything.
- **Correct him bluntly.** He asked for *"هاي غلط"*, not cushioning.
- **Never assume the work is finished.** End every block with *"هاي لو اكو بعد؟"*.
- **Recap at every transition.** Restate what is covered, what is solved, where you are.
- **The number is not sacred.** He said this three times. Do not re-fix a count.
- **Verify before asserting.** He has caught real errors; the standard is *verified*, not
  *probably fine*. Say *"سجل شغلك"* in the daily log when a chapter lands.
- **Never compress a source that is already condensed** without asking — depth is his call.
- **No fabricated deadlines.** Only what he reports.

---

*This file carries the work stream, not the whole law set. The laws stay in
`AGENT_HANDOFF_QUIZ_BANKS.md`; the live counts stay in `QUIZ_BANK_STATE.md`; the dated session
narrative stays in `.workbuddy-ai/memory/2026-11-04.md` and `2026-11-05.md`.*
