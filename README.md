# Milk Before Meat (MBM)

A mobile-first gospel-outreach app patterned after the way Jesus ministered: meet a
person exactly where they are, learn who they are by paying attention, and gently walk
them from foundational truth ("milk") toward the restored gospel ("meat") — never by
pressure, always with a real human one tap away.

This is the **version 1 rough-draft handoff**. The app is built, type-checks clean, and
has been submitted to both app stores. What remains is testing, the store waiting
periods, and polish.

---

## Start here (read in this order)

1. **[START-HERE.md](./START-HERE.md)** — the single source of truth for *what is true
   right now* (what's built, submitted, and pending). If anything else disagrees with
   this file, this file wins.
2. **[docs/00-PROJECT-MAP.md](./docs/00-PROJECT-MAP.md)** — the full table of contents:
   every folder, every important file, and where to find it.
3. **[AGENT-RULES.md](./AGENT-RULES.md)** — the vision, the laws, and how the app is
   meant to behave (the "Jesus method").
4. **[SESSION-LOG.md](./SESSION-LOG.md)** — the running history of every work session.

## At a glance

| Piece | Where it lives | What it is |
|---|---|---|
| The app (the thing people install) | `mobile/` | React Native + Expo. Source in `mobile/src/`. |
| The app's website | `site/` | milkb4meat.org pages (hosted by Firebase). |
| The public landing page | `pitch-book/site-milkb4meat.html` | The Squarespace landing page content. |
| The ministry console (your reply desk) | `admin/` | Private inbox for "talk to a real person" threads. |
| The proxy/server | `server/` | Keeps the AI key off the phone. |
| Marketing / pitch materials | `pitch-book/`, `church-launch-kit/`, `store-assets/` | Brochures, the book, screenshots, store copy. |
| All documentation | `docs/` | Publishing, roadmap, vision, reviews, archive. |
| Old builds (archived) | `builds-archive/` | Superseded .apk/.aab files. Nothing deleted. |

## Current status (one line)

iOS v1.0 (build 6) submitted to Apple (auto-releases on approval) and live on
TestFlight; Android live on Play **internal** testing, with a 12-tester / 14-day closed
test as the last gate before public. Full detail in **[START-HERE.md](./START-HERE.md)**.

## The non-negotiables

Meet people where they are. Never pressure, shame, or manipulate. Always keep a real
human one tap away. The AI speaks only from what it knows and admits uncertainty. A
person is not a data point. Jesus let the rich young ruler walk away — this app does too.
(Full set in [AGENT-RULES.md](./AGENT-RULES.md).)
