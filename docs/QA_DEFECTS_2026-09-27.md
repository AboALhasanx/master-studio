# QA Defect Log — Tablet E2E + Backend Abuse Testing

- **Date:** 2026-09-27
- **Tester:** Master Studio Co-Pilot (OpenCode)
- **Device:** Huawei JMS-W09 · Android 15 · `AJ5EJK5913W00158` (Chrome 153)
- **Server:** Flask dev server `0.0.0.0:5000` (`91_Dashboard/app.py`), access path `adb reverse tcp:5000 tcp:5000`
- **Method:** real-device E2E driven by `hs` gestures + Chrome DevTools Protocol monitoring, then a hostile-input battery against the live API.
- **Raw evidence:** `C:\Windows\Temp\opencode\abuse_results.json`, server log (traceback), `00_STUDIO_HUB/quiz_history.json`

> Data written by the test run (bogus attempts, junk bookmarks) was **restored to its pre-test state**;
> learner telemetry from the automated 30-question run was removed from `quiz_history.json` and the session journal.

---

## Severity scale

| Level | Meaning |
|:--|:--|
| **S1** | Data loss / corruption, or server crash |
| **S2** | Trust-boundary gap (any LAN client can act) |
| **S3** | Broken documented behaviour / misleading automation |
| **S4** | Noise, hygiene, cosmetic |

---

## Findings

### D-01 · S1 · Unhandled `500` on null byte in quiz filename → ✅ **FIXED**
`GET /api/quiz/<subject_id>/<quiz_id>` builds a `Path` from client input and calls `is_file()`/`read_text()` without guarding OS-level path errors.

- **Repro:** `curl -s -o /dev/null -w '%{http_code}' "http://127.0.0.1:5000/api/quiz/01_Cyber_Security/Quiz_01%00evil"` → **500**
- **Evidence (server log):** `ERROR in app: Exception on /api/quiz/... [GET]` → `ValueError: stat: embedded null character in path`
- **Also affected:** any other `OSError` from `Path` (illegal characters, path too long) currently escapes as a 500 instead of the intended `{"error": "Quiz not found"}` 404.
- **Why it matters:** the endpoint already has traversal guards (`.resolve()` + `relative_to()`), but error *handling* around filesystem metadata calls is missing — one malformed URL poisons the log with a full traceback and returns a generic 500.

### D-02 · S1 · `/api/quiz/bookmarks` overwrites real data with unvalidated payloads → ✅ **FIXED**
The POST branch accepts any JSON list, serialises it and atomically replaces `00_STUDIO_HUB/quiz_bookmarks.json` — **no schema check, no size cap, no auth**.

- **Repro:** `POST /api/quiz/bookmarks` body `{"bookmarks":[{"deep":{"x":[0..49]}}]}` → `200 {"status":"success"}`
- **Observed damage:** the file went from **6 real bookmarks → 1 junk object** (restored from backup afterwards).
- **Why it matters:** atomic write prevents *torn* files but not *wrong* files. One buggy or hostile client permanently destroys bookmark state.

### D-03 · S1 · `/api/quiz/submit` persists out-of-range telemetry → ✅ **FIXED**
`percentage`, `score`, `total` are not range- or type-validated before ingestion.

- **Repro:**
  - `{"percentage":-50,"score":-3,"total":-10,...}` → **200** and an attempt row is written (percentage silently clamped to `0.0`, but the row still lands).
  - `{"percentage":1e308,"score":1e20,"total":1,...}` → **200** and an attempt row is written.
- **Impact:** corrupts `quiz_history.json`, the daily session journal, catalog aggregates (`best_percentage`), and the BKT mastery model in `LEARNER_MODEL.md`.
- **Note:** idempotency **is** correct — a replayed `submission_uuid` returns `{"status":"already_ingested"}` (verified).

### D-04 · S2 · No rate limiting, no authentication on any write endpoint → ✅ **FIXED** (rate limiting)
- **Repro:** 30 × `POST /api/quiz/submit` completed in **0.36 s**, all processed.
- **Exposed writers:** `/api/quiz/submit` (history+journal), `/api/quiz/bookmarks` (file overwrite), `/api/quiz/import` (writes `.json` into the subject vault).
- **Context:** the tablet joins the same Wi-Fi as the PC; any device on the LAN (or any page the browser visits, via CSRF-style POSTs) can drive these endpoints. Traversal is rejected (`is_safe_vault_name`), so this is **not** path escape — it is *unauthenticated resource consumption and content injection*.

### D-05 · S2 · No security headers; version disclosure → ✅ **FIXED**
On `GET /` (and API responses):

| Header | Status |
|:--|:--|
| `Content-Security-Policy` | MISSING |
| `X-Content-Type-Options` | MISSING |
| `X-Frame-Options` | MISSING |
| `Referrer-Policy` | MISSING |
| `Server` | present → `Werkzeug/3.1.8 Python/3.12.0` |

- **Impact:** stack fingerprinting; no clickjacking or MIME-sniffing defence; no CSP mitigation layer for the HTML pages that embed JSON.

