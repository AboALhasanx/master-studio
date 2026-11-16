---
title: "ملزمة AI · W01 — ما هو الذكاء الاصطناعي؟ والـagent"
subtitle: "AI definitions · Turing test · PEAS · environment properties · five agent types"
course: Artificial Intelligence
instructor: Dr. Saif Ali
term: Fall 2026
week: Week 01
---

# ما هو الذكاء الاصطناعي؟ والـagent

> **ليش هذا الفصل أول شي:** كل ما بعده (بحث، تعلّم، تحكّم) يفترض إنك عارف **شنو** تريد تصنع و**لمن**. الفصل يجاوب سؤالين: «شنو نسمّي ذكاءً؟» و«شنو هو الشيء الذي نبنيه؟» — والجواب الثاني اسمه **agent**.

---

## 1. أربع طرق لتعريف الذكاء الاصطناعي (ص 2)

كل تعريف في الأدبيات يجيب على سؤالين: **هل نحاكي الإنسان أم نعمل بعقلانية؟** و**هل نريد التفكير أم الفعل؟**

| | **إنساني (Human)** | **عقلاني (Rational)** |
|:---|:---|:---|
| **تفكير (Think)** | **Thinking Humanly** — علم الإدراك | **Thinking Rationally** — قوانين الفكر |
| **فعل (Act)** | **Acting Humanly** — اختبار تورنغ | **Acting Rationally** — الـ**agent العقلاني** |

**التعريفات الأصلية:**

| المصدر | التعريف |
|:---|:---|
| **Bellman, 1978** | «أتمتة الأنشطة المرتبطة بالتفكير البشري — القرار، حلّ المسائل، التعلّم» |
| **Charniak & McDermott, 1985** | «دراسة الملكات الذهنية عبر نماذج حسابية» |
| **Dean et al., 1995** | «تصميم ودراسة برامج تتصرف بذكاء — تتصرف كما يتصرف إنسان أو حيوان نعتبر سلوكه ذكياً» |
| **Haugeland, 1985** | «الجهد الجديد المثير لجعل الحاسوب يفكّر — آلات لها عقول» |

**🧠 مرساة:** التعريف الذي **يُبنى عليه المنهج كله** هو **Acting Rationally** — لأنه لا يسأل «هل تفكّر مثلنا؟» بل «هل تفعل الشيء الصحيح؟». وهذا قابل للقياس والبرمجة.

---

## 2. الطريقة 1 — Acting Humanly: اختبار تورنغ (ص 3)

**الفكرة:** حكم بشري يحاور **الحاسوب** و**إنساناً** عبر قناة نصّية. لو ما ميّز بينهما ← الحاسوب «يفكّر».

**ماذا يحتاج الحاسوب حتى ينجح؟** خمس قدرات، وهي في الحقيقة **خريطة المنهج**:

| القدرة | الفرع الذي يغطيها |
|:---|:---|
| **معالجة اللغة** | NLP |
| **تمثيل المعرفة** | Knowledge Representation |
| **الاستدلال** | Reasoning |
| **التعلّم** | Machine Learning |
| **سمات إنسانية** (مزاح، عاطفة) | — (لا تُختبر في تورنغ الأصلي) |

**الاختبار الحديث:** **Loebner Prize** — مسابقة سنوية (مثال: برنامج **Alice**، فاز 2000 و2001).

**⚠️ ما يقيسه تورنغ وما لا يقيسه:** يقيس **محاكاة السلوك**، لا **الوعي**. حاسوب يغشّ (يخفي كونه آلة) ينجح؛ إنسان يصرّح بأنه آلة يفشل. فالاختبار **سلوكي** بحت.

### حجّة الغرفة الصينية (Chinese Room)

**التجربة الذهنية:** أنت في غرفة، معك **كتب قواعد** ودفاتر ومراسم، وفتحتان. تُدخل لك رموز صينية، وتُخرج رموزاً صينية وفق القواعد — بلا فهم للغة.

