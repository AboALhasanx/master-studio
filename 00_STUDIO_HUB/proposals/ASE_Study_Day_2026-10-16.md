# Advanced Software Engineering — Coordinated Study Day

> **Date:** 2026-10-16  
> **Coordinator:** Codex (GPT-6)  
> **Special event:** A shared, non-competitive study sprint across the Master Studio agent harnesses. Today's minimum target is to complete Chapters 1–3 as usable, source-checked question-and-answer study packs.

## Student-approved working rules

- Write both questions and model answers in English only. Do not add Arabic translations or explanatory sidebars; the student will annotate difficult words by hand after printing.
- Aggarwal & Singh is the controlling source for content, exercises, and model answers. Use its chapter text/book pages first. Use matching slides to check lecture coverage, not to overrule the book. The student identifies `Reference_Textbooks/AliFahim_Software_Engineering.pdf` as an older scanned edition of the Aggarwal source; prefer the searchable copy for routine reading and consult the scan selectively only to resolve a verified edition/topic/page gap.
- Consult Pressman, Sommerville, Mall, or another source only to fill a specific, verified omission in Aggarwal. Record why that source was needed and keep it secondary.
- Put a verbatim Aggarwal question's source beside the question. Leave an agent-authored question unreferenced at the stem. Cite the source for every answer, including answers to authored questions.
- Put each model answer directly under its question. Keep answers exam-ready and compact without removing reasoning or steps needed for a correct answer.
- The student has supplied the instructor's vocabulary lists for Lectures 1–3 from the cohort-group post. These are confirmed scope inputs and have been added to the ASE local index. Do not mark those chapters fully covered until every term has been mapped to Aggarwal and any genuine gaps have been checked in a supporting source. Vocabulary for later lectures remains pending.

## Today's completion target

Complete Chapters 1, 2, and 3 using one shared standard. A chapter counts as complete only when it has:

1. A source and topic coverage map tied to Aggarwal chapter/page anchors.
2. A chapter-specific question-type map: recall, explanation, comparison, diagram/model, calculation, interpretation, or scenario only where supported by that chapter.
3. A pruned question set with model answers immediately below each question and source anchors on answers.
4. A checked, printable PDF and an editable source file.
5. Coverage of the supplied vocabulary list for that chapter, with any genuine Aggarwal gaps explicitly sourced from a secondary book.

If a chapter's vocabulary list has not arrived, complete all source-grounded work that can proceed and mark the chapter **pending vocabulary coverage**. Do not claim full completion or invent the professor's terms.

## Coordinated workflow

### 0. Shared boot and source control

- Read `ACTIVE_STATE.md`, `HARNESS_REGISTRY.md`, this plan, and the canonical daily session before editing.
- Sign in by harness name in the existing `sessions/2026-10-16.md`; do not create parallel session logs.
- Use one chapter owner at a time for each deliverable. Other agents send findings to the owner/coordinator instead of editing the same file. Preserve prior harness work and name it with its date when reusing it.

### 1. Inventory and light memory

- Treat the existing `03_Study_Notes/ASE_Ch1-3_Exercises_Aggarwal.md/.pdf` as historical input. Verify its page count and content before deciding what to retain; never overwrite it.
- Maintain one lightweight ASE source index with relative path, chapter/week, source role and authority, topic/terms, page count or file type, and status (current, supporting, duplicate, archive, or QA-only). Link to sources rather than copying entire books into the index.
- A rebuildable, metadata-only local FTS5 index now covers 513 files under the ASE subject folder. It has verified instructor keywords for Lectures 1–3, anchored to the user-provided vocabulary post dated 2026-09-16, 2026-09-23, and 2026-09-30. It is lexical navigation, not vector/semantic retrieval; it stores no book text. Do not use the Sieve cloud API. Later vocabulary can be added after receipt and source checking.

### 2. Chapter source audits

