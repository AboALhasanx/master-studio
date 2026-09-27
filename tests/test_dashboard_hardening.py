"""
Hardening gates for the four critical defects found on 2026-09-27
(docs/QA_DEFECTS_2026-09-27.md -> D-01, D-02/D-03, D-04, D-05).

TDD contract: every test in this file FAILS against the unpatched dashboard and
passes once the fix lands.

    D-01  hostile path component  -> must be 404, never 500
    D-02  malformed bookmarks     -> rejected, file untouched
    D-03  out-of-range telemetry  -> rejected, history untouched
    D-04  write endpoints         -> rate limited (429 after burst)
    D-05  security headers        -> present, version banner gone
"""
import json
import re
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

BASE_DIR = Path(__file__).resolve().parent.parent
dashboard_path = BASE_DIR / "91_Dashboard"
if str(dashboard_path) not in sys.path:
    sys.path.insert(0, str(dashboard_path))

import app as dashboard_app
from app import app

TEMPLATES = dashboard_path / "templates"
STATIC = dashboard_path / "static"


@app.route("/__boom")
def _boom():
    """Deliberately crashing endpoint used by the generic-500 gate below."""
    raise RuntimeError("kaboom")

# Every one of these must NOT be a server error. %00 used to raise
# `ValueError: stat: embedded null character in path` -> 500 (D-01).
HOSTILE_IDS = [
    "Quiz_01%00evil",
    "..%2F..%2F..%2Fetc",
    "CON",
    "a" * 300,
    "Quiz_01<>|",
    "%2e%2e%2f%2e%2e%2f00_STUDIO_HUB",
]

VALID_SUBMISSION = {
    "submission_uuid": "harden-ok-0001",
    "subject_id": "01_Cyber_Security",
    "quiz_id": "Quiz_01_Cybersecurity_Foundations",
    "topic": "Week 01",
    "summary": {"total": 10, "correct": 7, "wrong": 3, "percentage": 70.0},
    "questions": [{"id": "q1", "concept_id": "cia", "is_correct": True,
                   "is_lucky_guess": False, "dwell_time_seconds": 4.0}],
}


@pytest.fixture
def client():
    app.config["TESTING"] = True
    limiter = getattr(dashboard_app, "limiter", None)
    if limiter is not None:
        limiter.reset()
    with app.test_client() as test_client:
        yield test_client
    if limiter is not None:
        limiter.reset()


@pytest.fixture
def isolated_hub(monkeypatch):
    """Point the app's HUB at a scratch directory so ingestion is side-effect free."""
    with TemporaryDirectory() as tmpdir:
        tmp_hub = Path(tmpdir)
        (tmp_hub / "sessions").mkdir(parents=True, exist_ok=True)
        monkeypatch.setattr(dashboard_app, "HUB", tmp_hub)
        yield tmp_hub


# ----------------------------------------------------------------- D-01
@pytest.mark.parametrize("bad_id", HOSTILE_IDS)
def test_hostile_quiz_id_never_500(client, bad_id):
    for path in (f"/api/quiz/01_Cyber_Security/{bad_id}",
                 f"/api/quiz/{bad_id}/Quiz_01"):
        res = client.get(path)
        assert res.status_code != 500, f"{path} -> 500 (unhandled filesystem error)"
        assert res.status_code in (200, 400, 404), f"{path} -> {res.status_code}"
        body = res.get_data(as_text=True)
        assert "Traceback" not in body and "embedded null" not in body


def test_generic_500_is_never_a_traceback(client):
    """A crashing endpoint must answer a clean JSON 500 (OWASP Error Handling)."""
    # TESTING mode re-raises by default; production must answer, not explode.
    previous = app.config.get("PROPAGATE_EXCEPTIONS")
    app.config["PROPAGATE_EXCEPTIONS"] = False
    try:
        res = client.get("/__boom")
        assert res.status_code == 500
        body = res.get_data(as_text=True)
        assert "kaboom" not in body and "Traceback" not in body
        assert res.is_json
        assert res.get_json()["message"] == "Internal error"
    finally:
        app.config["PROPAGATE_EXCEPTIONS"] = previous


# ----------------------------------------------------------------- D-02
def test_bookmarks_rejects_malformed_entries(client, monkeypatch):
    """Arbitrary nested junk must NOT replace the real bookmarks file (D-02)."""
    with TemporaryDirectory() as tmpdir:
        tmp_hub = Path(tmpdir)
        monkeypatch.setattr(dashboard_app, "HUB", tmp_hub)
        bookmarks_file = tmp_hub / "quiz_bookmarks.json"
        original = [{"k": "04_Advanced_Software_Eng/Quiz_01#0", "n": 0,
                     "question_data": {"answer": "B"}}]
        bookmarks_file.write_text(json.dumps(original), encoding="utf-8")

        junk = {"bookmarks": [{"deep": {"x": list(range(50))}}]}
        res = client.post("/api/quiz/bookmarks", json=junk)
        assert res.status_code == 400, "unvalidated payload accepted (200)"

        stored = json.loads(bookmarks_file.read_text(encoding="utf-8"))
        assert stored == original, "bookmarks file was overwritten by junk"


