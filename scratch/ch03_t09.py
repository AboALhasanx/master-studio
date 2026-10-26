#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch03 T09 — What a policy is like, and what it is worth strategically."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch03_lib import build

QUIZ = "Quiz_Ch03_T09_Strategic_Role_Of_Policies"
TOPIC_EN = "Policy Characteristics & Strategic Value"
TOPIC_AR = "خصائص السياسة وقيمتها الاستراتيجية"

I = [
    # 1 -------------------------------------------------------------------
    ("characteristics_count", "Remember",
     "How many characteristics of a security policy are named?",
     "كم خاصية لسياسة الأمن تُذكر؟",
     ["Four characteristics.", "Three characteristics.",
      "Five characteristics.", "Six characteristics."],
     ["أربع خصائص.", "ثلاث خصائص.", "خمس خصائص.", "ست خصائص."],
     "Four: high-level guidance, alignment with risk, organization-wide, and a living document.",
     "أربع: إرشاد عالي المستوى، وتوافق مع المخاطر، وشمول للمؤسسة، ووثيقة حيّة."),

    # 2 -------------------------------------------------------------------
    ("high_level_guidance", "Remember",
     "What does high-level guidance mean?",
     "ماذا يعني الإرشاد عالي المستوى؟",
     ["It states what must be done, not necessarily how.",
      "It states how each tool must be configured exactly.",
      "It lists every technical control in detail.",
      "It replaces the technical standards entirely."],
     ["تبيّن ما يجب عمله لا كيف بالضرورة.",
      "تبيّن كيف يُضبط كل أداة بدقة تامة.",
      "تسرد كل ضابط تقني بالتفصيل.",
      "تستبدل المعايير التقنية بالكامل."],
     "A policy says what has to be achieved. The how belongs to the standards and the technical procedures underneath it.",
     "السياسة تقول ما يجب تحقيقه. أما الكيف فيعود للمعايير والإجراءات التقنية تحتها."),

    # 3 -------------------------------------------------------------------
    ("alignment_with_risk", "Remember",
     "Where is a policy's content supposed to come from?",
     "من أين يُفترض أن يأتي مضمون السياسة؟",
     ["It is derived from the risk assessment.",
      "It is derived from the vendor's catalogue.",
      "It is derived from the legal department.",
      "It is derived from last year's budget."],
     ["مستمدّة من تقييم المخاطر الفعلي.",
      "مستمدّة من كتالوج المورّد الجاهز.",
      "مستمدّة من القسم القانوني وحده.",
      "مستمدّة من ميزانية العام الماضي."],
     "A policy has to address the actual threats, so it is derived from the risk assessment rather than copied from a template.",
     "السياسة يجب أن تعالج التهديدات الفعلية، فهي مستمدّة من تقييم المخاطر لا منسوخة من قالب."),

    # 4 -------------------------------------------------------------------
    ("organization_wide", "Remember",
     "Whom does an organization-wide policy cover?",
     "من تغطيه السياسة الشاملة للمؤسسة؟",
     ["It applies to staff, contractors, and third parties.",
      "It applies to the IT department only here today still.",
      "It applies to permanent employees only here.",
      "It applies to new joiners for the first six months."],
     ["تنطبق على الموظفين والمتعاقدين والغير.",
      "تنطبق على قسم التقنية وحده هنا تماماً.",
      "تنطبق على الموظفين الدائمين هنا تماماً.",
      "تنطبق على الموظفين الجدد ستة أشهر هنا."],
     "It applies across departments, to employees, contractors, and third parties: everyone who can touch an asset.",
     "تنطبق على كل الأقسام، على الموظفين والمتعاقدين والأطراف الثالثة: كل من يمكنه الوصول إلى أصل."),

    # 5 -------------------------------------------------------------------
    ("living_document", "Remember",
     "What does calling it a living document mean?",
     "ماذا يعني وصفها بأنها وثيقة حيّة؟",
     ["It evolves as threats and technology change.",
      "It is signed once and never reopened again.",
      "It is rewritten from scratch every year here.",
      "It is archived right after the first audit."],
     ["تتطور مع تغيّر التهديدات والتقنية.",
      "تُوقَّع مرة واحدة ولا تُفتح أبداً.",
      "تُعاد كتابتها من الصفر كل سنة هنا.",
      "تُؤرشف بعد أول تدقيق أمني كامل."],
     "It evolves as threats, technologies and regulations change, so a policy that is never revised is already out of date.",
     "تتطور مع تغيّر التهديدات والتقنيات والأنظمة، فسياسة لا تُراجَع أبداً صارت قديمة أصلاً."),

    # 6 -------------------------------------------------------------------
    ("strategic_benefits", "Remember",
     "Which five strategic benefits does a policy bring?",
     "أي خمس فوائد استراتيجية تجلبها السياسة؟",
     ["Consistency, accountability, compliance, culture, resilience.",
      "Speed, savings, scale, secrecy, and very strict control.",
      "Detection, response, recovery, learning, and full closure.",
      "Design, build, test, deploy, and final retirement here today."],
     ["الاتساق والمساءلة والامتثال والثقافة والصمود.",
      "السرعة والتوفير والحجم والسرية والضبط التام.",
      "الكشف والاستجابة والتعافي والتعلّم والإغلاق.",
      "التصميم والبناء والاختبار والنشر والإيقاف."],
     "Five: consistency, accountability, compliance, culture, and resilience.",
     "خمس: الاتساق، والمساءلة، والامتثال، والثقافة، والصمود."),

    # 7 -------------------------------------------------------------------
    ("benefit_consistency", "Remember",
     "What does the consistency benefit mean?",
     "ماذا تعني فائدة الاتساق؟",
     ["Standardised practice across departments.",
      "Clear roles and clear responsibilities for all.",
      "Alignment with laws and standards.",
      "Awareness embedded in daily routines."],
     ["ممارسات موحّدة عبر الأقسام.",
      "أدوار ومسؤوليات واضحة تماماً.",
      "توافق مع القوانين والمعايير.",
      "وعي مندمج في الروتين اليومي."],
     "Consistency means the same practice everywhere, so two departments cannot answer the same question differently.",
     "الاتساق يعني الممارسة نفسها في كل مكان، فلا يجيب قسمان إجابة مختلفة عن السؤال نفسه."),

    # 8 -------------------------------------------------------------------
    ("benefit_culture", "Understand",
     "What does the culture benefit mean?",
     "ماذا تعني فائدة الثقافة؟",
     ["Awareness embedded in daily routines.",
      "Standardised practice across departments.",
      "Clear roles and clear responsibilities for all.",
      "Alignment with laws and standards."],
     ["وعي مندمج في الروتين اليومي.",
      "ممارسات موحّدة عبر الأقسام.",
      "أدوار ومسؤوليات واضحة تماماً.",
      "توافق مع القوانين والمعايير."],
     "Culture means security awareness becomes part of the daily routine rather than a yearly briefing nobody remembers.",
     "الثقافة تعني أن يصبح الوعي الأمني جزءاً من الروتين اليومي لا محاضرة سنوية لا يتذكرها أحد."),

    # 9 -------------------------------------------------------------------
    ("benefit_resilience", "Remember",
     "What does the resilience benefit mean?",
     "ماذا تعني فائدة الصمود؟",
     ["Supporting continuity and crisis response.",
      "Standardised practice across all departments.",
      "Clear roles and clear responsibilities here.",
      "Awareness embedded in daily routines."],
     ["دعم الاستمرارية والاستجابة للأزمات.",
      "ممارسات موحّدة عبر كل الأقسام هنا.",
      "أدوار ومسؤوليات واضحة تماماً هنا.",
      "وعي مندمج في الروتين اليومي."],
     "Resilience is about business continuity and crisis response: the policy already says who does what when the incident lands.",
     "الصمود يخص استمرارية الأعمال والاستجابة للأزمات: السياسة تقول مسبقاً من يفعل ماذا حين يقع الحادث."),

    # 10 ------------------------------------------------------------------
    ("strategic_enabler", "Understand",
     "What do policies turn cybersecurity into?",
     "إلى ماذا تحوّل السياسات الأمن السيبراني؟",
     ["A strategic enabler of trust and compliance.",
      "A purely technical exercise for the IT team.",
      "An optional document for the auditors only.",
      "A temporary project for the board here."],
     ["مُمكّن استراتيجي للثقة والامتثال.",
      "تمرين تقني بحت لفريق التقنية فقط.",
      "مستند اختياري للمدققين فقط هنا.",
      "مشروع مؤقت لمجلس الإدارة هنا تماماً."],
     "Policies lift cybersecurity from a technical exercise into a strategic enabler of trust, resilience and compliance.",
     "السياسات ترفع الأمن السيبراني من تمرين تقني إلى مُمكّن استراتيجي للثقة والصمود والامتثال."),
]

KEY = "ABCDABCDAB"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
