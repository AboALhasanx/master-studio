# ASE Chapter 6 — Question Bank Review

> English stems and options are shown with their Arabic counterparts. The keyed choice is marked **Correct**.
> Source boundaries and corrections are documented in `Ch06_Bank_Coverage_Audit.md`.

## T01 — Measurement Fundamentals

Bank file: `Quiz_Ch06_T01_Measurement_Fundamentals.json`

### q1 · `ch6_measurement_purpose` · Understand

Which set best reflects questions software measurement can help address?

**العربية:** أي مجموعة تمثل أسئلة يمكن أن يساعد قياس البرمجيات في الإجابة عنها؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Estimate size, cost, likely defects, and release readiness | تقدير حجم النظام والكلفة والعيوب المتوقعة وجاهزية الإصدار |
| B | Describe morale, office layout, and employee meeting preferences | وصف معنويات الفريق وتصميم المكتب ومواعيد لقاء الموظفين |
| C | Choose product names, sales slogans, and customer advertising channels | اختيار أسماء المنتجات وشعارات البيع وقنوات الإعلان للعملاء |
| D | Plan hardware prices, hiring rules, and company reporting lines | تخطيط أسعار العتاد وقواعد التوظيف والتقارير الإدارية |

**Explanation:** Software measurement can inform estimates of size and cost, expected defects, testing, and release decisions; the alternatives concern matters outside product, process, or project attributes.

**ملاحظة:** يساعد القياس في تقدير الحجم والكلفة والعيوب والاختبار وقرار الإصدار؛ أما الخيارات الأخرى فلا تمثل أسئلة البرمجيات الواردة في هذا المحور.

### q2 · `ch6_measurement_vs_metric` · Understand

What is measurement in software engineering?

**العربية:** ما المقصود بالقياس وفق تعريفات المقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | A chosen property of the product | خاصية محددة في المنتج |
| B **Correct** | The act of determining a measure | هي عملية تحديد المقياس |
| C | An estimate of development effort | تقدير كمي لجهد التطوير |
| D | An interpretation of measured results | تفسير نتائج القياس |

**Explanation:** Measurement is the act of determining a measure; an attribute is observed, while a metric quantifies the degree of an attribute.

**ملاحظة:** القياس هو عملية تحديد مقياس؛ أما الخاصية فتُلاحظ، ويعبّر المقياس الكمي عن درجتها.

### q3 · `ch6_indirect_measure` · Understand

Which statement best describes an indirect software measure?

**العربية:** أي عبارة تصف مقياساً غير مباشر للبرمجيات؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | It counts an attribute directly using an agreed rule | يرصد الخاصية مباشرةً وفق قاعدة متفق عليها |
| B | It records the software entity being measured | يسجل الكيان البرمجي الذي يجري قياسه |
| C **Correct** | It derives an attribute from related measures | يقدّر الخاصية من مقاييس مرتبطة بها |
| D | It sets the planned release date for a product | يحدد موعد الإصدار المخطط للمنتج البرمجي |

**Explanation:** An indirect measure derives an attribute from related measures, whereas a direct measure counts or observes it directly.

**ملاحظة:** يستنتج المقياس غير المباشر الخاصية من مقاييس مرتبطة، بينما يرصدها المقياس المباشر أو يعدّها مباشرة.

### q4 · `ch6_measurement_entity` · Understand

In software measurement, what is an entity?

**العربية:** ما المقصود بالكيان في قياس البرمجيات؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | A numeric scale for recording software observations | سلم عددي لتسجيل ملاحظات النظام البرمجي |
| B | A formula for combining several measured values | صيغة حسابية تجمع مقاييس مختلفة |
| C | A management target for tracking project progress | هدف إداري لمتابعة أداء المشروع |
| D **Correct** | The product, component, or process being examined | العنصر أو العملية محل فحص الخصائص |

**Explanation:** The entity is what is examined, such as a product, component, or process; its attribute is the property being measured.

**ملاحظة:** الكيان هو ما يجري فحصه، مثل المنتج أو المكوّن أو العملية؛ أما الخاصية فهي الجانب الذي يُقاس.

### q5 · `ch6_ratio_scale` · Understand

Which property distinguishes a ratio scale from an interval scale?

**العربية:** أي خاصية تميز المقياس النسبي عن المقياس الفتري؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Equal intervals with a meaningful true zero | فواصل متساوية مع صفر حقيقي ذي معنى |
| B | Named categories without an ordering relationship | فئات مسماة من دون أي ترتيب بينها |
| C | Ranked values without equal intervals between them | قيم مرتبة بفواصل غير متساوية بينها |
| D | Equal intervals without a meaningful zero point | فواصل متساوية من دون صفر حقيقي ذي معنى |

**Explanation:** A ratio scale has equal intervals and a meaningful zero; an interval scale lacks a meaningful true zero.

**ملاحظة:** للمقياس النسبي فواصل متساوية وصفر حقيقي ذو معنى، بخلاف المقياس الفتري الذي يفتقد صفراً حقيقياً ذا معنى.

### q6 · `ch6_meaningful_measurement` · Analyze

When is a conclusion based on a measurement considered meaningful?

**العربية:** متى يكون الاستنتاج المبني على القياس ذا معنى؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Every scale uses the same numeric labels | تستعمل المقاييس جميعها التسميات العددية نفسها |
| B **Correct** | It holds under allowed transformations of the scale | صحة الاستنتاج مع التحويلات المسموحة للمقياس |
| C | Measured values are whole numbers without fractions | تكون القيم المقاسة أعداداً صحيحة دون كسور |
| D | The sample contains more observations than another | تضم العينة عدداً أكبر من المشاهدات مقارنة بغيرها |

**Explanation:** Measurement theory requires conclusions to respect the scale's admissible transformations; identical labels or integer values do not establish validity.

**ملاحظة:** تتطلب نظرية القياس أن تحترم الاستنتاجات التحويلات المقبولة للمقياس؛ فتطابق التسميات أو كون القيم صحيحة لا يثبت صلاحية الاستنتاج.

### q7 · `ch6_gqm_sequence` · Understand

What is the intended order in the Goal–Question–Metric approach?

**العربية:** ما الترتيب المقصود في منهج Goal–Question–Metric؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Choose metrics, then write questions and goals | اختيار المقاييس ثم صياغة الأسئلة والأهداف |
| B | List data, then select tools and improvement targets | حصر البيانات ثم اختيار الأدوات وأهداف التحسين |
| C **Correct** | Set a goal, derive questions, then choose metrics | تحديد الهدف ثم الأسئلة ثم اختيار المقاييس |
| D | Collect values, then report averages and state a goal | جمع القيم ثم عرض المتوسطات وصياغة هدف |

**Explanation:** GQM starts with a measurement goal, derives questions that characterize it, and chooses metrics that answer those questions.

**ملاحظة:** يبدأ GQM بهدف للقياس، ثم يشتق أسئلة توضحه، وبعدها يختار مقاييس تجيب عن تلك الأسئلة.

### q8 · `ch6_metric_definition` · Understand

Which statement best defines a software metric?

**العربية:** أي عبارة تقدم أفضل تعريف لمقياس البرمجيات في مادة المقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | The unit for measuring source-code size | وحدة عددية لقياس حجم الشيفرة المصدرية |
| B | The act of assigning a manager to a software task | تعيين مدير لمهمة تطوير برمجية محددة |
| C | Requirements awaiting customer review and approval | متطلبات بانتظار مراجعة العميل واعتمادها |
| D **Correct** | A quantitative measure of an attribute's degree | مقياس كمي لدرجة امتلاك خاصية برمجية |

**Explanation:** A metric quantifies the degree to which a system, component, or process possesses an attribute; the other choices describe unrelated activities or artifacts.

**ملاحظة:** يعبّر المقياس كمياً عن درجة امتلاك نظام أو مكوّن أو عملية لخاصية؛ أما الخيارات الأخرى فتصف أنشطة أو مخرجات مختلفة.

### q9 · `ch6_measurement_applications` · Understand

Which group contains established applications of software metrics?

**العربية:** أي مجموعة تضم مجالات راسخة لاستخدام مقاييس البرمجيات؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Estimate size and cost, predict quality, and check design | تقدير الحجم والكلفة والتنبؤ بالجودة والفحص الكمي للتصميم |
| B | Choose product names, plan offices, and negotiate salaries | اختيار أسماء المنتجات وتخطيط المكاتب والتفاوض على الرواتب |
| C | Buy hardware, promote staff, and forecast sales | شراء العتاد وترقية الموظفين والتنبؤ بالمبيعات |
| D | Schedule meetings, assign seats, and style documents | جدولة الاجتماعات وتوزيع المقاعد وتنسيق المستندات |

**Explanation:** Measurement supports estimation, quality prediction, and quantitative design checks; the alternatives are not common software-measurement goals.

**ملاحظة:** يحدد المقرر التقدير والتنبؤ بالجودة والفحوص الكمية للتصميم مجالات راسخة؛ أما المجموعات الأخرى فلا تمثل استخدامات مقاييس البرمجيات الواردة.

### q10 · `ch6_implementation_resistance` · Analyze

What concern can arise when introducing software measurement?

**العربية:** ما عقبة تطبيقية توضحها أمثلة المقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | No software properties can be observed or described | تعذر رصد خصائص المنتج البرمجي وقياسها |
| B **Correct** | Teams may resist quantitative oversight of software work | قد ترفض الفرق قياس أعمال البرمجيات كمياً |
| C | Project effort and delivery dates cannot be recorded | يتعذر تسجيل جهد المشروع ومواعيد التسليم |
| D | Every measured property must share one common unit | يجب توحيد الوحدة المستخدمة لكل خاصية مقاسة |

**Explanation:** Software teams may experience tension with managerial expectations about control, delays, and reliability constraints; that does not make measurement impossible.

**ملاحظة:** قد ينشأ توتر بين فرق البرمجيات وتوقعات الإدارة بشأن الضبط والتأخر وقيود الاعتمادية؛ وهذا لا يجعل القياس مستحيلاً.

## T02 — Software Metric Categories

Bank file: `Quiz_Ch06_T02_Metric_Categories.json`

### q1 · `ch6_product_metric` · Understand

Which observation is a product metric?

**العربية:** أي ملاحظة تمثل مقياساً للمنتج؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Product size, complexity, and reliability characteristics | خصائص حجم المنتج وتعقيده واعتماديته |
| B | Development effort, time, and defect-removal effectiveness | جهد التطوير ووقته وفاعلية إزالة العيوب |
| C | Staffing, project cost, schedule, and developer productivity | نمط التوظيف وكلفة المشروع وجدوله |
| D | Process maturity and testing-defect effectiveness | نضج العملية وفاعلية كشف عيوب الاختبار |

**Explanation:** Product metrics describe product characteristics such as size, complexity, performance, and reliability; the alternatives describe process or project properties.

**ملاحظة:** تصف مقاييس المنتج خصائصه مثل الحجم والتعقيد والأداء والاعتمادية؛ أما البدائل فتصف العملية أو المشروع.

### q2 · `ch6_process_metric` · Understand

Which set consists of process metrics?

**العربية:** أي مجموعة تتكون من مقاييس العملية وفق تصنيف المقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Product size, reliability, portability, and performance | حجم المنتج واعتماديته وقابليته للنقل وأداؤه |
| B **Correct** | Effort, time, defect removal, and process maturity | الجهد والوقت وإزالة العيوب ونضج العملية |
| C | Developer count, staffing, cost, and schedule | عدد المطورين ونمط التوظيف والكلفة والجدول |
| D | Class depth, method count, and object coupling | عمق الأصناف وعدد الطرق واقتران الكائنات |

**Explanation:** Process measures include effort, time, defect-removal effectiveness, testing defects, and maturity; the alternatives describe product or project data.

**ملاحظة:** يورد المقرر الجهد والوقت وفاعلية إزالة العيوب وعيوب الاختبار والنضج ضمن مقاييس العملية؛ أما البدائل فتصف بيانات المنتج أو المشروع.

### q3 · `ch6_project_metric` · Understand

Which observation is classified as a project metric?

**العربية:** أي ملاحظة تصنف مقياساً للمشروع؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | The source code's size and structural complexity | حجم الشيفرة وتعقيد بنية المنتج |
| B | The effectiveness of removing defects during development | فاعلية عملية إزالة عيوب البرمجيات |
| C **Correct** | Project staffing patterns, cost, and schedules | نمط التوظيف وجدول العمل للمشروع |
| D | The delivered product's reliability and portability | اعتمادية المنتج وقابليته للنقل |

**Explanation:** Project metrics describe project execution, including staffing, cost, schedule, and productivity; the other choices describe product or process characteristics.

**ملاحظة:** تصف مقاييس المشروع تنفيذه، بما في ذلك التوظيف والكلفة والجدول والإنتاجية؛ أما البدائل فتصف المنتج أو العملية.

### q4 · `ch6_internal_external_attribute` · Understand

Which distinction separates an internal attribute from an external one?

**العربية:** أي تمييز يفصل الخاصية الداخلية عن الخارجية؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Internal describes cost; external describes project staffing | تصف الداخلية كلفة المشروع، والخارجية نمط التوظيف |
| B | Internal describes process activity; external describes product reliability | تصف الداخلية نشاط العملية، والخارجية اعتمادية المنتج |
| C | Internal describes prediction; external describes project control | تصف الداخلية التنبؤ، والخارجية ضبط تقدم المشروع |
| D **Correct** | Internal describes product structure; external describes behavior in use | الداخلية بنية المنتج، والخارجية سلوكه عند الاستخدام |

