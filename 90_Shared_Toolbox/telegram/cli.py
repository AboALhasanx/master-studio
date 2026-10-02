"""Gateway CLI — the single entry point agents invoke (issue #15, Zero-CLI policy).

Usage (through the launcher so no PYTHONPATH juggling is needed)::

    python 90_Shared_Toolbox/tools/tg.py status
    python 90_Shared_Toolbox/tools/tg.py publish --chat -100123 --thread 7 --text "hi" --dry-run
    python 90_Shared_Toolbox/tools/tg.py topic --op create --chat -100123 --name 07-Thesis

Exit codes are stable (see :mod:`telegram.errors`): 0 ok, 2 invalid action,
3 access denied, 4 needs --confirm, 5 gateway not ready (live mode is a G2
capability), 6 registry problem, 7 transport failure, 8 file pipeline failure.

Gate G1 guarantees: without ``--dry-run`` the call still goes through the
mock transport — no socket is ever opened, and ``--live`` fails loudly.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from .acl import ACL, chat_allowlist_from_env
from .errors import ActionValidationError, GatewayError
from .executor import execute, plan
from .human import HUMAN_VERBS, authorize as authorize_human, human_enabled
from .publisher import MEDIA_KINDS, upload_uri
from .registry import Registry
from .schema import Action, parse_action
from .store import ChatRateLimiter, Store, load_dotenv
from .transport import build_transport

__all__ = ["main", "build_parser"]


# ---------------------------------------------------------------------------
# argument plumbing
# ---------------------------------------------------------------------------
def _add_target(parser: argparse.ArgumentParser, *, thread: bool = True) -> None:
    parser.add_argument("--subject", help="registry subject, e.g. 01-Cyber-Security")
    parser.add_argument("--chat", type=int, dest="chat_id", help="explicit chat id")
    if thread:
        parser.add_argument("--thread", type=int, dest="thread_id", help="explicit message_thread_id")


def _target(args: argparse.Namespace) -> dict[str, Any]:
    out: dict[str, Any] = {}
    if getattr(args, "subject", None):
        out["subject"] = args.subject
    if getattr(args, "chat_id", None) is not None:
        out["chat_id"] = args.chat_id
    if getattr(args, "thread_id", None) is not None:
        out["thread_id"] = args.thread_id
    return out


def _buttons(raw: list[str]) -> list[dict[str, str]]:
    """Repeated ``--button LABEL=URL`` flags -> the schema's button objects."""
    buttons = []
    for item in raw:
        label, sep, url = item.partition("=")
        if not sep or not url:
            raise ActionValidationError(f"--button expects LABEL=URL, got {item!r}")
        buttons.append({"label": label.strip(), "url": url.strip()})
    return buttons


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tg.py",
        description="Master Studio Telegram gateway (outbound-only, bot-first).",
    )
    parser.add_argument("--actor", type=int, help="Telegram user id driving the command (owner allowlist)")
    parser.add_argument("--confirm", action="store_true", help="required for destructive actions")
    parser.add_argument("--dry-run", action="store_true", help="validate and print the plan; no execution")
    parser.add_argument("--json", action="store_true", dest="as_json", help="machine-readable output")
    parser.add_argument("--live", action="store_true", help="use the live transport (arrives at gate G2)")
    parser.add_argument("--registry", help="path to the topic registry JSON")
    parser.add_argument("--db", help="path to the SQLite job store")

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="local health report")

    p = sub.add_parser("publish", help="post text or a file into a topic")
    _add_target(p)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="message text (HTML parse mode)")
    group.add_argument("--file", action="append", default=[], metavar="PATH",
                       help="local path (or file:// URI) to upload; "
                            "repeat 2-10 times to post an album")
    p.add_argument("--button", action="append", default=[], metavar="LABEL=URL",
                   help="inline URL button; repeatable")
    p.add_argument("--reply-to", type=int, dest="reply_to", help="anchor to an existing message id")
    p.add_argument("--caption", help="caption for an uploaded file")
    p.add_argument("--html", action="store_true", dest="html",
                   help="send --text/--caption as HTML")
    p.add_argument("--kind", choices=list(MEDIA_KINDS), default="document",
                   help="which send* method carries the file; document (default) is "
                        "byte-exact, photo/video are recompressed by Telegram")

    p = sub.add_parser("topic", help="manage forum topics")
    _add_target(p)
    p.add_argument("--op", required=True, choices=["create", "rename", "close", "reopen", "delete"])
    p.add_argument("--name", help="topic name (create/rename)")

    p = sub.add_parser("reply", help="reply to a message addressed by link or id")
    _add_target(p)
    p.add_argument("--to", required=True, help="t.me link or numeric message id")
    p.add_argument("--text", required=True)

    p = sub.add_parser("forward",
                       help="re-post a message into a topic, keeping its original sender")
    _add_target(p)
    p.add_argument("--from", dest="source", required=True,
                   help="source message: t.me/c/<chat>/<id>, t.me/<user>/<id> or a bare id")
    p.add_argument("--from-chat", type=int, dest="source_chat",
                   help="explicit source chat id (required when --from is a bare id)")

    p = sub.add_parser("copy",
                       help="re-post a message as our own, optionally re-captioned")
    _add_target(p)
    p.add_argument("--from", dest="source", required=True,
                   help="source message: t.me/c/<chat>/<id>, t.me/<user>/<id> or a bare id")
    p.add_argument("--from-chat", type=int, dest="source_chat",
                   help="explicit source chat id (required when --from is a bare id)")
    p.add_argument("--caption", help="replace the caption (omit to keep the original)")
    p.add_argument("--html", action="store_true", dest="html",
                   help="send --caption as HTML")

    p = sub.add_parser("edit", help="edit an existing message (text or caption)")
    _add_target(p, thread=False)
    p.add_argument("--message-id", type=int, required=True, dest="message_id")
    p.add_argument("--text", help="new message body -> editMessageText")
    p.add_argument("--caption", help="new media caption -> editMessageCaption")
    p.add_argument("--html", action="store_true", dest="html",
                   help="send the payload as HTML")
    p.add_argument("--button", action="append", default=[], metavar="LABEL=URL",
                   help="inline URL button (text edit only); repeatable")

    p = sub.add_parser("delete", help="delete one or many messages")
    _add_target(p, thread=False)
    p.add_argument("--message-id", type=int, required=True, dest="message_id", nargs="+")

    p = sub.add_parser("pin", help="pin / unpin a message, or sweep a whole topic")
    # `--thread` IS accepted: `--unpin-all` needs a thread (the sweep call is
    # topic-scoped, `resolve_destination(require_thread=True)`), and it used to
    # be impossible to supply one — the parser rejected the flag while the
    # executor demanded it, so `pin --unpin-all --chat X --thread Y` could
    # never run. `--subject` worked; the explicit form did not. Fixed 2026-09-29.
    _add_target(p, thread=True)
    p.add_argument("--message-id", type=int, dest="message_id",
                   help="the message to pin or unpin (omit with --unpin-all)")
    p.add_argument("--unpin", action="store_true")
    p.add_argument("--unpin-all", action="store_true", dest="unpin_all",
                   help="unpin every message in the topic (needs --confirm)")

    p = sub.add_parser("react", help="add a reaction to a message")
    _add_target(p, thread=False)
    p.add_argument("--message-id", type=int, required=True, dest="message_id")
    p.add_argument("--emoji", required=True)

    p = sub.add_parser("action", help="send a transient presence signal (typing ...)")
    _add_target(p)
    p.add_argument("--kind", required=True, help="typing | upload_document | choose_sticker | ...")

    p = sub.add_parser("queue", help="inspect or drain the local job queue")
    p.add_argument("op", nargs="?", choices=["list", "pending", "run"], default="list")
    p.add_argument("--limit", type=int, default=50)

    p = sub.add_parser("structure",
                       help="provision the group layout: topics + pinned cards + index")
    _add_target(p, thread=False)
    p.add_argument("--no-cards", dest="cards", action="store_false",
                   help="skip the pinned brief card per topic")
    p.add_argument("--no-index", dest="index", action="store_false",
                   help="skip the pinned index message in the General topic")
    p.add_argument("--only", action="append", default=[], metavar="SUBJECT",
                   help="limit to specific registry subjects (repeatable)")

    # RawTextHelpFormatter: the --source example is a full vault path, longer
    # than the help column, and argparse's default textwrap would shatter it
    # mid-word — --help would print something the operator cannot paste.
    p = sub.add_parser("pipeline",
                       help="export a vault file when stale, then publish it",
                       formatter_class=argparse.RawTextHelpFormatter)
    _add_target(p)
    p.add_argument("--source", required=True,
                   help="vault-relative path (from the checkout root), e.g. "
                        "01_Semester_1/01_Cyber_Security/03_Study_Notes/W01_DeepDive.md")
    p.add_argument("--caption", help="media caption for the uploaded artifact")
    p.add_argument("--html", action="store_true", dest="html",
                   help="send the caption as HTML")

    p = sub.add_parser("quiz",
                       help="publish a deep link into the dashboard quiz engine")
    _add_target(p)
    p.add_argument("--quiz-id", required=True, dest="quiz_id",
                   help="quiz bank name, e.g. Quiz_01_Software_Crisis")
    p.add_argument("--title", help="heading shown in the message (defaults to the id)")
    p.add_argument("--mode", choices=["exam", "study"], default="exam",
                   help="which dashboard mode the link opens (default: exam)")
    p.add_argument("--shuffle", action="store_true",
                   help="ask the dashboard to shuffle questions/options")
    p.add_argument("--host", default="127.0.0.1",
                   help="dashboard host as reachable from the phone (default: 127.0.0.1)")
    p.add_argument("--port", type=int, default=5000,
                   help="dashboard port (default: 5000)")
    p.add_argument("--text", help="override the generated message body")

    p = sub.add_parser("bridge",
                       help="one-shot Pull poll: read pending bot mentions as proposals (never sends)")
    p.add_argument("--limit", type=int, default=20,
                   help="cap on updates considered in one poll (default: 20)")
    p.add_argument("--bot-username",
                   help="the bot's @username, used to detect mentions "
                        "(default: TELEGRAM_BOT_USERNAME from .env)")
    p.add_argument("--subject", help="registry subject to steer notes toward")

    p = sub.add_parser("interactive",
                       help="one-shot listening session: reply to mentions (ADR D15)")
    p.add_argument("--for", type=float, dest="for_seconds", default=60.0,
                   help="how long the session may run, in seconds (default: 60)")
    p.add_argument("--max", type=int, dest="max_messages", default=20,
                   help="cap on messages handled in one session (default: 20)")
    p.add_argument("--bot-username",
                   help="the bot's @username, used to detect mentions "
                        "(default: TELEGRAM_BOT_USERNAME from .env)")
    p.add_argument("--subject", help="registry subject to steer answers toward")

    # `human` is a *separate* capability, not a schema verb: it drives a
    # personal MTProto account (issue #22) and, like `interactive`, is
    # dispatched before `_action_from_args` so it can never be composed into
    # the bot's publish path.
    p = sub.add_parser("human",
                       help="control the spare human account (issue #22)")
    p.add_argument("--verb", required=True, choices=list(HUMAN_VERBS),
                   help="what to do with the spare account")
    p.add_argument("--chat", type=int, dest="chat_id",
                   help="target chat id (required for read and say)")
    p.add_argument("--text", help="message body (verb say)")
    p.add_argument("--thread", type=int, dest="thread_id",
                   help="forum topic id to post into (verb say); omit to post "
                        "to the general topic")
    p.add_argument("--limit", type=int, default=10,
                   help="how many messages to fetch (verb read, default 10)")
    p.add_argument("--phone", help="spare account number in international "
                                   "form (verb login)")
    p.add_argument("--code", help="login code Telegram just sent (verb login)")
    p.add_argument("--password", help="2FA password, only after Telegram "
                                      "answers with a two-step challenge "
                                      "(verb login) — one-time, never persisted")

    return parser


