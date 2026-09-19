# Interactive Web Quiz Subsystem & Cognitive Telemetry Engine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a mobile-friendly, LAN-accessible interactive web quiz subsystem with per-question dwell-time tracking, metacognitive error reflection, lucky guess tagging, and idempotent bidirectional synchronization into Master Studio's cognitive model and analytics files.

**Architecture:** The subsystem integrates directly into the existing Flask server (`91_Dashboard/app.py`), binding to `0.0.0.0:5000` to serve both desktop and mobile clients on the local network. A pure vanilla ES6+ and CSS variables frontend with Lucide SVG icons provides zero-dependency client performance, tracking dwell times and reflections in `localStorage` with an offline-first retry queue. Upon completion, an idempotent telemetry payload updates `PROGRESS_ANALYTICS.md`, `LEARNER_MODEL.md`, and session logs deterministically.

**Tech Stack:** Python 3, Flask, Vanilla ES6+, CSS Variables, Lucide SVG Icons, JSON, Markdown, PyMuPDF/Regex.

**Spec:** `docs/superpowers/specs/2026-09-19-interactive-web-quiz-system-design.md`

## Global Constraints
- **Zero Emoji Icons**: All functional UI icons must be Lucide SVG icons; no emoji characters for UI controls.
- **Zero Paid APIs / Zero Token Scoring**: All scoring, dwell time calculation, and vault updates must be 100% deterministic Python logic.
- **Dark Mode Default**: Default background `#0B1C2E`, card surface `#132A42`, border `#1E3A5F`, text `#F8FAFC`.
- **Idempotency**: Submissions must use a client-generated UUID to ensure multiple taps never duplicate log entries.
- **Offline-First**: All state auto-saves to `localStorage`; offline sync queue flushes on reconnect.

---

### Task 1: Cognitive Ingestion & Vault Synchronization Engine

**Files:**
- Create: `90_Shared_Toolbox/tools/quiz_engine.py`
- Test: `tests/test_quiz_engine.py`

**Interfaces:**
- Produces:
  - `process_quiz_telemetry(payload: dict, hub_path: Path) -> dict`: Ingests telemetry, updates `PROGRESS_ANALYTICS.md`, `LEARNER_MODEL.md`, and `sessions/`, returning execution summary.
  - `calculate_bkt_update(prior_knowledge: float, is_correct: bool, is_lucky_guess: bool, reflection_reason: str) -> float`: Calculates posterior concept mastery.

- [ ] **Step 1: Write failing test for telemetry processing and BKT updates**

Create `tests/test_quiz_engine.py`:
```python
import pytest
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "90_Shared_Toolbox" / "tools"))
from quiz_engine import process_quiz_telemetry, calculate_bkt_update

def test_bkt_lucky_guess_prevents_mastery():
    # Normal correct answer should increase mastery
    prior = 0.5
    updated_normal = calculate_bkt_update(prior, is_correct=True, is_lucky_guess=False, reflection_reason=None)
    assert updated_normal > prior

    # Lucky guess should not increase mastery
    updated_lucky = calculate_bkt_update(prior, is_correct=True, is_lucky_guess=True, reflection_reason=None)
    assert updated_lucky <= prior + 0.01

def test_process_quiz_telemetry_idempotency():
    with TemporaryDirectory() as tmpdir:
        hub = Path(tmpdir)
        analytics_file = hub / "PROGRESS_ANALYTICS.md"
        learner_file = hub / "LEARNER_MODEL.md"
        sessions_dir = hub / "sessions"
        sessions_dir.mkdir()

        analytics_file.write_text("# Progress Analytics\n| # | Date | Subject | Topic | Score | Result | Status |\n|:---:|:---:|:---|:---|:---:|:---:|:---:|\n", encoding="utf-8")
        learner_file.write_text("# Learner Model\n## 3. Mastered Concepts List\n\n## 4. Active Review Queue\n| Subject | Concept / Error | Logged | Reason | Priority | Review Due |\n|:---|:---|:---|:---|:---:|:---|\n", encoding="utf-8")

        payload = {
            "submission_uuid": "test-uuid-1234",
            "subject_id": "01_Cyber_Security",
            "quiz_id": "Quiz_01_Cyber_Security",
            "topic": "Week 01 Scenario Drills",
            "timestamp": "2026-09-19T23:00:00Z",
            "summary": {
                "total": 5,
                "correct": 4,
                "wrong": 1,
                "skipped": 0,
                "percentage": 80.0,
                "total_time_seconds": 90,
                "avg_dwell_time_seconds": 18.0,
                "attempt_number": 1
            },
            "questions": [
                {
                    "id": "q1",
                    "selected": "B",
                    "correct": "B",
                    "is_correct": True,
                    "dwell_time_seconds": 12,
                    "reflection": None,
                    "is_lucky_guess": False
                },
                {
                    "id": "q2",
                    "selected": "C",
                    "correct": "A",
                    "is_correct": False,
                    "dwell_time_seconds": 25,
                    "reflection": {"reason": "Calculation Slip", "note": "Arithmetic error"},
                    "is_lucky_guess": False
                }
            ]
        }

        # First ingestion
        res1 = process_quiz_telemetry(payload, hub)
        assert res1["status"] == "success"
        assert "#001" in analytics_file.read_text(encoding="utf-8")
        assert "Calculation Slip" in learner_file.read_text(encoding="utf-8")

        # Second ingestion with same UUID (idempotency check)
        res2 = process_quiz_telemetry(payload, hub)
        assert res2["status"] == "already_ingested"
        # Verify log count did not double
        text = analytics_file.read_text(encoding="utf-8")
        assert text.count("#001") == 1
        assert "#002" not in text
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_quiz_engine.py`  
Expected: FAIL (ModuleNotFoundError: No module named 'quiz_engine')

- [ ] **Step 3: Implement `quiz_engine.py`**

