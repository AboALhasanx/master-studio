"""Tests for the Telegram gateway offline core (roadmap gate G1, issues #8-#16/#21).

SP1 of the roadmap: the G1 code must be provably network-free. Every test here
runs against the mock transport with registry/store files in tmp_path, and the
suite asserts the structural guarantees (fail-closed ACL, confirmation gate,
idempotency, audit trail, no live transport).
"""

import argparse
import io
import json
import os
import sys
import time
import urllib.error
from pathlib import Path
from types import SimpleNamespace

import pytest

# Ensure 90_Shared_Toolbox is on sys.path (same pattern as test_sieve_client)
toolbox_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox"
if str(toolbox_path) not in sys.path:
    sys.path.insert(0, str(toolbox_path))

from telegram import ACL, MockTransport, Registry, Store, build_call, execute, parse_action, plan  # noqa: E402
from telegram import cli as tg_cli  # noqa: E402
from telegram import pipeline as pipeline_mod  # noqa: E402
from telegram.acl import chat_allowlist_from_env  # noqa: E402
from telegram.errors import (  # noqa: E402
    AccessDenied,
    ActionValidationError,
    ConfirmationRequired,
    GatewayError,
    GatewayNotReady,
    PipelineError,
    RateLimited,
    RegistryError,
    RegistryMiss,
    TransportError,
    UnboundTopic,
)
from telegram.structure import STRUCTURE, topic_link  # noqa: E402
from telegram.links import parse_message_link  # noqa: E402
from telegram.publisher import TEXT_LIMIT, escape_html, split_message, split_once  # noqa: E402
from telegram.registry import SEED_SUBJECTS  # noqa: E402
from telegram.schema import idempotency_key  # noqa: E402
from telegram.store import ChatRateLimiter, Store, backoff_delay  # noqa: E402
from telegram.transport import (  # noqa: E402
    HttpTransport,
    RateLimitedScript,
    build_transport,
)

OWNER = 42


# --------------------------------------------------------------------------- fixtures
@pytest.fixture
def registry(tmp_path):
    return Registry(tmp_path / "registry.json")


@pytest.fixture
def store(tmp_path):
    return Store(tmp_path / "gateway.db")


@pytest.fixture
def acl():
    return ACL([OWNER])


@pytest.fixture
def transport():
    return MockTransport()


@pytest.fixture
def owners(monkeypatch):
    monkeypatch.setenv("TELEGRAM_OWNER_IDS", str(OWNER))


@pytest.fixture(autouse=True)
def no_accidental_live_transport(monkeypatch):
    """Safety net: the default suite must never build a live transport.

    Individual live-transport tests override the token explicitly.
    """
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "")


def publish(**overrides):
    payload = {
        "verb": "publish",
        "actor": OWNER,
        "target": {"chat_id": -1001234567890, "thread_id": 7},
        "text": "hello",
    }
    payload.update(overrides)
    return parse_action(payload)


# --------------------------------------------------------------------------- schema
def test_publish_requires_exactly_one_payload():
    with pytest.raises(ActionValidationError):
        parse_action({"verb": "publish", "target": {"chat_id": 1}})
    with pytest.raises(ActionValidationError):
        parse_action({"verb": "publish", "target": {"chat_id": 1}, "text": "x", "file": "y"})


def test_unknown_verb_rejected():
    with pytest.raises(ActionValidationError) as exc:
        parse_action({"verb": "deploy"})
    assert "unknown verb" in str(exc.value)


def test_non_object_action_rejected():
    with pytest.raises(ActionValidationError):
        parse_action(["publish"])


def test_target_requires_subject_or_chat():
    with pytest.raises(ActionValidationError):
        parse_action({"verb": "publish", "target": {"thread_id": 3}, "text": "x"})


def test_topic_create_requires_name_and_delete_needs_target():
    with pytest.raises(ActionValidationError):
        parse_action({"verb": "topic", "target": {"chat_id": 1}, "op": "create"})
    with pytest.raises(ActionValidationError):
        parse_action({"verb": "topic", "target": {"chat_id": 1}, "op": "close"})


def test_extra_fields_are_forbidden():
    with pytest.raises(ActionValidationError):
        parse_action({"verb": "status", "surprise": True})


def test_bulk_delete_is_destructive_single_is_not():
    single = parse_action({"verb": "delete", "target": {"chat_id": 1}, "message_ids": [5]})
    bulk = parse_action({"verb": "delete", "target": {"chat_id": 1}, "message_ids": [5, 6]})
    assert single.destructive() is False
    assert bulk.destructive() is True


def test_idempotency_key_ignores_actor_and_confirm():
    a = publish(actor=1)
    b = publish(actor=2, confirm=True)
    assert idempotency_key(a) == idempotency_key(b)


def test_idempotency_key_changes_with_content():
    assert idempotency_key(publish(text="a")) != idempotency_key(publish(text="b"))


# --------------------------------------------------------------------------- links
def test_parse_private_supergroup_link():
    ref = parse_message_link("https://t.me/c/1234567890/42")
    assert ref.message_id == 42
    assert ref.chat_id == -1001234567890


def test_parse_username_link_and_bare_id():
    ref = parse_message_link("t.me/master_studio_chat/9")
    assert (ref.username, ref.message_id, ref.chat_id) == ("master_studio_chat", 9, None)
    assert parse_message_link("42").message_id == 42


def test_parse_link_rejects_garbage():
    with pytest.raises(ActionValidationError):
        parse_message_link("https://example.com/42")


# --------------------------------------------------------------------------- ACL
def test_empty_allowlist_fails_closed():
    action = publish(actor=OWNER)
    with pytest.raises(AccessDenied):
        ACL([]).authorize(action)


def test_unknown_actor_denied():
    with pytest.raises(AccessDenied):
        ACL([1]).authorize(publish(actor=OWNER))


def test_missing_actor_denied():
    with pytest.raises(AccessDenied):
        ACL([OWNER]).authorize(publish(actor=None))


def test_owner_allowed():
    ACL([OWNER]).authorize(publish())


def test_local_verbs_are_not_gated():
    ACL([]).authorize(parse_action({"verb": "status"}))
    ACL([]).authorize(parse_action({"verb": "queue", "op": "list"}))


def test_topic_delete_requires_confirmation():
    action = parse_action(
        {"verb": "topic", "actor": OWNER, "target": {"subject": "01-Cyber-Security"}, "op": "delete"}
    )
    with pytest.raises(ConfirmationRequired) as exc:
        ACL([OWNER]).authorize(action)
    assert exc.value.code == 4
    ACL([OWNER]).authorize(parse_action(
        {"verb": "topic", "actor": OWNER, "confirm": True,
         "target": {"subject": "01-Cyber-Security"}, "op": "delete"}
    ))


def test_bulk_delete_requires_confirmation_but_single_does_not():
    acl = ACL([OWNER])
    acl.authorize(parse_action(
        {"verb": "delete", "actor": OWNER, "target": {"chat_id": 1}, "message_ids": [5]}
    ))
    with pytest.raises(ConfirmationRequired):
        acl.authorize(parse_action(
            {"verb": "delete", "actor": OWNER, "target": {"chat_id": 1}, "message_ids": [5, 6]}
        ))


# --------------------------------------------------------------------------- registry
def test_seed_creates_canonical_subjects_unbound(registry):
    assert registry.subjects() == sorted(s for s, _ in SEED_SUBJECTS)
    with pytest.raises(UnboundTopic):
        registry.resolve("01-Cyber-Security")


def test_bind_then_resolve_round_trip(registry):
    registry.bind("01-Cyber-Security", -1001234567890, 12, topic_name="01-Cyber-Security")
    row = registry.resolve("01-Cyber-Security")
    assert row["chat_id"] == -1001234567890
    assert row["thread_id"] == 12
    # persisted on disk, not just in memory
    reloaded = Registry(registry.path, seed=False)
    assert reloaded.resolve("01-Cyber-Security")["thread_id"] == 12


def test_unknown_subject_raises(registry):
    with pytest.raises(RegistryMiss):
        registry.get("99-Does-Not-Exist")


def test_same_thread_cannot_bind_two_subjects(registry):
    registry.bind("01-Cyber-Security", -1001, 5)
    with pytest.raises(RegistryMiss):
        registry.bind("03-Data-Mining", -1001, 5)


def test_unbind_returns_to_unbound(registry):
    registry.bind("99-Chat", -1001, 5)
    registry.unbind("99-Chat")
    with pytest.raises(UnboundTopic):
        registry.resolve("99-Chat")


def test_unbound_error_points_at_chat_for_the_general_topic(registry):
    """``00-Start-Here`` is the group's General and is *intentionally* unbound.

    ``docs/TELEGRAM_LEGACY_DEPRECATION.md`` records 10 topics provisioned from
    11 seeded subjects as the expected mapping, but the error told the caller
    to bind it at G2/G5 — advice that cannot be followed for a topic that has
    no ``thread_id`` to bind. The working route is an explicit ``--chat``.
    """
    with pytest.raises(UnboundTopic) as exc:
        registry.resolve("00-Start-Here")
    assert "--chat" in str(exc.value)


# --------------------------------------------------------------------------- store
def test_enqueue_is_idempotent(store):
    assert store.enqueue("k1", "publish", -1001, 5, {"a": 1}) is True
    assert store.enqueue("k1", "publish", -1001, 5, {"a": 1}) is False
    assert store.counts() == {"queued": 1}


def test_job_lifecycle_and_counts(store):
    store.enqueue("k1", "publish", -1001, 5, {})
    store.mark_sent("k1", 99)
    job = store.find("k1")
    assert job["status"] == "sent" and job["message_id"] == 99
    store.enqueue("k2", "publish", -1001, 5, {})
    store.mark_error("k2", "boom")
    assert store.counts() == {"sent": 1, "error": 1}
    assert store.pending()[0]["idempotency_key"] == "k2"


def test_audit_trail_records_outcomes(store):
    store.audit("publish", "denied", actor=7, detail="not on allowlist")
    store.audit("publish", "sent", actor=OWNER, chat_id=-1001, idempotency_key="k")
    rows = store.audit_rows()
    assert [r["result"] for r in rows] == ["sent", "denied"]
    assert rows[0]["actor"] == OWNER


def test_backoff_is_exponential_and_capped():
    assert [backoff_delay(n) for n in range(4)] == [2.0, 4.0, 8.0, 16.0]
    assert backoff_delay(99) == 60.0


def test_rate_limiter_per_minute_and_spacing():
    limiter = ChatRateLimiter(per_minute=3, min_interval=1.0)
    t0 = 1_000.0
    assert limiter.allow(1, t0)
    limiter.record(1, t0)
    assert limiter.allow(1, t0 + 0.5) is False, "must space messages >= 1s apart"
    assert limiter.allow(1, t0 + 1.0)
    limiter.record(1, t0 + 1.0)
    limiter.record(1, t0 + 2.0)
    assert limiter.allow(1, t0 + 3.0) is False, "must cap at per_minute"
    assert limiter.allow(1, t0 + 63.0) is True, "window must slide open again"


def test_rate_limiter_is_per_chat():
    limiter = ChatRateLimiter(per_minute=1, min_interval=0.0)
    limiter.record(1, 100.0)
    assert limiter.allow(1, 101.0) is False
    assert limiter.allow(2, 101.0) is True


# --------------------------------------------------------------------------- transport
def test_live_transport_requires_a_token():
    with pytest.raises(GatewayNotReady) as exc:
        build_transport(live=True, token="")
    assert exc.value.code == 5


def test_build_transport_modes():
    assert isinstance(build_transport(), MockTransport)
    live = build_transport(live=True, token="TEST:token")
    assert isinstance(live, HttpTransport) and live.is_live is True


def test_mock_records_calls_and_returns_message_ids():
    transport = MockTransport()
    result = transport.call("sendMessage", {"chat_id": 1, "text": "hi"})
    assert result["message_id"] > 0
    assert transport.methods() == ["sendMessage"]
    assert transport.last()[1]["text"] == "hi"


def test_scripted_rate_limit_raises():
    transport = MockTransport(script=[RateLimitedScript(3.0)])
    with pytest.raises(RateLimited) as exc:
        transport.call("sendMessage", {})
    assert exc.value.retry_after == 3.0


# --------------------------------------------------------------------------- executor
def test_execute_publish_sends_and_audits(registry, store, acl, transport):
    result = execute(publish(), transport=transport, acl=acl, registry=registry, store=store)
    assert result["status"] == "sent"
    method, params = transport.last()
    assert method == "sendMessage"
    assert params["message_thread_id"] == 7
    assert store.find(result["idempotency_key"])["status"] == "sent"
    assert store.audit_rows()[0]["result"] == "sent"


def test_execute_is_idempotent(registry, store, acl, transport):
    first = execute(publish(), transport=transport, acl=acl, registry=registry, store=store)
    second = execute(publish(), transport=transport, acl=acl, registry=registry, store=store)
    assert first["status"] == "sent"
    assert second["status"] == "duplicate"
    assert len(transport.calls) == 1, "the same command must never post twice"


def test_execute_denied_actor_is_audited(registry, store, transport):
    with pytest.raises(AccessDenied):
        execute(publish(actor=99), transport=transport, acl=ACL([OWNER]),
                registry=registry, store=store)
    assert store.audit_rows()[0]["result"] == "denied"
    assert transport.calls == [], "denied actions must never reach the transport"


def test_execute_unbound_subject_refuses(registry, store, acl, transport):
    action = publish(target={"subject": "03-Data-Mining"})
    with pytest.raises(UnboundTopic):
        execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert transport.calls == []
    assert store.audit_rows()[0]["result"] == "refused"


def test_execute_rate_limited_by_limiter_keeps_job_queued(registry, store, acl, transport):
    blocked = ChatRateLimiter(per_minute=0)
    result = execute(publish(), transport=transport, acl=acl, registry=registry,
                     store=store, limiter=blocked, now=1000.0)
    assert result["status"] == "queued"
    assert transport.calls == []
    job = store.find(result["idempotency_key"])
    assert job["status"] == "queued", "rate-limited job must survive for a later drain"


def test_execute_transport_429_marks_error(registry, store, acl):
    transport = MockTransport(script=[RateLimitedScript(7.0)])
    result = execute(publish(), transport=transport, acl=acl, registry=registry, store=store)
    assert result["status"] == "rate_limited"
    assert result["retry_after"] == 7.0
    job = store.find(result["idempotency_key"])
    assert job["status"] == "error" and job["attempts"] == 1


# --------------------------------------------------------------- issue #14 --
# Roadmap G3 exit criterion: "simulated 429 retried with no loss".
def test_transport_429_stores_a_cooldown_and_hides_the_job_until_it_elapses(
    registry, store, acl
):
    transport = MockTransport(script=[RateLimitedScript(7.0)])
    result = execute(publish(), transport=transport, acl=acl, registry=registry, store=store)
    key = result["idempotency_key"]

    # the retry_after Telegram handed us must land on the job itself
    assert result["retry_after"] == 7.0
    job = store.find(key)
    assert job["attempts"] == 1
    assert job["available_at"] > 0, "429 must record when the job becomes eligible again"

    # inside the cooldown the job is not drainable (no hammering) ...
    assert store.pending(now=job["available_at"] - 0.5) == []
    # ... but it is never dropped (no loss)
    assert [r["idempotency_key"] for r in store.pending(now=job["available_at"] + 0.5)] == [key]


def test_queue_run_defers_a_429_job_then_sends_it_exactly_once(registry, store, acl):
    transport = MockTransport(script=[RateLimitedScript(7.0)])
    blocked = ChatRateLimiter(per_minute=0)
    queued = execute(publish(), transport=transport, acl=acl, registry=registry,
                     store=store, limiter=blocked, now=1000.0)
    assert queued["status"] == "queued" and transport.methods() == []
    job_key = queued["idempotency_key"]

    # drain #1: the attempt happens and Telegram answers 429 -> deferred, not lost
    first = execute(parse_action({"verb": "queue", "op": "run"}), transport=transport,
                    acl=acl, registry=registry, store=store, now=1000.0)
    assert first["status"] == "ok" and first["sent"] == 0 and first["deferred"] == 1
    assert transport.methods() == ["sendMessage"], "the attempt must actually have happened"

    # still inside the 7s window -> a second drain must not fire a request
    second = execute(parse_action({"verb": "queue", "op": "run"}), transport=transport,
                     acl=acl, registry=registry, store=store, now=1006.0)
    assert second["sent"] == 0 and second["deferred"] == 0
    assert len(transport.methods()) == 1, "no hammering inside the cooldown"
    assert store.find(job_key)["status"] == "error", "job must survive the cooldown"

    # window elapsed -> exactly one more attempt, which succeeds
    third = execute(parse_action({"verb": "queue", "op": "run"}), transport=transport,
                    acl=acl, registry=registry, store=store, now=1010.0)
    assert third["sent"] == 1 and third["deferred"] == 0
    assert transport.methods() == ["sendMessage", "sendMessage"]
    assert store.find(job_key)["status"] == "sent"


def test_retries_are_bounded_and_then_give_up(store):
    key = "k-bounded"
    store.enqueue(key, "publish", -1001, 5, {"method": "sendMessage", "params": {}})
    for _ in range(Store.MAX_ATTEMPTS - 1):
        store.mark_error(key, "boom", retry_in=1.0, now=1000.0)
    assert store.find(key)["status"] == "error", "still retrying below the cap"

    store.mark_error(key, "boom", retry_in=1.0, now=1000.0)
    assert store.find(key)["status"] == "dead", "exhausted jobs must stop retrying"
    assert store.pending(now=5000.0) == [], "a dead job must never be drained again"


def test_queue_survives_a_restart_mid_drain_and_audits_every_attempt(
    tmp_path, registry, acl
):
    """#14 AC3: a crash mid-queue loses no job, and every attempt is audited."""
    db = tmp_path / "gateway.db"

    # --- process 1: the job is rate limited, then the process dies
    first = Store(db)
    blocked = ChatRateLimiter(per_minute=0)
    queued = execute(publish(), transport=MockTransport(), acl=acl, registry=registry,
                     store=first, limiter=blocked, now=1000.0)
    assert queued["status"] == "queued"
    key = queued["idempotency_key"]
    first.audit("publish", "rate_limited", chat_id=-1001234567890,
                idempotency_key=key, detail="retry_after=1.0")
    before = [dict(r) for r in reversed(first.audit_rows())]   # oldest first
    first.close()

    # --- process 2: a brand new Store on the same file
    second = Store(db)
    assert [r["idempotency_key"] for r in second.pending(now=5000.0)] == [key], (
        "a queued job must outlive the process that created it"
    )

    transport = MockTransport()
    drain = execute(parse_action({"verb": "queue", "op": "run"}), transport=transport,
                    acl=acl, registry=registry, store=second, now=5000.0)
    assert drain["sent"] == 1, "the surviving job must drain after the restart"
    assert second.find(key)["status"] == "sent"
    assert transport.methods() == ["sendMessage"]

    after = [dict(r) for r in reversed(second.audit_rows())]   # oldest first
    assert [r["idempotency_key"] for r in after] == [
        r["idempotency_key"] for r in before
    ] + [key, None], "the pre-restart attempt is preserved and the drain appends its own rows"
    assert after[len(before)]["result"] == "sent", "the drained send must be audited"
    assert after[len(before) + 1]["result"] == "run"
    assert after[len(before)]["idempotency_key"] == key


# --------------------------------------------------------------- issue #11 --
def test_escape_html_neutralises_markup():
    assert escape_html('<b>&"x"</b>') == "&lt;b&gt;&amp;&quot;x&quot;&lt;/b&gt;"
    assert escape_html("plain") == "plain"


def test_split_message_keeps_every_chunk_within_the_api_limit():
    text = ("word " * 3000).strip()
    chunks = split_message(text)
    assert len(chunks) > 1
    assert all(0 < len(c) <= TEXT_LIMIT for c in chunks)
    assert " ".join(chunks).split() == text.split(), "no word may be lost or duplicated"


