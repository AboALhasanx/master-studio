# Chapter 7 — Source and Question Coverage Map

**Prepared:** 2026-10-21. This is a navigation record. OCR and PDF text extraction locate candidate material; final claims, formulas, diagrams, and printed-page citations still require inspection of their original page images.

## Course-primary sources

| Source | Identified range | Role and limits |
|---|---|---|
| K.K. Aggarwal & Yogesh Singh, *Software Engineering*, 3rd ed., scanned course copy `AliFahim_Software_Engineering.pdf` | Chapter 7 prose/exercises provisionally printed pp. 308–364; PDF spreads 160–188. Printed p.365 starts Chapter 8. | Primary prose, definitions, model explanations, figures, examples, and exercises. The scan's title page is absent; identity is inferred from its contents and the matching named companion deck. Spread 188 mixes p.364 Chapter 7 exercises with p.365 Chapter 8 material; use only the left-page content for Chapter 7. Check visible page numbers before citation. |
| K.K. Aggarwal & Yogesh Singh, Chapter 7 companion slides | 126 slides; slide groups below | Official course companion. It contains lecture emphasis, slide figures, 50 MCQs, and 35 exercises. Question prompts are slide-sourced; no publisher key was found. A second copy in `Aggarwal_Singh_Slides/chapter_7_software_reliability.pdf` has 126 pages and a page-normalized text hash identical to the `By_Chapter` deck; index the `By_Chapter` copy once. |
| Student-provided instructor list | 19 terms, recorded in `V7_Doctor_Vocabulary.md` | Scope authority for this build. The original instructor post is not attached, so provenance is the student's direct report. |

## Vocabulary-to-source map

| Required term | Companion slides | Provisional primary-book anchor | Question/figure clues |
|---|---:|---:|---|
| What is Software Reliability? | 6–8 | pp. 308–310 | Exercises 7.1, 7.6 |
| Software Reliability and Hardware Reliability | 2–5 | pp. 308–310 | Exercises 7.2–7.3; Figs. 7.1–7.2 |
| Failures and Faults | 8–15 | pp. 310–317 | Exercises 7.4–7.6; failure-occurrence forms and intensity |
| Environment | 16–20 | pp. 318–320 | Operational profile and input-space figures 7.4–7.6 |
| Uses of Reliability Studies | 21–23 | pp. 320–322 | Exercise 7.7; Fig. 7.7 |
| McCall Software Quality Model | 30–39 | pp. 321–324 | Exercises 7.10–7.11; Figs. 7.9–7.10 |
| Boehm Software Quality Model | 40 | pp. 324–326 | Exercise 7.12; Fig. 7.11 |
| ISO 9126 | 41–46 | pp. 326–328 | Exercises 7.13–7.14; Fig. 7.12 |
| Basic Execution Time Model | 47–58 | pp. 329–334 | Example 7.1; Exercises 7.15, 7.18, 7.24; Figs. 7.13–7.17 |
| Logarithmic Poisson Execution Time Model | 59–71 | pp. 335–339 | Examples 7.2–7.3; Exercises 7.16–7.21; Figs. 7.18–7.19 |
| Calendar Time Component | 72–88 | pp. 339–344 | Examples 7.4–7.6; Exercise 7.23; Figs. 7.20–7.21 |
| Jelinski–Moranda Model | 89–92 | pp. 345–346 | Example 7.7; Exercise 7.25; Fig. 7.22 |
| Bug Seeding Model | 93 | pp. 346–347 | Exercise 7.26; verify the source's model assumptions and spelling before using “Mills.” |
| CMM Maturity Levels | 94–96 | pp. 347–349 | Exercises 7.27–7.28; Figs. 7.23–7.24 |
| CMM Key Process Areas | 97–101 | pp. 350–352 | Exercises 7.28, 7.33 |
| CMM Common Features | 102 | pp. 353–354 | The chapter explains the common-feature structure; inspect the figure/list before making a memorization list. |
| Mapping ISO 9001 to the CMM | 103–106 | pp. 355–357 | Exercises 7.29–7.30 |
| Contrasting ISO 9001 and the CMM | 107 | pp. 355–357 | Exercises 7.31, 7.34–7.35 |
| Conclusion | 107 | pp. 356–357 | Exercise 7.31 asks for a comparison and preference; answer the requested judgement directly and preserve its historical context. |

The book page ranges above are preliminary OCR/navigation anchors, not final citations. The scan start (p.308) and end boundary (p.364 / next chapter begins p.365) have been checked visually. Slide anchors are page numbers in the 126-page companion PDF.

## Publisher question inventory

