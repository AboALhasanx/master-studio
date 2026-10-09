### القسم 1 — Develop a risk-management program / Use NIST security controls / The NIST Framework Stakeholders
#### ① النص الأصلي
> **Develop a risk-management program.** This breaks into three steps:
>
> - **Determine the risks** of losing control of a host.
> - **Identify potential adversarial activities** that could target your domain (e.g., are they targeting intellectual property?).
> - **Present a risk-informed report** so the organization recognizes the risks and provides support/buy-in to resolve, reduce, or prevent risks of loss.
>
> **Use NIST security controls.**
>
> - **Create a matrix** of individual concerns and associated attack vectors.
> - **Provide a mitigation method(s)** for each.
> - **Select the appropriate NIST family** (Management, Operational, Technical) of security controls to implement (reference NIST SP 800-53, tables, spreadsheets, tools).
> - **Justify the selection**: the reasons must be commensurate to the risks. Describe the low-, medium-, and high-level implementations in the guidance to ensure a cost-effective solution — and don't overprescribe controls!
>
> **The NIST Framework Stakeholders.**
>
> - **Create a policy for assessments.**
> - **Define the environment.**
> - **Determine organizational priorities** for protecting company property and materials.
> - **Ensure senior management is supportive.**
> - **Procedurally define a process and diligence** to form an informative assessment outcome.

#### ② الترجمة
> «**طوّر برنامج إدارة مخاطر (risk-management program).** وينقسم إلى ثلاث خطوات:
>
> - **حدّد المخاطر** الناتجة عن فقدان السيطرة على الـ host.
> - **حدّد الأنشطة العدائية المحتملة** اللي قد تستهدف نطاقك (domain) (مثلاً: هل يستهدفون الملكية الفكرية؟).
> - **قدّم تقريراً مبنياً على المخاطر (risk-informed)** حتى تدرك المنظمة المخاطر وتقدّم الدعم/التأييد (buy-in) لحلّها أو تقليلها أو منعها.
>
> **استخدم ضوابط أمان NIST.**
>
> - **أنشئ مصفوفة (matrix)** بالاهتمامات الفردية ومتجهات الهجوم (attack vectors) المرتبطة بها.
> - **وفّر طريقة/طرق تخفيف (mitigation)** لكل واحدة.
> - **اختر عائلة NIST المناسبة** (Management, Operational, Technical) من ضوابط الأمان اللي تحتاج تنفيذ (راجع NIST SP 800-53، والجداول، والأدوات).
> - **برّر الاختيار**: لازم تكون الأسباب متناسبة مع المخاطر. وصف التنفيذات منخفضة/متوسطة/عالية المستوى في الإرشادات لضمان حل فعّال من حيث التكلفة — ولا تفرط في وصف الضوابط!
>
> **أصحاب المصلحة في إطار عمل NIST.**
>
> - **أنشئ سياسة (policy) للتقييمات.**
> - **حدّد البيئة.**
> - **حدّد أولويات المنظمة** لحماية ممتلكات الشركة وموادها.
> - **تأكد من دعم الإدارة العليا.**
> - **حدّد إجرائياً العملية والاجتهاد** لتكوين نتيجة تقييم مفيدة وغنية بالمعلومات.»

#### ③ الشرح الفهمي
هذي ثلاث بلوكات من مصدر ثاني (مب من كتاب Sharp) تجي تحت عنوان كبير "NIST". كلها إرشادات عملية procedural — يعني "شلون تسوي"، مب "شو هو المفهوم".

| البلوك | شو يسوي |
|---|---|
| Develop a risk-management program | تبني برنامج كامل: تشوف مخاطر فقدان السيطرة على الـ host ← تحدّد الأنشطة العدائية ← تنتهي بتقرير risk-informed |
| Use NIST security controls | مصفوفة (concern ← attack vector) + mitigation لكل واحد + اختيار عائلة NIST المناسبة (Management / Operational / Technical)، والمرجع NIST SP 800-53 |
| The NIST Framework Stakeholders | policy للتقييمات، تحديد البيئة، أولويات حماية الممتلكات، دعم الإدارة العليا، وتحديد العملية الإجرائية |

> **ملاحظة مهمة (رأي الطالب من قبل):** هذي البلوكات الثلاثة تبع NIST **مب مهمة للامتحان** (NOT exam-important). هي إرشادات عملية عامة، مب مفاهيم امتحانية، فاحفظها للفهم بس ولا تضيّع وقتك عليها حفظ.

