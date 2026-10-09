### القسم 1 — 1. Introduction

#### ① النص الأصلي

> The growth of digital infrastructure has expanded the attack surface of information systems, letting adversaries exploit vulnerabilities at unprecedented scales. As networks grow in size and complexity, perimeter defenses such as firewalls and VPNs alone prove insufficient — attackers bypass static defenses using polymorphic malware, encrypted payloads, and zero-day vulnerabilities. To close these gaps, Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) emerged as complementary mechanisms providing active visibility and control inside enterprise environments.
>
> An IDS monitors traffic and system activity for signs of compromise, issuing alerts upon detection. An IPS extends this paradigm by not only detecting malicious activity but also taking automated actions to block, quarantine, or modify traffic. Together they provide a critical control layer for detecting advanced persistent threats, insider misuse, and anomalies that bypass perimeter defenses.
>
> This chapter presents an advanced treatment of IDS and IPS — their architectures, algorithms, and the mathematical models that underpin performance evaluation — emphasizing their relevance within modern cybersecurity ecosystems, especially against encrypted traffic, distributed architectures, and adversarial evasion.

#### ② الترجمة

> «نموّ البنية التحتية الرقمية وسّع سطح الهجوم للأنظمة المعلوماتية، مما مكّن الخصوم من استغلال الثغرات على نطاقات غير مسبوقة. ومع نموّ الشبكات حجمًا وتعقيدًا، تبيّن أن الدفاعات المحيطية وحدها — كالجدران النارية و VPNs — غير كافية؛ إذ يتجاوز المهاجمون الدفاعات الساكنة بالبرمجيات الخبيثة متعدّدة الأشكال (polymorphic malware)، والحمولات المشفّرة، وثغرات اليوم صفر (zero-day). لسدّ هذه الفجوات، ظهرت أنظمة كشف التسلل (IDS) وأنظمة منع التسلل (IPS) كآليات مكمّلة توفّر رؤيةً وتحكّمًا نشطًا داخل بيئات المؤسسة.
>
> الـ IDS يراقب حركة المرور ونشاط النظام بحثًا عن مؤشرات الاختراق، ويصدر تنبيهات عند الكشف. والـ IPS يوسّع هذا النموذج بأنه لا يكتشف النشاط الخبيث فقط، بل يتّخذ إجراءات آلية للحجب أو الحجر أو تعديل حركة المرور. ومعًا يشكّلان طبقة تحكّم حرجة لكشف التهديدات المستمرة المتقدمة (APT)، وإساءة الاستخدام الداخلية، والشذوذات التي تتجاوز الدفاعات المحيطية.
>
> يعرض هذا الفصل معالجة متقدّمة للـ IDS والـ IPS — معمارياتهما وخوارزمياتهما والنماذج الرياضية التي تسند تقييم أدائهما — مع التأكيد على أهميتهما داخل المنظومات السيبرانية الحديثة، خصوصًا في مواجهة حركة المرور المشفّرة والمعماريات الموزّعة والتهرّب العدائي (adversarial evasion).»

#### ③ الشرح الفهمي

الفكرة الأساسية: كل ما تكبر الشبكة وتتعقّد، كل ما يكبر سطح الهجوم. الجدار الناري (firewall) والـ VPN يحمون الحدود (perimeter)، بس هذي وحدها ما عاد تكفي، لأن المهاجم صار يتجاوزها بـ:

- **polymorphic malware** — برمجية خبيثة تغيّر شكلها لتتفادى التوقيعات.
- **encrypted payloads** — حمولات مشفّرة تخفي المحتوى.
- **zero-day** — ثغرات ما عندها توقيع معروف بعد.

لهذا طلع الـ IDS والـ IPS — طبقة داخلية تعطي **رؤية (visibility)** و**تحكّم (control)** جوّة المؤسسة، مو بس على الحدود.

الفرق الجوهري بينهم:

| النظام | الوظيفة | الإجراء |
|---|---|---|
| IDS | يراقب ويكتشف | يصدر تنبيه (alert) فقط |
| IPS | يراقب ويكتشف ويتصرّف | يحجب / يحجر / يعدّل تلقائيًا |

يعني الـ IPS = IDS + قدرة ردّ فعل آلية. والاثنان معًا يكشفون الـ APT والإساءة الداخلية (insider misuse) والشذوذات اللي تعدّي الـ firewall.

