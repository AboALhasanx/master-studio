---
subject: "02_English_Language"
artifact: "Exercise inventory and vector-memory metadata map"
scope: "New Headway Upper-Intermediate Units 1–2; Q: Skills for Success 4 Units 1–2"
status: "Inventory from existing solution files and their source/audit notes; not an independent re-solution of every answer"
---

# English Exercise Inventory for Vector Memory

## Purpose

Use this map to label and retrieve exercises from the four existing solution sets. An exercise may carry multiple labels: for example, a listening gap-fill can be tagged `listening`, `grammar`, and `fill-in`. Keep the source, edition, printed page, and answer-evidence status attached to each indexed chunk. Do not merge answers across books or editions merely because the unit numbers match.

## Label vocabulary

| Field | Labels / values | Meaning |
|:--|:--|:--|
| `source` | `new_headway` · `q_skills` | Course book family |
| `unit` | `U01` · `U02` | Book unit, not semester week |
| `skill` | `grammar` · `vocabulary` · `collocation` · `reading` · `listening` · `pronunciation` · `writing` · `speaking` · `study_skill` · `everyday_english` | Main language area; multi-label |
| `task_type` | `matching` · `gap_fill` · `multiple_choice` · `ordering` · `true_false_correction` · `comprehension` · `transformation` · `classification` · `dictation_or_transcript` · `model_response` · `free_response` · `peer_review` · `word_formation` · `source_control` | What the learner does, including edition-specific provenance controls |
| `learning_mode` | `memorization` · `understanding` · `practice` · `production` | How to study it |
| `classroom_mode` | `class_discussion` · `pair_work` · `individual` · `presentation_or_submission` | Whether the prompt expects interaction or personal production |
| `assessment` | `exam_priority` · `class_participation` · `general_practice` · `not_single_answer` | Likely use, based on notes; not a guarantee of an actual exam |
| `answer_status` | `key_verified` · `source_supported` · `model_only` · `partial_or_cross_referenced` · `audio_missing_answer_available` · `edition_supplement` | Strength and nature of answer evidence |

## Source map

### New Headway Upper-Intermediate — Unit 1: “No place like home”

**Primary solution:** `Unit_01_No_Place_Like_Home_Solutions.md` (Student Book, Third Edition, pp. 6–15). The document identifies the course Student Book as primary and the Teacher Book as the answer-key companion. The wide-slide companion is `NH_U1_Wide_Slides/NH_U1_Wide_Slides.pdf`.

| Exercise cluster | Recommended labels | Study/use classification | Verification notes |
|:--|:--|:--|:--|
| Max's letter, Sophie's email, expat tales, phone-call dialogue | `reading`, `comprehension`, `listening` where track-based, `pair_work`, `class_participation` | Understanding; class/pair practice | Solutions include sample answers and linked listening material. Some opener/listening exercises are cross-referenced to a separate grammar note. |
| Tense system, active/passive charts, tense contrasts, colloquial-to-formal language | `grammar`, `transformation`, `gap_fill`, `exam_priority` | Understanding + practice; revise patterns | T1.3 and other track material can overlap with grammar. Preserve the track/exercise ID in chunk metadata. |
| House/home compounds and vocabulary exercises | `vocabulary`, `word_formation`, `matching`, `gap_fill`, `memorization` | Memorization + usage practice | The unit map marks the compound-word exercises as exam-relevant. |
| Everyday English social expressions | `everyday_english`, `matching`, `memorization`, `exam_priority` | Memorization + contextual use | Unit map identifies an eight-item matching activity. |
| Stress, rhythm, missing words, and speech reductions | `pronunciation`, `listening`, `gap_fill`, `memorization` | Listening/repetition | Keep pronunciation items distinct from written grammar even when contractions are involved. |
| “Talking about you”, speaking prompts, personal responses | `speaking`, `free_response`, `production`, `class_discussion`, `model_only` | Classroom/pair activity | Answers are personal or model responses, not a single official key. |

