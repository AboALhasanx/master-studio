# Handoff — Gemini writes MCSQuiz question banks

> **Who reads this:** Gemini (Antigravity / the Gemini web app / any Gemini-based harness) that has been asked to author question banks for the MCSQuiz portal. **Who hands it over:** the student, or any vault harness (OpenCode, Codex, WorkBuddy, MiMo) that received the output.
> **Rule of the house:** `00_STUDIO_HUB/guides/QUIZ_BANK_PROTOCOL.md` is binding. This handoff only explains *how to do the job in one pass*; if the two ever disagree, the protocol wins.

---

## 0. The prompt the student sends (fill the brackets)

```
اقرأ أولاً (بالترتيب):
1) 00_STUDIO_HUB/handoffs/GEMINI_QUIZ_HANDOFF.md
2) 00_STUDIO_HUB/guides/QUIZ_BANK_PROTOCOL.md
3) 00_STUDIO_HUB/templates/template-quiz-bank.json
4) المصدر: (مسار ملف الملاحظات داخل 03_Study_Notes)

المهمة — بنك أسئلة واحد:
- subject_id: (01_Cyber_Security)
- الجابتر: (3)
- النموذج: (أ)
- عدد الأسئلة: (5)
- quiz_id: (Quiz_Ch03_ModelA_Cybersecurity_Foundations)
- مسار الحفظ: 01_Semester_1/(01_Cyber_Security)/07_Quizzes_&_Anki/(Quiz_Ch03_ModelA_Cybersecurity_Foundations).json
- الدكتور: انسخه من أي بنك موجود بنفس المجلد
- العنوان العربي: (عنوان الجابتر من المصدر) — النموذج أ

نفّذ حسب البروتوكول، ولا تخترع أي معلومة ليست في المصدر، ولا تلمس أي ملف ثاني.
بعد الكتابة: شغّل فحوصات البوابة (إذا عندك صلاحية ملفات) واطبع نتيجتها، أو اطبع الـJSON كاملاً ببلوك كود واحد.
```

A batch version and a two-models version are in `GEMINI_QUIZ_PROMPT.md`.

---

## 1. Read first

| # | file | why |
|---|---|---|
| 1 | `00_STUDIO_HUB/guides/QUIZ_BANK_PROTOCOL.md` | the binding rules: schema, naming, two models, style, gates, publish |
| 2 | `00_STUDIO_HUB/templates/template-quiz-bank.json` | the exact shape to copy (delete every `_`-prefixed key before saving) |
| 3 | `01_Semester_1/<Subject>/03_Study_Notes/<the file named in the order>` | the **only** source of facts for this bank |
| 4 | any existing bank in `01_Semester_1/<Subject>/07_Quizzes_&_Anki/` | copy `subject_title`, `instructor_ar`, `instructor` from it, and avoid repeating its concepts |

If a fact is not in (3): pick another fact from (3). Never invent a definition, a number, a paper, a page or a DOI.

---

## 2. The work order (fill this in before writing)

```
subject_id        :
subject_title     :   (copy from an existing bank of the same subject)
chapter           :   (the book's chapter number, e.g. 3 — not a running counter)
model             :   A  or  B          -> topic ends with "— Model A" / "— النموذج أ"
quiz_id           :   Quiz_Ch<NN>_Model<A|B>_<Slug>
file path         :   01_Semester_1/<subject_id>/07_Quizzes_&_Anki/<quiz_id>.json
question count    :   (5 minimum; 10–15 when the material is rich)
source file       :   (one file; more only if the order names them)
instructor_ar / instructor : (copied, not guessed)
```

Two models per chapter, never three. If the chapter already has a bank, you are writing the **other** model and your concepts must not repeat the existing one's `concept_id`s.

---

## 3. Output contract — pick the mode you are in

**Mode A — you can read and write files (an agent inside the vault):**
1. Write exactly one file: `<file path>` (UTF-8, no BOM, `\n` line endings, 2-space indent).
2. Run the gates and paste the raw output:
   ```bash
   cd C:\Users\gokoq\Master-Studio
   python "90_Shared_Toolbox/tools/quiz_balancer.py" "<file path>"
   python "90_Shared_Toolbox/tools/quiz_balancer.py" "<file path>" --check --strict
   python -c "import sys,json,io; sys.path.insert(0,r'90_Shared_Toolbox/tools'); from quiz_balancer import validate_schema_v2; sys.path.insert(0,r'C:\Users\gokoq\mcq-portal\tools'); import portal_schema as ps; p=r'<file path>'; b=json.load(io.open(p,encoding='utf-8')); print(validate_schema_v2(b), ps.validate_v3(ps.to_v3(b)))"
   ```
   Fix and repeat until: the balancer saved a balanced bank, `--check --strict` exits **0**, and both validation lists are **empty**.
3. Do **not** publish (`portal_content.py sync`) — hand back and let the receiving agent publish.

