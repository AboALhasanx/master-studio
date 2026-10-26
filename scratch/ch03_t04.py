#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch03 T04 — Risk management as the bridge, and as a continuous cycle."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch03_lib import build

QUIZ = "Quiz_Ch03_T04_Governance_Bridge_And_Cycle"
TOPIC_EN = "The Governance Bridge & the Risk Cycle"
TOPIC_AR = "جسر الحوكمة ودورة إدارة المخاطر"

I = [
    # 1 -------------------------------------------------------------------
    ("bridge_role", "Understand",
     "What role does cybersecurity risk management play between the two sides?",
     "أي دور تلعبه إدارة مخاطر الأمن السيبراني بين الجانبين؟",
     ["It translates technical risk into business risk.",
      "It replaces the governance structures entirely.",
      "It removes the need for technical controls here.",
      "It reports incidents after they have happened."],
     ["يترجم الخطر التقني إلى خطر أعمال.",
      "يستبدل هياكل الحوكمة بالكامل هنا.",
      "يغني عن الضوابط التقنية كلها هنا.",
      "يبلّغ عن الحوادث بعد وقوعها فعلاً."],
     "It is the bridge: it translates technical vulnerabilities into business risks that executives can understand and act on.",
     "هو الجسر: يترجم الثغرات التقنية إلى مخاطر أعمال يفهمها التنفيذيون ويستطيعون التصرف بناءً عليها."),

    # 2 -------------------------------------------------------------------
    ("technical_controls_list", "Remember",
     "Which set lists the technical controls?",
     "أي مجموعة تسرد الضوابط التقنية؟",
     ["Firewalls, IDS, antivirus, and patching.",
      "Policies, compliance, and oversight.",
      "Budgets, staffing, and staff training too.",
      "Contracts, audits, and insurance."],
     ["الجدران النارية وكشف التطفل والتحديث.",
      "السياسات والامتثال والإشراف التنفيذي.",
      "الميزانيات والموظفون والتدريب المستمر.",
      "العقود والتدقيق والتأمين السنوي."],
     "Technical controls are firewalls, intrusion detection, antivirus, and patching: the machine-level measures.",
     "الضوابط التقنية هي الجدران النارية وكشف التطفل ومكافحة الفيروسات والتحديث: تدابير مستوى الآلة."),

    # 3 -------------------------------------------------------------------
    ("governance_structures_list", "Remember",
     "Which set lists the governance structures?",
     "أي مجموعة تسرد هياكل الحوكمة؟",
     ["Policies, compliance frameworks, and oversight.",
      "Firewalls, IDS, antivirus, and regular patching.",
      "Backups, redundancy, and response plans.",
      "Encryption, tokens, and access control."],
     ["السياسات وأطر الامتثال والإشراف التنفيذي.",
      "الجدران النارية وكشف التطفل والتحديث.",
      "النسخ الاحتياطي والتكرار وخطط الاستجابة.",
      "التشفير والرموز والتحكم بالوصول كله هنا."],
     "Governance structures are policies, compliance frameworks, and executive oversight: the decision layer above the tools.",
     "هياكل الحوكمة هي السياسات وأطر الامتثال والإشراف التنفيذي: طبقة القرار فوق الأدوات."),

    # 4 -------------------------------------------------------------------
    ("silos_without_rm", "Understand",
     "What happens to the two sides without risk management?",
     "ماذا يحدث للجانبين بدون إدارة المخاطر؟",
     ["The two operate in silos without it.",
      "The two merge into one single team.",
      "The two replace each other entirely.",
      "The two are legally required to merge."],
     ["يعمل الجانبان في جزر معزولة.",
      "يندمج الجانبان في فريق واحد.",
      "يستبدل كل جانب الآخر كلياً.",
      "يُلزَم الجانبان بالاندماج قانوناً."],
     "Without risk management the technical side and the governance side operate in silos, each with its own language and its own priorities.",
     "بدون إدارة المخاطر يعمل الجانب التقني وجانب الحوكمة في جزر معزولة، لكل منهما لغته وأولوياته."),

    # 5 -------------------------------------------------------------------
    ("patch_becomes_business_risk", "Analyze",
     "A missing patch is found on a server. What does risk management turn it into?",
     "تحديث ناقص يُكتشف على خادم. إلى ماذا تحوّله إدارة المخاطر؟",
     ["A quantified business risk executives can rank.",
      "A technical ticket for the IT team only here.",
      "A compliance exception granted to the auditor.",
      "An incident report written after the fact here."],
     ["خطر أعمال كمي يستطيع التنفيذيون ترتيبه.",
      "تذكرة تقنية لفريق التقنية فقط هنا تماماً.",
      "استثناء امتثال يُمنح للمدقق هنا.",
      "تقرير حادث يُكتب بعد الواقعة فعلاً هنا."],
     "It quantifies the finding in financial and operational terms, so a patch becomes a ranked business risk instead of a ticket nobody funds.",
     "يقدّر النتيجة مالياً وتشغيلياً، فيصبح التحديث خطر أعمال مرتباً لا تذكرة بلا تمويل."),

    # 6 -------------------------------------------------------------------
    ("not_one_time", "Remember",
     "Is risk management a one-time assessment?",
     "هل إدارة المخاطر تقييم يُجرى مرة واحدة؟",
     ["No, it is a continuous cycle always.",
      "Yes, once a year is easily enough.",
      "Yes, one assessment for each system.",
      "Only when an incident actually occurs."],
     ["لا، هي دورة مستمرة دائماً.",
      "نعم، مرة واحدة في السنة تكفي.",
      "نعم، تقييم واحد لكل نظام.",
      "فقط عند وقوع حادث أمني كبير."],
     "It is not a one-time assessment. It is a continuous cycle integrated into enterprise operations.",
     "ليست تقييماً يُجرى مرة واحدة، بل دورة مستمرة مندمجة في عمليات المؤسسة."),

    # 7 -------------------------------------------------------------------
    ("cycle_steps", "Remember",
     "Which five steps make up the risk management cycle?",
     "أي خمس خطوات تشكّل دورة إدارة المخاطر؟",
     ["Identify, assess, mitigate, monitor, review.",
      "Plan, do, check, act, and then report.",
      "Detect, respond, recover, learn, and then close.",
      "Design, build, test, deploy, and then retire."],
     ["تحديد وتقييم وتخفيف ومراقبة ومراجعة.",
      "تخطيط وتنفيذ وتحقق وتصحيح وتقرير.",
      "كشف واستجابة وتعافٍ وتعلّم وإغلاق.",
      "تصميم وبناء واختبار ونشر وإيقاف نهائي."],
     "The cycle runs identify, assess, mitigate, monitor, review. It is the risk cycle, not the incident-response cycle.",
     "الدورة: تحديد، تقييم، تخفيف، مراقبة، مراجعة. وهي دورة المخاطر لا دورة الاستجابة للحوادث."),

    # 8 -------------------------------------------------------------------
    ("identify_step", "Remember",
     "What does the identify step cover?",
     "ماذا تغطي خطوة التحديد؟",
     ["Assets, vulnerabilities, and threats.",
      "Probability and impact of each risk.",
      "Controls and their cost for each asset.",
      "Incidents recorded in the last year."],
     ["الأصول والثغرات والتهديدات.",
      "احتمال كل خطر وتأثيره عليه.",
      "الضوابط وكلفتها لكل أصل هنا.",
      "الحوادث المسجلة في السنة الماضية."],
     "Identify catalogues the assets, the vulnerabilities, and the threats that could reach them.",
     "التحديد يجرد الأصول والثغرات والتهديدات التي قد تصل إليها."),

    # 9 -------------------------------------------------------------------
    ("assess_step", "Remember",
     "What does the assess step measure?",
     "ماذا تقيس خطوة التقييم؟",
     ["Probability and impact.", "Assets and their threats.",
      "Controls and costs.", "Incidents and losses."],
     ["الاحتمال والتأثير.", "الأصول والتهديدات.",
      "الضوابط والكلف.", "الحوادث والخسائر."],
     "Assess puts a probability and an impact on each identified risk, which is what makes ranking possible.",
     "التقييم يضع احتمالاً وتأثيراً لكل خطر محدد، وهذا ما يجعل الترتيب ممكناً."),

    # 10 ------------------------------------------------------------------
    ("nist_role", "Remember",
     "What does NIST SP 800-37 do?",
     "ماذا يفعل NIST SP 800-37؟",
     ["It formalises the risk management process.",
      "It replaces the technical controls entirely.",
      "It lists the industry sectors at risk.",
      "It measures policy compliance only."],
     ["إنه يُقنن عملية إدارة المخاطر.",
      "إنه يستبدل الضوابط التقنية.",
      "إنه يسرد القطاعات المعرضة للخطر.",
      "إنه يقيس الامتثال للسياسة فقط."],
     "NIST SP 800-37 formalises the risk management process, which is why it is named as the reference for the cycle.",
     "NIST SP 800-37 يُقنن عملية إدارة المخاطر، ولهذا يُذكر كمرجع للدورة."),

    # 11 ------------------------------------------------------------------
    ("why_continuous", "Understand",
     "Why must the cycle keep running?",
     "لماذا يجب أن تستمر الدورة؟",
     ["New vulnerabilities emerge constantly.",
      "The auditors require quarterly reports.",
      "The budget changes every single year.",
      "The staff changes every single year."],
     ["ثغرات جديدة تظهر باستمرار.",
      "المدققون يطلبون تقارير فصلية.",
      "الميزانية تتغير كل سنة.",
      "الموظفون يتغيرون كل سنة."],
     "New vulnerabilities appear continuously and the risk profile moves with them, so an assessment that stops is already out of date.",
     "ثغرات جديدة تظهر باستمرار ويتحرك ملف المخاطر معها، فتقييم يتوقف يصبح قديماً فوراً."),
]

KEY = "ABCDABCDABC"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
