#!/usr/bin/env python3
"""
Sandbox trial -- clean academic English Word document (Chapter 5: Software Design).
Simple standard format: Times New Roman, numbered headings, cover, TOC, list of figures,
embedded code-authored figures. No Arabic. Discussion-only artifact.
"""
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Pt, RGBColor

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
OUT = HERE / "Ch5_Software_Design_Study_Notes.docx"

BODY_FONT = "Times New Roman"
NAVY = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x44, 0x44, 0x44)

FIGURES = [
    ("fig02_conceptual_technical.png", 5.6,
     "The two-part design process. Conceptual design answers \u201cwhat\u201d for the "
     "customer; technical design answers \u201chow\u201d for the system builders."),
    ("fig01_modularity_cost.png", 4.9,
     "Modularity and software cost. Total cost is the sum of a falling development "
     "cost and a rising integration cost, so an optimum number of modules exists."),
    ("fig03_coupling_spectrum.png", 5.2,
     "The coupling spectrum, from worst (content) to best (data). Low coupling is a "
     "primary design objective."),
    ("fig06_common_coupling.png", 5.4,
     "Common coupling: independent modules read and write a shared global data area, so "
     "any change to the variables affects every module."),
    ("fig05_high_low_coupling.png", 5.4,
     "High versus low coupling visualised as inter-module dependency lines. Fewer, "
     "simpler links mean a cheaper system to maintain."),
    ("fig04_cohesion_ladder.png", 5.4,
     "The cohesion ladder, from weakest (coincidental) to strongest (functional). High "
     "cohesion is the counterpart objective to low coupling."),
    ("fig07_structure_chart.png", 6.2,
     "A function-oriented structure chart for \u201cUpdate File\u201d, showing module "
     "hierarchy and labelled data couples on the invocation arrows."),
    ("fig09_class_inheritance.png", 5.2,
     "Inheritance in object-oriented design: an abstract Shape base class with Square and "
     "Triangle subclasses that override Draw()."),
    ("fig10_oo_pipeline.png", 5.0,
     "The object-oriented analysis and design pipeline, from the problem statement through "
     "use cases, activity, interaction and class models to design documents."),
    ("fig08_sequence.png", 5.6,
     "A UML sequence diagram for the library \u201cIssue Book\u201d scenario, showing the "
     "ordered interaction between actor, controllers and databases."),
]


def set_base_style(doc):
    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(11)
    normal.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15
    rpr = normal.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(a), BODY_FONT)


def add_field(paragraph, instr):
    r = paragraph.add_run()
    fld_begin = OxmlElement("w:fldChar"); fld_begin.set(qn("w:fldCharType"), "begin")
    instr_el = OxmlElement("w:instrText"); instr_el.set(qn("xml:space"), "preserve")
    instr_el.text = instr
    fld_sep = OxmlElement("w:fldChar"); fld_sep.set(qn("w:fldCharType"), "separate")
    fld_text = OxmlElement("w:t"); fld_text.text = "Update field (right-click > Update Field)"
    fld_end = OxmlElement("w:fldChar"); fld_end.set(qn("w:fldCharType"), "end")
    for el in (fld_begin, instr_el, fld_sep, fld_text, fld_end):
        r._r.append(el)


def heading(doc, text, level=1, page_break=False):
    if page_break:
        doc.add_page_break()
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.name = BODY_FONT
        run.font.color.rgb = NAVY
        run.font.size = Pt(16 if level == 1 else 13 if level == 2 else 11.5)
        run.font.bold = True
    h.paragraph_format.space_before = Pt(14 if level == 1 else 10)
    h.paragraph_format.space_after = Pt(6)
    return h


def body(doc, text, italic=False, space_after=8):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    run.italic = italic
    run.font.name = BODY_FONT
    return p


def bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run(text)
    run.font.name = BODY_FONT
    return p


def add_figure(doc, filename, width_in, caption, number):
    path = FIG / filename
    if not path.exists():
        body(doc, f"[missing figure: {filename}]")
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(str(path), width=Inches(width_in))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_after = Pt(12)
    run = cap.add_run(f"Figure {number}. {caption}")
    run.italic = True
    run.font.size = Pt(9.5)
    run.font.color.rgb = GREY
    run.font.name = BODY_FONT


