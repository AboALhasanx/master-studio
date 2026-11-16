---
title: "ملزمة AI · W03 — التصنيف: KNN · أشجار القرار · Naive Bayes · SVM"
subtitle: "Supervised classification · ID3 entropy and information gain · Bayes rule · maximum margin"
course: Artificial Intelligence
instructor: Dr. Saif Ali
term: Fall 2026
week: Week 03
---

# التصنيف — أربع خوارزميات على مجموعة بيانات واحدة

> **من وين جاي:** W02 انتهت عند البحث — «كيف أصل إلى هدف». هذا الفصل يقلب السؤال: **«كيف أتعلّم القاعدة من الأمثلة؟»** بدل أن تبحث عن الحل، تعطيك البيانات أمثلة محلولة وتطلب منك تعميمها على مثال جديد. وهذا اسمه **supervised classification**.

**لماذا مجموعة واحدة؟** لأن الامتحان لا يسأل «كيف يعمل KNN؟» بل «**أيّهما تختار ولماذا؟**». فسنشرح الأربعة على **نفس البيانات** (PlayTennis) ونفس الاستعلام، ونقارن النتائج.

---

## 1. الإطار العام

| | **Classification** | **Clustering** |
|:---|:---|:---|
| التعلّم | **Supervised** — التسميات موجودة | **Unsupervised** — لا تسميات |
| السؤال | «أي صنف ينتمي هذا؟» | «ما المجموعات الطبيعية؟» |
| أمثلة | KNN · Trees · NB · SVM | K-means · DBSCAN |

**البيانات:** $\{(\mathbf{x}_i, y_i)\}$ حيث $\mathbf{x}_i$ متجه الخصائص و$y_i$ التسمية.

**الهدف:** تعلّم دالة $f: \mathbf{x} \to y$ تُعمَّم على أمثلة **لم تُرَ**.

---

## 2. مجموعة البيانات المشتركة — PlayTennis

أربعة عشر يوماً، أربع خصائص، تسمية واحدة: **هل نلعب التنس؟**

| اليوم | Outlook | Temperature | Humidity | Wind | Play |
|:--:|:---|:---|:---|:---|:--:|
| D1 | Sunny | Hot | High | Weak | **No** |
| D2 | Sunny | Hot | High | Strong | **No** |
| D3 | Overcast | Hot | High | Weak | **Yes** |
| D4 | Rain | Mild | High | Weak | **Yes** |
| D5 | Rain | Cool | Normal | Weak | **Yes** |
| D6 | Rain | Cool | Normal | Strong | **No** |
| D7 | Overcast | Cool | Normal | Strong | **Yes** |
| D8 | Sunny | Mild | High | Weak | **No** |
| D9 | Sunny | Cold | Normal | Weak | **Yes** |
| D10 | Rain | Mild | Normal | Weak | **Yes** |
| D11 | Sunny | Mild | Normal | Strong | **Yes** |
| D12 | Overcast | Mild | High | Strong | **Yes** |
| D13 | Overcast | Hot | Normal | Weak | **Yes** |
| D14 | Rain | Mild | High | Strong | **No** |

**الأعداد:** 14 مثالاً · **Yes = 9** · **No = 5**.

---

## 3. K-Nearest Neighbour

### الفكرة

**لا يبني نموذجاً إطلاقاً.** يخزّن البيانات، وعند سؤال جديد يحسب **المسافة** لأقرب $k$ أمثلة ويأخذ **الأغلبية**.

فـKNN مثال على **lazy learning** — التعلّم كله **مؤجّل** إلى لحظة السؤال.

| المصطلح | المعنى |
|:---|:---|
| **Instance-based** | يتعلّم من **الأمثلة نفسها**، لا من قاعدة مستخلصة |
| **Non-parametric** | لا يفترض شكلاً ثابتاً للبيانات |
| **Lazy** | لا يبني نموذجاً قبل السؤال |

### المسافة

**المسافة الإقليدية** (الافتراضية للبيانات الرقمية):

$$d(\mathbf{p}, \mathbf{q}) = \sqrt{\sum_{i=1}^{n} (p_i - q_i)^2}$$

**للبيانات المختلطة:** Gower distance أو أي مقياس ملائم.

**⚠️ الشرط الحاسم:** **طبّع أو وحّد (normalize/standardize)** الأعمدة قبل حساب المسافة. لماذا؟ لأن خاصية بمدى آلاف (الراتب) **تسحق** خاصية بمدى 0–1 (العمر)، فيصبح الوزن لعمود واحد بلا سبب.

$$x' = \frac{x - \min}{\max - \min} \quad\text{(min-max)} \qquad x' = \frac{x - \mu}{\sigma} \quad\text{(z-score)}$$

### مثال محسوب — نفس الاستعلام، ثلاثة $k$

**الأمثلة** (خاصيتان، صنفان):