**Explanation:** Internal attributes are assessed from the software product itself, while external attributes concern its behavior or effects in its operating context.

**ملاحظة:** تُقيّم الخصائص الداخلية من المنتج البرمجي نفسه، بينما تتعلق الخصائص الخارجية بسلوكه أو أثره في بيئة تشغيله.

### q5 · `ch6_predictor_metric` · Understand

What is the role of a predictor metric?

**العربية:** ما دور المقياس التنبؤي؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Uses a related measure to estimate an attribute | يستعمل مقياساً مرتبطاً لتقدير الخاصية |
| B | Records actual progress against the project plan | يسجل التقدم المحقق مقارنة بخطة المشروع |
| C | Classifies an artifact into a software category | يصنف مخرجاً ضمن فئات برمجية محددة |
| D | States the exact value of every future outcome | يحدد القيمة الدقيقة لكل نتيجة مستقبلية |

**Explanation:** A predictor is selected for its relationship with an attribute to be estimated; recording progress against a plan is a control use, not prediction.

**ملاحظة:** يُختار المقياس التنبؤي لارتباطه بخاصية يراد تقديرها؛ أما تسجيل التقدم مقابل الخطة فهو استخدام ضبطي لا تنبؤي.

### q6 · `ch6_control_metric` · Understand

A manager tracks actual effort against the approved plan. What is the metric's role?

**العربية:** يتابع مدير الجهد الفعلي مقارنة بالخطة المعتمدة؛ ما دور المقياس هنا؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Predicts product reliability before release | يتنبأ باعتمادية المنتج قبل الإصدار |
| B **Correct** | Tracks project progress against an approved plan | يتابع تقدم المشروع مقارنة بالخطة |
| C | Describes product behavior during operation | يصف سلوك المنتج عند استعماله |
| D | Counts functions visible to the delivered product's users | يعدّ الوظائف الظاهرة لمستخدمي المنتج |

**Explanation:** Control metrics help monitor the process or project against its plan; predicting reliability or measuring functionality are different roles.

**ملاحظة:** تساعد المقاييس الضبطية على متابعة العملية أو المشروع مقابل خطته؛ أما التنبؤ بالاعتمادية أو قياس الوظائف فلهما دور مختلف.

### q7 · `ch6_metric_category_vs_role` · Analyze

What do the labels product, process, and project classify?

**العربية:** ماذا تصنف التسميات product وprocess وproject؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | The metric's predictive or control role | هل يتنبأ المقياس أم يتابع تقدم العمل؟ |
| B | The permitted transformation of its numeric scale | تحويل المقياس المسموح به لقيمه |
| C **Correct** | The object or activity a metric describes | الشيء أو النشاط الذي يصفه المقياس |
| D | The programming language used to collect measures | لغة جمع القياس في نظام البرمجيات |

**Explanation:** Product, process, and project identify what is being described; predictor and control identify how the metric is used.

**ملاحظة:** تحدد product وprocess وproject ما الذي يصفه المقياس؛ أما predictor وcontrol فيحددان طريقة استخدامه.

### q8 · `ch6_category_role_axes` · Analyze

How should a metric's category and its management role be recorded?

**العربية:** كيف ينبغي تسجيل تصنيف المقياس ودوره الإداري؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Interchangeable names for a single metric category | التصنيف والدور اسمان متبادلان لنوع مقياس واحد |
| B | Labels that determine which numeric operations are meaningful | التصنيف والدور تسميتان للعمليات العددية ذات المعنى |
| C | Names for lifecycle phases that cannot overlap | التصنيف والدور تسميتان لمراحل دورة حياة لا تتداخل |
| D **Correct** | Separate labels describing different aspects of a metric | التصنيف والدور يصفان جانبين مختلفين للمقياس |

**Explanation:** Category and role answer different questions: what is measured and whether the measure is used to predict or control.

**ملاحظة:** يجيب التصنيف والدور عن سؤالين مختلفين: ما الذي يُقاس، وهل يُستخدم المقياس للتنبؤ أم للضبط.

## T03 — Software Size Metrics

Bank file: `Quiz_Ch06_T03_Software_Size_Metrics.json`

### q1 · `ch6_loc_counting_rule` · Understand

Under Conte's LOC definition, which lines are counted?

**العربية:** وفق تعريف Conte لـLOC، أي الأسطر تُحسب؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Nonblank, noncomment lines, including declarations | الأسطر غير الفارغة وغير التعليقية مع التصريحات |
| B | Executable lines alone, excluding declarations and headers | الأسطر التنفيذية وحدها دون تصريحات أو ترويسات |
| C | Every physical line, including comments and blank lines | كل أسطر المصدر بما فيها التعليقات والفراغات |
| D | Only lines containing one complete executable statement | الأسطر التي تحتوي تعليمة تنفيذية كاملة واحدة فقط |

**Explanation:** Conte's predominant research definition excludes blank and comment lines but includes headers, declarations, and executable or nonexecutable program text.

**ملاحظة:** يستبعد تعريف Conte السائد في البحوث الأسطر الفارغة والتعليقات، لكنه يشمل الترويسات والتصريحات والنص البرمجي التنفيذي وغير التنفيذي.

### q2 · `ch6_loc_counting_convention` · Analyze

Why must an LOC count state its counting convention?

**العربية:** لماذا يجب أن يحدد عدّ LOC قاعدة العد المستعملة؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | LOC is calculated from the program's runtime failure rate | يحسب LOC من معدل إخفاق البرنامج وقت التشغيل |
| B **Correct** | Counting comments, blanks, or declarations can change LOC | قد تغير التعليقات والفراغات والتصريحات عدد LOC |
| C | All programming languages use identical line structures | تستعمل لغات البرمجة كلها بنية أسطر متماثلة |
| D | Function-point totals fix every line-counting convention | يثبت مجموع نقاط الوظائف جميع قواعد عد LOC |

**Explanation:** LOC totals change when blanks, comments, or executable-only lines are treated differently, so the counting rule must be explicit.

**ملاحظة:** يعرض مثال المقرر أعداداً مختلفة بحسب استبعاد الفراغات والتعليقات أو عد التعليمات التنفيذية فقط؛ لذلك يجب توضيح القاعدة.

### q3 · `ch6_fp_functional_units` · Remember

Which list contains the five Albrecht function-point components?

**العربية:** أي قائمة تضم المكونات الخمسة لنقاط الوظائف وفق Albrecht؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Classes, methods, inheritance links, coupling, cohesion, interfaces, and objects | أصناف وطرق وروابط وراثة واقتران وتماسك وواجهات وعلاقات كائنات |
| B | Statements, branches, loops, function calls, declarations, operators, and data flow | تعليمات وتفرعات وحلقات واستدعاءات دوال وتصريحات وعوامل وتدفق بيانات |
| C **Correct** | External inputs, outputs, inquiries, internal files, and external interface files | مدخلات ومخرجات واستعلامات وملفات منطقية داخلية وملفات واجهة خارجية |
| D | Actors, transactions, screens, reports, algorithms, environment, and adjustments | ممثلون ومعاملات وشاشات وتقارير وخوارزميات وبيئة وعوامل ضبط |

**Explanation:** Albrecht's function-point analysis counts external inputs, external outputs, inquiries, internal logical files, and external interface files.

**ملاحظة:** يعدّ تحليل Albrecht نقاط الإدخال والإخراج والاستعلامات والملفات المنطقية الداخلية وملفات الواجهات الخارجية.

### q4 · `ch6_fp_external_inquiry` · Understand

What distinguishes an external inquiry in function-point analysis?

**العربية:** ما الذي يميز الاستعلام الخارجي في تحليل نقاط الوظائف؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | It maintains logical data within the measured system | يحافظ على بيانات منطقية داخل النظام المقاس |
| B | It sends newly generated information outside the system | يرسل معلومات مولدة حديثاً إلى خارج النظام |
| C | It processes control data entering from another system | يعالج بيانات تحكم تدخل من نظام آخر |
| D **Correct** | It combines input and output to retrieve information | يجمع الإدخال والإخراج لاسترجاع المعلومات |

**Explanation:** An external inquiry is an input-output combination whose result is data retrieval; file maintenance and outbound reporting are different function types.

**ملاحظة:** الاستعلام الخارجي يجمع الإدخال والإخراج لاسترجاع البيانات؛ أما صيانة الملفات والتقارير الصادرة فأنواع وظيفية مختلفة.

### q5 · `ch6_fp_ilf_eif` · Understand

How does an EIF differ from an ILF for the system being measured?

**العربية:** بماذا يختلف EIF عن ILF بالنسبة إلى النظام المقاس؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | An EIF is referenced here but maintained elsewhere | يستعمل النظام EIF ويُصان في نظام خارجي |
| B | An ILF is referenced here but maintained elsewhere | يستعمل النظام ILF وتديره منظومة أخرى |
| C | An EIF is an outbound transaction that sends information | يمثل EIF معاملة ترسل مخرجات إلى المستخدمين |
| D | An ILF is an input-output request that retrieves data | يمثل ILF طلب استعلام يسترجع البيانات |

**Explanation:** An EIF is logically related data referenced by the measured system but maintained by another system; an ILF is maintained within the measured system.

**ملاحظة:** يمثل EIF بيانات مترابطة منطقياً يشير إليها النظام المقاس وتديرها منظومة أخرى؛ أما ILF فيُصان داخل النظام المقاس.

### q6 · `ch6_fp_adjustment_factor` · Understand

What does the function-point adjustment factor modify?

**العربية:** ماذا يعدّل عامل ضبط نقاط الوظائف؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Uses the selected language to count source lines | يستعمل اللغة المختارة لعد أسطر المصدر |
| B **Correct** | Adjusts unadjusted FP using system-influence ratings | تعديل FP الخام بتقديرات تأثير النظام |
| C | Counts actors using graphical user interfaces | يعد الممثلين الذين يستخدمون واجهة رسومية |
| D | Counts defects observed after a product release | يحسب العيوب المرصودة بعد إصدار المنتج |

**Explanation:** The adjustment factor modifies the unadjusted function-point count using fourteen system-influence ratings; it does not adjust LOC or actor counts.

**ملاحظة:** يطبق المقرر عامل ضبط التعقيد على العدد غير المعدل لنقاط الوظائف اعتماداً على أربعة عشر تقديراً لمؤثرات النظام؛ ولا يعدّل LOC أو عدد الممثلين.

### q7 · `ch6_fp_language_independence` · Understand

Why can function points be estimated before implementation language is chosen?

**العربية:** لماذا يمكن تقدير نقاط الوظائف قبل اختيار لغة التنفيذ؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Counts executable statements after compilation | تعد التعليمات التنفيذية بعد الترجمة |
| B | Counts operators and operands in source code | تعد العوامل والمعاملات في الشيفرة المصدرية |
| C **Correct** | Counts user-facing functions from requirements | تعد الوظائف الظاهرة من متطلبات النظام |
| D | Measures elapsed time during production runs | تقيس الزمن المنقضي أثناء التشغيل الإنتاجي |

**Explanation:** Function points use the system's functional view and can be estimated from requirements or design, independently of implementation language.

**ملاحظة:** تعتمد نقاط الوظائف على المنظور الوظيفي للنظام ويمكن تقديرها من المتطلبات أو التصميم بمعزل عن لغة التنفيذ.

### q8 · `ch6_feature_point_algorithm` · Understand

What additional characteristic do feature points count?

**العربية:** ما الخاصية الإضافية التي تعدّها Feature Points؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Counts developers assigned to each project phase | عدد المطورين المخصصين لكل مرحلة |
| B | Measures inheritance depth across software classes | عمق الوراثة في الأصناف البرمجية |
| C | Measures elapsed time between successive failures | الزمن المنقضي بين الإخفاقات المتعاقبة |
| D **Correct** | Adds algorithmic complexity to the size measure | تضيف التعقيد الخوارزمي لقياس الحجم |

**Explanation:** Feature points extend the information-domain count with algorithms, making the measure useful for applications with high algorithmic complexity.

**ملاحظة:** تضيف Feature Points الخوارزميات إلى عدّ مجال المعلومات، مما يلائم التطبيقات ذات التعقيد الخوارزمي المرتفع.

### q9 · `ch6_object_points` · Remember

Which artifacts are counted by the Object Point approach?

**العربية:** أي مخرجات يعدّها أسلوب Object Points؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Screens, reports, and third-generation components | شاشات وتقارير ومكونات الجيل الثالث |
| B | Operators, operands, and total token occurrences | العوامل والمعاملات ومجموع مرات ظهورها |
| C | Actors, transactions, and environment-adjustment factors | الممثلون والمعاملات وعوامل ضبط البيئة |
| D | Methods, attributes, and inheritance relationships | الطرق والخصائص وعلاقات الوراثة |

**Explanation:** Object Points estimate size from screens, reports, and third-generation-language components; the other choices belong to different metric families.

**ملاحظة:** تقدّر Object Points الحجم من الشاشات والتقارير ومكونات لغات الجيل الثالث؛ أما البدائل فتنتمي إلى عائلات مقاييس مختلفة.

### q10 · `ch6_backfiring` · Understand

What does backfiring do when relating LOC and function points?

**العربية:** ماذا تفعل backfiring عند الربط بين LOC ونقاط الوظائف؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Estimates LOC from class coupling and inheritance depth | تقدّر LOC من اقتران الأصناف وعمق الوراثة |
| B **Correct** | Derives function points from LOC using language ratios | تقدّر FP من LOC بنسب خاصة باللغة |
| C | Estimates defects from effort and phase duration | تقدّر العيوب من الجهد ومدة المرحلة |
| D | Estimates time from token counts and mental rate | تقدّر الزمن من معدلات الرموز والجهد |

