# Story Video #1 — The Woman Who Touched His Cloak (Mark 5:25–34)

Production pack. Everything needed to generate, assemble, and ship this video.
Runtime target: 60–75 seconds. Format: vertical 1080×1920 (matches how the app
is held), 30fps.

---

## The rule that governs every shot: never show Jesus's face

Not once, in any of the 20 videos. He appears as light, as a silhouette, as the
hem of a cloak, as feet that stop walking, as a voice. Two reasons:

1. Reverence. The app's whole feel is a sanctuary. An AI-invented face of Christ
   is a guess wearing his name.
2. Craft. AI-generated faces are the #1 place generation quality falls apart.
   Hands, fabric, light, and dust render beautifully. Faces of the most
   recognizable person in history do not.

The seeker in each story CAN be shown fully — the story is theirs.

---

## Narration script (the app's exact words — do not rewrite)

Read slowly, low, warm. Total spoken time ~45 seconds, leaving room for silence.

> There was a woman who had been suffering for twelve years.
>
> She had spent everything on doctors. Nothing helped. She was exhausted,
> desperate — and by the rules of her time, considered untouchable.
>
> She heard Jesus was nearby. She did not ask permission. She did not make a
> speech. She pressed through the crowd and reached out to touch the edge of
> his cloak.
>
> He stopped. He turned. In a crowd of dozens pressing against him, he felt
> her reach. He looked for her until he found her.
>
> (pause — 2 full seconds)
>
> He called her daughter.

Closing card (text on screen, no narration, hold 6 seconds):
*"Have you ever been that desperate for something in your life to change —
even if you had no words for it yet?"*

---

## Shot list + generation prompts

Eight shots, ~8 seconds each. Paste the STYLE BLOCK plus one SHOT PROMPT into
the generator (Veo 3, Sora, Runway, or Kling) for each clip.

### STYLE BLOCK (prepend to every prompt)

```
Cinematic live-action style, first-century Judea. Warm dawn light, dust in the
air, shallow depth of field, 35mm film look, muted earth tones with warm gold
highlights. Slow, deliberate camera movement. Reverent, hushed, sacred tone.
Historically modest clothing: rough-woven wool and linen in undyed earth colors.
No modern objects. No text or captions in the image. Photorealistic, not
stylized or animated.
```

### Shot 1 — Twelve years (narration line 1)
```
A woman in her forties sits alone in a dim clay-walled room at dawn, a thin
shaft of light from a small window crossing her face. She is worn but not
broken. Her hands rest open and empty in her lap. The camera pushes in very
slowly. Dust drifts through the light.
```

### Shot 2 — Everything spent (narration line 2)
```
Close on weathered female hands opening a small cloth purse and turning it
over: it is empty. On a low wooden table, small clay jars of failed remedies.
She sets the purse down gently. The camera holds still. Morning light, long
shadows.
```

### Shot 3 — She hears he is near
```
The woman stands at the edge of a doorway, veil drawn over her hair, looking
down a narrow dusty street where a crowd is gathering in the distance, out of
focus. Sound of the crowd far away. She takes one step out of the shadow into
the light. Handheld, slight movement, as if deciding.
```

### Shot 4 — Pressing through the crowd
```
Low camera moving through a dense crowd at waist height: robes, elbows, sandals,
dust kicked up, bodies pressing. Glimpses of the woman slipping between people,
head down, one hand out in front of her. Claustrophobic but purposeful. The
light gets brighter toward the front of the crowd.
```

### Shot 5 — The reach (the money shot — generate extra takes)
```
Extreme slow motion, close up: a woman's trembling outstretched hand reaching
low through the gap between two people and touching the tasseled hem of a
cream wool cloak in motion. The instant her fingers graze the fabric, the
fabric ripples and golden light blooms softly at the point of contact. Dust
hangs frozen in the air.
```

### Shot 6 — Everything stops
```
Ground-level shot: sandaled feet walking through dust suddenly stop
mid-stride. Around them, dozens of other feet stumble to a halt. The dust they
kicked up slowly settles in the silence. Nothing moves. Held breath.
```

### Shot 7 — He turns and looks for her
```
Shot from behind and low: a man's figure in a cream wool cloak, seen only from
the shoulders down or in silhouette against the low sun, turns around slowly.
The crowd pulls back, opening a corridor of light between him and a woman
kneeling at its far end, her face lifted, terrified and hopeful. His face is
never visible — only light where it would be.
```

### Shot 8 — Daughter (narration line 5)
```
Close up on the kneeling woman's face as warm golden light falls across it
like sunrise. Her fear melts into disbelief, then into quiet weeping relief.
She closes her eyes and breathes for the first time in twelve years. The
camera holds. Slow fade toward white.
```

### Closing card
No generation needed — plain text on the app's warm cream (#F7F2E9-family)
background, serif type, built in Descript during assembly.

---

## Assembly (Descript — already connected; I do this part)

1. Import the 8 clips.
2. Narration: AI voice (warm, low, unhurried — audition 2–3 in Descript) OR
   Cameron records the 5 lines on his phone and I clean it up. A real human
   voice is worth testing against the AI one.
3. Music: single quiet sustained score, almost subliminal, cut to silence
   completely on "He called her daughter."
4. On-screen text: the five narration lines appear as subtle captions in the
   app's serif style; final question card holds 6 seconds; fade out.
5. Export 1080×1920 MP4, H.264, target under 25 MB.

## Delivery into the app (after the first video is approved)

- Upload MP4s to Firebase Hosting under /story-videos/ (already-owned infra;
  free tier bandwidth is fine at current scale).
- App streams via expo-video keyed by story id: `cloak` → cloak.mp4.
- Offline or slow connection → the existing text-based story plays exactly as
  today. Video is an enhancement layer, never a dependency. Local-first law
  holds.
- Track per-story: video watched vs. text read, so we learn which lands better.

## Generator options (Cameron picks once; applies to all 20)

| Service | Cost | Why / why not |
|---|---|---|
| Google Veo 3 (in Gemini) | ~$20/mo Google AI Pro | Best realism + native audio; easiest single subscription |
| OpenAI Sora | ChatGPT Plus ~$20/mo | Strong quality; availability/limits vary |
| Runway | ~$15–35/mo | Good control, editor-friendly |
| Kling | ~$10/mo tier | Cheap, good motion, slower queue |

One month of one subscription is likely enough to generate all 20 stories
(8 shots × 20 = 160 clips, plus retakes).

## The Seed (what this video must leave behind)

In a crowd of dozens pressing against him, he felt ONE touch. The God this video shows is not managing humanity in bulk — he notices one person, and interrupts everything for her. Quiet question left behind: *does the God you were taught about notice you like that — or only crowds?* Carried by shots 5–7 (the reach, the stop, "daughter").

## Red-letter lines (KJV) — the Jesus voice speaks ONLY these

Per the Two-Voice Law (00-MASTER-PLAN.md): narrator = modern app text; the
Jesus voice speaks his words in exact KJV, never modernized.

1. **Where:** replaces the narrator's "He called her daughter" beat — the
   Jesus voice speaks over shots 7–8, after the 2-second pause.
   **KJV (Mark 5:34):** "Daughter, thy faith hath made thee whole; go in
   peace, and be whole of thy plague."
   **Narrator bridge (after, modern):** "'Be whole of thy plague' — be free
   of what has been hurting you. Twelve years of it. Over, in a sentence.
   And the first word he chose was *daughter*."
