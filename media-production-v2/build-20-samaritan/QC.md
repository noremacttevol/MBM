# QC — Row 20, The Good Samaritan (Luke 10:25-37), realistic V2

Worker: Claude worker 14, Machine A `Dev`, 2026-08-02.

---

## 1. Audio is LOCKED and was never touched

The authoritative narration is `media-production/build-20-samaritan/audio/` — 22 segments.
`v2_assemble.py` copied V1's AAC stream packet-for-packet: **AUDIO LOCK PASS, SHA256
d3fe79df…**, delivered 186.665 s / 21.5 MB against the V1 mp4's identical duration.
Nothing was re-voiced.

**The V2 folder's copy of `audio/` is STALE and was ignored** (dated 2026-07-28 against
the V1 folder's 2026-07-29; its `n12.mp3` is a byte-for-byte duplicate of `card.mp3`).
`extract_beats.py` reads the V1 build, and so did I.

## 2. THE TRAP ON THIS ROW: the V1 narration SCRIPT is stale, but the AUDIO is not

`media-production/build-20-samaritan/make_narration.py` was rewritten
**programmatically after the voices were cut** — its string quoting flipped from `"` to
`'` throughout — and the rewrite **stripped the plain-English retellings out of four
segments**. `make_narration.py.pre-echo` is the version that matches the audio.

`v2_assemble.py` draws caption text from that script, so the stale text would have
printed words nobody says over four segments *and* thrown their caption timing off,
because `timed_windows` matches the caption text character-by-character against the
timing sidecar. Verified with faster-whisper on the real mp3s:

| seg | what the stale script says | what the audio actually says |
|---|---|---|
| n1b | opens "Jesus turned it straight back on him" | opens **"Teacher, what must I do to inherit eternal life?"** |
| n12 | opens "He did not just help and move on" | opens **"And whatever more it costs, when I come back, I will repay you myself."** |
| n14 | "could not bring himself to name the Samaritan… a category to define" | **"could not even say the word Samaritan. He answered, the one who showed mercy. Jesus had flipped the whole question…"** |
| n15 | "The lesson ends in motion, not admiration…" | **"Stop asking who you are allowed to walk past. Go, and be the neighbor…"** |

**Fix put in the SHARED tool, not this build's prose:** `v2_assemble.py` now honours a
build-declared `TEXT_OVERRIDES = {seg: text}`. V1 is never edited (V2-KICKOFF hard
protection #1). The mechanism is opt-in, so no other row's behaviour changes. All four
overrides were confirmed firing in the assembly log and confirmed on rendered frames.

**Lesson for every later row: a `.pre-echo` / `.pre-speaker` sibling that DISAGREES
with the live script is a signal to transcribe the mp3s before trusting either file.**

## 3. The inherited beat map was wrong, again

`beats_v2.py` had been scaffolded with 30 beats ending at **172.63 s** against the real
**180.035 s** card start, adrift from the very first beat (its b01 ended at 4.46 s
against the real 4.997 s) and growing all the way down. Its last beat held ONE picture
over 21.6 s of narration. It also carried no `must_show` / `must_not_show`, so it could
never have passed `--check`.

Every window was recomputed from the fixed `extract_beats.py` reading the V1 build, then
split on each segment's own `audio/*.timing.json` phrase boundaries.

Result: **42 windows, contiguous 0.28 s → 180.035 s, zero gaps and zero overlaps**,
4.28 s per picture, longest 6.76 s (V1 had EIGHT pictures for the whole 3-minute story,
one of them on screen for 22 s). Verified programmatically: all 22 segments' speech
starts land inside the window written for them.

## 4. Anchor-first casting, and the rerolls

Six face-showing beats were generated FIRST as identity anchors (b02 lawyer, b11
traveller, b15 priest, b16 Levite, b24 Samaritan, b29 innkeeper) and then wired into
`REFS`, so every later frame naming that lock got the image attached. Reroll rate
**12 % (5 of 42)** — well under row 19's 32 % and row 16's 49 %, which is the anchor-first
order paying for itself.

| defect | beat | fix |
|---|---|---|
| The Samaritan rendered as a **grey-bearded old man** | b29 | The row-19 `PETER-HOLD` family exactly. Root cause: `v2_gen_api` builds its REFS cache once at the start of a run, so during the anchor pass the Samaritan anchor did not yet exist on disk. Rerolled after the anchor landed — fixed in one pass. **Generate anchors in their own run, then start a second run for everything else.** |
| A bright **cream head-cloth** in the near foreground of the crowd | b08 | Stated positively: every head-cloth, shawl, tunic and mantle in the frame — *including the large out-of-focus ones and the ones cut off by the edges* — is a named saturated earth colour |
| A **metal pin buckle** on the priest's sandal | b18 | The sandal named affirmatively as a flat leather sole with plain thongs and a knotted ankle lace, knot and lace-tail visible |
| Pale **moulded shoe soles** | b25 | Soles named as bare brown skin or flat dark undyed leather. Second render came back as dust-whitened leather sandals with visible toe-thongs — accepted; dust on a limestone road is not a defect |
| Jesus's **pupils on the lens** in a tight portrait | b38 | Geometry, not prohibition, and the row-19 cure: rebuilt as an over-the-shoulder two-shot so his gaze has a target *inside* the frame. Fixed in one pass |

## 5. Standing laws checked on every accepted frame

- Jesus: JESUS-V2-REF attached and LOCK v5 byte-identical on all 11 Jesus beats; one
  cream robe and **only he wears cream**; no halo, glow or rim-light anywhere.
- Time of day is the story's own clock: one continuous warm late afternoon for the whole
  frame story (b01-b10, b21, b23, b34-b41); hard vertical white glare on the Jericho
  road; amber low light as they walk to the inn; one clay lamp at night; thin level light
  at dawn; warm low light on the empty road at the close. No sunset palette anywhere.
- Luke 10:30's "went DOWN" is on screen: every travel frame in the parable descends.
- v31/v32 staged so the crossing is visible — the road's full width lies empty between
  the man in the dust and the priest and Levite on the far edge; b19 makes that distance
  the subject of the picture.
- v34 shows both stated remedies (clay oil flask + goatskin wineskin) and the Samaritan
  ON FOOT beside the loaded donkey.
- v35's "two pence" is **exactly two countable coins**, separated on the palm, hand-struck
  and unmilled — COUNT-AS-GEOMETRY held.
- Content-care AMBER, handled: the robbery is before-and-after only (b13 men coming off
  the rocks, b14 the aftermath). No blow lands on camera, no blade touches a body, no
  pooled blood, and the stripped man keeps his torn knee-length undertunic in every frame.
- Captions checked on rendered frames from the delivered mp4: bottom band only, white
  narrator, red Jesus-voice KJV, light-blue scripture, and the closing question card
  carries its words.

## 6. Spend

$0.80 anchors (6) + $0.13 b29 reroll + $4.82 main pass (36) + $0.54 rerolls (4) =
**$6.30** for 42 keepers. One generator process at a time, every run under a hard
`--ceiling` recomputed from the live meter; meter went $81.07 → $87.37 with zero
duplicate billing.
