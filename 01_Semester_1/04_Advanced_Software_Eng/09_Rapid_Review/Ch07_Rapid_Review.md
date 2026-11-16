# Chapter 7 — Software Reliability

**Skeleton**

- **Defend the definition.** Reliability is R(t) = P(no failure in [0,t]) under a specified environment. Without the time and the environment, the number is meaningless.
- **Separate software from hardware.** Hardware fails from wear and physical degradation, so its hazard follows the bathtub curve. Software does not wear; it fails when a latent fault is *activated* by an input the operational profile reaches.
- **Fix the vocabulary.** A fault is a latent defect in the code; an error is an incorrect internal state; a failure is the observable deviation from required behaviour. One fault may cause zero, one, or many failures.
- **Use reliability studies for decisions.** Release readiness, test stopping, failure-intensity targets, warranty and support planning, and comparison of design alternatives.
- **Model failure intensity.** Musa's basic execution-time model assumes a linear decrease per failure; the logarithmic Poisson assumes a geometric decrease, which fits many real projects better.
- **Translate execution time to calendar time.** The calendar-time component models availability, staff utilisation, and delay so that a mathematically neat execution-time result becomes a project date.
- **Add classical models.** Jelinski–Moranda (piecewise constant intensity between failures) and bug seeding (capture-recapture estimate of residual faults).
- **Place quality models.** McCall and Boehm give factor hierarchies; ISO 9126 gives six characteristics. CMM and ISO 9001 govern the *process* that produces reliability.

**Keywords**

- **Software reliability** — Probability of failure-free operation in a stated environment — <span dir="rtl">موثوقية البرمجيات</span>
- **Fault / error / failure** — Defect, corrupted state, observable deviation — <span dir="rtl">خطأ كامن / حالة خاطئة / فشل</span>
- **Fault activation** — The input that exposes a latent fault — <span dir="rtl">تنشيط الخطأ</span>
- **Operational profile** — Probability distribution of input usage — <span dir="rtl">الملف التشغيلي</span>
- **Failure intensity** — Failures per unit execution time — <span dir="rtl">شدة الفشل</span>
- **MTTF / MTBF** — Mean time to or between failures — <span dir="rtl">متوسط الزمن للفشل</span>
- **Availability** — MTBF/(MTBF+MTTR) — <span dir="rtl">الإتاحة</span>
- **Basic execution time model** — Linear intensity decay — <span dir="rtl">نموذج زمن التنفيذ الأساسي</span>
- **Logarithmic Poisson** — Geometric intensity decay — <span dir="rtl">بواسون اللوغاريتمي</span>
- **Jelinski–Moranda** — Stepwise constant intensity between failures — <span dir="rtl">جيلينسكي–موراندا</span>
- **Bug seeding** — Capture-recapture estimate of residual faults — <span dir="rtl">بذر العيوب</span>
- **Calendar time component** — Converts execution time to calendar time — <span dir="rtl">مكوّن الزمن التقويمي</span>
- **McCall model** — Eleven quality factors in three groups — <span dir="rtl">نموذج ماكول</span>
- **Boehm model** — Hierarchical quality factors — <span dir="rtl">نموذج بوهم</span>
- **ISO 9126** — Six quality characteristics — <span dir="rtl">أيزو 9126</span>
- **CMM** — Five process maturity levels — <span dir="rtl">نموذج نضج القدرات</span>
- **KPA** — Level-specific process capability area — <span dir="rtl">منطقة عملية رئيسية</span>

**Facts, numbers, formulas**

- **Reliability and intensity.** For constant failure intensity, $R(t)=e^{-\lambda t}$ and $MTBF=1/\lambda$. Availability $A=\dfrac{MTBF}{MTBF+MTTR}$.
- **Musa basic execution time model.**

$$\lambda(\mu)=\lambda_0\left(1-\frac{\mu}{v_0}\right)$$

$$\mu(\tau)=v_0\left[1-e^{-\lambda_0\tau/v_0}\right]$$