**Explanation:** Backfiring uses language-specific LOC-to-function-point relationships to estimate functionality from delivered code; it is approximate and should be used judiciously.

**ملاحظة:** تستعمل backfiring علاقات خاصة باللغة بين LOC ونقاط الوظائف لتقدير الوظائف من الشيفرة المنجزة؛ وهي تقريبية وينبغي استعمالها بحذر.

## T04 — Halstead Software Science

Bank file: `Quiz_Ch06_T04_Halstead_Software_Science.json`

### q1 · `ch6_halstead_vocabulary` · Understand

What contributes to Halstead program vocabulary?

**العربية:** ما الذي يدخل في مفردات البرنامج وفق Halstead؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Unique operator and operand types in software | أنواع العوامل والمعاملات الفريدة في النظام |
| B | Every operator and operand occurrence in software | كل مرات ظهور العوامل والمعاملات في النظام |
| C | Executable statements and control-flow branches | تعليمات البرنامج وتفرعات تدفق التحكم فيه |
| D | Software modules and their external interfaces | الوحدات البرمجية وواجهاتها المعتمدة خارجياً |

**Explanation:** Halstead vocabulary combines the counts of unique operators and unique operands; total occurrences contribute to program length instead.

**ملاحظة:** تجمع مفردات Halstead عدد العوامل والمعاملات الفريدة؛ أما مجموع مرات الظهور فيدخل في طول البرنامج.

### q2 · `ch6_halstead_program_length` · Understand

What does Halstead's program length count?

**العربية:** ماذا يعدّ طول البرنامج في مقاييس Halstead؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Unique operator and operand types in the program | أنواع العوامل والمعاملات الفريدة في البرنامج |
| B **Correct** | All operator and operand occurrences in the program | جميع مرات ظهور العوامل والمعاملات في البرنامج |
| C | Executable statements after removing every operator | التعليمات التنفيذية بعد حذف العوامل منها |
| D | Modules and data structures called by the program | الوحدات وبنى البيانات التي يستدعيها البرنامج مباشرةً |

**Explanation:** Program length uses total token occurrences; vocabulary counts unique tokens, so the two measures answer different questions.

**ملاحظة:** يعتمد طول البرنامج على مجموع مرات ظهور الرموز؛ أما المفردات فتعدّ الرموز الفريدة، ولذلك يجيب المقياسان عن سؤالين مختلفين.

### q3 · `ch6_halstead_volume` · Understand

How is the meaning of Halstead volume described?

**العربية:** كيف يوصف معنى حجم Halstead؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | The number of independent control-flow paths | عدد المسارات المستقلة لتدفق التحكم |
| B | The elapsed time required to execute the program | الزمن المنقضي اللازم لتنفيذ البرنامج |
| C **Correct** | Encoded program size from its length and vocabulary | حجم البرنامج المرمّز بطوله ومفرداته |
| D | The count of distinct modules in the software | عدد الوحدات البرمجية المتميزة في النظام |

**Explanation:** Volume estimates the program's size in bits under a uniform encoding of its vocabulary; it is not execution time or control-flow complexity.

**ملاحظة:** يقدّر الحجم عدد البتات اللازمة لترميز البرنامج عند ترميز مفرداته بانتظام؛ ولا يمثل زمن التنفيذ أو تعقيد تدفق التحكم.

### q4 · `ch6_halstead_potential_volume` · Understand

What does Halstead's potential volume represent?

**العربية:** ماذا يمثل الحجم المحتمل لدى Halstead؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | The total source size after removing comments | الحجم الكلي للمصدر بعد حذف التعليقات |
| B | The volume of every module in the finished system | حجم كل وحدة في النظام البرمجي المكتمل |
| C | The encoded size of distinct project requirements | الحجم المرمّز لمتطلبات المشروع المتميزة |
| D **Correct** | Minimum volume for implementing the algorithm | الحجم الذي يحققه أدنى تنفيذ للخوارزمية |

**Explanation:** Potential volume is tied to the minimal implementation of the algorithm, whereas program volume describes the measured implementation.

**ملاحظة:** يرتبط الحجم المحتمل بأدنى تنفيذ للخوارزمية، بينما يصف حجم البرنامج التنفيذ المقاس.

### q5 · `ch6_halstead_program_level` · Understand

What does a higher Halstead program level indicate?

**العربية:** إلى ماذا يشير ارتفاع مستوى البرنامج لدى Halstead؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Small measured volume relative to potential volume | صغر الحجم المقاس نسبةً إلى الحجم المحتمل |
| B | The program has more control-flow regions | يحتوي البرنامج على مناطق تدفق تحكم أكثر |
| C | Each program execution takes more elapsed time | يستغرق كل تنفيذ للبرنامج زمناً منقضياً أطول |
| D | The software contains a greater number of modules | يحتوي النظام البرمجي على وحدات متميزة أكثر |

**Explanation:** Program level compares potential volume with measured volume; a value nearer one corresponds to a compact, high-level implementation in this model.

**ملاحظة:** يقارن مستوى البرنامج الحجم المحتمل بالحجم المقاس؛ والقيمة الأقرب إلى الواحد تقابل تنفيذاً موجزاً عالي المستوى ضمن هذا النموذج.

### q6 · `ch6_halstead_level_difficulty` · Analyze

How are Halstead difficulty and program level related?

**العربية:** ما العلاقة بين الصعوبة ومستوى البرنامج في نموذج المقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Difficulty equals the program's control-flow path count | تساوي الصعوبة عدد مسارات تدفق التحكم بالبرنامج |
| B **Correct** | Difficulty varies inversely with the program level | تتناسب الصعوبة عكسياً مع مستوى البرنامج |
| C | Difficulty equals program level times program volume | تساوي الصعوبة مستوى البرنامج مضروباً بحجمه |
| D | Difficulty equals elapsed execution time in seconds | تساوي الصعوبة زمن التنفيذ المنقضي بالثواني |

**Explanation:** Difficulty varies inversely with program level; the alternatives substitute control-flow, size, or time measures.

**ملاحظة:** يربط المقرر الصعوبة بمستوى البرنامج بعلاقة عكسية؛ أما البدائل فتستبدل بها مقاييس تدفق التحكم أو الحجم أو الزمن.

### q7 · `ch6_halstead_effort_unit` · Understand

Which unit represents Halstead effort?

**العربية:** بأي وحدة يفسر المقرر جهد Halstead في أمثلته؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Development effort measured in person-months | جهد تطوير البرمجيات لكل وحدة شخص-شهر |
| B | Actual hours spent running the finished program | الساعات الفعلية لتشغيل البرنامج بعد اكتماله |
| C **Correct** | Effort measured in elementary mental discriminations | الجهد المقاس بالتمييزات الذهنية الأولية |
| D | Independent control paths exercised during testing | مسارات تحكم مستقلة أثناء اختبار البرمجيات |

**Explanation:** Halstead effort is expressed as elementary mental discriminations; it is not a project staffing unit or a runtime measure.

**ملاحظة:** يُعبّر عن جهد Halstead بالتمييزات الذهنية الأولية؛ فهو ليس وحدة توظيف للمشروع ولا مقياساً لزمن التشغيل.

### q8 · `ch6_halstead_time` · Understand

How is Halstead programming time estimated?

**العربية:** كيف يقدّر المقرر زمن البرمجة لدى Halstead؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Module length multiplied by its number of branches | طول الوحدة مضروباً بعدد التفرعات الموجودة |
| B | Vocabulary divided by the unique-operator count | مفردات البرنامج مقسومة على عدد العوامل الفريدة |
| C | Effort multiplied by the count of external data files | الجهد مضروباً بعدد ملفات البيانات الخارجية |
| D **Correct** | Effort divided by Stroud's assumed rate per second | الجهد مقسوماً على معدل Stroud المفترض في الثانية |

**Explanation:** Estimated programming time divides mental-discrimination effort by the assumed Stroud rate of eighteen per second.

**ملاحظة:** يحسب مثال المقرر الزمن بقسمة جهد التمييزات الذهنية على معدل Stroud المفترض، وهو ثمانية عشر في الثانية.

### q9 · `ch6_halstead_estimated_length` · Understand

What token information is used to estimate program length?

**العربية:** ما معلومات الرموز المستخدمة لتقدير طول البرنامج؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Counts of unique operators and unique operands | أعداد العوامل الفريدة والمعاملات الفريدة |
| B | Counts of modules and their called components | أعداد الوحدات والمكونات التي تستدعيها |
| C | Source-line totals and the number of comments | مجموع أسطر المصدر وعدد التعليقات |
| D | Failure totals and their recorded operating hours | مجموع الإخفاقات وزمن التشغيل المسجل لها |

**Explanation:** The estimated-length relation uses the unique operator and operand counts; observed total token occurrences instead determine actual length.

**ملاحظة:** تستعمل علاقة الطول المقدّر أعداد العوامل والمعاملات الفريدة؛ أما الطول الفعلي فيعتمد على مجموع مرات ظهور الرموز.

### q10 · `ch6_halstead_c_function_calls` · Understand

Under C's counting convention, how is a function call treated?

**العربية:** وفق قواعد عدّ C في المقرر، كيف تُعامل استدعاءات الدوال؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | A function call is counted as a distinct operand | يُحسب استدعاء الدالة معاملاً متميزاً في التحليل |
| B **Correct** | A function call is counted as an operator token | يُحسب استدعاء الدالة رمز عامل في التحليل |
| C | A function call is excluded from token counting | يُستبعد استدعاء الدالة من عدّ رموز البرنامج |
| D | A function call is counted as a control-flow region | يُحسب استدعاء الدالة منطقةً لتدفق التحكم |

**Explanation:** C classifies function calls as operators; identifiers and supplied arguments follow operand-counting rules.

**ملاحظة:** تصنف قواعد C استدعاءات الدوال عوامل؛ أما المعرّفات والمعاملات الممررة فتُحسب وفق قواعد المعاملات.

## T05 — Data Structure Metrics

Bank file: `Quiz_Ch06_T05_Data_Structure_Metrics.json`

### q1 · `ch6_data_categories` · Remember

Which categories describe data associated with a module?

**العربية:** كيف يصنف المقرر البيانات المرتبطة بالوحدة البرمجية؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Input data, internal data, and output data | بيانات إدخال وبيانات داخلية وبيانات إخراج |
| B | Control data, project data, and schedule data | بيانات تحكم وبيانات مشروع وبيانات جدول زمني |
| C | Operator data, operand data, and token data | بيانات عوامل وبيانات معاملات وبيانات رموز |
| D | Product data, process data, and actor data | بيانات منتج وبيانات عملية وبيانات ممثلين |

**Explanation:** The data-structure material distinguishes input, internal, and output data for a module; the alternatives belong to other classifications.

**ملاحظة:** يميز محور بنية البيانات بين بيانات الإدخال والبيانات الداخلية وبيانات الإخراج للوحدة؛ أما البدائل فتنتمي إلى تصنيفات أخرى.

### q2 · `ch6_cross_reference_list` · Understand

What does a cross-reference list record for a variable?

**العربية:** ماذا تسجل قائمة الإحالات المتقاطعة للمتغير؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Modules inheriting the class of that variable | الوحدات التي ترث صنف ذلك المتغير البرمجي |
| B **Correct** | Source statements that refer to the variable | تعليمات المصدر التي تشير إلى ذلك المتغير |
| C | Failures attributed to the variable's value | الإخفاقات المنسوبة إلى قيمة ذلك المتغير |
| D | Actors that enter a value for the variable | الممثلون الذين يدخلون قيمة لذلك المتغير |

**Explanation:** A cross-reference list connects a variable with its reference line numbers, supporting later live-variable and span analysis.

**ملاحظة:** تربط قائمة الإحالات المتقاطعة المتغير بأرقام أسطر الإشارة إليه، مما يدعم تحليل المتغيرات الحية والامتداد لاحقاً.

### q3 · `ch6_live_variable` · Understand

When is a variable considered live across a program point?

**العربية:** متى يعدّ المتغير حياً عبر نقطة في البرنامج؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | It is declared in a class with many subclasses | يُصرح به داخل صنف له أصناف فرعية عديدة |
| B | It appears only in a comment or a blank line | يظهر في تعليق أو سطر فارغ دون استخدام تنفيذي |
| C **Correct** | Its value may be read before the next assignment | قد تُقرأ قيمته المسندة قبل إسناد قيمة جديدة |
| D | It is passed to an external user as output | تُمرر قيمته إلى مستخدم خارجي بوصفها مخرجاً |

**Explanation:** Liveness concerns whether a value can still be used before it is overwritten; declaration, inheritance, and output status alone do not establish liveness.

**ملاحظة:** تتعلق الحياة بإمكان استعمال القيمة قبل استبدالها؛ فالتصريح والوراثة وكون المتغير مخرجاً لا تثبت حياته وحدها.

### q4 · `ch6_average_live_variables` · Understand

How is the average number of live variables formed?

**العربية:** كيف يحسب متوسط عدد المتغيرات الحية؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Unique operands divided by the number of modules | المعاملات الفريدة مقسومة على عدد الوحدات البرمجية |
| B | Module weaknesses divided by variable count | نقاط ضعف الوحدات مقسومة على عدد المتغيرات |
| C | Variable definitions divided by source-line count | تعريفات المتغيرات مقسومة على عدد أسطر المصدر |
| D **Correct** | Mean live-variable count per executable statement | متوسط عدد المتغيرات الحية عبر التعليمات التنفيذية |

