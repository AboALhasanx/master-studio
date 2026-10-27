# Agent Handoff — Cyber Security quiz banks (MCSQuiz)

> **Read this before touching any `Quiz_Ch*.json` in `01_Semester_1/01_Cyber_Security/07_Quizzes_&_Anki/`.**
> Written 2026-10-26 by Koko. It exists so a second agent (ChatGPT, Claude, anything) can work on the
> same banks without undoing what has already been decided. Every rule below was paid for by a real
> correction from the student — none of it is preference or style.
>
> **This file is the "what". The "how" — the exact command sequence from gate to publish, with
> expected output and failure meanings — is `QUIZ_PUBLISH_RUNBOOK.md` in this same folder. Read both
> before your first edit: this one first, the runbook second.**

---

## 1. What the system is

| Piece | Where | Role |
|---|---|---|
| Vault bank (master) | `01_Semester_1/01_Cyber_Security/07_Quizzes_&_Anki/Quiz_ChNN_TNN_*.json` | **The source of truth.** Schema v2. |
| Publisher | `90_Shared_Toolbox/tools/publish_quizzes.py` + `portal_content.py` | vault → Supabase, converts v2 → v3 |
| Live content | Supabase project `gywniovuupjmllbmjmai`, RPCs `content_manifest` / `content_bank` | what students actually read |
| App | `C:\Users\gokoq\mcq-portal` (Vercel: `mcq-portal-jade.vercel.app`) | PWA reader, schema v3 only |
| Mirror | `mcq-portal/data/` | offline fallback; refreshed by `portal_content.py pull` |

**v2 (vault) shape:** `question` · `question_ar` · `options` · `options_ar` · `options_en` · `answer` (`"A"`-`"D"`) · `correct` (0-3) · `explanation` · `explanation_ar` · `bloom_level` · `concept_id`.
**v3 (live) shape:** `stem {ar,en}` · `options [{ar,en}×4]` · `answer` **integer** · `explanation {ar,en}` · `bloom`. Never hand-edit the live shape; let the publisher convert.

---

## 2. The five laws. A bank that breaks any of them is not finished.

### L1 — A question must stand on its own
No reference to the handout, the lecture, the material, the chapter, the book, the course, or the
doctor. This is not about the word "ملزمة" — it is the whole class:

- naming the source: lecture · notes · booklet · handout · slides · material · source · text · book · course · module
- pointing at the document: *this chapter · this section · as we saw · as covered · as discussed*
- pointing at the person: *her rule · she said · her vocabulary · in her*
- Arabic: المحاضرة · الملزمة · الدكتورة · الشرائح · المصدر · الجابتر · المذكور · قاعدتها · قالت إن

> Wrong: *"Which techniques does the lecture list under confidentiality?"*
> Right: *"Which techniques enforce confidentiality?"*

Enforced at build time by `META_RE` in `scratch/ch0N_lib.py`, over **stem + both option lists + both explanations**.

### L2 — The answer must not be guessable from its shape
Measured, not felt. In the original Chapter 1 banks the correct option was the unique longest in
**43 %** and the unique shortest in **35 %** — a student picking the longest scored 43 % knowing
nothing. The `--strict` balancer does **not** catch this: it only bounds the correct option against
the *mean* distractor length, so an option can be the unique maximum and still pass.

Hard caps, **measured separately in English and Arabic** (the portal renders `options_ar`, so an
Arabic-only tell is still a tell):

| Metric | Cap | Chance |
|---|---|---|
| correct is the unique longest | ≤ 30 % of the bank | 25 % |
| correct is the unique shortest | ≤ 30 % of the bank | 25 % |
| correct ÷ mean(distractors) | 0.88 – 1.12 | 1.00 |
| max ÷ min option length | ≤ 1.40 | — |

### L3 — No formula, no worked step, no LaTeX inside an option
A formula makes that option visually different, so it is answerable by shape. For compute questions
the stem carries the numbers and every option is a bare value of equal width:

