# MBM — Status

_Last updated: 2026-06-24_

> The master manual is [`AGENT-RULES.md`](./AGENT-RULES.md) — read it first. This file
> is just the current build state.

> **Latest changes (2026-06-24):** (1) All virtue/Christlikeness scoring removed — no
> more "seven spirit levels," `traitScores`, or `christlikeCap`. (2) The restored-gospel
> gate now reads the person's **own words only** (`mayReferenceLds` / `restorationReady`).
> (3) Every recorded signal is shown openly on the Profile and can be edited or removed
> (`forgetSignal`, "What the app has noticed" card). (4) A standing "not officially
> affiliated with any church" disclaimer appears on the first screen and the Profile.
> (5) Restored scripture is never embedded — meat cards link to the official Gospel
> Library; only public-domain KJV is bundled inline.

MBM (Milk Before Meat) is a mobile-first gospel-outreach app patterned after how
Jesus ministered: meet people where they are, learn them through their own words,
and route them silently — never with visible gates — always obeying the
milk-before-meat law.

## What runs today

**Mobile app** (`mobile/`) — React Native + Expo, local-first, on-device state.

- Onboarding (story → question → reflection), feed, journal, chat, and profile.
- A single Zustand store (`mobile/src/store/useAppStore.ts`) persisted to
  AsyncStorage. It holds the person's signals, feed track, journal, chat,
  faith words, story moments, name, and active spiritual exercise. No virtue/trait
  scores — retired 2026-06-24. Every signal is visible and removable on the Profile.
- Invisible emergent routing: feed tags MILK / BRIDGE / RESTORATION / MAINTENANCE
  are chosen from signals, never shown, and re-derived after every interaction. The
  restored-gospel gate reads the person's own words only (`mayReferenceLds`).
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

**Anthropic transport (local-first)** — Per CLAUDE.md the app is local-first and
runs with no server terminal. The store calls Anthropic directly using
`EXPO_PUBLIC_ANTHROPIC_API_KEY` from `mobile/.env` (gitignored, never committed).
Connect requests are captured on-device and reviewed by Cameron in admin
(Phase 1). The `server/` proxy is kept in the repo as an optional Phase-2 path
but is not used by the shipping app.

## Verification

- `mobile/`: `npx tsc --noEmit` → 0 errors.
- Engine acceptance tests (INSTALL Step 9 items 1–4): 19/19 checks passing
  (MILK routing + first question; closed gate on "God doesn't still speak";
  Reformed rejection + affirmation both heard; LDS self-ID unlocks member track).

## What still needs an account (owner-only)

1. **Build the APK** with EAS cloud build. Run these from inside the mobile
   folder (this is where the earlier build failed — it was run from `~`):

   ```
   cd ~/Desktop/Brain/MBM/mobile
   npx eas-cli login
   npx eas-cli build -p android --profile preview
   ```

## Layout

- `mobile/` — the app (this is where all new work happens).
- `server/` — the key proxy + owner inbox.
- `port-back/` — the verified reference bundle (INSTALL, laws, sim report, data).
- `ministry-sim/` — the 102-persona ministry simulation harness.
- `content/`, `outputs/` — content corpus and generated artifacts.
- `archive/docs/` — historical prompts, session notes, and design docs.
- `CLAUDE.md`, `.claudecode.md` — the operating manual and system guardrails.