def _action_from_args(args: argparse.Namespace) -> Action:
    data: dict[str, Any] = {
        "verb": args.command,
        "actor": args.actor,
        "confirm": bool(args.confirm),
    }
    if args.command == "status":
        return parse_action(data)

    if args.command == "publish":
        data["target"] = _target(args)
        if args.text is not None:
            data["text"] = args.text
        if args.file:
            if len(args.file) == 1:
                data["file"] = upload_uri(args.file[0])
            else:
                data["files"] = [upload_uri(f) for f in args.file]  # 2+ -> one sendMediaGroup
        if args.caption is not None:
            data["caption"] = args.caption
        if args.html:
            data["parse_mode"] = "HTML"
        data["kind"] = args.kind
        if args.reply_to is not None:
            data["reply_to"] = args.reply_to
        if args.button:
            data["buttons"] = _buttons(args.button)

    elif args.command == "topic":
        data["target"] = _target(args)
        data["op"] = args.op
        if args.name:
            data["name"] = args.name

    elif args.command == "reply":
        data["target"] = _target(args)
        data["to"] = args.to
        data["text"] = args.text

    elif args.command in ("forward", "copy"):
        data["target"] = _target(args)
        data["source"] = args.source
        if args.source_chat is not None:
            data["source_chat"] = args.source_chat
        if args.command == "copy":
            if args.caption is not None:
                data["caption"] = args.caption
            if args.html:
                data["parse_mode"] = "HTML"

    elif args.command == "edit":
        data["target"] = _target(args)
        data["message_id"] = args.message_id
        if args.text is not None:
            data["text"] = args.text
        if args.caption is not None:
            data["caption"] = args.caption
        if args.html:
            data["parse_mode"] = "HTML"
        if args.button:
            data["buttons"] = _buttons(args.button)

    elif args.command == "delete":
        data["target"] = _target(args)
        data["message_ids"] = list(args.message_id)

    elif args.command == "pin":
        data["target"] = _target(args)
        data["unpin_all"] = bool(args.unpin_all)
        if args.unpin_all:
            data["pinned"] = False
        else:
            data["message_id"] = args.message_id
            data["pinned"] = not args.unpin

    elif args.command == "react":
        data["target"] = _target(args)
        data["message_id"] = args.message_id
        data["emoji"] = args.emoji

    elif args.command == "action":
        data["target"] = _target(args)
        data["kind"] = args.kind

    elif args.command == "queue":
        data["op"] = args.op
        data["limit"] = args.limit

    elif args.command == "structure":
        data["target"] = _target(args)
        data["cards"] = bool(args.cards)
        data["index"] = bool(args.index)
        data["only"] = list(args.only or [])

    elif args.command == "pipeline":
        data["target"] = _target(args)
        data["source"] = args.source
        if args.caption is not None:
            data["caption"] = args.caption
        if args.html:
            data["parse_mode"] = "HTML"

    elif args.command == "quiz":
        data["target"] = _target(args)
        data["quiz_id"] = args.quiz_id
        data["host"] = args.host
        data["port"] = args.port
        data["mode"] = args.mode
        data["shuffle"] = bool(args.shuffle)
        if args.title is not None:
            data["title"] = args.title
        if args.text is not None:
            data["text"] = args.text

    return parse_action(data)


