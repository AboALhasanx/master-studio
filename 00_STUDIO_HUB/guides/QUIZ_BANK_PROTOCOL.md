# Quiz Bank Protocol (MCSQuiz content)

> **Scope:** how any harness (OpenCode, WorkBuddy, Codex, MiMo, Antigravity, FreeBuf, …) authors and publishes question banks for the MCSQuiz PWA. Read this **before** writing or editing anything under `01_Semester_1/<Subject>/07_Quizzes_&_Anki/`. The vault is the master; Supabase is the content portal in the middle; the app is the reader.

**ملخص عربي:** هذا البروتوكول يحدد كيف تُكتب بنوك الأسئلة: الملفات في المجلد `07_Quizzes_&_Anki` بصيغة v2، والجابتر إما نموذجان (أ/ب) أو بنوك مواضيع مرقمة، والأسئلة عربية أولاً مع الإنجليزية، ومصدرها ملاحظات المادة، وتُفحص بأدوات `quiz_balancer` و`portal_content` قبل النشر.

## 1. Boot and coordinate

1. Read `00_STUDIO_HUB/ACTIVE_STATE.md`, `HARNESS_REGISTRY.md`, today's `sessions/YYYY-MM-DD.md`, and this file. Sign in by name before editing (root `AGENTS.md` §8).
2. Read `00_STUDIO_HUB/guides/PORTAL_PUBLISH.md` for the publishing mechanics — this file governs **what a question is**, that file governs **how it ships**.
3. One shared map, no private copies: the live truth is `python 90_Shared_Toolbox/tools/portal_content.py status` plus `01_Semester_1/*/07_Quizzes_&_Anki/`. Do not create `Quiz_*_v2.json`, `_new.json`, or per-harness variants.
4. When you find another harness's bank, name it with the date (*"found work from OpenCode 2026-10-21, left intact"*) and do not silently rewrite it. Fixing a factual error is allowed — say so in the session log and in the commit message.
5. Handing the work to a model outside the vault (Gemini, another chat model): give it `00_STUDIO_HUB/handoffs/GEMINI_QUIZ_HANDOFF.md` and the matching prompt from `00_STUDIO_HUB/handoffs/GEMINI_QUIZ_PROMPT.md`. It writes the bank (or prints the JSON); the receiving vault agent runs the gates, publishes, and mirrors.

## 2. Where a bank lives, and what it is called

```
01_Semester_1/<Subject>/07_Quizzes_&_Anki/Quiz_<ChNN>_(Model<A|B>|T<NN>)_<Slug>.json   <- master (schema v2)
        |
        |  portal_content.py sync      (validate -> merge -> publish)
        v
Supabase content_banks (payload = schema v3)  ->  the app + its offline cache
        |
        |  portal_content.py pull      (mirror back into mcq-portal/data + SW list)
        v
mcq-portal/data/banks/*.json   (the bundled fallback that ships with the shell)
```

| rule | value |
|---|---|
| file name | model: `Quiz_Ch<NN>_Model<A\|B>_<Slug>.json` (e.g. `Quiz_Ch03_ModelA_Feature_Extraction.json`); topic: `Quiz_Ch<NN>_T<NN>_<Slug>.json` (e.g. `Quiz_Ch01_T03_CIA_Triad_and_Utility_Function.json`) — never mix the two shapes in one chapter without asking the student first |
| `quiz_id` | identical to the file stem |
| chapter number | taken from `Ch<NN>` in the name; legacy ids (`Quiz_01_…`) keep the chapter recorded in `mcq-portal/data/index.json` |
| models per chapter | either **exactly two models** («النموذج أ», «النموذج ب») **or** a run of **numbered topic banks** (`T01`, `T02`, …) that tile the chapter's sections in ملزمة order — never a Model A next to a T-bank for the same material | 
| `topic` / `topic_ar` | model banks end with `— Model A` / `— النموذج أ` (`B` / `ب`); **topic banks carry a plain title with no suffix** (e.g. `ثالوث CIA ودالة المنفعة الأمنية U(C,I,A) والتقنيات المعيارية`) | 
| title hygiene | **never repeat the subject name** in `topic_ar` — the card already shows the subject chip, and the app adds the `موضوع: N` badge itself. `التعريف، النطاق، والتطور التاريخي` ✓, `الأمن السيبراني: التعريف…` ✗ |
| retired bank | move the file to `07_Quizzes_&_Anki/_retired/` (never delete), then `hide`/remove its portal row and say so |