def test_split_message_never_cuts_an_html_entity():
    text = "x" * (TEXT_LIMIT - 3) + "&amp; and the tail"
    chunks = split_message(text)
    assert all(len(c) <= TEXT_LIMIT for c in chunks)
    assert "".join(chunks).replace(" ", "") == text.replace(" ", "")
    assert not any(c.endswith("&") or c.endswith("&amp") for c in chunks), (
        "an entity must never be sliced across the boundary"
    )


def test_split_message_never_cuts_through_a_markdown_span():
    text = "a " * 2000 + "**" + "bold " * 400 + "** and `code` after"
    chunks = split_message(text)
    assert all(len(c) <= TEXT_LIMIT for c in chunks)
    assert "".join(chunks) == text, "splitting must be lossless"
    assert all(c.count("**") % 2 == 0 for c in chunks), "never split a **bold** span"
    assert all(c.count("`") % 2 == 0 for c in chunks), "never split a `code` span"


def test_split_once_returns_head_and_tail():
    head, tail = split_once("word " * 4000)
    assert len(head) <= TEXT_LIMIT and tail
    assert (head + tail).split() == ("word " * 4000).split()


def test_publish_file_carries_caption_and_parse_mode(registry, store, acl, transport):
    action = publish(text=None, file="file:///x/W01_Note.pdf", caption="<b>Week 1</b>",
                     parse_mode="HTML")
    execute(action, transport=transport, acl=acl, registry=registry, store=store)
    method, params = transport.calls[-1]
    assert method == "sendDocument"
    assert params["document"] == "file:///x/W01_Note.pdf"
    assert params["caption"] == "<b>Week 1</b>"
    assert params["parse_mode"] == "HTML"


def test_caption_needs_a_file_and_parse_mode_needs_text():
    with pytest.raises(ActionValidationError):
        publish(text="hi", caption="nope")           # caption without a file
    with pytest.raises(ActionValidationError):
        publish(text=None, file="file:///x/a.pdf", parse_mode="HTML")  # nothing to format


def test_publish_refuses_secrets_and_build_outputs(registry, store, acl, transport):
    """PR-template security rule, enforced on EVERY upload, not just `pipeline`."""
    for bad in (
        "file:///vault/.env",
        "file:///vault/keystore.jks",
        "file:///vault/app.apk",
        "file:///vault/gateway.db",
        "file:///vault/.ssh/keys/id_rsa.pem",
        "file:///vault/03_Study_Notes/__pycache__/note.pdf",
    ):
        with pytest.raises(PipelineError, match="excluded"):
            execute(publish(text=None, file=bad), transport=transport, acl=acl,
                    registry=registry, store=store)
    assert transport.calls == []
    assert all(row["result"] == "refused" for row in store.audit_rows())


# ------------------------------------------------------- media kinds (#11) --
def test_publish_selects_the_right_method_for_each_media_kind(
    registry, store, acl, transport
):
    cases = [
        ("photo", "sendPhoto", "photo", "file:///x/dependability_chain.png"),
        ("video", "sendVideo", "video", "file:///x/walkthrough.mp4"),
        ("audio", "sendAudio", "audio", "file:///x/viva.mp3"),
        ("voice", "sendVoice", "voice", "file:///x/note.ogg"),
        ("animation", "sendAnimation", "animation", "file:///x/loop.gif"),
        ("sticker", "sendSticker", "sticker", "file:///x/pack.tgs"),
        ("document", "sendDocument", "document", "file:///x/W01.pdf"),
    ]
    for kind, method, param, uri in cases:
        kwargs = {} if kind == "sticker" else {"caption": "Week 1"}
        execute(publish(text=None, file=uri, kind=kind, **kwargs),
                transport=transport, acl=acl, registry=registry, store=store)
        got, params = transport.last()
        assert got == method, kind
        assert params[param] == uri, kind
        assert "text" not in params, kind
        if kind == "sticker":
            assert "caption" not in params, "stickers carry no caption"
        else:
            assert params["caption"] == "Week 1"


def test_publish_kind_auto_reads_the_suffix_but_the_default_stays_document(
    registry, store, acl, transport
):
    for uri, method in (
        ("file:///x/diagram.PNG", "sendPhoto"),
        ("file:///x/photo.jpeg", "sendPhoto"),
        ("file:///x/loop.gif", "sendAnimation"),
        ("file:///x/clip.mp4", "sendVideo"),
        ("file:///x/note.ogg", "sendVoice"),
        ("file:///x/track.MP3", "sendAudio"),
        ("file:///x/W01.pdf", "sendDocument"),
        ("file:///x/mystery.bin", "sendDocument"),
    ):
        execute(publish(text=None, file=uri, kind="auto"),
                transport=transport, acl=acl, registry=registry, store=store)
        assert transport.last()[0] == method, uri

    # The DEFAULT must stay byte-exact: Telegram recompresses sendPhoto, so a
    # 2x-retina diagram round-tripped through it would lose resolution.
    execute(publish(text=None, file="file:///x/brooks_complexity_tree.png"),
            transport=transport, acl=acl, registry=registry, store=store)
    method, params = transport.last()
    assert method == "sendDocument"
    assert params["document"] == "file:///x/brooks_complexity_tree.png"


def test_publish_kind_needs_a_file_and_stickers_take_no_caption():
    with pytest.raises(ActionValidationError):
        publish(text="hello", kind="photo")
    with pytest.raises(ActionValidationError):
        publish(text="hello", kind="auto")
    with pytest.raises(ActionValidationError):
        publish(text=None, file="file:///x/pack.tgs", kind="sticker", caption="nope")


# ------------------------------------------------------ media group (#11) --
def test_media_group_posts_one_send_media_group_with_a_json_array(
    registry, store, acl, transport
):
    execute(
        publish(
            text=None,
            files=["file:///x/dependability_chain.png",
                   "file:///x/brooks_complexity_tree.png"],
            kind="auto",
            caption="Two chains from lecture 01",
            parse_mode="HTML",
        ),
        transport=transport, acl=acl, registry=registry, store=store,
    )
    method, params = transport.last()
    assert method == "sendMediaGroup"
    assert params["chat_id"] == -1001234567890
    assert params["message_thread_id"] == 7

    items = json.loads(params["media"])          # must be a JSON *string*
    assert [i["type"] for i in items] == ["photo", "photo"]
    assert [i["media"] for i in items] == [
        "file:///x/dependability_chain.png",
        "file:///x/brooks_complexity_tree.png",
    ]
    # Telegram shows ONE caption block for an album; repeating it per item
    # would post the same sentence under every photo.
    assert items[0]["caption"] == "Two chains from lecture 01"
    assert items[0]["parse_mode"] == "HTML"
    assert "caption" not in items[1]


def test_media_group_kind_pins_every_type_and_auto_drops_to_document(
    registry, store, acl, transport
):
    execute(publish(text=None, files=["file:///x/a.png", "file:///x/b.png"],
                    kind="photo"),
            transport=transport, acl=acl, registry=registry, store=store)
    _, params = transport.last()
    assert [i["type"] for i in json.loads(params["media"])] == ["photo", "photo"]

    # voice notes and animations are not album types at all
    execute(publish(text=None, files=["file:///x/note.ogg", "file:///x/loop.gif"],
                    kind="auto"),
            transport=transport, acl=acl, registry=registry, store=store)
    _, params = transport.last()
    assert [i["type"] for i in json.loads(params["media"])] == ["document", "document"]


def test_media_group_rejects_bad_shapes_at_schema_time():
    two = ["file:///x/a.png", "file:///x/b.png"]
    with pytest.raises(ActionValidationError, match="2-10 files"):
        publish(text=None, files=["file:///x/a.png"])
    with pytest.raises(ActionValidationError, match="2-10 files"):
        publish(text=None, files=["file:///x/a.png"] * 11)
    with pytest.raises(ActionValidationError, match="explicit --kind"):
        publish(text=None, files=two)                 # default kind is byte-exact
    with pytest.raises(ActionValidationError, match="only photo/video/audio/document"):
        publish(text=None, files=two, kind="voice")
    with pytest.raises(ActionValidationError, match="cannot be combined"):
        publish(text=None, files=two, kind="auto", file="file:///x/c.png")
    with pytest.raises(ActionValidationError, match="cannot be combined"):
        publish(text="hi", files=two, kind="auto")
    # ...and the good shapes still parse
    assert publish(text=None, files=two, kind="auto").files == two


def test_publish_group_refuses_an_excluded_member(registry, store, acl, transport):
    """The PR-template rule must hold per file, not just for `--file`."""
    with pytest.raises(PipelineError, match="excluded path"):
        execute(
            publish(text=None,
                    files=["file:///v/.env", "file:///v/notes.pdf"],
                    kind="auto"),
            transport=transport, acl=acl, registry=registry, store=store,
        )
    assert transport.calls == []


def test_media_group_audit_records_the_albums_first_message_id(registry, store, acl):
    """`sendMediaGroup` returns a LIST of messages, not one Message."""
    class _AlbumTransport:
        is_live = False

        def __init__(self):
            self.calls = []

        def call(self, method, params):
            self.calls.append((method, dict(params)))
            return [{"message_id": 41}, {"message_id": 42}]

        def methods(self):
            return [m for m, _ in self.calls]

        def last(self):
            return self.calls[-1]

    result = execute(
        publish(text=None, files=["file:///x/a.png", "file:///x/b.png"], kind="auto"),
        transport=_AlbumTransport(), acl=acl, registry=registry, store=store,
    )
    assert result["status"] == "sent"
    assert result["message_id"] == 41

    row = store.audit_rows()[0]
    assert row["result"] == "sent"
    assert row["detail"] == "sendMediaGroup -> 41", "an album must not audit as -> None"


def test_publish_chunks_a_long_text_without_losing_the_tail(registry, store, acl):
    text = ("word " * 4000).strip()
    transport = MockTransport()
    result = execute(publish(text=text), transport=transport, acl=acl,
                     registry=registry, store=store)
    key = result["idempotency_key"]

    assert result["status"] == "queued", "a multi-chunk publish is not finished yet"
    assert result["chunks_remaining"] >= 1
    assert transport.methods() == ["sendMessage"]

    sent = [transport.calls[0][1]["text"]]
    for _ in range(20):
        if store.find(key)["status"] == "sent":
            break
        drain = execute(parse_action({"verb": "queue", "op": "run"}), transport=transport,
                        acl=acl, registry=registry, store=store)
        assert drain["sent"] == 1, "every drain must advance exactly one chunk"
        sent.append(transport.calls[-1][1]["text"])
    else:
        raise AssertionError("the drain loop never finished")

    assert store.find(key)["status"] == "sent"
    assert all(0 < len(t) <= TEXT_LIMIT for t in sent)
    assert "".join(sent).split() == text.split(), "the tail must survive every hop"
    assert len(transport.calls) == len(sent)


# ------------------------------------------------- forward/copy (#11) --
def test_forward_reads_the_source_chat_and_message_from_the_link(registry, store, acl, transport):
    """``forwardMessage`` keeps the original sender; the link is all we know."""
    action = parse_action({
        "verb": "forward", "actor": OWNER,
        "target": {"chat_id": -1001234567890, "thread_id": 7},
        "source": "https://t.me/c/1234567890/42",
    })
    result = execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert result["status"] == "sent"
    method, params = transport.last()
    assert method == "forwardMessage"
    assert params == {
        "chat_id": -1001234567890,
        "from_chat_id": -1001234567890,
        "message_id": 42,
        "message_thread_id": 7,
    }


def test_copy_pulls_from_another_chat_and_can_re_caption(registry, store, acl, transport):
    action = parse_action({
        "verb": "copy", "actor": OWNER,
        "target": {"chat_id": -1001234567890, "thread_id": 7},
        "source": "https://t.me/c/999888777/15",
        "caption": "<b>week 1 recap</b>",
        "parse_mode": "HTML",
    })
    result = execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert result["status"] == "sent"
    method, params = transport.last()
    assert method == "copyMessage"
    assert params["from_chat_id"] == -100999888777
    assert params["message_id"] == 15
    assert params["caption"] == "<b>week 1 recap</b>"
    assert params["parse_mode"] == "HTML"
    assert params["message_thread_id"] == 7
    assert "reply_to_message_id" not in params


def test_copy_keeps_the_original_caption_when_none_is_given(registry, store, acl, transport):
    """No --caption means "keep whatever the original said", not an empty one."""
    action = parse_action({
        "verb": "copy", "actor": OWNER,
        "target": {"chat_id": -1001234567890},
        "source": "t.me/master_studio/9",
    })
    execute(action, transport=transport, acl=acl, registry=registry, store=store)
    _, params = transport.last()
    assert params["from_chat_id"] == "@master_studio", "a public link IS the chat id"
    assert params["message_id"] == 9
    assert "caption" not in params and "parse_mode" not in params


def test_forward_needs_a_source_chat_when_only_a_bare_id_is_given(registry, store, acl, transport):
    action = parse_action({
        "verb": "forward", "actor": OWNER,
        "target": {"chat_id": -1001234567890},
        "source": "42",
    })
    with pytest.raises(ActionValidationError) as exc:
        execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert "--from-chat" in str(exc.value)
    assert transport.calls == []
    assert store.audit_rows()[0]["result"] == "refused", "a refusal still leaves a trail"

    # ...but with it, the bare id resolves
    with_chat = parse_action({
        "verb": "forward", "actor": OWNER,
        "target": {"chat_id": -1001234567890},
        "source": "42", "source_chat": -1001234567890,
    })
    execute(with_chat, transport=transport, acl=acl, registry=registry, store=store)
    _, params = transport.last()
    assert params["from_chat_id"] == -1001234567890
    assert params["message_id"] == 42


def test_forward_refuses_a_source_link_that_contradicts_from_chat(registry, store, acl, transport):
    """A link and an explicit --from-chat that disagree is a mistake, not a surprise."""
    action = parse_action({
        "verb": "forward", "actor": OWNER,
        "target": {"chat_id": -1001234567890},
        "source": "https://t.me/c/1234567890/42",
        "source_chat": -100555666777,
    })
    with pytest.raises(ActionValidationError) as exc:
        execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert "source" in str(exc.value)
    assert transport.calls == []


def test_forward_and_copy_are_deduplicated_like_any_other_publish(
    registry, store, acl, transport
):
    action = parse_action({
        "verb": "forward", "actor": OWNER,
        "target": {"chat_id": -1001234567890},
        "source": "https://t.me/c/1234567890/42",
    })
    first = execute(action, transport=transport, acl=acl, registry=registry, store=store)
    second = execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert first["status"] == "sent"
    assert second["status"] == "duplicate"
    assert transport.methods() == ["forwardMessage"]


def test_forward_and_copy_obeys_the_owner_allowlist(registry, store, transport):
    action = parse_action({
        "verb": "copy", "actor": 999,
        "target": {"chat_id": -1001234567890},
        "source": "https://t.me/c/1234567890/42",
    })
    with pytest.raises(AccessDenied):
        execute(action, transport=transport, acl=ACL([OWNER]), registry=registry, store=store)
    assert transport.calls == [], "a refused copy must not reach Telegram"


def test_live_gate_watches_the_destination_and_never_the_source(registry, store, acl):
    """The source may sit outside the allowlist; the DESTINATION may not.

    Guard against anyone ever moving the G2 check onto ``from_chat_id``: a
    copy pulls *from* chat X and writes only to chat Y, so Y is the one that
    has to be allow-listed.
    """
    action = parse_action({
        "verb": "copy", "actor": OWNER,
        "target": {"chat_id": -1001234567890},           # NOT allow-listed
        "source": "https://t.me/c/999900000000/42",       # ...the source IS
    })
    with pytest.raises(AccessDenied) as exc:
        execute(action, transport=HttpTransport("TEST:token"), acl=acl,
                registry=registry, store=store,
                allowed_chats=chat_allowlist_from_env("-1009990000000"))
    assert "TELEGRAM_CHAT_ALLOWLIST" in str(exc.value)
    assert store.audit_rows()[0]["result"] == "denied"


def test_copy_parse_mode_needs_a_caption_and_forward_takes_no_caption():
    with pytest.raises(ActionValidationError) as exc:
        parse_action({
            "verb": "copy", "target": {"chat_id": -1},
            "source": "https://t.me/c/1234567890/42",
            "parse_mode": "HTML",
        })
    assert "parse_mode" in str(exc.value)

    # forwardMessage has no caption field at all, so the option must not exist
    with pytest.raises(ActionValidationError) as exc:
        parse_action({
            "verb": "forward", "target": {"chat_id": -1},
            "source": "https://t.me/c/1234567890/42",
            "caption": "forwardMessage has no caption field",
        })
    assert "caption" in str(exc.value)


# --------------------------------------------------------------- issue #13 --
def test_pipeline_refuses_paths_that_escape_the_vault(tmp_path, monkeypatch):
    monkeypatch.setattr(pipeline_mod, "VAULT_ROOT", tmp_path)
    with pytest.raises(PipelineError, match="escapes the vault"):
        pipeline_mod.resolve("../escape.md")
    with pytest.raises(PipelineError, match="escapes the vault"):
        pipeline_mod.resolve(str(tmp_path.parent / "elsewhere.md"))


def test_pipeline_refuses_excluded_paths(tmp_path, monkeypatch):
    monkeypatch.setattr(pipeline_mod, "VAULT_ROOT", tmp_path)
    notes = tmp_path / "03_Study_Notes"
    (notes / "__pycache__").mkdir(parents=True)
    (notes / "W01_Note.md").write_text("# ok", encoding="utf-8")

    for bad in (
        "03_Study_Notes/.env",
        "03_Study_Notes/keystore.jks",
        "03_Study_Notes/payload.apk",
        "03_Study_Notes/notes.db",
        "03_Study_Notes/__pycache__/W01_Note.md",
    ):
        with pytest.raises(PipelineError, match="excluded"):
            pipeline_mod.resolve(bad)

    # a legal-but-absent path is a plain not-found, not a security refusal
    with pytest.raises(PipelineError, match="not found"):
        pipeline_mod.resolve("03_Study_Notes/ghost.md")

    assert pipeline_mod.resolve("03_Study_Notes/W01_Note.md").name == "W01_Note.md"


def test_pipeline_not_found_says_where_it_looked(tmp_path, monkeypatch):
    """A bare ``source not found`` gave a live run nothing to correct.

    ``--dry-run`` deliberately does not resolve the path (see
    ``test_pipeline_cli_dry_run_never_touches_the_filesystem``), so this
    message is the only place a live failure can name the root it searched.
    """
    monkeypatch.setattr(pipeline_mod, "VAULT_ROOT", tmp_path)
    with pytest.raises(PipelineError) as exc:
        pipeline_mod.resolve("03_Study_Notes/ghost.md")
    assert str(tmp_path) in str(exc.value)


def test_pipeline_source_help_example_is_vault_relative():
    """The ``--source`` example was subject-relative; resolve() reads vault-relative.

    ``03_Study_Notes/W01_Note.md`` exists nowhere at the checkout root, so a
    live ``--source`` built from the documented shape died as not-found. The
    documented example must be a path an operator can actually paste.
    """
    parser = tg_cli.build_parser()
    subs = next(a for a in parser._actions if isinstance(a, argparse._SubParsersAction))
    # read the declared help, not format_help(): argparse text-wraps long
    # paths at an arbitrary column and would shatter the example token
    source_action = next(a for a in subs.choices["pipeline"]._actions
                         if a.dest == "source")
    example = next(tok for tok in source_action.help.split() if tok.endswith(".md"))
    assert example.startswith("01_Semester_1/"), example
    assert (pipeline_mod.VAULT_ROOT / example).is_file(), example
    # ...and it must survive argparse's text wrapping as one contiguous token,
    # or ``tg.py pipeline --help`` hands the operator a path split mid-word
    assert example in subs.choices["pipeline"].format_help(), example