نقطة مهمة: كلمة "advanced treatment" بالفصل تعني إنه ما يكتفي بالوصف — يبيّن المعماريات والخوارزميات و**النماذج الرياضية** لتقييم الأداء (وهذا اللي راح يجي بالأقسام 4-6).

---

### القسم 2 — 2. Historical and Conceptual Foundations

#### ① النص الأصلي

> **2.1 Evolution**
>
> - **First-generation IDS (1980s–1990s):** Focused on signature-based detection. Systems like Dorothy Denning's anomaly-based IDS model laid the conceptual foundation.
> - **Second-generation IDS (2000s):** Introduced anomaly-based detection, integrating statistical learning and early machine learning techniques.
> - **Contemporary IDS/IPS:** Employ hybrid approaches, distributed deployment (host-based and network-based), and integration with Security Information and Event Management (SIEM) systems.
>
> **2.2 Position in layered defense**
>
> IDS and IPS occupy a middle layer between perimeter defenses (firewalls, VPNs) and endpoint protections (anti-malware, EDR). They serve as visibility nodes, ensuring that malicious activities not filtered at the edge are detected and mitigated internally.

#### ② الترجمة

> «**2.1 التطوّر**
>
> - **الجيل الأول من الـ IDS (الثمانينيات–التسعينيات):** ركّز على الكشف بالتوقيعات (signature-based). أنظمة مثل نموذج الكشف بالشذوذ (anomaly-based) لدوروثي ديننغ أرست الأساس المفاهيمي.
> - **الجيل الثاني من الـ IDS (الألفينيات):** أدخل الكشف بالشذوذ، ودمج التعلّم الإحصائي وتقنيات التعلّم الآلي المبكرة.
> - **الـ IDS/IPS المعاصر:** يستخدم مقاربات هجينة، ونشرًا موزّعًا (قائم على المضيف وعلى الشبكة)، وتكاملًا مع أنظمة إدارة المعلومات والأحداث الأمنية (SIEM).
>
> **2.2 الموقع ضمن الدفاع الطبقي**
>
> الـ IDS والـ IPS يحتلّان طبقة وسطى بين الدفاعات المحيطية (الجدران النارية، VPNs) وحمايات نقاط النهاية (مضاد البرمجيات الخبيثة، EDR). يعملان كعُقد رؤية، تضمن كشف الأنشطة الخبيثة التي لم تُفلتر عند الحدود وتخفيفها داخليًا.»

#### ③ الشرح الفهمي

الموضوع هذا تاريخي بس مهم، لأنه يبيّن إن الـ IDS تطوّر بثلاث مراحل:

| الجيل | الفترة | الميزة |
|---|---|---|
| الأول | 1980s–1990s | الكشف بالتوقيعات (signature-based) + أساس نظري من Denning |
| الثاني | 2000s | الكشف بالشذوذ (anomaly-based) + تعلّم إحصائي و ML مبكّر |
| المعاصر | اليوم | هجين + نشر موزّع + تكامل مع SIEM |

ملاحظة أمانة: بالنص الأصلي في تناقض بسيط — يقول الجيل الأول كان signature-based، بس بنفس الجملة يقول نموذج Denning الـ anomaly-based "أرسى الأساس". المعنى: الجيل الأول اعتمد التوقيعات عمليًا، لكن نموذج Denning الشاذ قدّم الأساس النظري للكشف بالشذوذ اللي انفجر بالجيل الثاني.

بالنسبة للموقع الطبقي (2.2)، الـ IDS/IPS **طبقة وسطى** — يعني مو على الحدود (edge) ومو عند نقطة النهاية (endpoint)، بل بالنص:

| الطبقة | أمثلة |
|---|---|
| المحيطية (perimeter) | firewall، VPN |
| **الوسطى ← IDS/IPS** | رؤية داخلية وتخفيف |
| نقطة النهاية (endpoint) | anti-malware، EDR |

دورهما "visibility nodes": يكشفون أي شي خبيث عدّى الـ firewall وما انمسك عند الحد.

---

### القسم 3 — 3. IDS/IPS Architectures

#### ① النص الأصلي