---

### القسم 2 — Security Policies
#### ① النص الأصلي
> A key component that brings all three levels of security together is a well-designed **security policy** that states how security is implemented at each level. Businesses and organizations develop comprehensive security policies that define **who is authorized** to access different assets and **what they are allowed to do** with those assets.
>
> For example, allowing employees and visitors free access to all departments inside the organization creates a variety of security risks. You want to maintain access control to reduce the human nature of temptation — if everyone can move freely inside, it is much harder to implement safeguards to prevent them from accessing or taking physical or cyber assets. You also need access control to prevent accidents.
>
> Instead, develop a **cohesive access-control policy** at each level that gives authorized people appropriate levels of access to selected assets, while inhibiting access to people who are not authorized. Then **enforce** those policies with the correct types and numbers of access-control devices (sensors, barriers, logs, ID badges, or security guards).

#### ② الترجمة
> «المكوّن الأساسي اللي يجمع مستويات الأمان الثلاثة مع بعض هو **security policy** مصمَّمة بشكل جيد، تبيّن كيف يُنفَّذ الأمان في كل مستوى. الشركات والمنظمات تطوّر سياسات أمنية شاملة تحدّد **مَن المصرَّح له** بالوصول إلى الأصول المختلفة، و**شو مسموح له يسوي** بها لما يوصلها.
>
> مثلاً، السماح للموظفين والزوار بالوصول الحر إلى كل الأقسام داخل المنظمة يخلق مخاطر أمنية متنوعة. أنت تريد تحافظ على access control لتقليل طبيعة الإنسان المتمثّلة في الإغراء (temptation) — إذا الكل يتحرك بحرية بالداخل، يصير أصعب بكثير تطبيق الضمانات (safeguards) لمنعهم من الوصول أو أخذ أصول مادية أو إلكترونية. كذلك تحتاج access control لمنع الحوادث (accidents).
>
> بدلاً من ذلك، طوّر **access-control policy متماسكة (cohesive)** عند كل مستوى، تعطي المصرَّح لهم مستويات وصول مناسبة لأصول مختارة، وتمنع وصول غير المصرَّح لهم. بعدين **افرض (enforce)** هذي السياسات بالأنواع والأعداد الصحيحة من أجهزة access-control (حساسات، حواجز، سجلات logs، شارات هوية ID badges، أو حراس أمن).»

#### ③ الشرح الفهمي
الفكرة الأساسية: الـ **security policy** هي الخيط اللي يجمع مستويات الأمان الثلاثة. تعرّف شيئين بالضبط:

| السؤال | الجواب بالـ policy |
|---|---|
| مَن المصرَّح له يوصل؟ (who) | تحديد authorized users للأصول |
| شو مسموح له يسوي؟ (what) | تحديد الصلاحيات بعد الوصول |

المثال اللي يعطيه المصدر: إذا خليت الموظفين والزوار يتحركون بحرية بكل الأقسام ← تصير مخاطر أمنية كثيرة، لأن صعب تحط safeguards. فالحل إنك تسوي **access-control policy** عند كل مستوى، وتفرضها بأجهزة مناسبة (sensors, barriers, logs, ID badges, security guards).

النقطة اللي يحب يقرها بالامتحان: الـ policy لازم تكون **cohesive** (متماسكة) و**enforced** (مفروضة) — مب بس مكتوبة على ورق.

---

### القسم 3 — Physical Security Controls
#### ① النص الأصلي
> Enforcing access-control measures may initially include placing **locks on doors** that access offices and separating departments or networking sections with similar physical barriers. Many companies have a front door or an entranceway that includes a **receptionist** to control access.
>
> The physical controls are:
>
> - **Locks and Keys**: The primary physical barrier in most security perimeters is the lockable door. The door is the physical barrier but by itself only keeps honest people out; the **lock** provides the authentication function through its key. Having the key means the person either possesses or knows the information required to gain access.
> - **Standard Key-Locking Deadbolts**: Have a locking mechanism similar to the electronic solenoid-operated deadbolt, but are engaged or withdrawn with a **key**. They add security for doors operated manually, and are available with a single or double cylinder.
> - **Solenoid-Operated Deadbolt Locks**: Electronically operated deadbolt locks offer increased security for the perimeter. Adaptable to any security system, they perform well as **auxiliary locks** on doors where access control is desired.
> - **Cipher Locks**: Require personal access codes known by the user, and are often used in access-control and management systems. They unlock magnetic door locks when the correct programmed code is entered on the cipher-lock **keypad**, adding security for perimeter entry areas.
> - **Access-Control Gates**: Like a door, a gate is a physical barrier that can be swung, drawn, or lowered to control **ingress and egress** through a wall or fence. Two main types: **sliding gates** (where high operational safety and security are needed) and **swinging gates** (with fully adjustable hinges that swing through 180 degrees).
> - **Control Relays**: Electromechanical devices that use safer **low-voltage/low-current** control signals to control **higher-voltage/higher-current** devices.

