# ASE Chapter 7 MCSQuiz Coverage Audit

**Reviewed:** 2026-11-06
**Status:** Rebuilt, strictly gated, and production-payload verified. At the final sync, the global portal already matched the canonical banks; the offline mirror was refreshed, and its service-worker precache was already current.

## Student format decisions

Use concise bilingual MCQs that test definitions, formula or model meaning, assumptions, distinctions, and key course notes. Keep scenarios short. Do not turn these banks into long numerical-result problems. Keep every topic bank within the agreed 8–16-question limit.

## Evidence and scope limits

- Instructor scope and terminology: [`V7_Doctor_Vocabulary.md`](../03_Study_Notes/Ch07_Software_Reliability/V7_Doctor_Vocabulary.md). The vocabulary is the student's recovered list; the original instructor post is not attached. It establishes intended coverage, not exam weighting.
- Course-source map: [`V7_SOURCE_COVERAGE_MAP.md`](../03_Study_Notes/Ch07_Software_Reliability/V7_SOURCE_COVERAGE_MAP.md), which maps the vocabulary to K.K. Aggarwal and Yogesh Singh, *Software Engineering*, third edition, Chapter 7, and the 126-page companion slide deck. The scanned book's title page is absent, so the bibliographic identification is high-confidence but inferred.
- Source exercise inventory: [`V7_QUESTION_INVENTORY.md`](../03_Study_Notes/Ch07_Software_Reliability/V7_QUESTION_INVENTORY.md). It records the publisher's MCQ and written-exercise prompts, their source locations, and unresolved source discrepancies. No official answer key was found; keyed answers were independently checked against the mapped course material.
- Related course artifacts: `T1_MCQ.md`, `T2_Descriptive.md`, `T3_Compare_Analyze.md`, `T4_Diagrams.md`, `T5_Apply_Interpret.md`, and `T7_Calculations.md` under [`Ch07_Software_Reliability`](../03_Study_Notes/Ch07_Software_Reliability/). The calculation pack remains the place for longer derivations and numeric-result problems.
- Annotation check: the inspected textbook and slide PDFs contained no PDF annotation objects, and no instructor-marked copy was found among the searched local/Downloads materials. Do not infer that any topic is crossed out or predict exam emphasis from this absence.

## Active topic-bank map

| Active bank | Coverage represented |
|:---|:---|
| `Quiz_Ch07_B01_Basic_Concepts` | Software reliability; fault versus failure; software versus hardware failure behavior; operational profile, input space, functional environment, execution time, and clock time. |
| `Quiz_Ch07_B02_Software_Quality_Models` | Quality versus reliability; McCall's factor groups and factor/criterion relation; Boehm's hierarchy; ISO 9126 characteristics, hierarchy, and user view. |
| `Quiz_Ch07_B03_CMM_Maturity_Levels` | The staged CMM progression and the defining process capabilities of Initial, Repeatable, Defined, Managed, and Optimizing. |
| `Quiz_Ch07_B04_CMM_Process_Areas` | Key Process Areas, their relation to maturity levels, the five common-feature categories, and how common features institutionalize practices. |
| `Quiz_Ch07_B05_Reliability_Measures` | Reliability probability versus failure intensity; mean-value and failure-time views; MTTF versus MTBF; trend, release, component, and project-management interpretation. |
| `Quiz_Ch07_B06_Execution_Time_Models` | Conceptual interpretation of the Basic Execution Time, Logarithmic Poisson, Calendar Time, Jelinski–Moranda, and Bug Seeding models, including assumptions and behavior. |
| `Quiz_Ch07_B07_ISO_9000` | ISO 9000/9001 roles, source-era ISO 9000-3 guidance, ISO 9001 and CMM scope, documented-process principles, mapping examples, and certification limits. |

## Review outcome

- Each recovered vocabulary area has a corresponding active-bank representation. The mapping is a coverage aid; it does not claim that every slide MCQ or written exercise is reproduced one-to-one in the portal.
- Model questions focus on interpreting relationships, assumptions, and behavior. Longer calculations, derivations, and numerical outcomes remain in the separate calculation pack, consistent with the student's MCQ-format decision.
- The MTTF and MTBF stems explicitly distinguish time to a failure from the interval between recurring failures; the quality gate no longer reports them as near duplicates.
- The complete bilingual item-by-item review, including every option, keyed answer, and explanation, is [`Ch07_Draft_Review.md`](Ch07_Draft_Review.md).
- Source-based statements follow the course book and companion slides. The source map's provisional OCR page anchors and the vocabulary's missing original instructor post remain limitations; no exam weighting or marked-out content is asserted.

## Release verification

- Structural, shape, anti-padding, strict answer-balance/schema, strict authoring, and portal v2-to-v3 dry-run gates passed. The generated [`QUIZ_BANK_STATE.md`](../../../00_STUDIO_HUB/QUIZ_BANK_STATE.md) is the only maintained location for bank totals, content/shell versions, and measured chapter-state rows.
- The subject-scoped portal sync reported no pending content changes. Read-only live audits confirmed that the live manifest contains the active Chapter 7 banks, the bilingual option pairs and keyed answers match the canonical vault files, and the live payload has no handout references.
- The portal mirror pull refreshed the offline fallback banks without pruning files. Although the service-worker precache URLs were already current, the changed fallback assets required a new shell cache release; the full portal CI passed and the production deployment completed READY.
- After deployment, the automated production-site check passed catalogue visibility, topic badges, subject labels, English/Arabic toggle, question and option reshuffling between launches, and correct-answer stability. No answer was submitted.
- The self-contained tracked authoring tool is [`build_ase_ch07_banks.py`](../../../90_Shared_Toolbox/tools/build_ase_ch07_banks.py). The banks remain the canonical source; the review sheet is derived from them.
