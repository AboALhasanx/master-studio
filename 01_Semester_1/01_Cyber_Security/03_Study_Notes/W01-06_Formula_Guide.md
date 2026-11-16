---
title: "Cyber Security — شرح معادلات الفصول 1 إلى 6"
subtitle: "معنى كل رمز، فكرة القانون، موضع استخدامه، وتفسير الناتج مع أمثلة محلولة"
subject: "01_Cyber_Security"
week: 1
sources:
  - "W01_DeepDive.md and W01_Annotation_Map.md"
  - "W02_Formulas.md and W02_Chapter2_TriLayer.md"
  - "W03_Chapter3_TriLayer.md and W04_Chapter4_TriLayer.md"
  - "W05_Chapter5_TriLayer.md and W06_Chapter6_TriLayer.md"
type: "exam formula guide — expanded symbol-by-symbol edition"
---

# شرح معادلات Cyber Security — الفصول 1 إلى 6

هذا دليل شرح، مو بطاقة قوانين مزدحمة. كل صيغة معروضة وحدها، وبعدها نفك رموزها ونوضح فكرتها ومتى تنفع وما الذي تقوله النتيجة. المعادلة الرياضية نفسها تبقى باتجاهها القياسي من اليسار إلى اليمين، أما الشرح العربي فيُقرأ من اليمين إلى اليسار. الأمثلة الموسومة **مثال تدريبي** جديدة للتوضيح وليست أمثلة الملزمة.

## حدود المادة والحذوفات

| الفصل | ما استبعدته حسب ملاحظات المادة | ما أفعله هنا |
|:---|:---|:---|
| 1 | دراسات الحالة التابعة للفصل 7 مثل Stuxnet وColonial Pipeline وGDPR enforcement. | أشرح صيغ الفصول 1–6 فقط. |
| 2 | كتل NIST، المثال الرقمي للملزمة، البند «رقم 6»، والموضوعات بعد Authentication المحددة في ملاحظة «ما مو داخل». | أبقي صيغتي الخطر الأساسي والمتبقي فقط، وأستخدم أرقاماً تدريبية جديدة. |
| 3 | الأجزاء المشطوبة في خريطة الفصل، ومنها Balancing Cost of Controls وPolicy vs. Technology وتعريف السياسة وأمثلتها وبعض أمثلة السياسة والبند «رقم 6». | لا أعيد أمثلة هذه الأجزاء. أشرح الصيغ التي بقيت في ملخص المعادلات، مع تمييز الأمثلة الجديدة. |
| 4 | لا يوجد حذف محدد موثق في سجل المادة للفصل. | أشرح صيغ التشفير الواردة في ملخص الفصل ومذكرته. |
| 5 | لا يوجد حذف محدد موثق في سجل المادة. | أشرح الصيغ الواردة في مذكرة الفصل. |
| 6 | الصفحتان المطبوعتان 12–13 من النسخة المؤشّرة خارجتان بالكامل. | استبعدت النماذج الخاصة بهاتين الصفحتين؛ أبقيت صيغة التوازي الواردة قبلها في الصفحة 10. |

مصدر حدود الحذف: `W01_Annotation_Map.md`، فقرة «ما مو داخل» في `W02_Chapter2_TriLayer.md`، خريطة التأشيرات وخلاصة الحذف في `W03_Chapter3_TriLayer.md`، وسجلات جلسات 2026-09-18 و2026-09-23 و2026-09-26. وفي الفصل 6 راجعت نسخة الدكتورة المؤشّرة: ص12–13 مستبعدتان؛ لذلك لا أدرج معادلات Mahalanobis وZero Trust وAPI risk والـquantum وDevSecOps leakage والحاويات والـbiometrics والـblockchain الخاصة بهما. صيغة موثوقية التوازي في الدليل باقية لأنها واردة قبل ذلك في ص10 ضمن الجزء الداخل، وليست اعتماداً على صيغة الحاويات في ص13.

## طريقة قراءة أي مسألة رياضية

1. حدّد الكمية التي يطلبها السؤال: احتمال، خطر، زمن، كلفة، موثوقية، أو أداء.
2. طابق معنى الرموز مع كلمات السؤال، ولا تختَر الصيغة من شكل الحرف وحده. الرمز `R(t)` مثلاً له معنيان مختلفان في الفصلين 1 و6.
3. اكتب الصيغة وحدها، ثم عوّض القيم مع وحداتها، وبعدها احسب.
4. فسّر الرقم بوحدته ومعناه. النتيجة `0.2` قد تعني احتمالاً 20%، أو خطراً على مقياس عددي، بحسب تعريف السؤال.
5. إذا كانت القيم وصفية مثل Low وMedium وHigh، استخدم مصفوفة المادة؛ لا تحوّلها إلى أرقام من عندك.

<div class="page-break"></div>

## الفصل 1 — أساسيات الخطر والأمن

### 1. تقليل الخطر المتوقع بعد الاستثمار الأمني (Expected Risk Minimization After Security Investment)

$$\min R = \sum_{i=1}^{n} P_i I_i - \sum_{j=1}^{m} C_j$$

**الرموز:** `R` الخطر/القيمة التي نريد تقليلها؛ `P_i` احتمال التهديد رقم `i`؛ `I_i` أثره؛ `C_j` استثمار الضابط رقم `j`؛ `n` عدد التهديدات و`m` عدد الضوابط. مجموع `P_i I_i` يجمع الخسائر المتوقعة، والحد الثاني يمثل استثمارات الحماية وفق صياغة المحاضرة.

**الفكرة ومتى تظهر:** صيغة الهدف تقارن الخسارة المتوقعة بكلفة الضوابط ضمن مسألة تحسين. لحلّ `min` فعلياً نحتاج بدائل للخطط وقيودها؛ المثال هنا يحسب الطرف الأيمن لخطة واحدة فقط. الناتج قيمة على مقياس المحاضرة، وليس احتمالاً تلقائياً.

**Worked example:** For one specified security plan, two threat scenarios have probability-impact pairs (0.2, 100) and (0.1, 200), and the plan costs 15 units. Evaluate the right-hand side of the course expression for this plan.
{.keep-next}

**Solution:**
{.keep-next}

$$ \text{RHS for this plan}=(0.2\times100)+(0.1\times200)-15=40-15=25\text{ units} $$

### 2. التعرض للخطر المتغير مع الزمن (Time-Dependent Risk Exposure)

$$R(t)=\sum_{i=1}^{n}P_i(t)I_i(t)$$

**الرموز:** `t` الزمن؛ `P_i(t)` احتمال التهديد `i` عند ذلك الزمن؛ `I_i(t)` أثره عند ذلك الزمن؛ `n` عدد التهديدات. `Σ` تعني حساب حاصل الاحتمال في الأثر لكل تهديد ثم جمع النواتج.

**الفكرة ومتى تظهر:** هذه صيغة تعرض الخطر؛ تفيد عندما تتغير احتمالات الهجمات أو آثارها بمرور الوقت. الناتج درجة/قيمة خطر في الزمن `t`، وليس احتمال بقاء مكوّن عاملاً.

**Worked example:** At time t, two threats have probability-impact pairs of (0.1, 100) and (0.2, 50).
{.keep-next}

**Solution:**
{.keep-next}

$$ R(t)=0.1\times100+0.2\times50=20 $$

### 3. منفعة CIA الموزونة (Weighted CIA Utility)

$$U(C,I,A)=\alpha C+\beta I+\gamma A$$

**الرموز:** `C` درجة Confidentiality السرية؛ `I` درجة Integrity السلامة؛ `A` درجة Availability التوفر؛ `α, β, γ` أوزان الأهمية؛ `U` المنفعة الناتجة. مجموع الأوزان عادة يساوي 1 إذا عرّف السؤال ذلك.

**الفكرة ومتى تظهر:** تُستخدم لمقارنة أهمية أبعاد CIA في نظام معيّن عندما يعطي السؤال درجات وأوزاناً. الناتج درجة منفعة موزونة، وتُفهم مقارنةً بمقياس الإدخال.

**Worked example:** Let confidentiality, integrity, and availability scores be 0.8, 0.9, and 0.5, with weights 0.4, 0.4, and 0.2.
{.keep-next}

**Solution:**
{.keep-next}

$$ U=0.4(0.8)+0.4(0.9)+0.2(0.5)=0.78 $$

### 4. مساحة الهجوم (Attack Surface)

$$AS=\sum_{j=1}^{m} E_jV_jA_j$$

**الرموز:** `AS` Attack Surface؛ `j` مكوّن النظام؛ `m` عدد المكوّنات؛ `E_j` نقاط الدخول/التعرض؛ `V_j` شدة أو قابلية الثغرة في المكوّن؛ `A_j` قيمة الأصل المتأثر.

**الفكرة ومتى تظهر:** تفيد عند مقارنة سطح الهجوم قبل تقليل نقاط الدخول أو بعده. نضرب عوامل كل مكوّن ثم نجمع، لذلك الناتج مؤشر مقارن وفق المقياس المعطى، وليس احتمالاً موحداً.

**Worked example:** A component has exposure E=2, vulnerability V=5, and asset value A=10. Then reduce E to 1 while keeping the other values fixed.
{.keep-next}

**Solution:**
{.keep-next}

$$ AS_{before}=2\times5\times10=100\qquad AS_{after}=1\times5\times10=50 $$

### 5. احتمال تجاوز عتبة خطر (Probability of Exceeding a Risk Threshold)

$$P(R>r)=1-F(r)$$

**الرموز:** `R` متغير الخطر؛ `r` العتبة؛ `F(r)` احتمال أن يكون الخطر أقل من أو مساوياً للعتبة وفق التوزيع التراكمي؛ `P(R>r)` احتمال تجاوزها.

**الفكرة ومتى تظهر:** تظهر عندما يعطي السؤال قيمة CDF ويطلب احتمال أن تتجاوز القيمة حدّاً. الناتج احتمال بين 0 و1.

**Worked example:** If the cumulative distribution value at the threshold is F(r)=0.8, find the probability of exceeding the threshold.
{.keep-next}

**Solution:**
{.keep-next}

$$ P(R>r)=1-F(r)=1-0.8=0.2=20\% $$

### 6. مؤشر الامتثال الموزون (Weighted Compliance Index)

$$PCI=\frac{\sum_{k=1}^{n}w_kc_k}{\sum_{k=1}^{n}w_k}$$

**الرموز:** `k` متطلب امتثال؛ `n` عدد المتطلبات؛ `c_k` درجة الامتثال للمتطلب، غالباً من 0 إلى 1؛ `w_k` وزن أهمية المتطلب؛ `PCI` المتوسط الموزون.

**الفكرة ومتى تظهر:** استخدمه عندما تختلف أهمية المتطلبات. الناتج درجة امتثال موزونة؛ اضرب كل درجة بوزنها، اجمع، ثم اقسم على مجموع الأوزان.

**Worked example:** Compliance scores are 0.8 with weight 3 and 0.5 with weight 1.
{.keep-next}

**Solution:**
{.keep-next}

$$ PCI=\frac{3(0.8)+1(0.5)}{3+1}=0.725=72.5\% $$

## الفصل 2 — تقييم المخاطر

### 7. الخطر الأساسي (Inherent Risk (Risk Matrix))

$$S=F\times K$$

**الرموز:** `S` مستوى الخطر الأساسي؛ `F` تكرار/احتمال الحادث كما تسميه المادة؛ `K` العاقبة أو شدة الأثر. في مقياس المادة قد تكون `F` و`K` فئات وصفية.

**الفكرة ومتى تظهر:** تظهر عندما يطلب السؤال تحديد الخطر من احتمال/تكرار وعاقبة. إذا أعطى قيم Low/Medium/High، نأخذ المستوى من مصفوفة الخطر. الناتج فئة أو درجة بحسب المقياس، وليس ضرباً رقمياً مفروضاً.

**Worked example:** According to the course risk matrix, both the frequency and consequence are High. Identify the risk level.
{.keep-next}

**Solution:**
{.keep-next}

$$ S=F\times K\quad\Rightarrow\quad\text{High frequency + High consequence = High (red) risk} $$

### 8. الخطر المتبقي بعد الضوابط (Residual Risk After Controls)

$$R=\frac{S}{M}$$

**الرموز:** `R` الخطر المتبقي؛ `S` الخطر الأساسي؛ `M` عامل الحماية/أثر الضوابط وفق تعريف الملزمة. إذا كان التقييم وصفياً فاستعمل طريقة المصفوفة الخاصة بالمادة.

**الفكرة ومتى تظهر:** تسأل المسألة عن الخطر بعد وجود وسائل حماية. الصيغة توضح اتجاه العلاقة: زيادة الحماية تخفض الخطر في هذا النموذج؛ والناتج مستوى الخطر بعد أخذ العامل بالحسبان.

**Worked example:** A numeric scale is explicitly provided with inherent risk S=12 and control factor M=3.
{.keep-next}

**Solution:**
{.keep-next}

$$ R=\frac{S}{M}=\frac{12}{3}=4 $$

## الفصل 3 — الخسائر والفعالية

### 9. الخسارة المالية المتوقعة (Expected Financial Loss)

$$EFL=\sum_{i=1}^{n}P_iI_i$$

**الرموز:** `EFL` Expected Financial Loss؛ `P_i` احتمال الحادث `i`؛ `I_i` قيمة خسارته المالية عند حدوثه؛ `n` عدد الحوادث/السيناريوهات. الناتج خسارة مالية متوقعة بوحدة العملة.

**الفكرة ومتى تظهر:** نستخدمها عندما تُعطى احتمالات عدة حوادث وآثار مالية وتُطلب الخسارة المتوقعة الكلية. هذه هي قيمة الخطر المالي المتوقعة بحسب السيناريوهات المدرجة.

**Worked example:** Two incidents have probabilities 0.1 and 0.2 and financial losses of $10,000 and $2,000.
{.keep-next}

**Solution:**
{.keep-next}

$$ EFL=0.1(10{,}000)+0.2(2{,}000)=1{,}400\text{ dollars} $$

