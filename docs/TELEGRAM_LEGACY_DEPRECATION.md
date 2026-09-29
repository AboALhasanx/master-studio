# Retiring Playwright/CDP Telegram Automation (issue #20)

> **Status:** DEPRECATION NOTICE — the scripts listed below still exist and still work, but
> they are **superseded**. This document is the migration mapping required by issue #20.
> **Behavioural change: none.** Nothing was deleted and nothing was edited in place.
> Actual removal is a separate follow-up PR (see §5).

---

## 1. Why these scripts are being retired

They drive a **debug Chromium over CDP** (`http://127.0.0.1:9222`) against
`https://web.telegram.org/a/`. That approach is fragile by construction:

| Problem | Consequence |
|---|---|
| Selector-based UI automation | Any Telegram web redesign breaks every script silently |
| Needs a **logged-in browser session at all times** | Cannot run headless or on a schedule; the human must keep a window open |
| Duplicates the official API | Same job, more failure modes |
| No ACL, no audit, no idempotency | A mis-click can post twice, to the wrong place, with nobody able to reconstruct why |

The **gateway** (`90_Shared_Toolbox/telegram/` + `tools/tg.py`) replaces all of it through the
official Bot API: outbound-only, fail-closed allowlist, `--confirm` on destructive verbs,
SQLite-backed idempotency and a full audit log.

## 2. The scripts being retired

All under `90_Shared_Toolbox/tools/`:

| Script | Size | What it did |
|---|---|---|
| `telegram_publisher.py` | 1.9 KB | CDP connect + login check; held the legacy `TOPICS` list |
| `telegram_chrome.bat` | 408 B | Launched the debug Chromium with `--remote-debugging-port=9222` |
| `tg_probe.py` / `tg_probe2.py` / `tg_probe3.py` | ~1 KB each | Scraped the DOM to discover what the web client exposed |
| `tg_create_click.py` | 1.2 KB | Clicked through "create topic" in the UI |
| `tg_fill_name.py` | 827 B | Typed a topic name into the UI |
| `tg_state.py` / `tg_state2.py` | ~1 KB each | Dumped UI state to understand the topic model |

Also superseded: the `.tg-profile/` Chromium profile directory next to them.

## 3. Migration mapping — old script → gateway command

### 3.1 Launch / connect / login

| Old | New |
|---|---|
| `telegram_chrome.bat` (start debug Chromium) | not needed — no browser at all |
| `telegram_publisher.py status` → `LOGGED_IN` / `NEED_LOGIN` | `python 90_Shared_Toolbox/tools/tg.py --json status` |
| `telegram_publisher.py open` (park a session open for an hour) | not needed — each command is a short-lived call |

### 3.2 Discovery

| Old | New |
|---|---|
| `tg_probe*.py` (scrape the DOM for what exists) | `tg.py --json structure --chat <id>` (dry-run reveals the plan) · `registry.json` holds the bound `thread_id`s |
| `tg_state*.py` (dump the topic list) | `tg.py --json status` → `registry: {subjects, bound}`; the layout itself is `STRUCTURE` in `structure.py` |

### 3.3 Topic management

| Old | New |
|---|---|
| `tg_create_click.py` (click "create topic") | `tg.py --live --actor <id> topic --op create --chat <id> --name "NN 🧩 Name"` |
| `tg_fill_name.py` (type the name) | the `--name` flag on the same command |
| → provisioning the whole layout by hand | `tg.py --live --actor <id> structure --chat <id>` — **idempotent**, creates only what is missing |
| (no old equivalent) rename / close / reopen | `topic --op rename\|close\|reopen --subject <key> …` |
| (no old equivalent) delete | `topic --op delete --subject <key> --confirm` |

### 3.4 Publishing

| Old | New |
|---|---|
| (manual posting in the web client) | `tg.py --live --actor <id> publish --subject <key> --text "…"` |
| (manual file upload) | `publish --subject <key> --file <path> [--caption …] [--kind …]` |
| (manual, multi-step) a note → PDF → upload | `pipeline --subject <key> --source <vault-relative .md>` |
| (manual) share a quiz link | `quiz --subject <key> --quiz-id <bank> --host <lan-ip>` |

### 3.5 The legacy `TOPICS` list

`telegram_publisher.py` carried a 9-entry `TOPICS` list. It has been **harvested** into the
gateway, which is the point of keeping the file until now:

| Legacy `TOPICS` entry | Now lives in |
|---|---|
| all 9 keys (`00-Start-Here`, `01`…`06`, `90-Toolbox`, `99-Chat`) | `registry.SEED_SUBJECTS` (committed source) — **verified: 0 missing** |
| the descriptions ("CS501 FINALs." …) | `structure.py` `STRUCTURE` brief cards (enriched: instructor, schedule, vault path) |

One nuance worth recording: `00-Start-Here` is seeded in the registry but is **not** a
`STRUCTURE` topic, because it *is* the group's **General** — it has no `thread_id` to create.
So the gateway provisioned **10 topics from 11 seeded subjects**, which is the expected mapping,
not a gap.

The gateway's layout is otherwise a **superset**: it added `70-Exams-and-MCQ` and
`71-Progress-Analytics` and gave every topic a pinned card + a pinned index. Source of truth:
`90_Shared_Toolbox/telegram/registry.json`, conventions in
`00_STUDIO_HUB/guides/TELEGRAM_TOPICS_PLAYBOOK.md`.

## 4. What NOT to migrate

Nothing in these scripts is unique logic worth porting. They contain **no business rules** —
only selectors and clicks. The one asset (the topic list) is already harvested (§3.5).

## 5. Follow-up PR (the actual removal)

Deferred to gate **G7** and tracked as a separate, isolated, revertible PR:

1. `git rm` the nine scripts, `telegram_chrome.bat`, and the `.tg-profile/` directory.
2. Delete `telegram_publisher.py`'s `TOPICS`/`GROUP_NAME` only after confirming
   `SEED_SUBJECTS` + `STRUCTURE` cover every entry (already true as of 2026-09-29).
3. Update `AGENTS.md` if it still names any of the scripts.
4. Re-run `pytest -q` (the gateway suite must stay green — it never imports these files).

**Until that PR merges, the scripts remain exactly as they are.** This issue changes
documentation only.

---

**Sources for the Bot API claims:** <https://core.telegram.org/bots/api>.
**Gateway entry point:** `python 90_Shared_Toolbox/tools/tg.py` (see `.mimocode/skills/telegram/SKILL.md`).
