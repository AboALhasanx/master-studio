### القسم 1 — Introduction
#### ① النص الأصلي
> The triad of firewalls, proxies, and virtual private networks (VPNs) forms the foundation of contemporary network defense and traffic governance. Each is rooted in decades of operational practice, has evolved under the pressures of performance, encryption, and adversarial sophistication, and embodies a different abstraction of trust boundaries.
>
> Firewalls mediate traffic at defined layers, enforcing security policy through allow/deny semantics and inspection. Proxies mediate application-layer interactions, providing indirection, filtering, and performance optimization. VPNs create cryptographically enforced tunnels across untrusted networks, securing confidentiality and integrity of data in motion.
>
> In modern practice, these functions increasingly blur: next-generation firewalls perform deep application inspection once associated with proxies, and VPNs converge with Zero Trust network access and cloud-edge models. Yet their conceptual distinctness remains analytically useful, particularly for understanding vulnerabilities, performance trade-offs, and mathematical risk postures.
#### ② الترجمة
> «ثلاثية الـ firewalls والـ proxies والـ virtual private networks (VPNs) تُشكّل أساس الدفاع الشبكي المعاصر وحوكمة حركة المرور (traffic governance). كلٌّ منها متجذّر في عقود من الممارسة التشغيلية، وتطوّر تحت ضغط الأداء والتشفير وتعقيد المهاجمين (adversarial sophistication)، ويجسّد تجريداً مختلفاً لحدود الثقة (trust boundaries).»
>
> «تتوسّط الـ firewalls حركة المرور عند طبقات محدّدة، وتفرض سياسة الأمن عبر دلالات allow/deny والفحص (inspection). وتتوسّط الـ proxies التفاعلات على مستوى طبقة التطبيق (application layer)، فتوفّر التمرير غير المباشر (indirection) والتصفية وتحسين الأداء. أما الـ VPNs فتُنشئ أنفاقاً مفروضة تشفيرياً (cryptographically enforced tunnels) عبر الشبكات غير الموثوقة، مؤمّنةً سرية البيانات وسلامتها أثناء النقل.»
>
> «في الممارسة الحديثة، هذه الوظائف تتداخل بشكل متزايد: فالـ next-generation firewalls تُجري فحصاً عميقاً للتطبيقات كان يُنسب سابقاً إلى الـ proxies، والـ VPNs تتقارب مع Zero Trust network access ونماذج cloud-edge. ومع ذلك يبقى تمييزها المفاهيمي مفيداً تحليلياً، لا سيّما لفهم نقاط الضعف ومقايضات الأداء والمواقف الرياضية للمخاطر (mathematical risk postures).»
#### ③ الشرح الفهمي
هذا القسم مقدّمة تحضيرية: يقول إن **firewalls + proxies + VPNs** هم العمود الفقري للدفاع الشبكي الحديث. الثلاثة ما ظهروا بيوم واحد، بل تراكموا من عقود من الممارسة العملية، وتطوّروا تحت ثلاثة ضغوط: **الأداء (performance)** و**التشفير (encryption)** و**تطوّر المهاجمين (adversarial sophistication)**. كل واحد منهم يعبّر عن **abstraction مختلف لحدود الثقة (trust boundaries)** — يعني كل واحد يرسم "وين الثقة تبدأ ووين تنتهي" بطريقة مختلفة.

الفروق الأساسية بين الثلاثة:

| التقنية | شنو تسوي | المستوى |
|---|---|---|
| Firewalls | تتوسّط حركة المرور وتفرض سياسة الأمن عبر allow/deny + inspection | طبقات محدّدة |
| Proxies | تتوسّط تفاعلات التطبيق، تعطي indirection + filtering + performance | application layer |
| VPNs | تنشئ أنفاق مشفّرة (tunnels) عبر شبكات غير موثوقة، تحفظ confidentiality + integrity | data in motion |

