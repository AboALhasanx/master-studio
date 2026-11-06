# ASE Chapter 7 — MCSQuiz Question Review

This sheet mirrors the active bilingual question banks. Each item shows the complete option set, keyed answer, and explanation for review.

## Student format decisions

Use concise bilingual MCQs that test definitions, formula or model interpretation, assumptions, distinctions, and key course notes. Keep scenarios short. Do not turn the banks into long numerical-result problems. Each bank stays within the agreed 8–16 question limit.

## Questions

## B01 — Reliability Foundations and Operating Environment

**الموضوع:** أسس الموثوقية وبيئة التشغيل

### Q1 — What defines software reliability?

ما الذي يحدد موثوقية البرمجيات؟

**Options / الخيارات**

- **A.** Failure-free operation for a stated time and environment.
  - عمل خالٍ من الإخفاق خلال زمن وبيئة محددين.
- **B.** Correct output for every input in every possible setting.
  - نتائج صحيحة لكل المدخلات وفي جميع البيئات.
- **C.** A defect-free codebase after its final inspection.
  - برنامج خالٍ من العيوب بعد الفحص النهائي.
- **D.** A fixed count of successful runs regardless of duration.
  - عدد محدد من التشغيلات الناجحة مهما طال الزمن.

**Answer:** A. Failure-free operation for a stated time and environment.

**الإجابة:** A. عمل خالٍ من الإخفاق خلال زمن وبيئة محددين.

**Explanation:** Reliability is the probability of failure-free operation under stated conditions for a specified period.

**ملاحظة:** الموثوقية احتمال استمرار العمل بلا إخفاق ضمن ظروف محددة ولمدة معلومة.

### Q2 — How does a fault differ from a failure?

كيف يختلف العيب عن الإخفاق؟

**Options / الخيارات**

- **A.** A fault is a wrong output; a failure is its hidden cause.
  - العيب مخرج خاطئ، والإخفاق سببه الداخلي.
- **B.** A fault is latent; a failure is observed incorrect operation.
  - العيب كامن، والإخفاق انحراف ظاهر عن المتطلبات.
- **C.** A failure is latent; a fault is observed incorrect operation.
  - الإخفاق كامن، والعيب انحراف ظاهر عن المتطلبات.
- **D.** A fault is a missing test; a failure is a passed test.
  - العيب حالة اختبار مفقودة، والإخفاق اختبار ناجح.

**Answer:** B. A fault is latent; a failure is observed incorrect operation.

**الإجابة:** B. العيب كامن، والإخفاق انحراف ظاهر عن المتطلبات.

**Explanation:** A fault is a latent defect; a failure is the program's externally visible departure from requirements.

**ملاحظة:** العيب نقص كامن في البرنامج، أما الإخفاق فهو انحراف ظاهر عن المتطلبات عند التشغيل.

### Q3 — What can happen when one fault remains in a program?

ماذا قد يحدث عند بقاء عيب واحد في البرنامج؟

**Options / الخيارات**

- **A.** Several failures only if several separate faults exist.
  - إخفاقات متعددة لا تحدث إلا بوجود عيوب متعددة.
- **B.** No failure unless the fault is manually activated.
  - لا يظهر الإخفاق إلا عند تفعيل العيب يدوياً.
- **C.** Repeated failures whenever its triggering condition recurs.
  - إخفاقات متكررة كلما تكرر شرط تفعيل العيب.
- **D.** One failure total, even when its triggering condition recurs.
  - إخفاق واحد فقط حتى مع تكرر شرط التفعيل.

**Answer:** C. Repeated failures whenever its triggering condition recurs.

**الإجابة:** C. إخفاقات متكررة كلما تكرر شرط تفعيل العيب.

**Explanation:** One fault can produce multiple failures when execution repeatedly reaches the condition that activates it.

**ملاحظة:** قد يسبب العيب الواحد إخفاقات متعددة عند تكرر شرط التشغيل الذي يفعّله.

### Q4 — Which pattern describes the hardware bathtub curve?

أي نمط يصف منحنى حوض الاستحمام للأجهزة؟

**Options / الخيارات**

- **A.** It rises during burn-in, steadies, then falls with wear.
  - ترتفع في الإحماء، تستقر، ثم تنخفض مع الاهتراء.
- **B.** It stays steady during burn-in, then falls as parts age.
  - تستقر في الإحماء، ثم تنخفض مع تقادم الأجزاء.
- **C.** It falls continuously because software faults are removed.
  - تنخفض باستمرار بسبب إزالة عيوب البرمجيات.
- **D.** It falls during burn-in, steadies, then rises with wear.
  - تنخفض في الإحماء، تستقر، ثم ترتفع مع الاهتراء.

**Answer:** D. It falls during burn-in, steadies, then rises with wear.

**الإجابة:** D. تنخفض في الإحماء، تستقر، ثم ترتفع مع الاهتراء.

**Explanation:** Hardware failures are initially high during burn-in, lower during useful life, and higher again with wear-out.

**ملاحظة:** تكون إخفاقات الأجهزة مرتفعة أولاً، ثم تستقر في العمر النافع، ثم ترتفع مع الاهتراء.

### Q5 — Which contrast between software and hardware failures is sound?

أي مقارنة بين إخفاقات البرمجيات والأجهزة دقيقة؟

**Options / الخيارات**

- **A.** Software faults are design defects; hardware often suffers physical wear.
  - عيوب البرمجيات تصميمية، بينما تتعرض الأجهزة غالباً للاهتراء.
- **B.** Software mainly suffers physical wear; hardware mainly has design faults.
  - تهترئ البرمجيات غالباً، بينما تكون عيوب الأجهزة تصميمية.
- **C.** Both fail mainly through material aging after devices are manufactured.
  - يفشل كلاهما غالباً بسبب تقادم المواد بعد التصنيع والتشغيل.
- **D.** Neither failure pattern depends on its operating conditions.
  - لا يعتمد أي منهما على ظروف الاستخدام أو بيئة التشغيل.

**Answer:** A. Software faults are design defects; hardware often suffers physical wear.

**الإجابة:** A. عيوب البرمجيات تصميمية، بينما تتعرض الأجهزة غالباً للاهتراء.

**Explanation:** Software failures are associated with design faults and their activation; hardware also degrades physically.

**ملاحظة:** ترتبط إخفاقات البرمجيات بعيوب التصميم وتفعيلها، بينما تتدهور الأجهزة مادياً أيضاً.

### Q6 — What does an operational profile describe?

ماذا يصف Operational Profile؟

**Options / الخيارات**

- **A.** The hardware parts installed in each deployment environment.
  - الأجزاء المادية المثبتة ضمن بيئة نشر محددة.
- **B.** The expected proportions of the program's different run types.
  - النسب المتوقعة لأنواع التشغيل المختلفة للبرنامج.
- **C.** The sequence of source files used during software construction.
  - ترتيب ملفات البرنامج المستخدمة أثناء بناء النسخة.
- **D.** The order in which faults are repaired during a test session.
  - تسلسل إصلاح العيوب خلال جلسة اختبار واحدة.

**Answer:** B. The expected proportions of the program's different run types.

**الإجابة:** B. النسب المتوقعة لأنواع التشغيل المختلفة للبرنامج.

**Explanation:** An operational profile assigns probabilities to run types reflecting expected use.

**ملاحظة:** يحدد Operational Profile احتمالات أنواع التشغيل وفقاً للاستخدام المتوقع.

### Q7 — Why can one program have different reliability under two use profiles?

لماذا قد تختلف موثوقية البرنامج نفسه باختلاف ملفي الاستخدام؟

**Options / الخيارات**

- **A.** Reliability ignores which operations users perform in that profile.
  - يتجاهل مقياس الموثوقية العمليات التي ينفذها المستخدمون.
- **B.** A new use profile removes faults without changing the software.
  - يزيل ملف الاستخدام العيوب من دون تعديل البرنامج.
- **C.** Profiles weight operations by their different failure chances.
  - يمنح كل ملف أوزاناً مختلفة لعمليات تختلف فرص إخفاقها.
- **D.** Each profile rewrites the program's code automatically.
  - يغير كل ملف شفرة البرنامج تلقائياً عند التشغيل.

**Answer:** C. Profiles weight operations by their different failure chances.

**الإجابة:** C. يمنح كل ملف أوزاناً مختلفة لعمليات تختلف فرص إخفاقها.

**Explanation:** Changing the probabilities of operations with different conditional failure chances changes the profile-level reliability.

**ملاحظة:** يتغير تقدير الموثوقية إذا اختلفت أوزان العمليات واختلفت فرص إخفاقها الشرطية.

### Q8 — What is the input space of a program?

ما المقصود بفضاء مدخلات البرنامج؟

**Options / الخيارات**

- **A.** The set of output values produced by completed runs.
  - مجموعة قيم الخرج الناتجة عن التشغيلات المكتملة.
- **B.** The list of faults detected during a reliability study.
  - قائمة العيوب المكتشفة خلال دراسة الموثوقية.
- **C.** The processor time reserved for the program's execution.
  - مدة المعالج المخصصة لتنفيذ البرنامج فعلياً.
- **D.** The set of possible states of its external input variables.
  - مجموعة الحالات الممكنة لمتغيرات الإدخال الخارجية.

**Answer:** D. The set of possible states of its external input variables.

**الإجابة:** D. مجموعة الحالات الممكنة لمتغيرات الإدخال الخارجية.

**Explanation:** An input state is a combination of values for external variables; the input space contains the possible states.

**ملاحظة:** حالة الإدخال مجموعة قيم للمتغيرات الخارجية، وفضاء الإدخال يضم الحالات الممكنة.

### Q9 — How does the functional environment affect observed failures?

كيف تؤثر البيئة الوظيفية في الإخفاقات المرصودة؟

**Options / الخيارات**

- **A.** Different run types can activate different faults in the same program.
  - تفعّل أنواع التشغيل عيوباً مختلفة في البرنامج نفسه.
- **B.** The environment determines how many faults were written in the code.
  - تحدد البيئة عدد العيوب المكتوبة مسبقاً في الشفرة.
- **C.** Different environments make every fault fail on every execution.
  - تجعل البيئة كل عيب يفشل مع كل تشغيل للبرنامج.
- **D.** Run types affect hardware wear but never software failures.
  - تؤثر أنواع التشغيل في عتاد النظام لا في البرنامج.

