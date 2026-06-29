# Milk Before Meat — Publishing Roadmap

Plain-language map of where this app has been, where it is right now, and exactly
what is left before you can comfortably hand it to friends and family.

Last updated: June 29, 2026 (refreshed during the v1 cleanup)

> For the absolute current state, `START-HERE.md` always wins. This roadmap is the
> stage-by-stage map; the snapshot below is the quick truth as of the last refresh.

---

## June 29 snapshot — what is actually true now (read this first)

Since this roadmap was first written (June 25), several "unknowns" became "done." The
current reality:

- **iOS: submitted to Apple.** Version 1.0 (build 6 — the member-recognition build) is in
  `WAITING_FOR_REVIEW` and set to **release automatically** once Apple approves
  (~24h typical). It is also live on **TestFlight** (public link
  `https://testflight.apple.com/join/cPNpeh3H`). Nothing left for Cameron on iOS but wait.
  Detail: `IOS-STATUS-AND-APPLE-READINESS.md` and the active wait checklist `WAITING-ON-APPLE.md`.
- **Android: live on Play internal testing,** and the **service-account key is set up** so
  builds upload automatically (same as iOS). The only real remaining gate is Google's
  **12-tester / 14-day closed test**. Detail: `ANDROID-PUBLISH-PATH.md`.
- **The member-recognition fix** (the big one — editing the faith box flips the app into
  member/meat mode) is in code and in build 6.
- **The website is built** (`pitch-book/site-milkb4meat.html`), publish-ready, iPhone card
  parked in a "coming soon" state until Apple approves.
- **The recurring lesson, restated:** writing/committing code does NOT put it on a phone —
  only a NEW build + install does. When a fix "isn't there," check which commit the
  installed build came from before assuming the code is wrong.

The honest viability check on all of this is in `PUBLISHING-VIABILITY-REVIEW.md`.

---

## How to read this

Each stage has checkboxes. A checked box means it is **done and verified**. An
unchecked box is **still to do**. The stages go in order — Stage 0 is the
groundwork, Stage 5 is "ready to send to your people," and Stages 6–7 are the
future. You are right at the line between Stage 4 and Stage 5.

---

## Stage 0 — Foundation & Plan (what should happen before any building)

This is the part most people skip and regret. You actually did it.

- [x] Decided what the app IS (gospel outreach, meet people where they are, milk before meat)
- [x] Picked the right tech for one-person publishing: React Native + Expo (cloud builds, no Mac needed)
- [x] Chose local-first design so the app works without a server running
- [x] Kept the AI key OFF the phone — it lives on a server (the "proxy") so no one can steal it
- [x] Wrote down the rules and vision so any tool can pick up where the last left off (AGENT-RULES.md, CLAUDE.md)

---

## Stage 1 — The App Itself (the thing people install)

- [x] App builds and runs
- [x] Code compiles with zero errors (`tsc` clean)
- [x] Onboarding: story-first, one question, invisible routing (the "Jesus method")
- [x] Feed, dialogue, journal, and "talk to a real person" all wired up
- [x] App name set: "Milk Before Meat" (shows as "Milk B4 Meat" on the phone)
- [x] App icon and splash screen in place
- [x] Reset/"start fresh" testing path exists for clean test runs

---

## Stage 2 — Live Services (the parts that run on the internet)

- [x] Proxy server live and answering (Railway: mbm-proxy) — verified HTTP 200
- [x] AI chat endpoint working (`/api/chat` responds) — verified
- [x] "Talk to a real person" inbox working (Firebase) with anonymous sign-in
- [x] Admin reply desk hosted and login-protected (same Railway service)
- [x] Website live: milkb4meat.org, /privacy.html, /support.html — all verified HTTP 200
- [ ] **Rotate the keys that got exposed during setup** (see Stage 5 — do before wide release)
- [ ] **Change the admin desk password** from the placeholder "JosephSmith" to a strong one

---

## Stage 3 — Android / Google Play

- [x] Android app file built (`.aab`, the format Google Play wants)
- [x] Store listing text written and ready to paste
- [x] Data-safety and content-rating answers prepared
- [x] **.aab uploaded to Google Play Internal Testing and rolled out** — CONFIRMED
  (June 26 update verified live; versionCode 6 served on internal). This was the old
  "unknown" — now resolved.
