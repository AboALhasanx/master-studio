# 03 — كل ما يفيدنا لهذا الجابتر (Everything Useful)
### ASE · Chapter 5 · Software Design — مسح شامل لكل الملفات

> **شنو هذا الملف:** نتيجة فحصي **لكل** ملف بالمجلد. لقيت 3 بنوك أسئلة + 19 ورقة امتحان + توتوريالز + ملفات دراسة سابقة. هذا الملف يجمع **كل سؤال خارجي يخص الديزاين** + **المحتوى الأعمق** اللي ما موجود بالسلايدات.
> **القيمة:** هذا هو الفرق بين "مذاكرة من السايدات" و"مذاكرة من كل شي موجود".

---

## الجزء 1 — المصادر اللي فحصتها (الجرد الكامل)

| المصدر | الموقع | شنو لقيت |
|---|---|---|
| بنك SEPM ModuleWise | `02_Raw_Materials/Question_Banks/` | 5 موديولات — تشمل تصميم جزئياً |
| بنك NRCMEC UnitWise | `02_Raw_Materials/Question_Banks/` | **Unit III = Design Engineering — 20 سؤال + مستويات Bloom (BT)** |
| بنك GitHub (KPRIT) | `02_Raw_Materials/Question_Banks/` | **Part A/B/C — Unit III تصميم، مع تصنيف Bloom** |
| 19 ورقة امتحان MRCET | `Aggarwal_Singh_Slides/exam_papers/02_Exam_Question_Papers/` | **أسئلة تصميم بصيغة امتحان حقيقي (7M/14M)** |
| 5 توتوريالز MAIT ETCS-252 | `exam_papers/01_MAIT_ETCS252_Tutorials/` | **MCQ حقيقية على coupling/cohesion/OOD** |
| ملاحظات ساندبوكس سابقة | `05_Seminars_&_Slides/_sandbox_trial/` | **شرح أعمق بكثير** (fan-in/out, layered design, depth/width) + corpus الكتب |

---

## الجزء 2 — أسئلة MCQ خارجية على الديزاين (مع الأجوبة)

**من توتوريالز MAIT (أسئلة حقيقية متعددة الخيارات):**

| # | السؤال | الجواب |
|---|---|---|
| Q2 | The worst type of coupling is: Data / Control / Stamp / **Content** | Content |
| Q9 | Modules X and Y operate on the **same input and output data**, then the cohesion is: Sequential / **Communicational** / Procedural / Logical | Communicational |
| Q16 | The **desired** level of coupling is: No coupling / Control / Common / **Data** | Data |
| Q19 | Coupling and cohesion can be represented using a: cause-effect graph / dependence matrix / **Structure chart** / SRS | Structure chart |
| Q23 | The feature of the OO paradigm which helps **code reuse** is: object / class / **inheritance** / aggregation | Inheritance |
| Q29 | An object encapsulates: Data / Behaviour / State / **Both Data and behaviour** | Both |
| Q31 | Aggregation represents: is_a / **part_of** / composed_of / none | part_of |
| Q39 | Structured charts are a product of: requirements gathering / requirements analysis / **design** / coding | Design |
| Q42 | Pseudocode can replace: **flowcharts** / structure charts / decision tables / cause-effect graphs | Flowcharts |
| Q61 | **Top-down** approach is used for: development / identification of faults / **testing and validation** / reverse engineering | testing and validation |
| Q15 | Which is true: ADTs = classes / ADTs don't allow inheritance / classes can't inherit same base / **Objects have state and behaviour** | Objects have state and behaviour |

**من بنك NRCMEC — Unit III (Design Engineering) مع مستوى Bloom:**

| # | السؤال | BT |
|---|---|---|
| 1 | Write brief notes on **data design**. | L1 |
| 5 | Define **design process**. | L1 |
| 6 | List the **principles of software design**. | L1 |
| 9 | What are the **goals of the design process**? | L1 |
| 12 | **Draw and explain sequence diagrams** with an example. | L1 |
| 14 | Explain: i) **Class diagrams** ii) **Sequence diagrams**. | L3 |
| 17 | Define software architecture. Explain why it may be necessary to design system architecture **before** specifications. **Compare function-oriented and object-oriented designs.** | L1 |
| 18 | Explain: i) **Collaboration diagrams** ii) **Use case diagrams**. | L3 |
| 15 | Discuss about **mapping data flow into software architecture**. | L1 |

**من بنك GitHub (KPRIT) — Unit III، Part A/B/C:**

