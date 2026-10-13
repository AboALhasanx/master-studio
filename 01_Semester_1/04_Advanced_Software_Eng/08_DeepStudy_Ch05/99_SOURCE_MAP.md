# SOURCE MAP — Ch05 (Software Design) — خريطة مرجعية سريعة
### اللي يربط السؤال بمصدره

## أين تجد الأشكال الأصلية

| الشكل | الموضوع | سلايد | كتاب (مطبوع) |
|---|---|---|---|
| Fig 1 | Framework of design process | 1–4 | 203 |
| Fig 2 | Two-part design process | 5 | 203 |
| Fig 3 | Informal → detailed design | 9 | 204 |
| Fig 4 | Modularity and software cost | 14 | 206 |
| Fig 5 | Module coupling (uncoupled/loose/highly) | 15–16 | 207 |
| Fig 6 | Example of coupling (student record) | 18 | 208 |
| **Fig 7** | **Types of coupling (الجدول الأساسي)** | 19–21 | 208–209 |
| Fig 8 | Example of common coupling | 22 | 210 |
| Fig 9 | Example of content coupling | 24 | 210 |
| Fig 10 | Types of cohesion | 25 | 211 |
| **Fig 11** | **Types of module cohesion (الجدول الأساسي)** | 27 | 211 |
| **Fig 12** | **Relationship between cohesion & coupling** | 31 | 213 |
| Fig 13 | Bottom-up tree structure | 33 | 214 |
| Fig 14/15 | Function oriented / structure chart | 36, 41 | 216–217 |
| Fig 16–18 | Structure chart / transaction | 42–45 | 218–219 |
| Fig 19 | Transaction-centred structure | 43 | 219 |
| Fig 20 | Class "car" (Indica, Santro…) | 63 | 227 |
| Fig 21 | The square class | 64 | 228 |
| Fig 22 | The triangle class | 66 | 229 |
| **Fig 23** | **Abstracting common features → Shape** | 68 | 229 |
| Fig 24 | Hierarchy | 70 | 230 |
| **Fig 25** | **Steps for OOD (6 خطوات)** | 72, 75 | 231–232 |
| Fig 26 | Activity diagram (process order) | 73 | 232 |
| Fig 27 | Object types (boundary/entity/control) | 75 | 233 |
| Fig 28 | State chart diagram | 78 | 235 |
| **Fig 29** | **Use case diagram (Library)** | 81 | 236 |

## الجدولان الحاسمان (احفظهما)

**Fig 7 — Coupling (best ← worst):** ⚠️ *تم التحقق من الصورة (سلايد 19) — الترتيب في الجدول مُثبَّت بسهم "Best" فوق و"Worst" تحت*
Data → Stamp → Control → External → Common → Content

**Fig 11 — Cohesion (best ← worst):** ⚠️ *تم التحقق من الصورة (سلايد 27) — 7 مستويات، "Best (high)" فوق و"Worst (low)" تحت*
Functional → Sequential → Communicational → Procedural → Temporal → Logical → Coincidental

**Fig 4 (سلايد 14) — Modularity & cost:** منحنى U — "Cost of Effort" ضد "Number of Modules"، مع **Region of Minimum Cost (M)**؛ يزيد cost-to-integrate والـcost الكلي بعد النقطة M. **معنى:** ما تزيد الوحدات "لأقصى حد" — أكو نطقة مثلى.

**Fig 12 (سلايد 31) — Relationship C&C:** شكلان — يسار "High Coupling" (روابط كثيرة متشابكة) ويمين "Low Coupling" (روابط قليلة). النص: *"a software engineer must design the modules with goal of high cohesion and low coupling"*.

**Fig 25 (سلايد 72) — OOD steps:** ⚠️ *تم التحقق* — السلايد يعرض **6 صناديق**: (1) Create use case model (2) Draw Activity Diagram (if reqd.) (3) Draw the interaction diagrams (4) Draw the class diagram (5) Draw the state chart/object diagram (if required) (6) Draw component & Deployment Diagram ← Design documents. **الكتاب أيضًا يعرض 6 خطوات** (Fig 5.25 على ص.232 = 6 صناديق، والنص يستخدم الحروف a←f) — فالكتاب والسلايدات **متطابقان**: 6 خطوات. الفرق الوحيد: سلايد 75 يكتب "a) b) d)" (ينط الحرف c) لكن المحتوى نفسه).

**Fig 29 (سلايد 81) — Library case study:** نص المتطلبات (Issue of Books — حد أقصى 4 كتب book bank و3 عامة لمدة 15 يوم، إلخ). السلايدات تعرض المخططات فقط؛ الكتاب يعرض **وصف الـuse cases الكامل**.

## مسار المجلدات

| المسار | الوصف |
|---|---|
| `04_Advanced_Software_Eng/` | مجلد المادة |
| `02_Raw_Materials/Aggarwal_Singh_SE_3rd_ed_By_Chapter/Ch05_Software_Design.pdf` | 99 سلايد |
| `02_Raw_Materials/Reference_Textbooks/AliFahim_Software_Engineering.pdf` | سكان — ص.202–248 = PDF 107–153 |
| `03_Study_Notes/Ch05_MCQ_Solved.md` | الأسئلة الرسمية محلولة — 36 |
| `03_Study_Notes/Ch05_AliFahim_vs_Slides_Audit.md` | فحص الكتاب مقابل السلايدات |
| `08_DeepStudy_Ch05/` | الساندبوكس (هذا المجلد) |
| `08_DeepStudy_Ch05/00_STUDY_SYSTEM.md` | ملف النظام |
| `08_DeepStudy_Ch05/01_TIER1_MODEL_QUESTIONS.md` | الطبقة النموذجية |
| `08_DeepStudy_Ch05/02_TIER2_DEEP_QUESTIONS.md` | الطبقة العميقة |
| `08_DeepStudy_Ch05/99_SOURCE_MAP.md` | خريطة المصادر |

---
*بُني 2026-10-12*


---

## Retrieval set (active recall)

| السؤال | الجواب |
|---|---|
| الجدولان الحاسمان؟ | جدول الاقتران (Fig. 7) + جدول التلاحم (Fig. 11) |
| أين ترتيب الاقتران؟ | Fig. 7 · سلايد 19 · كتاب ص.208–209 |
| أين ترتيب التلاحم؟ | Fig. 11 · سلايد 27 · كتاب ص.211 |
| أين خطوات OOD الست؟ | سلايد 72 (Fig. 25) · كتاب ص.232 |
| مدى الفصل؟ | 99 سلايد · كتاب ص.202–251 |
