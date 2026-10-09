### القسم 1 — 1. Introduction

#### ① النص الأصلي

> Cryptography finds its most visible and impactful role not in theoretical design but in real-world applications. Every time a user logs into an online bank account, shops on Amazon, or transfers Bitcoin, cryptographic protocols ensure confidentiality, integrity, authenticity, and non-repudiation.
>
> The most prominent example is HTTPS, which secures web communications through the SSL/TLS protocols; these protocols show how symmetric and asymmetric encryption combine in hybrid systems to provide both scalability and efficiency. Beyond HTTPS, cryptography powers financial transactions, e-commerce, secure email, and blockchain ecosystems.
>
> This section explores how cryptographic primitives integrate into protocols, why they succeed (or sometimes fail), and presents a mathematical model to quantify the security of hybrid cryptography in real-world use.

#### ② الترجمة

> «التشفير يلقى دوره الأكثر وضوحاً وتأثيراً مو بالتصميم النظري، بل بالتطبيقات العملية بالعالم الحقيقي. كل مرة مستخدم يسجّل دخول لحساب بنك أونلاين، أو يتسوّق على Amazon، أو يحوّل Bitcoin، البروتوكولات التشفيرية تضمن السرية والسلامة والأصالة وعدم الإنكار.
>
> أوضح مثال هو HTTPS، اللي يؤمّن اتصالات الويب عبر بروتوكولات SSL/TLS؛ وهذي البروتوكولات تبيّن شلون التشفير المتماثل وغير المتماثل يتحدّون بأنظمة هجينة توفر القابلية للتوسع والكفاءة سوا. وما بعد HTTPS، التشفير يشغّل المعاملات المالية والتجارة الإلكترونية والإيميل الآمن وأنظمة البلوكتشين.
>
> هذي الفقرة تستكشف شلون المكوّنات التشفيرية الأولية تتكامل داخل البروتوكولات، وليش تنجح (أو أحياناً تفشل)، وتقدّم موديل رياضي لقياس أمن التشفير الهجين بالاستخدام الواقعي.»

#### ③ الشرح الفهمي

هنا الفصل الرابع يبدأ يدخل على الجانب العملي. الفكرة الأساسية إن التشفير مو بس شي نظري بالكتب، بل موجود بكل مكان نستخدمه بحياتنا اليومية.

مثلاً:
- تدخل حسابك البنكي ← TLS يشتغل.
- تشتري من Amazon ← TLS يشتغل.
- تحوّل Bitcoin ← توقيعات ECDSA والهاشات تشتغل.

هدف الفصل كله إن يوضّح إن الأنظمة الحقيقية تستخدم تشفير **hybrid** (متماثل + غير متماثل + hash)، وبعدين يعطينا موديل رياضي نحسب بيه "قوة الأمن".

| المفهوم | المعنى بالمختصر |
|---|---|
| Confidentiality | السرية — ما حد يقرأ البيانات |
| Integrity | السلامة — البيانات ما تتغيّر |
| Authenticity | الأصالة — نعرف منو المرسل |
| Non-repudiation | عدم الإنكار — المرسل ما يكدر ينكر |

---

### القسم 2 — 2. HTTPS and SSL/TLS

#### ① النص الأصلي

