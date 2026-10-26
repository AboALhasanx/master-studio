#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch03 T01 — Cybersecurity as an organizational risk, and why it is one."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch03_lib import build

QUIZ = "Quiz_Ch03_T01_Organizational_Risk"
TOPIC_EN = "Cybersecurity as an Organizational Risk"
TOPIC_AR = "الأمن السيبراني كخطر تنظيمي"

I = [
    # 1 -------------------------------------------------------------------
    ("early_technical_framing", "Remember",
     "How was cybersecurity framed for much of its early history?",
     "كيف كان الأمن السيبراني يُصاغ في معظم تاريخه المبكر؟",
     ["A technical challenge solved by firewalls and antivirus.",
      "A legal obligation enforced by regulators and auditors.",
      "A reputational matter handled by the marketing team.",
      "A financial risk carried entirely by the insurance providers."],
     ["تحدٍّ تقني يُحلّ بالجدران النارية ومكافحة الفيروسات.",
      "التزام قانوني تفرضه الجهات التنظيمية والمدققون معاً.",
      "مسألة سمعة يتولاها فريق التسويق وحده بالكامل.",
      "خطر مالي يحمله مزوّدو التأمين وحدهم تماماً."],
     "Early on, security was treated as a technical problem: firewalls, antivirus and intrusion detection were assumed to be enough, and every problem was expected to be fixed by buying the right tool.",
     "في البداية كان الأمن يُعامَل كمشكلة تقنية: الجدران النارية ومكافحة الفيروسات وكشف التطفل كانت تُعدّ كافية، وكل مشكلة كان يُفترض حلها بشراء الأداة الصحيحة."),

    # 2 -------------------------------------------------------------------
    ("failures_are_organizational", "Remember",
     "What have the last two decades shown about cybersecurity failures?",
     "ماذا أثبت العقدان الماضيان عن إخفاقات الأمن السيبراني؟",
     ["That failures are fundamentally organizational threats.",
      "That failures come mostly from outdated antivirus signatures.",
      "That failures stay inside the IT department boundary.",
      "That failures can be removed by buying the right tools."],
     ["أن الإخفاقات تهديدات تنظيمية بالأساس.",
      "أن الإخفاقات سببها توقيعات فيروسات قديمة.",
      "أن الإخفاقات تبقى داخل قسم تقنية المعلومات.",
      "أن الإخفاقات تُزال بشراء الأدوات الصحيحة."],
     "Two decades of incidents showed the opposite of the early assumption: these failures are organizational threats, not tool failures.",
     "عقدان من الحوادث أظهرا عكس الافتراض المبكر: هذه الإخفاقات تهديدات تنظيمية لا أعطال أدوات."),

    # 3 -------------------------------------------------------------------
    ("consequence_set", "Remember",
     "Which set of consequences follows from a cybersecurity failure?",
     "أي مجموعة نتائج تترتب على إخفاق أمني سيبراني؟",
     ["Financial loss, reputation damage, and regulatory penalties.",
      "Slower networks and much higher hardware costs.",
      "Loss of the whole IT team to much better-paying competitors.",
      "Extra training hours for the administrative staff every year."],
     ["خسارة مالية وضرر بالسمعة وعقوبات تنظيمية.",
      "شبكات أبطأ وكلفة عتاد أعلى بكثير.",
      "فقدان فريق التقنية كله لمنافسين يدفعون أكثر.",
      "ساعات تدريب إضافية للموظفين الإداريين."],
     "A failure brings financial loss, reputational damage and regulatory penalties, and at national scale it can become a systemic risk.",
     "الإخفاق يجلب خسارة مالية وضرراً بالسمعة وعقوبات تنظيمية، وعلى المستوى الوطني قد يصبح خطراً نظامياً."),

    # 4 -------------------------------------------------------------------
    ("not_isolated_in_it", "Understand",
     "Where can cybersecurity not be kept?",
     "أين لا يمكن حصر الأمن السيبراني؟",
     ["It cannot be isolated inside the IT department.",
      "It belongs to the legal department by default.",
      "It is best handled by an external provider.",
      "It is a product that can be bought off the shelf."],
     ["لا يمكن عزله داخل قسم تقنية المعلومات.",
      "ينتمي إلى القسم القانوني بشكل افتراضي.",
      "من الأفضل أن يتولاه مزوّد خارجي متخصص.",
      "منتج يُشترى جاهزاً من السوق مباشرة."],
     "It cannot be isolated within the IT department. It is a boardroom-level concern instead.",
     "لا يمكن عزله داخل قسم تقنية المعلومات، بل هو شأن على مستوى مجلس الإدارة."),

    # 5 -------------------------------------------------------------------
    ("boardroom_requirements", "Remember",
     "If cybersecurity is a boardroom-level concern, what does it require?",
     "إذا كان الأمن السيبراني شأناً على مستوى مجلس الإدارة، فماذا يتطلب؟",
     ["Governance, risk management, and strategy alignment.",
      "A much larger antivirus budget and faster patching.",
      "An outsourced security operations centre for the group.",
      "A separate security department under the IT manager."],
     ["حوكمة وممارسات إدارة مخاطر ودمج بالاستراتيجية.",
      "ميزانية مكافحة فيروسات أكبر وتحديث أسرع للنظم.",
      "مركز عمليات أمنية خارجي للمجموعة كلها فعلاً.",
      "قسم أمني منفصل يتبع مدير التقنية نفسه."],
     "Boardroom level means governance structures, risk management practices, and integration with organizational strategy.",
     "مستوى مجلس الإدارة يعني هياكل حوكمة وممارسات إدارة مخاطر ودمجاً مع استراتيجية المؤسسة."),

    # 6 -------------------------------------------------------------------
    ("four_reasons_count", "Remember",
     "How many reasons make cybersecurity an organizational matter?",
     "كم سبباً يجعل الأمن السيبراني مسألة تنظيمية؟",
     ["Four reasons.", "Three reasons.", "Five reasons.", "Two reasons."],
     ["أربعة أسباب.", "ثلاثة أسباب.", "خمسة أسباب.", "سببان فقط."],
     "Four: pervasive digitization, ecosystem dependence, adversarial nature, and the legal and regulatory context.",
     "أربعة: الرقمنة الشاملة، والاعتماد على المنظومة، والطبيعة العدائية، والسياق القانوني والتنظيمي."),

    # 7 -------------------------------------------------------------------
    ("reason_digitization", "Remember",
     "What does pervasive digitization mean as a reason?",
     "ماذا تعني الرقمنة الشاملة كسبب؟",
     ["Every business process now depends on IT systems.",
      "Vendors and cloud services form a long supply chain.",
      "Attackers adapt faster than the defenders do.",
      "Compliance rules tie breaches to penalties."],
     ["كل عملية تجارية اليوم تعتمد على أنظمة تقنية.",
      "الموردون والخدمات السحابية تشكّل سلسلة توريد.",
      "المهاجمون يتكيّفون أسرع من المدافعين.",
      "قواعد الامتثال تربط الاختراق بعقوبات."],
     "Digitization is about reach: finance, healthcare and supply chains all run on IT, so a failure can stop the operation itself.",
     "الرقمنة تخص الانتشار: المالية والرعاية الصحية وسلاسل التوريد كلها تعمل بأنظمة تقنية، فالإخفاق قد يوقف العملية نفسها."),

    # 8 -------------------------------------------------------------------
    ("reason_ecosystem", "Remember",
     "What does ecosystem dependence mean as a reason?",
     "ماذا يعني الاعتماد على المنظومة كسبب؟",
     ["One weak vendor link can cascade enterprise-wide.",
      "Every business process depends on an internal system.",
      "Attackers are intelligent and keep adapting to defences.",
      "Compliance rules turn a breach into a financial penalty."],
     ["حلقة مورّد ضعيفة قد تتسلسل على المؤسسة كلها.",
      "كل عملية تجارية تعتمد على نظام تقني داخلي.",
      "المهاجمون أذكياء ويستمرون بالتكيّف مع الدفاع.",
      "قواعد الامتثال تحوّل الاختراق إلى عقوبة."],
     "Ecosystem dependence is about the chain: vendors, cloud services and global supply chains mean a breach in one weak link can cascade.",
     "الاعتماد على المنظومة يخص السلسلة: الموردون والخدمات السحابية وسلاسل التوريد العالمية تعني أن اختراق حلقة واحدة قد يتسلسل."),

    # 9 -------------------------------------------------------------------
    ("reason_adversarial", "Remember",
     "What makes cyber risk different from a fire or a flood?",
     "ما الذي يجعل الخطر السيبراني مختلفاً عن الحريق أو الفيضان؟",
     ["Cyber risks come from adaptive, intelligent adversaries.",
      "Cyber risks come from fires, floods and other natural events.",
      "Cyber risks come from outdated documentation alone.",
      "Cyber risks come from the hardware supply chain itself."],
     ["المخاطر السيبرانية من خصوم متكيّفين وأذكياء.",
      "المخاطر السيبرانية من الحرائق والفيضانات.",
      "المخاطر السيبرانية من وثائق قديمة فقط تماماً.",
      "المخاطر السيبرانية من سلسلة توريد العتاد."],
     "Natural risks do not think. Cyber risk comes from hackers, nation-states and insiders who adapt to whatever defence is deployed.",
     "المخاطر الطبيعية لا تفكّر. أما الخطر السيبراني فيأتي من قراصنة ودول وعناصر داخلية تتكيّف مع أي دفاع يُنشر."),

    # 10 ------------------------------------------------------------------
    ("reason_legal", "Remember",
     "Which obligations tie a breach directly to a penalty?",
     "أي التزامات تربط الاختراق بعقوبة مباشرة؟",
     ["GDPR, HIPAA, and PCI-DSS tie breaches to penalties.",
      "Firewalls, antivirus, and intrusion detection tools.",
      "Backups, encryption, and access control policies.",
      "Governance, strategy, and full board reporting."],
     ["GDPR و HIPAA و PCI-DSS تربط الاختراق بعقوبات.",
      "الجدران النارية ومكافحة الفيروسات وكشف التطفل.",
      "النسخ الاحتياطي والتشفير وضوابط الوصول.",
      "الحوكمة والاستراتيجية والتقارير لمجلس الإدارة."],
     "Compliance obligations such as GDPR, HIPAA and PCI-DSS attach legal liability and financial penalties to a security failure.",
     "التزامات الامتثال مثل GDPR و HIPAA و PCI-DSS تربط المسؤولية القانونية والعقوبات المالية بالإخفاق الأمني."),

    # 11 ------------------------------------------------------------------
    ("tools_are_one_layer", "Understand",
     "Where do the technical tools sit in the overall picture?",
     "أين تقع الأدوات التقنية في الصورة الكاملة؟",
     ["One layer inside a broader governance framework.",
      "The only layer that really matters in practice.",
      "A full replacement for the governance framework.",
      "A temporary fix until governance is written."],
     ["طبقة واحدة داخل إطار حوكمة أوسع.",
      "الطبقة الوحيدة المهمة عملياً في المؤسسة.",
      "بديل كامل عن إطار الحوكمة كله.",
      "حل مؤقت حتى تُكتب الحوكمة المناسبة."],
     "Technical tools are one layer only, inside a larger framework of governance and risk management. They are necessary, not sufficient.",
     "الأدوات التقنية طبقة واحدة فقط، داخل إطار أوسع من الحوكمة وإدارة المخاطر. فهي ضرورية لكنها غير كافية."),

    # 12 ------------------------------------------------------------------
    ("risk_management_purpose", "Understand",
     "What does risk management let an organization do?",
     "ماذا تتيح إدارة المخاطر للمؤسسة؟",
     ["Anticipate, prioritise, and mitigate before crisis.",
      "Detect the incidents after they have already spread.",
      "Replace technical controls with written policy.",
      "Move the risk to an external insurance provider."],
     ["توقّع المخاطر وترتيبها وتخفيفها قبل الأزمة.",
      "كشف الحوادث بعد أن تكون قد انتشرت فعلاً.",
      "استبدال الضوابط التقنية بسياسة مكتوبة فقط.",
      "نقل الخطر إلى مزوّد تأمين خارجي كبير جداً."],
     "Risk management lets the organization anticipate, prioritize and mitigate risks before they escalate into crises.",
     "إدارة المخاطر تتيح للمؤسسة توقّع المخاطر وترتيب أولوياتها وتخفيفها قبل أن تتصاعد إلى أزمات."),
]

KEY = "ABCDACBDABCD"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