> **3.1 Host-based IDS (HIDS)**
>
> Monitors events within a single host. It inspects system calls, file integrity, and application logs. HIDS provides granularity but lacks visibility across networks.
>
> **3.2 Network-based IDS (NIDS)**
>
> Deployed at strategic network points, monitoring traffic flow across segments. NIDS can analyze packet headers and payloads, but faces challenges with encrypted traffic.
>
> **3.3 Hybrid IDS**
>
> Combines host- and network-level monitoring, integrating log analysis, anomaly detection, and behavior monitoring.
>
> **3.4 IPS Deployment Modes**
>
> - **Inline IPS:** Positioned directly in the traffic path, capable of blocking traffic in real-time.
> - **Out-of-band IDS:** Only alerts administrators, leaving response actions to human operators.

#### ② الترجمة

> «**3.1 نظام كشف التسلل القائم على المضيف (HIDS)**
>
> يراقب الأحداث داخل مضيف واحد. يفحص استدعاءات النظام (system calls)، وسلامة الملفات (file integrity)، وسجلات التطبيقات. يوفّر الـ HIDS دقّة تفصيلية (granularity) لكن يفتقر إلى الرؤية عبر الشبكات.
>
> **3.2 نظام كشف التسلل القائم على الشبكة (NIDS)**
>
> يُنشَر عند نقاط شبكية استراتيجية، ويراقب تدفّق حركة المرور عبر المقاطع. يستطيع الـ NIDS تحليل رؤوس الحزم (packet headers) والحمولات (payloads)، لكنه يواجه تحديات مع حركة المرور المشفّرة.
>
> **3.3 نظام كشف التسلل الهجين (Hybrid IDS)**
>
> يجمع المراقبة على مستوى المضيف والشبكة معًا، ويدمج تحليل السجلات وكشف الشذوذ ومراقبة السلوك.
>
> **3.4 أنماط نشر الـ IPS**
>
> - **الـ IPS المضمّن (Inline):** يوضع مباشرة في مسار حركة المرور، وقادر على الحجب في الزمن الحقيقي.
> - **الـ IDS خارج المسار (Out-of-band):** ينبّه المسؤولين فقط، تاركًا إجراءات الاستجابة للمشغّلين البشريين.»

#### ③ الشرح الفهمي

المعماريات تنقسم حسب "وين" يراقب النظام:

| المعمارية | نطاق المراقبة | يشوف شنو | الضعف |
|---|---|---|---|
| HIDS | مضيف واحد | system calls، ملفات، سجلات | ما يشوف الشبكة |
| NIDS | الشبكة/المقاطع | packet headers + payloads | يضيع مع التشفير |
| Hybrid | الاثنين معًا | سجلات + شذوذ + سلوك | أعقد وأثقل |

**HIDS** يعطيك تفصيل عميق (granularity) داخل الجهاز — يعرف إن ملف تغيّر أو process غريب اشتغل. بس ما يعرف شنو يصير بالأجهزة الثانية.

**NIDS** ينصب عند نقاط استراتيجية بالشبكة (spans، TAPs) ويحلّل الحزم. مشكلته الأساسية: إذا الترافيك مشفّر (TLS)، الـ payload يصير غير مقروء.

**Hybrid** يدمج الاثنين — هذا اللي يستخدم اليوم غالبًا.

أما أنماط النشر (3.4)، الفرق بينهم هو **موقع الجهاز بالنسبة للمسار**:

| النمط | الموقع | القدرة |
|---|---|---|
| Inline IPS | داخل مسار الترافيك | يحجب فورًا (real-time block) |
| Out-of-band IDS | خارج المسار (نسخة/مرآة) | ينبّه فقط، والبشري يقرّر |

نقطة مهمة: Inline IPS عنده خطر — إذا الجهاز نفسه وقع، ممكن يقطع الشبكة كلها. Out-of-band أأمن بس ما عنده رد فعل آلي.

---

### القسم 4 — 4. Detection Techniques

#### ① النص الأصلي

> **4.1 Signature-based detection**
>
> Relies on pattern matching against a database of known threats. Efficient but blind to zero-day attacks.
>
> Mathematical formulation: Let $M = \{m_1, m_2, \cdots, m_n\}$ be observed traffic sequences and $S = \{s_1, s_2, \cdots, s_k\}$ be signature database patterns. The detection function is defined below. Here $D(m_i) = 1$ denotes detection of malicious activity.
>
> **4.2 Anomaly-based detection**
>
> Defines a model of "normal" behavior and flags deviations as anomalies. Statistical model shown below, where $x$ is an observed metric, $\mu$ the mean, $\sigma$ the standard deviation, and $k$ a sensitivity constant.
>
> **4.3 Machine learning–based IDS**
>
> Incorporates supervised and unsupervised algorithms (decision trees, SVMs, neural networks, clustering) to classify or detect anomalies. Given a feature vector $\mathbf{x} \in \mathbb{R}^d$, a classifier $f$ maps traffic to class labels. The decision boundary is optimized using a loss function $L(f(\mathbf{x}), \mathcal{Y})$, where $\mathcal{Y}$ is ground truth.

