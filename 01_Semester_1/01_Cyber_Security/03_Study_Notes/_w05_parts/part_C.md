### القسم 1 — 7. Interdomain routing: BGP, RPKI, and BGPsec

#### ① النص الأصلي

> **7.1 BGP's trust model and hijack surface.** BGP was designed for policy exchange among autonomous systems (ASes) with implicit trust in path attributes. Attackers (or misconfigurations) can mis-originate a prefix or shorten paths, diverting or black-holing traffic.
>
> **7.2 Origin validation with RPKI.** RPKI (RFC 6480) binds IP prefixes and ASNs to certificates in a hierarchical public-key infrastructure. Operators publish Route Origin Authorizations (ROAs). Routers perform BGP origin validation (RFC 6811), marking updates as valid, invalid, or unknown; policies can drop or de-prefer invalid paths, reducing mis-origination.
>
> **7.3 Path validation with BGPsec.** BGPsec (RFC 8205) extends BGP with per-hop cryptographic signatures that protect the AS_PATH against tampering, strengthening guarantees but increasing CPU and memory costs and complicating incremental deployment.
>
> **Validation efficacy model.** If a fraction $f$ of global routes are covered by ROAs and participating ASes enforce "drop invalid," the probability a random hijack succeeds on an end-to-end path of length $L$ is approximately $(1-f)^{L}$ (assuming independent AS adoption), highlighting network effects: each additional validating AS exponentially reduces hijack success on traversals.

#### ② الترجمة

> «**7.1 نموذج الثقة وسطح الاختطاف في BGP.** صُمِّم BGP لتبادل السياسات بين الأنظمة المستقلة (ASes) اعتمادًا على ثقة ضمنية في خصائص المسار (path attributes). ويمكن للمهاجمين (أو أخطاء الإعداد) أن يُعلنوا أصلًا خاطئًا (mis-originate) لبادئة معيّنة أو أن يقصّروا المسارات، فيحوّلون حركة المرور أو يبتلعونها (black-holing).
>
> **7.2 التحقق من الأصل عبر RPKI.** يربط RPKI (RFC 6480) بادئات IP و ASNs بشهادات في بنية تحتية هرمية للمفاتيح العامة. وينشر المشغّلون تصاريح أصل المسار (ROAs). وتُجري الراوترات تحقق أصل BGP (RFC 6811) فتصنّف التحديثات إلى صحيحة أو غير صحيحة أو مجهولة؛ ويمكن للسياسات أن تُسقط المسارات غير الصحيحة أو تُقلّل أولويتها، مما يحدّ من خطأ الأصل (mis-origination).
>
> **7.3 التحقق من المسار عبر BGPsec.** يوسّع BGPsec (RFC 8205) بروتوكول BGP بتوقيعات تشفيرية لكل قفزة (per-hop) تحمي الـ AS_PATH من التلاعب، فتقوّي الضمانات لكنها ترفع كلفة المعالج والذاكرة وتُعقّد النشر التدريجي.
>
> **نموذج فعالية التحقق.** إذا كانت نسبة $f$ من المسارات العالمية مغطّاة بـ ROAs، وكانت الأنظمة المستقلة المشاركة تطبّق "أسقِط غير الصحيح" (drop invalid)، فإن احتمال نجاح اختطاف عشوائي على مسار من طرف إلى طرف بطول $L$ يقارب $(1-f)^{L}$ (بافتراض تبنٍّ مستقل بين الأنظمة المستقلة)، وهذا يبرز تأثيرات الشبكة (network effects): فكل نظام تحقق إضافي يقلّل نجاح الاختطاف أُسّيًا عبر عمليات العبور.»

#### ③ الشرح الفهمي

شنو قصة BGP؟ هو بروتوكول التوجيه **بين** الأنظمة المستقلة (interdomain) — يعني هو اللي يخبر الإنترنت كله «هذي البادئة (prefix) موجودة عندي، وهذا المسار اللي يوصّلها». المشكلة الأساسية إنه مبني على **الثقة الضمنية (implicit trust)**: أي AS يعلن شي، الباقي يصدّقه من غير ما يتحقق. من هنا يجي سطح الهجوم.

نوعان من الهجوم:

| الهجوم | شنو يسوي | النتيجة |
|---|---|---|
| Prefix hijack / mis-origination | AS يعلن بادئة مو ملكه | حركة المرور تروح للمهاجم (interception) أو تختفي |
| Path shortening | يحذف قفزات من المسار ليصير "الأقصر" | يُفضَّل عليه لأن BGP يفضّل المسار الأقصر |

الحلول تجي على طبقتين:

| الحل | شنو يحمي بالضبط | كيف | الـ RFC |
|---|---|---|---|
| RPKI + ROAs | **الأصل (origin) فقط** | شهادة تربط البادئة بـ AS معيّن | RFC 6480 |
| BGP origin validation | تصنيف التحديث | valid / invalid / unknown | RFC 6811 |
| BGPsec | **المسار الكامل (AS_PATH)** | توقيع تشفيري لكل قفزة | RFC 8205 |

نقطة مهمة جدًا: **RPKI و BGPsec مو بدائل لبعض، هم مكمّلين.**
- RPKI يتأكد «هل AS الفلاني مسموح يعلن هالبادئة؟» ← يحمي الأصل بس.
- BGPsec يحمي المسار كامل ← يتأكد إن كل قفزة بالمسار ما تلاعبوا بيها.

يعني لو عندك RPKI بس، المهاجم ما يقدر يختطف الأصل، بس يقدر يلعب بالمسار. و BGPsec يسد هالثغرة، بس ثمنه CPU/memory عالية ونشر تدريجي صعب (لأنه يحتاج كل AS على المسار تدعمه).

نموذج الفعالية — ليش «تأثيرات الشبكة» مهمة:

$$P_{\text{hijack}} \approx (1-f)^{L}$$

| الرمز | المعنى |
|---|---|
| $f$ | نسبة المسارات العالمية المغطّاة بـ ROA |
| $L$ | طول المسار (عدد قفزات الـ ASes) |
| $(1-f)$ | احتمال إن القفزة الوحدة **مو** محميّة |
| $P_{\text{hijack}}$ | احتمال نجاح اختطاف عشوائي |

المعنى: كل قفزة إضافية تضرب نفسها مرّة ثانية. مثال: لو $f = 0.5$ و $L = 4$:

$$P_{\text{hijack}} \approx (0.5)^{4} = 0.0625 = 6.25\%$$

هذا اللي يقصدوه بـ **network effects**: كل AS إضافي يتبنّى التحقق يفيد الشبكة كلها، لأن أي مسار يمرّ بيه يصير محمي. والعكس: طالما التبنّي جزئي، فائدته محدودة.

### القسم 2 — 8. Time synchronization: NTP and reflection abuse (RFC 5905)

#### ① النص الأصلي

> NTP underpins log ordering, Kerberos ticket lifecycles, and TLS certificate validation. Misconfigured servers historically exposed commands (e.g., monlist) exploitable for reflection amplification DDoS. Current guidance disables legacy commands and restricts public exposure; correct implementation follows RFC 5905.
>
> **Amplification calculus.** For reflectors $j$ with request-to-response ratios $A_j$ and request rates $r_j$, victim ingress is $\sum_{j} A_j r_j$. Rate-limiting at the reflectors caps $r_j$, while upstream filtering (BCP 38) removes spoofed sources, pushing $\sum_{j} r_j$ toward zero.

#### ② الترجمة

> «يشكّل NTP الأساس لترتيب السجلات (log ordering)، ودورة حياة تذاكر Kerberos، والتحقق من صلاحية شهادات TLS. وقد كشفت الخوادم المُهيّأة بشكل خاطئ تاريخيًا عن أوامر (مثل monlist) قابلة للاستغلال في هجمات الانعكاس والتضخيم (reflection amplification DDoS). والإرشاد الحالي يعطّل الأوامر القديمة ويقيّد التعرض العام؛ والتنفيذ الصحيح يتبع RFC 5905.
>
> **حساب التضخيم.** بالنسبة للـ reflectors $j$ بنسب الرد إلى الطلب $A_j$ ومعدّلات الطلبات $r_j$، فإن الوارد عند الضحية هو $\sum_{j} A_j r_j$. وتحديد المعدّل (rate-limiting) عند الـ reflectors يحدّ $r_j$، أما الفلترة في المنبع (BCP 38) فتُزيل المصادر المزوّرة، مما يدفع $\sum_{j} r_j$ نحو الصفر.»

