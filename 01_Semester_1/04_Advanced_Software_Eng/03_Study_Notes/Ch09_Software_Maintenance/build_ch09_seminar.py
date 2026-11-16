from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.section import WD_SECTION
from pathlib import Path
import re

OUT=Path(r'C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\05_Seminars_&_Slides\Ch09_Software_Maintenance_Seminar.docx')
FIG=Path(r'C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\05_Seminars_&_Slides\Ch09_Assets\Ch09_Fig01_Maintenance_Effort.png')

doc=Document()
sec=doc.sections[0]
sec.top_margin=Inches(.88); sec.bottom_margin=Inches(.88); sec.left_margin=Inches(1.0); sec.right_margin=Inches(1.0)
sec.header_distance=Inches(.32); sec.footer_distance=Inches(.34)

# Typography and paragraph rhythm
styles=doc.styles
normal=styles['Normal']; normal.font.name='Times New Roman'; normal.font.size=Pt(11.5); normal.font.color.rgb=RGBColor(35,43,52)
normal._element.rPr.rFonts.set(qn('w:eastAsia'),'Times New Roman')
normal.paragraph_format.space_after=Pt(8.5); normal.paragraph_format.line_spacing=1.35
for name,size in [('Title',30),('Subtitle',15),('Heading 1',16),('Heading 2',13),('Heading 3',11.5)]:
    st=styles[name]; st.font.name='Aptos Display' if name in ('Title','Heading 1','Heading 2','Heading 3') else 'Times New Roman'; st.font.size=Pt(size); st.font.color.rgb=RGBColor(0,0,0); st.font.bold=name!='Subtitle'
    st._element.rPr.rFonts.set(qn('w:eastAsia'),st.font.name)
    st.paragraph_format.keep_with_next=True
styles['Heading 1'].paragraph_format.space_before=Pt(14); styles['Heading 1'].paragraph_format.space_after=Pt(7)
styles['Heading 2'].paragraph_format.space_before=Pt(10); styles['Heading 2'].paragraph_format.space_after=Pt(4)
# Remove the built-in Title style's decorative border for a clean academic title.
for stname in ('Title','Subtitle'):
    ppr=styles[stname]._element.get_or_add_pPr()
    bdr=ppr.find(qn('w:pBdr'))
    if bdr is not None: ppr.remove(bdr)

# Header
h=sec.header.paragraphs[0]; h.alignment=WD_ALIGN_PARAGRAPH.RIGHT
r=h.add_run('ADVANCED SOFTWARE ENGINEERING  |  CHAPTER 9'); r.font.name='Aptos'; r.font.size=Pt(8); r.font.color.rgb=RGBColor(85,99,113)
# Footer page field
f=sec.footer.paragraphs[0]; f.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=f.add_run('Predictive vocabulary draft  •  '); r.font.name='Aptos'; r.font.size=Pt(8); r.font.color.rgb=RGBColor(90,100,110)
fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE'); f._p.append(fld)

def shade(cell,fill):
    tcPr=cell._tc.get_or_add_tcPr(); shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),fill); tcPr.append(shd)
def set_cell_text(cell,text,bold=False,color=None,size=9):
    cell.text=''; p=cell.paragraphs[0]; p.paragraph_format.space_after=Pt(1); p.paragraph_format.line_spacing=1.0
    run=p.add_run(text); run.font.name='Cambria'; run.font.size=Pt(size); run.bold=bold
    if color: run.font.color.rgb=RGBColor(*color)
    cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER

def para(text,style=None,italic=False,bold_lead=None):
    p=doc.add_paragraph(style=style)
    if bold_lead and text.startswith(bold_lead):
        rr=p.add_run(bold_lead); rr.bold=True; p.add_run(text[len(bold_lead):])
    else:
        rr=p.add_run(text); rr.italic=italic
    return p

def bullet(text):
    p=doc.add_paragraph(style='List Bullet'); p.paragraph_format.space_after=Pt(3); p.paragraph_format.left_indent=Inches(.28); p.add_run(text); return p

def numbered(text):
    p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(3); p.paragraph_format.left_indent=Inches(.28); p.paragraph_format.first_line_indent=Inches(-.22)
    previous=doc.paragraphs[-2] if len(doc.paragraphs)>1 else None
    match=re.match(r'^(\d+)\. ',previous.text) if previous is not None else None
    n=int(match.group(1))+1 if match else 1
    run=p.add_run(f'{n}. {text}'); run.font.name='Times New Roman'; return p

# The first content cluster uses a comparison table before the asset paths and
# later figure helpers are initialized; define the table helper at that point.
def grid(headers,rows,widths=None,size=8.5):
    table=doc.add_table(rows=1,cols=len(headers)); table.alignment=WD_TABLE_ALIGNMENT.CENTER; table.style='Table Grid'; table.autofit=False
    if widths:
        for i,w in enumerate(widths): table.columns[i].width=Inches(w)
    for i,htext in enumerate(headers): set_cell_text(table.rows[0].cells[i],htext,True,(255,255,255),size); shade(table.rows[0].cells[i],'315B7E')
    for idx,row in enumerate(rows):
        cells=table.add_row().cells
        for i,text in enumerate(row): set_cell_text(cells[i],text,bold=(i==0),size=size)
        if idx%2==1:
            for cell in cells: shade(cell,'EEF3F7')
    return table

# Cover
p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(76); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=p.add_run('ADVANCED SOFTWARE ENGINEERING'); r.bold=True; r.font.name='Aptos'; r.font.size=Pt(12); r.font.color.rgb=RGBColor(49,91,126)
p=doc.add_paragraph(style='Title'); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before=Pt(20); p.add_run('Software Maintenance')
p=doc.add_paragraph(style='Subtitle'); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.add_run('A source-grounded seminar across the predictive Chapter 9 vocabulary')
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before=Pt(22)
r=p.add_run('CHAPTER 9  |  PREDICTIVE WORKING DRAFT'); r.bold=True; r.font.name='Aptos'; r.font.size=Pt(10); r.font.color.rgb=RGBColor(49,91,126)
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before=Pt(10)
r=p.add_run('Working draft based on predictive vocabulary'); r.italic=True; r.font.size=Pt(11)
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=p.add_run('The official instructor vocabulary and lecture notes are still pending.'); r.font.size=Pt(9); r.font.color.rgb=RGBColor(90,100,110)
# Front matter panel
p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(50); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=p.add_run('SCOPE OF THIS ITEM'); r.bold=True; r.font.name='Aptos'; r.font.size=Pt(9); r.font.color.rgb=RGBColor(49,91,126)
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.left_indent=Inches(.7); p.paragraph_format.right_indent=Inches(.7)
p.add_run('Nine connected topic areas: maintenance fundamentals; maintenance problems and management; the maintenance process; process models; cost estimation; regression testing; reverse engineering and reengineering; software configuration management; and documentation and maintenance tools.')
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before=Pt(18)
r=p.add_run('SOURCE BASE'); r.bold=True; r.font.name='Aptos'; r.font.size=Pt(9); r.font.color.rgb=RGBColor(49,91,126)
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.left_indent=Inches(.75); p.paragraph_format.right_indent=Inches(.75)
p.add_run('Chapter 9 course text and companion lecture slides; the Chapter 9 treatment in B. B. Agarwal, S. P. Tayal, and M. Gupta, Software Engineering and Testing; and selective comparison with Sommerville, Pressman, Mall, and Leach. Source-specific terms and figures remain distinct.')
doc.add_page_break()
p=doc.add_paragraph('Contents',style='Heading 1')
fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'TOC \\o "1-2" \\h \\z \\u'); doc.add_paragraph()._p.append(fld)
doc.add_page_break()

# Content
p=doc.add_paragraph('1. Software Maintenance',style='Heading 1')
para('Software maintenance is the controlled modification of software that is already in operation. It keeps a delivered system useful as faults are discovered, operating conditions change, users request capabilities, and the system itself becomes harder to change. Maintenance therefore includes more than repairing defects: it can adapt a system, extend it, improve its internal condition, and reduce the risk of future change.')
para('This first item establishes the vocabulary used throughout the seminar. It distinguishes four maintenance purposes, interprets the course text’s effort figures, and explains what “manageable” means in practice. These distinctions matter because a change request should be classified by the reason for the change, not simply by the code that happens to be edited.')

p=doc.add_paragraph('1.1 Meaning and scope',style='Heading 2')
para('Delivery is a transition in the system’s use, not the end of its life cycle. Once software is deployed, its surrounding conditions continue to move: business rules evolve, hardware and operating systems are replaced, interfaces change, defects appear in actual use, and stakeholders learn what additional functions would help them. If the system is to remain useful, some of these changes must be reflected in the software.')
para('The course material frames maintenance around changes to an existing product after delivery. Its examples include correcting errors, accommodating changes in the external environment, extending functions beyond the original requirements, and improving performance or structure. The exact boundary can vary across software-engineering texts: some use “software evolution” as the broad life-cycle process and reserve “maintenance” for post-delivery change, especially where responsibility or documentation passes from the original development team. For this seminar, the course chapter’s post-delivery maintenance framing is retained.')
para('Software does not wear out like a mechanical component. Its maintenance demand comes from changed requirements and context, faults in operation, and the consequences of repeated modifications. A useful distinction is therefore between physical deterioration and socio-technical change: the software may remain bit-for-bit intact while becoming unsuitable for its users, platform, interfaces, or operating environment.')

p=doc.add_paragraph('1.2 Why maintenance matters',style='Heading 2')
para('Organizations maintain software because deployed systems embody prior investment and often support important operations. Replacing a useful system can require migration, retraining, data conversion, new integration work, and acceptance of transition risk. Maintenance preserves value when a bounded change can keep the system aligned with current needs at an acceptable cost and risk.')
para('Several recurring triggers explain the work:')
bullet('A fault is observed during operation and must be corrected to restore intended behavior.')
bullet('A platform, operating system, device, interface, policy, or external service changes, requiring adaptation.')
bullet('Users identify useful capabilities that were outside the original functional scope, or request improvements to existing behavior.')
bullet('Accumulated changes make the structure harder to understand or modify, creating a reason to improve the software before future changes become excessively risky.')
para('The supporting texts reinforce the continuing-change view while using different emphases. Sommerville connects software evolution to continuing business and environmental change. Leach frames maintenance as systematic change to software in operation and highlights the remaining useful life in deciding whether work is worthwhile. Pressman’s treatment makes preventive change concrete through reengineering: restructuring a program so later correction, adaptation, or enhancement is easier. These are complementary explanations, not a replacement taxonomy for the course material.')
para('The scanned chapter contrasts a maintenance period that may extend for about two decades with a development period of roughly one to two years. These durations illustrate why post-delivery work occupies a long part of a product’s life; they are the chapter’s contextual comparison, not a schedule that applies to every software system.')

p=doc.add_paragraph('1.3 Four maintenance purposes',style='Heading 2')
para('The course companion slides organize maintenance into four familiar purposes. The scanned course text gives full treatment to corrective, adaptive, and perfective maintenance, then discusses preventive maintenance in its “other types” discussion and notes that authors do not use the term uniformly. The slide set and its effort figure present preventive maintenance as a fourth category. The table below uses the four-part course-aligned view while preserving that source distinction.')
t=doc.add_table(rows=1,cols=3); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.style='Table Grid'; t.autofit=False
widths=[1.05,1.9,3.75]
for i,w in enumerate(widths): t.columns[i].width=Inches(w)
for i,text in enumerate(['Purpose','Question answered','Typical change']): set_cell_text(t.rows[0].cells[i],text,True,(255,255,255),9); shade(t.rows[0].cells[i],'315B7E')
rows=[
('Corrective','What is failing against intended behavior?','Repair a defect revealed in use; preserve the intended requirement or behavior.'),
('Adaptive','What surrounding condition has changed?','Modify the system for a new operating system, hardware platform, external interface, or governing environment.'),
('Perfective','What useful capability or quality should improve?','Add or improve user-facing functions, efficiency, performance, or other desired characteristics.'),
('Preventive','What change now would make later change safer or easier?','Restructure or reengineer code and related artifacts to reduce avoidable complexity and improve future correctability, adaptability, or enhancement.')]
for idx,row in enumerate(rows):
    cells=t.add_row().cells
    for i,text in enumerate(row): set_cell_text(cells[i],text,bold=(i==0),size=8.7)
    if idx%2==1:
        for c in cells: shade(c,'EEF3F7')

p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(4); p.paragraph_format.space_after=Pt(6)
r=p.add_run('Classification rule. '); r.bold=True
p.add_run('Classify a request by its primary purpose. A change can touch the same code for different reasons: a parser change may fix a defect, accommodate a new data format, add a new feature, or simplify the parser before further change. The code location alone does not determine the category.')

