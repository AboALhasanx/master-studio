# -*- coding: utf-8 -*-
"""Bilingual EN-AR comprehensive pack for ASE Lecture 01 (Dr. Ali Fahim)."""
from pathlib import Path
import html as H

OUT_DIR = Path(r"G:\My Drive\Master-Studio\01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes")

def e(s):
    return H.escape(str(s))

def bi(en, ar):
    return f'<div class="bi"><p class="en">{e(en)}</p><p class="ar">{e(ar)}</p></div>'

def quote(en):
    return f'<div class="q">{e(en)}</div>'

def callout(te, ta, be, ba, kind="warn"):
    return f'''<div class="callout {kind}">
<div class="ct"><span class="en">{e(te)}</span><span class="ar">{e(ta)}</span></div>
{bi(be, ba)}</div>'''

def table(headers, rows):
    hs = "".join(f"<th>{e(h)}</th>" for h in headers)
    body = []
    for r in rows:
        tds = "".join(f"<td>{e(c)}</td>" for c in r)
        body.append(f"<tr>{tds}</tr>")
    return f'<table><thead><tr>{hs}</tr></thead><tbody>{"".join(body)}</tbody></table>'

def sec(n, en, ar, body):
    return f'''<section class="sec">
<h2><span class="en">{n}. {e(en)}</span><span class="ar">{e(ar)}</span></h2>
{body}</section>'''

parts = []

parts.append(sec(1, "Course frame & textbooks", "1. إطار المادة والمصادر",
    bi("Advanced Software Engineering — Dr. Ali Fahim Ni'ma — Monday 10:30–13:30 — 3 credits. No static slides; primary literature + four canonical textbooks.",
       "هندسة البرمجيات المتقدمة — د. علي فاهم نعمة — الاثنين 10:30–13:30 — 3 ساعات. بلا سلايدات ثابتة؛ مراجع أساسية + أربعة كتب معتمدة.")
    + table(["Textbook", "Role", "الدور"], [
        ["Sommerville 9th Ed — Ch 1–2", "Evolving software · socio-technical systems", "تطور البرمجيات · الأنظمة الاجتماعية-التقنية"],
        ["Pressman — Ch 1", "Software as product + vehicle; process", "البرمجية كمنتج ومنصة؛ العملية"],
        ["Rajib Mall 4th Ed — Ch 1–2", "SE foundations", "أسس هندسة البرمجيات"],
        ["Agarwal et al. 2010 — Ch 1", "SE & testing intro", "مقدمة هندسة البرمجيات والاختبار"],
        ["Brooks 1987 IEEE Computer", "No Silver Bullet (Essential vs Accidental)", "لا رصاصة فضية"],
    ])
    + callout("External sources policy", "سياسة المصادر الخارجية",
        "Dr. Ali: students may adopt another source only after presenting it to him for review/approval.",
        "د. علي: يجوز اعتماد مصدر آخر بعد عرضه عليه للمراجعة والموافقة.", "rule")))

parts.append(sec(2, "Evolving role of software", "2. الدور المتطور للبرمجيات",
    table(["Era", "Architecture", "Paradigm", "Bottleneck", "العصر/العنق الزجاجي"], [
        ["1950s–1960s", "Batch processing", "Custom code, hardware-centric", "No formal methodology", "بلا منهجية رسمية"],
        ["1970s–1980s", "Multi-user systems", "Real-time DBs, product software", "Exploding maintenance costs", "انفجار كلفة الصيانة"],
        ["1990s–2000s", "Distributed & Web", "Client-server, component reuse", "Network reliability & security", "موثوقية وأمن الشبكات"],
        ["2010s–2026+", "Cloud & AI ubiquitous", "Cyber-physical, autonomous agents", "Socio-technical alignment; non-deterministic outputs", "مواءمة اجتماعية-تقنية؛ مخرجات غير حتمية"],
    ])
    + bi("Pressman dual role: (1) Software as a Product — computing capability, information transformation, business logic. (2) Software as a Vehicle/Infrastructure — platform controlling hardware, OS, networks, cyber-physical systems.",
        "الدور المزدوج (Pressman): (1) برمجية كمنتج — قدرة حسابية وتحويل معلومات ومنطق أعمال. (2) برمجية كمنصة/مركبة — تتحكم بالعتاد ونظم التشغيل والشبكات والأنظمة الفيزيائية-الرقمية.")
    + bi("Sommerville socio-technical systems: technical core (code, DBs, microservices) + operational process (procedures, runbooks, pipelines) + human element (operators, org structure, user psychology).",
        "أنظمة اجتماعية-تقنية (Sommerville): النواة التقنية + العملية التشغيلية + العنصر البشري (مشغّلون، بنية تنظيمية، سيكولوجية المستخدم).")))