### 10. نموذج الخطر: تهديد × ضعف × أثر (Threat–Vulnerability–Impact Risk Model)

$$Risk=Threat\times Vulnerability\times Impact$$

**الرموز:** `Threat` وجود/قوة التهديد؛ `Vulnerability` قابلية الاستغلال؛ `Impact` حجم الأثر. القيم قد تكون درجات على مقياس يحدده السؤال.

**الفكرة ومتى تظهر:** مفيد لترتيب المخاطر عندما تتوفر درجات للعوامل الثلاثة. إذا كان أحد العوامل منخفضاً جداً، ينخفض التقدير الناتج في هذا النموذج.

**Worked example:** On the assumed course scale, Threat=2, Vulnerability=3, and Impact=5.
{.keep-next}

**Solution:**
{.keep-next}

$$ Risk=2\times3\times5=30 $$

### 11. فعالية السياسة من تغير عدد الحوادث (Policy Effectiveness)

$$PE=\frac{Incidents_{before}-Incidents_{after}}{Incidents_{before}}$$

**الرموز:** `PE` Policy Effectiveness؛ `Incidents_before` عدد الحوادث قبل السياسة؛ `Incidents_after` عددها بعدها. الناتج نسبة التغير قياساً إلى خط الأساس.

**الفكرة ومتى تظهر:** تستخدم عندما يُقارن عدد الحوادث قبل تطبيق سياسة وبعدها. نتيجة موجبة تعني انخفاضاً؛ الصفر يعني لا تغير؛ والسالبة تعني زيادة الحوادث.

**Worked example:** Incidents decreased from 50 before a policy change to 10 afterward.
{.keep-next}

**Solution:**
{.keep-next}

$$ PE=\frac{50-10}{50}=0.8=80\% $$

## الفصل 4 — التشفير

### 12. تشفير النص الصريح (Encryption)

$$C=E_K(P)$$

**الرموز:** `P` Plaintext النص قبل التشفير؛ `K` المفتاح؛ `E` خوارزمية التشفير؛ `C` Ciphertext الناتج المشفّر.

**الفكرة ومتى تظهر:** عندما يطلب السؤال تحويل رسالة مقروءة إلى تمثيل محمي بمفتاح. الناتج `C` لا يُقرأ كالنص الأصلي دون إجراء فك مناسب.

**Worked example:** Let Eₖ denote the course encryption function with key K. Write the ciphertext produced from plaintext HI using the course notation.
{.keep-next}

**Solution:**
{.keep-next}

$$ C=E_K(\text{HI}) $$

### 13. فك التشفير (Decryption)

$$P=D_K(C)$$

**الرموز:** `C` النص المشفّر؛ `D` خوارزمية فك التشفير؛ `K` المفتاح المناسب؛ `P` النص المستعاد.

**الفكرة ومتى تظهر:** تظهر عندما يطلب السؤال استعادة النص الأصلي من النص المشفّر. الناتج رسالة مقروءة إذا كان المفتاح والخوارزمية صحيحين.

**Worked example:** For a reversible course cipher, let C=Eₖ(HI). Decrypt C with the same key K.
{.keep-next}

**Solution:**
{.keep-next}

$$ P=D_K(C)=D_K(E_K(\text{HI}))=\text{HI} $$

### 14. مسافة الوحدانية (Unicity Distance)

$$U\approx\frac{H(K)}{D}$$

**الرموز:** `U` كمية النص التقريبية التي قد تجعل استنتاج المفتاح ممكناً؛ `H(K)` إنتروبيا/عدم يقين المفتاح؛ `D` مقدار التكرار اللغوي (redundancy) حسب تعريف المذكرة.

**الفكرة ومتى تظهر:** تقدير نظري لكمية النص اللازمة لزوال الغموض عن المفتاح. الناتج وحدات نصية تقريبية، ويتأثر بمقياس الإنتروبيا والتكرار.

**Worked example:** Let the key entropy be 40 bits and the language redundancy be 2 bits per character. Estimate the unicity distance.
{.keep-next}

**Solution:**
{.keep-next}

$$ U\approx\frac{40\text{ bits}}{2\text{ bits/character}}=20\text{ characters} $$

### 15. متوسط زمن تجربة مفتاح بالقوة الغاشمة (Average Brute-Force Key Search Time)

$$T_{crack}\approx\frac{2^{k-1}}{R}$$

**الرموز:** `T_crack` الزمن المتوقع؛ `k` طول المفتاح بالبت؛ `2^k` حجم فضاء المفتاح؛ `2^(k−1)` متوسط عدد المحاولات إذا كان المفتاح موزعاً بالتساوي؛ `R` المحاولات في الثانية.

**الفكرة ومتى تظهر:** تستخدم لتقدير زمن البحث المتوسط. الناتج بوحدة الزمن التي تنتج من وحدات `R`؛ كلما زاد طول المفتاح، نما زمن التجربة أُسّياً.

**Worked example:** For an 8-bit key, the attacker tests 16 keys per second on average.
{.keep-next}

**Solution:**
{.keep-next}

$$ T_{crack}\approx\frac{2^{8-1}}{16}=8\text{ seconds} $$

### 16. أمان النظام الهجين (Hybrid-System Security Strength)

$$S_{TLS}=\min(S_{sym},S_{asym},S_{hash})$$

**الرموز:** `S_TLS` قوة الأمان التقريبية للنظام الهجين؛ `S_sym` أمان التشفير المتماثل؛ `S_asym` أمان التشفير غير المتماثل؛ `S_hash` أمان الهاش/المصادقة، وفق وحدات القوة المعطاة.

**الفكرة ومتى تظهر:** الأمن الكلي لا يتجاوز أضعف مكوّن في السلسلة. الناتج هو أصغر تقدير أمان، لا مجموعها.

**Worked example:** The hybrid system uses security strengths of 128, 112, and 128 bits.
{.keep-next}

**Solution:**
{.keep-next}

$$ S_{TLS}=\min(128,112,128)=112\text{ bits} $$

### 17. كلفة الهجوم الحسابية (Computational Attack Cost)

$$C_{attack}=R\times T\times c$$

**الرموز:** `C_attack` كلفة المحاولات؛ `R` عدد المحاولات في الزمن؛ `T` مدة الهجوم بوحدة زمن متوافقة؛ `c` كلفة المحاولة الواحدة.

**الفكرة ومتى تظهر:** تستخدم عندما تُعطى سرعة التجربة والمدة وسعر المحاولة. الناتج كلفة كلية بالوحدة المالية نفسها المستخدمة في `c`.

**Worked example:** An attacker makes 1,000 attempts per second for 60 seconds; each attempt costs 0.01 units.
{.keep-next}

**Solution:**
{.keep-next}

$$ \begin{aligned}C_{attack}&=(1{,}000)(60)(0.01)\\&=600\text{ cost units}\end{aligned} $$

### 18. تشفير Caesar (Caesar Cipher Encryption)

$$E(x)=(x+k)\bmod 26$$

**الرموز:** `x` رقم الحرف؛ `k` مقدار الإزاحة؛ `26` عدد حروف الأبجدية الإنجليزية؛ `mod 26` يعيد النتيجة إلى المجال 0–25.

**الفكرة ومتى تظهر:** تشفير حرف بإزاحته `k` مواقع مع الالتفاف عند نهاية الأبجدية. الناتج رقم الحرف المشفّر.

**Worked example:** Using zero-based letters, encrypt x=2 with Caesar shift k=3.
{.keep-next}

**Solution:**
{.keep-next}

$$ E(x)=(2+3)\bmod26=5 $$

### 19. فك Caesar (Caesar Cipher Decryption)

$$D(x)=(x-k)\bmod 26$$

**الرموز:** `x` رقم الحرف المشفّر؛ `k` الإزاحة؛ الطرح يعكس عملية التشفير؛ `mod 26` يحافظ على رقم صالح.

**الفكرة ومتى تظهر:** عندما يطلب استرجاع الحرف الأصلي من Caesar. الناتج رقم الحرف قبل الإزاحة.

**Worked example:** Decrypt Caesar value 5 using shift k=3.
{.keep-next}

**Solution:**
{.keep-next}

$$ D(5)=(5-3)\bmod26=2 $$

### 20. تشفير Vigenère عند الموضع i (Vigenère Cipher Encryption at Position i)

$$C_i=(P_i+K_i)\bmod 26$$

**الرموز:** `i` موضع الحرف؛ `P_i` رقم الحرف الأصلي؛ `K_i` رقم حرف المفتاح المقابل؛ `C_i` رقم الحرف المشفّر؛ `mod 26` التفاف الأبجدية.

**الفكرة ومتى تظهر:** تستعمل عندما يتغير مفتاح الإزاحة بحسب موضع الحرف. الناتج حرف مشفّر لكل موضع.

**Worked example:** At position i, let plaintext value P_i=2 and key value K_i=3.
{.keep-next}

**Solution:**
{.keep-next}

$$ C_i=(2+3)\bmod26=5 $$

### 21. عدد المفاتيح المشتركة بين n مستخدمين (Pairwise Shared-Key Count)

$$N_{keys}=\frac{n(n-1)}{2}$$

**الرموز:** `n` عدد المستخدمين؛ `N_keys` عدد المفاتيح الثنائية اللازمة إذا كان لكل زوج مفتاحه الخاص. القسمة على 2 تمنع عدّ الزوج مرتين.

**الفكرة ومتى تظهر:** تقيس عبء توزيع المفاتيح في نموذج الاتصال الثنائي الكامل. الناتج عدد مفاتيح.

**Worked example:** Find the number of pairwise shared keys required for four users.
{.keep-next}

**Solution:**
{.keep-next}

$$ N_{keys}=\frac{4(4-1)}{2}=6\text{ keys} $$

<div class="page-break"></div>

### 22. RSA: حساب n (RSA Modulus)

$$n=pq$$

**الرموز:** `p,q` عددان أوليان مختاران في المثال؛ `n` حاصل ضربهما ويكوّن جزءاً من المفتاح العام والخاص.

**الفكرة ومتى تظهر:** أول خطوة في المثال التعليمي لتوليد مفاتيح RSA. الناتج معامل الحساب modulo.

**Worked example:** Choose primes p=3 and q=11 for a small RSA demonstration.
{.keep-next}

**Solution:**
{.keep-next}

$$ n=pq=3\times11=33 $$

### 23. RSA: دالة أويلر (Euler Totient Function)

$$\varphi(n)=(p-1)(q-1)$$

**الرموز:** `φ(n)` عدد الأعداد من 1 إلى `n` المتباينة نسبياً مع `n`؛ `p,q` أوليان مختلفان؛ `n=pq`.

**الفكرة ومتى تظهر:** تحسب القيمة المستخدمة لاختيار الأسّين في RSA التعليمي. الناتج يحدد شرط العلاقة بين `e` و`d`.

**Worked example:** For p=3 and q=11, calculate Euler's totient value.
{.keep-next}

**Solution:**
{.keep-next}

$$ \varphi(n)=(3-1)(11-1)=20 $$

### 24. RSA: اختيار الأس الخاص d (RSA Private Exponent)

$$d\equiv e^{-1}\pmod{\varphi(n)}$$

**الرموز:** `e` الأس العام؛ `d` الأس الخاص؛ `e⁻¹ mod φ(n)` المعكوس الضربي؛ `≡` تكافؤ باقي القسمة.

**الفكرة ومتى تظهر:** نختار `d` بحيث `ed` يعطي باقي 1 عند القسمة على `φ(n)`. الناتج أسّ فك التشفير.

**Worked example:** Let e=3 and φ(n)=20. Find the modular inverse d.
{.keep-next}

**Solution:**
{.keep-next}

$$ 3d\equiv1\pmod{20}\qquad d=7\quad(3\times7=21\equiv1\pmod{20}) $$

### 25. RSA: التشفير (RSA Encryption)

$$C=P^e\bmod n$$

**الرموز:** `P` الرسالة ممثلة بعدد؛ `e` الأس العام؛ `n` معامل RSA؛ `C` النص المشفّر؛ `mod n` باقي القسمة.

**الفكرة ومتى تظهر:** عند حساب تشفير رسالة في المثال الرياضي. الناتج عدد بين `0` و`n−1`.

**Worked example:** Encrypt plaintext number P=4 with e=3 and n=33.
{.keep-next}

**Solution:**
{.keep-next}

$$ C=4^3\bmod33=31 $$

### 26. RSA: فك التشفير (RSA Decryption)

$$P=C^d\bmod n$$

**الرموز:** `C` النص المشفّر؛ `d` الأس الخاص؛ `n` المعامل؛ `P` الرسالة المستعادة.

**الفكرة ومتى تظهر:** تحسب استعادة الرسالة بالأس الخاص. إذا اتفقت معاملات المفتاح مع شروط المثال، يرجع الناتج `P`.

**Worked example:** Decrypt ciphertext C=31 with d=7 and n=33.
{.keep-next}

**Solution:**
{.keep-next}

$$ P=31^7\bmod33=4 $$

### 27. دالة الهاش (Hash Function)

$$h:\{0,1\}^{*}\to\{0,1\}^{n}$$

**الرموز:** `h` دالة الهاش؛ `{0,1}*` مدخل بطول متغير من البتات؛ `{0,1}^n` خرج بطول ثابت مقداره `n` بت.

**الفكرة ومتى تظهر:** تشرح أن الرسائل مختلفة الأطوال تتحول إلى بصمة ثابتة الطول. الخرج ملخص للمقارنة والتحقق، وليس تشفيراً قابلاً للعكس.

**Worked example:** A 1,000-bit message and a 2,000,000-bit file are hashed by the same fixed-length hash function.
{.keep-next}

**Solution:**
{.keep-next}

$$ |h(M_1)|=|h(M_2)|=n\text{ bits} $$

### 28. إنشاء التوقيع الرقمي (Digital Signature Generation)

$$Sig=E_{Priv}(h(M))$$

**الرموز:** `M` الرسالة؛ `h(M)` بصمتها؛ `Priv` المفتاح الخاص للمرسل؛ `E` عملية إنشاء التوقيع بحسب اصطلاح مذكرتك؛ `Sig` التوقيع.

