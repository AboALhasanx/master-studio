### القسم 1 — What Is Risk?
#### ① النص الأصلي
> What Is Risk?
> The word risk is used here in its technical sense, where it is understood to mean
> the quantitative probability that an error situation occurs and gives rise to
> damage.
> In IT security, “damage” is synonymous with a breach of the security policy. It is
> important to understand that this is an objective definition of risk, which must not
> be confused with subjective risk, which also takes human factors such as public
> attitudes, trust and personality into consideration.
#### ② الترجمة
> «شنو يعني Risk؟
> كلمة risk تُستخدم هنا بمعناها التقني، حيث يُفهم منها أنها تعني الاحتمال الكمّي (quantitative probability) بأن تحدث حالة خطأ (error situation) وتؤدي إلى damage.
> في أمن تكنولوجيا المعلومات (IT security)، فإن «damage» مرادف لخرق سياسة الأمن (breach of the security policy). من المهم أن نفهم أن هذا تعريف موضوعي (objective definition) للخطر، ويجب ألّا يُخلط بينه وبين subjective risk، الذي يأخذ أيضًا في الحسبان العوامل البشرية مثل مواقف الجمهور (public attitudes) والثقة (trust) والشخصية (personality).»
#### ③ الشرح الفهمي
هنا الـ risk مو بالمعنى العامّي (يعني «مخاطرة» بشكل عائم)، إنما بمعنى تقني دقيق: هو احتمال كمّي (quantitative probability) إنه تصير حالة خطأ (error situation) وتؤدي لـ damage. يعني لازم عدنا رقم/احتمال محسوب، مو مجرد إحساس أو تخمين.

وبالـ IT security، كلمة damage تعني بالضبط breach of the security policy، أي خرق لسياسة الأمن. يعني مو أي ضرر مادي، إنما أي خرق للقواعد الأمنية المحدّدة.

نقطة الفرق المهمة: هذا تعريف objective (موضوعي)، أي يعتمد على واقع النظام نفسه وعلى الاحتمال المحسوب، مو على إحساس الناس. بينما subjective risk هو الخطر الشخصي اللي يعتمد على العوامل البشرية مثل مواقف الجمهور (public attitudes)، الثقة (trust)، والشخصية (personality).

| المصطلح | المعنى | يعتمد على شنو |
|---|---|---|
| objective risk | تعريف موضوعي: احتمال كمّي لحدوث error situation تسبب damage | واقع النظام نفسه (الاحتمال × الضرر) |
| subjective risk | تعريف شخصي للخطر | العوامل البشرية: attitudes, trust, personality |

الخلاصة: الكتاب يتبنّى التعريف الـ objective، والـ subjective خطر ثاني منفصل ما نخلط بينه وبينه.

---

### القسم 2 — Threat, Vulnerability and Damage (Fig. 3.1)
#### ① النص الأصلي
> In IT security, people say that damage occurs when a threat is realised against
> some weakness in the system. A weakness which can be exploited to damage
> the
> system is known as a vulnerability. This idea is illustrated in Fig. 3.1, where the
> threat is a shark and the vulnerability is a welding fault in the shark cage.
#### ② الترجمة
> «في أمن تكنولوجيا المعلومات (IT security)، يقول الناس إن damage يحدث عندما يتحقق threat ضد بعض نقاط الضعف في النظام. أما الضعف الذي يمكن استغلاله لإلحاق الضرر بالنظام فيُعرف باسم vulnerability. وتُوضّح هذه الفكرة في Fig. 3.1، حيث يكون threat عبارة عن قرش (shark) وتكون vulnerability عبارة عن عيب في اللحام (welding fault) في قفص القرش.»
![القرش والثغرة — Fig. 3.1|420](../06_Diagrams_&_Mindmaps/from_sharp_ch3/fig3_1_shark.png)
#### ③ الشرح الفهمي
الفكرة الأساسية هي سلسلة سببية (causal chain): damage ما يصير من فراغ، إنما يصير لمّا threat يتحقق ضد weakness موجودة بالنظام. وهذه الـ weakness اللي يمكن استغلالها لإلحاق الضرر اسمها vulnerability.

