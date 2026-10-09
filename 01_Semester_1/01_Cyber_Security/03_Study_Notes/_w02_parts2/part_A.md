### القسم 1 — What Is Risk?
#### ① النص الأصلي
> In its technical sense, the word risk means the quantitative probability that an error situation occurs and gives rise to damage. In IT security, "damage" is synonymous with a breach of the security policy. This is an objective definition of risk, which must not be confused with subjective risk — the latter also takes human factors such as public attitudes, trust and personality into consideration.

#### ② الترجمة
> «بمعناها التقني، تعني كلمة risk الاحتمال الكمّي (quantitative probability) بأن تحدث حالة خطأ وتؤدي إلى damage. وفي IT security، فإن "damage" مرادفة لخرق الـ security policy. وهذا تعريف objective للخطر، ويجب عدم الخلط بينه وبين الـ subjective risk — فالأخير يأخذ بنظر الاعتبار أيضاً العوامل البشرية مثل المواقف العامة (attitudes) والثقة (trust) والشخصية (personality).»

#### ③ الشرح الفهمي
الـ risk بمعناه التقني مب مجرد "خطر" بالمعنى العام. هو رقم — احتمال (probability) محسوب — إنه يصير خطأ وبعدين ينتج منه damage.

وبـ IT security، شو يعني damage؟ يعني صار breach للـ security policy، يعني تجاوزنا القواعد الأمنية المتفق عليها.

أكو نوعين لازم نفرّق بينهم:

| النوع | يعتمد على | مثال |
|---|---|---|
| objective risk | أرقام وحقائق قابلة للقياس | احتمال إن ينجح هجوم معيّن |
| subjective risk | العوامل البشرية: attitudes، trust، personality | إحساس المستخدم بالخوف أو الثقة |

نقطة مهمة: تعريفنا هنا objective — يعني محسوب ومحدّد بالأرقام، مب مبني على رأي أحد.

---

### القسم 2 — The Threat / Vulnerability / Damage Chain (Fig. 3.1)
#### ① النص الأصلي
> In IT security, damage occurs when a threat is realised against some weakness in the system. A weakness which can be exploited to damage the system is known as a vulnerability. Fig. 3.1 illustrates this idea, where the threat is a shark and the vulnerability is a welding fault in the shark cage.

![القرش والثغرة — Fig. 3.1|300](../06_Diagrams_&_Mindmaps/from_sharp_ch3/fig3_1_shark.png)

#### ② الترجمة
> «في IT security، يحدث الـ damage عندما يتحقق threat ضد ضعف ما في النظام. والضعف الذي يمكن استغلاله لإلحاق الضرر بالنظام يُعرف بالـ vulnerability. ويوضّح Fig. 3.1 هذه الفكرة، حيث الـ threat هو قرش (shark) والـ vulnerability هي عيب في اللحام (welding fault) في قفص القرش.»

#### ③ الشرح الفهمي
السلسلة تمشي هيك: threat ← vulnerability ← damage.

- threat: القوة أو الجهة اللي تحاول تضر.
- vulnerability: نقطة ضعف بالنظام قابلة للاستغلال.
- damage: النتيجة — خرق الـ security policy.

مثال القرش (Fig. 3.1) يوضّح كل شي:

| بالتشبيه | بالـ IT | المعنى |
|---|---|---|
| القرش | threat | المهاجم / القوة الخارجية |
| عيب اللحام بالقفص | vulnerability | الثغرة في النظام |
| القفص | النظام نفسه | اللي المفروض يحميك |
| الغوّاص جوّه | الـ asset | اللي يتضرر فعلاً |

الفكرة الأساسية: الضرر ما يصير بمجرد وجود قرش — لازم يكون أكو ثغرة (welding fault) يستغلها. لو القفص سليم، القرش موجود بس ما يأثر عليك.

---

### القسم 3 — Basic Risk S = F × K and the Risk Matrix
#### ① النص الأصلي
> The basic risk, S, of a threat depends on the frequency, F, of attempts to exploit the vulnerability and the consequences, K, of a successful attempt, as expressed in the equation:
>
> $$S = F \times K$$
>
> These concepts are often visualized in a so-called risk matrix, where the result of the "multiplication" is indicated by a colour code: red indicates a high risk associated with the given threat, arising when both the consequences of a successful attack and the frequency of attempts to exploit the vulnerability are high. The yellow areas indicate a medium level and the green areas a low level of risk.

![مصفوفة الخطر — Frequency × Consequences|400](../06_Diagrams_&_Mindmaps/from_sharp_ch3/fig3_2_risk_matrix.png)

