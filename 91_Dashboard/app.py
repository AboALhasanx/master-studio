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
import socket
import sys
from pathlib import Path
from datetime import datetime
import uuid
from flask import Flask, render_template, jsonify, request

# Ensure Shared Toolbox is importable
_toolbox_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox" / "tools"
if str(_toolbox_path) not in sys.path:
    sys.path.insert(0, str(_toolbox_path))
from quiz_engine import process_quiz_telemetry, get_quiz_history

app = Flask(__name__)

BASE = Path(__file__).resolve().parent.parent
HUB = BASE / "00_STUDIO_HUB"
SEM1 = BASE / "01_Semester_1"


def read_file(path):
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def get_lan_ip() -> str:
    """Detect host Wi-Fi/Ethernet LAN IP address, fallback to 127.0.0.1."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        if ip.startswith("10."):
            try:
                hostname = socket.gethostname()
                ip_list = socket.gethostbyname_ex(hostname)[2]
                wifi_ips = [candidate for candidate in ip_list if candidate.startswith("192.168.")]
                if wifi_ips:
                    return wifi_ips[0]
            except Exception:
                pass
        return ip
    except Exception:
        return "127.0.0.1"
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
def parse_sessions():
    """Parses session journal files from 00_STUDIO_HUB/sessions."""
    sessions_dir = HUB / "sessions"
    sessions = []
    if sessions_dir.exists():
        for sf in sorted(sessions_dir.glob("*.md"), reverse=True):
            text = read_file(sf)
            title = re.search(r'title:\s*["\']?(.*?)["\']?\s*$', text, re.M)
            sid = re.search(r'session_id:\s*["\']?(.*?)["\']?\s*$', text, re.M)
            date_m = re.search(r'date:\s*["\']?(.*?)["\']?\s*$', text, re.M)
            sessions.append({
                "id": sid.group(1) if sid else sf.stem,
                "title": title.group(1) if title else sf.stem,
                "date": date_m.group(1) if date_m else "",
                "filename": sf.name
            })
    return sessions

def parse_college_buddy():
    """Parses active events and debriefs from 00_STUDIO_HUB/COLLEGE_BUDDY.md."""
    buddy_file = HUB / "COLLEGE_BUDDY.md"
    if not buddy_file.exists():
        return {"events": [], "alerts_count": 0, "debriefs_count": 0}

    text = read_file(buddy_file)
    lines = text.splitlines()
    events = []
    in_active = False

    today = datetime.now().date()

    for line in lines:
        if "## 1. Active Events" in line:
            in_active = True
            continue
        elif line.startswith("## ") and in_active:
            break

        if not in_active or not line.strip().startswith("|"):
            continue

        cols = [c.strip() for c in line.strip().split("|")[1:-1]]
        if not cols or "ID" in cols[0] or "---" in cols[0]:
            continue

        if len(cols) >= 6:
            evt_id = cols[0].replace("*", "").strip()
            date_str = cols[1].strip()
            subj = cols[2].strip()
            event = cols[3].strip()
            prof = cols[4].strip()
            status = cols[5].strip().upper()
            urgency = cols[6].strip() if len(cols) > 6 else "MEDIUM"
            notes = cols[7].strip() if len(cols) > 7 else ""

            if status in ["COMPLETED", "CANCELED"]:
                continue

            try:
                evt_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                delta = (evt_date - today).days
            except Exception:
                delta = 999

            events.append({
                "id": evt_id,
                "date": date_str,
                "subject": subj,
                "event": event,
                "professor": prof,
                "status": status,
                "urgency": urgency,
                "notes": notes,
                "delta": delta,
                "is_urgent": delta <= 3 and delta >= 0,
                "is_overdue": delta < 0 and status == "UPCOMING"
            })

    alerts_count = sum(1 for e in events if e["is_urgent"])
    debriefs_count = sum(1 for e in events if e["is_overdue"])
    return {
        "events": events,
        "alerts_count": alerts_count,
        "debriefs_count": debriefs_count
    }


@app.route("/")
def index():
    active = parse_active_state()
    learner = parse_learner_model()
    progress = parse_progress_analytics()
    gpa = parse_gpa_tracker()
    folder_stats = get_folder_stats()
    sessions = parse_sessions()
    buddy = parse_college_buddy()
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
        sessions=sessions,
        buddy=buddy,
        available_quizzes=get_all_quizzes(),
    )


@app.route("/opencode")
def opencode_guide():
    """OpenCode V2 cheat-sheet with live config."""
    live = {"model": "?", "plugins": [], "tui_plugins": [], "agents": [], "mcp": []}
    try:
        cfg = json.loads((Path.home() / ".config" / "opencode" / "opencode.json").read_text(encoding="utf-8"))
        live["model"] = cfg.get("model", "?")
        live["plugins"] = cfg.get("plugins", cfg.get("plugin", []))
        live["agents"] = list(cfg.get("agents", cfg.get("agent", {})).keys())
        live["mcp"] = list(cfg.get("mcp", {}).get("servers", cfg.get("mcp", {})).keys())
    except Exception:
        pass
    try:
        cli = json.loads((Path.home() / ".config" / "opencode" / "cli.json").read_text(encoding="utf-8"))
        live["tui_plugins"] = cli.get("plugins", [])
    except Exception:
        pass
    return render_template("opencode.html", live=live)


@app.route("/api/data")
def api_data():
    return jsonify({
        "active": parse_active_state(),
        "learner": parse_learner_model(),
        "progress": parse_progress_analytics(),
        "gpa": parse_gpa_tracker(),
        "folder_stats": get_folder_stats(),
        "sessions": parse_sessions(),
        "buddy": parse_college_buddy(),
    })

def get_all_quizzes():
    """Scans all semester directories for available quizzes and enriches with attempt history."""
    semester_dirs = sorted([d for d in BASE.glob("0*_Semester_*") if d.is_dir()])
    if SEM1 not in semester_dirs:
        semester_dirs.insert(0, SEM1)
    quizzes = []
    history_summary = get_quiz_history(HUB).get("summary", {})
    subject_names = {
        "01_Cyber_Security": "الأمن السيبراني",
        "02_English_Language": "اللغة الإنجليزية",
        "03_Data_Mining": "تنقيب البيانات",
        "04_Advanced_Software_Eng": "هندسة البرمجيات المتقدمة",
        "05_Soft_Computing": "الحوسبة المرنة",
        "06_Artificial_Intelligence": "الذكاء الاصطناعي",
    }
    prof_names_ar = {
        "01_Cyber_Security": "أ.م.د. هدى لفتة مجيد",
        "02_English_Language": "أ.م.د. حيدر عكاب علوان",
        "03_Data_Mining": "أ.م.د. أحمد شاكر عبد الرضا",
        "04_Advanced_Software_Eng": "أ.م.د. علي فاهم نعمة",
        "05_Soft_Computing": "أ.د. عبد الهادي محمد ادخيل",
        "06_Artificial_Intelligence": "أ.د. سيف علي السعيدي",
    }
    for sem in semester_dirs:
        for qf in sorted(sem.glob("*/07_Quizzes_&_Anki/Quiz_*.json")):
            try:
                content = json.loads(qf.read_text(encoding="utf-8"))
                subject_folder = qf.parent.parent.name
                quiz_name = qf.stem
                h_info = history_summary.get(quiz_name, {})
                quizzes.append({
                    "semester": sem.name,
                    "semester_label": "كورس أول" if "Semester_1" in sem.name else "كورس ثاني",
                    "subject": subject_folder,
                    "subject_title": subject_names.get(subject_folder, subject_folder.replace("_", " ")),
                    "quiz_id": quiz_name,
                    "topic": content.get("topic", quiz_name),
                    "instructor": prof_names_ar.get(subject_folder, content.get("instructor", "")),
                    "instructor_ar": prof_names_ar.get(subject_folder, content.get("instructor", "")),
                    "questions_count": len(content.get("questions", [])),
                    "url": f"/quiz/{subject_folder}/{quiz_name}",
                    "attempts": h_info.get("attempts", 0),
                    "best_percentage": h_info.get("best_percentage"),
                    "best_score": h_info.get("best_score"),
                    "last_attempt": h_info.get("last_attempt")
                })
            except Exception:
                continue
    return quizzes


@app.route("/api/health")
def api_health():
    """Heartbeat endpoint for mobile and desktop clients to probe connectivity."""
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "client_ip": request.remote_addr,
        "lan_ip": get_lan_ip()
    }), 200


@app.route("/api/quiz/history")
def api_quiz_history():
    """Returns historical quiz submissions and aggregated per-quiz statistics."""
    return jsonify(get_quiz_history(HUB)), 200

@app.route("/api/quiz/list")
def api_quiz_list():
    """Returns a list of all available quizzes across all semesters."""
    return jsonify({"quizzes": get_all_quizzes()})


@app.route("/sw.js")
def service_worker_root():
    """Serves the PWA Service Worker at root scope ('/') so it can intercept ALL app navigation."""
    from flask import send_from_directory, make_response
    resp = make_response(send_from_directory(BASE / "91_Dashboard" / "static", "sw.js"))
    resp.headers["Content-Type"] = "application/javascript"
    resp.headers["Service-Worker-Allowed"] = "/"
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return resp


@app.route("/quiz")
def quiz_hub():
    """Hub landing page for interactive quizzes."""
    lan_ip = get_lan_ip()
    return render_template(
        "quiz.html",
        direct_mode=False,
        subject_id=None,
        quiz_id=None,
        lan_ip=lan_ip,
        available_quizzes=get_all_quizzes(),
    )


@app.route("/quiz/bookmarks")
def quiz_bookmarks_page():
    """Standalone, linkable saved-question library."""
    return render_template("quiz_library.html", page="bookmarks")


@app.route("/quiz/history")
@app.route("/quiz/history/<attempt_id>")
def quiz_history_page(attempt_id=None):
    """Standalone local attempt history and saved review view."""
    return render_template("quiz_library.html", page="history", attempt_id=attempt_id)


@app.route("/quiz/<subject_id>/<quiz_id>")
def quiz_direct(subject_id, quiz_id):
    """Direct view for a specific quiz."""
    lan_ip = get_lan_ip()
    return render_template(
        "quiz.html",
        direct_mode=True,
        subject_id=subject_id,
        quiz_id=quiz_id,
        lan_ip=lan_ip,
    )

@app.route("/api/quiz/<subject_id>/<quiz_id>")
def api_quiz_get(subject_id, quiz_id):
    clean_id = quiz_id[:-5] if quiz_id.endswith(".json") else quiz_id
    filename = f"{clean_id}.json"
    semester_dirs = sorted([d for d in BASE.glob("0*_Semester_*") if d.is_dir()])
    if SEM1 not in semester_dirs:
        semester_dirs.insert(0, SEM1)
    target_file = None

    for sem in semester_dirs:
        if not sem.is_dir():
            continue
        candidate_dir = (sem / subject_id / "07_Quizzes_&_Anki").resolve()
        if not candidate_dir.is_dir():
            # Fuzzy subject directory match
            for sdir in sem.iterdir():
                if sdir.is_dir() and subject_id.lower() in sdir.name.lower():
                    candidate_dir = (sdir / "07_Quizzes_&_Anki").resolve()
                    break
        if candidate_dir.is_dir():
            # 1. Exact match
            candidate_file = (candidate_dir / filename).resolve()
            try:
                candidate_file.relative_to(candidate_dir)
                if candidate_file.is_file():
                    target_file = candidate_file
                    break
            except ValueError:
                pass

            # 2. Case-insensitive or prefix slug match (e.g. Quiz_01 -> Quiz_01_Software_Crisis)
            for qf in candidate_dir.glob("Quiz_*.json"):
                stem_lower = qf.stem.lower()
                clean_lower = clean_id.lower()
                if stem_lower == clean_lower or stem_lower.startswith(clean_lower) or clean_lower in stem_lower:
                    target_file = qf
                    break
            if target_file:
                break

    if not target_file or not target_file.is_file():
        return jsonify({"error": "Quiz not found"}), 404

    try:
        content = target_file.read_text(encoding="utf-8")
        quiz_data = json.loads(content)
        return jsonify(quiz_data)
    except Exception as e:
        return jsonify({"error": f"Failed to load quiz: {str(e)}"}), 500
@app.route("/api/quiz/submit", methods=["POST"])
def api_quiz_submit():
    """Accepts JSON telemetry, ingests via quiz engine, returns result."""
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"status": "error", "message": "Invalid JSON payload"}), 400

    result = process_quiz_telemetry(payload, HUB)
    if result.get("status") == "error":
        return jsonify(result), 400

    return jsonify(result), 200


@app.route("/api/quiz/bookmarks", methods=["GET", "POST"])
def api_quiz_bookmarks():
    """GET or POST bookmarked question IDs from/to 00_STUDIO_HUB/quiz_bookmarks.json."""
    bookmarks_file = HUB / "quiz_bookmarks.json"
    if request.method == "POST":
        data = request.get_json(silent=True)
        if data is None:
            return jsonify({"status": "error", "message": "Invalid JSON"}), 400

        if isinstance(data, list):
            bookmarks = data
        elif isinstance(data, dict) and "bookmarks" in data:
            bookmarks = data["bookmarks"]
        else:
            return jsonify({"status": "error", "message": "Expected list or {'bookmarks': [...]}"}), 400

        try:
            HUB.mkdir(parents=True, exist_ok=True)
            tmp_file = HUB / f"quiz_bookmarks_{uuid.uuid4().hex[:8]}.tmp"
            tmp_file.write_text(json.dumps(bookmarks, indent=2), encoding="utf-8")
            tmp_file.replace(bookmarks_file)
            return jsonify({"status": "success", "bookmarks": bookmarks}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    # GET
    if not bookmarks_file.is_file():
        return jsonify([]), 200

    try:
        content = bookmarks_file.read_text(encoding="utf-8")
        bookmarks = json.loads(content)
        return jsonify(bookmarks), 200
    except Exception:
        return jsonify([]), 200


if __name__ == "__main__":
    lan_ip = get_lan_ip()
    print("Master Studio Dashboard")
    print(f"Local:   http://127.0.0.1:5000")
    print(f"Network: http://{lan_ip}:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
