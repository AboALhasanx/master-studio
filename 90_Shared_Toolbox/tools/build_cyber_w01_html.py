# -*- coding: utf-8 -*-
"""Build bilingual Cyber Week 01 HTML for Edge print-to-PDF."""
from pathlib import Path
import html as H

OUT = Path(r"G:\My Drive\Master-Studio\01_Semester_1\01_Cyber_Security\03_Study_Notes\Week_01_Cybersecurity_Bilingual_EN_AR.html")

def esc(s):
    return H.escape(s)

def sec(title_en, title_ar, body_html):
    return f"""
<section class="sec">
  <h2><span class="en">{esc(title_en)}</span><span class="ar">{esc(title_ar)}</span></h2>
  {body_html}
</section>"""

def bilingual(en, ar):
    return f'<div class="bi"><p class="en">{esc(en)}</p><p class="ar">{esc(ar)}</p></div>'

def callout(te, ta, be, ba, kind="warn"):
    return f"""
<div class="callout {kind}">
  <div class="ct"><span class="en">{esc(te)}</span><span class="ar">{esc(ta)}</span></div>
  <div class="bi"><p class="en">{esc(be)}</p><p class="ar">{esc(ba)}</p></div>
</div>"""

def table(headers, rows, rtl_last=True):
    hs = "".join(f"<th>{esc(h)}</th>" for h in headers)
    body = []
    for r in rows:
        tds = []
        for j, c in enumerate(r):
            cls = ' class="ar-cell"' if rtl_last and j == len(r) - 1 else ""
            tds.append(f"<td{cls}>{esc(str(c))}</td>")
        body.append("<tr>" + "".join(tds) + "</tr>")
    return f'<table><thead><tr>{hs}</tr></thead><tbody>{"".join(body)}</tbody></table>'

def formula(f, note_ar=""):
    n = f'<div class="fnote ar">{esc(note_ar)}</div>' if note_ar else ""
    return f'<div class="formula">{esc(f)}</div>{n}'

def qa(qe, qa_, ae, aa):
    return f"""
<div class="qa">
  <div class="q"><span class="en">{esc(qe)}</span></div>
  <div class="q ar">{esc(qa_)}</div>
  <div class="a en">{esc(ae)}</div>
  <div class="a ar">{esc(aa)}</div>
</div>"""

parts = []

parts.append(f"""
<header class="cover">
  <div class="badge">CS601 · Week 01 · Chapters 1–6</div>
  <h1>CYBER SECURITY</h1>
  <h1 class="ar-title">الأمن السيبراني — الأسبوع الأول</h1>
  <p class="sub en">Introduction to Cybersecurity — Bilingual Study Reference (English + Arabic)</p>
  <p class="sub ar">مقدمة في الأمن السيبراني — مرجع مراجعة ثنائي اللغة كامل</p>
  <div class="meta">
    <div><b>Instructor</b><br>Asst. Prof. Dr. Huda Lafta Majeed<br><span class="ar">الدكتورة هدى لفطة مجيد — مقررة قسم الدراسات العليا</span></div>
    <div><b>Daily Quiz</b><br>Sunday 2026-09-20 · 08:30 · Essay · ~10 min · Soft stakes<br><span class="ar">الأحد 20/9 · 08:30 · مقالي · درجة خفيفة</span></div>
  </div>
  <div class="excl">Chapter 7 Case Studies EXCLUDED by the doctor — do not study it.<br><span class="ar">الفصل السابع (دراسات الحالة) خارج الامتحان — لا تذاكره.</span></div>
  <p class="foot en">Full content from vault notes + question bank — not compressed. Built by Koko 2026-09-19.</p>
  <p class="foot ar">محتوى كامل من ملاحظات الفولدر وبنك الأسئلة — بلا اختصار.</p>
</header>
""")

