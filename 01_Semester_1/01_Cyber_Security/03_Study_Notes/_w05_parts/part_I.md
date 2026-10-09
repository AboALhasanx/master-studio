### القسم 1 — 1. Introduction

#### ① النص الأصلي

> The accelerating complexity of modern digital ecosystems has made network security one of the most critical pillars of enterprise defense. Perimeter-based protections once sufficed, but the erosion of the traditional network boundary — driven by cloud adoption, distributed workforces, and the proliferation of Internet of Things (IoT) devices — demands a rethinking of traditional models. Within this context, network segmentation and defense in depth emerge as foundational strategies that strengthen resilience and align cybersecurity practices with evolving threat landscapes.
>
> Network segmentation divides networks into smaller, isolated zones, limiting the ability of adversaries to move laterally once an initial breach occurs. Defense in depth complements segmentation by layering multiple, overlapping security controls that collectively reduce the probability of a successful attack. Together, these strategies embody the principle of layered resilience, ensuring that no single point of failure can compromise the integrity of the system.
>
> This chapter analyzes network segmentation and defense in depth, emphasizing their theoretical underpinnings, practical deployment, and emerging trends such as micro segmentation, Zero Trust architectures, and AI-driven adaptive defenses. It incorporates mathematical models for quantifying risk reduction, residual vulnerabilities, and security reliability, keeping the discussion conceptually robust and empirically grounded.

#### ② الترجمة

> «التعقيد المتسارع في النظم الرقمية الحديثة جعل أمن الشبكات واحدًا من أهم أركان الدفاع المؤسسي. كانت الحمايات القائمة على المحيط (perimeter) كافية في السابق، لكن تآكل الحدود التقليدية للشبكة — بفعل تبنّي الحوسبة السحابية والقوى العاملة الموزّعة وانتشار أجهزة إنترنت الأشياء (IoT) — يستلزم إعادة التفكير في النماذج التقليدية. وفي هذا السياق، يبرز تقسيم الشبكة (network segmentation) والدفاع في العمق (defense in depth) كاستراتيجيتين تأسيسيتين تعزّزان المرونة وتوائمان ممارسات الأمن السيبراني مع مشهد التهديدات المتطوّر.
>
> تقسيم الشبكة يقسّم الشبكات إلى مناطق أصغر معزولة، مما يحدّ من قدرة الخصوم على الحركة الجانبية بعد حدوث اختراق أولي. والدفاع في العمق يكمّل التقسيم بطبقات متعددة متداخلة من الضوابط الأمنية التي تخفّض مجتمعةً احتمال نجاح الهجوم. ومعًا، يجسّدان مبدأ المرونة الطبقية، بما يضمن ألّا تؤدي أي نقطة فشل واحدة إلى المساس بسلامة النظام.
>
> يحلّل هذا الفصل تقسيم الشبكة والدفاع في العمق، مع التركيز على أسسهما النظرية وتطبيقهما العملي والاتجاهات الناشئة مثل التقسيم الدقيق (micro segmentation) ومعماريات Zero Trust والدفاعات التكيفية المدفوعة بالذكاء الاصطناعي. ويتضمّن نماذج رياضية لقياس خفض المخاطر والثغرات المتبقية وموثوقية الأمن، بما يبقي الطرح متينًا مفاهيميًا ومرتكزًا تجريبيًا.»

#### ③ الشرح الفهمي

الفكرة الأساسية إن الشبكة التقليدية اللي كان عندها "محيط" واحد (perimeter) ما عادت كافية. السحابة (cloud) والعمل عن بعد (remote work) وانتشار أجهزة IoT، كلها فتحت الشبكة ووزّعتها، فصار الخط الفاصل بين "داخل" و"خارج" مو واضح. لهذا نحتاج استراتيجيتين تأسيسيتين تشتغلان معًا:

| الاستراتيجية | شنو تسوي | الهدف |
|---|---|---|
| Network Segmentation | تقسّم الشبكة لمناطق (zones) معزولة بضوابط وفايرولات | تحدّ من الحركة الجانبية (lateral movement) بعد الاختراق |
| Defense in Depth | تحط طبقات متعددة من الضوابط فوق بعضها | لو طبقة فشلت، الطبقات الثانية تعوّض |

