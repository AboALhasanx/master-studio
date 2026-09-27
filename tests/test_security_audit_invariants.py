"""
Security Audit Regression Suite (Task 7)
========================================

Machine-checkable invariants for all 11 risky sinks audited under the
6-factor framework:

    credential <-> tenant/scope <-> actor/session <-> target/resource
        <-> action/intent <-> time/state

Each test proves ONE flow is NOT vulnerable. Together they form the
zero-defect gate: if any regression reintroduces a sink weakness, this
suite fails before the artifact can be shipped.

Flows proven NOT vulnerable by inspection are pinned here too, so a future
edit cannot silently downgrade them back to vulnerable.
"""

import json
import re
import sys
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parent.parent
DASHBOARD = BASE_DIR / "91_Dashboard"
TOOLS = BASE_DIR / "90_Shared_Toolbox" / "tools"

for p in (str(DASHBOARD), str(TOOLS)):
    if p not in sys.path:
        sys.path.insert(0, p)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _code_only(src: str) -> str:
    """Strip comments and string literals.

    The vault-wide sweep asserts ABSENT patterns (``shell=True``,
    ``os.system(``); a docstring that merely discusses them must not trip the
    gate, while the real call sites still must.
    """
    import io
    import tokenize

    kept = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type in (tokenize.COMMENT, tokenize.STRING):
                continue
            kept.append(tok.string)
    except (tokenize.TokenError, SyntaxError, IndentationError):
        return src
    return " ".join(kept)


@pytest.fixture
def client():
    from app import app

    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


# --------------------------------------------------------------------------- #
# Flow 1 - Network listener / Werkzeug interactive debugger (Critical RCE)
# --------------------------------------------------------------------------- #
def test_flask_debug_disabled_by_default():
    """No auth <-> 0.0.0.0 <-> any LAN host <-> HTTP <-> debug must be OFF."""
    import app as dashboard_app

    assert not dashboard_app.app.config.get("DEBUG", False), (
        "Critical RCE: Flask debug=True exposes the /console debugger to the LAN"
    )


def test_app_run_gate_is_env_controlled_not_hardcoded_true():
    src = _read(DASHBOARD / "app.py")
    # Find the app.run call inside __main__
    idx = src.find('if __name__ == "__main__":')
    assert idx != -1
    main_block = src[idx:]
    run_idx = main_block.find("app.run(")
    assert run_idx != -1, "app.run(...) missing"
    run_call = main_block[run_idx : run_idx + 300]

    assert "debug=True" not in run_call, (
        "Critical RCE: debug=True hardcoded in app.run() on 0.0.0.0"
    )
    assert "debug=" in run_call, "debug flag must be explicit (env-driven)"


# --------------------------------------------------------------------------- #
# Flow 2 - Telemetry file write / path traversal (High)
# --------------------------------------------------------------------------- #
def test_quiz_engine_uuid_allowlist_is_enforced():
    from quiz_engine import process_quiz_telemetry

    base = {
        "subject_id": "01_Cyber_Security",
        "topic": "T",
        "summary": {"percentage": 100, "correct": 1, "total": 1},
    }
    for evil in (
        "../../evil",
        "..\\evil",
        "a/../../b",
        "sub/uuid",
        "<script>",
        "x" * 200,
    ):
        payload = dict(base, submission_uuid=evil)
        res = process_quiz_telemetry(payload, Path(__file__).parent)
        assert res.get("status") == "error", (
            f"path traversal/log injection accepted: {evil!r}"
        )


def test_quiz_engine_missing_uuid_is_rejected():
    from quiz_engine import process_quiz_telemetry

    res = process_quiz_telemetry(
        {"subject_id": "S", "topic": "T",
         "summary": {"percentage": 0, "correct": 0, "total": 1}},
        Path(__file__).parent,
    )
    assert res.get("status") == "error"


def test_quiz_engine_temp_swap_names_are_randomized():
    """Swap files must never embed attacker-controlled submission_uuid."""
    src = _read(TOOLS / "quiz_engine.py")
    assert "quiz_history_{sub_uuid}.tmp" not in src, (
        "path traversal: submission_uuid still used to build temp file name"
    )
    assert "uuid.uuid4()" in src or "uuid4()" in src, (
        "atomic swap must use a randomized name"
    )


# --------------------------------------------------------------------------- #
# Flow 3 - Web-share JSON script-tag breakout (stored/reflected XSS)
# --------------------------------------------------------------------------- #
def test_safe_json_for_html_escapes_breakout_chars():
    from app import safe_json_for_html

    out = safe_json_for_html({"topic": "</script><script>alert(1)</script>"})
    assert "</script>" not in out
    assert "<" not in out and ">" not in out
    # must still round-trip as valid JSON for the browser
    parsed = json.loads(out)
    assert parsed["topic"] == "</script><script>alert(1)</script>"


def test_quiz_hub_uses_safe_serializer_not_raw_dumps():
    src = _read(DASHBOARD / "app.py")
    idx = src.find("def quiz_hub(")
    assert idx != -1
    body = src[idx : idx + 2500]
    assert "shared_quizzes=safe_json_for_html(" in body, (
        "XSS: quiz_hub still uses raw json.dumps() for the shared_quizzes blob"
    )


# --------------------------------------------------------------------------- #
# Flow 4 - DOM XSS in review card explanation (medium)
# --------------------------------------------------------------------------- #
def test_review_explanation_is_escaped_before_innerhtml():
    src = _read(DASHBOARD / "static" / "quiz.js")
    idx = src.find("review-explanation-box")
    assert idx != -1
    window = src[idx : idx + 400]
    assert "this.escapeHtml(q.explanation)" in window
    assert "${q.explanation}" not in window


