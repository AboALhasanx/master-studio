# Chapter 9 — Software Maintenance

**Skeleton**

- **Define and justify.** Maintenance is modification after delivery: correcting faults, adapting to environment change, improving performance or maintainability, or preventing future failure. It takes most of the lifecycle cost.
- **Classify the four types.** Corrective (reported defects), adaptive (new environment or platform), perfective (new requirements, enhancement, optimisation), preventive (future maintainability).
- **State the effort distribution.** Perfective about 50 percent, adaptive about 25 percent, corrective about 21 percent, preventive about 4 percent. Enhancement, not repair, dominates.
- **Walk the process.** Input objectives → program understanding → generate a maintenance proposal → account for ripple effects → modify → test the modified program → revalidate → deliver.
- **Compare the models.** Quick fix, iterative enhancement, reuse-oriented, Boehm, and Taute.
- **Estimate cost.** Belady–Lehman for effort from complexity and familiarity; Boehm's annual change traffic for yearly effort and whole-life cost.
- **Control change.** Configuration management with identification, change control, auditing, and status accounting, governed by a configuration control authority.
- **Recover the design.** Reverse engineering for understanding, reengineering for improvement, forward engineering for replacement, and restructuring for control-flow or efficiency cleanup.

**Keywords**

- **Software maintenance** — Post-delivery modification — <span dir="rtl">صيانة البرمجيات</span>
- **Corrective maintenance** — Fixing reported defects — <span dir="rtl">صيانة تصحيحية</span>
- **Adaptive maintenance** — Responding to environment change — <span dir="rtl">صيانة تكيفية</span>
- **Perfective maintenance** — New requirements and optimisation — <span dir="rtl">صيانة تحسينية</span>
- **Preventive maintenance** — Raising future maintainability — <span dir="rtl">صيانة وقائية</span>
- **Maintainability** — Ease of understanding and safe change — <span dir="rtl">قابلية الصيانة</span>
- **Ripple effect** — Change amplification across modules — <span dir="rtl">أثر الموجة</span>
- **Quick-fix model** — Patch now, decay later — <span dir="rtl">نموذج الإصلاح السريع</span>
- **Iterative enhancement** — Analyse, redesign, implement — <span dir="rtl">التحسين التكراري</span>
- **Reuse-oriented model** — Reuse existing components and OO design — <span dir="rtl">النموذج القائم على إعادة الاستخدام</span>
- **Taute model** — Eight sequential maintenance phases — <span dir="rtl">نموذج تاوت</span>
- **CCA** — Configuration control authority — <span dir="rtl">جهة التحكم بالتكوين</span>
- **Regression testing** — Retesting to catch reintroduced faults — <span dir="rtl">اختبار الانحدار</span>
- **Reverse engineering** — Recovering design from code — <span dir="rtl">الهندسة العكسية</span>
- **Reengineering** — Restructuring plus reverse engineering — <span dir="rtl">إعادة الهندسة</span>

**Facts, numbers, formulas**

- **Effort split:** perfective 50 percent, adaptive 25 percent, corrective 21 percent, preventive 4 percent. The order is the exam point: enhancement exceeds repair.
- **Defect cost escalation:** analysis : design : implementation ≈ 1 : 10 : 100, so a requirements defect that survives to coding costs a hundred times more than one caught in analysis.
- **Belady–Lehman maintenance effort:**
$$M=P+K\,e^{\,c-d}$$
where P is development effort, c is complexity, d is the degree of familiarity of the maintenance team, and K is an empirical constant. Raising familiarity (d) reduces effort exponentially; raising complexity (c) raises it exponentially.

- **Boehm's annual maintenance:**
ACT = (annual change traffic)/(initial size)
AME = ACT × SDE
where SDE is software development effort, so the multi-year lifecycle total is $SDE+\sum AME$ over the maintenance years.

- **Maintenance process and Taute's model.** Objectives in → understanding → proposal → ripple-effect accounting → modification → testing gate → revalidation → delivery. Taute's eight phases: change request, classification and prioritisation, analysis, design, implementation, testing, documentation update, release and review.
- **Rothermel–Harrold regression-test selection criteria:** inclusiveness (never omit a test that would expose a fault), precision (avoid tests that cannot expose one), efficiency (cost of selection), generality (works for any change and program).
- **SCM and reverse engineering.** SCM's four activities are identification, change control, auditing, and status accounting; revisions track change over time while variations track parallel versions. Reverse engineering recovers design at implementation, design, or requirements level: redocumentation is horizontal, design recovery is vertical.

**Model at a glance — logic and its price**

| Model | Logic | Price you pay |
|:--|:--|:--|
| Quick fix | Patch the symptom, redeploy fast | Architectural decay, repeated patches |
| Iterative enhancement | Analyse → redesign → implement in cycles | Repeated analysis cost |
| Reuse-oriented | Build from existing components and OO units | Component mismatch and glue cost |
| Boehm | Decision-driven flow with explicit alternatives and risk | Management overhead |
| Taute | Eight sequential phases with formal change control | Slower for trivial changes |

**Traps**

