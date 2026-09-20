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