Chapter numbers are the **book's** chapter numbers, not a running counter: Advanced Software Engineering legitimately uses 1, 2, 5 — a gap is correct, not a bug.

## 3. Subjects, instructors, sources

| subject_id | app title | instructor (Arabic / English) | read the material from |
|---|---|---|---|
| `01_Cyber_Security` | الأمن السيبراني | أ.م.د. هدى لفتة مجيد / Asst. Prof. Dr. Huda Lafta Majeed | `03_Study_Notes/W0x_*` |
| `02_English_Language` | اللغة الإنجليزية | أ.م.د. حيدر عكاب علوان / Asst. Prof. Dr. Haidar Akab Alwan | `03_Study_Notes/Unit_0x_*` |
| `03_Data_Mining` | تنقيب البيانات | أ.م.د. أحمد شاكر عبد الرضا / Asst. Prof. Dr. Ahmed Shakir Abd Al-Rida | `03_Study_Notes/Week_0x_*` |
| `04_Advanced_Software_Eng` | هندسة البرمجيات | أ.م.د. علي فاهم نعمة / Asst. Prof. Dr. Ali Fahim Ni'ma | `03_Study_Notes/Week_0x_*`, `Ch0x_*` |
| `05_Soft_Computing` | الحوسبة اللينة | أ.د. عبد الهادي محمد ادخيل / Prof. Dr. Abdul Hadi Mohammed Adkhil | `03_Study_Notes/W0x_*` |
| `06_Artificial_Intelligence` | الذكاء الاصطناعي | أ.د. سيف علي السعيدي / Prof. Dr. Saif Ali Al-Saidi | `03_Study_Notes/W0x_*`, `AI_W0x_*` |

- Copy the instructor pair and `subject_title` from an existing bank of the same subject (or `00_Doctor_Profile.md`). The portal's Arabic title (from `mcq-portal/data/index.json`) is what the app shows; a bank's own title is only a fallback.
- The source of a question is the subject's own study notes (and the named lecture/textbook they came from). **If a fact is not in a source, pick another fact** — never invent a definition, a number, an author, a page or a DOI (root `AGENTS.md` §2.1).

## 4. Schema v2 — the master file (what you write)

Required top-level keys: `schema_version: 2`, `subject_id`, `subject_title`, `semester: 1`, `semester_label: "كورس أول"`, `quiz_id`, `topic` (English), `instructor_ar`; plus the usual `topic_ar`, `instructor`, `subject`.

Every question object:

| key | rule |
|---|---|
| `id` | `q1`, `q2`, … renumbered from 1 inside each bank |
| `concept_id` | `snake_case`, the one idea the question tests; **unique inside the bank and across the chapter's two models** |
| `bloom_level` | one of `Remember`, `Understand`, `Apply`, `Analyze`, `Evaluate`, `Create` |
| `question` / `question_ar` | English + Arabic stem, both non-empty |
| `options` / `options_en` | the same 4 English options |
| `options_ar` | the same 4 options in Arabic, same order |
| `answer` | `A`–`D` |
| `correct` | `0`–`3`, and `"ABCD"[correct] === answer` (the validator fails otherwise) |
| `explanation` / `explanation_ar` | why the key is right **and** why the distractors are wrong, 1–3 sentences each |

