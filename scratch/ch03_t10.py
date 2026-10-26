#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch03 T10 — Modern policy trends: Zero Trust, AI auditing, ESG."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch03_lib import build

QUIZ = "Quiz_Ch03_T10_Modern_Trends"
TOPIC_EN = "Modern Trends: Zero Trust, AI Auditing, ESG"
TOPIC_AR = "الاتجاهات الحديثة: الثقة الصفرية والذكاء وESG"

I = [
    # 1 -------------------------------------------------------------------
    ("zero_trust_slogan", "Remember",
     "Which slogan captures the Zero Trust policy?",
     "أي شعار يلخّص سياسة الثقة الصفرية؟",
     ["Never Trust, Always Verify.", "Trust but verify everything.",
      "Trust the internal network.", "Verify once, then trust."],
     ["لا تثق أبداً، تحقّق دائماً.", "ثق لكن تحقّق من كل شيء دائماً.",
      "ثق بالشبكة الداخلية دائماً.", "تحقّق مرة واحدة ثم ثق دائماً."],
     "Never Trust, Always Verify. Trust is never granted by location, only by verification.",
     "لا تثق أبداً، تحقّق دائماً. الثقة لا تُمنح بالمكان بل بالتحقق."),

    # 2 -------------------------------------------------------------------
    ("zero_trust_rejects", "Understand",
     "What assumption does Zero Trust reject?",
     "أي افتراض ترفضه الثقة الصفرية؟",
     ["The idea that being inside means trusted.",
      "The need for any authentication at all.",
      "The use of encryption on the network here.",
      "The role of least privilege in policy."],
     ["فكرة أن الوجود بالداخل يعني الثقة.",
      "الحاجة إلى أي مصادقة إطلاقاً هنا.",
      "استخدام التشفير على الشبكة هنا.",
      "دور الامتياز الأدنى في السياسة."],
     "Perimeter security assumed that inside means trusted. Zero Trust rejects exactly that, which is why the perimeter stops being the boundary.",
     "أمن المحيط افترض أن الداخل موثوق. والثقة الصفرية ترفض ذلك بالضبط، ولهذا يتوقف المحيط عن كونه الحدّ."),

    # 3 -------------------------------------------------------------------
    ("continuous_verification", "Remember",
     "What happens to every access request?",
     "ماذا يحدث لكل طلب وصول؟",
     ["Every request is verified continuously.",
      "Every request is trusted once it is inside.",
      "Every request is logged and nothing more.",
      "Every request is approved by a manager."],
     ["كل طلب يُتحقَّق منه باستمرار.",
      "كل طلب يُوثَق به بعد الدخول.",
      "كل طلب يُسجَّل ولا شيء أكثر.",
      "كل طلب يوافق عليه مدير مسؤول."],
     "Every access request is verified continuously, not once at the door.",
     "كل طلب وصول يُتحقَّق منه باستمرار، لا مرة واحدة عند الباب."),

    # 4 -------------------------------------------------------------------
    ("three_actions", "Remember",
     "Which three things happen to every user, device and request?",
     "أي ثلاثة أمور تحدث لكل مستخدم وجهاز وطلب؟",
     ["Authenticated, authorised, and encrypted.",
      "Logged, archived, and then securely deleted.",
      "Approved, budgeted, and scheduled.",
      "Encrypted, compressed, and stored."],
     ["مصادَق عليه ومصرّح به ومشفّر.",
      "مسجَّل ومؤرشف ثم محذوف نهائياً.",
      "موافَق عليه ومسعَّر ومجدول.",
      "مشفّر ومضغوط ومخزَّن هنا."],
     "Every user, device and request is authenticated, authorized and encrypted. All three, every time.",
     "كل مستخدم وجهاز وطلب يُصادَق عليه ويُصرَّح به ويُشفَّر. الثلاثة، في كل مرة."),

    # 5 -------------------------------------------------------------------
    ("dynamic_least_privilege", "Understand",
     "How does Zero Trust handle least privilege?",
     "كيف تتعامل الثقة الصفرية مع الامتياز الأدنى؟",
     ["It is enforced dynamically, per request.",
      "It is written once in the policy document.",
      "It is granted to the whole department.",
      "It is reviewed once every five years."],
     ["يُفرَض ديناميكياً لكل طلب.",
      "يُكتب مرة واحدة في السياسة.",
      "يُمنح للقسم بأكمله هنا.",
      "يُراجَع مرة كل خمس سنوات."],
     "Least privilege is enforced dynamically, so the permissions follow the request rather than the person's job title.",
     "الامتياز الأدنى يُفرَض ديناميكياً، فالصلاحيات تتبع الطلب لا المسمّى الوظيفي."),

    # 6 -------------------------------------------------------------------
    ("reauthentication_example", "Remember",
     "What does the Zero Trust example require?",
     "ماذا يشترط مثال الثقة الصفرية؟",
     ["Sensitive transactions need re-authentication.",
      "Staff sign in once at the start of the day.",
      "Managers approve each transaction manually.",
      "The internal network is trusted by default here."],
     ["العمليات الحساسة تحتاج تحققاً جديداً.",
      "الموظفون يسجّلون الدخول مرة في الصباح.",
      "المديرون يوافقون على كل عملية.",
      "الشبكة الداخلية موثوقة افتراضياً."],
     "A sensitive transaction demands re-authentication even when the person is already inside the corporate network.",
     "العملية الحساسة تفرض تحققاً جديداً حتى لو كان الشخص داخل شبكة المؤسسة أصلاً."),

    # 7 -------------------------------------------------------------------
    ("manual_audit_problem", "Understand",
     "What is wrong with manual compliance audits?",
     "ما مشكلة التدقيق اليدوي على الامتثال؟",
     ["They are resource-intensive and error-prone.",
      "They are cheap and always completely accurate.",
      "They run continuously without any staff.",
      "They replace the need for any policy."],
     ["مكلفة بالموارد ومعرّضة للخطأ.",
      "رخيصة ودقيقة تماماً دائماً.",
      "تعمل باستمرار دون أي موظفين.",
      "تغني عن الحاجة إلى أي سياسة هنا."],
     "Manual audits are resource-intensive and error-prone, which is exactly the gap AI-driven auditing is sold to fill.",
     "التدقيق اليدوي مكلف بالموارد ومعرّض للخطأ، وهذا بالضبط الفراغ الذي يُطرح التدقيق بالذكاء لملئه."),

    # 8 -------------------------------------------------------------------
    ("ai_monitors_logs", "Remember",
     "What do AI auditing tools do with the logs?",
     "ماذا تفعل أدوات التدقيق بالذكاء بالسجلات؟",
     ["They monitor logs and flag non-compliance.",
      "They replace the raw logs with dashboards.",
      "They audit once at the end of the year.",
      "They delete the logs after each audit."],
     ["تراقب السجلات وترصد عدم الامتثال.",
      "تستبدل السجلات الخام بلوحات معلومات.",
      "تدقّق مرة واحدة في نهاية السنة هنا.",
      "تحذف السجلات بعد كل تدقيق أمني."],
     "They monitor the logs and detect non-compliant behaviour in real time, rather than reconstructing it months later.",
     "تراقب السجلات وترصد السلوك غير الممتثل في الوقت الحقيقي، بدل إعادة بنائه بعد أشهر."),

    # 9 -------------------------------------------------------------------
    ("ai_maps_gaps", "Remember",
     "Which standards do AI tools map compliance gaps against?",
     "بأي معايير تربط أدوات الذكاء فجوات الامتثال؟",
     ["They map gaps against ISO 27001 and NIST CSF.",
      "They map gaps against the marketing plan.",
      "They map gaps against last year's budget.",
      "They map gaps against the current staff roster."],
     ["تربط الفجوات بمعايير ISO 27001 و NIST CSF.",
      "تربط الفجوات بخطة التسويق السنوية هنا تماماً.",
      "تربط الفجوات بميزانية العام الماضي هنا.",
      "تربط الفجوات بكشف الموظفين الحالي هنا."],
     "They map the gaps automatically against ISO 27001 and the NIST CSF, so the mapping no longer waits for a consultant.",
     "تربط الفجوات تلقائياً بمعيار ISO 27001 وإطار NIST CSF، فلم يعد الربط ينتظر مستشاراً."),

    # 10 ------------------------------------------------------------------
    ("ai_predicts_risk", "Understand",
     "How do AI tools predict risk?",
     "كيف تتوقع أدوات الذكاء الخطر؟",
     ["By correlating violations with attack likelihood.",
      "By asking each department for its own risk forecast.",
      "By reading the annual audit report only here.",
      "By counting how many policies exist here."],
     ["بربط المخالفات باحتمال الهجوم.",
      "بسؤال كل قسم عن توقعه الخاص.",
      "بقراءة تقرير التدقيق السنوي فقط.",
      "بعدّ عدد السياسات الموجودة."],
     "They predict risk by correlating policy violations with the likelihood of an attack, which turns a violation into a probability.",
     "تتوقع الخطر بربط المخالفات باحتمال الهجوم، فتحوّل المخالفة إلى احتمال."),

    # 11 ------------------------------------------------------------------
    ("ai_keeps_policies_live", "Understand",
     "What does AI-driven compliance actually achieve?",
     "ماذا يحققه التدقيق بالذكاء فعلاً؟",
     ["Policies stay actively enforced, not just written.",
      "Policies are written once and then archived here for good.",
      "Policies no longer need any human review at all.",
      "Policies become optional for all of the staff."],
     ["تبقى السياسات مفروضة فعلياً لا مكتوبة فقط.",
      "تُكتب السياسات مرة واحدة ثم تُؤرشف هنا تماماً.",
      "لم تعد السياسات تحتاج أي مراجعة بشرية.",
      "تصبح السياسات اختيارية لكل الموظفين."],
     "It reduces human workload and keeps policies actively enforced instead of merely written, which is the whole point of monitoring.",
     "يقلّل عبء العمل البشري ويُبقي السياسات مفروضة فعلياً لا مكتوبة فقط، وهذا هو مغزى المراقبة."),

    # 12 ------------------------------------------------------------------
    ("esg_mapping", "Remember",
     "How does cybersecurity map onto the three ESG pillars?",
     "كيف يرتبط الأمن السيبراني بأركان ESG الثلاثة؟",
     ["Governance ethics, social trust, environmental IT.",
      "Governance budgets, social events, environmental PR.",
      "Governance audits, social media, environmental law.",
      "Governance policy, social training, environmental tax."],
     ["حوكمة أخلاقية وثقة اجتماعية وتقنية بيئية.",
      "ميزانيات حوكمة وفعاليات اجتماعية وعلاقات.",
      "تدقيق حوكمة وتواصل اجتماعي وقانون بيئي.",
      "سياسة حوكمة وتدريب اجتماعي وضريبة بيئية."],
     "Governance covers the ethical handling of data, Social covers customer trust and employee privacy, Environmental covers sustainable IT such as green data centres.",
     "الحوكمة تغطي التعامل الأخلاقي مع البيانات، والاجتماعي يغطي ثقة العملاء وخصوصية الموظفين، والبيئي يغطي تقنية مستدامة كمراكز البيانات الخضراء."),
]

KEY = "ABCDABCDABCD"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
