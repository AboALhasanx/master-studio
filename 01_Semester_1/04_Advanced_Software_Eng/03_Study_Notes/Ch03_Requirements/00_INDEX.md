# Chapter 3 — Software Requirements: Analysis and Specifications

**Course:** Advanced Software Engineering (CS603)  
**Scope source:** Dr. Ali Fahim's requirements vocabulary message, 2026-09-30  
**Status:** Source catalog and vector index built (296 Ch.3 chunks); source/diagram audit and question packs remain in progress.

## Confirmed scope coverage map

| Instructor vocabulary | Primary course evidence | Main exercise forms | Planned destination |
|:---|:---|:---|:---|
| Requirements Engineering: crucial process steps | K.K. scan §3.1, printed pp. 40–41; Fig. 3.1 p.41; slides 2–4 | Explain, order/diagram, analyze breakdown | T2, T4 |
| Present state of practice | K.K. scan §3.1, slides 4–5 | List challenges, explain consequences, propose modest improvements | T2, T3 |
| Functional and non-functional requirements | K.K. scan §3.1.1 and following types section; slides 6–7 | Define, distinguish, classify examples | T1, T2, T3 |
| User and system requirements | K.K. slides 8; written exercise 3.36(b) | Compare, classify | T2, T3 |
| Interface specification | K.K. slide 9 | List/explain interface forms and examples | T2 |
| Feasibility Study: purpose and focus | K.K. slides 11–15; slide 10 has an IBM statistic without a report date/citation and is not treated as current evidence | Explain purpose/focus; reason through feasibility factors | T2, T3, T5 |
| Risk Management Activities (listed under elicitation) | Instructor transcript; slide 14 asks if major project risks are identified and surmountable under feasibility | Bounded risk-feasibility answer; no separate lifecycle under elicitation without evidence | T2/T5, flagged in plan |
| Requirements Elicitation: interviews | K.K. slides 16–19; written exercises 3.7–3.8 | Explain/list, conduct/classify interview questions | T2, T5 |
| Requirements Elicitation: Use Case Approach | K.K. slides 27–81; slides 28–35 for concepts/guidelines and 36–81 for worked examples; exercises 3.11–3.14 | Define, components, guidelines, use-case diagram/narrative | T2, T4, T5 |
| Requirements Analysis: DFD | K.K. slides 82–86; exercises 3.20–3.23 | Explain rules/symbols; draw and analyze DFDs | T2, T4, T5 |
| Requirements Analysis: Data Dictionary | K.K. slides 87–88; exercise 3.22(ii); compare B.B. 2010 §3.3 | Define structure/content/benefit | T2, T4 |
| Requirements Analysis: ER diagrams | K.K. slides 89–100; exercises 3.15–3.19, 3.24 | Cardinality/participation, associative entity, draw ERD | T2, T3, T4, T5 |
| Requirements Analysis: Software Prototyping | K.K. slide 116; exercises 3.24, 3.26–3.28 | Explain, evaluate throw-away/reuse claims, advise on prototype use | T2, T3, T5 |
| Documentation: nature of SRS | K.K. slides 101–103 and scan §3.6–3.7; B.B. 2010 §3.6–3.7 as support | Define purpose, “what” boundary, uses/benefits | T2 |
| Characteristics of a good SRS | K.K. slides 103–110; scan; B.B. 2010 §3.10 | List/explain; detect ambiguity, omission, inconsistency | T2, T3, T5 |
| Organization of SRS | K.K. slides 105–110 and §3.6–3.7; exercises 3.30–3.35 | Explain sections/issues; create or critique a short example | T2, T3, T5 |
| Validation: Requirements Reviews | K.K. slides 111–115; B.B. 2010 §3.8 | Explain checks/review flow and corrective follow-up | T2, T3 |

## Source identity, hierarchy, and limitations

- **Course primary:** K.K. Aggarwal & Yogesh Singh, *Software Engineering*, 3rd edition. The local scan's cover/title page is missing; identity is high-confidence from internal contents/pagination plus the matching official slide series. Chapter 3 is printed pp. 40–138, scanned spreads 26–75.
- **Companion slides:** K.K. Aggarwal & Yogesh Singh, New Age International Publishers, 2007, Chapter 3, 140 slides. Slides 121–133 contain 25 MCQs; slides 134–140 contain 35 written stems and skip 3.25. The scanned textbook p.138 contains the missing-in-slides Exercise 3.25, so the full textbook exercise set has 36 stems. Slide MCQs 3.23 also repeat a printed label.
- **Supporting book:** B.B. Agarwal, S.P. Tayal & M. Gupta, 2010, Chapter 3 printed pp. 53–84 (PDF pp. 66–97). It differs in some terminology and adds Requirements Management; keep claims source-specific.
- **Answer key:** no official solution key has been located for the 25 K.K. slide MCQs yet. Any answer key assembled for T1 will be described as independently checked, not publisher-official, unless a matching key is found.
- **External question banks and SRS samples** are secondary practice/format material; they do not define lecture scope or establish the professor's answer key.

## Proposed pack allocation

Textbook exercise stems by dominant answer output (36 total, including p.138 Exercise 3.25 omitted from slides/handout): descriptive 16 (44.4%), compare/analyze/evaluate 10 (27.8%), named diagrams 3 (8.3%), system-case modeling 6 (16.7%), construct an inconsistent SRS example 1 (2.8%). Percentages describe source-bank composition, not exam marks. The 25 slide MCQs are a separate set.

Planned files: `T1_MCQ`, `T2_Descriptive`, `T3_Compare_Analyze`, `T4_Diagrams`, `T5_Apply_Create`, and `V3_Vocabulary_Coverage`. Pack boundaries can be adjusted after question-by-question mapping; avoid a thin standalone file for a single create task.

## Visual assets to assess

1. Requirements Engineering process diagram — scan Fig. 3.1, printed p. 41; companion slides 2–3.
2. Use-case elements and examples — slides 28–35; worked system/use-case narratives continue through slide 81.
3. DFD symbols/rules and examples — slides 84–86; DFD exercise prompts on slides 137–138.
4. Data-dictionary notation — slides 87–88.
5. ER concepts, degree/cardinality/participation — slides 89–100; related exercises 3.15–3.19 and 3.24.
6. SRS documentation — slides 101–110; validation and review — slides 111–115; prototypes — slide 116.

Text OCR alone cannot confirm diagram semantics or line relationships; retain a page/slide image check for every selected diagram.

## Current gates

- [x] Locate the professor's exact Ch.3 vocabulary in the supplied transcript.
- [x] Identify the three distinct course-related source families and separate their authority.
- [x] Verify the K.K scan's opening and closing printed-page mapping visually.
- [x] Inventory native MCQ and written-exercise counts and numbering anomalies.
- [ ] Map every term to exact printed pages/slides and verify source statements.
- [ ] Map and inspect the diagrams.
- [ ] Check external question-bank patterns without treating them as course authority.
- [x] Extend the local vector collection for Chapter 3 (296 chunks; total ASE vector index 1,726 chunks across Ch.2–3; local OCR on 50/50 scanned spreads).
- [ ] Author packs, export, and review them.