| الطرف | ما يراه الخارج | ما يجري فعلاً |
|:---|:---|:---|
| الخارج | «الغرفة تفهم الصينية» | — |
| الداخل (أنت) | — | **تتبّع قواعد بلا فهم** |

**الاستنتاج (Searle):** التنفيذ الصحيح للقواعد **لا يُنتج فهم**اً. فالحاسوب الذي ينجح في تورنغ قد لا «يفهم» شيئاً.

**Lifesaver للامتحان:** حجّة الغرفة **اعتراض على تورنغ**، لا دليل على استحالة AI. وهي تخصّ **Acting Humanly**، ولا تُسقط **Acting Rationally** — لأن الأخير لا يدّعي الفهم أصلاً.

---

## 3. الطرق الثلاث الباقية (ص 4)

### Thinking Humanly

يحتاج معرفة **كيف يعمل الدماغ** فعلاً. مشكلاته الثلاث: **أي مستوى تجريد؟** · **كيف نتحقّق؟** · وهو **علم الإدراك (Cognitive Science)** لا هندسة.

### Thinking Rationally

بدأها **أرسطو** بـ**القواعد المنطقية**. مشكلتان: **ليس كل سلوك ذكي منطقياً** (الحدس، الإبداع) · و**ما هو هدف التفكير** أساساً؟

### Acting Rationally

**الفكرة:** اعمل لتحقيق هدف، بحسب ما تعرفه. والفعل العقلاني = الذي **يزيد احتمال بلوغ الهدف**.

$$\text{Rational} \ne \text{Omniscient} \quad\text{و}\quad \text{Rational} \ne \text{Clairvoyant}$$

**هذا التعريف هو المعتمد** في Russell & Norvig — وهو الأساس الذي يجعل «agent» ممكناً للبرمجة.

---

## 4. تاريخ قصير — ما يُسأل عنه (ص 5)

**مؤتمر Dartmouth، 1956** — البداية المؤسسية لـAI.

| العالم | إسهامه |
|:---|:---|
| **John McCarthy** | **LISP** · تطبيق المنطق على الاستدلال |
| **Marvin Minsky** | الشبكات العصبية · Slots and frames · *Society of the Mind* |
| **Claude Shannon** | شطرنج الحاسوب · نظرية المعلومات · juggling بخمس كرات |
| **Allen Newell & Herb Simon** | **General Problem Solver** |

**⚠️ مصيدة:** Dartmouth **1956** مو 1943 (McCulloch–Pitts) ولا 1950 (مقال تورنغ). اسأل نفسك: «شنو الحدث المؤسسي؟» ← المؤتمر.

---

## 5. PEAS — وصف المهمة قبل أي بناء (ص 7)

$$\boxed{\textbf{P}erformance \cdot \textbf{E}nviornment \cdot \textbf{A}ctuators \cdot \textbf{S}ensors}$$

| العنصر | السؤال |
|:---|:---|
| **P**erformance | شنو معيار النجاح؟ (قياس رقمي) |
| **E**nvironment | شنو العالم الذي يعمل فيه؟ |
| **A**ctuators | شنو أعضاؤه الفاعلة؟ |
| **S**ensors | شنو حواسّه؟ |

### مثال — سائق التاكسي

| العنصر | الصياغة |
|:---|:---|
| **P**erformance | **آمن · سريع · قانوني · مريح · مربح** |
| **E**nvironment | طرق، إشارات، مشاة، عملاء، طقس |
| **A**ctuators | مقود، دعسة، فرامل، إشارة، كلاكسون |
| **S**ensors | كاميرات، **sonar**، **laser/ladar**، عجلة القيادة، **odometer**، ميكروفون، GPS |

**🧠 مرساة:** **PEAS يُسأل عنه في كل امتحان تقريباً.** صيغته الثابتة: ابدأ بـ**P** (ما نريده) ثم **E** (ما يقاومنا) ثم **A/S** (كيف نؤثّر ونحسّ).

