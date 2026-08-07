# QC — Row 18, The Road to Emmaus (Luke 24:13-35), realistic V2

Worker: Claude worker 12, Machine A `Dev`, 2026-08-01.

---

## 0. ✅ AUDIO-FIX RESOLVED + SHIPPED (Machine A `Dev`, Fable-5 author lane, 2026-08-07)

**COMPLAINT LEDGER (from `v2_outline.py 18`):**
- Cameron (2026-08-05, against `e0e3e726`): **"You mispronounced Jesus's."**
  → **FIXED in the shipped cut.** n0 re-voiced through the SAME ElevenLabs "Brian"
  narrator so the possessive is now pronounced /JEE-zus-iz/. See below.

**Root cause (the park note above had it half-wrong — corrected here).** The
shipped narration is **ElevenLabs** (44.1 kHz, `VOICE_ELEVEN` "Brian" narrator),
NOT edge-tts — `make_narration.py` in this build is the stale edge-tts scaffold
and does NOT generate the audio that actually ships. So the park's "set
`SPOKEN={"Jesus's":"jeezusiz"}` and run `make_narration.py`" would have re-voiced
n0 in a DIFFERENT engine (edge-tts AndrewNeural, 24 kHz) and swapped the narrator
voice at the very opening of the video — a new defect. faster-whisper confirmed
the actual defect: the ElevenLabs take said "two of **Jesus'** followers" — it
dropped the possessive "-iz" ending (the word spanned only 0.20 s), so it read as
"Jesus followers".

**The fix (reproducible: `build-18-emmaus/revoice_n0.py`, $0 image / a few cents
ElevenLabs).**
1. Re-rendered ONLY n0 through the SAME ElevenLabs narrator (`render_segment`,
   VOICE_ELEVEN[NARRATOR] "Brian" `nPczCjzI2devNBz1zQrb`) from a spoken string with
   the possessive respelled `Jesus's` → **`Jesuses`**, which ElevenLabs voices as
   /JEE-zus-iz/. The on-screen CAPTION is untouched — it comes from
   `make_narration.py` SEGMENTS (extract_beats reads s[2]), which still says
   "Jesus's", so caption and audio stay independent (no `TEXT_OVERRIDES` needed).
2. **Pitch-preserving atempo-matched** the new take back to the original n0
   duration (18.52 s raw → atempo 0.9453 → 19.566 s vs original 19.592 s, Δ −0.026 s)
   so **NO downstream still-window in `beats_v2.py` had to move** — the whole 243.3 s
   timeline stays structurally identical and every already-verified contiguous
   window stays valid. n0.timing.json rescaled to match.
