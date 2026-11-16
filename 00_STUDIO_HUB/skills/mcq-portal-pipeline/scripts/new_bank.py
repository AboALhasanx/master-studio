#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scaffold a new MCSQuiz bank with the envelope already correct.

The content still has to be written by a human (or a handoff model) — this
only guarantees the naming, the keys, the instructor pair and the numbering
rules from QUIZ_BANK_PROTOCOL.md §2, so the gates fail on content, never on
shape.

    python new_bank.py --subject 03_Data_Mining --chapter 2 --kind model --model B \
        --slug Data_Types --title-ar "أنواع البيانات وتحضيرها" \
        --title-en "Data types and preparation" --questions 5
    python new_bank.py --subject 01_Cyber_Security --chapter 1 --kind topic --topic-num 7 \
        --slug Scope_Review --title-ar "مراجعة النطاق" --title-en "Scope review" --questions 10
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
SEMESTER = ROOT / '01_Semester_1'


def fail(msg: str) -> int:
    print('refused: ' + msg)
    return 2


def load_existing_bank(subject: str):
    quiz_dir = SEMESTER / subject / '07_Quizzes_&_Anki'
    if not quiz_dir.is_dir():
        return None
    for path in sorted(quiz_dir.glob('Quiz_*.json')):
        try:
            with open(path, encoding='utf-8') as fh:
                bank = json.load(fh)
            if bank.get('subject_id') == subject:
                return bank
        except Exception:
            continue
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description='Scaffold a canonical v2 quiz bank.')
    ap.add_argument('--subject', required=True, help='e.g. 03_Data_Mining')
    ap.add_argument('--chapter', required=True, type=int, help="the book's chapter number")
    ap.add_argument('--kind', required=True, choices=('model', 'topic', 'source'))
    ap.add_argument('--model', choices=('A', 'B'), help='for kind=model')
    ap.add_argument('--topic-num', type=int, help='for kind=topic (1, 2, …)')
    ap.add_argument('--batch-num', type=int, default=1, help='for kind=source (1, 2, … -> S01, S02)')
    ap.add_argument('--slug', default='', help='Pascal_Slug, e.g. Data_Types (optional for source)')
    ap.add_argument('--title-ar', required=True)
    ap.add_argument('--title-en', required=True)
    ap.add_argument('--questions', required=True, type=int,
                    help='agreed with the student first (skill §0); minimum 4 so every letter can hold a key')
    ap.add_argument('--instructor-ar', default='')
    ap.add_argument('--instructor-en', default='')
    args = ap.parse_args()

    subject_dir = SEMESTER / args.subject
    if not subject_dir.is_dir():
        return fail('unknown subject folder: %s' % args.subject)
    if args.chapter < 1:
        return fail('chapter must be >= 1')
    if args.questions < 4:
        return fail('at least 4 questions (one key per letter); confirm the count with the student first')
    if args.kind == 'model' and args.model not in ('A', 'B'):
        return fail('kind=model needs --model A|B')
    if args.kind == 'topic' and not (args.topic_num and args.topic_num >= 1):
        return fail('kind=topic needs --topic-num >= 1')
    if args.kind == 'source' and not (args.batch_num and args.batch_num >= 1):
        return fail('kind=source needs --batch-num >= 1')
    if args.kind != 'source' and not args.slug:
        return fail('--slug is required for practice banks')
    if args.kind == 'source' and not 10 <= args.questions <= 15:
        return fail('source batches must use the approved 10-15 question size')

    existing = load_existing_bank(args.subject)
    subject_title = (existing or {}).get('subject_title') or ''
    instructor_ar = args.instructor_ar or (existing or {}).get('instructor_ar') or ''
    instructor_en = args.instructor_en or (existing or {}).get('instructor') or ''
    if not subject_title:
        return fail('no subject_title found: pass an existing bank or check the folder')
    if not instructor_ar:
        return fail('no instructor found: copy it from an existing bank of this subject')

    if args.kind == 'model':
        quiz_id = 'Quiz_Ch%02d_Model%s_%s' % (args.chapter, args.model, args.slug or 'Model')
        topic = '%s — Model %s' % (args.title_en, args.model)
        topic_ar = '%s — النموذج %s' % (args.title_ar, 'أ' if args.model == 'A' else 'ب')
    elif args.kind == 'source':
        quiz_id = 'Quiz_Ch%02d_S%02d_Source_MCQs' % (args.chapter, args.batch_num)
        topic = '%s — Source Batch %d' % (args.title_en, args.batch_num)
        topic_ar = '%s — دفعة المصدر %d' % (args.title_ar, args.batch_num)
    else:
        quiz_id = 'Quiz_Ch%02d_T%02d_%s' % (args.chapter, args.topic_num, args.slug or 'Topic')
        topic, topic_ar = args.title_en, args.title_ar

    # the app already prints the subject chip and the موضوع badge — a title
    # that repeats either of them shows up twice on the card
    if subject_title and subject_title in topic_ar:
        return fail('title_ar repeats the subject name (%s) — drop it' % subject_title)
    if args.kind == 'topic' and ('النموذج' in topic_ar or 'Model' in topic):
        return fail('a topic bank carries no model suffix — the app adds the موضوع badge itself')

    out = subject_dir / '07_Quizzes_&_Anki' / (quiz_id + '.json')
    if out.exists():
        return fail('already exists: %s' % out.name)

    questions = []
    is_source = (args.kind == 'source')
    for i in range(1, args.questions + 1):
        q_obj = {
            'id': 'q%d' % i,
            'concept_id': ('ase_source_ch%02d_q%02d' % (args.chapter, i)) if is_source else ('TODO_concept_%d' % i),
            'bloom_level': 'Understand',
            'question': 'TODO English stem %d' % i,
            'question_ar': 'TODO نص السؤال %d' % i,
            'options': ['TODO A%d' % i, 'TODO B%d' % i, 'TODO C%d' % i, 'TODO D%d' % i],
            'options_ar': ['TODO أ%d' % i, 'TODO ب%d' % i, 'TODO ج%d' % i, 'TODO د%d' % i],
            'options_en': ['TODO A%d' % i, 'TODO B%d' % i, 'TODO C%d' % i, 'TODO D%d' % i],
            'answer': 'A',
            'correct': 0,
            'explanation': 'TODO English explanation %d' % i,
            'explanation_ar': 'TODO شرح %d' % i,
        }
        if is_source:
            q_obj['answer'] = None
            q_obj['correct'] = None
            q_obj['bank_kind'] = 'source'
            q_obj['source'] = {
                'id': 'TODO_original_source_id_%d' % i,
                'reference': 'TODO original source reference',
                'key_status': 'disputed',
                'note': {'ar': 'TODO لم يُراجع المفتاح بعد', 'en': 'TODO key not reviewed'}
            }
        questions.append(q_obj)

    bank = {
        'schema_version': 2,
        'bank_kind': args.kind if args.kind == 'source' else 'practice',
        'subject_id': args.subject,
        'subject_title': subject_title,
        'semester': 1,
        'semester_label': 'كورس أول',
        'quiz_id': quiz_id,
        'topic': topic,
        'topic_ar': topic_ar,
        'instructor_ar': instructor_ar,
        'instructor': instructor_en,
        'subject': args.subject,
        'questions': questions,
    }
    with io.open(out, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(bank, fh, ensure_ascii=False, indent=2)
        fh.write('\n')

    print('wrote %s (%d TODO questions)' % (out.name, args.questions))
    print('next: fill every TODO, then run the three gates from the skill (balancer, --check --strict, v2+v3).')
    print('the scaffold alone MUST fail the gates — never sync it.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