### Agent vs Object

- **الإنسان:** Sensors = عيون، آذان · Actuators (= effectors) = أيدي، أرجل، فم.
- **الروبوت:** Sensors = كاميرات، sonar، laser، ladar، bump · Effectors = grippers، manipulators، motors.

**السلوك يُوصف بدالة** تُحوّل **الإحساس إلى فعل**: $f: \text{percept} \to \text{action}$.

---

## 6. خصائص البيئة — الجدول الذي يُحفظ (ص 8)

سبع خصائص، وكل بيئة تُوصف بها:

| الخاصية | السؤال | الطرفان |
|:---|:---|:---|
| **Observable** | هل الـagent يرى كل الحالة؟ | Fully ↔ Partially |
| **Deterministic** | هل النتيجة محدّدة من الحالة والفعل؟ | Deterministic ↔ Stochastic (وتُكتب **Strategic** لو حسم الخصم) |
| **Episodic** | هل كل قرار مستقل؟ | Episodic ↔ Sequential |
| **Static** | هل العالم يتغيّر أثناء التفكير؟ | Static ↔ **Semi** ↔ Dynamic |
| **Discrete** | هل القيم معدودة؟ | Discrete ↔ Continuous |
| **Agents** | كم وكيلاً؟ | Single ↔ Multi |

### الجدول الرسمي — تسع بيئات (ص 8)

| البيئة | Observable | Deterministic | Episodic | Static | Discrete | Agents |
|:---|:--:|:--:|:--:|:--:|:--:|:--:|
| شطرنج بساعة | Fully | Strategic | Sequential | **Semi** | Discrete | Multi |
| شطرنج بلا ساعة | Fully | Strategic | Sequential | Static | Discrete | Multi |
| بوكر | **Partial** | Strategic | Sequential | Static | Discrete | Multi |
| Backgammon | Fully | **Stochastic** | Sequential | Static | Discrete | Multi |
| قيادة تاكسي | **Partial** | **Stochastic** | Sequential | **Dynamic** | **Continuous** | Multi |
| تشخيص طبي | **Partial** | **Stochastic** | **Episodic** | Static | **Continuous** | **Single** |
| تحليل صور | Fully | Deterministic | Episodic | Semi | Discrete | Single |
| التقاط قطع روبوتياً | Fully | Deterministic | Episodic | Semi | Discrete | Single |
| معلّم إنكليزي تفاعلي | Partial | Stochastic | Sequential | Dynamic | Discrete | Multi |

**لماذا الساعة تُغيّر Static؟**

$$\text{شطرنج بلا ساعة} = \textbf{Static} \quad\text{أما}\quad \text{شطرنج بساعة} = \textbf{Semi}$$

لأن الساعة **تجبرك على قرار قبل أن تنتهي من التفكير** — فالعالم يتغيّر (ينفد الوقت) أثناء تفكيرك. وهذا **Semi-dynamic** لا Dynamic كامل، لأن التغيّر **مقنّن** لا مستمر.

**⚠️ مصيدة:** كثيراً ما يُسأل «ليش البوكر **Static** والتاكسي **Dynamic**؟» — لأن البوكر **يتوقّف** أثناء تفكيرك (الدور ينتظرك)، والتاكسي **يستمر** (الطريق يتحرّك وأنت تفكّر).

---

## 7. أنواع الـagents الخمسة (ص 9–11)

مرتّبة **بالعمومية والقدرة** على التعامل مع بيئات معقّدة:

| # | النوع | الفكرة | القصور |
|:--:|:---|:---|:---|
| 1 | **Simple reflex** | قواعد `if–then` فقط | **قصير النظر** — لا يتذكّر ولا يخطّط |
| 2 | **Reflex with state** | يخزّن ما رآه سابقاً | لا يخطّط نحو هدف |
| 3 | **Goal-based** | هدف يوجّه الأفعال | **قد يغفل الكلفة** — كل الطرق تنجح |
| 4 | **Utility-based** | دالة فائدة $f(\text{state}) \to \text{value}$ | أغلى حسابياً |
| 5 | **Learning** | يتعلّم من التجربة | يحتاج بيانات ووقتاً |

