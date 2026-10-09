### القسم 1 — Introduction

#### ① النص الأصلي
> Web application security is not merely a technical discipline; it is a systemic science requiring the integration of robust tools and disciplined practices to ensure the confidentiality, integrity, and availability of application services. Tools form the technological armory — firewalls, scanners, runtime protectors, and monitoring platforms — while practices constitute the human and procedural element: secure coding, authentication frameworks, and lifecycle governance. Together, these elements define the operational effectiveness of modern web application defense.
>
> A sophisticated understanding of tools and practices must extend beyond enumeration into a framework of strategic integration, continuous evolution, and quantitative evaluation. Mathematical models allow the quantification of effectiveness, providing a rigorous scientific foundation for decision-making.

#### ② الترجمة
> «أمن تطبيقات الويب ليس مجرّد تخصّص تقني؛ بل هو علم منظومي يتطلّب دمج أدوات قوية وممارسات منضبطة لضمان السرّية والسلامة والتوافرية لخدمات التطبيقات. فالأدوات تشكّل الترسانة التقنية — الجدران النارية والماسحات وحُماة وقت التشغيل ومنصّات المراقبة — أما الممارسات فتمثّل العنصر البشري والإجرائي: البرمجة الآمنة وأطر المصادقة وحوكمة دورة الحياة. ومعًا تُحدّد هذه العناصر الفاعلية التشغيلية للدفاع الحديث عن تطبيقات الويب.
>
> والفهم المتقدّم للأدوات والممارسات يجب أن يتجاوز مجرّد التعداد إلى إطار من التكامل الاستراتيجي والتطوّر المستمر والتقييم الكمّي. فالنماذج الرياضية تتيح قياس الفاعلية، ما يوفّر أساسًا علميًا صارمًا لاتخاذ القرار.»

#### ③ الشرح الفهمي
هاي المقدمة تربط فكرتين: **الأدوات (Tools)** و**الممارسات (Practices)**. الاثنين ما ينفعون بدون بعض — الأداة بدون ممارسة صحيحة تصير بس تكلفة، والممارسة بدون أداة تصير نية بلا تنفيذ.

| البُعد | الأدوات (Tools) | الممارسات (Practices) |
|---|---|---|
| شنو هي | تقنية/برمجية | بشرية وإجرائية |
| أمثلة | WAF، Scanner، RASP، SIEM | Secure Coding، Authentication، Governance |
| دورها | تكتشف وتمنع تقنيًا | تنظّم العمل وتضبط السلوك |
| الهدف | حماية تقنية مباشرة | استدامة وحوكمة |

النقطة الأهم: الفهم ما يوقف عند **enumeration** (عدّ الأدوات وحفظها)، بل يتطوّر إلى إطار من ثلاثة عناصر:

- **Strategic integration** ← دمج الأدوات والممارسات مع بعضها.
- **Continuous evolution** ← تتطوّر مع تغيّر التهديدات.
- **Quantitative evaluation** ← تقييم بالأرقام مو بالإحساس.

وهنا يظهر دور **النماذج الرياضية (Mathematical models)** — لأنها تحوّل «الأداة زينة أو لا» إلى رقم نقدر نقارن بيه ونقرّر. الأساس هو الثلاثية الأمنية **CIA**: Confidentiality + Integrity + Availability.

---

### القسم 2 — Tools in Web Application Security

