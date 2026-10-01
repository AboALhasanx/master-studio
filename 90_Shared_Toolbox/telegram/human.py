"""The spare human account (issue #22) — MTProto via Telethon.

Why this module is separate from ``transport.py``
------------------------------------------------
``transport.py`` speaks the **Bot API** and is the workhorse: every structured
operation in the vault goes through it. This module speaks **MTProto** as a
*person*, which is a categorically different risk profile — Telegram tolerates
a misbehaving bot with a ``FloodWait`` but restricts a misbehaving *user*
account. Two consequences shape everything below:

* **The gates run before anything is called.** :func:`authorize` is pure and
  touches no network, so a refused request provably never reaches Telegram.
* **Telethon's own defaults are overridden.** ``flood_sleep_threshold``
  defaults to ``60``, which would make Telethon *silently block* inside our
  call instead of reporting the wait; ``receive_updates`` defaults to
  ``True``, which would quietly install the update listener ADR D15 forbids.

Safety properties (each is a test in ``tests/test_telegram_human.py``)
---------------------------------------------------------------------
1. **Fail closed by default.** Human mode is off until ``TELEGRAM_HUMAN_ENABLED``
   says otherwise, and setting it back to ``0`` is the kill switch.
2. **The chat allowlist still applies.** A human account is not an ACL bypass:
   an empty allowlist denies every chat, exactly as it does for the bot.
3. **FloodWait is reported, never slept through and never retried.**
4. **A ``*.session`` file is a bearer token** — it grants full control of the
   account with no password and no 2FA — so it is gitignored before one exists.

Usage (the CLI entry point is ``tg.py human``; see ``skills/telegram/SKILL.md``)
"""

from __future__ import annotations

import asyncio
import json
import os
import time
from dataclasses import dataclass
from pathlib import Path

from .errors import (
    AccessDenied,
    ActionValidationError,
    GatewayError,
    GatewayNotReady,
    RateLimited,
    TransportError,
)
from .store import ChatRateLimiter

# Telethon is imported on first *use*, not on ``import telegram.human``: the
# CLI parser needs ``HUMAN_VERBS`` at build time, and pulling ~a dozen Telethon
# modules into every ``tg.py status`` / dashboard / quiz call would tax the
# whole vault for one capability. Tests replace this name directly.
TelegramClient = None

__all__ = [
    "CHAT_VERBS",
    "ENV_API_HASH",
    "ENV_API_ID",
    "ENV_ENABLED",
    "ENV_SESSION",
    "HUMAN_VERBS",
    "HumanRequest",
    "TelethonGateway",
    "authorize",
    "default_session_path",
    "human_enabled",
    "run",
]

# --- environment -----------------------------------------------------------
ENV_ENABLED = "TELEGRAM_HUMAN_ENABLED"
ENV_API_ID = "TELEGRAM_API_ID"
ENV_API_HASH = "TELEGRAM_API_HASH"
ENV_SESSION = "TELEGRAM_HUMAN_SESSION"

#: Values that switch human mode on. Everything else — including an absent
#: variable, ``0``, ``false`` and any typo — keeps the kill switch engaged.
TRUTHY = frozenset({"1", "true", "yes", "on"})

#: The complete verb set. Deliberately disjoint from ``schema.VERBS``: what
#: lives outside ``VERBS`` can never be composed into the bot's publish path.
HUMAN_VERBS = ("whoami", "chats", "read", "say", "login")

#: Verbs that name a chat, and therefore require that chat to be allowlisted.
CHAT_VERBS = frozenset({"read", "say"})

#: Verbs that actually put something into a chat, and therefore spend the
#: send budget. ``read`` gates on the allowlist too, but must never consume
#: slots — otherwise reading a group could silence it.
SEND_VERBS = frozenset({"say"})

