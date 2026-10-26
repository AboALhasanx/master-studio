#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch02 T05 — The five systematic security-analysis frameworks."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch02_lib import build

QUIZ = "Quiz_Ch02_T05_Analysis_Frameworks"
TOPIC_EN = "The Five Analysis Frameworks"
TOPIC_AR = "أطر التحليل الخمسة"

I = [
    # 1 -------------------------------------------------------------------
    ("framework_count", "Remember",
     "Which five frameworks are used for systematic security analysis?",
     "أي خمسة أطر تُستخدم للتحليل الأمني المنهجي؟",
     ["COBIT, COSO, FAIR, ISO/IEC 27002, and OCTAVE.",
      "COBIT, COSO, FAIR, ISO 9001, and OCTAVE too.",
      "COBIT, COSO, FAIR, NIST CSF, and OCTAVE.",
      "COBIT, COSO, FAIR, GDPR, and OCTAVE here only."],
     ["COBIT و COSO و FAIR و ISO/IEC 27002 و OCTAVE.",
      "COBIT و COSO و FAIR و ISO 9001 و OCTAVE أيضاً.",
      "COBIT و COSO و FAIR و NIST CSF و OCTAVE.",
      "COBIT و COSO و FAIR و GDPR و OCTAVE هنا."],
     "The five are COBIT, COSO, FAIR, ISO/IEC 27002, and OCTAVE. Only the middle one differs from ISO 9001 or NIST CSF.",
     "الخمسة هي: COBIT و COSO و FAIR و ISO/IEC 27002 و OCTAVE. والفرق الوحيد هو الثالث من حيث الترتيب."),

    # 2 -------------------------------------------------------------------
    ("cobit_offer", "Remember",
     "What does COBIT offer?",
     "ماذا يقدم COBIT؟",
     ["Objectives for measures that can manage risk.",
      "A taxonomy of the factors behind risk.",
      "A process for analysing threats and risks.",
      "A list of internal processes to reach low risk."],
     ["أهداف لتدابير يمكن استخدامها لإدارة الخطر.",
      "تصنيف للعوامل التي تكوّن الخطر نفسه هنا.",
      "عملية لتحليل التهديدات والمخاطر معاً دائماً.",
      "قائمة عمليات داخلية لبلوغ خطر منخفض جداً."],
     "COBIT stands for Control Objectives for Information and Related Technology, and what it offers is objectives for measures that manage risk.",
     "COBIT اختصار Control Objectives for Information and Related Technology، وما يقدمه هو أهداف لتدابير تدير الخطر."),

    # 3 -------------------------------------------------------------------
    ("coso_offer", "Remember",
     "What does COSO provide?",
     "ماذا يوفر COSO؟",
     ["A description of internal processes for low risk.",
      "Objectives for measures that can manage risk.",
      "A taxonomy of the factors that form risk.",
      "A process for analysing threats and all their risks."],
     ["وصف للعمليات الداخلية لبلوغ خطر منخفض.",
      "أهداف لتدابير يمكن استخدامها لإدارة الخطر.",
      "تصنيف للعوامل التي تكوّن الخطر نفسه هنا.",
      "عملية لتحليل التهديدات والمخاطر معاً دائماً."],
     "COSO describes the internal processes a company must follow to reach a suitably low level of risk.",
     "COSO يصف العمليات الداخلية التي يجب أن تتبعها الشركة لبلوغ مستوى خطر منخفض ومناسب."),

    # 4 -------------------------------------------------------------------
    ("fair_offer", "Remember",
     "What three things does FAIR present?",
     "أي ثلاثة أشياء يقدمها FAIR؟",
     ["A taxonomy, a naming standard, and a model.",
      "Objectives, internal processes, and controls.",
      "Three phases that end in a security plan.",
      "Fourteen categories of security controls."],
     ["تصنيف ومعيار تسمية ونموذج حساب.",
      "أهداف وعمليات داخلية وضوابط أمنية.",
      "ثلاث مراحل تنتهي بخطة أمنية كاملة.",
      "أربعة عشر قسماً من الضوابط الأمنية."],
     "FAIR gives a taxonomy of the factors that form risk, a standard for naming risk quantities, and a model for calculating risk.",
     "FAIR يقدم تصنيفاً للعوامل التي تكوّن الخطر، ومعياراً لتسمية كميات الخطر، ونموذجاً لحساب الخطر."),

    # 5 -------------------------------------------------------------------
    ("iso_offer", "Remember",
     "What does ISO/IEC 27002 give?",
     "ماذا يعطي ISO/IEC 27002؟",
     ["Guidance and controls for information security.",
      "Objectives for measures that can manage risk.",
      "A taxonomy of the factors that form risk.",
      "A process for analysing threats and all their risks."],
     ["إرشادات وضوابط أمنية لأمن المعلومات هنا.",
      "أهداف لتدابير يمكن استخدامها لإدارة الخطر.",
      "تصنيف للعوامل التي تكوّن الخطر نفسه هنا.",
      "عملية لتحليل التهديدات والمخاطر معاً دائماً."],
     "ISO/IEC 27002 is an international standard giving security guidance and controls for information security.",
     "ISO/IEC 27002 معيار دولي يعطي إرشادات وضوابط أمنية لأمن المعلومات."),

    # 6 -------------------------------------------------------------------
    ("octave_offer", "Remember",
     "What does OCTAVE describe?",
     "ماذا يصف OCTAVE؟",
     ["A process for analysing threats and risks.",
      "Guidance and controls for information security work.",
      "A taxonomy of the factors that form risk.",
      "Objectives for measures that can manage risk."],
     ["عملية لتحليل التهديدات والمخاطر معاً.",
      "إرشادات وضوابط أمنية لأمن المعلومات هنا.",
      "تصنيف للعوامل التي تكوّن الخطر نفسه هنا.",
      "أهداف لتدابير يمكن استخدامها لإدارة الخطر."],
     "OCTAVE describes a process: analyse the threats and their risks, then find suitable countermeasures.",
     "OCTAVE يصف عملية: تحليل التهديدات ومخاطرها، ثم إيجاد التدابير المضادة المناسبة."),

    # 7 -------------------------------------------------------------------
    ("fair_only_with_model", "Understand",
     "Which framework is the only one credited with a model for calculating risk?",
     "أي إطار هو الوحيد الموصوف بنموذج لحساب الخطر؟",
     ["FAIR, because it includes a calculation model.",
      "COSO, because it describes internal processes.",
      "OCTAVE, because it runs in three phases.",
      "COBIT, because it sets objectives for measures."],
     ["FAIR، لأنه يتضمن نموذجاً لحساب الخطر.",
      "COSO، لأنه يصف العمليات الداخلية للمؤسسة.",
      "OCTAVE، لأنه يعمل بثلاث مراحل واضحة.",
      "COBIT، لأنه يضع أهدافاً للتدابير الأمنية."],
     "FAIR is the only one of the five with a calculation model, which is why it is the strongest for quantitative work.",
     "FAIR هو الوحيد من الخمسة الذي يملك نموذج حساب، ولهذا هو الأقوى في العمل الكمي."),

    # 8 -------------------------------------------------------------------
    ("match_coso_scenario", "Apply",
     "A company wants a documented description of the internal processes it must follow to reach low risk. Which framework matches?",
     "شركة تريد وصفاً موثقاً للعمليات الداخلية التي يجب أن تتبعها لبلوغ خطر منخفض. أي إطار يناسب؟",
     ["COSO, which describes the internal processes.",
      "FAIR, which names the risk quantities for you.",
      "OCTAVE, which builds threat profiles.",
      "COBIT, which sets objectives for measures."],
     ["COSO، لأنه يصف العمليات الداخلية.",
      "FAIR، لأنه يسمّي كميات الخطر.",
      "OCTAVE، لأنه يبني ملفات التهديد.",
      "COBIT، لأنه يضع أهدافاً للتدابير."],
     "The request is for internal processes, and that is exactly COSO's contribution. COBIT offers objectives, FAIR a calculation model, OCTAVE a process.",
     "الطلب هو عمليات داخلية، وهذا بالضبط ما يقدمه COSO. أما COBIT فيعطي أهدافاً، وFAIR نموذج حساب، وOCTAVE عملية."),

    # 9 -------------------------------------------------------------------
    ("match_octave_scenario", "Apply",
     "A team must analyse the threats against its assets and then find suitable countermeasures. Which framework matches?",
     "فريق يجب أن يحلّل التهديدات ضد أصوله ثم يجد تدابير مضادة مناسبة. أي إطار يناسب؟",
     ["OCTAVE, which analyses threats for controls.",
      "COSO, which describes the internal processes.",
      "FAIR, which names the risk quantities for you.",
      "COBIT, which sets objectives for measures."],
     ["OCTAVE، لأنه يحلّل التهديدات ويجد الضوابط.",
      "COSO، لأنه يصف العمليات الداخلية للمؤسسة.",
      "FAIR، لأنه يسمّي كميات الخطر ويصنّفها كلها.",
      "COBIT، لأنه يضع أهدافاً للتدابير الأمنية."],
     "Analysing threats and arriving at countermeasures is the process OCTAVE describes.",
     "تحليل التهديدات والوصول إلى تدابير مضادة هو العملية التي يصفها OCTAVE."),

    # 10 ------------------------------------------------------------------
    ("why_systematic", "Understand",
     "Why is a systematic method needed at all?",
     "لماذا نحتاج منهجاً منهجياً أصلاً؟",
     ["Because ad hoc effort leaves gaps in coverage.",
      "Because frameworks are required by the law today.",
      "Because one framework replaces all controls.",
      "Because auditors demand a printed document."],
     ["لأن العمل العشوائي يترك ثغرات في التغطية.",
      "لأن القانون يفرض استخدام أطر جاهزة دائماً.",
      "لأن إطاراً واحداً يغني عن كل الضوابط.",
      "لأن المدققين يطلبون مستنداً مطبوعاً."],
     "A systematic method covers the ground in a fixed order, so nothing is skipped. The five are well-known examples of such methods.",
     "المنهج المنهجي يغطي الموضوع بترتيب ثابت فلا يُنسى شيء. والخمسة أمثلة معروفة على هذه المناهج."),
]

KEY = "ABCDABCDAB"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
