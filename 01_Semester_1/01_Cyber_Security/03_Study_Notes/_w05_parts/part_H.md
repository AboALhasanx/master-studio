### القسم 1 — 7. IDS/IPS in Encrypted Environments

#### ① النص الأصلي

> 7.1 Challenge of TLS/SSL inspection
>
> The ubiquity of encrypted traffic — today over 90% of Internet traffic — obscures payload inspection and forces IDS/IPS to adapt. Solutions include:
>
> • TLS termination at proxies/firewalls.
> • Metadata analysis (e.g., JA3 TLS fingerprinting).
> • Encrypted Traffic Analytics (ETA) using ML models.
>
> 7.2 Mathematical model for encrypted traffic anomaly detection
>
> Traffic features f_i (packet size, timing, direction) form a feature vector **f**. Its probability density function is modeled with a Gaussian Mixture Model, and a low likelihood p(**f**) < τ implies an anomaly.

$$p(\mathbf{f}) = \sum_{k=1}^{K} \pi_k \, \mathcal{N}\!\left(\mathbf{f} \mid \mu_k, \Sigma_k\right)$$

#### ② الترجمة

> «7.1 تحدّي فحص الـ TLS/SSL
>
> انتشار الترافيك المشفّر — اليوم أكثر من 90% من ترافيك الإنترنت — يخفي فحص الـ payload ويجبر الـ IDS/IPS إنه يتكيّف. الحلول تشمل:
>
> • إنهاء الـ TLS عند الـ proxies/firewalls.
> • تحليل الـ metadata (مثلاً JA3 TLS fingerprinting).
> • Encrypted Traffic Analytics (ETA) باستخدام موديلات ML.
>
> 7.2 الموديل الرياضي لكشف الـ anomaly بالترافيك المشفّر
>
> خصائص الترافيك f_i (حجم الـ packet، التوقيت، الاتجاه) تكوّن feature vector **f**. ودالة كثافة الاحتمال تتنمذج بـ Gaussian Mixture Model، والاحتمال المنخفض p(**f**) < τ يعني وجود anomaly.»

#### ③ الشرح الفهمي

هذا القسم يحلّ مشكلة أساسية: الـ IDS/IPS التقليدي يشوف الـ payload ويطابق الـ signatures، بس هسه أغلب الترافيك مشفّر (TLS)، فالـ payload يبينله عتمة. يعني صار "أعمى" قدام الهجمات اللي مخبّية داخل قنوات مشفّرة.

الحلول الثلاثة للفحص:

| الحل | شنو يسوي | الملاحظة |
|---|---|---|
| TLS termination | يفكّ التشفير عند الـ proxy/firewall، يفحص، وبعدين يعيد يشفّره | يشتغل بس الـ proxy يصير high-value target |
| Metadata analysis | ما يلمس المحتوى، بس يفحص بصمة الـ handshake (JA3) | خفيف وما يكسر الخصوصية |
| ETA (Encrypted Traffic Analytics) | يستخدم ML على إحصاءات الترافيك بدل المحتوى | الأحدث والأكثر قابلية للتوسع |

فكرة الـ GMM: بدل ما نفحص "شنو داخل الـ packet"، نفحص "شكل الـ flow". ننمذج الترافيك الطبيعي كخليط من K من الـ Gaussian distributions. إذا جاك flow جديد، نحسب احتماله؛ إذا كان أقل من threshold τ، يعني الـ flow شاذ (anomaly).

$$p(\mathbf{f}) = \sum_{k=1}^{K} \pi_k \, \mathcal{N}\!\left(\mathbf{f} \mid \mu_k, \Sigma_k\right)$$

