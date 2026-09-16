#!/usr/bin/env python3
"""
Master Studio Dashboard
-----------------------
Flask web app that visualizes progress, mastery, and GPA from the Hub files.

Usage:
  python app.py
  Then open http://127.0.0.1:5000
"""

import re
import json
from pathlib import Path
from datetime import datetime
from flask import Flask, render_template, jsonify

app = Flask(__name__)

BASE = Path(__file__).resolve().parent.parent
HUB = BASE / "00_STUDIO_HUB"
SEM1 = BASE / "01_Semester_1"


def read_file(path):
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def parse_frontmatter(text):
    """Extract key: value pairs from YAML frontmatter."""
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        kv = re.match(r'^(\w[\w_]*):\s*["\']?(.*?)["\']?\s*$', line)
        if kv:
            data[kv.group(1)] = kv.group(2)
    return data


def parse_active_state():
    text = read_file(HUB / "ACTIVE_STATE.md")
    fm = parse_frontmatter(text)
    return {
        "semester": fm.get("current_semester", "Unknown"),
        "week": fm.get("active_week", "?"),
        "subject": fm.get("active_subject", "Unknown"),
        "todo": fm.get("immediate_todo", ""),
        "next_focus": fm.get("next_session_focus", ""),
        "status": fm.get("status", ""),
        "updated": fm.get("last_updated", ""),
    }


def parse_learner_model():
    text = read_file(HUB / "LEARNER_MODEL.md")
    mastered = []
    review = []

    for m in re.finditer(r'\|\s*`([^`]+)`\s*\|\s*([^|]+)\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(\d+)%\s*\|\s*@(\w+)', text):
        mastered.append({
            "subject": m.group(1),
            "concept": m.group(2).strip(),
            "date": m.group(3),
            "score": int(m.group(4)),
            "agent": m.group(5),
        })

    for m in re.finditer(r'\|\s*`([^`]+)`\s*\|\s*([^|]+)\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]+)\|\s*(\w+)\s*\|\s*(\d{4}-\d{2}-\d{2})', text):
        review.append({
            "subject": m.group(1),
            "concept": m.group(2).strip(),
            "added": m.group(3),
            "reason": m.group(4).strip(),
            "priority": m.group(5),
            "due": m.group(6),
        })

    accuracy = re.search(r'Overall Scenario Accuracy:\*\*\s*(\d+)%', text)
    confidence = re.search(r'Oral Defense Confidence Rating:\*\*\s*([\d.]+)', text)
    quizzes = re.search(r'Total Quizzes Attempted:\*\*\s*(\d+)', text)

    return {
        "mastered": mastered,
        "review": review,
        "accuracy": int(accuracy.group(1)) if accuracy else 0,
        "confidence": float(confidence.group(1)) if confidence else 0,
        "quizzes_taken": int(quizzes.group(1)) if quizzes else 0,
    }


def parse_progress_analytics():
    text = read_file(HUB / "PROGRESS_ANALYTICS.md")
    subjects = []
    for m in re.finditer(
        r'\|\s*(\d{2}_[A-Za-z_]+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([\d%\-—]+)\s*\|\s*([^|]+)\|',
        text,
    ):
        score_str = m.group(4).strip()
        score = None
        if "%" in score_str:
            score = int(score_str.replace("%", ""))
        subjects.append({
            "name": m.group(1),
            "credits": int(m.group(2)),
            "quizzes": int(m.group(3)),
            "score": score,
            "status": m.group(5).strip(),
        })

    quiz_log = []
    for m in re.finditer(
        r'\|\s*#(\d+)\s*\|\s*([\d-]+)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+)\|\s*(\d+)\s*/\s*(\d+)\s*\((\d+)%\)\s*\|\s*(\w+)\s*\|',
        text,
    ):
        quiz_log.append({
            "id": m.group(1),
            "date": m.group(2),
            "subject": m.group(3),
            "topic": m.group(4).strip(),
            "correct": int(m.group(5)),
            "total": int(m.group(6)),
            "score": int(m.group(7)),
            "result": m.group(8),
        })

    readiness = re.search(r'Overall Semester Readiness:\s*([\d.]+)%', text)
    return {
        "subjects": subjects,
        "quiz_log": quiz_log,
        "readiness": float(readiness.group(1)) if readiness else 0,
    }


def parse_gpa_tracker():
    text = read_file(HUB / "GPA_TRACKER.md")
    courses = []
    for m in re.finditer(
        r'\|\s*\*\*(CS\d+)\*\*\s*\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([\d.]+)%\s*\|\s*(\w+)',
        text,
    ):
        grade_str = m.group(7).strip()
        grade = None
        if grade_str not in ("—", "-", ""):
            try:
                grade = float(grade_str)
            except ValueError:
                pass
        courses.append({
            "code": m.group(1),
            "name": m.group(2),
            "credits": int(m.group(3)),
            "instructor": m.group(4).strip(),
            "target": float(m.group(9)),
            "status": m.group(10),
            "grade": grade,
        })
    return {"courses": courses}


def get_folder_stats():
    """Count content files per subject (excluding raw materials)."""
    stats = {}
    if not SEM1.exists():
        return stats
    for subj in sorted(SEM1.iterdir()):
        if not subj.is_dir():
            continue
        notes = list((subj / "03_Study_Notes").glob("*.md")) if (subj / "03_Study_Notes").exists() else []
        slides = list((subj / "05_Seminars_&_Slides").glob("*.md")) if (subj / "05_Seminars_&_Slides").exists() else []
        diagrams = list((subj / "06_Diagrams_&_Mindmaps").glob("*.png")) if (subj / "06_Diagrams_&_Mindmaps").exists() else []
        quizzes = list((subj / "07_Quizzes_&_Anki").glob("*.json")) if (subj / "07_Quizzes_&_Anki").exists() else []
        raw = list((subj / "02_Raw_Materials").glob("*")) if (subj / "02_Raw_Materials").exists() else []
        raw = [f for f in raw if f.is_file() and f.name != "README.md"]
        stats[subj.name] = {
            "notes": len(notes),
            "slides": len(slides),
            "diagrams": len(diagrams),
            "quizzes": len(quizzes),
            "raw_materials": len(raw),
            "total_content": len(notes) + len(slides) + len(diagrams) + len(quizzes),
        }
    return stats


@app.route("/")
def index():
    active = parse_active_state()
    learner = parse_learner_model()
    progress = parse_progress_analytics()
    gpa = parse_gpa_tracker()
    folder_stats = get_folder_stats()

    total_content = sum(s["total_content"] for s in folder_stats.values())
    total_raw = sum(s["raw_materials"] for s in folder_stats.values())

    return render_template(
        "index.html",
        active=active,
        learner=learner,
        progress=progress,
        gpa=gpa,
        folder_stats=folder_stats,
        total_content=total_content,
        total_raw=total_raw,
    )


@app.route("/api/data")
def api_data():
    return jsonify({
        "active": parse_active_state(),
        "learner": parse_learner_model(),
        "progress": parse_progress_analytics(),
        "gpa": parse_gpa_tracker(),
        "folder_stats": get_folder_stats(),
    })


if __name__ == "__main__":
    print("Master Studio Dashboard")
    print("Open http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
