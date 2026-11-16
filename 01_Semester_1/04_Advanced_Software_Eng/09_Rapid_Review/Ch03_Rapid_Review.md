# Chapter 3 — Requirements Engineering

**Skeleton**

- **Name the process.** Feasibility study → elicitation → analysis → specification (SRS) → validation, with requirements management (traceability and change control) running underneath the whole chain.
- **Classify requirements.** Functional requirements state *what* the system does; non-functional requirements constrain *how well* it does it (performance, security, usability, reliability, maintainability, portability). User requirements are business-facing statements; system requirements are the expanded, technical, contractual version. Interface specifications cover user, hardware, software, and communication interfaces.
- **Justify feasibility before spending.** A feasibility study tests technical, economic, operational, and legal/schedule viability, and ends in a documented go/no-go.
- **Elicit with the right instrument.** Interviews (structured or unstructured, open or closed), brainstorming, FAST workshops, QFD, and the use-case approach. Each has a different cost and a different failure mode.
- **Analyse with models.** DFD for data movement and transformation, data dictionary for the meaning of every data element, ERD for the data model, and prototyping when the requirement cannot be verbalised.
- **Specify to IEEE 830 quality.** An SRS is correct, unambiguous, complete, consistent, ranked for importance and stability, verifiable, modifiable, and traceable.
- **Validate, don't assume.** Requirements reviews and inspections, checklist-driven walkthroughs, prototype demonstration, and test-case generation against each requirement.

**Keywords**

- **Requirements engineering** — Elicit, analyse, specify, validate, manage — <span dir="rtl">هندسة المتطلبات</span>
- **Functional requirement** — A service or behaviour the system must provide — <span dir="rtl">متطلب وظيفي</span>
- **Non-functional requirement** — A quality or constraint on the service — <span dir="rtl">متطلب غير وظيفي</span>
- **User requirement** — Natural-language statement from the client side — <span dir="rtl">متطلب المستخدم</span>
- **System requirement** — Detailed, technical, contractual expansion — <span dir="rtl">متطلب النظام</span>
- **Interface specification** — User, hardware, software, communication boundaries — <span dir="rtl">مواصفة الواجهة</span>
- **Feasibility study** — Technical, economic, operational, legal viability — <span dir="rtl">دراسة الجدوى</span>
- **Elicitation** — Interviews, brainstorming, FAST, QFD, use cases — <span dir="rtl">استخلاص المتطلبات</span>
- **FAST** — Facilitated team workshop producing a ranked requirement list — <span dir="rtl">تقنية المواصفة السريعة</span>
- **QFD** — House of Quality matrix mapping customer needs to technical characteristics — <span dir="rtl">نشر وظيفة الجودة</span>
- **Use case** — Actor, goal, scenario, include/extend relations — <span dir="rtl">حالة استخدام</span>
- **DFD** — Processes, flows, stores, external entities, levelling — <span dir="rtl">مخطط تدفق البيانات</span>
- **Data dictionary** — Definitions, composition, aliases of every data element — <span dir="rtl">قاموس البيانات</span>
- **ERD** — Entities, attributes, relationships, cardinality, participation — <span dir="rtl">مخطط الكيانات والعلاقات</span>
- **SRS** — The agreed, verifiable statement of what must be built — <span dir="rtl">مواصفة متطلبات البرمجيات</span>
- **Requirements review** — Inspection against completeness, consistency, testability — <span dir="rtl">مراجعة المتطلبات</span>
- **Traceability** — Every requirement links forward to design and tests — <span dir="rtl">التتبعية</span>

**Facts, numbers, formulas**

- **Cost of a defect** rises roughly by an order of magnitude per phase survived: a requirements defect fixed in requirements costs a fraction of the same defect found in operation.
- **IEEE 830 SRS structure:** Introduction (purpose, scope, definitions, references, overview) → Overall description (product perspective, functions, user characteristics, constraints, assumptions) → Specific requirements (functional, external interface, performance, design constraints, quality attributes) → Appendices → Index.
- **DFD symbol set:** process (circle or rounded box), data flow (labelled arrow), data store (open-ended rectangle), external entity (rectangle). Levelling: context diagram (level 0) → level 1 → level 2, with input and output flows *balanced* between parent and child.
- **ERD cardinality:** 1:1, 1:N, M:N; participation is total or partial; a weak entity depends on an identifying owner; an associative entity resolves M:N; ternary relationships involve three entities at once.
- **QFD:** customer requirements (the "whats") are mapped against engineering characteristics (the "hows") in the House of Quality, with relationship strengths and competitive assessment.
- **Use-case relations:** *include* is mandatory shared behaviour; *extend* is optional, condition-triggered behaviour; *generalisation* is specialisation of an actor or use case.
- **Review types:** informal walkthrough (author-led, learning-oriented) versus formal inspection (moderator, checklist, recorded defects, follow-up).

**Technique at a glance — what each one actually produces**

