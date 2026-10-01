"""Catalog-card launcher — the Zero-CLI entry agents invoke to refresh a
subject's pinned card (same shape as ``tg.py``).

    python 90_Shared_Toolbox/tools/tg_catalog.py --list
    python 90_Shared_Toolbox/tools/tg_catalog.py --print 01-Cyber-Security
    python 90_Shared_Toolbox/tools/tg_catalog.py --push 01-Cyber-Security --dry-run
    python 90_Shared_Toolbox/tools/tg_catalog.py --push-all --live

Without ``--live`` a push stays a dry run, so the default never touches the
network. Inserts ``90_Shared_Toolbox`` on ``sys.path`` so the local ``telegram``
package resolves without any PYTHONPATH setup.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from telegram.catalog import catalog_main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(catalog_main())
