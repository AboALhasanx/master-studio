# Telegram Topics Playbook — Master-Studio FINAL (issue #19)

> **Status:** ACTIVE — structure provisioned live on **2026-09-28** by the gateway (`structure` verb), 10/10 topics created, 0 failures.
> **Group:** `Master-Studio FINAL` → `chat_id -1003710711332` (forum enabled).
> **Authority:** conventions here are binding for the gateway (`telegram/structure.py`), the registry, and every agent publishing into the group.

**TL;DR (عربي):** التوبيكات مرقّمة لتقرأ بالترتيب، كل توبيك بكارت مثبّت يوصفه (لأن تيليجرام ما عنده حقل وصف)، والترتيب يصير بالأرقام لأن Bot API ما يعيد ترتيب التوبيكات. الفهرس العام مثبّت بأزرار تودّي لكل توبيك.

---

## 1. The Layout (provisioned)

| # | Topic (as shown) | Registry key | thread_id | Purpose |
|---|---|---|---|---|
| — | **General** (index) | `00-Start-Here` | *(none — send without thread)* | Rules, pinned **index message** with buttons |
| 01 | 🛡 Cyber Security | `01-Cyber-Security` | 6 | CS501 · Dr. Huda · Sun 08:30 |
| 02 | 🗣 English Language | `02-English-Language` | 8 | CS502 · Dr. Haidar · Sun 10:30 |
| 03 | ⛏ Data Mining | `03-Data-Mining` | 10 | Dr. Ahmed · Mon 08:30 |
| 04 | ⚙️ Software Engineering | `04-Advanced-Software-Eng` | 12 | CS504 · Dr. Ali Fahim · Mon 10:30 |
| 05 | 🧠 Soft Computing | `05-Soft-Computing` | 14 | Dr. Abdul Hadi · Tue 08:30 |
| 06 | 🤖 Artificial Intelligence | `06-Artificial-Intelligence` | 16 | Dr. Saif · Tue 10:30 (on hold — no material) |
| 70 | 📚 Exams & MCQ | `70-Exams-and-MCQ` | 18 | Quiz links, exam booklets, results |
| 71 | 📊 Progress & Analytics | `71-Progress-Analytics` | 20 | Weekly reports, mastery, review queue |
| 90 | 🧰 Toolbox | `90-Toolbox` | 22 | Tools, exporters, dashboard |
| 99 | 💬 Chat | `99-Chat` | 24 | Unstructured discussion |

Source of truth: `90_Shared_Toolbox/telegram/registry.json`. **Never address a topic by name in code — always by `subject` key**, and let the registry resolve `chat_id + thread_id`.

## 2. Naming & Ordering Rules

1. **Numbered names** (`01 … 99`): `01–06` = taught subjects in schedule order, `70–71` = cross-cutting academic, `90/99` = infrastructure. Ordering is expressed **in the name** because:
   - The Bot API cannot reorder or pin *topics* at all — those live only in MTProto (`messages.reorderPinnedForumTopics`, `messages.updatePinnedForumTopic`), and
   - Topic-level pinning is capped at `topics_pinned_limit` (a server value from the client config; ~5 in practice), so only the index and the live subjects could ever be pinned.
2. Emoji prefix is part of the name (visual scanning); it is **fixed at creation** together with the icon colour.
3. Renaming = `tg.py topic --op rename --subject <key> --name "…"` (registry updated automatically by the bound thread id).

