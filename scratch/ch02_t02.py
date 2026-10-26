#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch02 T02 — Basic risk, residual risk, and the two colour matrices."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch02_lib import build

QUIZ = "Quiz_Ch02_T02_Two_Equations_And_Matrices"
TOPIC_EN = "Basic Risk, Residual Risk & Their Matrices"
TOPIC_AR = "الخطر الأساسي والمتبقي ومصفوفتاهما"

I = [
    # 1 -------------------------------------------------------------------
    ("basic_risk_meaning", "Remember",
     "What does the basic risk S express?",
     "ماذا يعبّر عنه الخطر الأساسي S؟",
     ["The risk before countermeasures are applied.",
      "The risk left after countermeasures act.",
      "The number of countermeasures in place.",
      "The frequency of attacks over one year."],
     ["الخطر قبل تطبيق أي ضابط أمني.",
      "الخطر المتبقي بعد عمل الضوابط.",
      "عدد الضوابط الأمنية الموجودة.",
      "تكرار الهجمات خلال سنة واحدة."],
     "Basic risk is the risk of a threat as it stands, before any countermeasure is counted. Residual risk is what is left afterwards.",
     "الخطر الأساسي هو خطر التهديد كما هو، قبل احتساب أي ضابط. والخطر المتبقي هو ما يبقى بعده."),

    # 2 -------------------------------------------------------------------
    ("frequency_meaning", "Remember",
     "In the basic risk equation, what does F represent?",
     "في معادلة الخطر الأساسي، ماذا يمثّل F؟",
     ["How often attempts are made to exploit it.",
      "How much damage a success would cause.",
      "How many controls protect the asset.",
      "How long the asset stays offline after an attack."],
     ["كم مرة تُشنّ محاولات لاستغلالها.",
      "مقدار الضرر لو نجحت المحاولة.",
      "عدد الضوابط التي تحمي الأصل.",
      "مدة بقاء الأصل متوقفاً بعد الهجوم."],
     "F is the frequency of attempts to exploit the vulnerability, not the number of successes.",
     "F هو تكرار محاولات استغلال الثغرة، لا عدد المحاولات الناجحة."),

    # 3 -------------------------------------------------------------------
    ("consequences_meaning", "Remember",
     "In the same equation, what does K represent?",
     "في المعادلة نفسها، ماذا يمثّل K؟",
     ["The damage a successful attempt would cause.",
      "How often attempts are made against the asset.",
      "How many countermeasures are in place there.",
      "How quickly the incident is detected and closed."],
     ["حجم الضرر لو نجحت المحاولة.",
      "كم مرة تُشنّ المحاولات ضد الأصل.",
      "عدد الضوابط الأمنية الموجودة.",
      "سرعة كشف الحادث وإغلاقه."],
     "K is the consequences of one successful attempt: the size of the loss, not how often it happens.",
     "K هو عواقب محاولة واحدة ناجحة: حجم الخسارة، لا تكرارها."),

    # 4 -------------------------------------------------------------------
    ("multiplication_rationale", "Understand",
     "Why is basic risk a product rather than a sum?",
     "لماذا الخطر الأساسي حاصل ضرب لا مجموع؟",
     ["Because both must be high for risk to be high.",
      "Because addition cannot handle three factors.",
      "Because the lecture prefers the shorter formulas.",
      "Because colours need two numbers to combine."],
     ["لأن الخطر يعلى فقط إذا علا الاثنان.",
      "لأن الجمع لا يستوعب ثلاثة عوامل.",
      "لأن المحاضرة تفضّل الصيغ الأقصر.",
      "لأن الألوان تحتاج رقمين للدمج."],
     "With a sum, a huge consequence would make the risk high even if the attempt almost never happens. A product keeps the risk low unless both factors rise.",
     "بالمجموع، عاقبة ضخمة تجعل الخطر عالياً حتى لو كانت المحاولة نادرة جداً. وحاصل الضرب يُبقي الخطر منخفضاً إلا إذا علا العاملان معاً."),

    # 5 -------------------------------------------------------------------
    ("risk_matrix_red", "Remember",
     "Where does the red area of the risk matrix sit?",
     "أين يقع المنطقة الحمراء في مصفوفة الخطر؟",
     ["High frequency and high consequences together.",
      "High frequency together with low consequences.",
      "Low frequency together with high consequences.",
      "Low frequency and low consequences together."],
     ["تكرار عالٍ وعواقب عالية معاً.",
      "تكرار عالٍ مع عواقب منخفضة.",
      "تكرار منخفض مع عواقب عالية.",
      "تكرار منخفض وعواقب منخفضة معاً."],
     "Red needs both axes high. One high and one low gives yellow, and both low gives green.",
     "الأحمر يحتاج المحورين عاليين. واحد عالٍ وواحد منخفض يعطي أصفر، وكلاهما منخفض يعطي أخضر."),

    # 6 -------------------------------------------------------------------
    ("residual_matrix_red", "Remember",
     "Where does the red area of the residual risk matrix sit?",
     "أين تقع المنطقة الحمراء في مصفوفة الخطر المتبقي؟",
     ["High risk and low countermeasures together.",
      "High risk and high countermeasures together.",
      "Low risk and low countermeasures together.",
      "Low risk and high countermeasures together."],
     ["خطر عالٍ وضوابط قليلة معاً.",
      "خطر عالٍ وضوابط كثيرة معاً.",
      "خطر منخفض وضوابط قليلة معاً.",
      "خطر منخفض وضوابط كثيرة معاً."],
     "The second matrix has risk and countermeasures as its axes, and it is mirror-symmetric to the first: red is high risk with few countermeasures.",
     "المصفوفة الثانية محوراها الخطر والضوابط، وهي معكوسة تناظرياً للأولى: الأحمر خطر عالٍ مع ضوابط قليلة."),

    # 7 -------------------------------------------------------------------
    ("countermeasure_level_covers", "Remember",
     "What does the level of countermeasures M cover?",
     "ماذا يغطي مستوى الضوابط M؟",
     ["How many countermeasures there are and how effective.",
      "How many countermeasures there are, and what they cost.",
      "How effective the countermeasures are, and their age.",
      "How many attacks the countermeasures blocked this year."],
     ["عدد الضوابط الموجودة ومدى فعاليتها.",
      "عدد الضوابط الموجودة وتكلفتها.",
      "مدى فعالية الضوابط وعمرها الزمني.",
      "عدد الهجمات التي صدّتها الضوابط."],
     "M covers two things together: the number of countermeasures and their effectiveness. The lecture calls these the influencing factors.",
     "M يغطي شيئين معاً: عدد الضوابط ومدى فعاليتها. والمحاضرة تسمّي هذه العوامل المؤثرة."),

    # 8 -------------------------------------------------------------------
    ("denominator_rationale", "Understand",
     "Why does M sit in the denominator of the residual equation?",
     "لماذا يقع M في مقام معادلة الخطر المتبقي؟",
     ["Because more countermeasures leave less risk.",
      "Because countermeasures add to the total risk.",
      "Because the equation needs a second variable.",
      "Because countermeasures are measured in levels."],
     ["لأن زيادة الضوابط تترك خطراً أقل.",
      "لأن الضوابط تضيف إلى الخطر الكلي.",
      "لأن المعادلة تحتاج متغيراً ثانياً.",
      "لأن الضوابط تُقاس بمستويات."],
     "Division makes residual risk fall as M rises. If M were added or multiplied, stronger defences would raise the risk instead of lowering it.",
     "القسمة تجعل الخطر المتبقي ينخفض كلما علا M. ولو كان M يُجمع أو يُضرب، لرفعت الدفاعات الأقوى الخطر بدل أن تخفضه."),

    # 9 -------------------------------------------------------------------
    ("two_stage_relationship", "Understand",
     "How do the two equations relate?",
     "كيف ترتبط المعادلتان؟",
     ["The first produces S, and the second consumes it.",
      "The two are alternatives for the same quantity.",
      "The second produces S, and the first consumes it.",
      "They are independent and never share a term."],
     ["الأولى تنتج S والثانية تستهلكه.",
      "الاثنتان بديلان لنفس الكمية.",
      "الثانية تنتج S والأولى تستهلكه.",
      "مستقلتان ولا تشتركان بأي حد."],
     "They are two stages, not two choices: S is computed first, then fed into the residual equation as its numerator.",
     "هما مرحلتان لا خياران: S يُحسب أولاً، ثم يدخل معادلة الخطر المتبقي كبسط لها."),

    # 10 ------------------------------------------------------------------
    ("basic_risk_numeric", "Apply",
     "A threat has frequency 4 and consequences 50. What is its basic risk?",
     "تهديد تكراره 4 وعواقبه 50. ما خطرُه الأساسي؟",
     ["200", "240", "160", "100"],
     ["200", "240", "160", "100"],
     "Basic risk is frequency times consequences: 4 x 50 = 200.",
     "الخطر الأساسي هو التكرار ضرب العواقب: 4 × 50 = 200."),

    # 11 ------------------------------------------------------------------
    ("residual_numeric", "Apply",
     "A threat has basic risk 200 and the countermeasures reach level 4. What is the residual risk?",
     "تهديد خطره الأساسي 200 ومستوى الضوابط عنده 4. ما الخطر المتبقي؟",
     ["50", "40", "80", "60"],
     ["50", "40", "80", "60"],
     "Residual risk is basic risk divided by the level: 200 / 4 = 50.",
     "الخطر المتبقي هو الخطر الأساسي مقسوماً على المستوى: 200 ÷ 4 = 50."),

    # 12 ------------------------------------------------------------------
    ("same_risk_different_residual", "Apply",
     "Two departments face the same basic risk. A applies two effective controls, B applies one weak one. What follows?",
     "قسمان يواجهان الخطر الأساسي نفسه. A يطبّق ضابطين فعّالين وB يطبّق ضابطاً ضعيفاً. ماذا ينتج؟",
     ["Department A has the lower residual risk.",
      "Department B has the lower residual risk.",
      "Both departments have the same residual risk.",
      "Residual risk does not depend on the controls."],
     ["القسم A عنده خطر متبقٍّ أقل من B.",
      "القسم B عنده خطر متبقٍّ أقل من A.",
      "القسمان عندهما الخطر المتبقي نفسه.",
      "الخطر المتبقي لا يعتمد على الضوابط."],
     "Same S, higher M, lower R. A has both more controls and better ones, so its residual risk is the smaller of the two.",
     "نفس S، وM أعلى، إذن R أقل. A عنده ضوابط أكثر وأفضل، فخطره المتبقي أصغر."),
]

KEY = "ABCDACBDABCD"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
