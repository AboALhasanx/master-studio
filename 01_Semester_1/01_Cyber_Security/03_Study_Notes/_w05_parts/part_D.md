### القسم 1 — 11. Formalizing protocol risk and control

#### ① النص الأصلي

> **11.1 Multi-protocol residual risk portfolio.** Let protocols $i \in \{\text{TCP, UDP, DNS, DHCP, BGP, NTP}, \dots\}$ carry an exploit probability $P_i$ and an impact $I_i$. With controls reducing exploit probability by efficacy $e_i \in [0,1]$, the residual risk aggregates as the risk-portfolio sum given below. This linear, ISO 27005-style model helps prioritize investment: deploying DNSSEC raises $e_{\text{DNS}}$ markedly, adopting RPKI raises $e_{\text{BGP}}$, and enforcing BCP 38 raises $e_{\text{UDP-reflect}}$. (DNSSEC and RPKI effectiveness and semantics: RFC 4033/4035; RFC 6480/6811.)
>
> **11.2 State-machine exposure.** Protocols with explicit state (TCP, BGP, ND) expose DoS vectors where an attacker inflates $|S|$, the number of concurrent state instances. Let $M$ be the maximum manageable state; let burst arrivals follow a Poisson process with rate $\lambda$, and let state duration have mean $1/\mu$. The expected number of concurrent states in an $M/M/\infty$ system is $\lambda/\mu$; if $\lambda/\mu \ge M$, the system saturates. Controls such as SYN cookies (TCP) or hard caps on peering sessions (BGP) reduce the realized $\lambda/\mu$ or increase $M$.
>
> **11.3 Attacker work-factor via entropy.** For off-path spoofing (e.g., pre-DNSSEC poisoning), increasing the number of unpredictable bits $H$ (TXID + source port) raises the attacker's expected attempts toward $2^{H-1}$ for a 50% chance of success. Randomized ephemeral ports and per-query entropy (0x20 encoding, source-port randomization) raised $H$ significantly, buying time for the DNSSEC rollout.

$$R_{\text{net}} = \sum_{i} (1 - e_i)\, P_i\, I_i$$

$$\frac{\lambda}{\mu} \ge M \;\Rightarrow\; \text{saturation}$$

$$E[N] \approx 2^{\,H-1}$$

#### ② الترجمة

> «**11.1 محفظة المخاطر المتبقية متعددة البروتوكولات (Multi-protocol residual risk portfolio).** خلّي البروتوكولات $i \in \{\text{TCP, UDP, DNS, DHCP, BGP, NTP}, \dots\}$ عندها احتمال استغلال $P_i$ وأثر $I_i$. ولمّا الضوابط تقلّل احتمال الاستغلال بفاعلية $e_i \in [0,1]$، فالمخاطر المتبقية تتجمّع بمجموع محفظة المخاطر اللي تحت. هذا النموذج الخطي (على طراز ISO 27005) يساعد على ترتيب أولويات الاستثمار: تنصيب DNSSEC يرفع $e_{\text{DNS}}$ بشكل واضح، وتبنّي RPKI يرفع $e_{\text{BGP}}$، وتطبيق BCP 38 يرفع $e_{\text{UDP-reflect}}$. (فاعلية DNSSEC و RPKI ودلالاتها: RFC 4033/4035؛ RFC 6480/6811.)
>
> **11.2 التعرّض عبر آلة الحالة (State-machine exposure).** البروتوكولات اللي عندها حالة صريحة (TCP، BGP، ND) تفتح نواقل DoS حيث المهاجم يضخّم $|S|$، أي عدد نسخ الحالة المتزامنة. خلّي $M$ أقصى حالة قابلة للإدارة؛ وخلّي وصول الدفعات يتبع عملية بواسون (Poisson) بمعدل $\lambda$، وخلّي مدة الحالة عندها متوسط $1/\mu$. عدد الحالات المتزامنة المتوقّع بنظام $M/M/\infty$ هو $\lambda/\mu$؛ وإذا $\lambda/\mu \ge M$، فالنظام يتشبّع (saturates). ضوابط مثل SYN cookies (TCP) أو سقوف صلبة على جلسات الـ peering (BGP) تقلّل $\lambda/\mu$ الفعلي أو ترفع $M$.
>
> **11.3 عامل شغل المهاجم عبر الإنتروبيا (Attacker work-factor via entropy).** للانتحال خارج المسار (off-path spoofing) — مثل تسميم ما قبل DNSSEC — زيادة عدد البتات غير القابلة للتنبؤ $H$ (TXID + source port) ترفع عدد المحاولات المتوقّعة للمهاجم نحو $2^{H-1}$ لفرصة نجاح 50%. عشوائية المنافذ العابرة (randomized ephemeral ports) والإنتروبيا لكل استعلام (ترميز 0x20، عشوائية منفذ المصدر) رفعت $H$ بشكل كبير، فاشترت وقتًا لطرح DNSSEC.»

