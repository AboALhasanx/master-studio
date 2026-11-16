# Chapter 6 — Software Metrics

**Skeleton**

- **Define the vocabulary.** A measure assigns a value to an attribute; measurement is the act; a metric is a measure obtained by a defined method and scale; an indicator is a metric interpreted against a goal.
- **Fix the scale.** Nominal, ordinal, interval, ratio, absolute. Only ratio and absolute scales support meaningful ratios and percentages; averaging an ordinal scale is a category error.
- **State the representation condition.** A metric is valid when the numerical relation mirrors the empirical relation, so the statement remains true under admissible transformation.
- **Tie measurement to goals.** GQM: define the Goal, derive the Questions that would answer it, then choose the Metrics that answer those questions.
- **Classify metrics.** Product, process, project; internal versus external attributes; predictor versus control.
- **Measure size.** LOC/KLOC for physical size, function points for functional size, object points for early prototyping, and backfiring only as an approximation.
- **Measure structure.** Halstead for lexical content, data-structure metrics for live variables and span, information flow for fan-in and fan-out, McCabe for control-flow complexity, CK for object-oriented design.
- **Measure quality and defect behaviour.** Defect density, defect removal efficiency, phase containment, MTBF.
- **Warn about dysfunction.** Any metric used as a target is gamed; measurement must never be used to rank individuals without context.

**Keywords**

- **Measure / measurement / metric** — Value, act, defined method — <span dir="rtl">قياس / عملية القياس / مقياس</span>
- **Indicator** — Metric interpreted against a goal — <span dir="rtl">مؤشر</span>
- **Scale** — Nominal, ordinal, interval, ratio, absolute — <span dir="rtl">مقياس القياس</span>
- **Representation condition** — Numerical relation mirrors empirical relation — <span dir="rtl">شرط التمثيل</span>
- **GQM** — Goal-driven metric selection — <span dir="rtl">هدف، سؤال، مقياس</span>
- **Product / process / project metric** — Artifact, activity, management — <span dir="rtl">مقياس منتج / عملية / مشروع</span>
- **Internal / external attribute** — Visible from code vs from use — <span dir="rtl">سمة داخلية / خارجية</span>
- **Predictor / control metric** — Forecast vs monitor — <span dir="rtl">مقياس تنبؤي / ضابط</span>
- **LOC / KLOC** — Physical size — <span dir="rtl">أسطر الشيفرة</span>
- **Function point** — Functional size, language-independent — <span dir="rtl">نقطة وظيفية</span>
- **Backfiring** — LOC to FP approximation — <span dir="rtl">التحويل العكسي</span>
- **Halstead** — Operators, operands, volume, difficulty, effort — <span dir="rtl">علم البرمجيات لهالستد</span>
- **Live variable** — Defined and used later before redefinition — <span dir="rtl">متغير حي</span>
- **Information flow** — Fan-in and fan-out weighted by size — <span dir="rtl">تدفق المعلومات</span>
- **Cyclomatic complexity** — V(G) from the control-flow graph — <span dir="rtl">التعقيد الدوري</span>
- **CK suite** — WMC, DIT, NOC, CBO, RFC, LCOM — <span dir="rtl">مجموعة تشيدامبر وكيمرر</span>
- **Use case points** — Actor and use-case weighted size — <span dir="rtl">نقاط حالات الاستخدام</span>
- **Defect density** — Defects per KLOC or per function point — <span dir="rtl">كثافة العيوب</span>
- **DRE** — Share of defects removed before delivery — <span dir="rtl">كفاءة إزالة العيوب</span>
- **Phase containment** — Defects caught in the phase that created them — <span dir="rtl">الاحتواء المرحلي</span>

**Facts, numbers, formulas**

- **Halstead suite.** With $\eta_1$ unique operators, $\eta_2$ unique operands, $N_1$ total operators and $N_2$ total operands:

$$\eta=\eta_1+\eta_2,\qquad N=N_1+N_2,\qquad \hat{N}=\eta_1\log_2\eta_1+\eta_2\log_2\eta_2$$

$$V=N\log_2\eta,\qquad D=\frac{\eta_1}{2}\cdot\frac{N_2}{\eta_2},\qquad L=\frac{1}{D},\qquad E=DV,\qquad T=\frac{E}{18}$$

The Stroud number is 18 elementary mental discriminations per second; the Halstead defect constant is about 3000 discriminations per fault.

