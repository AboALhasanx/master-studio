### القسم 1 — Introduction
#### ① النص الأصلي
> The security of web applications is contingent upon the timely identification and mitigation of vulnerabilities. Traditional approaches once focused on perimeter defenses and patch cycles; however, the increasing complexity of digital ecosystems, reliance on third-party components, and the sophistication of adversarial techniques necessitate more advanced perspectives. Securing vulnerabilities is no longer a reactive task but a proactive, continuous process embedded in the strategic and operational fabric of modern organizations.
>
> The concept of vulnerability management must now extend beyond the remediation of known weaknesses to encompass predictive analytics, adaptive protection, and automated remediation pipelines. From SQL injection in monolithic architectures to API exploits in microservice environments, modern perspectives demand systemic solutions combining governance, technology, and quantitative risk analysis.
#### ② الترجمة
> «يتوقّف أمن تطبيقات الويب على التحديد والمعالجة في الوقت المناسب لنقاط الضعف (vulnerabilities). كانت المقاربات التقليدية تركّز على دفاعات المحيط (perimeter defenses) ودورات الترقيع (patch cycles)؛ بيد أن التعقيد المتزايد للنظم البيئية الرقمية، والاعتماد على مكوّنات الأطراف الثالثة، وتعقيد تقنيات الخصوم، كلها تستوجب منظورات أكثر تقدّماً. لم يعد تأمين نقاط الضعف مهمّة تفاعلية (reactive)، بل عملية استباقية مستمرة مندمجة في النسيج الاستراتيجي والتشغيلي للمؤسسات الحديثة.»
>
> «على مفهوم إدارة نقاط الضعف (vulnerability management) الآن أن يتجاوز معالجة الضعفات المعروفة ليشمل التحليلات التنبّؤية (predictive analytics)، والحماية التكيّفية (adaptive protection)، وخطوط المعالجة الآلية (automated remediation pipelines). فمن الـ SQL injection في البنى المتراصّة (monolithic) إلى استغلال الـ APIs في بيئات الـ microservices، تتطلّب المنظورات الحديثة حلولاً نُظُمية (systemic) تجمع بين الحوكمة والتقنية والتحليل الكمّي للمخاطر.»
#### ③ الشرح الفهمي
هذا القسم مقدّمة مفتاحية للفصل: يقول إن **أمن تطبيقات الويب ما يقوم إلا إذا تكتشف الثغرة وتعالجها بسرعة**. الماضي كان يعتمد على **perimeter defenses** (يعني تحمي الحافة بس) و**patch cycles** (ترقّع كل فترة). هذا الأسلوب صار ما يكفي، لثلاثة أسباب: **تعقيد النظم البيئية** + **الاعتماد على مكوّنات طرف ثالث (third-party components)** + **تعقيد المهاجمين**.

النقطة المحورية: **تأمين الثغرات انتقل من reactive ← إلى proactive**. صار عملية مستمرة، مو شغلة مرة وتخلص. وأضاف القسم إن **vulnerability management** اليوم لازم تتجاوز "نصلّح الضعفات المعروفة" لتصير ثلاثة أشياء:

- **Predictive analytics** — تحليل تنبّؤي يتوقّع الثغرة قبل ما تصير.
- **Adaptive protection** — حماية تتكيّف مع التهديد المتغيّر.
- **Automated remediation pipelines** — خطوط معالجة آلية تشتغل بنفسها.

المثال اللي يعطيه يوضّح المدى: من **SQL injection** بالبنى القديمة **monolithic** ← إلى **API exploits** ببيئات **microservices**. يعني المشكلة تطوّرت مع المعمارية. والحل المطلوب **systemic** (نُظُمي، مو بقعة هنا وبقعة هناك) يجمع ثلاثة أعمدة: **governance** (حوكمة) + **technology** (تقنية) + **quantitative risk analysis** (تحليل كمّي للمخاطر).

