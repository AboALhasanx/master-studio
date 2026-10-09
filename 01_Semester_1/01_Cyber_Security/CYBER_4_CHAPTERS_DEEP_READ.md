---
title: "قراءة عميقة — الجابترات الأربعة (W01 · W02 · W03 · W04)"
subject: "01_Cyber_Security"
created: "2026-10-07"
scope: "النص الكامل + كل المعادلات + تحليل التكرار والهشاشة الأكاديمية"
---

# قراءة عميقة — الجابترات الأربعة

> **ملاحظتك:** «أكو تكرار غير منطقي للكلام بشكل غريب جداً… المادة هشة أكاديمياً… كانه نسخة مجانية من GPT أو DeepSeek R1».
> **الحكم المسبق:** حدسك **صحيح**. أدناه: القراءة الكاملة + إثبات التكرار بالأرقام.

---

## 0. خريطة الجابترات (ولاحظ الفوضى بالترقيم من الأصل)

| الملف | العنوان داخل الملف | الصفحات | الترقيم الداخلي |
|:---|:---|:---:|:---|
| **W01_Intro** | "Chapter 1: Introduction…" | 5 | يحتوي **7 فصول مصغّرة** (Ch.1–Ch.7) بملف واحد! |
| **W02** (كتيّب) | "3 — What Is Risk?" | 24 | يبدأ برقم **"3"** (رقم فصل Sharp) |
| **W03_Risks** | "Introduction: Cybersecurity Risks…" | 14 | بلا رقم |
| **W04_Cryptography** | "**Week 3**: Cryptography Basics" | 18 | يسمّي نفسه **"Week 3"** (!!) |

**⇒ أول خلل:** W04 (التشفير) معنون **"Week 3"**، وW01 يحتوي 7 فصول دفعة واحدة. **الترقيم نفسه فوضى.**

---

## 1. الجابتر الأول — W01_Intro (5 صفحات)

**البنية: 7 «فصول» مصغّرة، كل واحد ينتهي بـ«نموذج رياضي» مُختَرَع.**

| الفصل الداخلي | المحتوى | المعادلة المُختَرَعة |
|:---|:---|:---|
| Ch.1 Introduction | تعريف، نطاق، تطوّر تاريخي، أهمية | `min R = Σ P_i·I_i − Σ C_j` |
| Ch.2 Importance & Scope | أفراد/شركات/حكومات + مجالات (Network/App/Cloud/IoT/Mobile/ICS) | `R(t) = Σ P_i(t)·I_i(t)` |
| Ch.3 The CIA Triad | Confidentiality/Integrity/Availability + تقنيات كل واحدة | `U(C,I,A) = αC + βI + γA` |
| Ch.4 Threat Landscape | Malware/Phishing/Insider/APT/IoT | `AS = Σ(E_j·V_j·A_j)` |
| Ch.5 Risks, Vulns, Exploits | Risk = likelihood × impact + OCTAVE/FAIR/NIST | `P(R>r) = 1 − F(r)` |
| Ch.6 Evolution & Policy | GDPR/HIPAA/NIST/ISO + منظور عالمي | `PCI = Σ w_k·c_k / Σ w_k` |
| Ch.7 Case Studies | Stuxnet 2010 · Colonial Pipeline 2021 · GDPR fines | — |

**نقطة مهمة:** CIA Triad + تقنياتها (encryption/access controls · hashing/digital signatures · redundancy/load balancing) — **هذي هي «مفردات» الامتحان** اللي تكتبها بين القوسين بأجوبة السيناريو.

---

## 2. الجابتر الثاني — W02 (كتيّب المخاطر، الحقيقي)

هذا **نص Sharp Ch.3 حرفياً** (+ مصدر ثانٍ للأمن الفيزيائي). المحتوى الحقيقي:
- تعريف المخاطرة (موضوعية/ذاتية) · `S = F × K` · `R = S / M` · مصفوفة المخاطر والخطر المتبقي (رتّبية لونية)
- 4 مجموعات تهديد: **Hardware · Software · Data · Liveware**
- 5 استراتيجيات تخفيف: Avoidance/Reduction/Retention/Transfer/Sharing
- COBIT · COSO · FAIR · ISO/IEC 27002 · OCTAVE · PDCA
- (ثم يلصق مصدراً ثانياً: أقفال، بطاقات، RFID، بصمات — **مو من Sharp**)