- [x] **Automated Play publishing set up** — service-account key wired into EAS, so
  every Android build can be uploaded with one command (`eas submit --platform android`).
- [ ] **Run Google's 12-tester / 14-day CLOSED test** — the real remaining gate before
  public. Cameron rounds up 12 testers; the assistant sets up the closed track + opt-in
  link and pushes the build. (See `ANDROID-PUBLISH-PATH.md`.)
- [ ] Upload the 6 store screenshots from `store-assets/` (the in-app uploader can't drive
  the native file picker, so Cameron drags them in once).

---

## Stage 4 — Apple / TestFlight (where you are right now)

- [x] Apple app record created (App Store Connect)
- [x] App Store Connect API key set up for hands-free uploads
- [x] iOS build uploaded and processed — now on **build 1.0 (6)**, the member-recognition
  build (superseding the earlier build 3 this section was first written against)
- [x] TestFlight Test Information filled in (feedback email, contact, review notes)
- [x] Internal tester group created ("Internal Team")
- [x] External tester group created ("Public Beta Testers")
- [x] Public invite link enabled: https://testflight.apple.com/join/cPNpeh3H
- [x] App Privacy "nutrition label" PUBLISHED + both 6.7" screenshots uploaded + metadata
  accepted (the parts Apple rejects apps over — all done)
- [x] **Submitted for PUBLIC App Store review** — releaseType AFTER_APPROVAL (it goes live
  on its own when Apple approves; no second tap needed from Cameron)
- [ ] **Apple approves the build** (usually ~24 hours) — the App Store page lights up by
  itself, and the public TestFlight link starts accepting external testers, after this

> The link above is real, but it will say "this beta isn't accepting testers" until
> Apple finishes its review. That is normal. Nothing is broken.

---

## Stage 5 — What's Left Before You Send It to Friends & Family

This is your real to-do list right now. None of these is hard.

- [ ] **Wait for Apple's "Approved" email** (TestFlight build). Then test the link yourself once.
- [ ] **Do a self-test on a real phone**: install via TestFlight, open it, run through onboarding,
      send one AI message, tap "talk to a real person," confirm a message lands in your desk.
- [ ] **Decide Android: in or out for round one?** If yes, finish Stage 3's two open items.
      If you'd rather start iPhone-only to keep it simple, that's a completely fine choice.
- [ ] **Security clean-up before wide sharing** (honest, important, quick):
  - [ ] Change the desk password from "JosephSmith" to something strong.
  - [ ] Rotate the API keys that were shown in setup logs (Firebase, Anthropic, Railway token).
        I can walk you through each one when you're ready — it's mostly "make new key, paste it, delete old."
- [ ] **Write your tester instructions** (1 short paragraph): how to install, what to try, how to send feedback.
- [ ] **Confirm feedback path**: testers can reach you at noremacprojects@gmail.com (already set in TestFlight).

When every box in Stage 5 is checked, you can send it out with a clear conscience.

---

## Stage 5.5 — June 25 review: what changed and where the app stands (DONE)

This captures the full all-sides check done on June 25, 2026, so nothing gets re-explained.

**What was changed and committed (git `fea4add`):**

- [x] Removed ALL Christlikeness / virtue scoring everywhere — no "seven spirit
      levels," no hidden judge, no trait scores. The app does not grade anyone's soul.
- [x] The restored-gospel gate now reads the person's **own words only**
      (`mayReferenceLds` / `restorationReady`) — nothing measured behind their back.
- [x] Every signal the app records is shown openly on the Profile with a **Forget**
      button that truly un-learns it and re-routes the feed. Nothing hidden.
- [x] Standing **"not officially affiliated with any Church"** disclaimer on the first
      screen, the Profile, and the privacy page.
- [x] Restored scripture is never embedded — meat cards link to the official Gospel
      Library; only the public-domain KJV is bundled inline.
- [x] AGENT-RULES.md and STATUS.md updated to match.

**How it was verified:**

- [x] Typecheck clean (`tsc --noEmit`, exit 0).
- [x] Read the full minister AI prompt — milk-before-meat, defend Jesus's goodness,
      no-duck rule, ask permission before the Restoration, crisis safety (988), member
      track: all present and sound.
