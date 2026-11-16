# Chapter 5 — Software Design

**Skeleton**

- **Separate the two designs.** Conceptual design establishes the architecture and the "what"; technical design fixes interfaces, data structures, algorithms, and the "how". Skipping design produces code-and-fix and spaghetti.
- **State the objectives.** Correctness, efficiency, maintainability, understandability, modularity, and traceability to requirements.
- **Establish modularity.** Decompose by information hiding (Parnas): each module hides a design decision likely to change. Add abstraction (procedural, data, control) and stepwise refinement (Wirth).
- **Judge the structure.** Coupling must be low and cohesion high, and the two move inversely. Measure fan-in, fan-out, depth, and width.
- **Choose a strategy.** Top-down (decompose from the whole), bottom-up (compose from reusable parts), or hybrid. Top-down gives early architectural control; bottom-up gives early tested components.
- **Derive the structure chart.** Transform analysis splits input → transform centre → output; transaction analysis makes a dispatcher fan out to action branches. Structure charts show hierarchy and couples, not execution order.
- **Describe the design to IEEE 1016.** An SDD records scope, definitions, purpose, content, and organisation across multiple design views.
- **Move to objects.** Object-oriented design identifies classes, attributes, operations, and relationships, then expresses them in UML.

**Keywords**

- **Conceptual design** — Architecture and high-level structure — <span dir="rtl">التصميم المفهومي</span>
- **Technical design** — Interfaces, data structures, algorithms — <span dir="rtl">التصميم التقني</span>
- **Abstraction** — Procedural, data, control — <span dir="rtl">التجريد</span>
- **Stepwise refinement** — Wirth: decompose top-down in steps — <span dir="rtl">التنقيح التدريجي</span>
- **Information hiding** — Parnas: hide decisions likely to change — <span dir="rtl">إخفاء المعلومات</span>
- **Modularity** — Decomposition into independently changeable units — <span dir="rtl">التماسك البنيوي</span>
- **Coupling** — Degree of interdependence between modules — <span dir="rtl">الارتباط</span>
- **Cohesion** — Degree of internal functional relatedness — <span dir="rtl">التلاحم</span>
- **Fan-in / fan-out** — Callers in; callees out — <span dir="rtl">الدخول / الخروج</span>
- **Depth / width** — Hierarchy levels; span per level — <span dir="rtl">العمق / العرض</span>
- **Structure chart** — Module hierarchy with data and control couples — <span dir="rtl">مخطط الهيكل</span>
- **Transform analysis** — Input, transform centre, output — <span dir="rtl">التحليل التحويلي</span>
- **Transaction analysis** — Dispatcher with action branches — <span dir="rtl">التحليل المعاملي</span>
- **SDD** — IEEE 1016 design description — <span dir="rtl">وثيقة تصميم البرمجيات</span>
- **OOD** — Classes, objects, inheritance, polymorphism — <span dir="rtl">التصميم الكائني</span>
- **Design review** — Formal defect detection before coding — <span dir="rtl">مراجعة التصميم</span>

**Facts, numbers, formulas**

- **Six coupling levels, best to worst:** data → stamp → control → external → common → content.
- *Data*: only needed scalar values pass.
- *Stamp*: a whole record or structure passes but only part is used.
- *Control*: a flag or switch directs the callee's logic.
- *External*: modules share an externally imposed protocol or device format.
- *Common*: modules share global data.
- *Content*: one module reaches into another's internals.
- **Seven cohesion levels, worst to best:** coincidental → logical → temporal → procedural → communicational → sequential → functional.
- *Coincidental*: no relationship. *Logical*: related by category, selected externally. *Temporal*: related by time of execution. *Procedural*: related by order of execution. *Communicational*: operate on the same input or output data. *Sequential*: output of one is input of the next. *Functional*: all elements contribute to one single task.
- **Meyer's five modularity criteria:** direct interface, few interfaces, small interfaces, explicit interfaces, information hiding.
- **Structure chart symbols:** module (rectangle), call (arrow), data couple (arrow with open circle), control couple (arrow with filled circle), conditional call (diamond).
- **Fan-in** is the number of modules that call a module (high is good: reuse and shared service). **Fan-out** is the number of modules a module calls (low is good, except for a legitimate dispatcher). **Depth** is the number of hierarchy levels; **width** is the number of modules at a level.
- **IEEE 1016 design views:** context, composition, logical, dependency, information, patterns, interface, structure, interaction, state dynamics, algorithm, resource.
- **OOD steps:** identify classes and objects → identify attributes and operations → establish relationships (association, aggregation, composition, generalisation) → define interfaces → iterate.

**Design decisions at a glance**

- **Strategy.** Top-down decomposes from the whole and gives early architectural control, but risks late component rework. Bottom-up composes from tested reusable parts and gives early working code, but risks a structure that does not fit the requirement. Hybrid fixes the architecture top-down, then builds and integrates bottom-up.
- **UML relationships.** Association (structural link), aggregation (weak whole-part, part survives), composition (strong whole-part, part dies with the whole), generalisation (is-a inheritance), realisation (implements an interface).
- **Function-oriented sequence.** DFD → identify transform or transaction centre → derive structure chart → assign couples → optimise fan-in and fan-out → review.
- **Design review checklist.** Requirements traceability, coupling and cohesion, interface completeness, error and exception handling, data structure adequacy, and testability.

