"""Contract tests for the phone-sync tool (``90_Shared_Toolbox/tools/phone_sync.py``).

Why this file exists
--------------------
The first version of ``phone_sync.py`` shipped eight defects that no test could
have caught, because nothing asserted the tool's *contract*:

* every ``adb push`` result was discarded, so a run in which every transfer
  failed still printed ``SYNC COMPLETE: 100% Up-to-Date``;
* no ``--sync``, so the whole ~1.3 GB vault was re-sent on every run;
* exclusions were applied at the top level only, so three nested ``.git``
  directories (≈26 MB) were pushed to the phone;
* ``--all`` and ``--clean`` were documented in the docstring and never
  implemented;
* ``quiz_mobile.html`` — a dead reference, archived and gitignored;
* dead counters (``synced_items``, ``total_bytes``) computed and discarded;
* "adb is not installed" and "no phone is attached" produced the same
  misleading error;
* two attached devices failed silently.

These tests pin the *behaviour*, not the implementation. ADB is replaced by a
recorder and the vault is a synthetic tree in ``tmp_path``, so no test here can
touch a real device or modify the real vault. Two read-only tests at the end
run against the actual vault, because the nested-``.git`` regression lives in
its real shape.
"""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox" / "tools" / "phone_sync.py"
SPEC = importlib.util.spec_from_file_location("phone_sync_under_test", MODULE_PATH)
ps = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ps)


# --------------------------------------------------------------------------- #
# A fake adb that records argv instead of touching a device
# --------------------------------------------------------------------------- #


class _Completed:
    def __init__(self, returncode=0, stdout=b"", stderr=b""):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


class FakeAdb:
    """Records every adb invocation; answers as a well-behaved device would."""

    DEVICE_OK = b"List of devices attached\nFAKE123\tdevice\n"
    PUSH_OK = b"12 files pushed, 34 skipped. 8.4 MB/s (1048576 bytes in 0.125s)\n"
    PULL_OK = b"7 files pulled. 5.0 MB/s (524288 bytes in 0.104s)\n"

    def __init__(self):
        self.calls: list[list[str]] = []
        self.devices_payload = self.DEVICE_OK
        self.remote_files: list[str] = []
        self.fail_push_for: set[str] = set()
        self.sizes_supported = True
        # Path -> size reported for the device copy. Unset paths report the
        # vault's own size, i.e. "in sync"; override one to simulate drift.
        self.size_overrides: dict[str, int] = {}

    # -- helpers ----------------------------------------------------------- #

    def _strip(self, argv: list[str]) -> list[str]:
        cmd = list(argv)
        while cmd and cmd[0] != "adb":
            cmd.pop(0)
        cmd = cmd[1:]
        if cmd and cmd[0] == "-s":
            cmd = cmd[2:]
        return cmd

    def _by(self, verb: str) -> list[list[str]]:
        out = []
        for call in self.calls:
            stripped = self._strip(call)
            if stripped and stripped[0] == verb:
                out.append(stripped)
        return out

    def pushes(self) -> list[list[str]]:
        return self._by("push")

    def pulls(self) -> list[list[str]]:
        return self._by("pull")

    def shells(self) -> list[str]:
        return [c[-1] for c in self._by("shell")]

    def push_sources(self) -> list[str]:
        return [c[-2] for c in self.pushes()]

    def push_destinations(self) -> list[str]:
        return [c[-1] for c in self.pushes()]

    def device_size(self, rel: str) -> int:
        if rel in self.size_overrides:
            return self.size_overrides[rel]
        local = ps.VAULT_ROOT / rel
        return local.stat().st_size if local.is_file() else 0

    # -- the stub ---------------------------------------------------------- #

    def __call__(self, args, capture_output=True, timeout=None, check=False):
        self.calls.append(list(args))
        cmd = self._strip(args)
        if not cmd:
            return _Completed()
        head = cmd[0]
        if head == "devices":
            return _Completed(stdout=self.devices_payload)
        if head == "push":
            if any(p in self.fail_push_for for p in cmd):
                return _Completed(returncode=1, stderr=b"adb: error: failed to copy")
            # adb writes its summary to stderr, never to stdout.
            return _Completed(stderr=self.PUSH_OK)
        if head == "pull":
            return _Completed(stdout=self.PULL_OK)
        if head == "shell":
            command = cmd[-1]
            if "-exec stat" in command and self.sizes_supported:
                payload = "".join(
                    f"{self.device_size(rel)}|./{rel}\n" for rel in self.remote_files
                )
                return _Completed(stdout=payload.encode("utf-8"))
            if "find . -type f" in command:
                payload = "".join(f"./{f}\n" for f in self.remote_files)
                return _Completed(stdout=payload.encode("utf-8"))
            if "[ -d " in command:
                return _Completed(stdout=b"yes\n")
            return _Completed()
        return _Completed()


