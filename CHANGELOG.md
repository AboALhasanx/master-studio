# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versioning follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Repository scaffold: Apache-2.0 `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`,
  `CODE_OF_CONDUCT.md`, `CITATION.cff`.
- GitHub community health: bug/feature issue templates, PR template,
  `CODEOWNERS`, Dependabot for Actions, stale-issue automation.
- CI: pytest suite on push/PR (`ci.yml`) plus weekly CodeQL analysis.
- `.gitignore` hardening: APK/AAB/keystores, device screenshots, temp extracts,
  editor dirs; `quiz_mobile.html` untracked (build output, kept on disk).
- README badges (CI, license, Python), contributor quickstart, docs index.
- iOS roadmap tracked as issues
  [#1](https://github.com/AboALhasanx/master-studio/issues/1),
  [#2](https://github.com/AboALhasanx/master-studio/issues/2),
  [#3](https://github.com/AboALhasanx/master-studio/issues/3) (deferred, Android first).

## [1.0.0] - 2026-09-26
- MSCQuiz Android client: offline-first APK builder (`build_mscquiz_apk.py`),
  signed release (`MSCQuiz_Signed.apk`), Telegram direct-open intents,
  bundled semester curriculum, SPA catalog navigation.
- Industrial quiz lifecycle: canonical schema v2, `QuizVault` IndexedDB engine,
  bundling API, LAN sync, Web Share Target + File Handling.