| # | السؤال | Bloom |
|---|---|---|
| A5 | Justify the importance of **refactoring**? | Understand |
| A6 | Discuss on **low coupling**? | Understand |
| A10 | **Compare function oriented and object oriented design**? | Understand |
| A11 | Define **top-down and bottom-up** design model? | Knowledge |
| A12 | Write short notes on **coupling**? | Knowledge |
| A14 | Write short notes on **cohesion**? | Knowledge |
| A19 | List out all the **design issues**? | Understand |
| B1 | Explain a **two-level process**. Why should system design be finished **before** detailed design, rather than starting detailed design after requirements specification? Explain with example. | Knowledge |
| B2 | Discuss the fundamental concepts of design: i) **Abstraction** ii) **Modularity** iii) **Information hiding**. | Understand |
| B3 | Explain: i) **Coupling between modules** ii) **The internal cohesion of a module**. | Understand |
| B4 | Discuss fundamental principles of **structured design**. Write notes on **transform analysis**. | Knowledge |
| C1 | State how do we **assess quality of a software design**? | Knowledge |
| C3 | Provide examples of **three data abstractions** and the procedural abstractions that manipulate them. | Apply |
| C5 | Demonstrate the architecture of a **house/building as metaphor**, compare with software architecture. How are classical and software architecture similar/different? | Apply |

---

## الجزء 3 — أسئلة التصميم من أوراق الامتحان الحقيقية (19 ورقة)

هذي الأقرب لصيغة امتحان الدكتور. الأقسام III (التصميم) من كل ورقة:

| الورقة | السؤال | العلامة |
|---|---|---|
| MRCET Dec 2022 Set-1 | **5A:** Translating the requirements model into the design model · **6A:** Software design concepts · **6B:** 3 golden rules of user interface design | 7M ×2 |
| MRCET Dec 2022 (2nd) | **5A:** Architecture in software design · **5B:** Types of architectural styles · **6A:** Data-centered architecture · **6B:** UI analysis and design | 7M |
| R18 Feb 2022 | **5A:** Software architecture with example · **5B:** Data design · **6A:** How to design user interface · **6B:** Object-oriented design process | 8M/6M |
| R18 Jul 2021 | **5:** Taxonomy of architectural styles (+ description of each) | 14M |
| R18 Oct/Nov 2020 | **5A:** Golden rules for UI design · **5B:** Software architecture · **6:** OOD process with examples | 14M |
| R18 Jun 2022 | **5:** Explain OOD process using UML · **6:** Data flow architecture / Call-and-return architecture | 14M / 7M |
| R18 Jun 2022 (IT) | **5A:** Merits of OOD process · **5B:** Design concepts · **6A:** Modularity & its importance by maximizing cohesion / minimizing coupling | 7M |
| R18 Nov 2022 | **5A:** Design concepts during design · **5B:** Architectural styles & patterns · **6A:** Data design & architectural design with examples · **6B:** Golden rules of UI design | 7M |
| R17 Feb 2022 | **5A:** Design quality in context of design engineering · **5B:** How software architecture is useful · **6:** UI analysis and design | 7M/14M |
| R17 Jul 2021 (IT) | **5A:** Design process w.r.t design engineering · **5B:** Data design + architectural styles · **6A:** Characteristics and criteria for a good design | 7M |
| R17 Jul/Aug 2021 | **5:** Design concepts | 14M |
| R17 Dec 21/Jan 22 | **5:** Translating analysis model into software design · **6:** Steps in effective UI design | 14M |
| Dec-21/Jan-22 (CSE) | **5:** What is design process? Characteristics of good design · **6:** Software architecture, why important | 14M |
| R18 Dec 2022 (IT) | **5A:** Golden rules of UI · **5B:** How can we assess design quality · **6A:** Role of software architecture + styles · **6B:** Key activities in OOD | 7M |
| Oct/Nov 2020 (IT) | **5A:** Explain design process · **5B:** Data design | 8M/6M |

**النمط اللي يتكرر (مهم جداً):** أسئلة الامتحان الحقيقية تدور على **6 محاور** بس:
1. **Software architecture** (تعريف + أهمية + styles/patterns + taxonomy)
2. **Design concepts / principles** (abstraction, modularity, information hiding)
3. **Coupling & Cohesion** (تعريف + أنواع + علاقتهن بالتصميم الجيد)
4. **OOD process** (الخطوات + UML + merits)
5. **UI design** (golden rules + steps)
6. **Data design**

**استنتاج:** لو حليت هذي الـ6 محاور من كل زاوية، **غطيت 95% من احتمالات الامتحان**.

---

## الجزء 4 — المحتوى الأعمق (اللي ما موجود بالسلايدات إطلاقاً)

من ملاحظات الساندبوكس السابقة (grounded من الكتاب) + فحصي — **هذا محتوى حقيقي موجود بالمصادر، ويوسّعك فوق السلايدات**:

### 4.1 Fan-in / Fan-out (مو بالسلايدات!)
- **Fan-out** = عدد الوحدات اللي تستدعيها وحدة معينة مباشرة. **fan-out عالي = خطر**: يعني الوحدة تفتقد الترابط، لأنها تنفذ وظائف كثيرة بدل واحدة. القاعدة: **fan-out أكبر من ~7 = تحذير**.
- **Fan-in** = عدد الوحدات اللي تستدعي وحدة معينة. **fan-in عالي = مرغوب**، لأنه يمثل **إعادة استخدام الكود** (code reuse).

