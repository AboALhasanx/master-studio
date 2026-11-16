# Chapter 1 — Introduction: Software, Crisis, and the Engineering Response

**Skeleton**

- **Define the object.** Software is not only code; it is programs plus procedures, rules, associated documentation, and data. It is engineered, not manufactured.
- **Separate the two failure curves.** Hardware follows the bathtub curve: infant mortality, a stable useful life, then wear-out. Software has no wear-out mechanism; its curve dips after debugging and then **rises again every time it is changed**, because each modification injects new defects.
- **State the crisis with evidence.** Schedule and cost overruns, low quality, unmaintainable legacy systems, and demand for engineers that exceeds supply.
- **Name the documented failures.** Y2K two-digit year fields; the Patriot missile timing defect (1991); a 1996 database project; Ariane-5 (1996); a financial software collapse; Windows XP delays; the Space Shuttle fuel-dump case.
- **Kill the myths.** Nine myths in three families: management, customer, and practitioner.
- **Answer the identity question.** Software engineering is a discipline with craft elements, but its claim to "engineering" rests on process, measurement, review, and repeatability, not on individual brilliance.
- **Measure what you manage.** Productivity is output per unit of effort; a measure is an attribute value, a metric is a measure with a defined method and scale, and an indicator is a metric interpreted against a goal.

**Keywords**

- **Software** — Programs + procedures + documentation + data, not just code — <span dir="rtl">البرمجيات</span>
- **Software engineering** — Multi-person, multi-version, engineered construction — <span dir="rtl">هندسة البرمجيات</span>
- **Software crisis** — Chronic overrun, poor quality, unmet demand — <span dir="rtl">أزمة البرمجيات</span>
- **Wear-out curve** — Software does not wear out; it deteriorates through change — <span dir="rtl">منحنى الاستهلاك</span>
- **Bathtub curve** — Hardware: infant mortality, useful life, wear-out — <span dir="rtl">منحنى الحوض</span>
- **Software myth** — A plausible belief that misdirects management or practice — <span dir="rtl">خرافة برمجية</span>
- **Software process** — Framework of activities, actions, and tasks — <span dir="rtl">عملية البرمجيات</span>
- **Umbrella activity** — Project management, quality assurance, configuration management, review — <span dir="rtl">نشاط مظلي</span>
- **Productivity** — Output per unit effort, e.g. LOC per person-month — <span dir="rtl">الإنتاجية</span>
- **Measure / metric / indicator** — Attribute value; defined measurement method; metric judged against a goal — <span dir="rtl">قياس / مقياس / مؤشر</span>
- **Maintainability** — Cost of understanding and changing the product — <span dir="rtl">قابلية الصيانة</span>
- **Legacy system** — Working system whose change cost is dominated by accumulated decay — <span dir="rtl">نظام قديم</span>

**Facts, numbers, formulas**

- **Productivity** = dfrac{output}{effort} in person-months. It is a ratio, never a raw LOC count.
- **Effort** is measured in person-months; **duration** is calendar time. They are not the same quantity, and compressing duration raises effort non-linearly.
- **Patriot defect:** 24-bit fixed-point truncation produced a clock drift of about **0.34 s after roughly 100 hours** of operation; the tracking error caused a missed intercept.
- **Ariane-5 defect:** reuse of Ariane-4 software outside its validated operating envelope; a 64-bit floating-point horizontal-bias value was converted to a **16-bit signed integer** and overflowed.
- **Y2K:** two-digit year storage made century boundaries ambiguous; the fix cost was enormous but the failure was a *design assumption*, not a coding typo.
- **Nine software myths** cluster as management myths (we already have standards, tools will save us, adding people rescues a late project), customer myths (objectives are obvious, requirements are easy to change, software is flexible), and practitioner myths (the job ends when the program runs, quality appears only at run time, the only deliverable is code).
- **No Silver Bullet** (Brooks): essential complexity (the conceptual construct) cannot be eliminated by technology; accidental complexity can be reduced.
- **Craft versus science:** the defensible answer is a *profession with a scientific core and craft residue*: design judgement is craft, validation and measurement are science.

**The failure cases, one line each**

| Case | Mechanism | What it proves |
|:--|:--|:--|
| Y2K | Two-digit year storage | A design assumption becomes a global defect |
| Patriot (1991) | 24-bit truncation, drift about 0.34 s per 100 h | Number representation is a safety property |
| Ariane-5 (1996) | 64-bit value converted to 16-bit signed integer | Reuse outside the validated envelope is a new system |
| 1996 database project | Scale and requirement misjudgement | Estimation and planning failures precede code |
| Financial software | Accumulated rounding error | Domain arithmetic must be specified, not assumed |
| Windows XP | Feature and schedule pressure | Scope grows when change control is weak |
| Shuttle fuel dump | Interface and unit mismatch | Interface contracts need explicit specification |
| No Silver Bullet | Essential versus accidental complexity | Tools reduce accident, never essence |

**Traps**

