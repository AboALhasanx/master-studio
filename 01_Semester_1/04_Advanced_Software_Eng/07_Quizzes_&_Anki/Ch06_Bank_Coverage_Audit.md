# ASE Chapter 6 MCSQuiz Coverage and Review

**Reviewed:** 2026-11-06
**Status:** Rebuilt, source-audited, globally published, strict-gated, and live-payload verified; portal CI and production deployment are green.

## Student format decisions

Use concise bilingual MCQs that test definitions, formula or model meaning, notation, assumptions, distinctions, and key course notes. Keep scenarios short. Do not turn these banks into long numerical-result problems. Keep each topic bank within the agreed 8–16-question limit and avoid filler.

## Evidence and scope limits

- Supplied scope: [`V6_Doctor_Vocabulary.md`](../03_Study_Notes/Ch06_Software_Metrics/V6_Doctor_Vocabulary.md). The original instructor post is not attached; the recovered vocabulary establishes scope, not exam weighting.
- Source and gap map: [`V6_SOURCE_COVERAGE_MAP.md`](../03_Study_Notes/Ch06_Software_Metrics/V6_SOURCE_COVERAGE_MAP.md), including printed-page and slide anchors and the limits of each source.
- Explanatory vocabulary ledger: [`V6_Vocabulary_Coverage.md`](../03_Study_Notes/Ch06_Software_Metrics/V6_Vocabulary_Coverage.md).
- Source question/exercise inventory: [`V6_SOURCE_QUESTION_INVENTORY.md`](../03_Study_Notes/Ch06_Software_Metrics/V6_SOURCE_QUESTION_INVENTORY.md). Its source question numbers are locators; no publisher answer key was found, so answers were independently checked against the cited material.
- Course spine: Aggarwal and Singh, *Software Engineering*, third edition, Chapter 6 and its companion slides. The scanned book's title page is absent, so the bibliographic identification remains high-confidence but inferred. The supplied vocabulary also requires selected, separately mapped material from Chapters 4, 7, and 8.
- Supporting sources are used only for documented gaps: Pressman for Henry–Kafura and DRE, Mall for phase containment, and the mapped sources for specific measurement terms. The student seminar PDF is not treated as answer authority.

## Supplied-topic coverage