**Explanation:** Average live variables is the total live-variable count across executable statements divided by the number of executable statements.

**ملاحظة:** متوسط المتغيرات الحية هو مجموع أعدادها عبر التعليمات التنفيذية مقسوماً على عدد التعليمات التنفيذية.

### q5 · `ch6_variable_span` · Understand

What does variable span measure?

**العربية:** ماذا يصف امتداد المتغير في مقاييس البيانات لدى المقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Statements between successive uses of a variable | التعليمات بين إحالات متعاقبة إلى المتغير نفسه |
| B | Classes between a root and one of its children | الأصناف الواقعة بين الجذر وأحد أصنافه الفرعية |
| C | Components called directly by the measured module | المكونات التي تستدعيها الوحدة المقاسة مباشرةً |
| D | Comments surrounding the variable's declaration | التعليقات المحيطة بتصريح ذلك المتغير البرمجي |

**Explanation:** Span is based on the statement distance between successive references under the stated source convention; it is not inheritance depth or call fan-out.

**ملاحظة:** يعتمد الامتداد على المسافة بين الإحالات المتعاقبة؛ ولا يمثل عمق الوراثة أو تفرع الاستدعاءات.

### q6 · `ch6_module_weakness` · Understand

Which relationship defines module weakness?

**العربية:** أي علاقة تعرّف ضعف الوحدة في نموذج المقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Average live-variable count times average span | متوسط عدد المتغيرات الحية مضروباً بمتوسط امتدادها |
| B **Correct** | Mean live-variable count × mean variable life | متوسط عدد المتغيرات الحية مضروباً بمتوسط عمرها |
| C | Total module weaknesses added across the program | مجموع نقاط ضعف الوحدات المضافة على مستوى البرنامج |
| D | Unique operands divided by unique operators | عدد المعاملات الفريدة مقسوماً على العوامل الفريدة |

**Explanation:** Module weakness uses average live variables times average variable life; span is a separate data metric.

**ملاحظة:** يستخدم ضعف الوحدة متوسط المتغيرات الحية مضروباً بمتوسط عمر المتغير؛ أما الامتداد فمقياس بيانات منفصل.

### q7 · `ch6_program_weakness` · Analyze

How is program weakness derived from its module weaknesses?

**العربية:** كيف يُشتق ضعف البرنامج من نقاط ضعف وحداته؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Sum module weaknesses without averaging across modules | جمع نقاط ضعف الوحدات دون حساب متوسطها |
| B | Largest module weakness multiplied by program length | أكبر نقطة ضعف لوحدة مضروبة بطول البرنامج |
| C **Correct** | The arithmetic mean across module-weakness values | المتوسط الحسابي لقيم ضعف الوحدات البرمجية |
| D | Module count divided by mean live-variable count | عدد الوحدات مقسوماً على متوسط المتغيرات الحية |

**Explanation:** Program weakness is the mean of module weaknesses; the sum alone is not normalized by the number of modules.

**ملاحظة:** ضعف البرنامج هو متوسط نقاط ضعف الوحدات؛ أما الجمع وحده فلا يطبّع القيمة بحسب عدد الوحدات.

### q8 · `ch6_program_metric_aggregation` · Understand

Why does the program-level weakness calculation divide by module count?

**العربية:** لماذا تقسم عملية حساب ضعف البرنامج على عدد الوحدات؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | It removes every module containing live variables | يحذف جميع الوحدات التي تتضمن متغيرات حية |
| B | It converts each module's value into a span count | يحوّل قيمة كل وحدة برمجية إلى عدد امتدادات |
| C | It makes program weakness equal to the largest module | يجعل ضعف البرنامج مساوياً لقيمة أكبر وحدة |
| D **Correct** | It gives the program-wide mean of module values | يحسب متوسط قيم الوحدات على مستوى البرنامج |

**Explanation:** Dividing the summed module weaknesses by the number of modules yields the stated program mean rather than a total or maximum.

**ملاحظة:** تعطي قسمة مجموع نقاط ضعف الوحدات على عددها متوسط البرنامج المحدد، لا المجموع ولا القيمة القصوى.

## T06 — Information Flow Metrics

Bank file: `Quiz_Ch06_T06_Information_Flow_Metrics.json`

### q1 · `ch6_fan_in` · Understand

Which callers contribute to a component's fan-in value?

**العربية:** أي جهات مستدعية تدخل في قيمة fan-in للمكوّن؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Components that call this component or pass control to it | المكونات التي تستدعي هذا المكوّن أو تمرر إليه التحكم |
| B | Components that this component calls or controls directly | المكونات التي يستدعيها هذا المكوّن أو يتحكم بها مباشرةً |
| C | Variables that remain live within the measured component | المتغيرات التي تظل حية داخل المكوّن الذي يجري قياسه |
| D | Methods that share attributes within the same component | الطرق التي تتشارك الخصائص ضمن المكوّن البرمجي نفسه |

**Explanation:** Basic fan-in counts incoming component calls or control transfers; outgoing calls are fan-out.

**ملاحظة:** يعدّ fan-in الأساسي استدعاءات المكونات أو تحويلات التحكم الواردة؛ أما الاستدعاءات الصادرة فهي fan-out.

### q2 · `ch6_fan_out` · Understand

What does the basic fan-out of a component count?

**العربية:** ماذا يعدّ fan-out الأساسي لمكوّن؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Components that can call the measured component | المكونات القادرة على استدعاء المكوّن الذي يجري قياسه |
| B **Correct** | Components this component directly calls or controls | المكونات التي يستدعيها هذا المكوّن أو يتحكم بها |
| C | Variables referenced in each executable statement | المتغيرات المشار إليها في كل تعليمة تنفيذية |
| D | Methods inherited from the component's parent classes | الطرق الموروثة من الأصناف الأصلية لذلك المكوّن |

**Explanation:** Basic fan-out counts direct outgoing calls; incoming callers are counted by fan-in.

**ملاحظة:** يعدّ fan-out الأساسي الاستدعاءات الصادرة المباشرة؛ أما الجهات المستدعية الواردة فيعدّها fan-in.

### q3 · `ch6_fan_boundary_convention` · Understand

What value does simple fan counting assign at a zero-count boundary?

**العربية:** في إجراء fan المبسط بالمقرر، ما القيمة المسندة عند حدّ ذي عدّ صفري؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Every component receives zero for both fan counts | تأخذ كل المكونات صفراً في عددي fan-in وfan-out |
| B | Roots receive fan-in one; leaves receive fan-out one | تأخذ الجذور fan-in واحداً، وتأخذ الأوراق fan-out واحداً |
| C **Correct** | Roots receive fan-out one; leaves receive fan-in one | تأخذ الجذور fan-out واحداً، وتأخذ الأوراق fan-in واحداً |
| D | Every component receives one for both fan counts | تأخذ كل المكونات واحداً في عددي fan-in وfan-out |

**Explanation:** This simple-fan convention assigns a minimum of one to top-level fan-in and leaf fan-out; it is not a universal definition.

**ملاحظة:** يسند إجراء الشريحة قيمة دنيا مقدارها واحد إلى fan-in للجذور وfan-out للأوراق؛ وهذا اصطلاح للإجراء لا تعريف شامل.

### q4 · `ch6_fan_in_reuse_caveat` · Analyze

What limitation can simple fan-in have?

**العربية:** ما القيد الذي يذكره المقرر بشأن fan-in المبسط؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | It ignores every component call made by a module | يتجاهل كل استدعاء مكوّن تجريه الوحدة |
| B | It measures elapsed time rather than connections | يقيس الزمن المنقضي بدلاً من الاتصالات |
| C | It treats all data structures as external files | يعامل جميع بنى البيانات بوصفها ملفات خارجية |
| D **Correct** | It can penalize a component that is reused | قد يفرض عقوبة على مكوّن يعاد استخدامه |

**Explanation:** A simple fan-in model may penalize reused components, so a high value needs contextual interpretation.

**ملاحظة:** تحذر الشريحة صراحةً من أن نموذج fan-in المبسط قد يفرض عقوبة على المكونات المعاد استخدامها؛ لذا يلزم تفسير القيمة في سياقها.

### q5 · `ch6_henry_kafura_formula` · Understand

What structure does the verified Henry–Kafura measure use?

**العربية:** ما البنية التي يستعملها مقياس Henry–Kafura الموثق؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Module length times (fan-in + fan-out) squared | طول الوحدة مضروباً بمربع مجموع fan-in وfan-out |
| B | Module size divided by live-variable count and span | حجم الوحدة مقسوماً على عدد المتغيرات الحية وامتدادها |
| C | Program length times unique operators and operands | طول البرنامج مضروباً بالعوامل والمعاملات الفريدة |
| D | Class depth plus the count of its immediate subclasses | عمق الصنف مضافاً إليه عدد أصنافه الفرعية المباشرة |

**Explanation:** Henry–Kafura combines module length with the square of total information flow; it is distinct from the basic fan counts alone.

**ملاحظة:** يجمع Henry–Kafura طول الوحدة مع مربع مجموع تدفق المعلومات؛ وهو يختلف عن عدّ fan الأساسي وحده.

### q6 · `ch6_henry_kafura_flow_scope` · Understand

Which relationships are included in Henry–Kafura fan-in and fan-out?

**العربية:** أي علاقات تدخل في fan-in وfan-out لدى Henry–Kafura؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Inheritance links and method overrides only | روابط الوراثة وتجاوز الطرق فقط دون غيرها |
| B **Correct** | Control links and accessed data structures | روابط التحكم وبنى البيانات المستخدمة عبر الوحدات |
| C | Live-variable spans and executable-statement counts | امتدادات المتغيرات الحية وأعداد التعليمات التنفيذية |
| D | Project staffing patterns and schedule changes | أنماط التوظيف في المشروع والتغييرات على جدوله |

**Explanation:** Henry–Kafura extends fan-in and fan-out beyond calls to include data structures a module retrieves or updates.

**ملاحظة:** يوسع Henry–Kafura مقياسي fan-in وfan-out ليتجاوزا الاستدعاءات ويشملا بنى البيانات التي تسترجعها الوحدة أو تحدثها.

### q7 · `ch6_extended_fan_out_terms` · Understand

Which set contributes to extended fan-out?

**العربية:** في إجراء fan-out الموسع بالمقرر، أي مجموعة تدخل في حسابه؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Incoming callers, inherited methods, and live variables | الجهات المستدعية والطرق الموروثة والمتغيرات الحية |
| B | Executable lines, unique operands, and class attributes | الأسطر التنفيذية والمعاملات الفريدة وخصائص الأصناف |
| C **Correct** | Called modules, passed parameters, and written data | استدعاء المكونات، تمرير المعاملات، وكتابة البيانات |
| D | Project effort, schedule duration, and defect density | جهد المشروع ومدة الجدول الزمني وكثافة العيوب |

**Explanation:** Extended fan-out counts called components, parameters passed across hierarchy levels, and data elements written by the component.

**ملاحظة:** يجمع fan-out الموسع في الشريحة المكونات المستدعاة والمعاملات الممررة بين مستويات التسلسل وعناصر البيانات التي يكتبها المكوّن.

### q8 · `ch6_henry_kafura_length_effect` · Apply

Two modules have equal fan-in and fan-out totals. Which has the higher Henry–Kafura value?

**العربية:** لدى وحدتين مجموع متساوٍ لـfan-in وfan-out؛ أيهما أعلى في Henry–Kafura؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Fewer source lines always produce a higher value | يؤدي عدد أسطر أقل دائماً إلى قيمة تعقيد أعلى |
| B | Comments determine the module's measured complexity | تحدد التعليقات قيمة التعقيد المقاسة للوحدة |
| C | Shorter names lower the complexity of a module | تخفض الأسماء الأقصر قيمة تعقيد الوحدة المقاسة |
| D **Correct** | With flow fixed, the longer module scores higher | مع ثبات التدفق، يزيد طول الوحدة قيمة التعقيد |

**Explanation:** With equal flow totals, the length factor gives the longer component a greater Henry–Kafura value.

**ملاحظة:** عند تساوي مجموع تدفقات المعلومات، يجعل عامل طول الوحدة قيمة Henry–Kafura للوحدة الأطول أكبر.

## T07 — Control Flow Complexity

Bank file: `Quiz_Ch06_T07_Control_Flow_Complexity.json`

### q1 · `ch6_control_flow_graph` · Understand

In a control-flow graph, what do nodes and edges represent?

**العربية:** ماذا تمثل العقد والحواف في مخطط تدفق التحكم؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Nodes: statements/blocks; edges: control transfers | العقد تمثل التعليمات والحواف تمثل انتقالات التحكم |
| B | Nodes are classes; edges are inheritance links | العقد تمثل الأصناف والحواف تمثل روابط الوراثة |
| C | Nodes are variables; edges show their live ranges | العقد تمثل المتغيرات والحواف تبين امتدادات حياتها |
| D | Nodes are files; edges show input and output | العقد تمثل الملفات والحواف تبين الإدخال والإخراج |

**Explanation:** A control-flow graph models executable flow: nodes are statements or blocks and directed edges show possible transfers of control.

**ملاحظة:** يمثل مخطط تدفق التحكم مسار التنفيذ؛ فالعقد تعليمات أو كتل، والحواف الموجهة تبين انتقالات التحكم الممكنة.

### q2 · `ch6_mccabe_graph_formula` · Understand

Which verbal form matches McCabe's graph-based complexity calculation?

