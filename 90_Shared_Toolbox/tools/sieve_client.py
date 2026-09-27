"""
Sieve scrape API client (https://scrape.usesieve.com).

Integration rules:
- Server-side only. The API key is read from SIEVE_API_KEY (process env) or the
  project's gitignored .env file. It is never printed, logged, or sent anywhere
  except the API itself (Authorization: Bearer header) — never to the browser
  bundle, analytics, or error reports.
- No key configured -> every entry point raises SieveNotConfigured and nothing
  else in the project is affected.
- POST /api/scrapes spends credits and has no idempotency key: it is NEVER
  retried after a timeout/network error (the first call may have succeeded).
  429/5xx responses create no run and are safe to retry.
- Every session_id is persisted atomically to 00_STUDIO_HUB/sieve_runs.json
  BEFORE start_run returns, so a crash resumes polling instead of duplicating
  a run.

Conventions reused from this repo: stdlib urllib (no HTTP client dependency),
Path-based project root, HUB JSON records written via tmp-file + os.replace.
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

BASE_URL = "https://scrape.usesieve.com"
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = PROJECT_ROOT / ".env"
RUNS_FILE = PROJECT_ROOT / "00_STUDIO_HUB" / "sieve_runs.json"

DEFAULT_TIMEOUT = 60
DOWNLOAD_TIMEOUT = 120
POLL_INITIAL_DELAY = 5
POLL_MAX_DELAY = 30
MAX_HTTP_RETRIES = 3


# --------------------------------------------------------------------------- #
# Errors
# --------------------------------------------------------------------------- #
class SieveError(Exception):
    """Base class for every Sieve failure."""


class SieveNotConfigured(SieveError):
    """No SIEVE_API_KEY available (env or project .env)."""


class SieveRequestError(SieveError):
    """HTTP 400: the request itself is wrong; fixing it is required, no retry."""


class SieveAuthError(SieveError):
    """HTTP 401: key missing or revoked."""


class SieveCreditError(SieveError):
    """HTTP 402: out of credits."""


class SieveNotFound(SieveError):
    """HTTP 404: not found, or not this account's."""


class SieveConflict(SieveError):
    """HTTP 409: a follow-up turn is already in flight."""


class SieveRateLimit(SieveError):
    """HTTP 429: wait Retry-After before retrying."""

    def __init__(self, message, retry_after=None):
        super().__init__(message)
        self.retry_after = retry_after


class SieveUnavailable(SieveError):
    """HTTP 5xx or a network failure."""


class SieveRefused(SieveError):
    """Terminal refusal: the run never started (refusal.code says why)."""

    def __init__(self, refusal):
        self.refusal = refusal or {}
        super().__init__(f"scrape run refused: {self.refusal.get('code', 'unknown')}")


class SieveUnknownRunStatus(SieveError):
    """A poll returned a status outside running/done/refused."""


# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #
def get_api_key():
    """Return the API key from the environment or the project's .env file.

    Never logs or prints the value.
    """
    key = os.environ.get("SIEVE_API_KEY", "").strip()
    if key:
        return key
    try:
        if ENV_FILE.is_file():
            for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("SIEVE_API_KEY="):
                    value = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if value:
                        return value
    except OSError:
        pass
    return None


# --------------------------------------------------------------------------- #
# HTTP boundary
# --------------------------------------------------------------------------- #
def _map_error(exc, payload):
    message = payload.get("error") or payload.get("message") or f"HTTP {exc.code}"
    if isinstance(message, (dict, list)):
        message = json.dumps(message, ensure_ascii=False)
    message = str(message)
    if exc.code == 400:
        return SieveRequestError(message)
    if exc.code == 401:
        return SieveAuthError(message)
    if exc.code == 402:
        return SieveCreditError(message)
    if exc.code == 404:
        return SieveNotFound(message)
    if exc.code == 409:
        return SieveConflict(message)
    if exc.code == 429:
        retry_after = None
        try:
            retry_after = int((exc.headers or {}).get("Retry-After"))
        except (TypeError, ValueError):
            retry_after = None
        return SieveRateLimit(message, retry_after=retry_after)
    if exc.code >= 500:
        return SieveUnavailable(message)
    return SieveError(message)