@pytest.fixture
def fake_adb(monkeypatch):
    stub = FakeAdb()
    monkeypatch.setattr(ps.subprocess, "run", stub)
    return stub


# --------------------------------------------------------------------------- #
# A synthetic vault with junk at depth
# --------------------------------------------------------------------------- #

SYNTHETIC = {
    "AGENTS.md": "root doc",
    "README.md": "root doc",
    "knowledge.md": "root doc",
    "00_STUDIO_HUB/ACTIVE_STATE.md": "hub",
    "00_STUDIO_HUB/agents/persona.md": "hub",
    "00_STUDIO_HUB/agents/desktop.ini": "drive junk",
    "00_STUDIO_HUB/deep/nested/keep.md": "deep keep",
    "00_STUDIO_HUB/deep/nested/__pycache__/junk.pyc": "junk",
    "00_STUDIO_HUB/deep/nested/__pycache__/junk.py": "junk",
    "01_Semester_1/SubjectA/03_Study_Notes/W01.md": "note",
    "01_Semester_1/SubjectA/03_Study_Notes/ملف عربي.md": "arabic note",
    "01_Semester_1/SubjectA/02_Raw_Materials/repo/.git/config": "junk",
    "01_Semester_1/SubjectA/02_Raw_Materials/repo/paper.pdf": "paper",
    "01_Semester_1/SubjectA/02_Raw_Materials/repo/desktop.ini": "drive junk",
    ".obsidian/app.json": "{}",
}

# A clean directory with enough files that a per-file push would be obvious.
BULK_DIR = "00_STUDIO_HUB/guides"
BULK_FILES = [f"{BULK_DIR}/g{i:02d}.md" for i in range(12)]
SYNTHETIC.update({rel: f"guide {i}" for i, rel in enumerate(BULK_FILES)})

# Files that must reach the phone: 27 fixtures minus 5 junk entries.
EXPECTED_ON_PHONE = {
    "AGENTS.md",
    "README.md",
    "knowledge.md",
    "00_STUDIO_HUB/ACTIVE_STATE.md",
    "00_STUDIO_HUB/agents/persona.md",
    "00_STUDIO_HUB/deep/nested/keep.md",
    "01_Semester_1/SubjectA/03_Study_Notes/W01.md",
    "01_Semester_1/SubjectA/03_Study_Notes/ملف عربي.md",
    "01_Semester_1/SubjectA/02_Raw_Materials/repo/paper.pdf",
    ".obsidian/app.json",
} | set(BULK_FILES)


@pytest.fixture
def vault(tmp_path, monkeypatch):
    root = tmp_path / "vault"
    for rel, text in SYNTHETIC.items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    monkeypatch.setattr(ps, "VAULT_ROOT", root)
    monkeypatch.setattr(ps, "LOCAL_INBOX", tmp_path / "inbox")
    return root


def scope() -> list[str]:
    return [t for t in ps.CORE_TARGETS if (ps.VAULT_ROOT / t).is_dir()]


def posix(paths: list[str]) -> list[str]:
    """adb sources are Windows paths here; compare them slash-agnostically."""
    return [p.replace("\\", "/") for p in paths]


# --------------------------------------------------------------------------- #
# Planning: what is in scope, and what must never leave the machine
# --------------------------------------------------------------------------- #


def test_manifest_contains_exactly_the_clean_files(vault):
    assert ps.local_manifest(scope()) == EXPECTED_ON_PHONE


@pytest.mark.parametrize("junk", [
    "__pycache__",
    ".git",
    "desktop.ini",
])
def test_exclusions_apply_at_every_depth(vault, junk):
    """The v1 bug: only top-level names were filtered, so nested junk shipped."""
    manifest = ps.local_manifest(scope())
    assert not any(junk in rel for rel in manifest), f"{junk} leaked into the plan"


