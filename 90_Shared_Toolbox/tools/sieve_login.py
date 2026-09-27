#!/usr/bin/env python3
"""
Sieve device-code login.

Phase 1 (no args):
    python sieve_login.py
    Prints verification_uri_complete + user_code. YOU open the link yourself,
    confirm the code matches, and click Approve. This tool never opens it.

Phase 2 (used by the background poller once the link was handed to the user):
    python sieve_login.py --resume <device_code> --interval 5

On approval the key is written to the project's gitignored .env file as
SIEVE_API_KEY. The key value is never printed or logged.
"""

import argparse
import sys
import time
from pathlib import Path

import sieve_client as sc

CLIENT_NAME = "Freebuff Buffy (Master Studio)"
ENV_FILE = sc.ENV_FILE


def store_key(api_key: str) -> None:
    """Write SIEVE_API_KEY into the project .env (gitignored), replacing any
    existing entry. The value never reaches stdout/stderr."""
    lines = []
    if ENV_FILE.is_file():
        lines = ENV_FILE.read_text(encoding="utf-8").splitlines()
    out = []
    replaced = False
    for line in lines:
        if line.strip().startswith("SIEVE_API_KEY="):
            out.append(f"SIEVE_API_KEY={api_key}")
            replaced = True
        else:
            out.append(line)
    if not replaced:
        if out and out[-1].strip():
            out.append("")
        out.append("# Sieve scrape API key - server-side only, never commit (.env is gitignored)")
        out.append(f"SIEVE_API_KEY={api_key}")
    tmp = ENV_FILE.with_name(".env.tmp")
    tmp.write_text("\n".join(out) + "\n", encoding="utf-8")
    tmp.replace(ENV_FILE)


def poll(device_code_value: str, interval: int) -> int:
    delay = max(int(interval or 5), 1)
    deadline = time.time() + 600  # codes expire after 10 minutes
    while time.time() < deadline:
        try:
            result = sc.device_token(device_code_value)
        except sc.SieveError as exc:
            print(f"  poll problem, retrying ({type(exc).__name__}): {exc}", flush=True)
            time.sleep(delay)
            continue

        if result.get("ok") and result.get("api_key"):
            store_key(result["api_key"])
            print("APPROVED - SIEVE_API_KEY stored in .env (value not shown).",
                  flush=True)
            return 0

        err = (result.get("error") or "").strip()
        if err == "authorization_pending":
            print("  waiting for approval...", flush=True)
        elif err == "slow_down":
            delay += 5
            print(f"  slow_down: polling every {delay}s", flush=True)
        elif err == "access_denied":
            print("DECLINED - the approval was rejected.", flush=True)
            return 2
        elif err == "expired_token":
            print("EXPIRED - run the login again for a fresh code.", flush=True)
            return 3
        elif err:
            print(f"UNEXPECTED RESPONSE: {err}", flush=True)
            return 4
        time.sleep(delay)
    print("TIMED OUT after 10 minutes without approval.", flush=True)
    return 5


def main() -> int:
    parser = argparse.ArgumentParser(description="Sieve device-code login")
    parser.add_argument("--resume", metavar="DEVICE_CODE",
                        help="poll an already-displayed device code")
    parser.add_argument("--interval", type=int, default=5)
    args = parser.parse_args()

    if args.resume:
        return poll(args.resume, args.interval)

    info = sc.device_code(CLIENT_NAME)
    uri = info.get("verification_uri_complete") or info.get("verification_uri")
    user_code = info.get("user_code")
    print("Open this link yourself, check the code matches, then click Approve:")
    print(f"  {uri}")
    print(f"  code: {user_code}")
    print(f"  (expires in {info.get('expires_in', 600)}s)", flush=True)
    return poll(info.get("device_code"), int(info.get("interval") or args.interval))


if __name__ == "__main__":
    sys.exit(main())