parts.append(sec(3, "Dependability chain (Error → Fault → Error State → Failure)", "3. سلسلة الاعتمادية (خطأ ← عيب ← حالة خطأ ← فشل)",
    table(["Stage", "English", "عربي", "Engineering meaning"], [
        ["1", "Human Error", "زلة/خطأ بشري", "Wrong mental act of programmer/architect → produces defect"],
        ["2", "Static Fault / Defect", "خلل/عيب ساكن", "Dormant flaw in code or specs until executed"],
        ["3", "Internal Error State", "حالة خطأ داخلية", "Invalid internal state when fault is activated at runtime"],
        ["4", "Observable Failure", "فشل مرصود", "Service deviates from spec at the user interface"],
    ])
    + bi("Chain: developer mistake → silent defect in repository → runtime activates defect → observable failure.",
        "السلسلة: خطأ المطوّر ← عيب ساكن بالمستودع ← التفعيل بالتشغيل ← فشل مرئي عند المستخدم.")
    + callout("Exam trap", "فخ امتحاني",
        "Do not swap Error (cognitive mistake) and Fault (static defect). Failure is what the user observes.",
        "لا تخلط بين Error (خطأ معرفي) و Fault (عيب ثابت). الـ Failure هو ما يرصده المستخدم.", "warn")))

parts.append(sec(4, "Patriot missile — Dhahran 1991 (kinematics)", "4. صاروخ الباتريوت — الظهران 1991 (الحركيات)",
    bi("US MIM-104 Patriot battery, Operation Desert Storm, 25 Feb 1991 — benchmark case: tiny numerical representation error → lethal system failure.",
        "بطارية باتريوت أمريكية، عاصفة الصحراء، 25 شباط/فبراير 1991 — دراسة مرجعية: خطأ تمثيل رقمي صغير ← فشل قاتل.")
    + table(["Parameter", "Value", "Meaning", "المعنى"], [
        ["Clock resolution", "0.1 s", "Integer tick every tenth second", "نبضة كل 0.1 ثانية"],
        ["24-bit truncation", "0.0999999046 s", "Binary 1/10 truncated at bit 24", "تقريب 1/10 عند البت 24"],
        ["Error per tick", "~9.54e-8 s", "Systematic negative drift", "انحراف سالب منهجي"],
        ["Uptime", "100 h = 3,600,000 ticks", "Mobile system left running", "نظام ميداني شغّال 100 ساعة"],
        ["Total drift", "0.3433 s", "Clock lagged real time", "تأخر الساعة عن الزمن الحقيقي"],
        ["Scud speed", "Mach 5 ≈ 1676 m/s", "Ballistic target", "هدف باليستي سريع"],
        ["Range gate shift", "~687 m", "Radar searched empty air", "الرادار يبحث فضاءً فارغاً"],
        ["Human cost", "28 soldiers killed", "Dhahran barracks", "28 جندياً في الظهران"],
    ])
    + bi("Key lessons: (1) Inconsistent maintenance — some radar routines upgraded to 48-bit, range-gate calc left at 24-bit; inconsistency is more dangerous than unpatched legacy. (2) Operational envelope violation — design assumed intermittent mobile use, not 100h continuous.",
        "دروس: (1) صيانة غير متسقة — بعض روتينات الرادار حُدّثت إلى 48-bit وبقي حساب بوابة المدى 24-bit؛ عدم التطابق أخطر من النظام القديم غير المحدّث. (2) خرق نطاق التشغيل — التصميم افترض استخداماً ميدانياً متقطعاً مو 100 ساعة متواصلة.")
    + callout("Math takeaway", "الخلاصة الرياضية",
        "Per-tick error × number of ticks × target speed = range-gate displacement. Small representation error × long uptime × high speed = catastrophe.",
        "خطأ النبضة × عدد النبضات × سرعة الهدف = إزاحة بوابة المدى. خطأ صغير × وقت طويل × سرعة عالية = كارثة.", "calc")))