_VAULT_ROOT = Path(__file__).resolve().parents[2]
#: D14: the gateway owns ``00_STUDIO_HUB/telegram/`` and may write only there.
MEMORY_DIR = _VAULT_ROOT / "00_STUDIO_HUB" / "telegram"
#: Single-use hand-off for the login code hash (see ``TelethonGateway``).
LOGIN_STATE = MEMORY_DIR / "login_state.json"
#: Per-chat send stamps. The limiter is rebuilt on every invocation, so the
#: ceiling only means something if the ledger outlives the process.
PACING_STATE = MEMORY_DIR / "pacing.json"


# ---------------------------------------------------------------------------
# configuration
# ---------------------------------------------------------------------------
def human_enabled(raw: str | None = None) -> bool:
    """True only for an explicit affirmative.

    Deliberately strict: an unset variable, ``0``, ``false``, ``yes`` written
    by mistake or any unknown token all mean **off**. A kill switch that can
    be turned on by a typo is not a kill switch.
    """
    if raw is None:
        raw = os.environ.get(ENV_ENABLED, "")
    return str(raw).strip().lower() in TRUTHY


def default_session_path() -> Path:
    """Where Telethon keeps the authorization key — always ``*.session``.

    The suffix matters: ``.gitignore`` ignores ``*.session`` because the file
    *is* the account.
    """
    raw = os.environ.get(ENV_SESSION, "").strip()
    base = Path(raw) if raw else Path(__file__).resolve().parent / "human"
    return base if base.suffix == ".session" else base.with_suffix(".session")


@dataclass(frozen=True)
class HumanRequest:
    """One thing to do with the spare account, validated before any call."""

    verb: str
    chat_id: int | None = None
    text: str | None = None
    limit: int = 10
    phone: str | None = None
    code: str | None = None
    password: str | None = None
    # Forum topic to post into. None = the general topic, which is where a
    # bare announcement belongs; a subject topic is what turns a bare
    # `say` into interaction that lands under the right header.
    thread_id: int | None = None


# ---------------------------------------------------------------------------
# gates — pure, no network, no gateway
# ---------------------------------------------------------------------------
def authorize(req: HumanRequest, *, live: bool, enabled: bool,
              allowed_chats=()) -> None:
    """Raise before a single byte leaves the machine.

    Order is deliberate: the **kill switch is checked first**, so disabling
    human mode short-circuits validation, ``--live`` and the allowlist alike.
    """
    if not enabled:
        raise GatewayNotReady(
            f"human mode is disabled — set {ENV_ENABLED}=1 in .env to enable "
            "it, or leave it unset/0 to keep the kill switch engaged"
        )
    if req.verb not in HUMAN_VERBS:
        raise ActionValidationError(f"unknown human verb: {req.verb!r}")
    if not live:
        raise GatewayNotReady("human mode is a live-only capability (pass --live)")

    if req.verb in CHAT_VERBS:
        if req.chat_id is None:
            raise ActionValidationError(f"verb '{req.verb}' requires --chat")
        allowed = frozenset(int(c) for c in allowed_chats)
        if not allowed:
            raise AccessDenied(
                "no chat allowlist configured — fail closed "
                "(set TELEGRAM_CHAT_ALLOWLIST in .env)"
            )
        if int(req.chat_id) not in allowed:
            raise AccessDenied(
                f"chat {req.chat_id} is not on TELEGRAM_CHAT_ALLOWLIST"
            )
        if req.verb == "read" and int(req.limit) < 1:
            raise ActionValidationError("verb 'read' requires --limit >= 1")
        if req.verb == "say" and not (req.text or "").strip():
            raise ActionValidationError("verb 'say' requires a non-empty --text")

    if req.verb == "login" and not (req.phone or "").strip():
        raise ActionValidationError("verb 'login' requires --phone")

    if req.thread_id is not None:
        # Deliberately outside the CHAT_VERBS block so whoami/chats/login are
        # covered too: a flag that means nothing for the chosen verb must not
        # be dropped quietly, or the operator believes a reply landed in a
        # topic while it went to the general one.
        if req.verb != "say":
            raise ActionValidationError(
                f"--thread only applies to verb 'say' (got {req.verb!r})"
            )
        if int(req.thread_id) < 1:
            raise ActionValidationError("--thread must be a positive topic id")


