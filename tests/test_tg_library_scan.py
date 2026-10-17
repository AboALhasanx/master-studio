"""Contract tests for ``tg_library_scan`` — the curation half of the shelf.

`tg.py library` sends a manifest; this tool decides what the manifest may hold.
The rules it encodes were each a real decision (see its docstring), so they are
pinned here: the 62-byte display budget, the shelf a folder maps to, staging
that must never be re-sent, and telling same-named files apart.
"""
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent / "90_Shared_Toolbox" / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import tg_library_scan as scan  # noqa: E402


def test_fit_name_keeps_short_names_and_shrinks_long_ones():
    assert scan.fit_name("W01_Intro.pdf") == "W01_Intro.pdf"

    long_arabic = "ضوابط-التقديم-والقبول-للدراسات-العليا-٢٠٢٥-٢٠٢٦-1.pdf"
    fitted = scan.fit_name(long_arabic)
    assert len(fitted.encode("utf-8")) <= scan.NAME_BUDGET
    assert fitted.endswith(".pdf")
    assert fitted != ".pdf", "an Arabic name must keep at least one word"

    long_english = "Q Skills for Success 4 - Reading and Writing (Teacher Book).pdf"
    assert len(scan.fit_name(long_english).encode("utf-8")) <= scan.NAME_BUDGET


def test_classify_puts_every_folder_on_its_own_shelf():
    classify = scan.classify
    assert classify(Path("01_Semester_1/01_Cyber_Security/02_Raw_Materials/W01.pdf")) \
        == (("01-Cyber-Security", "source"), None)
    assert classify(Path("01_Semester_1/04_Advanced_Software_Eng/08_DeepStudy_Ch04/ByType/T1_MCQ.pdf")) \
        == (("04-Advanced-Software-Eng", "exam"), None)
    assert classify(Path("01_Semester_1/01_Cyber_Security/03_Study_Notes/CYBER_UG.pdf")) \
        == (("01-Cyber-Security", "summary"), None)
    assert classify(Path("00_STUDIO_HUB/official_docs/01_postgrad_regulations/x.pdf")) \
        == (("00-University", "rules"), None)


def test_classify_refuses_staging_and_internal_scaffolding():
    classify = scan.classify
    assert classify(Path("00_STUDIO_HUB/telegram/lectures/chapter.pdf")) \
        == (None, "publish-staging")
    assert classify(Path("00_STUDIO_HUB/telegram/catalog/files/"
                         "اللغة الإنجليزية - English Language.pdf")) \
        == (("02-English-Language", "card"), None)
    assert classify(Path("01_Semester_1/03_Data_Mining/_sandbox_trial/x.pdf"))[1] \
        == "internal-folder"
    assert classify(Path("01_Semester_1/03_Data_Mining/03_Study_Notes/00_INDEX.pdf"))[1] \
        == "internal-name"
    assert classify(Path("00_STUDIO_HUB/telegram/catalog/files/_work/scratch.pdf")) \
        == (None, "publish-staging")


def test_disambiguate_tells_same_named_files_apart():
    items = [
        {"file": "01_Semester_1/04_Advanced_Software_Eng/03_Study_Notes/"
                 "Ch01_Introduction/T1_MCQ.pdf",
         "display": "T1_MCQ.pdf", "_abs": __file__},
        {"file": "01_Semester_1/04_Advanced_Software_Eng/03_Study_Notes/"
                 "Ch02_SDLC_Models/T1_MCQ.pdf",
         "display": "T1_MCQ.pdf", "_abs": __file__},
    ]
    scan.disambiguate(items)
    displays = {item["display"] for item in items}
    assert len(displays) == 2, "identical display names must be told apart"
    assert all("Ch0" in display for display in displays)
    assert all(len(d.encode("utf-8")) <= scan.NAME_BUDGET for d in displays)


def _touch(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)


def test_scan_reserves_staging_and_splits_the_two_manifests(tmp_path):
    _touch(tmp_path / "01_Semester_1/01_Cyber_Security/02_Raw_Materials/a.pdf", b"one")
    # the same bytes already went out as a lecture: it must not go again
    _touch(tmp_path / "00_STUDIO_HUB/telegram/lectures/sent.pdf", b"one")
    _touch(tmp_path / "00_STUDIO_HUB/official_docs/rules.pdf", b"two")
    _touch(tmp_path / "01_Semester_1/01_Cyber_Security/03_Study_Notes/note.pdf", b"three")

    manifests, rows = scan.scan(tmp_path, chat="1234")

    queued = [item["file"] for item in manifests["all"]]
    assert "01_Semester_1/01_Cyber_Security/03_Study_Notes/note.pdf" in queued
    assert "01_Semester_1/01_Cyber_Security/02_Raw_Materials/a.pdf" not in queued, \
        "a file byte-identical to published staging must not be queued again"
    assert [item["subject"] for item in manifests["official"]] == ["00-University"]
    assert all(item["kind"] for item in manifests["all"])
    assert any(row["skip"] and row["skip"].startswith("duplicate of")
               for row in rows)
