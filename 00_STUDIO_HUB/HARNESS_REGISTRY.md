# Master Studio: Harness Attendance Registry

> **Rule (binding, see `AGENTS.md` §8):** every harness signs in by name. No anonymous "another agent" talk — when you find another harness's work, name it with date: *"found work from Codex 2026-09-22, left intact"*.
> New harness first session: add your row below, then append a sign-in line to today's `sessions/YYYY-MM-DD.md`.

| Harness | Agent identity | Marker it leaves | Last seen | Status | Role / notes |
|:---|:---|:---|:---|:---|:---|
| WorkBuddy | Koko 🐨 (named by student 2026-09-18) | `.workbuddy-ai/memory/` (tracked) | 2026-10-02 | ACTIVE — primary | Study notes, Telegram gateway, dashboard. Largest footprint. |
| OpenCode | Build agent (this session: cleanup phases) | `opencode-archive/` (legacy config) | 2026-10-03 | ACTIVE | Vault tidy, zero-leakage fixes, PDF rebuilds. |
| MiMo Studio / Desktop | Koko | `.mimocode/skills/` | 2026-10-02 | SEEN | Session logs, bilingual packs. Shares the Koko identity with WorkBuddy. |
| Codex | Reviewer | none (works inside shared logs) | 2026-09-22 | SEEN — reviewer | 10-point checklists, math audits (SC W02, DM W03). Reviews, does not author notes. |
| Oh My Pi (OMP) | session URLs (`my.omp.sh/s/…`) | `omp_session_url` in old logs | 2026-09-18 | HISTORICAL | Early sessions only. Do not expect new work. |
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
