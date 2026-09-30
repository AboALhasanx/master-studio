"""The suite must never write into the production gateway database.

`tg.py` defaults ``--db`` to ``90_Shared_Toolbox/telegram/gateway.db``, which is
the *real* audit log. A test that forgets the flag does not fail — it succeeds,
and appends a row claiming the account did something it never did.

Measured on 2026-10-01 with a fingerprint of the file before and after a full
run: ``rows=113`` became ``rows=114`` and the hash changed, i.e. every single
run left a false ``human:whoami refused`` entry behind. That is silent
corruption of the exact ledger monitoring (issue #22 AC 2) exists to be read —
worse than a red test, because nothing goes red.

So the default is redirected to a throwaway file for the duration of the suite,
and this module proves both that the redirect is in place and that it holds
under the call that was actually doing the damage.
"""

from __future__ import annotations

import hashlib
import sqlite3
import sys
from pathlib import Path

_TOOLBOX = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox"
if str(_TOOLBOX) not in sys.path:
    sys.path.insert(0, str(_TOOLBOX))

from telegram import store  # noqa: E402


def _production_db() -> Path:
    """The file ``--db`` would open if nothing had redirected it."""
    return Path(store.__file__).with_name("gateway.db")


def _fingerprint(path: Path):
    """A row count plus a content hash — cheap, and enough to catch a single
    appended row that a bare ``exists()`` check would miss."""
    if not path.exists():
        return "absent"
    conn = sqlite3.connect(str(path))
    try:
        rows = conn.execute("SELECT COUNT(*) FROM audit").fetchone()[0]
    finally:
        conn.close()
    return rows, hashlib.sha256(path.read_bytes()).hexdigest()


class TestTheSuiteCannotReachTheProductionLog:
    def test_the_default_db_is_redirected_away_from_production(self):
        """The guard itself. Without it ``DEFAULT_DB_PATH`` *is* the live log,
        and every ``--db``-less CLI call in the suite lands in it."""
        assert store.DEFAULT_DB_PATH != _production_db(), (
            "the suite's default --db is still the production audit log"
        )

    def test_a_cli_call_that_forgets_db_leaves_production_untouched(
            self, capsys):
        """The behaviour the guard exists for, exercised rather than assumed:
        run the real CLI with no ``--db`` — the exact omission that was
        producing one false row per run — and show the log does not move."""
        from telegram import cli

        before = _fingerprint(_production_db())
        # deliberately no --db, no --registry: this is the mistake itself
        cli.main(["--json", "--dry-run", "status"])
        capsys.readouterr()

        # a refusal inside `human` is what used to write the false row, so
        # drive that path too rather than the dry-run that writes nothing
        cli.main(["--json", "human", "--verb", "whoami"])
        capsys.readouterr()

        assert _fingerprint(_production_db()) == before, (
            "the suite wrote into the production audit log"
        )