def test_bookmarks_rejects_dict_instead_of_list(client, monkeypatch):
    with TemporaryDirectory() as tmpdir:
        monkeypatch.setattr(dashboard_app, "HUB", Path(tmpdir))
        res = client.post("/api/quiz/bookmarks", json={"evil": True})
        assert res.status_code == 400


def test_bookmarks_accepts_real_schema(client, monkeypatch):
    """The legitimate payload from quiz.js must still be accepted."""
    with TemporaryDirectory() as tmpdir:
        tmp_hub = Path(tmpdir)
        monkeypatch.setattr(dashboard_app, "HUB", tmp_hub)
        real = [{"k": "01_Cyber_Security/Quiz_01_Cybersecurity_Foundations#3",
                 "n": 3, "question_data": {"answer": "B", "options": ["a", "b", "c", "d"]}}]
        res = client.post("/api/quiz/bookmarks", json={"bookmarks": real})
        assert res.status_code == 200, res.get_data(as_text=True)
        stored = json.loads((tmp_hub / "quiz_bookmarks.json").read_text(encoding="utf-8"))
        assert stored == real


# ----------------------------------------------------------------- D-03
def test_submit_rejects_out_of_range_summary(client, isolated_hub):
    history = isolated_hub / "quiz_history.json"
    before = history.read_text(encoding="utf-8") if history.exists() else None

    bad_summaries = [
        {"percentage": -50.0, "correct": -3, "total": -10},
        {"percentage": 1e308, "correct": 10 ** 9, "total": 1},
        {"percentage": 150.0, "correct": 40, "total": 10},   # correct > total
        {"percentage": float("nan"), "correct": 0, "total": 0},
    ]
    for i, summary in enumerate(bad_summaries):
        payload = dict(VALID_SUBMISSION)
        payload["submission_uuid"] = f"harden-range-{i:04d}"
        payload["summary"] = summary
        res = client.post("/api/quiz/submit", json=payload)
        assert res.status_code == 400, f"accepted out-of-range summary {summary}"

    after = history.read_text(encoding="utf-8") if history.exists() else None
    assert after == before, "out-of-range telemetry was persisted"


def test_submit_rejects_out_of_range_top_level(client, isolated_hub):
    """Legacy/abuse payloads that put the numbers at the top level (D-03)."""
    for i, payload in enumerate([
        {"submission_uuid": "harden-top-0001", "percentage": -50, "score": -3, "total": -10},
        {"submission_uuid": "harden-top-0002", "percentage": 1e308, "score": 10 ** 20, "total": 1},
        {"submission_uuid": "harden-top-0003", "percentage": "99", "score": "1", "total": 0},
    ]):
        payload["submission_uuid"] = f"harden-top-{i:04d}"
        res = client.post("/api/quiz/submit", json=payload)
        assert res.status_code == 400, f"accepted {payload}"


def test_submit_accepts_valid_payload(client, isolated_hub):
    res = client.post("/api/quiz/submit", json=VALID_SUBMISSION)
    assert res.status_code == 200, res.get_data(as_text=True)
    assert res.get_json()["status"] in ("success", "already_ingested")


def test_submit_rejects_oversized_body(client):
    """OWASP API4: enforce a maximum payload size (-> 413, not 200)."""
    big = {"submission_uuid": "harden-big-0001", "pad": "x" * (2 * 1024 * 1024)}
    res = client.post("/api/quiz/submit", data=json.dumps(big),
                      content_type="application/json")
    assert res.status_code == 413, f"oversized body accepted -> {res.status_code}"


# ----------------------------------------------------------------- D-04
def test_rate_limit_on_bookmark_writes(client, monkeypatch):
    """OWASP API4: a client must not be able to hammer a write endpoint (D-04)."""
    with TemporaryDirectory() as tmpdir:
        monkeypatch.setattr(dashboard_app, "HUB", Path(tmpdir))
        statuses = []
        for i in range(70):
            res = client.post("/api/quiz/bookmarks",
                              json={"bookmarks": f"burst-{i}"})  # invalid shape on purpose
            statuses.append(res.status_code)
            if res.status_code == 429:
                break
        assert 429 in statuses, (
            f"no rate limiting on /api/quiz/bookmarks (statuses seen: {sorted(set(statuses))})"
        )