النقطة المهمة: هالثنتين مو بدائل لبعض، بل مكمّلات. Segmentation تضيّق مساحة الهجوم (attack surface) بعد ما يصير اختراق، و Defense in Depth تضمن إنه ما عندك نقطة فشل واحدة (single point of failure). اجتماعهم = layered resilience.

هذا الفصل راح يجمع بين:
- الأساس النظري والتطبيق العملي للتقسيم والدفاع الطبقي.
- الاتجاهات الحديثة: micro segmentation، و Zero Trust، والدفاعات المدفوعة بالـ AI.
- نماذج رياضية كمّية لقياس المخاطر وخفضها — يعني مو كلام نظري بس، بل أرقام.

---

### القسم 2 — 2. Conceptual Foundations of Network Segmentation

#### ① النص الأصلي

> Network segmentation is the practice of dividing a computer network into multiple segments or subnetworks, each isolated by access controls or firewalls. Its primary objectives are:
>
> - Containment of breaches: preventing an attacker who compromises one zone from accessing others.
> - Performance optimization: reducing congestion by limiting broadcast traffic.
> - Policy enforcement: applying granular controls to sensitive or regulated data flows.
>
> Segmentation can be logical (through VLANs or software-defined networking) or physical (separate hardware networks). The main types are:
>
> - VLAN-based segmentation: logical separation within switches to isolate broadcast domains.
> - Subnetting: splitting IP address ranges into smaller segments, controlling communication through routing policies.
> - Firewall segmentation: rules that limit access between segments.
> - Micro segmentation: granular segmentation at the workload or application level, increasingly important in virtualized and cloud-native infrastructures.
>
> Attackers frequently exploit flat networks to move laterally from low-value to high-value assets; by isolating critical resources, segmentation disrupts this progression. Formally, if an attacker compromises a node $v_i$ in a network graph $G = (V, E)$, the probability of reaching a target node $v_t$ without segmentation is the number of possible attack paths divided by $|E|$. Segmentation introduces cut-sets $C \subseteq E$ such that communication between zones requires crossing controlled gateways, which significantly reduces the probability of successful lateral movement.

$$P_{reach} = \frac{|P(v_i, v_t)|}{|E|} \qquad P_{reach}^{seg} = \frac{|P(v_i, v_t) \cap C|}{|E|}$$

| الرمز | المعنى |
|---|---|
| $P_{reach}$ | احتمال الوصول للهدف بدون تقسيم |
| $P_{reach}^{seg}$ | احتمال الوصول للهدف مع التقسيم |
| $v_i$ | العقدة المخترَقة (نقطة الدخول) |
| $v_t$ | العقدة الهدف |
| $G = (V, E)$ | مخطّط الشبكة: $V$ عقد، $E$ حواف |
| $P(v_i, v_t)$ | مجموعة مسارات الهجوم الممكنة من $v_i$ إلى $v_t$ |
| $C \subseteq E$ | مجموعة القطع (cut-set): حواف البوابات المتحكَّم بها |

#### ② الترجمة