#### ③ الشرح الفهمي

هذا القسم "يريّض" (formalizes) المخاطر بمعادلات، حتى ترتّب أولوياتك بالجهد والفلوس بدل الحدس. يقدّم ثلاث زوايا: **محفظة المخاطر** (كم بروتوكول ناقص ومجموعهم شكد)، **التعرّض عبر الحالة** (شنو يصير لمّا تتضخّم الحالات)، و**عامل شغل المهاجم** (شكد يكلّف المهاجم يتخمّن).

**11.1 — محفظة المخاطر:** كل بروتوكول عنده احتمال استغلال $P_i$ وأثر $I_i$. الضابط (control) ما يشيل الخطر كامل، يشيل بس نسبة $e_i$ منه، فاللي يبقى هو $(1-e_i)\,P_i I_i$؛ ونجمعهم على كل البروتوكولات ← $R_{net}$.

$$R_{\text{net}} = \sum_{i} (1 - e_i)\, P_i\, I_i$$

| الرمز | المعنى |
|---|---|
| $i$ | البروتوكول (TCP, UDP, DNS, DHCP, BGP, NTP, ...) |
| $P_i$ | احتمال استغلال البروتوكول $i$ (exploit probability) |
| $I_i$ | الأثر/الضرر إذا نجح الاستغلال (impact) |
| $e_i$ | فاعلية الضابط، من 0 (بلا فاعلية) إلى 1 (يمنع تمامًا) |
| $(1-e_i)$ | الاحتمال المتبقي بعد تطبيق الضابط |
| $R_{net}$ | المخاطر المتبقية الكلية على مستوى الشبكة |

نقطة الاستعمال: هذا نموذج **خطي** بسيط، مو دقيق 100%، بس وظيفته **ترتيب الأولويات**: إذا رفعت $e_i$ لأكبر حاصل $P_i I_i$، تنزل $R_{net}$ أكثر. مثلاً DNSSEC يرفع $e_{DNS}$، RPKI يرفع $e_{BGP}$، و BCP 38 يرفع $e_{UDP-reflect}$ (لأنه يمنع الانتحال من الأصل).

**11.2 — التعرّض عبر آلة الحالة:** كل بروتوكول عنده "حالة" (connection state، session، neighbor entry) يقدر المهاجم يستغلها إذا ضخّم عدد الحالات المتزامنة $|S|$. بنموذج الطابور $M/M/\infty$:

$$\frac{\lambda}{\mu} \ge M \;\Rightarrow\; \text{saturation}$$

| الرمز | المعنى |
|---|---|
| $\lambda$ | معدل وصول الحالات الجديدة (burst arrivals, Poisson) |
| $\mu$ | معدل "الخدمة"/إنهاء الحالة |
| $1/\mu$ | متوسط عمر الحالة |
| $M$ | أقصى عدد حالات يتحمّله النظام |
| $\lambda/\mu$ | متوسط عدد الحالات المتزامنة المتوقّع |

