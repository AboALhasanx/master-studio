#!/usr/bin/env python3
"""
Master Studio Dashboard
-----------------------
Flask web app that visualizes progress, mastery, and GPA from the Hub files.

Usage:
  python app.py
  Then open http://127.0.0.1:5000
"""

import math
import re
import json
import socket
import sys
import zlib
from pathlib import Path
from datetime import datetime, timezone
import uuid
from flask import Flask, render_template, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.serving import WSGIRequestHandler

# Ensure Shared Toolbox is importable
_toolbox_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox" / "tools"
if str(_toolbox_path) not in sys.path:
    sys.path.insert(0, str(_toolbox_path))
from quiz_engine import process_quiz_telemetry, get_quiz_history
from quiz_balancer import normalize_quiz_schema

app = Flask(__name__)

BASE = Path(__file__).resolve().parent.parent
HUB = BASE / "00_STUDIO_HUB"
SEM1 = BASE / "01_Semester_1"

# ---------------------------------------------------------------------------
# Hardening (docs/QA_DEFECTS_2026-09-27.md -> D-02/D-03/D-04/D-05)
#
#   D-02/D-03  schema + range validation before any state change
#              (OWASP Input Validation Cheat Sheet: allow-list, not clamp)
#   D-04       per-endpoint rate limiting on every write route
#              (OWASP API4:2023 Unrestricted Resource Consumption; NIST SP 800-204)
#   D-05       security headers + no version banner
#              (OWASP HTTP Headers Cheat Sheet)
#
# MAX_CONTENT_LENGTH -> Werkzeug answers 413 before a body is parsed, which is
# exactly the "maximum size of data on all incoming payloads" control API4 asks
# for. Largest quiz JSON on disk is ~84 KiB, so 1 MiB is a wide safety margin.
# ---------------------------------------------------------------------------
app.config["MAX_CONTENT_LENGTH"] = 1_048_576  # 1 MiB

# Must be set BEFORE the Limiter is constructed: the extension snapshots it at init.
# Tell clients how much budget they have left and when to retry, so a well behaved
# client (quiz.js offline queue) backs off instead of hammering a write endpoint.
app.config["RATELIMIT_HEADERS_ENABLED"] = True

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["1000 per minute"],  # safety valve for reads; writes get stricter limits
    storage_uri="memory://",  # single-process app: no DB overhead (0-database invariant)
)

# Response headers applied to every answer (D-05). CSP is HTML-only because it
# is meaningless for JSON; `style-src 'unsafe-inline'` stays because the
# templates use inline style attributes, while scripts are strictly 'self'.
_CSP_POLICY = (
    "default-src 'self'; "
    "script-src 'self'; "
    "style-src 'self' 'unsafe-inline'; "
    "img-src 'self' data: blob:; "
    "media-src 'self'; "
    "font-src 'self' data:; "
    "connect-src 'self'; "
    "worker-src 'self' blob:; "
    "manifest-src 'self'; "
    "object-src 'none'; "
    "base-uri 'self'; "
    "form-action 'self'; "
    "frame-ancestors 'none'"
)


class FingerprintlessRequestHandler(WSGIRequestHandler):
    """Serves without the `Server: Werkzeug/x.y Python/a.b` banner.

    BaseHTTPRequestHandler injects Server via version_string(); overriding it
    keeps the HTTP layer from fingerprinting the stack (OWASP HTTP Headers:
    "Remove this header or set non-informative values").
    """

    def version_string(self) -> str:
        return "MasterStudio"


@app.after_request
def security_headers(resp):
    resp.headers.setdefault("X-Content-Type-Options", "nosniff")
    resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    resp.headers.setdefault("X-Frame-Options", "DENY")
    resp.headers.setdefault(
        "Permissions-Policy", "geolocation=(), camera=(self), microphone=(), payment=()"
    )
    if resp.mimetype == "text/html":
        resp.headers.setdefault("Content-Security-Policy", _CSP_POLICY)
    return resp


@app.errorhandler(500)
def _internal_server_error(_exc):
    """OWASP Error Handling: one boundary, generic body, detail only in the log."""
    return jsonify({"status": "error", "message": "Internal error"}), 500


