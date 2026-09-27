# QA Fix Research — Professional / Standards-Based Remediation Plan

- **Date:** 2026-09-27
- **Companion:** `docs/QA_DEFECTS_2026-09-27.md` (the findings this answers)
- **Purpose:** map every caught defect to the *established* way professionals fix it — standards, cheat sheets and libraries — instead of ad-hoc patching.

## Sources used (all fetched and verified HTTP 200 on 2026-09-27)

| # | Source | URL | Verified |
|:--|:--|:--|:--|
| S1 | OWASP API Security Top 10 (2023) — API4:2023 Unrestricted Resource Consumption | https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/ | ✅ |
| S2 | OWASP Cheat Sheet Series — HTTP Headers | https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html | ✅ |
| S3 | OWASP Cheat Sheet Series — Input Validation | https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html | ✅ |
| S4 | OWASP Cheat Sheet Series — Error Handling | https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html | ✅ |
| S5 | OWASP Secure Headers Project | https://owasp.org/www-project-secure-headers/ | ✅ |
| S6 | Flask-Limiter (rate limiting for Flask) | https://flask-limiter.readthedocs.io/en/stable/ | ✅ |
| S7 | Flask-Talisman (security headers for Flask) | https://github.com/wntrblm/flask-talisman | ✅ |
| S8 | Hypothesis (property-based testing for Python) | https://hypothesis.readthedocs.io/en/latest/ | ✅ |
| S9 | Bandit (Python static security analyser) | https://bandit.readthedocs.io/en/latest/ | ✅ |
| S10 | Gunicorn (production WSGI HTTP server) | https://docs.gunicorn.org/ | ✅ |
| S11 | NIST SP 800-204 — Rate Limiting / Throttling in microservices | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204.pdf | ✅ |

> Flask-Talisman's ReadTheDocs host currently returns 404; the canonical reference is the GitHub repository (S7).
> Standards/tooling references are cited by URL; anything reasoned from first principles is tagged `[Foundational Knowledge / Standard Concept]`.

---

## D-01 · Filesystem `ValueError` → 500

**Professional pattern:** OWASP Error Handling Cheat Sheet (S4) — handle unexpected errors at a single boundary, return a generic client-safe response, log the detail server-side only; never let a raw traceback become the HTTP response.

```python
@app.route("/api/quiz/<subject_id>/<quiz_id>")
def api_quiz_get(subject_id, quiz_id):
    ...
    try:
        if target_file.is_file() and target_file.stat().st_size:   # any OSError/ValueError
            ...
    except (OSError, ValueError):
        app.logger.warning("Rejected invalid path component: %r", quiz_id)
        return jsonify({"error": "Quiz not found"}), 404
```

Plus a global handler so *any* future endpoint fails closed:

```python
@app.errorhandler(500)
def _ise(_):
    return jsonify({"status": "error", "message": "Internal error"}), 500
```

Test: `pytest` parametrised over hostile ids (`%00`, `..`, `\`, 4 KB names, illegal Windows chars) — each must yield 404, never 500.

---

## D-02 / D-03 · Unvalidated payloads persisted

**Professional pattern:** OWASP Input Validation (S3) — *allow-list* validation driven by a **schema**, with type, range, length and format constraints enforced **before** any state change. OWASP API4 (S1) additionally requires *"Define and enforce a maximum size of data on all incoming parameters and payloads … maximum length for strings, maximum number of elements in arrays"*.

Concrete design for this codebase:

```python
# 90_Shared_Toolbox/tools/quiz_models.py  (Pydantic v2)
class Telemetry(BaseModel):
    model_config = ConfigDict(extra="ignore")
    submission_uuid: str  # validated as UUID4
    subject_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9 _\-]{0,99}$")
    quiz_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9 _\-]{0,99}$")
    percentage: float = Field(ge=0.0, le=100.0)
    score: int = Field(ge=0)
    total: int = Field(ge=1, le=500)
    questions: list[dict] = Field(max_length=500)

    @model_validator(mode="after")
    def _score_consistency(self):
        if self.score > self.total:
            raise ValueError("score cannot exceed total")
        return self
```

- `app.config["MAX_CONTENT_LENGTH"] = 1_000_000` → Flask rejects oversized bodies with 413 before parsing (API4's "maximum upload file size").
- **Bookmarks:** validate shape (`list` of `{k: str, n: int, question_data: dict}`) and cap entries (e.g. ≤ 2000) before the atomic replace — atomicity alone does not guarantee *correctness*.
- Rejection → HTTP 400 with a precise reason; the existing 200-with-clamped-value behaviour is what corrupts the model, so clamping silently must stop.

---

## D-04 · No rate limiting / no auth on write endpoints

**Professional pattern (S1, verbatim):** *"Implement a limit on how often a client can interact with the API within a defined timeframe (rate limiting)"* and *"Rate limiting should be fine tuned — some API endpoints might require stricter policies."* Cross-referenced by OWASP to **CWE-770, CWE-400, CWE-799** and to **NIST SP 800-204** (S11).

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(key_func=get_remote_address, app=app,
                  default_limits=["60 per minute"],
                  storage_uri="memory://")          # single-process; no DB overhead

@app.post("/api/quiz/submit")
@limiter.limit("10 per minute")      # telemetry: strict
def api_quiz_submit(): ...

@app.post("/api/quiz/import")
@limiter.limit("5 per minute")       # vault writes: strictest
def api_quiz_import(): ...
```

