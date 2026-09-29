# Feature Proposal: Master Studio Telegram Gateway (Bot-First, Outbound-Only)

> **Status:** G0 → G4 COMPLETE — **every code issue is now closed (#8–#21), and the Epic [#7](https://github.com/AboALhasanx/master-studio/issues/7) is closed too.** **G3** closed #11–#14 and #18; **G4** closed #15 (the telegram skill), #16 (allowlist + confirmation gate in `acl.py`) and **#17 (human-like behaviour pack — `persona.py`, 14 tests)**; the doc/close-out set #19, #20, #21 went with them. `pytest -q` → **323 passed** (162 baseline + 161 gateway), `test_telegram_gateway.py` → **159 passed**, since 2026-09-29. CI and CodeQL are green on `ubuntu-latest`. **Plan reconciled with reality 2026-09-28/29** — see deviations D9–**D13**. **Only one thing is left in the whole plan: G5 — the single live step (one lecture post + one quiz link), the Playwright deprecation note (#20) already being written. Then G6/G7.** The only Telegram issue left open is **#22 (Telethon), deliberately backlogged**.
> **Epic:** GitHub issue [#7](https://github.com/AboALhasanx/master-studio/issues/7) (children #8–#22, label `telegram`).
> **Bot:** `@cs_mscbot` (token lives in local `.env` only — never in Git).
> **Source discussion:** https://chatgpt.com/share/6aba85ff-aa60-83eb-bd0b-a7d0b3fc01c8
> **Baseline gate:** `pytest -q` → **162 passed** (recorded at G0).

**TL;DR (عربي):** مخطّط هندسي بثماني بوابات G0→G7، كل بوابة تنتهي بـ **Safety Stop Point**: حالة متماسكة ومختبرة وقابلة للتوقف والعودة بأمان، قبل ما نلمس جروبنا الحقيقي.

---

## 1. Design Doctrine (Non-Negotiables)

1. **Bot-first.** Official Bot API only through G0–G6. No MTProto / user account (that is issue #22, deliberately backlogged).
2. **One direction.** `Agent → gateway → Telegram`. No `getUpdates` loop in production. A one-shot `getUpdates` is allowed only for bootstrap (capturing a chat id after you press Start / add the bot).
3. **Fail closed.** Permissions enforced in code (`acl.py`), never in a prompt. Secrets only via environment. Destructive operations require `--confirm`.
4. **The vault is the source of truth.** Topic registry, job queue and audit log live in SQLite/files inside the vault (gitignored where sensitive).
5. **Zero-CLI for the student.** The student speaks natural language; the agent runs the CLI in the background (`AGENTS.md` §1.2).
6. **Every gate ends in a Safety Stop Point (SP).** A stop point is a state where tests are green, nothing is half-wired, the real group is untouched, and we can pause indefinitely.

---

## 2. Repository Layout (where each piece lives)

| Path | Purpose | Issue |
|---|---|---|
| `00_STUDIO_HUB/proposals/FEATURE_TELEGRAM_GATEWAY_ROADMAP.md` | This roadmap (G0 deliverable) | #7 |
| `.env` (local, gitignored) | `TELEGRAM_BOT_TOKEN`, allowed chat ids | #8 |
| `.env.example` | Placeholders only, never real values | #8 |
| `90_Shared_Toolbox/telegram/schema.py` | Pydantic action schema (verbs, validation) | #15 |
| `90_Shared_Toolbox/telegram/registry.py` | Topic registry: `subject → (chat_id, thread_id, …)` | #8, #10 |
| `90_Shared_Toolbox/telegram/acl.py` | Owner allowlist + destructive-confirmation gate | #16 |
| `90_Shared_Toolbox/telegram/store.py` | SQLite queue + idempotency + audit log | #14 |
| `90_Shared_Toolbox/telegram/transport.py` | Bot API executor: `MockTransport` + `HttpTransport` (no `getUpdates`). **D9:** delivers #9 in place of a separate `gateway.py` | #9 |
| `90_Shared_Toolbox/telegram/publisher.py` | Publish pack (text/files/media/polls/buttons) | #11 |
| `90_Shared_Toolbox/telegram/moderation.py` | Reply / edit / delete / pin / reactions — **D11:** delivered inside `schema.py` + `executor.py`, no separate module | #12 |
| `90_Shared_Toolbox/telegram/pipeline.py` | Vault export → publish | #13 |
| `90_Shared_Toolbox/telegram/quizbridge.py` | MCQ deep-link composer (dashboard door, no engine) — **D12** | #18 |
| `90_Shared_Toolbox/telegram/persona.py` | Human-like defaults: pacing, presence, tone — **D13** | #17 |
| `90_Shared_Toolbox/telegram/cli.py` | Single entry point the agents invoke | #15 |
| `90_Shared_Toolbox/tools/tg.py` | Path launcher: `python 90_Shared_Toolbox/tools/tg.py <verb>` | #15 |
| `.mimocode/skills/telegram/SKILL.md` (+ mirror `skills/telegram/SKILL.md`) | Teaches every harness to drive the CLI — kept in sync by `TestTelegramSkill` | #15 |
| `tests/test_telegram_*.py` | Mocked-transport test suite (`-m live` opt-in) | #21 |
| `90_Shared_Toolbox/telegram/registry.json` | Topic registry data (created on first run; **gitignored** — live ids stay local, `SEED_SUBJECTS` is the committed source) | #8 |
| `90_Shared_Toolbox/telegram/gateway.db` | SQLite jobs + audit (gitignored, local-only) | #14 |
| `00_STUDIO_HUB/guides/TELEGRAM_TOPICS_PLAYBOOK.md` | Topic organization rules | #19 |

---

## 3. Gates and Safety Stop Points

### G0 — Alignment & Guardrails · **SP0: "documentation only, zero risk"**
- **Work:** this roadmap; `.env` with the token (gitignored) + placeholder in `.env.example`; baseline test run recorded; epic #7 cross-linked; decision recorded that pilots run in a **disposable test group**, not `Master-Studio FINAL`.
- **Entry:** token verified via `getMe`.
- **Exit / verification:** `pytest -q` → 162 passed; `git status` shows no tracked secret; `git check-ignore -v .env` confirms ignore rule.
- **Stop guarantees:** repo changed by docs only; the bot is idle; the real group untouched.
- **Rollback:** delete the roadmap file.

### G1 — Offline Core · **SP1: "the code exists but cannot touch the network"** — ✅ DONE
- **Work:** `schema.py`, `registry.py`, `acl.py`, `store.py`, `cli.py` plus `tests/test_telegram_*.py`, all against a **mocked transport** (no HTTP client importable in tests).
- **Entry:** SP0 satisfied.
- **Exit / verification:** `pytest -q` green including the new suite; `python -m telegram.cli --dry-run …` prints an action plan without I/O; no real token referenced anywhere in tests.
- **Stop guarantees:** no live call is possible from this state — the safest place to pause for a long time.
- **Rollback:** delete `90_Shared_Toolbox/telegram/` + `tests/test_telegram_*`.
- **Delivered:** `schema.py` (Pydantic verbs + idempotency keys), `links.py`, `acl.py`, `registry.py` (seeded with the 9 legacy subjects, unbound), `store.py` (SQLite jobs + audit + rate limiter + backoff + `.env` reader), `transport.py` (`MockTransport`; `build_transport(live=True)` raises `GatewayNotReady`), `executor.py` (authorize → resolve → dedupe → rate-limit → send → audit), `cli.py` + `__main__.py`, and the agent-facing launcher `90_Shared_Toolbox/tools/tg.py`. Verification: `pytest -q` → **213 passed**; `--live` exits 5; duplicate command exits 0 with `status=duplicate`; missing actor exits 3.

### G2 — Live Smoke, Isolated · **SP2: "only an allow-listed chat is reachable"** — ✅ DONE
- **Work:** real Bot API client (`HttpTransport` in `transport.py` — **D9**, not the layout's `gateway.py`); private-chat `sendMessage`; create → rename → close → reopen → delete a scratch topic; live tests behind `-m live`.
- **Entry:** SP1 green; test group created; bot added as admin (`manage topics`, `delete messages`, `pin messages`, `react to messages`, `change group info`).
- **Exit / verification:** live checklist passes; **chat-id allowlist contains only test ids** and every other target fails closed; `pytest -q` still green.
- **Stop guarantees:** production group is unreachable by construction (allowlist).
- **Rollback:** delete the scratch topic, remove the bot from the test group, reset the allowlist env var.
- **Delivered (2026-09-28):** `HttpTransport` (stdlib, `ensure_ascii=True` payloads — the fix for terminal mangling), 429 → `RateLimited(retry_after)`, other failures → `TransportError`; `chat_allowlist_from_env` enforced **at the executor for live transports only** (empty list denies everything); `.env` now carries `TELEGRAM_OWNER_IDS=5664798395` and `TELEGRAM_CHAT_ALLOWLIST=-1003710711332`.
- **Verified:** `pytest -q` → 221 passed (transport mocked at `urlopen`); live run `tg.py --live edit --chat -1003710711332 --message-id 4` → `sent`, audit row written; manual smoke posted message #4 and reply #5 (`reply_to: 4`) inside the group; `/start` bootstrap captured owner id.
- **Deviation (owner decision):** the disposable test group was replaced by promoting the real group's chat id at G2 — blast radius stays a single allow-listed chat, and every live action is audited. Recorded as **D8**.
- **Structure provisioned live (2026-09-28):** the `structure` verb (composite, idempotent, rate-limited) created **10 topics**, auto-bound every `thread_id` (including jobs drained from the queue), posted a **pinned brief card** per topic and a **pinned index with topic buttons** in General — 0 failures; a live re-run posted nothing (`created: []`, everything `duplicate`). Conventions documented in the Topics Playbook (#19).

### G3 — Capability Packs · **SP3: "rich actions, confined to the single allow-listed chat"** — ✅ DONE
- **Work:** publish pack (#11), moderation pack (#12), file pipeline (#13), durable queue with rate limits / retries / idempotency / audit (#14), MCQ bridge Phase A (#18).
  - **#14 ✅ (closed):** `available_at` cooldown honours `retry_after`, bounded retries (`MAX_ATTEMPTS=8`), `deferred` counter, per-attempt `queue/sent` audit rows, restart-survival test. Deviation: the drain used to leave only an aggregate `queue/run` row.
  - **#13 ✅ (closed):** new `pipeline` verb (resolve → export if stale → publish), fail-closed path refusals via `PipelineError` (exit 8), exclusions per the PR-template security rule. `TOOLS_DIR` deliberately does **not** follow `VAULT_ROOT`. Caught by the live run, not by tests: `VAULT_ROOT` was computed as `parents[3]`, which resolves to the *user profile* directory — every test had monkeypatched the root onto a tmp_path, so a live `--source` died as `source not found`. Now `parents[2]`, with a test that exercises the real checkout layout.
  - **#11 ✅ (closed):** captions, `parse_mode`, `escape_html()`, entity/Markdown-safe chunking under one idempotency key; **and the upload path is now proven live** — `file://` used to travel as JSON, which the Bot API rejects with `400 wrong file identifier/HTTP URL`, so `publish --file` was unshippable until G3. **Landed 2026-09-28/29 (unit-tested only — a new Bot API method or verb stays off the group until G5):** `publish --kind` → `sendPhoto`/`sendVideo`/`sendAudio`/`sendVoice`/`sendAnimation`/`sendSticker` with an `auto` suffix fallback and `document` as the deliberate byte-exact default (Telegram *recompresses* `sendPhoto`), the previously missing `publish --caption`/`--html`, **`media_group`** (a repeatable `--file` becomes one `sendMediaGroup` whose local members are rewritten to `attach://file0…` multipart parts), and **`forward` / `copy`** — the source is read from the link alone (`t.me/c/<chat>/<id>`, `t.me/<user>/<id>`, or a bare id plus `--from-chat`), `copy` may re-caption, and the allowlist gate deliberately watches the **destination** because `copy` only ever *reads* its source. Verified by `--dry-run` against the real registry, not sent.
  - **#18 ✅ (closed, 2026-09-29):** the MCQ bridge Phase A — a new `quiz` verb composes the dashboard deep link (`/quiz/<folder>/<bank>?mode=exam|study[&shuffle=true]`) and publishes it as a `sendMessage` with URL buttons into the registry-resolved subject topic. **No new Bot API method** (the reason it stays inside the outbound-only envelope) and **no second engine**: `quizbridge.py` is pure string arithmetic, imports nothing from the gateway, and the AC2 test parses its AST to prove no `sendPoll`/`correct_option_id` is ever constructed (the docstring names them only to document the deferral). `subject_folder()` is the single place the registry key (`01-Cyber-Security`) becomes the vault folder (`01_Cyber_Security`) — a mismatch there would have produced a 404 the student only sees *after* tapping. **Phase B (native `sendPoll` quiz) stays deferred** (AC3): poll answers arrive as `poll_answer` updates, which needs a `getUpdates` loop forbidden by ADR D2. Verified against the three real banks by `--dry-run`; 16 tests, written RED first (one asserted `status == "ok"` where the executor's convention is `"sent"` — the test was wrong, not the code, and was corrected).
  - **#12 ✅ (closed):** `action` → `sendChatAction` (Bot-API vocabulary validated at schema time, thread-scoped so the signal lands in the topic), `editMessageCaption` vs `editMessageText` chosen by which payload you supply (exactly-one-of enforced), `pin --unpin-all` → `unpinAllForumTopicMessages` behind `--confirm` (bulk ⇒ ADR D7), tests for topic `rename`/`close`/`reopen`, and ACL refusals now audited **with their idempotency key**. AC2 proven live in the allow-listed group (audit ids 97–106); `action` deliberately not exercised live — see the stop guarantee below.
- **Entry:** SP2 green. **Scope note after D8:** there is no disposable test group any more — the allowlist already points at `Master-Studio FINAL`, so "confined" means *the one allow-listed chat and nothing else*. Every pack ships against `MockTransport` first; live sends stay behind `--live`.
- **Exit / verification:** ✅ **all five verified live 2026-09-28** — (1) idempotency: a repeat carries the same key and reports `duplicate` instead of posting twice; (2) simulated 429 retried with no loss (unit-tested, `deferred` counter); (3) **a real PDF exported and published**: `pipeline` → `pdf_exporter.py -t study_pack` → `sendDocument` → **message 28** in `04-Advanced-Software-Eng`; (4) audit rows for every attempt: **ids 97–106**, including `delete … denied — destructive action requires --confirm` carrying the *same* idempotency key as the confirmed run that followed; (5) a non-allowlisted chat id fails closed with **no network call** (exit 3).
- **Stop guarantees:** nothing outside the allow-listed chat; queue survives restarts; production group untouched by *new* verbs until G5 — honoured: only verbs that already existed in `build_call` were used live, `action` was not.
- **Rollback:** stop using the queue; posts made through packs are editable/deletable (D8 blast radius).

### G4 — Agent Control · **SP4: "natural language works, unauthorized actors cannot"** — ✅ DONE (2026-09-29)
- **Work:** telegram skill (#15) + `cli.py` verbs wired end to end; owner allowlist and confirmations (#16); human-like defaults (#17).
- **Entry:** SP3 green.
- **Exit / verification:** natural-language request → CLI → post appears in the allow-listed group (D8); an unauthorized actor id is refused and logged (test); invalid action input rejected with no network call.
- **Delivered (2026-09-29):** `.mimocode/skills/telegram/SKILL.md` (+ the mirror `skills/telegram/SKILL.md`, which a test keeps byte-identical) — a complete driver for every harness: the `--dry-run`-first protocol, the destination/registry table, all 15 verbs with worked examples, the exit-code table, the six in-code safety rules, and a troubleshooting matrix. `#16` is delivered by `acl.py` (owner allowlist, fail-closed on an *empty* list, `--confirm` gate for topic-delete / bulk-delete / `unpin-all`), all audited with the idempotency key. **`#17` is delivered by `persona.py`** — presence-first (`sendChatAction` on live transports only, so the suite never sleeps), deterministic-but-unequal pacing (0.8/2.0/1.4/2.6, capped at 25 s, RNG forbidden by an AST test), contextual reply-anchoring (`reply_to` → `reply_to_message_id`), and the Iraqi tone block quoted verbatim in SKILL §5. All three #17 acceptance criteria carry their own test names (`test_ac1_*`, `test_ac2_*` ×3, `test_ac3_*` ×2) so they are machine-checkable; `TestPersona` → **14 passed**.
- **Verified:** `pytest -q` → **323 passed**; `tests/test_telegram_gateway.py` → **159 passed**. Six skill tests pin the doc to the CLI — every verb must be documented, **no flag may be documented that the parser lacks** (`--registry`/`--db` plumbing aside), all media kinds + quiz modes present, **every one of the 29 real invocations in the SKILL.md is run through the real parser** (`--live` swapped for `--dry-run`, so the check can never reach the network), and the two copies of the skill must not drift. AC2 proven live: `publish --kind photo` with no file → `code 2`; `--actor 999999` → `code 3`, both with no network call.
- **Stop guarantees:** the skill changes agent behaviour only when invoked; every new verb is confined to the allow-listed chat; nothing was posted to the group in this gate.
- **Rollback:** remove the skill file; agents fall back to no telegram actions.

### G5 — Pilot Cutover · **SP5: "the real group is touched, minimally"**
- **Work:** ~~promote the allowlist to `Master-Studio FINAL`~~ ✅ **done at G2 (D8)**; ~~build the topic registry~~ ✅ **done at G2** (10 topics auto-bound in `registry.json`); publish **one** lecture post and **one** quiz link; add the deprecation note to the Playwright scripts (#20).
- **Entry:** SP4 green; bot is admin in the real group ✅; registry seeded ✅. **What actually remains:** the two posts + the deprecation note.
- **Exit / verification:** the two posts are live and correctly placed; registry resolves every subject; `pytest -q` green; audit log shows exactly the intended actions.
- **Stop guarantees:** old Playwright scripts still present; bot can be pulled from the group instantly.
- **Rollback:** remove the bot from the group **or** reset the allowlist to test ids — both take seconds.

### G6 — MCQ Bridge & Digests · **SP6: "results flow, still one-directional"**
- **Work:** ~~publish quiz deep links with URL buttons (#18)~~ ✅ **Phase A done at G3 (D12)** — the `quiz` verb publishes the dashboard door; agent-generated results summaries from `/api/quiz/history` + `/api/quiz/list`; topic digests (#19 conventions). **Phase B (native `sendPoll` quiz with `poll_answer` ingestion) remains explicitly deferred** — it conflicts with D2 and is tracked inside #18.
- **Entry:** SP5 stable for at least one real study session.
- **Exit / verification:** one command publishes a working exam link; results summary lands in the same topic; no second quiz engine exists (shared JSON schema intact) — the AC2 AST test in `tests/test_telegram_gateway.py` pins this permanently.
- **Rollback:** stop issuing the publish command; nothing else changes.

### G7 — Hardening & Close-out · **Final stop: "gateway is the only path"**
- **Work:** topic playbook committed (#19); retire Playwright/CDP scripts in a dedicated PR (#20); full pytest coverage review (#21); epic acceptance criteria checked.
- **Entry:** SP6 green.
- **Exit / verification:** `pytest -q` green; playbook cites official Telegram sources; removal PR merged; epic #7 checkboxes satisfied.
- **Rollback:** the removal PR is isolated and revertible on its own.

---

## 4. Safety Stop Point Matrix

| SP | Safe state guarantee | Verification | Rollback |
|---|---|---|---|
| **SP0** | Docs only, secret isolated, bot idle | `pytest -q`; `git check-ignore -v .env` | delete roadmap |
| **SP1** | Code cannot reach the network | `pytest -q`; `cli --dry-run` | delete package + tests |
| **SP2** | Only the single allow-listed chat reachable — after D8 that chat *is* `Master-Studio FINAL`; every other target fails closed | live checklist; allowlist test | reset `TELEGRAM_CHAT_ALLOWLIST` / remove bot |
| **SP3** | Rich actions confined to the allow-listed chat; queue durable | idempotency + backoff tests | drop queue usage |
| **SP4** | Natural language works; strangers refused & logged | e2e + ACL tests | remove skill file |
| **SP5** | Real group touched by 2 posts; old scripts intact | live review + registry check | remove bot / reset allowlist |
| **SP6** | One-way results; quiz schema shared | publish link + summary test | stop command |
| **Final** | Gateway is the only publishing path | full gate: pytest + docs | revert removal PR |

**Standing rule:** any gate may be paused at its SP without technical debt. To resume, re-run that gate's verification; if it fails, fix forward — never skip a gate.

---

## 5. Decision Log (ADR)

| # | Decision | Rationale |
|---|---|---|
| D1 | Official bot only (no user account) | Zero ban risk; MTProto is backlog #22 |
| D2 | No `getUpdates` loop in production | Scope is one-directional; no always-on service needed |
| D3 | CLI + skill now, MCP later | Zero-CLI policy + token economy with a single harness |
| D4 | Web-quiz link first, native quiz poll later | Poll answers require inbound updates (violates D2) |
| D5 | Disposable test group before the real group — **superseded by D8** | SP2/SP3 isolation |
| D6 | Topics addressed by `message_thread_id` registry | Bot API has no "list topics" method |
| D7 | Topic deletion always needs `--confirm` | Deleting a topic wipes every message inside it |
| D8 | Promote the real group's chat id at G2 instead of a disposable test group (owner decision) | Blast radius is one allow-listed chat; every live action is audited and reversible (edit/delete) |
| D9 | Deliver the Bot API client inside `transport.py` (`HttpTransport`) instead of the layout's separate `gateway.py` | One stdlib HTTP path already owns the `urlopen` seam tests mock, plus 429 → `RateLimited` and failure → `TransportError`; a second module would duplicate it |
| D10 | Gitignore `registry.json` (live chat/thread bindings) and keep `SEED_SUBJECTS` as the committed source | Live ids are runtime state, not source; a fresh clone re-provisions with a no-op idempotent `structure` run |
| D11 | Deliver the moderation pack inside `schema.py` (action classes) + `executor.py` (`build_call`) instead of the layout's separate `moderation.py` | Every verb already funnels through `parse_action` → `build_call` → ACL → audit; a second module would duplicate the destination resolution, the `Call` seam and the confirmation path for no gain. `publisher.py` *stays* separate because it owns real text semantics (HTML escaping, 4096/1024 limits, entity-safe chunking) — same split logic as D9 |
| D12 | The MCQ bridge (#18) is a **`quiz` verb composed in `quizbridge.py`**, not a `publish` preset and not a poll | A deep-link door is: (a) one verb, so the agent cannot forget the allowlist/audit path; (b) pure string arithmetic, so AC2 ("no second engine") is enforceable by an AST test rather than a promise; (c) `sendMessage`-only, so it needs no new Bot API capability and stays shippable at G5. Native `sendPoll` remains Phase B because poll answers require `getUpdates` ingestion — forbidden by D2 |
| D13 | Pacing/tone (#17) live in a **`persona.py` policy module** with a **deterministic** delay pattern, applied **only to live transports** | Pacing is policy, the transport is mechanism — the split lets the executor sleep between calls while `MockTransport` stays instantaneous, so the suite asserts the behaviour without waiting. The pattern is fixed (not RNG) so an audit log is reproducible and tests never flake; a live `sendChatAction` is cosmetic and its failure is swallowed so it can never break a real post |

---

## 6. Risk Register

| Risk | Mitigation |
|---|---|
| Token leak | `.env*` gitignored (verified `!.env.example` exception); token never in docs or code; rotate via @BotFather if ever exposed |
| Publishing to the wrong group | Fail-closed chat-id allowlist in code; promotion was moved to G2 by **D8**, so the allowlist is the *only* guard — treat any second entry as an incident |
| Topic deletion wipes content | `--confirm` gate (D7) + audit log |
| Telegram rate limits (429) | Durable queue, per-chat token bucket, backoff honouring `retry_after` |
| Arabic text mangled in terminal | Observed live at G0 (`setMyCommands`); pass UTF-8 payloads via files, keep CLI args ASCII |
| Confusion with legacy scripts | Deprecation note at G5; removal isolated at G7 |
| Bot privacy mode (`can_read_all_group_messages: false`) | Irrelevant under D2; as group admin it receives messages anyway if ingestion is ever added |

---

## 7. Standing Verification Gates

```bash
pytest -q                                   # must be green at every SP (323 since 2026-09-29)
python 90_Shared_Toolbox/tools/tg.py --dry-run status   # plan without I/O
                                             # (--dry-run is GLOBAL: it must precede the verb,
                                             #  and `python -m telegram.cli` only resolves from
                                             #  90_Shared_Toolbox/ — use tools/tg.py from the vault root)
python -m bandit -q -r 90_Shared_Toolbox/telegram -f json   # baseline 7x B101 + 1x B310 (pre-existing idiom)
gh issue list --label telegram --state open # phase backlog health
git check-ignore -v .env                    # secret isolation
git check-ignore -v 90_Shared_Toolbox/telegram/registry.json  # live ids stay local (D10)
```

---

## 8. Issue ↔ Gate Map

| Gate | Issues |
|---|---|
| G0 | #7 (epic) |
| G1 | #15, #16, #21 (schema/ACL/test scaffolding) |
| G2 | #8, #9, #10 (bootstrap captured owner id + group chat id; `manage_topics` confirmed) |
| G3 | #11, #12, #13, #14, #18 |
| G4 | #15, #16, #17 (all closed — #17's human-like pack is `persona.py` + `TestPersona`, 14 tests) |
| G5 | #8, #10, #20 (note) |
| G6 | #18 (Phase B — native poll, deferred) |
| G7 | #19, #20, #21, #7 acceptance — **all four now closed**; only #22 (Telethon) stays open by design |
| Backlog | #22 |