def test_polluted_dirs_track_the_branches_that_hold_junk(vault):
    polluted = ps.compute_polluted(scope())
    # the two branches that actually contain junk, and every ancestor of them
    assert "00_STUDIO_HUB/deep/nested" in polluted
    assert "00_STUDIO_HUB/deep" in polluted
    assert "01_Semester_1/SubjectA/02_Raw_Materials/repo" in polluted
    # a clean branch must stay bulk-pushable
    assert "00_STUDIO_HUB/agents" not in polluted
    assert ".obsidian" not in polluted


# --------------------------------------------------------------------------- #
# Push shape
# --------------------------------------------------------------------------- #


def test_directories_are_pushed_in_bulk_not_file_by_file(vault, fake_adb):
    ps.main(["--quiet", "--no-verify"])
    sources = posix(fake_adb.push_sources())

    # a clean directory with 12 files costs exactly one adb call...
    assert sources.count(posix([str(vault / BULK_DIR)])[0] + "/.") == 1
    assert not any(s.endswith("g00.md") for s in sources)
    # ...while a polluted branch is descended into, one file at a time
    assert any(s.endswith("repo/paper.pdf") for s in sources)
    # and the bulk form is strictly cheaper than a call per file
    assert len(sources) < len(EXPECTED_ON_PHONE)


def test_directory_push_keeps_the_raw_dot_suffix(vault, fake_adb):
    """``pathlib`` eats ``Path / "."``; adb then nests dirs inside same-named dirs."""
    ps.main(["--quiet", "--no-verify"])
    for source in fake_adb.push_sources():
        if Path(source).is_dir():
            assert source.endswith("/."), f"bulk source lost its '/.': {source}"


def test_junk_is_never_placed_by_a_push(vault, fake_adb):
    """Excluded *files* may ride along inside a bulk directory — they are then
    removed by the device purge — but an excluded *directory* must never fall
    inside a bulk source, or its whole contents ship."""
    ps.main(["--quiet", "--no-verify"])
    sources = posix(fake_adb.push_sources())

    assert not any(s.endswith("02_Raw_Materials/.") for s in sources)
    assert not any(s.endswith("repo/.") for s in sources)
    assert not any(s.endswith("nested/.") for s in sources)
    assert not any("__pycache__" in s for s in sources)
    assert not any("/.git" in s for s in sources)
    # and the junk that does exist is cleaned on the device instead
    assert any("__pycache__" in s for s in fake_adb.shells())


def test_incremental_and_dry_run_flags(vault, fake_adb):
    ps.main(["--quiet", "--no-verify", "--dry-run"])
    for call in fake_adb.pushes():
        assert "--sync" in call, "incremental sync was dropped"
        assert "-n" in call, "dry run did not ask adb to write nothing"


def test_full_mode_drops_sync(vault, fake_adb):
    ps.main(["--quiet", "--no-verify", "--full"])
    assert fake_adb.pushes()
    for call in fake_adb.pushes():
        assert "--sync" not in call


def test_all_mode_adds_the_development_folders(vault, fake_adb):
    for name in ps.EXTRA_TARGETS:
        target = vault / name / "sample.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("dev", encoding="utf-8")
    ps.main(["--quiet", "--no-verify", "--all"])
    blob = "\n".join(fake_adb.push_destinations())
    for name in ps.EXTRA_TARGETS:
        assert f"/{name}/" in blob, f"--all did not mirror {name}"


# --------------------------------------------------------------------------- #
# Honesty: exit status and reporting
# --------------------------------------------------------------------------- #


def test_perfect_mirror_exits_zero(vault, fake_adb):
    fake_adb.remote_files = sorted(EXPECTED_ON_PHONE)
    assert ps.main(["--quiet"]) == 0


def test_files_missing_on_the_device_fail_the_run(vault, fake_adb):
    """Verification is the only thing that can catch a silently skipped file."""
    fake_adb.remote_files = sorted(EXPECTED_ON_PHONE)[:-1]
    assert ps.main(["--quiet"]) == 1


def test_a_failed_push_is_never_reported_as_success(vault, fake_adb):
    """The v1 headline bug: failures were swallowed and success was printed."""
    fake_adb.remote_files = sorted(EXPECTED_ON_PHONE)
    fake_adb.fail_push_for = {str(vault / "AGENTS.md")}
    assert ps.main(["--quiet"]) == 1