### D-06 · S3 · Client calls an endpoint the server does not implement
`GET /api/internal/shared-quizzes` → **404** (observed on first page load).

- The route only exists inside the service worker (`sw.js` intercepts it and drains the share-target cache). While the SW is **not yet controlling** the page, the request falls through to Flask and 404s.
- Client code tolerates it (`if (swRes.ok)`), so it is *noise*, but it is a client/server contract mismatch that shows up in every cold-start log.
- Related: `sw.js` pre-cache is resilient (`cache.add` wrapped in `try/catch`), so the install itself does **not** fail.

### D-07 · S3 · Documented `/cards/...` flashcard route never existed → **RESOLVED**
`GET /cards/01_Cyber_Security/Quiz_01_...` returned the Flask `404 Not Found` page on the tablet.

- `91_Dashboard/app.py` has no `/cards` route and no `cards.html` template; grep of all templates found no link to it either.
- **Action taken (2026-09-27):** per the student's instruction, the flashcard web system was purged from documentation (`AGENTS.md`, `skills/examiner/SKILL.md`, `91_Dashboard/static/{sw,qr-scanner}.js` comments, `docs/superpowers/specs/2026-09-25-quiz-system-overhaul-design.md`, `opencode-archive/AGENTS.md`). Active recall remains the Anki/TSV export block in study notes.

### D-08 · S3 · `hs tap "Label"` silently no-ops inside Chrome/WebView
The strongest device-side finding of this session.

- **Repro:** on the quiz start screen, `hs tap "ابدأ الكوز الآن"` → `tapped ... via click → ok`, but a CDP-installed listener recorded **`ev: []`** — zero `pointerdown/touchstart/click` reached the page, and `#btn-start-quiz` stayed visible.
- **Control experiments:**
  - `adb shell input tap 399 809` → page transitions to question 1 ✅
  - `hs tap 399 809` (coordinates) → page transitions ✅
  - CDP `element.click()` → page transitions ✅
- **Conclusion:** Chrome's accessibility `ACTION_CLICK` on web content does not synthesise an input event, while coordinate gestures do. The command still reports success → an agent can loop forever "clicking" nothing.
- **Mitigation:** after *any* label-based tap in a WebView, assert observable state (or use coordinate taps). Recorded in the machine-global protocol.

### D-09 · S4 · Intermittent LAN reachability tablet ↔ PC
- **First attempt:** `ERR_ADDRESS_UNREACHABLE`, tablet→PC ping `100% loss` / `Destination Host Unreachable`, `nc ... 5000` → *No route to host*.
- **Re-test minutes later:** tablet→PC `4/4` received, PC→tablet `4/4`, and `GET http://192.168.100.3:5000/api/health` from the tablet returned `client_ip: 192.168.100.179` ✅.
- **Conclusion:** the Wi-Fi path is *flaky* (ARP/power-save warm-up), not permanently isolated. The QR/LAN flow documented in `AGENTS.md` can therefore fail at the exact moment the student scans it.
- **Reliable path:** `adb reverse tcp:5000 tcp:5000` → `http://127.0.0.1:5000` (verified working throughout this session).

### D-10 · S4 · Production use of the Flask development server
Startup banner: *"This is a development server. Do not use it in a production deployment."* — single-process, `threaded=True`, no worker manager, version banner enabled (D-05).

### D-11 · S4 · Over-permissive fuzzy quiz resolution
`/api/quiz/<subject>/<quiz>` falls back to `clean_lower in stem_lower` and `subject_id.lower() in sdir.name.lower()`. Short ids (`Quiz_01`) or partial subject names silently resolve to the *first* matching file instead of returning 404 — convenient, but it masks client typos and can serve a different quiz than requested.

---

## Verified-good (no defect)

| Behaviour | Evidence |
|:--|:--|
| Full quiz E2E on the device | 30/30 answered, results screen, "Telemetry Synced" toast |
| Telemetry round-trip | `POST /api/quiz/submit` → **200**; row appended to `quiz_history.json`; journal entry written |
| Idempotent submission | duplicate `submission_uuid` → `already_ingested` |
| Path traversal on import | `../../evil`, `..\\..\\pwned`, `../.._pwned` → all **400** with explicit reason |
| Traversal on quiz GET | encoded `..%2F` → **404**, resolved-path containment holds |
| Payload shape validation | arrays / strings / wrong content-type / empty body → **400** |
| Deep JSON nesting (60 levels) | rejected cleanly, no crash |
| No absolute path leak | `/api/data` contains no `C:\Users\...` |
| No JS errors during the whole run | CDP `pageerror`/`console.error` → `[]` |
| Exam mode + shuffle load | `?mode=exam&shuffle=true` renders the start screen correctly |

---

## Remediation applied — 2026-09-27 (TDD: failing test → fix → full suite green)

Scope chosen by the student: the **four critical defects (D-01 … D-05)**. Each fix was written
as a failing test first (`tests/test_dashboard_hardening.py`, 23 gates), then implemented.