| الرمز | المعنى |
|---|---|
| $p(\mathbf{f})$ | احتمال إنه الـ flow يكون طبيعي |
| $\mathbf{f}$ | feature vector (حجم الـ packet، التوقيت، الاتجاه) |
| $K$ | عدد الـ Gaussian components |
| $\pi_k$ | وزن الـ component رقم $k$ (مجموع الأوزان = 1) |
| $\mu_k$ | المتوسط (mean) للـ component رقم $k$ |
| $\Sigma_k$ | مصفوفة التغاير (covariance) للـ component رقم $k$ |
| $\mathcal{N}(\dots)$ | دالة الـ Gaussian (normal) distribution |
| $\tau$ | الـ threshold: إذا $p(\mathbf{f}) < \tau$ نعتبره anomaly |

---

### القسم 2 — 8. Case Studies and Incidents

#### ① النص الأصلي

> 8.1 Snort and Suricata adoption
>
> Open-source IDS frameworks like Snort became global standards, while Suricata introduced multithreaded performance to address high-throughput environments.
>
> 8.2 Heartbleed exploitation
>
> The Heartbleed bug in OpenSSL bypassed IDS/IPS visibility into encrypted payloads, illustrating the challenges of monitoring vulnerabilities within encrypted channels.
>
> 8.3 Stuxnet and stealth
>
> Stuxnet avoided detection through rootkits that manipulated process-control-system logs, demonstrating that sophisticated adversaries target IDS blind spots.

#### ② الترجمة

> «8.1 تبنّي Snort وSuricata
>
> أطر الـ IDS مفتوحة المصدر مثل Snort صارت معايير عالمية، بينما Suricata أدخلت أداء multithreaded لمعالجة البيئات عالية الإنتاجية.
>
> 8.2 استغلال Heartbleed
>
> ثغرة Heartbleed بـ OpenSSL تجاوزت رؤية الـ IDS/IPS للـ payload المشفّر، وهذا يوضّح تحدّيات مراقبة الثغرات داخل القنوات المشفّرة.
>
> 8.3 Stuxnet والتخفّي
>
> Stuxnet تجنّب الكشف عبر rootkits تلاعبت بسجلات أنظمة التحكم بالعمليات، وهذا يبيّن إن الخصوم المتقدمين يستهدفون النقاط العمياء للـ IDS.»

#### ③ الشرح الفهمي

هذا القسم ثلاث دراسات حالة، وكلها تدور حول نفس الفكرة: الـ IDS/IPS عندها نقاط عمياء، والمهاجم الشاطر يستهدفها.

| الحالة | شنو صار | الدرس |
|---|---|---|
| Snort & Suricata | Snort صار معيار عالمي مفتوح المصدر، وSuricata حلّت مشكلة الأداء بالـ multithreading | الـ IDS صار commodity، والأداء صار عامل حاسم بالشبكات السريعة |
| Heartbleed (2014) | ثغرة بـ OpenSSL سرّبت ذاكرة الـ server (منها مفاتيح خاصة)، والـ IDS ما شافها لأن الترافيك مشفّر | الـ IDS ما تكدر تراقب الـ vulnerabilities داخل القناة المشفّرة نفسها |
| Stuxnet (2010) | استخدمت rootkits تعدّل سجلات أنظمة التحكم (ICS/SCADA) | الخصم المتقدم يستهدف logs ونقاط عمياء حتى ما ينكشف |

الخلاصة: ما تكفي بس تحطّ IDS وتعتبر نفسك آمن. لازم تعرف وين عمياء، وتكمّل بالـ endpoint detection والـ integrity monitoring.

---

### القسم 3 — 9. Integration with SIEM and SOAR

#### ① النص الأصلي

> Modern IDS/IPS feed alerts into Security Information and Event Management (SIEM) systems, which correlate events across sources, and into Security Orchestration, Automation, and Response (SOAR) platforms, which automate responses. Correlation is modeled as a weighted sum of evidence, and if the score exceeds a threshold θ, an incident is declared.

$$C(E) = \sum_{i=1}^{n} w_i e_i$$

#### ② الترجمة

