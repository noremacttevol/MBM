# QC — Row 19, Breakfast on the Shore (John 21:1-17), realistic V2

Worker: Claude worker 13, Machine A `Dev`, 2026-08-01/02.

---

## 0. C-FIX SHIPPED (Machine A `Dev`, 2026-08-07)

> ### ✅ BOTH COMPLAINTS CLOSED IN ONE TOUCH-ONCE RE-CUT — 2026-08-07
> **COMPLAINT LEDGER (Cameron against live `128fc218`, from `v2_outline.py 19`) — now CLOSED:**
> - **(B) PICTURE** *"1:05 picture he is swimming the wrong way."* → **FIXED.**
>   Beat `v2-r019-b17` (`assets/s17-and-swam-for-shore.jpeg`) rerolled ONCE
>   (`--only v2-r019-b17 --redo`). New frame: the boat + disciples sit firmly
>   BEHIND Peter and his face, leading arm and wake all drive TOWARD the
>   foreground beach — he is unmistakably swimming to shore, never toward the
>   boat. Verified in the RENDERED mp4 at t≈65s (`He threw himself into the sea
>   and swam for shore`). CAMERON GATE (b17 `must_not_show`) passes.
> - **(A) AUDIO-pacing** *"JESUS talks too fast and ignores commas."* → **FIXED
>   at source and now BAKED INTO THIS CUT.** `j1` was already re-voiced
>   2.038s → 3.291s (both commas breathe) and `AUDIO_FROM_V1_SEGMENTS = True`.
>   This re-cut rebuilt the track from the 22 V1 segment mp3s (**AUDIO REBUILD
>   PASS** SHA256=`7435cdf735ab74e8c8853301e820795add1a15df2fe58d1c24694842aa0e9629`,
>   159.017s, all 22 segments placed), so the fixed j1 is in the shipped mp4.
>
> ONE re-cut carried BOTH fixes (touch-once law). 1 reroll on a 37-beat row =
> 2.7% (≤15% budget). Captions bottom-band only; end/question card clean; all
> frames realistic (no cartoon/mixed). Shipped + deployed live per step 7c.

## (superseded) RUNNER PARK (C-FIX, Machine A `Dev`, 2026-08-07)

> ### ✅ AUDIO PART (A) IS FIXED — 2026-08-07 (Machine A `Dev`, audio-fix lane)
> Complaint (A) "JESUS talks too fast and ignores commas" is **RESOLVED at the
> source**. `j1` ("Simon, son of Jonas, lovest thou me?") was re-voiced through the
> SAME locked ElevenLabs JESUS voice (Alexander) with ellipsis + `<break>` tags so
> **both commas now breathe**: `media-production/build-19-shore/audio/j1.mp3`
> **2.038s → 3.291s** (sha256 `279c086f…1751c`; timing.json rewritten to the one
> exact-KJV caption span). No dead-air gaps (ellipsis = a natural spoken hesitation,
> NOT the robotic double-ellipsis that got row 10 rejected). Nothing else re-voiced.
>
> Because the new j1 is now newer than the 2026-07-29 V1 final mp4, copying the V1
> AAC stream would ship the OLD rushed j1 (STALE-V1 recency guard correctly refuses
> it), so `AUDIO_FROM_V1_SEGMENTS = True` was set in `beats_v2.py`. Verified: the
> rebuild-from-segments path assembles a **159.017 s** track that matches the
> extract_beats timeline to **0.000 s** (gate ≤0.5 s) with all 22 segments placed.
>
> ### 🛠 REMAINING WORK IS PICTURE-ONLY (B) — for the picture C-FIX lane
> Do **NOT** re-park this to NEEDS-AUDIO — the audio is already correct in the
> source. The ONLY open work is the **one-frame reroll (B)**: beat
> **`v2-r019-b17`** → `assets/s17-and-swam-for-shore.jpeg` (Peter swimming the wrong
> way at 1:05; the beat already carries the CAMERON GATE). In ONE touch-once re-cut:
> reroll b17 until Peter's stroke visibly drives toward the beach, then
> `python3 media-production-v2/v2_assemble.py 19` — the `AUDIO_FROM_V1_SEGMENTS`
> flag automatically rebuilds the track with the fixed j1, so the re-cut closes
> **BOTH** complaints at once. Ship + deploy (step 7c, live-verified); the review
> card answers Cameron in his words: *"too fast / ignores commas"* → j1 now breathes
> at both commas (2.0 s → 3.3 s); *"swimming the wrong way at 1:05"* → Peter drives
> toward the beach. Board is BUILT / Audio OK so this lane owns it (the live cut is
> unchanged, so the complaint still matches the shipped hash and is picked up).

**COMPLAINT LEDGER (open, from `v2_outline.py 19`), Cameron against `128fc218`:**
- **(A) AUDIO-pacing:** *"JESUS talks too fast and ignores commas when asking
  peter if he loves him."*
