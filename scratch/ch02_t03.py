#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch02 T03 — The four threat groups and the countermeasure pairings."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch02_lib import build

QUIZ = "Quiz_Ch02_T03_Threat_Groups_And_Countermeasures"
TOPIC_EN = "The Four Threat Groups & Their Countermeasures"
TOPIC_AR = "مجموعات التهديد الأربع والتدابير المضادة"

I = [
    # 1 -------------------------------------------------------------------
    ("threat_groups_count", "Remember",
     "Into how many main groups does the lecture divide threats?",
     "إلى كم مجموعة رئيسية تقسم المحاضرة التهديدات؟",
     ["Four main groups.", "Three main groups.",
      "Five main groups.", "Six main groups."],
     ["أربع مجموعات رئيسية.", "ثلاث مجموعات رئيسية.",
      "خمس مجموعات رئيسية.", "ست مجموعات رئيسية."],
     "The lecture says at least four: hardware, software, data, and liveware.",
     "المحاضرة تقول أربع على الأقل: العتاد، البرمجيات، البيانات، والعامل البشري."),

    # 2 -------------------------------------------------------------------
    ("mistaken_belief", "Understand",
     "Which mistaken belief does the lecture set out to correct?",
     "أي اعتقاد خاطئ تحاول المحاضرة تصحيحه؟",
     ["That only outside hackers threaten a computer.",
      "That hardware faults are the main danger.",
      "That insiders are more dangerous than hackers.",
      "That software errors are always deliberate."],
     ["أن المخترقين الخارجيين وحدهم تهديد.",
      "أن أعطال العتاد هي الخطر الأكبر دائماً.",
      "أن الداخليين أخطر من المخترقين.",
      "أن أخطاء البرمجيات دائماً متعمّدة."],
     "Many users think the only threat is an attacker breaking in. The lecture answers that the threat pattern is far more varied.",
     "كثير من المستخدمين يظنون أن التهديد الوحيد هو مهاجم يخترق الجهاز. والمحاضرة تجيب أن نمط التهديدات أوسع بكثير."),

    # 3 -------------------------------------------------------------------
    ("hardware_group_content", "Remember",
     "Which set lists hardware-related threats?",
     "أي مجموعة تسرد تهديدات متعلقة بالعتاد؟",
     ["Storms, theft, and faults in the infrastructure.",
      "Viruses, worms, and Trojan horses inside the files.",
      "Inference, masquerading, and deletion of data.",
      "Phishing, IT fraud, and forgery by the users."],
     ["العواصف والسرقة وأعطال البنية التحتية.",
      "الفيروسات والديدان وأحصنة طروادة في الملفات.",
      "الاستنتاج والتنكّر والحذف غير المصرّح.",
      "التصيّد والاحتيال والتزوير من المستخدمين."],
     "Hardware threats act physically on the machine or the infrastructure it depends on: harmful surroundings, storms, theft, and infrastructure faults.",
     "تهديدات العتاد تؤثر مادياً على الجهاز أو البنية التي يعتمد عليها: بيئة ضارّة، عواصف، سرقة، وأعطال في البنية."),

    # 4 -------------------------------------------------------------------
    ("software_group_content", "Remember",
     "Which set lists software-related threats?",
     "أي مجموعة تسرد تهديدات متعلقة بالبرمجيات؟",
     ["Viruses, worms, Trojan horses, and logic bombs.",
      "Storms, theft, and faults in the infrastructure.",
      "Inference, masquerading, and deletion of data.",
      "Phishing, IT fraud, and forgery by the users."],
     ["الفيروسات والديدان وأحصنة طروادة والقنابل المنطقية.",
      "العواصف والسرقة وأعطال البنية التحتية للشبكة كلها معاً.",
      "الاستنتاج والتنكّر والحذف غير المصرّح للبيانات.",
      "التصيّد والاحتيال والتزوير من قبل المستخدمين."],
     "Software threats cover malware, badly designed programs with vulnerabilities, out-of-date versions, and unauthorized copying of software.",
     "تهديدات البرمجيات تشمل البرمجيات الخبيثة، والبرامج سيئة التصميم التي فيها ثغرات، والإصدارات القديمة، والنسخ غير المصرّح به."),

    # 5 -------------------------------------------------------------------
    ("inference_meaning", "Remember",
     "What does inference mean as a data threat?",
     "ماذا يعني الاستنتاج كتهديد للبيانات؟",
     ["Deducing secret information from data that is public.",
      "Copying a file onto an unauthorised storage device.",
      "Encrypting a database and losing the only key for it.",
      "Deleting a record by accident during an update."],
     ["استنتاج معلومات سرية من بيانات متاحة للجميع.",
      "نسخ ملف إلى وسيط تخزين غير مصرّح به للاستخدام.",
      "تشفير قاعدة بيانات وفقدان المفتاح الوحيد.",
      "حذف سجل بالخطأ أثناء عملية تحديث قاعدة البيانات."],
     "Inference is collecting accessible data and deducing confidential information that was never directly available.",
     "الاستنتاج هو جمع بيانات متاحة واستنتاج معلومات سرية لم تكن متاحة مباشرة."),

    # 6 -------------------------------------------------------------------
    ("masquerading_meaning", "Remember",
     "What does masquerading mean?",
     "ماذا يعني التنكّر؟",
     ["Pretending to be someone else to gain access.",
      "Hiding data inside another file before sending it.",
      "Changing a record so the change cannot be seen.",
      "Blocking a service so that nobody can use it."],
     ["التظاهر بأنك شخص آخر للوصول إلى النظام.",
      "إخفاء بيانات داخل ملف آخر قبل إرساله للضحية.",
      "تغيير سجل بحيث لا يظهر التغيير عليه.",
      "حجب خدمة بحيث لا يستطيع أحد استخدامها."],
     "Masquerading is pretending to be someone else, and the lecture lists it under data threats next to unauthorized access.",
     "التنكّر هو التظاهر بأنك شخص آخر، والمحاضرة تدرجه تحت تهديدات البيانات بجانب الوصول غير المصرّح."),

    # 7 -------------------------------------------------------------------
    ("classify_storm", "Apply",
     "A storm floods the room holding the servers. Which group does the lecture place this in?",
     "عاصفة تُغرق الغرفة التي فيها الخوادم. في أي مجموعة تضعها المحاضرة؟",
     ["Hardware, because it acts physically on the machine.",
      "Software, because it stops the programs from running.",
      "Data, because the records on the disks are lost.",
      "Liveware, because nobody checked the weather report."],
     ["العتاد، لأنه يؤثر مادياً على الجهاز نفسه.",
      "البرمجيات، لأنه يوقف البرامج عن العمل.",
      "البيانات، لأن السجلات على الأقراص تضيع.",
      "العامل البشري، لأن أحداً لم يتابع حالة الطقس."],
     "The lecture names natural disasters such as storms under hardware threats, because the damage is physical to the machine or its surroundings.",
     "المحاضرة تذكر الكوارث الطبيعية كالعواصف تحت تهديدات العتاد، لأن الضرر مادي على الجهاز أو محيطه."),

    # 8 -------------------------------------------------------------------
    ("classify_cleaner", "Analyze",
     "A cleaner unplugs a server to vacuum behind it. Which group fits best?",
     "عامل تنظيف يفصل الخادم عن الكهرباء ليكنس خلفه. أي مجموعة تناسب أكثر؟",
     ["Liveware, because a person made the error.",
      "Hardware, because the server was the object.",
      "Software, because the machine shut down uncleanly.",
      "Data, because the records were left unreadable."],
     ["العامل البشري، لأن شخصاً ارتكب الخطأ.",
      "العتاد، لأن الخادم كان الشيء المتأثر.",
      "البرمجيات، لأن الجهاز أُطفئ بشكل غير سليم.",
      "البيانات، لأن السجلات بقيت غير قابلة للقراءة."],
     "Liveware covers human error by the system's own users. The server is only the object; the cause is a person's mistake.",
     "العامل البشري يغطي الخطأ البشري من مستخدمي النظام أنفسهم. الخادم مجرد شيء متأثر، والسبب خطأ شخص."),

    # 9 -------------------------------------------------------------------
    ("cm_malware", "Understand",
     "Which countermeasure does the lecture pair with threats from malware?",
     "أي تدبير مضاد تقرنه المحاضرة بتهديدات البرمجيات الخبيثة؟",
     ["Antivirus and security programs.",
      "Firewalls placed in the network.",
      "Regular backup copies of the data.",
      "A secure room for the equipment."],
     ["برامج مكافحة الفيروسات والبرامج الأمنية.",
      "جدران الحماية المثبتة داخل الشبكة نفسها.",
      "نسخ احتياطية منتظمة تُؤخذ من البيانات.",
      "غرفة آمنة تُوضع فيها المعدات كلها معاً."],
     "Malware is answered by antivirus together with the other security programs, because the threat is inside the machine rather than at the network edge.",
     "البرمجيات الخبيثة يُجاب عليها بمكافحة الفيروسات مع البرامج الأمنية الأخرى، لأن التهديد داخل الجهاز لا عند حدود الشبكة."),

    # 10 ------------------------------------------------------------------
    ("cm_physical_damage", "Understand",
     "Which countermeasure does the lecture pair with vandalism, theft, and physical damage?",
     "أي تدبير مضاد تقرنه المحاضرة بالتخريب والسرقة والضرر المادي؟",
     ["Place the equipment in a secure room.",
      "Take regular backup copies of data.",
      "Use encryption and access control on it.",
      "Check the personnel and train them."],
     ["وضع المعدات في غرفة آمنة.",
      "أخذ نسخ احتياطية منتظمة.",
      "استخدام التشفير وضبط الوصول.",
      "فحص الموظفين وتدريبهم."],
     "Physical threats are answered physically: the equipment goes into a secure room. Software controls cannot stop someone carrying a machine away.",
     "التهديدات المادية يُجاب عليها مادياً: توضع المعدات في غرفة آمنة. وضوابط البرمجيات لا تمنع أحداً من حمل الجهاز."),

    # 11 ------------------------------------------------------------------
    ("cm_unauthorized_modification", "Understand",
     "Which countermeasure does the lecture pair with unauthorized modification or deletion?",
     "أي تدبير مضاد تقرنه المحاضرة بالتعديل أو الحذف غير المصرّح به؟",
     ["Take regular backup copies of the data.",
      "Use encryption or access control on it.",
      "Place the equipment in a secure room.",
      "Check the personnel and give them training."],
     ["أخذ نسخ احتياطية منتظمة من البيانات.",
      "استخدام التشفير أو التحكم بالوصول إليها.",
      "وضع المعدات كلها في غرفة آمنة.",
      "فحص الموظفين وتدريبهم بشكل مناسب."],
     "Backups answer modification and deletion, because the point is to restore the earlier state. Encryption would not bring a deleted record back.",
     "النسخ الاحتياطية تجيب على التعديل والحذف، لأن الهدف استعادة الحالة السابقة. والتشفير لا يُعيد سجلاً محذوفاً."),

    # 12 ------------------------------------------------------------------
    ("countermeasure_adaptation", "Understand",
     "Why must a countermeasure suit the type of threat?",
     "لماذا يجب أن يناسب التدبير المضاد نوع التهديد؟",
     ["Because each threat needs a matching control.",
      "Because one strong control covers every threat.",
      "Because countermeasures must be cheap first.",
      "Because the policy requires a fixed list."],
     ["لأن كل تهديد يحتاج ضابطاً يناسبه.",
      "لأن ضابطاً قوياً واحداً يكفي لكل تهديد.",
      "لأن الضوابط يجب أن تكون رخيصة أولاً.",
      "لأن السياسة تفرض قائمة ثابتة."],
     "The lecture says countermeasures must be adapted to suit the type of threat, which is why the list pairs a different control with each threat.",
     "المحاضرة تقول إن التدابير المضادة يجب أن تُكيَّف بما يناسب نوع التهديد، ولهذا تقرن القائمة ضابطاً مختلفاً بكل تهديد."),
]

KEY = "ABCDACBDABCD"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
