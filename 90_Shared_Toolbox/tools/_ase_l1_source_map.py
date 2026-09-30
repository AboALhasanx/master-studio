from pypdf import PdfReader
from pathlib import Path
import re, json

books = {
    "Sommerville9": Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\Software-Engineering-9th-Edition-by-Ian-Sommerville.pdf"),
    "Pressman5": Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\Software Engineering by Roger Pressman.pdf"),
    "Agarwal2010": Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\2010 SW_Engineering_and_Testing_An_Introduction_CS_Agarwal.pdf"),
    "Mall4": Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\fundamentals_of_software_engineering_fourth_edition_rajib_mall_1.pdf"),
}

# term -> list of regex patterns
TERMS = {
    "evolving_role": [r"evolving role", r"changing nature of software", r"changing nature"],
    "patriot": [r"patriot"],
    "no_silver_bullet": [r"no silver bullet", r"silver bullet", r"accidental", r"essential complexity"],
    "software_tripartite": [r"code\s*(\+|and)\s*data\s*(\+|and)\s*documentation", r"programs.*data.*documentation", r"programs \+ documentation", r"source code.*data structures.*documentation"],
    "se_definition": [r"software engineering is", r"definition of software engineering", r"IEEE.*software engineering"],
    "software_process_def": [r"software process is", r"software process\b.{0,40}set of", r"a set of activities"],
    "software_crisis": [r"software crisis"],
    "ibm_figures": [r"IBM", r"31%", r"189%", r"94 restarts", r"cost overrun"],
    "myths_management": [r"management myth", r"customer myth", r"practitioner's myth", r"software myth"],
    "error_fault_failure": [r"error.{0,30}fault.{0,30}failure", r"fault.{0,30}error", r"failure.{0,30}fault"],
    "defect": [r"\bdefect\b"],
    "ethics": [r"ethics", r"ACM/IEEE", r"code of ethics", r"professional ethics"],
    "milestones_deliverables": [r"deliverable", r"milestone"],
    "program_vs_software": [r"program versus software", r"program vs\. software", r"software.{0,20}is more than a program"],
}

def scan(path):
    print(f"\n{'='*70}\nBOOK {path.name} size={path.stat().st_size}")
    try:
        r = PdfReader(str(path))
    except Exception as e:
        print("OPEN ERR", e)
        return
    n = len(r.pages)
    print("pages", n)
    # cache pages text
    texts = []
    for i, p in enumerate(r.pages):
        try:
            texts.append((p.extract_text() or "").lower())
        except Exception:
            texts.append("")
    for term, pats in TERMS.items():
        hits = []
        snippets = []
        for i, t in enumerate(texts):
            if not t:
                continue
            for pat in pats:
                for m in re.finditer(pat, t, re.I):
                    hits.append(i + 1)
                    if len(snippets) < 3:
                        a = max(0, m.start() - 60)
                        b = min(len(t), m.end() + 80)
                        snippets.append((i + 1, t[a:b].replace("\n", " ")))
                    break
        uniq = sorted(set(hits))
        print(f"\n--- {term} | hits_pages={len(uniq)} sample_pages={uniq[:25]}")
        for pg, sn in snippets:
            print(f"    p{pg}: ...{sn}...")
    return

for k, p in books.items():
    if p.exists():
        scan(p)
    else:
        print("MISSING", k, p)
