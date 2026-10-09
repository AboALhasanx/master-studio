### القسم 1 — Introduction
#### ① النص الأصلي
> Encryption is one of the most fundamental mechanisms in cybersecurity, ensuring that sensitive information can only be accessed by authorized parties. All modern secure communication systems — from mobile banking and cloud storage to national defense and blockchain — depend on two complementary paradigms of encryption: symmetric encryption and asymmetric encryption.
>
> - **Symmetric encryption**: Same key used for encryption and decryption.
> - **Asymmetric encryption**: Uses mathematically related public/private key pairs.
>
> Each approach has distinct strengths, weaknesses, and applications, and in practice they are combined to provide scalability, efficiency, and trust in secure systems. This section explores both paradigms in depth — their algorithms, applications, limitations, and most importantly a mathematical framework for analyzing their security levels in real-world cybersecurity contexts.

#### ② الترجمة
> «التشفير (Encryption) واحد من أهم المبادئ الأساسية في الأمن السيبراني، لأنه يضمن أن المعلومات الحساسة ما يوصل لها إلا الأطراف المصرّح لها. كل أنظمة الاتصال الآمنة الحديثة — من الموبايل بانكنگ والتخزين السحابي إلى الدفاع الوطني والبلوكچين — تعتمد على نمطين متكاملين من التشفير: التشفير المتماثل (symmetric) والتشفير غير المتماثل (asymmetric).
>
> - **التشفير المتماثل (Symmetric encryption)**: نفس المفتاح يُستخدم للتشفير وفك التشفير.
> - **التشفير غير المتماثل (Asymmetric encryption)**: يستخدم زوج مفاتيح (public/private) مرتبطة ببعضها رياضياً.
>
> كل طريقة لها نقاط قوة وضعف وتطبيقات مميزة، وعملياً يتم دمجهن سوة لتوفير القابلية للتوسّع (scalability) والكفاءة (efficiency) والثقة (trust) في الأنظمة الآمنة. هذا القسم يستعرض النمطين بعمق — الخوارزميات والتطبيقات والقيود، والأهم إطار رياضي لتحليل مستويات الأمان مالهن في سياقات الأمن السيبراني الواقعية.»

#### ③ الشرح الفهمي
التشفير هو أساس الأمن السيبراني: بدونه أي معلومة تمرّ على الشبكة تكون مكشوفة. الفكرة كلها تدور على **نموذجين (paradigms)** للتشفير:

| النموذج | عدد المفاتيح | الفكرة بجملة |
|---|---|---|
| **Symmetric** | مفتاح واحد مشترك | نفس المفتاح يقفل ويفتح |
| **Asymmetric** | زوج مفاتيح (public + private) | مفتاح للقفل ومفتاح مختلف للفتح |

ولا واحد منهن كافي لحاله: المتماثل سريع بس عنده مشكلة توزيع المفتاح، وغير المتماثل يحل توزيع المفتاح بس بطيء. لهذا الواقع يجمع بينهن (Hybrid) — وهذا اللي راح نشوفه بالـ TLS مثلاً. هذا القسم راح يشرح الاثنين ويحطّ إطار رياضي (mathematical framework) نقيس بيه مستوى الأمان بشكل رقمي.

---

### القسم 2 — Symmetric Encryption
#### ① النص الأصلي
> **2.1 Definition**
>
> Symmetric encryption employs a single shared secret key $K$ for both encryption and decryption.
>
> - Encryption: $C = E_K(P)$
> - Decryption: $P = D_K(C)$
>
> Where:
>
> - $P$ = plaintext message,
> - $C$ = ciphertext,
> - $E_K$ = encryption function under key $K$,
> - $D_K$ = decryption function under key $K$.
>
> If the system is secure, $D_K(E_K(P)) = P$.
>
> **2.2 Key Characteristics**
>
> - **Fast and efficient**: Handles large volumes of data quickly.
> - **Minimal resource usage**: Suitable for embedded devices and IoT.
> - **Key distribution challenge**: Securely sharing $K$ across networks is difficult.
>
> **2.3 Common Algorithms**
>
> 1. **DES (Data Encryption Standard, 1977)**
>    - Block cipher, 56-bit key.
>    - Once dominant but broken by brute force.
>    - Demonstrated the danger of underestimating future computing power.
> 2. **AES (Advanced Encryption Standard, 2001)**
>    - Block cipher with 128-, 192-, or 256-bit keys.
>    - Secure against all practical cryptanalysis.
>    - Standard for VPNs, TLS, disk encryption.
> 3. **ChaCha20 (2014)**
>    - Stream cipher optimized for speed and resistance to timing attacks.
>    - Widely deployed in TLS 1.3 and mobile applications.
>
> **2.4 Strengths**
>
> - **Performance**: AES can achieve gigabits/sec throughput.
> - **Simplicity**: Easier to implement securely than asymmetric cryptography.
> - **Compactness**: Smaller key sizes achieve high security (AES-128 is robust).
>
> **2.5 Weaknesses**
>
> - **Key distribution problem**: If the key is intercepted or leaked, confidentiality collapses.
> - **Scalability**: With $n$ users, a symmetric system requires $\frac{n(n-1)}{2}$ unique keys.
> - **Revocation difficulty**: Replacing a compromised key requires distributing a new one securely.
>
> **2.6 Use Cases in Cybersecurity**
>
> - Encrypting stored data (databases, disks).
> - Securing network traffic (VPNs, Wi-Fi protocols like WPA2/WPA3).
> - Bulk encryption of cloud backups.