$$\lambda(\tau)=\lambda_0 e^{-\lambda_0\tau/v_0}$$

$$\Delta\mu=\frac{v_0}{\lambda_0}(\lambda_P-\lambda_F),\qquad \Delta\tau=\frac{v_0}{\lambda_0}\ln\frac{\lambda_P}{\lambda_F}$$

- **Musa logarithmic Poisson model.** With decay parameter $\theta$:

$$\lambda(\mu)=\lambda_0 e^{-\theta\mu}$$

$$\mu(\tau)=\frac{1}{\theta}\ln(\lambda_0\theta\tau+1)$$

$$\lambda(\tau)=\frac{\lambda_0}{\lambda_0\theta\tau+1}$$

- **Jelinski–Moranda.** With $N$ initial faults and proportionality constant $\phi$, the intensity during the $i$-th interval is $\lambda_i=\phi\,[N-(i-1)]$, so $MTTF_i=1/\lambda_i$. Every failure removes exactly one fault.
- **Bug seeding.** If $n_1$ seeded and $n_2$ indigenous faults are found, with $n_{12}$ seeded faults among them, the estimated indigenous total is $\hat{N}=\dfrac{n_1n_2}{n_{12}}$ (capture-recapture), and residual faults are $\hat{N}-n_2$.
- **McCall's eleven factors** in three groups: product operations (correctness, reliability, efficiency, integrity, usability), product revision (maintainability, flexibility, testability), product transition (portability, reusability, interoperability).
- **Boehm's hierarchy:** three high-level uses (as-is utility, maintainability, portability) refined into seven intermediate qualities (portability, reliability, efficiency, human engineering, testability, understandability, modifiability).
- **ISO 9126 six characteristics:** functionality, reliability, usability, efficiency, maintainability, portability, each with sub-characteristics.
- **CMM five levels:** Initial → Repeatable (managed) → Defined → Managed (quantitative) → Optimizing. Each level is defined by key process areas, and every KPA is described through five common features: commitment to perform, ability to perform, activities performed, measurement and analysis, verifying implementation.

**Model at a glance — assumption first, formula second**

| Model | Core assumption | Shape of decay | Use it for |
|:--|:--|:--|:--|
| Musa basic execution time | Finite $v_0$ faults, linear intensity loss per failure | Linear in $\mu$ | Stable test environment, early planning |
| Musa logarithmic Poisson | Faults vary in detectability; decaying returns | Geometric per failure | Large systems where later faults are harder |
| Jelinski–Moranda | One fault removed per failure, constant per-fault hazard | Stepwise constant | Classical teaching and small datasets |
| Bug seeding | Seeded and indigenous faults are equally detectable | Capture–recapture ratio | Estimating residual faults, no time model |
| Calendar-time component | Execution time converts through availability and staff utilisation | Piecewise conversion | Turning τ into a delivery date |

**Traps**

- **"Software wears out like hardware."** It does not. Hardware hazard follows the bathtub curve; software failure intensity depends on fault activation and removal.
- **Fault, error, and failure are not synonyms.** A fault is latent, an error is an internal state, a failure is the external symptom.
- **One fault, one failure?** No. A fault can never be activated, or can cause many failures before removal.
- **Reliability without an operational profile.** The same program has different field reliability under different usage distributions; state the profile or the number is unfalsifiable.
- **Confusing execution time with calendar time.** Musa's models are in execution time. Calendar time needs the calendar-time component, availability, and staffing delays.
- **Basic versus logarithmic Poisson.** Basic implies a fixed total failure count v_0 and linear decay; logarithmic Poisson implies decreasing returns and unbounded total failures.
- **ISO 9001 is not CMM.** ISO 9001 is a generic contract-oriented quality management standard stating *what* must be controlled; CMM is software-specific, staged, and prescriptive about process capability.
- **CMM level names.** Level 2 is Repeatable (also called Managed); level 4 is Managed (Quantitatively Managed). Do not shift the ladder.

**Three lines**
Reliability is a probability with two hidden arguments: time and operational profile.
Musa's two models differ only in how intensity decays; everything else follows from that choice.
Models estimate; CMM and ISO 9001 change the process that produces the number.