**العربية:** أي صياغة لفظية تطابق حساب McCabe المعتمد على الرسم؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Nodes minus edges plus twice the operator count | عدد العقد ناقص الحواف مضافاً إليه مثلي عدد العوامل |
| B **Correct** | Edges minus nodes plus twice the component count | عدد الحواف ناقص العقد مضافاً إليه مثلي عدد المكونات |
| C | Predicates minus regions plus the number of modules | عدد الشروط ناقص المناطق مضافاً إليه عدد الوحدات |
| D | Edges plus nodes divided by the number of predicates | عدد الحواف مضافاً إليه العقد مقسوماً على عدد الشروط |

**Explanation:** The graph formula uses edges, nodes, and the number of connected components; the alternatives mix unrelated counts or operations.

**ملاحظة:** تستعمل صيغة الرسم الحواف والعقد وعدد المكونات المتصلة؛ أما البدائل فتخلط بها أعداداً أو عمليات مختلفة.

### q3 · `ch6_mccabe_connected_components` · Understand

What does P denote in the graph-based McCabe formula?

**العربية:** ماذا يرمز P في صيغة McCabe المعتمدة على الرسم؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | The number of predicate nodes in the flow graph | عدد عقد الشروط في مخطط تدفق التحكم |
| B | The number of program variables shown in the graph | عدد متغيرات البرنامج الظاهرة في مخطط التدفق |
| C **Correct** | The number of connected components in the flow graph | عدد المكونات المتصلة في مخطط تدفق التحكم |
| D | The number of independent test teams for the graph | عدد فرق الاختبار المستقلة الخاصة بالمخطط |

**Explanation:** P counts connected components, commonly one for a single connected program flow graph; predicate nodes are used by a different method.

**ملاحظة:** يعدّ P المكونات المتصلة، وغالباً تكون واحدة لمخطط برنامج متصل؛ أما عقد الشروط فتدخل في طريقة أخرى.

### q4 · `ch6_mccabe_predicate_method` · Understand

How is cyclomatic complexity obtained from predicate nodes?

**العربية:** كيف يستخرج التعقيد الدوري من عقد الشروط؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Count graph edges, then subtract one from the count | عدد حواف المخطط ناقصاً 1 |
| B | Count source lines, then divide the total by two | عدد أسطر المصدر مقسوماً على 2 |
| C | Count classes, then add their inheritance depth | عدد الأصناف مع عمق الوراثة |
| D **Correct** | Count predicate nodes, then add one to the count | عدد عقد الشروط في المخطط + 1 |

**Explanation:** The predicate method returns the number of predicate nodes plus one; it is an alternate computation of McCabe complexity.

**ملاحظة:** تعطي طريقة عقد الشروط عدد عقد الشرط مضافاً إليه واحد؛ وهي طريقة بديلة لحساب تعقيد McCabe.

### q5 · `ch6_mccabe_regions_method` · Understand

Which graph feature gives cyclomatic complexity by the region method?

**العربية:** أي خاصية في الرسم تعطي التعقيد الدوري بطريقة المناطق؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | The number of regions in the control-flow graph | عدد المناطق في مخطط تدفق التحكم |
| B | The number of variables live across each region | عدد المتغيرات الحية عبر كل منطقة |
| C | The number of modules called from each region | عدد الوحدات المستدعاة من كل منطقة |
| D | The number of operators found inside each region | عدد العوامل الموجودة داخل كل منطقة |

**Explanation:** Region counting is another way to obtain cyclomatic complexity from a flow graph.

**ملاحظة:** يعرض المقرر عدّ المناطق طريقة ثالثة لاستخراج التعقيد الدوري من مخطط التدفق.

### q6 · `ch6_mccabe_independent_paths` · Understand

What does cyclomatic complexity count in terms of paths?

**العربية:** ماذا يعدّ التعقيد الدوري من حيث المسارات؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | The count of all possible execution traces without limits | عدد مسارات التنفيذ الممكنة كافة دون قيود |
| B **Correct** | The count of linearly independent paths through a module | عدد المسارات المستقلة خطياً عبر الوحدة البرمجية |
| C | The count of data references in each source statement | عدد إحالات البيانات الموجودة في كل تعليمة مصدر |
| D | The count of files accessed during program execution | عدد الملفات التي يجري الوصول إليها أثناء التنفيذ |

**Explanation:** Cyclomatic complexity gives the number of linearly independent paths; it is not a count of every possible trace or data reference.

**ملاحظة:** يعطي التعقيد الدوري عدد المسارات المستقلة خطياً؛ ولا يعدّ كل أثر تنفيذ ممكن أو إحالة بيانات.

### q7 · `ch6_mccabe_test_basis` · Apply

What does the independent-path interpretation help a tester organize?

**العربية:** بماذا يساعد تفسير المسارات المستقلة المختبِر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | A list of classes used to test inheritance behavior | قائمة أصناف تُستخدم لاختبار سلوك الوراثة |
| B | A mapping between LOC and function-point size units | تحويل بين LOC ووحدات حجم نقاط الوظائف |
| C **Correct** | A basis set of paths for control-flow testing | مجموعة أساس من المسارات لاختبار تدفق التحكم |
| D | An effort-distribution table for lifecycle phases | جدول لتوزيع الجهد على مراحل دورة حياة البرمجيات |

**Explanation:** Independent paths provide a basis for organizing path-focused tests of control flow; they do not measure size or project effort.

**ملاحظة:** توفر المسارات المستقلة أساساً لتنظيم اختبارات تركز على تدفق التحكم؛ ولا تقيس الحجم أو جهد المشروع.

### q8 · `ch6_cyclomatic_not_size` · Analyze

Why is cyclomatic complexity not a size metric?

**العربية:** لماذا لا يعدّ التعقيد الدوري مقياساً للحجم؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | It measures product reliability rather than its amount | يقيس اعتمادية المنتج بدلاً من مقداره البرمجي |
| B | It measures project staffing rather than software structure | يقيس توظيف المشروع بدلاً من بنية البرمجيات |
| C | It measures language vocabulary rather than source size | يقيس مفردات اللغة بدلاً من حجم الشيفرة المصدرية |
| D **Correct** | It describes control flow rather than product size | يصف بنية التحكم وتفرعات البرنامج، لا حجمه |

**Explanation:** Cyclomatic complexity describes the control-flow decision structure; LOC, function points, and program length are size measures.

**ملاحظة:** يصف التعقيد الدوري بنية قرارات تدفق التحكم؛ أما LOC ونقاط الوظائف وطول البرنامج فهي مقاييس حجم.

## T08 — Object-Oriented Metrics

Bank file: `Quiz_Ch06_T08_Object_Oriented_Metrics.json`

### q1 · `ch6_oo_measurement_unit` · Understand

What is the primary measurement unit for class-oriented OO metrics?

**العربية:** ما وحدة القياس الأساسية للمقاييس الكائنية الموجهة للصنف؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | The class, its hierarchy, and its collaborations | الصنف وتسلسله الهرمي وتعاوناته |
| B | The source file, its comments, and its release date | ملف المصدر وتعليقاته وتاريخ إصداره |
| C | The project, its schedule, and its staffing pattern | المشروع وجدوله ونمط التوظيف فيه |
| D | The test case, its result, and its execution time | حالة الاختبار ونتيجتها وزمن تنفيذها |

**Explanation:** Object-oriented metrics focus on classes, class hierarchies, and collaborations because these are central design structures in OO systems.

**ملاحظة:** تركز مقاييس البرمجيات كائنية التوجه على الأصناف وتسلسلها الهرمي وتعاوناتها لأنها بنى تصميم مركزية في هذه الأنظمة.

### q2 · `ch6_wmc` · Understand

What does Weighted Methods per Class capture?

**العربية:** ماذا يقيس Weighted Methods per Class؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Classes coupled to a class through references | الأصناف المقترنة بصنف عبر الإحالات إليه |
| B **Correct** | Sum of method complexities within a class | مجموع تعقيدات الطرق الموزونة داخل الصنف |
| C | Methods able to respond to a class message | الطرق القادرة على الاستجابة لرسالة الصنف |
| D | Subclasses directly inheriting from a class | الأصناف الفرعية التي ترث مباشرةً من صنف |

**Explanation:** WMC counts methods or sums their chosen complexity values; coupling, response, and child counts are different OO metrics.

**ملاحظة:** يعدّ WMC طرق الصنف أو يجمع قيم تعقيدها المختارة؛ أما الاقتران والاستجابة وعدد الفروع فمقاييس مختلفة.

### q3 · `ch6_dit` · Understand

What does Depth of Inheritance Tree describe?

**العربية:** ماذا يصف Depth of Inheritance Tree؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | The count of immediate subclasses of a class | عدد الأصناف الفرعية المباشرة التابعة لصنف |
| B | The count of methods defined within a class | عدد الطرق المعرفة داخل الصنف البرمجي |
| C **Correct** | The class depth in its inheritance hierarchy | عمق الصنف ضمن التسلسل الهرمي للوراثة |
| D | The count of other classes coupled to a class | عدد الأصناف الأخرى المقترنة بذلك الصنف |

**Explanation:** DIT describes inheritance depth; immediate children are NOC, while method count and coupling are separate measures.

**ملاحظة:** يصف DIT عمق الوراثة؛ أما الأبناء المباشرون فهم NOC، ويختلف عنهما عدد الطرق والاقتران.

### q4 · `ch6_noc` · Understand

Which classes are counted by Number of Children?

**العربية:** أي أصناف يعدّها Number of Children؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Every ancestor appearing above the measured class | جميع الأصناف الأصلية فوق الصنف الذي يجري قياسه |
| B | Every class referenced by methods in the class | كل صنف تشير إليه الطرق المعرفة داخل الصنف |
| C | Every method inherited by the class's subclasses | كل طريقة ترثها الأصناف الفرعية التابعة للصنف |
| D **Correct** | The immediate subclasses directly below a class | الأصناف الفرعية المباشرة أسفل الصنف المقاس |

**Explanation:** NOC counts immediate subclasses; ancestors and referenced classes are not children.

**ملاحظة:** يعدّ المقرر صراحةً الأصناف الفرعية المباشرة فقط في NOC؛ فالأصناف الأصلية والمرجعية ليست أبناء.

### q5 · `ch6_cbo` · Understand

What does Coupling Between Objects count for a class?

**العربية:** ماذا يعدّ Coupling Between Objects لصنف؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Other classes coupled to the measured class | الأصناف المرتبطة بالصنف عبر الاقتران المتبادل |
| B | Public methods sharing instance data within the class | الطرق العامة التي تتشارك بيانات المثيل داخل الصنف |
| C | Methods inherited from the parent classes | الطرق الموروثة والمتاحة من الأصناف الأصلية |
| D | Control-flow regions inside the measured class | مناطق تدفق التحكم ضمن الصنف الذي يجري قياسه |

**Explanation:** CBO counts other classes coupled to the measured class; shared attributes, inherited methods, and control-flow regions describe other properties.

**ملاحظة:** يعدّ CBO الأصناف الأخرى المرتبطة بالصنف المقاس؛ أما الخصائص المشتركة والطرق الموروثة ومناطق التدفق فتصف خصائص أخرى.

### q6 · `ch6_rfc` · Understand

What does Response For a Class measure?

**العربية:** كيف يصف المقرر Response For a Class؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Classes that inherit directly from the measured class | الأصناف التي ترث مباشرةً من الصنف المقاس |
| B **Correct** | Methods the class can respond with to a message | الطرق التي قد ينفذها الصنف عند تلقي رسالة |
| C | Attributes declared by methods of the class | الخصائص المعلنة ضمن طرق الصنف البرمجي |
| D | Method pairs that share no attributes in common | أزواج الطرق التي لا تتشارك أي خصائص |

**Explanation:** RFC counts internal and external methods that may respond to a message; NOC, attribute count, and LCOM are different measures.

**ملاحظة:** تعرف شريحة المقرر RFC بعدد الطرق الداخلية والخارجية؛ أما NOC وعدّ الخصائص وLCOM فتشير إلى مقاييس أخرى.

### q7 · `ch6_dac` · Remember

What does Data Abstraction Coupling count?

**العربية:** ماذا يعدّ Data Abstraction Coupling؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Methods inherited and available to the class | الطرق الموروثة والمتاحة للاستخدام داخل الصنف |
| B | Immediate child classes below the measured class | الأصناف الأبناء المباشرة أسفل الصنف المقاس |
| C **Correct** | Abstract data types declared within a class | أنواع البيانات المجردة المعرّفة داخل الصنف |
| D | Data values shared between the class's methods | قيم البيانات المشتركة بين طرق ذلك الصنف |

**Explanation:** DAC counts abstract data types in a class; inherited methods, child classes, and shared-variable cohesion are separate properties.

**ملاحظة:** يعدّ DAC أنواع البيانات المجردة في الصنف؛ أما الطرق الموروثة والأصناف الأبناء وتماسك المتغيرات المشتركة فخصائص أخرى.

### q8 · `ch6_lcom` · Understand

What design property does Lack of Cohesion in Methods assess?

**العربية:** ما خاصية التصميم التي يقيّمها Lack of Cohesion in Methods؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Other classes that invoke methods of this class | الأصناف الأخرى التي تستدعي طرق هذا الصنف |
| B | The class's depth within its inheritance hierarchy | عمق الصنف ضمن التسلسل الهرمي للوراثة |
| C | Messages sent by a method to other software objects | رسائل طرق الصنف الموجهة إلى الكائنات الأخرى |
| D **Correct** | How little the class's methods share instance data | مدى قلة مشاركة طرق الصنف لبيانات المثيل |