$$C = E_K(P) \qquad P = D_K(C)$$

$$\text{keys needed for } n \text{ users} = \frac{n(n-1)}{2}$$

#### ② الترجمة
> «**2.1 التعريف**
>
> التشفير المتماثل (Symmetric encryption) يستخدم مفتاح سري واحد مشترك $K$ للتشفير وفك التشفير سوة.
>
> - التشفير (Encryption): $C = E_K(P)$
> - فك التشفير (Decryption): $P = D_K(C)$
>
> حيث:
>
> - $P$ = الرسالة الأصلية (plaintext),
> - $C$ = النص المشفّر (ciphertext),
> - $E_K$ = دالة التشفير تحت المفتاح $K$,
> - $D_K$ = دالة فك التشفير تحت المفتاح $K$.
>
> إذا النظام آمن، فإن $D_K(E_K(P)) = P$.
>
> **2.2 الخصائص الرئيسية**
>
> - **سريع وفعّال (Fast and efficient)**: يتعامل مع كميات كبيرة من البيانات بسرعة.
> - **استهلاك موارد قليل (Minimal resource usage)**: مناسب للأجهزة المدمجة (embedded) والـ IoT.
> - **تحدي توزيع المفتاح (Key distribution challenge)**: مشاركة $K$ بشكل آمن عبر الشبكات صعبة.
>
> **2.3 الخوارزميات الشائعة**
>
> 1. **DES (معيار تشفير البيانات، 1977)**
>    - Block cipher، مفتاح 56-bit.
>    - كان مسيطر زمان بس انكسر بالقوة الغاشمة (brute force).
>    - أثبت خطر الاستهانة بقوة الحوسبة المستقبلية.
> 2. **AES (معيار التشفير المتقدم، 2001)**
>    - Block cipher بمفاتيح 128- أو 192- أو 256-bit.
>    - آمن ضد كل التحليل التشفيري العملي (practical cryptanalysis).
>    - معيار للـ VPNs والـ TLS وتشفير الأقراص (disk encryption).
> 3. **ChaCha20 (2014)**
>    - Stream cipher مُحسّن للسرعة ومقاوم لهجمات التوقيت (timing attacks).
>    - مُنتشر بشكل واسع في TLS 1.3 وتطبيقات الموبايل.
>
> **2.4 نقاط القوة**
>
> - **الأداء (Performance)**: الـ AES يوصل إنتاجية (throughput) بالگيگابت/ثانية.
> - **البساطة (Simplicity)**: أسهل تنفيذاً بشكل آمن من التشفير غير المتماثل.
> - **الاختصار (Compactness)**: أحجام مفاتيح أصغر تحقق أمان عالي (AES-128 قوي).
>
> **2.5 نقاط الضعف**
>
> - **مشكلة توزيع المفتاح (Key distribution problem)**: إذا انقطع المفتاح أو تسرّب، السرّية (confidentiality) تنهار.
> - **القابلية للتوسّع (Scalability)**: مع $n$ مستخدمين، النظام المتماثل يحتاج $\frac{n(n-1)}{2}$ مفاتيح فريدة.
> - **صعوبة الإبطال (Revocation difficulty)**: تبديل مفتاح مخترق يتطلّب توزيع مفتاح جديد بشكل آمن.
>
> **2.6 حالات الاستخدام في الأمن السيبراني**
>
> - تشفير البيانات المخزّنة (قواعد البيانات، الأقراص).
> - تأمين حركة الشبكة (VPNs، بروتوكولات الواي فاي مثل WPA2/WPA3).
> - التشفير الكمّي (bulk encryption) للنسخ الاحتياطية السحابية.»