- **(B) PICTURE:** *"1:05 picture he is swimming the wrong way."*

**Why this row is PARKED, not shipped.** The complaint is MIXED — one audio, one
picture — and complaint (A) is an **AUDIO-pacing** defect. Per RUNNER-LESSONS
("PACING/'too fast'/'rushed' complaints are ALSO audio-domain — park them the same
as a mispronunciation", rows 10/50/51), the fix for (A) is a **re-voice** (slow the
line + force pauses at the commas + regenerate the mp3 + re-assemble), which the
picture-runner is FORBIDDEN to do (audio-immutability; the runner ships
byte-identical audio and AUDIO LOCK is its only proof). The touch-once law says a
row is touched ONCE — every open complaint batched into ONE re-cut. If the runner
fixed only the picture and shipped now, the audio would be unchanged, so complaint
(A) would REPEAT on the very next view — the worst failure this pipeline can make
(exactly the row-46 "put-uth" mistake). So the whole row is PARKED NEEDS-AUDIO and
the picture reroll (B) is deferred into the SAME re-cut that carries the re-voiced
audio. **NO pictures were touched this session; the shipped mp4 is unchanged.**

Not the row-57 ship-exception: board Audio is OK but there is NO paced/pause
override baked in for j1 and NO "verified in final audio" pacing commit — the fix
is not in the mp4, so it must not be shipped over.

**Complaint (A) — the diagnosis.** The voiced question is segment **j1**, JESUS,
KJV John 21:16: *"Simon, son of Jonas, lovest thou me?"* (~1:37 in the cut). The
line has two commas (after "Simon" and after "Jonas") that must breathe; the
shipped ElevenLabs take runs them together and lands too fast to carry weight.
The shipped voice is ElevenLabs (`media-production/build-19-shore/audio/j1.mp3`,
44.1 kHz/128 kbps; JESUS `stability` 0.55 in `mbm_eleven.py`).

**Complaint (B) — the diagnosis (picture, for the eventual re-cut only).** The
"1:05" swim frame is beat **`v2-r019-b17`** → `assets/s17-and-swam-for-shore.jpeg`,
seg `n6 p3`, window **64.80–67.86 s** (exactly 1:05). The shipped take reads as
Peter swimming toward the boat / parallel to shore instead of driving toward the
beach. The beat text ALREADY carries the fix-gate (author-wired): `must_show`
"DIRECTION EXACT: his face, leading arm and wake all drive TOWARD the beach; the
boat is BEHIND his kick, the shore AHEAD of his stroke" and `must_not_show`
"CAMERON GATE (open complaint at 1:05 …): Peter must NEVER appear to swim toward
the boat or parallel to shore; if his stroke does not visibly aim at the beach,
the frame fails." So (B) is a plain reroll of one beat — the runner does it in the
post-re-voice re-cut; do NOT reroll it now (nothing to ship it in).

**AUTHOR / audio-fix lane — exact resume for (A):**
1. Re-voice **j1 only** through ElevenLabs so the two commas land as real pauses
   and the line slows. Simplest proven lever: respell the SPOKEN string for j1
   with pause punctuation, e.g. `SPOKEN`-style override
   `"Simon, son of Jonas, lovest thou me?"` → `"Simon... son of Jonas... lovest
   thou me?"` (ellipses force ElevenLabs to breathe; the CAPTION keeps the exact
   KJV text unchanged — only the spoken string is respelled). If it is still
   rushed, nudge JESUS `stability` up for this segment. Do NOT touch j0a/j0b/j2 or
   any narrator segment.
2. Regenerate ONLY `audio/j1.mp3` via the build's ElevenLabs path, and A/B-listen
   to confirm the commas now breathe and the question no longer rushes.
3. Re-assemble (`python3 media-production-v2/v2_assemble.py 19`) — AUDIO LOCK will
   re-hash the new track; confirm **PASS**.
4. Hand back Ready ✅ / Audio OK. The RUNNER then, in ONE re-cut: rerolls beat
   `v2-r019-b17` until Peter's stroke visibly aims at the beach (complaint B),
   re-assembles over the new audio, ships + deploys (step 7c), and the review card
   answers BOTH complaints in Cameron's words ("too fast / ignores commas" → j1
   now breathes at the commas; "swimming the wrong way at 1:05" → Peter drives
   toward the beach).

~~State flipped BUILT→NEEDS-AUDIO, Audio OK→CHECK on AUTHOR-BOARD row 19.~~
**UPDATE 2026-08-07: (A) fixed by the audio-fix lane (see the green block at the top
of §0). State flipped NEEDS-AUDIO→BUILT, Audio CHECK→OK. Only the picture reroll (B)
remains, and it is owned by the picture C-FIX lane.**

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
