"""Suite-wide guard: no test may write into the production gateway database.

``tg.py`` defaults ``--db`` to ``90_Shared_Toolbox/telegram/gateway.db`` — the
*live* audit log. A test that forgets the flag does not fail; it succeeds, and
appends a row claiming the account did something it never did. Measured on
2026-10-01 by fingerprinting the file either side of a full run: ``rows=113``
became ``rows=114``, so every single run was leaving a false
``human:whoami refused`` entry in the very ledger that monitoring (issue #22
AC 2) exists to be read.

Redirecting the default to a throwaway file per test costs nothing — tests
that pass ``--db`` explicitly are untouched — and removes the whole class of
silent corruption rather than the one call site that happened to be caught.
Proven by ``tests/test_suite_isolation.py``, which fails if this fixture is
removed or weakened.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_TOOLBOX = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox"
if str(_TOOLBOX) not in sys.path:
    sys.path.insert(0, str(_TOOLBOX))

from telegram import store  # noqa: E402


@pytest.fixture(autouse=True)
def _isolated_gateway_db(tmp_path, monkeypatch):
    """Point the default ``--db`` at a per-test throwaway file.

    ``cli.py`` imports ``Store`` rather than ``DEFAULT_DB_PATH``, and
    ``Store.__init__`` reads the module global on every call, so patching
    here is enough to redirect every CLI invocation in the suite.
    """
    monkeypatch.setattr(store, "DEFAULT_DB_PATH", tmp_path / "gateway.db")
