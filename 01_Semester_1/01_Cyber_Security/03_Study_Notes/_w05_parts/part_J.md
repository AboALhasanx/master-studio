### القسم 1 — 6. Emerging Trends in Defense in Depth

#### ① النص الأصلي

> Defense in depth is evolving from static layers toward adaptive, resilient designs. Machine learning models dynamically adjust security controls based on real-time telemetry; for example, anomaly-based IDS coupled with predictive analytics can anticipate new attack vectors.
>
> The governing model here is Bayesian updating of risk, where A is the presence of an attack and E is the observed evidence; continuous updating enables adaptive thresholds.
>
> Defense in depth is now extended with resilience engineering, ensuring recovery and continuity even when defenses are breached. Resilience is captured by a reliability function over time t, where λ is the failure rate of layered defenses; a lower λ reflects higher resilience due to redundancy.

$$P(A \mid E) = \frac{P(E \mid A)\,P(A)}{P(E \mid A)\,P(A) + P(E \mid \lnot A)\,P(\lnot A)}$$

$$R(t) = e^{-\lambda t}$$

#### ② الترجمة

> «الدفاع في العمق يتطوّر من طبقات جامدة إلى تصاميم تكيّفية ومرنة. نماذج تعلّم الآلة تعدّل ضوابط الأمن ديناميكيًا اعتمادًا على القياسات اللحظية (telemetry)؛ فمثلًا، نظام كشف التسلل القائم على الشذوذ (anomaly-based IDS) مقترنًا بالتحليلات التنبؤية يستطيع توقّع نواقل هجوم جديدة.
>
> النموذج الحاكم هنا هو التحديث البايزي للمخاطر (Bayesian updating)، حيث A وجود الهجوم و E الدليل المرصود؛ والتحديث المستمر يمكّن من عتبات تكيّفية (adaptive thresholds).
>
> ثم يُوسَّع الدفاع في العمق بهندسة المرونة (resilience engineering)، بما يضمن التعافي والاستمرارية حتى عند اختراق الدفاعات. وتُعبَّر المرونة بدالة موثوقية (reliability function) على الزمن t، حيث λ معدّل فشل الدفاعات الطبقية؛ فانخفاض λ يعكس مرونة أعلى بفعل التكرار الاحتياطي (redundancy).»

#### ③ الشرح الفهمي

الدفاع في العمق التقليدي = طبقات ثابتة (firewall, IDS, WAF, EDR). الجديد هنا إنه صار «حيّ»: كل ما تجيه telemetry جديدة يعدّل قراره. هذا هو جوهر الـ **adaptive defense** — بدل قواعد مكتوبة مرّة وتنتهي، عندنا نظام يتعلّم ويتغيّر.

**١) التحديث البايزي (Bayesian updating):**

$$P(A \mid E) = \frac{P(E \mid A)\,P(A)}{P(E \mid A)\,P(A) + P(E \mid \lnot A)\,P(\lnot A)}$$

| الرمز | المعنى |
|---|---|
| $A$ | وجود الهجوم (attack present) |
| $E$ | الدليل المرصود (observed evidence) |
| $P(A)$ | الاحتمال المسبق للهجوم قبل رؤية الدليل (prior) |
| $P(E \mid A)$ | احتمال رؤية الدليل بوجود هجوم فعلي |
| $P(E \mid \lnot A)$ | احتمال رؤية نفس الدليل بدون هجوم (معدّل الإنذار الكاذب) |
| $P(A \mid E)$ | الاحتمال اللاحق للهجوم بعد رؤية الدليل (posterior) |

الفكرة: كل ما يجي دليل جديد نحدّث اعتقادنا. لو نفس الدليل ممكن يجي من ضجة طبيعية (يعني $P(E \mid \lnot A)$ عالية) ← الـ posterior ما يرتفع واجد، وهذا يحمينا من الإنذارات الكاذبة. و«العتبات التكيّفية» تعني إن النظام يرفع أو ينزّل الحساسية حسب السياق الحالي بدل ما تكون ثابتة.

**٢) دالة الموثوقية (reliability function):**

$$R(t) = e^{-\lambda t}$$

| الرمز | المعنى |
|---|---|
| $R(t)$ | احتمال بقاء النظام شغّالًا بلا فشل حتى الزمن $t$ |
| $t$ | الزمن |
| $\lambda$ | معدّل الفشل (failure rate) للدفاعات الطبقية |
| $e$ | أساس اللوغاريتم الطبيعي |

كل ما $\lambda$ أصغر ← $R(t)$ أعلى ← مرونة (resilience) أعلى، وهذا يصير بفضل الـ redundancy.

