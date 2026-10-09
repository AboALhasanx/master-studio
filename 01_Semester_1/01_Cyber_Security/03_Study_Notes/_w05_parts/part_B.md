### القسم 1 — 4. Network layer: IPv4/IPv6, spoofing, fragmentation, and ND/RA
#### ① النص الأصلي
> **4.1 IPv4/IPv6 source spoofing and ingress controls (RFC 2827 / BCP 38)**
>
> IP permits endpoints to set their own source addresses, so attackers can forge ("spoof") sources to hide their origin, defeat naive filters, and enable reflection. BCP 38 (RFC 2827) mandates ingress filtering at provider edges so that only topologically valid source addresses traverse upstream; despite its age, universal deployment remains incomplete.
>
> **4.2 IPv6 Neighbor Discovery, rogue RA, and SEND/RA-Guard (RFC 3971 SEND · RFC 6105 RA-Guard)**
>
> IPv6 replaces ARP with Neighbor Discovery (ND) and uses Router Advertisements (RAs) for autoconfiguration. Both can be forged to perform on-link MITM or route black-holing. SEND (RFC 3971) secures ND via Cryptographically Generated Addresses and signatures but is operationally heavy. RA-Guard (RFC 6105 + RFC 7113) adds L2 filtering for RAs but must parse the full IPv6 header chain to resist evasion via extension headers.
>
> **4.3 IPv6 extension headers: filtering and survivability**
>
> IPv6 extension headers complicate middlebox processing, and ambiguities historically allowed evasion (e.g., hiding RA inside crafted chains). Updates clarify handling (RFC 7045) and ongoing work tightens hop-by-hop processing guidance, but operational filtering of exotic header combinations remains prudent in high-speed fabrics. A finite-state parsing model treats the legal header chains as a DFA $H = (S, \Sigma, \delta, s_0, F)$, where states $S$ represent "next header expected" classes; a middlebox that accepts only $x \in \Sigma^{*}$ with $\delta(s_0, x) \in F$ thwarts many header-chain evasions, with performance bounds depending on $|x|$ (chain length) and per-transition cost.

$$H = (S, \Sigma, \delta, s_0, F), \qquad x \text{ accepted} \iff \delta(s_0, x) \in F$$

#### ② الترجمة
> «**4.1 انتحال المصدر في IPv4/IPv6 وضوابط الدخول (ingress controls) — RFC 2827 / BCP 38**
>
> بروتوكول IP يسمح للأطراف (endpoints) إنها تحدّد عنوان المصدر بنفسها، فلهذا المهاجم يقدر يزوّر ("ينتحل") المصدر ليخفي أصله، ويكسر الفلاتر الساذجة (naive filters)، ويفعّل الانعكاس (reflection). معيار BCP 38 (RFC 2827) يفرض ترشيح الدخول (ingress filtering) عند حدود مزوّد الخدمة، بحيث ما تعبر للأعلى إلا عناوين المصدر الصحيحة طوبولوجياً؛ ورغم قِدمه، النشر الشامل ما زال ناقصاً.
>
> **4.2 استكشاف الجيران في IPv6 (ND)، وإعلانات الموجّه المزوّرة (rogue RA)، و SEND/RA-Guard — RFC 3971 SEND · RFC 6105 RA-Guard**
>
> IPv6 يستبدل ARP بـ Neighbor Discovery (ND) ويستخدم إعلانات الموجّه (RAs) للتكوين التلقائي (autoconfiguration). الاثنين يقدرون يتزوّرون لتنفيذ هجوم رجل بالوسط على الرابط (on-link MITM) أو حجب التوجيه (route black-holing). بروتوكول SEND (RFC 3971) يؤمّن الـ ND عبر العناوين المولّدة تشفيرياً (Cryptographically Generated Addresses) والتوقيعات، بس ثقيل عملياً. أما RA-Guard (RFC 6105 + RFC 7113) فيضيف ترشيح L2 للـ RAs، بس لازم يحلّل سلسلة ترويسات IPv6 كاملة لمقاومة التهرّب (evasion) عبر ترويسات الامتداد (extension headers).
>
> **4.3 ترويسات الامتداد في IPv6: الترشيح وقابلية البقاء (survivability)**
>
> ترويسات الامتداد في IPv6 تعقّد معالجة الأجهزة الوسيطة (middlebox)، والغموض سابقاً سمح بالتهرّب (مثلاً إخفاء RA داخل سلاسل مُصمّمة). التحديثات توضّح المعالجة (RFC 7045) والعمل الجاري يشدد إرشادات معالجة hop-by-hop، بس الترشيح التشغيلي لتراكيب الترويسات الغريبة يبقى حكمة في الشبكات عالية السرعة. نموذج التحليل بالحالات المحدودة (finite-state) يتعامل مع سلاسل الترويسات القانونية كنموذج DFA $H = (S, \Sigma, \delta, s_0, F)$، حيث الحالات $S$ تمثّل أصناف "الترويسة التالية المتوقّعة"؛ والجهاز الوسيط اللي يقبل فقط $x \in \Sigma^{*}$ بحيث $\delta(s_0, x) \in F$ يمنع كثير من عمليات التهرّب بسلاسل الترويسات، مع حدود أداء تعتمد على $|x|$ (طول السلسلة) وكلفة كل انتقال.»