#### ① النص الأصلي
> **2.1 Web Application Firewalls (WAFs)** — A Web Application Firewall (WAF) operates at the application layer, filtering and monitoring HTTP/S traffic to block malicious payloads such as SQL injection and Cross-Site Scripting (XSS). Modern WAFs deploy signature-based detection, heuristic anomaly detection, and AI-driven adaptive filtering. WAF efficiency can be captured using the true positive rate (TPR) and the false positive rate (FPR), and the optimal strategy maximizes E_WAF by balancing detection accuracy with usability.
>
> **2.2 Vulnerability Scanners** — These are automated tools probing applications for misconfigurations, outdated components, or insecure coding patterns. They integrate with CVE (Common Vulnerabilities and Exposures) databases to detect known weaknesses. Risk scores from scanners can be formalized, forming the basis for vulnerability prioritization matrices in enterprise strategies.
>
> **2.3 Runtime Application Self-Protection (RASP)** — RASP operates within the runtime environment of an application, monitoring its internal behavior and intercepting malicious activity dynamically. Unlike WAFs, which monitor external traffic, RASP detects attacks by analyzing execution flow, API calls, and memory states. Its effectiveness is represented as runtime coverage (RC); the closer RC approaches 1, the more comprehensive the runtime protection.
>
> **2.4 Penetration Testing Platforms** — Whether automated or manual, these tools simulate adversarial techniques to identify weaknesses not captured by automated scanners. Their value lies in the adversarial creativity factor (ACF). An ACF greater than 1 indicates that human-led or hybrid pentesting provides additional strategic insight beyond automation.
>
> **2.5 Security Information and Event Management (SIEM) and Threat Intelligence Tools** — SIEM systems aggregate logs, detect anomalies, and provide real-time alerts. Their power lies in event correlation, which transforms isolated alerts into actionable incidents, forming the backbone of security orchestration.
>
> **2.6 Emerging Tools.** The emerging toolset includes:
>
> - API Gateways with Security Layers: Protect APIs with schema validation, OAuth 2.0 enforcement, and rate limiting.
> - Container and Cloud-Native Scanners: Tools scanning Kubernetes deployments or serverless functions.
> - AI-Powered Anomaly Detection: Reinforcement learning models predicting attack sequences.
>
> These emerging tools reflect the shift of strategic attention toward distributed architectures and intelligent adversaries.

$$E_{WAF} = \frac{TP}{TP + FN} - \lambda \cdot \frac{FP}{FP + TN}$$

| الرمز | المعنى |
|---|---|
| $TP$ | true positives — الهجمات اللي انصدّت بالصح |
| $FN$ | false negatives — الهجمات اللي فاتت (missed) |
| $FP$ | false positives — طلبات شرعية انحظرت بالغلط |
| $TN$ | true negatives — طلبات شرعية عدّت صح |
| $\lambda$ | معامل وزن يعكس تحمّل المؤسسة للـ false positives |

$$R_i = L_i \cdot I_i \cdot S_i$$

| الرمز | المعنى |
|---|---|
| $R_i$ | درجة خطر الثغرة $i$ |
| $L_i$ | likelihood — احتمال استغلال الثغرة $i$ |
| $I_i$ | impact — الأثر عند نجاح الاستغلال |
| $S_i$ | exposure scope — نطاق التعرّض (عدد النسخ المتاحة) |

$$RC = \frac{\text{Monitored Execution Paths}}{\text{Total Execution Paths}}$$

| الرمز | المعنى |
|---|---|
| $RC$ | runtime coverage — نسبة مسارات التنفيذ المراقَبة |
| Monitored Execution Paths | مسارات التنفيذ اللي يراقبها الـ RASP |
| Total Execution Paths | كل مسارات التنفيذ الممكنة |

$$ACF = \frac{V_d}{V_a}$$

| الرمز | المعنى |
|---|---|
| $ACF$ | adversarial creativity factor — عامل الإبداع الخصمي |
| $V_d$ | الثغرات المكتشفة عبر هجمات محاكاة (discovered) |
| $V_a$ | الثغرات المفترضة من التحليل الآلي (assumed) |

$$C_{event} = f(\Delta t, S, P)$$

| الرمز | المعنى |
|---|---|
| $C_{event}$ | قوة/درجة ربط الحدث |
| $\Delta t$ | temporal proximity — التقارب الزمني بين الأحداث المترابطة |
| $S$ | source similarity — تشابه المصدر (IP، هوية الجهاز) |
| $P$ | probability threshold — عتبة الاحتمال للربط |

