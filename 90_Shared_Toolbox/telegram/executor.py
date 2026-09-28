"""Planner + executor: turns a validated action into Bot API calls (issues #9/#14).

Flow of :func:`execute`::

    ACL authorize -> resolve destination via registry -> build Bot API call
        -> idempotency gate (SQLite) -> rate limiter -> transport.call
        -> mark job + audit

Nothing here performs HTTP at gate G1: the injected transport is the mock.
``plan()`` is the pure, side-effect-free half used by ``--dry-run``.
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from typing import Any

from .acl import ACL
from .schema import parse_action
from .structure import STRUCTURE, card_text, index_payload
from .errors import (
    AccessDenied,
    ActionValidationError,
    GatewayError,
    RateLimited,
    RegistryError,
    TransportError,
    UnboundTopic,
)
from .links import parse_message_link
from .publisher import TEXT_LIMIT, split_message, split_once
from .registry import Registry
from .schema import Action, DeleteAction, PublishAction, ReactAction, ReplyAction, TopicAction, idempotency_key
from .store import ChatRateLimiter, Store, backoff_delay
from .transport import Transport

__all__ = ["Call", "build_call", "plan", "execute", "resolve_destination"]


@dataclass(frozen=True)
class Call:
    method: str
    params: dict[str, Any]
    chat_id: int | None
    thread_id: int | None


def resolve_destination(
    target, registry: Registry, *, require_thread: bool
) -> tuple[int, int | None]:
    """Resolve ``(chat_id, thread_id)`` from an explicit target and the registry.

    Unbound subjects raise :class:`UnboundTopic` — the gateway never guesses a
    destination (issue #8). ``require_thread`` is false for ``topic create``
    (no thread exists yet) and for posts into the General topic.
    """
    chat_id = target.chat_id
    thread_id = target.thread_id

    if target.subject is not None:
        try:
            row = registry.resolve(target.subject)
        except UnboundTopic:
            if chat_id is None or require_thread:
                raise
        else:
            chat_id = chat_id if chat_id is not None else row["chat_id"]
            thread_id = thread_id if thread_id is not None else row["thread_id"]

    if chat_id is None:
        raise RegistryError("no destination chat resolved (bind the subject or pass chat_id)")
    if require_thread and thread_id is None:
        raise RegistryError(
            "no topic thread resolved (bind the subject in the registry or pass thread_id)"
        )
    return int(chat_id), (int(thread_id) if thread_id is not None else None)


def _chunk_params(params: dict[str, Any]) -> tuple[dict[str, Any], str | None]:
    """Trim ``params['text']`` to the API limit, returning the unsent tail.

    Used by both :func:`execute` and the queue drain, so a 20 000-character
    digest is posted as several messages under **one** idempotency key: the
    already-sent part is never re-sent (issue #11).
    """
    text = params.get("text")
    if not isinstance(text, str) or len(text) <= TEXT_LIMIT:
        return params, None
    head, tail = split_once(text)
    return {**params, "text": head}, tail


def build_call(action: Action, registry: Registry) -> Call:
    """Pure translation of a validated action into one Bot API call."""
    verb = action.verb

    if verb == "publish":
        assert isinstance(action, PublishAction)
        chat_id, thread_id = resolve_destination(action.target, registry, require_thread=False)
        params: dict[str, Any] = {"chat_id": chat_id}
        if thread_id is not None:
            params["message_thread_id"] = thread_id
        if action.reply_to is not None:
            params["reply_to_message_id"] = action.reply_to
        if action.text is not None:
            method = "sendMessage"
            params["text"] = action.text
        else:
            method = "sendDocument"
            params["document"] = action.file
            params["caption"] = action.caption or ""
        if action.parse_mode is not None:
            params["parse_mode"] = action.parse_mode
        if action.buttons:
            params["reply_markup"] = {
                "inline_keyboard": [[{"text": b.label, "url": b.url}] for b in action.buttons]
            }
        return Call(method, params, chat_id, thread_id)

    if verb == "reply":
        assert isinstance(action, ReplyAction)
        chat_id, thread_id = resolve_destination(action.target, registry, require_thread=False)
        ref = parse_message_link(action.to)
        if ref.chat_id is not None and ref.chat_id != chat_id:
            raise ActionValidationError(
                f"message link belongs to chat {ref.chat_id}, but target resolves to {chat_id}"
            )
        return Call(
            "sendMessage",
            {"chat_id": chat_id, "text": action.text, "reply_to_message_id": ref.message_id},
            chat_id,
            thread_id,
        )

    if verb == "edit":
        chat_id, thread_id = resolve_destination(action.target, registry, require_thread=False)
        return Call(
            "editMessageText",
            {"chat_id": chat_id, "message_id": action.message_id, "text": action.text},
            chat_id,
            thread_id,
        )

    if verb == "delete":
        assert isinstance(action, DeleteAction)
        chat_id, thread_id = resolve_destination(action.target, registry, require_thread=False)
        return Call(
            "deleteMessages",
            {"chat_id": chat_id, "message_ids": list(action.message_ids)},
            chat_id,
            thread_id,
        )

    if verb == "pin":
        chat_id, thread_id = resolve_destination(action.target, registry, require_thread=False)
        method = "pinChatMessage" if action.pinned else "unpinChatMessage"
        return Call(method, {"chat_id": chat_id, "message_id": action.message_id}, chat_id, thread_id)

    if verb == "react":
        assert isinstance(action, ReactAction)
        chat_id, thread_id = resolve_destination(action.target, registry, require_thread=False)
        return Call(
            "setMessageReaction",
            {
                "chat_id": chat_id,
                "message_id": action.message_id,
                "reaction": [{"type": "emoji", "emoji": action.emoji}],
            },
            chat_id,
            thread_id,
        )

    if verb == "topic":
        assert isinstance(action, TopicAction)
        need_thread = action.op != "create"
        chat_id, thread_id = resolve_destination(
            action.target, registry, require_thread=need_thread
        )
        if action.op == "create":
            params = {"chat_id": chat_id, "name": action.name}
            if action.icon_color is not None:
                params["icon_color"] = action.icon_color
            return Call("createForumTopic", params, chat_id, None)
        params = {"chat_id": chat_id, "message_thread_id": thread_id}
        if action.op == "rename":
            params["name"] = action.name
            method = "editForumTopic"
        elif action.op == "close":
            method = "closeForumTopic"
        elif action.op == "reopen":
            method = "reopenForumTopic"
        else:  # delete
            method = "deleteForumTopic"
        return Call(method, params, chat_id, thread_id)

    raise ActionValidationError(f"verb '{verb}' does not map to a Telegram call")


def plan(action: Action, registry: Registry) -> dict[str, Any]:
    """Side-effect-free preview used by ``--dry-run`` (no ACL, no writes)."""
    if action.verb == "structure":
        from .structure import STRUCTURE as _STRUCTURE

        chat_id = action.target.chat_id
        to_create, bound = [], []
        for spec in _STRUCTURE:
            if action.only and spec.subject not in action.only:
                continue
            row = registry.get(spec.subject)
            (bound if row.get("thread_id") is not None else to_create).append(spec.subject)
        return {
            "verb": action.verb,
            "destructive": False,
            "chat_id": chat_id,
            "create": to_create,
            "already_bound": bound,
            "cards": action.cards,
            "index": action.index,
            "idempotency_key": idempotency_key(action),
        }
    if action.verb in ("status", "queue"):
        return {
            "verb": action.verb,
            "destructive": False,
            "local": True,
            "idempotency_key": idempotency_key(action),
        }
    call = build_call(action, registry)
    return {
        "verb": action.verb,
        "destructive": action.destructive(),
        "method": call.method,
        "chat_id": call.chat_id,
        "thread_id": call.thread_id,
        "params": call.params,
        "idempotency_key": idempotency_key(action),
    }


def execute(
    action: Action,
    *,
    transport: Transport,
    acl: ACL,
    registry: Registry,
    store: Store,
    limiter: ChatRateLimiter | None = None,
    now: float | None = None,
    allowed_chats: frozenset[int] | set[int] | None = None,
) -> dict[str, Any]:
    """Authorize, deduplicate, rate-limit and execute one action."""
    try:
        acl.authorize(action)
    except GatewayError as exc:
        store.audit(action.verb, "denied", actor=action.actor, detail=str(exc))
        raise
    now = time.time() if now is None else float(now)
    key = idempotency_key(action)

    if action.verb == "structure":
        return _structure_op(
            action,
            transport=transport,
            acl=acl,
            registry=registry,
            store=store,
            limiter=limiter,
            allowed_chats=allowed_chats,
        )

    if action.verb == "queue":
        return _queue_op(action, transport=transport, store=store, limiter=limiter, now=now, registry=registry)

    if action.verb == "status":
        return _status_payload(acl=acl, registry=registry, store=store, transport=transport)

    try:
        call = build_call(action, registry)
    except GatewayError as exc:
        store.audit(action.verb, "refused", actor=action.actor, detail=str(exc))
        raise

    # Gate G2: the live transport may only reach allow-listed chats, and an
    # empty list denies everything (fail closed — see acl.chat_allowlist_from_env).
    if getattr(transport, "is_live", False):
        allowed = frozenset(int(c) for c in (allowed_chats or ()))
        if call.chat_id not in allowed:
            store.audit(
                action.verb,
                "denied",
                actor=action.actor,
                chat_id=call.chat_id,
                idempotency_key=key,
                detail="chat not in TELEGRAM_CHAT_ALLOWLIST",
            )
            raise AccessDenied(
                f"chat {call.chat_id} is not in TELEGRAM_CHAT_ALLOWLIST (fail closed)"
            )

    params, unsent_tail = _chunk_params(call.params)
    if params is not call.params:
        call = Call(call.method, params, call.chat_id, call.thread_id)

    payload: dict[str, Any] = {"method": call.method, "params": call.params}
    if unsent_tail is not None:
        payload["_tail"] = unsent_tail  # re-sent under this same key (issue #11)
    if action.verb == "topic" and action.op == "create" and action.target.subject:
        # remember what to bind when the topic id comes back (issue #8)
        payload["_bind"] = {
            "subject": action.target.subject,
            "chat_id": call.chat_id,
            "topic_name": action.name,
        }
    if not store.enqueue(key, action.verb, call.chat_id, call.thread_id, payload):
        store.audit(
            action.verb,
            "duplicate",
            actor=action.actor,
            chat_id=call.chat_id,
            thread_id=call.thread_id,
            idempotency_key=key,
            detail="already enqueued",
        )
        return {"status": "duplicate", "idempotency_key": key}

    if limiter is not None and not limiter.allow(call.chat_id, now):
        store.mark_queued(key, now=now)
        store.audit(
            action.verb,
            "queued",
            actor=action.actor,
            chat_id=call.chat_id,
            thread_id=call.thread_id,
            idempotency_key=key,
            detail="rate limited",
        )
        return {"status": "queued", "reason": "rate_limited", "idempotency_key": key}

    try:
        result = transport.call(call.method, call.params)
    except RateLimited as exc:
        # G3 / issue #14: a 429 is a *deferral*, not a failure. The job keeps
        # retrying after Telegram's own retry_after instead of being dropped.
        store.mark_error(key, str(exc), retry_in=exc.retry_after, now=now)
        store.audit(
            action.verb,
            "rate_limited",
            actor=action.actor,
            chat_id=call.chat_id,
            idempotency_key=key,
            detail=f"retry_after={exc.retry_after}",
        )
        return {
            "status": "rate_limited",
            "retry_after": exc.retry_after,
            "idempotency_key": key,
        }
    except TransportError as exc:
        store.mark_error(key, str(exc), retry_in=backoff_delay(0), now=now)
        store.audit(action.verb, "error", actor=action.actor, chat_id=call.chat_id,
                    idempotency_key=key, detail=str(exc))
        return {"status": "error", "error": str(exc), "idempotency_key": key}

    if limiter is not None:
        limiter.record(call.chat_id, now)
    message_id = result.get("message_id") if isinstance(result, dict) else None
    _maybe_bind(store, registry, payload, result)

    unsent = payload.pop("_tail", None)
    if unsent is not None:
        # A long digest is only partly out: keep the job queued with the rest
        # so a retry resumes exactly where it stopped (never re-sends a chunk).
        next_params, next_tail = _chunk_params({**call.params, "text": unsent})
        next_payload: dict[str, Any] = {"method": call.method, "params": next_params}
        if next_tail is not None:
            next_payload["_tail"] = next_tail
        store.requeue_payload(key, next_payload, now=now)
        remaining = len(split_message(unsent))
        store.audit(
            action.verb,
            "sent",
            actor=action.actor,
            chat_id=call.chat_id,
            thread_id=call.thread_id,
            idempotency_key=key,
            detail=f"{call.method} -> {message_id} (chunk, {remaining} left)",
        )
        return {
            "status": "queued",
            "chunks_remaining": remaining,
            "message_id": message_id,
            "idempotency_key": key,
        }

    store.mark_sent(key, message_id)
    store.audit(
        action.verb,
        "sent",
        actor=action.actor,
        chat_id=call.chat_id,
        thread_id=call.thread_id,
        idempotency_key=key,
        detail=f"{call.method} -> {message_id}",
    )
    return {
        "status": "sent",
        "method": call.method,
        "message_id": message_id,
        "idempotency_key": key,
    }


# ---------------------------------------------------------------------------
# local verb payloads
# ---------------------------------------------------------------------------
def _status_payload(*, acl: ACL, registry: Registry, store: Store, transport: Transport) -> dict[str, Any]:
    from . import __version__

    bound = sum(1 for s in registry.subjects() if registry.get(s).get("thread_id") is not None)
    return {
        "status": "ok",
        "version": __version__,
        "mode": type(transport).__name__,
        "live_transport": False,  # gate G1: no HTTP transport exists yet
        "acl_configured": acl.configured,
        "registry": {"subjects": len(registry.subjects()), "bound": bound},
        "jobs": store.counts(),
    }


def _queue_op(action, *, transport: Transport, store: Store, limiter: ChatRateLimiter | None, now: float, registry: Registry | None = None) -> dict[str, Any]:
    """Local queue inspection; ``run`` drains jobs already authorized at enqueue.

    A job bounced by a 429 is *deferred* (``deferred`` counter): it keeps its
    place and becomes eligible again once ``retry_after`` has elapsed. Any job
    that exhausts :attr:`Store.MAX_ATTEMPTS` disappears from the drain and is
    reported by ``store.counts()`` as ``dead``.
    """
    if action.op in ("list", "pending"):
        rows = store.pending(action.limit, now=now)
        return {"status": "ok", "pending": len(rows), "jobs": rows}

    jobs = store.pending(action.limit, now=now)
    sent = skipped = deferred = 0
    for job in jobs:
        chat_id = job.get("chat_id")
        if limiter is not None and chat_id is not None and not limiter.allow(int(chat_id), now):
            skipped += 1
            continue
        key = job["idempotency_key"]
        try:
            payload = json.loads(job["payload"])
            result = transport.call(payload["method"], payload["params"])
        except RateLimited as exc:
            store.mark_error(key, str(exc), retry_in=exc.retry_after, now=now)
            store.audit("queue", "rate_limited", chat_id=chat_id, idempotency_key=key,
                        detail=f"retry_after={exc.retry_after}")
            deferred += 1
            continue
        except GatewayError as exc:
            store.mark_error(key, str(exc), retry_in=backoff_delay(int(job.get("attempts") or 0)),
                             now=now)
            store.audit("queue", "error", chat_id=chat_id, idempotency_key=key, detail=str(exc))
            skipped += 1
            continue
        unsent = payload.pop("_tail", None)
        if unsent is not None:
            # advance one chunk of a long message (issue #11), never re-send
            next_params, next_tail = _chunk_params({**payload["params"], "text": unsent})
            next_payload: dict[str, Any] = {"method": payload["method"], "params": next_params}
            if next_tail is not None:
                next_payload["_tail"] = next_tail
            store.requeue_payload(key, next_payload, now=now)
            store.audit("queue", "sent", chat_id=chat_id, idempotency_key=key,
                        detail=f"chunk, {len(split_message(unsent))} left")
        else:
            store.mark_sent(key, result.get("message_id") if isinstance(result, dict) else None)
            _maybe_bind(store, registry, payload, result)
        if limiter is not None and chat_id is not None:
            limiter.record(int(chat_id), now)
        sent += 1
    store.audit("queue", "run", detail=f"sent={sent} skipped={skipped} deferred={deferred}")
    return {"status": "ok", "sent": sent, "skipped": skipped, "deferred": deferred}


def _maybe_bind(store: Store, registry: Registry | None, payload: dict[str, Any], result: Any) -> None:
    """Bind a freshly created topic to its subject (issue #8).

    Called after every successful ``createForumTopic``, whether it ran inline
    or was drained later from the queue.
    """
    if registry is None or not isinstance(payload, dict):
        return
    bind = payload.get("_bind")
    if not bind or not isinstance(result, dict):
        return
    thread_id = result.get("message_thread_id") or result.get("message_id")
    if not thread_id:
        return
    try:
        registry.bind(bind["subject"], int(bind["chat_id"]), int(thread_id),
                      topic_name=bind.get("topic_name"))
    except GatewayError as exc:
        store.audit("topic", "bind_failed", chat_id=int(bind["chat_id"]),
                    detail=f"{bind['subject']}: {exc}")
        return
    store.audit("topic", "bound", chat_id=int(bind["chat_id"]), thread_id=int(thread_id),
                detail=bind["subject"])


def _structure_op(
    action,
    *,
    transport: Transport,
    acl: ACL,
    registry: Registry,
    store: Store,
    limiter: ChatRateLimiter | None,
    allowed_chats: frozenset[int] | set[int] | None,
    timeout: float = 300.0,
) -> dict[str, Any]:
    """Composite provisioning: create topics -> pin cards -> publish index.

    Every sub-action goes through :func:`execute`, so it inherits ACL, the
    idempotency gate, the rate limiter and the audit trail. A sub-action that
    lands in the queue is waited for (drained) before its follow-up pin, so a
    re-run is safe and never leaves a half-provisioned topic unpinned.
    """
    chat_id = action.target.chat_id
    if chat_id is None:
        raise RegistryError("structure requires an explicit chat id (--chat)")

    specs = [s for s in STRUCTURE if not action.only or s.subject in action.only]

    def run(sub: dict[str, Any]) -> dict[str, Any]:
        return execute(
            parse_action(sub), transport=transport, acl=acl, registry=registry,
            store=store, limiter=limiter, allowed_chats=allowed_chats,
        )

    def run_wait(sub: dict[str, Any]) -> dict[str, Any]:
        result = run(sub)
        if result.get("status") != "queued":
            return result
        key = result["idempotency_key"]
        deadline = time.time() + timeout
        while time.time() < deadline:
            time.sleep(2)
            run({"verb": "queue", "op": "run", "actor": action.actor})
            job = store.find(key)
            if job and job["status"] == "sent":
                return {"status": "sent", "message_id": job["message_id"],
                        "idempotency_key": key}
            if job and job["status"] == "dead":
                return {"status": "error", "error": job["last_error"],
                        "idempotency_key": key}
        return {"status": "queued", "idempotency_key": key}

    summary: dict[str, Any] = {
        "created": [], "existing": [], "cards": [], "pins": [], "index": None,
        "failures": [],
    }

    for spec in specs:
        entry = registry.get(spec.subject)
        if entry.get("thread_id") is None:
            create = {
                "verb": "topic", "actor": action.actor, "confirm": action.confirm,
                "target": {"subject": spec.subject, "chat_id": chat_id},
                "op": "create", "name": spec.name, "icon_color": spec.icon_color,
            }
            result = run_wait(create)
            if result.get("status") != "sent":
                create.pop("icon_color", None)  # API rejected the colour: default it
                result = run_wait(create)
            if result.get("status") == "sent":
                summary["created"].append(spec.subject)
            else:
                summary["failures"].append({"subject": spec.subject, "step": "create",
                                             "result": result})
                continue
        else:
            summary["existing"].append(spec.subject)

        thread_id = registry.get(spec.subject).get("thread_id")
        if thread_id is None:
            summary["failures"].append({"subject": spec.subject, "step": "bind",
                                         "result": "no thread id after create"})
            continue

        if action.cards:
            card = run_wait({
                "verb": "publish", "actor": action.actor,
                "target": {"chat_id": chat_id, "thread_id": thread_id},
                "text": card_text(spec),
            })
            if card.get("status") == "sent" and card.get("message_id"):
                pin = run_wait({
                    "verb": "pin", "actor": action.actor,
                    "target": {"chat_id": chat_id}, "message_id": card["message_id"],
                })
                summary["cards"].append({"subject": spec.subject,
                                         "message_id": card["message_id"]})
                summary["pins"].append({"subject": spec.subject,
                                        "status": pin.get("status")})
            elif card.get("status") == "duplicate":
                summary["cards"].append({"subject": spec.subject, "status": "duplicate"})
            else:
                summary["failures"].append({"subject": spec.subject, "step": "card",
                                             "result": card})

    if action.index:
        bound: dict[str, int] = {}
        for spec in STRUCTURE:
            if action.only and spec.subject not in action.only:
                continue
            thread_id = registry.get(spec.subject).get("thread_id")
            if thread_id is not None:
                bound[spec.subject] = thread_id
        text, button_rows = index_payload(chat_id, bound)
        index = run_wait({
            "verb": "publish", "actor": action.actor, "target": {"chat_id": chat_id},
            "text": text,
            "buttons": [b for row in button_rows for b in row],
        })
        if index.get("status") == "sent" and index.get("message_id"):
            pin = run_wait({
                "verb": "pin", "actor": action.actor,
                "target": {"chat_id": chat_id}, "message_id": index["message_id"],
            })
            summary["index"] = {"message_id": index["message_id"],
                                "pinned": pin.get("status")}
        elif index.get("status") == "duplicate":
            summary["index"] = {"status": "duplicate"}
        else:
            summary["failures"].append({"step": "index", "result": index})

    store.audit(
        "structure",
        "partial" if summary["failures"] else "sent",
        actor=action.actor,
        chat_id=chat_id,
        detail=json.dumps({k: v for k, v in summary.items() if k != "failures"},
                          ensure_ascii=False),
    )
    return {"status": "partial" if summary["failures"] else "ok", **summary}