#### ③ الشرح الفهمي
طبقة الشبكة (Network layer) هي اللي تتحكم بالعناوين والتوجيه، وهاي بالضبط نقطة ضعفها: **IP ما عندە مصادقة على عنوان المصدر** — يعني أي جهاز يقدر يحطّ أي عنوان مصدر يريده. من هاي الثغرة تطلع ثلاث عائلات:

| الهجوم | الطبقة | المعيار | العلاج |
|---|---|---|---|
| **Source spoofing** | IP | BCP 38 / RFC 2827 | ingress filtering عند حدود المزوّد |
| **Rogue RA / ND poisoning** | IPv6 (L2/L3) | RFC 3971 (SEND)، RFC 6105/7113 (RA-Guard) | ترشيح L2 + توقيعات CGA |
| **Extension-header evasion** | IPv6 | RFC 7045، RFC 7113 | تحليل سلسلة الترويسات كاملة (DFA) |

الفكرة المهمة بالانتحال: لمّا يكون المصدر مزوّر، المهاجم يخفي أصله ويفعّل الانعكاس (reflection) — وهذا هو أساس هجمات UDP amplification اللي نشوفها بعدين.

بالـ IPv6 القصة تختلف: ما كو ARP، بداله **ND** و **RA** للتكوين التلقائي. بما إنهن بلا مصادقة، أي واحد يقدر يبعت RA مزوّر ويصير رجل بالوسط (MITM) أو يحجب التوجيه. الحلول: **SEND** (توقيعات + CGA، بس ثقيل عملياً) و **RA-Guard** (ترشيح L2). بس RA-Guard عنده مصيدة: إذا ما حلّل **سلسلة الترويسات كاملة**، المهاجم يخبّي الـ RA داخل extension headers ويتجاوزه.

لهذا جاء **نموذج الـ DFA**: نعرّف "شكل الترويسة القانوني" كآلة حالات محدودة، وأي سلسلة تطلع خارج الحالات المقبولة تنرفض. المعادلة برا الصندوق توضّح: نقبل $x$ بس إذا $\delta(s_0, x) \in F$.

---

### القسم 2 — 5. Naming: DNS, DNSSEC, and encrypted resolution (DoT/DoH)
#### ① النص الأصلي
> **5.1 Classic DNS weaknesses and the Kaminsky cache-poisoning episode**
>
> Traditional DNS uses 16-bit transaction IDs, UDP source ports, and no authentication. In 2008, a generalized cache-poisoning technique showed that an attacker sending floods of forged replies during a resolver's query window could inject false records with modest effort; emergency patches randomized source ports to expand entropy, but the architectural fix is DNSSEC (origin authentication and integrity via signed zones). In an entropy model, if a resolver randomizes a 16-bit TXID and a 16-bit UDP source port, an off-path attacker must guess a 32-bit value, so the success probability per forged reply is $p = 2^{-32}$; with $m$ guesses during the race window, success probability is $1 - (1-p)^{m}$. Rate-limiting and response pacing cap $m$, while DNSSEC eliminates guessing by cryptographically validating RRSIGs.
>
> **5.2 DNSSEC: signed answers and the chain of trust (RFC 4033/4035)**
>
> DNSSEC introduces new record types (DNSKEY, RRSIG, DS, NSEC/X) and the concept of a signed zone with validation along a hierarchical chain of trust from the root. Validating resolvers reject tampered data, preventing cache poisoning regardless of off-path spoofing capabilities.
>
> **5.3 Resolver-to-recursor privacy: DoT and DoH (DoT = RFC 7858 · DoH = RFC 8484)**
>
> To mitigate local passive surveillance and manipulation, DNS-over-TLS (RFC 7858) and DNS-over-HTTPS (RFC 8484) encrypt the resolver channel. DoT uses TLS on port 853; DoH maps DNS exchanges into HTTPS requests, inheriting HTTP's authentication and caching. These mechanisms complement, not replace, DNSSEC: DoT/DoH protect the path; DNSSEC protects the data.