# 0 Exam method
parts.append(sec("0. Exam Method — Confirmed", "0. أسلوب الامتحان — مؤكد", bilingual(
    "Two question types only. Numbers given → apply the formula (write formula, substitute, compute, interpret). No numbers → analytical scenario: step → CIA pillar → (techniques in parentheses). Parentheses are mandatory. Both deep step-by-step and whole-scenario answers are accepted. Quiz is written/essay, ~10 min, soft stakes (reading compliance).",
    "نمطان فقط: بيه أرقام ← طبّق المعادلة (معادلة ← تعويض ← حساب ← تفسير). بلا أرقام ← سيناريو: خطوة ← ركن CIA ← (التقنيات بالقوس). القوس إلزامي. تُقبل الإجابة خطوة بخطوة أو تحليل السيناريو ككل. الكويز مقالي ~10 دقائق، درجة خفيفة."
) + table(
    ["If the question…", "Then you…", "بالعربي"],
    [
        ["has numbers", "formula → substitute → compute → interpret", "أرقام: معادلة ← تعويض ← حساب ← تفسير"],
        ["scenario, no numbers", "number events → CIA → (techniques)", "سيناريو: رقّم ← CIA ← (تقنيات)"],
    ],
) + callout(
    "Dr. Huda's rule on min R — record verbatim",
    "قاعدة الدكتورة على min R — سجّلها كما هي",
    "\"Above 100 → there is investment; below 100 → there is no investment.\" She heads Postgraduate Studies; her statements are the reference.",
    "«فوق 100 ← اكو استثمار؛ أقل من 100 ← مفيش استثمار». هي مقررة قسم الدراسات العليا وكلامها المرجع.",
    "rule",
)))

# CH1
parts.append(sec("1. Definition, Scope, Evolution, Importance", "1. التعريف، النطاق، التطور، الأهمية",
    bilingual(
        "Cybersecurity protects systems, networks, applications, and data from cyber threats, unauthorized access, and harm. It covers technical, legal, managerial, and social aspects. Scope: personal devices → enterprises → national critical infrastructure. Importance: national security, economic stability, privacy.",
        "الأمن السيبراني يحمي الأنظمة والشبكات والتطبيقات والبيانات من التهديدات الإلكترونية والوصول غير المصرّح به والضرر. يشمل جوانب تقنية وقانونية وإدارية واجتماعية. النطاق: أجهزة شخصية ← مؤسسات ← بنية تحتية وطنية حرجة. الأهمية: أمن وطني، استقرار اقتصادي، خصوصية."
    ) + table(
        ["Period", "Stage (EN)", "المرحلة (عربي)"],
        [
            ["1960s", "First mentions with ARPANET and early mainframes", "أول ذِكر مع ARPANET والـ mainframes"],
            ["1980s–90s", "Viruses, worms, antivirus appear", "الفيروسات والديدان ومضادات الفيروسات"],
            ["2000s", "Core to e-commerce and banking", "أساسي للتجارة الإلكترونية والمصرفية"],
            ["2010s–now", "APT · Ransomware · IoT · AI · Zero Trust", "APT · فدية · IoT · ذكاء اصطناعي · Zero Trust"],
        ],
    ) + callout("TRAP: ARPANET date", "فخ: تاريخ ARPANET",
        "ARPANET and mainframes = 1960s, not 1980s. Material says 1960s.",
        "ARPANET والـ mainframes = ستينيات 1960s مو ثمانينيات. المادة تقول 1960s.") + bilingual(
        "Formula (cyber as optimization): min R = Σ P_i · I_i − Σ C_j. P_i = probability of threat i; I_i = impact; C_j = security control investment. Idea: balance risk reduction vs investment — not blind spending.",
        "المعادلة (السايبر كمشكلة تحسين): min R = مجموع (احتمال × تأثير) − مجموع الاستثمار. P_i احتمال التهديد، I_i التأثير، C_j الاستثمار بالضابط. الفكرة: موازنة مو إنفاق أعمى."
    ) + callout("Worked example + TRAP", "مثال محلول + فخ",
        "P1=0.4,I1=200; P2=0.3,I2=100; ΣC=5 → 80+30=110; min R=105. 105>100 → investment exists. TRAPS: 0.3×100=30 not 90; P=Probability not Portability; recheck arithmetic.",
        "P1=0.4,I1=200؛ P2=0.3,I2=100؛ C=5 ← 80+30=110؛ min R=105. بما أن 105>100 ← اكو استثمار. فخاخ: 0.3×100=30 مو 90؛ P=Probability مو Portability؛ راجع الحساب مرتين.",
        "calc")))

