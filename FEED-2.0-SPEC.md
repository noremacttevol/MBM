# FEED 2.0 — The Prescribed Feed (locked spec, 2026-07-07)

Cameron's direction, given in full and confirmed through clarifying questions.
This is the law for the feed revamp. Read alongside AGENT-RULES.md, CLAUDE.md,
media-production/00-MASTER-PLAN.md, and media-production/THE-200.md.

Cameron's private strategy framing stays out of the app, out of store copy,
and out of any user-facing text — it lives only in his own notes. In the
product this is simply: fresh, unseen content first; the stories invite
honest questioning the way Jesus invited it; nothing is ever forced.
The existing Gospel Principles laws all still bind (never pressure, never
manipulate, real human one tap away, the rich young ruler walks away free).

---

## 1. Content model

- **The 200 videos** are the spine of the feed. They are the AI-selected
  best Jesus-gospel stories proving he is a good God. **STYLE RE-LOCKED
  2026-07-08 (Cameron's decision, overrides the June live-action lock):
  respectful ANIMATION, not photorealistic live-action.** Cameron watched
  the completed photoreal video #1 clips and rejected the look — the
  "fake AI" uncanny-valley feel was visible throughout and photorealism
  was also too expensive per usable clip. New direction: a beautiful,
  reverent animated/illustrated style (painterly storybook / warm 2D /
  sacred-art feel — exact style chosen from side-by-side tests, then
  locked into ONE master style block used on every clip of all 200 for
  consistency). Rationale: stylized art hides AI artifacts instead of
  exposing them, succeeds first-take far more often (cheaper per finished
  video), and reads as "made with care" rather than almost-real. 90
  seconds to 3 minutes, story-driven length
  (each takes the time its story needs; never padded, never capped short).
  Two-Voice Law applies (KJV red-letter Jesus voice + modern LDS-lens
  narrator). Every video carries its Seed question. The 200 stay MILK:
  their one job is showing Jesus is good. Bridge and meat live elsewhere.
- **Each video is paired with its linked KJV verse** displayed beneath it.
  The pair is displayed together but HONORED separately (section 2).
- **~100 verse-only items** (target pool) fill and vary the pages.
- **Page composition (every prescribed page):** 2 video+verse pairs,
  0–1 rare standalone verse, 1 question, 1 invitation at the bottom.
  200 videos ÷ 2 per page = ~100 pages of prescribed feed.
- **The 20-story opening bank stays text-only.** Cold-open stories have no
  video. Videos live in the feed only. (The 20 packs still lead video
  production — those stories are entries 1–20 of THE-200 — their videos
  just ship into the feed, not into onboarding.)
- **BRIDGE sprinkles (signal-gated, placed with care):** occasional
  non-story scriptures for users whose own words show readiness — e.g.
  1 Corinthians 15:29 (baptism for the dead), John 10:30 read against its
  Greek and against John 17 (oneness of purpose, distinct beings),
  Galatians 1:8 and the LDS scholarly responses to it. These require real
  study before writing — accuracy over cleverness, subtlety over argument.
  Never shown to users without signals. Never argued, only offered.
- **Member / self-proclaimed track:** users who self-identify interest in
  the restored gospel or membership see the SAME video pages (LDS-approved
  video content is a later phase) with MORE verse-only items drawn from all
  four standard works. Legal note (verified): the scripture TEXT of the
  KJV, Book of Mormon, D&C, and Pearl of Great Price is public domain; the
  Church's copyright covers modern study helps (footnotes, headings), which
  the feed never shows. Bare verse text is safe.
- **Prescribed order:** the flow moves God-is-good → Jesus atoned for you →
  subtle, gated invitations toward the Restoration, driven by
  self-proclaimed signals and the user's own words. If someone's words show
  they refuse restoration content, the prescription takes the hint and
  serves Jesus stories that respect where they are. Every story is placed
  for a purpose; the prescribed order is meant to be run through, not
  skimmed.

## 2. Honoring and replacement rules

"Honoring" = the user actually experienced an item:
- Video: watched to 100% (see section 3).
- Verse (paired or standalone): its link was opened and viewed.
- Question: answered or interacted with.
- Invitation: tapped/acted on.

Rules:
- **Video and its paired verse are honored separately.** Watch the video
  but skip the verse link → on scroll-away, the VIDEO moves to previous
  pages (and is logged on the profile); the VERSE recycles into the future
  pool and resurfaces later as a standalone reminder ("you watched this
  story — here is its verse"). The slot refills with a new pair.
- **Replacement trigger:** an honored item is replaced when the user
  scrolls away from it. If they scroll down and come back up, the slot
  already holds something new — interaction is rewarded instantly.
- **Un-honored items DO NOT move.** They stay on the home page. Ignoring
  the page and pressing next-page leaves the home page exactly as it was
  (one dot marks the ignored page); tapping the home icon returns to it.
- **Home page auto-refresh happens in exactly one case:** the user scrolled
  through the whole page, honored nothing, and left to a different tab.
  On return, the page is fresh.
- Design intent: reward viewing immediately, discourage quick swiping.

## 3. Video playback law

- Tapping a video starts full-screen playback with NO controls: no pause,
  no seek, no scrub, no skip. The app does nothing else until the video
  completes.
- Leaving the app (without closing it) pauses implicitly; on return the
  video rewinds 5 seconds and resumes.
- Fully closing the app = no credit; the video remains on the home feed,
  unwatched.
- Only a 100% watch counts as viewed → logged on the profile, honored per
  section 2.
- **Flagged risk (assistant's note, logged once):** media without a pause
  control can draw App Store review friction and accessibility complaints.
  Build to this spec first. If review ever rejects it, the pre-approved
  fallback that preserves the intent is: allow pause ONLY (still no seek or
  skip; a paused video earns nothing until finished). One flag in code
  should switch between the two behaviors.

## 4. Next-page wait ladder

- Waits per session for using next-page without honoring content:
  5s for attempts 1–3, 15s for 4–6, 30s for 7–9, then 60s, adding 60s for
  each attempt after that.
- **Resets every app session** (Cameron's choice).
- The wait is presented honestly as the page being prepared — never as an
  error, never as a spinner that looks broken.

## 5. Wheel navigation (the new feed chrome)

- Horizontal swipe wheel of pages. HOME (the current prescribed page) is
  the anchor.
- Swipe toward previous pages: the full re-viewable history, loads
  instantly. Everything ever honored lives here, in order, watchable again.
- Swipe toward next pages: allowed but ladder-delayed (section 4).
- **Dots along the bottom** accumulate — one per page created (including
  ignored pages). The home icon sits among the dots; tapping it always
  returns to the prescribed page fast (refreshed only per section 2 rules).
- **Deep links into previous pages:** a "saved item" in the Journal links
  straight to that item's spot in previous pages. Interactions and seed-
  question answers are logged on the Profile (with links). Chat discussions
  of an item live in chat history. Minimum guarantee: every 100%-viewed
  video is at least counted on the Profile.

## 6. Build order

1. **Master pairing list:** select the exact KJV verse(s) for each of the
   200 video entries; assemble the ~100-item verse-only pool; research and
   draft the BRIDGE sprinkle set (scholar-grade care).
2. **Feed engine rework (React Native, local-first SQLite):** page
   composer, honoring tracker, previous-pages archive, wheel navigation,
   wait ladder, deep links from Journal/Profile/Chat, signal-gated pools.
3. **Video layer:** expo-video full-screen locked player per section 3;
   Firebase Hosting `/story-videos/` streaming; offline → verse/text only.
4. **Wave-one video production** (packs 01–20; blocked only on Cameron's
   generator sign-in — Veo 3 recommended).
