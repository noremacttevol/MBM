# START HERE — MBM Current State (the ONLY file that is allowed to say "now")

**Last verified true: 2026-07-04 (pt.3) — Three fixes from Cameron's live testing SHIPPED
via OTA (code commit 841af0e; EAS update group 4093b44f, iOS+Android, runtime 1.0.0 —
reaches installed builds after closing and reopening the app twice): (a) cold-open
disclaimer no longer flashes before the animation (footer fade moved to the JS driver);
(b) Talk About It history/clock icon no longer clipped (emoji replaced with an Ionicons
vector icon); (c) AI consent REWORKED — removed from onboarding entirely, AI defaults
OFF, a just-in-time card appears the first time someone opens Talk About It, says "AI"
not "Anthropic," shows the topic they arrived with, and offers an equal real-person path
that carries their sourced question into a Connect thread. Profile on/off toggle kept.
Privacy policy still names Anthropic (required); in-app strings do not. Everything below
from pt.2 remains true: iPHONE LAUNCH WORK ALL DONE; waiting only on
Apple's public index. iOS 1.0 (build 8) is READY_FOR_SALE; the zero-territories bug was
fixed earlier today (all 175 territories, availableInNewTerritories=true, release date
2026-07-04). As of this writing the iTunes lookup still returns 0 — normal for a few
hours after an availability change; a SCHEDULED TASK ("check-appstore-live", 3x daily)
now watches it, will notify Cameron when live, update this file, and disable itself.
EVERYTHING ELSE IS ALREADY FLIPPED AND DEPLOYED: (1) site/index.html iPhone card now
points at the App Store (https://apps.apple.com/app/id6783621048), roadmap.html updated
(iPhone = public, Android = testing), DEPLOYED to Firebase hosting and verified serving.
(2) Print kit refreshed: church-launch-kit/How-to-Get-the-App.html+pdf and TO-PRINT
sheet #4 now give App Store steps with a NEW qr-appstore.png QR; 04_Install-Guide.md
iPhone path rewritten for the App Store. Sheet #4 old printouts are obsolete — reprint.
Come-and-See / Members / Bishop brochures unaffected (they only show milkb4meat.org).
(3) DOMAIN NOTE CORRECTED: milkb4meat.org + www are ALREADY connected to Firebase
hosting and serving the real site (verified via DNS + HTTP 2026-07-04) — the old
"Squarespace placeholder" warning below was stale; ignore it. Android version code 7 is
LIVE on the Play internal track; Android public release still needs the 12-tester/14-day
closed test. Railway key proxy HARDENED (see FOR-CAMERON/SECURITY-REPORT-2026-07-02.md);
app token NOT enforced yet (build 8 does not send it). Cameron-only task still open:
set a monthly spend cap at console.anthropic.com.**
**If you are an AI assistant: read this whole file before you say ONE word about what is
done, published, built, or pending. Do not trust your memory over this file. If this file
and any other file/your memory disagree, THIS FILE WINS until a human updates it.**

If today's date is more than a few days after the "Last verified true" date above, say so
out loud to Cameron and ask him to confirm anything time-sensitive before acting on it.

---

## Who Cameron is (so you treat him right)
Cameron is non-technical and relies on the assistant to do the technical work. He has
limited time and a low tolerance for being asked to re-explain things or being told to
redo work that is already done. Take initiative. Do not make him be the bug reporter.
Do not re-ask settled questions. Verify before you claim anything is or isn't done.

### Cameron's phones / testing setup — KNOW THIS, never re-ask
- **Cameron's own phone is an ANDROID phone.** By default, assume Android. He installs
  and updates MBM through the **Google Play Store** (he is an internal tester; the
  Google Play account and its fee are ALREADY PAID — never tell him otherwise).
- He ALSO tests the iPhone app on **his wife's iPhone**, using her account, during the
  daytime. He will explicitly SAY when he is "using my wife's phone / testing the
  iPhone app." Only then is TestFlight (iPhone) the right path.
- So: unless Cameron says he's on his wife's iPhone, the phone in question is HIS
  ANDROID, and the delivery path is Google Play, not TestFlight.

---

## THE TRUTH RIGHT NOW (do not contradict this)

### Accounts — ALL EXIST. Never tell Cameron to create these or pay setup fees.
- Apple Developer account — exists, paid, set up.
- Google Play Console account — **created, $25 fee already paid, identity verified.**
  NEVER say he needs to "create a Google Play account" or pay "$25." That is DONE.
- Expo / EAS account — `milkb4meat`, logged in, used for cloud builds.
- Railway account — proxy `mbm-proxy` runs here.
- Firebase project — live (Anonymous sign-in on, firestore.rules published).
- Domain `milkb4meat.org` — owned, DNS at Squarespace, and ✅ CONNECTED to Firebase hosting
  (verified 2026-07-04: apex A record → 199.36.158.100, www CNAME → milk-b4-meat.web.app,
  both serve the real site over HTTPS). The old "Squarespace placeholder" issue is RESOLVED.

### Publishing — already shipped before. This is NOT a from-scratch setup.
- **iOS: RESUBMITTED — WAITING_FOR_REVIEW (2026-07-02, confirmed via ASC API).** The
  5.1.1(i)/5.1.2(i) rejection was fixed in commit 41ecf03 (consent gate), audited, built
  as **build 8**, attached to version 1.0, and submitted in a NEW review submission
  (3888660e-454c-4d81-bd4a-67dc30b6463c) after canceling the dead rejected one. The
  updated privacy policy naming Anthropic is verified LIVE on the website. Nothing for
  Cameron to do — wait for Apple's verdict. If approved, the public-release tap is his;
  if rejected again, read the new message and iterate.
- **Android: version code 7 (same fixes) is LIVE on the internal track (2026-07-02).**
  Cameron's phone picks it up through Play internal testing as usual.
- **iOS (history):** **REJECTED BY APPLE (verified 2026-07-01 via ASC API).** Version 1.0 (build 6)
  was submitted 2026-06-26; appVersionState is now **REJECTED**, reviewSubmission
  99f5b00a-00ca-4d82-b5be-8d402fab6d11 state **UNRESOLVED_ISSUES**. The rejection
  REASON is in the Resolution Center (ASC web UI — the API key cannot read it) and in
  an email sent to **noremacprojects@gmail.com** (NOT Cameron's main inbox — this is why
  no one noticed for 5 days). NEXT STEP: read the rejection message (Cameron signs into
  ASC in the browser, or pastes the email), fix the issues, resubmit. Do NOT tell
  Cameron "just wait for Apple." Everything Apple needed at submit time was done: metadata, both
  6.7" screenshots, age rating, categories (Lifestyle/Books), free worldwide pricing,
  content-rights declaration, App Review contact (Cameron, phone, admin@milkb4meat.org),
  and the **App Privacy data-usage label is PUBLISHED** (Name, Sensitive Info, Other User
  Content, User ID — all "App Functionality", linked to identity, no tracking). The whole
  iOS store side was driven via the App Store Connect REST API (no Mac, no browser uploads).
  Nothing left for Cameron on iOS — just wait for Apple's review (~24h typical).
  - Still also on **TestFlight** (public link https://testflight.apple.com/join/cPNpeh3H).
- **Android:** Automated Google Play publishing is now LIVE and VERIFIED (2026-06-26).
  - Play **service-account key** is set up, downloaded, gitignored at
    `mobile/credentials/play-service-account.json`, API enabled, robot account
    `mbm-play-publisher@mbm-publishing.iam.gserviceaccount.com` is Active in Play Console.
    `eas.json` submit.production.android wired (track currently `internal`).
  - PROVEN working: `eas submit` pushed production **vc 6** (commit dda114e, the
    member-recognition / meat-leak-fix build) to the **internal track** on 2026-06-26 with
    status COMPLETED. Internal testing now serves vc 6 (latest release Jun 26 ~5:26 AM).
  - **Cameron can pre-check the latest build RIGHT NOW** via the internal-testing web
    opt-in link: **https://play.google.com/apps/internaltest/4700576250998456373**
    (he's an active tester — noremacttevol@gmail.com is in the "MBM Testers" list).
  - **Store listing:** app name, short + full description, app icon (512×512), and feature
    graphic (1024×500) are DONE and saved. The icon + feature graphic were cropped from the
    existing brand art in the asset library. STILL NEEDED: phone + 7" + 10" tablet
    screenshots — the polished files exist in `store-assets/` (play_phone_1/2,
    play_tablet7_1/2, play_tablet10_1/2) but the in-app uploader can't drive the native
    file-picker, so Cameron uploads those 6 himself (Add assets → Upload under each section).
  - To go PUBLIC, Android still needs Google's **12-tester / 14-day CLOSED test**. Once the
    screenshots are uploaded (store listing turns green), the ONLY remaining substantive
    dependency is lining up the 12 closed-test testers; the closed-track build push is
    automatable via eas submit (switch track to a closed track). Full map:
    **ANDROID-PUBLISH-PATH.md**.
- **Latest code commit:** verify with `git log -1` (iOS submit work is docs/config only).

### The ONE bug that keeps wasting Cameron's time — check this FIRST every time
**Writing/committing code does NOT put it on the phone.** A fix can be correct in the
files, committed, and pushed — and still not be on any device until a NEW build is made
AND installed. Several "missing fixes" were all this exact thing: the installed build was
made from older code. RULE: when Cameron says a fix "isn't there," first check which
commit the installed build came from (`cd mobile && npx eas build:list`), not whether the
code is right. JS-only changes can also be pushed instantly with `eas update` (OTA), no
rebuild needed.

---

## DONE vs ONLY-WRITTEN vs CAMERON-ONLY
(The full living version is STATUS-AND-ROADMAP.md — but THIS file is the quick truth.
Keep both in sync; update this file's date whenever you change it.)

### Done & shipped (in code, committed, in a build)
Cold-open fade fix, "Talk About It" chat header fix, de-surveilled Profile with Remove
buttons, ministry-console resilience, no-repeat story-on-cold-open, own-words restoration
gate, open/removable signals, non-affiliation disclaimer. All in `e4a2575`/`56b41a2`.

### Fixed in code June 26, awaiting a NEW build to reach the phone
- **Member recognition (THE big one).** Editing the faith box on the Profile to say "I am a
  member of the Church of Jesus Christ of Latter-day Saints" now snaps the app into member /
  meat mode: feed shifts to MAINTENANCE, the private discipleship companion turns on, a
  visible "Walk with Christ" banner appears on the home feed, and the chat acknowledges the
  person as a fellow Latter-day Saint. This fires from ANY faith-write path (Profile edit,
  Profile add, onboarding free-text) and from chat. Broadened the member phrasings the app
  recognizes and added negation/third-person guards ("my wife is a member" / "I'm NOT a
  member" never mint membership). Verified by regex unit test + `tsc --noEmit` clean.
- The header-cramping and "what the app has noticed" complaints were ALREADY fixed in code
  (`a287171`/`e4a2575`); Cameron is seeing them because his installed build is older. A new
  build clears them too. Same for the iPhone opening-animation flash (native-driver +
  deferred first-frame mount already in code).

### Written/planned but NOT built yet
Tiered model routing (Haiku/Sonnet/Opus by signal) — see MODEL-ROUTING-AND-OFFLINE-PLAN.md.
Belief/testimony answer option for dialogue.

### Decided AGAINST (do not build)
- **A "Start fresh" reset button.** Cameron's call (June 2026): users control their own
  record by REMOVING or EDITING what the app has stored about them, right on the Profile —
  the per-item Remove buttons and the editable faith box already do this. There is no blunt
  wipe-everything button; honoring a person means letting them adjust the specific things
  the app learned, not nuking the whole relationship.

### Only Cameron can do (human + accounts + money + the public button)
1. **The public store release — the ONE final tap, with a sworn promise around it.**
   The assistant's promise to Cameron, in plain words: *I will do everything myself.*
   I build the app, I run the checks, I upload the build to App Store Connect / Google
   Play Console, I fill in the store listing, I open the exact page in the browser, and I
   tell Cameron the exact button to press and where it is on the screen — by name, with a
   screenshot if I can. I do NOT stop early and hand him a vague "now you take it from
   here." The only thing left for Cameron is the single irreversible public-release tap
   that Apple/Google legally require the account owner to make. I get him all the way to
   that one button and point right at it. If I ever can't do a step myself, I say exactly
   why and exactly what I need from him — I never use "only you can press the button" as a
   reason to give up or leave him hanging.
2. Firebase Blaze (paid) upgrade, if he wants to kill the free-tier read limit.
3. Any new card/billing caps or new API keys with spend limits.
4. Store listing details Apple/Google require the account owner to confirm.
5. Entering his own passwords / 2FA codes — always handed back to him.

---

## FILE HIERARCHY — which file wins when they disagree
The repo was reorganized on 2026-06-29 (see SESSION-LOG). Most docs now live under `docs/`.
`docs/00-PROJECT-MAP.md` is the full index. Order of authority:
1. **START-HERE.md** (this file) — current state. Highest authority for "what is true now."
2. **AGENT-RULES.md** — the vision, the laws, how to behave. Highest authority for "how/why."
3. **CLAUDE.md** + **.claudecode.md** — operating rules (auto-loaded by the tooling).
4. **docs/roadmap/STATUS-AND-ROADMAP.md** — the detailed living roadmap. Sync it with this file.
5. **.auto-memory/MEMORY.md** + topic files — accumulated history; CAN BE STALE; do not
   trust it over this file.

Current docs now live in `docs/publishing/`, `docs/roadmap/`, `docs/vision/`, and
`docs/reviews/`. Publishing detail: `docs/publishing/` (PUBLISHING-ROADMAP,
PUBLISHING-VIABILITY-REVIEW, ANDROID-PUBLISH-PATH, IOS-STATUS-AND-APPLE-READINESS,
WAITING-ON-APPLE). Forward work: `docs/roadmap/FORWARD-WORK-PLAN.md`. Everything in
`docs/archive/` (old handoffs, superseded plans) is HISTORICAL ONLY — if it conflicts with
this file, this file is right. Old build binaries and a superseded full app copy (~920 MB)
were deleted on 2026-06-30 to keep the project lean — all regenerable from EAS or git
history, so nothing was lost.

---

## UPDATE RULE (for the assistant — do this, don't skip it)
At the END of any session where something real changed (a build shipped, an account
changed, a feature went from written to built, the public release happened): update the
"Last verified true" date at the top of this file and the TRUTH section, in plain
language. Keep it short. A stale truth file is worse than none — it is exactly what
broke Cameron's trust in the first place.
