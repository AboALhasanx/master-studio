#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild the existing ASE Chapter 7 topic banks from course sources.

The seven-bank shape is preserved. This script validates the complete draft
before writing any bank, then replaces only topic metadata and question arrays.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\gokoq\Master-Studio")
OUT = ROOT / "01_Semester_1/04_Advanced_Software_Eng/07_Quizzes_&_Anki"
LETTERS = "ABCD"
META = re.compile(
    r"\bthe lecture|\blecture notes|\bthe notes\b|\bthe booklet\b|\bthe handout\b|"
    r"\baccording to\b|\bthe doctor\b|\bthe syllabus\b|\bthe slides?\b|"
    r"\bthe material\b|\bthe source\b|\bthe text\b|\bthe book\b|\bthe course\b|"
    r"\bthis chapter|\bthe chapter|\bthis section|\bas we saw|\bas covered|\bas discussed|"
    r"المحاضرة|الملزمة|الدكتورة|الشرائح|المصدر|الجابتر|هذا الفصل|هذا القسم", re.I)


def item(cid, bloom, en, ar, enopts, aropts, exp_en, exp_ar):
    return (cid, bloom, en, ar, enopts, aropts, exp_en, exp_ar)


BANKS = [
    {
        "file": "Quiz_Ch07_B01_Basic_Concepts.json",
        "topic": "Reliability Foundations and Operating Environment",
        "topic_ar": "أسس الموثوقية وبيئة التشغيل",
        "key": "ABCDABCDAB",
        "items": [
            item("ch7_reliability_definition", "Understand",
                 "What defines software reliability?",
                 "ما الذي يحدد موثوقية البرمجيات؟",
                 ["Failure-free operation for a stated time and environment.", "Correct output for every input in every possible setting.", "A defect-free codebase after its final inspection.", "A fixed count of successful runs regardless of duration."],
                 ["عمل خالٍ من الإخفاق خلال زمن وبيئة محددين.", "نتائج صحيحة لكل المدخلات وفي جميع البيئات.", "برنامج خالٍ من العيوب بعد الفحص النهائي.", "عدد محدد من التشغيلات الناجحة مهما طال الزمن."],
                 "Reliability is the probability of failure-free operation under stated conditions for a specified period.",
                 "الموثوقية احتمال استمرار العمل بلا إخفاق ضمن ظروف محددة ولمدة معلومة."),
            item("ch7_failure_fault_distinction", "Understand",
                 "How does a fault differ from a failure?",
                 "كيف يختلف العيب عن الإخفاق؟",
                 ["A fault is latent; a failure is observed incorrect operation.", "A failure is latent; a fault is observed incorrect operation.", "A fault is a missing test; a failure is a passed test.", "A fault is a wrong output; a failure is its hidden cause."],
                 ["العيب كامن، والإخفاق انحراف ظاهر عن المتطلبات.", "الإخفاق كامن، والعيب انحراف ظاهر عن المتطلبات.", "العيب حالة اختبار مفقودة، والإخفاق اختبار ناجح.", "العيب مخرج خاطئ، والإخفاق سببه الداخلي."],
                 "A fault is a latent defect; a failure is the program's externally visible departure from requirements.",
                 "العيب نقص كامن في البرنامج، أما الإخفاق فهو انحراف ظاهر عن المتطلبات عند التشغيل."),
            item("ch7_one_fault_many_failures", "Understand",
                 "What can happen when one fault remains in a program?",
                 "ماذا قد يحدث عند بقاء عيب واحد في البرنامج؟",
                 ["Repeated failures whenever its triggering condition recurs.", "One failure total, even when its triggering condition recurs.", "Several failures only if several separate faults exist.", "No failure unless the fault is manually activated."],
                 ["إخفاقات متكررة كلما تكرر شرط تفعيل العيب.", "إخفاق واحد فقط حتى مع تكرر شرط التفعيل.", "إخفاقات متعددة لا تحدث إلا بوجود عيوب متعددة.", "لا يظهر الإخفاق إلا عند تفعيل العيب يدوياً."],
                 "One fault can produce multiple failures when execution repeatedly reaches the condition that activates it.",
                 "قد يسبب العيب الواحد إخفاقات متعددة عند تكرر شرط التشغيل الذي يفعّله."),
            item("ch7_hardware_bathtub", "Understand",
                 "Which pattern describes the hardware bathtub curve?",
                 "أي نمط يصف منحنى حوض الاستحمام للأجهزة؟",
                 ["It falls during burn-in, steadies, then rises with wear.", "It rises during burn-in, steadies, then falls with wear.", "It stays steady during burn-in, then falls as parts age.", "It falls continuously because software faults are removed."],
                 ["تنخفض في الإحماء، تستقر، ثم ترتفع مع الاهتراء.", "ترتفع في الإحماء، تستقر، ثم تنخفض مع الاهتراء.", "تستقر في الإحماء، ثم تنخفض مع تقادم الأجزاء.", "تنخفض باستمرار بسبب إزالة عيوب البرمجيات."],
                 "Hardware failures are initially high during burn-in, lower during useful life, and higher again with wear-out.",
                 "تكون إخفاقات الأجهزة مرتفعة أولاً، ثم تستقر في العمر النافع، ثم ترتفع مع الاهتراء."),
            item("ch7_hardware_software_failure_causes", "Analyze",
                 "Which contrast between software and hardware failures is sound?",
                 "أي مقارنة بين إخفاقات البرمجيات والأجهزة دقيقة؟",
                 ["Software faults are design defects; hardware often suffers physical wear.", "Software mainly suffers physical wear; hardware mainly has design faults.", "Both fail mainly through material aging after devices are manufactured.", "Neither failure pattern depends on its operating conditions."],
                 ["عيوب البرمجيات تصميمية، بينما تتعرض الأجهزة غالباً للاهتراء.", "تهترئ البرمجيات غالباً، بينما تكون عيوب الأجهزة تصميمية.", "يفشل كلاهما غالباً بسبب تقادم المواد بعد التصنيع والتشغيل.", "لا يعتمد أي منهما على ظروف الاستخدام أو بيئة التشغيل."],
                 "Software failures are associated with design faults and their activation; hardware also degrades physically.",
                 "ترتبط إخفاقات البرمجيات بعيوب التصميم وتفعيلها، بينما تتدهور الأجهزة مادياً أيضاً."),
            item("ch7_operational_profile_definition", "Understand",
                 "What does an operational profile describe?",
                 "ماذا يصف Operational Profile؟",
                 ["The expected proportions of the program's different run types.", "The sequence of source files used during software construction.", "The order in which faults are repaired during a test session.", "The hardware parts installed in each deployment environment."],
                 ["النسب المتوقعة لأنواع التشغيل المختلفة للبرنامج.", "ترتيب ملفات البرنامج المستخدمة أثناء بناء النسخة.", "تسلسل إصلاح العيوب خلال جلسة اختبار واحدة.", "الأجزاء المادية المثبتة ضمن بيئة نشر محددة."],
                 "An operational profile assigns probabilities to run types reflecting expected use.",
                 "يحدد Operational Profile احتمالات أنواع التشغيل وفقاً للاستخدام المتوقع."),
            item("ch7_profile_changes_reliability", "Apply",
                 "Why can one program have different reliability under two use profiles?",
                 "لماذا قد تختلف موثوقية البرنامج نفسه باختلاف ملفي الاستخدام؟",
                 ["Profiles weight operations by their different failure chances.", "Each profile rewrites the program's code automatically.", "Reliability ignores which operations users perform in that profile.", "A new use profile removes faults without changing the software."],
                 ["يمنح كل ملف أوزاناً مختلفة لعمليات تختلف فرص إخفاقها.", "يغير كل ملف شفرة البرنامج تلقائياً عند التشغيل.", "يتجاهل مقياس الموثوقية العمليات التي ينفذها المستخدمون.", "يزيل ملف الاستخدام العيوب من دون تعديل البرنامج."],
                 "Changing the probabilities of operations with different conditional failure chances changes the profile-level reliability.",
                 "يتغير تقدير الموثوقية إذا اختلفت أوزان العمليات واختلفت فرص إخفاقها الشرطية."),
            item("ch7_input_space", "Understand",
                 "What is the input space of a program?",
                 "ما المقصود بفضاء مدخلات البرنامج؟",
                 ["The set of possible states of its external input variables.", "The set of output values produced by completed runs.", "The list of faults detected during a reliability study.", "The processor time reserved for the program's execution."],
                 ["مجموعة الحالات الممكنة لمتغيرات الإدخال الخارجية.", "مجموعة قيم الخرج الناتجة عن التشغيلات المكتملة.", "قائمة العيوب المكتشفة خلال دراسة الموثوقية.", "مدة المعالج المخصصة لتنفيذ البرنامج فعلياً."],
                 "An input state is a combination of values for external variables; the input space contains the possible states.",
                 "حالة الإدخال مجموعة قيم للمتغيرات الخارجية، وفضاء الإدخال يضم الحالات الممكنة."),
            item("ch7_functional_environment", "Analyze",
                 "How does the functional environment affect observed failures?",
                 "كيف تؤثر البيئة الوظيفية في الإخفاقات المرصودة؟",
                 ["Different run types can activate different faults in the same program.", "The environment determines how many faults were written in the code.", "Different environments make every fault fail on every execution.", "Run types affect hardware wear but never software failures."],
                 ["تفعّل أنواع التشغيل عيوباً مختلفة في البرنامج نفسه.", "تحدد البيئة عدد العيوب المكتوبة مسبقاً في الشفرة.", "تجعل البيئة كل عيب يفشل مع كل تشغيل للبرنامج.", "تؤثر أنواع التشغيل في عتاد النظام لا في البرنامج."],
                 "The operations and inputs exercised determine which latent faults are encountered.",
                 "تحدد العمليات والمدخلات المنفذة العيوب الكامنة التي يجري الوصول إليها."),
            item("ch7_execution_clock_time", "Understand",
                 "What distinguishes execution time from clock time?",
                 "ما الفرق بين زمن التنفيذ وزمن الساعة؟",
                 ["Execution time is processor work; clock time includes waits within a run.", "Execution time includes shutdowns; clock time excludes all waiting.", "Execution time measures calendar days; clock time counts failures.", "Execution time is user effort; clock time is processor utilization."],
                 ["وقت التنفيذ هو وقت المعالج، والساعة تشمل انتظار التشغيل.", "يشمل زمن التنفيذ الإطفاء، ولا يحسب زمن الساعة أي انتظار.", "يقيس زمن التنفيذ الأيام، بينما يحصي زمن الساعة الإخفاقات.", "زمن التنفيذ جهد المستخدم، وزمن الساعة انشغال المعالج."],
                 "Execution time is time spent by the processor executing the program; clock time also includes waits during a run.",
                 "زمن التنفيذ هو وقت عمل المعالج على البرنامج، أما زمن الساعة فيشمل فترات الانتظار أثناء التشغيل."),
        ],
    },
    {
        "file": "Quiz_Ch07_B02_Software_Quality_Models.json",
        "topic": "Software Quality Models",
        "topic_ar": "نماذج جودة البرمجيات",
        "key": "ABCDABCDABC",
        "items": [
            item("ch7_quality_reliability_difference", "Analyze",
                 "How does software reliability relate to software quality?",
                 "كيف ترتبط موثوقية البرمجيات بجودتها؟",
                 ["Reliability is one quality attribute, not the whole of quality.", "Reliability and quality are identical measures in every model.", "Quality measures failures, while reliability measures source size.", "Reliability is a development process; quality is a test technique."],
                 ["الموثوقية سمة من سمات الجودة وليست الجودة كلها.", "الموثوقية والجودة مقياس واحد في جميع النماذج.", "تقيس الجودة الإخفاقات، وتقيس الموثوقية حجم الشفرة.", "الموثوقية عملية تطوير، والجودة أسلوب اختبار."],
                 "Reliability is a quality characteristic; software quality covers additional attributes as well.",
                 "الموثوقية إحدى خصائص الجودة، وتشمل جودة البرمجيات سمات أخرى أيضاً."),
            item("ch7_mccall_categories", "Understand",
                 "Which groups organize McCall's software quality factors?",
                 "ما المجموعات التي تنظم عوامل الجودة في نموذج McCall؟",
                 ["Product operation, product revision, and product transition.", "Process planning, process control, and process improvement.", "Functionality, reliability, usability, and maintainability.", "Primary uses, intermediate constructs, and primitive constructs."],
                 ["تشغيل المنتج ومراجعته وانتقاله ضمن تصنيف الجودة.", "إدارة العملية وقياسها وتحسينها ضمن نضج المؤسسة.", "الوظيفية والموثوقية وسهولة الاستخدام والصيانة.", "الاستخدامات والبنى المتوسطة والبدائية في نموذج Boehm."],
                 "McCall groups product quality factors under operation, revision, and transition.",
                 "ينظم McCall عوامل جودة المنتج ضمن التشغيل والمراجعة والانتقال."),
            item("ch7_mccall_factor_criteria", "Understand",
                 "What is the relationship between McCall's factors and criteria?",
                 "ما العلاقة بين العوامل والمعايير في نموذج McCall؟",
                 ["Criteria are lower-level attributes that inform quality factors.", "Factors are lower-level attributes that define quality criteria.", "Criteria replace factors when the product enters operation.", "Factors and criteria are interchangeable names for one level."],
                 ["المعايير سمات أدنى مستوى تصف عوامل الجودة.", "العوامل سمات أدنى مستوى تحدد معايير الجودة.", "تحل المعايير محل العوامل عند تشغيل المنتج.", "العوامل والمعايير اسمان متبادلان للمستوى نفسه."],
                 "Quality factors are the higher-level attributes; criteria are the second-level attributes related to them.",
                 "عوامل الجودة سمات المستوى الأعلى، أما المعايير فسمات المستوى الثاني المرتبطة بها."),
            item("ch7_product_operation_reliability", "Apply",
                 "Where does reliability belong in McCall's product-factor groups?",
                 "ضمن أي مجموعة تقع الموثوقية في عوامل McCall؟",
                 ["Product operation, which concerns the product during use.", "Product revision, which concerns testing and maintenance.", "Product transition, which concerns transfer between platforms.", "Process improvement, which concerns organizational maturity."],
                 ["تشغيل المنتج ويضم عوامل أدائه أثناء الاستخدام.", "مراجعة المنتج وتشمل الاختبار والصيانة والتعديل.", "انتقال المنتج ويشمل النقل بين المنصات والأنظمة.", "تحسين العملية يرفع نضج الممارسات المؤسسية."],
                 "Reliability is a product-operation factor alongside attributes such as correctness and usability.",
                 "الموثوقية من عوامل تشغيل المنتج إلى جانب سمات مثل الصحة وسهولة الاستخدام."),
            item("ch7_product_revision_factors", "Understand",
                 "Which concern best fits McCall's product revision group?",
                 "أي اهتمام يلائم مجموعة مراجعة المنتج لدى McCall؟",
                 ["Making software easier to test, maintain, and modify.", "Moving software between platforms and linking systems.", "Helping users operate the software during normal use.", "Measuring maturity across an organization's process levels."],
                 ["تسهيل اختبار البرمجيات وصيانتها وتعديلها.", "نقل البرمجيات بين المنصات وربط الأنظمة.", "مساعدة المستخدمين على تشغيل البرمجيات يومياً.", "قياس نضج العملية عبر مستويات المؤسسة."],
                 "Product revision covers factors related to testing and maintaining the software.",
                 "تشمل مراجعة المنتج العوامل المرتبطة باختبار البرمجيات وصيانتها."),
            item("ch7_product_transition_factors", "Understand",
                 "Which set contains McCall's product transition factors?",
                 "أي مجموعة تضم عوامل انتقال المنتج في نموذج McCall؟",
                 ["Portability, reusability, and interoperability.", "Correctness, efficiency, and integrity.", "Testability, flexibility, and maintainability.", "Suitability, accuracy, and recoverability."],
                 ["قابلية النقل وإعادة الاستخدام والتشغيل البيني.", "الصحة والكفاءة والتكامل ضمن عوامل تشغيل المنتج.", "الاختبار والمرونة والصيانة ضمن مراجعة المنتج.", "الملاءمة والدقة والاستعادة ضمن خصائص المنتج."],
                 "McCall places portability, reusability, and interoperability under product transition.",
                 "يضع McCall قابلية النقل وإعادة الاستخدام والتشغيل البيني ضمن انتقال المنتج."),
            item("ch7_boehm_levels", "Understand",
                 "Which hierarchy describes Boehm's software quality model?",
                 "أي تسلسل يصف هرم نموذج Boehm لجودة البرمجيات؟",
                 ["Primary uses, intermediate constructs, and primitive constructs.", "Product operation, product revision, and product transition.", "Functionality, reliability, usability, and maintainability.", "Initial, repeatable, defined, managed, and optimizing."],
                 ["الاستخدامات الأولية والبنى المتوسطة والبدائية.", "تشغيل المنتج ومراجعته وانتقاله ضمن نموذج McCall.", "خصائص ISO 9126 الست ضمن بنية جودة صارمة.", "مستويات CMM الخمسة من الأولي إلى المحسن."],
                 "Boehm organizes quality through primary uses, intermediate constructs, and primitive constructs.",
                 "ينظم Boehm الجودة عبر الاستخدامات الأولية والبنى المتوسطة والبنى البدائية."),
            item("ch7_boehm_intermediate", "Understand",
                 "What do Boehm's intermediate constructs resemble?",
                 "بماذا تشبه البنى المتوسطة في نموذج Boehm؟",
                 ["McCall's higher-level product quality factors.", "McCall's lower-level product quality criteria.", "CMM's maturity levels for software-process improvement.", "ISO 9001's clauses for quality-system certification."],
                 ["عوامل الجودة الأعلى مستوى في نموذج McCall.", "معايير الجودة الأدنى مستوى في نموذج McCall.", "مستويات النضج في CMM لتحسين العملية.", "بنود ISO 9001 لاعتماد نظام الجودة."],
                 "Boehm's intermediate constructs are similar to McCall's quality factors.",
                 "تشبه البنى المتوسطة لدى Boehm عوامل الجودة في نموذج McCall."),
            item("ch7_iso9126_characteristics", "Understand",
                 "Which set lists ISO 9126's top-level quality characteristics?",
                 "أي مجموعة تسرد خصائص الجودة العليا في ISO 9126؟",
                 ["Functionality, reliability, usability, efficiency, maintainability, portability.", "Correctness, efficiency, integrity, usability, flexibility, reusability.", "Operation, revision, transition, testing, maturity, certification, and process control.", "Suitability, accuracy, security, training, audit, and documented process control."],
                 ["الوظيفية والموثوقية وسهولة الاستخدام والكفاءة والصيانة والنقل.", "الصحة والكفاءة والتكامل وسهولة الاستخدام والمرونة وإعادة الاستخدام.", "التشغيل والمراجعة والانتقال والنضج والاختبار والاعتماد.", "الملاءمة والدقة والأمن والتدريب والتدقيق وضبط العملية."],
                 "ISO 9126 names functionality, reliability, usability, efficiency, maintainability, and portability.",
                 "يسمي ISO 9126 الوظيفية والموثوقية وسهولة الاستخدام والكفاءة والصيانة وقابلية النقل."),
            item("ch7_iso9126_hierarchy", "Analyze",
                 "What structural feature distinguishes the ISO 9126 hierarchy?",
                 "ما السمة البنيوية التي تميز هرم ISO 9126؟",
                 ["Each characteristic is linked to one attribute in a strict hierarchy.", "Every attribute may belong to several unrelated characteristics.", "Quality factors are grouped only by their development cost.", "The model replaces software characteristics with maturity levels."],
                 ["ترتبط كل خاصية بسمة واحدة ضمن تسلسل هرمي صارم.", "قد تنتمي كل سمة إلى خصائص متعددة غير مترابطة.", "تُجمع عوامل الجودة حسب كلفة تطويرها فقط.", "يستبدل النموذج خصائص البرمجيات بمستويات النضج."],
                 "The ISO 9126 hierarchy is strict: each characteristic relates to one attribute.",
                 "هرم ISO 9126 صارم؛ إذ ترتبط كل خاصية بسمة واحدة."),
            item("ch7_iso_user_view", "Analyze",
                 "Whose view do ISO 9126's outer quality characteristics primarily reflect?",
                 "أي منظور تعكسه خصائص الجودة الخارجية في ISO 9126 أساساً؟",
                 ["The user's external view of the software product.", "The compiler's view of the program's internal code.", "The project manager's view of schedule variance.", "The hardware designer's view of component aging."],
                 ["منظور المستخدم إلى الجودة الخارجية للمنتج.", "منظور المترجم إلى البنية الداخلية للبرنامج.", "منظور المدير إلى انحراف جدول المشروع.", "منظور مصمم الأجهزة إلى تقادم المكونات."],
                 "The model's outer attributes describe quality from the user's view rather than an internal developer view.",
                 "تصف السمات الخارجية الجودة من منظور المستخدم لا من منظور المطور الداخلي."),
        ],
    },
    {
        "file": "Quiz_Ch07_B03_CMM_Maturity_Levels.json",
        "topic": "CMM Maturity Levels",
        "topic_ar": "مستويات النضج في CMM",
        "key": "ABCDABCD",
        "items": [
            item("ch7_cmm_staged_sequence", "Understand",
                 "Which sequence gives the CMM maturity levels from lowest to highest?",
                 "أي تسلسل يرتب مستويات نضج CMM من الأدنى إلى الأعلى؟",
                 ["Initial, Repeatable, Defined, Managed, Optimizing.", "Initial, Defined, Repeatable, Managed, Optimizing.", "Repeatable, Initial, Defined, Optimizing, Managed.", "Initial, Repeatable, Managed, Defined, Optimizing."],
                 ["الأولي والمتكرر والمحدد والمدار والمحسن.", "الأولي والمحدد والمتكرر والمدار والمحسن.", "المتكرر والأولي والمحدد والمحسن والمدار.", "الأولي والمتكرر والمدار والمحدد والمحسن."],
                 "The staged path progresses from Initial through Repeatable, Defined, and Managed to Optimizing.",
                 "يتدرج المسار من الأولي إلى المتكرر ثم المحدد والمدار وصولاً إلى المحسن."),
            item("ch7_cmm_process_capability", "Understand",
                 "What does a CMM maturity level characterize?",
                 "ماذا يصف مستوى النضج في CMM؟",
                 ["Software-process maturity and organizational capability.", "The number of defects remaining in one software release.", "The quality of a single program's user interface.", "The percentage of code that passed a specific test suite."],
                 ["قدرة عملية البرمجيات في المؤسسة ونضجها.", "عدد العيوب الباقية في إصدار برمجي واحد.", "جودة واجهة المستخدم لبرنامج منفرد.", "نسبة الشفرة التي اجتازت مجموعة اختبار محددة."],
                 "CMM maturity describes process capability, not the defect count or quality score of one product.",
                 "يصف نضج CMM قدرة العملية، لا عدد عيوب منتج واحد أو درجة جودته."),
            item("ch7_cmm_initial", "Understand",
                 "What best describes an organization at the Initial CMM level?",
                 "ما الوصف الأنسب لمؤسسة عند المستوى الأولي في CMM؟",
                 ["Work is ad hoc; results depend heavily on individuals.", "Projects follow stable plans based on earlier results.", "A standard process is documented across the organization.", "Process performance stays within measured limits."],
                 ["العمل ارتجالي ونتائجه تعتمد غالباً على الأفراد.", "تتبع المشاريع خططاً مستقرة مستندة إلى نتائج سابقة.", "توثق المؤسسة عملية معيارية مشتركة على مستوى المؤسسة.", "يضبط الأداء بحدود كمية تقيس استقرار العملية."],
                 "At the Initial level, the process is unpredictable and often depends on individual effort.",
                 "تكون العملية عند المستوى الأولي غير قابلة للتنبؤ وتعتمد غالباً على جهد الأفراد."),
            item("ch7_cmm_repeatable", "Understand",
                 "What makes the Repeatable CMM level distinct?",
                 "ما الذي يميز المستوى المتكرر في CMM؟",
                 ["Stable project management repeats earlier successful practices.", "One standard process is tailored across organization units.", "Statistical control predicts process performance across projects.", "Continuous improvement prevents recurring known defects."],
                 ["تتكرر ممارسات ناجحة بإدارة مشاريع مستقرة.", "تتكيف المشاريع مع عملية موحدة في المؤسسة.", "يتنبأ الضبط الإحصائي بأداء العملية عبر المشاريع.", "يمنع التحسين المستمر تكرار العيوب المعروفة."],
                 "Repeatable project management lets organizations reproduce earlier successful practices.",
                 "تتيح إدارة المشاريع المستقرة تكرار الممارسات التي أثبتت نجاحها سابقاً."),
            item("ch7_cmm_defined", "Understand",
                 "What process capability is established at the Defined CMM level?",
                 "ما قدرة العملية التي يرسخها المستوى المحدد في CMM؟",
                 ["Each project tailors the documented standard process.", "A project process controlled only by individual managers.", "A quantitative limit for every software defect.", "A continuous improvement program driven by new practices."],
                 ["توثق المؤسسة معياراً للعمل وتكيفه المشاريع.", "يضبط المدير الفرد عملية مشروعه من دون معيار مؤسسي.", "تقاس به جودة العيوب المكتشفة في كل برنامج.", "برنامج تحسين مستمر تقوده ممارسات جديدة."],
                 "The Defined level documents a standard software process across the organization; projects tailor it.",
                 "يوثق المستوى المحدد عملية معيارية للمؤسسة، وتكيفها المشاريع وفق خصائصها."),
            item("ch7_cmm_managed", "Understand",
                 "How does the Managed CMM level control process performance?",
                 "كيف يضبط المستوى المدار في CMM أداء العملية؟",
                 ["It uses quantitative measurement to manage process variation.", "It relies on informal practices that change by individual.", "It defines one process without measuring its performance.", "It focuses only on introducing new software technologies."],
                 ["يستخدم القياس الكمي لإدارة تباين العملية.", "يعتمد ممارسات غير رسمية تتغير باختلاف الأفراد.", "يحدد عملية واحدة من دون قياس أدائها.", "يركز فقط على إدخال تقنيات برمجية جديدة."],
                 "At the Managed level, process and product quality are measured and variation is controlled quantitatively.",
                 "يُقاس أداء العملية وجودة المنتج كمياً عند المستوى المدار ويُضبط التباين."),
            item("ch7_cmm_optimizing", "Understand",
                 "What is the central aim of the Optimizing CMM level?",
                 "ما الهدف المحوري للمستوى المحسن في CMM؟",
                 ["Continuous improvement prevents recurring defects in software.", "Stable project tracking using previously successful practices.", "Organization-wide process documentation for engineering and management.", "Quantitative control of variation within established limits."],
                 ["التحسين المستمر للعملية ومنع تكرار العيوب.", "متابعة مستقرة للمشاريع بممارسات ناجحة سابقة.", "توثيق عملية هندسية وإدارية معيارية للمؤسسة.", "ضبط كمي لتباين الأداء ضمن حدود معتمدة."],
                 "The Optimizing level proactively strengthens the process and seeks to prevent known defects.",
                 "يعزز المستوى المحسن العملية استباقياً ويسعى لمنع العيوب المعروفة."),
            item("ch7_defined_vs_managed", "Analyze",
                 "Which distinction separates Defined from Managed maturity?",
                 "أي فرق يفصل بين النضج المحدد والنضج المدار؟",
                 ["Defined standardizes the process; Managed controls measured variation.", "Defined prevents all defects; Managed begins project planning.", "Defined certifies products; Managed replaces software processes.", "Defined measures hardware wear; Managed measures user satisfaction."],
                 ["يوحد المحدد العملية، بينما يقيس المدار تباينها كمياً.", "يمنع المحدد كل العيوب، بينما يبدأ المدار تخطيط المشروع.", "يعتمد المحدد المنتجات، بينما يستبدل المدار عمليات البرمجيات.", "يقيس المحدد اهتراء الأجهزة، بينما يقيس المدار رضا المستخدم."],
                 "Defined establishes a standard process; Managed adds quantitative measurement and control.",
                 "يرسخ المستوى المحدد عملية معيارية، ويضيف المدار القياس والضبط الكميين."),
        ],
    },
    {
        "file": "Quiz_Ch07_B04_CMM_Process_Areas.json",
        "topic": "CMM Key Process Areas and Common Features",
        "topic_ar": "مناطق العملية والخصائص المشتركة في CMM",
        "key": "ABCDABCD",
        "items": [
            item("ch7_kpa_meaning", "Understand",
                 "What does KPA mean in the CMM?",
                 "ماذا يعني KPA في CMM؟",
                 ["Key Process Area, a group of related process practices.", "Key Product Attribute, a software quality characteristic.", "Known Performance Average, a reliability measurement.", "Kernel Program Activity, a software execution phase."],
                 ["منطقة رئيسية تضم ممارسات عملية مترابطة.", "سمة رئيسية تصف جودة منتج برمجي محدد.", "متوسط شائع لقياس موثوقية المنتج البرمجي.", "نشاط برمجي يحدد مرحلة من مراحل التطوير."],
                 "A Key Process Area groups related goals and practices important to process capability at a maturity level.",
                 "تجمع منطقة العملية الأساسية أهدافاً وممارسات مترابطة لازمة لقدرة العملية في مستوى نضج معين."),
            item("ch7_kpa_level_structure", "Analyze",
                 "How are Key Process Areas organized in staged CMM?",
                 "كيف تُنظم مناطق العملية الأساسية في CMM المرحلي؟",
                 ["Higher CMM maturity levels introduce their own KPAs.", "Every KPA belongs to all maturity levels at the same time.", "KPAs replace maturity levels in the staged model.", "The Initial level contains all KPAs before any process work."],
                 ["تظهر KPAs في المستويات الأعلى بعد المستوى الأولي.", "تنتمي كل منطقة عملية إلى جميع مستويات النضج معاً.", "تحل مناطق العملية محل مستويات النضج في النموذج المرحلي.", "يضم المستوى الأولي كل المناطق قبل بدء العمل."],
                 "The Initial level has no defined KPAs; the staged areas are introduced at higher levels.",
                 "لا يضم المستوى الأولي مناطق محددة، وتظهر مناطق العملية في المستويات الأعلى."),
            item("ch7_common_features_list", "Understand",
                 "Which set names CMM's common features for institutionalizing a KPA?",
                 "أي مجموعة تسمي الخصائص المشتركة لترسيخ KPA في CMM؟",
                 ["Commitment, ability, activities, measurement, and verification.", "Planning, coding, compiling, testing, and deployment.", "Operation, revision, transition, maturity, and certification.", "Reliability, usability, portability, efficiency, and integrity."],
                 ["الالتزام والقدرة والأنشطة والقياس والتحقق.", "التخطيط والبرمجة والترجمة والاختبار والنشر.", "التشغيل والمراجعة والانتقال والنضج والاعتماد.", "الموثوقية وسهولة الاستخدام والنقل والكفاءة والتكامل."],
                 "The five common features are Commitment to Perform, Ability to Perform, Activities Performed, Measurement and Analysis, and Verifying Implementation.",
                 "الخصائص الخمس هي الالتزام بالأداء والقدرة عليه والأنشطة المنفذة والقياس والتحليل والتحقق من التنفيذ."),
            item("ch7_ability_perform_scenario", "Apply",
                 "A process area lacks trained staff, tools, and a clear role structure; which feature is weak?",
                 "تفتقر منطقة عملية إلى موظفين مدربين وأدوات وأدوار واضحة؛ أي خاصية ضعيفة؟",
                 ["Ability to Perform, which provides necessary resources and skills.", "Verifying Implementation, which reviews adherence to procedures.", "Measurement and Analysis, which evaluates process data.", "Commitment to Perform, which establishes management policy."],
                 ["توفر القدرة على الأداء موارد الفريق وتدريبه.", "يراجع التحقق من التنفيذ اتباع إجراءات العمل.", "يحلل القياس بيانات أداء العملية وأهدافها.", "يحدد الالتزام بالأداء سياسة الإدارة ودعمها."],
                 "Ability to Perform covers prerequisites such as resources, organizational structure, training, and tools.",
                 "تشمل القدرة على الأداء الموارد والبنية التنظيمية والتدريب والأدوات اللازمة."),
            item("ch7_verification_scenario", "Apply",
                 "A team audits whether an established process is followed; which feature is applied?",
                 "يدقق فريق في الالتزام بعملية مقررة؛ أي خاصية يطبق؟",
                 ["Verifying Implementation checks adherence to the process.", "Activities Performed defines plans and required work products.", "Ability to Perform supplies staff, tools, and training.", "Commitment to Perform sets policy and management support."],
                 ["التحقق من التنفيذ يراجع الالتزام بإجراءات العمل.", "تحدد الأنشطة المنفذة الخطط ومخرجات العمل المطلوبة.", "توفر القدرة على الأداء الموظفين والموارد والتدريب.", "يحدد الالتزام بالأداء سياسة الإدارة والدعم المطلوب."],
                 "Verifying Implementation uses reviews and audits to ensure that activities follow established procedures.",
                 "يستخدم التحقق من التنفيذ المراجعات والتدقيق لضمان اتباع الإجراءات المقررة."),
            item("ch7_kpa_vs_common_feature", "Analyze",
                 "How do a KPA and a common feature differ?",
                 "كيف تختلف KPA عن الخاصية المشتركة؟",
                 ["A KPA names an area; common features institutionalize it.", "A KPA names a quality factor; common features measure defects.", "A KPA describes a maturity stage; common features replace stages.", "A KPA measures a product; common features specify user inputs."],
                 ["تسمي KPA منطقة عملية، وتنظم الخصائص المشتركة ترسيخها.", "تسمي KPA عامل جودة، وتقيس الخصائص المشتركة العيوب.", "تصف KPA مرحلة نضج، وتحل الخصائص المشتركة محل المراحل.", "تقيس KPA منتجاً، وتحدد الخصائص المشتركة مدخلات المستخدم."],
                 "A KPA identifies the process area; common features describe how practices in that area are institutionalized.",
                 "تحدد KPA مجال العملية، وتصف الخصائص المشتركة كيفية ترسيخ ممارساته."),
            item("ch7_common_features_scope", "Understand",
                 "What remains shared when the subject of a CMM KPA changes?",
                 "ما الذي يبقى مشتركاً عند تغير موضوع KPA في CMM؟",
                 ["Common features span distinct software process areas.", "Each area retains its own specific goals and practices.", "Each area measures attributes of a software product.", "Organizations receive one common maturity level."],
                 ["تتكرر الفئات المشتركة عبر مناطق العملية.", "تحتفظ كل منطقة بأهداف وممارسات خاصة بها.", "تقيس كل منطقة سمات منتج برمجي محدد.", "تحصل المؤسسات على مستوى نضج موحد."],
                 "The KPA content varies, while the same common-feature categories organize its implementation.",
                 "يختلف محتوى مناطق العملية، بينما تنظم الفئات المشتركة طريقة تنفيذها."),
            item("ch7_process_area_institutionalization", "Analyze",
                 "What indicates that a KPA is institutionalized rather than used temporarily?",
                 "ما الذي يدل على ترسيخ KPA بدلاً من تطبيقها مؤقتاً؟",
                 ["Its practices are lasting and repeatable over time.", "Its practices are performed once by a project expert.", "Its goals are replaced whenever a product is released.", "Its procedures are kept informal and undocumented."],
                 ["تبقى ممارساتها قائمة وقابلة للتكرار.", "ينفذ خبير المشروع ممارساتها مرة واحدة فقط.", "تُستبدل أهدافها عند كل إصدار للمنتج.", "تبقى إجراءاتها غير رسمية وغير موثقة."],
                 "Institutionalization makes KPA practices enduring and repeatable rather than dependent on one temporary effort.",
                 "يجعل الترسيخ ممارسات المنطقة مستمرة وقابلة للتكرار بدلاً من اعتمادها على جهد مؤقت."),
        ],
    },
    {
        "file": "Quiz_Ch07_B05_Reliability_Measures.json",
        "topic": "Reliability Measures and Failure Behavior",
        "topic_ar": "مقاييس الموثوقية وسلوك الإخفاق",
        "key": "ABCDABCDABC",
        "items": [
            item("ch7_reliability_vs_intensity", "Analyze",
                 "How does reliability differ from failure intensity?",
                 "كيف تختلف الموثوقية عن شدة الإخفاق؟",
                 ["Reliability is a failure-free probability; intensity is a failure rate.", "Reliability is a failure rate; intensity is a failure-free probability.", "Reliability counts latent faults; intensity counts source lines.", "Reliability is a process level; intensity is a quality attribute."],
                 ["الموثوقية احتمال خلو الزمن، والشدة معدل الإخفاق.", "الموثوقية معدل الإخفاق، والشدة احتمال خلو الزمن.", "تحصي الموثوقية العيوب، وتقيس الشدة حجم الشفرة.", "الموثوقية صفة جودة، والشدة معدل وقوع الإخفاق."],
                 "Reliability is a probability over a specified interval; failure intensity is an instantaneous rate per unit time.",
                 "الموثوقية احتمال خلال مدة محددة، أما شدة الإخفاق فمعدل لحظي لكل وحدة زمن."),
            item("ch7_mean_value_function", "Understand",
                 "What does the mean value function represent in a reliability model?",
                 "ماذا تمثل دالة القيمة المتوسطة في نموذج الموثوقية؟",
                 ["The expected cumulative failures by a given point in time.", "The instantaneous chance of a failure at one input state.", "The average processor utilization during a calendar month.", "The fixed number of faults remaining after final release."],
                 ["العدد التراكمي المتوقع للإخفاقات حتى زمن معين.", "الاحتمال اللحظي للإخفاق عند حالة إدخال واحدة.", "متوسط انشغال المعالج خلال شهر تقويمي.", "العدد الثابت للعيوب الباقية بعد الإصدار النهائي."],
                 "The mean value function gives the expected cumulative number of failures up to a time point.",
                 "تعطي دالة القيمة المتوسطة العدد التراكمي المتوقع للإخفاقات حتى نقطة زمنية معينة."),
            item("ch7_mttf_meaning", "Understand",
                 "Before the first observed failure, what duration does MTTF summarize?",
                 "قبل أول إخفاق مرصود، أي مدة يلخصها MTTF؟",
                 ["The average operating time until a failure occurs.", "The average time separating successive failures.", "The number of failures observed in a time interval.", "The cumulative count of failures at a chosen time."],
                 ["متوسط زمن التشغيل المتوقع حتى حدوث إخفاق.", "متوسط الزمن الفاصل بين إخفاقين متتاليين.", "عدد الإخفاقات المرصودة ضمن فترة زمنية.", "العدد التراكمي للإخفاقات عند زمن مختار."],
                 "Mean Time to Failure is the average operating time before a failure occurs.",
                 "متوسط الزمن حتى الإخفاق هو متوسط زمن التشغيل السابق لوقوع إخفاق."),
            item("ch7_mtbf_meaning", "Understand",
                 "When failures recur during operation, what interval does MTBF summarize?",
                 "عند تكرر الإخفاقات أثناء التشغيل، أي فاصل يلخصه MTBF؟",
                 ["The average time separating successive failures.", "The average operating time until the first failure.", "The failure rate during a single execution interval.", "The expected total failures over the product lifetime."],
                 ["متوسط الزمن الفاصل بين إخفاقات متعاقبة.", "متوسط زمن التشغيل حتى الإخفاق الأول.", "معدل الإخفاق خلال فترة تنفيذ واحدة.", "إجمالي الإخفاقات المتوقع طوال عمر المنتج."],
                 "Mean Time Between Failures measures the average interval between successive failures.",
                 "يقيس متوسط الزمن بين الإخفاقات متوسط الفاصل بين إخفاقات متتالية."),
            item("ch7_failure_time_representations", "Understand",
                 "Which set represents the four common time-based views of failures?",
                 "أي مجموعة تمثل الصور الزمنية الأربع الشائعة للإخفاقات؟",
                 ["Event time, inter-event time, cumulative and interval counts.", "Input state, output state, run type, operational profile.", "Execution time, clock time, calendar time, machine time.", "Fault count, program size, test cases, processor usage."],
                 ["زمن الحدث والفاصل بين الأحداث والعدد التراكمي وعدد الفترة.", "حالة الإدخال وحالة الخرج ونوع التشغيل وملف التشغيل.", "زمن التنفيذ وزمن الساعة والزمن التقويمي وزمن الآلة.", "عدد العيوب وحجم الشفرة وحالات الاختبار واستخدام المعالج."],
                 "Failures may be represented by their times, intervals, cumulative count, or count within an interval.",
                 "يمكن تمثيل الإخفاقات بأزمنتها أو فواصلها أو عددها التراكمي أو عددها ضمن فترة."),
            item("ch7_failure_intensity_units", "Understand",
                 "What does a failure-intensity value express?",
                 "ماذا تعبّر عنه قيمة شدة الإخفاق؟",
                 ["A rate of failures per unit of the specified time.", "A probability that ignores the observation period.", "A total fault count independent of program execution.", "A percentage of source code inspected by reviewers."],
                 ["معدل إخفاقات لكل وحدة زمن محددة.", "احتمال لا يرتبط بمدة رصد محددة.", "عدد العيوب بصرف النظر عن تنفيذ البرنامج.", "نسبة الشفرة التي فُحصت بالمراجعة."],
                 "Failure intensity is expressed as a rate, such as failures per hour of execution time.",
                 "تُعبّر شدة الإخفاق عن معدل، مثل عدد الإخفاقات لكل ساعة تنفيذ."),
            item("ch7_reliability_range", "Understand",
                 "Which range is valid for a reliability probability?",
                 "أي مدى يصح لاحتمال الموثوقية؟",
                 ["From zero to one, including both endpoints.", "From zero to one hundred, excluding zero.", "Any positive value with no upper bound.", "Only values greater than one during testing."],
                 ["قيمة من الصفر حتى الواحد مع شمول الحدين.", "قيمة بين الصفر والمئة من دون شمول الصفر.", "أي قيمة موجبة ولو تجاوزت الواحد كثيراً.", "قيمة أكبر من الواحد خلال الاختبار فقط."],
                 "Reliability is a probability, so it lies between zero and one inclusive.",
                 "الموثوقية احتمال، لذا تقع بين الصفر والواحد مع شمول الحدين."),
            item("ch7_reliability_intensity_trend", "Analyze",
                 "During fault removal, which trend commonly links reliability and intensity?",
                 "أثناء إزالة العيوب، ما العلاقة الشائعة بين الموثوقية والشدة؟",
                 ["Reliability rises as failure intensity falls.", "Reliability falls as failure intensity falls.", "Both measures stay fixed after the first test.", "Both measures rise whenever a fault is removed."],
                 ["ترتفع الموثوقية حين تنخفض شدة الإخفاق.", "تنخفض الموثوقية حين تنخفض شدة الإخفاق.", "يبقى المقياسان ثابتين بعد الاختبار الأول.", "ترتفع الموثوقية والشدة عند إزالة عيب."],
                 "As testing removes faults, reliability commonly increases while the failure intensity decreases.",
                 "تزداد الموثوقية عادة مع إزالة العيوب، بينما تنخفض شدة الإخفاق."),
            item("ch7_intensity_release_objective", "Apply",
                 "A release decision focuses on the instantaneous risk of failure; which measure fits best?",
                 "يركز قرار الإصدار على خطر الإخفاق اللحظي؛ أي مقياس يلائمه؟",
                 ["Failure intensity, a rate describing risk at a given time.", "Reliability, an average defect count during operation.", "Mean time to failure, which counts input states exercised.", "Input space, which measures failure chance per time."],
                 ["شدة الإخفاق لأنها معدل خطر عند زمن محدد.", "الموثوقية لأنها متوسط لعدد العيوب في المنتج.", "متوسط الزمن حتى الإخفاق لأنه يحصي حالات الإدخال.", "فضاء الإدخال لأنه يقيس معدل الخطر لكل زمن."],
                 "Failure intensity is suited to a release objective stated as a risk rate at a point in testing.",
                 "تلائم شدة الإخفاق هدف الإصدار المعبر عنه بمعدل الخطر عند نقطة من الاختبار."),
            item("ch7_reliability_component_combination", "Understand",
                 "Which measure is suited to combining component reliability values?",
                 "أي مقياس يلائم جمع قيم موثوقية المكونات؟",
                 ["Reliability is a probability under stated conditions.", "Failure intensity is a time-based failure rate.", "Mean value is the expected cumulative failure count.", "Calendar time is elapsed duration for testing staff."],
                 ["الموثوقية احتمال في ظروف تشغيل محددة.", "شدة الإخفاق معدل مرتبط بوحدة الزمن.", "القيمة المتوسطة عدد الإخفاقات المتوقع.", "الزمن التقويمي مدة العمل والموارد."],
                 "Reliability is a probability measure that can be combined for system components using reliability theory.",
                 "الموثوقية مقياس احتمالي يمكن دمجه لمكونات النظام وفق نظرية الموثوقية."),
            item("ch7_reliability_study_use", "Apply",
                 "How can reliability studies help project management during testing?",
                 "كيف تساعد دراسات الموثوقية إدارة المشروع أثناء الاختبار؟",
                 ["They guide release timing, schedule, and cost during testing.", "They estimate program size without observing test failures.", "They replace project plans with counts of user requests.", "They guarantee that deployed software contains no faults."],
                 ["تتابع تقدم الاختبار وتدعم قرارات الإصدار والكلفة.", "تقدر حجم البرنامج من دون رصد إخفاقات الاختبار.", "تستبدل خطة المشروع بإحصاء طلبات المستخدمين.", "تضمن خلو البرنامج المنشور من العيوب البرمجية."],
                 "Reliability measures help monitor test progress and relate release decisions to schedule and cost.",
                 "تساعد مقاييس الموثوقية على متابعة الاختبار وربط قرارات الإصدار بالجدول والكلفة."),
        ],
    },
    {
        "file": "Quiz_Ch07_B06_Execution_Time_Models.json",
        "topic": "Reliability Growth Models and Time Components",
        "topic_ar": "نماذج نمو الموثوقية ومكونات الزمن",
        "key": "ABCDABCDABCDABC",
        "items": [
            item("ch7_nhpp_meaning", "Understand",
                 "What does NHPP mean in software reliability modeling?",
                 "ماذا يعني NHPP في نمذجة موثوقية البرمجيات؟",
                 ["Nonhomogeneous Poisson Process model.", "Nonlinear Hardware Performance Profile.", "Normalized Hazard Probability Pattern.", "Nonparametric Human Process Prediction."],
                 ["عملية بواسون غير المتجانسة.", "ملف أداء الأجهزة غير الخطي.", "نمط احتمال الخطر المعياري.", "تنبؤ العملية البشرية اللامعلمي."],
                 "NHPP stands for Nonhomogeneous Poisson Process, whose failure intensity can change over time.",
                 "يشير NHPP إلى عملية بواسون غير متجانسة يمكن أن تتغير شدة إخفاقها مع الزمن."),
            item("ch7_basic_intensity_shape", "Understand",
                 "How does the Basic Execution Time Model relate intensity to failures experienced?",
                 "كيف يربط نموذج زمن التنفيذ الأساسي الشدة بالإخفاقات المرصودة؟",
                 ["Intensity decreases linearly as failures are experienced.", "Intensity decreases exponentially as time passes.", "Intensity stays constant until all faults are removed.", "Intensity rises linearly as failures are experienced."],
                 ["تنخفض الشدة خطياً مع الإخفاقات المرصودة.", "تنخفض الشدة أُسّياً مع مرور الزمن.", "تبقى الشدة ثابتة حتى إزالة جميع العيوب.", "ترتفع الشدة خطياً مع الإخفاقات المرصودة."],
                 "The basic model assumes a linear decrease in failure intensity as the expected failures experienced grow.",
                 "يفترض النموذج الأساسي انخفاضاً خطياً في الشدة مع زيادة الإخفاقات المتوقعة المرصودة."),
            item("ch7_basic_finite_population", "Understand",
                 "What does the Basic Execution Time Model assume about eventual failures?",
                 "ماذا يفترض نموذج زمن التنفيذ الأساسي بشأن الإخفاقات النهائية؟",
                 ["A finite expected failure population bounds the cumulative mean.", "The cumulative failure mean grows without any finite bound.", "Failure intensity is independent of failures already experienced.", "Every input state produces the same number of failures."],
                 ["يقترب العدد التراكمي المتوقع من حد نهائي.", "ينمو متوسط الإخفاقات التراكمي بلا حد نهائي.", "لا تعتمد الشدة على الإخفاقات المرصودة سابقاً.", "تنتج كل حالة إدخال العدد نفسه من الإخفاقات."],
                 "The basic model has a finite eventual failure population, so its cumulative mean approaches that limit.",
                 "يفترض النموذج الأساسي عدداً نهائياً متوقعاً من الإخفاقات ويقترب المتوسط التراكمي منه."),
            item("ch7_basic_uniform_profile", "Analyze",
                 "Which operational-profile assumption accompanies the Basic Execution Time Model?",
                 "أي افتراض لملف التشغيل يصاحب نموذج زمن التنفيذ الأساسي؟",
                 ["A uniform profile gives faults equal chances to manifest.", "Run types have arbitrary probabilities that never affect failures.", "Only the most common input state can activate a fault.", "Fault removal occurs without any observed failure."],
                 ["يمنح الملف الموحد كل عيب فرصة متساوية للظهور.", "تعطي أنواع التشغيل احتمالات لا تؤثر في الإخفاقات.", "تفعّل حالة الإدخال الأشيع وحدها جميع العيوب.", "تزيل الاختبارات العيوب من دون رصد أي إخفاق."],
                 "The basic model implies a uniform operational profile, giving faults equal chances to manifest.",
                 "يفترض النموذج الأساسي ملف تشغيل موحداً يمنح العيوب فرصاً متساوية للظهور."),
            item("ch7_basic_decrement", "Understand",
                 "What happens to failure intensity per additional failure in the Basic model?",
                 "ماذا يحدث لشدة الإخفاق مع كل إخفاق إضافي في النموذج الأساسي؟",
                 ["It drops by a constant amount under the model assumptions.", "It drops by an amount that grows exponentially each time.", "It remains unchanged until the final fault is removed.", "It increases by the same amount after each failure."],
                 ["تنخفض بمقدار ثابت وفق افتراضات النموذج.", "تنخفض بمقدار يزداد أُسّياً في كل مرة.", "تبقى بلا تغير حتى إزالة العيب الأخير.", "ترتفع بالمقدار نفسه بعد كل إخفاق."],
                 "A constant decrement in intensity per failure follows from the basic model's linear intensity relation.",
                 "ينتج الانخفاض الثابت للشدة لكل إخفاق عن العلاقة الخطية في النموذج الأساسي."),
            item("ch7_log_intensity_shape", "Understand",
                 "How does the Logarithmic Poisson Model describe intensity as failures accumulate?",
                 "كيف يصف نموذج بواسون اللوغاريتمي الشدة مع تراكم الإخفاقات؟",
                 ["Intensity declines exponentially as failures accumulate.", "Intensity declines linearly with calendar time observed.", "Intensity stays fixed while the expected failure count grows.", "Intensity rises exponentially after each fault is corrected."],
                 ["تتناقص الشدة أُسّياً مع الإخفاقات.", "تنخفض الشدة خطياً مع الأيام المقاسة.", "تبقى الشدة ثابتة مع نمو متوسط الإخفاقات.", "ترتفع الشدة أُسّياً عند إصلاح العيب."],
                 "In the logarithmic Poisson model, failure intensity decays exponentially as failures are experienced.",
                 "تتناقص شدة الإخفاق أُسّياً مع الإخفاقات المرصودة في نموذج بواسون اللوغاريتمي."),
            item("ch7_log_theta_meaning", "Understand",
                 "What role does theta play in the Logarithmic Poisson Model?",
                 "ما دور theta في نموذج بواسون اللوغاريتمي؟",
                 ["It controls how quickly intensity decays per failure.", "It gives the finite total number of eventual failures.", "It measures the calendar time lost to staff shortages.", "It counts the faults remaining after each test run."],
                 ["يحدد معامل theta سرعة تناقص الشدة لكل إخفاق مرصود.", "يعطي معامل theta عدداً ثابتاً للإخفاقات النهائية.", "يقيس معامل theta وقت الاختبار المفقود بسبب نقص الموظفين.", "يحصي معامل theta العيوب الباقية بعد كل تشغيل اختباري."],
                 "Theta is the failure-intensity decay parameter in the logarithmic Poisson model.",
                 "تمثل theta معامل تناقص شدة الإخفاق في نموذج بواسون اللوغاريتمي."),
            item("ch7_log_unbounded_mean", "Understand",
                 "What long-run behavior does the Logarithmic Poisson Model allow for cumulative failures?",
                 "أي سلوك بعيد المدى يسمح به نموذج بواسون اللوغاريتمي للإخفاقات التراكمية؟",
                 ["The cumulative mean has no finite upper asymptote.", "The cumulative mean stops at a fixed finite population.", "The mean falls whenever one more failure is observed.", "The cumulative mean stays equal to the initial intensity."],
                 ["لا يملك المتوسط التراكمي حداً أعلى نهائياً.", "يتوقف المتوسط التراكمي عند عدد ثابت ومحدود.", "ينخفض المتوسط كلما رُصد إخفاق إضافي.", "يبقى المتوسط التراكمي مساوياً للشدة الأولية."],
                 "The logarithmic Poisson form has an unbounded cumulative mean, unlike a finite-population assumption.",
                 "يملك نموذج بواسون اللوغاريتمي متوسطاً تراكمياً غير محدود بخلاف افتراض المجتمع المحدود."),
            item("ch7_model_shape_selection", "Analyze",
                 "Observed intensity falls roughly linearly with failures; which model form matches that pattern?",
                 "تنخفض الشدة المرصودة خطياً تقريباً مع الإخفاقات؛ أي نموذج يلائم النمط؟",
                 ["The Basic Execution Time Model.", "The Logarithmic Poisson Model.", "The Jelinski–Moranda Model only.", "The Calendar Time Component Model only."],
                 ["نموذج زمن التنفيذ الأساسي.", "نموذج بواسون اللوغاريتمي.", "نموذج Jelinski–Moranda وحده.", "نموذج مكون الزمن التقويمي وحده."],
                 "The basic model expresses a linear intensity decrease as failures are experienced.",
                 "يعبر النموذج الأساسي عن انخفاض خطي للشدة مع الإخفاقات المرصودة."),
            item("ch7_calendar_execution_relation", "Understand",
                 "What mediates the relationship between execution time and calendar time?",
                 "ما الذي يتوسط العلاقة بين زمن التنفيذ والزمن التقويمي؟",
                 ["Testing effort links execution time to calendar duration.", "The product model's quality-factor count sets elapsed time.", "The team's maturity level determines testing duration.", "The number of input states fixes the time required."],
                 ["جهد الاختبار يربط زمن التنفيذ بمدة التقويم.", "عدد عوامل الجودة يحدد مدة تنفيذ الاختبار.", "مرحلة نضج الفريق تحدد مدة الاختبار المطلوبة.", "عدد حالات الإدخال يحدد زمن الاختبار الكلي."],
                 "Calendar-time progress depends on testing resources and the effort required as execution proceeds.",
                 "يعتمد التقدم بالزمن التقويمي على موارد الاختبار والجهد اللازم مع تقدم التنفيذ."),
            item("ch7_calendar_resource_limits", "Apply",
                 "Testing needs more calendar time despite adequate CPU capacity; what may explain the delay?",
                 "يحتاج الاختبار زمناً تقويمياً أطول رغم كفاية المعالج؛ ما سبب التأخير المحتمل؟",
                 ["Personnel or other testing resources limit progress.", "The processor has stopped measuring execution time.", "The operational profile contains fewer possible inputs.", "The software has reached a higher CMM maturity level."],
                 ["تحد قلة الموظفين أو الموارد تقدم الاختبار.", "يتوقف المعالج عن احتساب زمن تنفيذ البرنامج.", "يضم ملف التشغيل حالات إدخال أقل من المعتاد.", "وصل فريق البرمجيات إلى مستوى أعلى في CMM."],
                 "The calendar-time component accounts for resource limitations, including testing personnel.",
                 "يأخذ مكون الزمن التقويمي قيود الموارد بالحسبان، ومنها موظفو الاختبار."),
            item("ch7_jm_remaining_faults", "Understand",
                 "How does Jelinski–Moranda relate failure intensity to remaining faults?",
                 "كيف يربط Jelinski–Moranda شدة الإخفاق بالعيوب الباقية؟",
                 ["Intensity depends on the estimated faults still remaining.", "Intensity is proportional to the calendar time already elapsed.", "Intensity is independent of the faults removed so far.", "Intensity equals the number of input states exercised."],
                 ["تتناسب الشدة مع عدد العيوب المقدّر بقاؤها.", "تتناسب الشدة مع الزمن التقويمي المنقضي.", "لا تعتمد الشدة على العيوب التي أزيلت.", "تساوي الشدة عدد حالات الإدخال المنفذة."],
                 "The Jelinski–Moranda intensity depends on the estimated number of faults not yet removed.",
                 "تعتمد شدة Jelinski–Moranda على العدد المقدّر للعيوب التي لم تُزل بعد."),
            item("ch7_jm_step_change", "Analyze",
                 "Why does Jelinski–Moranda intensity change after a fault-caused failure is removed?",
                 "لماذا تتغير شدة Jelinski–Moranda بعد إزالة عيب تسبب بإخفاق؟",
                 ["The estimated remaining fault count decreases by one.", "The operational profile becomes uniform automatically.", "Calendar time is replaced by processor time.", "The model's total fault population increases."],
                 ["ينخفض عدد العيوب الباقية واحداً.", "يصبح ملف التشغيل موحداً تلقائياً.", "يحل زمن المعالج محل الزمن التقويمي.", "يزداد مجتمع العيوب الكلي في النموذج."],
                 "Removing a fault reduces the remaining-fault term that determines the next interval's intensity.",
                 "تقلل إزالة العيب حد العيوب الباقية الذي يحدد شدة الفترة التالية."),
            item("ch7_bug_seeding_estimate", "Understand",
                 "How does bug seeding estimate the indigenous fault population?",
                 "كيف يقدّر نموذج بذر الأخطاء مجتمع العيوب الأصلية؟",
                 ["It compares detected seeded and indigenous faults.", "It counts discovered faults without labeling seeded ones.", "It compares run time before and after each code change.", "It imports a hardware component's failure rate."],
                 ["يقارن العيوب المزروعة والأصلية المكتشفة.", "يحصي العيوب المكتشفة دون تمييز المزروع منها.", "يقارن زمن التنفيذ قبل تغيير الشفرة وبعده.", "يستخدم معدل إخفاق مكوّن من أجهزة أخرى."],
                 "Bug seeding uses the detected seeded-to-indigenous ratio to estimate faults that remain undiscovered.",
                 "يستخدم بذر الأخطاء نسبة العيوب المزروعة إلى الأصلية المكتشفة لتقدير العيوب غير المكتشفة."),
            item("ch7_bug_seeding_assumption", "Analyze",
                 "Which assumption is needed for bug-seeding estimates to be credible?",
                 "أي افتراض يلزم لمصداقية تقدير نموذج بذر الأخطاء؟",
                 ["Seeded and indigenous faults have comparable chances of detection.", "Seeded faults are always easier to detect than indigenous faults.", "Every indigenous fault causes exactly one observed failure.", "Testers know the location of every hidden fault in advance."],
                 ["تتقارب فرص اكتشاف العيوب المزروعة والأصلية.", "يسهل دائماً اكتشاف العيوب المزروعة أكثر من الأصلية.", "يسبب كل عيب أصلي إخفاقاً مرصوداً واحداً بالضبط.", "يعرف المختبرون مسبقاً مواقع جميع العيوب الخفية."],
                 "The estimate relies on comparable detection probabilities for seeded and indigenous faults.",
                 "يعتمد التقدير على تقارب احتمالات اكتشاف العيوب المزروعة والأصلية."),
        ],
    },
    {
        "file": "Quiz_Ch07_B07_ISO_9000.json",
        "topic": "ISO 9000 and CMM Comparison",
        "topic_ar": "مقارنة ISO 9000 وCMM",
        "key": "ABCDABCDABC",
        "items": [
            item("ch7_iso9000_family", "Understand",
                 "What is the ISO 9000 series primarily concerned with?",
                 "بماذا تعنى سلسلة ISO 9000 أساساً؟",
                 ["Quality-management and quality-assurance standards.", "A staged model of software process maturity.", "A family of software product reliability models.", "A collection of input profiles for software testing."],
                 ["معايير مترابطة لإدارة الجودة وضمانها.", "نموذج مرحلي لنضج عمليات تطوير البرمجيات.", "مجموعة نماذج لموثوقية المنتجات البرمجية.", "مجموعة ملفات لتمثيل مدخلات اختبار البرمجيات."],
                 "ISO 9000 is a related series of standards dealing with quality management and assurance.",
                 "ISO 9000 سلسلة معايير مترابطة تعنى بإدارة الجودة وضمانها."),
            item("ch7_iso9001_role", "Understand",
                 "What role does ISO 9001 play within the ISO 9000 series?",
                 "ما دور ISO 9001 ضمن سلسلة ISO 9000؟",
                 ["It specifies requirements for a quality-management system.", "It ranks organizations by software maturity level.", "It defines software product quality characteristics.", "It estimates failure intensity during program execution."],
                 ["يحدد متطلبات نظام الجودة وإدارته داخل المؤسسة.", "يرتب المؤسسات بمستويات نضج عملية البرمجيات.", "يحدد خصائص جودة المنتج في الأنظمة البرمجية.", "يقدر شدة إخفاق البرمجيات خلال التنفيذ."],
                 "ISO 9001 is the quality-system standard in the series most directly applied to development organizations.",
                 "يمثل ISO 9001 معيار نظام الجودة الأوثق صلة بمؤسسات التطوير ضمن السلسلة."),
            item("ch7_iso90003_guidance", "Understand",
                 "What does ISO 9000-3 provide in software quality management?",
                 "ماذا يقدم ISO 9000-3 لإدارة جودة البرمجيات؟",
                 ["Guidance for applying ISO 9001 to software development.", "A replacement for ISO 9001's quality-system requirements.", "A five-level scale for measuring process maturity.", "A model for estimating software failure intensity."],
                 ["إرشادات لتطبيق ISO 9001 على تطوير البرمجيات.", "بديلاً عن متطلبات نظام الجودة في ISO 9001.", "مقياساً من خمسة مستويات لقياس نضج العملية.", "نموذجاً لتقدير شدة إخفاق البرمجيات."],
                 "ISO 9000-3 gives software-specific guidance for applying the broader ISO 9001 requirements.",
                 "يقدم ISO 9000-3 إرشادات خاصة بالبرمجيات لتطبيق متطلبات ISO 9001 الأوسع."),
            item("ch7_iso_clause_version", "Understand",
                 "In a 20-clause ISO 9001 version, what do the clauses collectively specify?",
                 "في إصدار ISO 9001 ذي البنود العشرين، ماذا تحدد البنود مجتمعة؟",
                 ["Requirements for an organization's quality system.", "A five-stage path for software-process maturity.", "A hierarchy of quality attributes for software products.", "Equations for estimating failure rates during testing."],
                 ["متطلبات نظام الجودة وإدارته داخل المؤسسة.", "تتابع مراحل نضج عملية تطوير البرمجيات.", "هرم يضم خصائص جودة المنتجات البرمجية.", "معادلات لقياس معدل الإخفاق أثناء الاختبار."],
                 "The clause count belongs to a specific edition; the clauses describe quality-system requirements.",
                 "يرتبط عدد البنود بإصدار محدد، وتصف البنود متطلبات نظام الجودة."),
            item("ch7_iso_cmm_scope", "Analyze",
                 "Which scope contrast between ISO 9001 and CMM is accurate?",
                 "أي فرق في النطاق بين ISO 9001 وCMM دقيق؟",
                 ["ISO 9001 is broad; CMM focuses on software-process maturity.", "ISO 9001 is software-only; CMM applies to all industries.", "Both standards apply only to hardware manufacturing.", "CMM specifies quality-system certification for every product."],
                 ["نطاق ISO 9001 واسع، ويركز CMM على نضج عملية البرمجيات.", "يقتصر ISO 9001 على البرمجيات، ويشمل CMM الصناعات كلها.", "يقتصر المعياران على إجراءات تصنيع الأجهزة فقط.", "يمنح CMM اعتماد جودة لجميع المنتجات البرمجية."],
                 "ISO 9001 applies across sectors, whereas CMM provides a software-process maturity framework.",
                 "يطبق ISO 9001 على قطاعات واسعة، بينما يقدم CMM إطاراً لنضج عملية البرمجيات."),
            item("ch7_iso_cmm_improvement", "Analyze",
                 "Which emphasis most clearly distinguishes CMM from ISO 9001?",
                 "أي اهتمام يميز CMM بوضوح عن ISO 9001؟",
                 ["CMM emphasizes continuous software-process improvement.", "CMM emphasizes product certification for all industries.", "ISO 9001 measures software faults after every execution.", "ISO 9001 defines a five-stage maturity progression."],
                 ["يركز CMM على التحسين المستمر لعملية البرمجيات.", "يركز CMM على اعتماد المنتجات في الصناعات كلها.", "يقيس ISO 9001 عيوب البرمجيات بعد كل تشغيل.", "يحدد ISO 9001 تدرجاً من خمس مراحل للنضج."],
                 "The CMM places strong emphasis on continuous process improvement; ISO 9001 specifies an acceptable quality system.",
                 "يركز CMM بقوة على التحسين المستمر، بينما يحدد ISO 9001 نظام جودة مقبولاً."),
            item("ch7_iso_cmm_shared_principle", "Understand",
                 "Which principle is shared by ISO 9001 and CMM?",
                 "أي مبدأ مشترك بين ISO 9001 وCMM؟",
                 ["Document the process and follow it as documented.", "Replace all process records with product inspections.", "Use the same software process in every industry.", "Guarantee that every delivered program has no faults."],
                 ["وثق العملية ونفذ العمل بما يطابق توثيقها.", "استبدل سجلات العملية بفحص المنتج النهائي.", "استخدم إجراءً واحداً في كل قطاعات الصناعة.", "اضمن خلو كل برنامج من العيوب بعد التسليم."],
                 "Both approaches emphasize documented processes and work that matches them.",
                 "تقدر المقاربتان توثيق العمليات وتنفيذ العمل وفقاً لها."),
            item("ch7_iso_document_mapping", "Apply",
                 "Which CMM practice area most directly supports ISO 9001 document control?",
                 "أي مجال في CMM يدعم ضبط الوثائق وفق ISO 9001 مباشرة؟",
                 ["Software Configuration Management processes.", "Software Subcontract Management practices.", "Software Project Planning activities.", "Software Product Engineering practices."],
                 ["إدارة تهيئة البرمجيات.", "إدارة التعاقدات البرمجية.", "تخطيط مشروع البرمجيات.", "هندسة المنتج البرمجي."],
                 "CMM configuration-management practices control the distribution and modification of documents.",
                 "تضبط ممارسات إدارة التهيئة توزيع الوثائق وتعديلها."),
            item("ch7_iso_audit_mapping", "Apply",
                 "Which CMM common feature most directly supports ISO 9001 quality audits?",
                 "أي خاصية مشتركة في CMM تدعم تدقيق الجودة وفق ISO 9001 مباشرة؟",
                 ["Verifying Implementation, through reviews and audits.", "Ability to Perform, through staff and tools.", "Activities Performed, through plans and work products.", "Commitment to Perform, through management policy."],
                 ["التحقق من التنفيذ عبر المراجعات والتدقيق.", "القدرة على الأداء عبر الموارد والتدريب.", "الأنشطة المنفذة عبر الخطط ومخرجات العمل.", "الالتزام بالأداء عبر السياسة والدعم الإداري."],
                 "The Verifying Implementation feature uses reviews and audits to check adherence to established practice.",
                 "تستخدم خاصية التحقق من التنفيذ المراجعات والتدقيق لفحص الالتزام بالممارسة المقررة."),
            item("ch7_iso_certification_limit", "Analyze",
                 "What does ISO 9001 certification establish most directly?",
                 "ماذا يثبت اعتماد ISO 9001 مباشرة؟",
                 ["The quality system's conformance to specified requirements.", "That the software contains no faults in operation.", "That the organization has reached CMM's highest level.", "That every project follows identical technical methods."],
                 ["مطابقة نظام الجودة لمتطلبات محددة.", "خلو البرمجيات من العيوب أثناء التشغيل.", "بلوغ المؤسسة أعلى مستوى في CMM.", "اتباع كل مشروع أساليب تقنية متطابقة."],
                 "Certification concerns the quality system's conformance; it is not proof of fault-free software or CMM maturity.",
                 "يتعلق الاعتماد بمطابقة نظام الجودة، ولا يثبت خلو البرمجيات من العيوب أو مستوى نضج CMM."),
            item("ch7_iso_cmm_selection", "Evaluate",
                 "An organization seeks software-process improvement but also faces a buyer's certification requirement; which choice is sound?",
                 "تسعى مؤسسة لتحسين عملية البرمجيات وتواجه شرط اعتماد من مشترٍ؛ أي اختيار سليم؟",
                 ["Use CMM to guide improvement and meet required ISO certification.", "Use ISO certification alone as proof of continuous improvement.", "Use CMM maturity as a substitute for every market certificate.", "Choose either approach because both guarantee defect-free products."],
                 ["استخدم CMM للتحسين ونفذ اعتماد ISO المطلوب.", "استخدم اعتماد ISO لإثبات التحسين المستمر.", "استخدم نضج CMM بديلاً لكل اعتماد سوقي.", "اخترهما لأن كليهما يضمن خلو المنتج من العيوب."],
                 "CMM can structure software-process improvement, while a market may separately require ISO 9001 certification.",
                 "يمكن لـCMM تنظيم تحسين عملية البرمجيات، وقد يتطلب السوق اعتماد ISO 9001 أيضاً."),
        ],
    },
]


