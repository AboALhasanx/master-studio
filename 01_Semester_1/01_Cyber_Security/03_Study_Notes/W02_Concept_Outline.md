---
title: "Week 02 — Cybersecurity Risks and Threats (Booklet 2) · Bilingual Concept Outline"
subject: "01_Cyber_Security"
week: 2
instructor: "Asst. Prof. Dr. Huda Lafta Majeed"
source: "../02_Raw_Materials/W02_Risks_DrHuda_Booklet2.docx"
source_state: "text-only DOCX (no embedded images, no OMML equations)"
status: "concept outline — complete coverage, formula verification flags open"
created: 2026-09-23
---

# Week 02 — Cybersecurity Risks and Threats · Bilingual Concept Outline

> **Why this file exists.** Produced as the Thursday step of `00_STUDIO_HUB/PLAN_2026-09-23_to_27.md`: work through the Risk booklet in manageable sections, build a bilingual concept outline, and flag everything that needs source verification. This is the **backbone of the full study note** — it is not a compression of the booklet, and nothing from the booklet has been dropped.

> **Companion file — read this one for what to drill:** `W02_Exam_Focus.md` (built 2026-09-23 after the student's lecture report). It carries the **doctor's own emphasis map** — 30 highlight runs and 27 coloured runs extracted mechanically from the delivered DOCX — plus the numbered sets to memorise, the acronym list, and the open conflicts. **This outline is the reference; that sheet is the revision list.**

> **Late finding, 2026-09-23:** the DOCX **does** contain the doctor's highlighting (30 runs: `yellow` and `red`) and coloured text (red `FF0000`, dark red `C00000`, blue `548DD4`). My first pass at this file missed it because I only extracted plain `<w:t>` runs. The emphasis map is now recorded in the exam-focus sheet and the affected items are cross-referenced below.

**How to read it**

- **EN** = the booklet's own wording. Keep these exact terms for the exam; Dr. Huda's questions are answered in her vocabulary.
- **AR** = the concept explained in your dialect, technical terms left in English.
- `[VERIFY]` = an item that could not be confirmed from the delivered file and must be checked against another source before it is treated as exam-safe.
- Section numbers below are **this outline's** numbering. The booklet itself carries only a stray `3` at the top, which suggests the material is **chapter 3** of its parent textbook.

---

## 1. What Is Risk? — the technical definition

**EN.** Risk is used in its **technical sense**: the **quantitative probability that an error situation occurs and gives rise to damage**. In IT security, "damage" is **synonymous with a breach of the security policy**. This is an **objective** definition and must not be confused with **subjective risk**, which also takes human factors into account — public attitudes, trust, and personality.

**AR.** الـ risk هنا **مو** كلمة عامة، إلها تعريف تقني واحد: **احتمال كمّي (quantitative probability)** إنه تصير حالة خطأ وتسبّب **ضرر**. والضرر بالأمن السيبراني = **خرق لسياسة الأمن (breach of the security policy)**. يعني الـ damage مو "خسارة مالية" بالضرورة — خرخ السياسة نفسه ضرر.

**النقطة اللي تنقصّ بالامتحان:** التعريف هذا **موضوعي (objective)**. الـ **subjective risk** شي ثاني تماماً لأنه يدخل بيه العامل البشري — نظرة الناس، الثقة، الشخصية. أي سؤال يخلط بين الاثنين، جوابه إنه الاثنان مو نفس المفهوم.

---

## 2. Threat, vulnerability, damage — the causal chain

**EN.** Damage occurs when a **threat is realised against some weakness in the system**. A weakness which can be exploited to damage the system is known as a **vulnerability**. The booklet illustrates this with a shark: the **threat is the shark**, the **vulnerability is a welding fault in the shark cage** (Fig. 3.1).

**AR.** السلسلة السببية: **threat** (تهديد) → يشتغل على **weakness/vulnerability** (نقطة ضعف قابلة للاستغلال) → يصير **damage** (ضرر = خرق السياسة).

تشبيه القفص: **القرش = التهديد**، و**عيوب اللحام بالقفص = الثغرة**. لاحظ الدقة: القرش موجود واللحام موجود، والضرر يصير لما الاثنين يتلاقون. لهذا **الثغرة مو تهديد** والتهديد مو ثغرة.

---

## 3. The risk equation and the risk matrix

**EN.** The **basic risk, S**, of a threat depends on the **frequency, F**, of attempts to exploit the vulnerability and the **consequences, K**, of a successful attempt:

```text
S = F × K
```

The relationship is visualised as a **risk matrix**, where the result of the multiplication is given by a colour code:

- **Red = high risk** — arises when the consequences of a successful attack are **high** *and* the frequency of attempts is **also high**.
- **Yellow = medium risk.**
- **Green = low risk.**

**AR.** الـ **basic risk `S`** يتحدد بعاملين بس: **`F` = تكرار محاولات استغلال الثغرة**، و **`K` = حجم العواقب لو نجحت المحاولة**. الجداء بينهن يعطي `S`.

بالـ **risk matrix**: المحور يمثل التكرار والمحور الثاني يمثل العواقب، وكل تهديد يُوزَّع على المربّع اللي يطابق `(F, K)` ماله. **الأحمر ما يجي إلا من اجتماع الاثنين** — عواقب عالية **و** تكرار عالي. عواقب عالية بتكرار واطي مو أحمر.

`[VERIFY]` — the operator symbol `×` is **missing from the delivered DOCX text layer** (the equation sits in a stacked multi-paragraph layout and the glyph did not survive). The multiplication reading is taken from the booklet's own next sentence: *"The result of the 'multiplication' is indicated by a color code."* Confirm the symbol against the printed original.

---

## 4. Countermeasures and residual risk

**EN.** Risk is reduced by introducing **countermeasures** (also known as **controls**), which must protect against the relevant threat. The reduced risk is known as the **residual risk, R**. If the threat is evaluated to give a risk `S`, and the level of countermeasures is `M`:

```text
R = S / M
```

`M` covers **both** the number of countermeasures (there can be several things affecting the risk for a particular type of attack) **and** their effectiveness. This is visualised as a **residual risk matrix**, again colour-coded:

- **Red = high residual risk** — arises when the risk is **high** and the level of countermeasures is **low**.
- **Yellow = medium.**
- **Green = low.**

**AR.** الـ **countermeasures** (وتسمى أيضاً **controls**) هي اللي تخفّض الخطر. الخطر بعد التخفيض اسمه **residual risk `R`**، ويُحسب بقسمة `S` على `M`.

**النقطة المهمة:** `M` **مو عدد التدابير بس** — تشمل **العدد + الفعالية**. يعني عشرة تدابير ضعيفة مو مثل تدبير واحد قوي.

بمصفوفة الـ residual risk: **الأحمر = خطر عالي مع تدابير واطية**. لاحظ الانعكاس: هذي المصفوفة محاورها `(risk, countermeasures)` مو `(frequency, consequences)`.

`[VERIFY]` — the `/` operator is likewise **absent from the DOCX text layer**. The division reading is taken from the booklet's next sentence: *"The result of the 'division' is again given by a colour code."* Confirm against the printed original.

`[CONFLICT — 2026-09-23 lecture report]` — the student reports the two equations from the lecture as **`f = s · k`** and **`f = s / n`, with `n` = number of threats**. That does **not** match the file's letters (`S = F × K`, `R = S / M`) or its definition of the denominator (the **level of countermeasures**, covering *number + effectiveness*). The lecture wording is recorded verbatim in `W02_Exam_Focus.md` §8.1. **Not resolved — awaiting the student's paper notes.** One hard fact from the doctor's own marking: she coloured the letters **`S`, `F`, `K`** red, so those three are hers.

**الفرق اللي لازم يثبت:** `S = F × K` مصفوفتها محاورها **(التكرار × العواقب)**؛ `R = S / M` مصفوفتها محاورها **(الخطر ÷ التدابير)**. مصفوفتان، محوران مختلفان، ولا وحدة تكمل الثانية.

---

## 5. Threats in IT systems — the four groups

**EN.** Many IT users mistakenly believe the only threat is an attacker hacking in. In reality the threat pattern is much more varied, related to many different aspects of the computer's operation. At least **four main groups**:

### 5.1. Hardware-related threats
Threats which **physically** affect the computer itself or the infrastructure it depends on in order to work as required.
- Harmful surroundings
- Natural disasters such as storms
- Physical attacks on the computer, such as theft
- Faults in the infrastructure

### 5.2. Software-related threats
Threats which affect the **software installed** in the computer (applications and the operating system), or which are due to **poorly designed or wilfully malicious programs coming from outside**.
- Unauthorized modification or deletion of software
- Wilfully malicious programs (so-called **malware**) such as **viruses, worms, trojan horses and logic bombs**
- Use of poorly designed programs which contain vulnerabilities
- Use of incorrect or out-of-date software versions
- Theft or unauthorized copying of software

### 5.3. Data-related threats
Threats which can lead to **unauthorized processing (including storage) of data** in any way.
- Unwanted storage, modification, disclosure or deletion of data
- **Inference** — collecting accessible data from which it is possible to **deduce confidential information which is not directly accessible**
- **Masquerading** (pretending to be someone else), unauthorized access

### 5.4. Liveware-related threats
Threats related to **human error among the computer's users**.
- Social engineering, phishing
- IT fraud, forgery and other forms of criminality, now carried out with the help of computers

**AR.** أربع مجموعات، والمفتاح إنك تميّز التهديد من **مصدره**:

| المجموعة | مصدرها | مثال سريع |
|:---|:---|:---|
| Hardware | يلمس الجهاز أو البنية التحتية **مادياً** | عاصفة، سرقة، عطل بنية تحتية، بيئة ضارّة |
| Software | البرامج المثبَّتة أو برامج خارجية سيئة التصميم/خبيثة | تعديل/حذف غير مصرّح، malware، نسخ قديمة، سرقة برامج |
| Data | **المعالجة** غير المصرّح بها للبيانات | تخزين/تعديل/كشف/حذف، **inference**، **masquerading** |
| Liveware | **الخطأ البشري** عند المستخدمين | social engineering، phishing، احتيال وتزوير |

**تعريف الـ inference مهم:** مو سرقة بيانات سرّية مباشرة — هي **جمع بيانات متاحة** وتستنتج منها معلومات سرّية **مو متاحة مباشرة**. الفرق هذا يجي بالامتحان.

---

## 6. Countermeasure-to-threat matching

**EN.** A threat is blocked by control of a vulnerability with the help of suitable countermeasures, which **must be adapted to suit the type of threat**. Examples given (explicitly "but not limited"):

| Threat | Countermeasure |
|:---|:---|
| Attackers outside the system, attacking through the Internet | **Firewalls** in the network, to prevent traffic from the attacker reaching the target |
| Malware | **Antivirus programs** and other so-called security programs |
| Vandalism, theft and other physical damage to equipment | Place the equipment in a **secure room** |
| Unauthorized modification or deletion of data or software | Take **regular backup copies** |
| Unauthorized access to data | Use **encryption or access control** |
| Personnel and ordinary authorized users | **Check personnel** and introduce **suitable training** |

**AR.** القاعدة: **كل تهديد إله تدبير مناسب لنوعه** — مو تدبير واحد للكل. لاحظ إن آخر صف مهم: التهديد من **المستخدمين المصرّح لهم** أنفسهم، وعلاجه **فحص الأفراد + التدريب**، مو تقنية.

---

## 7. Risk management and the five mitigation strategies

**EN.** **Risk management** deals with **all the activities related to evaluating and reducing risks**. The part whose aim is to reduce risk to an **acceptable level** is often called **risk mitigation**. Five generally recognised strategies:

1. **Risk avoidance** — keep the target system away from given risks. *e.g. Forbid risky behaviour such as use of WiFi.*
2. **Risk reduction** — take proactive steps to prevent losses occurring or to reduce the extent of the loss. *e.g. Make use of backups, encryption and so on.*
3. **Risk retention** — allow a certain, agreed amount of "residual risk". *e.g. Use reliable, but not redundant communication equipment.*
4. **Risk transfer** — transfer the risk to others. *e.g. Set up a contract for outsourcing.*
5. **Risk sharing** — agree with other parties to deal with risks jointly. *e.g. Agree on common facilities or mutual insurance.*

**AR.** **Risk management** هو المظلة الكبيرة (كل نشاط يتعلق بتقييم وتخفيض المخاطر). **Risk mitigation** جزء منه تحديداً: الجزء اللي هدفه يوصل الخطر لمستوى **مقبول**.

الخمس استراتيجيات — احفظهن بالمثال، لأن السؤال يجي "أي استراتيجية هذي؟" ويكتب لك حالة:

| الاستراتيجية | الفكرة | مثال الكتيّب |
|:---|:---|:---|
| Avoidance | ابعد النظام عن الخطر أصلاً | منع سلوك خطِر مثل استخدام WiFi |
| Reduction | خطوات استباقية تمنع الخسارة أو تقلّلها | نسخ احتياطية، تشفير |
| Retention | اقبل قدر **متفق عليه** من الخطر المتبقي | معدات اتصال موثوقة لكن **مو مكرّرة** |
| Transfer | انقل الخطر لغيرك | عقد outsourcing |
| Sharing | اتفق مع أطراف ثانية تتقاسمونه | مرافق مشتركة أو تأمين متبادل |

**فرّق بين Transfer و Sharing:** Transfer = **تخلّي** عن الخطر لطرف آخر. Sharing = **تقاسم** مع أطراف أخرى. مثال الـ retention انتبه له: "موثوقة لكن مو مكرّرة" — يعني قبلت الخطر المتبقي طوعاً.

---

## 8. Systematic security analysis — the five frameworks

**EN.** To develop a secure system it is an advantage to use a systematic method; over the years a number of systematic procedures for security analysis of IT systems have been developed. Well-known examples:

| Framework | What it presents |
|:---|:---|
| **COBIT** (Control Objectives for Information and related Technology) | Objectives for measures which can be used to **manage risk** |
| **COSO** (Committee of Sponsoring Organizations) | A detailed description of **internal processes** which must be followed within a company in order to achieve suitably low risk |
| **FAIR** (Factor Analysis of Information Risk) | A **taxonomy** for factors which can contribute to risk formation, a **standard for naming** risk-related quantities, and a **model for calculating risk** |
| **ISO/IEC 27002** | A **checklist** of things which have to be taken into consideration in order to achieve a secure system |
| **OCTAVE** (Operationally Critical Threat, Asset and Vulnerability Evaluation) | The **process** of analysing threats and the corresponding risks and of finding suitable countermeasures |

**AR.** خمسة أطر، والتمييز بينهن يجي بالامتحان — كل واحد "شنو يقدّم":

- **COBIT** → أهداف لتدابير إدارة الخطر.
- **COSO** → **عمليات داخلية** يجب تتبعها داخل الشركة.
- **FAIR** → **تصنيف (taxonomy)** + **معيار تسمية** + **نموذج حساب** للخطر. (هذا الوحيد اللي فيه "حساب".)
- **ISO/IEC 27002** → **قائمة فحص (checklist)**.
- **OCTAVE** → **عملية (process)** تحليل التهديدات والمخاطر وإيجاد التدابير.

---

## 9. ISO/IEC 27002

**EN.** Part of a series developed jointly by the **International Organization for Standardization (ISO)** and the **International Electrotechnical Commission (IEC)**. The series currently consists of **44 complete or planned standards**, covering many aspects of information security, both in general and within specific areas such as **finance, energy supply, collection of digital evidence and "cloud computing"**.

The latest version, from **2022**, describes targets for what has to be done within **14 categories**:

1. Information security policies
2. Organization of information security
3. Human resource security
4. Asset management
5. Access control
6. Cryptography
7. Physical and environmental security
8. Operation security
9. Communication security
10. System acquisition, development and maintenance
11. Supplier relationships
12. Information security incident management
13. Information security aspects of business continuity management
14. Compliance with legal and contractual requirements

**AR.** **ISO + IEC** معاً (مو ISO لحالها). السلسلة **44 معيار** مكتمل أو مخطط. نسخة **2022** تعطي **14 فئة**.

**نمط الحفظ:** لاحظ إن الفئات مرتبة منطقياً — سياسات، تنظيم، بشر، أصول، وصول، تشفير، فيزيائي، عمليات، اتصالات، تطوير، موردون، حوادث، استمرارية، امتثال. لو حفظت التسلسل المنطقي ما تحتاج تحفظها عشوائي.

**سؤال محتمل:** "كم فئة في نسخة 2022؟" → **14**. "من أصدره؟" → **ISO و IEC معاً**.

---

## 10. OCTAVE

**EN.** A method for **risk analysis** developed for the international organization **CERT (Computer Emergency Response Team)** at **Carnegie Mellon University, USA**. The method is based on a **systematic analysis of assets, threats and vulnerabilities in three phases**:

- **Phase 1:** Build up **asset-based threat profiles**.
- **Phase 2:** Identify **vulnerabilities in the infrastructure** which could lead to unauthorized action.
- **Phase 3:** Develop a **security strategy and plans**.

OCTAVE exists in **four variants**:
1. **OCTAVE** — the original method.
2. **OCTAVE-S** — a simplified version for **small enterprises with limited resources**.
3. **OCTAVE ALLEGRO** — an expanded version for enterprises with an **advanced IT structure**.
4. **OCTAVE FORTE**.

**AR.** الاسم نفسه فكّكه: **O**perationally **C**ritical **T**hreat, **A**sset and **V**ulnerability **E**valuation.

- المطوّر: **CERT** في **جامعة كارنيجي ميلون**، أمريكا.
- **ثلاث مراحل** بالترتيب: (1) بروفايلات تهديد مبنية على الأصول → (2) ثغرات البنية التحتية اللي تسمح بعمل غير مصرّح → (3) استراتيجية وخطة أمنية.
- **أربع نسخ**: الأصل، **-S** للشركات الصغيرة محدودة الموارد، **ALLEGRO** للمتقدّمة، **FORTE**.

`[VERIFY]` — the booklet names the fourth variant (OCTAVE FORTE) without describing it. If the doctor asks what FORTE is for, this outline has no sourced answer.

---

## 11. Risk management as a PDCA process

**EN.** Risk management should **not be a one-time activity**. The risk profile changes with time as new forms of attack are developed or known threats appear more often, so the situation must be **re-evaluated at regular intervals**. Risk management therefore most often takes the form of a **PDCA process** with four characteristic phases:

- **Plan** — Threats are identified, risks are analyzed, and countermeasures are planned.
- **Do** — Countermeasures or other forms of risk management are implemented.
- **Check** — The implemented solution is monitored, to check that the desired level of security is maintained.
- **Act** — The solution is adjusted, so that it continues to give the desired security level, or a decision is taken to carry out a completely new **Plan** phase.

**AR.** الفكرة الأساسية: **إدارة الخطر مو شغلة تسويها مرة وتخلص** — لأن مشهد التهديدات يتغيّر، فلازم إعادة تقييم دورية. ولهذا تاخذ شكل **PDCA**.

| المرحلة | شنو يصير بيها |
|:---|:---|
| **Plan** | تحديد التهديدات + تحليل المخاطر + تخطيط التدابير |
| **Do** | تنفيذ التدابير |
| **Check** | مراقبة الحل المنفَّذ — هل مستوى الأمن المطلوب محفوظ؟ |
| **Act** | تعديل الحل ليستمر بنفس المستوى، **أو** قرار ببدء **Plan** جديدة |

**الربط المهم:** `Act` تنتهي إما بتعديل أو **بدورة جديدة كاملة**. يعني PDCA **حلقة (cycle)** مو خط مستقيم.

---

## 12. NIST-oriented material

**EN.** The booklet presents three NIST-related workstreams as bulleted directives.

**Develop a risk-management program**
- Determine the risks of losing control of a host.
- Identify potential adversarial activities that could target your domain (e.g. are they targeting intellectual property?).
- Present a **risk-informed report** to ensure the organization recognizes the risks and provides support/buy-in to resolve, reduce, or prevent risks of loss.

**Use NIST security controls**
- Create a **matrix of individual concerns and associated attack vectors**.
- Provide **mitigation method(s) for each**.
- Select the appropriate **NIST family** — **Management, Operational, Technical** — of security controls that need to be implemented (reference **NIST SP 800-53**, tables, spreadsheets, tools).
- Ensure that the reasons for their selection are **commensurate to the risks**. The selection of **low-, medium-, and high-level** implementations should be described in the guidance and should help ensure a **cost-effective** solution. **"Don't overprescribe controls!"**

**The NIST Framework stakeholders — create a policy for assessments**
- Define the environment.
- Determine organizational priorities for protecting company property and materials.
- Ensure senior management is supportive.
- Procedurally define a process and diligence to form an informative assessment outcome.

**AR.** ثلاث حزم:

1. **برنامج إدارة الخطر** — تحدد مخاطر فقدان السيطرة على host، وتحدد الأنشطة العدائية المحتملة اللي تستهدف نطاقك (مثلاً: هل يستهدفون الملكية الفكرية؟)، وتقدّم **تقرير مبني على الخطر** حتى المؤسسة تعترف بالمخاطر وتدعم الحل.
2. **ضوابط NIST** — مصفوفة (اهتمامات × نواقل هجوم) + طريقة تخفيف لكل واحدة + اختيار **العائلة** المناسبة: **Management / Operational / Technical** (مرجع **NIST SP 800-53**) + تبرير الاختيار **بما يتناسب مع الخطر** + وصف مستوى التنفيذ **low/medium/high** + حل **فعّال الكلفة**. والعبارة اللي تنحفظ حرفياً: **"Don't overprescribe controls!"**
3. **أصحاب المصلحة بإطار NIST** — سياسة للتقييمات: تحديد البيئة، أولويات حماية الممتلكات، دعم الإدارة العليا، وتحديد إجراء وعناية بشكل إجرائي للوصول لمخرج تقييم مفيد.

**عائلات NIST الثلاث لازم تنحفظ بالترتيب:** **Management → Operational → Technical**.

---

## 13. Security policy

**EN.** A key component that **brings all three levels of security together** is a well-designed **security policy** that states **how security is implemented at each level**. Businesses and organizations develop comprehensive security policies that define **who is authorized to access different assets** and **what they are allowed to do with those assets** when they do access them.

Worked example: allowing employees and visitors **free access to all departments** provides a variety of security risks. You will want to maintain **access control** to create an environment that reduces the human nature of temptation; if everyone can move freely inside the organization, it is much harder to implement safeguards preventing them from accessing or taking physical or cyber assets. Access control also prevents **accidents**.

Instead, develop a **cohesive access-control policy at each level** that gives authorized people appropriate levels of access to selected assets while inhibiting access by people who are not authorized. Then **enforce** those policies with the correct **types and numbers of access-control devices** — **sensors, barriers, logs, ID badges, or security guards** — as deemed appropriate.

**AR.** السياسة الأمنية مو ورقة نظرية — هي **اللي تربط المستويات الثلاثة للأمن ببعضها**، وتحدد **من مصرّح له** و**شنو مسموح له يسوي** بالأصل بعد ما يوصل.

مثال الكتيّب: خلي الموظفين والزوار يتنقلون بحرية بكل الأقسام = مخاطر متعددة. الحل: **access control**، وله سببين: (1) يقلّل **إغراء الطبيعة البشرية**، (2) يمنع **الحوادث**.

**الترتيب اللي بالكتيّب:** سياسة متكاملة لكل مستوى → **إنفاذ** بأجهزة وصول بالنوع والعدد الصحيح → الأمثلة: **sensors · barriers · logs · ID badges · security guards**.

---

## 14. Physical security controls

**EN.** Enforcing access-control measures may initially include **placing locks on doors** that access offices and **separating departments or networking sections with similar physical barriers**. Many companies have a front door or an entranceway that includes a **receptionist** to control access.

### Locks and keys
The primary physical barrier in most security perimeters is the **lockable door**. The **door** provides the physical barrier but in itself will only **keep honest people out**. The **lock** provides the **authentication function** of the barrier through its **key**. Having the key signifies that the person either **possesses or knows** the information required to gain access.

### Standard key-locking deadbolts
Locking mechanism similar to that of the electronic solenoid-operated deadbolt, but **engaged or withdrawn with a key**. They provide an **added level of security for doors that can be operated manually**. Available with a **single or double cylinder**.

### Solenoid-operated deadbolt locks
**Electronically operated** deadbolt locks offering an **increased level of security for the perimeter**. Adaptable to any security system; perform well as **auxiliary locks** on doors where access control is desired.

### Cipher locks
Require **personal access codes known by the user**; often used in access-control and management systems. They operate by **unlocking magnetic door locks when the correct programmed code is entered** on the cipher-lock keypad. They provide an added level of security for **perimeter entry areas**.

### Access-control gates
Like a door, a gate is a type of physical barrier that can be **swung, drawn, or lowered** to control **ingress and egress** through a wall or fence. Two main types:
- **Sliding gates** — used where **high levels of operational safety and security** are needed.
- **Swinging gates** — equipped with **fully adjustable hinges** that allow the gate to swing through **180 degrees**.

### Control relays
**Electromechanical devices** that employ safer, **low-voltage/low-current control signals** to control **higher-voltage/higher-current devices**.

**AR.** الجدار الفيزيائي الأول بأغلب المحيطات = **الباب القابل للقفل**. والتمييز المهم: **الباب** يوفر الحاجز المادي بس "يوقف الناس الأمينة بس"، أما **القفل** فهو اللي يوفر **وظيفة المصادقة (authentication)** عبر **المفتاح**. وملك المفتاح يعني إما **يملك** أو **يعرف** المعلومات اللازمة للدخول.

| العنصر | التمييز |
|:---|:---|
| Standard key-locking deadbolt | يشتغل **بمفتاح**، لبوابات تُدار يدوياً، **single أو double cylinder** |
| Solenoid-operated deadbolt | **إلكتروني**، مستوى أمن أعلى للمحيط، يصلح **قفل مساعد** |
| Cipher lock | **رمز وصول شخصي**، يفتح الأقفال المغناطيسية عند إدخال الرمز الصحيح |
| Sliding gate | لما نحتاج **سلامة وأمن تشغيلي عالي** |
| Swinging gate | **مفصلات قابلة للتعديل بالكامل**، تدور **180 درجة** |
| Control relay | جهاز **كهروميكانيكي**: إشارة تحكّم **واطية الفولتية/التيار** تتحكم بجهاز **عالي الفولتية/التيار** |

---

## 15. Authentication systems

**EN.** **Authentication** is the process of **determining that someone is who they say they are**. Effective access control involves being able to control the **ingress, egress, and regress** to an asset based on **authorization**. In particular, **limiting the access of unauthorized personnel to important assets is the most fundamental security step that you can take**. Therefore **authorization is based on authentication**.

Multiple factors are involved in authentication:

| Factor | Booklet wording |
|:---|:---|
| **Knowledge** | Something you **know** or something that only the designated person should know |
| **Possession** | Something you **have** or something that only the designated person should have |
| **Inheritance** | Something you **are** or something that only the designated person is |
| **Location** | Somewhere you **are** or somewhere that only the designated person is |

**AR.** **Authentication** = "أثبت إنك من تدّعي". والترتيب المنطقي: **authorization مبنية على authentication** — ما تكدر تصرّح لأحد قبل ما تعرف منو. وأهم خطوة أمنية أساسية بحسب الكتيّب: **تحديد وصول غير المصرّح لهم إلى الأصول المهمة**.

العوامل الأربعة (احفظهن بالمفتاح الإنجليزي):

| العامل | المعنى |
|:---|:---|
| **Knowledge** | شي **تعرفه** |
| **Possession** | شي **تملكه** |
| **Inheritance** | شي **إنت هو** (صفة ذاتية) |
| **Location** | مكان **إنت بيه** |

`[VERIFY]` — the booklet prints **"Inheritance"** for the factor meaning *something you are*. The standard English security term for this factor is **"Inherence"** (*inheritance* normally means receiving property from a predecessor). Recorded here verbatim as the booklet writes it, because the exam follows the doctor's material. Worth one clarifying question in class if the term comes up — this is a terminology check, not a challenge to the content.

**لاحظ:** هذي **أربعة عوامل**، مو ثلاثة. أغلب الطلبة يحفظون ثلاثة (know / have / are) وينسون **Location**.

---

## 16. Physical authentication technologies

**EN.**
- **Magnetic stripe readers** — a magnetic stripe card is a physical credit-card-like device that contains authentication information in the form of **magnetically coded spots on a magnetic stripe**.
- **Smart cards** — also credit-card-like and often resemble magnetic stripe cards, but offer **improved data security** due to the presence of **intelligent circuitry** that can be used to **hide the user's data until an authentication process has been performed**.
- **RFID badges** — **Radio Frequency Identification** badges provide **hands-free** access-control tools that improve on the **bar code, magnetic stripe, and proximity reader** technologies. The RFID system employs **radio signals** to identify unique items using an **RFID reader device and RFID tags**.
- **Biometric scanners** — **biometrics** is the term used to describe access-control mechanisms that use **human physical characteristics** to verify individual identities.

**AR.** أربع تقنيات، والفرق بينهن بالخطر الأمني:

| التقنية | النقطة المميزة |
|:---|:---|
| Magnetic stripe | معلومات المصادقة = **نقاط مشفّرة مغناطيسياً** على شريط |
| Smart card | **دارة ذكية** تخفي بيانات المستخدم **لحد ما تصير المصادقة** ← أمن بيانات أعلى |
| RFID badge | **بلا لمس (hands-free)**، بإشارات راديو، يتفوق على الباركود والشريط المغناطيسي و proximity readers |
| Biometric | يعتمد على **خصائص جسدية بشرية** للتحقق من الهوية |

---

## 17. Remote-access monitoring and automated access control

**EN.**
- **Remote-access monitoring** — monitoring or measuring devices from a **remote location or control room**. In the security realm this involves having **external access to the security system through a communication system**.
- **Automated access-control systems** — add another dimension to standard security monitoring and reporting functions. Although automated access control is **not an integral part** of the typical intrusion-detection and monitoring system, it **adds to the safety and convenience** of perimeter-access control. Two flavours:
  - **Remote-access-control systems** — a design feature that manages entry to protected areas by **authenticating the identity of persons entering a secured area** (security zone or computer system) using an authentication system **located in a different location than the access point**.
  - **Remote-control access systems** — a design feature that works with remote monitoring systems to **monitor, control, and supervise doors, gates, and conveyances from a distance**.

**AR.** فرّق بين الثلاثة — الأسماء متشابهة والامتحان يلعب على هذا:

| المصطلح | الفكرة |
|:---|:---|
| Remote-access **monitoring** | **مراقبة/قياس** الأجهزة من مكان بعيد أو غرفة تحكّم |
| Remote-**access control** | **إدارة الدخول** بمصادقة تجري **من موقع مختلف عن نقطة الوصول** |
| Remote-**control access** | **تحكّم وإشراف** على الأبواب والبوابات والوسائل من بعيد، مع أنظمة المراقبة |

**نقطة دقيقة:** Automated access control **مو جزء أساسي** من نظام كشف التسلل والمراقبة التقليدي — بس **يضيف** سلامة وراحة للتحكم بمحيط الوصول.

---

## 18. Cyber security policy and cyber risk assessment

**EN.**

**Security policy** — documentation stating **how security should be implemented at each level**. Businesses develop comprehensive security policies defining who is authorized to access different assets and what they are allowed to do with those assets. *(Figure reference: NIST SP-800-30 Risk Assessment Process.)*

**Cyber security policy** — the company's security policy explains the **overall requirements** needed to protect an organization's **network data and computer systems**.

**Cyber risk assessment and management** — the process of **identifying, evaluating, and mitigating** the risks associated with cyber threats to an organization or system. It involves understanding the **potential vulnerabilities in a system**, the **likelihood of cyberattacks**, and the **impact** such attacks could have on the organization's **operations, reputation, and data security**.

**Key components:**
1. **Risk Identification** — pinpointing potential cyber threats such as malware, phishing, ransomware, data breaches, etc.
2. **Risk Evaluation** — analyzing the likelihood of each risk materializing and the severity of its potential impact.
3. **Risk Mitigation** — developing strategies to reduce or manage the risks. This includes implementing security controls such as **firewalls, encryption, user education, and backup systems**.
4. **Monitoring and Review** — continuously observing the cyber landscape, updating defenses, and reassessing risks as new threats emerge.

**Importance:**
- As technology advances, cyber threats become more complex, making risk management essential for protecting sensitive data and ensuring the **continuity of business operations**.
- Standards and frameworks like **ISO 27001, NIST Cybersecurity Framework**, and country-specific guidelines (e.g. from the **UK's National Cyber Security Centre**) provide structured approaches to performing risk assessments and management in cybersecurity contexts.

**Outcome:** by properly conducting cyber risk assessments and management, organizations can **improve their resilience against attacks** and better prepare for the inevitable challenges in the digital landscape.

**AR.** ثلاث مصطلحات متدرجة:
1. **Security policy** — وثيقة **كيف** يُنفَّذ الأمن بكل مستوى.
2. **Cyber security policy** — سياسة الشركة اللي تشرح **المتطلبات الشاملة** لحماية بيانات الشبكة وأنظمة الحاسوب.
3. **Cyber risk assessment and management** — **العملية** الكاملة: تعريف + تقييم + تخفيف.

**المكوّنات الأربعة بالترتيب (احفظ التسلسل):**
**Risk Identification → Risk Evaluation → Risk Mitigation → Monitoring and Review**

**أهمية:** التهديدات تزداد تعقيداً → إدارة الخطر ضرورية لحماية البيانات الحسّاسة و**استمرارية العمل**. والأطر المذكورة: **ISO 27001 · NIST CSF · إرشادات خاصة بالدول (مثل UK NCSC)**.

`[VERIFY]` — the booklet names **NIST SP 800-30** only in a figure caption, and **ISO 27001** in the importance list, while §9 covers **ISO/IEC 27002**. The two ISO numbers are **not the same standard** (27001 is the management-system requirements standard; 27002 is the controls guidance). The booklet does not explain the difference. Flagged, not resolved.

---

## 19. Formula card

Two equations are given in this booklet. Both are quoted, with their verification state.

| Equation | Meaning | Variables | State |
|:---|:---|:---|:---|
| **S = F × K** | Basic risk of a threat | `S` = basic risk · `F` = frequency of attempts to exploit the vulnerability · `K` = consequences of a successful attempt | Operator `×` reconstructed from the booklet's prose ("the result of the *multiplication*"). `[VERIFY]` symbol against the printed original |
| **R = S / M** | Residual risk after countermeasures | `R` = residual risk · `S` = risk of the threat · `M` = level of countermeasures (**number + effectiveness**) | Operator `/` reconstructed from the booklet's prose ("the result of the *division*"). `[VERIFY]` symbol against the printed original |

**Matrix pairing — do not mix these up**

| Matrix | Axes | Red corner |
|:---|:---|:---|
| **Risk matrix** | frequency `F` × consequences `K` | high `F` **and** high `K` |
| **Residual risk matrix** | risk `S` ÷ countermeasures `M` | high `S` **and** low `M` |

---

## 20. Terminology table (EN → AR)

| English (booklet term) | Arabic | Note |
|:---|:---|:---|
| Risk (technical sense) | الخطر — التعريف التقني | Quantitative probability of an error situation causing damage |
| Subjective risk | الخطر الذاتي | Includes human factors: attitudes, trust, personality |
| Damage | الضرر | Synonymous with **breach of the security policy** |
| Threat | التهديد | — |
| Vulnerability | الثغرة / نقطة الضعف | A weakness exploitable to damage the system |
| Basic risk `S` | الخطر الأساسي | `S = F × K` |
| Frequency `F` | تكرار المحاولات | — |
| Consequences `K` | العواقب | — |
| Countermeasure / control | التدبير المضاد / الضابط | `M` covers number **and** effectiveness |
| Residual risk `R` | الخطر المتبقي | `R = S / M` |
| Risk matrix | مصفوفة الخطر | Axes: frequency × consequences |
| Residual risk matrix | مصفوفة الخطر المتبقي | Axes: risk ÷ countermeasures |
| Risk management | إدارة الخطر | All evaluating + reducing activities |
| Risk mitigation | تخفيف الخطر | The part reducing risk to an acceptable level |
| Inference | الاستدلال | Deducing confidential info from accessible data |
| Masquerading | انتحال الهوية | Pretending to be someone else |
| Liveware-related threat | تهديد متعلق بالعنصر البشري | Human error among users |
| Malware | البرمجيات الخبيثة | Viruses, worms, trojan horses, logic bombs |
| PDCA | خطة – تنفيذ – فحص – تصحيح | Plan, Do, Check, Act |
| Authentication | المصادقة | Determining that someone is who they say they are |
| Authorization | التصريح | Built **on** authentication |
| Ingress / egress / regress | الدخول / الخروج / العودة | — |
| Knowledge / Possession / Inheritance / Location | المعرفة / الحيازة / الصفة الذاتية / الموقع | The booklet's four factors |
| Biometrics | القياسات الحيوية | Human physical characteristics |

---

## 21. Source-verification flags (open items)

| # | Flag | Status |
|:---:|:---|:---|
| 1 | `S = F × K` — the `×` glyph is absent from the DOCX text layer | Reconstructed from prose. Confirm on the printed original |
| 2 | `R = S / M` — the `/` glyph is absent from the DOCX text layer | Reconstructed from prose. Confirm on the printed original |
| 3 | **No images exist in the delivered file** — the DOCX contains zero media entries | All figures (Fig. 3.1 shark, risk matrix, residual risk matrix, OCTAVE phases, PDCA diagram, physical barriers, cipher lock, gates, magnetic stripe, smart cards, RFID, biometrics, remote-access options, remote-control operations, NIST SP-800-30 process) are **referenced but not present**. Obtain the illustrated version before relying on any figure |
| 4 | "Inheritance" as the *something you are* factor | Booklet wording recorded verbatim; standard term is **Inherence**. Terminology check, not a content challenge |
| 5 | ISO 27001 (mentioned in §18) vs ISO/IEC 27002 (§9) | Different standards; the booklet does not distinguish them |
| 6 | OCTAVE FORTE — named as the 4th variant with no description | No sourced description in the booklet |
| 7 | Source textbook / chapter attribution | **RESOLVED 2026-09-23** — the booklet is a direct extraction of **Sharp, R., "Risk", in *Introduction to Cybersecurity: A Multidisciplinary Challenge*, Springer, 2024, pp. 37–56**, DOI [10.1007/978-3-031-41463-3_3](https://doi.org/10.1007/978-3-031-41463-3_3). The stray `3` is the chapter number. **Verification also found two factual errors in the booklet — see `W02_Source_Verify.md`** |
| 9 | ISO/IEC 27002 "**2022** … 14 categories" (§9) | **ERROR (verified).** The 14 categories are the **2013** structure; **2022** is **4 themes / 93 controls**. Dr. Huda highlighted this line yellow |
| 10 | OCTAVE's fourth variant "**OCTAVE FORTE**" (§10) | **ERROR (verified).** Only **three** public OCTAVE methodologies exist: OCTAVE, OCTAVE-S, OCTAVE Allegro |
| 11 | Authentication factor "**Inheritance**" (§15) | **TERMINOLOGY ERROR (verified).** Standard term is **Inherence** |
| 8 | Exact quiz date | Still **unconfirmed**. The postponed quiz covers **both** booklets |

---

## 22. Week 01 closed-book recall (no answers — attempt before checking)

Answer these from memory, then verify against `W01_Source_Notes.md`. Mark each one: **solid / shaky / blank**.

1. Define cybersecurity in one sentence, and state what the *cybersecurity-as-an-optimization-problem* equation optimises.
2. Name the three pillars of the CIA Triad and give the one-line definition of each.
3. Which pillar does a **bank** weight most heavily, and why? What does the weighting change about the security utility function?
4. Write the **attack surface** equation `AS`, and explain in one sentence **why it is a product (×) and not a sum (+)**.
5. Distinguish **threat**, **vulnerability**, and **risk** — one line each, no overlap.
6. A firewall: is it classified by *where it sits* or by *what it inspects*? Justify.
7. Ransomware hits a hospital: state the response steps in order, and name the CIA pillar each step protects.
8. State the **risk exposure** relationship from Chapter 2 and the **policy compliance index** from Chapter 6.
9. Which chapter is **excluded** from the exam?
10. Scenario drill: given a short case with **no numbers**, write the answer in the required shape — **step → CIA pillar → (techniques in parentheses)**.

---

## 23. Exam-method mapping (Dr. Huda)

The quiz is **written/essay**, roughly 10 minutes, at the start of the lecture, and the stakes are soft — it is a reading-compliance check.

| If the question gives you… | You answer with… |
|:---|:---|
| **Numbers** | Apply the formula. `S = F × K` and `R = S / M` are the two in this booklet |
| **No numbers** (analytical scenario) | **step → CIA pillar → (techniques in parentheses)** |

**Drill the two formulas until they are automatic**, and keep the CIA Triad plus its technique lists cold — they are the vocabulary every scenario answer is built from. This booklet adds two more memorisable sets that fit the same method: the **five risk-mitigation strategies** and the **four authentication factors**.

---

## 24. What this booklet does NOT cover

Stated explicitly so it does not get mistaken for a gap in your notes:

- No worked numerical example of `S = F × K` or `R = S / M` is given — the equations are defined, not exercised.
- No quantitative scale for the risk matrix is provided (no numeric bands behind red/yellow/green).
- The figures are absent from the delivered file (see flag 3).
- No coverage of Week 01's chapters — this is booklet 2 of 2.

---

*Concept outline built 2026-09-23 as the Thursday step of `PLAN_2026-09-23_to_27.md`. Every item above is drawn from the delivered booklet; nothing has been inferred or added from outside it. Open items are in §21.*
