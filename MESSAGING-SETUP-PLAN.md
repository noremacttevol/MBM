# MBM — Messaging & Admin Team Plan

_Plan written 2026-06-18. Plan only — no code written yet. This fills the
`RESPONDER-ROADMAP.md` that `admin/inbox.mjs` refers to, and extends it._

This is the plan for how a person's message to a real human reaches you, alerts
you wherever you are, lets you reply easily, and lets approved helpers carry some
of the load with conversations split between them automatically.

Your three choices are baked in: **reply outside the consumer app**, **whatever
is easiest**, and **auto-distribute** work across helpers.

---

## The short version — what you'll actually experience

1. Someone in the app taps "talk to a real person" and writes a note.
2. Within seconds you (or the helper it's auto-assigned to) get an **email** with
   the person's message and a single link.
3. You tap the link, it opens your **reply desk** in any browser — phone or
   computer — and you type back. Your reply appears in their app, signed only as
   "a real person."
4. When you approve a helper, new conversations start getting handed out
   automatically so no one person carries everyone, and nobody trips over each
   other answering the same person.

Nothing about this lives inside the app people use. Your desk is its own private
thing.

---

## What you already have (we build on this, not over it)

- **The cloud inbox is done.** Messages flow into Firebase. Each person can only
  ever see their own thread — that's locked by the security rules. This is the one
  cloud piece in the whole product; everything else stays on the phone.
- **Your reply desk is done** (`admin/inbox.mjs`). It lists everyone waiting,
  shows full threads, lets you reply, marks things "needs reply / handled," and
  already stamps every reply with who sent it.
- **The team groundwork is already in the data.** The desk already writes
  "assigned to" and "handled by" fields. Right now the responder is just
  hard-wired to you (`RESPONDER = { id: 'cameron', name: 'Cameron' }`). Helpers
  slot into that with no rewrite.

So we are adding three things, not rebuilding anything.

---

## The three things we add

### 1. Alerts that reach you anywhere — by email (easiest)

**The gap:** today an alert only pops up while the desk page is sitting open in a
browser. If the page is closed, nothing tells you someone wrote in.

**The fix:** a small always-on watcher notices every new message the moment it
lands and emails the right person. Email is the easiest, most reliable choice —
it works on every phone with nothing to install, and the email carries the
message text plus one tap-through link straight to that conversation.

Text-message (SMS) and phone push alerts are easy to add later on top of the same
watcher if email ever feels too slow. Email first.

### 2. A desk you can open from your phone, anywhere — safely

**The gap:** the desk runs only on your computer (`localhost`), so you can't
answer from your phone at the store.

**The fix:** put the same desk on a private web address protected by a login, so
you can open it from any browser, anywhere. The powerful master key
(`serviceAccount.json`) stays on the server side and is never sent to your phone —
your phone just logs in. (Note: you already use Railway for the `server/` proxy;
that same host can run this desk, so it's not a new account to learn.)

### 3. A team: approve helpers, split work automatically

**The gap:** one hard-coded responder, no way to add or approve helpers, no
splitting.

**The fix, in three parts:**

- **Sign-in instead of hard-coded name.** Each helper signs into the desk with
  their own Google account. The desk then knows who's answering and stamps replies
  with their identity automatically.
- **You approve helpers.** A new helper who signs in lands as "pending" and can't
  see anyone's messages until you approve them. You get an "Admins" tab where you
  approve, pause, or remove people. You're the owner; only you can approve.
- **Auto-distribute (your pick).** When a brand-new conversation arrives, the
  watcher hands it to the approved, available helper with the fewest open
  conversations (simple round-robin / least-busy). That helper — and only that
  helper — gets the email and owns the thread. Everyone can still see a shared
  "all conversations" view, and you as owner see everything, but the day-to-day
  load spreads itself.

This rides on the "assigned to" field the desk already writes, so it's an
extension, not a new system.

---

## How one message flows, start to finish

1. Person taps "talk to a real person," writes a note → it's saved to Firebase
   under their hidden anonymous identity.
2. The watcher sees a new note with no one assigned yet.
3. It picks the approved + available helper with the lightest load and stamps the
   thread "assigned to [helper]."
4. It emails that helper: the person's message, where they are in their journey
   (for gentle context), and a link.
5. Helper taps the link → desk opens in their browser → they log in (if not
   already) → they read the thread and reply.
6. The reply lands in the person's app within a second, signed "a real person,"
   and the thread is marked handled.
7. If the person writes again, it goes back to the same helper who owns them, so
   the relationship stays continuous.

---

## What it costs

- **Firebase:** free at this scale. The always-on watcher uses Firebase's
  pay-as-you-go tier, which has a large free allowance — at MBM's early volume
  the realistic cost is **$0**, but it does require putting a card on file. If you
  would rather not, the watcher can instead run on the Railway server already in
  the repo and stay on Firebase's fully-free tier. Either works; I'll pick
  whichever is least hassle when we build.
- **Email sending:** a free transactional-email tier (thousands of emails/month
  free) covers Phase 1 and 2 easily.
- **The desk host:** the free/cheap Railway tier you already use.

No new paid commitment is needed to start.

---

## What I'll need from you to build it (one short setup session)

You won't have to code anything. When we build, I'll walk you through, one tap at
a time:

1. The six Firebase config values (you may already have these — they go in
   `mobile/.env`).
2. Generating the Firebase service-account key once (the master key for the desk).
3. Saying yes to one of: add a card to Firebase (stays $0) **or** use Railway for
   the watcher. I'll recommend the easier one when we're there.
4. The list of emails you want approved as helpers to start (can just be you).

Everything else I build and verify myself, with screenshots, before calling it
done.

---

## One thing to clean up while we're here

There are currently two half-overlapping admin paths in the repo: the **Firebase
desk** (`admin/inbox.mjs`, the real "talk to a real person" path) and the older
**`server/` proxy** (which mainly hides your Anthropic key and has its own little
`admin.html` queue). The messaging plan above standardizes on the **Firebase
desk** as the single place you answer people. The `server/` proxy keeps its real
job (protecting the API key) but stops being a second, confusing inbox. I'll make
that split clean so there's only ever one place to look.

---

## Suggested build order (when you say go)

- **Step A — Alerts first.** Stand up the watcher so you get an email the instant
  anyone writes in. This alone removes the "I missed someone" worry, even before
  the team part exists.
- **Step B — Desk on the web.** Move the desk to a private login-protected address
  so you can answer from your phone.
- **Step C — Team + auto-split.** Add helper sign-in, your approval screen, and
  automatic hand-out of new conversations.

Each step is useful on its own, so you get value after Step A without waiting for
all of it.
