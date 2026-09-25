# Academic Paper Assignment — English Language (CS502)

> **⚠️ STATUS: ALTERNATIVE CANDIDATE — NOT SELECTED.** The selected paper for the English assignment is **`social_network_sensors_plos2010.md`** (Christakis & Fowler, PLOS ONE 2010). This note documents a *second verified option* prepared as a backup; build the explanation deliverable from the selected paper unless the student explicitly switches.

> (Verification-only record) — Topic: spatio-temporal event detection on Twitter via space-time scan statistics. 10 pages, DOI `10.1371/journal.pone.0097807`, PLoS ONE 9(6):e97807 (2014). Fits all constraints (CS field, DOI, ≤15 pp, free PDF, journal+volume). Kept as a备选 in case the student prefers it over the selected `social_network_sensors` paper.

---

## 1. The Chosen Paper (الورقة المختارة)

**Title:** Event Detection using Twitter: A Spatio-Temporal Approach
**Authors:** Tao Cheng, Thomas Wicks (SpaceTimeLab, University College London)
**Journal:** PLoS ONE
**Year:** 2014
**Volume / Issue / Article:** 9(6), e97807
**DOI:** `10.1371/journal.pone.0097807`  *(verified resolvable via Crossref)*
**Pages:** 10  *(verified via PyMuPDF — under the 15-page limit)*
**Open-access PDF:** https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0097807
**Local PDF (vault):** `02_Raw_Materials/event_detection_twitter_PLOS2014.pdf`

---

## 2. Why this paper (لماذا هذي الورقة)

| Constraint from your instruction | Status |
|---|---|
| مجال علوم الحاسوب (Computer Science field) | ✅ Data mining / spatio-temporal event detection on social media (geocomputation + statistical scanning) |
| منشور وله رقم ومجلة (Published, with journal + volume number) | ✅ PLoS ONE, Vol. 9, Issue 6 |
| موثّقة برقم DOI (Explicit, resolvable DOI) | ✅ `10.1371/journal.pone.0097807` — confirmed in Crossref + embedded in the PDF |
| صفحات قليلة ولا تتعدى 15 (Few pages, ≤ 15) | ✅ 10 pages |
| pdf مجاني (Free/open-access PDF) | ✅ PLoS ONE is fully open access |

**Correction note:** This replaces the earlier *scikit-learn (JMLR 2011)* pick, which had **no DOI** (violated your "موثقة" rule), and also replaces a mistaken PLOS ONE download that turned out to be a *biology/immunology* paper (wrong field). That wrong file was deleted from the vault.

---

## 3. What the paper is about (ملخص الورقة — from the abstract)

- **Problem:** ~400 million tweets are sent daily, a rich source for detecting and monitoring real-world news/disaster events. Existing approaches track *pre-chosen keywords* and watch how word usage changes over time — but you must already know the event to pick the words, and you can't be sure those words are the right ones.
- **Method (their contribution):** Use **space-time scan statistics (STSS)** to look for clusters of tweets across **both space and time**, *regardless of tweet content*. The idea: during a real event people tweet far more than expected, so an unusual spatio-temporal cluster spontaneously appears.
- **Case study:** The **2013 London helicopter crash**. The method found a spatio-temporally significant cluster tied to the crash — short-lived, but rich in keywords and photos — and also detected other special events.

---

## 4. Suggested explanation structure (هيكل الشرح المقترح)

When you present/explain this paper in English, follow this spine:

1. **Context** — social media as a real-time sensor for the physical world.
2. **Limitation of the baseline** — keyword/temporal methods need prior knowledge of the event.
3. **The proposed method** — space-time scan statistics: scan for spatio-temporal clusters, content-independent.
4. **Experiment / case study** — 2013 London helicopter crash; what the cluster revealed.
5. **Strengths & weaknesses** — detects unknown events, but clusters are short-lived; discuss limitations.
6. **Conclusion** — why a content-free, space+time scan is a useful complement to keyword methods.

---

## 5. Next step (الخطوة الجاية)

Build the full bilingual deliverable: a simplified Arabic/English **summary + key-contributions analysis + short spoken-presentation outline** of this paper, then export to PDF. Confirm with me before I generate the PDF (depth is your call).
