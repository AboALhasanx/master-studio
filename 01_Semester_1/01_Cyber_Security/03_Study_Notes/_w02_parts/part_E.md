### القسم 1 — Magnetic Stripe Readers
#### ① النص الأصلي
> A magnetic stripe card is a physical credit-card-like device that contains authentication information in the form of magnetically coded spots on a magnetic stripe.
> Fig. Magnetic Stripe Card System
#### ② الترجمة
> «بطاقة الشريط المغناطيسي (magnetic stripe card) هي جهاز مادي يشبه بطاقة الائتمان، ويحتوي على معلومات المصادقة (authentication) على شكل نقاط مُرمَّزة مغناطيسياً على شريط مغناطيسي.»
#### ③ الشرح الفهمي
هاي أبسط أنواع أدوات المصادقة الفيزيائية. الفكرة: عندك بطاقة بلاستيكية مثل بطاقة البنك، وعلى ظهرها شريط مغناطيسي (magnetic stripe) مخزّن عليه بيانات المصادقة بشكل نقاط مغناطيسية. الجهاز (reader) يقرأ هذا الشريط ويقارن البيانات حتى يتأكد إنه أنت المسموح لك بالدخول.

نقطة مهمة أمنياً: بيانات الشريط المغناطيسي مكشوفة نسبياً وسهلة النسخ (copying / skimming)، لأنها مجرد نقاط مغناطيسية تُقرأ مباشرة — يعني ما فيها حماية ذكية تخفي البيانات. هذا الفرق هو اللي يخلي smart cards أحسن منها، وهاي هي النقطة اللي تشرحها الفقرة الجاية.

### القسم 2 — Smart Cards
#### ① النص الأصلي
> Smart cards are also credit-card-like devices that often resemble magnetic stripe cards. However, they offer improved data security due to the presence of intelligent circuitry that can be used to hide the user’s data until an authentication process has been performed.
> Fig. Smart Cards
#### ② الترجمة
> «البطاقات الذكية (smart cards) هي أيضاً أجهزة تشبه بطاقة الائتمان، وكثيراً ما تشبه بطاقات الشريط المغناطيسي. لكنها توفّر أماناً أفضل للبيانات بسبب وجود دائرة إلكترونية ذكية (intelligent circuitry) يمكن استخدامها لإخفاء بيانات المستخدم إلى أن تُنفَّذ عملية المصادقة (authentication).»
#### ③ الشرح الفهمي
شكلها من برّا مثل بطاقة الشريط المغناطيسي، بس الفرق بالجوّا: فيها chip / دائرة ذكية. هذا الـ chip ما يخلّي بيانات المستخدم مكشوفة، يخليها مخفية (hidden) لحد ما تتم عملية المصادقة بنجاح. يعني حتى لو حد مسك البطاقة، ما يقدر يقرأ البيانات مباشرة مثل ما يصير بالشريط المغناطيسي. هذا هو سبب كونها "improved data security".

الفكرة الأساسية بالجملة: الأمان الأفضل جاي من الـ intelligent circuitry اللي تخفي البيانات لين تصير المصادقة.

### القسم 3 — RFID Badges
#### ① النص الأصلي
> Radio Frequency Identification (RFID) badges provide hands-free access-control tools that improve on the bar code, magnetic stripe, and proximity reader technologies. The RFID system employs radio signals to identify unique items using an RFID reader device and RFID tags.
> Fig. RFID System
#### ② الترجمة
> «شارات التعريف بترددات الراديو (RFID badges) توفّر أدوات للتحكم بالوصول من دون استخدام اليدين (hands-free)، وهي تطوّر على تقنيات الباركود (bar code) والشريط المغناطيسي (magnetic stripe) وقارئات الاقتراب (proximity reader). ونظام RFID يستعمل إشارات الراديو (radio signals) لتمييز العناصر الفريدة باستخدام جهاز قارئ RFID ووسوم RFID (RFID tags).»
#### ③ الشرح الفهمي
كلمة hands-free هي المفتاح: يعني ما تحتاج تطلّع البطاقة وتمرّرها، بس تقرّبها أو تمرّ جنبها وتتقرأ تلقائياً. النظام يتكوّن من جزئين:
- **RFID reader device** ← الجهاز اللي يقرأ.
- **RFID tags** ← الوسوم اللي تكون على الشارة/العنصر.

يستعمل **إشارات راديو** (radio signals) حتى يميّز كل عنصر عن الثاني (identify unique items). بالمقارنة، هذا أفضل من bar code وmagnetic stripe وproximity reader لأنه أسرع وأسهل بالاستخدام وما يحتاج لمس.