القاعدة: إذا $\lambda/\mu \ge M$ ← النظام يتشبّع ويصير DoS. الضوابط إما تنزّل $\lambda/\mu$ الفعلي (SYN cookies: ما تحفظ حالة إلا بعد ACK، فتصير الحالة أرخص وأقصر) أو ترفع $M$ (سقوف الـ peering بالـ BGP).

**11.3 — عامل شغل المهاجم:** إذا المهاجم **خارج المسار** (ما يشوف الرد)، لازم يخمّن القيمة غير المتوقّعة. عدد البتات السرّية $H$ يحدّد كلفة التخمين:

$$E[N] \approx 2^{\,H-1}$$

| الرمز | المعنى |
|---|---|
| $H$ | عدد البتات غير القابلة للتنبؤ (مثلاً 16-bit TXID + 16-bit source port = 32 بت) |
| $E[N]$ | عدد المحاولات المتوقّعة للمهاجم للوصول لفرصة نجاح 50% |
| $2^{\,H-1}$ | نصف فضاء الاحتمالات (نصف $2^H$) اللازم لتغطية 50% من الاحتمالات |

علاقة مهمة: كل ما تزيد $H$ بواحد، الكلفة **تتضاعف** (نمو أُسّي). لهذا عشوائية المنفذ وترميز 0x20 رفعوا $H$ و"اشتروا وقتًا" لحد ما ينتشر DNSSEC. بس نقطة جوهرية: هذا **دفاع احتمالي** (probabilistic) — يصعّب الهجوم، ما يمنعه جذريًا؛ اللي يمنعه جذريًا هو التحقق التشفيري (cryptographic validation).

---

### القسم 2 — 12. Protocol-specific vulnerability précis and mitigations

#### ① النص الأصلي

> This précis pairs each protocol's canonical weakness with its standard mitigation.
>
> **TCP**
>
> - Attacks: SYN flood; RST injection on long-haul links; session hijacking where sequence-number windows are predictable.
> - Mitigations: SYN cookies, short half-open timers, TCP-AO for authenticated options in sensitive contexts, and BCP 38 to suppress spoofing.
>
> **UDP**
>
> - Attacks: reflection/amplification (DNS, NTP, SSDP).
> - Mitigations: anti-spoofing (BCP 38), rate-limiting on reflectors, disabling legacy commands, and response-size limiting.
>
> **DNS**
>
> - Attacks: cache poisoning, Kaminsky-style "race," interception by rogue resolvers.
> - Mitigations: DNSSEC validation (authoritative + recursive), source-port randomization as a stop-gap, and DoT/DoH to encrypt the path.
>
> **DHCP**
>
> - Attacks: rogue server, starvation (exhausting pools), MITM via malicious options.
> - Mitigations: DHCP snooping at switches, 802.1X/NAC, private VLANs; RFC 3118 authentication where feasible.
>
> **IPv6 ND/RA**
>
> - Attacks: rogue RA, neighbor-table poisoning.
> - Mitigations: RA-Guard with full header-chain parsing; SEND for cryptographic assurance in high-assurance environments.
>
> **BGP**
>
> - Attacks: prefix hijack/mis-origination; path shortening.
> - Mitigations: RPKI/ROAs with origin validation (drop invalid), BGPsec for path validation, and prefix filtering with IRR/RPKI hygiene.
>
> **NTP**
>
> - Attacks: reflection via legacy commands; time shifting for authentication disruption.
> - Mitigations: RFC 5905-compliant configurations, restrict mode 6/7, authenticated associations for critical domains.
>
> **TLS/HTTP**
>
> - Attacks: legacy protocol downgrade, weak ciphersuites, compression or renegotiation bugs (largely removed in TLS 1.3); HTTP/2 abuse (header flooding).
> - Mitigations: enforce TLS 1.3, strict cipher policy, ALPN pinning, and request/stream limits for HTTP/2 and HTTP/3.

