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

    def send(self, chat_id: int, text: str,
             thread_id: int | None = None) -> dict:
        self._hit("send", chat_id, text, thread_id)
        return {"message_id": 4242, "chat_id": chat_id}

    def send_file(self, chat_id: int, path: str, *, caption=None,
                  filename=None, thread_id=None) -> dict:
        self._hit("send_file", chat_id, path, caption, filename, thread_id)
        return {"message_id": 4343, "chat_id": chat_id}

    def edit_message(self, chat_id: int, message_id: int, text: str) -> dict:
        self._hit("edit_message", chat_id, message_id, text)
        return {"message_id": message_id, "chat_id": chat_id}

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

    def test_thread_only_makes_sense_with_say(self):
        """A silently dropped ``--thread`` would be worse than an error.

        The operator would believe the reply landed inside the topic while it
        went to the general one, and nothing on screen would contradict them.
        So it is refused for every other verb, and a non-positive thread id is
        refused for ``say`` itself.
        """
        gateway = FakeGateway()
        with pytest.raises(ActionValidationError):
            run(request("read", chat_id=ALLOWED_CHAT, thread_id=12), gateway)
        with pytest.raises(ActionValidationError):
            run(request("say", chat_id=ALLOWED_CHAT, text="x",
                        thread_id=0), gateway)
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
        assert gateway.calls == [("send", ALLOWED_CHAT, "hi", None)]  # exactly one

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

    def test_human_dispatches_before_action_parsing(self, tmp_path):
        """``main`` must branch on ``human`` before ``_action_from_args`` runs,
        exactly as it already does for ``interactive``."""
        import telegram.cli as cli

        def explode(*a, **k):  # pragma: no cover - the assertion is the point
            raise AssertionError("_action_from_args must not run for `human`")

        original = cli._action_from_args
        cli._action_from_args = explode
        try:
            # --db on purpose: the default is the production audit log, and
            # this refusal writes a row, so without the flag every run left a
            # false "the account was refused" entry behind
            code = cli.main(["--json", "--db", str(tmp_path / "g.db"),
                             "human", "--verb", "whoami"])  # no --live -> 5
        finally:
            cli._action_from_args = original
        assert code == 5

    def test_human_verbs_are_a_fixed_known_set(self):
        assert set(human.HUMAN_VERBS) == {
            "whoami", "chats", "read", "say", "sendfile", "edit", "login"}
        assert human.CHAT_VERBS == frozenset({"read", "say", "sendfile", "edit"})
        assert human.SEND_VERBS == frozenset({"say", "sendfile"})

    def test_sendfile_needs_an_existing_file(self, tmp_path):
        with pytest.raises(ActionValidationError, match="requires --file"):
            run(request("sendfile", chat_id=ALLOWED_CHAT, text="x"))
        with pytest.raises(ActionValidationError, match="does not exist"):
            run(request("sendfile", chat_id=ALLOWED_CHAT,
                        file=str(tmp_path / "nope.pdf")))

    def test_sendfile_passes_caption_and_display_name(self, tmp_path):
        doc = tmp_path / "dm_ch1.pdf"
        doc.write_bytes(b"%PDF-1.4 test")
        gw = FakeGateway()
        result = run(request("sendfile", chat_id=ALLOWED_CHAT, file=str(doc),
                             text="الفهرس : كتالوج المادة",
                             filename="تنقيب البيانات - الجابتر الاول.pdf",
                             thread_id=86), gateway=gw)
        assert result["ok"] is True
        name, chat, path, caption, filename, thread = gw.calls[0]
        assert name == "send_file"
        assert chat == ALLOWED_CHAT
        assert path == str(doc)
        assert caption == "الفهرس : كتالوج المادة"
        assert filename == "تنقيب البيانات - الجابتر الاول.pdf"
        assert thread == 86

    def test_sendfile_outside_the_allowlist_is_denied(self, tmp_path):
        doc = tmp_path / "x.pdf"
        doc.write_bytes(b"%PDF")
        with pytest.raises(AccessDenied):
            run(request("sendfile", chat_id=-999, file=str(doc)),
                allowed=(ALLOWED_CHAT,))

    def test_sendfile_spends_the_send_budget(self, tmp_path):
        doc = tmp_path / "x.pdf"
        doc.write_bytes(b"%PDF")
        from telegram.store import ChatRateLimiter

        blocked = ChatRateLimiter(per_minute=0)
        with pytest.raises(RateLimited):
            run(request("sendfile", chat_id=ALLOWED_CHAT, file=str(doc)),
                gateway=FakeGateway(), limiter=blocked)


