### القسم 1 — 1. Purpose and scope

#### ① النص الأصلي

> Modern software systems live on networks, so their security posture depends not only on application code but also on the behavior and weaknesses of the protocols that move, resolve, route, and time their packets. This chapter surveys the core Internet protocols — link, network, transport, name resolution, routing, timing, and selected application protocols — analyzes their canonical vulnerabilities, and frames mitigation strategies grounded in standards. Where helpful, compact mathematical models formalize attack surfaces and control efficacy.

#### ② الترجمة

> «الأنظمة البرمجية الحديثة تعيش على الشبكات، فموقفها الأمني يعتمد مو بس على كود التطبيق، بل كذلك على سلوك وثغرات البروتوكولات اللي تنقل الحزم وتحلّل الأسماء وتوجّهها وتوقّتها. هذا الفصل يستعرض بروتوكولات الإنترنت الأساسية — link و network و transport و name resolution و routing و timing وبعض بروتوكولات التطبيق — ويحلّل ثغراتها المعروفة، ويؤطّر استراتيجيات تخفيف مستندة إلى المعايير. وحيث يفيد، تستخدم نماذج رياضية مدمجة لتصيغ أسطح الهجوم وفعالية الضوابط.»

#### ③ الشرح الفهمي

الفكرة الأساسية إن الأمن مو بس كود التطبيق. حتى لو التطبيق مكتوب صح، البروتوكولات اللي تشتغل تحته تحمل ثغرات: اللي تنقل البيانات (move)، اللي تحلّل الأسماء لـ IP (resolve)، اللي توجّه الحزم بين الشبكات (route)، واللي تزامن الوقت (time). الفصل هذا يعمل مسح (survey) شامل لكل هذي الطبقات، بعدين يحلّل الثغرات المتعارف عليها (canonical vulnerabilities)، ويقدّم تخفيفات (mitigations) مبنية على المعايير. وكلما يفيد الموضوع، يستخدم نماذج رياضية مدمجة حتى يقيس سطح الهجوم (attack surface) وفعالية الضوابط (control efficacy).

| المجال | أمثلة بروتوكولات | شنو يشتغل |
|---|---|---|
| link | Ethernet, ARP | التواصل بين الجيران على نفس السلك |
| network | IPv4/IPv6, ICMP | العنونة والتوجيه |
| transport | TCP, UDP, QUIC | نقل البيانات بين الطرفين |
| name resolution | DNS, DoH, DoT | ترجمة الأسماء إلى عناوين IP |
| routing | BGP, RPKI, BGPsec | التوجيه بين الشبكات المستقلة |
| timing | NTP | تزامن الوقت بين الأجهزة |

الدرس: تدرس البروتوكولات مو كمعرفة نظرية، بل لأن كل واحدة منها تمثّل سطح هجوم (attack surface) محتمل. وإذا فهمت التصميم الأصلي ووين الثغرة، تكدر تعرف شنو الضابط المناسب وشنو حجم الخطر الباقي (residual risk).

---

### القسم 2 — 2. The layered context: why protocol design choices matter

#### ① النص الأصلي

> The canonical "TCP/IP stack" (link → network → transport → application) was engineered for reachability and resilience, not for adversarial environments. Many protocols shipped with minimal or no cryptographic protections and implicit trust in endpoints or intermediaries. Security retrofits — DNSSEC, TLS 1.3, QUIC, RPKI/BGPsec, DoT/DoH, RA-Guard, SEND — were introduced later to constrain known classes of attacks without sacrificing interoperability or performance. Understanding both the original design intent and the retrofits is essential to reason about residual risk and prioritize controls.
>
> Protocol originals and security upgrades:
>
> - TCP — RFC 793
> - TLS 1.3 — RFC 8446
> - DoH — RFC 8484
> - DNSSEC — RFC 4033/4035
> - RPKI — RFC 6480
> - BGPsec — RFC 8205
> - RA-Guard — RFC 6105/7113

#### ② الترجمة

> «حزمة TCP/IP الكانونية (link ← network ← transport ← application) انهندست لتحقيق الوصولية (reachability) والصمود (resilience)، مو لبيئة معادية (adversarial). كثير بروتوكولات نزلت بحماية تشفيرية ضئيلة أو معدومة، ومعها ثقة ضمنية (implicit trust) بالأطراف أو بالوسطاء. الترقيعات الأمنية — DNSSEC و TLS 1.3 و QUIC و RPKI/BGPsec و DoT/DoH و RA-Guard و SEND — جت لاحقًا لتقييد أصناف معروفة من الهجمات دون التضحية بالتشغيل البيني (interoperability) أو الأداء. وفهم نية التصميم الأصلية والترقيعات معًا ضروري للتفكير بالخطر الباقي وترتيب أولويات الضوابط.
>
> أصول البروتوكولات وترقيعاتها الأمنية:
>
> - TCP — RFC 793
> - TLS 1.3 — RFC 8446
> - DoH — RFC 8484
> - DNSSEC — RFC 4033/4035
> - RPKI — RFC 6480
> - BGPsec — RFC 8205
> - RA-Guard — RFC 6105/7113»

