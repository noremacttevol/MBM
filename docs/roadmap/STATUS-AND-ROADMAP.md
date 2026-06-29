# MBM — Status & Honest Roadmap (June 25, 2026)

Plain-language snapshot of where things stand and exactly who has to do what next.
Written so Cameron never has to dig through the code to know the state of the app.

---

## The one thing that kept biting us (now fixed for good)

Every time a fix "didn't show up on the phone," the cause was the same: **writing the
code is not the same as building and installing it.** A fix can be correct in the
files, committed, and pushed — and still not be on any phone until a NEW build is
made and installed. The June fixes Cameron tested on the iPhone were in that exact
gap: they were written down, but the last build (build 4) was made from older code
that didn't include them.

Two guardrails now prevent this from sneaking up again:

1. **`scripts/preflight.sh`** — one command (`bash scripts/preflight.sh`) that checks
   no secrets are in git, the app still type-checks, and the server has no syntax
   errors. Run it before every build.
2. **This file** — the running record of what is built vs. what is only written.

---

## DONE — written, type-checked, committed, pushed, and now building

All of the following are in commit `e4a2575` on GitHub (`main`) and are included in
the two builds kicked off today:

- **Cold-open animation** no longer flashes the disclaimer first; the screen fades in
  smoothly. (`HookScreen.tsx`)
- **"Talk About It" header** fixed for small screens: small square icon buttons
  (**+** for new, **🕐** for history), the "Real / Person" label stacked on two
  lines, and the title shrinks to fit so nothing overlaps. (`ChatScreen.tsx`)
- **Profile no longer feels like surveillance.** Dropped the "here's what we noticed
  about you" framing; it now plainly lists what the app keeps, with **Remove** on
  each item. (`ProfileScreen.tsx`, `useAppStore.ts`)
- **Ministry console (admin desk)** survives the Firebase free-tier limit instead of
  freezing on "Loading…", and reads the database less often (15s cache + slower
  poll) so it hits the limit far less. (`admin/inbox.mjs`)
- **Tiered-model + offline research** written up with the key correction: one API
  key can call any model (Haiku/Sonnet/Opus); a second key is only for budget
  separation. Offline AI answers stay parked behind a measured quality gate.
  (`MODEL-ROUTING-AND-OFFLINE-PLAN.md`)

### Builds running right now (from the code above)
- **iOS** — build `26eb6316-0b4e-4c6d-84d8-ed61b6773cdf`
- **Android** — build `c302b9bb-a523-42e2-9327-ddcab0735073` (versionCode 5)
- Watch progress: https://expo.dev/accounts/milkb4meat/projects/mbm/builds
- These take ~20–40 min. When they say **finished**, the new version with every fix
  above exists as an installable app.

---

## WHAT I CAN DO NEXT (no Cameron action needed)

- **Build the tiered-model routing for real** (signal-based: crisis/sharp-debate →
  strongest model, doubt/hard-question → mid, everything else → everyday), with the
  proxy enforcing an allow-list so the phone can never request an expensive model.
  This is the clear, contained next win.
- **Add a "Start fresh" reset** on the Profile screen for the testing phase.
- **Add the well-framed belief/testimony answer option** to dialogue questions so a
  believer can testify instead of being boxed into doubt (Locked Direction #5).
- **Keep tending the ministry console** and the build/verify scripts.
- **Confirm the exact current model IDs** against docs.claude.com before the routing
  ships.

---

## WHAT ONLY CAMERON CAN DO (accounts / real-world / the public step)

These need a human with the accounts and a card; I'll prep everything up to the
button and tell you exactly which button.

1. **The public store release.** Building makes the app; **submitting** sends it to
   Apple App Store / Google Play review for the world to download. That is the one
   irreversible, public step. I will not push the app to public review on my own —
   when the builds finish I'll hand you the ready-to-submit artifacts and the exact
   command/click, and you say go.
2. **Firebase Blaze plan** (paid) if you want the ministry console to stop hitting
   the daily free read limit entirely. It's a billing change on your Google account.
3. **Any new card/billing caps** — e.g., a separate API key with a spending cap for
   the "strongest model" tier, if you decide you want a hard budget.
4. **App Store / Play Console listing details** — screenshots, description, privacy
   answers, age rating — anything Apple/Google ask the account owner to confirm.

---

## How to ship a new version (the repeatable runbook)

1. `bash scripts/preflight.sh` — must say **ALL CHECKS PASSED**.
2. Commit + push the code.
3. Build: `cd mobile && npx eas build --platform all --profile production`.
4. Wait for **finished** at the Expo builds link above.
5. Submit (the public step — Cameron approves): `npx eas submit --platform ios` and
   `--platform android`.
6. Update the **DONE** section of this file so the record stays honest.
