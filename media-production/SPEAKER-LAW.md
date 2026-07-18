# MBM SPEAKER LAW

**Who is speaking decides the voice AND the caption colour. One declaration, both outcomes.**

Companion to `CAPTION-LAW.md`, which is unchanged and still governs the *look*.
This file governs *who is talking*. Drafted 2026-07-18. **Status: awaiting Cameron's
sign-off on the four voices and three colours — everything else below is decided.**

---

## 1. The five speakers

| Speaker | Caption | Who it is | Voice brief |
|---|---|---|---|
| `NARRATOR` | white | The storyteller. The regular guy. Most of the runtime. | unchanged — `en-US-AndrewNeural` |
| `JESUS` | red `0xEE3322` | **Only** where a red-letter King James Bible actually prints red. | younger than the current voice; put together, slow, calm, collected |
| `GOD` | green `0x5BE38B` | The Father, the Holy Ghost, or the premortal Christ (Jehovah) — including Old Testament passages. | older, deeper, peaceful, angelic, stable |
| `SCRIPTURE` | light blue `0x8FDCFF` | Everyone else quoted from the KJV — Paul, the prophets, the apostles, the people in the stories. One shared voice. | raspier, warm, a believable man |
| `WOMAN` | pink `0xFF9EC7` | Any woman the Bible records speaking. | a good female voice, Old English delivery |

### The hard rule
Everything spoken by anyone other than the white storyteller is **verbatim King
James text a viewer could go look up and find**. Old English, straight from the
KJV. Only the storyteller speaks in modern English.

### The retelling rule
When a scripture line is quoted in Old English by any non-narrator speaker, the
narrator then **retells it in plain modern English** so it lands for a listener
today. This is part of the job, not optional. It is also the single biggest
storytelling upgrade in this pass: the viewer now hears the words as they were
written *and* understands them.

---

## 2. Why so much red becomes green (the doctrinal point)

A red-letter Bible prints red only what Jesus said **in the flesh, in mortality**.
Old Testament passages where Jehovah speaks are not red-lettered — not because
they are not Deity, but because he had not yet come in the flesh.

As Latter-day Saints we understand that the God of the Old Testament *is* Jehovah,
the premortal Christ. Green is how the videos carry that: it is honest to the
red-letter convention a viewer can verify in their own Bible, and honest to the
Restoration's understanding of who was speaking. **Green covering premortal
Jehovah is doctrinally consistent, and Cameron has confirmed it applies across all
200.** It will show up constantly in rows 151–200.

This is milk, not meat: nothing on screen argues the point. The colour simply tells
the truth quietly, and a viewer who later learns who Jehovah was finds the videos
were right all along.

**Current state: 422 beats across the 200 videos are painted Jesus-red.** A large
share of them are God, Paul, the prophets, or people in the stories. Every one gets
re-judged against a red-letter KJV.

---

## 3. The schema

A build declares a speaker **once**, and both the voice and the colour follow.

### Why not just add a colour field
Under the old system the voice lived in `make_narration.py` and the colour lived in
`build.py` as `KJV = {...}`. They drifted: **15 segments are painted Jesus-red while
being spoken in the narrator's voice.** Deriving both from one declaration makes that
class of bug impossible.

### `make_narration.py`

```python
from mbm_speakers import NARRATOR, JESUS, GOD, SCRIPTURE, WOMAN
from mbm_caption_timing import save_speaker_narration

SEGMENTS = [
    ("n1", NARRATOR,  "There was a woman who had been suffering for twelve years."),
    ("j0", JESUS,     "Who touched my clothes?"),
    ("n4", NARRATOR,  "He wanted to know who had reached for him."),
    ("g1", GOD,       "I will make all my goodness pass before thee."),
    ("s1", SCRIPTURE, "For I am persuaded, that neither death, nor life..."),
    ("f1", WOMAN,     "Thy people shall be my people, and thy God my God."),
]

async def main():
    for name, speaker, text in SEGMENTS:
        await save_speaker_narration(text, speaker, f"audio/{name}.mp3")
```

A rare beat that needs its own pacing may pass overrides:
`("j9", JESUS, "It is finished.", "-30%", "-6Hz")`.

### `build.py`

```python
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}
```

`KJV = {...}` and the template-B `caption_style` field are both **retired**.
`caption_filter(seg_id, dur, spoken_end, text, speaker)` takes the speaker.
During migration it still accepts the old boolean, so an un-migrated build renders
exactly as it does today instead of crashing.