| النقطة | $x_1$ | $x_2$ | الصنف |
|:--:|:--:|:--:|:--:|
| $P_1$ | 1 | 1 | A |
| $P_2$ | 2 | 2 | A |
| $P_3$ | 3 | 0 | A |
| $P_4$ | 6 | 1 | B |
| $P_5$ | 6 | 3 | B |
| $P_6$ | 7 | 2 | B |

**الاستعلام:** $\mathbf{q} = (4, 2)$.

**المسافات:**

| النقطة | الحساب | $d$ | الصنف |
|:--:|:---|:--:|:--:|
| $P_2$ | $\sqrt{(4-2)^2 + (2-2)^2} = \sqrt{4}$ | **2.000** | A |
| $P_3$ | $\sqrt{(4-3)^2 + (2-0)^2} = \sqrt{5}$ | **2.236** | A |
| $P_4$ | $\sqrt{(4-6)^2 + (2-1)^2} = \sqrt{5}$ | **2.236** | B |
| $P_5$ | $\sqrt{(4-6)^2 + (2-3)^2} = \sqrt{5}$ | **2.236** | B |
| $P_6$ | $\sqrt{(4-7)^2 + (2-2)^2} = \sqrt{9}$ | **3.000** | B |
| $P_1$ | $\sqrt{(4-1)^2 + (2-1)^2} = \sqrt{10}$ | **3.162** | A |

**النتيجة تتغيّر مع $k$:**

| $k$ | أقرب الجيران | الأصوات | القرار |
|:--:|:---|:---|:--:|
| **1** | $P_2$ (A) | A:1 | **A** |
| **3** | $P_2$(A) · $P_3$(A) · $P_4$(B) | **A:2 · B:1** | **A** |
| **5** | + $P_5$(B) · $P_6$(B) | A:2 · **B:3** | **B** |

**شنو تتعلم:** نفس البيانات ونفس السؤال أعطيا **جوابين متعاكسين** بسبب $k$ وحده. ولهذا «** كيف نختار $k$؟**» سؤال حقيقي، لا تفصيل.

| $k$ صغير | $k$ كبير |
|:---|:---|
| حساس للضجيج (نقطة واحدة تقلب القرار) | يمسح الحدود بين الأصناف |
| **overfitting** | **underfitting** |
| جرّب $k$ فردياً (يمنع التعادل) | $k \le \sqrt{n}$ كقاعدة عملية |

---

## 4. أشجار القرار و ID3

### الفكرة

كل **عقدة داخلية** تسأل عن **خاصية واحدة** · كل **فرع** = إجابة ممكنة · كل **ورقة** = **قرار التصنيف**.

**التعبير المنطقي للشجرة:** الشجرة في الصفحة التالية تكتب:

$$(\text{Outlook}=\text{Sunny} \wedge \text{Humidity}=\text{Normal}) \ \vee\ (\text{Outlook}=\text{Overcast}) \ \vee\ (\text{Outlook}=\text{Rain} \wedge \text{Wind}=\text{Weak})$$

### لماذا «الأبسط»؟

من مجموعة تدريب واحدة تُوجد **شجرات كثيرة** صحيحة. والقاعدة: **اختر الأبسط** (الأقصر)، لأن الأقصر **يعمّم** أفضل.

**المشكلة:** تجربة كل الشجرات واختيار الأقصر = **وقت هائل**. فـ**ID3** يبني شجرة قصيرة **بكفاءة**، دون ضمان أنها الأقصر مطلقاً.

### الإنتروبيا — مقياس «الاختلاط»

$$E(S) = -p_+ \log_2 p_+ - p_- \log_2 p_-$$

| الحالة | $E$ | المعنى |
|:---|:--:|:---|
| كل الأمثلة **Yes** | **0** | نقاء تام |
| كل الأمثلة **No** | **0** | نقاء تام |
| **50% / 50%** | **1** | أقصى اختلاط |

**للحالة العامة (أكثر من صنفين):**

$$E(S) = -\sum_{i=1}^{n} p_i \log_2 p_i$$

### Information Gain — معيار الاختيار

$$\boxed{Gain(S, A) = E(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} \, E(S_v)}$$

**اقرأها:** «الإنتروبيا قبل التقسيم» **ناقص** «الإنتروبيا المتوقّعة بعده». أي: **كم نقاءً كسبنا** من هذا السؤال.

### التتبّع الكامل — PlayTennis

**الخطوة 1 — إنتروبيا الجذر:**

$$E(S) = -\frac{9}{14}\log_2\frac{9}{14} - \frac{5}{14}\log_2\frac{5}{14} = 0.6429(0.6374) + 0.3571(1.4855) = \mathbf{0.9403}$$

**الخطوة 2 — Gain لكل خاصية:**

**Outlook:**