**Explanation:** LCOM examines disjoint versus shared instance-variable use among methods; coupling, inheritance depth, and message counts are different concerns.

**ملاحظة:** يفحص LCOM استخدام الطرق لمتغيرات المثيل المشتركة أو المنفصلة؛ أما الاقتران وعمق الوراثة وعدد الرسائل فموضوعات أخرى.

### q9 · `ch6_tcc_lcc` · Analyze

How does Loose Class Cohesion differ from Tight Class Cohesion?

**العربية:** بماذا يختلف Loose Class Cohesion عن Tight Class Cohesion؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | LCC also counts method pairs connected indirectly | يحسب LCC أيضاً أزواج الطرق المترابطة بصورة غير مباشرة |
| B | TCC counts all pairs whether they share data or not | يحسب TCC كل الأزواج سواء تشاركت البيانات أم لا |
| C | LCC counts immediate subclasses instead of method pairs | يحسب LCC الأصناف الفرعية المباشرة بدلاً من أزواج الطرق |
| D | TCC counts inherited methods across class hierarchies | يحسب TCC الطرق الموروثة عبر التسلسلات الهرمية للأصناف |

**Explanation:** TCC counts public method pairs sharing attributes; LCC extends this notion to include indirect connections between methods.

**ملاحظة:** يعدّ TCC أزواج الطرق العامة التي تتشارك الخصائص؛ ويوسع LCC الفكرة ليشمل الاتصالات غير المباشرة بين الطرق.

### q10 · `ch6_mood_inheritance_factors` · Understand

Which distinction separates AIF from MIF in the MOOD metrics?

**العربية:** أي تمييز يفصل AIF عن MIF في مقاييس MOOD؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | AIF concerns outgoing calls; MIF concerns incoming calls | يرتبط AIF بالاستدعاءات الصادرة وMIF بالواردة |
| B **Correct** | AIF concerns inherited attributes; MIF concerns methods | يرتبط AIF بالخصائص الموروثة وMIF بالطرق الموروثة |
| C | AIF concerns public method pairs; MIF shared variables | يرتبط AIF بأزواج الطرق العامة وMIF بالمتغيرات المشتركة |
| D | AIF concerns class depth; MIF immediate child count | يرتبط AIF بعمق الصنف وMIF بعدد الأبناء المباشرين |

**Explanation:** MOOD's Attribute Inheritance Factor concerns inherited attributes, whereas its Method Inheritance Factor concerns inherited methods.

**ملاحظة:** يتعلق Attribute Inheritance Factor في MOOD بالخصائص الموروثة، بينما يتعلق Method Inheritance Factor بالطرق الموروثة.

### q11 · `ch6_lorenz_kidd_categories` · Remember

Which categories organize Lorenz and Kidd's class-oriented metrics?

**العربية:** أي فئات تنظم مقاييس الأصناف لدى Lorenz وKidd؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Product, process, project, and predictor metric roles | أدوار مقاييس المنتج والعملية والمشروع والتنبؤ |
| B | Inputs, outputs, inquiries, and logical data files | المدخلات والمخرجات والاستعلامات وملفات البيانات المنطقية |
| C **Correct** | Size, inheritance, class internals, and class externals | الحجم والوراثة والخصائص الداخلية والخارجية للصنف |
| D | Nominal, ordinal, interval, and ratio measurement scales | مقاييس القياس الاسمي والترتيبي والفتري والنسبي |

**Explanation:** Lorenz and Kidd group OO class measures into size, inheritance, internals, and externals; the alternatives are other metric frameworks.

**ملاحظة:** يصنف Lorenz وKidd مقاييس الأصناف الكائنية إلى الحجم والوراثة والخصائص الداخلية والخارجية؛ أما البدائل فأطر أخرى.

## T09 — Use-Case Oriented Metrics

Bank file: `Quiz_Ch06_T09_Use_Case_Oriented_Metrics.json`

### q1 · `ch6_actor_simple` · Understand

In the actor-weight table, which external interface receives weight 1?

**العربية:** أي واجهة خارجية تأخذ الوزن 1 في جدول الممثلين؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Another system reached through a defined interface | نظام آخر يُستدعى عبر واجهة محددة للتعامل معه |
| B | A person using a graphical interface to interact | شخص يتفاعل مع النظام باستخدام واجهة رسومية |
| C | Another system communicating through a text protocol | نظام آخر يتواصل عبر واجهة بروتوكول نصي |
| D | A use case containing several user transactions | حالة استخدام تتضمن عدة معاملات ينفذها المستخدم |

**Explanation:** A simple actor is another system with a defined interface; text-protocol systems and people using a GUI are the other actor types.

**ملاحظة:** الممثل البسيط نظام آخر ذو واجهة محددة؛ أما أنظمة البروتوكول النصي والأشخاص مستخدمو GUI فنوعان آخران.

### q2 · `ch6_actor_average` · Understand

Which actor fits the average category?

**العربية:** أي ممثل يطابق الفئة المتوسطة وفق المقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Another system reached through a defined interface | نظام آخر يُستدعى عبر واجهة محددة للتعامل معه |
| B **Correct** | Another system using a text-protocol interface | نظام آخر يتواصل مع النظام عبر بروتوكول نصي |
| C | A person interacting through a graphical interface | شخص يتفاعل مع النظام باستخدام واجهة رسومية |
| D | A human user sending no requests to the system | مستخدم بشري لا يرسل أي طلبات إلى النظام |

**Explanation:** A text-protocol external system is an average actor; a defined interface and a human GUI represent the other types.

**ملاحظة:** يصنف المقرر النظام الخارجي ذي الواجهة النصية أو المعتمد على بروتوكول ممثلاً متوسطاً؛ وتحدد الواجهة المعرّفة ومستخدم GUI النوعين الآخرين.

### q3 · `ch6_actor_complex` · Understand

Which human interaction is assigned the highest actor weight?

**العربية:** أي تفاعل بشري يأخذ أعلى وزن للممثل؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Another system reached through a defined interface | نظام آخر يُستدعى عبر واجهة محددة للتعامل معه |
| B | Another system using a text-based protocol interface | نظام آخر يتعامل عبر واجهة بروتوكول نصي |
| C **Correct** | A person using a GUI to interact with the system | شخص يستخدم واجهة GUI للتفاعل مع النظام |
| D | A batch process without external user interaction | عملية دفعية لا تتضمن تفاعلاً مع مستخدم خارجي |

**Explanation:** A person using a graphical interface is a complex actor; the two external-system interfaces receive lower categories.

**ملاحظة:** يسمي المقرر الشخص الذي يستخدم واجهة رسومية ممثلاً معقداً؛ أما واجهتا النظام الخارجي فتحصلان على فئتين أدنى.

### q4 · `ch6_actor_weight_sum` · Understand

How is the actor-weight subtotal formed?

**العربية:** كيف يحسب المجموع الجزئي لأوزان الممثلين؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Multiply actor count by the number of transactions | ضرب عدد الممثلين بعدد المعاملات في النموذج |
| B | Add the factors assigned to each software module | جمع العوامل المسندة إلى كل وحدة برمجية في النظام |
| C | Divide actor count by the number of user screens | قسمة عدد الممثلين على عدد شاشات المستخدم |
| D **Correct** | Add the assigned weight for each counted actor | جمع الوزن المسند لكل ممثل جرى احتسابه في النموذج |

**Explanation:** Add the actor-type factors to obtain the actor weight; transaction weighting is handled separately.

**ملاحظة:** ينص المقرر على جمع عوامل أنواع الممثلين للحصول على وزن الممثلين؛ أما وزن المعاملات فيحسب على نحو منفصل.

### q5 · `ch6_simple_use_case` · Understand

How many transactions define a simple use case, and what weight applies?

**العربية:** كيف تصنف حالة الاستخدام البسيطة وتوزن في جدول المقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Three or fewer transactions, with a factor of five | ثلاث معاملات أو أقل، بعامل مقداره خمسة |
| B | Four to seven transactions, with a factor of ten | أربع إلى سبع معاملات، بعامل مقداره عشرة |
| C | More than seven transactions, with a factor of fifteen | أكثر من سبع معاملات، بعامل مقداره خمسة عشر |
| D | Three or fewer actors, with a factor of three | ثلاثة ممثلين أو أقل، بعامل مقداره ثلاثة |

**Explanation:** The simple use-case row is based on three or fewer transactions and carries a factor of five; actor categories use a different table.

**ملاحظة:** يعتمد صف حالة الاستخدام البسيطة على ثلاث معاملات أو أقل ويحمل عاملاً مقداره خمسة؛ أما فئات الممثلين فلها جدول مختلف.

### q6 · `ch6_average_use_case` · Understand

Which transaction range defines an average use case?

**العربية:** أي نطاق معاملات يحدد حالة الاستخدام المتوسطة في جدول المقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Three or fewer transactions, with a factor of five | ثلاث معاملات أو أقل، بعامل مقداره خمسة |
| B **Correct** | Four to seven transactions, with a factor of ten | أربع إلى سبع معاملات، بعامل مقداره عشرة |
| C | More than seven transactions, with a factor of fifteen | أكثر من سبع معاملات، بعامل مقداره خمسة عشر |
| D | Four to seven actors, with a factor of two | أربعة إلى سبعة ممثلين، بعامل مقداره اثنين |

**Explanation:** An average use case has four to seven transactions and factor ten; the other rows describe simple or complex cases or actor counts.

**ملاحظة:** تضم حالة الاستخدام المتوسطة أربعاً إلى سبع معاملات وعاملها عشرة؛ أما البدائل فتصف الحالات البسيطة أو المعقدة أو عدد الممثلين.

### q7 · `ch6_complex_use_case` · Understand

Which transaction count defines a complex use case?

**العربية:** أي عدد معاملات يحدد حالة الاستخدام المعقدة في جدول المقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Three transactions or fewer; use-case weight is five | ثلاث معاملات أو أقل، ووزن حالة الاستخدام خمسة |
| B | Four to seven transactions; use-case weight is ten | أربع إلى سبع معاملات، ووزن حالة الاستخدام عشرة |
| C **Correct** | More than seven transactions; use-case weight is fifteen | أكثر من سبع معاملات، ووزن حالة الاستخدام خمسة عشر |
| D | Actor class above seven; assigned actor weight is three | أكثر من سبعة ممثلين، ووزن الممثل يساوي ثلاثة |

**Explanation:** The complex use-case row has more than seven transactions and factor fifteen; the actor table is separate.

**ملاحظة:** تضم حالة الاستخدام المعقدة أكثر من سبع معاملات وعاملها خمسة عشر؛ أما جدول الممثلين فمنفصل.

### q8 · `ch6_use_case_weighting` · Apply

How are transaction-based use-case weights combined?

**العربية:** كيف تجمع أوزان حالات الاستخدام المعتمدة على المعاملات؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Count actors and multiply them by class-inheritance depth | احتساب الممثلين وضرب عددهم بعمق وراثة الأصناف |
| B | Count source lines and allocate them across project files | احتساب أسطر المصدر المقاسة وتوزيعها على ملفات المشروع |
| C | Count defects and multiply them by average execution time | احتساب العيوب وضرب عددها بمتوسط زمن التشغيل |
| D **Correct** | Count use-case classes and apply each assigned weight | عدّ فئات حالات الاستخدام وضرب كل فئة بوزنها المحدد |

**Explanation:** Each use-case type is weighted by its transaction-based factor to give an unadjusted subtotal; this is not the full adjusted UCP formula.

**ملاحظة:** يزن المقرر كل نوع من حالات الاستخدام بعامله المعتمد على المعاملات؛ وينتج بذلك المجموع الجزئي غير المعدل، لا صيغة UCP الكاملة غير الموثقة.

## T10 — Quality and Defect Metrics

Bank file: `Quiz_Ch06_T10_Quality_And_Defect_Metrics.json`

### q1 · `ch6_dre_project_formula` · Understand

What is the project-level meaning of defect removal efficiency?

**العربية:** ما معنى كفاءة إزالة العيوب على مستوى المشروع؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Pre-delivery E divided by all counted errors (E + D) | DRE للمشروع تساوي E مقسوماً على E مضافاً إليه D |
| B | Post-delivery defects divided by delivered source size | عيوب بعد التسليم مقسومة على حجم المصدر المسلّم |
| C | Pre-delivery errors divided by total project effort | أخطاء قبل التسليم مقسومة على جهد المشروع الكلي |
| D | All failures divided by the number of product releases | جميع الإخفاقات مقسومة على عدد إصدارات المنتج |

**Explanation:** Project DRE is E divided by E plus D, where E is found before delivery and D is found after delivery; it reflects defect-filtering effectiveness.

**ملاحظة:** تساوي DRE للمشروع E مقسوماً على E مضافاً إليه D؛ إذ تمثل E ما اكتشف قبل التسليم وD ما اكتشف بعده، ويعكس المقياس فاعلية تنقية العيوب.

### q2 · `ch6_dre_error_terms` · Remember

In project-level DRE, what do E and D represent?

**العربية:** ماذا يمثل E وD في DRE على مستوى المشروع؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | E is total effort; D is total development duration | تمثل E مجموع الجهد وD مدة التطوير الكلية |
| B **Correct** | E is pre-delivery errors; D is post-delivery defects | تمثل E أخطاء ما قبل التسليم وD عيوب ما بعده |
| C | E is executable lines; D is distinct data operands | تمثل E الأسطر التنفيذية وD معاملات البيانات الفريدة |
| D | E is project staff; D is delivered documentation pages | تمثل E موظفي المشروع وD صفحات التوثيق المسلّمة |

