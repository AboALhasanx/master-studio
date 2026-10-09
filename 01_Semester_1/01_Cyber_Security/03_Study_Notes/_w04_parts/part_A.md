### القسم 1 — Why history matters in cybersecurity

#### ① النص الأصلي

> Cryptography's history reads like an arms race between code-makers and code-breakers. Each epoch's "breakthrough" method was eventually broken by a new analytic technique, a faster computer, or a procedural slip. This history isn't trivia — it explains why today's controls look the way they do, which assumptions are safe (or unsafe), and how to reason quantitatively about security over time.
>
> At a high level, three transitions define the arc:
>
> - **Classical secrecy** → statistical cryptanalysis (frequency analysis topples substitution ciphers).
> - **Mechanical complexity** → operational cryptanalysis (Enigma's combinatorics beaten by procedure, capture, and clever automation).
> - **Mathematical hardness** → computational cryptanalysis (modern systems stand on well-studied hard problems and provable design goals until computing, math, or implementation mistakes catch up).
>
> Those transitions map directly to modern cybersecurity lessons:
>
> - Security is not only math — it's math ⨉ implementation ⨉ operations.
> - Keys (their entropy and handling) matter more than algorithms in many real failures.
> - "Unbreakable" is always contextual: it means "beyond the feasible work factor of realistic adversaries, within the asset's lifetime."

![الانتقالات الثلاثة في تاريخ التشفير|720](../06_Diagrams_&_Mindmaps/cy_w4_crypto_timeline.svg)

#### ② الترجمة

> «تاريخ التشفير يُقرأ كسباق تسلّح بين صانعي الشيفرة وكاسريها. كل «اختراق» في حقبة ما انتهى مكسورًا عبر تقنية تحليلية جديدة، أو حاسوب أسرع، أو زلة إجرائية. هذا التاريخ ليس معرفة هامشية — بل يفسّر لماذا تبدو ضوابط اليوم كما هي، وأي الافتراضات آمنة (أو غير آمنة)، وكيف نفكّر كمّيًا بشأن الأمن عبر الزمن.
>
> على المستوى العام، ثلاثة انتقالات ترسم المسار:
>
> - **السرية الكلاسيكية** ← التحليل الإحصائي للتشفير (تحليل التكرار يُسقط شيفرات الاستبدال).
> - **التعقيد الميكانيكي** ← التحليل التشغيلي للتشفير (تراكيب Enigma تُهزم بالإجراء والاستيلاء والأتمتة الذكية).
> - **الصعوبة الرياضية** ← التحليل الحسابي للتشفير (الأنظمة الحديثة تقف على مسائل صعبة مدروسة جيدًا وأهداف تصميم قابلة للإثبات حتى تلحق بها الحوسبة أو الرياضيات أو أخطاء التنفيذ).
>
> هذه الانتقالات تنعكس مباشرة على دروس الأمن السيبراني الحديثة:
>
> - الأمن ليس رياضيات فقط — بل رياضيات ⨉ تنفيذ ⨉ عمليات.
> - المفاتيح (إنتروبيتها وإدارتها) تهمّ أكثر من الخوارزميات في كثير من الإخفاقات الحقيقية.
> - «غير القابل للكسر» سياقي دائمًا: يعني «خارج عامل العمل الممكن للخصوم الواقعيين، ضمن عمر الأصل».»

#### ③ الشرح الفهمي

الفكرة الأساسية إن التشفير مو حالة ثابتة — هو صراع مستمر. كل ما يطلع طريقة تشفير قوية، تطلع بعدها طريقة تحليل تكسرها. لهذا ندرس التاريخ: مو لأنه معلومات قديمة، بل لأنه يفسّر ليش ضوابطنا الحالية مصمّمة بهذا الشكل، وأي افتراضات تكدر تعتمد عليها وأي لا.

الانتقالات الثلاثة هي جوهر الموضوع:

| المرحلة | شلون انكسرت | الدرس |
|---|---|---|
| السرية الكلاسيكية | تحليل التكرار (frequency analysis) | الشيفرة اللي تعتمد على سرّية الآلية تنكسر |
| التعقيد الميكانيكي (Enigma) | إجراء + استيلاء + أتمتة | التعقيد يأخّر التحليل بس ما يمنعه |
| الصعوبة الرياضية (الحديثة) | حوسبة / رياضيات / أخطاء تنفيذ | الأمان مسألة عامل عمل (work factor) |

والدروس الثلاثة تختصر فلسفة المادة كلها: (1) الأمن = رياضيات ⨉ تنفيذ ⨉ عمليات — يعني الخوارزمية وحدها ما تكفي. (2) المفتاح (entropy وإدارة) أهم من الخوارزمية بكثير من الإخفاقات الحقيقية. (3) كلمة «غير قابل للكسر» سياقية: تعني خارج قدرة الخصم الواقعي خلال عمر الأصل، مو مستحيل مطلقًا.

مثال عملي: لو خزّنت مفتاح ضعيف أو تسرّب المفتاح، خوارزمية AES القوية ما راح تنقذك. الهجوم غالبًا يجي على المفتاح أو على التنفيذ، مو على الخوارزمية نفسها.

---

### القسم 2 — 2.1 Caesar (shift) cipher

#### ① النص الأصلي

> The Caesar cipher replaces each letter $x$ (encoded 0–25) with $(x + k) \bmod 26$, using the encryption and decryption functions shown below.
>
> Why it fails:
>
> - Tiny keyspace (25 nontrivial keys).
> - Preserved statistics: letter frequencies and diagram patterns leak the shift.
> - Automatable attacks: exhaustive search or frequency analysis recover $k$ in milliseconds.
>
> Cybersecurity lesson: Small keyspaces and preserved structure are fatal. Any scheme that fails to obscure plaintext statistics is brittle once an adversary can collect enough ciphertext.

$$E(x) = (x + k) \bmod 26 \qquad D(x) = (x - k) \bmod 26$$

| Symbol | Meaning |
|---|---|
| $x$ | letter encoded 0–25 |
| $k$ | shift / key |

#### ② الترجمة

> «شيفرة قيصر تستبدل كل حرف $x$ (مُرمَّز 0–25) بـ $(x + k) \bmod 26$، باستخدام دالتي التشفير وفكّ التشفير الموضّحتين أدناه.
>
> لماذا تفشل:
>
> - فضاء مفاتيح ضئيل (25 مفتاحًا غير تافه).
> - إحصاءات محفوظة: تكرارات الحروف وأنماط الثنائيات تسرّب الإزاحة.
> - هجمات قابلة للأتمتة: البحث الشامل أو تحليل التكرار يستعيدان $k$ خلال ميلي ثانية.
>
> درس الأمن السيبراني: فضاءات المفاتيح الصغيرة والبنية المحفوظة قاتلة. أي مخطط يفشل في إخفاء إحصاءات النص الأصلي يصبح هشًّا بمجرد أن يجمع الخصم نصًّا مشفّرًا كافيًا.»

#### ③ الشرح الفهمي

شيفرة قيصر أبسط أنواع الاستبدال: كل حرف تزيحه بعدد ثابت $k$. مثلاً بـ $k = 3$: يتحوّل A ← D، و B ← E، وهكذا. والتشفير وفكّ التشفير عكس بعض تمامًا — الإزاحة والرجوع عنها.

ليش تنكسر؟

1. فضاء المفاتيح صغير جدًا — 25 احتمال غير تافه بس، يعني تكدر تجرّبهم كلهم بالثواني (brute force).
2. ما تخفي إحصاءات اللغة — تكرار حرف E بالإنجليزية يبقى ظاهر بس مزيّح، فـ frequency analysis يكتشف الإزاحة بسرعة.
3. قابلة للأتمتة بالكامل — حاسوب بسيط يستعيد $k$ بميلي ثانية.

| الخاصية | قيصر |
|---|---|
| نوع الشيفرة | substitution (monoalphabetic) |
| فضاء المفاتيح | 25 مفتاحًا غير تافه |
| هل يخفي التكرار؟ | لا |
| طريقة الكسر | brute force / frequency analysis |

ملاحظة أمانة: بالنص الأصلي مكتوب `mode` بدل `mod` بالمعادلة الثانية — الصحيح `mod` (باقي القسمة على 26)، وهي الصيغة الصحيحة المعروضة أعلاه.

الدرس: أي شيفرة ما تخفي إحصاءات النص الأصلي تكون هشّة بمجرد ما يجمع المهاجم نص مشفّر كافي.

---

### القسم 3 — 2.2 Vigenère (polyalphabetic) cipher

#### ① النص الأصلي

> Vigenère uses a repeated key $K$ to apply different Caesar shifts per position.
>
> For centuries this looked "unbreakable" because a single frequency distribution no longer sufficed — each key position induced its own distribution. But Kasiski examination and Friedman's index of coincidence reveal the key length. Once the period is known, the cipher reduces to multiple Caesar problems.
>
> Cybersecurity lesson: Adding complexity (multiple alphabets) can delay, not prevent, analysis. Attackers evolve; security that relies on secrecy of mechanism rather than work factor erodes with time.

$$C_i = (P_i + K_i) \bmod 26$$

| Symbol | Meaning |
|---|---|
| $C_i$ | ciphertext letter at position $i$ |
| $P_i$ | plaintext letter at position $i$ |
| $K_i$ | key letter at position $i$ (from the repeated keyword) |

#### ② الترجمة

> «فيجينير يستخدم مفتاحًا متكرّرًا $K$ لتطبيق إزاحات قيصر مختلفة لكل موضع.
>
> لقرون بدا هذا «غير قابل للكسر» لأن توزيع تكرار واحد لم يعد كافيًا — كل موضع مفتاح أنتج توزيعه الخاص. لكن فحص كاسيسكي ومؤشّر التطابق لفريدمان يكشفان طول المفتاح. وبمجرد معرفة الدورة، تتحوّل الشيفرة إلى عدة مسائل قيصر.
>
> درس الأمن السيبراني: إضافة التعقيد (أبجديات متعددة) يمكن أن تؤجّل التحليل لا أن تمنعه. المهاجمون يتطوّرون؛ والأمن الذي يعتمد على سرّية الآلية بدل عامل العمل يتآكل مع الزمن.»

#### ③ الشرح الفهمي

فيجينير تطوّر على قيصر: بدل إزاحة واحدة ثابتة، تستخدم كلمة مفتاحية (keyword) وتكرّرها. كل حرف من النص يُشفّر بإزاحة مختلفة حسب الحرف المقابل من الكلمة. مثلاً keyword = KEY تعني إزاحات 10, 4, 24, 10, 4, 24... وهكذا دواليك.

لهذا حيّرت الناس لقرون: تحليل التكرار العادي ما ينفع، لأن كل موضع من المفتاح يعطي توزيع مختلف، فيتوزّع تكرار الحرف الواحد على عدة أبجديات (polyalphabetic).

شلون تنكسر؟

- **Kasiski examination**: يكتشف طول المفتاح (period) عن طريق تكرار مقاطع متطابقة بالنص المشفّر.
- **Friedman's index of coincidence (IC)**: يقيس انتظام التوزيع ويقدّر طول المفتاح إحصائيًا.
- بعد معرفة الطول، الشيفرة تنفصل إلى عدة مسائل قيصر مستقلة — كل واحدة تنكسر بتحليل التكرار العادي.

| الخوارزمية | المفتاح | الإزاحة لكل موضع |
|---|---|---|
| Caesar | حرف واحد (رقم) | ثابتة |
| Vigenère | كلمة مفتاحية متكرّرة | تتغيّر حسب الحرف |

نقطة توضيح مهمة: **Caesar و Vigenère الاثنان symmetric** — يعني مفتاح واحد يُستخدم للتشفير وفكّ التشفير. الفرق الحقيقي بينهم هو إن Vigenère يستخدم keyword متكرّر (إزاحة مختلفة لكل موضع)، مو إنه «asymmetric».

الدرس: التعقيد (أبجديات متعددة) يأخّر التحليل بس ما يمنعه. والأمن اللي يعتمد على سرّية الآلية بدل عامل العمل يتآكل مع الزمن.

---

### القسم 4 — 2.3 A quantitative view: unicity distance

#### ① النص الأصلي

> Claude Shannon formalized why classical ciphers break under enough ciphertext. The unicity distance $U$ estimates how many characters an attacker needs, on average, to determine a unique key given language redundancy.
>
> - $H(K)$: key entropy (bits).
> - $D$: redundancy of the language (bits/character; English ≈ 1–1.5).
>
> Example: A monoalphabetic substitution cipher's keyspace is $26!$ (about $2^{88}$ possibilities). With English redundancy $D \approx 1.5$, $U \approx 88/1.5 \approx 59$ characters. In other words, mere paragraphs suffice, in principle, to uniquely determine the key.
>
> Cybersecurity relevance: Even without computers, statistics break systems once the ciphertext exceeds $U$. Modern designs strive to ensure $U$ is effectively unreachable within an asset's lifetime and bandwidth.

$$U \approx \frac{H(K)}{D}$$

| Symbol | Meaning |
|---|---|
| $U$ | unicity distance (characters) |
| $H(K)$ | key entropy in bits |
| $D$ | redundancy of the language (bits/char; English ≈ 1–1.5) |

#### ② الترجمة

> «كلود شانون صاغ رياضيًا لماذا تنكسر الشيفرات الكلاسيكية عند وجود نص مشفّر كافٍ. مسافة الوحدانية $U$ تقدّر عدد الأحرف التي يحتاجها المهاجم، في المتوسط، لتحديد مفتاح وحيد بالنظر إلى تكرارية اللغة.
>
> - $H(K)$: إنتروبيا المفتاح (بت).
> - $D$: تكرارية اللغة (بت/حرف؛ الإنجليزية ≈ 1–1.5).
>
> مثال: فضاء مفاتيح شيفرة الاستبدال أحادية الأبجدية هو $26!$ (حوالي $2^{88}$ احتمالًا). مع تكرارية إنجليزية $D \approx 1.5$، فإن $U \approx 88/1.5 \approx 59$ حرفًا. بعبارة أخرى، فقرات بسيطة تكفي مبدئيًا لتحديد المفتاح بشكل وحيد.
>
> الأهمية السيبرانية: حتى دون حواسيب، الإحصاء يكسر الأنظمة بمجرد أن يتجاوز النص المشفّر $U$. التصاميم الحديثة تسعى لجعل $U$ غير قابل للوصول فعليًا ضمن عمر الأصل وعرض النطاق.»

#### ③ الشرح الفهمي

شانون سأل سؤال ذكي: كم حرف مشفّر يحتاج المهاجم حتى يصير عنده مفتاح وحيد صحيح؟ الجواب هو unicity distance، ورمزه $U$.

المعادلة أعلاه تقول: $U$ = إنتروبيا المفتاح ÷ تكرارية اللغة. يعني:

| الرمز | المعنى |
|---|---|
| $U$ | مسافة الوحدانية (بالأحرف) |
| $H(K)$ | إنتروبيا المفتاح (بت) — كم بت من العشوائية بالمفتاح |
| $D$ | تكرارية اللغة (redundancy، بت/حرف) — الإنجليزية ≈ 1–1.5 |

المعنى المنطقي: كل ما المفتاح أكبر إنتروبيا ($H(K)$ أكبر) أو اللغة أقل تكرارية ($D$ أقل)، كل ما احتاج المهاجم نص مشفّر أكثر حتى يثبّت المفتاح الوحيد.

المثال المحسوب خطوة بخطوة:

- شيفرة الاستبدال أحادية الأبجدية عندها $26!$ مفتاح ممكن.
- $\log_2(26!) \approx 88$ بت، يعني $H(K) \approx 88$ بت.
- اللغة الإنجليزية $D \approx 1.5$ بت/حرف.
- إذن $U \approx 88 / 1.5 \approx 59$ حرف.

يعني حوالي فقرة صغيرة تكفي نظريًا لتحديد المفتاح الوحيد — مو نص طويل. لهذا الشيفرات الكلاسيكية تنكسر بسهولة بالنص الكافي، حتى بدون حاسوب.

الأهمية السيبرانية: التصاميم الحديثة تحاول تخلي $U$ كبيرة جدًا لدرجة مستحيلة الوصول خلال عمر الأصل — يعني عمليًا تحتاج نص مشفّر أكبر من اللي راح يجمعه المهاجم بحياته، وهذا اللي يحمي النظام.