# CH2
parts.append(sec("2. Levels, Domains, R(t)", "2. المستويات، المجالات، R(t)",
    table(
        ["Level", "Protects (EN)", "شنو يحمي"],
        [
            ["Individuals", "Devices · email · social · bank data", "أجهزة · إيميل · سوشيال · بيانات مصرف"],
            ["Enterprises", "Continuity · trust · legal compliance", "استمرارية · ثقة · امتثال قانوني"],
            ["Governments", "National security · defense · e-gov", "أمن وطني · دفاع · حكومة إلكترونية"],
            ["Global Trade", "Cross-border digital trade · finance", "تجارة رقمية عابرة للحدود · مالية"],
        ],
    ) + callout("Do not mix the two fours", "لا تخلط بين الأربعات",
        "Ch.1 aspects: technical · legal · managerial · social. Ch.2 levels: individuals · enterprises · governments · global trade.",
        "جوانب الفصل 1: تقنية · قانونية · إدارية · اجتماعية. مستويات الفصل 2: أفراد · مؤسسات · حكومات · تجارة عالمية.") + table(
        ["#", "Domain", "Techniques", "أدوات"],
        [
            ["1", "Network Security", "firewalls · IDS/IPS", "جدران نارية · IDS/IPS"],
            ["2", "Application Security", "secure coding · OWASP", "برمجة آمنة · OWASP"],
            ["3", "Cloud Security", "encryption · IAM · virtualization", "تشفير · IAM · افتراضية"],
            ["4", "IoT Security", "lightweight encryption · anomaly detection", "تشفير خفيف · كشف شذوذ"],
            ["5", "Mobile Security", "sandboxing · malware detection", "عزل · كشف برمجيات خبيثة"],
            ["6", "ICS Security", "industrial control protection", "حماية تحكم صناعي"],
        ],
    ) + callout("TRAP: incomplete technique lists", "فخ: قوائم تقنيات ناقصة",
        "Material lists IDS/IPS (not IDS only), OWASP under Application, IAM under Cloud. Domain list can expand (AI Security, Supply-Chain Security…).",
        "المادة تكتب IDS/IPS و OWASP تحت Application و IAM تحت Cloud. القائمة قابلة للزيادة (AI Security · Supply-Chain…).") + bilingual(
        "R(t) = Σ P_i(t) · I_i(t) — expected risk at time t. Doctor: awareness only (\"we just know this law is used here\").",
        "R(t) = مجموع (احتمال × تأثير) عند الزمن t. الدكتورة: وعي سطحي فقط — «بس نعرف هذا القانون هنا يستخدم»."
    )))

# CH3 CIA
parts.append(sec("3. CIA Triad — Most Important", "3. ثالوث CIA — الأهم بالوحدة",
    bilingual(
        "CIA is the vocabulary written inside parentheses in every scenario answer. Without it the answer is incomplete.",
        "ثاثوث CIA هو المفردات اللي تكتبها بالقوس بكل جواب سيناريو. بدونها الجواب ناقص."
    ) + table(
        ["Pillar", "Definition (EN)", "Techniques (parentheses)", "التعريف"],
        [
            ["Confidentiality", "Prevent unauthorized access", "encryption · access controls · VPNs", "منع وصول غير مصرّح به"],
            ["Integrity", "Data accurate and unaltered", "hashing (SHA-256) · digital signatures · version control", "دقة البيانات وعدم تعديلها"],
            ["Availability", "Resources available when needed", "redundancy · load balancing · DDoS mitigation", "توفر الموارد وقت الحاجة"],
        ],
    ) + callout("TRAP: Integrity · Firewall", "فخ: Integrity · Firewall",
        "Write Integrity, not Integration. Firewall belongs to Network Security domain techniques, NOT inside CIA-Confidentiality list.",
        "اكتب Integrity مو Integration. الـ Firewall يندرج تحت Network Security مو داخل قائمة CIA-Confidentiality.") + bilingual(
        "U(C,I,A) = α·C + β·I + γ·A. C,I,A normalized in [0,1]; α,β,γ importance weights for that system. Weights are NOT fixed.",
        "U(C,I,A) = α·C + β·I + γ·A. القيم منظّمة 0–1 والأوزان حسب النظام — وليست ثابتة."
    ) + table(
        ["Domain", "Heaviest pillar", "Why", "ليش"],
        [
            ["Healthcare", "Confidentiality (α)", "Patient privacy first", "خصوصية المرضى أولاً"],
            ["Banking", "Integrity (β)", "Changed account/balance = catastrophe", "تغيير رقم حساب أو رصيد = كارثة"],
            ["Emergency", "Availability (γ)", "Must stay up always", "لازم يشتغل دائماً"],
        ],
    ) + callout("TRAP: banking β + worked U", "فخ: β بالمصرف + مثال U",
        "Banking: Integrity β is heavy, not light. Worked: α=0.5,β=0.3,γ=0.2; C=0.9,I=0.7,A=0.8 → 0.45+0.21+0.16=0.82 ∈ [0,1]. Doctor quote: \"In healthcare, confidentiality (α) has higher weight than availability.\"",
        "بالمصرف β ثقيل مو خفيف. مثال: α=0.5,β=0.3,γ=0.2 و C=0.9,I=0.7,A=0.8 ← 0.45+0.21+0.16=0.82 وينتمي لـ[0,1]. كلام الدكتورة: بالصحة α أثقل من التوفر.",
        "calc")))

