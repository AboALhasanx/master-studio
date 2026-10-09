---
title: "Cyber Security — Chapter 1: Introduction to Cybersecurity"
subtitle: "النص الأصلي · الترجمة الحرفية · الشرح الفهمي — مع المعادلات الست"
course: "Cyber Security (CS601)"
week: 1
type: "study note — tri-layer (text · translation · explanation)"
---

# الفصل الأول — Introduction to Cybersecurity

> **دليل القراءة:** كل مقطع مقسوم ثلاث طبقات:
> **① النص الأصلي (English)** — حرفي من ملزمة الدكتورة · **② الترجمة** — حرفية بالعربي · **③ الشرح الفهمي** — الشرح اللي يفهمك المفهوم.
> **ملاحظة المصادر:** كل نص إنكليزي بين قوسين مزدوجين هو **حرفي** من `W01_Intro.pdf`.

---

## القسم 1 — التعريف والنطاق

### ① النص الأصلي

> "Cybersecurity refers to the practice of protecting systems, networks, applications, and data from cyber threats, unauthorized access, or damage. It encompasses technical, legal, managerial, and social aspects."

> "Definition: The set of tools, policies, security concepts, safeguards, risk management approaches, and technologies to protect the cyber environment."

> "Scope: Includes everything from personal devices to enterprise systems and national critical infrastructure."

### ② الترجمة

> «الأمن السيبراني هو ممارسة حماية الأنظمة والشبكات والتطبيقات والبيانات من التهديدات السيبرانية، والوصول غير المصرّح به، أو الضرر. ويشمّل جوانب تقنية وقانونية وإدارية واجتماعية.»

> «التعريف: مجموعة الأدوات، والسياسات، والمفاهيم الأمنية، ووسائل الحماية، ومناهج إدارة المخاطر، والتقنيات لحماية البيئة السيبرانية.»

> «النطاق: يشمل كل شيء — من الأجهزة الشخصية، إلى أنظمة المؤسسات، إلى البنية التحتية الوطنية الحرجة.»

### ③ الشرح الفهمي

الأمن السيبراني مو بس «حماية» — هو **ممارسة** (شي تسويه باستمرار). ولاحظ **الجوانب الأربعة**: تقني + قانوني + إداري + اجتماعي. يعني حتى لو عندك أقوى جدار ناري (تقني)، إذا ماكو **سياسة** (إداري) أو **وعي قانوني** (قانوني)، الأمن ينكسر. والنطاق يبدأ من تلفونك وينتهي بالبنية التحتية للدولة — **كل مستوى إله تهديده**.

---

## القسم 2 — التطور التاريخي

### ① النص الأصلي

> "Historical Evolution:"
>
> - 1960s: First mentions with ARPANET and early mainframes.
> - 1980s–90s: Rise of viruses, worms, and antivirus solutions.
> - 2000s: Cybersecurity becomes integral to e-commerce and e-banking.
> - 2010s–present: Advanced Persistent Threats (APT), ransomware, IoT, AI, and Zero Trust security models.

### ② الترجمة

> «التطور التاريخي: الستينيات: أول ذِكر مع ARPANET وأجهزة الـ mainframe الأولى. الثمانينيات–التسعينيات: ظهور الفيروسات والديدان وحلول مضادات الفيروسات. الألفينيات: الأمن السيبراني يصير جزءاً أساسياً من التجارة الإلكترونية والمصرفية. العقد 2010–الآن: التهديدات المتقدمة المستمرة (APT)، وبرامج الفدية، وإنترنت الأشياء، والذكاء الاصطناعي، ونماذج الثقة الصفرية.»

### ③ الشرح الفهمي

القصة **تدرّجية**: بدت الشبكات (ARPANET) بلا أمن ← طلعت الفيروسات ← صار الأمن ضرورة تجارية ← اليوم **العدو ذكي ومتطور** (APT). كل مرحلة طلّعت **تهديدها** و**ردّها**. هذا القسم يحفظ كـ**جدول أزمنة** — الدكتورة تحب تسأل عنه.

---

## القسم 3 — الأهمية

### ① النص الأصلي

> "Importance: Cybersecurity is directly linked to national security, economic stability, and privacy protection."

### ② الترجمة

> «الأهمية: الأمن السيبراني مرتبط مباشرةً بالأمن الوطني، والاستقرار الاقتصادي، وحماية الخصوصية.»