**الفكرة ومتى تظهر:** تربط التوقيع بالرسالة وبمفتاح صاحبها. الناتج توقيع يمكن التحقق منه بالمفتاح العام؛ تطبيقات التوقيع الفعلية تستخدم خوارزمية توقيع معيارية.

**Worked example:** A digital signature is generated by signing the message digest rather than every message bit separately.
{.keep-next}

**Solution:**
{.keep-next}

$$ Sig=E_{Priv}(h(M)) $$

### 29. التحقق من التوقيع (Digital Signature Verification)

$$h(M)\stackrel{?}{=}D_{Pub}(Sig)$$

**الرموز:** `h(M)` البصمة المحسوبة للرسالة المستلمة؛ `Pub` المفتاح العام؛ `D_Pub(Sig)` القيمة المستخرجة/المتحقق منها من التوقيع وفق اصطلاح الملزمة؛ علامة الاستفهام تعني مقارنة القيمتين.

**الفكرة ومتى تظهر:** إذا تطابقت القيمتان، فهذا يدعم سلامة الرسالة وصحة التوقيع ضمن افتراضات النظام والثقة بالمفتاح. الناتج قرار تطابق/عدم تطابق.

**Worked example:** Suppose the message digest is a and the digest recovered from the signature is b, where a≠b.
{.keep-next}

**Solution:**
{.keep-next}

$$ h(M)=a\ne b=D_{Pub}(Sig)\quad\Rightarrow\quad\text{verification fails} $$

### 30. احتمال تصادم هاش n-bit في نموذج مبسط (Simplified n-bit Hash-Guess Probability)

$$P_{int}\approx2^{-n}$$

**الرموز:** `P_int` احتمال محاولة تطابق/تزوير محددة في النموذج المبسط للمذكرة؛ `n` طول خرج الهاش بالبت؛ الأس السالب يعني واحداً على `2^n`.

**الفكرة ومتى تظهر:** تقدير توضيحي لاحتمال تخمين قيمة محددة. لا تخلط هذا بتقدير هجوم birthday على وجود أي زوج متصادم؛ كما أن التصادمات مستحيلة التجنب تماماً عندما يكون المدخل أطول من فضاء الخرج.

**Worked example:** For an 8-bit output, estimate the chance of one exact random hash guess.
{.keep-next}

**Solution:**
{.keep-next}

$$ P_{int}\approx2^{-8}=\frac{1}{256}\approx0.0039=0.39\% $$

### 31. زمن تجربة توقيع بطول b bit (Signature Brute-Force Time)

$$T_{forge}\approx\frac{2^{b_{sig}}}{R}$$

**الرموز:** `T_forge` الزمن التقريبي؛ `b_sig` عدد البتات التي يفترض النموذج أنها تحمي التوقيع؛ `R` محاولات في الثانية.

**الفكرة ومتى تظهر:** تقدير بحث شامل عندما يحدد السؤال فضاءً من `2^b` احتمالاً. الناتج بوحدة الزمن المتوافقة مع `R`.

**Worked example:** An 8-bit signature space is tested at 32 guesses per second. Find the exhaustive full-space search time.
{.keep-next}

**Solution:**
{.keep-next}

$$ T_{forge}\approx\frac{2^8}{32}=\frac{256}{32}=8\text{ seconds} $$

### 32. الثقة في سلسلة الشهادات (Certificate-Chain Trust Probability)

$$P_{trust}=(1-P_{ca})(1-P_{val})$$

**الرموز:** `P_ca` احتمال اختراق/فشل جهة التصديق؛ `P_val` احتمال فشل التحقق؛ المكمّل `1−P` احتمال عدم وقوع الفشل المفترض؛ `P_trust` قيمة الثقة في هذا النموذج المبسط.

**الفكرة ومتى تظهر:** تستخدم إذا عرّف السؤال عاملَي فشل مستقلين. الناتج حاصل احتمال اجتياز العاملين وفق افتراض الاستقلال.

**Worked example:** The CA failure probability is 0.01 and the independent validation failure probability is 0.02. Find the probability both trust checks succeed.
{.keep-next}

**Solution:**
{.keep-next}

$$ P_{trust}=(1-0.01)(1-0.02)=0.99\times0.98=0.9702 $$

### 33. الأمان الكلي عبر احتمالات الإخفاق (Combined Security Probability)

$$P_{secure}=(1-P_{int})(1-P_{sig})(1-P_{trust})$$

**الرموز:** `P_int` احتمال إخفاق سلامة الهاش في النموذج؛ `P_sig` احتمال إخفاق التوقيع؛ `P_trust` احتمال فشل الثقة؛ كل عامل `1−P` يمثل عدم وقوع الإخفاق المقابل.

**الفكرة ومتى تظهر:** صيغة تركيب مبسطة تحت افتراض الاستقلال. الناتج قيمة مركبة؛ تأكد من أن المذكرة عرّفت كل `P` بالطريقة نفسها قبل الحساب.

**Worked example:** Integrity, signature, and trust failures are independent, with probabilities P_int=0.01, P_sig=0.02, and P_trust=0.03. Find the probability all three checks succeed.
{.keep-next}

**Solution:**
{.keep-next}

$$ P_{secure}=(1-0.01)(1-0.02)(1-0.03)=0.941094 $$

### 34. زمن كسر النظام الهجين (Hybrid-System Break Time)

$$T_{system}=\min(T_{sym},T_{asym})$$

**الرموز:** `T_sym` زمن كسر المكوّن المتماثل؛ `T_asym` زمن كسر المكوّن غير المتماثل؛ `min` تختار الأصغر.

**الفكرة ومتى تظهر:** عندما يعتمد النظام على المكوّنين معاً، أضعفهما زمنياً قد يحدد أقصر مسار للهجوم. الناتج الزمن الأصغر، وليس مقياس البتات `S_TLS`.

**Worked example:** The symmetric and asymmetric break-time estimates are 10 years and 3 years.
{.keep-next}

**Solution:**
{.keep-next}

$$ T_{system}=\min(10,3)=3\text{ years} $$

## الفصل 5 — أمن الشبكات والكشف

### 35. حمل طابور SYN (SYN Queue Utilization)

$$\rho=\frac{\lambda}{\mu}$$

**الرموز:** `λ` معدل وصول طلبات SYN؛ `μ` معدل خدمة الطلبات؛ `ρ` نسبة الحمل إلى قدرة الخدمة. يجب قياس المعدلين بوحدة واحدة، مثل اتصال/ثانية.

**الفكرة ومتى تظهر:** تعطي مؤشراً على ضغط الطابور. عندما تقترب `ρ` من 1 يرتفع الضغط، وإذا تجاوزت 1 باستمرار فالوصول أسرع من الخدمة.

**Worked example:** The SYN arrival rate is 80 connections per second and the service rate is 100 per second.
{.keep-next}

**Solution:**
{.keep-next}

$$ \rho=\frac{80}{100}=0.8 $$

### 36. احتمال حجب اتصال شرعي بسبب امتلاء الطابور (SYN Queue Blocking Probability)

$$P_{block}=\frac{(1-\rho)\rho^B}{1-\rho^{B+1}}\quad(\rho\ne1)$$

**الرموز:** `P_block` احتمال الحجب في نموذج الطابور؛ `ρ` الحمل؛ `B` سعة الطابور؛ الشرط `ρ≠1` لأن الصيغة المكتوبة لا تغطي حالة الواحد.

**الفكرة ومتى تظهر:** تستخدم فقط إذا أعطى السؤال نموذج الطابور وقيم `ρ,B`. الناتج احتمال ضمن افتراضات النموذج؛ ليست قاعدة عامة لكل هجوم SYN.

**Worked example:** For an M/M/1/2 queue, where capacity 2 includes the job in service, utilization is ρ=0.5. Find the blocking probability.
{.keep-next}

**Solution:**
{.keep-next}

$$ P_{block}=\frac{(1-0.5)(0.5)^2}{1-(0.5)^3}=\frac{0.125}{0.875}=\frac17\approx0.1429 $$

### 37. مكونات DFA لمحلل ترويسات IPv6 (DFA Definition for IPv6 Extension-Header Parsing)

$$H=(S,\Sigma,\delta,s_0,F)$$

**الرموز:** `S` مجموعة الحالات؛ `Σ` رموز الإدخال؛ `δ` دالة الانتقال؛ `s₀` حالة البداية؛ `F` مجموعة الحالات النهائية؛ `H` الآلة كاملة.

**الفكرة ومتى تظهر:** هذا تعريف لبنية آلة حالات محدودة، مو معادلة حساب قيمة واحدة. يفيد في وصف قواعد قبول تسلسل ترويسات.

**Worked example:** A DFA has states S={s₀,s₁,s_f,s_d}, alphabet Σ={IPv6,TCP,other}, start state s₀, and accepting set F={s_f}. Its defined transitions are δ(s₀,IPv6)=s₁, δ(s₁,TCP)=s_f; every other transition goes to s_d, which loops on all symbols. Write its tuple H.
{.keep-next}

**Solution:**
{.keep-next}

$$ H=(\{s_0,s_1,s_f,s_d\},\{IPv6,TCP,other\},\delta,s_0,\{s_f\}) $$

### 38. شرط قبول سلسلة من المحلل (DFA String-Acceptance Condition)

$$x\text{ مقبولة}\iff\delta(s_0,x)\in F$$

**الرموز:** `x` تسلسل الترويسات؛ `δ(s₀,x)` الحالة بعد معالجة التسلسل من البداية؛ `F` الحالات النهائية المسموح بها؛ `⇔` شرط لازم وكافٍ.

**الفكرة ومتى تظهر:** يحدد هل تسلسل المدخل صالح وفق آلة DFA. الناتج قبول أو رفض، وليس رقماً.

**Worked example:** The parser ends in final state s_f after reading the sequence IPv6, TCP.
{.keep-next}

**Solution:**
{.keep-next}

$$ \delta(s_0,[IPv6,TCP])=s_f\in F\quad\Rightarrow\quad\text{accepted} $$

### 39. عامل تضخيم الانعكاس (Reflection Amplification Factor)

$$A=\frac{response\ bytes}{request\ bytes}$$

**الرموز:** `response bytes` حجم الرد؛ `request bytes` حجم الطلب؛ `A` عدد مرات التضخيم. يجب استعمال وحدة حجم واحدة للطرفين.

**الفكرة ومتى تظهر:** يقيس كم مرة يصبح الرد أكبر من الطلب في خدمة عاكسة. الناتج نسبة بلا وحدة.

**Worked example:** A reflector sends a 40 KB response to a 1 KB request.
{.keep-next}

**Solution:**
{.keep-next}

$$ A=\frac{40\text{ KB}}{1\text{ KB}}=40 $$

### 40. معدل الحركة التي تصل إلى الضحية في هجوم انعكاس (Victim Bandwidth in Reflection Attacks)

$$Bandwidth_{victim}\approx A\sum_{j=1}^{m}r_j$$

**الرموز:** `A` عامل التضخيم؛ `r_j` معدل الطلب إلى العاكس `j`؛ `m` عدد العواكس؛ `Bandwidth_victim` معدل الردود التقريبي نحو الضحية.

**الفكرة ومتى تظهر:** تقدّر الحركة الناتجة إذا أعطى السؤال معدلات الطلب والتضخيم. الناتج معدل بيانات؛ طابق وحدة `r_j` مع الوحدة المطلوبة.

**Worked example:** The amplification factor is 40 and the combined request rate is 100 KB/s.
{.keep-next}

**Solution:**
{.keep-next}

$$ Bandwidth_{victim}\approx40\times100=4{,}000\text{ KB/s} $$

### 41. احتمال تخمين DNS في محاولة واحدة (Single-Attempt DNS Guessing Probability)

$$p=2^{-32}$$

**الرموز:** `p` نجاح محاولة واحدة في النموذج؛ `32` بتاً عشوائياً مفترضاً (16 للمعرّف و16 للمنفذ في المثال الوارد).

**الفكرة ومتى تظهر:** احتمال تخمين قيمة واحدة من `2^32` قيمة متساوية الاحتمال. الناتج صغير جداً، مع اعتماد النتيجة على افتراضات العشوائية وعدم معرفة الحقول.

**Worked example:** A DNS guess is chosen uniformly from a space of 2³² possibilities. Find the probability of success on one guess.
{.keep-next}

**Solution:**
{.keep-next}

$$ p=2^{-32}=\frac{1}{4{,}294{,}967{,}296}\approx2.3283\times10^{-10} $$

### 42. احتمال نجاح تخمين DNS بعد m محاولات (DNS Guessing Success over m Attempts)

$$P(success)=1-(1-p)^m$$

**الرموز:** `p` نجاح المحاولة الواحدة؛ `m` عدد المحاولات؛ `(1−p)^m` احتمال فشل كل المحاولات؛ الناتج احتمال نجاح واحدة على الأقل.

**الفكرة ومتى تظهر:** استخدمها عندما تكون المحاولات مستقلة واحتمال كل واحدة ثابتاً. الناتج احتمال تراكمي.

**Worked example:** A single-attempt success probability is 0.01. Estimate success after 10 independent attempts.
{.keep-next}

**Solution:**
{.keep-next}

$$ P(success)=1-(1-0.01)^{10}\approx0.0956=9.56\% $$

### 43. الخطر المتبقي بعد فعالية الضوابط (Residual Network Risk after Controls)

$$R_{net}=\sum_i(1-e_i)P_iI_i$$

**الرموز:** `P_i` احتمال التهديد؛ `I_i` أثره؛ `e_i` فعالية الضابط من 0 إلى 1 في النموذج؛ `1−e_i` الجزء الذي يبقى؛ `R_net` مجموع الخطر المتبقي.

**الفكرة ومتى تظهر:** تستخدم عندما يطلب السؤال أثر ضابط على مخاطر متعددة. نخفض كل مساهمة بنسبة فعاليتها ثم نجمع.