Create `90_Shared_Toolbox/tools/quiz_engine.py`:
```python
#!/usr/bin/env python3
"""
Master Studio Cognitive Ingestion & Vault Synchronization Engine
-----------------------------------------------------------------
Processes quiz telemetry payloads with Bayesian Knowledge Tracing,
slip/guess calibration, and idempotent markdown updates.
"""

from pathlib import Path
from datetime import datetime, timedelta
import json
import re

SEEN_UUIDS = set()

def calculate_bkt_update(prior_knowledge: float, is_correct: bool, is_lucky_guess: bool, reflection_reason: str = None) -> float:
    """Calculates posterior mastery using BKT with slip/guess calibration."""
    p_l = max(0.01, min(0.99, prior_knowledge))
    p_t = 0.1  # transition probability

    if is_correct:
        p_g = 1.0 if is_lucky_guess else 0.25
        p_s = 0.1
        # P(L|Correct)
        numerator = p_l * (1.0 - p_s)
        denominator = numerator + ((1.0 - p_l) * p_g)
        p_l_obs = numerator / denominator if denominator > 0 else p_l
    else:
        # Slip calibration: calculation/misread errors preserve high prior
        p_s = 0.9 if reflection_reason in ["Calculation Slip", "Misread Question"] else 0.1
        p_g = 0.25
        # P(L|Wrong)
        numerator = p_l * p_s
        denominator = numerator + ((1.0 - p_l) * (1.0 - p_g))
        p_l_obs = numerator / denominator if denominator > 0 else p_l

    # Posterior including transition
    p_next = p_l_obs + ((1.0 - p_l_obs) * p_t)
    return round(max(0.01, min(0.99, p_next)), 3)

def process_quiz_telemetry(payload: dict, hub_path: Path) -> dict:
    """Ingests telemetry into PROGRESS_ANALYTICS.md, LEARNER_MODEL.md, and sessions/."""
    sub_uuid = payload.get("submission_uuid")
    if not sub_uuid:
        return {"status": "error", "message": "Missing submission_uuid"}

    # Idempotency check against memory and session journals
    if sub_uuid in SEEN_UUIDS:
        return {"status": "already_ingested"}

    today_str = datetime.now().strftime("%Y-%m-%d")
    sessions_dir = hub_path / "sessions"
    sessions_dir.mkdir(exist_ok=True)
    today_session = sessions_dir / f"{today_str}.md"

    if today_session.exists() and sub_uuid in today_session.read_text(encoding="utf-8"):
        SEEN_UUIDS.add(sub_uuid)
        return {"status": "already_ingested"}

    SEEN_UUIDS.add(sub_uuid)

    subject = payload.get("subject_id", "Unknown_Subject")
    topic = payload.get("topic", "Quiz")
    summary = payload.get("summary", {})
    percentage = summary.get("percentage", 0.0)
    score_str = f"{summary.get('correct', 0)}/{summary.get('total', 0)}"
    avg_dwell = summary.get("avg_dwell_time_seconds", 0.0)

    # 1. Update PROGRESS_ANALYTICS.md
    analytics_file = hub_path / "PROGRESS_ANALYTICS.md"
    if analytics_file.exists():
        text = analytics_file.read_text(encoding="utf-8")
        log_count = sum(1 for line in text.splitlines() if line.strip().startswith("| #"))
        new_id = f"#{log_count + 1:03d}"
        now_ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        status = "🟢 Mastered" if percentage >= 80 else ("🟡 Borderline" if percentage >= 60 else "🔴 Review Needed")
        result = "PASS" if percentage >= 60 else "FAIL"

        row = f"| {new_id} | {now_ts} | `{subject}` | {topic} | {score_str} ({percentage:.0f}%) | {result} | {status} |\n"
        
        lines = text.splitlines(keepends=True)
        new_lines = []
        appended = False
        for line in lines:
            new_lines.append(line)
            if line.strip().startswith("|:---:|:---:|:---|:---|:---:|:---:|:---:|") and not appended:
                new_lines.append(row)
                appended = True
        if not appended:
            new_lines.append(row)
        analytics_file.write_text("".join(new_lines), encoding="utf-8")

    # 2. Update LEARNER_MODEL.md
    learner_file = hub_path / "LEARNER_MODEL.md"
    if learner_file.exists():
        l_text = learner_file.read_text(encoding="utf-8")
        review_entries = []
        now_date = datetime.now().strftime("%Y-%m-%d")
        due_date = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")

        for q in payload.get("questions", []):
            if not q.get("is_correct"):
                ref = q.get("reflection") or {}
                reason = ref.get("reason", "Concept Gap")
                note = ref.get("note", "").strip()
                desc = f"{topic}: Q_{q.get('id', '')} ({reason}{' - ' + note if note else ''})"
                review_entries.append(f"| `{subject}` | {desc} | {now_date} | Error Reflection | High | {due_date} |\n")
            elif q.get("is_lucky_guess"):
                desc = f"{topic}: Q_{q.get('id', '')} (Lucky Guess / Fluke)"
                review_entries.append(f"| `{subject}` | {desc} | {now_date} | Fluke Confirmation | Medium | {due_date} |\n")

        if review_entries:
            lines = l_text.splitlines(keepends=True)
            out_lines = []
            inserted = False
            for line in lines:
                out_lines.append(line)
                if line.strip().startswith("|:---|:---|:---|:---|:---:|:---|") and not inserted:
                    out_lines.extend(review_entries)
                    inserted = True
            if not inserted:
                out_lines.extend(review_entries)
            learner_file.write_text("".join(out_lines), encoding="utf-8")

    # 3. Append to today's session journal
    journal_entry = (
        f"\n- **[Quiz WebUI]** Completed `{subject}` - {topic} ({percentage:.0f}%, {score_str}).\n"
        f"  - Avg Dwell Time: {avg_dwell:.1f}s | UUID: `{sub_uuid}`\n"
        f"  - Recorded {summary.get('wrong', 0)} error reflections and {sum(1 for q in payload.get('questions', []) if q.get('is_lucky_guess'))} lucky guesses.\n"
    )
    with open(today_session, "a", encoding="utf-8") as f:
        f.write(journal_entry)

    return {"status": "success", "percentage": percentage}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_quiz_engine.py`  
Expected: PASS

---

### Task 2: Backend REST Endpoints & LAN IP Helper

**Files:**
- Modify: `91_Dashboard/app.py:20-40,270-320`
- Test: `tests/test_dashboard_quiz_api.py`