النقطة المحورية في القسم: **الوظائف تداخلت (blur)**. الـ NGFW صار يسوي فحص تطبيقات عميق كان سابقاً شغل الـ proxy، والـ VPN صار يتقارب مع **Zero Trust** ونماذج **cloud-edge**. بس رغم التداخل، الفصل المفاهيمي بينهم يبقى مفيد — لأن كل واحد له **vulnerabilities** و**performance trade-offs** و**mathematical risk posture** مختلفة. يعني تفهم كل واحد على حدة، حتى لو واقعياً اشتغلوا سوية.

### القسم 2 — Firewalls: Evolution, Architectures, and Threat Posture
#### ① النص الأصلي
> 2.1 Classic models: Early firewalls enforced policy through stateless packet filtering, matching headers against access control lists (ACLs). Stateful firewalls extended this by tracking connection state (SYN, ESTABLISHED) and inspecting traffic sequences. These approaches embody the perimeter defense model: the enterprise edge as a chokepoint, with firewalls defining the demarcation between "inside" and "outside."
>
> 2.2 Next-generation firewalls (NGFWs): Modern firewalls integrate:
>
> - Deep Packet Inspection (DPI) to classify traffic by application signatures.
> - TLS/SSL interception to inspect encrypted payloads.
> - Intrusion prevention features that embed IDS/IPS engines.
> - Integration with identity providers for per-user access control.
>
> NGFWs extend firewalls beyond packet/connection semantics into application-layer policy enforcement, aligning with the migration of threats to port-agile, encrypted traffic.
>
> 2.3 Firewall evasion techniques: Attackers employ fragmentation, tunneling (HTTP/S encapsulation), encryption misuse, and traffic shaping to evade detection. Adaptive firewalls incorporate anomaly detection and machine learning classifiers to identify traffic characteristics even under obfuscation.
>
> 2.4 Mathematical framing: firewall reliability. Let P_allow be the probability that malicious traffic is erroneously allowed, and P_deny the probability that benign traffic is erroneously blocked. Define firewall accuracy as A = 1 − (P_allow + P_deny). Further, let incoming traffic consist of proportions q_m (malicious) and q_b (benign). The expected risk exposure is R = q_m·P_allow·I_m + q_b·P_deny·I_b, where I_m and I_b denote impact of missed detections and false positives respectively. This quantifies the balance between security and usability in firewall deployments.

$$A = 1 - (P_{allow} + P_{deny})$$

$$R = q_m\,P_{allow}\cdot I_m + q_b\,P_{deny}\cdot I_b$$
#### ② الترجمة
> «2.1 النماذج الكلاسيكية (Classic models): فرضت الـ firewalls المبكّرة سياستها عبر ترشيح الحزم عديم الحالة (stateless packet filtering)، بمطابقة الترويسات (headers) مع قوائم التحكم بالوصول (ACLs). ثم وسّعت الـ stateful firewalls ذلك بتتبّع حالة الاتصال (SYN، ESTABLISHED) وفحص تسلسلات حركة المرور. هذه المقاربات تجسّد نموذج الدفاع المحيطي (perimeter defense): حافة المؤسسة كنقطة عنق زجاجة (chokepoint)، حيث تحدّد الـ firewalls الحدّ الفاصل بين "الداخل" و"الخارج".»
>
> «2.2 الجيل الجديد من الـ firewalls (NGFWs): تدمج الـ firewalls الحديثة:»
>
> - «الفحص العميق للحزم (Deep Packet Inspection — DPI) لتصنيف المرور حسب بصمات التطبيقات (application signatures).»
> - «اعتراض TLS/SSL لفحص الحمولات المشفّرة (encrypted payloads).»
> - «خصائص منع التسلّل (intrusion prevention) التي تُدمج محرّكات IDS/IPS.»
> - «التكامل مع مزوّدي الهوية (identity providers) للتحكم بالوصول لكل مستخدم.»
>
> «توسّع الـ NGFWs نطاق الـ firewall إلى ما بعد دلالات الحزمة/الاتصال ليشمل فرض السياسة على طبقة التطبيق، بما يوافق انتقال التهديدات نحو مرور مشفّر يتنقّل بين المنافذ (port-agile).»
>
> «2.3 تقنيات تجنّب الـ firewall (evasion techniques): يوظّف المهاجمون التجزئة (fragmentation)، والأنفاق (tunneling عبر تغليف HTTP/S)، وإساءة استخدام التشفير، وتشكيل المرور (traffic shaping) لتجنّب الكشف. أما الـ adaptive firewalls فتُدرج كشف الشذوذ (anomaly detection) ومصنّفات التعلّم الآلي لتحديد خصائص المرور حتى تحت التمويه (obfuscation).»
>
> «2.4 التأطير الرياضي: موثوقية الـ firewall. لتكن P_allow احتمال السماح الخاطئ بمرور مرور ضارّ، وP_deny احتمال الحجب الخاطئ لمرور سليم. عرّف دقة الـ firewall بأنها A = 1 − (P_allow + P_deny). كذلك لتتكوّن حركة المرور الواردة من نسبتين q_m (ضارّ) وq_b (سليم). والتعرض المتوقّع للمخاطر هو R = q_m·P_allow·I_m + q_b·P_deny·I_b، حيث I_m وI_b تدلّان على أثر حالات عدم الكشف والإنذارات الخاطئة (false positives) على التوالي. هذا يكمّم التوازن بين الأمن والاستعمالية (usability) في نشر الـ firewalls.»
#### ③ الشرح الفهمي
الـ firewall هي أول خط دفاع، وهي بالجوهر جهاز يفرض سياسة **allow/deny** على حركة المرور. تطوّرت على ثلاث مراحل:

