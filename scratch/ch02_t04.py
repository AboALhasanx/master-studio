#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch02 T04 — The five mitigation strategies and the PDCA cycle."""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch02_lib import build

QUIZ = "Quiz_Ch02_T04_Mitigation_And_PDCA"
TOPIC_EN = "The Five Mitigation Strategies & the PDCA Cycle"
TOPIC_AR = "استراتيجيات التخفيف الخمس ودورة PDCA"

I = [
    # 1 -------------------------------------------------------------------
    ("risk_management_scope", "Remember",
     "What does risk management cover?",
     "ماذا تغطي إدارة المخاطر؟",
     ["All activities that evaluate and reduce risk.",
      "The part that cuts risk to an acceptable level.",
      "The process of writing the security policy.",
      "The list of countermeasures already installed."],
     ["كل الأنشطة التي تقيّم الخطر وتقلّله.",
      "الجزء الذي يخفّض الخطر لمستوى مقبول.",
      "عملية كتابة سياسة الأمن للمؤسسة كلها.",
      "قائمة الضوابط المثبتة فعلاً في الشبكة."],
     "Risk management is the whole set of activities for evaluating and reducing risk. Mitigation is only the part that lowers risk to an acceptable level.",
     "إدارة المخاطر هي كل أنشطة تقييم الخطر وتقليله. أما التخفيف فهو فقط الجزء الذي يخفّض الخطر لمستوى مقبول."),

    # 2 -------------------------------------------------------------------
    ("risk_mitigation_definition", "Remember",
     "What is the part of risk management that reduces risk to an acceptable level called?",
     "ماذا يُسمّى الجزء من إدارة المخاطر الذي يخفّض الخطر لمستوى مقبول؟",
     ["Risk mitigation.", "Risk transference.", "Risk retention.", "Risk analysis."],
     ["تخفيف المخاطر.", "نقل المخاطر للغير.", "الاحتفاظ بها.", "تحليل المخاطر."],
     "That part has its own name: risk mitigation. It is one component of risk management, not a synonym for it.",
     "ذلك الجزء له اسمه الخاص: تخفيف المخاطر. وهو مكوّن من إدارة المخاطر لا مرادف لها."),

    # 3 -------------------------------------------------------------------
    ("strategies_order", "Remember",
     "Which sequence gives the five mitigation strategies in their recognised order?",
     "أي تسلسل يعطي استراتيجيات التخفيف الخمس بترتيبها المعتمد؟",
     ["Avoidance, reduction, retention, transfer, sharing.",
      "Avoidance, retention, reduction, sharing, transfer.",
      "Reduction, avoidance, transfer, retention, sharing.",
      "Retention, avoidance, sharing, reduction, transfer."],
     ["التجنّب، التقليل، الاحتفاظ، النقل، المشاركة.",
      "التجنّب، الاحتفاظ، التقليل، المشاركة، النقل.",
      "التقليل، التجنّب، النقل، الاحتفاظ، المشاركة.",
      "الاحتفاظ، التجنّب، المشاركة، التقليل، النقل."],
     "The order is avoidance, reduction, retention, transfer, sharing, and it is one of only two lists where the order matters.",
     "الترتيب هو: التجنّب، التقليل، الاحتفاظ، النقل، المشاركة، وهو أحد موضعين فقط يكون فيهما الترتيب مهماً."),

    # 4 -------------------------------------------------------------------
    ("strategy_avoidance", "Apply",
     "An organisation forbids WiFi on its premises. Which strategy is this?",
     "مؤسسة تمنع استخدام WiFi في مبانيها. أي استراتيجية هذه؟",
     ["Risk avoidance.", "Risk reduction.", "Risk retention.", "Risk transfer."],
     ["استراتيجية التجنّب.", "استراتيجية التقليل.", "استراتيجية الاحتفاظ.", "استراتيجية النقل."],
     "Avoidance keeps the system away from the risk altogether, and forbidding a risky behaviour such as WiFi is the standard example.",
     "التجنّب يُبعد النظام عن الخطر أصلاً، ومنع سلوك خطر كاستخدام WiFi هو المثال القياسي."),

    # 5 -------------------------------------------------------------------
    ("strategy_reduction", "Apply",
     "A team adds backups and encryption to prevent losses and shrink their extent. Which strategy is this?",
     "فريق يضيف نسخاً احتياطية وتشفيراً لمنع الخسائر وتقليل حجمها. أي استراتيجية هذه؟",
     ["Risk reduction.", "Risk avoidance.", "Risk retention.", "Risk sharing."],
     ["استراتيجية التقليل.", "استراتيجية التجنّب.", "استراتيجية الاحتفاظ.", "استراتيجية المشاركة."],
     "Reduction takes proactive steps to prevent the loss or to make it smaller. Backups and encryption are the standard examples.",
     "التقليل يتخذ خطوات استباقية لمنع الخسارة أو تصغيرها. والنسخ الاحتياطي والتشفير هما المثالان القياسيان."),

    # 6 -------------------------------------------------------------------
    ("strategy_retention", "Apply",
     "An organisation uses reliable but not redundant equipment and accepts the resulting exposure. Which strategy is this?",
     "مؤسسة تستخدم معدات موثوقة لكن غير مكرّرة وتقبل التعرّض الناتج. أي استراتيجية هذه؟",
     ["Risk retention.", "Risk reduction.", "Risk transfer.", "Risk sharing."],
     ["استراتيجية الاحتفاظ.", "استراتيجية التقليل.", "استراتيجية النقل.", "استراتيجية المشاركة."],
     "Retention allows a certain agreed amount of residual risk to stay. Reliable but non-redundant equipment is the standard example.",
     "الاحتفاظ يسمح ببقاء مقدار متفق عليه من الخطر المتبقي. والمعدات الموثوقة غير المكرّرة هي المثال القياسي."),

    # 7 -------------------------------------------------------------------
    ("strategy_transfer", "Apply",
     "An organisation signs an outsourcing contract so another company carries part of the risk. Which strategy is this?",
     "مؤسسة توقّع عقد استعانة بمصادر خارجية لتتحمل شركة أخرى جزءاً من الخطر. أي استراتيجية هذه؟",
     ["Risk transfer.", "Risk avoidance.", "Risk reduction.", "Risk sharing."],
     ["استراتيجية نقل الخطر.", "استراتيجية التجنّب.", "استراتيجية التقليل.", "استراتيجية المشاركة."],
     "Transfer hands the risk to others, and an outsourcing contract is the standard example.",
     "النقل يحوّل الخطر إلى طرف آخر، وعقد الاستعانة بمصادر خارجية هو المثال القياسي."),

    # 8 -------------------------------------------------------------------
    ("strategy_sharing", "Apply",
     "Two firms agree on common facilities and mutual insurance. Which strategy is this?",
     "شركتان تتفقان على مرافق مشتركة وتأمين متبادل. أي استراتيجية هذه؟",
     ["Risk sharing.", "Risk avoidance.", "Risk retention.", "Risk transfer."],
     ["استراتيجية المشاركة.", "استراتيجية التجنّب.", "استراتيجية الاحتفاظ.", "استراتيجية النقل."],
     "Sharing means dealing with the risk jointly with other parties, and common facilities or mutual insurance are the standard examples.",
     "المشاركة تعني التعامل مع الخطر بشكل مشترك مع أطراف أخرى، والمرافق المشتركة أو التأمين المتبادل هما المثالان القياسيان."),

    # 9 -------------------------------------------------------------------
    ("transfer_vs_sharing", "Analyze",
     "What separates risk transfer from risk sharing?",
     "ما الذي يفرّق نقل المخاطر عن مشاركتها؟",
     ["Transfer moves the risk; sharing splits it with others.",
      "Transfer splits the risk in two; sharing moves it to others.",
      "Transfer keeps the risk; sharing removes it entirely.",
      "Transfer removes the risk; sharing keeps it quietly."],
     ["النقل يحوّل الخطر، والمشاركة تقسمه مع غيرك.",
      "النقل يقسم الخطر نصفين، والمشاركة تحوّله لغيرك.",
      "النقل يحتفظ بالخطر، والمشاركة تزيله كلياً.",
      "النقل يزيل الخطر، والمشاركة تحتفظ به بصمت."],
     "In transfer one party hands the exposure to another. In sharing the parties carry it together, which is why insurance and common facilities count as sharing.",
     "في النقل يُسلّم طرفٌ التعرّض لطرف آخر. وفي المشاركة يحمله الأطراف معاً، ولهذا يُعدّ التأمين والمرافق المشتركة من المشاركة."),

    # 10 ------------------------------------------------------------------
    ("pdca_four_elements", "Remember",
     "Which four elements make up the PDCA cycle?",
     "أي أربعة عناصر تشكّل دورة PDCA؟",
     ["Plan, Do, Check, and Act.", "Plan, Do, Control, Adjust.",
      "Prepare, Do, Check, Adjust.", "Plan, Deploy, Check, Accept."],
     ["تخطيط، تنفيذ، تحقق، تصحيح.", "تخطيط، تنفيذ، ضبط، تعديل.",
      "تحضير، تنفيذ، تحقق، تعديل.", "تخطيط، نشر، تحقق، قبول."],
     "The four are Plan, Do, Check, Act. Check and Act are separate steps: one measures, the other adjusts.",
     "الأربعة هي: تخطيط، تنفيذ، تحقق، تصحيح. والتحقق والتصحيح خطوتان منفصلتان: واحدة تقيس والأخرى تعدّل."),

    # 11 ------------------------------------------------------------------
    ("pdca_plan", "Remember",
     "Which activities belong to the Plan phase?",
     "أي أنشطة تنتمي إلى مرحلة التخطيط؟",
     ["Threats identified, risks analysed, controls planned.",
      "Controls implemented across the whole organisation.",
      "The solution monitored for the level actually achieved.",
      "The solution adjusted or a whole new plan started."],
     ["تحديد التهديدات وتحليل المخاطر والتخطيط.",
      "تنفيذ الضوابط أو أشكال إدارة المخاطر.",
      "مراقبة الحل للتأكد من بقاء مستوى الأمان.",
      "تعديل الحل أو البدء بخطة جديدة كلياً."],
     "Plan identifies the threats, analyses the risks, and plans the countermeasures. Nothing is implemented yet in this phase.",
     "التخطيط يحدد التهديدات ويحلّل المخاطر ويخطط التدابير المضادة. ولا شيء يُنفَّذ بعد في هذه المرحلة."),

    # 12 ------------------------------------------------------------------
    ("pdca_do", "Remember",
     "What happens in the Do phase?",
     "ماذا يحدث في مرحلة التنفيذ؟",
     ["The controls are implemented.", "The threats are identified.",
      "The solution is monitored over time.", "The solution is adjusted later."],
     ["تنفيذ الضوابط المخطَّطة.", "تحديد التهديدات في البداية.",
      "مراقبة الحل المنفَّذ باستمرار.", "تعديل الحل بعد المراقبة."],
     "Do is where the countermeasures or other forms of risk management are actually put in place.",
     "التنفيذ هو حيث تُطبَّق التدابير المضادة أو أشكال إدارة المخاطر فعلياً."),

    # 13 ------------------------------------------------------------------
    ("pdca_act", "Remember",
     "What does the Act phase allow?",
     "ماذا تتيح مرحلة التصحيح؟",
     ["The solution is adjusted or a new plan begins.",
      "The threats are identified and then analysed.",
      "The controls are implemented everywhere.",
      "The solution is monitored for the level reached."],
     ["تعديل الحل أو البدء بخطة جديدة كلياً.",
      "تحديد التهديدات وتحليلها بعد ذلك.",
      "تنفيذ الضوابط في المؤسسة كلها فعلياً.",
      "مراقبة الحل للتأكد من المستوى المطلوب."],
     "Act adjusts the solution so it keeps giving the wanted level, or decides on a completely new Plan phase.",
     "التصحيح يعدّل الحل ليبقى معطياً المستوى المطلوب، أو يقرر البدء بمرحلة تخطيط جديدة كلياً."),

    # 14 ------------------------------------------------------------------
    ("why_pdca_repeats", "Understand",
     "Why does risk management take the form of a repeating cycle?",
     "لماذا تأخذ إدارة المخاطر شكل دورة متكررة؟",
     ["Because the risk profile changes as attacks evolve.",
      "Because the plan is always written incorrectly at first.",
      "Because the controls stop working after one year.",
      "Because the policy requires four separate reports."],
     ["لأن ملف المخاطر يتغير بتطور الهجمات.",
      "لأن الخطة تُكتب بشكل خاطئ دائماً.",
      "لأن الضوابط تتوقف عن العمل بعد سنة.",
      "لأن السياسة تفرض أربعة تقارير منفصلة."],
     "The risk profile shifts as new attack forms appear and known threats become more frequent, so the situation must be re-evaluated at regular intervals.",
     "ملف المخاطر يتغيّر مع ظهور أشكال هجوم جديدة وزيادة تكرار التهديدات المعروفة، فلهذا يجب إعادة تقييم الوضع على فترات منتظمة."),
]

KEY = "ABCDABCDACBDAB"

build(QUIZ, TOPIC_EN, TOPIC_AR, I, KEY)
