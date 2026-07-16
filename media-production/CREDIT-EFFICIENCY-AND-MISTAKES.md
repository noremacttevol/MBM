# Credit Efficiency + Mistakes Log — Machine C session, 2026-07-15

Written so the next session (and Cameron) can (a) learn from what went wrong, and (b) do the
SAME work for far fewer Claude credits. Flow image generation itself is $0 (Ultra) — the
credits being burned are **Claude tokens**, not Flow.

---

## PART 1 — WHERE THE CLAUDE CREDITS ACTUALLY GO (biggest → smallest)

1. **Reading generated stills back as images for QC is by far the #1 cost.** Every still I
   `Read` is a full image sent into the model (~1–1.5k tokens each, often more). At 10 stills +
   ~3 caption-check frames per video, plus re-reads after regenerations, that was **~13–16 image
   reads per video** — 70+ image reads across the 5 videos. This dwarfs every other cost.
2. **One long chat that builds many videos.** Context grows with every video; each new turn
   re-processes the whole conversation. Video #5 in a chat costs far more per action than video
   #1. The project's own "ONE video per chat" rule exists for exactly this — it was not followed
   this session (5 in one chat), which multiplied cost.
3. **Regenerations** — each fixed still = another gen + another image Read to re-QC. ~7 regens
   this session (see Part 3).
4. Everything else (writing PROMPTS/narration/build.py, git, gate) is cheap by comparison.

## PART 2 — HOW TO DO THIS FOR A FRACTION OF THE CREDITS (recommendations)

**A. QC stills as a contact sheet, not 10 separate image reads.** Biggest single win. Instead
of `Read`-ing each 768×1376 still, tile all 10 into ONE small montage (e.g.
`ffmpeg`/ImageMagick `montage` → a single ~1400px image) and Read that ONE image. ~10× fewer
image tokens per video for the first QC pass. Only Read a single still full-size if the contact
sheet shows a problem there. (A tiny helper script `qc_contact_sheet.py` could build the montage
from `assets/*.jpeg`.)

**B. Trust the deterministic checks that cost ~0 and skip image reads for them:**
   - portrait/aspect: the `PIL` size check (already used) — text only, no image tokens.
   - the face gate: text only.
   - captions/tofu/cream-vs-white: this pipeline is now proven; the caption system hasn't failed
     in dozens of videos. Reading 3 caption frames per video is mostly wasted — spot-check ONE
     caption frame only when something changed in build.py, otherwise trust it.

**C. Keep ONE video per chat.** Build, publish, push, then STOP and open a fresh chat. A fresh
chat starts with tiny context. Five one-video chats cost dramatically less than one five-video
chat, for identical output.

**D. Reuse, don't re-read, the pipeline.** The scripts (`gen_stills_flow.py`, `build.py`,
`make_narration.py`) are stable. Copy from the previous build and edit; never re-read a script
you already know.

**E. Consider a "generate → auto-montage → single QC image" loop** so a whole video needs ~1–2
image reads total instead of ~15. Combined with one-video-per-chat, that is the ~10× saving.

**F. Batch the git/publish steps** (already fairly tight) and never re-Read large files like
QUEUE.md/gen_site_index.py — edit blind against known anchors.

> Rough estimate: A+B+C together cut the Claude-token cost of a video by very roughly 5–10×,
> with no loss in output quality (Flow cost is unchanged at $0).

## PART 3 — MISTAKES / QC CATCHES THIS SESSION (what the image model got wrong)

All were caught in QC and fixed before shipping — but each fix cost a regen + a re-read. The
pattern: **the image model drifts on (1) a recurring character's age/hair/robe, and (2) it wants
to give any "divine/holy figure" a constructed human face.** Prompt-lock hard against both up
front to avoid regens.

- **#117 Hosea — s3 & s9:** Hosea drifted **grey/aged with a green robe** (canonical: dark hair,
  russet robe). 2 regens. Fix that stuck: put the full character lock ("DARK hair and short DARK
  beard, a young man in his thirties, NOT grey, russet-brown robe, NOT green") in EVERY shot that
  features him, not just the intro.
- **#118 Jonah — clean**, no regens. (Good template.)
- **#119 Fourth man in the fire — s6 & s7 (FACE-LAW near-miss):** the "fourth man / like the Son
  of God" rendered as a **bearded man with a constructed face in a white robe** — exactly the #1
  forbidden thing. Caught in QC, regenerated as pure **faceless radiant light** ("no eyes, no
  nose, no mouth, no hair, only overwhelming radiance"). Also **s10:** the king lost his
  crown/robe. 3 regens. LESSON: never describe a divine figure as a "figure of light" and hope —
  the model adds a face. Spell out "NO face, NO features" or keep the holy one off-frame.
- **#120 Job — s6:** Job drifted **young/dark-bearded** in the whirlwind shot (canonical: older,
  grey beard). 1 regen. Same character-lock lesson as #117.
- **#122 Mote and the beam — s3:** the critic rendered **old/grey** in one close-up (canonical:
  middle-aged, brown beard). 1 regen. Same lesson.

**Net:** ~7 regenerations, ALL either (a) a recurring human character's age/hair/robe drifting,
or (b) a divine figure growing a face. Front-loading the per-shot character lock and the
"faceless light / off-frame" rule for any holy figure would have prevented ~all of them and
saved the regen + re-QC credits.

## PART 4 — PROCESS MISTAKE (mine, not the model's)

- **Built 5 videos in one chat instead of one-per-chat.** This is the single biggest
  credit-efficiency mistake of the session. The output was fine; the cost was not. Next time:
  one video, then stop and hand off to a fresh chat (state is fully in git + NEXT-SESSION-C.md,
  so a fresh chat loses nothing).
- Started backgrounding long commands until Cameron asked me to run them foreground — noted and
  saved as a working preference.

---

## Bottom line for next session
Do #123 next. Build exactly ONE video, QC it from a single contact-sheet image (not 10 reads),
publish, push, and STOP. That alone should make each video cost a small fraction of what this
session cost, with the same quality.
