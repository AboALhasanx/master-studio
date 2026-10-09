### القسم 1 — 1. Introduction

#### ① النص الأصلي

> Cybersecurity relies not only on encrypting information for confidentiality but also on ensuring integrity, authenticity, and trust. Encryption hides data, but organizations also need to confirm:
>
> 1. Has the data been modified? (Integrity)
> 2. Who created or sent the data? (Authenticity)
> 3. Can the sender later deny involvement? (Non-repudiation)
> 4. Can we trust the identity behind a key? (Trust assurance)
>
> These needs are met through hash functions, digital signatures, and digital certificates. Together, they form the backbone of secure Internet protocols, enabling banking, e-commerce, digital government, and blockchain ecosystems.

#### ② الترجمة

> «الأمن السيبراني ما يعتمد بس على تشفير المعلومات من أجل السرية (confidentiality)، بل كذلك على ضمان السلامة (integrity) والأصالة (authenticity) والثقة (trust). التشفير يخفي البيانات، بس المؤسسات كذلك تحتاج تأكّد:
>
> 1. هل البيانات تغيّرت؟ (السلامة ← Integrity)
> 2. منو أنشأ أو أرسل البيانات؟ (الأصالة ← Authenticity)
> 3. هل يمكن للمرسل لاحقًا ينكر التورط؟ (عدم الإنكار ← Non-repudiation)
> 4. هل نكدر نثق بالهوية اللي وراء المفتاح؟ (ضمان الثقة ← Trust assurance)
>
> هذي الاحتياجات تتحقّق عبر دوال الهاش (hash functions)، والتواقيع الرقمية (digital signatures)، والشهادات الرقمية (digital certificates). ومجتمعة تشكّل العمود الفقري لبروتوكولات الإنترنت الآمنة، وتُمكّن المصارف والتجارة الإلكترونية والحكومة الرقمية وأنظمة الـ blockchain.»

#### ③ الشرح الفهمي

الفكرة الأساسية: التشفير لحاله ما يكفي. التشفير يعطيك **confidentiality** (يخفي البيانات)، بس الأمن الكامل يحتاج أربعة أشياء غير — وهذا القسم يمهّد لهن قبل ما يدخل بالتقنيات.

| الحاجة | السؤال اللي تجاوب عليه | التقنية اللي تحققها |
|---|---|---|
| **Integrity** (السلامة) | هل البيانات تغيّرت؟ | Hash Functions |
| **Authenticity** (الأصالة) | منو أنشأ أو أرسل البيانات؟ | Digital Signatures |
| **Non-repudiation** (عدم الإنكار) | هل المرسل يمكن ينكر؟ | Digital Signatures |
| **Trust assurance** (ضمان الثقة) | هل نثق بالهوية وراء المفتاح؟ | Digital Certificates / PKI |

خلاصة تربط كل شي: **Hashing** يضمن السلامة، **Digital Signatures** يضمنون الأصالة وعدم الإنكار، و**Certificates/PKI** يعطونك الثقة بالهوية. وهذي الثلاثة مجتمعة هي أساس كل بروتوكول إنترنت آمن — من المصارف والتجارة الإلكترونية للحكومة الرقمية والـ blockchain.

---

### القسم 2 — 2. Hash Functions

#### ① النص الأصلي

