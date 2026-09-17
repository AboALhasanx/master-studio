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
BUDDY_FILE = HUB / "COLLEGE_BUDDY.md"


def parse_buddy_events(reference_date=None):
    """
    Parses active events from COLLEGE_BUDDY.md and categorizes them.
    Returns (alerts, debriefs, all_active).
    """
    if not BUDDY_FILE.exists():
        return [], [], []

    ref = reference_date or datetime.now().date()
    if hasattr(ref, "date"):
        ref = ref.date()

    text = BUDDY_FILE.read_text(encoding="utf-8")
    lines = text.splitlines()

    alerts = []
    debriefs = []
    all_active = []

    in_active_table = False
    for line in lines:
        if "## 1. Active Events" in line:
            in_active_table = True
            continue
        elif line.startswith("## ") and in_active_table:
            break

        if not in_active_table or not line.strip().startswith("|"):
            continue

        cols = [c.strip() for c in line.strip().split("|")[1:-1]]
        if not cols or "ID" in cols[0] or "---" in cols[0]:
            continue

        # Format: ID | Target Date | Subject | Event / Topic | Professor | Status | Urgency | Buddy Notes / Action
        if len(cols) >= 6:
            evt_id = cols[0].replace("*", "").strip()
            date_str = cols[1].strip()
            subject = cols[2].strip()
            event = cols[3].strip()
            prof = cols[4].strip()
            status = cols[5].strip().upper()
            urgency = cols[6].strip() if len(cols) > 6 else "MEDIUM"
            notes = cols[7].strip() if len(cols) > 7 else ""

            if status in ["COMPLETED", "CANCELED"]:
                continue

            try:
                evt_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                delta = (evt_date - ref).days
            except Exception:
                delta = 999

            evt_dict = {
                "id": evt_id,
                "date": date_str,
                "subject": subject,
                "event": event,
                "professor": prof,
                "status": status,
                "urgency": urgency,
                "notes": notes,
                "delta": delta,
            }
            all_active.append(evt_dict)

            if delta < 0 and status == "UPCOMING":
                debriefs.append(evt_dict)
            elif delta <= 3:
                alerts.append(evt_dict)

    return alerts, debriefs, all_active


def get_boot_context():
    """Generates ultra-compact fast-boot text (< 150 tokens) with active College Buddy alerts."""
    active_text = ACTIVE_STATE_FILE.read_text(encoding="utf-8") if ACTIVE_STATE_FILE.exists() else ""

    # Extract Active State values
    sem = re.search(r'current_semester:\s*["\']?(.*?)["\']?\s*$', active_text, re.M)
    week = re.search(r'active_week:\s*["\']?(.*?)["\']?\s*$', active_text, re.M)
    subj = re.search(r'active_subject:\s*["\']?(.*?)["\']?\s*$', active_text, re.M)
    todo = re.search(r'immediate_todo:\s*["\']?(.*?)["\']?\s*$', active_text, re.M)
    focus = re.search(r'next_session_focus:\s*["\']?(.*?)["\']?\s*$', active_text, re.M)

    alerts, debriefs, _ = parse_buddy_events()

    lines = [
        "=== MASTER STUDIO FAST-BOOT CONTEXT ===",
        f"Semester: {sem.group(1) if sem else 'Semester 1'}",
        f"Active Week: {week.group(1) if week else '1'}",
        f"Active Subject: {subj.group(1) if subj else '04_Advanced_Software_Eng'}",
        f"Current Milestone: {todo.group(1) if todo else ''}",
        f"Next Focus: {focus.group(1) if focus else ''}",
        "",
        "Core Directives: Zero emojis, native vector PPTX (31pt/21pt/17.5pt/14pt), BiDi DOCX (<w:bidi/>), code-generated diagrams, local CPU OCR for scans.",
        "Hub Files: 00_STUDIO_HUB/ACTIVE_STATE.md | 00_STUDIO_HUB/COLLEGE_BUDDY.md | http://127.0.0.1:5000",
    ]

    if debriefs or alerts:
        lines.append("")
        lines.append("--- College Buddy Alerts ---")
        for d in debriefs:
            days_ago = abs(d["delta"])
            lines.append(f"  * [CHECK-IN NEEDED] {d['id']}: {d['subject']} - '{d['event']}' with {d['professor']} was {days_ago}d ago. Ask student how it went!")
        for a in alerts:
            if a["delta"] == 0:
                t_str = "TODAY"
            elif a["delta"] == 1:
                t_str = "TOMORROW"
            else:
                t_str = f"in {a['delta']} days ({a['date']})"
            lines.append(f"  * [UPCOMING] {a['id']}: {a['subject']} - '{a['event']}' with {a['professor']} ({t_str})")
    else:
        lines.append("College Buddy: All caught up! (No pending deadlines in next 3 days)")

    lines.append("=======================================")
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


