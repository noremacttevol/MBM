# MBM PRODUCTION BIBLE — The Permanent Law for Making All 200 Videos

> **READ THIS BEFORE TOUCHING ANY VIDEO WORK. EVERY SESSION. EVERY AI. EVERY PLATFORM.**
> Cameron explained this system once (2026-07-08) and never has to explain it again.
> Any AI helping with MBM media reads this file first and follows it exactly.
> Cameron's job: watch finished videos and say yes or no. That's it.
> The AI's job: everything else — prompting, generating, reviewing, assembling, reporting.
> Cameron NEVER writes prompts, never edits clips, never hunts for errors. If the AI
> finds itself asking Cameron to do any of that, the AI is doing it wrong.

---

## 1. The Mission (unchanged, forever)

Every video exists to show one thing: **Jesus is good.** Story-first, scripture-true,
never argumentative, never preachy. The Jesus Method rules in CLAUDE.md / AGENT-RULES.md
govern all content. The Two-Voice Law applies: narrator speaks modern; Jesus speaks
ONLY exact KJV words. Jesus's face is NEVER shown — light, silhouette, hem, feet,
hands-never-visible. The BOM law holds: these 200 videos stay MILK.

**The Voice Law (Cameron, 2026-07-07 — permanent):** The Jesus voice is AMERICAN,
never British — he was not British. Current voices (edge-tts, placeholders until
Cameron locks finals): narrator `en-US-AndrewNeural`, Jesus
`en-US-ChristopherNeural`. Any future voice change still obeys: American, warm,
low, unhurried, same Jesus voice across all 200 videos.
**NEVER use a "Multilingual" voice model (Cameron, 2026-07-08):** the
`en-US-AndrewMultilingualNeural` narrator drifted into foreign-sounding accents
on ordinary English words (caught on video #6). Plain US models only.

**The Ear-Check Law (Cameron, 2026-07-08 — permanent):** Cameron must never be
the one who catches broken audio. After EVERY narration generation, run the
speech-to-text ear-check (`qc_narration.py`, first built in build-06-two-sons):
it transcribes every mp3 and diffs it word-for-word against the script. Any
segment under 0.93 match is regenerated (reworded if needed) BEFORE assembly.
No video is assembled, let alone shown to Cameron, with unverified narration.

**The No-Dead-Air Law (Cameron, 2026-07-08 — permanent):** The narrator carries
the story through EVERY scene. No silent "visual beats" — a mid-video stretch
without narration reads as broken to viewers ("it just stops talking"). Verify
with `silencedetect` (no gap >2.5s between first word and last); the only
allowed silences are a short breath before the closing card and the card's tail.

**The Translation Law (Cameron, 2026-07-08 — permanent):** After the Jesus
voice speaks a KJV line, the narrator NEVER re-quotes or echoes the KJV words.
He gives only the plain modern meaning ("He was asking: which of the two did
what his father wanted?"). Jesus's words belong to Jesus alone.

**The Readable-Card Law (Cameron, 2026-07-08):** The closing question card is
held long enough to read comfortably (~13s) AND read aloud by the narrator,
gently. Never cut a text card before a slow reader finishes it.

**The Self-Revision Law (Cameron, 2026-07-08 — permanent; video #6 was the
lesson):** Video #6 took FIVE revisions with Cameron catching the problems
himself. That must never happen again. Before ANY video is presented to
Cameron, the AI runs the complete revision loop itself, as many passes as it
takes:
1. Re-read this entire file and apply EVERY law — they all bind every video,
   not just the one that taught the lesson.
2. Ear-check every narration segment (transcribe + diff against the script).
3. Silence-scan the full mix — no dead air over 2.5s in the spoken body.
4. Frame-strip the full video — every caption on the right scene, KJV in
   cream italic, characters on-model, style painted not cartoon.
5. Watch it as a stranger would: does the story flow start to finish with no
   confusing scene? Would a slow reader finish every card? Does anything look
   AI-weird (things appearing or vanishing, extra objects, odd pacing)?
6. Fix everything found and loop again until a full pass finds NOTHING.
Cameron sees a video ONCE, for the final yes. He is the approver, not the QC
department. Revisions are the AI's job.

**The Full-Story Law (Cameron, 2026-07-07):** Never flatten a story to its
headline moment. Include the surrounding humanity that shows he actually cared —
e.g. for the cloak story: he was already on his way to Jairus's dying daughter,
the crowd made one sick woman nearly invisible, he FELT power go out of him,
asked "Who touched my clothes?" (KJV Mark 5:30), was questioned by his own
disciples, ignored them, and kept looking until he found her. Backstory and
resistance beats make the stop mean something.

**The Approval Law (Cameron, 2026-07-08):** Cameron gives the FINAL yes on
every video — nothing ships without it. Leighton (Cameron's daughter) is a
crew operator: she runs day shifts with the AI, reacts to storyboards and
assets, and can mark a finished video "READY FOR DAD," after which she and
the AI continue to the next story in the queue. Shift handoffs are spoken in
chat: "Leighton is working on it for the day" / "this is cameron again." The
crew's full operating manual is **CREW-GUIDE.md** — any AI doing media work
reads it alongside this file. The AI also teaches while it works (plain-word
explanations, prompts shown before submitting) so the crew grows toward
running Flow themselves with the AI in prompt-only mode.

**The Feedback-Study Law (Cameron, 2026-07-08):** Video #1 v2 is approved to
HOLD as-is and gather real viewer comments. Known self-critique to beat in
future videos: it reads as AI-made and paces slow. Every batch of viewer
comments gets studied and distilled into new QC lines in section 5. Current
improvement targets: (a) tighten pacing — trim dead air between beats, let
strong images breathe less when the narration has already moved; (b) chase
the human feel — vary shot rhythm, favor faces/hands/small human details of
the PEOPLE (never Jesus), let emotion land in the pictures, not just the
words. Nothing here overrides the sacred pause before Jesus's KJV words.

## 2. THE LOCKED LOOK — Master Style Block (never change without Cameron's explicit word)

Every image and every video clip for all 200 videos begins with this exact text:

```
Beautiful hand-painted 2D animation style, reverent and warm, like a classic
illustrated storybook of scripture brought to life. Soft painterly brushstroke
textures, glowing golden light, muted earth tones with warm gold highlights.
First-century Judea. Slow, tender movement. Sacred, hushed tone. Not
photorealistic. No text or captions in the image. Historically modest clothing:
rough-woven wool and linen in undyed earth colors. No modern objects.
```

(For stills, drop the "Slow, tender movement" line.)

- **Approved reference:** the clip "Woman touches cloak hem" in Flow project
  "MBM Story Videos — Wave One" (generated 2026-07-08, Veo 3.1 Fast) is the visual
  gold standard. Every new generation is compared against it. When Flow's
  Ingredients/reference-image feature is available, use frames from approved clips
  as style anchors to hold consistency.
- **Consistency check (every asset):** same palette (warm gold/earth), same painted
  texture, same reverent lighting. If a generation drifts toward photorealism,
  3D-render look, cartoon-comedy look, or a different palette — reject and
  regenerate. Style drift is a QC failure equal to a scripture error.
- The photoreal live-action direction is DEAD (Cameron, 2026-07-08). Never revive it.

## 3. The Hybrid Pipeline (stills + motion, story decides the mix)

**The format:** narrated storybook videos. Beautiful painted stills carry most of the
runtime with slow camera drift (Ken Burns) added in assembly. Real animated video
clips are used ONLY where the story's power demands motion — the "money moments."

**THE STORY-FIT RULE (Cameron's law):** there is NO fixed ratio. The story decides.
- A quiet parable told mostly by the narrator may be ALL stills (0 video clips).
- A standard story: ~10–14 stills + 1–2 animated clips for its money moments.
- A story whose heart IS motion (calming the storm, walking on water) may earn
  3–4 animated clips. That's the ceiling without flagging it to Cameron in the
  session report (not asking permission — just visibility on credit spend).
- Every story gets a STORYBOARD first (section 4) that declares which beats are
  stills and which earn motion, with one line of why.

**Validation sequence (locked):** the first two full productions after video #1 are
LOW-ANIMATION stories (mostly/entirely stills) to prove the cheap end of the format
works. Then scale the motion budget per story as the Story-Fit Rule allows.

## 4. Per-Video Assembly Line (the AI runs every step)

1. **Scripture card.** Pull the exact KJV passage. Derive two lists from the text
   alone: MUST SHOW (facts the text states) and MUST NEVER SHOW (things the text
   contradicts + the standing rules: Jesus's face never, Jesus's hands never,
   Jesus never touches first in stories where the person reached for him, etc.).
   The card is written into the video's production pack before any generation.
2. **Storyboard.** 8–16 beats. Each beat marked STILL or MOTION with a one-line
   reason. Narration line drafted per beat. Jesus's KJV words (if any) placed.
3. **Generate stills** in Flow (Image mode, 9:16, master style block + beat prompt
   + the card's MUST NEVER SHOW items as explicit "no ..." lines). 1–2 credits each.
   Review each against the card at a glance; regenerate misses immediately.
4. **Generate motion clips** (Veo Fast, 9:16, 1x, 8s) for money moments only.
   Same style block + card prohibitions in the prompt. Review IN THE PLAYER,
   not just the thumbnail — scrub start/middle/end. (Lesson learned: a wrong
   hand hid in motion once. Never approve from a thumbnail again.)
5. **Assemble locally** (ffmpeg/editor on Cameron's machine — costs nothing):
   drift moves over stills, clips cut in at their beats, narration track,
   serif captions, KJV verse card, closing question card (6s, cream #F7F2E9),
   music bed cut to silence at the sacred line. Export 1080×1920 H.264 <25MB.
6. **QC pass (checklist below), then present the finished video to Cameron.**
   He watches and says yes/no. On yes → delivery pipeline (Firebase Hosting
   /story-videos/, expo-video key per THE-200 id). On no → AI fixes and re-presents.

## 4b. RIGHT-FIRST-TIME PRE-FLIGHT (Cameron, 2026-07-08 — check the PLAN before generating anything)

> Cameron's directive: stop relying on revisions to reach perfect. The Self-Revision
> Law is the safety net, not the method. The method is this pre-flight: every known
> failure from past videos is checked ON PAPER, in the production pack, BEFORE any
> credit is spent or any assembly is run. Fixing a script costs nothing; fixing a
> built video costs time, credits, and trust.

**Before generating ANY audio (check the written narration script):**
- [ ] FULL-STORY check: read the parable's scripture END-TO-END against the
      beat map — every scene and every character Jesus put in the story is in
      the storyboard, through the FINAL verse. Half a parable sells half the
      point (added 2026-07-09, video #2: first cut ended at the feast and
      omitted the older brother — the entire half aimed at the religious men
      the story was told to answer. Cameron caught it, not the loop.)
- [ ] Every scene in the storyboard has a narration line — map beat-by-beat; no
      silent "visual beats" exist anywhere in the plan (No-Dead-Air Law)
- [ ] No narrator line quotes or echoes KJV wording — plain modern meaning only
      (Translation Law); Jesus lines are exact KJV, verified against the passage
- [ ] Read every line ALOUD in your head for TTS traps: clipped phrases
      ("he just went to work"), odd contractions, tongue-twisters — reword now
- [ ] Voices are `en-US-AndrewNeural` + `en-US-ChristopherNeural` — no
      Multilingual model anywhere (Voice Law)
- [ ] The closing card text is written to be READ ALOUD by the narrator and the
      card is scheduled ~13s (Readable-Card Law)

**Before generating ANY image or clip (check the written prompts):**
- [ ] Master Style Block byte-identical, zero added style words (§5b ban #2)
- [ ] No "NEGATIVE PROMPT:" list; every constraint stated positively — exact
      counts, exact emptiness, "one single figure and only him" (§5b ban #1)
- [ ] Character/wardrobe locks and prop locks written into EVERY prompt for
      every scene the character/prop appears in (wardrobe drift, lamp lesson)
- [ ] No beat asks the model for an "AI tell": instant physical changes (sweat
      appearing), objects popping in, anything materializing — plan the beat so
      the risky detail simply isn't requested (video #6 sweat lesson)
- [ ] MUST NEVER SHOW items from the scripture card confirmed against each prompt

**Before assembly (check the timing math):**
- [ ] Measure real durations of every generated audio file; recompute all
      offsets from measurements, never from estimates
- [ ] On-paper silence map: no gap >2.5s between segments in the spoken body
- [ ] Measure the silent TAIL inside each mp3 (TTS files can carry ~1s+ of
      trailing silence); compute every breath/gap from the SPOKEN end, not the
      file end — verify with silencedetect after the mix (added 2026-07-08,
      video #2: j1's 1.2s internal tail stretched a planned 2s breath to 3.5s)
- [ ] Music bed scheduled to reach full silence BEFORE the peak KJV line

**Assembly craft laws (added 2026-07-09 — Cameron: "it just seems like a video
made by ai, it glitches" — every one of these was a real, found defect):**
- [ ] ANTI-SHIMMER: never render zoompan straight at delivery resolution.
      zoompan rounds its crop to whole pixels each frame — at 1080 that
      stepping is visible on slow drifts (the "AI slideshow" jitter). Render
      the move supersampled (≥4x input, 2x output) and lanczos down to
      delivery size so steps land on quarter-pixels. Measured fix: frame-to-
      frame motion variation halved.
- [ ] CAPTION FADES: captions never pop in or out at a cut. Render each
      caption (text + box + shadow) on its own transparent RGBA layer,
      alpha-fade 0.5s in and 0.5s out (gone ~0.1s before the cut), overlay.
- [ ] ENCODE: intermediates near-lossless (crf 16); final pass is the ONLY
      lossy generation — preset veryslow, start crf 21, step up only if the
      <25MB law demands it. Never starve the bitrate to fit (1050k caused
      visible blocking on video #2).
- [ ] LOUDNESS: measure the final mix (EBU R128) and deliver ≈ -15 LUFS via
      static gain + true-peak limiter. Quiet audio reads as amateur.
- [ ] MUSIC BED: no bare sine waves — every voice a slightly detuned pair
      (natural slow beating) through a soft room echo. And no long bone-dry
      stretches unless sacred quiet IS the point of that moment.

Only after this pre-flight passes does generation begin. Then the Self-Revision
Law loop runs on the built video — and if the pre-flight was done honestly, that
loop should find nothing. Every time the loop DOES find something, that means a
check is missing from this list: add it, dated, so the next video is right the
first time.

## 5. QC Checklist (every video, before Cameron ever sees it)

- [ ] Every MUST SHOW item from the scripture card appears
- [ ] Zero MUST NEVER SHOW items appear (scrub every motion clip fully)
- [ ] Jesus's face never visible in any frame; his hands never visible
- [ ] Style matches the gold-standard reference (palette, texture, tone)
- [ ] No AI text/gibberish baked into any image
- [ ] Narration modern; Jesus voice EXACT KJV only
- [ ] Verse card wording pulled from PAIRING-LIST.md, text fetched not hand-typed
- [ ] Closing question matches the pack's Seed question
- [ ] 9:16, 1080×1920, plays clean start to finish

## 5b. PROMPT FAILURE LOG (banned techniques — every mistake that wasted credits gets written here so no AI repeats it)

**2026-07-08 — The "NEGATIVE PROMPT" cartoon disaster (video #8, Scene 4, 10 credits wasted).**
The clip came back flat-cartoon (big glossy Disney eyes, plastic shading) and clashed
hard with the painted stills around it. Crew verdict: "horrible, way worse." Two causes,
both now BANNED:

1. **NEVER put a "NEGATIVE PROMPT:" list inside a Veo prose prompt.** Veo does not
   honor negative lists. Naming the things you don't want ("two coins", "AI-generated
   look", "3D CGI") puts those words INTO the prompt and can pull them into the video.
   Say what you WANT, positively and only that: "EXACTLY ONE coin — one single coin,
   and only that one coin, in the whole video."
2. **NEVER add or strengthen style words beyond the locked Master Style Block.** Adding
   emphasis like extra "2D animation" wording shoved the output into cartoon land. The
   Master Style Block in section 2 is used byte-identical, every prompt, no additions,
   no paraphrasing. Style drift = automatic redo, so don't invite it.

Standing rule: every future prompt failure that wastes credits gets its own dated entry
here, with the cause and the ban, before any retry is attempted.

## 6. Money & Credits (why this plan is affordable)

- **ACTIVE PLAN (Cameron, 2026-07-08): Google AI Ultra $200 tier = 25,000
  credits/mo.** Bought specifically to produce the corpus at full speed for the
  next month. Use it thoroughly — the constraint is now throughput, not credits.
  Round-the-clock crew shifts (Cameron nights, Leighton days) exist to spend it.
- Stills: 1–2 credits. Veo Fast clip: 10 credits on Ultra.
- Typical video ≈ 25–60 credits. All 200 ≈ ~11,000 credits including retakes —
  the $200 tier covers all 200 in one month with >2x margin. Credits don't roll over.
- The AI reports credit spend in every session log entry so Cameron always knows
  where the month stands. Big-motion stories (3–4 clips) get flagged in the report.

## 7. What Cameron's money is buying (the promise this file enforces)

Same look, same feel, same flow, every video, no matter which AI session makes it —
because the style block is frozen text, the pipeline is frozen steps, the QC list is
frozen checks, and this file is the single source of truth. If any future direction
change is wanted, Cameron says it once, this file gets edited and committed, and the
new law holds from then on. Nothing lives in anyone's memory. Everything lives here.

## 8. Session workflow for any AI picking up media work

1. Read CLAUDE.md chain protocol, START-HERE.md, AGENT-RULES.md — then THIS FILE.
2. Check SESSION-LOG.md top entry for where production stands (which video, credits left).
3. Continue the assembly line exactly where it stopped. No re-litigating style or format.
4. End of session: SESSION-LOG.md entry (videos progressed, credits spent/left,
   any QC lessons learned added to section 5), commit, push.

---
*Created 2026-07-08 from Cameron's direction. This file outranks any older media doc
where they conflict (00-MASTER-PLAN.md production packs remain valid for story
content, narration scripts, Seeds, and scripture cards — only their photoreal
style blocks are replaced by section 2 above).*
