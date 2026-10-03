"""Contract tests for the two blocking delivery gates.

`note_linter.py --strict` must fail loudly on leaking notes (exit 1) and
pass clean ones (exit 0); `session_memory.py boot` must stay a cheap,
read-only fast-boot (< 150 tokens of output is aspirational — here we pin
exit 0 and non-empty output so a future refactor cannot silently break
AGENTS.md §8 step 1).
"""

import subprocess
import sys
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parent.parent
TOOLS = BASE_DIR / "90_Shared_Toolbox" / "tools"
CLEAN_NOTE = BASE_DIR / "01_Semester_1" / "04_Advanced_Software_Eng" / "03_Study_Notes" / "Week_02_Unit_05_RAD.md"


def _run(tool, *args):
    return subprocess.run(
        [sys.executable, str(TOOLS / tool), *args],
        capture_output=True,
        text=True,
        cwd=str(BASE_DIR),
    )


def test_note_linter_passes_clean_unit():
    proc = _run("note_linter.py", str(CLEAN_NOTE), "--strict")
    assert proc.returncode == 0, f"clean unit must pass the gate:\n{proc.stdout[-2000:]}"


def test_note_linter_fails_leaking_note(tmp_path):
    bad = tmp_path / "leak.md"
    bad.write_text(
        "---\ntitle: Leak\n---\n\n# Unit 01\n\nSee File 02 of 10 for more. **EN.**\n",
        encoding="utf-8",
    )
    proc = _run("note_linter.py", str(bad), "--strict")
    assert proc.returncode == 1, "leaking note must fail the gate (exit 1)"


def test_session_memory_boot_is_cheap_and_readonly():
    before = {p.name for p in TOOLS.glob("*.tmp")}
    proc = _run("session_memory.py", "boot")
    assert proc.returncode == 0, f"boot must exit 0:\n{proc.stderr[-1000:]}"
    assert proc.stdout.strip(), "boot must inject context, not silence"
    after = {p.name for p in TOOLS.glob("*.tmp")}
    assert after == before, "boot must not leave scratch files behind"