مقارنة سريعة بين الطرازين:

| البُعد | دفاع في العمق التقليدي | دفاع في العمق التكيّفي |
|---|---|---|
| الضوابط | ثابتة (static) | تتغيّر حسب telemetry |
| أساس القرار | قواعد يكتبها الإنسان | نماذج ML + تحديث بايزي |
| هدف التصميم | منع الاختراق | منع + مرونة + تعافٍ |

### القسم 2 — 7. Case Studies

#### ① النص الأصلي

> Three incidents illustrate the value of segmentation and layered defense:
>
> - **Target Data Breach (2013):** Attackers gained entry through a third-party vendor and moved laterally across a flat internal network; the lack of segmentation allowed them to reach payment card systems.
> - **Stuxnet (2010):** Although segmented networks were present in industrial systems, inadequate depth in defense allowed attackers to exploit trusted certificates and removable media — highlighting the need for both segmentation and multi-layered defenses.
> - **Financial Sector Micro segmentation:** Global banks adopted micro segmentation using software-defined policies, reducing lateral movement; risk exposure decreased by 35–40% based on internal metrics.

#### ② الترجمة

> «ثلاث حوادث توضّح قيمة التقسيم (segmentation) والدفاع الطبقي:
>
> - **اختراق Target (2013):** دخل المهاجمون عبر مورّد خارجي (third-party vendor) وتحرّكوا جانبيًا (lateral movement) داخل شبكة داخلية مسطّحة (flat)؛ وغياب التقسيم سمح لهم بالوصول إلى أنظمة بطاقات الدفع.
> - **Stuxnet (2010):** مع إن الشبكات في الأنظمة الصناعية كانت مقطّعة، إلا إن قلة العمق في الدفاع (inadequate depth) سمحت للمهاجمين باستغلال شهادات موثوقة (trusted certificates) ووسائط قابلة للإزالة (removable media) — وهذا يبيّن إنك تحتاج الاثنين معًا: تقسيم + دفاع متعدد الطبقات.
> - **التقسيم الدقيق في القطاع المالي (Micro segmentation):** البنوك العالمية تبنّت micro segmentation بسياسات معرّفة برمجيًا (software-defined)، ممّا قلّل الحركة الجانبية؛ وانخفض التعرّض للمخاطر بنسبة 35–40% حسب مؤشرات داخلية.»

#### ③ الشرح الفهمي

الثلاث حالات تعطي ثلاث دروس مختلفة، وكل واحدة تكمّل الثانية:

| الحالة | شنو صار | الدرس |
|---|---|---|
| Target 2013 | شبكة داخلية مسطّحة (flat) ← حركة جانبية حرّة | غياب التقسيم = الكارثة |
| Stuxnet 2010 | كان فيه تقسيم، بس العمق ضعيف | التقسيم لحده ما يكفي بلا طبقات |
| Micro segmentation المالي | سياسات software-defined | التقسيم الدقيق قلّل المخاطر 35–40% |

توضيح كل حالة:

- **Target** = دليل على إن الـ flat network خطر. الهجوم ما جاء من ضعف تشفير أو خوارزمية — جاء من إن كل الأجهزة تقدر توصل لبعضها. لو كان فيه segmentation، كان الهجوم وقف عند نقطة الدخول بدل ما يوصل لبطاقات الدفع.
- **Stuxnet** = العكس بالمعنى: كان فيه segmentation (شبكات معزولة صناعيًا) بس نفّذ الهجوم عبر قنوات «موثوقة» (شهادات موثوقة + USB). هذا يثبت إن التقسيم لحده لا يكفي — لازم defense in depth معه.
- **القطاع المالي** = الدليل العملي على الفائدة: نفس فكرة الـ micro segmentation بالـ SDN قلّلت المخاطر 35–40%. لاحظ إن الرقم جاي من internal metrics (مصدر داخلي) — مو رقم نظري.

الخلاصة: **segmentation + depth سوا**. أي واحد لحده يفشل.

### القسم 3 — 8. Quantitative Evaluation of Emerging Models

#### ① النص الأصلي

> Two models allow a quantitative evaluation of the emerging approaches.
>
> The **segmentation cost-benefit model** uses Return on Security Investment (ROSI). Let the cost of implementing segmentation be Cs and the expected annual loss reduction be ΔL. If segmentation reduces the annual breach cost from 10 million to 6 million at a cost of 2 million, ROSI equals 1, or 100%.
>
> The **optimal layer allocation model** asks: given a budget B and the cost of each layer ci, maximize risk reduction, subject to the total layer cost not exceeding B. This optimization ensures a rational allocation of resources across defensive layers.