#### ② الترجمة

> «**4.1 الكشف القائم على التوقيعات (signature-based)**
>
> يعتمد على مطابقة الأنماط (pattern matching) مع قاعدة بيانات للتهديدات المعروفة. فعّال لكنه أعمى تجاه هجمات اليوم صفر (zero-day).
>
> الصياغة الرياضية: لتكن $M = \{m_1, m_2, \cdots, m_n\}$ متتاليات حركة المرور المرصودة، و $S = \{s_1, s_2, \cdots, s_k\}$ أنماط قاعدة بيانات التوقيعات. تُعرَّف دالة الكشف أدناه. هنا $D(m_i) = 1$ يدلّ على كشف نشاط خبيث.
>
> **4.2 الكشف القائم على الشذوذ (anomaly-based)**
>
> يعرّف نموذجًا للسلوك "الطبيعي" ويرصد الانحرافات كشذوذ. النموذج الإحصائي موضّح أدناه، حيث $x$ قياس مرصود، و $\mu$ المتوسط، و $\sigma$ الانحراف المعياري، و $k$ ثابت حسّاسية.
>
> **4.3 نظام كشف التسلل القائم على التعلّم الآلي (ML-based)**
>
> يضمّ خوارزميات خاضعة للإشراف وغير خاضعة له (أشجار القرار، SVMs، الشبكات العصبية، التجميع clustering) لتصنيف أو كشف الشذوذ. بمعطى متجه السمات $\mathbf{x} \in \mathbb{R}^d$، يربط المصنّف $f$ حركة المرور بتسميات الفئات. ويُحسَّن حدّ القرار (decision boundary) باستخدام دالة خسارة $L(f(\mathbf{x}), \mathcal{Y})$، حيث $\mathcal{Y}$ هي الحقيقة الأرضية (ground truth).»

$$D(m_i) = \begin{cases} 1 & \text{if } \exists\, s_j \in S : \text{match}(m_i, s_j) = \text{true} \\[4pt] 0 & \text{otherwise} \end{cases}$$

| الرمز | المعنى |
|---|---|
| $m_i$ | متتالية حركة مرور مرصودة |
| $s_j$ | نمط توقيع من قاعدة البيانات $S$ |
| $\text{match}(m_i, s_j)$ | دالة مطابقة الأنماط |
| $D(m_i)$ | $1$ = كُشف نشاط خبيث، $0$ = لا |

$$A(x) = \begin{cases} 1 & \text{if } |x - \mu| > k\sigma \\[4pt] 0 & \text{otherwise} \end{cases}$$

| الرمز | المعنى |
|---|---|
| $x$ | القياس المرصود |
| $\mu$ | المتوسط (mean) للسلوك الطبيعي |
| $\sigma$ | الانحراف المعياري (standard deviation) |
| $k$ | ثابت الحسّاسية (sensitivity constant) |
| $A(x)$ | $1$ = شاذ (anomaly)، $0$ = طبيعي |

$$f: \mathbb{R}^d \rightarrow \{\text{benign}, \text{malicious}\}, \qquad \min_f \; \mathbb{E}\big[\, L(f(\mathbf{x}), \mathcal{Y}) \,\big]$$

| الرمز | المعنى |
|---|---|
| $\mathbf{x} \in \mathbb{R}^d$ | متجه السمات (feature vector) بُعده $d$ |
| $f$ | المصنّف (classifier) |
| $\{\text{benign}, \text{malicious}\}$ | فضاء التسميات (labels) |
| $L$ | دالة الخسارة (loss function) |
| $\mathcal{Y}$ | الحقيقة الأرضية (ground truth) |

#### ③ الشرح الفهمي

عندنا ثلاث عائلات للكشف، كل واحدة تفكّر بطريقة مختلفة:

| التقنية | المنطق | القوة | الضعف |
|---|---|---|---|
| Signature-based | يطابق مع توقيعات معروفة | سريع ودقيق على المعروف | أعمى على zero-day |
| Anomaly-based | يعرّف "الطبيعي" ويرصد الانحراف | يمسك الجديد | false positives عالية |
| ML-based | يتعلّم من البيانات ويصنّف | يتكيّف ويتطوّر | يحتاج بيانات + هجمات adversarial |

**4.1 التوقيعات:** تخيّل عندك قائمة بصمات (signatures) لكل هجوم معروف. الـ IDS يقارن كل متتالية ترافيك $m_i$ مع كل توقيع $s_j$؛ إذا طابق واحد، يرجع $D(m_i)=1$ (كشف). سريع بس إذا الهجوم جديد ما عنده توقيع، يمر بسلام.

**4.2 الشذوذ:** بدل التوقيعات، تتعلم شنو "طبيعي". إذا القياس $x$ بعيد عن المتوسط $\mu$ بأكثر من $k$ انحرافات معيارية ($k\sigma$)، نعتبره شاذ. المشكلة: أي شي غير مألوف (بس بريء) يطلع alert — false positives. و $k$ يتحكّم بالحساسية: $k$ صغير ← حساس أكثر (تنبيهات أكثر)، $k$ كبير ← متسامح.

**4.3 التعلّم الآلي:** نحوّل الترافيك لمتجه سمات $\mathbf{x}$ (بُعده $d$)، والمصنّف $f$ يربطه بتسمية: benign أو malicious. التدريب يصير بتقليل دالة الخسارة $L$ (يعني كل ما نتوقّع غلط، الخسارة تكبر، والنموذج يعدّل نفسه). يشمل خوارزميات supervised (decision trees, SVM, neural nets) و unsupervised (clustering).

---

### القسم 5 — 5. Prevention Mechanisms in IPS

#### ① النص الأصلي

> Unlike IDS, which only detects and alerts, IPS systems act upon detections. Actions include:
>
> - **Packet dropping:** Malicious packets are removed.
> - **TCP reset:** Connections are forcefully terminated.
> - **Traffic rate-limiting:** Mitigates flooding or DoS.
> - **Quarantine:** Segments hosts until remediation.
>
> IPS introduces a performance-security trade-off, as false positives directly impact availability.
>
> Mathematical reliability model — define probabilities:
>
> - $P_{TP}$: True positive rate (detection of actual attack).
> - $P_{FP}$: False positive rate (benign traffic flagged).
> - $P_{FN}$: False negative rate (missed attack).
>
> The security effectiveness index (SEI) is defined below. A high SEI reflects a system that balances strong detection with minimal disruption.

#### ② الترجمة

> «بخلاف الـ IDS الذي يكتشف وينبّه فقط، فإن أنظمة الـ IPS تتصرّف بناءً على الكشوفات. الإجراءات تشمل:
>
> - **إسقاط الحزم (Packet dropping):** تُزال الحزم الخبيثة.
> - **إعادة ضبط TCP (TCP reset):** تُنهى الاتصالات قسرًا.
> - **تحديد معدّل المرور (Traffic rate-limiting):** يخفّف الفيض (flooding) أو هجمات DoS.
> - **الحجر (Quarantine):** يعزل المضيفين حتى المعالجة (remediation).
>
> يُدخل الـ IPS مقايضة بين الأداء والأمن (performance-security trade-off)، إذ تؤثّر الإيجابيات الكاذبة مباشرة على التوفّر (availability).
>
> نموذج موثوقية رياضي — عرّف الاحتمالات:
>
> - $P_{TP}$: معدّل الإيجابيات الصحيحة (كشف هجوم فعلي).
> - $P_{FP}$: معدّل الإيجابيات الكاذبة (ترافيك بريء صُنِّف هجومًا).
> - $P_{FN}$: معدّل السلبيات الكاذبة (هجوم لم يُكتشف).
>
> يُعرَّف مؤشّر الفعالية الأمنية (SEI) أدناه. القيمة العالية للـ SEI تعكس نظامًا يوازن بين كشف قوي وأقلّ إزعاج ممكن.»

$$\text{SEI} = \frac{P_{TP}}{P_{TP} + P_{FN} + P_{FP}}$$

