import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from publish_quizzes import merge_question


class MergeQuestionTests(unittest.TestCase):
    def test_new_vault_stem_wins_over_stale_portal_text_alias(self):
        vault = {
            "id": "q1",
            "question": "Updated English stem",
            "question_ar": "صياغة عربية جديدة",
        }
        portal = {
            "text": "Old English stem",
            "stem": {"en": "Old English stem", "ar": "ترجمة عربية سابقة"},
        }

        merged = merge_question(vault, portal)

        self.assertEqual(merged["question"], "Updated English stem")
        self.assertNotIn("text", merged)
        self.assertEqual(merged["question_ar"], "صياغة عربية جديدة")

    def test_portal_translation_is_still_filled_when_vault_is_blank(self):
        vault = {"id": "q1", "question": "English stem", "question_ar": ""}
        portal = {
            "text": "English stem",
            "stem": {"en": "English stem", "ar": "الترجمة المحفوظة"},
        }

        merged = merge_question(vault, portal)

        self.assertEqual(merged["question_ar"], "الترجمة المحفوظة")


if __name__ == "__main__":
    unittest.main()
