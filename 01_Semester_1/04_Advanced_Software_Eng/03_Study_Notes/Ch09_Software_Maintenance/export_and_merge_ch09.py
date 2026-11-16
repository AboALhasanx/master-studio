import os
import subprocess
import fitz  # PyMuPDF

ch09_dir = r"01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch09_Software_Maintenance"
packs = [
    "T1_MCQ",
    "T2_Descriptive",
    "T3_Compare_Analyze",
    "T4_Diagrams",
    "T5_Apply_Select",
    "T7_Calculations",
]

# Export all 6 packs
for pack in packs:
    md_file = os.path.join(ch09_dir, f"{pack}.md")
    pdf_file = os.path.join(ch09_dir, f"{pack}.pdf")
    print(f"[*] Exporting {pack}.md to PDF...")
    cmd = ["python", r"90_Shared_Toolbox\tools\pdf_exporter.py", md_file, "-t", "study_pack"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[!] Error exporting {pack}:")
        print(res.stderr)
        raise RuntimeError(f"Export failed for {pack}")
    print(f"[+] Successfully exported {pack}.pdf")

# Merge into Ch09_Software_Maintenance_Print.pdf
output_pdf_path = os.path.join(ch09_dir, "Ch09_Software_Maintenance_Print.pdf")
print(f"[*] Merging component PDFs into {output_pdf_path}...")

merged_doc = fitz.open()
toc_entries = []
current_page = 1

titles = {
    "T1_MCQ": "T1: Multiple Choice Questions (Publisher Q9.1–Q9.25)",
    "T2_Descriptive": "T2: Descriptive & Conceptual Exercises",
    "T3_Compare_Analyze": "T3: Comparative & Analytical Evaluations",
    "T4_Diagrams": "T4: Structural Diagrams & Process Workflows",
    "T5_Apply_Select": "T5: Applied Decisions & Scenario Matrices",
    "T7_Calculations": "T7: Calculations & Quantitative Models",
}

for pack in packs:
    pack_pdf_path = os.path.join(ch09_dir, f"{pack}.pdf")
    doc = fitz.open(pack_pdf_path)
    page_count = len(doc)
    print(f"   -> Adding {pack}: {page_count} pages (starts at p. {current_page})")
    
    # 1-based level, title, page number
    toc_entries.append([1, titles[pack], current_page])
    merged_doc.insert_pdf(doc)
    current_page += page_count
    doc.close()

merged_doc.set_toc(toc_entries)
merged_doc.save(output_pdf_path)
total_pages = len(merged_doc)
merged_doc.close()

print(f"[+] COMPLETE: Merged {len(packs)} packs into {output_pdf_path}")
print(f"    Total Pages: {total_pages}")
