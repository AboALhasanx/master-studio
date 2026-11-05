#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ASE Chapter 5's vocabulary-aligned MCSQuiz banks (schema v2)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT = ROOT / "scratch" / "ase_ch05_stage"
LETTERS = "ABCD"

BALANCED_OPTIONS = {
    "ch5_design_bridge": (["The approved requirements become a technical blueprint", "Executable code carries out the required system behavior", "Verification evidence records the system's test outcomes", "A released interface lets users access the completed product"], ["تحويل المتطلبات المعتمدة إلى مخطط تقني قابل للبناء", "شيفرة تنفيذية تحقق السلوك المطلوب للمستخدم النهائي", "تقرير تحقق يوثق نتائج اختبار وظائف النظام", "واجهة منشورة تتيح استخدام المنتج بعد اكتماله"]),
    "ch5_design_question": (["How required behavior will be structured and built", "What user problem the product is expected to address", "Who approves the budget and assigns project resources", "When the completed product is planned for release"], ["كيفية بناء السلوك المطلوب وتنظيم مكونات النظام", "ما المشكلة التي ينبغي أن يعالجها المنتج للمستخدم", "من يعتمد ميزانية المشروع ويوزع موارده المتاحة", "متى يخطط لإصدار المنتج المكتمل للمستخدمين"]),
    "ch5_design_outputs": (["Architecture, interfaces, data structures, and procedures", "Workflows, screens, business operations, and data formats", "Source files, executables, test reports, and releases", "Budget estimates, staff plans, risks, and delivery dates"], ["المعمارية والواجهات وبنى البيانات والإجراءات البرمجية", "سير العمل والشاشات والعمليات التجارية وصيغ البيانات", "ملفات الشيفرة والبرامج وتقارير الاختبار وحزم الإصدارات", "تقديرات الميزانية وخطط الموارد والمخاطر ومواعيد التسليم"]),
    "ch5_design_sdlc": (["After requirements analysis and before implementation", "After system deployment and before needs analysis", "Before feasibility work and after product maintenance", "During coding after the unit tests are completed"], ["بعد تحليل المتطلبات وقبل تنفيذ البرمجيات", "بعد نشر النظام وقبل تحليل حاجات المستخدم", "قبل دراسة الجدوى وبعد صيانة المنتج", "أثناء البرمجة بعد اكتمال اختبارات الوحدات"]),
    "ch5_design_not_code": (["It specifies construction decisions before code is written", "It executes the required functions for end users", "It records defects discovered after product deployment", "It replaces the need to analyze the system requirements"], ["يحدد قرارات البناء قبل كتابة الشيفرة البرمجية", "ينفذ الوظائف المطلوبة للمستخدمين النهائيين", "يسجل العيوب المكتشفة بعد نشر المنتج البرمجي", "يلغي الحاجة إلى تحليل متطلبات النظام البرمجي"]),
    "ch5_closed_system": (["A closed system with no exchange across its boundary", "An open system exchanging with its environment", "An interactive system responding to external actors", "A distributed system spanning connected locations"], ["نظام مغلق لا يتبادل المعلومات عبر حدوده الخارجية", "نظام مفتوح يتبادل المعلومات مع بيئته الخارجية", "نظام تفاعلي يستجيب لطلبات الجهات الخارجية", "نظام موزع يعمل عبر مواقع مترابطة متعددة"]),
    "ch5_design_structure": (["How components are arranged and communicate", "How user training is scheduled after delivery", "How a product name is chosen for marketing", "How project invoices are reviewed and approved"], ["كيفية ترتيب مكونات النظام وطرق التواصل بينها", "كيفية جدولة تدريب المستخدمين بعد تسليم المنتج", "كيفية اختيار اسم المنتج لأغراض التسويق", "كيفية مراجعة فواتير المشروع والحصول على اعتمادها"]),
    "ch5_design_construction": (["The structures and interfaces that need implementation", "The user problem that still needs initial discovery", "The product price determined by market demand", "The production defects hidden from design reviewers"], ["البنى والواجهات التي ينبغي تنفيذها في البرمجيات", "مشكلة المستخدم التي ما زالت بحاجة إلى اكتشاف أولي", "سعر المنتج الذي تحدده متطلبات السوق التجارية", "عيوب الإنتاج التي تخفى عن مراجعي التصميم"]),
    "ch5_conceptual_what": (["The capabilities that users can observe and request", "The internal hierarchy of calling software components", "The algorithms that programmers select for execution", "The memory layout used by components at runtime"], ["القدرات التي يستطيع المستخدمون رؤيتها وطلبها", "التسلسل الداخلي لاستدعاء مكونات البرمجيات", "الخوارزميات التي يختار المبرمجون تنفيذها", "تنظيم الذاكرة الذي تستخدمه المكونات أثناء التشغيل"]),
    "ch5_technical_how": (["How the architecture realizes required system behavior", "What business outcomes the customer expects to receive", "Why an organization approved the proposed project", "Which interface colors users happen to prefer"], ["كيفية تحقيق المعمارية للسلوك المطلوب من النظام", "النتائج التجارية التي يتوقع العميل أن يحققها", "أسباب اعتماد المؤسسة للمشروع البرمجي المقترح", "ألوان الواجهة التي يفضلها المستخدمون عادة"]),
    "ch5_conceptual_audience": (["Customers and users who describe external needs", "Database administrators who manage stored records", "Technicians who maintain computing hardware", "Compiler developers who build translation tools"], ["العملاء والمستخدمون الذين يصفون الحاجات الخارجية", "مسؤولو قواعد البيانات الذين يديرون السجلات المخزنة", "فنيو الصيانة الذين يصلحون أجهزة الحاسوب", "مطورو المترجمات الذين يبنون أدوات ترجمة الشيفرة"]),
    "ch5_technical_audience": (["Builders who implement the system components", "Customers who approve visible user workflows", "Marketers who position a product in its market", "Operators who schedule workplace meetings"], ["المنفذون الذين يبنون مكونات النظام البرمجي", "العملاء الذين يعتمدون إجراءات واجهة المستخدم", "المسوّقون الذين يحددون موقع المنتج في السوق", "المشغلون الذين ينظمون اجتماعات العمل"]),
    "ch5_conceptual_artifacts": (["A user workflow showing visible steps and outcomes", "A method signature defining parameters and returns", "A database schema describing stored data fields", "A module hierarchy showing procedural control calls"], ["سير مستخدم يوضح الخطوات والنتائج الظاهرة للنظام", "توقيع طريقة يحدد المعاملات والقيم المعادة", "مخطط قاعدة بيانات يصف حقول السجلات المخزنة", "تسلسل وحدات يوضح استدعاءات التحكم الإجرائي"]),
    "ch5_technical_artifacts": (["Technical design specifying internal construction decisions", "Conceptual design describing user-visible capabilities", "Marketing design positioning the product for customers", "Operational training explaining the released interface"], ["تصميم فني يحدد قرارات البناء الداخلية للنظام", "تصميم مفهومي يصف القدرات الظاهرة للمستخدمين", "تصميم تسويقي يحدد موقع المنتج لدى العملاء", "تدريب تشغيلي يشرح واجهة المنتج بعد إصداره"]),
    "ch5_conceptual_language": (["Business terms describing the user's intended goals", "Implementation terms describing internal method calls", "Storage terms describing database tables and indexes", "Hardware terms describing device and processor registers"], ["مصطلحات الأعمال التي تصف أهداف المستخدم المقصودة", "مصطلحات التنفيذ التي تصف استدعاء الطرق الداخلية", "مصطلحات التخزين التي تصف الجداول والفهارس", "مصطلحات الأجهزة التي تصف سجلات المعالج والذاكرة"]),
    "ch5_conceptual_technical_translation": (["Translate user expectations into buildable system structure", "Replace user needs with a preferred technology choice", "Turn architecture decisions into marketing statements", "Hide system behavior from the implementation team"], ["ترجمة توقعات المستخدم إلى بنية قابلة للبناء", "استبدال حاجات المستخدم بتقنية يفضلها الفريق", "تحويل قرارات المعمارية إلى عبارات تسويقية", "إخفاء سلوك النظام عن فريق التنفيذ البرمجي"]),
    "ch5_design_objectives_set": (["Correct and complete, understandable, right-level, maintainable", "Fast and portable, minimal, secure, fully reusable", "Cheap and familiar, automated, distributed, fault-free", "Compact and generic, fashionable, independent, measurable"], ["صحيح وكامل ومفهوم وبالمستوى المناسب وقابل للصيانة", "سريع ومحمول ومختصر وآمن وقابل لإعادة الاستخدام", "رخيص ومألوف ومؤتمت وموزع وخالٍ من الأعطال", "مدمج وعام وحديث ومستقل وقابل للقياس"]),
    "ch5_objective_correct_complete": (["The required behavior and relevant system requirements", "Every future feature a user could possibly request", "Only the screens approved by the marketing group", "Implementation details unrelated to stated needs"], ["السلوك المطلوب والمتطلبات ذات الصلة بالنظام", "كل ميزة قد يطلبها مستخدم في المستقبل", "الشاشات التي اعتمدتها مجموعة التسويق فقط", "تفاصيل تنفيذ لا ترتبط بالحاجات المحددة"]),
    "ch5_objective_understandable": (["Clear enough for its intended technical readers", "Hidden from everyone except its original author", "Expanded with every low-level coding statement", "Written only in vendor-specific machine terms"], ["واضح بما يكفي للقراء الفنيين المقصودين", "مخفي عن الجميع عدا مؤلفه الأصلي", "موسع بكل تعليمة برمجية منخفضة المستوى", "مكتوب بمصطلحات آلة خاصة بمورد واحد"]),
    "ch5_objective_right_level": (["Its detail matches the decision and intended audience", "It contains every implementation statement in full", "It omits all structure until coding is finished", "It gives every stakeholder an identical detail level"], ["تفاصيله تلائم القرار والجمهور المقصود", "يتضمن كل تعليمة تنفيذية بصورة كاملة", "يحذف البنية حتى انتهاء كتابة الشيفرة", "يعرض المستوى نفسه من التفاصيل للجميع"]),
    "ch5_objective_maintainable": (["Maintainability across later requirement changes", "Visual novelty in the delivered user interface", "Maximum implementation detail in every component", "Minimum communication among system stakeholders"], ["قابلية الصيانة عند تغير متطلبات النظام لاحقاً", "الجدة البصرية في واجهة المستخدم النهائية", "أقصى تفصيل للتنفيذ في جميع المكونات", "أقل تواصل بين أصحاب المصلحة في النظام"]),
    "ch5_objective_traceability": (["Correctness and completeness of the design", "Appropriate level of technical detail", "Ease of visual presentation to reviewers", "Technical independence from system users"], ["صحة التصميم واكتماله في تمثيل المتطلبات", "ملاءمة مستوى التفاصيل الفنية للتنفيذ", "سهولة العرض البصري على مراجعي التصميم", "الاستقلال الفني عن مستخدمي النظام"]),
    "ch5_objective_audience": (["The right level of detail for implementation", "Requirements completeness and traceability", "External openness across system boundaries", "Protection of internal data at runtime"], ["مستوى التفاصيل المناسب لتنفيذ النظام", "اكتمال المتطلبات وإمكان تتبعها", "انفتاح النظام عبر حدوده الخارجية", "حماية البيانات الداخلية أثناء التشغيل"]),
    "ch5_objectives_not_exhaustiveness": (["Enough detail for clear and correct construction", "Every code statement written before analysis ends", "One quality optimized while others are ignored", "Extra features replacing required behavior coverage"], ["تفاصيل كافية لبناء واضح وصحيح للنظام", "كتابة كل تعليمة قبل انتهاء التحليل", "تحسين خاصية مع تجاهل الخصائص الأخرى", "ميزات إضافية تحل محل تغطية المتطلبات"]),
    "ch5_design_importance_bridge": (["It turns requirements into a construction plan", "It replaces the need to define user needs", "It guarantees implementation without any defects", "It makes verification unnecessary after coding"], ["يحول المتطلبات إلى خطة لبناء النظام", "يلغي الحاجة إلى تحديد حاجات المستخدم", "يضمن تنفيذ النظام من دون عيوب", "يجعل التحقق غير ضروري بعد البرمجة"]),
    "ch5_design_quality": (["The quality and maintainability of the result", "The laws governing the customer's industry", "The size of the target user population", "The electricity at a deployment location"], ["جودة المنتج البرمجي وقابليته للصيانة", "القوانين المنظمة لمجال عمل العميل", "عدد مستخدمي السوق المستهدف للنظام", "الكهرباء المتاحة في موقع نشر النظام"]),
    "ch5_design_early_decisions": (["Shared choices can shape many system components", "Every design choice becomes irrelevant after coding", "Requirements stop changing once classes exist", "Testing cannot identify defects in implemented code"], ["قد تؤثر القرارات المشتركة في مكونات النظام", "يصبح كل قرار تصميمي غير مهم بعد البرمجة", "تتوقف المتطلبات عن التغير بعد إنشاء الأصناف", "لا يستطيع الاختبار كشف عيوب الشيفرة المنفذة"]),
    "ch5_design_quality_three": (["Durability, utility, and charm", "Speed, portability, and security", "Accuracy, usability, and modularity", "Cost, schedule, and productivity"], ["المتانة والمنفعة والجاذبية", "السرعة وقابلية النقل والأمن", "الدقة وقابلية الاستخدام والنمطية", "الكلفة والجدول والإنتاجية"]),
    "ch5_design_vs_coding": (["Design plans the solution; coding implements it", "Design tests the product; coding approves its scope", "Design gathers needs; coding selects the users", "Design deploys services; coding manages budgets"], ["يخطط التصميم للحل وتنفذ البرمجة هذا الحل", "يختبر التصميم المنتج وتعتمد البرمجة نطاقه", "يجمع التصميم الحاجات وتختار البرمجة المستخدمين", "ينشر التصميم الخدمات وتدير البرمجة الميزانيات"]),
    "ch5_design_construction_errors": (["It clarifies component roles before implementation", "It prevents maintenance work after product release", "It removes the need to communicate interfaces", "It proves each requirement is already validated"], ["يوضح أدوار المكونات قبل بدء التنفيذ", "يمنع أعمال الصيانة بعد إصدار المنتج", "يلغي الحاجة إلى توضيح الواجهات", "يثبت اعتماد كل متطلب قبل التنفيذ"]),
    "ch5_design_maintainability": (["Maintainability through localized design decisions", "Conceptual scope through user-visible workflows", "External openness through system boundaries", "Deployment clarity through physical nodes"], ["قابلية الصيانة بحصر قرارات التصميم", "النطاق المفهومي عبر إجراءات المستخدم", "الانفتاح الخارجي عبر حدود النظام", "وضوح النشر عبر العقد المادية"]),
    "ch5_design_not_guarantee": (["It guides construction but cannot ensure defect-free code", "It removes all uncertainty from future maintenance", "It proves every implementation choice will be optimal", "It prevents requirements changing after approval"], ["يوجه البناء لكنه لا يضمن شيفرة خالية من العيوب", "يزيل كل عدم يقين عن الصيانة المستقبلية", "يثبت مثالية كل خيار تنفيذي في النظام", "يمنع تغير المتطلبات بعد اعتمادها"]),
}

BALANCED_OPTIONS.update({
    "ch5_design_not_code": (["It sets the build plan before coding begins", "It executes the required functions for end users", "It records defects found after product deployment", "It removes the need to analyze system requirements"], ["يحدد خطة البناء قبل بدء كتابة الشيفرة", "ينفذ الوظائف المطلوبة للمستخدمين النهائيين", "يسجل عيوب المنتج بعد نشره للمستخدمين", "يلغي الحاجة إلى تحليل متطلبات النظام البرمجي"]),
    "ch5_closed_system": (["A distributed system operating at connected sites", "A closed system without exchange across its boundary", "An open system exchanging data with its environment", "An interactive system responding to outside requests"], ["نظام موزع يعمل عبر مواقع مترابطة", "نظام مغلق بلا تبادل عبر الحدود الخارجية", "نظام مفتوح يتبادل البيانات مع البيئة", "نظام تفاعلي يستجيب لطلبات خارجية متنوعة"]),
    "ch5_design_construction": (["A user problem still awaiting its initial discovery", "A final product price determined by market demand", "Production defects hidden from design reviewers", "Structures and interfaces planned for implementation"], ["مشكلة مستخدم ما زالت قيد الاكتشاف الأولي", "سعر نهائي تحدده متطلبات السوق التجارية", "عيوب إنتاج مخفية عن مراجعي التصميم", "بنى وواجهات مخطط لتنفيذها في النظام"]),
    "ch5_conceptual_artifacts": (["A user workflow showing visible steps and outcomes", "A method signature defining parameters and returns", "A database schema describing stored data fields", "A module hierarchy showing procedural control calls"], ["سير مستخدم يوضح الخطوات الظاهرة والنتائج المتوقعة", "توقيع طريقة يحدد المعاملات والقيم التي تعيدها", "مخطط قاعدة يصف الحقول المخزونة وأنواعها", "تسلسل وحدات يبين التحكم واستدعاءات الإجراءات"]),
    "ch5_conceptual_technical_translation": (["Replace user needs with a selected technology choice", "Turn architecture decisions into marketing statements", "Hide system behavior from the implementation team", "Translate user expectations into a buildable design"], ["استبدال حاجات المستخدم بتقنية مختارة مسبقاً", "تحويل قرارات المعمارية إلى عبارات تسويق", "حجب سلوك النظام عن فريق التنفيذ البرمجي", "ترجمة توقعات المستخدم إلى بنية قابلة للبناء"]),
    "ch5_design_objectives_set": (["Correct, complete, understandable, right-level, maintainable", "Fast, portable, compact, secure, reusable across projects", "Low-cost, familiar, automated, distributed, fault-resistant", "Compact, generic, current, independent, measurable, flexible"], ["صحيح وكامل ومفهوم وبالمستوى المناسب وقابل للصيانة", "سريع ومحمول ومختصر وآمن وقابل لإعادة الاستخدام", "منخفض الكلفة ومألوف ومؤتمت وموزع ومقاوم للأعطال", "مدمج وعام وحديث ومستقل وقابل للقياس والتوسع"]),
    "ch5_objective_correct_complete": (["Required behavior and relevant system requirements", "Every imaginable feature requested by future users", "Only visible screens approved by the marketing team", "Implementation details unrelated to stated system needs"], ["السلوك المطلوب والمتطلبات المرتبطة بالنظام", "كل ميزة قد يطلبها المستخدم مستقبلاً للنظام", "الشاشات الظاهرة التي اعتمدها فريق التسويق", "تفاصيل تنفيذ لا ترتبط بالحاجات المحددة"]),
    "ch5_objective_maintainable": (["Maintainability across later requirement changes", "Visual novelty added to the final user interface", "Maximum implementation detail in every component", "Reduced communication among system stakeholders"], ["قابلية الصيانة عند تغير متطلبات النظام لاحقاً", "الجدة البصرية المضافة إلى واجهة المستخدم النهائية", "التفاصيل التنفيذية القصوى في كل مكون برمجي", "تقليل التواصل بين أصحاب المصلحة في النظام"]),
    "ch5_design_quality": (["The electricity at a software deployment location", "The quality and maintainability of the final result", "The laws governing the customer's industry", "The size of the system's target user population"], ["الكهرباء المتاحة في موقع نشر البرمجيات", "جودة المنتج النهائي وقابليته للصيانة", "القوانين المنظمة لمجال عمل العميل", "عدد المستخدمين في السوق المستهدف للنظام"]),
    "ch5_design_maintainability": (["External openness through system boundaries", "Deployment clarity through physical nodes", "Maintainability through localized design choices", "Conceptual scope through user-visible workflows"], ["الانفتاح الخارجي عبر حدود النظام البرمجي", "وضوح النشر عبر عقد الأجهزة المادية", "صيانة أسهل عبر حصر قرارات التصميم", "النطاق المفهومي عبر إجراءات المستخدم الظاهرة"]),
    "ch5_design_not_guarantee": (["It removes uncertainty from future maintenance", "It proves every implementation choice will be optimal", "It prevents requirements changing after approval", "It guides construction but cannot promise defect-free code"], ["يزيل أوجه الغموض عن الصيانة المستقبلية", "يثبت مثالية الخيارات التنفيذية في النظام", "يمنع تغير المتطلبات بعد الاعتماد النهائي", "يوجه البناء ولا يضمن خلو المنتج من العيوب"]),
})

# These six choices were accidentally placed after the distractors in an earlier
# draft. Keep the source-supported answer at index zero because build_question()
# rotates that position into the balanced answer key.
BALANCED_OPTIONS.update({
    "ch5_closed_system": ([
        "A closed system without exchange across its boundary",
        "An open system exchanging data with its environment",
        "An interactive system responding to outside requests",
        "A distributed system operating at connected sites",
    ], [
        "نظام مغلق بلا تبادل للمعلومات عبر حدوده الخارجية",
        "نظام مفتوح يتبادل البيانات مع بيئته الخارجية",
        "نظام تفاعلي يستجيب لطلبات خارجية متنوعة",
        "نظام موزع يعمل عبر مواقع وأجهزة حاسوبية مترابطة",
    ]),
    "ch5_design_construction": ([
        "Structures and interfaces planned for implementation",
        "A user problem still awaiting its initial discovery",
        "A product price set by market demand and buyers",
        "Production defects hidden from design reviewers",
    ], [
        "بنى وواجهات النظام التي تحدد طريقة تنفيذه",
        "مشكلة المستخدم التي لم يتحدد حلها بعد",
        "السعر النهائي للمنتج وفق متطلبات السوق التجارية",
        "عيوب الإنتاج التي يخفيها الفريق عن مراجعي التصميم",
    ]),
    "ch5_conceptual_technical_translation": ([
        "Translate user expectations into a buildable system design",
        "Replace user needs with a preferred technology choice",
        "Turn architecture decisions into marketing statements",
        "Hide system behavior from the implementation team",
    ], [
        "ترجمة توقعات المستخدم إلى تصميم تقني قابل للتنفيذ",
        "استبدال حاجات المستخدم بتقنية يفضلها فريق التطوير",
        "تحويل قرارات المعمارية إلى عبارات تسويقية واضحة",
        "حجب سلوك النظام عن فريق التنفيذ البرمجي",
    ]),
    "ch5_design_quality": ([
        "The quality and maintainability of the final result",
        "The electricity available at the deployment location",
        "The laws governing the customer's business sector",
        "The size of the system's intended user population",
    ], [
        "جودة المنتج النهائي وقابليته للصيانة على المدى البعيد",
        "الكهرباء المتاحة في موقع نشر النظام البرمجي",
        "القوانين المنظمة لمجال عمل العميل التجاري",
        "عدد المستخدمين المتوقعين للنظام في السوق المستهدف",
    ]),
    "ch5_design_maintainability": ([
        "Maintainability through localized design decisions",
        "Conceptual scope through user-visible workflows",
        "External openness through system boundaries",
        "Deployment clarity through physical computing nodes",
    ], [
        "قابلية الصيانة عبر حصر أثر قرارات التصميم",
        "النطاق المفهومي عبر إجراءات المستخدم الظاهرة",
        "انفتاح النظام عبر حدوده مع البيئات الخارجية",
        "وضوح النشر عبر عقد الحوسبة المادية",
    ]),
    "ch5_design_not_guarantee": ([
        "It guides construction but cannot ensure defect-free code",
        "It removes uncertainty from future maintenance work",
        "It proves every implementation choice will be optimal",
        "It prevents requirements from changing after approval",
    ], [
        "يوجه البناء لكنه لا يضمن خلو الشيفرة من العيوب",
        "يزيل أوجه الغموض عن أعمال الصيانة المستقبلية",
        "يثبت أن كل خيار تنفيذي في النظام هو الأمثل",
        "يمنع تغير المتطلبات بعد الحصول على الاعتماد",
    ]),
})

EXPECTED_CORRECT_FIRST = {
    "ch5_closed_system": "A closed system without exchange across its boundary",
    "ch5_design_construction": "Structures and interfaces planned for implementation",
    "ch5_conceptual_technical_translation": "Translate user expectations into a buildable system design",
    "ch5_design_quality": "The quality and maintainability of the final result",
    "ch5_design_maintainability": "Maintainability through localized design decisions",
    "ch5_design_not_guarantee": "It guides construction but cannot ensure defect-free code",
}

# Keep choices parallel in length and grammar using explanatory wording rather
# than repeated padding. For each question the first English and Arabic choices
# are the intended key; build_question() rotates them into the answer pattern.
BALANCED_OPTIONS.update({
    "ch5_design_not_code": ([
        "It sets the technical build plan before coding begins",
        "It executes the required functions for end users",
        "It records defects found after product deployment",
        "It removes the need to analyze system requirements",
    ], [
        "يحدد خطة البناء قبل بدء كتابة الشيفرة",
        "ينفذ الوظائف المطلوبة للمستخدمين النهائيين",
        "يسجل عيوب المنتج بعد نشره للمستخدمين",
        "يلغي الحاجة إلى تحليل متطلبات النظام البرمجي",
    ]),
    "ch5_design_construction": ([
        "Structures and interfaces planned for implementation",
        "A user problem still awaiting its initial discovery",
        "A product price set by market demand and buyers",
        "Production defects hidden from design reviewers",
    ], [
        "بنى وواجهات النظام التي تحدد طريقة تنفيذه",
        "مشكلة المستخدم قبل تحديد حلها التقني",
        "سعر المنتج وفق طلب السوق وتكاليفه",
        "عيوب الإنتاج التي لم تظهر في مراجعة التصميم",
    ]),
    "ch5_conceptual_artifacts": ([
        "A user workflow showing visible steps and outcomes",
        "A method signature defining parameters and returns",
        "A database schema describing stored data fields",
        "A module hierarchy showing procedural control calls",
    ], [
        "سير مستخدم يوضح خطوات التفاعل والنتائج",
        "توقيع طريقة يحدد المعاملات والقيم المعادة",
        "مخطط قاعدة يصف الحقول المخزونة وأنواع بياناتها",
        "تسلسل وحدات يوضح التحكم واستدعاءات الإجراءات",
    ]),
    "ch5_conceptual_technical_translation": ([
        "Translate user expectations into a buildable system design",
        "Replace user needs with a preferred technology choice",
        "Turn architecture decisions into marketing statements",
        "Hide system behavior from the implementation team",
    ], [
        "ترجمة توقعات المستخدم إلى تصميم تقني قابل للتنفيذ",
        "استبدال حاجات المستخدم بتقنية يفضلها فريق التطوير",
        "تحويل قرارات المعمارية إلى عبارات تسويقية واضحة",
        "حجب سلوك النظام عن فريق التنفيذ البرمجي",
    ]),
    "ch5_design_quality": ([
        "The quality and maintainability of the final result",
        "The electricity available at the deployment location",
        "The laws governing the customer's business sector",
        "The size of the system's intended user population",
    ], [
        "جودة المنتج البرمجي وإمكان صيانته لاحقاً",
        "الكهرباء المتوفرة في موقع نشر النظام البرمجي",
        "القوانين التي تنظم قطاع عمل العميل التجاري",
        "عدد المستخدمين المتوقعين في السوق المستهدف",
    ]),
    "ch5_modularity_definition": ([
        "A system divided into focused, loosely linked modules",
        "Combining every responsibility into one shared unit",
        "Duplicating each function throughout every component",
        "Removing defined interfaces among all system parts",
    ], [
        "تقسيم النظام إلى وحدات واضحة قليلة الترابط",
        "جمع مسؤوليات النظام داخل وحدة مشتركة واحدة",
        "تكرار كل وظيفة ضمن جميع مكونات النظام",
        "إلغاء الواجهات بين مكونات النظام كافة",
    ]),
    "ch5_meyer_criteria": ([
        "Decomposability, composability, understandability, continuity, protection",
        "Entity identity, stated purpose, processing steps, resources, deployment",
        "Accurate results, high productivity, portable code, security, interoperability",
        "Objects, classes, messages, reusable inheritance, polymorphism",
    ], [
        "قابلية التفكيك والتركيب والفهم والاستمرار والحماية",
        "تحديد الوحدة وغرضها ومعالجتها ومواردها وموقع نشرها",
        "دقة النتائج والإنتاجية والنقل والأمن والتشغيل البيني",
        "الأصناف والكائنات والرسائل والتغليف والوراثة وتعدد الأشكال",
    ]),
    "ch5_modular_decomposability": ([
        "Breaking a complex problem into smaller subproblems",
        "Concealing every requirement from implementation teams",
        "Moving all responsibilities into the user interface",
        "Combining finished products without defined interfaces",
    ], [
        "تفكيك المشكلة المعقدة إلى مسائل أصغر",
        "حجب متطلبات النظام عن فرق التنفيذ",
        "نقل مسؤوليات النظام إلى واجهة المستخدم",
        "دمج منتجات جاهزة دون واجهات محددة",
    ]),
    "ch5_modularity_tradeoff": ([
        "Coordination costs can outweigh local simplicity",
        "Every small part becomes reusable automatically",
        "All dependencies vanish from the system design",
        "Testing becomes unnecessary for small components",
    ], [
        "قد يفوق التنسيق تعقيد الأجزاء الصغيرة",
        "تصبح الأجزاء الصغيرة قابلة لإعادة الاستخدام تلقائياً",
        "تلغي التجزئة جميع الاعتماديات الخارجية",
        "تغني كثرة الأجزاء عن اختبار النظام",
    ]),
    "ch5_coupling_definition": ([
        "Interdependence between separate software modules",
        "Functional strength inside one software module",
        "Number of screens displayed by an application",
        "Amount of data stored inside an application",
    ], [
        "الاعتماد المتبادل بين وحدات برمجية منفصلة",
        "تماسك العناصر الوظيفية داخل وحدة واحدة",
        "عدد الشاشات الظاهرة في واجهة التطبيق",
        "حجم البيانات المحفوظة داخل التطبيق",
    ]),
    "ch5_best_coupling": ([
        "Data coupling through simple parameter values",
        "Content coupling through access to private code",
        "Control coupling through caller-selected flags",
        "Common coupling through shared global state",
    ], [
        "اقتران البيانات عبر معاملات بسيطة",
        "اقتران المحتوى بتعديل الشيفرة الداخلية",
        "اقتران التحكم عبر علم يوجه التفرع",
        "اقتران مشترك بسبب بيانات عامة مشتركة",
    ]),
    "ch5_worst_coupling": ([
        "Content coupling through access to another module's code",
        "Data coupling through simple parameter values",
        "Stamp coupling through an underused composite record",
        "External coupling through a shared protocol",
    ], [
        "اقتران المحتوى بالوصول إلى داخل الوحدة",
        "اقتران البيانات عبر معاملات بسيطة",
        "اقتران البنية عند تمرير حقول غير لازمة",
        "اقتران خارجي ببروتوكول أو صيغة مشتركة",
    ]),
    "ch5_control_coupling": ([
        "Control coupling through a caller-selected branch flag",
        "Data coupling through simple parameter values",
        "External coupling through a shared protocol",
        "Content coupling through access to another module's code",
    ], [
        "اقتران التحكم عبر علم يختار تفرعاً داخلياً",
        "اقتران البيانات عبر معاملات بسيطة",
        "اقتران خارجي ببروتوكول أو صيغة مشتركة",
        "اقتران المحتوى بالوصول إلى داخل الوحدة",
    ]),
    "ch5_stamp_coupling": ([
        "Stamp coupling through a composite record only partly used",
        "Content coupling through access to private code",
        "Data coupling through simple parameter values",
        "Common coupling through shared global state",
    ], [
        "اقتران بنية مركبة يستخدم منها جزء محدد",
        "اقتران المحتوى بالوصول إلى داخل الوحدة",
        "اقتران البيانات بتمرير معاملات بسيطة",
        "اقتران مشترك عبر ذاكرة أو بيانات عامة",
    ]),
    "ch5_external_coupling": ([
        "External coupling through a shared format or protocol",
        "Data coupling through simple parameter values",
        "Content coupling through access to private code",
        "Common coupling through shared global state",
    ], [
        "اقتران خارجي بسبب بروتوكول أو صيغة مشتركة",
        "اقتران البيانات عبر معاملات بسيطة",
        "اقتران المحتوى بالوصول إلى داخل الوحدة",
        "اقتران مشترك عبر ذاكرة أو بيانات عامة",
    ]),
    "ch5_zero_coupling": ([
        "They must exchange data or transfer control",
        "They must all use identical internal code",
        "They must store state in shared global memory",
        "They must avoid every published interface",
    ], [
        "لا بد أن تتبادل البيانات أو التحكم",
        "لا بد أن تستخدم شيفرة داخلية موحدة",
        "لا بد أن تخزن الحالة في بيانات عامة مشتركة",
        "لا بد أن تتجنب جميع الواجهات المعلنة",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_design_construction": ([
        "Structures and interfaces planned for implementation",
        "A user problem still awaiting its initial discovery",
        "A product price set by market demand and buyers",
        "Production defects hidden from design reviewers",
    ], [
        "بنى وواجهات النظام التي تحدد طريقة تنفيذه",
        "مشكلة المستخدم قبل تحديد حلها التقني",
        "سعر المنتج وفق طلب السوق وتكاليفه",
        "عيوب المنتج التي لم تكشفها مراجعة التصميم",
    ]),
    "ch5_conceptual_artifacts": ([
        "A user workflow showing visible steps and outcomes",
        "A method signature defining parameters and returns",
        "A database schema describing stored data fields",
        "A module hierarchy showing procedural control calls",
    ], [
        "سير مستخدم يوضح خطوات التفاعل والنتائج",
        "توقيع طريقة يحدد المعاملات والقيم المعادة",
        "مخطط قاعدة يحدد حقول البيانات المخزنة",
        "تسلسل وحدات يوضح استدعاءات الإجراءات",
    ]),
    "ch5_conceptual_technical_translation": ([
        "Translate user needs into an implementable design",
        "Replace user needs with a preferred technology choice",
        "Turn architecture decisions into marketing statements",
        "Hide system behavior from the implementation team",
    ], [
        "ترجمة حاجات المستخدم إلى تصميم قابل للتنفيذ",
        "استبدال حاجات المستخدم بتقنية يفضلها فريق التطوير",
        "تحويل قرارات المعمارية إلى عبارات تسويقية واضحة",
        "حجب سلوك النظام عن فريق التنفيذ البرمجي",
    ]),
    "ch5_design_quality": ([
        "The quality and maintainability of the final result",
        "The electricity available at the deployment location",
        "The laws governing the customer's business sector",
        "The size of the system's intended user population",
    ], [
        "جودة النظام وإمكان صيانته على المدى البعيد",
        "الكهرباء المتوفرة في موقع النشر البرمجي",
        "القوانين المنظمة لقطاع عمل الجهة المستفيدة",
        "حجم الفئة المستهدفة من مستخدمي النظام",
    ]),
    "ch5_modularity_tradeoff": ([
        "Coordination costs can outweigh local simplicity",
        "Every small part becomes reusable automatically",
        "All dependencies vanish from the system design",
        "Testing becomes unnecessary for small components",
    ], [
        "قد يفوق التنسيق بساطة الأجزاء الصغيرة",
        "تزيد الأجزاء الصغيرة إمكان إعادة استخدامها",
        "تلغي التجزئة جميع الاعتماديات الخارجية",
        "تغني كثرة الأجزاء عن اختبار النظام",
    ]),
    "ch5_coupling_definition": ([
        "Interdependence between separate software modules",
        "Functional strength inside one software module",
        "Number of screens displayed by an application",
        "Amount of data stored inside an application",
    ], [
        "الاعتماد المتبادل بين وحدات برمجية منفصلة",
        "تماسك العناصر الوظيفية داخل مكون برمجي واحد",
        "عدد الشاشات التي تعرضها واجهة التطبيق",
        "حجم البيانات التي يخزنها التطبيق أثناء عمله",
    ]),
    "ch5_worst_coupling": ([
        "Content coupling reaches into another module's code",
        "Data coupling through simple parameter values",
        "Stamp coupling through an underused composite record",
        "External coupling through a shared protocol",
    ], [
        "اقتران المحتوى بالوصول إلى داخل الوحدة",
        "اقتران البيانات عبر معاملات بسيطة",
        "اقتران البنية عند تمرير حقول غير لازمة",
        "اقتران خارجي ببروتوكول أو صيغة مشتركة",
    ]),
    "ch5_control_coupling": ([
        "Control coupling uses a caller-selected branch flag",
        "Data coupling through simple parameter values",
        "External coupling through a shared protocol",
        "Content coupling through access to another module's code",
    ], [
        "اقتران التحكم عبر علم يختار تفرعاً داخلياً",
        "اقتران البيانات عبر معاملات بسيطة ومحددة",
        "اقتران خارجي ببروتوكول أو صيغة مشتركة",
        "اقتران المحتوى بالوصول إلى داخل الوحدة",
    ]),
    "ch5_stamp_coupling": ([
        "Stamp coupling passes a partly unused record",
        "Content coupling through access to private code",
        "Data coupling through simple parameter values",
        "Common coupling through shared global state",
    ], [
        "اقتران بنية مركبة يستخدم منها جزء محدد",
        "اقتران المحتوى بالوصول إلى داخل الوحدة",
        "اقتران البيانات بتمرير معاملات بسيطة",
        "اقتران مشترك عبر ذاكرة أو بيانات عامة",
    ]),
    "ch5_external_coupling": ([
        "External coupling uses a shared format or protocol",
        "Data coupling passes simple values as parameters",
        "Content coupling reaches into another module's code",
        "Common coupling uses the same global data area",
    ], [
        "اقتران خارجي بسبب بروتوكول أو صيغة مشتركة",
        "اقتران البيانات عبر معاملات بسيطة ومحددة",
        "اقتران المحتوى بالوصول إلى داخل الوحدة",
        "اقتران مشترك عبر ذاكرة أو بيانات عامة",
    ]),
})

EXPECTED_CORRECT_FIRST["ch5_conceptual_technical_translation"] = "Translate user needs into an implementable design"

