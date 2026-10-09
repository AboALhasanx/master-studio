### القسم 1 — Develop a risk-management program / Use NIST security controls / The NIST Framework Stakeholders
#### ① النص الأصلي
> Develop a risk-management program.
> ▶Determine the risks of losing control of a host.
> ▶Identify potential adversarial activities that could target your domain
> (e.g., are they targeting intellectual property?).
> ▶Present a risk-informed report to ensure the organization recognizes
> the risks and provides support/buy-in to resolve, reduce, or prevent
> risks of loss.
> Use NIST security controls.
> ▶Create a matrix of individual concerns and associated attack vectors.
> ▶Provide a mitigation method(s) for each.
> ▶Select the appropriate NIST family (Management, Operational,
> Technical) of security controls that need to be implemented
> (Reference NIST SP 800-53, tables, spreadsheets, tools).
> ▶Ensure that the reasons for their selection are commensurate to the
> risks. The selection of low-, medium-, and high-level implementations
> should be described in the guidance and should help ensure a
> cost-effective solution. Don’t overprescribe controls!
>
> The NIST Framework Stakeholders
> Create a policy for assessments.
> ▶Define the environment.
> ▶Determine organizational priorities for protecting company property
> and materials.
> ▶Ensure senior management is supportive.
> ▶Procedurally define a process and diligence to form an informative
> assessment outcome.

#### ② الترجمة
> «طوّر برنامج إدارة مخاطر.
> ▶حدّد المخاطر الناتجة عن فقدان السيطرة على الـ host.
> ▶حدّد الأنشطة العدائية المحتملة التي قد تستهدف نطاقك (domain) (مثلاً: هل يستهدفون الملكية الفكرية؟).
> ▶قدّم تقريراً مبنياً على المخاطر (risk-informed) لضمان أن المنظمة تدرك المخاطر وتقدّم الدعم/التأييد لحلّها أو تقليلها أو منعها.
> استخدم ضوابط أمان NIST.
> ▶أنشئ مصفوفة (matrix) بالاهتمامات الفردية ومتجهات الهجوم (attack vectors) المرتبطة بها.
> ▶وفّر طريقة/طرق تخفيف (mitigation) لكل واحدة منها.
> ▶اختر عائلة NIST المناسبة (Management, Operational, Technical) من ضوابط الأمان التي تحتاج إلى تنفيذ (راجع NIST SP 800-53، والجداول، وجداول البيانات، والأدوات).
> ▶تأكد أن أسباب اختيارها متناسبة مع المخاطر. يجب وصف اختيار التنفيذات منخفضة ومتوسطة وعالية المستوى في الإرشادات، ويجب أن يساعد في ضمان حل فعّال من حيث التكلفة. لا تفرط في وصف الضوابط!
>
> أصحاب المصلحة في إطار عمل NIST
> أنشئ سياسة للتقييمات.
> ▶حدّد البيئة.
> ▶حدّد أولويات المنظمة لحماية ممتلكات الشركة وموادها.
> ▶تأكد من دعم الإدارة العليا.
> ▶حدّد إجرائياً عملية واجتهاداً لتشكيل نتيجة تقييم مُفيدة وغنية بالمعلومات.»

#### ③ الشرح الفهمي
هذي ثلاث بلوكات من مصدر تاني (مب من كتاب Sharp) تجي تحت عنوان كبير "NIST". كلها بلوكات إرشادية procedural، يعني "شلون تسوي" مب "شو هو المفهوم".

- **Develop a risk-management program:** تبني برنامج كامل لإدارة المخاطر. أول شي تشوف مخاطر فقدان السيطرة على الـ host (الجهاز/الخادم). بعدين تشوف الأنشطة العدائية المحتملة اللي تستهدف نطاقك — مثلاً إذا يستهدفون الملكية الفكرية (intellectual property). وتنتهي بتقرير risk-informed حتى الإدارة تدرك المخاطر وتعطي دعم (buy-in).
- **Use NIST security controls:** تسوي مصفوفة تربط كل concern بمتجه هجوم (attack vector)، وتحط لكل واحد طريقة mitigation. تختار عائلة الضوابط المناسبة — وNIST تقسم الضوابط لثلاث عوائل: Management وOperational وTechnical. المرجع هو NIST SP 800-53. ونقطة مهمة: لا تفرط في وصف الضوابط (Don’t overprescribe controls!).
- **The NIST Framework Stakeholders:** تدور على أصحاب المصلحة. تسوي policy للتقييمات، تحدّد البيئة، تحدّد أولويات حماية الممتلكات، تضمن دعم الإدارة العليا، وتحدّد العملية الإجرائية.

