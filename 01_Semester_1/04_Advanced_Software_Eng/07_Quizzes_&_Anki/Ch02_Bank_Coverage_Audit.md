# ASE Chapter 2 — Question-Bank Coverage Audit

## Scope and evidence

The confirmed scope is Dr. Ali Fahem's vocabulary list in `03_Study_Notes/Ch02_SDLC_Models/V2_Doctor_Vocabulary.md`. The list identifies the examinable topic blocks; it does not specify marks, question counts, or that every textbook subheading needs a separate bank. The primary course text is B.B. Agarwal et al., *Software Engineering*, Chapter 2. The chapter's vetted study packs and source map were used to locate and cross-check material. K.K. Aggarwal & Yogesh Singh's course text/slides and Sommerville were used only where the course text lacks a dedicated treatment or where the lecture explicitly supplies a model-selection/diagram distinction.

The verified course-text span consulted for the principal SDLC/model material is printed pp. 29–52. The lecture's RAD activity sequence, Unified Process phase/workflow diagrams, Spiral reading key, and model-selection matrices were checked against their visible slide content. Some slide image filenames in the local source atlas do not match the displayed matrix; the displayed source image, rather than its filename, was treated as evidence. Exact page-level attribution for every supporting-source detail should be checked in the referenced source map before expanding beyond the scope below.

## Vocabulary-to-bank disposition

| Confirmed vocabulary block | Evidence and distinctions retained | Disposition |
|:--|:--|:--|
| SDLC, Build & Fix, Waterfall | Course text supports SDLC and Waterfall; Build & Fix is explained with the mapped supporting text/slides. Waterfall phase order and feedback are kept distinct from an unstructured Build & Fix cycle. | Covered together because these concepts are directly comparative and the evidence supports distinct application questions. |
| Incremental and Iterative Enhancement | Incremental delivery adds usable functionality in pieces; iterative enhancement revises/refines an existing solution. The sources do not justify treating the terms as synonyms. | Covered together with questions that test both the distinction and a short scenario. |
| RAD and applicability conditions | The book's staged RAD account and the lecture's activity labels are not silently merged. Applicability is tied to the stated team, user, and tooling conditions. | Covered; claims are limited to the conditions supported in the course materials and mapped source. |
| Evolutionary and Prototyping | Evolutionary development and prototyping are connected but not interchangeable; prototype purpose and evolution of the delivered system are distinguished. | Covered together as the instructor groups them, without padding a standalone prototype bank from repeated definitions. |
| Spiral and risk-driven development | Spiral is risk-driven; its loop/quadrants are read in their documented order, including review and planning the next loop. | Covered; removed the unsupported shortcut that skipping risk automatically makes a process Waterfall. |
| Unified Process | Inception, elaboration, construction, and transition are phases; workflows are a separate dimension and may occur across phases. | Covered using the mapped UP source and lecture figures. |
| Selecting a life-cycle model by requirements and risk | Selection-matrix axes are interpreted from the displayed lecture figures. The low project/team experience case points to Spiral in the verified matrix. | Covered using evidence-backed scenario questions; corrected the earlier answer that contradicted the actual matrix. |
| Agile / XP / Scrum | Agile principles, XP practices, and Scrum roles/events/artifacts are kept at the distinctions supported by the mapped source. | Covered without expanding into unrelated Agile methods. |

## Quality corrections and limits

- Removed generic suffixes that made distractors longer without adding meaning, and rewrote weak choices as plausible technical alternatives.
- Corrected unsupported or overgeneralized claims about RAD, Spiral, evolutionary development, Unified Process, and model selection. Where the book and lecture use different labels or levels of detail, the bank preserves that distinction.
- Checked keyed-answer intent against the cited source material after answer balancing. The automated gates establish schema, shape, length balance, and answer-position balance; they do not prove factual accuracy, so the source review remains necessary.
- The instructor vocabulary and available course sources support the published topic coverage. They do not establish that every secondary-text detail is required on the exam. No unsupported extra model taxonomy or generic filler was added to inflate coverage.
- No further independent bank is justified by the currently mapped evidence without duplicating these topic blocks. Reopen the scope if the instructor supplies additional marked material or a corrected vocabulary list.

## Release record

The rebuilt banks passed the chapter quality gate (including shape and anti-padding checks), strict authoring audit, per-bank strict psychometric check, schema validation, publish dry run, live payload comparison, and production browser QA. The live ASE payload and local mirror were synchronized. The production service-worker precache was already current, so no shell deployment was needed. Current bank totals and content/shell versions are recorded only in the generated `00_STUDIO_HUB/QUIZ_BANK_STATE.md`.