parts.append(sec(5, "Brooks — No Silver Bullet (Essential vs Accidental)", "5. بروكس — لا رصاصة فضية (جوهري مقابل عرضي)",
    quote("There is no single development, in either technology or management technique, which by itself promises even one order of magnitude (10x) improvement in productivity, in reliability, in simplicity, within a decade.")
    + table(["Dimension", "Type", "Definition", "Implication", "النوع/المعنى"], [
        ["Complexity", "Essential", "Vast non-identical interacting parts", "Non-linear scaling; exploding state space", "تفاعل أجزاء غير متطابقة؛ انفجار فضاء الحالة"],
        ["Conformity", "Essential", "Must conform to arbitrary human institutions/interfaces", "No natural laws to simplify", "مواءمة مؤسسات بشرية اعتباطية"],
        ["Changeability", "Essential", "Perpetual pressure to modify software", "Architecture decays under change", "ضغط دائم للتعديل"],
        ["Invisibility", "Essential", "No geometric physical representation", "Cannot fully draw topology in 2D/3D", "بلا تمثيل هندسي مكاني"],
        ["Syntax / assembly", "Accidental", "Tedious language & boilerplate", "Solved by high-level languages", "حُلّت بلغات عالية المستوى"],
        ["Tool friction", "Accidental", "Slow compile/link/batch queues", "Solved by IDEs, CI/CD", "حُلّت بأدوات حديثة"],
        ["Memory allocation", "Accidental", "Manual leaks, dangling pointers", "Solved by GC & modern types", "حُلّت بـ GC وأنظمة أنواع"],
    ])
    + bi("Essential complexity is inherent to the software problem itself. Accidental complexity is overhead of tools/languages — reducible, but never to zero total difficulty.",
        "التعقيد الجوهري متأصل في مشكلة البرمجيات نفسها. العرضي زائد أدوات/لغات — يمكن تخفيضه، لكن لا يلغي صعوبة البرمجيات الجوهرية.")
    + callout("Oral defense cue", "إشارة الشفوي",
        "Generative AI / cloud cannot eliminate the crisis because they mainly attack accidental complexity; essential complexity (complexity, conformity, changeability, invisibility) remains.",
        "الذكاء الاصطناعي التوليدي/السحابة لا يلغيان الأزمة لأنهما يهاجمان غالباً التعقيد العرضي؛ الجوهري يبقى.", "rule")))

parts.append(sec(6, "What software is — Tripartite asset + SE definitions", "6. شنو البرمجية — الأصل الثلاثي + تعريفات الهندسة",
    quote("Software = Programs + Data Structures + Complete Documentation")
    + table(["Pillar", "Components", "Role", "الدور"], [
        ["Programs (Code)", "binaries, source, build scripts, tests", "Execute logic; transform I/O", "تنفيذ المنطق"],
        ["Data Structures", "schemas, caches, JSON/Protobuf", "Encapsulate state & domain model", "تغليف الحالة ونموذج المجال"],
        ["Documentation", "SRS (ISO 29148), architecture (IEEE 42010), ADRs, runbooks", "Preserve knowledge; enable maintenance", "حفظ المعرفة وتمكين الصيانة"],
    ])
    + quote("IEEE 610.12: Software Engineering is the application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering to software.")
    + quote("Fritz Bauer (Garmisch 1968): The establishment and use of sound engineering principles in order to obtain economically software that is reliable and works efficiently on real machines.")
    + table(["Dimension", "Computer Science", "Software Engineering", "الفرق"], [
        ["Focus", "Theory, algorithms, formal logic", "Systematic development, lifecycle, quality", "نظرية مقابل تطوير ودورة حياة"],
        ["Success metric", "Complexity proofs, correctness", "Availability, maintainability, budget/schedule", "برهان مقابل خدامة/التزام"],
        ["Scale", "Individual algorithms/programs", "Large multi-person systems 10–20 years", "فرد مقابل أنظمة طويلة الأمد"],
        ["Constraints", "Compute/memory limits", "Cost, deadlines, incomplete requirements, humans", "كلفة ومواعيد ومتطلبات ناقصة"],
    ])
    + table(["Process activity", "Objective", "Work products", "النشاط"], [
        ["1 Specification", "Define capabilities & boundaries", "SRS ISO 29148", "المواصفات"],
        ["2 Development", "Spec → executable system", "Architecture, design, tested code", "التطوير"],
        ["3 Validation", "Prove user expectations met (V&V)", "Tests, acceptance, audits", "التحقق والتأكيد"],
        ["4 Evolution", "Adapt to change", "Refactor, migration, patches", "التطور"],
    ])))

