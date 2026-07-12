# Feed 2.0 ("The Prescribed Feed") — Rebuild Prompt for Claude Code

Paste this into Claude Code in the MBM repo. Compare it against the existing app
(FEED-2.0-SPEC.md, mobile/src/screens/FeedScreen.tsx, ContentCard.tsx,
SaveNoteLink.tsx, JournalScreen.tsx, ProfileScreen) before writing anything —
the app already has the interaction layer working; only the prescribed-feed
page/honoring system is new.

---

## Task

Rebuild the feed as Feed 2.0 per `FEED-2.0-SPEC.md`, preserving ALL existing
content interactions exactly as they work today. First produce a comparison:
what the spec + notes below require vs. what already exists in the codebase,
then implement only the gap.

## Feed structure (locked spec)

- ~100 prescribed pages. Each page contains: 2 video+verse pairs, 0–1 rare
  standalone verse, 1 question, 1 invitation (at the bottom).
- The 200 animated Jesus-story videos are the spine (reverent painterly style,
  90s–3min, Two-Voice Law: KJV red-letter Jesus voice + modern narrator, each
  carries its Seed question, MILK-only). Each video sits with its linked KJV
  verse underneath. ~100 verse-only pool items.
- The 20-story opening bank stays text-only; videos live only in the feed.

## Honoring system

- Honored = video watched to 100% / verse link opened / question answered /
  invitation tapped.
- When the user scrolls away from the home page, honored items move to the
  previous pages (re-viewable any time) and their slots refill instantly with
  fresh content. Un-honored items do not move; ignoring a page and hitting
  next leaves the home page as it was.
- Video and its verse honor SEPARATELY. Watch the video but skip the verse →
  the verse recycles back into a later page as a reminder.
- In-product framing: "fresh unseen content first, nothing forced."

## Video playback law

- Tap → full-screen, no controls: no pause, no seek, no skip, until complete.
- Leave the app and return → rewind 5 seconds and resume.
- (Pre-approved App Store contingency: a single flag that enables a pause
  fallback if review requires it.)

## Navigation

- Wheel navigation along the bottom: one dot per previous page + a home icon
  for today's page. Previous pages are re-viewable any time.
- "Next page" uses the honest wait ladder ("Preparing your next page…" —
  escalating waits; time spent with current content earns pages faster).

## Scripture linking — IMPORTANT CORRECTION

- "Read the verse" is an EXTERNAL LINK, not in-app scripture text:
  - Bible Gateway for general users
  - For LDS content: the Church's approved, freely-given scripture sources
    (churchofjesuschrist.org Gospel Library) — member-approved material only.
- Do not host or reproduce scripture inside the app for this action; link out
  to the approved sources. Opening the link is what honors the verse.

## Interactions — every item gets the full set (already built in the app)

Every video, verse, story, question, and invitation carries the existing
interaction row (see ContentCard.tsx / SaveNoteLink.tsx — reuse, don't rewrite):

- **Reflect on this →** — inline reflection box, saved on Keep.
- **Talk About It →** — prefills chat ("I just watched/read … Can we talk
  about it?") and opens the existing Talk About It AI minister chat.
- **Save it →** — saves the item.

Where saves land (by content type):

- Reflections on SCRIPTURE or STORIES → the **Journal**.
- Interactions with QUESTIONS or INVITATIONS → the **Profile** (the user's
  record/faith timeline).
- Saved verses appear in the Journal as the verse TITLE ONLY (e.g.
  "Luke 13:10–17"); the title is a link that takes the user back to that
  scripture / scripture+video wherever it sits in their past historical feed
  pages (or today's page if not yet honored).

## Flow / tone guardrails

- God is good → Jesus atoned for you → subtle, signal-gated invitations toward
  the Restoration, driven by the user's own words.
- Feed content stays MILK — its one job is showing Jesus is good.
- Visual language: existing app theme — near-black #0a0a0f, gold #d4c89a,
  warm parchment text, Jost, quiet thin-bordered cards, italic blue sub-links.

## Deliverable

1. A comparison table: each requirement above vs. current implementation
   (file + status: exists / partial / missing).
2. Implementation plan for the gaps only.
3. Then build, reusing existing components and stores wherever they already
   do the job.