> 2.1 HTTPS Defined
>
> - HTTP (HyperText Transfer Protocol) is the foundation of web communication.
> - HTTPS ("HTTP Secure") = HTTP + SSL/TLS.
> - TLS provides:
>   - Confidentiality (symmetric encryption).
>   - Integrity (hashes and MACs).
>   - Authentication (certificates, PKI).
>
> 2.2 The TLS Handshake
>
> The TLS handshake establishes a secure channel between client and server.
>
> 1. ClientHello: Browser → Server; the browser lists the supported cryptographic algorithms (cipher suites).
> 2. ServerHello + Certificate: The server selects the algorithms and sends its X.509 certificate (contains the server's public key, signed by a CA).
> 3. Key Exchange: RSA handshake (legacy) — the client encrypts the session key with the server's public key; ECDHE handshake (modern) — client and server perform an Elliptic Curve Diffie–Hellman Ephemeral exchange to derive a shared session key.
> 4. Session Key Established: Both parties compute the symmetric session key; a symmetric cipher (AES, ChaCha20) is used for data.
> 5. Encrypted Communication: All subsequent HTTP requests and responses are encrypted.
>
> 2.3 Hybrid Encryption in TLS
>
> TLS is a hybrid cryptosystem:
>
> - Asymmetric cryptography: Used in authentication and key exchange.
> - Symmetric cryptography: Used for fast, bulk encryption.
> - Hashes/MACs: Ensure integrity.
> - Certificates (PKI): Provide trust in server identity.
>
> This design solves the scalability and performance challenge of purely asymmetric or symmetric systems.
>
> 2.4 Mathematical Model of TLS Security
>
> Let $S_{sym}$ be the security level of the symmetric algorithm (bits), $S_{asym}$ the security level of the asymmetric key exchange (bits), and $S_{hash}$ the security level of the hash function (bits). The effective security level of a TLS session is:
>
> Example: TLS 1.3 with AES-128, ECDHE-256, and SHA-256 gives $S_{sym} = 128$ bits, $S_{asym} \approx 128$ bits (ECC-256), and $S_{hash} = 128$ bits (SHA-256 collision resistance), so:
>
> This ensures ~$2^{128}$ operations are required to compromise the session, well beyond feasible attacks.
>
> .5 Security Evolution: TLS 1.0 → TLS 1.3
>
> - SSL 2.0/3.0: Deprecated due to vulnerabilities.
> - TLS 1.0/1.1: Weak ciphers (RC4, MD5).
> - TLS 1.2: Strong ciphers (AES, GCM), SHA-2.
> - TLS 1.3: Mandates forward secrecy (ECDHE), removes legacy algorithms, faster handshakes.

![مصافحة TLS — 5 خطوات|720](../06_Diagrams_&_Mindmaps/cy_w4_tls_handshake.svg)

$$S_{TLS} = \min(S_{sym}, S_{asym}, S_{hash})$$

$$S_{TLS} = \min(128, 128, 128) = 128\ \text{bits} \qquad (\text{TLS 1.3, AES-128 + ECDHE-256 + SHA-256})$$

#### ② الترجمة

> «2.1 تعريف HTTPS
>
> - HTTP (HyperText Transfer Protocol) هو أساس الاتصال بالويب.
> - HTTPS ("HTTP Secure") = HTTP + SSL/TLS.
> - TLS يوفّر:
>   - السرية (تشفير متماثل).
>   - السلامة (hashes و MACs).
>   - الأصالة (الشهادات، PKI).
>
> 2.2 مصافحة TLS
>
> مصافحة TLS تنشئ قناة آمنة بين العميل والسيرفر.
>
> 1. ClientHello: المتصفح ← السيرفر؛ والمتصفح يعدّد الخوارزميات المدعومة (cipher suites).
> 2. ServerHello + Certificate: السيرفر يختار الخوارزميات ويرسل شهادته X.509 (تحتوي المفتاح العام للسيرفر، موقّعة من CA).
> 3. Key Exchange: مصافحة RSA (قديمة) — العميل يشفّر مفتاح الجلسة بالمفتاح العام للسيرفر؛ ومصافحة ECDHE (حديثة) — العميل والسيرفر يسوّون تبادل Elliptic Curve Diffie–Hellman Ephemeral باش يشتقّون مفتاح جلسة مشترك.
> 4. Session Key Established: الطرفان يحسبون مفتاح الجلسة المتماثل؛ ويستخدمون تشفير متماثل (AES، ChaCha20) للبيانات.
> 5. Encrypted Communication: كل طلبات وردود HTTP اللاحقة تكون مشفّرة.
>
> 2.3 التشفير الهجين في TLS
>
> TLS هو نظام تشفير هجين:
>
> - التشفير غير المتماثل: يُستخدم بالمصادقة وتبادل المفاتيح.
> - التشفير المتماثل: يُستخدم للتشفير السريع وبالحجم الكبير.
> - Hashes/MACs: تضمن السلامة.
> - الشهادات (PKI): توفّر الثقة بهوية السيرفر.
>
> هالتصميم يحلّ مشكلة القابلية للتوسع والأداء عند الأنظمة غير المتماثلة أو المتماثلة الصافية.
>
> 2.4 الموديل الرياضي لأمن TLS
>
> خلّينا $S_{sym}$ مستوى أمن الخوارزمية المتماثلة (bits)، و$S_{asym}$ مستوى أمن تبادل المفاتيح غير المتماثل (bits)، و$S_{hash}$ مستوى أمن دالة الهاش (bits). مستوى الأمن الفعلي لجلسة TLS هو:
>
> مثال: TLS 1.3 مع AES-128 وECDHE-256 وSHA-256 يعطي $S_{sym} = 128$ bits، و$S_{asym} \approx 128$ bits (ECC-256)، و$S_{hash} = 128$ bits (SHA-256 collision resistance)، إذن:
>
> هذا يضمن إن ~$2^{128}$ عملية مطلوبة لاختراق الجلسة، وهذا بعيد جداً عن الهجمات الممكنة.
>
> .5 تطوّر الأمن: TLS 1.0 ← TLS 1.3
>
> - SSL 2.0/3.0: مهجورة بسبب الثغرات.
> - TLS 1.0/1.1: خوارزميات ضعيفة (RC4، MD5).
> - TLS 1.2: خوارزميات قوية (AES، GCM)، SHA-2.
> - TLS 1.3: تفرض forward secrecy (ECDHE)، وتحذف الخوارزميات القديمة، ومصافحات أسرع.»

#### ③ الشرح الفهمي

الفكرة الأساسية: TLS = **hybrid cryptosystem**. يعني يستخدم غير المتماثل مرة وحدة بالبداية (عشان نتفق على مفتاح جلسة)، وبعدين يستخدم المتماثل لباقي البيانات (أسرع بمراحل).

ليش هيج؟
- غير المتماثل (RSA/ECC) قوي بس بطيء.
- المتماثل (AES/ChaCha20) سريع جداً بس يحتاج مفتاح مشترك.
- الحل: نستخدم غير المتماثل بس لتبادل المفتاح، وبعدين متماثل للبيانات.

**خطوات المصافحة الخمس (ملخّص):**

| # | الخطوة | شنو يصير |
|---|---|---|
| 1 | ClientHello | المتصفح يگول للسيرفر: هاي الخوارزميات اللي أدعمها |
| 2 | ServerHello + Certificate | السيرفر يختار ويبعث شهادته X.509 |
| 3 | Key Exchange | يتبادلون مفتاح الجلسة (RSA قديم / ECDHE حديث) |
| 4 | Session Key Established | الطرفان عندهم نفس المفتاح المتماثل |
| 5 | Encrypted Communication | كل شي بعدها مشفّر |

**الموديل الرياضي — قاعدة "أضعف حلقة":**

$$S_{TLS} = \min(S_{sym}, S_{asym}, S_{hash})$$

| الرمز | المعنى |
|---|---|
| $S_{TLS}$ | مستوى أمن الجلسة الكلي (bits) |
| $S_{sym}$ | مستوى أمن التشفير المتماثل |
| $S_{asym}$ | مستوى أمن تبادل المفاتيح غير المتماثل |
| $S_{hash}$ | مستوى أمن دالة الهاش |

معنى $\min$: الجلسة قوّتها بقوة **أضعف** مكوّن، مو أقواه. مثلاً لو AES-256 وECDHE-256 بس SHA-256 (يعني 128) ← النتيجة 128 مو 256.

**ملاحظة أمانة:** المصافحة والموديل $S = \min(\dots)$ مكرّرين مرة ثانية بالفصل (بالقسم 4 — Mathematical Model). هذا تكرار من نفس المادة، فإذا سُئلت اكتب أي صيغة منهما.

---

### القسم 3 — 3. Real-World Applications

#### ① النص الأصلي

> 3.1 Banking Transactions
>
> - Online banking, SWIFT transfers, and stock trading rely on TLS.
> - Example: HSBC and JPMorgan Chase secure transactions with AES-256 and ECC certificates.
> - Failure case: In 2011, a Turkish certificate authority compromise enabled MITM attacks on banking websites.
>
> Cybersecurity lesson: Even strong algorithms fail if PKI governance is weak.
>
> 3.2 E-Commerce Security
>
> - Giants like Amazon, eBay, and PayPal rely on HTTPS.
> - TLS ensures:
>   - Credit card details are encrypted.
>   - Merchant identity verified by certificate.
>   - Transactions cannot be modified.
>
> Mathematical insight: Attack cost > potential fraud value. A 128-bit TLS session resists brute-force beyond feasible attacker economics.
>
> 3.3 Secure Email
>
> Two main standards:
>
> 1. PGP (Pretty Good Privacy) → Web-of-trust model.
> 2. S/MIME (Secure/Multipurpose Internet Mail Extensions) → PKI-based.
>
> Both combine:
>
> - Hashing (SHA-256) for integrity.
> - Digital signatures (RSA/ECC) for authenticity.
> - Encryption (AES) for confidentiality.
>
> Case study: The 2018 "EFAIL" vulnerability showed that improper integration (mixing HTML rendering + encrypted messages) can leak plaintext. Cybersecurity lesson: protocol design and implementation matter as much as algorithms.
>
> 3.4 Blockchain and Cryptocurrency
>
> Blockchain systems like Bitcoin and Ethereum use cryptography in three layers:
>
> 1. Hashes (SHA-256, Keccak-256): ensure immutability of the blockchain; each block references the previous block's hash.
> 2. Digital Signatures (ECDSA/EdDSA): authenticate transactions; only the private key owner can spend funds.
> 3. Consensus Mechanisms: security relies on computational hardness (Proof-of-Work) or cryptographic commitments (Proof-of-Stake).
>
> Case study: The 2010 Bitcoin overflow bug allowed the creation of billions of coins due to missing integer checks. Although not a cryptographic flaw, it highlights that protocol integrity is as important as primitives.

#### ② الترجمة

> «3.1 المعاملات البنكية
>
> - البنك الأونلاين وتحويلات SWIFT وتداول الأسهم تعتمد على TLS.
> - مثال: HSBC وJPMorgan Chase يؤمّنون المعاملات بـ AES-256 وشهادات ECC.
> - حالة فشل: سنة 2011، اختراق سلطة شهادات تركية مكّن هجمات MITM على مواقع بنكية.
>
> درس أمني: حتى الخوارزميات القوية تفشل لو حوكمة PKI ضعيفة.
>
> 3.2 أمن التجارة الإلكترونية
>
> - عمالقة مثل Amazon وeBay وPayPal تعتمد على HTTPS.
> - TLS يضمن:
>   - تفاصيل بطاقة الائتمان تكون مشفّرة.
>   - هوية التاجر موثّقة بالشهادة.
>   - المعاملات ما تتحوّل.
>
> بُعد رياضي: كلفة الهجوم > قيمة الاحتيال المحتملة. جلسة TLS بـ 128-bit تقاوم brute-force بما يتجاوز اقتصاد المهاجم الممكن.
>
> 3.3 الإيميل الآمن
>
> معياران رئيسيان:
>
> 1. PGP (Pretty Good Privacy) ← موديل web-of-trust.
> 2. S/MIME (Secure/Multipurpose Internet Mail Extensions) ← يعتمد على PKI.
>
> كلاهما يجمع:
>
> - Hashing (SHA-256) للسلامة.
> - توقيعات رقمية (RSA/ECC) للأصالة.
> - تشفير (AES) للسرية.
>
> دراسة حالة: ثغرة "EFAIL" سنة 2018 بيّنت إن التكامل الخاطئ (خلط عرض HTML + الرسائل المشفّرة) يكدر يسرّب النص الصريح. درس أمني: تصميم البروتوكول وتنفيذه مهمين بقدر الخوارزميات.
>
> 3.4 البلوكتشين والعملات الرقمية
>
> أنظمة البلوكتشين مثل Bitcoin وEthereum تستخدم التشفير بثلاث طبقات:
>
> 1. Hashes (SHA-256، Keccak-256): تضمن عدم قابلية التغيير بالبلوكتشين؛ وكل بلوك يشير لهاش البلوك السابق.
> 2. توقيعات رقمية (ECDSA/EdDSA): توثّق المعاملات؛ ومالك المفتاح الخاص فقط يكدر يصرف الأموال.
> 3. آليات التوافق (Consensus): الأمن يعتمد على الصلابة الحسابية (Proof-of-Work) أو الالتزامات التشفيرية (Proof-of-Stake).
>
> دراسة حالة: ثغرة overflow في Bitcoin سنة 2010 سمحت بإنشاء مليارات العملات بسبب نقص فحوصات الأعداد الصحيحة. مع إنها مو خلل تشفيري، بس تبيّن إن سلامة البروتوكول مهمة بقدر المكوّنات الأولية.»

#### ③ الشرح الفهمي

هذا القسم يعطينا أمثلة واقعية كيف التشفير يشتغل بأربع مجالات. النمط المتكرر: **الخوارزميات قوية، بس الحوكمة/التنفيذ هو اللي يفشل**.

| المجال | شنو يستخدم | الحادثة | الدرس |
|---|---|---|---|
| Banking | TLS + AES-256 + ECC | اختراق CA تركي 2011 | حوكمة PKI ضعيفة تكسر كل شي |
| E-Commerce | HTTPS + TLS 128-bit | — | كلفة الهجوم > قيمة الاحتيال |
| Secure Email | PGP / S/MIME | EFAIL 2018 | التنفيذ مهم بقدر الخوارزمية |
| Blockchain | SHA-256 + ECDSA | Bitcoin overflow 2010 | سلامة البروتوكول مهمة |

**PGP vs S/MIME** — الفرق الأساسي بمصدر الثقة:

| | PGP | S/MIME |
|---|---|---|
| موديل الثقة | Web-of-trust (الناس توقّع على مفاتيح بعض) | PKI (سلطات شهادات رسمية) |
| الاستخدام | شائع بالمجتمعات التقنية | شائع بالمؤسسات والشركات |

**طبقات البلوكتشين الثلاث:**

$$Layer = \{\text{hashes}, \text{digital signatures}, \text{consensus}\}$$

| الطبقة | الوظيفة |
|---|---|
| Hashes | عدم قابلية التغيير (immutability) |
| Digital Signatures | ملكية الأموال والأصالة |
| Consensus | يمنع الغش والتوافق بين العقد |

نقطة مهمة: حادثة EFAIL وحادثة Bitcoin overflow الاثنين مو خلل بالخوارزمية، بل بالتنفيذ/البروتوكول. هذا الدرس يتكرر بالفصل.

---

### القسم 4 — 4. Mathematical Model: Security of Hybrid Cryptography in Real-World Applications

#### ① النص الأصلي

> We formalize security as a minimum guarantee model across primitives.
>
> 4.1 Components
>
> - Symmetric security: $S_{sym} = k_{sym}$ bit (AES-128 = 128).
> - Asymmetric security: $S_{asym} = f(\text{key size})$; RSA-2048 ≈ 112 bits, ECC-256 ≈ 128 bits.
> - Hash security: $S_{hash} = n/2$ bits for an $n$-bit digest (collision resistance).
>
> 4.2 Overall Security
>
> The overall security of the system is the minimum across all primitives:
>
> 4.3 Economic Security Model
>
> The attacker's expected cost to break the system is:
>
> where $R$ is the attack rate (operations/sec), $T_{crack} = 2^{S_{system}-1}/R$, and $c$ is the cost per operation (energy/hardware). The system is secure if:
>
> 4.4 Example: Banking Transaction
>
> - AES-256 (sym): 256 bits.
> - ECDHE-384 (asym): ~192 bits.
> - SHA-256: 128 bits (collision).
>
> So $S_{system} = \min(256, 192, 128) = 128$ bits. Assume $R = 10^{18}$ ops/sec, $c = 10^{-12}$ USD/op, and $T_{crack} \approx 2^{127}/10^{18}$, then:
>
> This far exceeds the value of any banking transaction, hence the system is secure.

$$S_{system} = \min(S_{sym}, S_{asym}, S_{hash})$$

$$C_{attack} = R \cdot T_{crack} \cdot c \qquad \text{secure if } C_{attack} > V_{asset}$$

$$C_{attack} \approx (10^{18})(1.7 \times 10^{20})(10^{-12}) \approx 1.7 \times 10^{26}\ \text{USD}$$

#### ② الترجمة

> «نصيغ الأمن كموديل "ضمان أدنى" عبر المكوّنات الأولية.
>
> 4.1 المكوّنات
>
> - أمن متماثل: $S_{sym} = k_{sym}$ bit (AES-128 = 128).
> - أمن غير متماثل: $S_{asym} = f(\text{حجم المفتاح})$؛ RSA-2048 ≈ 112 bits، ECC-256 ≈ 128 bits.
> - أمن الهاش: $S_{hash} = n/2$ bits لهضم بحجم $n$-bit (collision resistance).
>
> 4.2 الأمن الكلي
>
> الأمن الكلي للنظام هو الأدنى عبر كل المكوّنات:
>
> 4.3 الموديل الاقتصادي للأمن
>
> الكلفة المتوقعة للمهاجم لكسر النظام هي:
>
> حيث $R$ معدّل الهجوم (عمليات/ثانية)، و$T_{crack} = 2^{S_{system}-1}/R$، و$c$ كلفة العملية الوحدة (طاقة/هاردوير). والنظام آمن إذا:
>
> 4.4 مثال: معاملة بنكية
>
> - AES-256 (متماثل): 256 bits.
> - ECDHE-384 (غير متماثل): ~192 bits.
> - SHA-256: 128 bits (collision).
>
> إذن $S_{system} = \min(256, 192, 128) = 128$ bits. افترض $R = 10^{18}$ عملية/ثانية، و$c = 10^{-12}$ USD/عملية، و$T_{crack} \approx 2^{127}/10^{18}$، إذن:
>
> هذا يفوق بمراحل قيمة أي معاملة بنكية، وبالتالي النظام آمن.»

#### ③ الشرح الفهمي

هذا القسم يجمع كل شي بموديل رياضي واحد. الفكرة بثلاث قواعد:

**1) الأمن الكلي = أضعف مكوّن** (نفس فكرة TLS):

