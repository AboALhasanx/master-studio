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
    group.add_argument("--file", help="path of a document to upload")
    p.add_argument("--button", action="append", default=[], metavar="LABEL=URL",
                   help="inline URL button; repeatable")
    p.add_argument("--reply-to", type=int, dest="reply_to", help="anchor to an existing message id")

    p = sub.add_parser("topic", help="manage forum topics")
    _add_target(p)
    p.add_argument("--op", required=True, choices=["create", "rename", "close", "reopen", "delete"])
    p.add_argument("--name", help="topic name (create/rename)")

    p = sub.add_parser("reply", help="reply to a message addressed by link or id")
    _add_target(p)
    p.add_argument("--to", required=True, help="t.me link or numeric message id")
    p.add_argument("--text", required=True)

    p = sub.add_parser("edit", help="edit an existing message (text or caption)")
    _add_target(p, thread=False)
    p.add_argument("--message-id", type=int, required=True, dest="message_id")
    p.add_argument("--text", help="new message body -> editMessageText")
    p.add_argument("--caption", help="new media caption -> editMessageCaption")
    p.add_argument("--html", action="store_true", dest="html",
                   help="send the payload as HTML")

    p = sub.add_parser("delete", help="delete one or many messages")
    _add_target(p, thread=False)
    p.add_argument("--message-id", type=int, required=True, dest="message_id", nargs="+")

    p = sub.add_parser("pin", help="pin / unpin a message, or sweep a whole topic")
    _add_target(p, thread=False)
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

    p = sub.add_parser("pipeline",
                       help="export a vault file when stale, then publish it")
    _add_target(p)
    p.add_argument("--source", required=True,
                   help="vault-relative path, e.g. 03_Study_Notes/W01_Note.md")
    p.add_argument("--caption", help="media caption for the uploaded artifact")
    p.add_argument("--html", action="store_true", dest="html",
                   help="send the caption as HTML")

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
        if args.file is not None:
            data["file"] = args.file
        if args.reply_to is not None:
            data["reply_to"] = args.reply_to
        if args.button:
            buttons = []
            for raw in args.button:
                label, sep, url = raw.partition("=")
                if not sep or not url:
                    raise ActionValidationError(
                        f"--button expects LABEL=URL, got {raw!r}"
                    )
                buttons.append({"label": label.strip(), "url": url.strip()})
            data["buttons"] = buttons

    elif args.command == "topic":
        data["target"] = _target(args)
        data["op"] = args.op
        if args.name:
            data["name"] = args.name

    elif args.command == "reply":
        data["target"] = _target(args)
        data["to"] = args.to
        data["text"] = args.text

    elif args.command == "edit":
        data["target"] = _target(args)
        data["message_id"] = args.message_id
        if args.text is not None:
            data["text"] = args.text
        if args.caption is not None:
            data["caption"] = args.caption
        if args.html:
            data["parse_mode"] = "HTML"

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
# entry point
# ---------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    args = build_parser().parse_args(argv)

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
        return 0

    except GatewayError as exc:
        _emit({"status": "error", "error": str(exc), "code": exc.code}, args.as_json)
        return int(exc.code)
    except BrokenPipeError:  # pragma: no cover
        return 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