#### ② الترجمة
> «**2.1 جدران حماية تطبيقات الويب (WAFs)** — يعمل جدار حماية تطبيقات الويب (WAF) على طبقة التطبيق، فيرشّح ويراقب حركة HTTP/S لحجب الحمولات الخبيثة مثل حقن SQL والبرمجة عبر المواقع (XSS). والـ WAFs الحديثة تستخدم الكشف القائم على التوقيعات، وكشف الشذوذ الإرشادي، والترشيح التكيّفي المدفوع بالذكاء الاصطناعي. ويمكن التعبير عن كفاءة الـ WAF باستخدام معدّل الإيجابيات الحقيقية (TPR) ومعدّل الإيجابيات الكاذبة (FPR)، والاستراتيجية المثلى تعظّم E_WAF عبر الموازنة بين دقة الكشف وقابلية الاستخدام.
>
> **2.2 ماسحات الثغرات** — أدوات آلية تفحص التطبيقات بحثًا عن أخطاء التهيئة أو المكوّنات القديمة أو أنماط البرمجة غير الآمنة. وتتكامل مع قواعد بيانات CVE (Common Vulnerabilities and Exposures) لاكتشاف نقاط الضعف المعروفة. ويمكن صياغة درجات الخطر الصادرة من الماسحات، وهي تشكّل أساسًا لمصفوفات ترتيب أولوية الثغرات في استراتيجيات المؤسسات.
>
> **2.3 الحماية الذاتية للتطبيق وقت التشغيل (RASP)** — يعمل الـ RASP داخل بيئة تشغيل التطبيق، فيراقب سلوكه الداخلي ويعترض النشاط الخبيث ديناميكيًا. وخلافًا للـ WAFs التي تراقب الحركة الخارجية، يكشف الـ RASP الهجمات عبر تحليل مسار التنفيذ واستدعاءات الـ API وحالات الذاكرة. ويُمثَّل فعاليته بتغطية وقت التشغيل (RC)؛ وكلّما اقتربت RC من 1 صارت حماية وقت التشغيل أشمل.
>
> **2.4 منصّات اختبار الاختراق** — سواء كانت آلية أو يدوية، تحاكي هذه الأدوات أساليب الخصم لتحديد نقاط ضعف لا تلتقطها الماسحات الآلية. وتكمن قيمتها في عامل الإبداع الخصمي (ACF). وقيمة ACF أكبر من 1 تدلّ على أن اختبار الاختراق البشري أو الهجين يوفّر رؤية استراتيجية إضافية تتجاوز الأتمتة.
>
> **2.5 إدارة معلومات وأحداث الأمن (SIEM) وأدوات استخبارات التهديدات** — تجمع أنظمة الـ SIEM السجلات، وتكشف الشذوذ، وتقدّم تنبيهات فورية. وتكمن قوّتها في ربط الأحداث، الذي يحوّل التنبيهات المعزولة إلى حوادث قابلة للتنفيذ، فيشكّل العمود الفقري لتنسيق الأمن.
>
> **2.6 الأدوات الناشئة.** وتشمل المجموعة الناشئة:
>
> - بوّابات الـ API مع طبقات أمنية: تحمي الـ APIs عبر التحقّق من الـ schema وفرض OAuth 2.0 وتحديد المعدّل.
> - ماسحات الحاويات والسحابة الأصلية: أدوات تفحص نشر Kubernetes أو دوال serverless.
> - كشف الشذوذ المدفوع بالذكاء الاصطناعي: نماذج التعلّم المعزّز تتنبّأ بتسلسلات الهجوم.
>
> وتعكس هذه الأدوات الناشئة انتقال الاهتمام الاستراتيجي نحو البنى الموزّعة والخصوم الأذكياء.»

