---
name: telegram
description: "Master Studio Telegram Gateway driver. Publishes study notes, PDFs, quiz links and reports into the group's Arabic forum topics; manages topics, replies, edits, pins and reactions — all through one outbound-only CLI the agent runs in the background (Zero-CLI for the student)."
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
| `01-Cyber-Security` … `06-Artificial-Intelligence` | the six taught subjects (`◆ <name>`) |
| `70-Exams-and-MCQ`, `71-Progress-Analytics`, `90-Toolbox` | **unbound** — their utility topics were deleted 2026-10-02; an old command resolves to a clear *unbound*, never to a silent success |

Titles carry **no numbers and no emoji** — only the Arabic name behind the monochrome
`◆` marker. General has no registry key: it is the chat room
(`محادثة`, topic id 1, never provisioned), so send to it with `--chat` and **no thread**.

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
    publish --subject 03-Data-Mining --file a.png --file b.png --kind photo --caption "مخططان"

# with a URL button
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> quiz \
    --subject 01-Cyber-Security --quiz-id Quiz_01_Cybersecurity_Foundations \
    --host 192.168.1.50
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
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> topic --op rename --subject 01-Cyber-Security --name "◆ أمن المعلومات"
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

# repoint a text message's inline keyboard. Text-only (editMessageCaption has no
# keyboard) and the one route for a message older than 48h: deletion is refused
# then, editing is not.
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> edit \
    --chat -1003710711332 --message-id 26 --text "Master Studio — فهرس الكروب" \
    --button "◆ أمن المعلومات=https://t.me/c/3710711332/84"

# delete (one message = cheap; many = needs --confirm)
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> delete --chat -1003710711332 --message-id 30

# pin / unpin, or sweep a topic
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> pin --subject 03-Data-Mining --message-id 190
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> --confirm pin --subject 03-Data-Mining --unpin-all

# a reaction, and a transient "typing" signal
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> react --chat -1003710711332 --message-id 28 --emoji "👍"
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> action --subject 03-Data-Mining --kind typing
```

### 4.6 `forward` / `copy` — re-post a message

```bash
# forward keeps the original sender; copy posts it as ours, optionally re-captioned
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> forward \
    --subject 03-Data-Mining --from "https://t.me/c/1003710711332/28"
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> copy \
    --subject 03-Data-Mining --from "https://t.me/c/1003710711332/28" --caption "أُعيد النشر هنا"
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

### 4.9 `interactive` — one bounded listening session (D15)

**This is the only verb that reads the group.** Everything above is outbound; `interactive`
opens a *window*, handles whatever is aimed at the bot inside it, and closes itself. There is
no daemon and no permanent `getUpdates` loop — that is the whole point of **D15**: reply on
demand, not 24/7.

```bash
python 90_Shared_Toolbox/tools/tg.py --live interactive --for 30 --max 5
python 90_Shared_Toolbox/tools/tg.py --json --live interactive --for 120 --max 20 --subject 04-Advanced-Software-Eng
python 90_Shared_Toolbox/tools/tg.py --live interactive --bot-username cs_mscbot
```

**The bounds are hard, not hints.** `--for <seconds>` (default `60`) and `--max <n>` (default
`20`) are limits the session *stops* on, whichever comes first — an open-ended listener is
exactly what this layer exists to avoid. `--bot-username` defaults to `TELEGRAM_BOT_USERNAME`
from `.env`; it is what mentions are matched against. `--subject` steers answers toward one
registry topic. **No `--actor` is required**: the session gates on the chat allowlist and the
owner list instead of on the caller.

**It fails closed on every axis, before any network call:**

| You get | Why | Fix |
|---|---|---|
| exit `5` | live-only capability — `--live` is missing | add `--live` |
| exit `3` | `TELEGRAM_CHAT_ALLOWLIST` empty or absent | configure it; never work around it |
| exit `2` | `--for` or `--max` is ≤ 0 | pick a real window |

**Where the state lives (D14).** The gateway owns its own folder,
`00_STUDIO_HUB/telegram/`:

