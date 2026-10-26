#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch01 T03 — CIA triad, its technique lists, and the security utility function."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch01_lib import build

QUIZ = "Quiz_Ch01_T03_CIA_Triad_and_Utility_Function"
TOPIC_EN = "The CIA Triad, Technique Lists & Utility Weights"
TOPIC_AR = "ثالوث CIA وقوائم التقنيات وأوزان المنفعة"

I = [
    # 1 -------------------------------------------------------------------
    ("cia_triad_is_backbone", "Remember",
     "Which model is the backbone of cybersecurity?",
     "أي نموذج هو العمود الفقري للأمن السيبراني؟",
     ["The CIA triad.", "The OSI model.", "The TCP stack.", "The NIST model."],
     ["ثالوث CIA.", "نموذج OSI.", "حزمة TCP.", "نموذج NIST."],
     "The CIA triad is the backbone of cybersecurity: every control serves one of its three pillars.",
     "ثالوث CIA هو العمود الفقري للأمن السيبراني: كل ضابط يخدم أحد أركانه الثلاثة."),

    # 2 -------------------------------------------------------------------
    ("cia_confidentiality_definition", "Remember",
     "What does confidentiality protect data against?",
     "ماذا تحمي السرية البيانات منه؟",
     ["Unauthorised reading or disclosure.",
      "Unauthorised change or deletion of the record.",
      "Loss of access when it is needed.",
      "Loss of accuracy during transfer."],
     ["القراءة أو الكشف غير المصرّح به.",
      "التغيير أو الحذف غير المصرّح به.",
      "فقدان الوصول إلى البيانات عند الحاجة.",
      "فقدان دقة البيانات أثناء النقل."],
     "Confidentiality is about preventing unauthorised access, which means stopping people from reading or disclosing data they should not see.",
     "السرية تخص منع الوصول غير المصرّح به، أي منع الأشخاص من قراءة أو كشف بيانات لا يحق لهم رؤيتها."),

    # 3 -------------------------------------------------------------------
    ("cia_integrity_definition", "Remember",
     "What does integrity guarantee about data?",
     "ماذا تضمن السلامة بشأن البيانات؟",
     ["That it is accurate, complete, and unaltered.",
      "That it is hidden from unauthorised readers.",
      "That it is reachable whenever it is actually needed.",
      "That it is stored in more than one place."],
     ["أنها دقيقة وكاملة وغير معدّلة.",
      "أنها مخفية عن القارئ غير المصرّح به.",
      "أنها متاحة كلما احتاجها المستخدم.",
      "أنها محفوظة في أكثر من مكان واحد."],
     "Integrity means the data stays accurate and unaltered, with nothing added, removed, or changed behind your back.",
     "السلامة تعني أن البيانات تبقى دقيقة وغير معدّلة، دون إضافة أو حذف أو تغيير يجري من دون علمك."),

    # 4 -------------------------------------------------------------------
    ("cia_availability_definition", "Remember",
     "What does availability guarantee?",
     "ماذا يضمن التوافر؟",
     ["That resources are accessible whenever they are needed.",
      "That resources are always encrypted before they are stored.",
      "That resources are audited after every single change.",
      "That resources are backed up to a second location."],
     ["أن الموارد متاحة كلما دعت الحاجة إليها.",
      "أن الموارد مشفّرة قبل أن تُخزَّن.",
      "أن الموارد تُدقَّق بعد كل تغيير يجري عليها.",
      "أن الموارد منسوخة إلى موقع ثانٍ."],
     "Availability is about access when needed. Backups and encryption are means, not the guarantee itself.",
     "التوافر يخص الوصول عند الحاجة. النسخ الاحتياطي والتشفير وسائل وليست الضمان نفسه."),

    # 5 -------------------------------------------------------------------
    ("cia_confidentiality_techniques", "Remember",
     "Which techniques enforce confidentiality?",
     "أي تقنيات تحقق السرية؟",
     ["Encryption, access controls, and VPN tunnels.",
      "Hashing, digital signatures, and version control.",
      "Redundancy, load balancing, and DDoS mitigation.",
      "Firewalls, IDS/IPS, and network segmentation."],
     ["التشفير وضوابط الوصول والشبكات الخاصة الافتراضية.",
      "التجزئة والتواقيع الرقمية والتحكم بالإصدارات.",
      "التكرار وموازنة الحمل والتخفيف من هجمات الحجب.",
      "الجدران النارية وكشف التطفل وتقسيم الشبكة."],
     "Confidentiality is served by encryption, access controls, and VPNs. These three are the vocabulary you write in the parentheses of a scenario answer.",
     "السرية تُخدم بالتشفير وضوابط الوصول والشبكات الخاصة الافتراضية. هذه الثلاثة هي المفردات التي تكتبها بين القوسين في جواب السيناريو."),

    # 6 -------------------------------------------------------------------
    ("cia_integrity_techniques", "Remember",
     "Which techniques enforce integrity?",
     "أي تقنيات تحقق السلامة؟",
     ["Hashing, digital signatures, and version control.",
      "Encryption, access controls, and VPN tunnels.",
      "Redundancy, load balancing, and DDoS mitigation.",
      "Patching, hardening, and routine vulnerability scanning."],
     ["التجزئة والتواقيع الرقمية والتحكم بالإصدارات.",
      "التشفير وضوابط الوصول والشبكات الخاصة الافتراضية.",
      "التكرار وموازنة الحمل والتخفيف من هجمات الحجب.",
      "التحديث والتحصين وفحص الثغرات الأمنية."],
     "Integrity uses hashing, digital signatures, and version control. Hashing is the one named with its algorithm, SHA-256.",
     "السلامة تستخدم التجزئة والتواقيع الرقمية والتحكم بالإصدارات. والتجزئة هي المقترنة بخوارزميتها SHA-256."),

    # 7 -------------------------------------------------------------------
    ("cia_availability_techniques", "Remember",
     "Which techniques enforce availability?",
     "أي تقنيات تحقق التوافر؟",
     ["Redundancy, load balancing, and DDoS mitigation.",
      "Encryption, access controls, and VPN tunnels.",
      "Hashing, digital signatures, and version control.",
      "Patching, hardening, and routine vulnerability scanning."],
     ["التكرار وموازنة الحمل والتخفيف من هجمات الحجب.",
      "التشفير وضوابط الوصول والشبكات الخاصة الافتراضية.",
      "التجزئة والتواقيع الرقمية والتحكم بالإصدارات.",
      "التحديث والتحصين وفحص الثغرات الأمنية."],
     "Availability is served by redundancy, load balancing, and DDoS mitigation, because each one keeps the service reachable.",
     "التوافر يُخدم بالتكرار وموازنة الحمل والتخفيف من هجمات الحجب، لأن كل واحدة منها تُبقي الخدمة قابلة للوصول."),

    # 8 -------------------------------------------------------------------
    ("cia_scenario_leak", "Apply",
     "A customer database is copied and published online. Which pillar is broken?",
     "قاعدة بيانات العملاء نُسخت ونُشرت على الإنترنت. أي ركن انكسر؟",
     ["Confidentiality is the pillar involved here.",
      "Integrity is the main pillar involved here.",
      "Availability is the pillar involved here.",
      "Authorisation is the pillar involved here."],
     ["السرية هي الركن المعني في هذه الحالة.",
      "السلامة هي الركن المعني في هذه الحالة.",
      "التوافر هو الركن المعني في هذه الحالة.",
      "التخويل هو الركن المعني في هذه الحالة."],
     "The data was read by people who should not have seen it, so confidentiality is broken. Nothing was altered and nothing went offline.",
     "البيانات قرأها أشخاص لا يحق لهم رؤيتها، فالسرية هي المنكسرة. لم يُعدَّل شيء ولم تتوقف خدمة."),

    # 9 -------------------------------------------------------------------
    ("cia_scenario_outage", "Apply",
     "A traffic flood makes a website unreachable for six hours. Which pillar is broken?",
     "هجوم حجب يجعل موقعاً غير قابل للوصول ست ساعات. أي ركن انكسر؟",
     ["Availability is the pillar involved here.",
      "Confidentiality is the pillar involved here.",
      "Integrity is the main pillar involved here.",
      "Authorisation is the pillar involved here."],
     ["التوافر هو الركن المعني في هذه الحالة.",
      "السرية هي الركن المعني في هذه الحالة.",
      "السلامة هي الركن المعني في هذه الحالة.",
      "التخويل هو الركن المعني في هذه الحالة."],
     "The resource stopped being reachable when it was needed, so availability is broken. The answer names DDoS mitigation as the control.",
     "المورد توقف عن أن يكون متاحاً عند الحاجة، فالتوافر هو المنكسر. والجواب يذكر التخفيف من هجمات الحجب كضابط."),

    # 10 ------------------------------------------------------------------
    ("cia_scenario_bank_balance", "Apply",
     "A balance drops by 100,000, the bank finds a program error, fixes it and restores the money. Which two pillars are involved, in order?",
     "رصيد ينخفض 100,000، فيكتشف المصرف خطأ برمجياً ويصلحه ويعيد المال. أي ركنين يتدخلان، بالترتيب؟",
     ["Integrity, then availability.",
      "Availability, then integrity.",
      "Confidentiality, then integrity.",
      "Integrity, then confidentiality."],
     ["السلامة ثم التوافر.",
      "التوافر ثم السلامة.",
      "السرية ثم السلامة.",
      "السلامة ثم السرية."],
     "First the record was altered, which is integrity. Then the service had to be corrected and restored, which is availability.",
     "أولاً تغيّر السجل، وهذه السلامة. ثم وجب تصحيح الخدمة واستعادتها، وهذا التوافر."),

    # 11 ------------------------------------------------------------------
    ("utility_function_weights", "Remember",
     "In the security utility function, what do the three weights represent?",
     "في دالة المنفعة الأمنية، ماذا تمثّل الأوزان الثلاثة؟",
     ["How much each pillar matters to that system.",
      "How much each control costs the company to operate.",
      "How often each pillar fails in practice.",
      "How many users each pillar serves directly."],
     ["مقدار أهمية كل ركن في ذلك النظام.",
      "تكلفة تشغيل كل ضابط أمني على حدة.",
      "عدد مرات فشل كل ركن عملياً.",
      "عدد المستخدمين الذين يخدمهم كل ركن."],
     "The weights are importance weights for a particular system, not costs or failure rates. They are what makes the same triad score differently in different domains.",
     "الأوزان هي أوزان أهمية لنظام معيّن، وليست تكاليف أو نسب فشل. وهي التي تجعل الثالوث نفسه يعطي درجة مختلفة في كل مجال."),

    # 12 ------------------------------------------------------------------
    ("utility_weight_healthcare_alpha", "Analyze",
     "Why does a hospital system weight confidentiality above availability?",
     "لماذا يرجّح نظام مستشفى السرية على التوافر؟",
     ["A leaked patient record causes permanent harm that cannot be undone.",
      "Hospital systems are usually offline, so uptime does not matter.",
      "Medical law forbids the use of any encryption on patient data.",
      "Doctors rarely need to open any patient records during working hours."],
     ["تسريب سجل المريض يسبب ضرراً دائماً لا يمكن إصلاحه.",
      "أنظمة المستشفى غالباً غير متصلة، فالاستمرارية لا تهم.",
      "القانون الطبي يمنع استخدام التشفير على بيانات المرضى.",
      "الأطباء نادراً ما يحتاجون فتح السجلات في الدوام."],
     "In healthcare confidentiality carries more weight: a disclosed diagnosis can never be taken back, while an outage can be repaired.",
     "في الرعاية الصحية وزن السرية أعلى: التشخيص المكشوف لا يمكن سحبه، بينما الانقطاع يمكن إصلاحه."),

    # 13 ------------------------------------------------------------------
    ("utility_weight_banking_beta", "Analyze",
     "Why does a core banking system weight integrity above the other two?",
     "لماذا يرجّح نظام مصرفي أساسي السلامة على الركنين الآخرين؟",
     ["An altered ledger corrupts balances and causes immediate loss.",
      "Banks do not need availability because they close at night.",
      "Confidentiality matters less because accounts are public.",
      "Hashing is simply not available to the banking software vendors."],
     ["تعديل السجل يفسد الأرصدة ويسبب خسارة فورية.",
      "المصارف لا تحتاج التوافر لأنها تغلق ليلاً.",
      "السرية أقل أهمية لأن الحسابات معلنة للجميع.",
      "دوال التجزئة غير متاحة لمورّدي برامج المصارف."],
     "Money is a record, so a changed record is a changed balance. Integrity therefore dominates in banking the way confidentiality dominates in healthcare.",
     "المال سجل، فتغيير السجل تغيير للرصيد. لذلك تسيطر السلامة في المصارف كما تسيطر السرية في الرعاية الصحية."),

    # 14 ------------------------------------------------------------------
    ("utility_function_purpose", "Understand",
     "What does the utility function add beyond naming the three pillars?",
     "ماذا تضيف دالة المنفعة على مجرد تسمية الأركان الثلاثة؟",
     ["It lets each system weight the pillars differently.",
      "It replaces the three separate pillars with a single score.",
      "It proves the three pillars always weigh the same.",
      "It removes the need to measure each pillar."],
     ["يسمح لكل نظام بترجيح الأركان بدرجات مختلفة.",
      "يستبدل الأركان الثلاثة بدرجة واحدة مجمّعة.",
      "يثبت أن الأركان الثلاثة متساوية الوزن دائماً.",
      "يلغي الحاجة إلى قياس كل ركن على حدة."],
     "The triad says what to protect. The function says how much each part counts for a given system, which is why the weights change by domain.",
     "الثالوث يقول ماذا نحمي. والدالة تقول كم يهمّ كل جزء في نظام معيّن، ولهذا تتغيّر الأوزان بحسب المجال."),
]

KEY = "ACBDABDCBACDAB"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