> «الـ IDS/IPS الحديثة تغذّي التنبيهات لأنظمة Security Information and Event Management (SIEM)، اللي تربط الأحداث بين المصادر المختلفة، ولأنظمة Security Orchestration, Automation, and Response (SOAR)، اللي تؤتمت الاستجابات. والربط (correlation) يتنمذج كمجموع مرجّح للأدلة، وإذا النتيجة تجاوزت threshold θ، تُعلن حادثة (incident).»

#### ③ الشرح الفهمي

الفكرة: الـ IDS/IPS لحالها تنتج تنبيهات كثيرة، وأغلبها ممكن يكون false positives. فبدل ما نتعامل مع كل تنبيه لحاله، نرسله للـ SIEM اللي يربط (correlate) الأحداث من مصادر متعددة، وبعدين الـ SOAR يؤتمت الاستجابة (مثلاً يفتح ticket أو يعزل host).

$$C(E) = \sum_{i=1}^{n} w_i e_i$$

| الرمز | المعنى |
|---|---|
| $C(E)$ | نتيجة الربط (correlation score) |
| $E$ | مجموعة الأدلة (evidence) القادمة من التنبيهات |
| $e_i$ | دليل رقم $i$ من تنبيهات الـ IDS/IPS |
| $w_i$ | وزن الربط (correlation weight) للدليل $e_i$ |
| $n$ | عدد الأدلة |
| $\theta$ | الـ threshold: إذا $C(E) > \theta$ تُعلن حادثة (incident) |

نقطة مهمة: الأوزان $w_i$ تعبّر عن "أهمية" كل دليل — مثلاً تنبيه من IPS + تسجيل دخول غريب + تغيير بصلاحيات = مجموع عالي ← incident. هذا يقلّل الـ noise ويخلي القرار أكثر دقة.

---

### القسم 4 — 10. IDS/IPS in Next-Generation Architectures

#### ① النص الأصلي

> 10.1 Cloud-native environments
>
> IDS/IPS are integrated into cloud fabrics, monitoring east–west traffic inside virtualized networks.
>
> 10.2 Zero Trust architectures
>
> IDS/IPS support continuous verification of device and user behavior, monitoring micro-segmented environments.
>
> 10.3 AI-driven systems
>
> Machine learning enhances IDS/IPS to adapt to evolving threats, reducing reliance on static signatures. Adversarial ML attacks (evasion, poisoning) introduce new research challenges.

#### ② الترجمة

> «10.1 البيئات السحابية الأصلية (Cloud-native)
>
> الـ IDS/IPS تُدمج داخل الـ cloud fabrics، وتراقب ترافيك east–west داخل الشبكات الافتراضية.
>
> 10.2 معماريات Zero Trust
>
> الـ IDS/IPS تدعم التحقق المستمر من سلوك الأجهزة والمستخدمين، وتراقب البيئات micro-segmented.
>
> 10.3 الأنظمة المدفوعة بالذكاء الاصطناعي (AI-driven)
>
> الـ machine learning يعزّز الـ IDS/IPS حتى تتكيّف مع التهديدات المتطوّرة، ويقلّل الاعتماد على الـ signatures الثابتة. وهجمات adversarial ML (الـ evasion والـ poisoning) تقدّم تحدّيات بحثية جديدة.»

#### ③ الشرح الفهمي

هذا القسم يبيّن إن الـ IDS/IPS ما بقيت بس على حافة الشبكة، بل انتقلت لبيئات جديدة:

| البيئة | شنو تغيّر | ليش مهم |
|---|---|---|
| Cloud-native | مراقبة ترافيك east–west داخل الشبكات الافتراضية | بالـ cloud الترافيك الداخلي كبير وأهم من الحافة |
| Zero Trust | تحقق مستمر من الجهاز والمستخدم + مراقبة micro-segmentation | ما بقى في "ثقة ضمنية" داخل الشبكة |
| AI-driven | ML يتكيّف مع تهديدات جديدة بدل signatures ثابتة | الـ malware يتغيّر بسرعة، فالـ static signatures تفشل |

