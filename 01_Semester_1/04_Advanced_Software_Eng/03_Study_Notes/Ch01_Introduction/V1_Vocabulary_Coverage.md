---
title: ASE Chapter 1 — V1 · Lecture-1 Vocabulary Coverage
course: Advanced Software Engineering
subtitle: The instructor's Lecture-1 terms mapped to their coverage — English terms, brief Arabic notes
---

# V1 · Lecture-1 Vocabulary Coverage
## Chapter 1 — Introduction

> **كيف تستخدم الملف.** هذا خريطة تغطية لمفردات المحاضرة الأولى (قائمة الدكتور، 16/9). لكل مصطلح: **وين مغطّى** (ملف · قسم · صفحة) + سطر عربي قصير. المصدر الأساسي أغروال؛ الفجوتان تُملآن بمصدر مساند **مسمّى**.

**المصدر.** Aggarwal & Singh, *Software Engineering*, 3rd ed. (الطبعة الثالثة) — السكان `AliFahim_Software_Engineering.pdf`. الفجوتان: **Sommerville, *Software Engineering*, 9th ed.** (مصدر مساند مسمّى — يُذكر لأنه نقطة ناقصة عند أغروال Ch1).

## Retrieval set — Lecture-1 term coverage

**1. Evolving role of software.** Covered — `T2 1.9` · **§1.1، ص.1.** (تغيّر دور البرمجيات وأثرها في كل جانب من الحياة.)

**2. Changing nature of software.** Covered — `T2 1.15` · **§1.3، ص.10–11; Fig. 1.7.** (البرمجيات صارت جزءاً من معظم مجالات الحياة، وصُنّفت **ثمانية** مجالات للتطبيق.)

**3. What software is: code + data + documentation.** Covered — `T2 1.7, 1.14` · **§1.2.2، ص.4–5.** تنبيه: صياغة الكتاب هي **programs + documentation + operating procedures**؛ كلمة «data» مو لفظه.

**4. Definition of software engineering.** Covered — `T2 1.8, 1.10` · **§1.2.1، ص.4.** (تعريفا Fritz Bauer [FRIT68] وStephen Schach [SCHA90].)

**5. The software process.** Covered — `T2 1.11; T3 U.4` · **§1.2.3، ص.6–7.**

**6. The software crisis.** Covered — `T2 1.1, 1.2, 1.4, 1.5` · **§1.1، ص.1; §1.4، ص.12.** (خمسة عوامل مساهمة + جملة «driving forces behind the emergence of software engineering».)

**7. The software crisis: IBM figures.** Covered — **§1.1، ص.1** مباشرة: **"31% of the projects get cancelled before they are completed, 53% over-run their cost estimates by an average of 189% and for every 100 projects, there are 94 restarts" [IBMG2K].** المصدر المطبوع: تقرير IBM المقتبس بكتاب أغروال.
> [!TRAP] لا أرقام OS/360
> أرقام IBM هنا **مقتبسة بنص الكتاب ص.1 وموثّقة**. أما أرقام **IBM OS/360** (مثل man-years أو كلفة النظام) فما موجودة بمادة Ch1، و**ممنوع تثبيتها** قبل توثيقها من مصدر. إذا احتجتها، انسبها لمصدرها بالاسم والصفحة.

**8. Software myths (management, customer, developer).** Covered — `T2 1.6; T3 U.3` · **§1.4، ص.11–12** (يذكر **تسع** خرافات). تجميع الشرائح حسب المنظور (management / customer / developer) موجود بشرائح المؤلف (36–46).

**9. "No Silver Bullet".** Covered — `T4 A.6` · **§1.1.2، ص.3.** (لا تطوير منفرد يوعد بتحسّن رتبة كاملة.)

**10. Documented failures (Patriot missile).** Covered — `T4 A.1, A.3` · **§1.1.1، ص.2.** (القائمة الرسمية: Y2K · Patriot · قاعدة بيانات 1996 · Ariane-5 · برمجيات مالية · Windows XP. حالة الشاتل = **شرائح المؤلف الرسمية، سلايد 14–15** — تُذكر كسلايد.)

**11. Core terminology: error, fault, failure, defect.** **فجوة حقيقية** — غير معرّفة بـCh1 عند أغروال. **Sommerville، §11.2، ص.297، Fig. 11.3** يميّز الخطأ البشري، عيب النظام، حالة الخطأ، وفشل الخدمة. أما **Pressman، §8.4.1، ص.203** فيوضح أن `defect` و`fault` مترادفان في سياق عملية البرمجيات؛ لذلك `defect` مو مرحلة رابعة مستقلة.

**12. Professional ethics.** **فجوة حقيقية** — غير موجودة بالكتاب/الشرائح. المصدر المساند: **Sommerville، §1.2، ص.15–16** (المدونة المشتركة، ثمانية مبادئ، Fig. 1.3).

**13. ACM / IEEE (code of ethics).** نفس الفجوة — المصدر المساند: **Sommerville، §1.2، ص.15–16** (مدونة ACM/IEEE المشتركة).

---

> [!CONCEPT] خلاصة التغطية
> من 13 مدخلاً: **10 مغطّاة عند أغروال**؛ والمدخلات 11–13 تغطي **موضوعين مساندين**: مصطلحات الخطأ/العيب/الفشل، ومدونة الأخلاقيات.

### Supporting-source answers for the two lecture gaps

**11 · How are error, fault, system error, and failure related?**

> [!NOTE] Answer
> **A human error or mistake can introduce a system fault. When faulty code runs, it can create a system error, an incorrect system state. If the system then fails to provide the expected service, a system failure occurs. In software-process usage, defect and fault are synonyms, not two separate stages.**
>
> **Sommerville, §11.2, p.297, Fig. 11.3; Pressman, §8.4.1, p.203.**

**12–13 · What does professional software ethics require, and which code covers it?**

> [!NOTE] Answer
> **Software engineers have responsibilities beyond technical work and should act ethically and responsibly. The joint Software Engineering Code of Ethics and Professional Practice has eight principles: Public, Client and Employer, Product, Judgment, Management, Profession, Colleagues, and Self.**
>
> **Sommerville, §1.2, pp.15–16.**

## Rapid self-test — recall prompts (no answers shown)

1. Which two topics are missing from Aggarwal Chapter 1, and which supporting sources cover them? How is `defect` related to `fault`?
2. Where exactly are the IBM figures printed, and what are the three numbers?
3. Which failure cases are in the book's own list, and which one comes only from the slides?
4. What components does the source include in software?
