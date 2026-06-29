# MBM — CONSOLIDATED HANDOFF (2026-06-26)

**This is the single, clean handoff Cameron asked for.** His chats kept contradicting
each other, so this file pulls everything into one place: what the app is, what's truly
done vs. not, his concerns, and the pitch task. Paste this into the new pitch chat.

> **One rule above all:** When this file or any doc says "X is done/live/published," the
> new chat must VERIFY it against the real Apple App Store Connect and Google Play Console
> before repeating it to Cameron. Trusting a chat's memory over the live console is exactly
> what broke Cameron's trust. Directly-observed live facts beat any written note — including
> this one.

---

## 0. How to work with Cameron (most important section)
- **Plain language, short answers.** No jargon, no long explanations, no "word vomiting."
  A few short sentences. One step at a time.
- **Do the work for him.** Take initiative. Hand him only the single simple click he must
  do himself (passwords, payments, the final public-release tap). Never make him the bug
  reporter or ask him to re-explain settled things.
- **Be honest fast, own mistakes plainly.** He lost trust when chats said things were "done"
  that weren't. Don't sugarcoat, don't reassure without proof. If you're not sure, say so and
  go look.
- **Never enter his passwords or 2FA.** Hand those back to him every time.
- **Don't nag** about rotating keys — he asked to stop hearing that.

---

## 1. What MBM is (for the pitch)
**MBM = "Milk Before Meat."** A mobile gospel-outreach app (React Native + Expo) for The
Church of Jesus Christ of Latter-day Saints, modeled on how Christ ministered: meet a person
exactly where they are, learn them over time, and move gently from foundational truth ("milk")
toward the restored gospel ("meat") — never with visible gates, pressure, or shame.

The experience: a calm "sanctuary" cold-open, then a short, beautifully told scripture story
ending in one open question. The app quietly learns from answers and personalizes a feed.
A real human is always one tap away ("Talk About It"). Nothing is ever labeled or waved in
front of seekers — the routing is invisible. No login or account required.

**What makes it worth pitching:** invisible, loving personalization (not surveys or gates);
story-first onboarding; a growing personal record of stories and answers on the Profile that
pulls people back; always a real person available; it never argues doctrine — it lets Jesus'
own words, from scripture people already accept, do the work.

---

## 2. CURRENT STATE — what's actually true (verify before repeating)

### iOS (Apple) — basically done, just waiting on Apple
- **Directly observed in App Store Connect THIS session (most reliable):**
  - App "Milk Before Meat", bundle `org.milkb4meat.app`. Account holder
    `noremacprojects@gmail.com` (Cameron Lovett).
  - **Build 4 = 1.0.0 (4)**, uploaded Jun 25, **"Waiting for Review."** Attached to both the
    internal team group AND the external "Public Beta Testers" group.
  - **Build 3 (1.0.0(3)) was EXPIRED this session** to clean up the "multiple versions in
    review" mess — only Build 4 is live now.
  - **Public TestFlight link is live: https://testflight.apple.com/join/cPNpeh3H** — Build 4 is
    attached to it. Once Apple finishes the one-time Beta App Review (hours), anyone with that
    link can install on an iPhone **with no account and no payment.**
- ⚠️ **Build-number conflict to resolve:** the project docs (SESSION-LOG, START-HERE,
  IOS-STATUS-AND-APPLE-READINESS) say iOS is **build 6, submitted for full public App Store
  review.** But the live App Store Connect this session showed **build 4 in TestFlight review**,
  not build 6, and not a public-store submission. **The new chat must open App Store Connect and
  confirm which is true before telling Cameron iOS is "submitted for the public store."**

### iOS testing path — settled the professional way
- Use **External testing** (the public link above): no Apple account, no developer purchase,
  shareable to all friends/family. This is the path to give the wife and everyone else.
- **Do NOT add testers as internal/team members** (Users and Access). That path twice pushed
  Cameron's wife toward "purchase a Developer subscription." The wife's team-member invite was
  **removed** this session to stop that prompt. Internal testing = team members = bad path here.
- Cameron's wife: **Ellin Chartier, ellinchartier@gmail.com**, already has TestFlight installed.
  Send her the public link once Build 4 is approved.