- [x] Stress-tested the gate engine with 12 adversarial profiles — **12/12 passed.**
      Fresh visitors never get the Church named; Calvinist/harsh-God pictures stay
      blocked even when the person says "God is good"; a single soft signal is never
      enough (two witnesses required); "how do I get baptized" with no readiness routes
      to a real person, not a fast-tracked missionary referral.

**Church / trademark posture (the part only a human can finish):**

The core worry is simple — *don't make the app look like the Church built or endorsed
it.* You already cleared that: it's branded "Milk Before Meat" (not the Church's name),
no Church logo or Angel Moroni, neutral icon, and now a non-affiliation disclaimer.
Intellectual Reserve, Inc. owns "The Church of Jesus Christ of Latter-day Saints,"
"Mormon," "Book of Mormon," the Church logo/wordmark, and program brands (Come Follow
Me, Liahona, FamilySearch, CTR). Referring to them in text is fine; looking official is
not. So the rule for publishing: never put those names/logos in the app **title, icon,
or store listing**, and never imply it's an official Church app.

- [ ] (Optional) One-line trademark attribution note on the website footer.
- [ ] (Before any *public/wide* launch — not friends-and-family) Call the Church
      Intellectual Property Office, 1-801-240-3959, and describe the app honestly.
- [ ] (Cameron's own step) Talk it over with a bishop / stake president.

> Honest note for the record: the strongest protection with the Church is being
> upfront, not racing to stay unseen. The good news is these very changes — the
> disclaimer and removing the soul-scoring — are exactly what make the app safe to be
> looked at. Publishing the improved build is the move; nothing here needs to stay
> hidden to be okay.

---

## Next mission — push the improved build to the stores

The reviewed, scoring-free, disclaimer-carrying version is what should be live. Get it
out to testers/users as the current build.

- [ ] Build a fresh iOS build (Expo/EAS) from the current code and upload to TestFlight.
- [ ] Build a fresh Android `.aab` from the current code and upload to Play internal testing.
- [ ] Confirm both new builds carry: removed scoring, own-words gate, open/removable
      signals, the non-affiliation disclaimer, and Gospel-Library links (no embedded
      restored scripture).
- [ ] Bump the version/build number so the stores accept the update.
- [ ] (Still open from Stage 5) Security clean-up: strong admin password + rotate keys.
- [ ] Self-test the new build on a real phone before sharing.

---

## Stage 6 — After They're Testing (the first week or two)

- [ ] Watch the admin desk for "talk to a real person" messages and reply
- [ ] Collect feedback (TestFlight has a built-in feedback + screenshot tool)
- [ ] Keep a simple list of bugs/ideas; ship small fixes via Expo updates when easy
- [ ] Note which stories and questions land best (the app records this for you)

---

## Stage 7 — Toward a Full Public Launch (later, no rush)

- [ ] Polish based on real feedback
- [ ] Decide on full App Store + Google Play public release (vs. staying in testing)
- [ ] Privacy policy URL added to the store listings (required for full public release)
- [ ] A real pitch/landing story for inviting people beyond friends and family
- [ ] Phase 2 thinking: a small team of helpers answering messages, not just you

---

## The "did I do this right?" technical checklist (what most devs verify before a friends-and-family test)

These are the standard sanity checks. Here's where each one stands today.

- [x] App compiles cleanly (no errors): **verified**
- [x] Backend/AI responds: **verified (HTTP 200, /api/chat works)**
- [x] Website + privacy + support pages load: **verified**
- [x] Secrets are not shipped inside the app (key lives on the server): **verified by design**
- [x] A build actually exists for at least one store (iOS in review; Android .aab built): **yes**
- [ ] You personally installed the store build and clicked through it: **do this once Apple approves**
- [ ] Exposed keys rotated + admin password strengthened: **not yet — do in Stage 5**
- [ ] Android Play internal-testing release confirmed live (if you want Android in round one): **unconfirmed**

Short version: the app is in genuinely good shape for a rough-draft / first-testers release.
The only true "must-do before wide sharing" items are the security clean-up and a personal
walk-through on a real phone once Apple approves. Everything else is polish.

---

## One-line status

The app passed a full June 25 review — scoring removed, own-words gate, open/removable
signals, non-affiliation disclaimer, 12/12 gate stress-tests passing, typecheck clean.
Next mission: build and upload the fresh iOS + Android builds so the improved version is
what's live, then the quick security clean-up and a self-test on a real phone.