#### ② الترجمة
> «الخطر الأساسي S لأي threat يعتمد على التكرار F لمحاولات استغلال الـ vulnerability، وعلى العواقب K لمحاولة ناجحة، كما في المعادلة: S = F × K. وهذه المفاهيم غالباً ما تُصوَّر على شكل ما يسمى risk matrix، حيث تُشار إلى نتيجة "الضرب" برمز لوني: الأحمر يعني خطراً عالياً مرتبطاً بالـ threat المعني، وينشأ عندما تكون العواقب المترتبة على هجوم ناجح عالية وكذلك تكرار محاولات استغلال الـ vulnerability عالياً. والمناطق الصفراء تعني مستوى متوسطاً، والخضراء مستوى منخفضاً من الخطر.»

#### ③ الشرح الفهمي
الـ basic risk S يطلع من ضرب شيئين: شكد يهجمون عليك (F)، وشكد يضرّونك لو نجحوا (K).

$$S = F \times K$$

| الرمز | الاسم | المعنى |
|---|---|---|
| S | Risk | الخطر الأساسي (basic risk) |
| F | Frequency | تكرار محاولات استغلال الثغرة |
| K | Consequences | حجم الضرر إذا نجحت المحاولة |

يعني لو F عالي (يهجمون عليك هواي) و K عالي (إذا نجح يخرّب هواي)، راح يصير S عالي.

الـ risk matrix تحوّل هذي الأرقام إلى لون:

| اللون | المستوى | متى يطلع |
|---|---|---|
| أحمر | عالي (high) | F عالي و K عالي |
| أصفر | متوسط (medium) | واحد منهم عالي والثاني متوسط |
| أخضر | منخفض (low) | F و K الاثنين واطيين |

الفكرة: كل threat نحدّده على المصفوفة حسب موقعه بـ F و K، واللون يخبرنا بسرعة بأولوية الاهتمام.

---

### القسم 4 — Countermeasures and Residual Risk R = S / M
#### ① النص الأصلي
> The risk is reduced by introducing countermeasures (also known as controls), which must protect against the relevant threat; the reduced risk is known as the residual risk, R. If the threat is evaluated to give a risk S, and the level of countermeasures is M, then the residual risk is often defined by the equation:
>
> $$R = \frac{S}{M}$$
>
> M covers both the number of countermeasures (there can be several things which affect the risk for particular types of attack) and their effectiveness. These relationships are often visualised in a so-called residual risk matrix, where the result of the "division" is again given by a colour code: a high residual risk from a given threat is indicated by red, arising when the risk is high and the level of countermeasures is low. As in the risk matrix, yellow indicates a medium level and green a low level of residual risk.

![مصفوفة الخطر المتبقي — Risk ÷ Countermeasures|400](../06_Diagrams_&_Mindmaps/from_sharp_ch3/fig3_3_residual.png)

#### ② الترجمة
> «يُقلَّل الخطر بإدخال countermeasures (وتُعرف أيضاً بالـ controls)، التي يجب أن تحمي من الـ threat المعني؛ والخطر بعد التقليل يُعرف بالـ residual risk أي R. وإذا قُيّم الـ threat ليعطي خطراً S، وكان مستوى الـ countermeasures هو M، فإن الـ residual risk يُعرَّف غالباً بالمعادلة: R = S / M. ويشمل M كلاً من عدد الـ countermeasures (إذ يمكن أن تكون هناك عدة أمور تؤثر على الخطر لأنواع معينة من الهجوم) وفاعليتها. وهذه العلاقات غالباً ما تُصوَّر على شكل ما يسمى residual risk matrix، حيث تُعطى نتيجة "القسمة" مرة أخرى برمز لوني: الخطر المتبقي العالي من threat معين يُشار إليه بالأحمر، وينشأ عندما يكون الخطر عالياً ومستوى الـ countermeasures واطئاً. وكما في risk matrix، يشير الأصفر إلى مستوى متوسط والأخضر إلى مستوى منخفض من الـ residual risk.»

#### ③ الشرح الفهمي
الـ countermeasures (أو controls) هي كل شي نضيفه لنقلّل الخطر — firewall، antivirus، encryption، backup، تدريب الموظفين... إلخ.

الخطر بعد ما نضيف الحماية يصير اسمه residual risk (R):

$$R = \frac{S}{M}$$

| الرمز | الاسم | المعنى |
|---|---|---|
| R | Residual risk | الخطر المتبقي بعد الحماية |
| S | Risk | الخطر الأساسي |
| M | Level of countermeasures | مستوى الحماية، ويشمل العدد + الفاعلية |

نقطة مهمة: M مب بس "عدد" الحمايات، لا — يشمل العدد و effective لكل واحدة. عشر جدران حماية ضعيفة يمكن تكون أقل فاعلية من واحد قوي.

الـ residual risk matrix:

| اللون | المستوى | متى يطلع |
|---|---|---|
| أحمر | عالي (high) | S عالي و M واطي |
| أصفر | متوسط (medium) | في توازن بين S و M |
| أخضر | منخفض (low) | S واطي أو M عالي |

الفكرة النهائية: ما يمكن نوصل خطر صفر. دايماً يبقى residual risk، والمهم نخليه ضمن مستوى مقبول (acceptable level).
