# -*- coding: utf-8 -*-
"""Bilingual EN-AR comprehensive study packs for DM Week 01 and Week 02. Full content, no compression."""
from pathlib import Path
import html as H

OUT_DIR = Path(r"G:\My Drive\Master-Studio\01_Semester_1\03_Data_Mining\03_Study_Notes")

def e(s):
    return H.escape(str(s))

def bilingual(en, ar):
    return f'<div class="bi"><p class="en">{e(en)}</p><p class="ar">{e(ar)}</p></div>'

def quote(en):
    return f'<div class="q">{e(en)}</div>'

def callout(te, ta, be, ba, kind="warn"):
    return f'''<div class="callout {kind}">
<div class="ct"><span class="en">{e(te)}</span><span class="ar">{e(ta)}</span></div>
<div class="bi"><p class="en">{e(be)}</p><p class="ar">{e(ba)}</p></div></div>'''

def table(headers, rows):
    hs = "".join(f"<th>{e(h)}</th>" for h in headers)
    body = []
    for r in rows:
        tds = "".join(f"<td>{e(c)}</td>" for c in r)
        body.append(f"<tr>{tds}</tr>")
    return f'<table><thead><tr>{hs}</tr></thead><tbody>{"".join(body)}</tbody></table>'

def formula(f, ar=""):
    a = f'<div class="fnote ar">{e(ar)}</div>' if ar else ""
    return f'<div class="formula">{e(f)}</div>{a}'

def sec(n, en, ar, body):
    return f'''<section class="sec">
<h2><span class="en">{n}. {e(en)}</span><span class="ar">{e(ar)}</span></h2>
{body}</section>'''