- Note: `noremacttevol@gmail.com` (Cameron's personal email) is **locked for security** on the
  Apple side — don't try to unlock it; that's an account-recovery action for Cameron only.

### Android (Google Play) — THIS IS THE BIG UNRESOLVED CONFLICT
Two different states are claimed and **they cannot both be true. Verify in the live Play Console
before saying anything to Cameron.**
- **Optimistic version (START-HERE.md + SESSION-LOG.md, 2026-06-26):** Automated Google Play
  publishing is LIVE and verified; a service account pushed **version code 6** to the internal
  track, status COMPLETED; internal-testing opt-in link
  `https://play.google.com/apps/internaltest/4700576250998456373`; store listing text + icon +
  feature graph done; only screenshots and the 12-tester / 14-day closed test remain.
- **Pessimistic version (HANDOFF-2026-06-26-publishing-and-testing-chat.md):** App is still a
  **DRAFT, 0 installs, "no previous releases,"** stuck on a **signing-key mismatch** — the build
  with the right package name is signed with the wrong key, and the old key Google expects is
  gone from EAS. Fast test path via "Internal App Sharing" was being set up; a proper fix needs a
  Play Console **upload-key reset** (~up to 48h).
- **What to do:** open Google Play Console → MBM → check **Release > Releases overview** and the
  internal testing track. If there's a real release serving a build, the optimistic version is
  right. If it says "no previous releases"/Draft, the signing problem is real. **Don't guess.**

### Website
- Working pages are on **Firebase Hosting: `milk-b4-meat.web.app`** (`index.html`, a well-written
  `privacy.html`, `support.html`). Apple's privacy link points here.
- **`milkb4meat.org` is a Squarespace "under construction" placeholder** — not ready. Before any
  PUBLIC launch, finish it or redirect it to the Firebase site. Not a blocker for private testing.

### Accounts (all exist — never tell Cameron to create these or pay setup fees)
Apple Developer (paid), Google Play Console ($25 paid, verified), Expo/EAS (`milkb4meat`),
Railway (`mbm-proxy`), Firebase (live), domain `milkb4meat.org` (owned).

---

## 3. The ONE recurring bug that wastes Cameron's time
**Writing/committing code does NOT put it on a phone.** A fix can be correct in the files,
committed, and pushed — and still not be on any device until a NEW build is made AND installed.
Several "the fix isn't there" complaints were all this. When Cameron says a fix is missing,
first check which build is actually installed on his phone, not whether the code is right.
(JS-only changes can ship instantly via `eas update` OTA, no rebuild.)

---

## 4. Cameron's standing concerns (carry these forward)
- **Trust / memory continuity:** chats keep losing the true state. He wants a reliable system so
  every new chat knows what's done before acting. (This file is part of that fix.)
- **Cost at scale:** wants honest, upfront numbers on what running the app costs as it grows
  (Firebase free-tier read limits, AI API costs). No surprises.
- **AI model tiering:** route harder/crisis questions to a stronger model, everyday chat to a
  cheaper one, with a safety allow-list so the phone can't request expensive models. Plan in
  `MODEL-ROUTING-AND-OFFLINE-PLAN.md`. Not built yet.
- **Offline mode:** do NOT ship offline AI answers until quality is measured against a steady
  threshold. He won't allow low-quality answers going out unmonitored.
- **Professionalism:** he repeatedly rejected clunky/email-by-email approaches. Whatever the
  testers use must look clean and be easy for non-technical friends (a shareable link).

---

## 5. THE PITCH TASK — the reason for the new chat
This is what Cameron most wants worked on now.
- Help him **figure out how to pitch/introduce this app** to friends, family, and fellow members
  of The Church of Jesus Christ of Latter-day Saints, to recruit the first testers.
- He wants a **recruiting/explanation message** for his list, framed around his real story:
  he's been **learning to build apps as an online-college extra-credit discipleship project.**
- Include an **intake step**: ask each person **what kind of phone** they have, so he knows
  whether to send the Android link or the iPhone/TestFlight link.
- He mentioned wanting **"safety thresholds"** for emailing the list — he'll provide those
  specifics himself; **ask him for them, don't invent them.**
- Keep the pitch consistent with the app's own ethic: **no pressure, no shame, meet people where
  they are** — the same "milk before meat" spirit.
- **Before writing the pitch, ask Cameron who he most wants to reach first** (seekers; struggling
  or falling-away members; active members wanting better-than-doomscrolling content; people his
  friends/ward could share it with).

Deliverables to explore with him: the one-sentence hook; a short "what it is / why it's
different" blurb for word of mouth and the store/TestFlight invite; a phone-type intake question;
a few talking points — all no-pressure.

---

## 6. One-line status
**iPhone:** Build 4 in TestFlight review, public link live, wife's bad "internal" invite removed —
confirm whether it's really build 4 (TestFlight) or build 6 (public store) in App Store Connect.
**Android:** CONFLICTED — either internal track live (vc6) or still Draft + signing-key blocked;
check the live Play Console first. **Website:** Firebase pages live, `.org` placeholder not ready.
**Pitch:** ask Cameron who to reach first, then draft the no-pressure invite with a phone-type
intake step.

---

## 7. Where the real truth lives (file authority)
1. The **live Apple App Store Connect / Google Play Console** — beats every doc.
2. `START-HERE.md` — current state per the project (but it conflicts with live obs on iOS build #).
3. `AGENT-RULES.md` — vision, laws, how to behave.
4. `SESSION-LOG.md` — session chain.
Everything else (the many other handoff/.md files) is historical context and may be stale.
