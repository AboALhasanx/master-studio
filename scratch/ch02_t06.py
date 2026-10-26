#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch02 T06 — ISO/IEC 27002: who writes it, what it counts, and what it is for."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch02_lib import build

QUIZ = "Quiz_Ch02_T06_ISO_IEC_27002"
TOPIC_EN = "ISO/IEC 27002: Scope, Count and Role"
TOPIC_AR = "ISO/IEC 27002: النطاق والعدد والدور"

I = [
    # 1 -------------------------------------------------------------------
    ("joint_developers", "Remember",
     "Which two bodies develop the series ISO/IEC 27002 belongs to?",
     "أي هيئتين تطوّران السلسلة التي ينتمي إليها ISO/IEC 27002؟",
     ["ISO and IEC, working together.",
      "ISO alone, with national bodies.",
      "IEC alone, with vendor groups.",
      "ANSI and NIST, working together."],
     ["منظمتا ISO و IEC معاً بشكل مشترك.",
      "منظمة ISO وحدها مع هيئات وطنية.",
      "منظمة IEC وحدها مع مجموعات موردين.",
      "منظمتا ANSI و NIST معاً بشكل مشترك."],
     "The series is developed jointly by ISO and IEC, which is why both names appear in the title.",
     "السلسلة تُطوَّر بالاشتراك بين ISO و IEC، ولهذا يظهر الاسمان في العنوان."),

    # 2 -------------------------------------------------------------------
    ("categories_count", "Remember",
     "Within how many categories does the lecture say ISO/IEC 27002 works?",
     "داخل كم قسماً تقول المحاضرة إن ISO/IEC 27002 يعمل؟",
     ["Fourteen categories.", "Twelve categories.",
      "Sixteen categories.", "Eighteen categories."],
     ["أربعة عشر قسماً.", "اثنا عشر قسماً.",
      "ستة عشر قسماً.", "ثمانية عشر قسماً."],
     "The lecture says the latest version describes what has to be done within fourteen categories.",
     "المحاضرة تقول إن أحدث إصدار يصف ما يجب عمله داخل أربعة عشر قسماً."),

    # 3 -------------------------------------------------------------------
    ("version_year", "Remember",
     "Which year does the lecture give for that version of ISO/IEC 27002?",
     "أي سنة تعطيها المحاضرة لذلك الإصدار من ISO/IEC 27002؟",
     ["2022", "2013", "2019", "2005"],
     ["2022", "2013", "2019", "2005"],
     "The lecture dates the version it describes to 2022.",
     "المحاضرة تؤرّخ الإصدار الذي تصفه بسنة 2022."),

    # 4 -------------------------------------------------------------------
    ("category_cryptography", "Remember",
     "Which category covers the use of cryptography?",
     "أي قسم يغطي استخدام التشفير؟",
     ["The cryptography category of the standard.",
      "The access control category of the standard.",
      "The asset management category of the standard.",
      "The operations security category of it."],
     ["قسم التشفير في المعيار.",
      "قسم التحكم بالوصول فيه.",
      "قسم إدارة الأصول فيه.",
      "قسم أمن العمليات فيه."],
     "One of the fourteen categories is named Cryptography, which is how the standard groups keys, ciphers and their use.",
     "أحد الأقسام الأربعة عشر اسمه التشفير، وفيه تجمع المواصفة المفاتيح والخوارزميات واستخدامها."),

    # 5 -------------------------------------------------------------------
    ("category_supplier", "Remember",
     "Which category covers an external provider that must meet security requirements?",
     "أي قسم يغطي مزوّداً خارجياً يجب أن يلبي متطلبات أمنية؟",
     ["The supplier relationships category.",
      "The access control category of it.",
      "The asset management category of it.",
      "The operations security category."],
     ["قسم علاقات الموردين.",
      "قسم التحكم بالوصول.",
      "قسم إدارة الأصول هنا.",
      "قسم أمن العمليات هنا."],
     "External providers sit under supplier relationships, one of the fourteen categories.",
     "المزوّدون الخارجيون يقعون تحت علاقات الموردين، وهو أحد الأقسام الأربعة عشر."),

    # 6 -------------------------------------------------------------------
    ("category_continuity", "Remember",
     "Which category covers keeping essential operations running through a disruption?",
     "أي قسم يغطي إبقاء العمليات الأساسية عاملة خلال انقطاع؟",
     ["The business continuity category.",
      "The incident management category.",
      "The asset management category.",
      "The access control category."],
     ["قسم استمرارية الأعمال.",
      "قسم إدارة الحوادث الأمنية.",
      "قسم إدارة الأصول هنا.",
      "قسم التحكم بالوصول هنا."],
     "Continuity of operations is its own category: information security aspects of business continuity management.",
     "استمرارية العمليات قسم مستقل: جوانب أمن المعلومات لإدارة استمرارية الأعمال."),

    # 7 -------------------------------------------------------------------
    ("category_human_resource", "Remember",
     "Which category covers screening new employees before they get access?",
     "أي قسم يغطي فحص الموظفين الجدد قبل منحهم الوصول؟",
     ["The human resource security category.",
      "The access control category of it.",
      "The asset management category of it.",
      "The operations security category itself."],
     ["قسم أمن الموارد البشرية.",
      "قسم التحكم بالوصول إليه هنا.",
      "قسم إدارة الأصول هنا.",
      "قسم أمن العمليات هنا."],
     "Screening staff is human resource security. Access control is the separate category that governs permissions.",
     "فحص الموظفين هو أمن الموارد البشرية. أما التحكم بالوصول فهو القسم المنفصل الذي ينظّم الصلاحيات."),

    # 8 -------------------------------------------------------------------
    ("iso_role_among_frameworks", "Understand",
     "What does ISO/IEC 27002 give, compared with the other frameworks?",
     "ماذا يعطي ISO/IEC 27002 مقارنة ببقية الأطر؟",
     ["A checklist of what must be considered.",
      "A model for calculating the risk.",
      "A process with three clear phases.",
      "Objectives for measures that manage risk."],
     ["قائمة بما يجب أن يُؤخذ بالحسبان.",
      "نموذج كامل لحساب الخطر نفسه.",
      "عملية من ثلاث مراحل واضحة تماماً.",
      "أهداف لتدابير يمكنها إدارة الخطر."],
     "ISO/IEC 27002 is the checklist: it says what has to be considered for a secure system. FAIR calculates, OCTAVE runs a process, COBIT sets objectives.",
     "ISO/IEC 27002 هو القائمة: يقول ما يجب أخذه بالحسبان لنظام آمن. وFAIR يحسب، وOCTAVE يدير عملية، وCOBIT يضع أهدافاً."),

    # 9 -------------------------------------------------------------------
    ("count_honest_position", "Analyze",
     "The lecture says the 2022 version works within fourteen categories. What is the honest position?",
     "المحاضرة تقول إن إصدار 2022 يعمل بأربعة عشر قسماً. ما الموقف الصحيح؟",
     ["It matches 2013; 2022 uses four themes.",
      "It is correct and current for the 2022 edition.",
      "It is a printing error in the lecture notes.",
      "It counts controls, not the categories."],
     ["يطابق 2013، أما 2022 فبأربعة محاور.",
      "صحيح وحديث تماماً لإصدار سنة 2022.",
      "خطأ مطبعي في ملاحظات المحاضرة كلها.",
      "يعدّ الضوابط وليس الأقسام نفسها."],
     "Fourteen is the 2013 structure. The 2022 edition reorganised into four themes with 93 controls. Answer in her vocabulary, but know the fact.",
     "الأربعة عشر هي بنية 2013. وإصدار 2022 أعاد التنظيم إلى أربعة محاور و93 ضابطاً. أجب بمفرداتها، لكن اعرف الحقيقة."),

    # 10 ------------------------------------------------------------------
    ("ordering_logic", "Understand",
     "The fourteen categories are described as logically ordered. What does that order let you do?",
     "الأقسام الأربعة عشر موصوفة بأنها مرتبة منطقياً. ماذا يتيح لك هذا الترتيب؟",
     ["It lets you follow a secure system's flow.",
      "It makes the standard easier to translate.",
      "It matches the order of the PDCA cycle.",
      "It groups the categories by their cost."],
     ["لأنها تتيح تتبّع مسار النظام الآمن.",
      "لأنها تسهّل ترجمة المعيار للغات.",
      "لأنها تطابق ترتيب دورة PDCA تماماً.",
      "لأنها تجمع الأقسام حسب كلفتها كلها."],
     "The categories run from policy, through organisation, people and assets, down to compliance, so the order follows how a secure system is built and run.",
     "الأقسام تمشي من السياسة، عبر التنظيم والأفراد والأصول، وصولاً إلى الامتثال، فالترتيب يتبع كيفية بناء النظام الآمن وتشغيله."),
]

KEY = "ABCDABCDAB"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
