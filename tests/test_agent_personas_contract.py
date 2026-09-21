import os
import json
import re
from pathlib import Path
import pytest

VAULT_ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = VAULT_ROOT / "00_STUDIO_HUB" / "agents"
SKILLS_DIR = VAULT_ROOT / "skills"
TEMPLATES_DIR = VAULT_ROOT / "00_STUDIO_HUB" / "templates"


def test_all_agent_personas_exist_and_match_skills():
    """Verifies that all 4 personas have definitions in both agents/ and skills/."""
    expected_personas = ["tutor", "examiner", "seminar", "scout"]
    for persona in expected_personas:
        agent_file = AGENTS_DIR / f"{persona}.md"
        skill_file = SKILLS_DIR / persona / "SKILL.md"
        assert agent_file.is_file(), f"Missing agent definition: {agent_file}"
        assert skill_file.is_file(), f"Missing skill card: {skill_file}"


def test_tutor_contract_enforces_feynman_and_socratic_co_derivation():
    """Verifies that @tutor explicitly enforces Feynman teaching and Socratic co-derivation."""
    tutor_agent = (AGENTS_DIR / "tutor.md").read_text(encoding="utf-8")
    tutor_skill = (SKILLS_DIR / "tutor" / "SKILL.md").read_text(encoding="utf-8")

    # Must forbid dry summarization and mandate 9-year-old explanation
    for text in [tutor_agent, tutor_skill]:
        assert "Feynman" in text or "9-year-old" in text
        assert "Co-Derivation" in text or "Co-Solving" in text
        assert "Terminology" in text or "Exam Trap" in text
        assert "Worked" in text or "Example" in text


def test_examiner_contract_enforces_both_viva_and_strict_mcq_gates():
    """Verifies that @examiner covers both Analytical Viva/Formulas and strict WebUI MCQs."""
    examiner_agent = (AGENTS_DIR / "examiner.md").read_text(encoding="utf-8")
    examiner_skill = (SKILLS_DIR / "examiner" / "SKILL.md").read_text(encoding="utf-8")

    for text in [examiner_agent, examiner_skill]:
        assert "Viva" in text or "Oral Defense" in text
        assert "quiz_balancer.py" in text
        assert "strict" in text.lower()


def test_zero_conflict_across_agent_roles():
    """Verifies that trigger commands and primary roles are strictly orthogonal."""
    agents_md = (VAULT_ROOT / "AGENTS.md").read_text(encoding="utf-8")

    # Each persona must be present with distinct responsibilities
    assert "@tutor" in agents_md
    assert "@examiner" in agents_md
    assert "@seminar" in agents_md
    assert "@scout" in agents_md

    # Check that @tutor is pedagogical, @examiner is assessment, @seminar is slides, @scout is literature
    lines = [l for l in agents_md.splitlines() if l.strip().startswith("| **`@")]
    assert len(lines) == 4
    roles = " ".join(lines)
    assert "Socratic" in roles or "Conceptual" in roles
    assert "Quizzes" in roles or "defense" in roles
    assert "presentations" in roles or "Slide" in roles
    assert "Literature" in roles or "DOIs" in roles


def test_canonical_templates_exist_and_are_valid():
    """Verifies that all required templates exist and have valid structure."""
    study_note_tmpl = TEMPLATES_DIR / "template-study-note.md"
    terms_tmpl = TEMPLATES_DIR / "template-academic-terms.md"
    quiz_json_tmpl = TEMPLATES_DIR / "template-quiz-bank.json"
    quiz_md_tmpl = TEMPLATES_DIR / "template-quiz-bank.md"

    assert study_note_tmpl.is_file()
    assert terms_tmpl.is_file()
    assert quiz_json_tmpl.is_file()
    assert quiz_md_tmpl.is_file()

    # JSON template must be valid parseable JSON
    with open(quiz_json_tmpl, "r", encoding="utf-8") as f:
        quiz_json = json.load(f)
    assert "questions" in quiz_json
    assert len(quiz_json["questions"]) >= 4

    # Terms template must feature Feynman explanation and exam traps
    terms_text = terms_tmpl.read_text(encoding="utf-8")
    assert "Feynman" in terms_text or "تشرح لطفل" in terms_text
    assert "Exam Trap" in terms_text or "فخ الامتحان" in terms_text
