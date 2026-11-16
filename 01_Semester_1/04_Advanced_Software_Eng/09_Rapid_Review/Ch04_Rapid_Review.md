# Chapter 4 — Software Project Planning: Size, Cost, Schedule, Risk

**Skeleton**

- **Estimate size first.** Lines of code are concrete but language- and style-dependent; function points measure delivered functionality and are language-independent. Size is the input to every cost model.
- **Convert size to effort.** Static single-variable models use one driver (usually size); static multivariable models add cost drivers. COCOMO is the canonical family.
- **State COCOMO's three levels.** Basic uses size only; Intermediate multiplies by an Effort Adjustment Factor built from cost drivers; Detailed applies the same model per module and per phase.
- **Place COCOMO II correctly.** Application Composition (object points, prototyping-heavy), Early Design (function points or size, seven cost drivers), Post-Architecture (source statements, seventeen multipliers and five scale factors). The model is chosen by *life-cycle stage*, not by taste.
- **Use Putnam for the time-cost trade-off.** Effort, duration, and size are coupled: compressing the schedule demands disproportionately more effort, and the Rayleigh/Norden curve describes how staffing rises to a peak and decays.
- **Manage risk explicitly.** Identify, analyse (probability and loss), plan a response, and monitor. Risk exposure is probability times loss.
- **Close with a schedule and a control loop.** Milestones, staffing, and earned-value style monitoring convert the estimate into a plan.

**Keywords**

- **Size estimation** — LOC, KLOC, function count — <span dir="rtl">تقدير الحجم</span>
- **LOC** — Physical size; language-dependent — <span dir="rtl">أسطر الشيفرة</span>
- **Function point** — Functional size from five component types — <span dir="rtl">نقطة وظيفية</span>
- **UFP / VAF / FP** — FP = UFP × VAF — <span dir="rtl">نقاط غير معدلة / عامل التعديل / نقاط وظيفية</span>
- **COCOMO** — Constructive Cost Model, three levels — <span dir="rtl">نموذج الكلفة البنائي</span>
- **Organic / Semi-detached / Embedded** — Project mode by size and constraint tightness — <span dir="rtl">عضوي / نصف منفصل / مدمج</span>
- **EAF** — Product of cost-driver multipliers — <span dir="rtl">عامل تعديل الجهد</span>
- **Cost driver** — Product, computer, personnel, project attribute — <span dir="rtl">محرك الكلفة</span>
- **COCOMO II** — Application composition, early design, post-architecture — <span dir="rtl">كوكومو 2</span>
- **Putnam model** — Effort-time trade-off with Rayleigh staffing — <span dir="rtl">نموذج بوتنام</span>
- **Rayleigh / Norden curve** — Staffing rises to a peak then decays — <span dir="rtl">منحنى رايلي / نوردن</span>
- **Difficulty metric** — Effort concentration relative to duration — <span dir="rtl">مقياس الصعوبة</span>
- **Risk** — Uncertain event with probability and loss — <span dir="rtl">خطر</span>
- **Risk exposure** — RE = P × L — <span dir="rtl">التعرض للخطر</span>
- **Risk management** — Identification, analysis, planning, monitoring — <span dir="rtl">إدارة المخاطر</span>

**Facts, numbers, formulas**

- **COCOMO 81 effort and schedule:**
$$E = a\,(\text{KLOC})^{b}\ \text{person-months}$$

$$D = c\,E^{d}\ \text{months}$$
Course-book coefficients — Organic a=2.4, b=1.05, c=2.5, d=0.38; Semi-detached a=3.0, b=1.12, c=2.5, d=0.35; Embedded a=3.6, b=1.20, c=2.5, d=0.32.

- **Intermediate COCOMO:** $E = a(KLOC)^{b}\times EAF$, where EAF is the product of the fifteen cost drivers. Fifteen drivers fall into four groups: product, computer, personnel, project. Each is rated very low to very high.
- **Detailed COCOMO:** the intermediate model is applied per module and per phase, so effort is distributed across the phase plan rather than reported as one lump.
- **Function points.** $UFP=\sum(\text{count}\times\text{weight})$ over five component types (external inputs, external outputs, external inquiries, internal logical files, external interface files); $VAF=0.65+0.01\sum_{i=1}^{14}F_i$; $FP=UFP\times VAF$. The VAF range is 0.65 to 1.35.
- **Putnam.** $S=C_k K^{1/3} t_d^{4/3}$ with difficulty $D_0=K/t_d^{3}$ in the course register, and $K=6K_d$ relating total lifecycle effort to development effort.
- **Rayleigh/Norden:** staffing follows a Rayleigh density, peaking at roughly 40 percent of the elapsed schedule; the area under the curve is total effort.
- **Risk exposure:** RE = P(unsatisfactory outcome) × L(loss). Prioritise by exposure, not by probability alone.

**Estimator at a glance — what each model really answers**

