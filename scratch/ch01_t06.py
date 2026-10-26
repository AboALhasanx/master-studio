#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch01 T06 — Policies, global perspectives, PCI, and the optimisation model."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch01_lib import build

QUIZ = "Quiz_Ch01_T06_Policies_Compliance_and_Optimization"
TOPIC_EN = "Policies, Compliance Index PCI & the Optimisation Model"
TOPIC_AR = "السياسات ومؤشر الامتثال ونموذج التحسين"

I = [
    # 1 -------------------------------------------------------------------
    ("policy_gdpr_scope", "Remember",
     "What does the GDPR regulate?",
     "ماذا تنظّم لائحة GDPR؟",
     ["Data protection and personal privacy.",
      "Healthcare records and patient safety.",
      "Payment cards and transaction security.",
      "Network routing and traffic control."],
     ["حماية البيانات والخصوصية الشخصية.",
      "سجلات الرعاية الصحية وسلامة المرضى.",
      "بطاقات الدفع وأمن المعاملات المالية.",
      "توجيه الشبكات وضبط حركة المرور."],
     "GDPR is the European Union regulation for data protection and privacy.",
     "GDPR هي لائحة الاتحاد الأوروبي لحماية البيانات والخصوصية."),

    # 2 -------------------------------------------------------------------
    ("policy_hipaa_scope", "Remember",
     "Which framework protects healthcare information in the United States?",
     "أي إطار يحمي معلومات الرعاية الصحية في الولايات المتحدة؟",
     ["The HIPAA framework.", "The GDPR framework.",
      "The ISO 27001 standard.", "The NIST CSF framework."],
     ["إطار HIPAA الأمريكي.", "إطار GDPR الأوروبي.",
      "معيار ISO 27001 الدولي.", "إطار NIST CSF المعتمد."],
     "HIPAA is the American law for healthcare information. GDPR is European and covers data protection generally.",
     "HIPAA هو القانون الأمريكي لمعلومات الرعاية الصحية. أما GDPR فأوروبي ويغطي حماية البيانات عموماً."),

    # 3 -------------------------------------------------------------------
    ("policy_international_standards", "Remember",
     "Which set covers international information security standards?",
     "أي مجموعة تغطي معايير أمن المعلومات الدولية؟",
     ["The NIST and ISO 27001 standards.",
      "The GDPR and HIPAA regulations.",
      "The OWASP and CVE catalogues.",
      "The OCTAVE and FAIR assessment models."],
     ["معايير NIST و ISO 27001 المعتمدة.",
      "لوائح GDPR و HIPAA الأوروبية المعتمدة.",
      "قواعد OWASP و CVE المعتمدة للثغرات.",
      "نماذج OCTAVE و FAIR لتقييم المخاطر."],
     "The international standards are NIST and ISO 27001. The others are laws, vulnerability catalogues, or risk models.",
     "المعايير الدولية هي NIST و ISO 27001. أما البقية فقوانين أو قواعد ثغرات أو نماذج مخاطر."),

    # 4 -------------------------------------------------------------------
    ("perspective_us", "Remember",
     "Which frameworks mark the United States perspective?",
     "أي أطر تُمثّل منظور الولايات المتحدة؟",
     ["The NIST CSF and the federal strategy.",
      "The GDPR and the ENISA agency role.",
      "The national cybersecurity councils.",
      "The ISO 27001 and HIPAA rule set here."],
     ["إطار NIST CSF والاستراتيجية الوطنية.",
      "لائحة GDPR ووكالة ENISA الأوروبية.",
      "مجالس الأمن السيبراني الوطنية.",
      "قواعد ISO 27001 و HIPAA المعتمدة."],
     "The United States works through the NIST Cybersecurity Framework and the Federal Cybersecurity Strategy.",
     "الولايات المتحدة تعمل بإطار NIST للأمن السيبراني والاستراتيجية الفدرالية."),

    # 5 -------------------------------------------------------------------
    ("perspective_eu", "Remember",
     "Which frameworks mark the European Union perspective?",
     "أي أطر تُمثّل منظور الاتحاد الأوروبي؟",
     ["The GDPR with the ENISA agency role.",
      "The NIST CSF and federal strategy.",
      "The national cybersecurity councils.",
      "The ISO 27001 and HIPAA rule set here."],
     ["لائحة GDPR مع وكالة ENISA الأوروبية.",
      "إطار NIST CSF والاستراتيجية الوطنية.",
      "مجالس الأمن السيبراني الوطنية.",
      "قواعد ISO 27001 و HIPAA المعتمدة."],
     "Europe is represented by GDPR together with ENISA, the agency that coordinates cyber policy across the Union.",
     "أوروبا تُمثَّل بـ GDPR مع ENISA، وهي الوكالة التي تنسّق سياسة الأمن السيبراني في الاتحاد."),

    # 6 -------------------------------------------------------------------
    ("perspective_middle_east", "Remember",
     "How is cyber governance organised in the Middle East?",
     "كيف تُنظَّم الحوكمة السيبرانية في الشرق الأوسط؟",
     ["National cybersecurity councils.",
      "A single regional data protection law.",
      "Outsourced foreign cloud firms.",
      "Paper-based sovereign records."],
     ["مجالس الأمن السيبراني الوطنية.",
      "قانون بيانات إقليمي واحد فقط.",
      "شركات سحابة خارجية متعاقدة.",
      "سجلات سيادية ورقية محفوظة."],
     "The Middle East is described through National Cybersecurity Councils that oversee strategic cyber governance.",
     "الشرق الأوسط يوصف عبر مجالس الأمن السيبراني الوطنية التي تشرف على الحوكمة السيبرانية الاستراتيجية."),

    # 7 -------------------------------------------------------------------
    ("pci_what_it_measures", "Understand",
     "What does the policy compliance index measure?",
     "ماذا يقيس مؤشر الامتثال للسياسات؟",
     ["How well the organisation meets its controls.",
      "How much the organisation spends on its controls.",
      "How many controls the organisation has written.",
      "How often the organisation audits its controls."],
     ["مدى التزام المؤسسة بالضوابط المطلوبة منها.",
      "مقدار ما تنفقه المؤسسة على ضوابطها.",
      "عدد الضوابط المكتوبة التي تملكها المؤسسة.",
      "عدد مرات تدقيق المؤسسة على ضوابطها."],
     "It is a weighted average of how far each requirement is met, so it measures compliance rather than spending or counting.",
     "هو متوسط مرجّح لمدى تحقّق كل متطلب، فهو يقيس الالتزام لا الإنفاق ولا العدد."),

    # 8 -------------------------------------------------------------------
    ("pci_weight_meaning", "Understand",
     "In the compliance index, what does the weight of a requirement represent?",
     "في مؤشر الامتثال، ماذا يمثّل وزن المتطلب؟",
     ["How important that requirement is to the index.",
      "How compliant the organisation is with that requirement.",
      "How much it costs the organisation to meet.",
      "How often the requirement is reviewed again."],
     ["مقدار أهمية ذلك المتطلب في المؤشر.",
      "مقدار التزام المؤسسة بذلك المتطلب.",
      "تكلفة الوفاء بذلك المتطلب سنوياً.",
      "عدد مرات مراجعة ذلك المتطلب."],
     "The weight says how much a requirement counts. The compliance score is the other term, and it says how well you meet it.",
     "الوزن يقول كم يهمّ المتطلب. أما درجة الالتزام فهي الحد الآخر، وهي تقول كم تلتزم به."),

    # 9 -------------------------------------------------------------------
    ("pci_compute", "Apply",
     "Two requirements: weights 3 and 1, scores 1.0 and 0.6. What is the compliance index?",
     "متطلبان: وزناهما 3 و1، ودرجتاهما 1.0 و0.6. ما مؤشر الامتثال؟",
     ["0.90", "0.80", "0.60", "0.75"],
     ["0.90", "0.80", "0.60", "0.75"],
     "Multiply each score by its weight and divide by the sum of weights: (3 x 1.0 + 1 x 0.6) divided by 4 gives 0.90.",
     "اضرب كل درجة بوزنها واقسم على مجموع الأوزان: (3 × 1.0 + 1 × 0.6) ÷ 4 = 0.90."),

    # 10 ------------------------------------------------------------------
    ("optimisation_model_meaning", "Understand",
     "What does the optimisation model subtract from the expected risk?",
     "ماذا يطرح نموذج التحسين من الخطر المتوقع؟",
     ["Risk minus the investment made in controls.",
      "Risk plus the whole investment made in controls.",
      "Risk divided by the number of controls.",
      "Risk multiplied by the cost of controls."],
     ["الخطر ناقص الاستثمار في الضوابط.",
      "الخطر زائد الاستثمار في الضوابط.",
      "الخطر مقسوماً على عدد الضوابط.",
      "الخطر مضروباً بتكلفة الضوابط."],
     "The model takes the sum of probability times impact and subtracts the investment in controls, so it balances risk against spending.",
     "النموذج يأخذ مجموع الاحتمال × التأثير ويطرح منه الاستثمار في الضوابط، فيوازن بين الخطر والإنفاق."),

    # 11 ------------------------------------------------------------------
    ("optimisation_threshold_rule", "Remember",
     "In the optimisation model, what does a result above 100 indicate?",
     "في نموذج التحسين، ماذا تعني نتيجة فوق 100؟",
     ["A result above 100 means there is investment.",
      "A result above 100 means there is no investment.",
      "A result above 100 means risk cannot be reduced.",
      "A result above 100 means the model is invalid."],
     ["نتيجة فوق 100 تعني وجود استثمار.",
      "نتيجة فوق 100 تعني غياب الاستثمار.",
      "نتيجة فوق 100 تعني أن الخطر لا يُخفَّض.",
      "نتيجة فوق 100 تعني أن النموذج غير صالح."],
     "The rule: above 100 means there is investment, below 100 means there is none.",
     "القاعدة: فوق 100 يعني هناك استثمار، وتحت 100 يعني لا يوجد."),
]

KEY = "ACBDABDCABC"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
