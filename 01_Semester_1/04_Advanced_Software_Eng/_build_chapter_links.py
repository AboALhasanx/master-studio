"""Generate per-chapter link files for ASE, mapping Sommerville videos to the
Aggarwal & Singh chapter structure (the course chapters)."""
from pathlib import Path

OUT = Path(r"C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\ASE_LINKS_BY_CHAPTER")
OUT.mkdir(parents=True, exist_ok=True)

CH = {
 "01": dict(
  topic="Introduction to Software Engineering",
  slides="chapter_1_introduction.pdf",
  videos=[
   ("Ten Questions about Software Engineering (*)", "https://www.youtube.com/watch?v=gi5kxGslkNc"),
   ("Why Software Engineering Matters (*)", "https://www.youtube.com/watch?v=R3NzTt0BTWE"),
   ("The Conscience of Computing Professionals – Code of Ethics", "https://www.youtube.com/watch?v=d91MTV9AlNg"),
   ("An introduction to critical systems", "https://www.youtube.com/watch?v=msp05wJ7fD4"),
   ("System dependability", "https://www.youtube.com/watch?v=Oa27Xej1KdY"),
   ("Introducing sociotechnical systems (*)", "https://www.youtube.com/watch?v=xdFftbIToV0"),
  ],
  qs=["What is Software and Software Engineering? (NRCMEC U-I)",
      "Discuss about changing nature of software.",
      "Define Software. Explain the nature of software."],
 ),
 "02": dict(
  topic="Software Development Life Cycle Models",
  slides="chapter_2_software_development_life_cycle_models.pdf",
  videos=[
   ("Plan-driven and Agile Software Processes (*)", "https://www.youtube.com/watch?v=q8X2Rk5sRFI"),
   ("Fundamental Activities in Software Engineering (*)", "https://www.youtube.com/watch?v=Z2no7DxDWRI"),
   ("The Software Process", "https://www.youtube.com/watch?v=YMbAdgb6pG8"),
   ("Software Development Life Cycle", "https://www.youtube.com/watch?v=9STHYg7igIQ"),
   ("Genesis Consulting: Agile vs Waterfall", "https://www.youtube.com/watch?v=jL1VOF5JgPQ"),
   ("Software Testing Training – V model", "https://www.youtube.com/watch?v=zzPDHqR2qhU"),
   ("What is agile development (Part 1)", "https://www.youtube.com/watch?v=-zDct5d2smY"),
   ("What is agile development (Part 2)", "https://www.youtube.com/watch?v=N4NQ6rZiQ5Q"),
   ("Scrum 101 Part 1", "https://www.youtube.com/watch?v=aQrsVfjbQZ4"),
   ("Scrum 101 Part 2", "https://www.youtube.com/watch?v=29dnS7XGgqs"),
   ("Strengths and Weaknesses of Extreme Programming", "https://www.youtube.com/watch?v=LkhLZ7_KZ5w"),
   ("Test-driven development", "https://www.youtube.com/watch?v=dWayn0QsJr8"),
   ("Scaling agile methods (*)", "https://www.youtube.com/watch?v=GuK46hw3CyI"),
  ],
  qs=["What is Software Development Life Cycle. (NRCMEC U-I)",
      "List the task regions in the spiral model.",
      "Distinguish between software process and project.",
      "How do agile principles address the challenges of traditional development? (SEPM Module 1)"],
 ),
 "03": dict(
  topic="Software Requirements (SRS)",
  slides="chapter_3_software_requirements.pdf",
  videos=[
   ("An introduction to requirements engineering (*)", "https://www.youtube.com/watch?v=Ec0s0z5uXQ8"),
   ("What is a requirement?", "https://www.youtube.com/watch?v=u2GD4-7tHqc"),
   ("Requirements engineering processes (*)", "https://www.youtube.com/watch?v=GSe4xIy-iBE"),
   ("Stakeholders, viewpoints and concerns (*)", "https://www.youtube.com/watch?v=P5X-ridjaOY"),
   ("Requirements engineering challenges (*)", "https://www.youtube.com/watch?v=bK-y0CaGkhU"),
   ("User stories (*)", "https://www.youtube.com/watch?v=UpYdVSV3dG8"),
   ("UML 2.0 video tutorial (Derek Banas)", "https://www.youtube.com/watch?v=OkC7HKtiZC0"),
   ("UML Tutorial – Use Case, Activity, Sequence", "https://www.youtube.com/watch?v=RMuMz5hQMf4"),
  ],
  qs=["What is SRS? What are the characteristics of a good SRS?",
      "Explain the requirements engineering process.",
      "Difference between functional and non-functional requirements."],
 ),
 "04": dict(
  topic="Software Project Planning",
  slides="chapter_4_software_project_planning.pdf",
  videos=[
   ("Why software project management is different?", "https://www.youtube.com/watch?v=TYBVAvWkG6M"),
   ("Risk management fundamentals", "https://www.youtube.com/watch?v=gmTSb1A2VBc"),
   ("Ten deadly sins of software estimation", "https://www.youtube.com/watch?v=s9AFpnvkmyM"),
   ("Gantt Chart Tutorial", "https://www.youtube.com/watch?v=rm_iWKoOd0U"),
   ("Create a Basic Gantt Chart in Excel", "https://www.youtube.com/watch?v=QdsjVN3du78"),
   ("Estimating Coding Costs Using COCOMO", "https://www.youtube.com/watch?v=byt7WiVQcTw"),
   ("Agile estimation", "https://www.youtube.com/watch?v=7nTxdl29ePY"),
  ],
  qs=["Explain COCOMO model with an example.",
      "What is function point analysis? Compute FP for a given problem.",
      "Explain risk management in software projects."],
 ),
 "05": dict(
  topic="Software Design",
  slides="chapter_5_software_design.pdf",
  videos=[
   ("What is software architecture?", "https://www.youtube.com/watch?v=Rn1g6V-vlHw"),
   ("Architecting Software the SEI Way", "http://resources.sei.cmu.edu/library/asset-view.cfm?assetid=21534"),
   ("Design patterns – introduction", "https://www.youtube.com/watch?v=0KhDDYwngyQ"),
   ("Introduction to Distributed Systems", "https://www.youtube.com/watch?v=F_4BCNl0iVk"),
   ("Client-server architecture", "https://www.youtube.com/watch?v=eRhxxFefAeA"),
   ("Software as a service", "https://www.youtube.com/watch?v=3DCqdY3yyDE"),
   ("Introducing OCL", "https://www.youtube.com/watch?v=c4JHSHgZ1vk"),
  ],
  qs=["Explain coupling and cohesion with types and examples.",
      "What is modularity? Explain the design process.",
      "Difference between top-down and bottom-up design."],
 ),
 "06": dict(
  topic="Software Metrics",
  slides="chapter_6_software_metrics.pdf",
  videos=[
   ("Software metrics", "https://www.youtube.com/watch?v=3CnuwmF-e-Y"),
   ("Software quality assurance", "https://www.youtube.com/watch?v=5_cTi5xBlYg"),
   ("Estimating Coding Costs Using COCOMO", "https://www.youtube.com/watch?v=byt7WiVQcTw"),
  ],
  qs=["Define software metrics. Explain its types.",
      "What is cyclomatic complexity? Compute for a given flow graph.",
      "Explain Halstead's metrics."],
 ),
 "07": dict(
  topic="Software Reliability",
  slides="chapter_7_software_reliability.pdf",
  videos=[
   ("Availability and reliability (*)", "https://www.youtube.com/watch?v=C94_arCm-Mw"),
   ("Airbus FCS – software and hardware redundancy (*)", "https://www.youtube.com/watch?v=EOexjozpBdI"),
   ("Reliability 6 – Software Reliability", "https://www.youtube.com/watch?v=wv51aF_qODA"),
   ("FMEA and Fault-trees", "https://www.youtube.com/watch?v=S0Tfjrze3Vg"),
   ("System safety (*)", "https://www.youtube.com/watch?v=IITymheitxw"),
   ("Ariane launch failure", "https://www.youtube.com/watch?v=W3YJeoYgozw"),
  ],
  qs=["Define software reliability. Explain reliability metrics.",
      "What is MTBF and MTTF?",
      "Explain reliability growth models."],
 ),
 "08": dict(
  topic="Software Testing",
  slides="chapter_8_software_testing.pdf",
  videos=[
   ("A beginners guide to testing", "https://www.youtube.com/watch?v=9hz9aQztdrw"),
   ("Equivalence partitioning & boundary value analysis", "https://www.youtube.com/watch?v=uydAyjqTSiw"),
   ("Open-lecture by James Bach on software testing", "https://www.youtube.com/watch?v=ILkT_HV9DVU"),
   ("Test-driven development", "https://www.youtube.com/watch?v=dWayn0QsJr8"),
   ("Software Testing Training – V model", "https://www.youtube.com/watch?v=zzPDHqR2qhU"),
   ("Security Testing Fundamentals", "https://www.youtube.com/watch?v=PYwqyVlH8lQ"),
  ],
  qs=["What is software testing? Explain its types.",
      "Explain black-box and white-box testing.",
      "What is equivalence partitioning and boundary value analysis?"],
 ),
 "09": dict(
  topic="Software Maintenance",
  slides="chapter_9_software_maintenance.pdf",
  videos=[
   ("Legacy systems", "https://www.youtube.com/watch?v=sJPRgYHHA_w"),
   ("Lecture 25: Software Evolution (IIT Bombay)", "https://www.youtube.com/watch?v=0HUU612UuXI"),
   ("The reuse landscape (*)", "https://www.youtube.com/watch?v=feAZV7Ofov4"),
   ("Software Product Line Engineering", "https://www.youtube.com/watch?v=R1gybFwAy10"),
   ("What is ERP?", "https://www.youtube.com/watch?v=E0tgKVOxihI"),
   ("Component-based Software Engineering – Module 1", "https://www.youtube.com/watch?v=mxq9M4m-wkA"),
  ],
  qs=["What is software maintenance? Explain its types.",
      "What is reverse engineering?",
      "Explain software re-engineering."],
 ),
 "10": dict(
  topic="Software Certification",
  slides="chapter_10_software_certification.pdf",
  videos=[
   ("System security (*)", "https://www.youtube.com/watch?v=GTxPzKfriOU"),
   ("Security is a sociotechnical issue (*)", "https://www.youtube.com/watch?v=8bLwJy2BwKs"),
   ("An introduction to cybersecurity (*)", "https://www.youtube.com/watch?v=YPxlwsxEW48"),
   ("Stuxnet worm case study (*)", "https://www.youtube.com/watch?v=RilxHjt5yRE"),
   ("Systems of systems (*)", "https://www.youtube.com/watch?v=ryLeFaHarPQ"),
   ("An introduction to real-time systems (*)", "https://www.youtube.com/watch?v=_U6Le3_eL2I"),
  ],
  qs=["What is software certification? Explain its levels.",
      "What are the standards used in safety-critical systems?",
      "Explain ISO/IEC 9126 quality model."],
 ),
}