def _emit(payload: dict[str, Any], as_json: bool) -> None:
    """Print without ever dying on the console's encoding.

    A Windows console defaults to cp1252, so any Arabic caption or emoji in
    the payload (`react --emoji 👍`) raised UnicodeEncodeError *before* a
    single byte was written — the live smoke hit exactly that. Forcing UTF-8
    with a replacement fallback keeps the JSON parseable and the CLI alive.
    """
    for stream in (sys.stdout, sys.stderr):
        if stream is not None and hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")

    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2, default=str), flush=True)
        return
    status = payload.get("status", "ok")
    print(
        f"[{status}] " + " ".join(f"{k}={v}" for k, v in payload.items() if k != "status"),
        flush=True,
    )


# ---------------------------------------------------------------------------
# agent bridge (Pull model) — one poll, proposals only, never sends
# ---------------------------------------------------------------------------
def _run_bridge(args: argparse.Namespace) -> int:
    """Poll once for pending mentions and print proposals as JSON.

    Live-only and allowlist-gated like ``interactive``: without
    ``TELEGRAM_CHAT_ALLOWLIST`` it refuses (exit 3) before any network call.
    The processed ``update_id`` watermark is read from and written back to
    the gateway's own memory, so a message is never proposed twice.
    Restricted proposals are NOT executed — the approval card text is
    included for the agent to forward to the private chat.
    """
    from .bridge import pull_once  # local import: keeps the outbound CLI path lean
    from .telegram_memory import read_state, set_state

    allowed = chat_allowlist_from_env()
    if not allowed:
        _emit({"status": "error", "code": 3,
               "error": "bridge needs TELEGRAM_CHAT_ALLOWLIST (fail closed)"},
              args.as_json)
        return 3
    if not args.live:
        _emit({"status": "error", "code": 5,
               "error": "bridge is a live-only capability (pass --live)"},
              args.as_json)
        return 5

    limit = int(getattr(args, "limit", 20) or 20)
    if limit <= 0 or limit > 100:
        _emit({"status": "error", "code": 2,
               "error": "bridge --limit must be 1..100"}, args.as_json)
        return 2

    import os as _os

    store = Store(args.db)
    acl = ACL.from_env()
    bot_username = args.bot_username or _os.environ.get("TELEGRAM_BOT_USERNAME")
    state = read_state()
    offset = int(state.get("update_offset") or 0)

    result = pull_once(
        build_transport(live=True),
        bot_username=bot_username,
        allowed_chats=allowed,
        owner_ids=acl.owners,
        offset=offset,
        limit=limit,
    )
    set_state(update_offset=result.next_offset,
              last_bridge=result.summary())
    for proposal in result.proposals:
        store.audit("bridge", proposal.kind, actor=proposal.actor,
                    chat_id=proposal.chat_id,
                    detail=(proposal.text or "")[:200])
    payload = result.summary()
    payload["proposals_detail"] = [p.summary() for p in result.proposals]
    _emit(payload, args.as_json)
    return 0 if result.status == "ok" else 1