**Answer:** A. Different run types can activate different faults in the same program.

**الإجابة:** A. تفعّل أنواع التشغيل عيوباً مختلفة في البرنامج نفسه.

**Explanation:** The operations and inputs exercised determine which latent faults are encountered.

**ملاحظة:** تحدد العمليات والمدخلات المنفذة العيوب الكامنة التي يجري الوصول إليها.

### Q10 — What distinguishes execution time from clock time?

ما الفرق بين زمن التنفيذ وزمن الساعة؟

**Options / الخيارات**

- **A.** Execution time is user effort; clock time is processor utilization.
  - زمن التنفيذ جهد المستخدم، وزمن الساعة انشغال المعالج.
- **B.** Execution time is processor work; clock time includes waits within a run.
  - وقت التنفيذ هو وقت المعالج، والساعة تشمل انتظار التشغيل.
- **C.** Execution time includes shutdowns; clock time excludes all waiting.
  - يشمل زمن التنفيذ الإطفاء، ولا يحسب زمن الساعة أي انتظار.
- **D.** Execution time measures calendar days; clock time counts failures.
  - يقيس زمن التنفيذ الأيام، بينما يحصي زمن الساعة الإخفاقات.

**Answer:** B. Execution time is processor work; clock time includes waits within a run.

**الإجابة:** B. وقت التنفيذ هو وقت المعالج، والساعة تشمل انتظار التشغيل.

**Explanation:** Execution time is time spent by the processor executing the program; clock time also includes waits during a run.

**ملاحظة:** زمن التنفيذ هو وقت عمل المعالج على البرنامج، أما زمن الساعة فيشمل فترات الانتظار أثناء التشغيل.

## B02 — Software Quality Models

**الموضوع:** نماذج جودة البرمجيات

### Q1 — How does software reliability relate to software quality?

كيف ترتبط موثوقية البرمجيات بجودتها؟

**Options / الخيارات**

- **A.** Reliability is one quality attribute, not the whole of quality.
  - الموثوقية سمة من سمات الجودة وليست الجودة كلها.
- **B.** Reliability and quality are identical measures in every model.
  - الموثوقية والجودة مقياس واحد في جميع النماذج.
- **C.** Quality measures failures, while reliability measures source size.
  - تقيس الجودة الإخفاقات، وتقيس الموثوقية حجم الشفرة.
- **D.** Reliability is a development process; quality is a test technique.
  - الموثوقية عملية تطوير، والجودة أسلوب اختبار.

**Answer:** A. Reliability is one quality attribute, not the whole of quality.

**الإجابة:** A. الموثوقية سمة من سمات الجودة وليست الجودة كلها.

**Explanation:** Reliability is a quality characteristic; software quality covers additional attributes as well.

**ملاحظة:** الموثوقية إحدى خصائص الجودة، وتشمل جودة البرمجيات سمات أخرى أيضاً.

### Q2 — Which groups organize McCall's software quality factors?

ما المجموعات التي تنظم عوامل الجودة في نموذج McCall؟

**Options / الخيارات**

- **A.** Primary uses, intermediate constructs, and primitive constructs.
  - الاستخدامات والبنى المتوسطة والبدائية في نموذج Boehm.
- **B.** Product operation, product revision, and product transition.
  - تشغيل المنتج ومراجعته وانتقاله ضمن تصنيف الجودة.
- **C.** Process planning, process control, and process improvement.
  - إدارة العملية وقياسها وتحسينها ضمن نضج المؤسسة.
- **D.** Functionality, reliability, usability, and maintainability.
  - الوظيفية والموثوقية وسهولة الاستخدام والصيانة.

**Answer:** B. Product operation, product revision, and product transition.

**الإجابة:** B. تشغيل المنتج ومراجعته وانتقاله ضمن تصنيف الجودة.

**Explanation:** McCall groups product quality factors under operation, revision, and transition.

**ملاحظة:** ينظم McCall عوامل جودة المنتج ضمن التشغيل والمراجعة والانتقال.

### Q3 — What is the relationship between McCall's factors and criteria?

ما العلاقة بين العوامل والمعايير في نموذج McCall؟

**Options / الخيارات**

- **A.** Criteria replace factors when the product enters operation.
  - تحل المعايير محل العوامل عند تشغيل المنتج.
- **B.** Factors and criteria are interchangeable names for one level.
  - العوامل والمعايير اسمان متبادلان للمستوى نفسه.
- **C.** Criteria are lower-level attributes that inform quality factors.
  - المعايير سمات أدنى مستوى تصف عوامل الجودة.
- **D.** Factors are lower-level attributes that define quality criteria.
  - العوامل سمات أدنى مستوى تحدد معايير الجودة.

**Answer:** C. Criteria are lower-level attributes that inform quality factors.

**الإجابة:** C. المعايير سمات أدنى مستوى تصف عوامل الجودة.

**Explanation:** Quality factors are the higher-level attributes; criteria are the second-level attributes related to them.

**ملاحظة:** عوامل الجودة سمات المستوى الأعلى، أما المعايير فسمات المستوى الثاني المرتبطة بها.

### Q4 — Where does reliability belong in McCall's product-factor groups?

ضمن أي مجموعة تقع الموثوقية في عوامل McCall؟

**Options / الخيارات**

- **A.** Product revision, which concerns testing and maintenance.
  - مراجعة المنتج وتشمل الاختبار والصيانة والتعديل.
- **B.** Product transition, which concerns transfer between platforms.
  - انتقال المنتج ويشمل النقل بين المنصات والأنظمة.
- **C.** Process improvement, which concerns organizational maturity.
  - تحسين العملية يرفع نضج الممارسات المؤسسية.
- **D.** Product operation, which concerns the product during use.
  - تشغيل المنتج ويضم عوامل أدائه أثناء الاستخدام.

**Answer:** D. Product operation, which concerns the product during use.

**الإجابة:** D. تشغيل المنتج ويضم عوامل أدائه أثناء الاستخدام.

**Explanation:** Reliability is a product-operation factor alongside attributes such as correctness and usability.

**ملاحظة:** الموثوقية من عوامل تشغيل المنتج إلى جانب سمات مثل الصحة وسهولة الاستخدام.

### Q5 — Which concern best fits McCall's product revision group?

أي اهتمام يلائم مجموعة مراجعة المنتج لدى McCall؟

**Options / الخيارات**

- **A.** Making software easier to test, maintain, and modify.
  - تسهيل اختبار البرمجيات وصيانتها وتعديلها.
- **B.** Moving software between platforms and linking systems.
  - نقل البرمجيات بين المنصات وربط الأنظمة.
- **C.** Helping users operate the software during normal use.
  - مساعدة المستخدمين على تشغيل البرمجيات يومياً.
- **D.** Measuring maturity across an organization's process levels.
  - قياس نضج العملية عبر مستويات المؤسسة.

**Answer:** A. Making software easier to test, maintain, and modify.

**الإجابة:** A. تسهيل اختبار البرمجيات وصيانتها وتعديلها.

**Explanation:** Product revision covers factors related to testing and maintaining the software.

**ملاحظة:** تشمل مراجعة المنتج العوامل المرتبطة باختبار البرمجيات وصيانتها.

### Q6 — Which set contains McCall's product transition factors?

أي مجموعة تضم عوامل انتقال المنتج في نموذج McCall؟

**Options / الخيارات**

- **A.** Suitability, accuracy, and recoverability.
  - الملاءمة والدقة والاستعادة ضمن خصائص المنتج.
- **B.** Portability, reusability, and interoperability.
  - قابلية النقل وإعادة الاستخدام والتشغيل البيني.
- **C.** Correctness, efficiency, and integrity.
  - الصحة والكفاءة والتكامل ضمن عوامل تشغيل المنتج.
- **D.** Testability, flexibility, and maintainability.
  - الاختبار والمرونة والصيانة ضمن مراجعة المنتج.

**Answer:** B. Portability, reusability, and interoperability.

**الإجابة:** B. قابلية النقل وإعادة الاستخدام والتشغيل البيني.

**Explanation:** McCall places portability, reusability, and interoperability under product transition.

**ملاحظة:** يضع McCall قابلية النقل وإعادة الاستخدام والتشغيل البيني ضمن انتقال المنتج.

### Q7 — Which hierarchy describes Boehm's software quality model?

أي تسلسل يصف هرم نموذج Boehm لجودة البرمجيات؟

**Options / الخيارات**

- **A.** Functionality, reliability, usability, and maintainability.
  - خصائص ISO 9126 الست ضمن بنية جودة صارمة.
- **B.** Initial, repeatable, defined, managed, and optimizing.
  - مستويات CMM الخمسة من الأولي إلى المحسن.
- **C.** Primary uses, intermediate constructs, and primitive constructs.
  - الاستخدامات الأولية والبنى المتوسطة والبدائية.
- **D.** Product operation, product revision, and product transition.
  - تشغيل المنتج ومراجعته وانتقاله ضمن نموذج McCall.

**Answer:** C. Primary uses, intermediate constructs, and primitive constructs.

**الإجابة:** C. الاستخدامات الأولية والبنى المتوسطة والبدائية.

**Explanation:** Boehm organizes quality through primary uses, intermediate constructs, and primitive constructs.

**ملاحظة:** ينظم Boehm الجودة عبر الاستخدامات الأولية والبنى المتوسطة والبنى البدائية.

### Q8 — What do Boehm's intermediate constructs resemble?

بماذا تشبه البنى المتوسطة في نموذج Boehm؟

**Options / الخيارات**

- **A.** McCall's lower-level product quality criteria.
  - معايير الجودة الأدنى مستوى في نموذج McCall.
- **B.** CMM's maturity levels for software-process improvement.
  - مستويات النضج في CMM لتحسين العملية.
- **C.** ISO 9001's clauses for quality-system certification.
  - بنود ISO 9001 لاعتماد نظام الجودة.
- **D.** McCall's higher-level product quality factors.
  - عوامل الجودة الأعلى مستوى في نموذج McCall.

**Answer:** D. McCall's higher-level product quality factors.

**الإجابة:** D. عوامل الجودة الأعلى مستوى في نموذج McCall.

**Explanation:** Boehm's intermediate constructs are similar to McCall's quality factors.

**ملاحظة:** تشبه البنى المتوسطة لدى Boehm عوامل الجودة في نموذج McCall.

### Q9 — Which set lists ISO 9126's top-level quality characteristics?