- **MCQ:** 50 numbered items, `7.1`–`7.50`, companion slides 108–119 and primary-book printed pp. 359–362.
- **Written exercises:** 35 numbered items, `7.1`–`7.35`, companion slides 120–126 and primary-book printed pp. 363–364.
- These are source-bank counts, not exam marks or probabilities. Some slides place MCQs out of numeric order, and the text layer can detach equation options, especially around 7.20–7.25. Preserve item IDs rather than visual order.
- **Verified source conflict:** slide 115 labels 7.34 as “process management,” duplicating 7.35. The book's p.361 wording is 7.34 “process control” and 7.35 “process management.” Use the book for 7.34 and note the companion-slide discrepancy.
- No answer key or solutions section was found in the inspected primary Chapter 7 pages or companion deck. MCQ answers need independent reasoning against the chapter; source counts do not establish exam probability.
- **Example 7.2 arithmetic note (scan p.337, visually checked):** the source prints μ(20)=109. Substitution in its displayed formula gives about 109.861. Preserve the source result only with a brief visible note about its integer truncation/rounding; otherwise show the computed value accurately. Do not present the two values as exactly equal.
- Tag every exercise exactly once by its primary response form. A comparison or numeric prompt may have a short cross-reference elsewhere, but should not be reprinted as a duplicate question.

## Supporting-source candidates in the vault

All below are distinct books from the course-primary K.K. Aggarwal & Singh scan. They are a gap-check pool, not a mandate to cite every title.

| Candidate | Searchable location observed | Best possible contribution | Use rule |
|---|---|---|---|
| B.B. Agarwal, S.P. Tayal & M. Gupta, *Software Engineering and Testing: An Introduction* (2010) | PDF pp. 100–129; book-page headers show pp. 87–116, Chapter 4 “Software Reliability and Quality Assurance” | Direct adjacent coverage of quality models, reliability metrics/growth, CMM, and ISO 9000 | Strongest broad cross-check candidate. Keep its definitions, model assumptions, and page numbers separately attributed; use only for a confirmed gap or materially clearer explanation. |
| Rajib Mall, *Fundamentals of Software Engineering*, 4th ed. | Chapter 11, PDF pp. 611–621 and 632–637 | Reliability metrics, operational profile, reliability growth/Jelinski–Moranda, quality attributes, CMM | Best targeted candidate for reliability-model intuition and CMM; check exact printed page labels before citations. |
| Roger S. Pressman, *Software Engineering: A Practitioner's Approach* | Chapter 8, PDF pp. 240–247 (printed pp. 212–219 visible in headers) | Reliability as an end-user failure concern and quality-assurance context | Use for a concise clarification only; it does not replace the named five-model coverage. |
| Ian Sommerville, *Software Engineering*, 9th ed. | Reliability testing/operational profile, PDF pp. 418–420 (printed pp. 401–403); ISO 9001 context, PDF pp. 677–679 (printed pp. 660–662) | Reliability testing and operational-profile context; quality-management standard framing | Targeted optional explanation only. Do not import broader dependability/security chapters. |
| R.J. Leach, *Introduction to Software Engineering*, 2nd ed. | Reliability-model discussion, PDF pp. 330–332 (printed pp. 302–304) | Statistical testing/reliability model context | Additional candidate; not needed unless the primary model explanation has a real gap. |

## Other related files and authority boundary

- `05_Seminars_&_Slides/Reliability_Seminar/Ch7_Software_Reliability.pdf` is an existing OpenCode-produced seminar artifact; the current PDF is **62 pages** (the older session-log claim of 56 pages is stale). Its Markdown source has 25,738 words, 17 tables, and 24 generated grayscale figures. Its structural `qa_check.py` passes, but `eq_check.py` currently detects **zero** numbered equation lines: its regex requires a leading `*`, while the current Markdown equations are plain lines, and its empty-list numbering check passes vacuously. The script's hard-coded numerical assertions do not parse or compare the document's formula text. Therefore, the reported equation-check success is not evidence that the written equations were verified. Keep this artifact as a navigation/checklist aid; its claims and generated figures are not answer sources until checked against the primary book/slides. It also contains extra material beyond the instructor list (for example, reliability metrics, SQA, ISO 25010, and model-selection/limitations material).
- The same folder's `_reliab_sources.txt`, `_quality_sources.txt`, `SOURCE_ch7_slides.txt`, OCR text, and build scripts are generated research aids from that seminar work. They can point to pages but are not primary evidence.
- Targeted searches of the three external question-bank PDFs found generic overlap on software reliability, McCall/ISO 9126, and CMM/CMMI. They provide question-form examples only; they do not add scope, an authoritative answer key, or evidence of this instructor's preferred marks.
- The mirrored Chapter 7 slide PDF is text-identical by page after whitespace normalization; retain one indexed copy to avoid duplicate retrieval.

## Current coverage conclusion

All **19/19** instructor terms have a mapped official-slide location and a provisional scanned-book chapter range. This establishes navigation coverage only. It does not yet establish that every answer, formula, figure, or model detail has been verified, nor does it mean every possible exam question is covered.