> **2.1 Definition.** A hash function is a mathematical transformation that maps input data of arbitrary size to a fixed-size output, called a hash or digest.
>
> Where:
>
> - Input: any message of arbitrary length.
> - Output: fixed-length $n$-bit digest.
>
> **2.2 Properties of a Secure Hash**
>
> 1. Deterministic: same input → same output.
> 2. Pre-image resistance: hard to find $x$ given $h(x)$.
> 3. Second pre-image resistance: hard to find $y \neq x$ with $h(y) = h(x)$.
> 4. Collision resistance: hard to find any two inputs $x, y$ where $h(x) = h(y)$.
> 5. Avalanche effect: small input change → drastically different output.
>
> **2.3 Mathematical Property.** $h(x) \neq h(y)$ if $x \neq y$. This idealized property reflects collision resistance. In practice, collisions are inevitable due to the pigeonhole principle, but a good hash makes them computationally infeasible.
>
> **2.4 Algorithms**
>
> - SHA-256 (SHA-2 family): 256-bit output, standard in blockchain, TLS, and certificates.
> - SHA-3 (Keccak): sponge construction, resistant to length extension attacks.
> - Insecure algorithms: MD5 and SHA-1, both broken by practical collisions.
>
> **2.5 Cybersecurity Use Cases**
>
> **1. Password Storage.** Instead of storing plaintext passwords, systems store hashes; users' input passwords are hashed and compared to stored values. With salts (random values appended before hashing), attacks using rainbow tables are mitigated.
>
> Example:
>
> - Input: "password123"
> - SHA-256 digest: `ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f`
>
> **2. File Integrity Verification.** Software updates are distributed with hash values; users recompute the hash to verify no tampering occurred during download.
>
> **3. Blockchain Security.** Bitcoin blocks use SHA-256 hashes of previous blocks, ensuring immutability; tampering with one block alters all subsequent blocks, making fraud evident.

$$h : \{0,1\}^{*} \rightarrow \{0,1\}^{n}$$

$$h(x) \neq h(y) \quad \text{if} \quad x \neq y$$

#### ② الترجمة

> «**2.1 التعريف (Definition).** دالة الهاش هي تحويل رياضي يربط بيانات إدخال بحجم اعتباطي (arbitrary size) بمخرج بحجم ثابت، يُسمّى hash أو digest.
>
> حيث:
>
> - الإدخال (Input): أي رسالة بطول اعتباطي.
> - الإخراج (Output): digest بطول ثابت $n$ بت.
>
> **2.2 خصائص الهاش الآمن (Properties of a Secure Hash)**
>
> 1. حتمية (Deterministic): نفس الإدخال ← نفس الإخراج.
> 2. مقاومة الصورة الأصلية (Pre-image resistance): يصعب إيجاد $x$ إذا عندك $h(x)$.
> 3. مقاومة الصورة الأصلية الثانية (Second pre-image resistance): يصعب إيجاد $y \neq x$ بحيث $h(y) = h(x)$.
> 4. مقاومة التصادم (Collision resistance): يصعب إيجاد أي مدخلين $x, y$ بحيث $h(x) = h(y)$.
> 5. تأثير الانهيار الجليدي (Avalanche effect): تغيير صغير بالإدخال ← مخرج مختلف جذريًا.
>
> **2.3 الخاصية الرياضية (Mathematical Property).** $h(x) \neq h(y)$ إذا $x \neq y$. هذي خاصية مثالية تعكس مقاومة التصادم. عمليًا، التصادمات حتمية بسبب مبدأ الحمّام (pigeonhole principle)، بس الهاش الجيد يخليها غير مجدية حسابيًا.
>
> **2.4 الخوارزميات (Algorithms)**
>
> - SHA-256 (عائلة SHA-2): مخرج 256 بت، معيارية بالـ blockchain و TLS والشهادات.
> - SHA-3 (Keccak): بنية إسفنجية (sponge construction)، مقاومة لهجمات تمديد الطول (length extension attacks).
> - خوارزميات غير آمنة (Insecure): MD5 و SHA-1، الاثنين مكسورين بتصادمات عملية.
>
> **2.5 حالات الاستخدام في الأمن السيبراني (Cybersecurity Use Cases)**
>
> **1. تخزين كلمات المرور (Password Storage).** بدل ما تخزّن كلمات المرور نص صريح، الأنظمة تخزّن هاشات؛ كلمة مرور المستخدم تُهشَّش وتُقارن بالقيمة المخزّنة. ومع الـ salts (قيم عشوائية تُضاف قبل الهاش)، تُخفَّف الهجمات اللي تستخدم جداول القوس قزح (rainbow tables).
>
> مثال:
>
> - الإدخال: "password123"
> - digest الـ SHA-256: `ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f`
>
> **2. التحقق من سلامة الملفات (File Integrity Verification).** تحديثات البرامج تُوزَّع مع قيم هاش؛ والمستخدمون يعيدون حساب الهاش للتأكد إن ما صار تلاعب أثناء التنزيل.
>
> **3. أمن الـ Blockchain (Blockchain Security).** كتل البيتكوين تستخدم هاشات SHA-256 للكتل السابقة، مما يضمن عدم القابلية للتغيير (immutability)؛ والتلاعب بكتلة واحدة يغيّر كل الكتل اللي بعدها، فيصير الغش واضحًا.»