**Explanation:** Pressman's project definition separates errors found before delivery from defects found after delivery; these are the denominator's two parts.

**ملاحظة:** يفصل تعريف Pressman للمشروع بين الأخطاء المكتشفة قبل التسليم والعيوب المكتشفة بعده؛ وهما جزآ المقام.

### q3 · `ch6_dre_activity_scope` · Understand

Which two error counts enter activity-level DRE?

**العربية:** ما مجموعتا الأخطاء اللتان تدخلان في DRE على مستوى النشاط؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Release defects relative to the count of project activities | عيوب الإصدار نسبةً إلى عدد أنشطة المشروع |
| B | Design errors relative to the product's source-statement count | أخطاء التصميم نسبةً إلى عدد تعليمات مصدر المنتج |
| C **Correct** | Errors found in activity i plus escaped errors found in i+1 | أخطاء النشاط i وما تسرب منها إلى النشاط التالي |
| D | Activity effort relative to the project's total development cost | جهد النشاط نسبةً إلى كلفة التطوير الكلية للمشروع |

**Explanation:** Activity-level DRE divides errors found in activity i by those errors plus escaped defects from that activity found in the next activity.

**ملاحظة:** تقسم DRE للنشاط أخطاء النشاط i على مجموعها والعيوب المتسربة منه والمكتشفة في النشاط التالي.

### q4 · `ch6_dre_interpretation` · Analyze

What does a DRE value approaching one indicate?

**العربية:** إلى ماذا تشير قيمة DRE التي تقترب من الواحد؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | No further measurement is needed after the current phase | عدم الحاجة إلى قياس إضافي بعد المرحلة الحالية |
| B | The software has no faults under every operating condition | خلو البرمجيات من العيوب في جميع ظروف التشغيل |
| C | The product has the smallest source-code size | امتلاك المنتج أصغر حجم للشيفرة المصدرية |
| D **Correct** | Most measured errors are found before the next boundary | اكتشاف معظم الأخطاء قبل الحد المحدد للقياس |

**Explanation:** A value near one indicates effective early filtering for the defined scope; it does not prove that software has no faults under all conditions.

**ملاحظة:** تشير القيمة القريبة من الواحد إلى فاعلية التنقية المبكرة ضمن النطاق المحدد؛ ولا تثبت خلو البرمجيات من العيوب في جميع الظروف.

### q5 · `ch6_phase_containment` · Understand

What is the principle of phase containment of errors?

**العربية:** ما مبدأ احتواء الأخطاء في المرحلة؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Find errors in their phase of introduction | اكتشاف الأخطاء في المرحلة التي جرى إدخالها فيها |
| B | Delay all correction until final system testing | تأجيل التصحيح كله إلى اختبار النظام النهائي |
| C | Measure only errors visible to end users | قياس الأخطاء الظاهرة للمستخدم النهائي فقط |
| D | Move every detected error to the following phase | نقل كل خطأ مكتشف إلى مرحلة التطوير التالية |

**Explanation:** Phase containment aims to detect errors as close as possible to where they were committed, reducing later rework across phases.

**ملاحظة:** يهدف احتواء المرحلة إلى كشف الأخطاء قرب الموضع الذي أُدخلت فيه، مما يقلل إعادة العمل عبر المراحل اللاحقة.

### q6 · `ch6_defect_density` · Understand

Why express defects per KLOC or per function point?

**العربية:** لماذا يعبر عن العيوب لكل KLOC أو لكل نقطة وظيفة؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Convert defect counts into execution time | تحويل عدد العيوب إلى زمن تنفيذ منقضٍ |
| B **Correct** | Relate defect counts to measured product size | مقارنة عدد العيوب بحجم المنتج المقاس |
| C | Replace identification of the measured release | استبدال تحديد إصدار المنتج الذي جرى قياسه |
| D | Equalize product sizes before comparison | مساواة أحجام المنتجات المختلفة قبل المقارنة |

**Explanation:** A size denominator makes defect counts interpretable relative to product size; raw counts alone do not normalize differently sized products.

**ملاحظة:** يجعل مقام الحجم عدد العيوب قابلاً للتفسير نسبةً إلى حجم المنتج؛ فالعدد الخام وحده لا يطبع أحجام المنتجات المختلفة.

### q7 · `ch6_defect_per_kloc` · Understand

Which denominator is used by a defects-per-KLOC metric?

**العربية:** أي مقام يستخدمه مقياس العيوب لكل KLOC؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | The number of methods in its largest class | عدد الطرق المعرفة في أكبر صنف بالمنتج |
| B | The actor count in the product's use-case model | عدد الممثلين في نموذج حالات استخدام المنتج |
| C **Correct** | Thousands of source lines in the measured product | آلاف أسطر المصدر الموجودة في المنتج المقاس |
| D | Operating hours between consecutive failures | زمن التشغيل بين الإخفاقات المتعاقبة |

**Explanation:** Defects per KLOC normalizes a defect count by thousands of source lines; function points provide a different size denominator.

**ملاحظة:** يقسم مقياس العيوب لكل KLOC عدد العيوب على آلاف الأسطر البرمجية؛ أما نقاط الوظائف فمقام حجم مختلف.

### q8 · `ch6_defect_per_fp` · Understand

What does a defects-per-function-point measure normalize?

**العربية:** ما الذي يطبّعه مقياس العيوب لكل نقطة وظيفة؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Defects measured by elapsed time between failures | عدد العيوب بحسب الزمن المنقضي بين الإخفاقات |
| B | Project staffing measured by output-report count | توظيف المشروع بحسب عدد تقارير المخرجات |
| C | Class complexity by depth in its inheritance hierarchy | تعقيد الصنف بحسب عمق تسلسل الوراثة الخاص به |
| D **Correct** | Defects relative to delivered functional size | عدد العيوب نسبةً إلى الحجم الوظيفي المسلّم |

**Explanation:** The function-point denominator relates defects to functional size; KLOC is a code-size denominator rather than a functional one.

**ملاحظة:** يربط مقام نقاط الوظائف العيوب بالحجم الوظيفي؛ أما KLOC فيمثل مقاماً لحجم الشيفرة لا للحجم الوظيفي.

### q9 · `ch6_mtbf_product_measure` · Understand

What does Mean Time Between Failures describe as a product measure?

**العربية:** ماذا يصف Mean Time Between Failures بوصفه مقياساً للمنتج؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Average operating time between successive failures | متوسط زمن التشغيل بين الإخفاقات المتعاقبة |
| B | Faults introduced during one development phase | العيوب المدخلة أثناء مرحلة تطوير واحدة |
| C | Calendar time required to complete a product release | الزمن التقويمي اللازم لإكمال إصدار المنتج |
| D | Average executable statements within one module | متوسط التعليمات التنفيذية داخل وحدة برمجية واحدة |

**Explanation:** MTBF concerns elapsed operating time between failures and is used as a reliability-oriented product measure; it is not a defect count or project schedule.

**ملاحظة:** يتعلق MTBF بزمن التشغيل بين الإخفاقات ويستخدم مقياساً للمنتج مرتبطاً بالاعتمادية؛ وليس عدّاً للعيوب أو جدولاً للمشروع.

### q10 · `ch6_dre_unit_scope` · Analyze

Within a defined observation scope, what does a DRE of one imply?

**العربية:** ضمن نطاق رصد محدد، ماذا تعني قيمة DRE تساوي واحداً؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | No defect can exist under any operating condition | استحالة وجود أي عيب تحت جميع ظروف التشغيل |
| B **Correct** | No counted error escaped the defined boundary | لم يتسرب أي خطأ معدود عبر الحد المحدد في القياس |
| C | The project needed no effort after its first phase | عدم حاجة المشروع إلى جهد بعد مرحلته الأولى |
| D | The product has the smallest possible source size | امتلاك المنتج أصغر حجم ممكن للشيفرة المصدرية |

**Explanation:** For the defined pre/post boundary and observation window, DRE equal to one means no counted defect escaped that boundary; it does not prove universal absence of faults.

**ملاحظة:** ضمن حدّ الرصد والفترة المحددين، تعني DRE التي تساوي واحداً أن أياً من العيوب المعدودة لم يتسرب عبر الحد؛ ولا تثبت غياب العيوب مطلقاً.

## T11 — Productivity and Process Metrics

Bank file: `Quiz_Ch06_T11_Productivity_And_Process_Metrics.json`

### q1 · `ch6_productivity_ratio` · Understand

What relationship defines a software productivity measure?

**العربية:** ما العلاقة التي تعرّف مقياس إنتاجية البرمجيات؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | A stated software output divided by the effort used | مخرج برمجي محدد مقسوماً على الجهد المستخدم |
| B | A defect total divided by elapsed operating time | مجموع العيوب مقسوماً على زمن التشغيل المنقضي |
| C | A source length multiplied by control-flow complexity | طول المصدر مضروباً بتعقيد تدفق التحكم |
| D | A class count divided by the depth of inheritance | عدد الأصناف مقسوماً على عمق الوراثة |

**Explanation:** Productivity relates an output measure to the effort used to produce it; defect rate, complexity, and inheritance answer different questions.

**ملاحظة:** تربط الإنتاجية مقياساً للمخرج بالجهد المستخدم لإنتاجه؛ أما معدل العيوب والتعقيد والوراثة فتجيب عن أسئلة أخرى.

### q2 · `ch6_loc_person_month` · Understand

What does LOC per person-month express?

**العربية:** ماذا يعبر عنه LOC لكل شخص-شهر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Failure intervals observed during one calendar month | فترات الإخفاق المرصودة خلال شهر تقويمي واحد |
| B **Correct** | Source lines produced per person-month of effort | أسطر المصدر المنجزة لكل شخص-شهر من الجهد |
| C | Distinct operators counted in each software module | العوامل المتميزة المعدودة في كل وحدة برمجية |
| D | Project cost per external function-point component | كلفة المشروع لكل مكوّن خارجي لنقاط الوظائف |

**Explanation:** LOC per person-month uses code size as output and person-months as effort; it is sensitive to the LOC counting convention and language.

**ملاحظة:** يستعمل LOC لكل شخص-شهر حجم الشيفرة مخرجاً وأشهر العمل جهداً؛ ويتأثر بقاعدة عد LOC ولغة البرمجة.

### q3 · `ch6_fp_person_month` · Understand

What does function points per person-month express?

**العربية:** ماذا تعبر عنه نقاط الوظائف لكل شخص-شهر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Functional size divided by post-release defect count | الحجم الوظيفي مقسوماً على عدد عيوب ما بعد الإصدار |
| B | Source lines divided by the number of inheritance levels | أسطر المصدر مقسومة على عدد مستويات الوراثة |
| C **Correct** | Functional size delivered relative to development effort | الحجم الوظيفي المسلّم نسبةً إلى جهد التطوير |
| D | Elapsed failure time divided by project schedule duration | زمن الإخفاق المنقضي مقسوماً على مدة جدول المشروع |

**Explanation:** FP per person-month relates delivered function-point size to development effort; it measures productivity rather than defects or complexity.

**ملاحظة:** تربط FP لكل شخص-شهر حجم نقاط الوظائف المسلّم بجهد التطوير؛ فهي تقيس الإنتاجية لا العيوب أو التعقيد.

### q4 · `ch6_loc_language_effect` · Analyze

Why should LOC-based productivity be compared cautiously across languages?

**العربية:** لماذا ينبغي مقارنة الإنتاجية المعتمدة على LOC بحذر بين اللغات؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Every language uses the same statement and line structure | تستخدم كل لغة بنية التعليمات والأسطر نفسها |
| B | Function points are counted only from runtime failures | تُحسب نقاط الوظائف من إخفاقات التشغيل وحدها |
| C | LOC directly records customer transaction totals | يسجل LOC مباشرة العدد الكلي لمعاملات العميل |
| D **Correct** | Equivalent features may need different LOC by language | قد تختلف LOC للوظيفة المكافئة حسب اللغة |

**Explanation:** The LOC-to-function relationship varies by language, so line-based productivity values are not directly comparable without context.

**ملاحظة:** تختلف العلاقة بين LOC والوظائف باختلاف اللغة؛ لذلك لا تقارن قيم الإنتاجية القائمة على الأسطر مباشرةً من دون سياق.

### q5 · `ch6_effort_distribution` · Understand

What does effort distribution across phases summarize?

**العربية:** ماذا يلخص توزيع الجهد عبر المراحل؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | How project effort is allocated among lifecycle activities | كيفية توزيع جهد المشروع بين أنشطة دورة الحياة |
| B | How software functions are divided among external actors | كيفية تقسيم وظائف البرمجيات بين الممثلين الخارجيين |
| C | How variable references are spaced across statements | كيفية تباعد إحالات المتغيرات عبر التعليمات |
| D | How classes are arranged across inheritance levels | كيفية ترتيب الأصناف عبر مستويات الوراثة |

**Explanation:** Effort distribution describes the allocation of project effort to lifecycle activities or phases; the other options describe different structures.

**ملاحظة:** يصف توزيع الجهد تخصيص جهد المشروع لأنشطة أو مراحل دورة الحياة؛ أما البدائل فتصف بنى مختلفة.

### q6 · `ch6_late_rework` · Analyze

Why can late defect discovery increase project effort?

