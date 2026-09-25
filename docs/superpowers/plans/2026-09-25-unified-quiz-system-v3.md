# Unified Dual-Mode Quizzing Architecture & PWA Overhaul (v3 Plan)

- **Target App:** Master Studio Quizzing Subsystem (`MCS Quiz`)
- **Version:** v3 (Production-Grade Unified Engineering)
- **Date:** 2026-09-25
- **Execution Model:** Subagent-driven or step-by-step TDD with atomic verification gates.

---

## 1. Executive Summary & Design System

### 1.1. Core Identity & 2026 Icon Standard
- **App Name:** `MCS Quiz` (Short, clean, fits Android launcher grid without truncating).
- **Theme Palette:** Deep Obsidian Canvas (`#0A0E17`), Precision Border (`#1E293B`), Focal Glyph in Ice-White (`#F8FAFC`) with Electric Cyan (`#38BDF8`) dynamic checkmark/chevron.
- **Design Philosophy:** Bold minimalism (Linear/Raycast aesthetic) with high contrast. Zero washed-out transparency or blurred discs. 100% compliant with Android maskable safe zones (glyph within central 66% circle).

### 1.2. Unified Architecture (Ports & Adapters)
- Single source of truth for UI, Arabic BiDi typography, dwell timers, and option shuffling.
- **Two Pluggable Adapters:**
  - **Online Adapter (PC-Connected via USB / LAN):** Interacts with Flask on `0.0.0.0:5000`, streams telemetry to `quiz_history.json` and `sessions/YYYY-MM-DD.md`, and enables real-time AI agent debriefs.
  - **Offline Adapter (Standalone on Campus / Bus):** Consumes pre-synced JSONs from `phone_sync.py` or device storage, runs with local timers, and queues telemetry for automatic background sync upon reconnecting to the PC.

---

## 2. Implementation Phases & Task Breakdown

### Phase 1: Identity & PWA Manifest Assets
- [ ] **Task 1.1: Verify & Commit Generated 2026 Icons**
  - Verify `icon-192.png` and `icon-512.png` (high-contrast Option C: "The Precision Dual-Tone Q / Checkmark").
  - Confirm `manifest.json` and `manifest-quiz.json` specify `MCS Quiz` and `#0A0E17` theme color.
  - Update `quiz.html` `<title>` and `<meta name="theme-color">`.

### Phase 2: Network & Link Resolution Hardening (`quiz_qr.py`)
- [ ] **Task 2.1: Intelligent NIC & USB Detection**
  - Replace naive `s.connect(("8.8.8.8", 80))` with physical adapter enumeration (prioritize `192.168.x.x` / `172.x.x.x`, filter out WireGuard/VPN `10.x.x.x`).
  - Detect active USB ADB devices via `adb devices`:
    - When connected: Automatically execute `adb reverse tcp:5000 tcp:5000` and display `http://localhost:5000/quiz/<Subject>/<Quiz>`.
- [ ] **Task 2.2: Fuzzy Slug Resolution in Link Generator**
  - Allow `python quiz_qr.py 04_Advanced_Software_Eng Quiz_01` to automatically resolve to `Quiz_01_Software_Crisis.json`.

### Phase 3: Server Listener & Data Layer (`app.py`, `quiz_engine.py`)
- [ ] **Task 3.1: Heartbeat & Health Check Endpoint**
  - Add `GET /api/health` returning `{"status": "ok", "timestamp": "...", "client_ip": "..."}`.
- [ ] **Task 3.2: Fuzzy Routing in `api_quiz_get`**
  - Allow slug prefix matching so `/api/quiz/<subject>/Quiz_01` resolves `Quiz_01_Software_Crisis.json` instead of 404.
- [ ] **Task 3.3: Structured Persistence (`quiz_history.json`)**
  - In `quiz_engine.py`, atomically append structured records to `00_STUDIO_HUB/quiz_history.json` on `POST /api/quiz/submit`.
  - Wire `calculate_bkt_update()` into `process_quiz_telemetry()` to log updated mastery probabilities alongside session entries.
- [ ] **Task 3.4: History Query Endpoint**
  - Add `GET /api/quiz/history` to provide aggregated scores and attempts per quiz to the client.

### Phase 4: Frontend UX & State Separation (`quiz.html`, `quiz.js`, `quiz.css`)
- [ ] **Task 4.1: Clean Up Leaked Scaffolding**
  - Set `#local-file-input` to `display: none !important;` to eliminate the 6x6 pixel gray button leak on mobile Chromium.
- [ ] **Task 4.2: Full Separation of Catalog Hub vs. Quiz Session**
  - In `quiz.js`: When `direct_mode === false`, hide topic banner, progress section, and quiz start screen. Show the clean catalog with subject filter chips.
  - Remove `getFallbackQuizData()` and phantom timers from the catalog view.
- [ ] **Task 4.3: Start Screen Header De-duplication**
  - Keep `.topic-banner` and `.progress-section` hidden while `#quiz-start-view` is active. Show them only when `btn-start-quiz` is clicked.
- [ ] **Task 4.4: Live Sync Status Badge**
  - Add header pill: 🟢 `Live Sync (PC Connected)` when `/api/health` succeeds, transitioning to 🟡 `Offline Mode` when disconnected.
  - Automatically flush offline submission queue on reconnection.

### Phase 5: Verification & Quality Gate
- [ ] **Task 5.1: Pytest Suite**
  - Run `pytest tests/` ensuring 100% pass across quiz engine, balancer, and API routes.
- [ ] **Task 5.2: Mobile Accessibility Tree Audit**
  - Inspect Android UI hierarchy via `adb shell uiautomator dump` verifying zero visual leaks and correct accessibility roles.
- [ ] **Task 5.3: End-to-End Submission & History Verification**
  - Complete a live quiz via link over USB reverse tunnel, verify telemetry ingestion in `quiz_history.json` and `sessions/YYYY-MM-DD.md`, and verify history badge on catalog.
