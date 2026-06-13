-- ============================================================================
-- MBM — "Talk to a real person" two-way inbox
-- ============================================================================
-- Run this ONCE in the Supabase dashboard: SQL Editor → New query → paste → Run.
--
-- How it stays private with NO login:
--   Every install signs in ANONYMOUSLY (Supabase anonymous auth). That gives the
--   device a real, hidden auth identity (auth.uid()) without the person ever
--   creating an account or giving an email. Row-Level Security below scopes every
--   read and write to that identity, so a person can ONLY ever see their own
--   thread — even though the app ships with the public anon key.
--
--   The admin (you) reads and replies with the SERVICE ROLE key, which bypasses
--   RLS. That key lives ONLY in your local admin page (admin/inbox.html), never
--   in the app and never in git.
-- ============================================================================

create extension if not exists "pgcrypto";

create table if not exists public.messages (
  id            uuid primary key default gen_random_uuid(),
  user_id       uuid not null,                       -- the person's anonymous auth uid
  sender        text not null check (sender in ('user', 'admin')),
  body          text not null default '',
  excerpt       text,                                -- optional chat excerpt carried in
  journey_stage text,                                -- where they are, for your triage
  created_at    timestamptz not null default now(),
  read_by_admin boolean not null default false,      -- you have seen it
  read_by_user  boolean not null default false       -- they have seen your reply
);

create index if not exists messages_user_id_created_idx
  on public.messages (user_id, created_at);

-- ── Row-Level Security ──────────────────────────────────────────────────────
alter table public.messages enable row level security;

-- A person may INSERT only their own messages, only as the 'user' sender.
drop policy if exists "user inserts own" on public.messages;
create policy "user inserts own" on public.messages
  for insert to authenticated
  with check ( auth.uid() = user_id and sender = 'user' );

-- A person may READ only their own thread (their notes + your replies to them).
drop policy if exists "user reads own" on public.messages;
create policy "user reads own" on public.messages
  for select to authenticated
  using ( auth.uid() = user_id );

-- A person may mark messages in their own thread as read (read_by_user).
drop policy if exists "user updates own" on public.messages;
create policy "user updates own" on public.messages
  for update to authenticated
  using ( auth.uid() = user_id )
  with check ( auth.uid() = user_id );

-- NOTE: there is intentionally NO admin policy. The admin uses the service-role
-- key, which bypasses RLS entirely. Never give the anon/authenticated role broad
-- read access — that would let any device read every person's thread.

-- ── Realtime ────────────────────────────────────────────────────────────────
-- Let the app receive your replies the moment you send them. RLS still applies,
-- so each device only receives rows from its own thread.
alter publication supabase_realtime add table public.messages;