BALANCED_OPTIONS.update({
    "ch5_cohesion_definition": ([
        "How strongly a module's elements serve one purpose",
        "How strongly separate modules depend on each other",
        "How much memory an application uses during operation",
        "How many users can access a service at the same time",
    ], [
        "مدى ترابط عناصر المكون لخدمة غرض وظيفي واحد",
        "مدى اعتماد المكونات المنفصلة بعضها على بعض",
        "مقدار الذاكرة التي يستخدمها التطبيق أثناء التشغيل",
        "عدد المستخدمين القادرين على دخول الخدمة معاً",
    ]),
    "ch5_worst_cohesion": ([
        "Coincidental cohesion groups elements without a shared purpose",
        "Sequential cohesion passes one operation's output to the next",
        "Communicational cohesion groups operations using the same data",
        "Logical cohesion groups related tasks selected by a control flag",
    ], [
        "التماسك العشوائي يجمع عناصر بلا هدف مشترك",
        "التماسك التسلسلي يمرر ناتج عملية إلى التالية",
        "التماسك الاتصالي يجمع عمليات تستخدم البيانات نفسها",
        "التماسك المنطقي يجمع مهاماً يختارها علم تحكم",
    ]),
    "ch5_temporal_cohesion": ([
        "Temporal cohesion groups tasks by execution time",
        "Sequential cohesion passes output to the next task",
        "Functional cohesion serves one defined task",
        "Communicational cohesion groups tasks on shared data",
    ], [
        "التماسك الزمني يجمع المهام التي تعمل في الفترة نفسها",
        "التماسك التسلسلي يمرر ناتج مهمة إلى التالية",
        "التماسك الوظيفي يخدم مهمة محددة واحدة",
        "التماسك الاتصالي يجمع مهاماً تستخدم البيانات نفسها",
    ]),
    "ch5_functional_cohesion": ([
        "Functional cohesion serves one well-defined task",
        "Elements share a convenient place in one source file",
        "Elements run together only during system startup",
        "A selector chooses one task from an unrelated group",
    ], [
        "التماسك الوظيفي يجعل العناصر تخدم وظيفة محددة واحدة",
        "تشترك العناصر في موضع مناسب داخل ملف واحد",
        "تعمل العناصر معاً عند بدء النظام فقط",
        "يختار محدد عملية من مجموعة غير مترابطة",
    ]),
    "ch5_communicational_cohesion": ([
        "Communicational cohesion groups different tasks using shared data",
        "Procedural cohesion links tasks through their execution order",
        "Coincidental cohesion groups elements without a shared purpose",
        "Sequential cohesion passes one task's output to the next",
    ], [
        "التماسك الاتصالي يجمع عمليات مختلفة تستخدم البيانات نفسها",
        "التماسك الإجرائي يربط المهام بحسب ترتيب تنفيذها",
        "التماسك العشوائي يضم عناصر بلا هدف مشترك",
        "التماسك التسلسلي يربط خرج مهمة بمدخل التالية",
    ]),
    "ch5_logical_cohesion": ([
        "Logical cohesion lets a selector choose among related tasks",
        "Functional cohesion makes every part serve one task",
        "Sequential cohesion passes one task's output to the next",
        "Coincidental cohesion groups elements without a shared purpose",
    ], [
        "التماسك المنطقي يتيح اختيار مهمة من فئة متقاربة",
        "التماسك الوظيفي يجعل كل جزء يخدم مهمة واحدة",
        "التماسك التسلسلي يمرر ناتج مهمة إلى التالية",
        "التماسك العشوائي يجمع عناصر بلا هدف مشترك",
    ]),
    "ch5_cc_design_target": ([
        "High cohesion within modules and low coupling between them",
        "Low cohesion within modules and high coupling between them",
        "High cohesion and high coupling across all components",
        "Low cohesion and low coupling inside each component",
    ], [
        "تماسك عالٍ داخل الوحدات واقتران منخفض بين الوحدات",
        "تماسك منخفض داخل الوحدات واقتران عالٍ بين الوحدات",
        "تماسك عالٍ واقتران عالٍ بين جميع المكونات",
        "تماسك منخفض واقتران منخفض داخل كل وحدة",
    ]),
    "ch5_cc_high_coupling": ([
        "A change can ripple across components that depend on one another",
        "A focused component can no longer have one clear purpose",
        "Every interface becomes hidden from its users and callers",
        "The system loses its ability to exchange data altogether",
    ], [
        "قد ينتقل أثر التغيير إلى المكونات التي يعتمد بعضها على بعض",
        "يفقد المكون المركز غرضه الوظيفي الواحد",
        "تختفي الواجهات عن الجهات التي تستدعيها",
        "يفقد النظام قدرته على تبادل البيانات كلياً",
    ]),
    "ch5_cc_low_cohesion": ([
        "Unrelated responsibilities share one software component",
        "A component depends only on the data values it needs",
        "System functions are isolated by their responsibilities",
        "A user interface contains only a small number of screens",
    ], [
        "اجتماع مسؤوليات غير مترابطة داخل مكون برمجي واحد",
        "اعتماد المكون على قيم البيانات التي يحتاج إليها فقط",
        "عزل وظائف النظام بحسب المسؤوليات التي تؤديها",
        "احتواء واجهة المستخدم على عدد قليل من الشاشات",
    ]),
    "ch5_cc_modularity": ([
        "Focused components communicate through limited dependencies",
        "Unrelated tasks are grouped together to reduce file count",
        "Shared internal state replaces every defined interface",
        "One central component takes every system responsibility",
    ], [
        "تتواصل المكونات المركزة عبر اعتماديات محدودة",
        "تجمع المهام غير المترابطة لتقليل عدد الملفات",
        "تحل الحالة الداخلية المشتركة محل الواجهات المحددة",
        "يتولى مكون مركزي واحد مسؤوليات النظام كلها",
    ]),
    "ch5_cc_information_hiding": ([
        "Callers depend on a stable interface instead of internal representation",
        "Every caller must change whenever internal data changes",
        "All components must share the hidden state of this component",
        "The system can operate without communication among components",
    ], [
        "يعتمد المستدعون على واجهة ثابتة لا على التمثيل الداخلي",
        "يجب أن يتغير كل مستدعٍ عند تغير البيانات الداخلية",
        "تتشارك المكونات كلها الحالة الداخلية المخفية للمكون",
        "يعمل النظام من دون تواصل بين مكوناته البرمجية",
    ]),
    "ch5_strategy_definition": ([
        "How a system is divided into parts and assembled",
        "How project funds are reviewed and approved",
        "How users are selected for acceptance testing",
        "How a released service is promoted to customers",
    ], [
        "طريقة تقسيم النظام إلى أجزاء وتجميع مكوناته",
        "طريقة مراجعة ميزانية المشروع واعتمادها",
        "طريقة اختيار مستخدمي اختبار القبول",
        "طريقة تسويق الخدمة بعد إطلاقها",
    ]),
    "ch5_strategy_topdown_focus": ([
        "The system's high-level goals and overall structure",
        "The internal state of each object in the system",
        "The interface colors preferred by system users",
        "The lowest library details without system context",
    ], [
        "أهداف النظام العليا وبنيته العامة",
        "الحالة الداخلية لكل كائن ضمن النظام",
        "ألوان الواجهات التي يفضلها مستخدمو النظام",
        "تفاصيل المكتبات الدنيا بمعزل عن أهداف النظام",
    ]),
    "ch5_strategy_hybrid": ([
        "It combines high-level system goals with suitable existing parts",
        "It replaces system goals with disconnected utility routines",
        "It uses only classes and rejects procedural components",
        "It delays structural choices until the product is released",
    ], [
        "يجمع أهداف النظام العليا مع أجزاء موجودة وملائمة",
        "يستبدل أهداف النظام بإجراءات خدمية منفصلة",
        "يستخدم الأصناف وحدها ويرفض المكونات الإجرائية",
        "يؤجل القرارات البنيوية إلى ما بعد إصدار المنتج",
    ]),
    "ch5_strategy_not_design": ([
        "Embedded design places software within a physical device",
        "Hybrid design combines top-down and bottom-up directions",
        "Top-down design refines system goals into lower-level details",
        "Bottom-up design combines basic parts into larger systems",
    ], [
        "التصميم المضمن يضع البرمجيات داخل جهاز مادي",
        "التصميم الهجين يجمع الاتجاهين التنازلي والتصاعدي",
        "التصميم التنازلي ينقح أهداف النظام إلى تفاصيل أدنى",
        "التصميم التصاعدي يركب الأجزاء الأساسية لبناء النظام",
    ]),
    "ch5_strategy_select": ([
        "Hybrid design can combine system goals with reusable utilities",
        "Top-down design must discard every available utility",
        "No design strategy applies when components already exist",
        "Bottom-up design must ignore the overall system goals",
    ], [
        "يجمع التصميم الهجين أهداف النظام مع الأدوات القابلة لإعادة الاستخدام",
        "يجب أن يهمل التصميم التنازلي كل أداة متاحة",
        "لا تلائم أي استراتيجية وجود مكونات جاهزة مسبقاً",
        "يجب أن يتجاهل التصميم التصاعدي أهداف النظام العامة",
    ]),
    "ch5_strategy_no_universal_winner": ([
        "Match the approach to system goals and available components",
        "Assume one strategy works best for every software project",
        "Choose only by how many diagrams the team will produce",
        "Select the strategy that uses the newest terminology",
    ], [
        "اختيار النهج الذي يلائم أهداف النظام ومكوناته المتاحة",
        "افتراض تفوق استراتيجية واحدة في جميع المشاريع البرمجية",
        "تحديد النهج بحسب عدد المخططات التي سينتجها الفريق فقط",
        "اختيار الاستراتيجية ذات المصطلحات الأحدث دائماً",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_bottomup_definition": ([
        "With basic components and utility routines",
        "With the system's highest-level coordinator",
        "With arrangements for user-interface screens",
        "With the final deployment configuration",
    ], [
        "بالمكونات الأساسية والإجراءات الخدمية",
        "بمنسق النظام الأعلى الذي يحدد اتجاهه",
        "بترتيب شاشات واجهة المستخدم النهائية",
        "بتهيئة أجهزة النشر وتشغيل النظام",
    ]),
    "ch5_bottomup_direction": ([
        "Lower-level components combine to form larger structures",
        "Control paths are flattened sideways across modules",
        "System goals are divided downward into smaller functions",
        "User views are projected outward to external actors",
    ], [
        "تُجمع الأجزاء الدنيا باتجاه بنية أعلى",
        "تُسطح مسارات التحكم جانبياً عبر الوحدات",
        "تُفكك أهداف النظام إلى وظائف أدنى",
        "تُعرض مناظير المستخدم إلى جهات خارجية",
    ]),
    "ch5_bottomup_strength": ([
        "It can reuse existing low-level components and utilities",
        "It keeps every system goal visible from the start",
        "It avoids the need to integrate separate components",
        "It guarantees that all interfaces remain unchanged",
    ], [
        "إعادة استخدام أدوات ومكونات منخفضة المستوى موجودة",
        "إبقاء أهداف النظام كلها واضحة منذ البداية",
        "الاستغناء عن دمج الوحدات المنفصلة لاحقاً",
        "ضمان ثبات الواجهات طوال مراحل التطوير",
    ]),
    "ch5_bottomup_limit": ([
        "Early components may not fit later system goals",
        "Low-level components cannot be tested in isolation",
        "Existing utilities always create content coupling",
        "The approach cannot produce higher-level services",
    ], [
        "قد لا تلائم المكونات المبكرة أهداف النظام اللاحقة",
        "يصعب اختبار المكونات الأولية بمعزل عن النظام",
        "تسبب الأدوات الموجودة اقتران المحتوى دائماً",
        "يعجز النهج عن تقديم خدمات على مستوى أعلى",
    ]),
    "ch5_bottomup_integration": ([
        "Separate parts must ultimately fit the overall architecture",
        "Bottom-up work forbids interfaces between software parts",
        "Every utility must be rewritten before it can be tested",
        "Design begins only after all system parts are deployed",
    ], [
        "ينبغي أن تلائم الأجزاء المنفصلة معمارية النظام العامة",
        "يمنع النهج التصاعدي إنشاء واجهات بين المكونات",
        "تتطلب كل أداة إعادة كتابة قبل اختبارها",
        "يبدأ التصميم بعد نشر جميع مكونات النظام فقط",
    ]),
    "ch5_topdown_definition": ([
        "With the system's overall purpose and general structure",
        "With the smallest reusable utility in the system",
        "With a final diagram of the deployment hardware",
        "With detailed implementation of the data stores",
    ], [
        "بتحديد غرض النظام وبنيته العامة",
        "بأصغر إجراء خدمي قابل لإعادة الاستخدام",
        "بمخطط أجهزة النشر النهائي للنظام",
        "بتنفيذ تفصيلي لمخازن بيانات النظام",
    ]),
    "ch5_topdown_goal_focus": ([
        "The overall purpose stays visible during decomposition",
        "Test stubs are no longer needed during early checks",
        "The design no longer depends on stated requirements",
        "Every low-level library is available immediately",
    ], [
        "يبقى الغرض العام واضحاً أثناء تفكيك النظام",
        "تصبح بدائل الاختبار غير لازمة للفحص المبكر",
        "لا يعود التصميم معتمداً على المتطلبات المحددة",
        "تتوفر كل مكتبة منخفضة المستوى فور بدء التصميم",
    ]),
    "ch5_topdown_testing": ([
        "Stubs simulate subordinate routines that are not implemented yet",
        "Drivers invoke every missing higher-level caller instead",
        "Shared data replaces the interfaces between components",
        "Deployment nodes stand in for the complete system",
    ], [
        "تحاكي بدائل الاختبار الإجراءات التابعة غير المكتملة",
        "تستدعي برامج الاختبار الوظائف العليا المفقودة",
        "تحل البيانات المشتركة محل واجهات المكونات البرمجية",
        "تمثل عقد النشر المادية النظام بأكمله مؤقتاً",
    ]),
    "ch5_topdown_limit": ([
        "Integrating low-level libraries and hardware may happen later",
        "Communicating the architecture to software implementers",
        "Defining the system-wide goals and public interfaces",
        "Dividing behavior into progressively smaller functions",
    ], [
        "قد يتأخر دمج المكتبات والأجهزة منخفضة المستوى",
        "توضيح المعمارية لفرق التنفيذ البرمجية",
        "تحديد الأهداف العامة وواجهات النظام",
        "تقسيم السلوك إلى وظائف أصغر متتابعة",
    ]),
    "ch5_topdown_stepwise": ([
        "Stepwise refinement from general behavior to detail",
        "Coincidental cohesion among unrelated statements",
        "Transaction dispatch across alternative operations",
        "Shared global coupling between separate modules",
    ], [
        "تنقيح تدريجي يحول السلوك العام إلى تفاصيل",
        "تماسك عشوائي يجمع عبارات غير مترابطة",
        "توجيه المعاملات بين عمليات بديلة متعددة",
        "اقتران عام يربط وحدات برمجية منفصلة",
    ]),
    "ch5_topdown_vs_bottomup": ([
        "Top-down refines goals; bottom-up assembles basic parts",
        "Top-down assembles utilities; bottom-up divides system goals",
        "Top-down omits architecture; bottom-up omits components",
        "Both approaches begin by writing the source code",
    ], [
        "يفكك التنازلي الأهداف ويجمع التصاعدي الأجزاء",
        "يجمع التنازلي الأدوات ويفكك التصاعدي الأهداف",
        "يتجنب التنازلي المعمارية ويتجنب التصاعدي المكونات",
        "يبدأ النهجان ببرمجة النظام قبل وضع تصميمه",
    ]),
    "ch5_hybrid_definition": ([
        "Combining top-down and bottom-up design",
        "Using only the smallest available utility routines",
        "Dividing the system solely by user-interface screens",
        "Avoiding architectural decomposition altogether",
    ], [
        "الجمع بين التصميم التنازلي والتصاعدي",
        "استخدام الإجراءات الخدمية الأصغر المتاحة فقط",
        "تقسيم النظام بحسب شاشات واجهة المستخدم وحدها",
        "تجنب التفكيك المعماري لمكونات النظام كلياً",
    ]),
    "ch5_hybrid_topdown_role": ([
        "Overall system structure and its major responsibilities",
        "Detailed behavior of connected external hardware",
        "Internal implementation of every reused software library",
        "Final market price of each software component",
    ], [
        "بنية النظام العامة ومسؤولياته الرئيسة",
        "سلوك الأجهزة الخارجية المرتبطة بالنظام",
        "الشيفرة الداخلية لكل مكتبة مستخدمة",
        "السعر السوقي النهائي لكل مكون برمجي",
    ]),
    "ch5_hybrid_when": ([
        "When system goals and reusable components both matter",
        "When bottom-up design must ignore the system goals",
        "When top-down design must discard existing libraries",
        "When no available component can support the design",
    ], [
        "عندما تهم أهداف النظام والمكونات القابلة لإعادة الاستخدام معاً",
        "عندما يجب أن يتجاهل التصميم التصاعدي أهداف النظام",
        "عندما يجب أن يهمل التصميم التنازلي المكتبات الموجودة",
        "عندما لا يدعم التصميم أي مكون متاح مسبقاً",
    ]),
    "ch5_hybrid_balance": ([
        "System goals, architectural needs, and reusable components",
        "The number of developers sharing one programming language",
        "Preference for a newly released design notation",
        "Length of the final printed system description",
    ], [
        "أهداف النظام وحاجاته المعمارية والمكونات القابلة لإعادة الاستخدام",
        "عدد المطورين الذين يعملون بلغة برمجة واحدة",
        "تفضيل أحدث أساليب رسم مخططات التصميم",
        "حجم الوثيقة المطبوعة التي تصف النظام",
    ]),
    "ch5_hybrid_no_guarantee": ([
        "It combines two strategies without guaranteeing design success",
        "It separates the system from its user requirements",
        "It removes every integration and testing risk",
        "It always outperforms both strategies in every system",
    ], [
        "يجمع استراتيجيتين لكنه لا يضمن نجاح التصميم",
        "يفصل النظام عن حاجات المستخدم ومتطلباته",
        "يزيل مخاطر التكامل والاختبار كافة",
        "يتفوق دائماً على الاستراتيجيتين في كل نظام",
    ]),
    "ch5_hybrid_not_third_process": ([
        "It draws on both design directions within one effort",
        "It begins only after the system has been deployed",
        "It forbids reuse of previously built components",
        "It replaces design approaches with a testing process",
    ], [
        "يستفيد من الاتجاهين خلال جهد تصميم واحد",
        "يبدأ تطبيقه بعد اكتمال نشر النظام",
        "يمنع إعادة استخدام المكونات المبنية سابقاً",
        "يستبدل أساليب التصميم بعملية اختبار فقط",
    ]),
    "ch5_hybrid_architecture": ([
        "A design arrangement combining both decomposition directions",
        "A conceptual view of the system's user-visible behavior",
        "A classification of dependencies among software modules",
        "A cohesion pattern grouping tasks by execution time",
    ], [
        "ترتيب تصميم يجمع اتجاهي التفكيك والبناء",
        "منظور مفهومي يصف سلوك النظام الظاهر للمستخدمين",
        "تصنيف يوضح الاعتماد بين الوحدات البرمجية",
        "نمط تماسك يجمع المهام بحسب وقت تنفيذها",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_temporal_cohesion": ([
        "Temporal cohesion groups tasks by execution time",
        "Sequential cohesion passes output to the next task",
        "Functional cohesion serves one defined task",
        "Communicational cohesion groups tasks on shared data",
    ], [
        "التماسك الزمني يجمع المهام بحسب زمن تنفيذها",
        "التماسك التسلسلي يربط ناتج مهمة بما يليها",
        "التماسك الوظيفي يخدم هدفاً واحداً محدداً",
        "التماسك الاتصالي يجمع مهاماً تستخدم بيانات مشتركة",
    ]),
    "ch5_functional_cohesion": ([
        "Functional cohesion serves one defined purpose",
        "Elements share a convenient place in one source file",
        "Elements run together only during system startup",
        "A selector chooses one task from an unrelated group",
    ], [
        "التماسك الوظيفي يخدم غرضاً واحداً محدداً",
        "تشترك العناصر في موضع مناسب داخل ملف واحد",
        "تعمل العناصر معاً عند بدء النظام فقط",
        "يختار محدد عملية من مجموعة غير مترابطة",
    ]),
    "ch5_communicational_cohesion": ([
        "Communicational cohesion groups tasks that use shared data",
        "Procedural cohesion links operations by their execution order",
        "Coincidental cohesion groups elements without a shared purpose",
        "Sequential cohesion links one operation's output to the next input",
    ], [
        "التماسك الاتصالي يجمع مهاماً تستخدم بيانات مشتركة",
        "التماسك الإجرائي يربط عمليات بترتيب تنفيذها",
        "التماسك العشوائي يضم عناصر لا يجمعها هدف مشترك",
        "التماسك التسلسلي يربط خرج عملية بمدخل التالية",
    ]),
    "ch5_cc_design_target": ([
        "High cohesion within modules and low coupling between them",
        "Low cohesion within modules and high coupling between them",
        "High cohesion and high coupling across all components",
        "Low cohesion and low coupling inside each component",
    ], [
        "تماسك عالٍ داخل الوحدات واقتران منخفض بين مكوناتها",
        "تماسك منخفض داخل الوحدات واقتران عالٍ بين مكوناتها",
        "تماسك عالٍ واقتران عالٍ بين جميع مكونات النظام",
        "تماسك منخفض واقتران منخفض داخل كل مكون برمجي",
    ]),
    "ch5_cc_high_coupling": ([
        "A change can spread through components that depend on it",
        "A focused component may lose its single defined purpose",
        "Every interface becomes hidden from its users and callers",
        "The system loses its ability to exchange data altogether",
    ], [
        "قد يمتد أثر التغيير إلى الوحدات المعتمدة على المكون",
        "قد يفقد المكون المركز غرضه الوظيفي الواحد",
        "تُحجب الواجهات عن الجهات التي تستدعي المكونات",
        "يفقد النظام قدرته على تبادل البيانات بين وحداته",
    ]),
    "ch5_cc_information_hiding": ([
        "Callers rely on a stable interface, not internal details",
        "Every caller must change whenever internal data changes",
        "All components must share the hidden state of this component",
        "The system can operate without communication among components",
    ], [
        "يعتمد المستدعون على واجهة ثابتة لا على تفاصيل التمثيل",
        "يجب أن يتغير كل مستدعٍ عند تغير البيانات الداخلية",
        "تتشارك المكونات الحالة الداخلية المخفية لهذا المكون",
        "يعمل النظام من دون تواصل بين مكوناته البرمجية",
    ]),
    "ch5_strategy_definition": ([
        "How a system is divided into parts and assembled",
        "How project funds are reviewed and approved",
        "How users are selected for acceptance testing",
        "How a released service is promoted to customers",
    ], [
        "تفكيك النظام إلى أجزاء ثم تجميعها",
        "مراجعة ميزانية المشروع واعتمادها",
        "اختيار المستخدمين لإجراء اختبار القبول",
        "تسويق الخدمة بعد إطلاقها للعملاء",
    ]),
    "ch5_strategy_topdown_focus": ([
        "The system's high-level goals and overall structure",
        "The internal state of each object in the system",
        "The interface colors preferred by system users",
        "The lowest library details without system context",
    ], [
        "أهداف النظام العليا وبنيته التنظيمية",
        "الحالة الداخلية لكل كائن ضمن النظام",
        "ألوان الواجهات التي يفضلها المستخدمون عادةً",
        "تفاصيل المكتبات الدنيا بمعزل عن أهداف النظام",
    ]),
    "ch5_strategy_hybrid": ([
        "It combines system goals with suitable existing components",
        "It replaces system goals with disconnected utility routines",
        "It uses only classes and rejects procedural components",
        "It delays structural choices until the product is released",
    ], [
        "يجمع أهداف النظام مع مكونات موجودة وملائمة",
        "يستبدل أهداف النظام بإجراءات خدمية منفصلة",
        "يستخدم الأصناف وحدها ويرفض المكونات الإجرائية",
        "يؤجل القرارات البنيوية إلى ما بعد إصدار المنتج",
    ]),
    "ch5_strategy_not_design": ([
        "Embedded design places software within a physical device",
        "Hybrid design combines top-down and bottom-up directions",
        "Top-down design refines system goals into lower-level details",
        "Bottom-up design combines basic parts into larger systems",
    ], [
        "التصميم المضمن يضع البرمجيات داخل جهاز مادي",
        "التصميم الهجين يجمع اتجاهي التصميم",
        "التصميم التنازلي ينقح أهداف النظام إلى تفاصيل أدنى",
        "التصميم التصاعدي يركب الأجزاء لبناء أنظمة أكبر",
    ]),
    "ch5_strategy_select": ([
        "Hybrid design respects system goals and reuses suitable parts",
        "No strategy applies to a project with existing components",
        "Bottom-up design ignores all system goals during construction",
        "Top-down design discards every available utility component",
    ], [
        "يجمع الهجين أهداف النظام والأدوات المناسبة",
        "لا تلائم المكونات الجاهزة أياً من اتجاهات التصميم",
        "يتجاهل التصاعدي أهداف النظام العامة عند البناء",
        "يهمل التنازلي الأدوات المتاحة ويعيد بناءها",
    ]),
})

EXPECTED_CORRECT_FIRST["ch5_conceptual_technical_translation"] = "Translate user needs into an implementable design"

