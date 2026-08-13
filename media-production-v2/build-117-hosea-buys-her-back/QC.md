# QC / RUNNER HANDOFF — build-117-hosea-buys-her-back (Hosea 1-3)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 38 beats, ~215 s.

## COMPLAINT LEDGER
- **CLOSED 2026-08-13 (AUDIO):** Cameron — *"it was all good until the very
  end where you miss pronounced 'Dramatized' — fix that audio at the very end
  and its good."* → FIXED: the closing question card's first word "dramatized"
  was mispronounced (Brian's natural read rose into the 2nd syllable =
  "druh-MAT-ized"). Re-voiced the card ONLY through ElevenLabs Brian with the
  spoken respell "DRAMatized" (caption spelling unchanged), picked the best of
  6 takes by front-stress energy+pitch (falling contour 124→108 Hz vs the
  original's rising 112→121 Hz), atempo-locked to the original card duration so
  NO downstream still-window moved. Verified on the SHIPPED mp4 at ~3:35 (215.4s):
  now reads "God DRAM-uh-tized …", front-stressed (e_front 0.192 > e_back 0.157).
  Nothing else in the audio changed.

## AUDIO-FIX SHIPPED (2026-08-13, Machine A `Dev`, audio lane)
- File re-voiced: `media-production/build-117-hosea-buys-her-back/audio/card.mp3`
  (V1 dir — AUDIO_FROM_V1_SEGMENTS=True ships from here; V2-dir copy updated too).
- Audio baseline: **card.mp3 md5 03f3d9e4 → 9e9cc0d6**; full mp4
  **SHA256 358dd0f3…** (AUDIO REBUILD PASS, 229.746s, 20.8 MB). ElevenLabs Brian,
  44100 Hz / 128 k — same voice, same wording, same timing outside the card.
- Cost: $0 Gemini, ~10 short ElevenLabs card takes (candidate + robustness +
  6-take batch), 0 image reroll. 38 stills UNCHANGED (no picture re-cut —
  complaint-first / touch-once).

## RUNNER RESUME (2026-08-09, Machine A `Dev`, Opus runner)
Previous autopilot lane DIED after generating all 38 frames, before assembly.
Already-shipped check: NO committed mp4, v117 card still old newvoice (no
`realistic-v2`) → NOT shipped, resumed. No live sibling `v2_gen_api`.
`v2_prompt.py --check` PASS, `v2_gen_api --dry-run` = 0 shots / $0.00 (all 38
frames present, none sub-2K) → generation complete, $0 spent this session.
Resumed at: Light QC → assemble → ship.

## CONTENT-CARE — this story is about unfaithfulness, rendered clean

- Gomer's fall is told by GEOGRAPHY and LIGHT, never by depiction:
  warm home → grey road → cold glittering horizon → flat-noon market
  → the worn stone step at its unswept edge. NOTHING suggestive is
  ever framed — no clients, no touching strangers, nothing of the
  trade itself. The "step where the city seats the people it has
  finished with" is a seated, spent, wrapped woman — dignity law
  (rows 44/74/75 women's class), full stop.
- The BUYING-BACK (silver + barley) is a redemption image: coins
  counted into an open hand, her led out wrapped in HIS mantle. It
  must read as rescue, never as a transaction over a person — his
  eyes on her face, never appraising.

## Identity / continuity traps

- GOMER's wine-red dress is the tracking device across the whole
  arc (bright at the vow → worn at the market → glimpsed under the
  charcoal mantle after). Face-board her hardest — she ages and
  weathers but stays the SAME woman (beard-drift class applies to
  wardrobe/hair here).
- HOSEA: grief-free young face at the vow, worn but never bitter
  after. Same man ~24 frames.
- The BLUE DOOR is the row's visual rhyme (vow → left open → restored
  → closing frame). It must be the same door every time — HOME is
  promote-first from b01; every later HOME frame copies it.

## Direction law (Cameron's Peter-walking-sideways class)

- b06: she walks AWAY from the open door, small on the road — camera
  at the threshold, her back to us. Never sideways, never toward.
- b13/b33: Hosea walks the SAME road the SAME direction she went.
- b30 is the doctrine frame: she has TURNED — now facing back up the
  road toward home. The reversal must be unmistakable at a glance.

## Coverage shape

Three true wides with stated geometry: b02 (the vow — past the
family's backs at the low wall), b15 (market established once — high
over the stalls, crowd from the side), b23 (leaving the market —
camera following behind them as the crowd parts). Thirteen flips:
lone-figure road beats, person-free postcard/desert frames, the
hands-insert b32, the two-shots b36/b38.

- Light arc: golden evening → grey morning → cold dusk glitter →
  flat noon → rose-gold dawn → warm dusk. The light IS the theology.
- Plates: build-38 MARKET auto-match REJECTED (wrong place class —
  village doorway vs city market). HOME promote-first from b01,
  MARKET from b15, WILD from b25.
- Clone-crowd check on b15/b18/b23 market crowds (rows 90/107 class);
  counts law: exactly TWO at the vow door, family behind the wall.

## RUNNER PARK 2026-08-13 → NEEDS-AUDIO (Opus runner, Machine A `Dev`) — AUDIO-DOMAIN complaint, pictures untouched

**Cameron's complaint (his words, `v2_outline.py 117`):** *"it was all good
until the very end where you miss pronounced 'Dramatized' — fix that audio at
the very end and its good."*

**Domain verdict: AUDIO, not picture.** Grep-confirmed the word "dramatized"
appears in exactly ONE place in the whole cut — the closing question **card**:
`make_narration.py:56` NARRATOR line *"God **dramatized** his own love with a
marriage: however far she wandered, he went and bought her back and brought her
home. You are not too far gone to be wanted. What would it mean to be loved home
like that?"* No still is wrong; the runner did NOT re-cut pictures (per
complaint-first / touch-once law — a picture re-cut here would burn credits and
change nothing Cameron flagged). All 38 stills stay as shipped.