# ---------------------------------------------------------------------------
# interactive session (ADR D15) — a bounded, on-demand listener
# ---------------------------------------------------------------------------
def _run_interactive(args: argparse.Namespace) -> int:
    """Run one listening session and report what it saw and did.

    Fails closed on every axis: no chat allowlist, no live transport, or an
    empty window all return a refusal rather than opening a listener. The
    processed ``update_id`` watermark is read from and written back to the
    gateway's own memory (D14), so a message is never handled twice.
    """
    from .interactive import SessionLimits, run_session  # local import: keeps the
    from .telegram_memory import read_state, set_state  # outbound CLI path lean

    allowed = chat_allowlist_from_env()
    if not allowed:
        _emit({"status": "error", "code": 3,
               "error": "interactive needs TELEGRAM_CHAT_ALLOWLIST (fail closed)"},
              args.as_json)
        return 3
    if not args.live:
        _emit({"status": "error", "code": 5,
               "error": "interactive is a live-only capability (pass --live)"},
              args.as_json)
        return 5

    try:
        limits = SessionLimits(seconds=args.for_seconds, max_messages=args.max_messages)
    except ValueError as exc:
        _emit({"status": "error", "code": 2, "error": str(exc)}, args.as_json)
        return 2

    store = Store(args.db)
    acl = ACL.from_env()
    bot_username = args.bot_username or __import__("os").environ.get("TELEGRAM_BOT_USERNAME")
    state = read_state()
    offset = int(state.get("update_offset") or 0)

    result = run_session(
        build_transport(live=True),
        bot_username=bot_username,
        allowed_chats=allowed,
        owner_ids=acl.owners,
        limits=limits,
        offset=offset,
        audit=store.audit,
        subject_hint=args.subject,
    )
    set_state(update_offset=result.next_offset,
              last_listen={"seen": len(result.seen), "replied": result.replied})
    payload = result.summary()
    payload["status"] = result.status
    _emit(payload, args.as_json)
    return 0 if result.status == "ok" else 1