3. Set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py` (the rebuilt audio now
   legitimately differs from the pre-fix V1 mp4), re-assembled — **AUDIO REBUILD
   PASS SHA256 `3592466846055ce4`**, 243.3 s / 21.4 MB, `--check` PASS.

**Verified in the DELIVERED mp4** (not just the segment): the possessive word now
onsets at n0-local **5.20 s** (the new take) vs the old take's **5.62 s** — a 0.42 s
shift no measurement jitter can explain — and its acoustic span roughly tripled
(0.20 s → ~0.5 s), i.e. the "-iz" syllable is now voiced. Old take preserved at
`audio/n0.mp3.eleven-orig-2026-08-07`.

Board flipped NEEDS-AUDIO→BUILT, Audio CHECK→OK. Shipped: review card 🛠 flag
answers Cameron's complaint in his words; deployed to the reviewer + live-verified.

---

## 1. Audio is LOCKED and was never touched

All 18 narration segments in `media-production/build-18-emmaus/audio/` are
44.1 kHz / 128 kbps — ElevenLabs' format (edge-tts writes 24 kHz mono / 48 kbps),
so this row already carries the current voices and REDO-ALL is satisfied without
re-voicing. Nothing was re-rendered, re-timed, gained or re-encoded. The V1 folder
holds exactly ONE mp4, so `v2_assemble.py`'s AUDIO LOCK had no backup file to work
around.

## 2. The inherited beat map was wrong, and that is the expensive lesson again

`beats_v2.py` was scaffolded on 2026-07-29 with 38 beats and good scene prose, but
its windows ran on a **219.5 s** timeline against the real **232.62 s** — adrift by
up to 13 s at the end. VERIFY THE ARTEFACT, NEVER THE PROSE: every window was
recomputed from the fixed `extract_beats.py` plus each segment's own
`audio/*.timing.json` phrase boundaries, then audited for contiguity.

Result: 41 windows, contiguous from 0.28 s to the card at 232.62 s, **zero gaps and
zero overlaps**, average 5.7 s per picture, longest hold 9.6 s.

Three NEW beats were authored where the inherited map left one picture sitting over
too much narration:

| new beat | segment | closes |
|---|---|---|
| `b02b` | n0 p3b | "the arrest, the cross, the end of everything they had hoped for" |
| `b31b` | n8 p3 | "he had been with them the entire way, and they had almost missed him" |
| `b39` | n10 p5 | the closing line, "still in the habit of walking with the ones who have lost hope" |

## 3. Staging decision this story forces

Luke 24:16 — "their eyes were holden that they should not know him." The build takes
the honest reading rather than disguising him: **Jesus looks exactly like himself in
every frame**, locked face, cream robe, no hood and no shadowed face. The failure is
put entirely on the two disciples, who look straight at him and do not see. The gap
between what the viewer sees and what the two see is the whole first half.

The vanishing (v31) is shown as AFTERMATH only — an empty stool, his untouched cup,
the bread in their hands. No fade, no transparency, no light, no effect.

## 4. Defects found and fixed — and where each fix was put

Fixes went into the **shared locks** wherever the defect could recur, per the row-16
lesson, rather than into one beat's prose.

1. **Anachronistic Jerusalem skyline.** The first `s01` came back with a minaret, a
   church campanile and red pitched tile roofs — row 16's Dome-of-the-Rock family.
   Fixed by a new `JERUSALEM` lock naming the AD 33 city positively: dressed
   limestone walls, square crenellated towers, flat roofs, the Second Temple
   highest, and no minaret/steeple/spire/dome/tile roof anywhere.

2. **Direction of travel reversed.** `s01` and `s03` put the walled city at the END
   of the road in front of the men, so the picture read as walking TO Jerusalem when
   the story is walking away from it. Fixed by a new `OUTBOUND` lock — "the road
   ahead ends in empty hills, not in a city" — attached to all 15 outbound beats.

3. **My own scene text contradicted the shared lock.** The b01 geometry sentence said
   the men's backs faced "the camera and Jerusalem", which puts the city where the
   lens is; the model resolved the contradiction by moving the city in front of them.
   Rewritten to an elevated side vantage where backs-to-camera and
   city-behind-them are both true. b08 had the same conflict and got a roadside
   profile vantage. **A beat's own scene text must not contradict the shared locks.**

4. **Companion identity drift.** He rendered as a beardless youth in s06/s08/s09.
   Root cause: both image anchors (`s01`, `s03`) show him only from BEHIND, so no
   anchor carried his face. Fixed by writing the invariant into the lock ("a grown
   man of about thirty with a full thick dark beard — never a beardless youth, never
   clean-shaven") AND swapping the anchor to `s04`, which shows both disciples'
   faces clearly.

5. **Camera-to-back geometry missing on every wide beat.** The inherited map predated
   the 2026-08-01 hardening; `--check` flagged all 22 wide beats. Each got its own
   camera-position sentence — the row-14 fix that took 5 of 9 rerolls to zero.

6. **Advancing into the lens / staring down the lens.** b02 and b16 came back as men
   walking into the camera and b13 as Jesus with his pupils on the lens. Fixed by
   naming the geometry (camera behind, subjects walking away, head turned off the
   camera axis with the eyeline exiting a named edge).

## 5. Standing laws checked on every accepted frame

- Jesus: JESUS-V2-REF attached and LOCK v5 byte-identical on every Jesus beat; one
  cream robe and **only he wears cream**; no halo, glow or rim-light anywhere.
- Time of day follows the story's own clock: afternoon road → sunset at Emmaus →
  lamplit interior → night run back to Jerusalem.
- Interiors are lit ONLY by clay saucer oil lamps and the doorway's dusk — no glass
  chimney, no metal lantern, no hanging fixture (the row-16 interior trap).
- Content-care GREEN: the crucifixion is referred to but never depicted.
- Every figure's action reads correctly at a glance; no extra bodies at frame edges.