- **"Maintenance means fixing bugs."** Corrective work is only about a fifth of effort; perfective and adaptive work dominate.
- **Maintenance versus new development.** Maintenance starts from an existing artifact, is constrained by its architecture and undocumented decisions, and carries regression risk; new development starts from a clean specification.
- **Quick fix is not "the cheap option".** It defers cost into architectural decay and raises the next change's cost. State the trade-off, not just the patch.
- **Reverse engineering is not reengineering.** Reverse engineering *recovers understanding* and changes no code; reengineering = reverse engineering + restructuring/forward engineering.
- **High coupling is a maintenance multiplier.** It widens the ripple effect and reduces stability; this is the design-to-maintenance link examiners look for.
- **Belady–Lehman direction.** d is *familiarity*, so higher d lowers M; students routinely invert it.
- **AME is annual, not total.** Multiply by the maintenance horizon before comparing with development cost.
- **Configuration auditing is not testing.** Audit verifies that the configuration items and their status match what was approved; testing verifies behaviour.

**Three lines**
Maintenance is evolution: most of the effort goes into enhancement, not repair.
Cost is driven by understanding, familiarity, and coupling, which is why design quality is a maintenance metric.
Never leave a maintenance answer without the ripple effect, regression testing, and configuration control.

**Definitions to quote**

| Term | Definition | بالعربي |
|:--|:--|:--|
| Maintenance | Post-delivery modification to correct, adapt, improve or prevent | تعديل بعد التسليم |
| Perfective maintenance | Enhancement and optimisation for new or changed needs | تحسين وتطوير |
| Ripple effect | Change amplification across dependent modules | انتشار التغيير |
| Reverse engineering | Recovering design understanding without changing the artifact | فهم بلا تعديل |
| Reengineering | Restructuring or rebuilding using recovered understanding | إعادة بناء |
| SCM | Identification, change control, auditing and status accounting | ضبط التغيير |

**Question patterns**

- **"Classify this maintenance request"** → corrective if a reported defect, adaptive if the environment changed, perfective if the user wants more, preventive if the goal is future maintainability.
- **"Estimate maintenance effort"** → Belady–Lehman $M=P+Ke^{c-d}$ from complexity and familiarity, or Boehm $AME=ACT\times SDE$ from annual change traffic. Say which input you were given.
- **"Choose a maintenance model"** → quick fix for an emergency with acknowledged decay, iterative enhancement for structured growth, reuse-oriented when components exist, Taute when formal control is required.
- **"Why does maintenance cost rise?"** → poor program understanding, high coupling and ripple effect, missing documentation, and staff unfamiliarity. Each maps to a design decision.
- **"Reverse engineering or reengineering?"** → understanding versus change. Reverse engineering alters nothing; reengineering restructures using what was recovered.
- **"Legacy decision"** → compare reengineering cost against replacement cost and business risk; Sneed's rule is the reference point, not a slogan.
- **"Design the SCM workflow"** → identification, change control through the CCA, auditing, status accounting; distinguish revisions over time from variations across environments.
- **"Select regression tests"** → choose coverage-based, minimization-based or safe techniques, and state the hazard: minimization can drop the test that would have caught the fault.
- **"What makes maintenance hard?"** → the change is constrained by decisions nobody documented, and every modification must preserve behaviour that is not written down.

## الاسترجاع
AR:الصيانة ليست إصلاحاً متأخراً بل استمرار حياة نظام قائم، وهي تستهلك الحصة الكبرى من كلفة دورة الحياة. وتُقسم أربعة أنواع: تصحيحية لإصلاح عيوب مبلّغة، وتكيفية للاستجابة لتغيّر البيئة، وتحسينية لمتطلبات جديدة وتحسين الأداء، ووقائية لرفع قابلية الصيانة مستقبلاً. والتوزيع العملي يكشف المفارقة: التحسينية نحو النصف والتكيفية نحو الربع والتصحيحية نحو الخُمس والوقائية نسبة صغيرة، أي أن التطوير لا الإصلاح هو محرك الكلفة. وتمرّ العملية من الأهداف إلى فهم البرنامج ثم اقتراح الصيانة ثم حساب أثر الموجة ثم التعديل ثم اختبار البرنامج المعدّل. والنماذج تُقارن بمنطقها وثمنها: الإصلاح السريع يرقّع الرمز فيُسرّع التدهور المعماري، والتحسين التكراري يعيد التحليل والتصميم والتنفيذ، ونموذج إعادة الاستخدام يبني على مكونات موجودة، ونموذجا Boehm وTaute يضيفان القرار الصريح والمراحل الثماني. وتُقدَّر الكلفة بنموذج Belady–Lehman الذي يربط الجهد بالتعقيد والألفة، وبمعدل التغيير السنوي عند Boehm. وأخيراً تحكم التغيير إدارة التكوين بأربعة أنشطة وجهة تحكم، وتُفهم الأنظمة القديمة بالهندسة العكسية ثم تُحسَّن بإعادة الهندسة مع اختبار انحدار يحمي ما لم يُقصد تغييره.