# CH4
parts.append(sec("4. Threat Landscape + Attack Surface AS", "4. مشهد التهديدات + سطح الهجوم",
    table(
        ["Type", "Description", "Examples", "الوصف"],
        [
            ["Malware", "Malicious software", "Viruses · Worms · Trojans · Ransomware", "برمجيات خبيثة"],
            ["Phishing / SE", "Exploit human trust", "spear phishing · BEC", "استغلال الثقة البشرية"],
            ["Insider Threats", "Staff misuse privileges", "internal leak", "موظفون يسيئون الصلاحيات"],
            ["APTs", "State-backed · stealthy · long-term", "Advanced Persistent Threats", "مدعومة من دول · خفية · طويلة"],
            ["IoT Attacks", "Compromise IoT devices", "Botnets — Mirai", "أجهزة إنترنت الأشياء — Mirai"],
        ],
    ) + bilingual(
        "Trends 2023–2024: (1) Ransomware damages exceed $20B; (2) cloud attacks rise from misconfigurations; (3) AI-powered attacks grow.",
        "اتجاهات 2023–2024: (1) أضرار الفدية تتجاوز 20 مليار؛ (2) هجمات سحابية بسبب misconfigurations؛ (3) هجمات مدعومة بالذكاء الاصطناعي."
    ) + formula("AS = Σ ( E_j · V_j · A_j )", "سطح الهجوم = مجموع نقاط الدخول × شدة الثغرة × قيمة الأصل") + table(
        ["Symbol", "Meaning", "Range", "المعنى"],
        [
            ["E_j", "Exposed entry points", "count", "نقاط دخول مكشوفة"],
            ["V_j", "Vulnerability severity (CVSS)", "0.0–10.0", "شدة الثغرة"],
            ["A_j", "Asset value", "money/ops", "قيمة الأصل"],
        ],
    ) + callout("Why multiply · worked · lever", "ليش ضرب · مثال · رافعة",
        "Multiply because all three needed: E=0 unreachable; V=0 hardened; A=0 not worth it. Example: (3×8×100)+(2×5×300)=2400+3000=5400. Fastest lever: lower E (close unused ports, segmentation).",
        "الضرب لأن الثلاثة لازم يتوفرون: E=0 ما يوصله أحد، V=0 محصّن، A=0 ما يستاهل. مثال: 2400+3000=5400. أسرع رافعة: قلّل E بإغلاق البورتات غير المستخدمة والتقسيم.",
        "calc")))

# CH5
parts.append(sec("5. Risk / Vulnerability / Exploit + P(R>r)", "5. خطر / ثغرة / استغلال + P(R>r)",
    table(
        ["Concept", "Definition", "Example", "التعريف"],
        [
            ["Risk", "Probability × Impact function", "30% × $1M", "دالة (احتمال × تأثير)"],
            ["Vulnerability", "Software/hardware/human weakness", "OWASP Top 10 · CVEs", "نقطة ضعف برمجية/عتادية/بشرية"],
            ["Exploit", "Tool/technique using the weakness", "Metasploit · script", "أداة تستغل الثغرة"],
        ],
    ) + bilingual(
        "Relation: vulnerability + exploit = risk when probability and impact are high. Models: OCTAVE (Operationally Critical Threat, Asset, and Vulnerability Evaluation), FAIR (Factor Analysis of Information Risk), NIST RMF (Risk Management Framework).",
        "العلاقة: ثغرة + استغلال = خطر إذا الاحتمال والتأثير عاليان. النماذج: OCTAVE و FAIR و NIST RMF — احفظ الأسماء والتوسّع."
    ) + formula("P(R > r) = 1 − F(r)", "احتمال تجاوز الخطر للحد = 1 − دالة التوزيع التراكمي") + callout("Meaning + worked", "المعنى + مثال",
        "F(r)=P(R≤r) is always in [0,1] (probability). 1−F(r) is the catastrophe tail. Example: r=$10,000, F=0.92 → P(R>r)=0.08 → 8% chance loss exceeds limit.",
        "F(r)=احتمال الخطر≤r ودائماً بين 0 و1. و 1−F(r) احتمال الكارثة الأكبر من الحد. مثال: r=10,000 و F=0.92 ← 0.08 أي 8%.",
        "calc")))