- Read each matching Aggarwal chapter and its exercises. Record section/page boundaries, exact question text where used, answer evidence, and the question forms supported by the material.
- Cross-check the matching publisher slides and existing lecture assets for coverage. Compare against the student's vocabulary list when received.
- Cross-check the matching publisher slides and existing lecture assets against the supplied vocabulary lists for Lectures 1–3.
- Extract only useful existing questions from verified question banks and exercises; discard repetition and unsupported depth. Keep the source and exact wording traceable.
- Treat the SRS/project examples as structure examples, not answer authorities. Treat MAIT tutorials and the MRCET exam as supplementary question-form examples from another institution, not as professor-authored questions or primary content sources.

#### Provisional question-type map from checked Ch1–2 slides/exercises and Ch3 coverage

| Chapter | Supported forms to retain if matched by the official terms/exercises | Guardrail |
|---|---|---|
| **1 — Introduction** | Define, list/classify, explain causes, compare, correct a myth, analyze a documented failure case, interpret/draw a simple graph, MCQ, and a light LOC/person-month productivity application. | No extended numerical section; only include a calculation if the source actually supports it. Ch1 has printed exercise-number anomalies on pp.58 and 63–64. |
| **2 — SDLC Models** | Define/explain, compare models, list benefits/limitations, draw/interpret the Spiral, reason about risk, choose a model for a scenario, describe Unified Process phases and outcomes. | Checked Ch2 exercises 2.1–2.22 (printed pp.46–48) support no equation/calculation set. Include Agile/XP/Scrum because they are in the supplied instructor list, but map coverage to sources rather than presume they are in the Ch2 slide deck. |
| **3 — Requirements** | Define/classify requirements; compare user/system and functional/nonfunctional requirements; explain or select elicitation methods; conduct feasibility reasoning; construct/interpret use-case, context/DFD, and ER models; specify data dictionaries; inspect, improve, or validate SRS quality. | The vocabulary includes elicitation, analysis, documentation, and validation. Diagrams are appropriate where the source or prompt calls for them; do not invent formula work. Verify every diagram convention and answer against the actual cited source pages. |

This is a **provisional content-supported map**, not the final question selection. The final map must be reconciled with the instructor lists and the user's print-pack preferences before chapter completion.

### 3. Author and review

- Use the agreed common format for all three chapters, while varying question forms by chapter content.
- Separate direct source questions from authored questions using the source-label rule above. Do not present authored questions as professor/book questions.
- Review answers against the cited Aggarwal pages. For any secondary-source supplement, verify the claimed gap and cite the exact supporting source/page.
- Keep the set usable on paper: readable spacing, answer visually distinct but immediately below the question, diagrams/tables printable, and no excessive duplicate questions.

### 4. Publish and verify

- Keep Markdown as the editable source and export the student-facing print PDF with the existing PDF exporter. Use the study-pack layout for chapter packs; consider a single booklet only after the chapter PDFs are individually approved.
- Run `note_linter.py --fix --strict` on each Markdown deliverable and resolve all failures. Quiz JSON balancing rules apply only if a WebUI quiz JSON is separately requested; they do not replace review of the printable open-response pack.
- Inspect rendered PDF pages for clipping, answer placement, diagrams, page breaks, and source legibility. A successful export alone is not visual verification.
- Add a compact final index of question types for Chapters 1–3 today. Extend it chapter by chapter later until it covers all ten chapters.

## Agent coordination contract

- **Codex (GPT-6), coordinator:** owns this shared plan, source hierarchy, cross-chapter format, merge decisions, and final verification. The coordinator's name is recorded first for today's event.
- **Chapter owners:** each agent announces its harness and identity at the start of its contribution, claims one chapter, reports source-backed findings, and avoids editing another owner's active deliverable.
- **All harnesses:** use the canonical daily session file, leave other agents' work intact, state what they verified versus inferred, and pass source/page anchors with every finding. The shared aim is one consistent study pack, not competing versions.

## Known inputs and pending items

