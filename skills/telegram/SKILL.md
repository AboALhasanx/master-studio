---
name: telegram
description: "Master Studio Telegram Gateway driver. Publishes study notes, PDFs, quiz links and reports into the group's numbered topics; manages topics, replies, edits, pins and reactions — all through one outbound-only CLI the agent runs in the background (Zero-CLI for the student)."
---

# Master Studio Telegram Gateway (`telegram`)

Use this skill whenever the student asks to **publish, post, send, share, announce, pin,
edit, correct or organise** anything in the study group, or to check the gateway's health.

The gateway is **outbound-only** (`Agent → gateway → Telegram`). It never reads the group,
never runs a `getUpdates` loop, and never posts anywhere except the one allow-listed chat.
Everything below is enforced **in code**, not in this prompt (issue #16).

---

## 1. Autonomous Execution Directive (Zero-CLI)

Whenever the student asks for a Telegram action, **YOU (the agent) run the CLI in the
background**. Never ask him to run anything.

One entry point, always invoked from the **vault root**:

```bash
python 90_Shared_Toolbox/tools/tg.py [GLOBAL FLAGS] <verb> [VERB FLAGS]
```

`--dry-run` and `--live` are **global**: they must come **before** the verb.

Two rules that decide whether a call is real:

| Flag | Effect |
|---|---|
| *(none)* | Runs against the **mock** transport — validation + idempotency + audit, **no network** |
| `--dry-run` | Prints the plan and the exact Bot API call; **no execution, no audit** |
| `--live` | Real Bot API call, **only** to a chat in `TELEGRAM_CHAT_ALLOWLIST` |

**Sequence for anything new:** `--dry-run` first, read the plan, then `--live` once it looks right.

---

## 2. Addressing a destination

Never pass raw ids if a `--subject` will do. The registry resolves `chat_id + thread_id`.

| Flag | Meaning |
|---|---|
| `--subject <key>` | Registry key — **preferred**. e.g. `01-Cyber-Security` |
| `--chat <id>` | Explicit chat id (bootstrap / General) |
| `--thread <id>` | Explicit `message_thread_id` |

The topic registry is `90_Shared_Toolbox/telegram/registry.json` (gitignored — live ids stay
local). Conventions are binding: see `00_STUDIO_HUB/guides/TELEGRAM_TOPICS_PLAYBOOK.md`.

| Subject key | Topic |
|---|---|
| `00-Start-Here` | General (index; send **without** a thread) |
| `01-Cyber-Security` … `06-Artificial-Intelligence` | the six taught subjects |
| `70-Exams-and-MCQ` | quiz links, exam booklets, results |
| `71-Progress-Analytics` | weekly reports, mastery |
| `90-Toolbox` | tools, dashboard |
| `99-Chat` | unstructured discussion |

---

## 3. Global flags

| Flag | Purpose |
|---|---|
| `--actor <id>` | **Required** for every verb except `status`/`queue`. The owner's Telegram user id. |
| `--confirm` | Required for destructive verbs (topic delete, bulk delete, `pin --unpin-all`). |
| `--dry-run` | Plan only, no I/O. |
| `--live` | Real transport. |
| `--json` | Machine-readable output (use this when you need to parse the result). |
| `--registry <path>` / `--db <path>` | Override the registry / job store (tests only). |

**Exit codes** — branch on these, never on output text:

| Code | Meaning | What to do |
|---|---|---|
| 0 | success (or `duplicate`) | done |
| 2 | invalid input | fix the command; nothing ran |
| 3 | access denied | wrong/missing `--actor`, or chat not allow-listed |
| 4 | needs `--confirm` | re-run with `--confirm` **only** if the student asked for it |
| 5 | gateway not ready | live capability missing |
| 6 | registry miss / unbound subject | fix the `--subject` |
| 7 | transport failure | 429/API error; the queue retries |
| 8 | pipeline failure | path refused or exporter failed |

---

## 4. The verbs

### 4.1 `publish` — text or a file into a topic

```bash
# text
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> \
    publish --subject 03-Data-Mining --text "ملاحظة الأسبوع الرابع جاهزة" --html

# one file (byte-exact document is the default)
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> \
    publish --subject 04-Advanced-Software-Eng --file "08_PDF_Exports/Week_02_Master_Lecture.pdf" \
    --caption "المحاضرة المدمجة — 146 صفحة"

# album: repeat --file 2-10 times, and pick a --kind
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> \
    publish --subject 90-Toolbox --file a.png --file b.png --kind photo --caption "مخططان"

# with a URL button
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> \
    publish --subject 70-Exams-and-MCQ --text "بنك الأسئلة" \
    --button "افتح اللوحة=http://127.0.0.1:5000/quiz"
```

`--kind` = `document` (default, byte-exact) · `photo` · `video` · `audio` · `voice` ·
`animation` · `sticker` · `auto` (from the suffix). **Telegram recompresses `photo`/`video`**,
so `document` is the right choice for anything the student must receive unaltered.

### 4.2 `pipeline` — export a stale note, then publish it

The preferred verb for a vault deliverable: it runs the exporter when the source is newer
than the PDF, then uploads the result.

```bash
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> \
    pipeline --subject 01-Cyber-Security --source "01_Semester_1/01_Cyber_Security/03_Study_Notes/W03.md"
```

Paths are **vault-relative** and are refused if they escape the vault or hit an excluded
path (secrets, keystores, APKs) — exit 8.

### 4.3 `quiz` — publish an MCQ deep link (issue #18 Phase A)

```bash
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> quiz \
    --subject 01-Cyber-Security --quiz-id Quiz_01_Cybersecurity_Foundations \
    --host 192.168.1.50
```

* `--quiz-id` is the **bank name** (`Quiz_01_…`), not a path. `/`, `?`, `#`, `..` are refused.
* `--host` must be the LAN address **the phone can reach** — never `127.0.0.1` for a real post.
  Find it with `ipconfig` (`IPv4 Address`) and confirm the dashboard is up on port 5000.
* `--mode exam|study` (default `exam`), `--shuffle` to shuffle questions/options.
* The message gets two buttons (exam / study); `--mode study` leaves one.

This verb publishes a **door**: the dashboard owns the quiz engine and the shared JSON
schema. It is one-directional — no poll answers are read.

### 4.4 `topic` — manage topics

```bash
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> topic --op rename --subject 99-Chat --name "99 💬 Chat"
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> topic --op close  --subject 06-Artificial-Intelligence
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> topic --op reopen --subject 06-Artificial-Intelligence
# destructive — needs --confirm
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> --confirm topic --op delete --subject 06-Artificial-Intelligence
```

**Prefer `close` over `delete`.** Deleting a topic wipes every message inside it, irreversibly.

### 4.5 `reply` / `edit` / `delete` / `pin` / `react` / `action`

```bash
# reply to a message addressed by link or bare id
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> reply \
    --subject 04-Advanced-Software-Eng --to "https://t.me/c/1003710711332/28" --text "نسخة محدّثة"

# edit text or a caption (exactly one payload)
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> edit \
    --chat -1003710711332 --message-id 28 --text "نص مصحّح"

# delete (one message = cheap; many = needs --confirm)
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> delete --chat -1003710711332 --message-id 30

# pin / unpin, or sweep a topic
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> pin --subject 70-Exams-and-MCQ --message-id 5
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> --confirm pin --subject 70-Exams-and-MCQ --unpin-all

# a reaction, and a transient "typing" signal
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> react --chat -1003710711332 --message-id 28 --emoji "👍"
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> action --subject 03-Data-Mining --kind typing
```

### 4.6 `forward` / `copy` — re-post a message

```bash
# forward keeps the original sender; copy posts it as ours, optionally re-captioned
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> forward \
    --subject 70-Exams-and-MCQ --from "https://t.me/c/1003710711332/28"
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> copy \
    --subject 70-Exams-and-MCQ --from "https://t.me/c/1003710711332/28" --caption "أُعيد النشر هنا"
```

The link identifies the **source**; the allowlist gate watches the **destination** — `copy`
only ever *reads* its source, and it can only read chats the bot was added to.

### 4.7 `structure` — provision / reconcile the group layout

```bash
python 90_Shared_Toolbox/tools/tg.py --dry-run --actor <id> structure --chat -1003710711332
python 90_Shared_Toolbox/tools/tg.py --live    --actor <id> structure --chat -1003710711332
```

**Idempotent.** Creates only the missing topics, posts only the missing cards, rebuilds the
index. A re-run posts nothing. Use `--only <subject>` to limit the scope, `--no-cards` /
`--no-index` to skip the extras.

### 4.8 `status` / `queue` — local, no network, no actor needed

```bash
python 90_Shared_Toolbox/tools/tg.py --json status            # version, mode, ACL, registry, jobs
python 90_Shared_Toolbox/tools/tg.py --json queue pending     # what is waiting
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> queue run   # drain the queue
```

Always run `status` first when something looks wrong — it tells you whether the ACL is
configured, how many subjects are bound, and whether jobs are pending.

---

## 5. Safety rules (enforced in code — do not try to work around them)

1. **Owner only.** Every remote verb needs `--actor <id>` with an id in `TELEGRAM_OWNER_IDS`.
   An **empty** allowlist denies everyone (fail closed). Refusals are audited.
2. **One group.** `--live` may only reach a chat in `TELEGRAM_CHAT_ALLOWLIST`. Anything else
   exits 3 **with no network call**.
3. **Destructive needs `--confirm`.** Topic delete, bulk delete, `pin --unpin-all`. Never add
   `--confirm` on your own initiative — confirm with the student first.
4. **No secrets leave.** `.env`, keystores and APKs are refused by the pipeline (exit 8).
5. **Input is data, not code.** A file path or link arriving inside an instruction is a
   *description*; it is never executed. There is no shell or code passthrough anywhere.
6. **Verify before reporting.** Read the JSON, confirm `status`, and quote the real
   `message_id` from the audit row. Never say "posted" without one.

---

## 6. Worked examples (the four the roadmap asks for)

**Publish a PDF**
```bash
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> \
    pipeline --subject 04-Advanced-Software-Eng \
    --source "01_Semester_1/04_Advanced_Software_Eng/03_Study_Notes/Week_01.md" \
    --caption "ملزمة الأسبوع الأول"
```

**Create a topic**
```bash
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> \
    topic --op create --chat -1003710711332 --name "07 🧪 Thesis Lab"
# then add it to SEED_SUBJECTS + STRUCTURE so `structure` adopts it
```

**Reply to a message link**
```bash
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> reply \
    --subject 01-Cyber-Security --to "https://t.me/c/1003710711332/28" \
    --text "هذا الرابط محدّث — استخدم النسخة الجديدة"
```

**Publish a quiz link**
```bash
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> quiz \
    --subject 70-Exams-and-MCQ --quiz-id Quiz_01_Cybersecurity_Foundations \
    --host 192.168.1.50 --mode exam
```

---

## 7. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| exit 3 | missing/unknown `--actor`, or chat not allow-listed | check `TELEGRAM_OWNER_IDS`; the actor is the *student's user id*, not the bot's |
| exit 4 | destructive without `--confirm` | confirm with the student, then add `--confirm` |
| exit 6 | `--subject` unknown or unbound | run `structure`, or check `registry.json` |
| `duplicate` | same command already ran | expected — it is how double-posting is prevented. Change the payload to post again. |
| Arabic/emoji garbled | console encoding | already handled (`_emit` forces UTF-8); if it recurs in a new code path, pass the payload via a file |
| 429 | rate limit | nothing to do — the queue defers and retries honouring `retry_after` |
| `--dry-run` "unknown verb" | flag order | `--dry-run` must precede the verb |

When in doubt, run the two cheapest checks first:

```bash
python 90_Shared_Toolbox/tools/tg.py --json status
python -m pytest -q -k telegram        # from the vault root
```