- Endpoint-specific limits are exactly what API4 prescribes; `default_limits` covers everything else.
- **Authentication layer:** the vault-writer routes (`/api/quiz/import`, `/api/quiz/bookmarks`) should require a shared bearer token (env var) — this converts "any LAN device" into "the student's device". `[Foundational Knowledge / Standard Concept]`
- **CSRF:** these are JSON POSTs without cookies, so Same-Origin Policy already blocks classic cross-site form posts; adding a simple `X-Requested-With`/origin check is cheap defence-in-depth (OWASP CSRF Prevention Cheat Sheet).

---

## D-05 · Missing security headers + version disclosure

**Professional pattern (S2, verbatim):**
- `X-Content-Type-Options: nosniff` — "Set the Content-Type header correctly throughout the site."
- `Referrer-Policy: strict-origin-when-cross-origin`.
- `X-Frame-Options: DENY` → *"Use Content Security Policy (CSP) `frame-ancestors` directive if possible."*
- **`Server` header:** *"Remove this header or set non-informative values"* → today it leaks `Werkzeug/3.1.8 Python/3.12.0`.
- CSP per S2 → see the OWASP Content Security Policy Cheat Sheet for the policy itself.
- `Permissions-Policy: geolocation=(), camera=(), microphone=()` (the app needs none of them; the QR scanner needs `camera` **only** on `/quiz`).

```python
@app.after_request
def secure_headers(resp):
    resp.headers.setdefault("X-Content-Type-Options", "nosniff")
    resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    resp.headers.setdefault("X-Frame-Options", "DENY")
    resp.headers.setdefault("Permissions-Policy", "geolocation=(), microphone=()")
    resp.headers.pop("Server", None)          # Werkzeug version banner
    if resp.mimetype == "text/html":
        resp.headers.setdefault(
            "Content-Security-Policy",
            "default-src 'self'; img-src 'self' data:; media-src 'self'; "
            "style-src 'self' 'unsafe-inline'; script-src 'self'; "
            "frame-ancestors 'none'; base-uri 'self'; form-action 'self'")
    return resp
```

- Ready-made alternative: **Flask-Talisman** (S7) does this in one call.
- **Do not enable HSTS** — the app is plain HTTP on a LAN; HSTS would break it (S2 warns explicitly about misconfigured HSTS lockout).
- Audit with **Mozilla Observatory** (named in S2) or the OWASP Secure Headers Project (S5) tooling.
- Known friction: the pages embed JSON via `<script type="application/json">` (safe under `script-src 'self'`) and may use inline styles → keep `style-src 'unsafe-inline'` initially, then remove. Expect a report-only CSP pass first. `[Foundational Knowledge / Standard Concept]`

---

## D-06 · Client calls a route the server does not implement

**Professional pattern:** OWASP API9:2023 *Improper Inventory Management* — every endpoint a client depends on must exist and be versioned/inventoried. Two clean options:

1. **Implement it** (smallest diff, keeps the SW/quiz.js contract):
   ```python
   @app.route("/api/internal/shared-quizzes")
   def internal_shared_quizzes():
       return jsonify([])   # share-target payloads are drained by the SW cache
   ```
2. **Delete the fetch** in `quiz.js` and the SW branch, if the Web Share Target flow is not used.

Leaving a 404 that "someone else handles" is the failure mode API9 describes.

---

## D-08 · `hs tap "Label"` silently no-ops in WebView (device/tooling)

Not a web-security issue but a **verification-discipline** issue: the tool reported success while nothing happened.

**Professional pattern:** assert *observable state* after every action instead of trusting the actor's return code — the same principle that underlies Playwright's auto-waiting and Android UI testing's `UiDevice.wait(...)` assertions. `[Foundational Knowledge / Standard Concept]`

Operational rules (now in the machine-global protocol):
1. In WebView/Chrome contexts, prefer **coordinate taps** (`hs tap X Y`) or `adb shell input tap` — both verified working; label taps verified broken.
2. After *any* tap, assert a postcondition (`hs wait "Label"`, a DOM state via CDP, or a server-log line) before continuing.
3. Treat `ok` from `hs` as *dispatched*, never as *handled*.