#### ③ الشرح الفهمي

الفكرة: دالة الهاش تشبه "بصمة" للبيانات. تاخذ أي شي — رسالة قصيرة أو ملف ضخم — وتطلّع منه سلسلة ثابتة الطول. أهم شي: **ما ترجع للوراء** (one-way)، يعني ما تكدر تستخرج النص الأصلي من الهاش.

**ملاحظة صادقة عن رموز الإدخال/الإخراج:** النص الأصلي يكتب مخرج الهاش `{0,1}*` للإدخال و `{0,1}^n` للإخراج. معنى `{0,1}*` = أي سلسلة بتات بأي طول (الـ `*` تعني "صفر أو أكثر")، وهذا دومين الإدخال (رسالة اعتباطية الطول). ومعنى `{0,1}^n` = سلسلة بتات بطول $n$ بت بالضبط، وهذا الـ digest ثابت الطول.

$$h : \{0,1\}^{*} \rightarrow \{0,1\}^{n}$$

يعني: الهاش دالة تاخذ **أي طول** وتطلّع **طول ثابت $n$**.

| الخاصية | شنو تعني بكلام بسيط |
|---|---|
| Deterministic | نفس الشي داخل ← نفس الشي خارج، دايمًا |
| Pre-image resistance | ما تكدر ترجع من الهاش للنص الأصلي |
| Second pre-image resistance | ما تكدر تطلّع رسالة ثانية تعطي نفس الهاش لنفس الرسالة |
| Collision resistance | ما تكدر تطلّع أي رسالتين مختلفتين تعطون نفس الهاش |
| Avalanche effect | تغيّر حرف واحد ← الهاش يتغير بالكامل |

**نقطة الرياضيات:** نظريًا الهاش يفترض `h(x) ≠ h(y)` إذا `x ≠ y` (يعني ما يصير تصادم). بس بسبب **pigeonhole principle** — عدد المدخلات اللانهائي مقابل عدد المخارج المحدود ($2^n$) — التصادمات **لا بد تصير** رياضيًا. الشغل الحقيقي مو "منع التصادم"، بل **خليه غير مجدي حسابيًا** (computationally infeasible).

$$h(x) \neq h(y) \quad \text{if} \quad x \neq y$$

**الخوارزميات:** SHA-256 (معيار البيتكوين و TLS)، SHA-3 (Keccak، يختلف بالبنية الإسفنجية ويقاوم length-extension attacks). أما **MD5 و SHA-1 فهما مكسورين** — صارت عليهن تصادمات عملية، فلا تُستخدم.

**حالات الاستخدام:**
- **Password Storage:** النظام ما يخزّن كلمة المرور، يخزّن الهاش. الـ **salt** = قيمة عشوائية تُضاف قبل الهاش، حتى لو مستخدمان عندهما نفس كلمة المرور يطلع هاش مختلف، وتُبطَل جداول الـ rainbow tables.
- **File Integrity:** عندك ملف تحديث؟ تاخذ الـ hash الرسمي وتقارنه بالهاش اللي حسبته — إذا اختلف، معناه الملف تلاعبوا بيه.
- **Blockchain:** كل كتلة تحمل هاش الكتلة اللي قبلها ← سلسلة؛ تغيّر كتلة واحدة ← كل الكتل بعدها تتغير، فالغش يصير مكشوف.