def test_escapeHtml_helper_still_present():
    src = _read(DASHBOARD / "static" / "quiz.js")
    assert re.search(r"escapeHtml\s*\(\s*str\s*\)", src), (
        "escapeHtml() helper missing - all DOM sinks depend on it"
    )


# --------------------------------------------------------------------------- #
# Flow 5 - OS command injection in standalone launcher (medium/high)
# --------------------------------------------------------------------------- #
def test_quiz_qr_never_calls_os_system():
    import quiz_qr

    src = _code_only(_read(Path(quiz_qr.__file__)))
    assert "os.system(" not in src, (
        "command injection: os.system() present in quiz_qr.py"
    )


def test_quiz_qr_validates_identifiers_before_spawn():
    from quiz_qr import launch_standalone_window

    for bad in ('a"&calc', "b|whoami", "c&&dir", "d<e", 'f"g', "%PATH%"):
        with pytest.raises(ValueError):
            launch_standalone_window(bad, "Quiz_01")
        with pytest.raises(ValueError):
            launch_standalone_window("04_Advanced_Software_Eng", bad)


def test_quiz_qr_popen_uses_argv_array_without_shell():
    from unittest.mock import patch

    from quiz_qr import launch_standalone_window

    with patch("subprocess.Popen") as mock_popen:
        launch_standalone_window("04_Advanced_Software_Eng", "Quiz_01")

    args, kwargs = mock_popen.call_args
    assert isinstance(args[0], list)
    assert kwargs.get("shell") is not True


# --------------------------------------------------------------------------- #
# Flow 6 - Bearer token third-party exfiltration (medium/high)
# --------------------------------------------------------------------------- #
def test_sieve_url_origin_classifier_rejects_lookalikes():
    from sieve_client import _url_is_first_party

    assert _url_is_first_party("https://scrape.usesieve.com/files/x")
    assert _url_is_first_party("https://scrape.usesieve.com/anything?query=1")

    # host-suffix / port / scheme tricks
    assert not _url_is_first_party("https://scrape.usesieve.com.evil.com/x")
    assert not _url_is_first_party("https://evil.com/https://scrape.usesieve.com")
    assert not _url_is_first_party("http://scrape.usesieve.com/x")  # scheme downgrade
    assert not _url_is_first_party("https://evil.com/x")


def test_download_files_builds_header_only_for_first_party():
    """Static proof that Authorization is conditional, not unconditional."""
    src = _read(TOOLS / "sieve_client.py")
    idx = src.find("def download_files(")
    assert idx != -1
    body = src[idx : idx + 1600]
    assert "if _url_is_first_party(full):" in body, (
        "credential leak: Authorization header is not origin-gated"
    )


# --------------------------------------------------------------------------- #
# Flows 7 & 8 - Quiz import / read traversal (proven NOT vulnerable)
# --------------------------------------------------------------------------- #
def test_vault_name_validator_blocks_traversal():
    from app import is_safe_vault_name

    assert is_safe_vault_name("04_Advanced_Software_Eng")
    assert not is_safe_vault_name("../etc")
    assert not is_safe_vault_name("..\\Windows")
    assert not is_safe_vault_name("a/b")


def test_quiz_api_rejects_traversal_subject_and_quiz_id(client):
    for path in (
        "/api/quiz/..%2F..%2Fsecrets/Quiz_01",
        "/api/quiz/01_Cyber_Security/..%2F..%2Fapp",
        "/api/quiz/..%5C..%5Capp/Quiz_01",
    ):
        res = client.get(path)
        assert res.status_code in (400, 404), (
            f"traversal not rejected for {path}: {res.status_code}"
        )


# --------------------------------------------------------------------------- #
# Flow 9 - Bookmarks atomic write (proven NOT vulnerable)
# --------------------------------------------------------------------------- #
def test_bookmark_sink_path_is_fixed_and_payload_typed():
    src = _read(DASHBOARD / "app.py")
    idx = src.find("quiz_bookmarks.json")
    assert idx != -1
    # the destination must be a constant, never derived from request input
    assert 'HUB / "quiz_bookmarks.json"' in src or "HUB/'quiz_bookmarks.json'" in src


# --------------------------------------------------------------------------- #
# Flow 11 - Phone sync must never use a shell
# --------------------------------------------------------------------------- #
def test_phone_sync_uses_argv_arrays():
    src = _read(TOOLS / "phone_sync.py")
    assert "shell=True" not in src, "phone_sync must never spawn a shell"
    assert "os.system(" not in src, "phone_sync must never call os.system()"


# --------------------------------------------------------------------------- #
# Vault-wide sweep: no regressions reintroduced anywhere in the core tools
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize("rel", [
    "90_Shared_Toolbox/tools/quiz_engine.py",
    "90_Shared_Toolbox/tools/quiz_qr.py",
    "90_Shared_Toolbox/tools/phone_sync.py",
    "90_Shared_Toolbox/tools/session_memory.py",
    "91_Dashboard/app.py",
])
def test_no_shell_execution_in_critical_modules(rel):
    src = _code_only(_read(BASE_DIR / rel))
    assert "shell=True" not in src, f"{rel}: shell=True reintroduced"
    assert "os.system(" not in src, f"{rel}: os.system() reintroduced"


def test_flask_app_has_no_debug_pin_backdoor():
    src = _read(DASHBOARD / "app.py")
    assert "use_debugger=True" not in src
    assert "app.run(" in src
