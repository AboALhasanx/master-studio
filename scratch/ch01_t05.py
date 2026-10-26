#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch01 T05 — Risk, vulnerability, exploit, the three models, and P(R>r)."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch01_lib import build

QUIZ = "Quiz_Ch01_T05_Risks_Vulnerabilities_and_Distribution"
TOPIC_EN = "Risks, Vulnerabilities & the Distribution Model"
TOPIC_AR = "المخاطر والثغرات ونموذج التوزيع"

I = [
    # 1 -------------------------------------------------------------------
    ("risk_is_function_of_two", "Remember",
     "How is risk defined?",
     "كيف يُعرَّف الخطر؟",
     ["A function of likelihood and impact.",
      "A function of control cost and time.",
      "A function of user count and devices.",
      "A function of policy strength and audit."],
     ["دالة للاحتمالية وحجم التأثير.",
      "دالة لتكلفة الضابط والوقت.",
      "دالة لعدد المستخدمين والأجهزة.",
      "دالة لقوة السياسة والتدقيق."],
     "Risk is a function of two things only: how likely the event is, and how much damage it would do.",
     "الخطر دالة لشيئين فقط: احتمال وقوع الحدث، ومقدار الضرر الذي يسببه."),

    # 2 -------------------------------------------------------------------
    ("ch01_vulnerability_definition", "Remember",
     "What is a vulnerability?",
     "ما هي الثغرة؟",
     ["A weakness in software, hardware, or people.",
      "A tool used to attack an existing weakness.",
      "The amount of loss an attack would cause.",
      "A control that blocks an attack from landing."],
     ["نقطة ضعف في البرمجيات أو العتاد أو البشر.",
      "أداة تُستخدم لمهاجمة نقطة ضعف قائمة.",
      "مقدار الخسارة التي يسببها الهجوم على النظام.",
      "ضابط أمني يمنع الهجوم من تحقيق هدفه."],
     "A vulnerability is the weakness itself, and it can sit in software, hardware, or the human factor.",
     "الثغرة هي الضعف نفسه، ويمكن أن يكون في البرمجيات أو العتاد أو العامل البشري."),

    # 3 -------------------------------------------------------------------
    ("vulnerability_examples_owasp_cve", "Remember",
     "Which catalogues are the standard references for known vulnerabilities?",
     "أي قائمتين هما المرجع القياسي للثغرات المعروفة؟",
     ["The OWASP Top 10 and the CVE list.",
      "The ISO 27001 and NIST CSF lists.",
      "The GDPR and HIPAA legal frameworks.",
      "The OCTAVE and FAIR assessment models."],
     ["قائمة OWASP Top 10 وقائمة CVE المعتمدة.",
      "قوائم ISO 27001 و NIST CSF المعتمدة.",
      "أطر GDPR و HIPAA القانونية المعتمدة.",
      "نماذج OCTAVE و FAIR المستخدمة للتقييم."],
     "Vulnerabilities are illustrated with the OWASP Top 10 for web applications and CVE for publicly known flaws.",
     "الثغرات تُمثَّل بقائمة OWASP Top 10 لتطبيقات الويب وقاعدة CVE للثغرات المعلنة."),

    # 4 -------------------------------------------------------------------
    ("exploit_definition", "Remember",
     "What is an exploit?",
     "ما هو الاستغلال؟",
     ["A tool or method that takes advantage of a flaw.",
      "A patch released to close a reported flaw.",
      "A policy written to forbid a risky practice.",
      "A backup kept in case the system is ever lost."],
     ["أداة أو طريقة تستغل ثغرة قائمة.",
      "تحديث يُصدر لإغلاق ثغرة معلنة.",
      "سياسة تُكتب لمنع ممارسة خطرة.",
      "نسخة احتياطية تُحفظ لاستعادة النظام."],
     "An exploit is the tool or the method used against a vulnerability. The flaw already exists; the exploit is what uses it.",
     "الاستغلال هو الأداة أو الطريقة المستخدمة ضد ثغرة. الضعف موجود أصلاً، والاستغلال هو ما يستخدمه."),

    # 5 -------------------------------------------------------------------
    ("risk_vuln_exploit_relation", "Understand",
     "How do vulnerability, exploit, and risk relate?",
     "كيف ترتبط الثغرة والاستغلال والخطر؟",
     ["The flaw is the weakness, the exploit uses it, the risk is the loss.",
      "The flaw is the loss, the exploit is the weakness, the risk is the tool.",
      "The exploit is the weakness, the risk is the tool, the flaw is the loss.",
      "The risk is the weakness, the flaw is the tool, the exploit is the loss."],
     ["الثغرة هي الضعف، والاستغلال يستخدمها، والخطر هو الخسارة.",
      "الثغرة هي الخسارة، والاستغلال هو الضعف، والخطر هو الأداة.",
      "الاستغلال هو الضعف، والخطر هو الأداة، والثغرة هي الخسارة.",
      "الخطر هو الضعف، والثغرة هي الأداة، والاستغلال هو الخسارة."],
     "The chain runs weakness, then tool, then loss: the flaw is the weakness, the exploit is the tool used on it, and the risk is the loss that follows.",
     "السلسلة هي: ضعف ثم أداة ثم خسارة. الثغرة هي الضعف، والاستغلال هو الأداة المستخدمة ضدها، والخطر هو الخسارة الناتجة."),

    # 6 -------------------------------------------------------------------
    ("risk_assessment_models", "Remember",
     "Which three models are used for risk assessment?",
     "أي ثلاثة نماذج تُستخدم لتقييم المخاطر؟",
     ["OCTAVE, FAIR, and NIST RMF.", "GDPR, HIPAA, and ISO 27001.",
      "OWASP, CVE, and CVSS scores.", "NIST CSF, ENISA, and COBIT."],
     ["OCTAVE و FAIR و NIST RMF.", "GDPR و HIPAA و ISO 27001.",
      "OWASP و CVE و CVSS.", "NIST CSF و ENISA و COBIT."],
     "The three are OCTAVE, FAIR and the NIST Risk Management Framework. The others are laws, catalogues or agencies.",
     "الثلاثة هي OCTAVE و FAIR وإطار إدارة المخاطر NIST. أما البقية فقوانين أو قواعد بيانات أو هيئات."),

    # 7 -------------------------------------------------------------------
    ("vulnerability_scenario_human", "Apply",
     "A password is written on a note stuck to the monitor. What kind of weakness is this?",
     "كلمة مرور مكتوبة على ورقة ملصقة على الشاشة. أي نوع من الضعف هذا؟",
     ["A human-factor weakness.", "A software design flaw.",
      "A hardware defect in it.", "An exploit tool for it."],
     ["ضعف في العامل البشري.", "خلل في تصميم البرمجية.",
      "عيب في العتاد نفسه.", "أداة استغلال جاهزة."],
     "A weakness can sit in software, hardware, or the human factor. A note on a monitor is neither code nor metal, so it is the human factor.",
     "الضعف يكون في البرمجيات أو العتاد أو العامل البشري. ورقة على الشاشة ليست كوداً ولا معدناً، فهي العامل البشري."),

    # 8 -------------------------------------------------------------------
    ("risk_compare_compute", "Apply",
     "Threat 1: likelihood 0.2, impact 500,000. Threat 2: likelihood 0.4, impact 100,000. Which carries more risk?",
     "التهديد 1: احتمال 0.2 وتأثير 500,000. والتهديد 2: احتمال 0.4 وتأثير 100,000. أيهما أخطر؟",
     ["Threat 1, because its expected loss is larger.",
      "Threat 2, because its likelihood is larger.",
      "Threat 1, because its impact is larger.",
      "Neither, because the two cannot be compared."],
     ["التهديد 1 لأن خسارته المتوقعة أكبر.",
      "التهديد 2 لأن احتماليته أكبر بكثير.",
      "التهديد 1 لأن حجم تأثيره أكبر بكثير.",
      "لا هذا ولا ذاك لأنهما غير قابلين للمقارنة."],
     "Expected loss is 0.2 x 500,000 = 100,000 against 0.4 x 100,000 = 40,000. Threat 1 is higher, and the reason is the expected value, not the raw impact.",
     "الخسارة المتوقعة 0.2 × 500,000 = 100,000 مقابل 0.4 × 100,000 = 40,000. التهديد 1 أعلى، والسبب هو القيمة المتوقعة لا التأثير الخام."),

    # 9 -------------------------------------------------------------------
    ("distribution_f_r_definition", "Remember",
     "In the distribution model, what is F(r)?",
     "في نموذج التوزيع، ما هو F(r)؟",
     ["The cumulative distribution of loss, 0 to 1.",
      "The probability density of loss, 0 upward.",
      "The average loss expected over one year.",
      "The maximum loss the system could suffer."],
     ["التوزيع التراكمي للخسارة بين 0 و1.",
      "كثافة احتمالية الخسارة من الصفر صعوداً.",
      "متوسط الخسارة المتوقعة خلال سنة.",
      "أقصى خسارة يمكن أن يتعرض لها النظام."],
     "F is the cumulative distribution function, and by definition it is bounded between 0 and 1.",
     "F هي دالة التوزيع التراكمي، وهي بحكم تعريفها محصورة بين 0 و1."),

    # 10 ------------------------------------------------------------------
    ("distribution_tail_meaning", "Understand",
     "What does the distribution model actually tell a risk manager?",
     "ماذا يقول نموذج التوزيع لمدير المخاطر فعلياً؟",
     ["The chance that loss will exceed a set threshold.",
      "The chance that loss will stay under a threshold.",
      "The chance that no incident will occur at all.",
      "The chance that a control will fail this year."],
     ["احتمال أن تتجاوز الخسارة حداً معيّناً.",
      "احتمال أن تبقى الخسارة تحت حدّ معيّن.",
      "احتمال ألا يقع أي حادث إطلاقاً.",
      "احتمال أن يفشل ضابط أمني هذا العام."],
     "The model gives the probability of exceeding a chosen threshold, which is how a manager asks whether the loss could pass what the organisation can absorb.",
     "النموذج يعطي احتمال تجاوز حدّ مختار، وبه يسأل المدير إن كانت الخسارة قد تتجاوز ما تستطيع المؤسسة تحمّله."),

    # 11 ------------------------------------------------------------------
    ("distribution_compute", "Apply",
     "If F(50) equals 0.85, what is the probability that loss exceeds 50?",
     "إذا كانت F(50) تساوي 0.85، فما احتمال أن تتجاوز الخسارة 50؟",
     ["0.15", "0.85", "0.35", "1.85"],
     ["0.15", "0.85", "0.35", "1.85"],
     "The two parts sum to one, so the answer is 1 minus 0.85, which is 0.15.",
     "الجزءان مجموعهما واحد، فالجواب 1 ناقص 0.85 ويساوي 0.15."),

    # 12 ------------------------------------------------------------------
    ("distribution_boundary_case", "Analyze",
     "If F(r) reaches 1 at some threshold, what follows?",
     "إذا وصلت F(r) إلى 1 عند حدّ ما، فماذا ينتج؟",
     ["The probability of exceeding the threshold is zero.",
      "The probability of exceeding the threshold is one.",
      "The probability of exceeding it cannot be computed.",
      "The probability of exceeding it equals the threshold."],
     ["احتمال تجاوز الحد يساوي صفراً.",
      "احتمال تجاوز الحد يساوي واحداً.",
      "احتمال التجاوز لا يمكن حسابه هنا.",
      "احتمال التجاوز يساوي قيمة الحد نفسه."],
     "One minus one is zero, so no loss is left above the threshold. That is what the upper bound of F means in practice.",
     "واحد ناقص واحد يساوي صفراً، فلا تبقى خسارة فوق الحد. وهذا معنى الحد الأعلى لـ F عملياً."),
]

KEY = "ACBDABDCABCD"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