p=doc.add_paragraph('1.4 Keeping taxonomies distinct',style='Heading 2')
para('The four-part scheme is useful for this course, but it is not the only taxonomy in the supporting literature. Mall presents three categories—corrective, adaptive, and perfective—in the relevant section. Sommerville uses a different three-way grouping: fault repairs, adaptation to a different operating environment, and functional extension or modification. Leach also describes three major types in his maintenance discussion. Pressman’s taxonomy includes correction, adaptation, enhancement, and prevention, describing prevention through software reengineering.')
para('These schemes overlap in purpose but do not align label-for-label. In particular, a source that presents three categories may omit preventive maintenance or treat structural improvement under another heading. The seminar therefore follows the course’s four-way teaching presentation where it is explicit, and uses the alternative texts to clarify purpose and decision context rather than silently merging their labels.')
para('Agarwal, Tayal, and Gupta frame software as an evolving entity and summarize three observed tendencies: software must continue changing to remain useful; repeated maintenance tends to degrade program structure; and the rate of development remains approximately constant over a product’s life. These observations add a life-cycle perspective to the maintenance categories. They are not four extra maintenance types, and they do not provide a project-specific forecast.')
para('The same book’s maintenance examples clarify the categories without replacing the course taxonomy. A change in tax rules illustrates adaptation to a changed external policy; moving store-to-head-office data transfer from physical media to network links illustrates a changed operating environment; and improving performance, maintainability, or requested functionality illustrates perfective work. Its preventive-maintenance discussion emphasizes avoiding obsolescence through reverse engineering and reengineering. The course text places preventive work under “other types” and describes its purpose differently, so these descriptions remain source-specific.')

p=doc.add_paragraph('1.5 Reading the effort distribution',style='Heading 2')
para('The course text reproduces an effort distribution in Figure 1.1. The figure reports perfective maintenance at 50%, adaptive at 25%, corrective at 21%, and preventive at 4%. It communicates the relative distribution in the cited source; it is not a universal forecast for every organization, software product, or period. The comparatively small preventive slice does not imply that preventive work lacks value: the chapter’s discussion connects preventive action with preserving structure and reducing future difficulty.')
p=doc.add_picture(str(FIG),width=Inches(4.35)); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after=Pt(2)
r=p.add_run('Figure 1.1. Distribution of maintenance effort reproduced from the course text, Figure 9.1, printed p. 461.'); r.italic=True; r.font.size=Pt(8.5)
p=para('The same chapter also gives a separate activity-based survey in Table 9.1 on printed p. 462. It distributes effort among eight kinds of work. These percentages should not be combined with Figure 1.1: the figure groups work by maintenance purpose, whereas the table lists operational activity types from a separate survey presentation.'); p.paragraph_format.keep_together=True
t2=doc.add_table(rows=1,cols=2); t2.alignment=WD_TABLE_ALIGNMENT.CENTER; t2.style='Table Grid'; t2.autofit=False
t2.columns[0].width=Inches(5.0); t2.columns[1].width=Inches(1.2)
for i,text in enumerate(['Activity reported in the course table','Share']): set_cell_text(t2.rows[0].cells[i],text,True,(255,255,255),8.7); shade(t2.rows[0].cells[i],'315B7E')
activities=[('User-requested enhancements','41.8%'),('Adaptation to the data environment','17.3%'),('Emergency debugging','12.4%'),('Routine debugging','9.3%'),('Adaptation to hardware or operating system','6.2%'),('Documentation improvement','5.5%'),('Code-efficiency improvement','4.0%'),('Other activities','3.5%')]
for i,(a,v) in enumerate(activities):
    c=t2.add_row().cells; set_cell_text(c[0],a,size=8.5); set_cell_text(c[1],v,size=8.5)
    if i%2==1:
        for cell in c: shade(cell,'EEF3F7')

p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(4)
r=p.add_run('Interpretation. '); r.bold=True
p.add_run('The table’s largest named activity is user enhancement; debugging is split between emergency and routine work; adaptation also appears in two separate rows. Because one table row is an activity and another is a request purpose, these data are best read as a description of the survey’s reported workload—not as a direct conversion to the four-category pie chart.')

p=doc.add_paragraph('1.6 What “manageable” means',style='Heading 2')
para('The course chapter argues that maintenance is manageable. This does not mean that every request is predictable, inexpensive, or technically simple. It means that organizations can reduce avoidable emergency work and handle a substantial portion of change through deliberate planning, prioritization, and preparation. In the chapter’s cited survey discussion, approximately 79% of maintenance activity is described as adaptive, perfective, or preventive work that can be anticipated and managed; the text contrasts this with a smaller share requiring special immediate attention. These are source-specific survey figures, not a guaranteed rate for a new project.')
para('Manageability follows from treating maintenance as continuing work rather than an afterthought:')
numbered('Record and classify requests. Capture the observed behavior, requested outcome, affected users, urgency, and evidence. Separate the symptom from the proposed solution.')
numbered('Assess impact and value. Identify affected components, interfaces, data, tests, and dependent systems. Estimate effort and risk, and compare the benefit with cost and remaining useful life.')
numbered('Prioritize and schedule. Distinguish emergencies from work that can enter a planned release. Coordinate related changes to limit avoidable rework and disruption.')
numbered('Implement with system understanding. Examine the existing design and behavior before changing it, especially when the original developers are no longer responsible for the system.')
numbered('Validate and preserve the system record. Test the change and plausible side effects, update relevant documentation, and retain the rationale and release information for future maintainers.')
para('This sequence is a practical synthesis of the chapter’s manageability discussion and the supporting texts’ treatment of systematic maintenance, change assessment, and reengineering. It is not presented as a verbatim named process from one source. Its purpose is to show how planned work can reduce the chance that every change becomes urgent and isolated.')

p=doc.add_paragraph('1.7 Worked classification example',style='Heading 2')
para('Consider a campus library system that has been in operation for several years. A change request arrives after users report a set of problems and new needs. The classification depends on the reason for each change:')
t3=doc.add_table(rows=1,cols=3); t3.alignment=WD_TABLE_ALIGNMENT.CENTER; t3.style='Table Grid'; t3.autofit=False
for i,w in enumerate([2.0,2.25,2.8]): t3.columns[i].width=Inches(w)
for i,text in enumerate(['Observed request','Primary purpose','Reason']): set_cell_text(t3.rows[0].cells[i],text,True,(255,255,255),8.5); shade(t3.rows[0].cells[i],'315B7E')
examples=[
('Search sometimes omits a valid record.','Corrective','The system fails to meet its existing intended behavior.'),
('The institution replaces its database interface.','Adaptive','The system must accommodate a changed external environment.'),
('Students request a saved-search feature.','Perfective','The change adds useful functionality beyond the previous scope.'),
('The search module is tightly coupled and costly to modify.','Preventive','Restructuring is undertaken to make future changes safer and more manageable.')]
for i,row in enumerate(examples):
    cells=t3.add_row().cells
    for j,text in enumerate(row): set_cell_text(cells[j],text,bold=(j==1),size=8.2)
    if i%2==1:
        for c in cells: shade(c,'EEF3F7')
para('A single release may contain several of these purposes. They remain analytically distinct even if they are implemented together. For example, adding saved search can be perfective work, while refactoring its module for future change can be preventive work. Keeping the rationale visible supports estimation, review, and later evaluation of whether the request delivered its intended benefit.')

p=doc.add_paragraph('1.8 Key distinctions and closing synthesis',style='Heading 2')
bullet('Maintenance begins after delivery in the course chapter’s framing and exists because faults, requirements, and operating environments change.')
bullet('Corrective, adaptive, perfective, and preventive identify different reasons for changing an existing system.')
bullet('The course text’s pie chart and activity table use different groupings; their percentages describe different views and must remain separate.')
bullet('Maintenance is manageable when requests are recorded, analyzed, prioritized, implemented with system understanding, tested, and documented. Manageable does not mean cheap, easy, or fully predictable.')
para('Software maintenance preserves the usefulness of a system through controlled change. Corrective work restores intended behavior; adaptive work responds to external change; perfective work adds or improves user value; preventive work improves the system’s capacity for future change. The course evidence suggests that enhancement and adaptation occupy substantial portions of the reported effort, while its discussion of manageability emphasizes preparing and organizing change. Together, these ideas provide the foundation for the next topic: the problems that make maintenance difficult and the decisions organizations use to respond.')

p=doc.add_paragraph('1.9 Evolution across the operational life cycle',style='Heading 2')
para('Sommerville describes evolution through three operational states. During evolution, the system is actively changed in response to new requirements and environmental conditions. During servicing, the organization makes relatively small changes, often corrections, while the system remains in routine use. During phaseout, the system is still available but receives no major new functionality; users may be directed toward a replacement. These states distinguish the scale and purpose of change over time. They should not be read as a mandatory one-way schedule: a product can remain in one state for an extended period, and organizational decisions determine when a transition is warranted.')
para('The handover from development to maintenance affects how much context is available. A development team may hold design rationale and informal knowledge that is not captured in delivered documents. If maintenance is transferred to a separate team, that knowledge gap becomes an operational risk: the receiving group must infer behavior from code, records, users, and observed operation. Sommerville’s discussion of agile development raises a related tension. Frequent releases and evolving code can leave user documentation behind, while the development team may assume that the maintenance team can interpret the source. The practical response is to make handover content and ownership explicit, especially for interfaces, known limitations, test evidence, and release history.')
para('The same distinction helps separate custom-developed software from packaged software. A custom system is changed for a particular organization’s requirements; a packaged product is developed for a broader market and may be configured or extended through vendor-controlled releases. In either case, the organization must determine who can authorize changes, who can inspect implementation details, and how new versions affect existing data and interfaces. A maintenance plan therefore depends on contractual and technical access as well as on the code’s internal quality.')

p=doc.add_paragraph('1.10 Lehman’s eight observations and their scope',style='Heading 2')
para('Sommerville presents eight laws associated with long-term studies of large organizational software systems whose requirements change with business needs. They are empirical observations about E-type systems, not guarantees for every small program or every release. The table gives a concise, source-faithful explanation of each observation while retaining the original scope qualification.')
grid(['Observation','Maintenance implication'],[
('Continuing change','A system embedded in a changing environment must evolve or become progressively less useful; each release may also influence subsequent needs.'),
('Increasing complexity','Repeated change tends to increase structural complexity unless work is devoted to maintaining or reducing it.'),
('Self-regulation','Evolution exhibits recurring system-level patterns; measures such as size, release interval, and reported errors may remain approximately stable for a particular system.'),
('Organizational stability','Over a system’s life, its long-term development rate may remain approximately constant despite changes in resources.'),
('Conservation of familiarity','The scale of change in a release is constrained by the amount of system knowledge that can be maintained across the people involved.'),
('Continuing growth','Users’ satisfaction depends on a continued increase in useful functionality as needs change.'),
('Declining quality','Quality tends to fall when a system is not adapted to changes in its operational environment.'),
('Feedback system','Evolution involves feedback among multiple participants and loops; those interactions must be understood to improve the process.')],[1.75,5.05],7.7)
para('These observations have consequences for release planning. A large functionality increment may create additional faults that require a later repair-focused release. Small changes can limit structural disruption, although business or market conditions may still make a large release necessary. The laws therefore prompt managers to account for follow-up correction and for the decision delays that influence release pace. They do not prescribe a fixed release size or prove that adding staff has no effect in every project; their claims concern the empirical setting and system scale described by the source.')
para('The laws must also remain distinct from the three software-evolution tendencies summarized by Agarwal et al. That separate account says that software continues to change to remain useful, repeated maintenance can degrade structure, and the development rate remains approximately constant. The overlap with several Lehman observations does not make the two lists identical: the first is an eight-part set with stated E-type scope, while the second is a three-point summary in another text.')

p=doc.add_paragraph('1.11 Long-term cost and maintainability economics',style='Heading 2')
para('Sommerville treats maintainability as an economic property of a system over its useful life. A design or implementation choice that costs more during development may reduce the effort of repeated future changes. The source illustrates this trade-off with a hypothetical example: an additional $25,000 spent to improve maintainability is compared with $100,000 in projected maintenance savings. The figures are an illustration of a possible life-cycle decision, not a measured universal return or a promise that an investment will produce that saving.')
para('Four conditions shape whether the comparison is favorable: the number and complexity of expected changes; the quality of the system design and implementation; the availability of people who understand the system; and the duration for which the system is expected to remain in use. The same improvement may be worthwhile for a long-lived, frequently changed business system and uneconomic for a product nearing retirement. The decision must use expected change traffic and system life, rather than initial development cost alone.')
grid(['Economic question','Evidence to collect before deciding'],[
('How much change is likely?','Request history, expected business and platform changes, and the size or complexity of likely modifications.'),
('How difficult is a change now?','Effort spent locating behavior, understanding dependencies, implementing a change, and validating it.'),
('Who carries system knowledge?','Team familiarity, staff continuity, handover materials, and access to relevant records.'),
('How long must the system remain useful?','Business plans, platform support horizons, replacement feasibility, and the remaining value of the system.'),
('What is the cost of preparation?','A bounded estimate for restructuring, documentation, refactoring, or reengineering and the expected reduction in later work.')],[2.0,4.8],8.0)
para('The comparison is cumulative: maintainability work should be judged against a stream of future changes, not a single repair. It also requires separating a forecast from an observed result. After the system evolves, actual change effort can be compared with the assumptions used in the original investment decision, improving later estimates for that organization.')

