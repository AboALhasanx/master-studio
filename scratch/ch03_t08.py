#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch03 T08 — Why policy fails in practice, and the five-step lifecycle."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch03_lib import build

QUIZ = "Quiz_Ch03_T08_Policy_Challenges_And_Lifecycle"
TOPIC_EN = "Policy Challenges & the Five-Step Lifecycle"
TOPIC_AR = "تحديات السياسة ودورتها الخماسية"

I = [
    # 1 -------------------------------------------------------------------
    ("write_vs_enforce", "Understand",
     "What is the real challenge with security policies?",
     "ما التحدي الحقيقي في سياسات الأمن؟",
     ["Writing is easy; enforcing and maintaining is hard.",
      "Writing is hard, and enforcing it is almost trivial.",
      "Both writing and enforcing are equally easy.",
      "Neither writing nor enforcing is possible at all."],
     ["الكتابة سهلة، والفرض والصيانة هما التحدي.",
      "الكتابة صعبة جداً، والفرض سهل جداً هنا.",
      "الكتابة والفرض كلاهما سهل بالقدر نفسه.",
      "لا الكتابة ولا الفرض ممكنان إطلاقاً."],
     "Writing a policy is straightforward. Enforcing it and keeping it alive across an organization is the real challenge.",
     "كتابة السياسة أمر مباشر. أما فرضها وإبقاؤها حيّة في المؤسسة فهو التحدي الحقيقي."),

    # 2 -------------------------------------------------------------------
    ("user_resistance", "Remember",
     "Why do employees resist a security policy?",
     "لماذا يقاوم الموظفون سياسة الأمن؟",
     ["They see policies as a burden on convenience.",
      "They disagree with the technical controls.",
      "They were never told the policy even exists.",
      "They are usually the ones who wrote it themselves."],
     ["يرون السياسات عبئاً على الراحة.",
      "يختلفون مع الضوابط التقنية المطلوبة.",
      "لم يُبلَّغوا بوجود السياسة أصلاً.",
      "هم عادةً من كتب السياسة بأنفسهم."],
     "Employees read a policy as a burden, especially when it costs convenience, such as frequent password changes.",
     "الموظفون يقرؤون السياسة كعبء، خصوصاً حين تكلّفهم راحة، كتغيير كلمات المرور المتكرر."),

    # 3 -------------------------------------------------------------------
    ("resistance_grows", "Understand",
     "When does that resistance grow?",
     "متى تزداد تلك المقاومة؟",
     ["Convenience drops without the benefits explained.",
      "The policy is written in English only here still.",
      "The policy is longer than ten printed pages.",
      "The training session was optional for staff."],
     ["تنقص الراحة دون توضيح الفوائد.",
      "السياسة مكتوبة بالإنجليزية فقط.",
      "السياسة أطول من عشر صفحات.",
      "جلسة التدريب كانت اختيارية."],
     "Resistance grows when a policy reduces convenience without a clear explanation of what the benefit is.",
     "المقاومة تزداد حين تقلّل السياسة الراحة دون توضيح واضح للفائدة."),

    # 4 -------------------------------------------------------------------
    ("lack_of_enforcement", "Understand",
     "Why do well-written policies still fail?",
     "لماذا تفشل السياسات الجيدة الكتابة رغم ذلك؟",
     ["Weak monitoring and no executive backing.",
      "Too many policies written at the same time.",
      "Policies that are too short to be followed.",
      "Staff who never read the policy at all."],
     ["رقابة ضعيفة ولا دعم تنفيذي.",
      "سياسات كثيرة تُكتب دفعة واحدة.",
      "سياسات قصيرة جداً لا تُتبَع.",
      "موظفون لا يقرؤون السياسة."],
     "Many organizations hold well-written policies that are simply not enforced, because monitoring is weak and executives do not back them.",
     "مؤسسات كثيرة تحمل سياسات مكتوبة جيداً لكنها غير مفروضة، لأن الرقابة ضعيفة والتنفيذيون لا يدعمونها."),

    # 5 -------------------------------------------------------------------
    ("outdated_policy", "Remember",
     "Which example shows a policy going out of date?",
     "أي مثال يوضّح سياسة صارت قديمة؟",
     ["An AUP written before cloud and personal devices.",
      "An AUP that is longer than the audit report.",
      "An AUP signed by the chief executive only.",
      "An AUP translated into three different foreign languages."],
     ["سياسة استخدام كُتبت قبل السحابة والأجهزة.",
      "سياسة استخدام أطول من تقرير التدقيق.",
      "سياسة استخدام وقّعها المدير التنفيذي فقط.",
      "سياسة استخدام مترجمة لثلاث لغات أجنبية."],
     "An acceptable-use policy written before cloud services and personal devices existed cannot address the risks those bring.",
     "سياسة استخدام كُتبت قبل وجود الخدمات السحابية والأجهزة الشخصية لا تستطيع معالجة المخاطر التي تجلبها."),

    # 6 -------------------------------------------------------------------
    ("cultural_barrier", "Remember",
     "What is the cultural barrier described?",
     "ما الحاجز الثقافي الموصوف؟",
     ["Security is treated as IT's job, not everyone's.",
      "Security is treated as the board's only job.",
      "Security is treated as the auditor's own job.",
      "Security is treated as a temporary project here."],
     ["يُعامَل الأمن كوظيفة التقنية لا الجميع.",
      "يُعامَل الأمن كوظيفة المجلس وحده هنا.",
      "يُعامَل الأمن كوظيفة المدقق وحده هنا.",
      "يُعامَل الأمن كمشروع مؤقت عابر هنا."],
     "In organizations with legacy IT practice, employees treat security as the IT department's job rather than a shared responsibility.",
     "في المؤسسات ذات الممارسات التقنية القديمة، يعامل الموظفون الأمن كوظيفة قسم التقنية لا كمسؤولية مشتركة."),

    # 7 -------------------------------------------------------------------
    ("enforcement_lesson", "Remember",
     "What does the lesson require of enforcement?",
     "ماذا يشترط الدرس من الفرض؟",
     ["Enforcement must be practical, consistent, updated.",
      "Enforcement must be strict and without any review.",
      "Enforcement should be left to the IT team alone.",
      "Enforcement is optional if the policy is good enough."],
     ["الفرض يجب أن يكون عملياً وثابتاً ومحدّثاً.",
      "الفرض يجب أن يكون صارماً بلا أي مراجعة.",
      "الفرض يُترك لفريق التقنية وحده هنا تماماً.",
      "الفرض اختياري إذا كانت السياسة جيدة."],
     "Enforcement has to be practical, consistent, and continuously updated. Anything else decays back into a document nobody follows.",
     "الفرض يجب أن يكون عملياً وثابتاً ومحدَّثاً باستمرار. وما دون ذلك يتحوّل إلى وثيقة لا يتبعها أحد."),

    # 8 -------------------------------------------------------------------
    ("lifecycle_steps", "Remember",
     "Which five steps make up the policy lifecycle?",
     "أي خمس خطوات تشكّل دورة حياة السياسة؟",
     ["Draft, approve, communicate, enforce, review.",
      "Plan, do, check, act, and then retire it.",
      "Write, sign, publish, audit, and then archive.",
      "Draft, test, deploy, monitor, and rollback."],
     ["صياغة واعتماد وإبلاغ وفرض ومراجعة.",
      "تخطيط وتنفيذ وتحقق وتصحيح وإيقاف.",
      "كتابة وتوقيع ونشر وتدقيق وأرشفة.",
      "صياغة واختبار ونشر ومراقبة وتراجع."],
     "The lifecycle runs draft, approve, communicate, enforce, then review and update. A policy is not static.",
     "الدورة: صياغة، اعتماد، إبلاغ، فرض، ثم مراجعة وتحديث. فالسياسة ليست ثابتة."),

    # 9 -------------------------------------------------------------------
    ("step_draft", "Remember",
     "Where does the draft step start?",
     "من أين تبدأ خطوة الصياغة؟",
     ["It starts from the risk assessment findings.",
      "It starts from the board's annual budget.",
      "It starts from the auditor's own checklist.",
      "It starts from the vendor's ready-made template."],
     ["تبدأ من نتائج تقييم المخاطر.",
      "تبدأ من ميزانية المجلس السنوية.",
      "تبدأ من قائمة المدقق الجاهزة.",
      "تبدأ من قالب المورّد الجاهز."],
     "Drafting begins with the risks identified by the assessment frameworks, such as OCTAVE or NIST SP 800-30.",
     "الصياغة تبدأ من المخاطر التي تحددها أطر التقييم، مثل OCTAVE أو NIST SP 800-30."),

    # 10 ------------------------------------------------------------------
    ("step_approval", "Understand",
     "Why does the approval step need senior leadership?",
     "لماذا تحتاج خطوة الاعتماد القيادة العليا؟",
     ["Senior leadership endorsement, not optional.",
      "A simple majority vote by all the employees.",
      "A legal review by an outside law firm only.",
      "A technical review by the IT department alone."],
     ["تأييد القيادة العليا، فهو ليس اختيارياً.",
      "تصويت أغلبية بسيطة من جميع الموظفين.",
      "مراجعة قانونية من مكتب محاماة خارجي.",
      "مراجعة تقنية من قسم التقنية وحده هنا."],
     "Executive buy-in from the CIO, CISO or board is what makes a policy strategic rather than optional.",
     "تأييد القيادة التنفيذية من مدير المعلومات أو الأمن أو المجلس هو ما يجعل السياسة استراتيجية لا اختيارية."),

    # 11 ------------------------------------------------------------------
    ("step_communication", "Remember",
     "What does the communication step actually require?",
     "ماذا تشترط خطوة الإبلاغ فعلاً؟",
     ["Training that explains why the rules matter.",
      "Publishing the policy on the intranet only here.",
      "Sending one email to the managers only.",
      "Printing the policy and filing it away."],
     ["تدريب يشرح لماذا تهم القواعد فعلاً.",
      "نشر السياسة على الشبكة الداخلية فقط.",
      "إرسال بريد إلكتروني واحد للمديرين.",
      "طباعة السياسة وحفظها في ملف فقط."],
     "Training has to explain not only what the rules are but why they matter, which is why simulated phishing is used to make it concrete.",
     "التدريب يجب أن يشرح ليس فقط ما القواعد بل لماذا تهم، ولهذا تُستخدم حملات التصيّد المحاكاة لتجسيدها."),

    # 12 ------------------------------------------------------------------
    ("step_enforcement", "Remember",
     "What does the enforcement step involve?",
     "ماذا تتضمن خطوة الفرض؟",
     ["Monitoring activity and disciplining breaches.",
      "Monitoring activity and reporting it to the board.",
      "Rewarding staff who remember the policy best.",
      "Reviewing the policy once every five years here."],
     ["مراقبة النشاط وتطبيق إجراءات تأديبية.",
      "مراقبة النشاط وتقديم تقرير للمجلس.",
      "مكافأة الموظفين الذين يتذكرون السياسة.",
      "مراجعة السياسة مرة كل خمس سنوات."],
     "Enforcement means monitoring activity and applying disciplinary measures when the policy is broken.",
     "الفرض يعني مراقبة النشاط وتطبيق إجراءات تأديبية عند خرق السياسة."),
]

KEY = "ABCDABCDABCD"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
