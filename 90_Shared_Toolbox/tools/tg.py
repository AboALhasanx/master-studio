"""Gateway launcher — the Zero-CLI entry agents invoke (issue #15).

    python 90_Shared_Toolbox/tools/tg.py status
    python 90_Shared_Toolbox/tools/tg.py publish --subject 01-Cyber-Security --text "..." --dry-run

Inserts ``90_Shared_Toolbox`` on ``sys.path`` so the local ``telegram``
package resolves without any PYTHONPATH setup.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from telegram.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
