# Chapter 2 — Software Life-Cycle Models

**Skeleton**

- **Define the frame.** The SDLC is the set of phases from feasibility and requirements through design, coding, testing, and maintenance. A *process* is the activity framework; a *methodology* is a prescribed way of executing it; a *model* is the lifecycle arrangement of phases.
- **Build & Fix.** Code first, fix later. Viable only for tiny, disposable programs; it produces no design record, so cost explodes as size grows.
- **Waterfall.** Sequential, plan-driven, phase-gated, documentation-heavy. Correct when requirements are frozen and the technology is understood; wrong when feedback arrives only after delivery.
- **Incremental versus iterative.** Incremental delivers *additive* usable increments; iterative *reworks and refines* the same product through repeated passes. They can be combined but are not synonyms.
- **RAD.** Component-based, time-boxed, small-team, user-intensive. It requires modular deliverable systems, reusable high-quality components, and short decision cycles; without those conditions it degrades into hacking.
- **Prototyping and evolutionary.** Throwaway prototyping clarifies requirements; evolutionary prototyping becomes the product. The classic risk is that a throwaway prototype is shipped.
- **Spiral.** Risk-driven: each loop sets objectives and constraints, identifies and resolves risk, develops and verifies, then plans the next loop. It is the model of choice for large, high-risk work, and it costs real risk-analysis expertise.
- **Unified Process.** Four phases (Inception, Elaboration, Construction, Transition) crossed with workflows; iterative, incremental, architecture-centric, use-case driven, and risk-driven. A phase is not a workflow.
- **Agile / XP / Scrum.** Agile is the value system; XP supplies engineering practices; Scrum supplies the management container.

**Keywords**

- **SDLC** — Phases from feasibility to maintenance — <span dir="rtl">دورة حياة تطوير النظام</span>
- **Build & Fix** — No design phase; rapid but unmaintainable — <span dir="rtl">ابنِ ثم أصلح</span>
- **Waterfall** — Sequential, plan-driven, phase gates — <span dir="rtl">الشلال</span>
- **Iterative enhancement** — Repeated full passes over a growing product — <span dir="rtl">التحسين التكراري</span>
- **Incremental delivery** — Product grows by usable increments — <span dir="rtl">التسليم التدريجي</span>
- **RAD** — Time-boxed, component-based, small team — <span dir="rtl">التطوير السريع للتطبيقات</span>
- **Prototyping** — Throwaway versus evolutionary — <span dir="rtl">النمذجة الأولية</span>
- **Spiral** — Risk-driven loops with explicit risk resolution — <span dir="rtl">الحلزون</span>
- **Unified Process** — Four phases across repeated iterations — <span dir="rtl">العملية الموحدة</span>
- **Agile** — Working software, collaboration, response to change — <span dir="rtl">الرشاقة</span>
- **XP** — TDD, pair programming, refactoring, small releases — <span dir="rtl">البرمجة المتطرفة</span>
- **Scrum** — Backlog, sprint, three roles, four ceremonies — <span dir="rtl">سكرم</span>
- **Risk-driven** — Expensive uncertainty resolved early — <span dir="rtl">مدفوع بالمخاطر</span>

**Facts, numbers, formulas**

- **Waterfall phase order:** feasibility/requirements → analysis → design → coding → testing → maintenance. Each gate is a review; rework cost multiplies downstream.
- **Spiral quadrants (Boehm):** (1) determine objectives, alternatives, constraints; (2) identify and resolve risks; (3) develop and verify the next product level; (4) plan the next iteration. The radius is cumulative cost; the angular sweep is progress.
- **UP phases and their exit criteria:** Inception → lifecycle objectives agreed and business case; Elaboration → executable architecture baseline and resolved major risks; Construction → product complete and beta-tested; Transition → usable release in the user environment.
- **UP workflows:** Requirements, Analysis, Design, Implementation, Test, plus Configuration and Change Management, Project Management, and Environment.
- **Scrum roles:** Product Owner (value and backlog order), Scrum Master (process servant-leader), Development Team (self-organising, cross-functional). **Ceremonies:** Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective. **Artifacts:** Product Backlog, Sprint Backlog, Increment.
- **XP core practices:** planning game, small releases, metaphor, simple design, test-first development, refactoring, pair programming, collective code ownership, continuous integration, sustainable pace, on-site customer, coding standards.
- **Selection matrix axes:** requirements clarity and volatility, technical risk, system size, team skill and distribution, customer availability, contractual fixedness, time pressure.

**Model at a glance — pick one, then defend the sacrifice**

| Model | Choose it when | You pay with |
|:--|:--|:--|
| Build & Fix | Program is tiny and disposable | Any design record; unmaintainable growth |
| Waterfall | Requirements frozen, contract fixed, technology known | Late feedback; expensive change |
| Incremental | Core is clear and can ship in slices | Integration overhead per increment |
| Iterative enhancement | Requirements emerge, product must grow | Repeated rework of the whole |
| RAD | Modular system, reusable components, small co-located team | Fails hard without those preconditions |
| Throwaway prototyping | Requirements cannot be verbalised | Prototype may be shipped by mistake |
| Evolutionary prototyping | Requirements unclear, product must still ship | Architecture grows by accident |
| Spiral | Large, high-risk, expensive failure | Risk-analysis expertise at every loop |
| Unified Process | Architecture and risk must be handled explicitly | Ceremony and iteration discipline |
| Agile / XP / Scrum | Change is normal, customer is available | Documentation and long-range predictability |

