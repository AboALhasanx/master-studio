---
title: "Cyber Security — Week 03: Annotation Map (doctor's own marks)"
subject: "01_Cyber_Security"
week: 3
source_pdf: "C:\\Users\\gokoq\\Downloads\\Telegram Desktop\\W02_Risks.pdf"
pages: 14
captured: "2026-10-26 by Koko — red-stroke detection mapped to text, every page viewed"
---

# Week 03 — Annotation Map

> **Why this file exists.** The clean copy `02_Raw_Materials/W03_Risks.pdf` has **no annotations**
> (0 `/Annots`, 0 `/Highlight`, 0 `/Ink`) — verified, not assumed. The marked copy lives outside the
> vault at the path above: 555,669 bytes, 14 pages, marks **flattened into the page content**, so no
> PDF annotation objects exist either. The marks had to be found by rendering the pages and by
> detecting red strokes and mapping them to the words underneath
> (`scratch/w03_crossings.py`).
>
> **Rule:** 🟡 = required for the exam · ❌ = crossed out, **do not ask about it**.

---

## 1. The two marks

| Mark | Pages | Meaning |
|:--|:--|:--|
| 🟡 yellow highlight | 1, 3, 4, 5, 8, 9, 12, 14 | memorise / be able to explain |
| ❌ red strike-through | 4, 5, 6, 7, 8, 9, 11, 12, 13, 14 | **out of scope** |

Ten of the fourteen pages carry at least one strike-through. This is a much heavier cut than
Chapter 1, where only the case-study chapter was crossed.

---

## 2. ❌ Crossed out — delete from every bank

| Page | What is crossed |
|:--:|:---|
| **4** | the two bullets **Reduce likelihood** / **Reduce impact** |
| **4** | the whole **Governance Integration** block and its two bullets (corporate governance frameworks, enterprise risk management) |
| **5** | the **Cross-departmental policies** bullet and the sentence *"This shift requires executives, managers, and employees alike…"* |
| **5** | **the whole of section 3 — Balancing Cost of Controls vs. Potential Damage**, including the Firewall Dilemma, its `EFL = P · I` computation, and Over-Control vs. Under-Control |
| **6–7** | **the whole hospital quantification scenario** — Setting, baseline risk register, controls C1–C4, Portfolios A and B, the recommendation |
| **8** | **the whole of section 5 — Definition of Security Policies** (the definition paragraph) |
| **8** | the **Examples** list (Acceptable Use, Data Handling, Incident Response) and the sentence *"Thus, policies bridge strategic objectives…"* |
| **8** | **the whole of section 2 — Policy vs. Technology: Complementary Roles** |
| **9** | the **Technology without Policy** bullet and the socio-technical sentence |
| **11** | **the whole of section 2 — Core Functions of Enterprise Security Policies** (2.1 defining responsibilities, 2.2 aligning with business objectives, 2.3 legal and regulatory compliance) |
| **12** | the compliance block (GDPR / HIPAA / PCI-DSS policies) and **2.4 Reducing Insider Threats** |
| **13–14** | **the whole PCI mathematical framing** — the formula, the weighted computation, the heat banding, the 90-day plan, the what-if case and the executive takeaway |

**Consequence for the banks:** the hospital quantification bank has no surviving source at all and
must be retired. The cost-of-controls material and the policy-versus-technology material go with it.

---

## 3. 🟡 Highlighted — keep and test

| Page | What is highlighted |
|:--:|:---|
| **1** | *"cybersecurity cannot be isolated within the IT department"* · **Why?** · the four reason labels — **Pervasive Digitization**, **Ecosystem Dependence**, **Adversarial Nature**, **Legal/Regulatory Context** |
| **3** | *5. Future Challenges in Cyber Risk Management* |
| **4** | *Why It Is Not Only IT's Concern* and its four numbered items |
| **5** | *4. Industry-Specific Cyber Risks* · *4.1 Banking and Financial Services* |
| **8** | *Characteristics of Security Policies* (high-level guidance · alignment with risk · organization-wide · living document) |
| **9** | *3. Challenges in Policy Creation and Enforcement* (3.1 user resistance · 3.2 lack of enforcement · 3.3 outdated policies · 3.4 cultural barriers) |
| **9** | *6. Policy Lifecycle* — Draft → Approval → Communication → Enforcement |
| **12** | *3. Modern Trends in Enterprise Security Policies* · *3.1 Zero Trust ("Never Trust, Always Verify")* · *3.2 AI-Driven Compliance Auditing* · *3.3 Integration with Corporate Governance and ESG* |
| **14** | *Strategic Value of Policies in Enterprise Security* |

---

## 4. What survives, in one list

1. Cybersecurity as an organizational risk, and the **four reasons** why.
2. The **three dimensions** — financial, operational, reputational — with `EFL = Σ P_i · I_i`.
3. The **risk equation** and its aggregate form (section 6, not crossed).
4. **Future challenges** in cyber risk management.
5. **Why it is not only IT's concern** — the four enterprise-wide items.
6. **Industry-specific** risks (banking, healthcare, and the rest).
7. **Characteristics** of a security policy.
8. **Challenges** in creating and enforcing policy, and the **lifecycle**.
9. **Modern trends** — Zero Trust, AI-driven compliance auditing, ESG.
10. **Strategic value** of policies.

Everything else on the fourteen pages is crossed.

---

## 5. Honest note on the equations

The chapter carries four invented equations (`EFL`, `Risk = T × V × I`, `PE`, `PCI`). The source note
says plainly they are **AI-generated, not from Sharp's book**, but that the doctor teaches them as
given. Her own marks then **cross out the PCI worked example entirely** (pp. 13–14) and cross out the
`EFL = P · I` computation inside the firewall dilemma (p. 5) — while leaving the `EFL` framing on p. 1
uncrossed. So: `EFL` survives as a definition, the arithmetic that demonstrates it does not, and
`PCI` has no surviving application. Do not build compute questions on the crossed ones.
