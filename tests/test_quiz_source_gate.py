"""Unit tests for quiz_source_gate.py standalone validator.

Verifies:
  - Source bank valid passes
  - Disputed ungraded items pass with answer: null, correct: null and bilingual note
  - Disputed with guessed key fails
  - Disputed with missing bilingual note fails
  - Practice bank rejected (wrong bank_kind)
  - Unknown bank_kind rejected
  - Missing source metadata rejected
  - Manifest tamper / alteration detection
"""
import json
import pytest
from pathlib import Path
import sys

tools_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox" / "tools"
if str(tools_path) not in sys.path:
    sys.path.insert(0, str(tools_path))

from quiz_source_gate import validate_source_bank, validate_source_collection


@pytest.fixture
def base_source_bank():
    return {
        "schema_version": 2,
        "bank_kind": "source",
        "subject_id": "04_Advanced_Software_Eng",
        "subject_title": "Advanced Software Engineering",
        "semester": 1,
        "semester_label": "Semester 1",
        "quiz_id": "Quiz_Ch01_S01_Source_MCQs",
        "topic": "Source MCQs - Batch 1",
        "instructor_ar": "د. علي",
        "questions": [
            {
                "id": "q1",
                "concept_id": "ase_source_ch01_q01",
                "bloom_level": "Understand",
                "bank_kind": "source",
                "source": {
                    "id": "SRC_Q1",
                    "reference": "Slide 10",
                    "key_status": "confirmed",
                    "note": {"ar": "مفتاح مؤكد", "en": "Confirmed key"}
                },
                "question": "What is the primary goal of software engineering?",
                "question_ar": "ما هو الهدف الأساسي لهندسة البرمجيات؟",
                "options": ["Quality software on time", "Fast coding only", "Writing documentation only", "Avoiding all meetings"],
                "options_en": ["Quality software on time", "Fast coding only", "Writing documentation only", "Avoiding all meetings"],
                "options_ar": ["برمجيات عالية الجودة في الوقت المحدد", "البرمجة السريعة فقط", "كتابة الوثائق فقط", "تجنب كل الاجتماعات"],
                "answer": "A",
                "correct": 0,
                "explanation": "Software engineering aims for professional quality delivered economically.",
                "explanation_ar": "تهدف هندسة البرمجيات لإنتاج برمجيات احترافية ذات جودة واقتصادية."
            },
            {
                "id": "q2",
                "concept_id": "ase_source_ch01_q02",
                "bloom_level": "Apply",
                "bank_kind": "source",
                "source": {
                    "id": "SRC_Q2",
                    "reference": "Exam 2022 Q3",
                    "key_status": "derived",
                    "note": {"ar": "مستنتج من النص الأصلي", "en": "Derived from source textbook"}
                },
                "question": "Which model is best suited when requirements are well understood from the start?",
                "question_ar": "أي نموذج هو الأنسب عندما تكون المتطلبات مفهومة جيداً من البداية؟",
                "options": ["Waterfall model", "Evolutionary model", "Throwaway prototyping", "Extreme Programming"],
                "options_en": ["Waterfall model", "Evolutionary model", "Throwaway prototyping", "Extreme Programming"],
                "options_ar": ["نموذج الشلال", "النموذج التطوري", "النمذجة الأولية المؤقتة", "البرمجة القصوى"],
                "answer": "A",
                "correct": 0,
                "explanation": "Waterfall assumes stable and known requirements upfront.",
                "explanation_ar": "يفترض نموذج الشلال متطلبات مستقرة ومفهومة مسبقاً."
            },
            {
                "id": "q3",
                "concept_id": "ase_source_ch01_q03",
                "bloom_level": "Remember",
                "bank_kind": "source",
                "source": {
                    "id": "SRC_Q3",
                    "reference": "Slide 25",
                    "key_status": "confirmed",
                    "note": {"ar": "معتمد", "en": "Confirmed"}
                },
                "question": "Software costs are dominated by which phase?",
                "question_ar": "أي مرحلة تستحوذ على الحصة الأكبر من تكاليف البرمجيات؟",
                "options": ["Specification", "Design", "Implementation", "Maintenance"],
                "options_en": ["Specification", "Design", "Implementation", "Maintenance"],
                "options_ar": ["التوصيف", "التصميم", "التنفيذ", "الصيانة والتطوير"],
                "answer": "D",
                "correct": 3,
                "explanation": "Evolution and maintenance take the majority of lifecycle costs.",
                "explanation_ar": "تستحوذ الصيانة والتطوير على الحصة الأكبر من التكلفة الإجمالية."
            },
            {
                "id": "q4",
                "concept_id": "ase_source_ch01_q04",
                "bloom_level": "Analyze",
                "bank_kind": "source",
                "source": {
                    "id": "SRC_Q4",
                    "reference": "Exam 2023 Q12",
                    "key_status": "disputed",
                    "note": {
                        "ar": "صياغة السؤال غامضة وتحتمل خيارين B و C",
                        "en": "Stem wording is ambiguous and admits both B and C under different definitions"
                    }
                },
                "question": "Is software engineering synonymous with computer science?",
                "question_ar": "هل هندسة البرمجيات مرادفة لعلوم الحاسوب؟",
                "options": ["Always yes", "No, CS focuses on theory while SE focuses on practical delivery", "Partially overlapping disciplines", "Never related"],
                "options_en": ["Always yes", "No, CS focuses on theory while SE focuses on practical delivery", "Partially overlapping disciplines", "Never related"],
                "options_ar": ["نعم دائماً", "لا، علوم الحاسوب تركز على النظريات والهندسة تركز على التطبيق العملي", "تخصصان متداخلان جزئياً", "غير مرتبطين إطلاقاً"],
                "answer": None,
                "correct": None,
                "explanation": "The relationship can be defined as distinct focus or partial overlap.",
                "explanation_ar": "يمكن النظر للعلاقة كتباين في التركيز أو كتداخل عملي ونظري."
            }
        ]
    }