| Path | Holds | Written by |
|---|---|---|
| `STATE.md` | the processed `update_id` watermark plus `last_listen` / `last_post` | **gateway only** |
| `TELEGRAM_MEMORY.md` | durable facts the gateway noticed | gateway |
| `log/YYYY-MM-DD.md` | one line per session, append-only | gateway |
| `pending_approval.json` | administrative requests waiting on the student | gateway — **never auto-run** |

The watermark is why a message is never handled twice and never dropped between sessions.
The gateway may write **its own folder and nothing else**: it reads `MEMORY.md` for context
but **never writes `MEMORY.md`** — the agent stays the only intermediary between the two.

**D16 — approvals do not execute themselves.** Any administrative action requested from a
chat lands in `pending_approval.json` as a *pending approval*. Surface it to the student and
act only on his explicit yes; the owner allowlist and `--confirm` still apply on top.

### 4.10 `bridge` — one Pull poll, proposals only (never sends)

The user talks to the agent **through the bot**. The agent is usually asleep on
Windows, so pending messages wait in Telegram until it polls — Pull, not Push:
one `getUpdates` call, bounded by `--limit` (default `20`, max `100`), then it
stops. Nothing is executed and nothing is sent; every addressed mention becomes
a **proposal** the agent (or you) dispositions afterwards.

```bash
python 90_Shared_Toolbox/tools/tg.py --live bridge --limit 20
python 90_Shared_Toolbox/tools/tg.py --json --live bridge --limit 50 --bot-username cs_mscbot
```

| Mention from | Becomes | Meaning |
|---|---|---|
| owner + `/publish` / `/edit` / `/quiz` / `/reply` / `/react` | `urgent` | run it now (still needs `--actor`, still audited) |
| owner + `/delete` / `/pin` / admin command | `restricted` | send the included approval card to the private chat first |
| owner + plain text | `note` | the agent reads it later — no action attached |
| non-owner (any text) | `denied` | audited, never executed |

**Urgent vs. restricted** lives in `telegram/permissions.py`: `topic`,
`delete`, `pin` and `structure` are always restricted, anything
`Action.destructive()` reports is restricted, everything else from an owner is
urgent. A restricted proposal carries its approval card
(`format_approval_request`); the owner replies `نعم` / `yes` to run it (with
`--confirm`) or `لا` / `no` to drop it — anything else keeps it pending
(`parse_approval_reply`). The processed `update_id` watermark is read from and
written back to the gateway memory (`STATE.md` → `update_offset`), so a message
is never proposed twice — including denied ones.

Same fail-closed gates as `interactive`: live-only (exit `5` without `--live`),
empty allowlist refuses before any network call (exit `3`), `--limit` outside
`1..100` is exit `2`.

### 4.11 `human` — the spare account (issue #22, MTProto)

**A different animal from everything above.** `transport.py` speaks the Bot API; this speaks
**MTProto as a person** through Telethon. Telegram forgives a clumsy bot with a `FloodWait`,
but restricts a clumsy *user* account — so this verb brings its own gates and is **off until
you switch it on**.

```bash
# identity and discovery
python 90_Shared_Toolbox/tools/tg.py --live human --verb whoami
python 90_Shared_Toolbox/tools/tg.py --live human --verb chats

# inside the allowed group only — TELEGRAM_CHAT_ALLOWLIST applies unchanged
python 90_Shared_Toolbox/tools/tg.py --live human --verb read --chat -1003710711332 --limit 10
python 90_Shared_Toolbox/tools/tg.py --live human --verb say --chat -1003710711332 --text "أهلاً"

# the same say, but inside a subject topic instead of the general one
python 90_Shared_Toolbox/tools/tg.py --live human --verb say --chat -1003710711332 --thread 12 --text "سؤال سريع"

# publish a FILE as the spare account (the file publisher): --filename is the
# display name Telegram shows — a chapter sent as dm_ch1.pdf reads as scaffolding
python 90_Shared_Toolbox/tools/tg.py --live human --verb sendfile \
    --chat -1003710711332 --thread 86 \
    --file "C:\path\dm_ch1.pdf" \
    --filename "تنقيب البيانات - الجابتر الاول.pdf" \
    --text "الفهرس : <a href='https://t.me/c/3710711332/181'>كتالوج المادة</a>"

# rewrite a message the spare account OWNS, in place — the pinned catalog card
# is the case that matters: Telegram refuses an edit by anyone but its sender,
# so a card the spare posted can only ever be corrected by the spare
python 90_Shared_Toolbox/tools/tg.py --live human --verb edit \
    --chat -1003710711332 --message-id 190 \
    --text "<b>الفهرس المحدّث</b>"

# two-step login: request the code, then spend it
python 90_Shared_Toolbox/tools/tg.py --live human --verb login --phone +9647XXXXXXXXX
python 90_Shared_Toolbox/tools/tg.py --live human --verb login --phone +9647XXXXXXXXX --code 12345

# ...and only if Telegram answers with a two-step challenge
python 90_Shared_Toolbox/tools/tg.py --live human --verb login --phone +9647XXXXXXXXX --password <2FA>
```

