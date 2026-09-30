"""Tests for the spare human account (issue #22, MTProto via Telethon).

The bot path (``transport.py``) and this path are deliberately different
animals: a user account is a *person*, so Telegram punishes mistakes far more
harshly than it punishes a bot (``FloodWait`` first, account restriction
after). What is therefore under test here is not the network — it is the four
properties that keep the account alive and the vault safe:

1. **Fail closed by default.** Human mode is off until it is switched on, and
   switching it off is the kill switch (#22 AC 2).
2. **Nothing is called before the gates pass.** Every refusal happens before a
   gateway object is touched, so a refused request cannot reach Telegram.
3. **The chat allowlist still applies.** A human account is *not* a bypass of
   the bot's ACL — an empty allowlist denies every chat.
4. **Pacing is enforced locally and FloodWait is never retried.**

A fifth, structural property: ``human`` must stay outside ``schema.VERBS`` so
it can never be composed into the bot's publish path.

Running the suite (the env var is mandatory on this machine):

    CODEBUDDY_SAFE_DELETE_ENABLED=0 \
      "C:/Users/gokoq/AppData/Local/Programs/Python/Python312/python.exe" \
      -m pytest tests/test_telegram_human.py -p no:cacheprovider -q
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

toolbox_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox"
if str(toolbox_path) not in sys.path:
    sys.path.insert(0, str(toolbox_path))

from telegram import human  # noqa: E402
from telegram.errors import (  # noqa: E402
    AccessDenied,
    ActionValidationError,
    GatewayNotReady,
    RateLimited,
)

ALLOWED_CHAT = -1003710711332
OTHER_CHAT = -1009999999999


# ---------------------------------------------------------------------------
# fakes — the gateway is injected, so a refusal can be proven by it never
# being touched rather than by inspecting a network log.
# ---------------------------------------------------------------------------
class FakeGateway:
    """Records every call it receives; optionally raises on a chosen verb."""

    def __init__(self, raise_on: str | None = None, exc: Exception | None = None):
        self.calls: list[tuple] = []
        self.raise_on = raise_on
        self.exc = exc

    def _hit(self, name: str, *args) -> None:
        self.calls.append((name, *args))
        if self.raise_on == name:
            raise self.exc

    def whoami(self) -> dict:
        self._hit("whoami")
        return {"id": 77, "username": "spare_acct", "phone": "+964770******"}

    def dialogs(self) -> list[dict]:
        self._hit("dialogs")
        return [{"id": ALLOWED_CHAT, "title": "Master-Studio FINAL"}]

    def history(self, chat_id: int, limit: int) -> list[dict]:
        self._hit("history", chat_id, limit)
        return [{"id": 1, "text": "hi"}] * min(limit, 1)

    def send(self, chat_id: int, text: str) -> dict:
        self._hit("send", chat_id, text)
        return {"message_id": 4242, "chat_id": chat_id}

    def request_code(self, phone: str) -> dict:
        self._hit("request_code", phone)
        return {"phone": phone, "sent": True}

    def sign_in(self, phone: str, code: str) -> dict:
        self._hit("sign_in", phone, code)
        return {"authorized": True, "user_id": 77}


def request(verb: str, **kw) -> human.HumanRequest:
    return human.HumanRequest(verb=verb, **kw)


def run(req, gateway=None, *, live=True, enabled=True, allowed=(ALLOWED_CHAT,),
        limiter=None):
    """Thin wrapper so each test states only what differs from the default."""
    return human.run(
        req,
        gateway if gateway is not None else FakeGateway(),
        live=live,
        enabled=enabled,
        allowed_chats=frozenset(allowed),
        limiter=limiter,
    )


# ===========================================================================
# 1. Kill switch — fail closed by default (#22 AC 2)
# ===========================================================================
class TestKillSwitch:
    def test_human_mode_is_off_by_default(self, monkeypatch):
        """Absent from the environment must mean *off*, never *on*."""
        monkeypatch.delenv(human.ENV_ENABLED, raising=False)
        assert human.human_enabled() is False

    @pytest.mark.parametrize("value", ["0", "false", "FALSE", "no", "off", "",
                                       "  ", "maybe", "2", "-1", "trueish"])
    def test_only_an_explicit_affirmative_enables(self, monkeypatch, value):
        monkeypatch.setenv(human.ENV_ENABLED, value)
        assert human.human_enabled() is False

    @pytest.mark.parametrize("value", ["1", "true", "TRUE", "yes", "on", " 1 "])
    def test_explicit_affirmative_enables(self, monkeypatch, value):
        monkeypatch.setenv(human.ENV_ENABLED, value)
        assert human.human_enabled() is True

    def test_kill_switch_short_circuits_even_a_malformed_request(self):
        """The switch is checked *first* — that is what makes it a kill switch.

        A disabled account must refuse before validating, before checking
        ``--live`` and above all before touching the gateway.
        """
        gateway = FakeGateway()
        with pytest.raises(GatewayNotReady) as exc:
            run(request("say", chat_id=None), gateway, enabled=False)
        assert exc.value.code == 5
        assert gateway.calls == []

    def test_disabled_mode_reaches_the_gateway_nowhere(self, monkeypatch):
        """Every verb, not just the dangerous one, dies at the switch."""
        gateway = FakeGateway()
        for verb in human.HUMAN_VERBS:
            with pytest.raises(GatewayNotReady):
                run(request(verb, chat_id=ALLOWED_CHAT, text="x"), gateway,
                    enabled=False)
        assert gateway.calls == []

    def test_the_switch_documented_name_is_the_env_var_used(self):
        """The documented kill switch and the code must be the same string."""
        assert human.ENV_ENABLED == "TELEGRAM_HUMAN_ENABLED"


# ===========================================================================
# 2. Every gate runs before the gateway is touched
# ===========================================================================
class TestGatesRunBeforeTheGateway:
    def test_live_is_required(self):
        """Same contract as ``interactive``: a live-only capability (exit 5)."""
        gateway = FakeGateway()
        with pytest.raises(GatewayNotReady) as exc:
            run(request("whoami"), gateway, live=False)
        assert exc.value.code == 5
        assert gateway.calls == []

    def test_unknown_verb_is_rejected(self):
        gateway = FakeGateway()
        with pytest.raises(ActionValidationError):
            run(request("delete", chat_id=ALLOWED_CHAT), gateway)
        assert gateway.calls == []

    def test_say_without_a_chat_is_a_validation_error(self):
        gateway = FakeGateway()
        with pytest.raises(ActionValidationError) as exc:
            run(request("say", text="hello"), gateway)
        assert exc.value.code == 2
        assert gateway.calls == []

    def test_read_without_a_chat_is_a_validation_error(self):
        gateway = FakeGateway()
        with pytest.raises(ActionValidationError):
            run(request("read"), gateway)
        assert gateway.calls == []


# ===========================================================================
# 3. The chat allowlist still applies — a human is not an ACL bypass
# ===========================================================================
class TestChatAllowlist:
    def test_say_outside_the_allowlist_is_denied(self):
        gateway = FakeGateway()
        with pytest.raises(AccessDenied) as exc:
            run(request("say", chat_id=OTHER_CHAT, text="hi"), gateway)
        assert exc.value.code == 3
        assert gateway.calls == []

    def test_read_outside_the_allowlist_is_denied(self):
        gateway = FakeGateway()
        with pytest.raises(AccessDenied):
            run(request("read", chat_id=OTHER_CHAT), gateway)
        assert gateway.calls == []

    def test_empty_allowlist_denies_every_chat(self):
        """Fail closed: a mis-configured deployment must not open a new door."""
        gateway = FakeGateway()
        with pytest.raises(AccessDenied):
            run(request("say", chat_id=ALLOWED_CHAT, text="hi"), gateway,
                allowed=())
        assert gateway.calls == []

    @pytest.mark.parametrize("verb", ["read", "say"])
    def test_an_allowlisted_chat_passes_the_gate(self, verb):
        kwargs = {"chat_id": ALLOWED_CHAT}
        if verb == "say":
            kwargs["text"] = "hello"
        out = run(request(verb, **kwargs))
        assert out["ok"] is True

    @pytest.mark.parametrize("verb", ["whoami", "chats"])
    def test_identity_verbs_need_no_chat_and_no_allowlist(self, verb):
        """``whoami``/``chats`` name no chat, so there is nothing to allow —
        they are gated by the kill switch and ``--live`` alone."""
        out = run(request(verb), allowed=())
        assert out["ok"] is True


# ===========================================================================
# 4. Pacing and FloodWait (#22 AC 2 — never retried, never slept through)
# ===========================================================================
class TestFloodControl:
    def test_local_pacing_blocks_a_burst_before_telegram_is_asked(self):
        from telegram.store import ChatRateLimiter

        limiter = ChatRateLimiter(per_minute=2, min_interval=0.0)
        gateway = FakeGateway()
        now = 1_000.0
        for i in range(2):
            out = human.run(request("say", chat_id=ALLOWED_CHAT, text=str(i)),
                            gateway, live=True, enabled=True,
                            allowed_chats=frozenset({ALLOWED_CHAT}),
                            limiter=limiter, now=now)
            assert out["ok"] is True
        assert len(gateway.calls) == 2

        with pytest.raises(RateLimited) as exc:
            human.run(request("say", chat_id=ALLOWED_CHAT, text="3"), gateway,
                      live=True, enabled=True,
                      allowed_chats=frozenset({ALLOWED_CHAT}),
                      limiter=limiter, now=now)
        # the third send was refused locally — Telegram never saw it
        assert len(gateway.calls) == 2
        assert exc.value.code == 7
        assert exc.value.retry_after > 0

    def test_minimum_interval_is_honoured_between_sends(self):
        from telegram.store import ChatRateLimiter

        limiter = ChatRateLimiter(per_minute=100, min_interval=5.0)
        gateway = FakeGateway()
        human.run(request("say", chat_id=ALLOWED_CHAT, text="a"), gateway,
                  live=True, enabled=True,
                  allowed_chats=frozenset({ALLOWED_CHAT}),
                  limiter=limiter, now=1_000.0)
        with pytest.raises(RateLimited):
            human.run(request("say", chat_id=ALLOWED_CHAT, text="b"), gateway,
                      live=True, enabled=True,
                      allowed_chats=frozenset({ALLOWED_CHAT}),
                      limiter=limiter, now=1_001.0)
        assert len(gateway.calls) == 1

    def test_flood_wait_surfaces_retry_after_and_is_never_retried(self):
        """Telegram says "wait 42s": we report it and stop. We never sleep,
        never loop, and never hide the number from the caller."""
        flood = _flood_wait(42)
        gateway = FakeGateway(raise_on="send", exc=flood)
        with pytest.raises(RateLimited) as exc:
            run(request("say", chat_id=ALLOWED_CHAT, text="hi"), gateway)
        assert exc.value.retry_after == pytest.approx(42.0)
        assert gateway.calls == [("send", ALLOWED_CHAT, "hi")]  # exactly one

    def test_flood_wait_on_a_read_is_typed_the_same_way(self):
        gateway = FakeGateway(raise_on="history", exc=_flood_wait(7))
        with pytest.raises(RateLimited) as exc:
            run(request("read", chat_id=ALLOWED_CHAT), gateway)
        assert exc.value.retry_after == pytest.approx(7.0)
        assert len(gateway.calls) == 1

    def test_an_unrelated_error_is_not_swallowed_into_a_flood(self):
        """Only exceptions carrying Telethon's ``seconds`` become RateLimited;
        everything else propagates untouched instead of being mislabelled."""
        gateway = FakeGateway(raise_on="whoami", exc=ValueError("boom"))
        with pytest.raises(ValueError, match="boom"):
            run(request("whoami"), gateway)

    def test_a_real_send_records_the_stamp_only_on_success(self):
        from telegram.store import ChatRateLimiter

        limiter = ChatRateLimiter(per_minute=1, min_interval=0.0)
        failing = FakeGateway(raise_on="send", exc=ValueError("nope"))
        with pytest.raises(ValueError):
            human.run(request("say", chat_id=ALLOWED_CHAT, text="x"), failing,
                      live=True, enabled=True,
                      allowed_chats=frozenset({ALLOWED_CHAT}),
                      limiter=limiter, now=1_000.0)
        # a failed send must not consume a pacing slot
        healthy = FakeGateway()
        out = human.run(request("say", chat_id=ALLOWED_CHAT, text="x"), healthy,
                        live=True, enabled=True,
                        allowed_chats=frozenset({ALLOWED_CHAT}),
                        limiter=limiter, now=1_000.0)
        assert out["ok"] is True
        assert len(healthy.calls) == 1


# ===========================================================================
# 5. Structural separation from the bot's publish path
# ===========================================================================
class TestStructuralSeparation:
    def test_human_is_not_a_schema_verb(self):
        """D15's rule, applied again: what is outside ``VERBS`` cannot be
        composed into a publish path — ``human`` never becomes an Action."""
        from telegram.schema import VERBS

        assert "human" not in VERBS

    def test_human_is_a_cli_subcommand(self):
        import telegram.cli as cli

        subcommands = cli.build_parser()._subparsers._group_actions[0].choices
        assert "human" in subcommands

    def test_human_dispatches_before_action_parsing(self):
        """``main`` must branch on ``human`` before ``_action_from_args`` runs,
        exactly as it already does for ``interactive``."""
        import telegram.cli as cli

        def explode(*a, **k):  # pragma: no cover - the assertion is the point
            raise AssertionError("_action_from_args must not run for `human`")

        original = cli._action_from_args
        cli._action_from_args = explode
        try:
            code = cli.main(["human", "--verb", "whoami"])  # no --live -> exit 5
        finally:
            cli._action_from_args = original
        assert code == 5

    def test_human_verbs_are_a_fixed_known_set(self):
        assert set(human.HUMAN_VERBS) == {"whoami", "chats", "read", "say", "login"}
        assert human.CHAT_VERBS == frozenset({"read", "say"})


# ===========================================================================
# 6. Session safety — a *.session file is a bearer token
# ===========================================================================
class TestSessionSafety:
    def test_session_files_are_gitignored(self):
        """A Telethon ``*.session`` holds the ``auth_key``: full account
        control, no password, no 2FA — and this repository is public."""
        root = Path(__file__).resolve().parent.parent
        rules = (root / ".gitignore").read_text(encoding="utf-8").splitlines()
        assert any(r.strip() == "*.session" for r in rules), \
            "*.session is not ignored — a committed session = a stolen account"
        assert any(r.strip() == "*.session-journal" for r in rules)
        # the login hand-off carries the spare number; it must not outlive the
        # login attempt in tracked space either
        ignored = human.LOGIN_STATE.name
        assert any(ignored in r for r in rules), \
            f"{ignored} is not ignored — it would leak the spare phone number"

    def test_the_default_session_path_carries_the_session_suffix(self):
        assert human.default_session_path().suffix == ".session"

    def test_credentials_are_read_from_env_not_hardcoded(self):
        assert human.ENV_API_ID == "TELEGRAM_API_ID"
        assert human.ENV_API_HASH == "TELEGRAM_API_HASH"
        source = (toolbox_path / "telegram" / "human.py").read_text(encoding="utf-8")
        assert "20702076" not in source, "api_id leaked into source"
        assert "32f75541cc320b7fe8f5b7de205f423d" not in source, \
            "api_hash leaked into source"


# ===========================================================================
# 7. Documentation linkage (#22 AC 2 must be reachable from the skill)
# ===========================================================================
class TestDocumentationLinkage:
    @staticmethod
    def _skill_text() -> str:
        root = Path(__file__).resolve().parent.parent
        return (root / "skills" / "telegram" / "SKILL.md").read_text(
            encoding="utf-8")

    def test_every_human_flag_is_documented(self):
        import telegram.cli as cli

        subcommands = cli.build_parser()._subparsers._group_actions[0].choices
        flags = {
            opt
            for action in subcommands["human"]._actions
            for opt in action.option_strings
        } - {"-h", "--help"}
        text = self._skill_text()
        undocumented = sorted(f for f in flags if f not in text)
        assert undocumented == [], f"human flags absent from SKILL.md: {undocumented}"

    def test_ac2_controls_are_documented(self):
        """AC 2 asks for flood control, monitoring and a kill switch to be
        *documented* as well as tested — all three must be findable."""
        text = self._skill_text()
        assert human.ENV_ENABLED in text, "the kill switch is undocumented"
        assert "FloodWait" in text, "flood-control policy is undocumented"
        assert "*.session" in text, "the session-file rule is undocumented"


# ===========================================================================
# 8. The Telethon adapter — where a wrong default costs the account
# ===========================================================================
class FakeTelethonClient:
    """Stands in for ``TelegramClient`` so the adapter's *construction* and
    its connect/disconnect discipline can be asserted without a network."""

    instances: list = []

    def __init__(self, session, api_id, api_hash, **kwargs):
        self.session, self.api_id, self.api_hash = session, api_id, api_hash
        self.kwargs = kwargs
        self.connected = False
        self.disconnected = False
        self.sent_codes: list[str] = []
        self.sent_messages: list[tuple] = []
        FakeTelethonClient.instances.append(self)

    # class-level on purpose: a subclass must be able to flip authorization
    # without __init__ shadowing it with an instance attribute.
    authorized = True

    # --- lifecycle -------------------------------------------------------
    async def connect(self):
        self.connected = True

    def disconnect(self):
        self.disconnected = True

    async def is_user_authorized(self):
        return self.authorized

    # --- data ------------------------------------------------------------
    async def get_me(self):
        class _Me:
            id = 77
            username = "spare_acct"
            phone = "9647701234567"
            first_name = "Spare"
            last_name = ""
        return _Me()

    async def get_dialogs(self, limit=None):
        # real Telethon: `await client.get_dialogs()` -> TotalList
        class _D:
            id = ALLOWED_CHAT
            name = "Master-Studio FINAL"
        return [_D()]

    async def get_messages(self, entity, limit=None):
        # real Telethon: `await client.get_messages(...)` -> TotalList
        class _M:
            id = 11
            message = "مرحبا"
            sender_id = 77
        return [_M() for _ in range(int(limit or 1))]

    async def send_message(self, entity, message="", **kw):
        self.sent_messages.append((entity, message))
        class _Msg:
            id = 4242
        return _Msg()

    # --- login -----------------------------------------------------------
    async def send_code_request(self, phone, **kw):
        self.sent_codes.append(phone)
        class _Sent:
            phone_code_hash = "hash-for-" + phone
        return _Sent()

    async def sign_in(self, phone=None, code=None, phone_code_hash=None, **kw):
        self.signed_in_with = {"phone": phone, "code": code,
                               "phone_code_hash": phone_code_hash}
        return await self.get_me()


class TestTelethonGatewayAdapter:
    """The adapter is thin, but two of Telethon's *defaults* are actively
    dangerous for a human account and must be overridden on construction."""

    @staticmethod
    def _gateway(monkeypatch, tmp_path=None, **env):
        FakeTelethonClient.instances.clear()
        monkeypatch.setattr(human, "TelegramClient", FakeTelethonClient)
        monkeypatch.setenv(human.ENV_API_ID, env.get("api_id", "20702076"))
        monkeypatch.setenv(human.ENV_API_HASH, env.get("api_hash", "deadbeef" * 8))
        kwargs = {}
        if tmp_path is not None:
            # never let a test write the real gateway memory folder
            kwargs["login_state"] = tmp_path / "login_state.json"
        return human.TelethonGateway.from_env(**kwargs)

    def test_telethon_never_sleeps_through_a_flood_wait(self, monkeypatch):
        """Telethon's default ``flood_sleep_threshold=60`` makes it **silently
        block for up to a minute** inside our own call. For an account whose
        ban risk is the whole point of AC 2, that must be off — every
        FloodWait has to surface as a reported ``retry_after``."""
        gw = self._gateway(monkeypatch)
        gw.whoami()
        client = FakeTelethonClient.instances[0]
        assert client.kwargs.get("flood_sleep_threshold") == 0, \
            "Telethon would silently sleep on FloodWait"

    def test_no_update_listener_is_ever_installed(self, monkeypatch):
        """D15 forbids a persistent listener; the human path must not quietly
        reintroduce one through Telethon's update machinery."""
        gw = self._gateway(monkeypatch)
        gw.whoami()
        client = FakeTelethonClient.instances[0]
        assert client.kwargs.get("receive_updates") is False

    def test_the_session_file_carries_the_ignored_suffix(self, monkeypatch):
        gw = self._gateway(monkeypatch)
        gw.whoami()
        client = FakeTelethonClient.instances[0]
        assert str(client.session).endswith(".session")

    def test_credentials_come_from_the_environment(self, monkeypatch):
        gw = self._gateway(monkeypatch, api_id="1234567")
        gw.whoami()
        client = FakeTelethonClient.instances[0]
        assert client.api_id == 1234567
        assert client.api_hash == "deadbeef" * 8

    def test_every_call_connects_and_closes_the_session(self, monkeypatch):
        """One CLI invocation = one event loop = one connect/disconnect pair.
        The loop dies with the call, so nothing can leak between verbs."""
        gw = self._gateway(monkeypatch)
        gw.whoami()
        client = FakeTelethonClient.instances[0]
        assert client.connected is True
        assert client.disconnected is True

    def test_an_unauthorized_session_is_reported_not_silently_used(
            self, monkeypatch):
        from telegram.errors import GatewayNotReady

        gw = self._gateway(monkeypatch)
        FakeTelethonClient.instances.clear()

        class Unauthorized(FakeTelethonClient):
            authorized = False
        monkeypatch.setattr(human, "TelegramClient", Unauthorized)

        with pytest.raises(GatewayNotReady) as exc:
            gw.whoami()
        assert exc.value.code == 5
        assert "login" in str(exc.value)

    def test_whoami_masks_the_phone_number(self, monkeypatch):
        """Output lands in the terminal and, later, in journals — the full
        number must never appear in either."""
        gw = self._gateway(monkeypatch)
        me = gw.whoami()
        assert "1234567" not in me["phone"], "the spare number was printed"
        assert "*" in me["phone"]
        assert me["username"] == "spare_acct"

    def test_say_and_read_pass_the_chat_id_straight_through(self, monkeypatch):
        gw = self._gateway(monkeypatch)
        gw.send(ALLOWED_CHAT, "hello")
        gw.history(ALLOWED_CHAT, 5)
        client = FakeTelethonClient.instances[0]
        assert client.sent_messages == [(ALLOWED_CHAT, "hello")]

    def test_login_requests_a_code_before_signing_in(self, monkeypatch, tmp_path):
        gw = self._gateway(monkeypatch, tmp_path)
        out = gw.request_code("+9647700000000")
        assert out["sent"] is True
        client = FakeTelethonClient.instances[0]
        assert client.sent_codes == ["+9647700000000"]

    def test_phone_code_hash_survives_between_two_invocations(
            self, monkeypatch, tmp_path):
        """Telethon keeps ``_phone_code_hash`` **in memory only** — it is
        never written to the session file. So ``login --phone`` (which sends
        the code) and ``login --phone --code`` (which consumes it) run as two
        separate processes, and without an explicit hand-off the second one
        cannot possibly sign in. The hash is therefore carried in the
        gateway's own memory folder and dropped once used."""
        gw = self._gateway(monkeypatch, tmp_path)
        gw.request_code("+9647700000000")
        state_file = tmp_path / "login_state.json"
        assert state_file.exists(), "the code hash was never handed off"
        assert not state_file.with_suffix(".committed").exists()

        state = json.loads(state_file.read_text(encoding="utf-8"))
        assert state["phone"] == "+9647700000000"
        assert state["phone_code_hash"] == "hash-for-+9647700000000"

        FakeTelethonClient.instances.clear()
        out = gw.sign_in("+9647700000000", "12345")
        assert out["authorized"] is True
        client = FakeTelethonClient.instances[0]
        assert client.signed_in_with["phone_code_hash"] == \
            "hash-for-+9647700000000"

        # a one-time credential must not outlive its single use
        assert not state_file.exists(), "the code hash was left on disk"

    def test_sign_in_without_a_prior_request_is_refused(
            self, monkeypatch, tmp_path):
        """No hash means no possible sign-in — say so instead of letting
        Telethon raise an opaque error."""
        from telegram.errors import GatewayNotReady

        gw = self._gateway(monkeypatch, tmp_path)
        with pytest.raises(GatewayNotReady) as exc:
            gw.sign_in("+9647700000000", "12345")
        assert "login --phone" in str(exc.value)

    def test_sign_in_authorizes_the_session(self, monkeypatch, tmp_path):
        gw = self._gateway(monkeypatch, tmp_path)
        gw.request_code("+9647700000000")
        out = gw.sign_in("+9647700000000", "12345")
        assert out["authorized"] is True

    def test_a_wrong_phone_never_writes_a_handoff(self, monkeypatch, tmp_path):
        """If Telegram rejects the number, no state file may be created —
        a stale hash would otherwise block the retry."""
        gw = self._gateway(monkeypatch, tmp_path)

        class BadPhone(FakeTelethonClient):
            async def send_code_request(self, phone, **kw):
                raise ValueError("phone invalid")
        monkeypatch.setattr(human, "TelegramClient", BadPhone)

        with pytest.raises(ValueError):
            gw.request_code("+964700")
        assert not (tmp_path / "login_state.json").exists()


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def _flood_wait(seconds: int):
    """Build a real Telethon FloodWait so the conversion is tested against
    the actual exception shape rather than a stand-in."""
    from telethon.errors import FloodWaitError

    exc = FloodWaitError(None, capture=seconds)
    assert exc.seconds == seconds, "Telethon's FloodWaitError exposes .seconds"
    return exc