| Supplied topic | Active bank | Review |
|:---|:---|:---|
| Measurement fundamentals | Measurement Fundamentals | [Review section](Ch06_Draft_Review.md#draft-quiz-ch06-t01-measurement-fundamentals) |
| Metric categories | Metric Categories | [Review section](Ch06_Draft_Review.md#draft-quiz-ch06-t02-metric-categories) |
| Software size measures | Software Size Metrics | [Review section](Ch06_Draft_Review.md#draft-quiz-ch06-t03-software-size-metrics) |
| Halstead software science | Halstead Software Science | [Review section](Ch06_Draft_Review.md#draft-quiz-ch06-t04-halstead-software-science) |
| Data-structure measures | Data Structure Metrics | [Review section](Ch06_Draft_Review.md#draft-quiz-ch06-t05-data-structure-metrics) |
| Information-flow measures | Information Flow Metrics | [Review section](Ch06_Draft_Review.md#draft-quiz-ch06-t06-information-flow-metrics) |
| Control-flow and complexity measures | Control Flow Complexity | [Review section](Ch06_Draft_Review.md#draft-quiz-ch06-t07-control-flow-complexity) |
| Object-oriented measures | Object-Oriented Metrics | [Review section](Ch06_Draft_Review.md#draft-quiz-ch06-t08-object-oriented-metrics) |
| Use-case-oriented measures | Use-Case Oriented Metrics | [Review section](Ch06_Draft_Review.md#draft-quiz-ch06-t09-use-case-oriented-metrics) |
| Quality and defect measures | Quality and Defect Metrics | [Review section](Ch06_Draft_Review.md#draft-quiz-ch06-t10-quality-and-defect-metrics) |
| Productivity and process measures | Productivity and Process Metrics | [Review section](Ch06_Draft_Review.md#draft-quiz-ch06-t11-productivity-and-process-metrics) |
| Analysis and measurement program | Metrics Analysis and Program | [Review section](Ch06_Draft_Review.md#draft-quiz-ch06-t12-metrics-analysis-and-program) |

## Source boundaries

- LOC and Function Points follow the course's Chapter 4 counting and component conventions. Function-point coverage distinguishes internal logical files from external interface files and preserves the course VAF range.
- Halstead items follow the companion slides' operator/operand notation, C counting rules, and definitions of effort and estimated time.
- Data-structure questions preserve the course distinction between module weakness and program weakness; program weakness is an average of module weaknesses, not their sum.
- Information-flow questions separate the course slide's fan-in/fan-out boundary convention from the separately sourced Henry–Kafura formula. IF4 and Shepperd variants are not asserted without verified source support.
- Cyclomatic-complexity items use the three methods supported by the course source. Essential/design complexity, knot count, and nesting depth are not expanded into unsupported definitions.
- OO questions draw on the course's metric vocabulary and the verified CK, Lorenz–Kidd, and MOOD material. No unsupported metric variant is introduced.
- Use-case coverage is limited to sourced actor and transaction-count weights. Unsupported UCP adjustments and effort-estimation formulas are excluded.
- Defect questions use sourced DRE, phase-containment, and MTBF definitions. Customer-reported problem metrics are not given an invented formula.
- Analysis questions cover the slide-supported descriptive statistics, plots, PCA, correlation/regression, outliers, data issues, and measurement-program practices. Theoretical/empirical validation and ethics claims remain bounded to what the mapped material supports.

## Corrections to the superseded active set

The new wording corrects source mismatches in measurement scales and reliability, LOC and the FP adjustment range, Halstead vocabulary/volume/effort, program weakness and variable-span treatment, and the activity-level DRE error sets. Unsupported IF4/Shepperd variants, essential/design complexity, knot/nesting claims, and UCP adjustment/effort formulas were removed rather than presented as verified facts. The source map records the supporting evidence and remaining limits.

## Published artifact and release verification

- [Open the full bilingual question review](Ch06_Draft_Review.md). It displays each stem, all answer choices, the keyed answer, and the explanation.
- The active schema-v2 bank files are the source of truth; the tracked builder is [`build_ase_ch06_banks.py`](../../../90_Shared_Toolbox/tools/build_ase_ch06_banks.py).
- Structural, shape, anti-padding, strict answer-balance/schema, scoped authoring, portal-schema, and publish dry-run checks passed. The live payload audit, offline mirror refresh, portal CI, and production deployment are recorded below.
- Bank totals, chapter totals, and content/shell versions are maintained only in the generated [`QUIZ_BANK_STATE.md`](../../../00_STUDIO_HUB/QUIZ_BANK_STATE.md).

## Review and release record

- The student authorized replacing the old Chapter 6 banks, publishing globally, and updating the shared portal. Superseded files are retained under `_retired/`.


- Chapter structural, shape, anti-padding, strict answer-balance/schema, bilingual portal-schema, and scoped authoring gates passed; the publish dry run was clean.
- The full portal sync retired the superseded Chapter 6 IDs. The live manifest now returns the new bank IDs, their v3 payloads match the exact local conversions, and the retired IDs are absent.
- The portal mirror pull completed; after the content-only correction, the service-worker precache was already current. Portal CI passed after local UI specs were isolated from the live content-manifest endpoint.
- The production deployment reached READY at the public portal alias. No bank totals or release versions are duplicated here; the generated state file remains authoritative.
- The PCA item was revised to test the method without referring to the analysis slides. The shared reference detector now distinguishes handout references from technical source-code, source-file, and module wording; the generated state shows Chapter 6 clean and its drift check passes.
- The shared publisher merge was fixed so a stale portal English-text alias cannot mask an updated canonical vault stem; existing Arabic translations still fill blank vault fields. The targeted regression checks pass.
- The corrected content was republished globally and the exact live v3 question payload matches the local v2 conversion; retired IDs remain absent.
- After the content-only correction, the generated offline bank and index were pushed. The complete portal CI passed with no failures, the production deployment reached READY again, and an authenticated Vercel CLI read-back confirmed the deployed corrected stem and explanation.