**Definitions to quote**

| Term | Definition | بالعربي |
|:--|:--|:--|
| Reliability | Probability of failure-free operation for a stated time and environment | احتمال بزمن وبيئة |
| Fault / error / failure | Latent defect, incorrect state, observable deviation | عيب ثم حالة ثم فشل |
| Operational profile | Probability distribution of input usage in the field | توزيع الاستخدام |
| Failure intensity | Failures per unit of execution time | فشل لكل وحدة زمن |
| CMM | Five process maturity levels defined by key process areas | نضج العملية |
| ISO 9126 | Six quality characteristics including reliability and maintainability | ست خصائص جودة |

- **Reliability versus safety.** Reliability counts failures; safety counts harm. A system can be reliable and unsafe, or unreliable and safe.
- **Failure intensity versus defect density.** Intensity is a rate in execution time; density is a count per unit size. They answer different questions and are not interchangeable.

**Question patterns**

- **"Define reliability"** → probability of failure-free operation for a stated time in a stated environment. Drop any of the three and the number is meaningless.
- **"Compute the basic model"** → $\lambda(\mu)=\lambda_0(1-\mu/v_0)$ for a failure count, or the exponential form for a time. State the units: failures per CPU hour.
- **"Which model fits?"** → basic when each fault contributes equally, logarithmic Poisson when later faults are harder to find, Jelinski–Moranda for stepwise classical treatment, bug seeding when there is no time data.
- **"Reliability or availability?"** → reliability is uninterrupted operation over an interval; availability is the fraction of time the service is up, including repairs. High availability can coexist with poor reliability.
- **"Why does the operational profile matter?"** → it sets which faults are activated, so the same code has different field reliability under different usage mixes.
- **"CMM level question"** → place the practice on the ladder: Initial, Repeatable, Defined, Managed, Optimizing, then name the key process area and the common feature.
- **"ISO 9001 or CMM?"** → ISO 9001 is a generic contract-oriented quality system stating what must be controlled; CMM is software-specific, staged and prescriptive about capability.
- **"Estimate residual faults"** → seed faults, count the overlap, apply capture-recapture $\hat N=n_1n_2/n_{12}$, and state the equal-detectability assumption.
- **"Translate to calendar time"** → execution time is not delivery time; apply availability, staff utilisation and delay, then report the calendar date.

## الاسترجاع
AR:الموثوقية احتمال، ومن دون زمن محدد وبيئة تشغيل محددة تصبح رقماً بلا معنى. تُعرَّف بأنها احتمال العمل دون فشل في فترة معينة داخل بيئة معينة، والملف التشغيلي هو توزيع احتمال الاستخدام الذي يحدد أي عيب كامن سيُستثار. ويجب التفريق بين الخطأ الكامن والحالة الخاطئة والفشل المرصود، فالعيب الواحد قد لا يُستثار أبداً أو يُنتج فشلاً واحداً أو فشلاً متكرراً. والعتاد يبلى مادياً فيأخذ منحنى الحوض، أما البرمجيات فلا تبلى وإنما يعتمد فشلها على كثافة تنشيط العيوب. ويُدار ذلك بنماذج شدة الفشل: نموذج زمن التنفيذ الأساسي يفترض تناقصاً خطياً مع كل عيب يُزال، ونموذج بواسون اللوغاريتمي يفترض تناقصاً هندسياً لأن العيوب الأخيرة أصعب اكتشافاً، ونموذج Jelinski–Moranda يفترض ثبات الخطر بين كل فشلين. ويُضاف بذر العيوب لتقدير المتبقي بأسلوب الأسر والاستعادة، ومكوّن الزمن التقويمي ليحوّل زمن التنفيذ إلى تاريخ تسليم. ثم تُوضع الجودة في نماذج McCall وBoehm وISO 9126، والنضج في CMM بمستوياته الخمسة، وISO 9001 يعالج الإدارة العامة لا نضج عملية البرمجيات.