أي مجموعة تسرد خصائص الجودة العليا في ISO 9126؟

**Options / الخيارات**

- **A.** Functionality, reliability, usability, efficiency, maintainability, portability.
  - الوظيفية والموثوقية وسهولة الاستخدام والكفاءة والصيانة والنقل.
- **B.** Correctness, efficiency, integrity, usability, flexibility, reusability.
  - الصحة والكفاءة والتكامل وسهولة الاستخدام والمرونة وإعادة الاستخدام.
- **C.** Operation, revision, transition, testing, maturity, certification, and process control.
  - التشغيل والمراجعة والانتقال والنضج والاختبار والاعتماد.
- **D.** Suitability, accuracy, security, training, audit, and documented process control.
  - الملاءمة والدقة والأمن والتدريب والتدقيق وضبط العملية.

**Answer:** A. Functionality, reliability, usability, efficiency, maintainability, portability.

**الإجابة:** A. الوظيفية والموثوقية وسهولة الاستخدام والكفاءة والصيانة والنقل.

**Explanation:** ISO 9126 names functionality, reliability, usability, efficiency, maintainability, and portability.

**ملاحظة:** يسمي ISO 9126 الوظيفية والموثوقية وسهولة الاستخدام والكفاءة والصيانة وقابلية النقل.

### Q10 — What structural feature distinguishes the ISO 9126 hierarchy?

ما السمة البنيوية التي تميز هرم ISO 9126؟

**Options / الخيارات**

- **A.** The model replaces software characteristics with maturity levels.
  - يستبدل النموذج خصائص البرمجيات بمستويات النضج.
- **B.** Each characteristic is linked to one attribute in a strict hierarchy.
  - ترتبط كل خاصية بسمة واحدة ضمن تسلسل هرمي صارم.
- **C.** Every attribute may belong to several unrelated characteristics.
  - قد تنتمي كل سمة إلى خصائص متعددة غير مترابطة.
- **D.** Quality factors are grouped only by their development cost.
  - تُجمع عوامل الجودة حسب كلفة تطويرها فقط.

**Answer:** B. Each characteristic is linked to one attribute in a strict hierarchy.

**الإجابة:** B. ترتبط كل خاصية بسمة واحدة ضمن تسلسل هرمي صارم.

**Explanation:** The ISO 9126 hierarchy is strict: each characteristic relates to one attribute.

**ملاحظة:** هرم ISO 9126 صارم؛ إذ ترتبط كل خاصية بسمة واحدة.

### Q11 — Whose view do ISO 9126's outer quality characteristics primarily reflect?

أي منظور تعكسه خصائص الجودة الخارجية في ISO 9126 أساساً؟

**Options / الخيارات**

- **A.** The project manager's view of schedule variance.
  - منظور المدير إلى انحراف جدول المشروع.
- **B.** The hardware designer's view of component aging.
  - منظور مصمم الأجهزة إلى تقادم المكونات.
- **C.** The user's external view of the software product.
  - منظور المستخدم إلى الجودة الخارجية للمنتج.
- **D.** The compiler's view of the program's internal code.
  - منظور المترجم إلى البنية الداخلية للبرنامج.

**Answer:** C. The user's external view of the software product.

**الإجابة:** C. منظور المستخدم إلى الجودة الخارجية للمنتج.

**Explanation:** The model's outer attributes describe quality from the user's view rather than an internal developer view.

**ملاحظة:** تصف السمات الخارجية الجودة من منظور المستخدم لا من منظور المطور الداخلي.

## B03 — CMM Maturity Levels

**الموضوع:** مستويات النضج في CMM

### Q1 — Which sequence gives the CMM maturity levels from lowest to highest?

أي تسلسل يرتب مستويات نضج CMM من الأدنى إلى الأعلى؟

**Options / الخيارات**

- **A.** Initial, Repeatable, Defined, Managed, Optimizing.
  - الأولي والمتكرر والمحدد والمدار والمحسن.
- **B.** Initial, Defined, Repeatable, Managed, Optimizing.
  - الأولي والمحدد والمتكرر والمدار والمحسن.
- **C.** Repeatable, Initial, Defined, Optimizing, Managed.
  - المتكرر والأولي والمحدد والمحسن والمدار.
- **D.** Initial, Repeatable, Managed, Defined, Optimizing.
  - الأولي والمتكرر والمدار والمحدد والمحسن.

**Answer:** A. Initial, Repeatable, Defined, Managed, Optimizing.

**الإجابة:** A. الأولي والمتكرر والمحدد والمدار والمحسن.

**Explanation:** The staged path progresses from Initial through Repeatable, Defined, and Managed to Optimizing.

**ملاحظة:** يتدرج المسار من الأولي إلى المتكرر ثم المحدد والمدار وصولاً إلى المحسن.

### Q2 — What does a CMM maturity level characterize?

ماذا يصف مستوى النضج في CMM؟

**Options / الخيارات**

- **A.** The percentage of code that passed a specific test suite.
  - نسبة الشفرة التي اجتازت مجموعة اختبار محددة.
- **B.** Software-process maturity and organizational capability.
  - قدرة عملية البرمجيات في المؤسسة ونضجها.
- **C.** The number of defects remaining in one software release.
  - عدد العيوب الباقية في إصدار برمجي واحد.
- **D.** The quality of a single program's user interface.
  - جودة واجهة المستخدم لبرنامج منفرد.

**Answer:** B. Software-process maturity and organizational capability.

**الإجابة:** B. قدرة عملية البرمجيات في المؤسسة ونضجها.

**Explanation:** CMM maturity describes process capability, not the defect count or quality score of one product.

**ملاحظة:** يصف نضج CMM قدرة العملية، لا عدد عيوب منتج واحد أو درجة جودته.

### Q3 — What best describes an organization at the Initial CMM level?

ما الوصف الأنسب لمؤسسة عند المستوى الأولي في CMM؟

**Options / الخيارات**

- **A.** A standard process is documented across the organization.
  - توثق المؤسسة عملية معيارية مشتركة على مستوى المؤسسة.
- **B.** Process performance stays within measured limits.
  - يضبط الأداء بحدود كمية تقيس استقرار العملية.
- **C.** Work is ad hoc; results depend heavily on individuals.
  - العمل ارتجالي ونتائجه تعتمد غالباً على الأفراد.
- **D.** Projects follow stable plans based on earlier results.
  - تتبع المشاريع خططاً مستقرة مستندة إلى نتائج سابقة.

**Answer:** C. Work is ad hoc; results depend heavily on individuals.

**الإجابة:** C. العمل ارتجالي ونتائجه تعتمد غالباً على الأفراد.

**Explanation:** At the Initial level, the process is unpredictable and often depends on individual effort.

**ملاحظة:** تكون العملية عند المستوى الأولي غير قابلة للتنبؤ وتعتمد غالباً على جهد الأفراد.

### Q4 — What makes the Repeatable CMM level distinct?

ما الذي يميز المستوى المتكرر في CMM؟

**Options / الخيارات**

- **A.** One standard process is tailored across organization units.
  - تتكيف المشاريع مع عملية موحدة في المؤسسة.
- **B.** Statistical control predicts process performance across projects.
  - يتنبأ الضبط الإحصائي بأداء العملية عبر المشاريع.
- **C.** Continuous improvement prevents recurring known defects.
  - يمنع التحسين المستمر تكرار العيوب المعروفة.
- **D.** Stable project management repeats earlier successful practices.
  - تتكرر ممارسات ناجحة بإدارة مشاريع مستقرة.

**Answer:** D. Stable project management repeats earlier successful practices.

**الإجابة:** D. تتكرر ممارسات ناجحة بإدارة مشاريع مستقرة.

**Explanation:** Repeatable project management lets organizations reproduce earlier successful practices.

**ملاحظة:** تتيح إدارة المشاريع المستقرة تكرار الممارسات التي أثبتت نجاحها سابقاً.

### Q5 — What process capability is established at the Defined CMM level?

ما قدرة العملية التي يرسخها المستوى المحدد في CMM؟

**Options / الخيارات**

- **A.** Each project tailors the documented standard process.
  - توثق المؤسسة معياراً للعمل وتكيفه المشاريع.
- **B.** A project process controlled only by individual managers.
  - يضبط المدير الفرد عملية مشروعه من دون معيار مؤسسي.
- **C.** A quantitative limit for every software defect.
  - تقاس به جودة العيوب المكتشفة في كل برنامج.
- **D.** A continuous improvement program driven by new practices.
  - برنامج تحسين مستمر تقوده ممارسات جديدة.

**Answer:** A. Each project tailors the documented standard process.

**الإجابة:** A. توثق المؤسسة معياراً للعمل وتكيفه المشاريع.

**Explanation:** The Defined level documents a standard software process across the organization; projects tailor it.

**ملاحظة:** يوثق المستوى المحدد عملية معيارية للمؤسسة، وتكيفها المشاريع وفق خصائصها.

### Q6 — How does the Managed CMM level control process performance?

كيف يضبط المستوى المدار في CMM أداء العملية؟

**Options / الخيارات**

- **A.** It focuses only on introducing new software technologies.
  - يركز فقط على إدخال تقنيات برمجية جديدة.
- **B.** It uses quantitative measurement to manage process variation.
  - يستخدم القياس الكمي لإدارة تباين العملية.
- **C.** It relies on informal practices that change by individual.
  - يعتمد ممارسات غير رسمية تتغير باختلاف الأفراد.
- **D.** It defines one process without measuring its performance.
  - يحدد عملية واحدة من دون قياس أدائها.

**Answer:** B. It uses quantitative measurement to manage process variation.

**الإجابة:** B. يستخدم القياس الكمي لإدارة تباين العملية.

**Explanation:** At the Managed level, process and product quality are measured and variation is controlled quantitatively.

**ملاحظة:** يُقاس أداء العملية وجودة المنتج كمياً عند المستوى المدار ويُضبط التباين.

### Q7 — What is the central aim of the Optimizing CMM level?

ما الهدف المحوري للمستوى المحسن في CMM؟

**Options / الخيارات**

- **A.** Organization-wide process documentation for engineering and management.
  - توثيق عملية هندسية وإدارية معيارية للمؤسسة.
- **B.** Quantitative control of variation within established limits.
  - ضبط كمي لتباين الأداء ضمن حدود معتمدة.