> **ملاحظة مهمة (رأي الطالب من قبل):** هذي البلوكات الثلاثة تبع NIST **مب مهمة للامتحان** (NOT exam-important). هي إرشادات عملية عامة، مب مفاهيم امتحانية، فاحفظها للفهم بس ولا تضيّع وقتك عليها حفظ.

---

### القسم 2 — Security Policies
#### ① النص الأصلي
> A key component that brings all three levels of security together is a
> welldesigned
> security policy that states how security is implemented at each level. Businesses
> and organizations develop comprehensive security policies that define who is
> authorized to access different assets and what they are allowed to do with those
> assets when they do access them.
> For example, allowing employees and visitors to have free access to all the
> departments inside the organization provides a variety of security risks. You will
> want to maintain access control to create an environment that reduces the
> human
> nature of temptation. If everyone can move freely within the interior of the
> organization, it is much more difficult to implement safeguards to prevent them
> from accessing or taking physical or cyber assets. You also need to maintain
> access control to prevent accidents.
> Instead, develop a cohesive access-control policy at each level that provides
> authorized people with appropriate levels of access to selected assets, while
> inhibiting access to assets by people who are not authorized. Then enforce those
> policies with the correct types and numbers of access-control devices (sensors,
> barriers, logs, ID badges, or security guards) as deemed appropriate.

#### ② الترجمة
> «المكوّن الأساسي الذي يجمع مستويات الأمان الثلاثة كلها مع بعض هو security policy مصمَّمة بشكل جيد، وهي تبيّن كيف يُنفَّذ الأمان في كل مستوى. الشركات والمنظمات تطوّر security policies شاملة تحدّد مَن المصرَّح له بالوصول إلى الأصول (assets) المختلفة، وشو مسموح له يسوي بهذي الأصول لما يوصلها.
> على سبيل المثال، السماح للموظفين والزوار بالوصول الحر إلى كل الأقسام داخل المنظمة يخلق مجموعة متنوعة من المخاطر الأمنية. أنت تريد تحافظ على access control حتى تسوي بيئة تقلّل من طبيعة الإنسان المتمثّلة في الإغراء (temptation). إذا كان الكل يقدر يتحرك بحرية داخل المنظمة، يصير أصعب بكثير تطبيق الضمانات (safeguards) لمنعهم من الوصول أو أخذ أصول مادية أو إلكترونية. كذلك تحتاج تحافظ على access control لمنع الحوادث (accidents).
> بدلاً من ذلك، طوّر access-control policy متماسكة عند كل مستوى تعطي الأشخاص المصرَّح لهم مستويات وصول مناسبة لأصول مختارة، وفي نفس الوقت تمنع وصول غير المصرَّح لهم إلى الأصول. بعدين فرض هذي السياسات بالأنواع والأعداد الصحيحة من أجهزة access-control (حساسات، حواجز، سجلات logs، شارات هوية ID badges، أو حراس أمن) حسب ما يُرى مناسباً.»

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
> Enforcing access-control measures may initially include placing locks on doors
> that access offices and separating departments or networking sections with
> similar physical barriers. Many companies have a front door or an entranceway
> that includes a receptionist to control access.
> Fig. Physical Barriers
> Locks and Keys
> The primary physical barrier in most security perimeters is the lockable door.
> The door provides the physical barrier but in itself will only keep honest people
> out. The lock, on the other hand, provides the authentication function of the
> barrier through its key. Having the key signifies that the person either possesses
> or knows the information required to gain access through the door.
> Standard Key-Locking Deadbolts
> Standard key-locking deadbolts have a locking mechanism similar to that of the
> electronic solenoid-operated deadbolt but are engaged or withdrawn with a key.
> They provide an added level of security for doors that can be operated manually.
> A key-locking deadbolt is available with a single or double cylinder.
> Solenoid-Operated Deadbolt Locks
> Electronically operated deadbolt locks offer an increased level of security for
> the perimeter. Adaptable to any security system, electric deadbolts perform well
> as auxiliary locks on doors where access control is desired.
> Cipher Locks
> Cipher locks requiring personal access codes known by the user are often used
> in access-control and management systems. These locks operate by unlocking
> magnetic door locks when the correct programmed code is entered by the user
> on the cipher-lock keypad. They provide an added level of security for
> perimeter entry areas. An example of a cipher lock
> Fig. Cipher Lock
> Access-Control Gates
> Like a door, a gate is a type of physical barrier that can be swung, drawn, or
> lowered to control ingress and egress through a wall or fence. Access-control
> gates can be classified into two main types:
> ▶Sliding gates: are used where high levels of operational safety and security
> are needed.
> Fig. Sliding Gate
> ▶Swinging gates: are equipped with fully adjustable hinges that allow the gate
> to swing through 180 degrees.
> Fig. Swinging Gate
> Control Relays
> Relays are electromechanical devices that employ safer, low-voltage/low-
> current control signals to be used to control higher-voltage/higher-current
> devices.

