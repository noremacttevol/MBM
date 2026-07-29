# V2-NEXT-SESSION-PROMPT — the paste-and-go for every V2 production session

> **Cameron: open a new Claude Code session on this repo, set the model to
> OPUS 5, and paste exactly this line:**
>
> ```
> Read V2-NEXT-SESSION-PROMPT.md and execute it. Start now.
> ```
>
> That is the whole ritual. Every new session resumes exactly where the last one
> stopped. (Why Opus: the two places quality is actually made — planning the beat
> map from the scripture, and judging every picture at full resolution — are
> judgment work. The generation itself is scripted and costs the model nothing.)

---

## To the session reading this: you are a V2 production worker. Do this, in order.

### 0. Orient (5 minutes, no browser)

1. `hostname` → look yourself up in `MACHINE-IDENTITY.md`.
2. Read the TOP entry of `SESSION-LOG.md`; verify its commit is in `git log`.
3. Read **`V2-KICKOFF.md`** (the job spec) and **`media-production-v2/PRODUCTION-LEDGER.md`**
   (the state). You resume at the FIRST row that is not DONE, finishing any
   IN-PROGRESS row from its last completed step. If Cameron assigned this machine a
   range in his message, work ONLY that range, in order.
4. Proof this works: row 1 (`build-01-cloak`) is DONE and **approved by Cameron** —
   its build folder is the reference implementation for everything below. Row 2
   (`build-02-prodigal`) shows the multi-character/staged-wardrobe pattern.

### 1. The standing decisions (do not re-litigate these)

- **Pictures come from FLOW on Cameron's subscription — at 2K (Cameron's order,
  2026-07-28: "I need the same quality from Flow").** Discovered the same night:
  Flow's image viewer has a Download menu with **1K (original) / 2K (upscaled,
  1536×2752) / 4K (3072×5504)** — the old driver always fetched the 1K gallery
  copy. `flow_driver.py gen` now downloads **2K by default** (`--size`), which
  matches the API's 2K pixel-for-pixel in size. Generate with:
  `python3 media-production-v2/v2_prompt.py <build-dir> --gen`
  (it drives Flow with `--model "Nano Banana Pro" --size 2K`). Flow limits that
  remain: ~20 pictures/hour, one at a time, Chrome runs on the machine — announce
  each burst, stop instantly if Cameron messages.
- 🛑 **FLOW ONLY. THE PAID API IS BANNED (Cameron, 2026-07-29).** His words:
  *"i told you to stop with the api key. use flow only why can you listen."* He had
  said it once already; a session ran `v2_gen_api.py` anyway, burned his prepaid
  credits and hit `RESOURCE_EXHAUSTED` mid-row. **`v2_gen_api.py` is RETIRED and now
  refuses to run.** There is no budget exception, no speed exception, no "the API is
  faster" exception, and no "Flow is throttling" exception. If Flow is slow, you wait.
  Every picture comes from Flow on Cameron's subscription, via
  `python3 media-production-v2/v2_prompt.py <build-dir> --gen`. Do not add a new API
  path, do not un-retire the old one, do not ask him to refill credits.
- **The Jesus face is LOCKED and APPROVED**: `media-production-v2/JESUS-V2-REF/jesus-v2-face.jpeg`.
  Never regenerate or "improve" it. Every Jesus shot = byte-identical JESUS LOCK v4
  (assembled by code) + that ref attached.
- **V1 is read-only.** You read audio/timing/scripts from `media-production/build-*`;
  you write only inside `media-production-v2/`.
- **Audio is preserved, never trimmed.** The V2 cut derives every duration from the
  audio at build time, so it can never come out shorter than the narration. If a
  story FEELS compressed when you listen/read it (the ElevenLabs re-voice is faster
  than the old voice), do NOT fix it yourself — note "story feels compressed" in the
  ledger row so the re-voice track picks it up. 99 builds still carry the OLD Jesus
  voice (list: `media-production/REVOICE-WORKLIST.md`); if your row is on it, note
  "audio pre-Alexander — re-render after revoice" and build anyway. The word-anchored
  markers make the re-render automatic later.

### 2. Per-row loop (A–I, from V2-KICKOFF, with the lessons already paid for)

**A.** Open the ledger row (start timestamp, machine).

