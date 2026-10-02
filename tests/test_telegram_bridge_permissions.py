"""Bridge (Pull) + permissions (urgent vs. restricted) — failing-test-first gate.

Covers the third item of the approved plan (agent bridge + permission model):
* permissions.classify / needs_approval / approval reply parsing
* bridge.pull_once / proposal_for_mention — proposals only, never sends
"""

from __future__ import annotations

import pytest

from telegram.bridge import BridgeProposal, proposal_for_mention, pull_once
from telegram.errors import TransportError
from telegram.interactive import Mention
from telegram.permissions import (
    classify,
    format_approval_request,
    needs_approval,
    parse_approval_reply,
)
from telegram.schema import parse_action
from telegram.transport import MockTransport

OWNER = 5664798395
CHAT = -1003710711332


def _action(**kw):
    base = {"verb": "publish", "actor": OWNER,
            "target": {"chat_id": CHAT, "thread_id": 84}, "text": "hi"}
    base.update(kw)
    return parse_action(base)


def _mention(text, *, actor=OWNER, chat=CHAT, uid=10, thread=84):
    return Mention(update_id=uid, message_id=uid + 100, chat_id=chat,
                   actor=actor, text=text, thread_id=thread)


def _update(uid, text, *, actor=OWNER, chat=CHAT):
    return {"update_id": uid,
            "message": {"message_id": uid + 100, "chat": {"id": chat},
                        "from": {"id": actor}, "text": text}}


class _Batch(MockTransport):
    """A MockTransport whose ``getUpdates`` returns a fixed batch, then []."""

    def __init__(self, batch):
        super().__init__()
        self._batch = list(batch)
        self._polled = 0

    def call(self, method, params):
        self.calls.append((method, dict(params)))
        if method == "getUpdates":
            self._polled += 1
            if self._polled == 1:
                return self._batch
            return []
        return {"message_id": 9000 + self._polled}


# ---------------------------------------------------------------- permissions
class TestClassify:
    @pytest.mark.parametrize("verb", ["publish", "reply", "forward", "copy",
                                      "react", "action", "quiz"])
    def test_plain_verbs_are_urgent(self, verb):
        kw = {"verb": verb, "actor": OWNER, "target": {"chat_id": CHAT}}
        if verb == "publish":
            kw["text"] = "hi"
        elif verb == "reply":
            kw.update(to="123", text="hi")
        elif verb in ("forward", "copy"):
            kw["source"] = "123"
        elif verb == "react":
            kw.update(message_id=1, emoji="👍")
        elif verb == "action":
            kw["kind"] = "typing"
        elif verb == "quiz":
            kw["quiz_id"] = "Quiz_01_X"
        assert classify(parse_action(kw)) == "urgent"

    def test_local_verbs_are_urgent(self):
        assert classify(parse_action({"verb": "status"})) == "urgent"
        assert classify(parse_action({"verb": "queue", "op": "list"})) == "urgent"

    def test_edit_single_message_is_urgent(self):
        action = parse_action({"verb": "edit", "actor": OWNER,
                               "target": {"chat_id": CHAT},
                               "message_id": 141, "text": "new card"})
        assert classify(action) == "urgent"
        assert needs_approval(action) is False

    def test_pipeline_single_publish_is_urgent(self):
        action = parse_action({"verb": "pipeline", "actor": OWNER,
                               "target": {"chat_id": CHAT},
                               "source": "01_Semester_1/02_X/03_Study_Notes/W01.md"})
        assert classify(action) == "urgent"

    @pytest.mark.parametrize("op", ["create", "rename", "delete"])
    def test_topic_ops_are_restricted(self, op):
        kw = {"verb": "topic", "actor": OWNER,
              "target": {"chat_id": CHAT, "thread_id": 84}, "op": op}
        if op in ("create", "rename"):
            kw["name"] = "X"
        assert classify(parse_action(kw)) == "restricted"

    def test_any_delete_is_restricted(self):
        action = parse_action({"verb": "delete", "actor": OWNER,
                               "target": {"chat_id": CHAT}, "message_ids": [99]})
        assert classify(action) == "restricted"
        assert needs_approval(action) is True

    def test_bulk_delete_is_restricted_via_destructive(self):
        action = parse_action({"verb": "delete", "actor": OWNER,
                               "target": {"chat_id": CHAT},
                               "message_ids": [99, 100]})
        assert action.destructive() is True
        assert classify(action) == "restricted"

    def test_pin_and_unpin_all_are_restricted(self):
        single = parse_action({"verb": "pin", "actor": OWNER,
                               "target": {"chat_id": CHAT}, "message_id": 141})
        sweep = parse_action({"verb": "pin", "actor": OWNER,
                              "target": {"chat_id": CHAT, "thread_id": 84},
                              "unpin_all": True, "pinned": False})
        assert classify(single) == "restricted"
        assert classify(sweep) == "restricted"

    def test_structure_is_restricted(self):
        action = parse_action({"verb": "structure", "actor": OWNER,
                               "target": {"chat_id": CHAT}})
        assert classify(action) == "restricted"


