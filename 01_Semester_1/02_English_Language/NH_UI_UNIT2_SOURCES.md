---
title: "New Headway Upper-Intermediate — Unit 2 (Been there, done that!) — Sources Discovery"
subject: "02_English_Language"
unit: "Unit 2 — Been there, done that!"
book: "New Headway Upper-Intermediate — Third Edition (Oxford, 2005)"
discovered: "2026-10-10"
phase: "PRE-CREATION — مصادر فقط، ما كُتب حل بعد"
verdict: "المصدر الرسمي الكامل موجود محلياً (Teacher's Book) وتمّ تحويله لنصّ قابل للبحث. لا حاجة لأي مصدر خارجي للتحقق."
---

# استكشاف مصادر Unit 2 — New Headway Upper-Intermediate

> **الهدف:** نحدّد **أهم المصادر المتاحة** لحل الجابتر قبل ما نكتب أي حل.
> **الخلاصة بسطر:** 🥇 **كتاب المعلّم الرسمي موجود عندنا محلياً** (194 ص، Oxford 2005) — وحوّلته **لنصّ قابل للبحث بالـOCR**، وفيه **مفتاح الحلول + نصوص التسجيلات + الشرح**. يعني **ماكو حاجة** لأي مفتاح مقرصن.

---

## 1. المصادر المحلية (🥇 الأساس)

| # | الملف | الصفحات | الحالة | القيمة |
|:--|:--|:--|:--|:--|
| 1 | **`NH Upper Intermediate - Teacher Book (Answer Key).pdf`** | **194** | سكان، صفر نص | 🥇 **مفتاح الحلول الرسمي + Tapescripts + الشرح** |
| 2 | `Upper Intermediate - Unit 2 - Been There Done That.pdf` | 10 | سكان، صفر نص | 🎯 **كتاب الطالب — اليونت نفسه** |
| 3 | `New Headway Upper-Intermediate (Student Book).pdf` | 159 | سكان، صفر نص | الكتاب الكامل (مرجع) |
| 4 | `Upper Intermediate - Unit 1 - No Place Like Home.pdf` | 10 | سكان، صفر نص | اليونت الأول (نموذج للمقارنة) |
| 5 | `CamScanner Scan - Grammar Worksheet (No Place Like Home).pdf` | — | سكان | ورقة قواعد لليونت 1 |

### ⚠️ حقيقة تقنية مهمة
**كل** ملفات New Headway عندنا **سكان خالص — صفر طبقة نصية**. يعني:
- ما ينفع `get_text()` إطلاقاً.
- لازم **قراءة بصرية** أو **OCR**.

### 🎯 ما نُفّذ فعلاً (وسبق الاستكشاف)
`pdf_reader.py --ocr` (RapidOCR محلي) على **صفحات 20–30** من كتاب المعلّم ← **45,103 حرف** نصّ نظيف.

**المحفوظ:** `02_Raw_Materials/NH_UI_TeacherBook_Unit2_OCR.md` ✅ (المجلد محجوب عن git — تأكدت بـ`git check-ignore`)

**يحتوي:** صناديق **Answers** (45 صندوق) + **Tapescripts T2.1/T2.2/T2.3** + `TEST YOUR GRAMMAR` + شرح القواعد + جدول hot verbs (make/do) + Exclamations + أجوبة القراءات والاستماع.

**تحقق من التطابق:** الملف يذكر **Marco Polo ×5** و **Tommy Willis ×4** و **Tashi ×11** — وكتاب الطالب عنده Marco Polo/Tommy Willis ✓ ⇒ **كتاب المعلّم مطابق لطبعة كتاب الطالب** (لا مشكلة طبعة).

### 🔢 تحديد صفحات Unit 2 (خريطة مثبتة)
بنيت خريطة من **تذييل كل صفحة** من كتاب المعلّم:

| اليونت | صفحات الكتاب | صفحات الـPDF |
|:--|:--|:--|
| Unit 1 — No place like home | 7–18 | 8–19 |
| **Unit 2 — Been there, done that!** | **19–29** | **20–30** |
| Unit 3 — What a story! | 31–39 | 32–40 |
| Unit 4 — Nothing but the truth | 41–43+ | 42–44+ |

> **درس:** تذييل الصفحة (`Unit 2 · Been there, done that!  19`) هو أسرع طريقة لتحديد حدود أي يونت بكتاب مصوّر — اجمعها بشريط واحد واقرأها.