def rotate(seq, shift):
    n = len(seq)
    return [seq[(j - shift) % n] for j in range(n)]


def all_questions():
    built = []
    all_ids = set()
    errors = []
    for b in BANKS:
        items = b["items"]
        key = b["key"]
        if len(items) != len(key) or not 8 <= len(items) <= 16:
            errors.append((b["file"], "bank size/key", len(items), len(key)))
            continue
        for c in LETTERS:
            if key.count(c) > 0.32 * len(items):
                errors.append((b["file"], "key bias", c, key.count(c)))
        questions = []
        long_en = short_en = long_ar = short_ar = 0
        for idx, (cid, bloom, en, ar, oe, oa, ee, ea) in enumerate(items):
            if cid in all_ids:
                errors.append((cid, "duplicate concept_id in Chapter 7"))
            all_ids.add(cid)
            if len(oe) != 4 or len(oa) != 4:
                errors.append((cid, "needs four options"))
                continue
            for field, value in (("question", en), ("question_ar", ar),
                                 ("explanation", ee), ("explanation_ar", ea),
                                 *(("option", x) for x in oe + oa)):
                if META.search(value):
                    errors.append((cid, "handout reference", field, value))
            for lang, opts, ratio in (("EN", oe, 1.40), ("AR", oa, 1.30)):
                if any(not x.strip() for x in opts):
                    errors.append((cid, lang + " empty option"))
                lens = [len(x) for x in opts]
                spread = max(lens) / min(lens)
                corr = lens[0] / (sum(lens[1:]) / 3)
                if spread > ratio or not 0.88 <= corr <= 1.12:
                    errors.append((cid, lang, "option lengths", lens,
                                   "spread=%.2f correct/mean=%.2f" % (spread, corr), opts))
                if lang == "EN":
                    long_en += int(lens[0] == max(lens) and lens.count(max(lens)) == 1)
                    short_en += int(lens[0] == min(lens) and lens.count(min(lens)) == 1)
                else:
                    long_ar += int(lens[0] == max(lens) and lens.count(max(lens)) == 1)
                    short_ar += int(lens[0] == min(lens) and lens.count(min(lens)) == 1)
            if any("$" in o or "\\" in o for o in oe + oa):
                errors.append((cid, "formula or LaTeX in option"))
            if any(re.search(r"\([A-Za-z]{3,}[^)]*\)", o) for o in oe + oa):
                errors.append((cid, "parenthetical English gloss in option"))
            if len(en) > 200 or len(ar) > 200:
                errors.append((cid, "stem exceeds 200 characters"))
            shift = LETTERS.index(key[idx])
            en_rot = rotate(oe, shift)
            ar_rot = rotate(oa, shift)
            questions.append({
                "id": "q%d" % (idx + 1),
                "concept_id": cid,
                "bloom_level": bloom,
                "question": en,
                "question_ar": ar,
                "options": en_rot,
                "options_ar": ar_rot,
                "options_en": en_rot,
                "answer": key[idx],
                "correct": shift,
                "explanation": ee,
                "explanation_ar": ea,
            })
        for lang, counts in (("EN", (long_en, short_en)), ("AR", (long_ar, short_ar))):
            if counts[0] > 0.30 * len(items) or counts[1] > 0.30 * len(items):
                errors.append((b["file"], lang, "unique length tells", counts, len(items)))
        built.append((b, questions))

    # Concept IDs must be unique across all other active ASE banks too.
    for path in OUT.glob("Quiz_*.json"):
        if path.stem.startswith("Quiz_Ch07_"):
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for q in data.get("questions", []):
            cid = q.get("concept_id")
            if cid in all_ids:
                errors.append((cid, "concept_id already used in", path.name))
    return built, errors


def main():
    write = "--write" in sys.argv
    built, errors = all_questions()
    print("Chapter 7 draft validation")
    for b, questions in built:
        print("%-46s questions=%2d keys=%s" % (b["file"], len(questions),
                                                 " ".join(c + ":" + str(b["key"].count(c)) for c in LETTERS)))
    if errors:
        print("FAIL: %d issue(s)" % len(errors))
        for e in errors:
            print(" -", e)
        raise SystemExit(1)
    print("PASS: IDs, schema shape, source references, option parity, and length gates")
    if not write:
        print("Dry run only; no bank files changed. Use --write after reviewing this result.")
        return
    # Preserve each bank's existing envelope and update only its topic and questions.
    for b, questions in built:
        path = OUT / b["file"]
        bank = json.loads(path.read_text(encoding="utf-8"))
        bank["topic"] = b["topic"]
        bank["topic_ar"] = b["topic_ar"]
        bank["questions"] = questions
        path.write_text(json.dumps(bank, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("wrote", path.name)


if __name__ == "__main__":
    main()