> «تقسيم الشبكة هو ممارسة تقسيم شبكة الحاسوب إلى عدة قطاعات أو شبكات فرعية، كل منها معزول بضوابط وصول أو فايرولات. أهدافه الأساسية هي:
>
> - احتواء الاختراقات: منع المهاجم الذي يخترق منطقة واحدة من الوصول إلى غيرها.
> - تحسين الأداء: تقليل الازدحام بالحدّ من حركة البثّ (broadcast traffic).
> - فرض السياسات: تطبيق ضوابط دقيقة على تدفّقات البيانات الحسّاسة أو المنظَّمة.
>
> يمكن أن يكون التقسيم منطقيًا (عبر VLANs أو الشبكات المعرّفة برمجيًا) أو ماديًا (شبكات عتاد منفصلة). والأنواع الرئيسية هي:
>
> - التقسيم القائم على VLAN: فصل منطقي داخل السويتشات لعزل نطاقات البثّ.
> - التقسيم إلى شبكات فرعية (Subnetting): تقسيم نطاقات عناوين IP إلى قطع أصغر، والتحكّم في الاتصال عبر سياسات التوجيه.
> - تقسيم الفايرول: قواعد تحدّ من الوصول بين القطاعات.
> - التقسيم الدقيق (Micro segmentation): تقسيم دقيق على مستوى الحِمل أو التطبيق، ويزداد أهميته في البنى الافتراضية والسحابية.
>
> كثيرًا ما يستغل المهاجمون الشبكات المسطّحة (flat) للحركة الجانبية من أصول منخفضة القيمة إلى أصول عالية القيمة؛ وبعزل الموارد الحسّاسة، يعطّل التقسيم هذا التقدّم. وبشكل صريح، إذا اخترق المهاجم عقدة $v_i$ في مخطّط الشبكة $G = (V, E)$، فإن احتمال الوصول إلى عقدة هدف $v_t$ بدون تقسيم هو عدد مسارات الهجوم الممكنة مقسومًا على $|E|$. ويُدخِل التقسيم مجموعات قطع $C \subseteq E$ بحيث يتطلّب الاتصال بين المناطق عبور بوابات متحكَّم بها، مما يخفّض احتمال نجاح الحركة الجانبية تخفيضًا كبيرًا.»

#### ③ الشرح الفهمي

التقسيم يعني بدل شبكة واحدة كبيرة مفتوحة، تسوّي جُزر (zones) معزولة، والتنقّل بينها يمرّ عبر بوابات متحكَّم بها (gateways). ليش؟ لأن المهاجم اللي يدخل منطقة صغيرة، ما راح يكدر يقفز لكل الشبكة — تُحتوى المشكلة بمكانها.

الأنواع الأربعة:

| النوع | وين يشتغل | شلون يعزل |
|---|---|---|
| VLAN-based | داخل السويتش | يفصل نطاقات البثّ (broadcast domains) منطقيًا |
| Subnetting | طبقة IP / التوجيه | يقسّم نطاقات العناوين ويسيطر عبر routing policies |
| Firewall segmentation | بين القطاعات | قواعد allow/deny بين المناطق |
| Micro segmentation | مستوى الحِمل/التطبيق | سياسات دقيقة قائمة على الهوية (identity-based) |

الجزء الرياضي: تخيّل الشبكة كمخطّط (graph) $G=(V,E)$ — العقد $V$ هي الأجهزة، والحواف $E$ هي وصلات الاتصال. لو المهاجم دخل عند عقدة $v_i$، احتمال يوصّل للهدف $v_t$ يعتمد على عدد المسارات الممكنة بينهم نسبةً لكل الحواف. المعادلة أعلاه تحسب هالاحتمال:

- $P_{reach} = \dfrac{|P(v_i, v_t)|}{|E|}$ — بدون تقسيم، كل المسارات ممكنة.
- $P_{reach}^{seg} = \dfrac{|P(v_i, v_t) \cap C|}{|E|}$ — مع تقسيم، المسارات لازم تعبر البوابات المتحكَّم بها $C$ فقط.

الخلاصة: كل ما زادت البوابات المتحكَّم بها (cut-set $C$)، قلّت المسارات المتاحة للمهاجم، فنزل احتمال الحركة الجانبية. هذا جوهر الحماية اللي يقدّمها التقسيم.

---

### القسم 3 — 3. Defense in Depth: A Strategic Paradigm

#### ① النص الأصلي

> Defense in depth is a layered security approach designed to ensure that multiple controls exist at different levels — network, host, application, and user — so that if one fails, others compensate. The key layers are:
>
> - Perimeter layer: firewalls, VPNs, and proxies.
> - Detection layer: IDS/IPS and SIEM systems.
> - Application layer: secure coding and web application firewalls (WAF).
> - Endpoint layer: antivirus and endpoint detection and response (EDR).
> - User layer: policies, awareness, and multi-factor authentication.
>
> Mathematically, if each security control $i$ reduces the initial risk $R_0$ by a factor $r_i \in (0,1)$, the residual risk after $n$ layers is $R_0$ multiplied by the product of the terms $(1 - r_i)$. For example, with three layers reducing risk by 40%, 50%, and 30% respectively, the residual risk equals $R_0 \times (0.6 \times 0.5 \times 0.7) = 0.21 R_0$, which illustrates the compounding benefit of layered defenses.