**B.** `python3 media-production-v2/extract_beats.py <row> --json media-production-v2/build-NN-slug/beats.json`
— it parses the V1 build without executing it and prints every segment's audio
window. Copy (never move) the V1 `audio/` into the V2 build folder, plus
`make_narration.py`, `mbm_caption_timing.py`, `mbm_speakers.py`, `mbm_pronounce.py`.

**C.** Write `beats_v2.py` (copy the shape from build-01/build-02):
- **Coverage law (Cameron, 2026-07-28): aim ~15 pictures per story, range 10–20,**
  scaled by runtime — a 100-second story sits near 15; a 2.5-minute story may run
  above 20 only when the narration genuinely demands it. The narration decides,
  never a quota.
- **Burst sequences get burst coverage.** Cameron's example is John 21: not
  knowing it's Jesus → being told → realizing → leaping out of the boat → swimming.
  Each micro-beat is its OWN frame, switched mid-segment with word-anchored
  markers (`marker_time`). Any fast action chain works this way.
- Study the KJV passage first; write the scripture facts into the file header and
  let them govern direction, position, scale, time of day.
- Check `media-production/CONTENT-CARE.md` §3 for the row's flags FIRST.
- Locks: byte-identical per character per video, assembled by `v2_prompt.py` —
  local LOCKS for this video's people, CAST_LOCKS for recurring cast.
  **A setting lock must never name a character** (naming one puts him in the
  frame — proven by the STRAY-JESUS defect). **A lock must never contradict a
  beat's scene text** (the model obeys the lock; the contradiction is still a bug).
  If the story changes someone's clothing (prodigal son), lock face/build only and
  state clothing per beat.

**D.** `python3 media-production-v2/v2_prompt.py media-production-v2/build-NN-slug --check --dump`
must PASS. If it flags a word like "glow" that you meant innocently (lamplight),
REWORD the scene — never weaken the checker.

**E.** `nohup python3 media-production-v2/v2_gen_api.py media-production-v2/build-NN-slug > /tmp/rNNN-api.log 2>&1 &`
— runs unattended, ~1 min/picture, logs every save and the dollar figure.

**F.** **QC every single picture by Reading the jpeg at full resolution** — Cameron's
explicit requirement: "something has checked all of the pictures." Judge against the
V2 rubric in V2-KICKOFF step F (hard fails + 1–5 scores). Regenerate fails with
`--only bNN --redo` and a prompt fix; log the defect code in the ledger. Three
failed rerolls on one beat → best available wins, note it, move on.

**G.** Write the build's `build.py` from the build-01/build-02 template: THIS
build's LEAD/GAP/KJV_GAP/TAIL and CARD id (extract_beats prints them), BEATS with
marker words, verify every marker resolves (`python3 -c` loop — see row-2 pattern)
BEFORE rendering. Run it. Then: `bash admin/verify-mp4.sh <out>.mp4` must print OK;
ffmpeg silencedetect ≥2.5 s must find nothing; extract 3–4 frames and Read them
(captions on the right scenes, right colours, bottom band).

**H.** Write `MINISTRY-GATE.md` — the four §5 answers, honestly, as the target
viewer.

**I.** Close the ledger row (end time, gens, accepted, rerolls by defect code,
dollars, mp4 size/duration). `git add` ONLY text files (never jpeg/mp3/mp4 —
the `.gitignore` enforces it). Commit. ONE `git push` attempt with a 2-minute
timeout; if it fails, write "push skipped" and keep working.

**J.** Next row. Do not wait, do not ask. One-line progress note to Cameron
between videos.

### 3. Session hygiene

- The repo is the memory; the ledger is the state. Never rely on chat scrollback.
- When context gets tight: FINISH the current row through step I, update the
  ledger, print exactly: `SESSION FULL — open a new session and say: Read
  V2-NEXT-SESSION-PROMPT.md and execute it. Start now.` Then stop.
- Any message from Cameron interrupts everything instantly.
- Deliver each finished video to Cameron with SendUserFile the moment it passes
  the gates — he approves per video.

### 4. Known blocker (tell Cameron if it bites)

Machine A (`Dev`) cannot `git push` (12.7 GB pre-existing backlog; pushes reject).
Its V2 work is committed locally and safe, but **other machines cannot see
`media-production-v2/` until that repair happens**. Multi-machine V2 production
needs either that repair or all sessions running on Machine A.