### New Headway Upper-Intermediate — Unit 2: “Been there, done that”

**Primary solution:** `NH_U2_Wide_Slides/حلول NewHeadway Unit2.pdf`; companion evidence and build record: `NH_U2_Wide_Slides/HANDOFF_TO_OPENCODE.md`. The handoff records 59 pages total, including 54 exercise pages and 5 vocabulary pages, and documents 10 QA gates. The Student Book and Teacher Book answer key were compared during the rebuild.

| Exercise cluster | Recommended labels | Study/use classification | Verification notes |
|:--|:--|:--|:--|
| Unit vocabulary and travel/explorer word sets | `vocabulary`, `memorization`, `matching`, `gap_fill` | Memorization + contextual use | Vocabulary pages are separate from exercise pages in the slide pack. |
| Reading texts and comprehension (including extended readings) | `reading`, `comprehension`, `multiple_choice`, `true_false_correction` | Understanding; exam/general practice | Long readings may span multiple source pages; index with printed page and reading title. |
| Present perfect vs. past simple and related tense practice | `grammar`, `gap_fill`, `classification`, `transformation` | Pattern understanding + practice | Match items and sentence completion are distinct task types; do not index all as generic grammar. |
| `make` / `do` and phrasal-verb exercises | `grammar`, `vocabulary`, `collocation`, `gap_fill`, `matching` | Memorization + usage | Multi-label because the distinction is lexical/collocational and grammatical in use. |
| Listening tracks T2.4–T2.14, dialogue ordering, response matching | `listening`, `dictation_or_transcript`, `ordering`, `matching`, `gap_fill` | Listening practice + memorization | Handoff says tapescripts/answers were incorporated and all numbered items in 34 source screenshots received an answer/model. Audio assets themselves are not established by this evidence. |
| Exclamations, dialogues, role-play, discussion and personal questions | `speaking`, `free_response`, `model_response`, `pair_work`, `class_discussion` | Production; class participation | Where the source key says answers vary, store the response as a model, never as the only correct answer. |

### Q: Skills for Success 4 — Unit 1: “What makes someone a hero?”

**Primary solution:** `Unit_01_What_Makes_Someone_a_Hero_Solutions.md` and its PDF. The solution metadata identifies the Student Book as Third Edition, pages 3–27. The file's unit map explicitly classifies activities and marks its coverage as complete; it also says the Teacher Book available is a different edition, with only specified identical grammar/writing/vocabulary exercises transferable.

| Exercise cluster | Recommended labels | Study/use classification | Verification notes |
|:--|:--|:--|:--|
| Unit opener, quotations, preview-the-unit prompts | `speaking`, `free_response`, `class_discussion`, `model_only` | Classroom discussion | Use sample/model answers; responses can vary. |
| Reading 1 and Reading 2 main ideas/details | `reading`, `comprehension`, `multiple_choice`, `ordering`, `true_false_correction` | Understanding + exam practice | Two readings; preserve reading title and printed page range. |
| Reading vocabulary sets and unit glossary | `vocabulary`, `matching`, `classification`, `memorization`, `gap_fill` | Memorization + contextual meaning | Glossary contains the unit's core terms and contextual expressions. |
| Previewing and vocabulary-learning skills | `study_skill`, `reading`, `vocabulary`, `classification` | Strategy practice | Store the skill prompt separately from the answer to a reading question. |
| Restrictive relative clauses | `grammar`, `gap_fill`, `transformation`, `exam_priority` | Rule understanding + practice | The solution file includes grammar explanation and Activities A/B/C. |
| Paragraph structure, ordering, analysis paragraph | `writing`, `ordering`, `production`, `model_response`, `peer_review` | Writing practice/submission | Separate fixed ordering/key items from open-ended paragraph writing. |

### Q: Skills for Success 4 — Unit 2: “What makes you want to buy something?”