parts.append(sec(7, "Software Crisis + IBM OS/360 + Brooks' Law + Myths", "7. أزمة البرمجيات + OS/360 + قانون بروكس + الخرافات",
    bi("Software Crisis term coined at NATO Science Committee conference, Garmisch 1968 — maintenance cost and failure rates exceeded hardware economics.",
        "مصطلح أزمة البرمجيات رُسمياً بمؤتمر NATO العلمي، غارميش 1968 — كلفة الصيانة والفشل فاقت منطق كلفة العتاد.")
    + table(["OS/360 fact", "Value", "القيمة"], [
        ["Effort", "> 5,000 man-years", "أكثر من 5000 رجل-سنة"],
        ["Cost", "> $50,000,000 (1960s)", "أكثر من 50 مليون دولار (ستينيات)"],
        ["Schedule", "Multi-year slip; thousands of known defects", "تأخير سنوات؛ آلاف العيوب المعروفة"],
    ])
    + callout("Brooks' Law", "قانون بروكس",
        "\"Adding human resources to a late software project makes it later.\" Reasons: onboarding drains seniors; communication channels grow C = N(N-1)/2.",
        "«إضافة بشر لمشروع متأخر تجعله أتأخر». الأسباب: تدريب الجدد يستهلك الخبراء؛ قنوات الاتصال تنمو C = N(N-1)/2.", "warn")
    + bi("Communication channels formula: C = N(N-1)/2. Example: N=5 → 10 channels; N=10 → 45 channels.",
        "صيغة قنوات الاتصال: C = N(N-1)/2. مثال: 5 أشخاص ← 10 قنوات؛ 10 أشخاص ← 45 قناة.")
    + table(["Myth category", "Myth", "Reality", "الخرافة/الواقع"], [
        ["Management", "Behind schedule? Hire more programmers", "Brooks' Law — more overhead/training drag", "التوظيف الزائد يزيد العبء"],
        ["Customer", "Vague objective OK; details later", "Ambiguous requirements → architectural rework", "غموض المتطلبات يسبب إعادة بناء"],
        ["Developer", "Code compiles/runs → job done", "Maintenance = 60–80% of lifecycle effort", "الصيانة 60–80% من الجهد"],
        ["Developer", "Working program is the only deliverable", "Code without docs = unmaintainable liability", "كود بلا توثيق = مسؤولية غير قابلة للصيانة"],
    ])))

parts.append(sec(8, "ACM/IEEE Code of Ethics — 8 principles", "8. مدونة أخلاقيات ACM/IEEE — 8 مبادئ",
    table(["#", "Principle", "Obligation", "الالتزام"], [
        ["1", "Public", "Consistent with public safety, health, welfare", "سلامة وصحة ورفاه الجمهور"],
        ["2", "Client and Employer", "Best interests, consistent with public interest", "مصلحة العميل/صاحب العمل موافقة للجمهور"],
        ["3", "Product", "Modifications meet highest professional standards", "تعديلات المنتج بمعايير مهنية عالية"],
        ["4", "Judgment", "Professional objectivity, integrity, independence", "موضوعية ونزاهة واستقلال"],
        ["5", "Management", "Promote ethical development & maintenance", "تعزيز نهج أخلاقي بالتطوير والصيانة"],
        ["6", "Profession", "Advance integrity and reputation of SE", "سمعة ونزاهة المهنة"],
        ["7", "Colleagues", "Fair, transparent, supportive to peers", "عدل وشفافية ودعم الزملاء"],
        ["8", "Self", "Lifelong learning; promote ethical practice", "تعلم مدى الحياة وممارسة أخلاقية"],
    ])
    + callout("Memory cue", "مرساة الحفظ",
        "Public · Client/Employer · Product · Judgment · Management · Profession · Colleagues · Self",
        "الجمهور · العميل/الجهة · المنتج · الحكم/الاستقلالية · الإدارة · المهنة · الزملاء · الذات", "ok")))