def test_summary_reports_real_numbers(vault, fake_adb, capsys):
    fake_adb.remote_files = sorted(EXPECTED_ON_PHONE)
    ps.main([])
    out = capsys.readouterr().out
    # real counts parsed out of adb's own output, not the number of calls we made
    assert re.search(r"pushed \d+ file\(s\) \(\d+(\.\d+)? [KMG]B, \d+\.\d MB/s\)", out), out
    assert re.search(r"skipped \d+ unchanged file\(s\)", out), out
    assert "excluded 2 junk dir(s)" in out
    assert "100% Up-to-Date" not in out  # the v1 lie must not come back


def test_json_summary_is_machine_readable(vault, fake_adb, capsys):
    import json

    fake_adb.remote_files = sorted(EXPECTED_ON_PHONE)
    ps.main(["--json", "--quiet"])
    payload = json.loads(capsys.readouterr().out)
    assert payload["ok"] is True
    assert payload["missing_on_device"] == []
    assert payload["files_pushed"] > 0


def test_push_statistics_are_read_from_stderr(vault, fake_adb, capsys):
    """adb reports 'N files pushed' on *stderr*; reading stdout alone yields zero."""
    fake_adb.remote_files = sorted(EXPECTED_ON_PHONE)
    ps.main([])
    out = capsys.readouterr().out
    match = re.search(r"pushed (\d+) file\(s\) \(([\d.]+ [KMG]B)", out)
    assert match, out
    assert int(match.group(1)) > 0, "the push summary was not parsed"
    assert int(re.search(r"skipped (\d+) unchanged", out).group(1)) > 0


def test_drifted_file_is_detected_and_force_repaired(vault, fake_adb, capsys):
    """``--sync`` trusts timestamps, so a newer-but-different device copy is
    skipped on every run. Measured live on 2026-10-07: the phone kept a
    31,188-byte AGENTS.md against the vault's 25,697-byte one, and every sync
    reported success. Verification must compare sizes and force the file back."""
    fake_adb.remote_files = sorted(EXPECTED_ON_PHONE)
    fake_adb.size_overrides["AGENTS.md"] = 999_999
    assert ps.main([]) == 0
    out = capsys.readouterr().out
    assert "different content" in out
    assert "repaired 1 file(s)" in out

    forced = [c for c in fake_adb.pushes() if c[-1].endswith("/AGENTS.md")]
    assert forced, "the drifted file was never re-pushed"
    # the repair pass is the one that must ignore timestamps, or it repeats the
    # very comparison that let the file drift
    assert any("--sync" not in c for c in forced), \
        "drift repair was attempted with --sync"


def test_no_repair_reports_drift_as_an_unresolved_problem(vault, fake_adb, capsys):
    fake_adb.remote_files = sorted(EXPECTED_ON_PHONE)
    fake_adb.size_overrides["AGENTS.md"] = 999_999
    assert ps.main(["--no-repair"]) == 1
    assert "different content" in capsys.readouterr().out


def test_device_that_cannot_report_sizes_says_so(vault, fake_adb, capsys):
    """Degrading to existence-only must be announced, not passed off as verified."""
    fake_adb.remote_files = sorted(EXPECTED_ON_PHONE)
    fake_adb.sizes_supported = False
    assert ps.main([]) == 0
    assert "existence-only" in capsys.readouterr().out


# --------------------------------------------------------------------------- #
# Device-side hygiene
# --------------------------------------------------------------------------- #


def test_prune_lists_stale_files_and_deletes_nothing_without_confirmation(vault, fake_adb):
    fake_adb.remote_files = sorted(EXPECTED_ON_PHONE) + ["00_STUDIO_HUB/stale.pdf"]
    assert ps.main(["--quiet", "--prune"]) == 0
    assert not any("rm -f " in s for s in fake_adb.shells())


def test_clean_yes_removes_stale_files(vault, fake_adb):
    fake_adb.remote_files = sorted(EXPECTED_ON_PHONE) + ["00_STUDIO_HUB/stale.pdf"]
    ps.main(["--quiet", "--clean", "--yes"])
    deletes = [s for s in fake_adb.shells() if "rm -f " in s]
    assert deletes, "clean --yes deleted nothing"
    assert "stale.pdf" in deletes[0]