#### ③ الشرح الفهمي

الـ TCP/IP stack الأصلي انبنى لهدفين واضحين: الوصولية (reachability) — يعني أي طرف يوصل لأي طرف — والصمود (resilience) — يعني الشبكة تبقى شغّالة حتى لو انكسر جزء منها. بس ما انبنى أبدًا لبيئة معادية (adversarial). بمعنى آخر: التصميم الأصلي افترض حسن النية، والخصم ما عنده حسن نية. لهذا كثير بروتوكولات نزلت بأمان تشفيري ضعيف أو معدوم، ومعها ثقة ضمنية (implicit trust) بالأطراف وبالوسطاء (middleboxes).

عشان نعالج هذا، جت الترقيعات الأمنية (security retrofits) لاحقًا — كل ترقيع يعالج صنف هجمات معروف، بس دون ما يكسر التشغيل البيني (interoperability) أو الأداء.

| الثغرة الأصلية | الترقيع الأمني | الـ RFC |
|---|---|---|
| DNS بلا تحقق من صحة البيانات | DNSSEC | RFC 4033/4035 |
| TLS بهجمات معروفة | TLS 1.3 | RFC 8446 |
| DNS بلا تشفير (يُراقَب بسهولة) | DoH / DoT | RFC 8484 |
| توجيه BGP قابل للانتحال | RPKI / BGPsec | RFC 6480 / RFC 8205 |
| إعلانات RA مزيّفة في IPv6 | RA-Guard | RFC 6105/7113 |
| Neighbor Discovery غير موثّق | SEND | — |
| TCP بلا تشفير مدمج في النقل | QUIC | — |

الخلاصة: تفهم الاثنين معًا — نية التصميم الأصلي ووين كانت الثغرة، والترقيع اللي جاء بعدها — حتى تكدر تقدّر الخطر الباقي (residual risk) وترتب أولوياتك بالضوابط. مو كل ترقيع يغطّي كل شي، ولهذا لازم تعرف حدود كل واحد.

---

### القسم 3 — 3. Transport protocols: TCP, UDP, and QUIC

#### ① النص الأصلي

> **3.1 TCP: reliability with state and the SYN flood**
>
> TCP provides connection-oriented reliability using a three-way handshake and per-connection state — and that state can be weaponized. In a SYN flooding attack, an adversary sends a high rate of SYNs (often with spoofed sources), driving the server into keeping half-open connections and exhausting backlog resources, denying service to legitimate clients. Mitigations include SYN cookies, reduced SYN-RECEIVED timers, and ingress filtering to block spoofed sources (BCP 38).
>
> **Queueing model of a SYN flood.** Let $\beta$ be the backlog capacity, $\lambda$ the arrival rate of half-open SYNs, and $\mu$ the "service" rate at which half-opens transition (to established or drop). Modeling the backlog as an $M/M/1/B$ queue, the blocking probability (probability an honest SYN is dropped) under load $\rho = \lambda/\mu$ is the Erlang loss. SYN cookies effectively increase $\mu$ (no state until ACK) and reduce pressure on $B$, while BCP 38 reduces $\lambda$ by filtering spoofed sources upstream.
>
> **3.2 UDP: simplicity with no session semantics**
>
> UDP's statelessness and lack of handshake enable reflection and amplification: an attacker spoofs the victim's source IP and sends small queries to misconfigured reflectors (DNS, NTP, memcached), which reply with larger responses to the victim. The amplification factor $A$ is the ratio of response bytes to request bytes, and total attack bandwidth at the victim approximates $A \sum_j r_j$ — the sum of rates $r_j$ across reflectors. NTP's historic monlist made $A$ dangerously high until patched and widely disabled.
>
> **3.3 QUIC (over UDP) and HTTP/3: encrypting the transport**
>
> QUIC integrates TLS 1.3 into the transport, yielding 0-RTT/1-RTT handshakes, per-stream multiplexing without head-of-line blocking, connection migration, and authenticated encryption by default. HTTP/3 maps HTTP semantics onto QUIC. These shifts close large classes of passive observation and injection attacks present in TCP+TLS and improve performance, but move more complexity — and thus security responsibility — into user-space stacks and middlebox interactions.

$$B = \frac{\rho^{B+1}}{1 + \rho + \rho^2 + \cdots + \rho^{B+1}} \quad (\rho \neq 1)$$

