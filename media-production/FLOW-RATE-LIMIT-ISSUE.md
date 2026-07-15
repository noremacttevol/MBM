# ISSUE: Google Flow rate-limits the automated session after heavy use (2026-07-15, Machine C)

## What happened
Machine C built and published **12 videos in one continuous session** (#101–111 + the
#121 v3 redo). Partway through video **#112 (The Beatitudes)** — after roughly **120 image
generations** on the same Flow project / same machine — Google began serving its anti-bot
interstitial to the automated Chrome:

```
https://www.google.com/sorry/index?continue=https://labs.google/fx/tools/flow&q=...
```

That is Google's **"unusual traffic" / CAPTCHA rate-limit page**. Once it appears:
- `flow_driver.py gen` fails with **"prompt focus failed: no visible prompt box"** and
  **`aspect_9_16=False`** (the real Flow UI never loads — the /sorry page has no prompt box).
- `flow_driver.py check` reports **`logged_in=False project=saved`** (it can't find the
  dashboard because Google is showing the CAPTCHA instead).

It is **not** a prompt bug, a login bug, or a driver bug — the driver is working; Google is
deliberately throttling the automated browser.

## Current state (safe — nothing lost)
- #101–111 and #121: **built, QC'd, pushed, live on the gallery.**
- **#112 The Beatitudes: 8/10 stills done** (missing **s8-the-peacemakers** and
  **s10-the-upside-down-kingdom**). PROMPTS.md (gate-PASS), make_narration.py (audio done),
  and build.py are all committed. It needs only those 2 stills, then `build.py` +
  `gen_site_index.py` + push.
- The block persisted through re-checks at +5 min and +25 min (still `logged_in=False`).

## Why it happened
- **Volume + velocity on one IP/profile/account:** ~120 automated generations back-to-back
  in a single session is exactly the pattern Google's abuse systems flag.
- **Heavy project page:** every generation this session went into the SAME Flow project, so
  that project accumulated 120+ images. A very heavy project page also makes the prompt UI
  slow/flaky to load, which compounds the problem (this is what first looked like the
  "stuck session" in the playbook, before the /sorry page confirmed a hard block).

## Options — what we could do next
1. **Clear the CAPTCHA once, by hand (fastest).** Open the Chrome window on Machine C
   (the flow_driver profile `~/.mbm-flow-profile`), let the /sorry page load, solve the
   one CAPTCHA. The block usually lifts immediately and generation resumes.
2. **Wait it out.** These limits reset on their own — often 30–60 min, sometimes a few
   hours. Don't hammer it with repeated checks (that can extend the timer). One check every
   ~40 min is plenty.
3. **Throttle the factory cadence (prevent recurrence).** Cap generations per session/machine
   (e.g. ~6–8 videos ≈ 60–80 images) and add small random delays between gens so the pattern
   looks less bot-like. The "one video per chat" hygiene rule already points this way; this
   session deliberately ran 12+ to fill the gallery fast and tripped the limit.
4. **Fresh Flow project per video (or every few videos).** Keeps each project page light and
   avoids the 120-images-in-one-project slowdown. flow_driver would clear `~/.mbm-flow-project`
   and create a new project via the New-project button. (Attempted mid-block and it also hit
   the /sorry page, so this only helps once the block is clear.)
5. **Spread the load across the 4 machines/accounts** so no single IP/account does 120 gens
   in a row.

## Recommendation
- **Right now:** solve the CAPTCHA by hand in the Chrome window (option 1) OR wait ~40–60 min
  (option 2). Then finish #112's two stills and continue #113→#150.
- **Going forward:** adopt option 3 (cap ~6–8 videos per machine per session) and option 4
  (fresh project every few videos) so this doesn't recur. Do NOT attempt to bypass the
  CAPTCHA programmatically — that risks the account.

## Repro / verify
```
python3 media-production/flow_driver.py check
# blocked  -> logged_in=False project=saved  (and the browser URL is google.com/sorry/...)
# cleared  -> logged_in=True  project=saved   (safe to resume)
```
Resume point after it clears: `cd media-production/build-112-beatitudes && python3
gen_stills_flow.py` (it skips the 8 already on disk, generates s8+s10), then `python3
build.py`, add title to `gen_site_index.py`, rerun it, commit + push.
