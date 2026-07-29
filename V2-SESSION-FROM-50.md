# V2-SESSION-FROM-50 — paste-and-go for a session starting at video #50

> **Cameron: open a new Claude Code session on this repo, set the model to OPUS 5,
> and paste exactly this line:**
>
> ```
> Read V2-SESSION-FROM-50.md and execute it. Start at row 50. Do not stop.
> ```
>
> That machine then owns rows 50 and up and works the same way rows 1–3 were built.
> Another machine can be pointed at a different starting row with its own copy of
> this file — the QUEUE/ledger claim is what keeps them off each other.

---

## You are a V2 production worker. Start at row 50 and keep going.

### 0. Orient (terminal only, no browser)

1. `hostname` → look yourself up in `MACHINE-IDENTITY.md`.
2. Read the TOP entry of `SESSION-LOG.md`; confirm its commit is in `git log`.
3. Read `V2-KICKOFF.md` (job spec) and `media-production-v2/PRODUCTION-LEDGER.md`
   (state). **Work rows 50 upward, in order.** If row 50 is already DONE, take the
   lowest not-DONE row at or above 50. Never touch a row another machine has claimed.
4. `media-production-v2/build-02-prodigal/` is your reference implementation —
   `beats_v2.py`, `build.py`, `MINISTRY-GATE.md`. Copy its shapes.

### 1. THE HARD LAWS — do not re-litigate, do not "improve" on these

- 🛑 **FLOW ONLY. THE PAID API IS BANNED (Cameron, 2026-07-29):** *"i told you to stop
  with the api key. use flow only why can you listen."* `v2_gen_api.py` is retired and
  refuses to run. No budget, speed or throttling exception — if Flow is slow, you
  wait. Never ask him to refill credits. Every picture:
  `python3 media-production-v2/v2_prompt.py <build-dir> --gen` (Nano Banana Pro, 2K).
- **The Jesus face is LOCKED and APPROVED:** `media-production-v2/JESUS-V2-REF/jesus-v2-face.jpeg`.
  Never regenerate or "improve" it. Every Jesus shot gets byte-identical JESUS LOCK v4
  (the assembler adds it) plus that ref.
- **V1 is read-only.** You READ audio/timing/scripts from `media-production/build-*`;
  you WRITE only inside `media-production-v2/`.
- **Audio is preserved, never trimmed or re-timed.**
- **Never ask permission you already have.** Cameron said go. Build the whole video
  and show him the finished thing. Any message from him stops the browser instantly.
- **Announce every Chrome burst** in the message right before it starts, then start
  immediately.

### 2. Per-row loop

**A.** Open the ledger row (start timestamp, machine).

**B.** `python3 media-production-v2/extract_beats.py <row> --json media-production-v2/build-NN-slug/beats.json`
Copy (never move) the V1 `audio/` into the V2 build folder, plus `make_narration.py`,
`mbm_caption_timing.py`, `mbm_speakers.py`, `mbm_pronounce.py`.

