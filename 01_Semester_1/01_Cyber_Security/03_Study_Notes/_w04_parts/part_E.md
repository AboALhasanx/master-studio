### القسم 1 — Certificates and PKI
#### ① النص الأصلي
> 4.1 Problem Addressed: Digital signatures require knowledge of a public key. But how can users confirm that a given public key actually belongs to "Alice" and not to an attacker? This is solved by Certificates and Public Key Infrastructure (PKI).
>
> 4.2 Digital Certificates: A digital certificate is an electronic credential that binds a public key to an entity's identity. The contents of an X.509 certificate are:
>
> - Subject (entity identity).
> - Public key.
> - Issuer (Certificate Authority).
> - Validity period.
> - Digital signature from the issuer.
>
> 4.3 Certificate Authorities (CAs): CAs are trusted organizations that verify identities and issue certificates. Examples: DigiCert, Let's Encrypt, GlobalSign.
>
> - The CA digitally signs the certificate using its private key.
> - Browsers/OS trust certificates signed by recognized CAs.
>
> 4.4 Public Key Infrastructure (PKI): PKI manages certificates through policies, technologies, and processes:
>
> - Issuance: CA verifies and signs certificates.
> - Validation: Clients check certificate chain against trusted roots.
> - Revocation: Expired/compromised certificates are invalidated via CRLs (Certificate Revocation Lists) or OCSP (Online Certificate Status Protocol).
>
> 4.5 Cybersecurity Use Cases:
>
> 1. HTTPS (TLS/SSL): Servers present certificates to browsers, and browsers validate the chain before establishing encrypted sessions.
> 2. Code Signing: Certificates confirm the legitimacy of software vendors.
> 3. VPNs and Secure Emails: Certificates authenticate devices and users.
>
> 4.6 Weaknesses and Attacks:
>
> - CA compromise: If a CA is hacked, attackers can issue fake certificates (e.g., DigiNotar breach, 2011).
> - Expired certificates: Service outages occur if certificates are not renewed (e.g., Microsoft Teams outage, 2020).
> - Man-in-the-Middle (MITM): Attackers with fraudulent certificates can impersonate websites.
#### ② الترجمة
> «4.1 المشكلة التي يُعالجها (Problem Addressed): التوقيعات الرقمية (digital signatures) تتطلّب معرفة المفتاح العام (public key). لكن كيف يمكن للمستخدمين التأكّد من أن هذا المفتاح العام يعود فعلاً إلى "Alice" وليس إلى مهاجم؟ يُحلّ ذلك عبر الشهادات (Certificates) والبنية التحتية للمفاتيح العامة (PKI).»
>
> «4.2 الشهادات الرقمية (Digital Certificates): الشهادة الرقمية وثيقة إلكترونية تربط مفتاحاً عاماً بهوية كيان ما. ومحتويات شهادة X.509 هي:»
>
> - «Subject (هوية الكيان).»
> - «Public key (المفتاح العام).»
> - «Issuer (جهة الإصدار — Certificate Authority).»
> - «Validity period (فترة الصلاحية).»
> - «Digital signature from the issuer (توقيع رقمي من جهة الإصدار).»
>
> «4.3 جهات إصدار الشهادات (CAs): هي منظّمات موثوقة تتحقّق من الهويات وتُصدر الشهادات. أمثلة: DigiCert، Let's Encrypt، GlobalSign.»
>
> - «توقّع الـ CA الشهادة رقمياً باستخدام مفتاحها الخاص (private key).»
> - «المتصفحات وأنظمة التشغيل (Browsers/OS) تثق بالشهادات الموقّعة من قِبل CAs معترف بها.»
>
> «4.4 البنية التحتية للمفاتيح العامة (PKI): تُدير الـ PKI الشهادات عبر السياسات والتقنيات والعمليات:»
>
> - «الإصدار (Issuance): تتحقّق الـ CA من الهوية وتوقّع الشهادة.»
> - «التحقق (Validation): يفحص العملاء سلسلة الشهادات (certificate chain) مقابل الجذور الموثوقة (trusted roots).»
> - «الإبطال (Revocation): تُبطَل الشهادات المنتهية أو المخترقة عبر قوائم إبطال الشهادات CRLs أو بروتوكول حالة الشهادة OCSP.»
>
> «4.5 حالات الاستخدام في الأمن السيبراني (Cybersecurity Use Cases):»
>
> 1. «HTTPS (TLS/SSL): تعرض الخوادم شهاداتها على المتصفحات، وتتحقّق المتصفحات من السلسلة قبل إنشاء الجلسات المشفّرة.»
> 2. «توقيع الشيفرة (Code Signing): تؤكّد الشهادات شرعية موردي البرمجيات.»
> 3. «شبكات VPN والبريد الآمن (VPNs and Secure Emails): تُصادِق الشهادات على الأجهزة والمستخدمين.»
>
> «4.6 نقاط الضعف والهجمات (Weaknesses and Attacks):»
>
> - «اختراق الـ CA (CA compromise): إذا اختُرقت جهة إصدار، يمكن للمهاجمين إصدار شهادات مزيّفة (مثل اختراق DigiNotar عام 2011).»
> - «الشهادات المنتهية (Expired certificates): تحدث انقطاعات في الخدمة إذا لم تُجدَّد الشهادات (مثل انقطاع Microsoft Teams عام 2020).»
> - «هجوم الوسيط (Man-in-the-Middle / MITM): يستطيع المهاجمون الذين يملكون شهادات مزيّفة انتحال مواقع الويب.»
#### ③ الشرح الفهمي
القسم هذا يحلّ فجوة أساسية في الـ digital signatures. التوقيع الرقمي يثبت إن الرسالة ما تغيّرت ومين وقّعها، **بس** يبقى سؤال: منين تعرف إن هذا الـ public key فعلاً ملك "Alice" مو ملك مهاجم انتحل شخصيتها؟ الجواب: **الشهادة (certificate) + PKI**.

