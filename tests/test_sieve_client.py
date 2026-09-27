"""
Tests for the Sieve scrape client.

HTTP is mocked only at the boundary (urllib.request.urlopen); every behavior
under test — request building, retry policy, status handling, the follow-up
turn check, persistence, and error mapping — is the real client code.
"""

import io
import json
import sys
import urllib.error
from pathlib import Path

import pytest

# Ensure 90_Shared_Toolbox/tools is in sys.path (same pattern as test_quiz_qr)
toolbox_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox" / "tools"
if str(toolbox_path) not in sys.path:
    sys.path.insert(0, str(toolbox_path))

import sieve_client as sc


# --------------------------------------------------------------------------- #
# HTTP-boundary fakes
# --------------------------------------------------------------------------- #
class FakeResponse:
    def __init__(self, payload, headers=None):
        self._body = json.dumps(payload).encode("utf-8")
        self.headers = headers or {}

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def http_error(code, payload, headers=None):
    return urllib.error.HTTPError(
        "https://scrape.usesieve.com/x", code, "error", headers or {},
        io.BytesIO(json.dumps(payload).encode("utf-8")),
    )


def urlopen_script(sequence):
    """Return (fake_urlopen, calls). Each item is an Exception to raise or a
    payload/tuple to return, consumed in order."""
    calls = []

    def fake(req, timeout=None):
        calls.append(req)
        if not sequence:
            raise AssertionError("unexpected extra HTTP call")
        item = sequence.pop(0)
        if isinstance(item, Exception):
            raise item
        if isinstance(item, tuple):
            return FakeResponse(*item)
        return FakeResponse(item)

    return fake, calls


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #
@pytest.fixture
def api_key(monkeypatch):
    monkeypatch.setenv("SIEVE_API_KEY", "dc_sk_test_key")


@pytest.fixture
def runs_file(monkeypatch, tmp_path):
    path = tmp_path / "sieve_runs.json"
    monkeypatch.setattr(sc, "RUNS_FILE", path)
    return path


@pytest.fixture
def sleeps(monkeypatch):
    recorded = []
    monkeypatch.setattr(sc.time, "sleep", lambda s: recorded.append(s))
    return recorded


def _install(monkeypatch, sequence):
    fake, calls = urlopen_script(sequence)
    monkeypatch.setattr(sc.urllib.request, "urlopen", fake)
    return calls


def _headers(req):
    return {k.lower(): v for k, v in req.header_items()}


# --------------------------------------------------------------------------- #
# Request building
# --------------------------------------------------------------------------- #
def test_start_run_builds_correct_request(monkeypatch, api_key, runs_file):
    calls = _install(monkeypatch, [
        {"status": "queued", "session_id": "s1", "poll": "/api/scrapes/s1"},
    ])
    sid = sc.start_run("Extract the text and author of each quote",
                       target_urls=["https://quotes.toscrape.com"])

    assert sid == "s1"
    req = calls[0]
    assert req.full_url == "https://scrape.usesieve.com/api/scrapes"
    assert req.get_method() == "POST"
    assert _headers(req)["authorization"] == "Bearer dc_sk_test_key"
    body = json.loads(req.data.decode("utf-8"))
    assert body["instruction"] == "Extract the text and author of each quote"
    assert body["target_urls"] == ["https://quotes.toscrape.com"]
    assert body["compliance_mode"] == "regular"   # default per contract


def test_start_run_optional_fields_and_compliance_override(monkeypatch, api_key,
                                                           runs_file):
    calls = _install(monkeypatch, [{"status": "queued", "session_id": "s2"}])
    sc.start_run("pull rows", fields=["quote", "author"],
                 output_schema={"type": "object"}, table_shape="wide",
                 compliance_mode="conservative")
    body = json.loads(calls[0].data.decode("utf-8"))
    assert body["fields"] == ["quote", "author"]
    assert body["output_schema"] == {"type": "object"}
    assert body["table_shape"] == "wide"
    assert body["compliance_mode"] == "conservative"


def test_session_id_persisted_durably_before_return(monkeypatch, api_key,
                                                    runs_file):
    _install(monkeypatch, [{"status": "queued", "session_id": "s9"}])
    sc.start_run("anything")
    assert runs_file.is_file()
    data = json.loads(runs_file.read_text(encoding="utf-8"))
    assert "s9" in data["runs"]
    assert data["runs"]["s9"]["instruction"] == "anything"
    assert data["runs"]["s9"]["status"] == "queued"