**Worked example:** A threat has P=0.2 and impact I=100; its control effectiveness is e=0.5.
{.keep-next}

**Solution:**
{.keep-next}

$$ R_{net}=(1-0.5)(0.2)(100)=10 $$

### 44. احتمال نجاح اختطاف مسار في نموذج التبني (BGP Route-Hijack Success Probability)

$$P_{hijack}\approx(1-f)^L$$

**الرموز:** `f` نسبة المسارات المغطاة بالتحقق؛ `L` عدد الأنظمة/المراحل المستقلة على المسار في النموذج؛ `1−f` الجزء غير المغطى.

**الفكرة ومتى تظهر:** يوضح كيف أن زيادة التغطية تقلل احتمال المرور عبر كل المراحل غير المغطاة، وفق افتراضات النموذج. الناتج احتمال تقريبي.

**Worked example:** Along a four-hop route, each hop independently has adoption fraction f=0.5. Use the course model to find the probability that the route has no adopted hop.
{.keep-next}

**Solution:**
{.keep-next}

$$ P_{hijack}\approx(1-0.5)^4=0.5^4=0.0625=6.25\% $$

### 45. متوسط الحالات المتزامنة (Expected Concurrent States)

$$N_{concurrent}\approx\frac{\lambda}{\mu}$$

**الرموز:** `λ` معدل وصول الحالات في الثانية؛ `μ` معدل خدمتها في الثانية؛ `N_concurrent` مقياس الحالات المتزامنة المتوقع في النموذج المبسط.

**الفكرة ومتى تظهر:** تقارن حمل الوصول بسرعة المعالجة. الناتج عدد تقريبي للحالات المتزامنة وفق صياغة المذكرة.

**Worked example:** The arrival rate is 120 states per second and the service rate is 10 per second.
{.keep-next}

**Solution:**
{.keep-next}

$$ N_{concurrent}\approx\frac{120}{10}=12 $$

### 46. شرط تشبع سعة الحالة (State-Capacity Saturation Condition)

$$\frac{\lambda}{\mu}\ge M\Rightarrow\text{saturation}$$

**الرموز:** `λ/μ` نسبة الحمل؛ `M` سعة إدارة الحالات؛ `≥` يعني بلوغ السعة أو تجاوزها؛ `saturation` تشبع النظام.

**الفكرة ومتى تظهر:** بعد حساب نسبة الحالات، قارنها بسعة النظام. الناتج حكم تشغيلي: هل يقترب/يصل النموذج إلى التشبع.

**Worked example:** The arrival-to-service ratio is 12 and the state capacity is M=10.
{.keep-next}

**Solution:**
{.keep-next}

$$ \frac{\lambda}{\mu}=12\ge10=M\quad\Rightarrow\quad\text{saturation} $$

### 47. عدد المحاولات المتوقع عند H bits من العشوائية (Expected Guess Count from H-bit Entropy)

$$E[N]\approx2^{H-1}$$

**الرموز:** `E[N]` متوسط المحاولات؛ `H` مقدار الإنتروبيا بالبت؛ `2^H` فضاء الاحتمالات؛ عامل `1/2` يمثل متوسط البحث في الفضاء.

**الفكرة ومتى تظهر:** تقدير متوسط البحث عن قيمة مخفية بافتراض ترتيب/توزيع مناسب. الناتج عدد محاولات.

**Worked example:** A random secret has H=8 bits of entropy.
{.keep-next}

**Solution:**
{.keep-next}

$$ E[N]\approx2^{8-1}=128\text{ guesses} $$

### 48. تجاوز طبقات دفاع مستقلة (Independent Defense-Layer Bypass Probability)

$$P_{success}=\prod_{i=1}^{n}q_i$$

**الرموز:** `q_i` احتمال فشل/تجاوز الطبقة `i`؛ `n` عدد الطبقات؛ `Π` ضرب احتمالات جميع الطبقات.

**الفكرة ومتى تظهر:** إذا كان لا بد من تجاوز كل طبقة وكانت الأحداث مستقلة، احتمال المرور الكلي هو حاصل الضرب. الناتج احتمال مركب.

**Worked example:** Two independent defense layers each have a 0.2 probability of being bypassed.
{.keep-next}

**Solution:**
{.keep-next}

$$ P_{success}=0.2\times0.2=0.04=4\% $$

### 49. توافر القرار مع أخطاء السماح والمنع (Decision Availability after Allow/Deny Errors)

$$A=1-(P_{allow}+P_{deny})$$

**الرموز:** `P_allow` احتمال السماح لحركة خبيثة؛ `P_deny` احتمال منع حركة سليمة؛ `A` مؤشر التوفر/جودة القرار كما في نموذج المذكرة.

**الفكرة ومتى تظهر:** إذا أعطى السؤال احتمالي الخطأين وطلب المؤشر. الناتج يتناقص عندما تكبر الأخطاء؛ لا تخلط `A` هنا بتوفر الخدمة في الفصل 6.

**Worked example:** Assume allow-error and deny-error events are disjoint. Their probabilities are 0.02 and 0.03. Find the accuracy using the course expression.
{.keep-next}

**Solution:**
{.keep-next}

$$ A=1-(0.02+0.03)=0.95=95\% $$

### 50. الخطر الموزون لأخطاء السماح والمنع (Weighted Risk of Allow/Deny Errors)

$$R=q_mP_{allow}I_m+q_bP_{deny}I_b$$

**الرموز:** `q_m,q_b` أوزان/احتمالات المكوّنين وفق تعريف المذكرة؛ `P_allow` خطأ السماح؛ `I_m` أثره؛ `P_deny` خطأ المنع؛ `I_b` أثره؛ `R` الخطر الناتج.

**الفكرة ومتى تظهر:** تقارن أثر نوعَي الخطأ بعد وزن احتمال كل منهما وشدته. الناتج قيمة خطر على مقياس النموذج.

**Worked example:** The weighted allow-error contribution is 0.02×10, and the deny-error contribution is 0.03×5.
{.keep-next}

**Solution:**
{.keep-next}

$$ R=(0.02)(10)+(0.03)(5)=0.20+0.15=0.35 $$

### 51. نسبة إصابة الذاكرة المخبأة (Cache Hit Ratio)

$$CHR=\frac{H}{N}$$

**الرموز:** `CHR` Cache Hit Ratio؛ `H` عدد الطلبات التي وجدت محتواها في الذاكرة المخبأة؛ `N` عدد الطلبات الكلي.

**الفكرة ومتى تظهر:** تقيس نسبة الطلبات التي خُدمت من Cache. الناتج نسبة من 0 إلى 1 أو مئوية.

**Worked example:** The cache serves 80 hits from 100 requests.
{.keep-next}

**Solution:**
{.keep-next}

$$ CHR=\frac{80}{100}=0.8=80\% $$

### 52. فرق زمن الاستجابة بين المصدر وCache (Cache Latency Savings per Hit)

$$\Delta L=L_{origin}-L_{cache}$$

**الرموز:** `ΔL` زمن التأخير الذي توفره إصابة واحدة؛ `L_origin` زمن جلب المحتوى من المصدر؛ `L_cache` زمن جلبه من الذاكرة المخبأة.

**الفكرة ومتى تظهر:** تستخدم عندما يسأل السؤال كم زمناً وفّرته كل إصابة. الناتج فرق زمن، مثل millisecond، وليس المتوسط بحد ذاته.

**Worked example:** The origin responds in 5 ms and the cache responds in 1 ms.
{.keep-next}

**Solution:**
{.keep-next}

$$ \Delta L=5-1=4\text{ ms per hit} $$

### 53. مجموع زمن الاستجابة الموفر (Total Cache Latency Saved)

$$L_{saved}=H(L_{origin}-L_{cache})$$

**الرموز:** `H` عدد الإصابات؛ `L_origin−L_cache` التوفير لكل إصابة؛ `L_saved` مجموع الزمن الموفر.

**الفكرة ومتى تظهر:** تستخدم بعد معرفة عدد الإصابات وفرق الزمن. الناتج زمن إجمالي موفر عبر الطلبات المحتسبة.

**Worked example:** There are 80 cache hits, each saving 4 ms.
{.keep-next}

**Solution:**
{.keep-next}

$$ L_{saved}=80(4\text{ ms})=320\text{ ms} $$

### 54. التعرض بعد ضابط وقائي (Exposure Probability after a Preventive Control)

$$P_{exp}=(1-e_p)P'_{exp}$$

**الرموز:** `P'_exp` الاحتمال قبل الضابط وفق ترميز المذكرة؛ `e_p` فعالية الضابط الوقائي؛ `P_exp` التعرض بعد الضابط.

**الفكرة ومتى تظهر:** احسب الجزء الذي لم يمنعه الضابط. تحقّق من تعريف الشرطة العليا في السؤال؛ هنا اعتبرناها القيمة السابقة للضابط كما في شرح المصدر.

**Worked example:** Before a preventive control, exposure probability is P′ₑₓₚ=0.2. The control effectiveness is eₚ=0.5. Find the post-control exposure probability Pₑₓₚ.
{.keep-next}

**Solution:**
{.keep-next}

$$ P_{exp}=(1-0.5)(0.2)=0.1 $$

### 55. احتمال الاعتراض بعد VPN (Interception Probability after VPN Protection)

$$P'_{int}=(1-e_{vpn})P_{int}$$

**الرموز:** `P_int` احتمال الاعتراض قبل أثر الضابط في ترميز المذكرة؛ `e_vpn` فعالية حماية VPN؛ `P'_int` الاحتمال بعد الضابط.

**الفكرة ومتى تظهر:** صيغة تخفيض بالمكمّل؛ الناتج احتمال متبقٍ في نموذج الفصل. لا تستنتج فعالية واقعية ثابتة من اسم التقنية وحده.

**Worked example:** The original interception probability is 0.1 and VPN effectiveness is 0.8.
{.keep-next}

**Solution:**
{.keep-next}

$$ P\prime_{int}=(1-0.8)(0.1)=0.02 $$

### 56. زمن الاتصال مع كلفة VPN (VPN-Adjusted Connection Time)

$$T_{vpn}=T_0+O_{enc}$$

**الرموز:** `T_0` زمن الاتصال الأساسي؛ `O_enc` الزمن الإضافي الناتج من التشفير؛ `T_vpn` الزمن الكلي في النموذج.

**الفكرة ومتى تظهر:** عند مقارنة زمن اتصال قبل VPN وبعد إضافة كلفة التشفير. الناتج زمن، لذلك يجب توحيد الوحدات.

**Worked example:** A connection takes T_0=10 ms, and VPN encryption adds O_enc=2 ms.
{.keep-next}

**Solution:**
{.keep-next}

$$ T_{vpn}=10+2=12\text{ ms} $$

### 57. خطر متبقٍ بعد ضابط واحد (Residual Risk after One Control)

$$R_{res}=R_0(1-e)$$

**الرموز:** `R_0` الخطر قبل الضابط؛ `e` فعالية الضابط بين 0 و1؛ `R_res` المتبقي.

**الفكرة ومتى تظهر:** عندما يكون هناك ضابط واحد وفعاليته معروفة. نضرب الخطر بالجزء الذي لم يزل.

**Worked example:** Initial risk is 100 and one control has effectiveness e=0.8.
{.keep-next}

**Solution:**
{.keep-next}

$$ R_{res}=100(1-0.8)=20 $$

### 58. خطر متبقٍ بعد ضوابط مستقلة متعددة (Residual Risk after Independent Multiple Controls)

$$R_{residual}=R_0\prod_i(1-e_i)$$

**الرموز:** `R_0` الخطر الابتدائي؛ `e_i` فعالية الضابط `i`؛ `Π` ضرب أجزاء الخطر المتبقية؛ `R_residual` الخطر بعد كل الضوابط.

**الفكرة ومتى تظهر:** عندما تفترض المسألة استقلال أثر الضوابط وتطبيقها بالتتابع. الناتج يتناقص مع كل طبقة فعالة.

**Worked example:** Initial risk is 100; two independent controls each reduce the remaining risk by 50%.
{.keep-next}

**Solution:**
{.keep-next}

$$ R_{residual}=100(1-0.5)(1-0.5)=25 $$

### 59. حاصل فعالية مكونات دفاعية (Combined Defensive-Component Effectiveness)

$$a_{total}=a_fa_pa_v$$

**الرموز:** `a_f,a_p,a_v` عوامل فعالية المكونات التي سمتها المذكرة؛ `a_total` الناتج المركب. المقصود الدقيق لكل حرف يتبع تعريف المصدر.

**الفكرة ومتى تظهر:** تستخدم إذا أعطى السؤال قيم هذه العوامل وافترض تركيبها بالضرب. الناتج مؤشر مركب، وليس نسبة نجاح عامة من دون مقياس.

**Worked example:** In the course model, the combined score is the product of three component scores a_f=0.9, a_p=0.8, and a_v=0.5. Find a_total.
{.keep-next}

**Solution:**
{.keep-next}

$$ a_{total}=0.9\times0.8\times0.5=0.36 $$

### 60. منفعة القرار الأمني (Security Decision Utility)

$$U=\alpha S+\beta P-\gamma C$$

**الرموز:** `S` درجة الأمن؛ `P` درجة الخصوصية؛ `C` الكلفة؛ `α,β,γ` أوزان الأهمية؛ `U` المنفعة الصافية على المقياس المحدد.

**الفكرة ومتى تظهر:** تقارن بدائل عندما تكسب أمنًا وخصوصية لكن تتحمل كلفة. الأوزان تجعل الوحدات/الأهمية قابلة للموازنة وفق السؤال.

**Worked example:** Let S=8, P=6, C=4, and weights α=1, β=1, γ=0.5.
{.keep-next}

**Solution:**
{.keep-next}

$$ U=1(8)+1(6)-0.5(4)=12 $$

### 61. كشف نمط معروف بالتوقيع (Signature-Based Detection Rule)

$$D(m_i)=\begin{cases}1&\text{إذا طابق }m_i\text{ توقيعاً }s_j\\0&\text{خلاف ذلك}\end{cases}$$