| القيمة | $n$ | Yes | No | $E(S_v)$ |
|:---|:--:|:--:|:--:|:--:|
| Overcast | 4 | 4 | 0 | **0.0000** |
| Rain | 5 | 3 | 2 | **0.9710** |
| Sunny | 5 | 2 | 3 | **0.9710** |

$$Gain = 0.9403 - \left[\tfrac{4}{14}(0) + \tfrac{5}{14}(0.9710) + \tfrac{5}{14}(0.9710)\right] = 0.9403 - 0.6935 = \mathbf{0.2467}$$

**Humidity:**

| القيمة | $n$ | Yes | No | $E(S_v)$ |
|:---|:--:|:--:|:--:|:--:|
| High | 7 | 3 | 4 | **0.9852** |
| Normal | 7 | 6 | 1 | **0.5917** |

$$Gain = 0.9403 - \left[\tfrac{7}{14}(0.9852) + \tfrac{7}{14}(0.5917)\right] = 0.9403 - 0.7885 = \mathbf{0.1518}$$

**Temperature:**

| القيمة | $n$ | Yes | No | $E(S_v)$ |
|:---|:--:|:--:|:--:|:--:|
| Cold | 1 | 1 | 0 | 0.0000 |
| Cool | 3 | 2 | 1 | 0.9183 |
| Hot | 4 | 2 | 2 | **1.0000** |
| Mild | 6 | 4 | 2 | 0.9183 |

$$Gain = 0.9403 - 0.8760 = \mathbf{0.0642}$$

**Wind:**

| القيمة | $n$ | Yes | No | $E(S_v)$ |
|:---|:--:|:--:|:--:|:--:|
| Strong | 6 | 3 | 3 | **1.0000** |
| Weak | 8 | 6 | 2 | 0.8113 |

$$Gain = 0.9403 - 0.8922 = \mathbf{0.0481}$$

**الخطوة 3 — الترتيب:**

| الخاصية | Gain |
|:---|:--:|
| **Outlook** | **0.2467** ✅ |
| Humidity | 0.1518 |
| Temperature | 0.0642 |
| Wind | 0.0481 |

**الجذر = Outlook** (أعلى Gain).

**الخطوة 4 — الشجرة النهائية:**

$$\text{Outlook} = \begin{cases} \textbf{Overcast} & \to \textbf{Yes} \quad (4/0 \text{ نقية}) \\[4pt] \textbf{Rain} & \to \text{Wind} = \begin{cases} \text{Strong} \to \textbf{No} \\ \text{Weak} \to \textbf{Yes} \end{cases} \\[10pt] \textbf{Sunny} & \to \text{Humidity} = \begin{cases} \text{High} \to \textbf{No} \\ \text{Normal} \to \textbf{Yes} \end{cases} \end{cases}$$

**لماذا توقّفنا عند Overcast؟** لأن $E = 0$ — الفرع **نقي**، فلا حاجة لسؤال آخر.

**⚠️ مصيدة:** لا تقسّم فرعاً **نقياً**. الطالب كثيراً ما يكمل التقسيم على `Overcast` ويستهلك خصائص بلا فائدة، فيصنع شجرة **أوسع** — وهذا **يخالف** هدف ID3 (أقصر شجرة).

### Overfitting والتقليم

شجرة تنمو حتى **نقاء تام** على بيانات التدريب قد تحفظ **الضجيج**.

| التقنية | الفكرة |
|:---|:---|
| **Pre-pruning** | أوقف النمو عند شرط (مثل: $n <$ حدّ، أو $Gain <$ حدّ) |
| **Post-pruning** | ابنِ الشجرة كاملة ثم **اقطع** الفروع التي لا تحسّن دقة التحقّق |
| **Cross-validation** | قِس الدقة على بيانات لم تُرَ |

### البيانات الرقمية

ID3 يتعامل مع **قيم منفصلة**. للخاصية الرقمية: رتّب القيم واختبر **عتبات** ($x \le t$)، واختر العتبة بأعلى Gain. هذا ما يفعله **C4.5**.

---

## 5. Naive Bayes

### نظرية بايز

$$P(C \mid X) = \frac{P(X \mid C)\, P(C)}{P(X)}$$

| الحدّ | الاسم |
|:---|:---|
| $P(C)$ | **Prior** — اعتقادك قبل رؤية المثال |
| $P(X \mid C)$ | **Likelihood** — كم يفسّر الصنف البيانات |
| $P(C \mid X)$ | **Posterior** — ما تريده |

### الافتراض «الساذج»

$X = (x_1, \ldots, x_n)$ تحتاج $P(x_1, \ldots, x_n \mid C)$ — جدول **هائل**. فـNB يفترض **الاستقلال الشرطي**:

$$P(X \mid C) \approx \prod_{i=1}^{n} P(x_i \mid C)$$

$$\boxed{P(C \mid X) \propto P(C) \prod_{i=1}^{n} P(x_i \mid C)}$$