| الرمز | المعنى |
|---|---|
| $\text{SEI}$ | مؤشّر الفعالية الأمنية (Security Effectiveness Index) |
| $P_{TP}$ | معدّل الإيجابيات الصحيحة (كشف الهجوم الحقيقي) |
| $P_{FN}$ | معدّل السلبيات الكاذبة (هجوم فائت) |
| $P_{FP}$ | معدّل الإيجابيات الكاذبة (ترافيك بريء مُعلَّم) |

#### ③ الشرح الفهمي

الفرق الجوهري: الـ IDS "يشوف وينبّه"، الـ IPS "يشوف ويتصرّف". إجراءاته الأربعة:

| الإجراء | الوظيفة | يمنع |
|---|---|---|
| Packet dropping | إسقاط الحزم الخبيثة | تسلّل الحمولة |
| TCP reset | قطع الاتصال قسرًا | جلسة مهاجم |
| Traffic rate-limiting | تحديد المعدّل | flooding / DoS |
| Quarantine | عزل المضيف | انتشار جانبي |

بس هنا تجي المقايضة الخطيرة: **performance-security trade-off**. لأن الـ IPS يتصرّف آليًا، أي **false positive** (يظن ترافيك بريء إنه هجوم) راح يحجب ترافيك شرعي ← يضرّ **availability**. يعني IPS قوي بالكشف بس عدواني زيادة ممكن يوقّف شغلك.

مؤشّر SEI يقيس هذي الموازنة:

$$\text{SEI} = \frac{P_{TP}}{P_{TP} + P_{FN} + P_{FP}}$$

المعنى من المقام: البسط هو الكشف الصحيح ($P_{TP}$)، والمقام يجمع الكشف الصحيح + الهجمات الفائتة ($P_{FN}$) + الإنذارات الكاذبة ($P_{FP}$). يعني:

- $P_{TP}$ كبير ← SEI يقترب من 1 ← نظام ممتاز.
- $P_{FN}$ كبير ← يفوّت هجمات ← SEI ينزل.
- $P_{FP}$ كبير ← إنذارات كاذبة وإزعاج ← SEI ينزل.

النظام المثالي يوازن: كشف قوي ($P_{TP}$ عالي) مع أقل إزعاج ($P_{FP}$ واطي). لاحظ إن القيمة القصوى للـ SEI هي 1 (لما $P_{FN}=P_{FP}=0$).

---

### القسم 6 — 6. Mathematical Models of IDS/IPS Performance

#### ① النص الأصلي

> **6.1 Risk reduction model**
>
> If the initial risk of compromise is $R_0$ and IDS/IPS efficacy is $e$, residual risk becomes the expression below. Efficacy depends on attack detection probability and prevention reliability.
>
> **6.2 ROC analysis**
>
> Receiver Operating Characteristic (ROC) curves characterize IDS/IPS classifiers.
>
> - **True Positive Rate (TPR):** as defined below.
> - **False Positive Rate (FPR):** as defined below.
>
> The Area Under the Curve (AUC) quantifies detection performance, with a higher AUC reflecting stronger classifiers.
>
> **6.3 Bayesian attack probability model**
>
> Let $A$ denote attack presence and $D$ denote detection alert. Using Bayes' theorem, the posterior attack probability given an IDS alert is given below. This provides probabilistic assurance for decision-making.

#### ② الترجمة

> «**6.1 نموذج تقليل المخاطر**
>
> إذا كان الخطر الابتدائي للاختراق $R_0$ وفعالية الـ IDS/IPS هي $e$، فإن الخطر المتبقّي يصبح كما في التعبير أدناه. وتعتمد الفعالية على احتمال كشف الهجوم وموثوقية المنع.
>
> **6.2 تحليل ROC**
>
> منحنيات خاصية تشغيل المستقبِل (ROC) تميّز مصنّفات الـ IDS/IPS.
>
> - **معدّل الإيجابيات الصحيحة (TPR):** كما هو معرّف أدناه.
> - **معدّل الإيجابيات الكاذبة (FPR):** كما هو معرّف أدناه.
>
> المساحة تحت المنحنى (AUC) تقيس أداء الكشف، حيث تعكس AUC الأعلى مصنّفات أقوى.
>
> **6.3 نموذج الاحتمال البايزي للهجوم**
>
> لتكن $A$ تدلّ على وجود هجوم، و $D$ تدلّ على تنبيه الكشف. باستخدام مبرهنة بايز، يُعطى الاحتمال البعدي (posterior) للهجوم بمعطى تنبيه IDS كما أدناه. وهذا يوفّر ضمانًا احتماليًا لاتخاذ القرار.»

