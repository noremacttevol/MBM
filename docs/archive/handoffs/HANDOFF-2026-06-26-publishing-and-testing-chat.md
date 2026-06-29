# MBM — Handoff from the "publishing & testing" chat (2026-06-26)

This is ONE chat's contribution to the consolidated pitch/launch chat Cameron is building.
It records what THIS chat actually did and **directly observed** (mostly inside the live
Google Play Console and from the build files on disk), plus the concerns Cameron raised here.

> Trust note: Cameron is consolidating several chats because they keep contradicting each
> other about the true state. Where this chat's first-hand observations disagree with another
> chat's notes, that conflict is flagged below. **Resolve conflicts by looking at the real
> Play Console / App Store Connect, not by trusting any chat's memory — including this one.**

---

## 0. How to work with Cameron (reinforced this chat)
- Plain language ONLY. He explicitly said the jargon and long explanations overwhelm him
  ("word vomiting on me all this stuff i don't understand"). Keep answers to a few short
  sentences. One step at a time. Don't dump.
- Do the work for him; hand him only the single, simple click he must do himself.
- Be honest fast. He got (rightly) frustrated when an earlier point in this chat told him he
  was "good" when the upload had actually been silently rejected. Own mistakes plainly,
  don't sugarcoat, don't promise "last click" unless it truly is.
- Don't remind him to rotate keys — he asked to stop hearing that.

---

## 1. The simple picture (two phones, two stores)
- **Android (Cameron's own phone)** → Google Play.
- **iPhone (his wife's phone)** → Apple App Store / TestFlight.
- Cameron's near-term goal: get the app onto BOTH phones to test, and have his wife do a
  fresh run on her iPhone and **screenshot the whole experience**. He wanted to add himself
  as an Android tester to try it on his own phone first.

---

## 2. ANDROID — what this chat directly observed (primary source: live Play Console)
- App in Play Console: **"Milk Before Meat", package `com.milk_before_meat`, status DRAFT,
  0 installs.**
- **Release history: "There are no previous releases."** Internal testing track exists,
  testers were already selected (done earlier), but the release has been **stuck as a Draft**
  and never rolled out.
- **Why it was stuck — a signing/key problem, diagnosed from the actual build files:**
  - Old file on disk `com.milk_before_meat.aab` (Jun 20) is **signed with the key Google
    expects** (SHA1 `47:61:62:20:5A:FB:65:37:F1:7C:DE:30:9C:CE:C4:0A:33:4A:DF:C6`) BUT its
    internal package name is wrong (`com.mbm.app`). → rejected for wrong package.
  - Newer file `jun21-prod.aab` (EAS production build) has the **correct package**
    (`com.milk_before_meat`) BUT is **signed with a different key**
    (SHA1 `03:38:D4:03:A4:DC:AA:C4:CD:B7:65:18:FC:6A:B2:C2:3B:43:C6:CF`). → rejected: "signed
    with the wrong key."
  - Root cause: the build's signing key was **rotated** between Jun 20 and Jun 21. EAS now
    holds ONLY the new key (`03:38:D4`); the old key (`47:61:62`) Google expects is gone from
    EAS and there is no local keystore backup on the machine.
- **Two fixes identified:**
  1. **Proper Internal testing track (for the friends/family rollout):** request an
     **upload-key reset** in Play Console to register the new key (`03:38:D4`). The upload
     certificate was exported to `/home/noremacttevol/Desktop/Brain/MBM/upload_certificate.pem`.
     Google can take up to ~48h to process this. NOT done yet.
  2. **Fast path to test on Cameron's own phone NOW — Internal App Sharing.** It ignores the
     key mismatch and just serves the file you give it. This chat turned it on (Cameron
     approved accepting its Terms of Service). Google had to "generate keys" for the new
     developer account first ("up to 48h") — **this finished the same day; Internal App
     Sharing is now LIVE/ready.** The upload page (`play.google.com/console/internal-app-sharing`)
     was opened; a small one-time age/privacy "Accept" box is still pending, then the build
     gets uploaded and produces an instant install link.
- **Correct build file to upload:** `/home/noremacttevol/Desktop/Brain/MBM/jun21-prod.aab`
  (package `com.milk_before_meat`). Do NOT use `com.milk_before_meat.aab` — misleading name,
  wrong internal package.

### ⚠️ CONFLICT to resolve
`HANDOFF-for-pitch-chat.md` (another chat, same date) states Android "already shipped versions
3 and 4" and only needs a quick upload of a "version code 5" `.aab`, with "no new setup and no
new fee." That does **not** match what this chat saw in the live console (Draft, 0 installs,
no release history, EAS builds at version code 2, and a key mismatch blocking upload). One of
these is stale or mistaken. **Verify against the real Play Console before telling Cameron
Android is basically done — getting this wrong is exactly what has eroded his trust.**

---

## 3. APPLE — state this chat touched
- TestFlight build was `1.0.0 (3)`, "Waiting for Review." (Note: another handoff says
  "1.0 build 6" — another number conflict to verify in App Store Connect.)
- This chat filled in and **saved** the previously-blank TestFlight **Marketing URL**
  (`https://milk-b4-meat.web.app/`) and **Privacy Policy URL**
  (`https://milk-b4-meat.web.app/privacy.html`).
- Today an Apple email arrived: **"App Store Connect API Access Request Approved."** That's a
  developer-tooling approval (used by the EAS submit credentials), not the TestFlight review
  itself. It's a sign Apple's side is progressing.
- Next on iPhone: once Apple approves the build, install on the wife's iPhone via the
  TestFlight link and screenshot the fresh run.

---

## 4. WEBSITE — Cameron's stated main worry
- The REAL, working pages are on **Firebase Hosting at `milk-b4-meat.web.app`** (serves the
  `site/` folder): `index.html`, `privacy.html` (well-written), `support.html`. Apple's
  privacy link now points here.
- **`milkb4meat.org` is a Squarespace "under construction" placeholder** that returns a
  soft-200 for every path — i.e., NOT ready. Earlier in this chat an incorrect "website
  verified 200 OK" claim was made and then corrected. Before any PUBLIC launch, the `.org`
  domain should be finished or redirected to the working Firebase site. (Not blocking private
  testing.)

---

## 5. Tool limitations hit this chat (so the next chat doesn't waste time)
- The browser file-upload tool **no longer accepts a file path from disk**, so the actual
  "pick the file" upload step must be done by Cameron with one manual click. EAS Submit for
  Android isn't a workaround here either (no Google service-account key configured; setting one
  up needs Google Cloud API terms — out of scope to do on his behalf).