مثال تحفظه: `"password123"` ← الـ SHA-256 digest يبدأ بـ `ef92b778...`.

---

### القسم 3 — 3. Digital Signatures

#### ① النص الأصلي

> **3.1 Purpose.** While hashes provide integrity, they cannot confirm who created the data. For this, cybersecurity employs digital signatures, which bind identity to data using asymmetric cryptography. Digital signatures guarantee:
>
> - Integrity (data unaltered).
> - Authenticity (verifies sender identity).
> - Non-repudiation (sender cannot deny creating it).
>
> **3.2 Process**
>
> 1. Sender computes hash of message $M$: $h(M)$.
> 2. Sender encrypts hash with private key: $Sig = E_{Priv}(h(M))$.
> 3. Receiver decrypts signature with sender's public key and compares: $h(M) \stackrel{?}{=} D_{Pub}(Sig)$.
>
> If equal, the signature is valid.
>
> **3.3 Algorithms**
>
> - RSA Signatures: based on RSA encryption with private/public key.
> - DSA (Digital Signature Algorithm): U.S. Federal standard.
> - ECDSA (Elliptic Curve DSA): stronger security with smaller keys, used in Bitcoin and modern web services.
>
> **3.4 Cybersecurity Use Cases**
>
> 1. Software Distribution: operating systems digitally sign updates; users verify signatures before installation.
> 2. Secure Email (S/MIME, PGP): ensures emails truly come from the claimed sender.
> 3. Blockchain Transactions: Bitcoin uses ECDSA signatures to prove coin ownership.
> 4. Digital Contracts: legally binding e-signatures rely on digital signatures.
>
> **3.5 Attacks and Weaknesses**
>
> - Private key theft: if an attacker gains the private key, they can forge signatures.
> - Weak hash usage: if MD5 or SHA-1 is used, collisions allow forged signatures.
> - Implementation flaws: side-channel attacks (timing, power) can leak private keys.

$$Sig = E_{Priv}\big(h(M)\big)$$

$$\text{verify: } h(M) \stackrel{?}{=} D_{Pub}(Sig)$$

#### ② الترجمة

> «**3.1 الغرض (Purpose).** بينما الهاش يوفّر السلامة، ما يكدر يأكّد منو أنشأ البيانات. لهذا السبب يستخدم الأمن السيبراني التواقيع الرقمية (digital signatures)، اللي تربط الهوية بالبيانات باستخدام التشفير غير المتماثل (asymmetric cryptography). التواقيع الرقمية تضمن:
>
> - السلامة (Integrity): البيانات ما تغيّرت.
> - الأصالة (Authenticity): تتحقق من هوية المرسل.
> - عدم الإنكار (Non-repudiation): المرسل ما يكدر ينكر إنه أنشأها.
>
> **3.2 العملية (Process)**
>
> 1. المرسل يحسب هاش الرسالة $M$: $h(M)$.
> 2. المرسل يشفّر الهاش بالمفتاح الخاص: $Sig = E_{Priv}(h(M))$.
> 3. المستقبل يفكّ التوقيع بالمفتاح العام للمرسل ويقارن: $h(M) \stackrel{?}{=} D_{Pub}(Sig)$.
>
> إذا تساوَوا، فالتوقيع صحيح.
>
> **3.3 الخوارزميات (Algorithms)**
>
> - تواقيع RSA: مبنية على تشفير RSA بالمفتاح الخاص/العام.
> - DSA (خوارزمية التوقيع الرقمي): معيار فدرالي أمريكي.
> - ECDSA (توقيع المنحنى البيضوي): أمان أقوى بمفاتيح أصغر، تُستخدم في البيتكوين والخدمات الحديثة.
>
> **3.4 حالات الاستخدام في الأمن السيبراني (Cybersecurity Use Cases)**
>
> 1. توزيع البرامج (Software Distribution): أنظمة التشغيل توقّع التحديثات رقميًا؛ والمستخدمون يتحققون من التواقيع قبل التنصيب.
> 2. البريد الآمن (Secure Email — S/MIME, PGP): يضمن إن الإيميلات فعلاً تجي من المرسل المعلن.
> 3. معاملات الـ Blockchain: البيتكوين يستخدم تواقيع ECDSA لإثبات ملكية العملة.
> 4. العقود الرقمية (Digital Contracts): التواقيع الإلكترونية الملزمة قانونيًا تعتمد على التواقيع الرقمية.
>
> **3.5 الهجمات ونقاط الضعف (Attacks and Weaknesses)**
>
> - سرقة المفتاح الخاص (Private key theft): إذا حصل المهاجم على المفتاح الخاص، يكدر يزوّر التواقيع.
> - استخدام هاش ضعيف (Weak hash usage): إذا استُخدم MD5 أو SHA-1، فالتصادمات تسمح بتواقيع مزوّرة.
> - عيوب التنفيذ (Implementation flaws): هجمات القناة الجانبية (side-channel attacks) مثل التوقيت والطاقة تكدر تفشي المفتاح الخاص.»