### القالب الأول — Simple Reflex (ص 9)

$$\textbf{function } \text{SimpleReflexAgent}(\text{percept}):$$
$$\quad \text{state} \leftarrow \text{InterpretInput}(\text{percept})$$
$$\quad \text{rule} \leftarrow \text{RuleMatch}(\text{state}, \text{rules})$$
$$\quad \text{action} \leftarrow \text{RuleAction}(\text{rule})$$
$$\quad \textbf{return } \text{action}$$

### مثال — الـVacuum Agent

| العنصر | التفصيل |
|:---|:---|
| **Performance** | نقطة لكل مربّع يُنظَّف خلال $T$ · أو (مربّعات نظيفة − حركات) لكل خطوة |
| **Environment** | مربّعات، وسخ، مناطق متعددة |
| **Actions** | `left` · `right` · `suck` · `idle` |
| **Sensors** | الموقع والمحتوى — مثال: `[A, dirty]` |

**القاعدة (Simple Reflex):**

$$\text{if } \text{Dirty} \to \text{Suck} \quad\text{else if } \text{location}=A \to \text{Right} \quad\text{else} \to \text{Left}$$

**ثلاث جمل تُحفظ (ص 9):**

$$\text{Rational} \ne \text{Omniscient (البيئة قد تكون } \textbf{partial}\text{)}$$
$$\text{Rational} \ne \text{Clairvoyant (البيئة قد تكون } \textbf{stochastic}\text{)}$$
$$\therefore \text{Rational} \ne \text{always successful}$$

### القالب الثاني — Reflex with State (ص 10)

$$\textbf{function } \text{ReflexAgentWithState}(\text{percept}):$$
$$\quad \text{state} \leftarrow \text{UpdateState}(\text{state}, \text{action}, \text{percept})$$
$$\quad \text{rule} \leftarrow \text{RuleMatch}(\text{state}, \text{rules})$$
$$\quad \text{action} \leftarrow \text{RuleAction}(\text{rule})$$
$$\quad \textbf{return } \text{action}$$

**الفرق الوحيد:** سطر `UpdateState`. ويُمكّنه من **الاستدلال على ما لم يره** — مثال: «لو ما زرت المربّع الثاني أكثر من 3 وحدات ← اذهب إليه».

### Goal-based

الهدف **يعكس رغبات** الـagent، ويستطيع **إسقاط الأفعال** ليرى أيها يوصل للهدف. **العيبان:** يستغرق وقتاً، والعالم قد يتغيّر أثناء استدلاله.

### Utility-based

$$\text{Utility}: f(\text{state}) \to \text{value}$$

يفيد حين تتعارض الأهداف. **الفرق عن Goal-based:** الهدف يقول «أوصل»؛ الفائدة تقول «**أي طريق أفضل**». فالأول يفرّق بين **نجاح/فشل**، والثاني يفرّق بين **درجات النجاح**.

---

## ✎ أسئلة — التعريفات والـPEAS

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">1</span> **س1.** اذكر الطرق الأربع لتعريف AI، وأيّها معتمد في المنهج ولماذا.

**الحل:**

| | إنساني | عقلاني |
|:---|:---|:---|
| **تفكير** | Thinking Humanly | Thinking Rationally |
| **فعل** | Acting Humanly (تورنغ) | **Acting Rationally** ✅ |

**المعتمد: Acting Rationally**، لأنه لا يسأل عن الوعي ولا عن مطابقة الدماغ، بل عن **الفعل الصحيح** — وهو **قابل للقياس والبرمجة**. ومنه جاء اسم **rational agent**.

---

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">2</span> **س2.** صِغ PEAS لمعلّم لغة إنكليزية تفاعلي.