parts.append(sec(9, "Hard points Dr. Ali likes (difficult / easy to mix)", "9. نقاط صعبة يحبها د. علي (سهلة الخلط)",
    callout("H1 — Error vs Fault vs Failure", "H1 — خطأ مقابل عيب مقابل فشل",
        "Error = human cognitive mistake. Fault/Defect = static flaw in artifact. Error state = invalid runtime state. Failure = observable deviation. Scenario MCQs map stages in that order.",
        "Error = خطأ معرفي بشري. Fault = عيب ثابت بالمنتج. Error state = حالة داخلية خاطئة. Failure = انحراف مرصود. أسئلة السيناريو ترتيبها هكذا.", "warn")
    + callout("H2 — Essential vs Accidental", "H2 — جوهري مقابل عرضي",
        "Invisibility & conformity are ESSENTIAL (not tool problems). Slow compile & assembly syntax are ACCIDENTAL. AI mostly reduces accidental complexity.",
        "الخفاء والتوافقية جوهريان (مو مشكلة أدوات). بطء التجميع وصعوبة Assembly عرضية. الذكاء الاصطناعي غالباً يقلل العرضي.", "warn")
    + callout("H3 — Patriot arithmetic", "H3 — حساب الباتريوت",
        "Know the chain: 0.1 s → 24-bit truncation → ~9.5e-8 per tick → 100 h → 0.3433 s → Mach 5 → ~687 m gate shift. Inconsistent 48-bit vs 24-bit maintenance is a key lesson.",
        "اعرف السلسلة: 0.1 ثانية ← قطع 24-bit ← خطأ كل نبضة ← 100 ساعة ← 0.3433 ثانية ← ماخ 5 ← ~687 متر. الصيانة غير المتسقة 48 مقابل 24 بت درس أساسي.", "calc")
    + callout("H4 — Software is not just code", "H4 — البرمجية مو بس كود",
        "Master's definition: Programs + Data Structures + Documentation. Missing docs = unmaintainable liability.",
        "تعريف الماجستير: برامج + هياكل بيانات + توثيق. غياب التوثيق = مسؤولية غير قابلة للصيانة.", "rule")
    + callout("H5 — CS vs SE", "H5 — علوم الحاسوب مقابل الهندسة",
        "CS: theory/algorithms/correctness proofs. SE: lifecycle, quality, cost, deadlines, people, incomplete requirements.",
        "علوم: نظرية وخوارزميات وبراهين. هندسة: دورة حياة وجودة وكلفة ومواعيد وبشر ومتطلبات ناقصة.", "rule")
    + callout("H6 — Brooks' Law formula", "H6 — صيغة قانون بروكس",
        "C = N(N-1)/2 communication channels. Adding people late → more channels + training drag → later delivery.",
        "C = N(N-1)/2 قنوات اتصال. إضافة أشخاص للمتأخر ← قنوات أكثر + عبء تدريب ← تسليم أبطأ.", "calc")))

parts.append(sec(10, "Viva / exam simulation from the note", "10. محاكاة امتحان/شفوي من الملاحظة",
    bi("Scenario: flight control module OK at cruise; supersonic dive + thermal stress → 16-bit accumulator overflow → stabilizer locks. Correct IEEE/Laprie mapping?",
        "سيناريو: وحدة تحكم طيران سليمة بالانطلاق؛ غطس فوق صوتي + إجهاد حراري ← تجاوز مكدس 16-bit ← تجمّد مثبت الأفقي. التصنيف الصحيح IEEE/Laprie؟")
    + bi("Correct answer pattern (from note Q1): developer's wrong variable sizing = Error; dormant 16-bit declaration = Fault/Defect; runtime wrong value = error state; stabilizer lockup = Failure.",
        "نمط الجواب الصحيح (س1 بالملاحظة): اختيار المطوّر الخاطئ لحجم المتغير = Error؛ التعريف الساكن 16-bit = Fault؛ القيمة الخاطئة وقت التشغيل = error state؛ تجمد المثبت = Failure.")
    + bi("Oral prompt: explain why No Silver Bullet means GenAI/cloud cannot fully erase the software crisis — they target accidental complexity; essential remains.",
        "سؤال شفوي: فسّر لماذا «لا رصاصة فضية» تعني أن GenAI/السحابة لا يمحوان الأزمة كلياً — يهاجمان العرضي والجوهر يبقى.")))