| Technique | Produces | Best when |
|:--|:--|:--|
| Interview | Stakeholder statements and constraints | Access to one knowledgeable person at a time |
| Brainstorming | A wide, unfiltered idea pool | The problem space is unclear |
| FAST | A facilitated, ranked requirement list | Users and developers must agree quickly |
| QFD | House of Quality mapping customer needs to technical traits | Priorities and trade-offs must be explicit |
| Use case | Actors, goals, scenarios, include/extend relations | Behaviour is interaction-driven |
| DFD | Processes, flows, stores, external entities, levelled | Data movement must be modelled |
| Data dictionary | Definitions, composition, aliases of elements | Names and structures are inconsistent |
| ERD | Entities, attributes, relationships, cardinality | Static data structure matters |
| Prototype | A working fragment for feedback | Requirements resist verbal description |
| Review / inspection | A recorded list of defects | Specification must be validated |

**Traps**

- **"Non-functional" does not mean "optional" or "not about function".** It is a constraint on quality or implementation, and it must be quantified to be testable.
- **User versus system requirement.** The user statement is a need; the system requirement is the technical expansion that the contract enforces. Never present the business wish as the specification.
- **DFD is not a flowchart.** It shows data transformation and movement, not control flow, sequence, or timing.
- **ERD is not a DFD.** One models static data structure, the other models data movement; mixing them loses marks immediately.
- **"Complete" does not mean "everything".** Completeness means every required behaviour and constraint is specified, with nothing missing and nothing dangling.
- **QFD is not a requirements list.** It is a *translation matrix* from the voice of the customer to measurable engineering characteristics.
- **Validation is not verification.** Verification asks "did we build the product right?"; validation asks "did we build the right product?" Requirements reviews are validation.

**Three lines**
Requirements errors are the cheapest to fix and the most expensive to miss, so elicitation and validation carry the grade.
Model the *data* with ERD and dictionary, the *movement* with DFD, and the *behaviour* with use cases.
An SRS earns its name only when every statement is verifiable and traceable.

**Definitions to quote**

| Term | Definition | بالعربي |
|:--|:--|:--|
| Functional requirement | A service or behaviour the system must provide | وظيفة مطلوبة |
| Non-functional requirement | A quality or constraint on how a service is delivered | جودة أو قيد |
| FAST | Facilitated workshop producing a ranked requirement list | ورشة متطلبات |
| QFD | Matrix translating customer needs into technical characteristics | ترجمة صوت العميل |
| SRS | The agreed, verifiable statement of what must be built | عقد قابل للاختبار |
| Validation | Confirmation that the product meets the intended user need | الشيء الصحيح |

- **Prototype in requirements or in design?** In requirements it is a elicitation instrument and may be thrown away; in design it is an architectural experiment and usually evolves.
- **Traceability direction.** Forward links a requirement to design and tests; backward links a test failure to the requirement it violates. Both are needed for change impact.

**Question patterns**

- **"List the RE process"** → feasibility, elicitation, analysis, specification, validation, with management across all five. Order matters; validation is not optional.
- **"Functional or non-functional?"** → behaviour versus constraint on behaviour. A non-functional requirement is still testable, so attach a metric or it is a wish.
- **"User or system requirement?"** → the user statement is the business need; the system statement is its technical expansion and the contractual form.
- **"Which elicitation technique?"** → match the instrument to the obstacle: interviews for individual knowledge, brainstorming for breadth, FAST for consensus, QFD for priority conflict, use cases for interaction, prototypes for tacit requirements.
- **"Draw the DFD"** → four symbols, levelled, and balanced: the flows into a parent process equal the flows into its child diagram. Never show control flow or timing.
- **"Model the data"** → ERD for entities and relationships with cardinality and participation, data dictionary for element meaning and composition. One models structure, the other models vocabulary.
- **"Judge this SRS"** → score it against correct, unambiguous, complete, consistent, ranked, verifiable, modifiable, traceable, and quote the defective sentence.
- **"Why validate requirements?"** → because a defect fixed in requirements costs a fraction of the same defect found in operation, and reviews are the cheapest detector.
- **"Write a use case"** → actor, goal, preconditions, main success scenario, alternates, postconditions; then mark include for mandatory shared behaviour and extend for optional behaviour.

## الاسترجاع
AR:هندسة المتطلبات تحوّل حاجة إنسانية غامضة إلى عقد قابل للاختبار، وكل عيب ينجو إلى مرحلة لاحقة تزداد كلفته بمرتبة تقريباً. تبدأ العملية بدراسة الجدوى التي تفحص الجوانب التقنية والاقتصادية والتشغيلية والقانونية قبل إنفاق أي مبلغ، ثم الاستخلاص بأدوات مختلفة الكلفة وأنماط الفشل: المقابلات، والعصف الذهني، وورشة FAST التي تنتج قائمة متطلبات مرتبة، وQFD الذي يترجم صوت العميل إلى خصائص هندسية قابلة للقياس، وحالات الاستخدام التي تصف التفاعل بين الفاعل والهدف. بعدها يأتي التحليل بنماذج ثلاثة لا تختلط: مخطط تدفق البيانات يصف حركة البيانات وتحويلها وليس تدفق السيطرة، وقاموس البيانات يثبّت معنى كل عنصر وتركيبه، ومخطط الكيانات والعلاقات يصف البنية الساكنة للبيانات مع الاعتدادية والمشاركة. وأخيراً تُكتب مواصفة SRS بمعايير الجودة الثمانية، صحيحة وغير غامضة وكاملة ومتسقة ومرتبة وقابلة للتحقق والتعديل والتتبع، ثم تُراجع لا تُفترض، لأن التحقق من صحة البناء يختلف عن التحقق من بناء الشيء الصحيح.