**الرموز:** `m_i` رسالة/حركة مفحوصة؛ `s_j` توقيع هجوم معروف؛ `D` دالة الكشف؛ `1` تطابق؛ `0` عدم تطابق.

**الفكرة ومتى تظهر:** قاعدة قرار ثنائية للكشف بالتواقيع. الناتج 1 أو 0؛ عدم التطابق لا يثبت وحده أن الحركة سليمة، فقد يكون الهجوم جديداً.

**Worked example:** A message m_i contains a signature pattern s_j from the rule set.
{.keep-next}

**Solution:**
{.keep-next}

$$ D(m_i)=1\quad\text{(signature match)} $$

### 62. كشف شذوذ عن المتوسط (Mean-Deviation Anomaly Detection Rule)

$$A(x)=\begin{cases}1&|x-\mu|>k\sigma\\0&\text{خلاف ذلك}\end{cases}$$

**الرموز:** `x` القياس الحالي؛ `μ` المتوسط؛ `σ` الانحراف المعياري؛ `k` عدد الانحرافات المسموح بها؛ `A(x)` قرار التنبيه.

**الفكرة ومتى تظهر:** تنبه إذا ابتعد القياس عن المتوسط بأكثر من العتبة `kσ`. الناتج ثنائي ويتأثر باختيار العتبة.

**Worked example:** Let μ=10, σ=2, k=3, and x=17. Compare the deviation with the threshold.
{.keep-next}

**Solution:**
{.keep-next}

$$ |17-10|=7>3(2)=6\quad\Rightarrow\quad A(x)=1 $$

### 63. فضاء مصنف الحركة (Traffic-Classifier Mapping)

$$f:\mathbb{R}^{d}\to\{benign,malicious\}$$

**الرموز:** `f` المصنف؛ `R^d` متجه من `d` ميزات رقمية؛ `benign` حركة سليمة؛ `malicious` حركة خبيثة.

**الفكرة ومتى تظهر:** تصف شكل مدخل ومخرج نظام تصنيف. لا تنتج دقة وحدها؛ تحتاج نموذجاً وبيانات وتقييماً.

**Worked example:** A classifier is defined as f: Rᵈ → {benign, malicious}. What labels can it return?
{.keep-next}

**Solution:**
{.keep-next}

$$ f(x)\in\{benign,malicious\} $$

### 64. هدف تدريب المصنف (Classifier Training Objective)

$$\min_f\mathbb{E}[L(f(\mathbf{x}),\mathcal{Y})]$$

**الرموز:** `f` المصنف المراد اختياره؛ `x` متجه الميزات؛ `Y` التصنيف الصحيح؛ `L` كلفة/خسارة الخطأ؛ `E` المتوسط المتوقع على البيانات.

**الفكرة ومتى تظهر:** تصوغ التدريب كاختيار نموذج يقلل متوسط كلفة التنبؤات الخاطئة. الناتج نموذج أمثل وفق دالة الخسارة والبيانات، لا ضمان كمال.

**Worked example:** On the same validation data, model f_1 has mean loss 0.2 and model f_2 has mean loss 0.3.
{.keep-next}

**Solution:**
{.keep-next}

$$ \mathbb{E}[L(f_1(\mathbf{x}),\mathcal{Y})]=0.2<0.3=\mathbb{E}[L(f_2(\mathbf{x}),\mathcal{Y})] $$

### 65. معدل الكشف الحقيقي (True Positive Rate)

$$TPR=\frac{TP}{TP+FN}$$

**الرموز:** `TP` هجمات كُشفت صحيحاً؛ `FN` هجمات لم تُكتشف؛ `TP+FN` كل الهجمات الفعلية.

**الفكرة ومتى تظهر:** يقيس نسبة الهجمات المكتشفة من مجموع الهجمات. الناتج نسبة؛ ارتفاعه يقلل الهجمات الفائتة.

**Worked example:** The detector finds 90 positive cases and misses 10 positive cases.
{.keep-next}

**Solution:**
{.keep-next}

$$ TPR=\frac{90}{90+10}=0.90=90\% $$

### 66. معدل الإنذار الكاذب (False Positive Rate)

$$FPR=\frac{FP}{FP+TN}$$

**الرموز:** `FP` حالات سليمة صُنفت هجوماً؛ `TN` حالات سليمة صُنفت سليمة؛ المقام جميع الحالات السليمة.

**الفكرة ومتى تظهر:** يقيس نسبة الإنذارات الخاطئة بين الحالات السليمة. الناتج نسبة؛ انخفاضه يقلل الإزعاج والحجب الخاطئ.

**Worked example:** Among 100 actual-negative cases, the detector raises 5 false alarms and correctly rejects 95. Find the false-positive rate.
{.keep-next}

**Solution:**
{.keep-next}

$$ FPR=\frac{FP}{FP+TN}=\frac{5}{5+95}=0.05=5\% $$

### 67. مؤشر SEI كما ورد في المذكرة (SEI (Source-Defined Detection Effectiveness Index))

$$SEI=\frac{P_{TP}}{P_{TP}+P_{FN}+P_{FP}}$$

**الرموز:** `P_TP` وزن/احتمال حالة الاكتشاف الصحيح؛ `P_FN` الفوات؛ `P_FP` الإنذار الكاذب؛ `SEI` المؤشر الذي تسميه المذكرة.

**الفكرة ومتى تظهر:** احسبه فقط عندما يحدد السؤال هذه القيم وتعريفها. لا تخلطه بمقياس آخر له اختصار مشابه؛ الناتج مؤشر بحسب تعريف المصدر.

**Worked example:** The source-defined SEI inputs are P_TP=0.8, P_FN=0.1, and P_FP=0.1.
{.keep-next}

**Solution:**
{.keep-next}

$$ SEI=\frac{0.8}{0.8+0.1+0.1}=0.8 $$

### 68. احتمال الهجوم بعد وصول تنبيه (Posterior Attack Probability (Bayes’ Rule))

$$P(A|D)=\frac{P(D|A)P(A)}{P(D|A)P(A)+P(D|\neg A)P(\neg A)}$$

**الرموز:** `A` وقوع هجوم؛ `D` صدور تنبيه؛ `P(A)` الاحتمال القبلي للهجوم؛ `P(D|A)` احتمال التنبيه إذا وقع هجوم؛ `P(D|¬A)` احتمال الإنذار الكاذب؛ `P(A|D)` احتمال الهجوم بعد رؤية التنبيه.

**الفكرة ومتى تظهر:** عندما يطلب السؤال تفسير دقة التنبيه مع مراعاة ندرة الهجوم. الناتج احتمال شرطي بعد تحديث الاعتقاد.

**Worked example:** An attack has prior probability 1%; detector sensitivity is 90%, and its false-positive rate is 5%. Find the attack probability after a positive alert.
{.keep-next}

**Solution:**
{.keep-next}

$$ P(A\mid D)=\frac{0.90(0.01)}{0.90(0.01)+0.05(0.99)}\approx0.1538=15.38\% $$

### 69. نموذج خليط Gaussian لميزات الحركة (Gaussian Mixture Model for Traffic Features)

$$p(\mathbf f)=\sum_{k=1}^{K}\pi_k\mathcal{N}(\mathbf f|\mu_k,\Sigma_k)$$

**الرموز:** `f` متجه الميزات؛ `K` عدد المكونات؛ `π_k` وزن المكون ومجموع الأوزان 1؛ `N` توزيع Gaussian؛ `μ_k` متوسطه؛ `Σ_k` مصفوفة تباينه؛ `p(f)` كثافة الميزات.

**الفكرة ومتى تظهر:** تمثيل بيانات الحركة كمزيج مجموعات إحصائية. الناتج كثافة/درجة ملاءمة للبيانات، وليس مباشرة فئة هجوم دون قاعدة قرار إضافية.

**Worked example:** For a one-dimensional Gaussian mixture, π₁=0.6 with N(0,1), π₂=0.4 with N(1,1), and the observed feature is f=0. Find p(f), using unit variance for both components.
{.keep-next}

**Solution:**
{.keep-next}

$$ p(0)=0.6\,\mathcal N(0\mid0,1)+0.4\,\mathcal N(0\mid1,1)\approx0.6(0.39894)+0.4(0.24197)=0.33615 $$

### 70. درجة ترابط أدلة SIEM الموزونة (Weighted SIEM Evidence Correlation Score)

$$C(E)=\sum_iw_ie_i$$

**الرموز:** `e_i` درجة الدليل الأمني `i` القادم من IDS/IPS؛ `w_i` وزن مساهمته في الترابط؛ `C(E)` مجموع درجات الأدلة الموزونة كما يعرّفها المصدر. هذه الصيغة مجموع موزون وليست متوسطاً.

**الفكرة ومتى تظهر:** تجمع إشارات IDS/IPS بأوزانها ضمن SIEM لإنتاج درجة ترابط. الناتج درجة ترابط؛ ولا يحدد وحده وجود حادث ما لم توجد عتبة قرار.

**Worked example:** A SIEM combines two IDS/IPS evidence scores e₁=0.8 and e₂=0.5 with correlation weights w₁=3 and w₂=1. Find the correlation score C(E).
{.keep-next}

**Solution:**
{.keep-next}

$$ C(E)=3(0.8)+1(0.5)=2.9 $$

### 71. توافر IDS وIPS معاً (Joint IDS/IPS Availability)

$$A_{eff}=A_{ids}A_{ips}$$

**الرموز:** `A_ids` توافر IDS؛ `A_ips` توافر IPS؛ `A_eff` توافرهما معاً في نموذج يتطلب عمل الاثنين.

**الفكرة ومتى تظهر:** حاصل الضرب مناسب إذا كان توقف أي واحد يعطل الوظيفة المطلوبة وافترض الاستقلال. الناتج احتمال التوفر المشترك.

**Worked example:** An IDS and IPS are both required for the system to operate, and their availabilities are independent: A_ids=0.99 and A_ips=0.98. Find series availability.
{.keep-next}

**Solution:**
{.keep-next}

$$ A_{eff}=0.99\times0.98=0.9702=97.02\% $$

### 72. الخسارة المتوقعة مع الكشف والمنع (Expected Loss after Detection and Prevention)

$$EL=P_a(1-P_dP_p)I$$

**الرموز:** `P_a` احتمال الهجوم؛ `P_d` فعالية الكشف؛ `P_p` فعالية المنع وفق صيغة المصدر؛ `I` أثر الخسارة؛ `EL` الخسارة المتوقعة.

**الفكرة ومتى تظهر:** تقدّر الأثر المتبقي بعد طبقتي الكشف والمنع كما يصوغهما نموذج المذكرة. اقرأ ترتيب الأقواس كما هو؛ لا تستبدل الصيغة بتفسير مختلف دون سند.

**Worked example:** In the course model, the combined mitigation term is P_dP_p. Let P_a=0.1, P_d=0.8, P_p=0.5, and I=100. Find expected loss EL.
{.keep-next}

**Solution:**
{.keep-next}

$$ EL=0.1(1-0.8\times0.5)100=6 $$

### 73. مؤشر الوصول بين عقدتين (Path-to-Edge Reachability Index)

$$P_{reach}=\frac{|P(v_i,v_t)|}{|E|}$$

**الرموز:** `v_i` نقطة البداية؛ `v_t` الهدف؛ `P(v_i,v_t)` مجموعة/عدد المسارات بينهما كما عرّف النموذج؛ `E` مجموعة الحواف؛ `|·|` العدد؛ `P_reach` مؤشر الوصول المعرّف في المادة كنسبة عدد المسارات إلى عدد الحواف.

**الفكرة ومتى تظهر:** مقياس نسبي مبسط لمسارات الوصول قبل التقسيم. لأن تفسير عدد المسارات ونطاق الحواف يعتمد على المصدر، استخدم تعريف المسألة عند حسابه.

**Worked example:** Using the course-defined path-to-edge reachability index, the counted attack-path total is 4 and the graph has 20 edges. Find the index value.
{.keep-next}

**Solution:**
{.keep-next}

$$ P_{reach}\text{ (course-defined index)}=\frac{4}{20}=0.2 $$

### 74. مؤشر الوصول بعد التقسيم (Segmented Reachability Index)

$$P_{reach}^{seg}=\frac{|P(v_i,v_t)\cap C|}{|E|}$$

**الرموز:** `C` مجموعة المسارات/العناصر التي يسمح بها نطاق التقسيم وفق المذكرة؛ التقاطع `∩` يأخذ المسارات المشتركة مع النطاق؛ وباقي الرموز كما في الصيغة السابقة.

**الفكرة ومتى تظهر:** تقارن الوصول بعد فرض التقسيم. انخفاض المؤشر يعني أن المسارات المتاحة ضمن الحد أصبحت أقل وفق تعريف النموذج.

**Worked example:** Using the course-defined segmented path-to-edge index, 2 counted paths remain after segmentation and the graph has 20 edges. Find the index value.
{.keep-next}

**Solution:**
{.keep-next}

$$ P_{reach}^{seg}\text{ (course-defined index)}=\frac{2}{20}=0.1 $$

### 75. خطر عنصر شبكي (Individual Network-Element Risk)

$$R_i=P_iV_i$$

**الرموز:** `P_i` احتمال التهديد/الوصول للعنصر `i`؛ `V_i` قيمة أثره/ضعفه وفق تعريف الفصل؛ `R_i` مساهمة العنصر في الخطر.

**الفكرة ومتى تظهر:** تحسب مساهمة عنصر واحد قبل جمع عناصر الشبكة. الناتج درجة خطر على مقياس المدخلات.

**Worked example:** A network element has P_i=0.2 and V_i=10.
{.keep-next}

**Solution:**
{.keep-next}

$$ R_i=0.2\times10=2 $$

### 76. مجموع مخاطر الشبكة (Total Network Risk)

$$R_{net}=\sum_iR_i$$

**الرموز:** `R_i` خطر العنصر `i`؛ `i` يتكرر على العناصر؛ `R_net` مجموعها.