**الحل:**

| العنصر | الصياغة |
|:---|:---|
| **P**erformance | تحسّن الطالب في المفردات والقواعد · رضا الطالب · زمن الجلسة |
| **E**nvironment | الطالب، المنهج، تمارين، أخطاء شائعة |
| **A**ctuators | عرض نص/صوت، أسئلة، تلميحات، تصحيح |
| **S**ensors | إجابات الطالب، سرعة الاستجابة، تكرار الخطأ |

**لاحظ:** البيئة **partial** (لا نرى عقل الطالب) و**stochastic** (استجابته غير محدّدة) — ولهذا الـagent المناسب **utility-based** ثقيل الحساب، لا reflex.

---

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">3</span> **س3.** لماذا «عقلاني» لا تعني «ناجح دائماً»؟ أعطِ سببين.

**الحل:**

$$\text{Rational} \ne \text{Omniscient} \qquad \text{Rational} \ne \text{Clairvoyant}$$

1. **ليس علاّم الغيوب:** البيئة **partial** ← يبني قراره على **ما رآه**، وقد يكون هناك ما لم يره.
2. **ليس عرّافاً:** البيئة **stochastic** ← أفضل قرار **احتمالاً** قد يفشل.

**الخلاصة:** العقلانية هي **أفضل قرار في ضوء المعرفة المتاحة**، لا **أفضل نتيجة ممكنة**. وهذه الجملة تُكتب حرفياً في الامتحان.

---

## ✎ أسئلة — البيئة وأنواع الـagents

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">4</span> **س4.** صنّف بيئة **الشطرنج مع ساعة**، وبيّن لماذا **Semi-static**.

**الحل:**

| الخاصية | القيمة |
|:---|:---|
| Observable | **Fully** — كل القطع مرئية |
| Deterministic | **Strategic** — اللاعب الآخر يحدّد النتيجة |
| Episodic | **Sequential** — كل نقلة تؤثر على ما بعدها |
| Static | **Semi** |
| Discrete | **Discrete** |
| Agents | **Multi** |

**لماذا Semi:** الساعة **تفرض قيداً زمنياً**، فالعالم «يتغيّر» أثناء تفكيرك (ينفد وقتك). لكنه **ليس Dynamic** كالتاكسي، لأن التغيّر **مقنّن ومنتظم** لا مستمر.

**مقارنة سريعة:**

| | بلا ساعة | بساعة |
|:---|:--:|:--:|
| Static | Static | **Semi** |

---

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">5</span> **س5.** ما الفرق بين Simple reflex وReflex with state؟ وماذا يضيف كل منهما؟

**الحل:**

**الفرق سطر واحد في القالب:**

$$\text{SimpleReflex}: \text{state} \leftarrow \text{InterpretInput}(\text{percept})$$
$$\text{WithState}: \text{state} \leftarrow \textbf{UpdateState}(\text{state}, \text{action}, \text{percept})$$

| | Simple reflex | With state |
|:---|:---|:---|
| الذاكرة | **لا** | **نعم** |
| يرى | اللحظة الحالية فقط | اللحظة **وما مضى** |
| يستطيع | قاعدة واحدة | «زرت هذا المربّع قبل 3 خطوات» |
| القصور | **قصير النظر** | لا يخطّط نحو هدف |

**مثال:** Simple ← «لو وسخ: `Suck`». With state ← «لو ما زرت المربّع الآخر أكثر من 3 وحدات، اذهب إليه».

---

<span style="display:inline-block;min-width:1.5em;height:1.5em;line-height:1.5em;text-align:center;border-radius:50%;background:#dc2626;color:#ffffff;font-weight:700;font-size:0.85em;">6</span> **س6.** متى تحتاج **Utility-based** ولا يكفيك **Goal-based**؟

**الحل:**

**Goal-based** يفرّق بين شيئين فقط: **تحقّق الهدف** أو **لا**.

**Utility-based** يفرّق بين **درجات** تحقّق الهدف:

$$f(\text{state}) \to \text{value}$$

**مثال يوضّح الفرق:** هدفك «اذهب إلى المطار». المساران يوصلان — فالـgoal-based **لا يفرّق بينهما**. لكن مساراً كلفته 20 دقيقة وآخر 50 دقيقة ← الـ**utility** تختار الأول.

**القاعدة:** حين تتعارض الأهداف، أو حين تريد «أفضل» لا «مقبول» ← **utility**.

---

## 8. ورقة الصيغ والمصطلحات

| المصطلح | المعنى |
|:---|:---|
| **Agent** | كيان يُحسّ ويؤثّر: $f: \text{percept} \to \text{action}$ |
| **PEAS** | Performance · Environment · Actuators · Sensors |
| **Rational** | أفضل فعل بحسب المعرفة المتاحة |
| **Fully / Partially observable** | يرى كل الحالة / بعضها |
| **Deterministic / Stochastic / Strategic** | النتيجة محدّدة / عشوائية / يحدّدها الخصم |
| **Episodic / Sequential** | قرارات مستقلة / مترابطة |
| **Static / Semi / Dynamic** | لا يتغيّر / يتغيّر مقنّناً / يتغيّر باستمرار |
| **Discrete / Continuous** | معدود / مستمر |
| **Utility** | $f(\text{state}) \to \text{value}$ |
| **Turing test** | حكم بشري لا يميّز الآلة عن الإنسان |
| **Chinese Room** | تتبّع قواعد بلا فهم |

---

## 9. مصائد الامتحان

| # | المصيدة | الجواب الآمن |
|:--:|:---|:---|
| 1 | تورنغ يقيس الوعي | ❌ يقيس **محاكاة السلوك** |
| 2 | حجّة الغرفة تُسقط AI | ❌ تُسقط **Acting Humanly** فقط، لا Acting Rationally |
| 3 | Dartmouth 1950 | ❌ **1956** |
| 4 | Shannon = LISP | ❌ **McCarthy** = LISP · Shannon = شطرنج ونظرية معلومات |
| 5 | Rational = successful | ❌ ليس علاّم غيوب ولا عرّافاً |
| 6 | شطرنج بساعة = Dynamic | ❌ **Semi** |
| 7 | البوكر Dynamic | ❌ **Static** — الدور ينتظرك |
| 8 | التاكسي Static | ❌ **Dynamic** و**Continuous** |
| 9 | Goal-based = Utility-based | ❌ الأول نجاح/فشل، الثاني **درجات** |
| 10 | Simple reflex يتذكّر | ❌ **Reflex with state** هو الذي يتذكّر |
| 11 | تشخيص طبي Sequential | ❌ **Episodic** |
| 12 | PEAS يبدأ بالبيئة | ❌ يبدأ بـ**Performance** — ما نريد قياسه أولاً |

---

## 10. ماذا يجب أن تكون قادراً عليه بعد هذا الفصل

| # | القدرة | المحكّ |
|:--:|:---|:---|
| 1 | ترسم مصفوفة الطرق الأربع | تفكير/فعل × إنساني/عقلاني |
| 2 | تشرح اختبار تورنغ وقدراته الخمس | وتفرّقه عن الوعي |
| 3 | تلخّص حجّة الغرفة | وتحدّد ما تُسقطه |
| 4 | تذكر إسهامات الأربعة | McCarthy · Minsky · Shannon · Newell & Simon |
| 5 | تصوغ PEAS لأي مهمة | P أولاً |
| 6 | تصنّف أي بيئة بسبع خصائص | وتعطي جدولاً كاملاً |
| 7 | تفسّر Semi-static | الساعة |
| 8 | تفرّق الأنواع الخمسة | وبأي ترتيب تتزايد |
| 9 | تكتب قالب Simple reflex | وReflex with state |
| 10 | تفسّر لماذا العقلاني لا ينجح دائماً | partial + stochastic |

---