parts.append(sec(11, "Morning checklist — ASE W01", "11. قائمة صباحية — ASE الأسبوع الأول",
    table(["Must know", "Details", "لازم تحفظ"], [
        ["SE definition IEEE 610.12", "systematic, disciplined, quantifiable approach", "تعريف IEEE كامل"],
        ["Bauer 1968", "sound engineering principles; economic reliable software", "تعريف باور"],
        ["Tripartite software", "Programs + Data Structures + Documentation", "الثلاثي"],
        ["Process 4 activities", "Spec → Develop → Validate → Evolve", "أربع نشاطات"],
        ["CS vs SE", "4 dimensions", "الفرق بأربع أبعاد"],
        ["Patriot numbers", "0.1s · 24-bit · 0.3433s · 687m · 28 killed", "أرقام الباتريوت"],
        ["Dependability chain", "Error → Fault → Error state → Failure", "سلسلة الاعتمادية"],
        ["Brooks essential 4", "Complexity, Conformity, Changeability, Invisibility", "الجوهري الأربعة"],
        ["Accidental examples", "syntax, tools, memory/GC", "العرضي"],
        ["Brooks' Law + C formula", "adding people late; N(N-1)/2", "القانون والصيغة"],
        ["OS/360", "5000 man-years; $50M+; defects", "أرقام OS/360"],
        ["Software crisis", "NATO Garmisch 1968", "غارميش 1968"],
        ["4 myth groups", "Management, Customer, Developer ×2", "الخرافات"],
        ["Ethics 8 principles", "Public … Self", "ثمانية مبادئ"],
    ])
    + bi("Related vault files: full note MD/DOCX · seminar PPTX/PDF · diagrams patriot/dependability/brooks · Quiz_01_Software_Crisis.json · four textbooks in 02_Raw_Materials.",
        "ملفات الفولدر: ملاحظة كاملة · سمينار PPTX/PDF · رسومات الباتريوت والاعتمادية وبروكس · كويز JSON · الكتب الأربعة.")))

# Fix accidental formula leftover - I had a bug with formula := ""
# Rebuild HTML without that broken expression - already in parts if formula was empty string joined