- **C.** Continuous improvement prevents recurring defects in software.
  - التحسين المستمر للعملية ومنع تكرار العيوب.
- **D.** Stable project tracking using previously successful practices.
  - متابعة مستقرة للمشاريع بممارسات ناجحة سابقة.

**Answer:** C. Continuous improvement prevents recurring defects in software.

**الإجابة:** C. التحسين المستمر للعملية ومنع تكرار العيوب.

**Explanation:** The Optimizing level proactively strengthens the process and seeks to prevent known defects.

**ملاحظة:** يعزز المستوى المحسن العملية استباقياً ويسعى لمنع العيوب المعروفة.

### Q8 — Which distinction separates Defined from Managed maturity?

أي فرق يفصل بين النضج المحدد والنضج المدار؟

**Options / الخيارات**

- **A.** Defined prevents all defects; Managed begins project planning.
  - يمنع المحدد كل العيوب، بينما يبدأ المدار تخطيط المشروع.
- **B.** Defined certifies products; Managed replaces software processes.
  - يعتمد المحدد المنتجات، بينما يستبدل المدار عمليات البرمجيات.
- **C.** Defined measures hardware wear; Managed measures user satisfaction.
  - يقيس المحدد اهتراء الأجهزة، بينما يقيس المدار رضا المستخدم.
- **D.** Defined standardizes the process; Managed controls measured variation.
  - يوحد المحدد العملية، بينما يقيس المدار تباينها كمياً.

**Answer:** D. Defined standardizes the process; Managed controls measured variation.

**الإجابة:** D. يوحد المحدد العملية، بينما يقيس المدار تباينها كمياً.

**Explanation:** Defined establishes a standard process; Managed adds quantitative measurement and control.

**ملاحظة:** يرسخ المستوى المحدد عملية معيارية، ويضيف المدار القياس والضبط الكميين.

## B04 — CMM Key Process Areas and Common Features

**الموضوع:** مناطق العملية والخصائص المشتركة في CMM

### Q1 — What does KPA mean in the CMM?

ماذا يعني KPA في CMM؟

**Options / الخيارات**

- **A.** Key Process Area, a group of related process practices.
  - منطقة رئيسية تضم ممارسات عملية مترابطة.
- **B.** Key Product Attribute, a software quality characteristic.
  - سمة رئيسية تصف جودة منتج برمجي محدد.
- **C.** Known Performance Average, a reliability measurement.
  - متوسط شائع لقياس موثوقية المنتج البرمجي.
- **D.** Kernel Program Activity, a software execution phase.
  - نشاط برمجي يحدد مرحلة من مراحل التطوير.

**Answer:** A. Key Process Area, a group of related process practices.

**الإجابة:** A. منطقة رئيسية تضم ممارسات عملية مترابطة.

**Explanation:** A Key Process Area groups related goals and practices important to process capability at a maturity level.

**ملاحظة:** تجمع منطقة العملية الأساسية أهدافاً وممارسات مترابطة لازمة لقدرة العملية في مستوى نضج معين.

### Q2 — How are Key Process Areas organized in staged CMM?

كيف تُنظم مناطق العملية الأساسية في CMM المرحلي؟

**Options / الخيارات**

- **A.** The Initial level contains all KPAs before any process work.
  - يضم المستوى الأولي كل المناطق قبل بدء العمل.
- **B.** Higher CMM maturity levels introduce their own KPAs.
  - تظهر KPAs في المستويات الأعلى بعد المستوى الأولي.
- **C.** Every KPA belongs to all maturity levels at the same time.
  - تنتمي كل منطقة عملية إلى جميع مستويات النضج معاً.
- **D.** KPAs replace maturity levels in the staged model.
  - تحل مناطق العملية محل مستويات النضج في النموذج المرحلي.

**Answer:** B. Higher CMM maturity levels introduce their own KPAs.

**الإجابة:** B. تظهر KPAs في المستويات الأعلى بعد المستوى الأولي.

**Explanation:** The Initial level has no defined KPAs; the staged areas are introduced at higher levels.

**ملاحظة:** لا يضم المستوى الأولي مناطق محددة، وتظهر مناطق العملية في المستويات الأعلى.

### Q3 — Which set names CMM's common features for institutionalizing a KPA?

أي مجموعة تسمي الخصائص المشتركة لترسيخ KPA في CMM؟

**Options / الخيارات**

- **A.** Operation, revision, transition, maturity, and certification.
  - التشغيل والمراجعة والانتقال والنضج والاعتماد.
- **B.** Reliability, usability, portability, efficiency, and integrity.
  - الموثوقية وسهولة الاستخدام والنقل والكفاءة والتكامل.
- **C.** Commitment, ability, activities, measurement, and verification.
  - الالتزام والقدرة والأنشطة والقياس والتحقق.
- **D.** Planning, coding, compiling, testing, and deployment.
  - التخطيط والبرمجة والترجمة والاختبار والنشر.

**Answer:** C. Commitment, ability, activities, measurement, and verification.

**الإجابة:** C. الالتزام والقدرة والأنشطة والقياس والتحقق.

**Explanation:** The five common features are Commitment to Perform, Ability to Perform, Activities Performed, Measurement and Analysis, and Verifying Implementation.

**ملاحظة:** الخصائص الخمس هي الالتزام بالأداء والقدرة عليه والأنشطة المنفذة والقياس والتحليل والتحقق من التنفيذ.

### Q4 — A process area lacks trained staff, tools, and a clear role structure; which feature is weak?

تفتقر منطقة عملية إلى موظفين مدربين وأدوات وأدوار واضحة؛ أي خاصية ضعيفة؟

**Options / الخيارات**

- **A.** Verifying Implementation, which reviews adherence to procedures.
  - يراجع التحقق من التنفيذ اتباع إجراءات العمل.
- **B.** Measurement and Analysis, which evaluates process data.
  - يحلل القياس بيانات أداء العملية وأهدافها.
- **C.** Commitment to Perform, which establishes management policy.
  - يحدد الالتزام بالأداء سياسة الإدارة ودعمها.
- **D.** Ability to Perform, which provides necessary resources and skills.
  - توفر القدرة على الأداء موارد الفريق وتدريبه.

**Answer:** D. Ability to Perform, which provides necessary resources and skills.

**الإجابة:** D. توفر القدرة على الأداء موارد الفريق وتدريبه.

**Explanation:** Ability to Perform covers prerequisites such as resources, organizational structure, training, and tools.

**ملاحظة:** تشمل القدرة على الأداء الموارد والبنية التنظيمية والتدريب والأدوات اللازمة.

### Q5 — A team audits whether an established process is followed; which feature is applied?

يدقق فريق في الالتزام بعملية مقررة؛ أي خاصية يطبق؟

**Options / الخيارات**

- **A.** Verifying Implementation checks adherence to the process.
  - التحقق من التنفيذ يراجع الالتزام بإجراءات العمل.
- **B.** Activities Performed defines plans and required work products.
  - تحدد الأنشطة المنفذة الخطط ومخرجات العمل المطلوبة.
- **C.** Ability to Perform supplies staff, tools, and training.
  - توفر القدرة على الأداء الموظفين والموارد والتدريب.
- **D.** Commitment to Perform sets policy and management support.
  - يحدد الالتزام بالأداء سياسة الإدارة والدعم المطلوب.

**Answer:** A. Verifying Implementation checks adherence to the process.

**الإجابة:** A. التحقق من التنفيذ يراجع الالتزام بإجراءات العمل.

**Explanation:** Verifying Implementation uses reviews and audits to ensure that activities follow established procedures.

**ملاحظة:** يستخدم التحقق من التنفيذ المراجعات والتدقيق لضمان اتباع الإجراءات المقررة.

### Q6 — How do a KPA and a common feature differ?

كيف تختلف KPA عن الخاصية المشتركة؟

**Options / الخيارات**

- **A.** A KPA measures a product; common features specify user inputs.
  - تقيس KPA منتجاً، وتحدد الخصائص المشتركة مدخلات المستخدم.
- **B.** A KPA names an area; common features institutionalize it.
  - تسمي KPA منطقة عملية، وتنظم الخصائص المشتركة ترسيخها.
- **C.** A KPA names a quality factor; common features measure defects.
  - تسمي KPA عامل جودة، وتقيس الخصائص المشتركة العيوب.
- **D.** A KPA describes a maturity stage; common features replace stages.
  - تصف KPA مرحلة نضج، وتحل الخصائص المشتركة محل المراحل.

**Answer:** B. A KPA names an area; common features institutionalize it.

**الإجابة:** B. تسمي KPA منطقة عملية، وتنظم الخصائص المشتركة ترسيخها.

**Explanation:** A KPA identifies the process area; common features describe how practices in that area are institutionalized.

**ملاحظة:** تحدد KPA مجال العملية، وتصف الخصائص المشتركة كيفية ترسيخ ممارساته.

### Q7 — What remains shared when the subject of a CMM KPA changes?

ما الذي يبقى مشتركاً عند تغير موضوع KPA في CMM؟

**Options / الخيارات**

- **A.** Each area measures attributes of a software product.
  - تقيس كل منطقة سمات منتج برمجي محدد.
- **B.** Organizations receive one common maturity level.
  - تحصل المؤسسات على مستوى نضج موحد.
- **C.** Common features span distinct software process areas.
  - تتكرر الفئات المشتركة عبر مناطق العملية.
- **D.** Each area retains its own specific goals and practices.
  - تحتفظ كل منطقة بأهداف وممارسات خاصة بها.

**Answer:** C. Common features span distinct software process areas.

**الإجابة:** C. تتكرر الفئات المشتركة عبر مناطق العملية.

**Explanation:** The KPA content varies, while the same common-feature categories organize its implementation.

**ملاحظة:** يختلف محتوى مناطق العملية، بينما تنظم الفئات المشتركة طريقة تنفيذها.

### Q8 — What indicates that a KPA is institutionalized rather than used temporarily?

ما الذي يدل على ترسيخ KPA بدلاً من تطبيقها مؤقتاً؟

**Options / الخيارات**

- **A.** Its practices are performed once by a project expert.
  - ينفذ خبير المشروع ممارساتها مرة واحدة فقط.
- **B.** Its goals are replaced whenever a product is released.
  - تُستبدل أهدافها عند كل إصدار للمنتج.
- **C.** Its procedures are kept informal and undocumented.
  - تبقى إجراءاتها غير رسمية وغير موثقة.
