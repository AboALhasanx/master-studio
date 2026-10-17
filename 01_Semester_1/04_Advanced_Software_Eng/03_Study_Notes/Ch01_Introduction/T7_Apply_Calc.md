---
title: ASE Chapter 1 — T7 · Apply / Calculate
course: Advanced Software Engineering
subtitle: Productivity and effort — the chapter's only applied relationship — answers in English, notes in Arabic
---

# T7 · Apply / Calculate
## Chapter 1 — Introduction

> **كيف تستخدم الملف.** هذا الفصل **بلا محور حسابي**؛ البند التطبيقي الوحيد هو علاقة الإنتاجية بالجهد. **الجواب بالإنجليزي** — هذا اللي تترجمه بالورقة.

**المصدر.** Aggarwal & Singh, *Software Engineering*, 3rd ed. (الطبعة الثالثة) — السكان `AliFahim_Software_Engineering.pdf`. §1.5.5، ص.14.

> [!WARN] ملاحظة الفصل — بلا محور حسابي
> This chapter contains no computational spine. The only applied relationship is **productivity = output / effort**, with effort measured in **person-months**. ما نخترع مسائل بلا سند؛ الأرقام الإضافية أمثلة تدريبية من عندنا.

> [!CONCEPT] طريقة قراءة الإجابات
> الكلام العريض مبني على المصدر، وقد يُبسّط بألفاظ أسهل. الكلام العادي صياغة أو استنتاج مختصر. الاقتباس الحرفي فقط يوضع بين علامتي تنصيص.

---

## Retrieval set — T7 Apply / Calculate

**C.1 · Define productivity and state the appropriate unit of effort.**
{: .keep-next }

> [!NOTE] Answer
> **Productivity** is **"the rate of output, or production per unit of effort, i.e., the output achieved with regard to the time taken but irrespective of the cost incurred."** Output is measured in **lines of code (LOC)**. The appropriate unit of effort is **"Person Months (PMs), meaning thereby number of persons involved for specified months."**
>
> **Aggarwal, §1.5.5, p.14.**

---

**C.2 · Apply: a project delivers 30,000 LOC at an effort of 15 person-months. Compute the productivity.**
{: .keep-next }

> [!NOTE] Answer
> Productivity = output ÷ effort = **30,000 LOC ÷ 15 PM = 2,000 LOC/PM.**
>
> **Aggarwal, §1.5.5, p.14.**
> الأرقام (30,000 و15) مثال تدريبي لتطبيق المعادلة؛ أما المعادلة والوحدة فمن المصدر.

---

**C.3 · Why is productivity expressed as LOC/PM rather than as a raw number of lines?**
{: .keep-next }

> [!NOTE] Answer
> Because it is a **rate** — output per unit of effort — its unit must combine output and effort, hence **LOC/PM**. A raw line count ignores how much effort produced it.
>
> **Aggarwal, §1.5.5, p.14.**
> تفسير الوحدة بوصفها نسبة بين المخرَج والجهد هو توضيح مباشر للمعادلة؛ المصدر يحدد المخرَج والجهد ووحدة الجهد.

---

## Rapid self-test — recall prompts (no answers shown)

1. Define software productivity.
2. What is the appropriate unit of effort, and why person-months?
3. Compute LOC/PM for 48,000 LOC at 16 person-months.
