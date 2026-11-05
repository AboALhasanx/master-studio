import importlib.util
import unittest
from pathlib import Path


GATE_PATH = Path(__file__).resolve().parents[1] / "quiz_quality_gate.py"
SPEC = importlib.util.spec_from_file_location("quiz_quality_gate", GATE_PATH)
quality_gate = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(quality_gate)


class PaddingSuffixGateTests(unittest.TestCase):
    def test_isolated_natural_suffix_does_not_fail(self):
        choices = [("en", f"plausible distractor {i}") for i in range(63)]
        choices.append(("en", "the component used here"))
        failed, hits, total = quality_gate.padding_share_exceeds_gate(choices)
        self.assertFalse(failed)
        self.assertEqual((hits, total), (1, 64))

    def test_repeated_english_suffix_padding_fails(self):
        choices = [("en", f"plausible distractor {i}") for i in range(48)]
        choices.extend(("en", f"plausible distractor {i} here again") for i in range(8))
        choices.extend(("ar", f"خيار معقول {i}") for i in range(8))
        failed, hits, total = quality_gate.padding_share_exceeds_gate(choices)
        self.assertTrue(failed)
        self.assertEqual((hits, total), (8, 64))

    def test_repeated_arabic_suffix_padding_fails(self):
        choices = [("en", f"plausible distractor {i}") for i in range(48)]
        choices.extend(("ar", f"خيار معقول {i}") for i in range(8))
        choices.extend(("ar", f"خيار معقول {i} هنا مجدداً") for i in range(8))
        failed, hits, total = quality_gate.padding_share_exceeds_gate(choices)
        self.assertTrue(failed)
        self.assertEqual((hits, total), (8, 64))


if __name__ == "__main__":
    unittest.main()
