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

## Data Source

Reads directly from `00_STUDIO_HUB/` markdown files — no database, no config. If the Hub files update, refresh the page.