---

## 3. الجابتر الثالث — W03_Risks (14 صفحة) — **مولّد AI**

**البنية (لاحظ التكرار الداخلي):**
1. Cybersecurity as Organizational Risk + "Why?" (4 نقاط)
2. Why Risk Management is Strategic (Financial / Operational / Reputational) — **`EFL = Σ P_i·I_i`**
3. Bridging Technical Controls & Governance
4. Risk Management as Continuous Process (Identify/Assess/Prioritize/Mitigate/Monitor)
5. Future Challenges (Cloud/IoT/AI/Quantum)
6. **«Importance of Risk Management»** ← يعيد كل شي: تعريف المخاطرة، `Risk = Threat×Vuln×Impact`، `Risk = Σ P_i·I_i`، أمثلة مصرفية/صحية
7. **«Creating and Enforcing Security Policies»** ← `PE = (before−after)/before` + `PCI`
8. **«Role of Policy in Enterprise Security»** ← **`PCI` مرة ثانية** بنفس المثال (بنك، 0.78)

**⇒ تكرار صارخ:** مفهوم المخاطرة موضّح **3 مرات** (أقسام 1، 6)، و`PCI` معرّف **مرتين** بنفس المثال، و`EFL`/`Σ P_i·I_i` **مرتين**.

---

## 4. الجابتر الرابع — W04_Cryptography (18 صفحة) — **مولّد AI**

**البنية: 4 «أقسام» كبيرة، كل قسم ينتهي بـ«نموذج رياضي»:**

| القسم | المحتوى | المعادلات |
|:---|:---|:---|
| §1 History | Caesar `E(x)=(x+k)mod26` · Vigenère `C_i=(P_i+K_i)mod26` · unicity `U≈H(K)/D` | 3 معادلات (هذي **حقيقية** — رياضيات قياسية) |
| §2 Sym vs Asym | `C=E_K(P)`, `P=D_K(C)` · DES/AES/ChaCha20 · RSA `n=pq, φ(n)`, `C=P^e mod n` · ECC · hybrid TLS | `T_crack≈2^(k−1)/R` · `T_system=min(T_sym,T_asym)` |
| §3 Hash/Signatures/PKI | hash props · `Sig=E_Priv(h(M))` · X.509/PKI | `P_int≈2^(−n)` · `P_trust=(1−P_ca)(1−P_val)` · `P_secure=(1−P_int)(1−P_sig)(1−P_trust)` |
| §4 Real-World (TLS) | HTTPS/TLS handshake · banking/e-commerce/email/blockchain | `S_TLS=min(S_sym,S_asym,S_hash)` · `C_attack=R·T_crack·c` |

**ملاحظة منصفة:** تشفير W04 **أفضل بكثير** من W01/W03 — لأنه يعتمد على **مفاهيم ورياضيات قياسية حقيقية** (RSA, ECC, SHA-256, TLS) الـLLM يعرفها صح. الخلل هنا مو بالوقائع، بل **بالتكرار** وبالصيغ «النموذجية» المضافة في النهاية.

---

## 5. ⭐ تحليل التكرار — اللي حسّيت بيه (بالأرقام)

### 5.1 تكرار **داخل** W04 (ملف واحد)

| الشي المتكرر | شكد مرة | الأماكن |
|:---|:---:|:---|
| `S_system = min(S_sym, S_asym, S_hash)` | **2** | §2 (5.4) + §4 (4.2) |
| TLS Handshake خطوة-بخطوة | **2** | §2 (نموذج) + §4 (2.2) |
| DigiNotar 2011 | **2** | §3 (Case 1) + §4 (5.2) |
| «Asymmetric = session key · Symmetric = bulk» | **3+** | §2, §4 |
| RSA-2048≈112 / ECC-256≈128 بت | **3** | §2, §4 (مرتين) |
| Quantum (Shor/Grover) | **2** | §2 (Case 4) + §4 (5.1) |
| Heartbleed / downgrade / side-channel | **2** | §3 + §4 |
| «نموذج رياضي» منفصل | **5** | كل قسم + نموذج اقتصادي |

**⇒ §4 كامل تقريباً = إعادة لِـ§2 و§3.** «Real-World Applications» يعيد TLS + الهجين + الحالات.