### ③ الشرح الفهمي

ثلاث كلمات مفتاحية: **أمن وطني · استقرار اقتصادي · خصوصية**. يعني خرق واحد مو «مشكلة شركة» — ممكن يهدد **دولة** كاملة. هذا اللي يرفع الأمن السيبراني من «مهمة IT» إلى «أولوية وطنية».

---

## القسم 4 — المعادلة الأولى: الأمن كمشكلة تحسين

### ① النص الأصلي

> "Mathematical Viewpoint: Cybersecurity as an optimization problem, where the goal is to minimize risk R while maximizing security investments."

### ② الترجمة

> «من منظور رياضي: الأمن السيبراني كمسألة تحسين، حيث الهدف هو تقليل الخطر R مع زيادة استثمارات الأمن.»

### ③ المعادلة + الشرح

$$\min R = \sum_{i=1}^{n} P_i \cdot I_i - \sum_{j=1}^{m} C_j$$

| الرمز | المعنى |
|:---|:---|
| $P_i$ | احتمال حصول التهديد $i$ |
| $I_i$ | تأثير التهديد $i$ |
| $C_j$ | الاستثمار في ضابط الأمان $j$ |

**الشرح:** الخطر المتوقع = مجموع (احتمال × تأثير) لكل التهديدات. ونطرح منه **الاستثمار** بالضوابط. فكرتها: نقلّل الخطر **ونزيد الاستثمار** معاً — مو حماية وخلاص.

> **قاعدة الدكتورة (تُحفظ كما هي):** إذا الناتج **أكبر من 100** ← فيه استثمار؛ إذا **أقل من 100** ← ما فيه استثمار.

---

## القسم 5 — الأهمية والنطاق والمجالات

### ① النص الأصلي

> "Cybersecurity's importance extends across multiple domains:"
>
> - Individuals: Protecting personal devices, emails, social media accounts, and banking details.
> - Enterprises: Ensuring business continuity, customer trust, and legal compliance.
> - Governments: Protecting national security, defense, and e-governance infrastructure.
> - Global Trade: Safeguarding cross-border digital commerce and financial systems.

> "Key Domains:"
>
> - Network Security (firewalls, IDS/IPS).
> - Application Security (secure coding, OWASP standards).
> - Cloud Security (encryption, IAM, virtualization).
> - IoT Security (lightweight encryption, anomaly detection).
> - Mobile Security (sandboxing, malware detection).
> - Industrial Control Systems (ICS) Security.

### ② الترجمة

> «الأفراد: حماية الأجهزة الشخصية والإيميلات وحسابات التواصل وبيانات المصرف. المؤسسات: ضمان استمرارية العمل وثقة العملاء والامتثال القانوني. الحكومات: حماية الأمن الوطني والدفاع والبنية التحتية للحكومة الإلكترونية. التجارة العالمية: تأمين التجارة الرقمية عبر الحدود والأنظمة المالية.»

> «المجالات الأساسية: أمن الشبكات (جدران نارية، IDS/IPS). أمن التطبيقات (ترميز آمن، معايير OWASP). أمن السحابة (تشفير، IAM، افتراضية). أمن إنترنت الأشياء (تشفير خفيف، كشف الشذوذ). أمن الموبايل (عزل التطبيقات، كشف البرمجيات الخبيثة). أمن أنظمة التحكم الصناعي (ICS).»

### ③ الشرح الفهمي

**أربعة مستويات** تتدرّج: فرد ← مؤسسة ← حكومة ← تجارة عالمية. و**ستة مجالات** — والدكتورة قالت: **«عدد المجالات قابلة للزيادة»** (مو رقم ثابت، احفظ الستة كأمثلة).

**المعادلة الثانية:**

$$R(t) = \sum_{i=1}^{n} P_i(t) \cdot I_i(t)$$

| الرمز | المعنى |
|:---|:---|
| $R(t)$ | الخطر عند الزمن $t$ |
| $P_i(t)$ | احتمال التهديد $i$ عند الزمن $t$ |
| $I_i(t)$ | تأثير التهديد $i$ عند الزمن $t$ |