BALANCED_OPTIONS.update({
    "ch5_bottomup_strength": ([
        "It can reuse existing low-level components and utilities",
        "It keeps every system goal visible from the start",
        "It avoids the need to integrate separate components",
        "It guarantees that all interfaces remain unchanged",
    ], [
        "إمكان إعادة استخدام مكونات منخفضة المستوى",
        "الحفاظ على أهداف النظام واضحة منذ البداية",
        "الاستغناء عن دمج الوحدات المنفصلة لاحقاً",
        "ضمان ثبات واجهات النظام طوال التطوير",
    ]),
    "ch5_bottomup_limit": ([
        "Early components may not fit later system goals",
        "Low-level components cannot be tested in isolation",
        "Existing utilities always create content coupling",
        "The approach cannot produce higher-level services",
    ], [
        "قد لا تلائم المكونات الأولى أهداف النظام اللاحقة",
        "يصعب اختبار المكونات منخفضة المستوى بصورة مستقلة",
        "تسبب الأدوات المستخدمة اقتران المحتوى دائماً",
        "يعجز النهج عن تقديم خدمات على مستوى أعلى",
    ]),
    "ch5_bottomup_integration": ([
        "Separate parts must ultimately fit the overall architecture",
        "Bottom-up work forbids interfaces between software parts",
        "Every utility must be rewritten before it can be tested",
        "Design begins only after all system parts are deployed",
    ], [
        "تلائم الأجزاء المنفصلة المعمارية العامة للنظام",
        "يمنع النهج التصاعدي إنشاء واجهات بين المكونات",
        "تستلزم كل أداة برمجية إعادة كتابة قبل اختبارها",
        "يبدأ التصميم بعد نشر جميع مكونات النظام فقط",
    ]),
    "ch5_topdown_definition": ([
        "With the system's overall goals and architecture",
        "With the smallest reusable utility in the system",
        "With a final diagram of deployment hardware and sites",
        "With detailed implementation of the system's data stores",
    ], [
        "بالبدء من غرض النظام وبنيته العامة",
        "بأصغر إجراء خدمي قابل لإعادة الاستخدام",
        "بمخطط أجهزة النشر ومواقعه النهائي للنظام",
        "بتنفيذ تفصيلي لمخازن بيانات النظام",
    ]),
    "ch5_topdown_testing": ([
        "Stubs stand in for subordinate routines that are unfinished",
        "Drivers invoke every missing higher-level caller instead",
        "Shared data replaces the interfaces between components",
        "Deployment nodes stand in for the complete system",
    ], [
        "تحاكي بدائل الاختبار الإجراءات التابعة غير المكتملة",
        "تستدعي برامج الاختبار الوظائف العليا المفقودة",
        "تحل البيانات المشتركة محل واجهات المكونات البرمجية",
        "تمثل عقد النشر المادية النظام بأكمله مؤقتاً",
    ]),
    "ch5_topdown_limit": ([
        "Integrating low-level assets may occur at a later stage",
        "Communicating the architecture to software implementers",
        "Defining the system-wide goals and public interfaces",
        "Dividing behavior into progressively smaller functions",
    ], [
        "قد يتأخر دمج مكتبات المستوى الأدنى والأجهزة",
        "توضيح قرارات المعمارية لفرق التنفيذ البرمجية",
        "تحديد الأهداف العامة وواجهات النظام",
        "تقسيم السلوك إلى وظائف أصغر متتابعة",
    ]),
    "ch5_hybrid_definition": ([
        "Hybrid design combines top-down and bottom-up reasoning",
        "Bottom-up design uses low-level parts but ignores system goals",
        "Top-down design divides behavior but rejects reusable parts",
        "Screen-based design divides a system only by visible pages",
    ], [
        "التصميم الهجين يجمع النهجين التنازلي والتصاعدي",
        "يبدأ التصاعدي بمكونات دنيا بلا توجيه شامل للنظام",
        "يفكك التنازلي الأهداف ويرفض الأجزاء القابلة لإعادة الاستخدام",
        "يقسم التصميم المعتمد على الشاشات النظام بحسب صفحاته الظاهرة",
    ]),
    "ch5_hybrid_when": ([
        "When system goals and reusable components both matter",
        "When bottom-up design must ignore the system goals",
        "When top-down design must discard existing libraries",
        "When no available component can support the design",
    ], [
        "عند الجمع بين أهداف النظام ومكونات جاهزة ملائمة",
        "حين يتجاهل النهج التصاعدي أهداف النظام العليا",
        "حين يهمل النهج التنازلي مكتبات موجودة وملائمة",
        "عند غياب مكونات جاهزة تلائم متطلبات النظام",
    ]),
    "ch5_hybrid_balance": ([
        "System requirements, architectural needs, and available components",
        "The number of developers sharing one programming language",
        "Preference for a newly released design notation",
        "Length of the final printed system description",
    ], [
        "متطلبات النظام ومعماريته والمكونات المناسبة المتاحة",
        "عدد المطورين في الفريق وتقاسمهم لغة برمجية واحدة",
        "الرغبة في اعتماد أحدث أسلوب لرسم مخطط التصميم",
        "عدد صفحات الوثيقة النهائية المعدة للطباعة",
    ]),
    "ch5_hybrid_no_guarantee": ([
        "It combines two strategies but cannot ensure success",
        "It separates the system from its user requirements",
        "It removes every integration and testing risk",
        "It always outperforms both strategies in every system",
    ], [
        "يجمع نهجين لكنه لا يضمن نجاح التصميم",
        "يفصل النظام عن حاجات المستخدم ومتطلباته",
        "يزيل مخاطر التكامل والاختبار كلها",
        "يتفوق دائماً على الاستراتيجيتين في كل نظام",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_cc_high_coupling": ([
        "A focused component may lose its single defined purpose",
        "Every interface becomes hidden from its users and callers",
        "The system loses its ability to exchange data altogether",
        "A change can ripple into components that depend on it",
    ], [
        "قد يفقد المكون المركز غرضه الوظيفي الواحد",
        "تُحجب الواجهات عن الجهات التي تستدعي المكونات",
        "يفقد النظام قدرته على تبادل البيانات بين وحداته",
        "قد يمتد أثر التغيير إلى الوحدات التي تعتمد عليه",
    ]),
    "ch5_strategy_not_design": ([
        "Embedded design places software within a physical device",
        "Hybrid design combines top-down and bottom-up directions",
        "Top-down design refines system goals into lower-level details",
        "Bottom-up design combines basic parts into larger systems",
    ], [
        "التصميم المضمن يضع البرمجيات داخل جهاز مادي",
        "التصميم الهجين يجمع اتجاهي التطوير والتصميم",
        "التصميم التنازلي ينقح أهداف النظام إلى تفاصيل أدنى",
        "التصميم التصاعدي يركب الأجزاء لبناء أنظمة أكبر",
    ]),
    "ch5_topdown_limit": ([
        "Integrating low-level assets may occur at a later stage",
        "Communicating the architecture to software implementers",
        "Defining the system-wide goals and public interfaces",
        "Dividing behavior into progressively smaller functions",
    ], [
        "قد يتأخر دمج مكتبات المستوى الأدنى والأجهزة",
        "توضيح قرارات المعمارية لفرق التنفيذ البرمجية",
        "تحديد الأهداف العامة وواجهات النظام",
        "تقسيم وظائف النظام إلى أعمال أصغر متتابعة",
    ]),
    "ch5_hybrid_definition": ([
        "Hybrid design combines top-down and bottom-up reasoning",
        "Bottom-up design uses low-level parts but ignores system goals",
        "Top-down design divides behavior but rejects reusable parts",
        "Screen-based design divides a system only by visible pages",
    ], [
        "يجمع التصميم الهجين بين الاتجاهين التنازلي والتصاعدي",
        "يبدأ التصاعدي بمكونات دنيا بلا توجيه شامل للنظام",
        "يفكك التنازلي النظام لكنه يهمل المكونات الموجودة",
        "يقسم التصميم المعتمد على الشاشات النظام إلى واجهات",
    ]),
    "ch5_hybrid_balance": ([
        "System needs, architecture, and reusable components",
        "The number of developers sharing one programming language",
        "Preference for a newly released design notation",
        "Length of the final printed system description",
    ], [
        "حاجات النظام ومعماريته والمكونات المتاحة",
        "عدد المطورين في الفريق وتقاسمهم لغة برمجية واحدة",
        "الرغبة في اعتماد أحدث أسلوب لرسم مخطط التصميم",
        "عدد صفحات الوثيقة النهائية المعدة للطباعة",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_fod_definition": ([
        "Functions and their procedural hierarchy",
        "Objects and their identity relationships",
        "Hardware nodes and deployment locations",
        "User stories and project release dates",
    ], [
        "الوظائف وتفكيكها الإجرائي",
        "الكائنات وعلاقات هويتها",
        "العقد المادية ومواقع نشرها",
        "قصص المستخدم ومواعيد الإصدارات",
    ]),
    "ch5_fod_data_separation": ([
        "Data structures and their related procedures",
        "Requirements and boundaries across external systems",
        "Component nodes and the physical machines hosting them",
        "Class identity and its runtime object instances",
    ], [
        "بنى البيانات والإجراءات المرتبطة باستخدامها",
        "متطلبات النظام وحدوده مع الأنظمة الخارجية",
        "عقد المكونات والحواسيب المادية التي تستضيفها",
        "هوية الصنف والنسخ المنشأة منه أثناء التشغيل",
    ]),
    "ch5_fod_dfd": ([
        "Data Flow Diagram",
        "Structure Chart",
        "Use-Case Diagram",
        "Deployment Diagram",
    ], [
        "مخطط يوضح تدفق البيانات",
        "مخطط يوضح بنية الوحدات البرمجية",
        "مخطط يوضح حالات الاستخدام",
        "مخطط يوضح عقد النشر",
    ]),
    "ch5_fod_structure_chart": ([
        "Structure Chart",
        "Data Flow Diagram",
        "State Diagram",
        "Deployment Diagram",
    ], [
        "مخطط يوضح بنية الوحدات البرمجية",
        "مخطط يوضح حركة البيانات وتحولاتها",
        "مخطط يوضح تغير حالة الكائن",
        "مخطط يوضح توزيع البرمجيات على الأجهزة",
    ]),
    "ch5_procedural_abstraction": ([
        "Procedural abstraction through a named operation",
        "Control abstraction across structured execution paths",
        "Deployment abstraction over physical computing nodes",
        "Data abstraction around hidden stored representation",
    ], [
        "التجريد الإجرائي عبر عملية ذات اسم واضح",
        "تجريد التحكم عبر مسارات تنفيذ منظمة",
        "تجريد النشر عبر عقد الحوسبة المادية",
        "تجريد البيانات حول تمثيل مخزن مخفي",
    ]),
    "ch5_dfd_view": ([
        "Data movement, stores, and transformations",
        "Module calls and their control hierarchy",
        "Object states and behavior over time",
        "Physical nodes and allocation of hardware",
    ], [
        "حركة البيانات ومخازنها والتحولات التي تجري عليها",
        "استدعاءات الوحدات وتسلسل التحكم بينها",
        "حالات الكائنات والسلوك المرتبط بمرور الزمن",
        "توزيع الأجهزة والعقد المادية على مواقع النشر",
    ]),
    "ch5_structure_chart_view": ([
        "Procedural control and module invocation hierarchy",
        "User goals and actors at the system boundary",
        "Data stores and exchanges with external sources",
        "Physical machines and their deployment locations",
    ], [
        "التحكم الإجرائي وترتيب استدعاء الوحدات",
        "أهداف المستخدم والجهات خارج حدود النظام",
        "مخازن البيانات وتبادلها مع الجهات الخارجية",
        "الأجهزة المادية ومواقع تشغيل النظام",
    ]),
    "ch5_static_dynamic_notations": ([
        "Class diagram for structure; sequence diagram for behavior",
        "Structure chart with data dictionary",
        "Data-flow diagram with deployment view",
        "Flowchart for control; class diagram for object structure",
    ], [
        "مخطط الأصناف للبنية ومخطط التسلسل للسلوك",
        "مخطط البنية مع قاموس تعريفات البيانات",
        "مخطط تدفق البيانات مع منظور النشر",
        "مخطط التدفق للتحكم ومخطط الأصناف للبنية",
    ]),
    "ch5_notation_stakeholders": ([
        "A use-case view showing actor goals and system services",
        "A procedure body listing local variables and operations",
        "A detailed flowchart tracing algorithmic decisions",
        "A deployment view mapping processors to system nodes",
    ], [
        "منظور حالات الاستخدام لأهداف الجهات وخدمات النظام",
        "جسم إجراء يحدد المتغيرات المحلية والعمليات",
        "مخطط تدفق يتتبع خطوات الخوارزمية وقراراتها",
        "منظور نشر يحدد مواقع المعالجات والعقد",
    ]),
    "ch5_transform_transaction": ([
        "A transaction tag selects one path from several alternatives",
        "A continuous flow passes through one central transform",
        "A specialized class inherits attributes from a general class",
        "A sequence diagram orders messages exchanged by objects",
    ], [
        "تحدد علامة المعاملة المسار المناسب من مسارات عدة",
        "يمر تدفق البيانات عبر تحويل مركزي واحد",
        "يرث الصنف المتخصص سمات من صنف عام",
        "يرتب مخطط التسلسل الرسائل المتبادلة بين الكائنات",
    ]),
    "ch5_procedure_level1": ([
        "The interface, calls, and side-effects level",
        "The detailed procedure body and its implementation notation",
        "The system deployment description and physical locations",
        "The local data structures and timing constraints level",
    ], [
        "مستوى الواجهة والاستدعاءات والآثار الجانبية",
        "مستوى تفاصيل جسم الإجراء وشفرة تنفيذه",
        "مستوى وصف النشر ومواقع النظام المادية",
        "مستوى البيانات المحلية وقيود وقت التنفيذ",
    ]),
    "ch5_procedure_level2": ([
        "At the level of local data, timing, and exception limits",
        "At the level of the procedure's purpose and role",
        "At the level of call parameters and external effects",
        "At the level of physical deployment nodes and sites",
    ], [
        "في مستوى البيانات والقيود المحلية",
        "في مستوى هدف الإجراء ووظيفته",
        "في مستوى معاملات الإجراء وواجهته",
        "في مستوى عقد النشر وتوزيع الأجهزة",
    ]),
    "ch5_procedure_level3": ([
        "The detailed procedure body in a suitable notation",
        "The procedure name and its position in the system",
        "The callers, parameters, and interface assertions",
        "The module hierarchy and external protocols",
    ], [
        "تفاصيل جسم الإجراء بترميز مناسب",
        "اسم الإجراء وموضعه ضمن بنية النظام",
        "المستدعون والمعاملات وتأكيدات الواجهة",
        "تسلسل الوحدات والبروتوكولات الخارجية",
    ]),
    "ch5_procedure_not_arch_layers": ([
        "Increasing detail levels for one procedure description",
        "Four coupling categories between separate modules",
        "Separate architectural tiers throughout the full system",
        "Different stages of a software product release",
    ], [
        "مستويات تفاصيل متزايدة لوصف إجراء واحد",
        "أربعة أنواع اقتران بين وحدات منفصلة",
        "طبقات معمارية منفصلة في النظام بأكمله",
        "مراحل مختلفة لإصدار المنتج البرمجي",
    ]),
    "ch5_procedure_level1_vs2": ([
        "Level one covers interfaces; level two covers local constraints",
        "Level one covers deployment; level two covers user workflows",
        "Level one covers data stores; level two covers module calls",
        "Level one covers code bodies; level two covers system goals",
    ], [
        "يغطي الأول الواجهات والثاني القيود المحلية",
        "يغطي الأول النشر والثاني إجراءات المستخدم",
        "يغطي الأول المخازن والثاني استدعاء الوحدات",
        "يغطي الأول أجسام الشيفرة والثاني أهداف النظام",
    ]),
    "ch5_procedure_notation_choice": ([
        "Pseudocode or a flowchart for the detailed procedure body",
        "A system scope statement without procedural behavior",
        "A deployment map showing physical nodes only",
        "A list of user actors without any procedure details",
    ], [
        "شيفرة وصفية أو مخطط تدفق لتفاصيل جسم الإجراء",
        "بيان نطاق النظام من دون وصف السلوك الإجرائي",
        "خريطة نشر توضح العقد المادية وحدها",
        "قائمة بالجهات المستخدمة من دون تفاصيل الإجراءات",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_ieee_edition": ([
        "The nineteen ninety-eight revision",
        "The two thousand nine revision",
        "The two thousand sixteen revision",
        "The nineteen ninety-five revision",
    ], [
        "مراجعة IEEE 1016 لعام ألف وتسعمئة وثمانية وتسعين",
        "مراجعة IEEE 1016 لعام ألفين وتسعة في تحديث لاحق",
        "مراجعة IEEE 1016 لعام ألفين وستة عشر في تحديث لاحق",
        "مراجعة IEEE 1016 لعام ألف وتسعمئة وخمسة وتسعين",
    ]),
    "ch5_ieee_role": ([
        "SDD information content, structure, and organization",
        "The interface colors and release branding for a product",
        "The programming language and compiler settings to use",
        "The project budget and staffing plan for development",
    ], [
        "محتوى SDD وبنية وثيقة التصميم وطريقة تنظيمها",
        "ألوان الواجهة وهوية إصدار المنتج وتنسيقها",
        "لغة البرمجة وخيارات المترجم وإعداداتها",
        "ميزانية المشروع وخطة الموارد والجدول الزمني",
    ]),
    "ch5_ieee_recommended": ([
        "A recommended practice describing software design descriptions",
        "A cost-estimation model for software project planning",
        "A deployment protocol for web applications and services",
        "A mandatory standard for programming languages",
    ], [
        "ممارسة موصى بها لوصف تصميم البرمجيات وتنظيم معلوماته",
        "نموذج لتقدير كلفة المشروع وموارده وخطة عمله",
        "بروتوكول لنشر تطبيقات الويب وخدماتها وإدارتها",
        "معيار إلزامي لتوحيد لغات البرمجة وإعدادها",
    ]),
    "ch5_ieee_audience": ([
        "Developers, testers, and maintainers of the software",
        "Customers who select the interface colors only",
        "Marketing and finance teams without implementation staff",
        "The original authors of requirements and specifications",
    ], [
        "المطورون والمختبرون وفرق صيانة البرمجيات",
        "عملاء يختارون ألوان الواجهات حصراً",
        "فريق التسويق والمالية دون فرق التنفيذ",
        "المؤلفون الأصليون لمتطلبات النظام ومواصفاته",
    ]),
    "ch5_ieee_lineage": ([
        "Keep the stated edition distinct from later revisions",
        "Replace it with the newest edition without explanation",
        "Treat every standard edition as the same document",
        "Omit the revision whenever the standard is named",
    ], [
        "تمييز الإصدار المذكور عن مراجعات المعيار اللاحقة",
        "استبدال الإصدار بالأحدث من دون توضيح",
        "اعتبار مراجعات المعيار وثيقة واحدة متطابقة",
        "حذف رقم المراجعة كلما ذُكر المعيار",
    ]),
    "ch5_sdd_scope_applicability": ([
        "Its applicability to software design descriptions",
        "The programming language required for every project",
        "A mandatory top-down design procedure for systems",
        "One interface notation required across all systems",
    ], [
        "انطباق الممارسة على أوصاف تصميم البرمجيات",
        "اللغة البرمجية المحددة والمستخدمة في كل مشروع",
        "إلزام جميع المشاريع بإجراءات تصميم تنازلي",
        "اعتماد ترميز واحد لواجهات جميع الأنظمة",
    ]),
    "ch5_sdd_scope_content": ([
        "Required SDD information and how the description is organized",
        "User training plans and software release scheduling",
        "Project costs, work estimates, and staff assignments",
        "Source-code style rules and compiler configuration",
    ], [
        "محتوى المعلومات المطلوبة وكيفية تنظيمها داخل SDD",
        "خطط تدريب المستخدم وجدولة إصدار البرمجيات",
        "كلف المشروع وتقديرات العمل وتوزيع الموظفين",
        "قواعد تنسيق الشيفرة وإعداد المترجم البرمجي",
    ]),
    "ch5_sdd_scope_methodology": ([
        "No, it does not mandate a design methodology",
        "Yes, it requires one functional notation",
        "No, it addresses only source-code layout",
        "Yes, it excludes object-oriented design",
    ], [
        "لا، فهو لا يفرض منهجية محددة للتصميم",
        "نعم، يفرض ترميزاً وظيفياً واحداً",
        "لا، فهو يخص تنسيق الشيفرة فقط",
        "نعم، يستبعد التصميم الموجه بالكائنات",
    ]),
    "ch5_sdd_scope_ood": ([
        "Yes, the scope is independent of design method",
        "No, it covers function-oriented systems only",
        "No, it excludes systems that contain classes",
        "Yes, after the system's source code is complete",
    ], [
        "نعم، فالنطاق مستقل عن منهجية التصميم",
        "لا، فالنطاق يقتصر على الأنظمة الوظيفية",
        "لا، فالنطاق يستبعد الأنظمة التي تضم أصنافاً",
        "نعم، بعد أن تكتمل برمجة النظام بالكامل",
    ]),
    "ch5_sdd_scope_domains": ([
        "None of the listed application domains is excluded",
        "Commercial software is the only excluded domain",
        "Embedded software is the only excluded domain",
        "Scientific software is the only excluded domain",
    ], [
        "لا يستثني أياً من مجالات التطبيق المذكورة",
        "البرمجيات التجارية وحدها مستثناة من النطاق",
        "البرمجيات المضمنة وحدها مستثناة من النطاق",
        "البرمجيات العلمية وحدها مستثناة من النطاق",
    ]),
    "ch5_sdd_scope_not_lifecycle": ([
        "It prescribes one mandatory software development lifecycle",
        "It is independent of a specific design methodology",
        "It defines SDD information and its arrangement",
        "It applies across several software application domains",
    ], [
        "يفرض دورة تطوير برمجيات واحدة إلزامية للمشاريع",
        "يستقل عن منهجية تصميم محددة للنظام",
        "يحدد معلومات SDD وطريقة ترتيبها",
        "ينطبق على مجالات متعددة للتطبيقات البرمجية",
    ]),
    "ch5_sdd_scope_not_language": ([
        "Compiler settings used when implementing software",
        "The organization of design information in an SDD",
        "The information included in the design description",
        "Applicability of design descriptions across systems",
    ], [
        "إعدادات المترجم المستخدمة عند تنفيذ البرمجيات",
        "تنظيم معلومات التصميم داخل وصف البرمجيات",
        "المعلومات التي يتضمنها وصف تصميم البرمجيات",
        "مجالات انطباق أوصاف التصميم البرمجي",
    ]),
    "ch5_sdd_scope_use": ([
        "Its design methodology and modeling approach",
        "Whether to describe any design information at all",
        "Whether to organize required content in the SDD",
        "Whether an SDD is a description of software design",
    ], [
        "منهجية التصميم وأسلوب النمذجة المتبع",
        "ما إذا كان سيصف معلومات التصميم أصلاً",
        "ما إذا كان سينظم المحتوى المطلوب في SDD",
        "ما إذا كان SDD وصفاً لتصميم البرمجيات",
    ]),
    "ch5_design_entity_definition": ([
        "A distinct structural element represented in the design description",
        "A complete user story awaiting formal project approval",
        "A physical server hosting a running software application",
        "A change request filed after a product has been released",
    ], [
        "عنصر بنيوي مميز ممثل في وثيقة التصميم",
        "قصة مستخدم كاملة تنتظر اعتماد المشروع رسمياً",
        "خادم مادي يستضيف تطبيقاً برمجياً قيد التشغيل",
        "طلب تغيير مقدم بعد إصدار المنتج البرمجي",
    ]),
    "ch5_design_view_definition": ([
        "Attributes organized around a particular design concern",
        "Only the external data entering the software system",
        "Every source file arranged in deployment order",
        "All project users who approve a delivery plan",
    ], [
        "سمات منظمة لمعالجة جانب محدد من التصميم",
        "البيانات الخارجية الداخلة إلى النظام البرمجي فقط",
        "ملفات الشيفرة كلها مرتبة حسب تسلسل النشر",
        "مستخدمو المشروع الذين يعتمدون خطة التسليم",
    ]),
    "ch5_sdd_definition": ([
        "A technical description of software design information",
        "A user survey that measures system performance",
        "A project plan listing staff, cost, and delivery dates",
        "An executable program delivered to software users",
    ], [
        "وصف فني لمعلومات تصميم النظام البرمجي",
        "استطلاع مستخدم يقيس أداء النظام البرمجي",
        "خطة مشروع توضح الموارد والكلفة ومواعيد التسليم",
        "برنامج تنفيذي يقدم إلى مستخدمي النظام",
    ]),
    "ch5_entity_vs_view": ([
        "An entity is described; a view groups attributes by concern",
        "An entity is a project team; a view is its delivery schedule",
        "An entity is a test stage; a view is a release package",
        "An entity is a user role; a view is the project plan",
    ], [
        "الكيان عنصر بنيوي والمنظور يجمع سمات جانب محدد",
        "الكيان فريق عمل والمنظور جدول مواعيد التسليم",
        "الكيان مرحلة اختبار والمنظور حزمة الإصدار",
        "الكيان دور مستخدم والمنظور خطة المشروع",
    ]),
    "ch5_entity_examples": ([
        "A subsystem with defined structural responsibilities",
        "A meeting invitation distributed to the project team",
        "A project budget total without any software element",
        "A user complaint with no design response attached",
    ], [
        "نظام فرعي له مسؤوليات بنيوية محددة داخل النظام",
        "دعوة اجتماع موزعة على أعضاء فريق المشروع",
        "مجموع ميزانية مشروع بلا عنصر برمجي محدد",
        "شكوى مستخدم بلا استجابة تصميمية مرتبطة بها",
    ]),
    "ch5_view_not_diagram": ([
        "An organized subset of design information for one concern",
        "One mandatory drawing containing the entire software system",
        "A complete list of project risks and their controls",
        "A compiled version of one software component",
    ], [
        "مجموعة منظمة من معلومات التصميم لجانب معين",
        "رسم إلزامي واحد يضم أجزاء النظام البرمجي كلها",
        "قائمة شاملة بمخاطر المشروع وإجراءات ضبطها",
        "نسخة مترجمة من مكون برمجي جاهز للتشغيل",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_sdd_purpose": ([
        "Guide implementation with an authoritative technical design description",
        "Replace stated requirements with executable application code",
        "Record only defects discovered after software release",
        "Select the commercial pricing model used by the customer",
    ], [
        "توجيه التنفيذ بوصف فني معتمد لقرارات تصميم البرمجيات",
        "استبدال المتطلبات المحددة بشيفرة التطبيق القابلة للتشغيل",
        "تسجيل العيوب التي تظهر بعد إصدار البرمجيات فقط",
        "اختيار نموذج التسعير التجاري الذي يعتمده العميل",
    ]),
    "ch5_sdd_implementation": ([
        "The documented interface decision for the disputed components",
        "An unrelated budget for deploying the software system",
        "A replacement user requirement that was not reviewed",
        "A marketing plan prepared after the product release",
    ], [
        "قرار الواجهة الموثق للمكونات موضع الاختلاف",
        "ميزانية غير مرتبطة بنشر النظام البرمجي",
        "متطلب مستخدم بديل لم يخضع للمراجعة",
        "خطة تسويقية أعدت بعد إصدار المنتج",
    ]),
    "ch5_sdd_verification": ([
        "It provides a baseline to compare the design with requirements",
        "It measures only runtime speed after implementation is complete",
        "It converts test outcomes into new user stories for the project",
        "It removes the need to retain written system requirements",
    ], [
        "يوفر أساساً لمقارنة التصميم بمتطلبات النظام",
        "يقيس سرعة التشغيل بعد اكتمال التنفيذ فقط",
        "يحول نتائج الاختبار إلى قصص مستخدم جديدة للمشروع",
        "يلغي الحاجة إلى الاحتفاظ بمتطلبات النظام المكتوبة",
    ]),
    "ch5_sdd_maintenance": ([
        "It preserves technical design information for later maintenance",
        "It prevents every possible requirement change in the future",
        "It replaces all software tests performed after initial delivery",
        "It contains the only valid copy of the program source code",
    ], [
        "يحفظ معلومات التصميم الفني لأعمال الصيانة اللاحقة",
        "يمنع كل تغيير محتمل في المتطلبات مستقبلاً",
        "يستبدل اختبارات البرمجيات بعد التسليم الأولي كلها",
        "يحتوي النسخة الوحيدة المعتمدة من ملفات البرنامج",
    ]),
    "ch5_sdd_guessing": ([
        "It states the architectural and interface decisions for builders",
        "It lists user complaints without recording any design resolution",
        "It lets each implementation team invent an incompatible interface",
        "It hides the responsibilities assigned to each software component",
    ], [
        "يوضح القرارات المعمارية وقرارات الواجهة للمنفذين",
        "يسرد شكاوى المستخدم من دون توثيق حلول تصميمية",
        "يتيح لكل فريق تنفيذ ابتكار واجهة غير متوافقة",
        "يخفي المسؤوليات المسندة إلى كل مكون برمجي",
    ]),
    "ch5_sdd_not_code": ([
        "It guides implementation but is not executable software",
        "It guarantees that the implemented system has no defects",
        "It removes the need to review the software design",
        "It is the final running product delivered to customers",
    ], [
        "يوجه التنفيذ لكنه ليس برنامجاً قابلاً للتشغيل",
        "يضمن خلو النظام المنفذ من العيوب البرمجية",
        "يلغي الحاجة إلى مراجعة التصميم البرمجي",
        "يمثل المنتج النهائي العامل الذي يسلم للعملاء",
    ]),
    "ch5_sdd_audience_purpose": ([
        "Communicating technical design decisions to later project teams",
        "Setting the initial commercial price paid by software users",
        "Approving annual leave requests for software developers",
        "Selecting the organization's hiring policy for new staff",
    ], [
        "إيصال قرارات التصميم الفني إلى فرق المشروع اللاحقة",
        "تحديد السعر التجاري الأولي الذي يدفعه مستخدمو النظام",
        "اعتماد طلبات الإجازة السنوية لمطوري البرمجيات",
        "اختيار سياسة التوظيف للمؤسسة والموارد الجديدة",
    ]),
    "ch5_sdd_attributes_set": ([
        "Identification, type, purpose, function, subordinates, dependencies, interfaces, resources, processing, data",
        "Actors, use cases, activities, messages, classes, states, components, deployment nodes, packages, tests",
        "Project cost, effort, duration, schedule, staffing, risks, quality, budget, market, release planning",
        "Data inputs, outputs, storage, control, timing, ownership, security, workload, pricing, operating policy",
    ], [
        "التعريف والنوع والغرض والوظيفة والتابعون والاعتماديات والواجهات والموارد والمعالجة والبيانات",
        "الجهات وحالات الاستخدام والأنشطة والتفاعلات والأصناف والحالات والمكونات والعقد والحزم والاختبارات",
        "كلفة المشروع والجهد والمدة والجدول والموارد والمخاطر والجودة والميزانية والسوق وموعد الإصدار",
        "مدخلات البيانات ومخرجات النظام والخزن والتحكم ووقت التنفيذ والملكية وأمن الوصول وعبء العمل والكلفة والسياسة",
    ]),
    "ch5_sdd_entity_identifier": ([
        "Identification: the entity's name and unique identity",
        "Dependencies: other design elements the entity relies on",
        "Processing: the operations performed by the design entity",
        "Resources: facilities and inputs required by the entity",
    ], [
        "التعريف: اسم الكيان وهويته المميزة",
        "الاعتماديات: عناصر تصميم يعتمد عليها الكيان",
        "المعالجة: العمليات التي يؤديها كيان التصميم",
        "الموارد: الوسائل والمدخلات التي يحتاج إليها الكيان",
    ]),
    "ch5_sdd_entity_interface": ([
        "Interface: the entity's communication with other design elements",
        "Processing: the internal operations performed by the entity",
        "Resources: the facilities and inputs needed for its operation",
        "Subordinates: the lower-level entities contained beneath it",
    ], [
        "الواجهة: تواصل الكيان مع عناصر التصميم الأخرى",
        "المعالجة: العمليات الداخلية التي ينفذها الكيان",
        "الموارد: الوسائل والمدخلات اللازمة لتشغيل الكيان",
        "التوابع: كيانات المستوى الأدنى الواقعة تحته",
    ]),
    "ch5_sdd_entity_subordinates": ([
        "Subordinates: the lower-level design elements contained beneath it",
        "Dependencies: the external elements on which the entity relies",
        "Purpose: the role this element fulfills in the design",
        "Data: the information it stores, receives, or produces",
    ], [
        "التوابع: عناصر التصميم الأدنى الواقعة ضمن الكيان",
        "الاعتماديات: عناصر خارجية يعتمد عليها الكيان",
        "الغرض: الدور الذي يؤديه العنصر ضمن التصميم",
        "البيانات: معلومات يخزنها العنصر أو يستقبلها أو ينتجها",
    ]),
    "ch5_sdd_entity_dependencies": ([
        "Dependencies: other design elements on which the entity relies",
        "Subordinates: lower-level entities that belong beneath the element",
        "Identification: the name and identity of the design element",
        "Processing: actions the entity performs when it receives input",
    ], [
        "الاعتماديات: عناصر تصميم أخرى يعتمد عليها الكيان",
        "التوابع: كيانات أدنى تنتمي إلى العنصر البنيوي",
        "التعريف: اسم عنصر التصميم وهويته المميزة",
        "المعالجة: أفعال ينفذها الكيان عند استقبال المدخلات",
    ]),
    "ch5_sdd_entity_resources": ([
        "Resources: the facilities and inputs a design entity requires",
        "Identification: the distinct name assigned to the entity",
        "Purpose: the role performed by the element in the system",
        "Function: behavior the design element is expected to provide",
    ], [
        "الموارد: الوسائل والمدخلات التي يحتاج إليها كيان التصميم",
        "التعريف: الاسم المميز المسند إلى الكيان",
        "الغرض: الدور الذي يؤديه العنصر داخل النظام",
        "الوظيفة: السلوك المتوقع أن يقدمه عنصر التصميم",
    ]),
    "ch5_sdd_entity_processing": ([
        "Processing: the operations and transformations performed by the entity",
        "Subordinates: the lower-level elements contained by the entity",
        "Identification: the name that distinguishes this design element",
        "Dependencies: the external elements the entity relies on",
    ], [
        "المعالجة: العمليات والتحويلات التي ينفذها الكيان",
        "التوابع: العناصر ذات المستوى الأدنى التي يضمها الكيان",
        "التعريف: الاسم الذي يميز عنصر التصميم",
        "الاعتماديات: العناصر الخارجية التي يعتمد عليها الكيان",
    ]),
    "ch5_sdd_content_vs_view": ([
        "Views organize design-entity attributes around specific concerns",
        "Attributes replace every design entity in the description",
        "Views are executable forms of each documented attribute",
        "Attributes describe only the system's deployment hardware",
    ], [
        "تنظم المناظير سمات كيان التصميم بحسب جوانب محددة",
        "تستبدل السمات كيانات التصميم الواردة في الوصف كلها",
        "المناظير صيغ تنفيذية لكل سمة موثقة في التصميم",
        "تصف السمات أجهزة نشر النظام البرمجي فقط",
    ]),
    "ch5_sdd_views_set": ([
        "Decomposition, dependency, interface, and detailed-design views",
        "Use-case, activity, sequence, and deployment-diagram views",
        "Input, transform, output, and transaction-analysis views",
        "Data, control, procedural, and communicational-cohesion views",
    ], [
        "مناظير التفكيك والاعتمادية والواجهة والتصميم التفصيلي",
        "مناظير حالات الاستخدام والنشاط والتسلسل ومخططات النشر",
        "مناظير المدخل والتحويل والمخرج وتحليل المعاملات",
        "مناظير البيانات والتحكم والتماسك الإجرائي والاتصالي",
    ]),
    "ch5_sdd_detail_view": ([
        "In the detailed-design view describing algorithms and local data",
        "In the dependency view mapping relationships among elements",
        "In the interface view defining public signatures and contracts",
        "In the scope statement describing the software system boundary",
    ], [
        "في منظور التفصيل الذي يصف الخوارزميات والبيانات المحلية",
        "في منظور الاعتمادية الذي يوضح العلاقات بين العناصر",
        "في منظور الواجهة الذي يحدد التواقيع والعقود العامة",
        "في بيان النطاق الذي يصف حدود النظام البرمجي",
    ]),
    "ch5_sdd_views_purpose": ([
        "Each view helps examine one specific design concern",
        "Views remove the need to identify entities in the design",
        "Each view replaces the system requirements specification",
        "Every view repeats the complete implementation source code",
    ], [
        "يساعد كل منظور على فحص جانب تصميمي محدد",
        "تلغي المناظير الحاجة إلى تحديد كيانات التصميم",
        "يستبدل كل منظور مواصفة متطلبات النظام",
        "يكرر كل منظور الشيفرة الكاملة لتنفيذ النظام",
    ]),
    "ch5_sdd_function_view_note": ([
        "Decomposition view shows the function hierarchy and responsibilities",
        "Interface view describes signatures and communication contracts",
        "Dependency view describes links among design entities",
        "Detailed view specifies algorithms and internal data",
    ], [
        "يعرض منظور التفكيك تسلسل الوظائف ومسؤوليات المكونات",
        "يعرض منظور الواجهة التواقيع وعقود التواصل",
        "يعرض منظور الاعتمادية الروابط بين كيانات التصميم",
        "يعرض منظور التفصيل الخوارزميات والبيانات الداخلية",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_ood_definition": ([
        "Design based on interacting objects and their classes",
        "Design based only on a hierarchy of software procedures",
        "Design based on data flows without structural entities",
        "Design based on deployment nodes without software behavior",
    ], [
        "تصميم يقوم على كائنات متفاعلة وأصنافها",
        "تصميم يعتمد على تسلسل الإجراءات البرمجية وحده",
        "تصميم يعرض تدفق البيانات بلا عناصر بنيوية",
        "تصميم يصف عقد النشر من دون سلوك برمجي",
    ]),
    "ch5_ood_domain_model": ([
        "Entities with identity, state, and behavior",
        "Functions without associated data or runtime identity",
        "Source files containing explanatory comments only",
        "Network devices without software state or behavior",
    ], [
        "كيانات لها هوية وحالة وسلوك",
        "وظائف بلا بيانات أو هوية أثناء التشغيل",
        "ملفات مصدرية تحوي تعليقات تفسيرية فقط",
        "أجهزة شبكية بلا حالة أو سلوك برمجي",
    ]),
    "ch5_ood_vs_fod": ([
        "OOD centers on objects; FOD centers on functions",
        "Both approaches focus only on database storage and tables",
        "Neither approach models system responsibilities or behavior",
        "OOD centers on procedures; FOD centers on objects",
    ], [
        "يركز OOD على الكائنات وFOD على الوظائف",
        "يركز النهجان على خزن البيانات وجداولها فقط",
        "لا يمثل أي نهج مسؤوليات النظام وسلوكه",
        "يركز OOD على الإجراءات وFOD على الكائنات",
    ]),
    "ch5_ood_class": ([
        "Common structure and behavior shared by related objects",
        "One specific runtime message passed between two objects",
        "A deployment machine and its network address",
        "An ordered sequence of procedures with unrelated purposes",
    ], [
        "بنية وسلوك مشتركان بين كائنات الصنف الواحد",
        "رسالة تشغيلية واحدة تنتقل بين كائنات النظام",
        "آلة نشر وعنوانها الشبكي ضمن المعمارية",
        "تسلسل منظم لإجراءات غير مترابطة في التطبيق",
    ]),
    "ch5_ood_encapsulation": ([
        "Hides internal state behind a controlled public interface",
        "Exposes every internal field for direct external modification",
        "Combines unrelated procedures within a shared source file",
        "Removes all communication among interacting software objects",
    ], [
        "يخفي الحالة الداخلية خلف واجهة عامة مضبوطة",
        "يكشف الحقول الداخلية كلها للتعديل الخارجي المباشر",
        "يجمع إجراءات غير مترابطة داخل ملف شيفرة مشترك",
        "يلغي التواصل بين الكائنات البرمجية المتفاعلة كلها",
    ]),
    "ch5_ood_abstraction_focus": ([
        "Relevant properties while leaving out needless detail",
        "All possible operations regardless of the model's purpose",
        "Every implementation detail before requirements are known",
        "Only the object's physical location in a deployment view",
    ], [
        "الخصائص المهمة مع حذف التفاصيل غير اللازمة",
        "كل العمليات الممكنة مهما كان غرض النموذج",
        "تفاصيل التنفيذ كلها قبل تحديد المتطلبات",
        "موقع الكائن المادي ضمن منظور النشر فقط",
    ]),
    "ch5_ood_not_guarantee": ([
        "It can model domain entities when that model fits the system",
        "It guarantees fewer defects in every software system",
        "It removes the need for stable interfaces or software testing",
        "It always costs less than function-oriented design",
    ], [
        "قد يلائم تمثيل كيانات المجال بعض الأنظمة",
        "يضمن عيوباً أقل في كل نظام برمجي",
        "يلغي الحاجة إلى واجهات ثابتة واختبارات برمجية",
        "يخفض الكلفة دائماً مقارنة بالتصميم الوظيفي",
    ]),
    "ch5_ood_object": ([
        "Its own identity, current state, and behavior",
        "Its source-file size and software release date",
        "Its class name without any state in the instance",
        "Its position in a printed structure-chart hierarchy",
    ], [
        "هويته وحالته وسلوكه الخاص",
        "حجم ملفه وتاريخ إصدار البرمجيات",
        "اسم صنفه من دون حالة لنسخته",
        "موضعه في تسلسل مخطط بنية مطبوع",
    ]),
    "ch5_ood_message": ([
        "One object requests another object to perform an operation",
        "One procedure changes a global flag without calling a component",
        "One diagram assigns a hardware device to a software node",
        "One class stores the source file of another class",
    ], [
        "طلب كائن من آخر تنفيذ عملية محددة",
        "تغيير إجراء علماً عاماً دون استدعاء مكون",
        "تخصيص مخطط جهازاً لعقدة برمجية محددة",
        "خزن صنف ملف الشيفرة الخاص بصنف آخر",
    ]),
    "ch5_ood_polymorphism": ([
        "Different object types implement the same operation differently",
        "Every object stores identical state in its internal data fields",
        "Each class defines exactly one method for all its instances",
        "Messages can be transmitted only during source-code compilation",
    ], [
        "تطبق الأنواع المختلفة العملية نفسها بطرائق متباينة",
        "تخزن الكائنات كلها الحالة نفسها ضمن حقولها الداخلية",
        "يحدد كل صنف طريقة واحدة لجميع النسخ المنتمية إليه",
        "لا تُرسل الرسائل إلا خلال ترجمة ملفات البرنامج",
    ]),
    "ch5_basic_abstraction": ([
        "Abstraction of relevant operations with internal details omitted",
        "A deployment view assigning objects to physical system nodes",
        "Direct access to internal representation and stored fields",
        "Content coupling between classes through access to private state",
    ], [
        "تجريد العمليات ذات الصلة وإغفال تفاصيلها الداخلية",
        "منظور نشر يوزع الكائنات على عقد النظام المادية",
        "وصول مباشر إلى التمثيل والحقول الداخلية",
        "اقتران محتوى بين الأصناف عبر الوصول إلى حالتها الخاصة",
    ]),
    "ch5_ood_adt_class": ([
        "An ADT specifies operations; a class models object data and behavior",
        "A class is a table of values without operations or behavior",
        "An ADT exposes its internal representation to every caller",
        "An ADT is always a class that uses inheritance and polymorphism",
    ], [
        "يحدد ADT العمليات ويصف الصنف بيانات الكائن وسلوكه",
        "الصنف جدول قيم لا يحدد سلوك الكائن أو عملياته",
        "يكشف ADT تمثيله المخزني لكل مستدعٍ للنظام",
        "يكون ADT دائماً صنفاً يرث ويتعدد شكله وسلوكه",
    ]),
    "ch5_ood_inheritance_caution": ([
        "When the general-specialized relationship is unclear",
        "When shared behavior genuinely belongs to a base type",
        "When a class has a stable and well-defined interface",
        "When a subtype specializes valid inherited behavior",
    ], [
        "عندما تكون علاقة العام بالمتخصص غير واضحة",
        "حين ينتمي السلوك المشترك فعلاً إلى صنف أساس",
        "عندما يحدد الصنف واجهة واضحة للمستعملين",
        "حين يخصص النوع الفرعي سلوكاً موروثاً ملائماً",
    ]),
    "ch5_oo_process_first": ([
        "Identify actors and define their use cases for system behavior",
        "Prepare final design documents before analyzing system actors",
        "Create component and deployment views at the start of analysis",
        "Create object and state diagrams before defining use cases",
    ], [
        "تحديد الجهات وإنشاء حالات استخدام تصف سلوك النظام",
        "إعداد وثائق التصميم النهائية قبل تحليل الجهات",
        "إنشاء مناظير المكونات والنشر في بداية التحليل",
        "إنشاء مخططات الكائنات والحالات قبل تعريف الاستخدامات",
    ]),
    "ch5_oo_process_activity_optional": ([
        "When analysis needs an activity view for a use case",
        "For every use case in every system without exception",
        "Before any actors have been identified in the system",
        "Only after the final design documents are approved",
    ], [
        "عند حاجة التحليل إلى مخطط نشاط لحالة استخدام",
        "لكل حالة استخدام في جميع الأنظمة بلا استثناء",
        "قبل تحديد الجهات التي تتفاعل مع النظام",
        "بعد اعتماد وثائق التصميم النهائية حصراً",
    ]),
    "ch5_oo_process_interaction": ([
        "Participating objects and interaction diagrams for each use case",
        "Risk registers and cost estimates for the entire system",
        "Source-code listings and final software test reports",
        "Data tables and physical deployment labels for nodes",
    ], [
        "الكائنات المشاركة ومخططات التفاعل لكل حالة استخدام",
        "سجلات المخاطر وتقديرات كلفة النظام بأكمله",
        "قوائم الشيفرة وتقارير اختبار البرمجيات النهائية",
        "جداول البيانات وتسميات عقد النشر المادية",
    ]),
    "ch5_oo_process_state_optional": ([
        "If the design needs diagrams that clarify object states",
        "Before the use-case model in every software system",
        "Only after the application is deployed to its users",
        "Instead of preparing the system's interaction diagrams",
    ], [
        "عند الحاجة إلى توضيح حالات الكائن ضمن التصميم",
        "قبل نموذج حالات الاستخدام في كل نظام برمجي",
        "بعد نشر التطبيق البرمجي إلى المستخدمين فقط",
        "بدلاً من إعداد مخططات التفاعل الخاصة بالنظام",
    ]),
    "ch5_oo_process_components": ([
        "Component and deployment views for implementation structure",
        "Sequence and collaboration views for object interaction",
        "Activity and use-case views for actor goals and workflows",
        "Class and state-chart views for structure and behavior",
    ], [
        "مناظير المكونات والنشر لتوضيح بنية التنفيذ",
        "مناظير التسلسل والتعاون لشرح تفاعل الكائنات",
        "مناظير النشاط وحالات الاستخدام لأهداف الجهات وسير العمل",
        "مناظير الأصناف والحالة لوصف البنية والسلوك",
    ]),
    "ch5_oo_process_order": ([
        "Interaction, class, optional state/object, components, deployment",
        "Deployment, then interaction, state, use cases, and class diagrams",
        "Activity, components, use cases, class modeling, interaction",
        "Class, deployment, use cases, optional activity, interaction",
    ], [
        "التفاعل، الأصناف، الحالة والكائن عند الحاجة، المكونات، النشر",
        "النشر ثم التفاعل والحالة وحالات الاستخدام والأصناف",
        "النشاط ثم المكونات وحالات الاستخدام ونمذجة الأصناف والتفاعل",
        "الأصناف ثم النشر وحالات الاستخدام والنشاط والتفاعل",
    ]),
    "ch5_oo_process_documents": ([
        "Prepare and organize the final technical design documents",
        "Replace all system requirements with executable source code",
        "Repeat actor identification after the product is deployed",
        "Publish the user interface without a design review",
    ], [
        "إعداد الوثائق الفنية النهائية لتصميم النظام وتنظيمها",
        "استبدال متطلبات النظام ببرنامج قابل للتنفيذ",
        "إعادة تحديد الجهات بعد نشر النظام البرمجي للمستخدمين",
        "نشر واجهة المستخدم من دون إجراء مراجعة تصميمية",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_fod_data_separation": ([
        "Data structures and procedures that operate on those structures",
        "Class identity and its runtime object instances",
        "Requirements and boundaries across external systems",
        "Component nodes and the machines that host them",
    ], [
        "بنى البيانات والإجراءات التي تستخدم تلك البنى",
        "هوية الصنف والنسخ المنشأة منه أثناء التشغيل",
        "متطلبات النظام وحدوده مع الأنظمة الخارجية",
        "عقد المكونات والأجهزة المادية التي تستضيفها",
    ]),
    "ch5_fod_dfd": ([
        "Data Flow Diagram",
        "Structure Chart",
        "Use-Case Diagram",
        "Deployment Diagram",
    ], [
        "مخطط يوضح حركة البيانات وتحولها",
        "مخطط يوضح استدعاء الوحدات وترتيبها",
        "مخطط يوضح أهداف الجهات وحالات استخدامها",
        "مخطط يوضح عقد التنفيذ ومواقعها",
    ]),
    "ch5_fod_structure_chart": ([
        "Structure Chart",
        "Data Flow Diagram",
        "State Diagram",
        "Deployment Diagram",
    ], [
        "مخطط يوضح بنية الوحدات البرمجية",
        "مخطط يوضح حركة البيانات وتحولاتها",
        "مخطط يوضح تغير حالة الكائن",
        "مخطط يوضح توزيع النظام على أجهزة النشر",
    ]),
    "ch5_fod_hierarchy": ([
        "System functions decomposed into subordinate procedures",
        "Hardware devices mapped to business objectives",
        "Object states allocated to physical deployment nodes",
        "Database records assigned to external user roles",
    ], [
        "تفكيك وظائف النظام إلى إجراءات أصغر تابعة",
        "ربط أجهزة الحاسوب بأهداف العمل التجارية",
        "تخصيص حالات الكائن لعقد النشر المادية",
        "إسناد سجلات قاعدة البيانات إلى أدوار المستخدمين",
    ]),
    "ch5_procedural_abstraction": ([
        "Procedural abstraction through a named operation",
        "Control abstraction across structured execution paths",
        "Deployment abstraction over physical computing nodes",
        "Data abstraction around hidden stored representation",
    ], [
        "التجريد الإجرائي عبر عملية ذات اسم واضح",
        "تجريد التحكم عبر مسارات تنفيذ منظمة",
        "تجريد النشر عبر عقد الحوسبة المادية",
        "تجريد البيانات حول تمثيل مخزن مخفي",
    ]),
    "ch5_dfd_view": ([
        "Data movement, stores, and transformations",
        "Module calls and their control hierarchy",
        "Object states and behavior over time",
        "Physical nodes and allocation of hardware",
    ], [
        "حركة البيانات والمخازن والتحولات بينها",
        "استدعاءات الوحدات وتسلسل التحكم بينها",
        "حالات الكائنات والسلوك المرتبط بمرور الزمن",
        "توزيع الأجهزة والعقد المادية على مواقع النشر",
    ]),
    "ch5_multiple_notations": ([
        "Different views expose different design concerns",
        "A design diagram can never be revised after review",
        "Every stakeholder must read identical design detail",
        "Notation choice replaces important architecture decisions",
    ], [
        "تكشف المناظير المختلفة جوانب متعددة من التصميم",
        "لا يمكن تعديل مخطط التصميم بعد مراجعته",
        "ينبغي أن يراجع أصحاب المصلحة مستوى التفاصيل نفسه",
        "يستبدل اختيار الترميز قرارات المعمارية المهمة",
    ]),
    "ch5_static_dynamic_notations": ([
        "Class diagram for structure; sequence diagram for behavior",
        "Structure chart showing calls with a dictionary of terms",
        "Data-flow diagram for movement with a deployment view",
        "Flowchart for control with a class diagram for object types",
    ], [
        "مخطط الأصناف للبنية ومخطط التسلسل للسلوك",
        "مخطط بنية للاستدعاءات مع قاموس للمصطلحات",
        "مخطط تدفق للحركة مع منظور خاص بالنشر",
        "مخطط تدفق للتحكم مع مخطط أصناف لأنواع الكائنات",
    ]),
    "ch5_notation_stakeholders": ([
        "A use-case view showing actor goals and system services",
        "A detailed flowchart tracing the algorithm's decisions",
        "A deployment view mapping processors to system nodes",
        "A procedure body listing local variables and operations",
    ], [
        "منظور حالات الاستخدام الذي يبين أهداف الجهات وخدمات النظام",
        "مخطط تدفق يتتبع خطوات الخوارزمية وقراراتها",
        "منظور نشر يحدد مواقع المعالجات والعقد",
        "جسم إجراء يحدد المتغيرات المحلية والعمليات",
    ]),
    "ch5_transform_transaction": ([
        "A transaction tag selects a suitable path among several",
        "A continuous data flow passes through a central transform",
        "A specialized class inherits attributes from a general class",
        "A sequence diagram orders messages exchanged by objects",
    ], [
        "تختار علامة المعاملة مساراً مناسباً من مسارات متعددة",
        "يمر تدفق البيانات عبر تحويل مركزي في النظام",
        "يرث الصنف المتخصص سمات من نوع عام",
        "يرتب مخطط التسلسل رسائل الكائنات المتبادلة عبر الزمن",
    ]),
    "ch5_procedure_level1": ([
        "The interface, calls, and side-effects level",
        "The procedure body and its implementation notation",
        "System deployment sites and physical placement",
        "Local data, timing, exception, and limit details",
    ], [
        "مستوى الواجهة والاستدعاءات والآثار الجانبية",
        "مستوى جسم الإجراء وتفاصيل ترميزه للتنفيذ",
        "مستوى النشر ومواقع النظام المادية المختلفة",
        "مستوى البنى المحلية وقيود وقت التنفيذ",
    ]),
    "ch5_procedure_level3": ([
        "A detailed procedure body written in a suitable notation",
        "The procedure name and its position in the system",
        "The callers, parameters, and interface assertions",
        "The module hierarchy and external protocols",
    ], [
        "وصف تفصيلي لجسم الإجراء باستخدام ترميز مناسب",
        "اسم الإجراء وموضعه ضمن بنية النظام",
        "المستدعون والمعاملات وتأكيدات الواجهة",
        "تسلسل الوحدات والبروتوكولات الخارجية",
    ]),
    "ch5_procedure_notation_choice": ([
        "Pseudocode or a flowchart for the procedure body",
        "A system scope statement without procedural behavior",
        "A deployment map showing physical nodes and sites",
        "A list of user actors without procedural descriptions",
    ], [
        "شيفرة وصفية أو مخطط تدفق لتفاصيل جسم الإجراء",
        "بيان نطاق النظام من دون وصف سلوكه الإجرائي",
        "خريطة نشر توضح العقد والمواقع المادية",
        "قائمة الجهات المستخدمة من دون وصف الإجراءات",
    ]),
    "ch5_ieee_recommended": ([
        "Recommended practice for software design descriptions",
        "A cost-estimation model for project planning work",
        "A protocol for deploying web applications and services",
        "A mandatory standard for software programming languages",
    ], [
        "ممارسة موصى بها لأوصاف تصميم البرمجيات وتنظيمها",
        "نموذج لتقدير كلفة المشروع وتخطيط أعماله",
        "بروتوكول لنشر تطبيقات الويب وخدماتها وإدارتها",
        "معيار إلزامي للغات البرمجة المستخدمة في الأنظمة",
    ]),
    "ch5_ieee_sdd": ([
        "System Deployment Diagram",
        "Software Data Dictionary",
        "System Development Duration",
        "Software Design Description",
    ], [
        "مخطط يصف توزيع النظام على عقد النشر",
        "قاموس يوضح بيانات النظام البرمجي",
        "مدة دورة تطوير النظام البرمجي",
        "وثيقة تصف التصميم الفني للبرمجيات",
    ]),
    "ch5_ieee_lineage": ([
        "Keep the stated edition distinct from later revisions",
        "Replace the stated edition with the newest without explanation",
        "Treat every standard revision as an identical document",
        "Omit the revision whenever the standard is named",
    ], [
        "حفظ رقم الإصدار عند مقارنته بالمراجعات اللاحقة",
        "استبدال الإصدار المذكور بالأحدث من دون شرح",
        "اعتبار مراجعات المعيار وثيقة واحدة متطابقة",
        "إهمال رقم المراجعة كلما جرى ذكر المعيار",
    ]),
    "ch5_sdd_scope_content": ([
        "Required information content and its organization",
        "User training plans and software release scheduling",
        "Project costs, work estimates, and staff assignments",
        "Source-code style rules and compiler configuration",
    ], [
        "المعلومات التي ينبغي أن يتضمنها SDD وطريقة تنظيمها",
        "خطط تدريب المستخدم وجدولة إصدار البرمجيات",
        "كلف المشروع وتقديرات العمل وتوزيع الموظفين",
        "قواعد تنسيق الشيفرة وإعداد المترجم البرمجي",
    ]),
    "ch5_sdd_scope_not_lifecycle": ([
        "It applies across several software application domains",
        "It requires one mandatory lifecycle for development",
        "It is independent of a specific design methodology",
        "It defines SDD information and its arrangement",
    ], [
        "ينطبق على مجالات متعددة للتطبيقات البرمجية",
        "يفرض دورة تطوير إلزامية واحدة للمشاريع",
        "يستقل عن منهجية تصميم محددة للنظام",
        "يحدد معلومات SDD وطريقة ترتيبها",
    ]),
    "ch5_sdd_scope_not_language": ([
        "Compiler settings used when implementing software",
        "Information included in the software design description",
        "Applicability of design descriptions across systems",
        "Organization of information within the software design description",
    ], [
        "إعدادات المترجم المستخدمة لتنفيذ النظام",
        "معلومات تفصيلية يتضمنها وصف تصميم النظام",
        "مجالات تطبيق وصف التصميم على الأنظمة",
        "طريقة تنظيم معلومات التصميم في وثيقة SDD",
    ]),
    "ch5_design_entity_definition": ([
        "A distinct structural element described in the software design",
        "A user story defining behavior for customer review",
        "A physical server hosting a deployed application service",
        "A change request submitted after the software release",
    ], [
        "عنصر بنيوي محدد في وصف تصميم النظام",
        "قصة مستخدم تحدد السلوك لمراجعة العميل",
        "خادم مادي يستضيف خدمة تطبيق منشورة",
        "طلب تغيير يقدم بعد إصدار البرنامج",
    ]),
    "ch5_design_view_definition": ([
        "Attributes addressing a particular design concern",
        "All project users who review and approve the delivery plan",
        "Only the external data entering the software system",
        "Every source file arranged by deployment sequence",
    ], [
        "سمات تعالج جانباً محدداً من التصميم",
        "مستخدمو المشروع الذين يراجعون خطة التسليم ويعتمدونها",
        "البيانات الخارجية الداخلة إلى النظام البرمجي فقط",
        "ملفات الشيفرة كلها مرتبة حسب تسلسل النشر",
    ]),
    "ch5_entity_examples": ([
        "A subsystem with clear structural responsibilities",
        "A meeting invitation distributed to the project team",
        "A project budget total without any software element",
        "A user complaint with no design response attached",
    ], [
        "نظام فرعي ذو مسؤوليات بنيوية واضحة",
        "دعوة اجتماع موزعة على أعضاء فريق المشروع",
        "مجموع ميزانية مشروع بلا عنصر برمجي محدد",
        "شكوى مستخدم بلا استجابة تصميمية مرتبطة بها",
    ]),
    "ch5_sdd_purpose": ([
        "Guide implementation with an authoritative design description",
        "Replace stated requirements with executable application code",
        "Record only defects discovered after software release",
        "Select the commercial pricing model used by the customer",
    ], [
        "توجيه التنفيذ بوصف فني معتمد لقرارات تصميم البرمجيات",
        "استبدال المتطلبات المحددة بشيفرة التطبيق القابلة للتشغيل",
        "تسجيل العيوب التي تظهر بعد إصدار البرمجيات فقط",
        "اختيار نموذج التسعير التجاري الذي يعتمده العميل",
    ]),
    "ch5_sdd_implementation": ([
        "The recorded interface decision that builders should follow",
        "An unrelated budget for deploying the software system",
        "A replacement user requirement that was not reviewed",
        "A marketing plan prepared after the product release",
    ], [
        "قرار الواجهة المعتمد الذي يتبعه المنفذون",
        "ميزانية غير مرتبطة بنشر النظام البرمجي",
        "متطلب مستخدم بديل لم يخضع للمراجعة",
        "خطة تسويقية أعدت بعد إصدار المنتج",
    ]),
    "ch5_sdd_content_vs_view": ([
        "Views organize an entity's attributes around design concerns",
        "Attributes replace every design entity in the description",
        "Views are executable forms of each documented attribute",
        "Attributes describe only the system's deployment hardware",
    ], [
        "تنظم المناظير سمات الكيان حول جوانب تصميم محددة",
        "تستبدل السمات كيانات التصميم الواردة في الوصف كلها",
        "المناظير صيغ تنفيذية لكل سمة موثقة في التصميم",
        "تصف السمات أجهزة نشر النظام البرمجي فقط",
    ]),
    "ch5_sdd_detail_view": ([
        "In the detailed-design view describing algorithms and local data",
        "In the dependency view mapping relationships among elements",
        "In the interface view defining public signatures and contracts",
        "In the scope statement describing the system boundary and contents",
    ], [
        "في منظور التفصيل الذي يصف الخوارزميات والبيانات المحلية",
        "في منظور الاعتمادية الذي يوضح العلاقات بين العناصر",
        "في منظور الواجهة الذي يحدد التواقيع والعقود العامة",
        "في بيان نطاق النظام الذي يوضح حدوده ومكوناته",
    ]),
    "ch5_sdd_function_view_note": ([
        "Decomposition view shows the function hierarchy and responsibilities",
        "Interface view describes public signatures and communication contracts",
        "Dependency view describes links among design entities",
        "Detailed view specifies algorithms and internal data",
    ], [
        "يعرض منظور التفكيك تسلسل الوظائف ومسؤوليات المكونات",
        "يعرض منظور الواجهة التواقيع وعقود التواصل",
        "يعرض منظور الاعتمادية الروابط بين كيانات التصميم",
        "يعرض منظور التفصيل الخوارزميات والبيانات الداخلية",
    ]),
    "ch5_ood_domain_model": ([
        "Entities with identity, state, and behavior",
        "Functions with no identity or associated data",
        "Source files containing comments but no runtime entities",
        "Network devices without software state or behavior",
    ], [
        "كيانات تمتلك هوية وحالة وسلوكاً",
        "وظائف بلا هوية أو بيانات مرتبطة بها",
        "ملفات مصدرية تحوي تعليقات لا كيانات تشغيلية",
        "أجهزة شبكية بلا حالة أو سلوك برمجي",
    ]),
    "ch5_ood_vs_fod": ([
        "OOD centers on objects; FOD centers on functions",
        "Both approaches focus only on stored database tables",
        "Neither approach models system responsibilities or behavior",
        "OOD models procedures; FOD models objects",
    ], [
        "يركز OOD على الكائنات وFOD على الوظائف",
        "يركز النهجان على جداول البيانات المخزنة فقط",
        "لا يمثل أي نهج مسؤوليات النظام وسلوكه",
        "ينظم OOD الإجراءات وFOD الكائنات",
    ]),
    "ch5_ood_object": ([
        "Its own identity, current state, and behavior",
        "Its source-file size and software release date",
        "Its class name without any state in the instance",
        "Its position in a printed structure-chart hierarchy",
    ], [
        "هويته وحالته وسلوكه الأساسي",
        "حجم ملفه وتاريخ إصدار البرمجيات",
        "اسم صنفه من دون حالة لنسخته",
        "موضعه في تسلسل مخطط بنية مطبوع",
    ]),
    "ch5_ood_adt_class": ([
        "An ADT specifies operations; a class models object features",
        "A class is a table of values without operations or behavior",
        "An ADT exposes its internal representation to every caller",
        "An ADT is always a class that uses inheritance and polymorphism",
    ], [
        "يحدد ADT العمليات ويصف الصنف حالة الكائن وسلوكه",
        "الصنف جدول قيم لا يحدد سلوك الكائن أو عملياته",
        "يكشف ADT تمثيله المخزني لكل مستدعٍ للنظام",
        "يكون ADT دائماً صنفاً يرث ويتعدد شكله وسلوكه",
    ]),
    "ch5_oo_process_interaction": ([
        "Objects and diagrams that show messages for each use case",
        "Risk records and cost estimates for the entire system",
        "Source-code listings and final software test reports",
        "Data tables and physical deployment labels for nodes",
    ], [
        "الكائنات ومخططات الرسائل المتبادلة لكل حالة استخدام",
        "سجلات المخاطر وتقديرات كلفة النظام بأكمله",
        "قوائم الشيفرة وتقارير اختبار البرمجيات النهائية",
        "جداول البيانات وتسميات عقد النشر المادية",
    ]),
    "ch5_oo_process_components": ([
        "Component and deployment views for implementation structure",
        "Sequence and collaboration views for object interaction",
        "Activity and use-case views for actor goals and workflows",
        "Class and state-chart views for structure and behavior",
    ], [
        "مناظير المكونات والنشر لتوضيح بنية التنفيذ",
        "مناظير التسلسل والتعاون لشرح تفاعل الكائنات",
        "مناظير النشاط وحالات الاستخدام لأهداف الجهات وسير العمل",
        "مناظير الأصناف والحالة لوصف البنية والسلوك",
    ]),
    "ch5_oo_process_order": ([
        "Interaction, class, optional state/object, components, deployment",
        "Deployment, then interaction, state, use cases, and class diagrams",
        "Activity, components, use cases, class modeling, interaction",
        "Class, deployment, use cases, optional activity, interaction",
    ], [
        "التفاعل والأصناف والحالة والكائن اختيارياً ثم المكونات والنشر",
        "النشر ثم التفاعل والحالة وحالات الاستخدام والأصناف",
        "النشاط ثم المكونات وحالات الاستخدام ونمذجة الأصناف والتفاعل",
        "الأصناف ثم النشر وحالات الاستخدام والنشاط والتفاعل",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_fod_definition": ([
        "Functions and their procedural hierarchy", "Objects and their identity relationships",
        "Hardware nodes and deployment locations", "User stories and planned release dates",
    ], [
        "الوظائف وتسلسل الإجراءات الذي يضمها النظام", "الكائنات وهوياتها وعلاقاتها البنيوية",
        "العقد المادية ومواقع توزيع مكونات النظام", "قصص المستخدم وأهدافها ضمن خطة الإصدار",
    ]),
    "ch5_fod_data_separation": ([
        "Data structures and procedures that transform them", "Class identity and its runtime object instances",
        "Requirements and boundaries across external systems", "Component nodes and the machines that host them",
    ], [
        "بنى البيانات والإجراءات التي تحولها", "هوية الصنف والنسخ التي تنشأ منه أثناء التشغيل",
        "متطلبات النظام وحدوده مع الأنظمة الخارجية", "عقد المكونات والأجهزة المادية التي تستضيفها",
    ]),
    "ch5_fod_structure_chart": ([
        "Structure Chart showing the module hierarchy", "Data Flow Diagram tracing input and output",
        "State Diagram showing object state changes", "Deployment Diagram mapping software to nodes",
    ], [
        "مخطط بنية يوضح تسلسل الوحدات البرمجية", "مخطط تدفق يوضح حركة البيانات وتحولاتها",
        "مخطط حالة يوضح تغير حالات الكائنات", "مخطط نشر يوضح توزيع النظام على أجهزته",
    ]),
    "ch5_fod_hierarchy": ([
        "System functions divided into subordinate procedures", "Hardware devices mapped to business objectives",
        "Object states assigned to physical deployment nodes", "Database records assigned to external user roles",
    ], [
        "تقسيم وظائف النظام إلى إجراءات أصغر تابعة", "ربط أجهزة الحاسوب بأهداف العمل التجارية",
        "تخصيص حالات الكائن لعقد النشر المادية", "إسناد سجلات البيانات إلى أدوار المستخدمين",
    ]),
    "ch5_procedural_abstraction": ([
        "Procedural abstraction through a named operation", "Control abstraction across structured execution paths",
        "Deployment abstraction over physical computing nodes", "Data abstraction around hidden stored representation",
    ], [
        "التجريد الإجرائي عبر عملية محددة الاسم", "تجريد التحكم عبر مسارات تنفيذ منظمة",
        "تجريد النشر عبر عقد الحوسبة المادية", "تجريد البيانات حول تمثيل مخزن غير ظاهر",
    ]),
    "ch5_notation_stakeholders": ([
        "A use-case view showing actor goals and system services", "A detailed flowchart tracing algorithm decisions",
        "A deployment view mapping processors to system nodes", "A procedure body listing variables and operations",
    ], [
        "منظور حالات استخدام يوضح أهداف الجهات وخدمات النظام", "مخطط تدفق يتتبع خطوات الخوارزمية وقراراتها",
        "منظور نشر يحدد مواقع المعالجات والعقد", "جسم إجراء يسرد المتغيرات والعمليات",
    ]),
    "ch5_transform_transaction": ([
        "A transaction tag selects a path among available alternatives", "A continuous data flow passes through a central transform",
        "A specialized class inherits attributes from a general class", "A sequence diagram orders messages exchanged by objects",
    ], [
        "تحدد علامة المعاملة مساراً من بدائل متاحة", "يمر تدفق البيانات عبر تحويل مركزي في النظام",
        "يرث الصنف المتخصص سمات من صنف عام", "يرتب مخطط التسلسل رسائل الكائنات المتبادلة عبر الزمن",
    ]),
    "ch5_procedure_level3": ([
        "A procedure's detailed body in a selected notation", "The procedure name and its place in the system",
        "Its callers, parameters, and interface assertions", "The module hierarchy and its external protocols",
    ], [
        "وصف جسم الإجراء بتفصيل باستخدام ترميز مناسب", "اسم الإجراء وموضعه ضمن بنية النظام",
        "الجهات المستدعية والمعاملات وتأكيدات الواجهة", "تسلسل الوحدات والبروتوكولات الخارجية للنظام",
    ]),
    "ch5_ieee_lineage": ([
        "Keep the stated edition distinct from later revisions", "Replace the stated edition with the newest without explanation",
        "Treat every standard revision as an identical document", "Omit the revision whenever the standard is named",
    ], [
        "حفظ رقم الإصدار وتمييزه عن المراجعات اللاحقة", "استبدال الإصدار المذكور بالأحدث من دون توضيح",
        "اعتبار كل مراجعة للمعيار وثيقة مطابقة للأصل", "إهمال رقم المراجعة عند ذكر المعيار في النص",
    ]),
    "ch5_sdd_scope_content": ([
        "Required information content and its organization", "User training plans and software release scheduling",
        "Project costs, work estimates, and staff assignments", "Source-code style rules and compiler configuration",
    ], [
        "المعلومات المطلوبة في SDD وطريقة تنظيمها", "خطط تدريب المستخدم وجدولة إصدار البرمجيات",
        "كلف المشروع وتقديرات العمل وتوزيع الموظفين", "قواعد تنسيق الشيفرة وإعداد المترجم البرمجي",
    ]),
    "ch5_sdd_scope_not_lifecycle": ([
        "It applies across several software application domains", "It requires one mandatory development lifecycle",
        "It is independent of a specific design methodology", "It defines SDD information and its arrangement",
    ], [
        "ينطبق على مجالات متنوعة من التطبيقات البرمجية", "يفرض دورة تطوير واحدة إلزامية لكل مشروع",
        "يستقل عن منهجية تصميم محددة للنظام", "يحدد معلومات SDD وطريقة ترتيبها",
    ]),
    "ch5_sdd_scope_not_language": ([
        "Compiler settings used when implementing the software", "Information included in the software design description",
        "Applicability of design descriptions across systems", "Organization of information within the design description",
    ], [
        "إعدادات المترجم المستخدمة عند تنفيذ البرمجيات", "المعلومات التي يتضمنها وصف تصميم البرمجيات",
        "مجالات تطبيق أوصاف التصميم على الأنظمة", "تنظيم المعلومات داخل وصف تصميم البرمجيات",
    ]),
    "ch5_design_entity_definition": ([
        "A distinct structural element in the software design", "A user story defining behavior for customer review",
        "A physical server hosting a deployed application service", "A change request submitted after the software release",
    ], [
        "عنصر بنيوي محدد ضمن تصميم البرمجيات", "قصة مستخدم تحدد سلوكاً لمراجعته مع العميل",
        "خادم مادي يستضيف خدمة تطبيق بعد نشرها", "طلب تغيير يقدم بعد إصدار المنتج البرمجي",
    ]),
    "ch5_design_view_definition": ([
        "Attributes addressing a particular design concern", "Project users reviewing the software delivery plan",
        "External data entering the software system", "Source files arranged by their deployment sequence",
    ], [
        "سمات تعالج جانباً محدداً من التصميم", "مستخدمو المشروع الذين يراجعون خطة تسليم النظام",
        "بيانات خارجية تدخل إلى النظام البرمجي", "ملفات الشيفرة مرتبة حسب تسلسل نشر النظام",
    ]),
    "ch5_entity_vs_view": ([
        "An entity is described; a view groups attributes by concern", "An entity is a project team; a view is its schedule",
        "An entity is a test stage; a view is a release package", "An entity is a user role; a view is a project plan",
    ], [
        "الكيان عنصر بنيوي يصفه التصميم والمنظور يجمع سماته حسب الجانب", "الكيان فريق المشروع والمنظور جدول مواعيد التسليم",
        "الكيان مرحلة اختبار والمنظور حزمة إصدار البرنامج", "الكيان دور مستخدم والمنظور خطة المشروع العامة",
    ]),
    "ch5_entity_examples": ([
        "A subsystem with clear structural responsibilities", "A meeting invitation sent to the project team",
        "A project budget total without a software element", "A user complaint without an attached design response",
    ], [
        "نظام فرعي واضح البنية وله مسؤوليات محددة", "دعوة اجتماع أرسلت إلى أعضاء فريق المشروع",
        "مجموع ميزانية مشروع بلا عنصر برمجي محدد", "شكوى مستخدم بلا استجابة تصميمية مرتبطة بها",
    ]),
    "ch5_sdd_implementation": ([
        "The recorded interface decision that builders should follow", "An unrelated budget for deploying the software system",
        "A replacement user requirement that was not reviewed", "A marketing plan prepared after the product release",
    ], [
        "قرار الواجهة المسجل الذي ينبغي للمنفذين اتباعه", "ميزانية نشر لا ترتبط بالتصميم البرمجي",
        "متطلب مستخدم بديل لم يخضع للمراجعة", "خطة تسويق أعدت بعد إصدار المنتج البرمجي",
    ]),
    "ch5_sdd_entity_identifier": ([
        "Identification: the entity's name and unique identity", "Dependencies: other design elements it relies on",
        "Processing: operations performed by the design entity", "Resources: facilities and inputs required by the entity",
    ], [
        "التعريف: الاسم الذي يحدد هوية كيان التصميم", "الاعتماديات: عناصر التصميم الأخرى التي يعتمد عليها",
        "المعالجة: العمليات التي ينفذها كيان التصميم", "الموارد: الوسائل والمدخلات اللازمة للكيان",
    ]),
    "ch5_sdd_entity_subordinates": ([
        "Subordinates: lower-level design elements contained within it", "Dependencies: external elements on which the entity relies",
        "Purpose: the role this element fulfills in the design", "Data: information it stores, receives, or produces",
    ], [
        "التوابع: عناصر تصميم أدنى يضمها الكيان", "الاعتماديات: عناصر خارجية يعتمد عليها الكيان",
        "الغرض: الدور الذي يؤديه هذا العنصر في التصميم", "البيانات: معلومات يخزنها أو يستقبلها أو ينتجها",
    ]),
    "ch5_sdd_entity_resources": ([
        "Resources: facilities and inputs a design entity requires", "Identification: the distinct name assigned to the entity",
        "Purpose: the role performed by the element in the system", "Function: behavior the design element should provide",
    ], [
        "الموارد: الوسائل والمدخلات التي يتطلبها كيان التصميم", "التعريف: الاسم المميز المسند إلى كيان التصميم",
        "الغرض: الدور الذي يؤديه العنصر داخل النظام", "الوظيفة: السلوك الذي ينبغي أن يقدمه عنصر التصميم",
    ]),
    "ch5_sdd_entity_processing": ([
        "Processing: operations and transformations performed by the entity", "Subordinates: lower-level elements contained within it",
        "Identification: the name that distinguishes this design element", "Dependencies: external elements the entity relies on",
    ], [
        "المعالجة: عمليات وتحويلات ينفذها كيان التصميم", "التوابع: عناصر أدنى مستوى يضمها الكيان",
        "التعريف: الاسم الذي يميز عنصر التصميم هذا", "الاعتماديات: عناصر خارجية يعتمد عليها كيان التصميم",
    ]),
    "ch5_sdd_detail_view": ([
        "In the detailed-design view describing algorithms and local data", "In the dependency view mapping relationships among elements",
        "In the interface view defining public signatures and contracts", "In the scope statement describing system boundaries",
    ], [
        "في منظور التفصيل الذي يصف الخوارزميات والبيانات الداخلية", "في منظور الاعتمادية الذي يوضح روابط عناصر التصميم",
        "في منظور الواجهة الذي يحدد التواقيع والعقود العامة", "في بيان النطاق الذي يصف حدود النظام ومكوناته",
    ]),
    "ch5_sdd_function_view_note": ([
        "Decomposition view shows the function hierarchy and responsibilities", "Interface view describes public signatures and communication contracts",
        "Dependency view describes links among design entities", "Detailed view specifies algorithms and internal data",
    ], [
        "يعرض منظور التفكيك تسلسل الوظائف ومسؤوليات الوحدات", "يعرض منظور الواجهة التواقيع العامة وعقود التواصل",
        "يعرض منظور الاعتمادية الروابط بين كيانات التصميم", "يعرض منظور التفصيل الخوارزميات والبيانات الداخلية",
    ]),
    "ch5_ood_domain_model": ([
        "Entities with identity, state, and associated behavior", "Functions with no identity or associated data",
        "Source files containing comments but no runtime entities", "Network devices without software state or behavior",
    ], [
        "كيانات لها هوية وحالة وسلوك برمجي مرتبط", "وظائف بلا هوية أو بيانات مرتبطة بها",
        "ملفات مصدرية تحوي تعليقات لا كيانات تشغيلية", "أجهزة شبكية بلا حالة أو سلوك برمجي",
    ]),
    "ch5_ood_vs_fod": ([
        "OOD centers on objects; FOD centers on functions", "Both approaches focus only on stored database tables",
        "Neither approach models system responsibilities or behavior", "OOD models procedures; FOD models objects",
    ], [
        "يركز OOD على الكائنات وFOD على الوظائف", "يركز النهجان على جداول البيانات المخزنة وحدها",
        "لا يمثل أي نهج مسؤوليات النظام أو سلوكه", "ينظم OOD الإجراءات وFOD الكائنات",
    ]),
    "ch5_ood_not_guarantee": ([
        "It can model domain entities when that model fits the system", "It guarantees fewer defects in every software system",
        "It removes the need for stable interfaces and testing", "It always costs less than function-oriented design",
    ], [
        "قد يلائم تمثيل كيانات المجال طبيعة بعض الأنظمة", "يضمن عيوباً أقل في جميع الأنظمة البرمجية",
        "يلغي الحاجة إلى واجهات مستقرة واختبارات برمجية", "يخفض الكلفة دائماً مقارنة بالتصميم الوظيفي",
    ]),
    "ch5_basic_abstraction": ([
        "Abstraction of relevant operations with internal details omitted", "A deployment view assigning objects to physical nodes",
        "Direct access to internal representation and stored fields", "Content coupling through access to another class's private state",
    ], [
        "تجريد العمليات ذات الصلة مع إغفال تفاصيلها الداخلية", "منظور نشر يوزع الكائنات على عقد النظام المادية",
        "وصول مباشر إلى التمثيل الداخلي والحقول المخزنة", "اقتران محتوى عبر الوصول إلى الحالة الخاصة لصنف آخر",
    ]),
    "ch5_oo_process_interaction": ([
        "Objects and diagrams showing messages for each use case", "Risk records and cost estimates for the whole system",
        "Source-code listings and final software test reports", "Data tables and physical deployment labels for nodes",
    ], [
        "كائنات ومخططات توضح الرسائل لكل حالة استخدام", "سجلات مخاطر وتقديرات كلفة للنظام بأكمله",
        "قوائم الشيفرة وتقارير الاختبار النهائية للبرمجيات", "جداول بيانات وتسميات عقد النشر المادية",
    ]),
    "ch5_oo_process_components": ([
        "Component and deployment views describing implementation structure", "Sequence and collaboration views for object interaction",
        "Activity and use-case views for actor goals and workflows", "Class and state-chart views describing structure and behavior",
    ], [
        "مناظير المكونات والنشر التي توضح بنية التنفيذ", "مناظير التسلسل والتعاون التي تشرح تفاعل الكائنات",
        "مناظير النشاط وحالات الاستخدام لأهداف الجهات وسير العمل", "مناظير الأصناف والحالة لوصف البنية والسلوك",
    ]),
    "ch5_oo_process_order": ([
        "Interaction, class, optional state/object, components, deployment", "Deployment, then interaction, state, use cases, and class diagrams",
        "Activity, components, use cases, class modeling, interaction", "Class, deployment, use cases, optional activity, interaction",
    ], [
        "التفاعل ثم الأصناف فالحالة والكائن عند الحاجة ثم المكونات والنشر", "النشر ثم التفاعل والحالة وحالات الاستخدام ومخططات الأصناف",
        "النشاط ثم المكونات وحالات الاستخدام ونمذجة الأصناف والتفاعل", "الأصناف ثم النشر وحالات الاستخدام والنشاط والتفاعل",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_fod_data_separation": ([
        "Data structures and procedures that transform them", "Class identity and its runtime object instances",
        "Requirements and boundaries across external systems", "Component nodes and their host machines",
    ], [
        "بنى البيانات والإجراءات التي تحولها", "هوية الصنف ونسخه المنشأة أثناء التشغيل",
        "متطلبات النظام وحدوده مع الأنظمة الخارجية", "عقد المكونات وأجهزة الحاسوب التي تستضيفها",
    ]),
    "ch5_notation_stakeholders": ([
        "A use-case view showing actor goals and system services", "A detailed flowchart tracing algorithm decisions",
        "A deployment view mapping processors to system nodes", "A procedure body listing variables and operations",
    ], [
        "منظور حالات استخدام يوضح أهداف المستخدم وخدمات النظام", "مخطط تدفق يبين خطوات الخوارزمية وفروعها",
        "منظور نشر يربط المعالجات بعقد النظام", "جسم إجراء يحدد متغيراته وعملياته المحلية",
    ]),
    "ch5_transform_transaction": ([
        "A transaction tag selects a path among available alternatives", "A continuous data flow passes through a central transform",
        "A specialized class inherits attributes from a general class", "A sequence diagram orders messages exchanged by objects",
    ], [
        "تحدد علامة المعاملة مساراً من بدائل متاحة", "يمر تدفق البيانات عبر عملية تحويل مركزية",
        "يرث صنف متخصص سمات من صنف عام في التصميم", "يرتب مخطط التسلسل رسائل الكائنات حسب الزمن",
    ]),
    "ch5_sdd_scope_not_lifecycle": ([
        "It applies across varied software application domains", "It requires one mandatory development lifecycle",
        "It is independent of a specific design methodology", "It defines SDD information and its arrangement",
    ], [
        "ينطبق على مجالات عديدة من تطبيقات البرمجيات", "يفرض دورة تطوير موحدة على جميع المشاريع",
        "لا يشترط منهجية تصميم محددة للنظام", "يحدد معلومات SDD وتنظيمها داخل وصف التصميم",
    ]),
    "ch5_sdd_scope_not_language": ([
        "Compiler settings used when implementing the software", "Information included in the software design description",
        "Applicability of design descriptions across systems", "Organization of information within the design description",
    ], [
        "إعدادات بناء البرمجيات وضبط المترجم", "المعلومات التي يتضمنها وصف تصميم البرمجيات",
        "مجالات تطبيق أوصاف التصميم على الأنظمة", "تنظيم المعلومات داخل وصف تصميم البرمجيات",
    ]),
    "ch5_design_view_definition": ([
        "Attributes addressing a particular design concern", "Project users reviewing the software delivery plan",
        "External data entering the software system", "Source files arranged by their deployment sequence",
    ], [
        "سمات تمثل جانباً محدداً من تصميم البرمجيات", "مستخدمو المشروع الذين يراجعون خطة تسليم النظام",
        "بيانات خارجية تدخل إلى النظام البرمجي", "ملفات الشيفرة مرتبة حسب تسلسل نشر النظام",
    ]),
    "ch5_entity_vs_view": ([
        "An entity is described; a view groups attributes by concern", "An entity is a project team; a view is its schedule",
        "An entity is a test stage; a view is a release package", "An entity is a user role; a view is a project plan",
    ], [
        "الكيان يوصف، والمنظور ينظم سماته بحسب جانب التصميم", "الكيان فريق المشروع والمنظور جدول مواعيد التسليم",
        "الكيان مرحلة اختبار والمنظور حزمة إصدار البرنامج", "الكيان دور مستخدم والمنظور خطة المشروع العامة",
    ]),
    "ch5_sdd_implementation": ([
        "The recorded interface decision builders should follow", "An unrelated budget for deploying the software system",
        "A replacement user requirement that was not reviewed", "A marketing plan prepared after the product release",
    ], [
        "قرار الواجهة المسجل الذي يتبعه فريق التنفيذ", "ميزانية نشر لا ترتبط بقرار التصميم البرمجي",
        "متطلب مستخدم بديل لم يخضع لمراجعة رسمية", "خطة تسويق أعدت بعد إصدار المنتج للمستخدمين",
    ]),
    "ch5_sdd_entity_subordinates": ([
        "Subordinates: lower-level design elements contained within it", "Dependencies: external design elements the entity relies on",
        "Purpose: the role this element fulfills in the design", "Data: information it stores, receives, or produces",
    ], [
        "التوابع: عناصر تصميم أدنى يضمها هذا الكيان", "الاعتماديات: عناصر تصميم خارجية يعتمد عليها الكيان",
        "الغرض: الدور الذي يؤديه هذا العنصر في التصميم", "البيانات: معلومات يخزنها أو يستقبلها أو ينتجها",
    ]),
    "ch5_sdd_entity_resources": ([
        "Resources: facilities and inputs a design entity requires", "Identification: the distinct name assigned to the entity",
        "Purpose: the role performed by the element in the system", "Function: behavior the design element should provide",
    ], [
        "الموارد: وسائل ومدخلات يحتاجها كيان التصميم", "التعريف: الاسم المميز المسند إلى كيان التصميم",
        "الغرض: الدور الذي يؤديه العنصر داخل النظام", "الوظيفة: السلوك الذي ينبغي أن يقدمه عنصر التصميم",
    ]),
    "ch5_sdd_entity_processing": ([
        "Processing: operations the design entity performs", "Subordinates: lower-level elements inside the entity",
        "Identification: the name distinguishing this design element", "Dependencies: external elements the entity relies on",
    ], [
        "المعالجة: عمليات وتحويلات ينفذها كيان التصميم", "التوابع: عناصر تصميم ذات مستوى أدنى يضمها الكيان",
        "التعريف: اسم يميز عنصر التصميم هذا عن غيره", "الاعتماديات: عناصر خارجية يتطلبها كيان التصميم",
    ]),
    "ch5_sdd_detail_view": ([
        "In the detailed-design view describing algorithms and local data", "In the dependency view mapping relationships among elements",
        "In the interface view defining public signatures and contracts", "In the scope statement describing system boundaries",
    ], [
        "في منظور التفصيل الذي يشرح الخوارزميات والبيانات", "في منظور الاعتمادية الذي يوضح روابط عناصر التصميم",
        "في منظور الواجهة الذي يحدد التواقيع والعقود العامة", "في بيان النطاق الذي يوضح حدود النظام ومكوناته الرئيسة",
    ]),
    "ch5_sdd_function_view_note": ([
        "Decomposition view shows function hierarchy and roles", "Interface view defines public signatures and communication contracts",
        "Dependency view maps links among design entities", "Detailed view specifies algorithms and internal data",
    ], [
        "يعرض منظور التفكيك تسلسل الوظائف ومسؤوليات الوحدات", "يعرض منظور الواجهة التواقيع العامة وعقود التواصل",
        "يعرض منظور الاعتمادية الروابط بين كيانات التصميم", "يعرض منظور التفصيل الخوارزميات والبيانات الداخلية",
    ]),
    "ch5_ood_vs_fod": ([
        "OOD centers on objects; FOD centers on functions", "Both approaches focus only on stored data tables",
        "Neither models software responsibilities or behavior", "OOD centers on procedures; FOD centers on objects",
    ], [
        "يركز OOD على الكائنات وFOD على الوظائف", "يركز النهجان على تخزين البيانات في الجداول فقط",
        "لا يمثل أي منهج سلوك النظام ومسؤولياته", "يركز OOD على الإجراءات وFOD على الكائنات",
    ]),
    "ch5_ood_not_guarantee": ([
        "It can model entities when the domain suits objects", "It guarantees fewer defects in every software system",
        "It removes the need for stable interfaces and testing", "It always costs less than function-oriented design",
    ], [
        "قد يلائم تمثيل كيانات المجال طبيعة بعض الأنظمة", "يضمن عيوباً أقل في جميع الأنظمة البرمجية",
        "يلغي الحاجة إلى واجهات مستقرة واختبارات برمجية", "يخفض الكلفة دائماً مقارنة بالتصميم الوظيفي",
    ]),
    "ch5_oo_process_components": ([
        "Component and deployment diagrams define build structure", "Sequence and collaboration views describe object interaction",
        "Activity and use-case views show actor goals and workflows", "Class and state-chart views show structure and behavior",
    ], [
        "مناظير المكونات والنشر التي توضح بنية التنفيذ", "مناظير التسلسل والتعاون التي تشرح تفاعل الكائنات",
        "مناظير النشاط وحالات الاستخدام لأهداف الجهات وسير العمل", "مناظير الأصناف والحالة التي توضح البنية والسلوك",
    ]),
    "ch5_oo_process_order": ([
        "Interaction, class, optional state/object, components, deployment", "Deployment, then interaction, state, use cases, and class diagrams",
        "Activity, components, use cases, class modeling, interaction", "Class, deployment, use cases, optional activity, interaction",
    ], [
        "التفاعل ثم الأصناف فالحالة والكائن عند الحاجة فالمكونات والنشر", "النشر ثم التفاعل فالحالة وحالات الاستخدام ومخططات الأصناف",
        "النشاط فالمكونات وحالات الاستخدام ثم نمذجة الأصناف والتفاعل", "الأصناف ثم النشر وحالات الاستخدام والنشاط ومخططات التفاعل",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_fod_data_separation": ([
        "Data structures and procedures that transform them", "Class identity and its runtime object instances",
        "Requirements and boundaries across external systems", "Component nodes and their host machines",
    ], [
        "بنى البيانات والإجراءات التي تحولها معاً", "هوية الصنف ونسخه المنشأة أثناء التشغيل",
        "متطلبات النظام وحدوده مع الأنظمة الخارجية", "عقد المكونات وأجهزة الحاسوب التي تستضيفها",
    ]),
    "ch5_notation_stakeholders": ([
        "A use-case view showing actor goals and system services", "A detailed flowchart tracing algorithm decisions",
        "A deployment view mapping processors to system nodes", "A procedure body listing variables and operations",
    ], [
        "منظور حالات الاستخدام لأهداف الجهات وخدماتها", "مخطط تدفق يوضح خطوات الخوارزمية وفروع القرار",
        "منظور نشر يربط المعالجات بعقد النظام الموزعة", "جسم إجراء يحدد متغيراته وعملياته المحلية",
    ]),
    "ch5_sdd_scope_not_lifecycle": ([
        "It applies across varied software application domains", "It requires one mandatory development lifecycle",
        "It is independent of a specific design methodology", "It defines SDD information and its arrangement",
    ], [
        "ينطبق على مجالات متعددة من تطبيقات البرمجيات", "يفرض دورة تطوير واحدة ملزمة على جميع المشاريع",
        "لا يشترط منهجية تصميم معينة خاصة بالنظام", "يحدد معلومات SDD وتنظيمها داخل وصف التصميم",
    ]),
    "ch5_sdd_scope_not_language": ([
        "Compiler settings used when implementing the software", "Information included in the software design description",
        "Applicability of design descriptions across systems", "Organization of information within the design description",
    ], [
        "إعدادات ضبط المترجم أثناء تنفيذ البرمجيات", "المعلومات التي يتضمنها وصف تصميم البرمجيات",
        "مجالات تطبيق أوصاف التصميم على الأنظمة", "تنظيم المعلومات داخل وصف تصميم البرمجيات",
    ]),
    "ch5_entity_vs_view": ([
        "Entities are described; views group attributes by concern", "An entity is a project team; a view is its schedule",
        "An entity is a test stage; a view is a release package", "An entity is a user role; a view is a project plan",
    ], [
        "الكيان يوصف، والمنظور ينظم سماته بحسب جانب التصميم", "الكيان فريق المشروع والمنظور جدول مواعيد التسليم",
        "الكيان مرحلة اختبار والمنظور حزمة إصدار البرنامج", "الكيان دور مستخدم والمنظور خطة المشروع العامة",
    ]),
    "ch5_sdd_entity_subordinates": ([
        "Subordinates: lower-level elements contained in the entity", "Dependencies: external design elements the entity relies on",
        "Purpose: the role this element fulfills in the design", "Data: information it stores, receives, or produces",
    ], [
        "التوابع: عناصر تصميم أدنى يضمها هذا الكيان", "الاعتماديات: عناصر تصميم خارجية يعتمد عليها الكيان",
        "الغرض: الدور الذي يؤديه هذا العنصر في التصميم", "البيانات: معلومات يخزنها أو يستقبلها أو ينتجها",
    ]),
    "ch5_sdd_function_view_note": ([
        "Decomposition view shows function hierarchy and roles", "Interface view defines public signatures and contracts",
        "Dependency view maps links among design entities", "Detailed view specifies algorithms and internal data",
    ], [
        "يعرض منظور التفكيك تسلسل الوظائف ومسؤوليات الوحدات", "يعرض منظور الواجهة التواقيع العامة وعقود التواصل",
        "يعرض منظور الاعتمادية الروابط بين كيانات التصميم", "يعرض منظور التفصيل الخوارزميات والبيانات الداخلية",
    ]),
})

