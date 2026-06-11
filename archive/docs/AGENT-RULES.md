# MBM — Agent Rules & Project Bible
**Read this first. Every session. No exceptions.**
This file exists so Cameron does not have to re-explain the vision every time. If you are an AI agent working on this project, this document contains everything you need. Do not ask Cameron to clarify what is already answered here.

---

## What This App Is

MBM (Milk Before Meat) is a mobile gospel outreach app.

The single best way to understand it: Facebook spreads entertainment through algorithms that learn what a person responds to, then keep serving more of it. MBM does the exact same thing — but instead of entertainment, it spreads the gospel of Jesus Christ. Instead of optimizing for addictive engagement, it optimizes for spiritual growth. Instead of pushing people toward the natural man, it moves them toward Christ.

The app learns who a person is spiritually — where they are right now, what kind of content resonates with them, what questions they are asking — and then routes them toward the truth they are ready to receive. It meets people exactly where they are. It does not push. It invites.

The ultimate destination of the app is to introduce people to the restored gospel of Jesus Christ as found in The Church of Jesus Christ of Latter-day Saints. But that destination is never revealed upfront, never forced, and never the starting point. The path leads there naturally through progressive trust.

---

## The Single Most Important Rule

**Never lead with LDS. Never reveal the destination to a user who is not ready for it.**

A secular user, an atheist, or someone in a faith crisis must never see the words "Latter-day Saints," "LDS," "Joseph Smith," "Book of Mormon," or "Restoration" until they have arrived there themselves through their own curiosity and the app's gentle escalation.

This is not deception. This is exactly how Christ taught — He met people where they were. He did not open with theology. He opened with a question, a story, an act of service. The doctrine came later, when trust was established.

The app must do the same. This rule overrides everything else.

---

## Working Guardrails for This Build

These are the operating principles we will keep remembering while building and refining the app:

### Launch rules (non-negotiable)
1. The canonical Expo app is always `mobile/`.
2. Do not run raw `npx expo start` from the repo root.
3. Use the repo-root launcher scripts instead:
   - `npm run mobile:web` for the stable browser preview
   - `npm run mobile:dev` for the normal Expo path
   - `npm run mobile:tunnel` only if a tunnel is specifically needed
4. If Expo says the port is in use, accept the next port instead of fighting the old one.
5. If phone testing fails, verify the web preview path first before spending time on tunnel troubleshooting.
6. Keep this file, `LESSONS-LEARNED.md`, and `TONIGHT-STARTUP.md` updated after every session.

1. Keep the richer mobile experience, including the main tabs and deeper pages, but make them comfortable to use on real phones.
2. Make the bottom navigation touch-friendly and tall enough to avoid interfering with Android gesture areas or iPhone home-area spacing.
3. Story-first onboarding remains the default. The user should feel seen before any deeper theological invitation appears.
4. Deeper LDS-specific content must be introduced only when the user has shown real openness, curiosity, or a desire to understand the truth more fully.
5. Questions should invite honesty and spiritual reflection — for example, whether God is good, whether the person is open to revelation, or whether they want the deeper story behind the gospel.
6. The Creation Dilemma and Restoration material are not front-loaded. They appear only after readiness signals are present.

These guardrails are now part of the project standard and should guide every future improvement.

---

## The Three Content Feeds

All content in the app falls into one of three hidden categories. These labels are NEVER shown to the user.

### MILK — Foundational Light
**Who gets this:** Secular users, people with zero gospel exposure, spiritually sensitive seekers, anyone who chose "peace and hope" or "never thought about it."
**What it contains:** Universal human goodness. The Sermon on the Mount. The Good Samaritan. The Prodigal Son. Psalm 23. Stories about love, forgiveness, sacrifice, beauty in creation. The Light of Christ as experienced by every human who has ever felt moved by goodness — whether or not they have a name for it.
**What it does NOT contain:** Doctrine. Institutional references. The word "LDS." Anything that would make a non-Christian feel targeted.
**Goal:** Make the user feel understood, seen, and at peace. Name the feeling they already have. Build the foundation.

