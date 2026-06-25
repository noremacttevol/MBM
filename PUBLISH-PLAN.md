# MBM — Getting it into people's hands (the real, non-localhost plan)

This is the honest path from "works on my computer" to "my friends download it from
the store and I reply to them from anywhere, with my admin team." Nothing here is a
localhost workaround.

There are two separate tracks. They don't depend on each other — we can do both.

---

## TRACK A — A real Android app your friends download

### What's already done (no action needed)
- The project is configured to build a real Android app (Expo/EAS, package `com.mbm.app`).
- **Over-the-air updates are built in.** Once someone has the app, I can push most
  changes (text, screens, fixes) to their phone in seconds — no reinstall.

### The fastest real route: Google Play **Internal Testing**
This is the actual Play Store, but private to people you invite — no public-review
wait, up to 100 testers, they install from a real Play link.

**Steps (only you can do the account ones — they need your identity/payment):**
1. **Make a Google Play developer account** — one-time $25, at play.google.com/console.
   (New accounts need a quick identity verification; usually clears fast.)
2. **Make a free Expo account** at expo.dev (this is what builds the app in the cloud).
3. Tell me when those exist. Then I hand you the exact commands; you run:
   - `eas login` (sign into Expo — your password, in your terminal, never shown to me)
   - `eas build -p android --profile production` → Expo builds it in the cloud and
     gives you a file to upload to Play.
4. In the Play Console: create the app → **Internal testing** → upload that file →
   add your friends' emails → share the install link.
5. Friends tap the link, install from Play, done. To update later: I run/give you
   `eas update` and it lands on their phones.

**Even faster for *today* (optional):** `eas build --profile preview` makes a plain
`.apk` download link you can text to a friend to install directly (they tap "allow
from this source"). Good for a same-day trial while the Play account clears. Same app,
just sideloaded instead of from the store.

### The one decision before building (I'll prep it either way)
The AI chat needs an Anthropic key. We must NOT bake that key into a downloadable app
(anyone could pull it out and run up your bill). Two options:
- **(Recommended) Tiny hosted "key keeper" (proxy)** so the key stays on a server, not
  in the app. The code already exists in `server/`; it needs one cheap/free deploy.
- For a *private same-day APK to close friends only*, embedding the key is a tolerable
  short-term risk — but not for a store release.
I'll set up whichever you choose.

---

## TRACK B — Replying from anywhere, with your admin team (no localhost)

### The requirement (your words)
You need to add people to your admin group and have all of you read/reply from
anywhere. A local desk can't do that — it only runs on your computer.

### The real version
A **hosted admin console with logins**:
- You and each admin sign in with your own account.
- Everyone sees the incoming messages and replies from any browser or phone.
- You add/remove admins (your "group") whenever you want.
- It runs on the Firebase you already have — replies flow through the same cloud the
  app already uses.

**What I'll build (code — no account needed from you):**
- The hosted console (read threads, reply, triage, the crisis/cancel badges already
  built), protected by login.
- Admin accounts via Firebase Authentication.
- The security rules that let your admin accounts (and only them) read/reply to
  everyone, while regular users still only see their own messages.

**What needs you (your accounts):**
- Turn on Email/Password sign-in in Firebase (one toggle).
- Publish the updated security rules (one command/click).
- Deploy the console to Firebase Hosting (one command) → gives a real
  `https://...web.app` link you and your team log into.
- Create each admin's login.

### For *today*, while Track B is built
You can keep replying from the local desk for a tiny first test (it still works, your
friends can fully use the app). The moment the hosted console is live, you switch to it
and never touch localhost again.

---

## Honest summary of who does what
- **I do:** all the code, config, security rules, the hosted console, the proxy,
  exact command sheets, and push OTA updates.
- **You do (only you can):** create the Expo + Google Play + (if proxy) host accounts,
  run the `eas`/deploy commands in your terminal (your passwords stay with you), and
  click the Play Console / Firebase toggles.
- **Realistic timing:** a sideload APK can be in a friend's hands *today*; a real Play
  internal-testing link + hosted multi-admin console is a *this-week* thing, gated only
  by account setup and Google's check — not by our code.