### القسم 4 — Biometric Scanners
#### ① النص الأصلي
> Biometrics is the term used to describe access-control mechanisms that use human physical characteristics to verify individual identities.
> Fig. Typical Biometric Authentication Methods
#### ② الترجمة
> «القياسات الحيوية (Biometrics) هو المصطلح المستخدم لوصف آليات التحكم بالوصول (access-control mechanisms) التي تستعمل الخصائص الجسدية للإنسان للتحقق من هوية الأفراد (verify individual identities).»
#### ③ الشرح الفهمي
بدل ما تعتمد على شي تملكه (بطاقة) أو شي تعرفه (كلمة مرور)، الـ biometrics تعتمد على **خصائص جسدية** خاصة بشخصك أنت. أمثلة شائعة: بصمة الإصبع (fingerprint)، بصمة العين/القزحية (iris)، بصمة الوجه (face)، الصوت (voice). الوظيفة الأساسية: تتحقق من هوية الفرد (verify identity). هذا النوع أقوى لأنه صعب ينتقل من شخص لشخص مثل البطاقة أو كلمة المرور.

وهذا جدول يجمّع تقنيات المصادقة الفيزيائية الأربعة اللي مرّت علينا (Magnetic Stripe, Smart Cards, RFID, Biometric):

| التقنية | النقطة المميزة |
|---|---|
| Magnetic Stripe Readers | بيانات المصادقة مخزّنة كنقاط مغناطيسية على شريط، والأمان فيها أضعف |
| Smart Cards | فيها دائرة ذكية (intelligent circuitry) تخفي بيانات المستخدم لين تتم المصادقة |
| RFID Badges | hands-free، تستعمل إشارات راديو (radio signals) مع reader وtags |
| Biometric Scanners | تعتمد على الخصائص الجسدية للإنسان للتحقق من الهوية |

### القسم 5 — Remote-Access Monitoring
#### ① النص الأصلي
> Remote monitoring refers to monitoring or measuring devices from a remote location or control room. In the security realm, this involves having external access to the security system through a communication system.
> Fig. Remote-Access Communication Options
#### ② الترجمة
> «المراقبة عن بُعد (Remote monitoring) تشير إلى مراقبة أو قياس الأجهزة من موقع بعيد أو من غرفة تحكم (control room). وفي المجال الأمني، هذا يعني امتلاك وصول خارجي (external access) إلى النظام الأمني عبر نظام اتصال (communication system).»
#### ③ الشرح الفهمي
الفكرة: بدل ما تكون واقف عند الجهاز نفسه، تراقبه من مكان ثاني (بعيد أو من control room). بالمجال الأمني، هذا يتحقق لما يكون عندك **وصول خارجي للنظام الأمني عبر نظام اتصال** — يعني الاتصال هو الجسر اللي يوصّل المراقب البعيد بالنظام. النتيجة: تقدر تشوف وتقيس شنو يصير بالأجهزة الأمنية وأنت بعيد.

### القسم 6 — Automated Access-Control Systems
#### ① النص الأصلي
> Automated access-control capabilities add another dimension to standard security monitoring and reporting functions. Although automated access control is not an integral part of the typical intrusion-detection and monitoring system, it adds to the safety and convenience of perimeter-access control. Automated access-control systems come in two flavors: remote-access-control systems and remote-control access systems.
> Remote-access control is a design feature that manages entry to protected areas by authenticating the identity of persons entering a secured area (security zone or computer system) using an authentication system located in a different location than the access point. While Remote-control access is a design feature that works with remote monitoring systems to monitor, control, and supervise doors, gates, and conveyances from a distance.
> Fig. Remote-Control Operations
#### ② الترجمة
> «قدرات التحكم الآلي بالوصول (Automated access-control) تضيف بُعداً آخر لوظائف المراقبة والإبلاغ الأمنية القياسية. ومع إن التحكم الآلي بالوصول ما هو جزء أصيل (integral) من نظام كشف التسلل والمراقبة (intrusion-detection and monitoring) النموذجي، إلا إنه يضيف للأمان والراحة في التحكم بالوصول عند المحيط (perimeter-access control). وأنظمة التحكم الآلي بالوصول تجي بنوعين: أنظمة التحكم بالوصول عن بُعد (remote-access-control systems) وأنظمة الوصول بالتحكم عن بُعد (remote-control access systems).
> التحكم بالوصول عن بُعد (Remote-access control) هو خاصية تصميمية تدير الدخول إلى المناطق المحمية عبر مصادقة هوية الأشخاص الداخلين إلى منطقة مؤمّنة (منطقة أمنية أو نظام حاسوبي) باستخدام نظام مصادقة موجود في موقع مختلف عن نقطة الدخول (access point). بينما الوصول بالتحكم عن بُعد (Remote-control access) هو خاصية تصميمية تشتغل مع أنظمة المراقبة عن بُعد لمراقبة والتحكم والإشراف على الأبواب والبوابات ووسائل النقل (doors, gates, and conveyances) من مسافة بعيدة.»
#### ③ الشرح الفهمي
هنا الفقرة تفرّق بين شيئين اسمهم متشابه بس معناهم مختلف تماماً، وهذا أشهر موضع يخبط الطالب:

- **Remote-access control**: أنت تسيطر على **من يدخل** (entry management). آلية العمل: فيه نظام مصادقة (authentication system) موجود بمكان **مختلف عن نقطة الدخول** — يعني الجهاز اللي يصادق الهوية مو بنفس الباب. من خلال المصادقة، تدير الدخول للمنطقة المحمية.
- **Remote-control access**: أنت تسيطر على **الأجهزة نفسها عن بُعد** (أبواب، بوابات، conveyances). تشتغل مع remote monitoring systems حتى تراقب وتتحكم وتشرف من مسافة بعيدة.

خلاصة الفرق: الأول محوره **هوية الشخص الداخل**، والثاني محوره **التحكم الفيزيائي بالبوابات والأبواب من بعيد**.

| المصطلح | شنو يدير | مكان آلية العمل |
|---|---|---|
| Remote-access monitoring | مراقبة/قياس الأجهزة فقط (بدون تحكم بالدخول) | وصول خارجي للنظام الأمني عبر نظام اتصال |
| Remote-access control | يدير **الدخول** للمناطق المحمية عبر مصادقة الهوية | نظام المصادقة بموقع **مختلف عن نقطة الدخول** |
| Remote-control access | يراقب ويتحكم ويشرف على **الأبواب والبوابات ووسائل النقل** | يشتغل مع أنظمة المراقبة عن بُعد ومن مسافة بعيدة |

### القسم 7 — Security Policy
#### ① النص الأصلي
> Documentation stating how security should be implemented at each level.
> Businesses and organizations develop comprehensive security policies that define who is authorized to access different assets and what they are allowed to do with those assets when they do access them.
> Fig. NIST SP-800-30 Risk Assessment Process.
#### ② الترجمة
> «وثائق تبيّن كيف ينبغي تنفيذ الأمن (implement security) على كل مستوى. والشركات والمؤسسات تطوّر سياسات أمنية شاملة (comprehensive security policies) تحدّد من هو المصرّح له (authorized) بالوصول إلى الأصول المختلفة (assets)، وشنو المسموح لهم يسوون بهذه الأصول عند وصولهم إليها.»
#### ③ الشرح الفهمي
تعريف قصير: سياسة الأمن = **وثائق** تقول كيف يتنفّذ الأمن على كل مستوى (level). وهي مو بس كلام، هي اللي تحدّد شيئين:
1. **من** المصرّح له يوصل للأصول (who is authorized).
2. **شنو** مسموح يسوي بهالأصول بعد ما يوصل (what they are allowed to do).

يعني السياسة تجاوب على سؤالين: مَن يقدر يدخل؟ وشنو يقدر يسوي بعد الدخول؟

### القسم 8 — Cyber Security Policy
#### ① النص الأصلي
> The company’s security policy explains the overall requirements needed to protect an organization’s network data and computer systems.
#### ② الترجمة
> «سياسة الأمن الخاصة بالشركة (company’s security policy) تشرح المتطلبات الكلية (overall requirements) اللازمة لحماية بيانات شبكة المؤسسة (network data) وأنظمة الحاسوب الخاصة بها.»
#### ③ الشرح الفهمي
هنا السياسة ترتفع من المستوى العام (documentation) إلى مستوى **الأمن السيبراني** تحديداً. السياسة تشرح **المتطلبات الكلية** اللازمة لحماية شيئين بالذات:
- **network data** ← بيانات الشبكة.
- **computer systems** ← أنظمة الحاسوب.

يعني هي الإطار العام اللي يحدّد شنو محتاجين نسوي حتى نحمي الشبكة والحواسيب من التهديدات.