#### ③ الشرح الفهمي

ليش الوقت (time) أمنيًا مهم؟ لأنه أساس لثلاثة أشياء:
- ترتيب السجلات (log ordering) — التحقيق الجنائي يعتمد على توقيت الأحداث.
- عمر تذاكر Kerberos (ticket lifecycles) — صلاحية التذكرة مرتبطة بالوقت.
- التحقق من صلاحية شهادات TLS — هل الشهادة منتهية أو لا.

يعني لو انضرب الوقت (time shifting)، كل هذي تختل: ممكن تذكرة منتهية تشتغل، أو شهادة منتهية تبدو صالحة.

الاستغلال (reflection/amplification): خوادم NTP القديمة كانت تفتح أوامر مثل `monlist` اللي يرجّع قائمة آخر العملاء — طلب **صغير** ورد **كبير**. المهاجم يزوّر IP الضحية، فتروح الردود الكبيرة كلها للضحية ← DDoS.

معادلة الـ amplification:

$$R_{\text{victim}} = \sum_{j} A_j r_j$$

| الرمز | المعنى |
|---|---|
| $A_j$ | نسبة الرد إلى الطلب عند الـ reflector رقم $j$ |
| $r_j$ | معدّل الطلبات المرسلة إلى الـ reflector رقم $j$ |
| $R_{\text{victim}}$ | معدّل الوارد عند الضحية (ingress) |

كيف نحدّها؟ على طبقتين:
- **Rate-limiting عند الـ reflectors** ← يحدّ $r_j$ نفسه.
- **BCP 38 (upstream filtering)** ← يشيل المصادر المزوّرة (spoofed)، فالمهاجم ما يقدر يخلي الردود تروح للضحية ← $\sum_{j} r_j$ يقترب من الصفر.

الخلاصة العملية: تنفيذ متوافق مع RFC 5905، تعطيل الأوامر القديمة، وتقييد التعرض العام للخادم.

### القسم 3 — 9. Security of application transports: TLS 1.3 and the Web (RFC 8446)

#### ① النص الأصلي

> TLS 1.3 (RFC 8446) eliminates legacy ciphers, compressions, and renegotiation pitfalls, standardizes AEAD suites, and shortens handshakes with forward secrecy by default. When combined with HTTP/2 or HTTP/3, it provides authenticated, encrypted channels for most Web traffic, reducing passive surveillance and active tampering risks. However, enterprise inspection policies must reconcile visibility with end-to-end cryptography (e.g., via split-TLS proxies), which themselves become high-value targets.

#### ② الترجمة

> «يُلغي TLS 1.3 (RFC 8446) التشفيرات القديمة (legacy ciphers) والضغط ومزالق إعادة التفاوض (renegotiation)، ويوحّد أطقم AEAD، ويقصّر المصافحات (handshakes) مع السرّية الأمامية (forward secrecy) بشكل افتراضي. وعند دمجه مع HTTP/2 أو HTTP/3، يوفّر قنوات موثّقة ومشفّرة لمعظم حركة الويب، مما يقلّل خطر التنصّت السلبي (passive surveillance) والتلاعب النشط (active tampering). إلا أن سياسات التفتيش في المؤسسات يجب أن توفّق بين الرؤية (visibility) والتشفير من طرف إلى طرف (مثلًا عبر بروكسيات split-TLS)، وهذه البروكسيات نفسها تصبح أهدافًا عالية القيمة.»

#### ③ الشرح الفهمي

TLS 1.3 هو النسخة اللي «نظّفت» TLS من المشاكل التاريخية. شنو سوى بالضبط:

| اللي شاله / صلّحه | ليش كان مشكلة |
|---|---|
| legacy ciphers | تشفيرات قديمة ضعيفة (زي RC4 و 3DES) |
| compression | الضغط يفتح الباب لهجوم يستغل فرق حجم البيانات |
| renegotiation | مزالق إعادة التفاوض اللي تربك حالة الجلسة |

