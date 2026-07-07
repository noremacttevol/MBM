# MBM Story Videos — Master Production Plan

Goal: a cinematic video for every story in the app's opening-story bank (20
today), plus a backlog of further gospel stories, so people can SEE Jesus's
way of treating people — not just read it. Videos play where the text story
plays today; the text remains the offline fallback (local-first law holds).

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
   illustrates them; it never rewrites them.

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

- Vertical 1080×1920, 30fps, 60–90 seconds.
- Narration: one warm, low, unhurried voice across all 20 (Descript AI voice,
  or Cameron's voice — audition both on video #1).
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
| 03 | zacchaeus | Zacchaeus | ✅ | — | — | — | — |
| 04 | nicodemus | Nicodemus at night | ✅ | — | — | — | — |
| 05 | bent_woman | The bent-over woman | ✅ | — | — | — | — |
| 06 | two_sons | The two sons | ✅ | — | — | — | — |
| 07 | peter_water | Peter walks on water | ✅ | — | — | — | — |
| 08 | lost_coin | The lost coin | ✅ | — | — | — | — |
| 09 | rich_ruler | The rich young ruler | ✅ | — | — | — | — |
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

## Backlog — gospel stories beyond the current 20

For future story-bank expansions (each would first be written as an in-app
story in the Jesus-Method format — story, question, choices including the
believer's testimony option — THEN get a video, same pipeline):

- The woman taken in adultery — "Neither do I condemn thee" (John 8)
- Feeding the five thousand (John 6)
- "Let the children come to me" (Mark 10)
- The widow's mite (Mark 12)
- Doubting Thomas — "Blessed are they that have not seen" (John 20)
- The washing of the disciples' feet (John 13)
- The widow of Nain — he raised her son because he saw HER (Luke 7)
- The woman who washed his feet with her tears (Luke 7)
- The lost sheep — leaving the ninety-nine (Luke 15)
- The wedding at Cana — his first miracle was saving a family's joy (John 2)
- Gethsemane — "not my will, but thine" (Luke 22)
- The thief on the cross — "today… in paradise" (Luke 23)
- Mary Magdalene at the tomb — he said her name (John 20)
- The sower (Matthew 13)
- The unmerciful servant — forgiven much, forgiving little (Matthew 18)
- Workers in the vineyard — the generous landowner (Matthew 20)

Sensitive-content note: Gethsemane, the cross, and the tomb are the heart of
the gospel and belong in the app — but they are told with the same restraint
as everything else. No gore, no shock. Light, shadow, and the words carry it.

## Generator decision (Cameron's — money/accounts)

| Service | Cost | Notes |
|---|---|---|
| Google Veo 3 (Gemini / AI Pro) | ~$20/mo | Recommended: best realism + audio |
| OpenAI Sora | ~$20/mo | Strong; availability varies |
| Runway | ~$15–35/mo | Editor-friendly control |
| Kling | ~$10/mo | Cheapest, slower queue |

~140 clips total for all 20 stories plus retakes; one month of one
subscription should cover it.
