"""Vault file pipeline: resolve -> export if stale -> publish (issue #13).

The Zero-CLI contract is one sentence long: the student asks for a note to be
shared, and the agent runs one command that

1. resolves the source **inside the vault** (refusing anything that escapes
   the root or matches an exclusion pattern — the repo security rule),
2. re-exports it with the exporters we already own (``pdf_exporter.py``) only
   when the artifact is missing or older than the source,
3. hands the resulting binary to the ``publish`` verb, which inherits ACL,
   idempotency, rate limiting and the audit trail for free.

Nothing here talks to Telegram; ``telegram/executor.py`` composes the steps.
"""

from __future__ import annotations

# Bandit B404 (subprocess) is a false positive here: argv is a list, shell stays
# False, the executable is the fixed sys.executable, and every path has already
# passed the containment/exclusion checks in resolve().
import subprocess  # nosec B404
import sys
from pathlib import Path
from typing import Any, Callable

from .errors import PipelineError

__all__ = [
    "VAULT_ROOT",
    "TOOLS_DIR",
    "EXPORT_RULES",
    "EXCLUDED_NAMES",
    "EXCLUDED_SUFFIXES",
    "EXCLUDED_DIRS",
    "resolve",
    "artifact_for",
    "needs_export",
    "run_export",
]

#: Vault root — three levels up from ``90_Shared_Toolbox/telegram/``.
VAULT_ROOT = Path(__file__).resolve().parents[3]

#: Where the exporters live. Derived from *this file*, never from VAULT_ROOT:
#: the toolchain is part of the checkout, the vault is the data it operates on.
TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"

#: source suffix -> (exporter script, extra CLI flags, produced suffix).
EXPORT_RULES: dict[str, tuple[str, list[str], str]] = {
    ".md": ("pdf_exporter.py", ["-t", "study_pack"], ".pdf"),
}

#: Never uploaded: secrets, keystores, build outputs, personal state.
EXCLUDED_NAMES = {".env", ".env.local", ".env.production", ".env.example"}
EXCLUDED_SUFFIXES = {
    ".env", ".apk", ".aab", ".jks", ".keystore", ".p12", ".pfx",
    ".key", ".pem", ".crt", ".db", ".sqlite", ".sqlite3", ".log",
}
EXCLUDED_DIRS = {
    ".git", "__pycache__", ".mimocode", "node_modules", ".venv", "venv",
    ".ssh", "sessions", "extracted",
}


def resolve(source: Any, root: Path | None = None) -> Path:
    """Resolve ``source`` against the vault root, refusing unsafe paths.

    Raises :class:`~telegram.errors.PipelineError` — before any export or
    upload happens — when the path escapes the root, is excluded, or is absent.
    """
    base = (Path(root) if root is not None else Path(VAULT_ROOT)).resolve()
    raw = Path(str(source))
    candidate = (raw if raw.is_absolute() else base / raw).resolve()

    if candidate != base and base not in candidate.parents:
        raise PipelineError(f"path escapes the vault root: {source}")
    if _is_excluded(candidate, base):
        raise PipelineError(f"refusing to publish an excluded path: {source}")
    if not candidate.is_file():
        raise PipelineError(f"source not found: {source}")
    return candidate


def _is_excluded(path: Path, base: Path) -> bool:
    if path.name.startswith(".env") or path.name in EXCLUDED_NAMES:
        return True
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return True
    try:
        rel = path.relative_to(base)
    except ValueError:  # pragma: no cover - resolve() already checked containment
        return False
    return any(part in EXCLUDED_DIRS for part in rel.parts[:-1])


def artifact_for(source: Path) -> Path:
    """Where ``source`` should be published from (source itself if pre-built)."""
    source = Path(source)
    rule = EXPORT_RULES.get(source.suffix.lower())
    if rule is None:
        return source
    return source.with_suffix(rule[2])


def needs_export(source: Path, artifact: Path) -> bool:
    """True when the artifact must be (re)generated: missing or stale."""
    source, artifact = Path(source), Path(artifact)
    if source == artifact:
        return False
    if not artifact.exists():
        return True
    return artifact.stat().st_mtime < source.stat().st_mtime


def run_export(
    source: Path,
    artifact: Path,
    *,
    runner: Callable[..., Any] | None = None,
    timeout: float = 600.0,
) -> Path:
    """Run the exporter that owns ``source`` and return the produced artifact.

    ``runner`` exists so tests can exercise the command line without invoking
    the real exporter (it renders fonts and takes seconds).
    """
    source, artifact = Path(source), Path(artifact)
    rule = EXPORT_RULES.get(source.suffix.lower())
    if rule is None:
        raise PipelineError(f"no exporter rule for {source.suffix!r} sources: {source}")
    script, flags, _ = rule

    cmd = [
        sys.executable,
        str(TOOLS_DIR / script),
        str(source),
        *flags,
    ]

    proc = (runner or subprocess.run)(cmd, capture_output=True, text=True, timeout=timeout)
    code = getattr(proc, "returncode", 0)
    if code != 0:
        stderr = (getattr(proc, "stderr", "") or "").strip().splitlines()
        tail = f": {stderr[-1]}" if stderr else ""
        raise PipelineError(f"exporter failed ({script}, exit {code}){tail}")
    if not artifact.exists():
        raise PipelineError(f"exporter produced no artifact: {artifact}")
    return artifact