# ---------------------------------------------------------------------------
# execution — gates first, then exactly one gateway call
# ---------------------------------------------------------------------------
def run(req: HumanRequest, gateway, *, live: bool, enabled: bool,
        allowed_chats=(), limiter: ChatRateLimiter | None = None,
        now: float | None = None,
        persist: Path | str | None = None) -> dict:
    """Authorize, pace, then perform **one** call and summarise it.

    Three properties are load-bearing:

    * a refusal raises before ``gateway`` is touched, so "denied" and "never
      attempted" are the same thing;
    * a successful send records its pacing stamp *after* the fact, so a failed
      attempt never burns a slot the account did not use;
    * ``persist`` makes the ledger outlive the process — the CLI is one verb
      per invocation, so a fresh limiter every time would leave the documented
      ceiling blocking nothing at all (found live on 2026-09-30).
    """
    authorize(req, live=live, enabled=enabled, allowed_chats=allowed_chats)

    paced = limiter if limiter is not None else ChatRateLimiter()
    stamp_now = time.time() if now is None else float(now)
    if persist is not None:
        paced.seed(_read_pacing(Path(persist)))

    if req.verb in SEND_VERBS and not paced.allow(int(req.chat_id), stamp_now):
        retry = float(paced.min_interval)
        if paced.per_minute > 0:
            retry = max(retry, 60.0 / float(paced.per_minute))
        raise RateLimited(
            f"local pacing refused the send: at most {paced.per_minute} "
            f"messages/minute and {paced.min_interval}s apart in one chat "
            "(Telegram was never asked)",
            retry_after=retry,
        )

    call = _dispatch_table(req, gateway)
    try:
        result = call()
    except GatewayError:
        raise
    except Exception as exc:  # Telethon's FloodWaitError carries .seconds
        seconds = getattr(exc, "seconds", None)
        if seconds is None:
            raise
        raise RateLimited(
            f"Telegram flood wait: {seconds}s — reported, never slept through "
            "and never retried",
            retry_after=float(seconds),
        ) from exc

    if req.verb in SEND_VERBS:
        paced.record(int(req.chat_id), stamp_now)
        if persist is not None:
            _write_pacing(Path(persist), paced)
    return {"verb": req.verb, "ok": True, "result": result}


def _dispatch_table(req: HumanRequest, gateway):
    if req.verb == "whoami":
        return lambda: gateway.whoami()
    if req.verb == "chats":
        return lambda: gateway.dialogs()
    if req.verb == "read":
        return lambda: gateway.history(req.chat_id, req.limit)
    if req.verb == "say":
        return lambda: gateway.send(req.chat_id, req.text,
                                    thread_id=req.thread_id)
    if req.verb == "login":
        # password wins: Telethon's sign_in is an if/elif chain (see the
        # adapter), so handing it a code as well would clear nothing.
        if req.password:
            return lambda: gateway.sign_in(req.phone, None,
                                           password=req.password)
        if req.code:
            return lambda: gateway.sign_in(req.phone, req.code)
        return lambda: gateway.request_code(req.phone)
    # unreachable: authorize() rejects anything outside HUMAN_VERBS
    raise ActionValidationError(f"unknown human verb: {req.verb!r}")


# ---------------------------------------------------------------------------
# the Telethon adapter
# ---------------------------------------------------------------------------
def mask_phone(phone) -> str:
    """Hide most of the number.

    Output lands in the terminal and eventually in session journals, so the
    spare number must never appear whole in either.
    """
    text = str(phone or "")
    if len(text) <= 6:
        return "*" * len(text)
    return text[:4] + "*" * max(len(text) - 6, 1) + text[-2:]


def _save_login_state(path: Path, phone: str, code_hash: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"phone": phone, "phone_code_hash": code_hash, "ts": time.time()}
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")


