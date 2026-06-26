# MBM SESSION LOG — the never-ending chain link

**This is the running record of every work session on MBM. Newest entry is at the TOP.**

### How the chain works (read this if you're an AI assistant)
1. At the START of every new chat you MUST read the TOP entry below, then run
   `git log --oneline -5` and confirm the "Commit:" hash of that top entry appears
   in the history (proving that session was actually saved/pushed). Your FIRST
   message to Cameron must recap that last session and show that commit hash —
   proving you read the chain and that the previous session was saved. Do no other
   work until you've done this.
2. At the END of every session where anything happened, add a NEW entry at the top
   (copy the template), then commit and push to GitHub. That commit hash becomes the
   proof the session was saved, and the next chat verifies against it.
3. If the top entry's commit hash does NOT match `git log`, something wasn't saved —
   tell Cameron immediately instead of guessing.

### Entry template (copy this for each new session)
```
## YYYY-MM-DD — <one-line title>
- What we did:
- What changed in the app (files/commits):
- What is now true that wasn't before:
- What's next / handed off:
- Commit: <hash filled in after you commit>
```

---

## 2026-06-26 — iOS SUBMITTED TO APPLE FOR PUBLIC REVIEW (App Privacy published)
- What we did: Finished the last iOS blocker and pushed the app to public App Store review.
  Completed and PUBLISHED the App Privacy data-usage label in App Store Connect (the one
  thing the API couldn't do): declared 4 data types — Name, Sensitive Info (the religious
  faithNote), Other User Content (inbox messages), User ID (anon Firebase UID) — each as
  "App Functionality", linked to the user's identity, used for NO tracking. Basis came from
  reading messaging.ts (Firebase persistently stores those tied to an anonymous UID; the
  Anthropic chat is real-time so it isn't "collected"). Then via the ASC REST API: added the
  version item to the review submission (201, READY_FOR_REVIEW — no blockers left) and
  PATCHed submitted:true.
- What changed (files/commits): no app CODE change. Docs/config only: START-HERE.md updated
  to reflect iOS submitted; new ANDROID-PUBLISH-PATH.md; auto-memory updated.
- What is now true that wasn't before: **iOS v1.0 (build 6) is WAITING_FOR_REVIEW at Apple**,
  releaseType AFTER_APPROVAL (auto-goes-live on approval). App Privacy is PUBLISHED. The
  entire iOS store side (metadata, screenshots, age rating, pricing, contact, privacy,
  submit) was driven without a Mac and without browser uploads.
- What's next / handed off: iOS — just wait for Apple (~24h typical). Android to go public
  needs two owner-only things from Cameron: (1) round up 12 testers for the 14-day closed
  test, (2) download one Google Play service-account key and hand it to me. See
  ANDROID-PUBLISH-PATH.md. Public Android is ≥2 weeks out by Google's rule regardless.
- Commit: 137726d

## 2026-06-26 — Double-check pass found & fixed a MEAT LEAK (non-members saw meat)
- What we did: Cameron said "double check everything." Re-verified the whole three-way
  routing against the actual files (not trusting prior claims). Found a real bug:
  free-text onboarding (`inferTagFromText`) keyword-guessed the feed tag and sent
  generic Christian words (faith/church/gospel/grow/scripture) to MAINTENANCE — which
  shows the MEAT track. A Baptist/Catholic typing their faith in the opening free-text
  box would have seen meat on their very first feed. That broke milk-before-meat AND
  Cameron's law that ONLY Latter-day Saint membership flips the flow.
- What changed in the app (files/commits):
  - `inferTagFromText` now routes free text through the SAME guarded path everything
    else uses — `harvestSignals -> routeFeedTag` — so the founding entry obeys the
    LDS-only member guard and the bridge-acceptance rule. (useAppStore.ts)
  - chatEar: split sentences on semicolons too, so a negated clause can't silence a
    real acceptance in the next clause and vice versa.
  - chatEar: detect the exact contradiction Cameron named — God does NOT damn people
    for His glory — guarded so a Calvinist AFFIRMING the harsh view stays on milk.
- What is now true that wasn't before: Every non-LDS tradition starts on milk, the way
  Jesus would treat them the same. Only explicit LDS self-ID reaches the member/meat
  track. Verified: tsc 0; 18/18 route cases pass (Baptist/Catholic->MILK, LDS->
  MAINTENANCE, ambiguous "mission/priesthood" don't mint membership, third-person &
  negation guarded, bridge acceptances->BRIDGE, Calvinist affirming harsh view->MILK).
- What's next / handed off: re-shipped corrected OTA + new build (the earlier 80b009d
  OTA/build were pre-fix and must be replaced on the phone).
- Commit: cb9ac2b

## 2026-06-26 — Three-way stage structure: member / bridge / milk, the Jesus way
- What we did: Implemented Cameron's full ministering structure and tightened member
  detection to exactly one religion, per his correction.