وشنو الجديد اللي ضافه:

| الميزة | المعنى |
|---|---|
| AEAD suites موحّدة | كل الأطقم المسموحة AEAD (زي AES-GCM و ChaCha20-Poly1305) |
| forward secrecy افتراضيًا | كسر مفتاح طويل الأمد ما يفكّ الجلسات القديمة |
| handshake أقصر | 1-RTT أو 0-RTT ← أسرع وأبسط |

مع HTTP/2 أو HTTP/3، يصير عندك قناة مشفّرة وموثّقة لمعظم حركة الويب ← يقلّل التنصّت السلبي والتلاعب النشط.

بس تظهر معضلة (dilemma): المؤسسات تريد تفتّش حركة المرور (inspection) للكشف عن التهديدات، بس TLS 1.3 يشفّر كل شي. الحل هو **split-TLS proxies** — بروكسي يفك التشفير، يفحص، وبعدين يعيد يشفّر. والمشكلة إن هذا البروكسي نفسه يصير **هدفًا عالي القيمة (high-value target)**: لو انكسر، كل حركة المؤسسة تصير مكشوفة. يعني حلّينا مشكلة الرؤية، وخلقنا نقطة فشل مركزية جديدة.

### القسم 4 — 10. Intradomain control: ICMP/ICMPv6 and control-plane hygiene

#### ① النص الأصلي

> ICMP communicates reachability and diagnostics. Filtering all ICMP breaks PMTU discovery and can degrade performance; selective filtering that blocks abuse patterns while allowing essential types (e.g., "fragmentation needed" for IPv4, "Packet Too Big" for IPv6) is a safer posture. IPv6 moves many control-plane functions (ND, RA) into ICMPv6; the security of these functions thus inherits the ND/RA considerations discussed earlier (RA-Guard/SEND).

#### ② الترجمة

> «ينقل ICMP معلومات الوصول (reachability) والتشخيص (diagnostics). وفلترة كل رسائل ICMP تكسر اكتشاف PMTU وقد تُدهور الأداء؛ أما الفلترة الانتقائية التي تحجب أنماط الاستغلال مع السماح بالأنواع الضرورية (مثل "fragmentation needed" في IPv4 و"Packet Too Big" في IPv6) فهي وضعية أكثر أمانًا. وينقل IPv6 الكثير من وظائف الطبقة التحكمية (ND و RA) إلى داخل ICMPv6؛ وبالتالي يرث أمان هذه الوظائف اعتبارات ND/RA التي نوقشت سابقًا (RA-Guard/SEND).»

#### ③ الشرح الفهمي

ICMP هو بروتوكول «الطبقة التحكمية» — ينقل معلومات الوصول (reachability) والتشخيص (diagnostics). الخطأ الشائع: منع ICMP كليًا. ليش غلط؟

لأنه يكسر **PMTU discovery** (اكتشاف وحدة النقل القصوى على المسار). لما تمنع رسائل ICMP الضرورية، الراوترات ما تقدر تخبر الأطراف «الرزمة كبيرة عليّ»، فتصير **black hole** — الاتصال يعلّق من غير سبب واضح.

الحل الصح: **فلترة انتقائية (selective filtering)** — تحجب أنماط الاستغلال بس تسمح بالأنواع الضرورية.

| الحالة | لازم تسمح | إذا منعتها |
|---|---|---|
| IPv4 PMTU | "fragmentation needed" | PMTU discovery ينكسر ← black hole |
| IPv6 PMTU | "Packet Too Big" | نفس المشكلة بـ IPv6 |
| ICMPv6 ND/RA | رسائل ND/RA | تفقد الـ autoconfiguration وتصير عرضة لـ rogue RA |

نقطة IPv6: أغلب وظائف الطبقة التحكمية (ND و RA) انتقلت داخل ICMPv6. يعني أمان ICMPv6 = أمان ND/RA ← يرث نفس المخاطر اللي مرّت سابقًا (rogue RA و neighbor poisoning)، وعلاجها RA-Guard و SEND. فإذا فلترت ICMPv6 كليًا، إما تكسر الـ IPv6 أو تترك نفسك مكشوف لهذي الهجمات.
