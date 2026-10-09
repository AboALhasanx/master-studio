### القسم 1 — Threats in IT Systems
#### ① النص الأصلي
> Many IT users believe mistakenly that the only threat which can prevent the correct operation of their computers is attackers who hack their way into the computer. In reality, the threat pattern is much more varied, and the threats can be related to many different aspects of the computer's operation. We can distinguish between at least four main groups of threats:
>
> - **Hardware related threats**: threats which physically affect the computer itself or the infrastructure on which it depends in order to work as required — harmful surroundings, natural disasters such as storms, physical attacks such as theft, and faults in the infrastructure.
> - **Software related threats**: threats which affect the installed software (applications and the operating system) or which are due to poorly designed or wilfully malicious programs coming from outside — unauthorized modification or deletion of software; wilfully malicious programs (so-called malware) such as viruses, worms, trojan horses and logic bombs; use of poorly designed programs which contain vulnerabilities; use of incorrect or out-of-date software versions; theft or unauthorized copying of software.
> - **Data related threats**: threats which can lead to unauthorized processing (including storage) of data in any way — unwanted storage, modification, disclosure or deletion of data; Inference, that is, collecting accessible data from which it is possible to deduce confidential information which is not directly accessible; "Masquerading" (i.e. pretending to be someone else) and unauthorized access.
> - **Liveware related threats**: threats which are related to human error among the computer's users — social engineering and phishing, as well as IT fraud, forgery and other forms of criminality now carried out with the help of computers.
#### ② الترجمة
> «يعتقد كثير من مستخدمي الـ IT خطأً أن التهديد الوحيد الذي يمكن أن يمنع التشغيل الصحيح لأجهزتهم هو المهاجمون الذين يخترقون الحاسوب. في الواقع، نمط التهديدات أكثر تنوّعًا بكثير، ويمكن أن ترتبط التهديدات بجوانب مختلفة عديدة من عمل الحاسوب. ويمكننا التمييز بين أربع مجموعات رئيسية على الأقل من التهديدات:
>
> - **تهديدات متعلقة بالـ Hardware**: تهديدات تؤثّر فيزيائيًا على الحاسوب نفسه أو على البنية التحتية التي يعتمد عليها ليعمل كما هو مطلوب — بيئة ضارّة، وكوارث طبيعية كالعواصف، وهجمات فيزيائية كالسرقة، وأعطال في البنية التحتية.
> - **تهديدات متعلقة بالـ Software**: تهديدات تؤثّر على البرمجيات المثبّتة (التطبيقات ونظام التشغيل)، أو تكون ناتجة عن برامج مصمَّمة بشكل سيّئ أو خبيثة عن قصد قادمة من الخارج — التعديل أو الحذف غير المصرّح به للبرمجيات؛ والبرامج الخبيثة عن قصد (malware) كالفيروسات والـ worms وأحصنة طروادة والقنابل المنطقية (logic bombs)؛ واستخدام برامج مصمَّمة بشكل سيّئ تحتوي ثغرات؛ واستخدام إصدارات برمجية خاطئة أو قديمة؛ وسرقة البرمجيات أو نسخها دون تصريح.
> - **تهديدات متعلقة بالبيانات (Data)**: تهديدات يمكن أن تؤدي إلى معالجة غير مصرّح بها (بما فيها التخزين) للبيانات بأي طريقة — التخزين أو التعديل أو الإفشاء أو الحذف غير المرغوب فيه للبيانات؛ والاستنتاج (Inference)، أي جمع بيانات متاحة يمكن منها استنتاج معلومات سرية غير متاحة مباشرة؛ و"التنكّر" (Masquerading) أي التظاهر بأنك شخص آخر، والوصول غير المصرّح به.
> - **تهديدات متعلقة بالبشر (Liveware)**: تهديدات مرتبطة بالخطأ البشري عند مستخدمي الحاسوب — الهندسة الاجتماعية (social engineering) والتصيّد (phishing)، إضافة إلى الاحتيال المعلوماتي (IT fraud) والتزوير (forgery) وأشكال أخرى من الجريمة تُنفَّذ الآن بمساعدة الحاسوب.»
#### ③ الشرح الفهمي
هذا القسم يصحّح فكرة غلط شائعة: المستخدم يظن إن الخطر الوحيد هو "الهاكر اللي يخترق الكومبيوتر". المصدر يقول إن نمط التهديدات أوسع بكثير، ويقسّمها لأربع مجموعات رئيسية على الأقل. مفتاح الحفظ: كل مجموعة ترتبط بجزء معيّن من منظومة الكومبيوتر ← الـ hardware، الـ software، الداتا، والبشر (liveware).