| الجيل | الطريقة | الخصائص |
|---|---|---|
| Stateless packet filtering | يطابق الـ headers مع الـ ACLs | سريع بس غبي — ما يفهم سياق الاتصال |
| Stateful | يتتبّع حالة الاتصال (SYN, ESTABLISHED) | يفهم إذا الحزمة جزء من جلسة قائمة |
| NGFW | DPI + TLS interception + IPS + identity | يشوف على مستوى التطبيق والمستخدم |

نموذج **perimeter defense** (الدفاع المحيطي): المؤسسة كأنها قلعة، والحافة (edge) هي **chokepoint** — كل المرور لازم يمر من نقطة واحدة، وهناك الـ firewall ترسم الحد بين "inside" و"outside". مشكلة هذا النموذج إنه ينهار لو صار المرور مشفّر أو يتنقّل بين منافذ (**port-agile**).

**الـ NGFW** يدمج أربعة أشياء: **DPI** (تصنيف حسب بصمة التطبيق)، **TLS/SSL interception** (فك التشفير للفحص)، **IPS engine**، و**identity integration** (سياسة لكل مستخدم).

**تقنيات التجنّب (evasion):** المهاجم يستعمل fragmentation، tunneling عبر تغليف HTTP/S، إساءة استخدام التشفير، وtraffic shaping. الرد عليها: **adaptive firewalls** بكشف شذوذ و**ML classifiers**.

أما الرياضيات، فهي تقيس الموثوقية بمقايضة **security ↔ usability**:

| الرمز | المعنى |
|---|---|
| $P_{allow}$ | احتمال السماح الخاطئ بمرور ضارّ (missed detection) |
| $P_{deny}$ | احتمال الحجب الخاطئ لمرور سليم (false positive) |
| $A$ | دقة الـ firewall |
| $q_m$ | نسبة المرور الضارّ الوارد |
| $q_b$ | نسبة المرور السليم الوارد |
| $I_m$ | أثر تفويت الكشف (missed detection impact) |
| $I_b$ | أثر الإنذار الخاطئ (false positive impact) |
| $R$ | التعرض المتوقّع للمخاطر (expected risk exposure) |

المعادلة الأولى $A = 1 - (P_{allow} + P_{deny})$: الدقة = 1 ناقص مجموع نوعي الخطأ. لاحظ إنه **مجموع** مو ضرب، لأن الخطأين (allow خاطئ وdeny خاطئ) كلاهما يقلّل الدقة بنفس الاتجاه.