| الرمز | المعنى |
|---|---|
| $\rho$ | offered load — الحمل المعروض على الطابور ($\rho = \lambda/\mu$) |
| $B$ | buffer / queue size — حجم الـ backlog (سعة الطابور) |
| $\lambda$ | معدل وصول الـ SYN نصف المفتوحة (arrival rate) |
| $\mu$ | معدل خدمة الـ half-opens (تنتقل لـ established أو تُسقط) |

#### ② الترجمة

> «**3.1 TCP: الموثوقية بالحالة وهجوم SYN flood**
>
> TCP يوفّر موثوقية موجهة للاتصال (connection-oriented) عبر مصافحة ثلاثية (three-way handshake) وحالة لكل اتصال (per-connection state) — وهذي الحالة ممكن تتحوّل لسلاح. في هجوم SYN flooding، الخصم يرسل معدلًا عاليًا من حزم SYN (غالبًا بمصادر مزيّفة)، فيجبر السيرفر على الاحتفاظ باتصالات نصف مفتوحة (half-open) واستنزاف موارد الـ backlog، فيُحجب الخدمة عن العملاء الشرعيين. التخفيفات تشمل SYN cookies، وتقليل مؤقتات SYN-RECEIVED، والترشيح الداخلي (ingress filtering) لحجب المصادر المزيّفة (BCP 38).
>
> **نموذج الطابور لهجوم SYN flood.** لتكن $\beta$ سعة الـ backlog، و $\lambda$ معدل وصول حزم SYN نصف المفتوحة، و $\mu$ معدل «الخدمة» اللي تنتقل به الحالات النصف مفتوحة (إلى established أو تُسقط). بنمذجة الـ backlog كطابور $M/M/1/B$، فإن احتمال الحجب (احتمال إسقاط SYN شرعية) عند حمل $\rho = \lambda/\mu$ هو Erlang loss. SYN cookies فعليًا تزيد $\mu$ (بلا حالة حتى يجي الـ ACK) وتقلّل الضغط على $B$، بينما BCP 38 تقلّل $\lambda$ بترشيح المصادر المزيّفة في المنبع (upstream).
>
> **3.2 UDP: البساطة بلا دلالات جلسة**
>
> انعدام الحالة (statelessness) في UDP وغياب المصافحة يمكّنان الانعكاس والتضخيم (reflection and amplification): المهاجم يزيّف عنوان المصدر تبع الضحية ويرسل استعلامات صغيرة إلى مُنعكسات (reflectors) سيئة الضبط (DNS, NTP, memcached)، وهذي المُنعكسات ترد بردود أكبر على الضحية. عامل التضخيم $A$ هو نسبة بايتات الرد إلى بايتات الطلب، وعرض نطاق الهجوم الكلي عند الضحية يقارب $A \sum_j r_j$ — مجموع المعدلات $r_j$ عبر المُنعكسات. أمر monlist التاريخي في NTP خلّى $A$ مرتفعًا بشكل خطير إلى أن تم ترقيعه وتعطيله على نطاق واسع.
>
> **3.3 QUIC (فوق UDP) و HTTP/3: تشفير طبقة النقل**
>
> QUIC يدمج TLS 1.3 داخل طبقة النقل، فيمنح مصافحات 0-RTT/1-RTT، وتعدد إرسال لكل stream دون حجب رأس الطابور (head-of-line blocking)، وترحيل الاتصال (connection migration)، وتشفيرًا موثّقًا (authenticated encryption) بشكل افتراضي. أما HTTP/3 فيُسقط دلالات HTTP على QUIC. هذي التحوّلات تسدّ أصنافًا كبيرة من هجمات المراقبة السلبية والحقن الموجودة في TCP+TLS وتحسّن الأداء، لكنها تنقل تعقيدًا أكبر — وبالتالي مسؤولية أمنية أكبر — إلى مكدّسات (stacks) مساحة المستخدم (user space) وتفاعلات الوسطاء (middleboxes).»

#### ③ الشرح الفهمي

هذا القسم يقارن ثلاث بروتوكولات نقل (transport): TCP و UDP و QUIC. القاعدة العامة: **كل ما تضيف موثوقية وحالة، كل ما تفتح ثغرة جديدة**.

**3.1 — TCP وهجوم SYN flood.** TCP موثوق (reliable) لأنه connection-oriented: قبل ما تنتقل البيانات، يصير three-way handshake (SYN ← SYN-ACK ← ACK)، وبعدها السيرفر يحتفظ بحالة (state) لكل اتصال. هذي الحالة هي نقطة الضعف: المهاجم يرسل وابل من حزم SYN (غالبًا بمصادر مزيّفة/spoofed) فيدخل السيرفر في حالة نصف مفتوحة (half-open) وينتظر الـ ACK اللي ما راح يجي، فيمتلئ الـ backlog ← وبالتالي تُسقط حزم SYN الحقيقية ويصير denial of service.

