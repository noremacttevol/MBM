# MISTAKES MADE + HOW TO USE FAR FEWER CREDITS (Machine C, 2026-07-15)

Cameron asked me to write down the mistakes I made and how to stop burning Claude/cloud
usage. This session built 16 videos in ONE chat — great output, but expensive. Here is the
honest post-mortem and the plan to do the same work for a fraction of the usage.

## THE BIG PICTURE: what actually eats "credits" (Claude usage, not Flow)
Flow image generation is $0 (Ultra plan). The usage Cameron is paying for is **Claude
context/token usage**, and the two biggest drivers this session were:
1. **Running 16 videos in one ever-growing context.** Every new video carried the full
   weight of all previous ones. Token cost per video climbs the longer the chat runs. The
   "one video per chat" rule exists exactly for this — I ignored it 16x.
2. **Reading a LOT of images for QC.** Every `Read` of a still or a video frame is a large
   multimodal cost. I read ~5+ images per video (often more when rerolling). That is the
   single most expensive repeated action.

### The fix (do these and usage drops massively)
- **One video per chat.** Fresh context each time. Biggest single lever.
- **QC by sampling, not exhaustively.** Read at most 2 images per video: one Jesus/character
  frame (consistency + only-Jesus-cream + no-halo) and one final caption frame (KJV exact +
  no tofu). Trust the pipeline for the rest. Do NOT read all 10 stills.
- **Don't re-read images you already reasoned about.** I sometimes re-extracted/re-read
  frames. Extract once, read once.
- **Fewer status/poll cycles.** Waiting loops that re-enter context cost tokens. Kick off a
  build, do one wait, check once.

## MISTAKES I MADE (and the cheap way to avoid each)
1. **Didn't check claims before generating.** I started making master-face candidates before
   pulling — Machine A had already claimed the bootstrap. Wasted gens + churn. → Always
   `git pull` and read the claim/QUEUE first.
2. **Broke a working fix during a merge, then ran a whole batch on it.** My flow_driver
   conflict resolution silently broke the 9:16 chip-finder; a 10-still batch failed on
   aspect before I noticed. → After resolving a conflict in a working file, run the small
   isolated test ONCE before a full batch.
3. **Generated real assets before verifying settings.** Made a 16:9 still, then had to redo
   it after fixing 9:16. → Verify settings in isolation first; then generate.
4. **Attached the bust portrait as `--ref` for scene shots.** Nano Banana COPIED the
   portrait (two #121 shots came back as portrait clones), wasting gens + a rebuild. → Jesus
   scene shots are PROMPT-DRIVEN (JESUS LOCK v3), never `--ref`.
5. **Killed a running gen and relaunched immediately → Chrome profile lock.** 9 stills failed
   "Opening in existing browser session." → After killing gen: `pkill -9 -f mbm-flow-profile`,
   `rm -f ~/.mbm-flow-profile/Singleton*`, wait, THEN relaunch.
6. **Beat-mapping slips.** Several times a still was left unused or the still order jumped
   backward, needing re-edits. → Before building, assert all 10 stills map in ascending
   order 1→10.
7. **Wardrobe drift not caught until a frame read.** #103 had a disciple in cream, #111 had
   Jesus in a brown mantle. One reroll. → Put "only the central figure in cream; everyone
   else in saturated dark earth colours" in every crowd prompt.
8. **Storybook border discovered late (#104).** Some stills have a painted vignette border.
   → Known now: use the build.py with `crop=iw*0.88` when stills are bordered.
9. **THE COSTLY ONE — ran ~160 gens into a SINGLE Flow project.** The project got heavy,
   detection went slow (6-min windows + page reloads = lots of wall-clock and my
   polling/token cost), and it tripped a Google rate-limit at ~120 gens (google.com/sorry).
   → Start a FRESH Flow project every few videos; cap ~6–8 videos per machine per session.

## A LEANER PER-VIDEO RECIPE (same quality, far less usage)
1. Fresh chat. `git pull`. Read `NEXT-SESSION-C.md` (not the whole history).
2. Claim row, push. Write PROMPTS from a template. Pass the gate.
3. `gen_stills_flow.py` (fresh project). Do NOT read all 10 stills — glance only if a
   sensitive care-flag story.
4. Narration + build.py from templates.
5. Build. Read exactly TWO frames: one character frame + one caption frame. If both pass,
   ship.
6. Publish, push. Hand off / end the chat.

Estimated effect: one-video-per-chat + 2-image QC + fresh project should cut per-video
Claude usage by a large margin versus this session, and remove the rate-limit risk entirely.

## WHAT WENT RIGHT (keep doing)
The pipeline itself is now solid and worth the investment: flow_driver is fixed (submit,
9:16, ref, heavy-project detection), captions are tofu-free, ffmpeg is installed, care flags
were handled well (Sodom/Isaac destruction & knife kept off-screen), and 16 videos + the
#121 redo shipped clean. The fixes are permanent and benefit all four machines.