def _load_login_state(path: Path, phone: str) -> str | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if not isinstance(data, dict) or data.get("phone") != phone:
        return None
    return data.get("phone_code_hash") or None


def _drop_login_state(path: Path) -> None:
    try:
        path.unlink()
    except OSError:
        pass


def _read_pacing(path: Path) -> dict:
    """Send stamps recorded by an earlier process, or ``{}``."""
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    if not isinstance(data, dict):
        return {}
    return {
        chat: stamps for chat, stamps in data.items()
        if isinstance(stamps, list)
    }


def _write_pacing(path: Path, limiter: ChatRateLimiter) -> None:
    """Persist the ledger as strings-on-purpose: JSON object keys are
    strings, and the chat ids come back as strings that seed() re-ints."""
    payload = {str(chat): list(ts) for chat, ts in limiter.stamps().items()}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def _client_cls():
    """Resolve ``TelegramClient`` on first use (see the module comment)."""
    global TelegramClient
    if TelegramClient is None:
        from telethon import TelegramClient as _cls  # noqa: PLC0415
        TelegramClient = _cls
    return TelegramClient


class TelethonGateway:
    """Sync facade over Telethon's async client, one event loop per call.

    Each verb builds a client, connects, does exactly one thing and
    disconnects. The loop is created and destroyed with the call, so no
    connection, update handler or ``_phone_code_hash`` can leak between verbs
    — which is also why the login code hash needs an explicit hand-off below.
    """

    def __init__(self, api_id, api_hash, session: Path | str,
                 login_state: Path | str = LOGIN_STATE):
        self.api_id = int(api_id)
        self.api_hash = str(api_hash)
        self.session = Path(session)
        self.login_state = Path(login_state)

    @classmethod
    def from_env(cls, *, login_state: Path | str | None = None) -> "TelethonGateway":
        api_id = os.environ.get(ENV_API_ID, "").strip()
        api_hash = os.environ.get(ENV_API_HASH, "").strip()
        if not api_id or not api_hash:
            raise GatewayNotReady(
                f"human mode needs {ENV_API_ID} and {ENV_API_HASH} set in .env"
            )
        return cls(api_id, api_hash, default_session_path(),
                   login_state=login_state or LOGIN_STATE)

    # -- plumbing ---------------------------------------------------------
    def _call(self, fn):
        async def body():
            # flood_sleep_threshold=0: Telethon's default of 60 would make it
            # silently BLOCK for up to a minute inside this call instead of
            # letting us report retry_after (issue #22 AC 2).
            # receive_updates=False: never installs the listener ADR D15 bans.
            client = _client_cls()(
                str(self.session), self.api_id, self.api_hash,
                flood_sleep_threshold=0,
                receive_updates=False,
            )
            await client.connect()
            try:
                return await fn(client)
            finally:
                client.disconnect()

        return asyncio.run(body())

    @staticmethod
    async def _require(client):
        if not await client.is_user_authorized():
            raise GatewayNotReady(
                "the spare account has no session yet — run "
                "`human --verb login --phone <number>` first"
            )
        return client

    # -- verbs ------------------------------------------------------------
    def whoami(self) -> dict:
        async def body(client):
            await self._require(client)
            return await client.get_me()

        me = self._call(body)
        return {
            "id": me.id,
            "username": getattr(me, "username", None),
            "name": " ".join(x for x in (getattr(me, "first_name", ""),
                                          getattr(me, "last_name", "")) if x),
            "phone": mask_phone(getattr(me, "phone", "")),
        }

    def dialogs(self, limit: int = 50) -> list[dict]:
        async def body(client):
            await self._require(client)
            found = await client.get_dialogs(limit=limit)
            return [
                {"id": d.id, "title": getattr(d, "name", None) or ""}
                for d in found
            ]

        return self._call(body)

    def history(self, chat_id: int, limit: int = 10) -> list[dict]:
        async def body(client):
            await self._require(client)
            found = await client.get_messages(chat_id, limit=int(limit))
            return [
                {
                    "message_id": m.id,
                    "sender_id": getattr(m, "sender_id", None),
                    "text": getattr(m, "message", None) or "",
                }
                for m in found
            ]

        return self._call(body)

    def send(self, chat_id: int, text: str,
             thread_id: int | None = None) -> dict:
        async def body(client):
            await self._require(client)
            # Telethon 1.41 has no `message_thread_id` (that is Bot API); it
            # takes `reply_to`. Replying to a forum topic's root message *is*
            # what places a message inside that topic -- the same wire shape
            # the bot path produces as message_thread_id -- and None keeps
            # the general topic, which is the default anyway.
            sent = await client.send_message(chat_id, text, reply_to=thread_id)
            return {"message_id": sent.id, "chat_id": chat_id}

        return self._call(body)

    # -- login ------------------------------------------------------------
    def request_code(self, phone: str) -> dict:
        """Send the login code and persist the hash it comes with.

        Telethon keeps ``_phone_code_hash`` **in memory only** — it is never
        written to the session file. Since ``login --phone`` and
        ``login --phone --code`` run as two separate processes, the hash has
        to be carried across by hand, and dropped as soon as it is used.
        """
        async def body(client):
            sent = await client.send_code_request(phone)
            return getattr(sent, "phone_code_hash", None)

        code_hash = self._call(body)
        if not code_hash:
            raise TransportError("Telegram returned no phone code hash")
        _save_login_state(self.login_state, phone, code_hash)
        return {"phone": mask_phone(phone), "sent": True}

    def sign_in(self, phone: str, code: str | None = None,
                password: str | None = None) -> dict:
        """Finish the login, either by spending the code or by clearing 2FA.

        Telethon resolves ``sign_in`` as an if/elif chain — *phone and not
        code and not password* → send a code, *elif code* → verify the code,
        *elif password* → check the password. Passing a code **and** a
        password therefore takes the code branch, silently ignores the
        password and re-raises ``SessionPasswordNeededError``. The two modes
        are kept apart on purpose.

        The hand-off is dropped only after success: a mistyped password or a
        refused sign-in must not force a fresh code request.
        """
        if password:
            async def with_password(client):
                return await _guarded(client.sign_in(password=password))

            user = self._call(with_password)
            _drop_login_state(self.login_state)
            return {"authorized": True, "user_id": getattr(user, "id", None)}

        code_hash = _load_login_state(self.login_state, phone)
        if not code_hash:
            raise GatewayNotReady(
                "no pending login for this number — run "
                "`human --verb login --phone <number>` first (the code hash "
                "is single-use and expires in about two minutes)"
            )

        async def with_code(client):
            return await _guarded(
                client.sign_in(phone=phone, code=code,
                               phone_code_hash=code_hash)
            )

        user = self._call(with_code)
        _drop_login_state(self.login_state)
        return {"authorized": True, "user_id": getattr(user, "id", None)}


async def _guarded(coro):
    """Map Telethon's RPC hierarchy onto the gateway's stable exit codes.

    Kept lazy so ``import telegram.human`` never pulls Telethon in. Each
    branch exists because the raw message is otherwise a four-line nest of
    request wrappers that an agent cannot branch on:

    * ``FloodWaitError`` is re-raised untouched — :func:`run` already reads
      its ``seconds`` and turns it into a reported ``retry_after``;
    * ``SessionPasswordNeededError`` becomes an instruction, not a stack;
    * any other ``RPCError`` becomes ``TransportError`` (exit 7).
    """
    from telethon.errors import (  # noqa: PLC0415
        FloodWaitError,
        RPCError,
        SessionPasswordNeededError,
    )

    try:
        return await coro
    except FloodWaitError:
        raise
    except SessionPasswordNeededError as exc:
        raise GatewayNotReady(
            "two-step verification is enabled — the code was accepted; "
            "re-run the same `login` with --password to finish signing in"
        ) from exc
    except RPCError as exc:
        raise TransportError(
            f"Telegram refused: {type(exc).__name__}: {exc}"
        ) from exc