def buddy_list():
    """Prints a friendly status of all College Buddy events and reminders."""
    alerts, debriefs, all_active = parse_buddy_events()
    print("=== College Buddy: Academic Deadlines & Events ===")
    if not all_active:
        print("No active events tracked yet. Tell me a date to add one!")
        return

    for evt in all_active:
        delta = evt["delta"]
        if delta < 0:
            time_tag = f"[OVERDUE {abs(delta)}d ago - NEEDS CHECK-IN]"
        elif delta == 0:
            time_tag = "[TODAY!]"
        elif delta == 1:
            time_tag = "[TOMORROW]"
        else:
            time_tag = f"[{delta} days left]"

        print(f"• {evt['id']} ({evt['date']}) {time_tag}")
        print(f"  Subject:   {evt['subject']}")
        print(f"  Event:     {evt['event']} (Prof: {evt['professor']})")
        print(f"  Status:    {evt['status']} | Urgency: {evt['urgency']}")
        if evt["notes"]:
            print(f"  Notes:     {evt['notes']}")
        print()

    if debriefs:
        print(f"⚠️  {len(debriefs)} event(s) have passed and need your check-in!")


def buddy_add(date_str, subject, event, prof, notes="", urgency="MEDIUM"):
    """Adds a new event to COLLEGE_BUDDY.md."""
    if not BUDDY_FILE.exists():
        print(f"Error: {BUDDY_FILE} not found.", file=sys.stderr)
        return

    text = BUDDY_FILE.read_text(encoding="utf-8")
    existing_ids = re.findall(r"EVT-(\d+)", text)
    next_num = max([int(i) for i in existing_ids], default=0) + 1
    new_id = f"EVT-{next_num:02d}"

    row = f"| **{new_id}** | {date_str} | {subject} | {event} | {prof} | UPCOMING | {urgency} | {notes} |\n"

    lines = text.splitlines(keepends=True)
    out_lines = []
    inserted = False
    for line in lines:
        out_lines.append(line)
        if not inserted and line.strip().startswith("|:---") and "|:---|" in line:
            out_lines.append(row)
            inserted = True

    if not inserted:
        out_lines.append(f"\n{row}")

    BUDDY_FILE.write_text("".join(out_lines), encoding="utf-8")
    print(f"College Buddy: Added {new_id} ({event} on {date_str})!")


def buddy_update(event_id, status, notes="", new_date=None):
    """Updates an event's status, notes, or shifts date if postponed."""
    if not BUDDY_FILE.exists():
        print(f"Error: {BUDDY_FILE} not found.", file=sys.stderr)
        return

    text = BUDDY_FILE.read_text(encoding="utf-8")
    lines = text.splitlines()
    new_lines = []
    found = False

    clean_id = event_id.replace("*", "").strip()

    for line in lines:
        if line.strip().startswith("|") and (f"**{clean_id}**" in line or f"| {clean_id} |" in line):
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 6:
                found = True
                if new_date:
                    cols[1] = new_date
                cols[5] = status.upper()
                if notes:
                    if len(cols) > 7:
                        cols[7] = notes
                    else:
                        cols.append(notes)
                new_line = "| " + " | ".join(cols) + " |"
                new_lines.append(new_line)
                continue
        new_lines.append(line)

    if found:
        BUDDY_FILE.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        print(f"College Buddy: Updated {clean_id} to status '{status.upper()}'!")
    else:
        print(f"Event {clean_id} not found in {BUDDY_FILE.name}.")


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

    # buddy-list
    subparsers.add_parser("buddy-list", help="List active College Buddy academic events and reminders")

    # buddy-add
    b_add = subparsers.add_parser("buddy-add", help="Add a new deadline or event to College Buddy")
    b_add.add_argument("--date", required=True, help="Target date YYYY-MM-DD")
    b_add.add_argument("--subject", required=True, help="Subject code/name")
    b_add.add_argument("--event", required=True, help="Description of event / quiz / assignment")
    b_add.add_argument("--prof", required=True, help="Professor name")
    b_add.add_argument("--notes", default="", help="Preparation notes or action")
    b_add.add_argument("--urgency", default="MEDIUM", choices=["HIGH", "MEDIUM", "LOW"], help="Urgency level")

    # buddy-update
    b_upd = subparsers.add_parser("buddy-update", help="Update an event's status or record debrief")
    b_upd.add_argument("--id", required=True, help="Event ID e.g. EVT-01")
    b_upd.add_argument("--status", required=True, choices=["COMPLETED", "POSTPONED", "CANCELED", "UPCOMING", "NEEDS_CHECKIN"], help="New status")
    b_upd.add_argument("--notes", default="", help="Debrief reflection or outcome notes")
    b_upd.add_argument("--new-date", default=None, help="New target date if postponed (YYYY-MM-DD)")

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
    elif args.command == "buddy-list":
        buddy_list()
    elif args.command == "buddy-add":
        buddy_add(args.date, args.subject, args.event, args.prof, args.notes, args.urgency)
    elif args.command == "buddy-update":
        buddy_update(args.id, args.status, args.notes, args.new_date)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