# Source-grounded continuation: clusters 2–9. Wording is a close academic
# restatement of the assigned sources; original course figures are embedded.
ASSET=Path(r'C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\05_Seminars_&_Slides\Ch09_Assets')
DIAG=Path(r'C:\Users\gokoq\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch09_Software_Maintenance\diagrams')
MODEL=ASSET/'agent_models'/'audit_20261024'
REG=ASSET/'regression'

def figure(path,caption,width=5.9):
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(path),width=Inches(width))
    p.paragraph_format.keep_with_next=True
    cp=doc.add_paragraph(); cp.alignment=WD_ALIGN_PARAGRAPH.CENTER; cp.paragraph_format.space_after=Pt(5); cp.paragraph_format.keep_together=True
    rr=cp.add_run(caption); rr.italic=True; rr.font.size=Pt(8.5)

def grid(headers,rows,widths=None,size=8.5):
    t=doc.add_table(rows=1,cols=len(headers)); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.style='Table Grid'; t.autofit=False
    if widths:
        for i,w in enumerate(widths): t.columns[i].width=Inches(w)
    for i,x in enumerate(headers): set_cell_text(t.rows[0].cells[i],x,True,(255,255,255),size); shade(t.rows[0].cells[i],'315B7E')
    for ri,row in enumerate(rows):
        cells=t.add_row().cells
        for ci,x in enumerate(row): set_cell_text(cells[ci],x,bold=(ci==0),size=size)
        if ri%2:
            for c in cells: shade(c,'EEF3F7')
    return t

# 2. Maintenance problems and management
p=doc.add_paragraph('2. Maintenance Problems and Management',style='Heading 1')
para('Maintenance is difficult because a change has to be made inside a system whose history, dependencies, and user context may be only partly visible. The effort is not limited to editing a statement: maintainers must recover enough of the existing system’s organization to predict the change’s consequences and preserve required behavior.')
p=doc.add_paragraph('2.1 Why maintenance becomes difficult',style='Heading 2')
para('The course chapter identifies several interacting sources of difficulty. They concern the maintainer’s knowledge, the age and authorship of the product, the way program text communicates structure, the quality of records, the gap between users and technical staff, and whether change was considered during design.')
grid(['Difficulty','Effect on maintenance work'],[
('Understanding before changing','The maintainer must understand an existing program and anticipate what a proposed modification will affect.'),
('Many authors and a long history','Large systems may contain contributions from many people over many years; the current maintainer may not know the original design intent.'),
('Degradation through uninformed change','A change made without understanding the original organization can weaken the system’s structure and make subsequent work harder.'),
('Source text not arranged for comprehension','Program listings may require repeated movement between locations to follow the relevant logic, raising the effort of understanding.'),
('Staff turnover and inadequate records','Later maintainers may not be the original authors. Missing, stale, or insufficient documentation makes it easier to miss effects elsewhere.'),
('User–technical communication gap','Operational experience reveals needs that were not clear during development; users may struggle to express them in a form analysts and programmers can directly implement.'),
('Change not anticipated in design','When the product was not organized to support modification, even a valid change can be difficult to isolate and implement.')],[2.0,4.8],8.2)
para('These difficulties reinforce each other. Weak documentation increases the effort required to understand a system; poor understanding makes impact analysis less reliable; an unanticipated side effect may then create additional corrective work. The sequence explains why maintenance cost depends on the condition and history of the system as well as on the apparent size of the requested edit.')
p=doc.add_paragraph('2.2 Requests are not all the same',style='Heading 2')
para('A separate course survey groups requests by report-related work rather than by the four maintenance purposes in Section 1. The reported shares are: new reports, 40.8%; adding data to existing reports, 27.1%; reforming reports, 10%; condensing reports, 5.6%; consolidating reports, 6.4%; and other requests, 10.1%. This is a different survey partition from both the effort-distribution figure and the activity table. It should be read as the source’s description of request types, not merged into either earlier distribution.')
para('The distinction between request type and maintenance purpose is useful in practice. “Add a field to an existing report” describes the form of the requested work; its purpose may be perfective if it supplies a new capability, corrective if it repairs an omission against an approved requirement, or adaptive if it responds to an external data-format change. Classification therefore needs both the request’s content and its reason.')
p=doc.add_paragraph('2.3 Management responses',style='Heading 2')
para('The chapter presents three broad responses when maintenance demand becomes a management concern. They are alternatives to assess in context, not an automatic decision rule.')
grid(['Response','What it entails','Trade-off emphasized'],[
('Reallocate effort and budget','Shift organizational attention toward requirements, design, maintainability, advanced specification or design practices, and quality assurance.','Preparation consumes resources before a visible change is delivered, but can address causes that make later maintenance expensive.'),
('Replace the existing system','Undertake a new system effort in place of continued maintenance.','Replacement is costly and risky; it does not guarantee a better result and can expose defects in functions that had worked in the old system.'),
('Maintain and enhance the existing system','Continue corrective work and introduce improvements in stages while the system remains in operation.','This retains operational knowledge and working practices and allows new functions or platform integration to be introduced incrementally.')],[1.55,2.8,2.45],8.1)
para('The source’s comparison is deliberately not reduced to “old system versus new system” as a simple technical choice. The existing product may embody stable, valuable behavior that is difficult to reproduce; a new product may offer a cleaner foundation but requires investment and transition. Small corrective or preventive changes can remain affordable even when a large replacement project cannot be justified. Conversely, continued modification can become unattractive if the condition of the system prevents safe or economic change. The chapter does not provide a numerical threshold that resolves every case.')
p=doc.add_paragraph('2.4 Maintenance versus replacement: decision dimensions',style='Heading 2')
para('A source-bounded comparison can be organized around the concerns the chapter identifies: cost, risk, the state of the existing system, the value of preserving its operational behavior, the feasibility of incremental enhancement, and the need to integrate new capabilities or platforms. These dimensions guide analysis without claiming a formula absent from the source.')
bullet('Estimate the maintenance work that is actually expected: correction, environment changes, requested enhancements, and preparation for later change.')
bullet('Assess whether the existing system can be understood and modified while preserving its working functions.')
bullet('Account for replacement effort and transition risk, including whether behavior that users depend on can be reproduced and accepted.')
bullet('Consider whether staged enhancement can satisfy near-term needs while keeping the current system in service.')
bullet('Revisit the decision as the system, its environment, and the value of its functions change; the chapter does not define a one-time permanent choice.')
para('This comparison is an organizing synthesis of the three responses described in the chapter. It should not be mistaken for a source-authored scoring model or an economic break-even equation.')
p=doc.add_paragraph('2.5 Small organizations and one-person production',style='Heading 2')
para('The course exercise asks about the implications of maintenance for a one-person software-production organization but does not supply a distinct model or numerical answer. The source-supported implication is that post-delivery changes still require understanding, impact assessment, implementation, validation, and continued attention to documentation, even when one person performs several roles. A small organization may have less separation between development and maintenance responsibility, but the same change can still affect other functions and operating expectations.')
para('The chapter’s large-system effort percentages cannot be projected onto a one-person organization from the evidence provided. A bounded answer should therefore focus on the work implied by the maintenance process and on the organization’s ability to allocate effort—not claim that one person must spend a fixed fraction of time maintaining software.')
p=doc.add_paragraph('2.6 Maintenance triggers and taxonomy limits',style='Heading 2')
para('Leach itemizes twelve triggers and groups them according to the terminology used in that chapter. The first eight concern changes in the technology surrounding a product: hardware platforms, operating systems, compilers, language standards, communications standards, graphical interfaces, related application packages, and relationships with other software developers. The remaining triggers concern defects revealed after use, customer requests for features, competitive upgrades, and preventing existing errors from reappearing in new releases.')
grid(['Leach grouping','Items included in the source’s list','Interpretation for request triage'],[
('Adaptive: 1–8','Hardware; operating systems; compilers; language standards; communications standards; graphical interfaces; related application packages; relationships with other application/system-software developers.','Record which external dependency changed and identify the system interface, platform assumption, or integration contract it affects.'),
('Corrective / perfective terminology: 9–11','Defects that appear in customer use; demand for features; competitive upgrades.','The source labels this corrective while noting that perfective is also used. Preserve that wording distinction when comparing taxonomies.'),
('Preventive: 12','Prevent existing software errors from appearing in a new release.','Treat regression prevention as a release concern and connect the change to tests and change records.')],[1.6,3.0,2.2],7.8)
para('This classification exposes a taxonomy mismatch worth remembering. In Leach’s twelve-trigger list, the feature-request and competitive-upgrade cases appear in a group labeled corrective, with perfective identified as an alternate term. In the course’s four-purpose scheme, feature addition is usually perfective. The sources are describing related work using different boundaries; the seminar does not silently recast Leach’s group as the course taxonomy. A request ledger can retain both the source classification and the local project classification if comparison is required.')

p=doc.add_paragraph('2.7 Corrective intake, prioritization, and closure',style='Heading 2')
para('Leach presents corrective maintenance as a sequence beginning with problem identification. Finding the responsible module can require trial and error guided by knowledge of the product and software-engineering practice. Before implementation, the organization must decide which issues to fix, how to fix them, and when to schedule the work. Resource limits are part of the decision: some low-priority problems may remain open rather than being repaired immediately.')
numbered('Observe the issue and capture the conditions under which it appears, including the relevant system version and operating environment.')
numbered('Document the reported behavior and determine whether it reflects an actual software fault, a configuration issue, or misunderstanding of operating instructions.')
numbered('Assess severity and importance, estimate repair difficulty, then prioritize work and make explicit decisions about deferred or unfixed issues.')
numbered('Locate the cause, implement a solution, and test the change for effects on other portions of the software.')
numbered('Record the resolution in source comments or records as appropriate, update design and user documentation when their content changes, and update the error history.')
numbered('Verify the repaired behavior and retain the affected modules, effort, and verification information for future maintenance.')
para('The intake process begins before a developer can inspect the source. A support person may need to reproduce a user’s steps, check setup and configuration, and decide whether the user has misunderstood installation or operating instructions. If the fault is real, the report becomes evidence for maintenance; if the instructions or interface caused the problem, that discovery can still generate documentation or usability work. The report should therefore preserve the observed facts rather than assert an unverified cause.')
figure(ASSET/'verified_figures'/'Leach_Fig8_2_Request_Form.png','Figure 2.1. Maintenance request form, Leach, Figure 8.2, printed p. 340.',4.4)
para('The request form records identity and context as well as the symptom: request number, system and version, related requests, environment, problem description, severity, classification, reporter, verification, and the organization responsible for repair. This information allows a report to be linked with a product state and makes prioritization more useful than an unversioned statement that “the system failed.”')
figure(ASSET/'verified_figures'/'Leach_Fig8_3_Response_Form.png','Figure 2.2. Maintenance response form, Leach, Figure 8.3, printed p. 341.',4.5)
para('The response form links the repair to its originating request and records the environment, severity, classification, verification, the person who made the repair, its resolution, affected modules, and time needed. Its second half captures verification of the solution, modules affected, and repair time. This closes the loop between the initial observation and the engineering response, allowing later effort analysis and traceability.')
figure(ASSET/'verified_figures'/'Leach_Fig8_4_Combined_Form.png','Figure 2.3. Combined maintenance request and response form, Leach, Figure 8.4, printed p. 342.',4.6)
para('The combined form keeps the report and response in one record, with a visible separation between problem intake and repair information. Leach notes the value of attaching screen evidence: a digital screen image is preferable where available, while a photograph can preserve what the user saw when direct capture is unavailable. The evidence should support reproduction and diagnosis, not substitute for a clear description of steps, expected behavior, and actual behavior.')
grid(['Record element','What it allows a maintainer to determine'],[
('Request identity and links','Whether this report duplicates or relates to earlier requests.'),
('Product version and environment','Whether the issue depends on a particular build, platform, operating system, GUI, or related package.'),
('Description and severity','What the user observed and how urgently it affects operation.'),
('Verification and ownership','Who checked the report and which organization or maintainer is responsible.'),
('Resolution and modules affected','What was changed and which program areas may require retesting.'),
('Time and closure evidence','How much repair effort was observed and whether the proposed solution was verified.')],[2.0,4.8],8.0)

p=doc.add_paragraph('2.8 Maintenance evidence and bounded examples',style='Heading 2')
para('Leach reports a maintenance database example in which a large share of errors—44 percent in the cited case—was associated with a legacy command-language parser. The action discussed was to remove or freeze that parser rather than continue treating every report as an unrelated defect. The percentage belongs to that system’s error history; it is evidence for investigating a fault concentration, not a general claim that command parsers cause 44 percent of maintenance problems.')
para('A fault history becomes more useful when reports can be grouped by subsystem, release, environment, symptom, and cause. Repeated reports in one component may indicate a structural hotspot, a misunderstood interface, or a concentrated exposure. A high report count alone does not establish the right remedy: the team still needs to compare repair cost, operational importance, alternatives, and risk of a broad change.')