**Exact fix for the audio lane (this note is your per-row authority):**
1. **File to re-voice:** the CARD audio only. Shipped audio uses
   `AUDIO_FROM_V1_SEGMENTS=True` (see board), so the delivered card comes from
   the **V1 dir**: `media-production/build-117-hosea-buys-her-back/audio/card.mp3`
   (write the corrected mp3 THERE; V2-dir `audio/card.mp3` is the same text).
   Nothing else in the narration is touched.
2. **The defect:** "dramatized" is mispronounced. Target reading is
   DRAM-uh-tized — /ˈdræm.ə.taɪzd/, primary stress on the FIRST syllable, hard
   final "-ized" (NOT "druh-MAT-ized" like "dramatic", NOT "-teezd").
3. **Engine first (memory [[eleven-bypasses-say-map]]):** transcribe the
   delivered `card.mp3` before diagnosing. Card is 44100 Hz / 128 kbps =
   ElevenLabs profile, and NARRATOR is edge `AndrewNeural` in `VOICE` — so the
   V1 card was very likely ElevenLabs-voiced and a `mbm_pronounce.SAY` respell
   will be IGNORED. If ElevenLabs: re-render the card line directly with the
   correct pronunciation (A/B + round-trip-transcribe per
   [[eleven-vowel-fix-literal-respell]] / [[eleven-stress-defect-space-respell]];
   "dramatized" is a STRESS defect → validate front-peak stress, respell with
   SPACES not hyphens if needed). If it is edge, add a measured SAY winner.
   Keep the **caption** spelling "dramatized" unchanged (pronounce map only
   changes what is spoken).
4. Re-assemble (`v2_assemble.py 117` → AUDIO LOCK PASS — note the card is the
   +3s trailing segment the STALE-V1 flag already handles), ship, deploy
   (step 7c, live-verify the served mp4 hash), and make the review card answer
   Cameron in his words: "Your complaint — the mispronounced 'dramatized' at the
   very end — is re-voiced; the rest of the audio is unchanged."

**PROMPT AUTOPSY (rubric meta-law 3) — N/A for pictures.** No image prompt
caused this; it is a TTS pronunciation defect on the card line. No frame reroll.

**FULL-CUT GATE note for the audio lane's re-ship:** the 38 stills already
passed 3 independent FULL-CUT GATE passes (board QC cell, 2026-08-11) and are
NOT changed by this audio-only fix, so re-running the gate on the re-assembled
mp4 is a picture no-op — the only thing that changed is `card.mp3`.

Board set: State BUILT → NEEDS-AUDIO (Audio col stays OK); Claim carries
`RUNNER PARK` (no `AUDIO-FIX` string) so `autopilot.sh` line 219 routes it to
the audio lane.