| المجموعة | مصدرها | أمثلة |
|---|---|---|
| Hardware related threats | الشي الفيزيائي: الكومبيوتر نفسه أو البنية التحتية اللي يعتمد عليها | بيئة مؤذية (harmful surroundings)، كوارث طبيعية كالعواصف، هجمات فيزيائية كالسرقة، أعطال في البنية التحتية |
| Software related threats | السوفتوير المثبّت (تطبيقات + نظام تشغيل) أو برامج جاية من الخارج مصمّمة بشكل سيئ/خبيثة | تعديل أو حذف غير مصرّح به، malware (فيروسات، worms، trojan horses، logic bombs)، برامج فيها ثغرات، إصدارات خاطئة أو قديمة، سرقة/نسخ السوفتوير |
| Data related threats | البيانات نفسها: أي معالجة (بما فيها التخزين) غير مصرّح بها | تخزين/تعديل/إفشاء/حذف غير مرغوب فيه، Inference (استنتاج معلومة سرية من بيانات متاحة)، Masquerading (تنكّر) ووصول غير مصرّح به |
| Liveware related threats | الخطأ البشري عند المستخدمين | social engineering و phishing، الاحتيال المعلوماتي (IT fraud)، التزوير (forgery) وأشكال جريمة أخرى بمساعدة الكومبيوتر |

ملاحظة مهمة للحفظ: مجموعة الـ Data فيها تهديدين مذكورين بالاسم — الـ **Inference** (استنتاج معلومة سرية من بيانات متاحة بدون وصول مباشر إلها) والـ **Masquerading** (التنكّر بشخصية غيرك). ومجموعة الـ Liveware تربط الخطر بسلوك البشر لا بالجهاز ← يعني حتى لو الأجهزة كلها سليمة، الخطأ البشري يبقى ثغرة.

---

### القسم 2 — Countermeasures
#### ① النص الأصلي
> A threat is blocked by control of a vulnerability with the help of suitable countermeasures, which must of course be adapted to suit the type of threat. For example, but not limited:
>
> - **Threats from attackers outside the system who attack through the Internet**: use firewalls in the network, in order to prevent traffic from the attacker reaching the target.
> - **Threats from malware**: use antivirus programs and other so-called security programs.
> - **Threats such as vandalism, theft and other physical damage to the equipment**: place the equipment in a secure room.
> - **Threats such as unauthorized modification or deletion of data or software**: take regular backup copies.
> - **Threats such as unauthorized access to data**: use encryption or access control.
> - **Threats from personnel and ordinary authorized users**: check personnel and introduce suitable training.
#### ② الترجمة
> «التهديد يُسدّ من خلال السيطرة على ثغرة (vulnerability) بمساعدة تدابير مضادة (countermeasures) مناسبة، وهذه بطبيعة الحال يجب أن تُكيَّف بما يناسب نوع التهديد. على سبيل المثال، وليس على سبيل الحصر:
>
> - **تهديدات من مهاجمين خارج النظام يهاجمون عبر الإنترنت**: استخدام جدران الحماية (firewalls) في الشبكة، لمنع حركة المرور الصادرة من المهاجم من الوصول إلى الهدف.
> - **تهديدات من الـ malware**: استخدام برامج مكافحة الفيروسات (antivirus) وبرامج أمنية أخرى تُسمّى كذلك.
> - **تهديدات مثل التخريب (vandalism) والسرقة وأي ضرر فيزيائي آخر على المعدات**: وضع المعدات في غرفة آمنة (secure room).
> - **تهديدات مثل التعديل أو الحذف غير المصرّح به للبيانات أو البرمجيات**: أخذ نسخ احتياطية منتظمة (backup copies).
> - **تهديدات مثل الوصول غير المصرّح به إلى البيانات**: استخدام التشفير (encryption) أو التحكم بالوصول (access control).
> - **تهديدات من الموظفين والمستخدمين المصرّح لهم العاديين**: فحص الموظفين وإدخال تدريب مناسب.»
#### ③ الشرح الفهمي
الفكرة الأساسية هنا: ما تقدر تحمي شي بدون ما تعرف نوع التهديد. كل تهديد ← إله تدبير مضاد (countermeasure) يناسبه، يعني التدبير ما يكون عام، يكون مكيّف حسب التهديد. المصدر يعطينا ست حالات ويقول "مثلاً بس مو محصور" ← يعني هذي أمثلة مو قائمة كاملة.

| التهديد | التدبير |
|---|---|
| مهاجمون خارج النظام يهاجمون عبر الإنترنت | استخدام firewalls في الشبكة لمنع وصول الترافيك للمهاجم للهدف |
| البرامج الخبيثة (malware) | استخدام برامج antivirus وبرامج أمنية أخرى |
| التخريب (vandalism)، السرقة، والضرر الفيزيائي للمعدات | وضع المعدات في غرفة آمنة (secure room) |
| تعديل أو حذف غير مصرّح به للبيانات أو السوفتوير | أخذ نسخ احتياطية منتظمة (regular backups) |
| وصول غير مصرّح به للبيانات | استخدام encryption أو access control |
| تهديدات من الموظفين والمستخدمين المصرّح لهم العاديين | فحص الموظفين (personnel checks) وإدخال تدريب مناسب (training) |

نقطة تربطها بالوضع العملي: لاحظ إن التدابير هنا موزّعة على نفس مجموعات القسم الأول تقريباً — فيزائي (غرفة آمنة)، سوفتوير (antivirus)، داتا (backup + encryption/access control)، وبشر (فحص وتدريب). يعني الحماية ما تكون من جهة وحدة ← لازم تغطّي كل المجموعات.