**The naming scheme is the same one the gateway enforces.** `structure.py` owns the canonical
`subject` → `name` pairs, `registry.json` stores the resulting `thread_id`, and the topic
manager (`topic --op …`) addresses topics by the **same `subject` key** — never by name. That
single key is what keeps the playbook, the registry and the CLI in agreement (issue #19 AC3).

## 3. The Extras That Make Topics Self-Describing

Each topic carries a **pinned brief card** — Telegram has no topic-description field, so the pinned message *is* the description: course code, instructor, schedule, vault path, and what belongs there.

**General** carries the **pinned index message**: one message with an inline button per topic linking `https://t.me/c/1003710711332/<thread_id>` (deep link into the topic). Rebuilt idempotently by the `structure` verb — rerunning it posts nothing (verified live: `created: []`, all `duplicate`).

Other extras available on demand: `edit` (correct a published card), `react`, `pin/unpin`, `close` (retire a finished week without losing history).

## 4. Bot Constraints to Remember

| Constraint | Consequence |
|---|---|
| Bot API has **no list-topics method** | Ids come from `createForumTopic` (auto-bound) or a topic-root message link |
| A forum is intended to hold a large number of topics, but **pinning is capped by `topics_pinned_limit`** | Only the General index + the currently-active subjects are worth pinning; the rest are found by number, not by pin |
| Reordering pinned topics, pinning a *topic*, and hiding **General** are **MTProto-only** (`messages.reorderPinnedForumTopics`, `messages.updatePinnedForumTopic`) | The Bot API has **no** topic-pin/reorder method at all → ordering must live in the **name** (see §2) |
| `General` (`id=1`) is the **only** hideable topic, and the only one that cannot be deleted (`messages.deleteTopicHistory` refuses it) | Never plan a layout that depends on hiding a numbered topic |
| Icon colour fixed at creation | Choose from the palette in `structure.py`; the gateway retries with the default colour if the API rejects a value |
| Custom-emoji topic icons need Premium | Non-Premium is limited to the default topic-icon pack; the emoji *in the name* (§2.2) is the portable alternative |
| ~1 msg/s and ~20 msgs/min per chat (≈30 msg/s globally) | `structure` paces itself and drains its own queue (`store` + `ChatRateLimiter`) |
| Only `manage_topics` admins may create/edit/delete topics | Bot is admin with `can_manage_topics` (verified at bootstrap) |
| Pins here are **message pins**, not topic pins | Available via Bot API (`pinChatMessage`, `unpinAllForumTopicMessages`), unlike topic ordering |

## 5. Reading UX — how the group is meant to be *read*

The point of the numbered layout is that a phone screen shows it in a stable order. A few
member-side settings make that work; none of them are Bot-API operations, so they are
documentation for the human, not for the gateway.

- **Per-topic notification control.** Every topic carries its own mute/unmute. The intended
  default is: **mute the group globally**, then unmute only the subject topics that are live
  this week (`01`–`05`) and `70-Exams-and-MCQ` — so an exam link never gets buried under Chat.
- **"View as messages" (chat-style) layout.** The mobile clients offer a tab view and a
  single-stream "View as messages" view. The tab view is the default recommendation: it maps
  1:1 onto the numbered topics, and `99-Chat` stays visually last.
- **Unread badges.** Each topic shows its own unread count, which is why the index message
  carries a button per topic — one tap goes straight to whatever is new, instead of scrolling
  General.
- **Close ≠ mute.** A closed topic stays readable and searchable but stops accepting messages
  (§6). That is the right end-state for a finished week: history preserved, no new noise.
- **Why not one channel per subject.** A forum group keeps every subject in **one** chat id,
  so the registry stays a single lookup and the bot needs no per-channel membership.

## 6. Lifecycle Rules

- **Close, don't delete.** `topic --op delete` wipes every message in the topic (irreversible, ADR D7) → always `--confirm`, prefer `--op close`.
- A subject that ends (e.g. `06-Artificial-Intelligence` on hold) stays **created but quiet** — no posts until material exists.
- New subject added to the vault → add a `SEED_SUBJECTS` entry + a `STRUCTURE` entry, then rerun `structure`; only the new topic is created.

## 7. Operating Commands

```bash
# preview the layout plan (no network)
python 90_Shared_Toolbox/tools/tg.py --dry-run --actor <id> structure --chat -1003710711332

# provision / reconcile (idempotent; only missing topics are created)
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> structure --chat -1003710711332

# publish into a subject topic by name (registry resolves the thread id)
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> publish --subject 03-Data-Mining --text "…"

# publish an MCQ link into a subject topic (issue #18 Phase A)
#   --host is the LAN address the PHONE can reach, not the agent's machine
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> quiz \
    --subject 01-Cyber-Security --quiz-id Quiz_01_Cybersecurity_Foundations \
    --host 192.168.1.50

# topic lifecycle
python 90_Shared_Toolbox/tools/tg.py --live --actor <id> topic --op close --subject 06-Artificial-Intelligence
```

**Quiz links (`quiz` verb).** `--quiz-id` is the *bank name* (`Quiz_01_…`), and the gateway
translates the registry key into the vault folder (`01-Cyber-Security` → `01_Cyber_Security`)
when it composes the URL — never hand-write the folder form. The message carries two buttons
(exam / study); `--mode study` leaves just one. A bank name containing `/`, `?`, `#` or `..`
is refused at schema time, because a broken link is only discovered by the student *after*
they tap it. This verb adds no quiz engine: the dashboard owns `/quiz/...` and the shared
JSON schema, and an AST test in the gateway suite enforces that permanently (issue #18 AC2).

## 8. Sources

Every constraint above traces to Telegram's own documentation — no third-party blogs.

| Claim in this playbook | Official source |
|---|---|
| Forum/topic model; **reorder, pin-a-topic and hide-General are MTProto-only** (`messages.reorderPinnedForumTopics`, `messages.updatePinnedForumTopic`); `topics_pinned_limit` is a **client-config** value (no fixed number in the docs); `General` is the only hideable — and undeletable — topic | <https://core.telegram.org/api/forum> |
| `createForumTopic`, `editForumTopic`, `closeForumTopic`, `reopenForumTopic`, `deleteForumTopic`, `unpinAllForumTopicMessages` all exist; **no topic-pin or topic-reorder method exists** in the Bot API | <https://core.telegram.org/bots/api> (verified against the live page, 2026-09-29) |
| `pinChatMessage`, `unpinChatMessage` (message pins, not topic pins) | <https://core.telegram.org/bots/api#pinchatmessage> · <https://core.telegram.org/bots/api#unpinchatmessage> |
| `message_thread_id` addresses a topic on every send | <https://core.telegram.org/bots/api#message> (`message_thread_id`) |
| Topic icon palette + custom-emoji icons | <https://core.telegram.org/bots/api#getforumtopiciconstickers> · <https://core.telegram.org/api/forum#custom-emoji-topic-icons> |
| Rate limits (~30 msg/s global, ~1 msg/s and ~20/min per chat) | <https://core.telegram.org/bots/faq#my-bot-is-hitting-limits-how-do-i-avoid-this> |
| Per-topic mute/unread, "View as messages", tab layout (client behaviour) | <https://telegram.org/blog/topics-in-groups-collectible-usernames> |

> **Correction recorded (2026-09-29).** An earlier draft cited `toggleForumTopicPinned` as an
> MTProto method. No such method exists — the real names are `messages.updatePinnedForumTopic`
> (method) and `updatePinnedForumTopic` (the *update* it fires). Caught while checking the
> anchors for this issue; fixed here rather than left as a plausible-looking fabrication.

Deviations from the roadmap's original layout table (which named a separate `moderation.py`
and `gateway.py`) are recorded as ADR **D9/D11** in `00_STUDIO_HUB/proposals/FEATURE_TELEGRAM_GATEWAY_ROADMAP.md`.