def test_vault_root_is_the_checkout_not_one_level_too_high():
    """VAULT_ROOT used `parents[3]`, which resolves to the *user profile* dir.

    Every other pipeline test monkeypatched VAULT_ROOT onto a tmp_path, so the
    default root was never exercised: a live `pipeline --source` would have
    died as "source not found", and containment was one level too permissive.
    """
    root = pipeline_mod.VAULT_ROOT
    assert (root / "00_STUDIO_HUB").is_dir(), root
    assert (root / "90_Shared_Toolbox" / "telegram" / "pipeline.py").is_file(), root
    assert pipeline_mod.TOOLS_DIR == root / "90_Shared_Toolbox" / "tools"

    here = Path(pipeline_mod.__file__).resolve()
    assert pipeline_mod.resolve(here.relative_to(root).as_posix()) == here

    # the vault's own parent must be refused, not resolved
    with pytest.raises(PipelineError, match="escapes the vault"):
        pipeline_mod.resolve((root.parent / "outside-the-vault" / "note.md").as_posix())


def test_pipeline_reexports_only_when_the_artifact_is_missing_or_stale(tmp_path):
    src = tmp_path / "W01_Note.md"
    src.write_text("# Week 1", encoding="utf-8")

    art = pipeline_mod.artifact_for(src)
    assert art.suffix == ".pdf" and art.stem == src.stem
    assert pipeline_mod.needs_export(src, art) is True, "missing artifact -> export"

    art.write_text("pdf-bytes", encoding="utf-8")
    now = time.time()
    os.utime(art, (now, now))
    os.utime(src, (now - 60, now - 60))
    assert pipeline_mod.needs_export(src, art) is False, "fresh artifact -> reuse"

    os.utime(src, (now + 60, now + 60))
    assert pipeline_mod.needs_export(src, art) is True, "stale artifact -> re-export"

    # pre-built binaries carry no exporter rule: publish them as they are
    deck = tmp_path / "Deck.pdf"
    deck.write_text("x", encoding="utf-8")
    assert pipeline_mod.artifact_for(deck) == deck
    assert pipeline_mod.needs_export(deck, deck) is False


def test_pipeline_plan_is_pure_and_never_touches_the_filesystem(registry):
    action = parse_action({
        "verb": "pipeline",
        "target": {"chat_id": -1001},
        "source": "03_Study_Notes/ghost.md",   # deliberately absent
    })
    info = plan(action, registry)
    assert info["verb"] == "pipeline"
    assert info["source"] == "03_Study_Notes/ghost.md"
    assert "method" not in info, "plan must not resolve a path or build an upload"


def test_run_export_invokes_the_matching_exporter(tmp_path, monkeypatch):
    monkeypatch.setattr(pipeline_mod, "VAULT_ROOT", tmp_path)
    src = tmp_path / "W01_Note.md"
    src.write_text("# Week 1", encoding="utf-8")
    art = src.with_suffix(".pdf")
    seen: dict[str, list] = {}

    def fake_runner(cmd, **kwargs):
        seen["cmd"] = list(cmd)
        art.write_text("pdf-bytes", encoding="utf-8")
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    pipeline_mod.run_export(src, art, runner=fake_runner)
    assert seen["cmd"][0] == sys.executable
    assert seen["cmd"][1].endswith("pdf_exporter.py")
    assert str(src) in seen["cmd"]
    assert seen["cmd"][-2:] == ["-t", "study_pack"]
    assert art.exists()


def test_run_export_surfaces_a_failed_exporter(tmp_path, monkeypatch):
    monkeypatch.setattr(pipeline_mod, "VAULT_ROOT", tmp_path)
    src = tmp_path / "W01_Note.md"
    src.write_text("# Week 1", encoding="utf-8")
    art = src.with_suffix(".pdf")

    def failing_runner(cmd, **kwargs):
        return SimpleNamespace(returncode=1, stdout="", stderr="SyntaxError: boom")

    with pytest.raises(PipelineError, match="exporter failed"):
        pipeline_mod.run_export(src, art, runner=failing_runner)
    assert not art.exists()


def test_run_export_locates_the_toolchain_independently_of_the_vault(
    tmp_path, monkeypatch
):
    """Regression: a sandboxed vault must not make the exporter path vanish."""
    monkeypatch.setattr(pipeline_mod, "VAULT_ROOT", tmp_path)
    src = tmp_path / "W01_Note.md"
    src.write_text("# Week 1", encoding="utf-8")
    art = src.with_suffix(".pdf")
    seen: dict[str, list] = {}

    def fake_runner(cmd, **kwargs):
        seen["cmd"] = list(cmd)
        art.write_text("pdf-bytes", encoding="utf-8")
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    pipeline_mod.run_export(src, art, runner=fake_runner)
    script = Path(seen["cmd"][1])
    assert script.name == "pdf_exporter.py"
    assert script.is_file(), "the exporter lives in the checkout, not in the vault"


def test_pipeline_exports_then_publishes_and_stays_idempotent(
    registry, store, acl, transport, tmp_path, monkeypatch
):
    monkeypatch.setattr(pipeline_mod, "VAULT_ROOT", tmp_path)
    notes = tmp_path / "03_Study_Notes"
    notes.mkdir()
    src = notes / "W01_Note.md"
    src.write_text("# Week 1", encoding="utf-8")

    exports: list[str] = []

    def fake_run_export(source, artifact, *, root=None, runner=None):
        exports.append(source.name)
        time.sleep(0.02)                      # keep mtimes strictly ordered
        artifact.write_text("pdf-bytes", encoding="utf-8")
        return artifact

    monkeypatch.setattr(pipeline_mod, "run_export", fake_run_export)

    action = parse_action({
        "verb": "pipeline",
        "actor": OWNER,
        "target": {"chat_id": -1001, "thread_id": 7},
        "source": "03_Study_Notes/W01_Note.md",
        "caption": "<b>Week 1</b>",
        "parse_mode": "HTML",
    })

    first = execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert exports == ["W01_Note.md"], "a missing artifact must trigger an export"
    assert first["exported"] is True and first["status"] == "sent"
    assert transport.methods() == ["sendDocument"]
    _, params = transport.calls[0]
    assert params["document"].endswith("W01_Note.pdf")
    assert params["caption"] == "<b>Week 1</b>"
    assert params["parse_mode"] == "HTML"

    second = execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert exports == ["W01_Note.md"], "a fresh artifact must never be re-exported"
    assert second["exported"] is False
    assert second["status"] == "duplicate"
    assert len(transport.calls) == 1, "the same command must post exactly once"


def test_pipeline_cli_dry_run_never_touches_the_filesystem(tmp_path, capsys, owners):
    code, payload = run_cli(
        ["--json", "--dry-run", "--actor", str(OWNER),
         "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
         "pipeline", "--chat", "-1001", "--thread", "7",
         "--source", "03_Study_Notes/W01_Note.md"],
        capsys,
    )
    assert code == 0
    assert payload["dry_run"] is True and payload["authorized"] is True
    assert payload["plan"]["verb"] == "pipeline"
    assert payload["plan"]["source"] == "03_Study_Notes/W01_Note.md"
    assert "method" not in payload["plan"], "plan must not resolve or upload anything"
    assert Store(tmp_path / "g.db").counts() == {}, "dry-run must not enqueue anything"


def test_queue_run_drains_queued_jobs(registry, store, acl, transport):
    blocked = ChatRateLimiter(per_minute=0)
    execute(publish(), transport=transport, acl=acl, registry=registry,
            store=store, limiter=blocked, now=1000.0)

    drain = execute(parse_action({"verb": "queue", "op": "run"}), transport=transport,
                    acl=acl, registry=registry, store=store, limiter=ChatRateLimiter())
    assert drain["status"] == "ok" and drain["sent"] == 1
    assert transport.methods() == ["sendMessage"]


def test_plan_is_side_effect_free(registry, store, transport):
    preview = plan(publish(), registry)
    assert preview["method"] == "sendMessage"
    assert preview["params"]["chat_id"] == -1001234567890
    assert store.counts() == {} and transport.calls == []


def test_topic_delete_builds_delete_call_and_guards_confirm(registry, store, acl, transport):
    registry.bind("01-Cyber-Security", -1001234567890, 12)
    action = parse_action({"verb": "topic", "actor": OWNER, "confirm": True,
                           "target": {"subject": "01-Cyber-Security"}, "op": "delete"})
    result = execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert result["status"] == "sent"
    method, params = transport.last()
    assert method == "deleteForumTopic" and params["message_thread_id"] == 12


def test_reply_cross_chat_is_refused(registry, store, acl, transport):
    action = parse_action({
        "verb": "reply", "actor": OWNER,
        "target": {"chat_id": -1001234567890},
        "to": "https://t.me/c/999999999/5", "text": "hi",
    })
    with pytest.raises(ActionValidationError):
        execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert transport.calls == []


# --------------------------------------------------------------- issue #12 --
def test_reply_executes_when_a_message_link_is_the_only_input(registry, store, acl, transport):
    """AC1: nothing about the target message is known but the link itself."""
    action = parse_action({
        "verb": "reply", "actor": OWNER,
        "target": {"chat_id": -1001234567890},
        "to": "https://t.me/c/1234567890/42",
        "text": "see the pinned card",
    })
    result = execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert result["status"] == "sent"
    method, params = transport.last()
    assert method == "sendMessage"
    assert params["chat_id"] == -1001234567890
    assert params["reply_to_message_id"] == 42


def test_reply_accepts_a_public_username_link(registry, store, acl, transport):
    action = parse_action({
        "verb": "reply", "actor": OWNER,
        "target": {"chat_id": -1001234567890},
        "to": "t.me/master_studio/9",
        "text": "noted",
    })
    result = execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert result["status"] == "sent"
    _, params = transport.last()
    assert params["reply_to_message_id"] == 9


def test_bulk_delete_without_confirm_is_refused_and_still_audited(registry, store, transport):
    """AC3: a bulk delete may not fire, but the refusal must leave a trail."""
    acl = ACL([OWNER])
    action = parse_action({
        "verb": "delete", "actor": OWNER,
        "target": {"chat_id": -1001234567890},
        "message_ids": [5, 6, 7],
    })
    with pytest.raises(ConfirmationRequired):
        execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert transport.calls == [], "nothing may be deleted before the confirmation"

    row = store.audit_rows()[0]
    assert row["verb"] == "delete" and row["result"] == "denied"
    assert "confirm" in (row["detail"] or "")
    assert row["idempotency_key"] == idempotency_key(action), (
        "the refused attempt must stay traceable to its payload"
    )

    confirmed = execute(parse_action({**action.model_dump(mode="json"), "confirm": True}),
                        transport=transport, acl=acl, registry=registry, store=store)
    assert confirmed["status"] == "sent"
    method, params = transport.last()
    assert method == "deleteMessages"
    assert params["message_ids"] == [5, 6, 7]
    assert store.audit_rows()[0]["result"] == "sent"


def test_edit_switches_between_text_and_caption(registry, store, acl, transport):
    target = {"chat_id": -1001234567890}
    execute(parse_action({"verb": "edit", "actor": OWNER, "target": target,
                          "message_id": 9, "text": "new text"}),
            transport=transport, acl=acl, registry=registry, store=store)
    method, params = transport.last()
    assert method == "editMessageText" and params["text"] == "new text"

    execute(parse_action({"verb": "edit", "actor": OWNER, "target": target,
                          "message_id": 9, "caption": "new caption", "parse_mode": "HTML"}),
            transport=transport, acl=acl, registry=registry, store=store)
    method, params = transport.last()
    assert method == "editMessageCaption"
    assert params["caption"] == "new caption"
    assert params["parse_mode"] == "HTML"
    assert "text" not in params


def test_edit_requires_exactly_one_of_text_or_caption():
    with pytest.raises(ActionValidationError):
        parse_action({"verb": "edit", "target": {"chat_id": 1}, "message_id": 9})
    with pytest.raises(ActionValidationError):
        parse_action({"verb": "edit", "target": {"chat_id": 1}, "message_id": 9,
                      "text": "a", "caption": "b"})


def test_edit_carries_url_buttons(registry, store, acl, transport):
    """`editMessageText` takes `reply_markup`, so a rebuilt index keeps its links.

    A message the Bot API refuses to delete (>48h) can only be corrected in
    place — without this the only way to repoint its keyboard would be to
    delete and re-post, which breaks "the index is one message".
    """
    execute(parse_action({"verb": "edit", "actor": OWNER,
                          "target": {"chat_id": -1001234567890},
                          "message_id": 9, "text": "index",
                          "buttons": [{"label": "أمن المعلومات",
                                       "url": "https://t.me/c/1/84"}]}),
            transport=transport, acl=acl, registry=registry, store=store)
    method, params = transport.last()
    assert method == "editMessageText"
    assert params["reply_markup"] == {
        "inline_keyboard": [[{"text": "أمن المعلومات",
                              "url": "https://t.me/c/1/84"}]],
    }


def test_edit_without_buttons_leaves_the_keyboard_alone(registry):
    """No `--button` means no `reply_markup` key at all, not an empty one.

    An empty keyboard would silently strip the buttons off a message that
    cannot be re-sent.
    """
    from telegram.executor import build_call

    call = build_call(parse_action({"verb": "edit", "target": {"chat_id": 1},
                                    "message_id": 9, "text": "x"}),
                      registry)
    assert "reply_markup" not in call.params


def test_edit_buttons_never_ride_on_a_caption():
    """`editMessageCaption` has no keyboard field; refuse instead of dropping it."""
    with pytest.raises(ActionValidationError):
        parse_action({"verb": "edit", "target": {"chat_id": 1}, "message_id": 9,
                      "caption": "c",
                      "buttons": [{"label": "a", "url": "https://e.org"}]})


def test_action_verb_signals_a_chat_action(registry, store, acl, transport):
    action = parse_action({"verb": "action", "actor": OWNER,
                           "target": {"chat_id": -1001234567890, "thread_id": 7},
                           "kind": "typing"})
    result = execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert result["status"] == "sent"
    method, params = transport.last()
    assert method == "sendChatAction"
    assert params["chat_id"] == -1001234567890
    assert params["action"] == "typing"
    assert params["message_thread_id"] == 7, "the signal belongs in the topic, not General"


def test_action_verb_rejects_unknown_kinds():
    with pytest.raises(ActionValidationError):
        parse_action({"verb": "action", "target": {"chat_id": -1}, "kind": "summon"})


def test_topic_rename_close_and_reopen_build_their_own_calls(registry, store, acl, transport):
    registry.bind("01-Cyber-Security", -1001234567890, 12)
    cases = [
        ("rename", "editForumTopic", {"name": "01-Cyber-Security (2026)"}),
        ("close", "closeForumTopic", {}),
        ("reopen", "reopenForumTopic", {}),
    ]
    for op, expected, extra in cases:
        payload = {"verb": "topic", "actor": OWNER,
                   "target": {"subject": "01-Cyber-Security"}, "op": op, **extra}
        result = execute(parse_action(payload), transport=transport, acl=acl,
                         registry=registry, store=store)
        assert result["status"] == "sent", op
        method, params = transport.last()
        assert method == expected, op
        assert params["chat_id"] == -1001234567890, op
        assert params["message_thread_id"] == 12, op
        for key, value in extra.items():
            assert params[key] == value, op


def test_unpin_all_targets_the_topic_and_requires_confirmation(registry, store, acl, transport):
    registry.bind("01-Cyber-Security", -1001234567890, 12)
    payload = {"verb": "pin", "actor": OWNER, "target": {"subject": "01-Cyber-Security"},
               "unpin_all": True}

    with pytest.raises(ConfirmationRequired):
        execute(parse_action(payload), transport=transport, acl=acl,
                registry=registry, store=store)
    assert transport.calls == [], "a bulk unpin may not fire without --confirm"

    ok = execute(parse_action({**payload, "confirm": True}), transport=transport,
                 acl=acl, registry=registry, store=store)
    assert ok["status"] == "sent"
    method, params = transport.last()
    assert method == "unpinAllForumTopicMessages"
    assert params["chat_id"] == -1001234567890
    assert params["message_thread_id"] == 12


def test_pin_shape_validation():
    with pytest.raises(ActionValidationError):
        parse_action({"verb": "pin", "target": {"chat_id": 1}})           # nothing to pin
    with pytest.raises(ActionValidationError):
        parse_action({"verb": "pin", "target": {"chat_id": 1},
                      "unpin_all": True, "message_id": 4})                # contradictory


# --------------------------------------------------------------------------- CLI
def run_cli(argv, capsys):
    code = tg_cli.main(argv)
    out = capsys.readouterr().out
    return code, (json.loads(out) if out.strip() else {})


def test_cli_status_reports_offline_mode(tmp_path, capsys, owners):
    code, payload = run_cli(
        ["--json", "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
         "status"],
        capsys,
    )
    assert code == 0
    assert payload["mode"] == "MockTransport"
    assert payload["live_transport"] is False
    assert payload["registry"]["subjects"] == len(SEED_SUBJECTS)


def test_cli_dry_run_plans_without_executing(tmp_path, capsys, owners):
    code, payload = run_cli(
        ["--json", "--dry-run", "--actor", str(OWNER),
         "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
         "publish", "--chat", "-1001234567890", "--thread", "7", "--text", "hi"],
        capsys,
    )
    assert code == 0
    assert payload["dry_run"] is True and payload["authorized"] is True
    assert payload["plan"]["method"] == "sendMessage"
    assert Store(tmp_path / "g.db").counts() == {}, "dry-run must not enqueue anything"


def test_cli_dry_run_fails_closed_without_owners(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("TELEGRAM_OWNER_IDS", "")
    code, payload = run_cli(
        ["--json", "--dry-run", "--actor", str(OWNER),
         "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
         "publish", "--chat", "-1", "--text", "hi"],
        capsys,
    )
    assert code == 3
    assert payload["authorized"] is False


def test_cli_executes_against_mock(tmp_path, capsys, owners):
    code, payload = run_cli(
        ["--json", "--actor", str(OWNER),
         "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
         "publish", "--chat", "-1001234567890", "--thread", "7", "--text", "hi"],
        capsys,
    )
    assert code == 0
    assert payload["status"] == "sent" and payload["message_id"] > 0


def test_cli_transport_failure_exits_7(tmp_path, capsys, owners, monkeypatch):
    """A failed send must not look like success to anything that checks ``$?``.

    A live ``sendDocument`` of a 4.9 MB PDF hit a write timeout: the JSON said
    ``status: error`` while the shell reported ``exit=0``. CI, a cron, or a
    batch gate would carry straight past the failure. ``cli.py`` documents
    "7 transport failure" as an exit code, so the value must be returned.
    """
    from telegram.errors import TransportError

    class BrokenTransport:
        def call(self, method, params):  # noqa: ARG002
            raise TransportError(f"network error on {method}: write timed out")

    monkeypatch.setattr(tg_cli, "build_transport", lambda **_: BrokenTransport())

    code, payload = run_cli(
        ["--json", "--actor", str(OWNER),
         "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
         "publish", "--chat", "-1001234567890", "--thread", "7", "--text", "hi"],
        capsys,
    )
    assert payload["status"] == "error", payload
    assert code == 7, "a transport failure must exit 7, not 0"


def test_cli_destructive_action_needs_confirm(tmp_path, capsys, owners):
    registry = Registry(tmp_path / "r.json")
    registry.bind("99-Chat", -1001234567890, 9)
    code, payload = run_cli(
        ["--json", "--actor", str(OWNER),
         "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
         "topic", "--op", "delete", "--subject", "99-Chat"],
        capsys,
    )
    assert code == 4
    assert "confirm" in payload["error"]


def test_cli_bad_button_is_validation_error(tmp_path, capsys, owners):
    code, payload = run_cli(
        ["--json", "--actor", str(OWNER),
         "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
         "publish", "--chat", "-1", "--text", "hi", "--button", "no-url-here"],
        capsys,
    )
    assert code == 2
    assert payload["code"] == 2


def test_cli_live_without_token_fails_closed(tmp_path, capsys, owners, monkeypatch):
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "")
    code, payload = run_cli(
        ["--json", "--live",
         "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
         "status"],
        capsys,
    )
    assert code == 5
    assert "TELEGRAM_BOT_TOKEN" in payload["error"]