---

## 2. المصادر الرسمية على النت (✅ موثوقة)

| # | المصدر | شنو يعطي | ملاحظة |
|:--|:--|:--|:--|
| 6 | **`elt.oup.com/student/headway/upperintermediate/grammar/unit02/`** | **موقع Oxford الرسمي** — تمارين تفاعلية لـUnit 2 | **يصحّح آلياً** ✅ |
| 7 | ↳ `.../unit02/hwy_upp_unit02_1` | **Present Perfect Simple and Continuous** — "Choose the correct answers" | **الطبعة الرابعة** — نفس القاعدة، جمل مختلفة |
| 8 | ↳ `.../unit02/hwy_upp_unit02_2` | **Present Perfect and Past Simple** | نفس الملاحظة |
| 9 | `.../vocabulary/` · `.../everydayenglish/` · `.../download` · `.../testbuilder` | مفردات · إنجليزية يومية · **تحميل صوتيات وفيديو** · باني اختبارات | لكل يونت |
| 10 | `elt.oup.com/teachers/headway/` (Teacher's Site) | موارد المعلّم | بعضها بكود |

> **ملاحظة صدق:** موقع الطالب هو **الطبعة الرابعة**، فما يعطي **حلول تمارين كتابنا** حرفياً — بس يعطي **تدريب رسمي على نفس القاعدة** وتأكيد إن التراكيب صحيحة.

---

## 3. يوتيوب — محاضرات عربية على نفس اليونت (🥈)

سُحبت الترجمات التلقائية بـ`yt_dlp` وفحصت محتواها. **الترتيب حسب المطابقة لكتابنا:**

| # | الفيديو | القناة | المدة | المطابقة |
|:--|:--|:--|:--|:--|
| 11 | **`UNIT5Nj0Mik`** | Nada Aziz Yousif | 46 د | 🥇 **الأقرب** — يذكر *"present perfect simple and continuous · hot verbs make/do · exclamations"* + **Tashi** + **tourism ×20** |
| 12 | **`97CT2BYa5lE`** | محاضرة المرحلة الرابعة (مساعد د. ياسر عبد الستار) | 58 د | 🥈 **New Headway Plus** — present perfect ×16 · hot verbs ×3 · exclamations ×2 · Marco Polo ×3 |
| 13 | **`f7IGUU4vhRc`** | Sarab Al-Akraa | 31 د | 🥈 present perfect ×30 · hot verbs ×2 · make ×35 — يبدأ من **Test your grammar** |
| 14 | `aRQwTkUjf_c` | Myo Thuya Kyaw | 19 د | ⚠️ **الطبعة الرابعة** — نصّ الشريط 2.1 Marco Polo |
| 15 | `pDb6B8q-bOY` | Marwa Mousa | 13 د | ⚠️ *NEW HEADWAY PLUS* — نصّ الشريط 2.1 (قائمة دول + Where are you from) |
| 16 | **بلا ترجمات** (تحتاج تفريغ يدوي) | — | — | — |
| 16أ | `dfCCRMovKo4` — **كلية اللغات / جامعة بغداد** — *"been there, done that"* | College of Languages | 15 د | 🎯 **عنوان يونتنا حرفياً** — بس **ماكو ترجمات** |
| 16ب | `MVI5SxReUDM` — **أ.م.د. ياسر عبدالستار** | دروس ومحاضرات | 58 د | نسخة أخرى من #12 |
| 16ج | `FNnKSWxeYXc` (Rasha Saeed) · `vDWA1ss1hmc` (Thaer Roomi) | — | 15/29 د | عناوين مطابقة، بلا ترجمات |

**المحفوظ:** ترجمات 5 فيديوهات بـ`%TEMP%\nhsubs\` (en + ar).

> **تحذير مطابقة:** لازم تتأكد من **الطبعة** قبل الاعتماد على أي فيديو — فيديوهات "Marco Polo" كـ*نصّ شريط 2.1* تعني طبعة مختلفة التركيب. الفيديوهات اللي تذكر **Tashi** هي الأقرب لكتابنا.

---

## 4. مصادر فُحصت ورُفضت (لا تضيّع وقتك)

| المصدر | السبب |
|:--|:--|
| `sbk.wallace.outthinkgroup.com/.../New Headway Upper Intermediate Student Answer Key.pdf` | **404 + شهادة SSL مغشوشة** — رابط SEO وهمي |
| `kingsridgecofc.org/pdf/...teachers-book` | صفحة **تسويق كتاب**، مو الكتاب |
| `pdfcoffee.com/efthirdeduppintworkbookkeypdf` | **English File**، مو Headway — نتيجة خاطئة |
| `pdfcoffee.com/headway-5th-edition-...workbook-answer-key` | **الورك بوك، الطبعة الخامسة** — مو كتابنا + محجوب بـCloudflare |
| `studifor.com/.../new-headway-upper-intermediate-workbook-5th-edition` | **الورك بوك، الطبعة الخامسة** — تنظيم مختلف (Language focus/Vocabulary/Pronunciation) |
| `sciarium.com/file/525402/` | الورك بوك 5th — وsciarium محجوبة بكابتشا |
| مواقع الحلول المدفوعة | لا حاجة — عندنا الرسمي |

---

## 5. 🧭 خريطة الطبعات (الأهم — تمنع الخطأ)

| الطبعة | وحدة 2 | ملاحظة |
|:--|:--|:--|
| **الثالثة (2005) ← كتابنا** | **Present Perfect · Simple and continuous · Hot verbs make/do · Exclamations** — قراءة **Marco Polo + Tommy Willis** + استماع **Tashi Wheeler (Lonely Planet)** | ✅ **كتاب المعلّم عندنا يطابقها** |
| الرابعة | Unit 2 — نصّ الشريط 2.1 = **Marco Polo** (تركيب مختلف) | فيديو `aRQwTkUjf_c` |
| **Headway Plus** (طبعة الشرق الأوسط) | نفس أهداف اللغة — تُدرَّس بالجامعات العراقية | فيديوهات `97CT2BYa5lE` · `pDb6B8q-bOY` |
| الخامسة | تنظيم مختلف تماماً (Language focus / Vocabulary / Pronunciation) | studifor / sciarium |

> **قاعدة:** أي مصدر يقول **Tashi / Lonely Planet** = يطابق كتابنا. أي مصدر يركّز على **Marco Polo كنصّ شريط 2.1** = طبعة رابعة.

---

## 6. الخلاصة والخطة المقترحة

### الحكم
> **ماكو حاجة لأي مصدر خارجي.** 🥇 **كتاب المعلّم الرسمي** عندنا محلياً، محوّل لنصّ، ويغطي **كل** تمرين بحلّه + النصوص المسموعة. والتحقق الثانوي متاح من **يوتيوب** (3 محاضرات مطابقة) و**موقع Oxford الرسمي**.

### الخطة المقترحة للمرحلة القادمة
1. **فهرسة تمارين اليونت** من `Upper Intermediate - Unit 2 - Been There Done That.pdf` (10 ص) — كل تمرين برقم صفحته.
2. **ربط كل تمرين بحلّه** من `NH_UI_TeacherBook_Unit2_OCR.md` (نصّ جاهز).
3. **تحقق ثانوي** من يوتيوب (`UNIT5Nj0Mik` + `97CT2BYa5lE`) لأي تمرين غامض.
4. **بناء ملزمة الحلول** بنفس نمط Q Skills (`Unit_02_..._Solutions.md`).
5. **بناء منصّة الشرائح العريضة** بنفس دليل `WIDE_SLIDES_PLAYBOOK.md` — بس انتبه: **هذا الكتاب سكان بصفر نص**، فالـOCR لِزامي، والأجوبة تُقرأ بصرياً من الكتاب.

### ✅ المحجوزات (جاهزة)
| الملف | الحالة |
|:--|:--|
| `02_Raw_Materials/NH_UI_TeacherBook_Unit2_OCR.md` | **45,889 حرف** — مفتاح رسمي + tapescripts · **محجوب عن git** ✅ |
| `%TEMP%\nhsubs\*.vtt` | ترجمات 5 فيديوهات (en + ar) |
| `%TEMP%\nh\*.png` | صور الصفحات + خريطة تذييل كتاب المعلّم |

---

*استكشاف فقط — ما كُتب أي حل بعد. تاريخ: 2026-10-10.*

---

## 7. البحث العميق الإضافي (توسيع دائرة المصادر)

> **السياق:** بعد إكمال التقرير الأوّلي، طُلب البحث بكل الطرق العميقة — Wayback Machine، LibGen، مرايا جامعية، يوتيوب إضافي، Baidu Netdisk، Telegram، Reddit، متصفّح حقيقي (CDP) لمواقع محجوبة.

### ما نُفّذ فعلاً

| الطريقة | النتيجة |
|:--|:--|
| **Wayback Machine** (`archive.org`) | ✅ **6 volumes** (314 MB) بس **"Access-restricted-item: true"** + "printdisabled". PDF محمي (encrypted) — 172 بايت فقط عند التحميل. **غير متاح.** |
| **LibGen / ZLibrary** | لا توجد نتائج لـ Upper-Intermediate 3rd edition Workbook or Audio. |
| **مرايا جامعية** | Kansas U (CLC) ← redirect إلى `librarycentral.org.uk` (صفحة وهمية). YNFE (الصين) ← 502 Bad Gateway. SASFIN ← 502. |
| **Zhihu (知乎) + Baidu Netdisk** | مقال يدّعي توفير **الطبعة الرابعة كاملة** (Student's Book + Teacher's Book + Workbook + Class MP3 + software). الرابط (`acadsocclub.com`) ← **موقع تسويقي** (لا ملفات). روابط Baidu Netdisk موجودة لكنها تتطلّب **حساب صيني + تطبيق Baidu**. |
| **sciarium بالمتصفّح الحقيقي (CDP)** | **CAPTCHA-blocked** — اكتشف الـVPN (IP `169.224.117.148`). لا يمكن تجاوزه آلياً. |
| **Phuket Language School** | فقط **Intermediate** (ليس Upper-Intermediate) + **الطبعة الرابعة**. لا يناسبنا. |
| **Oxford ELT download / Teacher's Site** | **403 Forbidden** — يحتاج تسجيل دخول (account) أو ربما IP محظور. |
| **audio-digital.net** | موقع وهمي/تسويقي — لا ملفات حقيقية. |
| **YouTube إضافي** | لا فيديوهات جديدة تغطي Unit 2 بالذات. |

### ⚠️ خلاصة البحث العميق

**لم يُعثر على أي مصدر خارجي إضافي يتجاوز ما لدينا محلياً.** كل البوابات إما:
- محجوبة (CAPTCHA / 403 / 502)
- محدودة الوصول (Archive.org printdisabled)
- وهمية (LibraryCentral / audio-digital / acadsocclub)
- تتطلّب حسابات أو تطبيقات إقليمية (Baidu Netdisk)

### 💡 ما يزال ممكناً (إذا أردت)

| الخيار | الجهد | التوقع |
|:--|:--|:--|
| **Baidu Netdisk** | تحميل تطبيق Baidu + تسجيل حساب + إدخال رابط المشاركة | قد يعطي Workbook + Class Audio للطبعة الرابعة (للثالثة غير مضمون) |
| **sciarium يدوياً** | فتح الموقع من جهازك الخاص (بدون VPN) + حل CAPTCHA + تحميل Audio CD | ممكن — الموقع يملك Class Audio CDs |
| **Oxford Teacher's Site** | تسجيل حساب معلّم (أو استخدام حساب جامعي إن وُجد) | Workbook + Tests + Worksheets + Audio streaming |
| **Archive.org (borrow)** | تسجيل حساب + "Borrow" ككتاب إلكتروني | قد يعطي access مؤقت للـPDF المشفر |

> **الحكم:** بالنسبة لـ **Unit 2**، **ماكو حاجة** لأي من هذه الخطوات — كتاب المعلّم يكفي. بس إذا أردت **Workbook** أو **Audio** لاحقاً (للتدريب الإضافي)، Baidu Netdisk أو sciarium يدوياً هما الأرجح.

---

## 8. اكتشافات البحث العميق الإضافي (الموثّقة)

### ما لُقِيَ بعد

| المصدر | الحالة | التفاصيل |
|:--|:--|:--|
| **Rutracker (روسي)** | ✅ **Magnet Link متاح** | `magnet:?xt=urn:btih:B988DE9CAC8774A23A7C14A5B3DAC9C98DD48221` — **5.96 GB** pack يحتوي على **كل الطبعة الثالثة**: `3rd_Edition_UpperIntermediate_StudentsBook_Audio.rar` + `Workbook_Audio.rar` + `StudentsBook_pdf.rar` + `Workbook_pdf.rar` + `TeachersBook_pdf.rar`. يتطلّب **Torrent client** (μTorrent / qBittorrent) للتحميل. |
| **NUBIP (جامعة أوكرانية)** | ✅ **Workbook PDF** | `nubip.edu.ua/sites/default/files/u137/2_new_headway_-_upper-intermediate_workbook_1.pdf` — **17.3 MB**، **Workbook with key** (غلاف أرجواني، Soars + Wheeldon). **سكان** (لا نصّ). |
| **Google Drive** | ✅ **Workbook PDF** | `drive.google.com/file/d/0B0UMT7qwz-RySGJIaVlhNUw0SG8` — نفس الـWorkbook (17.3 MB). |
| **forum.majidonline.com** | ⚠️ **روابط Rapidshare قديمة** | نفس الملفات (pack كامل) بس روابط Rapidshare من 2007 — غالباً ميتة. |
| **archive.org (نسخة ثانية)** | ❌ **محدودة** | `newheadwayupperi0000soar` — 276 MB، <3> books + <4> audio discs، بس **printdisabled + encrypted**. |
| **YouTube Audio** | ⚠️ **الطبعة الخامسة فقط** | `q61_YfSc2Bs` (CD1 · 65 د) · `889jHmpqWa0` (CD4 · 71 د) — **الطبعة الخامسة**، مو الثالثة. لا يوجد Audio للطبعة الثالثة على YouTube. |

### ملخص الموارد المكتسبة بالبحث العميق

| الملف | المصدر | الحجم | الحالة |
|:--|:--|:--|:--|
| `nubip_workbook.pdf` | NUBIP + Google Drive | 17.3 MB | ✅ **Workbook with key** (سكان) |
| `Headway English Course – 3 издания` | Rutracker Magnet | 5.96 GB | ✅ **كل شيء** (PDF + Audio) — يحتاج Torrent |

### إذا أردت الـAudio

**الخيار الأفضل:** Magnet Link من Rutracker — يحتوي على:
- `3rd_Edition_UpperIntermediate_StudentsBook_Audio.rar`
- `3rd_Edition_UpperIntermediate_Workbook_Audio.rar`

**التعليمات:** انسخ الـMagnet Link إلى **qBittorrent** أو **μTorrent** وانتظر التحميل. الـpack كبير (5.96 GB) لأنه يحتوي على **كل المستويات** (Beginner إلى Advanced) + كل الإصدارات الثلاثة.

---

## Retrieval set — قائمة تحقق قبل ما تبدأ البناء

> جاوب بلا ما ترجع للتقرير. اللي تنساه ← ارجع للقسم المذكور.

1. **شنو المصدر الأساسي لحلول Unit 2؟** ووين موجود؟ (§1)
2. **شنو الحقيقة التقنية عن كل ملفات New Headway عندنا؟** وشنو يترتّب عليها؟ (§1)
3. **أي صفحات بكتاب المعلّم تغطي Unit 2؟** وشلون عرفناها؟ (§1)
4. **شنو الملف المحفوظ اللي فيه المفتاح؟** ووين؟ ومحمي من git؟ (§1)
5. **شنو يعطي موقع Oxford الرسمي؟** وشنو تحذيره؟ (§2)
6. **أي فيديو يوتيوب هو الأقرب لكتابنا؟** وليش؟ (§3)
7. **شنو العلامة اللي تميّز كتابنا عن الطبعة الرابعة؟** (§5)
8. **ليش لازم نتأكد من الطبعة قبل الاعتماد على أي فيديو؟** (§3، §5)
9. **أي مصادر نرفضها ولا نضيّع وقتنا فيها؟** وليش؟ (§4)
10. **شنو الخطوات الخمس المقترحة للمرحلة القادمة؟** (§6)
11. **شنو نتيجة البحث العميق الإضافي؟** هل لقينا مصدر جديد يتجاوز المحلي؟ (§7)
12. **إذا أردت Audio أو Workbook إضافي، شنو الخيار الأرجح؟** (§7)
13. **شنو اكتشاف Rutracker؟** وشنو يحتوي الـMagnet Link؟ (§8)
14. **Workbook with key وين لقيناه؟** وشنو حجمه؟ (§8)