# --------------------------------------------------------------------------- #
# Never retry POST on timeout / network error
# --------------------------------------------------------------------------- #
def test_start_run_never_retries_network_error(monkeypatch, api_key, runs_file):
    calls = _install(monkeypatch, [urllib.error.URLError("connection reset")])
    with pytest.raises(sc.SieveUnavailable):
        sc.start_run("might have been accepted")
    assert len(calls) == 1, "POST /api/scrapes must never be auto-retried after a network error"
    assert not runs_file.exists(), "no run may be persisted when the outcome is unknown"


def test_start_run_never_retries_timeout(monkeypatch, api_key, runs_file):
    calls = _install(monkeypatch, [TimeoutError("timed out")])
    with pytest.raises(sc.SieveUnavailable):
        sc.start_run("might have been accepted")
    assert len(calls) == 1


def test_start_run_retries_429_then_succeeds(monkeypatch, api_key, runs_file, sleeps):
    calls = _install(monkeypatch, [
        http_error(429, {"error": "rate limited"}, {"Retry-After": "7"}),
        {"status": "queued", "session_id": "s3"},
    ])
    sid = sc.start_run("retry me")
    assert sid == "s3"
    assert len(calls) == 2
    assert sleeps == [7], "429 must honor Retry-After (safe: no run was created)"


def test_start_run_retries_5xx_then_succeeds(monkeypatch, api_key, runs_file, sleeps):
    calls = _install(monkeypatch, [
        http_error(503, {"error": "unavailable"}),
        {"status": "queued", "session_id": "s4"},
    ])
    assert sc.start_run("retry me") == "s4"
    assert len(calls) == 2


# --------------------------------------------------------------------------- #
# Error mapping
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize("code,exc_type", [
    (400, sc.SieveRequestError),
    (401, sc.SieveAuthError),
    (402, sc.SieveCreditError),
    (404, sc.SieveNotFound),
])
def test_error_mapping_for_client_and_auth_errors(monkeypatch, api_key, runs_file,
                                                  code, exc_type):
    calls = _install(monkeypatch, [http_error(code, {"error": f"e{code}"})])
    with pytest.raises(exc_type):
        sc.start_run("x")
    assert len(calls) == 1, "4xx must not be retried"


def test_400_message_carried_for_device_flow(monkeypatch):
    calls = _install(monkeypatch, [http_error(400, {"error": "authorization_pending"})])
    result = sc.device_token("dev-123")
    assert result == {"ok": False, "error": "authorization_pending"}
    assert len(calls) == 1


def test_not_configured_is_inert(monkeypatch, runs_file, tmp_path):
    monkeypatch.delenv("SIEVE_API_KEY", raising=False)
    monkeypatch.setattr(sc, "ENV_FILE", tmp_path / "no-such-.env")
    calls = _install(monkeypatch, [])
    with pytest.raises(sc.SieveNotConfigured):
        sc.start_run("x")
    assert calls == [], "no key -> no HTTP traffic, nothing else breaks"


def test_api_key_read_from_env_file(monkeypatch, tmp_path):
    monkeypatch.delenv("SIEVE_API_KEY", raising=False)
    env = tmp_path / ".env"
    env.write_text('OTHER=1\nSIEVE_API_KEY="dc_sk_from_file"\n', encoding="utf-8")
    monkeypatch.setattr(sc, "ENV_FILE", env)
    assert sc.get_api_key() == "dc_sk_from_file"


# --------------------------------------------------------------------------- #
# Poll status handling: running / done / refused / unknown
# --------------------------------------------------------------------------- #
def test_get_run_retries_network_error(monkeypatch, api_key, runs_file, sleeps):
    calls = _install(monkeypatch, [
        urllib.error.URLError("blip"),
        {"status": "running"},
    ])
    assert sc.get_run("s1")["status"] == "running"
    assert len(calls) == 2, "GET polling must retry network errors"


def test_wait_until_done_backoff(monkeypatch, api_key, runs_file, sleeps):
    _install(monkeypatch, [
        {"status": "running"},
        {"status": "running"},
        {"status": "running"},
        {"status": "running"},
        {"status": "running"},
        {"status": "done", "turns": 1, "result": {"ok": True}},
    ])
    run = sc.wait_until_done("s1")
    assert run["status"] == "done"
    assert sleeps == [5, 10, 20, 30, 30], "poll starts at 5s, doubles, and caps at 30s"
    data = json.loads(runs_file.read_text(encoding="utf-8"))
    assert data["runs"]["s1"]["status"] == "done"


def test_wait_until_done_refused_raises_with_code(monkeypatch, api_key, runs_file):
    _install(monkeypatch, [
        {"status": "refused", "refusal": {"code": "quota", "message": "no credits"}},
    ])
    with pytest.raises(sc.SieveRefused) as excinfo:
        sc.wait_until_done("s1")
    assert excinfo.value.refusal["code"] == "quota"
    data = json.loads(runs_file.read_text(encoding="utf-8"))
    assert data["runs"]["s1"]["status"] == "refused"