$$S_{system} = \min(S_{sym}, S_{asym}, S_{hash})$$

**2) الموديل الاقتصادي** — السؤال: "قديش يكلّف المهاجم حتى يكسر النظام؟"

$$C_{attack} = R \cdot T_{crack} \cdot c \qquad \text{secure if } C_{attack} > V_{asset}$$

**3) الشرط:** إذا كلفة الهجوم أكبر من قيمة الهدف ← النظام آمن (منطقياً المهاجم ما يستفيد).

**جدول الرموز:**

| الرمز | المعنى |
|---|---|
| $S_{sym}$ | مستوى أمن التشفير المتماثل (bits) |
| $S_{asym}$ | مستوى أمن التشفير غير المتماثل (bits) |
| $S_{hash}$ | مستوى أمن دالة الهاش (bits) |
| $S_{system}$ | الأمن الكلي للنظام = الأدنى |
| $R$ | معدّل هجوم المهاجم (عمليات/ثانية) |
| $T_{crack}$ | زمن كسر المفتاح = $2^{S_{system}-1}/R$ |
| $c$ | كلفة العملية الوحدة (طاقة/هاردوير) |
| $V_{asset}$ | القيمة الاقتصادية للهدف |

**مثال البنك (4.4) خطوة بخطوة:**
- المكوّنات: 256 / 192 / 128 ← الأدنى = **128 bits**.
- $T_{crack} \approx 2^{127}/10^{18} \approx 1.7 \times 10^{20}$ (ثواني/وحدات زمن).
- $C_{attack} \approx (10^{18})(1.7 \times 10^{20})(10^{-12}) \approx 1.7 \times 10^{26}$ USD.
- بما إن الرقم خيالي ← النظام آمن عملياً.