- The assistant won't click "Accept" on legal terms without Cameron's explicit per-action OK.

---

## 6. Automation set up this chat
- A **daily scheduled task** `mbm-publish-status-check` (runs ~10:09 AM local) checks both the
  Android (Internal App Sharing readiness) and Apple (TestFlight review) status and reports
  back in plain language. It only works when Cameron's Chrome is open and signed in.

---

## 7. THE PITCH TASK (the reason for the new chat) — what Cameron wants
This is the part Cameron most wants carried forward and worked on:
- He wants help **figuring out how to pitch/introduce this app to people** — friends, family,
  and fellow members of The Church of Jesus Christ of Latter-day Saints — to recruit the first
  testers.
- He raised wanting a **recruiting / explanation message** to send to his list, framed around
  his real story: that he's been **learning to build apps as an online-college extra-credit
  discipleship project**.
- He wants an **intake step** in that outreach, including asking **what kind of phone** each
  person has (so he knows whether to send them the Android link or the iPhone/TestFlight link).
- He referred to wanting **"safety thresholds"** for emailing the list — he intends to provide
  those specifics himself; ask him for them rather than inventing them.
- Keep any pitch consistent with the app's own ethic: **no pressure, no shame, meet people
  where they are** (the same "milk before meat" spirit the app is built on).
- Before writing the pitch, ask Cameron **who he most wants to reach first.**

(For app description / positioning material to draw on, see `HANDOFF-for-pitch-chat.md`
sections 2 and 7, and `App Summary Paragraph.md` — but re-verify the "current state" claims.)

---

## 8. One-line status for the new chat
iPhone: submitted, waiting on Apple. Android: NOT yet live (Draft + signing-key mismatch);
fast test path via Internal App Sharing is ready and one upload click away; proper rollout
needs an upload-key reset (~up to 48h). Website: Firebase pages live, `.org` placeholder not
ready. Verify all version numbers and the "already shipped" claim against the real consoles.