HEADER = """# الفصل {n} — {topic}

> **المادة:** Advanced Software Engineering · **الكتاب:** Aggarwal & Singh, *Software Engineering* 3rd ed.
> **ملاحظة:** الفيديوهات من موقع Sommerville (المؤلف) — مُعلَّمة بـ(*) من إعداده. المطابقة تقريبية (الفصول تختلف بين الكتابين).

## 📕 المصدر
- **الشرائح الرسمية:** `../Aggarwal_Singh_SE_PPT_Chapters/{slides}`
- **الكتاب الكامل:** `../_community_resources/Aggarwal_Singh_SE_3rd_ed_Book.pdf`
- **بنك أسئلة (بالوحدات):** `../_community_resources/SE_QuestionBank_UnitWise_NRCMEC.pdf`

## 🎥 فيديوهات
{videos}

## 🎯 أسئلة ذات صلة (نماذج)
{qs}

## 📝 ملاحظات
- راجع **التمارين بنهاية الفصل** بالكتاب (62 تمريناً بالكتاب كله).
- بنك NRCMEC يعطيك مستوى بلوم (BT) ومخرجات المقرر (CO) لكل سؤال.
"""

def main():
    for n, d in CH.items():
        vids = "\n".join(f"- {t} — {u}" for t, u in d["videos"])
        qs = "\n".join(f"- {q}" for q in d["qs"])
        txt = HEADER.format(n=n, topic=d["topic"], slides=d["slides"], videos=vids, qs=qs)
        (OUT / f"Ch{n}.md").write_text(txt, encoding="utf-8")
        print("wrote", f"Ch{n}.md", len(d["videos"]), "videos")

    # master index
    idx = ["# ASE — الروابط حسب الفصول", "",
           "> مجلد مفهرس: ملف لكل فصل من فصول الكتاب (Aggarwal & Singh, 3rd ed.).", "",
           "| الفصل | الموضوع | فيديوهات | الملف |",
           "|:---:|:---|:---:|:---|"]
    for n, d in CH.items():
        idx.append(f"| {n} | {d['topic']} | {len(d['videos'])} | [`Ch{n}.md`](Ch{n}.md) |")
    idx += ["", "## موارد عامة (خارج الفصول)",
            "- كل الروابط: `../ASE_ALL_LINKS.md`",
            "- بنوك أسئلة: `../_community_resources/`",
            "- الكتاب الكامل: `../_community_resources/Aggarwal_Singh_SE_3rd_ed_Book.pdf`"]
    (OUT / "README.md").write_text("\n".join(idx), encoding="utf-8")
    print("wrote README.md")


if __name__ == "__main__":
    main()
