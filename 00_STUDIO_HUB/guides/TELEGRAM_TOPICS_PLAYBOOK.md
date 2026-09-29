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
   - The Bot API cannot reorder or pin *topics* (those are MTProto-only: `reorderPinnedForumTopics`, `updatePinnedForumTopic`), and
   - Topic-level pinning is capped at ~5 per forum (`topics_pinned_limit`).
2. Emoji prefix is part of the name (visual scanning); it is **fixed at creation** together with the icon colour.
3. Renaming = `tg.py topic --op rename --subject <key> --name "…"` (registry updated automatically by the bound thread id).

## 3. The Extras That Make Topics Self-Describing

Each topic carries a **pinned brief card** — Telegram has no topic-description field, so the pinned message *is* the description: course code, instructor, schedule, vault path, and what belongs there.

**General** carries the **pinned index message**: one message with an inline button per topic linking `https://t.me/c/1003710711332/<thread_id>` (deep link into the topic). Rebuilt idempotently by the `structure` verb — rerunning it posts nothing (verified live: `created: []`, all `duplicate`).

Other extras available on demand: `edit` (correct a published card), `react`, `pin/unpin`, `close` (retire a finished week without losing history).

## 4. Lifecycle Rules

- **Close, don't delete.** `topic --op delete` wipes every message in the topic (irreversible, ADR D7) → always `--confirm`, prefer `--op close`.
- A subject that ends (e.g. `06-Artificial-Intelligence` on hold) stays **created but quiet** — no posts until material exists.
- New subject added to the vault → add a `SEED_SUBJECTS` entry + a `STRUCTURE` entry, then rerun `structure`; only the new topic is created.

## 5. Bot Constraints to Remember

| Constraint | Consequence |
|---|---|
| Bot API has **no list-topics method** | Ids come from `createForumTopic` (auto-bound) or a topic-root message link |
| Icon colour fixed at creation | Choose from the palette in `structure.py`; the gateway retries with the default colour if the API rejects a value |
| ~1 msg/s and ~20 msgs/min per chat | `structure` paces itself and drains its own queue (`store` + `ChatRateLimiter`) |
| Only `manage_topics` admins may create/edit/delete topics | Bot is admin with `can_manage_topics` (verified at bootstrap) |
| Pins here are **message pins**, not topic pins | Available via Bot API (`pinChatMessage`), unlike topic ordering |

## 6. Operating Commands

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

## 7. Sources

- Forum/topic mechanics: <https://core.telegram.org/api/forum> (creation, edit, close, delete, pin/reorder = MTProto; `topics_pinned_limit`; only "General" can be hidden).
- Bot API methods: <https://core.telegram.org/bots/api> (`createForumTopic`, `editForumTopic`, `closeForumTopic`, `reopenForumTopic`, `deleteForumTopic`, `pinChatMessage`, `unpinAllForumTopicMessages`).
- Limits: ~30 msg/s global, ~1 msg/s and ~20 msgs/min per chat; topic icons palette fixed at creation.