$$ROSI = \frac{\Delta L - C_s}{C_s}$$

$$\max \left( R_0 - R_{residual} \right) = R_0 \left( 1 - \prod_{i=1}^{n} (1 - r_i) \right) \quad \text{subject to} \quad \sum_{i=1}^{n} c_i \le B$$

#### ② الترجمة

> «نموذجان يسمحان بتقييم كمّي للأساليب الناشئة.
>
> **نموذج الكلفة-الفائدة للتقسيم (segmentation cost-benefit model)** يستخدم العائد على الاستثمار الأمني (ROSI). لنفترض إن كلفة تنفيذ التقسيم $C_s$ والانخفاض السنوي المتوقّع في الخسارة $\Delta L$. لو التقسيم قلّل كلفة الاختراق السنوية من 10 مليون إلى 6 مليون بكلفة 2 مليون، فإن ROSI تساوي 1، أي 100%.
>
> **نموذج التوزيع الأمثل للطبقات (optimal layer allocation)** يسأل: بمعطى ميزانية $B$ وكلفة كل طبقة $c_i$، عظّم تقليل المخاطر، بشرط ألّا يتجاوز مجموع كلف الطبقات $B$. هذا التحسين يضمن توزيعًا عقلانيًا للموارد على طبقات الدفاع.»

#### ③ الشرح الفهمي

هنا ننتقل من الكلام النظري إلى الأرقام. نموذجان:

**١) ROSI — العائد على الاستثمار الأمني:**

$$ROSI = \frac{\Delta L - C_s}{C_s}$$

| الرمز | المعنى |
|---|---|
| $\Delta L$ | الانخفاض السنوي المتوقّع في الخسارة (expected annual loss reduction) |
| $C_s$ | كلفة تنفيذ التقسيم (cost of implementing segmentation) |
| $ROSI$ | العائد على الاستثمار الأمني (Return on Security Investment) |

مثال من النص: كلفة الاختراق السنوية نزلت من 10M إلى 6M، يعني $\Delta L = 4M$، والكلفة $C_s = 2M$:

$$ROSI = \frac{4 - 2}{2} = 1 = 100\%$$

يعني كل وحدة نقدية تحطها، ترجع لك ضعفها بالمنفعة. لو ROSI > 0 ← المشروع مربح أمنيًا؛ لو ROSI < 0 ← ما يستاهل من ناحية اقتصادية بحتة.

**٢) التوزيع الأمثل للطبقات تحت قيد الميزانية:**

$$\max \left( R_0 - R_{residual} \right) = R_0 \left( 1 - \prod_{i=1}^{n} (1 - r_i) \right) \quad \text{subject to} \quad \sum_{i=1}^{n} c_i \le B$$

| الرمز | المعنى |
|---|---|
| $R_0$ | المخاطر الابتدائية قبل أي طبقة (initial risk) |
| $r_i$ | نسبة تقليل المخاطر للطبقة $i$، حيث $r_i \in (0,1)$ |
| $R_{residual}$ | المخاطر المتبقية بعد كل الطبقات |
| $n$ | عدد طبقات الدفاع |
| $c_i$ | كلفة الطبقة $i$ |
| $B$ | الميزانية الكلية (budget) |

المعنى: نريد نكبّر الفرق بين المخاطر الابتدائية والمتبقية (يعني نقلّل المخاطر أكثر ما يمكن)، بس بشرط إن مجموع الكلف ما يتجاوز الميزانية. هذا هو الـ **constrained optimization** — نفس منطق الـ knapsack. الطبقات الرخيصة وذات $r_i$ العالية تكون أولوية، والغالية قليلة الفائدة تتأجّل.

ملاحظة: النص الأصلي كان يستخدم رمز العملة الدولارية للمبالغ؛ هنا ذكرنا المبالغ كأرقام مجرّدة (10M, 6M, 2M) لتجنّب كتابة رمز العملة.

### القسم 4 — 9. Synthesis and Future Directions

#### ① النص الأصلي