**Traps**

- **Coupling and cohesion are inversely related but not mechanically.** You cannot "maximise both"; the design answer is a justified trade-off, and you must say what is sacrificed.
- **Stamp versus data coupling.** Passing a whole record when one field is needed is stamp coupling even though it "works".
- **Control versus stamp.** A boolean flag that steers the callee's internal logic is control coupling, which is worse.
- **Content coupling is not "very high common coupling".** It means direct access to another module's internal code or data.
- **A structure chart is not a flowchart.** It shows static module hierarchy and inter-module couples; it does not show sequence, branches, or loops.
- **Depth is not complexity by itself.** A deep, narrow, single-purpose hierarchy can be better than a shallow, wide one with high fan-out.
- **IEEE 1016 is a description standard, not a design method.** It prescribes how to *document* a design, not how to produce one.
- **Design review is not testing.** It is static defect detection on the design artifact, before code exists.

**Three lines**
Design quality is not taste: it is coupling, cohesion, hiding, and hierarchy, each with a name and a direction.
Derive structure charts from DFDs by transform or transaction analysis, and label data couples separately from control couples.
Every design claim needs a trade-off sentence: what improves, what pays for it.

**Definitions to quote**

| Term | Definition | بالعربي |
|:--|:--|:--|
| Coupling | Degree of interdependence between two modules | الاعتماد المتبادل |
| Cohesion | Degree to which a module serves one focused purpose | وحدة الهدف |
| Information hiding | Hiding the design decisions most likely to change | إخفاء القرارات |
| Fan-in / fan-out | Callers into a module versus callees out of it | الداخل والخارج |
| Structure chart | Module hierarchy with data and control couples | هيكل الوحدات |
| Transform analysis | Deriving a structure chart from input, centre and output | مركز التحويل |

**One-mark distinctions**
- **Architecture versus design.** Architecture sets the structural decisions that are expensive to reverse; design fills in the local decisions inside that structure.
- **Coupling versus cohesion.** One is between modules, the other inside a module, and the goal is low then high. Stating only one direction loses half the mark.
- **Structural versus behavioural models.** Structure charts and class diagrams show composition; sequence and state diagrams show behaviour over time.
- **Modularity versus decomposition.** Decomposition is the act of splitting; modularity is the resulting property of independent, coherent, hideable units.

**Question patterns**

- **"Rank the coupling levels"** → data, stamp, control, external, common, content. Six in the course book, best to worst, and say why each step is worse.
- **"Rank the cohesion levels"** → coincidental, logical, temporal, procedural, communicational, sequential, functional, worst to best.
- **"Redesign this module"** → lower coupling by passing only needed data and hiding decisions behind an interface; raise cohesion by removing unrelated responsibilities; then name the trade-off.
- **"Derive a structure chart"** → find the transform centre or the transaction centre, factor input and output branches, label data couples separately from control couples.
- **"Top-down or bottom-up?"** → top-down gives architectural control and late component validation; bottom-up gives early tested parts and a risk of a structure that does not fit the requirement. Hybrid fixes the architecture first.
- **"What goes in the SDD?"** → scope, definitions, purpose, content and organisation, across the IEEE 1016 views: context, composition, logical, dependency, information, interface, structure, interaction, state, algorithm, resource.
- **"Diagnose fan-in and fan-out"** → high fan-in is reuse and should be preserved; high fan-out is dependency and should be reduced, except for a legitimate dispatcher.
- **"Design review or testing?"** → review is static and catches design defects before code exists; testing is dynamic and cannot see what was never built.
- **"OOD in one pass"** → classes, attributes, operations, then association, aggregation, composition, generalisation, then interfaces, then iterate.

## الاسترجاع
AR:التصميم جسر بين مواصفة المتطلبات والبناء، وجودته ليست ذوقاً بل خصائص قابلة للتسمية والقياس: ارتباط منخفض وتلاحم عالٍ وإخفاء للمعلومات وتوزيع متوازن للهيكل. يبدأ التصميم المفهومي بالمعمارية والسؤال عن الكل، ثم يثبّت التصميم التقني الواجهات والبيانات والخوارزميات. والتجريد ثلاثة أنواع إجرائي وبياني وتحكمي، ويُدار التعقيد بالتنقيح التدريجي الذي يقسّم المشكلة خطوة بخطوة وبإخفاء المعلومات الذي يخفي القرارات الأكثر عرضة للتغيير. والوحدات تُحكم بستة مستويات ارتباط من الأفضل إلى الأسوأ وسبعة مستويات تلاحم من الأسوأ إلى الأفضل، وهما يتعاكسان في الاتجاه لا في القيمة. وتُشتق مخططات الهيكل من مخططات تدفق البيانات بتحليل تحويلي يبحث عن مركز التحويل أو تحليل معاملي يبحث عن موزّع، مع تمييز الاقتران البياني من التحكمي. وأخيراً يوثّق التصميم وفق IEEE 1016 بوجهات نظر متعددة ثم ينتقل إلى الكائنات بعلاقاتها، وكل قرار تصميمي يحتاج جملة مقايضة تقول ما تحسّن وما دُفع ثمناً.