**الفكرة ومتى تظهر:** بعد حساب المخاطر الفردية، اجمعها للحصول على المؤشر الكلي وفق افتراض الجمع.

**Worked example:** Three network elements have risk scores 2, 3, and 1.
{.keep-next}

**Solution:**
{.keep-next}

$$ R_{net}=2+3+1=6 $$

### 77. الخطر الشبكي المعدل بعامل فعالية (Effectiveness-Adjusted Network Risk)

$$R_{eff}=\alpha R_{net}$$

**الرموز:** `R_net` مجموع خطر الشبكة؛ `α` عامل الفعالية/التعديل كما عرفه المصدر؛ `R_eff` الخطر المعدل.

**الفكرة ومتى تظهر:** تضرب المجموع بعامل يحدد أثر النموذج. تحقّق هل `α` يمثل بقاء الخطر أو نسبة الخطر قبل التعويض، لأن المعنى يعتمد على تعريف المصدر.

**Worked example:** The total network risk is 10 and the adjustment factor is α=0.4.
{.keep-next}

**Solution:**
{.keep-next}

$$ R_{eff}=0.4(10)=4 $$

### 78. نسبة الاتصالات الممنوعة بالتقسيم الدقيق (Microsegmentation Blocking Rate)

$$E_{micro}=\frac{N-N_{allowed}}{N}$$

**الرموز:** `N` كل الاتصالات/المسارات المفحوصة؛ `N_allowed` ما سُمح به؛ `N−N_allowed` ما مُنع؛ `E_micro` نسبة المنع.

**الفكرة ومتى تظهر:** تقيس نسبة الاتصالات غير المسموح بها. الناتج نسبة من الكل.

**Worked example:** Microsegmentation allows 20 of 100 connections and blocks the rest.
{.keep-next}

**Solution:**
{.keep-next}

$$ E_{micro}=\frac{100-20}{100}=0.8=80\% $$

### 79. التوزيع المستقر في سلسلة Markov (Stationary Distribution of a Markov Chain)

$$\boldsymbol{\pi}=\boldsymbol{\pi}P$$

**الرموز:** `π` متجه احتمالات الحالات المستقرة؛ `P` مصفوفة انتقال الحالات؛ الضرب يترك التوزيع كما هو بعد انتقال واحد.

**الفكرة ومتى تظهر:** تبحث عن توزيع لا يتغير بعد تطبيق مصفوفة الانتقال. الناتج متجه احتمالات مستقر.

**Worked example:** For P=[[0.8,0.2],[7/15,8/15]], test whether π=(0.7,0.3) is stationary.
{.keep-next}

**Solution:**
{.keep-next}

$$ \boldsymbol{\pi}P=(0.7,0.3)P=(0.7,0.3)=\boldsymbol{\pi} $$

### 80. مجموع احتمالات التوزيع (Probability Normalization Condition)

$$\sum_j\pi_j=1$$

**الرموز:** `π_j` احتمال الحالة `j`؛ `j` كل الحالات الممكنة؛ مجموع الاحتمالات يساوي 1.

**الفكرة ومتى تظهر:** شرط تحقق للتوزيع الاحتمالي، ويستخدم لتطبيع متجه Markov.

**Worked example:** A distribution has state probabilities 0.7 and 0.3.
{.keep-next}

**Solution:**
{.keep-next}

$$ \sum_j\pi_j=0.7+0.3=1 $$

### 81. عائد الاستثمار الأمني (Return on Security Investment (ROSI))

$$ROSI=\frac{\Delta L-C_s}{C_s}$$

**الرموز:** `ΔL` الخسارة المتجنبة/المخفضة؛ `C_s` كلفة الحل الأمني؛ `ROSI` عائد الاستثمار الأمني النسبي.

**الفكرة ومتى تظهر:** تقارن المنفعة المالية المتجنبة بكلفة الضابط. الناتج نسبة؛ قيمة موجبة تعني أن المنفعة المقدرة أعلى من الكلفة وفق افتراض النموذج.

**Worked example:** The security investment prevents 4 units of loss and costs 2 units.
{.keep-next}

**Solution:**
{.keep-next}

$$ ROSI=\frac{4-2}{2}=1=100\% $$

### 82. تعظيم مقدار الخطر المخفّض (Maximum Risk Reduction)

$$\max(R_0-R_{residual})=R_0\left(1-\prod_i(1-r_i)\right)$$

**الرموز:** `R_0` الخطر الأولي؛ `R_residual` المتبقي؛ `r_i` مقدار التخفيض المنسوب للضابط `i` في هذا النموذج؛ الضرب يجمع الأجزاء المتبقية؛ `max` يعني اختيار البديل الأفضل.

**الفكرة ومتى تظهر:** هدف تحسين لا عملية حساب منفردة: اختر الضوابط التي تزيد الخطر المخفّض ضمن القيود.

**Worked example:** The only available control plan contains two independent controls, each reducing the remaining risk by 50%. Initial risk is 100. Find the maximum reduction over the available plan set.
{.keep-next}

**Solution:**
{.keep-next}

$$ \max(R_0-R_{residual})=100\left[1-(1-0.5)^2\right]=75\text{ risk units} $$

### 83. قيد ميزانية الضوابط (Security-Control Budget Constraint)

$$\sum_i c_i\le B$$

**الرموز:** `c_i` كلفة الضابط `i`؛ `B` الميزانية الكلية؛ `Σ` مجموع تكاليف الضوابط المختارة؛ `≤` لا تتجاوز.

**الفكرة ومتى تظهر:** شرط يقيّد مسألة الاختيار/التحسين. الناتج فحص صلاحية: هل مجموع الإنفاق ضمن الميزانية؟

**Worked example:** Two selected controls cost 3 and 4 units; the available budget is 8 units.
{.keep-next}

**Solution:**
{.keep-next}

$$ \sum_i c_i=3+4=7\le8=B\quad\text{(within budget)} $$

## الفصل 6 — أمن تطبيقات الويب والاستمرارية

### 84. احتمال اختراق كل طبقات الدفاع (Layered Defense Compromise Probability)

$$P_{compromise}=\prod_{i=1}^{n}(1-E_i)$$

**الرموز:** `E_i` فعالية الطبقة `i`؛ `1−E_i` احتمال فشلها في هذا النموذج؛ `n` عدد الطبقات؛ `P_compromise` احتمال اختراقها كلها.

**الفكرة ومتى تظهر:** إذا كان على المهاجم تجاوز كل طبقة وكانت النتائج مستقلة، نضرب احتمالات فشل الطبقات. الناتج احتمال مركب.

**Worked example:** Two independent defense layers each have effectiveness E_i=0.8.
{.keep-next}

**Solution:**
{.keep-next}

$$ P_{compromise}=(1-0.8)^2=0.04=4\% $$

### 85. تغير عدد الثغرات بين دورتين (Vulnerability Count Update per Development Cycle)

$$V_{t+1}=V_t(1-\alpha)+\beta$$

**الرموز:** `V_t` الثغرات الحالية؛ `V_(t+1)` العدد بالدورة التالية؛ `α` نسبة ما أزيل؛ `β` عدد الثغرات الجديدة المضافة.

**الفكرة ومتى تظهر:** تحسب تحديث العدد بعد الإصلاح والإضافات. الناتج ينخفض عندما تكون الإزالة أكبر من الإضافة.

**Worked example:** There are V_t=100 vulnerabilities, a removal rate α=0.2, and β=5 new vulnerabilities.
{.keep-next}

**Solution:**
{.keep-next}

$$ V_{t+1}=100(1-0.2)+5=85 $$

### 86. خطر ثغرة واحدة (Individual Vulnerability Risk)

$$R_i=L_iS_iI_i$$

**الرموز:** `L_i` احتمال/قابلية استغلال الثغرة؛ `S_i` شدتها؛ `I_i` أثرها على النظام؛ `R_i` درجة الخطر للثغرة `i`.

**الفكرة ومتى تظهر:** رتّب الثغرات عندما يعطي السؤال هذه العوامل بمقياس رقمي. الناتج درجة على مقياس النموذج.

**Worked example:** A vulnerability has likelihood L=0.5, severity S=4, and impact I=10.
{.keep-next}

**Solution:**
{.keep-next}

$$ R_i=0.5\times4\times10=20 $$

### 87. مجموع مخاطر الثغرات (Total Vulnerability Risk)

$$R_{total}=\sum_iR_i$$

**الرموز:** `R_i` درجة خطر الثغرة `i`؛ `R_total` مجموع المخاطر المدرجة.

**الفكرة ومتى تظهر:** تجمع المخاطر الفردية إذا افترض السؤال الجمع. الناتج مجموع درجات، وليس احتمالاً إلا إذا عرّف النموذج ذلك.

**Worked example:** Three vulnerabilities have scores 20, 5, and 3.
{.keep-next}

**Solution:**
{.keep-next}

$$ R_{total}=20+5+3=28 $$

### 88. تقليل الخطر المتبقي تحت ميزانية (Budget-Constrained Residual-Risk Minimization)

$$\min R_{residual}=\sum_iR_i(1-M_i)$$

**الرموز:** `R_i` الخطر الابتدائي للعنصر؛ `M_i` فعالية/تخفيف الضابط المقابل؛ `R_residual` مجموع الخطر المتبقي؛ `min` اختيار أقل نتيجة.

**الفكرة ومتى تظهر:** مسألة اختيار ضوابط تقلل المخاطر. لكل عنصر نحسب الجزء غير المخفّض ثم نجمع.

**Worked example:** The only candidate control has effectiveness M=0.6 and acts on a risk score of 100. Find the minimum residual risk over the available candidate set.
{.keep-next}

**Solution:**
{.keep-next}

$$ \min R_{residual}=100(1-0.6)=40\text{ risk units} $$

### 89. تقليل سطح الهجوم (Attack Surface Reduction)

$$ASR=1-\frac{E_{exposed}}{E_{total}}$$

**الرموز:** `E_exposed` نقاط النهاية التي بقيت مكشوفة؛ `E_total` كل نقاط النهاية؛ `ASR` نسبة السطح الذي خُفّض/أزيل تعرّضه.

**الفكرة ومتى تظهر:** تستخدم عندما يقارن السؤال نقاط النهاية المكشوفة بعد المعالجة بإجماليها. الناتج نسبة التخفيض وفق هذا التعريف.

**Worked example:** Five of 20 endpoints remain exposed after mitigation.
{.keep-next}

**Solution:**
{.keep-next}

$$ ASR=1-\frac{5}{20}=0.75=75\% $$

### 90. فعالية WAF مع كلفة الإنذارات الكاذبة (WAF Effectiveness with False-Positive Penalty)

$$E_{WAF}=\frac{TP}{TP+FN}-\lambda\frac{FP}{FP+TN}$$

**الرموز:** `TP` هجمات كُشفت؛ `FN` هجمات فاتت؛ `FP` طلبات سليمة حُجبت؛ `TN` طلبات سليمة مرّت؛ `λ` وزن كلفة الإنذار الكاذب؛ `E_WAF` مؤشر الفعالية المعدل.

**الفكرة ومتى تظهر:** تجمع حساسية الكشف وتطرح عقوبة الإنذارات الخاطئة. الناتج درجة نموذجية تتأثر بوزن `λ`.

**Worked example:** The WAF true-positive rate is 0.9, false-positive rate is 0.1, and penalty weight λ=0.5.
{.keep-next}

**Solution:**
{.keep-next}

$$ E_{WAF}=0.9-0.5(0.1)=0.85 $$

### 91. موثوقية مكوّن حتى الزمن t (Component Reliability over Time)

$$R(t)=e^{-\lambda t}$$

**الرموز:** `R(t)` احتمال بقاء المكوّن عاملاً حتى `t`؛ `λ` معدل الفشل لكل وحدة زمن؛ `e` أساس اللوغاريتم الطبيعي؛ `t` الزمن.

**الفكرة ومتى تظهر:** نموذج موثوقية بزمن فشل أسي ومعدل ثابت. يختلف عن `R(t)` في الفصل 1 الذي يعني مجموع التعرض للخطر؛ اسأل ما المعطيات: معدل فشل وزمن أم احتمالات تهديد وأثر.

**Worked example:** A component has a constant failure rate λ=0.1 per hour and operates for t=10 hours.
{.keep-next}

**Solution:**
{.keep-next}

$$ R(10)=e^{-(0.1)(10)}=e^{-1}\approx0.368 $$

### 92. تقدير كلفة المدافع (Defender Utility)

$$U_{defender}=-(P_AI)-C_D$$

**الرموز:** `P_A` احتمال/عامل الهجوم؛ `I` أثره؛ `C_D` كلفة الدفاع؛ `U_defender` منفعة المدافع بإشارة سالبة للخسارة والكلفة وفق النموذج.

**الفكرة ومتى تظهر:** تمثل المفاضلة بين خسارة الهجوم وكلفة الدفاع. الناتج منفعة/كلفة على مقياس السؤال؛ لا تخلطها بمنفعة CIA.

**Worked example:** The expected attack damage is P_A I=20 units, and defender cost C_D=5 units.
{.keep-next}

**Solution:**
{.keep-next}

$$ U_{defender}=-(20)-5=-25 $$

### 93. تغطية المسارات المراقبة (Monitored-Path Coverage)

$$RC=\frac{Monitored\ Paths}{Total\ Paths}$$

**الرموز:** `Monitored Paths` المسارات التي تراقبها الضوابط؛ `Total Paths` كل المسارات؛ `RC` نسبة التغطية.

**الفكرة ومتى تظهر:** قياس مدى مراقبة طرق التنفيذ/الوصول. الناتج نسبة من 0 إلى 1.

**Worked example:** Eight of 10 execution paths are monitored.
{.keep-next}

**Solution:**
{.keep-next}

$$ RC=\frac{8}{10}=0.8=80\% $$

### 94. نسبة الثغرات المكتشفة (Vulnerability Detection Coverage Factor)

$$ACF=\frac{V_d}{V_a}$$

**الرموز:** `V_d` الثغرات المكتشفة؛ `V_a` الثغرات المتاحة/الموجودة وفق تعريف المصدر؛ `ACF` نسبة التغطية.