BALANCED_OPTIONS.update({
    "ch5_fan_in_out": ([
        "Fan-in counts callers; fan-out counts modules called", "Fan-in counts outgoing calls; fan-out counts callers",
        "Both count stored fields and interface parameter values", "Both measure source size and runtime speed per module",
    ], [
        "Fan-in عدد مستدعيات الوحدة وFan-out عدد ما تستدعيه", "Fan-in عدد الاستدعاءات الصادرة وFan-out عدد مستدعيها",
        "كلاهما يقيس حقول البيانات ومعاملات الواجهة للوحدة", "كلاهما يقيس حجم الشيفرة وزمن تنفيذ كل وحدة برمجية",
    ]),
    "ch5_cc_independence_benefits": ([
        "Focused modules are easier to understand, test, and maintain", "Every module becomes independent of shared system behavior",
        "Cohesion automatically removes all dependencies between modules", "All communication disappears between cooperating components",
    ], [
        "يسهل فهم الوحدات المركزة واختبارها وصيانتها", "تنفصل كل وحدة تماماً عن سلوك النظام المشترك",
        "يزيل التماسك تلقائياً كل اعتماد بين الوحدات البرمجية", "يختفي كل تواصل بين المكونات التي تتعاون معاً",
    ]),
    "ch5_cc_logical_control_pair": ([
        "Logical cohesion may use a caller flag, creating control coupling", "Temporal cohesion groups same-time tasks and requires stamp coupling",
        "Functional cohesion serves one purpose through shared global coupling", "Communicational cohesion shares data through external coupling",
    ], [
        "قد يصاحب التماسك المنطقي اقتران تحكم بسبب علم المستدعي", "يجمع التماسك الزمني مهاماً متزامنة مع اقتران البنية",
        "يخدم التماسك الوظيفي غرضاً واحداً مع اقتران مشترك", "يستخدم التماسك الاتصالي بيانات مشتركة مع اقتران خارجي",
    ]),
    "ch5_ood_inheritance_without_polymorphism": ([
        "Inheritance can express a type relation without method overriding", "Inheritance requires every subtype to redefine shared methods",
        "Polymorphism and inheritance describe the same type feature", "A class cannot inherit unless several methods are overloaded",
    ], [
        "قد تمثل الوراثة علاقة أنواع حتى بلا إعادة تعريف الطرق", "تشترط الوراثة دائماً إعادة تعريف الطرق المشتركة كلها",
        "الوراثة وتعدد الأشكال هما الخاصية نفسها في التصميم", "لا يرث الصنف إلا مع تحميل الطرق المتعددة بالاسم نفسه",
    ]),
    "ch5_ood_class_quality": ([
        "Keep a class concept, state, and operations coherent", "Combine unrelated ideas to reduce the number of classes",
        "Expose internal representation as the class's public interface", "Use inheritance without a valid general-specialized relation",
    ], [
        "اجمع مفهوماً مترابطاً مع حالته وعملياته المناسبة", "ادمج مفاهيم غير مرتبطة لتقليل عدد الأصناف",
        "اكشف التمثيل الداخلي بوصفه الواجهة العامة للصنف", "استخدم الوراثة بلا علاقة صحيحة بين الأنواع",
    ]),
    "ch5_structural_layer": ([
        "Module boundaries, calls, and interface contracts", "Stepwise algorithms inside each individual procedure",
        "Processor assignments to physical deployment nodes", "Customer goals and planned user-facing release dates",
    ], [
        "حدود الوحدات وعلاقات الاستدعاء وعقود الواجهة", "تسلسل الخوارزمية في جسم كل إجراء برمجي",
        "توزيع المعالجات على عقد النشر المادية للنظام", "أهداف العميل ومواعيد إصدار الواجهة للمستخدم",
    ]),
    "ch5_procedural_layer": ([
        "It describes a module's internal algorithm and behavior", "It defines module boundaries and call relationships",
        "It assigns processors to software deployment nodes", "It records customer goals and planned release dates",
    ], [
        "تصف الخوارزمية الداخلية وطريقة تنفيذ كل وحدة", "تحدد حدود الوحدات وعلاقات الاستدعاء بينها",
        "توزع المعالجات على عقد النشر البرمجية", "تسجل أهداف العميل ومواعيد الإصدار المخطط",
    ]),
})