**Two-step verification (2FA).** If the account has it on — and a spare account should — the
code step answers with `SessionPasswordNeededError`, which means *the code already succeeded
and only the password remains*. Re-run the same `login` with `--password` and **without**
`--code`: Telethon resolves `sign_in` as an `if/elif` chain (`phone and not code and not
password` → send a code, `elif code` → verify the code, `elif password` → check the password),
so handing it both would silently take the *code* branch, ignore the password and re-raise the
identical error. A refused sign-in keeps the pending login intact, so a mistyped password never
costs you a fresh code. **`--password` is one-time: never write it to `.env`, to a file, or to
the session journal.**

`--verb` is one of `whoami`, `chats`, `read`, `say`, `sendfile`, `edit`, `login`. `read` needs `--chat`
**and** `--limit` (default `10`); `say` needs `--chat` **and** `--text`; `edit` needs `--chat`,
`--message-id` **and** `--text` (the replacement body, HTML — the pinned card is a document, so an
in-place update must render the same markup it shipped with); `sendfile` needs
`--chat` **and** `--file` (an existing path) and takes `--filename` (the display name) and
`--text` (the caption); `login` needs `--phone`, and `--code` on the second step. Both `say`
and `sendfile` also take `--thread <topic id>`, which posts into that forum topic; omit it and
the message goes to the general topic as before. `--thread` is refused for every other verb and
for a non-positive id — a `--thread` that quietly did nothing would leave you believing a reply
landed inside a topic while it came out under the wrong header. The chat
must be on `TELEGRAM_CHAT_ALLOWLIST` — **a human account
is not an ACL bypass**: an empty allowlist denies every chat, exactly as it does for the bot.

**The kill switch.** Human mode is **off by default**. Set `TELEGRAM_HUMAN_ENABLED=1` in
`.env` to enable it; set it back to `0` (or delete the line) to stop everything at once. Only
the literal values `1` / `true` / `yes` / `on` count as on — an absent variable, `0`, `false`
and any typo all mean **off**, because a kill switch that a typo can enable is not one.

**Flood control, in two layers — neither sleeps and neither retries.**

* *Local pacing*, before Telegram is ever asked: at most 20 messages/minute and at least 1s
  apart in one chat. A refused send never reaches the network. The send stamps are persisted to
  `00_STUDIO_HUB/telegram/pacing.json` — without that the limiter would be rebuilt empty on
  every invocation and the ceiling would block nothing at all, since the CLI is one verb per
  process. Only `say` and `sendfile` spend the budget; `read` and `edit` gate on the allowlist but
  never consume slots — otherwise refreshing a card could silence a real send.
* *Server-side*, a `FloodWait` is surfaced as a `retry_after` number and that is the end of
  it. Telethon is built with `flood_sleep_threshold=0` because its default of 60 would make it
  **silently block inside our own call** instead of letting us report the wait; it is never
  retried. `receive_updates=False` keeps the update listener that **D15** forbids from ever
  being installed.