### 4.2 Layered Design + المصطلحات (مو بالسلايدات!)
- **الترتيب الطبقي:** الوحدة تستدعي **فقط** الوحدات بالطبقة اللي تحتها مباشرة — لا الطبقة اللي فوقها، ولا حتى طبقتها نفسها.
- **Superordinate** = الوحدة المسيطرة. **Subordinate** = الوحدة المسيطر عليها.
- **Visible** = الوحدة B مرئية لـA إذا A تستدعيها مباشرة.
- **Depth** = عدد الطبقات. **Width** = المدى الكلي للسيطرة.
- **Control abstraction** = الطبقات العليا مجرّدة عن اللي تحتها.

### 4.3 الطريقة العملية لقياس الـcohesion (اختبار حاسم)
حكم على ترابط أي وحدة بهاي الطريقة:
1. شوف شنو تسوي الدوال فعلاً.
2. حاول توصف شغل الوحدة **بجملة واحدة**.
- إذا احتجت **جملة مركّبة** → cohesion = Sequential أو Communicational.
- إذا احتجت كلمات **"first / next / after / then"** → Sequential أو Temporal.
- إذا احتجت **"initialise / setup / shut down"** → Temporal.

### 4.4 الفرق الدقيق بين Flowchart و Structure Chart
- صعب تحدد الوحدات من الـflowchart.
- **تبادل البيانات** بين الوحدات **مو** ممثل بالـflowchart.
- التسلسل الزمني بالـflowchart **يُلغى** بالـstructure chart.
- **الـstructure chart بلا صناديق قرار (decision boxes)**.
- الـstructure chart يوضّح **كيف تتفاعل الوحدات** وشنو البيانات الممررة بينها.

### 4.5 Functional Independence (المفهوم اللي يربط كل شي)
**وحدة highly cohesive + low coupling = functionally independent.** وهي تعطي **3 فوائد**:
1. **Error isolation** — الخطأ ما ينتشر، وسهل تحديده.
2. **Scope for reuse** — الوحدة تنسحب وتُستخدم بمكان ثاني.
3. **Understandability** — تفهم الوحدة لحالها.

### 4.6 عوامل الـCoupling (جدول من Agarwal 2010)
| العامل | low (زين) | high (سيء) |
|---|---|---|
| Interface complexity | Simple / Obvious | Complicated / Obscure |
| Type of connection | To module **by name** | To **internal elements** |
| Type of communication | **Data** | **Control / Hybrid** |

### 4.7 الـDesign Framework (cyclic)
التصميم **مو خطوة واحدة** — هو إطار دوري: تجمع متطلبات → تحلل → تصميم عالي المستوى → تنقّح وتوثّق → **تتحقق (validate)** ضد المتطلبات → لأن التحقق ممكن يرفع أسئلة متطلبات جديدة → ترجع تنقّح. **دوري بطبيعته، مو عيب.**

---

## الجزء 5 — خريطة الكتب المتوفرة (للاستزادة)

| الكتاب | الموقع | قوة Ch5 |
|---|---|---|
| **Aggarwal & Singh** (الكتاب الأم — سلايداتنا منه) | سلايدات Ch05 | المصدر الرسمي |
| **AliFahim** (سكان) | `Reference_Textbooks/` | نفس الكتاب الأم — ص.202–248 |
| **Rajib Mall 4th** | نفس المجلد | الأقوى: coupling p298–299، cohesion p295–298، layered p293–300، function-vs-object p303–307، OOD Ch7 p388–405 |
| **Pressman 7th** | نفس المجلد | Ch13 p365–392: abstraction, modularity+cost curve, coupling p354–355, cohesion p353, info hiding p351 |
| **CS Agarwal 2010** | نفس المجلد | Ch5 System Design p119–144 |
| **Sommerville 9th** | نفس المجلد | ضعيف لمصطلحات Aggarwal |
| **Leach 2nd** | نفس المجلد | مرجع عام |

---

## الجزء 6 — الخلاصة العملية (شنو نسوي بهاي المعلومة)

**الحصيلة:** الجابتر هذا **أغنى بكثير** مما بالسلايدات، وامتحانه **متوقع النمط جداً** (6 محاور متكررة).

**التوصية:**
1. **Tier1** (الملف 01) = ضمان أسئلة الكتاب.
2. **Tier2** (الملف 02) = العمق.
3. **هذا الملف** = أسئلة خارجية + محتوى أعمق (fan-in/out, layered, functional independence) — يغطي الـ6 محاور الامتحانية.
4. **الأولوية القصوى للمذاكرة:** Coupling/Cohesion (أكثر محور متكرر) ثم OOD process ثم Architecture/styles ثم UI golden rules.

---
*مصادر: 3 بنوك أسئلة + 19 ورقة امتحان + 5 توتوريالز + sandbox grounded notes + 6 كتب مرجعية. كل شي داخل مجلد المادة — بلا مصدر خارجي.*