### 5.2 تكرار **بين** الملفات

| الشي | W01 | W03 | W04 |
|:---|:---:|:---:|:---:|
| `PCI` | ✅ (Ch.6) | ✅ **مرتين** | — |
| `EFL = Σ P_i·I_i` | — | ✅ **مرتين** | — |
| `Risk = likelihood × impact` | ✅ (Ch.5) | ✅ | — |
| CIA Triad | ✅ | — | ✅ (مفهومياً) |
| Quantum threat | ✅ (Ch.4) | ✅ | ✅ **مرتين** |

**⇒ نفس المفاهيم تتكرر عبر 3 ملفات مختلفة، وأحياناً بنفس الصيغة حرفياً.**

---

## 6. الهشاشة الأكاديمية (شنو بالضبط ضعيف)

| العلامة | التفصيل |
|:---|:---|
| **صفر مراجع** | لا استشهادات، لا DOI، لا «et al.» بكل الملفات |
| **معادلات مُختَرَعة** | `EFL`, `PCI`, `min R`, `U(C,I,A)`, `AS`, `R(t)` — **مو موجودة بأي مرجع** (مو بـSharp، مو بالمعايير) |
| **«نموذج رياضي» قالب** | كل قسم/فصل يُختم بـ«Mathematical Model» — **قالب LLM**، مو بنية أكاديمية |
| **عناوين بنمط SEO** | "What Are Malware Detection Techniques…?" |
| **سلطة مفردات** | "fiduciary stewardship", "orchestrate" (W16) — محتوى ضبابي بمفردات فخمة |
| **تكرار القوالب** | W07: Viruses→How They Work→Example→Worms→… (حلقة) |
| **فوضى الترقيم** | W04 = "Week 3" · W01 = 7 فصول · W02 = يبدأ بـ"3" |
| **خلط مصادر** | كتيّب W02 = Sharp + مصدر ثانٍ بلا إشارة |

**الخلاصة:** المادة **متماسكة سطحياً** (الوقائع العامة صحيحة) لكن **هشّة هيكلياً**: تتكرر، تلفّق معادلات، تخلط مصادر، وتفتقر لأي مرجع. هذي بصمة **نموذج صغير/رخيص**، مو تحرير أكاديمي.

---

## 7. تحليل النموذج (GPT مجاني؟ DeepSeek R1؟)

**ملاحظتك:** «كانه نسخة مجانية من GPT أو DeepSeek R1، مو v4/v4.1».

**ما تشير إليه الأدلة (بلا قطع):**
- **قالب «Definition → Scope → Importance → Mathematical Model → Where:»** = أسلوب مخرجات LLM العامة.
- **«نموذج رياضي» لكل قسم** = حشو لتبدو «علمية» (بلا أساس).
- **التكرار الحلقي** = سلوك نماذج **أصغر/أقدم** (تفقد التماسك على النصوص الطويلة) — النماذج الأكبر تحافظ على التماسك وتتجنب إعادة التعريف.
- **الوقائع العامة صحيحة، الصيغ المُخصّصة مُختَرَعة** = نموذج «يعرف الظواهر، يلفّق الرياضيات».

**الفرضية المعقولة:** كُتبت الملفات بـ**نموذج استدلالي/رخيص (نوع R1)** — يولّد نصاً طويلاً منظّماً لكنه **يكرر ويعيد التعريف** بدل بناء تراكمي. **هذا يتوافق تماماً مع حدسك.**

⚠️ **تحذير:** لا أقدر أجزم بالنموذج بالضبط (البيانات الوصفية تقول فقط Microsoft Word / riyadhrahef). هذا **تحليل أسلوبي**، مو إثبات.

---

## 8. الخلاصة العملية

1. **حدسك صح:** تكرار غريب + هشاشة أكاديمية + بصمة نموذج رخيص.
2. **الأنفع:** الجابتر الثاني (W02) = الحقيقة (Sharp). W04 (تشفير) = مقبول (مفاهيم قياسية). W01/W03 = هشّة (معادلات مُختَرَعة).
3. **للامتحان:** جاوب بمفرداتها، بس اعرف إن المعادلات المُختَرَعة مو قياسية.

---

*النصوص مستخرجة حرفياً من `02_Raw_Materials/W01…W04` (PyMuPDF). المعادلات منقولة كما ظهرت في الملفات.*