### القسم 2 — Evolution of Vulnerability Management
#### ① النص الأصلي
> **2.1 Traditional Approach.** In earlier eras, vulnerability management was largely reactive. Periodic scans identified flaws, and security teams prioritized patches manually. This model suffered from long exposure windows, poor scalability, and limited contextual awareness.
>
> **2.2 Contemporary Approach.** Modern vulnerability management integrates continuous monitoring, real-time intelligence, and automated remediation. Vulnerabilities are contextualized by their exploitability, potential impact, and relation to business-critical assets. Strategic emphasis lies in predictive identification and risk-based prioritization, ensuring that scarce resources mitigate the most significant threats.
#### ② الترجمة
> «**2.1 المقاربة التقليدية (Traditional Approach).** في عصور سابقة، كانت إدارة نقاط الضعف تفاعلية (reactive) إلى حدّ كبير. فقد كانت الفحوصات الدورية (periodic scans) تحدّد العيوب، وتُرتّب فرق الأمن الترقيعات يدوياً. وعانى هذا النموذج من نوافذ تعرّض طويلة (long exposure windows)، وضعف قابلية التوسّع (scalability)، ومحدودية الوعي السياقي (contextual awareness).»
>
> «**2.2 المقاربة المعاصرة (Contemporary Approach).** تدمج إدارة نقاط الضعف الحديثة المراقبة المستمرة (continuous monitoring)، والاستخبارات الفورية (real-time intelligence)، والمعالجة الآلية (automated remediation). وتُوضَع نقاط الضعف في سياقها حسب قابليتها للاستغلال (exploitability)، وأثرها المحتمل، وعلاقتها بالأصول الحيوية للأعمال (business-critical assets). ويكمن التشديد الاستراتيجي في التحديد التنبّؤي (predictive identification) والترتيب القائم على المخاطر (risk-based prioritization)، بما يضمن أن الموارد الشحيحة تخفّف أخطر التهديدات.»
#### ③ الشرح الفهمي
هذا القسم يقارن بين عصرين في إدارة الثغرات. الفرق الأساسي: **reactive ← proactive**.

| المعيار | Traditional | Contemporary |
|---|---|---|
| التوقيت | فحوصات دورية (periodic scans) | مراقبة مستمرة (continuous monitoring) |
| الترتيب | يدوي (manual) | قائم على المخاطر (risk-based) |
| المصدر | بلا استخبارات | استخبارات فورية (real-time intelligence) |
| المعالجة | يدوية | آلية (automated remediation) |
| السياق | محدود (limited contextual awareness) | سياق كامل (exploitability + impact + أصول حرجة) |

المشاكل الثلاث للمقاربة التقليدية لازم تحفظها: **long exposure windows** (الثغرة تبقى مكشوفة مدة طويلة) + **poor scalability** (ما تتوسّع) + **limited contextual awareness** (ما تفهم شكد الثغرة مهمّة).

المقاربة الحديثة ترتّب الثغرة بثلاثة معايير: **exploitability** (شكد سهلة تُستغل) + **potential impact** (شكد أثرها) + **relation to business-critical assets** (هل تخصّ أصل حيوي). والهدف: **scarce resources** (موارد شحيحة) تروح للأخطر. النقطة المهمة للامتحان: **predictive identification** — يعني تتوقّع قبل ما تُستغل.

