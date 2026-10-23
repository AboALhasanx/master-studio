# Publishing questions to the portal (بوابة MSCQuiz)

> The vault is the master. Supabase is the **content portal** in the middle.
> The app reads from the portal and keeps a local copy, so it also works offline.
>
> **Authoring rules** (schema v2/v3, the two models per chapter, bilingual style,
> the psychometric gates) live in `QUIZ_BANK_PROTOCOL.md` — read it before
> writing or editing a bank. This file covers shipping only.

## The shape of it

```
01_Semester_1/<Subject>/07_Quizzes_&_Anki/Quiz_*.json      (the master copy)
        |
        |  portal_content.py sync      (the agent, one command)
        v
Supabase:  content_banks  +  content_publishes  +  content_meta (a version)
        |
        |  content_manifest()  ->  only the chapters whose version changed
        v
PWA: manifest + banks cached on the device (IndexedDB/localStorage)  ->  offline
```

The shell (HTML/CSS/JS/fonts/KaTeX) still lives on Vercel and changes rarely.
**The questions never need a deploy**: publish them and the next visit shows them.

## The commands (agent side)

```bash
# publish everything that changed
python 90_Shared_Toolbox/tools/portal_content.py sync

# one subject only
python 90_Shared_Toolbox/tools/portal_content.py sync --subject 03_Data_Mining

# what is live right now (version, chapters, counts, drafts)
python 90_Shared_Toolbox/tools/portal_content.py status

# keep a chapter out of the app (draft) and put it back
python 90_Shared_Toolbox/tools/portal_content.py hide Quiz_Ch02_DrHuda_20MCQ
python 90_Shared_Toolbox/tools/portal_content.py show Quiz_Ch02_DrHuda_20MCQ

# copy what is published back into mcq-portal/data (a backup / a mirror)
python 90_Shared_Toolbox/tools/portal_content.py pull

# optional: also post the Telegram notice
python 90_Shared_Toolbox/tools/portal_content.py sync --notify
```

`sync` always: validates (vault gate + v3 gate + every LaTeX formula) →
merges with what is live (an Arabic translation or a topic title that only
exists in the portal is never dropped) → upserts → moves the global content
version **only when something really changed** → logs the publish.

## What the student sees

- Next visit: the **bell** shows the unread count.
- The sheet lists: subject · chapter · number of questions, each opening the quiz.
- «قراءة الكل» clears them; opening one marks it read.
- The questions are also cached on the device, so the new chapter works offline.

## The store (Supabase, project `gywniovuupjmllbmjmai`)

| object | what |
|---|---|
| `content_banks` | one row per chapter: `payload` (v3 jsonb), `version`, `chapter_no`, `topic_ar/en`, `question_count`, `has_math`, `material_url`, `hidden` |
| `content_meta` | a single row: the global publish version the app compares against |
| `content_publishes` | the audit log (actor, action, quiz, version, at) |
| `content_manifest()` | RPC: the tiny manifest (version + every chapter's version/count/topic) |
| `content_bank(p_quiz_id)` | RPC: one bank payload |

**Security:** anon can only `select`, and never a `hidden` chapter; the publish
log has no anon policy. **Writes never happen from the browser** — the agent
uses the service key fetched at run time with the Supabase Management token.

**Credentials (`90_Shared_Toolbox/tools/supabase_auth.py`):** the management
token is resolved in this order — `SUPABASE_ACCESS_TOKEN` → a personal access
token in `~/.config/opencode/supabase-pat` → the OAuth tokens that
`opencode mcp auth supabase` stores in `mcp-auth.json`. An expired OAuth token
is refreshed automatically and the **rotated** refresh token is written back
immediately (Supabase invalidates the old one on every use, so a refresh that
is not persisted breaks the chain for good). A 401 retries once after a forced
refresh. If nothing works the tool prints exactly which of the two fixes to
apply instead of a traceback.

**Retirement:** `sync` now compares the vault with the portal and **hides any
live bank whose file left the vault** (moved to `07_Quizzes_&_Anki/_retired/`),
so the vault and the portal can no longer disagree. A whole subject is never
hidden just because its folder failed to read.

## Fallbacks (nothing takes the app down)

1. Portal unreachable → the manifest this device saw last time (cached).
2. No cached manifest (first visit, no network) → the bundled
   `mcq-portal/data/index.json` + `data/banks/*` that ship with the shell.
3. A single bank fails → the cached copy of that bank is kept.

The older `publish_quizzes.py` (git + Vercel, writing `data/*.json`) still works
and is what keeps the bundled fallback fresh. It is no longer the primary path.

## The question format (Canonical Schema v3)

```json
{
  "schema_version": 3,
  "subject_id": "03_Data_Mining",
  "quiz_id": "Quiz_01_Introduction_to_Data_Mining",
  "topic": { "ar": "مقدمة في التنقيب عن البيانات", "en": "Introduction to Data Mining" },
  "version": 3,
  "has_math": true,
  "updated_at": "2026-10-21T12:00:00Z",
  "questions": [{
    "id": "q1",
    "concept_id": "support_measure",
    "bloom": "Apply",
    "stem":        { "ar": "… $R = L \\times I$ …", "en": "…" },
    "options":     [{ "ar": "…", "en": "…" }, … 4],
    "answer": 0,
    "explanation":{ "ar": "…", "en": "…" }
  }]
}
```

Math goes between `$...$` (or `$$...$$` for a block) inside any Arabic or
English string; the app renders it with KaTeX, isolated (`<bdi dir="ltr">`) so
it keeps its direction inside the Arabic line. Older v2 banks (and the alias
soup: `text`/`question`/`question_ar`, `options_ar`…) are converted on read by
`mcq-portal/tools/portal_schema.py`, so nothing breaks mid-migration.
