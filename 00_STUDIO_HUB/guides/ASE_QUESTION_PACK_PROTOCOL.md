# ASE Exam Question-Pack Protocol

> **Scope:** Reusable workflow for question-type packs in Advanced Software Engineering. Applies to Codex, WorkBuddy, OpenCode, MiMo, FreeBuf, and any other harness working in this vault. The chapter plan and the student's latest explicit decisions remain authoritative for chapter-specific choices.

## 1. Boot and coordinate

1. Read `00_STUDIO_HUB/ACTIVE_STATE.md`, `HARNESS_REGISTRY.md`, today's session file, and the current ASE chapter's build plan and index. Follow the sign-in rule before edits.
2. Read the latest relevant decisions in `STUDENT_NOTES_LOG.md`; later decisions override older chapter notes. Update living plans when rules change, and append decisions rather than rewriting history.
3. Use one shared plan, index, and daily journal. Split review work by explicit artifact/source scope when several agents contribute. Name the harness and date for prior work; do not duplicate or overwrite work that is already verified.
4. This is an exam-pack workflow, not a study-compendium workflow. Do not force 10 units, long narrative sections, or verbatim definition blocks into a concise question pack unless the student or chapter plan requests them.
5. When a chapter has a catalog in `00_STUDIO_HUB/indexes/04_Advanced_Software_Eng/knowledge_sources.json`, use `ase_vector_index.py status` and search with `--chapter <n>` plus the needed `--category` to locate candidate passages. Retrieval and OCR help navigation only; verify each claim on the original source page/slide. Preserve the catalog's authority labels and do not index unrelated content into the chapter just because it is searchable.

## 2. Determine chapter scope before writing

- Inspect the chapter's textbook pages, assigned slides, exercise/question files, instructor vocabulary, and known exam examples. Build a coverage map that says which question, answer, or term actually covers each required item.
- Consider relevant question forms (for example MCQ, define, explain, count/list, compare, analyze a case, evaluate, draw, calculate), but do not manufacture all forms for every chapter. Use the chapter's real material and likely examinable tasks to decide which packs are warranted.
- When the instructor supplies vocabulary rather than lecture content, treat that exact list as the coverage boundary. Explain each confirmed term to a modest but usable depth: definition, main mechanism/conditions, important distinction, and a relevant diagram only where needed. Do not expand to every topic found in every textbook.
- A coverage map or source pointer is not an answer. A vocabulary item needs a usable definition or short answer; an index should show where the answer lives.
- Keep breadth and depth proportional to the course, available study time, and student request. Do not turn a small chapter or thin calculation section into an oversized essay bank.

## 3. Ground answers and citations

- Identify the exact primary textbook and edition before using its name or page numbers. Distinguish similarly named books and editions. For scans, inspect the actual page image and read the **printed page number**; record the PDF page separately only when useful.
- Follow the **chapter plan's explicit source hierarchy**; do not assume the same similarly named Aggarwal book is primary in every context. For Chapter 2, the user identified B.B. Agarwal, S.P. Tayal & M. Gupta (2010) as the course-aligned textbook; K.K. Aggarwal & Yogesh Singh's scanned third edition and companion slides are separate sources. Use one named supporting source only for a confirmed coverage/explanation gap or when it is materially clearer. This is selective source triangulation, not a merge of every book. If sources conflict, the chapter plan's primary controls. Identify slide-only material as slides.
- Check each meaningful factual claim, number, causal statement, example, category, and diagram against the cited source. Preserve qualifications and scope. A simultaneous trend is not automatically causation; a percentage of projects is not market share; a historical example is not a universal rule.
- A source citation is a locator, not evidence that a claim is correct. Confirm that the cited section/page supports the distinction and the complete answer. Never invent authors, sections, pages, editions, or DOIs.

## 4. Write for this student