# ---------------------------------------------------------------------------
# spare human account (issue #22) — a gated MTProto client
# ---------------------------------------------------------------------------
def _run_human(args: argparse.Namespace) -> int:
    """Do one thing with the spare account, refusing before anything is built.

    The gates run **twice**, deliberately: once before the Telethon client is
    constructed (so a refused request never even opens one — "denied" and
    "never attempted" stay the same thing) and once inside ``run`` (so the
    executor is safe for any direct caller). Authorization is pure, so the
    second pass costs nothing.
    """
    from .errors import AccessDenied, RateLimited, TransportError
    from .human import (HumanRequest, PACING_STATE, SEND_VERBS,
                        TelethonGateway, run)

    store = Store(args.db)
    req = HumanRequest(
        verb=args.verb,
        chat_id=getattr(args, "chat_id", None),
        text=getattr(args, "text", None),
        limit=getattr(args, "limit", 10),
        phone=getattr(args, "phone", None),
        code=getattr(args, "code", None),
        password=getattr(args, "password", None),
        thread_id=getattr(args, "thread_id", None),
    )
    gate = dict(
        live=bool(args.live),
        enabled=human_enabled(),
        allowed_chats=chat_allowlist_from_env(),
    )

    def _row(result: str, detail: str | None = None) -> None:
        """Record the attempt. Deliberately unwrapped, like every audit call
        in ``executor.py``: a ledger that fails must surface loudly, not let
        work pass unmonitored — that would defeat AC 2's monitoring leg."""
        # thread_id belongs here for the same reason chat_id does: five
        # `human:say` rows read thread=None while MTProto showed them inside
        # topics 6/8/10/12/14, so the ledger contradicted the messages.
        store.audit(f"human:{req.verb}", result,
                    chat_id=req.chat_id, thread_id=req.thread_id,
                    detail=detail)

    def _failure(exc: Exception) -> str:
        if isinstance(exc, AccessDenied):
            return "denied"
        if isinstance(exc, RateLimited):          # before TransportError: subclass
            return "rate_limited"
        if isinstance(exc, TransportError):
            return "error"
        return "refused"

    try:
        authorize_human(req, **gate)
        gateway = TelethonGateway.from_env()
        # the pacing ledger must outlive this process, or the documented
        # ceiling would reset on every invocation and block nothing
        result = run(req, gateway, persist=PACING_STATE, **gate)
    except GatewayError as exc:
        _row(_failure(exc), str(exc))
        _emit({"status": "error", "code": exc.code, "verb": req.verb,
               "error": str(exc)}, args.as_json)
        return exc.code
    except Exception as exc:  # a raw Telethon RPCError must not become a traceback
        _row("error", f"{type(exc).__name__}: {exc}")
        _emit({"status": "error", "code": 1, "verb": req.verb,
               "error": f"{type(exc).__name__}: {exc}"}, args.as_json)
        return 1

    _row("sent" if req.verb in SEND_VERBS else "ok",
         _human_detail(req, result))
    _emit({"status": "ok", **result}, args.as_json)
    return 0


