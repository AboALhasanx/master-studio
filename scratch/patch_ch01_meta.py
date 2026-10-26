#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Strip every reference to the handout from the Chapter 1 builders.

A stem like "Which techniques does the lecture list under confidentiality?"
tests whether you read the notes. "Which techniques enforce confidentiality?"
tests whether you know the subject. Same answer, better question.
"""
import glob

PAIRS = [
    # ---- stems -----------------------------------------------------------
    ("The lecture says the list of domains is not fixed. What follows from that?",
     "Why are the six security domains best read as examples?"),
    ("المحاضرة تقول إن قائمة المجالات ليست ثابتة. ماذا ينتج عن ذلك؟",
     "لماذا تُقرأ المجالات الستة كأمثلة لا كقائمة مغلقة؟"),
    ("Which construct does the lecture call the backbone of cybersecurity?",
     "Which model is the backbone of cybersecurity?"),
    ("أي بناء تسمّيه المحاضرة العمود الفقري للأمن السيبراني؟",
     "أي نموذج هو العمود الفقري للأمن السيبراني؟"),
    ("Which techniques does the lecture list under confidentiality?",
     "Which techniques enforce confidentiality?"),
    ("أي تقنيات تسردها المحاضرة تحت السرية؟", "أي تقنيات تحقق السرية؟"),
    ("Which techniques does the lecture list under integrity?",
     "Which techniques enforce integrity?"),
    ("أي تقنيات تسردها المحاضرة تحت السلامة؟", "أي تقنيات تحقق السلامة؟"),
    ("Which techniques does the lecture list under availability?",
     "Which techniques enforce availability?"),
    ("أي تقنيات تسردها المحاضرة تحت التوافر؟", "أي تقنيات تحقق التوافر؟"),
    ("Which four programs does the lecture group under malware?",
     "Which four programs are grouped under malware?"),
    ("أي أربعة برامج تصنّفها المحاضرة تحت البرمجيات الخبيثة؟",
     "أي أربعة برامج تُصنَّف تحت البرمجيات الخبيثة؟"),
    ("Which example does the lecture give for IoT attacks?",
     "Which botnet is the standard example of an IoT attack?"),
    ("أي مثال تعطيه المحاضرة لهجمات إنترنت الأشياء؟",
     "أي شبكة بوت هي المثال القياسي لهجوم إنترنت الأشياء؟"),
    ("Which three trends does the lecture record for 2023 and 2024?",
     "Which three trends shaped the 2023-2024 threat landscape?"),
    ("أي ثلاثة اتجاهات تسجّلها المحاضرة لعامي 2023 و2024؟",
     "أي ثلاثة اتجاهات شكّلت مشهد التهديدات في 2023-2024؟"),
    ("How does the lecture define risk?", "How is risk defined?"),
    ("كيف تعرّف المحاضرة الخطر؟", "كيف يُعرَّف الخطر؟"),
    ("Which examples does the lecture give for vulnerabilities?",
     "Which catalogues are the standard references for known vulnerabilities?"),
    ("أي أمثلة تعطيها المحاضرة للثغرات؟",
     "أي قائمتين هما المرجع القياسي للثغرات المعروفة؟"),
    ("Which three risk assessment models does the lecture name?",
     "Which three models are used for risk assessment?"),
    ("أي ثلاثة نماذج لتقييم المخاطر تسمّيها المحاضرة؟",
     "أي ثلاثة نماذج تُستخدم لتقييم المخاطر؟"),
    ("How does the lecture describe the Middle East approach?",
     "How is cyber governance organised in the Middle East?"),
    ("كيف تصف المحاضرة مقاربة الشرق الأوسط؟",
     "كيف تُنظَّم الحوكمة السيبرانية في الشرق الأوسط؟"),
    ("The lecture gives a rule of thumb for the optimisation result. What is it?",
     "In the optimisation model, what does a result above 100 indicate?"),
    ("المحاضرة تعطي قاعدة تقريبية لنتيجة التحسين. ما هي؟",
     "في نموذج التحسين، ماذا تعني نتيجة فوق 100؟"),

    # ---- explanations ----------------------------------------------------
    ("The lecture links it to national security, economic stability, and privacy protection. That is what raises it from an IT task to a national priority.",
     "Cybersecurity is tied to national security, economic stability, and privacy protection. That is what raises it from an IT task to a national priority."),
    ("المحاضرة تربطه بالأمن الوطني والاستقرار الاقتصادي وحماية الخصوصية. وهذا ما يرفعه من مهمة تقنية إلى أولوية وطنية.",
     "الأمن السيبراني مرتبط بالأمن الوطني والاستقرار الاقتصادي وحماية الخصوصية. وهذا ما يرفعه من مهمة تقنية إلى أولوية وطنية."),
    ("Firewalls and IDS/IPS are the two tools the lecture names for network security.",
     "Firewalls and IDS/IPS are the two defining tools of network security."),
    ("الجدران النارية وأنظمة كشف ومنع التطفل هما الأداتان اللتان تذكرهما المحاضرة لأمن الشبكات.",
     "الجدران النارية وأنظمة كشف ومنع التطفل هما أداتا أمن الشبكات المميّزتان."),
    ("IoT devices are small and low-powered, so the lecture pairs lightweight encryption with anomaly detection.",
     "IoT devices are small and low-powered, so their security rests on lightweight encryption and anomaly detection."),
    ("أجهزة إنترنت الأشياء صغيرة وقليلة الطاقة، لذلك تقرن المحاضرة التشفير الخفيف بكشف الشذوذ.",
     "أجهزة إنترنت الأشياء صغيرة وقليلة الطاقة، لذلك يعتمد أمنها على التشفير الخفيف وكشف الشذوذ."),
    ("The lecture states plainly that the CIA triad is the backbone of cybersecurity, and it highlights the whole block.",
     "The CIA triad is the backbone of cybersecurity: every control in this chapter serves one of its three pillars."),
    ("المحاضرة تنص صريحاً على أن ثالوث CIA هو العمود الفقري للأمن السيبراني، وقد ظلّلت الكتلة بأكملها.",
     "ثالوث CIA هو العمود الفقري للأمن السيبراني: كل ضابط في هذا الجابتر يخدم أحد أركانه الثلاثة."),
    ("The lecture gives healthcare as the example: confidentiality carries more weight because a disclosed diagnosis can never be taken back, while an outage can be repaired.",
     "In healthcare confidentiality carries more weight: a disclosed diagnosis can never be taken back, while an outage can be repaired."),
    ("المحاضرة تعطي الرعاية الصحية كمثال: السرية وزنها أعلى لأن التشخيص المكشوف لا يمكن سحبه، بينما الانقطاع يمكن إصلاحه.",
     "في الرعاية الصحية وزن السرية أعلى: التشخيص المكشوف لا يمكن سحبه، بينما الانقطاع يمكن إصلاحه."),
    ("The lecture names exactly four: viruses, worms, Trojans, and ransomware. Spyware, adware and rootkits are real, but they are not on this list.",
     "Malware covers exactly four here: viruses, worms, Trojans, and ransomware. Spyware, adware and rootkits are real, but they belong to other families."),
    ("المحاضرة تذكر أربعة بالضبط: الفيروسات والديدان وأحصنة طروادة وبرامج الفدية. التجسس والإعلانات والجذور الخفية موجودة فعلاً لكنها ليست في هذه القائمة.",
     "البرمجيات الخبيثة أربعة هنا: الفيروسات والديدان وأحصنة طروادة وبرامج الفدية. والتجسس والإعلانات والجذور الخفية موجودة لكنها من عائلات أخرى."),
    ("Phishing is social engineering: it targets the person, not the machine. The lecture puts it under exploiting human trust.",
     "Phishing is social engineering: it targets the person, not the machine, so its raw material is human trust."),
    ("التصيّد هندسة اجتماعية: يستهدف الشخص لا الآلة. والمحاضرة تضعه تحت استغلال ثقة الإنسان.",
     "التصيّد هندسة اجتماعية: يستهدف الشخص لا الآلة، فمادته الخام ثقة الإنسان."),
    ("The middle factor is the severity of the vulnerability, which the lecture ties to the CVSS score.",
     "The middle factor is the severity of the vulnerability, measured by its CVSS score."),
    ("العامل الأوسط هو درجة خطورة الثغرة، والمحاضرة تربطها بدرجة CVSS.",
     "العامل الأوسط هو درجة خطورة الثغرة، وتُقاس بدرجة CVSS."),
    ("A vulnerability is the weakness itself, and the lecture allows three places for it: software, hardware, and the human factor.",
     "A vulnerability is the weakness itself, and it can sit in software, hardware, or the human factor."),
    ("الثغرة هي الضعف نفسه، والمحاضرة تسمح بثلاثة مواضع له: البرمجيات والعتاد والعامل البشري.",
     "الثغرة هي الضعف نفسه، ويمكن أن يكون في البرمجيات أو العتاد أو العامل البشري."),
    ("The lecture allows software, hardware, or the human factor. A note on a monitor is neither code nor metal, so it is the human factor.",
     "A weakness can sit in software, hardware, or the human factor. A note on a monitor is neither code nor metal, so it is the human factor."),
    ("المحاضرة تسمح بثلاثة مواضع: البرمجيات أو العتاد أو العامل البشري. ورقة على الشاشة ليست كوداً ولا معدنًا، فهي العامل البشري.",
     "الضعف يكون في البرمجيات أو العتاد أو العامل البشري. ورقة على الشاشة ليست كوداً ولا معدناً، فهي العامل البشري."),
    ("F is the cumulative distribution function, and the lecture annotates that it is bounded between 0 and 1.",
     "F is the cumulative distribution function, and by definition it is bounded between 0 and 1."),
    ("F هي دالة التوزيع التراكمي، والمحاضرة تكتب ملاحظة أنها محصورة بين 0 و1.",
     "F هي دالة التوزيع التراكمي، وهي بحكم تعريفها محصورة بين 0 و1."),
    ("The international standards in the lecture are NIST and ISO 27001. The others are laws, vulnerability catalogues, or risk models.",
     "The international standards are NIST and ISO 27001. The others are laws, vulnerability catalogues, or risk models."),
    ("المعايير الدولية في المحاضرة هي NIST و ISO 27001. أما البقية فقوانين أو قواعد ثغرات أو نماذج مخاطر.",
     "المعايير الدولية هي NIST و ISO 27001. أما البقية فقوانين أو قواعد ثغرات أو نماذج مخاطر."),
    ("The lecture lists the NIST Cybersecurity Framework and the Federal Cybersecurity Strategy for the United States.",
     "The United States works through the NIST Cybersecurity Framework and the Federal Cybersecurity Strategy."),
    ("المحاضرة تذكر إطار NIST للأمن السيبراني والاستراتيجية الفدرالية للولايات المتحدة.",
     "الولايات المتحدة تعمل بإطار NIST للأمن السيبراني والاستراتيجية الفدرالية."),
]

files = sorted(glob.glob(r"C:\Users\gokoq\Master-Studio\scratch\ch01_t0*.py"))
applied = missing = 0
for f in files:
    s = open(f, encoding="utf-8").read()
    before = s
    for old, new in PAIRS:
        if old in s:
            s = s.replace(old, new)
            applied += 1
    if s != before:
        open(f, "w", encoding="utf-8").write(s)
print("replacements applied:", applied)
for old, new in PAIRS:
    hit = any(old in open(f, encoding="utf-8").read() for f in files)
    if hit:
        print("  STILL PRESENT:", old[:70])