@app.errorhandler(429)
def _rate_limited(_exc):
    """JSON answer for a breached limit (D-04).

    Werkzeug would render an HTML error page; API clients only understand the
    JSON contract used everywhere else in this app. The Retry-After /
    X-RateLimit-* headers are attached by flask-limiter after this handler.
    """
    return jsonify({
        "status": "error",
        "message": "Rate limit exceeded — retry after the Retry-After header",
    }), 429

# ---------------------------------------------------------------------------
# Production-grade response optimization for slow LAN links:
#   1. Gzip text payloads (Werkzeug's dev server never compresses by default).
#   2. Long-lived caching for static assets + revalidation for HTML.
#      (Flask already emits strong ETags on /static, so repeats become 304s.)
# ---------------------------------------------------------------------------
_GZIP_MIMETYPES = frozenset(
    {
        "text/html",
        "text/css",
        "text/plain",
        "text/javascript",
        "application/javascript",
        "application/x-javascript",
        "application/json",
        "image/svg+xml",
    }
)


@app.after_request
def optimize_response(resp):
    try:
        if resp.mimetype == "text/html":
            resp.headers.setdefault("Cache-Control", "no-cache")
        if request.path.startswith("/static/"):
            resp.headers.setdefault("Cache-Control", "public, max-age=1800")

        accept = request.headers.get("Accept-Encoding", "")
        if (
            resp.status_code == 200
            and "gzip" in accept
            and "Content-Encoding" not in resp.headers
            and "Range" not in request.headers
            and resp.mimetype in _GZIP_MIMETYPES
        ):
            # send_file() responses run in direct-passthrough mode; release it
            # so the payload can be read and re-encoded.
            resp.direct_passthrough = False
            raw = resp.get_data()
            if len(raw) >= 1024:
                compressor = zlib.compressobj(9, zlib.DEFLATED, 16 + zlib.MAX_WBITS)
                packed = compressor.compress(raw) + compressor.flush()
                if len(packed) < len(raw):
                    resp.set_data(packed)
                    resp.headers["Content-Encoding"] = "gzip"
                    resp.headers["Content-Length"] = str(len(packed))
                    vary = resp.headers.get("Vary")
                    resp.headers["Vary"] = (
                        f"{vary}, Accept-Encoding" if vary else "Accept-Encoding"
                    )
    except Exception:
        # Never let transport optimization break a response.
        pass
    return resp


def read_file(path):
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


_SAFE_VAULT_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 _\-]{0,99}$")


def is_safe_vault_name(name) -> bool:
    """Reject path separators, '..' and other traversal characters in
    client-controlled vault folder/file names (subject_id, quiz_id)."""
    return isinstance(name, str) and bool(_SAFE_VAULT_NAME.match(name))


def safe_json_for_html(obj) -> str:
    """Serializes object to JSON safely for embedding inside HTML <script> tags."""
    dumped = json.dumps(obj, ensure_ascii=False)
    return dumped.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")


# ---------------------------------------------------------------------------
# Input validation (D-02 / D-03)
# OWASP Input Validation Cheat Sheet: validate type, range and length against
# an explicit schema BEFORE mutating state, and reject — never silently clamp.
# A clamped value still writes a poisoned attempt into quiz_history.json and the
# session journal, which then feeds the BKT mastery model.
# ---------------------------------------------------------------------------
_BOOKMARK_MAX_ENTRIES = 5000
_BOOKMARK_MAX_KEY_LEN = 400
_MAX_QUESTIONS = 500  # a real quiz bank never exceeds this (largest on disk: 30)
_MAX_SECONDS = 86400.0  # no single session/dwell can exceed 24h