#### ② الترجمة
> «فرض إجراءات access-control قد يشمل في البداية وضع **أقفال على الأبواب** اللي تدخل على المكاتب، وفصل الأقسام أو أقسام الشبكة بحواجز مادية مشابهة. شركات كثيرة عندها باب أمامي أو مدخل يشمل **موظف استقبال (receptionist)** للسيطرة على الوصول.
>
> الضوابط المادية هي:
>
> - **الأقفال والمفاتيح (Locks and Keys)**: الحاجز المادي الأساسي في معظم محيطات الأمان (security perimeters) هو الباب القابل للإقفال. الباب هو الحاجز المادي لكن بحد ذاته بس يمنع الناس الصادقين؛ أما **القفل** فيوفّر وظيفة المصادقة (authentication) عن طريق مفتاحه. امتلاك المفتاح يعني أن الشخص إما يملك أو يعرف المعلومات المطلوبة للوصول.
> - **الأقفال المزلاجية القياسية بمفتاح (Standard Key-Locking Deadbolts)**: آلية إقفال مشابهة للقفل المزلاجي المدفوع إلكترونياً، لكنها تُفعَّل أو تُسحب بـ **مفتاح**. توفّر أماناً مضافاً للأبواب اللي تُشغَّل يدوياً، ومتوفّرة بأسطوانة واحدة أو مزدوجة (single or double cylinder).
> - **الأقفال المزلاجية المدفوعة بالـ Solenoid (Solenoid-Operated Deadbolt Locks)**: أقفال مزلاجية تُشغَّل إلكترونياً وتوفّر أماناً متزايداً للمحيط. قابلة للتكيّف مع أي نظام أمان، وتداوم بشكل جيد كـ **أقفال مساعدة (auxiliary)** على الأبواب اللي يُراد فيها access control.
> - **الأقفال الشفرية (Cipher Locks)**: تتطلب أكواد وصول شخصية يعرفها المستخدم، وتُستخدم غالباً في أنظمة access-control والإدارة. تفتح الأقفال المغناطيسية لما يُدخِل المستخدم الكود المبرمج الصحيح على **لوحة مفاتيح (keypad)** القفل الشفري، وتوفّر أماناً مضافاً لمناطق دخول المحيط.
> - **بوابات التحكم بالوصول (Access-Control Gates)**: مثل الباب، البوابة حاجز مادي يمكن أن تُفتح أو تُسحب أو تُنزَل للسيطرة على **الدخول والخروج (ingress and egress)** عبر جدار أو سياج. نوعان رئيسيان: **البوابات المنزلقة (sliding gates)** حيث تكون هناك حاجة لمستويات عالية من السلامة التشغيلية والأمان، و**البوابات المتأرجحة (swinging gates)** المجهّزة بمفصلات قابلة للتعديل بالكامل تدور 180 درجة.
> - **مرحّلات التحكم (Control Relays)**: أجهزة كهروميكانيكية (electromechanical) تستخدم إشارات تحكم أكثر أماناً بـ **جهد/تيار منخفض (low-voltage/low-current)** للتحكم بأجهزة ذات **جهد/تيار أعلى (higher-voltage/higher-current)**.»

#### ③ الشرح الفهمي
هذا القسم يتكلم عن **الطبقة المادية** (physical layer) من الأمان. الفكرة العامة: أول خط دفاع هو حواجز مادية — أبواب، أقفال، بوابات، حتى موظف استقبال. المصدر يمشي عنصر عنصر:

| العنصر | التمييز |
|---|---|
| Locks and Keys | الباب هو الحاجز المادي، لكن القفل هو اللي يوفّر وظيفة authentication عن طريق المفتاح. امتلاك المفتاح ← إما تملك أو تعرف المعلومة المطلوبة. |
| Standard Key-Locking Deadbolts | قفل مزلاجي بمفتاح، آلية مشابهة للـ solenoid لكن يُفعَّل/يُسحب بمفتاح يدوي. متوفر بأسطوانة واحدة أو مزدوجة. |
| Solenoid-Operated Deadbolt Locks | قفل مزلاجي يُشغَّل إلكترونياً، يزيد الأمان، ويتكيّف مع أي نظام أمان. يُستخدم كقفل مساعد (auxiliary). |
| Cipher Locks | تحتاج كود وصول شخصي، وتفتح الأقفال المغناطيسية لما يُدخَل الكود الصحيح على الـ keypad. |
| Access-Control Gates | حاجز مادي يُفتح/يُسحب/يُنزَل للسيطرة على ingress وegress. نوعان: Sliding gates (للسلامة والأمان العاليين) وSwinging gates (تدور 180°). |
| Control Relays | جهاز كهروميكانيكي يستخدم إشارات low-voltage/low-current للتحكم بأجهزة higher-voltage/higher-current. |

نقطة مهمة: لاحظ المصدر يفرّق بين **الباب (the door)** و**القفل (the lock)**. الباب حاجز مادي بحد ذاته، لكن القفل هو اللي يعطي وظيفة المصادقة. والباب لحاله "بس يمنع الناس الصادقين" (keep honest people out).

---

### القسم 4 — Authentication Systems
#### ① النص الأصلي
> Authentication is the process of determining that someone is who they say they are. Effective access control means being able to control the **ingress, egress, and regress** to an asset based on authorization; limiting the access of unauthorized personnel to important assets is the most fundamental security step you can take. Therefore, **authorization is based on authentication**.
>
> Multiple factors are involved in authentication:
>
> - **Knowledge**: Something you know, or something only the designated person should know.
> - **Possession**: Something you have, or something only the designated person should have.
> - **Inheritance**: Something you are, or something only the designated person is.
> - **Location**: Somewhere you are, or somewhere only the designated person is.

#### ② الترجمة
> «المصادقة (Authentication) هي عملية تحديد أن الشخص هو فعلاً مَن يدّعي أنه هو. الـ access control الفعّال يعني القدرة على السيطرة على **الدخول (ingress) والخروج (egress) والرجوع (regress)** إلى أصل (asset) بناءً على التصريح (authorization)؛ وتحديد وصول الأفراد غير المصرَّح لهم إلى الأصول المهمة هو أكثر خطوة أمنية أساسية يمكن أن تتخذها. لذلك، **الـ authorization مبني على الـ authentication**.
>
> عوامل متعددة تدخل في المصادقة:
>
> - **Knowledge (المعرفة)**: شي تعرفه، أو شي يجب أن يعرفه الشخص المعني (designated) فقط.
> - **Possession (الحيازة)**: شي تملكه، أو شي يجب أن يملكه الشخص المعني فقط.
> - **Inheritance (الوراثة)**: شي تكونه، أو شي يكونه الشخص المعني فقط.
> - **Location (الموقع)**: مكان تتواجد فيه أنت، أو مكان يتواجد فيه الشخص المعني فقط.»

#### ③ الشرح الفهمي
الفكرة: الـ **Authentication** تجيب على سؤال "هل أنت فعلاً مَن تدّعي؟". والـ **Authorization** يعتمد عليها — يعني أول تصادق (authentication)، بعدين تصرّح (authorization). والوصول لازم يسيطر على ثلاث حركات: **ingress** (الدخول)، **egress** (الخروج)، و**regress** (الرجوع).

عوامل المصادقة الأربعة:

| العامل | معناها |
|---|---|
| Knowledge | شي تعرفه — مثل password أو PIN. |
| Possession | شي تملكه — مثل بطاقة، مفتاح، أو token. |
| Inheritance | شي تكونه — خصائص جسدية/بيولوجية (biometrics). |
| Location | مكان تتواجد فيه — الموقع الجغرافي. |

> **ملاحظتان مهمتان (بصراحة):**
> 1. الكتاب مطبوع فيه **"Inheritance"**، لكن المصطلح الإنجليزي القياسي والمعتمد هو **"Inherence"** (يعني الصفة الملازمة/الجوهرية للشخص، مثل البصمة). "Inheritance" حرفياً تعني "الوراثة" وهي مب دقيقة هُنا، فانتبه للامتحان — الأرجح يقصدون Inherence.
> 2. عدد العوامل **أربعة (FOUR)، مب ثلاثة**. أحياناً الطالب ينسى واحد ويفتكرهم ثلاثة، فاحفظهم أربعة: Knowledge · Possession · Inherence · Location.