def _request(method, path, body=None, *, auth=True, retry_network=True,
             retry_http=True, timeout=DEFAULT_TIMEOUT):
    """One JSON round-trip against the Sieve API.

    retry_network=False is mandatory for non-idempotent POSTs (a timeout may
    mean the call already succeeded server-side).
    """
    headers = {"Accept": "application/json"}
    if auth:
        key = get_api_key()
        if not key:
            raise SieveNotConfigured(
                "SIEVE_API_KEY is not configured (set it in the environment or project .env)"
            )
        headers["Authorization"] = f"Bearer {key}"
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")

    attempt = 0
    while True:
        attempt += 1
        req = urllib.request.Request(BASE_URL + path, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read().decode("utf-8", errors="replace").strip()
                payload = json.loads(raw) if raw else {}
                return payload, getattr(resp, "headers", {})
        except urllib.error.HTTPError as exc:
            try:
                payload = json.loads((exc.read() or b"").decode("utf-8", errors="replace") or "{}")
            except Exception:
                payload = {}
            if retry_http and exc.code == 429 and attempt <= MAX_HTTP_RETRIES:
                delay = None
                try:
                    delay = int((exc.headers or {}).get("Retry-After"))
                except (TypeError, ValueError):
                    delay = None
                time.sleep(delay if delay else min(2 ** attempt, 30))
                continue
            if retry_http and exc.code >= 500 and attempt <= MAX_HTTP_RETRIES:
                time.sleep(min(2 ** attempt, 30))
                continue
            raise _map_error(exc, payload) from None
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            if retry_network and attempt <= MAX_HTTP_RETRIES:
                time.sleep(min(2 ** attempt, 15))
                continue
            reason = getattr(exc, "reason", exc)
            raise SieveUnavailable(f"network error on {method} {path}: {reason}") from None


# --------------------------------------------------------------------------- #
# Durable run ledger (crash-resume: never start a duplicate run)
# --------------------------------------------------------------------------- #
def _load_runs():
    try:
        if RUNS_FILE.is_file():
            data = json.loads(RUNS_FILE.read_text(encoding="utf-8"))
            if isinstance(data, dict) and isinstance(data.get("runs"), dict):
                return data
    except (OSError, ValueError):
        pass
    return {"runs": {}}


def _persist_run(session_id, record):
    data = _load_runs()
    runs = data["runs"]
    merged = dict(runs.get(session_id) or {})
    merged.update(record)
    merged["session_id"] = session_id
    merged["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    runs[session_id] = merged
    try:
        RUNS_FILE.parent.mkdir(parents=True, exist_ok=True)
        tmp = RUNS_FILE.with_name(f"sieve_runs_{uuid.uuid4().hex[:8]}.tmp")
        tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        tmp.replace(RUNS_FILE)
    except OSError as exc:
        raise SieveError(
            f"run {session_id} started but could not be persisted: {exc}"
        ) from exc
    return merged


# --------------------------------------------------------------------------- #
# Runs
# --------------------------------------------------------------------------- #
def start_run(instruction, *, target_urls=None, fields=None, schema=None,
              output_schema=None, table_shape=None, compliance_mode="regular"):
    """Start a scrape run. Returns its session_id (persisted before returning).

    Never retried on timeout/network error; 429/5xx retries are safe (no run
    was created).
    """
    if not instruction or not isinstance(instruction, str):
        raise SieveRequestError("instruction (plain language) is required")
    body = {"instruction": instruction, "compliance_mode": compliance_mode or "regular"}
    if target_urls:
        body["target_urls"] = list(target_urls)
    if fields:
        body["fields"] = fields
    if schema:
        body["schema"] = schema
    if output_schema:
        body["output_schema"] = output_schema
    if table_shape:
        body["table_shape"] = table_shape

    resp, _ = _request("POST", "/api/scrapes", body, retry_network=False)
    session_id = resp.get("session_id")
    if not session_id:
        raise SieveError("scrape start response did not include a session_id")
    _persist_run(session_id, {
        "instruction": instruction,
        "status": resp.get("status", "queued"),
        "turns": 0,
        "poll_path": resp.get("poll") or f"/api/scrapes/{session_id}",
    })
    return session_id


def get_run(session_id):
    """One poll: GET /api/scrapes/<session_id> (network errors retried)."""
    run, _ = _request("GET", f"/api/scrapes/{session_id}")
    if not isinstance(run, dict):
        raise SieveError("unexpected poll payload")
    return run


def wait_until_done(session_id, *, timeout=1800,
                    initial_delay=POLL_INITIAL_DELAY, max_delay=POLL_MAX_DELAY):
    """Poll until status == 'done' (5s -> ~30s backoff). refused -> SieveRefused.

    Any other status is an error. Returns the done run payload.
    """
    delay = initial_delay
    deadline = time.monotonic() + timeout
    while True:
        run = get_run(session_id)
        status = run.get("status")
        turns = run.get("turns", 0)
        if status == "done":
            _persist_run(session_id, {"status": "done", "turns": turns})
            return run
        if status == "refused":
            _persist_run(session_id, {"status": "refused",
                                      "refusal": run.get("refusal") or {}})
            raise SieveRefused(run.get("refusal"))
        if status != "running":
            raise SieveUnknownRunStatus(f"unexpected run status: {status!r}")
        _persist_run(session_id, {"status": "running", "turns": turns})
        if time.monotonic() >= deadline:
            raise SieveError(f"timed out after {timeout}s waiting for {session_id}")
        time.sleep(delay)
        delay = min(delay * 2, max_delay)


def require_clean_result(run):
    """Return run['result'], refusing to present a failed-conformance payload.

    'fail' means the output is still non-conforming after repair; it must never
    be shown as clean data.
    """
    conf = run.get("schema_conformance") or {}
    if conf.get("status") == "fail":
        detail = conf.get("summary") or run.get("summary") or "output not conforming"
        raise SieveError(f"schema conformance failed: {detail}")
    return run.get("result")


def _url_is_first_party(url: str) -> bool:
    """True only when `url` resolves to the exact Sieve API origin.

    Compares the parsed (scheme, host, port) triple against BASE_URL so that
    lookalike hosts (`scrape.usesieve.com.evil.com`, `scrape.usesieve.com@evil`,
    wrong scheme/port) never qualify for credential attachment.
    """
    try:
        target = urllib.parse.urlsplit(url)
        base = urllib.parse.urlsplit(BASE_URL)
    except ValueError:
        return False
    return (target.scheme, target.hostname, target.port) == (
        base.scheme, base.hostname, base.port
    )


def download_files(run, dest_dir):
    """Download files[] from a done run (relative URLs prefixed with base URL).

    Credential isolation: `Authorization: Bearer <key>` is attached ONLY when
    the final URL is first-party (same origin as BASE_URL). Absolute URLs that
    point elsewhere are still fetched, but stripped of the API key so a hostile
    `files[].url` can never exfiltrate the Sieve token.
    """
    key = get_api_key()
    if not key:
        raise SieveNotConfigured("SIEVE_API_KEY is not configured")
    dest = Path(dest_dir)
    dest.mkdir(parents=True, exist_ok=True)
    saved = []
    for entry in run.get("files") or []:
        url = entry.get("url") or ""
        if not url:
            continue
        full = url if url.startswith("http") else BASE_URL + url
        headers = {}
        if _url_is_first_party(full):
            headers["Authorization"] = f"Bearer {key}"
        req = urllib.request.Request(full, headers=headers, method="GET")
        content = None
        for attempt in range(1, MAX_HTTP_RETRIES + 1):
            try:
                with urllib.request.urlopen(req, timeout=DOWNLOAD_TIMEOUT) as resp:
                    content = resp.read()
                break
            except urllib.error.HTTPError as exc:
                if exc.code >= 500 and attempt < MAX_HTTP_RETRIES:
                    time.sleep(min(2 ** attempt, 30))
                    continue
                raise _map_error(exc, {}) from None
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                if attempt < MAX_HTTP_RETRIES:
                    time.sleep(min(2 ** attempt, 15))
                    continue
                raise SieveUnavailable(f"network error downloading {full}: "
                                       f"{getattr(exc, 'reason', exc)}") from None
        name = Path(entry.get("name") or full).name
        target = dest / name
        target.write_bytes(content or b"")
        saved.append(target)
    return saved


def send_follow_up(session_id, body, *, wait_timeout=1800,
                   initial_delay=POLL_INITIAL_DELAY, max_delay=POLL_MAX_DELAY):
    """POST a follow-up turn and wait for the NEW answer.

    Turns are recorded before sending; polling stops only when status is
    'done' AND turns has advanced, otherwise the previous answer would be
    read. 409 means a turn is in flight: wait, then resend.
    """
    if not isinstance(body, dict) or not body:
        raise SieveRequestError("follow-up body must be a non-empty dict")
    before = get_run(session_id).get("turns", 0)   # record turns FIRST

    attempt = 0
    while True:
        attempt += 1
        try:
            _request("POST", f"/api/scrapes/{session_id}/messages", body,
                     retry_network=False)
            break
        except SieveConflict:
            if attempt > 6:
                raise
            time.sleep(initial_delay)

    delay = initial_delay
    deadline = time.monotonic() + wait_timeout
    while True:
        run = get_run(session_id)
        status = run.get("status")
        turns = run.get("turns", 0)
        if status == "done" and turns > before:
            _persist_run(session_id, {"status": "done", "turns": turns})
            return run
        if status == "refused":
            _persist_run(session_id, {"status": "refused",
                                      "refusal": run.get("refusal") or {}})
            raise SieveRefused(run.get("refusal"))
        if status not in ("running", "done"):
            raise SieveUnknownRunStatus(f"unexpected run status: {status!r}")
        _persist_run(session_id, {"status": status, "turns": turns})
        if time.monotonic() >= deadline:
            raise SieveError(f"timed out waiting for follow-up turn of {session_id}")
        time.sleep(delay)
        delay = min(delay * 2, max_delay)


def get_credits():
    """GET /api/me/credits -> plan/limit/used/remaining."""
    resp, _ = _request("GET", "/api/me/credits")
    return resp


# --------------------------------------------------------------------------- #
# Device login (no API key required)
# --------------------------------------------------------------------------- #
def device_code(client_name):
    """Step 1 of the device-code flow: request a code pair."""
    resp, _ = _request("POST", "/api/auth/device/code",
                       {"client_name": client_name}, auth=False, retry_network=False)
    return resp


def device_token(device_code_value):
    """Poll the device-code token endpoint.

    Returns {"ok": True, "api_key": ...} on success, or
    {"ok": False, "error": "<code>"} for authorization_pending / slow_down /
    access_denied / expired_token. The api_key must never be printed.
    """
    try:
        resp, _ = _request("POST", "/api/auth/device/token",
                           {"device_code": device_code_value},
                           auth=False, retry_network=False)
        return {"ok": True, "api_key": resp.get("api_key"),
                "key_name": resp.get("key_name")}
    except SieveRequestError as exc:
        return {"ok": False, "error": str(exc)}