**الفكرة ومتى تظهر:** تحسب التغطية إذا عرف السؤال العدد المكتشف والإجمالي. الناتج نسبة؛ لا يساوي بالضرورة فعالية منع الاستغلال.

**Worked example:** A scanner detects 18 of 20 available vulnerabilities.
{.keep-next}

**Solution:**
{.keep-next}

$$ ACF=\frac{18}{20}=0.9=90\% $$

### 95. كلفة حدث أمني (Security-Event Cost Function)

$$C_{event}=f(\Delta t,S,P)$$

**الرموز:** `Δt` مدة الحدث/الانقطاع؛ `S` الشدة؛ `P` الاحتمال؛ `f` دالة الكلفة التي يجب أن يعرّفها المصدر أو المسألة.

**الفكرة ومتى تظهر:** تصف اعتماد الكلفة على المدة والشدة والاحتمال، لكنها لا تكفي لإنتاج رقم من دون تعريف الدالة `f`.

**Worked example:** The source leaves event-cost function f unspecified. Write the event cost symbolically in terms of duration Δt, severity S, and probability P.
{.keep-next}

**Solution:**
{.keep-next}

$$ C_{event}=f(\Delta t,S,P) $$

### 96. الخطر بعد طبقات تخفيف (Residual Risk after Multiple Mitigation Layers)

$$R_{reduced}=R_{initial}\prod_j(1-E_j)$$

**الرموز:** `R_initial` الخطر الأولي؛ `E_j` فعالية الضابط `j`؛ `1−E_j` الجزء الباقي؛ `R_reduced` الخطر بعد الطبقات.

**الفكرة ومتى تظهر:** مثل نموذج الخطر المتبقي متعدد الضوابط؛ كل طبقة تضرب الجزء المتبقي، بافتراض الاستقلال.

**Worked example:** Initial risk is 100 and two mitigation layers each have effectiveness E_j=0.5.
{.keep-next}

**Solution:**
{.keep-next}

$$ R_{reduced}=100(1-0.5)(1-0.5)=25 $$

### 97. احتمال تجاوز طبقات المصادقة (Unauthorized-Access Probability through Authentication Layers)

$$P_{unauth}=\prod_k(1-F_k)$$

**الرموز:** `F_k` فعالية العامل `k` في منع المحاولة؛ `1−F_k` احتمال فشله؛ `P_unauth` احتمال الوصول غير المصرح به بعد العوامل.

**الفكرة ومتى تظهر:** عند افتراض أن المهاجم يحتاج تجاوز كل عوامل المصادقة وأنها مستقلة. الناتج احتمال مركب.

**Worked example:** An attacker must defeat three independent authentication factors. Each factor blocks 90% of attempts, so Fₖ=0.9 for all three factors. Find the unauthorized-access probability.
{.keep-next}

**Solution:**
{.keep-next}

$$ P_{unauth}=\prod_{k=1}^{3}(1-0.9)=0.1^3=0.001=0.1\% $$

### 98. مؤشر الصمود التشغيلي (Operational Resilience Index)

$$Resilience=\frac{1}{MTTD+MTTR}$$

**الرموز:** `MTTD` متوسط زمن اكتشاف المشكلة؛ `MTTR` متوسط زمن إصلاحها؛ `Resilience` مؤشر عكسي للزمنين وفق نموذج المذكرة.

**الفكرة ومتى تظهر:** تقارن سرعة الكشف والتعافي. كلما قصر مجموع الزمنين، ارتفع المؤشر. وحدته مقلوب الزمن.

**Worked example:** Mean time to detect is 2 hours and mean time to repair is 3 hours. Find resilience in inverse hours.
{.keep-next}

**Solution:**
{.keep-next}

$$ Resilience=\frac{1}{2+3}=0.2\text{ h}^{-1} $$

### 99. شرط انخفاض عدد الثغرات (Condition for Vulnerability Count Reduction)

$$\alpha>\frac{\beta}{V_t}$$

**الرموز:** `α` نسبة إزالة الثغرات؛ `β` عدد الثغرات الجديدة؛ `V_t` الثغرات الحالية. الشرط مشتق من مقارنة ما يزول بما يضاف في نموذج التحديث.

**الفكرة ومتى تظهر:** عندما يُسأل متى ينخفض العدد بين الدورات. إذا تحقق الشرط، الإزالة النسبية تتجاوز الإضافة.

**Worked example:** There are V_t=100 current vulnerabilities and β=5 new vulnerabilities per cycle. Find the condition for the count to decrease.
{.keep-next}

**Solution:**
{.keep-next}

$$ \alpha>\frac{5}{100}=0.05=5\% $$

### 100. فعالية تغطية تهديدات مستقلة (Combined Coverage of Independent Threats)

$$E_{total}=1-\prod_{i=1}^{p}(1-T_i)\prod_{j=1}^{q}(1-P_j)$$

**الرموز:** `T_i` تغطية/أثر مصدر التهديد `i`؛ `P_j` تغطية/أثر الضابط `j` كما عرفهما المصدر؛ `p,q` عدد العناصر؛ حاصل ضرب المكمّلات يمثل ما لم تغطه أي منها.

**الفكرة ومتى تظهر:** صيغة مكمّل الاتحاد تحت افتراض الاستقلال. راجع تعريف `T_i` و`P_j` في سؤال الفصل، لأن الرمز `P` له معانٍ متعددة.

**Worked example:** Two independent threat sources each provide coverage T_i=0.5; there are no additional control terms in this example.
{.keep-next}

**Solution:**
{.keep-next}

$$ E_{total}=1-(1-0.5)^2=0.75=75\% $$

### 101. دالة تقدير احتمال الاستغلال (Exploit-Likelihood Estimation Function)

$$L_i=f(CVSS,E_t,P_h)$$

**الرموز:** `L_i` تقدير احتمال/مستوى استغلال الثغرة `i`؛ `CVSS` درجة الشدة؛ `E_t` عامل التعرض؛ `P_h` سجل/احتمال تاريخي؛ `f` دالة التقدير.

**الفكرة ومتى تظهر:** وصف اعتماد التقدير على عدة عوامل، وليس قانوناً عددياً كاملاً من دون تعريف `f` وأوزانها.

**Worked example:** The source does not define the exploit-scoring function f. Write the score symbolically in terms of CVSS, exposure E_t, and historical evidence P_h.
{.keep-next}

**Solution:**
{.keep-next}

$$ L_i=f(CVSS,E_t,P_h) $$

### 102. مجموع معدلات الفشل التشغيلي والعدائي (Combined Operational and Adversarial Failure Rate)

$$\lambda_{total}=\lambda_o+\lambda_c$$

**الرموز:** `λ_o` معدل الفشل التشغيلي؛ `λ_c` معدل الفشل الناتج من سبب عدائي؛ `λ_total` مجموع المعدلين إذا اعتُبرا مستقلين ومتوافقين بالوحدة.

**الفكرة ومتى تظهر:** عند جمع مساهمتين في معدل الفشل لكل وحدة زمن. الناتج معدل إجمالي.

**Worked example:** The operational failure rate is 0.02 per hour and the adversarial failure rate is 0.03 per hour.
{.keep-next}

**Solution:**
{.keep-next}

$$ \lambda_{total}=0.02+0.03=0.05\text{ per hour} $$

### 103. موثوقية مع معدل فشل مركب (Reliability under a Combined Failure Rate)

$$R(t)=e^{-(\lambda_o+\lambda_c)t}$$

**الرموز:** `λ_o+λ_c` المعدل الكلي؛ `t` الزمن؛ `R(t)` احتمال البقاء عاملاً حتى ذلك الزمن وفق نموذج المعدل الثابت.

**الفكرة ومتى تظهر:** استخدمها بعد جمع معدلات فشل مستقلة/مضافة. الناتج موثوقية بين 0 و1.

**Worked example:** Operational and adversarial failure rates are 0.02 and 0.03 per hour; evaluate reliability after 10 hours.
{.keep-next}

**Solution:**
{.keep-next}

$$ R(10)=e^{-(0.02+0.03)(10)}=e^{-0.5}\approx0.6065\approx0.607 $$

### 104. مؤشر استمرارية الأعمال الموزون (Weighted Business Continuity Index)

$$BCI=\frac{\sum_iw_iC_i}{\sum_iw_i}$$

**الرموز:** `C_i` درجة مكوّن الاستمرارية `i`؛ `w_i` أهميته؛ `BCI` المتوسط الموزون.

**الفكرة ومتى تظهر:** عند تقييم عدة مكونات بوزن مختلف. الناتج متوسط موزون على مقياس الدرجات.

**Worked example:** Business-continuity scores are 0.8 and 0.6, with weights 3 and 1.
{.keep-next}

**Solution:**
{.keep-next}

$$ BCI=\frac{3(0.8)+1(0.6)}{3+1}=0.75 $$

### 105. شرط ميزانية الاستمرارية (Business-Continuity Budget Constraint)

$$\sum_iC_i\le B$$

**الرموز:** `C_i` كلفة/مخصص المكوّن `i` كما في قيد المصدر؛ `B` الميزانية؛ `Σ` مجموع الكلف.

**الفكرة ومتى تظهر:** قيد إنفاق مرافق لمؤشر الاستمرارية. يجب توحيد معنى `C_i` مع تعريف المصدر؛ لا تخلطه بدرجة المكوّن في معادلة BCI إذا كان السياق يغيّر تعريفه.

**Worked example:** Continuity components cost 4 and 3 units, and the budget is 8 units.
{.keep-next}

**Solution:**
{.keep-next}

$$ \sum_iC_i=4+3=7\le8=B\quad\text{(within budget)} $$

### 106. موثوقية مكوّنات على التوالي (Series-System Reliability)

$$R_{series}=\prod_iR_i$$

**الرموز:** `R_i` موثوقية المكوّن `i`؛ `Π` ضرب موثوقيات جميع المكونات؛ `R_series` موثوقية النظام المتسلسل.

**الفكرة ومتى تظهر:** في نظام يتوقف إذا تعطل أي مكوّن، ومع افتراض استقلال الأعطال. الناتج أقل من أو يساوي موثوقية كل مكوّن.

**Worked example:** A series system has two independent components, each with reliability 0.9.
{.keep-next}

**Solution:**
{.keep-next}

$$ R_{series}=0.9\times0.9=0.81 $$

### 107. موثوقية مكونات على التوازي (Parallel-System Reliability)

$$R_{parallel}=1-\prod_i(1-R_i)$$

**الرموز:** `R_i` موثوقية المكوّن؛ `1−R_i` احتمال فشله؛ ضرب احتمالات الفشل يعطي فشل الجميع؛ طرحه من 1 يعطي عمل واحد على الأقل.

**الفكرة ومتى تظهر:** في نظام متوازٍ مستقل يكفي أن يعمل مكوّن واحد. الناتج عادة أعلى من موثوقية مكوّن مفرد.

**Worked example:** A parallel system has two independent components, each with reliability 0.9.
{.keep-next}

**Solution:**
{.keep-next}

$$ R_{parallel}=1-(1-0.9)^2=0.99 $$

### 108. التوفر من متوسط زمن العمل والإصلاح (Availability from MTBF and MTTR)

$$A=\frac{MTBF}{MTBF+MTTR}$$

**الرموز:** `A` التوفر؛ `MTBF` متوسط الزمن بين الأعطال؛ `MTTR` متوسط زمن الإصلاح. يجب توحيد وحدة الزمن.

**الفكرة ومتى تظهر:** تقدير نسبة الوقت المتوقع أن تكون فيه الخدمة عاملة في نموذج دوري مبسط. الناتج نسبة من 0 إلى 1.

**Worked example:** A service has MTBF=99 hours and MTTR=1 hour.
{.keep-next}

**Solution:**
{.keep-next}

$$ A=\frac{99}{99+1}=0.99=99\% $$

## تشابه الرموز: احسمه من السياق

| الرمز | المعنى هنا | علامة السياق |
|:---|:---|:---|
| `R(t)` في الفصل 1 | تعرض التهديدات وأثرها بمرور الزمن | ترى `P_i(t)` و`I_i(t)` ثم مجموعاً |
| `R(t)` في الفصل 6 | موثوقية مكوّن حتى زمن `t` | ترى `e^(−λt)` ومعدل فشل |
| `A` | قد تعني Availability أو Attack Amplification أو Alert/Anomaly | اقرأ اسم المؤشر والرموز المجاورة |
| `P` | قد تعني probability أو privacy أو plaintext | اقرأ الفهرس والسياق قبل التعويض |
| `C` | قد تعني confidentiality أو cost أو ciphertext | حدّد الفصل والدالة أولاً |
| `H` | قد تعني عدد Cache hits أو entropy أو hash | انتبه للوحدات والموضع |

## بطاقة تذكير قصيرة

- **احتمال مع أثر:** اضربهما لتحصل على مساهمة خطر، ثم اجمع السيناريوهات عند طلب الإجمالي.
- **ضابط فعاليته `e`:** الجزء الباقي عادة `1−e` في الصيغ التي تنص على ذلك.
- **طبقات مستقلة يجب أن تفشل كلها كي ينجح الهجوم:** اضرب احتمالات فشل الطبقات.
- **توازي موثوقية:** اطرح احتمال فشل الجميع من 1. **توالي:** اضرب الموثوقيات.
- **نتيجة بلا وحدة:** احتمال أو نسبة. **نتيجة بزمن/مال:** احفظ وحدة المدخلات في الحساب.
- قوانين الفصول 5–6 المساندة تشرح نماذج المذكرات؛ لا تفترض أن كل واحدة مطلوبة حفظاً إذا لم يقل ذلك سجل الامتحان.

## Retrieval set — راجع فهمك

