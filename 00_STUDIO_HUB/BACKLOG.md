# Deferred Review Backlog (student-ordered, not scheduled)

> Rule: items here are acknowledged but explicitly NOT now. A harness must not
> start them unprompted — the student promotes an item by saying so.

## 1. Quiz banks: expand to 20–25 questions + pass `--strict` (DEFERRED 2026-10-03)

- **Standard (student-set):** no 5-question quizzes — minimum 20–25 questions per bank.
- **Current state:** 8 banks exist (5–12Q). `quiz_balancer.py --strict` FAILS on
  `Quiz_01_Grammar_and_Tenses` (English) and `Quiz_01_Software_Crisis` (ASE):
  40% key concentration + longest-correct tells. 5Q banks cannot balance
  mathematically — expansion (not permutation) is the fix.
- **When promoted:** author +12–20 new scenario questions per bank from the
  matching study notes, lengthen distractors to ±25% of the key, run
  `quiz_balancer.py --strict` until exit 0, student reviews new items first.

## 2. Tool defect: `quiz_balancer.py --strict` rewrites banks in check mode (FOUND 2026-10-03)

- Running `--strict` (no `--fix`, no `--seed`) permuted options in 6 banks
  in place. Reverted via `git checkout` — verified state restored, suite green.
- Fix required: check mode must be read-only; any rewrite needs an explicit
  write flag. Until fixed, run the balancer only on copies, or commit first
  so `git checkout` can rescue a surprise rewrite.