#### ② الترجمة

> «هذا الملخّص الدقيق (précis) يقارن الضعف القانوني (canonical weakness) لكل بروتوكول ← التخفيف المعياري (standard mitigation) الخاص بيه.
>
> **TCP**
>
> - الهجمات (Attacks): فيضان SYN (SYN flood)؛ حقن RST على الروابط الطويلة (RST injection on long-haul links)؛ اختطاف الجلسة (session hijacking) لمّا تكون نوافذ أرقام التسلسل قابلة للتنبؤ.
> - التخفيفات (Mitigations): SYN cookies، مؤقتات نصف-مفتوحة قصيرة (short half-open timers)، TCP-AO للخيارات الموثّقة بالسياقات الحساسة، و BCP 38 لكبت الانتحال.
>
> **UDP**
>
> - الهجمات: الانعكاس/التضخيم (reflection/amplification) عبر DNS و NTP و SSDP.
> - التخفيفات: مكافحة الانتحال (BCP 38)، تحديد المعدّل (rate-limiting) على المنعكسات (reflectors)، تعطيل الأوامر القديمة، وتحديد حجم الرد.
>
> **DNS**
>
> - الهجمات: تسميم الذاكرة المؤقتة (cache poisoning)، "سباق" على طريقة Kaminsky، الاعتراض عبر resolvers خبيثة.
> - التخفيفات: تحقق DNSSEC (عند الـ authoritative والـ recursive)، عشوائية منفذ المصدر كحل مؤقّت (stop-gap)، و DoT/DoH لتشفير المسار.
>
> **DHCP**
>
> - الهجمات: سيرفر خبيث (rogue server)، الاستنزاف (starvation) بإفراغ المجمّعات (pools)، وهجوم رجل-بالوسط (MITM) عبر خيارات خبيثة.
> - التخفيفات: DHCP snooping عند السويتشات، 802.1X/NAC، private VLANs؛ ومصادقة RFC 3118 حيثما يكون ذلك ممكنًا.
>
> **IPv6 ND/RA**
>
> - الهجمات: إعلان راوتر خبيث (rogue RA)، تسميم جدول الجيران (neighbor-table poisoning).
> - التخفيفات: RA-Guard مع تحليل سلسلة الهيدرات كاملة؛ SEND للضمان التشفيري ببيئات الضمان العالي.
>
> **BGP**
>
> - الهجمات: اختطاف/سوء إسناد البادئة (prefix hijack/mis-origination)؛ تقصير المسار (path shortening).
> - التخفيفات: RPKI/ROAs مع تحقق الأصل (origin validation) وإسقاط الـ invalid، BGPsec لتحقق المسار، وتصفية البادئات مع نظافة IRR/RPKI.
>
> **NTP**
>
> - الهجمات: الانعكاس عبر الأوامر القديمة؛ تحويل الوقت (time shifting) لتعطيل المصادقة.
> - التخفيفات: إعدادات متوافقة مع RFC 5905، تقييد mode 6/7، وروابط موثّقة (authenticated associations) للنطاقات الحرجة.
>
> **TLS/HTTP**
>
> - الهجمات: تخفيض البروتوكول القديم (protocol downgrade)، مجموعات تشفير ضعيفة (weak ciphersuites)، أخطاء الضغط أو إعادة التفاوض (أُزيلت غالبًا في TLS 1.3)؛ إساءة استعمال HTTP/2 (فيضان الهيدرات).
> - التخفيفات: فرض TLS 1.3، سياسة تشفير صارمة، تثبيت ALPN، وحدود الطلبات/الجداول لـ HTTP/2 و HTTP/3.»

#### ③ الشرح الفهمي

هذا القسم جدول مرجعي سريع: لكل بروتوكول **الضعف** ← **التخفيف**. احفظه كأزواج، مو كقائمة منفصلة، لأن بالامتحان غالبًا يسأل "شنو ضعف X وشنو علاجه؟".