### القسم 3 — Modern Vulnerabilities in Web Applications
#### ① النص الأصلي
> The modern web application landscape is shaped by six dominant vulnerability classes, ranging from long-known exploits that keep resurfacing to risks unique to contemporary architectures.
>
> - **3.1 SQL Injection (SQLi).** SQLi remains a high-impact vulnerability, particularly when applications directly interact with relational databases. Despite its maturity as a threat, variations such as blind SQLi and NoSQL injection have reemerged due to the adoption of flexible data stores.
> - **3.2 Cross-Site Scripting (XSS).** XSS exploits remain prevalent, particularly in single-page applications (SPAs) where JavaScript dominates. DOM-based XSS introduces new complexity by shifting vulnerability to client-side code execution.
> - **3.3 Cross-Site Request Forgery (CSRF).** While mitigated by the SameSite cookie attribute, CSRF continues to present risks in environments with complex session handling, particularly across federated identity systems.
> - **3.4 API and Microservices Vulnerabilities.** With microservice adoption, APIs have become the primary interface for business logic. Broken object-level authorization (BOLA) and excessive data exposure now rank among the most exploited vulnerabilities.
> - **3.5 Supply Chain Vulnerabilities.** Third-party libraries and frameworks, often incorporated without sufficient vetting, create systemic risk. Exploits such as dependency confusion and malicious package injection demonstrate the necessity of securing the software supply chain.
> - **3.6 Cloud-Native and Serverless Vulnerabilities.** Container misconfigurations, insecure orchestration (e.g., Kubernetes API exposure), and event injection in serverless platforms highlight vulnerabilities unique to modern architectures.
#### ② الترجمة
> «يتشكّل مشهد تطبيقات الويب الحديثة من ستّ فئات مهيمنة من نقاط الضعف، تتراوح بين استغلالات معروفة منذ زمن طويل تعاود الظهور، ومخاطر فريدة بالبنى المعاصرة.»
>
> - «**3.1 حقن SQL (SQL Injection — SQLi).** يبقى الـ SQLi ثغرة عالية الأثر، لا سيّما حين تتفاعل التطبيقات مباشرة مع قواعد البيانات العلائقية (relational databases). ورغم نضوجه كتهديد، أعادت تنويعات مثل الـ blind SQLi وحقن NoSQL (NoSQL injection) الظهور بسبب تبنّي مخازن بيانات مرنة.»
> - «**3.2 البرمجة عبر المواقع (Cross-Site Scripting — XSS).** ما زالت استغلالات الـ XSS سائدة، خصوصاً في تطبيقات الصفحة الواحدة (SPAs) التي يهيمن عليها JavaScript. ويُدخل الـ DOM-based XSS تعقيداً جديداً بنقل نقطة الضعف إلى تنفيذ الكود على جانب العميل (client-side code execution).»
> - «**3.3 تزوير الطلب عبر المواقع (Cross-Site Request Forgery — CSRF).** رغم تخفيفها بخاصية SameSite في الـ cookie، لا يزال الـ CSRF يمثّل مخاطر في البيئات ذات إدارة الجلسات المعقّدة (complex session handling)، خصوصاً عبر أنظمة الهوية الاتحادية (federated identity systems).»
> - «**3.4 ثغرات الـ API والـ microservices.** مع تبنّي الـ microservices، صارت الـ APIs الواجهة الأساسية لمنطق الأعمال (business logic). ويُصنَّف الـ broken object-level authorization (BOLA) والكشف المفرط عن البيانات (excessive data exposure) الآن ضمن أكثر الثغرات استغلالاً.»
> - «**3.5 ثغرات سلسلة التوريد (Supply Chain).** تُنشئ مكتبات وأُطُر الأطراف الثالثة — التي كثيراً ما تُدمَج دون تدقيق كافٍ (sufficient vetting) — خطراً نُظُمياً. وتُظهر استغلالات مثل dependency confusion وحقن الحزم الخبيثة (malicious package injection) ضرورة تأمين سلسلة توريد البرمجيات.»
> - «**3.6 ثغرات البيئات السحابية الأصلية والـ serverless (Cloud-Native and Serverless).** تُبرز إساءات ضبط الحاويات (container misconfigurations)، والتنسيق غير الآمن (insecure orchestration، مثل تعرّض Kubernetes API)، وحقن الأحداث (event injection) في منصّات الـ serverless، نقاط ضعف فريدة بالبنى الحديثة.»
#### ③ الشرح الفهمي
هذا القسم هو **أهم قسم امتحانياً في الفصل** — الستّ ثغرات. خلّ نفهما وحدة وحدة، وبعدها الجدول الجامع.