نقطة حساسة: الـ AI-driven IDS تفتح باب جديد للهجوم — **adversarial ML**:

- **Evasion**: المهاجم يعدّل الـ input شوي حتى يخدع الموديل ويعدّيه كـ benign.
- **Poisoning**: المهاجم يلوّث بيانات التدريب حتى الموديل يتعلّم غلط.

يعني نفس الذكاء اللي يحمي، يصير هدف. وهذا من أهم اتجاهات البحث بالمجال.

---

### القسم 5 — 11. Mathematical Reliability and Resilience Modeling

#### ① النص الأصلي

> 11.1 Availability
>
> Let IDS availability be A_ids and IPS availability A_ips. If deployed in tandem, the effective availability is the product of the two.
>
> 11.2 Expected loss model
>
> Let probability of attack P_a, probability of detection P_d, prevention success P_p, and impact I. The expected loss quantifies economic exposure under IDS/IPS protection.

$$A_{eff} = A_{ids} \cdot A_{ips}$$

$$EL = P_a(1 - P_d P_p) I$$

#### ② الترجمة

> «11.1 التوافرية (Availability)
>
> خلّينا توافرية الـ IDS هي A_ids وتوافرية الـ IPS هي A_ips. وإذا نُشرا مع بعض، فالتوافرية الفعّالة هي حاصل ضربهما.
>
> 11.2 موديل الخسارة المتوقعة (Expected loss)
>
> خلّينا احتمال الهجوم P_a، واحتمال الكشف P_d، ونجاح المنع P_p، والتأثير I. الخسارة المتوقعة تكمّم التعرض الاقتصادي تحت حماية الـ IDS/IPS.»

#### ③ الشرح الفهمي

هذا القسم يعطينا موديلين: واحد للـ reliability (التوافرية) وواحد للـ economic exposure (الخسارة المتوقعة).

**1) التوافرية (Availability):** لأن الـ IDS والـ IPS مركّبين بالـ series (إذا واحد وقف، السلسلة كلها تتأثر)، فالتوافرية الفعّالة هي حاصل ضربهم. يعني لو الاثنين 99% ← النتيجة 98% تقريباً، لأن الأعطال تتراكم.

$$A_{eff} = A_{ids} \cdot A_{ips}$$

| الرمز | المعنى |
|---|---|
| $A_{eff}$ | التوافرية الفعّالة للنظام كله |
| $A_{ids}$ | توافرية الـ IDS |
| $A_{ips}$ | توافرية الـ IPS |

**2) الخسارة المتوقعة (Expected loss):** تقيس التعرض الاقتصادي. الفكرة: الخسارة تحصل بس إذا صار هجوم **و** فشل الكشف/المنع. فاحتمال "نجاح الهجوم" = $1 - P_d P_p$، ونضربه بـ احتمال الهجوم $P_a$ وبالتأثير $I$.

$$EL = P_a(1 - P_d P_p) I$$

| الرمز | المعنى |
|---|---|
| $EL$ | الخسارة المتوقعة (expected loss) |
| $P_a$ | احتمال وقوع الهجوم |
| $P_d$ | احتمال كشف الهجوم (detection) |
| $P_p$ | احتمال نجاح المنع (prevention success) |
| $I$ | حجم التأثير (impact) إذا نجح الهجوم |
| $P_d P_p$ | الاحتمال المركّب إنه الهجوم ينكشف **و** ينمنع |

نقطة مهمة: لاحظ إن $P_d P_p$ هي "الحماية الفعّالة". كل ما زادت، كل ما قلّت الخسارة المتوقعة. وإذا $P_d P_p = 1$ (حماية كاملة) ← الخسارة = 0. وهذا يوضّح ليش نستثمر بالكشف والمنع سوا، مو بس الكشف.
