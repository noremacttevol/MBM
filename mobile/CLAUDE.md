# MBM-Mobile — Agent Instructions

**Read [`../AGENT-RULES.md`](../AGENT-RULES.md) first** — the single master manual
(vision, laws, architecture, how Cameron works). Then [`../STATUS.md`](../STATUS.md)
for current build state. Then read the code before changing it.

## This Folder's Specifics

- React Native + Expo app. **All new work happens here.** Never add a web server or
  backend — the app is local-first (Zustand store persisted to AsyncStorage).
- AI calls go directly to Anthropic using `EXPO_PUBLIC_ANTHROPIC_API_KEY` from
  `mobile/.env` (gitignored — never commit it).
- Run with `npx expo start`; test on a real phone via Expo Go.
- Before calling work done, run the self-correction checklist in `AGENT-RULES.md`.

If anything here conflicts with `AGENT-RULES.md`, that file wins.