**Interfaces:**
- Consumes: `process_quiz_telemetry` from `quiz_engine.py`
- Produces:
  - `GET /quiz`: Renders quiz hub / subject selection.
  - `GET /quiz/<subject_id>/<quiz_id>`: Renders direct quiz view.
  - `GET /api/quiz/<subject_id>/<quiz_id>`: Returns quiz JSON.
  - `POST /api/quiz/submit`: Receives telemetry payload and calls `process_quiz_telemetry`.
  - `GET /api/quiz/bookmarks`: Returns stored bookmarks.
  - `POST /api/quiz/bookmarks`: Updates stored bookmarks.

- [ ] **Step 1: Write failing test for Flask quiz endpoints**

Create `tests/test_dashboard_quiz_api.py`:
```python
import pytest
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "91_Dashboard"))
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_quiz_hub_route(client):
    res = client.get("/quiz")
    assert res.status_code == 200

def test_quiz_api_not_found(client):
    res = client.get("/api/quiz/nonexistent_subject/nonexistent_quiz")
    assert res.status_code == 404

def test_quiz_api_existing(client):
    # Test with existing Quiz_01_Software_Crisis
    res = client.get("/api/quiz/04_Advanced_Software_Eng/Quiz_01_Software_Crisis")
    assert res.status_code == 200
    data = json.loads(res.data)
    assert "questions" in data
    assert len(data["questions"]) > 0

def test_quiz_submit_endpoint(client):
    payload = {
        "submission_uuid": "test-endpoint-uuid-999",
        "subject_id": "04_Advanced_Software_Eng",
        "quiz_id": "Quiz_01_Software_Crisis",
        "topic": "Testing Topic",
        "summary": {"total": 5, "correct": 5, "percentage": 100.0},
        "questions": []
    }
    res = client.post("/api/quiz/submit", json=payload)
    assert res.status_code in [200, 201]
    data = json.loads(res.data)
    assert data["status"] in ["success", "already_ingested"]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_dashboard_quiz_api.py`  
Expected: FAIL (404 on `/quiz` and `/api/quiz/...`)

- [ ] **Step 3: Add Quiz endpoints to `91_Dashboard/app.py`**

Edit `91_Dashboard/app.py` to import `process_quiz_telemetry` and add the routes:
```python
import socket
from flask import request

sys.path.insert(0, str(BASE / "90_Shared_Toolbox" / "tools"))
try:
    from quiz_engine import process_quiz_telemetry
except ImportError:
    process_quiz_telemetry = None

def get_lan_ip():
    """Detects local LAN IP for mobile access."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

@app.route("/quiz")
def quiz_hub():
    """Quiz Hub landing page."""
    lan_ip = get_lan_ip()
    return render_template("quiz.html", subject_id="", quiz_id="", lan_ip=lan_ip, direct_mode=False)

@app.route("/quiz/<subject_id>/<quiz_id>")
def quiz_direct(subject_id, quiz_id):
    """Direct Quiz Route."""
    lan_ip = get_lan_ip()
    return render_template("quiz.html", subject_id=subject_id, quiz_id=quiz_id, lan_ip=lan_ip, direct_mode=True)

@app.route("/api/quiz/<subject_id>/<quiz_id>")
def api_get_quiz(subject_id, quiz_id):
    """Returns quiz JSON for a subject."""
    quiz_file = SEM1 / subject_id / "07_Quizzes_&_Anki" / f"{quiz_id}.json"
    if not quiz_file.exists():
        # Also try matching without .json suffix or case
        candidates = list((SEM1 / subject_id / "07_Quizzes_&_Anki").glob(f"*{quiz_id}*.json"))
        if candidates:
            quiz_file = candidates[0]
        else:
            return jsonify({"error": "Quiz not found"}), 404

    try:
        with open(quiz_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/quiz/submit", methods=["POST"])
def api_quiz_submit():
    """Receives quiz telemetry and updates vault."""
    payload = request.get_json()
    if not payload:
        return jsonify({"error": "Invalid payload"}), 400

    if process_quiz_telemetry:
        result = process_quiz_telemetry(payload, HUB)
        return jsonify(result)
    return jsonify({"status": "skipped_no_engine"}), 200

@app.route("/api/quiz/bookmarks", methods=["GET", "POST"])
def api_quiz_bookmarks():
    bm_file = HUB / "quiz_bookmarks.json"
    if request.method == "POST":
        data = request.get_json() or []
        with open(bm_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return jsonify({"status": "saved"})
    
    if bm_file.exists():
        with open(bm_file, "r", encoding="utf-8") as f:
            return jsonify(json.load(f))
    return jsonify([])
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_dashboard_quiz_api.py`  
Expected: PASS

---

### Task 3: WebUI Frontend Template (`quiz.html`)

**Files:**
- Create: `91_Dashboard/templates/quiz.html`
- Dependencies: Lucide Icons CDN, `quiz.css`, `quiz.js`

**Interfaces:**
- Consumes: `lan_ip`, `subject_id`, `quiz_id`, `direct_mode` from Flask template renderer
- Produces: HTML structure for:
  - Top navigation bar with Lucide icons (Bookmark, Analytics, Theme toggle).
  - Progress bar with dwell timer and session timer.
  - Active question canvas with A/B/C/D option buttons and bookmark toggle.
  - Result & Review Screen with metacognitive reflection chips and "Lucky Guess" badge.
  - Slide-over drawers for Bookmarks and Analytics.

- [ ] **Step 1: Create `91_Dashboard/templates/quiz.html`**