def _is_number(value) -> bool:
    """Finite int/float (bools are rejected: isinstance(True, int) is True)."""
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _is_count(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def validate_telemetry(payload: dict) -> str | None:
    """Type/range gate for POST /api/quiz/submit. Returns None when valid,
    otherwise the human-readable reason the caller must answer 400."""
    errors = []

    for key, limit in (
        ("submission_uuid", 64),
        ("subject_id", 120),
        ("quiz_id", 120),
        ("topic", 300),
        ("finished_at", 40),
    ):
        value = payload.get(key)
        if value is None:
            continue
        if not isinstance(value, str):
            errors.append(f"{key} must be a string")
        elif len(value) > limit:
            errors.append(f"{key} exceeds {limit} characters")
        elif any(ord(ch) < 32 for ch in value):
            errors.append(f"{key} must not contain control characters")

    def check_number(value, name: str, lo: float, hi: float) -> None:
        if value is None:
            return
        if not _is_number(value):
            errors.append(f"{name} must be a finite number")
        elif not lo <= float(value) <= hi:
            errors.append(f"{name} must be between {lo:g} and {hi:g}")

    def check_count(value, name: str, hi: int) -> None:
        if value is None:
            return
        if not _is_count(value):
            errors.append(f"{name} must be an integer")
        elif not 0 <= value <= hi:
            errors.append(f"{name} must be between 0 and {hi}")

    def check_score_pair(correct, total, label: str) -> None:
        if _is_count(correct) and _is_count(total) and correct > total:
            errors.append(f"{label}: correct cannot exceed total")

    def check_summary(summary, prefix: str) -> None:
        if not isinstance(summary, dict):
            errors.append(f"{prefix}summary must be an object")
            return
        check_number(summary.get("percentage"), f"{prefix}percentage", 0.0, 100.0)
        check_count(summary.get("total"), f"{prefix}total", _MAX_QUESTIONS)
        check_count(summary.get("correct"), f"{prefix}correct", _MAX_QUESTIONS)
        check_count(summary.get("wrong"), f"{prefix}wrong", _MAX_QUESTIONS)
        check_number(summary.get("session_duration_seconds"),
                     f"{prefix}session_duration_seconds", 0.0, _MAX_SECONDS)
        check_number(summary.get("avg_dwell_time_seconds"),
                     f"{prefix}avg_dwell_time_seconds", 0.0, _MAX_SECONDS)
        check_score_pair(summary.get("correct"), summary.get("total"), prefix or "summary")

    # Top-level legacy fields (older clients and hostile payloads share this shape).
    check_number(payload.get("percentage"), "percentage", 0.0, 100.0)
    check_count(payload.get("total"), "total", _MAX_QUESTIONS)
    check_count(payload.get("score"), "score", _MAX_QUESTIONS)
    check_score_pair(payload.get("score"), payload.get("total"), "top level")
    check_number(payload.get("session_duration_seconds"),
                 "session_duration_seconds", 0.0, _MAX_SECONDS)

    if payload.get("summary") is not None:
        check_summary(payload.get("summary"), "")

    questions = payload.get("questions")
    if questions is not None:
        if not isinstance(questions, list):
            errors.append("questions must be a list")
        elif len(questions) > _MAX_QUESTIONS:
            errors.append(f"questions exceeds {_MAX_QUESTIONS} entries")
        else:
            for i, item in enumerate(questions):
                if not isinstance(item, dict):
                    errors.append(f"questions[{i}] must be an object")
                    break
                check_number(item.get("dwell_time_seconds"),
                             f"questions[{i}].dwell_time_seconds", 0.0, _MAX_SECONDS)

    return "; ".join(errors) if errors else None


def validate_bookmarks(bookmarks) -> str | None:
    """Shape gate for POST /api/quiz/bookmarks (D-02).

    The endpoint performs a full-file replace, so anything it accepts becomes
    the truth. Accepted entries are exactly what quiz.js/quiz-library.js write:
    a plain question key (legacy) or a `{k, n, question_data}` object.
    """
    if not isinstance(bookmarks, list):
        return "bookmarks must be a list"
    if len(bookmarks) > _BOOKMARK_MAX_ENTRIES:
        return f"bookmarks exceeds {_BOOKMARK_MAX_ENTRIES} entries"

    for i, item in enumerate(bookmarks):
        if isinstance(item, str):
            if not 0 < len(item) <= _BOOKMARK_MAX_KEY_LEN:
                return f"bookmarks[{i}] key must be 1-{_BOOKMARK_MAX_KEY_LEN} characters"
            continue
        if not isinstance(item, dict):
            return f"bookmarks[{i}] must be a question key string or a bookmark object"
        key = item.get("k")
        if not isinstance(key, str) or not 0 < len(key) <= _BOOKMARK_MAX_KEY_LEN:
            return f"bookmarks[{i}].k must be a 1-{_BOOKMARK_MAX_KEY_LEN} character string"
        index = item.get("n")
        if index is not None and (not _is_count(index) or index < 0):
            return f"bookmarks[{i}].n must be a non-negative integer"
        data = item.get("question_data")
        if data is not None and not isinstance(data, dict):
            return f"bookmarks[{i}].question_data must be an object"
        if item.get("subject") is not None and not isinstance(item.get("subject"), str):
            return f"bookmarks[{i}].subject must be a string"
        if item.get("quiz") is not None and not isinstance(item.get("quiz"), str):
            return f"bookmarks[{i}].quiz must be a string"
    return None


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
    """Count content files per subject (excluding raw materials).

    Index/plan/build scaffolding (*Plan*, *Index*, *Build*) is excluded from
    the notes count so the dashboard reports real study notes, not meta files.
    """
    _NON_NOTE_HINTS = ("plan", "index", "build")
    stats = {}
    if not SEM1.exists():
        return stats
    for subj in sorted(SEM1.iterdir()):
        if not subj.is_dir():
            continue
        all_notes = list((subj / "03_Study_Notes").glob("*.md")) if (subj / "03_Study_Notes").exists() else []
        notes = [p for p in all_notes
                 if not any(h in p.stem.lower() for h in _NON_NOTE_HINTS)]
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
    live = {"model": "?", "version": "", "plugins": [], "tui_plugins": [], "agents": [], "mcp": []}
    try:
        cfg = json.loads((Path.home() / ".config" / "opencode" / "opencode.json").read_text(encoding="utf-8"))
        live["model"] = cfg.get("model", "?")
        live["version"] = str(cfg.get("version", ""))
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


@app.route("/api/quiz/bundle")
def api_quiz_bundle():
    """Consolidated curriculum bundle endpoint for batch offline importing."""
    raw_sem = request.args.get("semester", "1")
    try:
        sem_target = int(raw_sem)
    except (ValueError, TypeError):
        sem_target = 1

    sem_folder = f"0{sem_target}_Semester_{sem_target}"
    target_sem_dir = BASE / sem_folder
    if not target_sem_dir.is_dir():
        semester_dirs = sorted([d for d in BASE.glob(f"0{sem_target}_Semester_*") if d.is_dir()])
        target_sem_dir = semester_dirs[0] if semester_dirs else (BASE / "01_Semester_1")

    quizzes_payload = []
    for qf in sorted(target_sem_dir.glob("*/07_Quizzes_&_Anki/Quiz_*.json")):
        try:
            content = json.loads(qf.read_text(encoding="utf-8"))
            subj = qf.parent.parent.name
            normalized = normalize_quiz_schema(content, subject_id=subj, quiz_id=qf.stem)
            quizzes_payload.append(normalized)
        except Exception:
            continue

    bundle = {
        "bundle_version": 2,
        "exported_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "semester": sem_target,
        "total_quizzes": len(quizzes_payload),
        "quizzes": quizzes_payload,
    }
    return jsonify(bundle), 200


@app.route("/sw.js")
def service_worker_root():
    """Serves the PWA Service Worker at root scope ('/') so it can intercept ALL app navigation."""
    from flask import send_from_directory, make_response
    resp = make_response(send_from_directory(BASE / "91_Dashboard" / "static", "sw.js"))
    resp.headers["Content-Type"] = "application/javascript"
    resp.headers["Service-Worker-Allowed"] = "/"
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return resp


@app.route("/quiz", methods=["GET", "POST"])
def quiz_hub():
    """Hub landing page for interactive quizzes, supporting Web Share Target POST."""
    lan_ip = get_lan_ip()
    shared_quizzes = []
    if request.method == "POST":
        files = request.files.getlist("quiz_files")
        for f in files:
            try:
                raw = json.loads(f.read().decode("utf-8"))
                if isinstance(raw, dict):
                    if "quizzes" in raw and isinstance(raw["quizzes"], list):
                        shared_quizzes.extend(raw["quizzes"])
                    elif "questions" in raw and isinstance(raw["questions"], list):
                        shared_quizzes.append(raw)
            except Exception:
                continue
    return render_template(
        "quiz.html",
        direct_mode=False,
        subject_id=None,
        quiz_id=None,
        lan_ip=lan_ip,
        available_quizzes=get_all_quizzes(),
        shared_quizzes=safe_json_for_html(shared_quizzes) if shared_quizzes else None,
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
    """Serve one quiz JSON by id (D-01 hardened).

    Every client-controlled path component is resolved inside a boundary that
    converts filesystem errors into 404 JSON: a malformed name must never reach
    the client as a 500 with a traceback in the log.
    """
    try:
        return _resolve_quiz_payload(subject_id, quiz_id)
    except (OSError, ValueError, UnicodeError) as exc:
        app.logger.warning("Rejected invalid quiz path subject=%r quiz=%r: %s",
                           subject_id, quiz_id, exc)
        return jsonify({"error": "Quiz not found"}), 404


def _resolve_quiz_payload(subject_id, quiz_id):
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
        quiz_data = normalize_quiz_schema(quiz_data, subject_id=target_file.parent.parent.name, quiz_id=target_file.stem)
        return jsonify(quiz_data)
    except json.JSONDecodeError:
        # A corrupt file on disk is a server-side defect: 500, generic body.
        app.logger.exception("Failed to parse quiz %s", target_file)
        return jsonify({"error": "Failed to load quiz"}), 500
    except (OSError, ValueError, UnicodeError) as exc:
        app.logger.warning("Unreadable quiz file %s: %s", target_file, exc)
        return jsonify({"error": "Quiz not found"}), 404
    except Exception:
        # Detail stays in the log only (OWASP Error Handling Cheat Sheet).
        app.logger.exception("Failed to serve quiz %s", target_file)
        return jsonify({"error": "Failed to load quiz"}), 500
@app.route("/api/quiz/submit", methods=["POST"])
@limiter.limit("60 per minute")
def api_quiz_submit():
    """Accepts JSON telemetry, ingests via quiz engine, returns result."""
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"status": "error", "message": "Invalid JSON payload"}), 400

    # D-03: reject out-of-range telemetry instead of clamping it — a clamped
    # value still poisons quiz_history.json, the journal and the BKT model.
    reason = validate_telemetry(payload)
    if reason:
        app.logger.warning("Rejected telemetry (%s): %s", payload.get("submission_uuid"), reason)
        return jsonify({"status": "error", "message": f"Invalid telemetry payload: {reason}"}), 400

    try:
        result = process_quiz_telemetry(payload, HUB)
    except Exception as e:
        # Persistence failure: answer 5xx so the PWA keeps the submission
        # queued in QuizVault and retries later instead of losing it.
        app.logger.exception("Telemetry ingestion failed")
        return jsonify({"status": "error", "message": f"Persistence failure: {e}"}), 500

    if result.get("status") == "error":
        return jsonify(result), 400

    return jsonify(result), 200



