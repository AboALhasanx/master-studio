#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One place that answers "what Supabase credential do I use?".

Why this exists: `portal_content.py` used to read
`mcp-auth.json -> supabase.tokens.accessToken` directly. That token is an
OAuth access token that lives one hour; when it expired, publishing stopped
with a bare 401 and nothing refreshed it.

The chain, in order:

  1. `SUPABASE_ACCESS_TOKEN` in the environment (CI, one-off runs).
  2. A personal access token (`sbp_...`) in `SUPABASE_PAT_FILE`
     (default `~/.config/opencode/supabase-pat`). Does not expire, is not
     rotated, and cannot be broken by the MCP connector. Preferred for a
     machine that publishes regularly.
  3. The OAuth tokens that `opencode mcp auth supabase` stores in
     `mcp-auth.json`, refreshed here when they are expired and **written back
     immediately** (Supabase rotates the refresh token on every use, so a
     refresh that is not persisted kills the chain).

Every Management API call retries once after a forced refresh on 401, so an
expired token can no longer block a publish silently.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

PROJECT = os.environ.get("SUPABASE_PROJECT", "gywniovuupjmllbmjmai")
API = "https://api.supabase.com/v1"
MCP_AUTH = Path(os.environ.get("MCP_AUTH", str(Path.home() / ".local/share/opencode/mcp-auth.json")))
PAT_FILE = Path(os.environ.get("SUPABASE_PAT_FILE", str(Path.home() / ".config/opencode/supabase-pat")))
SKEW = 120  # refresh this early so a long sync never starts with a token that dies mid-write


class CredentialError(RuntimeError):
    """No usable Supabase credential — the message says how to fix it."""


HELP = """\
No usable Supabase credential. Fix it with ONE of these:

  A. Re-authorise the connector (keeps the MCP tools working too):
         opencode mcp auth supabase
     then re-run the command.

  B. Create a personal access token and store it once (recommended for this
     machine; it does not expire and is never rotated):
         https://supabase.com/dashboard/account/tokens  ->  Generate new token
         echo sbp_xxxxxxxx > "%s"
     (or set SUPABASE_ACCESS_TOKEN / SUPABASE_PAT_FILE instead)
""" % PAT_FILE


# --------------------------------------------------------------------------- #
# small io helpers
# --------------------------------------------------------------------------- #
def _read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise CredentialError("missing %s\n\n%s" % (path, HELP))
    except ValueError as exc:
        raise CredentialError("unreadable %s (%s)\n\n%s" % (path, exc, HELP))


def _write_json_atomic(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def _post_form(url: str, form: dict) -> tuple[int, dict]:
    body = urllib.parse.urlencode(form).encode("utf-8")
    req = urllib.request.Request(
        url, data=body, method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return r.status, json.loads(r.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        try:
            return exc.code, json.loads(raw)
        except ValueError:
            return exc.code, {"message": raw[:300]}
    except urllib.error.URLError as exc:
        return 0, {"message": str(exc.reason)}


def _get(url: str, token: str) -> tuple[int, object]:
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + token, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            raw = r.read().decode("utf-8")
            return r.status, (json.loads(raw) if raw.strip() else None)
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")[:300]
    except urllib.error.URLError as exc:
        return 0, str(exc.reason)


# --------------------------------------------------------------------------- #
# token chain
# --------------------------------------------------------------------------- #
def pat() -> str:
    """An explicit personal access token, or ''."""
    env = (os.environ.get("SUPABASE_ACCESS_TOKEN") or "").strip()
    if env:
        return env
    if PAT_FILE.is_file():
        value = PAT_FILE.read_text(encoding="utf-8").strip()
        if value:
            return value
    return ""


def _refresh_oauth(force: bool = False) -> str:
    data = _read_json(MCP_AUTH)
    sb = data.get("supabase") or {}
    tokens = sb.get("tokens") or {}
    expires = float(tokens.get("expiresAt") or 0)
    if not force and tokens.get("accessToken") and expires - SKEW > time.time():
        return tokens["accessToken"]

    refresh = tokens.get("refreshToken")
    client = sb.get("clientInfo") or {}
    if not refresh:
        raise CredentialError("the stored Supabase OAuth token has no refresh token.\n\n" + HELP)
    if not client.get("clientId") or not client.get("clientSecret"):
        raise CredentialError("the stored Supabase OAuth token has no client credentials.\n\n" + HELP)

    status, out = _post_form(API + "/oauth/token", {
        "grant_type": "refresh_token",
        "refresh_token": refresh,
        "client_id": client["clientId"],
        "client_secret": client["clientSecret"],
    })
    if status != 200 or not isinstance(out, dict) or not out.get("access_token"):
        message = (out or {}).get("message") if isinstance(out, dict) else str(out)
        raise CredentialError(
            "Supabase refused to refresh the OAuth token (HTTP %s: %s). "
            "A refresh token is single-use, so this one is spent.\n\n%s" % (status, message, HELP)
        )

    # persist immediately: losing a rotated refresh token breaks the chain
    tokens["accessToken"] = out["access_token"]
    if out.get("refresh_token"):
        tokens["refreshToken"] = out["refresh_token"]
    tokens["expiresAt"] = time.time() + int(out.get("expires_in") or 3600)
    sb["tokens"] = tokens
    data["supabase"] = sb
    _write_json_atomic(MCP_AUTH, data)
    return tokens["accessToken"]


def access_token(force_refresh: bool = False) -> str:
    token = pat()
    if token:
        return token
    return _refresh_oauth(force=force_refresh)


def service_key(project: str = PROJECT, force_refresh: bool = False) -> str:
    """The service_role key for a project (fetched with the management token)."""
    token = access_token(force_refresh=force_refresh)
    status, keys = _get("%s/projects/%s/api-keys" % (API, project), token)
    if status == 401 and not force_refresh and not pat():
        token = access_token(force_refresh=True)
        status, keys = _get("%s/projects/%s/api-keys" % (API, project), token)
    if status != 200 or not isinstance(keys, list):
        if status == 401:
            raise CredentialError("the credential was rejected (401).\n\n" + HELP)
        raise RuntimeError("could not read the api keys (HTTP %s): %s" % (status, keys))
    for item in keys:
        if item.get("name") in ("service_role", "service_role_key") or item.get("type") == "secret":
            return item["api_key"]
    raise RuntimeError("service_role key not found among %s" % [k.get("name") for k in keys])


def describe() -> str:
    """Human-readable source of the current credential (for logs)."""
    if (os.environ.get("SUPABASE_ACCESS_TOKEN") or "").strip():
        return "env SUPABASE_ACCESS_TOKEN"
    if pat():
        return "PAT %s" % PAT_FILE
    return "OAuth %s" % MCP_AUTH


if __name__ == "__main__":
    print("source:", describe())
    try:
        key = service_key()
        print("service key: %s...%s (%d chars)" % (key[:6], key[-4:], len(key)))
    except CredentialError as exc:
        raise SystemExit(str(exc))