#### ③ الشرح الفهمي

المشكلة: الـ Hash يعطيك **integrity** بس — يعني يعرفك إذا البيانات تغيّرت، بس **ما يعرفك منو أرسلها**. أي واحد يقدر يحسب الهاش نفسه! فهنا يجي الـ **Digital Signature**: يربط الهوية بالبيانات باستخدام **asymmetric cryptography**.

الفكرة الذكية: المرسل يوقّع **بالهاش** مو بالرسالة كلها (أسرع وأقصر)، ويشفّر هذا الهاش **بمفتاحه الخاص**. المستقبل يفكّ **بالمفتاح العام** ويعيد حساب الهاش من الرسالة ويقارن.

$$Sig = E_{Priv}\big(h(M)\big)$$

$$\text{verify: } h(M) \stackrel{?}{=} D_{Pub}(Sig)$$

نقطة مهمة تلخبط الطلاب: هذي **عكس** التشفير العادي!
- **التشفير (Encryption):** تشفّر بالمفتاح **العام**، يفكّون بالمفتاح **الخاص** ← للسرية.
- **التوقيع (Signature):** يوقّع بالمفتاح **الخاص**، يتحققون بالمفتاح **العام** ← للأصالة.

| الضمانة | شنو تعني |
|---|---|
| **Integrity** | البيانات ما تغيّرت (الهاش يطابق) |
| **Authenticity** | فعلاً فلان هو اللي أرسلها (فقط هو عنده المفتاح الخاص) |
| **Non-repudiation** | ما يكدر ينكر — لأن التوقيع ما يصير إلا بمفتاحه الخاص |

**الخوارزميات:** RSA Signatures (تعتمد على RSA)، DSA (معيار فدرالي أمريكي)، ECDSA (أقوى بمفاتيح أصغر — مستخدمة بالبيتكوين).

**الهجمات الثلاثة (احفظهن):**
1. **سرقة المفتاح الخاص** ← المهاجم يزوّر أي توقيع.
2. **هاش ضعيف** (MD5/SHA-1) ← التصادم يسمح بتزوير التوقيع.
3. **عيوب التنفيذ** ← side-channel attacks (timing / power) تفشي المفتاح الخاص.

خلاصة تربط كل شي: الهاش لحاله = سلامة بدون هوية. التوقيع = سلامة + هوية + عدم إنكار. ولهذا التواقيع الرقمية تعتمد **دايمًا** على دالة هاش جيدة وراها.
