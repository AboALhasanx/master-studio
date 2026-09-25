# -*- coding: utf-8 -*-
"""Build bilingual EN-AR Cyber Security Week 01 study PDF via DOCX."""
from pathlib import Path
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsmap
from docx.oxml import OxmlElement

OUT_DIR = Path(r"G:\My Drive\Master-Studio\01_Semester_1\01_Cyber_Security\03_Study_Notes")
DOCX = OUT_DIR / "Week_01_Cybersecurity_Bilingual_EN_AR.docx"

NAVY = RGBColor(0x1E, 0x3A, 0x8A)
TEAL = RGBColor(0x0F, 0x76, 0x6E)
DARK = RGBColor(0x1F, 0x29, 0x37)
RED = RGBColor(0xB9, 0x1C, 0x1C)
GOLD = RGBColor(0x92, 0x40, 0x0E)
GRAY = RGBColor(0x4B, 0x55, 0x63)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

AR_FONT = "Arial"
EN_FONT = "Arial"


def set_run_font(run, size=11, bold=False, color=DARK, font=EN_FONT, italic=False):
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    r = run._element
    rPr = r.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn("w:ascii"), font)
    rFonts.set(qn("w:hAnsi"), font)
    rFonts.set(qn("w:cs"), font)
    rFonts.set(qn("w:eastAsia"), font)


def set_para_bidi(paragraph, rtl=True):
    p = paragraph._element
    pPr = p.get_or_add_pPr()
    # remove existing bidi
    for tag in ("w:bidi",):
        for el in pPr.findall(qn(tag)):
            pPr.remove(el)
    bidi = OxmlElement("w:bidi")
    bidi.set(qn("w:val"), "1" if rtl else "0")
    pPr.append(bidi)
    if rtl:
        paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    else:
        paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT


def set_cell_shading(cell, hex_color):
    tc = cell._tePr if hasattr(cell, "_tePr") else cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


def set_cell_bidi(cell):
    for p in cell.paragraphs:
        set_para_bidi(p, True)


def add_p(doc, text, size=11, bold=False, color=DARK, rtl=False, space_after=6, space_before=0, align=None, italic=False):
    p = doc.add_paragraph()
    run = p.add_run(text)
    set_run_font(run, size=size, bold=bold, color=color, font=AR_FONT if rtl else EN_FONT, italic=italic)
    if rtl:
        set_para_bidi(p, True)
    else:
        set_para_bidi(p, False)
    if align == "center":
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(space_before)
    pf.line_spacing = 1.15
    return p


def add_h(doc, en, ar=None, level=1):
    if level == 1:
        add_p(doc, en, size=16, bold=True, color=NAVY, space_before=12, space_after=4)
        if ar:
            add_p(doc, ar, size=14, bold=True, color=TEAL, rtl=True, space_after=8)
    elif level == 2:
        add_p(doc, en, size=13, bold=True, color=NAVY, space_before=10, space_after=3)
        if ar:
            add_p(doc, ar, size=12, bold=True, color=TEAL, rtl=True, space_after=6)
    else:
        add_p(doc, en, size=11.5, bold=True, color=DARK, space_before=8, space_after=2)
        if ar:
            add_p(doc, ar, size=11, bold=True, color=TEAL, rtl=True, space_after=4)


def add_bilingual_block(doc, en, ar):
    add_p(doc, en, size=10.5, color=DARK, space_after=2)
    add_p(doc, ar, size=10.5, color=GRAY, rtl=True, space_after=8)