p=doc.add_paragraph('2.9 Synthesis',style='Heading 2')
para('Maintenance difficulty arises from incomplete system understanding, distributed history, structural and documentary weaknesses, evolving user needs, and the consequences of change. Management can respond by improving the conditions for future maintenance, replacing the system, or continuing staged maintenance and enhancement. The central question is how each response preserves useful behavior and supports the changes the organization can justify.')
para('Agarwal et al. add a maintenance to-do list that extends the work beyond correcting code. It includes correcting errors and requirements/design flaws, improving design, making enhancements, interfacing with other systems, conversion to other hardware, migration of legacy systems, and eventual retirement. Their list also calls for maintaining control over day-to-day operation and system modification, perfecting acceptable functions, and preventing performance from falling to unacceptable levels. These activities help distinguish maintenance as life-cycle stewardship from an isolated repair ticket.')
para('Their list of reasons for maintenance includes changing user requirements, system problems, a changing hardware/software environment, efficiency and throughput improvement, component modification, testing the modified product, removing unwanted side effects, fine-tuning or augmenting the software, code optimization, standards review, improved understandability, and correction of specification deviations. Several items overlap with the course categories, but the list is organized by maintenance need and work objective rather than by the course chapter’s survey groupings.')

# 3. Maintenance process and maintainability
p=doc.add_paragraph('3. The Maintenance Process and Maintainability',style='Heading 1')
para('The course process organizes maintenance around an objective, program understanding, a maintenance proposal, ripple-effect analysis, and testing. The diagram’s test decision is a loop: if the modified program does not pass, work returns to the objective; if it passes, the maintenance cycle can exit. Its stages connect technical work with properties needed to make the work dependable.')
figure(DIAG/'CH09_FIG02_Maintenance_Process.png','Figure 3.1. Maintenance process, reproduced from course-text Figure 9.2, printed pp. 464–465.',5.6)
p=doc.add_paragraph('3.1 Establish the maintenance objective',style='Heading 2')
para('A maintenance activity begins with a reason for change. The chapter’s examples include correcting an error, adding a capability, removing functionality that is no longer needed, or optimizing a system. The objective frames what the modification is meant to accomplish and gives later analysis and testing a criterion against which to judge the result.')
p=doc.add_paragraph('3.2 Understand the existing program',style='Heading 2')
para('Before deciding how to modify a program, the maintainer needs a sufficiently accurate account of its behavior and organization. The chapter relates understanding effort to program complexity, including control flow and data flow. Self-descriptiveness concerns how far the program can communicate its structure and intended use through its own organization and accompanying description. A system that is difficult to read or follow increases the effort of working out where a proposed change belongs.')
para('Program understanding is not an isolated preliminary task. It supports the proposal, the estimate of affected areas, the prediction of ripple effects, and the selection of tests. If understanding changes as new dependencies are discovered, the proposal and its impact assessment may need revision.')
p=doc.add_paragraph('3.3 Generate a maintenance proposal',style='Heading 2')
para('A proposal must address the stated objective in the target program. The maintainer needs to understand both the requested outcome and the existing implementation to judge whether the proposed change is suitable. The chapter associates this stage with extensibility: the degree to which the system’s critical functions can support extension. Extensibility is therefore a property of the system in relation to future capability changes, not simply a count of functions or modules.')
p=doc.add_paragraph('3.4 Analyze ripple effects and stability',style='Heading 2')
para('A modification can affect locations beyond the statement or module where it begins. The chapter distinguishes logical or functional consequences from performance consequences. Ripple-effect analysis asks how far the proposed change can propagate through related behavior. Stability describes resistance to amplification: a small proposed change should not cause an uncontrolled expansion of additional modifications. Stability does not mean that a system has no dependencies, that every ripple can be eliminated, or that the system must remain unchanged.')
para('This distinction is important because a local code edit can have nonlocal consequences. A change to an interface, data representation, or shared computation may alter behavior in more than one function. The maintenance proposal should therefore be judged not only by whether it implements the requested behavior, but also by the scope and manageability of the effects it induces.')
p=doc.add_paragraph('3.5 Test the modified program',style='Heading 2')
para('Testing checks that the modified program meets the maintenance objective while preserving at least the reliability expected of the prior system. The chapter emphasizes cost-effective testing and defines testability in terms of the effort required to test a program adequately against a defined criterion. A system that is hard to exercise or whose expected behavior is unclear raises the effort needed to establish confidence in a change.')
para('A failed test is not merely a reporting event in the process diagram; it sends the work back for reconsideration. The change may not meet the objective, the program’s behavior may have been misunderstood, or the impact analysis may have missed a consequence. A successful test permits the process to exit, subject to the organization’s release and configuration controls.')
p=doc.add_paragraph('3.6 Maintainability as a combined property',style='Heading 2')
para('The chapter treats maintainability as a combined set of system attributes that supports understanding, correction, adaptation, and enhancement. Understanding and maintainability are related: the effort to recover how a system works affects the effort needed to change it. Maintainability is not equated with one stylistic feature or one metric; it concerns whether the product and its supporting records can be changed with acceptable effort and control.')
grid(['Process point','Quality property emphasized','Question for the maintainer'],[
('Program understanding','Complexity and self-descriptiveness','Can the relevant behavior, control flow, data flow, and purpose be recovered?'),
('Proposal generation','Extensibility','Can the critical functions support the requested extension?'),
('Ripple analysis','Stability','Will the change remain bounded, or will it amplify into further changes?'),
('Testing','Testability','Can the modified behavior be checked adequately and cost-effectively?')],[1.65,1.7,3.45],8.2)
p=doc.add_paragraph('3.7 Coupling and SESE as bounded study terms',style='Heading 2')
para('The predictive vocabulary includes coupling and single-entry single-exit structure because both relate to the ability to reason about change and tests. The chapter’s general process discussion supports attention to relationships among program parts and to understandable control flow, but its exercise asking why SESE systems are easier to test does not itself provide a developed explanation. In this seminar, these terms are used as analysis prompts: identify how one part depends on another, and identify the entry and exit paths that must be followed when reasoning about a program fragment. No unprovided quantitative coupling scale or universal SESE guarantee is attributed to the course text.')
p=doc.add_paragraph('3.8 Maintainability in requirements and design',style='Heading 2')
para('The process model places maintainability considerations before a change is attempted: system complexity and self-description influence understanding; extensibility influences whether a proposal can be implemented; stability concerns the breadth of its effects; and testability concerns whether the result can be validated. This connection motivates considering maintenance needs in requirements and design documentation rather than treating change cost as something discovered only after release. The course source associates these quality concerns with the stages of its maintenance process; the seminar does not add a new maintenance requirement formula.')

p=doc.add_paragraph('3.9 Change proposals and impact assessment',style='Heading 2')
para('Sommerville describes an evolution request as the input to a controlled sequence: analyze the proposed change, estimate its impact and cost, decide whether to implement it, plan the next release, and implement and validate the selected changes. A request should be connected to the system components it may affect. This relationship matters because a seemingly small requirement can cross subsystem boundaries, introduce dependencies, or force a change in test and user documentation.')
para('Impact analysis is therefore both a technical and a planning activity. The technical analysis identifies components, interfaces, data structures, operational assumptions, and tests associated with the request. The planning analysis estimates effort, value, risk, and release placement. Proposed changes can then be grouped into releases rather than handled as a sequence of unrelated edits. A change may be deferred because its value is low, its cost is high, its dependencies are unresolved, or a safer release opportunity is needed.')
para('Emergency work follows a different path. A serious operational problem may require an immediate modification before the complete analysis and documentation are available. The correction still needs validation and a controlled record; after stabilization, its design rationale, affected artifacts, and test evidence should be reconciled with the system documentation. This separates the timing of the emergency from the obligation to restore the system’s maintained record.')
grid(['Impact-analysis question','Information that supports an answer'],[
('Which behavior is requested?','The observed problem or desired outcome, with acceptance conditions.'),
('Where is the behavior implemented?','Component, interface, data, and cross-reference information from the existing system.'),
('What else can change as a consequence?','Dependencies, callers, shared data, operating assumptions, reports, and linked system functions.'),
('How can correctness be checked?','Existing tests, required new cases, regression history, and observable acceptance criteria.'),
('When should the change be released?','Urgency, benefit, cost, risk, dependencies, available resources, and other requests suitable for the same release.')],[2.3,4.5],8.0)

# 4. Maintenance process models
p=doc.add_paragraph('4. Maintenance Process Models',style='Heading 1')
para('The chapter presents five models that organize maintenance work in different ways. They differ in how they begin, how much analysis and documentation they expect, how they use existing artifacts, and how they move a change into operation. The figures are reproduced from the scanned course text; their sequence and labels govern the descriptions below.')
p=doc.add_paragraph('4.1 Quick-Fix model',style='Heading 2')
figure(MODEL/'CH09_FIG03_QuickFix_source_p466.png','Figure 4.1. Quick-Fix model, course-text Figure 9.3, printed p. 466.',4.1)
para('Quick-Fix maintenance begins when a problem is encountered and the maintainer applies a rapid modification. The method is reactive and concentrates on making the immediate correction or change. Its weak point is the limited analysis of long-term impact and the limited attention that may be given to updating the system’s supporting documentation. As modifications accumulate, the structure may become harder to understand and later changes more difficult or costly.')
para('The chapter does not treat every quick fix as irrational. A temporary fix can be useful when a single maintainer knows the system well, resources or time are constrained, users cannot wait, or a larger upgrade is already planned. The risk is dependence on this mode as the ordinary long-term process: the shortcut may solve the immediate problem while leaving the product and its records less suitable for future change.')
p=doc.add_paragraph('4.2 Iterative Enhancement model',style='Heading 2')
figure(ASSET/'verified_figures'/'CH09_FIG04_Iterative_clean.png','Figure 4.2. Iterative Enhancement model, course-text Figure 9.4, printed p. 467.',5.0)
para('Iterative Enhancement treats maintenance as a sequence of controlled revisions. Its three principal activities are: analyze the existing system; characterize the proposed modifications; and redesign the current version followed by implementation. Work starts from the system’s documentation and updates affected documentation from higher-level descriptions toward implementation detail. The model depends on complete documentation and analysis so that the next version remains understandable.')
para('The model can accommodate other maintenance approaches within its larger cycle, including a quick fix for an urgent issue. The difference is that the system continues to be managed as a series of versions with analysis and document updates, rather than allowing each local patch to stand alone without a considered connection to the system record.')
p=doc.add_paragraph('4.3 Reuse-Oriented model',style='Heading 2')
figure(ASSET/'verified_figures'/'CH09_FIG05_Reuse_clean.png','Figure 4.3. Reuse-Oriented model, course-text Figure 9.5, printed p. 468.',5.7)
para('Reuse-Oriented maintenance starts by identifying parts of the existing system that may serve as reusable candidates. The maintainer then understands the selected parts, modifies them to satisfy the new requirements, and integrates the result into the new system. The model relates old requirements, design, source, and test artifacts to a component library and to corresponding artifacts for the new system. Its starting point can be any phase in the life cycle where suitable reusable material exists.')
para('Reuse is not equivalent to copying code without analysis. Candidate parts must be understood and judged against the new requirement; modification may be needed before integration. The figure makes the artifact relationships visible: requirements, design, source, and test data participate in the reuse path, not source code alone.')
p=doc.add_paragraph('4.4 Boehm process model',style='Heading 2')
figure(MODEL/'CH09_FIG06_Boehm_source_p468.png','Figure 4.4. Boehm maintenance process model, course-text Figure 9.6, printed p. 468.',5.6)
para('Boehm’s process model organizes maintenance as a closed-loop economic decision process. Management objectives and environmental constraints shape a proposed change. The proposal is evaluated in cost–benefit terms; approved work receives resources and a budget; the change is implemented as a new version; and software in use provides feedback to the next cycle. Thus maintenance is connected to operational experience and management decisions, not only to code modification.')
para('This process model must be distinguished from the Boehm-based ACT/AME cost-estimation model in Section 5. The process model describes the flow of proposal, evaluation, approval, implementation, release, and feedback. The estimation model supplies equations for annual maintenance effort. The shared attribution does not make the two models interchangeable.')
p=doc.add_paragraph('4.5 Taute model',style='Heading 2')
figure(ASSET/'verified_figures'/'CH09_FIG07_Taute_review.png','Figure 4.5. Taute maintenance model, course-text Figure 9.7, printed p. 469.',5.0)
para('The Taute cycle is presented as eight named phases: Change Request, Estimate, Schedule, Program, Test, Documentation, Release, and Operation. An operational problem or desired change enters as a request. The work is estimated and its impact considered; an accepted request is scheduled for a release; the program is changed and tested; documentation is updated before release; users accept the release; and the software returns to operation, where further requests may arise.')
para('The order highlights coordination as well as implementation. Estimation precedes scheduling, testing precedes release, and documentation is part of preparing the release. The operational phase closes the loop by returning the maintained software to the environment in which additional change needs can be observed.')
p=doc.add_paragraph('4.6 Model comparison',style='Heading 2')
grid(['Model','Starting emphasis','Characteristic control','Main caution'],[
('Quick-Fix','Immediate problem','Rapid local modification','Repeated use may omit impact analysis and documentation.'),
('Iterative Enhancement','Existing system and its records','Analyze, characterize, redesign, implement; update documents','Requires complete documentation and careful analysis.'),
('Reuse-Oriented','Existing artifacts and reusable parts','Identify, understand, modify, integrate','A candidate must be understood and adapted before use.'),
('Boehm process','Management objective and environmental constraints','Cost–benefit evaluation, approval/resources, implementation, operational feedback','Do not confuse the process model with the ACT/AME equation.'),
('Taute','Change request','Estimate, schedule, program, test, document, release, operate','A request is not ready for release merely because its code change is complete.')],[1.2,1.65,2.2,1.75],7.9)
para('The models are complementary views rather than five competing universal laws. They make different parts of maintenance visible: urgency, iterative system evolution, reuse of artifacts, economic approval, or release discipline. The chapter also allows one model’s activities to appear within another broader approach.')

