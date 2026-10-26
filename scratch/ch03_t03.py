#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch03 T03 — The risk equation and its aggregate form."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch03_lib import build

QUIZ = "Quiz_Ch03_T03_Risk_Equation"
TOPIC_EN = "The Risk Equation and Its Aggregate Form"
TOPIC_AR = "معادلة الخطر وصيغتها المجمّعة"

I = [
    # 1 -------------------------------------------------------------------
    ("risk_definition", "Remember",
     "What is risk in the cybersecurity context?",
     "ما هو الخطر في سياق الأمن السيبراني؟",
     ["The quantifiable chance a threat exploits a weakness.",
      "The damage that has already been recorded and paid.",
      "The number of vulnerabilities found in a single year.",
      "The budget assigned to security controls each year."],
     ["الاحتمال القابل للقياس أن يستغل تهديد ثغرة.",
      "الضرر الذي سُجّل فعلاً وتم دفعه للغير هنا.",
      "عدد الثغرات المكتشفة في سنة واحدة كاملة.",
      "الميزانية المخصصة لضوابط الأمن سنوياً هنا."],
     "Risk is the quantifiable possibility that a threat actor exploits a vulnerability and damages organizational assets. It is a measurable quantity, not a mood.",
     "الخطر هو الاحتمال القابل للقياس أن يستغل جهة تهديد ثغرةً ويلحق ضرراً بأصول المؤسسة. وهو مقدار قابل للقياس لا إحساس."),

    # 2 -------------------------------------------------------------------
    ("risk_outcomes", "Remember",
     "Which four outcomes can that risk produce?",
     "أي أربع نتائج يمكن أن ينتجها ذلك الخطر؟",
     ["Financial loss, disruption, reputation, liability.",
      "Slower patching and much larger backup windows.",
      "Higher staff turnover and much lower morale.",
      "Bigger budgets and many more security staff on site."],
     ["خسارة مالية وتعطّل وضرر سمعة ومسؤولية قانونية.",
      "تحديث أبطأ بكثير ونوافذ نسخ احتياطي أطول.",
      "دوران موظفين أعلى بكثير ومعنويات أدنى هنا.",
      "ميزانيات أكبر بكثير وعدد موظفي أمن أكبر."],
     "Four outcomes: financial loss, operational disruption, reputational damage, and legal liability.",
     "أربع نتائج: خسارة مالية، وتعطّل تشغيلي، وضرر بالسمعة، ومسؤولية قانونية."),

    # 3 -------------------------------------------------------------------
    ("simple_equation_factors", "Remember",
     "Which two quantities does the basic risk equation combine?",
     "أي كميتين تجمعهما معادلة الخطر الأساسية؟",
     ["Likelihood multiplied by impact alone.",
      "Threat multiplied by vulnerability.",
      "Cost multiplied by benefit of controls.",
      "Frequency multiplied by attack duration."],
     ["الاحتمال مضروباً بالتأثير.",
      "التهديد مضروباً بالثغرة.",
      "الكلفة مضروبة بفائدة الضوابط.",
      "التكرار مضروباً بمدة الهجوم."],
     "The basic equation multiplies likelihood by impact. Threat and vulnerability are the ingredients behind likelihood, not the two terms of the equation.",
     "المعادلة الأساسية تضرب الاحتمال بالتأثير. أما التهديد والثغرة فهما مكوّنان داخل الاحتمال لا حدّان في المعادلة."),

    # 4 -------------------------------------------------------------------
    ("likelihood_meaning", "Remember",
     "What does likelihood mean here?",
     "ماذا يعني الاحتمال هنا؟",
     ["The chance a threat exploits a vulnerability.",
      "The size of the loss if the attempt succeeds.",
      "The number of vulnerabilities present in total.",
      "The time remaining until the next incident."],
     ["احتمال أن يستغل تهديد ثغرة.",
      "حجم الخسارة إذا نجحت المحاولة.",
      "عدد الثغرات الموجودة إجمالاً.",
      "الوقت المتبقي حتى الحادث القادم."],
     "Likelihood is the probability that a threat will actually exploit a vulnerability.",
     "الاحتمال هو فرصة أن يستغل التهديد الثغرة فعلاً."),

    # 5 -------------------------------------------------------------------
    ("impact_meaning", "Remember",
     "What does impact mean here?",
     "ماذا يعني التأثير هنا؟",
     ["The potential damage if the threat succeeds.",
      "The probability that a threat appears at all.",
      "The count of vulnerabilities actually exploited.",
      "The cost of the controls deployed so far."],
     ["الضرر المحتمل إذا نجح التهديد.",
      "احتمال ظهور التهديد أصلاً.",
      "عدد الثغرات المستغلة فعلياً.",
      "كلفة الضوابط المنشورة حتى الآن."],
     "Impact is the potential damage, and it is read on three scales: financial, reputational, and operational.",
     "التأثير هو الضرر المحتمل، ويُقاس على ثلاثة مقاييس: المالي والسمعوي والتشغيلي."),

    # 6 -------------------------------------------------------------------
    ("aggregate_form", "Understand",
     "What does the aggregate form do with the simple equation?",
     "ماذا تفعل الصيغة المجمّعة بالمعادلة البسيطة؟",
     ["It sums probability times impact over all threats.",
      "It takes the largest single probability found.",
      "It takes the average of the impacts across threats.",
      "It multiplies every impact by the same factor."],
     ["يجمع الاحتمال مضروباً بالتأثير هنا.",
      "يأخذ أكبر احتمال منفرد موجود بينها.",
      "يأخذ متوسط التأثيرات على كل التهديدات.",
      "يضرب كل تأثير في العامل نفسه دائماً."],
     "The aggregate form repeats the simple equation once per threat and adds the results, so the whole register produces one number.",
     "الصيغة المجمّعة تكرّر المعادلة البسيطة مرة لكل تهديد وتجمع النواتج، فينتج عن السجل كله رقم واحد."),

    # 7 -------------------------------------------------------------------
    ("phishing_vs_zero_day", "Understand",
     "How do a phishing campaign and a zero-day exploit differ?",
     "كيف يختلف حملة تصيّد عن ثغرة يوم الصفر؟",
     ["High likelihood and low impact versus the reverse.",
      "Two threats with the same likelihood and impact.",
      "A threat that has no measurable impact at all here.",
      "A threat that cannot be quantified by any model."],
     ["احتمال عالٍ وتأثير منخفض مقابل العكس.",
      "تهديدان لهما الاحتمال والتأثير نفسه تماماً.",
      "تهديد بلا تأثير قابل للقياس إطلاقاً.",
      "تهديد لا يمكن قياسه بأي نموذج معروف."],
     "Phishing is likely but usually small per event; a zero-day is unlikely but catastrophic. Risk management has to weigh both, which is why one number is not enough.",
     "التصيّد محتمل لكنه صغير عادةً لكل حادثة، وثغرة يوم الصفر غير محتملة لكنها كارثية. وإدارة المخاطر توازن بينهما، ولهذا لا يكفي رقم واحد."),

    # 8 -------------------------------------------------------------------
    ("why_quantify", "Understand",
     "What does the quantitative framing give an organization?",
     "ماذا يمنح التصوير الكمي للمؤسسة؟",
     ["A rational basis for allocating resources.",
      "A replacement for the security policy.",
      "A way to avoid measuring anything at all.",
      "A guarantee that no incident will ever occur."],
     ["أساس عقلاني لتوزيع الموارد.",
      "بديل عن سياسة الأمن كلها.",
      "طريقة لتجنّب قياس أي شيء.",
      "ضمان أن لا يقع أي حادث إطلاقاً."],
     "It gives a rational basis for decision-making on resource allocation and security investment, instead of spending by instinct.",
     "يمنح أساساً عقلانياً للقرار في توزيع الموارد والاستثمار الأمني، بدل الإنفاق بالحدس."),

    # 9 -------------------------------------------------------------------
    ("simple_compute", "Apply",
     "A threat has likelihood 0.4 and impact 25. What is its risk?",
     "تهديد احتماله 0.4 وتأثيره 25. ما خطره؟",
     ["10", "25", "40", "15"],
     ["10", "25", "40", "15"],
     "Risk is likelihood times impact: 0.4 x 25 = 10.",
     "الخطر هو الاحتمال ضرب التأثير: 0.4 × 25 = 10."),

    # 10 ------------------------------------------------------------------
    ("aggregate_compute", "Apply",
     "Two threats: 0.5 chance of a 20 loss, and 0.25 chance of a 40 loss. What is the aggregate risk?",
     "تهديدان: احتمال 0.5 لخسارة 20، واحتمال 0.25 لخسارة 40. ما الخطر المجمّع؟",
     ["20", "60", "30", "10"],
     ["20", "60", "30", "10"],
     "Each threat contributes probability times impact: 0.5 x 20 = 10 and 0.25 x 40 = 10. The aggregate is 20.",
     "كل تهديد يسهم بالاحتمال ضرب التأثير: 0.5 × 20 = 10، و0.25 × 40 = 10. والمجموع 20."),

    # 11 ------------------------------------------------------------------
    ("risk_is_quantifiable", "Understand",
     "Why is risk called quantifiable rather than abstract?",
     "لماذا يُسمّى الخطر قابلاً للقياس لا مجرّداً؟",
     ["It can be expressed as a number, not a feeling.",
      "It is only a theoretical construct for teaching.",
      "It depends entirely on the auditor's personal view.",
      "It applies only after an incident has happened."],
     ["يمكن التعبير عنه برقم لا بإحساس.",
      "مفهوم نظري للتدريس فقط هنا تماماً.",
      "يعتمد كلياً على رأي المدقق الشخصي.",
      "لا يُطبَّق إلا بعد وقوع الحادث فعلاً."],
     "It can be expressed as a number, which is what makes comparison between threats and between investments possible at all.",
     "يمكن التعبير عنه برقم، وهذا ما يجعل المقارنة بين التهديدات وبين الاستثمارات ممكنة أصلاً."),
]

KEY = "ABCDABCDABC"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