**Monitoring.** Every attempt — allowed or refused — writes one audit row to the gateway's own
`audit` table, namespaced `human:<verb>` so a person-shaped account's actions can never be
mistaken for the bot's (`read` / `say` are schema verbs; `human:read` / `human:say` are not).
The `result` column uses the same vocabulary as the executor's rows: `ok` for identity, read and
edit verbs, `sent` for a message that Telegram accepted, `denied` for the allowlist, `rate_limited`
for local pacing, `error` for a transport refusal and `refused` for the kill switch or a missing
`--live`. `detail` carries the reason, and for `say` the **text actually spoken** plus its
`message_id` — the one field an audit must never lose, because "did the account say anything,
and what?" has to be answerable after the fact. An `edit` records the same pair with the **new**
body, since Telegram keeps no visible history and the ledger is the only record of what the card
said before the next edit overwrote it. The write is deliberately **not** wrapped in a
`try/except`, exactly like every `store.audit(...)` call in `executor.py`: a ledger that fails
must surface loudly rather than let work pass unmonitored, which is what would defeat AC 2's
monitoring leg in the first place.

**Exit codes** follow the shared table in §1: `5` = disabled, missing `--live`, missing
credentials or no session yet; `3` = chat not allowlisted; `2` = malformed request;
`7` = local pacing or `FloodWait`.

**A `*.session` file is a bearer token.** It holds the authorization key — full control of the
account with **no password and no 2FA**. It is written under `90_Shared_Toolbox/telegram/`, and
both `*.session` and `*.session-journal` are gitignored, because this repository is public;
never move one into tracked space. The single-use login hand-off
(`00_STUDIO_HUB/telegram/login_state.json`, which carries the code hash Telethon keeps only in
memory) is deleted the moment the code is spent.

---

### 4.11 `tg_catalog` — the subject catalog card (one message per subject)

A subject is **one message**, not one message per asset: a **document plus a
caption**, and it is deliberately *the first message of its topic*. Today the
document is a one-page placeholder PDF; when the merged official lectures
land it is the merged file itself. The caption is the index.

Three speeds, exactly as in the bachelor channels: the catalogue is small and
revisable, the warehouse is huge and untouched, the meta block is dated.

**The source of truth is a file, not the message.**
`00_STUDIO_HUB/telegram/catalog/<subject>.json` is what you merge into. So the
whole of "ضيفها" when new material lands is: add the chapter (the next
message id in `chapters`) and bump `updated` there, then re-push. Never
hand-edit the Telegram message instead — the file and the card would then
disagree with no way to tell which one is right.

```bash
python 90_Shared_Toolbox/tools/tg_catalog.py --list
python 90_Shared_Toolbox/tools/tg_catalog.py --print 01-Cyber-Security
python 90_Shared_Toolbox/tools/tg_catalog.py --push 01-Cyber-Security --dry-run
python 90_Shared_Toolbox/tools/tg_catalog.py --push-all --live
```

`--push` is repeatable and `--push-all` walks every material subject, sleeping
between them so the pacing ceiling is respected. **A push is a dry run unless
`--live` is given** — there is no way to reach the network by forgetting a
flag. The actor is derived from `TELEGRAM_OWNER_IDS` (override with
`--actor`); without one the ACL answers `denied`, because every non-local verb
needs a named driver.

**Publish or edit is chosen by the file, not by a flag.** While
`catalog_message_id` is `null` the card does not exist yet and the tool runs
`publish --file … --caption …`; once the id is recorded it runs `edit
--message-id … --caption …`. Recording that id is the step that makes the next
"ضيفها" an in-place edit rather than a second copy dropped at the bottom of
the topic — which would break "the first message is the catalog".

**Sources are recorded, not rendered.** The canonical textbooks posted into a
topic are listed in the same JSON under `references`
(`[{"message_id": …, "source": …, "edition": …}]`), copied verbatim from the
caption that shipped (`مصدر مادة` / `الطبعة`). The field is a *validated*
ledger — a half-filled entry is refused — and it stays out of the card on
purpose: the card is a caption capped at 1024 characters and already carries
the chapters, while the sources live in the topic as their own posts.

**A chapter is a lecture file, not a calendar week.** Soft Computing's W02
spanned two weeks on the timetable but is one lecture in one file, so it is one
chapter. Never re-derive the list from dates.

**Placeholder chapter ids sit far above live traffic** (`100001` and up), not at
the next free message id. The first push's own cards consume the low range, and
a placeholder must never resolve to a real, unrelated message. They are replaced
by the real lecture message ids when the files land.