- **Data-structure metrics.** $\overline{LV}=\frac{1}{n}\sum LV(S_i)$; $\gamma=\frac{\sum LV(S_i)}{\text{total variables}}$; $WM=\overline{LV}\times\gamma$; $WP=\frac{1}{m}\sum WM_i$; variable span $SP=b-a-1$ between successive references at statements $a$ and $b$.
- **Information flow (Henry–Kafura).** $IF=(\text{fan-in}\times\text{fan-out})^{2}\times\text{length}$; the IF4 variant adds data complexity to the length weighting. High fan-out signals dependence on many callees; high fan-in signals a reused shared service.
- **McCabe.** V(G) = E - N + 2P; equivalently V(G) = predicate nodes + 1 (valid when every predicate has two exits); equivalently the number of bounded regions in the flow graph.
- **Function points.** $UFP=\sum(\text{count}\times\text{weight})$ over ILF, EIF, EI, EO, EQ; $VAF=0.65+0.01\sum_{i=1}^{14}F_i$; $FP=UFP\times VAF$.
- **Use case points.** $UUCP=UAW+UUCW$; $TCF=0.6+0.01\sum TF$; $ECF=1.4-0.03\sum EF$; $UCP=UUCP\times TCF\times ECF$; effort $=UCP\times$ productivity rate.
- **CK suite.** WMC (weighted methods per class), DIT (depth of inheritance tree), NOC (number of children), CBO (coupling between objects), RFC (response for a class), LCOM (lack of cohesion in methods).
- **Quality metrics.** Defect density = dfrac{defects}{KLOC or FP}; DRE = dfrac{E}{E+D} where E is defects found before delivery and D after; phase containment effectiveness = dfrac{defects found in phase}{defects present at phase entry}; MTBF = dfrac{total operating time}{number of failures}.

**Metric at a glance — what it sees, what it ignores**

| Metric | Measures | Ignores |
|:--|:--|:--|
| LOC / KLOC | Physical volume | Language, style, reuse |
| Function points | Delivered functional size | Algorithmic difficulty |
| Halstead | Lexical vocabulary and effort | Control flow and design |
| Data-structure metrics | Live variables, span, weakness | Inter-module structure |
| Information flow | Fan-in and fan-out weighted by size | Data semantics |
| Cyclomatic V(G) | Branching and basis paths | Data complexity and nesting depth |
| CK suite | Class design: size, inheritance, coupling, cohesion | System-level architecture |
| Use case points | Actor and use-case driven size | Non-functional constraints |
| Defect density | Field or test defect concentration | Severity and cost |
| DRE | Removal effectiveness before delivery | Defects never reported |

**Traps**

- **Averaging an ordinal scale.** "Average severity 2.4" is meaningless; ordinal values rank only.
- **Calling LOC a productivity metric.** LOC is a size metric; productivity is size per unit effort, and even then LOC favours verbose code.
- **Confusing V with hat{N}.** V is measured volume; hat{N} is an *estimate* of length from vocabulary. They answer different questions.
- **Using V(G) = E - N + 2 when the graph is disconnected.** The 2P term matters; P is the number of connected components.
- **Treating $D=1/L$ and $D=\eta_1N_2/2\eta_2$ as different metrics.** They are the same quantity expressed two ways.
- **Equating CK's CBO with fan-out.** CBO counts coupled classes, not calls; RFC counts the response set, including inherited methods.
- **Using DRE without the denominator definition.** DRE = E/(E+D) only makes sense when E and D are counted over the same delivery boundary.
- **Assuming a metric is valid because it is popular.** Validity is theoretical (construct) and empirical (correlational), and both must be argued.

**Three lines**
No metric without a scale, a goal, and a validity argument.
Halstead measures vocabulary, McCabe measures branching, CK measures design, and function points measure delivered function — never substitute one for another.
Every metric used as a target will be gamed; say so before you recommend one.

**Definitions to quote**

| Term | Definition | بالعربي |
|:--|:--|:--|
| Measure / metric / indicator | Attribute value, defined method, goal-interpreted metric | قيمة ثم مقياس |
| GQM | Goal, question, metric: choosing metrics from a stated goal | الهدف يقود المقياس |
| Halstead volume | Program volume from length and vocabulary, in bits | حجم المفردات |
| Cyclomatic complexity | Independent paths in the control-flow graph | التفرع المستقل |
| CK suite | Six class metrics including WMC, DIT, CBO and LCOM | مقاييس الأصناف |
| DRE | Defects removed before delivery over all defects found | كفاءة الإزالة |
| Internal / external attribute | Measurable from the artifact alone versus from its use | داخلية وخارجية |
| Predictor / control metric | Forecasts a later attribute versus monitors a running process | تنبؤي وضابط |