```json
{
  "schema_version": 2,
  "subject_id": "06_Artificial_Intelligence",
  "subject_title": "الذكاء الاصطناعي",
  "semester": 1,
  "semester_label": "كورس أول",
  "quiz_id": "Quiz_Ch01_ModelA_AI_Foundations",
  "topic": "AI Foundations — Model A",   // topic banks: plain title, no suffix
  "topic_ar": "أسس الذكاء الاصطناعي: الوكلاء والبيئات والمهام — النموذج أ",
  "instructor_ar": "أ.د. سيف علي السعيدي",
  "instructor": "Prof. Dr. Saif Ali Al-Saidi",
  "subject": "06_Artificial_Intelligence",
  "questions": [
    {
      "id": "q1",
      "concept_id": "turing_test_acting_humanly",
      "bloom_level": "Understand",
      "question": "The Turing Test is the standard operational measure for which of the four historical definitions of AI?",
      "question_ar": "اختبار Turing هو المقياس العملي المعياري لأي من التعريفات التاريخية الأربعة للذكاء الاصطناعي؟",
      "options": ["Acting rationally", "Thinking humanly", "Thinking rationally", "Acting humanly"],
      "options_ar": ["التصرف بعقلانية", "التفكير كإنسان", "التفكير بعقلانية", "التصرف كإنسان"],
      "options_en": ["Acting rationally", "Thinking humanly", "Thinking rationally", "Acting humanly"],
      "answer": "D",
      "correct": 3,
      "explanation": "The test judges visible behaviour in a conversation, which places it in the acting-humanly family; the rational-thinking family rests on the laws of thought and says nothing about dialogue.",
      "explanation_ar": "الاختبار يحكم على السلوك الظاهر في الحوار، لذلك ينتمي إلى عائلة التصرف كإنسان؛ أما التفكير بعقلانية فيقوم على قوانين الفكر ولا يفحص الحوار."
    }
  ]
}
```

**Size:** agreed with the student first (see §0) — 5 is a normal drill, 10–15 when the material is rich, 16 for a ملزمة-section topic bank. The whole bank must stay playable in one sitting.

## 5. Schema v3 — generated, never hand-written

`portal_content.py sync` converts v2 → v3 (`topic/stem/explanation: {ar,en}`, `options: [{ar,en}]×4`, integer `answer`, `has_math`). You never edit the Supabase payload by hand, and you never write v3 into the vault. The app reads v3 only.

## 6. Writing rules (content)

- **Arabic-first, English technical.** Arabic is Modern Standard, natural, no dialect. Standard technical terms stay in clean English inside the Arabic sentence — `Fuzzy Set`, `Waterfall`, `UCS`, `Feature Selection` — with **no parenthetical echo** (`المجموعات الضبابية (Fuzzy Set)` ✗).
- **RTL arrow:** inside an Arabic line a "leads to" arrow is `←`; inside an English line it is `→`.
- **Source fidelity:** if the source states a list, the question/answer keeps a list; a heading stays a heading; a formula stays a formula.
- **The stem asks one thing.** No "all of the above", no "both A and C", no negative trick wording, no double negatives.
- **Distractors are plausible and same-shaped:** each is a real misconception or a neighbouring concept, within ±25 % of the correct option's length. The correct option must never be the longest, the most qualified, or the only one with a technical term.
- **Explanations teach:** the correct answer's reason, then the specific flaw of each distractor. Cite the mechanism, not "the lecture says so".
- **Language of the English subject:** keep the English items in English in `options_ar` (translating a vocabulary option gives the answer away); only the instruction and the explanation are Arabic.
- **Math:** `$x$` inline, `$$…$$` for display, KaTeX renders it. **No Arabic inside math** — it would render as symbols. Prefer one clear formula over three decorative ones.

## 7. Psychometric rules (the gate that fails most often)

| bank size | answer-key rule |
|---|---|
| ≥ 10 questions | no letter may exceed **32 %** of the keys |
| exactly 5 | every letter appears at least once, none more than twice (2/1/1/1) |

- Option-length parity: the correct option's length must stay within **1.30×** the average distractor length (target ±25 %); fix it by rewriting distractors, not by padding the correct one.
- `concept_id`s must be unique across **every bank of the chapter** (A+B, or T01…T0N) — never test the same idea twice in one chapter.
- Split rule, model chapters: alternate the questions (`0,2,4…` / `1,3,5…`) so both models cover the whole chapter. Split rule, topic chapters: one bank per ملزمة section, in ملزمة order (`T01`, `T02`, …), each covering only its section.

