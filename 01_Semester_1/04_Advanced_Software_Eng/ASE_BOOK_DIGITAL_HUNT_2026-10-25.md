# ASE — مطاردة النسخة الرقمية للكتاب (تحقّق مباشر)

> **التاريخ:** 2026-10-25 · **المادة:** Advanced Software Engineering
> **السؤال:** هل يوجد `Software Engineering` (Aggarwal & Singh) كنسخة رقمية قابلة للبحث؟
> **الجواب:** **الكتاب كله صار رقمي وقابل للبحث — بملف واحد.**
> **الملف النهائي:** `02_Raw_Materials/Aggarwal_SE_3rdEd_COMPLETE/Aggarwal_SE_3rdEd_COMPLETE_Ch1-10_OCR.pdf` — **452 صفحة · 209 MB · 910,590 حرف قابل للبحث · 11 فصلاً بفهرس قفز**.

---

## 1. هوية الكتاب بالضبط

**K. K. Aggarwal & Yogesh Singh, _Software Engineering_, New Age International (P) Ltd., New Delhi.**

| الطبعة | السنة | ISBN-13 | الصفحات | الصيغة |
|:---|:---|:---|:---|:---|
| 2nd | 2005 | 978-81-241-6381-3 | ~494 | Paperback |
| **3rd** | **2008** | **978-81-224-2360-0** | **528** | **Paperback** |
| 4th | 2022 | 978-93-95161-35-0 | 515 | Paperback |
| 5th | 2026 | — | — | Paperback |

المصدر: كتالوج الناشر الرسمي (Computer Science 2020، ص.8، رمز 44) — `newagepublishers.com/Dcatalogue/1622173226Computer Science 2020.pdf`.

---

## 2. ⭐ الحصيلة: نسخة رقمية كاملة قابلة للبحث

### 2.1 الفصول 1–6 — الطبعة الثالثة، 240 DPI + OCR

**Internet Archive:** `software-engineering-3rd-ed-yogesh-singh-k-k-aggarwal-1-removed`
- مرفوعة 2024-12-17 · collection: **opensource** (تحميل مباشر، بلا قيود)
- الطبعة الثالثة، الصفحات المطبوعة **1–307** (الفصول 1–6)
- السكان الأصلي: **233 DPI** · OCR: **Tesseract 5.3.0**
- الملفات العامة: `…removed.pdf` (132 MB)، `…_text.pdf` (17 MB فيه طبقة نص)، `…_djvu.txt` (682 KB نص خام)

**شنو سويت:** أخذت **الصور بدقة 240 DPI** من الـPDF الكبير + **طبقة النص** من `_text.pdf`، ودمجتهم بملف واحد بـPyMuPDF (نص غير مرئي `render_mode=3` فوق الصورة).

**النتيجة عندنا:**
| الملف | الوصف |
|:---|:---|
| `02_Raw_Materials/Aggarwal_SE_3rdEd_InternetArchive/Aggarwal_SE_3rdEd_Ch1-6_240dpi_OCR.pdf` | **327 صفحة · 240 DPI · 654,101 حرف قابل للبحث · 137 MB** |
| `02_Raw_Materials/Aggarwal_SE_3rdEd_InternetArchive/Aggarwal_SE_3rdEd_Ch1-6_OCR_fulltext.txt` | النص الخام كامل (للـgrep) |

**فحص البحث (فعلي، على الملف النهائي):**

| الكلمة | صفحات فيها |
|:---|:---|
| cohesion | 14 |
| coupling | 20 |
| COCOMO | 23 |
| function point | 13 |
| Halstead | 11 |
| waterfall | 14 |
| SRS | 40 |
| data flow | 18 |

٤ صفحات فقط بلا نص (غلاف/فارغة). البحث بالعبارة يشتغل بعد (`Waterfall Model`, `Requirements analysis`).

### 2.2 الكتاب كامل — الطبعة الثانية، استعارة مجانية

**Internet Archive:** `softwareengineer0000agga`
- Aggarwal, K. K. · 2005 · New Age International · ISBN 978-81-241-6381-3
- **494 صفحة · 360 DPI · OCR كامل**
- `access-restricted-item: true` → **استعارة رقمية** (حساب مجاني، ساعة أو 14 يوم)، ويشتغل «search inside» بلا استعارة
- سكان IA الرسمي (Arcadia Fund) — أنظف سكان متاح، بس طبعة أقدم

---

### 2.3 الفصول 7–10 — سكان GitHub + OCR صنعناه بأنفسنا

ما لقينا نسخة رقمية للفصول 7–10 بأي مصدر عام (تفاصيل §3). فبنينا الطبقة بأنفسنا:

**الطريقة:** سكانات GitHub (202–231 DPI) → كل صفحة تُصوَّر بـ200 DPI → **RapidOCR (PP-OCR ONNX)** → النص يُكتب فوق الصفحة الأصلية كنص **غير مرئي** (`render_mode=3`) بـPyMuPDF. الصور الأصلية ما تُعاد ضغطها — الحجم نفسه تقريبًا.

**النتيجة** في `02_Raw_Materials/Aggarwal_Printed_Book_OCR_Ch7-10/`:

| الملف | صفحات | حروف | صفحات بلا نص |
|:---|:---|:---|:---|
| `Ch07_Software_Reliability_printed308-364.pdf` | 57 | 62,405 | 0 |
| `Ch08_Software_Testing_printed365-458.pdf` | 48 | 60,467 | 0 |
| `Ch09_Software_Maintenance_printed459-490.pdf` | 17 | 114,076 | 0 |
| `Ch10_Software_Certification_printed493-497.pdf` | 3 | 19,541 | 0 |
| **المجموع** | **125** | **256,489** | **0** |

