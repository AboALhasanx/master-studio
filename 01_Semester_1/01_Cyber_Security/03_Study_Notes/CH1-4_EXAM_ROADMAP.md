---
title: "خريطة مراجعة — الجابترات 1–4 (Cyber Security)"
course: Cyber Security
subtitle: دليل سريع: من وين تدرس، شنو تحفظ، وشلون تجاوب — حتى تنجح بامتحان الدكتورة
---

# خريطة مراجعة — الجابترات 1 إلى 4

> **الهدف:** النجاح بامتحان الدكتورة. نمشي **على ملزمتها ومفرداتها** — مو على «الصح».
> **القاعدة الذهبية:** اكتب **بمفرداتها**، بس **اعرف الصح** (للاحتياط).

---

## 1. خريطة الملفات (وين تدرس)

| الجابتر | الملف المصدر | ملاحظة الشرح | الحالة |
|:---|:---|:---|:---:|
| **1 — Introduction** | `W01_Intro.pdf` | `W01_DeepDive.md` | ✅ موجود |
| **2 — Risk (كتيّب حقيقي)** | `W02_Risks_DrHuda_Booklet2.pdf` | `W02_DeepDive.md` + `W02_Formulas.md` | ✅ موجود |
| **3 — Risk (تنظيمي)** | `W03_Risks.pdf` | `W03_DeepDive.md` | ✅ جديد |
| **4 — Cryptography** | `W04_Cryptography.pdf` | `W04_DeepDive.md` | ✅ جديد |

---

## 2. الـ5 أشياء اللي **لازم** تحفظها (كل الجابترات)

1. **CIA Triad + تقنياتها** (تُكتب بين القوسين بكل جواب سيناريو):
   - **Confidentiality** (encryption · access controls · VPNs)
   - **Integrity** (hashing SHA-256 · digital signatures · version control)
   - **Availability** (redundancy · load balancing · DDoS mitigation)

2. **المعادلات** (احفظ رمزها + معناها):
   | المعادلة | الجابتر |
   |:---|:--:|
   | `min R = Σ P_i·I_i − Σ C_j` | 1 |
   | `S = F × K` · `R = S / M` | 2 |
   | `EFL = Σ P_i·I_i` · `Risk = T×V×I` · `PCI = Σw_k·c_k/Σw_k` · `PE` | 3 |
   | `C=E_K(P)` · `U≈H(K)/D` · `T_crack≈2^(k−1)/R` · `S_TLS=min(...)` · `C_attack=R·T·c` | 4 |

3. **القوائم المعدودة** (يسأل عنها كثير): 5 استراتيجيات تخفيف · 4 مجموعات تهديد · 5 خطوات دورة إدارة المخاطر · 5 خطوات دورة حياة السياسة · 5 خصائص الهاش · محتوى X.509.

4. **المصطلحات الإنجليزية** — الدكتورة تقول صراحة: **«ضروري تحضرون نفسكم بالكلمات الإنجليزية»**. الجواب بالإنجليزي.

5. **السيناريو**: اكتب **خطوة بخطوة**، سمّي **ركن CIA** بكل خطوة، واكتب **التقنيات بين قوسين**.

---

## 3. قالب جواب السيناريو (الطريقة الرسمية)

**4 مستويات (تُحفظ):**
1. **Threat Identification** — نوع التهديد + متجه الهجوم.
2. **Vulnerability & Mechanism** — ليش نجح الهجوم.
3. **Immediate Containment** — خطوات فورية.
4. **Strategic Remediation** — حلول طويلة + معايير (NIST/ISO).

**مثال (طريقة الدكتورة):**
> *"A bank customer's account drops $100,000."*
> ← الخطوة 1: **Integrity** (hashing SHA-256, digital signatures, version control) · الخطوة 2: **Availability** (redundancy, load balancing, DDoS mitigation) …

---

## 4. مصائد الامتحان (خلاصة كل الجابترات)

| # | المصيدة | الجواب الآمن |
|:--:|:---|:---|
| 1 | Vigenère = غير متماثل؟ | ❌ **متماثل** — الفرق عن Caesar = كلمة مفتاحية متكررة |
| 2 | AES كم جولة؟ | **10/12/14** |
| 3 | IT = Cyber Security؟ | ❌ الأمن **جزء من** IT |
| 4 | PDCA كم مرحلة؟ | **4** |
| 5 | دورة إدارة المخاطر كم خطوة؟ | **5** |
| 6 | `EFL` و `Risk=ΣP_i·I_i`؟ | **نفس الشي** |
| 7 | D بـ unicity؟ | **Redundancy** مو distance |

---

## 5. خطة المراجعة المقترحة (بالترتيب)

1. **الجابتر 1** — التعريفات + CIA + المعادلات الـ7 + الحالات (Stuxnet/Colonial).
2. **الجابتر 2** — `S=F×K`, `R=S/M` + 5 استراتيجيات + PDCA (المادة الحقيقية).
3. **الجابتر 3** — الأبعاد الثلاثة + دورة إدارة المخاطر + `EFL`/`PCI` + السياسات.
4. **الجابتر 4** — Caesar/Vigenère/unicity + Symmetric/Asymmetric + RSA/ECC + Hash/PKI + TLS.

**نصيحة:** كل جابتر، اقرأ الـDeepDive مالتها، بعدين **جاوب الـRetrieval Set** بصوت عالي بلا تنظر — هذا أقوى تمرين.

---
*الملفات المرتبطة: `W01_DeepDive.md` · `W02_DeepDive.md` · `W03_DeepDive.md` · `W04_DeepDive.md`.*