| البروتوكول | الضعف (Weakness) | التخفيف (Mitigation) |
|---|---|---|
| **TCP** | SYN flood؛ حقن RST؛ اختطاف جلسة (نوافذ تسلسل متوقّعة) | SYN cookies؛ مؤقتات half-open قصيرة؛ TCP-AO؛ BCP 38 |
| **UDP** | انعكاس/تضخيم (DNS, NTP, SSDP) | مكافحة الانتحال (BCP 38)؛ rate-limiting على المنعكسات؛ تعطيل الأوامر القديمة؛ تحديد حجم الرد |
| **DNS** | تسميم الكاش؛ سباق Kaminsky؛ اعتراض من resolvers خبيثة | تحقق DNSSEC؛ عشوائية منفذ المصدر (مؤقّت)؛ DoT/DoH |
| **DHCP** | سيرفر خبيث؛ استنزاف المجمّع؛ MITM بخيارات خبيثة | DHCP snooping؛ 802.1X/NAC؛ private VLANs؛ مصادقة RFC 3118 |
| **IPv6 ND/RA** | rogue RA؛ تسميم جدول الجيران | RA-Guard مع تحليل سلسلة الهيدرات؛ SEND |
| **BGP** | اختطاف/سوء إسناد بادئة؛ تقصير المسار | RPKI/ROAs + origin validation؛ BGPsec؛ تصفية بادئات (IRR/RPKI) |
| **NTP** | انعكاس بأوامر قديمة؛ تحويل الوقت | إعداد RFC 5905؛ تقييد mode 6/7؛ روابط موثّقة |
| **TLS/HTTP** | downgrade؛ تشفير ضعيف؛ أخطاء ضغط/إعادة تفاوض؛ إساءة HTTP/2 | فرض TLS 1.3؛ سياسة تشفير صارمة؛ ALPN pinning؛ حدود الطلبات/الجداول |

قراءة الجدول: كل صف = زوج "هجوم ← علاج". لاحظ إن **BCP 38** يتكرّر (TCP و UDP) لأنه يعالج جذر المشكلة — الانتحال. ولاحظ إن **DNSSEC** يخص **البيانات**، بينما **DoT/DoH** يخصّون **المسار** (قناة الـ resolver). هذي التفاصيل تجيب عليها بالامتحان.

---

### القسم 3 — 13. Case analysis: DNS cache poisoning as a design-level lesson

#### ① النص الأصلي

> The 2008 DNS event illustrated how probabilistic defenses can be outpaced by well-resourced adversaries, and why cryptographic validation is a qualitatively different control. Emergency source-port randomization raised the entropy of the race but did not change DNS's trust model; DNSSEC did. The coordinated response — multivendor patches plus guidance — remains a canonical example of upgrading a critical protocol without breaking the Internet.

#### ② الترجمة

> «حدث الـ DNS سنة 2008 وضّح كيف إن الدفاعات الاحتمالية (probabilistic defenses) يمكن تتجاوزها من خصوم ذوي موارد قوية، وليش التحقق التشفيري (cryptographic validation) ضابط من نوع مختلف جذريًا (qualitatively different). العشوائية الطارئة لمنفذ المصدر رفعت إنتروبيا السباق، بس ما غيّرت نموذج الثقة (trust model) بالـ DNS؛ اللي غيّره هو DNSSEC. والاستجابة المنسّقة — تحديثات من عدة شركات (multivendor patches) مع إرشادات — تبقى مثالًا نموذجيًا على ترقية بروتوكول حرج بدون كسر الإنترنت.»

#### ③ الشرح الفهمي

الدرس الأساسي: الفرق بين **دفاع احتمالي** و**دفاع تشفيري**. الأول يصعّب الهجوم بس يبقى ممكنًا إذا المهاجم قوي؛ الثاني يقطعه من الأساس.

