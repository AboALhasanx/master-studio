### القسم 1 — 6. Cybersecurity Threats to Reliability and Continuity

#### ① النص الأصلي

> Cybersecurity threats to reliability and continuity strike at availability and at the survival of critical functions, and four categories dominate this risk.
>
> - **6.1 Distributed Denial-of-Service (DDoS)** — DDoS attacks target reliability directly, overwhelming services and making them unavailable; mitigation includes rate-limiting, traffic scrubbing, and CDN-based absorption.
> - **6.2 Ransomware** — ransomware disrupts continuity by encrypting critical data and demanding ransom, so effective continuity requires offline backups, immutable storage, and tested recovery workflows.
> - **6.3 Insider Threats** — malicious or negligent insiders can compromise reliability by altering configurations or disabling security controls.
> - **6.4 Supply Chain Compromises** — compromises in third-party components may undermine continuity, as illustrated by SolarWinds, where adversarial infiltration of updates caused systemic disruption.

#### ② الترجمة

> «تضرب التهديدات السيبرانية للموثوقية والاستمرارية التوفرية وبقاء الوظائف الحرجة، وتسيطر أربع فئات على هذا الخطر.
>
> - **6.1 هجمات الحرمان من الخدمة الموزّعة (DDoS)** — تستهدف هجمات DDoS الموثوقية مباشرةً، فتُغرق الخدمات وتجعلها غير متاحة؛ ويشمل التخفيف تحديد المعدل، وتنقية المرور، والامتصاص عبر CDN.
> - **6.2 برامج الفدية** — تُعطّل برامج الفدية الاستمرارية عبر تشفير البيانات الحرجة وطلب فدية، لذا تتطلب الاستمرارية الفعّالة نسخاً احتياطية غير متصلة وتخزيناً غير قابلاً للتغيير وسير عمل استرداد مُختبَراً.
> - **6.3 الخصوم الداخليون** — يمكن للخصوم الداخليين الخبثاء أو المهملين أن يُضعفوا الموثوقية عبر تغيير الإعدادات أو تعطيل ضوابط الأمان.
> - **6.4 اختراقات سلسلة التوريد** — قد تُقوّض الاختراقات في مكوّنات الأطراف الثالثة الاستمرارية، كما يتضح من حادثة SolarWinds حيث أدّى التسلل العدائي إلى التحديثات إلى تعطّل منهجي.»

#### ③ الشرح الفهمي

هذي التهديدات الأربعة مو بس تخترق بيانات — هي تستهدف مباشرة قدرة الخدمة على الاستمرار بالعمل. خلينا نفهم كل واحد:

- **DDoS**: يغرّق الخدمة بطلبات وهمية ← تصير ما تستجيب للمستخدمين الحقيقيين. هذا هجوم على التوفرية (availability) مو على السرية. التخفيف: rate-limiting (نحدد عدد الطلبات)، traffic scrubbing (ننقّي الترافيك)، وامتصاص عبر CDN (نوزّع الحمل على شبكة واسعة).
- **Ransomware**: يشفّر البيانات ويطلب فدية. المشكلة إنه ما يسرق بس — يوقف العمل كله. لهذا الحل: نسخ احتياطية offline (ما متصلة بالشبكة)، تخزين immutable (ما ينعدّل ولا ينمسح)، وسير استرداد مُختبَر (تجربته قبل ما تحتاجه).
- **Insider Threats**: شخص من داخل الشركة — إما بنيّة خبيثة أو بإهمال — يغيّر إعدادات أو يعطّل حماية. هذي خطيرة لأن الداخلي عنده صلاحيات أصلاً.
- **Supply Chain**: تخترق مكوّن طرف ثالث (مكتبة، تحديث). SolarWinds مثال كلاسيكي: المهاجم دخل عبر تحديث رسمي موثوق ← انتشر لكل العملاء وسبّب تعطّل منهجي.

| التهديد | يستهدف | الأثر | التخفيف |
|---|---|---|---|
| DDoS | التوفرية | الخدمة توقف للمستخدمين | rate-limiting، traffic scrubbing، CDN |
| Ransomware | البيانات والاستمرارية | تشفير + توقف كامل للعمل | backups offline، immutable storage، استرداد مُختبَر |
| Insider Threats | الضوابط والإعدادات | تعطيل حماية من الداخل | least privilege، مراقبة، فصل المهام |
| Supply Chain | مكوّنات الطرف الثالث | انتشار واسع عبر تحديث موثوق | SBOM، توقيع التحديثات، تحقق من الموردين |

