#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch03 T05 — The four emerging challenges to cyber risk management."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch03_lib import build

QUIZ = "Quiz_Ch03_T05_Emerging_Challenges"
TOPIC_EN = "Emerging Challenges: Cloud, IoT, AI, Quantum"
TOPIC_AR = "التحديات الناشئة: السحابة والأشياء والذكاء والكم"

I = [
    # 1 -------------------------------------------------------------------
    ("four_challenges", "Remember",
     "Which four challenges does risk management face now?",
     "أي أربعة تحديات تواجه إدارة المخاطر الآن؟",
     ["Cloud, IoT and OT, AI-driven attacks, quantum.",
      "Phishing, ransomware, insider fraud, DDoS.",
      "Patching, backups, training, and auditing.",
      "Budget cuts, staff turnover, and big mergers."],
     ["السحابة وإنترنت الأشياء والذكاء الاصطناعي وهجمات الحجب.",
      "التصيّد والفدية والاحتيال الداخلي وهجمات الحجب هنا.",
      "التحديث والنسخ والتدريب والتدقيق الأمني هنا تماماً.",
      "تخفيض الميزانية ودوران الموظفين والاندماج الكبير جداً."],
     "Four: cloud security, IoT and operational technology, AI-driven attacks, and quantum computing.",
     "أربعة: أمن السحابة، وإنترنت الأشياء والتقنيات التشغيلية، والهجمات المدفوعة بالذكاء الاصطناعي، والحوسبة الكمومية."),

    # 2 -------------------------------------------------------------------
    ("cloud_cause", "Remember",
     "What is the leading cause of cloud breaches?",
     "ما السبب الرئيسي لاختراقات السحابة؟",
     ["Misconfigured cloud storage, such as open buckets.",
      "Weak passwords chosen by the cloud provider itself.",
      "Encrypted backups that cannot be restored.",
      "Too many administrators sharing one account."],
     ["سوء إعداد التخزين السحابي كالدلاء المفتوحة.",
      "كلمات مرور ضعيفة يختارها المزوّد نفسه هنا.",
      "نسخ مشفّرة لا يمكن استعادتها أبداً هنا تماماً.",
      "مديرون كثيرون يتشاركون حساباً واحداً هنا."],
     "Misconfigured cloud storage, such as an open S3 bucket, is a leading cause of breaches: the data is exposed by a setting, not by an exploit.",
     "سوء إعداد التخزين السحابي، كدلو S3 مفتوح، من الأسباب الرئيسية للاختراق: البيانات تنكشف بإعداد خاطئ لا باستغلال ثغرة."),

    # 3 -------------------------------------------------------------------
    ("iot_attack_surface", "Remember",
     "What do billions of IoT devices do to the risk picture?",
     "ماذا تفعل مليارات أجهزة إنترنت الأشياء بصورة الخطر؟",
     ["The attack surface, through billions of devices.",
      "The network speed between the connected devices.",
      "The monthly cost of the cloud subscription.",
      "The number of staff needed to run the plant."],
     ["مساحة الهجوم بمليارات الأجهزة.",
      "سرعة الشبكة بين الأجهزة المتصلة.",
      "الكلفة الشهرية لاشتراك السحابة.",
      "عدد الموظفين اللازم لتشغيل المصنع."],
     "They expand the attack surface enormously: every connected device is another entry point that has to be secured.",
     "توسّع مساحة الهجوم هائلةً: كل جهاز متصل نقطة دخول أخرى يجب تأمينها."),

    # 4 -------------------------------------------------------------------
    ("ics_missing", "Remember",
     "What do industrial control systems lack?",
     "ما الذي تفتقر إليه أنظمة التحكم الصناعي؟",
     ["Robust security in industrial control systems.",
      "Fast internet links between all the plants.",
      "Enough trained operators to run the whole plant.",
      "An adequate budget for new machinery here."],
     ["أمن قوي في أنظمة التحكم الصناعي.",
      "روابط إنترنت سريعة بين المصانع.",
      "مشغّلون كافون لتشغيل المصنع هنا.",
      "ميزانية كافية لآلات جديدة هنا."],
     "ICS were built for availability and safety, not for security, so they lack robust protection while being connected to the same networks.",
     "أنظمة التحكم الصناعي بُنيت للتوافر والسلامة لا للأمن، فهي تفتقر لحماية قوية وهي متصلة بالشبكات نفسها."),

    # 5 -------------------------------------------------------------------
    ("ai_weaponised", "Remember",
     "Which two forms of attack is AI used to produce?",
     "أي شكلين من الهجوم يُستخدم الذكاء الاصطناعي لإنتاجهما؟",
     ["Polymorphic malware and deepfake phishing.",
      "Faster patching and much better detection.",
      "Cheaper storage and faster networks.",
      "Stronger encryption and longer keys."],
     ["برمجيات متعددة الأشكال وتصيّد عميق.",
      "تحديث أسرع بكثير وكشف أفضل هنا تماماً.",
      "تخزين أرخص بكثير وشبكات أسرع هنا.",
      "تشفير أقوى بكثير ومفاتيح أطول هنا."],
     "AI is weaponised for polymorphic malware, which changes shape to evade signatures, and for deepfake phishing, which fakes a person.",
     "الذكاء يُستخدم كسلاح لإنتاج برمجيات متعددة الأشكال تتغيّر لتفادي التوقيعات، ولتصيّد بالتزييف العميق ينتحل شخصاً."),

    # 6 -------------------------------------------------------------------
    ("quantum_breaks", "Remember",
     "Which algorithms does quantum computing break?",
     "أي خوارزميات تكسرها الحوسبة الكمومية؟",
     ["RSA and ECC public-key algorithms.",
      "AES and SHA-256 symmetric ciphers.",
      "TLS and HTTPS transport protocols.",
      "Passwords and PINs used by staff."],
     ["خوارزميتا RSA و ECC للمفتاح العام.",
      "خوارزميتا AES و SHA-256 المتماثلتان.",
      "بروتوكولا TLS و HTTPS للنقل.",
      "كلمات المرور والأرقام السرية."],
     "It breaks the public-key algorithms RSA and ECC, which is what makes the migration problem urgent.",
     "تكسر خوارزميات المفتاح العام RSA و ECC، وهذا ما يجعل مشكلة الانتقال عاجلة."),

    # 7 -------------------------------------------------------------------
    ("quantum_plan", "Remember",
     "What must risk management plan for because of quantum computing?",
     "لماذا يجب أن تخطط إدارة المخاطر بسبب الحوسبة الكمومية؟",
     ["Plan for post-quantum cryptography.",
      "Buy much longer RSA keys immediately.",
      "Stop using encryption altogether.",
      "Rely on the cloud provider's keys."],
     ["التخطيط للتشفير ما بعد الكمومي.",
      "شراء مفاتيح RSA أطول بكثير فوراً.",
      "التوقف عن استخدام التشفير كلياً.",
      "الاعتماد على مفاتيح مزوّد السحابة."],
     "The answer is post-quantum cryptography: migration takes years, so the planning has to start before the machine exists.",
     "الجواب هو التشفير ما بعد الكمومي: الانتقال يستغرق سنوات، فالتخطيط يبدأ قبل وجود الآلة."),

    # 8 -------------------------------------------------------------------
    ("challenges_conclusion", "Understand",
     "What do these four challenges together prove?",
     "ماذا تثبته هذه التحديات الأربعة معاً؟",
     ["They make risk management dynamic and forward-looking.",
      "They remove the need for any risk register at all here.",
      "They prove that the cloud is unsafe for anyone to use.",
      "They only affect the very largest organisations today."],
     ["تجعل إدارة المخاطر ديناميكية واستباقية.",
      "تلغي الحاجة إلى أي سجل مخاطر تماماً هنا.",
      "تثبت أن السحابة غير آمنة إطلاقاً هنا.",
      "تؤثر فقط في المؤسسات الكبيرة جداً هنا."],
     "Together they show risk management has to be a dynamic, forward-looking discipline rather than an annual audit.",
     "معاً تُظهر أن إدارة المخاطر يجب أن تكون تخصصاً ديناميكياً يستشرف المستقبل لا تدقيقاً سنوياً."),

    # 9 -------------------------------------------------------------------
    ("scenario_iot_ot", "Apply",
     "A hospital connects thousands of infusion pumps to its network. Which challenge is this?",
     "مستشفى يربط آلاف مضخات التسريب بشبكته. أي تحدٍّ هذا؟",
     ["An IoT and operational-technology risk.",
      "A cloud storage misconfiguration risk.",
      "A quantum computing threat to the keys.",
      "An AI-driven deepfake phishing risk."],
     ["خطر إنترنت الأشياء والتقنيات التشغيلية.",
      "خطر سوء إعداد التخزين السحابي هنا تماماً.",
      "خطر الحوسبة الكمومية على المفاتيح.",
      "خطر تصيّد بالتزييف العميق بالذكاء هنا."],
     "Medical devices on the network are IoT and operational technology: many entry points, and the devices themselves are rarely hardened.",
     "الأجهزة الطبية على الشبكة هي إنترنت أشياء وتقنية تشغيلية: نقاط دخول كثيرة، والأجهزة نفسها نادراً ما تكون محصّنة."),

    # 10 ------------------------------------------------------------------
    ("scenario_cloud", "Apply",
     "A bucket holding customer files is left readable by anyone. Which challenge is this?",
     "دلو يحوي ملفات عملاء تُرك قابلاً للقراءة من أي أحد. أي تحدٍّ هذا؟",
     ["A cloud storage misconfiguration risk.",
      "An IoT and operational-technology risk.",
      "A quantum computing risk for keys.",
      "A supply chain compromise at the vendor."],
     ["خطر سوء إعداد التخزين السحابي هنا.",
      "خطر إنترنت الأشياء والتشغيلية هنا.",
      "خطر الحوسبة الكمومية على المفاتيح.",
      "خطر اختراق سلسلة التوريد هنا."],
     "An open bucket is a configuration mistake in the cloud, which is exactly the failure mode the cloud challenge describes.",
     "الدلو المفتوح خطأ إعداد في السحابة، وهو بالضبط نمط الفشل الذي يصفه تحدّي السحابة."),

    # 11 ------------------------------------------------------------------
    ("why_forward_looking", "Understand",
     "Why must the discipline look forward rather than report backwards?",
     "لماذا يجب أن تستشرف المهنة المستقبل لا أن تكتفي بتقرير الماضي؟",
     ["The threat may arrive before the control does.",
      "Auditors demand a full five-year projection.",
      "Budgets are set before the year begins.",
      "Regulators publish a list of new risks yearly."],
     ["قد يصل التهديد قبل أن يصل الضابط.",
      "المدققون يطلبون توقعاً لخمس سنوات.",
      "الميزانيات تُقرَّر قبل بداية السنة.",
      "الجهات التنظيمية تنشر قائمة مخاطر."],
     "Quantum and AI threats are known before they are usable, so the control has to be ready first. A backward-looking report always arrives late.",
     "تهديدات الكم والذكاء معروفة قبل أن تصبح قابلة للاستخدام، فالضابط يجب أن يكون جاهزاً أولاً. والتقرير الرجعي يصل متأخراً دائماً."),
]

KEY = "ABCDABCDABC"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
