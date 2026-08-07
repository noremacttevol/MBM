# QC / RUNNER HANDOFF — build-188-be-ye-therefore-perfect (Matthew 5:44-48)

**Authored 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).** 16-beat V2 map,
`v2_prompt.py --check` PASS (0 warnings), windows contiguous+monotonic 0.000→71.724=card,
every speech onset in-window.

## 🅿️ PARKED NEEDS-AUDIO — NOT Ready. AUDIO LANE owns the fix.

### COMPLAINT LEDGER (LEARNING LAW) — OPEN, COMPLAINT-FIRST
`v2_outline.py 188`: **"'Maketh' (the archaic version of the modern word 'makes') is
pronounced MAY-kith 0:29."** — pronunciation defect in **j2** ("for he maketh his sun to
rise…").

### ROOT CAUSE (diagnosed this lane)
The global `mbm_pronounce.py` map carries `"maketh": {"jesus": "mayketh", "scripture":
"maykith"}` — a respell **tuned for edge-tts** (Eric/Steffan), with a stale note calling
"MAY-kith" Cameron's target. But build-188's delivered audio is now **ElevenLabs**: every
segment mp3 is **44100 Hz / 128 kbps** (the ElevenLabs signature; edge-tts renders at
24 kHz). j2's speaker is JESUS, so the edge-tts `"mayketh"` respell is applied and, on the
ElevenLabs voice, comes out as the wrong **"MAY-kith"** Cameron flagged. This is the SAME
engine-migration trap as rows 50/51/70 (a respell orphaned to the wrong engine).

### AUDIO-LANE FIX (needs ELEVENLABS_API_KEY — this lane spent $0)
1. Add a **build-local `SPOKEN`** override in `build-188-be-ye-therefore-perfect/
   make_narration.py` (build overrides WIN over the global map — mbm_pronounce
   `spoken_text` priority). Test candidates by ear + faster-whisper on the **ElevenLabs
   JESUS voice**, pick the one that reads clearly as MAY-kuhth / a natural "-eth" ending
   (NOT "MAY-kith"): try plain `"maketh"` first (the edge-tts note says Andrew's plain word
   tested fine — ElevenLabs may too), then `"make-eth"`, then `"may-kuth"`. **Leave the
   global map alone** so no other row changes. "sendeth" (same segment) is NOT complained
   — do not touch unless it audibly drifts.
2. Re-voice **ONLY j2** through the SAME locked ElevenLabs JESUS voice, atempo-match to the
   original j2 duration (seg 32.671→45.019 = 12.348 s) so **NO window moves**; place in the
   V1 `audio/` dir; set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py.
3. Verify: whisper the delivered mp4 near 0:29 reads "maketh" correctly; audio-audit 0;
   total unchanged (71.724 card / 79.773 total). THEN set **Ready ✅** and the review card
   MUST tell Cameron the "maketh" pronunciation is fixed.

The picture map is COMPLETE and passes --check — the picture runner may generate every
still now; only the audio blocks Ready.

## The story / speaker law
Sermon on the Mount. j1/j2/j3 are Jesus's own words → **RED** on Jesus's face (jesus=True,
ref=True). All narrator segments white. Only Jesus wears cream.

## HARD GATES
- **GOD / THE FATHER IS NEVER EMBODIED.** "children of your Father in heaven" (j2), "even
  as your Father… is perfect" (j3), and the n1/n3 "Father" lines are carried by the warm
  open SKY, the equal sun/rain, and Jesus's teaching — never a figure/throne/beam/dove/
  symbol.
- **EQUALITY MUST BE VISIBLE** (b09-b12): ONE sun, ONE rain lying equally on every field —
  no brighter field, no favoured side (build-124 sun/rain lesson).
- **CONTENT-CARE:** love-your-enemies shown as a hard, generous teaching received — no
  persecutors attacking, no violence, no judgement-lightning.
- No halo/ring/rim-light (drift-word gate). Hillside = warm late-afternoon gold; b09 sun /
  b10 rain are a DELIBERATE separate register, not drift.

## Places / cast
- **HILLSIDE + CROWD** — byte-identical to build-124 / rows 121-124 (same sermon slope +
  congregation). Reuse the mount plate via `v2_stash.py --wire` (build-124/112 carry one).
- **VALLEY-FIELDS** (NEW) — b09-b12. **Promote from b09** (a NON-Jesus frame).
- **Jesus** — injected on the teaching/j beats; JESUS-MASTER-REF + LOCK v5; only he wears
  cream; face gate exit 0.

## Runner note
Do NOT build+ship until the audio lane clears the "maketh" park and sets Ready ✅. The
picture stills may be generated in parallel, but assembly must use the corrected j2 audio.
