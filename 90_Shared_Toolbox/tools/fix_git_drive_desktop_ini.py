#!/usr/bin/env python3
"""
fix_git_drive_desktop_ini.py -- Master Studio maintenance tool.

PROBLEM
-------
When the vault lives on Google Drive File Stream (e.g. drive G:), Drive injects
Windows ``desktop.ini`` files into EVERY folder -- including inside the ``.git/``
directory. A file at ``.git/refs/desktop.ini`` makes git interpret it as a broken
ref and emit:

    fatal: bad object refs/desktop.ini
    error: failed to perform geometric repack

...which breaks ``git fetch``, background maintenance, and the
``origin/<branch>`` remote-tracking ref (``git status`` shows ``[gone]``).

The stray files are pure Windows shell metadata (``[.ShellClassInfo]`` + a
Google Drive icon path) -- they are NOT git data and are safe to delete.

WHAT THIS TOOL DOES
-------------------
1. Deletes every stray ``desktop.ini`` inside the repo's ``.git`` directory.
2. Optionally re-creates the ``origin/<branch>`` tracking ref from the remote
   (``--repair-ref``) so ``git status`` is healthy again.
3. Prints a concise report.

USAGE
-----
    python fix_git_drive_desktop_ini.py                 # clean .git of desktop.ini
    python fix_git_drive_desktop_ini.py --repair-ref    # also fix origin/<branch>
    python fix_git_drive_desktop_ini.py --repo "G:/My Drive/Master-Studio"
    python fix_git_drive_desktop_ini.py --dry-run       # report only, delete nothing
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

DESKTOP_INI = "desktop.ini"


def run_git(repo: Path, *args: str) -> tuple[int, str]:
    """Run a git command inside repo, returning (returncode, stdout+stderr)."""
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=str(repo),
            capture_output=True,
            text=True,
        )
        return proc.returncode, (proc.stdout + proc.stderr).strip()
    except FileNotFoundError:
        return 127, "git executable not found on PATH"


def find_git_dir(repo: Path) -> Path | None:
    """Return the .git directory (handles worktrees / submodules minimally)."""
    git_path = repo / ".git"
    if git_path.is_dir():
        return git_path
    if git_path.is_file():
        # .git file points to the real gitdir (worktree / submodule)
        content = git_path.read_text(encoding="utf-8", errors="ignore").strip()
        if content.lower().startswith("gitdir:"):
            target = Path(content.split(":", 1)[1].strip())
            return target if target.is_dir() else None
    return None


def collect_stray_files(git_dir: Path) -> list[Path]:
    """All files named desktop.ini anywhere under .git."""
    return [p for p in git_dir.rglob("*") if p.is_file() and p.name.lower() == DESKTOP_INI]


def main() -> int:
    parser = argparse.ArgumentParser(description="Remove Google Drive desktop.ini pollution from a git repo.")
    parser.add_argument("--repo", default=None, help="Path to the git repository (default: current dir).")
    parser.add_argument("--repair-ref", action="store_true", help="Re-create the origin/<branch> tracking ref.")
    parser.add_argument("--dry-run", action="store_true", help="Report only; delete nothing.")
    args = parser.parse_args()

    repo = Path(args.repo).resolve() if args.repo else Path.cwd()

    git_dir = find_git_dir(repo)
    if git_dir is None:
        print(f"[X] No git repository found at: {repo}")
        return 1

    print(f"[i] Repository : {repo}")
    print(f"[i] Git dir    : {git_dir}")

    strays = collect_stray_files(git_dir)
    print(f"[i] Stray desktop.ini found inside .git : {len(strays)}")

    if strays and args.dry_run:
        for p in strays[:20]:
            print(f"    (dry-run) would delete: {p.relative_to(git_dir)}")
        if len(strays) > 20:
            print(f"    ... and {len(strays) - 20} more")
    elif strays:
        deleted = 0
        for p in strays:
            try:
                os.remove(p)
                deleted += 1
            except OSError as exc:
                print(f"[!] Could not delete {p}: {exc}")
        print(f"[OK] Deleted {deleted} stray desktop.ini file(s).")

    # -- optional: repair origin/<branch> tracking ref --------------------------
    if args.repair_ref:
        rc, out = run_git(repo, "rev-parse", "--abbrev-ref", "HEAD")
        branch = out if rc == 0 and out else "master"
        rc, remote_head = run_git(repo, "ls-remote", "origin", f"refs/heads/{branch}")
        if rc == 0 and remote_head:
            sha = remote_head.split()[0]
            ref = f"refs/remotes/origin/{branch}"
            run_git(repo, "update-ref", ref, sha)
            (git_dir / "refs" / "remotes" / "origin").mkdir(parents=True, exist_ok=True)
            (git_dir / "refs" / "remotes" / "origin" / branch).write_text(sha + "\n", encoding="utf-8")
            print(f"[OK] Repaired {ref} -> {sha}")
        else:
            print(f"[!] Could not read remote ref for branch '{branch}': {remote_head}")

    # -- final status -----------------------------------------------------------
    rc, status = run_git(repo, "status", "-sb")
    print("[i] git status -sb:")
    for line in status.splitlines():
        print(f"    {line}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
