---
title: "ورقة امتحانية — الجابتر السادس: أمن تطبيقات الويب"
course: "Cyber Security (CS601)"
subtitle: "الخلاصة المكثّفة: الثغرات · الأدوات · الممارسات · المعادلات · المصائد · المفردات"
week: 6
type: "exam sheet (condensed)"
---

# 🎯 ورقة امتحانية — الجابتر السادس
## Web Application Security · المصدر: 23 صفحة ← الورقة: 4 صفحات

> **قاعدة الاستعمال:** اقرا هذي الورقة **أولاً وبورقة وقلم**. لا تفتح الـtri-layer إلا لما شي يلخبطك.
> **⭐ المستند الثالث فقط** فيه الثغرات — الباقي كلام إداري.

---

## 1️⃣ الثغرات الست (الأهم — احفظ الجدول حرفياً)

| الثغرة | كيف تشتغل | الحماية |
|:---|:---|:---|
| **SQL Injection (SQLi)** | إدخال المستخدم يدخل مباشرة بالاستعلام. تنويعات: **blind SQLi** · **NoSQL injection** | **Parameterized queries / prepared statements** + input validation |
| **Cross-Site Scripting (XSS)** | JavaScript خبيث ينفّذ بمتصفّح الضحية. تنويع: **DOM-based** (بالـSPAs) | **Output encoding** + **CSP** + sanitization |
| **CSRF** | يخدع المتصفّح يرسل طلب **مصادَق عليه** بدون علم الضحية | **SameSite cookie** + **anti-CSRF tokens** |
| **API / Microservices** | **BOLA** (تخويل الكائن مكسور) + **excessive data exposure** | Object-level authorization + schema validation + rate limiting |
| **Supply Chain** | مكتبات طرف ثالث بلا تدقيق · **dependency confusion** · **malicious package injection** | Dependency vetting + **SCA** + **pinning** |
| **Cloud-Native / Serverless** | **container misconfigurations** · **insecure orchestration** (K8s API) · **event injection** | Hardening + policy enforcement + monitoring |

> **الجذر الجامع (اكتبه بأي جواب سيناريو):** إدخال غير موثوق يوصل لـ sink حسّاس — والتحقق + الترميز (encoding) + التخويل يقطعون السلسلة.

---

## 2️⃣ المبادئ الاستراتيجية الأربعة

| المبدأ | المعنى بجملة |
|:---|:---|
| **Defense-in-Depth** | طبقات متراكبة — كل طبقة تفترض إن اللي قبلها انكسرت |
| **Zero Trust** | «Never Trust, Always Verify» — الداخل مو موثوق تلقائياً |
| **Security by Design** | الأمن من التصميم (shift-left)، مو يُضاف لاحقاً |
| **Risk-Based Prioritization** | الموارد محدودة ← نرتّب حسب الخطر (CVSS · FAIR) |

---

## 3️⃣ الأدوات والممارسات (تعداد — يُحفظ)

**الأدوات (Tools):**
- **WAF** — فلترة بطبقة التطبيق (ضابط **تعويضي**، ما يصلّح الثغرة)
- **Vulnerability Scanners** — كشف آلي
- **RASP** — حماية **داخل** التطبيق، تشوف البيانات بعد فك التشفير
- **Penetration-Testing Platforms** — يمسك اللي يفوت على السكانر
- **SIEM + Threat Intelligence** — ربط الأحداث + مؤشرات
- **Emerging Tools** — ML/AI + ترقيع آلي

**الممارسات (Practices):**
- **Secure Coding** · **Authentication & Authorization** · **Secure Configuration & Hardening** · **Continuous Monitoring & IR** · **DevSecOps & Lifecycle**

---

## 4️⃣ المعادلات (6)

| المعادلة | المعنى |
|:---|:---|
| $V_{t+1} = V_t(1-\alpha) + \beta$ | تقليل الثغرات بدورات DevSecOps — فعّال إذا $\alpha > \beta/V_t$ |
| $R_i = L_i \cdot S_i \cdot I_i$ | خطر الثغرة = احتمال × شدّة × أثر |
| $R(t) = e^{-\lambda t}$ | الموثوقية عبر الزمن ($\lambda$ = معدل الفشل **+ النشاط العدائي**) |
| $R_{sys} = 1 - \prod_{i=1}^{n}(1-R_i)$ | موثوقية **المتوازي** (redundancy) ← الموثوقية **تطلع** |
| $R = \prod_i R_i$ | موثوقية **السلسلة** ← الموثوقية **تنزل** |
| $A = \dfrac{MTBF}{MTBF + MTTR}$ | التوافر (Availability) |