**العربية:** لماذا قد يزيد اكتشاف العيب المتأخر جهد المشروع؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Late discovery automatically reduces the source-code size | ينخفض حجم المصدر تلقائياً عند اكتشاف العيب متأخراً |
| B **Correct** | Earlier outputs and dependent later work may need revision | قد يلزم تعديل مخرجات سابقة وأعمال لاحقة معتمدة عليها |
| C | Late discovery changes the project's function-point weights | تتغير أوزان نقاط الوظائف عند اكتشاف العيب متأخراً |
| D | Late discovery removes the need for regression testing | يلغي الاكتشاف المتأخر الحاجة إلى اختبار الانحدار |

**Explanation:** When an error escapes its phase, correction may require reworking downstream design, code, and tests; this is why phase containment matters.

**ملاحظة:** عندما يتسرب الخطأ من مرحلته قد يتطلب التصحيح إعادة عمل التصميم والشيفرة والاختبارات اللاحقة؛ لذلك تبرز أهمية احتواء المرحلة.

### q7 · `ch6_process_maturity` · Understand

What does process maturity describe?

**العربية:** ماذا يصف نضج العملية في تصنيفات المقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | The operator count in a finished source program | عدد العوامل في البرنامج المصدري المكتمل |
| B | The screen count in the product's user interface | عدد الشاشات في واجهة المستخدم للمنتج |
| C **Correct** | Maturity of the process used to produce the software | نضج العملية المستخدمة لإنتاج البرمجيات |
| D | Reliability of a hardware component outside the product | اعتمادية مكوّن عتادي يقع خارج المنتج |

**Explanation:** Process maturity is a process metric; the other choices describe product size or an external component.

**ملاحظة:** يورد المقرر نضج العملية ضمن مقاييس العملية؛ أما البدائل فتصف حجم المنتج أو مكوّناً خارجياً.

### q8 · `ch6_productivity_vs_complexity` · Analyze

Why should productivity metrics not be confused with complexity metrics?

**العربية:** لماذا يجب عدم الخلط بين مقاييس الإنتاجية ومقاييس التعقيد؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Both always measure source length in the same manner | كلاهما يقيس طول المصدر دائماً بالطريقة نفسها |
| B | Complexity values directly equal project productivity | تساوي قيم التعقيد إنتاجية المشروع مباشرةً |
| C | Productivity values replace all software-size measures in every context | تحل الإنتاجية محل مقاييس حجم البرمجيات |
| D **Correct** | They describe distinct properties with different meanings | تقيس خصائص مختلفة وتحتاج إلى تفسير منفصل |

**Explanation:** Productivity should not be confused with complexity: output per effort differs from control-flow or structure measures.

**ملاحظة:** يحذر المقرر صراحةً من الخلط بين الإنتاجية والتعقيد؛ فمعدل المخرج لكل جهد ليس مقياساً لتدفق التحكم أو البنية.

## T12 — Metrics Analysis and Program

Bank file: `Quiz_Ch06_T12_Metrics_Analysis_And_Program.json`

### q1 · `ch6_summary_statistics` · Remember

Which items are summary statistics listed for metric analysis?

**العربية:** أي عناصر تمثل إحصاءات موجزة أوردها تحليل المقاييس؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | Mean, median, maximum, and minimum values for a measure | قيم المتوسط والوسيط والحدين الأعلى والأدنى للمقياس |
| B | Class metrics: fan-in, fan-out, DIT, and NOC counts | مقاييس الأصناف: أعداد fan-in وfan-out وDIT وNOC |
| C | Function-point items: inputs, outputs, inquiries, and files | عناصر نقاط الوظائف: مدخلات ومخرجات واستعلامات وملفات |
| D | Use-case items: actors, transactions, screens, and reports | عناصر حالات الاستخدام: ممثلون ومعاملات وشاشات وتقارير |

**Explanation:** Mean, median, maximum, and minimum are summary statistics; the alternatives are software metrics or sizing terms.

**ملاحظة:** يسمي المقرر المتوسط والوسيط والقيمتين العظمى والصغرى إحصاءات موجزة؛ أما البدائل فمصطلحات لمقاييس أو أحجام برمجية.

### q2 · `ch6_histogram` · Understand

Which representation is listed for displaying metric-data distributions?

**العربية:** أي تمثيل ورد لعرض توزيعات بيانات المقاييس؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | A call graph showing module-to-module relationships | مخطط استدعاء يعرض علاقات الوحدات البرمجية |
| B **Correct** | A histogram displaying metric-value distributions | مدرج تكراري يعرض توزيع قيم بيانات المقاييس |
| C | A cross-reference table showing variable line locations | جدول إحالات متقاطعة يعرض مواضع المتغيرات في الأسطر |
| D | A class hierarchy showing inheritance depth | تسلسل هرمي للأصناف يوضح عمق الوراثة بينها |

**Explanation:** Histograms are listed as graphical summaries for metric data; call graphs, cross-reference tables, and class hierarchies show other structures.

**ملاحظة:** ترد المدرجات التكرارية ملخصاتٍ رسومية لبيانات المقاييس؛ أما مخططات الاستدعاء وجداول الإحالة وتسلسلات الأصناف فتعرض بنى أخرى.

### q3 · `ch6_box_plot` · Remember

Which graphic can summarize distributions of metric data?

**العربية:** أي تقنية رسومية مدرجة صراحةً ضمن قائمة التحليل بالمقرر؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Control-flow graphs for counting source-code regions | مخططات تدفق التحكم لعدّ مناطق الشيفرة |
| B | Use-case diagrams for weighting user transactions | مخططات استخدام لوزن معاملات المستخدم |
| C **Correct** | Box plots for summarizing measured metric values | مخططات الصندوق لتمثيل بيانات القياس |
| D | Class diagrams for assessing actor-system complexity | مخططات أصناف لتقييم تعقيد ممثلي النظام |

**Explanation:** Box plots summarize distributions alongside histograms and pie charts.

**ملاحظة:** تلخص مخططات الصندوق التوزيعات إلى جانب المدرجات التكرارية والمخططات الدائرية.

### q4 · `ch6_pca` · Understand

Which technique transforms correlated metric variables into principal components?

**العربية:** أي تقنية تحول المتغيرات المترابطة إلى مكونات رئيسية؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Phase containment analysis across lifecycle stages | تحليل احتواء الأخطاء بين مراحل دورة الحياة |
| B | Object-point adjustment for application features | تحليل تعديل نقاط الكائنات وخصائص التطبيق |
| C | Program weakness analysis across software modules | تحليل ضعف البرنامج عبر وحداته البرمجية |
| D **Correct** | Principal component analysis for metric data | تحليل المكونات الرئيسية لبيانات المقاييس |

**Explanation:** Principal component analysis transforms correlated variables into orthogonal principal components.

**ملاحظة:** يحوّل تحليل المكونات الرئيسية المتغيرات المترابطة إلى مكونات رئيسية متعامدة.

### q5 · `ch6_correlation_interpretation` · Analyze

What conclusion is not justified by correlation alone?

**العربية:** أي استنتاج لا تبرره علاقة الارتباط وحدها؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | That correlation alone proves one attribute caused another | أن الارتباط وحده يثبت تسبب خاصية بتغير الأخرى |
| B | That measured observations vary together within the sample | أن المشاهدات المقاسة تتغير معاً ضمن بيانات العينة |
| C | That the observed relationship deserves further investigation | أن العلاقة المرصودة تستحق فحصاً إضافياً بالأدلة |
| D | That the sample shows a statistical association between measures | أن العينة تظهر ارتباطاً إحصائياً بين المقاييس |

**Explanation:** Correlation describes association, not causation; causal claims need additional design or evidence beyond a correlated metric trend.

**ملاحظة:** يصف الارتباط التلازم لا السببية؛ فالادعاء السببي يحتاج تصميماً أو دليلاً إضافياً يتجاوز اتجاه المقاييس المترابطة.

### q6 · `ch6_regression_analysis` · Understand

What does regression analysis help examine in metric data?

**العربية:** بماذا يساعد تحليل الانحدار عند فحص بيانات المقاييس؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Immediate child count in a software class hierarchy | عدد الأبناء المباشرين في تسلسل أصناف البرمجيات |
| B **Correct** | A modeled relationship among measured variables | علاقة ممثلة بنموذج بين متغيرات جرى قياسها |
| C | The operator count within a source-code procedure | عدد العوامل الموجودة ضمن إجراء في الشيفرة |
| D | Transaction count within a single use case | عدد المعاملات الموجودة ضمن حالة استخدام واحدة |

**Explanation:** Regression and correlation are listed among analysis techniques for metric data; the other choices are counts from unrelated metric families.

**ملاحظة:** يرد الانحدار والارتباط ضمن تقنيات تحليل بيانات المقاييس؛ أما البدائل فهي أعداد من عائلات مقاييس أخرى.

### q7 · `ch6_outlier` · Analyze

Why should an outlier be examined before pooling project metrics?

**العربية:** لماذا ينبغي فحص القيمة الشاذة قبل جمع مقاييس المشاريع؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | It proves the chosen scale is nominal without review | تثبت أن المقياس المختار اسمي دون أي مراجعة |
| B | It identifies the most productive project without context | تحدد المشروع الأعلى إنتاجية دون النظر إلى سياقه |
| C **Correct** | It may distort summaries or fitted metric-data models | قد تشوه الملخصات أو النماذج المقدرة للبيانات |
| D | It removes the need to compare project characteristics | تلغي الحاجة إلى مقارنة خصائص المشاريع |

**Explanation:** Outliers are explicitly listed as a metric-data problem and can affect summaries or fitted relationships, so they need contextual review.

**ملاحظة:** ترد القيم الشاذة صراحةً مشكلةً في بيانات المقاييس وقد تؤثر في الملخصات أو العلاقات المقدرة، لذلك تحتاج مراجعة سياقية.

### q8 · `ch6_metric_data_problems` · Remember

Which group contains problems named for metric-data analysis?

**العربية:** أي مجموعة تضم مشكلات مسماة لتحليل بيانات المقاييس؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Inheritance depth, method response, and child-class count | عمق الوراثة واستجابة الطرق وعدد الأصناف الأبناء |
| B | Input files, output files, and transaction totals | ملفات الإدخال وملفات الإخراج ومجاميع المعاملات |
| C | Source length, actor weight, and the project schedule | طول المصدر ووزن الممثل والجدول الزمني للمشروع |
| D **Correct** | Distribution, outliers, measurement scale, collinearity | التوزيع والقيم الشاذة والمقياس والتعدد الخطي |

**Explanation:** Metric-data analysis can require distribution assumptions, outlier checks, a suitable measurement scale, and attention to multicollinearity.

**ملاحظة:** يورد المقرر مشكلات التوزيع الطبيعي والقيم الشاذة ومقياس القياس والتعدد الخطي ضمن مشكلات تحليل البيانات.

### q9 · `ch6_common_pool_representative` · Analyze

How should projects be selected for a common metric-data pool?

**العربية:** كيف ينبغي اختيار المشاريع لمجموعة بيانات مقاييس مشتركة؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A **Correct** | A representative mix of domains and development styles | مزيج ممثل من مجالات التطبيق وأساليب تطوير المشاريع |
| B | Projects from one application domain and one style only | مشاريع من مجال تطبيق واحد وأسلوب تطوير واحد فقط |
| C | Only the largest available software-development project | اختيار أكبر مشروع تطوير فقط من المجموعة المتاحة |
| D | Projects whose metric definitions are missing or unclear | مشاريع تفتقر إلى تعريفات واضحة للمقاييس المستخدمة |

**Explanation:** Use a representative project pool rather than one drawn from a single domain or development style.

**ملاحظة:** يوصي المقرر بمجموعة مشاريع ممثلة بدلاً من مجموعة تأتي من مجال واحد أو أسلوب تطوير واحد.

### q10 · `ch6_common_pool_dominance` · Understand

What should be prevented when assembling a common project-data pool?

**العربية:** ما الذي ينبغي منعه عند إعداد مجموعة بيانات مشاريع مشتركة؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Projects representing different application domains | مشاريع تمثل مجالات تطبيق مختلفة في المجموعة |
| B **Correct** | One large project outweighing the rest of the pool | هيمنة مشروع كبير على بقية بيانات المجموعة |
| C | Projects with missing metric values being identified | تحديد المشاريع التي تفتقر إلى بعض قيم المقاييس |
| D | Projects being collected by an automated process | جمع بيانات المشاريع بواسطة عملية مؤتمتة |

**Explanation:** A single very large project can distort the mix represented in a common pool, so it should not dominate the data.

**ملاحظة:** يحذر المقرر من هيمنة مشروع كبير جداً على المجموعة المشتركة، لأن ذلك يشوه مزيج المشاريع الممثل.

### q11 · `ch6_metrics_program_automation` · Understand

Which practice is highlighted for a successful metrics program?

**العربية:** أي ممارسة يبرزها المقرر لنجاح برنامج المقاييس؟

| Key | English option | الخيار العربي |
|:---:|:---|:---|
| A | Use one measure while discarding its historical context | استخدام مقياس واحد مع إهمال سياقه التاريخي |
| B | Collect every value manually only after product release | جمع كل قيمة يدوياً بعد إصدار المنتج فقط |
| C **Correct** | Automate collection and retire measures that lose value | أتمتة الجمع وإيقاف المقاييس التي تفقد فائدتها |
| D | Keep every metric unchanged regardless of its usefulness | إبقاء كل مقياس دون تغيير بصرف النظر عن فائدته |

**Explanation:** A successful metrics program automates collection, matures and maintains measures, and retires those that no longer serve a purpose.

**ملاحظة:** يؤكد المقرر الأتمتة والمقاييس متعددة العوامل ونضج المقاييس وصيانتها وإيقاف ما لم يعد منها مفيداً.
