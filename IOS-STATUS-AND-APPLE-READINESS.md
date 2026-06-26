# iOS / Apple App Store — Status & Readiness Record

**Last verified true: 2026-06-26.** This file exists so any chat (especially the pitch chat)
can rely on a single honest answer to one question: *Is the Apple side done, will it be easy,
and is there anything to do better?* If this disagrees with someone's memory, re-verify against
EAS / App Store Connect before acting. START-HERE.md remains the master truth file; this file
is the iOS-specific detail behind it.

---

## THE VERDICT (one paragraph)

The Apple side is **done and will be easy.** The finished app (version 1.0, build 6 — the
member-recognition build, commit `dda114e`) was submitted to Apple for public App Store review
on 2026-06-26 and is set to **release automatically the moment Apple approves it** (typical
turnaround ~24 hours). Nothing on the Apple side is waiting on Cameron. And critically for the
pitch: people do **not** have to wait for Apple — anyone with an iPhone can install the real,
full-quality app **right now** through the public TestFlight link. So the pitch chat can safely
promise iPhone users a professional, ready-to-use app today.

---

## WHAT IS ALREADY DONE ON APPLE (so the pitch chat can count on it)

- **Public TestFlight link — LIVE NOW:** https://testflight.apple.com/join/cPNpeh3H
  Anyone with an iPhone can tap this, install TestFlight, and run the real app immediately.
  This is the link to give beta users **before** the App Store goes live.
- **Submitted for public review:** v1.0 (build 6) in App Store Connect, releaseType
  AFTER_APPROVAL — it goes live on its own when Apple approves. No second tap needed from
  Cameron to release (this was set at submission time).
- **Store listing is complete and accepted:** app name, subtitle/description metadata, age
  rating, categories (Lifestyle / Books), free worldwide pricing, content-rights declaration,
  and App Review contact (Cameron, phone, admin@milkb4meat.org).
- **App Privacy "nutrition label" is PUBLISHED:** Name, Sensitive Info, Other User Content,
  User ID — all declared as "App Functionality," linked to identity, **no tracking.** This is
  the part Apple rejects apps over, and it is done correctly.
- **Two 6.7" screenshots uploaded** (1290×2796, verified) — meets Apple's minimum.
- **Built and shipped without a Mac or any browser uploads** — the whole iOS store side was
  driven through the App Store Connect REST API, so future updates are repeatable the same way.

**Bottom line for the pitch chat:** iPhone is the *easy* platform. Hand people the TestFlight
link today; the App Store page lights up by itself within ~a day of Apple's approval.

---

## IS THERE ANYTHING TO DO BETTER ON THE APP STORE PAGE?

Nothing here is required and nothing blocks launch. These are **optional polish** items that
would make the public App Store page look fuller and convert better once it's live — useful only
because Cameron plans to send real people to it. Ranked by value-for-effort:

1. **More screenshots (highest value, real work).** Apple allows **up to 10** screenshots on the
   6.7" size; we currently have **2** (`store-assets/ios_67_1.png`, `ios_67_2.png`). A gallery of
   5–8 makes the page feel like a finished, trustworthy product instead of a bare minimum. NOTE:
   the existing Android phone shots in `store-assets/` are 1080×1920 — the **wrong** aspect for
   iOS (needs 1290×2796), so they can't be reused directly; new iOS-sized frames would have to be
   generated. This can be added **any time, even after launch,** without a new app build.
2. **Promotional text (easy, no review delay).** A 170-character line above the description that
   can be edited **any time without resubmitting** the app — ideal for a launch message or a
   "now available" note. Currently not a blocker; worth adding when convenient.
3. **Keywords field (easy).** Improves how the app is found in App Store search. Low effort,
   editable on the next metadata update.
4. **App preview video (high effort, optional).** A 15–30s autoplay clip at the top of the page.
   Nice-to-have, not needed for a friends/family/church launch.

If Cameron wants any of these, item 1 (more screenshots) is the only one with meaningful payoff
for the pitch, and it's additive — it does not require touching the submitted build or re-review.

---

## HOW iOS FITS THE PITCH / TESTING PLAN (Cameron's strategy, 2026-06-26)

Cameron's plan: get church people excited and **already using a beta** first, get the church to
bless it, *then* start Google's official 14-day closed test — maximizing the value of that
window. iOS supports this perfectly:

- **iPhone users:** TestFlight link now → seamless auto-upgrade to the public App Store app once
  Apple approves. They never have to reinstall or do anything; the same app just becomes "official."
- **Android users:** the same people are also the pool for Google's required **12 testers / 14
  continuous days** closed test. One outreach feeds both platforms.
- **The dependency that matters is Android's 12-tester clock, not iOS.** Apple is effectively
  finished. So in the pitch, iOS = "here's the link, you're in," and the structured 14-day push
  is an Android concern (see ANDROID-PUBLISH-PATH.md).

---

## QUICK FACTS FOR ANY ASSISTANT

- Latest iOS build: **v1.0 (6)**, commit `dda114e`, EAS build `992d2c36-...`, finished 2026-06-26.
- Submission state: submitted for review, AFTER_APPROVAL auto-release.
- TestFlight public link: https://testflight.apple.com/join/cPNpeh3H
- iOS screenshots on file: `store-assets/ios_67_1.png`, `ios_67_2.png` (1290×2796).
- Re-verify build state any time with: `cd mobile && npx eas build:list --platform ios`.
- Re-verify live App Store review status in App Store Connect (Cameron's Apple account).
