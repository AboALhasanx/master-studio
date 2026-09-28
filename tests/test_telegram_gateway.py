"""Tests for the Telegram gateway offline core (roadmap gate G1, issues #8-#16/#21).

SP1 of the roadmap: the G1 code must be provably network-free. Every test here
runs against the mock transport with registry/store files in tmp_path, and the
suite asserts the structural guarantees (fail-closed ACL, confirmation gate,
idempotency, audit trail, no live transport).
"""

import io
import json
import sys
import time
import urllib.error
from pathlib import Path

import pytest

# Ensure 90_Shared_Toolbox is on sys.path (same pattern as test_sieve_client)
toolbox_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox"
if str(toolbox_path) not in sys.path:
    sys.path.insert(0, str(toolbox_path))

from telegram import ACL, MockTransport, Registry, Store, execute, parse_action, plan  # noqa: E402
from telegram import cli as tg_cli  # noqa: E402
from telegram.acl import chat_allowlist_from_env  # noqa: E402
from telegram.errors import (  # noqa: E402
    AccessDenied,
    ActionValidationError,
    ConfirmationRequired,
    GatewayNotReady,
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