# 5. Maintenance cost estimation
p=doc.add_paragraph('5. Maintenance Cost Estimation',style='Heading 1')
para('The chapter presents three levels of estimation: a relative effort ratio for analysis, design, and implementation; the Belady–Lehman maintenance-effort model; and the Boehm ACT/AME approach with an effort adjustment factor. Their inputs and units differ, so the models must be applied separately and interpreted within their stated assumptions.')
p=doc.add_paragraph('5.1 Relative repair effort',style='Heading 2')
para('The course table gives the relative ratio Analysis : Design : Implementation as 1 : 10 : 100. This expresses a relative effort relationship in the cited presentation; it is not a currency rate, a universal staffing estimate, or an equation that converts every maintenance request into hours. Its instructional use is to emphasize that implementation effort can dominate the listed repair phases in the example framework.')
p=doc.add_paragraph('5.2 Belady–Lehman model',style='Heading 2')
p=para('M = P + K e^(c − d)'); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
para('The model defines M as total effort expended, P as productive effort—analysis, design, coding, testing, and evaluation—K as an empirical calibration constant, c as complexity associated with poor design or documentation, and d as the maintenance team’s familiarity with the system. The exponential term makes complexity and familiarity consequential to the estimate: greater complexity increases the effort component, while greater familiarity reduces it.')
para('Worked Example 5.1 uses P = 500 person-months, K = 0.3, and c = 8. With d = 0.9, the estimated result is 863.59 PM; with d = 0.1, the result is 1,309.18 PM. The comparison holds the other inputs fixed and demonstrates the model’s sensitivity to team familiarity. M remains the model’s total effort quantity; it must not be relabeled as maintenance effort alone.')
grid(['Input','Meaning in the model','Example value(s)'],[
('P','Productive effort covering analysis, design, coding, testing, and evaluation','500 PM'),('K','Empirical calibration constant','0.3'),('c','Complexity associated with poor design/documentation','8'),('d','Maintenance-team familiarity','0.9 or 0.1'),('M','Total effort expended under the model','863.59 PM or 1,309.18 PM')],[0.75,3.7,2.35],8.2)
p=doc.add_paragraph('5.3 ACT and AME',style='Heading 2')
para('Annual Change Traffic (ACT) represents the fraction of the software instructions changed during a year through additions and deletions. The course equation is:')
p=para('ACT = (KLOC_added + KLOC_deleted) / KLOC_total'); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
para('The course text counts modified code as both added and deleted for this measure: the former version is removed and the changed version is introduced. The numerator is therefore additions plus deletions, not additions plus a separate “modified” count. This distinction prevents a modified portion from being counted only once when applying the source’s definition.')
para('Annual Maintenance Effort (AME) begins with ACT and Software Development Effort (SDE), measured in person-months. The baseline estimate is ACT × SDE. When an Effort Adjustment Factor is used, the adjusted estimate is:')
p=para('AME = ACT × SDE × EAF'); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
para('Worked Example 5.2: with ACT = 0.15 and SDE = 600 PM, the annual estimate is 90 PM. Over ten years this is 900 PM, giving 1,500 PM total when the initial 600 PM development effort is included. The annual, decade-total, and full life-cycle quantities must remain distinct.')
para('Worked Example 5.3: ACT = 0.10/year and SDE = 500 PM. The example’s effort multipliers are RELY high 1.15, DATA high 1.08, ACAP high 0.86, AEXP very high 0.82, and LEXP high 0.95. Their product gives EAF = 0.83206548, approximately 0.832; therefore AME = 0.10 × 500 × 0.83206548 ≈ 41.6 PM per year.')
grid(['Factor','Rating used in example','Multiplier'],[
('RELY','High','1.15'),('DATA','High','1.08'),('ACAP','High','0.86'),('AEXP','Very high','0.82'),('LEXP','High','0.95'),('EAF','Product of listed multipliers','0.83206548 ≈ 0.832')],[1.2,3.25,2.35],8.2)
p=doc.add_paragraph('5.4 Factors affecting maintenance effort',style='Heading 2')
para('Agarwal et al. list ten conditions that can change the effort required to maintain a system. These factors explain why identical change counts need not produce identical effort:')
grid(['Factor','How it conditions the estimate'],[
('Application type','The kind of system and its operational demands shape the nature and consequences of change.'),
('System novelty','A less familiar or unusual system can require additional effort to understand and modify.'),
('Staff turnover and availability','The continuity and availability of maintenance personnel affect the knowledge and capacity available.'),
('System life span','The expected period of continued operation changes how much future maintenance is relevant.'),
('Dependence on a changing environment','Frequent external change can create recurring adaptation work.'),
('Hardware characteristics','The target hardware and platform constrain implementation and conversion effort.'),
('Design quality','The design affects how readily a change can be located, reasoned about, and contained.'),
('Code quality','The organization and clarity of code affect modification effort.'),
('Documentation quality','Current, adequate system records reduce the work needed to recover design intent and dependencies.'),
('Testing quality','The available test evidence affects the effort needed to establish that a change is correct.')],[1.8,5.0],7.8)
para('Agarwal et al. report maintenance as roughly 40–60% of full life-cycle cost and explicitly note that the share can vary by application domain. The scanned course text instead cites a 40–70% range for large-scale software systems. These figures have different stated boundaries and are not averaged into a single forecast. Neither range should be used as a universal estimate for a particular system.')
p=doc.add_paragraph('5.5 Reading estimates responsibly',style='Heading 2')
para('Each estimate is conditioned by its inputs. Belady–Lehman uses productive effort, calibration, complexity, and familiarity; ACT/AME uses annual change traffic, baseline development effort, and—in the adjusted form—an effort factor. The relative repair ratio offers a comparison among work phases rather than a complete project estimate. These methods should not be collapsed into one formula or treated as guarantees of actual effort.')
para('The supporting estimation discussion also points to the information needed to improve a forecast: the number and complexity of change requests, the volatility of requirements and business processes, time spent on impact analysis, implementation time, and outstanding requests. The value of an estimate depends on the quality of those inputs and on whether the estimate is calibrated to the organization and system under consideration.')

p=doc.add_paragraph('5.6 Predicting change demand and maintenance hotspots',style='Heading 2')
figure(ASSET/'verified_figures'/'Sommerville_Fig9_10_Maintenance_Prediction.png','Figure 5.1. Questions linking change prediction, maintainability, and maintenance cost, Sommerville, Figure 9.10, printed p. 247.',5.3)
para('Sommerville separates three related forecasts: which system parts are likely to be affected by requests; which parts are likely to be most expensive to maintain; and what the overall maintenance cost may be for a period such as the next year or the system’s remaining life. These questions require different evidence. Change frequency depends on the system’s relationship with its environment; expensive hotspots depend on component complexity and accumulated change; total cost depends on both expected demand and the effort required to respond.')
para('Three external indicators help estimate change demand: the number and complexity of system interfaces; the number of requirements that are inherently volatile, such as those shaped by policy or procedure; and the business processes that depend on the system. More interfaces create more opportunities for external change. More volatile requirements and business processes create more reasons to request change. These indicators identify exposure, not the exact number of future requests.')
para('After deployment, process measures provide evidence about maintainability. Sommerville identifies four measures: the number of corrective-maintenance requests; average time for impact analysis; average time to implement a request after impact analysis; and the number of outstanding requests. A growing fault backlog or increasing analysis and implementation times can signal declining maintainability. These measures should be interpreted together: implementation time is distinct from impact-analysis time, even when both move in the same direction.')
grid(['Measure','What a sustained increase may indicate','Measurement caution'],[
('Corrective requests','More faults are being introduced than repaired, or system quality is declining.','Separate the number of reports from severity and from duplicate reports.'),
('Impact-analysis time','More components or dependencies must be examined for each change.','Record the request class and scope; complex requests naturally take longer.'),
('Implementation time','The system and its documentation take more effort to modify after affected components are identified.','Do not combine with impact-analysis duration if diagnosing the source of delay.'),
('Outstanding requests','The organization cannot resolve incoming changes at the rate they arrive.','Account for priority, deferred work, rejected items, and changes awaiting information.')],[1.65,3.1,2.05],7.7)
para('Complexity measures can help identify components that deserve closer attention, but a system-wide average can hide concentrated maintenance effort. Sommerville reports that effort often focuses on a relatively small set of complex components. A practical response is to combine complexity indicators with request history and impact-analysis evidence, then consider replacing especially difficult components with simpler alternatives where the system’s constraints allow it. This is a prioritization strategy, not a claim that a single complexity metric predicts all maintenance cost.')

p=doc.add_paragraph('5.7 Economic choice: reengineer or redevelop',style='Heading 2')
para('Pressman’s Sneed-style economic comparison keeps several current and projected quantities visible: current and projected maintenance cost; current and projected operations cost; current and projected business value; reengineering cost and duration; risk; and the expected remaining system life. The comparison is not a single cost ratio. It asks whether a reengineered system can preserve or increase business value while reducing future maintenance and operating burden, and whether the expected period of use is long enough to recover the transformation effort.')
grid(['Economic variable','Decision question'],[
('Current maintenance cost','What does it cost to keep the existing product changeable and correct now?'),
('Projected maintenance cost','How is that burden expected to change if the system is left as it is?'),
('Current and projected operations cost','What resources are needed to run the present system, and how are those costs expected to move?'),
('Current and projected business value','What value does the system deliver today, and what value is expected during its remaining life?'),
('Reengineering cost and time','What will the transformation require in money, effort, and calendar duration?'),
('Risk','What operational, migration, quality, or delivery risk accompanies the reengineering decision?'),
('Expected remaining life','For how long can the organization expect to benefit from the transformed system?')],[2.0,4.8],7.9)
para('These variables support a comparison among continued operation, reengineering, and replacement. If remaining life is short, a large transformation may not repay its cost. If business value remains high but maintenance burden is rising, reengineering may be preferable to a risky full redevelopment. If the business value is low or a supported replacement meets the need at reasonable cost, the balance can shift. The estimate is only as credible as its projected values and assumptions, so uncertainty and scenario ranges should be recorded.')
para('Mall adds a caution about effort estimators: ACT is only one input to maintenance cost and may omit conditions such as staff experience, product familiarity, hardware, and system complexity. In embedded applications, domain-specific factors also affect cost. An ACT-based figure should therefore be treated as a baseline estimate whose assumptions need review, not as a complete model for every product domain.')