OPTION_EXPANSIONS = {
    "Closed system": ("Closed system with no environmental exchange", "نظام مغلق بلا تبادل مع البيئة"),
    "Open system": ("Open system exchanging with its environment", "نظام مفتوح يتبادل مع البيئة"),
    "Interactive system": ("Interactive system responding to external actors", "نظام تفاعلي يستجيب لجهات خارجية"),
    "Distributed system": ("Distributed system across connected locations", "نظام موزع عبر مواقع مترابطة"),
    "Data coupling": ("Data coupling through simple parameter values", "اقتران البيانات عبر قيم معامل بسيطة"),
    "Stamp coupling": ("Stamp coupling through an underused composite record", "اقتران بنية مركبة مع استخدام جزء منها"),
    "Control coupling": ("Control coupling through caller-selected flags", "اقتران التحكم عبر علم يوجه التفرع"),
    "External coupling": ("External coupling through a shared protocol", "اقتران خارجي بسبب بروتوكول مشترك"),
    "Common coupling": ("Common coupling through shared global state", "اقتران مشترك عبر الحالة العامة"),
    "Content coupling": ("Content coupling through access to private code", "اقتران المحتوى بالتدخل في الشيفرة الداخلية"),
    "Coincidental cohesion": ("Coincidental cohesion groups unrelated elements", "التماسك العشوائي يجمع عناصر غير مترابطة"),
    "Logical cohesion": ("Logical cohesion lets a selector choose related tasks", "التماسك المنطقي يتيح اختيار مهمة من فئة متقاربة"),
    "Temporal cohesion": ("Temporal cohesion groups tasks by execution time", "التماسك الزمني يجمع المهام بحسب وقت تنفيذها"),
    "Procedural cohesion": ("Procedural cohesion links tasks by control order", "التماسك الإجرائي يربط المهام بترتيب التحكم"),
    "Communicational cohesion": ("Communicational cohesion groups tasks using the same data", "التماسك الاتصالي يجمع مهاماً تستخدم البيانات نفسها"),
    "Sequential cohesion": ("Sequential cohesion passes one task's output to the next", "التماسك التسلسلي يمرر ناتج مهمة إلى التالية"),
    "Functional cohesion": ("Functional cohesion makes every part serve one task", "التماسك الوظيفي يجعل كل جزء يخدم مهمة واحدة"),
    "Modular protection": ("Modular protection confines faults within one component", "الحماية النمطية تحصر الأعطال داخل مكون واحد"),
    "Modular continuity": ("Modular continuity localizes small requirement changes", "الاستمرارية النمطية تحصر التغييرات الصغيرة"),
    "Modular understandability": ("Modular understandability supports isolated reading", "قابلية الفهم النمطية تتيح فهم المكون مستقلاً"),
    "Modular composability": ("Modular composability combines self-contained parts", "قابلية التركيب النمطية تجمع أجزاء مستقلة"),
    "Modular decomposability": ("Modular decomposability breaks complex problems into parts", "قابلية التفكيك النمطية تقسم المشكلة المعقدة"),
    "Top-down design": ("Top-down design refines system goals into details", "التصميم التنازلي ينقح أهداف النظام إلى تفاصيل"),
    "Bottom-up design": ("Bottom-up design combines basic parts into systems", "التصميم التصاعدي يجمع الأجزاء الأساسية في أنظمة"),
    "Hybrid design": ("Hybrid design combines both design directions", "التصميم الهجين يجمع اتجاهي التصميم"),
    "Embedded design": ("Embedded design places software within a device", "التصميم المضمن يضع البرمجيات داخل جهاز"),
    "Inheritance": ("Inheritance links a specialized class to a general one", "تربط الوراثة صنفاً متخصصاً بآخر عام"),
    "Encapsulation": ("Encapsulation hides internal state behind an interface", "يخفي التغليف الحالة الداخلية خلف واجهة"),
    "Message passing": ("Message passing requests an operation from another object", "يطلب تمرير الرسائل عملية من كائن آخر"),
    "Temporal cohesion": ("Temporal cohesion groups tasks by execution time", "التماسك الزمني يجمع المهام بحسب وقت تنفيذها"),
    "The interface view": ("Interface view describes signatures and communication contracts", "يعرض منظور الواجهة التواقيع وعقود التواصل"),
    "The dependency view": ("Dependency view describes relationships among design parts", "يعرض منظور الاعتمادية العلاقات بين أجزاء التصميم"),
    "The detailed design view": ("Detailed design view describes algorithms and internal data", "يعرض منظور التفصيل الخوارزميات والبيانات الداخلية"),
    "The decomposition view": ("Decomposition view describes the component hierarchy", "يعرض منظور التفكيك التسلسل الهرمي للمكونات"),
    "Interface view": ("Interface view describes signatures and communication contracts", "يعرض منظور الواجهة التواقيع وعقود التواصل"),
    "Dependency view": ("Dependency view describes relationships among design parts", "يعرض منظور الاعتمادية العلاقات بين أجزاء التصميم"),
    "Detailed design view": ("Detailed design view describes algorithms and internal data", "يعرض منظور التفصيل الخوارزميات والبيانات الداخلية"),
    "Decomposition view": ("Decomposition view describes the component hierarchy", "يعرض منظور التفكيك التسلسل الهرمي للمكونات"),
    "An activity diagram": ("An activity diagram showing workflow and control", "مخطط نشاط يوضح سير العمل والتحكم"),
    "A deployment diagram": ("A deployment diagram mapping software to hardware", "مخطط نشر يوزع البرمجيات على الأجهزة"),
    "A flowchart": ("A flowchart showing procedural steps and branches", "مخطط تدفق يوضح الخطوات الإجرائية وفروعها"),
    "A class diagram": ("A class diagram showing types and their relations", "مخطط أصناف يوضح الأنواع والعلاقات بينها"),
    "A class diagram": ("A class diagram showing types and their relations", "مخطط أصناف يوضح الأنواع والعلاقات بينها"),
    "Class diagram": ("Class diagram showing types and their relations", "مخطط أصناف يوضح الأنواع والعلاقات بينها"),
    "Flowchart": ("Flowchart showing procedural steps and branches", "مخطط تدفق يوضح الخطوات الإجرائية وفروعها"),
    "Use-Case Diagram": ("Use-Case Diagram showing actor goals and services", "مخطط حالات استخدام يعرض أهداف الجهات والخدمات"),
    "A use-case model with actors and use cases": ("A use-case model identifying actors, goals, and services", "نموذج حالات استخدام يحدد الجهات والأهداف والخدمات"),
    "A user workflow showing visible actions": ("A user workflow showing visible steps and outcomes", "سير مستخدم يوضح الخطوات والنتائج الظاهرة"),
    "Technical design": ("Technical design specifying internal construction decisions", "تصميم فني يحدد قرارات البناء الداخلية"),
    "Conceptual design": ("Conceptual design describing user-visible capabilities", "تصميم مفهومي يصف القدرات الظاهرة للمستخدم"),
    "Maintainability": ("Maintainability across later requirement changes", "قابلية الصيانة عند تغير المتطلبات لاحقاً"),
    "Visual novelty": ("Visual novelty in the delivered user interface", "الجدة البصرية في واجهة المستخدم"),
    "A test driver that calls the component": ("A test driver that invokes the lower-level component", "برنامج اختبار يستدعي المكون ذي المستوى الأدنى"),
    "A test stub that replaces its callers": ("A test stub that simulates an unfinished component", "بديل اختباري يحاكي مكوناً غير مكتمل"),
    "The interface view": ("Interface view describes signatures and communication contracts", "يعرض منظور الواجهة التواقيع وعقود التواصل"),
    "The dependency view": ("Dependency view describes relationships among design parts", "يعرض منظور الاعتمادية العلاقات بين أجزاء التصميم"),
    "The detailed design view": ("Detailed design view describes algorithms and internal data", "يعرض منظور التفصيل الخوارزميات والبيانات الداخلية"),
    "The decomposition view": ("Decomposition view describes the component hierarchy", "يعرض منظور التفكيك التسلسل الهرمي للمكونات"),
    "A user workflow showing visible actions": ("A user workflow showing visible steps and outcomes", "سير مستخدم يوضح الخطوات والنتائج الظاهرة"),
}


def q(cid, bloom, en, ar, en_options, ar_options, exp_en, exp_ar):
    # Expand taxonomy-only option sets into parallel definitions. Mixed sets
    # retain their authored wording so one correct term is not uniquely longer.
    if cid in BALANCED_OPTIONS:
        expanded_en, expanded_ar = BALANCED_OPTIONS[cid]
    elif all(option_en in OPTION_EXPANSIONS for option_en in en_options):
        expanded_en = [OPTION_EXPANSIONS[option_en][0] for option_en in en_options]
        expanded_ar = [OPTION_EXPANSIONS[option_en][1] for option_en in en_options]
    else:
        expanded_en, expanded_ar = list(en_options), list(ar_options)
    expected = EXPECTED_CORRECT_FIRST.get(cid)
    if expected is not None and expanded_en[0] != expected:
        raise ValueError(f"{cid}: intended correct option is not first")
    return (cid, bloom, en, ar, expanded_en, expanded_ar, exp_en, exp_ar)


