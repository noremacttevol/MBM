# Handoff prompt — push the improved MBM build + continue publishing

Copy everything inside the box below into a new chat. It tells that chat
everything it needs to ship the reviewed build and continue the store process.

---

You are picking up the MBM ("Milk Before Meat") project mid-publish. Work in the
folder `/home/noremacttevol/Desktop/Brain/MBM`. Before doing anything, read these
files in order so you have the full picture: `AGENT-RULES.md`, `CLAUDE.md`,
`STATUS.md`, and `PUBLISHING-ROADMAP.md` (especially "Stage 5.5 — June 25 review"
and "Next mission"). Do not re-ask me to explain the vision; it is all written down.

## What just happened (June 25, 2026)
The app passed a full all-sides review. These changes are DONE and committed
(git commits `fea4add` and `558f705` on branch `main`):
- All Christlikeness / virtue "soul-scoring" removed everywhere.
- The restored-gospel gate now reads the person's OWN WORDS only
  (`mayReferenceLds` / `restorationReady`).
- Every recorded signal is shown openly on the Profile with a "Forget" button.
- A "not officially affiliated with any Church" disclaimer is on the first screen,
  the Profile, and the privacy page.
- Restored scripture is never embedded; meat cards link to the official Gospel
  Library; only public-domain KJV is bundled inline.
- Typecheck is clean (`cd mobile && node_modules/.bin/tsc --noEmit`, exit 0) and a
  12-case gate stress-test passed 12/12.

These changes are JavaScript/TypeScript only — no native code changed.

## The mission (do these in order; confirm with me before any publish/submit action)

1. **Verify the working tree is clean and the changes are committed.**
   `cd /home/noremacttevol/Desktop/Brain/MBM && git log --oneline -3` should show
   `558f705` and `fea4add`. Run `cd mobile && node_modules/.bin/tsc --noEmit` and
   confirm exit 0 before shipping anything.

2. **Ship the update over-the-air (fastest path — no store review).**
   Because the changes are JS-only, an Expo OTA update lands on already-installed
   apps almost instantly. EAS CLI (v20+) is installed and already logged in as
   account `milkb4meat`. Channels are `preview` (internal testers) and `production`.
   - Recommend to me: push to `preview` FIRST, let me confirm it looks right, then
     `production`.
   - Command shape: `cd mobile && npx eas update --channel preview --message "June 25: remove scoring, own-words gate, open/removable signals, non-affiliation disclaimer"`
   - STOP and get my explicit "yes" before running it — this publishes to real
     users' phones. After it runs, report the update group/IDs and confirm success.

3. **Continue the store publishing using my already-open, already-trusted Chrome.**
   I have Chrome tabs open and signed in where my Apple Developer / App Store Connect
   (and Google Play Console) sessions are already authenticated and the browser is
   trusted. Use the Claude Chrome browser tools to do this:
   - First call `tabs_context_mcp` to list my open tabs and FIND the existing App
     Store Connect / Play Console tabs. Reuse those already-signed-in tabs — do not
     open a fresh login.
   - NEVER enter my password, 2FA code, or any credential, and never try to create
     or change account/security settings. If a page is logged out or asks me to
     authenticate, STOP and hand it back to me to sign in myself.
   - Read the current state of the TestFlight build (1.0.0) and the Play internal
     testing release, and tell me exactly what's left (e.g. Apple approval status,
     whether the Android `.aab` is actually rolled out).
   - Before clicking any irreversible control (Submit, Publish, Send to testers,
     Confirm), describe exactly what it will do and get my explicit "yes" first.

4. **If a fresh native build is ever needed** (only if native deps change), bump the
   version/build number in `mobile/app.json` and use `eas build` then `eas submit`.
   For these June 25 changes you should NOT need this — prefer the OTA update.

5. **Security clean-up before any WIDE sharing** (still open from Stage 5): the admin
   desk password is the placeholder "JosephSmith" — I need to change it to something
   strong myself, and the API keys shown in setup logs (Firebase, Anthropic, Railway)
   should be rotated. Remind me; walk me through it; do not do the account steps for me.

## Key facts you'll need
- App name: "Milk Before Meat" (shows as "Milk B4 Meat"). Version 1.0.0.
- iOS bundle: `org.milkb4meat.app`. Android package: `com.milk_before_meat`.
- TestFlight public link: https://testflight.apple.com/join/cPNpeh3H
- Website: milkb4meat.org (+ /privacy.html, /support.html). Proxy: Railway `mbm-proxy`.
- Feedback/contact email already set in TestFlight: noremacprojects@gmail.com.
- EAS account: `milkb4meat` (admin@milkb4meat.org), already logged in.

## Guardrails (do not skip)
- The mission is to make the REVIEWED, improved version the live one — being upfront
  is the point; nothing about this needs to be hidden.
- Do NOT commit the loose binaries or sensitive files in the repo root (`*.apk`,
  `*.aab`, `*.pem`, `*.backup.gz`) — they should not go into git. Suggest adding
  them to `.gitignore`.
- Get my explicit approval before: pushing any `eas update`, clicking Submit/Publish/
  Send-to-testers in the stores, or anything irreversible.
- Never enter my passwords/credentials or change account or security settings — hand
  those back to me.
- Trademark/Church note: the app is correctly branded as MY independent app, not the
  Church's. Keep it that way — never put "LDS"/"Mormon"/"Book of Mormon"/the Church
  logo in the app title, icon, or store listing, and never imply it's official.

Start by reading the four files above, then report back the current git + typecheck
state and your proposed first step. Then wait for my go-ahead.
