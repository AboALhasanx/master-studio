# Contributing to Master-Studio

Thanks for stopping by. This is a personal study vault that doubles as a small
open-source toolbox (quiz engine, PDF/dashboard utilities, MSCQuiz Android client).
Contributions are welcome, but review bandwidth is limited — please keep PRs small
and focused.

## Setup

Requirements: Python 3.10+.

```bash
pip install -r requirements.txt
```

No other services are required to run the test suite. The Flask dashboard
(`91_Dashboard/`) is optional for most changes.

## Running tests

```bash
pytest -q
```

A change that adds or alters functionality must arrive with a test under
`tests/` (see `tests/test_quiz_engine.py` for the established style).

## Opening a pull request

1. Branch from `master`: `git checkout -b feat/short-description`.
2. Follow the existing [Conventional Commits](https://www.conventionalcommits.org/)
   style used in this repo (`feat:`, `fix:`, `chore:`, `docs:`, `test:` …).
3. Fill in the PR template checklist (tests run, files affected, screenshots for UI).
4. Keep it to one concern per PR.

## What counts as acceptable

- Small, reviewable diffs with passing `pytest`.
- No binaries, keystores, APKs, `.env` files, textbooks, or personal documents.
  Anything gitignored stays out of PRs — no exceptions.
- New quiz content must pass the balancer/linter flow described in the quiz docs.

## Communication

- Bugs and ideas: [GitHub Issues](../../issues).
- Security problems: see [SECURITY.md](SECURITY.md) — do **not** open a public issue.