#### ③ الشرح الفهمي
هذا القسم يجمع **الأدوات (Tools)** اللي نستخدمها لحماية تطبيقات الويب، وكل أداة تشتغل من زاوية مختلفة. الجدول يلخّص الستة:

| الأداة | وين تشتغل | شنو تسوي | المقياس |
|---|---|---|---|
| WAF | طبقة التطبيق (خارجي) | يرشّح HTTP/S ويحجب SQLi و XSS | $E_{WAF}$ |
| Vulnerability Scanner | على التطبيق كامل | يفحص ثغرات معروفة من CVE | $R_i$ |
| RASP | داخل runtime التطبيق | يراقب السلوك الداخلي ويعترض | $RC$ |
| Pentest Platform | ضد التطبيق (محاكاة) | يحاكي المهاجم يلقط اللي الماسح فوّته | $ACF$ |
| SIEM + Threat Intel | على السجلات والأحداث | يجمع logs ويربط الأحداث | $C_{event}$ |
| Emerging Tools | API / Cloud / AI | بوّابات API، ماسحات الحاويات، كشف AI | — |

**أهم تفريق لازم تحفظه:** الفرق بين **WAF** و**RASP**. الـ WAF يشوف من **برّه** (external traffic)، والـ RASP يشوف من **جوّه** (execution flow + API calls + memory states). يعني لو الهجوم وصل داخل التطبيق وتجاوز الـ WAF، الـ RASP بعد يقدر يمسكه ← هاي فكرة **defense-in-depth**.

**المعادلات بالعراقي:**

- **$E_{WAF}$:** الكفاءة = نسبة الهجمات اللي انصدّت (TP / TP+FN) ناقص عقوبة على الإنذارات الكاذبة (FP / FP+TN) مضروبة بـ $\lambda$. معنى $\lambda$: إذا المؤسسة تكره تحجب طلبات الزبائن الشرعيين، ترفع $\lambda$ ← تصير الأداة أكثر حذرًا (أقل false positives بس ممكن تفوّت هجمات). فالتوازن بين **detection accuracy** و**usability** هو كل اللعبة.
- **$R_i = L_i \cdot I_i \cdot S_i$:** درجة الخطر = احتمال الاستغلال × الأثر × نطاق التعرّض. لأنه حاصل ضرب، لو أي عامل صفر ← الخطر صفر (مثلاً ثغرة ما الها impact، ما تستاهل أولوية). هاي أساس **prioritization matrices**.
- **$RC$:** تغطية وقت التشغيل = مسارات التنفيذ المراقَبة ÷ الكل. كلّما $RC$ اقتربت من **1** ← حماية أشمل. يعني الـ RASP قوي بقدر ما «يغطّي» من الكود الشغّال.
- **$ACF = V_d / V_a$:** لو $ACF > 1$ ← اختبار الاختراق البشري/الهجين لقط ثغرات أكثر من اللي توقّعها التحليل الآلي ← يعني **الإبداع البشري** يضيف قيمة ما تقدر الآلة توصلها لحالها.
- **$C_{event} = f(\Delta t, S, P)$:** قوة ربط الحدث تعتمد على ثلاثة: قرب الأحداث زمنيًا ($\Delta t$)، تشابه المصدر ($S$)، وعتبة الاحتمال ($P$). الفايدة: بدل ما يصير عندك ألف تنبيه معزول، الـ SIEM يربطهم ببعض ← يطلع **incident** واحد مفهوم قابل للتنفيذ. هاي عمود **security orchestration**.

النقطة الاستراتيجية: **الأدوات الناشئة (Emerging Tools)** تدل على وين رايح الاهتمام — من تطبيق واحد ← إلى **distributed architectures** (containers, serverless, APIs) وخصوم أذكياء يستخدمون AI.

![الأدوات مقابل الممارسات|720](../06_Diagrams_&_Mindmaps/cy_w6_tools_practices.svg)