| Model | Input | Answers | Blind spot |
|:--|:--|:--|:--|
| LOC | Physical size | How big is the artifact | Language and style bias |
| Function points | Five component types | How much function is delivered | Subjective weighting |
| COCOMO basic | KLOC and mode | Nominal effort and duration | Ignores cost drivers |
| COCOMO intermediate | KLOC plus 15 drivers | Effort adjusted for project attributes | Drivers are rated subjectively |
| COCOMO detailed | Module-level data | Effort per module and phase | Needs a design to exist |
| COCOMO II | Stage-appropriate size | Early and late estimates across the lifecycle | Needs calibrated constants |
| Putnam | Size, difficulty, duration | The effort-time trade-off | Sensitive to the schedule constraint |
| Rayleigh–Norden | Elapsed schedule | Staffing profile over time | Assumes a stable project shape |
| Risk exposure | Probability and loss | Which risk to mitigate first | Probability is a judgement |

**Traps**

- **Two COCOMO parameter families exist.** The course book uses organic 2.4 / semi 3.0 / embedded 3.6; Pressman's table uses 3.2 / 3.0 / 2.8. Quote the set you are working from and say so. Mixing them is the most common arithmetic loss.
- **Effort is not schedule.** Doubling effort never halves duration. Brooks's law: adding people to a late project makes it later through communication overhead.
- **LOC is not a quality measure.** Fewer lines for the same function is better; LOC rewards verbosity if used as a productivity target.
- **Function points are not LOC converted.** Backfiring (LOC to FP) is a rough ratio, not a measurement.
- **COCOMO II model choice is by stage.** Application Composition for early prototyping, Early Design before architecture, Post-Architecture after it. It is not a size ladder.
- **A risk is not a problem.** A problem has already occurred; a risk is a future uncertain event with a probability and a loss.
- **The Rayleigh curve is staffing, not cumulative cost.** Cumulative cost is the integral; the staffing curve is its derivative.

**Three lines**
Size is the input, cost drivers are the correction, and duration is a separate output — never collapse them into one number.
COCOMO answers "how much effort", Putnam answers "how much time can I buy", and both punish schedule compression.
Risk is managed by exposure ranking, not by optimism.

**Definitions to quote**

| Term | Definition | بالعربي |
|:--|:--|:--|
| LOC | Physical source size, sensitive to language and style | حجم مادي |
| Function point | Functional size from five weighted component types | حجم وظيفي |
| COCOMO | Cost model in basic, intermediate and detailed forms | نموذج الكلفة |
| EAF | Product of cost-driver multipliers applied to nominal effort | تعديل الجهد |
| Putnam | Effort-time trade-off with a Rayleigh staffing curve | مقايضة الجهد والمدة |
| Risk exposure | Probability of an unsatisfactory outcome times its loss | احتمال الخسارة |

**Question patterns**

- **"Estimate the project"** → size first, then effort, then duration, then staffing. Three quantities, three outputs; collapsing them into one number is the standard error.
- **"Why did effort explode?"** → schedule compression, scope growth, or underestimated size. Putnam shows the first is non-linear; Brooks shows the second is social.
- **"Which COCOMO model?"** → Basic for a rough early figure, Intermediate when cost drivers are known, Detailed when a module breakdown exists; COCOMO II by lifecycle stage, not by size.
- **"Compute function points"** → classify the five component types, weight them, sum to UFP, add the fourteen general system characteristics to get VAF, multiply. Report both numbers.
- **"Compare LOC and FP"** → LOC measures physical size and punishes verbose languages; FP measures delivered function and needs judgement. Neither is a productivity measure by itself.
- **"Should we add people?"** → no, if the project is late: communication paths grow quadratically, onboarding consumes the people who know the design, and the schedule slips further.
- **"Read the Rayleigh curve"** → staffing rises to a peak near forty percent of the schedule then decays; the area is effort, the peak is a capacity constraint, not a target.
- **"Rank the risks"** → exposure equals probability times loss, so a likely minor risk can outrank a rare catastrophe. Show the arithmetic.
- **"What is a risk?"** → a future uncertain event with a probability and a loss. A problem has already happened; do not merge the two.

## الاسترجاع
AR:التخطيط تقدير احتمالي لا تنبؤ قاطع، وكل نموذج يجيب سؤالاً مختلفاً. يبدأ كل شيء بالحجم: أسطر الشيفرة حجم مادي سهل القياس لكنه متأثر باللغة والأسلوب، ونقاط الوظيفة تقيس الوظيفة المسلَّمة لا الشيفرة ولذلك تقاوم اختلاف اللغة. ثم يحوّل COCOMO الحجم إلى جهد عبر معادلة أُسية، ويضيف النموذج المتوسط عامل تعديل للجهد مبنياً على خمسة عشر محرك كلفة موزعة على المنتج والحاسوب والأفراد والمشروع، بينما يطبّق النموذج المفصّل المنطق نفسه على مستوى الوحدة والطور. أما COCOMO II فيُختار بحسب مرحلة دورة الحياة لا بحسب الحجم: تركيب التطبيقات ثم التصميم المبكر ثم ما بعد المعمارية. ونموذج Putnam يربط الحجم والجهد والمدة فيكشف أن ضغط الجدول يستلزم جهداً أكبر بعلاقة غير خطية، ومنحنى Rayleigh–Norden يصف كيف يرتفع التوظيف إلى ذروة ثم ينحدر. ويُدار الخطر بتعرضه لا باحتماله وحده، فالخطر حدث مستقبلي غير مؤكد وليس مشكلة وقعت، والجهد ليس المدة، وإضافة الأفراد لمشروع متأخر تؤخره أكثر.