def add_formula(doc, formula, ar_note=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(formula)
    set_run_font(run, size=12, bold=True, color=NAVY)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(4)
    if ar_note:
        add_p(doc, ar_note, size=10, color=GRAY, rtl=True, align="center", space_after=8)


def add_table(doc, headers, rows, col_widths=None, rtl_cols=None):
    """rtl_cols: set of column indices that should be RTL Arabic."""
    if rtl_cols is None:
        rtl_cols = set()
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # header
    for j, h in enumerate(headers):
        cell = table.rows[0].cells[j]
        cell.text = ""
        p = cell.paragraphs[0]
        run = p.add_run(h)
        set_run_font(run, size=9.5, bold=True, color=WHITE)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_cell_shading(cell, "1E3A8A")
    # body
    for i, row in enumerate(rows):
        bg = "F8FAFC" if i % 2 == 0 else "FFFFFF"
        for j, val in enumerate(row):
            cell = table.rows[i + 1].cells[j]
            cell.text = ""
            p = cell.paragraphs[0]
            run = p.add_run(str(val))
            is_rtl = j in rtl_cols
            set_run_font(run, size=9, color=DARK, font=AR_FONT)
            if is_rtl:
                set_para_bidi(p, True)
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            set_cell_shading(cell, bg)
    if col_widths:
        for row in table.rows:
            for j, w in enumerate(col_widths):
                row.cells[j].width = Cm(w)
    doc.add_paragraph()
    return table


def add_callout(doc, title_en, title_ar, body_en, body_ar):
    add_p(doc, f"■ {title_en}", size=11, bold=True, color=RED, space_before=8, space_after=2)
    add_p(doc, title_ar, size=11, bold=True, color=RED, rtl=True, space_after=4)
    add_p(doc, body_en, size=10.5, color=DARK, space_after=2)
    add_p(doc, body_ar, size=10.5, color=GRAY, rtl=True, space_after=8)


def main():
    doc = Document()
    # page setup
    for section in doc.sections:
        section.top_margin = Cm(1.6)
        section.bottom_margin = Cm(1.6)
        section.left_margin = Cm(1.8)
        section.right_margin = Cm(1.8)

    # ========== COVER ==========
    add_p(doc, "CYBER SECURITY — WEEK 01", size=22, bold=True, color=NAVY, align="center", space_before=40, space_after=6)
    add_p(doc, "الأمن السيبراني — الأسبوع الأول", size=18, bold=True, color=TEAL, rtl=True, align="center", space_after=12)
    add_p(doc, "Introduction to Cybersecurity — Chapters 1–6", size=14, bold=True, color=DARK, align="center", space_after=4)
    add_p(doc, "مقدمة في الأمن السيبراني — الفصول 1–6", size=13, color=GRAY, rtl=True, align="center", space_after=16)

    add_p(doc, "Instructor: Asst. Prof. Dr. Huda Lafta Majeed", size=11, color=DARK, align="center", space_after=2)
    add_p(doc, "الدكتورة هدى لفطة مجيد — مقررة قسم الدراسات العليا", size=11, color=GRAY, rtl=True, align="center", space_after=10)
    add_p(doc, "Bilingual Study Reference (English + Arabic) — Full, Not Compressed", size=11, bold=True, color=NAVY, align="center", space_after=2)
    add_p(doc, "ملف مراجعة ثنائي اللغة (إنكليزي + عربي) — كامل بلا اختصار", size=11, bold=True, color=TEAL, rtl=True, align="center", space_after=10)
    add_p(doc, "Quiz: Sunday 2026-09-20 · 08:30 · Written/essay · ~10 min · Soft stakes", size=10, color=RED, align="center", space_after=2)
    add_p(doc, "الامتحان اليومي: الأحد 2026-09-20 · 08:30 · مقالي · ~10 دقائق · درجة خفيفة", size=10, color=RED, rtl=True, align="center", space_after=8)
    add_p(doc, "Built from vault notes + question bank + doctor method map · Koko 2026-09-19", size=9, color=GRAY, align="center", space_after=4)
    add_p(doc, "Chapter 7 (Case Studies) EXCLUDED by the doctor — do not study it.", size=10, bold=True, color=RED, align="center", space_after=2)
    add_p(doc, "الفصل السابع (دراسات الحالة) خارج الامتحان — الدكتورة استثناته.", size=10, bold=True, color=RED, rtl=True, align="center", space_after=16)

    # ========== EXAM METHOD ==========
    add_h(doc, "0. Exam Method — Dr. Huda (Confirmed)", "صفر. أسلوب الامتحان — د. هدى (مؤكد)")
    add_bilingual_block(
        doc,
        "Two question types only. If numbers are given → apply the formula. If no numbers → analytical scenario: step → CIA pillar → (techniques in parentheses). The parentheses are mandatory. Both deep step-by-step answers and whole-scenario answers are accepted. Daily quiz is written/essay, ~10 minutes, soft stakes (reading compliance).",
        "نمطان فقط للسؤال. إذا جاب أرقام → طبّق المعادلة. إذا ما بيه أرقام → سيناريو تحليلي: خطوة ← ركن CIA ← (التقنيات بالقوس). القوس إلزامي. تُقبل إجابة خطوة بخطوة أو تحليل السيناريو ككل. الامتحان اليومي مقالي ~10 دقائق، ودرجته خفيفة (يتأكد إنك قريت)."
    )
    add_table(
        doc,
        ["If the question…", "Then you…", "بالعربي"],
        [
            ["has numbers", "write formula → substitute → compute → interpret in one line", "بيه أرقام: معادلة ← تعويض ← حساب ← تفسير"],
            ["has no numbers (scenario)", "number events → CIA pillar each step → techniques in parentheses", "سيناريو: رقّم الأحداث ← ركن CIA ← (تقنيات)"],
        ],
        rtl_cols={2},
    )

    add_callout(
        doc,
        "Dr. Huda's rule on min R (record verbatim)",
        "قاعدة الدكتورة على min R (سجّلها كما هي)",
        "\"If the result is above 100, there is investment; if below 100, there is no investment.\" She is Head of Postgraduate Studies — her statements are the reference.",
        "«إذا الناتج ازداد عن الـ100 يعني اكو استثمار، وإذا أقل من 100 يعني مفيش استثمار». هي مقررة قسم الدراسات العليا — كلامها هو المرجع، لا تناقشه.",
    )

    # ========== CH1 ==========
    add_h(doc, "1. Cybersecurity — Definition, Scope, Evolution, Importance", "1. الأمن السيبراني — التعريف، النطاق، التطور، الأهمية")
    add_h(doc, "1.1 Definition", "1.1 التعريف", level=2)
    add_bilingual_block(
        doc,
        "Cybersecurity is the protection of systems, networks, applications, and data from cyber threats, unauthorized access, and harm. It covers technical, legal, managerial, and social aspects.",
        "الأمن السيبراني هو حماية الأنظمة والشبكات والتطبيقات والبيانات من التهديدات الإلكترونية والوصول غير المصرّح به والضرر. يشمل جوانب تقنية + قانونية + إدارية + اجتماعية.",
    )
    add_h(doc, "1.2 Scope", "1.2 النطاق", level=2)
    add_bilingual_block(
        doc,
        "From personal devices → enterprise systems → national critical infrastructure.",
        "من الأجهزة الشخصية ← أنظمة المؤسسات ← البنية التحتية الوطنية الحرجة.",
    )
    add_h(doc, "1.3 Historical Evolution", "1.3 التطور التاريخي", level=2)
    add_table(
        doc,
        ["Period", "Stage (EN)", "المرحلة (عربي)"],
        [
            ["1960s", "First mentions with ARPANET and early mainframes", "أول ذِكر مع ARPANET وأجهزة الـ mainframe"],
            ["1980s–90s", "Viruses, worms, and antivirus appear", "ظهور الفيروسات والديدان ومضادات الفيروسات"],
            ["2000s", "Becomes core to e-commerce and banking", "الأمن السيبراني يصير جزء أساسي من التجارة الإلكترونية والمصرفية"],
            ["2010s–now", "APT · Ransomware · IoT · AI · Zero Trust", "APT · Ransomware · IoT · الذكاء الاصطناعي · Zero Trust"],
        ],
        rtl_cols={2},
    )
    add_callout(
        doc,
        "TRAP: ARPANET date",
        "فخ: تاريخ ARPANET",
        "ARPANET and mainframes = 1960s — NOT 1980s. You wrote 1980s once; the lecture material says 1960s.",
        "ARPANET والـ mainframes = ستينيات 1960s — مو ثمانينيات. المادة حرفياً: 1960s.",
    )

    add_h(doc, "1.4 Importance", "1.4 الأهمية", level=2)
    add_bilingual_block(
        doc,
        "Directly linked to national security, economic stability, and privacy protection.",
        "مرتبط مباشرة بالأمن الوطني · الاستقرار الاقتصادي · حماية الخصوصية.",
    )

    add_h(doc, "1.5 Formula — Cybersecurity as Optimization", "1.5 المعادلة — السايبر كمشكلة تحسين", level=2)
    add_formula(doc, "min R = Σ P_i · I_i − Σ C_j", "تقليل الخطر = مجموع (احتمال × تأثير) − مجموع الاستثمار الأمني")
    add_table(
        doc,
        ["Symbol", "Meaning", "المعنى"],
        [
            ["P_i", "Probability of threat i", "احتمال حصول التهديد i"],
            ["I_i", "Impact of threat i", "تأثير التهديد i"],
            ["C_j", "Investment in security control j", "الاستثمار في ضابط الأمان j"],
        ],
        rtl_cols={2},
    )
    add_bilingual_block(
        doc,
        "Idea: minimize risk while maximizing security investment value — not \"add more security blindly\"; you must balance cost and risk.",
        "الفكرة: تقليل الخطر مع موازنة الاستثمار الأمني — مو «زيد حماية وخلاص»؛ لازم توازن.",
    )
    add_callout(
        doc,
        "Worked example (numbers)",
        "مثال محلول (أرقام)",
        "P1=0.4, I1=200; P2=0.3, I2=100; ΣC=5. Then ΣP·I = 80+30=110; min R = 110−5 = 105. 105 > 100 → there IS investment (doctor's rule).",
        "P1=0.4, I1=200؛ P2=0.3, I2=100؛ مجموع C=5. إذن مجموع P·I = 80+30=110؛ min R = 110−5 = 105. بما أن 105 > 100 ← اكو استثمار حسب قاعدة الدكتورة.",
    )
    add_callout(
        doc,
        "TRAP: arithmetic + symbol",
        "فخ: الحساب والرمز",
        "0.3×100 = 30 (not 90). P = Probability (not Portability). Check arithmetic twice.",
        "0.3×100 = 30 مو 90. P = Probability (الاحتمال) مو Portability. راجع الحساب مرتين.",
    )

    # ========== CH2 ==========
    add_h(doc, "2. Importance, Levels, Domains, R(t)", "2. الأهمية، المستويات، المجالات، R(t)")
    add_h(doc, "2.1 Four Levels Protected", "2.1 المستويات الأربعة المحمية", level=2)
    add_table(
        doc,
        ["Level", "What it protects", "شنو يحمي"],
        [
            ["Individuals", "Personal devices · email · social media · bank data", "الأجهزة الشخصية · الإيميل · السوشيال · بيانات المصرف"],
            ["Enterprises", "Business continuity · customer trust · legal compliance", "استمرارية العمل · ثقة العملاء · الامتثال القانوني"],
            ["Governments", "National security · defense · e-government infrastructure", "الأمن الوطني · الدفاع · بنية الحكومة الإلكترونية"],
            ["Global Trade", "Cross-border digital trade · financial systems", "التجارة الرقمية عبر الحدود · الأنظمة المالية"],
        ],
        rtl_cols={2},
    )
    add_callout(
        doc,
        "Do NOT mix the two \"fours\"",
        "لا تخلط بين «الأربعات»",
        "Chapter 1 aspects = technical · legal · managerial · social. Chapter 2 levels = individuals · enterprises · governments · global trade.",
        "جوانب الفصل الأول = تقنية · قانونية · إدارية · اجتماعية. مستويات الفصل الثاني = أفراد · مؤسسات · حكومات · تجارة عالمية.",
    )

    add_h(doc, "2.2 Six Core Domains (list is expandable)", "2.2 المجالات الستة (القائمة قابلة للزيادة)", level=2)
    add_table(
        doc,
        ["#", "Domain", "Techniques / tools", "الأدوات"],
        [
            ["1", "Network Security", "firewalls · IDS/IPS", "جدران نارية · IDS/IPS"],
            ["2", "Application Security", "secure coding · OWASP", "برمجة آمنة · معايير OWASP"],
            ["3", "Cloud Security", "encryption · IAM · virtualization", "تشفير · IAM · افتراضية"],
            ["4", "IoT Security", "lightweight encryption · anomaly detection", "تشفير خفيف · كشف الشذوذ"],
            ["5", "Mobile Security", "sandboxing · malware detection", "عزل · كشف البرمجيات الخبيثة"],
            ["6", "ICS Security", "industrial control system protection", "حماية أنظمة التحكم الصناعي"],
        ],
        rtl_cols={3},
    )
    add_callout(
        doc,
        "TRAP: incomplete lists",
        "فخ: قوائم ناقصة",
        "Lecture lists IDS/IPS (not IDS only), OWASP under Application, IAM under Cloud. Your note: the number of cyber domains can grow (AI Security, Supply-Chain Security, Zero Trust…).",
        "المادة تكتب IDS/IPS (مو IDS فقط)، و OWASP تحت Application، و IAM تحت Cloud. ملاحظتك: عدد المجالات قابل للزيادة (AI Security · Supply-Chain · Zero Trust…).",
    )

    add_h(doc, "2.3 Formula — Risk Exposure R(t)", "2.3 المعادلة — التعرّض للخطر R(t)", level=2)
    add_formula(doc, "R(t) = Σ P_i(t) · I_i(t)", "الخطر المتوقع عند الزمن t = مجموع (احتمال × تأثير) لكل التهديدات")
    add_bilingual_block(
        doc,
        "Expected risk at time t, summed over threats. Doctor's stance: awareness only — \"we just know this law is used here.\" Do not over-invest memorization time.",
        "الخطر المتوقع عند زمن t، مجموع على كل التهديدات. موقف الدكتورة: وعي سطحي فقط — «بس نعرف هذا القانون هنا يستخدم». لا تصرف وقت حفظ زايد عليها.",
    )

    # ========== CH3 CIA ==========
    add_h(doc, "3. CIA Triad — MOST IMPORTANT", "3. ثالوث CIA — الأهم بالوحدة")
    add_bilingual_block(
        doc,
        "CIA is the vocabulary you write inside parentheses in every scenario answer. Without it, the answer is incomplete.",
        "ثاثوث CIA هو المفردات اللي تكتبها بالقوس بكل جواب سيناريو. بدونها الجواب ناقص.",
    )
    add_h(doc, "3.1 Mandatory Memory Table", "3.1 جدول الحفظ الإلزامي", level=2)
    add_table(
        doc,
        ["Pillar", "Definition (EN)", "Techniques (parentheses)", "التعريف (عربي)"],
        [
            ["Confidentiality", "Prevent unauthorized access to data", "encryption · access controls · VPNs", "منع الوصول غير المصرّح به للبيانات"],
            ["Integrity", "Ensure data is accurate and unaltered", "hashing (SHA-256) · digital signatures · version control", "ضمان دقة البيانات وعدم تعديلها"],
            ["Availability", "Ensure resources available when needed", "redundancy · load balancing · DDoS mitigation", "ضمان توفر الموارد وقت الحاجة"],
        ],
        rtl_cols={3},
    )
    add_callout(
        doc,
        "TRAP: Integrity vs Integration · Firewall location",
        "فخ: Integrity مو Integration · وين يندرج Firewall",
        "Write Integrity (not Integration — that is a different word). Firewall belongs under Network Security domains, not inside the CIA-Confidentiality technique list.",
        "اكتب Integrity مو Integration (Integration كلمة ثانية تماماً). الـ Firewall يندرج تحت مجال Network Security، مو داخل قائمة تقنيات CIA-Confidentiality.",
    )

    add_h(doc, "3.2 Formula — Security Utility Function", "3.2 المعادلة — دالة المنفعة الأمنية", level=2)
    add_formula(doc, "U(C, I, A) = α·C + β·I + γ·A", "المنفعة = وزن السرّية + وزن السلامة + وزن التوفر")
    add_table(
        doc,
        ["Symbol", "Meaning", "المعنى"],
        [
            ["C, I, A", "Normalized values in [0,1] for Confidentiality, Integrity, Availability", "قيم منظّمة 0–1 للسرّية والسلامة والتوفر"],
            ["α, β, γ", "Importance weights for a specific system (typically sum to 1)", "أوزان الأهمية لنظام معيّن (عادةً مجموعها 1)"],
        ],
        rtl_cols={2},
    )
    add_bilingual_block(
        doc,
        "Weights are NOT fixed. They change by domain. Doctor (red ink): \"In healthcare, confidentiality (α) has higher weight than availability.\"",
        "الأوزان مو ثابتة — تتغير حسب المجال. الدكتورة (بالأحمر): «In healthcare, confidentiality (α) has higher weight than availability.»",
    )
    add_table(
        doc,
        ["Domain", "Heaviest pillar", "Why", "ليش"],
        [
            ["Healthcare", "Confidentiality (α)", "Patient records — privacy first", "سجلات المرضى — الخصوصية أولاً"],
            ["Banking", "Integrity (β)", "Changed account number/balance = catastrophe", "تغيير رقم حساب أو رصيد = كارثة"],
            ["Emergency services", "Availability (γ)", "System must stay up always", "النظام لازم يشتغل دائماً"],
        ],
        rtl_cols={3},
    )
    add_callout(
        doc,
        "TRAP: banking weights",
        "فخ: أوزان المصرف",
        "For a bank, Integrity (β) is HEAVY, not light. You once argued β was \"not that much important\" while citing account-number integrity — that contradicts itself.",
        "بالمصرف، Integrity (β) ثقيل مو خفيف. مرة قلت β «مو مهم لهالدرجة» وبنفس الوقت تحكي عن عدم تعديل رقم الحساب — هذا تناقض. β هو الركن الأثقل للمصرف.",
    )
    add_callout(
        doc,
        "Worked example — U(C,I,A)",
        "مثال محلول — U(C,I,A)",
        "α=0.5, β=0.3, γ=0.2; C=0.9, I=0.7, A=0.8. Then 0.45+0.21+0.16 = 0.82. Check: 0.82 is in [0,1] → valid.",
        "α=0.5, β=0.3, γ=0.2؛ C=0.9, I=0.7, A=0.8. إذن 0.45+0.21+0.16 = 0.82. الفحص: 0.82 بين 0 و1 → الجواب سليم.",
    )

    # ========== CH4 ==========
    add_h(doc, "4. Threat Landscape + Attack Surface AS", "4. مشهد التهديدات + سطح الهجوم AS")
    add_h(doc, "4.1 Five Threat Types", "4.1 أنواع التهديدات الخمسة", level=2)
    add_table(
        doc,
        ["Type", "Description (EN)", "Examples", "الوصف (عربي)"],
        [
            ["Malware", "Malicious software", "Viruses · Worms · Trojans · Ransomware", "برمجيات خبيثة: فيروسات · ديدان · طروادة · فدية"],
            ["Phishing & Social Engineering", "Exploit human trust", "spear phishing · BEC", "استغلال الثقة البشرية"],
            ["Insider Threats", "Staff misuse privileges", "data leak from inside", "موظفون يسيئون استخدام صلاحياتهم"],
            ["APTs", "State-backed · stealthy · long-term", "Advanced Persistent Threats", "مدعومة من دول · خفية · طويلة المدى"],
            ["IoT Attacks", "Compromise internet-connected devices", "Botnets — e.g. Mirai", "استغلال أجهزة إنترنت الأشياء — مثال Mirai"],
        ],
        rtl_cols={3},
    )
    add_h(doc, "4.2 Trends 2023–2024", "4.2 اتجاهات 2023–2024", level=2)
    add_bilingual_block(
        doc,
        "(1) Ransomware damages exceed $20 billion. (2) Cloud attacks rise due to misconfigurations. (3) AI-powered attacks grow.",
        "(1) أضرار الـ Ransomware تتجاوز 20 مليار دولار. (2) هجمات السحابة ترتفع بسبب الأخطاء الإعدادية misconfigurations. (3) هجمات مدعومة بالذكاء الاصطناعي تنمو.",
    )

    add_h(doc, "4.3 Formula — Attack Surface", "4.3 المعادلة — سطح الهجوم", level=2)
    add_formula(doc, "AS = Σ ( E_j · V_j · A_j )", "سطح الهجوم = مجموع (نقاط الدخول × شدة الثغرة × قيمة الأصل) لكل مكوّن")
    add_table(
        doc,
        ["Symbol", "Meaning", "Range / source", "المعنى"],
        [
            ["E_j", "Exposed entry points for component j", "count 0,1,2,…", "عدد نقاط الدخول المكشوفة"],
            ["V_j", "Vulnerability severity", "CVSS 0.0–10.0", "شدة الثغرة (CVSS)"],
            ["A_j", "Asset value of component j", "money/ops value", "قيمة الأصل"],
        ],
        rtl_cols={3},
    )
    add_bilingual_block(
        doc,
        "Why multiply (not add)? All three must exist for real risk: if E=0 no one reaches it; if V=0 it is hardened; if A=0 it is not worth attacking. Any factor = 0 → AS contribution = 0.",
        "ليش ضرب مو جمع؟ الثلاثة لازم يتوفرون سوا حتى يصير خطر حقيقي: إذا E=0 ما يوصله أحد؛ إذا V=0 النظام محصّن؛ إذا A=0 ما يستاهل ينخترق. أي عامل = صفر ← مساهمة AS = صفر.",
    )
    add_callout(
        doc,
        "Worked example + control lever",
        "مثال محلول + رافعة التحكم",
        "Component 1: E=3,V=8,A=100 → 2400. Component 2: E=2,V=5,A=300 → 3000. AS = 5400. Best lever to reduce AS: lower E (close unused ports, segmentation) — easiest/cheapest. V needs patching; A rarely changes.",
        "مكوّن 1: 3×8×100=2400. مكوّن 2: 2×5×300=3000. AS=5400. أقوى رافعة لتقليل AS: قلّل E (إغلاق بورتات غير مستخدمة · segmentation) — أسهل وأرخص. V يحتاج تحديث؛ A نادراً ما يتغير.",
    )

    # ========== CH5 ==========
    add_h(doc, "5. Risk, Vulnerabilities, Exploits + P(R>r)", "5. المخاطر والثغرات والاستغلالات + P(R>r)")
    add_table(
        doc,
        ["Concept", "Definition (EN)", "Example", "التعريف (عربي)"],
        [
            ["Risk", "Function of Probability × Impact", "30% breach chance × $1M loss", "دالة (احتمال × تأثير)"],
            ["Vulnerability", "Software/hardware/human weakness", "OWASP Top 10 · CVEs", "نقطة ضعف برمجية/عتادية/بشرية"],
            ["Exploit", "Tool/technique that uses the vulnerability", "Metasploit · ready script", "أداة/طريقة تستغل الثغرة"],
        ],
        rtl_cols={3},
    )
    add_bilingual_block(
        doc,
        "Relation: vulnerability + exploit = risk (when probability and impact are high). House metaphor: broken window = vulnerability; how the thief enters = exploit; chance × value stolen = risk.",
        "العلاقة: ثغرة + أداة استغلال = خطر (إذا الاحتمال والتأثير عاليين). تشبيه البيت: نافذة مكسورة = ثغرة · طريقة دخول الحرامي = استغلال · احتمال الدخول × قيمة المسروق = خطر.",
    )
    add_table(
        doc,
        ["Model", "Expansion", "What it does", "شنو يسوي"],
        [
            ["OCTAVE", "Operationally Critical Threat, Asset, and Vulnerability Evaluation", "Operational critical threat/asset/vuln evaluation", "يقيّم تهديدات وأصول وثغرات حرجة تشغيلياً"],
            ["FAIR", "Factor Analysis of Information Risk", "Quantitative factor analysis of info risk", "تحليل عوامل خطر المعلومات (كمّي)"],
            ["NIST RMF", "NIST Risk Management Framework", "US government risk management framework", "إطار إدارة مخاطر حكومي أمريكي"],
        ],
        rtl_cols={3},
    )

    add_h(doc, "5.2 Formula — Tail Probability", "5.2 المعادلة — احتمال الذيل", level=2)
    add_formula(doc, "P(R > r) = 1 − F(r)", "احتمال تجاوز الخطر للحد r = 1 − دالة التوزيع التراكمي")
    add_bilingual_block(
        doc,
        "F(r) = CDF = P(R ≤ r) — probability that risk is at most r. F(r) is always in [0,1] because it is a probability (your lecture note — correct). 1−F(r) is the probability that risk EXCEEDS r (the catastrophe tail).",
        "F(r) = دالة توزيع تراكمي = احتمال إن الخطر ≤ r. مجالها دائماً 0–1 لأنها احتمال (ملاحظتك بالمحاضرة — صحيحة). و 1−F(r) = احتمال إن الخطر يتجاوز r (ذيل الكارثة).",
    )
    add_callout(
        doc,
        "Worked example",
        "مثال محلول",
        "r = $10,000; F(10,000)=0.92 → P(R>r)=1−0.92=0.08 → 8% chance loss exceeds the accepted limit.",
        "r = 10,000$؛ F=0.92 ← P(R>r)=1−0.92=0.08 ← احتمال 8% إن الخسارة تتجاوز الحد المقبول.",
    )

    # ========== CH6 ==========
    add_h(doc, "6. Evolution, Policies, Compliance PCI", "6. التطور، السياسات، مؤشر الامتثال PCI")
    add_table(
        doc,
        ["Phase", "Period", "Focus", "التركيز"],
        [
            ["Early Cybersecurity", "1960s–1990s", "Perimeter defense — firewalls · antivirus", "دفاع محيطي — جدران نارية · مضادات فيروسات"],
            ["Modern Cybersecurity", "2000s–now", "Cloud · IoT · Mobile · AI-driven attacks", "سحابة · IoT · موبايل · هجمات مدعومة بالذكاء الاصطناعي"],
        ],
        rtl_cols={3},
    )
    add_bilingual_block(
        doc,
        "Perimeter defense = fortify the border. Modern systems have blurred borders (cloud, mobile), so defense must be internal and distributed.",
        "الدفاع المحيطي = تحصين الحدود. الأنظمة الحديثة حدودها غير واضحة (سحابة · موبايل)، فالdefense لازم يكون داخلي وموزّع.",
    )
    add_table(
        doc,
        ["Framework", "Body", "Covers", "جهة/تغطية"],
        [
            ["GDPR", "European Union", "Data protection & privacy", "الاتحاد الأوروبي · حماية البيانات والخصوصية"],
            ["HIPAA", "United States", "Healthcare information protection", "أمريكا · حماية معلومات الرعاية الصحية"],
            ["NIST / ISO 27001", "International", "International standards", "دولية · معايير دولية"],
        ],
        rtl_cols={3},
    )
    add_table(
        doc,
        ["Region", "Tools / frameworks", "الأدوات"],
        [
            ["US", "NIST CSF · Federal Cybersecurity Strategy", "NIST CSF · استراتيجية فيدرالية"],
            ["EU", "GDPR · ENISA", "GDPR · ENISA"],
            ["Middle East", "National Cybersecurity Councils", "المجالس الوطنية للأمن السيبراني"],
        ],
        rtl_cols={2},
    )

    add_h(doc, "6.3 Formula — Policy Compliance Index", "6.3 المعادلة — مؤشر الامتثال للسياسات", level=2)
    add_formula(doc, "PCI = ( Σ w_k · c_k ) / ( Σ w_k )", "مؤشر الامتثال = متوسط موزون = مجموع (الوزن × الامتثال) ÷ مجموع الأوزان")
    add_table(
        doc,
        ["Symbol", "Meaning", "Range", "المعنى"],
        [
            ["c_k", "Compliance level of requirement k", "0–1", "مستوى الامتثال للمتطلب k"],
            ["w_k", "Importance weight of requirement k", "positive", "وزن أهمية المتطلب k"],
            ["Σ w_k", "Denominator — sum of weights (NOT n)", "positive", "المقام — مجموع الأوزان مو عدد المتطلبات"],
        ],
        rtl_cols={3},
    )
    add_callout(
        doc,
        "Worked example — PCI",
        "مثال محلول — PCI",
        "Requirements: (w=3,c=1.0), (w=2,c=0.5), (w=1,c=0.0). Numerator = 3.0+1.0+0.0=4.0; denominator=6; PCI=4/6=0.667 → 66.7% compliance. Divide by Σw, never by n alone.",
        "متطلبات: (3,1.0) و(2,0.5) و(1,0.0). البسط=3.0+1.0+0.0=4.0؛ المقام=6؛ PCI=4/6=0.667 ← 66.7% امتثال. القسمة على مجموع الأوزان مو على عدد المتطلبات n.",
    )

    # ========== CH7 excluded ==========
    add_h(doc, "7. Case Studies — OUT OF EXAM", "7. دراسات الحالة — خارج الامتحان")
    add_bilingual_block(
        doc,
        "Stuxnet · Colonial Pipeline · GDPR Enforcement — the doctor explicitly excluded this chapter. Do not spend time on it.",
        "Stuxnet · Colonial Pipeline · GDPR Enforcement — الدكتورة استثنت هذا الفصل صراحة. لا تضيّع وقتك عليه.",
    )

    # ========== SCENARIO RECIPE ==========
    add_h(doc, "8. Scenario Answer Recipe", "8. وصفة الإجابة على السيناريو")
    add_bilingual_block(
        doc,
        "Step 1: Number the events in order. Step 2: For each event ask ONE question — what was harmed? Data exposed → Confidentiality. Data altered → Integrity. System down/unavailable → Availability. Step 3: Write the pillar name + techniques in parentheses from the mandatory CIA table.",
        "الخطوة 1: رقّم الأحداث بالترتيب. الخطوة 2: لكل حدث اسأل سؤالاً واحداً — شنو تضرر؟ بيانات انكشفت ← Confidentiality. بيانات تغيّرت ← Integrity. النظام توقف ← Availability. الخطوة 3: اكتب اسم الركن + التقنيات من جدول CIA الإلزامي بالقوس.",
    )
    add_bilingual_block(
        doc,
        "Accepted: deep step-by-step OR whole-scenario analysis. Not accepted: answer without a CIA pillar, or a pillar without parentheses.",
        "المقبول: تحليل عميق خطوة بخطوة أو تحليل السيناريو ككل. غير المقبول: جواب بلا ركن CIA، أو ركن بلا قوس تقنيات.",
    )

    add_h(doc, "8.1 Practice Scenarios (from vault notes)", "8.1 سيناريوهات تدريبية (من الملاحظات)", level=2)

    add_h(doc, "Scenario 1 — Bank account drop", "سيناريو 1 — نقص رصيد مصرف", level=3)
    add_bilingual_block(
        doc,
        "Customer sees $100,000 missing from the bank account. Manager investigates; cause was a software bug; fixed and amount restored.",
        "عميل بمصرف شاف حسابه نقص 100,000 دولار مرة واحدة. المدير حقّق؛ السبب خلل برنامجي؛ انصلّح ورجع المبلغ.",
    )
    add_table(
        doc,
        ["Step", "What happened", "Pillar", "(Techniques)", "الحدث"],
        [
            ["1", "Customer data changed unexpectedly", "Integrity", "(hashing SHA-256, digital signatures, version control)", "بيانات العميل تغيّرت"],
            ["2", "System issue discovered / service impact", "Availability", "(redundancy, load balancing, DDoS mitigation)", "مشكلة بالنظام / أثر على الخدمة"],
            ["3", "Bug fixed; amount restored", "—", "incident resolved", "انصلّح ورجع المبلغ"],
        ],
        rtl_cols={4},
    )

    add_h(doc, "Scenario 2 — Hospital old account", "سيناريو 2 — مستشفى وحساب قديم", level=3)
    add_bilingual_block(
        doc,
        "Hospital patient records appear to unauthorized users from another department. Investigation: an old employee account is still active.",
        "مستشفى — سجلات المرضى تظهر لمستخدم غير مصرّح له من قسم آخر. التحقيق: حساب موظف قديم لا زال فعّالاً.",
    )
    add_table(
        doc,
        ["Step", "What happened", "Pillar", "(Techniques)", "الحدث"],
        [
            ["1", "Patient data exposed to unauthorized users", "Confidentiality", "(encryption, access controls, VPNs)", "بيانات المرضى انكشفت لغير المصرّح"],
            ["2", "Root cause: old account not disabled", "Access-control failure", "(access controls + periodic account review)", "حساب قديم ما انعطّل"],
            ["3", "Fix: disable account + audit privileges", "—", "remediation", "تعطيل + تدقيق صلاحيات"],
        ],
        rtl_cols={4},
    )

    add_h(doc, "Scenario 3 — University registration outage", "سيناريو 3 — وقوع نظام تسجيل الجامعة", level=3)
    add_bilingual_block(
        doc,
        "University registration system falls during registration week; thousands of students cannot register.",
        "نظام التسجيل بالجامعة وقع بوقت التسجيل؛ آلاف الطلاب ما قدروا يسجّلوا.",
    )
    add_table(
        doc,
        ["Step", "What happened", "Pillar", "(Techniques)", "الحدث"],
        [
            ["1", "System unavailable when needed", "Availability", "(redundancy, load balancing, DDoS mitigation)", "النظام ما كان متاح وقت الحاجة"],
            ["2", "Possible DDoS if attack-induced", "Availability", "(DDoS mitigation)", "احتمال DDoS"],
            ["3", "Long-term fix", "Availability", "(redundancy + load balancing)", "سيرفرات احتياطية + توزيع حمل"],
        ],
        rtl_cols={4},
    )

    add_h(doc, "Scenario 4 — E-commerce price change", "سيناريو 4 — تغير سعر متجر إلكتروني", level=3)
    add_bilingual_block(
        doc,
        "Customer notices the product price on the invoice changed after order confirmation.",
        "عميل لاحظ إن سعر المنتج بالفاتورة تغيّر بعد تأكيد الطلب.",
    )
    add_table(
        doc,
        ["Step", "What happened", "Pillar", "(Techniques)", "الحدث"],
        [
            ["1", "Data changed after confirmation", "Integrity", "(hashing SHA-256, digital signatures, version control)", "البيانات تغيّرت بعد التأكيد"],
            ["2", "version control shows who/when changed price", "Integrity", "(version control)", "version control يبيّن من غيّر"],
            ["3", "If system fault caused it", "Availability", "(system not operating correctly)", "لو السبب خلل بالنظام"],
        ],
        rtl_cols={4},
    )

    add_h(doc, "Scenario 5 — Million-dollar spend still breached", "سيناريو 5 — ملايين على الأمن ومع ذلك اختراق", level=3)
    add_bilingual_block(
        doc,
        "Company spent heavily on security tools; systems slow then fully down; CEO says \"we spent millions, they cannot hack us.\"",
        "شركة صارفة ملايين على الأدوات الأمنية؛ الأنظمة بطيئة ثم توقفت؛ المدير قال مستحيل يخترقونا.",
    )
    add_table(
        doc,
        ["Step", "What happened", "Pillar / factor", "(Techniques)", "الحدث"],
        [
            ["1", "Systems degraded then down", "Availability", "(redundancy, load balancing, DDoS mitigation)", "بطء ثم توقف"],
            ["2", "High spend ≠ low risk if misallocated", "Risk management", "(risk assessment before purchase)", "استثمار كبير مو بالضرورة خطر صغير"],
            ["3", "Reply to CEO: ΣC large does not force ΣP·I small", "min R logic", "(align spend to real threats)", "المال بدون تقييم مخاطر ما يحمي"],
        ],
        rtl_cols={4},
    )

    # ========== FORMULA SUMMARY ==========
    add_h(doc, "9. All Six Formulas — Quick Sheet", "9. المعادلات الست — ورقة سريعة")
    add_table(
        doc,
        ["#", "Formula", "When to use", "متى تستعملها"],
        [
            ["1", "min R = Σ P_i I_i − Σ C_j", "Numbers given; threshold >100 = investment (doctor)", "أرقام معطاة؛ >100 = اكو استثمار (قاعدة الدكتورة)"],
            ["2", "R(t) = Σ P_i(t) I_i(t)", "Awareness only — risk at time t", "وعي سطحي — خطر عند زمن t"],
            ["3", "U(C,I,A) = αC + βI + γA", "Numbers; weights by domain; result in [0,1]", "أرقام؛ أوزان حسب المجال؛ الناتج 0–1"],
            ["4", "AS = Σ E_j V_j A_j", "Numbers; E count, V CVSS 0–10, A asset value", "أرقام؛ E عدد · V CVSS · A قيمة أصل"],
            ["5", "P(R>r) = 1 − F(r)", "Numbers; F in [0,1]; result in [0,1]", "أرقام؛ F بين 0–1 والنتيجة كذلك"],
            ["6", "PCI = Σ w_k c_k / Σ w_k", "Weighted compliance; divide by Σw not n", "امتثال موزون؛ اقسم على مجموع الأوزان"],
        ],
        rtl_cols={3},
    )

    # ========== ERROR LOG ==========
    add_h(doc, "10. Your Error Log — Fix Before the Quiz", "10. سجل أخطاءك — صحّحها قبل الكويز")
    add_table(
        doc,
        ["Mistake", "Correct", "صححه"],
        [
            ["ARPANET = 1980s", "ARPANET/mainframes = 1960s", "1960s مو 1980s"],
            ["P = Portability", "P = Probability", "P = Probability الاحتمال"],
            ["0.3×100 = 90", "0.3×100 = 30 → min R = 105", "30 مو 90 — والجواب 105"],
            ["min R = −15 → no investment", "105 > 100 → investment exists", "105>100 اكو استثمار"],
            ["Integration", "Integrity (CIA pillar name)", "Integrity مو Integration"],
            ["IDS only / missing IPS · OWASP · IAM", "IDS/IPS · OWASP · IAM in domain lists", "اكتب اللي بالمادة: IDS/IPS · OWASP · IAM"],
            ["Firewall under CIA-Confidentiality", "Firewall under Network Security domains", "Firewall مال Network Security"],
            ["Banking: β not important", "Banking: Integrity β is heaviest", "بالمصرف β الأثقل"],
            ["Spelling: Ligal, bussnis, Availabilty, becoz", "Legal, business, Availability, because", "إملاء إنكليزي بالامتحان"],
        ],
        rtl_cols={2},
    )

    # ========== EXAM CHECKLIST ==========
    add_h(doc, "11. Exam Checklist — What to Memorize", "11. قائمة الفحص — شنو تحفظ")
    add_table(
        doc,
        ["Priority", "Item", "البند"],
        [
            ["HIGH", "CIA pillars + technique lists (3 columns)", "أركان CIA + قوائم التقنيات (3 أعمدة)"],
            ["HIGH", "Why α/β/γ change: healthcare / banking / emergency", "ليش الأوزان تختلف: صحة / مصرف / طوارئ"],
            ["HIGH", "Scenario recipe: step → CIA → (techniques)", "وصفة السيناريو: خطوة ← CIA ← (تقنيات)"],
            ["HIGH", "min R doctor threshold >100 investment", "قاعدة الدكتورة: فوق 100 اكو استثمار"],
            ["MED", "6 domains + techniques + expandable list", "المجالات الستة + أدواتها + قابلة للزيادة"],
            ["MED", "4 levels: individuals/enterprises/governments/trade", "المستويات الأربعة"],
            ["MED", "5 threat types + 2023–24 trends", "5 أنواع تهديدات + ترندات 2023–24"],
            ["MED", "OCTAVE · FAIR · NIST RMF names/expansions", "أسماء نماذج المخاطر وتوسّعاتها"],
            ["MED", "GDPR EU · HIPAA US · NIST/ISO international", "السياسات وجهاتها"],
            ["LOW", "R(t) awareness only", "R(t) — وعي فقط"],
            ["OUT", "Chapter 7 case studies", "الفصل السابع — خارج"],
        ],
        rtl_cols={2},
    )

    add_h(doc, "12. Core Question Bank (Selected — Full bank in vault)", "12. بنك أسئلة أساسي (مختارات — الكامل بالفولدر)")
    qa = [
        ("Q1", "Define cybersecurity in one sentence.", "عرّف الأمن السيبراني بجملة.", "Protection of systems, networks, applications, and data from cyber threats, unauthorized access, and harm — technical, legal, managerial, social.", "حماية الأنظمة والشبكات والتطبيقات والبيانات من التهديدات الإلكترونية والوصول غير المصرّح به والضرر — جوانب تقنية وقانونية وإدارية واجتماعية."),
        ("Q2", "Four aspects of cybersecurity (Ch.1)?", "أربع جوانب للفصل الأول؟", "Technical · Legal · Managerial · Social", "تقنية · قانونية · إدارية · اجتماعية"),
        ("Q3", "Four levels protected (Ch.2)?", "أربع مستويات محمية (الفصل 2)؟", "Individuals · Enterprises · Governments · Global Trade", "أفراد · مؤسسات · حكومات · تجارة عالمية"),
        ("Q4", "Six cyber domains + key techniques?", "ستة مجالات + تقنيات أساسية؟", "Network (firewalls, IDS/IPS) · Application (secure coding, OWASP) · Cloud (encryption, IAM, virtualization) · IoT (lightweight encryption, anomaly detection) · Mobile (sandboxing, malware detection) · ICS (industrial control protection). List can expand.", "شبكة · تطبيق · سحابة · IoT · موبايل · ICS — والقائمة قابلة للزيادة."),
        ("Q5", "Define CIA and list techniques.", "عرّف CIA واذكر التقنيات.", "C: unauthorized access blocked (encryption, access controls, VPNs). I: data accurate/unmodified (hashing SHA-256, digital signatures, version control). A: resources available (redundancy, load balancing, DDoS mitigation).", "C: منع وصول غير مصرّح (encryption, access controls, VPNs). I: دقة وعدم تعديل (hashing, digital signatures, version control). A: توفر (redundancy, load balancing, DDoS mitigation)."),
        ("Q6", "Why do α, β, γ differ by domain?", "ليش الأوزان تختلف حسب المجال؟", "Because pillar importance changes: healthcare prioritizes confidentiality; banking prioritizes integrity of balances/account IDs; emergency services prioritize availability.", "لأن أهمية الركن تتغير: الصحة تعطي السرّية أولاً؛ المصرف يشدّد على سلامة الأرصدة والأرقام؛ الطوارئ تحتاج التوفر دائماً."),
        ("Q7", "min R result 105 — investment or not?", "min R = 105 — اكو استثمار؟", "Yes — 105 > 100 → there is investment (doctor's stated rule).", "نعم — 105>100 ← اكو استثمار حسب قاعدة الدكتورة."),
        ("Q8", "How to reduce attack surface fastest?", "كيف تقلّل سطح الهجوم بسرعة؟", "Reduce E_j — close unused ports/services, network segmentation — easiest and cheapest lever.", "قلّل E_j — إغلاق خدمات وبورتات غير مستخدمة وتقسيم الشبكة — أسهل وأرخص رافعة."),
        ("Q9", "If F(r)=0.92, what is P(R>r)?", "لو F(r)=0.92 شنو P(R>r)؟", "0.08 → 8% chance risk exceeds r.", "0.08 ← احتمال 8% الخطر يتجاوز r."),
        ("Q10", "What does PCI measure?", "شنو يقيس PCI؟", "A weighted average of organizational compliance with policy requirements, giving more important requirements higher weight; result in [0,1].", "متوسط موزون لالتزام المؤسسة بمتطلبات السياسة، يعطي المتطلبات الأهم وزناً أكبر؛ الناتج بين 0 و1."),
    ]
    for qid, qe, qa_, ae, aa in qa:
        add_p(doc, f"{qid}. {qe}", size=10.5, bold=True, color=NAVY, space_before=6, space_after=1)
        add_p(doc, qa_, size=10.5, bold=True, color=TEAL, rtl=True, space_after=2)
        add_p(doc, f"A: {ae}", size=10, color=DARK, space_after=1)
        add_p(doc, f"الجواب: {aa}", size=10, color=GRAY, rtl=True, space_after=4)

    add_p(doc, "", space_after=8)
    add_p(doc, "Source of truth for this PDF: vault notes W01_Source_Notes.md + Week_01_Question_Bank.md + doctor method map. Full question bank (961 lines) remains in the vault.", size=9, color=GRAY, align="center", space_after=2)
    add_p(doc, "مصدر هذا الملف: ملاحظات الفولدر + بنك الأسئلة الكامل. لا يُغني عن قراءة الملاحظات الطويلة عند الحاجة للتفاصيل.", size=9, color=GRAY, rtl=True, align="center", space_after=2)
    add_p(doc, "Good luck Sunday — CIA + parentheses + arithmetic check.", size=11, bold=True, color=NAVY, align="center", space_after=2)
    add_p(doc, "حظاً موفقاً الأحد — CIA + القوس + مراجعة الحساب مرتين.", size=11, bold=True, color=TEAL, rtl=True, align="center")

    doc.save(str(DOCX))
    print("DOCX written:", DOCX)
    print("size", DOCX.stat().st_size)


if __name__ == "__main__":
    main()
