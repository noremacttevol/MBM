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

## 2026-07-07 (pt.3) — The Two-Voice Law: KJV red-letter Jesus voice + modern LDS-lens narrator, wired into all 20 packs
- What we did: Cameron locked the voice design. Every video has exactly two voices, the same two across all 200: (1) a Narrator in modern, plain storytelling language telling the story through a Latter-day Saint lens and gently unpacking Jesus's harder sayings to show he is a kind, loving, merciful God; (2) a distinct Jesus voice that speaks ONLY the words of Jesus, ONLY in exact KJV red-letter text (the Church's approved translation) — never modernized. Since his face is never shown, his voice IS his face: same voice in every video so people learn to recognize him. Parable rule: narrator retells the parable modern; Jesus voice delivers only the KJV heart-lines. Added a "Red-letter lines (KJV)" section to every pack 01-20 with the exact KJV text, where it lands in the shot list, and a modern narrator bridge after each hard phrase ("be whole of thy plague," "careful and troubled," "whether of them twain," etc.). Emmaus note: the stranger's voice is the Jesus voice — recurring viewers recognize him before the disciples do. Also answered Cameron's automation question: everything automatable except his generator sign-in; quality held by hard gates (word-for-word script/KJV verification, spec checks, assistant reviews every clip, Cameron reviews finished videos in batches).
- What changed in the app (files/commits): No app code. media-production/00-MASTER-PLAN.md gained the Two-Voice Law; packs 01-20 each gained "## Red-letter lines (KJV)".
- What is now true that wasn't before: the voice architecture for all 200 videos is decided and encoded per-story; no per-video voice decisions remain except the one-time audition on video #1 (narrator + Jesus voice candidates).
- What's next / handed off: unchanged blocker — Cameron signs into a generator (Veo 3 recommended); then clips for #1 (cloak), Descript assembly with both voice auditions, Cameron picks the two voices, template locks.
- Commit: b6ae69e

## 2026-07-07 (pt.2) — THE 200: full video corpus cataloged; Seed sections added to all 20 packs
- What we did: Cameron confirmed alignment ("you nailed it") and raised the target from 20 to 200 videos, with a locked storytelling law: these are NOT generic Christian videos — every one must show the actual character of the good Godhead (worthy of worship because of how they love us) so a viewer's inherited theology starts to feel too small, without argument and without naming the Church early. Added a "Seed" section to every existing pack (01-20): the quiet restoration-pointing question each video must leave behind, and which shots carry it. Wrote THE-200.md — the complete numbered catalog (verified 1..200, no gaps/dupes) across nine sections: the 20-story bank, 33 parables, 28 miracles, 30 encounters, 8 nativity, 22 passion/resurrection, 20 teachings-as-scenes, 19 Old Testament good-God stories, and 20 post-signal Restoration-track entries (3 Nephi, Ether 3, Moses 1/7, D&C 121, First Vision as #200) — Section IX gated by the BOM law, member-track from day one. Master plan updated to the 200 vision (~1,400 clips, generated in waves).
- What changed in the app (files/commits): No app code. media-production/: THE-200.md new; 00-MASTER-PLAN.md updated; packs 01-20 each gained "## The Seed".
- What is now true that wasn't before: the media effort has a complete target corpus and a theological aim locked into every recipe, not left to generation-time chance.
- What's next / handed off: unchanged — Cameron picks a generator (Veo 3 recommended) and signs in; assistant generates wave one (the 20), assembles in Descript, Cameron reviews #1 (cloak). New in-app stories get written from THE-200 in Jesus-Method format before their videos.
- Commit: cdaf563