**C.** Write `beats_v2.py` (copy build-02's shape). Read the KJV passage in full first
and put the governing scripture facts in the file header. Check
`media-production/CONTENT-CARE.md` §3 for this row's flags FIRST.

Coverage: **aim ~15 pictures, range 10–20**, scaled by runtime; the narration decides,
never a quota. Burst sequences get burst coverage via word-anchored `marker_time`.

**These four rules were each paid for with rejected frames. Apply them while WRITING
the beats, not at QC:**

1. **STATE THE CAMERA, not just the action.** Any beat where someone travels, watches,
   or arrives must say where the lens is and which way the figure faces —
   *"SHOT FROM BEHIND THE FATHER, his back to the camera, running AWAY from us down
   the road; far ahead of him, small with distance and IN THE DIRECTION HE IS RUNNING,
   his son."* Without this the model defaults to hero-shots facing the lens, and row 2
   shipped a first pass where **the father ran away from his son** in the icon shot of
   the parable, and "Then he left" read as the son arriving.
2. **A NEGATION IS A SUGGESTION; A STATED POSITIVE IS AN INSTRUCTION.** "never cream"
   gets you cream. Say the colour and anchor it to something in frame: *"the same
   saturated dark wool as their robes, plainly DARKER than the sunlit wall behind
   them."* Same for style: "not plastic CGI" drifts to CGI; *"real weathered skin,
   real coarse wool, photographed on location with a real camera"* holds. This has now
   bitten three times.
3. **LOCK RECURRING FACES BY IMAGE.** Text locks do NOT hold a face — row 2's elder
   son came back as three different men. As soon as one still of a character is
   ACCEPTED, copy it to `<build>/CAST-REF-V2/<name>-ref.jpeg` and put
   `"char_refs": ["CAST-REF-V2/<name>-ref.jpeg"]` on every later beat that character
   appears in, wherever their face is legible. Two char_refs per shot maximum.
4. **A LOCK MUST NEVER NAME A CHARACTER OR CONTRADICT A BEAT.** Naming someone in a
   setting lock paints him into frames he does not belong in (the STRAY-JESUS defect).
   If the story changes someone's clothing, lock face/build only and **state the
   clothing in every single beat** — the beats that forget are exactly the ones that
   drift. Track props the story gives later (row 2: the son stays BAREFOOT until the
   shoes are given in v22, or the gift means nothing).

**D.** `python3 media-production-v2/v2_prompt.py media-production-v2/build-NN-slug --check --dump`
must PASS. If it flags a word you meant innocently, REWORD the scene — never weaken
the checker.

**E.** Announce the Chrome burst, then:
`nohup python3 media-production-v2/v2_prompt.py media-production-v2/build-NN-slug --gen > /tmp/rNNN-flow.log 2>&1 &`
~3 min per still. Watch the log for `exit=0`. Never touch a CAPTCHA — if one appears,
stop the browser and tell Cameron in one line.

**F.** 🛑 **QC EVERY SINGLE PICTURE by Reading the jpeg at full resolution.** This is
Cameron's explicit requirement and it is where the value is: row 2 rejected 13 of 19
on this step, including one frame rendered rotated 90° and one with a solid black band
across the bottom third. Nothing else catches those.

HARD FAILS → fix the PROMPT and regenerate: embedded text/border/panel/watermark ·
Jesus's face not matching the ref · anyone but Jesus in cream · wrong head/object
count · anatomy wrong (count every figure: 2 arms, 2 hands, 5 fingers where legible,
2 legs, 1 head) · duplicated character · **action or direction contradicting the
narration at a glance** · wrong time of day · modern object · cartoon/plastic-CGI/
painted look · rotated or letterboxed frame · a character who changed face or clothes
since their last frame. Then score 1–5 on story accuracy, composition, lighting,
emotion, faces, hands, fabric, period, sharpness, consistency — accept only ≥4 average
with nothing below 3.

**When a defect could recur, fix the LOCK or the ASSEMBLER, not the one frame.** Move
rejects to `assets/_rejected/` and keep them: if a reroll comes back worse, the better
picture wins and you record that honestly. Three failed rerolls on one beat → best
available wins, note it, move on. Never stall the line on one image.

**G.** Write `build.py` from build-02's template with THIS build's
LEAD/GAP/KJV_GAP/TAIL and CARD id (extract_beats prints them). **Verify every marker
resolves before rendering.** Run it, then: `bash admin/verify-mp4.sh <out>.mp4` prints
OK · ffmpeg silencedetect at −45 dB/2.5 s finds nothing · extract 4–5 frames and Read
them (right caption on right scene, inside the bottom band, white narrator / red for
exact-KJV lines in Jesus's voice / cream question card). No music bed, ever.

**H.** Write `MINISTRY-GATE.md` — the four §5 answers, honestly, as the target viewer
(rows 50–100: a stranger with no faith background).

**I.** Close the ledger row (end time, beats, gens, accepted, rerolls by defect code,
mp4 size/duration). `git add` ONLY text files — never jpeg/mp3/mp4. Commit. **ONE**
`git push` attempt with a 2-minute timeout; if it fails write "push skipped" and keep
working. Never retry pushes in a loop.

**J.** Deliver the finished video to Cameron with `SendUserFile`, one line of context.
Then **go straight to the next row. Do not wait, do not ask.**

### 3. Session hygiene

- The repo is the memory; the ledger is the state. Never rely on chat scrollback.
- QC'ing ~20 pictures at full resolution is what fills a context window. When it gets
  tight, FINISH the current row through step I, update the ledger, print exactly:
  `SESSION FULL — open a new session and say: Read V2-SESSION-FROM-50.md and execute
  it. Start at the first row not DONE. Do not stop.` Then stop. Never start a row you
  cannot finish.

### 4. Known blocker

Machine A (`Dev`) cannot `git push` — a pre-existing 12.7 GB backlog rejects every
push. Its work is committed locally and safe, but other machines cannot see
`media-production-v2/` until that is repaired. If you are on `Dev`, expect the single
push attempt to fail and keep working.
