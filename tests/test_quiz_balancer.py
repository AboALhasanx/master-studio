import json
import pytest
from pathlib import Path
import sys

# Ensure tools directory is in sys.path
tools_path = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox" / "tools"
if str(tools_path) not in sys.path:
    sys.path.insert(0, str(tools_path))
from quiz_balancer import analyze_quiz, balance_quiz, clean_parenthetical_bloat, validate_strict_gate

# --------------------------------------------------------------------------
# 1. Clean Parenthetical Bloat Tests
# --------------------------------------------------------------------------
def test_clean_parenthetical_bloat_removes_english_echoes():
    raw_ar = "المعلومات (information)"
    cleaned = clean_parenthetical_bloat(raw_ar)
    assert cleaned == "المعلومات"

    raw_complex = "خوارزميات رياضية معقّدة (complex mathematical algorithms)"
    cleaned_complex = clean_parenthetical_bloat(raw_complex)
    assert cleaned_complex == "خوارزميات رياضية معقّدة"


def test_clean_parenthetical_bloat_preserves_uppercase_acronyms():
    raw_kdd = "Knowledge Discovery of Data (KDD)"
    cleaned_kdd = clean_parenthetical_bloat(raw_kdd)
    assert cleaned_kdd == "Knowledge Discovery of Data (KDD)"

    raw_otp = "One-Time Password (OTP)"
    cleaned_otp = clean_parenthetical_bloat(raw_otp)
    assert cleaned_otp == "One-Time Password (OTP)"


def test_clean_parenthetical_bloat_handles_non_string_safely():
    assert clean_parenthetical_bloat(None) is None
    assert clean_parenthetical_bloat(123) == 123
    assert clean_parenthetical_bloat("") == ""


# --------------------------------------------------------------------------
# 2. Analyze Quiz Tests
# --------------------------------------------------------------------------
def test_analyze_quiz_detects_severe_positional_bias():
    # Construct a 10-question quiz where 9 answers are "B"
    quiz = {
        "questions": [
            {
                "id": f"q{i}",
                "options": ["A opt", "B opt", "C opt", "D opt"],
                "answer": "B" if i < 9 else "A"
            }
            for i in range(10)
        ]
    }
    stats = analyze_quiz(quiz)
    assert stats["total"] == 10
    assert stats["distribution"]["B"]["percentage"] == 90.0
    dom_letter, dom_count = stats["dominant_letter"]
    assert dom_letter == "B"
    assert dom_count == 9


def test_analyze_quiz_detects_length_disparity_giveaway():
    quiz = {
        "questions": [
            {
                "id": "q1",
                "options": [
                    "Short",
                    "This is an extremely long, highly detailed, and thoroughly qualified answer that gives away the solution completely",
                    "Short",
                    "Short"
                ],
                "answer": "B"
            }
        ]
    }
    stats = analyze_quiz(quiz)
    assert len(stats["length_disparities"]) == 1
    disp = stats["length_disparities"][0]
    assert disp["id"] == "q1"
    assert disp["ratio"] > 5.0


def test_analyze_quiz_handles_empty_quiz():
    stats = analyze_quiz({})
    assert stats["total"] == 0
    assert stats["distribution"] == {}
    assert stats["length_disparities"] == []


# --------------------------------------------------------------------------
# 3. Balance Quiz Algorithmic Distribution Tests
# --------------------------------------------------------------------------
def test_balance_quiz_redistributes_biased_answers():
    # 24 questions, all originally in B
    quiz = {
        "questions": [
            {
                "id": f"q{i}",
                "options": [f"Opt A {i}", f"Correct Opt {i}", f"Opt C {i}", f"Opt D {i}"],
                "options_en": [f"En A {i}", f"Correct En {i}", f"En C {i}", f"En D {i}"],
                "answer": "B"
            }
            for i in range(24)
        ]
    }
    balanced = balance_quiz(quiz, seed=123, clean_bloat=True)
    stats = analyze_quiz(balanced)

    # In a 24-question quiz, each letter should have exactly 6 answers (25.0%)
    for letter in ["A", "B", "C", "D"]:
        assert stats["distribution"][letter]["count"] == 6
        assert stats["distribution"][letter]["percentage"] == 25.0


def test_balance_quiz_preserves_option_mapping():
    quiz = {
        "questions": [
            {
                "id": "q1",
                "options": ["Wrong 1", "THE_CORRECT_ANSWER", "Wrong 2", "Wrong 3"],
                "options_en": ["Wrong En 1", "THE_CORRECT_EN", "Wrong En 2", "Wrong En 3"],
                "answer": "B"
            }
        ]
    }
    balanced = balance_quiz(quiz, seed=999)
    q = balanced["questions"][0]
    new_ans = q["answer"]
    new_idx = ["A", "B", "C", "D"].index(new_ans)

    # The correct text MUST land at the new answer index
    assert q["options"][new_idx] == "THE_CORRECT_ANSWER"
    assert q["options_en"][new_idx] == "THE_CORRECT_EN"


