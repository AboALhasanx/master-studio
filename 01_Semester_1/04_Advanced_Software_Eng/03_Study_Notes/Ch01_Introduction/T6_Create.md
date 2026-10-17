---
title: ASE Chapter 1 — T6 · Create (Diagram)
course: Advanced Software Engineering
subtitle: The software non-wear-out curve against the hardware bath-tub curve — answers in English, notes in Arabic
---

# T6 · Create (Diagram)
## Chapter 1 — Introduction

> **كيف تستخدم الملف.** المطلوب هنا **رسم**، مو سرد. ارسم المحورين والمراحل، بعدين قارن برسمة الكتاب. **الجواب بالإنجليزي** — هذا اللي تترجمه بالورقة.

**المصدر.** Aggarwal & Singh, *Software Engineering*, 3rd ed. (الطبعة الثالثة) — السكان `AliFahim_Software_Engineering.pdf`. الشكلان = **Fig. 1.5، ص.8** و**Fig. 1.6، ص.9**.

> [!CONCEPT] طريقة قراءة الإجابات
> الكلام العريض مبني على المصدر، وقد يُبسّط بألفاظ أسهل. الكلام العادي صياغة أو استنتاج مختصر. الاقتباس الحرفي فقط يوضع بين علامتي تنصيص.

---

## Retrieval set — T6 Create

**D.1 · Draw the software failure-intensity curve against the hardware bath-tub curve, labelling the axes and the phases.**
{: .keep-next }

> [!NOTE] Answer
> **Axes:** failure intensity (vertical) against time (horizontal). The hardware curve (Fig. 1.5) has three phases: high intensity during **burn-in**, a low flat **useful-life** plateau, then a **rising** limb at **wear out**. The software curve (Fig. 1.6) has **only the descending curve**: defects are found and fixed, so intensity keeps falling and the rising limb never arrives.
>
> ![Failure intensity against time — hardware bath-tub (Fig. 1.5) vs software (Fig. 1.6)](_diagrams/d1_wearout.png)
>
> **Aggarwal, §1.2.4, pp.8–9; Fig. 1.5 p.8, Fig. 1.6 p.9.**

---

**D.2 · Interpret the drawing: why does the software curve never rise again?**
{: .keep-next }

> [!NOTE] Answer
> **Software does not wear out and has no wear-out phase.** It **becomes obsolete when the environment it was developed for changes.**
>
> **Aggarwal, §1.2.4, pp.8–10.**
> [!TRAP] تفسير الرسم
> ربط شكل المنحنى بغياب مرحلة الاهتراء قراءة تحليلية؛ البرمجيات لا تهترئ، لكنها قد تتقادم عند تغيّر البيئة.

---

## Rapid self-test — recall prompts (no answers shown)

1. Name the three phases of the hardware curve.
2. What shape does the software curve take, and why?
3. What happens to software instead of wearing out?