$$R_{residual} = R_0 \times \prod_{i=1}^{n} (1 - r_i)$$

| الرمز | المعنى |
|---|---|
| $R_{residual}$ | المخاطر المتبقية بعد كل الطبقات |
| $R_0$ | المخاطر الابتدائية قبل أي ضابط |
| $n$ | عدد طبقات الدفاع |
| $r_i$ | معامل الخفض للضابط $i$، وقيمته في المدى $(0,1)$ |

#### ② الترجمة

> «الدفاع في العمق هو أسلوب أمني طبقي مصمَّم لضمان وجود ضوابط متعددة على مستويات مختلفة — الشبكة والمضيف والتطبيق والمستخدم — بحيث إذا فشل أحدها، يعوّضه غيره. والطبقات الرئيسية هي:
>
> - طبقة المحيط: الفايرولات و VPNs والبروكسيات.
> - طبقة الكشف: أنظمة IDS/IPS وأنظمة SIEM.
> - طبقة التطبيق: البرمجة الآمنة وجدران حماية تطبيقات الويب (WAF).
> - طبقة الأجهزة الطرفية: مضادات الفيروسات وأنظمة الكشف والاستجابة الطرفية (EDR).
> - طبقة المستخدم: السياسات والتوعية والمصادقة متعددة العوامل.
>
> رياضيًا، إذا خفّض كل ضابط أمني $i$ المخاطر الابتدائية $R_0$ بمعامل $r_i \in (0,1)$، فإن المخاطر المتبقية بعد $n$ طبقة تساوي $R_0$ مضروبة في حاصل ضرب الحدود $(1 - r_i)$. وعلى سبيل المثال، مع ثلاث طبقات تخفّض المخاطر بنسب 40% و50% و30% على التوالي، تكون المخاطر المتبقية $R_0 \times (0.6 \times 0.5 \times 0.7) = 0.21 R_0$، وهو ما يوضّح الفائدة المتراكمة للدفاعات الطبقية.»

#### ③ الشرح الفهمي

Defense in Depth يعني ما تعتمد على حماية واحدة. بدل ما تحط جدار واحد وخلاص، تحط طبقات: لو المهاجم عدّى الفايرول، يلكاه IDS؛ لو عدّاه، يلكاه WAF؛ لو وصل للجهاز، يلكاه EDR؛ ولو وصل للمستخدم، يلكاه MFA. كل طبقة تزيد الصعوبة.

الطبقات الخمس حسب المصدر:

| # | الطبقة | أمثلة على الضوابط |
|---|---|---|
| 1 | Perimeter | Firewalls, VPNs, Proxies |
| 2 | Detection | IDS/IPS, SIEM |
| 3 | Application | Secure coding, WAF |
| 4 | Endpoint | Antivirus, EDR |
| 5 | User | Policies, Awareness, MFA |

الرياضيات: كل طبقة تخفّض المخاطر بنسبة $r_i$، يعني تخلي المتبقي $(1 - r_i)$ من المخاطر. ولأن الطبقات مستقلة، المتبقي الكلي = حاصل ضربهم (منتج تراكمي). المعادلة أعلاه تعبّر عن هذا.

المثال المحسوب خطوة بخطوة:
- طبقة 1: تخفض 40% ← يتبقى 0.6.
- طبقة 2: تخفض 50% ← يتبقى 0.5.
- طبقة 3: تخفض 30% ← يتبقى 0.7.
- المتبقي الكلي = $0.6 \times 0.5 \times 0.7 = 0.21$.

يعني بعد ثلاث طبقات، المخاطر صارت 21% فقط من الأصلية. لاحظ إن الفائدة متراكمة (multiplicative) — مو جمع. هذا اللي يخلي الدفاع الطبقي قوي: كل طبقة إضافية تضرب المتبقي، فينزل بسرعة.

