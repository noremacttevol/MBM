# MBM-Mobile — Agent Instructions
**Read this first. Then read ~/Desktop/Brain/MBM/AGENT-RULES.md. Then read the current code. Then build.**

---

## You Are Working Here

The MBM mobile app lives at: `~/Desktop/Brain/MBM/mobile/`

Do NOT touch `~/Desktop/Brain/MBM/app/` — that was a mistake by a previous agent. It is a dead FastAPI server that violates the project rules. Ignore it completely.

---

## What Is Already Built and Working

| File | What It Does | Status |
|------|-------------|--------|
| `App.tsx` | Navigation entry point for the Expo app | Done |
| `src/navigation/AppNavigator.tsx` | Main stack + tab navigation | Done |
| `src/screens/HookScreen.tsx` | "He Is Risen" opening animation | Done |
| `src/screens/OnboardScreen.tsx` | Single routing question, 5 answers | Done |
| `src/screens/FeedScreen.tsx` | Feed cards, 5-item cap, escalation/safety-valve buttons | Done |
| `src/store/useAppStore.ts` | App state and time-cap logic | Done |
| `src/data/content.ts` | Content feed data used by the app | Done |
| `src/data/questionBank.ts` | Onboarding question and choices | Done |

**Do not rebuild any of these.** Read them first. Build on top of what exists.

---

## What Is Not Done Yet

Work through these in order. Do not skip ahead.

### 1. Verify the app actually runs
```bash
cd ~/Desktop/Brain/MBM/mobile && npx expo start
```
Fix any errors before doing anything else. The app must show a QR code with no crashes.

### 2. User persistence across sessions
Right now each app launch is a fresh session. `user_session` rows exist but nothing carries over when the app closes.

What to build:
- On first launch: run onboarding, store `sessionId` in `AsyncStorage`
- On subsequent launches: read the stored `sessionId`, skip onboarding, go straight to feed
- "Reset my profile" button on the feed screen that clears `AsyncStorage` and restarts from HookScreen

### 3. Feed history (no repeats)
Right now the same content can appear multiple times in the same session.

What to build:
- Track which `content_id` values the user has already seen in `interaction_log`
- Exclude seen items from the feed query in `router.js`
- When all items in the user's feed tag are exhausted, show: "You have seen everything available. Come back tomorrow."

### 4. Expand content beyond 30 items
The seed has 30 items. Each feed (MILK, BRIDGE, MAINTENANCE) only has 10.

What to build:
- Add 10 more items to each feed tag in `seed.js` (30 new items, 90 total)
- Follow the content rules in AGENT-RULES.md: real sources, real URLs, no AI-generated doctrine
- After adding, re-seed the database by dropping and recreating the content table

### 5. Phase 2 — ML resonance learning (do not start until 1–4 are done)
The router currently uses simple tag + resonance_style matching. Phase 2 replaces this with a learned model trained on `interaction_log` data.

Do not start this until there is real interaction data from real users.

---

## How to Run the App

```bash
cd ~/Desktop/Brain/MBM/mobile
npx expo start
```

Scan the QR code with Expo Go on a real phone. That is the only test that matters.

---

## Rules That Cannot Be Broken

These come from AGENT-RULES.md. They apply here too.

1. This is a mobile app. Never add a server, backend, or API.
2. Keep the richer multi-screen experience, but make the bottom tabs tall enough and easy to tap on real devices.
3. Never show the words MILK, BRIDGE, or MAINTENANCE in the UI.
4. Never mention LDS, Latter-day Saints, Joseph Smith, or the Restoration to users in MILK or BRIDGE feeds.
5. Deeper LDS theology appears only when the user has signaled real openness, curiosity, or a desire to go further.
6. The 5-item screen time cap must always work and cannot be bypassed.
7. Never generate scripture or theological claims from AI — only link to real, verified sources.
8. Read the current code before writing any new code.
9. Run the self-correction checklist in AGENT-RULES.md before reporting any work as done.
10. Do not ask Cameron to re-explain the vision. It is in AGENT-RULES.md.

---

## What "Done" Means

Before reporting anything as complete:
- The app runs on a real phone via Expo Go with no errors
- The feature works end-to-end on the phone, not just in a terminal
- You have run the self-correction checklist from AGENT-RULES.md