**Traps**

- **"Waterfall is always wrong."** False. It is the correct choice for stable, well-understood, contract-bound requirements. Attack it only where change is expected.
- **Incremental = Iterative?** No. Incremental adds features; iterative reworks quality and design. A model can be both, but the words are not interchangeable.
- **Spiral = "a circle diagram".** The defining property is *explicit risk analysis and resolution before proceeding*, not the shape.
- **Phase versus workflow in the UP.** Inception is not "the requirements phase". Every phase executes every workflow to a different depth.
- **RAD without reusable components.** RAD's preconditions are modularity, reusable components, small teams, and rapid decision-making; a monolithic system cannot be RAD.
- **Scrum versus XP.** Scrum is a management framework with no engineering practices; XP is an engineering discipline inside a management envelope.

**Three lines**
Models differ in where they place uncertainty: Waterfall defers it, Spiral confronts it, Agile absorbs it continuously.
Choose by requirements stability, risk, size, and customer access, and always state what the chosen model sacrifices.
Never merge Incremental with Iterative, or a UP phase with a workflow.

**Definitions to quote**

| Term | Definition | بالعربي |
|:--|:--|:--|
| SDLC | The ordered set of phases from feasibility to maintenance | دورة الحياة |
| Waterfall | Sequential, plan-driven phases with review gates between them | تتابع مع بوابات |
| Incremental | Delivery of usable slices that add functionality | شرائح وظيفية |
| Iterative | Repeated passes that refine the same product | إعادة صياغة |
| Spiral | Risk-driven loop that resolves risk before proceeding | المخاطرة أولاً |
| RAD | Time-boxed, component-based development by a small team | مكونات وفريق صغير |

**One-mark distinctions**
- **Process, methodology, model.** The activity framework, the prescribed way of executing it, and the lifecycle arrangement of phases. One word, three different objects.
- **Phase versus iteration.** A phase is a stage of completeness; an iteration is a pass through all stages. Inception can contain several iterations.
- **Plan-driven versus change-driven.** Plan-driven fixes scope and estimates change; change-driven fixes time and lets scope flex.
- **Predictive versus adaptive.** Predictive models buy certainty early and pay for it in change cost; adaptive models absorb change and pay for it in predictability.

**Question patterns**

- **"Compare two models"** → compare phase structure, feedback timing, risk handling, cost of change, documentation weight, and the project profile each one fits. End with the sacrifice.
- **"Which model for a fixed-price contract?"** → Waterfall or a stage-gated variant, because scope is frozen and evidence of completion is document-based; add the caveat that change becomes expensive.
- **"Which model for unclear requirements and high risk?"** → Spiral when risk is the dominant cost, evolutionary prototyping when the product must still ship, Agile when the customer is continuously available.
- **"Why is Spiral risk-driven?"** → every loop resolves the highest risk before development continues, so money is spent retiring uncertainty rather than producing code that may be discarded.
- **"Incremental or iterative?"** → incremental adds usable slices; iterative refines the same slice. A project can be both, but the words are not interchangeable.
- **"Can we use RAD?"** → only with a modular system, reusable components, a small co-located team and fast user decisions. Name the missing precondition and RAD is disqualified.
- **"Phase or workflow in the UP?"** → phases are time; workflows are activity. Every phase runs every workflow to a different depth, so Inception is not the requirements phase.
- **"Scrum or XP?"** → Scrum is the management container, XP the engineering discipline. Choosing Scrum without XP leaves you with meetings and no technical practice.
- **"What is the danger of prototyping?"** → the throwaway prototype is shipped, so performance, error handling and architecture are never engineered.

## الاسترجاع
AR:كل نموذج لحياة تطوير البرمجيات رهان على توقيت شراء اليقين. نموذج الشلال يشتري اليقين مبكراً عبر توثيق صارم ومراحل متتابعة، وينجح فقط حين تكون المتطلبات مجمّدة والتقنية مفهومة، أما التغيير فيه فكلفته تتضاعف لأنه يصل بعد أن تكون المراحل اللاحقة قد استهلكت مخرجات المراحل السابقة. والنماذج التكرارية والتدريجية تعيد توزيع هذا اليقين: التدريجي يضيف وظائف قابلة للاستخدام على شكل شرائح، والتكراري يعيد صياغة المنتج نفسه مراراً، وهما ليسا مترادفين. والنمذجة الأولية تستخرج المتطلبات التي لا تُقال، وخطرها أن تُسلَّم كنموذج قابل للرمي. وRAD يشترط نظاماً معيارياً ومكونات قابلة لإعادة الاستخدام وفريقاً صغيراً ووصولاً سريعاً للمستخدم. والحلزون هو النموذج الوحيد الذي يجعل تحليل المخاطر وحلها صريحاً قبل التقدّم، والعملية الموحدة تمزج الأطوار الأربعة مع سير عمل متكرر داخل كل طور فلا تخلط الطور بسير العمل. وأخيراً الرشاقة توجه قيمي وXP انضباط هندسي وScrum إطار إداري، والخيار يُحسم باستقرار المتطلبات وحجم المخاطرة وحجم النظام وتوفر العميل.