**The caption carries the doctor's rank as the university writes it.**
`أ.م.د.` (assistant professor) and `أ.د.` (full professor) come from
`01_Semester_1/Weekly Schedule.docx` — transcribed there, never from memory,
because dropping the rank misstates the course. Four subjects are ا.م.د and
two are ا.د.

**The idempotency key hashes the payload**, so re-pushing an unchanged card
answers `duplicate` — nothing is posted twice — while a changed card is a real
`editMessageCaption`. The builder refuses a caption over Telegram's
**1024-character** caption limit or carrying unbalanced tags, rather than
shipping one Telegram would truncate: a caption is capped far below the 4096
text limit, and the card is a caption.

**Verify live, not only with the suite.** `tools/tg_verify.py --live` is the
permanent form of that check: it reads topics 84–89 over MTProto and prints
`ALL CHECKS PASSED` or the failing labels. It asserts the card is still the
*first* message of its topic (a re-push that published instead of editing would
leave a copy at the bottom) and is pinned, that the link entities point at the
ids you meant, that every chapter and source post exists, and that every
display filename is within the 62-byte budget. It is strictly read-only, exits
`1` on any failure, and refuses without `--live`.

One naming trap worth knowing: the **bot's** `edit` takes exactly one of
`--text` and `--caption`, with `--html` to parse markup — the card is media, so
it must be `--caption`, and `editMessageText` aimed at a document fails. Under
the current model an in-place card refresh is done by the **spare** account
instead (`human --verb edit --message-id … --text …`), because a message can
only be edited by its own sender.

Placeholder PDFs live under `00_STUDIO_HUB/telegram/catalog/placeholders/`,
one blank A4 page each, named after the subject key. They are replaced — not
augmented — when the real merged file arrives.

---

## 5. Persona — how the bot behaves (issue #17)


The bot is an **official bot**, but it does not behave like a firehose. The gateway applies
these defaults automatically; you do not pass flags for them.

| Behaviour | Rule |
|---|---|
| **Presence first** | A `typing` bubble precedes any text ≥ 120 chars; `upload_document` precedes any upload. Short one-liners get none — nobody types a single line for a second first. |
| **Human pacing** | Batch items are separated by a short, *unequal* delay (0.8–2.6 s). It is deterministic, not random, so an audit log is reproducible and the suite is never flaky. |
| **Reply in context** | Use `--reply-to <id>` to anchor a post to what it answers, instead of broadcasting into a topic. |
| **Edit, don't re-post** | To correct something, `edit --message-id <id>` — do not publish a second message saying "تصحيح". |
| **Live only** | Pacing and presence apply to `--live` sends **only**. `--dry-run` and the mock path stay instantaneous. |

### The tone (Iraqi, as the student writes)

> **ودّي ومباشر، بلا حشو وبلا مجاملة زايدة. يكتب بالعراقي الطبيعي، ويخلّي المصطلح التقني بالإنجليزي.**

Practical reading of that:

- Plain Iraqi Arabic for the message body — the way he actually talks, not MSA.
- **Technical terms stay in English** (`fuzzy relations`, `risk assessment`) — never transliterate.
- No filler openers ("بكل سرور"، "سؤال ممتاز"). Get to the point.
- Corrections are stated plainly: "هاي غلط، الصحيح…" — not softened.
- **No emoji, anywhere** — not in a body, a heading or a topic title. Use a single-colour
  symbol instead (`◆`, `●`); plain text must stay comfortable to read.

The persona is defined in `90_Shared_Toolbox/telegram/persona.py` (`PERSONA`), which is the
**single source** for pacing, thresholds and tone — the skill and the code cannot disagree.

## 6. Safety rules (enforced in code — do not try to work around them)

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

## 7. Worked examples (the four the roadmap asks for)

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
    topic --op create --chat -1003710711332 --name "◆ مختبر الرسائل"
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
    --subject 01-Cyber-Security --quiz-id Quiz_01_Cybersecurity_Foundations \
    --host 192.168.1.50 --mode exam
```

---

## 8. Troubleshooting

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