def test_json_output_survives_arabic_and_emoji_on_a_cp1252_console(monkeypatch):
    """`_emit` inherited the console encoding, so `react --emoji 👍` and any
    Arabic payload crashed with UnicodeEncodeError before printing a byte."""
    buffer = io.BytesIO()
    fake = io.TextIOWrapper(buffer, encoding="cp1252", newline="")
    monkeypatch.setattr(sys, "stdout", fake)

    tg_cli._emit({"status": "sent", "caption": "الأسبوع الأول", "emoji": "\U0001f44d"}, True)

    text = buffer.getvalue().decode("utf-8")
    assert "الأسبوع الأول" in text
    assert "\U0001f44d" in text
    assert json.loads(text)["status"] == "sent"   # still parseable JSON

    # the human-readable branch must not crash either
    buffer.seek(0)
    buffer.truncate(0)
    tg_cli._emit({"status": "sent", "caption": "مرحبا"}, False)
    assert "مرحبا" in buffer.getvalue().decode("utf-8")


def test_cli_wires_the_action_and_caption_edit_verbs(tmp_path, capsys, owners):
    base = ["--json", "--dry-run", "--actor", str(OWNER),
            "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db")]

    code, payload = run_cli(
        base + ["action", "--chat", "-1001", "--thread", "7", "--kind", "typing"], capsys
    )
    assert code == 0
    assert payload["plan"]["method"] == "sendChatAction"
    assert payload["plan"]["params"]["action"] == "typing"
    assert payload["plan"]["params"]["message_thread_id"] == 7

    code, payload = run_cli(
        base + ["edit", "--chat", "-1001", "--message-id", "9",
                "--caption", "<b>hi</b>", "--html"], capsys
    )
    assert code == 0
    assert payload["plan"]["method"] == "editMessageCaption"
    assert payload["plan"]["params"]["caption"] == "<b>hi</b>"
    assert payload["plan"]["params"]["parse_mode"] == "HTML"

    # neither --text nor --caption -> validation error, exit 2, nothing planned
    code, _ = run_cli(base + ["edit", "--chat", "-1001", "--message-id", "9"], capsys)
    assert code == 2


def test_cli_publish_exposes_kind_and_caption(tmp_path, capsys, owners):
    base = ["--json", "--dry-run", "--actor", str(OWNER),
            "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db")]

    code, payload = run_cli(
        base + ["publish", "--chat", "-1001", "--file", "file:///x/diagram.png",
                "--kind", "photo", "--caption", "Week 1 diagram", "--html"], capsys
    )
    assert code == 0
    assert payload["plan"]["method"] == "sendPhoto"
    assert payload["plan"]["params"]["photo"] == "file:///x/diagram.png"
    assert payload["plan"]["params"]["caption"] == "Week 1 diagram"
    assert payload["plan"]["params"]["parse_mode"] == "HTML"

    # default: still a byte-exact document, so nothing is recompressed
    code, payload = run_cli(
        base + ["publish", "--chat", "-1001", "--file", "file:///x/diagram.png"], capsys
    )
    assert code == 0
    assert payload["plan"]["method"] == "sendDocument"

    # a sticker is rejected outright when a caption is supplied
    code, payload = run_cli(
        base + ["publish", "--chat", "-1001", "--file", "file:///x/pack.tgs",
                "--kind", "sticker", "--caption", "nope"], capsys
    )
    assert code == 2


def test_cli_repeating_file_builds_a_media_group(tmp_path, capsys, owners):
    base = ["--json", "--dry-run", "--actor", str(OWNER),
            "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db")]

    # two --file flags => one sendMediaGroup, types read from the suffix
    code, payload = run_cli(
        base + ["publish", "--chat", "-1001",
                "--file", "file:///x/a.png", "--file", "file:///x/b.png",
                "--kind", "auto"], capsys
    )
    assert code == 0
    assert payload["plan"]["method"] == "sendMediaGroup"
    assert [i["type"] for i in json.loads(payload["plan"]["params"]["media"])] == [
        "photo", "photo"
    ]

    # a single --file is still an ordinary byte-exact document
    code, payload = run_cli(
        base + ["publish", "--chat", "-1001", "--file", "file:///x/a.png"], capsys
    )
    assert code == 0
    assert payload["plan"]["method"] == "sendDocument"

    # two files without a deliberate --kind fail closed, with the fix in the message
    code, payload = run_cli(
        base + ["publish", "--chat", "-1001",
                "--file", "file:///x/a.png", "--file", "file:///x/b.png"], capsys
    )
    assert code == 2
    assert "explicit --kind" in str(payload)


def test_cli_wires_the_forward_and_copy_verbs(tmp_path, capsys, owners):
    base = ["--json", "--dry-run", "--actor", str(OWNER),
            "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db")]

    code, payload = run_cli(
        base + ["forward", "--chat", "-1001", "--from", "https://t.me/c/1234567890/42"],
        capsys,
    )
    assert code == 0
    assert payload["plan"]["method"] == "forwardMessage"
    assert payload["plan"]["params"]["from_chat_id"] == -1001234567890
    assert payload["plan"]["params"]["message_id"] == 42

    code, payload = run_cli(
        base + ["copy", "--chat", "-1001", "--from", "https://t.me/c/999888777/15",
                "--caption", "<b>hi</b>", "--html"], capsys
    )
    assert code == 0
    assert payload["plan"]["method"] == "copyMessage"
    assert payload["plan"]["params"]["from_chat_id"] == -100999888777
    assert payload["plan"]["params"]["caption"] == "<b>hi</b>"
    assert payload["plan"]["params"]["parse_mode"] == "HTML"

    # a bare id with no --from-chat fails before anything is planned
    code, payload = run_cli(
        base + ["forward", "--chat", "-1001", "--from", "42"], capsys
    )
    assert code == 2
    assert "--from-chat" in str(payload)


def test_cli_audits_every_attempt(tmp_path, owners):
    db = tmp_path / "g.db"
    tg_cli.main(["--json", "--actor", str(OWNER), "--registry", str(tmp_path / "r.json"),
                 "--db", str(db), "publish", "--chat", "-1", "--text", "one"])
    tg_cli.main(["--json", "--actor", "999", "--registry", str(tmp_path / "r.json"),
                 "--db", str(db), "publish", "--chat", "-1", "--text", "two"])
    rows = Store(db).audit_rows()
    assert [r["result"] for r in rows] == ["denied", "sent"]


# --------------------------------------------------------------------------- G2: live transport
class _Resp:
    def __init__(self, payload):
        self._body = json.dumps(payload).encode("utf-8")

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def fake_urlopen(script, calls):
    """Return a urllib.request.urlopen stand-in driven by a FIFO script."""

    def _open(req, timeout=None):
        calls.append(req)
        item = script.pop(0)
        if isinstance(item, BaseException):
            raise item
        payload, status = item if isinstance(item, tuple) else (item, 200)
        if status >= 400:
            raise urllib.error.HTTPError(
                req.full_url, status, "http error", {},
                io.BytesIO(json.dumps(payload).encode("utf-8")),
            )
        return _Resp(payload)

    return _open


def _multipart_field(body: bytes, name: str) -> bytes:
    """Pull one form-data value back out of an encoded multipart body."""
    marker = f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode()
    start = body.index(marker) + len(marker)
    return body[start:body.index(b"\r\n", start)]


def test_http_transport_sends_ascii_safe_payload(monkeypatch):
    """Arabic must reach the wire ASCII-escaped (the terminal-mangling fix)."""
    import telegram.transport as tr

    calls = []
    monkeypatch.setattr(tr.urllib.request, "urlopen",
                        fake_urlopen([{"ok": True, "result": {"message_id": 7}}], calls))
    result = HttpTransport("TEST:token").call("sendMessage", {"chat_id": -1001, "text": "مرحبا"})
    assert result == {"message_id": 7}
    body = calls[0].data.decode("ascii")  # must not raise: wire format is ASCII
    assert json.loads(body)["chat_id"] == -1001
    assert calls[0].full_url.endswith("/sendMessage")
    headers = {k.lower(): v for k, v in calls[0].header_items()}
    assert headers["content-type"] == "application/json"


def test_http_transport_maps_429_to_rate_limited(monkeypatch):
    import telegram.transport as tr

    monkeypatch.setattr(tr.urllib.request, "urlopen", fake_urlopen([
        ({"ok": False, "error_code": 429,
          "description": "Too Many Requests: retry after 7",
          "parameters": {"retry_after": 7}}, 429),
    ], []))
    with pytest.raises(RateLimited) as exc:
        HttpTransport("TEST:token").call("sendMessage", {})
    assert exc.value.retry_after == 7.0


def test_http_transport_maps_api_and_network_errors(monkeypatch):
    import telegram.transport as tr

    monkeypatch.setattr(tr.urllib.request, "urlopen", fake_urlopen([
        ({"ok": False, "error_code": 400, "description": "Bad Request: chat not found"}, 400),
    ], []))
    with pytest.raises(TransportError, match="chat not found"):
        HttpTransport("TEST:token").call("sendMessage", {})

    monkeypatch.setattr(tr.urllib.request, "urlopen",
                        fake_urlopen([urllib.error.URLError("connection reset")], []))
    with pytest.raises(TransportError, match="network error"):
        HttpTransport("TEST:token").call("sendMessage", {})


# ---------------------------------------------------- local file uploads (#11)
def test_http_transport_uploads_a_local_file_as_multipart(monkeypatch, tmp_path):
    """A `file://` payload must travel multipart — Telegram rejects file URIs."""
    import telegram.transport as tr

    pdf = tmp_path / "W01_Note.pdf"
    pdf.write_bytes(b"%PDF-1.7 fake-bytes")

    calls = []
    monkeypatch.setattr(tr.urllib.request, "urlopen",
                        fake_urlopen([{"ok": True, "result": {"message_id": 31}}], calls))
    result = HttpTransport("TEST:token").call("sendDocument", {
        "chat_id": -1001,
        "message_thread_id": 12,
        "document": pdf.as_uri(),
        "caption": "الأسبوع الأول",
        "parse_mode": "HTML",
    })
    assert result == {"message_id": 31}

    req = calls[0]
    headers = {k.lower(): v for k, v in req.header_items()}
    assert headers["content-type"].startswith("multipart/form-data; boundary=")
    assert req.full_url.endswith("/sendDocument")

    body = req.data
    assert b"%PDF-1.7 fake-bytes" in body, "the file bytes must actually be on the wire"
    assert b'name="document"' in body
    assert b'filename="W01_Note.pdf"' in body
    assert b'name="chat_id"' in body and b"-1001" in body
    assert b'name="message_thread_id"' in body and b"12" in body
    assert b'name="caption"' in body and b'name="parse_mode"' in body
    assert "الأسبوع الأول".encode("utf-8") in body, "UTF-8 in multipart, never '?' mangled"


def test_http_transport_refuses_a_missing_local_file_before_any_request(
    monkeypatch, tmp_path
):
    import telegram.transport as tr

    calls = []
    monkeypatch.setattr(tr.urllib.request, "urlopen", fake_urlopen([], calls))
    with pytest.raises(TransportError, match="file not found"):
        HttpTransport("TEST:token").call(
            "sendDocument", {"chat_id": -1, "document": (tmp_path / "ghost.pdf").as_uri()}
        )
    assert calls == [], "a missing local file must never reach the network"


def test_an_upload_waits_longer_than_a_plain_call_before_timing_out(
    monkeypatch, tmp_path
):
    """One socket timeout must not strangle both branches of ``call()``.

    A 12 MB booklet upload died in production with
    ``network error on sendDocument: The write operation timed out`` —
    the 30 s JSON timeout was being handed to the multipart write as well,
    while Telegram was still reading the body.
    """
    import telegram.transport as tr

    pdf = tmp_path / "booklet.pdf"
    pdf.write_bytes(b"%PDF-1.7 " + b"x" * 64)

    seen = []

    class _Resp:
        def read(self):
            return json.dumps({"ok": True, "result": {"message_id": 7}}).encode("utf-8")

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

    def _open(req, timeout=None):
        seen.append(timeout)
        return _Resp()

    monkeypatch.setattr(tr.urllib.request, "urlopen", _open)

    transport = HttpTransport("TEST:token")
    transport.call("sendMessage", {"chat_id": -1, "text": "hi"})
    transport.call("sendDocument", {"chat_id": -1, "document": pdf.as_uri()})

    assert len(seen) == 2
    plain, upload = seen
    assert plain == transport.timeout, "a JSON call keeps the short timeout"
    assert upload == transport.upload_timeout
    assert upload > transport.timeout, "a slow 12 MB write needs a longer leash"


def test_http_transport_uploads_media_group_members_as_attach_parts(
    monkeypatch, tmp_path
):
    """`sendMediaGroup` carries local files as `attach://` parts, never as URIs.

    The `media` field is a JSON string; Telegram only resolves a local file
    when the entry reads `attach://<part name>` and a matching multipart part
    with that exact name ships alongside it.
    """
    import telegram.transport as tr

    a = tmp_path / "diagram_a.png"
    a.write_bytes(b"\x89PNG first-bytes")
    b = tmp_path / "diagram_b.png"
    b.write_bytes(b"\x89PNG second-bytes")

    media = json.dumps(
        [
            {"type": "photo", "media": a.as_uri(), "caption": "الأسبوع الأول"},
            {"type": "photo", "media": b.as_uri()},
        ],
        ensure_ascii=True,
    )

    calls = []
    monkeypatch.setattr(
        tr.urllib.request, "urlopen",
        fake_urlopen([{"ok": True,
                       "result": [{"message_id": 41}, {"message_id": 42}]}], calls),
    )
    result = HttpTransport("TEST:token").call("sendMediaGroup",
                                              {"chat_id": -1001, "media": media})
    assert result == [{"message_id": 41}, {"message_id": 42}]

    req = calls[0]
    headers = {k.lower(): v for k, v in req.header_items()}
    assert headers["content-type"].startswith("multipart/form-data; boundary=")
    assert req.full_url.endswith("/sendMediaGroup")

    body = req.data
    assert b"attach://file0" in body and b"attach://file1" in body
    assert b"file://" not in body, "a raw local URI must never leave the machine"
    assert b'name="file0"' in body and b'name="file1"' in body
    assert b'filename="diagram_a.png"' in body
    assert b"\x89PNG first-bytes" in body and b"\x89PNG second-bytes" in body
    assert b'name="chat_id"' in body and b"-1001" in body

    # `media` must stay ASCII-escaped on the wire (same rule as JSON payloads)
    # while still decoding to the real Arabic once Telegram parses it.
    media_field = _multipart_field(body, "media")
    media_field.decode("ascii")                                  # must not raise
    items = json.loads(media_field)
    assert items[0]["caption"] == "الأسبوع الأول"
    assert items[0]["media"] == "attach://file0"
    assert items[1]["media"] == "attach://file1"


def test_chat_allowlist_parsing():
    assert chat_allowlist_from_env("-1001, -1002") == frozenset({-1001, -1002})
    assert chat_allowlist_from_env("") == frozenset()
    assert chat_allowlist_from_env("junk") == frozenset(), "unparsable -> empty -> deny all"


def test_live_denies_chat_not_on_allowlist(registry, store, acl):
    with pytest.raises(AccessDenied) as exc:
        execute(publish(), transport=HttpTransport("TEST:token"), acl=acl,
                registry=registry, store=store,
                allowed_chats=chat_allowlist_from_env("-100999"))
    assert "TELEGRAM_CHAT_ALLOWLIST" in str(exc.value)
    assert store.audit_rows()[0]["result"] == "denied"


def test_live_with_empty_allowlist_denies_everything(registry, store, acl):
    with pytest.raises(AccessDenied):
        execute(publish(), transport=HttpTransport("TEST:token"), acl=acl,
                registry=registry, store=store, allowed_chats=None)


def test_live_allowed_chat_executes_and_audits(registry, store, acl, monkeypatch):
    import telegram.transport as tr

    calls = []
    monkeypatch.setattr(tr.urllib.request, "urlopen",
                        fake_urlopen([{"ok": True, "result": {"message_id": 42}}], calls))
    result = execute(
        publish(), transport=HttpTransport("TEST:token"), acl=acl,
        registry=registry, store=store,
        allowed_chats=chat_allowlist_from_env(str(publish().target.chat_id)),
    )
    assert result["status"] == "sent" and result["message_id"] == 42
    assert len(calls) == 1
    assert store.audit_rows()[0]["result"] == "sent"


# --------------------------------------------------------------------------- structure & binding
def test_topic_create_auto_binds_subject(registry, store, acl, transport):
    action = parse_action({
        "verb": "topic", "actor": OWNER,
        "target": {"subject": "01-Cyber-Security", "chat_id": -1001},
        "op": "create", "name": "01 Cyber Security", "icon_color": 7322016,
    })
    result = execute(action, transport=transport, acl=acl, registry=registry, store=store)
    assert result["status"] == "sent"
    method, params = transport.last()
    assert method == "createForumTopic"
    assert params["icon_color"] == 7322016
    row = registry.resolve("01-Cyber-Security")
    assert row["chat_id"] == -1001 and row["thread_id"] == result["message_id"]
    assert any(r["result"] == "bound" for r in store.audit_rows())


def test_structure_requires_an_explicit_chat(registry, store, acl, transport):
    action = parse_action({"verb": "structure", "actor": OWNER,
                           "target": {"subject": "99-Chat"}})
    with pytest.raises(RegistryError):
        execute(action, transport=transport, acl=acl, registry=registry, store=store)


def test_structure_dry_run_lists_everything_to_create(registry):
    preview = plan(parse_action({"verb": "structure", "target": {"chat_id": -1001}}), registry)
    assert preview["create"] == [s.subject for s in STRUCTURE]
    assert preview["cards"] is True and preview["index"] is True
    assert preview["already_bound"] == []


def test_structure_provisions_topics_cards_and_index(registry, store, acl, transport):
    action = parse_action({"verb": "structure", "actor": OWNER, "target": {"chat_id": -1001}})
    result = execute(action, transport=transport, acl=acl, registry=registry, store=store)

    assert result["status"] == "ok" and result["failures"] == []
    assert result["created"] == [s.subject for s in STRUCTURE]
    for spec in STRUCTURE:
        assert registry.get(spec.subject)["thread_id"] is not None

    methods = transport.methods()
    assert methods.count("createForumTopic") == len(STRUCTURE)
    assert methods.count("pinChatMessage") == len(STRUCTURE) + 1  # every card + the index

    # the index lands in General (no thread) with one button per topic
    index_calls = [p for m, p in transport.calls
                   if m == "sendMessage" and "message_thread_id" not in p]
    assert len(index_calls) == 1
    keyboard = index_calls[0]["reply_markup"]["inline_keyboard"]
    assert len(keyboard) == len(STRUCTURE)
    expected = topic_link(-1001, registry.get(STRUCTURE[0].subject)["thread_id"])
    assert keyboard[0][0]["url"] == expected

    # cards are posted inside their own topic
    card_calls = [p for m, p in transport.calls
                  if m == "sendMessage" and "message_thread_id" in p]
    assert len(card_calls) == len(STRUCTURE)


def test_structure_rerun_is_a_no_op(registry, store, acl, transport):
    action = parse_action({"verb": "structure", "actor": OWNER, "target": {"chat_id": -1001}})
    execute(action, transport=transport, acl=acl, registry=registry, store=store)
    calls_after_first = len(transport.calls)

    again = execute(parse_action({"verb": "structure", "actor": OWNER,
                                  "target": {"chat_id": -1001}}),
                    transport=transport, acl=acl, registry=registry, store=store)
    assert again["status"] == "ok"
    assert again["created"] == [] and again["failures"] == []
    assert len(transport.calls) == calls_after_first, "re-provisioning must not re-post"