def test_validate_source_bank_success(base_source_bank):
    ok, errs, warns = validate_source_bank(base_source_bank)
    assert ok is True, f"Errors: {errs}"
    assert errs == []


def test_disputed_ungraded_with_guessed_key_fails(base_source_bank):
    # Guessed key on disputed question must fail
    base_source_bank["questions"][3]["answer"] = "B"
    base_source_bank["questions"][3]["correct"] = 1
    ok, errs, warns = validate_source_bank(base_source_bank)
    assert ok is False
    assert any("disputed source item must have answer: null and correct: null" in e for e in errs)


def test_disputed_missing_bilingual_note_fails(base_source_bank):
    base_source_bank["questions"][3]["source"]["note"] = {"ar": "", "en": "Only en"}
    ok, errs, warns = validate_source_bank(base_source_bank)
    assert ok is False
    assert any("requires nonempty bilingual 'source.note'" in e for e in errs)


def test_reject_practice_bank(base_source_bank):
    base_source_bank["bank_kind"] = "practice"
    ok, errs, warns = validate_source_bank(base_source_bank)
    assert ok is False
    assert any("quiz_source_gate only validates 'source' banks" in e for e in errs)


def test_reject_unknown_bank_kind(base_source_bank):
    base_source_bank["bank_kind"] = "exam"
    ok, errs, warns = validate_source_bank(base_source_bank)
    assert ok is False
    assert any("invalid bank_kind 'exam'" in e for e in errs)


def test_manifest_tamper_detection(base_source_bank):
    manifest = {"items": {q['source']['id']: {'question': q['question'], 'options': list(q['options'])}
                          for q in base_source_bank['questions']}}
    # Clean check passes
    ok, errs, warns = validate_source_bank(base_source_bank, manifest=manifest)
    assert ok is True, f"Errors: {errs}"

    # Tampered stem
    base_source_bank["questions"][0]["question"] = "Tampered stem text"
    ok, errs, warns = validate_source_bank(base_source_bank, manifest=manifest)
    assert ok is False
    assert any("English stem does not match source manifest" in e for e in errs)


def test_publication_requires_independent_manifest(base_source_bank):
    ok, errors, _ = validate_source_bank(base_source_bank, check_publish=True)
    assert not ok
    assert any('source_manifest is required' in e for e in errors)


def test_missing_manifest_item_cannot_silently_pass(base_source_bank):
    ok, errors, _ = validate_source_bank(base_source_bank, manifest={'items': {'unrelated': {}}})
    assert not ok
    assert any('missing source manifest item' in e for e in errors)


def test_source_null_confirmed_key_reports_error_without_crashing(base_source_bank):
    q = base_source_bank['questions'][0]
    q['answer'] = q['correct'] = None
    ok, errors, _ = validate_source_bank(base_source_bank)
    assert not ok and errors


def test_empty_source_bank_returns_consistent_tuple(base_source_bank):
    base_source_bank['questions'] = []
    ok, errors, warnings = validate_source_bank(base_source_bank)
    assert not ok and errors


def test_source_duplicate_provenance_id_fails(base_source_bank):
    base_source_bank['questions'][1]['source']['id'] = 'SRC_Q1'
    ok, errors, _ = validate_source_bank(base_source_bank)
    assert not ok
    assert any('duplicate source.id' in e for e in errors)


def test_manifest_without_review_stamp_fails(base_source_bank):
    manifest = {'subject_id': '04_Advanced_Software_Eng',
                'sources': {}, 'items': {}}
    ok, errors, _ = validate_source_bank(base_source_bank, manifest=manifest, check_publish=True)
    assert not ok
    assert any('reviewed schema/review stamp' in e for e in errors)


def test_source_file_from_another_chapter_fails(base_source_bank):
    base_source_bank['questions'][0]['source']['path'] = '02_Raw_Materials/New/Ch02_Other.md'
    ok, errors, _ = validate_source_bank(base_source_bank)
    assert not ok
    assert any('another chapter' in e for e in errors)


def test_reversed_source_order_fails(base_source_bank):
    for i, q in enumerate(base_source_bank['questions'], 1):
        q['source']['id'] = f'1.{i}'
    base_source_bank['questions'] = list(reversed(base_source_bank['questions']))
    ok, errors, _ = validate_source_bank(base_source_bank)
    assert not ok
    assert any('order is not ascending' in e for e in errors)


def test_duplicate_source_across_banks_fails(base_source_bank):
    second = json.loads(json.dumps(base_source_bank))
    second['quiz_id'] = 'Quiz_Ch01_S02_Source_MCQs'
    errors = validate_source_collection([(Path('a.json'), base_source_bank), (Path('b.json'), second)])
    assert errors