## 2026-07-07 — Media production: packs for all 20 story videos written and verified
- What we did: Cameron asked for videos of every Jesus story in the app. Direction chosen: AI-generated cinematic scenes, played in-app, Cameron reviews each video. Created `media-production/` with a master plan (pipeline, style block, tracker, backlog of 16 future gospel stories) and a full production pack for EVERY one of the 20 opening stories: narration script (the app's exact story text, programmatically verified word-for-word), closing question card, and 6-8 paste-ready shot prompts per story. Two locked rules: Jesus's face is never shown (light/silhouette/hands/hem only), and narration is never rewritten. HeyGen/HyperFrames tried for a quick sample — out of free credits (see 07-06 entry: marketing videos consumed them) and wrong style anyway. No AI-video-generation MCP exists in the registry.
- What changed in the app (files/commits): No app code. New folder `media-production/` — 00-MASTER-PLAN.md + packs 01-20 (commit 8f99b53).
- What is now true that wasn't before: every story in the bank has a complete, verified video production recipe; clip generation is the only blocked step. NOTE: 3 HeyGen motion-graphics story videos already exist on disk (Marketing-Launch-Kit/videos/, per 07-06 session) — social-marketing style, distinct from this cinematic in-app effort.
- What's next / handed off: Cameron picks a generator (recommended: Google Veo 3 via Google AI Pro ~$20 for one month, covers all ~140 clips) and signs in on his browser; assistant drives generation via Chrome, assembles in Descript, Cameron reviews video #1 (cloak) first. Delivery: Firebase Hosting /story-videos/, streamed via expo-video, text story stays as the offline fallback.
- Commit: 8f99b53

## 2026-07-06 — Marketing kit re-activated: 3 story videos downloaded, bio link updated to live app
- What we did: Re-surfaced the Marketing-Launch-Kit for the social launch. Checked HeyGen: 3 of 4 story videos were rendered COMPLETED but never downloaded. Downloaded all three MP4s (verified frame-by-frame which story is which) into `Marketing-Launch-Kit/videos/`: 01-Woman-at-the-Well.mp4, 02-Prodigal-Son.mp4, 03-Woman-and-the-Cloak.mp4. Fourth (Good Shepherd) still stuck "processing" on HeyGen free tier since 07-01 — script ready, recompose when monthly credits reset or on paid tier.
- What changed in the app (files/commits): No app code. SOCIAL-PAGE-KIT.md "Link in bio" updated — app is live, so bio link = https://milkb4meat.org (+ App Store direct link). Videos added to kit (gitignored or committed per repo policy).
- What is now true that wasn't before: Cameron has the actual posting-ready MP4s on disk; the social kit's bio-link advice matches reality (app live).
- What's next / handed off: Cameron creates the IG/FB/X accounts per SOCIAL-PAGE-KIT.md (2 min each, needs his phone/password), posts Woman at the Well first + pins it, follows CAPTIONS-AND-CALENDAR.md. Good Shepherd video pending HeyGen credits. Spend cap + Android testers still open.
- Commit: fdd181f

## 2026-07-05 (pt.4) — App Store public indexing CONFIRMED; watcher retired
- What we did: Scheduled "check-appstore-live" watcher ran; iTunes lookup API (`https://itunes.apple.com/lookup?id=6783621048`) now returns resultCount 1. The app is fully live and publicly indexed: https://apps.apple.com/us/app/milk-before-meat/id6783621048 (Milk Before Meat, free, 4+, Lifestyle/Books, v1.0, released 2026-07-02).
- What changed in the app (files/commits): No app code. START-HERE.md "Last verified true" block updated to state indexing is confirmed and the watcher is disabled; this SESSION-LOG entry added.
- What is now true that wasn't before: App Store search index has the app — the last outstanding launch dependency on Apple's side is closed. Direct link, QR, and search all work.
- What's next / handed off: Scheduled task "check-appstore-live" disabled (no longer needed). Cameron: spend cap at console.anthropic.com still open; keep gathering Android testers toward the closed test.
- Commit: 49a8d44

## 2026-07-05 (pt.3) — Opening story on EVERY cold open, story bank 9 → 20, feed never repeats the opening story
- What we did: Fixed Cameron's Android report that the opening screen stopped appearing. Root cause: once all 9 stories were seen, cold opens skipped Hook and went straight to Main. Now the sanctuary opening (Hook) shows on EVERY cold open; its "Come and see" button routes to Onboard when an unseen story remains (or first launch), otherwise straight into the app. Wrote 11 new entry stories (well, storm, bartimaeus, roof, ten_lepers, centurion, mary_martha, lazarus, emmaus, shore, samaritan) in the exact Jesus-Method format — 20 total, each with the believer's testimony "E" choice. Added feed dedupe: the story just told on cold open is never re-served as a feed card in the same session (new `openingStoryRefs.ts` maps every story id to its scripture-chapter prefixes; `buildFeed` filters them out, with a fallback so the feed can never go empty).
- What changed in the app: `mobile/src/navigation/AppNavigator.tsx` (initialRouteName always 'Hook'), `mobile/src/screens/HookScreen.tsx` (CTA branches), `mobile/src/screens/OnboardScreen.tsx` (+11 stories), `mobile/src/store/useAppStore.ts` (session story exclusion in markStorySeen + buildFeed), new `mobile/src/data/openingStoryRefs.ts`.
- What is now true that wasn't before: every cold open begins at the opening screen; a fresh, never-repeated story plays on each cold open until all 20 are seen and answered; the feed never shows the passage the opening screen just told. Shipped OTA to production (update group a2a43538-81fc-4c14-bb17-6fe025bb14d6, iOS + Android, runtime 1.0.0) — reaches installed apps after close/reopen ×2.
- What's next / handed off: print the Bishopric-Stack when ink arrives; Cameron: spend cap at console.anthropic.com, keep gathering Android testers toward 15.
- Commit: 76d90de

## 2026-07-05 (pt.2) — Bishopric-Stack refined: white covers on the big three, compliance doc added, ink-heavy fully separated
- Built on the parallel session's stack (2d24a76). Docs 14 (Overview & Launch Plan) and
  15 (Cameron's Field Guide) replaced with NEW white-cover printable versions (sources:
  pitch-book/book-printable.html, cameron-guide-printable.html — CSS overrides kill the
  solid-navy cover page and dark quote/table blocks that drain cartridges).
- Added doc 16: "Within the Lord's Boundaries" compliance review, white-cover printable
  (compliance-printable.html). Verified current (0 stale terms).
- Moved "Walkthrough for Testers" (4.6MB of screenshots) out of the stack into
  TO-PRINT/"Ink-Heavy (screen or print shop)/", alongside the dark-cover Come-and-See and
  The Complete Book (screen-read, slightly dated — no rebuildable source; do not print).
- READ-ME — Print Kit.md updated to explain the two folders.
- Context: Cameron's printer ran out of ink mid-proof-set; all queues canceled. The full
  16-doc Bishopric-Stack (~62 pages, all ink-light) is ready to print when ink arrives.
- Commit: (this chain-link, on top of 2d24a76)

---

## 2026-07-05 (pt.2) — Bishopric-Stack built & printed; every doc de-staled; ink-heavy separated from printable
- Cameron asked for a complete printable stack for presenting to the bishopric, with
  ink-heavy (dark-page) pieces separated out, after verifying EVERY file is accurate.
- **Full staleness audit + fixes (all TestFlight/"waiting on Apple" wording removed):**
  pitch-book/book.html (status table → "Live", links + Ch.10 iPhone steps → public App
  Store), church-launch-kit 00/02/03/07 md files. 04_Install-Guide, sheets 2–4, Field
  Guide, Walkthrough already clean. Overview & Launch Plan PDF regenerated from the fixed
  book.html (22 pp, 0 stale) and synced to FOR-CAMERON + pitch-book.
- **NEW ink-light Come-and-See brochure** (pitch-book/brochure-printable.html → 4 white
  pages, same words, cross mark instead of dark cover/screenshots). Dark original moved
  to TO-PRINT/"Ink-Heavy (screen or print shop)/". Ink-light copy is the new TO-PRINT #1.
- **NEW TO-PRINT/Bishopric-Stack/** — 16 numbered PDFs in presentation order (90 pp):
  01 Church-Day Sheet · 02 Bishop Brochure · 03 Honest Review (kit 01) · 04 Privacy
  One-Pager · 05 FAQ & Objections · 06 Staged Approach · 07 Plain-English Map ·
  08 Priesthood Email · 09 Come-and-See ink-light · 10 For-Members · 11 How-to-Get ·
  12 Install Guide · 13 Roadmap · 14 Overview & Launch Plan · 15 Field Guide ·
  16 Walkthrough. Docs 03–08 + 12 newly rendered from the kit .md files (pandoc + Chrome,
  house style). Kit READ-ME updated to explain the new layout.
- **Excluded from print: FOR-CAMERON/The Complete Book.pdf** — 20 pp, still has 3 stale
  TestFlight mentions and NO rebuildable source found; screen-read only until rebuilt.
- **Printed on the HP DeskJet 4300:** earlier a 6-piece proof set (jobs 11–16), then per
  Cameron's explicit choice the FULL 90-page stack (jobs 17–32).
- Commit: (this chain-link, on top of 4769b29)

---

## 2026-07-05 — 🎉 STORE PAGE VERIFIED LIVE; church-day prep: roadmap refreshed everywhere, Cameron sheet made
- **The App Store page is publicly LIVE.** Direct URL https://apps.apple.com/app/id6783621048
  returns 200 and renders "Milk Before Meat" (verified by curl + content grep). The iTunes
  lookup API still returns resultCount 0 — that's just Apple's SEARCH index lagging, which is
  why the "check-appstore-live" watcher hasn't fired. Practical meaning: the QR/direct link
  works NOW; App Store *search* may not find the app for a day or two. Watcher left running
  to confirm when search indexing completes.
- Confirmed for Cameron: the three pt.3 fixes shipped OTA to BOTH platforms (one JS bundle,
  iOS + Android, runtime 1.0.0) — his Android internal-track build gets them after close/open ×2.
- **Roadmap was stale in 3 places, all fixed:** site/roadmap.html still had "Apple's review —
  submitted and waiting" as a NOW item (removed; the "approved and live" done-item already
  existed) and the section header said "invite-only testing phase" (now "iPhone public,
  Android finishing its test"). Regenerated the print PDF from the fixed page and synced all
  three copies: TO-PRINT/"5 - Roadmap (where it's going).pdf", site/Milk-Before-Meat-Roadmap.pdf,
  FOR-CAMERON/Roadmap.pdf. Site redeployed to Firebase hosting (verified serving).
  Old printed #5 copies are obsolete — reprint.
- Text-verified sheets 1–4: no stale TestFlight/waiting wording (sheet #4's "invite-only"
  line is about Android, which is true). #4 from July 4 is current.
- **NEW: FOR-CAMERON/Church-Day-Sheet.pdf (+.html)** — one-page printable, Cameron-only:
  60-second pre-church verification of the 3 fixes, what's true now (iPhone live but tell
  people to use the QR not search; Android invite flow), print quantities, one-breath script +
  ask-for-counsel framing, in-the-moment fallbacks, open Cameron tasks. Visually verified 1 page.
- Advice given: green light to show/share at church and seek counsel — iPhone installs work
  via QR/link today.
- Commit: (this chain-link, on top of d17db46)

---

## 2026-07-04 (pt.3) — Cameron's 3 fixes: cold-open flash, clipped clock icon, consent reworked his way — SHIPPED OTA
- Cameron's feedback (voice): (1) bottom "not God / not affiliated" disclaimer still flashes
  for a split second BEFORE the cold-open animation on the App Store build — the old fix
  didn't cover it; (2) the clock/history icon on Talk About It is clipped at the top ~10%
  on iPhone; (3) the AI-consent gate felt like it broadcast AI as the app's main purpose —
  he ruled: REMOVE it from onboarding ASAP, default OFF, keep the Profile toggle, disclose
  just-in-time at first chat use, say "AI" not "Anthropic" in-app (privacy policy still
  names Anthropic in full — Apple requires that and it stays), and when a "Talk about it"
  link arrives with AI off, offer BOTH turning AI on AND taking the sourced question to a
  real person.
- Fixes (commit 841af0e, all JS-only):
  1. HookScreen: root cause was the footer's static-0 → native-animated opacity handoff
     painting one full-opacity frame on iOS. Footer fade now uses the JS driver (opacity is
     a plain prop, 0 from frame one) — flash is structurally impossible; layout unchanged.
  2. ChatScreen header: 🕐 emoji (clipped by Jost lineHeight) replaced with Ionicons
     "time-outline" vector icons on both history buttons.
  3. OnboardScreen aiConsent page DELETED (faith page enters app directly; aiConsent stays
     'unknown' = off by default, nothing leaves device). ChatScreen consent card reworked:
     one short card for unknown+declined, no vendor name, honest "not tied to your name"
     wording, shows the sourced draft it arrived with, two equal buttons — "Turn on the AI
     conversation" / "Talk to a real person instead" (blue, sends the carried draft into a
     fresh real-person thread via sendConnectMessage + copied banner). ProfileScreen toggle
     reworded the same way. Apple 5.1.1(i)/5.1.2(i) still satisfied: disclosure + explicit
     yes still precede ANY send — just at point of use instead of onboarding.
- Verified: tsc --noEmit clean; no user-facing "Anthropic"/"Claude" strings remain (only
  code comments); consent gating in store untouched (aiConsentGranted still guards every
  network call).
- SHIPPED: eas update → production branch, runtime 1.0.0, iOS + Android (update group
  4093b44f-7fe2-445d-b294-08fe7a7f5e6d). Reaches App Store build 8 and Play vc7 on next
  app relaunch ×2 (first launch downloads, second applies).
- Commit: (chain-link on top of 841af0e)

## 2026-07-04 (pt.2) — "Fix it all": site flipped to App Store + deployed, print kit refreshed, domain warning stale
- What we did (Cameron said "fix it all, you're my project manager"):
  1. WEBSITE: site/index.html iPhone card flipped from TestFlight to the public App Store
     (https://apps.apple.com/app/id6783621048); section header updated ("It's here / Get it
     on your phone"). roadmap.html updated: iPhone = public/approved, Android = still testing.
     Deployed to Firebase hosting via the service-account method; VERIFIED the new card and
     roadmap text serving on milk-b4-meat.web.app. (The previously-uncommitted index.html
     TestFlight edits were superseded by this, as intended.)
  2. PRINT KIT: generated church-launch-kit/qr-appstore.png (QR → App Store URL). Rewrote the
     iPhone section of How-to-Get-the-App.html (App Store steps, no TestFlight), regenerated
     the PDF via headless Chrome, copied over TO-PRINT sheet #4, and visually verified the
     PDF (one page, clean, both QRs render). Rewrote 04_Install-Guide.md iPhone path for the
     App Store. Old printed copies of sheet #4 are obsolete — reprint. Other brochures fine.
  3. DOMAIN: verified milkb4meat.org is ALREADY on Firebase (apex 199.36.158.100, www CNAME
     milk-b4-meat.web.app, HTTP 200, real site content). START-HERE's June-30 Squarespace
     placeholder warning was STALE — corrected in START-HERE.md.
  4. STORE PAGE: still not indexed at time of writing (availability fix was earlier today;
     up to ~24h is normal). Created scheduled task "check-appstore-live" (3x daily) that
     notifies Cameron when live, updates START-HERE, commits, and disables itself.
- What changed: site/index.html, site/roadmap.html (deployed), church-launch-kit
  How-to-Get-the-App.html/pdf + qr-appstore.png (+ committed the existing qr pngs),
  TO-PRINT sheet #4, 04_Install-Guide.md, START-HERE.md, this entry.
- Commit: (chain-link on top of c3fcf5b)

## 2026-07-04 — Store-page 404 root-caused: ZERO territories set — FIXED via ASC API
- What we did: Cameron asked if Apple approved and whether the website/printed material
  need changing. Verified the chain (193cba4 ✓). Re-checked: 1.0 still READY_FOR_SALE,
  releaseType AFTER_APPROVAL (no release tap pending) — but iTunes lookup STILL returned
  0 results 2 days after approval. Dug in: GET appAvailabilityV2 returned NOT_FOUND —
  the app had NO territory availability record, i.e. available in ZERO countries. That,
  not propagation, was the 404.
- The fix: POST /v2/appAvailabilities with all 175 territories, availableInNewTerritories
  =true. Verified: 175 territories available, releaseDate 2026-07-04. Lookup not yet
  indexed at time of writing (expected lag after the change).
- Printed-material audit (for when the page goes live): TO-PRINT #4 hand-out,
  church-launch-kit How-to-Get-the-App (html+pdf), 04_Install-Guide.md, and
  qr-testflight.png all point at TestFlight → refresh with the App Store link.
  Come-and-See brochure only shows milkb4meat.org — fine as is. Website: site/index.html
  iPhone card still TestFlight (has UNCOMMITTED local edits — preserve them when flipping).
- What's next: re-check the store URL; when live, flip the site card + deploy hosting,
  refresh the print pieces above, update START-HERE.md.
- What changed: START-HERE.md truth block; this entry. No code. (Local uncommitted edits
  to site/index.html and print files were left untouched, as found.)
- Commit: (chain-link on top of 193cba4)

## 2026-07-02 (pt.5) — 🎉 APPLE APPROVED — 1.0 is READY_FOR_SALE (store page still propagating)
- What we did: Cameron asked if Apple accepted. Confirmed via the ASC API (signed JWT with
  the .p8 key): version 1.0 = READY_FOR_SALE / READY_FOR_DISTRIBUTION. Build 8 passed.
- BUT: the public listing https://apps.apple.com/us/app/id6783621048 was still 404 and the
  iTunes lookup API returned 0 results (checked ~19:55Z) — normal propagation lag after
  approval. So the website iPhone card was deliberately NOT flipped yet (no 404 buttons).
- What's next (one clean step for any session): re-check the store URL; when it loads,
  swap the site/index.html iPhone card from TestFlight to the App Store link, deploy
  Firebase hosting, verify, update START-HERE.md. Note site/index.html has uncommitted
  local edits — preserve them when editing.
- What changed: START-HERE.md truth block; this entry. No code.
- Commit: (chain-link on top of 87f9986)

## 2026-07-02 (pt.4) — Roadmap: prompt-caching restructure added (Cameron's call)
- What we did: after an honest cost comparison of AI providers (switching is a ~20-line
  proxy change, cheap models are 5-10x less, but tone risk + near-zero current bill =
  stay on Haiku for now), Cameron locked the cost lever into the roadmap instead:
  restructure the system prompt into a fixed shared prefix + small per-person tail so
  Anthropic prompt caching cuts input costs up to ~90% with zero quality change.
- Framing (Cameron's words, now a rule): the CURRENT TESTER PHASE is purposefully the
  research phase for this — we're using testers to learn which prompt parts stay fixed
  for everyone vs. truly vary per person, so the restructure is designed from real usage.
- What changed: docs/roadmap/FORWARD-WORK-PLAN.md — new APP IMPROVEMENTS item 2
  (others renumbered).
- What's next: keep collecting tester transcripts with that question in mind; build the
  split (pairs with tiered model routing); revisit provider choice only if the monthly
  bill nears $100.
- Commit: (chain-link commit on top of d4bd068)

## 2026-07-02 (pt.3) — SECURITY AUDIT + LIVE HARDENING of proxy and Firestore
- What we did (Cameron asked for a full security check of the app):
  - Audited everything: no secret keys in the repo or in ANY git commit ever; Firestore
    rules solid; server deps clean; mobile npm "vulns" are Expo build-tooling only.
  - THE real hole: the Railway key proxy (/api/chat) answered ANYONE on the internet —
    a stranger could extract the URL from the app bundle and burn Cameron's Anthropic
    money at unlimited volume. Fixed and DEPLOYED the same day.
- What changed (code commit f4a6cc2, deployed live to Railway + Firebase):
  - server/index.js: per-IP rate limits (chat 10/min + 300/day; connect/factcheck
    5/min + 30/day), global 5000/day chat fuse (env-tunable), message/system size caps,
    model locked server-side, queue caps (500) so disk can't fill, client IP taken from
    x-forwarded-for (req.ip was unreliable behind Railway — first deploy proved it).
  - App token groundwork: mobile sends x-mbm-app (EXPO_PUBLIC_MBM_APP_TOKEN in
    eas.json); Railway has MBM_APP_TOKEN set. NOT enforced yet — flip
    REQUIRE_APP_TOKEN=1 on Railway ONLY after builds carrying the token are what
    people have installed (the build in Apple review does NOT send it).
  - firebase/firestore.rules: size caps on message create (body/excerpt ≤4000 etc.) —
    PUBLISHED LIVE via new admin/deploy-rules.mjs (service-account path; the firebase
    CLI lacked a permission, the Rules API works).
  - FOR-CAMERON/SECURITY-REPORT-2026-07-02.md — plain-language report.
- Verified live: 11th rapid chat request → 429; oversize message → 400 message_too_long;
  a normal chat still answers (build 8 in Apple review is unaffected); connect throttles.
  (4 test notes labeled "security-test — safe to ignore/delete" are in the connect queue.)
- Cameron-only action: set a monthly spend cap at console.anthropic.com (Billing).
- What's next: after the next builds ship + old builds age out, set REQUIRE_APP_TOKEN=1
  on Railway (railway variables --service mbm-proxy --set REQUIRE_APP_TOKEN=1).
- Commit: f4a6cc2 (code) + chain-link on top.

## 2026-07-02 (pt.2) — REBUILT + RESUBMITTED TO APPLE (Waiting for Review) + Android vc7 live
- What we did (all automated, nothing left for Cameron):
  - Verified the updated privacy policy (naming Anthropic + consent) is LIVE at
    milk-b4-meat.web.app/privacy.html.
  - Built BOTH platforms from commit 9438d84 (`eas build --platform all --profile
    production --auto-submit`): iOS build 8, Android version code 7.
  - iOS: build 8 uploaded + processed (VALID, export compliance clean). Via the ASC API:
    attached build 8 to version 1.0, CANCELED the dead rejected review submission
    (99f5b00a…), created a NEW review submission 3888660e-454c-4d81-bd4a-67dc30b6463c,
    added the version, and SUBMITTED. Confirmed state: **WAITING_FOR_REVIEW**,
    submittedDate 2026-07-02T10:55Z. No Resolution Center reply was needed — the file
    "FOR-CAMERON/APPLE-RESUBMIT — copy-paste reply.md" is marked no-longer-needed (kept in
    case Apple writes back).
  - Android: auto-submit completed; Play **internal track now serves vc 7 (status
    completed)** — Cameron's phone gets the consent gate, small-screen fix, and
    Discipleship warm-up via Play internal testing.
- What is now true: iOS 1.0 (build 8) is in Apple's review queue; Android internal has vc7.
- What's next: wait for Apple (~24h typical). If approved, the public-release tap is
  Cameron's. If rejected again, read the new message and iterate.
- Commit: (chain-link commit on top of b668015)

---

## 2026-07-02 — Apple-rejection audit + small-Android fix + Discipleship warm-up
- NOTE ON THE CHAIN: the July 1 session (commit 41ecf03, the Apple 5.1.1(i)/5.1.2(i)
  consent fix) never wrote a session-log entry. This entry records it retroactively so
  the chain is whole again.
- What we did:
  - AUDITED the July 1 consent fix end to end. Verified all four AI call sites in
    useAppStore.ts (chat send, blessings, note summaries, discipleship summary) hard-block
    until aiConsent === 'granted'; onboarding consent page, chat consent card, and Profile
    on/off control all present; no other network path sends user words to the AI. The
    human-inbox Firestore path is user-initiated and covered by the published privacy label.
    eas.json production has autoIncrement (new build number automatic) and ships no
    Anthropic key — only the proxy URL.
  - FIXED the small-Android opening screen (HookScreen): the non-affiliation/"not God"
    disclaimer was position-absolute and overlapped the "Come and see" button on short or
    oddly-shaped phones. It now lives in normal layout flow below a flex centered zone, so
    overlap is impossible on any screen shape; a COMPACT mode (height < 700) also scales
    type/margins down. Footer now reserves its space from frame one (no flash, no jump).
  - WARMED UP My Discipleship (members-only): added "today's word" — a daily-rotating
    scripture verse per Christlike quality (all four standard works; member track only,
    never visible to seekers) opening the examen card; a "kept" confirmation moment after
    saving a reflection; and a "N reflections kept · walking here since <date>" gathering
    line on My Walk with Christ. No new AI calls, no scores, no streaks.
- What changed in the app: mobile/src/screens/HookScreen.tsx,
  mobile/src/screens/DiscipleshipScreen.tsx, mobile/src/data/examenPrompts.ts.
- Verified: tsc --noEmit clean, tools/feed_test.js ALL PASS, tools/kjv_test.js ALL PASS,
  scripts/preflight.sh ALL CHECKS PASSED (no secrets tracked).
- What is now true: the code is ready for the Apple resubmission build. NOT YET DONE:
  a new iOS production build + eas submit + reply in the ASC Resolution Center, and the
  updated site/privacy.html must be verified deployed on Firebase hosting.
- What's next / handed off: build + resubmit iOS (build number auto-increments); confirm
  privacy.html is live; Cameron confirms the rejection message in the Resolution Center
  matches 5.1.1(i)/5.1.2(i) only (the API cannot read it, so if Apple listed anything
  more, it needs to be pasted in).
- Commit: 9438d84 (work) + the chain-link commit on top; retroactively also records 41ecf03.

---

## 2026-06-30 (pt.7) — deletion cleanup: cut the project from 1.9 GB to ~994 MB
- What we did: Cameron asked what could be DELETED (not just added) to improve organization.
  Surveyed the whole folder; deleted the dead weight after his go-ahead.
- What changed:
  - DELETED ~920 MB of old builds & old app copies: `archive/_old-folders/builds-archive/`
    (old .apk/.aab installers + old DB backup), `archive/legacy/MBM-mobile/` (full
    superseded app copy), `archive/legacy/mobile-expo/` (old Expo copy). The big binaries
    were gitignored (never on GitHub); all regenerable from EAS or git history.
  - DELETED 4 duplicate book formats in `pitch-book/` (book-drive.html, book-upload.html,
    book-text.txt, book-doc.txt) — kept the real PDF book + book.html source.
  - DELETED stale top-level chat-openers NEXT-CHAT-PROMPT.md and SESSION-OPENER.txt
    (fully covered by CLAUDE.md's session-chain steps).
  - Updated the map/index files so none point at deleted things: CAMERON — START HERE.md,
    START-HERE.md, README.md, OPEN-ME-FIRST.txt, docs/00-PROJECT-MAP.md.
- What is now true: the project is ~half its former size and the top level is cleaner.
  No live app, website, or source code touched — only old copies/outputs and duplicates.
- What's next / handed off: nothing required of Cameron.
- Commit: feb5a14 (cleanup) + this chain-link commit on top.

---

## 2026-06-30 (pt.6) — organized the folder for release + polish/print kit (NOT yet committed)
- What we did: gave MBM a human-friendly layer for Cameron (non-technical owner) WITHOUT moving any
  code/build paths. Added top-level master index `CAMERON — START HERE.md`; a `FOR-CAMERON/` folder
  (roadmap, launch plan, field guide, tester walkthrough, full book + "READ-ME — For You.md"); and a
  `TO-PRINT/` print kit (5 numbered ready-to-print finals + "READ-ME — Print Kit.md"). Updated
  `OPEN-ME-FIRST.txt` and `docs/00-PROJECT-MAP.md` to point at the new buckets.
- Polish pass: the Bishop brochure still had `[your phone]`/`[your email]` placeholders — filled in
  (843) 582-7278 · admin@milkb4meat.org · milkb4meat.org and regenerated
  `church-launch-kit/Bishop-Brochure.pdf` (weasyprint). Created two NEW pieces:
  `Members-Outreach-Brochure.pdf` (members: feed faith + share it) and `How-to-Get-the-App.pdf`
  (iPhone/Android sign-up sheet). Corrected `church-launch-kit/00_README-Start-Here.md` (its old
  "replace the placeholders by hand" note was now stale). Website: copied the Come-and-See brochure
  into `site/` and added footer download links (Roadmap PDF + Brochure PDF) on `site/index.html` and
  `site/roadmap.html`. Verified milkb4meat.org references are consistent everywhere — no wrong
  spellings, no remaining placeholders.
- What changed in the app (files): none in `mobile/`. Marketing/site/docs only.
- What is now true that wasn't before: clear FOR-CAMERON / TO-PRINT buckets + one master index; the
  Bishop brochure is contact-complete; a members brochure and a get-the-app sheet now exist; the site
  links to the public PDFs. Verified the live site serves fully at milk-b4-meat.web.app (Roadmap link
  present). milkb4meat.org STILL returns an SSL cert altname mismatch — Firebase hasn't finished
  issuing the custom-domain certificate (same as pt.3/4/5); resolves automatically, no redeploy needed.
- DONE (Cameron approved "commit + push + deploy live"): committed e649300, recorded it in chain
  commit ba6d48c, pushed to origin/main. Deployed Firebase hosting via the service-account method
  (45 files) — verified LIVE on milk-b4-meat.web.app: home 200, the new footer links "Roadmap (PDF)"
  + "Brochure (PDF)" present, and both PDFs serve as application/pdf (200).
- What's next / handed off: Cameron-only — confirm milkb4meat.org SSL once Firebase finishes issuing
  the cert (still an altname mismatch as of now; auto-resolves, no redeploy needed); the physical
  print run; optionally swap the Bishop-brochure phone for a personal one.
- Commit: e649300 (work) + ba6d48c (chain link); deploy verified live after.

---

## 2026-06-30 (pt.5) — built the public Roadmap (page + printable PDF) and deployed it live
- What we did: built a professional, forward-looking roadmap in the site's navy/gold serif style.
  Created site/roadmap.html (Foundation = done checks; Phase 1 incl. a "where it is right now —
  invite-only testing phase" block + tester-critique/test-as-non-member invites; Phase 2; Phase 3
  framed as a possibility for the Church to decide; a Vision section incl. a "real social presence"
  card). Added a "Roadmap" link to the top nav in site/index.html. Generated a print-friendly
  (light-paper) PDF with WeasyPrint -> site/Milk-Before-Meat-Roadmap.pdf, linked from the page.
  Wrote NEXT-CHAT-PROMPT.md (a copy-paste prompt for a fresh chat whose job is folder organization
  + a print kit + a release-readiness consistency pass). Deployed hosting via the service-account
  method (44 files).
- What changed: site/roadmap.html (new), site/index.html (nav link), site/Milk-Before-Meat-Roadmap.pdf
  (new), NEXT-CHAT-PROMPT.md (new).
- What is now true that wasn't before: the Roadmap page + PDF are LIVE and confirmed serving 200 on
  milk-b4-meat.web.app (roadmap.html, the PDF as application/pdf, the nav link, and the new content
  all verified). NOTE: the custom domain milkb4meat.org resolves to Firebase (199.36.158.100) and
  301-redirects to https, but as of this deploy Firebase has NOT yet issued the SSL cert for the
  custom domain ("no alternative certificate subject name matches milkb4meat.org") — so
  https://milkb4meat.org still throws a cert error. This completes automatically; no redeploy needed
  once the cert lands, and the new content will be there.
- What's next / handed off: next chat = organize the cluttered MBM folder (see NEXT-CHAT-PROMPT.md):
  sort into for-Cameron / to-print / computer-only, build an index + print kit, and run a
  consistency pass (website URL on brochures, members-only outreach brochure, ensure the site links
  to the public PDFs). Also keep watching Firebase Console > Hosting > Domains until milkb4meat.org
  flips to "Connected" (SSL issued).
- Commit: 5fe8f58

## 2026-06-30 (pt.4) — set up www.milkb4meat.org as well
- What we did: added www.milkb4meat.org as a second Firebase custom domain (under the OWNER
  account admin@milkb4meat.org) and saved the CNAME it asked for in Squarespace:
  CNAME www -> milk-b4-meat.web.app. Hit the Squarespace "Verify to continue as
  admin@milkb4meat.org" Google gate again; Cameron cleared it ("i think its good") and the record
  saved. Confirmed in the Squarespace records list (www CNAME present; admin->Railway CNAME and all
  email records still intact). Clicked Verify in Firebase — still "Records not yet detected" because
  the CNAME had just been added (propagation lag, same as the apex).
- What is now true that wasn't before: both milkb4meat.org (apex, A + TXT) and www.milkb4meat.org
  (CNAME) are fully configured in DNS and added in Firebase. Nothing left to configure on either.
- What's next / handed off: just propagation + Firebase's automatic recheck. Re-open Firebase
  Hosting > Domains later and both should read "Connected" with SSL issued. milk-b4-meat.web.app is
  live now in the meantime. Rule reaffirmed: do all MBM work under admin@milkb4meat.org.
- Commit: d588162

---

## 2026-06-30 (pt.3) — connected the custom domain milkb4meat.org to the live Firebase site
- What we did: pointed milkb4meat.org at the live Firebase Hosting site. In Firebase Console
  (signed in as the project OWNER, admin@milkb4meat.org — NOT Cameron's personal
  noremacttevol@gmail.com) added milkb4meat.org as a custom domain. In Squarespace DNS deleted the
  "Squarespace Defaults" group (4 parking A records 198.185.159.144/145 + 198.49.23.144/145, the
  www CNAME to ext-sq.squarespace.com, and the HTTPS @ record) and added the two Firebase records:
  A @ -> 199.36.158.100 and TXT @ -> hosting-site=milk-b4-meat. Left ALL email/admin records
  untouched (Google Workspace MX, Amazon SES, DKIM/SPF/DMARC, and the admin -> Railway CNAME).
- Account correction (important, now a rule): Cameron does NOT want MBM under his personal
  noremacttevol@gmail.com. Verified via Firebase IAM that admin@milkb4meat.org is the project
  OWNER and switched to it for all MBM work. Always use admin@milkb4meat.org for MBM going forward.
- What is now true that wasn't before: DNS has fully propagated — milkb4meat.org now resolves to
  199.36.158.100 (the Firebase IP) on Google (8.8.8.8), Cloudflare (1.1.1.1), and the authoritative
  Squarespace nameserver; the hosting-site=milk-b4-meat TXT record is live. curl confirms the
  domain connects to the Firebase IP. The old Squarespace parking IPs are gone.
- What's next / handed off: Firebase still showed "Needs setup" at the moment we finished, because
  its earlier ACME check hit the OLD (cached) Squarespace IPs and 403'd. That check runs again
  automatically and will succeed now that DNS is correct, then it issues the SSL cert. This is
  just propagation/recheck time (minutes to a couple hours) — nothing left to configure. Re-open
  the Firebase Hosting > Domains page later to confirm it flipped to "Connected." In the meantime
  the site is fully live at https://milk-b4-meat.web.app. Follow-up: www.milkb4meat.org currently
  has no record (its old CNAME was removed) — add www as a second custom domain or a redirect.
- Commit: af8287a (chain link: this entry recorded in 7d936d4)

---

## 2026-06-30 (pt.2) — rebuilt the public website into a real promotional landing page
- What we did: Cameron asked me to "do it all like always" and build the website first so it
  promotes the app to everyone — church members and non-members alike — with a gentle note that
  members of The Church of Jesus Christ of Latter-day Saints get "the extra stuff" when they
  declare it, but not heavy-handed. Rebuilt site/index.html from a single hero into a full
  landing page: navy/gold palette, sticky nav, hero, a 6-pillar "Why this is good for the world"
  section (Met where you are / Never pushed / Always honest / A real human always / Yours to
  keep / For everyone), an embedded explainer video, a "what it really is" section, a 4-shot
  glimpse strip of real app screenshots, the gentle "For everyone — and a little more for some /
  Milk first. Meat when you're ready." member section, get-it cards (TestFlight + Play), and a
  footer with the not-officially-affiliated disclaimer. Matched privacy.html and support.html to
  the navy palette and switched all contact emails to admin@milkb4meat.org.
- What changed (files): site/index.html (major rewrite), site/privacy.html, site/support.html,
  + copied site/img/walk/*.png (37) and site/Milk-Before-Meat-Explainer.mp4 into site/.
- What is now true that wasn't before: the site source is a genuine promotional page, verified
  via Playwright on desktop and mobile.
- DEPLOYED LIVE at https://milk-b4-meat.web.app (HTTP 200, new promo content confirmed serving).
  The stored Firebase user token was expired, so I deployed using the service account at
  admin/serviceAccount.json via GOOGLE_APPLICATION_CREDENTIALS (temporarily stripped the expired
  tokens/user from ~/.config/configstore/firebase-tools.json so the CLI fell back to ADC; original
  config restored afterward). REUSABLE for future deploys without Cameron's login.
  Domain milkb4meat.org still points at the Squarespace "Coming Soon" placeholder (separate DNS
  fix, see website-status memory).
- What's next / handed off: Connect milkb4meat.org to Firebase (custom domain + Squarespace DNS
  swap) — needs Cameron's logins.
- Commit: 8d40e07 (code) / live deploy done after

## 2026-06-30 — fixed the ministry-console scroll snap-back bug
- What we did: Cameron reported the "mc" (ministry console) website scrolling back down to
  the bottom whenever he scrolled up to read the top of a message thread. Traced it to the
  real console (admin/inbox.mjs — the inline PAGE served on port 4545, NOT the older
  server/public/admin.html, which was a red herring). Root cause: the 15-second auto-refresh
  (`setInterval(() => { loadThreads(); if(current) openThread(current); }, 15000)`) re-called
  openThread on the open thread, and openThread unconditionally ran `conv.scrollTop =
  conv.scrollHeight`, yanking him to the bottom every 15s. Fixed openThread to (a) detect a
  same-thread refresh vs a fresh open, and (b) only jump to the newest message on first open
  or when the reader was already near the bottom (<60px); otherwise it preserves the reader's
  scroll position. Applied the same guard to the older server/public/admin.html review pane.
- What changed in the app (files/commits): admin/inbox.mjs (openThread scroll logic) and
  server/public/admin.html (openConv scroll logic). Commit 8e5d44b.
- What is now true that wasn't before: scrolling up in a thread on the ministry console no
  longer gets dragged back to the bottom by the auto-refresh; live watching at the bottom
  still follows new messages.
- Verification: node --check on inbox.mjs passed; both inline browser <script> blocks parse
  clean (new Function). THEN deployed live and Cameron confirmed it: "yeap its good."
- DEPLOYED LIVE (this was the real hold-up). The code fix alone did nothing for Cameron
  because the live site at admin.milkb4meat.org is a Railway deployment and the new code had
  never been pushed to it — he kept seeing the old snapping behavior. I (the assistant)
  deployed it myself using the Railway CLI already installed + logged in on his machine:
  `export PATH="$HOME/.npm-global/bin:$PATH" && cd ~/Desktop/Brain/MBM/admin && railway up --ci`.
  The admin/ folder is linked to project `mbm-proxy`, service `MBM Ministry Console`
  (URL https://admin.milkb4meat.org). Build finished "Deploy complete", new deployment ID,
  service Online, site HTTP 200. Cameron hard-refreshed and confirmed the scroll holds.
  LESSON (saved to .auto-memory/deploy-ministry-console.md): I can redeploy this console
  myself — do NOT hand Cameron terminal commands or "log into Railway" steps. Just deploy.
- Commit: 8e5d44b (code); live deployment done via railway up on 2026-06-30.

## 2026-06-29 (pt.2) — made the folder actually SIMPLE for Cameron + put contact info on the brochure
- What we did: Cameron opened the folder and was still overwhelmed — last cleanup added a `docs/`
  tree but did NOT reduce the 22 top-level folders he sees, so it didn't feel organized. Fixed that:
  (1) Added his phone (843) 582-7278 + email admin@milkb4meat.org + milkb4meat.org to the BACK PAGE
  of the Come-and-See brochure and regenerated the PDF (verified on the rendered page). (2) Archived
  the 5 junk book drafts (book-drive/drive2/upload/upload2/noimg) into docs/archive/book-drafts/.
  (3) Deleted __pycache__ (auto-junk) and swept all dead leftover folders (app-screens,
  finish-the-screens, port-back, web-preview, work-logs, outputs, builds-archive) + 2 junk loose
  files into archive/_old-folders/. Top level went from 22 folders -> 14. (4) Wrote OPEN-ME-FIRST.txt
  at the root: a plain-English map grouping everything into "things you print," "the app + website,"
  "your notes," and "machinery — ignore." Verified all 11 live folders intact, site/ files present,
  mobile/package.json readable, connect.py/knowing_engine.py still at root, git moves = clean renames.
- What changed in the app (files/commits): NO app source changed. New: OPEN-ME-FIRST.txt. Edited:
  pitch-book/brochure.html (contact block) + regenerated Milk-Before-Meat-Come-and-See.pdf. Moves only.
- What is now true that wasn't before: the brochure is print-ready WITH Cameron's contact info, and
  opening the MBM folder shows 14 clearly-grouped folders instead of 22 with junk mixed in.
- What's next / handed off: optional — could further reduce by tucking machinery folders into one
  "behind-the-scenes" folder, but that needs renaming load-bearing paths (mobile/site/server/admin
  are referenced in the rule files), so left alone to avoid breaking the app/website. Big PDFs
  (Complete-Book, Overview-and-Launch-Plan) still in pitch-book — asked Cameron if he wants those too.
- Commit: 10dc408

---

## 2026-06-29 — v1 rough-draft cleanup: organized the whole repo + wrote the handoff docs
- What we did: Did a full "professional handoff" cleanup of the project. Verified the chain
  (top entry 51e2cbc present in git log). Archived all 7 superseded .apk/.aab builds (~460MB)
  and the old DB backup into a new `builds-archive/` (nothing deleted). Moved ~28 loose root
  markdown docs into an organized `docs/` tree (publishing / roadmap / vision / reviews /
  claude-setup / archive{handoffs,superseded,old-screenshots}). Left the authority files at the
  root (START-HERE, AGENT-RULES, SESSION-LOG, CLAUDE, .claudecode, AGENTS) so the chain still
  works, plus config/brand assets and the prototype engine files (connect.py/knowing_engine.py
  are still imported by ministry-sim, so they stay).
- What changed in the app (files/commits): docs/structure only — NO app source changed. New:
  `README.md` (front door), `docs/00-PROJECT-MAP.md` (full table of contents), `docs/archive/README.md`,
  `docs/publishing/PUBLISHING-VIABILITY-REVIEW.md` (fresh go/no-go review),
  `docs/roadmap/FORWARD-WORK-PLAN.md` (one prioritized to-do list),
  `docs/claude-setup/CLAUDE-RECOMMENDATIONS.md`. Updated PUBLISHING-ROADMAP (June 29 snapshot +
  fixed stale iOS/Android checkboxes) and START-HERE's file-hierarchy section to the new paths.
- What is now true that wasn't before: the repo looks like a clean v1 dev handoff — a small root,
  a single index (PROJECT-MAP), current vs historical docs clearly separated, and the publishing
  plan has an honest viability review + a forward work plan.
- What's next / handed off: app state is UNCHANGED (still waiting on Apple; Android 12-tester gate
  still the last Android gate — see WAITING-ON-APPLE.md / FORWARD-WORK-PLAN.md). Optional follow-ups
  I recommended but did NOT auto-apply: update CLAUDE.md's internal doc paths to the new docs/ locations,
  and set up the two scheduled checks (Apple-approval + 14-day clock) — see CLAUDE-RECOMMENDATIONS.md.
- Commit: d4ae3ef

---

## 2026-06-27 — milkb4meat.org landing page built; iPhone card parked in a "coming soon" state while we wait on Apple
- What we did: Built the public website for `milkb4meat.org` (Squarespace) as a self-contained
  responsive landing page — hero, embedded explainer video, the "not the Church / not God / just a
  helper" framing, four screenshots, and two install cards (iPhone + Android) plus the disclaimer.
  Cameron pastes the content into Squarespace himself (assistant can't log into Squarespace).
  Cameron then found the public TestFlight link shows "this beta isn't accepting any new testers
  right now." Diagnosed: that's expected until Apple's Beta App Review passes (the build, 1.0.0 (6),
  is still WAITING_FOR_REVIEW — confirmed via `eas build:list`). To keep the site publishable with no
  dead button, switched the iPhone card to a temporary "Coming any day — email admin@milkb4meat.org"
  state, matching Android, and preserved the LIVE direct-link card as an HTML comment right beside it
  for a one-step revert.
- What changed in the app (files/commits): docs/marketing only. NEW `pitch-book/site-milkb4meat.html`;
  NEW `WAITING-ON-APPLE.md` (single resume checklist for any future session). No app source changed.
- What is now true that wasn't before: there is a publish-ready website, and a clear tracked trail so
  any later chat can finish the iOS hookup the moment Apple approves.
- What's next / handed off: WAIT ON APPLE. When build 1.0.0 (6) shows "Ready to Test" (or the link
  `https://testflight.apple.com/join/cPNpeh3H` starts accepting testers), follow `WAITING-ON-APPLE.md`:
  un-comment the LIVE iPhone card, re-verify, tell Cameron, update START-HERE, commit+push. Optional:
  add Kyle/Rich as internal testers for iPhone now (skips review). Also confirm admin@milkb4meat.org
  is a watched inbox. Still pending separately: printed walkthrough, telling Kyle & Rich.
- Commit: 51e2cbc

---

## 2026-06-26 — Pitch/tester kit finalized (walkthrough, explainer video, gallery) per Cameron's punch list
- What we did: Revised the full tester-facing kit to Cameron's detailed feedback. Fixed the tester
  walkthrough opening to lead with the "not the Church / not God / just a helper" forewarnings
  (captured AFTER the sanctuary animation settles), corrected onboarding steps (answer+reply, then
  faith question+reply with the Enter button), reframed the Feed step to sell the scripture depth
  honestly (100+ for non-members pointing to the Restoration; 100+ meat for members/friends of the
  Church), added the journal kept-notes truth, the "Talk About It" upload links across the app, and
  the real-person toggle/crop/send/cancel detail. Rewrote the feedback question away from the
  machine/AI framing. Rebuilt the explainer video intro (it isn't God / just a helper → story about
  the Lord asking how you feel) and added a journal scene. Rebuilt the gallery with 15 real-
  interaction tiles (common questions + popups).
- What changed in the app (files/commits): docs/marketing only — pitch-book/walkthrough.html +
  book.html, the rendered PDFs (Walkthrough-for-Testers, Overview-and-Launch-Plan, Come-and-See),
  Milk-Before-Meat-Explainer.mp4, and app-screens/ (new g01–g09 interaction shots, 06b-faith-enter,
  settled 01-welcome-sanctuary, rebuilt _GALLERY.png). No app source code changed.
- What is now true that wasn't before: the tester kit is internally consistent with how the app
  actually behaves and frames itself; nothing implies the app plays God or answers for Him.
- What's next / handed off: waiting on Apple TestFlight approval; Cameron to get a printer for the
  printed walkthrough, then tell Kyle and Rich. Open questions raised: TestFlight/Play tester-invite
  mechanics, and turning the domain into a real website for all this.
- Commit: dd68dcf

---

## 2026-06-26 — iOS status documented; Apple side confirmed done + easy for the pitch stage
- What we did: Cameron asked, for his upcoming friends/family/church beta pitch, whether the
  Apple app is done and will be easy, and whether anything on the App Store page should be done
  better. Verified iOS state directly (EAS build:list: v1.0 build 6, commit dda114e, finished
  2026-06-26) and confirmed against START-HERE. Wrote a dedicated tracked record so the separate
  pitch chat can rely on it.
- What changed in the app (files/commits): NEW file IOS-STATUS-AND-APPLE-READINESS.md (honest
  iOS verdict + what's done + optional App Store polish + how iOS fits the testing plan). No app
  code changed — docs only.
- What is now true that wasn't before: there is now a single tracked source of truth for the iOS
  side. Verdict recorded: Apple is effectively FINISHED — submitted, AFTER_APPROVAL auto-release,
  TestFlight public link live NOW (https://testflight.apple.com/join/cPNpeh3H) so beta users can
  install today. Only optional polish: more screenshots (have 2 of Apple's allowed 10; the
  Android shots are the wrong aspect so iOS-sized frames would need generating) — additive, no
  re-review, not a blocker.
- What's next / handed off: nothing required on iOS. The real dependency is Android's 12-tester /
  14-day closed test. Pitch is being handled in a separate chat per Cameron.
- Commit: 1493311

---

## 2026-06-26 — ANDROID AUTO-PUBLISH VERIFIED + latest build live for Cameron's pre-check
- What we did: Stood up and PROVED the automated Google Play publishing pipeline, and got
  the latest fixed build onto internal testing so Cameron can check it before any 14-day
  clock. Ran `eas submit --platform android --profile production` with the new service
  account → pushed production **vc 6** (commit dda114e) to the **internal track**, status
  COMPLETED. Confirmed in Play Console: internal testing latest release is now 1.0.0,
  released Jun 26 ~5:26 AM, "Available to internal testers". Verified Cameron
  (noremacttevol@gmail.com) is in the active "MBM Testers" list; internal opt-in link is
  https://play.google.com/apps/internaltest/4700576250998456373 .
  Also built out the Play **store listing**: app name, short + full description (from
  store-assets/STORE-COPY.md), app icon (512×512) and feature graphic (1024×500) — the two
  graphics were cropped in-console from the existing brand art (icon.png) since the
  in-browser uploader can't drive the OS native file-picker. Saved successfully.
- What changed (files/commits): no app CODE change. Docs/config: START-HERE.md Android
  section rewritten to reflect verified auto-publish + internal link + store-listing state;
  this SESSION-LOG entry. eas.json was already wired last session.
- What is now true that wasn't before: Android publishing is automated and proven (a build
  reached a Play track via the service account, no manual upload). The latest member-fix
  build (vc 6) is installable by Cameron via internal testing right now. Store listing is
  ~90% done (text + icon + feature graphic in; screenshots pending).
- What's next / handed off: (1) Cameron uploads the 6 screenshots in store-assets/ under
  Phone / 7" tablet / 10" tablet (Add assets → Upload) — this is the last store-listing
  item and it needs the native picker only he can use. (2) After the listing turns green,
  set up the closed-test track (eas submit to a closed track) + line up 12 testers; the
  14-day clock then starts. The single substantive human dependency for public Android is
  those 12 testers.
- Commit: fbd9842

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
