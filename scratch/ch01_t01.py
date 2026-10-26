#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch01 T01 — Definition, scope and historical evolution."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch01_lib import build

QUIZ = "Quiz_Ch01_T01_Cybersecurity_Definition_and_Evolution"
TOPIC_EN = "Definition, Scope & Historical Evolution"
TOPIC_AR = "التعريف والنطاق والتطور التاريخي"

I = [
    # 1 -------------------------------------------------------------------
    ("cyber_def_protected_assets", "Remember",
     "Which set of assets does the cybersecurity definition protect?",
     "أي مجموعة أصول يحميها تعريف الأمن السيبراني؟",
     ["Systems, networks, applications, and data.",
      "Servers, routers, applications, and users.",
      "Devices, accounts, applications, and sites.",
      "Networks, databases, passwords, and files."],
     ["الأنظمة والشبكات والتطبيقات والبيانات الرقمية.",
      "الخوادم والموجّهات والتطبيقات والمستخدمين.",
      "الأجهزة والحسابات والتطبيقات والمواقع.",
      "الشبكات وقواعد البيانات وكلمات المرور والملفات."],
     "The definition protects four assets: systems, networks, applications, and data. The other sets mix in users, accounts or passwords, which are not part of it.",
     "التعريف يحمي أربعة أصول: الأنظمة والشبكات والتطبيقات والبيانات. بقية المجموعات تُدخل المستخدمين أو الحسابات أو كلمات المرور، وهي ليست ضمنه."),

    # 2 -------------------------------------------------------------------
    ("cyber_def_practice_continuous", "Understand",
     "The definition calls cybersecurity a practice. What does that word imply?",
     "التعريف يصف الأمن السيبراني بأنه ممارسة. ماذا يعني ذلك؟",
     ["It is continuous work, not a product you install once.",
      "It is a licence a company buys and renews every year.",
      "It is a task done only after an incident happens.",
      "It is a service that outside vendors must deliver."],
     ["عمل مستمر وليس منتجاً يُثبَّت مرة واحدة.",
      "ترخيص تشتريه الشركة وتجدده كل سنة.",
      "مهمة تُنفَّذ فقط بعد وقوع حادث أمني كبير.",
      "خدمة يجب أن يقدمها مزوّدون خارجيون."],
     "Practice means ongoing work: monitoring, updating and responding all the time. A product or a licence can be bought once; a practice cannot.",
     "الممارسة تعني عملاً مستمراً: مراقبة وتحديث واستجابة طوال الوقت. المنتج أو الترخيص يُشترى مرة واحدة، أما الممارسة فلا."),

    # 3 -------------------------------------------------------------------
    ("cyber_four_aspects", "Remember",
     "Which four aspects does cybersecurity cover?",
     "أي أربعة جوانب يغطيها الأمن السيبراني؟",
     ["Technical, legal, managerial, and social.",
      "Technical, physical, financial, and legal.",
      "Legal, military, political, and social.",
      "Managerial, economic, ethical, and social."],
     ["تقنية وقانونية وإدارية واجتماعية.",
      "تقنية ومادية ومالية وقانونية.",
      "قانونية وعسكرية وسياسية واجتماعية.",
      "إدارية واقتصادية وأخلاقية واجتماعية."],
     "The four aspects are technical, legal, managerial, and social. A firewall alone fails without a policy and without user awareness.",
     "الجوانب الأربعة هي: تقنية وقانونية وإدارية واجتماعية. الجدار الناري وحده يفشل بدون سياسة وبدون وعي المستخدم."),

    # 4 -------------------------------------------------------------------
    ("cyber_scope_span", "Remember",
     "What range does the scope of cybersecurity cover?",
     "أي مدى يغطيه نطاق الأمن السيبراني؟",
     ["From personal devices up to national critical infrastructure.",
      "From home routers up to the networks of the commercial banks.",
      "From office desktops up to the servers of a campus site.",
      "From mobile phones up to the data centres of a company."],
     ["من الأجهزة الشخصية إلى البنية التحتية الوطنية الحرجة.",
      "من موجّهات المنزل إلى شبكات المصارف التجارية والدولية.",
      "من حواسيب المكتب إلى خوادم الحرم الجامعي.",
      "من الهواتف النقالة إلى مراكز بيانات المؤسسات."],
     "The scope starts at personal devices and ends at national critical infrastructure, so every level in between is in scope.",
     "النطاق يبدأ من الأجهزة الشخصية وينتهي بالبنية التحتية الوطنية الحرجة، وكل مستوى بينهما داخل النطاق."),

    # 5 -------------------------------------------------------------------
    ("cyber_importance_three_links", "Remember",
     "Cybersecurity is linked directly to which three concerns?",
     "بأي ثلاث قضايا يرتبط الأمن السيبراني مباشرةً؟",
     ["National security, economic stability, and privacy.",
      "Data accuracy, system speed, and the trust of vendors.",
      "Legal liability, staff training, and insurance.",
      "Market share, brand design, and recruitment."],
     ["الأمن الوطني والاستقرار الاقتصادي والخصوصية.",
      "دقة البيانات وسرعة الأنظمة وثقة المورّد.",
      "المسؤولية القانونية وتدريب الموظفين والتأمين.",
      "الحصة السوقية وتصميم العلامة والتوظيف."],
     "Cybersecurity is tied to national security, economic stability, and privacy protection. That is what raises it from an IT task to a national priority.",
     "الأمن السيبراني مرتبط بالأمن الوطني والاستقرار الاقتصادي وحماية الخصوصية. وهذا ما يرفعه من مهمة تقنية إلى أولوية وطنية."),

    # 6 -------------------------------------------------------------------
    ("evolution_1960s_arpanet", "Remember",
     "What marked the first mention of cybersecurity in the 1960s?",
     "ما الذي ميّز أول ذكر للأمن السيبراني في الستينيات؟",
     ["ARPANET and the first multi-user mainframes.",
      "The first personal computers sold to home users.",
      "The public launch of commercial web browsers.",
      "The spread of wireless mobile phone networks."],
     ["ظهور ARPANET وأول أنظمة حاسبات مركزية متعددة المستخدمين.",
      "أول حواسيب شخصية تُباع للمستخدمين في المنازل.",
      "الإطلاق العام لمتصفحات الويب التجارية على شبكة الإنترنت.",
      "انتشار شبكات الهواتف النقالة اللاسلكية بين الجمهور."],
     "The 1960s stage is ARPANET with early mainframes. Personal computers, browsers and mobile networks all come later.",
     "مرحلة الستينيات هي ARPANET مع الحاسبات المركزية الأولى. الحواسيب الشخصية والمتصفحات وشبكات النقال تأتي كلها بعدها."),

    # 7 -------------------------------------------------------------------
    ("evolution_1980s_1990s_malware", "Remember",
     "What defined the 1980s and 1990s in the cybersecurity timeline?",
     "ما الذي ميّز الثمانينيات والتسعينيات في الخط الزمني للأمن السيبراني؟",
     ["Viruses, worms, and the first antivirus products.",
      "Ransomware, botnets, and state-sponsored intrusion.",
      "Firewalls, encryption, and formal access control.",
      "Cloud outages, misconfiguration, and data leaks."],
     ["الفيروسات والديدان وأول برامج مضادة للفيروسات.",
      "برامج الفدية وشبكات البوت والاختراق المدعوم من دول.",
      "الجدران النارية والتشفير وضوابط الوصول الرسمية.",
      "انقطاع السحابة وسوء الإعداد وتسريب البيانات."],
     "That stage produced viruses and worms, and the antivirus products built to answer them. Ransomware and cloud leaks belong to later stages.",
     "تلك المرحلة أنتجت الفيروسات والديدان، ومعها برامج مضادة للفيروسات. الفدية وتسريبات السحابة تعود لمراحل لاحقة."),

    # 8 -------------------------------------------------------------------
    ("evolution_2000s_ecommerce", "Remember",
     "Which development pushed cybersecurity into business in the 2000s?",
     "أي تطور دفع الأمن السيبراني إلى عالم الأعمال في الألفينيات؟",
     ["The growth of e-commerce and online banking.",
      "The arrival of national privacy legislation.",
      "The spread of industrial control systems.",
      "The move of records to paper archives."],
     ["نمو التجارة الإلكترونية والمصرفية عبر الإنترنت.",
      "وصول تشريعات الخصوصية الوطنية إلى المنطقة كلها.",
      "انتشار أنظمة التحكم الصناعي في المصانع.",
      "نقل السجلات الرسمية إلى أرشيف ورقي بعيد."],
     "In the 2000s cybersecurity became integral to e-commerce and e-banking, because money started moving online.",
     "في الألفينيات صار الأمن السيبراني جزءاً أساسياً من التجارة الإلكترونية والمصرفية، لأن المال بدأ ينتقل عبر الشبكة."),

    # 9 -------------------------------------------------------------------
    ("evolution_current_era_threat", "Remember",
     "Which threat is characteristic of the current era, 2010s to today?",
     "أي تهديد يميّز العصر الحالي، من 2010 إلى اليوم؟",
     ["Ransomware and state-sponsored APTs.",
      "Boot-sector viruses on floppy disks.",
      "Telephone line eavesdropping on calls.",
      "Unauthenticated email relay abuse."],
     ["برامج الفدية والتهديدات المدعومة من دول.",
      "فيروسات الإقلاع على أقراص الفلوبي القديمة.",
      "التنصّت على المكالمات الهاتفية الأرضية.",
      "إساءة استخدام خوادم البريد المفتوحة."],
     "The current era adds APTs, ransomware, IoT attacks, AI-driven attacks and the Zero Trust model.",
     "العصر الحالي يضيف التهديدات المتقدمة وبرامج الفدية وهجمات إنترنت الأشياء والهجمات بالذكاء الاصطناعي ونموذج الثقة الصفرية."),

    # 10 ------------------------------------------------------------------
    ("evolution_driver_of_shift", "Analyze",
     "Why did the focus of cybersecurity shift from one era to the next?",
     "لماذا تحوّل تركيز الأمن السيبراني من عصر إلى آخر؟",
     ["Each era produced a new dominant threat and a matching defence.",
      "Each era inherited the same threat and changed only the tools.",
      "Governments forced a complete rewrite of protocols each decade.",
      "Vendors replaced their products on a fixed ten-year cycle."],
     ["كل عصر أنتج تهديداً مسيطراً جديداً ودفاعاً يقابله.",
      "كل عصر ورث التهديد نفسه وغيّر الأدوات فقط.",
      "الحكومات فرضت إعادة كتابة البروتوكولات كل عقد.",
      "المورّدون استبدلوا منتجاتهم وفق دورة عشرية ثابتة تماماً."],
     "The timeline moves with the threat: networks, then viruses, then online money, then organised and state-backed attack. Each stage answers the one before it.",
     "الخط الزمني يتحرك مع التهديد: الشبكات، ثم الفيروسات، ثم المال الرقمي، ثم الهجوم المنظّم والمدعوم من دول. كل مرحلة تجيب على التي قبلها."),
]

KEY = "ADBCABCDAB"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
