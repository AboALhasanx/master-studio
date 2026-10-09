### القسم 1 — 4. Hybrid Cryptography in Practice

#### ① النص الأصلي

> Modern systems rarely rely on just one paradigm; instead they combine both:
>
> - Asymmetric encryption → used to securely exchange a session key.
> - Symmetric encryption → used for efficient bulk data encryption.
>
> **Example: TLS Handshake**
>
> 1. Client connects to the server and retrieves the certificate (which contains the server's public key).
> 2. Client generates a random session key.
> 3. The session key is encrypted with the server's public key and sent.
> 4. Both parties now share the session key → use AES/ChaCha20 for the data.
>
> This model combines the scalability of asymmetric with the efficiency of symmetric encryption.

#### ② الترجمة

> «الأنظمة الحديثة نادرًا ما تعتمد على نموذج واحد فقط، بل تجمع بين الاثنين معًا:
>
> - التشفير غير المتماثل ← يُستخدم لتبادل مفتاح الجلسة (session key) بشكل آمن.
> - التشفير المتماثل ← يُستخدم لتشفير البيانات الكبيرة (bulk) بكفاءة.
>
> **مثال: مصافحة TLS (TLS Handshake)**
>
> 1. العميل يتصل بالخادم ويستحضر الشهادة (certificate) التي تحتوي على المفتاح العام للخادم.
> 2. العميل يولّد مفتاح جلسة (session key) عشوائيًا.
> 3. يُشفَّر مفتاح الجلسة بالمفتاح العام للخادم ويُرسَل.
> 4. الطرفان الآن يتشاركان مفتاح الجلسة ← يستخدمان AES/ChaCha20 للبيانات.
>
> هذا النموذج يجمع قابلية التوسّع (scalability) عند التشفير غير المتماثل مع كفاءة التشفير المتماثل.»

#### ③ الشرح الفهمي

ليش نخلط بين النوعين؟ لأن كل واحد عنده مشكلة والثاني يحلها. الـ **asymmetric** يحل مشكلة توزيع المفتاح (key distribution) بس بطيء. والـ **symmetric** سريع بس يحتاج مفتاح مشترك يوصل بأمان. فالحل هو الـ **Hybrid**: نستخدم asymmetric بس للجزء الصغير (تبادل مفتاح الجلسة)، وبعدها نكمّل بالـ symmetric للبيانات الكبيرة.

| المرحلة | نوع التشفير | السبب |
|---|---|---|
| تبادل مفتاح الجلسة | Asymmetric | يحل مشكلة توزيع المفتاح |
| نقل البيانات الفعلية | Symmetric (AES/ChaCha20) | سريع ويصلح للبيانات الكبيرة |

يعني باختصار: ندفع ضريبة البطء مرّة وحدة بس بالبداية، وبعدها نمشي بسرعة على البيانات.

### القسم 2 — 5. Mathematical Model: Security Work Factor in Encryption Systems

#### ① النص الأصلي

> To connect symmetric and asymmetric encryption to cybersecurity practice, we develop a **work factor model**. This quantifies how long a system can resist brute-force or mathematical attacks.
>
> **5.1 Bits of Security**
>
> - A system with a key space of size $2^k$ has $k$ bits of security.
> - The time to brute force depends on the adversary's computational rate $R$ (operations/sec).
>
> The average time equals half the keyspace:

$$T_{crack} \approx \frac{2^{k-1}}{R}$$

> **5.2 Symmetric Security**
>
> - AES-128.
> - With $R = 10^{18}$ ops/sec (an exascale adversary):

$$T_{crack} \approx \frac{2^{127}}{10^{18}} \approx 5.4 \times 10^{20}\ \text{years} \qquad (\text{AES-128})$$

> This is well beyond feasibility.
>
> **5.3 Asymmetric Security**
>
> The security of RSA/ECC is measured by its equivalent symmetric key strength:
>
> - RSA-2048 ≈ 112-bit symmetric security.
> - ECC-256 ≈ 128-bit symmetric security.
>
> These equivalences allow unified risk analysis.
>
> **5.4 Hybrid Model**
>
> For a secure system over lifetime $T_A$:

$$T_{system} = \min\{T_{sym}, T_{asym}\}$$

> - $T_{sym}$: cracking time for the symmetric session key.
> - $T_{asym}$: cracking time for the asymmetric key exchange.
>
> The weakest link dominates.

#### ② الترجمة

> «لربط التشفير المتماثل وغير المتماثل بالممارسة الأمنية، نبني **نموذج عامل الشغل (work factor model)**. هذا النموذج يقدّر كم من الوقت يقدر النظام يقاوم هجوم القوة الغاشمة (brute-force) أو الهجمات الرياضية.
>
> **5.1 بتات الأمان (Bits of Security)**
>
> - النظام اللي فضاء مفاتيحه (key space) بحجم $2^k$ عنده $k$ بت من الأمان.
> - زمن الـ brute force يعتمد على معدّل الحوسبة عند الخصم $R$ (عمليات/ثانية).
>
> متوسط الزمن يساوي نصف فضاء المفاتيح:»

$$T_{crack} \approx \frac{2^{k-1}}{R}$$

> «**5.2 الأمان المتماثل (Symmetric Security)**
>
> - AES-128.
> - بمعدّل $R = 10^{18}$ عملية/ثانية (خصم بمستوى exascale):»

$$T_{crack} \approx \frac{2^{127}}{10^{18}} \approx 5.4 \times 10^{20}\ \text{years} \qquad (\text{AES-128})$$

> «هذا يتجاوز حدود المعقول بكثير.
>
> **5.3 الأمان غير المتماثل (Asymmetric Security)**
>
> أمان RSA/ECC يُقاس بما يكافئه من قوة مفتاح متماثل:
>
> - RSA-2048 ≈ 112 بت من الأمان المتماثل.
> - ECC-256 ≈ 128 بت من الأمان المتماثل.
>
> هذه التكافؤات تسمح بتحليل موحّد للمخاطر.
>
> **5.4 النموذج الهجين (Hybrid Model)**
>
> لنظام آمن على مدى عمر $T_A$:»

$$T_{system} = \min\{T_{sym}, T_{asym}\}$$

> «- $T_{sym}$: زمن كسر مفتاح الجلسة المتماثل.
> - $T_{asym}$: زمن كسر تبادل المفتاح غير المتماثل.
>
> الحلقة الأضعف هي اللي تحكم (the weakest link dominates).»

#### ③ الشرح الفهمي

الفكرة الأساسية: الـ **work factor** يعني كم "شغل" لازم الخصم يسويه حتى يكسر النظام. ونقيسه بالـ **bits of security** — وكل بت إضافي يضاعف الشغل مرّتين. معادلة الزمن هي:

$$T_{crack} \approx \frac{2^{k-1}}{R}$$

| الرمز | المعنى |
|---|---|
| $k$ | بتات الأمان (bits of security) |
| $R$ | معدّل عمليات الخصم في الثانية (ops/sec) |
| $T_{crack}$ | الزمن المتوقع لكسر المفتاح (brute force) |

ليش $2^{k-1}$ مو $2^k$؟ لأننا بالمعدّل راح نلكى المفتاح بنص فضاء المفاتيح (half the keyspace).

مثال AES-128 مع خصم بمستوى exascale ($R = 10^{18}$):

$$T_{crack} \approx \frac{2^{127}}{10^{18}} \approx 5.4 \times 10^{20}\ \text{years} \qquad (\text{AES-128})$$

هذا رقم خيالي — للمقارنة، عمر الكون تقريبًا $1.4 \times 10^{10}$ سنة. يعني AES-128 عمليًا مستحيل.

نقطة مهمة جدًا: أمان **RSA/ECC** ما نقيسه بعدد بتات مفتاحه مباشرة، بل بما يكافئه من مفتاح متماثل. RSA-2048 (مفتاحه 2048 بت) يكافئ 112 بت متماثل بس! و ECC-256 يكافئ 128 بت. لذلك ECC أفضل — مفتاح أصغر وأمان أعلى.

والنموذج الهجين يقول إن أمان النظام كله = الأضعف بين الجزئين:

$$T_{system} = \min\{T_{sym}, T_{asym}\}$$

| الرمز | المعنى |
|---|---|
| $T_{sym}$ | زمن كسر الجزء المتماثل (session key) |
| $T_{asym}$ | زمن كسر الجزء غير المتماثل (key exchange) |
| $T_{system}$ | أمان النظام الكلي = الأضعف بينهما |

يعني لو الـ key exchange ضعيف، ما يفيدك إن الـ AES قوي — الحلقة الأضعف هي اللي تحكم.

ملاحظة صريحة: النص يعيد تكرار التكافؤ «RSA-2048 ≈ 112 بت / ECC-256 ≈ 128 بت» عدة مرات عبر الفصل — المادة مكرّرة بالتصميم.

### القسم 3 — 6. Case Studies

#### ① النص الأصلي

> **Case 1: Wi-Fi Security**
>
> - WPA2 uses AES-CCMP (symmetric).
> - Vulnerabilities often stem from key management (e.g., the KRACK attack exploiting nonce reuse).
>
> **Case 2: HTTPS/TLS**
>
> - Combination of asymmetric key exchange + symmetric encryption.
> - Misconfigured PKI or weak certificates are often the weak link.
>
> **Case 3: Bitcoin and Blockchain**
>
> - Transactions secured with ECDSA signatures (asymmetric).
> - Ledger integrity enforced with SHA-256 hashes.
>
> **Case 4: Quantum Threat**
>
> - RSA/ECC vulnerable to Shor's algorithm.
> - Symmetric AES only loses half its effective key length under Grover → AES-256 remains secure.

#### ② الترجمة

> «**الحالة 1: أمان الواي فاي (Wi-Fi Security)**
>
> - WPA2 يستخدم AES-CCMP (متماثل).
> - الثغرات غالبًا تنشأ من إدارة المفاتيح (key management) (مثل هجوم KRACK اللي يستغل إعادة استخدام الـ nonce).
>
> **الحالة 2: HTTPS/TLS**
>
> - مزيج من تبادل مفتاح غير متماثل + تشفير متماثل.
> - PKI المُهيّأ غلط أو الشهادات الضعيفة غالبًا هي الحلقة الأضعف.
>
> **الحالة 3: البيتكوين والبلوكتشين (Bitcoin and Blockchain)**
>
> - المعاملات مؤمّنة بتوقيعات ECDSA (غير متماثل).
> - سلامة السجل (ledger integrity) مفروضة بـ hashes من نوع SHA-256.
>
> **الحالة 4: التهديد الكمّي (Quantum Threat)**
>
> - RSA/ECC عرضة لخوارزمية Shor.
> - AES المتماثل يفقد نصف طول مفتاحه الفعلي تحت Grover، لذلك AES-256 يبقى آمنًا.»

#### ③ الشرح الفهمي

الأربع حالات تعلّمنا درس واحد: **النظام القوي = مزيج من الـ primitives، والأمان يحكمه أضعف جزء فيه**.

| الحالة | الـ primitive الأساسي | نقطة الضعف الفعلية |
|---|---|---|
| Wi-Fi (WPA2) | AES-CCMP متماثل | إدارة المفاتيح ← هجوم KRACK (nonce reuse) |
| HTTPS/TLS | hybrid (asym + sym) | PKI / شهادات ضعيفة |
| Bitcoin | ECDSA + SHA-256 | توقيع المفتاح الخاص |
| Quantum | Shor ضد RSA/ECC | Grover يضرب AES بس AES-256 يبقى آمن |

توضيح كل حالة:

- **Wi-Fi**: الخوارزمية (AES) قوية، بس الهجوم ما جاء من الخوارزمية — جاء من سوء إدارة المفاتيح (KRACK). يعني الحلقة الأضعف كانت implementation مو algorithm.
- **HTTPS/TLS**: يجمع الاثنين — asymmetric للـ handshake و symmetric للبيانات. والضعف عادة بالـ PKI (شهادات ضعيفة أو CA مخترق).
- **Bitcoin**: توقيع ECDSA يثبت ملكية العملة، و SHA-256 يثبّت البلوكتشين. لو غيّرت بلوك واحد، كل الـ hashes اللي بعده تتغيّر ← التلاعب يبان.
- **Quantum**: Shor يكسر RSA/ECC كامل، أما Grover على AES فيقلل البحث بـ square root بس ← AES-256 يفقد نصف طوله ويبقى ~128 بت أمان (آمن).
