"""Live verification launcher — the permanent form of playbook §7's gate.

    python 90_Shared_Toolbox/tools/tg_verify.py --live
    python 90_Shared_Toolbox/tools/tg_verify.py --live --subject 05-Soft-Computing
    python 90_Shared_Toolbox/tools/tg_verify.py --live --json

Reads each subject topic as the spare account and checks the catalog contract:
the card is the first content message and is pinned, names the subject and the
doctor, carries the verbatim chapter line and every ordinal, attaches the
merged booklet, its links point at the published chapter files, every chapter
and reference post exists, and no display filename exceeds Telegram's 62-byte
budget. Prints ``ALL CHECKS PASSED`` only when every check passes.

Without ``--live`` it refuses: this capability reads the real group. It is
strictly read-only — it can never change what it inspects.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from telegram.verify import verify_main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(verify_main())
