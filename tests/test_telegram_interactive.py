"""Tests for the interactive layer (ADR D15) and gateway memory (ADR D14).

Kept in their own file: the gateway file owns the *outbound* contract
(build_call/execute/transport), while everything here is about the *inbound*
seam and the memory boundary — a different failure surface entirely.

Running the suite (the env var is mandatory on this machine):

    CODEBUDDY_SAFE_DELETE_ENABLED=0 \
      "C:/Users/gokoq/AppData/Local/Programs/Python/Python312/python.exe" \
      -m pytest tests/test_telegram_interactive.py -p no:cacheprovider -q
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

toolbox_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox"
if str(toolbox_path) not in sys.path:
    sys.path.insert(0, str(toolbox_path))

from telegram import telegram_memory as mem  # noqa: E402
from telegram.interactive import (  # noqa: E402
    ADMIN_VERBS,
    Mention,
    SessionLimits,
    build_reply,
    extract_mentions,
    run_session,
)
from telegram.transport import MockTransport  # noqa: E402

BOT = "cs_mscbot"
GROUP = -1003710711332


# --------------------------------------------------------------------- helpers
def _update(uid, text, *, chat=GROUP, actor=42, mid=None, thread=None, entities=None):
    msg = {
        "message_id": mid if mid is not None else uid,
        "chat": {"id": chat},
        "from": {"id": actor},
        "text": text,
    }
    if thread is not None:
        msg["message_thread_id"] = thread
    if entities is not None:
        msg["entities"] = entities
    return {"update_id": uid, "message": msg}


class _Scripted(MockTransport):
    """A MockTransport whose ``getUpdates`` returns a fixed batch once, then []."""

    def __init__(self, batch, *, decline_after=1):
        super().__init__()
        self._batch = list(batch)
        self._decline_after = decline_after
        self._calls = 0

    def call(self, method, params):  # noqa: ANN001
        self.calls.append((method, dict(params)))
        if method == "getUpdates":
            self._calls += 1
            if self._calls <= self._decline_after:
                return self._batch
            return []
        return {"message_id": 9000 + self._calls}


class _Clock:
    """A frozen clock: ``sleep`` advances it, so sessions never really wait."""

    def __init__(self, start=0.0):
        self.t = start

    def now(self):
        return self.t

    def sleep(self, seconds):
        self.t += max(0.0, float(seconds))


# ===================================================================== memory
class TestGatewayMemory:
    """ADR D14 — the gateway owns a memory folder with an explicit contract."""

    def test_memory_root_is_the_studio_hub_telegram_folder(self, monkeypatch, tmp_path):
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", tmp_path / "telegram")
        root = mem.memory_root()
        assert root.exists() and root.name == "telegram"

    def test_state_round_trips_through_the_markdown_json_block(self, monkeypatch, tmp_path):
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", tmp_path / "telegram")
        mem.set_state(update_offset=321, live=True)
        state = mem.read_state()
        assert state["update_offset"] == 321
        assert state["live"] is True

    def test_set_state_merges_rather_than_replaces(self, monkeypatch, tmp_path):
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", tmp_path / "telegram")
        mem.set_state(a=1)
        mem.set_state(b=2)
        state = mem.read_state()
        assert state["a"] == 1 and state["b"] == 2, "a merge must keep earlier keys"

    def test_a_corrupt_state_file_reads_as_empty(self, monkeypatch, tmp_path):
        root = tmp_path / "telegram"
        root.mkdir(parents=True)
        (root / "STATE.md").write_text("garbage without json", encoding="utf-8")
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", root)
        assert mem.read_state() == {}

    def test_a_missing_state_file_reads_as_empty(self, monkeypatch, tmp_path):
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", tmp_path / "absent")
        assert mem.read_state() == {}

    def test_append_log_writes_a_dated_line(self, monkeypatch, tmp_path):
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", tmp_path / "telegram")
        path = mem.append_log("hello world", when="2026-09-30")
        text = path.read_text(encoding="utf-8")
        assert "hello world" in text and path.name == "2026-09-30.md"

    def test_append_log_accumulates(self, monkeypatch, tmp_path):
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", tmp_path / "telegram")
        mem.append_log("first", when="2026-09-30")
        path = mem.append_log("second", when="2026-09-30")
        text = path.read_text(encoding="utf-8")
        assert "first" in text and "second" in text

    def test_record_post_updates_last_post(self, monkeypatch, tmp_path):
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", tmp_path / "telegram")
        mem.record_post("01-Cyber-Security", 55, kind="quiz")
        last = mem.read_state()["last_post"]
        assert last["message_id"] == 55 and last["kind"] == "quiz"

    def test_record_post_error_does_not_advance_last_post(self, monkeypatch, tmp_path):
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", tmp_path / "telegram")
        mem.record_post("01-Cyber-Security", 55, kind="quiz")
        mem.record_post("02-English-Language", None, kind="post", error=True)
        assert mem.read_state()["last_post"]["subject"] == "01-Cyber-Security"

    def test_read_prefs_returns_the_memory_file(self, monkeypatch, tmp_path):
        root = tmp_path / "telegram"
        root.mkdir(parents=True)
        (root / "TELEGRAM_MEMORY.md").write_text("# prefs\n- x", encoding="utf-8")
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", root)
        assert "prefs" in mem.read_prefs()

    def test_read_prefs_missing_file_is_empty(self, monkeypatch, tmp_path):
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", tmp_path / "nope")
        assert mem.read_prefs() == ""

    def test_writes_are_atomic_no_tmp_file_is_left(self, monkeypatch, tmp_path):
        root = tmp_path / "telegram"
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", root)
        mem.set_state(x=1)
        leftovers = list(root.glob("*.tmp*"))
        assert leftovers == [], f"atomic write left temp files: {leftovers}"

    def test_memory_module_never_writes_the_parent_memory(self):
        """D14: the gateway memory module must not open the parent MEMORY.md."""
        import ast

        source = (toolbox_path / "telegram" / "telegram_memory.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        # no string literal anywhere may name the parent memory file as a path
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                assert "00_STUDIO_HUB/" not in node.value or "telegram" in node.value, (
                    f"a literal points at the parent hub: {node.value!r}"
                )
        # and the module must not import the agent's memory helpers
        assert "conversation_search" not in source


# ================================================================ limits/parsing
class TestSessionLimits:
    def test_defaults_are_finite(self):
        limits = SessionLimits()
        assert limits.seconds > 0 and limits.max_messages > 0

    def test_zero_seconds_is_refused(self):
        with pytest.raises(ValueError):
            SessionLimits(seconds=0)

    def test_zero_max_is_refused(self):
        with pytest.raises(ValueError):
            SessionLimits(max_messages=0)


class TestExtractMentions:
    def test_a_mention_in_an_allowed_chat_is_addressed(self):
        addressed, refused, _ = extract_mentions(
            [_update(1, "@cs_mscbot hi")], bot_username=BOT, allowed_chats={GROUP}
        )
        assert len(addressed) == 1 and not refused

    def test_a_mention_from_an_off_allowlist_chat_is_refused(self):
        addressed, refused, _ = extract_mentions(
            [_update(1, "@cs_mscbot hi", chat=-999)], bot_username=BOT, allowed_chats={GROUP}
        )
        assert not addressed and len(refused) == 1

    def test_a_plain_message_is_not_a_mention(self):
        addressed, refused, _ = extract_mentions(
            [_update(1, "hello everyone")], bot_username=BOT, allowed_chats={GROUP}
        )
        assert not addressed and not refused

    def test_a_slash_command_counts_as_addressing_the_bot(self):
        addressed, _, _ = extract_mentions(
            [_update(1, "/help")], bot_username=BOT, allowed_chats={GROUP}
        )
        assert len(addressed) == 1

    def test_min_update_id_filters_already_seen_updates(self):
        addressed, _, highest = extract_mentions(
            [_update(5, "@cs_mscbot a"), _update(9, "@cs_mscbot b")],
            bot_username=BOT, allowed_chats={GROUP}, min_update_id=6,
        )
        assert [m.update_id for m in addressed] == [9]
        assert highest == 9

    def test_highest_update_id_is_tracked_even_when_nothing_matches(self):
        _, _, highest = extract_mentions(
            [_update(77, "no mention here")], bot_username=BOT, allowed_chats={GROUP}
        )
        assert highest == 77

    def test_updates_without_an_integer_id_are_skipped(self):
        addressed, _, _ = extract_mentions(
            [{"update_id": "x", "message": {"text": "@cs_mscbot hi", "chat": {"id": GROUP}}}],
            bot_username=BOT, allowed_chats={GROUP},
        )
        assert not addressed

    def test_a_caption_mention_on_a_media_message_is_seen(self):
        update = {"update_id": 3, "message": {
            "message_id": 3, "chat": {"id": GROUP}, "from": {"id": 42},
            "caption": "@cs_mscbot look at this",
        }}
        addressed, _, _ = extract_mentions([update], bot_username=BOT, allowed_chats={GROUP})
        assert len(addressed) == 1

    def test_chat_and_sender_are_carried_through(self):
        addressed, _, _ = extract_mentions(
            [_update(1, "@cs_mscbot hi", thread=6, actor=7)],
            bot_username=BOT, allowed_chats={GROUP},
        )
        assert addressed[0].actor == 7 and addressed[0].thread_id == 6

    def test_an_empty_chat_allowlist_refuses_everything(self):
        addressed, refused, _ = extract_mentions(
            [_update(1, "@cs_mscbot hi")], bot_username=BOT, allowed_chats=set()
        )
        assert not addressed and len(refused) == 1


# =================================================================== intents
class TestMentionIntents:
    def _mention(self, text, actor=42):
        return Mention(update_id=1, message_id=1, chat_id=GROUP, actor=actor, text=text)

    def test_help_word_replies_with_help(self):
        assert build_reply(self._mention("help"), owner_ids={42})["action"] == "reply"

    def test_help_after_a_mention_is_still_help(self):
        """`@bot help` and `help` must mean the same thing."""
        plan = build_reply(self._mention("@cs_mscbot help"), owner_ids={42})
        assert "أقدر أساعدك" in plan["text"]

    def test_slash_help_is_help_not_an_unknown_command(self):
        plan = build_reply(self._mention("/help"), owner_ids={42})
        assert "ما أعرف" not in plan["text"]

    def test_an_admin_verb_becomes_an_approval_not_an_action(self):
        for verb in sorted(ADMIN_VERBS):
            plan = build_reply(self._mention(f"/{verb} 5"), owner_ids={42})
            assert plan["action"] == "approval", verb

    def test_an_unknown_command_gets_a_pointer_to_help(self):
        plan = build_reply(self._mention("/frobnicate"), owner_ids={42})
        assert plan["action"] == "reply" and "/help" in plan["text"]

    def test_a_bare_mention_gets_a_welcome(self):
        plan = build_reply(self._mention("@cs_mscbot"), owner_ids={42})
        assert plan["action"] == "reply"

    def test_a_subject_hint_steers_the_reply(self):
        plan = build_reply(self._mention("@cs_mscbot اشرح"), owner_ids={42},
                           subject_hint="01-Cyber-Security")
        assert "01-Cyber-Security" in plan["text"]

    def test_owner_and_non_owner_both_still_only_get_approval_for_admin_verbs(self):
        """D16: an admin verb is *never* auto-run, whoever asks."""
        owner = build_reply(self._mention("/delete 1", actor=42), owner_ids={42})
        stranger = build_reply(self._mention("/delete 1", actor=999), owner_ids={42})
        assert owner["action"] == "approval"
        assert stranger["action"] == "approval"

    def test_command_and_args_are_parsed(self):
        m = self._mention("/delete 12 13")
        assert m.command == "delete" and m.args == "12 13"


# =================================================================== session
class TestRunSession:
    def test_no_allowlist_refuses_before_any_call(self):
        transport = _Scripted([_update(1, "@cs_mscbot hi")])
        result = run_session(transport, bot_username=BOT, allowed_chats=None)
        assert result.status == "refused"
        assert transport.calls == [], "a refused session must not call the API at all"

    def test_an_empty_allowlist_also_refuses(self):
        transport = _Scripted([])
        result = run_session(transport, bot_username=BOT, allowed_chats=set())
        assert result.status == "refused" and transport.calls == []

    def test_a_mention_is_answered_once(self, tmp_path):
        clock = _Clock()
        transport = _Scripted([_update(1, "@cs_mscbot help")])
        result = run_session(
            transport, bot_username=BOT, allowed_chats={GROUP},
            limits=SessionLimits(seconds=5, max_messages=5),
            now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json",
        )
        assert result.replied == 1
        assert any(m == "sendMessage" for m, _ in transport.calls)

    def test_the_reply_targets_the_message_and_thread(self, tmp_path):
        clock = _Clock()
        transport = _Scripted([_update(1, "@cs_mscbot help", mid=44, thread=6)])
        run_session(transport, bot_username=BOT, allowed_chats={GROUP},
                    limits=SessionLimits(seconds=5, max_messages=5),
                    now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json")
        sent = [p for m, p in transport.calls if m == "sendMessage"][0]
        assert sent["reply_to_message_id"] == 44
        assert sent["message_thread_id"] == 6

    def test_an_off_allowlist_mention_is_refused_and_audited(self, tmp_path):
        clock = _Clock()
        audited = []

        def _audit(verb, result, **kw):  # noqa: ANN001
            audited.append((verb, result, kw))

        transport = _Scripted([_update(1, "@cs_mscbot hi", chat=-999)])
        result = run_session(
            transport, bot_username=BOT, allowed_chats={GROUP},
            limits=SessionLimits(seconds=5, max_messages=5),
            now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json",
            audit=_audit,
        )
        assert len(result.refused) == 1
        assert audited and audited[0][1] == "denied", audited
        assert not any(m == "sendMessage" for m, _ in transport.calls)

    def test_an_admin_request_is_queued_for_approval_not_executed(self, tmp_path):
        clock = _Clock()
        approval = tmp_path / "pending.json"
        transport = _Scripted([_update(1, "/pin 5", mid=7)])
        result = run_session(
            transport, bot_username=BOT, allowed_chats={GROUP}, owner_ids={42},
            limits=SessionLimits(seconds=5, max_messages=5),
            now=clock.now, sleep=clock.sleep, approval_path=approval,
        )
        assert result.queued_approval == 1
        items = json.loads(approval.read_text(encoding="utf-8"))
        assert items[0]["command"] == "pin" and items[0]["args"] == "5"
        # the bot answers "awaiting approval" but never runs pin itself
        methods = [m for m, _ in transport.calls]
        assert "pinChatMessage" not in methods

    def test_next_offset_advances_past_everything_seen(self, tmp_path):
        clock = _Clock()
        transport = _Scripted([_update(10, "@cs_mscbot a"), _update(11, "no mention")])
        result = run_session(
            transport, bot_username=BOT, allowed_chats={GROUP},
            limits=SessionLimits(seconds=5, max_messages=5), offset=9,
            now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json",
        )
        assert result.next_offset == 11

    def test_the_deadline_ends_the_session(self, tmp_path):
        clock = _Clock()
        transport = _Scripted([], decline_after=0)  # never returns updates
        result = run_session(
            transport, bot_username=BOT, allowed_chats={GROUP},
            limits=SessionLimits(seconds=3, max_messages=50),
            now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json",
        )
        assert result.status == "ok" and clock.t >= 3

    def test_max_messages_caps_the_session(self, tmp_path):
        clock = _Clock()
        batch = [_update(i, "@cs_mscbot help") for i in range(1, 10)]
        transport = _Scripted([batch])
        result = run_session(
            transport, bot_username=BOT, allowed_chats={GROUP},
            limits=SessionLimits(seconds=60, max_messages=3),
            now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json",
        )
        assert len(result.seen) <= 3

    def test_get_updates_is_called_with_offset_plus_one(self, tmp_path):
        clock = _Clock()
        transport = _Scripted([_update(50, "@cs_mscbot hi")])
        run_session(transport, bot_username=BOT, allowed_chats={GROUP}, offset=49,
                    limits=SessionLimits(seconds=5, max_messages=5),
                    now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json")
        first = [p for m, p in transport.calls if m == "getUpdates"][0]
        assert first["offset"] == 50

    def test_a_transport_failure_returns_error_not_an_exception(self, tmp_path):
        from telegram.errors import TransportError

        class Boom(MockTransport):
            def call(self, method, params):  # noqa: ANN001
                raise TransportError("network down")

        clock = _Clock()
        result = run_session(
            Boom(), bot_username=BOT, allowed_chats={GROUP},
            limits=SessionLimits(seconds=5, max_messages=5),
            now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json",
        )
        assert result.status == "error" and "network down" in (result.error or "")

    def test_summary_shape_is_stable(self, tmp_path):
        clock = _Clock()
        transport = _Scripted([_update(1, "@cs_mscbot help")])
        result = run_session(
            transport, bot_username=BOT, allowed_chats={GROUP},
            limits=SessionLimits(seconds=5, max_messages=5),
            now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json",
        )
        summary = result.summary()
        assert set(summary) == {"status", "seen", "replied", "queued_approval",
                                "refused", "next_offset", "error"}


# ================================================================ the CLI seam
class TestInteractiveCli:
    def _run(self, *argv):
        from telegram import cli as tg_cli
        return tg_cli.main(list(argv))

    def test_without_an_allowlist_it_refuses_with_code_3(self, monkeypatch, capsys):
        monkeypatch.setenv("TELEGRAM_CHAT_ALLOWLIST", "")
        code = self._run("--json", "interactive")
        assert code == 3
        out = json.loads(capsys.readouterr().out)
        assert out["code"] == 3

    def test_without_live_it_refuses_with_code_5(self, monkeypatch, capsys):
        monkeypatch.setenv("TELEGRAM_CHAT_ALLOWLIST", str(GROUP))
        code = self._run("--json", "interactive")
        assert code == 5
        assert json.loads(capsys.readouterr().out)["code"] == 5

    def test_a_bad_window_is_rejected_with_code_2(self, monkeypatch, capsys):
        monkeypatch.setenv("TELEGRAM_CHAT_ALLOWLIST", str(GROUP))
        code = self._run("--json", "--live", "interactive", "--for", "0")
        assert code == 2

    def test_interactive_is_not_a_schema_verb(self):
        """D15 isolation: it must never ride the publish path."""
        from telegram.schema import VERBS
        assert "interactive" not in VERBS
        assert "getUpdates" not in VERBS


# ============================================================ residual edges
class TestInteractiveEdges:
    """The branches a happy path never reaches — malformed input and failures."""

    def test_a_mention_entity_is_matched_by_offset(self):
        """The bot may be mentioned via an entity rather than bare text."""
        text = "hello @cs_mscbot there"
        entities = [{"type": "mention", "offset": 6, "length": 10}]
        addressed, _, _ = extract_mentions(
            [_update(1, text, entities=entities)],
            bot_username=BOT, allowed_chats={GROUP},
        )
        assert len(addressed) == 1

    def test_a_mention_entity_for_someone_else_is_ignored(self):
        text = "hello @someoneelse there"
        entities = [{"type": "mention", "offset": 6, "length": 13}]
        addressed, _, _ = extract_mentions(
            [_update(1, text, entities=entities)],
            bot_username=BOT, allowed_chats={GROUP},
        )
        assert not addressed

    def test_a_non_dict_entity_is_skipped(self):
        addressed, _, _ = extract_mentions(
            [_update(1, "@cs_mscbot hi", entities=["not-a-dict"])],
            bot_username=BOT, allowed_chats={GROUP},
        )
        assert len(addressed) == 1  # matched by the plain-text path

    def test_no_username_means_only_commands_count(self):
        addressed, _, _ = extract_mentions(
            [_update(1, "@cs_mscbot hi"), _update(2, "/help")],
            bot_username=None, allowed_chats={GROUP},
        )
        assert [m.update_id for m in addressed] == [2]

    def test_an_update_without_a_message_is_skipped(self):
        addressed, _, highest = extract_mentions(
            [{"update_id": 4, "callback_query": {"id": "x"}}],
            bot_username=BOT, allowed_chats={GROUP},
        )
        assert not addressed and highest == 4

    def test_a_dict_payload_wrapping_result_is_unwrapped(self, tmp_path):
        clock = _Clock()

        class Wrapped(MockTransport):
            def __init__(self):
                super().__init__()
                self._n = 0

            def call(self, method, params):  # noqa: ANN001
                self.calls.append((method, dict(params)))
                if method == "getUpdates":
                    self._n += 1
                    if self._n == 1:
                        return {"result": [_update(1, "@cs_mscbot help")]}
                    return {"result": []}
                return {"message_id": 1}

        result = run_session(
            Wrapped(), bot_username=BOT, allowed_chats={GROUP},
            limits=SessionLimits(seconds=5, max_messages=5),
            now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json",
        )
        assert result.replied == 1

    def test_a_second_approval_appends_to_the_existing_ledger(self, tmp_path):
        clock = _Clock()
        approval = tmp_path / "pending.json"
        for uid in (1, 2):
            run_session(
                _Scripted([_update(uid, f"/pin {uid}")]),
                bot_username=BOT, allowed_chats={GROUP}, owner_ids={42},
                limits=SessionLimits(seconds=5, max_messages=5),
                now=clock.now, sleep=clock.sleep, approval_path=approval,
            )
        items = json.loads(approval.read_text(encoding="utf-8"))
        assert len(items) == 2, "a second approval must append, not overwrite"

    def test_a_corrupt_approval_ledger_is_recovered_not_fatal(self, tmp_path):
        clock = _Clock()
        approval = tmp_path / "pending.json"
        approval.write_text("{ not json", encoding="utf-8")
        result = run_session(
            _Scripted([_update(1, "/pin 3")]),
            bot_username=BOT, allowed_chats={GROUP}, owner_ids={42},
            limits=SessionLimits(seconds=5, max_messages=5),
            now=clock.now, sleep=clock.sleep, approval_path=approval,
        )
        assert result.queued_approval == 1
        items = json.loads(approval.read_text(encoding="utf-8"))
        assert len(items) == 1, "a corrupt ledger must be replaced with a clean one"

    def test_a_non_list_approval_ledger_is_replaced(self, tmp_path):
        clock = _Clock()
        approval = tmp_path / "pending.json"
        approval.write_text('{"not": "a list"}', encoding="utf-8")
        run_session(
            _Scripted([_update(1, "/pin 3")]),
            bot_username=BOT, allowed_chats={GROUP}, owner_ids={42},
            limits=SessionLimits(seconds=5, max_messages=5),
            now=clock.now, sleep=clock.sleep, approval_path=approval,
        )
        assert isinstance(json.loads(approval.read_text(encoding="utf-8")), list)

    def test_a_failed_reply_is_audited_and_does_not_abort_the_session(self, tmp_path):
        from telegram.errors import TransportError

        clock = _Clock()
        audited = []

        class HalfBroken(MockTransport):
            def __init__(self):
                super().__init__()
                self._n = 0

            def call(self, method, params):  # noqa: ANN001
                self.calls.append((method, dict(params)))
                if method == "getUpdates":
                    self._n += 1
                    return [_update(1, "@cs_mscbot help")] if self._n == 1 else []
                raise TransportError("send failed")

        result = run_session(
            HalfBroken(), bot_username=BOT, allowed_chats={GROUP},
            limits=SessionLimits(seconds=5, max_messages=5),
            now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json",
            audit=lambda *a, **k: audited.append((a, k)),
        )
        assert result.status == "ok" and result.replied == 0
        # the failure was recorded, not swallowed (audit takes verb, result positionally)
        assert any(args and len(args) > 1 and args[1] == "error" for args, _kw in audited), audited

    def test_a_scripted_gateway_error_on_get_updates_stops_the_session(self, tmp_path):
        from telegram.errors import GatewayNotReady

        class NoToken(MockTransport):
            def call(self, method, params):  # noqa: ANN001
                raise GatewayNotReady("no token")

        clock = _Clock()
        result = run_session(
            NoToken(), bot_username=BOT, allowed_chats={GROUP},
            limits=SessionLimits(seconds=5, max_messages=5),
            now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json",
        )
        assert result.status == "error" and "no token" in (result.error or "")

    def test_edited_message_is_treated_as_a_mention(self, tmp_path):
        clock = _Clock()
        update = {"update_id": 1, "edited_message": {
            "message_id": 1, "chat": {"id": GROUP}, "from": {"id": 42},
            "text": "@cs_mscbot fixed",
        }}
        result = run_session(
            _Scripted([update]), bot_username=BOT, allowed_chats={GROUP},
            limits=SessionLimits(seconds=5, max_messages=5),
            now=clock.now, sleep=clock.sleep, approval_path=tmp_path / "p.json",
        )
        assert result.replied == 1

    def test_memory_self_check_writes_a_heartbeat(self, monkeypatch, tmp_path):
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", tmp_path / "telegram")
        mem._self_check()
        assert "last_self_check" in mem.read_state()

    def test_memory_write_survives_a_readonly_error(self, monkeypatch, tmp_path):
        """A memory failure must never propagate — it is bookkeeping only."""
        monkeypatch.setattr(mem, "DEFAULT_MEMORY_ROOT", tmp_path / "telegram")

        def _boom(self, text):  # noqa: ANN001
            raise OSError("disk full")

        monkeypatch.setattr(Path, "write_text", _boom)
        mem.append_log("this must not raise")  # swallows the OSError
