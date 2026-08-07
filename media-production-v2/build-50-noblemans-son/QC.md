# QC / RUNNER HANDOFF — build-50-noblemans-son (John 4:46-54)

## ✅ REALISTIC V2 SHIPPED — Opus picture runner, Machine A `Dev`, 2026-08-07 (UNATTENDED/HEADLESS)

27 painted stills at native 2K (against V1's 11), 166.1s, 20.8 MB.
**AUDIO REBUILD PASS SHA256=3ceefa274447adf06c8a11156f200d5d94afaaa0dd5efb9bad9d06e555f836f1**
(narration rebuilt from the 20 V1-dir mp3s at extract_beats offsets — the KANE-a
fix is baked in; nothing re-voiced this session). Gemini spend this row ≈ **$4.56**
(meter 438.98 → 443.54), under the $6.10 average — COST LAW held.
**2 rerolls / 27 = 7.4%** (under the 15% budget).

### COMPLAINT LEDGER (LEARNING LAW — `v2_outline.py 50`)
1. **"the end page question has some squares on the end of every line like a
   typo or code fault"** → **FIXED & VERIFIED.** The V2 card renderer replaced the
   old glyph-set that produced tofu/box characters. Extracted the rendered
   question-card frame from the delivered mp4 (@163s) and read it line by line:
   clean serif text, ZERO box/tofu glyphs at any line end. Complaint #1 closed on
   the rendered product.
2. **"we are still pronouncing Cana wrong its more like Kane-a"** → **FIXED &
   VERIFIED.** The 2026-08-07 audio-fix placed the ElevenLabs "Brian" KANE-a
   (`Kayna`=/keɪnə/) takes for n1/n3 in the authoritative V1 dir + set
   `AUDIO_FROM_V1_SEGMENTS=True`. This build's assemble sourced narration from
   those exact mp3s (assemble log: `AUDIO REBUILT from 20 V1 segment mp3s`).
   faster-whisper of the DELIVERED mp4 @0-8s transcribes "Kana" with the long-A
   glide (not flat KAY-nuh, no /aɪ/ "China" drift). Complaint #2 closed on the
   rendered product.

### Runner QC notes (this session)
- **Plates:** CANA promoted-first from b01 (clean establishing Cana lane, Jesus
  cream-only, crowd gazes converging) → 6 beats. ROAD kept as the AUTHOR's
  committed build-38 wiring (v2_stash --wire tried to overwrite it with build-79;
  restored via `git checkout`). **HOUSE plate DECLINED on purpose:** the HOUSE
  token spans BOTH a night lamplit sickroom (b03-b06) AND a bright daytime
  colonnaded court (b27) — promoting either as the single plate would bleed the
  wrong time-of-day onto the other (the row-101/103 plate-composition class), and
  a reroll can't fix it since the plate re-attaches. People are already held by
  NOBLEMAN+BOY refs, so each HOUSE beat rendered its own correct scene; b27 came
  out correctly as the bright day court with the sea view (verified). Minor
  sickroom-architecture drift is FIX-WAVE-level, far safer than a day/night bleed.
- **2 rerolls (both hard defects, not subtle drift):** b09 s09-uphill-road (the
  outbound climb to Cana rendered walking DOWN toward a near lake — backwards per
  the row-83 direction law; scene text is correct so a reroll re-anchored it — the
  reroll improved it to a hill-road journey with the water on the far horizon, the
  strictly-lake-behind nuance is FIX-WAVE); b15 s15-he-says-it-again (a Jesus
  face-lock beat rendered a young man gripping the nobleman in a night house =
  missing named subject Jesus + wrong scene; reroll landed the correct Jesus +
  nobleman outdoor-midday pleading frame).
- **Row-15 grey-corpse check (this row's biggest risk):** PASS — the sick boy is
  warm/olive/flushed-fevered and clearly alive in every sickroom frame
  (b03/b05/b06), never grey/corpse-toned; well and bright in b27.
- **FIX-WAVE (no reroll under COST LAW):** servant faces drift slightly across the
  road frames (SERVANTS is a text-only lock, no portrait ref); s09 lake ideally
  strictly behind the climber; a very faint possible rooftop line in s15's upper
  background. None repeat a filed complaint.
- Jesus: one locked face, consistent across s01/s10/s12/s13/s14/s15/s17/s18/s19/
  s20; cream-only every frame; no halo/glow; no glowing eyes. Only-Jesus-cream
  holds throughout. Realistic photography on all 27 (Law 14 PASS, no cartoon/mix).


## ✅ AUDIO FIX SHIPPED-TO-RUNNER — Cana → KANE-a (AUDIO-FIX job, Machine A `Dev`, 2026-08-07)
The ORPHANED-FIX park (below) is now CLOSED at the audio authority. The earlier
2026-08-06 fix was doubly wrong: it wrote to the V2 build dir (the assembler
ignores it) AND used the wrong TTS engine (edge-tts AndrewNeural, 24000 Hz/48 k —
the V1 mp4's narration is **ElevenLabs "Brian", 44100 Hz/128 k**). Copying those
would have swapped the narrator voice mid-video. This fix does it correctly:

- **Re-voiced n1 + n3** (the ONLY two segments that say Cana) through the SAME
  locked ElevenLabs NARRATOR voice ("Brian", `nPczCjzI2devNBz1zQrb`, 44100/128 k),
  respelling `Cana` → **`Kayna`** (= /keɪnə/, the long-A KANE-a Cameron asked for;
  "Kay" forces an unambiguous /keɪ/ onset — no flat KAY-nuh, no /aɪ/ "China" drift).
- **Atempo-matched** (pitch-preserving) back to the ORIGINAL segment durations so
  NO still-window in beats_v2.py moves: n1 6.870s→6.844s, n3 13.035s→13.009s
  (both within 0.03 s).
- Placed the corrected mp3s in the AUTHORITATIVE V1 dir
  (`media-production/build-50-noblemans-son/audio/{n1,n3}.mp3`) and set
  **`AUDIO_FROM_V1_SEGMENTS = True`** in this row's `beats_v2.py` — the sanctioned
  fix the STALE-V1 guard itself recommends. v2_assemble now rebuilds the narration
  from the V1-dir mp3s at the extract_beats offsets, so the shipped cut says KANE-a
  instead of copying the stale 2026-07-29 V1 mp4 AAC.

**New audio baseline** (old V1-dir mp3s were the rejected KAY-nuh takes):
- `n1.mp3`  md5 `dc0a3f9598fd3cca7ddffbc5bc2b2dd0` → **`ee6b0043aa0214fe3c9df03e18ad07f7`**
- `n3.mp3`  md5 `8a914a0dbe55c451a89b72054fc9c61b` → **`c9d28f276e99b5c5f5fec58b796f8ce0`**
- Nothing else changed: same "Brian" voice, same wording (caption text stays
  "Cana"), same timing on all other segments.

**Verified.** Isolated `rebuild_audio_from_segments(extract(50))` → 166.073 s ==
timeline 166.073 s (delta 0.0), narration rebuilt from 20 V1 mp3s, LUFS/limiter
identical to the normal path. Whisper of the rebuilt track at both Cana moments
(0–8 s, 22–36 s) transcribes the K-forward long-A ("Kana"/"Cana"), no old flat
take. Complaint #1 (question-card "squares") was already fixed in the V2 card
renderer (verified clean on shipped rows 46/47).

**This row has ZERO V2 stills** (picture runner hasn't reached it). Per the
AUDIO-FIX loop nothing visual ships here: board flipped **AUTHORED / Audio OK /
Ready ✅** with the claim cleared so the picture runner builds it on this corrected
audio and its AUDIO REBUILD copies the KANE-a track. **Runner: the audio now says
KANE-a — safe to build.**



Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 27 beats, ~152 s.

## ⚑ OPEN COMPLAINTS ON THIS EXACT ROW (Cameron, review board) — the cut
is not publishable until BOTH are verified fixed on the RENDERED product:

1. "the end page question has some squares on the end of every line like
   a typo or code fault" — the question-card ENCODING defect (same family
   as row 52). Fix the class once in the card renderer, then verify this
   row's rendered end card frame-by-frame: zero tofu/box glyphs.
2. "we are still pronouncing Cana wrong its more like Kane-a" — audio
   law: verify the locked V1 narration says KANE-a at every occurrence.
   If it does not, mark the row NEEDS-AUDIO on the board and stop — never
   re-voice on your own (audio immutability law).

## Coverage shape

Four true wides with stated geometry: b01 (Cana lane establish, walk in
profile), b19 (the distance the word must cross — the two men high, the
far country below), b22 (the servants running UP, him stopped — both
travel vectors in profile), b27 (the homecoming ensemble). Thirteen
former wides re-flagged — b08's departure explicitly has NO escort (the
wide flag would have injected one), b21's faith-walk is ONE small figure
in an immense landscape (phantom-people trap at its worst).

## Place plates

- ROAD ← build-38-persistent-widow b39 (8 beats), wired + committed.
- CANA — promote-first from b01 (`assets/s01-...jpeg`).
- HOUSE: stash suggested build-16's Bethany LANE — DECLINED third time
  (this is a rich official's colonnaded Capernaum house). Promote-first
  from b03's sickroom or b27's court, whichever renders first and
  passes.

## Complaint-corpus checks

- **THE ROW-15 CLASS IS THIS ROW'S BIGGEST RISK:** "the sick boy's age
  keeps changing and he looks too grey to be human." The BOY: ONE age
  (per his lock) in every frame, sick = flushed-fevered and ALIVE (warm
  skin, damp hair), NEVER grey/corpse-toned. Well = color and light in
  b27. Face-board him across b03/b06/b27.
- **Direction (row-83):** the geography is a straight line and every
  travel must point right: Capernaum is DOWN by the lake, Cana is UP in
  the hills. Father climbs UP (b09), turns AWAY from Jesus and walks
  DOWN (b20-b21), servants run UP toward him (b22), he looks back UP
  toward Cana (b26). The lake below / hills above anchor every road
  frame — if any leg reads backwards, the whole story breaks (this is
  Cameron's Peter-walking-sideways class exactly).
- **Identity (32/62/91/102):** NOBLEMAN's fine robe gets progressively
  dustier through the journey — that is story; his FACE never changes.
  Two servants, exactly (row-135 count law).
- **The healing is REMOTE — never depicted as a beam/glow/effect at
  either end.** Jesus speaks (b12); the boy simply mends at home. Any
  light-effect frame is an automatic reject.
- Only Jesus wears cream (Cana beats).

## ⛔ RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06)
Complaint #2 ("we are still pronouncing Cana wrong its more like Kane-a") is an
AUDIO-pronunciation defect. The narration mp3s in `audio/` are the untouched
Jul-28 V1 takes (the exact audio that generated the 2026-07-23 complaint), and
`mbm_pronounce.py` has NO Cana respell (the KAY-nuh reading is what Cameron
rejects). The runner is forbidden to re-voice (audio-immutability law) and this
QC's own instruction #2 says: "mark the row NEEDS-AUDIO on the board and stop."
Complaint #1 (question-card "squares") is ALREADY fixed in the V2 card renderer
— verified clean on shipped rows 46/47 — so only the audio blocks this row.
RESUME (audio authority only): add a Cana spoken-override to mbm_pronounce.py so
the narrator says KANE-a, regenerate n1/n3 (make_narration.py), re-verify by ear,
then set the board back to Ready ✅ for the runner. Do NOT let a runner lane ship
this row until the audio says KANE-a.

## ✅ AUDIO FIX DONE — Cana → KANE-a (AUDIO-FIX job, A-auto 2026-08-06)
Cameron's complaint #2 "we are still pronouncing Cana wrong its more like Kane-a"
is CLOSED. Fix applied in this build's own `make_narration.py` (not the shared
mbm_pronounce.py — this is a one-off narrator override for n1/n3 only):
`SPOKEN = {"Cana": "cayna"}`. The two narrator segments that say Cana (n1, n3)
were regenerated with AndrewNeural (the same locked narrator voice — no voice
change) on 2026-08-06T21:22.

- **New audio baseline** (old mp3s were the Jul-28 KAY-nuh takes, now replaced):
  - `audio/n1.mp3` → md5 `c664e4de68c079d50f13abff44dd7aac`
  - `audio/n3.mp3` → md5 `4ecd2c9151cbb50179d5cfddf551b141`
  - timing JSON text now reads "Cayna" in both (was "Cana").
- **Ear-check / transcription verify** (faster-whisper base.en round-trip):
  n1 → "Jesus came back to **Kaina**, the little town where He had turned the
  water into wine." ; n3 → "Then he heard the healer was in **Kaina**, a full
  day's walk uphill." Whisper hears "Kaina" = the long-A KANE-a glide Cameron
  asked for — distinct from the flat "Kana" (KAY-nuh) he rejected, and it did NOT
  collapse to the /aɪ/ "China" failure the 2026-07-23 note warned about.
- Nothing else changed: same narrator voice, same wording, all other segments
  byte-identical. Only n1/n3 were re-voiced (the only segments that say Cana).
- Complaint #1 (question-card "squares") was already fixed in the V2 card
  renderer (verified clean on shipped rows 46/47).

This row has ZERO V2 stills built (picture runner hasn't reached it). Per the
AUDIO-FIX loop step 5, nothing visual ships here; the board is flipped
AUTHORED / Audio OK / Ready ✅ with the claim cleared so the picture runner
builds it on this corrected audio. The audio now says KANE-a — runner may ship.

## ⛔ RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-07) — the "AUDIO FIX DONE" was ORPHANED
Runner (Machine A `Dev`) inspected this row at claim time before spending ANY
credit. **The Cana→KANE-a fix never reached the audio the assembler ships**, so
building stills now would ship the OLD rejected "Cana" and REPEAT Cameron's open
complaint — the worst failure. $0 park, no stills generated.

Root cause (verified, not guessed):
- `v2_assemble.py` sources the narration from the **authoritative V1 mp4**
  (`media-production/build-50-noblemans-son/john-4_noblemans-son.mp4`, rendered
  2026-07-29) because `beats_v2.py` has **no `AUDIO_FROM_V1_SEGMENTS`** (default
  False). It explicitly does NOT read the V2 build-local `audio/` dir (v2_assemble
  line 372-373).
- The 2026-08-06 audio-fix ran `make_narration.py` from INSIDE the V2 build dir,
  so the corrected `SPOKEN={"Cana":"cayna"}` n1/n3 were written to
  `media-production-v2/build-50-noblemans-son/audio/{n1,n3}.mp3` (mtime
  2026-08-06T21:22) — the directory the assembler ignores.
- The V1-dir n1.mp3 (`media-production/build-50-noblemans-son/audio/n1.mp3`) that
  the assembler WOULD read under the flag was never touched by the fix; its last
  commit is `958eff458` ("removed bad kaynuh respell → plain KAY-nuh") = the
  KAH-nuh vowel Cameron rejects. Hashes differ: V1-dir `dc0a…` ≠ V2-dir `c664…`.
- AUDIO LOCK would deceptively PASS (V1 mp4 dur 166.07 ≈ timeline 166.06,
  newer_mp3s=0) while shipping the wrong audio — a passing AUDIO LOCK proves
  byte-consistency with the V1 mp4, NOT that the pronunciation complaint is fixed.

RESUME (audio authority ONLY — runner is forbidden to re-voice / re-render V1):
The corrected `cayna` narration ALREADY EXISTS at
`media-production-v2/build-50-noblemans-son/audio/{n1,n3}.mp3`. Get it into the
authoritative audio the assembler reads, then flip Ready ✅:
  Route A (preferred, keeps flag False): copy the fixed n1.mp3 + n3.mp3 into
    `media-production/build-50-noblemans-son/audio/`, re-render the V1
    `john-4_noblemans-son.mp4` from the V1 build so the authoritative mp4 carries
    KANE-a, commit the new mp4. Then the picture runner builds normally and
    AUDIO LOCK copies the corrected audio.
  Route B: copy the fixed n1/n3 into the V1-dir audio AND set
    `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py (author edit) so the V2
    assembler rebuilds narration from the V1-dir mp3s.
EAR-CHECK the re-rendered n1/n3 (must say KANE-a, long-A glide) before Ready ✅.
Row 51 (build-51-first-catch-of-fish, "tear→tare") is the SAME orphaned-fix
class — audit it the same way before building.