**الشرح:** نفس فكرة الخطر، بس **مرتبطة بالزمن** — الخطر يتغيّر بمرور الوقت. **القانون مطلوب بالكامل** (لازم تعرفه وتستخدمه). بس **الـ t (الزمن) هي الجزء السطحي:** وظيفتها الوحيدة إنها **تدلّك أي قانون تستخدم** — إذا السؤال بيه **زمن (t)** ← تستخدم **هذا** القانون، مو الأول (`min R`). يعني الـ t «علامة» بالسؤال، مو شي تحسبه لحاله.

---

## القسم 6 — ثالوث CIA (الأهم) ⭐

### ① النص الأصلي

> "The CIA Triad (Confidentiality, Integrity, Availability) is the backbone of cybersecurity."

> "1. Confidentiality — Preventing unauthorized access to data. Techniques: encryption, access controls, VPNs."

> "2. Integrity — Ensuring data is accurate and unaltered. Techniques: hashing (SHA-256), digital signatures, version control."

> "3. Availability — Ensuring resources are accessible when needed. Techniques: redundancy, load balancing, DDoS mitigation."

### ② الترجمة

> «ثالوث CIA (السرية، السلامة، التوافر) هو العمود الفقري للأمن السيبراني.»

> «1. السرية — منع الوصول غير المصرّح به للبيانات. التقنيات: التشفير، ضوابط الوصول، الشبكات الخاصة الافتراضية (VPNs).»

> «2. السلامة — ضمان أن البيانات دقيقة ولم تتغيّر. التقنيات: التجزئة (SHA-256)، التوقيعات الرقمية، التحكم بالإصدارات.»

> «3. التوافر — ضمان أن الموارد متاحة عند الحاجة. التقنيات: التكرار، موازنة الحمل، التخفيف من هجمات DDoS.»

### ③ الشرح الفهمي

هذا **قلب المادة** — الدكتورة ظلّلت عليه. احفظ **الركن + تقنياته**:

| الركن | التقنيات (تُحفظ حرفياً) |
|:---|:---|
| **Confidentiality** | encryption · access controls · VPNs |
| **Integrity** | hashing (SHA-256) · digital signatures · version control |
| **Availability** | redundancy · load balancing · DDoS mitigation |

**المعادلة الثالثة:**

$$U(C, I, A) = \alpha C + \beta I + \gamma A$$

| الرمز | المعنى |
|:---|:---|
| $C, I, A$ | قيم مطبّعة (0–1) للسرية والسلامة والتوافر |
| $\alpha, \beta, \gamma$ | أوزان الأهمية لنظام معيّن |

**الشرح:** الأمان الكلي = مجموع مرجّح للأركان الثلاثة. **الأوزان تتغيّر حسب المجال** — الدكتورة قالت: **«بالرعاية الصحية، السرية (α) وزنها أعلى من التوافر»** (بيانات المريض أخطر من توقف الجهاز).

> **⭐ الأهم للامتحان:** هذي التقنيات هي **المفردات** اللي تكتبها **بين القوسين** بكل جواب سيناريو.

---

## القسم 7 — مشهد التهديدات

### ① النص الأصلي

> "The modern cyber threat landscape includes:"
>
> - Malware: Viruses, worms, Trojans, ransomware.
> - Phishing & Social Engineering: Exploiting human trust.
> - Insider Threats: Employees misusing access.
> - Advanced Persistent Threats (APTs): State-sponsored, stealthy long-term attacks.
> - IoT Attacks: Botnets (e.g., Mirai).

> "Global Trends (2023–2024):"
>
> - Ransomware damages expected to exceed $20 billion.
> - Cloud-related attacks rising due to misconfigurations.
> - AI-powered attacks growing.

### ② الترجمة

> «مشهد التهديدات الحديث يشمل: البرمجيات الخبيثة (فيروسات، ديدان، أحصنة طروادة، فدية). التصيّد والهندسة الاجتماعية (استغلال ثقة الإنسان). التهديدات الداخلية (موظفون يسيءون استخدام صلاحياتهم). التهديدات المتقدمة المستمرة (مدعومة من دول، هجمات خفية طويلة الأمد). هجمات إنترنت الأشياء (شبكات بوتنت مثل Mirai).»

> «الاتجاهات العالمية (2023–2024): خسائر الفدية متوقعة تجاوز 20 مليار دولار. ارتفاع الهجمات السحابية بسبب سوء الإعدادات. نمو الهجمات المدعومة بالذكاء الاصطناعي.»

### ③ الشرح الفهمي + المعادلة الرابعة

**المعادلة الرابعة:**

