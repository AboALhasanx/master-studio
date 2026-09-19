# Final Review Fix Brief: Schema Normalization & Reflection Telemetry

**Files to Modify:**
- `91_Dashboard/static/quiz.js`

**Review Findings to Fix:**
1. **Finding 1 (P0): Normalization of Options & Answer Key in `quiz.js`**:
   - Real quiz JSON files in `01_Semester_1` use dictionary options (e.g. `options: {"A": "...", "B": "..."}`) and `"answer": "B"`.
   - In `setupQuizSession()` in `quiz.js`, normalize each question in `this.quizData.questions`:
     - If `q.options` is a dictionary, extract `optionKeys = Object.keys(q.options)` and `optionsArray = Object.values(q.options)`.
     - If `q.options` is an array, `optionKeys = ['A', 'B', 'C', 'D'].slice(0, q.options.length)` and `optionsArray = q.options`.
     - Resolve `correct` (integer index 0-3) and `correctLetter` ('A'-'D') from either `q.answer` (e.g. "B") or `q.correct`.
     - Set `q.options = optionsArray`, `q.optionKeys = optionKeys`, `q.correct = correctIdx`, `q.correctLetter = correctLetter`.
   - Ensure `renderQuestion` and `renderReviewCards` use `q.options` safely without throwing TypeErrors.
   - Support `subject_id: this.quizData.subject || this.quizData.subject_id || this.subjectId`.

2. **Finding 2 (P1): Nested Reflection Object in Telemetry Payload**:
   - In `submitTelemetry()` in `quiz.js`, format the reflection metadata for each question as:
     ```javascript
     reflection: !isCorrect ? {
         reason: reflection?.reason || 'Concept Gap',
         note: reflection?.notes || reflection?.note || ''
     } : null,
     is_lucky_guess: isLucky
     ```
   - Also include `selected: userAns !== undefined ? q.optionKeys[userAns] : null` and `correct: q.correctLetter`.
   - This ensures `quiz_engine.py` receives the nested `q.get('reflection')` object with `reason` and `note` as expected by `process_quiz_telemetry` and the spec.

**Verification:**
- Check syntax with `node -c 91_Dashboard/static/quiz.js`.
- Run `python -m pytest tests/` and verify all tests pass.
- Write fix report to `.superpowers/sdd/2026-09-19-interactive-web-quiz-system/final-review-fix-report.md`.