**«ساذج» لأن** الاستقلال غالباً **غير صحيح** (الخصائص مترابطة). لكنه **يعمل جيداً عملياً** — وهذا مفارقة تُذكر في الامتحان.

### مثال محسوب — نفس البيانات

**الاستعلام:** $\text{Outlook}=\text{Sunny},\ \text{Temp}=\text{Cool},\ \text{Humidity}=\text{High},\ \text{Wind}=\text{Strong}$.

**الـPriors:**

$$P(\text{Yes}) = \frac{9}{14} = 0.6429 \qquad P(\text{No}) = \frac{5}{14} = 0.3571$$

**الـLikelihoods (من الجدول مباشرة):**

| الخاصية | $P(\cdot \mid \text{Yes})$ | $P(\cdot \mid \text{No})$ |
|:---|:--:|:--:|
| Outlook = Sunny | $2/9 = 0.2222$ | $3/5 = 0.6000$ |
| Temp = Cool | $2/9 = 0.2222$ | $1/5 = 0.2000$ |
| Humidity = High | $3/9 = 0.3333$ | $4/5 = 0.8000$ |
| Wind = Strong | $3/9 = 0.3333$ | $3/5 = 0.6000$ |

**الحساب:**

$$\text{Yes}: \ 0.6429 \times 0.2222 \times 0.2222 \times 0.3333 \times 0.3333 = \mathbf{0.003527}$$

$$\text{No}: \ 0.3571 \times 0.6000 \times 0.2000 \times 0.8000 \times 0.6000 = \mathbf{0.020571}$$

**التطبيع:**

$$P(\text{Yes} \mid X) = \frac{0.003527}{0.003527 + 0.020571} = \mathbf{0.1464}$$

$$P(\text{No} \mid X) = \mathbf{0.8536}$$

**القرار: No** بثقة **85.4%**.

**تحقّق متقاطع:** الشجرة أعطت نفس الجواب! المسار: `Sunny ← Humidity=High ← No`. فخوارزميتان مستقلتان اتفقتا — وهذا **اختبار ذاتي** جيد في الامتحان.

### مشكلة الصفر — ولماذا التنعيم

لو ظهرت قيمة لم تُرَ مع صنف، فـ$P(x_i \mid C) = 0$، والضرب **يصفر** كل شيء:

$$P(C \mid X) \propto P(C) \times 0 \times \cdots = 0$$

**الحل — Laplace smoothing ($\alpha = 1$):**

$$P(x_i \mid C) = \frac{\text{count}(x_i, C) + \alpha}{\text{count}(C) + \alpha \cdot |V_i|}$$

**تطبيقاً على الاستعلام نفسه:**

| الخاصية | Yes | No |
|:---|:--:|:--:|
| Outlook = Sunny | $\dfrac{2+1}{9+3} = 0.2500$ | $\dfrac{3+1}{5+3} = 0.5000$ |
| Temp = Cool | $\dfrac{2+1}{9+4} = 0.2308$ | $\dfrac{1+1}{5+4} = 0.2222$ |
| Humidity = High | $\dfrac{3+1}{9+2} = 0.3636$ | $\dfrac{4+1}{5+2} = 0.7143$ |
| Wind = Strong | $\dfrac{3+1}{9+2} = 0.3636$ | $\dfrac{3+1}{5+2} = 0.5714$ |

**⚠️ مصيدة:** التنعيم يمنع الصفر، لكنه **يغيّر الأرقام**. في الامتحان: إن لم يُطلب صريحاً، استعمل العدّ المباشر؛ وإن ظهر صفر في المقام أو البسط، **قل إنك تُنعّم** واذكر $\alpha$.

---

## 6. Support Vector Machines

### المصنّف الخطي

$$\mathbf{w}^T \mathbf{x} + b = 0 \quad\text{(المستوي الفاصل)}$$

$$f(\mathbf{x}) = \operatorname{sign}(\mathbf{w}^T \mathbf{x} + b)$$

| الحالة | المعنى |
|:---|:---|
| $\mathbf{w}^T\mathbf{x} + b > 0$ | صنف $+1$ |
| $\mathbf{w}^T\mathbf{x} + b < 0$ | صنف $-1$ |

### الهامش — الفكرة كلها

**أي مستوي فاصل صحيح؟** عدد لا نهائي. فـSVM يختار الذي **يبعد أكثر ما يمكن** عن أقرب النقاط من الطرفين.

$$\text{Margin} = \frac{2}{\lVert \mathbf{w} \rVert}$$

**ولهذا** SVM يحلّ:

$$\min_{\mathbf{w}, b} \tfrac{1}{2}\lVert \mathbf{w} \rVert^2 \quad \text{s.t.} \quad y_i(\mathbf{w}^T\mathbf{x}_i + b) \ge 1$$