المعادلة الثانية $R = q_m P_{allow} I_m + q_b P_{deny} I_b$: التعرض للمخاطر = (احتمال المرور الضارّ × خطأ السماح × أثره) + (احتمال المرور السليم × خطأ الحجب × أثره). الفكرة المحورية: **ما يكفي تعرف نسبة الخطأ، لازم توزنه بالأثر** — خطأ واحد بمرور ضارّ أثره $I_m$ يمكن يكون أكبر بمراتب من خطأ حجب سليم أثره $I_b$. هذا اللي يفسّر ليش بعض المؤسسات تختار تكون "أكثر تشدّداً" (تحجب أكثر) حتى لو تعطّلت خدمات شوي.

### القسم 3 — Proxies: Application Mediation and Indirection
#### ① النص الأصلي
> 3.1 Forward proxies: Forward proxies act on behalf of internal clients requesting external resources. Common uses include caching, content filtering, anonymization, and access control. Enterprises deploy forward proxies to enforce acceptable use policies, block malicious content, and aggregate monitoring.
>
> 3.2 Reverse proxies: Reverse proxies sit in front of servers, mediating inbound connections. They provide load balancing, TLS termination, caching, and Web Application Firewall (WAF) functionality. By abstracting servers behind a proxy, they reduce direct attack surface and enable consistent security enforcement.
>
> 3.3 Proxies in the encrypted era: With the near-universal adoption of TLS, proxies require decryption to inspect content. This introduces challenges:
>
> - Performance overhead of bulk decryption/re-encryption.
> - Privacy and trust concerns due to visibility into plaintext.
> - Certificate management complexity when implementing enterprise TLS interception.
>
> 3.4 Mathematical framing: cache hit optimization. One measure of proxy performance is cache hit ratio (CHR). If N requests are made and H are served from cache, CHR = H/N. Latency reduction per request can be approximated as ΔL = L_origin − L_cache, yielding total saved latency L_saved = H·(L_origin − L_cache). Security benefit emerges when malicious or unwanted content is blocked upstream, reducing exposure probability P_exp. For example, the expected malicious content exposure after proxy filtering is P_exp = (1 − e_p)·P_exp′, where e_p is proxy filtering efficacy.

$$CHR = \frac{H}{N}$$

$$\Delta L = L_{origin} - L_{cache}$$

$$L_{saved} = H \cdot (L_{origin} - L_{cache})$$

$$P_{exp} = (1 - e_p)\, P_{exp}'$$
#### ② الترجمة
> «3.1 الـ Forward proxies: تعمل بالنيابة عن العملاء الداخليين الذين يطلبون موارد خارجية. ومن استخداماتها الشائعة: التخزين المؤقّت (caching)، وتصفية المحتوى (content filtering)، وإخفاء الهوية (anonymization)، والتحكم بالوصول (access control). وتنشر المؤسسات الـ forward proxies لفرض سياسات الاستخدام المقبول، وحجب المحتوى الضارّ، وتجميع المراقبة (aggregate monitoring).»
>
> «3.2 الـ Reverse proxies: تقف أمام الخوادم فتتوسّط الاتصالات الواردة (inbound). وتوفّر موازنة الحمل (load balancing)، وإنهاء TLS (TLS termination)، والتخزين المؤقّت، ووظائف جدار حماية تطبيقات الويب (WAF). وبإخفاء الخوادم خلف البروكسي، تقلّل مساحة الهجوم المباشرة (direct attack surface) وتُتيح فرضاً متّسقاً للأمن.»
>
> «3.3 الـ proxies في عصر التشفير (encrypted era): مع التبنّي شبه العالمي لـ TLS، تحتاج الـ proxies إلى فك التشفير لفحص المحتوى. وهذا يطرح تحديات:»
>
> - «كلفة أداء (performance overhead) لفك وإعادة تشفير كميات كبيرة.»
> - «مخاوف الخصوصية والثقة بسبب الإطّلاع على النص الصريح (plaintext).»
> - «تعقيد إدارة الشهادات عند تطبيق اعتراض TLS على مستوى المؤسسة.»
>
> «3.4 التأطير الرياضي: تحسين إصابة الذاكرة المؤقّتة (cache hit optimization). أحد مقاييس أداء البروكسي هو نسبة إصابة الذاكرة المؤقّتة (CHR). إذا قُدِّم N طلب وخُدِم منها H من الذاكرة المؤقّتة، فإن CHR = H/N. ويمكن تقريب خفض زمن الاستجابة لكل طلب بـ ΔL = L_origin − L_cache، ما يعطي إجمالي زمن الاستجابة الموفَّر L_saved = H·(L_origin − L_cache). وينشأ نفع أمني عندما يُحجب المحتوى الضارّ أو غير المرغوب فيه عند المصدر (upstream)، فينخفض احتمال التعرّض P_exp. فعلى سبيل المثال، التعرض المتوقّع للمحتوى الضارّ بعد تصفية البروكسي هو P_exp = (1 − e_p)·P_exp′، حيث e_p هي فاعلية تصفية البروكسي.»
#### ③ الشرح الفهمي
الـ **proxy** هي وسيط (mediator) يقف بين طرفين ويتمرّر المرور بالنيابة عنهم، فيوفّر **indirection** (تمرير غير مباشر). نوعان أساسيان — والفرق بينهم هو **اتجاه من يستفيد**:

