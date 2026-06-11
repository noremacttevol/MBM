# MBM — Status

_Last updated: 2026-06-11_

MBM (Milk Before Meat) is a mobile-first gospel-outreach app patterned after how
Jesus ministered: meet people where they are, learn them through their own words,
and route them silently — never with visible gates — always obeying the
milk-before-meat law.

## What runs today

**Mobile app** (`mobile/`) — React Native + Expo, local-first, on-device state.

- Onboarding (story → question → reflection), feed, journal, chat, and profile.
- A single Zustand store (`mobile/src/store/useAppStore.ts`) persisted to
  AsyncStorage. It holds the person's signals, traits, feed track, journal, chat,
  faith words, story moments, name, and active spiritual exercise.
- Invisible emergent routing: feed tags MILK / BRIDGE / RESTORATION / MAINTENANCE
  are chosen from signals, never shown, and re-derived after every interaction.
- No time cap, no come-back wipe. The app never locks a person out and never
  erases what it has learned (Law 5).

**The engine** (`mobile/src/engine/`)

- `connect.ts` — the laws: two-witnesses god-good gate, Reformed/Calvinist
  framework blocking, member status only from explicit self-ID, the milk gate
  (`mayReferenceLds`), journey assessment, human/missionary handoff.
- `chatEar.ts` — the ear: `harvestSignals` (per-sentence, negation-guarded),
  the model-side signal-report protocol (`SIGNAL_REPORT_INSTRUCTION` +
  `stripSignalReport`), and `FAITH_ID_RE`.
- `exercises.ts` — spiritual exercises (invite → try → report → learn).
- `minister.ts` — the production minister system prompt.
- `data/questionBank.ts` — targeted dialogue routing (background → picture of God
  → God still speaks → the reach).

**The key proxy** (`server/`) — Express. Holds the Anthropic key server-side so
it never ships in the app. Endpoints: `POST /api/chat`, `POST /api/connect`,
`POST /api/factcheck`, `GET /api/admin/queue` (token-protected), `GET /health`.
Connect requests land in the owner inbox — "a human one tap away" is delivered,
not just captured.

## Verification

- `mobile/`: `npx tsc --noEmit` → 0 errors.
- Engine acceptance tests (INSTALL Step 9 items 1–4): 19/19 checks passing
  (MILK routing + first question; closed gate on "God doesn't still speak";
  Reformed rejection + affirmation both heard; LDS self-ID unlocks member track).

## What still needs an account (owner-only)

1. **Deploy the proxy** (`server/`) to Railway/Render/Fly and set env vars
   `ANTHROPIC_API_KEY` and `ADMIN_TOKEN`. Then set
   `EXPO_PUBLIC_SERVER_URL` in `mobile/.env` to the deployed URL.
2. **Build the APK** with EAS cloud build (`npx eas-cli login` then
   `npx eas-cli build -p android --profile preview`).

## Layout

- `mobile/` — the app (this is where all new work happens).
- `server/` — the key proxy + owner inbox.
- `port-back/` — the verified reference bundle (INSTALL, laws, sim report, data).
- `ministry-sim/` — the 102-persona ministry simulation harness.
- `content/`, `outputs/` — content corpus and generated artifacts.
- `archive/docs/` — historical prompts, session notes, and design docs.
- `CLAUDE.md`, `.claudecode.md` — the operating manual and system guardrails.