| البُعد | عشوائية منفذ المصدر (Probabilistic) | DNSSEC (Cryptographic) |
|---|---|---|
| شنو يزيد/يغيّر | يزيد الإنتروبيا $H$ ← يرفع عدد المحاولات $E[N]$ | يتحقق من توقيع RRSIG ← يمنع قبول أي بيانات غير موقّعة |
| هل يغيّر نموذج الثقة؟ | لا (نفس trust model) | نعم (يضيف سلسلة ثقة ← chain of trust) |
| أمام مهاجم قوي الموارد | يمكن يتجاوزه (outpaced) | يمنعه جذريًا |
| طبيعته | حل مؤقّت (stop-gap) | إصلاح معماري (architectural fix) |

نقطة "درس التصميم" (design-level lesson): لمّا البروتوكول مبني على افتراض ثقة (implicit trust)، فأي ترقيع احتمالي يبقى هشّ. الإصلاح الحقيقي يجي من داخل التصميم نفسه (تشفير وتحقّق). والنقطة الثانية: الترقية ممكنة **بدون كسر الإنترنت** إذا كانت منسّقة بين كل المصنّعين — وهذا اللي صار فعلاً سنة 2008.

---

### القسم 4 — 14. Toward robust networks: governance and deployment realities

#### ① النص الأصلي

> Standards codify mitigations, but risk depends on deployment. BCP 38's effectiveness scales with adoption; RPKI's benefits compound with more ROAs and more validating ASes; and DNSSEC validation at recursors helps even when many zones are unsigned — it still prevents off-path poisoning of signed responses and improves validation telemetry. Organizations should therefore treat protocol security as an ecosystem program, not a one-time toggle.

#### ② الترجمة

> «المعايير (standards) تُقنّن التخفيفات، بس الخطر يعتمد على التنفيذ الفعلي (deployment). فاعلية BCP 38 تتدرّج مع نسبة التبنّي (adoption)؛ وفوائد RPKI تتراكم مع زيادة عدد الـ ROAs وزيادة الـ ASes اللي تتحقق (validating)؛ وتحقق DNSSEC عند الـ recursors يفيد حتى لمّا تكون نطاقات كثيرة غير موقّعة (unsigned) — لأنه يبقى يمنع التسميم خارج المسار للردود الموقّعة ويحسّن قياسات التحقق (validation telemetry). لهذا المؤسسات لازم تتعامل مع أمن البروتوكولات كبرنامج بيئي متكامل (ecosystem program)، مو كمفتاح يُشغَل مرة واحدة (one-time toggle).»

#### ③ الشرح الفهمي

الفكرة المحورية: **وجود المعيار ≠ وجود الحماية**. الحماية الحقيقية تعتمد على **التبنّي** (deployment / adoption)، وهذا يخلق **تأثيرات شبكية** (network effects): كل ما يزيد عدد المشاركين، تزيد الفاعلية أسّيًا.

| الضابط (Control) | يعتمد على | التأثير الشبكي (Network effect) |
|---|---|---|
| **BCP 38** | نسبة تبنّي مزوّدي الخدمة | كل ما زاد التبنّي، قلّ الانتحال القادم من مصادرهم |
| **RPKI** | عدد الـ ROAs + عدد الـ validating ASes | الفوائد تتراكم (compound) مع زيادة الاثنين معًا |
| **DNSSEC** | تحقق عند الـ recursors | يفيد حتى لو نطاقات كثيرة غير موقّعة: يمنع التسميم خارج المسار للردود الموقّعة + يحسّن الـ telemetry |

الخلاصة العملية: لا تتعامل مع أمن البروتوكولات كـ **مفتاح ON/OFF** (one-time toggle)، بل كـ **برنامج مستمر** (ecosystem program) يتطوّر مع تبنّي بقية العالم — وهذا هو المعنى العملي للانتقال من "المعيار موجود" إلى "الشبكة فعلاً محمية".