| Defect | Fix | Standards anchor |
|:--|:--|:--|
| **D-01** | `api_quiz_get` now resolves client input inside a boundary that catches `(OSError, ValueError, UnicodeError)` → `404` JSON; corrupt-on-disk JSON → `500` with a **generic** body; global `@app.errorhandler(500)` returns JSON with no exception text (detail goes to the log only). | OWASP Error Handling Cheat Sheet |
| **D-02** | `validate_bookmarks()` allow-list gate on `POST /api/quiz/bookmarks`: list only, ≤ 5000 entries, entries must be a `1–400` char key **or** a `{k, n, question_data, subject, quiz}` object with typed fields → otherwise `400`, file untouched. | OWASP Input Validation Cheat Sheet |
| **D-03** | `validate_telemetry()` on `POST /api/quiz/submit`: finite-number check (rejects `NaN`/`inf`/booleans), `percentage ∈ [0,100]`, `correct ≤ total`, counts `∈ [0,500]`, dwell/duration `∈ [0, 86400]`, ≤ 500 questions, control-character and length limits on string fields; `MAX_CONTENT_LENGTH = 1 MiB` → `413`. Rejects instead of clamping (a clamped row still poisons the BKT model). | OWASP API4:2023, Input Validation Cheat Sheet |
| **D-04** | `flask-limiter 4.1.1`, in-memory (keeps the 0-database invariant): `submit 60/min`, `bookmarks 60/min`, `import 30/min`, default `1000/min` for reads. `RATELIMIT_HEADERS_ENABLED` → `X-RateLimit-Limit/Remaining/Reset` + `Retry-After`, and a custom `429` handler answers **JSON** instead of an HTML error page. | OWASP API4:2023, NIST SP 800-204 |
| **D-05** | `after_request` hook adds `Content-Security-Policy` (HTML only, `script-src 'self'`), `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY` + `frame-ancestors 'none'`, `Referrer-Policy`, `Permissions-Policy`. Version banner removed by `FingerprintlessRequestHandler.version_string()` → wire header is `Server: MasterStudio`. The inline PWA bootstrap in `quiz.html` was externalised to `/static/pwa-boot.js` to make `script-src 'self'` enforceable. | OWASP HTTP Headers Cheat Sheet, Secure Headers Project |

### Post-fix evidence

**Automated:** `python -m pytest tests/ -q` → **162 passed** (139 baseline + 23 new hardening gates).
`bandit -r 91_Dashboard/app.py` → 0 high; the single medium (`B104` `host="0.0.0.0"`) and the 7 low
(`B110/B112` try/except pass) are pre-existing and intentional (LAN server, fuzzy-match skipping).

**Live abuse battery (re-run after the fixes):**

| Attack | Before | After |
|:--|:--|:--|
| `GET .../Quiz_01%00evil` | **500** + traceback in log | **404** `{"error":"Quiz not found"}` + WARNING log line |
| `{"percentage":-50,"score":-3,"total":-10}` | **200** + poisoned row | **400** `percentage must be between 0 and 100; total must be between 0 and 500; …` |
| `{"percentage":1e308,…}` / `NaN` / `"99"` | **200** | **400** |
| junk bookmark object `{"deep":{…}}` | **200**, file overwritten | **400**, file untouched |
| 2 MiB body | accepted | **413** |
| 70 rapid writes | all processed | **429** after the 60th, JSON body, `Retry-After: 59` |
| `Server:` header | `Werkzeug/3.1.8 Python/3.12.0` | `MasterStudio` |
| CSP / nosniff / DENY / Referrer-Policy | missing | present on every response |
| **Any 5xx in the whole battery** | 1 (D-01) | **0** |
| Valid, real-shaped submission | 200 | **200** (no false positives — real clients still work) |

**Tablet E2E re-verification (AJ5EJK5913W00158, `adb reverse`):** quiz page `readyState: complete`,
`inlineScriptCount: 0`, scripts run = `lucide.min.js`, `quiz-vault.js`, `quiz.js`, **`pwa-boot.js`**,
service worker *controlled* (registration still works after externalising the script),
`#btn-start-quiz` → question 1/30 with running timer and progress bar →
**0 CSP violations · 0 JS exceptions · 0 console errors/warnings**.

**Hygiene:** `wire_verify.py` snapshots and restores `quiz_history.json`, `quiz_bookmarks.json`
and the session journal byte-for-byte, so this verification added no learner telemetry.

---

## Recommended fixes (research-backed — see `docs/QA_FIX_RESEARCH_2026-09-27.md`)

1. ✅ **Applied** — Wrap filesystem metadata calls in try/except → 404 JSON (**D-01**).
2. ✅ **Applied** — schema validation + size caps on `bookmarks`, `submit` (**D-02, D-03**).
3. ✅ **Applied** — `Flask-Limiter` on all write routes, JSON `429` + backoff headers (**D-04**).
4. ✅ **Applied** — security-header hook + `script-src 'self'` CSP + strip `Server` (**D-05**).
5. Add the internal route server-side or drop the fetch (**D-06**).
6. State assertion after every label-based tap in WebView contexts (**D-08**) — *recorded in the machine-global protocol*.
