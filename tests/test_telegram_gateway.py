"""Tests for the Telegram gateway offline core (roadmap gate G1, issues #8-#16/#21).

SP1 of the roadmap: the G1 code must be provably network-free. Every test here
runs against the mock transport with registry/store files in tmp_path, and the
suite asserts the structural guarantees (fail-closed ACL, confirmation gate,
idempotency, audit trail, no live transport).
"""

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

from telegram import ACL, MockTransport, Registry, Store, execute, parse_action, plan  # noqa: E402
from telegram import cli as tg_cli  # noqa: E402
from telegram import pipeline as pipeline_mod  # noqa: E402
from telegram.acl import chat_allowlist_from_env  # noqa: E402
from telegram.errors import (  # noqa: E402
    AccessDenied,
    ActionValidationError,
    ConfirmationRequired,
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