---

### القسم 4 — 4. Mathematical Models of Segmentation and Layered Security

#### ① النص الأصلي

> Let network assets be grouped into $m$ segments $S_1, S_2, \dots, S_m$. Each segment has a vulnerability score $V_i$ and a threat probability $P_i$, so the segment-specific risk is the product of the two. The aggregate network risk is the sum of the per-segment risks. If segmentation reduces inter-segment connectivity by a factor $\alpha \in [0,1]$, the effective risk becomes $\alpha$ times the aggregate risk, where $\alpha$ represents segmentation efficiency; for micro segmentation in virtualized systems, $\alpha$ approaches 0, significantly reducing aggregate risk.
>
> For attack paths, let the path consist of $n$ defense layers, each with a probability of failure $q_i$. The probability that an attack succeeds across all layers is the product of the $q_i$. If the average $q_i = 0.2$ across 5 layers, then $P_{success} = (0.2)^5 = 0.00032$, showing exponential risk reduction.

$$R_i = P_i \cdot V_i \qquad R_{net} = \sum_{i=1}^{m} R_i \qquad R_{eff} = \alpha \cdot R_{net}$$

$$P_{success} = \prod_{i=1}^{n} q_i$$

| الرمز | المعنى |
|---|---|
| $R_i$ | مخاطر القطاع $i$ المحدَّدة |
| $P_i$ | احتمال التهديد للقطاع $i$ |
| $V_i$ | درجة الثغرة (vulnerability score) للقطاع $i$ |
| $m$ | عدد القطاعات |
| $R_{net}$ | المخاطر الكلية للشبكة |
| $\alpha$ | معامل كفاءة التقسيم، وقيمته في المدى $[0,1]$ |
| $R_{eff}$ | المخاطر الفعلية بعد التقسيم |
| $P_{success}$ | احتمال نجاح الهجوم عبر كل الطبقات |
| $n$ | عدد طبقات الدفاع |
| $q_i$ | احتمال فشل الطبقة $i$ |

#### ② الترجمة

> «لنُجمّع أصول الشبكة في $m$ قطاع $S_1, S_2, \dots, S_m$. لكل قطاع درجة ثغرة $V_i$ واحتمال تهديد $P_i$، فتصبح مخاطر القطاع حاصل ضرب الاثنين. والمخاطر الكلية للشبكة هي مجموع مخاطر القطاعات. وإذا خفّض التقسيم الاتصال بين القطاعات بمعامل $\alpha \in [0,1]$، تصبح المخاطر الفعلية $\alpha$ مضروبًا في المخاطر الكلية، حيث يمثّل $\alpha$ كفاءة التقسيم؛ وفي التقسيم الدقيق داخل الأنظمة الافتراضية يقترب $\alpha$ من الصفر، فينخفض إجمالي المخاطر انخفاضًا كبيرًا.
>
> أما بالنسبة لمسارات الهجوم، فلنفترض أن المسار يتكوّن من $n$ طبقة دفاعية، ولكل منها احتمال فشل $q_i$. واحتمال نجاح الهجوم عبر كل الطبقات هو حاصل ضرب قيم $q_i$. وإذا كان المتوسط $q_i = 0.2$ عبر 5 طبقات، فإن $P_{success} = (0.2)^5 = 0.00032$، وهو ما يُظهر خفضًا أُسّيًا للمخاطر.»

#### ③ الشرح الفهمي

هذا القسم يحوّل الكلام النظري لأرقام. عندك نموذجان:

**1) توزيع المخاطر في الشبكة المقسّمة**

| الرمز | المعنى |
|---|---|
| $R_i = P_i \cdot V_i$ | مخاطر كل قطاع = احتمال التهديد × درجة الثغرة |
| $R_{net} = \sum_{i=1}^{m} R_i$ | المخاطر الكلية = مجموع مخاطر كل القطاعات |
| $R_{eff} = \alpha \cdot R_{net}$ | المخاطر الفعلية = المخاطر الكلية × كفاءة التقسيم |