نقطة مهمة: لاحظ إنه حتى لو AES-256 وECDHE-384 أقوياء، النتيجة النهائية 128 بس لأن SHA-256 هي الحلقة الأضعف. هذا نفس منطق TLS بالقسم 2.

---

### القسم 5 — 5. Challenges and Threats

#### ① النص الأصلي

> 5.1 Quantum Computing
>
> - Shor's algorithm: Breaks RSA/ECC.
> - Grover's algorithm: Reduces symmetric search by square root.
>
> Mitigation:
>
> - Post-quantum cryptography (lattice-based key exchange, hash-based signatures).
> - AES-256 remains quantum-resistant (effective ~128-bit security).
>
> 5.2 Certificate Authority (CA) Risks
>
> - DigiNotar breach (2011): Fraudulent certificates issued, enabling MITM attacks.
> - Solution: Certificate Transparency logs, multi-path validation, automated revocation.
>
> 5.3 Implementation Vulnerabilities
>
> - Heartbleed (2014): A bug in OpenSSL leaked private keys.
> - TLS downgrade attacks (forcing weak ciphers).
> - Side-channel attacks (timing leaks in RSA/ECDSA).
>
> Cybersecurity professionals must secure not only algorithms but also implementations.

#### ② الترجمة

> «5.1 الحوسبة الكمومية
>
> - خوارزمية Shor: تكسر RSA/ECC.
> - خوارزمية Grover: تقلّل البحث المتماثل بالجذر التربيعي.
>
> المعالجة:
>
> - تشفير ما بعد الكم (post-quantum): تبادل مفاتيح قائم على الشبكات (lattice-based)، وتوقيعات قائمة على الهاش (hash-based).
> - AES-256 يبقى مقاوم للكم (أمن فعّال ~128-bit).
>
> 5.2 مخاطر سلطة الشهادات (CA)
>
> - اختراق DigiNotar (2011): صدرت شهادات مزيفة، ومكّنت هجمات MITM.
> - الحل: سجلات Certificate Transparency، والتحقق متعدد المسارات، والإبطال الآلي.
>
> 5.3 ثغرات التنفيذ
>
> - Heartbleed (2014): خلل بـ OpenSSL سرّب المفاتيح الخاصة.
> - هجمات TLS downgrade (تجبر على خوارزميات ضعيفة).
> - هجمات القناة الجانبية (side-channel) (تسريب التوقيت بـ RSA/ECDSA).
>
> مختصو الأمن السيبراني لازم يؤمّنون مو بس الخوارزميات، بل التنفيذ هم.»