---

## 5️⃣ المصائد (10)

| # | المصيدة | الجواب |
|:--:|:---|:---|
| 1 | الوقاية من SQLi؟ | **Parameterized queries** |
| 2 | الوقاية من XSS؟ | **Output encoding + CSP** |
| 3 | WAF يكفي؟ | ❌ ضابط **تعويضي** — ما يصلّح الثغرة |
| 4 | CSRF = XSS؟ | ❌ XSS ينفّذ كود · CSRF يستغل الجلسة **بدون** كود |
| 5 | Strategy = Tactics؟ | ❌ Strategy أطر مستدامة · Tactics رد فعل |
| 6 | Security by Design = فايروول بالأخير؟ | ❌ الأمن **من التصميم** |
| 7 | RTO = RPO؟ | ❌ RTO = زمن التوقف · RPO = **بيانات** مفقودة |
| 8 | نضيف redundancy ← الموثوقية؟ | **تطلع** (parallel) · بالسلسلة **تنزل** |
| 9 | Cloud = مسؤولية المزوّد؟ | ❌ **shared responsibility** |
| 10 | BOLA = excessive data exposure؟ | ❌ BOLA = **تخويل** · Excessive = **كشف بيانات** |

---

## 6️⃣ المفردات الإنكليزية (الأستاذة تشدّد عليها)

`vulnerability` · `exploit` · `exploitability` · `remediation` · `patching` · `hardening` · `least privilege` · `object-level authorization (BOLA)` · `excessive data exposure` · `dependency confusion` · `container misconfiguration` · `orchestration` · `event injection` · `redundancy` · `failover` · `business continuity` · `disaster recovery` · `availability` · `resilience` · `compensating control`

**RTO** = Recovery Time Objective (شكد نتوقف) · **RPO** = Recovery Point Objective (شكد بيانات نخسر)

---

## أسئلة استرجاع (غطّها واختبر نفسك)

**1. الثغرات الست + حماية كل واحدة؟**
> SQLi ← parameterized queries · XSS ← output encoding + CSP · CSRF ← SameSite + tokens · API ← object-level authz · Supply Chain ← SCA + pinning · Cloud ← hardening.

**2. المبادئ الأربعة؟**
> Defense-in-Depth · Zero Trust · Security by Design · Risk-Based Prioritization.

**3. الأدوات الخمس + الناشئة؟**
> WAF · Scanners · RASP · Pen-test · SIEM — والناشئة ML/AI + ترقيع آلي.

**4. الممارسات الخمس؟**
> Secure Coding · Auth/Authz · Hardening · Monitoring & IR · DevSecOps.

**5. شنو BOLA؟**
> Broken Object-Level Authorization — المستخدم يوصل لكائن ما إله حق فيه (ما كو تحقق من الملكية).

**6. شنو dependency confusion؟**
> حزمة خبيثة بنفس اسم حزمة **داخلية** ← مدير الحزم يسحبها.

**7. الفرق Series/Parallel بالموثوقية؟**
> Series ← تنزل ($\prod R_i$) · Parallel/Redundancy ← تطلع ($1-\prod(1-R_i)$).

**8. RTO و RPO؟**
> RTO = زمن التوقف المسموح · RPO = البيانات المسموح خسارتها.

**9. WAF مقابل RASP؟**
> WAF بطبقة التطبيق (يُعمى بالتشفير) · RASP داخل التطبيق (يشوف البيانات بعد فك التشفير).

**10. الدرس الجامع؟**
> الأمن **نُظُمي** = حوكمة + تقنية + تحليل كمّي — من التصميم (shift-left) إلى الصمود (continuity).

---

*المرجع الكامل (61 صفحة): `W06_Chapter6_TriLayer.pdf`. هذي الورقة = ما تحتاجه للامتحان. المرجع = لما شي يلخبطك.*