html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8"/>
<title>ASE Week 01 — Foundations & Software Crisis</title>
<style>
@page {{ size: A4; margin: 13mm 11mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: "Segoe UI", Tahoma, Arial, sans-serif; color:#1f2937; margin:0; line-height:1.45; font-size:10.5pt; background:#fff; }}
.cover {{ page-break-after:always; text-align:center; padding:22mm 8mm 8mm; border:2px solid #1e3a8a; }}
.badge {{ display:inline-block; background:#1e3a8a; color:#fff; padding:6px 14px; border-radius:999px; font-size:10pt; font-weight:700; margin-bottom:12px; }}
h1 {{ color:#1e3a8a; font-size:22pt; margin:6px 0; }}
h1.ar-t {{ color:#0f766e; font-size:18pt; margin:0 0 10px; }}
.sub.en {{ color:#1e3a8a; font-weight:600; margin:2px 0; }}
.sub.ar {{ color:#0f766e; margin:2px 0; }}
.note {{ margin-top:14px; font-size:9.5pt; color:#4b5563; }}
.sec {{ margin:0 0 10px; }}
h2 {{ font-size:12.5pt; color:#fff; background:#1e3a8a; margin:14px 0 8px; padding:7px 10px; border-radius:6px; display:flex; flex-direction:column; gap:2px; }}
h2 .ar {{ font-size:11pt; color:#a7f3d0; font-weight:600; }}
.en {{ direction:ltr; text-align:left; unicode-bidi:plaintext; }}
.ar {{ direction:rtl; text-align:right; unicode-bidi:plaintext; font-family:Tahoma,Arial,sans-serif; }}
.bi {{ margin:4px 0 7px; }}
p.en {{ margin:2px 0; color:#111827; }}
p.ar {{ margin:2px 0; color:#374151; }}
.q {{ direction:ltr; text-align:left; unicode-bidi:plaintext; background:#f1f5f9; border-right:3px solid #64748b; padding:6px 8px; margin:4px 0; font-size:9.5pt; }}
table {{ width:100%; border-collapse:collapse; margin:6px 0 10px; font-size:9pt; page-break-inside:avoid; }}
th {{ background:#1e3a8a; color:#fff; padding:5px 6px; border:1px solid #1e3a8a; font-weight:700; }}
td {{ border:1px solid #d1d5db; padding:4px 6px; vertical-align:top; }}
tr:nth-child(even) td {{ background:#f8fafc; }}
.callout {{ border-right:4px solid #b91c1c; background:#fef2f2; padding:7px 9px; margin:7px 0; border-radius:0 8px 8px 0; page-break-inside:avoid; }}
.callout.ok {{ border-right-color:#0f766e; background:#ecfdf5; }}
.callout.calc {{ border-right-color:#92400e; background:#fffbeb; }}
.callout.rule {{ border-right-color:#1e3a8a; background:#eff6ff; }}
.ct {{ margin-bottom:3px; font-weight:700; }}
.ct .en {{ color:#b91c1c; display:block; }}
.ct .ar {{ color:#991b1b; display:block; }}
.callout.ok .ct .en, .callout.ok .ct .ar {{ color:#0f766e; }}
.callout.calc .ct .en, .callout.calc .ct .ar {{ color:#92400e; }}
.callout.rule .ct .en, .callout.rule .ct .ar {{ color:#1e3a8a; }}
</style>
</head>
<body>
<header class="cover">
<div class="badge">CS603 · ASE Lecture 01 · w01</div>
<h1>Advanced Software Engineering — Week 01</h1>
<h1 class="ar-t">هندسة البرمجيات المتقدمة — المحاضرة الأولى</h1>
<p class="sub en">Foundations · Software Crisis · Patriot · Brooks · Ethics</p>
<p class="sub ar">الأسس · أزمة البرمجيات · الباتريوت · بروكس · الأخلاقيات</p>
<p class="sub en">Comprehensive bilingual study pack (EN + AR) — FULL, not compressed</p>
<p class="sub ar">حزمة مراجعة شاملة ثنائية اللغة — كاملة بلا اختصار</p>
<p class="sub en">Instructor: Asst. Prof. Dr. Ali Fahim Ni'ma</p>
<p class="sub ar">الدكتور: أ.م.د. علي فاهم نعمة</p>
<p class="note en">Built from vault lecture note + syllabus + doctor profile · textbooks listed in Raw_Materials<br/>For morning review · Koko · 2026-09-20</p>
<p class="note ar">مبني على ملاحظة المحاضرة والسيلبس وبروفايل الدكتور — الكتب بمجلد Raw_Materials<br/>لمذاكرة الصباح — كوكو</p>
</header>
{''.join(parts)}
<div class="callout ok">
<div class="ct"><span class="en">Coverage check</span><span class="ar">فحص التغطية</span></div>
<p class="en">Textbooks · evolving software · dual role · socio-technical · dependability chain · Patriot kinematics · Brooks essential/accidental · tripartite software · IEEE/Bauer SE defs · CS vs SE · 4 process activities · crisis NATO 1968 · OS/360 · Brooks' Law + C formula · 4 myths · 8 ethics · hard points · viva scenario · morning checklist — ALL included.</p>
<p class="ar">المصادر · تطور البرمجيات · الدور المزدوج · الاجتماعي-التقني · سلسلة الاعتمادية · حركيات الباتريوت · بروكس جوهري/عرضي · الثلاثي · تعريفات IEEE/باور · CS مقابل SE · أربع نشاطات · الأزمة 1968 · OS/360 · قانون بروكس · الخرافات · 8 أخلاقيات · نقاط صعبة · شفوي · قائمة صباحية — كلها موجودة.</p>
</div>
</body>
</html>'''

out = OUT_DIR / "w01-ase-foundations-crisis-bilingual.html"
out.write_text(html, encoding="utf-8")
print("html", out, out.stat().st_size)