@app.route("/api/quiz/import", methods=["POST"])
@limiter.limit("30 per minute")
def api_quiz_import():
    """
    Receives a normalized quiz JSON from mobile client (e.g. from Telegram or file manager)
    and saves it into the canonical subject vault on the PC.
    """
    payload = request.get_json(silent=True)
    if not payload and request.files:
        f = request.files.get("quiz_file") or request.files.get("file")
        if f:
            try:
                payload = json.loads(f.read().decode("utf-8"))
            except Exception:
                payload = None

    if not isinstance(payload, dict):
        return jsonify({"status": "error", "message": "Invalid JSON quiz payload"}), 400

    imported_quizzes = []
    if "quizzes" in payload and isinstance(payload["quizzes"], list):
        raw_list = payload["quizzes"]
    elif "questions" in payload and isinstance(payload["questions"], list):
        raw_list = [payload]
    else:
        return jsonify({"status": "error", "message": "No valid quiz or questions found"}), 400

    for item in raw_list:
        if not isinstance(item, dict):
            continue
        subj = item.get("subject_id") or item.get("subject") or "00_STUDIO_HUB"
        quiz_id = item.get("quiz_id") or "Quiz_Imported"
        if not is_safe_vault_name(subj) or not is_safe_vault_name(quiz_id):
            return jsonify({
                "status": "error",
                "message": f"Invalid subject_id or quiz_id (path traversal rejected): {subj!r} / {quiz_id!r}"
            }), 400
        norm = normalize_quiz_schema(item, subject_id=subj, quiz_id=quiz_id)
        try:
            sem_num = int(norm.get("semester", 1))
        except (TypeError, ValueError):
            return jsonify({"status": "error", "message": f"Invalid semester: {norm.get('semester')!r}"}), 400
        if not 1 <= sem_num <= 9:
            return jsonify({"status": "error", "message": f"Invalid semester: {sem_num}"}), 400

        sem_dir = BASE / f"0{sem_num}_Semester_{sem_num}"
        target_dir = sem_dir / subj / "07_Quizzes_&_Anki"
        if not target_dir.is_dir():
            for sdir in sem_dir.glob("*"):
                if sdir.is_dir() and subj.lower() in sdir.name.lower():
                    target_dir = sdir / "07_Quizzes_&_Anki"
                    break
        target_file = target_dir / f"{quiz_id}.json"
        # Collision guard: a mobile import must never silently overwrite an
        # existing bank. Identical payloads are idempotent no-ops; differing
        # ones take the first free Quiz_<name>_N slot, reported back to mobile.
        note = None
        if target_file.is_file():
            try:
                identical = json.loads(target_file.read_text(encoding="utf-8")) == norm
            except Exception:
                identical = False
            if identical:
                imported_quizzes.append({
                    "subject_id": subj,
                    "quiz_id": quiz_id,
                    "path": str(target_file.relative_to(BASE)),
                    "questions_count": len(norm.get("questions", [])),
                    "note": "already present (identical payload)",
                })
                continue
            suffix = 2
            while (target_dir / f"{quiz_id}_{suffix}.json").is_file():
                suffix += 1
            quiz_id = f"{quiz_id}_{suffix}"
            norm["quiz_id"] = quiz_id
            target_file = target_dir / f"{quiz_id}.json"
            note = f"auto-renamed to avoid overwrite: {quiz_id}.json"
        try:
            target_file.resolve().relative_to(BASE.resolve())
        except ValueError:
            return jsonify({
                "status": "error",
                "message": "Resolved import path escapes the vault root"
            }), 400
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file.write_text(json.dumps(norm, ensure_ascii=False, indent=2), encoding="utf-8")
        entry = {
            "subject_id": subj,
            "quiz_id": quiz_id,
            "path": str(target_file.relative_to(BASE)),
            "questions_count": len(norm.get("questions", []))
        }
        if note:
            entry["note"] = note
        imported_quizzes.append(entry)

    return jsonify({
        "status": "success",
        "message": f"Successfully imported {len(imported_quizzes)} quizzes into PC vault",
        "imported": imported_quizzes
    }), 200

@app.route("/api/quiz/bookmarks", methods=["GET", "POST"])
@limiter.limit("60 per minute")
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

        # D-02: this endpoint replaces the whole file, so the payload becomes
        # the truth. Validate the shape before touching disk.
        reason = validate_bookmarks(bookmarks)
        if reason:
            return jsonify({"status": "error", "message": reason}), 400

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
    import os
    lan_ip = get_lan_ip()
    debug_mode = os.environ.get("FLASK_DEBUG", "0").lower() in ("1", "true", "yes")
    print("Master Studio Dashboard")
    print(f"Local:   http://127.0.0.1:5000")
    print(f"Network: http://{lan_ip}:5000")
    if debug_mode:
        print("[WARNING] Running with FLASK_DEBUG enabled. Do not expose to untrusted networks.")
    # use_reloader=False: the watchdog reloader raced on file churn and killed the
    # server silently (exit 1) twice mid-session while the student was testing.
    # Restart manually after editing app.py instead.
    app.run(host="0.0.0.0", port=5000, debug=debug_mode, threaded=True, use_reloader=False,
            request_handler=FingerprintlessRequestHandler)