- What changed in the app (files):
  - `mobile/src/engine/chatEar.ts` — added two bridge-acceptance signals
    (`accepts_ongoing_revelation`, `rejects_creation_ex_nihilo`) to VALID_REPORT_TOKENS
    and harvestSignals (affirmation-only, negation-guarded); TIGHTENED member markers to
    be unambiguously Latter-day Saint (dropped bare "served a mission" / "hold the
    priesthood" which other faiths use).
  - `mobile/src/engine/connect.ts` + `connect.py` (kept in sync) — added `BRIDGE_SIGNALS`
    + `bridgeReady()`; added `accepts_ongoing_revelation` to the milk gate's openness set.
  - `mobile/src/store/useAppStore.ts` — rewrote `routeFeedTag` to the three-way structure
    (member→MAINTENANCE, gate+consent→RESTORATION, bridgeReady→BRIDGE, else MILK) and
    REMOVED the old wrong "analytical doubt → BRIDGE"; biased the BRIDGE content pool to
    the question-sparking `restoration` milk track; injected a bridge note into the chat's
    LIVE GUIDANCE; humanized the two new signals for the Profile.
- What is now true that wasn't before: ONLY membership in The Church of Jesus Christ of
  Latter-day Saints flips the app into member/meat mode — every other tradition is treated
  the same. A non-member moves into the BRIDGE only by accepting a distinctively-LDS truth
  in their own words (God isn't cruel for His glory, God still speaks, creation organized
  not made from nothing); on the bridge the feed and chat steer a little harder toward the
  Restoration while still never naming the Church before the milk gate.
- Verified: tsc 0, web export 0, feed_test ALL PASS, connect.py self-test passed, node
  regex tests (member-only + bridge acceptances, with negation/third-person) ALL PASS.
- What's next / handed off: this is IN CODE; kicking off a new build so it reaches the
  phone. Future: build the deeper member "meat" learning sections + more bridge ministering
  functions/content.
- Commit: 5152c22

## 2026-06-26 — Member recognition FIXED + reset/public-release rules rewritten
- What we did: Fixed the app's #1 broken behavior — editing the faith box on the
  PROFILE to say "I am a member of the Church of Jesus Christ of Latter-day Saints"
  was being IGNORED instead of snapping the app into member/meat mode. Also confirmed
  the chat-header and iPhone-animation complaints are already fixed in code (old build
  on the phone), and rewrote two of Cameron's rules (reset + public-release promise).
- What changed in the app (files):
  - `mobile/src/engine/chatEar.ts` — broadened member self-ID phrasings in
    `harvestSignals` + added negation/third-person guards (Law 8 honored).
  - `mobile/src/store/useAppStore.ts` — `editFaithWord`, `addFaithWord`, and
    `recordFaithBackground` now detect `becameMember`, enable discipleship, push a
    "Welcome, fellow Latter-day Saint" moment, and `appendMetaMessage` to chat — the
    same member handling the chat path already had.
  - `mobile/src/screens/FeedScreen.tsx` — visible gold "Walk with Christ" banner on
    the home feed whenever the person reads as a member; taps into Discipleship.
  - `START-HERE.md` — removed the "Start fresh" reset idea (decided against; users
    remove/edit individual items instead); rewrote the public-release rule into a sworn
    promise that the assistant does everything up to the single legally-required tap and
    points Cameron right at it; logged the member fix; bumped date to 2026-06-26.
  - `.auto-memory/MEMORY.md` — recorded the member fix, the two-stage non-member design
    (unbeliever/milk vs bridge) + member meat track, the reset decision, the promise.
- What is now true that wasn't before: editing the Profile faith box to declare LDS
  membership snaps the whole app into member/meat mode (feed → MAINTENANCE, discipleship
  companion on, visible banner, chat acknowledgment) and it fires from any faith-write
  path or from chat. Verified: regex unit test all-pass (7 yes / 6 no) + `tsc --noEmit` 0.
- What's next / handed off: these fixes are IN CODE but NOT on Cameron's phone yet — they
  need a new build (or `eas update` for the JS-only parts) to land. The header/animation
  complaints clear with that same build. Larger follow-up: build out the deeper member
  "meat" learning sections and the bridge-stage ministering functions.
- Commit: 6dc061c (+ this log update committed right after)

## 2026-06-26 — Built the memory chain so chats stop losing context
- What we did: Diagnosed why new chats kept losing the project's true state and
  repeating stale facts (the "create a Google Play account / pay $25" mistake).
- Root cause found: `.auto-memory/MEMORY.md` (June 19) still listed Google Play as
  "pending ($25+ID)", and there were 24+ competing status/handoff docs with no clear
  winner, so chats trusted whichever stale file they read first.
- What changed:
  - Fixed the stale "pending Google Play $25" line in `.auto-memory/MEMORY.md` and
    added a banner pointing to START-HERE.md as the truth.
  - Rebuilt `START-HERE.md` into the single dated current-state file (accounts all
    exist; iOS on TestFlight; Android internal testing v3/v4 shipped, v5 built; the
    "code committed != code on phone" build gotcha; file-authority hierarchy).
  - Pointed `CLAUDE.md` (auto-loaded) at START-HERE.md first.
  - Created `SESSION-OPENER.txt` (paste-at-start checklist) for Cameron.
  - Created this `SESSION-LOG.md` chain and the start-of-chat recap protocol.
- What is now true that wasn't before: there is one dated source of truth, the stale
  Google Play lie is gone, and every future chat is instructed to open by recalling
  the last session from this log and verifying it against git.
- What's next / handed off: (optional) move the old contradicting status docs into an
  /archive folder; the written-but-not-built items remain — tiered model routing,
  Profile "Start fresh" reset, belief/testimony dialogue option.
- Commit: 16f2d65 (system created) — see also the follow-up commit that recorded this hash
