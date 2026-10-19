-- MCQ Portal — weekly league table (run once in Supabase Dashboard -> SQL Editor).
-- Copy everything below, press Run. Safe to re-run (IF NOT EXISTS / DROP IF EXISTS).
--
-- Threat model (friendly student group, v1): reads are public; writes are
-- open but CHECK-constrained (xp sane, name short). No auth needed because
-- identity comes from Telegram WebApp client-side. Upgrade path later:
-- edge-function verification of initData if griefing ever appears.

create table if not exists public.league_xp (
  user_id     text        not null,
  week_id     text        not null,            -- Monday date 'YYYY-MM-DD' of the week
  name        text        not null default '' check (char_length(name) <= 40),
  username    text        not null default '' check (char_length(username) <= 40),
  avatar      text        not null default '',
  hidden      boolean     not null default false,
  xp          integer     not null default 0  check (xp >= 0 and xp <= 5000),
  per_subject jsonb       not null default '{}'::jsonb,
  updated_at  timestamptz not null default now(),
  primary key (user_id, week_id)
);

alter table public.league_xp enable row level security;

drop policy if exists "league public read" on public.league_xp;
create policy "league public read"
  on public.league_xp for select
  using (true);

drop policy if exists "league community insert" on public.league_xp;
create policy "league community insert"
  on public.league_xp for insert
  with check (true);

drop policy if exists "league community update" on public.league_xp;
create policy "league community update"
  on public.league_xp for update
  using (true)
  with check (true);