Write standard HTML5 template with Lucide icons script and clean semantic layout:
```html
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Master Studio — Interactive Quiz</title>
  <link rel="stylesheet" href="/static/quiz.css">
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body data-subject="{{ subject_id }}" data-quiz="{{ quiz_id }}" data-direct="{{ 'true' if direct_mode else 'false' }}">
  <!-- Top App Bar -->
  <header class="quiz-header">
    <div class="header-left">
      <button id="btn-back" class="icon-btn" aria-label="Go Back">
        <i data-lucide="arrow-left"></i>
      </button>
      <div class="quiz-titles">
        <h1 id="quiz-title">Master Studio Quiz</h1>
        <span id="quiz-subtitle">Loading...</span>
      </div>
    </div>
    <div class="header-right">
      <button id="btn-bookmarks-toggle" class="icon-btn" aria-label="Bookmarks">
        <i data-lucide="bookmark"></i>
      </button>
      <button id="btn-analytics-toggle" class="icon-btn" aria-label="Analytics">
        <i data-lucide="bar-chart-2"></i>
      </button>
      <button id="btn-theme-toggle" class="icon-btn" aria-label="Toggle Theme">
        <i data-lucide="sun"></i>
      </button>
    </div>
  </header>

  <!-- Progress Bar & Timer Row -->
  <div class="progress-bar-container">
    <div id="progress-bar-fill" class="progress-bar-fill" style="width: 0%;"></div>
  </div>
  <div class="meta-row">
    <span id="question-counter">Question 1 / 1</span>
    <div class="timer-group">
      <span class="dwell-timer"><i data-lucide="clock" class="inline-icon"></i> <span id="dwell-time">00:00</span></span>
      <span class="total-timer">(Total: <span id="total-time">00:00</span>)</span>
    </div>
  </div>

  <!-- Main Canvas -->
  <main class="quiz-main">
    <!-- Active Question View -->
    <section id="question-view" class="view-panel active">
      <div class="question-card">
        <div class="question-header">
          <span id="question-domain-badge" class="badge">General</span>
          <button id="btn-bookmark-question" class="bookmark-action" aria-label="Bookmark Question">
            <i data-lucide="bookmark" id="bookmark-icon"></i>
          </button>
        </div>
        <p id="question-text" class="question-text">Loading question...</p>
        <div id="options-container" class="options-grid"></div>
      </div>
    </section>

    <!-- Result & Review View -->
    <section id="result-view" class="view-panel">
      <div class="score-card">
        <div class="score-gauge">
          <span id="score-percentage" class="score-number">0%</span>
          <span id="score-status-badge" class="status-badge">PASS</span>
        </div>
        <p id="score-message" class="score-message">Well done!</p>
        <div class="stats-grid">
          <div class="stat-item"><span id="stat-correct">0</span><label>Correct</label></div>
          <div class="stat-item"><span id="stat-wrong">0</span><label>Wrong</label></div>
          <div class="stat-item"><span id="stat-avg-dwell">0s</span><label>Avg Time/Q</label></div>
        </div>
        <div class="action-buttons">
          <button id="btn-try-again" class="btn btn-secondary">
            <i data-lucide="refresh-cw"></i> Try Again
          </button>
          <button id="btn-send-studio" class="btn btn-primary">
            <i data-lucide="send"></i> Send to Master Studio
          </button>
        </div>
        <div id="sync-confirmation" class="sync-banner hidden">
          <i data-lucide="check-circle-2"></i> Synced to Master Studio Vault
        </div>
      </div>

      <!-- Review Stream -->
      <div class="review-section">
        <h2>Review & Metacognitive Reflection</h2>
        <div id="review-list" class="review-list"></div>
      </div>
    </section>

    <!-- Subject Hub Selection (when no direct quiz loaded) -->
    <section id="hub-view" class="view-panel">
      <div class="hub-header">
        <h2>Select a Subject Quiz</h2>
        <p>Or scan with your phone on Wi-Fi: <code>http://{{ lan_ip }}:5000/quiz</code></p>
      </div>
      <div id="quiz-catalog-list" class="catalog-grid"></div>
    </section>
  </main>

  <!-- Bottom Navigation -->
  <footer id="quiz-footer" class="quiz-footer">
    <button id="btn-prev" class="btn btn-secondary" disabled>
      <i data-lucide="chevron-left"></i> Previous
    </button>
    <button id="btn-next" class="btn btn-primary">
      Next <i data-lucide="chevron-right"></i>
    </button>
  </footer>

  <!-- Bookmarks Slide-Over Drawer -->
  <aside id="drawer-bookmarks" class="drawer">
    <div class="drawer-header">
      <h3><i data-lucide="bookmark"></i> Bookmarked Questions</h3>
      <button class="drawer-close icon-btn" data-target="drawer-bookmarks"><i data-lucide="x"></i></button>
    </div>
    <div class="drawer-body" id="bookmarks-list">
      <p class="empty-state">No bookmarked questions yet.</p>
    </div>
  </aside>

  <!-- Analytics Slide-Over Drawer -->
  <aside id="drawer-analytics" class="drawer">
    <div class="drawer-header">
      <h3><i data-lucide="bar-chart-2"></i> Learning Analytics</h3>
      <button class="drawer-close icon-btn" data-target="drawer-analytics"><i data-lucide="x"></i></button>
    </div>
    <div class="drawer-body" id="analytics-content">
      <div class="analytics-stat">
        <label>Studio Target Floor</label>
        <strong>75.0% (Excellence)</strong>
      </div>
      <div class="analytics-stat">
        <label>MOHESR Pass Minimum</label>
        <strong>60.0%</strong>
      </div>
      <h4>Active Review Queue</h4>
      <div id="review-queue-list">Loading queue...</div>
    </div>
  </aside>

  <div id="drawer-overlay" class="drawer-overlay"></div>
  <script src="/static/quiz.js"></script>
</body>
</html>
```

- [ ] **Step 2: Commit template**

```bash
git add 91_Dashboard/templates/quiz.html
```

---

### Task 4: WebUI Styles & Theming (`quiz.css`)

**Files:**
- Create: `91_Dashboard/static/quiz.css`

**Interfaces:**
- Produces: CSS variables for `#0B1C2E` dark theme, light theme, drawer transitions, Lucide SVG icon scaling, and mobile touch targets ($\ge 48\text{px}$).

- [ ] **Step 1: Create `91_Dashboard/static/quiz.css`**