**Mode B — you are a chat model with no filesystem:**
1. Print the **complete** bank as **one** ```json code block, valid on its own (no comments, no ellipses, no `…`).
2. Immediately after it, print a short block:
   ```
   subject_id / chapter / model / quiz_id / file path / question count
   concepts (one line each)
   answer key distribution: A n | B n | C n | D n
   longest-correct-option ratio per question (correct chars ÷ average distractor chars)
   source lines used from <source file>
   ```
3. The receiving agent will run the gates and publish. If a gate fails it will come back with the flagged question — fix only that question and re-print the whole block.

---

## 4. The shape (skeleton — the full example is in the protocol §4)

```json
{
  "schema_version": 2,
  "subject_id": "…",
  "subject_title": "…",
  "semester": 1,
  "semester_label": "كورس أول",
  "quiz_id": "Quiz_Ch<NN>_Model<A|B>_<Slug>",
  "topic": "… — Model A",
  "topic_ar": "… — النموذج أ",
  "instructor_ar": "…",
  "instructor": "…",
  "subject": "…",
  "questions": [
    {
      "id": "q1",
      "concept_id": "snake_case_concept",
      "bloom_level": "Understand",
      "question": "English stem",
      "question_ar": "نص السؤال بالعربية",
      "options": ["EN 1", "EN 2", "EN 3", "EN 4"],
      "options_ar": ["ع 1", "ع 2", "ع 3", "ع 4"],
      "options_en": ["EN 1", "EN 2", "EN 3", "EN 4"],
      "answer": "C",
      "correct": 2,
      "explanation": "why the key is right and why each distractor fails (1–3 sentences)",
      "explanation_ar": "نفس الشي بالعربية (1–3 جمل)"
    }
  ]
}
```

`"ABCD"[correct] === answer` is mandatory. Exactly 4 options in each of `options` / `options_ar` / `options_en`. `id` renumbered `q1…qN`.

---

## 5. The eight rules that actually get failed

1. **Arabic-first, clean terms.** MSA, no dialect; `Fuzzy Set`, `Waterfall`, `UCS` stay English inside the Arabic sentence, **never** `المجموعات الضبابية (Fuzzy Set)`.
2. **Arrow direction:** `←` inside an Arabic line, `→` inside an English line.
3. **Length parity:** the correct option must stay within ±25 % of the distractors' average length — never the longest, never the only qualified one.
4. **Answer-key spread:** hand-distribute it (see §6). Never dump answers into one letter.
5. **One idea per question, one question per idea.** No "all of the above", no trick wording, no double negatives.
6. **Distractors are real misconceptions**, not filler; each explanation names the specific flaw.
7. **No repeats across the chapter's two models:** 10 distinct `concept_id`s for A + B.
8. **Math** only when the source has it: `$x$` inline, `$$…$$` display, **no Arabic inside math**.

---

## 6. Hand-distributed keys (when you cannot run the balancer)

| questions | target distribution |
|---|---|
| 5 | 2 / 1 / 1 / 1 (every letter at least once, none twice+) |
| 8 | 2 / 2 / 2 / 2 |
| 10 | 3 / 3 / 2 / 2 |
| 12 | 3 / 3 / 3 / 3 |
| 15 | 4 / 4 / 4 / 3 |

Never let one letter exceed 32 % of the keys. After the receiving agent runs the balancer the positions may be permuted — the intended correct **text** must remain the key.

---

## 7. Self-check before you answer

- [ ] The file name / `quiz_id` / chapter number match the order.
- [ ] `topic` / `topic_ar` end with `— Model A/B` / `— النموذج أ/ب`.
- [ ] 5+ questions, each with 4 options in all three option arrays.
- [ ] `answer` and `correct` agree in every question.
- [ ] Every claim traceable to the named source file; nothing invented.
- [ ] No parenthetical English echoes in Arabic; `←` in Arabic lines.
- [ ] Keys hand-distributed per §6; no correct option visibly longest.
- [ ] No `_`-prefixed template keys left in the file.
- [ ] Only the ordered file was created or changed.

---

## 8. Do not

- Publish, deploy, or run `portal_content.py sync` (the receiving agent does that).
- Edit, rename or delete an existing bank, or write a second bank for the same chapter/model.
- Touch another subject's folder, the study notes, or `mcq-portal/`.
- Use `git add -A` (other harnesses work in this tree).
- Invent citations, numbers, authors, pages, DOIs — and never quote a source you did not read.

---

## 9. Hand back exactly this

```
FILES       : <path> (one line per file)
BANK        : subject_id | chapter | model | quiz_id | questions
CONCEPTS    : q1 … qN (one line each)
SOURCE      : <file(s) read> — which section/slide each question came from
KEYS        : A n | B n | C n | D n
GATES       : balancer / --check --strict / v2+v3 output (Mode A) — or "not run (chat mode)"
OPEN ISSUES : anything the source did not settle, or a question you are unsure about
```

---

## 10. If you are an agent working inside the vault

1. Sign in first: read `00_STUDIO_HUB/HARNESS_REGISTRY.md`; if your row exists update its `Last seen`, otherwise add one; append one sign-in line to `00_STUDIO_HUB/sessions/YYYY-MM-DD.md`.
2. Name other harnesses' work with its date (*"found work from OpenCode 2026-10-22, left intact"*).
3. Stage only your own files when committing, and mention the bank ids in the commit message.
4. The receiving agent (or you, if you publish) then runs `portal_content.py sync`, checks `status`, and runs `pull` — see `PORTAL_PUBLISH.md`.