- **D.** Its practices are lasting and repeatable over time.
  - تبقى ممارساتها قائمة وقابلة للتكرار.

**Answer:** D. Its practices are lasting and repeatable over time.

**الإجابة:** D. تبقى ممارساتها قائمة وقابلة للتكرار.

**Explanation:** Institutionalization makes KPA practices enduring and repeatable rather than dependent on one temporary effort.

**ملاحظة:** يجعل الترسيخ ممارسات المنطقة مستمرة وقابلة للتكرار بدلاً من اعتمادها على جهد مؤقت.

## B05 — Reliability Measures and Failure Behavior

**الموضوع:** مقاييس الموثوقية وسلوك الإخفاق

### Q1 — How does reliability differ from failure intensity?

كيف تختلف الموثوقية عن شدة الإخفاق؟

**Options / الخيارات**

- **A.** Reliability is a failure-free probability; intensity is a failure rate.
  - الموثوقية احتمال خلو الزمن، والشدة معدل الإخفاق.
- **B.** Reliability is a failure rate; intensity is a failure-free probability.
  - الموثوقية معدل الإخفاق، والشدة احتمال خلو الزمن.
- **C.** Reliability counts latent faults; intensity counts source lines.
  - تحصي الموثوقية العيوب، وتقيس الشدة حجم الشفرة.
- **D.** Reliability is a process level; intensity is a quality attribute.
  - الموثوقية صفة جودة، والشدة معدل وقوع الإخفاق.

**Answer:** A. Reliability is a failure-free probability; intensity is a failure rate.

**الإجابة:** A. الموثوقية احتمال خلو الزمن، والشدة معدل الإخفاق.

**Explanation:** Reliability is a probability over a specified interval; failure intensity is an instantaneous rate per unit time.

**ملاحظة:** الموثوقية احتمال خلال مدة محددة، أما شدة الإخفاق فمعدل لحظي لكل وحدة زمن.

### Q2 — What does the mean value function represent in a reliability model?

ماذا تمثل دالة القيمة المتوسطة في نموذج الموثوقية؟

**Options / الخيارات**

- **A.** The fixed number of faults remaining after final release.
  - العدد الثابت للعيوب الباقية بعد الإصدار النهائي.
- **B.** The expected cumulative failures by a given point in time.
  - العدد التراكمي المتوقع للإخفاقات حتى زمن معين.
- **C.** The instantaneous chance of a failure at one input state.
  - الاحتمال اللحظي للإخفاق عند حالة إدخال واحدة.
- **D.** The average processor utilization during a calendar month.
  - متوسط انشغال المعالج خلال شهر تقويمي.

**Answer:** B. The expected cumulative failures by a given point in time.

**الإجابة:** B. العدد التراكمي المتوقع للإخفاقات حتى زمن معين.

**Explanation:** The mean value function gives the expected cumulative number of failures up to a time point.

**ملاحظة:** تعطي دالة القيمة المتوسطة العدد التراكمي المتوقع للإخفاقات حتى نقطة زمنية معينة.

### Q3 — Before the first observed failure, what duration does MTTF summarize?

قبل أول إخفاق مرصود، أي مدة يلخصها MTTF؟

**Options / الخيارات**

- **A.** The number of failures observed in a time interval.
  - عدد الإخفاقات المرصودة ضمن فترة زمنية.
- **B.** The cumulative count of failures at a chosen time.
  - العدد التراكمي للإخفاقات عند زمن مختار.
- **C.** The average operating time until a failure occurs.
  - متوسط زمن التشغيل المتوقع حتى حدوث إخفاق.
- **D.** The average time separating successive failures.
  - متوسط الزمن الفاصل بين إخفاقين متتاليين.

**Answer:** C. The average operating time until a failure occurs.

**الإجابة:** C. متوسط زمن التشغيل المتوقع حتى حدوث إخفاق.

**Explanation:** Mean Time to Failure is the average operating time before a failure occurs.

**ملاحظة:** متوسط الزمن حتى الإخفاق هو متوسط زمن التشغيل السابق لوقوع إخفاق.

### Q4 — When failures recur during operation, what interval does MTBF summarize?

عند تكرر الإخفاقات أثناء التشغيل، أي فاصل يلخصه MTBF؟

**Options / الخيارات**

- **A.** The average operating time until the first failure.
  - متوسط زمن التشغيل حتى الإخفاق الأول.
- **B.** The failure rate during a single execution interval.
  - معدل الإخفاق خلال فترة تنفيذ واحدة.
- **C.** The expected total failures over the product lifetime.
  - إجمالي الإخفاقات المتوقع طوال عمر المنتج.
- **D.** The average time separating successive failures.
  - متوسط الزمن الفاصل بين إخفاقات متعاقبة.

**Answer:** D. The average time separating successive failures.

**الإجابة:** D. متوسط الزمن الفاصل بين إخفاقات متعاقبة.

**Explanation:** Mean Time Between Failures measures the average interval between successive failures.

**ملاحظة:** يقيس متوسط الزمن بين الإخفاقات متوسط الفاصل بين إخفاقات متتالية.

### Q5 — Which set represents the four common time-based views of failures?

أي مجموعة تمثل الصور الزمنية الأربع الشائعة للإخفاقات؟

**Options / الخيارات**

- **A.** Event time, inter-event time, cumulative and interval counts.
  - زمن الحدث والفاصل بين الأحداث والعدد التراكمي وعدد الفترة.
- **B.** Input state, output state, run type, operational profile.
  - حالة الإدخال وحالة الخرج ونوع التشغيل وملف التشغيل.
- **C.** Execution time, clock time, calendar time, machine time.
  - زمن التنفيذ وزمن الساعة والزمن التقويمي وزمن الآلة.
- **D.** Fault count, program size, test cases, processor usage.
  - عدد العيوب وحجم الشفرة وحالات الاختبار واستخدام المعالج.

**Answer:** A. Event time, inter-event time, cumulative and interval counts.

**الإجابة:** A. زمن الحدث والفاصل بين الأحداث والعدد التراكمي وعدد الفترة.

**Explanation:** Failures may be represented by their times, intervals, cumulative count, or count within an interval.

**ملاحظة:** يمكن تمثيل الإخفاقات بأزمنتها أو فواصلها أو عددها التراكمي أو عددها ضمن فترة.

### Q6 — What does a failure-intensity value express?

ماذا تعبّر عنه قيمة شدة الإخفاق؟

**Options / الخيارات**

- **A.** A percentage of source code inspected by reviewers.
  - نسبة الشفرة التي فُحصت بالمراجعة.
- **B.** A rate of failures per unit of the specified time.
  - معدل إخفاقات لكل وحدة زمن محددة.
- **C.** A probability that ignores the observation period.
  - احتمال لا يرتبط بمدة رصد محددة.
- **D.** A total fault count independent of program execution.
  - عدد العيوب بصرف النظر عن تنفيذ البرنامج.

**Answer:** B. A rate of failures per unit of the specified time.

**الإجابة:** B. معدل إخفاقات لكل وحدة زمن محددة.

**Explanation:** Failure intensity is expressed as a rate, such as failures per hour of execution time.

**ملاحظة:** تُعبّر شدة الإخفاق عن معدل، مثل عدد الإخفاقات لكل ساعة تنفيذ.

### Q7 — Which range is valid for a reliability probability?

أي مدى يصح لاحتمال الموثوقية؟

**Options / الخيارات**

- **A.** Any positive value with no upper bound.
  - أي قيمة موجبة ولو تجاوزت الواحد كثيراً.
- **B.** Only values greater than one during testing.
  - قيمة أكبر من الواحد خلال الاختبار فقط.
- **C.** From zero to one, including both endpoints.
  - قيمة من الصفر حتى الواحد مع شمول الحدين.
- **D.** From zero to one hundred, excluding zero.
  - قيمة بين الصفر والمئة من دون شمول الصفر.

**Answer:** C. From zero to one, including both endpoints.

**الإجابة:** C. قيمة من الصفر حتى الواحد مع شمول الحدين.

**Explanation:** Reliability is a probability, so it lies between zero and one inclusive.

**ملاحظة:** الموثوقية احتمال، لذا تقع بين الصفر والواحد مع شمول الحدين.

### Q8 — During fault removal, which trend commonly links reliability and intensity?

أثناء إزالة العيوب، ما العلاقة الشائعة بين الموثوقية والشدة؟

**Options / الخيارات**

- **A.** Reliability falls as failure intensity falls.
  - تنخفض الموثوقية حين تنخفض شدة الإخفاق.
- **B.** Both measures stay fixed after the first test.
  - يبقى المقياسان ثابتين بعد الاختبار الأول.
- **C.** Both measures rise whenever a fault is removed.
  - ترتفع الموثوقية والشدة عند إزالة عيب.
- **D.** Reliability rises as failure intensity falls.
  - ترتفع الموثوقية حين تنخفض شدة الإخفاق.

**Answer:** D. Reliability rises as failure intensity falls.

**الإجابة:** D. ترتفع الموثوقية حين تنخفض شدة الإخفاق.

**Explanation:** As testing removes faults, reliability commonly increases while the failure intensity decreases.

**ملاحظة:** تزداد الموثوقية عادة مع إزالة العيوب، بينما تنخفض شدة الإخفاق.

### Q9 — A release decision focuses on the instantaneous risk of failure; which measure fits best?

يركز قرار الإصدار على خطر الإخفاق اللحظي؛ أي مقياس يلائمه؟

**Options / الخيارات**

- **A.** Failure intensity, a rate describing risk at a given time.
  - شدة الإخفاق لأنها معدل خطر عند زمن محدد.
- **B.** Reliability, an average defect count during operation.
  - الموثوقية لأنها متوسط لعدد العيوب في المنتج.
- **C.** Mean time to failure, which counts input states exercised.
  - متوسط الزمن حتى الإخفاق لأنه يحصي حالات الإدخال.
- **D.** Input space, which measures failure chance per time.
  - فضاء الإدخال لأنه يقيس معدل الخطر لكل زمن.

**Answer:** A. Failure intensity, a rate describing risk at a given time.

**الإجابة:** A. شدة الإخفاق لأنها معدل خطر عند زمن محدد.

**Explanation:** Failure intensity is suited to a release objective stated as a risk rate at a point in testing.

