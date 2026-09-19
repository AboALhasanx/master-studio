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