# 6. Regression testing
p=doc.add_paragraph('6. Regression Testing and Selective Retest',style='Heading 1')
para('Regression testing checks that changes have not damaged behavior that previously worked. The chapter contrasts regression testing with testing during initial development and then considers how to select a relevant subset of tests when rerunning the entire suite would be too costly.')
p=doc.add_paragraph('6.1 Regression testing compared with development testing',style='Heading 2')
grid(['Dimension','Development testing','Regression testing'],[
('Test material','A test plan and suite are developed for the new system.','Existing tests can be retained, adapted, and reused after a change.'),
('Scope decision','The product and its planned components define the testing scope.','Testing can cover all components or focus on components affected by the change.'),
('Resource setting','A new development plan allocates testing resources.','The available retest budget may be constrained by maintenance priorities.'),
('Timing','Testing is organized around development milestones.','Testing recurs across the software’s life as changes are made.')],[1.25,2.8,2.75],8.0)
p=doc.add_paragraph('6.2 Why select a subset',style='Heading 2')
para('A large regression suite may be expensive to execute after every modification. Selective retesting chooses a subset intended to exercise the changed system efficiently. Selection must still retain tests that can expose faults caused by the change. If minimization removes a defect-revealing test, the suite may be smaller but provide inadequate evidence about the modified program.')
figure(REG/'CH09_FIG09_Regression_Code_Fragments.png','Figure 6.1. Code fragments used to illustrate regression-test selection, course-text Figure 9.8, printed p. 474.',5.8)
figure(ASSET/'verified_figures'/'CH09_FIG10_Regression_Test_Cases_clean.png','Figure 6.2. Test cases and execution history used in regression selection, course-text Figure 9.9, printed p. 475.',5.8)
para('The paired program-fragment example shows why execution-history overlap alone is not enough to justify removing a test. In the modified fragment, a statement changes the divisor. Two tests may execute the same listed statements, yet only one input reaches the newly introduced divide-by-zero condition. If a minimized suite retains the other test and drops the revealing case, statement-path similarity can hide the regression. The example therefore ties the selection decision to both the modification and the fault condition being sought.')
p=doc.add_paragraph('6.3 Three selection categories',style='Heading 2')
grid(['Category','Selection purpose','Interpretive limit'],[
('Coverage','Choose tests that exercise relevant program elements or changed regions.','Coverage of a region does not alone prove that every affected behavior is correct.'),
('Minimization','Reduce a suite while preserving the selected coverage or criterion.','Over-aggressive minimization can omit a test that reveals a regression.'),
('Safe selection','Select tests according to a criterion intended to retain tests relevant to the modification.','Use the source’s criterion; do not claim that a method is universally safe without its conditions.')],[1.2,3.0,2.6],8.0)
para('A selective retest suite can also be described by the status of its test cases:')
grid(['Test-case status','Use after a modification'],[
('Reusable','The test exercises code and specifications that remain unchanged. It can be retained and reused in a later session.'),
('Retestable','The test exercises modified code or a modified specification and should be run again.'),
('Specification-obsolete','The input/output relationship for which the test was designed has changed, so the old test no longer checks the current specification.'),
('Coverage-obsolete','The test no longer exercises the program component or behavior it was originally intended to cover.'),
('Unclassified','The maintainer cannot confidently place the test in another category; it remains visible for review instead of being silently discarded.')],[1.65,5.15],8.0)
para('The two obsolete cases arise for different reasons: the specified behavior may have changed, or the test may no longer reach the part of the program it was designed to exercise. When the existing suite does not cover new structures or specification items, selective retesting may also require new structural or specification-based cases. Keeping these statuses explicit makes the selection review traceable and reduces accidental loss of useful evidence.')
p=doc.add_paragraph('6.4 Selection-quality criteria',style='Heading 2')
para('The chapter evaluates selection approaches using four criteria: inclusiveness, precision, efficiency, and generality. Together they ask whether relevant tests are included; whether unnecessary tests are avoided; whether the selection can be produced or executed economically; and whether the approach applies beyond a narrow special case. An approach can perform well on one criterion and still be weak on another, so the criteria should be considered as a set.')
bullet('Inclusiveness: whether the selected tests cover the relevant behavior or changes that must be checked.')
bullet('Precision: whether the selection avoids tests unrelated to the modification while retaining relevant ones.')
bullet('Efficiency: whether selecting and running the tests is practical given the available retest resources.')
bullet('Generality: whether the selection approach supports a useful range of programs and modifications.')
p=doc.add_paragraph('6.5 Retest decision and evidence',style='Heading 2')
para('The retest decision connects change-impact information with the existing test history. The maintainer identifies what changed, traces the relationships shown in the program, and selects tests according to a stated criterion. The recorded result should make clear which tests were rerun and what scope the selection covered. The source’s treatment supports selective rerun as a cost response, but does not imply that a reduced suite automatically offers the same evidence as a complete suite.')

p=doc.add_paragraph('6.6 Concurrency limits on test evidence',style='Heading 2')
para('Leach highlights a boundary of ordinary testing: some failures depend on the order in which concurrent processes obtain processor time or access shared state. Such an interleaving may occur rarely in a test run even when the defect exists. A race condition arises when the outcome of a computation depends on the order of concurrent execution. A test that passes under one schedule cannot establish that all possible schedules produce the same result.')
figure(ASSET/'verified_figures'/'Leach_Fig8_5_Race.png','Figure 6.3. Two concurrent instruction sequences that can produce order-dependent results, Leach, Figure 8.5, printed p. 345.',4.5)
para('The source figure places two processes around a shared variable. If their operations interleave in one order, one value remains; if the instructions interleave differently, a different final result can occur. The defect is therefore not determined solely by the input data: scheduling is also part of the execution condition. When maintenance changes synchronization or shared-state access, regression selection should consider concurrent paths and timing assumptions rather than only the affected sequential statements.')
para('A second hazard concerns an operation that appears to protect a shared resource but is not atomic. A process can be interrupted between checking a condition and acting on it. Another process may then alter the resource state before the first process proceeds, invalidating its earlier check. The resulting failure may be especially serious in real-time or safety-critical systems because scheduling is difficult to predict and tests may not reproduce the rare interleaving.')
figure(ASSET/'verified_figures'/'Leach_Fig8_6_Nonatomic.png','Figure 6.4. A non-atomic test-and-use sequence for a shared resource, Leach, Figure 8.6, printed p. 346.',4.7)
para('The figure’s sequence is a guard followed by a separate operation on the shared resource. If the guard and operation are not indivisible, another process can change availability in between. The maintenance implication is to inspect the actual synchronization guarantees of operating-system or library calls and the finite resources they protect. Repeating the same test many times may increase confidence in observed behavior, but it cannot by itself guarantee correctness for unobserved schedules. Where the failure consequence is high, review of concurrency design and the synchronization mechanism is necessary alongside testing.')
grid(['Test evidence can show','Test evidence alone cannot establish'],[
('A set of selected executions passed under the schedules observed.','That every possible process schedule was exercised.'),
('A modification did not trigger failures in the retained regression cases.','That a rare race or non-atomic interleaving cannot occur in operation.'),
('The test configuration satisfied its recorded environment assumptions.','That a real-time system will meet every run-time constraint under all loads.'),
('Concurrent behavior was sampled or stressed under chosen conditions.','A mathematical guarantee of atomicity or schedule-independent behavior when the design lacks it.')],[3.4,3.4],7.8)

# 7. Reverse engineering, reengineering, legacy systems
p=doc.add_paragraph('7. Reverse Engineering, Reengineering, and Legacy Systems',style='Heading 1')
para('The chapter turns to systems whose implementation exists but whose higher-level structure or rationale must be recovered. Reverse engineering seeks information and understanding from an existing software product. Reengineering uses knowledge of an existing product to transform it, while restructuring changes representation without changing the program’s functionality.')
p=doc.add_paragraph('7.1 Reverse engineering and its products',style='Heading 2')
para('The course discussion associates reverse engineering with several tasks: program comprehension, redocumentation, design recovery, identification of reusable components, determination of restructuring needs, discovery of business rules, and production of a higher-level system description. These activities recover different kinds of knowledge from the existing product; they are not all synonyms for translating code into another language.')
para('The chapter groups reverse-engineering work by the information sought. One task maps the application or problem domain to the programming or implementation domain. Another recovers high-level structure whose original purpose may have become obscured by later bug fixes, porting, modification, or enhancement. Reverse engineering can also search for links between program syntax and behavior when original semantics or design rationale are no longer available, and identify components that could be candidates for reuse. The result depends on the information requested; it need not reconstruct every original design decision.')
figure(DIAG/'CH09_FIG10_Domain_Mapping_complete.png','Figure 7.1. Domain mapping in reverse engineering, course-text Figure 9.10, printed p. 477.',5.7)
figure(DIAG/'CH09_FIG11_Reverse_Eng_Levels.png','Figure 7.2. Abstraction levels for reverse engineering, course-text Figure 9.11, printed pp. 477–478.',5.4)
para('The abstraction-level figure distinguishes implementation, design, and specification information. Redocumentation remains at a similar abstraction level by making existing information easier to use. Design recovery moves from implementation evidence toward a design description; specification recovery seeks still higher-level statements about the system. The figure’s levels clarify what kind of representation is being recovered rather than promising that every system yields a complete original specification.')
p=doc.add_paragraph('7.2 Course-named support tools',style='Heading 2')
para('The course chapter names a bounded set of tools used in the reverse-engineering discussion: restructurers, cross-referencers, static analyzers, text editors, Rigi, and ReFine. Their role is to help examine, navigate, report on, or reorganize program information. Rigi is described in connection with extracting components and relationships and arranging subsystem views. ReFine is described as a language-oriented workbench supporting browsing and report generation. These source-named examples are retained without adding a modern tool catalogue that the course chapter does not supply.')
para('The scanned chapter describes the component tools more specifically. A restructurer identifies poorly structured fragments and replaces them with an equivalent structured form. A cross-referencer reports where variables are defined and used. A static analyzer can flag anomalous constructs such as uninitialized variables or dead code. A text editor and related simple tools support source browsing and editing. These functions are distinct: navigation, structural transformation, static examination, and text modification address different maintenance needs.')
para('Rigi’s workflow begins by extracting components and relationships from source code into a repository; extraction includes parsing and recording such information as data types, functions, and dependencies. Graph-based views then support construction of subsystem hierarchies from those relationships. The analyst can examine subsystem structure, interfaces, and dependencies, and assess cohesion or coupling while refining the views. This supports identifying maintenance hot spots and possible reusable modules, but a structural view alone does not reveal every dynamic behavior.')
para('ReFine is described as a family of language-oriented workbenches that can be customized for programming languages. Reported capabilities include source navigation and browsing, generation of structural and definition reports, online viewing and printing of reports, and export of design information to forward-engineering tools. These are capabilities attributed to that source-named workbench, not a claim that every maintenance tool provides them.')
grid(['Tool named in the chapter','Use within the chapter’s discussion'],[
('Restructurer','Supports transformation of program structure while retaining intended functionality.'),
('Cross-referencer','Helps locate relationships and references among program elements.'),
('Static analyzer','Examines program properties without presenting it as a replacement for system understanding.'),
('Text editor','Supports inspection and modification of source text.'),
('Rigi','Extracts components and relationships and supports subsystem-oriented views.'),
('ReFine','Language-oriented workbench with browsing and report-generation support.')],[1.65,5.15],8.2)
p=doc.add_paragraph('7.2.1 Recovering processing, data, and interface views',style='Heading 3')
para('Pressman separates reverse-engineering analysis by the kind of system information that must be recovered. Processing recovery moves from a high-level view of the whole system toward programs, components, recurring patterns, and individual statements. At each level the analyst asks what processing occurs, what data it uses or produces, and how the operations relate. Moving to finer detail can clarify implementation, but it does not automatically reveal the business reason for a computation; domain knowledge and user confirmation may still be needed.')
para('Data recovery begins with evidence found in source structures, files, and databases. A candidate object model can be formed from recurring data entities, refined by identifying keys and class boundaries, and then improved by considering shared characteristics and relationships among the entities. Database schema recovery may require several passes: derive candidate classes from program data, identify keys that distinguish records, refine the classes, consider generalization where attributes or behavior are shared, and establish associations supported by actual processing. The resulting schema is a recovered model to validate, not a claim that the original designers used exactly that model.')
para('Interface recovery focuses on the actions available to a user, the system responses to those actions, and the data exchanged through the interface. If an existing interface is replaced, equivalence should be evaluated in terms of the tasks and business behavior that must remain available, not only by copying the old screen layout. A redesigned interface can change interaction while preserving required operations. Conversely, copying its appearance without understanding its behavior can omit hidden rules, error paths, or data constraints.')
para('Mall describes a preparation step before design recovery: make the program easier to read while preserving behavior. The examples include consistent formatting, meaningful identifiers, simplifying deeply nested conditionals where the logic allows it, and replacing suitable complex branching with clearer structures. Such cleanup reduces noise during later analysis, but it must be checked carefully because a readability change can itself alter behavior. It is therefore a controlled preparation activity with regression evidence, not a license to rewrite before understanding the system.')
grid(['Recovered view','Evidence examined','Validation question'],[
('Processing structure','Calls, control flow, data flow, components, and recurring code patterns.','Can the recovered operations be related to observed system behavior and relevant requirements?'),
('Data structure','Records, files, database schemas, keys, recurring entities, and relationships in code.','Do the proposed entities and associations match actual data and business constraints?'),
('User interface','User actions, visible responses, input/output constraints, and interface data.','Does the recovered behavior cover the tasks users must perform, including error cases?'),
('Design or requirements','Recovered processing, data, interface behavior, and stakeholder knowledge.','Which parts are directly evidenced, and which remain hypotheses needing confirmation?')],[1.55,2.7,2.55],7.8)
p=doc.add_paragraph('7.3 Legacy software and reengineering',style='Heading 2')
para('A legacy system may have accumulated enhancements and quick fixes over a long period. As its structure and records become harder to understand, additional change can become more difficult and costly. Reengineering transforms an existing system to improve its maintainability while making use of the system already in operation.')
figure(ASSET/'verified_figures'/'CH09_FIG08_New_Dev_vs_Reeng.png','Figure 7.3. New development compared with reengineering, course-text Figure 9.8, printed p. 481.',4.6)
para('The comparison distinguishes beginning from a specification and creating a new implementation from beginning with existing software and recovering or transforming its structure. Reengineering does not make the existing program disappear from the process: it treats the program and related information as the starting point for improvement.')
para('The source discussion links reengineering to legacy-system conditions: years of unplanned evolution, accumulated enhancements and patches, difficult or unavailable documentation, staff who no longer know the system, and products that were not designed for change. Reengineering may include redocumentation, restructuring, translation to a more modern language, implementation on newer hardware, and recovery of design information. The choice between reengineering and redevelopment depends partly on the extent of work required and the condition of the software; reengineering is not automatically preferable.')
p=doc.add_paragraph('7.3.1 Reengineering activities and limits',style='Heading 3')
figure(ASSET/'verified_figures'/'Sommerville_Fig9_11_Reengineering.png','Figure 7.4. Reengineering activities and program/data artifacts, Sommerville, Figure 9.11, printed p. 249.',5.8)
para('Sommerville presents a general reengineering path in which an existing program can be translated, analyzed to recover documentation, structurally improved, reorganized into clearer modules, and—when necessary—paired with data reengineering. The stages do not form a mandatory checklist in every project. Source translation may be unnecessary if the original language remains acceptable; reverse engineering may be unnecessary when the program is transformed automatically and reliable documentation already exists; data reengineering is needed when the data structures change.')
para('The activities address distinct artifacts. Source translation changes the programming-language representation. Reverse engineering extracts program information and can produce documentation. Program-structure improvement makes control flow easier to read and understand, often with some manual intervention. Program modularization groups related parts, removes redundancy, and may involve architectural refactoring. Data reengineering addresses the data representation and may include schema changes, conversion, and cleanup. An adapter or wrapper can present a better-structured interface around a legacy program so newer components can use it without requiring every internal interface to be replaced.')
para('Pressman’s chapter organizes reengineering in six activities: inventory analysis, document restructuring, reverse engineering, code restructuring, data restructuring, and forward engineering. Inventory analysis identifies candidate systems and prioritizes them; its priority should be revisited as the portfolio and business context change. Document restructuring depends on the value and condition of existing records. Reverse engineering recovers representations and relationships. Code and data restructuring transform their respective program and information structures. Forward engineering uses the recovered understanding to build the improved target representation. The activities are cyclical in application and can be selected according to what the system needs.')
para('A reverse-engineering result can be assessed along four dimensions: the abstraction level reached; the completeness of information recovered; how interactively an analyst can examine and refine it; and the direction of transformation from implementation toward higher-level descriptions. Tool automation can speed extraction, but these properties remain constraints on what the analyst actually knows. Recovery of a design view does not prove that the original rationale has been reconstructed, and incomplete or ambiguous code can leave more than one plausible explanation.')
grid(['Transformation boundary','What changes','What the source distinction protects'],[
('Code restructuring','Program organization or representation.','Keep the behavior-preserving transformation separate from a feature change.'),
('Data restructuring','Data structures, files, database schema, or values.','Recognize migration and cleanup work as a separate source of risk.'),
('Forward engineering','The target implementation or reconstructed system.','Use recovered knowledge to produce the transformed result rather than treating analysis as the final deliverable.'),
('Architectural change','Interfaces, component structure, or system organization.','Expect additional manual design and cost; automatic transformations have practical limits.')],[1.65,2.4,2.95],7.8)
para('Pressman’s economic discussion also asks whether reengineering is worthwhile in relation to the system’s remaining useful life, expected future maintenance and operations costs, business value, risk, and reengineering time and cost. The lower-cost end of the spectrum includes more automated transformations; architectural migration is substantially more expensive. Reengineering can improve maintainability but is not equivalent to a newly designed system: radical architectural and data-management changes are difficult to automate and can erase the economic advantage.')
para('Mall distinguishes two process models. In a direct maintenance model, developers use the running system, available source, and execution traces to make bounded changes without first performing an extensive reverse-engineering and forward-engineering cycle. A second model makes reverse engineering and forward engineering explicit around the change. Mall’s comparison includes an empirical threshold suggesting that when rework exceeds about 15 percent, the broader reengineering model may be worth consideration. That threshold belongs to the cited study and its context; it is a decision prompt, not a universal cutoff for every codebase.')