### القسم 9 — Cyber Risk Assessment and Management
#### ① النص الأصلي
> Cyber Risk Assessment and Management is the process of identifying, evaluating, and mitigating the risks associated with cyber threats to an organization or system. It involves understanding the potential vulnerabilities in a system, the likelihood of cyberattacks, and the impact such attacks could have on the organization’s operations, reputation, and data security.
> Key Components:
> 1. Risk Identification: Pinpointing potential cyber threats such as malware, phishing, ransomware, data breaches, etc.
> 2. Risk Evaluation: Analyzing the likelihood of each risk materializing and the severity of its potential impact.
> 3. Risk Mitigation: Developing strategies to reduce or manage the risks. This includes implementing security controls, such as firewalls, encryption, user education, and backup systems.
> 4. Monitoring and Review: Continuously observing the cyber landscape, updating defenses, and reassessing risks as new threats emerge.
> Importance:
> - As technology advances, cyber threats become more complex, making risk management essential for protecting sensitive data and ensuring the continuity of business operations.
> - Standards and frameworks like ISO 27001, NIST Cybersecurity Framework, and country-specific guidelines (e.g., from the UK’s National Cyber Security Centre) provide structured approaches to performing risk assessments and management in cybersecurity contexts.
> By properly conducting cyber risk assessments and management, organizations can improve their resilience against attacks and better prepare for the inevitable challenges in the digital landscape.
#### ② الترجمة
> «تقييم وإدارة المخاطر السيبرانية (Cyber Risk Assessment and Management) هي العملية المتمثلة في تحديد (identifying) وتقييم (evaluating) وتخفيف (mitigating) المخاطر المرتبطة بالتهديدات السيبرانية (cyber threats) على مؤسسة أو نظام. وهي تشمل فهم الثغرات المحتملة (potential vulnerabilities) في النظام، واحتمالية وقوع الهجمات السيبرانية (likelihood of cyberattacks)، والأثر الذي قد تُحدثه هذه الهجمات على عمليات المؤسسة وسمعتها وأمن بياناتها.
> المكوّنات الأساسية (Key Components):
> 1. تحديد المخاطر (Risk Identification): تحديد التهديدات السيبرانية المحتملة مثل البرمجيات الخبيثة (malware)، والتصيّد (phishing)، وبرامج الفدية (ransomware)، وخروقات البيانات (data breaches)، وغيرها.
> 2. تقييم المخاطر (Risk Evaluation): تحليل احتمالية تحقّق كل خطر وشدّة أثره المحتمل.
> 3. تخفيف المخاطر (Risk Mitigation): تطوير استراتيجيات لتقليل المخاطر أو إدارتها. ويشمل ذلك تنفيذ ضوابط أمنية (security controls) مثل الجدران النارية (firewalls)، والتشفير (encryption)، وتوعية المستخدمين (user education)، وأنظمة النسخ الاحتياطي (backup systems).
> 4. المراقبة والمراجعة (Monitoring and Review): المراقبة المستمرة للمشهد السيبراني، وتحديث الدفاعات، وإعادة تقييم المخاطر مع ظهور تهديدات جديدة.
> الأهمية (Importance):
> - مع تقدّم التقنية، تصبح التهديدات السيبرانية أكثر تعقيداً، مما يجعل إدارة المخاطر أمراً أساسياً لحماية البيانات الحساسة وضمان استمرارية عمليات الأعمال.
> - المعايير والأطر مثل ISO 27001، وإطار NIST للأمن السيبراني (NIST Cybersecurity Framework)، والإرشادات الخاصة بكل بلد (مثل الصادرة عن المركز الوطني للأمن السيبراني في المملكة المتحدة) توفّر مناهج منظّمة لتنفيذ تقييم وإدارة المخاطر في سياقات الأمن السيبراني.
> ومن خلال تنفيذ تقييم وإدارة المخاطر السيبرانية بشكل صحيح، يمكن للمؤسسات أن تحسّن مرونتها (resilience) في مواجهة الهجمات وأن تستعد بشكل أفضل للتحديات الحتمية في المشهد الرقمي.»
#### ③ الشرح الفهمي
هاي الفقرة تعطينا تعريف كامل + مكوّنات + أهمية. التعريف يقول إنها **عملية** من ثلاث خطوات: identifying ← evaluating ← mitigating. وعشان تسوي هذا، لازم تفهم ثلاث أشياء: الثغرات المحتملة (vulnerabilities)، احتمال الهجوم (likelihood)، والأثر (impact) على العمليات والسمعة وأمن البيانات.

المكوّنات الأربعة (وهي اللي تجي مرتّبة بالجدول تحت):

| المكوّن | شنو يعني |
|---|---|
| Risk Identification | تحديد التهديدات المحتملة (malware, phishing, ransomware, data breaches…) |
| Risk Evaluation | تحليل احتمال وقوع كل خطر + شدة تأثيره |
| Risk Mitigation | تطوير استراتيجيات لتقليل/إدارة الخطر (firewalls, encryption, user education, backups) |
| Monitoring and Review | مراقبة مستمرة + تحديث الدفاعات + إعادة تقييم المخاطر مع التهديدات الجديدة |

أما **الأهمية**: مع تقدّم التقنية، التهديدات تصير أعقد ← لهذا إدارة المخاطر صارت ضرورية لحماية البيانات الحساسة وضمان استمرارية العمل. وتوجد **أطر ومعايير** جاهزة تساعدك (ISO 27001, NIST Cybersecurity Framework, وإرشادات محلية مثل UK’s National Cyber Security Centre) تعطيك منهج منظّم. والنتيجة النهائية: لو طبّقتها صح، تزيد **resilience** (المرونة/القدرة على التعافي) وتستعد للتحديات الحتمية بالمشهد الرقمي.