> The convergence of network segmentation and defense in depth demonstrates the maturity of network security practices — a shift from static perimeter defense to dynamic, multi-layered resilience frameworks.
>
> Future directions include:
>
> - AI-driven segmentation policies that dynamically adapt zones based on observed traffic flows.
> - Quantum-resistant defense layers, ensuring cryptographic elements remain secure against quantum computing.
> - Self-healing networks, where defense-in-depth mechanisms automatically reconfigure after compromise.
>
> Network segmentation and defense in depth remain central strategies for safeguarding contemporary information infrastructures. Segmentation disrupts lateral movement, containing breaches within defined zones, while defense in depth ensures that multiple, redundant controls provide resilience even when individual mechanisms fail. The mathematical models — from residual risk formulations to attack path probabilities, Bayesian updating, and optimization under budget constraints — illustrate the scientific foundations of these strategies, enabling rigorous evaluation, predictive analysis, and resource optimization.
>
> As emerging trends reshape the security landscape through Zero Trust, micro segmentation, AI-driven defenses, and cloud-native deployments, the principles of segmentation and layered defense will continue to evolve. Their fusion represents not merely defensive measures but a holistic paradigm for resilience, adaptability, and strategic alignment between cybersecurity and organizational governance.

#### ② الترجمة

> «تقارب التقسيم الشبكي والدفاع في العمق يُظهر نضوج ممارسات أمن الشبكات — تحوّلًا من دفاع محيطي ثابت (static perimeter) إلى أطر مرونة ديناميكية متعددة الطبقات.
>
> الاتجاهات المستقبلية تشمل:
>
> - سياسات تقسيم مدفوعة بالذكاء الاصطناعي (AI-driven) تعدّل المناطق ديناميكيًا حسب تدفّقات الترافيك المرصودة.
> - طبقات دفاع مقاومة للحوسبة الكمّية (quantum-resistant)، تضمن بقاء العناصر التشفيرية آمنة ضد الحوسبة الكمّية.
> - شبكات ذاتية الشفاء (self-healing)، حيث تعيد آليات الدفاع في العمق تشكيل نفسها تلقائيًا بعد الاختراق.
>
> يبقى التقسيم الشبكي والدفاع في العمق استراتيجيتين محوريتين لحماية البنى المعلوماتية المعاصرة. التقسيم يعطّل الحركة الجانبية، فيحتوي الاختراقات داخل مناطق محدّدة، بينما يضمن الدفاع في العمق إن ضوابط متعددة ومكرّرة توفّر المرونة حتى عند فشل آليات فردية. والنماذج الرياضية — من صيغ المخاطر المتبقية إلى احتمالات مسارات الهجوم والتحديث البايزي والتحسين تحت قيود الميزانية — تُظهر الأسس العلمية لهذه الاستراتيجيات، وتمكّن من التقييم الصارم والتحليل التنبؤي وتحسين الموارد.
>
> ومع إعادة صياغة الاتجاهات الناشئة لمشهد الأمن عبر Zero Trust والتقسيم الدقيق والدفاعات المدفوعة بالذكاء الاصطناعي والنشر السحابي (cloud-native)، ستستمر مبادئ التقسيم والدفاع الطبقي في التطوّر. ودمجها يمثّل ليس مجرّد تدابير دفاعية، بل نموذجًا شموليًا للمرونة والقابلية للتكيّف والمواءمة الاستراتيجية بين الأمن السيبراني وحوكمة المنظّمة.»

#### ③ الشرح الفهمي

الفصل يختم بخلاصة: التقسيم والدفاع في العمق مو «حلول منفصلة» — هم فكرة وحدة اسمها **layered resilience**.

| الاستراتيجية | شنو تسوي | الأثر |
|---|---|---|
| Segmentation | تقسّم الشبكة لمناطق معزولة | توقف الـ lateral movement |
| Defense in depth | طبقات متعددة متداخلة | لو طبقة فشلت، الثانية تعوّض |

الاتجاهات الثلاثة المستقبلية:

| الاتجاه | الفكرة | ليش مهم |
|---|---|---|
| AI-driven segmentation | مناطق تتغيّر تلقائيًا حسب الترافيك | الشبكات السحابية تتغيّر بسرعة، فالقواعد الثابتة تتقادم |
| Quantum-resistant layers | تشفير يقاوم الحواسيب الكمّية | الخوف إن الـ RSA/ECC الحالي ينكسر مستقبلًا |
| Self-healing networks | إعادة تشكيل تلقائي بعد الاختراق | يقلّل زمن التعافي (recovery) ويحافظ على الاستمرارية |

الخلاصة الكبرى: النماذج الرياضية في الفصل (residual risk، attack path probability، Bayesian updating، budget optimization) مو زينة — هي اللي تخلّي القرار الأمني **قابل للقياس** بدل ما يكون بالحدس. يعني تقدر تجاوب على سؤال: «وين أحط فلوسي الأمنية حتى أحصل أكبر تقليل خطر؟»