#### ② الترجمة
> «فرض إجراءات access-control قد يشمل في البداية وضع أقفال على الأبواب اللي تدخل على المكاتب، وفصل الأقسام أو أقسام الشبكة بحواجز مادية مشابهة. شركات كثيرة عندها باب أمامي أو مدخل يشمل موظف استقبال (receptionist) للسيطرة على الوصول.
> Fig. حواجز مادية (Physical Barriers)
> الأقفال والمفاتيح (Locks and Keys)
> الحاجز المادي الأساسي في معظم محيطات الأمان (security perimeters) هو الباب القابل للإقفال. الباب يوفّر الحاجز المادي لكن بحد ذاته بس يمنع الناس الصادقين. أما القفل، من ناحية ثانية، يوفّر وظيفة المصادقة (authentication) للحاجز عن طريق مفتاحه. امتلاك المفتاح يعني أن الشخص إما يملك أو يعرف المعلومات المطلوبة للوصول عبر الباب.
> الأقفال المزلاجية القياسية بمفتاح (Standard Key-Locking Deadbolts)
> الأقفال المزلاجية القياسية بمفتاح عندها آلية إقفال مشابهة للقفل المزلاجي المدفوع إلكترونياً (electronic solenoid-operated deadbolt)، لكنها تُفعَّل أو تُسحب بمفتاح. توفر مستوى أمان مضافاً للأبواب اللي تُشغَّل يدوياً. القفل المزلاجي بالمفتاح متوفّر بأسطوانة واحدة أو مزدوجة (single or double cylinder).
> الأقفال المزلاجية المدفوعة بالـ Solenoid
> الأقفال المزلاجية المدفوعة إلكترونياً توفّر مستوى أمان متزايداً للمحيط. قابلة للتكيّف مع أي نظام أمان، والأقفال الكهربائية المزلاجية تداوم بشكل جيد كأقفال مساعدة (auxiliary) على الأبواب اللي يُراد فيها access control.
> الأقفال الشفرية (Cipher Locks)
> الأقفال الشفرية اللي تتطلب أكواد وصول شخصية يعرفها المستخدم تُستخدم غالباً في أنظمة access-control والإدارة. هذي الأقفال تعمل بفتح الأقفال المغناطيسية للأبواب لما يُدخِل المستخدم الكود المبرمج الصحيح على لوحة مفاتيح القفل الشفري. توفر مستوى أمان مضافاً لمناطق دخول المحيط. مثال على قفل شفري
> Fig. قفل شفري (Cipher Lock)
> بوابات التحكم بالوصول (Access-Control Gates)
> مثل الباب، البوابة هي نوع من الحاجز المادي اللي يمكن أن تُفتح أو تُسحب أو تُنزَل للسيطرة على الدخول والخروج (ingress and egress) عبر جدار أو سياج. بوابات access-control يمكن تصنيفها إلى نوعين رئيسيين:
> ▶البوابات المنزلقة (Sliding gates): تُستخدم حيث تكون هناك حاجة لمستويات عالية من السلامة التشغيلية والأمان.
> Fig. بوابة منزلقة (Sliding Gate)
> ▶البوابات المتأرجحة (Swinging gates): مجهّزة بمفصلات (hinges) قابلة للتعديل بالكامل تسمح للبوابة أن تتأرجح بزاوية 180 درجة.
> Fig. بوابة متأرجحة (Swinging Gate)
> مرحّلات التحكم (Control Relays)
> الـ Relays هي أجهزة كهروميكانيكية (electromechanical) تستخدم إشارات تحكم أكثر أماناً بجهد/تيار منخفض (low-voltage/low-current) للتحكم بأجهزة ذات جهد/تيار أعلى (higher-voltage/higher-current).»