عشان نفهم متى ينطرد الطلب الشرعي، نستخدم نموذج طابور $M/M/1/B$. احتمال الحجب (blocking probability) اللي تعطيه معادلة Erlang loss:

$$B = \frac{\rho^{B+1}}{1 + \rho + \rho^2 + \cdots + \rho^{B+1}} \quad (\rho \neq 1)$$

| الرمز | المعنى |
|---|---|
| $\rho$ | offered load — الحمل المعروض، $\rho = \lambda/\mu$ |
| $B$ | buffer / queue size — حجم الطابور (سعة الـ backlog) |
| $\lambda$ | arrival rate — معدل وصول الـ SYN |
| $\mu$ | service rate — معدل خدمة الـ half-opens |

المعنى المنطقي: كل ما الـ backlog ($B$) أصغر أو الحمل ($\rho$) أكبر، كل ما زاد احتمال حجب الـ SYN الشرعية. لهذا التخفيف يشتغل على طرفين:

- **SYN cookies** ← تزيد $\mu$ لأن السيرفر ما يحتفظ بحالة حتى يجي الـ ACK، فتقلّ الضغط على $B$.
- **BCP 38 (ingress filtering)** ← تقلّل $\lambda$ بترشيح المصادر المزيّفة في المنبع، فما تصلك أصلًا.

**3.2 — UDP والانعكاس/التضخيم.** UDP بلا اتصال (stateless) وبلا مصافحة، وهذي البساطة نفسها هي الثغرة. المهاجم يزيّف عنوان المصدر تبع الضحية (spoof)، ويرسل استعلام صغير لمُنعكس سيئ الضبط (misconfigured reflector مثل DNS أو NTP أو memcached)، والمُنعكس يرد برد كبير على الضحية. النتيجة:

$$A = \frac{\text{response bytes}}{\text{request bytes}}, \qquad \text{bandwidth at victim} \approx A \sum_j r_j$$

| الرمز | المعنى |
|---|---|
| $A$ | عامل التضخيم (amplification factor) |
| $r_j$ | معدل الطلبات من المُنعكس رقم $j$ |
| $\sum_j r_j$ | مجموع معدلات كل المُنعكسات |

كل ما $A$ أكبر، كل ما الهجوم أخطر. أمر monlist في NTP كان يعطي $A$ ضخم جدًا إلى أن تم ترقيعه وتعطيله.

**ملاحظة أمانة مهمة:** الانعكاس والتضخيم في UDP يشتغل أصلًا لأن **عنوان المصدر قابل للانتحال (spoofable)**. لو ما كدر المهاجم يزيّف العنوان، الردود ترجع له هو مو للضحية. لهذا الترشيح الداخلي (ingress filtering) — المعروف بـ BCP 38 / RFC 2827 — ضروري جدًا، وهو مشروح لاحقًا في هذا الفصل. يعني الحل ما بس عند الضحية، بل عند الشبكات اللي تسمح بحزم بمصدر مزيّف تخرج منها.

**3.3 — QUIC و HTTP/3.** QUIC هو محاولة تحل مشاكل TCP+TLS من الأساس: يدمج TLS 1.3 مباشرة في طبقة النقل (فوق UDP)، فيصير التشفير افتراضيًا مو اختياري، والمصافحة أسرع (0-RTT/1-RTT)، وكل stream مستقل بلا head-of-line blocking، مع دعم connection migration. HTTP/3 بعدين يشتغل فوق QUIC. الفائدة الأمنية: يسدّ أصناف كبيرة من هجمات المراقبة السلبية (passive observation) والحقن (injection). المقابل: يزيد التعقيد، وينقل المسؤولية إلى user-space stacks وإلى الوسطاء (middleboxes) اللي صاروا ما يكدرون يشوفون المحتوى.

| الخاصية | TCP | UDP | QUIC |
|---|---|---|---|
| نوع الاتصال | connection-oriented | stateless (بلا اتصال) | اتصال فوق UDP |
| الحالة | per-connection state | بلا حالة | حالة مشفّرة |
| الموثوقية | موثوق (retransmission) | غير موثوق | موثوق لكل stream |
| التشفير | لا (يحتاج TLS خارجي) | لا | TLS 1.3 مدمج (افتراضيًا) |
| الثغرة الأشهر | SYN flood | reflection / amplification | تعقيد user-space + middleboxes |

الخلاصة العملية: TCP يدفع ثمن الموثوقية بحالة قابلة للاستنزاف، و UDP يدفع ثمن البساطة بانعدام التحقق من المصدر، و QUIC يحاول يجمع الموثوقية والأمان معًا لكن ينقل التعقيد لمكان ثاني. كل بروتوكول عنده مقايضة (trade-off).

---

![TCP · UDP · QUIC — مقارنة النقل|720](../06_Diagrams_&_Mindmaps/cy_w5_transport.svg)