BANKS = [
    {
        "id": "Quiz_Ch05_T01_What_Is_Design",
        "title": "What Is Software Design?",
        "title_ar": "ما تصميم البرمجيات؟",
        "items": [
            q("ch5_design_bridge", "Understand", "What does software design turn into a technical blueprint?", "إلى ماذا يحوّل تصميم البرمجيات المتطلبات؟", ["The approved software requirements", "The final source code", "The completed test report", "The deployed user interface"], ["المتطلبات البرمجية المعتمدة", "الشيفرة البرمجية النهائية", "تقرير الاختبار المكتمل", "واجهة المستخدم المنشورة"], "Design translates the requirements into a blueprint that guides construction.", "يحوّل التصميم المتطلبات إلى مخطط يوجّه بناء البرمجيات."),
            q("ch5_design_question", "Understand", "Which question is primarily answered during software design?", "أي سؤال يجيب عنه التصميم البرمجي أساساً؟", ["How the required system will be built", "What problem the user experiences", "Who approves the project budget", "When the finished product is released"], ["كيف سيُبنى النظام المطلوب", "ما المشكلة التي يواجهها المستخدم", "من يعتمد ميزانية المشروع", "متى يُنشر المنتج المكتمل"], "Requirements describe what is needed; design describes how the solution is structured.", "تصف المتطلبات ما هو مطلوب، بينما يصف التصميم كيفية بناء الحل."),
            q("ch5_design_outputs", "Understand", "Which set best represents technical design outputs?", "أي مجموعة تمثل مخرجات التصميم الفني؟", ["Architecture, interfaces, data, and procedures", "Screens, workflows, branding, and user help", "Source files, executables, and release packages", "Test cases, defect logs, and acceptance records"], ["المعمارية والواجهات والبيانات والإجراءات", "الشاشات وسير العمل والهوية وإرشادات المستخدم", "ملفات الشيفرة والبرامج وحزم الإصدار", "حالات الاختبار وسجلات العيوب ومحاضر القبول"], "A technical design describes structure, interfaces, data, and procedural details.", "يصف التصميم الفني البنية والواجهات والبيانات والتفاصيل الإجرائية."),
            q("ch5_design_sdlc", "Understand", "Where does software design sit in the development flow?", "أين يقع التصميم ضمن تسلسل تطوير البرمجيات؟", ["After requirements and before implementation", "After deployment and before requirements", "Before feasibility and after maintenance", "Inside coding after unit testing"], ["بعد المتطلبات وقبل التنفيذ", "بعد النشر وقبل المتطلبات", "قبل الجدوى وبعد الصيانة", "داخل البرمجة بعد اختبار الوحدة"], "Design follows requirements analysis and provides the plan used by implementation.", "يأتي التصميم بعد تحليل المتطلبات ويوفر الخطة التي يتبعها التنفيذ."),
            q("ch5_design_not_code", "Understand", "What distinguishes a design description from working code?", "ما الذي يميّز وصف التصميم عن الشيفرة العاملة؟", ["It specifies construction decisions before implementation", "It executes the required functions for end users", "It records only defects found after deployment", "It replaces the need to analyze requirements"], ["يحدد قرارات البناء قبل التنفيذ", "ينفّذ الوظائف المطلوبة للمستخدمين", "يسجل العيوب المكتشفة بعد النشر فقط", "يلغي الحاجة إلى تحليل المتطلبات"], "Design records a technical plan; implementation turns that plan into executable software.", "يسجل التصميم خطة فنية، ويحوّلها التنفيذ إلى برمجيات قابلة للتشغيل."),
            q("ch5_closed_system", "Understand", "A system with no interaction across its external boundary is a...", "النظام الذي لا يتفاعل عبر حدوده الخارجية يسمى...", ["Closed system", "Open system", "Distributed system", "Interactive system"], ["نظام مغلق", "نظام مفتوح", "نظام موزع", "نظام تفاعلي"], "A closed system has no input from or output to its environment.", "لا يستقبل النظام المغلق مدخلات من بيئته ولا يرسل إليها مخرجات."),
            q("ch5_design_structure", "Understand", "Which architectural concern belongs in a software design?", "أي جانب معماري يدخل ضمن تصميم البرمجيات؟", ["How components are arranged and communicate", "How project invoices are approved and paid", "How end users are trained after delivery", "How marketing chooses a product name"], ["كيفية ترتيب المكونات وتواصلها", "كيفية اعتماد فواتير المشروع وتسديدها", "كيفية تدريب المستخدمين بعد التسليم", "كيفية اختيار التسويق اسماً للمنتج"], "Software design specifies the system's technical organization and component relationships.", "يحدد تصميم البرمجيات التنظيم الفني للنظام والعلاقات بين مكوناته."),
            q("ch5_design_construction", "Apply", "What does a construction team use the design blueprint to determine?", "ما الذي يستنتجه فريق البناء من مخطط التصميم؟", ["The structures and interfaces to implement", "The user problem to discover from scratch", "The final project price from market demand", "The production defects to hide from review"], ["البنى والواجهات التي ينبغي تنفيذها", "مشكلة المستخدم التي تُكتشف من جديد", "السعر النهائي للمشروع من طلب السوق", "عيوب الإنتاج التي ينبغي إخفاؤها عن المراجعة"], "The blueprint turns requirements into actionable construction decisions.", "يحوّل المخطط المتطلبات إلى قرارات قابلة للتنفيذ أثناء البناء."),
        ],
    },
    {
        "id": "Quiz_Ch05_T02_Conceptual_And_Technical_Design",
        "title": "Conceptual and Technical Design",
        "title_ar": "التصميم المفهومي والتصميم الفني",
        "items": [
            q("ch5_conceptual_what", "Understand", "What does conceptual design emphasize?", "على ماذا يركز التصميم المفهومي؟", ["The capabilities visible to users", "The internal module call hierarchy", "The algorithms chosen by programmers", "The memory layout used at runtime"], ["القدرات التي تظهر للمستخدمين", "تسلسل استدعاء الوحدات الداخلي", "الخوارزميات التي يختارها المبرمجون", "تنظيم الذاكرة أثناء التشغيل"], "Conceptual design explains what the system offers from an external user perspective.", "يشرح التصميم المفهومي ما يقدمه النظام من منظور المستخدم الخارجي."),
            q("ch5_technical_how", "Understand", "What does technical design emphasize?", "على ماذا يركز التصميم الفني؟", ["How the architecture realizes required behavior", "What business outcome the customer expects", "Which screen colors users prefer most", "Why the organization approved the project"], ["كيفية تحقيق المعمارية للسلوك المطلوب", "النتيجة التجارية التي يتوقعها العميل", "ألوان الشاشات التي يفضلها المستخدمون", "سبب اعتماد المؤسسة للمشروع"], "Technical design describes how the system will implement its required capabilities.", "يصف التصميم الفني كيفية تنفيذ النظام لقدراته المطلوبة."),
            q("ch5_conceptual_audience", "Understand", "Who is the primary audience for a conceptual design?", "من الجمهور الأساسي للتصميم المفهومي؟", ["Customers and system users", "Compiler and linker developers", "Database storage administrators", "Hardware maintenance technicians"], ["العملاء ومستخدمو النظام", "مطورو المترجمات والروابط", "مسؤولو تخزين قواعد البيانات", "فنيو صيانة الأجهزة"], "Conceptual design communicates system behavior in terms accessible to customers and users.", "يوصل التصميم المفهومي سلوك النظام بلغة يفهمها العملاء والمستخدمون."),
            q("ch5_technical_audience", "Understand", "Who primarily uses the technical design description?", "من يستخدم وصف التصميم الفني أساساً؟", ["Builders who implement system components", "Customers who approve screen workflows", "Marketers who choose product positioning", "Operators who schedule office meetings"], ["فريق البناء الذي ينفذ مكونات النظام", "العملاء الذين يعتمدون سير الشاشات", "المسوّقون الذين يحددون موقع المنتج", "المشغلون الذين يجدولون اجتماعات المكتب"], "Technical design gives implementers the details needed to construct the system.", "يمنح التصميم الفني المنفذين التفاصيل اللازمة لبناء النظام."),
            q("ch5_conceptual_artifacts", "Understand", "Which artifact best fits conceptual design?", "أي مخرج يلائم التصميم المفهومي أكثر؟", ["A user workflow showing visible actions", "A method signature defining parameters", "A database schema defining stored fields", "A module hierarchy defining control calls"], ["سير مستخدم يوضح الإجراءات الظاهرة", "توقيع طريقة يحدد المعاملات", "مخطط قاعدة بيانات يحدد الحقول", "تسلسل وحدات يحدد استدعاءات التحكم"], "Workflows describe user-visible behavior; signatures and schemas are technical details.", "يصف سير العمل السلوك الظاهر للمستخدم، أما التواقيع والمخططات فهي تفاصيل فنية."),
            q("ch5_technical_artifacts", "Apply", "A team must define module interfaces and data structures; which view fits?", "يريد فريق تحديد واجهات الوحدات وبنى البيانات؛ أي تصميم يلائمه؟", ["Technical design", "Conceptual design", "Marketing design", "Operational training"], ["التصميم الفني", "التصميم المفهومي", "التصميم التسويقي", "التدريب التشغيلي"], "Interfaces and data structures specify internal implementation decisions.", "تحدد الواجهات وبنى البيانات قرارات التنفيذ الداخلية."),
            q("ch5_conceptual_language", "Understand", "Which language best suits a conceptual design?", "أي لغة تناسب التصميم المفهومي أكثر؟", ["Business terms describing user goals", "Implementation terms describing method calls", "Storage terms describing table indexes", "Hardware terms describing device registers"], ["مصطلحات أعمال تصف أهداف المستخدم", "مصطلحات تنفيذ تصف استدعاء الطرق", "مصطلحات تخزين تصف فهارس الجداول", "مصطلحات أجهزة تصف سجلات المعالج"], "Conceptual design should express capabilities in the customer's domain language.", "ينبغي أن يعبّر التصميم المفهومي عن القدرات بلغة مجال العميل."),
            q("ch5_conceptual_technical_translation", "Analyze", "What is the designer's role between conceptual and technical views?", "ما دور المصمم بين المنظورين المفهومي والفني؟", ["Translate user expectations into buildable structure", "Replace user needs with preferred technology", "Turn architecture details into marketing slogans", "Hide system behavior from implementation teams"], ["ترجمة توقعات المستخدم إلى بنية قابلة للبناء", "استبدال حاجات المستخدم بتقنية مفضلة", "تحويل تفاصيل المعمارية إلى شعارات تسويقية", "إخفاء سلوك النظام عن فرق التنفيذ"], "The designer connects the external view of required behavior with an internal technical plan.", "يربط المصمم منظور السلوك المطلوب خارجياً بالخطة الفنية الداخلية."),
        ],
    },
    {
        "id": "Quiz_Ch05_T03_Objectives_Of_Design",
        "title": "Objectives of Software Design",
        "title_ar": "أهداف التصميم البرمجي",
        "items": [
            q("ch5_design_objectives_set", "Understand", "Which set states the software design objectives?", "أي مجموعة تمثل أهداف التصميم كما وردت في الكتاب؟", ["Correct and complete, understandable, right-level, maintainable", "Fast and portable, minimal, secure, fully reusable", "Cheap and familiar, automated, distributed, fault-free", "Compact and generic, fashionable, independent, measurable"], ["صحيح وكامل ومفهوم وبالمستوى المناسب وقابل للصيانة", "سريع ومحمول ومختصر وآمن وقابل لإعادة الاستخدام كلياً", "رخيص ومألوف ومؤتمت وموزع وخالٍ من الأعطال", "مدمج وعام وحديث ومستقل وقابل للقياس"], "The stated objectives are correctness and completeness, understandability, suitable level, and maintainability.", "أهداف التصميم هي الصحة والاكتمال وقابلية الفهم والمستوى المناسب وقابلية الصيانة."),
            q("ch5_objective_correct_complete", "Understand", "What does a correct and complete design preserve?", "ماذا يحافظ عليه التصميم الصحيح والكامل؟", ["The required behavior and relevant requirements", "Every possible feature a future user might request", "Only the screens already approved by marketing", "Implementation details unrelated to stated needs"], ["السلوك المطلوب والمتطلبات ذات الصلة", "كل ميزة قد يطلبها مستخدم مستقبلي", "الشاشات التي اعتمدها التسويق فقط", "تفاصيل تنفيذ لا ترتبط بالحاجات المحددة"], "Correctness and completeness require the design to represent the specified needs without omissions.", "تتطلب الصحة والاكتمال أن يمثل التصميم الحاجات المحددة من دون إغفال."),
            q("ch5_objective_understandable", "Understand", "A design is understandable when its structure is...", "يكون التصميم قابلاً للفهم عندما تكون بنيته...", ["Clear enough for its intended readers", "Hidden from everyone except its original author", "Expanded with every low-level coding statement", "Written only in vendor-specific machine terms"], ["واضحة بما يكفي لقرائها المقصودين", "مخفية عن الجميع عدا مؤلفها الأصلي", "موسعة بكل تعليمة برمجية منخفضة المستوى", "مكتوبة بمصطلحات آلة خاصة بمورّد واحد"], "Understandability depends on clear organization at the intended level of detail.", "تعتمد قابلية الفهم على وضوح التنظيم وبالمستوى المقصود من التفاصيل."),
            q("ch5_objective_right_level", "Understand", "What does “at the right level” mean for a design?", "ماذا يعني أن يكون التصميم بالمستوى المناسب؟", ["Its detail matches the decision and its audience", "It contains every implementation statement in full", "It omits all structure until coding is finished", "It uses the same detail for every stakeholder"], ["أن تلائم تفاصيله القرار وجمهوره", "أن يتضمن كل تعليمة تنفيذية كاملة", "أن يحذف البنية حتى اكتمال البرمجة", "أن يستخدم التفصيل نفسه لكل أصحاب المصلحة"], "The appropriate level provides enough detail for its purpose without forcing one depth everywhere.", "يوفر المستوى المناسب ما يكفي لغرضه من دون فرض عمق واحد على الجميع."),
            q("ch5_objective_maintainable", "Understand", "Which design objective most directly supports future changes?", "أي هدف تصميمي يدعم التغييرات المستقبلية مباشرة؟", ["Maintainability", "Visual novelty", "Maximum implementation detail", "Minimum stakeholder communication"], ["قابلية الصيانة", "الجِدة البصرية", "أقصى تفصيل للتنفيذ", "أقل تواصل مع أصحاب المصلحة"], "Maintainable structure helps people understand and change the system over time.", "تساعد البنية القابلة للصيانة على فهم النظام وتعديله بمرور الوقت."),
            q("ch5_objective_traceability", "Apply", "A design omits a required behavior from the SRS; which objective failed?", "أغفل التصميم سلوكاً مطلوباً في SRS؛ أي هدف لم يتحقق؟", ["Correctness and completeness", "Appropriate level of detail", "Ease of visual presentation", "Technical independence from users"], ["الصحة والاكتمال", "ملاءمة مستوى التفاصيل", "سهولة العرض البصري", "الاستقلال الفني عن المستخدمين"], "An omitted requirement makes the design incomplete and can make it incorrect.", "يجعل إغفال المتطلب التصميم غير مكتمل وقد يجعله غير صحيح."),
            q("ch5_objective_audience", "Apply", "A design is too abstract for implementers to build from; which objective is unmet?", "التصميم مجرد أكثر مما يحتاجه المنفذون للبناء؛ أي هدف لم يتحقق؟", ["The right level of detail", "Requirements completeness", "External system openness", "Runtime data protection"], ["مستوى التفاصيل المناسب", "اكتمال المتطلبات", "انفتاح النظام خارجياً", "حماية بيانات التشغيل"], "The design must give implementers sufficient detail at the level needed for construction.", "ينبغي أن يقدم التصميم للمنفذين تفاصيل كافية وبالمستوى اللازم للبناء."),
            q("ch5_objectives_not_exhaustiveness", "Evaluate", "Which interpretation best respects the design objectives?", "أي تفسير ينسجم أكثر مع أهداف التصميم؟", ["Give enough detail for clear, correct construction", "Specify every code statement before analysis ends", "Optimize one quality while ignoring all others", "Replace requirement coverage with extra features"], ["توفير تفاصيل تكفي لبناء واضح وصحيح", "تحديد كل تعليمة قبل انتهاء التحليل", "تحسين خاصية مع تجاهل جميع الخصائص الأخرى", "استبدال تغطية المتطلبات بميزات إضافية"], "The objectives call for suitable, understandable detail that remains correct, complete, and maintainable.", "تتطلب الأهداف تفاصيل مناسبة ومفهومة مع الحفاظ على الصحة والاكتمال والصيانة."),
        ],
    },
    {
        "id": "Quiz_Ch05_T04_Why_Design_Matters",
        "title": "Why Software Design Matters",
        "title_ar": "أهمية التصميم البرمجي",
        "items": [
            q("ch5_design_importance_bridge", "Understand", "Why is design an important engineering activity?", "لماذا يعد التصميم نشاطاً هندسياً مهماً؟", ["It turns requirements into a construction plan", "It replaces the need to define user needs", "It guarantees that implementation has no defects", "It makes verification unnecessary after coding"], ["يحوّل المتطلبات إلى خطة للبناء", "يلغي الحاجة إلى تحديد حاجات المستخدم", "يضمن خلو التنفيذ من العيوب", "يجعل التحقق غير ضروري بعد البرمجة"], "Design gives implementation a reasoned structure derived from the requirements.", "يمنح التصميم التنفيذ بنية مدروسة مشتقة من المتطلبات."),
            q("ch5_design_quality", "Understand", "What can a software design strongly influence?", "ما الذي يستطيع التصميم البرمجي التأثير فيه بقوة؟", ["The quality and maintainability of the result", "The laws governing the customer's industry", "The number of users in the target market", "The electricity available at the deployment site"], ["جودة المنتج وقابليته للصيانة", "القوانين التي تحكم مجال العميل", "عدد مستخدمي السوق المستهدف", "الكهرباء المتاحة في موقع النشر"], "Architectural choices influence important quality properties, including maintainability.", "تؤثر الخيارات المعمارية في خصائص جودة مهمة، ومنها قابلية الصيانة."),
            q("ch5_design_early_decisions", "Analyze", "Why should major structural decisions be made before coding spreads?", "لماذا ينبغي حسم القرارات البنيوية قبل انتشار البرمجة؟", ["Shared decisions can shape many components", "Every design choice becomes irrelevant after coding", "Requirements stop changing once a class is created", "Testing cannot identify defects in implemented code"], ["قد تؤثر القرارات المشتركة في مكونات كثيرة", "يصبح كل قرار تصميمي غير مهم بعد البرمجة", "تتوقف المتطلبات عن التغيير بعد إنشاء صنف", "لا يستطيع الاختبار كشف عيوب الشيفرة المنفذة"], "A structural decision may affect interfaces and dependencies throughout the system.", "قد يؤثر القرار البنيوي في الواجهات والاعتماديات عبر النظام."),
            q("ch5_design_quality_three", "Understand", "Which three qualities are attributed to Vitruvius in the design discussion?", "ما الصفات الثلاث المنسوبة إلى Vitruvius في نقاش التصميم؟", ["Durability, utility, and charm", "Speed, portability, and security", "Accuracy, usability, and modularity", "Cost, schedule, and productivity"], ["المتانة والمنفعة والجاذبية", "السرعة وقابلية النقل والأمن", "الدقة وقابلية الاستخدام والنمطية", "الكلفة والجدول والإنتاجية"], "The cited design discussion presents durability, utility, and charm as three qualities.", "يعرض نقاش التصميم المتانة والمنفعة والجاذبية بوصفها ثلاث صفات."),
            q("ch5_design_vs_coding", "Understand", "Which statement best separates design from coding?", "أي عبارة تميّز التصميم عن البرمجة بأفضل صورة؟", ["Design plans the solution; coding realizes it", "Design tests the product; coding approves its scope", "Design gathers requirements; coding selects the users", "Design deploys the service; coding maintains its budget"], ["يخطط التصميم للحل وتحققه البرمجة", "يختبر التصميم المنتج وتعتمد البرمجة نطاقه", "يجمع التصميم المتطلبات وتختار البرمجة مستخدميه", "ينشر التصميم الخدمة وتدير البرمجة ميزانيتها"], "Design describes the solution structure, while coding implements that structure.", "يصف التصميم بنية الحل، بينما تنفذ البرمجة تلك البنية."),
            q("ch5_design_construction_errors", "Analyze", "How can a design blueprint help a construction team?", "كيف يساعد مخطط التصميم فريق البناء؟", ["It clarifies component roles before implementation", "It removes the need to communicate interfaces", "It proves every requirement is already validated", "It prevents all maintenance work after release"], ["يوضح أدوار المكونات قبل التنفيذ", "يلغي الحاجة إلى توضيح الواجهات", "يثبت اعتماد كل متطلب مسبقاً", "يمنع كل أعمال الصيانة بعد الإصدار"], "A clear design helps builders coordinate component responsibilities and interfaces.", "يساعد التصميم الواضح المنفذين على تنسيق مسؤوليات المكونات وواجهاتها."),
            q("ch5_design_maintainability", "Apply", "A small policy change forces edits across many unrelated components; what design value was weak?", "تغيير بسيط في سياسة يفرض تعديلات على مكونات غير مترابطة؛ ما القيمة الضعيفة؟", ["Maintainability through localized decisions", "Conceptual scope through user workflows", "External openness through system boundaries", "Deployment clarity through physical nodes"], ["قابلية الصيانة عبر حصر التغييرات", "النطاق المفهومي عبر سير المستخدم", "الانفتاح الخارجي عبر حدود النظام", "وضوح النشر عبر العقد المادية"], "A maintainable design localizes changes rather than spreading them across unrelated parts.", "يحصر التصميم القابل للصيانة التغييرات بدلاً من نشرها في أجزاء غير مترابطة."),
            q("ch5_design_not_guarantee", "Evaluate", "What is the safest claim about a well-prepared design?", "ما الادعاء الأدق بشأن التصميم المعد جيداً؟", ["It guides construction but cannot guarantee defect-free code", "It removes all uncertainty from future maintenance", "It proves every implementation choice will be optimal", "It prevents requirements from changing after approval"], ["يوجه البناء لكنه لا يضمن شيفرة خالية من العيوب", "يزيل كل عدم يقين عن الصيانة المستقبلية", "يثبت أن كل خيار تنفيذ سيكون مثالياً", "يمنع تغير المتطلبات بعد اعتمادها"], "Design improves the basis for implementation; coding and verification still matter.", "يحسن التصميم أساس التنفيذ، لكن البرمجة والتحقق يظلان ضروريين."),
        ],
    },
    {
        "id": "Quiz_Ch05_T05_Modularity",
        "title": "Modularity and Modular Quality",
        "title_ar": "النمطية وجودة التقسيم",
        "items": [
            q("ch5_modularity_definition", "Understand", "What does modularity mean in software architecture?", "ماذا تعني النمطية في معمارية البرمجيات؟", ["Decomposing a system into cohesive, loosely linked units", "Combining every responsibility into one shared unit", "Duplicating each function in every component", "Removing interfaces between all system parts"], ["تقسيم النظام إلى وحدات متماسكة قليلة الترابط", "جمع كل المسؤوليات في وحدة مشتركة واحدة", "تكرار كل وظيفة في جميع المكونات", "إزالة الواجهات بين أجزاء النظام كلها"], "Modularity organizes a system as distinct components with focused roles and defined interactions.", "تنظم النمطية النظام في مكونات متميزة ذات أدوار محددة وتفاعلات واضحة."),
            q("ch5_meyer_criteria", "Understand", "Which set contains Meyer's five modularity criteria?", "أي مجموعة تضم معايير Meyer الخمسة للنمطية؟", ["Decomposability, composability, understandability, continuity, protection", "Accuracy, productivity, portability, security, interoperability", "Inheritance, abstraction, message passing, reuse, polymorphism", "Identification, purpose, processing, resources, deployment"], ["قابلية التفكيك والتركيب والفهم والاستمرارية والحماية", "الدقة والإنتاجية والنقل والأمن والتشغيل البيني", "الوراثة والتجريد وتمرير الرسائل وإعادة الاستخدام وتعدد الأشكال", "التعريف والهدف والمعالجة والموارد والنشر"], "Meyer's criteria evaluate whether components can be separated, reused, understood, changed, and contained.", "تقيّم معايير Meyer إمكان فصل المكونات وإعادة استخدامها وفهمها وتعديلها وحصر أعطالها."),
            q("ch5_modular_continuity", "Apply", "A small requirement change affects one isolated component; which criterion is shown?", "أثر تغيير متطلب صغير في مكون معزول؛ أي معيار ظهر؟", ["Modular continuity", "Modular composability", "Modular protection", "Modular decomposability"], ["الاستمرارية النمطية", "قابلية التركيب النمطية", "الحماية النمطية", "قابلية التفكيك النمطية"], "Continuity localizes the effect of a small requirement change.", "تحصر الاستمرارية أثر التغيير الصغير في المتطلب داخل موضع محدد."),
            q("ch5_modular_protection", "Apply", "A fault stays inside its originating component; which criterion does this illustrate?", "بقي عطل داخل المكون الذي بدأ فيه؛ أي معيار يوضحه ذلك؟", ["Modular protection", "Modular continuity", "Modular understandability", "Modular composability"], ["الحماية النمطية", "الاستمرارية النمطية", "قابلية الفهم النمطية", "قابلية التركيب النمطية"], "Protection confines the consequences of a fault or exceptional condition.", "تحصر الحماية نتائج العطل أو الحالة الاستثنائية ضمن المكون."),
            q("ch5_modular_understandability", "Understand", "A component can be understood without reading its neighbors; this supports...", "يمكن فهم مكون من دون قراءة جيرانه؛ وهذا يحقق...", ["Modular understandability", "Modular decomposability", "Modular protection", "Modular continuity"], ["قابلية الفهم النمطية", "قابلية التفكيك النمطية", "الحماية النمطية", "الاستمرارية النمطية"], "Understandability means each component can be comprehended in isolation.", "تعني قابلية الفهم إمكان استيعاب كل مكون بصورة مستقلة."),
            q("ch5_modular_composability", "Understand", "What does modular composability enable?", "ما الذي تتيحه قابلية التركيب النمطية؟", ["Combining self-contained components in new systems", "Changing every component when one rule changes", "Reading all internal code before using a component", "Sharing unrestricted data across every component"], ["تركيب مكونات مستقلة لبناء أنظمة جديدة", "تغيير كل مكون عند تعديل قاعدة واحدة", "قراءة الشيفرة الداخلية قبل استخدام أي مكون", "مشاركة بيانات غير مقيدة بين جميع المكونات"], "Composability supports reuse by allowing self-contained parts to be assembled.", "تدعم قابلية التركيب إعادة الاستخدام من خلال تجميع أجزاء مستقلة."),
            q("ch5_modular_decomposability", "Understand", "What does modular decomposability accomplish?", "ماذا تحقق قابلية التفكيك النمطية؟", ["Breaking a complex problem into smaller subproblems", "Combining finished products without defined interfaces", "Concealing every requirement from implementation teams", "Moving all responsibilities into the user interface"], ["تقسيم مشكلة معقدة إلى مشكلات فرعية أصغر", "جمع منتجات مكتملة بلا واجهات محددة", "إخفاء كل المتطلبات عن فرق التنفيذ", "نقل كل المسؤوليات إلى واجهة المستخدم"], "Decomposability separates a complex problem into manageable parts.", "تفصل قابلية التفكيك المشكلة المعقدة إلى أجزاء يسهل التعامل معها."),
            q("ch5_modularity_tradeoff", "Evaluate", "What is the main risk of decomposing a system into too many tiny parts?", "ما الخطر الأبرز من تقسيم النظام إلى أجزاء صغيرة أكثر من اللازم؟", ["Coordination overhead can outweigh local simplicity", "Every part automatically becomes reusable", "All dependencies disappear from the architecture", "Testing becomes unnecessary for the system"], ["قد يفوق عبء التنسيق فائدة البساطة المحلية", "يصبح كل جزء قابلاً لإعادة الاستخدام تلقائياً", "تختفي جميع الاعتماديات من المعمارية", "يصبح اختبار النظام غير ضروري"], "Modular design balances manageable parts with the cost of their interactions.", "يوازن التصميم النمطي بين سهولة إدارة الأجزاء وكلفة تفاعلاتها."),
        ],
    },
    {
        "id": "Quiz_Ch05_T06_Module_Coupling",
        "title": "Module Coupling",
        "title_ar": "الاقتران بين الوحدات",
        "items": [
            q("ch5_coupling_definition", "Understand", "What does module coupling measure?", "ماذا يقيس الاقتران بين الوحدات؟", ["Dependence between separate software components", "Functional strength inside one component", "Number of screens in the user interface", "Amount of data stored by the application"], ["الاعتماد بين مكونات برمجية منفصلة", "قوة الترابط الوظيفي داخل مكون واحد", "عدد شاشات واجهة المستخدم", "كمية البيانات المخزنة في التطبيق"], "Coupling measures the degree of interdependence between separate components.", "يقيس الاقتران درجة الاعتماد المتبادل بين المكونات المنفصلة."),
            q("ch5_best_coupling", "Understand", "Which coupling type uses only simple parameter values?", "أي نوع من الاقتران يقتصر على تمرير قيم بسيطة؟", ["Data coupling", "Control coupling", "Common coupling", "Content coupling"], ["اقتران البيانات", "اقتران التحكم", "الاقتران المشترك", "اقتران المحتوى"], "Data coupling communicates through needed data values and keeps dependencies limited.", "يتواصل اقتران البيانات عبر القيم المطلوبة ويحد من الاعتماديات."),
            q("ch5_worst_coupling", "Understand", "Which coupling form is the most restrictive and undesirable?", "أي شكل من الاقتران هو الأشد والأقل رغبة؟", ["Content coupling", "External coupling", "Data coupling", "Stamp coupling"], ["اقتران المحتوى", "الاقتران الخارجي", "اقتران البيانات", "اقتران البنية المركبة"], "Content coupling occurs when one component reaches into another's internal code or data.", "يحدث اقتران المحتوى عندما تتدخل وحدة في الشيفرة الداخلية لوحدة أخرى أو بياناتها."),
            q("ch5_common_coupling", "Apply", "Two components read and write the same global data area; this is...", "تقرأ وحدتان منطقة بيانات عامة مشتركة وتعدّلانها؛ هذا هو...", ["Common coupling", "Control coupling", "External coupling", "Stamp coupling"], ["الاقتران المشترك", "اقتران التحكم", "الاقتران الخارجي", "اقتران البنية المركبة"], "Shared global state creates common coupling.", "تنشئ الحالة العامة المشتركة اقتراناً مشتركاً."),
            q("ch5_control_coupling", "Apply", "One component passes a flag that selects another's internal branch; this is...", "مررت وحدة علماً يحدد فرعاً داخلياً في وحدة أخرى؛ هذا هو...", ["Control coupling", "Data coupling", "External coupling", "Content coupling"], ["اقتران التحكم", "اقتران البيانات", "الاقتران الخارجي", "اقتران المحتوى"], "A control flag directs another component's internal logic, creating control coupling.", "يوجه علم التحكم المنطق الداخلي لمكون آخر، فينشأ اقتران التحكم."),
            q("ch5_stamp_coupling", "Apply", "A component receives a record but uses only one of its fields; this is...", "استقبلت وحدة سجلاً مركباً ولم تستخدم إلا حقلاً واحداً؛ هذا هو...", ["Stamp coupling", "Data coupling", "Common coupling", "Content coupling"], ["اقتران البنية المركبة", "اقتران البيانات", "الاقتران المشترك", "اقتران المحتوى"], "Stamp coupling passes a composite structure when the receiver uses only part of it.", "يمرر اقتران البنية المركبة سجلاً كاملاً مع أن المستقبِل يستخدم جزءاً منه فقط."),
            q("ch5_external_coupling", "Understand", "Dependence on a shared external file format or protocol is...", "الاعتماد على صيغة ملف أو بروتوكول خارجي مشترك هو...", ["External coupling", "Common coupling", "Data coupling", "Content coupling"], ["الاقتران الخارجي", "الاقتران المشترك", "اقتران البيانات", "اقتران المحتوى"], "External coupling arises from dependence on an external format, protocol, or device.", "ينشأ الاقتران الخارجي من الاعتماد على صيغة أو بروتوكول أو جهاز خارجي."),
            q("ch5_zero_coupling", "Evaluate", "Why is zero coupling unrealistic for cooperating components?", "لماذا يستحيل عملياً انعدام الاقتران بين مكونات متعاونة؟", ["They must exchange data or transfer control", "They must all use identical internal code", "They must store state in shared global memory", "They must avoid every published interface"], ["لا بد أن تتبادل البيانات أو التحكم", "لا بد أن تستخدم الشيفرة الداخلية نفسها", "لا بد أن تخزن حالتها في ذاكرة عامة مشتركة", "لا بد أن تتجنب كل واجهة معلنة"], "Useful components need some communication; the goal is loose coupling rather than no interaction.", "تحتاج المكونات المفيدة إلى بعض التواصل؛ والهدف هو اقتران خفيف لا انعدام التفاعل."),
        ],
    },
    {
        "id": "Quiz_Ch05_T07_Module_Cohesion",
        "title": "Module Cohesion",
        "title_ar": "التماسك داخل الوحدة",
        "items": [
            q("ch5_cohesion_definition", "Understand", "What does cohesion describe?", "ماذا يصف التماسك؟", ["How strongly a component's elements serve one purpose", "How strongly separate components depend on each other", "How much memory an application uses at runtime", "How many users can access a service at once"], ["مدى خدمة عناصر المكون لغرض واحد", "مدى اعتماد المكونات المنفصلة بعضها على بعض", "مقدار الذاكرة التي يستخدمها التطبيق", "عدد المستخدمين القادرين على دخول خدمة"], "Cohesion concerns how well the elements within one component belong together.", "يتعلق التماسك بمدى ترابط العناصر داخل المكون الواحد."),
            q("ch5_best_cohesion", "Understand", "Which cohesion type makes every element serve one defined task?", "أي نوع من التماسك يجعل كل عنصر يخدم مهمة محددة؟", ["Functional cohesion", "Procedural cohesion", "Temporal cohesion", "Logical cohesion"], ["التماسك الوظيفي", "التماسك الإجرائي", "التماسك الزمني", "التماسك المنطقي"], "Functional cohesion means the elements cooperate for one well-defined task.", "يعني التماسك الوظيفي أن تتعاون العناصر لأداء مهمة واحدة محددة."),
            q("ch5_worst_cohesion", "Understand", "Which cohesion form is the weakest?", "أي شكل من التماسك هو الأضعف؟", ["Coincidental cohesion", "Logical cohesion", "Sequential cohesion", "Communicational cohesion"], ["التماسك العشوائي", "التماسك المنطقي", "التماسك التسلسلي", "التماسك الاتصالي"], "Coincidental cohesion groups elements with no meaningful relationship.", "يجمع التماسك العشوائي عناصر بلا علاقة ذات معنى."),
            q("ch5_temporal_cohesion", "Apply", "Initialization tasks grouped because they run at startup show...", "تجميع مهام التهيئة لأنها تعمل عند بدء التشغيل يوضح...", ["Temporal cohesion", "Sequential cohesion", "Functional cohesion", "Communicational cohesion"], ["التماسك الزمني", "التماسك التسلسلي", "التماسك الوظيفي", "التماسك الاتصالي"], "Temporal cohesion groups activities that execute during the same period.", "يجمع التماسك الزمني الأنشطة التي تنفذ في الفترة الزمنية نفسها."),
            q("ch5_functional_cohesion", "Understand", "What characterizes functional cohesion?", "ما الذي يميز التماسك الوظيفي؟", ["Every element contributes to one defined function", "Elements share a convenient place in one file", "Elements run together only during startup", "A selector chooses one unrelated operation"], ["تسهم كل العناصر في وظيفة واحدة محددة", "تشترك العناصر في مكان مناسب داخل ملف", "تعمل العناصر معاً عند بدء التشغيل فقط", "يختار محدد عملية غير مرتبطة"], "A functionally cohesive component has one focused and well-defined purpose.", "للمكون المتماسك وظيفياً غرض واحد واضح ومحدد."),
            q("ch5_procedural_cohesion", "Apply", "Elements linked by a required execution order but using different data show...", "ترتبط العناصر بترتيب تنفيذ مطلوب لكنها تستخدم بيانات مختلفة؛ هذا هو...", ["Procedural cohesion", "Sequential cohesion", "Logical cohesion", "Temporal cohesion"], ["التماسك الإجرائي", "التماسك التسلسلي", "التماسك المنطقي", "التماسك الزمني"], "Procedural cohesion links operations through their control-flow sequence.", "يربط التماسك الإجرائي العمليات عبر تسلسل تدفق التحكم."),
            q("ch5_communicational_cohesion", "Apply", "Different operations grouped because they use the same input data show...", "جُمعت عمليات مختلفة لأنها تستخدم بيانات الإدخال نفسها؛ هذا هو...", ["Communicational cohesion", "Sequential cohesion", "Procedural cohesion", "Coincidental cohesion"], ["التماسك الاتصالي", "التماسك التسلسلي", "التماسك الإجرائي", "التماسك العشوائي"], "Communicational cohesion groups distinct operations that work on the same data.", "يجمع التماسك الاتصالي عمليات مختلفة تعمل على البيانات نفسها."),
            q("ch5_logical_cohesion", "Apply", "A selector chooses one operation from a family of related tasks; this is...", "يختار محدد عملية واحدة من عائلة مهام متقاربة؛ هذا هو...", ["Logical cohesion", "Functional cohesion", "Sequential cohesion", "Coincidental cohesion"], ["التماسك المنطقي", "التماسك الوظيفي", "التماسك التسلسلي", "التماسك العشوائي"], "Logical cohesion groups similar categories of activity and uses a control choice among them.", "يجمع التماسك المنطقي فئات أنشطة متشابهة ويستخدم اختياراً للتحكم بينها."),
        ],
    },
    {
        "id": "Quiz_Ch05_T08_Cohesion_Coupling_Relationship",
        "title": "Cohesion and Coupling Relationship",
        "title_ar": "العلاقة بين التماسك والاقتران",
        "items": [
            q("ch5_cc_design_target", "Understand", "What combination is preferred in a modular design?", "ما التركيبة المفضلة في التصميم النمطي؟", ["High cohesion within parts and low coupling between them", "Low cohesion within parts and high coupling between them", "High cohesion and high coupling everywhere", "Low cohesion and low coupling within each part"], ["تماسك عالٍ داخل الأجزاء واقتران منخفض بينها", "تماسك منخفض داخل الأجزاء واقتران عالٍ بينها", "تماسك عالٍ واقتران عالٍ في كل موضع", "تماسك منخفض واقتران منخفض داخل كل جزء"], "A sound design focuses each component and limits dependencies across boundaries.", "يركز التصميم الجيد كل مكون ويحد الاعتماد عبر الحدود."),
            q("ch5_cc_scope_distinction", "Understand", "Where is cohesion measured, and where is coupling measured?", "أين يقاس التماسك وأين يقاس الاقتران؟", ["Inside one component; between separate components", "Between separate systems; inside one database", "Across user roles; inside a single operation", "Inside a network; between source files only"], ["داخل مكون واحد؛ وبين مكونات منفصلة", "بين أنظمة منفصلة؛ وداخل قاعدة بيانات", "عبر أدوار المستخدم؛ وداخل عملية واحدة", "داخل شبكة؛ وبين ملفات الشيفرة فقط"], "Cohesion is internal to one component; coupling concerns relationships across components.", "يقع التماسك داخل المكون الواحد، أما الاقتران فيتعلق بالعلاقات بين المكونات."),
            q("ch5_cc_not_causal", "Analyze", "Does high cohesion automatically guarantee low coupling?", "هل يضمن التماسك العالي تلقائياً اقتراناً منخفضاً؟", ["No, they are related but separate design goals", "Yes, cohesion directly removes every dependency", "Yes, both measure the same internal property", "No, coupling applies only to external systems"], ["لا، فهما هدفان تصميميان منفصلان ومتكاملان", "نعم، فالتماسك يزيل كل اعتماد مباشرة", "نعم، فكلاهما يقيس الخاصية الداخلية نفسها", "لا، فالاقتران يخص الأنظمة الخارجية فقط"], "A component can have a focused purpose yet still depend heavily on other components.", "قد يكون للمكون غرض مركز مع بقائه شديد الاعتماد على مكونات أخرى."),
            q("ch5_cc_high_coupling", "Analyze", "What is a common maintenance risk of high coupling?", "ما خطر الصيانة الشائع عند ارتفاع الاقتران؟", ["A change can ripple across dependent components", "A focused component can no longer have one purpose", "Every interface becomes hidden from its callers", "The system loses all ability to exchange data"], ["قد ينتقل أثر التغيير إلى المكونات المعتمدة", "يفقد المكون المركز غرضه الواحد", "تختفي كل واجهة عن الجهات التي تستدعيها", "يفقد النظام قدرته على تبادل البيانات كلياً"], "Strong dependencies make a local change more likely to affect connected parts.", "تجعل الاعتماديات القوية التغيير المحلي أكثر عرضة للتأثير في الأجزاء المرتبطة."),
            q("ch5_cc_low_cohesion", "Analyze", "What does low cohesion commonly indicate?", "على ماذا يدل انخفاض التماسك غالباً؟", ["Unrelated responsibilities share one component", "A component depends only on needed data values", "All system functions have been correctly isolated", "A user interface contains too few screens"], ["اشتراك مسؤوليات غير مترابطة في مكون واحد", "اعتماد المكون على قيم البيانات المطلوبة فقط", "عزل وظائف النظام كلها بصورة صحيحة", "احتواء واجهة المستخدم على شاشات قليلة"], "Low cohesion means the elements inside a component do not serve one focused purpose.", "يعني انخفاض التماسك أن عناصر المكون لا تخدم غرضاً مركزاً واحداً."),
            q("ch5_cc_modularity", "Understand", "How do cohesion and coupling support modularity together?", "كيف يدعم التماسك والاقتران النمطية معاً؟", ["Focused parts communicate through limited dependencies", "Shared internals replace all defined interfaces", "One central part owns every system responsibility", "Unrelated tasks are grouped to reduce file count"], ["تتواصل الأجزاء المركزة عبر اعتماديات محدودة", "تحل التفاصيل المشتركة محل الواجهات المحددة", "يتولى جزء مركزي كل مسؤوليات النظام", "تجمع المهام غير المرتبطة لتقليل الملفات"], "Modularity works best when components are internally focused and loosely connected.", "تعمل النمطية بأفضل صورة عندما تكون المكونات مركزة داخلياً ومترابطة بخفة."),
            q("ch5_cc_zero_coupling", "Evaluate", "Why should designers avoid treating zero coupling as the goal?", "لماذا لا ينبغي اعتبار انعدام الاقتران هو الهدف؟", ["Components still need purposeful communication", "Components should share every internal data structure", "Every component should implement the same algorithm", "Separate components never need to cooperate"], ["ما زالت المكونات تحتاج إلى تواصل هادف", "ينبغي للمكونات مشاركة كل بنياتها الداخلية", "ينبغي لكل مكون تنفيذ الخوارزمية نفسها", "لا تحتاج المكونات المنفصلة إلى التعاون"], "The design target is enough communication for cooperation with avoidable dependencies removed.", "الهدف تواصل يكفي للتعاون مع إزالة الاعتماديات التي يمكن تجنبها."),
            q("ch5_cc_information_hiding", "Apply", "A component hides a design decision behind a stable interface; what is the benefit?", "أخفى مكون قراراً تصميمياً خلف واجهة مستقرة؛ ما الفائدة؟", ["Callers need not rely on its internal representation", "Every caller must change whenever its data changes", "All components must share its private state", "The system no longer needs communication"], ["لا يحتاج المستدعون إلى تمثيله الداخلي", "يجب أن يتغير كل مستدعٍ عند تغير بياناته", "يجب أن تشارك المكونات حالته الخاصة", "لا يعود النظام بحاجة إلى التواصل"], "Information hiding reduces dependencies on internal design decisions.", "يقلل إخفاء المعلومات الاعتماد على القرارات التصميمية الداخلية."),
            q("ch5_cc_independence_benefits", "Understand", "What benefit can high cohesion with low coupling provide?", "ما الفائدة التي يتيحها التماسك العالي مع الاقتران المنخفض؟", ["Focused modules are easier to understand, test, and maintain", "Every module becomes independent of shared system behavior", "Cohesion automatically removes all dependencies between modules", "All communication disappears between cooperating components"], ["يسهل فهم الوحدات المركزة واختبارها وصيانتها", "تنفصل كل وحدة تماماً عن سلوك النظام المشترك", "يزيل التماسك تلقائياً كل اعتماد بين الوحدات البرمجية", "يختفي كل تواصل بين المكونات التي تتعاون معاً"], "High cohesion and low coupling support functional independence, which makes components easier to understand, test, and maintain.", "يدعم التماسك العالي والاقتران المنخفض استقلالية المكونات، ويسهل فهمها واختبارها وصيانتها."),
            q("ch5_cc_logical_control_pair", "Analyze", "Which relationship commonly links logical cohesion with coupling?", "أي علاقة تربط عادة التماسك المنطقي بالاقتران؟", ["Logical cohesion may use a caller flag, creating control coupling", "Temporal cohesion groups same-time tasks and requires stamp coupling", "Functional cohesion serves one purpose through shared global coupling", "Communicational cohesion shares data through external coupling"], ["قد يصاحب التماسك المنطقي اقتران تحكم بسبب علم المستدعي", "يجمع التماسك الزمني مهاماً متزامنة مع اقتران البنية", "يخدم التماسك الوظيفي غرضاً واحداً مع اقتران مشترك", "يستخدم التماسك الاتصالي بيانات مشتركة مع اقتران خارجي"], "A caller flag selects one activity within a logically cohesive group and can create control coupling.", "يختار علم المستدعي نشاطاً ضمن مجموعة متماسكة منطقياً وقد ينشأ عنه اقتران تحكم."),
        ],
    },
    {
        "id": "Quiz_Ch05_T09_Strategy_Of_Design",
        "title": "Strategy of Design",
        "title_ar": "استراتيجية التصميم",
        "items": [
            q("ch5_strategy_definition", "Understand", "What does a design strategy guide?", "ما الذي توجهه استراتيجية التصميم؟", ["How a system is decomposed and assembled", "How project invoices are checked and approved", "How users are recruited for acceptance testing", "How the service is advertised after release"], ["كيفية تفكيك النظام وتجميعه", "كيفية تدقيق فواتير المشروع واعتمادها", "كيفية اختيار المستخدمين لاختبار القبول", "كيفية تسويق الخدمة بعد إصدارها"], "A design strategy sets the broad direction used to shape the system architecture.", "تحدد استراتيجية التصميم الاتجاه العام المستخدم لتشكيل معمارية النظام."),
            q("ch5_strategy_families", "Understand", "Which set names the three recognized design strategies?", "أي مجموعة تسمي استراتيجيات التصميم الثلاث المعروفة؟", ["Top-down, bottom-up, and hybrid design", "Waterfall, spiral, and incremental delivery", "Testing, debugging, and formal verification", "Functional, temporal, and logical cohesion"], ["التصميم التنازلي والتصاعدي والهجين", "الشلال والحلزوني والتسليم التزايدي", "الاختبار والتنقيح والتحقق الصوري", "التماسك الوظيفي والزمني والمنطقي"], "The three design strategies are top-down, bottom-up, and their hybrid combination.", "استراتيجيات التصميم الثلاث هي التنازلي والتصاعدي ومزيجهما الهجين."),
            q("ch5_strategy_topdown_focus", "Understand", "Which concern stays visible in a top-down strategy?", "أي جانب يبقى واضحاً في الاستراتيجية التنازلية؟", ["The system's high-level goals and structure", "The lowest-level library details alone", "The internal state of every object first", "The interface colors selected by users"], ["أهداف النظام العليا وبنيته", "تفاصيل المكتبات الأدنى وحدها", "الحالة الداخلية لكل كائن أولاً", "ألوان الواجهات التي يختارها المستخدمون"], "Top-down design starts from the overall purpose and refines its structure.", "يبدأ التصميم التنازلي من الغرض العام وينقح بنيته."),
            q("ch5_strategy_bottomup_start", "Understand", "Which starting point identifies a bottom-up strategy?", "أي نقطة بداية تميز الاستراتيجية التصاعدية؟", ["Basic components assembled into larger parts", "System goals divided into lower-level tasks", "User roles expanded into interface scenarios", "High-level diagrams translated into test reports"], ["تجميع المكونات الأساسية في أجزاء أكبر", "تقسيم أهداف النظام إلى مهام أدنى", "توسيع أدوار المستخدم إلى سيناريوهات واجهة", "تحويل المخططات العليا إلى تقارير اختبار"], "Bottom-up design begins with lower-level building blocks and combines them upward.", "يبدأ التصميم التصاعدي بلبنات البناء الدنيا ثم يجمعها صعوداً."),
            q("ch5_strategy_hybrid", "Understand", "What makes a design strategy hybrid?", "ما الذي يجعل استراتيجية التصميم هجينة؟", ["It combines high-level decomposition with suitable existing parts", "It replaces system goals with disconnected utility routines", "It uses only classes and rejects procedural components", "It delays all structural choices until release"], ["تجمع التفكيك من الأعلى مع أجزاء موجودة مناسبة", "تستبدل أهداف النظام بإجراءات خدمية منفصلة", "تستخدم الأصناف وحدها وترفض المكونات الإجرائية", "تؤجل كل القرارات البنيوية إلى ما بعد الإصدار"], "Hybrid design uses top-down and bottom-up reasoning where each fits.", "يستخدم التصميم الهجين التفكير التنازلي والتصاعدي حيث يناسب كل منهما."),
            q("ch5_strategy_not_design", "Understand", "Which item is not one of the three design strategies?", "أي عنصر ليس من استراتيجيات التصميم الثلاث؟", ["Embedded design", "Top-down design", "Bottom-up design", "Hybrid design"], ["التصميم المضمّن", "التصميم التنازلي", "التصميم التصاعدي", "التصميم الهجين"], "Embedded design is not one of the stated top-down, bottom-up, and hybrid strategies.", "التصميم المضمّن ليس من بين التصميم التنازلي والتصاعدي والهجين."),
            q("ch5_strategy_select", "Apply", "A project has clear system goals and reusable utilities; which approach fits?", "للمشروع أهداف واضحة وأدوات قابلة لإعادة الاستخدام؛ أي نهج يلائمه؟", ["Hybrid design can use both kinds of structure", "Bottom-up design must ignore the system goals", "Top-down design must discard existing utilities", "No strategy applies when components already exist"], ["يمكن للتصميم الهجين استخدام الاتجاهين", "يجب أن يتجاهل التصميم التصاعدي أهداف النظام", "يجب أن يهمل التصميم التنازلي الأدوات الموجودة", "لا تلائم أي استراتيجية وجود مكونات مسبقة"], "A hybrid approach can retain system-level direction while using suitable existing components.", "يستطيع النهج الهجين الحفاظ على اتجاه النظام العام مع استخدام مكونات مناسبة موجودة."),
            q("ch5_strategy_no_universal_winner", "Evaluate", "What is a sound way to choose a design strategy?", "ما الطريقة السليمة لاختيار استراتيجية التصميم؟", ["Match the approach to goals and available components", "Assume one strategy dominates every project", "Choose only by the number of diagrams produced", "Select the strategy with the newest terminology"], ["ملاءمة النهج لأهداف النظام والمكونات المتاحة", "افتراض تفوق استراتيجية في كل مشروع", "الاختيار بحسب عدد المخططات المنتجة فقط", "اختيار الاستراتيجية ذات المصطلحات الأحدث"], "The strategy should suit the system goals and the components that can be reused.", "ينبغي أن تلائم الاستراتيجية أهداف النظام والمكونات الممكن إعادة استخدامها."),
        ],
    },
    {
        "id": "Quiz_Ch05_T10_Bottom_Up_Design",
        "title": "Bottom-Up Design",
        "title_ar": "التصميم التصاعدي",
        "items": [
            q("ch5_bottomup_definition", "Understand", "Where does bottom-up design begin?", "من أين يبدأ التصميم التصاعدي؟", ["With basic components and utility routines", "With the highest system coordinator", "With user-interface screen arrangements", "With a final deployment configuration"], ["بالمكونات الأساسية والإجراءات الخدمية", "بمنسق النظام الأعلى", "بترتيب شاشات واجهة المستخدم", "بتهيئة النشر النهائية"], "Bottom-up design starts with low-level building blocks.", "يبدأ التصميم التصاعدي بلبنات البناء ذات المستوى الأدنى."),
            q("ch5_bottomup_direction", "Understand", "In which direction are larger structures formed?", "بأي اتجاه تتكون البنى الأكبر؟", ["Lower-level parts are combined upward", "System goals are divided downward", "User views are projected outward", "Control paths are flattened sideways"], ["تُجمع الأجزاء الدنيا باتجاه الأعلى", "تُفكك أهداف النظام إلى الأسفل", "تُعرض مناظير المستخدم إلى الخارج", "تُسطح مسارات التحكم جانبياً"], "Higher-level subsystems emerge by combining lower-level components.", "تنشأ الأنظمة الفرعية الأعلى من جمع المكونات ذات المستوى الأدنى."),
            q("ch5_bottomup_reuse", "Apply", "A team starts with tested reusable utilities; which strategy does this reflect?", "بدأ فريق بأدوات مجربة قابلة لإعادة الاستخدام؛ أي استراتيجية يعكس ذلك؟", ["Bottom-up design", "Top-down design", "Conceptual design", "Logical cohesion"], ["التصميم التصاعدي", "التصميم التنازلي", "التصميم المفهومي", "التماسك المنطقي"], "Beginning with existing low-level utilities is characteristic of bottom-up design.", "البداية بأدوات منخفضة المستوى موجودة سمة للتصميم التصاعدي."),
            q("ch5_bottomup_strength", "Understand", "What is a recognized strength of bottom-up design?", "ما إحدى نقاط قوة التصميم التصاعدي المعروفة؟", ["It can reuse existing low-level components", "It keeps every system goal visible from the start", "It avoids the need to integrate components", "It guarantees that all interfaces stay unchanged"], ["إمكان إعادة استخدام المكونات الدنيا الموجودة", "إبقاء أهداف النظام كلها واضحة منذ البداية", "الاستغناء عن دمج المكونات", "ضمان بقاء كل الواجهات بلا تغيير"], "Bottom-up design can capitalize on available libraries and foundational parts.", "يستفيد التصميم التصاعدي من المكتبات والأجزاء الأساسية المتاحة."),
            q("ch5_bottomup_limit", "Analyze", "What is a possible weakness of a purely bottom-up approach?", "ما أحد أوجه الضعف المحتملة للنهج التصاعدي الخالص؟", ["Early components may not fit later system goals", "Low-level components cannot be tested separately", "Existing utilities always create content coupling", "The approach cannot produce higher-level services"], ["قد لا تلائم المكونات المبكرة أهداف النظام اللاحقة", "يتعذر اختبار المكونات الدنيا بصورة مستقلة", "تنشئ الأدوات الموجودة اقتران محتوى دائماً", "لا يستطيع النهج إنتاج خدمات أعلى مستوى"], "Without early system-level guidance, useful pieces may not align with overall requirements.", "من دون توجيه مبكر من مستوى النظام قد لا تلائم الأجزاء المفيدة المتطلبات العامة."),
            q("ch5_bottomup_test_driver", "Understand", "What may be needed to exercise a low-level component early?", "ما الذي قد يلزم لتشغيل مكون منخفض المستوى مبكراً؟", ["A test driver that calls the component", "A test stub that replaces its callers", "A deployment view of the finished system", "A screen mockup for each internal routine"], ["برنامج اختبار يستدعي المكون", "بديل اختباري يحل محل مستدعيه", "منظور نشر للنظام المكتمل", "نموذج شاشة لكل إجراء داخلي"], "A driver can invoke a lower-level part before higher-level callers exist.", "يستطيع برنامج الاختبار استدعاء الجزء الأدنى قبل وجود مستدعياته العليا."),
            q("ch5_bottomup_integration", "Analyze", "Why can integration be a concern in bottom-up design?", "لماذا قد يكون الدمج موضع اهتمام في التصميم التصاعدي؟", ["Separate parts must later fit the overall architecture", "The design begins after all components are deployed", "Bottom-up work forbids interfaces between parts", "Every utility must be rewritten before testing"], ["يجب أن تلائم الأجزاء المنفصلة المعمارية العامة لاحقاً", "يبدأ التصميم بعد نشر المكونات كلها", "يمنع العمل التصاعدي الواجهات بين الأجزاء", "يجب إعادة كتابة كل أداة قبل اختبارها"], "The team must ensure that reusable pieces combine into the required system.", "على الفريق التأكد من أن الأجزاء القابلة لإعادة الاستخدام تتجمع لتكوين النظام المطلوب."),
            q("ch5_bottomup_vs_topdown", "Analyze", "Which contrast with top-down design is accurate?", "أي مقارنة مع التصميم التنازلي صحيحة؟", ["Bottom-up starts with parts; top-down starts with system goals", "Bottom-up starts with goals; top-down starts with utility parts", "Both strategies begin only after coding is complete", "Both strategies prohibit reuse of existing components"], ["يبدأ التصاعدي بالأجزاء والتنازلي بأهداف النظام", "يبدأ التصاعدي بالأهداف والتنازلي بالأدوات", "تبدأ الاستراتيجيتان بعد اكتمال البرمجة فقط", "تحظر الاستراتيجيتان إعادة استخدام المكونات"], "The two strategies differ mainly in their direction of decomposition and assembly.", "تختلف الاستراتيجيتان أساساً في اتجاه التفكيك والتجميع."),
        ],
    },
    {
        "id": "Quiz_Ch05_T11_Top_Down_Design",
        "title": "Top-Down Design",
        "title_ar": "التصميم التنازلي",
        "items": [
            q("ch5_topdown_definition", "Understand", "Where does top-down design begin?", "من أين يبدأ التصميم التنازلي؟", ["With the overall system purpose and structure", "With the smallest reusable utility routine", "With the final deployment hardware diagram", "With a detailed data-store implementation"], ["بالغرض العام للنظام وبنيته", "بأصغر إجراء خدمي قابل لإعادة الاستخدام", "بمخطط أجهزة النشر النهائي", "بتنفيذ تفصيلي لمخزن البيانات"], "Top-down design starts at the highest system level.", "يبدأ التصميم التنازلي من أعلى مستوى في النظام."),
            q("ch5_topdown_direction", "Understand", "How does a top-down strategy develop lower-level parts?", "كيف تطور الاستراتيجية التنازلية الأجزاء الأدنى؟", ["By refining larger functions into smaller tasks", "By combining utility routines into a system root", "By replacing requirements with class diagrams", "By sorting implementation files by size"], ["بتنقيح الوظائف الكبيرة إلى مهام أصغر", "بجمع الإجراءات الخدمية نحو جذر النظام", "باستبدال المتطلبات بمخططات الأصناف", "بترتيب ملفات التنفيذ بحسب الحجم"], "Stepwise decomposition turns higher-level behavior into progressively detailed parts.", "يحول التفكيك التدريجي السلوك الأعلى إلى أجزاء أكثر تفصيلاً."),
            q("ch5_topdown_goal_focus", "Understand", "What advantage comes from starting with system goals?", "ما فائدة البدء بأهداف النظام؟", ["The overall purpose remains visible during decomposition", "Every low-level library is available immediately", "Test stubs become unnecessary for early checks", "The design no longer depends on requirements"], ["يبقى الغرض العام واضحاً أثناء التفكيك", "تتوفر كل مكتبة منخفضة المستوى فوراً", "تصبح بدائل الاختبار غير لازمة للفحص المبكر", "لا يعود التصميم معتمداً على المتطلبات"], "Starting from the system goal keeps the global purpose in view.", "يحافظ البدء بهدف النظام على وضوح الغرض العام."),
            q("ch5_topdown_stubs", "Understand", "What can replace an unfinished lower-level part during early testing?", "ما الذي قد يحل محل جزء أدنى غير مكتمل أثناء الاختبار المبكر؟", ["A test stub that simulates the missing part", "A test driver that calls an existing utility", "A shared global variable for all callers", "A database view that lists the missing code"], ["بديل اختباري يحاكي الجزء غير المكتمل", "برنامج اختبار يستدعي أداة موجودة", "متغير عام مشترك بين كل المستدعين", "منظور قاعدة بيانات يسرد الشيفرة الناقصة"], "A stub supplies temporary behavior when a subordinate component is not yet implemented.", "يوفر البديل الاختباري سلوكاً مؤقتاً عندما لا يكون المكون التابع قد نُفذ بعد."),
            q("ch5_topdown_testing", "Apply", "Higher-level behavior is ready before its subordinate routines; what supports testing?", "اكتمل السلوك الأعلى قبل إجراءاته التابعة؛ ما الذي يدعم الاختبار؟", ["Stubs for the unfinished subordinate routines", "Drivers for every missing higher-level caller", "Shared data that bypasses the interfaces", "Final deployment nodes for the whole system"], ["بدائل اختبارية للإجراءات التابعة غير المكتملة", "برامج اختبار لكل مستدعٍ أعلى مفقود", "بيانات مشتركة تتجاوز الواجهات", "عقد النشر النهائية للنظام كله"], "Stubs let a higher-level component be exercised before its dependencies are ready.", "تتيح البدائل اختبار المكون الأعلى قبل جاهزية اعتمادياته."),
            q("ch5_topdown_limit", "Analyze", "What may a top-down approach postpone?", "ما الذي قد يؤجله النهج التنازلي؟", ["Integration of low-level libraries and hardware", "Definition of system-wide goals and interfaces", "Division of behavior into smaller functions", "Communication of the architecture to implementers"], ["دمج المكتبات والأجهزة منخفضة المستوى", "تحديد أهداف النظام وواجهاته العامة", "تقسيم السلوك إلى وظائف أصغر", "توضيح المعمارية للمنفذين"], "Lower-level assets may be integrated later because the strategy starts above them.", "قد يتأخر دمج الأصول الدنيا لأن الاستراتيجية تبدأ من مستوى أعلى."),
            q("ch5_topdown_stepwise", "Understand", "Which technique is closely associated with top-down decomposition?", "أي تقنية ترتبط بالتفكيك التنازلي؟", ["Stepwise refinement", "Shared global coupling", "Coincidental cohesion", "Transaction dispatching"], ["التنقيح التدريجي", "الاقتران العام المشترك", "التماسك العشوائي", "توجيه المعاملات"], "Stepwise refinement repeatedly expands abstract functions into more detailed steps.", "يوسع التنقيح التدريجي الوظائف المجردة إلى خطوات أكثر تفصيلاً بصورة متكررة."),
            q("ch5_topdown_vs_bottomup", "Analyze", "Which statement contrasts top-down with bottom-up design?", "أي عبارة تقارن التصميم التنازلي بالتصميم التصاعدي؟", ["Top-down decomposes goals; bottom-up assembles basic parts", "Top-down assembles utilities; bottom-up decomposes system goals", "Top-down avoids architecture; bottom-up avoids components", "Both start by writing the final source code"], ["يفكك التنازلي الأهداف ويجمع التصاعدي الأجزاء الأساسية", "يجمع التنازلي الأدوات ويفكك التصاعدي أهداف النظام", "يتجنب التنازلي المعمارية ويتجنب التصاعدي المكونات", "يبدأ كلاهما بكتابة الشيفرة النهائية"], "Top-down proceeds from the whole toward detail; bottom-up proceeds from parts toward the whole.", "ينتقل التنازلي من الكل إلى التفاصيل، والتصاعدي من الأجزاء إلى الكل."),
        ],
    },
    {
        "id": "Quiz_Ch05_T12_Hybrid_Design",
        "title": "Hybrid Design",
        "title_ar": "التصميم الهجين",
        "items": [
            q("ch5_hybrid_definition", "Understand", "What is the defining idea of hybrid design?", "ما الفكرة التي تعرّف التصميم الهجين؟", ["Combining top-down and bottom-up design", "Using only the smallest available routines", "Dividing the system only by user screens", "Avoiding architectural decomposition entirely"], ["الجمع بين التصميم التنازلي والتصاعدي", "استخدام الإجراءات الأصغر المتاحة فقط", "تقسيم النظام بحسب شاشات المستخدم فقط", "تجنب التفكيك المعماري كلياً"], "Hybrid design combines the two broad directions when both are useful.", "يجمع التصميم الهجين الاتجاهين العامين عندما يكون كل منهما مفيداً."),
            q("ch5_hybrid_topdown_role", "Understand", "What can the top-down part of a hybrid approach establish?", "ماذا يستطيع الجانب التنازلي في النهج الهجين أن يحدد؟", ["The system-level structure and major responsibilities", "The internal code of every reused library", "The final market price of each component", "The complete behavior of external hardware"], ["بنية النظام ومسؤولياته الرئيسة", "الشيفرة الداخلية لكل مكتبة يعاد استخدامها", "السعر السوقي النهائي لكل مكون", "السلوك الكامل للأجهزة الخارجية"], "Top-down decomposition can establish the goal-driven architecture.", "يستطيع التفكيك التنازلي تحديد المعمارية الموجهة بالأهداف."),
            q("ch5_hybrid_bottomup_role", "Understand", "What can the bottom-up part contribute to a hybrid design?", "ماذا يستطيع الجانب التصاعدي إضافته إلى التصميم الهجين؟", ["Suitable existing lower-level components", "A replacement for all system requirements", "A guarantee of zero component interaction", "An excuse to omit interface decisions"], ["مكونات دنيا موجودة وملائمة", "بديلاً عن متطلبات النظام كلها", "ضماناً بانعدام تفاعل المكونات", "مبرراً لإغفال قرارات الواجهات"], "Bottom-up work contributes reusable building blocks where they fit the architecture.", "يسهم العمل التصاعدي بلبنات قابلة لإعادة الاستخدام حيث تلائم المعمارية."),
            q("ch5_hybrid_when", "Apply", "A team has firm goals and useful existing libraries; what approach can fit?", "لدى فريق أهداف ثابتة ومكتبات نافعة موجودة؛ أي نهج قد يلائم؟", ["A hybrid strategy can combine both inputs", "A pure bottom-up strategy must ignore the goals", "A pure top-down strategy must discard the libraries", "A design strategy cannot use existing components"], ["تستطيع الاستراتيجية الهجينة الجمع بين المعطيات", "يجب أن تتجاهل الاستراتيجية التصاعدية الأهداف", "يجب أن تهمل الاستراتيجية التنازلية المكتبات", "لا تستطيع استراتيجية التصميم استخدام مكونات موجودة"], "The hybrid approach can preserve system direction and reuse suitable lower-level parts.", "يستطيع النهج الهجين الحفاظ على اتجاه النظام وإعادة استخدام الأجزاء الدنيا المناسبة."),
            q("ch5_hybrid_balance", "Analyze", "What should guide the balance between the two directions?", "ما الذي ينبغي أن يوجه الموازنة بين الاتجاهين؟", ["Requirements, architecture, and available components", "The number of developers using one language", "A preference for the newest design diagram", "The size of the final printed document"], ["المتطلبات والمعمارية والمكونات المتاحة", "عدد المطورين الذين يستخدمون لغة واحدة", "تفضيل أحدث مخطط تصميم", "حجم الوثيقة المطبوعة النهائية"], "The combination should reflect the system's needs and the fit of available components.", "ينبغي أن يعكس الجمع حاجات النظام ومدى ملاءمة المكونات المتاحة."),
            q("ch5_hybrid_no_guarantee", "Evaluate", "Which claim about hybrid design is justified?", "أي ادعاء عن التصميم الهجين له ما يسنده؟", ["It combines two strategies without guaranteeing success", "It eliminates every integration and testing risk", "It always outperforms both strategies in every system", "It makes the system independent of its requirements"], ["يجمع استراتيجيتين من دون ضمان النجاح", "يلغي كل مخاطر الدمج والاختبار", "يتفوق دائماً على الاستراتيجيتين في كل نظام", "يجعل النظام مستقلاً عن متطلباته"], "Combining approaches is a design choice, not a guarantee of quality or schedule.", "الجمع بين النهجين خيار تصميمي وليس ضماناً للجودة أو الجدول."),
            q("ch5_hybrid_not_third_process", "Understand", "How is hybrid design related to the other two strategies?", "ما علاقة التصميم الهجين بالاستراتيجيتين الأخريين؟", ["It draws on both directions within one design effort", "It replaces both directions with a test process", "It applies only after a system is deployed", "It forbids reuse of previously built components"], ["يستفيد من الاتجاهين ضمن جهد تصميم واحد", "يستبدل الاتجاهين بعملية اختبار", "يطبق بعد نشر النظام فقط", "يحظر إعادة استخدام مكونات مبنية سابقاً"], "Hybrid describes a combination of top-down and bottom-up design reasoning.", "يصف الهجين الجمع بين التفكير التصميمي التنازلي والتصاعدي."),
            q("ch5_hybrid_architecture", "Apply", "A top-level service tree includes selected reusable utilities; this is...", "تضم شجرة خدمات عليا أدوات مختارة قابلة لإعادة الاستخدام؛ هذا هو...", ["A hybrid design arrangement", "A purely conceptual design view", "A coupling taxonomy", "A temporal cohesion pattern"], ["ترتيب تصميم هجين", "منظور تصميم مفهومي خالص", "تصنيف للاقتران", "نمط تماسك زمني"], "The example combines high-level decomposition with lower-level reusable parts.", "يجمع المثال بين التفكيك من المستوى الأعلى والأجزاء الدنيا القابلة لإعادة الاستخدام."),
        ],
    },
    {
        "id": "Quiz_Ch05_T13_Function_Oriented_Design",
        "title": "Function-Oriented Design",
        "title_ar": "التصميم الموجه بالوظائف",
        "items": [
            q("ch5_fod_definition", "Understand", "What is the main organizing focus of function-oriented design?", "ما محور التنظيم الرئيس في التصميم الموجه بالوظائف؟", ["Functions and their procedural decomposition", "Objects and their identity relationships", "Hardware nodes and deployment locations", "User stories and project release dates"], ["الوظائف وتفكيكها الإجرائي", "الكائنات وعلاقات هويتها", "العقد المادية ومواقع نشرها", "قصص المستخدم ومواعيد الإصدارات"], "Function-oriented design organizes the system around functions and subfunctions.", "ينظم التصميم الموجه بالوظائف النظام حول الوظائف والوظائف الفرعية."),
            q("ch5_fod_view", "Understand", "How does function-oriented design view computation?", "كيف ينظر التصميم الموجه بالوظائف إلى المعالجة؟", ["As functions transforming inputs into outputs", "As objects exchanging identity tokens only", "As database tables without processing behavior", "As hardware nodes exchanging deployment files"], ["وظائف تحول المدخلات إلى مخرجات", "كائنات تتبادل رموز الهوية فقط", "جداول بيانات بلا سلوك معالجة", "عقد أجهزة تتبادل ملفات النشر"], "The functional view models computation as transformations of data.", "يمثل المنظور الوظيفي المعالجة بوصفها تحويلات للبيانات."),
            q("ch5_fod_data_separation", "Understand", "What is generally separated in function-oriented decomposition?", "ما الذي يفصل عادة في التفكيك الموجه بالوظائف؟", ["Data structures and the procedures that use them", "Class identity and each object instance", "Requirements and all system boundaries", "Component nodes and physical machines"], ["بنى البيانات والإجراءات التي تستخدمها", "هوية الصنف وكل نسخة من كائناته", "المتطلبات وحدود النظام كلها", "عقد المكونات والحواسيب المادية"], "Function-oriented design commonly treats data and the procedures operating on it separately.", "يتعامل التصميم الموجه بالوظائف عادة مع البيانات وإجراءات معالجتها على نحو منفصل."),
            q("ch5_fod_dfd", "Understand", "Which notation primarily models data movement and transformation?", "أي ترميز يمثل حركة البيانات وتحولها أساساً؟", ["Data Flow Diagram", "Structure Chart", "Use-Case Diagram", "Deployment Diagram"], ["مخطط تدفق البيانات", "مخطط البنية", "مخطط حالات الاستخدام", "مخطط النشر"], "A DFD represents data flows, stores, sources, and transformations.", "يمثل DFD تدفقات البيانات ومخازنها ومصادرها وتحولاتها."),
            q("ch5_fod_hierarchy", "Understand", "What does a function-oriented hierarchy decompose?", "ماذا يفكك التسلسل الهرمي الموجه بالوظائف؟", ["System functions into subordinate procedures", "Object states into physical deployment nodes", "Database records into external user roles", "Hardware devices into business objectives"], ["وظائف النظام إلى إجراءات تابعة", "حالات الكائنات إلى عقد نشر مادية", "سجلات قاعدة البيانات إلى أدوار المستخدم", "الأجهزة إلى أهداف العمل"], "Functional decomposition breaks system behavior into a hierarchy of procedures.", "يقسم التفكيك الوظيفي سلوك النظام إلى تسلسل هرمي من الإجراءات."),
            q("ch5_procedural_abstraction", "Understand", "Which abstraction names an operation while hiding its implementation?", "أي تجريد يسمي عملية ويخفي طريقة تنفيذها؟", ["Procedural abstraction", "Data abstraction", "Control abstraction", "Deployment abstraction"], ["التجريد الإجرائي", "تجريد البيانات", "تجريد التحكم", "تجريد النشر"], "Procedural abstraction lets callers use a named operation without knowing its internal steps.", "يتيح التجريد الإجرائي للمستدعين استخدام عملية مسماة دون معرفة خطواتها الداخلية."),
            q("ch5_fod_transform", "Understand", "What can connect a DFD analysis to a functional structure chart?", "ما الذي قد يربط تحليل DFD بمخطط بنية وظيفي؟", ["Transform or transaction analysis", "Class inheritance or object cloning", "Physical deployment or node allocation", "Cohesion ranking or global coupling"], ["تحليل التحويل أو تحليل المعاملات", "وراثة الأصناف أو استنساخ الكائنات", "النشر المادي أو توزيع العقد", "ترتيب التماسك أو الاقتران العام"], "Transform and transaction analysis map data-flow structure into procedural structure.", "يربط تحليل التحويل والمعاملات بنية تدفق البيانات بالبنية الإجرائية."),
            q("ch5_fan_in_out", "Understand", "What do fan-in and fan-out measure for a module?", "ماذا يقيس Fan-in وFan-out في الوحدة؟", ["Fan-in counts callers; fan-out counts modules called", "Fan-in counts outgoing calls; fan-out counts callers", "Both count stored fields and interface parameter values", "Both measure source size and runtime speed per module"], ["يقيس Fan-in الوحدات المستدعية وFan-out الوحدات التي تستدعيها", "يقيس Fan-in الاستدعاءات الصادرة وFan-out مستدعياتها", "يقيس كلاهما حقول البيانات وقيم المعاملات بين الوحدات", "يقيس كلاهما حجم الشيفرة وزمن التنفيذ لكل وحدة"], "Fan-in counts modules that call a component; fan-out counts the components it calls.", "يرصد Fan-in الوحدات التي تستدعي المكون، ويرصد Fan-out المكونات التي يستدعيها."),
        ],
    },
    {
        "id": "Quiz_Ch05_T14_Design_Notations",
        "title": "Software Design Notations",
        "title_ar": "ترميزات التصميم البرمجي",
        "items": [
            q("ch5_dfd_view", "Understand", "Which design view does a DFD primarily show?", "أي منظور تصميم يوضحه DFD أساساً؟", ["Data movement, stores, and transformations", "Module calls and control hierarchy", "Object states and time-dependent behavior", "Physical nodes and hardware allocation"], ["حركة البيانات ومخازنها وتحولاتها", "استدعاء الوحدات والتسلسل الهرمي للتحكم", "حالات الكائن والسلوك المتغير مع الزمن", "العقد المادية وتوزيع الأجهزة"], "A DFD focuses on how data moves and changes through a system.", "يركز DFD على حركة البيانات وتحولها عبر النظام."),
            q("ch5_structure_chart_view", "Understand", "Which design view does a structure chart primarily show?", "أي منظور تصميم يوضحه مخطط البنية أساساً؟", ["Procedural control and invocation hierarchy", "Data stores and external data movement", "Physical machines and deployment locations", "User goals and system boundary actors"], ["التحكم الإجرائي وتسلسل الاستدعاءات", "مخازن البيانات وحركتها الخارجية", "الأجهزة المادية ومواقع النشر", "أهداف المستخدم والجهات عند حدود النظام"], "A structure chart represents procedural hierarchy and component invocation.", "يمثل مخطط البنية التسلسل الإجرائي واستدعاء المكونات."),
            q("ch5_flowchart_view", "Understand", "What does a flowchart most directly communicate?", "ماذا يوصل مخطط التدفق مباشرة؟", ["The sequence and branching of procedural steps", "The hierarchy of calling software components", "The data stores in an external environment", "The classes deployed on physical devices"], ["تسلسل الخطوات الإجرائية وتفرعها", "تسلسل استدعاء مكونات البرمجيات", "مخازن البيانات في البيئة الخارجية", "الأصناف المنشورة على الأجهزة المادية"], "A flowchart shows algorithmic steps and their control flow.", "يوضح مخطط التدفق خطوات الخوارزمية وتدفق التحكم فيها."),
            q("ch5_flowchart_vs_structure", "Analyze", "What is the key distinction between a flowchart and a structure chart?", "ما الفرق الجوهري بين مخطط التدفق ومخطط البنية؟", ["Steps and branches versus calls among components", "Data movement versus physical deployment nodes", "User roles versus class inheritance structure", "Stored records versus external system messages"], ["الخطوات والفروع مقابل استدعاء المكونات", "حركة البيانات مقابل عقد النشر المادية", "أدوار المستخدم مقابل وراثة الأصناف", "السجلات المخزنة مقابل رسائل النظام الخارجي"], "Flowcharts model procedural flow; structure charts model calling relationships.", "يمثل مخطط التدفق سير الإجراءات، ويمثل مخطط البنية علاقات الاستدعاء."),
            q("ch5_multiple_notations", "Understand", "Why do designers use more than one notation?", "لماذا يستخدم المصممون أكثر من ترميز واحد؟", ["Different views expose different design concerns", "One diagram can never be revised after review", "Every stakeholder must read identical detail", "Notation choice replaces architecture decisions"], ["تكشف المناظير المختلفة جوانب تصميم مختلفة", "لا يمكن تعديل المخطط بعد مراجعته", "ينبغي لكل أصحاب المصلحة قراءة التفاصيل نفسها", "يحل اختيار الترميز محل قرارات المعمارية"], "Specialized notations avoid clutter by presenting distinct architectural dimensions.", "تتجنب الترميزات المتخصصة التشويش بعرض أبعاد معمارية مختلفة."),
            q("ch5_static_dynamic_notations", "Understand", "Which pair contrasts static structure with dynamic behavior?", "أي زوج يقارن البنية الساكنة بالسلوك الديناميكي؟", ["Class diagram and sequence diagram", "DFD and deployment diagram", "Flowchart and class diagram", "Structure chart and data dictionary"], ["مخطط الأصناف ومخطط التسلسل", "مخطط تدفق البيانات ومخطط النشر", "مخطط التدفق ومخطط الأصناف", "مخطط البنية وقاموس البيانات"], "Class diagrams show structure; sequence diagrams show interactions over time.", "يعرض مخطط الأصناف البنية، ويعرض مخطط التسلسل التفاعلات عبر الزمن."),
            q("ch5_notation_stakeholders", "Apply", "A business user needs to validate system goals; which notation is suitable?", "يريد مستخدم تجاري التحقق من أهداف النظام؛ أي ترميز يناسبه؟", ["A use-case view of user goals", "A deployment view of processor locations", "A procedure body with local variables", "A detailed algorithmic flowchart"], ["منظور حالات استخدام لأهداف المستخدم", "منظور نشر لمواقع المعالجات", "جسم إجراء يضم متغيرات محلية", "مخطط تدفق تفصيلي للخوارزمية"], "Use-case diagrams express system services and actor goals at a high level.", "تعرض مخططات حالات الاستخدام خدمات النظام وأهداف الجهات بمستوى عالٍ."),
            q("ch5_transform_transaction", "Analyze", "Which DFD pattern calls for transaction analysis?", "أي نمط في DFD يناسبه تحليل المعاملات؟", ["A transaction tag selects one of several action paths", "A continuous flow passes through one central transform", "A class inherits attributes from a general class", "A sequence diagram orders object messages"], ["تحدد علامة المعاملة مساراً من عدة مسارات", "يمر تدفق مستمر عبر تحويل مركزي واحد", "يرث صنف سمات من صنف عام", "يرتب مخطط التسلسل رسائل الكائنات"], "Transaction analysis suits a dispatcher that routes by the transaction type.", "يلائم تحليل المعاملات موزعاً يوجه التنفيذ بحسب نوع المعاملة."),
        ],
    },
    {
        "id": "Quiz_Ch05_T15_Functional_Procedure_Layers",
        "title": "Functional Procedure Layers",
        "title_ar": "مستويات وصف الإجراء الوظيفي",
        "items": [
            q("ch5_procedure_layers_overview", "Understand", "How many detail levels are used for a functional procedure description?", "كم مستوى تفصيل يستخدم لوصف الإجراء الوظيفي؟", ["Four levels from purpose to procedure body", "Three levels from class to deployment node", "Five levels from user story to release", "Two levels from interface to database"], ["أربعة مستويات من الغرض إلى جسم الإجراء", "ثلاثة مستويات من الصنف إلى عقدة النشر", "خمسة مستويات من قصة المستخدم إلى الإصدار", "مستويان من الواجهة إلى قاعدة البيانات"], "The procedure description uses levels zero through three, with increasing detail.", "يستخدم وصف الإجراء المستويات من الصفر إلى ثلاثة بتفصيل متزايد."),
            q("ch5_procedure_level0", "Understand", "Which information belongs at the highest-level procedure description?", "أي معلومات تنتمي إلى المستوى الأعلى لوصف الإجراء؟", ["Its name, purpose, position, and callers", "Its local data structures and timing limits", "Its detailed body and decision branches", "Its physical servers and deployment sites"], ["اسمه وغرضه وموضعه ومستدعوه", "بناه المحلية وقيود توقيته", "جسمه التفصيلي وفروع قراراته", "خوادمه المادية ومواقع نشره"], "Level zero identifies the procedure and its context in the system.", "يحدد المستوى صفر الإجراء وسياقه ضمن النظام."),
            q("ch5_procedure_level1", "Apply", "A procedure specification lists parameters, called routines, and side effects; it is...", "يسرد وصف إجراء معاملاته وإجراءاته المستدعاة وآثاره الجانبية؛ فهو...", ["The interface-and-effects level", "The local-structure-and-timing level", "The detailed-procedure-body level", "The system-deployment-description level"], ["مستوى الواجهة والآثار الجانبية", "مستوى البنى المحلية والتوقيت", "مستوى جسم الإجراء التفصيلي", "مستوى وصف نشر النظام"], "Level one records parameters, calls, globals, side effects, and assertions.", "يسجل المستوى الأول المعاملات والاستدعاءات والمتغيرات العامة والآثار والتأكيدات."),
            q("ch5_procedure_level2", "Apply", "Where are local structures, timing limits, and exception conditions described?", "أين توصف البنى المحلية وقيود التوقيت وحالات الاستثناء؟", ["At the local-details level", "At the procedure-purpose level", "At the call-interface level", "At the deployment-node level"], ["في مستوى التفاصيل المحلية", "في مستوى غرض الإجراء", "في مستوى واجهة الاستدعاء", "في مستوى عقدة النشر"], "Level two covers local data, timing, exceptions, and limitations.", "يغطي المستوى الثاني البيانات المحلية والتوقيت والاستثناءات والقيود."),
            q("ch5_procedure_level3", "Understand", "What belongs in the most detailed procedure level?", "ما الذي ينتمي إلى مستوى الإجراء الأكثر تفصيلاً؟", ["The procedure body in a suitable notation", "The procedure name and system position", "The global callers and interface assertions", "The module hierarchy and external protocols"], ["جسم الإجراء بترميز مناسب", "اسم الإجراء وموضعه في النظام", "المستدعون العامون وتأكيدات الواجهة", "تسلسل الوحدات والبروتوكولات الخارجية"], "Level three specifies the function body using an appropriate procedural notation.", "يحدد المستوى الثالث جسم الوظيفة باستخدام ترميز إجرائي مناسب."),
            q("ch5_procedure_not_arch_layers", "Analyze", "What do the functional procedure levels describe?", "ماذا تصف مستويات الإجراء الوظيفي؟", ["Increasing detail for one procedure", "Separate architectural tiers of the full system", "Different stages of software release", "Four kinds of module coupling"], ["تفاصيل متزايدة لإجراء واحد", "طبقات معمارية منفصلة للنظام كله", "مراحل مختلفة لإصدار البرمجيات", "أربعة أنواع من اقتران الوحدات"], "These levels specify one procedure; they are not system-wide architectural layers.", "تحدد هذه المستويات إجراءً واحداً وليست طبقات معمارية للنظام كله."),
            q("ch5_procedure_level1_vs2", "Analyze", "Which distinction between the middle procedure levels is correct?", "أي تمييز بين المستويين الأوسطين للإجراء صحيح؟", ["Level one covers interfaces; level two covers local constraints", "Level one covers code bodies; level two covers system goals", "Level one covers deployment; level two covers user workflows", "Level one covers data stores; level two covers module calls"], ["يغطي الأول الواجهات والثاني القيود المحلية", "يغطي الأول أجسام الشيفرة والثاني أهداف النظام", "يغطي الأول النشر والثاني سير المستخدم", "يغطي الأول مخازن البيانات والثاني استدعاء الوحدات"], "Level one describes calls and effects, while level two adds local details and constraints.", "يصف المستوى الأول الاستدعاءات والآثار، ويضيف الثاني التفاصيل والقيود المحلية."),
            q("ch5_procedure_notation_choice", "Understand", "Which form can express a detailed procedure body?", "أي شكل يمكن أن يعبّر عن جسم إجراء تفصيلي؟", ["Pseudocode or a flowchart", "A system scope statement only", "A deployment map without behavior", "A list of user actors only"], ["شيفرة وصفية أو مخطط تدفق", "بيان نطاق النظام فقط", "خريطة نشر بلا سلوك", "قائمة الجهات المستخدمة فقط"], "The detailed procedure body may use pseudocode, decision tables, flowcharts, or similar forms.", "يمكن تمثيل جسم الإجراء التفصيلي بالشيفرة الوصفية أو جداول القرار أو مخططات التدفق وأشباهها."),
            q("ch5_structural_layer", "Understand", "Which concern belongs to the structural layer of functional design?", "أي جانب تنتمي إليه الطبقة الهيكلية في التصميم الوظيفي؟", ["Module boundaries, calls, and interface contracts", "Stepwise algorithms inside each individual procedure", "Processor assignments to physical deployment nodes", "Customer goals and planned user-facing release dates"], ["حدود الوحدات وعلاقات الاستدعاء وعقود الواجهة", "تسلسل الخوارزمية في جسم كل إجراء برمجي", "توزيع المعالجات على عقد النشر المادية للنظام", "أهداف العميل ومواعيد إصدار الواجهة للمستخدم"], "The structural layer describes module decomposition, call relationships, and interface boundaries; algorithms belong to the procedural layer.", "تصف الطبقة الهيكلية تفكيك الوحدات وعلاقات استدعائها وحدود واجهاتها، أما الخوارزميات فتخص الطبقة الإجرائية."),
            q("ch5_procedural_layer", "Understand", "What distinguishes the procedural layer from the structural layer?", "ما الذي يميز الطبقة الإجرائية عن الطبقة الهيكلية؟", ["It describes a module's internal algorithm and behavior", "It defines module boundaries and call relationships", "It assigns processors to software deployment nodes", "It records customer goals and planned release dates"], ["تصف الخوارزمية الداخلية وطريقة تنفيذ كل وحدة", "تحدد حدود الوحدات وعلاقات الاستدعاء بينها", "توزع المعالجات على عقد النشر البرمجية", "تسجل أهداف العميل ومواعيد الإصدار المخطط"], "The procedural layer specifies what the individual module does internally, while the structural layer defines its place and connections.", "تحدد الطبقة الإجرائية ما تفعله الوحدة داخلياً، بينما تحدد الطبقة الهيكلية موضعها واتصالاتها."),
        ],
    },
    {
        "id": "Quiz_Ch05_T16_IEEE_1016_Recommended_Practice",
        "title": "IEEE Recommended Practice for Software Design Descriptions",
        "title_ar": "ممارسة IEEE الموصى بها لوصف التصميم البرمجي",
        "items": [
            q("ch5_ieee_edition", "Understand", "Which revision identifier is associated with IEEE Std 1016?", "أي إصدار من IEEE 1016 يسميه مقرر المادة؟", ["The nineteen ninety-eight revision", "The two thousand nine revision", "The two thousand sixteen revision", "The nineteen ninety-five revision"], ["مراجعة عام ألف وتسعمئة وثمانية وتسعين", "مراجعة عام ألفين وتسعة", "مراجعة عام ألفين وستة عشر", "مراجعة عام ألف وتسعمئة وخمسة وتسعين"], "IEEE Std 1016-1998 is distinct from later revisions of the standard.", "تستخدم المادة IEEE Std 1016-1998 ولا ينبغي استبداله بإصدار لاحق من دون توضيح."),
            q("ch5_ieee_role", "Understand", "What does IEEE Std 1016 define for an SDD?", "ماذا يحدد IEEE Std 1016 لوثيقة SDD؟", ["Its information content, structure, and organization", "Its programming language and compiler settings", "Its project budget and staffing schedule", "Its user-interface colors and release branding"], ["محتواها المعلوماتي وبنيتها وتنظيمها", "لغة البرمجة وإعدادات المترجم", "ميزانية المشروع وجدول الموارد", "ألوان الواجهة وهوية الإصدار"], "IEEE Std 1016 recommends what information an SDD contains and how it is organized.", "يوصي IEEE Std 1016 بالمعلومات التي تتضمنها SDD وكيفية تنظيمها."),
            q("ch5_ieee_recommended", "Understand", "What type of document is IEEE Std 1016?", "كيف يوصف IEEE Std 1016 في المادة؟", ["A recommended practice for design descriptions", "A mandatory programming language standard", "A model for estimating project cost", "A protocol for deploying web applications"], ["ممارسة موصى بها لأوصاف التصميم", "معيار إلزامي للغات البرمجة", "نموذج لتقدير كلفة المشروع", "بروتوكول لنشر تطبيقات الويب"], "It is a recommended practice for software design descriptions.", "تعرفه المادة بوصفه ممارسة موصى بها لوصف التصميم البرمجي."),
            q("ch5_ieee_sdd", "Understand", "What does the abbreviation SDD stand for?", "إلى ماذا يشير الاختصار SDD؟", ["Software Design Description", "System Deployment Diagram", "Software Data Dictionary", "System Development Duration"], ["وصف التصميم البرمجي", "مخطط نشر النظام", "قاموس بيانات البرمجيات", "مدة تطوير النظام"], "SDD means Software Design Description.", "تعني SDD وصف التصميم البرمجي الذي يعرض البنية والقرارات الفنية."),
            q("ch5_ieee_method_neutral", "Analyze", "Does IEEE Std 1016 mandate one design methodology?", "هل يفرض IEEE Std 1016 منهجية تصميم واحدة؟", ["No, it addresses SDD content and organization", "Yes, it requires function-oriented design only", "Yes, it requires object-oriented design only", "No, it addresses source-code formatting only"], ["لا، فهو يعالج محتوى SDD وتنظيمها", "نعم، يفرض التصميم الموجه بالوظائف فقط", "نعم، يفرض التصميم الموجه بالكائنات فقط", "لا، فهو يعالج تنسيق الشيفرة فقط"], "The standard concerns design description information and does not prescribe one method.", "يهتم المعيار بمعلومات وصف التصميم ولا يفرض منهجية بعينها."),
            q("ch5_ieee_audience", "Understand", "Who can use an SDD as a technical design reference?", "من يستطيع استخدام SDD مرجعاً فنياً للتصميم؟", ["Developers, testers, and maintainers", "Only the marketing and finance teams", "Only the original requirements authors", "Only customers selecting interface colors"], ["المطورون والمختبرون والقائمون بالصيانة", "فريقا التسويق والمالية فقط", "مؤلفو المتطلبات الأصليون فقط", "العملاء الذين يختارون ألوان الواجهة فقط"], "An SDD communicates design decisions to people who build, verify, and maintain software.", "توصل SDD قرارات التصميم إلى من يبنون البرمجيات ويتحققون منها ويصونونها."),
            q("ch5_ieee_not_implementation", "Evaluate", "Which task falls outside the core purpose of IEEE Std 1016?", "أي مهمة تقع خارج الغرض الأساسي من IEEE Std 1016؟", ["Choosing a compiler's command-line switches", "Organizing technical design information", "Describing design entities and their interfaces", "Communicating a system's architectural views"], ["اختيار مفاتيح تشغيل المترجم", "تنظيم معلومات التصميم الفنية", "وصف كيانات التصميم وواجهاتها", "توصيل المناظير المعمارية للنظام"], "The standard structures design descriptions; it does not set compiler invocation details.", "ينظم المعيار أوصاف التصميم ولا يحدد تفاصيل تشغيل المترجم."),
            q("ch5_ieee_lineage", "Understand", "How should a cited IEEE revision be treated?", "كيف ينبغي التعامل مع مراجعة IEEE التي تسميها المادة؟", ["Keep the stated edition distinct from later revisions", "Replace it with the newest edition without comment", "Treat all standard editions as identical documents", "Omit the revision whenever the standard is named"], ["الإبقاء على الإصدار المذكور متميزاً عن اللاحق", "استبداله بالأحدث من دون توضيح", "اعتبار إصدارات المعيار وثيقة واحدة متطابقة", "حذف رقم المراجعة عند ذكر المعيار"], "IEEE Std 1016-1998 should remain distinct from later revisions.", "يجب عدم استبدال مرجع عام 1998 في المادة بإصدار لاحق من دون توضيح."),
        ],
    },
    {
        "id": "Quiz_Ch05_T17_IEEE_1016_Scope",
        "title": "Scope of IEEE Std 1016",
        "title_ar": "نطاق IEEE Std 1016",
        "items": [
            q("ch5_sdd_scope_applicability", "Understand", "What does the scope of IEEE Std 1016 establish?", "ماذا يحدد نطاق IEEE Std 1016؟", ["Its applicability to software design descriptions", "The exact programming language for every project", "A mandatory top-down design procedure", "A single user-interface notation for all systems"], ["مجالات انطباقه على أوصاف التصميم البرمجي", "لغة البرمجة المحددة لكل مشروع", "إجراء تصميم تنازلي إلزامي", "ترميز واجهة موحد لكل الأنظمة"], "The scope says where the recommended practice for SDDs applies.", "يحدد النطاق مواضع انطباق الممارسة الموصى بها لوثائق SDD."),
            q("ch5_sdd_scope_content", "Understand", "What aspects of an SDD does the standard scope address?", "ما الجوانب التي يعالجها نطاق المعيار في SDD؟", ["Required information and its organization", "Project costs and staff assignments", "Source-code style and compiler setup", "User training and release scheduling"], ["المعلومات المطلوبة وطريقة تنظيمها", "كلف المشروع وتوزيع الموظفين", "أسلوب الشيفرة وإعداد المترجم", "تدريب المستخدم وجدولة الإصدار"], "The scope concerns SDD information content and organization.", "يتعلق النطاق بمحتوى SDD المعلوماتي وتنظيمه."),
            q("ch5_sdd_scope_methodology", "Analyze", "Does the standard scope require function-oriented design?", "هل يفرض نطاق المعيار التصميم الموجه بالوظائف؟", ["No, it does not mandate a specific method", "Yes, it excludes object-oriented design", "Yes, it requires a single functional notation", "No, it applies only to source-code layout"], ["لا، فهو لا يفرض منهجية محددة", "نعم، يستبعد التصميم الموجه بالكائنات", "نعم، يفرض ترميزاً وظيفياً واحداً", "لا، فهو يخص تنسيق الشيفرة فقط"], "The recommended practice applies to SDD content without prescribing one design methodology.", "تنطبق الممارسة الموصى بها على محتوى SDD من دون فرض منهجية تصميم واحدة."),
            q("ch5_sdd_scope_ood", "Apply", "Can an object-oriented system have an SDD under this scope?", "هل يمكن لنظام كائني أن تكون له SDD ضمن هذا النطاق؟", ["Yes, the scope is independent of design method", "No, the scope covers function-oriented systems only", "No, the scope excludes systems with classes", "Yes, only when source code is already complete"], ["نعم، فالنطاق مستقل عن منهجية التصميم", "لا، فالنطاق يشمل الأنظمة الوظيفية فقط", "لا، فالنطاق يستبعد الأنظمة ذات الأصناف", "نعم، بعد اكتمال الشيفرة فقط"], "The standard does not limit SDD use to a particular design methodology.", "لا يقصر المعيار استخدام SDD على منهجية تصميم بعينها."),
            q("ch5_sdd_scope_domains", "Understand", "Which software domain is excluded from the stated scope?", "أي مجال برمجي مستثنى من النطاق المذكور؟", ["None of the listed application domains", "Commercial software alone is excluded", "Embedded software alone is excluded", "Scientific software alone is excluded"], ["لا يستثني أياً من مجالات التطبيق المذكورة", "البرمجيات التجارية وحدها مستثناة", "البرمجيات المضمنة وحدها مستثناة", "البرمجيات العلمية وحدها مستثناة"], "The scope covers commercial, scientific, embedded, and military software.", "يشمل النطاق البرمجيات التجارية والعلمية والمضمنة والعسكرية."),
            q("ch5_sdd_scope_not_lifecycle", "Evaluate", "Which claim goes beyond the scope of the SDD practice?", "أي ادعاء يتجاوز نطاق ممارسة SDD؟", ["It prescribes one mandatory development lifecycle", "It defines SDD information and arrangement", "It can apply across software domains", "It is independent of design methodology"], ["يفرض دورة تطوير واحدة إلزامية", "يحدد معلومات SDD وترتيبها", "يمكن أن ينطبق على مجالات برمجية مختلفة", "يستقل عن منهجية التصميم"], "The scope defines description guidance, not one required software lifecycle.", "يحدد النطاق إرشادات الوصف ولا يفرض دورة تطوير واحدة."),
            q("ch5_sdd_scope_not_language", "Evaluate", "Which subject is outside the standard's stated scope?", "أي موضوع يقع خارج النطاق المذكور للمعيار؟", ["The compiler settings used for implementation", "The applicability of design descriptions", "The organization of design information", "The information included in an SDD"], ["إعدادات المترجم المستخدمة في التنفيذ", "انطباق أوصاف التصميم", "تنظيم معلومات التصميم", "المعلومات التي تتضمنها SDD"], "Compiler settings concern implementation tooling rather than SDD scope.", "تتعلق إعدادات المترجم بأدوات التنفيذ لا بنطاق SDD."),
            q("ch5_sdd_scope_use", "Understand", "What may a project choose while still following the SDD scope?", "ما الذي يستطيع المشروع اختياره مع الالتزام بنطاق SDD؟", ["Its design methodology and modeling approach", "Whether to describe any design information", "Whether to organize the required SDD content", "Whether to treat the SDD as a design description"], ["منهجية التصميم وأسلوب النمذجة", "ما إذا كان سيصف أي معلومات تصميم", "ما إذا كان سينظم محتوى SDD المطلوب", "ما إذا كان سيعد SDD وصفاً للتصميم"], "The standard leaves the design method open while guiding the description.", "يترك المعيار منهجية التصميم مفتوحة مع توجيه طريقة الوصف."),
        ],
    },
    {
        "id": "Quiz_Ch05_T18_IEEE_1016_Definitions",
        "title": "IEEE Std 1016 Definitions",
        "title_ar": "تعريفات IEEE Std 1016",
        "items": [
            q("ch5_design_entity_definition", "Understand", "What is a design entity in an SDD?", "ما كيان التصميم في SDD؟", ["A distinct structural element being described", "A complete user story awaiting approval", "A physical server hosting the application", "A change request filed after release"], ["عنصر بنيوي مميز يجري وصفه", "قصة مستخدم كاملة تنتظر الاعتماد", "خادم مادي يستضيف التطبيق", "طلب تغيير مقدم بعد الإصدار"], "A design entity is a discrete structural part represented in the design description.", "كيان التصميم جزء بنيوي مميز تمثله وثيقة وصف التصميم."),
            q("ch5_design_view_definition", "Understand", "What does a design view collect?", "ماذا يجمع منظور التصميم؟", ["Attributes addressing a particular design concern", "Every source file in deployment order", "All users who approve a project plan", "Only the external data entering a system"], ["سمات تعالج جانباً تصميمياً محدداً", "ملفات الشيفرة كلها حسب ترتيب النشر", "كل المستخدمين الذين يعتمدون خطة المشروع", "البيانات الخارجية الداخلة إلى النظام فقط"], "A design view presents a subset of design attributes relevant to a concern.", "يعرض منظور التصميم مجموعة فرعية من السمات المرتبطة بجانب محدد."),
            q("ch5_sdd_definition", "Understand", "What does SDD represent?", "ماذا تمثل SDD؟", ["A technical description of software design", "A source-code executable for end users", "A user survey about system performance", "A project plan for staffing and cost"], ["وصفاً فنياً للتصميم البرمجي", "برنامجاً تنفيذياً للمستخدمين", "استطلاعاً للمستخدم عن أداء النظام", "خطة مشروع للموارد والكلفة"], "An SDD documents technical design information and architectural decisions.", "توثق SDD معلومات التصميم الفني والقرارات المعمارية."),
            q("ch5_entity_vs_view", "Analyze", "How does a design entity differ from a design view?", "بماذا يختلف كيان التصميم عن منظور التصميم؟", ["An entity is described; a view groups concern-specific attributes", "An entity is a concern; a view is an executable part", "An entity is a project team; a view is its schedule", "An entity is a testing stage; a view is a release"], ["يُوصف الكيان ويجمع المنظور سمات جانب محدد", "الكيان جانب والمنظور جزء تنفيذي", "الكيان فريق والمنظور جدوله", "الكيان مرحلة اختبار والمنظور إصدار"], "An entity is a structural element; a view organizes information about design concerns.", "الكيان عنصر بنيوي، والمنظور ينظم معلومات عن جوانب التصميم."),
            q("ch5_entity_examples", "Apply", "Which item can be treated as a design entity?", "أي عنصر يمكن اعتباره كيان تصميم؟", ["A subsystem with defined structural responsibilities", "A meeting invitation sent to the project team", "A budget total without a software element", "A user complaint with no design response"], ["نظام فرعي له مسؤوليات بنيوية محددة", "دعوة اجتماع مرسلة إلى فريق المشروع", "مجموع ميزانية بلا عنصر برمجي", "شكوى مستخدم بلا استجابة تصميمية"], "Subsystems and other structural software parts can be design entities.", "يمكن أن تكون الأنظمة الفرعية وأجزاء البرمجيات البنيوية كيانات تصميم."),
            q("ch5_view_concern", "Apply", "A view groups interface attributes for focused inspection; it is...", "جمع منظور سمات الواجهة لتفتيش مركز؛ فهذا المنظور...", ["Concern-specific design information", "A separate executable subsystem", "A project-level staffing estimate", "A user-level acceptance decision"], ["معلومات تصميم مخصصة لجانب محدد", "نظاماً فرعياً تنفيذياً مستقلاً", "تقديراً للموارد على مستوى المشروع", "قرار قبول على مستوى المستخدم"], "A design view organizes a relevant subset of information for a particular concern.", "ينظم منظور التصميم مجموعة معلومات مناسبة لجانب معين."),
            q("ch5_definitions_purpose", "Understand", "Why does a standard definitions section help a design team?", "كيف يفيد قسم التعريفات القياسي فريق التصميم؟", ["It gives shared meanings to design terms", "It assigns each developer a release deadline", "It selects the project's implementation language", "It replaces review of interface details"], ["يوحد معاني مصطلحات التصميم", "يحدد موعد إصدار لكل مطور", "يختار لغة تنفيذ المشروع", "يستبدل مراجعة تفاصيل الواجهات"], "Shared terminology reduces ambiguity when people discuss design entities and views.", "تقلل المصطلحات المشتركة الالتباس عند مناقشة كيانات التصميم ومناظره."),
            q("ch5_view_not_diagram", "Evaluate", "Which statement best describes a design view?", "أي عبارة تصف منظور التصميم بأفضل صورة؟", ["An organized subset of design information for a concern", "A mandatory single drawing for the entire system", "A full list of project risks and controls", "A compiled version of a software component"], ["مجموعة منظمة من معلومات التصميم لجانب محدد", "رسم إلزامي واحد للنظام كله", "قائمة كاملة بمخاطر المشروع وضوابطه", "نسخة مترجمة لمكون برمجي"], "A view is a concern-oriented organization of design information, not one required diagram.", "المنظور تنظيم لمعلومات التصميم بحسب جانب معين وليس مخططاً واحداً إلزامياً."),
        ],
    },
    {
        "id": "Quiz_Ch05_T19_Purpose_Of_SDD",
        "title": "Purpose of a Software Design Description",
        "title_ar": "الغرض من وصف التصميم البرمجي",
        "items": [
            q("ch5_sdd_purpose", "Understand", "What is the primary purpose of an SDD?", "ما الغرض الرئيس من SDD؟", ["Guide implementation with an authoritative design description", "Replace requirements with executable code", "Record only defects discovered after release", "Select the customer's commercial pricing model"], ["توجيه التنفيذ بوصف تصميم رسمي", "استبدال المتطلبات بشيفرة قابلة للتنفيذ", "تسجيل العيوب المكتشفة بعد الإصدار فقط", "اختيار نموذج التسعير التجاري للعميل"], "An SDD gives implementation teams an authoritative technical design reference.", "توفر SDD لفرق التنفيذ مرجعاً فنياً معتمداً للتصميم."),
            q("ch5_sdd_implementation", "Apply", "Implementers disagree about an interface; what should the SDD provide?", "اختلف المنفذون حول واجهة؛ ماذا ينبغي أن توفر SDD؟", ["The documented interface decision", "A replacement user requirement", "A post-release marketing plan", "An unrelated deployment budget"], ["قرار الواجهة الموثق", "متطلب مستخدم بديل", "خطة تسويقية بعد الإصدار", "ميزانية نشر غير مرتبطة"], "The SDD records design decisions that guide consistent implementation.", "تسجل SDD قرارات التصميم التي توجه التنفيذ المتسق."),
            q("ch5_sdd_verification", "Understand", "How can an SDD support verification against the SRS?", "كيف تدعم SDD التحقق بالمقارنة مع SRS؟", ["It provides a technical baseline to compare with requirements", "It removes the need to retain requirements", "It measures only the speed of completed code", "It converts test results into user stories"], ["توفر أساساً فنياً يقارن بالمتطلبات", "تلغي الحاجة إلى حفظ المتطلبات", "تقيس سرعة الشيفرة المكتملة فقط", "تحول نتائج الاختبار إلى قصص مستخدم"], "The SDD can be checked against the SRS to see whether the design addresses required behavior.", "يمكن مقارنة SDD مع SRS للتحقق من معالجة التصميم للسلوك المطلوب."),
            q("ch5_sdd_maintenance", "Understand", "Why is an SDD useful after initial implementation?", "لماذا تبقى SDD مفيدة بعد التنفيذ الأولي؟", ["It preserves design information for maintenance", "It prevents all future requirement changes", "It replaces every future software test", "It contains the only valid copy of source code"], ["تحفظ معلومات التصميم لأعمال الصيانة", "تمنع كل تغييرات المتطلبات المستقبلية", "تستبدل كل اختبار برمجي لاحق", "تحتوي النسخة الصحيحة الوحيدة من الشيفرة"], "Lifecycle design information helps maintainers understand existing decisions.", "تساعد معلومات التصميم عبر دورة الحياة القائمين بالصيانة على فهم القرارات القائمة."),
            q("ch5_sdd_review", "Apply", "Which artifact can reviewers inspect to examine architectural choices?", "أي وثيقة يستطيع المراجعون فحصها لدراسة الخيارات المعمارية؟", ["The Software Design Description", "The marketing campaign calendar", "The payroll approval register", "The user attendance report"], ["وصف التصميم البرمجي", "تقويم الحملة التسويقية", "سجل اعتماد الرواتب", "تقرير حضور المستخدمين"], "The SDD records the design that is examined in a technical review.", "تسجل SDD التصميم الذي يجري فحصه في المراجعة الفنية."),
            q("ch5_sdd_guessing", "Analyze", "How does a clear SDD reduce implementation guesswork?", "كيف يقلل وصف واضح للتصميم التخمين أثناء التنفيذ؟", ["It states architectural and interface decisions", "It lets each team invent incompatible interfaces", "It hides component responsibilities from builders", "It lists only user complaints without resolutions"], ["يحدد القرارات المعمارية وقرارات الواجهات", "يتيح لكل فريق ابتكار واجهات غير متوافقة", "يخفي مسؤوليات المكونات عن المنفذين", "يسرد شكاوى المستخدم بلا حلول فقط"], "Documented decisions give builders a shared basis for their implementation choices.", "توفر القرارات الموثقة أساساً مشتركاً لخيارات التنفيذ لدى الفرق."),
            q("ch5_sdd_not_code", "Evaluate", "Which claim about an SDD is accurate?", "أي ادعاء عن SDD صحيح؟", ["It guides implementation but is not executable software", "It is the final running product for customers", "It guarantees that the coded system has no defects", "It eliminates the need for design review"], ["توجه التنفيذ لكنها ليست برمجيات قابلة للتشغيل", "هي المنتج النهائي الذي يعمل للعملاء", "تضمن خلو النظام المبرمج من العيوب", "تلغي الحاجة إلى مراجعة التصميم"], "An SDD describes the design; implementation and verification remain separate activities.", "تصف SDD التصميم، بينما يبقى التنفيذ والتحقق نشاطين منفصلين."),
            q("ch5_sdd_audience_purpose", "Understand", "What lifecycle role does an SDD play?", "ما دور SDD عبر دورة حياة البرمجيات؟", ["Communicating design decisions to later teams", "Setting the initial business price for users", "Approving annual leave for developers", "Selecting the organization's hiring policy"], ["إيصال قرارات التصميم إلى الفرق اللاحقة", "تحديد السعر التجاري الأولي للمستخدمين", "اعتماد إجازات المطورين السنوية", "اختيار سياسة التوظيف للمؤسسة"], "The document carries technical design knowledge across implementation and maintenance.", "تنقل الوثيقة المعرفة الفنية بالتصميم عبر التنفيذ والصيانة."),
        ],
    },
    {
        "id": "Quiz_Ch05_T20_Design_Description_Information_Content",
        "title": "SDD Information Content",
        "title_ar": "محتوى المعلومات في SDD",
        "items": [
            q("ch5_sdd_attributes_set", "Understand", "Which set matches the design-entity information attributes?", "أي مجموعة تطابق سمات معلومات كيان التصميم؟", ["Identification, type, purpose, function, subordinates, dependencies, interfaces, resources, processing, data", "Actors, use cases, activities, messages, classes, states, components, nodes, packages, tests", "Cost, effort, schedule, staff, risk, duration, quality, budget, market, release", "Input, output, storage, control, timing, ownership, security, workload, price, policy"], ["التعريف والنوع والغرض والوظيفة والتابعون والاعتماديات والواجهات والموارد والمعالجة والبيانات", "الجهات وحالات الاستخدام والأنشطة والرسائل والأصناف والحالات والعقد والاختبارات", "الكلفة والجهد والجدول والموارد والمخاطر والمدة والجودة والميزانية", "المدخلات والمخرجات والخزن والتحكم والتوقيت والملكية والأمن والسعر"], "Each design entity is described through a defined set of attributes.", "تسرد المادة عشر سمات لوصف كل كيان تصميم."),
            q("ch5_sdd_entity_identifier", "Understand", "Which attribute identifies a design entity?", "أي سمة تحدد كيان التصميم؟", ["Identification", "Processing", "Resources", "Dependencies"], ["التعريف", "المعالجة", "الموارد", "الاعتماديات"], "Identification distinguishes the entity being described.", "تميز سمة التعريف كيان التصميم الذي يجري وصفه."),
            q("ch5_sdd_entity_interface", "Apply", "Where should an entity's communication contract be described?", "أين يوصف عقد التواصل الخاص بكيان؟", ["In its interface information", "In its resource allocation only", "In its processing description only", "In its identifying label only"], ["ضمن معلومات واجهته", "ضمن تخصيص موارده فقط", "ضمن وصف معالجته فقط", "ضمن اسمه التعريفي فقط"], "The interface attribute records how the entity communicates with other parts.", "تسجل سمة الواجهة كيفية تواصل الكيان مع الأجزاء الأخرى."),
            q("ch5_sdd_entity_subordinates", "Apply", "Which attribute records the lower-level elements owned by an entity?", "أي سمة تسجل العناصر الأدنى التابعة لكيان؟", ["Subordinates", "Dependencies", "Purpose", "Data"], ["العناصر التابعة", "الاعتماديات", "الغرض", "البيانات"], "Subordinates describe lower-level design entities beneath the entity.", "تصف سمة العناصر التابعة كيانات التصميم ذات المستوى الأدنى."),
            q("ch5_sdd_entity_dependencies", "Apply", "Which attribute records a design entity's reliance on other elements?", "أي سمة تسجل اعتماد كيان التصميم على عناصر أخرى؟", ["Dependencies", "Subordinates", "Identification", "Processing"], ["الاعتماديات", "العناصر التابعة", "التعريف", "المعالجة"], "Dependencies identify other elements on which the entity relies.", "تحدد سمة الاعتماديات العناصر الأخرى التي يعتمد عليها الكيان."),
            q("ch5_sdd_entity_resources", "Understand", "Which attribute captures resources needed by a design entity?", "أي سمة تسجل الموارد التي يحتاج إليها كيان التصميم؟", ["Resources", "Purpose", "Function", "Identification"], ["الموارد", "الغرض", "الوظيفة", "التعريف"], "The resources attribute records resources associated with the entity.", "تسجل سمة الموارد الموارد المرتبطة بالكيان."),
            q("ch5_sdd_entity_processing", "Understand", "Which attribute describes an entity's processing details?", "أي سمة تصف تفاصيل معالجة الكيان؟", ["Processing", "Dependencies", "Subordinates", "Identification"], ["المعالجة", "الاعتماديات", "العناصر التابعة", "التعريف"], "Processing captures the processing information associated with the design entity.", "تسجل سمة المعالجة معلومات المعالجة المرتبطة بكيان التصميم."),
            q("ch5_sdd_content_vs_view", "Analyze", "How do entity attributes relate to design views?", "كيف ترتبط سمات الكيان بمناظير التصميم؟", ["Views organize entity attributes around concerns", "Attributes replace all design entities in the SDD", "Views are executable forms of every attribute", "Attributes describe only the deployment hardware"], ["تنظم المناظير سمات الكيان بحسب جوانب التصميم", "تستبدل السمات كل كيانات التصميم في SDD", "المناظير صيغ تنفيذية لكل سمة", "تصف السمات أجهزة النشر فقط"], "Attributes describe entities; views arrange relevant information for focused concerns.", "تصف السمات الكيانات، وتنظم المناظير المعلومات المناسبة لجوانب محددة."),
        ],
    },
    {
        "id": "Quiz_Ch05_T21_Design_Description_Organization",
        "title": "Design Description Organization",
        "title_ar": "تنظيم وصف التصميم",
        "items": [
            q("ch5_sdd_views_set", "Understand", "Which set names the four design views for an SDD?", "أي مجموعة تسمي مناظير التصميم الأربعة في المادة؟", ["Decomposition, dependency, interface, detailed design", "Use case, activity, sequence, deployment", "Input, transform, output, transaction", "Data, control, procedural, communicational"], ["التفكيك والاعتمادية والواجهة والتصميم التفصيلي", "حالات الاستخدام والنشاط والتسلسل والنشر", "المدخل والتحويل والمخرج والمعاملة", "البيانات والتحكم والإجرائي والاتصالي"], "The four views organize design information into decomposition, dependency, interface, and detail.", "تنظم المناظير الأربعة معلومات التصميم في التفكيك والاعتمادية والواجهة والتفصيل."),
            q("ch5_sdd_decomposition_view", "Understand", "What does the decomposition view show?", "ماذا يعرض منظور التفكيك؟", ["The subsystem and component hierarchy", "The dependencies between external protocols", "The public interface and communication rules", "The internal algorithm and local data"], ["التسلسل الهرمي للأنظمة والمكونات", "الاعتماديات بين البروتوكولات الخارجية", "الواجهة العامة وقواعد التواصل", "الخوارزمية الداخلية والبيانات المحلية"], "The decomposition view represents how the system is divided into lower-level parts.", "يمثل منظور التفكيك كيفية تقسيم النظام إلى أجزاء أدنى."),
            q("ch5_sdd_dependency_view", "Understand", "Which view focuses on relationships and dependencies among parts?", "أي منظور يركز على العلاقات والاعتماديات بين الأجزاء؟", ["Dependency view", "Interface view", "Detailed design view", "Decomposition view"], ["منظور الاعتمادية", "منظور الواجهة", "منظور التصميم التفصيلي", "منظور التفكيك"], "The dependency view describes dependencies among design entities and resources.", "يصف منظور الاعتمادية الاعتماديات بين كيانات التصميم وموارده."),
            q("ch5_sdd_interface_view", "Apply", "A reviewer needs parameter and communication contracts; which view helps?", "يحتاج المراجع إلى عقود المعاملات والتواصل؛ أي منظور يساعده؟", ["The interface view", "The dependency view", "The detailed design view", "The decomposition view"], ["منظور الواجهة", "منظور الاعتمادية", "منظور التصميم التفصيلي", "منظور التفكيك"], "The interface view presents public signatures and communication contracts.", "يعرض منظور الواجهة التواقيع العامة وعقود التواصل."),
            q("ch5_sdd_detail_view", "Apply", "Where should internal algorithms and data structures be organized?", "أين ينبغي تنظيم الخوارزميات الداخلية وبنى البيانات؟", ["In the detailed design view", "In the dependency view", "In the interface view", "In the scope statement"], ["في منظور التصميم التفصيلي", "في منظور الاعتمادية", "في منظور الواجهة", "في بيان النطاق"], "The detailed design view records internal algorithms, state, and data structures.", "يسجل منظور التصميم التفصيلي الخوارزميات الداخلية والحالة وبنى البيانات."),
            q("ch5_sdd_content_vs_organization", "Analyze", "What is the difference between SDD content and organization?", "ما الفرق بين محتوى SDD وتنظيمها؟", ["Content names the information; organization groups it into views", "Content names the views; organization selects the software domain", "Content is executable; organization is the source code", "Content sets the project budget; organization assigns staff"], ["يسمي المحتوى المعلومات وينظمها العرض ضمن مناظير", "يسمي المحتوى المناظير ويختار التنظيم المجال البرمجي", "المحتوى قابل للتنفيذ والتنظيم هو الشيفرة", "يحدد المحتوى الميزانية ويوزع التنظيم الموظفين"], "Entity attributes define information content, while design views organize that information.", "تحدد سمات الكيان محتوى المعلومات، وتنظم مناظير التصميم تلك المعلومات."),
            q("ch5_sdd_views_purpose", "Understand", "Why organize design information into separate views?", "لماذا تنظم معلومات التصميم في مناظير منفصلة؟", ["Each view helps inspect a specific concern", "Every view duplicates the complete source code", "Views remove the need to identify entities", "Each view replaces the requirements specification"], ["يساعد كل منظور على فحص جانب محدد", "يكرر كل منظور الشيفرة كاملة", "تلغي المناظير الحاجة إلى تحديد الكيانات", "يستبدل كل منظور مواصفة المتطلبات"], "Concern-oriented views make different aspects of the design easier to inspect.", "تسهل المناظير المخصصة لجوانب محددة فحص أبعاد التصميم المختلفة."),
            q("ch5_sdd_function_view_note", "Understand", "In which design view is the Function attribute organized?", "في أي منظور تضع المادة سمة Function؟", ["The decomposition view", "The interface view", "The dependency view", "The detailed design view"], ["منظور التفكيك", "منظور الواجهة", "منظور الاعتمادية", "منظور التصميم التفصيلي"], "The Function attribute is organized in the Decomposition view.", "تضع المادة سمة Function ضمن منظور التفكيك."),
        ],
    },
    {
        "id": "Quiz_Ch05_T22_Object_Oriented_Design",
        "title": "Object-Oriented Design",
        "title_ar": "التصميم الموجه بالكائنات",
        "items": [
            q("ch5_ood_definition", "Understand", "What is the organizing basis of object-oriented design?", "ما أساس التنظيم في التصميم الموجه بالكائنات؟", ["Interacting objects and their classes", "A hierarchy of procedures alone", "Data-flow paths without structural entities", "Deployment nodes without software behavior"], ["الكائنات المتفاعلة وأصنافها", "تسلسل الإجراءات وحده", "مسارات البيانات بلا عناصر بنيوية", "عقد النشر بلا سلوك برمجي"], "OOD organizes software design around objects and classes that interact.", "ينظم OOD تصميم البرمجيات حول كائنات وأصناف تتفاعل."),
            q("ch5_ood_domain_model", "Understand", "What do objects commonly represent in an object-oriented design?", "ماذا تمثل الكائنات عادة في التصميم الموجه بالكائنات؟", ["Entities with identity, state, and behavior", "Only files containing source-code comments", "Only hardware devices in a network", "Functions without data or identity"], ["كيانات لها هوية وحالة وسلوك", "ملفات تحوي تعليقات الشيفرة فقط", "أجهزة مادية في شبكة فقط", "وظائف بلا بيانات أو هوية"], "An object is an entity with its own identity, state, and behavior.", "الكائن كيان له هوية وحالة وسلوك خاص به."),
            q("ch5_ood_vs_fod", "Analyze", "Which contrast between OOD and FOD is accurate?", "أي مقارنة بين OOD وFOD صحيحة؟", ["OOD centers on objects; FOD centers on functions", "OOD centers on procedures; FOD centers on objects", "Both center only on database storage", "Neither approach models system responsibilities"], ["يركز OOD على الكائنات وFOD على الوظائف", "يركز OOD على الإجراءات وFOD على الكائنات", "يركز كلاهما على تخزين البيانات فقط", "لا يمثل أي نهج مسؤوليات النظام"], "The primary modeling focus differs: objects for OOD and functions for FOD.", "يختلف محور النمذجة الأساس؛ فـOOD للكائنات وFOD للوظائف."),
            q("ch5_ood_class", "Understand", "What does a class describe?", "ماذا يصف الصنف؟", ["Common structure and behavior for related objects", "One specific runtime message between objects", "A deployment machine and its network address", "An ordered sequence of unrelated procedures"], ["البنية والسلوك المشتركين لكائنات مترابطة", "رسالة تشغيل واحدة بين كائنات", "آلة نشر وعنوانها الشبكي", "تسلسلاً لإجراءات غير مترابطة"], "A class is a blueprint that describes common characteristics of its objects.", "الصنف مخطط يصف الخصائص المشتركة لكائناته."),
            q("ch5_ood_encapsulation", "Understand", "What does encapsulation do in object-oriented design?", "ماذا يحقق التغليف في التصميم الموجه بالكائنات؟", ["Hides internal representation behind an interface", "Exposes every field to direct external changes", "Combines unrelated procedures in one file", "Removes all communication between objects"], ["يخفي التمثيل الداخلي خلف واجهة", "يكشف كل حقل للتعديل الخارجي المباشر", "يجمع إجراءات غير مترابطة في ملف", "يلغي كل تواصل بين الكائنات"], "Encapsulation protects internal state by controlling access through an interface.", "يحمي التغليف الحالة الداخلية بتنظيم الوصول عبر واجهة."),
            q("ch5_ood_abstraction_focus", "Understand", "What does abstraction emphasize when modeling an object?", "على ماذا يركز التجريد عند نمذجة كائن؟", ["Relevant properties while omitting needless detail", "Every implementation detail before requirements", "Only the object's location in deployment", "All possible operations regardless of purpose"], ["الخصائص المهمة مع إغفال التفاصيل غير اللازمة", "كل تفاصيل التنفيذ قبل المتطلبات", "موقع الكائن في النشر فقط", "كل العمليات الممكنة بصرف النظر عن الغرض"], "Abstraction retains properties relevant to the model's purpose.", "يحتفظ التجريد بالخصائص المرتبطة بغرض النموذج."),
            q("ch5_ood_change_locality", "Apply", "A change to a class representation leaves its callers unchanged; what explains this?", "تغير تمثيل الصنف من دون تأثر مستدعيه؛ ما الذي يفسر ذلك؟", ["Encapsulation behind a stable public interface", "Inheritance that exposes every internal field", "Message passing without an operation contract", "Polymorphism that removes all class boundaries"], ["التغليف خلف واجهة عامة مستقرة", "وراثة تكشف كل الحقول الداخلية", "تمرير رسائل بلا عقد للعمليات", "تعدد أشكال يلغي حدود الأصناف"], "When callers depend on a stable interface, internal representation changes can remain local.", "عندما يعتمد المستدعون على واجهة مستقرة، يمكن حصر تغييرات التمثيل الداخلي."),
            q("ch5_ood_not_guarantee", "Evaluate", "Which claim about object-oriented design is appropriately limited?", "أي ادعاء عن التصميم الكائني مضبوط بحدوده؟", ["It can help represent domain entities, but is not best for every case", "It guarantees fewer defects in every software system", "It eliminates the need for interfaces and testing", "It always costs less than function-oriented design"], ["يساعد على تمثيل كيانات المجال لكنه لا يلائم كل حالة", "يضمن عيوباً أقل في كل نظام برمجي", "يلغي الحاجة إلى الواجهات والاختبار", "يقلل الكلفة دائماً مقارنة بالتصميم الوظيفي"], "OOD offers a useful modeling approach, not a universal guarantee of superiority.", "يوفر OOD أسلوب نمذجة مفيداً لا ضماناً عاماً بالتفوق."),
        ],
    },
    {
        "id": "Quiz_Ch05_T23_Object_Oriented_Basic_Concepts",
        "title": "Object-Oriented Basic Concepts",
        "title_ar": "المفاهيم الأساسية للتصميم الكائني",
        "items": [
            q("ch5_ood_basic_set", "Understand", "Which set names the central object-oriented concepts?", "أي مجموعة تسمي المفاهيم الكائنية الأساسية؟", ["Objects, classes, messages, abstraction, inheritance, polymorphism", "Processes, tables, transactions, scheduling, cost, reliability", "Inputs, stores, transformations, reports, branches, deployment", "Risks, estimates, milestones, staffing, reviews, releases"], ["الكائنات والأصناف والرسائل والتجريد والوراثة وتعدد الأشكال", "العمليات والجداول والمعاملات والجدولة والكلفة والاعتمادية", "المدخلات والمخازن والتحويلات والتقارير والفروع والنشر", "المخاطر والتقديرات والمراحل والموارد والمراجعات والإصدارات"], "These concepts form core object-oriented vocabulary.", "تشكل هذه المفاهيم مفردات التصميم الكائني الأساسية في الفصل."),
            q("ch5_ood_object", "Understand", "What gives an object its identity as a runtime entity?", "ما الذي يمنح الكائن هويته بوصفه كياناً أثناء التشغيل؟", ["Its identity, state, and behavior", "Its class name without any instance state", "Its position in a printed structure chart", "Its source file size and release date"], ["هويته وحالته وسلوكه", "اسم صنفه من دون حالة للنسخة", "موضعه في مخطط بنية مطبوع", "حجم ملفه وتاريخ إصداره"], "An object combines identity with state and behavior.", "يجمع الكائن الهوية والحالة والسلوك."),
            q("ch5_ood_message", "Understand", "What is message passing between objects?", "ما تمرير الرسائل بين الكائنات؟", ["One object requests an operation from another", "One class stores another class's source file", "One procedure changes a global flag without a call", "One diagram assigns hardware to a software node"], ["طلب كائن عملية من كائن آخر", "خزن صنف ملف شيفرة صنف آخر", "تغيير إجراء علماً عاماً بلا استدعاء", "تخصيص مخطط جهازاً لعقدة برمجية"], "Message passing is a communication request for an operation.", "تمرير الرسائل طلب تواصل لتنفيذ عملية."),
            q("ch5_ood_polymorphism", "Understand", "What does polymorphism allow for one operation?", "ماذا يتيح تعدد الأشكال للعملية الواحدة؟", ["Different object types can provide different implementations", "Every object must store the same internal data", "A class must contain only one method", "A message can be sent only during compilation"], ["تقديم أنواع كائنات مختلفة تطبيقات مختلفة", "تخزين كل كائن للبيانات الداخلية نفسها", "احتواء الصنف طريقة واحدة فقط", "إرسال الرسالة أثناء الترجمة فقط"], "Polymorphism lets the same operation have type-specific behavior.", "يتيح تعدد الأشكال للعملية نفسها سلوكاً يختلف باختلاف نوع الكائن."),
            q("ch5_basic_inheritance", "Apply", "A specialized type inherits shared characteristics from a general type; this is...", "ورث نوع متخصص خصائص مشتركة من نوع عام؛ هذا هو...", ["Inheritance", "Encapsulation", "Message passing", "Temporal cohesion"], ["الوراثة", "التغليف", "تمرير الرسائل", "التماسك الزمني"], "Inheritance expresses a relationship between general and specialized classes.", "تعبر الوراثة عن علاقة بين أصناف عامة ومتخصصة."),
            q("ch5_basic_abstraction", "Apply", "A caller uses a stack operation without seeing its storage layout; this illustrates...", "استخدم المستدعي عملية للمكدس من دون رؤية طريقة خزنه؛ وهذا يوضح...", ["Abstraction of relevant behavior", "Direct access to internal representation", "Content coupling between two classes", "A deployment view of object storage"], ["تجريد السلوك ذي الصلة", "الوصول المباشر إلى التمثيل الداخلي", "اقتران المحتوى بين صنفين", "منظور نشر لخزن الكائن"], "Abstraction lets a user rely on relevant operations without internal details.", "يتيح التجريد الاعتماد على العمليات المناسبة من دون معرفة التفاصيل الداخلية."),
            q("ch5_ood_adt_class", "Analyze", "Which statement avoids equating every class with an ADT?", "أي عبارة تتجنب مساواة كل صنف بـADT؟", ["An ADT specifies operations; a class describes shared object features", "An ADT is always a class with inheritance and polymorphism", "A class is only a table of values with no behavior", "An ADT exposes its storage representation to every caller"], ["يحدد ADT العمليات ويصف الصنف سمات الكائنات المشتركة", "يكون ADT دائماً صنفاً يرث ويتعدد شكله", "الصنف جدول قيم بلا سلوك", "يكشف ADT تمثيله المخزني لكل مستدعٍ"], "The terms are related but not interchangeable; their definitions emphasize different aspects.", "المصطلحان مرتبطان لكنهما غير متطابقين، إذ يركز كل تعريف على جوانب مختلفة."),
            q("ch5_ood_inheritance_caution", "Evaluate", "When is inheritance for reuse alone a poor choice?", "متى تكون الوراثة لمجرد إعادة الاستخدام خياراً ضعيفاً؟", ["When the general-specialized relationship is unclear", "When shared behavior genuinely belongs to a base type", "When a class has a well-defined interface", "When a subtype specializes valid inherited behavior"], ["عندما تكون علاقة العام بالمتخصص غير واضحة", "عندما ينتمي السلوك المشترك فعلاً إلى النوع الأساس", "عندما يملك الصنف واجهة محددة جيداً", "عندما يخصص النوع الفرعي سلوكاً موروثاً مناسباً"], "Inheritance adds a type relationship; reuse alone does not justify a misleading hierarchy.", "تضيف الوراثة علاقة بين الأنواع، ولا تبرر إعادة الاستخدام وحدها تسلسلاً مضللاً."),
            q("ch5_ood_inheritance_without_polymorphism", "Understand", "Can inheritance express a valid type relationship without polymorphic overriding?", "هل يمكن للوراثة تمثيل علاقة أنواع صحيحة من دون تعدد أشكال عبر إعادة التعريف؟", ["Inheritance can express a type relation without method overriding", "Inheritance requires every subtype to redefine shared methods", "Polymorphism and inheritance describe the same type feature", "A class cannot inherit unless several methods are overloaded"], ["قد تمثل الوراثة علاقة أنواع حتى بلا إعادة تعريف الطرق", "تشترط الوراثة إعادة تعريف الطرق المشتركة كلها", "الوراثة وتعدد الأشكال هما الخاصية التصميمية نفسها", "لا يرث الصنف إلا مع تحميل عدة طرق بالاسم نفسه"], "Inheritance can express specialization even when a subtype does not override a method; it is related to, but not identical with, polymorphism.", "قد تمثل الوراثة التخصص من دون أن يعيد النوع الفرعي تعريف طريقة؛ فهي مرتبطة بتعدد الأشكال لكنها ليست مطابقة له."),
            q("ch5_ood_class_quality", "Apply", "Which practice supports a reusable, well-formed class?", "أي ممارسة تدعم صنفاً جيداً وقابلاً لإعادة الاستخدام؟", ["Keep a class concept, state, and operations coherent", "Combine unrelated ideas to reduce the number of classes", "Expose internal representation as the class's public interface", "Use inheritance without a valid general-specialized relation"], ["اجمع مفهوماً مترابطاً مع حالته وعملياته المناسبة", "ادمج مفاهيم غير مرتبطة لتقليل عدد الأصناف", "اكشف التمثيل الداخلي بوصفه الواجهة العامة للصنف", "استخدم الوراثة بلا علاقة صحيحة بين الأنواع"], "A coherent class models a meaningful concept and keeps its relevant state and operations together.", "يمثل الصنف المترابط مفهوماً ذا معنى ويجمع حالته وعملياته ذات الصلة."),
        ],
    },
    {
        "id": "Quiz_Ch05_T24_OO_Analysis_And_Design_Steps",
        "title": "Steps to Analyze and Design an Object-Oriented System",
        "title_ar": "خطوات تحليل وتصميم نظام موجه بالكائنات",
        "items": [
            q("ch5_oo_process_first", "Understand", "What is the first major activity in the stated OO analysis and design sequence?", "ما النشاط الرئيس الأول في تسلسل التحليل والتصميم الكائني؟", ["Create a use-case model with actors and use cases", "Create component and deployment diagrams", "Prepare final design documents", "Create object and state diagrams"], ["إنشاء نموذج حالات استخدام يضم الجهات والحالات", "إنشاء مخططات المكونات والنشر", "إعداد وثائق التصميم النهائية", "إنشاء مخططات الكائنات والحالات"], "The process begins by identifying actors and use cases and modeling them.", "تبدأ العملية بتحديد الجهات وحالات الاستخدام ونمذجتها."),
            q("ch5_oo_process_activity_optional", "Understand", "When is an activity diagram created in the stated sequence?", "متى ينشأ مخطط النشاط ضمن التسلسل المذكور؟", ["If required by the system analysis", "Before identifying any actors", "After design documents are finalized", "For every use case without exception"], ["عند الحاجة إليه في تحليل النظام", "قبل تحديد أي جهة مستخدمة", "بعد إكمال وثائق التصميم", "لكل حالة استخدام بلا استثناء"], "The activity diagram is a conditional step, not an unconditional requirement.", "مخطط النشاط خطوة مشروطة وليس متطلباً إلزامياً في كل حالة."),
            q("ch5_oo_process_interaction", "Understand", "What is prepared for each use case during interaction modeling?", "ماذا يجهز لكل حالة استخدام أثناء نمذجة التفاعل؟", ["Objects and sequence or collaboration diagrams", "Data tables and deployment node labels", "Risk registers and cost estimate charts", "Source-code listings and test results"], ["الكائنات ومخططات التسلسل أو التعاون", "جداول البيانات وتسميات عقد النشر", "سجلات المخاطر ومخططات الكلفة", "قوائم الشيفرة ونتائج الاختبار"], "Interaction modeling identifies participating objects and describes their messages.", "تحدد نمذجة التفاعل الكائنات المشاركة وتصف الرسائل بينها."),
            q("ch5_oo_process_class", "Understand", "Which diagram captures the system's classes and their structural relations?", "أي مخطط يلتقط أصناف النظام وعلاقاتها البنيوية؟", ["A class diagram", "An activity diagram", "A deployment diagram", "A flowchart"], ["مخطط الأصناف", "مخطط النشاط", "مخطط النشر", "مخطط التدفق"], "The class diagram describes the static class structure and relationships.", "يصف مخطط الأصناف البنية الساكنة للأصناف وعلاقاتها."),
            q("ch5_oo_process_state_optional", "Understand", "When are state-chart and object diagrams included?", "متى تضاف مخططات الحالة والكائن؟", ["If required by the design", "Before the use-case model in every system", "Only after the application is deployed", "Instead of all interaction diagrams"], ["عند الحاجة إليها في التصميم", "قبل نموذج حالات الاستخدام في كل نظام", "بعد نشر التطبيق فقط", "بدلاً من مخططات التفاعل كلها"], "The process marks state-chart and object diagrams as conditional.", "تعد العملية مخططات الحالة والكائن مشروطة بالحاجة."),
            q("ch5_oo_process_components", "Understand", "Which diagrams describe implementation components and physical allocation?", "أي مخططات تصف مكونات التنفيذ والتوزيع المادي؟", ["Component and deployment diagrams", "Activity and use-case diagrams", "Class and state-chart diagrams", "Sequence and collaboration diagrams"], ["مخططا المكونات والنشر", "مخططا النشاط وحالات الاستخدام", "مخططا الأصناف والحالة", "مخططا التسلسل والتعاون"], "Component and deployment views are prepared after the structural and interaction models.", "تُعد مناظير المكونات والنشر بعد نماذج البنية والتفاعل."),
            q("ch5_oo_process_order", "Analyze", "Which sequence follows the stated process from interaction modeling onward?", "أي تسلسل يتبع تنظيم التحليل والتصميم ابتداءً من نمذجة التفاعل؟", ["Interaction, class, optional state and object, components and deployment", "Class, deployment, use cases, optional activity, interaction", "Deployment, interaction, state, use cases, class", "Activity, components, use cases, class, interaction"], ["التفاعل ثم الأصناف فالحالة والكائن عند الحاجة ثم المكونات والنشر", "الأصناف ثم النشر فحالات الاستخدام والنشاط والتفاعل", "النشر ثم التفاعل والحالة وحالات الاستخدام والأصناف", "النشاط ثم المكونات وحالات الاستخدام والأصناف والتفاعل"], "The stated sequence moves from interactions to classes, optional diagrams, then components and deployment.", "ينتقل الترتيب من التفاعلات إلى الأصناف فالمخططات المشروطة ثم المكونات والنشر."),
            q("ch5_oo_process_documents", "Understand", "What final activity follows the modeling diagrams?", "ما النشاط الختامي الذي يلي مخططات النمذجة؟", ["Prepare the design documents", "Replace all requirements with source code", "Repeat actor identification after deployment", "Publish the user interface without review"], ["إعداد وثائق التصميم", "استبدال المتطلبات كلها بالشيفرة", "إعادة تحديد الجهات بعد النشر", "نشر واجهة المستخدم بلا مراجعة"], "The process concludes by preparing the design documentation.", "تختتم العملية بإعداد وثائق التصميم."),
        ],
    },
];


