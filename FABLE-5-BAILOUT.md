# FABLE-5 BAILOUT — read this, then make one picture

> **Cameron: open a new session, set the model to FABLE 5, and paste exactly this:**
>
> ```
> Read FABLE-5-BAILOUT.md and do exactly what it says. Nothing else.
> ```

---

## Situation

The previous session (Opus 5) spent a full night and ~$9 of Cameron's money and got
**zero pictures approved**. The full honest account is in
[`SESSION-FAILURE-POSTMORTEM.md`](./SESSION-FAILURE-POSTMORTEM.md) — read it, it will
save you from repeating it. Cameron has said this is the last chance.

**He is out of patience. Every long message costs you credibility. Be short.**

## Hard rules — breaking any one of these ends it

1. **DO NOT BUILD TOOLING.** No runners, no scripts, no meters, no detectors, no
   audits, no new law files. The last session's whole failure was building
   infrastructure instead of pictures. Everything you need already exists.
2. **ONE PICTURE AT A TIME until he approves one.** Generate one. Check it yourself at
   full resolution. Fix it. Only show him when *you* cannot find a fault.
3. **NEVER hand him work you know is flawed.** He is not your QA. If you found a
   defect, fix it before he sees it — this is his oldest and most-broken rule.
4. **API only, and verify it works before assuming.** `python3
   media-production-v2/v2_gen_api.py <build-dir> --only bNN --ceiling 5`. Flow is dead
   by his order. If a call fails, re-test before telling him anything is blocked — the
   last session told him the API was dead while it was funded and working.
5. **Verify your edit actually applied before spending.** Assemble the prompt and grep
   it for the words you just added. The last session paid twice to re-shoot prompts it
   had not actually changed.
6. **Answer plainly. No lists of options, no essays.** If he asks a question, answer it
   in one or two sentences.

## The thing that will actually make the pictures good

**Whatever a prompt does not state, the model invents, and it invents wrong.** Every
rejected picture last session was an absent instruction, not bad luck. So before you
generate, make sure the beat states ALL of these — out loud, in words:

- **Where each person is looking.** ("His eyes are on Peter in the boat, NOT at the
  camera.") Unstated → everyone stares down the lens.
- **Which way anyone travelling faces**, plus where the camera is. ("Shot from behind
  him, walking away from us up the road.") Unstated → the geography inverts and people
  run away from what they are running toward.
- **The waterline**, if water is anywhere near a person. ("Bare feet ON TOP of the
  unbroken surface, ripple rings, nothing below the surface.")
- **Whether anyone is wet.** A man walking on top of water is DRY. This is in JESUS
  LOCK v5 now.
- **Exact counts.** "Eleven men in the boat, never more, never fewer."
- **Clothing colour of everyone else, anchored to Jesus.** "Every tunic plainly DARKER
  than the one cream robe he wears." Negations like "never cream" do not hold; a
  stated positive anchored to something in frame does.
- **Time of day**, matching the scripture, stated positively.
- **Anatomy counts** for every figure: two arms, two hands of five fingers, one head.

Also: a setting lock must never name a character (it paints them into frames they do
not belong in), and a lock may only carry what is true in EVERY frame — Zacchaeus's
"a head shorter than everyone" inside his lock made him dwarfish in close-ups.

## What is already done and must not be redone

- **The Jesus face is LOCKED and picked by Cameron**:
  `media-production-v2/JESUS-V2-REF/jesus-v2-face.jpeg` — Middle Eastern, warm
  olive-brown, long dark-brown hair with bronze lights, eyes an indeterminate
  green-amber-gold he approved as reading like "a flame of fire". **Never regenerate
  it.** `JESUS_LOCK_V5` in `v2_prompt.py` is the live text lock and is already wired in.
- **118 beat maps exist** in `media-production-v2/build-*/beats_v2.py` with scripture
  facts, camera notes and locks. Use them. Do not rewrite them wholesale.
- **Row 1 `build-01-cloak` is APPROVED by Cameron** — 20 pictures, 2K, ~$2.68. That is
  your quality benchmark and your proof the format works.
- Row 7 `build-07-peter-water`: locks are fixed (boat + disciples now load on all 14
  boat beats, Peter has a lock, Jesus is dry and on the surface). `s13-come.jpeg` is
  the one frame that passed everything.

## Cameron's standing complaints — check every picture against all of them

Jesus has ONE locked face, identical everywhere · only Jesus wears cream · no halo,
glow or rim-light · gazes visibly converge on him, never a small detached figure at the
frame edge · every figure's action reads correctly at a glance · lighting matches the
scripture's stated time of day · figures stay inside the boat with deck under their
feet unless scripture puts them on the water · nobody is submerged who should not be ·
the boat always has its mast and looks the same · all the disciples are in it and each
keeps the same face · no text, borders, panels or watermarks · not cartoon, not plastic
CGI, not a painted illustration · no rotated or letterboxed frames · captions in the
bottom band only, never over the art · no music bed, narration and silence only.

## Your first task, and only this

1. Read `SESSION-FAILURE-POSTMORTEM.md`.
2. Pick the **single most important picture** in `build-07-peter-water` — Peter walking
   on the water toward Jesus (`b16 s16-step-after-step.jpeg`).
3. Make sure its beat states everything in the list above. Verify the assembled prompt
   contains what you added.
4. Generate that ONE picture. ~$0.13.
5. Read it at full resolution and judge it against every complaint above.
6. If it is flawed, fix the prompt and shoot again. Do not show him a flawed one.
7. When it is clean, send him that one picture and one short sentence.
8. **Stop. Wait for his verdict.** Do not generate anything else, do not build
   anything, do not plan the other 99 stories.

If he approves that picture, ask him for permission to do the rest of that one story
the same way — one story, checked, then shown. Nothing wider until he says so.