الشهادة الرقمية = وثيقة إلكترونية تربط (bind) الـ public key بهوية الكيان. أهم صيغة هي **X.509**، ومحتوياتها:

| الحقل | المعنى بالمختصر |
|---|---|
| Subject | هوية الكيان (مين صاحب الشهادة) |
| Public key | المفتاح العام المربوط بالهوية |
| Issuer | الـ CA اللي أصدرت الشهادة |
| Validity period | فترة الصلاحية (بداية ونهاية) |
| Digital signature from the issuer | توقيع الـ CA — هذا اللي يخلّي الشهادة موثوقة |

الـ **CA (Certificate Authority)** = منظمة موثوقة تتحقق من الهويات وتصدر الشهادات (أمثلة: DigiCert, Let's Encrypt, GlobalSign). نقطتين مهمة: (1) الـ CA توقّع الشهادة بمفتاحها الخاص private key، و(2) المتصفحات والأنظمة Browsers/OS تثق تلقائياً بالشهادات الموقّعة من CAs معروفة.

أما الـ **PKI** فهي البنية التحتية الكاملة اللي تدير الشهادات عبر policies + technologies + processes، وثلاث عمليات:

| العملية | شنو تسوي |
|---|---|
| Issuance | الـ CA تتحقق من الهوية وتوقّع الشهادة |
| Validation | العميل يفحص سلسلة الشهادات (chain) ضد الجذور الموثوقة (trusted roots) |
| Revocation | إبطال الشهادات المنتهية أو المخترقة عبر CRL أو OCSP |

فرّق مهم بالـ Revocation: **CRL** = قائمة إبطال يسحبها العميل، **OCSP** = استعلام أونلاين مباشر عن حالة شهادة معينة. الاثنين هدفهم واحد: يمنعون شهادة مبطلة من أن تُقبل.

الاستخدامات: **HTTPS** (السيرفر يعرض شهادته والمتصفح يتحقق قبل ما يفتح session مشفّرة)، **Code Signing** (تأكيد إن البرنامج من ناشر شرعي)، و**VPNs & Secure Emails** (توثيق الأجهزة والمستخدمين).

أما نقاط الضعف:
- **CA compromise** ← لو اخترقت الـ CA، المهاجم يصدر شهادات مزيّفة (DigiNotar 2011).
- **Expired certificates** ← الشهادة المنتهية تسبّب انقطاع خدمة (Microsoft Teams 2020).
- **MITM** ← مهاجم بشهادة مزيّفة ينتحل موقع ويخدع المستخدم.

الخلاصة: الـ algorithms قوية، بس إذا الـ governance ضعيف، السلسلة كلها تنكسر.

### القسم 2 — Mathematical Model: Trust and Verification Framework
#### ① النص الأصلي
> We now integrate hashing, digital signatures, and PKI into a unified mathematical model for cybersecurity evaluation.
>
> 5.1 Integrity Probability (Hashing): Let $P_{int}$ be the probability that a tampered message goes undetected. If the hash output length is $n$ bits, then the collision probability is $P_{int} \approx 2^{-n}$. For SHA-256, $P_{int} \approx 2^{-256}$, effectively zero for practical purposes.
>
> 5.2 Authenticity Probability (Digital Signatures): Authenticity depends on the strength of the signature algorithm and private key security. Let $P_{sig}$ be the probability the signature is forged, $b_{sig}$ the effective security bits (RSA-2048 ≈ 112 bits, ECC-256 ≈ 128 bits), and $R$ the attacker rate in operations/sec. If $T_{forge} \gg$ asset lifetime, authenticity holds.
>
> 5.3 Trust Probability (Certificates & PKI): Let $P_{ca}$ be the probability the CA is compromised and $P_{val}$ the probability certificate validation fails. The overall trust probability is $P_{trust} = (1 - P_{ca})(1 - P_{val})$.
>
> 5.4 Integrated Security Model: The overall assurance that data is secure is $P_{secure} = (1 - P_{int})(1 - P_{sig})(1 - P_{trust})$. Integrity uses strong hashes to minimize $P_{int}$; authenticity uses strong signatures to minimize $P_{sig}$; trust uses robust PKI governance to minimize $P_{trust}$.

$$P_{int} \approx 2^{-n} \qquad \text{(SHA-256: } P_{int} \approx 2^{-256}\text{)}$$

$$T_{forge} \approx \frac{2^{b_{sig}}}{R}$$

$$P_{trust} = (1 - P_{ca})(1 - P_{val})$$

$$P_{secure} = (1 - P_{int})(1 - P_{sig})(1 - P_{trust})$$
#### ② الترجمة
> «ندمج الآن الـ hashing والتوقيعات الرقمية والـ PKI في نموذج رياضي موحّد لتقييم الأمن السيبراني.»
>
> «5.1 احتمال السلامة (Integrity Probability — Hashing): لتكن $P_{int}$ هي احتمال مرور رسالة متلاعب بها دون كشفها. إذا كان طول مخرَج الهاش $n$ بت، فإن احتمال التصادم (collision) هو $P_{int} \approx 2^{-n}$. وبالنسبة لـ SHA-256 يكون $P_{int} \approx 2^{-256}$، أي صفر فعلياً لأغراض عملية.»
>
> «5.2 احتمال الأصالة (Authenticity Probability — Digital Signatures): تعتمد الأصالة على قوة خوارزمية التوقيع وأمان المفتاح الخاص. لتكن $P_{sig}$ احتمال تزوير التوقيع، و$b_{sig}$ عدد بتات الأمان الفعلية (RSA-2048 ≈ 112 بت، ECC-256 ≈ 128 بت)، و$R$ معدّل المهاجم بالعمليات/الثانية. إذا كان $T_{forge} \gg$ عمر الأصل، فإن الأصالة تبقى صامدة.»
>
> «5.3 احتمال الثقة (Trust Probability — Certificates & PKI): لتكن $P_{ca}$ احتمال اختراق الـ CA، و$P_{val}$ احتمال فشل التحقق من الشهادة. واحتمال الثقة الكلي هو $P_{trust} = (1 - P_{ca})(1 - P_{val})$.»
>
> «5.4 نموذج الأمن المتكامل (Integrated Security Model): الضمان الكلي بأن البيانات آمنة هو $P_{secure} = (1 - P_{int})(1 - P_{sig})(1 - P_{trust})$. فالسلامة تستخدم هاشات قوية لتقليل $P_{int}$؛ والأصالة تستخدم توقيعات قوية لتقليل $P_{sig}$؛ والثقة تستخدم حوكمة PKI متينة لتقليل $P_{trust}$.»
#### ③ الشرح الفهمي
القسم هذا يجمع الـ hashing + digital signatures + PKI بموديل رياضي واحد يقيس الثقة. الفكرة المحورية: كل طبقة عندها احتمال فشل، والاحتمالات تتضارب (multiply) لأن كل الطبقات لازم تنجح حتى يكون النظام آمن.

الرموز:

| الرمز | المعنى |
|---|---|
| $P_{int}$ | احتمال عدم كشف التلاعب (tampered message goes undetected) |
| $P_{sig}$ | احتمال تزوير التوقيع |
| $b_{sig}$ | effective security bits |
| $R$ | attacker ops/sec |
| $T_{forge}$ | الزمن اللازم لتزوير التوقيع |
| $P_{ca}$ | احتمال اختراق الـ CA |
| $P_{val}$ | احتمال فشل التحقق (validation) |
| $P_{trust}$ | احتمال الثقة الكلية |
| $P_{secure}$ | الضمان الكلي بأن البيانات آمنة |

**5.1 السلامة (Integrity):** $P_{int} \approx 2^{-n}$ — كل ما زاد طول الهاش $n$، الاحتمال يقلّ أُسّياً. لـ SHA-256 الحساب يعطي $2^{-256}$ ≈ صفر عملياً، يعني مستحيل تصادم عملي.

**5.2 الأصالة (Authenticity):** $T_{forge} \approx \dfrac{2^{b_{sig}}}{R}$ — الزمن اللازم لتزوير التوقيع يعتمد على قوة البتات $b_{sig}$ وعلى سرعة المهاجم $R$. القاعدة: إذا $T_{forge}$ أكبر بكثير من عمر الأصل (asset lifetime) ← التوقيع يعتبر آمن.

**5.3 الثقة (Trust):** $P_{trust} = (1 - P_{ca})(1 - P_{val})$ — الثقة تعتمد على شرطين معاً: الـ CA مو مخترقة **AND** التحقق ما فشل. لو أي واحد من الاثنين خرب، الثقة تنزل.

**5.4 الأمن المتكامل (Integrated):** $P_{secure} = (1 - P_{int})(1 - P_{sig})(1 - P_{trust})$ — لاحظ إن الأقواس مضروبة ببعض، مو مجموعة. هذا يعني: لو أي عامل صار ضعيف (يعني $P$ تبعه صار كبير، و$(1-P)$ صار قريب من صفر)، يهبط بالأمان الكلي. نفس مبدأ "**the weakest link dominates**" — أضعف حلقة تحكم على السلسلة كلها.

ربط بالأقسام السابقة: 5.1 تجي من الـ hashing، 5.2 من الـ digital signatures، و5.3 من الـ PKI — يعني الموديل يغطّي الطبقات الثلاث اللي درسناها.

### القسم 3 — Case Studies: DigiNotar (2011)
#### ① النص الأصلي
> Case 1: DigiNotar (2011)
>
> - Dutch CA compromised.
> - Fraudulent certificates used for MITM attacks on Gmail.
> - Lesson: Weak PKI governance undermines entire trust chain.
#### ② الترجمة
> «الحالة الأولى: DigiNotar (2011)»
>
> - «اختراق جهة إصدار هولندية (Dutch CA).»
> - «استُخدمت شهادات مزيّفة (fraudulent certificates) في هجمات وسيط (MITM) على Gmail.»
> - «الدرس: الحوكمة الضعيفة للـ PKI تقوّض سلسلة الثقة بأكملها.»
#### ③ الشرح الفهمي
DigiNotar حالة واقعية تثبت الدرس اللي مرّ علينا في 4.6. سنة 2011، اخترقت جهة إصدار هولندية اسمها **DigiNotar**، والمهاجم أصدر شهادات مزيّفة استخدمها لـ **MITM على Gmail** — يعني كان يقدر يتنصّت على اتصالات مستخدمي Gmail وهم يظنون إن الاتصال آمن (يقفل القفل الأخضر بالمتصفح). النتيجة: انهيار الثقة بالـ CA وانهيار الشركة نفسها.

الدرس بالجملة: **Weak PKI governance undermines entire trust chain** — يعني الحوكمة الضعيفة للـ PKI تهدّ القوس كامل. المهم هنا: الـ algorithms (AES, RSA, SHA-256) ما غلطت ولا انكسرت؛ اللي فشل هو الـ **governance** — إدارة الـ CA وثقة الجمهور فيها. وهذا يأكّد إن الأمن = math ⨉ implementation ⨉ operations، مو رياضيات بس.

| العنصر | الحالة |
|---|---|
| الجهة المخترقة | DigiNotar (CA هولندية) |
| السنة | 2011 |
| الأداة | شهادات مزيّفة (fraudulent certificates) |
| الهجوم | MITM على Gmail |
| السبب الجذري | حوكمة PKI ضعيفة (مو خوارزمية مكسورة) |
| الدرس | Weak PKI governance undermines entire trust chain |

![سلسلة الثقة: هاش ← توقيع ← شهادة ← PKI|720](../06_Diagrams_&_Mindmaps/cy_w4_trust_chain.svg)