$$p = 2^{-32}, \qquad P(\text{success}) = 1 - (1-p)^{m}$$

#### ② الترجمة
> «**5.1 نقاط ضعف DNS الكلاسيكي وحادثة تسميم الكاش (Kaminsky cache-poisoning)**
>
> الـ DNS التقليدي يستخدم معرّفات معاملات (transaction IDs) بحجم 16-bit، ومنافذ مصدر UDP، وبدون أي مصادقة. في 2008، تقنية عامة لتسميم الكاش (cache poisoning) أظهرت إن المهاجم اللي يرسل سيولاً من الردود المزوّرة خلال نافذة استعلام الـ resolver يقدر يحقن سجلات كاذبة بجهد متواضع؛ والتحديثات الطارئة عشّرت منافذ المصدر لتوسيع العشوائية (entropy)، بس الحل المعماري هو DNSSEC (مصادقة الأصل (origin authentication) والسلامة (integrity) عبر المناطق الموقّعة (signed zones)). في نموذج العشوائية (entropy model)، إذا الـ resolver عشّر معرّف TXID بحجم 16-bit ومنفذ مصدر UDP بحجم 16-bit، فالمهاجم خارج المسار (off-path) لازم يخمّن قيمة بحجم 32-bit، فاحتمال النجاح لكل رد مزوّر هو $p = 2^{-32}$؛ ومع $m$ محاولة خلال نافذة السباق (race window)، احتمال النجاح هو $1 - (1-p)^{m}$. تحديد المعدّل (rate-limiting) وتهدئة الردود (response pacing) يحدّان من $m$، بينما DNSSEC يلغي التخمين عبر التحقّق التشفيري من توقيعات RRSIG.
>
> **5.2 DNSSEC: الردود الموقّعة وسلسلة الثقة (chain of trust) — RFC 4033/4035**
>
> DNSSEC يقدّم أنواع سجلات جديدة (DNSKEY، RRSIG، DS، NSEC/X) ومفهوم المنطقة الموقّعة (signed zone) مع التحقّق على طول سلسلة ثقة هرمية تبدأ من الجذر (root). الـ resolvers المتحقّقة ترفض البيانات المتلاعب بها، فتمنع تسميم الكاش بغض النظر عن قدرات الانتحال خارج المسار.
>
> **5.3 خصوصية Resolver-to-recursor: DoT و DoH — DoT = RFC 7858 · DoH = RFC 8484**
>
> لتخفيف المراقبة السلبية المحلية (passive surveillance) والتلاعب، تشفّر DNS-over-TLS (RFC 7858) و DNS-over-HTTPS (RFC 8484) قناة الـ resolver. الـ DoT يستخدم TLS على المنفذ 853؛ والـ DoH يحوّل تبادلات DNS إلى طلبات HTTPS، فيرث مصادقة HTTP والتخزين المؤقت (caching). هذي الآليات تكمّل DNSSEC ولا تستبدله: DoT/DoH يحميان المسار (the path)؛ و DNSSEC يحمي البيانات (the data).»

#### ③ الشرح الفهمي
الـ DNS هو "دفتر هاتف الإنترنت": يحوّل الاسم (google.com) إلى عنوان IP. المشكلة إنه بُني من الأساس **بدون مصادقة** — فالثقة عمياء، والـ resolver يقبل أي رد يوصل. من هنا تطلع ثغرتين منفصلتين:

| المشكلة | السبب | العلاج |
|---|---|---|
| **تسميم الكاش (cache poisoning)** | TXID 16-bit + منفذ 16-bit فقط، وبلا مصادقة | تعشير المنافذ (stop-gap) + **DNSSEC** |
| **المراقبة/التلاعب على المسار** | استعلامات نصّ صريح (plaintext) على UDP/53 | **DoT** (RFC 7858) / **DoH** (RFC 8484) |

**حادثة Kaminsky (2008):** المهاجم يغرق الـ resolver بردود مزوّرة خلال نافذة السباق (race window) قبل ما يوصل الرد الحقيقي. التحديث الطارئ كان يعشّر منافذ المصدر، فصار المهاجم لازم يخمّن قيمة **32-bit** (16 من TXID + 16 من المنفذ). احتمال النجاح لكل رد = $p = 2^{-32}$ تقريباً واحد من 4 مليار — بس مع $m$ محاولة يطلع الاحتمال $1 - (1-p)^{m}$. لهذا **rate-limiting** يقلّل $m$، و **DNSSEC** يصفّي الموضوع كلياً لأن الرد صار موقّع ومتحقَّق منه تشفيرياً.

