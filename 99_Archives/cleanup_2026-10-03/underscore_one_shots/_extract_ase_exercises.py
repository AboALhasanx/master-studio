from pypdf import PdfReader
from pathlib import Path

base = Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\Aggarwal_Singh_SE_PPT_Chapters")
out_dir = Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes")
out_dir.mkdir(parents=True, exist_ok=True)

def grab_exercises(pdf_path, label):
    r = PdfReader(str(pdf_path))
    parts = []
    for i, page in enumerate(r.pages):
        t = page.extract_text() or ""
        if "Exercise" in t:
            parts.append(f"\n### {label} p.{i + 1}\n\n{t.strip()}\n")
    return parts

lines = [
    "# Aggarwal & Singh — End-of-Chapter Exercises (Ch.1–3)\n",
    "> Source: publisher companion PDFs (3rd ed., New Age International, 2007).\n",
    "> Doctor covered ~3 chapters. These are the book's own review questions — high exam value.\n",
]

for name, label in [
    ("chapter_1_introduction.pdf", "Ch.1 Introduction"),
    ("chapter_2_software_development_life_cycle_models.pdf", "Ch.2 SDLC Models"),
    ("chapter_3_software_requirements.pdf", "Ch.3 Software Requirements / SRS"),
]:
    lines.append(f"\n---\n\n## {label}\n")
    lines.extend(grab_exercises(base / name, label))

path = out_dir / "ASE_Ch1-3_Exercises_Aggarwal.md"
path.write_text("\n".join(lines), encoding="utf-8")
print("wrote", path, "bytes", path.stat().st_size)
