# ASE Chapter 3 MCSQuiz Coverage Audit

**Reviewed:** 2026-11-05
**Purpose:** map the active portal topic banks to the instructor scope and course sources, and record what this portal set does not claim to replace.

## Evidence used

- Instructor scope and terminology: [`V3_Doctor_Vocabulary.md`](../03_Study_Notes/Ch03_Requirements/V3_Doctor_Vocabulary.md), based on Dr. Ali Fahim's requirements vocabulary message.
- Course source map and limitations: [`V3_Vocabulary_Coverage.md`](../03_Study_Notes/Ch03_Requirements/V3_Vocabulary_Coverage.md) and [`Ch03_BUILD_PLAN.md`](../03_Study_Notes/Ch03_Requirements/Ch03_BUILD_PLAN.md).
- Question and explanation source: the Chapter 3 study packs under [`Ch03_Requirements`](../03_Study_Notes/Ch03_Requirements/), including the slide MCQ set, descriptive and analytical exercises, diagrams, and applied tasks.
- Primary factual authority: K.K. Aggarwal and Yogesh Singh, *Software Engineering*, third edition, Chapter 3, together with the companion Chapter 3 slides. The chapter source map records printed pages and slide ranges. Supporting texts were used only for cross-checks where the course source is silent; their terminology was not silently merged into the course's model.
- Prior live banks were reviewed and preserved in `_retired/`; the new active set follows the topic-bank structure and the evidence map above.

## Active topic map

| Active bank | Coverage represented |
|:---|:---|
| `Quiz_Ch03_T01_Requirements_Engineering_Process_And_Practice` | Course's four requirements activities and input/output, review as an ongoing activity, current practice pressures, communication failures, and limits of tool reliance. |
| `Quiz_Ch03_T02_Requirements_Types_And_Interfaces` | Functional and non-functional requirements; user/system and type distinctions; procedural, data-structure, and data-format interfaces. |
| `Quiz_Ch03_T03_Feasibility_Study` | Early viability, decision purpose, build capacity, cost/schedule realism, scope stability, bounded project risk, business assumptions, and plan adequacy. |
| `Quiz_Ch03_T04_Elicitation_Techniques` | Interview depth and question form, tacit needs, brainstorming, FAST, QFD, and translation of customer needs into technical requirements. |
| `Quiz_Ch03_T05_Use_Case_Approach` | External actors, goals and system boundary, include/extend distinctions, main success path, alternate flows, and behavioral modeling. |
| `Quiz_Ch03_T06_Requirements_Analysis_Models` | DFD transformations, symbols, balancing and common defects; data-dictionary role; ER components and relationship degree; prototype feedback and throwaway rationale. |
| `Quiz_Ch03_T07_SRS_Documentation` | The SRS boundary, course-era terminology, quality properties, completeness, design independence, and traceability. |
| `Quiz_Ch03_T08_Requirements_Validation_And_Reviews` | Review purpose and sequence, verification/validation distinction, preparation, checklist use, conflict resolution, follow-up, and the boundary between review and software testing. |

## Review outcome and limits

- The active set covers each instructor vocabulary area represented in the Chapter 3 source map and keeps the source's distinctions intact, including the course's four-activity requirements process and its SRS terminology.
- Items use conceptual checks and short scenarios. The portal banks are retrieval practice; they do not replace the source packs' extended written answers, full diagram construction, or multi-step applied exercises.
- Coverage in this audit means that a topic has an active question-bank representation. It does not claim that every textbook exercise or slide item has a separate portal question, nor that the banks reproduce the print packs item by item.
- Source limits already recorded in the Chapter 3 study pack remain in force: the supporting book's additional Requirements Management terminology is not folded into the course's four-step sequence; the historical feasibility statistic without a dated report is not treated as current evidence; and the source MCQ slides do not provide an official answer key.
- The strict chapter, authoring, schema, and live-payload gate outcomes are recorded in the generated [`QUIZ_BANK_STATE.md`](../../../00_STUDIO_HUB/QUIZ_BANK_STATE.md). Do not copy bank totals, question totals, or content/shell versions into this hand-maintained audit.

## Reproduction

The self-contained builder is [`build_ase_ch03_banks.py`](../../../90_Shared_Toolbox/tools/build_ase_ch03_banks.py). The publish workflow and current generated state are linked from `00_STUDIO_HUB/AGENT_HANDOFF_QUIZ_BANKS.md` and `00_STUDIO_HUB/QUIZ_PUBLISH_RUNBOOK.md`.