يعني الترتيب المنطقي هو:

damage ← تحقّق threat ضد vulnerability موجودة بالنظام

المثال التوضيحي (Fig. 3.1) ذكي جدًا وسهل تذكره:
- الـ threat = القرش (shark) — القوة الخارجية اللي تهدّد.
- الـ vulnerability = عيب اللحام (welding fault) بالقفص — الثغرة بالنظام.
- الـ damage = إنه القرش يدخل ويأذي الغوّاص — الضرر الناتج.

النقطة المهمة: لو ما عندنا vulnerability، ما يصير damage حتى لو موجود threat. لذلك الأمن كلّه يدور حول سدّ الثغرات.

| العنصر | معناه | بالمثال |
|---|---|---|
| Threat | قوة/حدث خارجي يهدّد النظام | القرش |
| Vulnerability | ضعف يمكن استغلاله | عيب اللحام بالقفص |
| Damage | الضرر الناتج من تحقّق threat | دخول القرش وإيذاء الغوّاص |

---

### القسم 3 — The Basic Risk, S = F × K, and the Risk Matrix
#### ① النص الأصلي
> The basic risk, S, of a threat depends on the frequency, F, of attempts to exploit
> the vulnerability and the consequences, K, of a successful attempt, as expressed
> in the equation:
> S
> F
> K
> =
> The relationship between these concepts is often visualized in the form of a so-
> called risk matrix. The result of the “multiplication” is indicated by a color code:
> Red indicates a high risk associated with the given threat. This arises when the
> consequences of a successful attack are high and the frequency of attempts to
> exploit the vulnerability is also high. The yellow areas indicate a medium level
> and the green areas a low level of risk.
#### ② الترجمة
> «الـ basic risk، أي S، لـ threat يعتمد على التكرار F لمحاولات استغلال الـ vulnerability، وعلى consequences، أي K، لمحاولة ناجحة، كما هو معبّر عنه في المعادلة:
> S = F K
> غالبًا ما تُصوَّر العلاقة بين هذه المفاهيم في شكل ما يُسمّى risk matrix. وتُبيَّن نتيجة «الضرب» عن طريق ترميز لوني (color code): اللون الأحمر يشير إلى خطر مرتفع (high risk) مرتبط بالـ threat المعطى. وهذا يحدث عندما تكون consequences الهجوم الناجح مرتفعة ويكون تكرار محاولات استغلال الـ vulnerability مرتفعًا أيضًا. أما المناطق الصفراء (yellow) فتشير إلى مستوى متوسط (medium)، والمناطق الخضراء (green) إلى مستوى منخفض (low) من الخطر.»
![مصفوفة الخطر — Frequency × Consequences|560](../06_Diagrams_&_Mindmaps/from_sharp_ch3/fig3_2_risk_matrix.png)
#### ③ الشرح الفهمي
الـ basic risk هو الخطر الأساسي قبل أي حماية. يتكوّن من حاصل ضرب عنصرين:

$$S = F \times K$$

| الرمز | المعنى |
|---|---|
| S | basic risk — الخطر الأساسي |
| F | frequency — تكرار محاولات استغلال الـ vulnerability |
| K | consequences — حجم الضرر الناتج من محاولة ناجحة |

يعني لو التكرار عالي والضرر عالي، الـ S يصير عالي. ولو واحد منهم واطي، الـ S ينزل. هاي الفكرة تُعرض بشكل بصري عبر الـ risk matrix:

- اللون الأحمر (Red) = خطر عالي. يحدث لمّا تكون الـ consequences عالية **و** التكرار F عالي بنفس الوقت.
- اللون الأصفر (Yellow) = مستوى متوسط (medium).
- اللون الأخضر (Green) = مستوى منخفض (low).