def add_table(doc, headers, rows):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = t.rows[0].cells[i]
        cell.text = ""
        run = cell.paragraphs[0].add_run(h)
        run.bold = True
        run.font.size = Pt(10)
        run.font.name = BODY_FONT
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shade = OxmlElement("w:shd"); shade.set(qn("w:fill"), "1F3A5F")
        cell._element.get_or_add_tcPr().append(shade)
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            run = cells[i].paragraphs[0].add_run(val)
            run.font.size = Pt(10)
            run.font.name = BODY_FONT
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    return t


def cover(doc):
    for _ in range(3):
        doc.add_paragraph()
    title = doc.add_paragraph(); title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = title.add_run("Software Design")
    r.font.name = BODY_FONT; r.font.size = Pt(30); r.bold = True; r.font.color.rgb = NAVY
    sub = doc.add_paragraph(); sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = sub.add_run("Chapter 5 Study Notes \u2014 Advanced Software Engineering (CS603)")
    r.font.name = BODY_FONT; r.font.size = Pt(14); r.font.color.rgb = GREY
    doc.add_paragraph()
    meta = [
        ("Student", "[Your Name]  \u2014  MCS Candidate"),
        ("Course", "Advanced Software Engineering (CS603), 3 Credit Hours"),
        ("Instructor", "Asst. Prof. Dr. Ali Fahim Ni'ma"),
        ("Institution", "College of Computer Science & Information Technology, University of Wasit"),
        ("Document type", "Seminar / Study notes \u2014 English, trial build"),
    ]
    for label, value in meta:
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(f"{label}:  "); r1.bold = True; r1.font.name = BODY_FONT; r1.font.size = Pt(11)
        r2 = p.add_run(value); r2.font.name = BODY_FONT; r2.font.size = Pt(11)


def front_matter(doc):
    doc.add_page_break()
    heading(doc, "Table of Contents", 1)
    p = doc.add_paragraph()
    add_field(p, r'TOC \o "1-2" \h \z \u')
    note = doc.add_paragraph()
    rn = note.add_run("(In Word, select all and press F9 \u2014 or right-click \u2014 to build the table.)")
    rn.italic = True; rn.font.size = Pt(9); rn.font.color.rgb = GREY

    doc.add_page_break()
    heading(doc, "List of Figures", 1)
    for i, (_, _, cap) in enumerate(FIGURES, 1):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(f"Figure {i}.  {cap}")
        r.font.size = Pt(10); r.font.name = BODY_FONT


