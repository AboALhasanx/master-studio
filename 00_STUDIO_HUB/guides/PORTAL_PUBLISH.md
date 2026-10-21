# Publishing questions to the portal (بوابة MSCQuiz)

> One command. The vault is the master copy, the portal is the consumer.

## The command

```bash
# see what would change (validates everything, writes nothing)
python 90_Shared_Toolbox/tools/publish_quizzes.py --dry-run

# publish everything, then push it live and announce it
python 90_Shared_Toolbox/tools/publish_quizzes.py --deploy --announce

# one subject only
python 90_Shared_Toolbox/tools/publish_quizzes.py --subject 01_Cyber_Security --deploy
```

The agent runs it; the student never sees a command line.

## What it does, in order

1. **Reads** the canonical banks from
   `01_Semester_1/<Subject>/07_Quizzes_&_Anki/Quiz_*.json`.
2. **Validates** them three times over:
   - the vault's schema gate (`quiz_balancer.validate_schema_v2`),
   - the portal's **Canonical Schema v3** gate,
   - every LaTeX formula between `$...$` (a broken formula never reaches a student).
3. **Merges** with what the portal already has. The vault is the master for the
   content, but an Arabic translation that only exists in the portal is never
   dropped. `--write-back` copies the merged bank back into the vault, so the
   translation work accumulates in the master copy too.
4. **Writes** `mcq-portal/data/banks/*.json` in Schema v3 and rebuilds
   `data/index.json` with a **version per chapter**. The version only moves when
   what the student sees actually changed — a formatting change is not "new
   questions".
5. `--deploy` commits, pushes and runs the Vercel deploy.
6. `--announce` posts the notice into the subject's Telegram topic
   (`tg.py publish`), so the group gets the update on their phones.

## What the student sees

- The portal asks for `data/index.json` fresh on every open (the service worker
  never serves a stale `?v=` URL).
- If a chapter's version is newer than the one stored on the device, the chapter
  is downloaded and flagged: a **«جديد»** chip on its card and a **«نزلت أسئلة
  جديدة»** notice at the top of the catalogue, with the subject, the chapter and
  the count.
- Opening the chapter marks it seen, so the notice clears itself.
- Everything is kept on the device, so the new questions also work offline.

## Canonical Schema v3 (the format the portal reads)

One bilingual shape, no aliases:

```json
{
  "schema_version": 3,
  "subject_id": "01_Cyber_Security",
  "quiz_id": "Quiz_Ch02_DrHuda_20MCQ",
  "topic":   { "ar": "…", "en": "…" },
  "instructor": { "ar": "…", "en": "…" },
  "updated_at": "2026-10-21T12:00:00Z",
  "has_math": false,
  "version": 3,
  "questions": [{
    "id": "q1",
    "concept_id": "risk_vs_threat",
    "bloom": "Apply",
    "stem":        { "ar": "… $R = L \\times I$ …", "en": "…" },
    "options":     [{ "ar": "…", "en": "…" }, … 4],
    "answer": 0,
    "explanation":{ "ar": "…", "en": "…" }
  }]
}
```

**Math** goes inline between `$...$` (or `$$...$$` for a display block) inside any
Arabic or English string. The portal renders it with KaTeX, wrapped in
`<bdi dir="ltr">` so a formula keeps its own direction inside an Arabic line.
A question can mix Arabic prose, English technical terms and formulas freely.

**Older files** (v2 and the previous alias soup: `text`/`question`/`question_ar`,
`options`/`options_ar`/`options_en`, …) are converted on read by
`mcq-portal/tools/portal_schema.py`, so nothing breaks while the shelf is being
republished.

## Files

| Path | Role |
|---|---|
| `90_Shared_Toolbox/tools/publish_quizzes.py` | the publish command (vault side) |
| `mcq-portal/tools/portal_schema.py` | v3 conversion + validation (shared) |
| `mcq-portal/data/index.json` | the manifest: version per chapter, counts, math flag |
| `mcq-portal/data/banks/*.json` | the published banks (v3) |
| `mcq-portal/js/vendor/katex/` | the math renderer, vendored for offline |
