from pathlib import Path
import sys
import ipaddress
from unittest.mock import patch, MagicMock
import pytest

# Ensure 90_Shared_Toolbox/tools is in sys.path
toolbox_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox" / "tools"
if str(toolbox_path) not in sys.path:
    sys.path.insert(0, str(toolbox_path))

from quiz_qr import get_lan_ip, generate_quiz_link


def test_get_lan_ip_returns_valid_ipv4():
    ip = get_lan_ip()
    assert isinstance(ip, str)
    # Validate it's a valid IPv4 address
    parsed = ipaddress.IPv4Address(ip)
    assert parsed.version == 4


def test_get_lan_ip_secondary_fallback():
    # Mock socket where first connect fails, second succeeds
    mock_s = MagicMock()
    mock_s.connect.side_effect = [OSError("First connect failed"), None]
    mock_s.getsockname.return_value = ("192.168.1.42", 0)

    with patch("socket.socket", return_value=mock_s):
        ip = get_lan_ip()
        assert ip == "192.168.1.42"
        assert mock_s.connect.call_count == 2


def test_get_lan_ip_fallback_on_socket_error():
    with patch("socket.socket") as mock_socket:
        mock_socket.side_effect = OSError("Network unreachable")
        ip = get_lan_ip()
        assert ip == "127.0.0.1"


def test_generate_quiz_link_structure():
    with patch("quiz_qr.get_lan_ip", return_value="192.168.1.50"):
        link, lan_ip = generate_quiz_link("MATH-101", "midterm-quiz", print_qr=False)
        assert lan_ip == "192.168.1.50"
        assert link == "http://192.168.1.50:5000/quiz/MATH-101/midterm-quiz"


def test_generate_quiz_link_print_qr_disabled(capsys):
    with patch("quiz_qr.get_lan_ip", return_value="10.0.0.5"):
        link, lan_ip = generate_quiz_link("CS-101", "q1", print_qr=False)
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""


def test_generate_quiz_link_print_qr_enabled_output(capsys):
    with patch("quiz_qr.get_lan_ip", return_value="192.168.1.100"):
        link, lan_ip = generate_quiz_link("EE-201", "quiz-01", print_qr=True)
        captured = capsys.readouterr()
        assert "http://192.168.1.100:5000/quiz/EE-201/quiz-01" in captured.out
        assert "http://localhost:5000/quiz/EE-201/quiz-01" in captured.out


def test_generate_quiz_link_qrcode_missing_graceful_advice(capsys):
    with patch.dict(sys.modules, {"qrcode": None}):
        with patch("quiz_qr.get_lan_ip", return_value="192.168.1.100"):
            link, lan_ip = generate_quiz_link("CS-102", "quiz-02", print_qr=True)
            captured = capsys.readouterr()
            assert "qrcode" in captured.out.lower() or "pip install qrcode" in captured.out.lower()


def test_generate_quiz_link_qrcode_runtime_exception(capsys):
    mock_qr_module = MagicMock()
    mock_qr_instance = MagicMock()
    mock_qr_instance.make.side_effect = RuntimeError("Rendering error")
    mock_qr_module.QRCode.return_value = mock_qr_instance

    with patch.dict(sys.modules, {"qrcode": mock_qr_module}):
        with patch("quiz_qr.get_lan_ip", return_value="192.168.1.100"):
            link, lan_ip = generate_quiz_link("PHY-101", "quiz-03", print_qr=True)
            captured = capsys.readouterr()
            assert "Could not render QR code" in captured.out
            assert "http://192.168.1.100:5000/quiz/PHY-101/quiz-03" in captured.out

def test_check_adb_usb_device_success():
    from quiz_qr import check_adb_usb_device
    mock_proc = MagicMock()
    mock_proc.stdout = "List of devices attached\n166667061Y030799\tdevice\n"
    with patch("subprocess.run", return_value=mock_proc) as mock_run:
        assert check_adb_usb_device() is True
        # Verify adb reverse was called
        assert mock_run.call_count == 2


