# Runtime contract — MCSQuiz app (verified, not assumed)

What the app does with a bank after `portal_content.py sync` publishes it.
Verified 2026-10-22 against `C:\Users\gokoq\mcq-portal\js\app.js` and by launching
the same quiz 3× headless (`preparePool` is Fisher–Yates, `js/app.js:803-838`).

## 1. Every launch reshuffles — questions and options

- `preparePool()` runs on **every** session start (`launchSession`,
  `startSavedPractice`): `shuffle(pool)` reorders the questions, then each
  question's 4 options are reordered with an independent permutation.
- Probe result (Quiz_Ch01_ModelA_AI_Foundations, 3 launches):
  - question orders: `q5,q1,q3,q2,q4` / `q2,q4,q5,q1,q3` / `q4,q1,q5,q3,q2`
  - q1 option orders: 3 distinct permutations out of 3 launches.
- Consequence: two students (or two attempts) never see the same paper, and a
  screenshot of "question 3 = C" is meaningless on the next run.

## 2. The key follows the text, not the letter

- After permuting, the session recomputes the key from the **option text**:
  `q.correct = order.indexOf(key); q.answer = q.correct;`
  where `key` is the pre-shuffle index of the intended correct option.
- Probe result: the correct-answer **text** (`Acting humanly`) was identical
  across all 3 launches while its letter moved.
- Scoring, the live feedback (`q.correct === i`, `js/app.js:1440-1444`) and the
  answer sound (`i === q.correct`, `js/app.js:1498`) all compare the tapped
  index against the remapped `correct`. A shuffled layout can never mark a
  right answer wrong.

## 3. What this means for authoring

- The stored answer key (`answer`/`correct` in the vault file) is only the
  *intended* key. The balancer permutes it; the app permutes it again.
  What must stay stable is the **intended correct text** — re-check it after
  every balance pass (`"ABCD"[correct] === answer` with the right text).
- Positional bias in the stored file still matters (habits, screenshots, the
  saved-question review), so the psychometric gate (§7 of the protocol) stays
  mandatory — but it is **not** the anti-cheat mechanism. The per-launch
  shuffle is.
- Saved-question practice and retry-wrong go through the same
  `launchSession → preparePool` path, so they shuffle too.

## 4. Offline reads (relevant when verifying)

`portal manifest → cached manifest → bundled data/index.json + data/banks/`.
`pull` keeps the bundle and the service-worker precache list in step; a stale
worker serves a stale shell — `?v=<n>` forces a fresh fetch.
