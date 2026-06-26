# Android (Google Play) — the path to a PUBLIC release

**Written 2026-06-26.** iOS is already submitted to Apple for public review (see SESSION-LOG).
Android is the slower one — NOT because of our app, but because of two Google rules that
only apply to the account owner. This file is the plain-English map of what is left.

## Where Android is right now
- The app is ALREADY live on Google Play **internal testing** (versions 3, 4, and a v5
  build from June 25). Cameron installs/updates through Play as an internal tester.
- That is internal testing — it is NOT the public store yet.

## The two gates between "internal testing" and "public on Google Play"
Both are Google policy for a **personal** developer account. Neither is something our code
can satisfy by itself.

### Gate 1 — The 12-tester / 14-day closed test (the BIG wait)
Google requires a personal developer account to run a **closed test with at least 12
testers who stay opted-in for 14 continuous days** before it will unlock production
(public) access. This is a hard clock. Even with everything else perfect, public Android
release is **at least ~2 weeks out** from the day 12 testers are in.
- **What Cameron does:** gather 12 people willing to install and keep the app for 2 weeks
  (this matches his earlier plan: "Set it up, I'll gather 12 testers"). They join via a
  closed-test opt-in link from the Play Console.
- **What I do:** set up the closed-test track, generate the opt-in link, push the build to
  it, and tell Cameron exactly who needs to tap what.

### Gate 2 — The release upload itself (needs a service-account key — quick once we have it)
To let me upload builds straight to Play (like I do for Apple), EAS needs a **Google Play
service-account JSON key**. We don't have one yet, so `eas submit` for Android is not
wired up (eas.json has `submit.production.ios` only).
- **What Cameron does (one-time, ~5 min, account-owner only):** in Google Play Console →
  Setup → API access, create/link a Google Cloud project, create a service account, grant
  it "Release" permission, and download the JSON key. (Google requires the account owner
  to do this; I can't create credentials on his account.)
- **What I do:** the moment he hands me that JSON file, I add it to
  `mobile/credentials/` (gitignored), wire `submit.production.android` in eas.json, and
  from then on I can upload every Android build myself with one command.

## What I CAN do right now without waiting on Cameron
- Keep the production build current (`cd mobile && npx eas build --platform android
  --profile production --non-interactive --no-wait`).
- Finish the Play **store listing** text (title, short/full description, etc.) — the copy
  is already written in `store-assets/STORE-COPY.md`.
- The Play **graphics** (icon 512, feature graphic 1024x500, phone/tablet screenshots) are
  generated and sitting in `store-assets/` at Google-valid sizes, ready to upload.
  - NOTE: the in-browser uploader is currently broken (rejects host file paths), so the
    graphics either go up via the Play Publishing API once the service-account key exists,
    or Cameron drags them in manually. Either works; the files are ready.

## The single irreversible tap that stays Cameron's (the sworn promise)
Just like iOS, the very last "send to production / roll out to public" button on Google
Play is the one Google requires the account owner to press. I will get everything to that
exact screen, point at the button, and only then hand it to him — never a vague handoff.

## Summary for Cameron (the short version)
1. iOS: **DONE — submitted to Apple, waiting on their review.** Nothing for you to do.
2. Android, to go public, needs from you two things only you can do:
   - **(a)** round up 12 testers for a 14-day closed test (starts the 2-week clock), and
   - **(b)** download one Google Play "service account" key file and send it to me.
   I handle everything else and bring you to the final release button.