---

## D-09 · Flaky LAN reachability (tablet ↔ PC)

**Professional pattern:** health-check before choosing a transport, and keep a redundant path. `[Foundational Knowledge / Standard Concept]`

```
1. GET /api/health with a 1 s timeout → use http://<lan-ip>:5000 (QR/LAN flow)
2. on failure → adb reverse tcp:5000 tcp:5000 → http://127.0.0.1:5000
3. re-check health; surface a clear Arabic error if both fail
```

The QR launcher (`quiz_qr.py`) should print the fallback command alongside the code so a failed scan has an obvious next step.

---

## D-10 · Flask development server in use

**Professional pattern:** run the app behind a production WSGI server (S10, Gunicorn — the standard on Linux) or **Waitress** on Windows `[Foundational Knowledge / Standard Concept]`; the dev server is explicitly documented as unsuitable for production. This also removes the `Server:` banner issue class and gives proper concurrency/backpressure — which is what makes rate limiting (D-04) meaningful.

---

## D-11 · Ambiguous fuzzy quiz resolution

**Professional pattern:** fail fast and predictably — an ambiguous identifier should be 404, not a "best guess" (OWASP Input Validation S3: strict allow-lists over fuzzy matching). Keep the prefix match, but (a) require the match to be **unique**, (b) return 400 `{"error": "ambiguous quiz id"}` when several files match.

---

## Prioritised remediation backlog

| # | Fix | Defects | Effort | Risk reduced | Status |
|:--|:--|:--|:--|:--|:--|
| 1 | Try/except around FS metadata + 500 handler + parametrised hostile-id tests | D-01 | S | Crash / log poisoning | ✅ Applied 2026-09-27 |
| 2 | Schema validation + `MAX_CONTENT_LENGTH` + range checks | D-02, D-03 | M | Data & model corruption | ✅ Applied 2026-09-27 |
| 3 | `Flask-Limiter` per-route limits + JSON `429` + backoff headers | D-04 | S | DoS, unauthenticated writes | ✅ Applied 2026-09-27 |
| 4 | Security headers + strip `Server` (`after_request` hook + `FingerprintlessRequestHandler`) | D-05 | S | Fingerprinting, clickjacking, XSS layer | ✅ Applied 2026-09-27 |
| 5 | Implement or remove `/api/internal/shared-quizzes` | D-06 | XS | Log noise, contract drift | ⬜ Pending |
| 6 | Production WSGI (Waitress/Gunicorn) | D-10 | M | Stability under load | ⬜ Pending |
| 7 | Unique-match rule for quiz ids | D-11 | XS | Wrong-quiz serving | ⬜ Pending |
| 8 | Health-check + `adb reverse` fallback in `quiz_qr.py` | D-09 | S | Broken study sessions | ⬜ Pending |
| 9 | State-assertion rule after every tap | D-08 | XS | Wasted agent loops | ✅ Recorded in the machine-global Android protocol |

**Verification gates for every fix:** `pytest tests/` green, then `bandit -r 91_Dashboard 90_Shared_Toolbox/tools` clean for the touched files, then re-run the abuse battery in `C:\Windows\Temp\opencode\abuse_battery.py` expecting **zero 5xx** and expected 4xx, and finally the device E2E (`e2e_tablet.py`) green.

**Result for items 1–4 (2026-09-27):** all four gates passed — `162 passed` in pytest, bandit
0-high (1 medium = pre-existing intentional `host="0.0.0.0"` LAN binding), abuse battery **0 × 5xx**
with 404/400/413/429 exactly where expected, and a device re-verification through
`adb reverse` that checked CSP conformance specifically (0 violations, `pwa-boot.js` loaded,
service worker controlled, start → Q1/30). The device run deliberately stopped **short of submitting**
so that no synthetic attempt would touch `quiz_history.json` / the BKT model; a full real submission
was already proven green in the pre-fix E2E and the real-shaped payload is covered by the
`VALID telemetry → 200` wire check.

**Implementation notes / deviations from the original plan:**
- Validation is hand-rolled allow-list code in `app.py` (`validate_telemetry`, `validate_bookmarks`)
  rather than a separate Pydantic module: the two endpoints need only ~40 typed assertions, and the
  dashboard must keep importing with zero new module paths. Pydantic 2.13.4 remains available if the
  payload surface grows.
- `Flask-Talisman` was **not** adopted: it hard-codes an `https` upgrade path and a nonce policy that
  fights this plain-HTTP LAN + PWA setup; the explicit `after_request` header hook gives the same
  controls without a redirect trap, and its CSP is asserted by tests on the live socket.
- `flask-limiter` was added to `requirements.txt` (pinned `4.1.1`) and `91_Dashboard/requirements.txt`
  (`flask-limiter>=4.0`) so CI installs it.
