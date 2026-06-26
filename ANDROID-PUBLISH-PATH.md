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

### Gate 2 — The release upload itself (service-account key — DONE 2026-06-26)
To let me upload builds straight to Play (like I do for Apple), EAS needs a **Google Play
service-account JSON key**. This is now set up.

IMPORTANT CORRECTION: the old "Google Play Console → Setup → API access" page **no longer
exists** in Cameron's console version (verified — the page and its direct URL both redirect
to home). The modern path is Google Cloud Console + Play Console "Users and permissions",
which is what we used:
- Google Cloud Console → created project **"MBM Publishing"** (id `mbm-publishing`).
- Created service account **`mbm-play-publisher@mbm-publishing.iam.gserviceaccount.com`**.
- Created a JSON key for it; the file lives at
  `mobile/credentials/play-service-account.json` (gitignored). NOT committed.
- Enabled the **Google Play Android Developer API** (`androidpublisher.googleapis.com`)
  on the project.
- Wired `submit.production.android` in `mobile/eas.json`
  (`serviceAccountKeyPath` + `track: internal`).
- **The one owner-only step (Cameron's clicks):** Play Console → Users and permissions →
  Invite the service-account email and grant it release permission for the Milk Before Meat
  app, then Send. (Granting access is account-owner-only; I set the form up to that point.)
- From here I can upload every Android build myself with `eas submit --platform android`.

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
2. Android service-account key: **DONE 2026-06-26** (created in Google Cloud Console, wired
   into EAS; the only owner click was granting the robot account release permission in Play
   Console). I can now upload Android builds automatically, same as iOS.
3. Android, to go PUBLIC, now needs only ONE thing from you: round up **12 testers** for a
   **14-day closed test** (starts the 2-week clock). That is genuinely the last gate.
   I set up the closed-test track and the tester opt-in link; you send it to 12 people.
