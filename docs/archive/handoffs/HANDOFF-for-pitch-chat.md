# MBM — Full Handoff for a New Chat (focus: how to pitch this app to people)

Cameron is consolidating several confused chats into one clean chat. Paste everything
below into the new chat. It contains the full project state, what's done, what's left,
and every concern Cameron has raised, so the new chat can do its best with complete
information. The new chat's main job: figure out how to pitch/market this app to people.

---

## 1. Who Cameron is and how to work with him
- Cameron is non-technical and relies on the assistant to do almost everything technical.
- He hates being made to re-explain things already settled, and hates being treated like a
  first-time builder. Take initiative; check things yourself instead of asking him to.
- He has lost trust because past chats forgot established state (e.g., one chat treated
  Android publishing as brand-new setup and surfaced a "$25 Google fee" when Android had
  ALREADY shipped versions 3 and 4). Do not repeat that. Confirm current state from the
  project's own files/memory before claiming anything is undone.
- Plain language only, no jargon. Be honest about what genuinely needs Cameron (his
  passwords/payments) vs. what the assistant can do itself.

## 2. What MBM is (for the pitch)
- MBM = "Milk Before Meat." A mobile gospel-outreach app (React Native + Expo) for The
  Church of Jesus Christ of Latter-day Saints, modeled on how Christ ministered: meet a
  person exactly where they are, learn them over time, and move gently from foundational
  truth ("milk") toward the restored gospel ("meat") — never with visible gates, pressure,
  or shame.
- The experience: a calm "sanctuary" cold-open, then a short, beautifully told scripture
  story ending in one open question. The app quietly learns from answers and personalizes a
  feed. A real human is always one tap away ("Talk About It"). Nothing is ever labeled or
  waved in front of seekers — the routing is invisible.
- No login/account required to use it.
- Distinctives worth pitching: invisible, loving personalization (not corporate surveys or
  gates); story-first onboarding; a growing personal record of stories/answers on the
  Profile that pulls people back; always a real person available; it never argues doctrine —
  it lets Jesus' own words from scripture people already accept do the work.

## 3. Current published state (TRUE as of 2026-06-26)
- **iOS: SUBMITTED TO APPLE FOR PUBLIC APP STORE REVIEW.** Build 1.0 (build 6),
  WAITING_FOR_REVIEW, set to auto-release on approval. App Privacy declarations completed
  and PUBLISHED; App Review contact set. Nothing left for Cameron on iOS — just wait ~24h
  for Apple. Already on TestFlight too (public link exists).
- **Android: already shipped versions 3 and 4 in the past.** The newest corrected build
  (version code 5, containing all the latest UI fixes) is BUILT and ready as an `.aab` file.
  The only remaining step is uploading that file to Google Play Console — same as the prior
  Android releases. (Cameron already has the Google Play side set up; this is NOT new setup
  and there is NO new fee.)
- Everything is committed and pushed to GitHub (`main`), with no secrets leaked.

## 4. Fixes shipped in the latest build (what testers will now see)
- Cold-open animation no longer flashes the disclaimer first; it fades in smoothly.
- "Talk About It" chat header fixed for small screens: small square icon buttons (+ for new,
  clock for history), the "Real / Person" label stacked on two lines, title shrinks to fit.
- Profile no longer feels like surveillance: it plainly lists what the app keeps about you,
  each item removable — dropped the "here's what we noticed about you" framing.
- Ministry console (Cameron's admin desk) no longer freezes when Firebase hits its free
  daily limit; it also reads the database less often (cache + slower refresh).

## 5. Concerns Cameron has raised (carry these forward)
- **Trust / memory continuity:** chats keep losing the true state. He wants a reliable system
  so every new chat knows what's done before acting. (He's also creating a separate prompt
  specifically to fix the memory problem.)
- **Cost at scale:** he wants honest, upfront explanations of what running the app will cost
  as it grows (e.g., Firebase free-tier read limits; AI API costs) and no surprises.
- **AI model quality/tiering:** route harder/crisis questions to a stronger model, everyday
  chat to a cheaper one, with a safety allow-list so the phone can't request expensive models.
  Plan written in `MODEL-ROUTING-AND-OFFLINE-PLAN.md`. One API key can call any model.
- **Offline mode:** do NOT ship offline AI answers until their quality is measured against a
  steady threshold; he doesn't want low-quality answers going out unmonitored.
- **The build-vs-phone gap:** writing/committing code does not put it on a phone; a new build
  must be made AND installed. Several "missing fix" complaints traced to this.

## 6. What's left to do (project-wide)
- Android: upload the ready version-5 `.aab` to Google Play Console (short step).
- iOS: wait for Apple's review (~24h); it auto-releases on approval.
- Build the tiered model routing for real.
- Add a "Start fresh" reset on the Profile for testing; add a genuine belief/testimony answer
  option to dialogue questions so believers can testify instead of being boxed into doubt.

## 7. What the NEW chat should actually produce (the pitch task)
Cameron wants help figuring out how to pitch this app to people. Useful directions to explore
with him: who the first audience is (seekers, struggling/," falling-away" members, active
members wanting better-than-doomscrolling content, and people his friends/ward could share it
with); the one-sentence hook; a short "what it is / why it's different" description for word of
mouth and the TestFlight/store invite; how to invite first testers without it feeling pushy
(consistent with the app's own no-pressure ethic); and simple assets (a short blurb, a few
talking points). Ask Cameron who he most wants to reach first before writing the pitch.
