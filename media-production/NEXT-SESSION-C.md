# MACHINE C — SESSION REFRESH / RESUME (written 2026-07-15 by the previous C session)

You are Machine C (hostname `cameron-lovett-MS-7C91`), rows **101–150**. A prior session on
this machine built a lot and hit context limits. This file is how you continue WITHOUT
relearning everything. Read it, then read FLOW-BUILD-PLAYBOOK.md, then go.

## WHAT'S ALREADY DONE (do NOT rebuild these)
Built + pushed this machine, all in the review queue (`site/review.html`):
**#101–#119** (18 story videos) **and the #121 "Salt and Light" v3 REDO.**
Every one: 10 painted 9:16 Flow stills at $0, narration, exact-KJV captions, closing
invitation card, ~2.5–3.5 min, <30 MB, QC'd (face/consistency, no halos, only-Jesus-in-cream,
no dead air, no baked-in text, care flags).

**Session of 2026-07-15 (fresh Flow project 026b29c0) added #117, #118, #119:**
- **#117 Hosea** — care D,L; redemption/price-paid, never the scandal; God as light.
- **#118 Jonah** — care J; mercy IS the story, Nineveh spared on screen + card; fish a
  reverent rescue not gore; storm=night.
- **#119 Fourth man in the fire (Dan 3)** — care R; NO burning flesh. LESSON: the divine
  "fourth" figure must be **FACELESS radiant light** — the model gave it a constructed
  bearded face on the first pass (caught in QC, regenerated s6/s7). Daniel 3 has NO
  God-speech, so it is **all-narrator, white captions** (KJV quotes are human speakers) —
  build.py uses `KJV=set()` + a separate `SILENCE={"n3","n6"}` for the two music hushes.
  Copy build-119's build.py as the template for any future no-God-speech story.

## RESUME POINT
Next job = lowest ⬜ row in my range = **#122 The mote and the beam (Matt 7)** (120 and 121 are
done). Then #123 onward. **Check media-production/CONTENT-CARE.md for each row's care flags
before storyboarding.** #122 is a Jesus-TEACHING story (Sermon on the Mount) — if a Jesus
figure appears, use the JESUS LOCK v3 + face-by-angle rules and pass the gate; if it is told as
a parable illustration with no Jesus in frame, keep God/Jesus out of frame like the parables.

**Working preference (Cameron, 2026-07-15):** run every command in the FOREGROUND, here and
now — never background jobs. See memory `foreground-only-commands`.

## THE PIPELINE IS FIXED AND PROVEN — how to build one video (≈20–40 min)
1. `git pull --rebase --autostash`. Claim the row in QUEUE.md (stamp `CLAIMED Machine C
   <date>`), commit, push BEFORE generating.
2. Write `build-NN-slug/PROMPTS.md` (copy a recent one, e.g. build-116). Master Style Block
   byte-identical. `python3 media-production/jesus_face_gate.py --dir <dir>` must exit 0.
   - Gate trigger words in SHOT BODIES: avoid "the LORD"/"jesus"/"christ" when God is shown
     as light (use "God"/"a divine presence" — "God" is NOT a trigger). Avoid the words
     "halo"/"rim-light" anywhere except inside the byte-identical JESUS LOCK v3 (the gate
     blanks the lock but flags those words elsewhere, even negated).
3. Generate stills: `cp build-102-jacobs-ladder/gen_stills_flow.py <dir>/` then
   `python3 gen_stills_flow.py`. Nano Banana 2, 9:16, $0. `Read` each jpeg to QC (never
   screenshot). Verify portrait (taller than wide), face consistent to master, only Jesus
   in cream, care flags, no baked text.
4. Narration: copy a make_narration.py, edit SEGMENTS. Two voices: narrator
   `en-US-AndrewNeural` (paraphrase), Jesus/God `en-US-ChristopherNeural` (EXACT KJV only,
   cream italic). Others' KJV (Peter, Abraham) = narrator voice, white caption.
5. build.py: copy from a recent build and remap S1..S10 filenames, KJV set, BEATS
   (stills MUST advance 1→10, never jump backward), the two silence anchors, and the OUT
   filename `book-chap_slug.mp4`. Then `python3 build.py`.
6. Publish: add the title to `media-production/gen_site_index.py` TITLES map, run
   `python3 gen_site_index.py` (it now writes **site/review.html**, NOT index.html), tick
   `Prep`+`Built` ✅ (NOT Appr) in QUEUE.md, `git add` the build files + QUEUE + gen_site_index
   + site/review.html, commit, pull --rebase, push.

## KEY LESSONS (the expensive ones — don't rediscover)
- **JESUS master face is LOCKED** at `media-production/JESUS-MASTER-REF/jesus-face.jpeg`
  (candidate 1). For Jesus shots, go **PROMPT-DRIVEN** with the byte-identical JESUS LOCK v3
  paragraph + a `REF: jesus-master-ref` marker line — do NOT attach it as `--ref`; a
  bust-portrait ref makes Nano Banana COPY the portrait instead of composing the scene. QC
  every Jesus face against the master; drift = regenerate.
- **God the Father / the LORD is shown ONLY as warm light — never a figure/face/hand.**
- **Some stills come back with a painted storybook BORDER.** Uniform fix (no regen): the
  build.py from build-104/116 prepends `crop=iw*0.88:ih*0.88` to build_still. Copy that
  build.py when a build's stills are bordered; use build-102's (no crop) when they aren't.
- **ffmpeg is NOT system-installed here** — it's `static-ffmpeg` (pip, `--break-system-packages`)
  symlinked into `~/.local/bin` (ffmpeg + ffprobe). Already set up; if missing, reinstall.
- **This ffmpeg renders a raw `\n` in a drawtext textfile as a tofu box (□).** The build.py
  in recent builds draws each wrapped caption/card LINE as its own drawtext layer — never a
  newline in a textfile. Copy those functions; don't revert to `\n`-join.
- **flow_driver.py fixes (all pushed):** submit = click box + real keystrokes + ENTER (not
  the Create button); 9:16 = open the chip with a REAL MOUSE click then click `crop_9_16`;
  `--ref` = set the hidden `<input type=file>` directly; heavy-project detection = 6-min
  window + reload the page every ~40s (newest image surfaces at the top).

## ⚠️ THE ONE THING TO FIX FOR SPEED: the Flow project is HEAVY (~150 images)
Every gen this session went into ONE Flow project, which now holds ~150 images. That makes
gens slow (the 6-min/reload path) and is what tripped a Google rate-limit at ~120 gens
(google.com/sorry CAPTCHA — see FLOW-RATE-LIMIT-ISSUE.md and GitHub issue #2; it cleared on
its own and was NOT account-wide — other machines kept working).
**STRONGLY recommended: start a FRESH Flow project at the start of this session** to keep
pages light and avoid re-tripping the limit. The New-project button on the Flow dashboard is
`add_2\nNew project`; click it with a REAL mouse and wait for the URL to become
`.../project/<id>`, then write that URL to `~/.mbm-flow-project`. If the browser lands on
`google.com/sorry`, that's the rate-limit — wait ~30–60 min, don't hammer it, or clear the
CAPTCHA by hand in the Chrome window. Cap this session to ~6–8 videos to stay under the limit.

## SESSION HYGIENE
Build a handful of videos, then hand off with a fresh chat (this file + the repo hold all
state). Announce each Chrome burst; if Cameron messages mid-burst, yield instantly. Never
touch the paid Gemini API — Flow only.