### Two build templates exist
- **Template A — 184 builds.** `KJV = {...}` in `build.py`, text from `make_narration.SEGMENTS`.
- **Template B — 16 builds.** A 7-tuple `SEGMENTS` inside `build.py` carrying a per-beat
  `caption_style`, with hardcoded durations and its own local `caption_layers`.
  Builds 02, 07, 08, 09, 10, 12, 13, 14, 17, 18, 22, 26, 28, 31, 34, 37.
  These are converted to template A as part of the pass.

---

## 4. Splitting mixed segments

A segment is the atomic unit of **both** the audio and the caption colour. Some
segments mix speakers inside one block, so no single colour is correct:

> `build-169` — *"And Jesus answering said unto him, Suffer it to be so now: for thus
> it becometh us to fulfil all righteousness. Then he suffered him."*

A red-letter KJV prints only the middle clause red. The other two clauses are
Matthew narrating. That segment becomes three:

```python
("kv15a", SCRIPTURE, "And Jesus answering said unto him,"),
("kv15b", JESUS,     "Suffer it to be so now: for thus it becometh us to fulfil all righteousness."),
("kv15c", SCRIPTURE, "Then he suffered him."),
```

**A split does not change the picture.** Both halves stay on the same still, so
they are consecutive beats over one image — no new artwork is required and the
edit the viewer sees is identical. This is what makes splitting safe to do 200 times.

The reverse also happens: scripture buried inside a narrator beat, spoken in modern
paraphrase. `build-102` narrates *"I am with thee. I will keep thee. I will not
leave thee"* — that is Genesis 28:15, Jehovah speaking, and it should be lifted out
as a `GOD` beat with the narrator retelling it after.

---

## 5. Parables — where red is still right

Inside a parable, the characters' words are **Jesus's** words. A red-letter KJV
prints the whole parable red, including the dialogue Jesus puts in a character's
mouth. So these stay red:

- *"Well done, thou good and faithful servant"* — the lord in the parable of the talents
- *"There was a certain creditor which had two debtors"* — the parable of the two debtors
- *"Then said he unto the dresser of his vineyard..."* — the barren fig tree

The test is never "who is the character?" It is **"does a red-letter King James
Bible print this line in red?"**

---

## 6. Trailing dead air

Measured across all 200 delivered videos (`deadair.json`):

| Trailing silence | Videos |
|---|---|
| over 3.0s — must fix | **186** |
| 1.5–3.0s — in tolerance | 11 |
| 1.5s or less — leave alone | 3 |

Median 4.21s, worst 13.47s. The cause is `CARD_HOLD` (4.2 / 5.0 / 9.2 / 13.0 across
the library) plus `apad` on the audio mix.

**Target: the video ends 1.5s after narration stops. Hard ceiling 3.0s.**
`CARD_HOLD` stops being a hand-set constant and becomes computed: hold the card
long enough to read it, then end 1.5s after the last spoken word. The closing card
stays — it is intentional. Never clip the last word or the 0.8s fade-out.

---

## 7. Pronunciation

Fixed through the `SPOKEN` respelling dict. **The caption always keeps the true
spelling — only the spoken text changes.**

- **homographs** — bow, wound, wind, tears, lead, sow, live(s), read, close, use(d), minute, bass, does, desert, content
- **archaic KJV verbs** — forsaketh, spake, wist, durst, verily, sheweth, hearkened
- **proper nouns** — Gennesaret, Bartimaeus, Zacchaeus, Iscariot, Capernaum, Gethsemane, Melchizedek, Nebuchadnezzar, Zarephath, Abednego

Existing respellings are themselves audited — some are wrong (#30's "uhs" was read
as "Oz"; #41's "forsaketh" came out "for-Saccath"). **Verified by transcribing the
rendered audio with `faster_whisper`, never by assuming.**

---

## 8. What must not change

The caption *look* is finished. Untouched by this pass:

- Jost Bold, the flat-cross "t"
- the adaptive bottom band sized to the text (max 3 lines), `black@0.5`
- every line individually centred, 56px side margins
- 1080×1920 zoom-crop framing
- captions anchored to real edge-tts per-sentence timestamps (`.timing.json` sidecars),
  contiguous and non-overlapping
- **the artwork — all existing stills stay**

The only caption change is the colour, driven by who is speaking.

---

## 9. Sign-off

- [ ] Jesus voice
- [ ] God voice
- [ ] Scripture voice
- [ ] Woman voice
- [ ] green / light blue / pink hex

Audition page: `SPEAKER-LAW/audition.html`