def test_balance_quiz_handles_dictionary_options():
    quiz = {
        "questions": [
            {
                "id": "q1",
                "options": {
                    "A": "Dict Opt A",
                    "B": "DICT_CORRECT",
                    "C": "Dict Opt C",
                    "D": "Dict Opt D"
                },
                "answer": "B"
            }
        ]
    }
    balanced = balance_quiz(quiz, seed=42)
    q = balanced["questions"][0]
    new_ans = q["answer"]
    new_idx = ["A", "B", "C", "D"].index(new_ans)
    assert q["options"][new_idx] == "DICT_CORRECT"
# --------------------------------------------------------------------------
# 4. Strict Psychometric Gate Tests (TDD)
# --------------------------------------------------------------------------
def test_validate_strict_gate_fails_on_length_disparity():
    # Quiz with a 3-line correct answer and 1-line distractors
    quiz = {
        "questions": [
            {
                "id": "q1",
                "concept_id": "test_concept",
                "bloom_level": "Apply",
                "question": "Test question?",
                "question_ar": "سؤال تجريبي؟",
                "options": [
                    "Short distractor 1",
                    "This is an excessively long, highly detailed, and thoroughly elaborated correct answer that acts as an obvious tell",
                    "Short distractor 2",
                    "Short distractor 3"
                ],
                "options_ar": ["مشتت 1", "خيار صحيح طويل جداً ومليء بالتفاصيل ويعتبر علامة واضحة على الجواب", "مشتت 2", "مشتت 3"],
                "options_en": ["Short 1", "Excessively long correct answer with full details", "Short 2", "Short 3"],
                "answer": "B"
            }
        ]
    }
    is_valid, errors = validate_strict_gate(quiz)
    assert is_valid is False
    assert any("length disparity" in err.lower() or "longer than distractors" in err.lower() for err in errors)


def test_validate_strict_gate_fails_on_positional_bias():
    # 10 questions, 9 on Option B
    quiz = {
        "questions": [
            {
                "id": f"q{i}",
                "concept_id": f"c_{i}",
                "bloom_level": "Understand",
                "question": f"Q{i}?",
                "question_ar": f"سؤال {i}؟",
                "options": ["Option A of equal length", "Option B of equal length", "Option C of equal length", "Option D of equal length"],
                "options_ar": ["خيار أ بطول متساوي", "خيار ب بطول متساوي", "خيار ج بطول متساوي", "خيار د بطول متساوي"],
                "options_en": ["Option A equal", "Option B equal", "Option C equal", "Option D equal"],
                "answer": "B" if i < 9 else "A"
            }
            for i in range(10)
        ]
    }
    is_valid, errors = validate_strict_gate(quiz)
    assert is_valid is False
    assert any("positional bias" in err.lower() or "dominant" in err.lower() for err in errors)


def test_validate_strict_gate_fails_on_parenthetical_bloat():
    quiz = {
        "questions": [
            {
                "id": "q1",
                "concept_id": "c1",
                "bloom_level": "Understand",
                "question": "Q1?",
                "question_ar": "سؤال؟",
                "options": [
                    "المعلومات (information)",
                    "العتاد المادي فقط (hardware components)",
                    "البرمجيات (software)",
                    "الشبكات (networks)"
                ],
                "options_ar": ["المعلومات (information)", "العتاد المادي فقط (hardware components)", "البرمجيات (software)", "الشبكات (networks)"],
                "options_en": ["Information", "Hardware only", "Software", "Networks"],
                "answer": "A"
            }
        ]
    }
    is_valid, errors = validate_strict_gate(quiz)
    assert is_valid is False
    assert any("parenthetical" in err.lower() or "bloat" in err.lower() for err in errors)


def test_validate_strict_gate_passes_on_compliant_quiz():
    # 4 questions perfectly balanced, equal length, clean terms, full schema
    quiz = {
        "questions": [
            {
                "id": f"q{i+1}",
                "concept_id": f"concept_{i+1}",
                "bloom_level": "Understand",
                "question": f"Formal English question number {i+1}?",
                "question_ar": f"سؤال أكاديمي رقم {i+1} بالعربية؟",
                "options": [
                    "First option of exactly equal length.",
                    "Second option of exactly equal length.",
                    "Third option of exactly equal length.",
                    "Fourth option of exactly equal length."
                ],
                "options_ar": [
                    "الخيار الأول بطول متساوٍ ودقيق.",
                    "الخيار الثاني بطول متساوٍ ودقيق.",
                    "الخيار الثالث بطول متساوٍ ودقيق.",
                    "الخيار الرابع بطول متساوٍ ودقيق."
                ],
                "options_en": [
                    "First option of exactly equal length.",
                    "Second option of exactly equal length.",
                    "Third option of exactly equal length.",
                    "Fourth option of exactly equal length."
                ],
                "answer": ["A", "B", "C", "D"][i]
            }
            for i in range(4)
        ]
    }
    is_valid, errors = validate_strict_gate(quiz)
    assert is_valid is True
    assert len(errors) == 0
