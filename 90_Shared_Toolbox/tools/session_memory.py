#!/usr/bin/env python3
"""
Master Studio Cross-Agent Session & Memory Manager
--------------------------------------------------
Universal, local, vendor-neutral memory manager for Master Studio.
Works seamlessly across Oh My Pi (OMP), OpenCode, MiMo Studio, FreeBuf, and Cursor.

Commands:
  boot      Print compact context injection (< 150 tokens) for agent fast-boot.
  status    Show active session pointer, total sessions logged, and memory stats.
  log       Log a completed task or decision to today's session file.
  remember  Add a persistent rule or preference to MEMORY.md.
  recall    Search past sessions and persistent memory for keywords.
"""

import sys
import re
import argparse
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).resolve().parent.parent.parent
HUB = BASE / "00_STUDIO_HUB"
SESSIONS_DIR = HUB / "sessions"
ACTIVE_STATE_FILE = HUB / "ACTIVE_STATE.md"
MEMORY_FILE = HUB / "MEMORY.md"


def get_boot_context():
    """Generates ultra-compact fast-boot text (< 150 tokens)."""
    active_text = ACTIVE_STATE_FILE.read_text(encoding="utf-8") if ACTIVE_STATE_FILE.exists() else ""
    memory_text = MEMORY_FILE.read_text(encoding="utf-8") if MEMORY_FILE.exists() else ""

    # Extract Active State values
    sem = re.search(r'current_semester:\s*["\']?(.*?)["\']?\s*$', active_text, re.M)
    week = re.search(r'active_week:\s*["\']?(.*?)["\']?\s*$', active_text, re.M)
    subj = re.search(r'active_subject:\s*["\']?(.*?)["\']?\s*$', active_text, re.M)
    todo = re.search(r'immediate_todo:\s*["\']?(.*?)["\']?\s*$', active_text, re.M)
    focus = re.search(r'next_session_focus:\s*["\']?(.*?)["\']?\s*$', active_text, re.M)

    lines = [
        "=== MASTER STUDIO FAST-BOOT CONTEXT ===",
        f"Semester: {sem.group(1) if sem else 'Semester 1'}",
        f"Active Week: {week.group(1) if week else '1'}",
        f"Active Subject: {subj.group(1) if subj else '04_Advanced_Software_Eng'}",
        f"Current Milestone: {todo.group(1) if todo else ''}",
        f"Next Focus: {focus.group(1) if focus else ''}",
        "",
        "Core Directives: Zero emojis, native vector PPTX (31pt/21pt/17.5pt/14pt), BiDi DOCX (<w:bidi/>), code-generated diagrams, local CPU OCR for scans.",
        "Hub Files: 00_STUDIO_HUB/ACTIVE_STATE.md | 00_STUDIO_HUB/MEMORY.md | http://127.0.0.1:5000",
        "======================================="
    ]
    return "\n".join(lines)


def get_status():
    """Prints current memory state and session stats."""
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    session_files = sorted(list(SESSIONS_DIR.glob("*.md")))
    
    print("=== Master Studio Memory Status ===")
    print(f"Base Directory: {BASE}")
    print(f"Active State File: {'[Found]' if ACTIVE_STATE_FILE.exists() else '[Missing]'}")
    print(f"Persistent Memory File: {'[Found]' if MEMORY_FILE.exists() else '[Missing]'}")
    print(f"Total Session Logs: {len(session_files)}")
    if session_files:
        print(f"Latest Session: {session_files[-1].name}")
    print("===================================")


def log_entry(summary, subject=None):
    """Appends an entry to today's session log."""
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # Find or create today's session file
    matching = sorted(list(SESSIONS_DIR.glob(f"{today_str}-session-*.md")))
    if not matching:
        session_num = 1
        session_file = SESSIONS_DIR / f"{today_str}-session-01.md"
        content = [
            "---",
            f"title: \"Session Log: {today_str} — Session 01\"",
            f"session_id: \"{today_str}-01\"",
            f"date: \"{today_str}\"",
            "---",
            "",
            f"# Session Log: {today_str} — Session 01",
            "",
            "## Actions & Milestones Logged",
            f"- [{datetime.now().strftime('%H:%M:%S')}] {summary}" + (f" (Subject: {subject})" if subject else ""),
            ""
        ]
        session_file.write_text("\n".join(content), encoding="utf-8")
    else:
        session_file = matching[-1]
        with open(session_file, "a", encoding="utf-8") as f:
            f.write(f"- [{datetime.now().strftime('%H:%M:%S')}] {summary}" + (f" (Subject: {subject})" if subject else "") + "\n")

    print(f"Logged entry to: {session_file.relative_to(BASE)}")


def remember_fact(fact):
    """Appends a rule or invariant to MEMORY.md."""
    if not MEMORY_FILE.exists():
        print("Error: MEMORY.md not found.", file=sys.stderr)
        return

    with open(MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n- **Added {datetime.now().strftime('%Y-%m-%d')}:** {fact}\n")
    print("Added fact to MEMORY.md")


def recall_query(query):
    """Searches memory and session logs for matches."""
    query_lower = query.lower()
    matches = []

    # Search MEMORY.md
    if MEMORY_FILE.exists():
        text = MEMORY_FILE.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), 1):
            if query_lower in line.lower():
                matches.append((f"MEMORY.md (line {line_no})", line.strip()))

    # Search Sessions
    if SESSIONS_DIR.exists():
        for sf in sorted(SESSIONS_DIR.glob("*.md"), reverse=True):
            text = sf.read_text(encoding="utf-8")
            for line_no, line in enumerate(text.splitlines(), 1):
                if query_lower in line.lower():
                    matches.append((f"{sf.name} (line {line_no})", line.strip()))

    print(f"=== Recall Search for '{query}': {len(matches)} matches found ===")
    for src, line in matches[:15]:
        print(f"  [{src}] {line}")
    if len(matches) > 15:
        print(f"  ... and {len(matches) - 15} more matches.")


def main():
    parser = argparse.ArgumentParser(description="Master Studio Session & Memory CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # boot
    subparsers.add_parser("boot", help="Generate compact fast-boot context string")

    # status
    subparsers.add_parser("status", help="Show memory and session statistics")

    # log
    log_parser = subparsers.add_parser("log", help="Log an action to today's session journal")
    log_parser.add_argument("summary", help="Summary text of what was accomplished")
    log_parser.add_argument("-s", "--subject", help="Subject code or name", default=None)

    # remember
    rem_parser = subparsers.add_parser("remember", help="Save a persistent fact/rule to MEMORY.md")
    rem_parser.add_argument("fact", help="The fact or rule to persist")

    # recall
    rec_parser = subparsers.add_parser("recall", help="Search sessions and memory for a keyword")
    rec_parser.add_argument("query", help="Keyword or topic to search")

    args = parser.parse_args()

    if args.command == "boot":
        print(get_boot_context())
    elif args.command == "status":
        get_status()
    elif args.command == "log":
        log_entry(args.summary, args.subject)
    elif args.command == "remember":
        remember_fact(args.fact)
    elif args.command == "recall":
        recall_query(args.query)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