- Correction after the user's pointer to `02_Raw_Materials/Reference_Textbooks/`: `AliFahim_Software_Engineering.pdf` is a 256-page two-page-spread scan whose contents page says “Preface to the Third Edition” and lists the course-aligned sequence: Introduction, SDLC Models, Requirements Analysis and Specifications, Project Planning, Design, Metrics, Reliability, Testing, Maintenance, and Certification. It is a narrative textbook scan with printed book-page anchors, not a slide deck. Use the searchable textbook as the working copy, as the student requested; consult this scan selectively only if a real coverage or page discrepancy appears. Do not OCR or transcribe it wholesale.
- The searchable `CS_Agarwal_SW_Engineering_and_Testing_2010.pdf` has 529 pages and extractable text. Its embedded metadata names B. B. Agarwal, S. P. Tayal, and M. Gupta; its table of contents has a different chapter arrangement (for example, Ch4 is Reliability and Quality Assurance, while the scanned Third Edition contents place Project Planning at Ch4). Treat it as a searchable related/versioned source, not as proven page-for-page equivalence to the scan. Cross-check by topic and edition; cite the actual file and page used.
- The similarly named `Aggarwal_Singh_SE_3rd_ed_By_Chapter/Ch01–10` PDFs are publisher companion slides, not book chapters. The 1094-page `00_SOURCE_Full_1094pp_Slides.pdf` and same-hash `_REAL_Aggarwal_Singh_Textbook.pdf` are also slide series, according to the collection README. Keep book citations distinct from slide citations.
- The existing combined exercises pack is `03_Study_Notes/ASE_Ch1-3_Exercises_Aggarwal.md/.pdf`; a source audit measured the PDF at 7 pages. It is a short question collection, not the SRS sample and not the user's separately described older ~148-page exercise set. Preserve it and assess it as supplemental material; do not overwrite it.
- The subject folder has additional reference material: MAIT ETCS252 tutorials (80 MCQs plus a short problem sheet), one 19-page MRCET end-term paper, three separate question-bank PDFs (GitHub/KPRIT: 6 pages; UnitWise/NRCMEC: 3 pages; SEPM/module-wise: 3 pages), and an SRS/project-sample folder. Its README identifies the Student Management SRS sample as 232 pages and for format/structure only. These files are indexed but are secondary question-pattern/structure evidence; they are not Dr. Ali's question bank.
- The user's `C:\Users\gokoq\Downloads\5-word.json` is present (32 MB; OpenCode session titled “تحليل مصطلحات جابتر 5 وتصميم السيمنار والتحكم بـ Word عبر الذكاء الاصطناعي”). Its user-facing history records the Design seminar review and the instructor's concept-level feedback: missing abstraction, stepwise refinement, information hiding, fan-in/fan-out, depth/width, design review, and DFD-to-structure-chart methodology. It also records that students were asked to provide sources. Treat this as a useful observed example of semantic coverage review and source expectations, not as proof that those Chapter 5 topics belong in Chapters 1–3. The Doctor Profile already contains the longer cross-session record.
- The supplied lecture vocabulary text is at `C:\Users\gokoq\.codex\attachments\47d04156-932c-4e5f-8296-76b36aac7c69\Pasted text.txt`. It includes Lecture 1 (Sep 16), Lecture 2 (Sep 23), Requirements Analysis and Specifications (Sep 30), plus later planning/design/metrics vocabulary. Only the first three lists are incorporated into today's Chapters 1–3 scope; later lists remain available for their chapters.
- `00_Doctor_Profile.md` records lecture vocabulary lists as a likely exam-scope signal broader than the book. Student-provided lists are therefore a required coverage input.
- The OpenCode session `C:\Users\gokoq\Downloads\5-word.json` was located and reviewed for relevant user-facing course history. It is an important professor-mindset record, summarized above; see Doctor Profile §7 for the detailed prior analysis.

## Today's run order

1. Confirm existing files and available PDF/OCR/export/lint tools; avoid creating replacement utilities if current tools suffice.
2. Verify and classify the existing Chapters 1–3 exercise pack and the supporting question/SRS materials.
3. Complete the three non-overlapping chapter source audits under this shared rule set.
4. Map the now-received Lecture 1–3 terms to the source material; then finalize each chapter's coverage and question set.
5. Run source, answer, linter, and rendered-PDF checks; publish the three chapter packs and the Chapters 1–3 question-type index.
6. Update the canonical session journal and `ACTIVE_STATE.md` with completed chapters, pending terms, and the next exact action.