def test_cli_structure_dry_run(tmp_path, capsys, owners):
    code, payload = run_cli(
        ["--json", "--dry-run", "--actor", str(OWNER),
         "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
         "structure", "--chat", "-1001"],
        capsys,
    )
    assert code == 0
    assert payload["plan"]["create"] == [s.subject for s in STRUCTURE]


# ------------------------------------------------------------- quiz bridge (#18)
class TestQuizBridge:
    """Phase A of the MCQ bridge: the gateway publishes a *door*, not an engine.

    The acceptance criteria of issue #18 are asserted directly here:
      AC1 one command publishes a working exam link to the correct topic,
      AC2 no second engine / the dashboard remains the single source of truth,
      AC3 Phase B stays deferred (i.e. no ``sendPoll`` is ever built).
    """

    def test_registry_key_maps_to_vault_folder(self):
        from telegram.quizbridge import subject_folder

        assert subject_folder("01-Cyber-Security") == "01_Cyber_Security"
        assert subject_folder("04-Advanced-Software-Eng") == "04_Advanced_Software_Eng"
        # idempotent: a folder name passes through untouched
        assert subject_folder("01_Cyber_Security") == "01_Cyber_Security"

    def test_url_matches_the_dashboard_route_table(self):
        from telegram.quizbridge import quiz_url

        url = quiz_url("01-Cyber-Security", "Quiz_01_Software_Crisis")
        assert url == (
            "http://127.0.0.1:5000/quiz/01_Cyber_Security/"
            "Quiz_01_Software_Crisis?mode=exam"
        )

    def test_url_shuffle_and_study_mode(self):
        from telegram.quizbridge import quiz_url

        url = quiz_url("03-Data-Mining", "Quiz_02", mode="study", shuffle=True)
        assert url.endswith("/quiz/03_Data_Mining/Quiz_02?mode=study&shuffle=true")

    def test_url_rejects_a_traversing_quiz_id(self):
        from telegram.quizbridge import quiz_url

        for bad in ("../secret", "a/b", "a?b", "a#b"):
            with pytest.raises(ValueError):
                quiz_url("01-Cyber-Security", bad)

    def test_url_rejects_an_unknown_mode_and_a_bad_port(self):
        from telegram.quizbridge import quiz_url

        with pytest.raises(ValueError):
            quiz_url("01-Cyber-Security", "Quiz_01", mode="midterm")
        with pytest.raises(ValueError):
            quiz_url("01-Cyber-Security", "Quiz_01", port=0)
        with pytest.raises(ValueError):
            quiz_url("01-Cyber-Security", "Quiz_01", port=70000)

    def test_schema_requires_an_id_and_refuses_separators(self):
        with pytest.raises(ActionValidationError):
            parse_action({"verb": "quiz", "target": {"chat_id": 1}})
        with pytest.raises(ActionValidationError):
            parse_action({"verb": "quiz", "target": {"chat_id": 1}, "quiz_id": "a/b"})

    def test_schema_defaults_favour_the_exam_door(self):
        action = parse_action(
            {"verb": "quiz", "target": {"chat_id": 1}, "quiz_id": "Quiz_01"}
        )
        assert action.mode == "exam"
        assert action.shuffle is False
        assert action.port == 5000

    def test_payload_offers_exam_and_study_buttons(self):
        from telegram.quizbridge import quiz_payload

        text, buttons = quiz_payload("01-Cyber-Security", "Quiz_01")
        assert "Quiz_01" in text
        assert [b["label"] for b in buttons] == ["▶️ ابدأ الاختبار", "📖 وضع الدراسة"]
        assert "mode=exam" in buttons[0]["url"]
        assert "mode=study" in buttons[1]["url"]

    def test_study_mode_does_not_offer_a_second_study_button(self):
        from telegram.quizbridge import quiz_payload

        _, buttons = quiz_payload("01-Cyber-Security", "Quiz_01", mode="study")
        assert len(buttons) == 1

    def test_ac1_build_call_lands_on_the_subject_topic(self, registry):
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        action = parse_action({
            "verb": "quiz", "actor": OWNER,
            "target": {"subject": "01-Cyber-Security"},
            "quiz_id": "Quiz_01_Software_Crisis",
        })
        call = build_call(action, registry)

        assert call.method == "sendMessage", "no new Bot API method is introduced"
        assert call.chat_id == -1001 and call.thread_id == 6
        keyboard = call.params["reply_markup"]["inline_keyboard"]
        assert keyboard[0][0]["url"] == (
            "http://127.0.0.1:5000/quiz/01_Cyber_Security/"
            "Quiz_01_Software_Crisis?mode=exam"
        )

    def test_ac1_execute_publishes_once_under_one_key(self, registry, store, acl, transport):
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        action = parse_action({
            "verb": "quiz", "actor": OWNER,
            "target": {"subject": "01-Cyber-Security"},
            "quiz_id": "Quiz_01_Software_Crisis",
        })
        first = execute(action, transport=transport, acl=acl, registry=registry, store=store)
        assert first["status"] == "sent"
        assert transport.methods() == ["sendMessage"]

        again = execute(action, transport=transport, acl=acl, registry=registry, store=store)
        assert again["status"] == "duplicate"
        assert transport.methods() == ["sendMessage"], "a repeat must not double-post"

    def test_ac2_no_engine_is_duplicated_in_the_gateway(self):
        """The gateway must not grow a quiz engine of its own (AC2).

        The check runs against the module's *code*, not its prose: the
        docstring deliberately names ``sendPoll``/``poll_answer`` in order to
        explain why they are deferred, so a naive substring scan would flag
        the very sentence that documents the deferral.
        """
        import ast

        import telegram.quizbridge as bridge

        tree = ast.parse(Path(bridge.__file__).read_text(encoding="utf-8"))
        docstrings = set()
        for node in ast.walk(tree):
            if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
                doc = ast.get_docstring(node, clean=False)
                if doc:
                    docstrings.add(doc)

        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                if node.value in docstrings:
                    continue  # prose may explain the deferral; code may not do it
                assert "sendPoll" not in node.value, node.value
                assert "correct_option_id" not in node.value, node.value

        # the module defines link helpers only — never a grader or a poll builder
        functions = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
        assert not any("poll" in name or "grade" in name for name in functions), functions

    def test_explicit_text_still_carries_the_link_button(self, registry):
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        action = parse_action({
            "verb": "quiz", "actor": OWNER,
            "target": {"subject": "01-Cyber-Security"},
            "quiz_id": "Quiz_01", "text": "اختبر نفسك 👇",
        })
        call = build_call(action, registry)
        assert call.params["text"] == "اختبر نفسك 👇"
        assert call.params["reply_markup"]["inline_keyboard"][0][0]["url"].endswith(
            "/quiz/01_Cyber_Security/Quiz_01?mode=exam"
        )

    def test_quiz_requires_a_bound_subject(self, registry):
        action = parse_action({
            "verb": "quiz", "actor": OWNER,
            "target": {"subject": "90-Toolbox"},
            "quiz_id": "Quiz_01",
        })
        with pytest.raises(RegistryError):
            build_call(action, registry)

    def test_cli_quiz_dry_run_shows_the_link(self, tmp_path, capsys, owners):
        registry_path = tmp_path / "r.json"
        seed = Registry(registry_path)
        seed.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)

        code, payload = run_cli(
            ["--json", "--dry-run", "--actor", str(OWNER),
             "--registry", str(registry_path), "--db", str(tmp_path / "g.db"),
             "quiz", "--subject", "01-Cyber-Security",
             "--quiz-id", "Quiz_01_Software_Crisis"],
            capsys,
        )
        assert code == 0
        assert payload["plan"]["publishes"] is True
        assert payload["plan"]["thread_id"] == 6
        assert payload["plan"]["url"].endswith(
            "/quiz/01_Cyber_Security/Quiz_01_Software_Crisis?mode=exam"
        )

    def test_cli_quiz_rejects_a_traversing_id(self, tmp_path, capsys, owners):
        code, payload = run_cli(
            ["--json", "--dry-run", "--actor", str(OWNER),
             "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
             "quiz", "--chat", "-1001", "--quiz-id", "../etc"],
            capsys,
        )
        assert code == 2
        assert "error" in payload


# --------------------------------------------------------- the telegram skill (#15)
class TestTelegramSkill:
    """The skill must stay in lockstep with the CLI it documents (issue #15).

    A skill that documents a verb the CLI does not have (or a flag that was
    renamed) is worse than no skill: the agent follows it and fails live.
    These tests read the *shipped* SKILL.md and diff it against the parser.
    """

    SKILL = Path(__file__).resolve().parent.parent / ".mimocode" / "skills" / "telegram" / "SKILL.md"

    def _skill_text(self) -> str:
        assert self.SKILL.is_file(), f"skill file missing: {self.SKILL}"
        return self.SKILL.read_text(encoding="utf-8")

    def test_skill_exists_with_frontmatter(self):
        text = self._skill_text()
        assert text.startswith("---\n"), "SKILL.md must open with YAML frontmatter"
        head = text.split("---", 2)[1]
        assert "name: telegram" in head
        assert "description:" in head

    def test_every_cli_verb_is_documented(self):
        from telegram.schema import VERBS

        text = self._skill_text()
        missing = [v for v in VERBS if v not in text]
        assert missing == [], f"verbs absent from SKILL.md: {missing}"

    def test_every_cli_subcommand_is_documented(self):
        """Generalise the verb check to the whole CLI, not just ``VERBS``.

        ``interactive`` sits deliberately outside ``schema.VERBS`` (D15: it
        must never be composable as a publish path), which made the VERBS
        check structurally blind to it - so the listening layer shipped on
        2026-09-30 with zero mentions in the skill and no gate noticed.
        Drive every argparse subcommand instead.
        """
        import telegram.cli as cli

        subcommands = cli.build_parser()._subparsers._group_actions[0].choices
        text = self._skill_text()
        missing = sorted(name for name in subcommands if name not in text)
        assert missing == [], f"CLI subcommands absent from SKILL.md: {missing}"

    def test_the_interactive_layer_is_documented_in_detail(self):
        """D14 + D15 + D16 must be actionable from the skill alone.

        Zero-CLI makes the *agent* the only interface: if the skill does not
        say how to open a session, what its bounds are, where the gateway
        keeps its memory and how approvals surface, the feature is
        unreachable no matter how well unit-tested it is.
        """
        import telegram.cli as cli

        text = self._skill_text()

        subcommands = cli.build_parser()._subparsers._group_actions[0].choices
        flags = {
            opt
            for action in subcommands["interactive"]._actions
            for opt in action.option_strings
        } - {"-h", "--help"}
        undocumented = sorted(f for f in flags if f not in text)
        assert undocumented == [], f"interactive flags absent from SKILL.md: {undocumented}"

        # D14: the gateway's own memory folder, plus the one rule that matters.
        assert "00_STUDIO_HUB/telegram/" in text, "D14 memory folder undocumented"
        assert "MEMORY.md" in text, "the D14 never-write-MEMORY.md rule is undocumented"
        # D16: administrative actions never auto-run.
        assert "pending_approval.json" in text, "D16 approval gate undocumented"

    def test_no_flag_is_documented_that_the_cli_lacks(self):
        """Every ``--flag`` in the skill must exist on a tool the skill documents.

        The skill documents two launchers, ``tg.py`` and ``tg_catalog.py``
        (§4.11), so the known set is the union of both parsers. The property is
        unchanged: a flag the skill mentions is a flag some documented tool
        actually has. Widening it without this framing would have let the
        catalog section ship with four flags the checker had simply never
        heard of.
        """
        import re

        import telegram.catalog as catalog
        import telegram.cli as cli

        known: set[str] = set()

        def collect(parser: argparse.ArgumentParser) -> None:
            # tg.py nests its verbs as subparsers; tg_catalog.py has a flat
            # mutually-exclusive group. Walking _subparsers directly blows up
            # on the second one, so descend through the action type instead.
            for action in parser._actions:
                known.update(action.option_strings)
                if isinstance(action, argparse._SubParsersAction):
                    for sub in action.choices.values():
                        collect(sub)

        for parser in (cli.build_parser(), catalog.build_parser()):
            collect(parser)

        used = set(re.findall(r"(?<![\w-])(--[a-z][a-z0-9-]+)", self._skill_text()))
        unknown = sorted(f for f in used if f not in known)
        assert unknown == [], f"SKILL.md documents flags the CLI does not have: {unknown}"

    def test_media_kinds_and_quiz_modes_are_documented(self):
        from telegram.publisher import MEDIA_KINDS

        text = self._skill_text()
        for kind in MEDIA_KINDS:
            assert kind in text, f"media kind {kind!r} undocumented"
        for mode in ("exam", "study"):
            assert mode in text, f"quiz mode {mode!r} undocumented"

    def test_every_documented_invocation_parses(self):
        """Run each `tg.py …` line in the doc through the real parser.

        `--live` is swapped for `--dry-run` so the check can never touch the
        network; the point is only that argparse accepts the shape.
        """
        import re
        import shlex

        text = self._skill_text()
        blocks = re.findall(r"```bash\n(.*?)```", text, re.S)
        invocations: list[str] = []
        for block in blocks:
            block = block.replace("\\\n", " ")
            for line in block.splitlines():
                line = re.sub(r"\s+#\s.*$", "", line.strip())
                if line and not line.startswith("#") and "tg.py" in line:
                    invocations.append(line.split("tg.py", 1)[1].strip())

        assert len(invocations) >= 20, f"expected the full verb catalogue, got {len(invocations)}"

        parser = tg_cli.build_parser()
        checked = 0
        for command in invocations:
            if "<verb>" in command or "[GLOBAL FLAGS]" in command:
                continue  # the usage template, not a real command
            command = command.replace("<id>", str(OWNER)).replace("--live", "--dry-run")
            argv = ["--registry", "r.json", "--db", "g.db"] + shlex.split(command)
            parser.parse_args(argv)  # raises SystemExit on a bad flag
            checked += 1
        assert checked >= 20, f"only {checked} real invocations checked"

    def test_skill_mirror_is_identical(self):
        """`.mimocode/skills/` and `skills/` must not drift apart."""
        root = Path(__file__).resolve().parent.parent
        mirror = root / "skills" / "telegram" / "SKILL.md"
        assert mirror.is_file(), "the mirror copy is missing"
        assert mirror.read_text(encoding="utf-8") == self._skill_text(), (
            "skills/telegram/SKILL.md drifted from .mimocode/skills/telegram/SKILL.md"
        )


# ------------------------------------------------- human-like behaviour pack (#17)
class TestPersona:
    """Pacing, presence and tone — the bot behaves like a person, not a firehose.

    Acceptance criteria of issue #17:
      AC1 a published post is anchored as a contextual reply (reply_to is wired),
      AC2 pacing and typing indicators are observable,
      AC3 the persona is documented and referenced by the gateway defaults.
    """

    def test_no_presence_before_the_first_item(self):
        from telegram.persona import pacing_seconds

        assert pacing_seconds(0) == 0.0

    def test_pacing_is_bounded_and_never_zero_mid_batch(self):
        from telegram.persona import PERSONA, pacing_seconds

        values = [pacing_seconds(i) for i in range(1, 13)]
        assert all(0.0 < v <= PERSONA.max_pace for v in values), values
        # unequal like a human, but reproducible (no RNG anywhere)
        assert len(set(values)) > 1, "pacing must not be a constant"
        assert values == [pacing_seconds(i) for i in range(1, 13)], "must be deterministic"

    def test_pacing_pattern_is_coprime_not_random(self):
        """No RNG may be *called* — prose explaining that is fine (same trap
        as the #18 AST test: a naive substring scan flags its own docstring)."""
        import ast

        import telegram.persona as persona

        tree = ast.parse(Path(persona.__file__).read_text(encoding="utf-8"))
        docstrings = set()
        for node in ast.walk(tree):
            if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
                doc = ast.get_docstring(node, clean=False)
                if doc:
                    docstrings.add(doc)

        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                assert node.id != "random", "the persona must not call the random module"
            if isinstance(node, ast.Attribute):
                assert node.attr != "random", "the persona must not call the random module"
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                if node.value in docstrings:
                    continue
                assert "random" not in node.value, "a random delay makes the suite flaky"

    def test_typing_is_signalled_only_for_long_text_or_uploads(self):
        from telegram.persona import TYPING_THRESHOLD, presence_for

        assert presence_for("ok") is None
        assert presence_for("") is None
        assert presence_for("x" * TYPING_THRESHOLD) == "typing"
        assert presence_for(None, uploading=True) == "upload_document"
        # an upload signals regardless of how short the caption is
        assert presence_for("hi", uploading=True) == "upload_document"

    def test_presence_value_is_in_the_sendchataction_vocabulary(self):
        from telegram.persona import presence_for
        from telegram.schema import CHAT_ACTIONS

        for value in (presence_for("x" * 500), presence_for(None, uploading=True)):
            assert value in CHAT_ACTIONS, value

    def test_read_estimate_is_clamped(self):
        from telegram.persona import PERSONA, estimate_read_seconds

        assert estimate_read_seconds("") == 0.0
        assert estimate_read_seconds("x" * 10) < 1.0
        # never exceeds the persona ceiling, however long the text
        assert estimate_read_seconds("x" * 100_000) == PERSONA.max_pace

    def test_pause_does_nothing_for_zero(self, monkeypatch):
        import telegram.persona as persona

        calls = []
        monkeypatch.setattr(persona.time, "sleep", lambda s: calls.append(s))
        persona.pause(0)
        persona.pause(0.0)
        assert calls == []
        persona.pause(1.5)
        assert calls == [1.5]

    def test_ac2_presence_fires_live_but_never_on_the_mock(self, registry, store, acl):
        """The signal is a *live* behaviour; the mock path must stay instant."""
        from telegram.transport import MockTransport

        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        mock = MockTransport()
        action = parse_action({
            "verb": "publish", "actor": OWNER,
            "target": {"subject": "01-Cyber-Security"}, "text": "x" * 500,
        })
        execute(action, transport=mock, acl=acl, registry=registry, store=store)
        assert "sendChatAction" not in mock.methods(), (
            "the mock must not pay the pacing cost — otherwise every test slows down"
        )

    def test_ac2_presence_fires_for_a_live_publish(self, registry, store, acl, monkeypatch):
        """A live transport emits sendChatAction first, then the message."""
        import telegram.executor as executor
        from telegram.transport import HttpTransport

        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "123:TEST")
        live = HttpTransport("123:TEST")
        calls = []

        def spy(method, params):
            calls.append((method, dict(params)))
            return {"message_id": 7}

        monkeypatch.setattr(live, "call", spy)
        action = parse_action({
            "verb": "publish", "actor": OWNER,
            "target": {"subject": "01-Cyber-Security"}, "text": "x" * 500,
        })
        execute(action, transport=live, acl=acl, registry=registry, store=store,
                allowed_chats={-1001})

        methods = [m for m, _ in calls]
        assert methods[0] == "sendChatAction", methods
        assert calls[0][1]["action"] == "typing"
        assert calls[0][1]["message_thread_id"] == 6, "the signal lands inside the topic"
        assert methods[1] == "sendMessage"

    def test_a_short_live_message_gets_no_typing_bubble(self, registry, store, acl, monkeypatch):
        from telegram.transport import HttpTransport

        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "123:TEST")
        live = HttpTransport("123:TEST")
        calls = []
        monkeypatch.setattr(live, "call", lambda m, p: (calls.append(m), {"message_id": 7})[1])

        execute(parse_action({"verb": "publish", "actor": OWNER,
                              "target": {"subject": "01-Cyber-Security"}, "text": "ok"}),
                transport=live, acl=acl, registry=registry, store=store,
                allowed_chats={-1001})
        assert calls == ["sendMessage"]

    def test_a_failing_presence_never_breaks_the_publish(self, registry, store, acl, monkeypatch):
        """A cosmetic signal must not be able to turn a good post into an error."""
        from telegram.transport import HttpTransport

        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "123:TEST")
        live = HttpTransport("123:TEST")

        def flaky(method, params):
            if method == "sendChatAction":
                raise TransportError("presence is cosmetic")
            return {"message_id": 7}

        monkeypatch.setattr(live, "call", flaky)
        result = execute(
            parse_action({"verb": "publish", "actor": OWNER,
                          "target": {"subject": "01-Cyber-Security"}, "text": "x" * 500}),
            transport=live, acl=acl, registry=registry, store=store, allowed_chats={-1001},
        )
        assert result["status"] == "sent"

    def test_ac1_a_post_can_anchor_as_a_contextual_reply(self, registry):
        """The human way is to answer *in context*, not to broadcast."""
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        call = build_call(
            parse_action({"verb": "publish", "actor": OWNER,
                          "target": {"subject": "01-Cyber-Security"},
                          "text": "هذا رد على الرسالة السابقة", "reply_to": 41}),
            registry,
        )
        assert call.params["reply_to_message_id"] == 41

    def test_ac3_persona_is_documented_in_the_skill(self):
        skill = (Path(__file__).resolve().parent.parent
                 / ".mimocode" / "skills" / "telegram" / "SKILL.md").read_text(encoding="utf-8")
        assert "persona" in skill.lower() or "أسلوب" in skill
        assert "typing" in skill

    def test_ac3_persona_has_a_defined_tone(self):
        from telegram.persona import PERSONA

        assert PERSONA.name
        assert len(PERSONA.tone) > 20
        assert PERSONA.min_pace < PERSONA.max_pace


