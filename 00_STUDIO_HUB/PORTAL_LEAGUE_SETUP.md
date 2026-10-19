# Portal League Setup — shared Duolingo-style board (one time, ~10 min, free)

The league board is the ONLY shared piece: one public Supabase table.
Identity still comes from Telegram (no passwords). Everything else
(saved/history/stats) stays as-is.

## Status (2026-10-19) — DONE, live

- Project: `fauomjucqcreohnvmbcb` (`smart_booking_system`) — publishable key
  `sb_publishable_...` is already in `mcq-portal/js/supabase-config.js`.
- Tables created by running `PORTAL_LEAGUE_SCHEMA.sql` in the SQL Editor:
  `public.league_xp` (weekly board) and `public.portal_data` (personal bundle).
- Identity = Telegram. Two paths supported:
  `window.Telegram.WebApp` bridge (mobile/desktop app) and the
  `#tgWebAppData=...` hash (Telegram Web K) — both verified live in the
  user's real Telegram Web session (`linked: true`, `store: supabase`).
- Profile photo: `photo_url` from Telegram is used for the menu avatar and
  the league rows; falls back to the first letter of the display name.
- Personal sync = one JSON row per user in `portal_data` (saved questions,
  history, bests). Weekly league = rows in `league_xp` (xp, per_subject, hidden).
- Test rows used during verification were deleted again (no DELETE policy is
  left open on the tables; clients cannot delete rows).


1. Open https://supabase.com/dashboard and sign in (GitHub login is fine).
2. **New project** → name `mcq-portal` → pick a region near Iraq
   (e.g. West Europe) → set a database password (save it somewhere) → Create.
   Wait ~2 minutes until it reports healthy.
3. **Project Settings (gear icon) → API**: copy two values:
   - **Project URL** (`https://xxxx.supabase.co`)
   - **anon public key** (the long `eyJ...` token — public by design,
     it ships inside the web app; RLS rules below keep writes sane).

## 2. The league table + rules (copy/paste once)

Supabase Dashboard → **SQL Editor** → **New query** → paste the file
`00_STUDIO_HUB/PORTAL_LEAGUE_SCHEMA.sql` from this vault → **Run**.
It creates `public.league_xp(user_id, week_id, name, username, avatar,
hidden, xp, per_subject, updated_at)` with open-read + CHECK-constrained
writes (friendly-group threat model, documented in the file).

## 3. Put the key in the portal

Edit `mcq-portal/js/supabase-config.js`:
`key: '<PASTE_ANON_KEY_HERE>'` (url is already filled),
then commit + `vercel --prod`.

## 4. Telegram login (required for the board to know who is who)

Same as before (`PORTAL_CLOUD_SETUP.md`): set the Menu Button of
`@cs_mscbot` to `https://mcq-portal-jade.vercel.app/`
(+ optional `/setdomain mcq-portal-jade.vercel.app`).
Students open the portal from that menu — no passwords, ever.

## Defaults the agent used (say the word to change)

- Week starts **Monday** (like Duolingo). One line in `js/league.js` changes it.
- Display name = Telegram **first name** (+ @username as fallback).
- Hidden mode = excluded from the board entirely (private-profile style).
- XP = 1 per correct answer, weekly board + per-subject tabs + share button.
