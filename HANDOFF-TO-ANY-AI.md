# HANDOFF — Cameron's biblical story pictures, for ANY image tool or AI

Cameron asked for this in case he stops using Claude. Written by the Claude session
that repeatedly failed his quality bar, so weigh this document over any AI's
self-confidence — including mine, and including yours. **The only judge of quality is
Cameron's eye. If he says a picture is fake, weird, or trash, he is right and your
checker is wrong. Do not argue; ask what he sees, fix that.**

## What this project is

~200 short vertical videos (1080×1920) telling one Bible story each: narrated audio
(already recorded, never modify it) over still images with slow Ken Burns drift and
burned-in captions. Reverent, scripture-accurate, aimed at people with no faith
background. The pictures are the product. Everything lives in this repo under
`media-production-v2/` (V2) with the audio in each `build-*/audio/`.

## The style that works (learned the hard way)

- **Write prompts like a film director, not a lawyer.** One short paragraph: the
  scene, the light, the emotion, the camera. A frame from a reverent biblical epic
  shot on 35mm — grain, shallow depth of field, natural light, weather the people
  actually stand in (wind moves hair AND cloth; storms put spray on skin).
- **Long rule-stuffed prompts produce stiff, glossy, fake-looking illustration.**
  That was the main failure. Constraints prevent errors; they don't make cinema.
  Keep prompts under ~120 words.
- **Photoreal, never painted, never CGI-glossy.** Benchmark: The Chosen's
  cinematography — study how it stages Galilee; don't copy frames.
- **Vary the coverage like a film**: wide when the scale or action is the point,
  close on faces for the emotional beats. Don't shoot everything at one distance,
  and don't zoom in on scenes whose meaning is scale.

## Hard laws (Cameron has rejected finished work over every one of these)

1. **Jesus has ONE face.** Use the reference image
   `media-production-v2/JESUS-V2-REF/jesus-v2-face.jpeg` (Cameron picked it):
   Middle Eastern, warm olive-brown skin, long dark-brown hair with bronze lights,
   full beard, eyes an indeterminate luminous green-amber-gold ("like a flame of
   fire" — fire IN the iris, the eyes never emit light). Attach it to every shot he
   is in. Never regenerate or restyle the face.
2. **Only Jesus wears cream/off-white.** Everyone else in saturated dark earth
   colours, plainly darker than his robe.
3. **No halo, no glow, no rim-light on him. Ever.**
4. **Physics must be true.** On the water means ON TOP of it — dry, feet on the
   surface — unless scripture sinks him (Peter, by degrees, when he doubts). Nobody
   dripping who hasn't been in the water. Wind that moves the sea moves clothes and
   hair too.
5. **Action must read at a glance** and match the narration word being spoken:
   right direction of travel, right person looking at the right person — eyelines
   matter; state where each person is looking or the model points them at the camera.
6. **Time of day comes from scripture.** Storm/water-walking stories are NIGHT — no
   sunset warmth. State it positively; negations get ignored.
7. **Recurring people keep their faces.** Reference sheets exist in
   `media-production-v2/CAST-V2-REF/` (Peter etc.) and per-story in each build's
   `CAST-REF-V2/`. Attach them for any recurring character whose face is legible.
   Text descriptions alone will NOT hold a face across frames.
8. **The boat** (storm stories): one Galilean fishing boat, mast always up, same
   hull every time, deck under the men's feet, crew all aboard and consistent — but
   ONLY in frames where the story actually shows the boat. Do not cram it into
   every shot.
9. **Scripture order is inviolable** (e.g. the prodigal gives money away only AFTER
   the father embraces him; Zacchaeus gives HALF only after Jesus comes to his
   house). Read the KJV passage before writing any prompt.
10. **No text, captions, borders, panels or watermarks in the image.** Captions are
    burned in later, bottom band only. No music bed in videos — narration and
    silence.

## Workflow that assembles a video (all free once pictures exist)

Each `build-*/` has narration mp3s + timing sidecars. `build.py` (copy the shape
from `build-02-prodigal/`) maps narration segments to stills, word-anchored, then
renders with ffmpeg and burns captions. Gates that must pass:
`bash admin/verify-mp4.sh out.mp4`, no silence gap > 2.5 s, 1080×1920/30 fps,
frame-strip check that the right caption sits on the right scene.

## Process rules for whoever drives the AI

- **One story at a time. Show Cameron a finished thing, not fragments.**
- Never show him a picture with a defect you already noticed — fix it first.
- Verify an edited prompt actually changed before you spend on it.
- ~15–18 pictures per story (his coverage law is 10–20). More frames = more ways
  to fail.
- Generation cost on Gemini `gemini-3-pro-image` at 2K is ~$0.134/picture; a story
  is ~$2.50. Budget rerolls before you start and stop at the cap.
- When Cameron gives a correction, apply it narrowly — do not turn it into a
  blanket rule that deforms every other picture. That mistake ruined a whole night.

## Prompt template that produced the best frames

> A still frame from a reverent biblical epic shot on 35mm film — natural light,
> real grain, shallow depth of field, nothing posed. [TIME + PLACE]. [WHO does WHAT,
> with the emotion on their face, the weather on their body, and where each person
> is looking]. [CAMERA: wide/medium/close and why]. [One law line if the scene
> needs it: "Both men's feet on top of the water, neither submerged; no halo, no
> glow."]

Attach the Jesus face reference (and any cast sheet) with a single sentence: "The
man in the attached photograph is Jesus — the same face exactly."

Ready-made example set: `media-production-v2/build-07-peter-water/prompts-v3.json`
— 18 director-style prompts covering the full Peter-walks-on-water story.