المعنى المنطقي: كل قطاع له ثغرة ($V_i$) واحتمال استغلال ($P_i$). تجمعهم تحصل المخاطر الكلية. بعدين التقسيم يضربها بمعامل $\alpha$:
- لو $\alpha = 1$ ← يعني ما عندك عزل، المخاطر كاملة.
- لو $\alpha$ قريب من 0 ← يعني عزل شبه تام (micro segmentation)، المخاطر تنهار.

**2) احتمال نجاح الهجوم عبر طبقات الدفاع**

المنطق معاكس تمامًا لاحتمال الدفاع: حتى ينجح الهجوم، لازم يفشل **كل** الضوابط بالتتابع. فبدل ما نجمع، نضرب احتمالات الفشل $q_i$:

$$P_{success} = \prod_{i=1}^{n} q_i$$

المثال: متوسط فشل $q_i = 0.2$ عبر 5 طبقات:
- $P_{success} = 0.2 \times 0.2 \times 0.2 \times 0.2 \times 0.2 = (0.2)^5 = 0.00032$.

يعني احتمال نجاح 0.032% فقط — خفض أُسّي (exponential) مو خطي. هذا يفسّر ليش Defense in Depth فعّال جدًا: كل طبقة إضافية تقلّل الاحتمال بمعامل ثابت، فينزل بسرعة هائلة.

نقطة مقارنة سريعة:

| المفهوم | المعادلة | الاتجاه |
|---|---|---|
| مخاطر القطاع | $R_i = P_i \cdot V_i$ | تراكم ضربي |
| المخاطر الكلية | $R_{net} = \sum R_i$ | تراكم جمعي |
| خفض المخاطر بالتقسيم | $R_{eff} = \alpha \cdot R_{net}$ | ضرب بمعامل $\alpha$ |
| نجاح الهجوم عبر الطبقات | $P_{success} = \prod q_i$ | تراكم ضربي (أُسّي) |

---

### القسم 5 — 5. Emerging Trends in Network Segmentation

#### ① النص الأصلي

> Micro segmentation isolates workloads and applications at the process level, often enforced through software-defined networking (SDN). Unlike VLANs, which separate traffic by broadcast domains, micro segmentation enforces fine-grained, identity-based policies. Its efficiency can be modeled as the fraction of total communications that are not legitimate: with $N$ total communications and $N_{allowed}$ legitimate communications post-policy, the segmentation effectiveness rises as more unnecessary traffic is contained.
>
> Zero Trust assumes no implicit trust, even within internal networks; access is continuously verified, with segmentation enforcing least-privilege. This is often modeled as a Markov chain with four states — access request, authentication/verification, conditional access granted, and denial/quarantine — where the transition probabilities reflect verification rigor, and the steady-state probability of compromise is minimized under strict verification.
>
> In cloud-native environments, segmentation extends to containers, pods, and microservices. Policies are enforced via service meshes (e.g., Istio), ensuring encrypted, authenticated east–west communication.

$$E_{micro} = \frac{N - N_{allowed}}{N}$$

$$\pi = \pi P \qquad \text{s.t.} \qquad \sum_{j} \pi_j = 1$$

| الرمز | المعنى |
|---|---|
| $E_{micro}$ | فعالية التقسيم الدقيق (احتواء الحركة غير الضرورية) |
| $N$ | إجمالي الاتصالات |
| $N_{allowed}$ | الاتصالات المشروعة المسموح بها بعد السياسة |
| $\pi$ | متجه الاحتمالات في الحالة المستقرة (steady-state) لسلسلة Markov |
| $P$ | مصفوفة احتمالات الانتقال لسلسلة Markov |
| $S_1$ | Access Request |
| $S_2$ | Authentication / Verification |
| $S_3$ | Conditional Access Granted |
| $S_4$ | Denial / Quarantine |

#### ② الترجمة

