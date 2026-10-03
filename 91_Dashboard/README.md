# Master Studio Dashboard

Local Flask dashboard that visualizes progress, mastery, quiz history, and GPA from the Hub files.

## Quick Start

```bash
cd 91_Dashboard
pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## What It Shows

- Active session (current subject, week, todos)
- Semester readiness and quiz accuracy
- Subject mastery radar (all 6 courses)
- Content files per subject (notes, slides, diagrams, quizzes)
- Quiz history with pass/fail
- Mastered concepts and review queue
- GPA tracker with target grades
- Grading threshold scale (60% / 70% / 75%)
- **Interactive Quizzes & Drills:** Direct launch panel for browser assessments

## Interactive Quiz Subsystem

The dashboard includes a full-featured, zero-database quiz web application:

### Available Routes
- `GET /`: Main dashboard with progress radar, stats, and Interactive Quizzes launch panel.
- `GET /quiz`: Hub landing page for interactive quizzes.
- `GET /quiz/<subject_id>/<quiz_id>`: Direct quiz view in Study Mode (immediate feedback) or Exam Mode (`?mode=exam`).
- `GET /api/quiz/list`: JSON catalog of all available quizzes across all semester directories (`01_Semester_1`, `02_Semester_2`, etc.).
- `GET /api/quiz/<subject_id>/<quiz_id>`: Returns normalized quiz question JSON.
- `POST /api/quiz/submit`: Ingests completion telemetry (dwell times, lucky guesses, metacognitive reflections) and logs markers into `00_STUDIO_HUB/sessions/YYYY-MM-DD.md`.
- `GET/POST /api/quiz/bookmarks`: Persists starred questions across devices in `00_STUDIO_HUB/quiz_bookmarks.json`.

### Key Features
- **Study Mode vs. Exam Mode:** Switch via header pill button or `?mode=exam` URL parameter. Exam mode hides answer feedback and explanations until the final score screen.
- **Anti-Memorization Shuffle:** Header button or `?shuffle=true` randomizes questions and options via Fisher-Yates while preserving telemetry IDs.
- **Accessible & High-Contrast:** Paired design tokens for dark (#14161C) and light (#FFFFFF) themes exceeding WCAG AAA standards (>15:1 contrast).
- **Mobile QR Generation:** Run `python 90_Shared_Toolbox/tools/quiz_qr.py <Subject> <Quiz>` to print an ASCII QR code for LAN mobile studying.

## Data Source

All views read live from `00_STUDIO_HUB/` (ACTIVE_STATE, LEARNER_MODEL, GPA_TRACKER, quiz JSONs). No database.

## Trust Model (read before exposing)

LAN-trusted by design: the server binds `0.0.0.0:5000` with **no authentication**. Any device on the same network can read quizzes and telemetry — and `POST /api/quiz/import` can write quiz banks into the vault (collision-guarded, never overwriting). Never expose this port beyond the home LAN; there is no production WSGI/token gate (tracked as dashboard backlog).

## Agent & Mobile Notes (moved from root AGENTS.md — agent-facing detail lives here)

- **PWA install:** Service Worker (`/static/sw.js` + `/static/manifest.json`); "Add to Home Screen" in Chromium/Chrome; works 100% offline (Airplane mode) without the PC server.
- **Offline Local File Picker (zero-server fallback):** folder icon (`#btn-open-local-file`) opens the native Android picker for any `Quiz_*.json` from the phone's DriveSync folder; cached in `localStorage`.
- **Direct browser launch:** `python 90_Shared_Toolbox/tools/quiz_qr.py "<Subject>" "<Quiz>" --open` pops the quiz in Chromium; use its "Send to your devices" for 1-click phone sharing. LAN QR: same command without `--open` prints scannable terminal QR.
- **Mobile testing protocol (UIAutomator first):** agents automating Android MUST inspect UI hierarchy via `adb shell uiautomator dump` or compact accessibility snapshots — never VLM screenshot loops for coordinates. VLM vision reserved for one-shot cosmetic checks.
