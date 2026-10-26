#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch03 T06 — Industry-specific cyber risk: banking, healthcare, critical infrastructure."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch03_lib import build

QUIZ = "Quiz_Ch03_T06_Industry_Specific_Risks"
TOPIC_EN = "Industry-Specific Risks: Banking, Health, Infrastructure"
TOPIC_AR = "مخاطر القطاعات: المصارف والصحة والبنية التحتية"

I = [
    # 1 -------------------------------------------------------------------
    ("why_banks_targeted", "Remember",
     "Why are banks prime targets?",
     "لماذا تُعدّ المصارف أهدافاً رئيسية؟",
     ["Their assets have direct monetary value.",
      "Their networks are the oldest in the world.",
      "Their staff are the least trained of all.",
      "Their software is always out of date."],
     ["لأن أصولها ذات قيمة نقدية مباشرة.",
      "لأن شبكاتها هي الأقدم في العالم.",
      "لأن موظفيها الأقل تدريباً بين الجميع.",
      "لأن برمجياتها قديمة دائماً هنا."],
     "Banks hold assets with direct monetary value, so an attack converts into money faster than in any other sector.",
     "المصارف تحمل أصولاً ذات قيمة نقدية مباشرة، فالهجوم يتحول إلى مال أسرع من أي قطاع آخر."),

    # 2 -------------------------------------------------------------------
    ("banking_risks", "Remember",
     "Which set lists the banking risks?",
     "أي مجموعة تسرد مخاطر المصارف؟",
     ["Fraud, payment-system attacks, and breaches.",
      "Ransomware, HIPAA fines, and IoT exploits.",
      "ICS attacks, grid failure, and transport.",
      "Phishing, patching delays, and audit findings."],
     ["الاحتيال وهجمات أنظمة الدفع والاختراقات.",
      "الفدية وغرامات HIPAA واستغلال الأجهزة.",
      "هجمات ICS وتعطل شبكة الكهرباء والنقل هنا.",
      "التصيّد وتأخير التحديث والتدقيق الأمني."],
     "Three banking risks: fraud and theft, attacks on the payment systems such as SWIFT, and data breaches that expose customer records.",
     "ثلاثة مخاطر مصرفية: الاحتيال والسرقة، والهجوم على أنظمة الدفع كشبكة SWIFT، واختراق البيانات الذي يكشف سجلات العملاء."),

    # 3 -------------------------------------------------------------------
    ("banking_impact", "Understand",
     "What makes the banking impact larger than a single firm's loss?",
     "ما الذي يجعل أثر اختراق مصرف أكبر من خسارة شركة واحدة؟",
     ["Loss of trust can destabilise whole economies.",
      "Loss of trust affects only one bank's own shares.",
      "Loss of trust is limited to the IT budget.",
      "Loss of trust has no measurable effect."],
     ["فقدان الثقة قد يزعزع اقتصادات كاملة.",
      "فقدان الثقة يخص أسهم مصرف واحد فقط.",
      "فقدان الثقة محدود بميزانية التقنية.",
      "فقدان الثقة بلا أثر قابل للقياس."],
     "Loss of trust in a financial institution can destabilise entire economies, because the sector runs on confidence rather than on cash in a vault.",
     "فقدان الثقة بمؤسسة مالية قد يزعزع اقتصادات كاملة، لأن القطاع يعمل على الثقة لا على نقد في خزنة."),

    # 4 -------------------------------------------------------------------
    ("healthcare_data_value", "Remember",
     "Why is healthcare data attractive to attackers?",
     "لماذا تُعدّ بيانات الرعاية الصحية جاذبة للمهاجمين؟",
     ["It is highly valuable on the dark web.",
      "It is worthless because it is encrypted.",
      "It is already published by the hospitals.",
      "It is identical to banking data in value."],
     ["قيمتها عالية جداً في الويب المظلم.",
      "بلا قيمة لأنها مشفّرة دائماً هنا.",
      "منشورة أصلاً من المستشفيات نفسها.",
      "قيمتها مطابقة لبيانات المصارف هنا."],
     "Medical records are highly valuable on the dark web, which is why hospitals hold data that is worth stealing in its own right.",
     "السجلات الطبية عالية القيمة في الويب المظلم، ولهذا تحمل المستشفيات بيانات تستحق السرقة بذاتها."),

    # 5 -------------------------------------------------------------------
    ("hipaa_penalty", "Remember",
     "What does a HIPAA violation cost a healthcare provider?",
     "ماذا تكلف مخالفة HIPAA مزوّد الرعاية الصحية؟",
     ["Multimillion-dollar fines for the provider.",
      "A short warning with no any financial penalty.",
      "Loss of the hospital's medical licence only.",
      "Automatic closure of the affected ward here."],
     ["غرامات بملايين الدولارات على المزوّد.",
      "تحذير قصير بلا أي عقوبة مالية هنا.",
      "فقدان ترخيص المستشفى الطبي فقط هنا.",
      "إغلاق الجناح المتأثر تلقائياً هنا تماماً."],
     "Breaches of patient data bring multimillion-dollar fines under HIPAA, on top of the cost of the incident itself.",
     "اختراق بيانات المرضى يجلب غرامات بملايين الدولارات بموجب HIPAA، إضافة إلى كلفة الحادث نفسه."),

    # 6 -------------------------------------------------------------------
    ("healthcare_ransomware_example", "Remember",
     "Which attack locked hospital records in the UK in 2017?",
     "أي هجوم أقفل سجلات المستشفيات في بريطانيا سنة 2017؟",
     ["WannaCry, which crippled the UK NHS in 2017.",
      "Stuxnet, which hit Iranian centrifuges.",
      "The Ukraine electricity grid attack of 2015.",
      "The SWIFT interbank network compromise."],
     ["WannaCry التي شلّت NHS البريطانية 2017.",
      "Stuxnet التي ضربت أجهزة الطرد الإيرانية.",
      "هجوم شبكة كهرباء أوكرانيا في 2015.",
      "اختراق شبكة SWIFT بين المصارف كلها."],
     "WannaCry crippled the UK NHS in 2017: records were locked and treatment was delayed, which is the healthcare-specific damage.",
     "WannaCry شلّت NHS البريطانية في 2017: أُقفلت السجلات وتأخّر العلاج، وهذا هو الضرر الخاص بالقطاع الصحي."),

    # 7 -------------------------------------------------------------------
    ("healthcare_iot_vectors", "Remember",
     "Which devices are named as healthcare attack vectors?",
     "أي أجهزة تُذكر كنواقل هجوم في القطاع الصحي؟",
     ["Pacemakers, insulin pumps, and MRI scanners.",
      "ATMs, card readers, and payment terminals.",
      "Centrifuges, turbines, and grid relays here.",
      "Routers, switches, and perimeter firewalls."],
     ["منظّمات ضربات القلب ومضخات الأنسولين والرنين.",
      "أجهزة الصراف وقارئات البطاقات وأجهزة الدفع.",
      "أجهزة الطرد والتوربينات ومرحّلات الشبكة هنا.",
      "الموجّهات والمبدّلات والجدران النارية هنا."],
     "Pacemakers, insulin pumps and MRI machines are all connected and all carry patient risk, so they are attack vectors rather than mere equipment.",
     "منظّمات ضربات القلب ومضخات الأنسولين وأجهزة الرنين كلها متصلة وكلها تحمل خطراً على المريض، فهي نواقل هجوم لا مجرد أجهزة."),

    # 8 -------------------------------------------------------------------
    ("critical_infra_actors", "Remember",
     "Who targets utilities, energy, and transport?",
     "من يستهدف المرافق والطاقة والنقل؟",
     ["Nation-state actors, because of national value.",
      "Individual hobbyists looking for a challenge.",
      "Insider employees seeking a better pay rise.",
      "Competitors seeking a marketing advantage here."],
     ["فاعلون دوليون بسبب القيمة الوطنية.",
      "أفراد هواة يبحثون عن تحدٍّ شخصي.",
      "موظفون داخليون يطلبون زيادة راتب.",
      "منافسون يبحثون عن ميزة تسويقية هنا."],
     "Critical infrastructure attracts nation-state actors, because the target is national capability rather than money.",
     "البنية التحتية الحرجة تجذب فاعلين دوليين، لأن الهدف قدرة وطنية لا مال."),

    # 9 -------------------------------------------------------------------
    ("stuxnet_example", "Remember",
     "What did Stuxnet do in 2010?",
     "ماذا فعل Stuxnet سنة 2010؟",
     ["Stuxnet in 2010 sabotaged nuclear centrifuges.",
      "Stuxnet in 2015 cut power to 230,000 homes.",
      "Stuxnet in 2017 encrypted hospital records.",
      "Stuxnet in 2020 stole interbank transfer records."],
     ["Stuxnet سنة 2010 خربت أجهزة الطرد النووية.",
      "Stuxnet سنة 2015 قطعت الكهرباء عن 230,000.",
      "Stuxnet سنة 2017 شفّرت سجلات المستشفى.",
      "Stuxnet سنة 2020 سرقت تحويلات بين المصارف."],
     "Stuxnet in 2010 sabotaged Iranian nuclear centrifuges, which is the canonical industrial-control-system attack.",
     "Stuxnet سنة 2010 خرّبت أجهزة الطرد المركزي النووية الإيرانية، وهو هجوم أنظمة التحكم الصناعي القياسي."),

    # 10 ------------------------------------------------------------------
    ("ukraine_grid_example", "Remember",
     "What did the 2015 grid attack achieve?",
     "ماذا حقق هجوم الشبكة سنة 2015؟",
     ["In 2015, leaving 230,000 citizens without power.",
      "In 2010, destroying a uranium centrifuge hall.",
      "In 2017, locking hospital records across the NHS.",
      "In 2020, draining interbank transfer accounts."],
     ["سنة 2015 تاركاً 230,000 مواطناً بلا كهرباء.",
      "سنة 2010 مدمّراً قاعة أجهزة طرد اليورانيوم.",
      "سنة 2017 مقفلاً سجلات مستشفيات NHS كلها.",
      "سنة 2020 مستنزفاً حسابات التحويلات كلها."],
     "The 2015 Ukraine grid attack left 230,000 citizens without electricity, which is the canonical energy-sector example.",
     "هجوم شبكة أوكرانيا سنة 2015 ترك 230,000 مواطناً بلا كهرباء، وهو مثال الطاقة القياسي."),

    # 11 ------------------------------------------------------------------
    ("impact_beyond_money", "Analyze",
     "What does each sector's impact reach beyond money?",
     "إلى ماذا يصل أثر كل قطاع بعد المال؟",
     ["Money, then life, then national security.",
      "Money, then shares, then the IT budget.",
      "Shares, then licences, then the audit trail.",
      "Budget, then staff, then the marketing plan."],
     ["المال، ثم حياة المريض، ثم الأمن القومي.",
      "المال، ثم الأسهم، ثم ميزانية التقنية.",
      "الأسهم، ثم التراخيص، ثم سجل التدقيق.",
      "الميزانية، ثم الموظفون، ثم خطة التسويق."],
     "In banking the damage reaches the whole economy, in healthcare it reaches the patient's life, and in infrastructure it reaches national security.",
     "في المصارف يصل الضرر للاقتصاد كله، وفي الصحة يصل لحياة المريض، وفي البنية التحتية يصل للأمن القومي."),

    # 12 ------------------------------------------------------------------
    ("why_compare_industries", "Understand",
     "Why does comparing the three sectors matter?",
     "لماذا تهم مقارنة القطاعات الثلاثة؟",
     ["It shows the enterprise-wide weight of the risk.",
      "It proves that some industries need no controls.",
      "It ranks industries by their annual revenue.",
      "It replaces the need for any risk register at all."],
     ["تُظهر ثقل الخطر على مستوى المؤسسة.",
      "تُثبت أن بعض القطاعات لا تحتاج ضوابط.",
      "ترتّب القطاعات حسب إيراداتها السنوية.",
      "تُغني عن الحاجة إلى سجل مخاطر."],
     "The differences illustrate that the same discipline carries enterprise-wide weight: each sector loses something different, and all three lose more than money.",
     "الاختلافات توضّح أن التخصص نفسه يحمل ثقلاً على مستوى المؤسسة: كل قطاع يخسر شيئاً مختلفاً، والثلاثة يخسرون أكثر من المال."),
]

KEY = "ABCDABCDABCD"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