def test_junk_purge_runs_on_the_device(vault, fake_adb):
    ps.main(["--quiet", "--no-verify"])
    shells = fake_adb.shells()
    assert any("__pycache__" in s and "-prune" in s for s in shells)
    assert any("desktop.ini" in s for s in shells)


def test_junk_purge_is_derived_from_the_plan(vault, fake_adb):
    """A hand-written purge list silently diverges from the plan: 104 files
    under ``.superpowers/`` survived on the phone for that exact reason."""
    ps.main(["--quiet", "--no-verify"])
    purge = "\n".join(fake_adb.shells())
    for name in sorted(ps.EXCLUDE_DIR_NAMES):
        assert name in purge, f"the device purge does not sweep excluded dir {name!r}"


def test_junk_purge_can_be_skipped(vault, fake_adb):
    ps.main(["--quiet", "--no-verify", "--no-junk-purge"])
    assert not any("-prune" in s for s in fake_adb.shells())


# --------------------------------------------------------------------------- #
# Phone -> PC
# --------------------------------------------------------------------------- #


def test_pull_targets_the_inbox(vault, fake_adb, tmp_path):
    ps.main(["--quiet", "--no-verify", "--pull"])
    pulls = fake_adb.pulls()
    assert pulls, "pull never ran"
    assert pulls[0][-2] == f"{ps.PHONE_INBOX}/."
    assert Path(pulls[0][-1]) == tmp_path / "inbox"


# --------------------------------------------------------------------------- #
# Device states: every failure must be distinguishable
# --------------------------------------------------------------------------- #


def test_no_device_is_a_clear_error(fake_adb, capsys):
    fake_adb.devices_payload = b"List of devices attached\n\n"
    assert ps.main(["--quiet"]) == 1
    assert "No Android device detected" in capsys.readouterr().out


def test_unauthorized_device_tells_the_user_what_to_do(fake_adb, capsys):
    fake_adb.devices_payload = b"List of devices attached\nFAKE123\tunauthorized\n"
    assert ps.main(["--quiet"]) == 1
    out = capsys.readouterr().out
    assert "unauthorized" in out
    assert "Allow USB debugging" in out


def test_two_devices_requires_an_explicit_serial(fake_adb, capsys):
    fake_adb.devices_payload = b"List of devices attached\nA1\tdevice\nB2\tdevice\n"
    assert ps.main(["--quiet"]) == 1
    out = capsys.readouterr().out
    assert "More than one device" in out and "--serial" in out


def test_missing_adb_binary_is_not_reported_as_a_missing_phone(monkeypatch, capsys):
    def boom(*_a, **_kw):
        raise FileNotFoundError("adb")

    monkeypatch.setattr(ps.subprocess, "run", boom)
    assert ps.main(["--quiet"]) == 1
    out = capsys.readouterr().out
    assert "adb was not found" in out
    assert "No Android device detected" not in out


# --------------------------------------------------------------------------- #
# The real vault (read-only): the regression in its real shape
# --------------------------------------------------------------------------- #


def test_real_vault_plan_is_junk_free():
    targets = [t for t in ps.CORE_TARGETS if (ps.VAULT_ROOT / t).is_dir()]
    manifest = ps.local_manifest(targets)
    assert manifest, "the real vault produced an empty plan"
    for rel in manifest:
        parts = rel.split("/")
        assert not (set(parts) & ps.EXCLUDE_DIR_NAMES), f"excluded dir in plan: {rel}"
        assert not ps.is_excluded_file(parts[-1]), f"excluded file in plan: {rel}"


def test_real_vault_nested_git_dirs_are_excluded_from_the_bulk_push():
    """Three repos under the AI raw materials carried ~26 MB of ``.git``."""
    targets = [t for t in ps.CORE_TARGETS if (ps.VAULT_ROOT / t).is_dir()]
    polluted = ps.compute_polluted(targets)
    nested = [p for p in polluted if p.endswith("_github")]
    assert nested, "the nested git repos are no longer detected"
    assert all(".git" not in p for p in polluted)


def test_real_vault_keeps_arabic_filenames_intact():
    targets = [t for t in ps.CORE_TARGETS if (ps.VAULT_ROOT / t).is_dir()]
    manifest = ps.local_manifest(targets)
    arabic = [rel for rel in manifest if any(ord(c) > 127 for c in rel)]
    assert arabic, "no Arabic filenames found — UTF-8 handling is now untested"