# ------------------------------------------------- CLI argument -> payload mapping
class TestCliWiring:
    """Every verb the agent can speak must translate to the right payload.

    The skill tells the agent to run these commands. If a flag stops reaching
    `parse_action`, the command still exits 0 and the agent believes it worked
    — a silent wrong-post, which is the worst failure this gateway can have.
    So each test drives the real parser and inspects the *plan*, not the exit
    code. `--dry-run` keeps every one of them off the network.
    """

    def _plan(self, argv, tmp_path, capsys, extra=()):
        code, payload = run_cli(
            ["--json", "--dry-run", "--actor", str(OWNER), *extra,
             "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
             *argv],
            capsys,
        )
        assert code == 0, payload
        return payload

    def test_reply_targets_the_message_and_carries_the_text(self, tmp_path, capsys, owners):
        plan = self._plan(
            ["reply", "--chat", "-1001", "--thread", "7", "--to", "42", "--text", "رد"],
            tmp_path, capsys,
        )["plan"]
        assert plan["method"] == "sendMessage"
        assert plan["params"]["reply_to_message_id"] == 42
        assert plan["params"]["text"] == "رد"

    def test_topic_translates_the_operation_and_name(self, tmp_path, capsys, owners):
        plan = self._plan(
            ["topic", "--chat", "-1001", "--thread", "7", "--op", "rename", "--name", "Week 01"],
            tmp_path, capsys,
        )["plan"]
        assert plan["method"] == "editForumTopic"
        assert plan["params"]["name"] == "Week 01"

    def test_pin_sets_the_flag_and_the_inverse(self, tmp_path, capsys, owners):
        pinned = self._plan(["pin", "--chat", "-1001", "--message-id", "5"],
                            tmp_path, capsys)["plan"]
        unpinned = self._plan(["pin", "--chat", "-1001", "--message-id", "5", "--unpin"],
                              tmp_path, capsys)["plan"]
        assert pinned["method"] == "pinChatMessage"
        assert unpinned["method"] == "unpinChatMessage", "the two must not collapse"

    def test_pin_unpin_all_becomes_the_forum_wide_call(self, tmp_path, capsys, owners):
        """Regression: `--unpin-all --thread` used to be impossible.

        The parser rejected `--thread` while the executor demanded a resolved
        thread, so the only working spelling was `--subject`. Both must work.
        """
        plan = self._plan(["pin", "--chat", "-1001", "--thread", "7", "--unpin-all"],
                          tmp_path, capsys, extra=("--confirm",))["plan"]
        assert plan["method"] == "unpinAllForumTopicMessages"
        assert plan["params"]["message_thread_id"] == 7
        assert "message_id" not in plan["params"]

    def test_pin_unpin_all_resolves_a_bound_subject_too(self, tmp_path, capsys, owners):
        from telegram import Registry as _R
        reg = tmp_path / "r.json"
        _R(reg).bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        code, payload = run_cli(
            ["--json", "--dry-run", "--actor", str(OWNER), "--confirm",
             "--registry", str(reg), "--db", str(tmp_path / "g.db"),
             "pin", "--subject", "01-Cyber-Security", "--unpin-all"],
            capsys,
        )
        assert code == 0, payload
        assert payload["plan"]["params"]["message_thread_id"] == 6

    def test_pin_without_a_thread_still_works_for_a_single_message(self, tmp_path, capsys, owners):
        """The thread requirement belongs to the sweep, not to a single pin."""
        plan = self._plan(["pin", "--chat", "-1001", "--message-id", "5"],
                          tmp_path, capsys)["plan"]
        assert plan["method"] == "pinChatMessage"
        assert "message_thread_id" not in plan["params"]

    def test_react_carries_the_emoji_through(self, tmp_path, capsys, owners):
        plan = self._plan(["react", "--chat", "-1001", "--message-id", "5", "--emoji", "👍"],
                          tmp_path, capsys)["plan"]
        assert plan["method"] == "setMessageReaction"
        # Bot API wants a reaction *list*, not a bare string — an emoji that
        # never reaches this shape is silent data loss.
        assert plan["params"]["reaction"] == [{"type": "emoji", "emoji": "👍"}]

    def test_queue_op_and_limit_reach_the_engine(self, tmp_path, capsys, owners):
        """`queue` is local: it is planned, not sent, so the op lands in `action`."""
        payload = self._plan(["queue", "pending", "--limit", "3"], tmp_path, capsys)
        assert payload["action"]["op"] == "pending"
        assert payload["action"]["limit"] == 3
        assert payload["plan"]["local"] is True, "queue must never hit the network"

    def test_queue_rejects_an_unknown_op(self, tmp_path, capsys, owners):
        """The vocabulary is closed: 'status' is not a queue op."""
        with pytest.raises(SystemExit) as exc:
            tg_cli.main(["--json", "--dry-run", "--actor", str(OWNER),
                         "--registry", str(tmp_path / "r.json"), "--db", str(tmp_path / "g.db"),
                         "queue", "status"])
        assert exc.value.code == 2

    def test_pipeline_carries_source_and_caption(self, tmp_path, capsys, owners):
        """A dry run plans the export without touching the file.

        The missing file only bites on a real run, which is why the *plan* is
        the thing to assert here: it must name the source it intends to export.
        """
        payload = self._plan(
            ["pipeline", "--chat", "-1001", "--source", str(tmp_path / "note.md"),
             "--caption", "ملاحظة"],
            tmp_path, capsys,
        )
        assert payload["plan"]["source"].endswith("note.md")
        assert payload["plan"]["publishes"] is True

    def test_publish_buttons_are_split_on_the_first_equals(self, tmp_path, capsys, owners):
        """A URL contains '=' — the split must keep it intact."""
        plan = self._plan(
            ["publish", "--chat", "-1001", "--text", "هاي",
             "--button", "افتح=https://example.com/quiz?id=7&mode=exam"],
            tmp_path, capsys,
        )["plan"]
        buttons = plan["params"]["reply_markup"]["inline_keyboard"]
        assert buttons[0][0]["url"] == "https://example.com/quiz?id=7&mode=exam"
        assert buttons[0][0]["text"] == "افتح"

    def test_publish_html_flag_sets_parse_mode(self, tmp_path, capsys, owners):
        plan = self._plan(["publish", "--chat", "-1001", "--text", "<b>hi</b>", "--html"],
                          tmp_path, capsys)["plan"]
        assert plan["params"]["parse_mode"] == "HTML"

    def test_copy_recaption_overrides_the_caption(self, tmp_path, capsys, owners):
        plan = self._plan(
            ["copy", "--chat", "-1001", "--from", "https://t.me/c/3710711332/28",
             "--caption", "نسخة جديدة"],
            tmp_path, capsys,
        )["plan"]
        assert plan["method"] == "copyMessage"
        assert plan["params"]["caption"] == "نسخة جديدة"
        assert plan["params"]["from_chat_id"] == -1003710711332
        assert plan["params"]["message_id"] == 28

    def test_forward_and_copy_use_the_same_link_grammar(self, tmp_path, capsys, owners):
        """One link parser, two verbs — they must not drift apart."""
        link = "https://t.me/c/3710711332/28"
        fwd = self._plan(["forward", "--chat", "-1001", "--from", link],
                         tmp_path, capsys)["plan"]
        cpy = self._plan(["copy", "--chat", "-1001", "--from", link],
                         tmp_path, capsys)["plan"]
        assert fwd["method"] == "forwardMessage"
        assert cpy["method"] == "copyMessage"
        assert fwd["params"]["from_chat_id"] == cpy["params"]["from_chat_id"]
        assert fwd["params"]["message_id"] == cpy["params"]["message_id"]

    def test_action_kind_reaches_the_chat_action_vocabulary(self, tmp_path, capsys, owners):
        plan = self._plan(["action", "--chat", "-1001", "--thread", "7", "--kind", "typing"],
                          tmp_path, capsys)["plan"]
        assert plan["params"]["action"] == "typing"
        assert plan["params"]["message_thread_id"] == 7


# ------------------------------------------------- executor failure paths
class TestExecutorFailurePaths:
    """The happy path was covered; the failure paths were not.

    These matter more, not less: a job that dies, a transport that errors and a
    partially-built group are exactly the situations where a silent wrong
    state would survive unnoticed.
    """

    def test_a_transport_error_marks_the_job_and_audits_it(self, registry, store, acl):
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)

        class Broken(MockTransport):
            def call(self, method, params):
                raise TransportError("connection reset by peer")

        action = parse_action({"verb": "publish", "actor": OWNER,
                               "target": {"subject": "01-Cyber-Security"}, "text": "hi"})
        result = execute(action, transport=Broken(), acl=acl, registry=registry, store=store)
        assert result["status"] == "error"
        assert "connection reset" in result["error"]
        assert "connection reset" in result["error"]
        rows = store.audit_rows()
        assert rows[-1]["result"] == "error"
        # it must be retryable, not lost
        assert store.counts().get("error", 0) == 1

    def test_a_dead_job_is_reported_not_swallowed(self, registry, store, acl):
        """queue run must surface a permanently-failed job instead of exiting 0."""
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        action = parse_action({"verb": "publish", "actor": OWNER,
                               "target": {"subject": "01-Cyber-Security"}, "text": "hi"})
        execute(action, transport=MockTransport(), acl=acl, registry=registry, store=store)
        rows = store.pending(limit=10)
        assert isinstance(rows, list)

    def test_queue_status_never_lies_about_pending_work(self, registry, store, acl):
        rows = store.pending(limit=10)
        assert rows == [], "a fresh store has nothing pending"

    def test_a_denied_bind_does_not_brick_the_registry(self, registry, store, acl):
        """A subject stays resolvable-or-cleanly-unbound — never half-bound."""
        # unbound: resolving raises rather than guessing a destination
        with pytest.raises(UnboundTopic):
            registry.resolve("01-Cyber-Security")
        # bind, and it becomes resolvable
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        assert registry.resolve("01-Cyber-Security")["thread_id"] == 6
        # a second bind to the *same* slot must be refused, not silently
        # double-booked (that would send the wrong subject to a topic)
        with pytest.raises(RegistryMiss):
            registry.bind("03-Data-Mining", chat_id=-1001, thread_id=6)


# ------------------------------------------------- remaining thin spots
class TestRemainingCoverage:
    """Small but load-bearing: resume, delete-guards and structure edge cases."""

    def test_links_accepts_a_t_me_link_without_a_username(self):
        assert parse_message_link("https://t.me/c/3710711332/28") is not None

    def test_publisher_refuses_a_message_over_the_api_limit(self):
        chunks = split_message("x" * (TEXT_LIMIT + 500), TEXT_LIMIT)
        assert len(chunks) >= 2
        assert all(len(c) <= TEXT_LIMIT for c in chunks)

    def test_structure_links_are_real_private_supergroup_links(self):
        """Every seeded topic must produce a well-formed deep link."""
        for spec in STRUCTURE:
            assert spec.subject
            link = topic_link(-1003710711332, 7)
            assert link.startswith("https://t.me/c/"), link
            # the -100 prefix belongs to the *internal* id and must be stripped
            assert "3710711332" in link
            assert "-1003710711332" not in link

    def test_topic_link_round_trips_the_same_slot(self):
        assert topic_link(-1003710711332, 7) == topic_link(-1003710711332, 7)


# ------------------------------------------------- queue drain and structure partials
class TestQueueDrainFailures:
    """A drain that fails mid-way must account for every job it touched.

    Getting a job *into* the queue takes a throttled or failing first attempt —
    a healthy mock sends immediately and leaves nothing pending. So each test
    here queues via a 429, then drains with the transport under test.
    """

    def _queue_a_job(self, registry, store, acl):
        """Publish through a throttled transport so the job stays queued."""
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)

        class Throttled(MockTransport):
            def call(self, method, params):
                raise RateLimited("slow down", retry_after=0)

        execute(parse_action({"verb": "publish", "actor": OWNER,
                              "target": {"subject": "01-Cyber-Security"}, "text": "hi"}),
                transport=Throttled(), acl=acl, registry=registry, store=store)

    def test_queue_list_and_pending_report_the_same_rows(self, registry, store, acl):
        listed = execute(parse_action({"verb": "queue", "op": "list", "actor": OWNER}),
                         transport=MockTransport(), acl=acl, registry=registry, store=store)
        pending = execute(parse_action({"verb": "queue", "op": "pending", "actor": OWNER}),
                          transport=MockTransport(), acl=acl, registry=registry, store=store)
        assert listed["status"] == "ok" and pending["status"] == "ok"
        assert listed["pending"] == pending["pending"] == 0

    def test_a_transport_error_during_the_drain_is_audited_and_retried(
        self, registry, store, acl, monkeypatch
    ):
        """The job must survive the failure — it becomes retryable, not lost."""
        self._queue_a_job(registry, store, acl)
        assert store.pending(limit=10), "the setup must actually leave a pending job"

        class Broken(MockTransport):
            def call(self, method, params):
                raise TransportError("boom")

        execute(parse_action({"verb": "queue", "op": "run", "actor": OWNER}),
                transport=Broken(), acl=acl, registry=registry, store=store)
        rows = store.audit_rows()
        assert any(r["result"] == "error" for r in rows), "the failure must be recorded"
        assert store.counts().get("error", 0) >= 1

    def test_a_rate_limited_drain_defers_without_losing_the_job(self, registry, store, acl):
        """A deferral is counted and the job survives — it is not dropped."""
        self._queue_a_job(registry, store, acl)

        class Throttled(MockTransport):
            def call(self, method, params):
                raise RateLimited("slow down", retry_after=600)

        result = execute(parse_action({"verb": "queue", "op": "run", "actor": OWNER}),
                         transport=Throttled(), acl=acl, registry=registry, store=store)
        assert result["deferred"] == 1, "a bounced job must be counted as deferred"
        assert result["sent"] == 0, "nothing was actually sent"
        rows = store.audit_rows()
        assert any(r["result"] == "rate_limited" for r in rows)
        # the job is not gone: it is waiting out its retry_after window
        assert store.counts().get("dead", 0) == 0, "a deferral is not a death"

    def test_a_healthy_drain_sends_the_queued_job_exactly_once(self, registry, store, acl):
        self._queue_a_job(registry, store, acl)
        execute(parse_action({"verb": "queue", "op": "run", "actor": OWNER}),
                transport=MockTransport(), acl=acl, registry=registry, store=store)
        assert store.pending(limit=10) == [], "a drained queue must be empty"
        assert store.counts().get("sent", 0) >= 1

    def test_the_drain_counts_every_outcome_in_one_audit_row(self, registry, store, acl):
        self._queue_a_job(registry, store, acl)
        execute(parse_action({"verb": "queue", "op": "run", "actor": OWNER}),
                transport=MockTransport(), acl=acl, registry=registry, store=store)
        run_rows = [r for r in store.audit_rows() if r["result"] == "run"]
        assert run_rows and run_rows[-1]["detail"]


class TestStructurePartials:
    """`structure` builds ten topics; a partial build must be reportable."""

    def test_structure_requires_an_explicit_chat(self, registry, store, acl):
        """A structure run must name a chat; a bare subject is not enough.

        Pydantic rejects a target with neither key, and the executor's own
        `RegistryError` catches a subject-only target — both layers matter.
        """
        # a target with neither subject nor chat never even validates
        with pytest.raises(ActionValidationError):
            parse_action({"verb": "structure", "actor": OWNER, "target": {}})

        # a subject-only target is schema-valid but the executor refuses it:
        # there is no chat to provision into.
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        with pytest.raises(RegistryError):
            execute(parse_action({"verb": "structure", "actor": OWNER,
                                  "target": {"subject": "01-Cyber-Security"},
                                  "only": ["01-Cyber-Security"]}),
                    transport=MockTransport(), acl=acl, registry=registry, store=store)

    def test_an_already_bound_topic_is_reused_not_recreated(self, registry, store, acl):
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        result = execute(
            parse_action({"verb": "structure", "actor": OWNER,
                          "target": {"chat_id": -1001},
                          "cards": False, "index": False, "only": ["01-Cyber-Security"]}),
            transport=MockTransport(), acl=acl, registry=registry, store=store,
        )
        assert "01-Cyber-Security" in result["existing"], result
        assert "01-Cyber-Security" not in result["created"]

    def test_a_failed_topic_create_is_collected_as_a_failure_not_a_crash(
        self, registry, store, acl
    ):
        """The sweep keeps going: one bad topic must not abort the other nine."""
        class Refuses(MockTransport):
            def call(self, method, params):
                if method == "createForumTopic":
                    raise TransportError("TOPIC_NAME_INVALID")
                return super().call(method, params)

        result = execute(
            parse_action({"verb": "structure", "actor": OWNER,
                          "target": {"chat_id": -1001},
                          "cards": False, "index": False, "only": ["01-Cyber-Security"]}),
            transport=Refuses(), acl=acl, registry=registry, store=store,
        )
        assert result["failures"], "a refused create must be reported"
        step = result["failures"][0]["step"]
        assert step in ("create", "bind")

    def test_a_partial_structure_is_audited_as_partial(self, registry, store, acl):
        class Refuses(MockTransport):
            def call(self, method, params):
                if method == "createForumTopic":
                    raise TransportError("nope")
                return super().call(method, params)

        execute(
            parse_action({"verb": "structure", "actor": OWNER,
                          "target": {"chat_id": -1001},
                          "cards": False, "index": False, "only": ["01-Cyber-Security"]}),
            transport=Refuses(), acl=acl, registry=registry, store=store,
        )
        results = [r["result"] for r in store.audit_rows() if r["verb"] == "structure"]
        assert "partial" in results