- Questions, options, and model answers are in English. Student notes and traps are concise Arabic and visually separate from the English model answer.
- The student translates difficult vocabulary by hand after printing. Do not clutter model answers with inline translations, parenthetical echoes, or long side explanations.
- Answer the question's verb directly. Definitions define; comparisons state both sides; “why/how” gives the reason or mechanism; evaluation states a reasoned position. Do not leave a judgement question unanswered by saying only that the source is silent.
- Keep the answer complete but compact. Simplify difficult academic wording when accuracy and important qualifications remain. Verbatim quotation is optional; if used, reproduce the quoted wording faithfully and do not splice fragments together with the agent's commentary.
- In model answers, **bold marks source-grounded content or a faithful source paraphrase**; plain text marks our framing, reasoning, or synthesis. Put quotation marks around actual quotations only. Do not add the label `استنتاجي — مو نص أغروال` or similar. Do not write meta-prefaces such as “the book says”, “the author states”, or “the chapter explains”; place the source locator on its own line after the answer.
- For this student's ASE packs, the current source hierarchy is Aggarwal & Singh first, with named support only for gaps. The current preferred locator is author/book short name + section + printed page. Follow later student decisions if this changes.
- Do not use `bold` percentage as a proxy for correctness. Paraphrase can be source-based; plain-text judgement can be appropriate. Formatting communicates provenance but does not replace source checking.

## 5. Review independently and report honestly

Keep these review dimensions separate:

1. **Content:** Is every important claim supported, accurately scoped, and directly responsive?
2. **Coverage:** Are all items in the chapter plan, instructor list, and requested exercises actually answered?
3. **Artifact:** Do the Markdown and latest exported PDF agree, and are question and answer kept together?
4. **Presentation:** Does the rendered PDF show readable Arabic/RTL, legible diagrams, no clipping, and clear source lines?

- A blind audit means the reviewer did not see the author's answers. A cross-review means the reviewer saw them. Call each by its real name; record the artifacts, source pages, counts, corrections, and limitations. Do not imply independent or blind checking from a linter, shared-context agent review, or spot-check.
- Define percentages by their denominator. Keep artifact completion, required-topic coverage, and source-verification status separate. Do not claim that a chapter covers every possible exam question.
- Text extraction helps check presence and page placement, but it does not prove visual RTL, clipping, or diagram readability. Inspect rendered pages. If only changed or sampled pages were inspected, say so rather than claiming every page was visually inspected.
- Only close the gate that was actually requested and completed. If source verification remains open, say so; if the student has authorized closure and all applicable checks pass, update the index, plan, decision log, daily journal, and runtime state consistently.

## 6. Delivery gates

For every changed printable pack, use the current vault tools and verify their actual exit/result:

1. Run `note_linter.py <file>.md --fix --strict`; resolve findings and rerun until clean.
2. Export the matching PDF from the final Markdown. Confirm the PDF is newer than the Markdown and page count is sensible.
3. Check question-answer cohesion across the pack and confirm no literal build directives or temporary review artifacts leaked into the PDF.
4. Render and visually inspect changed pages, plus any pages implicated by pagination changes. Check Arabic/RTL and diagrams in pixels, not extraction alone.
5. Update the index and chapter plan to match disk. Append material decisions/findings to the student log and the canonical daily journal; update `ACTIVE_STATE.md` when the next action changes.

Passing a publication gate proves only the dimensions that gate checks. A clean linter is not a content audit; successful export is not visual approval; a visually clean sample is not whole-pack source verification.

## 7. Chapter 1 lessons carried forward

These are reusable failure patterns, not claims that the current Chapter 1 files still contain them:

- Book prose, official companion slides, instructor prompts, and supporting books can contain different wording and examples. Track source identity per claim.
- A source audit caught misattributed slide wording, an answer that only pointed to an absent term, a question that incorrectly asked about market share when the source reported project share, overbroad causal framing, and an evaluative answer with no judgement. Prevent them by checking attribution, answerability, units, causality, and the question verb separately.
- Long answers can accumulate unsupported interpretation. Prefer a direct, source-grounded response, then add only the short reasoning needed by the question.
- Printed-page offsets in scanned double-page PDFs must be established from visible page labels; do not copy a prior offset without checking it.
- Arabic inside an English answer can damage clarity and BiDi layout. Keep Arabic notes in their own callout, and inspect the exported PDF visually.
- A map is not coverage, a filename is not proof of export parity, and a previous agent's completion summary is not verification. Recheck the current artifacts before inheriting status.
