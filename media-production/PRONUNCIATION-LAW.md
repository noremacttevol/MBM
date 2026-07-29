# MBM PRONUNCIATION LAW — making edge-tts read King James English

**How to get the narration voices to say Old English correctly, and how to KNOW they did.**
Written 2026-07-18 from measured tests, not guesses. Every claim below was verified by
rendering the audio and transcribing it back.

---

## 1. The mechanism

Each build's `make_narration.py` has a `SPOKEN` dict. It overrides what the TTS *says*
without touching what the viewer *reads*:

```python
SPOKEN = {
    "j1": "full respelled text for segment j1",   # whole-segment override
    "bow": "boh",                                  # single-word respelling
}
```

**The caption always keeps the true King James spelling. Only the spoken text changes.**
A viewer must be able to look the verse up and find it word for word.

---

## 2. The ear: `check_pronunciation.py`

You cannot hear a mispronunciation by reading text. Close the loop — render it, transcribe
it back, compare:

```bash
# one line
python3 media-production/check_pronunciation.py \
    --text "He that forsaketh not all that he hath cannot be my disciple"

# test a candidate respelling BEFORE committing it
python3 media-production/check_pronunciation.py \
    --text "he that forsaketh not" --spoken "he that forsayketh not"

# a whole build (uses its SEGMENTS + SPOKEN)
python3 media-production/check_pronunciation.py --build build-41-counting-the-cost
```

Uses `faster-whisper` (plain `whisper` is broken on this box — NumPy/numba conflict).
Output is ranked: `!!` = sound differs a lot (likely real), `~` = probably just spelling.

---

## 3. THE THREE TRAPS — read before you "fix" anything

### Trap 1: the transcriber normalizes archaic words
`hath`, `saith`, `doth` come back as **"has"**, **"said"**, **"does"** *no matter what you
feed the TTS.* I fed it `hasth`, `seth`, `duhth` — still "has", "said", "does". The audio
was fine; whisper was modernizing it.

**Do not chase these.** A flagged `hath`/`saith`/`doth`/`spake`/`shew` is almost never a
real defect. Confirm with a human ear before touching it.

### Trap 2: respelling frequently makes it WORSE
Measured, same session:

| tried | came out as |
|---|---|
| `sore` → `sore-ly` | "sorrel while" |
| `raiment` → `rayamint` | "rear mint" |
| `forsaketh` → `for-SAY-keth` | "for Seyketh" |

**Hyphens split a word into two.** `for-SAY-keth` became "for Seyketh". Never put hyphens
or ALL-CAPS stress marks in a respelling — write one continuous lowercase word.
This trap already shipped bugs: #30's `uhs` was read as **"Oz"**, and #41's original
`forsaketh` came out **"for Saccath"**.

**Rule: never commit a respelling you have not A/B tested.** Original vs candidate, both
through the checker. If the candidate isn't clearly better, keep the original.

### Trap 3: word-boundary/liaison errors score 100% and hide
`straightway he arose` → **"heroes"**. The sounds are identical, so every similarity score
says perfect. These are invisible to scoring and only show up by *reading the transcript*.
Neither a comma nor a period fixed it in testing — it needs rephrasing or a deliberate
pause in the segment split.

Watch for: `he arose` → heroes, `of us` → Oz, `to him` → Tim, `in treat` / `Intreat`.

---

## 4. Verified findings

Confirmed REAL misreads (fix these):

| word | heard as | working fix |
|---|---|---|
| `forsaketh` | "for sakith" / "for Saccath" | `forsayketh` (no hyphens) |
| `wist` | "wished" | needs work — `wihst` gave "waste" |
| `whither` | "with a" | needs work |
| `peradventure` | "hair adventure" | `purradventure` → "per adventure" ✓ |
| `sheweth` | "should with" | `showeth` ✓ |
| `live` (verb) | "lyve" | `liv` ✓ (already used across builds) |
| `bow` (verb) | "bau" | `boh` ✓ |
| `overcometh` | — | `overcuhmuhth` ✓ |
| `Intreat` | — | `in treat` ✓ |
| `ought` | — | `awt` ✓ |

Verified FINE, leave alone: `verily`, `blessed`, `beloved`, `sepulchre`, `meek`,
`durst` ("derst" is correct), `brethren`, `unto`, `thee/thou/thy`.

Ambiguous — human ear required: `hath`, `saith`, `doth`, `raiment`, `sore`.

---

## 5. Word classes to screen in every new script

- **homographs**: bow, wound, wind, tears, lead, sow, live(s), read, close, use(d),
  minute, bass, does, desert, content, row, entrance
- **archaic verbs**: forsaketh, spake, wist, durst, sheweth, hearkened, girded, wroth
- **`-ed` as its own syllable**: blessed, learned, beloved, cursed (BLESS-ed vs blest)
- **proper nouns**: Gennesaret, Bartimaeus, Zacchaeus, Iscariot, Capernaum, Gethsemane,
  Melchizedek, Nebuchadnezzar, Zarephath, Abednego, Areopagus, Philippi

---

## 6. The safe workflow

1. Write the segment with the **verbatim KJV text**.
2. Run the checker on the build.
3. For each `!!`, **listen** — or at minimum read the transcript and judge by sound, not
   spelling. Rule out Trap 1 before doing anything.
4. Only if it's a real misread: draft a respelling, **A/B test it**, keep it only if it's
   clearly better.
5. Read the transcript line for liaison errors (Trap 3) — scores will not catch them.
6. Re-render, then re-check the final mixed audio.

**When in doubt, leave the real word alone.** A slightly odd reading of the true word beats
a confident mispronunciation of a made-up one. Cameron hears these on headphones.

---
**Tags:** #captions #narration #tts #kjv