$$AS = \sum_{j=1}^{m} \left( E_j \cdot V_j \cdot A_j \right)$$

| الرمز | المعنى |
|:---|:---|
| $E_j$ | عدد نقاط الدخول المكشوفة |
| $V_j$ | درجة خطورة الثغرة (CVSS) |
| $A_j$ | قيمة الأصل للمكوّن $j$ |

**الشرح:** سطح الهجوم = كم «قابل للاختراق» نظامك. كل ما زادت نقاط الدخول أو خطورة الثغرة أو قيمة الأصل — زاد سطح الهجوم. (حاشية الطالب: **«دراسة الثغرات»**.)

---

## القسم 8 — المخاطر والثغرات والاستغلال

### ① النص الأصلي

> - Risk: Function of likelihood and impact.
> - Vulnerabilities: Weaknesses in software, hardware, or human factors. (Examples: OWASP Top 10, CVEs).
> - Exploits: Tools/methods used to take advantage of vulnerabilities.
> - Models for Risk Assessment: OCTAVE, FAIR, NIST RMF.

### ② الترجمة

> «الخطر: دالة للاحتمالية والتأثير. الثغرات: نقاط ضعف في البرمجيات أو العتاد أو العامل البشري (أمثلة: OWASP Top 10، CVEs). الاستغلال: أدوات/طرق لاستغلال الثغرات. نماذج تقييم المخاطر: OCTAVE، FAIR، NIST RMF.»

### ③ الشرح الفهمي + المعادلة الخامسة

**المعادلة الخامسة:**

$$P(R > r) = 1 - F(r)$$

| الرمز | المعنى |
|:---|:---|
| $R$ | متغيّر عشوائي يمثّل تأثير الخطر |
| $F(r)$ | التوزيع التراكمي لقيم الخطر |
| $P(R>r)$ | احتمال أن يتجاوز الخطر حداً معيّناً $r$ |

**الشرح:** احتمال أن الخطر يتجاوز حداً معيّناً = 1 ناقص احتمال أنه ضمن الحد. (حاشية: **«F(r) محصورة بين 0 و 1»** — خاصية التوزيع التراكمي.)

---

## القسم 9 — التطور والسياسات

### ① النص الأصلي

> "Policies and Frameworks:"
>
> - GDPR (EU): Data protection and privacy.
> - HIPAA (US): Healthcare information protection.
> - NIST/ISO 27001: International standards.

> "Global Perspectives:"
>
> - US → NIST CSF, Federal Cybersecurity Strategy.
> - EU → GDPR, ENISA.
> - Middle East → National Cybersecurity Councils.

### ② الترجمة

> «السياسات والأطر: GDPR (الاتحاد الأوروبي): حماية البيانات والخصوصية. HIPAA (أمريكا): حماية معلومات الرعاية الصحية. NIST/ISO 27001: معايير دولية.»

> «المناظير العالمية: أمريكا ← NIST CSF، الاستراتيجية الفدرالية. أوروبا ← GDPR، ENISA. الشرق الأوسط ← مجالس الأمن السيبراني الوطنية.»

### ③ الشرح الفهمي + المعادلة السادسة

**المعادلة السادسة:**

$$PCI = \frac{\sum_{k=1}^{n} w_k \cdot c_k}{\sum_{k=1}^{n} w_k}$$

| الرمز | المعنى |
|:---|:---|
| $c_k$ | مستوى الامتثال للمتطلب $k$ (0–1) |
| $w_k$ | وزن/أهمية المتطلب $k$ |

**الشرح:** مؤشر الامتثال = متوسط مرجّح لمستوى التزامك بالسياسات (حاشية: **«الالتزام بالسياسة/القوانين»**). كل ما ارتفع، التزامك أفضل.

---

## القسم 10 — الحالات (خارج الامتحان) ❌

> **النص الأصلي:** "Case Studies & Examples: Stuxnet (2010) … Colonial Pipeline Ransomware (2021) … GDPR Enforcement …"

**⚠️ الدكتورة شخبطت (X) على هذا الفصل — قالت ما تريده. لا تضيّع وقت عليه.**

---

## 📋 خلاصة المعادلات الست (يُحفظ)

