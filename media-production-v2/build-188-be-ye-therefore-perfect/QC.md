# QC / RUNNER HANDOFF — build-188-be-ye-therefore-perfect (Matthew 5:44-48)

**Authored 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).** 16-beat V2 map,
`v2_prompt.py --check` PASS (0 warnings), windows contiguous+monotonic 0.000→71.724=card,
every speech onset in-window.

## ✅ AUDIO OK — complaint RESOLVED. Ready for the picture runner (no stills yet).

### COMPLAINT LEDGER (LEARNING LAW) — CLOSED
`v2_outline.py 188`: **"'Maketh' (the archaic version of the modern word 'makes') is
pronounced MAY-kith 0:29."** — pronunciation defect in **j2** ("for he maketh his sun to
rise…"). **CLOSED 2026-08-07 (AUDIO-FIX lane, Machine A `Dev`, $0):** the delivered
ElevenLabs audio already says "maketh" correctly (MAKE-eth). Verified, guarded, wired.

### WHAT THE PARK GOT WRONG (corrected this lane)
The prior park assumed the edge-tts respell `"maketh": {"jesus": "mayketh"}` from the
global `mbm_pronounce.py` SAY map was being applied to the ElevenLabs render, producing
MAY-kith. **It is not.** The real ElevenLabs renderer `media-production/
voice_from_transcripts.py` builds its spoken string with `eleven_spoken_text()`, which
applies **only PHRASES + build-local SPOKEN** and **bypasses the SAY / SAY_BY_VOICE map by
design** (that map was measured on Azure/edge voices and would hurt ElevenLabs). So j2 was
rendered from the PLAIN word "maketh", which ElevenLabs reads correctly. Cameron's
"MAY-kith 0:29" was the **pre-migration edge-tts cut** (edge DID apply "mayketh"); the
2026-07-23 ElevenLabs re-voice already fixed it.

### VERIFICATION (faster-whisper small.en, beam 5)
- delivered `j2.mp3` — **both** this v2 dir AND the V1 twin
  `media-production/build-188-be-ye-therefore-perfect/audio/` (byte-for-byte the same
  ElevenLabs take, 44100/128k, 10.945 s) → **"...for he MAKETH his son to rise..."** = CORRECT.
- control render of plain `"maketh"` on the locked ElevenLabs JESUS voice → "maketh"
  (identical to delivered).
- control render of the old `"mayketh"` respell → **"...for he MAY KETH..."** — reproduces
  Cameron's MAY-kith defect, i.e. exactly what the old edge cut sounded like.
- "sendeth" (same segment, NOT complained) transcribes cleanly — left untouched.

### WHAT THIS LANE DID (no re-voice, $0)
1. **Durability guard:** added build-local `SPOKEN = {"maketh": "maketh"}` to BOTH
   make_narration.py files (v2 dir + V1 twin). Build overrides WIN over the global map in
   both engines (verified: edge `spoken_text` returns plain "maketh" with the guard vs
   "mayketh" without; eleven returns plain "maketh" regardless), so no future re-render can
   re-introduce "mayketh". Global SAY map left untouched (other rows unaffected).
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py — assembly rebuilds the track from
   the build's own correct segment mp3s at the extract_beats offsets. Verified: extract
   resolves, all 9 placed segs (n0,j1,n0b,j2,n1,n2,n3,j3,card) present, total 79.4 s.
3. `v2_prompt.py --check` → PASS (16 beats). Audio unchanged (no hash change — nothing
   re-voiced); the sanctioned exception was not needed.

### FOR THE PICTURE RUNNER — review-card 🛠 line (answer Cameron in his words)
> **Your complaint — "'Maketh' pronounced MAY-kith at 0:29" — is fixed.** Jesus now says
> "maketh" the right way (MAKE-eth) in "for he maketh his sun to rise." Nothing else in the
> audio changed.

The picture map is COMPLETE and passes --check — generate all 16 stills and assemble on
this corrected-and-verified audio.

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
