# When Someone Emails Asking for the App — Your Playbook

_Written 2026-08-07. Everything here is verified working as of today._

## The one question to ask them: iPhone or Android?

---

## If they have an iPhone → NO tester setup needed. It's public.

The iPhone app is live on the App Store for everyone. Just reply with the link:

> The app is free on the App Store — here you go:
> https://apps.apple.com/us/app/milk-before-meat/id6783621048

That's it. Done. Do not use TestFlight for regular people — the store version is the real one.

---

## If they have an Android phone → 2 minutes in Play Console, then send the link.

Android isn't public yet. Google makes personal developer accounts run a
**closed test with 12 testers for 14 straight days** before the public button
unlocks. **Every person who emails you is one of your 12** — the traffic is
literally Google's requirement solving itself.

**Steps (do this for each person):**
1. Reply and ask for the **email address tied to their Google account** (the
   one their Play Store uses).
2. Go to https://play.google.com/console → Milk Before Meat → **Testing →
   Internal testing → Testers tab** → add their email to the **MBM Testers**
   list → Save.
3. Send them this reply:

> You're in! Two quick steps:
> 1. Open this link on your phone, signed into the same Google account you
>    gave me: https://play.google.com/apps/internaltest/4700576250998456373
> 2. Tap "Become a tester," then tap the Google Play link on that page to
>    install. Updates come automatically after that.

**Heads up:** the link does nothing until their email is on the list — always
do step 2 before sending the link.

## The 14-day public clock (what I staged for you)

A **closed-test release is already staged as a draft** on the Play "alpha"
track (done 2026-08-07 via the publishing robot). To start Google's 14-day
clock you have to press the buttons Google reserves for the account owner:

1. Play Console → Milk Before Meat → **Testing → Closed testing** → the staged
   "1.1.0 closed test" release → review and **roll it out / send for review**.
   (If the console asks you to finish any Content-rating / Data-safety
   questionnaires first, answer them — everything else is done.)
2. Once Google approves it, a **closed-test opt-in link** appears on the
   Closed-testing Testers tab — from then on, send new people THAT link
   instead of the internal one, because **closed-test opt-ins count toward
   the 12; internal ones don't.**

## Two small Play Console chores while you're in there

- **Screenshots:** I tried to upload the 6 store screenshots by robot and Google
  said no — the robot account lacks one permission. Either flip it on
  (**Users & permissions → mbm-play-publisher@mbm-publishing.iam.gserviceaccount.com
  → App permissions → check "Edit store listing"** — then tell the assistant and
  it uploads all 6 in seconds), or drag the 6 files in yourself from
  `store-assets/` (play_phone_1/2, play_tablet7_1/2, play_tablet10_1/2) under
  **Store listing → Add assets**.
- **Developer verification (deadline Sep 30, 2026):** Google emailed Aug 6 —
  Play Console will show a banner about registering apps + signing keys for
  Android developer verification. Follow it before Sep 30 or the app can be
  blocked. It's a form, not a rebuild.

---

## One more inbox to watch

Access emails from the website go to **admin@milkb4meat.org** (that's the
address on milkb4meat.org), not your main Gmail. Check it regularly — the
Apple rejection in June sat unseen for 5 days in a side inbox. Don't let a
person asking about Jesus content sit unanswered the same way.
