#!/usr/bin/env python3
"""Capture a separately reviewed source snapshot; never infer an answer key.

Run only after reviewing the source ledger, original-text anchors and publisher
keys. This records that review; it is not a substitute for academic verification.
Existing reviewed items cannot be silently replaced by a new capture.
"""
import argparse
import hashlib
import json
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--items', required=True, type=Path)
    ap.add_argument('--publisher-keys', required=True, type=Path)
    ap.add_argument('--subject', default='04_Advanced_Software_Eng')
    ap.add_argument('--output', required=True, type=Path)
    ap.add_argument('--reviewed', action='store_true', required=True,
                    help='explicit confirmation that the source/answer ledger was reviewed')
    args = ap.parse_args()
    root = (VAULT/'01_Semester_1'/args.subject).resolve()
    try:
        prepared = json.loads(args.items.read_text(encoding='utf-8-sig'))
        key_record = json.loads(args.publisher_keys.read_text(encoding='utf-8'))
        if args.output.exists():
            snapshot = json.loads(args.output.read_text(encoding='utf-8'))
            if snapshot.get('subject_id') != args.subject:
                raise ValueError('existing manifest belongs to another subject')
        else:
            snapshot = {'schema_version':1, 'subject_id':args.subject,
                        'review':'Source anchors and printed publisher key reviewed; unreviewed OCR is not claimed visually verified.',
                        'sources':{}, 'items':{}}

        def record_file(relative):
            file = (root/relative).resolve()
            if Path(relative).is_absolute() or not file.is_relative_to(root):
                raise ValueError('source path must remain inside subject folder')
            digest = hashlib.sha256(file.read_bytes()).hexdigest()
            previous = snapshot['sources'].get(relative)
            if previous and previous != digest:
                raise ValueError(f'previously reviewed source changed: {relative}')
            snapshot['sources'][relative] = digest

        key_file = Path(key_record['pdf']).resolve()
        record_file(key_file.relative_to(root).as_posix())
        for chapter in prepared['chapters']:
            for q in chapter['questions']:
                src = q['source']
                sid = src['id']
                relative = src['path']
                if type(src.get('line')) is not int or src['line'] < 1:
                    raise ValueError(f'{sid}: a real original-source line is required')
                record_file(relative)
                status = src['key_status']
                if status not in ('confirmed','derived','disputed'):
                    raise ValueError(f'{sid}: invalid review status')
                if status == 'disputed':
                    if q['answer'] is not None or q['correct'] is not None:
                        raise ValueError(f'{sid}: disputed questions must remain ungraded')
                elif q['answer'] != key_record['keys'][sid] or q['correct'] != 'ABCD'.index(q['answer']):
                    raise ValueError(f'{sid}: answer differs from reviewed publisher key')
                item = {'question':q['question'], 'options':q['options_en'],
                        'answer':q['answer'], 'correct':q['correct'], 'key_status':status,
                        'publisher_answer':key_record['keys'][sid],
                        'source_path':relative, 'source_line':src['line'], 'reference':src['reference'],
                        'normalizations':src.get('normalizations', [])}
                if sid in snapshot['items'] and snapshot['items'][sid] != item:
                    raise ValueError(f'{sid}: refusing to replace a previously reviewed item')
                snapshot['items'][sid] = item
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(f'Reviewed manifest captured: {len(snapshot["items"])} items; no banks published')
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'REFUSED: {exc}')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