**تصغير $\lVert \mathbf{w} \rVert$ = تكبير الهامش.** هذه هي المسألة، لا أكثر.

**النقاط الحرجة** التي تلمس حدود الهامش تُسمّى **support vectors** — وهي **وحدها** التي تحدّد المستوي. لو حذفت أي نقطة أخرى، **لا يتغيّر** المستوي.

### أرقام الهامش

| $\mathbf{w}$ | $b$ | $\lVert \mathbf{w} \rVert$ | الهامش $2/\lVert \mathbf{w} \rVert$ |
|:---|:--:|:--:|:--:|
| $(1,1)$ | $-3$ | 1.4142 | **1.4142** |
| $(2,2)$ | $-6$ | 2.8284 | **0.7071** |
| $(1,-1)$ | $0$ | 1.4142 | **1.4142** |

**لاحظ — نفس المستوي هندسياً، هامشان مختلفان:** $(1,1,-3)$ و$(2,2,-6)$ يمثّلان **نفس الخط** (الثاني ضِعف الأول). لكن $\lVert \mathbf{w} \rVert$ تضاعفت، فانكمش الهامش إلى النصف. **ولهذا** يجب **تثبيت المقياس** قبل المقارنة، ولهذا تظهر $=1$ في القيد $y_i(\mathbf{w}^T\mathbf{x}_i+b) \ge 1$ — إنها **تطبيع** لا شرطاً عشوائياً.

### Hard vs Soft Margin

| | **Hard margin** | **Soft margin** |
|:---|:---|:---|
| البيانات | **linearly separable** فقط | قابلة للخلط |
| المتغيّرات | — | **slack** $\xi_i \ge 0$ |
| الهدف | $\min \tfrac{1}{2}\lVert \mathbf{w} \rVert^2$ | $\min \tfrac{1}{2}\lVert \mathbf{w} \rVert^2 + C\sum \xi_i$ |
| المشكلة | نقطة شاذة واحدة تُفسد الحل | تحتاج ضبط $C$ |

**$C$:** صغير ← هامش واسع وتسامح أكثر · كبير ← يصرّ على تصنيف صحيح وهامش أضيق (**overfitting**).

### Kernel Trick — البيانات غير القابلة للفصل خطياً

لو لم يوجد مستوي فاصل في الفضاء الأصلي، **ارفع الأبعاد**:

$$\phi: \mathbf{x} \to \phi(\mathbf{x})$$

$$K(\mathbf{x}_i, \mathbf{x}_j) = \phi(\mathbf{x}_i)^T \phi(\mathbf{x}_j)$$

**الحيلة:** SVM لا يحتاج $\phi$ نفسها — بل **حاصل الضرب الداخلي** فقط. فـ$K$ تحسب النتيجة **بلا** بناء الفضاء العالي. ولهذا الرفع «مجاني» حسابياً.

| الـKernel | الصيغة |
|:---|:---|
| **Linear** | $\mathbf{x}_i^T \mathbf{x}_j$ |
| **Polynomial** | $(\gamma\, \mathbf{x}_i^T\mathbf{x}_j + r)^d$ |
| **RBF / Gaussian** | $\exp(-\gamma \lVert \mathbf{x}_i - \mathbf{x}_j \rVert^2)$ |

---

## 7. المقارنة — الجدول الذي يُحسم به السؤال

| | **KNN** | **Decision Tree** | **Naive Bayes** | **SVM** |
|:---|:---|:---|:---|:---|
| **نوع التعلّم** | Lazy · instance-based | Eager | Eager · probabilistic | Eager · geometric |
| **يبني نموذجاً؟** | ❌ لا | ✅ شجرة | ✅ احتمالات | ✅ مستوي + هامش |
| **يفسّر قراره؟** | ❌ | ✅ **قاعدة مقروءة** | جزئياً | ❌ صندوق أسود |
| **يحتاج تطبيعاً؟** | ✅ **إلزامي** | ❌ لا | ❌ لا | ✅ مفيد |
| **البيانات الرقمية** | ✅ طبيعي | يحتاج عتبات | يحتاج توزيعاً | ✅ طبيعي |
| **غير قابل للفصل خطياً** | ✅ يعمل | ✅ يعمل | ✅ يعمل | ✅ بـ**kernel** |
| **حساس للضجيج** | ✅ عالٍ | متوسط | منخفض | متوسط ($C$) |
| **القوة** | بسيط · بلا تدريب | **قابل للتفسير** | سريع · قليل البيانات | دقيق · أبعاد عالية |
| **الضعف** | بطيء عند السؤال · يحتاج ذاكرة كاملة | overfitting | افتراض استقلال خاطئ | لا يفسّر · يحتاج ضبط |

**قواعد الاختيار:**