الفرق الجوهري اللي ركز عليه بالامتحان: **DoT/DoH يحميان المسار (the path) — DNSSEC يحمي البيانات (the data).** الاثنين مكمّلين لبعض، ما واحد بديل عن الثاني.

![أمن التسمية: DNS ← DNSSEC ← DoT/DoH|720](../06_Diagrams_&_Mindmaps/cy_w5_dns_trust.svg)

---

### القسم 3 — 6. Address configuration: DHCP and its security gaps
#### ① النص الأصلي
> DHCP automates IP configuration but historically lacked authentication, enabling rogue DHCP servers and traffic redirection. RFC 3118 specifies DHCP message authentication but saw limited deployment due to key management and performance concerns; in practice, enterprises rely on DHCP snooping at switches and 802.1X/NAC to bind ports to legitimate servers and clients. A risk-aggregation model lets attack types $i$ (rogue server, starvation, MITM) have probability $P_i$ and impact $I_i$, giving residual risk $R_{DHCP} = \sum_i (1 - e_i) P_i I_i$, where $e_i \in [0,1]$ represents control efficacy (for example, snooping blocks rogue servers with $e$ near 1; RFC 3118, if operational, would further reduce $P_i$). This simple model supports prioritizing L2 controls when RFC 3118 is impractical.

$$R_{DHCP} = \sum_i (1 - e_i)\, P_i\, I_i$$

#### ② الترجمة
> «DHCP يؤتمت تكوين الـ IP بس تاريخياً كان بلا مصادقة، وهذا فتح الباب لخوادم DHCP المزوّرة (rogue DHCP servers) وإعادة توجيه الحركة (traffic redirection). المعيار RFC 3118 يحدّد مصادقة رسائل DHCP بس نشره كان محدود بسبب إدارة المفاتيح (key management) ومخاوف الأداء؛ وعملياً، المؤسسات تعتمد على DHCP snooping عند السويتشات و 802.1X/NAC لربط المنافذ بخوادم/عملاء شرعيين. نموذج تجميع المخاطر (risk-aggregation) يخلّي أنواع الهجوم $i$ (خادم مزوّر، استنزاف (starvation)، MITM) لها احتمال $P_i$ وتأثير $I_i$، فينتج خطر متبقٍ $R_{DHCP} = \sum_i (1 - e_i) P_i I_i$، حيث $e_i \in [0,1]$ تمثّل فاعلية الضابط (control efficacy) (مثلاً، الـ snooping يمنع الخوادم المزوّرة بـ $e$ قريب من 1؛ و RFC 3118، لو اشتغل، راح يقلّل $P_i$ أكثر). هذا النموذج البسيط يدعم ترجيح ضوابط الطبقة الثانية (L2) لما يكون RFC 3118 غير عملي.»

#### ③ الشرح الفهمي
الـ DHCP هو اللي يعطي الأجهزة إعداداتها (IP، البوابة، الـ DNS) تلقائياً. بما إنه بلا مصادقة، أي جهاز يقدر يشتغل كخادم DHCP ووزّع إعدادات غلط — والنتيجة **إعادة توجيه الحركة** أو MITM. ثلاث هجمات أساسية:

| الهجوم | الوصف | العلاج |
|---|---|---|
| **Rogue DHCP server** | خادم مزوّر يوزّع بوابة/DNS خبيثة | DHCP snooping عند السويتش |
| **Starvation** | استنزاف مجمّع العناوين (pool exhaustion) | port security / snooping |
| **MITM عبر خيارات خبيثة** | توجيه حركة الضحية عبر المهاجم | 802.1X / NAC |

**RFC 3118** يعرّف مصادقة رسائل DHCP، بس ما انتشر بسبب تعقيد إدارة المفاتيح وكلفة الأداء. لهذا الواقع المؤسسي اعتمد على ضوابط **الطبقة الثانية (L2)** — الـ snooping و 802.1X/NAC تربط المنفذ بخادم شرعي.

**نموذج المخاطر المتبقية:** الخطر المتبقي = مجموع (1 − فاعلية الضابط) × الاحتمال × التأثير. المعنى: كل ما زادت فاعلية $e_i$ اقترب الحد من الصفر. مثلاً الـ snooping عندە $e$ قريب من 1 للخادم المزوّر، فلو RFC 3118 غير عملي، الأفضل نرجّح ضوابط الـ L2.

$$R_{DHCP} = \sum_i (1 - e_i)\, P_i\, I_i$$
