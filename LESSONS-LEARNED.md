# MBM — Lessons Learned and Rules for Tonight

This file captures the operational lessons from the last session so we do not waste time repeating the same failures.

## What we learned
- The active app is the Expo app in `mobile/`.
- The repo root is not the Expo project root.
- `npx expo start` must be run from `mobile/`, or via the repo-root launcher scripts.
- `--lan` and `--tunnel` are unreliable in this environment for phone testing.
- The stable fallback path is the Expo web preview (`npm run mobile:web`).
- The phone path can fail even when the tunnel URL is reachable; the safest path is to use the verified local/web flow first.

## Non-negotiable rules
1. Never run Expo from the repo root with a raw `npx expo start` command.
2. Always use the repo-root scripts:
   - `npm run mobile:web` for the stable preview
   - `npm run mobile:dev` for the normal Expo run
3. If the port is busy, accept the new port prompt instead of fighting the old one.
4. Do not spend time on tunnel debugging until the local app is verified.
5. If the app fails to load on a phone, first verify the web preview works; then revisit tunnel setup.
6. Keep the canonical app in `mobile/` only.

## What to do tonight
1. Open the repo in the terminal.
2. Run `npm run mobile:web`.
3. Use the local preview URL in the browser to verify the app loads.
4. If the app looks correct, then try the phone path again only after the local path is confirmed.

## What to avoid
- Re-running raw `npx expo start` from the wrong working directory.
- Chasing tunnel/auth issues before verifying the basic app path.
- Creating duplicate app folders again.