> Right: `200` · `240` · `160` · `100`   |   `0.90` · `0.80` · `0.60` · `0.75`
> Wrong: *"The calculated value is 0.15, from 1 minus 0.85."*

The arithmetic belongs in `explanation`.

### L4 — One fact, one question
The student's phrase: *«كل شوية عايدها»*. The recurring defect is a five-item list asked fifteen
ways. Chapter 2's T05 spent 15 questions on the five analysis frameworks (description, acronym,
scenario, comparison); T04 spent 6 on the same five strategies. A list gets **one** question naming
it, plus at most two application questions — not one per row.

### L5 — Plain language, weighted by the doctor's marking
Stems are one sentence. No *"Which statement represents the canonical formal definition provided in
the lecture?"* No philosophical stems (*"Why does the lecture insist…"*). Distractors must be
plausible members of the same family — other regulations, other domains, other techniques — never
nonsense (*"Maritime cargo container customs tariff valuation"*, *"UNESCO heritage sites"*).

Weight follows the doctor's own highlight map, not an even split. Read
`03_Study_Notes/W0N_Exam_Focus.md` and `W01_Annotation_Map.md` first: yellow = memorise the list,
red = be able to explain, coloured text = the taxonomy.

---

## 3. Toolchain

```text
90_Shared_Toolbox/tools/quiz_balancer.py <file> --check --strict     # length mean + key spread
90_Shared_Toolbox/tools/publish_quizzes.py --dry-run                 # v2+v3 validation, all banks
90_Shared_Toolbox/tools/portal_content.py sync                       # publish to Supabase
90_Shared_Toolbox/tools/portal_content.py pull                       # refresh local mirror
90_Shared_Toolbox/tools/qa/web_chapter_verify.js                     # live-site checks
```

```text
SUBJECT=01_Cyber_Security CHAPTER=2 QUIZ=<full quiz_id> EXPECT=<bank count> \
PORTAL_URL=https://mcq-portal-jade.vercel.app node .../web_chapter_verify.js
```

Release: `python tools/release.py patch --note "..."` then `tools/ci.py` (**system Python312**, not
the managed interpreter) then deploy. Deploy with the cached CLI, not npx:
`node "C:/Users/gokoq/AppData/Local/npm-cache/_npx/69f9afb961c37556/node_modules/vercel/dist/vc.js" --prod --yes`.

### Builders (the reason chapters 1–2 are clean)

`scratch/ch01_lib.py` and `scratch/ch02_lib.py` hold the gates and are the template:

```python
build(quiz_id, topic_en, topic_ar, items, key_pattern)
# items: (concept_id, bloom, q_en, q_ar, opts_en, opts_ar, exp_en, exp_ar)
# options are written with the CORRECT option at index 0; key_pattern rotates them into place
```

They enforce L1, L2, L3 and cross-bank `concept_id` uniqueness against **every other bank in the
vault**, then print the key distribution. Copy one for the next chapter; do not weaken a gate to make
a bank pass — fix the wording.

`scratch/report_len.py <builder>.py` prints EN and AR option lengths and flags for a builder
**without writing the bank**. Use it to converge in one pass instead of five.

---

## 4. What is done, and what is not

| Chapter | Questions | State |
|---|---|---|
| Ch01 | 71 in 6 banks | rewritten 2026-10-26 · L1–L5 clean · live |
| Ch02 | 69 in 7 topic banks | rebuilt from Week 02 source 2026-10-27 · strict/shape/schema gates green · live; old Model A/B archived and hidden |
| Ch03 | 55 in 7 topic banks | rebuilt from Week 03 source 2026-10-27 · strict/shape/schema gates green · live; old Model A/B archived and hidden |
| Ch04 | 118 in 9 banks | cleaned 2026-10-27 · gates green · live · web verification passed |
| Ch05 | 221 in 17 banks | cleaned 2026-10-27 · strict/shape gates green · live · web verification passed |
| Ch06 | 104 in 10 banks | rebuilt 2026-10-27 · old 8 banks hidden · live · web verification passed |

Current content version: **52** · shell **1.7.12**.