**ملاحظة:** تلائم شدة الإخفاق هدف الإصدار المعبر عنه بمعدل الخطر عند نقطة من الاختبار.

### Q10 — Which measure is suited to combining component reliability values?

أي مقياس يلائم جمع قيم موثوقية المكونات؟

**Options / الخيارات**

- **A.** Calendar time is elapsed duration for testing staff.
  - الزمن التقويمي مدة العمل والموارد.
- **B.** Reliability is a probability under stated conditions.
  - الموثوقية احتمال في ظروف تشغيل محددة.
- **C.** Failure intensity is a time-based failure rate.
  - شدة الإخفاق معدل مرتبط بوحدة الزمن.
- **D.** Mean value is the expected cumulative failure count.
  - القيمة المتوسطة عدد الإخفاقات المتوقع.

**Answer:** B. Reliability is a probability under stated conditions.

**الإجابة:** B. الموثوقية احتمال في ظروف تشغيل محددة.

**Explanation:** Reliability is a probability measure that can be combined for system components using reliability theory.

**ملاحظة:** الموثوقية مقياس احتمالي يمكن دمجه لمكونات النظام وفق نظرية الموثوقية.

### Q11 — How can reliability studies help project management during testing?

كيف تساعد دراسات الموثوقية إدارة المشروع أثناء الاختبار؟

**Options / الخيارات**

- **A.** They replace project plans with counts of user requests.
  - تستبدل خطة المشروع بإحصاء طلبات المستخدمين.
- **B.** They guarantee that deployed software contains no faults.
  - تضمن خلو البرنامج المنشور من العيوب البرمجية.
- **C.** They guide release timing, schedule, and cost during testing.
  - تتابع تقدم الاختبار وتدعم قرارات الإصدار والكلفة.
- **D.** They estimate program size without observing test failures.
  - تقدر حجم البرنامج من دون رصد إخفاقات الاختبار.

**Answer:** C. They guide release timing, schedule, and cost during testing.

**الإجابة:** C. تتابع تقدم الاختبار وتدعم قرارات الإصدار والكلفة.

**Explanation:** Reliability measures help monitor test progress and relate release decisions to schedule and cost.

**ملاحظة:** تساعد مقاييس الموثوقية على متابعة الاختبار وربط قرارات الإصدار بالجدول والكلفة.

## B06 — Reliability Growth Models and Time Components

**الموضوع:** نماذج نمو الموثوقية ومكونات الزمن

### Q1 — What does NHPP mean in software reliability modeling?

ماذا يعني NHPP في نمذجة موثوقية البرمجيات؟

**Options / الخيارات**

- **A.** Nonhomogeneous Poisson Process model.
  - عملية بواسون غير المتجانسة.
- **B.** Nonlinear Hardware Performance Profile.
  - ملف أداء الأجهزة غير الخطي.
- **C.** Normalized Hazard Probability Pattern.
  - نمط احتمال الخطر المعياري.
- **D.** Nonparametric Human Process Prediction.
  - تنبؤ العملية البشرية اللامعلمي.

**Answer:** A. Nonhomogeneous Poisson Process model.

**الإجابة:** A. عملية بواسون غير المتجانسة.

**Explanation:** NHPP stands for Nonhomogeneous Poisson Process, whose failure intensity can change over time.

**ملاحظة:** يشير NHPP إلى عملية بواسون غير متجانسة يمكن أن تتغير شدة إخفاقها مع الزمن.

### Q2 — How does the Basic Execution Time Model relate intensity to failures experienced?

كيف يربط نموذج زمن التنفيذ الأساسي الشدة بالإخفاقات المرصودة؟

**Options / الخيارات**

- **A.** Intensity rises linearly as failures are experienced.
  - ترتفع الشدة خطياً مع الإخفاقات المرصودة.
- **B.** Intensity decreases linearly as failures are experienced.
  - تنخفض الشدة خطياً مع الإخفاقات المرصودة.
- **C.** Intensity decreases exponentially as time passes.
  - تنخفض الشدة أُسّياً مع مرور الزمن.
- **D.** Intensity stays constant until all faults are removed.
  - تبقى الشدة ثابتة حتى إزالة جميع العيوب.

**Answer:** B. Intensity decreases linearly as failures are experienced.

**الإجابة:** B. تنخفض الشدة خطياً مع الإخفاقات المرصودة.

**Explanation:** The basic model assumes a linear decrease in failure intensity as the expected failures experienced grow.

**ملاحظة:** يفترض النموذج الأساسي انخفاضاً خطياً في الشدة مع زيادة الإخفاقات المتوقعة المرصودة.

### Q3 — What does the Basic Execution Time Model assume about eventual failures?

ماذا يفترض نموذج زمن التنفيذ الأساسي بشأن الإخفاقات النهائية؟

**Options / الخيارات**

- **A.** Failure intensity is independent of failures already experienced.
  - لا تعتمد الشدة على الإخفاقات المرصودة سابقاً.
- **B.** Every input state produces the same number of failures.
  - تنتج كل حالة إدخال العدد نفسه من الإخفاقات.
- **C.** A finite expected failure population bounds the cumulative mean.
  - يقترب العدد التراكمي المتوقع من حد نهائي.
- **D.** The cumulative failure mean grows without any finite bound.
  - ينمو متوسط الإخفاقات التراكمي بلا حد نهائي.

**Answer:** C. A finite expected failure population bounds the cumulative mean.

**الإجابة:** C. يقترب العدد التراكمي المتوقع من حد نهائي.

**Explanation:** The basic model has a finite eventual failure population, so its cumulative mean approaches that limit.

**ملاحظة:** يفترض النموذج الأساسي عدداً نهائياً متوقعاً من الإخفاقات ويقترب المتوسط التراكمي منه.

### Q4 — Which operational-profile assumption accompanies the Basic Execution Time Model?

أي افتراض لملف التشغيل يصاحب نموذج زمن التنفيذ الأساسي؟

**Options / الخيارات**

- **A.** Run types have arbitrary probabilities that never affect failures.
  - تعطي أنواع التشغيل احتمالات لا تؤثر في الإخفاقات.
- **B.** Only the most common input state can activate a fault.
  - تفعّل حالة الإدخال الأشيع وحدها جميع العيوب.
- **C.** Fault removal occurs without any observed failure.
  - تزيل الاختبارات العيوب من دون رصد أي إخفاق.
- **D.** A uniform profile gives faults equal chances to manifest.
  - يمنح الملف الموحد كل عيب فرصة متساوية للظهور.

**Answer:** D. A uniform profile gives faults equal chances to manifest.

**الإجابة:** D. يمنح الملف الموحد كل عيب فرصة متساوية للظهور.

**Explanation:** The basic model implies a uniform operational profile, giving faults equal chances to manifest.

**ملاحظة:** يفترض النموذج الأساسي ملف تشغيل موحداً يمنح العيوب فرصاً متساوية للظهور.

### Q5 — What happens to failure intensity per additional failure in the Basic model?

ماذا يحدث لشدة الإخفاق مع كل إخفاق إضافي في النموذج الأساسي؟

**Options / الخيارات**

- **A.** It drops by a constant amount under the model assumptions.
  - تنخفض بمقدار ثابت وفق افتراضات النموذج.
- **B.** It drops by an amount that grows exponentially each time.
  - تنخفض بمقدار يزداد أُسّياً في كل مرة.
- **C.** It remains unchanged until the final fault is removed.
  - تبقى بلا تغير حتى إزالة العيب الأخير.
- **D.** It increases by the same amount after each failure.
  - ترتفع بالمقدار نفسه بعد كل إخفاق.

**Answer:** A. It drops by a constant amount under the model assumptions.

**الإجابة:** A. تنخفض بمقدار ثابت وفق افتراضات النموذج.

**Explanation:** A constant decrement in intensity per failure follows from the basic model's linear intensity relation.

**ملاحظة:** ينتج الانخفاض الثابت للشدة لكل إخفاق عن العلاقة الخطية في النموذج الأساسي.

### Q6 — How does the Logarithmic Poisson Model describe intensity as failures accumulate?

كيف يصف نموذج بواسون اللوغاريتمي الشدة مع تراكم الإخفاقات؟

**Options / الخيارات**

- **A.** Intensity rises exponentially after each fault is corrected.
  - ترتفع الشدة أُسّياً عند إصلاح العيب.
- **B.** Intensity declines exponentially as failures accumulate.
  - تتناقص الشدة أُسّياً مع الإخفاقات.
- **C.** Intensity declines linearly with calendar time observed.
  - تنخفض الشدة خطياً مع الأيام المقاسة.
- **D.** Intensity stays fixed while the expected failure count grows.
  - تبقى الشدة ثابتة مع نمو متوسط الإخفاقات.

**Answer:** B. Intensity declines exponentially as failures accumulate.

**الإجابة:** B. تتناقص الشدة أُسّياً مع الإخفاقات.

**Explanation:** In the logarithmic Poisson model, failure intensity decays exponentially as failures are experienced.

**ملاحظة:** تتناقص شدة الإخفاق أُسّياً مع الإخفاقات المرصودة في نموذج بواسون اللوغاريتمي.

### Q7 — What role does theta play in the Logarithmic Poisson Model?

ما دور theta في نموذج بواسون اللوغاريتمي؟

**Options / الخيارات**

- **A.** It measures the calendar time lost to staff shortages.
  - يقيس معامل theta وقت الاختبار المفقود بسبب نقص الموظفين.
- **B.** It counts the faults remaining after each test run.
  - يحصي معامل theta العيوب الباقية بعد كل تشغيل اختباري.
- **C.** It controls how quickly intensity decays per failure.
  - يحدد معامل theta سرعة تناقص الشدة لكل إخفاق مرصود.
- **D.** It gives the finite total number of eventual failures.
  - يعطي معامل theta عدداً ثابتاً للإخفاقات النهائية.

**Answer:** C. It controls how quickly intensity decays per failure.

**الإجابة:** C. يحدد معامل theta سرعة تناقص الشدة لكل إخفاق مرصود.

**Explanation:** Theta is the failure-intensity decay parameter in the logarithmic Poisson model.

**ملاحظة:** تمثل theta معامل تناقص شدة الإخفاق في نموذج بواسون اللوغاريتمي.

### Q8 — What long-run behavior does the Logarithmic Poisson Model allow for cumulative failures?

أي سلوك بعيد المدى يسمح به نموذج بواسون اللوغاريتمي للإخفاقات التراكمية؟

