# MBM-Mobile — Agent Instructions

Full project rules are at: ~/Desktop/Brain/MBM/AGENT-RULES.md
Read that file first. Everything in it applies here.

## This Folder's Specific Rules

- This is a React Native + Expo mobile app. Never add a web server or backend.
- Database is expo-sqlite. It lives inside the app. No external DB.
- Run with: `npx expo start` — test on phone via Expo Go.
- Three screens only right now: HookScreen → OnboardScreen → FeedScreen.
- The routing logic in `src/engine/router.js` is the hidden brain. Never expose it to the UI.
- Before touching any file, read it first.
- Before calling work done, run the self-correction checklist in AGENT-RULES.md.