- **"Software wears out."** It does not. Hardware wears out physically; software *deteriorates* because maintenance changes accumulate. Say "deterioration due to change", not "wear-out".
- **Confusing the two famous failures.** Patriot is a *timing/truncation* defect; Ariane-5 is a *data-representation/overflow* defect caused by reuse outside the validated envelope. Do not swap them.
- **Equating productivity with code volume.** More LOC for the same function is a *worse* result; function points exist precisely to avoid this.
- **Treating the crisis as a hardware problem.** The causes listed are management, estimation, requirements, and process failures.
- **Answering "art or science" with a slogan.** Give a position, then defend it with process, measurement, and review evidence.

**Three lines**
Software is engineered, not manufactured; its failure curve rises with change rather than with time.
The crisis is process and management, proved by a documented list of failures, not by rhetoric.
Engineering credibility comes from measurement, review, and repeatability, while craft remains in design judgement.

**Definitions to quote**

| Term | Definition | بالعربي |
|:--|:--|:--|
| Software | Programs, procedures, rules, associated documentation and data | البرمجيات كمنتج |
| Software engineering | Multi-person, multi-version, engineered construction of software | بناء هندسي |
| Software crisis | Chronic schedule and cost overruns with poor quality and unmet demand | أزمة إدارة وعملية |
| Software wear-out | Deterioration caused by repeated modification, not physical decay | تدهور بالتغيير |
| Software process | Framework of activities, actions and tasks used to build software | إطار العمل |
| Productivity | Output produced per unit of effort, e.g. LOC per person-month | الناتج على الجهد |

**One-mark distinctions**
- **Program versus software.** A program is executable code; software is the program plus procedures, documentation and data, plus the configuration that makes it run.
- **Crisis versus failure.** A failure is one event; the crisis is the persistent pattern of overrun, poor quality and unmet demand across the industry.
- **Measure versus metric versus indicator.** The value, the defined method, and the value judged against a goal. Examiners award the third word only when a goal is named.
- **Why maintenance dominates cost.** Because change, not construction, is the dominant activity over a system's life, and every change is constrained by earlier design decisions.

- **Evidence versus anecdote.** A failure case is exam evidence only when you name the system, the mechanism and the year; otherwise it is a story.
- **Why the engineering claim matters.** It converts individual skill into repeatable process, which is the only way to scale beyond the people who wrote the code.

**Question patterns**

- **"Define software"** → programs, procedures, rules, documentation, data. Never answer "code" alone; the definition is what separates software from a program.
- **"Why does software not wear out?"** → hardware degrades physically and follows the bathtub curve; software has no material to erode, so its failure rate rises only when modification injects new faults. Say deterioration, never wear-out.
- **"Analyse this failure"** → name the mechanism, then the root cause, then the lesson. Patriot is truncation drift; Ariane is a representation overflow caused by reuse outside the validated envelope; Y2K is a storage assumption.
- **"Are the myths harmless?"** → no. Each myth shifts cost downstream: management myths hide estimation error, customer myths freeze scope too early, practitioner myths replace review with confidence.
- **"Is software engineering art, craft or science?"** → take a position, then defend it with process, measurement and review. The defensible line is engineering discipline with a craft residue in design judgement.
- **"Compute productivity"** → output divided by effort, with units: LOC per person-month or FP per person-month. A bare number without units scores nothing.
- **"Compare hardware and software reliability"** → hardware hazard is time-driven and U-shaped; software hazard is change-driven and step-shaped.
- **"What proves the crisis is real?"** → documented overruns and failures plus a persistent demand-supply gap. Evidence, not adjectives.

## الاسترجاع
AR:البرمجيات ليست شيفرة تُكتب مرة ثم تُنسى، بل منتج منطقي يتغيّر باستمرار، ولهذا تقع كلفته الحقيقية في التصميم والصيانة لا في الكتابة. منحنى فشل العتاد يأخذ شكل الحوض لأنه يتلف مادياً، أما البرمجيات فلا تبلى جسدياً وإنما تتدهور كلما عُدّلت، لأن كل تغيير يحمل احتمال إدخال عيب جديد. من هنا جاءت أزمة البرمجيات: تجاوزات في الكلفة والجدول، وجودة متدنية، وأنظمة قديمة يصعب تغييرها، وهي أزمة إدارة وعملية لا أزمة أجهزة. وتشهد عليها حالات موثقة مثل مشكلة السنة ألفين وخطأ Patriot الناتج عن اقتطاع أربع وعشرين بت وتراكم انحراف زمني، وفيض Ariane خمسة الناتج عن تحويل تمثيلي خارج بيئة الاختبار المعتمدة. والخرافات التسع بثلاث عائلاتها هي التي تُعطّل القرار السليم، أما السؤال هل الهندسة علم أم حرفة فالجواب المتوازن أنها انضباط هندسي يقوم على القياس والمراجعة والتكرار مع بقاء حرفة في الحكم التصميمي، ومقياس الإنتاجية هو المخرجات على الجهد لا عدد الأسطر.