**Options / الخيارات**

- **A.** The cumulative mean stops at a fixed finite population.
  - يتوقف المتوسط التراكمي عند عدد ثابت ومحدود.
- **B.** The mean falls whenever one more failure is observed.
  - ينخفض المتوسط كلما رُصد إخفاق إضافي.
- **C.** The cumulative mean stays equal to the initial intensity.
  - يبقى المتوسط التراكمي مساوياً للشدة الأولية.
- **D.** The cumulative mean has no finite upper asymptote.
  - لا يملك المتوسط التراكمي حداً أعلى نهائياً.

**Answer:** D. The cumulative mean has no finite upper asymptote.

**الإجابة:** D. لا يملك المتوسط التراكمي حداً أعلى نهائياً.

**Explanation:** The logarithmic Poisson form has an unbounded cumulative mean, unlike a finite-population assumption.

**ملاحظة:** يملك نموذج بواسون اللوغاريتمي متوسطاً تراكمياً غير محدود بخلاف افتراض المجتمع المحدود.

### Q9 — Observed intensity falls roughly linearly with failures; which model form matches that pattern?

تنخفض الشدة المرصودة خطياً تقريباً مع الإخفاقات؛ أي نموذج يلائم النمط؟

**Options / الخيارات**

- **A.** The Basic Execution Time Model.
  - نموذج زمن التنفيذ الأساسي.
- **B.** The Logarithmic Poisson Model.
  - نموذج بواسون اللوغاريتمي.
- **C.** The Jelinski–Moranda Model only.
  - نموذج Jelinski–Moranda وحده.
- **D.** The Calendar Time Component Model only.
  - نموذج مكون الزمن التقويمي وحده.

**Answer:** A. The Basic Execution Time Model.

**الإجابة:** A. نموذج زمن التنفيذ الأساسي.

**Explanation:** The basic model expresses a linear intensity decrease as failures are experienced.

**ملاحظة:** يعبر النموذج الأساسي عن انخفاض خطي للشدة مع الإخفاقات المرصودة.

### Q10 — What mediates the relationship between execution time and calendar time?

ما الذي يتوسط العلاقة بين زمن التنفيذ والزمن التقويمي؟

**Options / الخيارات**

- **A.** The number of input states fixes the time required.
  - عدد حالات الإدخال يحدد زمن الاختبار الكلي.
- **B.** Testing effort links execution time to calendar duration.
  - جهد الاختبار يربط زمن التنفيذ بمدة التقويم.
- **C.** The product model's quality-factor count sets elapsed time.
  - عدد عوامل الجودة يحدد مدة تنفيذ الاختبار.
- **D.** The team's maturity level determines testing duration.
  - مرحلة نضج الفريق تحدد مدة الاختبار المطلوبة.

**Answer:** B. Testing effort links execution time to calendar duration.

**الإجابة:** B. جهد الاختبار يربط زمن التنفيذ بمدة التقويم.

**Explanation:** Calendar-time progress depends on testing resources and the effort required as execution proceeds.

**ملاحظة:** يعتمد التقدم بالزمن التقويمي على موارد الاختبار والجهد اللازم مع تقدم التنفيذ.

### Q11 — Testing needs more calendar time despite adequate CPU capacity; what may explain the delay?

يحتاج الاختبار زمناً تقويمياً أطول رغم كفاية المعالج؛ ما سبب التأخير المحتمل؟

**Options / الخيارات**

- **A.** The operational profile contains fewer possible inputs.
  - يضم ملف التشغيل حالات إدخال أقل من المعتاد.
- **B.** The software has reached a higher CMM maturity level.
  - وصل فريق البرمجيات إلى مستوى أعلى في CMM.
- **C.** Personnel or other testing resources limit progress.
  - تحد قلة الموظفين أو الموارد تقدم الاختبار.
- **D.** The processor has stopped measuring execution time.
  - يتوقف المعالج عن احتساب زمن تنفيذ البرنامج.

**Answer:** C. Personnel or other testing resources limit progress.

**الإجابة:** C. تحد قلة الموظفين أو الموارد تقدم الاختبار.

**Explanation:** The calendar-time component accounts for resource limitations, including testing personnel.

**ملاحظة:** يأخذ مكون الزمن التقويمي قيود الموارد بالحسبان، ومنها موظفو الاختبار.

### Q12 — How does Jelinski–Moranda relate failure intensity to remaining faults?

كيف يربط Jelinski–Moranda شدة الإخفاق بالعيوب الباقية؟

**Options / الخيارات**

- **A.** Intensity is proportional to the calendar time already elapsed.
  - تتناسب الشدة مع الزمن التقويمي المنقضي.
- **B.** Intensity is independent of the faults removed so far.
  - لا تعتمد الشدة على العيوب التي أزيلت.
- **C.** Intensity equals the number of input states exercised.
  - تساوي الشدة عدد حالات الإدخال المنفذة.
- **D.** Intensity depends on the estimated faults still remaining.
  - تتناسب الشدة مع عدد العيوب المقدّر بقاؤها.

**Answer:** D. Intensity depends on the estimated faults still remaining.

**الإجابة:** D. تتناسب الشدة مع عدد العيوب المقدّر بقاؤها.

**Explanation:** The Jelinski–Moranda intensity depends on the estimated number of faults not yet removed.

**ملاحظة:** تعتمد شدة Jelinski–Moranda على العدد المقدّر للعيوب التي لم تُزل بعد.

### Q13 — Why does Jelinski–Moranda intensity change after a fault-caused failure is removed?

لماذا تتغير شدة Jelinski–Moranda بعد إزالة عيب تسبب بإخفاق؟

**Options / الخيارات**

- **A.** The estimated remaining fault count decreases by one.
  - ينخفض عدد العيوب الباقية واحداً.
- **B.** The operational profile becomes uniform automatically.
  - يصبح ملف التشغيل موحداً تلقائياً.
- **C.** Calendar time is replaced by processor time.
  - يحل زمن المعالج محل الزمن التقويمي.
- **D.** The model's total fault population increases.
  - يزداد مجتمع العيوب الكلي في النموذج.

**Answer:** A. The estimated remaining fault count decreases by one.

**الإجابة:** A. ينخفض عدد العيوب الباقية واحداً.

**Explanation:** Removing a fault reduces the remaining-fault term that determines the next interval's intensity.

**ملاحظة:** تقلل إزالة العيب حد العيوب الباقية الذي يحدد شدة الفترة التالية.

### Q14 — How does bug seeding estimate the indigenous fault population?

كيف يقدّر نموذج بذر الأخطاء مجتمع العيوب الأصلية؟

**Options / الخيارات**

- **A.** It imports a hardware component's failure rate.
  - يستخدم معدل إخفاق مكوّن من أجهزة أخرى.
- **B.** It compares detected seeded and indigenous faults.
  - يقارن العيوب المزروعة والأصلية المكتشفة.
- **C.** It counts discovered faults without labeling seeded ones.
  - يحصي العيوب المكتشفة دون تمييز المزروع منها.
- **D.** It compares run time before and after each code change.
  - يقارن زمن التنفيذ قبل تغيير الشفرة وبعده.

**Answer:** B. It compares detected seeded and indigenous faults.

**الإجابة:** B. يقارن العيوب المزروعة والأصلية المكتشفة.

**Explanation:** Bug seeding uses the detected seeded-to-indigenous ratio to estimate faults that remain undiscovered.

**ملاحظة:** يستخدم بذر الأخطاء نسبة العيوب المزروعة إلى الأصلية المكتشفة لتقدير العيوب غير المكتشفة.

### Q15 — Which assumption is needed for bug-seeding estimates to be credible?

أي افتراض يلزم لمصداقية تقدير نموذج بذر الأخطاء؟

**Options / الخيارات**

- **A.** Every indigenous fault causes exactly one observed failure.
  - يسبب كل عيب أصلي إخفاقاً مرصوداً واحداً بالضبط.
- **B.** Testers know the location of every hidden fault in advance.
  - يعرف المختبرون مسبقاً مواقع جميع العيوب الخفية.
- **C.** Seeded and indigenous faults have comparable chances of detection.
  - تتقارب فرص اكتشاف العيوب المزروعة والأصلية.
- **D.** Seeded faults are always easier to detect than indigenous faults.
  - يسهل دائماً اكتشاف العيوب المزروعة أكثر من الأصلية.

**Answer:** C. Seeded and indigenous faults have comparable chances of detection.

**الإجابة:** C. تتقارب فرص اكتشاف العيوب المزروعة والأصلية.

**Explanation:** The estimate relies on comparable detection probabilities for seeded and indigenous faults.

**ملاحظة:** يعتمد التقدير على تقارب احتمالات اكتشاف العيوب المزروعة والأصلية.

## B07 — ISO 9000 and CMM Comparison

**الموضوع:** مقارنة ISO 9000 وCMM

### Q1 — What is the ISO 9000 series primarily concerned with?

بماذا تعنى سلسلة ISO 9000 أساساً؟

**Options / الخيارات**

- **A.** Quality-management and quality-assurance standards.
  - معايير مترابطة لإدارة الجودة وضمانها.
- **B.** A staged model of software process maturity.
  - نموذج مرحلي لنضج عمليات تطوير البرمجيات.
- **C.** A family of software product reliability models.
  - مجموعة نماذج لموثوقية المنتجات البرمجية.
- **D.** A collection of input profiles for software testing.
  - مجموعة ملفات لتمثيل مدخلات اختبار البرمجيات.

**Answer:** A. Quality-management and quality-assurance standards.

**الإجابة:** A. معايير مترابطة لإدارة الجودة وضمانها.

**Explanation:** ISO 9000 is a related series of standards dealing with quality management and assurance.

**ملاحظة:** ISO 9000 سلسلة معايير مترابطة تعنى بإدارة الجودة وضمانها.

### Q2 — What role does ISO 9001 play within the ISO 9000 series?

ما دور ISO 9001 ضمن سلسلة ISO 9000؟

**Options / الخيارات**

- **A.** It estimates failure intensity during program execution.
  - يقدر شدة إخفاق البرمجيات خلال التنفيذ.
- **B.** It specifies requirements for a quality-management system.
  - يحدد متطلبات نظام الجودة وإدارته داخل المؤسسة.
- **C.** It ranks organizations by software maturity level.
  - يرتب المؤسسات بمستويات نضج عملية البرمجيات.