p=doc.add_paragraph('7.3.2 Reengineering case: IMP-8 ground software',style='Heading 3')
para('Leach’s IMP-8 example shows why reengineering can preserve useful capability after its original platform becomes difficult to support. The satellite generated research data over a 33-year operating span. In 1997, about nine years before data transmission ended, the organization faced a maintenance charge for a dedicated mainframe that was comparable to the budget for the broader ground-control, data-storage, operations, and personnel effort. Replacing the ground hardware while preserving the still-useful software capability became the selected direction.')
para('The program contained 33 files and 108,161 lines of code, combining FORTRAN and Unisys assembly language. The FORTRAN was ported to a common FORTRAN 77 dialect; assembly portions were rewritten in FORTRAN. The files were separated into 584 individual modules/files to support analysis. Control-graph tools helped identify a small 2 percent of modules with complex internal structure, which then received additional testing attention. Pairwise comparison also exposed copied source: 19.4 percent of files were duplicates once naming conventions were accounted for. This gave the team a way to reduce redundant maintenance targets while moving to a modern workstation environment.')
para('The case makes three bounded points. First, remaining mission value can justify transformation even after the original vendor environment becomes uneconomic. Second, code metrics and clone comparison can focus review and test effort, but the figures only describe this project. Third, migration is not simply a compiler operation: the team translated source, separated modules, inspected complexity, removed duplicated copies, and retested the resulting software. The example does not imply that all legacy systems should be reengineered; the business value and remaining life made the effort meaningful in this case.')
p=doc.add_paragraph('7.4 Working with legacy code',style='Heading 2')
para('The chapter offers eight practical recommendations for understanding and maintaining legacy code. They focus on reading the product as it exists, making its structure and relationships visible, limiting the reach of change where possible, and preserving detailed maintenance information.')
numbered('Study the code before attempting a modification.')
numbered('Focus first on the overall control flow.')
numbered('Add comments that clarify the internal code.')
numbered('Create cross-references among relevant program elements.')
numbered('Build symbol tables to help identify and locate program names.')
numbered('Use local variables, constants, and declarations to localize effects.')
numbered('Keep detailed documentation of maintenance activity.')
numbered('Apply modern design techniques when improving the program.')
para('These recommendations are presented as guidance for maintaining existing code. They are not additional reverse-engineering phases or a guarantee that a legacy system can be fully recovered from source text alone.')
p=doc.add_paragraph('7.5 Program restructuring',style='Heading 2')
para('Restructuring changes a program’s representation while preserving its semantics or functionality. The chapter identifies control-flow-driven, efficiency-driven, and “adaption-driven” restructuring. The last label follows the source’s spelling; it is retained as such rather than silently normalized into a different taxonomy.')
figure(DIAG/'CH09_FIG13_Program_Restructuring.png','Figure 7.5. Program restructuring example, course-text Figure 9.13, printed p. 483.',4.6)
para('The source illustration shows a control-structure transformation from an IF/THEN/ELSE form into a CASE form. The example is about representation and structure; the defining condition remains that the program’s behavior is preserved. Restructuring must therefore be distinguished from reengineering as the broader transformation of an existing system and from redevelopment that begins from a specification.')
para('The three restructuring types describe different motivations. Control-flow-driven restructuring imposes a clearer modular or intramodular flow structure to improve readability and understanding; it may not fully solve poor modularity if related components remain dispersed. Efficiency-driven restructuring reorganizes computation to reduce unnecessary evaluation; the source’s IF/THEN/ELSE to CASE example reduces repeated Boolean evaluation. Adaption-driven restructuring changes representation so the program fits a new language or operating environment, or maps sequential processing to an equivalent parallel form. In each case, preserving program semantics is the boundary that distinguishes restructuring from a behavior-changing enhancement.')
p=doc.add_paragraph('7.6 Relationship of the terms',style='Heading 2')
grid(['Term','Primary concern','Relationship'],[
('Reverse engineering','Recover information or higher-level understanding from an existing product.','Can support comprehension, documentation, design/specification recovery, reuse decisions, and restructuring.'),
('Reengineering','Transform an existing system to improve its condition or maintainability.','Uses the existing software as a starting point and may include reverse- and forward-oriented work.'),
('Restructuring','Change representation while preserving functionality.','A focused transformation that can form part of a wider reengineering effort.'),
('Legacy maintenance','Continue to understand, correct, adapt, or enhance an established system.','Uses records, cross-references, structure, and disciplined changes to keep the system serviceable.')],[1.35,2.5,2.95],8.0)
p=doc.add_paragraph('7.7 Legacy-portfolio assessment',style='Heading 2')
para('Sommerville evaluates a legacy portfolio using two independent questions: how much business value each system contributes and how good its application and operating environment are. A system’s business importance does not guarantee sound technical quality, and a technically sound system may contribute little business value. Keeping these axes separate supports four strategic responses.')
figure(ASSET/'verified_figures'/'Sommerville_Fig9_13_Legacy_Assessment.png','Figure 7.6. Business value and system quality in legacy assessment, Sommerville, Figure 9.13, printed p. 254.',5.4)
grid(['Business value','System quality','Typical strategy described by Sommerville','Reasoning'],[
('Low','Low','Scrap or retire.','Continued operation is costly while the contribution to the business is small.'),
('High','Low','Reengineer; consider replacement if a suitable package is available.','The system matters, but poor quality makes continued change expensive.'),
('Low','High','Continue ordinary maintenance while conditions remain favorable; reconsider if expensive change is required.','The system is not costly to maintain, but replacement investment is difficult to justify.'),
('High','High','Keep operating and continue normal maintenance.','The system contributes strongly and is technically adequate, so transformation is not immediately needed.')],[1.1,1.05,2.45,2.2],7.4)
para('The axes are assessed from evidence rather than inferred from age alone. Business-value assessment asks who depends on the system, how it supports business processes, whether users can achieve their work without it, and whether its functionality is unique or available elsewhere. Technical assessment considers application quality, support software, hardware and supplier support, maintenance difficulty, documentation, dependability, and operational constraints. A supplier that no longer supports essential hardware or software can affect the environment assessment even when application code is sound.')
para('Sommerville identifies additional data that can inform technical quality: the accumulated number of change requests, the number of user interfaces, and the volume of data used by the system. More change requests can indicate structural degradation; numerous interfaces can increase inconsistency and redundancy; large data volumes can raise the chance of data inconsistency. These are indicators to investigate, not isolated verdicts. Portfolio decisions may also be affected by organizational and political factors, so an assessment should record both evidence and decision rationale.')