# ===========================================================================
# 5b. `edit` — refreshing a card the spare account owns
# ===========================================================================
class TestEditVerb:
    """The pinned card is the spare account's message, so refreshing it is an
    edit *by the same account* — the only account Telegram lets touch it.

    Before this verb the model had a hole: content moved to the spare
    account, the playbook promised the change went through ``human --verb
    edit``, and no such verb existed — the migration had to reach for a raw
    Telethon script that bypassed the kill switch, the allowlist and the
    audit ledger all at once.
    """

    def test_edit_requires_a_chat(self):
        with pytest.raises(ActionValidationError, match="requires --chat"):
            run(request("edit", message_id=190, text="x"))

    def test_edit_requires_a_message_id(self):
        with pytest.raises(ActionValidationError, match="requires --message-id"):
            run(request("edit", chat_id=ALLOWED_CHAT, text="x"))

    def test_edit_requires_a_non_empty_body(self):
        with pytest.raises(ActionValidationError, match="non-empty --text"):
            run(request("edit", chat_id=ALLOWED_CHAT, message_id=190,
                        text="   "))

    def test_edit_outside_the_allowlist_is_denied(self):
        with pytest.raises(AccessDenied):
            run(request("edit", chat_id=OTHER_CHAT, message_id=190, text="x"))

    def test_edit_rejects_a_thread_flag(self):
        # A message already lives in a topic; there is nothing to re-target,
        # so a `--thread` here means the operator misunderstood the verb.
        with pytest.raises(ActionValidationError, match="--thread"):
            run(request("edit", chat_id=ALLOWED_CHAT, message_id=190,
                        text="x", thread_id=86))

    def test_edit_dispatches_to_the_message_it_names(self):
        gw = FakeGateway()
        result = run(request("edit", chat_id=ALLOWED_CHAT, message_id=190,
                             text="الفهرس المحدّث"), gateway=gw)
        assert result["ok"] is True
        name, chat, mid, text = gw.calls[0]
        assert name == "edit_message"
        assert chat == ALLOWED_CHAT
        assert mid == 190
        assert text == "الفهرس المحدّث"

    def test_edit_does_not_spend_the_send_budget(self):
        """A refresh must never be able to silence a real send: ``edit`` adds
        no new message, so it is deliberately outside ``SEND_VERBS``."""
        from telegram.store import ChatRateLimiter

        blocked = ChatRateLimiter(per_minute=0)
        result = run(request("edit", chat_id=ALLOWED_CHAT, message_id=190,
                             text="x"), gateway=FakeGateway(), limiter=blocked)
        assert result["ok"] is True
        assert "edit" not in human.SEND_VERBS


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
        *documented* as well as tested — all three must be findable. The
        monitoring assertion used to be missing here while the docstring
        claimed it was covered, which is exactly the kind of promise that
        reads as satisfied and is not."""
        text = self._skill_text()
        assert human.ENV_ENABLED in text, "the kill switch is undocumented"
        assert "FloodWait" in text, "flood-control policy is undocumented"
        assert "**Monitoring.**" in text, "the monitoring policy is undocumented"
        assert "human:<verb>" in text, "the audit namespace is undocumented"
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
        self.sent_threads: list[int | None] = []   # message_thread_id per send
        self.edited: list[tuple] = []              # (chat, message_id, text, mode)
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

    async def send_message(self, entity, message="", *, reply_to=None):
        # Mirrors Telethon 1.41's signature **on purpose**: it takes
        # `reply_to`, not Bot API's `message_thread_id`, and the permissive
        # `**kw` this used to have let a bogus kwarg pass every test while six
        # live sends died with TypeError. No `**kw` = the fake refuses what
        # Telethon refuses.
        self.sent_messages.append((entity, message))
        self.sent_threads.append(reply_to)
        class _Msg:
            id = 4242
        return _Msg()

    async def edit_message(self, entity, message_id, text, *, parse_mode=None):
        # Same reason as send_message: no **kw, so a bogus argument fails here
        # instead of on a live card.
        self.edited.append((entity, message_id, text, parse_mode))
        class _Msg:
            id = message_id
        return _Msg()

    # --- login -----------------------------------------------------------
    async def send_code_request(self, phone, **kw):
        self.sent_codes.append(phone)
        class _Sent:
            phone_code_hash = "hash-for-" + phone
        return _Sent()

    async def sign_in(self, phone=None, code=None, phone_code_hash=None,
                      password=None, **kw):
        self.signed_in_with = {"phone": phone, "code": code,
                               "phone_code_hash": phone_code_hash,
                               "password": password}
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

    def test_say_can_target_a_forum_topic(self, monkeypatch):
        """A spare-account message has to be able to land *inside* a topic.

        Without a thread every ``say`` went to ``00-Start-Here``, so "real
        interaction inside the group" was structurally impossible: whatever
        the reply said, it came out under the wrong topic header. Omitting
        the flag must keep the old behaviour (``None``), because the general
        topic is still where an announcement belongs.
        """
        gw = self._gateway(monkeypatch)
        gw.send(ALLOWED_CHAT, "hello")
        gw.send(ALLOWED_CHAT, "سؤال سريع", thread_id=12)
        # _call builds a fresh client per invocation (bounded, no held
        # session), so the two sends land on two different instances.
        threads = [t for c in FakeTelethonClient.instances for t in c.sent_threads]
        assert threads == [None, 12]
        messages = [m for c in FakeTelethonClient.instances for m in c.sent_messages]
        assert messages == [(ALLOWED_CHAT, "hello"), (ALLOWED_CHAT, "سؤال سريع")]

    def test_edit_rewrites_in_place_with_html(self, monkeypatch):
        """An in-place refresh keeps the card's markup: ``send_file`` shipped
        it as HTML, so an edit that dropped ``parse_mode`` would re-render
        the links and bold spans as literal tags on the pinned message."""
        gw = self._gateway(monkeypatch)
        out = gw.edit_message(ALLOWED_CHAT, 190, '<b>الفهرس</b>')
        client = FakeTelethonClient.instances[0]
        assert client.edited == [(ALLOWED_CHAT, 190, '<b>الفهرس</b>', "html")]
        assert out["message_id"] == 190

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


# ===========================================================================
# 9. Two-step verification — Telethon's sign_in is an if/elif chain
# ===========================================================================
class TestTwoStepPassword:
    """`SessionPasswordNeededError` means the code already succeeded and only
    the 2FA password is missing. Telethon resolves sign_in with
    ``if phone-and-not-code-and-not-password / elif code / elif password``,
    so passing **both** silently takes the *code* branch, ignores the password
    and re-raises the very error you were trying to clear."""

    @staticmethod
    def _gw(monkeypatch, tmp_path):
        FakeTelethonClient.instances.clear()
        monkeypatch.setattr(human, "TelegramClient", FakeTelethonClient)
        monkeypatch.setenv(human.ENV_API_ID, "20702076")
        monkeypatch.setenv(human.ENV_API_HASH, "deadbeef" * 8)
        return human.TelethonGateway.from_env(login_state=tmp_path / "s.json")

    def test_a_password_alone_takes_the_password_branch(self, monkeypatch, tmp_path):
        gw = self._gw(monkeypatch, tmp_path)
        gw.request_code("+9647779398151")
        FakeTelethonClient.instances.clear()

        gw.sign_in("+9647779398151", None, password="s3cret")
        seen = FakeTelethonClient.instances[0].signed_in_with
        assert seen["password"] == "s3cret"
        assert seen["code"] is None, \
            "code was passed alongside the password — Telethon would ignore " \
            "the password and re-raise SessionPasswordNeededError"

    def test_the_code_path_still_needs_the_hash(self, monkeypatch, tmp_path):
        gw = self._gw(monkeypatch, tmp_path)
        gw.request_code("+9647779398151")
        FakeTelethonClient.instances.clear()

        gw.sign_in("+9647779398151", "39736")
        seen = FakeTelethonClient.instances[0].signed_in_with
        assert seen["code"] == "39736"
        assert seen["password"] is None
        assert seen["phone_code_hash"] == "hash-for-+9647779398151"

    def test_the_handoff_survives_a_password_challenge(self, monkeypatch, tmp_path):
        """A refused sign-in must not burn the hand-off — otherwise the user
        would have to request a fresh code just to retry a mistyped
        password."""
        state = tmp_path / "s.json"
        gw = self._gw(monkeypatch, tmp_path)
        gw.request_code("+9647779398151")
        assert state.exists()

        class Challenged(FakeTelethonClient):
            async def sign_in(self, **kw):
                raise _session_password_needed()
        monkeypatch.setattr(human, "TelegramClient", Challenged)

        with pytest.raises(GatewayNotReady) as exc:
            gw.sign_in("+9647779398151", "39736")
        assert "password" in str(exc.value)
        assert state.exists(), "the hand-off was dropped by a refusal"

    def test_a_password_challenge_is_an_actionable_not_an_opaque_error(
            self, monkeypatch, tmp_path):
        """The raw message is 4 lines of RPC nesting; the agent must be told
        exactly which flag clears it."""
        gw = self._gw(monkeypatch, tmp_path)
        gw.request_code("+9647779398151")

        class Challenged(FakeTelethonClient):
            async def sign_in(self, **kw):
                raise _session_password_needed()
        monkeypatch.setattr(human, "TelegramClient", Challenged)

        with pytest.raises(GatewayNotReady) as exc:
            gw.sign_in("+9647779398151", "39736", password=None)
        assert exc.value.code == 5
        assert "--password" in str(exc.value)

    def test_a_wrong_password_is_a_transport_error_not_a_traceback(
            self, monkeypatch, tmp_path):
        from telethon.errors import PasswordHashInvalidError
        from telegram.errors import TransportError

        gw = self._gw(monkeypatch, tmp_path)
        gw.request_code("+9647779398151")

        class Wrong(FakeTelethonClient):
            async def sign_in(self, **kw):
                raise PasswordHashInvalidError(None)
        monkeypatch.setattr(human, "TelegramClient", Wrong)

        with pytest.raises(TransportError) as exc:
            gw.sign_in("+9647779398151", None, password="nope")
        assert exc.value.code == 7

    def test_the_request_carries_the_password(self):
        req = human.HumanRequest(verb="login", phone="+9647700000000",
                                 password="pw")
        assert req.password == "pw"

    def test_login_accepts_a_password_without_a_code(self):
        """Ordering: `login --phone --password` must clear the 2FA challenge
        without demanding the code again."""
        authorize_human = human.authorize
        authorize_human(human.HumanRequest(verb="login", phone="+9647700000000",
                                           password="pw"),
                        live=True, enabled=True)

    def test_the_password_flag_is_documented(self):
        text = (Path(__file__).resolve().parent.parent
                / "skills" / "telegram" / "SKILL.md").read_text(encoding="utf-8")
        assert "--password" in text
        assert "two-step" in text.lower() or "2FA" in text


def _session_password_needed():
    from telethon.errors import SessionPasswordNeededError

    return SessionPasswordNeededError(None)


# ===========================================================================
# 10. Pacing must survive a process boundary
# ===========================================================================
class TestPacingPersistsAcrossInvocations:
    """The CLI is one verb per invocation, and each invocation builds a brand
    new ``ChatRateLimiter`` whose stamps live only in memory. So the ceiling
    documented in the skill — 20/minute, 1s apart — blocked *nothing* in real
    use: every call started from an empty ledger. Caught live on 2026-09-30
    when a second send inside the same window went through unchallenged."""

    @staticmethod
    def _limiter():
        from telegram.store import ChatRateLimiter

        return ChatRateLimiter(per_minute=2, min_interval=0.0)

    def _send(self, text, persist):
        """One send with a *fresh* limiter, exactly as a new process would."""
        return human.run(
            request("say", chat_id=ALLOWED_CHAT, text=text),
            FakeGateway(),
            live=True, enabled=True,
            allowed_chats=frozenset({ALLOWED_CHAT}),
            limiter=self._limiter(),
            now=1_000.0,
            persist=persist,
        )

    def test_the_third_send_is_refused_even_in_a_new_process(self, tmp_path):
        persist = tmp_path / "pacing.json"
        assert self._send("a", persist)["ok"] is True
        assert self._send("b", persist)["ok"] is True

        with pytest.raises(RateLimited) as exc:
            self._send("c", persist)
        assert exc.value.code == 7
        assert persist.exists(), "send stamps were never persisted"

    def test_without_persist_the_caller_keeps_full_control(self, tmp_path):
        """Explicit limiter + no persistence behaves exactly as before —
        the seam is opt-in."""
        out = human.run(
            request("say", chat_id=ALLOWED_CHAT, text="a"),
            FakeGateway(),
            live=True, enabled=True,
            allowed_chats=frozenset({ALLOWED_CHAT}),
            limiter=self._limiter(),
            now=1_000.0,
        )
        assert out["ok"] is True

    def test_only_successful_sends_are_persisted(self, tmp_path):
        """A send that Telegram refused must not consume a slot that was
        never used — the ledger has to mirror reality."""
        persist = tmp_path / "pacing.json"
        failing = FakeGateway(raise_on="send", exc=ValueError("nope"))
        with pytest.raises(ValueError):
            human.run(request("say", chat_id=ALLOWED_CHAT, text="x"), failing,
                      live=True, enabled=True,
                      allowed_chats=frozenset({ALLOWED_CHAT}),
                      limiter=self._limiter(), now=1_000.0,
                      persist=persist)
        assert not persist.exists()

    def test_reads_do_not_consume_or_record_pacing_slots(self, tmp_path):
        """``read`` shares the allowlist gate but must not spend the send
        budget — otherwise reading a chat could silence it."""
        persist = tmp_path / "pacing.json"
        for _ in range(3):
            human.run(request("read", chat_id=ALLOWED_CHAT), FakeGateway(),
                      live=True, enabled=True,
                      allowed_chats=frozenset({ALLOWED_CHAT}),
                      limiter=self._limiter(), now=1_000.0,
                      persist=persist)
        out = self._send("a", persist)
        assert out["ok"] is True

    def test_the_pacing_ledger_lives_in_the_gateway_memory_folder(self):
        assert human.PACING_STATE.name == "pacing.json"
        assert human.PACING_STATE.parent == human.MEMORY_DIR

    def test_the_pacing_ledger_is_gitignored(self):
        """Live state, not source: a fresh clone must start with an empty
        ledger, exactly like ``pending_approval.json``."""
        root = Path(__file__).resolve().parent.parent
        rules = (root / ".gitignore").read_text(encoding="utf-8").splitlines()
        assert any(human.PACING_STATE.name in r for r in rules), \
            f"{human.PACING_STATE.name} is not ignored"

    def test_send_stamps_round_trip_through_the_limiter(self):
        """The limiter keeps its stamps private, so persistence needs an
        explicit, tested way in and out."""
        from telegram.store import ChatRateLimiter

        limiter = ChatRateLimiter(per_minute=20, min_interval=1.0)
        assert limiter.stamps() == {}
        limiter.seed({ALLOWED_CHAT: [1_000.0, 1_001.0]})
        assert limiter.stamps()[ALLOWED_CHAT] == [1_000.0, 1_001.0]
        # seeded stamps count against the ceiling: only 0.5s after the last
        # one, the 1s floor has not elapsed yet
        assert limiter.allow(ALLOWED_CHAT, now=1_001.5) is False
        # ...and once it has, the same ledger lets the next send through
        assert limiter.allow(ALLOWED_CHAT, now=1_002.0) is True


# ===========================================================================
# 11. Monitoring — issue #22 AC 2, third leg
# ===========================================================================
class TestHumanMonitoring:
    """AC 2 asks for flood control, a kill switch **and monitoring**, all
    documented and tested. Without an audit row a run leaves nothing but its
    JSON printout, so after the fact nobody can reconstruct what the spare
    account did — which is exactly the observability gap already found in the
    interactive layer."""

    @staticmethod
    def _run(db, monkeypatch, *argv, env=None):
        """Drive the real CLI with a fake Telethon client.

        Every variable the path reads is set **here**, because CI has no
        `.env` at all — a test that leans on the developer's own file is green
        locally and red in the pipeline, which is exactly how these five were
        caught. Defaults are applied first so a test can still override them
        (the kill-switch case passes its own `0`).
        """
        import telegram.cli as cli

        FakeTelethonClient.instances.clear()
        monkeypatch.setattr(human, "TelegramClient", FakeTelethonClient)
        monkeypatch.setenv(human.ENV_ENABLED, "1")
        monkeypatch.setenv("TELEGRAM_CHAT_ALLOWLIST", str(ALLOWED_CHAT))
        monkeypatch.setenv(human.ENV_API_ID, "12345")
        monkeypatch.setenv(human.ENV_API_HASH, "0123456789abcdef")
        monkeypatch.setenv(human.ENV_SESSION, str(db.parent / "human.session"))
        # The pacing ledger must follow the test's own db. `_run_human` reads
        # PACING_STATE at call time, so without this every CLI test spends the
        # *live* chat's sending budget: the second `say` in this file was then
        # refused by a ledger the first one had just filled, and a test run
        # could equally have blocked a real send for up to a minute.
        monkeypatch.setattr(human, "PACING_STATE", db.parent / "pacing.json")
        for key, value in (env or {}).items():
            monkeypatch.setenv(key, value)
        return cli.main(["--json", "--live", "--db", str(db), "human", *argv])

    @staticmethod
    def _rows(db):
        from telegram.store import Store

        return Store(db).audit_rows()

    def test_a_successful_read_leaves_a_row(self, tmp_path, monkeypatch):
        db = tmp_path / "gw.db"
        code = self._run(db, monkeypatch, "--verb", "read",
                         "--chat", str(ALLOWED_CHAT), "--limit", "3")
        assert code == 0
        rows = self._rows(db)
        assert rows, "a successful read left no audit row"
        assert rows[0]["verb"] == "human:read"
        assert rows[0]["result"] == "ok"
        assert rows[0]["chat_id"] == ALLOWED_CHAT

    def test_a_successful_send_is_recorded_as_sent(self, tmp_path, monkeypatch):
        db = tmp_path / "gw.db"
        code = self._run(db, monkeypatch, "--verb", "say",
                         "--chat", str(ALLOWED_CHAT), "--text", "hi")
        assert code == 0
        rows = self._rows(db)
        assert rows[0]["verb"] == "human:say"
        assert rows[0]["result"] == "sent"

    def test_edit_reaches_telethon_from_the_command_line(
            self, tmp_path, monkeypatch):
        """``--message-id 190`` must survive argparse, HumanRequest, run() and
        the adapter — a flag that stops anywhere along the way edits the wrong
        message (or none) while still exiting 0 and writing an audit row."""
        db = tmp_path / "gw.db"
        code = self._run(db, monkeypatch, "--verb", "edit",
                         "--chat", str(ALLOWED_CHAT), "--message-id", "190",
                         "--text", "الفهرس المحدّث")
        assert code == 0
        client = FakeTelethonClient.instances[0]
        assert client.edited[0][1] == 190, "--message-id was dropped en route"
        assert client.edited[0][2] == "الفهرس المحدّث"

    def test_a_successful_edit_is_recorded_with_its_new_body(
            self, tmp_path, monkeypatch):
        """The new caption is the one thing the ledger must never lose:
        Telegram keeps no visible history, so this row is the only record of
        what the card said before the next edit overwrites it."""
        db = tmp_path / "gw.db"
        code = self._run(db, monkeypatch, "--verb", "edit",
                         "--chat", str(ALLOWED_CHAT), "--message-id", "190",
                         "--text", "الفهرس المحدّث")
        assert code == 0
        rows = self._rows(db)
        assert rows[0]["verb"] == "human:edit"
        assert rows[0]["result"] == "ok"       # no new message => not "sent"
        assert rows[0]["chat_id"] == ALLOWED_CHAT
        assert "message_id=190" in (rows[0]["detail"] or "")
        assert "الفهرس المحدّث" in (rows[0]["detail"] or "")

    def test_thread_reaches_telethon_from_the_command_line(
            self, tmp_path, monkeypatch):
        """``--thread 12`` must survive argparse, HumanRequest, run() and the
        adapter — a flag that stops anywhere along the way posts to the wrong
        topic while still exiting 0 and writing a `sent` audit row."""
        live_ledger = human.PACING_STATE          # before _run redirects it
        before = live_ledger.read_bytes() if live_ledger.exists() else None

        db = tmp_path / "gw.db"
        code = self._run(db, monkeypatch, "--verb", "say",
                         "--chat", str(ALLOWED_CHAT), "--text", "hi",
                         "--thread", "12")
        assert code == 0
        client = FakeTelethonClient.instances[0]
        assert client.sent_threads == [12], "--thread was dropped en route"

        after = live_ledger.read_bytes() if live_ledger.exists() else None
        assert after == before, "this CLI test spent the live pacing ledger"

    def test_a_threaded_say_records_where_it_landed(self, tmp_path, monkeypatch):
        """AC 2's monitoring leg: the ledger has to say *where* the spare
        account spoke.

        `_row` passed chat_id and detail but never thread_id, so every
        `human:say` read `thread=None` — including the five that MTProto
        proves landed inside topics 6/8/10/12/14. After the fact nobody
        could tell a topic reply from a general-topic one, and the ledger
        would have contradicted the messages it was describing.
        """
        db = tmp_path / "gw.db"
        code = self._run(db, monkeypatch, "--verb", "say",
                         "--chat", str(ALLOWED_CHAT), "--text", "hi",
                         "--thread", "14")
        assert code == 0
        rows = self._rows(db)
        assert rows[0]["thread_id"] == 14, "the audit row lost the topic"

    def test_a_say_without_a_thread_records_none(self, tmp_path, monkeypatch):
        """...and the general topic must stay distinguishable from it."""
        db = tmp_path / "gw.db"
        code = self._run(db, monkeypatch, "--verb", "say",
                         "--chat", str(ALLOWED_CHAT), "--text", "hi")
        assert code == 0
        rows = self._rows(db)
        assert rows[0]["thread_id"] is None

    def test_a_send_outside_the_allowlist_is_recorded_as_denied(
            self, tmp_path, monkeypatch):
        db = tmp_path / "gw.db"
        code = self._run(db, monkeypatch, "--verb", "say",
                         "--chat", str(OTHER_CHAT), "--text", "hi")
        assert code == 3
        rows = self._rows(db)
        assert rows[0]["verb"] == "human:say"
        assert rows[0]["result"] == "denied"
        assert rows[0]["chat_id"] == OTHER_CHAT
        assert "TELEGRAM_CHAT_ALLOWLIST" in (rows[0]["detail"] or "")

    def test_a_killed_switch_is_recorded_not_silently_dropped(
            self, tmp_path, monkeypatch):
        """The most important row of all: proof that human mode was asked
        for and stopped."""
        db = tmp_path / "gw.db"
        code = self._run(db, monkeypatch, "--verb", "whoami",
                         env={human.ENV_ENABLED: "0"})
        assert code == 5
        rows = self._rows(db)
        assert rows[0]["verb"] == "human:whoami"
        assert rows[0]["result"] == "refused"
        assert human.ENV_ENABLED in (rows[0]["detail"] or "")

    def test_local_pacing_is_recorded_as_rate_limited(
            self, tmp_path, monkeypatch):
        import time as _time

        db = tmp_path / "gw.db"
        ledger = tmp_path / "pacing.json"
        ledger.write_text(json.dumps({str(ALLOWED_CHAT): [_time.time()] * 20}),
                          encoding="utf-8")
        monkeypatch.setattr(human, "PACING_STATE", ledger)

        code = self._run(db, monkeypatch, "--verb", "say",
                         "--chat", str(ALLOWED_CHAT), "--text", "hi")
        assert code == 7
        rows = self._rows(db)
        assert rows[0]["result"] == "rate_limited"

    def test_identity_verbs_are_audited_too(self, tmp_path, monkeypatch):
        db = tmp_path / "gw.db"
        assert self._run(db, monkeypatch, "--verb", "whoami") == 0
        assert self._rows(db)[0]["verb"] == "human:whoami"

    def test_the_row_names_the_human_namespace_not_a_bot_verb(
            self, tmp_path, monkeypatch):
        """``human:*`` must be its own namespace: these actions are taken by
        a person-shaped account and must never be mistaken for the bot's."""
        db = tmp_path / "gw.db"
        self._run(db, monkeypatch, "--verb", "chats")
        verb = self._rows(db)[0]["verb"]
        assert verb.startswith("human:")
        from telegram.schema import VERBS
        assert verb.split(":", 1)[1] not in VERBS


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