$$R_{res} = R_0 (1 - e)$$

| الرمز | المعنى |
|---|---|
| $R_{res}$ | الخطر المتبقّي (residual risk) |
| $R_0$ | الخطر الابتدائي للاختراق |
| $e$ | فعالية الـ IDS/IPS (efficacy) |

$$\text{TPR} = \frac{TP}{TP + FN}, \qquad \text{FPR} = \frac{FP}{FP + TN}$$

| الرمز | المعنى |
|---|---|
| $\text{TPR}$ | معدّل الإيجابيات الصحيحة (حساسية) |
| $\text{FPR}$ | معدّل الإيجابيات الكاذبة |
| $TP$ | إيجابي صحيح (هجوم كُشف) |
| $FN$ | سلبي كاذب (هجوم فائت) |
| $FP$ | إيجابي كاذب (بريء مُعلَّم) |
| $TN$ | سلبي صحيح (بريء سليم) |

$$P(A \mid D) = \frac{P(D \mid A)\,P(A)}{P(D \mid A)\,P(A) + P(D \mid \neg A)\,P(\neg A)}$$

| الرمز | المعنى |
|---|---|
| $P(A \mid D)$ | الاحتمال البعدي لوجود هجوم بمعطى تنبيه |
| $P(D \mid A)$ | احتمال إصدار تنبيه عند وجود هجوم فعلًا (≈ TPR) |
| $P(A)$ | الاحتمال القبلي (prior) لوجود هجوم |
| $P(D \mid \neg A)$ | احتمال تنبيه كاذب عند عدم وجود هجوم (≈ FPR) |
| $P(\neg A)$ | الاحتمال القبلي لعدم وجود هجوم |

#### ③ الشرح الفهمي

هذا القسم يعطينا ثلاث أدوات رياضية لتقييم الـ IDS/IPS:

**6.1 تقليل المخاطر** — أبسط نموذج. عندك خطر ابتدائي $R_0$، والنظام يخفّضه بفعالية $e$ (بين 0 و 1). الخطر المتبقّي:

$$R_{res} = R_0 (1 - e)$$

مثال: لو $R_0 = 100$ و $e = 0.8$، يبقى $R_{res} = 100 \times 0.2 = 20$. يعني النظام شال 80% من الخطر. الفعالية $e$ نفسها تعتمد على احتمال الكشف وموثوقية المنع.

**6.2 تحليل ROC** — يقيس المصنّف بأربع نتائج ممكنة:

| | هجوم فعلي | لا هجوم |
|---|---|---|
| **تنبيه** | $TP$ | $FP$ |
| **لا تنبيه** | $FN$ | $TN$ |

ومنها:
- $\text{TPR} = TP/(TP+FN)$ ← كم نسبة الهجمات اللي كشفناها (كل ما أعلى أحسن).
- $\text{FPR} = FP/(FP+TN)$ ← كم نسبة البريء اللي أزعجناه (كل ما أوطى أحسن).

منحنى ROC يرسم TPR مقابل FPR، و**AUC** (المساحة تحت المنحنى) تختصر الأداء برقم واحد: AUC قريب من 1 ← مصنّف ممتاز، AUC = 0.5 ← عشوائي مثل رمي العملة.

**6.3 نموذج بايز** — يجيب سؤال ذكي: "طلع alert، شكد احتمال إنه فعلاً هجوم؟" هذا هو الاحتمال البعدي $P(A \mid D)$:

$$P(A \mid D) = \frac{P(D \mid A)\,P(A)}{P(D \mid A)\,P(A) + P(D \mid \neg A)\,P(\neg A)}$$

الفكرة المهمة (وهي مفاجئة): حتى لو الـ IDS دقيق، إذا الهجمات نادرة ($P(A)$ صغير جدًا)، معظم التنبيهات تطلع **كاذبة**. لأن $P(D \mid \neg A)$ (احتمال تنبيه كاذب) يضرب بعدد الأحداث البريئة الكبير. لهذا false positives مشكلة جوهرية بنماذج IDS الواقعية.

---

![IDS/IPS — المعماريات والتقنيات والمقاييس|720](../06_Diagrams_&_Mindmaps/cy_w5_ids_ips.svg)