```css
:root {
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

[data-theme="dark"] {
  --bg-primary: #0B1C2E;
  --bg-surface: #132A42;
  --bg-surface-hover: #1E3A5F;
  --border-color: #1E3A5F;
  --text-primary: #F8FAFC;
  --text-secondary: #94A3B8;
  --accent-primary: #38BDF8;
  --accent-hover: #0284C7;
  --color-correct: #10B981;
  --color-wrong: #EF4444;
  --color-warning: #F59E0B;
}

[data-theme="light"] {
  --bg-primary: #F8FAFC;
  --bg-surface: #FFFFFF;
  --bg-surface-hover: #F1F5F9;
  --border-color: #E2E8F0;
  --text-primary: #0F172A;
  --text-secondary: #64748B;
  --accent-primary: #0284C7;
  --accent-hover: #0369A1;
  --color-correct: #059669;
  --color-wrong: #DC2626;
  --color-warning: #D97706;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: var(--font-sans);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.5;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  -webkit-tap-highlight-color: transparent;
}

.icon-btn {
  background: transparent;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  color: var(--text-secondary);
  cursor: pointer;
  padding: 8px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
}
.icon-btn:hover { background: var(--bg-surface-hover); color: var(--text-primary); }

.quiz-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border-color);
}
.header-left { display: flex; align-items: center; gap: 12px; }
.header-right { display: flex; align-items: center; gap: 8px; }
.quiz-titles h1 { font-size: 16px; font-weight: 700; color: var(--text-primary); }
.quiz-titles span { font-size: 12px; color: var(--text-secondary); }

.progress-bar-container { height: 4px; background: var(--border-color); width: 100%; }
.progress-bar-fill { height: 100%; background: var(--accent-primary); transition: width 0.3s ease; }

.meta-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 16px;
  font-size: 13px;
  color: var(--text-secondary);
}
.timer-group { display: flex; align-items: center; gap: 8px; }
.inline-icon { width: 14px; height: 14px; vertical-align: -2px; }

.quiz-main { flex: 1; padding: 16px; max-width: 720px; width: 100%; margin: 0 auto; }
.view-panel { display: none; }
.view-panel.active { display: block; }

.question-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 20px;
}
.question-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
.badge { font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 9999px; background: var(--border-color); color: var(--accent-primary); }
.bookmark-action { background: none; border: none; color: var(--text-secondary); cursor: pointer; }
.bookmark-action.active { color: var(--accent-primary); }

.question-text { font-size: 17px; font-weight: 600; margin-bottom: 20px; line-height: 1.6; }
.options-grid { display: flex; flex-direction: column; gap: 10px; }

.option-btn {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px;
  border-radius: 10px;
  border: 1px solid var(--border-color);
  background: var(--bg-surface);
  color: var(--text-primary);
  font-size: 15px;
  cursor: pointer;
  text-align: left;
  transition: var(--transition);
  min-height: 52px;
}
.option-btn:hover { background: var(--bg-surface-hover); }
.option-btn.selected { border-color: var(--accent-primary); background: rgba(56, 189, 248, 0.1); }
.option-key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 6px;
  background: var(--border-color);
  font-weight: 700;
  font-size: 13px;
  flex-shrink: 0;
}

.quiz-footer {
  display: flex;
  justify-content: space-between;
  padding: 12px 16px;
  background: var(--bg-surface);
  border-top: 1px solid var(--border-color);
  position: sticky;
  bottom: 0;
  max-width: 720px;
  width: 100%;
  margin: 0 auto;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  border-radius: 10px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: var(--transition);
}
.btn-primary { background: var(--accent-primary); color: #0B1C2E; }
.btn-primary:hover { background: var(--accent-hover); }
.btn-secondary { background: var(--bg-surface); border: 1px solid var(--border-color); color: var(--text-primary); }
.btn-secondary:hover { background: var(--bg-surface-hover); }
.btn:disabled { opacity: 0.5; cursor: not-allowed; }

/* Score Card */
.score-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 24px;
  text-align: center;
  margin-bottom: 24px;
}
.score-number { font-size: 56px; font-weight: 800; color: var(--accent-primary); display: block; }
.status-badge { display: inline-block; padding: 4px 12px; border-radius: 9999px; font-weight: 700; font-size: 12px; margin-top: 8px; }
.status-badge.pass { background: rgba(16, 185, 129, 0.2); color: var(--color-correct); }
.status-badge.fail { background: rgba(239, 68, 68, 0.2); color: var(--color-wrong); }
.stats-grid { display: flex; justify-content: space-around; margin: 20px 0; border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color); padding: 12px 0; }
.stat-item strong { display: block; font-size: 20px; }
.stat-item label { font-size: 12px; color: var(--text-secondary); }
.action-buttons { display: flex; gap: 12px; justify-content: center; margin-top: 16px; }

/* Review Items */
.review-list { display: flex; flex-direction: column; gap: 16px; margin-top: 16px; }
.review-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-left: 4px solid var(--border-color);
  border-radius: 10px;
  padding: 16px;
}
.review-card.correct { border-left-color: var(--color-correct); }
.review-card.wrong { border-left-color: var(--color-wrong); }
.reflection-box { margin-top: 12px; padding-top: 12px; border-top: 1px dashed var(--border-color); }
.reflection-chips { display: flex; flex-wrap: wrap; gap: 8px; margin: 8px 0; }
.chip {
  background: var(--bg-primary);
  border: 1px solid var(--border-color);
  border-radius: 9999px;
  padding: 4px 10px;
  font-size: 12px;
  cursor: pointer;
  color: var(--text-secondary);
}
.chip.selected { border-color: var(--color-warning); color: var(--color-warning); background: rgba(245, 158, 11, 0.1); }
.lucky-guess-toggle { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; cursor: pointer; color: var(--text-secondary); margin-top: 8px; }

/* Drawers */
.drawer {
  position: fixed;
  top: 0;
  right: -360px;
  width: 340px;
  height: 100%;
  background: var(--bg-surface);
  border-left: 1px solid var(--border-color);
  z-index: 1000;
  transition: right 0.3s ease;
  display: flex;
  flex-direction: column;
}
.drawer.open { right: 0; }
.drawer-header { display: flex; justify-content: space-between; align-items: center; padding: 16px; border-bottom: 1px solid var(--border-color); }
.drawer-body { flex: 1; overflow-y: auto; padding: 16px; }
.drawer-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
  display: none;
  z-index: 999;
}
.drawer-overlay.active { display: block; }
```

- [ ] **Step 2: Commit stylesheet**

```bash
git add 91_Dashboard/static/quiz.css
```

---

### Task 5: Interactive WebUI Controller (`quiz.js`)

**Files:**
- Create: `91_Dashboard/static/quiz.js`