class TestApprovalCard:
    def test_card_carries_yes_no_instructions(self):
        action = parse_action({"verb": "delete", "actor": OWNER,
                               "target": {"chat_id": CHAT}, "message_ids": [99]})
        card = format_approval_request(action, actor=OWNER, chat_id=CHAT)
        assert card["kind"] == "restricted"
        assert "نعم" in card["text"] and "لا" in card["text"]
        assert "delete" in card["text"]

    @pytest.mark.parametrize("yes", ["نعم", "موافق", "اي", "تمام",
                                     "yes", "YES", "approve", "ok"])
    def test_affirmatives(self, yes):
        assert parse_approval_reply(yes) is True

    @pytest.mark.parametrize("no", ["لا", "رفض", "مرفوض", "الغي",
                                    "no", "NO", "reject", "cancel"])
    def test_negatives(self, no):
        assert parse_approval_reply(no) is False

    @pytest.mark.parametrize("other", ["", "   ", "شكرا", "هلا بوت",
                                       "maybe later", "123"])
    def test_non_decisions_stay_pending(self, other):
        assert parse_approval_reply(other) is None


# --------------------------------------------------------------------- bridge
class TestProposalForMention:
    def test_non_owner_is_denied(self):
        proposal = proposal_for_mention(_mention("/publish hi", actor=111),
                                        owner_ids={OWNER})
        assert proposal.kind == "denied"
        assert proposal.action is None

    def test_owner_free_text_is_a_note(self):
        proposal = proposal_for_mention(_mention("شلونك بوت؟"),
                                        owner_ids={OWNER})
        assert proposal.kind == "note"
        assert proposal.action is None

    def test_owner_publish_is_urgent(self):
        proposal = proposal_for_mention(_mention("/publish هلا بالمواد"),
                                        owner_ids={OWNER})
        assert proposal.kind == "urgent"
        assert proposal.action["verb"] == "publish"
        assert proposal.approval is None

    def test_owner_delete_is_restricted_with_card(self):
        proposal = proposal_for_mention(_mention("/delete 99"),
                                        owner_ids={OWNER})
        assert proposal.kind == "restricted"
        assert proposal.approval is not None
        assert "نعم" in proposal.approval["text"]

    def test_admin_verb_becomes_restricted(self):
        proposal = proposal_for_mention(_mention("/ban 111"),
                                        owner_ids={OWNER})
        assert proposal.kind == "restricted"
        assert proposal.approval is not None

    def test_unknown_command_is_a_note(self):
        proposal = proposal_for_mention(_mention("/frobnicate x"),
                                        owner_ids={OWNER})
        assert proposal.kind == "note"


class TestPullOnce:
    def test_empty_allowlist_refuses_before_network(self):
        transport = MockTransport()
        result = pull_once(transport, bot_username="cs_mscbot",
                           allowed_chats=set(), owner_ids={OWNER}, offset=5)
        assert result.status == "refused"
        assert result.next_offset == 5
        assert transport.calls == []

    def test_empty_inbox_is_ok(self):
        transport = _Batch([])
        result = pull_once(transport, bot_username="cs_mscbot",
                           allowed_chats={CHAT}, owner_ids={OWNER}, offset=7)
        assert result.status == "ok"
        assert result.proposals == []
        assert result.next_offset == 7

    def test_owner_command_becomes_urgent_proposal(self):
        transport = _Batch([_update(8, "/publish هلا")])
        result = pull_once(transport, bot_username="cs_mscbot",
                           allowed_chats={CHAT}, owner_ids={OWNER}, offset=7)
        assert result.status == "ok"
        assert len(result.proposals) == 1
        assert result.proposals[0].kind == "urgent"
        assert result.next_offset == 8
        # proposals only — the bridge never sends
        assert transport.methods() == ["getUpdates"]

    def test_off_allowlist_chat_is_refused_not_proposed(self):
        transport = _Batch([_update(9, "/publish hi", chat=-999)])
        result = pull_once(transport, bot_username="cs_mscbot",
                           allowed_chats={CHAT}, owner_ids={OWNER}, offset=8)
        assert result.proposals == []
        assert len(result.refused) == 1
        assert result.next_offset == 9

    def test_plain_chat_without_mention_advances_offset(self):
        transport = _Batch([_update(10, "دردشة عادية")])
        result = pull_once(transport, bot_username="cs_mscbot",
                           allowed_chats={CHAT}, owner_ids={OWNER}, offset=9)
        assert result.status == "ok"
        assert result.proposals == []
        assert result.next_offset == 10

    def test_transport_error_is_an_error_result(self):
        transport = MockTransport(script=[TransportError("down")])  # noqa: scripted error
        result = pull_once(transport, bot_username="cs_mscbot",
                           allowed_chats={CHAT}, owner_ids={OWNER}, offset=3)
        assert result.status == "error"
        assert result.next_offset == 3

    def test_denied_proposals_still_advance_offset(self):
        transport = _Batch([_update(12, "/publish hi", actor=111)])
        result = pull_once(transport, bot_username="cs_mscbot",
                           allowed_chats={CHAT}, owner_ids={OWNER}, offset=11)
        assert len(result.proposals) == 1
        assert result.proposals[0].kind == "denied"
        assert result.next_offset == 12

    def test_proposal_summary_shape(self):
        proposal: BridgeProposal = proposal_for_mention(
            _mention("/quiz Quiz_01_X"), owner_ids={OWNER})
        assert proposal.summary()["kind"] == "urgent"
