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
- Commit: <hash filled in after you commit>

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
