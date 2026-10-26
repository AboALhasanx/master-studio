#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch02 T01 — What risk is, what damage is, and the threat/vulnerability chain."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch02_lib import build

QUIZ = "Quiz_Ch02_T01_Risk_And_Threat_Chain"
TOPIC_EN = "Risk, Damage and the Threat Chain"
TOPIC_AR = "الخطر والضرر وسلسلة التهديد"

I = [
    # 1 -------------------------------------------------------------------
    ("risk_technical_meaning", "Remember",
     "In its technical sense, what is risk?",
     "بمعناها التقني، ما هو الخطر؟",
     ["The probability that an error causes damage.",
      "The damage that has already happened to you.",
      "The weakness that an attacker can exploit.",
      "The cost of the controls already applied."],
     ["احتمال أن يسبب خطأ ما ضرراً.",
      "الضرر الذي وقع فعلاً بالفعل.",
      "نقطة الضعف التي يستغلها المهاجم.",
      "تكلفة الضوابط المطبّقة حالياً."],
     "Risk is a probability, not the damage itself: the quantitative probability that an error situation occurs and gives rise to damage.",
     "الخطر احتمال وليس الضرر نفسه: الاحتمال الكمي لوقوع حالة خطأ ينتج عنها ضرر."),

    # 2 -------------------------------------------------------------------
    ("damage_is_policy_breach", "Remember",
     "In IT security, what counts as damage?",
     "في أمن المعلومات، ما الذي يُعدّ ضرراً؟",
     ["A breach of the security policy.",
      "A failure of the network hardware.",
      "A loss of the stored user passwords.",
      "A gap in the security budget."],
     ["خرق لسياسة الأمن المتفق عليها.",
      "عطل في عتاد الشبكة نفسه.",
      "فقدان كلمات مرور المستخدمين.",
      "نقص في ميزانية الأمن المخصصة."],
     "Damage is synonymous with a breach of the security policy, so it is defined by the rules, not by hardware failure.",
     "الضرر مرادف لخرق سياسة الأمن، فهو يُعرَّف بالقواعد لا بتعطل العتاد."),

    # 3 -------------------------------------------------------------------
    ("subjective_risk_factors", "Remember",
     "Which factors belong to subjective risk?",
     "أي عوامل تنتمي إلى الخطر الذاتي؟",
     ["Public attitudes, trust, and personality.",
      "Frequency of attempts and consequences.",
      "Number of controls and their strength.",
      "Policy breaches recorded in one year."],
     ["المواقف العامة والثقة والشخصية.",
      "تكرار المحاولات وحجم العواقب.",
      "عدد الضوابط الأمنية وقوة كل منها.",
      "حالات خرق السياسة المسجلة في سنة."],
     "Subjective risk adds the human factors: public attitudes, trust, and personality. Objective risk is the numeric one.",
     "الخطر الذاتي يضيف العوامل البشرية: المواقف العامة والثقة والشخصية. أما الخطر الموضوعي فهو الرقمي."),

    # 4 -------------------------------------------------------------------
    ("vulnerability_meaning", "Remember",
     "What is a vulnerability?",
     "ما هي الثغرة؟",
     ["A weakness that can be exploited for damage.",
      "A threat that has already caused real damage.",
      "A control that blocks a threat from arriving.",
      "A policy that forbids a risky behaviour at work."],
     ["نقطة ضعف قابلة للاستغلال لإحداث ضرر.",
      "تهديد وقع وأحدث ضرراً فعلياً بالنظام.",
      "ضابط أمني يمنع التهديد من الوصول.",
      "سياسة تمنع سلوكاً خطراً في العمل."],
     "A vulnerability is a weakness that can be exploited to damage the system. It is not the attacker and not the resulting loss.",
     "الثغرة نقطة ضعف يمكن استغلالها لإلحاق الضرر بالنظام. ليست المهاجم ولا الخسارة الناتجة."),

    # 5 -------------------------------------------------------------------
    ("damage_condition", "Understand",
     "When does damage occur in an IT system?",
     "متى يقع الضرر في نظام معلوماتي؟",
     ["When a threat is realised against a weakness.",
      "When a policy is written and then ignored.",
      "When a control is installed but not tested.",
      "When a threat exists anywhere in the world."],
     ["عندما يتحقق تهديد ضد نقطة ضعف.",
      "عندما تُكتب سياسة ثم تُهمَل.",
      "عندما يُثبَّت ضابط دون اختباره.",
      "عندما يوجد تهديد في أي مكان بالعالم."],
     "Damage needs both: a threat that is realised and a weakness for it to act on. A threat alone is not enough.",
     "الضرر يحتاج الاثنين معاً: تهديد يتحقق وضعف يعمل عليه. التهديد وحده لا يكفي."),

    # 6 -------------------------------------------------------------------
    ("chain_order", "Remember",
     "What is the order of the chain?",
     "ما ترتيب السلسلة؟",
     ["Threat, then vulnerability, then damage.",
      "Vulnerability, then threat, then damage.",
      "Damage, then threat, then vulnerability.",
      "Threat, then damage, then vulnerability."],
     ["تهديد ثم ثغرة ثم ضرر.",
      "ثغرة ثم تهديد ثم ضرر.",
      "ضرر ثم تهديد ثم ثغرة.",
      "تهديد ثم ضرر ثم ثغرة."],
     "The chain runs threat, then vulnerability, then damage: the threat acts on the weakness, and the result is damage.",
     "السلسلة تجري: تهديد ثم ثغرة ثم ضرر. التهديد يعمل على الضعف، والنتيجة ضرر."),

    # 7 -------------------------------------------------------------------
    ("shark_figure_mapping", "Understand",
     "In the shark-cage figure, which mapping is correct?",
     "في شكل قفص القرش، أي مطابقة صحيحة؟",
     ["Shark is the threat, welding fault is the vulnerability.",
      "Shark is the vulnerability, welding fault is the threat.",
      "Shark is the asset, welding fault is the threat.",
      "Shark is the damage, welding fault is the asset."],
     ["القرش هو التهديد وعيب اللحام هو الثغرة.",
      "القرش هو الثغرة وعيب اللحام هو التهديد.",
      "القرش هو الأصل وعيب اللحام هو التهديد.",
      "القرش هو الضرر وعيب اللحام هو الأصل."],
     "The shark is the threat and the welding fault in the cage is the vulnerability. The diver inside is the asset being protected.",
     "القرش هو التهديد، وعيب اللحام في القفص هو الثغرة. والغوّاص في الداخل هو الأصل المحمي."),

    # 8 -------------------------------------------------------------------
    ("chain_without_vulnerability", "Apply",
     "A shark circles a cage whose welds are intact. What follows?",
     "قرش يدور حول قفص لحامه سليم. ماذا ينتج؟",
     ["No damage occurs, because there is no flaw.",
      "Damage occurs, because the threat is present.",
      "Damage occurs, because the cage is the asset.",
      "No damage occurs, because the shark is the asset."],
     ["لا يقع ضرر لأن ماكو ثغرة.",
      "يقع ضرر لأن التهديد موجود.",
      "يقع ضرر لأن القفص هو الأصل.",
      "لا يقع ضرر لأن القرش هو الأصل."],
     "The threat is there, but with no weakness to act on the chain never reaches damage. That is the point of the figure.",
     "التهديد موجود، لكن بلا ضعف يعمل عليه لا تصل السلسلة إلى الضرر. وهذا مغزى الشكل."),

    # 9 -------------------------------------------------------------------
    ("scenario_threat_vs_vulnerability", "Apply",
     "A storm is forecast over a data centre with a cracked roof seal. Which part is the vulnerability?",
     "عاصفة متوقعة فوق مركز بيانات إحكام سطحه متصدّع. أي جزء هو الثغرة؟",
     ["The cracked seal on the roof.",
      "The storm that is forecast.",
      "The data centre building.",
      "The servers inside the room."],
     ["العيب في إحكام السطح.",
      "العاصفة القوية المتوقعة.",
      "مبنى مركز البيانات نفسه.",
      "الخوادم الموجودة داخل الغرفة."],
     "The storm is the threat and the cracked seal is the vulnerability. The servers are the asset that would be damaged.",
     "العاصفة هي التهديد، والإحكام المتصدّع هو الثغرة. والخوادم هي الأصل الذي يتضرر."),

    # 10 ------------------------------------------------------------------
    ("objective_definition_basis", "Understand",
     "Why is risk defined as an objective quantity?",
     "لماذا يُعرَّف الخطر كمقدار موضوعي؟",
     ["It is measured in numbers, not in feelings.",
      "It was written by an international standard body.",
      "It ignores the human factor on purpose.",
      "It applies only to technical systems."],
     ["لأنها تُقاس بالأرقام لا بالمشاعر.",
      "لأنها كتبها جهة معايير دولية.",
      "لأنها تتجاهل العامل البشري عمداً.",
      "لأنها تخص الأنظمة التقنية فقط."],
     "Objective means numeric and measurable. Subjective risk is the separate notion that also counts attitudes, trust and personality.",
     "الموضوعي يعني رقمياً قابلاً للقياس. والخطر الذاتي مفهوم منفصل يحسب أيضاً المواقف والثقة والشخصية."),
]

KEY = "ACBDABCDAC"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