- تريد **تفسيراً** للقرار (طب، قانون) ← **شجرة القرار**.
- **نصوص** أو أبعاد عالية ← **Naive Bayes** أو **SVM**.
- بيانات قليلة جداً ← **Naive Bayes**.
- **حدود معقّدة** ← **SVM بـkernel**.
- لا تريد تدريباً وتقبل بطء السؤال ← **KNN**.

---

## ✎ أسئلة — KNN والأشجار

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">1</span> **س1.** احسب مسافة الاستعلام $(4,2)$ إلى النقطة $(1,1)$، وهل يدخل في $k=3$؟

**الحل:**

$$d = \sqrt{(4-1)^2 + (2-1)^2} = \sqrt{9+1} = \sqrt{10} \approx \mathbf{3.162}$$

**الترتيب:** $P_2(2.000) < P_3,P_4,P_5(2.236) < P_6(3.000) < P_1(3.162)$.

النقطة $(1,1)$ هي **الأبعد** — فهي رقم **6** ولا تدخل في $k=3$ ولا $k=5$.

---

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">2</span> **س2.** لماذا يجب تطبيع الخصائص قبل KNN؟ أعطِ مثالاً عددياً.

**الحل:**

المسافة الإقليدية **تجمع فروقاً خامّة**. فعمود بمدى كبير يهيمن:

| النقطة | العمر | الراتب | 
|:---|:--:|:--:|
| $A$ | 30 | 1,000,000 |
| $B$ | 31 | 1,200,000 |
| $C$ | 60 | 1,000,000 |

$$d(A,B) = \sqrt{1^2 + 200{,}000^2} \approx 200{,}000$$
$$d(A,C) = \sqrt{30^2 + 0} = 30$$

**النتيجة:** $C$ (المختلف تماماً في العمر) أقرب **بستة آلاف مرّة** من $B$ — لأن **الراتب** سحق العمر. بعد التطبيع يتوازن الأمران.

**القاعدة:** **لا KNN بلا تطبيع.** هذه أول علامة في أي سؤال KNN.

---

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">3</span> **س3.** احسب $E(S)$ لفرع `Rain` (5 أمثلة: 3 Yes و2 No).

**الحل:**

$$p_+ = \frac{3}{5} = 0.6 \qquad p_- = \frac{2}{5} = 0.4$$

$$E = -(0.6)\log_2(0.6) - (0.4)\log_2(0.4)$$
$$= -(0.6)(-0.7370) - (0.4)(-1.3219)$$
$$= 0.4422 + 0.5288 = \mathbf{0.9710}$$

**لاحظ:** النتيجة **0.9710**، أي قريبة جداً من **1** (أقصى اختلاط) رغم أن النسبة 60/40 — لأن الإنتروبيا **شديدة الحساسية** قرب المنتصف.

---

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">4</span> **س4.** ليش ID3 اختار Outlook وليس Humidity، رغم أن Humidity قسّمت إلى قسمين فقط؟

**الحل:**

**عدد الأقسام ليس المعيار** — المعيار هو **المكسب في النقاء**:

| الخاصية | الأقسام | Gain |
|:---|:--:|:--:|
| **Outlook** | 3 | **0.2467** ✅ |
| Humidity | 2 | 0.1518 |

**السبب العميق:** `${Outlook}=\text{Overcast}$` أنتج فرعاً **نقياً تماماً** (4 Yes · 0 No، $E=0$) — أي **صفر اختلاط** كامل. وHumidity لم تُنتج أي فرع نقي (0.9852 و0.5917).

**الدرس:** ID3 يقيس **كم نقاءً كسبت**، لا **كم فرعاً صنعت**. تقسيم إلى فرعين نقيين أفضل من تقسيم إلى عشرة مختلطة.

---

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">5</span> **س5.** صنّف المثال `Sunny, Cool, High, Strong` بشجرة القرار، وتحقّق من الاتفاق مع Naive Bayes.

**الحل:**

**المسار في الشجرة:**

$$\text{Outlook}=\text{Sunny} \to \text{نذهب إلى عقدة Humidity}$$

$$\text{Humidity}=\text{High} \to \textbf{No}$$

**القرار: No.**

**مقارنة بـNB:** في القسم 5، NB أعطى **No** بثقة **85.4%**. **اتفقا.**

**شنو تتعلم:** خوارزميتان بمنطقين مختلفين (تقسيم حتمي ↔ احتمال) وصلتا لنفس الجواب. هذا **تحقّق متقاطع** — إن اختلفتا في الامتحان، **راجع حساباتك** قبل أن تشكّ في الخوارزمية.

---

## ✎ أسئلة — Bayes وSVM

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">6</span> **س6.** اكتب قاعدة بايز، وحدّد أي حدّ «قبل» وأيّها «بعد».

**الحل:**

$$P(C \mid X) = \frac{P(X \mid C)\, P(C)}{P(X)}$$