def test_check_adb_usb_device_none():
    from quiz_qr import check_adb_usb_device
    mock_proc = MagicMock()
    mock_proc.stdout = "List of devices attached\n\n"
    with patch("subprocess.run", return_value=mock_proc):
        assert check_adb_usb_device() is False


def test_resolve_quiz_slug_prefix():
    from quiz_qr import resolve_quiz_slug
    # Resolves Quiz_01 to Quiz_01_Software_Crisis for 04_Advanced_Software_Eng
    resolved = resolve_quiz_slug("04_Advanced_Software_Eng", "Quiz_01")
    assert resolved == "Quiz_01_Software_Crisis"


def test_standalone_launcher_uses_argument_array_not_shell():
    """Task 5 (Command Injection): launcher must use subprocess args, never os.system."""
    import inspect
    import quiz_qr

    src = inspect.getsource(quiz_qr)
    assert "os.system(" not in src, (
        "Command injection: quiz_qr.py still calls os.system() with a formatted command string"
    )
    assert hasattr(quiz_qr, "launch_standalone_window"), (
        "launch_standalone_window() helper missing from quiz_qr.py"
    )


def test_launch_standalone_window_rejects_shell_metacharacters():
    """Subject/quiz ids containing cmd metacharacters must be rejected before spawn."""
    from quiz_qr import launch_standalone_window

    with pytest.raises(ValueError):
        launch_standalone_window('04_Advanced" & calc', "Quiz_01")
    with pytest.raises(ValueError):
        launch_standalone_window("04_Advanced_Software_Eng", "Quiz_01|whoami")


def test_launch_standalone_window_spawns_argument_array():
    """Verify Popen receives a list (no shell=True, no string interpolation)."""
    from quiz_qr import launch_standalone_window

    with patch("subprocess.Popen") as mock_popen:
        launch_standalone_window("04_Advanced_Software_Eng", "Quiz_01")

    assert mock_popen.call_count == 1
    args, kwargs = mock_popen.call_args
    argv = args[0]
    assert isinstance(argv, list), "launcher must pass an argument list, not a shell string"
    assert kwargs.get("shell") is not True
    # user-controlled values must be discrete argv elements (never concatenated)
    assert "04_Advanced_Software_Eng" in argv
    assert "Quiz_01" in argv
    assert all(isinstance(a, str) for a in argv)


def test_launch_standalone_window_survives_missing_windows_only_flag():
    """``subprocess.CREATE_NEW_CONSOLE`` exists ONLY on Windows.

    GitHub's CI runs the suite on ``ubuntu-latest``, where that constant does
    not exist at all. Reading it unconditionally raises AttributeError before
    Popen is ever reached, so the launcher must treat the flag as optional.
    """
    import subprocess

    from quiz_qr import launch_standalone_window

    saved = getattr(subprocess, "CREATE_NEW_CONSOLE", None)
    try:
        if hasattr(subprocess, "CREATE_NEW_CONSOLE"):
            delattr(subprocess, "CREATE_NEW_CONSOLE")

        with patch("subprocess.Popen") as mock_popen:
            launch_standalone_window("04_Advanced_Software_Eng", "Quiz_01")
    finally:
        if saved is not None:
            subprocess.CREATE_NEW_CONSOLE = saved

    assert mock_popen.call_count == 1
    args, kwargs = mock_popen.call_args
    assert isinstance(args[0], list)
    assert kwargs.get("shell") is not True
    assert "creationflags" not in kwargs, (
        "creationflags must not be passed when Windows exposes no such flag"
    )


@pytest.mark.skipif(
    __import__("os").name != "nt", reason="CREATE_NEW_CONSOLE is a Windows-only flag"
)
def test_launch_standalone_window_requests_new_console_on_windows():
    """On Windows the standalone console window behaviour must be preserved."""
    import subprocess

    from quiz_qr import launch_standalone_window

    with patch("subprocess.Popen") as mock_popen:
        launch_standalone_window("04_Advanced_Software_Eng", "Quiz_01")

    assert (
        mock_popen.call_args.kwargs.get("creationflags")
        == subprocess.CREATE_NEW_CONSOLE
    )
