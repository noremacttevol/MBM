# QC — Row 19, Breakfast on the Shore (John 21:1-17), realistic V2

Worker: Claude worker 13, Machine A `Dev`, 2026-08-01/02.

---

## 1. Audio is LOCKED and was never touched

The authoritative narration is `media-production/build-19-shore/audio/` — 22 segments,
all 44.1 kHz / 128 kbps, which is ElevenLabs' format (edge-tts writes 24 kHz mono /
48 kbps), so this row already carries the current voices and REDO-ALL is satisfied
without re-voicing. `v2_assemble.py` copied V1's AAC stream packet-for-packet:
**AUDIO LOCK PASS, SHA256 e88bb8af…**, and the delivered cut is 156.967 s — the same
duration as the V1 mp4 to the millisecond.

**Trap found here, worth recording:** the copy of `make_narration.py` and the copy of
`audio/` sitting in the *V2* folder are STALE (2026-07-28) and differ from the V1
folder's (2026-07-29). The stale script is missing the retellings that were added so
no KJV line lands unexplained — n5b's "Have you caught anything, he called", n5c's
"Put the net over the right side, he told them", n11's "Only: do you love me" and
n12's "yes, Lord, you know that I love you". Every one of those is spoken in the
shipped audio. A beat map written against the V2 folder's script would have been
wrong about four segments. VERIFY THE ARTEFACT: `extract_beats.py` reads the V1 build,
and so did I.

## 2. The inherited beat map was wrong, again

`beats_v2.py` had been scaffolded with 27 beats on a **136.1 s** timeline against the
real **157.76 s** (the story ends and the card starts at 149.583 s) — adrift by more
than 13 s by the end. It also named a `PETER` and a `JOHN` lock the build never
defined. Every window was recomputed from the fixed `extract_beats.py` plus each
segment's own `audio/*.timing.json` phrase boundaries.

Result: **37 windows, contiguous 0.28 s → 149.583 s, zero gaps and zero overlaps**,
4.0 s per picture (V1 had 16 pictures for the whole story). Verified against
`silencedetect` on the delivered file: every speech start/stop in the audio lands
inside the window that was written for it.

## 3. The setting is where the money went, and the fixes went into shared locks

Row 19 is the first V2 build whose second half is an open boat, a shore and a
charcoal fire, and it produced exactly the first-time defects that predicts. Reroll
rate **32 % (12 of 37**, one beat twice**)**:

| defect | beats | fix, and where it was put |
|---|---|---|
| Modern dressing-gown / bathrobe silhouette on a robe | b08 | **New shared GARMENT-CONSTRUCTION clause in `v2_prompt.py`** — garments are straight woven rectangles; no shawl collar, lapel, placket, cuff or bow-tied sash |
| Manufactured objects invented for a new setting (a modern circular cast net with moulded floats, a stray white shoe) | b12 | **New shared PERIOD-MATERIALS lock in `v2_prompt.py`**, stated positively (wood, flax, clay, forged iron, hand-woven wool), plus a DRAG-NET clause in the build's NET lock |
| Peter drifting into a grey-haired old man in the wide and middle-distance frames | b14, b28, b31 | **New `PETER-HOLD` age-and-hair invariant**, attached to every beat in the build that names Peter. The CAST-V2 sheet alone does not hold him when he is small in frame |
| Faces rendered as light SOURCES (two figures with burning red faces in the dark) | b03 | Written into the build's COURTYARD lock: a face receives light and never emits it |
| Cream/off-white on someone other than Jesus | b24 | CREW lock added to that beat and the inventory stated positively in its scene text |
| Subject's pupils on the lens | b02, b27 (twice) | Geometry, not prohibition. b27 only cured on the second pass, when the camera was moved to an over-the-shoulder position so Peter's out-of-focus shoulder gives the gaze a target inside the frame |
| Unexplained arm/body at a frame edge | b01 | The lamp was named as standing on the table by itself, and Peter named as the only person in the picture |
| Action reversed: Peter throwing his coat AWAY as he jumps | b16 | John 21:7 has him putting it ON. Stated as the affirmative action, with the tunic underneath so nothing is exposed |

## 4. Standing laws checked on every accepted frame

- Jesus: JESUS-V2-REF attached and LOCK v5 byte-identical on all 15 Jesus beats; one
  cream robe and **only he wears cream**; no halo, glow or rim-light anywhere; he is
  dry on the shore because he was never in the water.
- John 21:4 is staged honestly: he is never hooded, shadowed or disguised. The
  disciples' failure to know him is done by DISTANCE (b07) and by their own faces.
- Time of day follows the story's own clock: lamplit interior → courtyard night →
  black water → flat grey first light → the sun clearing the eastern hills. No midday
  and no sunset palette anywhere.
- The charcoal fire is a bed of embers on stone, not a camp fire, and the courtyard
  brazier is deliberately the same bed of coals so the John 18:18 / John 21:9 rhyme is
  visible.
- Content-care GREEN: the denial is shown only as Peter's face and grief; v7's "he was
  naked" is a working tunic and a coat being pulled on.
- Captions checked on rendered frames from the delivered mp4: bottom band only, white
  narrator, red Jesus KJV, light-blue Peter's scripture, and the closing question card
  carries its words.

## 5. Spend

$4.96 first pass (37) + $1.47 rerolls (11) + $0.13 second reroll of b27 = **$6.56**.
One generator process at a time, every run under a hard `--ceiling` recomputed from
the live meter; meter went $74.50 → $81.07 with zero duplicate billing.

## OPEN CAMERON COMPLAINT — gate before rebuild (visual half)

"1:05 picture he is swimming the wrong way" → beat v2-r019-b17.
Peter's face, leading arm and wake all drive TOWARD the beach; the
boat is BEHIND his kick. If his stroke reads as aiming at the boat
or parallel to shore, reject. (The same complaint's audio half —
Jesus reading the Feed-my-sheep questions too fast through commas —
is an AUDIO-pipeline item, logged for the audio pass; do not
assemble a new cut that keeps the rushed line unfixed.)
