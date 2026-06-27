# WAITING ON APPLE — website + TestFlight resume checklist

**Purpose:** a single place so ANY future session (any chat, any tool) can pick this up
instantly, however long the wait is, and finish it in one step. Read this with START-HERE.md.

**Created / last touched: 2026-06-27.**

---

## The situation (why we're waiting)

- The iOS app, version **1.0.0 (build 6)**, is **submitted to Apple and waiting on review**
  (`WAITING_FOR_REVIEW`, releaseType `AFTER_APPROVAL` — it goes live by itself once approved).
  Verified via `eas build:list --platform ios` (build id `992d2c36-...`, finished 2026-06-26).
- The **public TestFlight link** is `https://testflight.apple.com/join/cPNpeh3H`.
- Right now that link shows **"This beta isn't accepting any new testers right now."**
  That is **normal and expected** — a public TestFlight link only admits *external* testers
  once the build has passed Apple's **Beta App Review**. Until Apple approves, the link is dead
  to new people. Nothing is broken on our end. It usually clears within a day or two and then
  the SAME link starts working with no change from Cameron.

## What we did because of the wait

- The website `pitch-book/site-milkb4meat.html` (for `milkb4meat.org`, Squarespace) had its
  **iPhone card switched to a temporary "Coming any day now — email admin@milkb4meat.org" state**,
  so the site is safe to publish today with NO dead TestFlight button. The Android card already
  uses the email path. The original LIVE iPhone card (with the direct TestFlight link) is kept
  **right next to it as an HTML comment**, clearly marked, for a one-step revert.

---

## ✅ WHEN APPLE APPROVES — do this (the whole resume, in order)

1. **Confirm it's actually approved.** Either:
   - In App Store Connect → app → **TestFlight** tab, build **1.0.0 (6)** shows **"Ready to Test"**
     (not "Waiting for Review" / "In Review"); OR
   - The public link `https://testflight.apple.com/join/cPNpeh3H` now lets you tap **Install**
     instead of showing "not accepting testers."
2. **Flip the website iPhone card back to live.** In `pitch-book/site-milkb4meat.html`, find the
   `<!-- iPhone -->` block: **delete the active "Coming any day now" card**, and **un-comment the
   "LIVE iPHONE CARD"** directly below it (it restores the 3-step TestFlight install with the link).
3. **Re-verify the page** (screenshot the `#get` section — see `/tmp/shot_cards.cjs` pattern, or just
   reuse the same playwright-core chromium walker) so both cards read correctly.
4. **Tell Cameron** it's live and the site button now works, and that he can publish / point
   `milkb4meat.org` at it. If the site is already published on Squarespace, remind him to paste the
   updated iPhone card text/link there too.
5. **Update START-HERE.md** (iOS now LIVE / approved, not just submitted) and add a SESSION-LOG entry,
   then commit + push. Optionally delete or mark this file done.

## Other things Cameron may want (offer, don't assume)

- **Get Kyle & Rich on iPhone BEFORE external approval:** add them as **internal testers**
  (App Store Connect → Users and Access → invite their Apple ID email → add to the internal
  testing group). Internal testers skip Beta App Review and can install immediately. Cameron must
  do the App Store Connect steps himself (assistant cannot log in).
- **Android testers:** they email `admin@milkb4meat.org` with the Google account email on their
  phone; Cameron adds them to the Play tester list and sends the opt-in link. (Play closed-test
  rule: 12 testers opted in for 14 continuous days before production.)
- **admin@milkb4meat.org must be a real, watched inbox** — it's the whole Android path AND the
  temporary iPhone path. Confirm forwarding is set on the domain.

## Useful facts / paths

- Website file: `pitch-book/site-milkb4meat.html` (self-contained; assets in `pitch-book/img/walk/`
  and the video `pitch-book/Milk-Before-Meat-Explainer.mp4`).
- TestFlight public link: `https://testflight.apple.com/join/cPNpeh3H` (Apple regenerates this if the
  beta group changes — re-confirm before relying on it).
- Check iOS build state anytime: `cd mobile && npx eas build:list --platform ios --limit 3`.