#### ③ الشرح الفهمي
هذا القسم يتكلم عن **الطبقة المادية** (physical layer) من الأمان. الفكرة العامة: أول خط دفاع هو حواجز مادية — أبواب، أقفال، بوابات، حتى موظف استقبال. المصدر يمشي عنصر عنصر:

| العنصر | التمييز |
|---|---|
| Locks and Keys | الباب هو الحاجز المادي، لكن القفل هو اللي يوفّر وظيفة authentication عن طريق المفتاح. امتلاك المفتاح ← يعني إما تملك أو تعرف المعلومة المطلوبة. |
| Standard Key-Locking Deadbolts | قفل مزلاجي بمفتاح، آلية مشابهة للـ solenoid لكن يُفعَّل/يُسحب بمفتاح يدوي. متوفر بأسطوانة واحدة أو مزدوجة. |
| Solenoid-Operated Deadbolt Locks | قفل مزلاجي يُشغَّل إلكترونياً، يزيد الأمان، ويتكيّف مع أي نظام أمان. يُستخدم كقفل مساعد (auxiliary). |
| Cipher Locks | تحتاج كود وصول شخصي. تفتح الأقفال المغناطيسية لما يُدخَل الكود الصحيح على لوحة المفاتيح (keypad). |
| Access-Control Gates | نوع من الحاجز المادي يُفتح/يُسحب/يُنزَل للسيطرة على ingress وegress. نوعان: Sliding gates (للسلامة والأمان العاليين) وSwinging gates (مفصلات قابلة للتعديل تدور 180°). |
| Control Relays | جهاز كهروميكانيكي يستخدم إشارات تحكم low-voltage/low-current للتحكم بأجهزة higher-voltage/higher-current. |

نقطة مهمة: لاحظ المصدر يفرّق بين **الباب (the door)** و**القفل (the lock)**. الباب حاجز مادي بحد ذاته، لكن القفل هو اللي يعطي وظيفة المصادقة. والباب لحاله "بس يمنع الناس الصادقين" (keep honest people out).

---

### القسم 4 — Authentication Systems
#### ① النص الأصلي
> Authentication is the process of determining that someone is who they say they
> are. Recall that effective access control involves being able to control the
> ingress,
> egress, and regress to an asset based on authorization. In particular, limiting the
> access of unauthorized personnel to important assets is the most fundamental
> security step that you can take. Therefore, authorization is based on
> authentication.
> Multiple factors are involved in authentication:
> ▶Knowledge: Something you know or something that only the designated
> person should know.
> ▶Possession: Something you have or something that only the designated
> person should have.
> ▶Inheritance: Something you are or something that only the designated
> person is.
> ▶Location: Somewhere you are or somewhere that only the designated person
> is.

#### ② الترجمة
> «المصادقة (Authentication) هي عملية تحديد أن الشخص هو فعلاً مَن يدّعي أنه هو. تذكّر أن access control الفعّال يتضمن القدرة على السيطرة على الدخول (ingress) والخروج (egress) والرجوع (regress) إلى أصل (asset) بناءً على التصريح (authorization). بشكل خاص، تحديد وصول الأفراد غير المصرَّح لهم إلى الأصول المهمة هو أكثر خطوة أمنية أساسية يمكن أن تتخذها. لذلك، الـ authorization مبني على الـ authentication.
> عوامل متعددة تدخل في المصادقة:
> ▶Knowledge (المعرفة): شي تعرفه، أو شي يجب أن يعرفه الشخص المعني (designated) فقط.
> ▶Possession (الحيازة): شي تملكه، أو شي يجب أن يملكه الشخص المعني فقط.
> ▶Inheritance (الوراثة): شي أنت تكونه، أو شي يكونه الشخص المعني فقط.
> ▶Location (الموقع): مكان تتواجد فيه أنت، أو مكان يتواجد فيه الشخص المعني فقط.»

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
