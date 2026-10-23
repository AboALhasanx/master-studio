# Master Studio: Harness Attendance Registry

> **Rule (binding, see `AGENTS.md` §8):** every harness signs in by name. No anonymous "another agent" talk — when you find another harness's work, name it with date: *"found work from Codex 2026-09-22, left intact"*.
> New harness first session: add your row below, then append a sign-in line to today's `sessions/YYYY-MM-DD.md`.

| Harness | Agent identity | Marker it leaves | Last seen | Status | Role / notes |
|:---|:---|:---|:---|:---|:---|
| WorkBuddy | Koko 🐨 (named by student 2026-09-18) | `.workbuddy-ai/memory/` (tracked) | 2026-10-16 | ACTIVE — primary | Study notes, Telegram gateway, dashboard, `phone_sync` v2. Largest footprint. |
| OpenCode | Build agent (DeepSeek V4.1 Flash; sessions: NH UI U2 wide-slides answer-key rebuild · one-activity-per-page + source-fidelity audit · ASE Ch01 T4–T7 + V1 vocabulary) | `opencode-archive/` (legacy config) | 2026-10-23 | ACTIVE | Vault tidy, zero-leakage fixes, PDF rebuilds, ASE slide-pack reorg, NH U2 wide-slides (59 pages) + NH U3 wide-slides (37 pages), both 10-gate, official-source extraction (`_extract_sources.py`), ASE Ch01 question-type packs T4_Analyze/T5_Evaluate/T6_Create/T7_Apply_Calc + V1_Vocabulary_Coverage. |
| MiMo Studio / Desktop | Koko | `.mimocode/skills/` | 2026-10-02 | SEEN | Session logs, bilingual packs. Shares the Koko identity with WorkBuddy. |
| Codex | Reviewer / study coordinator | none (works inside shared logs) | 2026-10-23 | ACTIVE | ASE Ch09 remediation coordination, source checks, print QA, and vector-index refresh. |
| Oh My Pi (OMP) / Antigravity | Coding Assistant (google-antigravity/gemini-3.8-flash) | `00_STUDIO_HUB/sessions/` entries | 2026-10-23 | ACTIVE — ASE Ch09 Question Packs Authoring Lead | Authoring study packs for Chapter 9 Software Maintenance, source verification, formula checks, diagram extraction, and strict delivery gates. |
| FreeBuf | unknown | `.freebuff/project-id` (single UUID file) | never in sessions | TRACE ONLY | No session content found. If it signs in, it adds its own row. |
| Cursor | unknown | none | never | ANNOUNCED | Named in `AGENTS.md` §8 only. Row waits for its first sign-in. |

## Sign-in line format (append to today's session file at session start)

```markdown
> **Harness sign-in:** <Harness> (<agent/model>) — <task area>. Registry row verified.
```

## Rules for coexisting

1. **Name, don't shadow.** Cite harness + date for any foreign work you touch or skip.
2. **One canonical file per day** (`sessions/YYYY-MM-DD.md`) — append with your harness heading, never fork `session-01` variants.
3. **Marker files are owned.** Don't delete another harness's marker dir (`.workbuddy-ai/`, `.mimocode/`, `.freebuff/`) — announce first per MEMORY.md rule §3.
4. **Registry is append-mostly.** Update your own `Last seen`; never rewrite another harness's row.