| النوع | يقف وين | يخدم مين | أهم الوظائف |
|---|---|---|---|
| Forward proxy | بين العملاء الداخليين والإنترنت | العملاء (clients) | caching, content filtering, anonymization, access control |
| Reverse proxy | أمام الخوادم (servers) | الخوادم | load balancing, TLS termination, caching, WAF |

الـ **forward proxy** تستعمله المؤسسة لفرض **acceptable use policies**، حجب محتوى ضارّ، وتجميع المراقبة. الـ **reverse proxy** يخفي الخوادم خلفه ← يقلّل **direct attack surface** ويفرض الأمن بشكل متّسق.

**مشكلة عصر التشفير (encrypted era):** بما إن تقريباً كل المرور صار TLS، الـ proxy لازم **يفك التشفير** حتى يفحص المحتوى. هذا يولّد ثلاث تحديات: كلفة أداء (decryption/re-encryption)، مخاوف خصوصية (لأنه يشوف الـ plaintext)، وتعقيد إدارة الشهادات عند **TLS interception** على مستوى المؤسسة.

أما رياضياً، فالقسم فيه محورين: **الأداء** و**الأمن**.

| الرمز | المعنى |
|---|---|
| $H$ | عدد الطلبات المخدومة من الذاكرة المؤقّتة (cache hits) |
| $N$ | إجمالي عدد الطلبات |
| $CHR$ | نسبة إصابة الذاكرة المؤقّتة (cache hit ratio) |
| $L_{origin}$ | زمن الاستجابة من المصدر الأصلي |
| $L_{cache}$ | زمن الاستجابة من الذاكرة المؤقّتة |
| $\Delta L$ | مقدار خفض الزمن لكل طلب |
| $L_{saved}$ | إجمالي الزمن الموفَّر |
| $e_p$ | فاعلية تصفية البروكسي (proxy filtering efficacy) |
| $P_{exp}$ | احتمال التعرّض للمحتوى الضارّ |

معادلة الأداء $CHR = \dfrac{H}{N}$: نسبة الطلبات اللي جاوبها الكاش. وكل ما زادت $CHR$، زاد النفع: $\Delta L = L_{origin} - L_{cache}$ هو الوفر لكل طلب، والإجمالي $L_{saved} = H \cdot (L_{origin} - L_{cache})$.

معادلة الأمن $P_{exp} = (1 - e_p)\, P_{exp}'$: نفس نمط "الفاعلية تختصر الاحتمال". $P_{exp}'$ هو التعرّض قبل التصفية، و$e_p$ فاعلية البروكسي؛ فكل ما زادت $e_p$، انخفض التعرّض. لاحظ إن البروكسي بحد ذاته **ما يمنع الهجوم** — هو بس **يقلّل فرصة الوصول** للمحتوى الضارّ.