# CH6
parts.append(sec("6. Evolution, Policies, PCI", "6. التطور، السياسات، PCI",
    table(
        ["Phase", "Period", "Focus", "التركيز"],
        [
            ["Early", "1960s–1990s", "Perimeter defense — firewalls · antivirus", "دفاع محيطي"],
            ["Modern", "2000s–now", "Cloud · IoT · Mobile · AI attacks", "سحابة · IoT · موبايل · AI"],
        ],
    ) + table(
        ["Framework", "Body", "Covers", "جهة"],
        [
            ["GDPR", "EU", "Data protection & privacy", "الاتحاد الأوروبي"],
            ["HIPAA", "USA", "Healthcare information", "أمريكا"],
            ["NIST / ISO 27001", "International", "International standards", "دولية"],
        ],
    ) + table(
        ["Region", "Tools", "أدوات"],
        [
            ["US", "NIST CSF · Federal Cybersecurity Strategy", "NIST CSF · استراتيجية فيدرالية"],
            ["EU", "GDPR · ENISA", "GDPR · ENISA"],
            ["Middle East", "National Cybersecurity Councils", "مجالس وطنية للأمن السيبراني"],
        ],
    ) + formula("PCI = ( Σ w_k · c_k ) / ( Σ w_k )", "مؤشر الامتثال = متوسط موزون") + callout("Worked PCI + trap", "مثال PCI + فخ",
        " (w,c)=(3,1.0),(2,0.5),(1,0.0) → numerator 4.0; denominator 6; PCI=0.667 → 66.7%. Divide by Σw, never by n alone. Result always in [0,1].",
        "(3,1.0) و(2,0.5) و(1,0.0) ← البسط 4.0 والمقام 6 ← PCI=0.667 أي 66.7%. اقسم على مجموع الأوزان مو على n. الناتج دائماً 0–1.",
        "calc")))

# CH7
parts.append(sec("7. Case Studies — OUT", "7. دراسات الحالة — خارج",
    bilingual(
        "Stuxnet · Colonial Pipeline · GDPR Enforcement — explicitly excluded by the doctor.",
        "Stuxnet · Colonial Pipeline · GDPR Enforcement — الدكتورة استثنتهن صراحة.",
    )))

# Scenarios
scen = []
scenarios = [
    ("Scenario 1 — Bank $100k drop", "سيناريو 1 — نقص 100,000 بالحساب",
     "Customer sees $100,000 missing; manager finds a software bug; amount restored.",
     "عميل شاف نقص 100,000$؛ المدير طلع السبب خلل برنامجي؛ رجع المبلغ.",
     [
         ["1", "Customer data changed", "Integrity", "(hashing SHA-256, digital signatures, version control)"],
         ["2", "System/service issue", "Availability", "(redundancy, load balancing, DDoS mitigation)"],
         ["3", "Fixed; amount restored", "—", "resolved"],
     ]),
    ("Scenario 2 — Hospital old account", "سيناريو 2 — مستشفى حساب قديم",
     "Patient records visible to unauthorized staff; old employee account still active.",
     "سجلات المرضى تظهر لغير المصرّح؛ حساب موظف قديم لسّه فعّال.",
     [
         ["1", "Patient data exposed", "Confidentiality", "(encryption, access controls, VPNs)"],
         ["2", "Old account not disabled", "Access-control failure", "(access controls + periodic review)"],
         ["3", "Disable + audit privileges", "—", "remediation"],
     ]),
    ("Scenario 3 — University registration down", "سيناريو 3 — وقوع التسجيل الجامعي",
     "Registration system fails during registration week; thousands cannot register.",
     "نظام التسجيل وقع بوقت التسجيل؛ آلاف ما قدروا يسجّلوا.",
     [
         ["1", "System unavailable when needed", "Availability", "(redundancy, load balancing, DDoS mitigation)"],
         ["2", "Possible DDoS", "Availability", "(DDoS mitigation)"],
         ["3", "Long-term: backup servers + LB", "Availability", "(redundancy + load balancing)"],
     ]),
    ("Scenario 4 — E-commerce price change", "سيناريو 4 — تغير سعر متجر",
     "Invoice price changed after order confirmation.",
     "سعر الفاتورة تغيّر بعد تأكيد الطلب.",
     [
         ["1", "Data changed after confirm", "Integrity", "(hashing, digital signatures, version control)"],
         ["2", "version control shows who/when", "Integrity", "(version control)"],
         ["3", "If system fault", "Availability", "(system not operating correctly)"],
     ]),
    ("Scenario 5 — Millions spent, still down", "سيناريو 5 — ملايين ومع ذلك وقع",
     "Heavy security spend; systems slow then down; CEO says they cannot be hacked.",
     "إنفاق أمني ضخم؛ الأنظمة بطيئة ثم توقفت؛ المدير قال مستحيل يخترقونا.",
     [
         ["1", "Systems degraded then down", "Availability", "(redundancy, load balancing, DDoS mitigation)"],
         ["2", "Spend ≠ protection if misaligned", "Risk logic", "(risk assessment before purchase)"],
         ["3", "ΣC large does not force ΣP·I small", "min R", "(align spend to real threats)"],
     ]),
]
for te, ta, be, ba, rows in scenarios:
    scen.append(callout(te, ta, be, ba, "scen") + table(
        ["Step", "What happened", "Pillar", "(Techniques)"], rows, rtl_last=False
    ))

