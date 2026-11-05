# ASE Chapter 1 — Question-Bank Coverage Audit

## Scope and source hierarchy

The instructor vocabulary ledger is `03_Study_Notes/Ch01_Introduction/V1_Vocabulary_Coverage.md`. The primary answer sources are the chapter's vetted study packs, which cite Aggarwal & Singh, *Software Engineering*, 3rd ed. by section and printed page. The error/fault terminology and professional ethics additions are explicitly supported by Sommerville (9th ed.); `defect`/`fault` synonymy is separately supported by Pressman. The vector index is only a scope-finding aid, not an answer source.

## Baseline findings from the legacy banks

- The current split bundles several instructor terms together, so it does not provide one bank per confirmed vocabulary block.
- A deterministic scan found substantive-looking option text padded with words such as “here”, “now”, “again”, and “too” across the banks. The strict balancer accepts some of these because it measures length, not meaning.
- The scan found 106 padded option strings. A disposable preview that removed only those filler suffixes failed the shape gate, with more than 70 option-shape warnings; therefore simple deletion is unsafe, and the choices need substantive rewriting as part of the bank rebuild.
- The chapter-wide quality gate found one near-duplicate pair in the product/process metrics bank. No deterministic structure or shape failure was reported by that gate.
- Root cause in the gate suite: the balancer and the existing shape gate are length/position checks; neither measures whether a suffix is meaningful. Added a separate `--padding-gate` with regression coverage. The general shape gate remains unchanged; newly authored/rebuilt banks must pass the additional check.
- Each legacy Ch01 bank failed the added padding gate. Those banks were moved to `_retired/`; the rebuilt active set clears the padding gate.
- A raw schema check confirmed that the stored `answer` and `correct` fields agree for the sampled IBM questions; the earlier apparent mismatch came from inspecting option zero rather than the keyed index. Do not report a key error without the keyed text.

## Vocabulary-to-bank disposition after the Chapter 1 rebuild

| Instructor item | Source-supported content | Disposition |
|---|---|---|
| Evolving role of software | Aggarwal §1.1, p.1; §1.2.1, p.4 | Covered in the software-engineering bank through the maintenance-cost shift and the disciplined objective; no separate bank was created because the support substantially overlaps that block. |
| Changing nature of software | Aggarwal §1.3, pp.10–11; Fig. 1.7 | Gap: the available source gives an eight-area taxonomy but not enough distinct, non-repetitive evidence for an eight-question bank under the no-list-padding rule. |
| What software is | Aggarwal §1.2.2, pp.4–6; Figs. 1.1–1.3 | Rebuilt as its own bank. It uses programs, documentation, operating procedures, manual families and examples; it does not substitute “data” for the book's wording. |
| Definition of software engineering | Aggarwal §1.2.1, p.4; T2 1.8–1.10 | Rebuilt as its own bank; Bauer and Schach are distinguished, with the quality, maintainability, time, budget and requirements objective. |
| Software process | Aggarwal §1.2.3, pp.6–7; §1.5, pp.13–14; T2 1.16–1.25 | Rebuilt as its own bank; product/process, measures and metrics, effort, productivity, and balanced process use are tested. |
| Software crisis | Aggarwal §1.1, pp.1–2; §1.4, p.12 | Rebuilt as its own bank; contributing pressures, crisis effects, emergence of the discipline, IBM figures and two case applications are included. |
| Software crisis: IBM figures | Aggarwal §1.1, p.1; quoted [IBMG2K] figures | Integrated into the crisis bank. A standalone bank is not supported by the three figures and their limited direct interpretations. |
| Software myths | Aggarwal §1.4, pp.11–12; T3 U.3 | Rebuilt as its own bank; questions test the myth concept, grouping, consequences and selected distinct applications rather than one item per myth row. |
| “No Silver Bullet” | Aggarwal §1.1.2, p.3; T4 A.6 | Rebuilt as its own bank, including the claim, CASE-tool experience, conceptual work and named software difficulties. |
| Documented failures | Aggarwal §1.1.1, pp.2–3; official slides 14–15 for Shuttle only | Partial coverage in the crisis bank through Y2K and Patriot. No separate failure-list bank was created: the six-case list alone cannot support eight distinct questions without turning each list row into recall. The remaining individual cases are a documented bank-scope gap. The Shuttle remains slide-sourced and is not attributed to the book. |
| Error, fault, failure, defect | Sommerville §11.2, p.297, Fig. 11.3; Pressman §8.4.1, p.203 | Rebuilt as its own bank; the causal progression is distinguished from externally visible failure, and defect/fault synonymy is preserved. |
| Professional ethics | Sommerville §1.2, pp.15–16 | Gap: the available Ch01 coverage note is only a short summary and does not retain enough sourced principle detail for eight distinct, application-based questions. |
| ACM / IEEE Code of Ethics | Sommerville §1.2, pp.15–16, Fig. 1.3 | Gap for the same evidence limit; the shared code and principle names are acknowledged in the coverage note, but a thin recall-only bank was not shipped. |

The replacement banks were cross-reviewed against the vetted chapter packs and vocabulary map. This was not a blind or independent content review. `quiz_authoring_audit.py --strict`, the chapter structural/shape/anti-padding gates, the strict psychometric check, and v2/v3 schema validation were run on the replacement set. Manual keyed-text inspection caught and corrected two wrong keys before release. The local evidence does not settle the three scope gaps above.

## Authoring and release boundary

Each shipped topic bank must contain 8–16 meaningful questions. A structurally green bank does not establish factual correctness, Arabic/English equivalence, or absence of answer-shape clues. Re-open every built JSON after balancing and verify each keyed answer against the source-backed intent. Retire superseded banks to `_retired/` only after their unique, valid questions are accounted for. Regenerate the generated bank state after the final set is settled; this audit intentionally carries no bank totals or version numbers.