def build_question(item, number):
    cid, bloom, stem, stem_ar, options_en, options_ar, explanation, explanation_ar = item
    if len(options_en) != 4 or len(options_ar) != 4:
        raise ValueError(f"{cid}: expected four bilingual options")
    if len(set(options_en)) != 4 or len(set(options_ar)) != 4:
        raise ValueError(f"{cid}: duplicate option text")
    correct_index = (number - 1) % 4

    def rotate(options):
        return list(options[-correct_index:]) + list(options[:-correct_index]) if correct_index else list(options)

    en = rotate(options_en)
    ar = rotate(options_ar)
    return {
        "id": f"q{number}",
        "concept_id": cid,
        "bloom_level": bloom,
        "question": stem,
        "question_ar": stem_ar,
        "options": en.copy(),
        "options_en": en,
        "options_ar": ar,
        "answer": LETTERS[correct_index],
        "correct": correct_index,
        "explanation": explanation,
        "explanation_ar": explanation_ar,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    all_ids = set()
    for bank in BANKS:
        quiz_id = bank["id"]
        out = {
            "schema_version": 2,
            "subject_id": "04_Advanced_Software_Eng",
            "subject_title": "هندسة البرمجيات",
            "semester": 1,
            "semester_label": "كورس أول",
            "instructor_ar": "أ.م.د. علي فاهم نعمة",
            "instructor": "Asst. Prof. Dr. Ali Fahim Ni'ma",
            "subject": "04_Advanced_Software_Eng",
            "quiz_id": quiz_id,
            "topic": bank["title"],
            "topic_ar": bank["title_ar"],
            "questions": [],
        }
        for number, item in enumerate(bank["items"], 1):
            if item[0] in all_ids:
                raise ValueError(f"duplicate concept_id: {item[0]}")
            all_ids.add(item[0])
            out["questions"].append(build_question(item, number))
        path = args.output_dir / f"{quiz_id}.json"
        path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Built {path.name} ({len(out['questions'])} questions)")


if __name__ == "__main__":
    main()