parts.append(sec("8. Scenario Recipe + Practice", "8. وصفة السيناريو + تدريب",
    bilingual(
        "Step 1 number events. Step 2 for each: what was harmed? Exposed → Confidentiality; altered → Integrity; down → Availability. Step 3 write pillar + techniques in parentheses from the CIA table. Accepted: deep steps or whole scenario. Not accepted: no CIA or no parentheses.",
        "1) رقّم الأحداث. 2) لكل حدث: شنو تضرر؟ انكشف ← C؛ تغيّر ← I؛ توقف ← A. 3) الركن + التقنيات بالقوس من جدول CIA. مقبول: تحليل عميق أو تحليل ككل. غير مقبول: بلا CIA أو بلا قوس."
    ) + "".join(scen)))

# Formulas summary
parts.append(sec("9. Six Formulas — Quick Sheet", "9. المعادلات الست — ورقة سريعة",
    table(
        ["#", "Formula", "Use / rule", "الاستعمال"],
        [
            ["1", "min R = Σ P_i I_i − Σ C_j", "Numbers; >100 = investment (doctor)", "أرقام؛ >100 اكو استثمار"],
            ["2", "R(t) = Σ P_i(t) I_i(t)", "Awareness only", "وعي سطحي"],
            ["3", "U = αC + βI + γA", "Weights by domain; U in [0,1]", "أوزان حسب المجال؛ U بـ[0,1]"],
            ["4", "AS = Σ E V A", "E count · V CVSS · A asset value", "E عدد · V شدة · A قيمة"],
            ["5", "P(R>r) = 1 − F(r)", "F in [0,1]; result in [0,1]", "F والنتيجة بـ[0,1]"],
            ["6", "PCI = Σ w c / Σ w", "Divide by Σw not n", "اقسم على مجموع الأوزان"],
        ],
    )))

# Error log
parts.append(sec("10. Error Log — Fix Before Quiz", "10. سجل الأخطاء — صحّحها قبل الكويز",
    table(
        ["Mistake", "Correct", "الصحيح"],
        [
            ["ARPANET = 1980s", "1960s", "1960s"],
            ["P = Portability", "P = Probability", "Probability"],
            ["0.3×100=90; min R=−15", "30; min R=105; investment", "30؛ 105؛ اكو استثمار"],
            ["Integration", "Integrity", "Integrity"],
            ["IDS only; missing IPS/OWASP/IAM", "IDS/IPS · OWASP · IAM", "اكتب اللي بالمادة"],
            ["Firewall in CIA-C list", "Firewall under Network Security", "مال Network Security"],
            ["Bank β not important", "Bank β heaviest", "β الأثقل بالمصرف"],
            ["Ligal / bussnis / becoz", "Legal / business / because", "إملاء إنكليزي صحيح"],
        ],
    )))

# Checklist
parts.append(sec("11. Exam Checklist", "11. قائمة الفحص",
    table(
        ["Priority", "Item", "البند"],
        [
            ["HIGH", "CIA + technique lists (3 columns)", "CIA + قوائم التقنيات"],
            ["HIGH", "α/β/γ by domain + banking Integrity heavy", "الأوزان حسب المجال"],
            ["HIGH", "Scenario: step → CIA → (techniques)", "وصفة السيناريو"],
            ["HIGH", "min R >100 investment rule + arithmetic check", "قاعدة 100 + مراجعة حساب"],
            ["MED", "6 domains + 4 levels + 5 threats + trends", "مجالات · مستويات · تهديدات"],
            ["MED", "OCTAVE/FAIR/NIST · GDPR/HIPAA/ISO", "نماذج وسياسات"],
            ["LOW", "R(t) awareness", "R(t) وعي فقط"],
            ["OUT", "Chapter 7 case studies", "الفصل السابع"],
        ],
    )))

