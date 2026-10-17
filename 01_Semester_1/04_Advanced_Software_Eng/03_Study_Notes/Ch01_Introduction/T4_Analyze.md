---
title: ASE Chapter 1 — T4 · Analyze (Documented Failures)
course: Advanced Software Engineering
subtitle: Failure-case analysis grounded in Aggarwal — answers in English, traps and notes in Arabic
---

# T4 · Analyze (Documented Failures)
## Chapter 1 — Introduction

> **كيف تستخدم الملف.** اقرأ السؤال، حلّل بنفسك، بعدين افتح البطاقة. **الجواب بالإنجليزي** — هذا اللي تترجمه بالورقة. **البطاقات الصفراء والحمراء بالعربي** — فخاخ وتنبيهات.

**المصدر.** Aggarwal & Singh, *Software Engineering*, 3rd ed. (الطبعة الثالثة) — السكان `AliFahim_Software_Engineering.pdf`. **قائمة حالات الفشل = §1.1.1، ص.2** · **No Silver Bullet = §1.1.2، ص.3** · **أسباب الأزمة = §1.4، ص.12**. الشرائح الرسمية `Aggarwal_Singh_Slides/chapter_1_introduction.pdf` تُسمّى **كشرائح** عند الحاجة. أغروال هو المصدر الأساسي؛ أي مصدر ثاني يُسمّى صراحةً.

> [!CONCEPT] طريقة قراءة الإجابات
> الكلام العريض مبني على المصدر، وقد يُبسّط بألفاظ أسهل. الكلام العادي صياغة أو استنتاج مختصر. الاقتباس الحرفي فقط يوضع بين علامتي تنصيص.

---

## Retrieval set — T4 Analyze (documented failures)

**A.1 · The chapter lists documented software failures. Name them, and state in one line what went wrong in each.**
{: .keep-next }

> [!NOTE] Answer
> **Y2K** — **the four-digit year was shortened to a two-digit format.** · **Patriot missile (Dhahran)** — **a small timing error in the system's clock accumulated.** · **a 1996 consumer database project was delivered on time but failed to work as promised; the design team was over-optimistic in agreeing to requirements, while developers became fixated on rebuilding and errors were ignored.** · **Ariane-5** — **a 64-bit value converted to a 16-bit format caused an overflow.** · **financial software** — **faults produced wrong information or crashed the system.** · **Windows XP** — **18 megabytes of patches were posted on the release day itself.**
>
> **Aggarwal, §1.1.1, pp.2–3.**

---

**A.2 · Why did Y2K become a problem, how was the problem described, and what did handling it cost?**
{: .keep-next }

> [!NOTE] Answer
> **Y2K** arose because only the **last two digits of the year** were used — the four-digit date was shortened to a two-digit form. The problem was described as **"practically non-existent"**, and handling it cost **"millions of rupees"**.
>
> **Aggarwal, §1.1.1, p.2.**

---

**A.3 · Analyse the Patriot missile failure: what was the root-cause mechanism, and why did long uptime matter?**
{: .keep-next }

> [!NOTE] Answer
> The Patriot missiles **failed several times to hit Scud missiles**, including one that **killed 28 US soldiers in Dhahran, Saudi Arabia**. Root cause: **a small timing error in the system's clock accumulated until, after 14 hours, the tracking system was no longer accurate.** In the Dhahran attack the battery **had been operating for more than 100 hours**, so the small error had time to grow.
>
> **Aggarwal, §1.1.1, p.2.**
> [!TRAP] لا تضف أرقام البتات
> الكتاب يذكر **خطأ توقيت صغير يتراكم** و14 ساعة و100 ساعة فقط. تفاصيل 24-bit و0.1s و0.3433s مو موجودة عند أغروال؛ لا تنسبها إليه. ربط حجم الخطأ بتمثيله بالبتات يحتاج مصدراً إضافياً.

---

**A.4 · Analyse the Ariane-5 failure: what went wrong, and why did the backup unit not save the mission?**
{: .keep-next }

> [!NOTE] Answer
> Ariane-5 **was destroyed 39 seconds after launch, with its four-satellite payload.** Root cause: the guidance computer converted the rocket's **sideways velocity from a 64-bit to a 16-bit format**; **the number was too big and an overflow occurred after 36.7 seconds.** The identical backup unit **had failed the same way a few milliseconds earlier**, so redundancy gave no protection — the designers had assumed **the value would never be large enough to cause trouble.**
>
> **Aggarwal, §1.1.1, pp.2–3.**

---

**A.5 · Analyse the Space Shuttle fuel-dump crash. Why did it happen, and what did the follow-up find?**
{: .keep-next }

> [!NOTE] Answer
> During an abort the Shuttle dumps fuel to lighten the craft. The fuel-management module **finished the first dump and exited**, then **restarted for the second dump — where the crash occurred.** A **simple fix solved it**, but applying a general method to that module and others **surfaced seventeen additional, previously unknown problems.**
>
> **Aggarwal companion slides, slides 14–15.**
> [!TRAP] سند الحالة = شرائح، مو صفحة كتاب
> هذي الحالة **مو بالسرد النثري للكتاب**. قائمة أغروال (§1.1.1، ص.2) هي: Y2K · Patriot · قاعدة بيانات 1996 · Ariane-5 · برمجيات مالية · Windows XP. الرحلة الشاتل جاية من **شرائح المؤلف الرسمية** (سلايد 14–15) — فاذكرها **كسلايد**، ولا تنسبها لصفحة كتاب.

---

**A.6 · Why is there "no silver bullet"? Analyse why CASE tools did not end the crisis.**
{: .keep-next }

> [!NOTE] Answer
> There is **no single development — in technology or in management — that by itself promises even one order-of-magnitude improvement in productivity, reliability or simplicity.** CASE tools were tried and **companies spent large sums with highly unsatisfactory results**; the reason is that **the hard part is specifying, designing and testing the conceptual construct, not the labour of representing it.**
>
> **Aggarwal, §1.1.2, p.3.**

---

**A.7 · What common pattern do these failures share, and why do they matter to the discipline?**
{: .keep-next }

> [!NOTE] Answer
> These cases illustrate the software crisis and its effects, including failures that caused **the death of many human beings** and made the crisis **a fixture of everyday life.** **Software myths, poor quality, increasing cost, and delays in delivery** were driving forces behind the emergence of software engineering.
>
> **Aggarwal, §1.1, pp.1–2; §1.4, p.12.**
> القاسم المشترك بين هذه الحالات — مشكلات برمجية تؤدي إلى فشل أو كلفة أو تأخير — قراءة تحليلية للمجموعة.

---

## Rapid self-test — recall prompts (no answers shown)

1. Name the six documented failures in the book's list and give the cause of any three.
2. What handling cost is reported for Y2K?
3. State the Patriot mechanism in one line (and the two uptime figures).
4. Why did Ariane-5's redundant unit fail to save the rocket?
5. Why did CASE tools fail to end the software crisis?
