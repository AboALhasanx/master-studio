#!/usr/bin/env python3
"""Master Studio - 1-Click Local Phone Sync (offline, incremental, honest).

Transfers the vault to the phone over ADB - USB cable or Wi-Fi - with no
Syncthing, no cloud round-trip and no background battery drain.

Design rules
------------
* Incremental. ``adb push --sync`` ships only files whose timestamp differs,
  so re-syncing the ~4,000-file vault costs seconds, not minutes.
* Honest. Every push invocation is checked. The summary reports real bytes,
  real skips and real failures, and the process exits non-zero if anything
  failed. It never prints "100% up to date" on a partial transfer.
* Correct. Junk is excluded at *every* depth, not just the top level; leftover
  junk pushed by older runs is purged on the device; ``--prune`` can turn the
  phone copy into an exact mirror of the vault.
* Safe. ADB is always invoked with argv arrays - never a shell - and device
  output is decoded as UTF-8 so Arabic filenames survive the round trip.

Usage
-----
    python phone_sync.py                  # incremental sync of study folders
    python phone_sync.py --dry-run        # show what would change, change nothing
    python phone_sync.py --all            # also toolbox + dashboard + docs
    python phone_sync.py --full           # ignore timestamps, re-push everything
    python phone_sync.py --prune          # list phone files that no longer exist here
    python phone_sync.py --clean --yes    # ... and delete them (exact mirror)
    python phone_sync.py --pull           # bring phone-authored files back to the vault
    python phone_sync.py --wifi 192.168.1.7
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

VAULT_ROOT = Path(__file__).resolve().parents[2]
PHONE_DEST = "/storage/emulated/0/Documents/MasterStudio"
PHONE_INBOX = f"{PHONE_DEST}/_inbox"           # phone -> PC hand-off folder
LOCAL_INBOX = VAULT_ROOT / "_inbox_from_phone"  # where --pull lands
DEFAULT_PORT = 5000                            # dashboard / PWA over USB reverse

# Study folders mirrored to the phone on every run.
CORE_TARGETS = [
    "00_STUDIO_HUB",
    "01_Semester_1",
    "02_Semester_2",
    "03_Thesis_&_Research_Transition",
    ".obsidian",
]

# Added only with --all (development side of the vault).
EXTRA_TARGETS = [
    "90_Shared_Toolbox",
    "91_Dashboard",
    "docs",
    "skills",
]

# Always mirrored, never bulky.
ROOT_FILES = ["AGENTS.md", "README.md", "knowledge.md"]

# Excluded at ANY depth. Matched on directory name.
EXCLUDE_DIR_NAMES = {
    # version control / tooling
    ".git", ".svn", ".hg",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    "node_modules", ".venv", "venv", ".tox",
    # sync debris from the Syncthing era
    ".stversions", ".stfolder",
    # agent / browser scratch space
    ".firecrawl", ".freebuff", ".mimocode", ".playwright-cli", ".superpowers",
    ".omp", ".workbuddy-ai",
    # dev-only trees
    "tests", "tmp", "renders_temp", "_pdf_qa", "dummy_dir",
    "_debug_inspect", "_debug_inspect_v2", "_debug_inspect_qa",
    "_workbuddy_inspect", "_workbuddy_inspect_fixed", "_workbuddy_inspect_gate",
}

# Excluded at ANY depth. Matched on file name.
EXCLUDE_FILE_NAMES = {
    "desktop.ini",   # injected into every folder by Google Drive File Stream
    ".DS_Store", "Thumbs.db",
    ".stignore", ".gitignore", ".gitattributes",
}

# Excluded at ANY depth. Matched on suffix.
EXCLUDE_FILE_SUFFIXES = {".pyc", ".pyo"}

# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #


def human_bytes(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if abs(n) < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} GB"


def q(path: str) -> str:
    """Quote a path for the *device* shell (we never spawn a local shell)."""
    return shlex.quote(path)


def is_excluded_file(name: str) -> bool:
    if name in EXCLUDE_FILE_NAMES:
        return True
    return Path(name).suffix.lower() in EXCLUDE_FILE_SUFFIXES


def decode(raw: bytes | None) -> str:
    """ADB speaks UTF-8; Windows would otherwise decode with the ANSI code page."""
    if not raw:
        return ""
    return raw.decode("utf-8", errors="replace").replace("\r\n", "\n")


# --------------------------------------------------------------------------- #
# ADB wrapper
# --------------------------------------------------------------------------- #

_PUSH_SUMMARY = re.compile(r"(\d+) files? pushed(?:,\s*(\d+) skipped)?", re.I)
_PUSH_BYTES = re.compile(r"\((\d+) bytes in ([\d.]+)s\)")


class Adb:
    """Thin, shell-free wrapper around the adb binary."""

    def __init__(self, serial: str | None = None, dry: bool = False):
        self.serial = serial
        self.dry = dry

    # -- plumbing ---------------------------------------------------------- #

    def base(self) -> list[str]:
        cmd = ["adb"]
        if self.serial:
            cmd += ["-s", self.serial]
        return cmd

    def run(self, args: list[str], timeout: int | None = 900) -> subprocess.CompletedProcess:
        return subprocess.run(
            self.base() + args,
            capture_output=True,
            timeout=timeout,
            check=False,
        )

    def shell(self, command: str, timeout: int | None = 300) -> subprocess.CompletedProcess:
        return self.run(["shell", command], timeout=timeout)

    def shell_text(self, command: str) -> str:
        return decode(self.shell(command).stdout)

    # -- high level -------------------------------------------------------- #

    def push(self, local: Path | str, remote: str, *, sync: bool = True,
             stats: dict | None = None) -> bool:
        """Push one path. Returns True on success, and accumulates real numbers."""
        args = ["push"]
        if sync:
            args.append("--sync")
        if self.dry:
            args.append("-n")
        args += [str(local), remote]

        res = self.run(args)
        # adb writes the "N files pushed" summary to *stderr*, not stdout.
        out = decode(res.stdout) + decode(res.stderr)
        err = decode(res.stderr)
        ok = res.returncode == 0

        if stats is not None:
            m = _PUSH_SUMMARY.search(out)
            if m:
                stats["files_pushed"] += int(m.group(1))
                stats["files_skipped"] += int(m.group(2) or 0)
            b = _PUSH_BYTES.search(out)
            if b:
                stats["bytes"] += int(b.group(1))
                stats["transfer_seconds"] += float(b.group(2))
            if not ok:
                stats["failures"].append({"path": remote, "error": (err or out).strip()[:400]})
        return ok


def list_devices() -> list[tuple[str, str]] | None:
    """Return [(serial, state)] or None when the adb binary itself is missing."""
    try:
        res = subprocess.run(["adb", "devices", "-l"], capture_output=True, timeout=30, check=False)
    except FileNotFoundError:
        return None
    except Exception:
        return None

    devices: list[tuple[str, str]] = []
    for line in decode(res.stdout).splitlines()[1:]:
        parts = line.split()
        if len(parts) >= 2 and parts[1] in {"device", "offline", "unauthorized", "bootloader"}:
            devices.append((parts[0], parts[1]))
        elif len(parts) >= 2 and parts[1] == "no":
            devices.append((parts[0], "no permissions"))
    return devices


def resolve_device(serial: str | None) -> tuple[str | None, str | None]:
    """Return (serial, error_message)."""
    devices = list_devices()
    if devices is None:
        return None, (
            "adb was not found on PATH.\n"
            "    Install Android Platform Tools (or add C:\\platform-tools to PATH)."
        )

    ready = [(s, st) for s, st in devices if st == "device"]
    blocked = [(s, st) for s, st in devices if st != "device"]

    if serial:
        for s, st in devices:
            if s == serial and st == "device":
                return s, None
        return None, f"Device {serial} is not in a usable state (or not attached)."

    if not devices:
        return None, (
            "No Android device detected.\n"
            "    - Plug the phone in over USB with USB debugging enabled, or\n"
            "    - connect over Wi-Fi first:  adb connect <phone_ip>:5555"
        )
    if len(ready) == 1:
        return ready[0][0], None
    if not ready:
        detail = "\n".join(f"    - {s}: {st}" for s, st in blocked)
        hint = ""
        if any(st == "unauthorized" for _, st in blocked):
            hint = "\n    Accept the 'Allow USB debugging?' prompt on the phone screen."
        return None, "Device attached but not usable:\n" + detail + hint
    listing = "\n".join(f"    - {s}" for s, _ in ready)
    return None, "More than one device is connected - pick one with --serial:\n" + listing


# --------------------------------------------------------------------------- #
# Local plan
# --------------------------------------------------------------------------- #


def compute_polluted(targets: list[str]) -> set[str]:
    """Relative dirs that must not be bulk-pushed because junk lives underneath.

    Only *directory* exclusions trigger a descent: they are the ones that can be
    large (``.git``, ``__pycache__``, ``node_modules``). Small excluded files
    (``desktop.ini``, ``*.pyc``) ride along in the bulk push and are removed by
    the device-side purge, which keeps the number of adb calls low.

    A single vault walk; excluded dirs are never traversed into.
    """
    polluted: set[str] = set()
    for target in targets:
        base = VAULT_ROOT / target
        if not base.is_dir():
            continue
        for dirpath, dirnames, _filenames in os.walk(base):
            hit = any(d in EXCLUDE_DIR_NAMES for d in dirnames)
            dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIR_NAMES]
            if not hit:
                continue
            node = Path(dirpath)
            while True:
                polluted.add(node.relative_to(VAULT_ROOT).as_posix())
                if node == base or node == node.parent:
                    break
                node = node.parent
    return polluted


def local_manifest_sizes(targets: list[str]) -> dict[str, int]:
    """Every file that *should* exist on the phone: {path relative to PHONE_DEST: bytes}."""
    files: dict[str, int] = {}
    for name in ROOT_FILES:
        candidate = VAULT_ROOT / name
        if candidate.is_file():
            files[name] = candidate.stat().st_size
    for target in targets:
        base = VAULT_ROOT / target
        if not base.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIR_NAMES]
            rel_dir = Path(dirpath).relative_to(VAULT_ROOT).as_posix()
            for f in filenames:
                if is_excluded_file(f):
                    continue
                rel = f"{rel_dir}/{f}" if rel_dir != "." else f
                try:
                    files[rel] = (Path(dirpath) / f).stat().st_size
                except OSError:
                    continue
    return files


def local_manifest(targets: list[str]) -> set[str]:
    """Every file that *should* exist on the phone, relative to PHONE_DEST."""
    return set(local_manifest_sizes(targets))


# --------------------------------------------------------------------------- #
# Push
# --------------------------------------------------------------------------- #


def push_tree(adb: Adb, rel_dir: str, remote_dir: str, polluted: set[str],
              stats: dict, full: bool) -> None:
    """Push one directory, descending only where exclusions actually exist."""
    local_dir = VAULT_ROOT / rel_dir
    adb.shell(f"mkdir -p {q(remote_dir)}")

    for child in sorted(local_dir.iterdir(), key=lambda p: p.name):
        rel_child = f"{rel_dir}/{child.name}"
        if child.is_dir():
            if child.name in EXCLUDE_DIR_NAMES:
                stats["excluded_dirs"] += 1
                continue
            if rel_child in polluted:
                push_tree(adb, rel_child, f"{remote_dir}/{child.name}", polluted, stats, full)
            else:
                # "dir/." (a raw string, NOT Path / ".") is what tells adb to copy
                # the *contents* of the directory instead of nesting it inside a
                # same-named folder on the device.
                adb.push(str(child) + "/.", f"{remote_dir}/{child.name}",
                         sync=not full, stats=stats)
        elif child.is_file():
            if is_excluded_file(child.name):
                stats["excluded_files"] += 1
                continue
            adb.push(child, f"{remote_dir}/{child.name}", sync=not full, stats=stats)


# --------------------------------------------------------------------------- #
# Device-side hygiene
# --------------------------------------------------------------------------- #


def purge_device_junk(adb: Adb) -> None:
    """Sweep the device of everything the plan excludes.

    The bulk push cannot filter by itself, so the device is cleaned afterwards.
    The patterns are *derived from the plan's own exclusion sets* rather than a
    hand-written list — a hard-coded list silently diverges, which is how 104
    files under ``.superpowers/`` and friends survived on the phone even though
    the plan had excluded them since v2.
    """
    dir_patterns = sorted(EXCLUDE_DIR_NAMES)
    file_patterns = sorted(EXCLUDE_FILE_NAMES) + [f"*{s}" for s in sorted(EXCLUDE_FILE_SUFFIXES)]
    file_patterns.append("*conflict*")

    dir_expr = " -o ".join(f"-name {q(p)}" for p in dir_patterns)
    base = f"find {q(PHONE_DEST)} -type d \\( {dir_expr} \\) -prune -exec rm -rf {{}}"
    res = adb.shell(base + " +")
    if res is not None and res.returncode != 0:
        # Some older toybox builds reject "-exec ... +"; fall back to per-entry.
        adb.shell(base + " \\;")

    for pattern in file_patterns:
        adb.shell(f"find {q(PHONE_DEST)} -type f -name {q(pattern)} -delete")


def remote_manifest(adb: Adb) -> dict[str, int | None] | None:
    """{relative path: bytes} for every file on the phone, in ONE adb call.

    A size of ``None`` means the device could not report it (``stat`` missing),
    in which case verification degrades to existence-only rather than silently
    claiming everything matches. ``None`` for the whole result means the listing
    itself failed.
    """
    out = adb.shell_text(
        f"cd {q(PHONE_DEST)} && find . -type f -exec stat -c '%s|%n' {{}} +"
    )
    files: dict[str, int | None] = {}
    for line in out.splitlines():
        line = line.strip()
        if "|" not in line:
            continue
        size, _, name = line.partition("|")
        if name.startswith("./"):
            name = name[2:]
        if not size.isdigit() or not name or name.startswith("-"):
            continue
        files[name] = int(size)
    if files:
        return files

    # No sizes available (old toybox): fall back to a plain listing.
    res = adb.shell(f"cd {q(PHONE_DEST)} && find . -type f")
    names: dict[str, int | None] = {}
    for line in decode(res.stdout).splitlines():
        line = line.strip()
        if line.startswith("./"):
            line = line[2:]
        if line and not line.startswith("-"):
            names[line] = None
    if not names and res.returncode != 0:
        return None
    return names


def verify_device(adb: Adb, expected: dict[str, int]) -> tuple[list[str], list[str], list[str], dict[str, int | None] | None]:
    """Compare the device against the vault: (missing, size_mismatch, extra, present).

    Existence alone is not enough. ``adb push --sync`` trusts timestamps, so a
    file whose device copy is *newer but different* is never corrected — the
    phone keeps stale content forever while every run reports success. Measured
    on 2026-10-07: the phone held a 31,188-byte ``AGENTS.md`` against the
    vault's 25,697-byte one, and ``--sync`` skipped it every time.
    """
    present = remote_manifest(adb)
    if present is None:
        return [], [], [], None
    missing = sorted(set(expected) - set(present))
    mismatched = sorted(
        rel for rel, size in expected.items()
        if rel in present and present[rel] is not None and present[rel] != size
    )
    extra = sorted(set(present) - set(expected))
    return missing, mismatched, extra, present


def repair_mismatches(adb: Adb, mismatched: list[str], stats: dict) -> int:
    """Force-push files whose device copy exists but differs.

    Deliberately *without* ``--sync``: the whole point is that the timestamp
    comparison is what let them drift in the first place.
    """
    repaired = 0
    for rel in mismatched:
        local = VAULT_ROOT / rel
        if not local.is_file():
            continue
        if adb.push(local, f"{PHONE_DEST}/{rel}", sync=False, stats=stats):
            repaired += 1
    stats["repaired"] = repaired
    return repaired


def prune_device(adb: Adb, stats: dict, present: dict[str, int | None] | None,
                 expected: set[str], confirm: bool) -> None:
    """Delete phone files that no longer exist in the vault."""
    if present is None:
        present = remote_manifest(adb)
    extras = sorted(set(present or {}) - expected)
    stats["extras"] = extras
    if not extras:
        return

    print(f"[!] {len(extras)} file(s) on the phone are not in the vault:")
    for p in extras[:25]:
        print(f"      - {p}")
    if len(extras) > 25:
        print(f"      ... and {len(extras) - 25} more")

    if not confirm:
        print("[i] Nothing deleted. Re-run with --clean --yes to remove them.")
        return

    deleted = 0
    for i in range(0, len(extras), 50):
        chunk = extras[i:i + 50]
        args = " ".join(q(f"{PHONE_DEST}/{p}") for p in chunk)
        adb.shell(f"rm -f {args}")
        deleted += len(chunk)
    adb.shell(f"find {q(PHONE_DEST)} -mindepth 1 -type d -empty -delete")
    stats["deleted"] = deleted
    print(f"[+] Removed {deleted} stale file(s); the phone is now an exact mirror.")


# --------------------------------------------------------------------------- #
# Phone -> PC
# --------------------------------------------------------------------------- #


def pull_inbox(adb: Adb) -> int:
    """Bring files the phone produced back into the vault."""
    probe = adb.shell(f"[ -d {q(PHONE_INBOX)} ] && echo yes || echo no")
    if "yes" not in decode(probe.stdout):
        print(f"[i] Nothing to pull: {PHONE_INBOX} does not exist on the phone.")
        print("    Create it there (e.g. with a file manager) and drop files in it.")
        return 0

    LOCAL_INBOX.mkdir(parents=True, exist_ok=True)
    res = adb.run(["pull", "-a", f"{PHONE_INBOX}/.", str(LOCAL_INBOX)])
    out = decode(res.stdout) + decode(res.stderr)
    m = re.search(r"(\d+) files? pulled", out)
    count = int(m.group(1)) if m else 0
    if res.returncode != 0:
        print(f"[-] Pull failed: {out.strip()[:300]}")
        return 1
    print(f"[+] Pulled {count} file(s) -> {LOCAL_INBOX}")
    return 0


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="phone_sync.py",
        description="Master Studio - local ADB sync to the phone (offline, incremental).",
    )
    p.add_argument("--all", action="store_true",
                   help="also mirror 90_Shared_Toolbox, 91_Dashboard, docs, skills")
    p.add_argument("--full", action="store_true",
                   help="re-push every file instead of only changed ones")
    p.add_argument("--dry-run", action="store_true",
                   help="report what would change without writing to the phone")
    p.add_argument("--prune", action="store_true",
                   help="list phone files that no longer exist in the vault")
    p.add_argument("--clean", action="store_true",
                   help="like --prune, and delete them (requires --yes)")
    p.add_argument("--yes", action="store_true",
                   help="confirm deletions requested by --clean/--prune")
    p.add_argument("--pull", action="store_true",
                   help=f"pull {PHONE_INBOX} back into {LOCAL_INBOX.name}/")
    p.add_argument("--serial", default=None,
                   help="target a specific device (see: adb devices)")
    p.add_argument("--wifi", default=None, metavar="IP[:PORT]",
                   help="connect over Wi-Fi before syncing")
    p.add_argument("--port", type=int, default=DEFAULT_PORT,
                   help=f"port for the USB reverse tunnel (default {DEFAULT_PORT})")
    p.add_argument("--no-tunnel", action="store_true",
                   help="do not set up the USB reverse tunnel for the dashboard")
    p.add_argument("--no-verify", action="store_true",
                   help="skip the post-push verification pass")
    p.add_argument("--no-repair", action="store_true",
                   help="report files whose device copy drifted, but do not re-push them")
    p.add_argument("--no-junk-purge", action="store_true",
                   help="skip removing sync debris on the phone")
    p.add_argument("--json", action="store_true", help="print a machine-readable summary")
    p.add_argument("--quiet", action="store_true", help="only print the final summary")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    t0 = time.time()

    def say(msg: str = "") -> None:
        if not args.quiet:
            print(msg)

    # --- device ----------------------------------------------------------- #
    if args.wifi:
        target = args.wifi if ":" in args.wifi else f"{args.wifi}:5555"
        say(f"[*] Connecting over Wi-Fi to {target} ...")
        subprocess.run(["adb", "connect", target], capture_output=True, timeout=30, check=False)

    serial, err = resolve_device(args.serial)
    if err:
        print("[-] " + err)
        return 1
    adb = Adb(serial=serial, dry=args.dry_run)

    say("=" * 67)
    say(" Master Studio: Local Phone Sync")
    say("=" * 67)
    say(f"[+] Device: {serial}")
    say(f"[+] Destination: {PHONE_DEST}")
    mode = "FULL re-push" if args.full else "incremental (changed files only)"
    say(f"[+] Mode: {mode}{'  [DRY RUN]' if args.dry_run else ''}")

    # --- tunnel ----------------------------------------------------------- #
    if not args.no_tunnel:
        res = adb.run(["reverse", f"tcp:{args.port}", f"tcp:{args.port}"], timeout=30)
        if res.returncode == 0:
            say(f"[+] Dashboard tunnel active: http://localhost:{args.port} on the phone.")
        else:
            say(f"[i] Reverse tunnel not available ({decode(res.stderr).strip()[:80]}).")

    # --- plan ------------------------------------------------------------- #
    targets = list(CORE_TARGETS) + (list(EXTRA_TARGETS) if args.all else [])
    targets = [t for t in targets if (VAULT_ROOT / t).is_dir()]
    polluted = compute_polluted(targets)
    expected = local_manifest_sizes(targets)
    say(f"[+] Targets: {', '.join(targets)}")
    say(f"[+] Vault files in scope: {len(expected)}")

    if args.dry_run:
        say("[*] Dry run - the device will not be modified.")

    # --- push ------------------------------------------------------------- #
    stats: dict = {
        "files_pushed": 0, "files_skipped": 0, "bytes": 0, "transfer_seconds": 0.0,
        "excluded_dirs": 0, "excluded_files": 0, "failures": [],
        "deleted": 0, "extras": [], "missing": [], "mismatched": [], "repaired": 0,
    }

    adb.shell(f"mkdir -p {q(PHONE_DEST)}")

    say("[*] Pushing top-level documents ...")
    for name in ROOT_FILES:
        f = VAULT_ROOT / name
        if f.is_file():
            adb.push(f, f"{PHONE_DEST}/{name}", sync=not args.full, stats=stats)
        else:
            say(f"[i] {name} not found locally - skipped.")

    say("[*] Pushing study folders ...")
    for target in targets:
        adb.shell(f"mkdir -p {q(PHONE_DEST + '/' + target)}")
        push_tree(adb, target, f"{PHONE_DEST}/{target}", polluted, stats, args.full)

    # --- hygiene ---------------------------------------------------------- #
    if not args.no_junk_purge and not args.dry_run:
        say("[*] Removing sync debris on the device ...")
        purge_device_junk(adb)

    # --- verify ----------------------------------------------------------- #
    present: dict[str, int | None] | None = None
    if not args.no_verify and not args.dry_run:
        say("[*] Verifying the device copy (existence + size) ...")
        missing, mismatched, _extras, present = verify_device(adb, expected)
        stats["missing"] = missing
        stats["mismatched"] = mismatched

        if present is not None and any(v is None for v in present.values()):
            say("[i] This device cannot report file sizes - verification was "
                "existence-only, so drifted content would not be caught.")

        if missing:
            say(f"[!] {len(missing)} file(s) expected on the phone but absent:")
            for p in missing[:15]:
                say(f"      - {p}")
            if len(missing) > 15:
                say(f"      ... and {len(missing) - 15} more")

        if mismatched:
            say(f"[!] {len(mismatched)} file(s) exist on the phone but with different "
                f"content (--sync cannot see these):")
            for p in mismatched[:15]:
                say(f"      - {p}  (vault {expected[p]} B, phone {present.get(p, '?')} B)")
            if len(mismatched) > 15:
                say(f"      ... and {len(mismatched) - 15} more")
            if not args.no_repair:
                say("[*] Force-re-pushing the drifted files ...")
                repaired = repair_mismatches(adb, mismatched, stats)
                say(f"[+] Repaired {repaired}/{len(mismatched)} file(s).")
                present = None  # the device changed; re-read before pruning

    # --- prune ------------------------------------------------------------ #
    if args.prune or args.clean:
        prune_device(adb, stats, present, set(expected), confirm=bool(args.yes))

    # --- pull ------------------------------------------------------------- #
    pull_rc = 0
    if args.pull:
        pull_rc = pull_inbox(adb)

    # --- summary ---------------------------------------------------------- #
    elapsed = time.time() - t0
    rate = stats["bytes"] / stats["transfer_seconds"] if stats["transfer_seconds"] else 0.0
    failed = len(stats["failures"])
    unrepaired = len(stats["mismatched"]) - stats["repaired"]
    problems = failed + len(stats["missing"]) + unrepaired

    if args.json:
        print(json.dumps({
            "device": serial,
            "dry_run": args.dry_run,
            "full": args.full,
            "targets": targets,
            "elapsed_seconds": round(elapsed, 2),
            "files_pushed": stats["files_pushed"],
            "files_skipped": stats["files_skipped"],
            "bytes_transferred": stats["bytes"],
            "excluded_dirs": stats["excluded_dirs"],
            "excluded_files": stats["excluded_files"],
            "missing_on_device": stats["missing"],
            "drifted_on_device": stats["mismatched"],
            "repaired": stats["repaired"],
            "stale_on_device": stats["extras"],
            "deleted": stats["deleted"],
            "failures": stats["failures"],
            "ok": problems == 0 and pull_rc == 0,
        }, indent=2, ensure_ascii=False))
    else:
        print()
        print("=" * 67)
        if problems:
            print(f"[!] SYNC FINISHED WITH {problems} PROBLEM(S) in {elapsed:.1f}s")
        else:
            print(f"[+] SYNC COMPLETE in {elapsed:.1f}s")
        print(f"    pushed {stats['files_pushed']} file(s) "
              f"({human_bytes(stats['bytes'])}, {rate / 1e6:.1f} MB/s)")
        print(f"    skipped {stats['files_skipped']} unchanged file(s)")
        print(f"    excluded {stats['excluded_dirs']} junk dir(s), "
              f"{stats['excluded_files']} junk file(s)")
        if stats["repaired"]:
            print(f"    repaired {stats['repaired']} file(s) that had drifted on the phone")
        if stats["deleted"]:
            print(f"    removed {stats['deleted']} stale file(s) from the device")
        if failed:
            print(f"    {failed} push failure(s):")
            for f in stats["failures"][:5]:
                print(f"      - {f['path']}: {f['error'][:120]}")
        if args.dry_run:
            print("    [DRY RUN] nothing was written to the device")
        print(f"    on the phone: Documents/MasterStudio/")
        print("=" * 67)

    if problems:
        return 1
    return pull_rc


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    sys.exit(main())
