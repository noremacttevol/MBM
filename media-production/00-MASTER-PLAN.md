# MBM Story Videos — Master Production Plan

Goal: 200 cinematic story videos — the full catalog lives in THE-200.md —
so people can SEE the goodness of the Godhead, not just read about it. The
videos are the app's answer to the social-media feed: the reason someone
opens MBM at 11pm instead of TikTok.

**Placement (corrected 2026-07-07, Cameron's direction — see FEED-2.0-SPEC.md):**
videos live in the FEED, two per prescribed page, each paired with its
linked KJV verse beneath it. The 20-story opening bank stays TEXT-ONLY —
no videos in onboarding. Packs 01–20 still lead production (those stories
are entries 1–20 of THE-200); their videos ship into the feed. Offline →
verse/text only (local-first law holds).

## Pipeline (who does what)

1. **Production packs** (files 01–20 in this folder) — DONE by assistant. Each
   contains the narration script (the app's exact story text, never rewritten)
   and paste-ready shot prompts.
2. **Clip generation** — needs an AI video service (Veo 3 / Sora / Runway /
   Kling). Cameron picks one and signs in; the assistant drives it via the
   browser and collects the clips. ~6–8 clips per story.
3. **Assembly** — assistant, in Descript (already connected): narration voice,
   music, cuts, caption text, closing question card. Export 1080×1920 MP4,
   H.264, under ~25 MB.
4. **Review** — Cameron watches each finished video and approves or gives
   notes before the next is made.
5. **Delivery** — upload approved MP4s to Firebase Hosting `/story-videos/`,
   app streams by story id via expo-video. Offline → text story, as today.

## The two non-negotiable production rules

1. **Jesus's face is never shown.** He appears as light, silhouette, the hem
   of a cloak, feet, hands (in healing moments hands are allowed, face never),
   or a voice. Reverence first — an AI-invented face of Christ is a guess
   wearing his name — and it also avoids AI video's weakest output. The
   seeker in each story is shown fully; the story is theirs.
2. **The narration is the app's exact story text.** The words were written to
   the Jesus-Method standard and are already live in the app. Video
   illustrates them; it never rewrites them. (Exception defined by the
   Two-Voice Law below: lines spoken BY Jesus are delivered by the Jesus
   voice in exact KJV — everything else stays word-for-word app text.)

## The Two-Voice Law (locked 2026-07-07, Cameron's direction)

Every video has exactly two voices, the same two in all 200:

1. **The Narrator** — warm, modern, plain storytelling language (the app's
   story text, easy to understand, the way the clearest modern translations
   read). The narrator tells the story through a Latter-day Saint lens and,
   where Jesus's words are hard for a modern ear, gently unpacks them —
   showing that when you really look at what he said, he is a kind, loving,
   merciful God. The narrator NEVER speaks Jesus's lines.
2. **The Jesus voice** — a second, distinct voice (lower, warmer, unhurried)
   that speaks ONLY the words of Jesus, and speaks them ONLY in the exact
   King James Version red-letter text — the translation held sacred by The
   Church of Jesus Christ of Latter-day Saints. His words are never
   modernized, paraphrased, or trimmed mid-thought. Since his face is never
   shown, his voice IS his face: the same voice in every video, so people
   learn to recognize him before he says a word.

Pattern inside every video: modern narration carries the viewer to the
moment → the KJV red-letter words land in the Jesus voice → the narrator
gently translates anything confusing, revealing the kindness inside it.

Parable rule: inside a parable, the whole story is technically red letter.
The narrator retells the parable in modern language, and the Jesus voice
delivers only the KJV heart-lines (e.g., "this my son was dead, and is
alive again"). Each pack's "Red-letter lines (KJV)" section lists exactly
which lines the Jesus voice speaks and their KJV text.

## STYLE BLOCK — prepend to every shot prompt

```
Cinematic live-action style, first-century Judea. Warm dawn light, dust in the
air, shallow depth of field, 35mm film look, muted earth tones with warm gold
highlights. Slow, deliberate camera movement. Reverent, hushed, sacred tone.
Historically modest clothing: rough-woven wool and linen in undyed earth
colors. No modern objects. No text or captions in the image. Photorealistic,
not stylized or animated. Never show the face of Jesus; when he is in frame,
show him only from behind, in silhouette, from the shoulders down, or as
light.
```

## Assembly standards (applied to every video)

- Vertical 1080×1920, 30fps. Runtime 90 seconds to 3 minutes, story-driven
  (locked 2026-07-07): each video takes the time its story needs — big
  stories (Lazarus, Emmaus, Prodigal) run 2–3 minutes with the narrator
  teaching through the KJV lines; smaller moments stay near 90s. Never
  padded, never capped short. (Pack runtime lines predating this are
  superseded.)
- Voices: exactly two, per the Two-Voice Law — one narrator voice (modern,
  warm; Descript AI voice or Cameron's voice — audition on video #1) and one
  Jesus voice (lower, warmer, unhurried) speaking only exact KJV red-letter
  lines. Both locked on video #1 and never changed.
- Music: single quiet sustained bed; cut to full silence on each story's peak
  line (marked in each pack).
- Captions: the narration lines appear as subtle serif text, app-style cream
  on warm dark; closing question card holds 6 seconds, then fade.
- No branding, no logo, no CTA inside the video. The app supplies the frame.

## Tracker

| # | id | Story | Pack | Clips | Cut | Approved | In app |
|---|----|-------|------|-------|-----|----------|--------|
| 01 | cloak | Woman who touched his cloak | ✅ | — | — | — | — |
| 02 | prodigal | The Prodigal Son | ✅ | — | — | — | — |
| 03 | zacchaeus | Zacchaeus | ✅ | ✅ | ✅ | ✅ 2026-07-09 (V3) | — |
| 04 | nicodemus | Nicodemus at night | ✅ | ✅ | ✅ | ✅ 2026-07-09 · eight-corrections re-audit PASSED 2026-07-09 | — |
| 05 | bent_woman | The bent-over woman | ✅ | ✅ | ✅ | ✅ 2026-07-09 | — |
| 06 | two_sons | The two sons | ✅ | — | — | — | — |
| 07 | peter_water | Peter walks on water | ✅ | ✅ | ✅ | ✅ 2026-07-09 (V6) — Cameron: "I LOVE IT" | — |
| 08 | lost_coin | The lost coin | ✅ | — | — | — | — |
| 09 | rich_ruler | The rich young ruler | ✅ | ✅ | ✅ | ❌ sent back by Cameron 2026-07-09 — rework queued | — |
| 10 | well | The woman at the well | ✅ | — | — | — | — |
| 11 | storm | Calming the storm | ✅ | — | — | — | — |
| 12 | bartimaeus | Blind Bartimaeus | ✅ | — | — | — | — |
| 13 | roof | Through the roof | ✅ | — | — | — | — |
| 14 | ten_lepers | The ten lepers | ✅ | — | — | — | — |
| 15 | centurion | The centurion | ✅ | — | — | — | — |
| 16 | mary_martha | Mary and Martha | ✅ | — | — | — | — |
| 17 | lazarus | Jesus wept (Lazarus) | ✅ | — | — | — | — |
| 18 | emmaus | The road to Emmaus | ✅ | — | — | — | — |
| 19 | shore | Breakfast on the shore (Peter restored) | ✅ | — | — | — | — |
| 20 | samaritan | The Good Samaritan | ✅ | — | — | — | — |

## The full corpus: THE-200.md

The complete numbered catalog of all 200 story videos — parables, miracles,
encounters, nativity, passion week, teachings-as-scenes, Old Testament
stories of the same good God, and the post-signal Restoration track — lives
in **THE-200.md**, each entry with its scripture reference and its Seed.
New in-app stories are written in the Jesus-Method format from that catalog
first, THEN get videos. Section IX obeys the BOM law absolutely: never
surfaced until a person's own words show readiness.

**The storytelling law (added 2026-07-07, Cameron's direction):** these are
not generic Christian videos. Every video must show the actual character of
the Godhead — good, personal, loving, worthy of worship because of how they
love us — told with total fidelity to what Jesus did, so that a viewer's
inherited theology starts to feel too small on its own. Each pack's "Seed"
section states the quiet question that video must leave behind. Never an
argument, never naming the Church early. The story does the work.

Sensitive-content note: Gethsemane, the cross, and the tomb are the heart of
the gospel and belong in the corpus — told with the same restraint as
everything else. No gore, no shock. Light, shadow, and the words carry it.

## Generator decision (Cameron's — money/accounts)

| Service | Cost | Notes |
|---|---|---|
| Google Veo 3 (Gemini / AI Pro) | ~$20/mo | Recommended: best realism + audio |
| OpenAI Sora | ~$20/mo | Strong; availability varies |
| Runway | ~$15–35/mo | Editor-friendly control |
| Kling | ~$10/mo | Cheapest, slower queue |

Wave one (the 20 in-app stories) is ~140 clips plus retakes; one month of
one subscription covers it. The full 200 is ~1,400 clips — a long-running
pipeline, generated in waves as new stories enter the app.