**Primary solution:** `Unit_02_What_Makes_You_Want_to_Buy_Something_Solutions.md`; slide/PDF companion: `QSk_U2_Wide_Slides/حلول Qskills Unit2.pdf`. The solution identifies the Student Book as First Edition (2011), printed pages 29–53. It contains an exercise-by-exercise coverage table and source-comparison notes.

| Exercise cluster | Recommended labels | Study/use classification | Verification notes |
|:--|:--|:--|:--|
| Reading 1 “So Much Dead Space” and Reading 2 “Now on Stage: Your Home!” | `reading`, `comprehension`, `multiple_choice`, `gap_fill`, `true_false_correction` | Understanding + exam practice | Keep the two reading titles separate for retrieval. |
| Vocabulary for both readings and unit word list | `vocabulary`, `matching`, `gap_fill`, `memorization` | Memorization + contextual use | The file documents comparisons with an Oxford key for most objective items. |
| Articles `a/an/the/Ø` | `grammar`, `gap_fill`, `exam_priority` | Rule practice | The file records a correction: email blank 2 is `the`, not `a`; preserve this correction and its rationale. |
| Collocations with nouns | `collocation`, `matching`, `gap_fill`, `memorization` | Memorization + phrase use | Activity A is keyed; Activity B includes model sentences. |
| Highlighting/annotating and outlines | `study_skill`, `reading`, `classification`, `ordering` | Strategy practice | Distinguish the marking/annotation task from comprehension answers. |
| Descriptive essay, brainstorming, outline, peer review | `writing`, `production`, `model_response`, `peer_review`, `presentation_or_submission` | Productive; prepare before class | No unique answer for the essay; index model answer and rubric/checklist as support. |
| Opener, questionnaires, preview discussions, “What do you think?” | `speaking`, `free_response`, `class_discussion`, `model_only` | Classroom participation | Answers vary; do not represent model responses as official fixed answers. |
| The Q Classroom Track 5 | `listening`, `class_discussion`, `audio_missing_answer_available` | Listening/class discussion | The solution reports official answers are included, but the audio file is absent from the subject folder. |
| Activities from the Second Edition supplement | `edition_supplement`, `reading`, `vocabulary`, `source_caution` | Optional comparative practice | The solution labels these as absent from the First Edition Student Book. Keep them out of First Edition core chunks. |

## Edition and source controls

1. New Headway solution files identify a Third Edition Student Book; keep them separate from Q: Skills records.
2. Q: Skills Unit 1 solution metadata says Third Edition, while the Iraqi Mlazma README says its core source is the First Edition (2011). Treat the Unit 1 solutions as a distinct edition-linked source until each relevant exercise is matched to the exact student-book pages.
3. Q: Skills Unit 2 solution is tied to the First Edition (2011). Its own audit says the online Oxford key checked was a Second Edition key, with a documented correction and some option-order differences. Keep source edition and answer-evidence labels on every affected chunk.
4. `key_verified` means a solution artifact documents a comparison to the matching answer key/source; it does not mean this inventory independently recomputed every answer. Use `model_only` for open discussion/writing responses.
5. The unit number is not sufficient identity. A chunk key should include at least `source + edition + unit + printed_page + exercise_id`.

## Suggested vector record

```yaml
subject: 02_English_Language
source: q_skills
edition: first_edition_2011
unit: U02
printed_page: 45
exercise_id: vocabulary_skill_activity_a
skill: [collocation, vocabulary]
task_type: [matching]
learning_mode: [memorization, practice]
classroom_mode: [individual]
assessment: [exam_priority]
answer_status: key_verified
answer_file: 03_Study_Notes/Unit_02_What_Makes_You_Want_to_Buy_Something_Solutions.md
source_evidence: Oxford answer-key comparison documented in the solution file
```

## Coverage boundary

This is a taxonomy and retrieval map based on the four solution artifacts, their embedded unit maps, and the New Headway Unit 2 handoff. It does not claim that every answer was independently solved again. Before embedding, split content at exercise boundaries, attach the labels above, and retain the original answer file/page as provenance. Missing audio should stay marked as missing even when a transcript or answer is available.