**3.1 SQL Injection (SQLi):** تصير لما التطبيق يحطّ إدخال المستخدم مباشرة داخل استعلام قاعدة بيانات. الـ SQLi ما مات، بالعكس: طلعت تنويعات جديدة بسبب **flexible data stores**:
- **Blind SQLi** — المهاجم ما يشوف النتيجة مباشرة، يستنتجها من سلوك التطبيق (yes/no أو time delay).
- **NoSQL injection** — نفس الفكرة بس على قواعد NoSQL المرنة.

**3.2 Cross-Site Scripting (XSS):** حقن JavaScript خبيث ينفّذ بمتصفّح الضحية. صار خطير أكثر ببيئات **SPAs (Single-Page Applications)** لأن JavaScript يهيمن على كل شي. وأخطر تنويع هو **DOM-based XSS**: نقطة الضعف انتقلت من السيرفر إلى **client-side code execution** — يعني الثغرة بالمتصفّح نفسه، مو بالسيرفر، فهي أصعب كشفاً.

**3.3 Cross-Site Request Forgery (CSRF):** يخدع متصفّح الضحية حتى يرسل طلب مصادَق عليه (بالجلسة القائمة) بدون علمه. الدفاع المعروف هو **SameSite cookie attribute**. بس يبقى خطر ببيئات **complex session handling**، وخصوصاً **federated identity systems** (نظام تسجيل دخول واحد لعدّة خدمات).

**3.4 API and Microservices Vulnerabilities:** مع تبنّي الـ microservices، صارت الـ APIs هي **primary interface for business logic**. الثغرتين الأشهر:
- **BOLA (Broken Object-Level Authorization)** — المستخدم يوصّل شي ما لازم يوصّله، لأن التطبيق ما يتحقّق من ملكية الـ object.
- **Excessive data exposure** — الـ API ترجّع بيانات أكثر من اللازم.

**3.5 Supply Chain Vulnerabilities:** مكتبات وأُطُر الطرف الثالث تدخل المشروع **بلا تدقيق كافٍ (insufficient vetting)**، وهذا **systemic risk** — يعني الخطر مو بكويدك، بل باللي تعتمد عليه. مثالان مهمّان:
- **Dependency confusion** — المهاجم ينشر حزمة بنفس اسم حزمة داخلية، فالمشروع يسحب الحزمة الخبيثة.
- **Malicious package injection** — حقن حزمة خبيثة داخل السلسلة.

**3.6 Cloud-Native and Serverless Vulnerabilities:** ثغرات ما تخصّ البنى القديمة:
- **Container misconfigurations** — إساءة ضبط الحاويات.
- **Insecure orchestration** — مثل **Kubernetes API exposure**.
- **Event injection** — حقن الأحداث بمنصّات الـ serverless.

الجدول الجامع — احفظه للامتحان:

| الثغرة | كيف تشتغل | كيف نحمي منها |
|---|---|---|
| **SQLi** | إدخال مستخدم يدخل مباشرة بالـ SQL query (حتى blind وNoSQL variants) | Prepared statements / parameterized queries + input validation |
| **XSS** | حقن JavaScript خبيث ينفّذ بمتصفّح الضحية (SPAs و DOM-based) | Output encoding + CSP + input sanitization |
| **CSRF** | يخدع المتصفّح يرسل طلب مصادَق عليه بدون علم الضحية | SameSite cookie + anti-CSRF tokens |
| **API / Microservices** | BOLA + excessive data exposure على واجهات الـ API | Object-level authorization + schema validation + rate limiting |
| **Supply Chain** | مكتبات طرف ثالث غير مدقّقة (dependency confusion / malicious package) | Dependency vetting + SCA + تثبيت النسخ (pinning) |
| **Cloud-Native / Serverless** | container misconfigurations + insecure orchestration + event injection | Hardening + policy enforcement + continuous monitoring |

![الثغرات الكلاسيكية والحديثة|720](../06_Diagrams_&_Mindmaps/cy_w6_vulnerabilities.svg)