#### ③ الشرح الفهمي
الفكرة الأساسية بجملة: **مفتاح واحد يقفل ويفتح**. يعني الطرفين (Sender و Receiver) لازم يكون عندهم نفس المفتاح $K$ سرّاً. إذا الأمان شغّال، فك التشفير يرجّعك للنص الأصلي بالضبط: $D_K(E_K(P)) = P$.

شنو يخلي المتماثل محبوب؟ سريع جداً ومناسب لكميات البيانات الكبيرة (bulk data) والأجهزة الضعيفة (IoT). بس عنده جرح كبير: **مشكلة توزيع المفتاح** — كيف نوصل نفس المفتاح للطرف الثاني بأمان أصلاً؟

الخوارزميات الثلاثة:

| الخوارزمية | السنة | النوع | حجم المفتاح | الملاحظة |
|---|---|---|---|---|
| **DES** | 1977 | Block cipher | 56-bit | انكسر بالـ brute force — درس: لا تستهين بقوة الحوسبة المستقبلية |
| **AES** | 2001 | Block cipher | 128 / 192 / 256-bit | المعيار الحالي، آمن عملياً |
| **ChaCha20** | 2014 | Stream cipher | — | سريع ومقاوم للـ timing attacks، مستخدم في TLS 1.3 |

معادلة عدد المفاتيح مهمة للامتحان: مع $n$ مستخدمين، عدد المفاتيح الفريدة المطلوبة = $\frac{n(n-1)}{2}$ — يعني تنمو بشكل تربيعي، وهذا سبب مشكلة الـ scalability.

⚠️ **ملاحظة صريحة (تصحيح):** النص ذكر مفاتيح AES (128/192/256) بس ما ذكر عدد الدورات (rounds). الحقيقة المعيارية: الـ AES يستخدم **10 / 12 / 14 دورات** لمفاتيح 128 / 192 / 256-bit — مو "16" (رقم شائع غلط). هاي معلومة خارج النص بس صحيحة ومهمة.

---

### القسم 3 — Asymmetric Encryption
#### ① النص الأصلي
> **3.1 Definition**
>
> Asymmetric encryption uses two related keys:
>
> - Public key ($K_{pub}$) → used for encryption.
> - Private key ($K_{priv}$) → used for decryption.
>
> This eliminates the need to share a secret key in advance.
>
> **3.2 RSA Algorithm (1978)**
>
> RSA is based on the difficulty of factoring large integers.
>
> 1. Choose two primes $p, q$.
> 2. Compute modulus: $n = p \cdot q$.
> 3. Compute Euler's totient: $\varphi(n) = (p-1)(q-1)$.
> 4. Choose public exponent $e$ with $\gcd(e, \varphi(n)) = 1$.
> 5. Compute private key $d \equiv e^{-1} \pmod{\varphi(n)}$.
> 6. Encryption: $C = P^{e} \bmod n$.
> 7. Decryption: $P = C^{d} \bmod n$.
>
> **3.3 Elliptic Curve Cryptography (ECC, 1985)**
>
> ECC relies on the Elliptic Curve Discrete Logarithm Problem (ECDLP).
>
> - Provides equivalent security with shorter keys:
>   - 256-bit ECC ≈ 3072-bit RSA.
> - More efficient for mobile, IoT, and blockchain.
>
> **3.4 Strengths**
>
> - **Key distribution solved**: No pre-shared secret required.
> - Supports digital signatures and authentication.
> - **Foundation of PKI** (certificates, HTTPS, secure email).
>
> **3.5 Weaknesses**
>
> - **Slower**: Orders of magnitude slower than AES.
> - **Resource intensive**: Not suitable for bulk encryption.
> - **Quantum vulnerability**: Shor's algorithm can break RSA/ECC.
>
> **3.6 Use Cases in Cybersecurity**
>
> - Establishing secure connections (TLS/SSL).
> - Email encryption and signing (PGP, S/MIME).
> - Authentication (SSH keys, smartcards).
> - Cryptocurrencies (Bitcoin wallets via ECC).

$$n = p \cdot q \qquad \varphi(n) = (p-1)(q-1) \qquad d \equiv e^{-1} \pmod{\varphi(n)}$$

$$C = P^{e} \bmod n \qquad P = C^{d} \bmod n$$