الخلاصة: الثلاثة الأولى تهدد التوفرية، والرابعة (supply chain) تهدد "الثقة بالمنبع" نفسه. وكلها تنعكس على الاستمرارية.

---

### القسم 2 — 7. Mathematical Modeling of Reliability and Continuity

#### ① النص الأصلي

> Reliability and continuity can be modeled quantitatively, turning resilience engineering into a measurable discipline through three complementary models.
>
> - **7.1 Probability of Failure Due to Cyber Events** — with an operational failure rate (λo) and a cybersecurity-induced failure rate (λc), the total failure rate is their sum, and reliability decays exponentially over time, highlighting the necessity of cybersecurity in reliability engineering.
> - **7.2 Continuity Index Model** — continuity is modeled with a Business Continuity Index (BCI), a weighted average in which Ci is the compliance level with continuity requirement i (0–1) and wi is its weight; a higher BCI reflects stronger resilience in the face of disruption.
> - **7.3 Resilience Optimization Model** — organizations minimize residual risk under budgetary constraints, where Mi is the mitigation effectiveness for vulnerability i, Ci is the cost of mitigation, and B is the available budget; this framework aligns cybersecurity investments with continuity objectives.

#### ② الترجمة

> «يمكن نمذجة الموثوقية والاستمرارية كمّياً، بما يحوّل هندسة المرونة إلى تخصّص قابل للقياس عبر ثلاثة نماذج متكاملة.
>
> - **7.1 احتمال الفشل بسبب الأحداث السيبرانية** — مع وجود معدّل فشل تشغيلي (λo) ومعدّل فشل ناتج عن الأمن السيبراني (λc)، يكون معدّل الفشل الكلي هو مجموعهما، وتتلاشى الموثوقية أُسّياً مع الوقت، مما يُبرز ضرورة الأمن السيبراني في هندسة الموثوقية.
> - **7.2 نموذج مؤشر الاستمرارية** — تُنمذَج الاستمرارية بمؤشر استمرارية الأعمال (BCI)، وهو متوسط مرجّح يكون فيه Ci مستوى الالتزام بمتطلب الاستمرارية i (0–1) وwi وزنه؛ وارتفاع BCI يعكس مرونة أقوى في مواجهة التعطّل.
> - **7.3 نموذج تحسين المرونة** — تُصغّر المؤسسات المخاطر المتبقية في ظل قيود الميزانية، حيث Mi فعالية التخفيف للثغرة i، وCi كلفة التخفيف، وB الميزانية المتاحة؛ ويوفّق هذا الإطار بين استثمارات الأمن السيبراني وأهداف الاستمرارية.»

#### ③ الشرح الفهمي

هذي المعادلات هي العمود الفقري — تحوّل "المرونة" من كلام إلى أرقام قابلة للحساب والبرهان. نمر على الثلاثة ونشوف رموزها.

**7.1 احتمال الفشل بسبب الأحداث السيبرانية**

$$
\lambda_{total} = \lambda_o + \lambda_c
$$

| الرمز | المعنى |
|---|---|
| $\lambda_{total}$ | معدّل الفشل الكلي |
| $\lambda_o$ | معدّل الفشل التشغيلي (operational) |
| $\lambda_c$ | معدّل الفشل الناتج عن الهجمات السيبرانية |

$$
R(t) = e^{-(\lambda_o + \lambda_c)t}
$$

| الرمز | المعنى |
|---|---|
| $R(t)$ | الموثوقية عند الزمن $t$ (احتمال بقاء النظام شغّالاً) |
| $\lambda_o + \lambda_c$ | معدّل الفشل الكلي $\lambda_{total}$ |
| $t$ | الزمن |

المعنى: كل ما يزيد $\lambda_c$ (الفشل السببه الهكر) كل ما يكبر المعدّل الكلي ← تقل الموثوقية $R(t)$. يعني الأمن السيبراني جزء من هندسة الموثوقية، مو شي منفصل.

**7.2 نموذج مؤشر الاستمرارية**