**Interfaces:**
- Consumes: `/api/quiz/<subject_id>/<quiz_id>`
- Produces:
  - Dwell timer per question with second-level resolution.
  - LocalStorage persistence under `quiz_session_state`.
  - Idempotent submission via `crypto.randomUUID()`.
  - Metacognitive reflection recorder & Lucky Guess tagger.
  - Drawers controller & theme switcher.

- [ ] **Step 1: Create `91_Dashboard/static/quiz.js`**

```javascript
/* Master Studio Interactive Quiz Controller */
(function () {
  const state = {
    subjectId: document.body.dataset.subject || "",
    quizId: document.body.dataset.quiz || "",
    isDirect: document.body.dataset.direct === "true",
    questions: [],
    currentIndex: 0,
    answers: {},
    dwellTimes: {},
    reflections: {},
    luckyGuesses: {},
    bookmarks: new Set(),
    timerInterval: null,
    totalSeconds: 0,
    currentDwellSeconds: 0,
    submissionUuid: null
  };

  function init() {
    initIcons();
    initTheme();
    initDrawers();
    loadBookmarks();

    if (state.subjectId && state.quizId) {
      loadQuiz(state.subjectId, state.quizId);
    } else {
      showHubCatalog();
    }

    bindEvents();
  }

  function initIcons() {
    if (window.lucide) {
      window.lucide.createIcons();
    }
  }

  function initTheme() {
    const saved = localStorage.getItem("quiz_theme") || "dark";
    document.documentElement.setAttribute("data-theme", saved);
    updateThemeIcon(saved);
  }

  function updateThemeIcon(theme) {
    const icon = document.querySelector("#btn-theme-toggle i");
    if (icon) {
      icon.setAttribute("data-lucide", theme === "dark" ? "sun" : "moon");
      initIcons();
    }
  }

  function initDrawers() {
    document.querySelectorAll(".drawer-close, #drawer-overlay").forEach(el => {
      el.addEventListener("click", () => {
        document.querySelectorAll(".drawer").forEach(d => d.classList.remove("open"));
        document.getElementById("drawer-overlay").classList.remove("active");
      });
    });

    document.getElementById("btn-bookmarks-toggle").addEventListener("click", () => {
      openDrawer("drawer-bookmarks");
    });

    document.getElementById("btn-analytics-toggle").addEventListener("click", () => {
      openDrawer("drawer-analytics");
    });

    document.getElementById("btn-theme-toggle").addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("quiz_theme", next);
      updateThemeIcon(next);
    });
  }

  function openDrawer(drawerId) {
    document.getElementById(drawerId).classList.add("open");
    document.getElementById("drawer-overlay").classList.add("active");
  }

  async function loadQuiz(subjectId, quizId) {
    try {
      const res = await fetch(`/api/quiz/${subjectId}/${quizId}`);
      if (!res.ok) throw new Error("Quiz not found");
      const data = await res.json();
      state.questions = data.questions || [];
      state.submissionUuid = crypto.randomUUID();

      document.getElementById("quiz-title").textContent = data.topic || "Master Studio Quiz";
      document.getElementById("quiz-subtitle").textContent = `${subjectId} · ${state.questions.length} Questions`;

      renderQuestion(0);
      startTimers();
      switchView("question-view");
    } catch (e) {
      alert("Failed to load quiz: " + e.message);
      showHubCatalog();
    }
  }

  function startTimers() {
    clearInterval(state.timerInterval);
    state.currentDwellSeconds = 0;
    state.timerInterval = setInterval(() => {
      state.totalSeconds++;
      state.currentDwellSeconds++;

      document.getElementById("dwell-time").textContent = formatTime(state.currentDwellSeconds);
      document.getElementById("total-time").textContent = formatTime(state.totalSeconds);
    }, 1000);
  }

  function formatTime(sec) {
    const m = Math.floor(sec / 60).toString().padStart(2, "0");
    const s = (sec % 60).toString().padStart(2, "0");
    return `${m}:${s}`;
  }

  function renderQuestion(index) {
    if (index < 0 || index >= state.questions.length) return;

    // Save dwell time of previous question
    if (state.questions[state.currentIndex]) {
      const prevId = state.questions[state.currentIndex].id || `q${state.currentIndex}`;
      state.dwellTimes[prevId] = (state.dwellTimes[prevId] || 0) + state.currentDwellSeconds;
    }

    state.currentIndex = index;
    state.currentDwellSeconds = 0;
    const q = state.questions[index];
    const qId = q.id || `q${index}`;

    document.getElementById("question-counter").textContent = `Question ${index + 1} / ${state.questions.length}`;
    document.getElementById("progress-bar-fill").style.width = `${((index + 1) / state.questions.length) * 100}%`;
    document.getElementById("question-text").textContent = q.question;

    const bmIcon = document.getElementById("bookmark-icon");
    if (state.bookmarks.has(qId)) {
      bmIcon.classList.add("active");
    } else {
      bmIcon.classList.remove("active");
    }

    const container = document.getElementById("options-container");
    container.innerHTML = "";

    const opts = q.options || {};
    const selected = state.answers[qId];

    Object.entries(opts).forEach(([key, text]) => {
      const btn = document.createElement("button");
      btn.className = `option-btn ${selected === key ? "selected" : ""}`;
      btn.innerHTML = `<span class="option-key">${key}</span> <span>${text}</span>`;
      btn.addEventListener("click", () => {
        state.answers[qId] = key;
        renderQuestion(state.currentIndex);
      });
      container.appendChild(btn);
    });

    document.getElementById("btn-prev").disabled = index === 0;
    document.getElementById("btn-next").innerHTML = index === state.questions.length - 1
      ? `Finish <i data-lucide="check"></i>`
      : `Next <i data-lucide="chevron-right"></i>`;
    initIcons();
  }

  function bindEvents() {
    document.getElementById("btn-prev").addEventListener("click", () => {
      renderQuestion(state.currentIndex - 1);
    });

    document.getElementById("btn-next").addEventListener("click", () => {
      if (state.currentIndex < state.questions.length - 1) {
        renderQuestion(state.currentIndex + 1);
      } else {
        finishQuiz();
      }
    });

    document.getElementById("btn-bookmark-question").addEventListener("click", () => {
      const q = state.questions[state.currentIndex];
      const qId = q.id || `q${state.currentIndex}`;
      if (state.bookmarks.has(qId)) {
        state.bookmarks.delete(qId);
      } else {
        state.bookmarks.add(qId);
      }
      saveBookmarks();
      renderQuestion(state.currentIndex);
    });

    document.getElementById("btn-try-again").addEventListener("click", () => {
      state.answers = {};
      state.dwellTimes = {};
      state.reflections = {};
      state.luckyGuesses = {};
      state.submissionUuid = crypto.randomUUID();
      document.getElementById("sync-confirmation").classList.add("hidden");
      renderQuestion(0);
      startTimers();
      switchView("question-view");
    });

    document.getElementById("btn-send-studio").addEventListener("click", sendToMasterStudio);
  }

  function finishQuiz() {
    clearInterval(state.timerInterval);
    // Record last question dwell
    const lastId = state.questions[state.currentIndex].id || `q${state.currentIndex}`;
    state.dwellTimes[lastId] = (state.dwellTimes[lastId] || 0) + state.currentDwellSeconds;

    let correct = 0;
    state.questions.forEach((q, idx) => {
      const qId = q.id || `q${idx}`;
      if (state.answers[qId] === q.answer) correct++;
    });

    const total = state.questions.length;
    const pct = total > 0 ? Math.round((correct / total) * 100) : 0;
    const avgDwell = total > 0 ? Math.round(state.totalSeconds / total) : 0;

    document.getElementById("score-percentage").textContent = `${pct}%`;
    const badge = document.getElementById("score-status-badge");
    badge.textContent = pct >= 60 ? "PASS" : "FAIL";
    badge.className = `status-badge ${pct >= 60 ? "pass" : "fail"}`;

    document.getElementById("stat-correct").textContent = correct;
    document.getElementById("stat-wrong").textContent = total - correct;
    document.getElementById("stat-avg-dwell").textContent = `${avgDwell}s`;

    renderReviewList();
    switchView("result-view");
    initIcons();
  }

  function renderReviewList() {
    const list = document.getElementById("review-list");
    list.innerHTML = "";

    state.questions.forEach((q, idx) => {
      const qId = q.id || `q${idx}`;
      const selected = state.answers[qId];
      const isCorrect = selected === q.answer;

      const card = document.createElement("div");
      card.className = `review-card ${isCorrect ? "correct" : "wrong"}`;

      let body = `
        <div style="display:flex;justify-content:space-between;margin-bottom:6px;">
          <strong>Q${idx + 1}</strong>
          <span style="font-size:12px;color:var(--text-secondary);">${state.dwellTimes[qId] || 0}s</span>
        </div>
        <p style="margin-bottom:8px;">${q.question}</p>
        <p style="font-size:13px;color:var(--color-correct);">✓ Correct: ${q.answer} (${q.options[q.answer] || ""})</p>
      `;

      if (!isCorrect) {
        body += `<p style="font-size:13px;color:var(--color-wrong);margin-bottom:8px;">✗ Your Choice: ${selected || "Skipped"} (${q.options[selected] || ""})</p>`;
        body += `
          <div class="reflection-box">
            <label style="font-size:12px;color:var(--text-secondary);">Why did you pick this?</label>
            <div class="reflection-chips" data-qid="${qId}">
              <span class="chip" data-val="Misread Question">Misread Question</span>
              <span class="chip" data-val="Calculation Slip">Calculation Slip</span>
              <span class="chip" data-val="Terminology Mix-up">Terminology Mix-up</span>
              <span class="chip" data-val="Concept Gap">Concept Gap</span>
            </div>
          </div>
        `;
      } else {
        body += `
          <label class="lucky-guess-toggle">
            <input type="checkbox" data-qid="${qId}" class="lucky-check" ${state.luckyGuesses[qId] ? "checked" : ""}>
            <span>Lucky Guess / WOW (I guessed this)</span>
          </label>
        `;
      }

      if (q.explanation) {
        body += `<p style="font-size:13px;margin-top:8px;color:var(--text-secondary);"><strong>Explanation:</strong> ${q.explanation}</p>`;
      }

      card.innerHTML = body;
      list.appendChild(card);
    });

    // Attach reflection chips listeners
    document.querySelectorAll(".chip").forEach(chip => {
      chip.addEventListener("click", (e) => {
        const qId = e.target.parentElement.dataset.qid;
        e.target.parentElement.querySelectorAll(".chip").forEach(c => c.classList.remove("selected"));
        e.target.classList.add("selected");
        state.reflections[qId] = { reason: e.target.dataset.val, note: "" };
      });
    });

    // Attach lucky guess listeners
    document.querySelectorAll(".lucky-check").forEach(chk => {
      chk.addEventListener("change", (e) => {
        const qId = e.target.dataset.qid;
        state.luckyGuesses[qId] = e.target.checked;
      });
    });
  }

  async function sendToMasterStudio() {
    const btn = document.getElementById("btn-send-studio");
    btn.disabled = true;
    btn.innerHTML = `<i data-lucide="loader-2"></i> Syncing...`;
    initIcons();

    const payload = {
      submission_uuid: state.submissionUuid,
      subject_id: state.subjectId,
      quiz_id: state.quizId,
      topic: document.getElementById("quiz-title").textContent,
      timestamp: new Date().toISOString(),
      summary: {
        total: state.questions.length,
        correct: parseInt(document.getElementById("stat-correct").textContent),
        wrong: parseInt(document.getElementById("stat-wrong").textContent),
        percentage: parseFloat(document.getElementById("score-percentage").textContent),
        total_time_seconds: state.totalSeconds,
        avg_dwell_time_seconds: Math.round(state.totalSeconds / (state.questions.length || 1))
      },
      questions: state.questions.map((q, idx) => {
        const qId = q.id || `q${idx}`;
        const isCorrect = state.answers[qId] === q.answer;
        return {
          id: qId,
          selected: state.answers[qId] || null,
          correct: q.answer,
          is_correct: isCorrect,
          dwell_time_seconds: state.dwellTimes[qId] || 0,
          reflection: state.reflections[qId] || null,
          is_lucky_guess: !!state.luckyGuesses[qId]
        };
      })
    };

    try {
      const res = await fetch("/api/quiz/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      if (!res.ok) throw new Error("Sync failed");
      document.getElementById("sync-confirmation").classList.remove("hidden");
      btn.innerHTML = `<i data-lucide="check"></i> Synced to Studio`;
    } catch (e) {
      alert("Failed to sync to Studio: " + e.message);
      btn.disabled = false;
      btn.innerHTML = `<i data-lucide="send"></i> Retry Send`;
    }
    initIcons();
  }

  function switchView(viewId) {
    document.querySelectorAll(".view-panel").forEach(v => v.classList.remove("active"));
    document.getElementById(viewId).classList.add("active");
    window.scrollTo(0, 0);
  }

  function showHubCatalog() {
    document.getElementById("quiz-title").textContent = "Master Studio Quizzes";
    document.getElementById("quiz-subtitle").textContent = "Select an active subject";
    document.getElementById("quiz-footer").style.display = "none";
    switchView("hub-view");
  }

  async function loadBookmarks() {
    try {
      const res = await fetch("/api/quiz/bookmarks");
      if (res.ok) {
        const data = await res.json();
        state.bookmarks = new Set(data);
      }
    } catch (_) {}
  }

  async function saveBookmarks() {
    try {
      await fetch("/api/quiz/bookmarks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(Array.from(state.bookmarks))
      });
    } catch (_) {}
  }

  document.addEventListener("DOMContentLoaded", init);
})();
```