#### ② الترجمة
> «**3.1 التعريف**
>
> التشفير غير المتماثل (Asymmetric encryption) يستخدم مفتاحين مرتبطين:
>
> - المفتاح العام (Public key، $K_{pub}$) ← يُستخدم للتشفير.
> - المفتاح الخاص (Private key، $K_{priv}$) ← يُستخدم لفك التشفير.
>
> هذا يلغي الحاجة لمشاركة مفتاح سري مسبقاً.
>
> **3.2 خوارزمية RSA (1978)**
>
> الـ RSA تعتمد على صعوبة تحليل الأعداد الكبيرة إلى عواملها (factoring large integers).
>
> 1. اختر عددين أوليين (primes) $p, q$.
> 2. احسب المعامل (modulus): $n = p \cdot q$.
> 3. احسب دالة أويلر (Euler's totient): $\varphi(n) = (p-1)(q-1)$.
> 4. اختر الأس العام (public exponent) $e$ بحيث $\gcd(e, \varphi(n)) = 1$.
> 5. احسب المفتاح الخاص $d \equiv e^{-1} \pmod{\varphi(n)}$.
> 6. التشفير (Encryption): $C = P^{e} \bmod n$.
> 7. فك التشفير (Decryption): $P = C^{d} \bmod n$.
>
> **3.3 تشفير المنحنيات الإهليلجية (ECC، 1985)**
>
> الـ ECC تعتمد على مسألة اللوگاريتم المتقطّع للمنحنى الإهليلجي (ECDLP).
>
> - تعطي أمان مكافئ بمفاتيح أقصر:
>   - 256-bit ECC ≈ 3072-bit RSA.
> - أكثر كفاءة للموبايل والـ IoT والبلوكچين.
>
> **3.4 نقاط القوة**
>
> - **حلّت مشكلة توزيع المفتاح**: ما كو حاجة لسر مشترك مسبق.
> - تدعم التوقيعات الرقمية (digital signatures) والمصادقة (authentication).
> - **أساس الـ PKI** (الشهادات، HTTPS، البريد الآمن).
>
> **3.5 نقاط الضعف**
>
> - **أبطأ (Slower)**: أبطأ من AES بمراتب كثيرة.
> - **مستهلكة للموارد (Resource intensive)**: ما تناسب التشفير الكمّي (bulk encryption).
> - **هشاشة كمومية (Quantum vulnerability)**: خوارزمية Shor تقدر تكسر RSA/ECC.
>
> **3.6 حالات الاستخدام في الأمن السيبراني**
>
> - إنشاء الاتصالات الآمنة (TLS/SSL).
> - تشفير وتوقيع البريد الإلكتروني (PGP، S/MIME).
> - المصادقة (مفاتيح SSH، البطاقات الذكية smartcards).
> - العملات الرقمية (محافظ البيتكوين عبر ECC).»

#### ③ الشرح الفهمي
هنا الفكرة معكوسة عن المتماثل: **مفتاحين مختلفين مرتبطين رياضياً**. المفتاح العام ($K_{pub}$) يوزّعه أي واحد، والمفتاح الخاص ($K_{priv}$) يبقى سرّ عندك. اللي يقفل بالمفتاح العام، ما يفتحه إلا المفتاح الخاص. وهذا يحل مشكلة توزيع المفتاح اللي كانت تقتل النظام المتماثل — لأن ما كو حاجة نتفق على سر مشترك من قبل.

**خطوات RSA السبع (مهمة للامتحان):**

1. اختر عددين أوليين $p, q$.
2. $n = p \cdot q$ ← هذا هو الـ modulus.
3. $\varphi(n) = (p-1)(q-1)$ ← دالة أويلر.
4. اختر $e$ بحيث $\gcd(e, \varphi(n)) = 1$.
5. $d \equiv e^{-1} \pmod{\varphi(n)}$.
6. التشفير: $C = P^{e} \bmod n$.
7. فك التشفير: $P = C^{d} \bmod n$.

مقارنة RSA و ECC:

| | RSA (1978) | ECC (1985) |
|---|---|---|
| المسألة الصعبة | factoring الأعداد الكبيرة | ECDLP (Elliptic Curve Discrete Log) |
| حجم المفتاح لأمان مكافئ | 3072-bit | 256-bit |
| المناسبة | الاستخدام العام | الموبايل، IoT، البلوكچين |

**القوة:** حلّت توزيع المفتاح + تدعم digital signatures + هي أساس الـ PKI. **الضعف:** بطيئة جداً مقارنة بالـ AES، ولهذا ما تُستخدم للـ bulk encryption، وأخطر شي إنها هشّة قدام الحوسبة الكمومية — خوارزمية **Shor** تكسر RSA/ECC.

⚠️ **ملاحظة صريحة (تصحيح):** النص طبع الخطوة 4 بالشكل `gdc(e, φ(n)) = 1`، والصحيح هو **gcd** (greatest common divisor = القاسم المشترك الأكبر). كتبناها بالشكل الصحيح gcd داخل النص، وهاي تصحيح خطأ مطبعي واضح مو تغيير بالمحتوى.

---

![المتماثل مقابل غير المتماثل|720](../06_Diagrams_&_Mindmaps/cy_w4_sym_vs_asym.svg)
