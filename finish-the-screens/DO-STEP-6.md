# DO-STEP-6 — finish the SCREENS (the visible half of the port)

## Context (read first)

The engine port (Steps 1–5 and 7 of `port-back/INSTALL.md`) is already done and
verified in this repo: the chat ear, signal harvesting, faithWords, exercises,
two-witnesses gate, and member-self-ID laws are all live in
`mobile/src/store/useAppStore.ts` and `mobile/src/engine/`. **Step 6 — the
screens — was skipped**, because the prototype file it depends on was missing
from the bundle. That is why the installed APK looks identical to the old app.

This folder contains the missing reference: **`MBM App.dc.html`** — the proven
prototype. It is a single HTML file: the screen markup (with inline styles) is
in the `<x-dc>` template at the top; the behavior is in the `class Component`
logic below it. Port screen copy, layout, palette, and behavior from it
**verbatim**. Where this doc and `port-back/PORT-BACK.md` §5 disagree with the
prototype, **the prototype wins** (it reflects the owner's latest amendments).

Do everything yourself. Do not stop after the engine — the deliverable is
screens that visibly match the prototype, then a clean typecheck, then the
acceptance greps below, then tell the owner to run the build command.

---

## 0. Palette + type (`mobile/src/theme.ts`)

Align the theme to the prototype's palette so every screen looks like last
night's design. From the prototype: background `#0a0a0f`, card `#111116`,
hairline/border `#2a2820`, parchment text `#f0e6c8`, body `#e8e4d8`, muted
`#9a9080`, faint label `#5a5240`, accent gold `#d4c89a` (on-accent text
`#15110a`). Serif/contemplative feel, generous line-height, small tracked-out
uppercase labels — copy sizes from the prototype's inline styles.

## 1. `FeedScreen.tsx`

- DELETE the "← Keep it simple" and "Take me deeper →" buttons and their
  `keepSimple`/`goDeeper` wiring. Replace with ONE full-width quiet button:
  **"Show me more →"** → store's same-track `refreshFeed` (it exists in the
  store; if the action is still named `goDeeper`/`keepSimple`, rename to
  `refreshFeed` and make it rebuild within the current track only — copy the
  prototype's `onMoreFeed` comment block, ~line 857).
- ADD `FollowUpCard` (renders at the TOP of the feed when an exercise
  follow-up is due) and `InvitationCard` (below content). The store already has
  `activeExercise`, accept/report actions, and `doneExerciseIds` — wire to
  those. Copy card copy + the optional "say what you noticed" reflection field
  (harvested) from the prototype.
- `ContentCard`: add **"Reflect on this →"** (saves to journal + harvests) and
  **"Talk about it →"** (opens Chat with a prefilled draft).

## 2. `OnboardScreen.tsx`

- Optional first-name input on the reflection step ("A first name is plenty —
  or skip it").
- ADD the **FAITH BACKGROUND page** as the final onboarding step — copy the
  prototype's `phaseFaith` block (template ~line 96 + logic `faithOptions` /
  `enterApp`): "Where does faith live for you — today, or in your past?",
  five options + open free-text field. It seeds routing signals, stores the
  person's words verbatim into `faithWords`, and marks question id 2.5
  answered. Names no church (Law 9).

## 3. `ProfileScreen.tsx`

- DELETE "CURRENT PATHWAY" and any "N signals active" line (Law 4: routing
  state is owner-only forever).
- KEEP the trait bars — but as the prototype's **"WHAT'S GROWING IN YOU"**
  section (owner amendment: virtues belong to the person), with its exact
  framing copy ("These are yours — they grow as you engage honestly. There is
  no score to beat.").
- ADD **"YOUR FAITH, AS YOU'VE TOLD IT"** — `faithWords` verbatim, newest
  first.
- ADD **"YOUR STORY SO FAR"** — titled moments, newest first, each with
  "Ask about this →" opening Chat with a prefilled draft.

## 4. New `WelcomeBackScreen.tsx` + route

On launch with persisted main-state: "Welcome back{, Name}." + recall of their
last journal line + "Pick up where you left off →". No cold restarts. Copy the
prototype's WelcomeBack block (template ~line 115, logic `welcomeName` /
`welcomeRecall` / `onPickUp`). Register it in `AppNavigator.tsx`.

## 5. `ChatScreen.tsx`

"Talk to a real person" must open the in-app connect capture (not mailto).
Verify; fix if needed.

## 6. Blessing toasts

After dialogue answers, hearts, journal saves, exercise accept/report — words
only, copy the line pools from the prototype. Journal's "Written." state gets a
blessing line.

---

## Acceptance — ALL must pass before you report done

```bash
cd mobile
# 1. old buttons gone, new one present
! grep -rn "Take me deeper\|Keep it simple" src/screens
grep -rn "Show me more" src/screens
# 2. new screen exists and is routed
test -f src/screens/WelcomeBackScreen.tsx && grep -n "WelcomeBack" src/navigation/AppNavigator.tsx
# 3. onboarding asks about faith openly, names no church
grep -n "Where does faith live" src/screens/OnboardScreen.tsx
! grep -rni "latter-day\|churchofjesuschrist" src/screens/OnboardScreen.tsx
# 4. profile sections
grep -n "WHAT'S GROWING IN YOU" src/screens/ProfileScreen.tsx
grep -n "YOUR FAITH" src/screens/ProfileScreen.tsx
grep -n "YOUR STORY SO FAR" src/screens/ProfileScreen.tsx
! grep -n "CURRENT PATHWAY\|signals active" src/screens/ProfileScreen.tsx
# 5. clean typecheck
npx tsc --noEmit
```

Do NOT change `mobile/.env`, the API key, or the chat transport — the owner
has decided the app calls Anthropic directly. Leave the store's engine logic
alone except where a screen needs a new action.

When everything passes, commit, then tell the owner to run:

```bash
cd ~/Desktop/Brain/MBM/mobile
npx eas-cli build -p android --profile preview
```

and to install the APK from the link EAS prints (open it on the phone).
