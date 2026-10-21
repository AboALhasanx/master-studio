# برومبتات Gemini — كتابة بنوك أسئلة MCSQuiz

> انسخ أحد البرومبتات، وبدّل ما بين الأقواس `(...)`. البروتوكول الملزم: `00_STUDIO_HUB/guides/QUIZ_BANK_PROTOCOL.md`، والهاندوف الكامل: `00_STUDIO_HUB/handoffs/GEMINI_QUIZ_HANDOFF.md`.

## كيف تملأ الأقواس

| الحقل | مثال | من وين تجيبه |
|---|---|---|
| `subject_id` | `01_Cyber_Security` | اسم مجلد المادة داخل `01_Semester_1` |
| `الجابتر` | `3` | رقم الفصل في الكتاب (مو ترقيم تسلسلي) |
| `النموذج` | `أ` أو `ب` | الجابتر له نموذجان فقط |
| `quiz_id` | `Quiz_Ch03_ModelA_Cybersecurity_Foundations` | `Quiz_Ch<رقم الجابتر>_Model<أ/ب>_<اسم مختصر>` |
| `عدد الأسئلة` | `5` | 5 كحد أدنى، و10–15 إذا المادة غنية |
| `المصدر` | `01_Semester_1/01_Cyber_Security/03_Study_Notes/W03_Chapter3_TriLayer.md` | ملف ملاحظات المادة |
| `الدكتور` | — | انسخه من أي بنك موجود بنفس مجلد `07_Quizzes_&_Anki` |

---

## 1) برومبت بنك واحد

```
اقرأ أولاً (بالترتيب):
1) 00_STUDIO_HUB/handoffs/GEMINI_QUIZ_HANDOFF.md
2) 00_STUDIO_HUB/guides/QUIZ_BANK_PROTOCOL.md
3) 00_STUDIO_HUB/templates/template-quiz-bank.json
4) المصدر: (مسار ملف الملاحظات)

المهمة — بنك أسئلة واحد:
- subject_id: (01_Cyber_Security)
- الجابتر: (3)
- النموذج: (أ)
- عدد الأسئلة: (5)
- quiz_id: (Quiz_Ch03_ModelA_Cybersecurity_Foundations)
- مسار الحفظ: 01_Semester_1/(01_Cyber_Security)/07_Quizzes_&_Anki/(Quiz_Ch03_ModelA_Cybersecurity_Foundations).json
- الدكتور: انسخه من أي بنك موجود بنفس المجلد
- العنوان العربي: (عنوان الجابتر من المصدر) — النموذج أ

الشروط: عربي أولاً + إنجليزي، فصحى، المصطلحات التقنية بالإنجليزية بدون أقواس، سهم ← في السطر العربي،
4 خيارات متقاربة الطول (±25%)، الإجابة الصحيحة مو الأطول، توزيع مفتاح الإجابة (2/1/1/1 للخمسة أسئلة)،
ولا تخترع أي معلومة مو موجودة في المصدر، ولا تلمس أي ملف ثاني.

بعد الكتابة: شغّل فحوصات البوابة (إذا عندك صلاحية ملفات) واطبع نتيجتها كاملة،
أو اطبع الـJSON كاملاً ببلوك كود واحد + ملخص (المفاهيم، توزيع المفاتيح، نسبة طول الخيار الصحيح).
```

---

## 2) برومبت النموذجين لجابتر واحد (أ + ب)

```
اقرأ أولاً: 00_STUDIO_HUB/handoffs/GEMINI_QUIZ_HANDOFF.md ثم 00_STUDIO_HUB/guides/QUIZ_BANK_PROTOCOL.md
ثم المصدر: (مسار ملف الملاحظات)

المهمة — نموذجان لنفس الجابتر:
- subject_id: (03_Data_Mining)
- الجابتر: (2)
- المصدر: (01_Semester_1/03_Data_Mining/03_Study_Notes/Week_02_Data_Types_and_Preparation.md)
- الدكتور: انسخه من بنك موجود بنفس المجلد

النموذج أ: (5) أسئلة → quiz_id: (Quiz_Ch02_ModelA_Data_Types_and_Preparation)
النموذج ب: (5) أسئلة → quiz_id: (Quiz_Ch02_ModelB_Data_Types_and_Preparation)

شرط مهم: ما يتكرر أي مفهوم بين النموذجين (10 مفاهيم مختلفة بـ concept_id)،
والنموذج أ يغطي النصف الأول من الجابتر والنموذج ب النصف الثاني.
كل الباقي حسب البروتوكول، واطبع ناتج الفحوصات (أو الـJSON ببلوكين).
```

---

## 3) برومبت دفعة كاملة (عدة جابترات)

```
اقرأ: 00_STUDIO_HUB/handoffs/GEMINI_QUIZ_HANDOFF.md و 00_STUDIO_HUB/guides/QUIZ_BANK_PROTOCOL.md

اكتب البنوك التالية، كل واحد بملف مستقل حسب التسمية Quiz_Ch<NN>_Model<A|B>_<Slug>.json
داخل 01_Semester_1/<subject_id>/07_Quizzes_&_Anki/ :

| subject_id | الجابتر | النموذج | عدد الأسئلة | المصدر | quiz_id |
|---|---|---|---|---|---|
| (01_Cyber_Security) | (1) | (ب) | (5) | (W01_Chapter1_TriLayer.md) | (Quiz_Ch01_ModelB_Cybersecurity_Foundations) |
| (01_Cyber_Security) | (2) | (ب) | (5) | (W02_Chapter2_TriLayer.md) | (Quiz_Ch02_ModelB_Risk_Management) |
| (03_Data_Mining)   | (2) | (أ) | (5) | (Week_02_Data_Types_and_Preparation.md) | (Quiz_Ch02_ModelA_Data_Types) |

القواعد نفسها لكل بنك (عربي أولاً، توزيع المفاتيح، طول الخيارات، عدم التكرار بين النموذجين، ولا اختراع).
سلّم النتائج بنفس ترتيب الجدول، مع ناتج الفحوصات لكل ملف.
```

---

## 4) لو Gemini بدون صلاحية ملفات (محادثة فقط)

أضف هذا السطر في نهاية أي برومبت:

```
ما عندك صلاحية ملفات: اطبع لكل بنك الـJSON كاملاً ببلوك كود واحد (بدون تعليقات ولا نقاط حذف)،
وبعده مباشرة: subject_id | الجابتر | النموذج | quiz_id | عدد الأسئلة | المفاهيم | توزيع المفاتيح | المصدر المستخدم.
```

---

## 5) بعد ما يسلّم Gemini

سلّم الملفات (أو الـJSON) لإيجنت داخل المخزن (OpenCode/Codex/WorkBuddy) وهو يسوي:

```bash
cd C:\Users\gokoq\Master-Studio
python "90_Shared_Toolbox/tools/quiz_balancer.py" "<الملف>"                 # توزين مفتاح الإجابة
python "90_Shared_Toolbox/tools/quiz_balancer.py" "<الملف>" --check --strict # البوابة (لازم exit 0)
python "90_Shared_Toolbox/tools/portal_content.py" sync                      # النشر للبوابة
python "90_Shared_Toolbox/tools/portal_content.py" pull                      # تحديث النسخة المرفقة + قائمة الـSW
```

ثم يتحقق داخل التطبيق: بطاقتان لكل جابتر، «النموذج أ» قبل «ب»، ومفتاح ع/EN يترجم السؤال.
