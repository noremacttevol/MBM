# THE GREAT PLAN — Project Home

Cameron's episodic film of the entire Latter-day Saint account of what God has
done for His children — told as one continuous war between the Father's will
and Lucifer's will, from the council in heaven to today. A realization piece
and a testimony of the restored gospel.

**Read [MASTER-STORY.md](./MASTER-STORY.md) first — every script answers to it.**

| File | What it is |
|---|---|
| [MASTER-STORY.md](./MASTER-STORY.md) | The canonical six-movement story. Scripts are written FROM it. |
| [EPISODE-MAP.md](./EPISODE-MAP.md) | **Part A** — all 33 episodes with loglines + scripture anchors. Cameron approves this before Part B. |
| `episodes/` | **Part B** — finished episode packets (VO script + shot list), four at a time, only after Part A approval. |

---

## Relationship to MBM

This is a **separate production lane** from the 200-video scripture-story
queue in `media-production-v2/`:

- The 200-queue is Phase-1 **stills-only** by law. The Great Plan is
  Cameron's explicit exception: it uses **AI motion clips** (stills animated
  via image-to-video), per his 2026-08-31 direction.
- **The locked faces carry over.** When Jesus appears (Movement III onward),
  every still uses the same locked face pipeline as the main queue
  (`media-production/JESUS-V2-REF/` + lock text) so Jesus is the SAME person
  across every MBM property. Recurring cast (Adam, Eve, Joseph Smith, etc.)
  get their own locked reference images the same way, kept in this folder
  once generated.
- Distribution (app / YouTube / milkb4meat.org) is an open decision — it does
  not block story or production work.

## Depicting the divine (standing decisions)

- **The Father and the Son are two distinct embodied persons** — that IS the
  doctrine and the film shows it (council, Grove). No abstraction, no light
  blob standing in for a person.
- **THE DEVIL LAW (Cameron, 2026-08-31): the devil has NO body — he is a
  spirit and a voice that sounds evil. He is NEVER rendered as a figure,
  character, monster, or man in ANY scene, including the premortal council.**
  On screen he is darkness gathering, shadow spreading, cold absence, a
  veil — the camera never finds him. His presence is carried by his VOICE
  (a produced voice cast to sound evil, locked once and reused in every
  episode) and by what the darkness does. Scripture's personified images
  (the serpent in Eden, the great chain of Moses 7:26) are rendered as the
  image scripture names — a serpent, a chain of darkness — never as a
  humanoid devil. This also kills the face-consistency problem: there is no
  devil face to keep locked. The film never makes him attractive or funny;
  his menace is in his voice and in what he takes.
- No halo/glow/rim-light outlining faces (same law as the main queue).
- Reverence outranks spectacle in every frame. "Fun and exciting battle"
  means the STAKES stay thrilling — never that sacred beings get action-movie
  treatment.

## Voice cast (Cameron, 2026-08-31: produced narrator, not Cameron's voice)

- **Narrator:** produced voice. Default = the SAME narrator voice as the
  first 200 videos (ElevenLabs Brian) so every MBM property sounds like one
  storyteller — Cameron can veto for a new dedicated voice.
- **Jesus:** speaks only exact KJV words, in the same locked Jesus voice as
  the main queue (Chris). Same voice + same locked face = one Jesus across
  everything MBM makes.
- **The devil:** his own locked voice that sounds evil — cast by rendering
  his Episode 1 council speech (Moses 4:1 KJV) in 2–3 candidate voices for
  Cameron to hear and pick ONE, which is then locked for all 33 episodes.
- **The Father:** speaks rarely and only exact scripture ("This is My
  Beloved Son. Hear Him!"). Voice cast the same audition way, with maximum
  reverence, before Episode 1 ships.

## Format & distribution (Cameron, 2026-08-31)

- **1080×1920 vertical (9:16), phone-scroll first** — identical to the 200-
  queue delivery spec. Every still is generated and framed for vertical.
- Distribution = the same three surfaces as the first 200 videos: social
  media + the app gallery + the website (milkb4meat.org).

---

## Production method (Cameron's locked order — do not reverse)

You are not generating a 3-minute movie in one prompt. Each episode is
**8–12 shots of 4–6 seconds**, cut under a voiceover recorded first.

1. **Lock the spoken words** (the script is the product; everything serves it)
2. **Render the VO** (produced voices per the Voice cast section — narrator,
   Jesus, the devil, the Father — never Cameron's own voice)
3. **Still images with locked faces** (Grok Imagine or the Gemini pipeline)
4. **Animate each still** (image-to-video)
5. **Edit picture to the voice** (CapCut or DaVinci)
6. **Music last**

Reversing this order burns credits on clips that cannot be used.

**Shot-type law:**
- **People = image-to-video** (animate an approved still — protects faces)
- **Skies, halls, oceans, maps, cosmos = text-to-video** (no faces at risk)
- Keep every face clip at **4–6 seconds** or the person turns into someone
  else.

**Reusable motion prompt** for almost every sacred still:

```
Preserve the exact faces, clothing, and composition. Slow push-in. Slight
wind in the robe. Dust motes in gold light. No new characters. No cut.
Reverent, stable, cinematic.
```

---

## Build order

Proof-of-method first — these four, in this order, before anything else gets
produced:

1. **Episode 1 — The Two Wills**
2. **Episode 8 — Not Damned for Adam**
3. **Episode 23 — The Famine of the Word**
4. **Episode 26 — The Grove**

If those four hold, the other 29 are the same method.

## Workflow gates

1. ✅ Master story locked (MASTER-STORY.md)
2. ⬜ **Part A approved** — Cameron approves EPISODE-MAP.md loglines
3. ⬜ Part B scripts — four episode packets at a time, starting with the
   proof-of-method four
4. ⬜ VO recorded per episode
5. ⬜ Stills → animation → cut → music per episode
