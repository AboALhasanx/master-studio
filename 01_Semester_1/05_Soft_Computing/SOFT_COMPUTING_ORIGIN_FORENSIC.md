# تقرير جنائي — من وين جاءت مادة الحوسبة الناعمة؟ (AI أم مصدر حقيقي؟)

> **التاريخ:** 2026-10-06 · **المادة:** Soft Computing (الحوسبة الناعمة) — أ.د. عبد الهادي محمد علايدي · **المكان:** `01_Semester_1/05_Soft_Computing/`
> **السؤال:** هل مادة الحوسبة **مولّدة بالـAI** مثل الأمن السيبراني، أم لها **أصل حقيقي**؟
> **الجواب:** **لا — مو مولّدة بالـAI.** المادة **منسوخة/مُعدّلة من مصادر حقيقية**. الأمن السيبراني هو المادة المولّدة، مو الحوسبة.

---

## 1. الحكم السريع — مقارنة مباشرة

| المؤشر | 🟥 الأمن السيبراني | 🟩 الحوسبة الناعمة |
|:---|:---:|:---:|
| كثافة هيكل LLM (`Definition:/Scope:/Mathematical Model`) | **عالية (4–59 بكل ملف)** | **صفر تقريباً** |
| كلمات بصمة الـAI (`delve/crucial/comprehensive`) | 3–22 | **0** (W02-03) · 2 (W01) |
| مراجع حقيقية | **صفر** | **إي — W01 عنده مراجع** |
| الطبيعة | **مولّد بالـAI** | **منسوخ من مصادر حقيقية** |

---

## 2. الدليل — ملف ملف

### ① محاضرة البداية (Week 01) — PPTX
| الحقل | القيمة |
|:---|:---|
| `dc:creator` | **Subrat Nayak** (شخص — مو الطبيب) |
| `lastModifiedBy` | **Abd Ul Hadi Mohammed ALIADI** (الطبيب) |
| `TotalTime` | **2 دقيقة** |
| التطبيق | Microsoft Macintosh PowerPoint |

**يعني:** الطبيب أخذ عرضاً جاهزاً **من شخص اسمه Subrat Nayak** وعدّله تعديل بسيط (دقيقتان).

**وأهم شي — سلايد 30 فيه مراجع حقيقية:**
- Haykin, Simon S. *Neural Networks and Learning Machines* (2009).
- Sivanandam & Deepa, *Principles of Soft Computing*.

عرض إنساني فيه مراجع → **مو AI**.

### ② محاضرة الفازي 2–3 (Week 02-03) — PDF (112 صفحة)
**المصدر مؤكد: TutorialsPoint — «Fuzzy Logic Tutorial»** (tutorialspoint.com/fuzzy_logic/).

**الدليل — نص حرفي مطابق:**
| السلايد | TutorialsPoint (حرفياً) |
|:---|:---|
| «A set is an unordered collection of different elements…» | «A set is an unordered collection of different elements.» |
| «Mathematical Representation of a Set» | «Mathematical Representation of a Set» |
| «Set Builder Notation» | «Set Builder Notation» |
| «Member and Nonmember of a Set» | «If an element x is a member of any set S, it is denoted by x∈S» |

وكذلك قسم **Fuzzy Set Theory** (Operations on Fuzzy Sets، Properties، De Morgan) = نفس موقع TutorialsPoint.

**تفصيل مكشوف:** العنوان المدمج داخل الـPDF هو **«Bluetooth Low Energy (BLE) based Mobile Electrocardiogram Monitoring System»** (مؤلف «HCL»، PowerPoint 2007، تاريخ 2020-09-14) — يعني الديك **بُني فوق قالب قديم** من مشروع ثاني، وبس استُبدل المحتوى.

**والديك يحمل سلايدات تمارين:** HOME TASK 4/5/6.

---

## 3. ليش حدسك نصّه صح (ونصّه غلط)

- **صح:** المادة **جهدها ضعيف** — منسوخة من موقع تعليمي مبتدئ (TutorialsPoint) + عرض شخص ثاني. إحساسك إن «أكو شي مو مضبوط» **صحيح**.
- **غلط:** مو **مولّدة بالـAI**. الفرق واضح بالأرقام: CS عنده هيكل LLM وبصمات AI **وما عنده مراجع**؛ الحوسبة **ما عنده بصمات AI وعنده مراجع ومنسوخة حرفياً**.

**الخلاصة:** الأمن = **AI**. الحوسبة = **نسخ/تعديل**. مادتين مختلفتين بالمشكلة.

---

## 4. جدول تفصيلي

| الملف | الحكم | الدليل |
|:---|:---:|:---|
| `Week 01 - Introduction to Soft Computing.pptx` | 🟩 **منسوخ/مُعدّل** | creator = Subrat Nayak؛ مراجع Haykin + Sivanandam |
| `Week 02-03 - Fuzzy Logic Systems.pdf` | 🟩 **منسوخ** | TutorialsPoint حرفياً؛ قالب BLE-ECG قديم |

---

## 5. ملاحظة على الـData Mining

ذُكر إن الـDM **مشكوك** إنه AI (بس ملخّص لمادة صحيحة). **ما فحصته بعد** — فحص ثاني منفصل إذا تريد.

---

*فُحص بـ: بيانات وصفية للـPPTX/PDF (zipfile + PyMuPDF)، تحليل بنيوي آلي، فحص بصمات AI، مقارنة نصية مع المصادر، وبحث ويب للعبارات المميزة. كل الأدلة قابلة للتكرار.*
