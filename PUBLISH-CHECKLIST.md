# MBM — Publish to Google Play Internal Testing (Android)

The plain, ordered path to a real Play install link you can text to up to 100
people — no public review wait. **[YOU]** = only you can do it (accounts/payment).
**[ME]** = I do it, no account needed from you.

Internal testing is the fast lane on purpose: the new "20 testers for 14 days"
rule Google added is only for *public* release, **not** internal testing. So this
route has no waiting period.

---

## The big picture (why these steps exist)
To put the app on Play you need four things lined up: an account to build it
(Expo), an account to publish it (Google Play), your AI key kept OUT of the
downloadable app (a tiny proxy), and a few required links/forms (privacy page,
data form). That's the whole list. Everything below is just doing those in order.

---

## Step 1 — Accounts to start now (do these first; one has a wait) **[YOU]**

- [ ] **Google Play developer account** — https://play.google.com/console
      $25 once. It asks for a quick identity check that can take a day or two, so
      start it *first* and let it process while we do everything else.
- [ ] **Free Expo account** — https://expo.dev (this is the cloud that builds your
      app). Just sign up; nothing to pay.

Tell me when these exist. You never share passwords with me — you'll run the
sign-in yourself when we build.

---

## Step 2 — Put your website pages online (gives Google your privacy link) **[YOU + ME]**

Google requires a public **privacy policy URL**. Your pages are already written
(`site/index.html`, `site/privacy.html`, `site/support.html`). They just need to
be live at milkb4meat.org.

- [ ] **[YOU]** At your domain registrar, set up **email forwarding** so these
      reach your inbox: `hello@`, `support@`, `privacy@` → your normal email.
      (Most registrars do this free — the site pages use these addresses.)
- [ ] **[ME]** Host the three pages. Easiest is Firebase Hosting (you already have
      Firebase) — I'll give you a one-time `firebase deploy` command, or we can use
      Cloudflare Pages. Result: `https://milkb4meat.org/privacy.html` works.

When done you'll have:
`https://milkb4meat.org` · `/privacy.html` · `/support.html`

---

## Step 3 — Keep your AI key safe (the one real code requirement) **[YOU + ME]**

A downloaded app must NOT contain your Anthropic key, or someone could pull it out
and run up your bill. Your app already supports the safe way (a tiny "key keeper"
proxy) — it just needs to be running somewhere.

- [ ] **[YOU]** Make a free **Railway** account — https://railway.app (the host for
      the little proxy). The proxy code already exists in `server/`.
- [ ] **[ME]** Prep the proxy for deploy and give you the exact deploy steps; you
      click deploy and paste me the URL it gives back.
- [ ] **[ME]** Put your *public* settings + that proxy URL into the build config,
      and deliberately leave the secret key out. (I'll show you the diff.)

> If you'd rather not add Railway, the proxy can run on a couple of other free
> hosts — tell me and I'll pick the simplest.

---

## Step 4 — Build the app **[YOU runs, ME prepares]**

- [ ] **[ME]** Final pre-build check (already passing: 0 TypeScript errors) and
      confirm the build config.
- [ ] **[YOU]** In your terminal:
      ```
      cd ~/Desktop/Brain/MBM/mobile
      npx eas-cli login          # your Expo login — stays with you
      npx eas-cli build -p android --profile production
      ```
      Expo builds it in the cloud (~10–20 min) and gives you an **.aab** file to
      download. (Run it from the `mobile` folder — the earlier failure was from
      running it in the wrong place.)

---

## Step 5 — Set it up in Play Console **[YOU clicks, ME provides the words]**

In https://play.google.com/console → create app "Milk Before Meat" → then:

- [ ] **Internal testing → Create release → upload the .aab** from Step 4.
- [ ] **Store listing** — paste the text I provide (below in this file).
- [ ] **Privacy policy** — paste `https://milkb4meat.org/privacy.html`.
- [ ] **App access** — note that almost everything works with no login; the AI and
      "talk to a real person" need internet. (I'll give exact wording.)
- [ ] **Data safety form** — use my answers (below).
- [ ] **Content rating** — answer honestly; I've noted what to expect (below).
- [ ] **Screenshots** — **[ME]** I'll generate phone screenshots for you to upload.
- [ ] **Testers** — add your friends' email addresses, **Save**, then **Roll out**.
- [ ] Copy the **install link** and share it. They tap, install from Play, done.

---

## Step 6 — Updates after launch **[ME]**
Most changes (text, screens, fixes) I push over-the-air with `eas update` — they
land on testers' phones in seconds, no reinstall. A new .aab is only needed for
deeper changes.

---

## Paste-ready: Store listing text

**App name:** Milk Before Meat

**Short description (max 80 chars):**
A quiet place to be met where you are, and pointed gently toward Jesus Christ.

**Full description:**
Milk Before Meat is a calm, unhurried space made to meet you exactly where you
are. Instead of noise and pressure, it offers a short story, an honest question,
and room to think — and it remembers what matters to you so each visit feels
personal.

Talk with a thoughtful AI companion any time, keep a private journal that never
leaves your phone, and whenever you want, reach a real person with a single tap —
no account, no sign-up, no pressure. You are always free to go at your own pace.

What's inside:
• A gentle daily story and one honest question
• A private, on-device journal
• A caring AI to talk things through with
• A real human, always one tap away
• No ads, ever — and your words stay yours

This app points you toward Jesus Christ. It is not a substitute for prayer,
Scripture, or the people who love you.

---

## Paste-ready: Data safety form answers

- **Does your app collect or share user data?** Yes (only the messages a person
  chooses to send).
- **Data collected:**
  - *Messages* — the notes a user sends to the AI and to "talk to a real person."
    Purpose: **App functionality**. **Not** shared for advertising. **Not** sold.
    Processed by our providers (Anthropic for AI replies; Google Firebase for the
    human inbox).
- **No** name, email, phone, location, contacts, photos, or identifiers collected
  (the app uses an anonymous ID; almost all activity stays on the device).
- **Is data encrypted in transit?** Yes.
- **Can users request data deletion?** Yes — via privacy@milkb4meat.org (also
  stated on the privacy page).

---

## What to expect: Content rating
The questionnaire is automated (IARC). MBM has no violence, sex, profanity, or
gambling, so the rating will be low (Everyone / PEGI 3-ish). Because users can
send messages to a real person, it may ask about "users interacting" or
"user-generated content" — answer **yes** honestly; it just notes that people can
communicate. It won't block you.

---

## Honest timing
- Today/this week: accounts created, site live, proxy deployed, build made.
- Gated only by Google's one-time ID check on your developer account — start that
  first. Once it clears and the .aab is uploaded, your testers can be in within
  hours.