## 8. The mandatory gates (run them, paste the output)

```bash
cd C:\Users\gokoq\Master-Studio

# 1) balance the answer key — this WRITES the file, run it once after writing
python "90_Shared_Toolbox/tools/quiz_balancer.py" "01_Semester_1/<Subject>/07_Quizzes_&_Anki/<file>.json"

# 2) the strict gate, read-only — must exit 0 for every file
python "90_Shared_Toolbox/tools/quiz_balancer.py" "01_Semester_1/<Subject>/07_Quizzes_&_Anki/<file>.json" --check --strict

# 3) schema v2 + portal v3 (both error lists must be empty)
python -c "import sys,json,io; sys.path.insert(0,r'90_Shared_Toolbox/tools'); from quiz_balancer import validate_schema_v2; sys.path.insert(0,r'C:\Users\gokoq\mcq-portal\tools'); import portal_schema as ps; p=r'<file>'; b=json.load(io.open(p,encoding='utf-8')); print(validate_schema_v2(b), ps.validate_v3(ps.to_v3(b)))"
```

`--check` is the only read-only mode: `--strict` on its own runs the gate **and then balances and saves**, so it is not a way to "just look". Re-balancing an already-balanced bank reshuffles the option order (the content stays valid, but the file changes and the next `sync` bumps its version) — so audit with `--check`, and balance only when you mean it.

**After the balancer permutes options, re-open the file and re-check every `answer`/`correct` pair** — the intended correct text must still be the key (the tool keeps them aligned, but a hand-written `answer` that disagrees with `correct` is the single most common defect).

If `--strict` exits 1: read the flagged question, lengthen the short distractors (or shorten the correct option) to match, and re-run until exit 0. Never deliver a bank that fails the gate.

## 9. Publish

```bash
# what is live right now (version, chapters, counts)
python "90_Shared_Toolbox/tools/portal_content.py" status

# publish everything that changed (validate -> merge -> upsert -> version -> log)
python "90_Shared_Toolbox/tools/portal_content.py" sync
python "90_Shared_Toolbox/tools/portal_content.py" sync --subject 03_Data_Mining

# keep a bank out of the app (draft) and put it back
python "90_Shared_Toolbox/tools/portal_content.py" hide  Quiz_Ch02_ModelA_Data_Types_and_Preparation
python "90_Shared_Toolbox/tools/portal_content.py" show  Quiz_Ch02_ModelA_Data_Types_and_Preparation

# refresh the bundled offline fallback + the service worker precache list
python "90_Shared_Toolbox/tools/portal_content.py" pull

# optional: post the Telegram notice
python "90_Shared_Toolbox/tools/portal_content.py" sync --notify
```

- **Content needs no deploy.** The next visit pulls the new manifest; the bell shows the unread count.
- **`pull` is not optional bookkeeping:** it rewrites `mcq-portal/data/*` and refreshes the worker precache list. The cache name follows the release `VERSION` (`mcq-portal-<version>`), so a precache change takes effect with the next `tools/release.py` bump — deploy the shell once after that:
  `cd C:\Users\gokoq\mcq-portal; npx -y vercel@latest --prod --yes`
- Writes only ever happen from the agent, with the service key fetched at run time. The browser can only read.

## 10. Verify in the app (not only in the JSON)

1. Open the app (or a headless browser): the subject chips must list the subject, the chapter bar must list **each chapter number once, plain** (`1`, `2`, … — never `1.1`), and selecting a chapter must show its cards each carrying the app-rendered **`موضوع: N` badge** («النموذج أ» before «النموذج ب» where models exist).
2. Start the new quiz **twice** and confirm the question order **and** the option order differ between runs while the correct-answer **text** stays the key (per-launch Fisher–Yates with key remap — the stored key is only the intent). Then answer one question, confirm the explanation renders (KaTeX included) and that the **translation-icon toggle** (yellow = Arabic, plain = English) translates stem, options and explanation.
3. Offline: the new chapter must open with the network off (portal → cached manifest → bundled fallback).
4. Report the evidence: the exact commands and their output, plus what you saw in the app.