# QA bank selected
qas = [
    ("Define cybersecurity.", "عرّف الأمن السيبراني.",
     "Protection of systems, networks, applications, and data from cyber threats, unauthorized access, and harm — technical, legal, managerial, social.",
     "حماية الأنظمة والشبكات والتطبيقات والبيانات من التهديدات والوصول غير المصرّح — جوانب تقنية وقانونية وإدارية واجتماعية."),
    ("Four aspects (Ch1) vs four levels (Ch2)?", "أربع جوانب (ف1) مقابل أربع مستويات (ف2)؟",
     "Aspects: technical, legal, managerial, social. Levels: individuals, enterprises, governments, global trade.",
     "جوانب: تقنية، قانونية، إدارية، اجتماعية. مستويات: أفراد، مؤسسات، حكومات، تجارة عالمية."),
    ("Six domains + techniques?", "ستة مجالات + تقنيات؟",
     "Network (firewalls, IDS/IPS); Application (secure coding, OWASP); Cloud (encryption, IAM, virtualization); IoT (lightweight encryption, anomaly detection); Mobile (sandboxing, malware detection); ICS (industrial control protection). Expandable list.",
     "شبكة · تطبيق · سحابة · IoT · موبايل · ICS — والقائمة قابلة للزيادة."),
    ("CIA + techniques?", "CIA + التقنيات؟",
     "C: encryption, access controls, VPNs. I: hashing SHA-256, digital signatures, version control. A: redundancy, load balancing, DDoS mitigation.",
     "C: تشفير، ضوابط وصول، VPNs. I: hashing، توقيعات رقمية، version control. A: redundancy، load balancing، DDoS mitigation."),
    ("Why α/β/γ differ?", "ليش الأوزان تختلف؟",
     "Domain priorities: healthcare → confidentiality; banking → integrity of accounts/balances; emergency → availability always on.",
     "أولويات المجال: صحة ← سرّية؛ مصرف ← سلامة الأرصدة؛ طوارئ ← توفر دائم."),
    ("min R = 105?", "min R = 105؟",
     "105 > 100 → there is investment (doctor's rule).",
     "105>100 ← اكو استثمار حسب قاعدة الدكتورة."),
    ("Fastest way to cut AS?", "أسرع تقليل لـ AS؟",
     "Reduce E_j — close unused ports/services, network segmentation.",
     "قلّل E_j — إغلاق خدمات وبورتات غير مستخدمة وتقسيم الشبكة."),
    ("F(r)=0.92 → P(R>r)?", "F(r)=0.92 ← P(R>r)؟",
     "1 − 0.92 = 0.08 → 8% chance risk exceeds r.",
     "1−0.92=0.08 ← احتمال 8% الخطر يتجاوز r."),
    ("What is PCI?", "شنو PCI؟",
     "Weighted average of compliance levels c_k with weights w_k; divide by Σw; result in [0,1].",
     "متوسط موزون لمستويات الامتثال c_k بأوزان w_k؛ القسمة على مجموع الأوزان؛ الناتج 0–1."),
]
qa_html = "".join(qa(*x) for x in qas)
parts.append(sec("12. Core Q&A (Selected)", "12. أسئلة وأجوبة أساسية (مختارات)", qa_html))

parts.append("""
<footer class="end">
  <p class="en"><b>Good luck Sunday</b> — CIA + parentheses + recheck arithmetic.</p>
  <p class="ar"><b>حظاً موفقاً الأحد</b> — CIA + القوس + راجع الحساب مرتين.</p>
  <p class="tiny en">Full vault notes + 961-line question bank remain at 01_Cyber_Security/03_Study_Notes and 07_Quizzes_&_Anki. This PDF is the complete bilingual reading pack for the quiz — not a compressed outline.</p>
  <p class="tiny ar">الملاحظات الكاملة وبنك الأسئلة يبقون بالفولدر. هذا الـ PDF حزمة القراءة الثنائية الكاملة للكويز — مو ملخص مضغوط.</p>
</footer>
""")