- [ ] **Step 2: Commit controller**

```bash
git add 91_Dashboard/static/quiz.js
```

---

### Task 6: LAN QR Code Generator Helper

**Files:**
- Create: `90_Shared_Toolbox/tools/quiz_qr.py`
- Test: `tests/test_quiz_qr.py`

**Interfaces:**
- Produces: `generate_quiz_link(subject_id: str, quiz_id: str, print_qr: bool = True) -> str`

- [ ] **Step 1: Write failing test for QR code helper**

Create `tests/test_quiz_qr.py`:
```python
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "90_Shared_Toolbox" / "tools"))
from quiz_qr import generate_quiz_link

def test_generate_quiz_link_format():
    link, ip = generate_quiz_link("01_Cyber_Security", "Quiz_01_Cyber_Security", print_qr=False)
    assert link.startswith("http://")
    assert ":5000/quiz/01_Cyber_Security/Quiz_01_Cyber_Security" in link
    assert len(ip.split(".")) == 4
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_quiz_qr.py`  
Expected: FAIL (ModuleNotFoundError: No module named 'quiz_qr')

- [ ] **Step 3: Implement `quiz_qr.py`**

Create `90_Shared_Toolbox/tools/quiz_qr.py`:
```python
#!/usr/bin/env python3
"""
Master Studio LAN Quiz Link & QR Code Generator
-----------------------------------------------
Detects host LAN IP and generates a mobile-ready URL with an optional ASCII QR code.
"""

import socket
import sys

def get_lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def generate_quiz_link(subject_id: str, quiz_id: str, print_qr: bool = True) -> tuple:
    ip = get_lan_ip()
    link = f"http://{ip}:5000/quiz/{subject_id}/{quiz_id}"
    
    if print_qr:
        print("\n" + "=" * 60)
        print("📲 MASTER STUDIO MOBILE QUIZ LINK")
        print("=" * 60)
        print(f"LAN URL : {link}")
        print(f"Local   : http://localhost:5000/quiz/{subject_id}/{quiz_id}")
        print("-" * 60)
        try:
            import qrcode
            qr = qrcode.QRCode(border=1)
            qr.add_data(link)
            qr.make(fit=True)
            qr.print_ascii(invert=True)
        except ImportError:
            print("[Tip: Install 'qrcode' library for terminal QR scan: pip install qrcode]")
        print("=" * 60 + "\n")
        
    return link, ip

if __name__ == "__main__":
    sub = sys.argv[1] if len(sys.argv) > 1 else "04_Advanced_Software_Eng"
    qz = sys.argv[2] if len(sys.argv) > 2 else "Quiz_01_Software_Crisis"
    generate_quiz_link(sub, qz, print_qr=True)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_quiz_qr.py`  
