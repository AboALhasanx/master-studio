#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch01 T02 — Four levels, six domains, and the R(t) exposure model."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch01_lib import build

QUIZ = "Quiz_Ch01_T02_Scope_Domains_and_Risk_Exposure"
TOPIC_EN = "4 Levels, 6 Domains & Risk Exposure R(t)"
TOPIC_AR = "المستويات الأربعة والمجالات الستة ونموذج التعرض للمخاطر"

I = [
    # 1 -------------------------------------------------------------------
    ("scope_four_levels", "Remember",
     "Which set lists the four levels of cybersecurity scope?",
     "أي مجموعة تسرد المستويات الأربعة لنطاق الأمن السيبراني؟",
     ["Individuals, enterprises, governments, and global trade.",
      "Individuals, enterprises, ministries, and local trade.",
      "Users, companies, regulators, and international trade.",
      "Individuals, institutions, governments, and the industry."],
     ["الأفراد والمؤسسات والحكومات والتجارة العالمية.",
      "الأفراد والمؤسسات والوزارات والتجارة المحلية.",
      "المستخدمون والشركات والجهات الرقابية والتجارة الدولية.",
      "الأفراد والهيئات والحكومات والقطاع الصناعي."],
     "The four levels are individuals, enterprises, governments, and global trade. The scope widens at each step.",
     "المستويات الأربعة هي: الأفراد، المؤسسات، الحكومات، التجارة العالمية. النطاق يتوسّع في كل خطوة."),

    # 2 -------------------------------------------------------------------
    ("scope_level_individuals", "Remember",
     "At the individuals level, what does cybersecurity protect?",
     "في مستوى الأفراد، ماذا يحمي الأمن السيبراني؟",
     ["Personal devices, email, social accounts, and banking details.",
      "Company devices, company email, social accounts, and bank records.",
      "National records, email, social accounts, and state data.",
      "Trading systems, email, social accounts, and contracts."],
     ["الأجهزة الشخصية والإيميل والحسابات المصرفية.",
      "أجهزة الشركة والإيميل والسجلات المصرفية.",
      "السجلات الوطنية والإيميل وبيانات الدولة الرسمية.",
      "أنظمة التداول والإيميل والعقود التجارية."],
     "The individuals level is about personal devices, personal email, social media accounts, and private banking details.",
     "مستوى الأفراد يخص الأجهزة الشخصية والإيميل الشخصي وحسابات التواصل وبيانات المصرف الخاصة."),

    # 3 -------------------------------------------------------------------
    ("scope_level_enterprises", "Understand",
     "What drives a security programme at the enterprises level?",
     "ما الذي يحرّك برنامج الأمن في مستوى المؤسسات؟",
     ["Continuity of business, customer trust, and compliance.",
      "Business growth, product design, and the retention of staff.",
      "National defence, border control, and e-government.",
      "Cross-border trade, currency flow, and shipping."],
     ["استمرارية العمل وثقة العملاء والامتثال القانوني.",
      "نمو العمل وتصميم المنتج والاحتفاظ بالموظفين.",
      "الدفاع الوطني وضبط الحدود والحكومة الإلكترونية للدولة.",
      "التجارة عبر الحدود وتدفق العملة والشحن."],
     "Enterprises care about keeping the business running, keeping customer trust, and meeting legal compliance.",
     "المؤسسات تهتم باستمرار العمل، والحفاظ على ثقة العملاء، والوفاء بالامتثال القانوني."),

    # 4 -------------------------------------------------------------------
    ("scope_level_governments", "Remember",
     "Which assets are protected at the governments level?",
     "أي أصول تُحمى في مستوى الحكومات؟",
     ["National security, defence, and e-government services.",
      "Retail catalogues, delivery systems, and online shops.",
      "Personal photos, messaging apps, and home routers.",
      "Trade contracts, payment systems, and shipping lanes."],
     ["الأمن الوطني والدفاع وخدمات الحكومة الإلكترونية.",
      "كتالوجات التجزئة وأنظمة التوصيل والمتاجر الكبرى.",
      "الصور الشخصية وتطبيقات المراسلة والموجّهات.",
      "عقود التجارة وأنظمة الدفع وخطوط الشحن."],
     "At the governments level the focus is national security, defence, and the infrastructure of e-governance.",
     "في مستوى الحكومات التركيز على الأمن الوطني والدفاع وبنية الحكومة الإلكترونية."),

    # 5 -------------------------------------------------------------------
    ("scope_level_global_trade", "Remember",
     "What does the global trade level of scope protect?",
     "ماذا يحمي مستوى التجارة العالمية في النطاق؟",
     ["Cross-border digital commerce and financial systems.",
      "Domestic retail chains and the local payment systems.",
      "National defence networks and military systems.",
      "Personal banking applications and home devices."],
     ["التجارة الرقمية عبر الحدود والأنظمة المالية.",
      "سلاسل التجزئة المحلية وأنظمة الدفع المحلية.",
      "شبكات الدفاع الوطنية والأنظمة العسكرية للدولة.",
      "تطبيقات المصرف الشخصية وأجهزة المنزل."],
     "Global trade covers cross-border digital commerce, interbank traffic, and the financial systems behind them.",
     "التجارة العالمية تغطي التجارة الرقمية عبر الحدود وحركة البيانات بين المصارف والأنظمة المالية التي تقف خلفها."),

    # 6 -------------------------------------------------------------------
    ("domains_six_core", "Remember",
     "Which set lists the six key domains of cybersecurity?",
     "أي مجموعة تسرد المجالات الستة الأساسية للأمن السيبراني؟",
     ["Network, application, cloud, IoT, mobile, and ICS.",
      "Network, hardware, cloud, IoT, desktop, and ICS.",
      "Network, application, storage, IoT, mobile, and web.",
      "Network, application, cloud, data, mobile, and ICS."],
     ["الشبكات والتطبيقات والسحابة وإنترنت الأشياء والموبايل والتحكم الصناعي.",
      "الشبكات والعتاد والسحابة وإنترنت الأشياء والحواسيب والتحكم الصناعي.",
      "الشبكات والتطبيقات والتخزين وإنترنت الأشياء والموبايل والويب العام.",
      "الشبكات والتطبيقات والسحابة والبيانات والموبايل والتحكم الصناعي."],
     "The six domains are network, application, cloud, IoT, mobile, and industrial control systems.",
     "المجالات الستة هي: الشبكات، التطبيقات، السحابة، إنترنت الأشياء، الموبايل، وأنظمة التحكم الصناعي."),

    # 7 -------------------------------------------------------------------
    ("domain_network_scope", "Understand",
     "Which domain covers firewalls and intrusion detection systems?",
     "أي مجال يغطي الجدران النارية وأنظمة كشف التطفل؟",
     ["The network security domain.",
      "The cloud security domain.",
      "The mobile security domain.",
      "The application security domain."],
     ["مجال أمن الشبكات.",
      "مجال أمن السحابة.",
      "مجال أمن الموبايل.",
      "مجال أمن التطبيقات."],
     "Firewalls and IDS/IPS are the two tools the lecture names for network security.",
     "الجدران النارية وأنظمة كشف ومنع التطفل هما الأداتان اللتان تذكرهما المحاضرة لأمن الشبكات."),

    # 8 -------------------------------------------------------------------
    ("domain_iot_scope", "Understand",
     "Which domain relies on lightweight encryption and anomaly detection?",
     "أي مجال يعتمد على التشفير الخفيف وكشف الشذوذ؟",
     ["The internet-of-things domain.",
      "The cloud security domain.",
      "The network security domain.",
      "The application security domain."],
     ["مجال إنترنت الأشياء.",
      "مجال أمن السحابة العامة.",
      "مجال أمن الشبكات الداخلية.",
      "مجال أمن التطبيقات."],
     "IoT devices are small and low-powered, so the lecture pairs lightweight encryption with anomaly detection.",
     "أجهزة إنترنت الأشياء صغيرة وقليلة الطاقة، لذلك تقرن المحاضرة التشفير الخفيف بكشف الشذوذ."),

    # 9 -------------------------------------------------------------------
    ("domains_list_is_open", "Understand",
     "The lecture says the list of domains is not fixed. What follows from that?",
     "المحاضرة تقول إن قائمة المجالات ليست ثابتة. ماذا ينتج عن ذلك؟",
     ["New domains appear as technology develops, so the six are examples.",
      "Only the six listed domains exist and no others will ever be added.",
      "The six domains are replaced every year by a completely new six.",
      "The domains are fixed but their order of importance changes."],
     ["تظهر مجالات جديدة مع تطور التقنية، فالستة أمثلة فقط.",
      "لا توجد إلا المجالات الستة المذكورة ولن يُضاف غيرها.",
      "المجالات الستة تُستبدل كل سنة بستة مجالات جديدة.",
      "المجالات ثابتة لكن ترتيب أهميتها هو الذي يتغيّر."],
     "She said the number of domains can grow, so treat the six as the current set of examples, not a closed list.",
     "قالت إن عدد المجالات قابل للزيادة، فالستة هي المجموعة الحالية من الأمثلة وليست قائمة مغلقة."),

    # 10 ------------------------------------------------------------------
    ("risk_exposure_model_symbols", "Remember",
     "In the exposure model, what does the product of probability and impact represent?",
     "في نموذج التعرّض، ماذا يمثّل حاصل ضرب الاحتمال بالتأثير؟",
     ["The expected risk of one threat at a given time.",
      "The total budget spent on one security control.",
      "The number of entry points exposed to attack.",
      "The share of users who completed security training."],
     ["الخطر المتوقع لتهديد واحد في وقت معيّن.",
      "إجمالي الميزانية المصروفة على ضابط أمني واحد.",
      "عدد نقاط الدخول المكشوفة أمام المهاجم.",
      "نسبة المستخدمين الذين أكملوا التدريب الأمني."],
     "The model sums probability times impact over all threats, so each term is the expected risk of a single threat.",
     "النموذج يجمع حاصل ضرب الاحتمال بالتأثير على كل التهديدات، فكل حد هو الخطر المتوقع لتهديد واحد."),

    # 11 ------------------------------------------------------------------
    ("risk_exposure_time_marker", "Understand",
     "A question mentions time explicitly. Which model should you apply?",
     "سؤال يذكر الزمن صراحةً. أي نموذج تستخدم؟",
     ["The exposure model, because time marks it.",
      "The optimisation model, because time is fixed.",
      "The utility model, because weights change.",
      "The compliance model, because time is audited."],
     ["نموذج التعرّض، لأن الزمن علامته.",
      "نموذج التحسين، لأن الزمن فيه ثابت.",
      "نموذج المنفعة، لأن الأوزان تتغيّر.",
      "نموذج الامتثال، لأن الزمن يُدقَّق."],
     "The time variable exists to tell you which law applies. Time in the question means the exposure model, not the optimisation model.",
     "متغيّر الزمن موجود ليدلّك أي قانون تستخدم. وجود الزمن في السؤال يعني نموذج التعرّض لا نموذج التحسين."),

    # 12 ------------------------------------------------------------------
    ("risk_exposure_compute", "Apply",
     "Threat A has probability 0.2 and impact 500. Threat B has probability 0.3 and impact 500. What is the total expected risk?",
     "التهديد A احتماله 0.2 وتأثيره 500. والتهديد B احتماله 0.3 وتأثيره 500. ما إجمالي الخطر المتوقع؟",
     ["250", "150", "500", "650"],
     ["250", "150", "500", "650"],
     "Each term is probability times impact: 0.2 x 500 = 100 and 0.3 x 500 = 150. The sum is 250.",
     "كل حد هو الاحتمال ضرب التأثير: 0.2 × 500 = 100، و0.3 × 500 = 150. والمجموع 250."),
]

KEY = "ABCADBCDACBD"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
