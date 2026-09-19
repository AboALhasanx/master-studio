#!/usr/bin/env python3
"""
Master Studio Interactive Quiz Runner & Mastery Tracker
-------------------------------------------------------
Administers interactive academic quizzes in the terminal, grades answers,
provides immediate bilingual explanations, and automatically records results
into `00_STUDIO_HUB/PROGRESS_ANALYTICS.md` and `00_STUDIO_HUB/LEARNER_MODEL.md`.

Usage:
  python quiz_runner.py path/to/quiz.json
  python quiz_runner.py path/to/quiz.md
"""

import sys
import os
import re
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path

def parse_markdown_quiz(md_path):
    """Extracts scenario questions, options, and answers from markdown files."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    questions = []
    # Pattern to match questions with A, B, C, D options
    q_blocks = re.split(r'###?\s+(?:Question|Q)\s*\d*[:\.]?', content, flags=re.IGNORECASE)
    for block in q_blocks[1:]:
        lines = [l.strip() for l in block.strip().split('\n') if l.strip()]
        if not lines:
            continue

        q_text = []
        options = {}
        answer = None
        explanation = ""

        in_options = False
        for line in lines:
            opt_match = re.match(r'^[\*\-]?\s*([A-D])[\)\.]\s*(.+)$', line, re.IGNORECASE)
            ans_match = re.match(r'^(?:\*\*)?Answer(?:\*\*)?:\s*([A-D])', line, re.IGNORECASE)
            exp_match = re.match(r'^(?:\*\*)?Explanation(?:\*\*)?:\s*(.+)', line, re.IGNORECASE)

            if opt_match:
                in_options = True
                opt_letter = opt_match.group(1).upper()
                options[opt_letter] = opt_match.group(2).strip()
            elif ans_match:
                answer = ans_match.group(1).upper()
            elif exp_match:
                explanation = exp_match.group(1).strip()
            elif not in_options:
                q_text.append(line)
            elif in_options and not ans_match and not exp_match:
                if answer is None:
                    # Continue explanation or option
                    explanation += " " + line

        if q_text and len(options) >= 2 and answer:
            questions.append({
                "question": " ".join(q_text),
                "options": options,
                "answer": answer,
                "explanation": explanation
            })

    return questions

def update_progress_analytics(analytics_path, subject, topic, score_str, percentage):
    """Appends quiz result to 00_STUDIO_HUB/PROGRESS_ANALYTICS.md."""
    if not analytics_path.exists():
        return

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    status = "🟢 Mastered" if percentage >= 80 else ("🟡 Borderline" if percentage >= 60 else "🔴 Review Needed")
    result = "PASS" if percentage >= 60 else "FAIL"

    # Count existing rows to generate Log ID
    with open(analytics_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    log_count = sum(1 for line in lines if line.strip().startswith('| #'))
    new_id = f"#{log_count + 1:03d}"

    row = f"| {new_id} | {now_str} | `{subject}` | {topic} | {score_str} ({percentage:.0f}%) | {result} | {status} |\n"

    # Find the table and append
    new_lines = []
    appended = False
    for line in lines:
        new_lines.append(line)
        if line.strip().startswith('|:---:|:---:|:---|:---|:---:|:---:|:---:|') and not appended:
            new_lines.append(row)
            appended = True

    if not appended:
        new_lines.append(row)

    with open(analytics_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"📊 Progress logged to {analytics_path.name}")

def update_learner_model(model_path, subject, topic, percentage, weak_items):
    """Updates mastered concepts or review queue in LEARNER_MODEL.md."""
    if not model_path.exists():
        return

    with open(model_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d")
    next_review = (now + timedelta(days=3)).strftime("%Y-%m-%d")

    out_lines = []
    inserted = False

    if percentage >= 80:
        target_header = "## 3. Mastered Concepts List"
        row = f"| `{subject}` | {topic} | {now_str} | {percentage:.0f}% | @examiner |\n"
    else:
        target_header = "## 4. Active Review Queue (Spaced Repetition)"
        error_note = "; ".join(weak_items) if weak_items else f"Score {percentage:.0f}% (below master floor)"
        row = f"| `{subject}` | {topic} | {now_str} | {error_note} | High | {next_review} |\n"

    in_target_section = False
    for line in lines:
        if target_header in line:
            in_target_section = True
            out_lines.append(line)
            continue

        # Insert after the blockquote / description line in that section
        if in_target_section and not inserted:
            if line.startswith("|") and ("---" in line or "Subject" in line):
                out_lines.append(line)
                continue
            # Insert right at the top of the table data
            out_lines.append(row)
            inserted = True
            in_target_section = False

        out_lines.append(line)

    if not inserted:
        # Fallback if section format changed
        out_lines.append(f"\n{row}")

    with open(model_path, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)
    print(f"🧠 Cognitive model updated in {model_path.name}")

def run_quiz(questions, subject="General", topic="Quiz"):
    """Runs interactive CLI test."""
    print("=" * 80)
    print(f"🎓 MASTER STUDIO INTERACTIVE EXAMINER — {subject.upper()}")
    print(f"📖 Topic: {topic}")
    print(f"📝 Total Questions: {len(questions)} | Target Floor: >= 60% (Ministerial) | Master Floor: >= 80%")
    print("=" * 80)
    print()

    correct_count = 0
    weak_items = []

    for idx, q in enumerate(questions, 1):
        print(f"────────────────────────────────────────────────────────────────────────")
        print(f"❓ Question {idx} of {len(questions)}:")
        print(f"   {q['question']}\n")

        for opt_key in sorted(q['options'].keys()):
            print(f"   [{opt_key}] {q['options'][opt_key]}")
        print()

        while True:
            choice = input("👉 Enter your answer (A, B, C, D) or [Q] to quit: ").strip().upper()
            if choice in ['A', 'B', 'C', 'D', 'Q']:
                break
            print("⚠️ Invalid choice. Please enter A, B, C, or D.")

        if choice == 'Q':
            print("\nQuiz aborted by user.")
            return

        expected = q['answer'].upper()
        if choice == expected:
            print("\n✅ CORRECT!")
            correct_count += 1
        else:
            print(f"\n❌ INCORRECT. Expected [{expected}], you selected [{choice}].")
            weak_items.append(f"Q{idx}: {q['question'][:50]}...")

        if q.get('explanation'):
            print(f"💡 Explanation: {q['explanation']}\n")
        else:
            print()

    # Results
    total = len(questions)
    pct = (correct_count / total) * 100
    print("=" * 80)
    print(f"🎯 QUIZ COMPLETED: {correct_count} / {total} Correct ({pct:.1f}%)")

    if pct >= 85:
        print("🌟 OUTSTANDING DISTINCTION! Ready for oral viva defense.")
    elif pct >= 75:
        print("🟢 SAFE / MEETS INSTITUTIONAL TARGET (Qualifies for research stage).")
    elif pct >= 60:
        print("🟡 PASSES SUBJECT, BUT BELOW 75% TARGET. Review active queue.")
    else:
        print("🔴 CRITICAL WARNING: BELOW 60% PASSING FLOOR. Re-study immediately.")
    print("=" * 80)

    # File updates
    repo_root = Path(__file__).resolve().parent.parent.parent
    analytics_file = repo_root / "00_STUDIO_HUB" / "PROGRESS_ANALYTICS.md"
    learner_file = repo_root / "00_STUDIO_HUB" / "LEARNER_MODEL.md"

    update_progress_analytics(analytics_file, subject, topic, f"{correct_count} / {total}", pct)
    update_learner_model(learner_file, subject, topic, pct, weak_items)

def main():
    parser = argparse.ArgumentParser(description="Master Studio Interactive Quiz Runner")
    parser.add_argument("quiz_file", help="Path to JSON or Markdown quiz file")
    parser.add_argument("-s", "--subject", default="Advanced_Software_Eng", help="Subject name")
    parser.add_argument("-t", "--topic", default="Coursework Quiz", help="Topic title")

    args = parser.parse_args()
    q_path = Path(args.quiz_file)

    if not q_path.exists():
        print(f"Error: Quiz file '{q_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if q_path.suffix.lower() == '.json':
        with open(q_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        questions = data.get("questions", data)
        subject = data.get("subject", args.subject)
        topic = data.get("topic", args.topic)
    else:
        questions = parse_markdown_quiz(q_path)
        subject = args.subject
        topic = args.topic

    if not questions:
        print(f"Error: No valid questions parsed from '{q_path}'.", file=sys.stderr)
        sys.exit(1)

    run_quiz(questions, subject=subject, topic=topic)

if __name__ == "__main__":
    main()