#### ③ الشرح الفهمي

القسم الأخير يعطينا التحديات اللي تواجه التشفير بالمستقبل. ثلاث فئات:

**1) التهديد الكمّي (Quantum):**

| الخوارزمية | تأثيرها |
|---|---|
| Shor | تكسر RSA/ECC تماماً (لأنها تحل factoring و discrete log) |
| Grover | تسرّع البحث بس بجذر تربيعي ← AES-256 ينزل لـ ~128-bit ويبقى آمن |

المعالجة: post-quantum cryptography + الاعتماد على AES-256.

**2) مخاطر CA:** المشكلة مو بالخوارزمية، بل بالثقة. إذا سلطة شهادات تُخترق (DigiNotar 2011) ← شهادات مزيفة ← MITM. الحل: Certificate Transparency + multi-path validation + إبطال آلي.

**3) ثغرات التنفيذ:** أشهرها Heartbleed (2014) بـ OpenSSL، وهجمات downgrade، وهجمات side-channel (تسريب التوقيت).

الدرس الجامع للفصل كله: **"الأمن = الخوارزمية ⨉ التنفيذ ⨉ الحوكمة"**. لو أي واحد منهم ضعيف، النظام كله ينهار — وهذا يتكرر بكل قسم من أقسام الفصل الأربعة.