**Quick distinctions**

- **Scale decides the statistic.** Nominal allows only equality, ordinal only order, interval allows differences, ratio allows ratios, absolute is counted. A mean is legal only from interval upward.
- **Halstead's standing.** Elegant and cheap, but sensitive to counting conventions and weakly validated across languages; report it alongside $V(G)$, never alone.
- **CK reading.** DIT and NOC describe inheritance shape, CBO and RFC describe coupling, LCOM describes cohesion, WMC describes class size. High values are not automatically bad; context decides.
- **UCP versus FP.** Both measure functional size; UCP weights actors and use cases and is cheaper early, FP weights data and transaction functions and is more granular.

- **Direct versus indirect.** Direct measures need one attribute; indirect measures combine several, which is why they must be validated before they are trusted.
- **Predictor versus control.** A predictor metric forecasts a later attribute; a control metric monitors an ongoing process. Using a predictor as a control turns a forecast into a target.
- **Measurement programme.** Baseline first, collect consistently, review the data with the people who produce it, and never publish individual rankings.

- **Metric categories.** Product measures the artifact, process measures the activity, project measures management: size, effort, schedule and risk.
- **LOC criticism.** It rewards verbosity, ignores language level, punishes reuse, and cannot be counted before code exists.
- **Use case point steps.** Classify actors and use cases, weight them, sum to UUCP, apply TCF and ECF, then multiply by a productivity rate.
- **Baseline.** A frozen measurement snapshot used for comparison; without it, any trend claim is an anecdote.

**Question patterns**

- **"Compute Halstead"** → count unique and total operators and operands, then η, N, V, D, L, E, T. Keep the units: bits for volume, discriminations for effort, seconds for time.
- **"Compute cyclomatic complexity"** → $V(G)=E-N+2P$; cross-check with predicate nodes plus one and with the region count. If the three disagree, the graph is wrong.
- **"Which metric for this question?"** → size: LOC or FP; vocabulary: Halstead; data: live variables and span; structure: fan-in and fan-out; branching: $V(G)$; design: CK; early size: use case points.
- **"Is this metric valid?"** → argue the representation condition and the empirical correlation, then name the scale. A metric without a scale cannot be averaged.
- **"Apply GQM"** → state the goal, derive the questions that would answer it, then choose the minimum set of metrics. Metrics precede goals only in bad organisations.
- **"Measure an OO design"** → WMC, DIT, NOC, CBO, RFC, LCOM, and interpret direction: deep trees raise complexity, high CBO raises change impact, high LCOM signals a split.
- **"Report quality"** → defect density normalised by size, DRE across the delivery boundary, phase containment per phase, MTBF from field data. Name the denominator every time.
- **"What is the risk of this metric?"** → measurement dysfunction. Any metric used as a target is gamed, so pair every productivity metric with a quality metric.
- **"Compare internal and external attributes"** → internal are measurable from the artifact alone, external only from its use, and only external ones predict user experience.

## الاسترجاع
AR:القياس ليس جمع أرقام، بل تعريف على مقياس صحيح واستخدام لهدف معلن. المقياس قيمة تُنسب إلى سمة، والقياس فعل، والمؤشر مقياس مُفسَّر مقابل هدف. والمقاييس خمسة: اسمي وترتيبي وفاصلي ونسبي ومطلق، ولا يجوز حساب متوسط على مقياس ترتيبي لأنه لا يحمل مسافات متساوية. وشرط التمثيل يقول إن المقياس صالح حين تعكس علاقاته الرقمية العلاقات التجريبية، ويُختار المقياس بطريقة GQM: هدف ثم أسئلة ثم مقاييس تجيب عنها. وتُصنَّف المقاييس إلى منتج وعملية ومشروع، وداخلية وخارجية، وتنبؤية وضابطة. ثم تأتي عائلة القياس: Halstead يقيس المفردات والجهد الذهني، ومقاييس بنية البيانات تقيس المتغيرات الحية والامتداد وضعف الوحدة، وتدفق المعلومات يقيس الدخول والخروج، وMcCabe يقيس التفرع بعدد المسارات المستقلة، ومجموعة CK تقيس تصميم الأصناف، ونقاط حالات الاستخدام تقيس الحجم الوظيفي. وتُغلق بالجودة والعيوب: كثافة العيوب وكفاءة الإزالة والاحتواء المرحلي ومتوسط الزمن بين الفشل. وأي مقياس يُتخذ هدفاً يُلعب به، فالقياس بلا سياق قرار خاطئ.