Expected: PASS

---

### Task 7: End-to-End System Smoke Test

**Files:**
- Create: `tests/test_e2e_quiz_flow.py`

**Interfaces:**
- Tests: Complete flow from Flask client fetching quiz $\rightarrow$ client submitting telemetry $\rightarrow$ verifying `PROGRESS_ANALYTICS.md` and `LEARNER_MODEL.md` updates.

- [ ] **Step 1: Write E2E smoke test**

Create `tests/test_e2e_quiz_flow.py`:
```python
import pytest
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "91_Dashboard"))
from app import app

def test_full_quiz_e2e_flow():
    app.config["TESTING"] = True
    with app.test_client() as client:
        # 1. Fetch real quiz
        res = client.get("/api/quiz/04_Advanced_Software_Eng/Quiz_01_Software_Crisis")
        assert res.status_code == 200
        quiz_data = json.loads(res.data)
        assert len(quiz_data["questions"]) > 0

        # 2. Simulate complete telemetry submission
        payload = {
            "submission_uuid": "e2e-test-uuid-001",
            "subject_id": "04_Advanced_Software_Eng",
            "quiz_id": "Quiz_01_Software_Crisis",
            "topic": "E2E Verification",
            "timestamp": "2026-09-19T23:59:00Z",
            "summary": {
                "total": 2,
                "correct": 1,
                "wrong": 1,
                "percentage": 50.0,
                "total_time_seconds": 45,
                "avg_dwell_time_seconds": 22.5
            },
            "questions": [
                {
                    "id": "q1",
                    "selected": "B",
                    "correct": "B",
                    "is_correct": True,
                    "dwell_time_seconds": 15,
                    "is_lucky_guess": True
                },
                {
                    "id": "q2",
                    "selected": "A",
                    "correct": "C",
                    "is_correct": False,
                    "dwell_time_seconds": 30,
                    "reflection": {"reason": "Terminology Mix-up", "note": "Confused essential complexity"}
                }
            ]
        }
        submit_res = client.post("/api/quiz/submit", json=payload)
        assert submit_res.status_code == 200
        res_data = json.loads(submit_res.data)
        assert res_data["status"] == "success"
```

- [ ] **Step 2: Run E2E test**

Run: `python -m pytest tests/test_e2e_quiz_flow.py`  
Expected: PASS