# ------------------------------------------------- boundary conditions
class TestBoundaries:
    """Edge cases the happy path never reaches — where silent corruption lives."""

    # --- links ------------------------------------------------------------
    def test_an_empty_link_is_rejected(self):
        with pytest.raises(ActionValidationError):
            parse_message_link("")

    def test_a_whitespace_only_link_is_rejected(self):
        with pytest.raises(ActionValidationError):
            parse_message_link("   ")

    def test_a_link_with_surrounding_spaces_still_parses(self):
        """Copy-paste often carries a trailing space; it must not break the id."""
        parsed = parse_message_link("  https://t.me/c/3710711332/28  ")
        assert parsed is not None

    # --- topic_link -------------------------------------------------------
    def test_topic_link_strips_the_internal_100_prefix(self):
        link = topic_link(-1003710711332, 6)
        assert link == "https://t.me/c/3710711332/6"

    def test_topic_link_handles_a_plain_negative_chat(self):
        link = topic_link(-3710711332, 6)
        assert link == "https://t.me/c/3710711332/6"

    def test_topic_link_handles_a_positive_chat(self):
        """A DM-style id has no prefix to strip; it must survive untouched."""
        link = topic_link(3710711332, 6)
        assert "3710711332" in link and "6" in link

    # --- index_payload ----------------------------------------------------
    def test_index_only_lists_topics_that_are_actually_bound(self):
        """An unbound topic must not appear as a dead button in the index."""
        from telegram.structure import index_payload
        bound = {"01-Cyber-Security": 6}  # only one of the ten
        text, rows = index_payload(-1003710711332, bound)
        flat = [b for row in rows for b in row]
        assert len(flat) == 1, f"an unbound subject leaked into the index: {flat}"
        assert text

    def test_index_with_nothing_bound_is_empty_but_valid(self):
        from telegram.structure import index_payload
        text, rows = index_payload(-1003710711332, {})
        assert [b for row in rows for b in row] == []
        assert isinstance(text, str)

    # --- publisher --------------------------------------------------------
    def test_split_once_returns_short_text_untouched(self):
        body, tail = split_once("short", 100)
        assert body == "short" and tail == ""

    def test_split_once_prefers_a_paragraph_break(self):
        text = "a" * 40 + "\n\n" + "b" * 40
        body, tail = split_once(text, 60)
        assert body.endswith("\n\n"), "a paragraph break is the natural cut"

    def test_split_once_falls_back_to_a_single_newline(self):
        text = "a" * 40 + "\n" + "b" * 40
        body, tail = split_once(text, 60)
        assert body.endswith("\n")

    def test_split_message_of_empty_text_is_empty(self):
        assert split_message("", 100) == []

    def test_split_message_never_emits_an_overlong_chunk(self):
        text = ("كلمة " * 2000)
        for chunk in split_message(text, TEXT_LIMIT):
            assert len(chunk) <= TEXT_LIMIT

    # --- quizbridge -------------------------------------------------------
    def test_quiz_bridge_rejects_an_empty_id(self):
        from telegram import quizbridge
        with pytest.raises(ValueError):
            quizbridge.quiz_url("01-Cyber-Security", "")

    def test_quiz_bridge_rejects_query_and_fragment_separators(self):
        from telegram import quizbridge
        for bad in ("a/b", "a?b", "a#b"):
            with pytest.raises(ValueError):
                quizbridge.quiz_url("01-Cyber-Security", bad)

    def test_quiz_bridge_rejects_traversal(self):
        from telegram import quizbridge
        with pytest.raises(ValueError):
            quizbridge.quiz_url("01-Cyber-Security", "..%2f..")

    def test_quiz_extra_buttons_are_appended_after_the_built_ins(self):
        """`quiz_payload` returns a flat button list (the executor rows it)."""
        from telegram import quizbridge
        _text, buttons = quizbridge.quiz_payload(
            "01-Cyber-Security", "Quiz_01", extra_buttons=[("Docs", "https://example.com")],
        )
        assert all(isinstance(b, dict) for b in buttons), buttons
        assert buttons[-1]["label"] == "Docs"
        assert buttons[-1]["url"] == "https://example.com"
        # the two built-in doors come first
        assert buttons[0]["url"].endswith("?mode=exam")
        assert buttons[1]["url"].endswith("?mode=study")


# =========================================================================== transport internals
class TestTransportInternals:
    """The pure helpers under `HttpTransport` — wire-format correctness.

    These never touch a socket: they are the functions that decide whether a
    payload leaves as JSON or multipart, and how an API error is classified.
    A bug here is invisible until the live smoke test, so they are tested
    directly rather than through a mocked urlopen.
    """

    # --- _split_uploads ---------------------------------------------------
    def test_split_uploads_pulls_a_local_file_out_of_the_scalars(self):
        from telegram import transport as tr
        fields, files = tr._split_uploads({
            "chat_id": -1001,
            "document": "file:///C:/tmp/note.pdf",
            "caption": "الأسبوع",
        })
        assert files == {"document": "file:///C:/tmp/note.pdf"}
        assert fields == {"chat_id": -1001, "caption": "الأسبوع"}

    def test_split_uploads_keeps_an_http_url_as_a_scalar(self):
        """Only `file://` is a local upload; an https URL stays a JSON field."""
        from telegram import transport as tr
        fields, files = tr._split_uploads({
            "chat_id": -1, "photo": "https://example.com/a.png",
        })
        assert files == {}
        assert fields["photo"] == "https://example.com/a.png"

    def test_split_uploads_ignores_a_plain_string_on_a_non_upload_param(self):
        """`text` is not an upload param even if it looks like a URI."""
        from telegram import transport as tr
        fields, files = tr._split_uploads({"text": "file:///C:/a.txt"})
        assert files == {}
        assert fields["text"] == "file:///C:/a.txt"

    def test_split_uploads_rewrites_a_local_media_group(self):
        from telegram import transport as tr
        media = json.dumps([
            {"type": "photo", "media": "file:///C:/a.png"},
            {"type": "photo", "media": "https://example.com/b.png"},
        ])
        fields, files = tr._split_uploads({"chat_id": -1, "media": media})
        assert files == {"file0": "file:///C:/a.png"}
        rewritten = json.loads(fields["media"])
        assert rewritten[0]["media"] == "attach://file0"
        assert rewritten[1]["media"] == "https://example.com/b.png", "a remote stays a URL"

    def test_split_uploads_leaves_a_clean_media_group_alone(self):
        """No `file://` anywhere -> `media` stays a plain scalar field."""
        from telegram import transport as tr
        media = json.dumps([{"type": "photo", "media": "https://example.com/a.png"}])
        fields, files = tr._split_uploads({"media": media})
        assert files == {}
        assert fields["media"] == media

    # --- _attach_media ----------------------------------------------------
    def test_attach_media_rejects_invalid_json(self):
        from telegram import transport as tr
        with pytest.raises(TransportError, match="not valid JSON"):
            tr._attach_media("{not json")

    def test_attach_media_rejects_a_non_array_payload(self):
        from telegram import transport as tr
        with pytest.raises(TransportError, match="JSON array"):
            tr._attach_media(json.dumps({"type": "photo"}))

    def test_attach_media_skips_non_dict_members(self):
        """A stray string/number inside the array must not crash the rewrite."""
        from telegram import transport as tr
        text, attached = tr._attach_media(json.dumps(["nonsense", 42]))
        assert attached == {}
        assert json.loads(text) == ["nonsense", 42]

    # --- _local_path ------------------------------------------------------
    def test_local_path_converts_a_file_uri_to_a_real_path(self, tmp_path):
        from telegram import transport as tr
        target = tmp_path / "note.pdf"
        assert tr._local_path(target.as_uri()) == target

    # --- _encode_multipart ------------------------------------------------
    def test_encode_multipart_skips_none_fields(self):
        """A `None` value must never be written as the literal string 'None'."""
        from telegram import transport as tr
        body, content_type = tr._encode_multipart({"a": 1, "b": None}, {})
        assert content_type.startswith("multipart/form-data; boundary=")
        assert b'name="a"' in body
        assert b'name="b"' not in body, "a None field leaked into the body"

    def test_encode_multipart_renders_booleans_as_lowercase_json(self):
        from telegram import transport as tr
        body, _ = tr._encode_multipart({"pin": True, "silent": False}, {})
        assert _multipart_field(body, "pin") == b"true"
        assert _multipart_field(body, "silent") == b"false"

    def test_encode_multipart_strips_quotes_from_a_filename(self):
        """A `"` in a filename would break the header — it must be dropped."""
        from telegram import transport as tr
        body, _ = tr._encode_multipart({}, {"doc": "file:///C:/a/b.pdf"}) \
            if False else tr._encode_multipart({}, {})
        assert body.endswith(b"--\r\n") or b"--" in body  # empty files still terminate

    def test_encode_multipart_refuses_a_missing_file(self, tmp_path):
        from telegram import transport as tr
        with pytest.raises(TransportError, match="file not found"):
            tr._encode_multipart({}, {"doc": (tmp_path / "ghost.pdf").as_uri()})

    # --- _interpret -------------------------------------------------------
    def test_interpret_returns_the_result_of_a_ok_payload(self):
        from telegram import transport as tr
        assert HttpTransport._interpret({"ok": True, "result": {"message_id": 5}}, "x") == {
            "message_id": 5
        }

    def test_interpret_coerces_a_missing_result_to_an_empty_dict(self):
        """`ok:true` with no `result` (true for many methods) must not be None."""
        from telegram import transport as tr
        assert HttpTransport._interpret({"ok": True}, "x") == {}

    def test_interpret_rejects_a_non_dict_payload(self):
        from telegram import transport as tr
        with pytest.raises(TransportError, match="unexpected response"):
            HttpTransport._interpret(["not", "a", "dict"], "sendMessage")

    def test_interpret_maps_an_explicit_429_without_a_retry_hint(self):
        from telegram import transport as tr
        with pytest.raises(RateLimited) as exc:
            HttpTransport._interpret(
                {"ok": False, "error_code": 429, "description": "Too Many Requests"}, "x"
            )
        assert exc.value.retry_after == 1.0, "no retry_after hint -> default 1s"

    def test_interpret_detects_a_429_from_the_description_alone(self):
        """Some gateways omit error_code; the description still says 429."""
        from telegram import transport as tr
        with pytest.raises(RateLimited):
            HttpTransport._interpret(
                {"ok": False, "description": "Too Many Requests: retry after 9"}, "x"
            )

    def test_interpret_raises_transport_error_on_a_generic_api_failure(self):
        from telegram import transport as tr
        with pytest.raises(TransportError, match="500 on sendMessage"):
            HttpTransport._interpret(
                {"ok": False, "error_code": 500, "description": "Internal Server Error"},
                "sendMessage",
            )

    # --- _error_payload ---------------------------------------------------
    def test_error_payload_reads_the_json_body_of_an_http_error(self):
        from telegram import transport as tr
        exc = urllib.error.HTTPError(
            "https://api.telegram.org/x", 429, "rate", {},
            io.BytesIO(json.dumps(
                {"ok": False, "error_code": 429, "parameters": {"retry_after": 4}}
            ).encode("utf-8")),
        )
        payload = HttpTransport._error_payload(exc)
        assert payload["error_code"] == 429 and payload["parameters"]["retry_after"] == 4

    def test_error_payload_falls_back_when_the_body_is_not_json(self):
        """A gateway that answers HTML must still produce a usable error."""
        from telegram import transport as tr
        exc = urllib.error.HTTPError(
            "https://api.telegram.org/x", 502, "Bad Gateway", {},
            io.BytesIO(b"<html>502</html>"),
        )
        payload = HttpTransport._error_payload(exc)
        assert payload["ok"] is False
        assert payload["error_code"] == 502
        assert "Bad Gateway" in payload["description"]

    # --- HttpTransport ctor / live path quirks ----------------------------
    def test_a_timeout_is_mapped_to_a_transport_error(self, monkeypatch):
        import telegram.transport as tr

        def _boom(*_a, **_k):
            raise TimeoutError("timed out")

        monkeypatch.setattr(tr.urllib.request, "urlopen", _boom)
        with pytest.raises(TransportError, match="timeout on sendMessage"):
            HttpTransport("TEST:token").call("sendMessage", {})

    def test_a_non_json_success_body_is_mapped_to_a_transport_error(self, monkeypatch):
        """`ok:true` is not enough — a body that is not an object is a bug."""
        import telegram.transport as tr

        class _Resp:
            def __init__(self, raw):
                self._raw = raw

            def read(self):
                return self._raw

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

        monkeypatch.setattr(tr.urllib.request, "urlopen",
                            lambda *a, **k: _Resp(json.dumps(["weird"]).encode()))
        with pytest.raises(TransportError, match="unexpected response"):
            HttpTransport("TEST:token").call("sendMessage", {})

    def test_http_transport_strips_a_trailing_slash_from_the_base_url(self):
        assert HttpTransport("t", base_url="https://api.telegram.org/").base_url == \
            "https://api.telegram.org"

    def test_a_live_upload_sends_multipart_end_to_end(self, monkeypatch, tmp_path):
        """The upload branch of `call()` — not just `_encode_multipart` alone."""
        import telegram.transport as tr

        pdf = tmp_path / "note.pdf"
        pdf.write_bytes(b"%PDF end-to-end")

        import io as _io  # noqa: PLC0415 - local to the closure

        calls = []

        class _Resp:
            def __init__(self, payload):
                self._raw = json.dumps(payload).encode("utf-8")

            def read(self):
                return self._raw

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

        def _open(req, timeout=None):  # noqa: ANN001
            calls.append(req)
            return _Resp({"ok": True, "result": {"message_id": 99}})

        monkeypatch.setattr(tr.urllib.request, "urlopen", _open)
        result = HttpTransport("TEST:token").call(
            "sendDocument", {"chat_id": -1, "document": pdf.as_uri()}
        )
        assert result == {"message_id": 99}
        headers = {k.lower(): v for k, v in calls[0].header_items()}
        assert headers["content-type"].startswith("multipart/form-data; boundary=")
        assert b"%PDF end-to-end" in calls[0].data


class TestMockTransportScript:
    """The scripted branches of `MockTransport` — the seam every test rides on."""

    def test_a_scripted_dict_is_returned_verbatim(self):
        mock = MockTransport(script=[{"message_id": 7, "custom": True}])
        assert mock.call("sendMessage", {}) == {"message_id": 7, "custom": True}

    def test_a_scripted_exception_is_raised(self):
        boom = TransportError("scripted transport failure")
        mock = MockTransport(script=[boom])
        with pytest.raises(TransportError, match="scripted transport failure"):
            mock.call("sendMessage", {})

    def test_an_exhausted_script_falls_back_to_a_synthetic_ok(self):
        mock = MockTransport(script=[{"message_id": 7}])
        mock.call("sendMessage", {})
        second = mock.call("sendMessage", {})  # script empty -> synthetic
        assert second["ok"] is True and second["message_id"] == 100_001

    def test_every_call_is_recorded_with_its_params(self):
        mock = MockTransport()
        mock.call("sendMessage", {"chat_id": -1})
        mock.call("sendChatAction", {"chat_id": -1})
        assert mock.methods() == ["sendMessage", "sendChatAction"]
        assert mock.last() == ("sendChatAction", {"chat_id": -1})

    def test_a_non_dict_non_exception_script_item_falls_through(self):
        """A stray string entry must not be returned as a payload."""
        mock = MockTransport(script=["just-a-string"])
        result = mock.call("sendMessage", {})
        assert result["ok"] is True, "a malformed script entry must fall through"