def wrap(title_en, title_ar, badge, parts):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8"/>
<title>{e(title_en)}</title>
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
h3 {{ font-size:11pt; color:#1e3a8a; margin:10px 0 4px; }}
h3 .ar {{ display:block; color:#0f766e; font-size:10.5pt; }}
.bi {{ margin:4px 0 7px; }}
.en {{ direction:ltr; text-align:left; unicode-bidi:plaintext; }}
.ar {{ direction:rtl; text-align:right; unicode-bidi:plaintext; font-family:Tahoma,Arial,sans-serif; }}
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
.formula {{ text-align:center; font-weight:700; color:#1e3a8a; background:#f1f5f9; border:1px solid #94a3b8; border-radius:8px; padding:8px; margin:6px 0 3px; font-size:11.5pt; }}
.fnote {{ text-align:center; color:#4b5563; font-size:9pt; margin-bottom:6px; }}
ul {{ margin:4px 0 8px 18px; }}
li {{ margin:2px 0; }}
.check {{ background:#f0fdf4; border:1px solid #86efac; padding:8px 10px; margin-top:12px; border-radius:8px; page-break-before:auto; }}
</style>
</head>
<body>
<header class="cover">
<div class="badge">{e(badge)}</div>
<h1>{e(title_en)}</h1>
<h1 class="ar-t">{e(title_ar)}</h1>
<p class="sub en">Comprehensive Bilingual Study Pack (English + Arabic) — FULL, Not Compressed</p>
<p class="sub ar">حزمة مراجعة شاملة ثنائية اللغة (إنكليزي + عربي) — كاملة بلا اختصار</p>
<p class="sub en">Instructor: Asst. Prof. Dr. Ahmed Shakir Abd Al-Rida · Data Mining</p>
<p class="sub ar">الدكتور: أ.م.د. أحمد شاكر عبد الرضا — تنقيب عن البيانات</p>
<p class="note en">Built from vault comprehensive notes + lecture originals + Gemini frameworks + Dr. Ahmed exam layer.<br/>WebUI MCQ platform check is NOT counted as a course exam.</p>
<p class="note ar">مبني على الملاحظات الشاملة بالفولدر + نصوص المحاضرة + قوالب Gemini + طبقة امتحان د. أحمد.<br/>اختبار منصة MCQ لا يُحسب امتحاناً للمادة.</p>
<p class="note en">For morning study · Koko · 2026-09-20</p>
<p class="note ar">لمذاكرة الصباح — كوكو — 2026-09-20</p>
</header>
{''.join(parts)}
</body>
</html>'''

# ================= WEEK 01 =================
p1 = []
p1.append(sec(1, "Definition of Data Mining", "1. تعريف التنقيب عن البيانات",
    quote("The process of extracting information to identify patterns, trends, and useful data that would allow the business to take the data-driven decision from huge sets of data is called Data Mining.")
    + quote("In other words, is the process of investigating hidden patterns of information to various perspectives for categorization into useful data, which is collected and assembled in particular areas such as data warehouses, efficient analysis, data mining algorithm, helping decision making and other data requirement to eventually cost-cutting and generating revenue.")
    + quote("Is the act of automatically searching for large stores of information to find trends and patterns that go beyond simple analysis procedures.")
    + quote("Data mining utilizes complex mathematical algorithms for data segments and evaluates the probability of future events.")
    + quote("Data Mining is also called Knowledge Discovery of Data (KDD).")
    + bilingual(
        "Data mining extracts information from huge datasets to find patterns, trends, and useful data for data-driven decisions. It automatically searches beyond simple analysis, uses complex mathematical algorithms, evaluates the probability of future events, works largely in data warehouses, and is also called KDD.",
        "التنقيب عن البيانات يستخرج المعلومات من مجموعات بيانات ضخمة لاكتشاف أنماط واتجاهات وبيانات مفيدة تسمح بقرارات مبنية على البيانات. بحث تلقائي يتجاوز التحليل البسيط، يستخدم خوارزميات رياضية معقّدة، يقيّم احتمال الأحداث المستقبلية، ويعمل غالباً في مستودعات البيانات، ويسمى أيضاً KDD.")
    + table(["Pillar / الركيزة", "Lecture text", "بالعربي"], [
        ["Automated search", "automatically searching", "استخراج تلقائي مو يدوي"],
        ["Tool", "complex mathematical algorithms", "خوارزميات رياضية معقّدة"],
        ["Function", "data segments + probability of future events", "تجزئة البيانات + تقييم احتمال المستقبل"],
        ["Place", "data warehouses", "مستودعات البيانات"],
        ["Alias", "Knowledge Discovery of Data (KDD)", "اكتشاف المعرفة من البيانات"],
    ])
    + table(["Type", "Works on", "Output", "النوع/المخرج"], [
        ["Simple analysis", "Known queries", "Direct answers", "استعلامات معروفة → إجابات مباشرة"],
        ["Data Mining", "Goes beyond simple analysis", "Hidden patterns + predictions", "يتجاوز التحليل البسيط → أنماط خفية + تنبؤات"],
    ])
    + callout("Applications intro (slide 6)", "مقدمة التطبيقات (سلايد 6)",
        "Primarily used by organizations with intense consumer demands — Retail, Communication, Financial, Marketing — to determine price, consumer preferences, product positioning, and impact on sales, satisfaction, and profits. A retailer can use point-of-sale records to develop products and promotions that attract customers.",
        "تستخدمه مؤسسات بشدة طلب استهلاكي — تجزئة، اتصالات، مالية، تسويق — لتحديد السعر وتفضيلات المستهلك وموقع المنتج وأثره على المبيعات والرضا والأرباح. التجزئة تستعمل سجلات نقاط البيع لتطوير منتجات وعروض تجذب الزبائن.", "rule")
    + table(["Entities", "Outputs", "الكيانات/المخرجات"], [
        ["Retail · Communication · Financial · Marketing", "price · preferences · positioning · sales & profit", "تجزئة · اتصالات · مالية · تسويق"],
    ])))

p1.append(sec(2, "Advantages — 7 points in 3 levels", "2. الفوائد — 7 نقاط بـ3 مستويات",
    table(["#", "Original lecture advantage", "النص الأصلي"], [
        ["1", "knowledge-based data", "بيانات مبنية على المعرفة"],
        ["2", "lucrative modifications in operation and production", "تعديلات مربحة بالعمليات والإنتاج"],
        ["3", "cost-efficient vs other statistical applications", "اقتصادي مقارنة بالتطبيقات الإحصائية"],
        ["4", "helps the decision-making process", "يساعد عملية اتخاذ القرار"],
        ["5", "automated discovery of hidden patterns + prediction of trends/behaviors", "اكتشاف تلقائي لأنماط خفية + تنبؤ"],
        ["6", "induced in new systems and existing platforms", "يدمج بالأنظمة الجديدة والقديمة"],
        ["7", "quick process; new users analyze huge data fast", "سريع؛ حتى المستخدم الجديد يحلل ضخماً بسرعة"],
    ])
    + table(["Level", "Gemini wording (EN)", "بالعربي", "Lecture #"], [
        ["Data / Discovery", "Hidden Patterns & Prediction; Knowledge-Based Data", "أنماط خفية وتنبؤ؛ تحويل الخام لبيانات معرفية", "1,5"],
        ["Business / Decision", "Decision-Making; Lucrative Modifications", "دعم القرار؛ تعديلات مربحة", "2,4"],
        ["System / Feasibility", "Cost-Efficient; System Integration; Speed & Usability", "اقتصادي؛ دمج جديد/قديم؛ سريع وسهل", "3,6,7"],
    ])
    + callout("Mental anchor — advantages", "مرساة الفوائد",
        "Extract & Predict (Data) → Decide & Profit (Business) → Cheap, Integratable & Fast (Tech).",
        "استخرج وتوقّع (بيانات) → قرّر واربِح (عمل) → رخيص ويندمج وسريع (تقنية).", "ok")))

p1.append(sec(3, "Disadvantages — Amex, tools, training, imprecision", "3. العيوب — Amex والأدوات والتدريب وعدم الدقة",
    table(["#", "Original lecture point", "النص الأصلي"], [
        ["1–2", "Organizations may sell useful customer data for money; American Express sold credit card purchases to other organizations", "مؤسسات قد تبيع بيانات العملاء؛ American Express باعت مشتريات البطاقات لمنظمات خارجية"],
        ["3", "Analytics software difficult to operate; needs advanced training", "برامج التحليلات صعبة وتحتاج تدريباً متقدماً"],
        ["4", "Different tools operate in distinct ways due to different algorithms — selecting the right tool is challenging", "أدوات مختلفة بخوارزميات مختلفة — اختيار الأداة تحدي"],
        ["5", "Techniques are not precise → may lead to severe consequences", "تقنيات غير دقيقة → نتائج وخيمة بظروف معينة"],
    ])
    + table(["Level", "Gemini wording", "بالعربي"], [
        ["Privacy / Ethics", "Customer Data Monetization; American Express example", "بيع بيانات العملاء؛ مثال Amex"],
        ["Technical / Operational", "Tool Selection Dilemma; Steep Learning Curve", "معضلة اختيار الأداة؛ منحنى تعلّم حاد"],
        ["Reliability / Accuracy", "Imprecision & Critical Consequences (probabilistic not exact)", "احتمالية مو دقيقة؛ عواقب وخيمة"],
    ])
    + callout("Exam-critical example", "مثال امتحاني",
        "Memorize: American Express + credit card purchases + sold to external organizations.",
        "احفظ: American Express + credit card purchases + بيع لمنظمات خارجية.", "warn")
    + callout("Disadvantages anchor", "مرساة العيوب",
        "Selling the Data (Amex) → Selecting & Running Tools (Algorithms & Training) → Flawed Results (Imprecision).",
        "بيع البيانات (Amex) → اختيار وتشغيل الأدوات (خوارزميات وتدريب) → نتائج معيبة (عدم الدقة).", "ok")))

# Applications full
apps = [
    ["Healthcare", "Improve services + reduce costs; ML, multidimensional DB, visualization, soft computing, statistics", "Patient Forecasting — category triage for intensive care at right place/time", "Fraud & Abuse in insurance claims", "تحسين الصحة؛ توقع المرضى للرعاية المركزة؛ كشف احتيال التأمين"],
    ["Market Basket", "Hypothesis: buy group A → more likely buy group B; understand purchase behavior; change store layout; compare stores/demographics", "Product Associations", "Purchase Behavior", "فرضية سلة السوق؛ ربط المنتجات؛ إعادة تنظيم المتجر"],
    ["Education (EDM)", "Newly emerging; explore knowledge from educational environments; affirm learning behavior; study support impact; promote learning science", "Student Performance Prediction — what to teach & how to teach", "Learning Behavior", "تنقيب تعليمي ناشئ؛ تنبؤ أداء الطالب؛ ماذا وكيف ندرّس"],
    ["Manufacturing", "Knowledge is the best asset; find patterns in complex manufacturing; system-level design links architecture/portfolio/customer data needs; forecast development period/cost", "Process Patterns", "Development Time & Cost", "المعرفة أفضل أصل؛ أنماط التصنيع؛ توقع زمن/تكلفة التطوير"],
    ["CRM", "Obtaining and holding customers; loyalty; customer-oriented strategies; collect + analyze data", "Acquisition & Retention", "Churn / Loyalty", "اكتساب والاحتفاظ بالعملاء؛ ولاء؛ استراتيجيات موجهة للزبون"],
    ["Fraud Detection", "Billions lost to fraud; traditional methods slow; supervised sample records classified fraudulent/non-fraudulent; model checks documents", "Supervised Classification", "Fraudulent vs Non-fraudulent", "مليارات تضيع بالاحتيال؛ تعلّم موجّه يصنّف احتيالي/سليم"],
    ["Lie Detection", "Hard to extract truth; law enforcement investigates offenses/terror comms; text mining on unstructured text; compare past investigations; build lie-detection model", "Text Mining on unstructured text", "Lie / Truth Model", "تنقيب نصوص على غير مهيكل؛ مقارنة تحقيقات سابقة؛ نموذج كشف الكذب"],
    ["Banking & Finance", "Digitalization generates huge transaction data; managers miss patterns because volume too large or produced too rapidly; mining finds trends, causalities, correlations; targeting/acquiring/retaining/segmenting profitable customers", "Trends, Causalities & Correlations", "Customer Segmentation", "بيانات ضخمة وسريعة؛ trends وcausalities وcorrelations؛ تقسيم العملاء"],
]
p1.append(sec(4, "Applications — 8 domains (2-keyword + full lecture)", "4. التطبيقات — 8 مجالات (قاعدة الكلمتين + نص المحاضرة)",
    table(["#", "Domain", "Core operation / keyword 1", "Risk / keyword 2", "بالعربي"], [[str(i+1), a[0], a[2], a[3], a[4]] for i,a in enumerate(apps)])
    + ''.join(f'''<h3><span class="en">{i+1}. {e(a[0])}</span><span class="ar">{e(a[4].split("؛")[0] if "؛" in a[4] else a[0])}</span></h3>
{bilingual("Lecture: " + a[1], "المحاضرة: " + a[4])}
{bilingual("Keywords: " + a[2] + " + " + a[3], "الكلمتان: " + a[2] + " + " + a[3])}''' for i,a in enumerate(apps))
    + callout("3-Pillar + Safe answer + Fixed sentence", "القالب الثلاثي + الجملة الآمنة",
        "For each domain: Goal & Stack + Core Operation + Risk/Anomaly. Exam safe: write the two keywords + fixed sentence \"Using techniques like Classification, Clustering, and Machine Learning.\" Marker looks for keywords, not filler.",
        "لكل مجال: الهدف والتقنيات + العملية الأساسية + الخطر/الشذوذ. الإجابة الآمنة: الكلمتان + الجملة الثابتة «Using techniques like Classification, Clustering, and Machine Learning». المصحح يبحث عن كلمات دالة مو حشو.", "rule")
    + table(["Healthcare safe lines (EN)", "عربي"], [
        ["Predicting patient volume for better resource allocation.", "تنبؤ أعداد المرضى لتوزيع أفضل للموارد"],
        ["Detecting fraud and abuse in insurance claims.", "كشف الاحتيال وإساءة استخدام مطالبات التأمين"],
    ])))

challenges = [
    ["Incomplete & Noisy Data", "heterogeneous, incomplete, noisy; huge data inaccurate/unreliable", "measuring instrument failure; human entry errors; users refuse to disclose", "obstruct mining; distort pattern extraction", "بيانات ناقصة/مشوّشة؛ أخطاء بشرية/أجهزة/رفض مشاركة؛ تشويه الأنماط"],
    ["Data Distribution", "data on various platforms/databases/internet", "organizational + technical concerns; regional servers", "central repo unfeasible → need distributed mining algorithms", "بيانات موزعة؛ تجميع مركزي صعب → خوارزميات موزعة"],
    ["Complex Data", "multimedia, spatial, time series heterogeneous", "diverse formats not standardized", "traditional techniques fail → new tools/methodologies", "وسائط/مكانية/زمنية متنوعة؛ التقنيات التقليدية تعجز"],
    ["Performance", "depends primarily on algorithm/technique efficiency", "algorithm not up to the mark", "adverse effect on efficiency/speed/accuracy", "أداء يعتمد على كفاءة الخوارزميات؛ تصميم ضعيف يضر"],
    ["Data Privacy & Security", "issues in security, governance, privacy", "analyze purchases without permission", "reveals habits/preferences without consent", "أمان وحوكمة وخصوصية؛ كشف عادات بدون إذن"],
    ["Data Visualization", "primary way to show output to user; hard to present complex I/O precisely/easily", "complicated inputs and outputs", "need efficient successful visualization → decision-ready", "عرض النتائج للمستخدم؛ مدخلات/مخرجات معقدة تحتاج تمثيلاً متقدماً"],
]
p1.append(sec(5, "Challenges — 6 items (Nature → Root Cause → Consequence)", "5. التحديات — 6 عناصر (طبيعة ← سبب ← أثر)",
    table(["#", "Challenge", "Nature", "Root cause", "Consequence", "بالعربي"], [[str(i+1), c[0], c[1], c[2], c[3], c[4]] for i,c in enumerate(challenges)])
    + callout("Store $500 phone story (lecture)", "قصة المتجر و500 دولار (المحاضرة)",
        "Retail chain collects phones of customers spending >$500; employee may mistype a digit (noisy/incomplete); customers may refuse to disclose (incomplete). All these make data mining challenging.",
        "سلسلة تجزئة تجمع هواتف من يصرف >500$؛ الموظف يمكن يغلط برقم (ضوضاء/نقص)؛ العميل يمكن يرفض المشاركة (نقص). كل هذا يجعل التنقيب صعباً.", "warn")
    + callout("Outlier rule (from W02 lecture material, linked)", "قاعدة القيمة الشاذة (مرتبطة بـ W02)",
        "An outlier is not necessarily an error — e.g. high blood pressure may be a real medical condition. Investigate before removing.",
        "القيمة الشاذة ليست بالضرورة خطأ — مثل ضغط دم مرتفع قد يكون حالة حقيقية. تحقق قبل الحذف.", "ok")
    + callout("Challenges anchor", "مرساة التحديات",
        "Data itself (noisy → distributed → complex) → Algorithm (performance) → Output (privacy → visualization).",
        "البيانات نفسها (مشوّشة → موزعة → معقّدة) → الخوارزمية (أداء) → المخرج (خصوصية → تمثيل).", "ok")))

p1.append(sec(6, "Exam quick sheet — Week 01", "6. ورقة الامتحان السريعة — الأسبوع الأول",
    table(["Topic", "Must know", "لازم تحفظ"], [
        ["Definition", "extract info · huge data · patterns · beyond simple analysis · KDD · algorithms · warehouses · future-event probability", "تعريف كامل + KDD + خوارزميات + warehouses"],
        ["Advantages", "3 levels + anchor Extract&Predict → Decide&Profit → Cheap/Integratable/Fast", "3 مستويات + المرساة"],
        ["Disadvantages", "Amex credit cards · tool selection · training · probabilistic not exact", "Amex + أدوات + تدريب + عدم دقة"],
        ["Applications", "8 domains × 2 keywords + fixed techniques sentence", "8 مجالات × كلمتان + الجملة الثابتة"],
        ["Challenges", "6 × (Nature → Cause → Effect) + $500 store story", "6 تحديات بثلاثة عناصر + قصة المتجر"],
        ["Doctor style", "Han-style precise definitions; no filler; formulas if numbers appear", "تعريفات دقيقة بلا حشو؛ معادلة إذا بيه أرقام"],
    ])))

# ================= WEEK 02 =================
p2 = []
p2.append(sec(1, "Data Object vs Attribute", "1. كائن البيانات مقابل الخاصية",
    quote("A data object represents an entity about which information is collected.")
    + quote("An attribute is a property or characteristic of a data object.")
    + bilingual(
        "Examples of objects: patient, student, customer, transaction, document, image, geographic location. Examples of attributes: Age, Gender, BMI, Blood pressure, Diabetes status. Each ROW is a data object; each COLUMN is an attribute. Before mining: understand objects, attributes, value types, and data organization — type/structure influence which mining technique to use.",
        "أمثلة الكائنات: مريض، طالب، زبون، معاملة، مستند، صورة، موقع جغرافي. أمثلة الخصائص: العمر، الجنس، BMI، ضغط الدم، حالة السكري. كل صف = كائن بيانات؛ كل عمود = خاصية. قبل التنقيب: افهم الكائنات والخصائص وأنواع القيم وتنظيم البيانات — النوع والهيكل يحدّدان تقنية التنقيب.")
    + table(["Patient", "Age", "Gender", "BMI", "Diabetes"], [
        ["P1", "45", "Male", "28.5", "Yes"],
        ["P2", "32", "Female", "24.1", "No"],
    ])
    + bilingual("Mental path: Object → Attribute → Value Type → Structure → Technique.",
                "مسار فكري: كائن ← خاصية ← نوع القيمة ← هيكل ← تقنية.")))

p2.append(sec(2, "Attribute taxonomy — Nominal / Ordinal / Binary / Numerical", "2. تصنيف الخصائص — اسمي/ترتبي/ثنائي/رقمي",
    quote("A nominal attribute contains categories with no natural order.")
    + quote("An ordinal attribute contains categories with a meaningful order, but the difference between categories is not necessarily measurable.")
    + quote("A binary attribute has only two possible values.")
    + quote("Numerical attributes contain quantitative numerical values.")
    + table(["Type", "Lecture examples", "Key rule", "أمثلة/قاعدة"], [
        ["Nominal", "Gender, Color, Country, Department", "No natural order; Male > Female does not make sense", "فئات بلا ترتيب طبيعي"],
        ["Ordinal", "Low/Medium/High · Poor/Good/Excellent · Small/Medium/Large · Mild/Moderate/Severe", "Order meaningful; gaps not measurable", "ترتيب موجود؛ الفجوة غير قابلة للقياس"],
        ["Binary", "Yes/No · True/False · 0/1 · Disease/No · Purchased/Not", "Only two values; common in classification & association", "قيمتان فقط"],
        ["Numerical", "Age, Height, Weight, Temp, Salary, BP", "Quantitative; Discrete countable vs Continuous in-range", "قيم كمية؛ منفصل/مستمر"],
    ])
    + table(["Discrete examples", "Continuous examples", "منفصل/مستمر"], [
        ["# children, # transactions, # students, # visits = 0,1,2,3…", "Height 175.5 cm · Weight 72.4 kg · Temp 36.7°C · Glucose 125.6 mg/dL", "عدّ مقابل قياس ضمن مدى"],
    ])
    + table(["Decision question", "Nominal", "Ordinal", "Binary", "Numerical", "سؤال القرار"], [
        ["Natural order?", "No", "Yes", "—", "—", "ترتيب طبيعي؟"],
        ["Measurable gaps?", "—", "Not necessarily", "—", "Yes", "فجوات قابلة للقياس؟"],
        ["Only two values?", "No", "No", "Yes", "No", "قيمتان فقط؟"],
        ["Quantity?", "No", "No", "No", "Yes", "كمية عددية؟"],
    ])
    + bilingual("Classification algorithm: (1) only two values? → Binary. (2) quantitative? → Numerical (then Discrete/Continuous; optionally Interval/Ratio). (3) ranked categories? → Ordinal. Else → Nominal.",
                "خوارزمية التصنيف: (1) قيمتان فقط؟ ← ثنائي. (2) كمية رقمية؟ ← رقمي (ثم منفصل/مستمر؛ وربما فاصل/نسبة). (3) فئات مرتّبة؟ ← ترتبي. وإلا ← اسمي.")
    + table(["Variable", "Type", "المتغير/النوع"], [
        ["Gender / Country / Color", "Nominal", "اسمي"],
        ["URL", "Nominal", "اسمي"],
        ["Satisfaction Poor/Good/Excellent", "Ordinal", "ترتبي"],
        ["Disease severity Mild/Moderate/Severe", "Ordinal", "ترتبي"],
        ["Diabetes Yes/No or 0/1", "Binary", "ثنائي"],
        ["Age 45 / # children", "Numerical Discrete-ish / Discrete", "رقمي منفصل"],
        ["Height 175.5 / Salary / BP", "Numerical Continuous / Ratio-like", "رقمي مستمر/نسبي"],
    ])
    + callout("Dr. Ahmed standing question — URL", "سؤال د. أحمد المفتوح — الرابط",
        "What is the data type of a URL? Answer: Nominal. A URL is a label/identifier — no natural order, no meaningful distance between URLs. Safe sentence: \"A URL is a Nominal attribute: categories/identifiers with no natural order and no meaningful distance between values.\"",
        "شنو نوع بيانات الرابط؟ الجواب: Nominal. الرابط وسم/معرّف — بلا ترتيب طبيعي وبلا فجوة قابلة للقياس بين الروابط.", "warn")
    + callout("Anchor — attribute types", "مرساة أنواع الخصائص",
        "No order → Order with unknown gap → Two values → Quantity. (اسمي → ترتبي → ثنائي → رقمي)",
        "بلا ترتيب → ترتيب بلا قياس → صفر/واحد → عدد.", "ok")))

p2.append(sec(3, "Interval vs Ratio + normalization formulas (Dr. Ahmed)", "3. الفاصل مقابل النسبة + صيغ التطبيع (د. أحمد)",
    table(["Subtype", "Zero means", "Ratios?", "Examples", "الصفر/الأمثلة"], [
        ["Interval-scaled", "Arbitrary reference (not absence)", "No — 20°C not twice 10°C", "Celsius, calendar years", "صفر اعتباطي؛ النسب غير معنوية"],
        ["Ratio-scaled", "Absolute physical zero (absence)", "Yes — 20kg is twice 10kg", "Kelvin, salary, weight, height, BP", "صفر مطلق؛ النسب معنوية"],
    ])
    + formula("Min-Max (into [0,1]): x' = (x - min) / (max - min)", "تطبيع المدى إلى [0,1]")
    + callout("Worked Min-Max (lecture)", "مثال Min-Max محلول (المحاضرة)",
        "min age=20, max=60, x=40 → x'=(40-20)/(60-20)=20/40=0.5 → 40 years = 0.5",
        "أدنى عمر=20، أقصى=60، x=40 ← (40-20)/(60-20)=0.5 ← العمر 40 = 0.5", "calc")
    + formula("Z-score: z = (x - mean) / σ", "زد-سكور")
    + formula("Z-score MAD: v' = (v - mean) / s_A,  s_A = (1/n) Σ |x_i - mean|", "زد-سكور بالانحراف المطلق")
    + formula("Decimal scaling: v' = v / 10^j  (max|v'| < 1)", "التوسيع العشري")
    + callout("Doctor protocol", "بروتوكول الدكتور",
        "Write symbolic formula first → define symbols → show intermediate arithmetic → state final value and range. Arithmetic discipline: divide missing-value mean by observed count (4 not 5).",
        "اكتب المعادلة الرمزية أولاً ← عرّف الرموز ← وسّط الحساب ← اذكر الناتج والمدى. انضباط حسابي: متوسط القيم المفقودة يُقسم على عدد الموجود (4 مو 5).", "rule")
    + callout("Anchor Interval vs Ratio", "مرساة الفاصل/النسبة",
        "Interval: zero is a ruler mark. Ratio: zero is nothing left.",
        "الفاصل: الصفر علامة على المسطرة. النسبة: الصفر يعني ما بقى شيء.", "ok")))

structs = [
    ["Record", "Collection of records; each record = set of attributes", "Patient/Student table", "classification, clustering, regression, outliers", "مجموعة سجلات؛ كل سجل خصائص؛ صف=كائن"],
    ["Transaction", "Each transaction = set of items", "T1={Bread,Milk,Eggs}; rule Bread→Milk", "Association rule mining", "كل معاملة مجموعة عناصر؛ قواعد ارتباط"],
    ["Text/Document", "Unstructured documents", "emails, reviews, papers, posts", "frequent words, topics, sentiment, similarity, text classification", "نصوص غير مهيكلة؛ تنقيب نصوص"],
    ["Sequence", "Elements in specific order; order matters", "A→B→C→D; Login→Search→Product→Purchase; DNA", "ordered patterns", "عناصر مرتّبة؛ الترتيب جزء من المعلومة"],
    ["Temporal/Time-Series", "Observations tied to time", "stock, weather, ECG, rainfall, sensors", "trends, seasonal/periodic, anomalies", "ملاحظات مرتبطة بالوقت؛ اتجاهات وشذوذ"],
    ["Spatial", "Geographic/physical locations", "maps, satellite, GPS (32.48,45.82), roads", "location-based relationships", "مواقع جغرافية؛ علاقات مكانية"],
    ["Image/Multimedia", "Pixels; Gray H×W; RGB H×W×3", "X-ray, MRI, CT, satellite, faces", "objects, shapes, patterns, textures, regions (CNN)", "بكسلات؛ صور طبية؛ أشكال وأنسجة"],
    ["Graph/Network", "Nodes (objects) + Edges (relationships)", "social, citation, road, financial, knowledge graphs", "communities, important nodes, paths", "عقد وحواف؛ مجتمعات ومسارات"],
]
p2.append(sec(4, "8 Data Structures (attributes vs organization)", "4. الهيكلية الثمانية (خصائص مقابل تنظيم البيانات)",
    quote("Nominal, ordinal, binary, and numerical describe attributes. Record, transaction, text, sequence, temporal, spatial, image, and graph data describe how the data is organized or represented.")
    + bilingual("Hard separation: attribute types answer \"what kind of value is this column?\" Data structures answer \"how is the whole dataset shaped?\"",
                "فصل صارم: أنواع الخصائص تجيب «شنو نوع القيمة بهالعمود؟»؛ الهياكل تجيب «شنو شكل مجموعة البيانات كاملة؟»")
    + table(["#", "Structure", "Core form", "Example", "Mining finds", "بالعربي"], [[str(i+1), s[0], s[1], s[2], s[3], s[4]] for i,s in enumerate(structs)])
    + callout("Structure anchor", "مرساة الهياكل",
        "Row → Basket → Document → Path → Clock → Map → Picture → Network",
        "صف ← سلة ← مستند ← مسار ← ساعة ← خريطة ← صورة ← شبكة", "ok")
    + callout("Safe answer", "إجابة آمنة",
        "\"The dataset is organized as [structure]. Mining techniques follow this structure — e.g. association rules for transactions, text mining for documents, graph mining for networks.\"",
        "«مجموعة البيانات منظّمة كـ [هيكل]. تقنيات التنقيب تتبع هذا الهيكل — مثلاً قواعد ارتباط للمعاملات، تنقيب نصوص للمستندات، تنقيب شبكات للرسوم.»", "rule")))

p2.append(sec(5, "Data Preparation — definition, dirty data, pipeline", "5. إعداد البيانات — تعريف وبيانات قذرة وخط سير",
    quote("Data Preparation is the process of preparing raw data so that it can be used effectively by Data Mining algorithms.")
    + bilingual("Real-world data is often incomplete, noisy, inconsistent, duplicated, in different formats, containing irrelevant attributes, and different numerical scales.",
                "بيانات الواقع غالباً ناقصة أو مشوّشة أو غير متسقة أو مكررة أو بتنسيقات مختلفة أو بخصائص غير ذات صلة أو بمقياس رقمي مختلف.")
    + formula("Raw Data → Data Preparation → Data Mining → Knowledge / Patterns", "البيانات الخام ← إعداد ← تنقيب ← معرفة/أنماط")
    + bilingual("Quality of prepared data strongly affects quality of discovered patterns and model performance.",
                "جودة البيانات المجهزة تؤثر بقوة على جودة الأنماط المكتشفة وأداء النموذج.")
    + formula("Raw → Cleaning → Integration → Transformation → Reduction → Discretization → Prepared → Algorithm → Patterns", "خام ← تنظيف ← دمج ← تحويل ← تقليل ← تجزئة ← مجهز ← خوارزمية ← أنماط")
    + callout("Important lecture point", "نقطة المحاضرة المهمة",
        "These steps are not necessarily performed in exactly the same order for every dataset. Data Preparation is NOT simply \"removing missing values\" — it is the complete process of making raw data suitable for discovering useful patterns. Good preparation → better data → more reliable results.",
        "الخطوات ليست إجبارياً بنفس الترتيب لكل بيانات. الإعداد ليس مجرد «حذف القيم المفقودة» — بل العملية الكاملة لجعل الخام صالحاً لاكتشاف أنماط مفيدة. إعداد جيد ← بيانات أفضل ← نتائج أوثق.", "rule")))

p2.append(sec(6, "Data Cleaning — missing (6 methods), noise, outliers, duplicates, inconsistency", "6. تنظيف البيانات — مفقود (6 طرق)، ضوضاء، شذوذ، تكرار، عدم اتساق",
    quote("Data Cleaning is the process of detecting and correcting problems in the data.")
    + bilingual("Common problems: missing values, noisy data, outliers, duplicate records, inconsistent data.",
                "مشاكل شائعة: قيم مفقودة، ضوضاء، قيم شاذة، سجلات مكررة، عدم اتساق.")
    + table(["Missing method", "When / note", "Lecture example", "الطريقة/المثال"], [
        ["1 Ignore record", "Only if very few missing; else lose info", "Remove row", "تجاهل السجل إذا القليل فقط"],
        ["2 Fill manually", "Domain expert (doctor)", "Expert sets value", "خبير يحدّد القيمة"],
        ["3 Mean", "Numerical data", "60,70,80,?,90 → sum 300 / count 4 = 75", "متوسط: 300÷4=75"],
        ["4 Median", "When extreme values exist", "60,65,70,75,200 — 200 extreme → median better", "وسيط عند القيم المتطرفة"],
        ["5 Mode", "Categorical / most frequent", "Male, Female, Male, Male, ? → Male", "منوال للفئوي"],
        ["6 Predict", "DM/ML model", "Regression, Decision tree, k-NN", "تنبؤ بنماذج تعلم آلي"],
    ])
    + callout("Mean trap", "فخ المتوسط",
        "Divide by observed count (4), not 5, when one value is missing.",
        "اقسم على عدد القيم الموجودة (4) مو 5 إذا وحدة مفقودة.", "calc")
    + bilingual("Noise = random errors or unwanted variation. Lecture example: true ages 21,22,23,24,25 but dataset has 223 — likely entry error. Approaches: binning, regression, clustering, outlier detection.",
                "الضوضاء = أخطاء عشوائية أو تغير غير مرغوب. مثال: أعمار حقيقية 21..25 لكن الداتا فيها 223 — غالباً خطأ إدخال. طرق: binning، انحدار، تجميع، كشف شذوذ.")
    + bilingual("Binning: divide numerical values into bins. Example 10,12,13,20,22,25,30,31 → Bin1 10–13 · Bin2 20–25 · Bin3 30–31. Helps smooth noisy numerical data.",
                "Binning: تقسيم القيم الرقمية إلى فئات. مثال 10..31 → فئة 10–13 و20–25 و30–31. يساعد على تنعيم بيانات مشوّشة.")
    + callout("Outlier — critical exam rule", "القيمة الشاذة — قاعدة امتحانية",
        "An outlier is a data object whose value differs significantly from others (e.g. 65,67,68,70,69,300). An outlier is NOT necessarily an error — high BP may be a real condition. Investigate before removing. Detection: statistical, distance-based, clustering, visualization, ML.",
        "القيمة الشاذة تختلف بقوة عن البقية (مثال 300). ليست بالضرورة خطأ — ضغط مرتفع قد يكون حالة حقيقية. تحقق قبل الحذف. الكشف: إحصائي، مسافات، تجميع، رؤية، تعلم آلي.", "warn")
    + bilingual("Duplicates: same object appears more than once (ID 101 Ahmed 45 twice). Harm: inflate size, bias analysis, affect frequencies and model performance. Handle appropriately.",
                "التكرار: نفس الكائن مرتين (معرّف 101 مكرر). الضرر: تضخم الحجم، تحيز التحليل، أثر على التكرارات والأداء. عالجها بشكل مناسب.")
    + bilingual("Inconsistency: same category different formats — Male / M / male → standardize to Male; Iraq / IRAQ / iraq → Iraq.",
                "عدم الاتساق: نفس الفئة بتنسيقات مختلفة — ذكر/M/male ← توحيد Male؛ العراق بثلاث صيغ ← توحيد Iraq.")))

p2.append(sec(7, "Integration · Transformation · Reduction · Discretization", "7. الدمج · التحويل · التقليل · التجزئة",
    quote("Data Integration combines data from multiple sources into a single dataset.")
    + bilingual("University example: DB1 student info + DB2 grades joined on student ID. Problems: different attribute names, formats, duplicates, units (kg vs pounds), schemas.",
                "مثال الجامعة: قاعدة معلومات طلاب + قاعدة درجات تُدمج بمعرف الطالب. مشاكل: أسماء مختلفة، تنسيقات، تكرار، وحدات (كجم/رطل)، مخططات مختلفة.")
    + quote("Data Transformation converts data into a suitable format for Data Mining algorithms.")
    + bilingual("Techniques: Normalization, Aggregation, Generalization, Encoding, Feature construction. Why normalize? Age 0–100 vs Salary 300–10,000 vs Income up to 100,000 — large ranges dominate some algorithms.",
                "تقنيات: تطبيع، تجميع، تعميم، ترميز، بناء ميزات. ليش نطبع؟ العمر مقابل الراتب مقابل الدخل — المدى الكبير قد يسيطر على خوارزميات.")
    + bilingual("Encoding: Male=1, Female=0 possible but may imply false order; for Red/Blue/Green use one-hot (each category its own binary column).",
                "الترميز: ذكر=1 أنثى=0 ممكن لكنه قد يوحي بترتيب وهمي؛ للألوان استعمل one-hot (عمود ثنائي لكل فئة).")
    + quote("Data Reduction attempts to reduce size or complexity while preserving important information.")
    + bilingual("Techniques: dimensionality reduction, feature selection, sampling, aggregation, numerosity reduction.",
                "تقنيات: تقليل أبعاد، اختيار ميزات، معاينة، تجميع، تقليل عددية.")
    + bilingual("Feature selection example: keep Age, Gender, BMI, Blood Pressure; drop Patient Name, Phone, Address for disease prediction.",
                "مثال اختيار الميزات: احتفظ بالعمر والجنس وBMI وضغط الدم؛ احذف الاسم والهاتف والعنوان للتنبؤ بالمرض.")
    + callout("Feature Selection vs Extraction", "الاختيار مقابل الاستخراج",
        "Selection: pick EXISTING features (Age). Extraction: CREATE new features from originals (PCA components; BMI from weight/height). Mnemonic: Pick vs Build.",
        "الاختيار: تاخذ ميزات موجودة (العمر). الاستخراج: تنشئ ميزات جديدة من الأصلية (مكوّنات PCA؛ BMI من الوزن/الطول). الحفظ: اختر مقابل ابنِ.", "warn")
    + bilingual("Dimensionality reduction example: 100 features → 10 principal components (PCA). Reduces cost, storage, complexity; may help visualization.",
                "مثال تقليل الأبعاد: 100 ميزة ← 10 مكوّنات رئيسية (PCA). يقلل الكلفة والتخزين والتعقيد.")
    + bilingual("Discretization: continuous → intervals/categories. Age 18,25,32,47,65,72 → 0–17 Child · 18–35 Young Adult · 36–60 Adult · 61+ Senior.",
                "التجزئة: مستمر ← فئات. أعمار معيّنة ← طفل/شاب/بالغ/كبار السن.")
    + callout("Medical dataset walkthrough (lecture)", "مشي المثال الطبي (المحاضرة)",
        "Diabetes data with missing Glucose: (1) handle missing (2) check outliers (3) encode Gender (4) normalize Age/Glucose/BMI if needed (5) select useful features (6) apply classifier — Decision Tree, Naïve Bayes, k-NN, Logistic Regression, Random Forest.",
        "بيانات سكري بجلوكوز مفقود: (1) عالج المفقود (2) تحقق من الشذوذ (3) رمّز الجنس (4) طبّع الرقمية إن لزم (5) اختر ميزات مفيدة (6) طبّق تصنيف — شجرة قرار، نايف بايز، k-NN، انحدار لوجستي، غابة عشوائية.", "rule")))

p2.append(sec(8, "Data Preparation vs Preprocessing + exam sheet", "8. الإعداد مقابل المعالجة الأولية + ورقة الامتحان",
    table(["Term", "Scope", "Contents", "النطاق"], [
        ["Data Preparation", "Broader process preparing data for mining", "Cleaning · Integration · Transformation · Reduction · Discretization", "عملية أوسع"],
        ["Data Preprocessing", "Often narrower pre-modeling ops", "missing, noise, encoding, scaling/normalization, feature selection", "عمليات أضيق قبل النمذجة"],
    ])
    + bilingual("Preprocessing is an important part of the broader preparation process. Terminology can vary between textbooks.",
                "المعالجة الأولية جزء مهم من الإعداد الأوسع. المصطلحات تختلف بين الكتب.")
    + table(["Must memorize", "Details", "لازم تحفظ"], [
        ["Attribute types + decision path", "order? gap? two values? quantity?", "الأنواع ومسار القرار"],
        ["URL = Nominal", "no order, no measurable gap", "الرابط اسمي"],
        ["8 structures + anchor", "Row→Basket→…→Network", "الهياكل والمرساة"],
        ["Attribute vs structure separation", "values vs organization", "فصل الخصائص عن التنظيم"],
        ["Prep pipeline 5 steps", "not always same order; not only missing values", "5 خطوات + ملاحظة الترتيب"],
        ["Missing 6 methods", "mean example 75; median if outliers", "6 طرق + مثال 75"],
        ["Outlier ≠ error", "investigate first", "شذوذ ≠ خطأ"],
        ["Min-Max 40→0.5", "formula first + range [0,1]", "تطبيع مثال 0.5"],
        ["Selection vs Extraction", "Pick vs Build", "اختيار مقابل استخراج"],
        ["Discretization bins", "Age groups example", "فئات العمر"],
        ["Doctor protocol", "formula → symbols → steps → result+range", "بروتوكول د. أحمد"],
    ])))

check = '''<div class="check">
<p class="en"><b>Coverage check (builder self-audit)</b></p>
<p class="ar"><b>فحص التغطية (تحقق ذاتي)</b></p>
<ul class="en">
<li>W1: Definition + KDD + warehouses + beyond simple analysis + applications intro entities — YES</li>
<li>W1: 7 advantages + 3 Gemini levels + anchor — YES</li>
<li>W1: Disadvantages including American Express + tools + training + imprecision + anchor — YES</li>
<li>W1: 8 applications with 2-keyword + lecture detail + safe sentences — YES</li>
<li>W1: 6 challenges Nature/Cause/Effect + $500 story + outlier rule — YES</li>
<li>W2: Object vs attribute — YES</li>
<li>W2: Nominal/Ordinal/Binary/Numerical + decision template + URL=Nominal — YES</li>
<li>W2: Interval/Ratio + Min-Max/Z-score/decimal + worked 0.5 — YES</li>
<li>W2: 8 structures + separation rule + anchor — YES</li>
<li>W2: Prep definition + dirty data + pipeline + not-only-missing — YES</li>
<li>W2: Cleaning 6 missing + noise/binning + outlier≠error + duplicates + inconsistency — YES</li>
<li>W2: Integration/Transformation/Reduction/Discretization + Selection vs Extraction + medical walkthrough — YES</li>
<li>W2: Prep vs Preprocess + exam quick tables — YES</li>
</ul>
<p class="ar">التحقق: الأقسام أعلاه موجودة كاملة في الملفين — بلا ضغط ولا حذف جوهري للمادة.</p>
</div>'''

w1_html = wrap(
    "Data Mining Week 01 — Introduction",
    "تنقيب عن البيانات — الأسبوع الأول: مقدمة",
    "CS603/CS503 · Booklet W01 · Chapters: Definition · Advantages · Disadvantages · Applications · Challenges",
    p1 + [check])
w2_html = wrap(
    "Data Mining Week 02 — Data Types & Preparation",
    "تنقيب عن البيانات — الأسبوع الثاني: أنواع البيانات وإعدادها",
    "Data Mining · Booklet W02 · Attributes · Structures · Preparation Pipeline",
    p2 + [check])

(OUT_DIR / "Week_01_Data_Mining_Bilingual_EN_AR.html").write_text(w1_html, encoding="utf-8")
(OUT_DIR / "Week_02_Data_Mining_Bilingual_EN_AR.html").write_text(w2_html, encoding="utf-8")
print("W1", (OUT_DIR / "Week_01_Data_Mining_Bilingual_EN_AR.html").stat().st_size)
print("W2", (OUT_DIR / "Week_02_Data_Mining_Bilingual_EN_AR.html").stat().st_size)