> «التقسيم الدقيق (Micro segmentation) يعزل أحمال العمل والتطبيقات على مستوى العملية (process)، وغالبًا يُفرض عبر الشبكات المعرّفة برمجيًا (SDN). وبخلاف VLANs التي تفصل الحركة بنطاقات البثّ، يفرض التقسيم الدقيق سياسات دقيقة قائمة على الهوية. ويمكن نمذجة فعاليته ككسر من إجمالي الاتصالات غير المشروعة: مع $N$ اتصالًا إجماليًا و $N_{allowed}$ اتصالًا مشروعًا بعد السياسة، ترتفع فعالية التقسيم كلما احتُويت حركة غير ضرورية أكثر.
>
> يفترض Zero Trust عدم وجود ثقة ضمنية، حتى داخل الشبكات الداخلية؛ ويُتحقَّق من الوصول باستمرار، مع فرض التقسيم لمبدأ الامتياز الأدنى (least-privilege). وغالبًا ما يُنمذَج هذا كسلسلة Markov بأربع حالات — طلب الوصول، والمصادقة/التحقق، ومنح الوصول المشروط، والرفض/الحجر — حيث تعكس احتمالات الانتقال صرامة التحقق، ويُقلَّل احتمال الاختراق في الحالة المستقرة في ظل تحقّق صارم.
>
> وفي البيئات السحابية الأصلية، يمتدّ التقسيم ليشمل الحاويات (containers) والـ pods والخدمات المصغّرة (microservices). وتُفرض السياسات عبر أعمدة الخدمة (service meshes) مثل Istio، بما يضمن اتصالًا شرق–غرب (east–west) مشفّرًا وموثّقًا.»

#### ③ الشرح الفهمي

هذا القسم عن ثلاثة اتجاهات حديثة:

**1) Micro segmentation**

الفرق الجوهري عن VLAN: الـ VLAN تفصل حسب نطاق البثّ (broadcast domain)، أما micro segmentation فتفرض سياسات دقيقة قائمة على الهوية (identity-based) على مستوى الحِمل/التطبيق/العملية. يعني عزل أدق بمراحل.

الفعالية تُقاس بالكسر: كم نسبة الحركة اللي **ما** سمحنا بها من أصل كل الحركة:

| الرمز | المعنى |
|---|---|
| $E_{micro}$ | الفعالية (احتواء الحركة غير الضرورية) |
| $N$ | إجمالي الاتصالات |
| $N_{allowed}$ | الاتصالات المشروعة المسموح بها بعد السياسة |

كل ما $E_{micro}$ أعلى ← عزلنا حركة أكثر غير ضرورية ← احتواء أفضل.

**2) Zero Trust Integration**

الفكرة: ما تعطي ثقة تلقائية لأي أحد، حتى لو كان داخل الشبكة. كل وصول يُتحقَّق منه باستمرار، والتقسيم يفرض least-privilege. يُنمذَج كسلسلة Markov بأربع حالات:

| الحالة | المعنى |
|---|---|
| $S_1$ | Access Request — طلب الوصول |
| $S_2$ | Authentication / Verification — المصادقة والتحقق |
| $S_3$ | Conditional Access Granted — منح الوصول المشروط |
| $S_4$ | Denial / Quarantine — الرفض أو الحجر |

احتمالات الانتقال ($P$) تعكس صرامة التحقق. ومعادلة الحالة المستقرة أعلاه ($\pi = \pi P$) تحسب التوزيع طويل الأمد على الحالات؛ كل ما التحقق أصرم، قلّ احتمال الوصول للحالة $S_3$ (المنح) وبالتالي قلّ احتمال الاختراق في الحالة المستقرة.

**3) Cloud and Containerized Segmentation**

في البيئات السحابية الأصلية، التقسيم ما يوقف عند الأجهزة — يمتد للحاويات (containers) والـ pods والخدمات المصغّرة (microservices). ويُفرض عبر service meshes مثل Istio، اللي تضمن إن الاتصال شرق–غرب (بين الخدمات داخليًا) يكون مشفّرًا وموثّقًا. هذا مهم لأن أغلب الهجمات الحديثة تستهدف الحركة الداخلية (east–west) مو الحدود الخارجية.

---

![التقسيم والدفاع في العمق — 5 طبقات|720](../06_Diagrams_&_Mindmaps/cy_w5_defense_in_depth.svg)