### القسم 4 — Virtual Private Networks (VPNs)
#### ① النص الأصلي
> 4.1 Fundamental role: VPNs secure communications across untrusted networks by creating encrypted tunnels. They provide confidentiality, integrity, and endpoint authentication, effectively extending a private network over the public Internet.
>
> 4.2 Protocol families:
>
> - IPsec (RFC 4301): Operates at the IP layer, supporting tunnel and transport modes, with ESP and AH for confidentiality and authentication.
> - SSL/TLS VPNs: Operate at transport/application layers, leveraging TLS.
> - WireGuard: A modern VPN protocol emphasizing simplicity, minimal codebase, and reliance on modern cryptographic primitives (Curve25519, ChaCha20-Poly1305).
>
> 4.3 Deployment models:
>
> - Remote access VPNs: Secure teleworker connections.
> - Site-to-site VPNs: Connect geographically dispersed enterprise sites.
> - Cloud-native VPNs: Integrate with multi-cloud and hybrid environments.
>
> 4.4 Vulnerabilities: Misconfigurations, weak authentication, obsolete protocols (PPTP, L2TP without IPsec), and credential theft undermine VPNs. Compromise of a VPN gateway provides adversaries with broad lateral movement opportunities.
>
> 4.5 Mathematical framing: VPN confidentiality assurance. Let P_int be the probability of successful interception without VPN, and e_vpn the efficacy of VPN encryption against interception. The residual probability of interception is P_int′ = (1 − e_vpn)·P_int. Similarly, performance overhead can be modeled: let T_0 be baseline transmission time and O_enc the overhead from encryption, then T_vpn = T_0 + O_enc. The trade-off between security and latency is expressed by optimizing e_vpn relative to acceptable T_vpn.

$$P_{int}' = (1 - e_{vpn})\, P_{int}$$

$$T_{vpn} = T_0 + O_{enc}$$
#### ② الترجمة
> «4.1 الدور الأساسي (Fundamental role): تؤمّن الـ VPNs الاتصالات عبر الشبكات غير الموثوقة بإنشاء أنفاق مشفّرة (encrypted tunnels). وتوفّر السرية (confidentiality) والسلامة (integrity) ومصادقة الأطراف (endpoint authentication)، فتمتدّ بالشبكة الخاصة فعلياً فوق الإنترنت العام.»
>
> «4.2 عائلات البروتوكولات (Protocol families):»
>
> - «IPsec (RFC 4301): يعمل عند طبقة IP، ويدعم نمطَي tunnel وtransport، مع ESP وAH للسرية والمصادقة.»
> - «SSL/TLS VPNs: تعمل عند طبقتي النقل/التطبيق، مستفيدةً من TLS.»
> - «WireGuard: بروتوكول VPN حديث يركّز على البساطة وقاعدة شيفرة ضئيلة والاعتماد على primitives تشفيرية حديثة (Curve25519، ChaCha20-Poly1305).»
>
> «4.3 نماذج النشر (Deployment models):»
>
> - «Remote access VPNs: تؤمّن اتصالات العاملين عن بُعد (teleworker).»
> - «Site-to-site VPNs: تربط مواقع المؤسسة المتباعدة جغرافياً.»
> - «Cloud-native VPNs: تتكامل مع البيئات متعدّدة السحابات والهجينة (multi-cloud / hybrid).»
>
> «4.4 نقاط الضعف (Vulnerabilities): تقوّض الـ VPNs الأخطاء في الإعداد (misconfigurations)، والمصادقة الضعيفة، والبروتوكولات المتقادمة (PPTP، وL2TP بدون IPsec)، وسرقة بيانات الاعتماد (credential theft). كما أن اختراق بوابة VPN (gateway) يمنح المهاجمين فرصاً واسعة للحركة الجانبية (lateral movement).»
>
> «4.5 التأطير الرياضي: ضمان سرية الـ VPN (confidentiality assurance). لتكن P_int احتمال الاعتراض الناجح دون VPN، وe_vpn فاعلية تشفير الـ VPN ضد الاعتراض. فاحتمال الاعتراض المتبقّي هو P_int′ = (1 − e_vpn)·P_int. وبالمثل يمكن نمذجة كلفة الأداء: لتكن T_0 زمن الإرسال الأساسي، وO_enc الكلفة الإضافية للتشفير، فيكون T_vpn = T_0 + O_enc. وتُعبَّر مقايضة الأمن وزمن الاستجابة (latency) عبر تحسين e_vpn نسبةً إلى T_vpn المقبول.»
#### ③ الشرح الفهمي
الـ **VPN** تحلّ مشكلة أساسية: كيف نمرّر بيانات سرّية عبر شبكة غير موثوقة (الإنترنت)؟ الجواب: **encrypted tunnel** — نفق مشفّر يخلّي الشبكة العامة كأنها شبكة خاصة ممتدّة. توفّر ثلاثة أشياء: **confidentiality** + **integrity** + **endpoint authentication**.

