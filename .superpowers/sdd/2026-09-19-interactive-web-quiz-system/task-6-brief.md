# Task 6 Brief: LAN QR Code Generator Helper

**Files:**
- Create: `90_Shared_Toolbox/tools/quiz_qr.py`
- Test: `tests/test_quiz_qr.py`

**Interfaces:**
- Produces:
  - `get_lan_ip() -> str`: Detects host Wi-Fi LAN IP (falls back to `127.0.0.1`).
  - `generate_quiz_link(subject_id: str, quiz_id: str, print_qr: bool = True) -> tuple[str, str]`:
    - Returns `(link, lan_ip)`.
    - `link` format: `http://{lan_ip}:5000/quiz/{subject_id}/{quiz_id}`.
    - If `print_qr=True`: prints a clean banner with LAN URL, Local URL, and attempts to render an ASCII QR code (gracefully advising if `qrcode` package is not installed).

**TDD Workflow:**
1. Write `tests/test_quiz_qr.py` testing URL format and LAN IP resolution.
2. Run `pytest tests/test_quiz_qr.py` (verify failure).
3. Implement `90_Shared_Toolbox/tools/quiz_qr.py`.
4. Run `pytest tests/test_quiz_qr.py` (verify pass).
5. Write execution report to `.superpowers/sdd/2026-09-19-interactive-web-quiz-system/task-6-report.md`.
