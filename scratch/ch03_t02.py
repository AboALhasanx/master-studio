#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch03 T02 — The three dimensions of cyber risk and expected financial loss."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch03_lib import build

QUIZ = "Quiz_Ch03_T02_Three_Dimensions_And_EFL"
TOPIC_EN = "The Three Dimensions of Cyber Risk & EFL"
TOPIC_AR = "أبعاد الخطر السيبراني الثلاثة والخسارة المالية المتوقعة"

I = [
    # 1 -------------------------------------------------------------------
    ("three_dimensions", "Remember",
     "Through which dimensions is the need for risk management explained?",
     "بأي أبعاد تُفسَّر الحاجة إلى إدارة المخاطر؟",
     ["Financial, operational, and reputational.",
      "Technical, legal, and managerial ones.",
      "Strategic, tactical, and operational.",
      "Internal, external, and regulatory ones."],
     ["مالية وتشغيلية وسمعة معاً.",
      "تقنية وقانونية وإدارية فقط.",
      "استراتيجية وتكتيكية وتشغيلية.",
      "داخلية وخارجية وتنظيمية هنا."],
     "Three dimensions carry the argument: financial, operational and reputational. They are the reason risk management is a management duty, not an IT task.",
     "ثلاثة أبعاد تحمل الحجة: المالي والتشغيلي والسمعة. وهي سبب كون إدارة المخاطر واجباً إدارياً لا مهمة تقنية."),

    # 2 -------------------------------------------------------------------
    ("financial_growth", "Remember",
     "How has the direct financial cost of cyberattacks moved?",
     "كيف تحرّكت الكلفة المالية المباشرة للهجمات السيبرانية؟",
     ["It has grown exponentially.", "It has fallen steadily.",
      "It has stayed flat for years.", "It cannot be measured at all."],
     ["نمت نمواً أسّياً كبيراً.", "انخفضت بثبات واضح جداً.",
      "بقيت ثابتة لسنوات عديدة.", "لا يمكن قياسها إطلاقاً هنا."],
     "The direct financial cost has grown exponentially, which is why the financial dimension leads the argument.",
     "الكلفة المالية المباشرة نمت نمواً أسّياً، ولهذا يتصدّر البعد المالي الحجة."),

    # 3 -------------------------------------------------------------------
    ("financial_sources", "Remember",
     "Which set lists the sources of financial loss?",
     "أي مجموعة تسرد مصادر الخسارة المالية؟",
     ["Response, disruption, penalties, ransom, litigation.",
      "Patching, backups, training, auditing, and monitoring.",
      "Firewalls, antivirus, encryption, and access control.",
      "Salaries, rent, utilities, marketing, and travel costs."],
     ["الاستجابة والتعطّل والعقوبات والفدية والتقاضي.",
      "التحديث والنسخ والتدريب والتدقيق والمراقبة.",
      "الجدران النارية ومكافحة الفيروسات والتشفير.",
      "الرواتب والإيجار والمرافق والتسويق والسفر هنا."],
     "Five sources: incident response costs, business disruption, legal penalties, ransom payments, and litigation.",
     "خمسة مصادر: تكاليف الاستجابة للحوادث، وتعطّل الأعمال، والعقوبات القانونية، ومدفوعات الفدية، والتقاضي."),

    # 4 -------------------------------------------------------------------
    ("efl_expression", "Understand",
     "What does expected financial loss sum?",
     "ما الذي يجمعه نموذج الخسارة المالية المتوقعة؟",
     ["Probability times impact, summed over threats.",
      "Impact divided by the number of threats we know.",
      "The largest single loss the firm could face.",
      "The average loss recorded in the last year."],
     ["الاحتمال مضروباً بالتأثير ومجموعاً.",
      "التأثير مقسوماً على عدد التهديدات كلها.",
      "أكبر خسارة منفردة قد تواجه المؤسسة فعلاً.",
      "متوسط الخسارة المسجلة في السنة الماضية."],
     "It multiplies each threat's probability by its impact and adds the results, so it is an expected value across the whole risk register.",
     "يضرب احتمال كل تهديد في تأثيره ويجمع النواتج، فهو قيمة متوقعة على كل سجل المخاطر."),

    # 5 -------------------------------------------------------------------
    ("efl_purpose", "Understand",
     "What does the expected-loss model let a CISO do?",
     "ماذا يتيح نموذج الخسارة المتوقعة لمدير أمن المعلومات؟",
     ["To prioritise investment in controls.",
      "To replace the security policy entirely.",
      "To measure staff productivity per team.",
      "To calculate the cost of the hardware."],
     ["ترتيب أولويات الاستثمار في الضوابط.",
      "استبدال سياسة الأمن بالكامل هنا.",
      "قياس إنتاجية الموظفين لكل فريق عمل.",
      "حساب كلفة العتاد المستخدم فعلياً."],
     "The model lets CISOs and executives prioritize investment in cybersecurity controls, because it puts a number on each risk.",
     "النموذج يتيح لمديري الأمن والتنفيذيين ترتيب أولويات الاستثمار في ضوابط الأمن، لأنه يضع رقماً لكل خطر."),

    # 6 -------------------------------------------------------------------
    ("operational_risk", "Understand",
     "What is the operational dimension about?",
     "عمّاذا يتحدث البعد التشغيلي؟",
     ["Paralysis, so continuity planning matters.",
      "A small dip in the share price for one quarter.",
      "Only a loss of customer trust over time.",
      "Only the legal penalties after an incident."],
     ["شلل تشغيلي، فالتخطيط للاستمرارية مهم.",
      "انخفاض بسيط في سعر السهم لربع واحد فقط.",
      "فقدان ثقة العملاء مع الوقت فقط هنا.",
      "العقوبات القانونية بعد الحادث فقط."],
     "A failure often produces operational paralysis, which is why cybersecurity has to be integrated with business continuity planning.",
     "الإخفاق كثيراً ما ينتج شللاً تشغيلياً، ولهذا يجب دمج الأمن السيبراني بتخطيط استمرارية الأعمال."),

    # 7 ------------------------------------------------------------------
    ("operational_resilience", "Remember",
     "Which measures keep the organization working under attack?",
     "أي تدابير تُبقي المؤسسة عاملة تحت الهجوم؟",
     ["Backups, redundancy, and incident response plans.",
      "Encryption and strict access control lists.",
      "A larger marketing budget for the whole brand.",
      "Outsourcing the entire IT department to a vendor."],
     ["النسخ الاحتياطي والتكرار وخطط الاستجابة.",
      "التشفير وقوائم التحكم بالوصول الصارمة.",
      "ميزانية تسويق أكبر للعلامة التجارية.",
      "إسناد قسم التقنية كله لمزوّد خارجي كبير."],
     "Resilience comes from backups, redundancy and incident response planning: the organization keeps functioning even under attack.",
     "الصمود يأتي من النسخ الاحتياطي والتكرار وتخطيط الاستجابة: المؤسسة تبقى عاملة حتى تحت الهجوم."),

    # 8 ------------------------------------------------------------------
    ("reputation_trust", "Understand",
     "Why does reputation count as a dimension of risk?",
     "لماذا تُعدّ السمعة بعداً من أبعاد الخطر؟",
     ["Trust is among the most valuable assets.",
      "Trust can always be rebuilt quickly.",
      "Reputation matters only to small firms.",
      "Reputation is only a technical control item."],
     ["الثقة من أثمن أصول المؤسسة.",
      "الثقة يمكن استرجاعها بسرعة دائماً.",
      "السمعة تهم الشركات الصغيرة فقط.",
      "السمعة ضابط تقني في النظام."],
     "Trust is one of the organization's most valuable assets, and a breach can do damage to customer trust that cannot be repaired.",
     "الثقة من أثمن أصول المؤسسة، والاختراق قد يُلحق بثقة العملاء ضرراً لا يمكن إصلاحه."),

    # 9 ------------------------------------------------------------------
    ("reputation_recovery", "Remember",
     "What happens to reputation once it is lost?",
     "ماذا يحدث للسمعة بعد أن تضيع؟",
     ["It is hard to recover once it is lost.",
      "It recovers automatically within a year.",
      "It improves after every incident here.",
      "It has no effect on revenue at all."],
     ["يصعب استرجاعها جداً بعد أن تضيع.",
      "تُستعاد تلقائياً خلال سنة واحدة.",
      "تتحسّن بعد كل حادث أمني هنا.",
      "لا تأثير لها على الإيرادات إطلاقاً."],
     "Reputation is hard to recover once lost, which is why the reputational dimension is treated as a risk in its own right.",
     "السمعة يصعب استرجاعها بعد ضياعها، ولهذا يُعامَل البعد السمعوي كخطر قائم بذاته."),

    # 10 -----------------------------------------------------------------
    ("reputation_revenue_link", "Remember",
     "In which sectors does reputation tie directly to revenue?",
     "في أي قطاعات ترتبط السمعة بالإيرادات مباشرةً؟",
     ["Banking, healthcare, and the e-commerce sector.",
      "Public universities and government schools only.",
      "Defence contractors and government agencies only.",
      "Small local retail businesses only here."],
     ["المصارف والرعاية الصحية وشركات التجارة.",
      "الجامعات العامة والمدارس الحكومية فقط.",
      "متعهدو الدفاع والوكالات الحكومية فقط.",
      "متاجر التجزئة المحلية الصغيرة فقط هنا."],
     "For financial institutions, healthcare providers and e-commerce firms, reputation is tied directly to customer retention and revenue flows.",
     "بالنسبة للمؤسسات المالية ومزوّدي الرعاية الصحية وشركات التجارة الإلكترونية، السمعة مرتبطة مباشرة بالاحتفاظ بالعملاء وتدفقات الإيرادات."),

    # 11 -----------------------------------------------------------------
    ("efl_numeric", "Apply",
     "Two threats: a 0.2 chance of a 10 loss, and a 0.1 chance of a 5 loss. What is the expected loss?",
     "تهديدان: احتمال 0.2 لخسارة 10، واحتمال 0.1 لخسارة 5. ما الخسارة المتوقعة؟",
     ["2.5", "3.0", "1.5", "0.5"],
     ["2.5", "3.0", "1.5", "0.5"],
     "Each term is probability times impact: 0.2 x 10 = 2 and 0.1 x 5 = 0.5. The sum is 2.5.",
     "كل حد هو الاحتمال ضرب التأثير: 0.2 × 10 = 2، و0.1 × 5 = 0.5. والمجموع 2.5."),

    # 12 -----------------------------------------------------------------
    ("dimensions_overlap", "Analyze",
     "Why does one failure matter on all three dimensions at once?",
     "لماذا يؤثر الإخفاق الواحد في الأبعاد الثلاثة معاً؟",
     ["A failure hits money, operations, and trust together.",
      "Only the financial dimension can ever be measured.",
      "The three dimensions never overlap in practice at all.",
      "Operational risk is the only one that really matters."],
     ["الإخفاق يضرب المال والتشغيل والثقة معاً.",
      "البعد المالي وحده هو القابل للقياس.",
      "الأبعاد الثلاثة لا تتقاطع عملياً أبداً هنا.",
      "الخطر التشغيلي هو الوحيد المهم فعلاً."],
     "The same incident produces a bill, a service interruption and a loss of confidence, which is why the three are listed as one risk seen from three sides.",
     "الحادث نفسه ينتج فاتورة وانقطاع خدمة وفقدان ثقة، ولهذا تُسرد الثلاثة كخطر واحد يُرى من ثلاث جهات."),
]

KEY = "ABCDABCDABCD"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
