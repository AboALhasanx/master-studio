#!/usr/bin/env python3
"""
Master Studio Subject Packer (for Free Web Chatbots)
---------------------------------------------------
Packs all notes, doctor profiles, roadmaps, and seminar sources of any subject
into a single, compact Markdown digest (< 20k tokens) that you can drag-and-drop
or copy-paste into free web chatbots (ChatGPT, Qwen Chat, DeepSeek, Gemini).

Powered by Repomix.
"""

import sys
import argparse
import subprocess
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Pack a Master Studio subject into a single chatbot digest")
    parser.add_argument("subject", help="Subject folder name or number (e.g. '04_Advanced_Software_Eng' or '04')")
    parser.add_argument("-o", "--output", help="Output file path (default: <subject_folder>/chatbot_digest.md)")

    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent.parent
    semester_dirs = sorted(repo_root.glob("0*_Semester_*"))

    target_dir = None
    for sem in semester_dirs:
        if (sem / args.subject).exists():
            target_dir = sem / args.subject
            break
        matches = list(sem.glob(f"{args.subject}*"))
        if matches:
            target_dir = matches[0]
            break

    if not target_dir:
        print(f"Error: Could not find subject folder matching '{args.subject}' in any semester directory", file=sys.stderr)
        sys.exit(1)

    rel_target = target_dir.relative_to(repo_root)
    out_file = Path(args.output) if args.output else target_dir / "chatbot_digest.md"

    print(f"📦 Packing subject '{target_dir.name}' for free web chatbots...")

    cmd = [
        "npx", "-y", "repomix",
        "--include", f"{rel_target}/**",
        "--ignore", f"{rel_target}/02_Raw_Materials/**,**/*.pdf,**/*.pptx,**/*.docx",
        "-o", str(out_file),
        "--style", "markdown",
        "--no-security-check"
    ]

    result = subprocess.run(cmd, cwd=str(repo_root), shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✅ Successfully created chatbot digest at:\n   {out_file}")
        print("\n💡 How to use:")
        print("1. Drag and drop this file into ChatGPT (Web/App), Qwen Chat, DeepSeek, or Gemini.")
        print("2. Ask: 'You are my academic study assistant. Using the context in this document, tutor me on this subject.'")
    else:
        print(f"❌ Repomix packing failed:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