- **D.** It defines software product quality characteristics.
  - يحدد خصائص جودة المنتج في الأنظمة البرمجية.

**Answer:** B. It specifies requirements for a quality-management system.

**الإجابة:** B. يحدد متطلبات نظام الجودة وإدارته داخل المؤسسة.

**Explanation:** ISO 9001 is the quality-system standard in the series most directly applied to development organizations.

**ملاحظة:** يمثل ISO 9001 معيار نظام الجودة الأوثق صلة بمؤسسات التطوير ضمن السلسلة.

### Q3 — What does ISO 9000-3 provide in software quality management?

ماذا يقدم ISO 9000-3 لإدارة جودة البرمجيات؟

**Options / الخيارات**

- **A.** A five-level scale for measuring process maturity.
  - مقياساً من خمسة مستويات لقياس نضج العملية.
- **B.** A model for estimating software failure intensity.
  - نموذجاً لتقدير شدة إخفاق البرمجيات.
- **C.** Guidance for applying ISO 9001 to software development.
  - إرشادات لتطبيق ISO 9001 على تطوير البرمجيات.
- **D.** A replacement for ISO 9001's quality-system requirements.
  - بديلاً عن متطلبات نظام الجودة في ISO 9001.

**Answer:** C. Guidance for applying ISO 9001 to software development.

**الإجابة:** C. إرشادات لتطبيق ISO 9001 على تطوير البرمجيات.

**Explanation:** ISO 9000-3 gives software-specific guidance for applying the broader ISO 9001 requirements.

**ملاحظة:** يقدم ISO 9000-3 إرشادات خاصة بالبرمجيات لتطبيق متطلبات ISO 9001 الأوسع.

### Q4 — In a 20-clause ISO 9001 version, what do the clauses collectively specify?

في إصدار ISO 9001 ذي البنود العشرين، ماذا تحدد البنود مجتمعة؟

**Options / الخيارات**

- **A.** A five-stage path for software-process maturity.
  - تتابع مراحل نضج عملية تطوير البرمجيات.
- **B.** A hierarchy of quality attributes for software products.
  - هرم يضم خصائص جودة المنتجات البرمجية.
- **C.** Equations for estimating failure rates during testing.
  - معادلات لقياس معدل الإخفاق أثناء الاختبار.
- **D.** Requirements for an organization's quality system.
  - متطلبات نظام الجودة وإدارته داخل المؤسسة.

**Answer:** D. Requirements for an organization's quality system.

**الإجابة:** D. متطلبات نظام الجودة وإدارته داخل المؤسسة.

**Explanation:** The clause count belongs to a specific edition; the clauses describe quality-system requirements.

**ملاحظة:** يرتبط عدد البنود بإصدار محدد، وتصف البنود متطلبات نظام الجودة.

### Q5 — Which scope contrast between ISO 9001 and CMM is accurate?

أي فرق في النطاق بين ISO 9001 وCMM دقيق؟

**Options / الخيارات**

- **A.** ISO 9001 is broad; CMM focuses on software-process maturity.
  - نطاق ISO 9001 واسع، ويركز CMM على نضج عملية البرمجيات.
- **B.** ISO 9001 is software-only; CMM applies to all industries.
  - يقتصر ISO 9001 على البرمجيات، ويشمل CMM الصناعات كلها.
- **C.** Both standards apply only to hardware manufacturing.
  - يقتصر المعياران على إجراءات تصنيع الأجهزة فقط.
- **D.** CMM specifies quality-system certification for every product.
  - يمنح CMM اعتماد جودة لجميع المنتجات البرمجية.

**Answer:** A. ISO 9001 is broad; CMM focuses on software-process maturity.

**الإجابة:** A. نطاق ISO 9001 واسع، ويركز CMM على نضج عملية البرمجيات.

**Explanation:** ISO 9001 applies across sectors, whereas CMM provides a software-process maturity framework.

**ملاحظة:** يطبق ISO 9001 على قطاعات واسعة، بينما يقدم CMM إطاراً لنضج عملية البرمجيات.

### Q6 — Which emphasis most clearly distinguishes CMM from ISO 9001?

أي اهتمام يميز CMM بوضوح عن ISO 9001؟

**Options / الخيارات**

- **A.** ISO 9001 defines a five-stage maturity progression.
  - يحدد ISO 9001 تدرجاً من خمس مراحل للنضج.
- **B.** CMM emphasizes continuous software-process improvement.
  - يركز CMM على التحسين المستمر لعملية البرمجيات.
- **C.** CMM emphasizes product certification for all industries.
  - يركز CMM على اعتماد المنتجات في الصناعات كلها.
- **D.** ISO 9001 measures software faults after every execution.
  - يقيس ISO 9001 عيوب البرمجيات بعد كل تشغيل.

**Answer:** B. CMM emphasizes continuous software-process improvement.

**الإجابة:** B. يركز CMM على التحسين المستمر لعملية البرمجيات.

**Explanation:** The CMM places strong emphasis on continuous process improvement; ISO 9001 specifies an acceptable quality system.

**ملاحظة:** يركز CMM بقوة على التحسين المستمر، بينما يحدد ISO 9001 نظام جودة مقبولاً.

### Q7 — Which principle is shared by ISO 9001 and CMM?

أي مبدأ مشترك بين ISO 9001 وCMM؟

**Options / الخيارات**

- **A.** Use the same software process in every industry.
  - استخدم إجراءً واحداً في كل قطاعات الصناعة.
- **B.** Guarantee that every delivered program has no faults.
  - اضمن خلو كل برنامج من العيوب بعد التسليم.
- **C.** Document the process and follow it as documented.
  - وثق العملية ونفذ العمل بما يطابق توثيقها.
- **D.** Replace all process records with product inspections.
  - استبدل سجلات العملية بفحص المنتج النهائي.

**Answer:** C. Document the process and follow it as documented.

**الإجابة:** C. وثق العملية ونفذ العمل بما يطابق توثيقها.

**Explanation:** Both approaches emphasize documented processes and work that matches them.

**ملاحظة:** تقدر المقاربتان توثيق العمليات وتنفيذ العمل وفقاً لها.

### Q8 — Which CMM practice area most directly supports ISO 9001 document control?

أي مجال في CMM يدعم ضبط الوثائق وفق ISO 9001 مباشرة؟

**Options / الخيارات**

- **A.** Software Subcontract Management practices.
  - إدارة التعاقدات البرمجية.
- **B.** Software Project Planning activities.
  - تخطيط مشروع البرمجيات.
- **C.** Software Product Engineering practices.
  - هندسة المنتج البرمجي.
- **D.** Software Configuration Management processes.
  - إدارة تهيئة البرمجيات.

**Answer:** D. Software Configuration Management processes.

**الإجابة:** D. إدارة تهيئة البرمجيات.

**Explanation:** CMM configuration-management practices control the distribution and modification of documents.

**ملاحظة:** تضبط ممارسات إدارة التهيئة توزيع الوثائق وتعديلها.

### Q9 — Which CMM common feature most directly supports ISO 9001 quality audits?

أي خاصية مشتركة في CMM تدعم تدقيق الجودة وفق ISO 9001 مباشرة؟

**Options / الخيارات**

- **A.** Verifying Implementation, through reviews and audits.
  - التحقق من التنفيذ عبر المراجعات والتدقيق.
- **B.** Ability to Perform, through staff and tools.
  - القدرة على الأداء عبر الموارد والتدريب.
- **C.** Activities Performed, through plans and work products.
  - الأنشطة المنفذة عبر الخطط ومخرجات العمل.
- **D.** Commitment to Perform, through management policy.
  - الالتزام بالأداء عبر السياسة والدعم الإداري.

**Answer:** A. Verifying Implementation, through reviews and audits.

**الإجابة:** A. التحقق من التنفيذ عبر المراجعات والتدقيق.

**Explanation:** The Verifying Implementation feature uses reviews and audits to check adherence to established practice.

**ملاحظة:** تستخدم خاصية التحقق من التنفيذ المراجعات والتدقيق لفحص الالتزام بالممارسة المقررة.

### Q10 — What does ISO 9001 certification establish most directly?

ماذا يثبت اعتماد ISO 9001 مباشرة؟

**Options / الخيارات**

- **A.** That every project follows identical technical methods.
  - اتباع كل مشروع أساليب تقنية متطابقة.
- **B.** The quality system's conformance to specified requirements.
  - مطابقة نظام الجودة لمتطلبات محددة.
- **C.** That the software contains no faults in operation.
  - خلو البرمجيات من العيوب أثناء التشغيل.
- **D.** That the organization has reached CMM's highest level.
  - بلوغ المؤسسة أعلى مستوى في CMM.

**Answer:** B. The quality system's conformance to specified requirements.

**الإجابة:** B. مطابقة نظام الجودة لمتطلبات محددة.

**Explanation:** Certification concerns the quality system's conformance; it is not proof of fault-free software or CMM maturity.

**ملاحظة:** يتعلق الاعتماد بمطابقة نظام الجودة، ولا يثبت خلو البرمجيات من العيوب أو مستوى نضج CMM.

### Q11 — An organization seeks software-process improvement but also faces a buyer's certification requirement; which choice is sound?

تسعى مؤسسة لتحسين عملية البرمجيات وتواجه شرط اعتماد من مشترٍ؛ أي اختيار سليم؟

**Options / الخيارات**

- **A.** Use CMM maturity as a substitute for every market certificate.
  - استخدم نضج CMM بديلاً لكل اعتماد سوقي.
- **B.** Choose either approach because both guarantee defect-free products.
  - اخترهما لأن كليهما يضمن خلو المنتج من العيوب.
- **C.** Use CMM to guide improvement and meet required ISO certification.
  - استخدم CMM للتحسين ونفذ اعتماد ISO المطلوب.
- **D.** Use ISO certification alone as proof of continuous improvement.
  - استخدم اعتماد ISO لإثبات التحسين المستمر.

**Answer:** C. Use CMM to guide improvement and meet required ISO certification.

**الإجابة:** C. استخدم CMM للتحسين ونفذ اعتماد ISO المطلوب.

**Explanation:** CMM can structure software-process improvement, while a market may separately require ISO 9001 certification.

**ملاحظة:** يمكن لـCMM تنظيم تحسين عملية البرمجيات، وقد يتطلب السوق اعتماد ISO 9001 أيضاً.