### BRIDGE — Apologetics and Evidence
**Who gets this:** Skeptics, analytical thinkers, atheists, people in faith transitions, anyone who said "I questioned it heavily."
**What it contains:** C.S. Lewis. Gary Habermas. Tim Keller. Historical evidence for the resurrection. Manuscript reliability. The problem of evil. Francis Collins on science and faith. Intellectual frameworks that take doubt seriously and answer it honestly.
**What it does NOT contain:** Emotional appeals that would feel manipulative to a logical thinker. LDS-specific content. Pressure.
**Goal:** Demonstrate that faith and reason are not enemies. Earn the right to go deeper by respecting the user's intellect.

### MAINTENANCE — Active Member Deepening
**Who gets this:** Existing Latter-day Saints, people who identified as already believing through family tradition.
**What it contains:** General Conference talks. Come Follow Me. Book of Mormon. Preach My Gospel. Elder Holland. President Nelson. Doctrine and Covenants. Temple preparation. Ministering.
**What it does NOT contain:** Basic Christianity 101 content they already know. Apologetics they do not need.
**Goal:** Deepen conversion. Strengthen testimony. Help them minister to others offline.

---

## The Routing Engine

This is the hidden brain of the app. The user never sees it. It works silently behind every interaction.

### Onboarding Question
Every new user sees one question after the opening animation:

> *"How did the very first time you ever heard about Jesus Christ defying death make you feel?"*

Their answer silently assigns them to a feed:

| Answer | Hidden Profile | Feed Assigned |
|--------|---------------|---------------|
| "My parents told me, I just believed it." | MEMBER | MAINTENANCE |
| "I questioned it — it sounded impossible." | SKEPTIC | BRIDGE |
| "It gave me deep peace and hope." | SEEKER | MILK |
| "I've never really thought about it until now." | SECULAR | MILK |
| "Other — in my own words." | UNKNOWN | Keyword NLP → best match |

### Escalation (Pull-Based Only)
The user moves up the ladder ONLY when THEY ask for it. Never push them.
- "Take me deeper" button: MILK → BRIDGE → MAINTENANCE (one step at a time)
- This is the only path to LDS content for a secular user. They must walk it themselves.

### Safety Valve
If a user disengages, drops interaction, or taps "Keep it simple":
- Immediately reset to MILK feed
- Reset resonance style to "comfort"
- No explanation given. Just quietly serve them something safe and warm.

### Resonance Matching
Within each feed, content is served by resonance style match first, then randomized:
- Emotional → stories, scripture, human moments
- Logical → apologetics, historical evidence, intellectual arguments
- Comfort → peace-focused psalms, rest, gentleness
- Moral → goodness in action, service, love your neighbor

---

## Screen Time Cap

After 5 content items, the feed locks and displays:

> *"You have filled your cup with light for today. Close the app. Step away from the screen. Go share that light with someone in the real world."*

This is non-negotiable. It is the most Christ-like design decision in the app. It proves MBM is not an engagement trap. It must always work. Never remove it or make it dismissible.

---

## Opening Animation

Every user sees the same opening screen regardless of their background:
- A minimalist animated empty tomb — stone rolling away
- Text: **"He Is Risen."**
- Subtext: "Every moment of pure peace you have ever felt has a source."
- Button: "I want to understand that"

This is the hook. It is universal. Even a secular person knows the Easter story. The animation creates curiosity before it asks anything. Do not skip it. Do not replace it with a login screen or a splash screen with a logo.

---

## Tech Stack (Non-Negotiable)

**This is a mobile app. Not a web app. Not a desktop app. Not a localhost server.**

| Layer | Technology | Rule |
|-------|-----------|------|
| Framework | React Native + Expo | No Flutter, no web React, no native Xcode/Android Studio needed for prototype |
| Database | expo-sqlite | Embedded in the app. No backend server. Runs offline. |
| Navigation | React Navigation (native stack) | Three screens: Hook → Onboard → Feed |
| Styling | StyleSheet API | Dark, minimal, serif font aesthetic. Background: #0a0a0f |
| Testing | Expo Go on real phone | Scan QR from `npx expo start`. No simulator required. |

**Current codebase lives at:** `~/Desktop/Brain/MBM/mobile/`

