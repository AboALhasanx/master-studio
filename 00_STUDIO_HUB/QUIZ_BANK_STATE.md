# MCSQuiz — Bank State

> **AUTO-GENERATED — DO NOT EDIT BY HAND.**
> Source: `90_Shared_Toolbox/tools/quiz_bank_state.py`.
> Regenerate: `python -X utf8 90_Shared_Toolbox/tools/quiz_bank_state.py`
> Drift gate: `python -X utf8 90_Shared_Toolbox/tools/quiz_bank_state.py --check`
>
> This is the **only** place live bank numbers, chapter counts and versions are
> recorded. `ACTIVE_STATE.md`, `AGENT_HANDOFF_QUIZ_BANKS.md` and
> `QUIZ_PUBLISH_RUNBOOK.md` must point here, never copy numbers out of it.
> A table keyed only by `ChNN` is forbidden — every row carries its subject id.

> Generated at: 2026-11-04T19:24:47+03:00

## Current versions

| Thing | Value |
|---|---|
| Live content version | **62** |
| Portal shell `VERSION` | **1.10.6** |
| Live manifest source | Supabase content_manifest (live) |

> No git hash is recorded here on purpose: a commit would change it and make
> `--check` report a false drift. Hashes belong in commit messages and session
> logs, and must never be cited before they are on `origin/master`.

**Totals:** vault 162 banks / 1605 questions · live 162 banks / 1605 questions · MATCH

## By subject (vault = live)

| Subject | Chapters | Banks | Questions | Live banks | Live questions | Drift |
|---|---:|---:|---:|---:|---:|---|
| `01_Cyber_Security` | 6 | 59 | 709 | 59 | 709 | — |
| `02_English_Language` | 3 | 18 | 184 | 18 | 184 | — |
| `03_Data_Mining` | 8 | 55 | 512 | 55 | 512 | — |
| `04_Advanced_Software_Eng` | 3 | 6 | 30 | 6 | 30 | — |
| `05_Soft_Computing` | 5 | 20 | 150 | 20 | 150 | — |
| `06_Artificial_Intelligence` | 2 | 4 | 20 | 4 | 20 | — |

## By subject and chapter — measured quality gates

`refs` = questions naming the handout (must be 0). `long/short` = correct option is the
unique longest / shortest, EN then AR (cap 30% each). `fx` = options containing a
formula or backslash (must be 0). `spr` = option-length spread violations
(EN > 1.40, AR > 1.30). `local audit` is a measured snapshot, **not** a substitute for
`preflight.py N --strict` and `quiz_quality_gate.py --shape-gate`.

| Subject | Ch | Banks | Q | refs | long EN/AR | short EN/AR | fx | spr | local audit |
|---|---:|---:|---:|---:|---|---|---:|---:|---|
| `01_Cyber_Security` | 01 | 6 | 71 | 0 | 6/10 | 6/7 | 0 | 7 | needs work |
| `01_Cyber_Security` | 02 | 8 | 92 | 0 | 6/6 | 6/5 | 0 | 8 | needs work |
| `01_Cyber_Security` | 03 | 9 | 103 | 0 | 2/14 | 6/10 | 0 | 0 | clean |
| `01_Cyber_Security` | 04 | 9 | 118 | 0 | 18/15 | 17/15 | 0 | 0 | clean |
| `01_Cyber_Security` | 05 | 17 | 221 | 0 | 36/30 | 32/24 | 0 | 0 | clean |
| `01_Cyber_Security` | 06 | 10 | 104 | 0 | 18/16 | 12/12 | 0 | 0 | clean |
| `02_English_Language` | 01 | 6 | 53 | 0 | 4/0 | 6/0 | 0 | 0 | clean |
| `02_English_Language` | 02 | 6 | 63 | 0 | 9/0 | 2/0 | 0 | 0 | clean |
| `02_English_Language` | 03 | 6 | 68 | 0 | 7/0 | 4/0 | 0 | 0 | clean |
| `03_Data_Mining` | 01 | 5 | 35 | 0 | 5/3 | 4/1 | 0 | 0 | clean |
| `03_Data_Mining` | 02 | 7 | 69 | 20 | 10/14 | 9/7 | 0 | 0 | needs work |
| `03_Data_Mining` | 03 | 7 | 55 | 16 | 8/11 | 5/5 | 0 | 0 | needs work |
| `03_Data_Mining` | 04 | 4 | 40 | 0 | 5/1 | 5/6 | 0 | 0 | clean |
| `03_Data_Mining` | 05 | 10 | 77 | 3 | 9/4 | 7/5 | 0 | 0 | needs work |
| `03_Data_Mining` | 06 | 7 | 86 | 1 | 9/6 | 8/10 | 0 | 0 | needs work |
| `03_Data_Mining` | 07 | 7 | 86 | 0 | 11/9 | 11/6 | 0 | 0 | clean |
| `03_Data_Mining` | 08 | 8 | 64 | 0 | 7/6 | 4/3 | 0 | 0 | clean |
| `04_Advanced_Software_Eng` | 01 | 2 | 10 | 3 | 8/4 | 0/1 | 0 | 13 | needs work |
| `04_Advanced_Software_Eng` | 02 | 2 | 10 | 1 | 5/2 | 0/3 | 0 | 4 | needs work |
| `04_Advanced_Software_Eng` | 05 | 2 | 10 | 0 | 8/4 | 0/1 | 0 | 2 | needs work |
| `05_Soft_Computing` | 01 | 3 | 18 | 4 | 2/4 | 2/2 | 0 | 0 | needs work |
| `05_Soft_Computing` | 02 | 3 | 20 | 1 | 2/1 | 0/2 | 0 | 0 | needs work |
| `05_Soft_Computing` | 03 | 4 | 32 | 0 | 1/3 | 1/0 | 0 | 0 | clean |
| `05_Soft_Computing` | 04 | 4 | 32 | 0 | 5/2 | 2/3 | 0 | 0 | clean |
| `05_Soft_Computing` | 05 | 6 | 48 | 0 | 3/7 | 1/4 | 0 | 0 | clean |
| `06_Artificial_Intelligence` | 01 | 2 | 10 | 0 | 3/0 | 2/1 | 0 | 2 | needs work |
| `06_Artificial_Intelligence` | 02 | 2 | 10 | 0 | 1/5 | 1/0 | 0 | 5 | needs work |

## What remains

- `01_Cyber_Security` Ch01 — 7 spread violations
- `01_Cyber_Security` Ch02 — 8 spread violations
- `03_Data_Mining` Ch02 — 20 handout refs
- `03_Data_Mining` Ch03 — 16 handout refs
- `03_Data_Mining` Ch05 — 3 handout refs
- `03_Data_Mining` Ch06 — 1 handout refs
- `04_Advanced_Software_Eng` Ch01 — 3 handout refs; 13 spread violations; answer-length tell
- `04_Advanced_Software_Eng` Ch02 — 1 handout refs; 4 spread violations; answer-length tell
- `04_Advanced_Software_Eng` Ch05 — 2 spread violations; answer-length tell
- `05_Soft_Computing` Ch01 — 4 handout refs
- `05_Soft_Computing` Ch02 — 1 handout refs
- `06_Artificial_Intelligence` Ch01 — 2 spread violations
- `06_Artificial_Intelligence` Ch02 — 5 spread violations; answer-length tell

**Not measured here (deliberate):** whether a chapter's source is annotated,
whether crossed-out material was excluded, and whether answers are factually
correct. Those need `W0N_Annotation_Map.md` and source review, not a counter.