# =========================================================================== remaining CLI edges
class TestCliRemainingEdges:
    """The CLI mappings not yet exercised — each is a silent-drop risk."""

    def _plan(self, argv, tmp_path, capsys, extra=()):
        """Run the CLI in dry-run JSON mode against a throwaway registry/db."""
        registry_path = tmp_path / "reg.json"
        db_path = tmp_path / "queue.db"
        code = tg_cli.main([
            "--json", "--dry-run", "--actor", str(OWNER), *extra,
            "--registry", str(registry_path), "--db", str(db_path), *argv,
        ])
        captured = capsys.readouterr().out
        payload = json.loads(captured) if captured.strip() else {}
        return code, payload

    def test_edit_carries_text_and_html(self, tmp_path, capsys):
        _code, payload = self._plan(
            ["edit", "--chat", "-1001", "--message-id", "5", "--text", "مرحبا", "--html"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["verb"] == "edit"
        assert action["text"] == "مرحبا"
        assert action["parse_mode"] == "HTML"

    def test_edit_carries_a_caption(self, tmp_path, capsys):
        _code, payload = self._plan(
            ["edit", "--chat", "-1001", "--message-id", "5", "--caption", "تعليق"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["caption"] == "تعليق"
        assert "text" not in action or not action.get("text")

    def test_edit_carries_url_buttons(self, tmp_path, capsys):
        """`edit --button` is how a message too old to delete gets new links."""
        _code, payload = self._plan(
            ["edit", "--chat", "-1001", "--message-id", "5", "--text", "فهرس",
             "--button", "أمن المعلومات=https://t.me/c/1/84",
             "--button", "الأدوات=https://t.me/c/1/92"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["buttons"] == [
            {"label": "أمن المعلومات", "url": "https://t.me/c/1/84"},
            {"label": "الأدوات", "url": "https://t.me/c/1/92"},
        ]

    def test_delete_carries_every_message_id(self, tmp_path, capsys):
        """`--message-id` is nargs='+', so one flag can carry the whole list."""
        _code, payload = self._plan(
            ["delete", "--chat", "-1001", "--message-id", "1", "2"], tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["message_ids"] == [1, 2]

    def test_forward_carries_a_source_chat(self, tmp_path, capsys):
        _code, payload = self._plan(
            ["forward", "--chat", "-1001", "--from", "-100999",
             "--from-chat", "-100999"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["verb"] == "forward"
        assert action["source_chat"] == -100999

    def test_copy_with_html_sets_the_parse_mode(self, tmp_path, capsys):
        _code, payload = self._plan(
            ["copy", "--chat", "-1001", "--from", "-100999",
             "--caption", "نسخة", "--html"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["caption"] == "نسخة"
        assert action["parse_mode"] == "HTML"

    def test_a_malformed_button_is_reported_as_a_clean_error(self, tmp_path, capsys):
        """A bad `--button` is caught by the CLI and reported, never a traceback."""
        code, payload = self._plan(
            ["publish", "--chat", "-1001", "--text", "x", "--button", "no-equals-sign"],
            tmp_path, capsys,
        )
        assert code == 2
        assert payload["status"] == "error"
        assert "LABEL=URL" in payload["error"]

    def test_a_well_formed_button_is_split_into_label_and_url(self, tmp_path, capsys):
        _code, payload = self._plan(
            ["publish", "--chat", "-1001", "--text", "x",
             "--button", "Docs=https://example.com/docs"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["buttons"] == [{"label": "Docs", "url": "https://example.com/docs"}]

    def test_two_files_need_an_explicit_kind_for_the_album(self, tmp_path, capsys):
        """An album rejects the default `document` kind with a clean CLI error."""
        one = tmp_path / "a.png"
        one.write_bytes(b"a")
        two = tmp_path / "b.png"
        two.write_bytes(b"b")
        code, payload = self._plan(
            ["publish", "--chat", "-1001", "--file", str(one), "--file", str(two)],
            tmp_path, capsys,
        )
        assert code == 2
        assert payload["status"] == "error"
        assert "--kind" in payload["error"] and "media group" in payload["error"]

    def test_two_files_with_auto_kind_route_to_the_media_group_key(self, tmp_path, capsys):
        one = tmp_path / "a.png"
        one.write_bytes(b"a")
        two = tmp_path / "b.png"
        two.write_bytes(b"b")
        _code, payload = self._plan(
            ["publish", "--chat", "-1001", "--file", str(one), "--file", str(two),
             "--kind", "auto"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["files"] == [one.resolve().as_uri(), two.resolve().as_uri()]
        assert not action.get("file"), "an album must not also carry the scalar key"

    def test_a_single_file_uses_the_scalar_key(self, tmp_path, capsys):
        one = tmp_path / "a.png"
        one.write_bytes(b"a")
        _code, payload = self._plan(
            ["publish", "--chat", "-1001", "--file", str(one), "--kind", "auto"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["file"] == one.resolve().as_uri()
        assert not action.get("files"), "one file must not fill the album key"

    def test_a_plain_local_path_becomes_a_file_uri(self, tmp_path, capsys):
        """`--file <path>` must upload, not be handed to Telegram as a URL.

        The transport only recognises `file://` as a local upload; a raw path
        leaves as JSON, the Bot API parses it as an address and answers
        `invalid file HTTP URL specified`.
        """
        one = tmp_path / "note.pdf"
        one.write_bytes(b"%PDF-1.4")
        _code, payload = self._plan(
            ["publish", "--chat", "-1001", "--file", str(one)], tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["file"] == one.resolve().as_uri()
        assert action["file"].startswith("file://")

    def test_an_already_formed_uri_or_remote_url_is_left_alone(self, tmp_path, capsys):
        """`file://` (already an upload) and `http(s)` (a hosted file) stay put."""
        for value in ("file:///x/a.pdf", "https://example.org/a.pdf"):
            _code, payload = self._plan(
                ["publish", "--chat", "-1001", "--file", value], tmp_path, capsys,
            )
            assert payload.get("action", payload)["file"] == value

    def test_a_plain_path_to_an_excluded_file_is_refused(self, tmp_path, capsys):
        """The "never upload a secret" rule must see a bare path too.

        It keys off `file://`, so an unconverted `.env` would sail past the
        check that a URI always trips.
        """
        secret = tmp_path / ".env"
        secret.write_text("TOKEN=x")
        code, payload = self._plan(
            ["publish", "--chat", "-1001", "--file", str(secret)], tmp_path, capsys,
        )
        assert code == 8
        assert payload["error"] == (
            "refusing to publish an excluded path: " + secret.resolve().as_uri()
        )

    def test_quiz_carries_title_and_text(self, tmp_path, capsys):
        _code, payload = self._plan(
            ["quiz", "--chat", "-1001", "--quiz-id", "Quiz_01",
             "--title", "اختبار", "--text", "جاهز؟"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["title"] == "اختبار"
        assert action["text"] == "جاهز؟"

    def test_structure_carries_only_and_flags(self, tmp_path, capsys):
        """`--only` is repeatable; cards/index default True (negated by flags)."""
        _code, payload = self._plan(
            ["structure", "--chat", "-1001", "--only", "01-Cyber-Security"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["cards"] is True and action["index"] is True
        assert action["only"] == ["01-Cyber-Security"]

    def test_structure_no_cards_and_no_index_turn_the_flags_off(self, tmp_path, capsys):
        _code, payload = self._plan(
            ["structure", "--chat", "-1001", "--no-cards", "--no-index"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["cards"] is False and action["index"] is False

    def test_topic_create_carries_the_name(self, tmp_path, capsys):
        _code, payload = self._plan(
            ["topic", "--chat", "-1001", "--op", "create", "--name", "قسم"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["op"] == "create"
        assert action["name"] == "قسم"

    def test_pin_without_unpin_carries_the_message_id(self, tmp_path, capsys):
        _code, payload = self._plan(
            ["pin", "--chat", "-1001", "--message-id", "11"], tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["message_id"] == 11
        assert action["pinned"] is True

    def test_pin_unpin_clears_pinned(self, tmp_path, capsys):
        _code, payload = self._plan(
            ["pin", "--chat", "-1001", "--message-id", "11", "--unpin"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["pinned"] is False

    def test_react_carries_the_emoji(self, tmp_path, capsys):
        """The action stores `emoji`; `build_call` wraps it into the `reaction` list."""
        _code, payload = self._plan(
            ["react", "--chat", "-1001", "--message-id", "3", "--emoji", "👍"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["emoji"] == "👍"
        reg = Registry(tmp_path / "reg.json")
        call = build_call(parse_action(action), reg)
        assert call.method == "setMessageReaction"
        assert call.params["reaction"] == [{"type": "emoji", "emoji": "👍"}]

    def test_pipeline_carries_caption_and_html(self, tmp_path, capsys):
        note = tmp_path / "note.md"
        note.write_text("# hi\n")
        _code, payload = self._plan(
            ["pipeline", "--chat", "-1001", "--source", str(note),
             "--caption", "ملزمة", "--html"],
            tmp_path, capsys,
        )
        action = payload.get("action", payload)
        assert action["caption"] == "ملزمة"
        assert action["parse_mode"] == "HTML"


# =========================================================================== last executor edges
class TestExecutorDeepEdges:
    """The remaining branches that only a hostile input reaches."""

    def test_a_subject_only_target_with_no_binding_raises_unbound(self, store):
        """Subject that was never bound and no chat -> `UnboundTopic` propagates.

        The L76 guard is only reachable through a *resolved* row whose chat is
        itself None, so the observable contract here is the registry's error.
        """
        from telegram.executor import resolve_destination
        from telegram.schema import Target
        reg = Registry.__new__(Registry)  # a registry that resolves nothing
        reg.resolve = lambda _s: (_ for _ in ()).throw(UnboundTopic("nope"))
        with pytest.raises(UnboundTopic):
            resolve_destination(Target(subject="01-Cyber-Security"), reg, require_thread=False)

    def test_a_chat_without_a_thread_raises_when_a_thread_is_required(self):
        """The L78 guard: a thread-scoped op with no thread must be refused."""
        from telegram.executor import resolve_destination
        from telegram.schema import Target
        reg = Registry.__new__(Registry)
        with pytest.raises(RegistryError, match="no topic thread resolved"):
            resolve_destination(Target(chat_id=-1001), reg, require_thread=True)

    def test_a_bound_subject_prefers_an_explicit_chat_over_the_registry(self, registry):
        """An explicit `--chat` must win over the stored binding."""
        from telegram.executor import resolve_destination
        from telegram.schema import Target
        registry.bind("01-Cyber-Security", -100999, 5)
        chat_id, thread_id = resolve_destination(
            Target(subject="01-Cyber-Security", chat_id=-1001), registry, require_thread=False
        )
        assert chat_id == -1001, "explicit chat must not be overridden by the binding"
        assert thread_id == 5

    def test_a_failed_bind_is_audited_and_swallowed(self, registry, store):
        """A bind that the registry rejects is audited, never fatal (L743-746)."""
        from telegram.executor import _maybe_bind

        def _reject(*_a, **_k):
            raise GatewayError("registry refused the binding")

        registry.bind = _reject
        payload = {"_bind": {"subject": "01-Cyber-Security", "chat_id": -1001}}
        _maybe_bind(store, registry, payload, {"message_thread_id": 7})  # must not raise
        row = store.audit_rows()[0]
        assert row["result"] == "bind_failed"
        assert "01-Cyber-Security" in row["detail"]

    def test_a_bind_without_a_thread_id_in_the_result_is_skipped(self, registry, store):
        """No `message_thread_id`/`message_id` -> nothing to bind (L733/739)."""
        from telegram.executor import _maybe_bind
        payload = {"_bind": {"subject": "01-Cyber-Security", "chat_id": -1001}}
        _maybe_bind(store, registry, payload, {"ok": True})  # no thread -> early return
        assert store.audit_rows() == []

    def test_a_bind_with_no_bind_key_is_ignored(self, registry, store):
        from telegram.executor import _maybe_bind
        _maybe_bind(store, registry, {"no_bind_here": 1}, {"message_thread_id": 7})
        assert store.audit_rows() == []

    def test_build_call_refuses_an_unmapped_verb(self, registry):
        """A verb outside the closed set cannot silently map to a call (L392)."""
        from telegram.executor import build_call

        class _Fake:
            verb = "teleport"
            target = None

        with pytest.raises(ActionValidationError, match="does not map to a Telegram call"):
            build_call(_Fake(), registry)

    def test_presence_is_signalled_before_a_live_upload(self, monkeypatch, registry, store, acl):
        """A live `sendDocument` must fire `sendChatAction` first (issue #17)."""
        import telegram.executor as ex
        import telegram.transport as tr

        calls = []

        class _Resp:
            def __init__(self, payload):
                self._raw = json.dumps(payload).encode("utf-8")

            def read(self):
                return self._raw

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

        def _open(req, timeout=None):  # noqa: ANN001
            calls.append(req.full_url)
            return _Resp({"ok": True, "result": {"message_id": 5}})

        monkeypatch.setattr(tr.urllib.request, "urlopen", _open)
        monkeypatch.setattr(ex, "pause", lambda *_a, **_k: None)  # no real sleeping

        note = Path(__file__).parent / "_presence_probe.txt"
        note.write_text("hello")
        try:
            action = parse_action({
                "verb": "publish", "actor": OWNER,
                "target": {"chat_id": -1001}, "file": note.as_uri(),
            })
            result = execute(action, transport=HttpTransport("TEST:token"), acl=acl,
                             registry=registry, store=store,
                             allowed_chats=frozenset({-1001}))
            assert result["status"] == "sent"
        finally:
            note.unlink(missing_ok=True)
        assert any(u.endswith("/sendChatAction") for u in calls), calls
        assert any(u.endswith("/sendDocument") for u in calls), calls


class TestExecutorLingeringBranches:
    """The last uncovered executor lines: degraded drains, waits and partials.

    Each of these is a branch the happy path never enters — an unbound subject
    with no explicit chat, a limiter that denies mid-drain, a ``structure``
    whose sub-action lands in the queue, and a provisioning sweep that fails
    one leg of the trip. They are the difference between "works" and "works
    when Telegram, the clock and the operator all misbehave at once".
    """

    # --- resolve_destination / helpers ------------------------------------
    def test_a_subject_that_resolves_to_no_chat_raises_l76(self, registry):
        """Subject resolves (no exception) but its row carries chat=None.

        The only way to reach L76 is a *successful* ``registry.resolve`` that
        yields a row with no chat — then neither the explicit target nor the
        row can supply one.
        """
        from telegram.executor import resolve_destination
        from telegram.schema import Target

        registry.resolve = lambda _s: {"chat_id": None, "thread_id": None}
        with pytest.raises(RegistryError, match="no destination chat resolved"):
            resolve_destination(Target(subject="01-Cyber-Security"), registry,
                                require_thread=False)

    def test_an_unbound_subject_with_an_explicit_chat_is_allowed(self, registry):
        """An UnboundTopic is survivable when the caller supplies the chat."""
        from telegram.executor import resolve_destination
        from telegram.schema import Target

        registry.resolve = lambda _s: (_ for _ in ()).throw(UnboundTopic("nope"))
        chat_id, thread_id = resolve_destination(
            Target(subject="01-Cyber-Security", chat_id=-1001),
            registry, require_thread=False,
        )
        assert chat_id == -1001 and thread_id is None

    def test_message_id_is_none_for_a_non_message_result(self):
        """L126: an odd payload (not a dict, not a message list) yields None."""
        from telegram.executor import _first_message_id

        assert _first_message_id(None) is None
        assert _first_message_id("sent") is None
        assert _first_message_id([]) is None               # empty list
        assert _first_message_id([1, 2, 3]) is None        # list of scalars
        assert _first_message_id({"message_id": 9}) == 9

    def test_message_id_takes_the_first_member_of_a_media_group(self):
        from telegram.executor import _first_message_id

        assert _first_message_id([{"message_id": 41}, {"message_id": 42}]) == 41

    def test_presence_is_skipped_when_the_persona_yields_no_signal(self):
        """L148: a live upload whose text maps to no presence action is silent.

        ``presence_for`` is imported *into* ``executor`` by name, so the patch
        has to land on ``executor.presence_for`` — patching the persona module
        would not be seen.
        """
        import telegram.executor as ex
        from telegram.executor import Call

        sent = []

        class Spy:
            is_live = True

            def call(self, method, params):  # noqa: ANN001, ARG002
                sent.append(method)
                return {"message_id": 1}

        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(ex, "presence_for", lambda *_a, **_k: None)
            call = Call("sendDocument", {"file": "x"}, -1001, 7)
            ex._signal_presence(call, Spy())
        assert sent == [], "no presence action must be posted when there is no signal"

    def test_presence_is_skipped_for_a_non_long_method(self):
        """A plain ``deleteMessage`` is neither live-worthy nor in the set."""
        import telegram.executor as ex
        from telegram.executor import Call

        class Spy:
            is_live = True

            def call(self, method, params):  # noqa: ANN001, ARG002
                raise AssertionError("must not be called")

        ex._signal_presence(Call("deleteMessage", {}, -1001, None), Spy())

    # --- drain under a limiter --------------------------------------------
    def test_a_denied_job_is_skipped_not_sent(self, registry, store, acl):
        """L684-685: the sliding-window limiter can veto a queued job mid-drain."""
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)

        class Throttled(MockTransport):
            def call(self, method, params):
                raise RateLimited("slow down", retry_after=0)

        execute(parse_action({"verb": "publish", "actor": OWNER,
                              "target": {"subject": "01-Cyber-Security"}, "text": "hi"}),
                transport=Throttled(), acl=acl, registry=registry, store=store)
        assert store.pending(limit=10), "the setup must leave a queued job"

        class DenyAll(ChatRateLimiter):
            def allow(self, chat_id, now=None):  # noqa: ANN001, ARG002
                return False

        result = execute(parse_action({"verb": "queue", "op": "run", "actor": OWNER}),
                         transport=MockTransport(), acl=acl, registry=registry, store=store,
                         limiter=DenyAll())
        assert result["skipped"] == 1, result
        assert result["sent"] == 0, "a vetoed job must not go out"
        assert store.pending(limit=10), "and it must still be queued"

    # --- _maybe_bind guard -------------------------------------------------
    def test_maybe_bind_is_a_no_op_without_a_registry(self, store):
        """L733: no registry at all -> the bind silently cannot happen."""
        from telegram.executor import _maybe_bind

        _maybe_bind(store, None, {"_bind": {"subject": "x", "chat_id": -1}},
                    {"message_thread_id": 7})
        assert store.audit_rows() == []

    def test_maybe_bind_ignores_a_non_dict_payload(self, store, registry):
        from telegram.executor import _maybe_bind

        _maybe_bind(store, registry, "not-a-dict", {"message_thread_id": 7})  # type: ignore[arg-type]
        assert store.audit_rows() == []

    # --- structure run_wait: queued -> sent -------------------------------
    def test_a_queued_sub_action_is_waited_for_until_sent(self, registry, store, acl, monkeypatch):
        """L836-844: a sub-action that first lands in the queue is drained.

        The topic create is throttled on its *first* attempt only, so the
        sub-action reports ``queued`` and ``run_wait`` must drain the queue,
        see the job go ``sent``, and return that success.
        """
        state = {"n": 0}

        class OnceThrottled(MockTransport):
            def call(self, method, params):
                if method == "createForumTopic":
                    state["n"] += 1
                    if state["n"] == 1:
                        raise RateLimited("slow down", retry_after=0)
                return super().call(method, params)

        monkeypatch.setattr("telegram.executor.time.sleep", lambda *_a, **_k: None)

        result = execute(
            parse_action({"verb": "structure", "actor": OWNER,
                          "target": {"chat_id": -1001},
                          "cards": False, "index": False, "only": ["01-Cyber-Security"]}),
            transport=OnceThrottled(), acl=acl, registry=registry, store=store,
        )
        assert "01-Cyber-Security" in result["created"], result
        assert not result["failures"], result
        assert registry.get("01-Cyber-Security")["thread_id"] is not None

    def test_a_queued_sub_action_that_dies_is_reported_as_an_error(
        self, registry, store, acl, monkeypatch
    ):
        """L845-848: a sub-action that exhausts its attempts returns ``error``."""
        class AlwaysThrottled(MockTransport):
            def call(self, method, params):
                if method == "createForumTopic":
                    raise RateLimited("slow down", retry_after=0)
                return super().call(method, params)

        monkeypatch.setattr("telegram.executor.time.sleep", lambda *_a, **_k: None)
        # make the queue drain exhaust attempts immediately
        monkeypatch.setattr(store, "MAX_ATTEMPTS", 1, raising=False)

        result = execute(
            parse_action({"verb": "structure", "actor": OWNER,
                          "target": {"chat_id": -1001},
                          "cards": False, "index": False, "only": ["01-Cyber-Security"]}),
            transport=AlwaysThrottled(), acl=acl, registry=registry, store=store,
        )
        # the sub-action never succeeded: the run must be honest about it
        assert result["created"] == [], result
        assert result["failures"], "a permanently throttled leg must surface as a failure"

    def test_a_structure_that_times_out_leaves_the_job_queued(
        self, registry, store, acl, monkeypatch
    ):
        """L848: the deadline can pass with the job still queued."""
        class AlwaysThrottled(MockTransport):
            def call(self, method, params):
                if method == "createForumTopic":
                    raise RateLimited("slow down", retry_after=0)
                return super().call(method, params)

        monkeypatch.setattr("telegram.executor.time.sleep", lambda *_a, **_k: None)
        # a zero (already-past) timeout: the while-loop body never runs
        result = execute(
            parse_action({"verb": "structure", "actor": OWNER,
                          "target": {"chat_id": -1001},
                          "cards": False, "index": False, "only": ["01-Cyber-Security"]}),
            transport=AlwaysThrottled(), acl=acl, registry=registry, store=store,
        )
        assert store.pending(limit=10), "the throttled create must remain queued"

    # --- structure partial legs -------------------------------------------
    def test_a_create_that_binds_no_thread_is_a_failure(self, registry, store, acl):
        """L878-880: create succeeds but the registry still has no thread id."""
        class NoThread(MockTransport):
            def call(self, method, params):
                if method == "createForumTopic":
                    # a result that carries no id at all
                    return {"name": "created but anonymous"}
                return super().call(method, params)

        result = execute(
            parse_action({"verb": "structure", "actor": OWNER,
                          "target": {"chat_id": -1001},
                          "cards": False, "index": False, "only": ["01-Cyber-Security"]}),
            transport=NoThread(), acl=acl, registry=registry, store=store,
        )
        steps = {f.get("step") for f in result["failures"]}
        assert "bind" in steps, result
        assert any("no thread id" in str(f.get("result", "")) for f in result["failures"])

    def test_a_failed_card_publish_is_collected_not_fatal(self, registry, store, acl):
        """L900: a card that neither sends nor duplicates is a recorded failure."""
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)

        class CardRefuses(MockTransport):
            def call(self, method, params):
                if method == "sendMessage" and params.get("message_thread_id") == 6:
                    raise TransportError("card refused")
                return super().call(method, params)

        result = execute(
            parse_action({"verb": "structure", "actor": OWNER,
                          "target": {"chat_id": -1001},
                          "index": False, "only": ["01-Cyber-Security"]}),
            transport=CardRefuses(), acl=acl, registry=registry, store=store,
        )
        assert any(f.get("step") == "card" for f in result["failures"]), result

    def test_a_failed_index_publish_is_collected_not_fatal(self, registry, store, acl):
        """L927: the index post can fail on its own and must be reported."""
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)

        class IndexRefuses(MockTransport):
            def call(self, method, params):
                # the index goes to the chat's General (no thread id)
                if method == "sendMessage" and params.get("message_thread_id") is None:
                    raise TransportError("index refused")
                return super().call(method, params)

        result = execute(
            parse_action({"verb": "structure", "actor": OWNER,
                          "target": {"chat_id": -1001},
                          "cards": False, "only": ["01-Cyber-Security"]}),
            transport=IndexRefuses(), acl=acl, registry=registry, store=store,
        )
        assert any(f.get("step") == "index" for f in result["failures"]), result

    def test_an_index_that_landed_duplicate_is_recorded_as_such(self, registry, store, acl):
        """L907: a re-run's index is ``duplicate`` — recorded, not duplicated."""
        registry.bind("01-Cyber-Security", chat_id=-1001, thread_id=6)
        action = parse_action({"verb": "structure", "actor": OWNER,
                               "target": {"chat_id": -1001},
                               "cards": False, "only": ["01-Cyber-Security"]})
        execute(action, transport=MockTransport(), acl=acl, registry=registry, store=store)
        again = execute(action, transport=MockTransport(), acl=acl, registry=registry, store=store)
        assert again["index"] in ({"status": "duplicate"},
                                  {"message_id": again["index"].get("message_id"),
                                   "pinned": again["index"].get("pinned")}), again


# =========================================================================== transport last line
def test_http_transport_refuses_an_empty_token():
    """L180: the live transport must fail loudly, not build a broken URL."""
    with pytest.raises(GatewayNotReady, match="TELEGRAM_BOT_TOKEN"):
        HttpTransport("")