1. اشرح الفرق بين `R(t)` في الفصل 1 و`R(t)` في الفصل 6، واذكر المعطيات التي تميّز كل واحدة.
2. في `S=F×K`، ماذا تفعل إذا كانت `F` و`K` وصفاً مثل Medium وHigh؟
3. ماذا تعني `ΔL` في صيغة Cache، وما الفرق بينها وبين `L_saved`؟
4. إذا كانت فعالية ضابط `e=0.75`، فما الجزء الذي يبقى من الخطر في نموذج `R(1−e)`؟
5. لماذا نأخذ الأصغر في `S_TLS=min(...)`؟
6. ما معنى `mod 26` في Caesar؟
7. في RSA التعليمي، ما علاقة `e` و`d` و`φ(n)`؟
8. كيف يُحسب احتمال نجاح محاولة واحدة على الأقل بعد `m` محاولات مستقلة؟
9. ما الفرق بين `TPR` و`FPR` من حيث المقام؟
10. متى يكون ضرب موثوقيات المكونات مناسباً، ومتى نضرب احتمالات فشلها؟

## الإجابات

1. الأولى تعرض تهديدات واحتمالاتها وآثارها المتغيرة مع الزمن؛ الثانية احتمال بقاء مكوّن عاملاً، وتظهر معها قيمة معدل الفشل `λ` والأس `e^(−λt)`.
2. نستخدم مصفوفة الخطر الوصفية في المادة، ولا نحول الفئات إلى أرقام من عندنا.
3. `ΔL` توفير الزمن لكل إصابة؛ `L_saved` مجموع التوفير بعد ضربه بعدد الإصابات `H`.
4. يبقى `1−0.75=0.25`، أي ربع الخطر الأصلي.
5. لأن قوة النظام المركب يحدها أضعف مكوّن أماناً في هذا النموذج.
6. يعيد الرقم إلى مجال الحروف من 0 إلى 25 بعد الإزاحة أو فكها.
7. `d` هو المعكوس الضربي لـ`e` modulo `φ(n)`، أي إن `ed` باقيه 1 عند القسمة على `φ(n)`.
8. `1−(1−p)^m`.
9. مقام `TPR` كل الحالات الإيجابية الفعلية `TP+FN`؛ مقام `FPR` كل السليمة `FP+TN`.
10. في التوالي نضرب احتمالات عمل كل المكونات؛ في التوازي نضرب احتمالات فشل الجميع ثم نطرح من 1.

## كيف نميّز المعادلات المتشابهة؟

راجعت الصيغ الـ108 على مستوى شكلها الرياضي ومعنى رموزها. بعض الصيغ لها **نفس البنية وتطبيق مختلف**، وبعضها **صيغة عامة وتطبيق خاص**، وبعضها **متشابه بالرموز فقط**. لذلك لا نختار المعادلة من شكلها وحده؛ نقرأ اسم الكمية المطلوبة وتعريف الرموز في السؤال.

### جمع الاحتمال في الأثر: خطر أم خسارة مالية؟

$$R(t)=\sum_i P_i(t)I_i(t)$$

$$EFL=\sum_i P_iI_i$$

كلاهما يجمع احتمال كل سيناريو مضروباً في أثره. الأولى تقدّر درجة الخطر عند زمن `t`، والثانية تقدّر خسارة متوقعة بعملة. إذا كان `I_i` مبلغاً مالياً فالنتيجة مالية؛ وإذا كان مقياس أثر أمني فالنتيجة مقياس خطر. لا نخلط الوحدتين.

### حساب خطر العنصر: عوامل مختلفة بحسب النموذج

$$Risk=Threat\times Vulnerability\times Impact$$

$$R_i=P_iV_i \qquad\text{أو}\qquad R_i=L_iS_iI_i$$

هذه نماذج ضرب لمكوّن خطر، لكنها ليست قابلة للتبديل تلقائياً: الأولى تستخدم تهديداً وضعفاً وأثراً؛ والثانية احتمالاً وقابلية/ضعفاً؛ والثالثة احتمال استغلال وشدة وأثراً. نستخدم تعريف الفصل أو المسألة كما هو.

### جمع مخاطر العناصر: خطر الشبكة وخطر الثغرات

$$R_{net}=\sum_iR_i \qquad\text{و}\qquad R_{total}=\sum_iR_i$$

البنية الرياضية واحدة، والاختلاف في مجموعة العناصر الداخلة في الجمع: عناصر الشبكة في الأولى، والثغرات في الثانية. معنى كل `R_i` يتبع تعريفه قبل الجمع. هذان اسمان لتطبيقين لسلسلة الجمع نفسها، لا قانونان رياضيان مستقلان.

### الخطر المتبقي: ضابط واحد أم ضوابط متعددة؟

$$R_{res}=R_0(1-e)$$

$$R_{residual}=R_0\prod_i(1-e_i) \qquad\text{و}\qquad R_{reduced}=R_{initial}\prod_j(1-E_j)$$

الأولى لضابط واحد. الصيغتان ذواتا حاصل الضرب تمثلان عدة طبقات، وتفترضان أن فعالية كل طبقة معرّفة وأن نموذج الضرب مناسب. الصيغتان الأخيرتان لهما البنية نفسها مع اختلاف أسماء الرموز؛ لا تحسبهما كفكرتين منفصلتين.

صيغة الشبكة تطبق عامل التخفيف على كل سيناريو قبل الجمع:

$$R_{net}=\sum_i(1-e_i)P_iI_i$$

أما الصيغة التالية فتختار الضوابط التي تقلل الخطر المتبقي تحت قيد ميزانية؛ فهي مسألة تحسين، لا مجرد حساب خطر متبقٍ:

$$\min R_{residual}=\sum_iR_i(1-M_i)$$

### ضرب احتمالات تجاوز الدفاع: الحدث الذي يفشل يختلف

$$P_{success}=\prod_iq_i \qquad\text{و}\qquad P_{compromise}=\prod_i(1-E_i)$$

$$P_{unauth}=\prod_k(1-F_k)$$

كلها تضرب احتمالات مرتبطة بتجاوز أو فشل طبقات مستقلة. `q_i` احتمال تجاوز الطبقة، و`1−E_i` الجزء الذي لم يمنعه الضابط، و`1−F_k` احتمال فشل عامل المصادقة. واحتمال الثقة بالشهادة يضرب نجاح التحقق من الجهة المصدّرة والتحقق من الشهادة؛ ثم تضرب صيغة الأمان المركب متمّمات أحداث الإخفاق التي عرّفتها المادة. التشابه في الحساب لا يجعل الأحداث أو الرموز متطابقة.

$$P_{trust}=(1-P_{ca})(1-P_{val}) \qquad\text{و}\qquad P_{secure}=(1-P_{int})(1-P_{sig})(1-P_{trust})$$

أما حاصل ضرب فعالية المكونات الدفاعية فيجمع فعاليات مكونات وفق تعريف النموذج:

$$a_{total}=a_fa_pa_v$$

لا نساويه تلقائياً بحاصل ضرب احتمالات الفشل أو الأجزاء المتبقية.

### احتمال نجاح واحد على الأقل: المتمّم بعد ضرب الإخفاقات

$$1-(1-p)^m \qquad\text{و}\qquad R_{parallel}=1-\prod_i(1-R_i)$$

الأولى لاحتمال نجاح محاولة واحدة على الأقل بعد `m` محاولات مستقلة؛ والثانية لموثوقية نظام متوازٍ يعمل إذا عمل مكوّن واحد على الأقل. الفكرة المشتركة هي طرح احتمال فشل الجميع من 1.

$$E_{total}=1-\prod_i(1-T_i)\prod_j(1-P_j)$$

هذه تجمع التغطية/الفعالية بافتراض الاستقلال وباستخدام متمّمات ما لم تغطه العناصر. وتستخدم صيغة خفض الخطر الفكرة نفسها لحساب نسبة الخطر المخفّض عبر ضوابط متعددة. تُفسّر `T_i` و`P_j` بتعريف المصدر، ولا تُساوى تلقائياً باحتمالات المحاولات أو موثوقيات المكونات.

$$\max(R_0-R_{residual})=R_0\left(1-\prod_i(1-r_i)\right)$$

### موثوقية المكوّن: معدل واحد أو معدل مركّب

$$R(t)=e^{-\lambda t}$$

$$\lambda_{total}=\lambda_o+\lambda_c \qquad\Rightarrow\qquad R(t)=e^{-(\lambda_o+\lambda_c)t}$$

الصيغة الثانية توسّع الأولى إلى معدلي فشل تشغيلي وعدائي بعد جمعهما. النتيجة في الحالتين احتمال بقاء المكوّن عاملاً، وليست درجة الخطر المحسوبة من احتمالات التهديدات وآثارها.

### التوفر: قرار أمني أم أجهزة معاً أم خدمة عبر الزمن؟

$$A=1-(P_{allow}+P_{deny}) \qquad\text{و}\qquad A_{eff}=A_{ids}A_{ips}$$

$$A=\frac{MTBF}{MTBF+MTTR}$$

الأولى تستنتج توافر القرار من أخطاء السماح والمنع، والثانية توافر IDS وIPS معاً وفق نموذج الضرب، والثالثة تقدّر توافر خدمة من أزمنة العمل والإصلاح. الرمز `A` مشترك، لكن وحدة التحليل والمدخلات مختلفة.

### المتوسط الموزون: امتثال أم استمرارية أعمال؟

$$PCI=\frac{\sum_iw_ic_i}{\sum_iw_i} \qquad\text{و}\qquad BCI=\frac{\sum_iw_iC_i}{\sum_iw_i}$$

البنية واحدة: درجات عناصر مضروبة بأوزانها، ثم القسمة على مجموع الأوزان. `PCI` للامتثال و`BCI` لاستمرارية الأعمال. أما `C(E)` فهو مجموع موزون؛ لا يصبح متوسطاً إلا إذا كان مجموع الأوزان `1`.

### قيود الميزانية: صياغة واحدة لمجالين

$$\sum_i c_i\le B \qquad\text{و}\qquad \sum_i C_i\le B$$

الصيغتان تعبران عن قيد مجموع الكلفة تحت ميزانية. الاختلاف في اسم التكلفة ومجموعة الضوابط أو مكونات الاستمرارية التي يغطيها القيد.

### نسبة بعدد جزئي وإجمالي: قاسم مشترك لا معنى واحد

$$CHR=\frac{H}{N} \qquad TPR=\frac{TP}{TP+FN} \qquad FPR=\frac{FP}{FP+TN}$$

$$RC=\frac{Monitored\ Paths}{Total\ Paths} \qquad ACF=\frac{V_d}{V_a}$$

هذه صيغ نسب، لكن المقامات تحدد معناها: إصابات Cache من كل الطلبات؛ كشف الإيجابيات الفعلية؛ الإنذارات الكاذبة بين الحالات السليمة؛ المسارات المراقبة؛ أو الثغرات المكتشفة من المتاحة. لا نقارن النسب قبل فحص البسط والمقام.

### تقليل السطح ومعدل المنع بالتقسيم

$$ASR=1-\frac{E_{exposed}}{E_{total}} \qquad E_{micro}=\frac{N-N_{allowed}}{N}$$

كلتاهما تقيسان جزءاً أُزيل أو مُنع من إجمالي. الأولى تخفيض نقاط النهاية المكشوفة؛ والثانية نسبة الاتصالات التي منعها التقسيم الدقيق. تتشابهان إذا كان تعريف العددين متوافقاً، لكنهما تقيسان مجموعتين مختلفتين.

<div class="page-break"></div>

### مؤشرات تستخدم أصغر قيمة: قوة أمان أم زمن كسر؟

$$S_{TLS}=\min(S_{sym},S_{asym},S_{hash}) \qquad T_{system}=\min(T_{sym},T_{asym})$$

كلتاهما تختار العنصر الأضعف/الأسرع في نموذج النظام الهجين، لكن الأولى تقارن قوة الأمان، والثانية تقارن أزمنة الكسر. الناتج ووحدته مختلفان.

### البحث بالقوة الغاشمة: عدد محاولات أم زمن؟

$$E[N]\approx2^{H-1} \qquad T_{crack}\approx\frac{2^{k-1}}{R} \qquad T_{forge}\approx\frac{2^{b_{sig}}}{R}$$

الأولى تقدّر عدد المحاولات المتوقع؛ والأخريان تحولان فضاء البحث إلى زمن بقسمته على معدل المحاولات `R`. الأخيرة خاصة بتجربة التواقيع وفق طولها `b_sig`.

### صف الانتظار: النسبة نفسها لقياسات مختلفة

$$\rho=\frac{\lambda}{\mu} \qquad N_{concurrent}\approx\frac{\lambda}{\mu} \qquad \frac{\lambda}{\mu}\ge M\Rightarrow\text{saturation}$$

تظهر نسبة الوصول إلى الخدمة `λ/μ` كمقياس استخدام للطابور، وكتقدير للحالات المتزامنة في النموذج، وكشرط تشبع عند تجاوز السعة `M`. واحتمال الحجب يعتمد على هذه النسبة وسعة الطابور `B`؛ فهو احتمال حجب لا مقياس استخدام. لا تساوي بين النتائج دون قراءة تعريف `λ` و`μ` في السياق.

$$P_{block}=\frac{(1-\rho)\rho^B}{1-\rho^{B+1}}\qquad(\rho\ne1)$$

### مقاييس Cache الثلاثة: إصابات وزمن لكل إصابة ومجموع توفير

$$CHR=\frac{H}{N} \qquad \Delta L=L_{origin}-L_{cache} \qquad L_{saved}=H(L_{origin}-L_{cache})$$

`CHR` نسبة الطلبات التي أصابت الذاكرة؛ `ΔL` زمن موفر لكل إصابة؛ و`L_saved` مجموع الزمن الموفر عبر `H` إصابات. الصيغ مترابطة وليست بدائل لبعضها.

### عدد الثغرات: معادلة تحديث وشرط انخفاض

$$V_{t+1}=V_t(1-\alpha)+\beta \qquad\text{والشرط المكافئ للانخفاض:}\qquad \alpha>\frac{\beta}{V_t}$$

الشرط مكافئ لكون العدد في الدورة التالية أقل من العدد الحالي. الأولى تحسب العدد في الدورة التالية؛ والثانية تحدد متى ينخفض.