def test_rate_limit_exists_on_submit_and_import(client):
    limiter = getattr(dashboard_app, "limiter", None)
    assert limiter is not None, "Flask-Limiter is not wired into the app"
    registered = app.extensions.get("limiter", set())
    assert any(item is limiter for item in registered), (
        f"limiter not registered on the Flask app (extensions: {app.extensions})"
    )
    routes = {str(r) for r in app.url_map.iter_rules()}
    assert "/api/quiz/submit" in routes and "/api/quiz/import" in routes
    assert app.view_functions.get("api_quiz_submit") is not None
    assert app.view_functions.get("api_quiz_import") is not None


# ----------------------------------------------------------------- D-05
def test_security_headers_present(client):
    res = client.get("/")
    assert res.status_code == 200
    h = res.headers

    assert h.get("X-Content-Type-Options") == "nosniff", "missing nosniff"
    assert h.get("Referrer-Policy"), "missing Referrer-Policy"
    csp = h.get("Content-Security-Policy", "")
    assert "frame-ancestors 'none'" in csp, f"missing frame-ancestors: {csp!r}"
    assert "script-src 'self'" in csp, f"missing script-src 'self': {csp!r}"
    assert "default-src 'self'" in csp
    assert h.get("X-Frame-Options") in ("DENY", "SAMEORIGIN")

    server = h.get("Server", "")
    assert "Werkzeug" not in server and "Python" not in server, (
        f"version banner still exposed: {server!r}"
    )


def test_security_headers_present_on_json_endpoints(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.headers.get("X-Content-Type-Options") == "nosniff"
    assert res.headers.get("Referrer-Policy")


def test_templates_have_no_inline_executable_scripts():
    """`script-src 'self'` is only enforceable if no page ships an inline <script>."""
    offenders = []
    for tpl in TEMPLATES.glob("*.html"):
        if "conflict" in tpl.name:
            continue
        text = tpl.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"<script\b([^>]*)>", text):
            attrs = m.group(1)
            if "src=" in attrs:
                continue
            if 'type="application/json"' in attrs or "type='application/json'" in attrs:
                continue  # data block, never executed
            offenders.append(f"{tpl.name}: {m.group(0)[:80]}")
    assert not offenders, "inline executable scripts violate CSP script-src 'self': " + "; ".join(offenders)


def test_pwa_boot_script_is_served_from_static():
    assert (STATIC / "pwa-boot.js").is_file(), (
        "the PWA bootstrap must live in /static/pwa-boot.js, not inline in the template"
    )


# ------------------------------------------------------------------ D-05 (wire)
def test_rate_limited_answer_is_json_with_backoff_headers(client, monkeypatch):
    """A 429 must be a machine-readable answer with Retry-After, not an HTML page."""
    with TemporaryDirectory() as tmpdir:
        monkeypatch.setattr(dashboard_app, "HUB", Path(tmpdir))
        limited = None
        for i in range(70):
            res = client.post("/api/quiz/bookmarks", json={"bookmarks": f"burst-{i}"})
            if res.status_code == 429:
                limited = res
                break
        assert limited is not None, "no 429 within 70 requests"

        assert limited.is_json, f"429 answered with {limited.content_type}, expected JSON"
        body = limited.get_json()
        assert body.get("status") == "error"
        assert "rate" in body.get("message", "").lower()

        retry = limited.headers.get("Retry-After")
        assert retry is not None, "429 carries no Retry-After header"
        assert 0 < int(retry) <= 60, f"Retry-After={retry} not a sane delta-seconds"


def test_limited_route_exposes_ratelimit_headers(client):
    res = client.get("/api/quiz/bookmarks")
    assert res.headers.get("X-RateLimit-Limit"), "missing X-RateLimit-Limit"
    assert res.headers.get("X-RateLimit-Remaining") is not None, "missing X-RateLimit-Remaining"
    assert res.headers.get("Retry-After"), "missing Retry-After on a limited route"


def test_live_server_strips_version_banner():
    """The `Server:` banner is injected by the HTTP layer, not the response
    object, so test_client() cannot see it. Serve on a real socket and check
    the actual bytes on the wire."""
    import threading
    import urllib.request

    from werkzeug.serving import make_server

    server = make_server("127.0.0.1", 0, app,
                         request_handler=dashboard_app.FingerprintlessRequestHandler)
    port = server.socket.getsockname()[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=10) as res:
            banner = res.headers.get("Server", "")
            assert "Werkzeug" not in banner and "Python" not in banner, (
                f"version banner still on the wire: {banner!r}"
            )
            assert res.headers.get("X-Content-Type-Options") == "nosniff"
            assert res.headers.get("X-Frame-Options") == "DENY"
            assert "frame-ancestors 'none'" in res.headers.get("Content-Security-Policy", "")
    finally:
        server.shutdown()
        thread.join(timeout=5)