def _human_detail(req, result: dict) -> str:
    """What the account actually did — enough to reconstruct a run later.

    ``say`` records the text it spoke (the one thing an audit must never
    lose); reads record only their size, since message bodies are content
    rather than an action.
    """
    payload = result.get("result")
    if req.verb == "say" and isinstance(payload, dict):
        return f"message_id={payload.get('message_id')} text={req.text}"
    if isinstance(payload, list):
        return f"count={len(payload)}"
    if isinstance(payload, dict):
        return json.dumps(payload, ensure_ascii=False)
    return str(payload)


# ---------------------------------------------------------------------------
# entry point
# ---------------------------------------------------------------------------
def _exit_code_for(result: dict[str, Any]) -> int:
    """Map ``execute()``'s result envelope onto the documented exit codes.

    ``execute`` records a transport failure instead of raising — the durable
    queue must keep the job so it can retry — so ``main`` would otherwise
    return 0 for a send that never reached Telegram. ``cli.py`` documents
    "7 transport failure", and a shell gate reading ``$?`` has to see it.

    ``rate_limited`` deliberately stays 0: that status means the job was
    deferred with a precise ``retry_after``, which is pacing working, not
    the transport failing.
    """
    return 7 if result.get("status") == "error" else 0


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    args = build_parser().parse_args(argv)

    if args.command == "interactive":
        return _run_interactive(args)

    if args.command == "bridge":
        return _run_bridge(args)

    if args.command == "human":
        return _run_human(args)

    try:
        action = _action_from_args(args)
        registry = Registry(args.registry)
        store = Store(args.db)
        acl = ACL.from_env()
        limiter = ChatRateLimiter()

        if args.dry_run:
            verdict: dict[str, Any] = {"authorized": True}
            try:
                acl.authorize(action)
            except GatewayError as exc:
                verdict = {"authorized": False, "reason": str(exc), "code": exc.code}
            payload: dict[str, Any] = {"dry_run": True, "action": action.model_dump(mode="json")}
            try:
                payload["plan"] = plan(action, registry)
                payload.update(verdict)
                _emit(payload, args.as_json)
                return 0 if verdict["authorized"] else int(verdict["code"])
            except GatewayError as exc:
                payload["error"] = str(exc)
                payload["code"] = exc.code
                _emit(payload, args.as_json)
                return int(exc.code)

        transport = build_transport(live=args.live)
        result = execute(
            action,
            transport=transport,
            acl=acl,
            registry=registry,
            store=store,
            limiter=limiter,
            allowed_chats=chat_allowlist_from_env(),
        )
        _emit(result, args.as_json)
        return _exit_code_for(result)

    except GatewayError as exc:
        _emit({"status": "error", "error": str(exc), "code": exc.code}, args.as_json)
        return int(exc.code)
    except BrokenPipeError:  # pragma: no cover
        return 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