| الحدّ | الاسم | متى |
|:---|:---|:---|
| $P(C)$ | **Prior** | **قبل** رؤية المثال |
| $P(X \mid C)$ | **Likelihood** | يفسّر البيانات **داخل** الصنف |
| $P(C \mid X)$ | **Posterior** | **بعد** رؤية المثال |
| $P(X)$ | **Evidence** | ثابت لكل الأصناف ← **يُهمل** في المقارنة |

**ولهذا** نكتب $\propto$ بدل $=$: المقام لا يغيّر **أيّ** صنف يفوز.

---

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">7</span> **س7.** ليش NB «ساذج»؟ ولماذا يعمل رغم ذلك؟

**الحل:**

**ساذج** لأنه يفترض **الاستقلال الشرطي**:

$$P(x_1, x_2 \mid C) \approx P(x_1 \mid C)\,P(x_2 \mid C)$$

وهذا **غالباً خاطئ** — مثلاً `Humidity` و`Outlook` مترابطتان (الشمسي يميل للجفاف).

**لكنه يعمل** لسببين:
1. التصنيف يحتاج **ترتيب** الأصناف، لا **دقة** الاحتمالات. حتى لو كانت $P$ مغلوطة رقمياً، قد يبقى **الأعلى** هو الأعلى.
2. الضرب يبالغ في الثقة لكنه **يحافظ على الترتيب** في كثير من الحالات.

**الجملة الامتحانية:** «Naive Bayes is naive in its assumption but strong in its ranking — it needs the argmax to be right, not the probabilities to be calibrated.»

---

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">8</span> **س8.** ما الـsupport vectors؟ ولماذا هي وحدها المهمة؟

**الحل:**

**Support vectors** = النقاط **الأقرب** إلى المستوي الفاصل، التي **تلمس** حدود الهامش (تحقّق $y_i(\mathbf{w}^T\mathbf{x}_i + b) = 1$).

**لماذا هي وحدها؟** لأن المستوي يُحدَّد بمسألة:

$$\min \tfrac{1}{2}\lVert \mathbf{w} \rVert^2 \ \text{ s.t. } \ y_i(\mathbf{w}^T\mathbf{x}_i + b) \ge 1$$

القيود الفعّالة (**active constraints**) هي فقط التي عندها **تساوٍ** — أي الـsupport vectors. أي نقطة **خارج** الهامش لا تدخل في الحل.

**النتيجة العملية:** لو حذفت نقطة بعيدة، **لا يتغيّر** المستوي. ولو حرّكت support vector بمقدار صغير، **يتغيّر**.

---

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">9</span> **س9.** احسب الهامش لـ$\mathbf{w} = (3,4)$ و$b = -5$. ثم بيّن ماذا يحدث لو ضربنا الكل في 2.

**الحل:**

$$\lVert \mathbf{w} \rVert = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$$

$$\text{Margin} = \frac{2}{\lVert \mathbf{w} \rVert} = \frac{2}{5} = \mathbf{0.4}$$

**لو ضربنا الكل في 2:** $\mathbf{w} = (6,8)$ و$b = -10$.

$$\lVert \mathbf{w} \rVert = 10 \quad\Rightarrow\quad \text{Margin} = \frac{2}{10} = \mathbf{0.2}$$

**المستوي الهندسي نفسه** (لأن $\frac{\mathbf{w}^T\mathbf{x}+b}{\lVert\mathbf{w}\rVert}$ لم يتغيّر)، لكن الهامش **انكمش للنصف**.

**الدرس:** الهامش **ليس** خاصية هندسية للمستوي — بل خاصية **للمعايرة**. ولهذا يفرض SVM القيد $=1$: ليُثبّت المقياس ويجعل $\lVert\mathbf{w}\rVert$ ذات معنى.

---

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">10</span> **س10.** بيانات **غير** قابلة للفصل خطياً. اذكر حلّين، وبيّن أيّهما يفضّله SVM عملياً.

**الحل:**

| الحل | كيف | الثمن |
|:---|:---|:---|
| **Soft margin** | slack $\xi_i$ + معامل $C$ | يسمح بأخطاء **محدودة** |
| **Kernel trick** | $\phi(\mathbf{x})$ لرفع الأبعاد + $K$ | حساب أعلى · خطر overfitting |

**ما يفضّله SVM:** يبدأ بـ**kernel** (RBF عادةً) لأنه يحلّ **البنية** لا الأخطاء فقط؛ ويُضاف **soft margin** لتحمّل الضجيج والشواذ.

**عملياً:** الاثنان **يُستعملان معاً** — RBF + $C$ مضبوط. أي أن السؤال «أيّهما؟» جوابه: **ليس إمّا/أو**.

---

## 8. ورقة الصيغ