html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8"/>
<title>Cyber Security Week 01 — Bilingual EN/AR</title>
<style>
@page {{ size: A4; margin: 14mm 12mm; }}
* {{ box-sizing: border-box; }}
body {{
  font-family: "Segoe UI", Tahoma, Arial, sans-serif;
  color: #1f2937;
  margin: 0;
  background: #fff;
  line-height: 1.45;
  font-size: 10.5pt;
}}
.cover {{
  page-break-after: always;
  text-align: center;
  padding: 28mm 8mm 10mm;
  border: 2px solid #1e3a8a;
}}
.badge {{
  display: inline-block;
  background: #1e3a8a;
  color: #fff;
  padding: 6px 14px;
  border-radius: 999px;
  font-size: 10pt;
  font-weight: 700;
  margin-bottom: 14px;
}}
h1 {{
  color: #1e3a8a;
  font-size: 26pt;
  margin: 8px 0 4px;
  letter-spacing: 0.5px;
}}
h1.ar-title {{
  color: #0f766e;
  font-size: 20pt;
  margin: 0 0 12px;
}}
.sub {{ margin: 2px 0; font-size: 11pt; }}
.sub.en {{ color: #1e3a8a; font-weight: 600; }}
.sub.ar {{ color: #0f766e; }}
.meta {{
  display: flex;
  justify-content: center;
  gap: 24px;
  margin: 22px 0 16px;
  text-align: center;
  font-size: 10pt;
}}
.meta > div {{
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  padding: 12px 16px;
  min-width: 200px;
}}
.excl {{
  margin: 18px auto;
  max-width: 480px;
  border: 2px dashed #b91c1c;
  color: #b91c1c;
  padding: 10px;
  font-weight: 600;
  border-radius: 8px;
}}
.foot {{ margin-top: 18px; font-size: 9pt; color: #6b7280; }}
.sec {{ page-break-inside: auto; margin: 0 0 14px; }}
h2 {{
  font-size: 13pt;
  color: #fff;
  background: #1e3a8a;
  margin: 16px 0 10px;
  padding: 8px 12px;
  border-radius: 6px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}}
h2 .en {{ font-weight: 700; }}
h2 .ar {{ font-size: 11pt; color: #a7f3d0; font-weight: 600; }}
.bi {{ margin: 6px 0 8px; }}
.bi p {{ margin: 3px 0; }}
.en {{ direction: ltr; text-align: left; unicode-bidi: plaintext; }}
.ar {{ direction: rtl; text-align: right; unicode-bidi: plaintext; font-family: Tahoma, Arial, "Segoe UI", sans-serif; }}
p.en {{ color: #111827; }}
p.ar {{ color: #374151; }}
table {{
  width: 100%;
  border-collapse: collapse;
  margin: 8px 0 12px;
  font-size: 9.5pt;
  page-break-inside: avoid;
}}
th {{
  background: #1e3a8a;
  color: #fff;
  padding: 6px 8px;
  border: 1px solid #1e3a8a;
  font-weight: 700;
}}
td {{
  border: 1px solid #d1d5db;
  padding: 5px 7px;
  vertical-align: top;
  background: #fff;
}}
tr:nth-child(even) td {{ background: #f8fafc; }}
td.ar-cell {{ direction: rtl; text-align: right; }}
.callout {{
  border-right: 4px solid #b91c1c;
  background: #fef2f2;
  padding: 8px 10px;
  margin: 8px 0 10px;
  border-radius: 0 8px 8px 0;
  page-break-inside: avoid;
}}
.callout.rule {{ border-right-color: #1e3a8a; background: #eff6ff; }}
.callout.calc {{ border-right-color: #92400e; background: #fffbeb; }}
.callout.scen {{ border-right-color: #0f766e; background: #ecfdf5; }}
.ct {{ margin-bottom: 4px; font-weight: 700; }}
.ct .en {{ color: #b91c1c; display: block; }}
.ct .ar {{ color: #991b1b; display: block; font-size: 10pt; }}
.callout.rule .ct .en, .callout.rule .ct .ar {{ color: #1e3a8a; }}
.callout.calc .ct .en, .callout.calc .ct .ar {{ color: #92400e; }}
.callout.scen .ct .en, .callout.scen .ct .ar {{ color: #0f766e; }}
.formula {{
  text-align: center;
  font-weight: 700;
  color: #1e3a8a;
  background: #f1f5f9;
  border: 1px solid #94a3b8;
  border-radius: 8px;
  padding: 10px;
  margin: 8px 0 4px;
  font-size: 12pt;
  letter-spacing: 0.3px;
}}
.fnote {{
  text-align: center;
  color: #4b5563;
  font-size: 9.5pt;
  margin-bottom: 8px;
}}
.qa {{
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 8px 10px;
  margin: 6px 0;
  page-break-inside: avoid;
  background: #fafafa;
}}
.qa .q {{ font-weight: 700; margin-bottom: 2px; }}
.qa .q.en {{ color: #1e3a8a; }}
.qa .q.ar {{ color: #0f766e; }}
.qa .a {{ margin-top: 2px; font-size: 10pt; }}
.qa .a.ar {{ color: #4b5563; }}
.end {{
  margin-top: 18px;
  padding-top: 10px;
  border-top: 2px solid #1e3a8a;
  text-align: center;
}}
.end .en {{ font-size: 12pt; color: #1e3a8a; }}
.end .ar {{ font-size: 12pt; color: #0f766e; font-weight: 700; }}
.tiny {{ font-size: 8.5pt; color: #6b7280; }}
</style>
</head>
<body>
{''.join(parts)}
</body>
</html>"""

OUT.write_text(html, encoding="utf-8")
print("HTML written", OUT, "bytes", OUT.stat().st_size)