The agent must NEVER produce:
- A Flask server
- A FastAPI server
- A web-only React app
- Anything that requires a terminal to stay open for the app to function on a phone

---

## Content Rules

1. **No AI-generated doctrine.** The app routes to verified content — it does not generate scripture, theological claims, or doctrinal statements. AI writes the app code. AI does not write the gospel.
2. **All content must link to a real, verifiable source.** LDS.org, known apologists (C.S. Lewis Institute, Gary Habermas, Tim Keller), scripture references with chapter/verse.
3. **No hallucinated scripture.** If a content item references a scripture, it must be a real reference that exists at the given URL.
4. **The LDS church is never named to MILK or BRIDGE users.** Content for those feeds must not include links to churchofjesuschrist.org or mention of Joseph Smith.

---

## What "Done" Looks Like

Before calling any work complete, the agent must verify:

- [ ] The app runs on a real phone via Expo Go without errors
- [ ] The opening animation plays on launch
- [ ] All 5 onboarding choices route correctly to the right feed (silently)
- [ ] The feed shows content matching the user's hidden profile
- [ ] "Take me deeper" escalates the feed by one level
- [ ] "Keep it simple" drops the feed back to MILK
- [ ] The screen time cap triggers after 5 items and cannot be bypassed
- [ ] No LDS-specific content appears in MILK or BRIDGE feeds
- [ ] No backend server is required for the app to function

---

## What the Agent Must Never Do

- Build a web app or localhost server instead of a mobile app
- Show the words MILK, BRIDGE, or MAINTENANCE in the user interface
- Mention "Latter-day Saints," "LDS," or "Joseph Smith" to MILK/BRIDGE users
- Generate scripture, doctrinal statements, or theological claims from AI
- Remove or make the screen time cap dismissible
- Skip the "He Is Risen" opening animation
- Ask Cameron to explain the vision again — it is all in this file
- Produce a large, partially-working app and call it done
- Rebuild what already exists — read the current codebase first

---

## Self-Correction Protocol

After every output, the agent runs this checklist internally before presenting work:

1. Is this a mobile app (Expo) or something else? If something else — scrap and rebuild.
2. Does any user-facing screen show routing labels or LDS content to non-members? If yes — fix it.
3. Does the screen time cap work? If no — implement it before calling done.
4. Did I generate any theological content from AI instead of linking to a verified source? If yes — replace with a real link.
5. Does the app require a running terminal/server to work on a phone? If yes — rearchitect it.

If the agent finds a problem on any of these checks, it fixes the problem silently and presents only the corrected output. It does not present the broken version and ask Cameron what to do.

---

## Cameron's Role

Cameron is the vision holder and the theological authority on this project. He is not the syntax writer, the debugger, or the prompt engineer. His job is to say what is right and wrong from a gospel perspective — not to continuously re-explain what the app is or correct technical mistakes.

If the agent is doing its job, Cameron should only need to weigh in on:
- Whether a piece of content feels right spiritually
- Whether a design choice matches Christ's method of ministering
- Whether the app is ready to show to another person

Everything else — the code, the routing logic, the database, the UI, the self-correction — is the agent's responsibility.

---

## Current Build Status (as of 2026-06-05)

| Component | Status |
|-----------|--------|
| React Native / Expo project | Complete — `~/Desktop/Brain/MBM/mobile/` |
| expo-sqlite local database | Complete — auto-seeds on first launch |
| 30 seed content items | Complete — MILK (10), BRIDGE (10), MAINTENANCE (10) |
| Hidden routing engine | Complete — answer map + keyword NLP fallback |
| HookScreen (He Is Risen animation) | Complete |
| OnboardScreen (5-choice question) | Complete |
| FeedScreen (cards + time cap) | Complete |
| Escalation logic | Complete |
| Safety valve | Complete |
| **App tested on real phone** | **Pending — needs Expo Go scan** |
| Content expanded beyond 30 items | Not started |
| User persistence across sessions | Not started |
| ML-based resonance learning | Not started (Phase 2) |

---

## The Vision in One Sentence

Build what Facebook built — but aim it at Christ.