## 11. Current map (snapshot — refresh it when you add a subject or a chapter)

| subject | chapters (shape) | banks | questions |
|---|---|---|---|
| الأمن السيبراني | 1 = 6 topics (T01–T06), 2 = أ/ب, 3 = أ/ب, 4 = أ/ب | 12 | 176 |
| اللغة الإنجليزية | 1 = أ/ب, 2 = أ/ب | 4 | 20 |
| تنقيب البيانات | 1 = أ + ModelB, 2 = أ/ب, 3 = أ/ب | 6 | 46 |
| هندسة البرمجيات | 1 = أ + ModelB, 2 = أ/ب, 5 = أ/ب | 6 | 30 |
| الحوسبة اللينة | 1 = أ + ModelB, 2 = 6q + ModelB | 4 | 22 |
| الذكاء الاصطناعي | 1 = أ/ب, 2 = أ/ب | 4 | 20 |
| **total** | 16 chapters | **36 banks / 314 questions** | content v12 |

`python 90_Shared_Toolbox/tools/portal_content.py status` is authoritative; if this table disagrees with it, fix the table.

## 12. Pitfalls that have actually happened

- **`answer` / `correct` drift** after the balancer or a manual edit → the validator's "Mismatch between 'correct' and 'answer'" error. Always re-check.
- **`--strict` is not read-only** — it balances and saves after the gate passes, and a second balancing pass reshuffles the option order. Audit with `--check --strict`; balance once, on purpose.
- **A bank that changed without meaning to** (a stray balance run) leaves the vault ahead of the portal: either re-run `sync` to publish the new order, or `git checkout --` the file to match what is live. Do not leave the two out of step.
- **Duplicated chapter chips** («1 1 2 2») when two banks share a chapter — the app de-duplicates by chapter number; if it reappears, that is an app regression, not a data problem.
- **Retired banks must leave the folder.** `discover_vault_banks()` publishes every `Quiz_*.json` in the quiz folder; an obsolete bank left in place is re-published forever. Move it to `_retired/` (note: the vault `.gitignore` ignores `_archive/`, so use `_retired/`).
- **A bank that repeats another chapter's content** (the old `Quiz_02_Patriot_Brooks` sat on chapter 2 while testing chapter-1 material) — retire it instead of renaming it.
- **`_archive/` is git-ignored** — content parked there is not versioned.
- **New bank files break the bundled fallback** until `pull` runs: the worker's precache list still points at the old names.
- **Headless QA creates real guest accounts** (`t######` / «اسم جديد») in `portal_users` and league rows. After a browser-based check, sweep them (keep the student's own account) — see the cleanup pattern in `sessions/2026-10-21.md`.
- **The shell caches hard.** A stale device shows an old app bar; the app now re-checks the worker on foreground, and `?v=<n>` forces a fresh fetch.
- **Never `git add -A` in the vault** — other harnesses work in the same tree. Stage only your files.

## 13. Delivery checklist

- [ ] File name + `quiz_id` follow the chapter's shape (`Model<A|B>` or `T<NN>`); chapter number is the book's.
- [ ] Titles: no subject name, no model suffix on topic banks.
- [ ] Count, chapter and shape confirmed with the student first (never assumed); `concept_id`s unique across the whole chapter.
- [ ] 5+ questions per bank; unique `concept_id`s across the chapter's two models.
- [ ] Every question grounded in a named source; nothing invented.
- [ ] Arabic-first bilingual, MSA, English terms without parentheses, `←` in Arabic lines.
- [ ] `quiz_balancer --check --strict` exit 0 for every file (after a balancing pass).
- [ ] v2 + v3 validation lists empty.
- [ ] `portal_content.py sync` run; `status` shows the new counts.
- [ ] `portal_content.py pull` run; deploy only if it reported a precache change.
- [ ] App checked: plain chapter chips, `موضوع: N` badges, أ before ب, two launches shuffle questions + options with a stable key, translation icon works, offline works.
- [ ] Session log updated (what was added, where, and the evidence).
