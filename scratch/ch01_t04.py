#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch01 T04 — Modern threat landscape, global trends, and the AS metric."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch01_lib import build

QUIZ = "Quiz_Ch01_T04_Threat_Landscape_and_Attack_Surface"
TOPIC_EN = "Modern Threat Landscape & Attack Surface Metric AS"
TOPIC_AR = "مشهد التهديدات الحديث ومقياس سطح الهجوم"

I = [
    # 1 -------------------------------------------------------------------
    ("threat_five_categories", "Remember",
     "Which set lists the five categories of the modern threat landscape?",
     "أي مجموعة تسرد فئات مشهد التهديدات الحديث الخمس؟",
     ["Malware, phishing, insiders, APTs, and IoT attacks.",
      "Malware, phishing, insiders, botnets, and spam mail.",
      "Viruses, phishing, insiders, APTs, and data leaks.",
      "Malware, phishing, insiders, DDoS floods, and theft."],
     ["البرمجيات الخبيثة والتصيّد والتهديدات الداخلية والتهديدات المتقدمة وهجمات إنترنت الأشياء.",
      "البرمجيات الخبيثة والتصيّد والتهديدات الداخلية والبوتنت والبريد المزعج.",
      "الفيروسات والتصيّد والتهديدات الداخلية والتهديدات المتقدمة وتسريب البيانات.",
      "البرمجيات الخبيثة والتصيّد والتهديدات الداخلية وهجمات الحجب والسرقة."],
     "The five are malware, phishing and social engineering, insider threats, APTs, and IoT attacks. A botnet is the tool behind the IoT category, not a category of its own.",
     "الخمسة هي: البرمجيات الخبيثة، التصيّد والهندسة الاجتماعية، التهديدات الداخلية، التهديدات المتقدمة، هجمات إنترنت الأشياء. والبوتنت أداة داخل فئة إنترنت الأشياء لا فئة مستقلة."),

    # 2 -------------------------------------------------------------------
    ("threat_malware_types", "Remember",
     "Which four programs are grouped under malware?",
     "أي أربعة برامج تُصنَّف تحت البرمجيات الخبيثة؟",
     ["Viruses, worms, Trojans, and ransomware.",
      "Worms, Trojans, spyware, and rootkits.",
      "Viruses, bots, adware, and keyloggers.",
      "Trojans, ransomware, worms, and backdoors."],
     ["الفيروسات والديدان وأحصنة طروادة وبرامج الفدية.",
      "الديدان وأحصنة طروادة وبرامج التجسس والجذور الخفية.",
      "الفيروسات والبوتات والبرامج الإعلانية ومسجلات المفاتيح.",
      "أحصنة طروادة والفدية والديدان والأبواب الخلفية."],
     "Malware covers exactly four here: viruses, worms, Trojans, and ransomware. Spyware, adware and rootkits are real, but they belong to other families.",
     "البرمجيات الخبيثة أربعة هنا: الفيروسات والديدان وأحصنة طروادة وبرامج الفدية. والتجسس والإعلانات والجذور الخفية موجودة لكنها من عائلات أخرى."),

    # 3 -------------------------------------------------------------------
    ("threat_phishing_exploits_trust", "Understand",
     "What does phishing exploit?",
     "ماذا يستغل التصيّد؟",
     ["Human trust and the fear of being blamed.",
      "Memory errors inside the running software.",
      "Weak encryption keys used on the server.",
      "Slow links between the internal networks."],
     ["ثقة الإنسان والخوف من اللوم.",
      "أخطاء الذاكرة في البرمجيات.",
      "ضعف مفاتيح التشفير المستخدمة.",
      "بطء روابط الشبكة الداخلية."],
     "Phishing is social engineering: it targets the person, not the machine, so its raw material is human trust.",
     "التصيّد هندسة اجتماعية: يستهدف الشخص لا الآلة، فمادته الخام ثقة الإنسان."),

    # 4 -------------------------------------------------------------------
    ("threat_insider_definition", "Understand",
     "How is an insider threat described?",
     "كيف يُوصف التهديد الداخلي؟",
     ["An employee misusing legitimate access.",
      "An outsider breaking through the firewall.",
      "A virus spreading across the local network.",
      "A botnet flooding the public website."],
     ["موظف يسيء استخدام صلاحياته المشروعة.",
      "شخص خارجي يخترق الجدار الناري.",
      "فيروس ينتشر داخل الشبكة المحلية.",
      "شبكة بوت تغرق الموقع العام بالطلبات."],
     "The insider is inside already: an employee, contractor or trusted person who misuses access they legitimately hold.",
     "الداخلي موجود في الداخل أصلاً: موظف أو متعاقد أو شخص موثوق يسيء استخدام صلاحية يملكها بشكل مشروع."),

    # 5 -------------------------------------------------------------------
    ("threat_apt_definition", "Remember",
     "What defines an advanced persistent threat?",
     "ما الذي يميّز التهديد المتقدم المستمر؟",
     ["State backing, stealth, and long presence.",
      "Fast spreading, noise, and instant damage.",
      "Low skill, random targets, and short visits.",
      "Open tools, public targets, and one strike."],
     ["دعم دولة وخفاء وحضور طويل.",
      "انتشار سريع وضجيج وضرر فوري.",
      "مهارة منخفضة وأهداف عشوائية.",
      "أدوات مفتوحة وأهداف معلنة."],
     "An APT is state-sponsored, stealthy, and sustained over a long period. Noise and speed are the opposite of what it wants.",
     "التهديد المتقدم مدعوم من دولة، خفي، ومستمر لفترة طويلة. الضجيج والسرعة نقيض ما يريده."),

    # 6 -------------------------------------------------------------------
    ("threat_iot_botnet_example", "Remember",
     "Which botnet is the standard example of an IoT attack?",
     "أي شبكة بوت هي المثال القياسي لهجوم إنترنت الأشياء؟",
     ["The Mirai botnet of infected devices.",
      "A worm spreading through email attachments.",
      "A Trojan hidden inside a free download.",
      "A virus infecting the boot sector area."],
     ["شبكة بوت Mirai من الأجهزة المصابة.",
      "دودة تنتشر عبر مرفقات البريد الإلكتروني.",
      "حصان طروادة مخفي داخل تنزيل مجاني.",
      "فيروس يصيب قطاع الإقلاع في القرص."],
     "Mirai is the named example: a botnet built from compromised IoT devices such as cameras and routers.",
     "Mirai هو المثال القياسي: شبكة بوت مبنية من أجهزة إنترنت أشياء مخترقة كالكاميرات والموجّهات."),

    # 7 -------------------------------------------------------------------
    ("threat_scenario_insider", "Apply",
     "An employee copies the customer list before resigning. Which category is this?",
     "موظف ينسخ قائمة العملاء قبل استقالته. أي فئة هذا؟",
     ["An insider threat.", "A phishing campaign.",
      "An IoT device botnet.", "An APT intrusion."],
     ["تهديد داخلي من موظف.", "حملة تصيّد إلكتروني.",
      "شبكة بوت لأجهزة.", "اختراق متقدم مستمر."],
     "He held legitimate access and used it for a purpose it was not granted for, which is the definition of an insider threat.",
     "كان يملك صلاحية مشروعة واستخدمها لغرض لم تُمنح له، وهذا تعريف التهديد الداخلي."),

    # 8 -------------------------------------------------------------------
    ("threat_scenario_phishing", "Apply",
     "An email claiming to be from IT asks for your password. Which category is this?",
     "بريد يدّعي أنه من قسم تقنية المعلومات ويطلب كلمة مرورك. أي فئة هذا؟",
     ["A phishing attempt.", "An insider threat.",
      "A malware infection.", "An APT intrusion."],
     ["محاولة تصيّد احتيالية.", "تهديد داخلي من موظف.",
      "إصابة ببرمجية خبيثة.", "اختراق متقدم مستمر."],
     "It asks the person to hand over a credential, which is social engineering rather than a technical break-in.",
     "الرسالة تطلب من الشخص تسليم بيانات دخوله، وهذا هندسة اجتماعية لا اختراق تقني."),

    # 9 -------------------------------------------------------------------
    ("trends_2023_2024", "Remember",
     "Which three trends shaped the 2023-2024 threat landscape?",
     "أي ثلاثة اتجاهات شكّلت مشهد التهديدات في 2023-2024؟",
     ["Rising ransomware losses, cloud misconfiguration, AI attacks.",
      "Falling ransomware losses, cloud migration, and AI defence.",
      "Rising malware volume, tape backups, and manual auditing.",
      "Flat ransomware losses, on-premise servers, and spam mail."],
     ["ارتفاع خسائر الفدية وسوء إعداد السحابة وهجمات الذكاء الاصطناعي.",
      "انخفاض خسائر الفدية والانتقال للسحابة والدفاع بالذكاء الاصطناعي.",
      "ارتفاع حجم البرمجيات الخبيثة والنسخ على الأشرطة والتدقيق اليدوي.",
      "ثبات خسائر الفدية والخوادم المحلية والبريد المزعج."],
     "The three are: ransomware losses above 20 billion dollars, cloud attacks rising from misconfiguration, and AI-powered attacks growing.",
     "الثلاثة هي: خسائر الفدية فوق عشرين مليار دولار، وارتفاع الهجمات السحابية بسبب سوء الإعداد، ونمو الهجمات المدعومة بالذكاء الاصطناعي."),

    # 10 ------------------------------------------------------------------
    ("attack_surface_model_symbols", "Remember",
     "In the attack surface metric, what does the middle factor represent?",
     "في مقياس سطح الهجوم، ماذا يمثّل العامل الأوسط؟",
     ["The severity of the flaw on that component.",
      "The number of entry points exposed on it.",
      "The value of the asset behind that component.",
      "The cost of the security control applied to it."],
     ["درجة خطورة الثغرة في ذلك المكوّن.",
      "عدد نقاط الدخول المكشوفة فيه.",
      "قيمة الأصل الذي يقف خلف المكوّن.",
      "تكلفة الضابط الأمني المطبّق عليه."],
     "The middle factor is the severity of the vulnerability, measured by its CVSS score.",
     "العامل الأوسط هو درجة خطورة الثغرة، وتُقاس بدرجة CVSS."),

    # 11 ------------------------------------------------------------------
    ("attack_surface_compute", "Apply",
     "A component has 2 entry points, a flaw severity of 3, and an asset value of 500. What is its attack surface score?",
     "مكوّن له نقطتا دخول، وخطورة ثغرة 3، وقيمة أصل 500. ما درجة سطح الهجوم له؟",
     ["3,000", "1,000", "2,500", "3,500"],
     ["3,000", "1,000", "2,500", "3,500"],
     "Multiply the three factors: 2 x 3 x 500 = 3,000. The model is a product, not a sum.",
     "اضرب العوامل الثلاثة: 2 × 3 × 500 = 3,000. النموذج حاصل ضرب لا مجموع."),

    # 12 ------------------------------------------------------------------
    ("attack_surface_meaning", "Understand",
     "What does a higher attack surface score tell you?",
     "ماذا تخبرك درجة سطح هجوم أعلى؟",
     ["The system is more exposed to being attacked.",
      "The system has stronger controls than before.",
      "The system has fewer users than it should.",
      "The system has older hardware than average."],
     ["النظام أكثر تعرضاً للهجوم من غيره.",
      "النظام يملك ضوابط أقوى من قبل.",
      "النظام يملك مستخدمين أقل من اللازم.",
      "النظام يملك عتاداً أقدم من المتوسط."],
     "The score measures how attackable the system is. More entry points, worse flaws or more valuable assets all push it up.",
     "الدرجة تقيس مدى قابلية النظام للاختراق. نقاط دخول أكثر أو ثغرات أخطر أو أصول أثمن ترفعها كلها."),
]

KEY = "ACBDABCDACBD"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
