# Portal Memory — MCQ student portal (the known place)

> Any agent in Master-Studio: when the student says "ادفع للبوابة / push to portal",
> this file + one command is the whole pipeline. No manual JSON editing.

## Where

- Portal repo (separate, student-facing): `C:/Users/gokoq/mcq-portal`
- Live URL: `https://mcq-portal-jade.vercel.app`
- Push tool: `90_Shared_Toolbox/tools/portal_push.py`

## The one command

```bash
# from Master-Studio root
python 90_Shared_Toolbox/tools/portal_push.py "<vault-quiz.json>" --subject <SUBJECT_ID> --chapter <N> [--dry-run]
```

The tool validates, converts (`chapter_no`, `demo:false`), writes the bank,
rebuilds the subject/chapter entry in the portal `index.json`, prunes demo
banks of that subject, refreshes `sw.js` cache + version. Deploy is separate:

```bash
cd C:/Users/gokoq/mcq-portal && npx -p vercel@latest vercel --prod --yes
```

## Canonical chapter order (first listed = Chapter 1)

| Subject | Ch | Vault bank |
|:---|:---:|:---|
| `01_Cyber_Security` | 1 | `01_Cyber_Security/07_Quizzes_&_Anki/Quiz_Ch01_DrHuda_20MCQ.json` |
| `01_Cyber_Security` | 2 | `01_Cyber_Security/07_Quizzes_&_Anki/Quiz_Ch02_DrHuda_20MCQ.json` |
| `01_Cyber_Security` | 3 | `01_Cyber_Security/07_Quizzes_&_Anki/Quiz_01_Cybersecurity_Foundations.json` |
| `01_Cyber_Security` | 4 | `01_Cyber_Security/07_Quizzes_&_Anki/Quiz_02_Risk_Assessment.json` |
| `02_English_Language` | 1 | `02_English_Language/07_Quizzes_&_Anki/Quiz_01_Grammar_and_Tenses.json` |
| `03_Data_Mining` | 1 | `03_Data_Mining/07_Quizzes_&_Anki/Quiz_01_Introduction_to_Data_Mining.json` |
| `04_Advanced_Software_Eng` | 1 | `04_Advanced_Software_Eng/07_Quizzes_&_Anki/Quiz_01_Software_Crisis.json` |
| `04_Advanced_Software_Eng` | 2 | `04_Advanced_Software_Eng/07_Quizzes_&_Anki/Quiz_02_Patriot_Brooks.json` |
| `05_Soft_Computing` | 1 | `05_Soft_Computing/07_Quizzes_&_Anki/Quiz_01_Soft_Computing_Foundations.json` |
| `05_Soft_Computing` | 2 | `05_Soft_Computing/07_Quizzes_&_Anki/Quiz_02_Fuzzy_Logic_Systems.json` |

## Rules

1. **Only quiz banks cross the boundary.** Never copy `LEARNER_MODEL.md`,
   `PROGRESS_ANALYTICS.md`, `quiz_history.json`, `sessions/`, or anything
   student-private. The tool only accepts `Quiz_*.json` files.
2. Structural failure (options != 4, answer/correct mismatch) = bank is
   **skipped**, fix the bank first. Length/positional-bias warnings print
   but do not block — report them to the student.
3. Known-flawed banks (audit 2026-10-18): `Quiz_01_Cybersecurity_Foundations`
   Q27 length tell · `Quiz_01_Grammar_and_Tenses` Q1/Q2/Q4 length ·
   `Quiz_01_Software_Crisis` 25 gate errors. Rebalance before pushing.
4. After pushing real banks, verify locally
   (`python -m http.server` in portal + `?debug=1`) before `vercel --prod`.