$$
BCI = \frac{\sum_{i=1}^{n} w_i \cdot C_i}{\sum_{i=1}^{n} w_i}
$$

| الرمز | المعنى |
|---|---|
| $BCI$ | مؤشر استمرارية الأعمال (بين 0 و 1) |
| $C_i$ | مستوى الالتزام بمتطلب الاستمرارية $i$ (0–1) |
| $w_i$ | وزن أهمية المتطلب $i$ |
| $n$ | عدد المتطلبات |

المعنى: هذا متوسط مرجّح. مو كل المتطلبات نفس الأهمية، فاللي وزنه أعلى ($w_i$ أكبر) يأثر أكثر على النتيجة. كل ما اقترب BCI من 1 ← مرونة أقوى وقت التعطّل.

**7.3 نموذج تحسين المرونة**

$$
\min R_{\text{residual}} = \sum_{i=1}^{n} \left( R_i \cdot (1 - M_i) \right)
$$

| الرمز | المعنى |
|---|---|
| $R_{\text{residual}}$ | المخاطر المتبقية بعد التخفيف |
| $R_i$ | المخاطر الكامنة للثغرة $i$ |
| $M_i$ | فعالية التخفيف للثغرة $i$ (0–1) |

Subject to:

$$
\sum_{i=1}^{n} C_i \le B
$$

| الرمز | المعنى |
|---|---|
| $C_i$ | كلفة التخفيف للثغرة $i$ |
| $B$ | الميزانية المتاحة |

المعنى: نريد نصغّر المخاطر المتبقية، بس بشرط الكلفة ما تتجاوز الميزانية $B$. الجزء $(1 - M_i)$ هو نسبة الخطر الباقية بعد التخفيف. يعني مو كل شي نصلّحه — نختار التركيبة اللي تعطي أعلى تقليل خطر بأقل كلفة.

ربط بين الثلاثة:

| النموذج | يجيب على أي سؤال |
|---|---|
| 7.1 | شكد الأمن السيبراني يأثر على الموثوقية؟ |
| 7.2 | شكد قوية استمراريتنا الحالية (رقم واحد)؟ |
| 7.3 | وين نصرف ميزانيتنا حتى نصغّر الخطر المتبقي؟ |

---

### القسم 3 — 8. Modern Perspectives in Reliability and Continuity

#### ① النص الأصلي

> Modern perspectives reframe how reliability and continuity are engineered across cloud, analytics, trust, and records.
>
> - **8.1 Cloud-Native Architectures** — cloud providers offer elasticity, redundancy, and global failover as strategic enablers of continuity, yet dependency on third-party infrastructure introduces shared-responsibility risks.
> - **8.2 AI-Driven Predictive Analytics** — machine learning models forecast potential disruptions by analyzing patterns in logs, user behavior, and infrastructure performance, enabling proactive mitigation through predictive reliability engineering.
> - **8.3 Zero Trust Architectures** — by assuming no implicit trust within networks, Zero Trust minimizes the impact of compromised credentials on continuity.
> - **8.4 Blockchain for Resilient Records** — blockchain-based solutions ensure immutable logs and tamper-proof records, enhancing continuity of trust even during systemic disruptions.
>
> Reliability and business continuity in web application security form the backbone of digital resilience. Reliability ensures predictable performance, while continuity guarantees the survival of critical functions under disruption. The fusion of redundancy engineering, proactive vulnerability management, incident response, and regulatory alignment creates a holistic security architecture.
>
> Mathematical models ranging from reliability functions and continuity indices to resilience optimization provide the scientific rigor necessary for strategic decisions. As organizations increasingly depend on digital ecosystems, modern perspectives dictate that reliability and continuity be treated as inseparable pillars of cybersecurity.

#### ② الترجمة