**عائلات البروتوكولات (Protocol families):**

| البروتوكول | الطبقة | ملاحظات |
|---|---|---|
| IPsec (RFC 4301) | IP layer | أنماط tunnel وtransport؛ ESP للسرية، AH للمصادقة |
| SSL/TLS VPNs | transport/application | تستفيد من TLS |
| WireGuard | — | حديث: بساطة + codebase ضئيل + Curve25519, ChaCha20-Poly1305 |

**نماذج النشر (Deployment models):**

| النموذج | الاستخدام |
|---|---|
| Remote access | العاملون عن بُعد (teleworker) |
| Site-to-site | ربط مواقع المؤسسة المتباعدة |
| Cloud-native | بيئات multi-cloud وhybrid |

**نقاط الضعف:** misconfigurations، مصادقة ضعيفة، بروتوكولات متقادمة (**PPTP**، **L2TP بدون IPsec**)، وسرقة credentials. أخطر نقطة: لو انخترقت **VPN gateway** ← المهاجم يحصل على **lateral movement** واسع داخل الشبكة. يعني الـ VPN تنقل الثقة (shift trust) بس **ما تلغي المخاطر** — نقطة مهمة جداً.

الرياضيات: محورين — **السرية** و**الأداء**.

| الرمز | المعنى |
|---|---|
| $P_{int}$ | احتمال الاعتراض الناجح بدون VPN |
| $e_{vpn}$ | فاعلية تشفير الـ VPN ضد الاعتراض |
| $P_{int}'$ | احتمال الاعتراض المتبقّي (residual) |
| $T_0$ | زمن الإرسال الأساسي (baseline transmission time) |
| $O_{enc}$ | الكلفة الإضافية للتشفير (encryption overhead) |
| $T_{vpn}$ | زمن الإرسال مع VPN |

معادلة السرية $P_{int}' = (1 - e_{vpn})\, P_{int}$: نفس نمط باقي الفصول — التشفير **يختصر** الاحتمال بنسبة فاعليته. لو $e_{vpn} = 0$ (بلا فاعلية) يبقى $P_{int}' = P_{int}$؛ ولو $e_{vpn}$ تقترب من 1، الاحتمال المتبقّي يقترب من صفر.

معادلة الأداء $T_{vpn} = T_0 + O_{enc}$: الـ VPN **تزيد** زمن الإرسال بمقدار كلفة التشفير. هذا هو جوهر الـ **trade-off**: ترفع الأمن ($e_{vpn}$ عالي) بس تدفع بـ latency أعلى ($T_{vpn}$ أكبر). الهدف العملي: **optimize** قيمة $e_{vpn}$ بما يوازن الأمن مقابل $T_{vpn}$ المقبول — مو "أعلى تشفير ممكن" دائماً، بل الأنسب للاستخدام.

![جدارات الحماية · البروكسي · VPN|720](../06_Diagrams_&_Mindmaps/cy_w5_fw_proxy_vpn.svg)