def build():
    doc = Document()
    set_base_style(doc)
    for s in doc.sections:
        s.top_margin = Inches(1.0); s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0); s.right_margin = Inches(1.0)

    cover(doc)
    front_matter(doc)

    # 1
    heading(doc, "1. Introduction: What Is Design?", 1, page_break=True)
    body(doc, "Analysis is concerned with establishing what a system must do; design is "
              "concerned with how it will do it. Software design is the creative problem-solving "
              "activity that transforms a validated set of requirements into a description of the "
              "internal structure of the system, sufficiently detailed to guide implementation. "
              "Where the requirements specification is a statement of the problem, the design is "
              "the first statement of the solution.")
    body(doc, "The output of design is the Software Design Document (SDD). A design must satisfy "
              "two different audiences at once. It must be understandable to the customer, because "
              "the customer validates that the intended behaviour has been captured, and it must be "
              "precise enough for the implementers, because they build directly from it. A design "
              "that pleases one audience and not the other is incomplete.")
    body(doc, "A well-formed design is expected to be correct with respect to the requirements, "
              "complete, understandable at the level of abstraction appropriate to its reader, and "
              "maintainable. These four qualities, rather than the mere presence of diagrams, "
              "distinguish design work from coding.")

    # 2
    heading(doc, "2. The Design Framework", 1)
    body(doc, "Design proceeds as an iterative refinement loop rather than a single step. The "
              "designer starts from the initial requirements, gathers and answers the open "
              "questions they raise, analyses the information, conceives a high-level solution, "
              "refines and documents it, and then validates the result against the original "
              "requirements. Validation may feed new questions back into the loop, so the process "
              "repeats until the design is stable.")
    body(doc, "Design also passes through levels of formality. It begins as an informal outline, "
              "becomes an informal design, is refined into a more formal design, and finally "
              "becomes the finished, documented design from which code is written. Each transition "
              "adds precision without changing the underlying decisions.")

    # 3
    heading(doc, "3. Conceptual and Technical Design", 1)
    body(doc, "Design is commonly separated into two complementary parts. Conceptual design "
              "addresses the customer's view: where data comes from, what happens to it, what the "
              "user sees, what choices are offered, and the timing and form of screens and reports. "
              "Technical design addresses the builder's view: the hardware configuration, the "
              "software needed, communication interfaces, input and output devices, and the overall "
              "software and network architecture.")
    body(doc, "The two are produced for different stakeholders but must remain consistent. "
              "A change in the conceptual view (for example, adding a new report) normally forces a "
              "corresponding change in the technical view. Figure 1 shows the relationship.")
    add_figure(doc, *FIGURES[0], number=1)

    # 4
    heading(doc, "4. Modularity", 1)
    body(doc, "Modularity is the decomposition of a system into a set of discrete, well-defined "
              "units called modules. The term has been interpreted at different granularities over "
              "time \u2014 from a Fortran subroutine, through an Ada package, a C or Pascal function, "
              "a C++ or Java class, up to a Java package \u2014 but the underlying idea is constant: "
              "a module is a unit that can be understood, implemented, tested, and replaced largely "
              "in isolation.")
    body(doc, "A well-formed modular system has modules with a well-defined and single purpose, "
              "which can be compiled and stored separately, may use other modules, are easier to "
              "use than to rebuild, and are simpler on the outside than on the inside. Modularity "
              "pays off because it makes the design intellectually manageable and eases "
              "implementation, debugging, testing, documentation, and maintenance.")
    body(doc, "Modularity is not free, however. Splitting a system into too few modules produces "
              "large, unmanageable units; splitting it into too many produces a proliferation of "
              "interfaces whose integration cost dominates. The total cost of effort is therefore a "
              "U-shaped curve with a minimum at some intermediate granularity, as Figure 2 shows.")
    add_figure(doc, *FIGURES[1], number=2)

    # 5
    heading(doc, "5. Coupling", 1)
    body(doc, "Coupling is the degree of interdependence between modules. It measures the strength "
              "of the connections that cross module boundaries. Low coupling is desirable because "
              "the less one module depends on the internals of another, the more freely either can "
              "be changed, tested, or reused without disturbing the rest of the system.")
    body(doc, "Coupling is not a single condition but a spectrum. From worst to best, the "
              "recognised forms are content, common, external, control, stamp, and data coupling. "
              "Figure 3 places them on that spectrum.")
    add_figure(doc, *FIGURES[2], number=3)
    body(doc, "Content coupling is the worst case: one module reaches into, branches into, or "
              "directly modifies the internal data of another. Common coupling arises when "
              "independent modules share a global data area, as shown in Figure 4. External "
              "coupling ties a module to an externally imposed format or protocol. Control coupling "
              "passes a flag whose only purpose is to steer the other module's logic. Stamp coupling "
              "passes a whole data structure when only part of it is needed. Data coupling, the best "
              "form, passes only the minimal data required, and nothing else.")
    body(doc, "The practical techniques that reduce coupling are therefore straightforward: pass "
              "few parameters, pass data rather than control flags, allow only parent-to-child "
              "invocation, and never share global state between peers. Figure 5 contrasts the "
              "resulting dependency structure.")
    add_figure(doc, *FIGURES[3], number=4)
    add_figure(doc, *FIGURES[4], number=5)

    add_table(doc,
              ["Coupling type", "What crosses the boundary", "Verdict"],
              [["Content", "Access to another module's internals", "Worst \u2014 avoid"],
               ["Common", "Shared global data area", "Poor"],
               ["External", "Externally imposed format/protocol", "Poor"],
               ["Control", "A flag that steers logic", "Moderate"],
               ["Stamp", "A whole structure, partly unused", "Fair"],
               ["Data", "Only the needed data", "Best \u2014 target"]])

    # 6
    heading(doc, "6. Cohesion", 1)
    body(doc, "Cohesion is the strength of the relationships among the elements within a single "
              "module. Where coupling looks outward across boundaries, cohesion looks inward. High "
              "cohesion is desirable: a module whose parts all serve one purpose is easier to "
              "understand, test, and reuse.")
    body(doc, "Like coupling, cohesion forms a ladder. From weakest to strongest the recognised "
              "types are coincidental, logical, temporal, procedural, communicational, sequential, "
              "and functional. Figure 6 shows the ladder.")
    add_figure(doc, *FIGURES[5], number=6)
    body(doc, "Coincidental cohesion packs unrelated statements together with no discernible "
              "relationship. Logical cohesion groups elements that are similar in category but "
              "controlled by a flag. Temporal cohesion groups activities that happen at the same "
              "time, such as initialisation. Procedural cohesion groups steps that must run in a "
              "fixed order. Communicational cohesion groups steps that operate on the same data. "
              "Sequential cohesion groups steps where the output of one is the input of the next. "
              "Functional cohesion, the strongest, groups every element around a single, "
              "well-defined task.")
    body(doc, "The two objectives are complementary and jointly define good modular design: aim "
              "for high cohesion within modules and low coupling between them. A design that "
              "maximises one without regard to the other is not balanced.")

    # 7
    heading(doc, "7. Strategies of Design", 1)
    body(doc, "Once the decision to decompose is made, the designer chooses a direction of "
              "refinement. In top-down design, also called stepwise refinement, the designer starts "
              "with the most abstract statement of the problem and decomposes it repeatedly until "
              "each part is small enough to implement. In bottom-up design, the designer starts "
              "from existing low-level modules and composes them upward, which suits situations "
              "where a library of reusable parts already exists. In hybrid design, the two are "
              "combined.")
    body(doc, "Top-down lets each module be specialised to exactly one parent and therefore tends "
              "to produce very cohesive modules, but it can duplicate logic. Bottom-up favours "
              "reuse and generalisation, but modules become shared by several parents and are "
              "harder to trace back to a single requirement. The hybrid strategy is the common "
              "practical choice: it takes top-down structure from the requirements and bottom-up "
              "reuse where components are already available.")

    # 8
    heading(doc, "8. Function-Oriented Design", 1)
    body(doc, "In function-oriented design the system is designed from a functional viewpoint: it "
              "is seen as a collection of interacting units, each with a clearly defined function. "
              "The dominant tool is the structure chart, which partitions the system into black "
              "boxes \u2014 modules whose functionality is known while their internals are hidden "
              "\u2014 arranged in a hierarchy with a single root.")
    body(doc, "A structure chart must not be confused with a flowchart. A flowchart shows the "
              "sequence of steps inside an algorithm; a structure chart shows the decomposition of "
              "the system into modules and the data and control couples exchanged between them. "
              "Alongside the structure chart, function-oriented design uses the data-flow diagram, "
              "the data dictionary, and pseudocode. Figure 7 shows a structure chart for a typical "
              "\u201cUpdate File\u201d task; the double-framed box denotes a library (predefined) "
              "module, and the labelled arrows denote data couples.")
    add_figure(doc, *FIGURES[6], number=7)
    body(doc, "Functional structure may be organised in layers. The top layer coordinates the "
              "task, the middle layers perform the main transformations, and the bottom layers "
              "provide primitive file and device operations. This layering is what allows the "
              "bottom layers to be written once and reused by many tasks.")

    # 9
    heading(doc, "9. Object-Oriented Design", 1)
    body(doc, "Object-oriented design is orthogonal to function-oriented design. Instead of "
              "organising the system around functions, it organises it around the things in the "
              "problem domain \u2014 their data (attributes) and their behaviour (operations). The "
              "core vocabulary is concise: an object is a run-time instance that holds state and "
              "offers operations; a class is the template from which objects are created; a message "
              "is a request sent to an object; abstraction suppresses detail; encapsulation hides "
              "state behind an interface; inheritance lets a class acquire the attributes and "
              "operations of another; polymorphism lets different classes respond to the same "
              "request in their own way; and hierarchy organises classes into ranked relationships.")
    body(doc, "Inheritance and polymorphism are usually discussed together because inheritance "
              "without overriding is little more than code sharing. Figure 8 shows a base class "
              "Shape with two subclasses, Square and Triangle, each of which supplies its own "
              "Draw() operation.")
    add_figure(doc, *FIGURES[7], number=8)
    body(doc, "The move from requirements to an object-oriented design follows a recognisable "
              "pipeline: build a use-case model, draw activity diagrams where control flow matters, "
              "draw interaction diagrams (sequence and collaboration), draw the class diagram, add "
              "state or object diagrams where an object has significant state, and finally draw "
              "component and deployment diagrams as the design approaches implementation. "
              "Figure 9 shows this pipeline.")
    add_figure(doc, *FIGURES[8], number=9)
    add_table(doc,
              ["Aspect", "Function-oriented", "Object-oriented"],
              [["Unit of decomposition", "Function", "Object / class"],
               ["Basic building block", "Module", "Class"],
               ["State", "Shared, often global", "Encapsulated in objects"],
               ["Extension mechanism", "Add a function", "Add / override a class"],
               ["Typical diagram", "Structure chart, DFD", "Class, sequence, state"],
               ["Best at", "Algorithmic, process-driven systems", "State-rich, evolving systems"]])

    # 10
    heading(doc, "10. Documenting the Design: The SDD", 1)
    body(doc, "The design phase concludes with the Software Design Document (SDD), defined by "
              "IEEE 1016. The SDD is the medium for communicating the design, the blueprint from "
              "which implementation proceeds, and the artefact against which the design is "
              "reviewed. It documents design entities, design views, and the attributes of each "
              "entity.")
    body(doc, "Each design entity is described through a consistent set of attributes: "
              "identification, type, purpose, function, subordinates, dependencies, interface, "
              "resources, processing detail, and data. The document is organised into four "
              "standard views: the decomposition view (how the system is partitioned into "
              "entities), the dependency view (how entities relate and use resources), the "
              "interface view (everything needed to use each entity), and the detail view (the "
              "internal detail of each entity).")

    # 11
    heading(doc, "11. Worked Example: The Library System", 1)
    body(doc, "The chapter illustrates the design techniques on a university library system. Its "
              "three functions are to issue a book, return a book, and answer queries and produce "
              "reports such as availability by title or author, printouts, and a logged, "
              "password-protected, fully backed-up data store.")
    body(doc, "Figure 10 traces the \u201cissue book\u201d scenario as a sequence diagram. The "
              "operator reads the student's barcode, a reader submits it to a controller, the "
              "controller retrieves and validates the student's details against the student "
              "database, the operator then reads the book's barcode, and a second controller "
              "checks, updates and records the issue. The numbering shows the strict ordering that "
              "design must preserve.")
    add_figure(doc, *FIGURES[9], number=10)
    body(doc, "The same scenario can be expressed as a set of collaborating objects (controllers "
              "for student and book information, entity objects for students and books, and "
              "interface objects for the forms), as a class diagram of those objects, and as a "
              "state chart for the Book class as it moves between available, issued, and returned "
              "states. The choice of view depends on which aspect of the design is being "
              "communicated, not on the size of the system.")

    # 12
    heading(doc, "12. Summary", 1)
    for b in [
        "Design answers how, where analysis answers what; its output is the SDD.",
        "Modularity decomposes the system and trades development cost against integration cost.",
        "Coupling is inter-module interdependence; keep it low (data coupling is best).",
        "Cohesion is intra-module relatedness; keep it high (functional cohesion is best).",
        "Design may proceed top-down, bottom-up, or hybrid; hybrid is the practical default.",
        "Function-oriented design uses structure charts; object-oriented design uses classes and "
        "the use-case to deployment pipeline.",
        "IEEE 1016 governs the SDD, organised into decomposition, dependency, interface, and "
        "detail views.",
    ]:
        bullet(doc, b)

    # References
    heading(doc, "References", 1, page_break=True)
    refs = [
        "K. K. Aggarwal and Y. Singh, Software Engineering, 3rd ed. New Delhi, India: New Age "
        "International Publishers, 2007, ch. 5 (Software Design).",
        "R. Mall, Fundamentals of Software Engineering, 4th ed. New Delhi, India: PHI Learning, "
        "2018, ch. 5.",
        "R. S. Pressman, Software Engineering: A Practitioner's Approach. New York, NY, USA: "
        "McGraw-Hill Education.",
        "I. Sommerville, Software Engineering, 9th ed. Boston, MA, USA: Addison-Wesley, 2011.",
        "IEEE, IEEE Standard for Information Technology \u2014 Systems Design \u2014 Software "
        "Design Descriptions, IEEE Std 1016-2009.",
    ]
    for i, r in enumerate(refs, 1):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.35)
        p.paragraph_format.first_line_indent = Inches(-0.35)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(f"[{i}]  {r}")
        run.font.size = Pt(10); run.font.name = BODY_FONT

    doc.save(OUT)
    print(f"Saved: {OUT}")
    print(f"Paragraphs: {len(doc.paragraphs)}  Tables: {len(doc.tables)}  "
          f"Figures: {len(FIGURES)}")
    return OUT


if __name__ == "__main__":
    build()