# 8. Software configuration management
p=doc.add_paragraph('8. Software Configuration Management',style='Heading 1')
para('Software Configuration Management (SCM) controls the identity and evolution of software artifacts as changes are proposed, approved, made, checked, and recorded. The chapter presents four core activities: configuration identification, configuration control, configuration auditing, and status accounting.')
p=doc.add_paragraph('8.1 Four SCM activities',style='Heading 2')
grid(['Activity','Purpose in the maintenance setting'],[
('Configuration identification','Identify configuration items and their versions so the objects being changed are known.'),
('Configuration control','Control proposed changes and incorporate approved changes in an orderly way.'),
('Configuration auditing','Check that the delivered configuration and its records correspond to the required and approved state.'),
('Status accounting','Record and report the current state and history of configuration items and changes.')],[1.7,5.1],8.2)
para('The activities work together. Identification establishes what is under control; change control governs what may be altered; auditing checks the resulting configuration; and status accounting preserves the information needed to determine what was changed and where it stands.')
para('The two assigned books partition the activities differently. The scanned course chapter names four activities—identification, control, auditing, and status accounting. Agarwal et al. present three principal activities: identification, control, and configuration accounting, with status accounting and configuration audit treated within configuration accounting. Both structures are retained as source-specific organizations; the three-part model is not substituted for the course’s four-part list.')
para('Agarwal et al. also summarize configuration management as a life-cycle discipline: identify the products likely to change, establish relationships among them, define how versions are distinguished, control imposed changes, and audit and report the changes made. Their discussion further attributes to IEEE a definition that includes identifying configuration items, controlling their changes through the life cycle, recording/reporting item and request status, and verifying item completeness and correctness. This emphasis connects the four course activities to the managed product record.')
p=doc.add_paragraph('8.2 Configuration items and records',style='Heading 2')
para('The source lists project plans, the Software Requirements Specification, Software Design Description, source-code listings, test plans, test procedures, test cases, user manuals, and related system records among the documents and products that may be placed under configuration management. Configuration information includes component identity, compiler and linker information, participating staff, and build date and time. These details help distinguish one built version from another and support the reconstruction or review of a released configuration.')
para('Agarwal et al. classify development objects as controlled, pre-controlled, and uncontrolled. Controlled objects already follow formal change procedures; pre-controlled objects are not yet controlled but are planned to enter control; uncontrolled objects are outside the control plan. Their examples of controllable objects include requirements and design documents, build tools such as compilers and linkers, source code for each module, test cases, and problem reports. The configuration-management plan identifies the objects placed under control.')
p=doc.add_paragraph('8.2.1 Baselines, reservation, and stable work',style='Heading 3')
para('The version-control example explains configuration control through a private working copy. A developer reserves or checks out a module, changes that copy, and restores it as the changed object; the configuration tool prevents a second simultaneous reservation of the same module until restoration. Once a controlled document is updated, the resulting state becomes a new baseline. This gives the team a stable reference while work proceeds and reduces collisions when one module is integrated with other components.')
figure(ASSET/'verified_figures'/'Aggarwal_Fig9_1_Config_Control.png','Figure 8.1. Baseline reservation and replacement in configuration control, Agarwal et al., Figure 9.1, printed p. 195.',4.8)
p=doc.add_paragraph('8.2.2 Status accounting and configuration audit',style='Heading 3')
para('Status accounting records the evolving state of configuration items and the activities performed on them. The four operational questions are: what happened, who did it, when it happened, and what else may be affected? A status entry is made when a software configuration item receives a new identity, when a change is approved and an engineering change order is issued, and when an audit is conducted. Reports connect the configuration items, change requests, engineering change orders, and resulting status.')
figure(ASSET/'verified_figures'/'Aggarwal_Fig9_2_Status_Accounting.png','Figure 8.2. Status-accounting relationships, Agarwal et al., Figure 9.2, printed p. 196.',4.7)
para('A configuration audit complements a technical review by checking whether the approved change was made as specified and whether extra changes entered; whether a formal technical review addressed correctness; whether the process and standards were followed; whether the configuration item marks the change and carries its date and author; whether SCM recording/reporting procedures were followed; and whether related items were updated. The audit examines the controlled product and its records together.')
grid(['Audit question','Evidence to check'],[
('Was the approved change implemented as specified?','Compare the change request/engineering change order with the modified item; identify additional modifications.'),
('Was technical correctness reviewed?','Check the formal technical review record.'),
('Were process and standards followed?','Review the applicable process and engineering-standard evidence.'),
('Is the change identified in the item?','Check change highlighting, date, author, and updated item attributes.'),
('Were SCM records maintained?','Check that the change was noted, recorded, and reported.'),
('Were related items updated?','Check dependent configuration items and associated documents.')],[2.1,4.7],8.0)
p=doc.add_paragraph('8.3 Versions: revisions and variations',style='Heading 2')
para('The chapter distinguishes revisions from variations. A revision represents a changed version in the product’s evolution; a variation represents a different form or configuration of the product. The distinction helps prevent a branch or platform-specific form from being confused with a later revision of one baseline. The record should make the identity and relationship of each managed form explicit.')
para('Agarwal et al. discuss versions and releases with a different emphasis. They use a version for a system instance that can differ in functionality, performance, fault repair, or target hardware/software configuration; closely related forms may be treated as variants. A release is a version distributed to customers, so internal development and test versions can outnumber released versions. In that account, major functionality/technology/platform change marks a version progression, while a bug fix or minor improvement can be a new release. These terms do not map one-to-one onto the scanned course chapter’s revision/variation distinction.')
figure(ASSET/'verified_figures'/'Aggarwal_Fig9_5_Version_Evolution_review.png','Figure 8.3. Example configuration-item evolution with revisions and branches, Agarwal et al., Figure 9.5, printed p. 199.',5.6)
para('The evolutionary graph begins at version 1.0, passes through smaller revisions, and then branches: one path makes a major change, while another maintains a parallel form. Later changes create further descendants. The graph conveys a lineage relationship among versions; it is not merely a list sorted by release date. A record should therefore preserve which baseline a new item derives from and which branch it continues.')
p=doc.add_paragraph('8.4 Change control and CCA',style='Heading 2')
para('A proposed change is submitted to a Change Control Authority (CCA) for review and disposition. When a change is approved, Quality Assurance revalidates the affected software and configuration management incorporates the approved result as a controlled version. The sequence separates a request from an authorized change and from the verified product configuration that is ultimately recorded.')
para('Agarwal et al. use the name Change Control Board (CCB) for a group that reviews a request in light of its project effect and expected benefit. The scanned course chapter names a Change Control Authority (CCA). The labels belong to their respective sources; this seminar uses CCA when describing the course form and records the CCB as the supporting text’s term rather than silently treating the names as identical organizational definitions.')
para('The chapter’s change-request form captures the information used to describe, assess, approve, implement, and close a request. The reproduced original contains 18 labeled fields. Its labels are retained in the figure itself so that students can inspect the source form rather than rely on an abbreviated paraphrase.')
figure(DIAG/'CH09_FIG14_Change_Request_Form.png','Figure 8.4. Change Request Form, course-text Figure 9.14, printed p. 485.',5.4)
para('The supporting change-control discussion frames the process through management questions that should remain answerable throughout a change: when it occurred, who made it, which components changed, whether it was correctly made, who authorized it, who was notified, who can cancel the request, who is responsible for it, and what priority it received. These questions make synchronization, identification, naming, authentication, authorization, routing, cancellation, delegation, and valuation visible as control concerns.')
p=doc.add_paragraph('8.5 Controlled change sequence',style='Heading 2')
numbered('Identify the affected configuration items and the baseline or version from which the request starts.')
numbered('Record the requested change using the change-request information and submit it for CCA review.')
numbered('Assess and approve, reject, or defer the change through the stated control authority.')
numbered('Implement an approved change and maintain the configuration records relevant to the new version.')
numbered('Have Quality Assurance revalidate the affected software before controlled incorporation.')
numbered('Record the resulting configuration and its status so the released version can be distinguished and traced.')
para('This sequence restates the source’s change-control relationships in operational order. It does not add an independent approval body or release gate beyond the CCA, QA, and configuration-management roles named in the chapter.')
figure(ASSET/'verified_figures'/'Aggarwal_Fig9_6_Config_Environment.png','Figure 8.5. Configuration-management environment from build through test and deployment, Agarwal et al., Figure 9.6, printed p. 201.',5.6)
para('The configuration-environment diagram connects a managed build to a test environment, a deployment-ready package, approval, and configuration-management support for deployment. It also returns completion status to the SCM environment. This makes release preparation part of the configuration record: a build becomes a package for deployment through a controlled testing and approval path.')

# 9. Documentation and maintenance tools
p=doc.add_paragraph('9. Software Documentation and Maintenance Tools',style='Heading 1')
para('Documentation is the written record associated with a software system. The chapter separates documentation intended to help users operate the system from documentation intended to describe the system itself and support development or maintenance. Keeping these audiences distinct helps clarify why a user guide and a design description serve different purposes.')
p=doc.add_paragraph('9.1 User documentation',style='Heading 2')
para('The course table identifies seven forms of user documentation:')
numbered('System overview.')
numbered('Installation guide.')
numbered('Beginner’s guide.')
numbered('Reference guide.')
numbered('Enhancement booklet.')
numbered('Quick-reference card.')
numbered('System-administration documentation.')
grid(['User document','Function described in the course table'],[
('System overview','Gives a general account of the system’s functions.'),
('Installation guide','Explains setup and configuration for local hardware and related software.'),
('Beginner’s guide','Introduces how to begin using the system.'),
('Reference guide','Provides in-depth descriptions of system facilities and how to use them.'),
('Enhancement booklet','Summarizes new features.'),
('Quick-reference card','Provides a concise factual lookup.'),
('System-administration documentation','Covers administration such as networking, security, and upgrades.')],[2.1,4.7],8.0)
para('Together, these materials address different user needs, from understanding the system and installing it to learning its basic use, consulting detailed reference information, finding a concise reminder, or administering the installation. They should not be collapsed into one generic “manual” when their purposes differ.')
p=doc.add_paragraph('9.2 System documentation',style='Heading 2')
para('The course table lists seven forms of system documentation:')
numbered('System rationale.')
numbered('Software Requirements Specification.')
numbered('Specification and design description.')
numbered('Implementation documentation.')
numbered('System test plan.')
numbered('Acceptance test plan.')
numbered('Data dictionaries.')
grid(['System document','Information it preserves'],[
('System rationale','The objectives of the system as a whole.'),
('Software Requirements Specification','The requirements agreed between the user and developer.'),
('Specification/design description','How requirements are implemented, how the system is decomposed into interacting program units, and the function of each unit.'),
('Implementation documentation','How detailed design is represented in the programming language and how program actions are explained.'),
('System test plan','How individual program units are tested and how the integrated system is tested.'),
('Acceptance test plan','The tests the system must pass before users accept it.'),
('Data dictionaries','Definitions of terms related to the software system.')],[2.1,4.7],7.9)
para('These artifacts preserve information about why the system exists, what it must do, how it is organized and implemented, how it is tested, and how its data are described. This information supports future understanding and change; its usefulness depends on being maintained as the system evolves.')
p=doc.add_paragraph('9.2.1 Documentation by operational audience',style='Heading 3')
para('Agarwal et al. also distinguish user manuals, operator manuals, and maintenance manuals. A user manual describes system behavior and use without detailing how that behavior is implemented. An operator manual explains operation and fault recovery. A maintenance manual carries the deeper technical record, including functional specification, design, source-code listing, test data, and test results. This audience-based grouping complements the course tables: it explains why different documentation sets should be provided to users, operators, and maintainers.')
p=doc.add_paragraph('9.3 Documentation as part of change',style='Heading 2')
para('Documentation participates in the maintenance models and controls already covered. Iterative Enhancement updates affected documents as the system changes; the Taute model places documentation before release; SCM identifies system documents as managed configuration items; and the legacy-code guidance calls for detailed maintenance records. These connections show that documentation is part of preserving a dependable system history, not a substitute for the program or its tests.')
p=doc.add_paragraph('9.3.1 Documentation policies for reengineering',style='Heading 3')
para('Pressman distinguishes documentation strategies by the condition and importance of the system. If a system is stable and close to retirement, extensive document recovery may not repay its cost. A document-when-touched policy adds or corrects material when a maintainer changes the associated program area. For a critical system, however, the minimum documentation necessary to understand and safely maintain essential functions should be made available. These policies make the cost of documentation explicit while recognizing that undocumented critical behavior creates operational risk.')
para('Documentation restructuring can range from reorganizing existing material to recovering missing descriptions from code. Its priority should depend on the documentation’s age, accuracy, usability, the system’s expected remaining life, and the effect of missing information on planned changes. A document that is formally complete but inconsistent with the current code may be less useful than a smaller, verified record attached to the changed components. The maintenance record should distinguish information recovered from artifacts from assumptions still requiring confirmation.')
p=doc.add_paragraph('9.3.2 Change record as a handover artifact',style='Heading 3')
para('A completed maintenance record should let a later maintainer reconstruct the change without relying on the memory of its author. It should connect the request to the product version, state the observed behavior and intended result, list affected modules and documents, identify the tests run, record unresolved risks, and point to the resulting baseline. When a temporary emergency correction is followed by a permanent change, both actions and their relationship should remain visible. This record supports handover across staff changes and makes subsequent impact analysis more reliable.')
p=doc.add_paragraph('9.4 Maintenance tools in the course scope',style='Heading 2')
para('The course names the reverse-engineering and program-support tools in Section 7, including restructurers, cross-referencers, static analyzers, text editors, Rigi, and ReFine. Maintenance also relies on the controlled records and tests described in the SCM and regression-testing sections. To keep the source’s scope clear, this seminar does not expand that list into a catalogue of tools or claim capabilities that the chapter does not attribute to its named examples.')
grid(['Need during maintenance','Course material connected to it'],[
('Locate program relationships','Cross-reference support and Rigi’s component/relationship views.'),
('Inspect code and properties','Text editors and static analyzers named in the reverse-engineering discussion.'),
('Improve program structure','Restructurers and the restructuring process.'),
('Browse and report on source information','ReFine’s browsing and report-generation role.'),
('Preserve a controlled product state','SCM identification, control, audit, status records, and version information.'),
('Check behavior after change','The retained and selected regression tests.')],[2.35,4.45],8.1)
p=doc.add_paragraph('9.5 Closing synthesis',style='Heading 2')
para('The Chapter 9 topics form a connected maintenance discipline. Organizations first distinguish why a change is needed, then understand the existing program, assess the proposal and its effects, choose an appropriate process, estimate effort, test for regression, and preserve the approved result through configuration control and documentation. Reverse engineering and reengineering help when the product’s structure or records no longer provide enough support for safe change. The models and tools serve different parts of this work; none removes the need to understand the system and verify the change.')
para('This seminar follows the predictive nine-cluster vocabulary currently available. The instructor’s official term list and lecture notes remain pending. When received, the headings and coverage should be reconciled to that list before the draft is treated as the confirmed seminar scope.')

# Closing source note, deliberately compact; no inline hyperlinks or repeated source callouts.
# Source scope is stated on the cover; detailed locators remain in the internal coverage plan.

# Table/caption behavior, avoid row splits and widow/orphan lines
for table in doc.tables:
    for row in table.rows:
        trPr=row._tr.get_or_add_trPr(); cant=OxmlElement('w:cantSplit'); trPr.append(cant)
# Set document metadata
props=doc.core_properties; props.title='Software Maintenance'; props.subject='Chapter 9 predictive vocabulary seminar'; props.author='Advanced Software Engineering seminar draft'; props.keywords='software maintenance, maintenance models, cost estimation, regression testing, reverse engineering, reengineering, configuration management, documentation'
OUT.parent.mkdir(parents=True,exist_ok=True); doc.save(OUT)
print(OUT)