| العنصر | الصيغة |
|:---|:---|
| المسافة الإقليدية | $d = \sqrt{\sum (p_i - q_i)^2}$ |
| التطبيع min-max | $x' = \dfrac{x - \min}{\max - \min}$ |
| التقييس z-score | $x' = \dfrac{x - \mu}{\sigma}$ |
| الإنتروبيا | $E(S) = -\sum_i p_i \log_2 p_i$ |
| إنتروبيا ثنائية | $E = -p_+\log_2 p_+ - p_-\log_2 p_-$ |
| Information Gain | $Gain(S,A) = E(S) - \sum_v \frac{\lvert S_v\rvert}{\lvert S\rvert} E(S_v)$ |
| Bayes | $P(C\mid X) = \dfrac{P(X\mid C)P(C)}{P(X)}$ |
| NB (التصنيف) | $P(C\mid X) \propto P(C)\prod_i P(x_i\mid C)$ |
| Laplace smoothing | $P(x_i\mid C) = \dfrac{\text{count}+\alpha}{\text{count}(C) + \alpha\lvert V_i\rvert}$ |
| المستوي الفاصل | $\mathbf{w}^T\mathbf{x} + b = 0$ |
| الهامش | $\dfrac{2}{\lVert \mathbf{w} \rVert}$ |
| SVM (hard) | $\min \tfrac12\lVert\mathbf{w}\rVert^2$ s.t. $y_i(\mathbf{w}^T\mathbf{x}_i+b)\ge 1$ |
| SVM (soft) | $\min \tfrac12\lVert\mathbf{w}\rVert^2 + C\sum \xi_i$ |
| Kernel | $K(\mathbf{x}_i,\mathbf{x}_j) = \phi(\mathbf{x}_i)^T\phi(\mathbf{x}_j)$ |
| RBF kernel | $\exp(-\gamma\lVert\mathbf{x}_i-\mathbf{x}_j\rVert^2)$ |

---

## 9. مصائد الامتحان

| # | المصيدة | الجواب الآمن |
|:--:|:---|:---|
| 1 | KNN يبني نموذجاً | ❌ **lazy** — لا نموذج |
| 2 | KNN بلا تطبيع | ❌ **إلزامي** — الأعمدة الكبيرة تسحق غيرها |
| 3 | $k$ كبير = أفضل | ❌ يسبب **underfitting** |
| 4 | $k$ زوجي | ⚠️ يقبل التعادل — استعمل **فردياً** |
| 5 | ID3 يختار الخاصية بأقل أقسام | ❌ بأعلى **Gain** |
| 6 | $E = 1$ تعني نقاء | ❌ $E=1$ **أقصى اختلاط**؛ النقاء $E=0$ |
| 7 | تقسيم الفرع النقي | ❌ **توقّف** عند $E=0$ |
| 8 | Naive Bayes يتطلّب استقلالاً حقيقياً | ❌ يفترضه **ساذجاً** ويعمل رغم ذلك |
| 9 | $P(X)$ مهم للتصنيف | ❌ ثابت — يُهمل |
| 10 | صفر في likelihood = صفر نهائي | ❌ **Laplace smoothing** |
| 11 | الهامش $=\lVert\mathbf{w}\rVert$ | ❌ **$2/\lVert\mathbf{w}\rVert$** |
| 12 | تكبير $\lVert\mathbf{w}\rVert$ يوسّع الهامش | ❌ **تصغيره** يوسّعه |
| 13 | support vectors = كل النقاط | ❌ النقاط على حدود الهامش **فقط** |
| 14 | SVM بلا kernel يفصل أي بيانات | ❌ **linear** فقط |
| 15 | الشجرة الأعمق أدقّ | ❌ **overfitting** — الأقصر يعمّم |

---

## 10. ماذا يجب أن تكون قادراً عليه بعد هذا الفصل

| # | القدرة | المحكّ |
|:--:|:---|:---|
| 1 | تحسب مسافات KNN وترتّبها | وتُظهر تغيّر القرار مع $k$ |
| 2 | تبرّر التطبيع | بمثال عددي |
| 3 | تحسب $E(S)$ | 0.9403 لـPlayTennis |
| 4 | تحسب $Gain$ لكل خاصية | Outlook 0.2467 الأعلى |
| 5 | تبني شجرة ID3 | وتتوقّف عند $E=0$ |
| 6 | تشرح overfitting والتقليم | pre/post |
| 7 | تطبّق Bayes | prior · likelihood · posterior |
| 8 | تحسب NB كاملاً | 14.64% مقابل 85.36% |
| 9 | تُنعّم بالقاعدة | $\alpha=1$ |
| 10 | تحسب الهامش | $2/\lVert\mathbf{w}\rVert$ |
| 11 | تشرح support vectors | القيود الفعّالة |
| 12 | تفرّق hard/soft margin | و$C$ |
| 13 | تشرح kernel trick | بلا بناء الفضاء |
| 14 | تختار الخوارزمية المناسبة | مع التبرير |

---