# MBM-Mobile — Agent Entry Point

**Read [`../AGENT-RULES.md`](../AGENT-RULES.md) first.** It is the single master
manual: the vision, the laws, the architecture, and how Cameron wants to work. Then
read [`../STATUS.md`](../STATUS.md) for current build state, then read the code.

## This folder

- This is the React Native + Expo app. **All new work happens here.** Never add a web
  server or backend; the app is local-first (state in a Zustand store persisted to
  AsyncStorage).
- Run it: `cd mobile && npx expo start`, then scan the QR with Expo Go on a real phone.
- Before reporting work done, run the self-correction checklist in `AGENT-RULES.md`
  (read the code first, obey the laws, typecheck with `npx tsc --noEmit`, verify the
  UI, commit with a clear message).

If anything here conflicts with `AGENT-RULES.md`, that file wins.