نقطة تذكّر: بالـ matrix، محور واحد يمثّل التكرار F والمحور الثاني يمثّل الضرر K، وكل threat يُوزَّع على المربّع اللي يوافق F وK تبعه.

---

### القسم 4 — Countermeasures and the Residual Risk, R = S / M
#### ① النص الأصلي
> The risk is reduced by introducing countermeasures (also known as controls),
> which must protect against the relevant threat. The reduced risk is known as the
> residual risk, R. If the threat is evaluated to give a risk S, and the level of
> countermeasures is M, then the residual risk is often defined by the equation:
> R
> S M
> =
> M covers both the number of countermeasures (there can be several things
> which affect the risk for particular types of attack) and their effectiveness. These
> relationships are often visualised in the form of a so-called residual risk matrix.
> The result of the “division” is again given by a colour code: A high residual risk
> from a given threat is indicated by a red colour. This arises when the risk is high
> and the level of countermeasures is low. As in the risk matrix, the yellow areas
> indicate a medium level and the green areas a low level of residual risk.
#### ② الترجمة
> «يُقلَّل الخطر بإدخال countermeasures (المعروفة أيضًا باسم controls)، والتي يجب أن تحمي من الـ threat المعني. ويُعرف الخطر المخفَّض باسم residual risk، أي R. وإذا تم تقييم الـ threat بحيث يعطي خطرًا S، وكان مستوى countermeasures هو M، فإن residual risk غالبًا ما يُعرَّف بالمعادلة:
> R = S / M
> والـ M يغطي كلاً من عدد countermeasures (يمكن أن تكون هناك عدة أمور تؤثّر في الخطر لأنواع معينة من الهجوم) وفعاليتها (effectiveness). وغالبًا ما تُصوَّر هذه العلاقات في شكل ما يُسمّى residual risk matrix. وتُعطى نتيجة «القسمة» مرة أخرى عبر ترميز لوني: ارتفاع الـ residual risk من threat معطى يُشار إليه باللون الأحمر. وهذا يحدث عندما يكون الخطر مرتفعًا ومستوى الـ countermeasures منخفضًا. وكما في risk matrix، تشير المناطق الصفراء إلى مستوى متوسط والمناطق الخضراء إلى مستوى منخفض من residual risk.»
![مصفوفة الخطر المتبقي — Risk ÷ Countermeasures|560](../06_Diagrams_&_Mindmaps/from_sharp_ch3/fig3_3_residual.png)
#### ③ الشرح الفهمي
لمّا ندخل countermeasures (أو controls)، الخطر ينزل من S إلى قيمة أقل اسمها residual risk = R. العلاقة معرّفة بـ:

$$R = \frac{S}{M}$$

| الرمز | المعنى |
|---|---|
| R | residual risk — الخطر المتبقي بعد الحماية |
| S | الخطر الأساسي (basic risk) قبل الحماية |
| M | level of countermeasures — مستوى الإجراءات الوقائية، ويشمل عددها (عدد countermeasures) + فعاليتها (effectiveness) |

فكرة القسمة مهمة: كل ما تكبر M (عدد أكثر + فعالية أعلى)، الـ R يصغر. وكل ما M صغير، الـ R يقرب من S.

والـ residual risk matrix تعرض هذا بصريًا:
- اللون الأحمر (Red) = residual risk عالي. يحدث لمّا يكون الخطر S عالي **و** مستوى countermeasures M واطي.
- اللون الأصفر (Yellow) = مستوى متوسط (medium).
- اللون الأخضر (Green) = مستوى منخفض (low) من residual risk.

نقطة تذكّر: الـ risk matrix تشتغل بالضرب (F × K)، بينما الـ residual risk matrix تشتغل بالقسمة (S ÷ M). الفرق بالمحاور: بدل ما نحطّ الـ consequences، نحطّ مستوى countermeasures.