| # | المعادلة | يقيس |
|:--:|:---|:---|
| 1 | $\min R = \sum P_i I_i - \sum C_j$ | الأمن كمشكلة تحسين |
| 2 | $R(t) = \sum P_i(t) I_i(t)$ | الخطر عبر الزمن |
| 3 | $U(C,I,A) = \alpha C + \beta I + \gamma A$ | الأمان المرجّح للـ CIA |
| 4 | $AS = \sum (E_j V_j A_j)$ | سطح الهجوم |
| 5 | $P(R>r) = 1 - F(r)$ | احتمال تجاوز الخطر حدّاً |
| 6 | $PCI = \dfrac{\sum w_k c_k}{\sum w_k}$ | مؤشر الامتثال |

**المهمة (الدكتورة دوّرتها): 1 · 3 · 4** — أتقنها.

---

## 🎯 طريقة الامتحان

- **إذا السؤال بيه أرقام** ← طبّق المعادلة واحسب.
- **إذا ما بيه أرقام** ← **سيناريو تحليلي**: خطوة بخطوة ← سمّي ركن CIA ← اكتب التقنيات بين قوسين.
- **احفظ CIA + تقنياتها** حرفياً (مفردات الجواب).

---

## Retrieval set — أسئلة استرجاع

**1. عدّد الجوانب الأربعة للأمن السيبراني.**
> تقني (technical) · قانوني (legal) · إداري (managerial) · اجتماعي (social).

**2. شنو نطاق الأمن السيبراني؟**
> من الأجهزة الشخصية ← أنظمة المؤسسات ← البنية التحتية الوطنية الحرجة.

**3. اكتب مراحل التطور التاريخي الأربعة.**
> 1960s (ARPANET) · 1980s–90s (فيروسات/مضادات) · 2000s (تجارة إلكترونية/مصرفية) · 2010s–الآن (APT/ransomware/IoT/AI/Zero Trust).

**4. بماذا يرتبط الأمن السيبراني مباشرةً؟**
> الأمن الوطني · الاستقرار الاقتصادي · حماية الخصوصية.

**5. اكتب معادلة الأمن كمشكلة تحسين، واشرحها.**
> $\min R = \sum P_i I_i - \sum C_j$ — نقلّل الخطر (مجموع احتمال×تأثير) ونطرح الاستثمار بالضوابط. **قاعدة: >100 استثمار، <100 لا.**

**6. عدّد المستويات الأربعة والمجالات الستة.**
> المستويات: Individuals · Enterprises · Governments · Global Trade. المجالات: Network · Application · Cloud · IoT · Mobile · ICS.

**7. عدّد أركان CIA وتقنيات كل ركن.**
> Confidentiality (encryption · access controls · VPNs) · Integrity (hashing SHA-256 · digital signatures · version control) · Availability (redundancy · load balancing · DDoS mitigation).

**8. اكتب معادلة الدالة النافعة الأمنية واشرح الأوزان.**
> $U(C,I,A) = \alpha C + \beta I + \gamma A$ — الأوزان تتغيّر حسب المجال (بالرعاية الصحية α أعلى من التوافر).

**9. عدّد التهديدات الحديثة الخمسة.**
> Malware · Phishing/Social Engineering · Insider Threats · APTs · IoT Attacks.

**10. اكتب معادلة سطح الهجوم واشرح رموزها.**
> $AS = \sum (E_j V_j A_j)$ — E = نقاط الدخول · V = خطورة الثغرة (CVSS) · A = قيمة الأصل.

**11. اكتب معادلة احتمال تجاوز الخطر حدّاً.**
> $P(R>r) = 1 - F(r)$ — F(r) توزيع تراكمي محصور بين 0 و 1.

**12. شنو نماذج تقييم المخاطر؟ وشنو معادلة الامتثال؟**
> النماذج: OCTAVE · FAIR · NIST RMF. الامتثال: $PCI = \sum w_k c_k / \sum w_k$.

**13. ليش الفصل السابع خارج الامتحان؟**
> لأن الدكتورة شخبطت عليه (X) وقالت ما تريده.

**14. شنو الفرق بين سؤال الأرقام وسؤال السيناريو؟**
> إذا بيه أرقام ← طبّق المعادلة. إذا ما بيه ← سيناريو تحليلي (خطوة ← ركن CIA ← التقنيات بين قوسين).

---
*المصدر: `W01_Intro.pdf` (+ النسخة المعلَّمة). التفاصيل المطوّلة: `W01_DeepDive.md` · `W01_Annotation_Map.md`.*