def test_wait_until_done_unknown_status_is_error(monkeypatch, api_key, runs_file):
    _install(monkeypatch, [{"status": "exploded"}])
    with pytest.raises(sc.SieveUnknownRunStatus):
        sc.wait_until_done("s1")


# --------------------------------------------------------------------------- #
# Follow-up turns
# --------------------------------------------------------------------------- #
def test_follow_up_waits_until_turns_advance(monkeypatch, api_key, runs_file, sleeps):
    calls = _install(monkeypatch, [
        {"status": "done", "turns": 1},                      # record turns before send
        {"status": "accepted", "turns": 1},                  # POST messages
        {"status": "running", "turns": 1},                   # turn in progress
        {"status": "done", "turns": 1},                      # previous answer still!
        {"status": "done", "turns": 2, "result": {"rows": []}},  # new turn ready
    ])
    run = sc.send_follow_up("s1", {"instruction": "also get the tags"})
    assert run["turns"] == 2
    assert len(calls) == 5, "must keep polling until turns advances past the recorded value"
    assert calls[1].get_method() == "POST"
    assert calls[1].full_url.endswith("/api/scrapes/s1/messages")
    body = json.loads(calls[1].data.decode("utf-8"))
    assert body["instruction"] == "also get the tags"


def test_follow_up_resends_after_409(monkeypatch, api_key, runs_file, sleeps):
    calls = _install(monkeypatch, [
        {"status": "done", "turns": 1},                 # record turns
        http_error(409, {"error": "turn in flight"}),   # first send: conflict
        {"status": "accepted", "turns": 1},             # resend succeeds
        {"status": "done", "turns": 2, "result": {}},   # new answer
    ])
    run = sc.send_follow_up("s1", {"instruction": "follow up"})
    assert run["turns"] == 2
    assert len(calls) == 4
    assert sleeps and sleeps[0] == sc.POLL_INITIAL_DELAY, "409 must wait before resending"


# --------------------------------------------------------------------------- #
# Result presentation safety
# --------------------------------------------------------------------------- #
def test_require_clean_result_blocks_fail(monkeypatch):
    run = {"schema_conformance": {"status": "fail", "summary": "missing columns"},
           "result": {"dirty": True}}
    with pytest.raises(sc.SieveError, match="schema conformance failed"):
        sc.require_clean_result(run)


def test_require_clean_result_allows_pass_and_partial(monkeypatch):
    pass_run = {"schema_conformance": {"status": "pass"}, "result": {"a": 1}}
    partial_run = {"schema_conformance": {"status": "partial"}, "result": {"a": 1}}
    assert sc.require_clean_result(pass_run) == {"a": 1}
    assert sc.require_clean_result(partial_run) == {"a": 1}


# --------------------------------------------------------------------------- #
# Task 6: Bearer token isolation in download_files
# --------------------------------------------------------------------------- #
def test_download_files_relative_url_gets_bearer_token(monkeypatch, api_key, tmp_path):
    """A first-party (relative) URL resolves against BASE_URL and IS authenticated."""
    calls = _install(monkeypatch, [{"status": "done"}])
    run = {"files": [{"url": "/files/report.csv", "name": "report.csv"}]}

    sc.download_files(run, tmp_path)

    assert calls[0].full_url == "https://scrape.usesieve.com/files/report.csv"
    assert _headers(calls[0]).get("authorization") == "Bearer dc_sk_test_key"


def test_download_files_third_party_url_never_leaks_bearer_token(monkeypatch, api_key, tmp_path):
    """Credential leak: an absolute third-party URL must be fetched WITHOUT the
    Sieve API key, otherwise the token is disclosed to an attacker-controlled host."""
    calls = _install(monkeypatch, [{"status": "done"}])
    run = {"files": [{"url": "https://evil.example.com/exfil", "name": "x.txt"}]}

    sc.download_files(run, tmp_path)

    headers = _headers(calls[0])
    assert "authorization" not in headers, (
        "Credential leak: Authorization: Bearer was sent to a non-BASE_URL host"
    )


def test_download_files_lookalike_host_does_not_get_token(monkeypatch, api_key, tmp_path):
    """Suffix tricks like https://scrape.usesieve.com.evil.com must not qualify."""
    calls = _install(monkeypatch, [{"status": "done"}])
    run = {"files": [{"url": "https://scrape.usesieve.com.evil.com/f", "name": "y.txt"}]}

    sc.download_files(run, tmp_path)

    assert "authorization" not in _headers(calls[0])