**فحص البحث:**

| المصطلح | Ch07 | Ch08 | Ch09 | Ch10 |
|:---|:---|:---|:---|:---|
| test case | 2 | 24 | 5 | 1 |
| fault | 13 | 2 | 5 | — |
| cyclomatic | — | 5 | — | — |
| maintenance | 5 | — | 17 | — |
| reverse engineering | — | — | 6 | — |
| regression | — | 3 | 5 | — |
| CMM | 12 | — | 2 | 2 |

> ⚠️ حدّ: OCR آلي — دقته عالية للبحث بس مو مثالية للنسخ الحرفي. للاقتباس المباشر راجع الصورة.

---

## 3. وين المجتمع ينشرها فعلاً

| المصدر | شنو ينشر | ملاحظة |
|:---|:---|:---|
| **Internet Archive** | الكتاب المطبوع (3rd Ch1–6 + 2nd كامل) | ⭐ الأفضل — OCR جاهز |
| **mait4us.weebly.com** (كلية MAIT دلهي) | **السلايدات الرسمية مقسّمة 10 فصول، PDF مولّد من PowerPoint** | ⭐ 1094 صفحة بالضبط = نفس ملفنا، بس **نص نظيف ومقسّم** |
| **GitHub** `BhaskarAnand-05/DTU_5th_Sem_Books` | فصول 4–10 سكان + السلايدات | طلاب DTU |
| **dpbck.ac.in** (كلية هندية) | السلايدات 1094ص (`…CPENTalk.com…pdf`) | نفس ملفنا بالضبط (7,027,035 بايت) |
| **Scribd** | 2nd ed 492ص · 3rd ed 528ص | خلف اشتراك |
| **LibGen** | 2nd ed 2005، **103 صفحة بس** | ناقص |
| **Anna's Archive** | يجمّع LibGen+Z-Lib | صفحة البحث JS — ما تنقرأ بلا متصفح |
| **Telegram** | قنوات كتب هندسية عامة | مشاركة بلا فهرسة |
| **Studocu / CourseHero** | ملاحظات طلاب بس | مو الكتاب |
| **Amazon / AbeBooks / Sapna / Mybooksfactory** | الطبعة 4 (2022) و5 | **ورقي فقط بكل الأسواق** |

**السلايدات عند MAIT — روابط مباشرة:**
`mait4us.weebly.com/software-engineering.html` → `chapter_1_introduction.pdf` … `chapter_10_software_certification.pdf` (مجموعها 1094 صفحة، نص كامل، ~7 MB).

---

## 4. مقارنة الجودة النهائية

| النسخة | التغطية | الدقة | قابل للبحث |
|:---|:---|:---|:---|
| **IA مدمج (عندنا)** ⭐ | Ch1–6 (1–307) | **240 DPI** | ✅ 654k حرف |
| **GitHub + OCR (عندنا)** ⭐ | Ch7–10 (308–497) | 202–231 DPI | ✅ 256k حرف |
| GitHub خام | Ch4–Ch10 | 202–231 DPI | ❌ |
| `AliFahim` | كامل (1–500) | **95–108 DPI** | ❌ |
| IA 2nd ed (استعارة) | كامل | 360 DPI | ✅ (داخل IA) |
| MAIT سلايدات | كل الفصول | مولّد رقميًا | ✅ (سلايدات مو متن) |

**الحصيلة: الكتاب كله (Ch1–Ch10) صار قابل للبحث — 910,590 حرف إجمالًا.**

---

## 5. التوصية

1. **افتح الملف الواحد:** `Aggarwal_SE_3rdEd_COMPLETE_Ch1-10_OCR.pdf` — 452 صفحة، Ctrl+F يشتغل بكل فصل، والفهرس (bookmarks) ينقلك على أي فصل بضغطة.
2. **للمراجعة الشاملة بدقة 360 DPI** → استعر الـ2nd ed من IA (`softwareengineer0000agga`، 494 صفحة، مجاني بحساب).
3. **للسلايدات بنص نظيف مقسّم** → MAIT4us (10 ملفات، 1094 صفحة).
4. اذكر دائمًا **رقم الصفحة المطبوعة** لا رقم صفحة الـPDF.

### فهرس الملف الموحّد (صفحة PDF ← الصفحة المطبوعة)

| الفصل | صفحة PDF | المطبوعة |
|:---|:---|:---|
| مقدمة/فهرس | 1 | — |
| Ch1 Introduction | 21 | 1–20 |
| Ch2 Life Cycle Models | 41 | 21–39 |
| Ch3 Requirements | 60 | 40–138 |
| Ch4 Project Planning | 159 | 139–202 |
| Ch5 Software Design | 223 | 203–249 |
| Ch6 Software Metrics | 270 | 250–307 |
| Ch7 Reliability | 328 | 308–364 |
| Ch8 Testing | 385 | 365–458 |
| Ch9 Maintenance | 433 | 459–490 |
| Ch10 Certification | 450 | 493–497 |

> الإزاحة للفصول 1–6 = **PDF = المطبوعة + 20**. للفصول 7–10: GitHub سكان، والملف يبدأ من صفحة 328.

---

*كل نتيجة أعلاه مفحوصة مباشرة في 2026-10-25: كتالوج الناشر، Amazon (5 أسواق)، Google Books/Play، Open Library، Perlego، LibGen، GitHub API، Internet Archive metadata API، وتنزيل فعلي + فحص PyMuPDF للملفات. لا شيء مأخوذ من الذاكرة.*