> **Chapter 3 was a scope problem before it was a wording problem.** The doctor's marked copy exists
> only outside the vault (`~/Downloads/Telegram Desktop/W02_Risks.pdf`; the clean
> `02_Raw_Materials/W03_Risks.pdf` has zero annotations). Ten of its fourteen pages carry red
> strike-throughs, and whole sections are dead — the cost-of-controls section, the policy-versus-
> technology section, the core-functions section, and the entire hospital quantification scenario and
> PCI worked example. Read `03_Study_Notes/W03_Annotation_Map.md` before writing a single question, or
> you will author questions on material she explicitly removed.

---

## 5. Boundaries for a delegated agent

**May:** read the source notes and exam-focus sheets; author or reword stems, options and
explanations; run the local gates; run `report_len.py`; propose a new bank split.

**Must not:**
- publish (`sync` / `pull` / deploy) without saying so — those touch what students see;
- weaken or bypass a gate to make a bank pass;
- invent a citation, a page number, or a claim about what the doctor marked — tag guesses
  `[Foundational Knowledge / Standard Concept]` instead;
- mark a chapter done because the JSON was written. Done means: all gates green, **and** the live
  payload audited question by question, **and** `web_chapter_verify.js` passed against the live URL;
- assume a formula or a figure is correct because it looks right. Chapter 1's `S = F × K` and
  `R = S / M` were confirmed against the book; the ISO "14 categories" line is 2013 structure, not
  2022 (2022 = four themes, 93 controls).

**Before claiming a pass, test the validator itself.** Two bugs in the L1 gate were only found by
running it against known-good text: a stray leading `|` created an empty alternative that matched
every string, and `قالت` matched inside `استقالته`. A validator that has not been tested on valid
input is not evidence.

---

## 6. The student, in his own rules

- **Zero-CLI.** He writes plain Iraqi Arabic and never runs a command. The agent runs everything.
- **Correct him bluntly.** He asked for *"هاي غلط"*, not cushioning.
- **Never assume the work is finished.** End every block with *"هاي لو اكو بعد؟"*.
- **Verify before asserting.** He has caught real errors; the standard is verified, not probably fine.
- **Never compress a source that is already condensed** without asking — depth is his call.
- **No fabricated deadlines.** Only what he reports.

---

*Keep this file current: when a chapter is cleaned, update §4 and the content version.*


### MCSQuiz — Ch4/Ch5 publish and Ch6 replacement cleanup (Codex, 2026-10-27)

- Replaced the 9 Ch4 / 17 Ch5 active vault banks with the preflighted candidates: Ch4 118 questions, Ch5 221. Preserved all 26 prior active JSON files under `07_Quizzes_&_Anki/_retired/ch04-ch05-prepublish-2026-10-27/`; SHA256 matched every installed candidate to its source.
- Candidate and active-path preflights passed: handout-reference scan, answer-shape/option-spread quality gate, strict balancer, v2/v3 schema, and local publish dry-run. Live Ch4 structural audit: 118 questions, 0 problems. Ch5 live manifest: 17 banks / 221 questions. Arabic options in all 26 Ch4/Ch5 live banks match the vault as multisets (0 diffs).
- `sync --subject 01_Cyber_Security` intentionally does not retire missing banks. It also upserted the 10 cleaned Ch6 banks while leaving 8 superseded Ch6 rows visible. Hid those exact 8 old IDs, then pulled again: Cyber Security now has 59 live banks across Ch1–Ch6; Ch6 has 10 banks / 104 questions, 104 unique concepts, and 0 structural problems.
- Updated the portal shell to **1.7.10** after the final mirror/précache change. CI passed (220 checks, 0 failures); production deployment is READY at `https://mcq-portal-jade.vercel.app`.
- Live web verification passed for Ch4 (9 cards), Ch5 (17), and Ch6 (10): topic numbering, card counts, subject tags, English toggle, per-launch question/option shuffle, and stable correct-answer text. Ch4/Ch5 JSON and the Ch6 retired copies remain preserved. No `ACTIVE_STATE.md` edit.