> «تعيد الرؤى الحديثة صياغة طريقة هندسة الموثوقية والاستمرارية عبر السحابة والتحليلات والثقة والسجلات.
>
> - **8.1 المعماريات السحابية الأصلية** — يوفّر مزوّدو السحابة المرونة والتكرار والتحويل العالمي عند الفشل كعوامل تمكينية استراتيجية للاستمرارية، لكن الاعتماد على بنية طرف ثالث يُدخل مخاطر المسؤولية المشتركة.
> - **8.2 التحليلات التنبؤية المدعومة بالذكاء الاصطناعي** — تتنبأ نماذج تعلّم الآلة بالتعطّلات المحتملة عبر تحليل الأنماط في السجلات وسلوك المستخدم وأداء البنية، مما يمكّن من التخفيف الاستباقي عبر هندسة الموثوقية التنبؤية.
> - **8.3 معماريات الثقة الصفرية** — بافتراض عدم وجود ثقة ضمنية داخل الشبكات، تُقلّل الثقة الصفرية من أثر بيانات الاعتماد المخترقة على الاستمرارية.
> - **8.4 البلوكتشين للسجلات المرنة** — تضمن الحلول القائمة على البلوكتشين سجلات غير قابلة للتغيير وسجلات مقاومة للتلاعب، مما يعزّز استمرارية الثقة حتى خلال الاضطرابات المنهجية.
>
> تشكّل الموثوقية واستمرارية الأعمال في أمن تطبيقات الويب العمود الفقري للمرونة الرقمية. فالموثوقية تضمن أداءً متوقعاً، بينما تضمن الاستمرارية بقاء الوظائف الحرجة تحت التعطّل. ودمج هندسة التكرار وإدارة الثغرات الاستباقية والاستجابة للحوادث والمواءمة التنظيمية يخلق معمارية أمنية شاملة.
>
> وتوفّر النماذج الرياضية — من دوال الموثوقية ومؤشرات الاستمرارية إلى تحسين المرونة — الصرامة العلمية اللازمة للقرارات الاستراتيجية. وبما أن المؤسسات تعتمد بشكل متزايد على الأنظمة الرقمية، فإن الرؤى الحديثة تُلزم بمعاملة الموثوقية والاستمرارية كعمودين غير قابلين للفصل في الأمن السيبراني.»

#### ③ الشرح الفهمي

النظرات الحديثة تغيّر طريقة هندسة الاستمرارية. بدل ما نبني حصن واحد وننتظر، نستعمل السحابة والذكاء الاصطناعي وZero Trust والبلوكتشين. نمر على الأربعة:

- **8.1 Cloud-Native**: السحابة تعطيك elasticity (توسّع عند الحاجة)، redundancy (نسخ احتياطية)، وglobal failover (تحويل عالمي عند العطل). بس الجانب الثاني: صرت تعتمد على طرف ثالث ← خطر "المسؤولية المشتركة" (shared responsibility).
- **8.2 AI Predictive Analytics**: موديلات ML تحلل اللوغات وسلوك المستخدم وأداء البنية ← تتنبأ بالعطل قبل وقوعه. يعني تخفيف استباقي (proactive) بدل رد فعل.
- **8.3 Zero Trust**: ما تفترض ثقة ضمنية بأي شبكة داخلية أو جلسة. هذا يقلل أثر سرقة بيانات الدخول على الاستمرارية — لأن السرقة ما تعطي حركة حرة.
- **8.4 Blockchain**: سجلات immutable وغير قابلة للتلاعب ← استمرارية الثقة حتى وقت الاضطراب المنهجي.

| الاتجاه | الفكرة | الفائدة للاستمرارية | التحدي |
|---|---|---|---|
| Cloud-Native | elasticity + redundancy + global failover | تعافي سريع وعالمي | shared-responsibility risk |
| AI Predictive | ML يتنبأ بالعطل من اللوغات والسلوك | تخفيف استباقي قبل المشكلة | جودة البيانات والإنذارات الكاذبة |
| Zero Trust | لا ثقة ضمنية، تحقق مستمر | يقلل أثر سرقة الدخول | التعقيد التشغيلي |
| Blockchain | سجلات immutable | استمرارية الثقة وقت الاضطراب | الأداء والكلفة |

وبعدها الوثيقة تختم بالخلاصة:

- الموثوقية تضمن الأداء المتوقع، والاستمرارية تضمن بقاء الوظائف الحرجة.
- دمج redundancy engineering + إدارة ثغرات استباقية + incident response + regulatory alignment = معمارية أمنية شاملة (holistic).
- النماذج الرياضية (reliability functions، continuity indices، resilience optimization) هي اللي تعطي القرارات الاستراتيجية الصرامة العلمية.
- النتيجة النهائية: الموثوقية والاستمرارية عمودين ما ينفصلون في الأمن السيبراني.
