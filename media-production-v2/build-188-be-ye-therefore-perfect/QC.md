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

---

## ✅ PICTURE RUNNER SHIPPED — 2026-08-13 (Machine A `Dev`, Opus runner headless)

**16 stills generated, 0 rerolls (0% — well under the 15% COST-LAW budget), ~$2.14 Gemini, 0 portraits (cast fully reused).**

### COMPLAINT LEDGER (LEARNING LAW) — verified CLOSED in the rendered mp4
- **"'Maketh' pronounced MAY-kith 0:29"** → CLOSED. faster-whisper on the RENDERED mp4 (36.5–41.5s) returns "for he **maketh** his sun to rise on the evil and on the good" — the clean word, NOT "may-kith". Audio is byte-identical to the author-verified V1 segment mp3s (AUDIO_FROM_V1_SEGMENTS rebuild), so no re-voice; guard `SPOKEN={"maketh":"maketh"}` remains. Review-card answers Cameron in his words.

### Plates / places
- VALLEY-FIELDS (NEW): promoted from b09 (non-Jesus anchor); b10-b12 copied it. Terraced valley below the mount, one sun / one rain lying equally on every field (equality doctrine visible).
- HILLSIDE: shared setting-lock text (same Galilee sermon slope as build-124/121/112). Did NOT wire a plate — every reuse candidate is Jesus-bearing (lesson 11 bans handing a Jesus frame to auto-wiring, which would inject a 2nd cream figure into non-Jesus beats b02/b06).

### FULL-CUT GATE (6b) — 16/16 rendered beat frames + card viewed
- Jesus identity consistent across all 9 face beats; green/hazel eyes ref-correct (lesson 20 — NOT edited to brown); calm eyes (no "crazy eyes", lesson 18); cream-only (crowd browns/olive/blue); no halo/rim-light; proportionate scale (no giant, lesson 14).
- GOD/FATHER never embodied — "children of your Father"/"be ye perfect" carried by the open sky + Jesus's teaching, no figure/throne/beam/dove (b08 sky, b16 open arms).
- Realistic photography throughout (no cartoon/mix). Clean anatomy/hands, no owl-neck (lesson 21), no modern objects, no grey faces.
- Captions bottom-band only: j1/j2/j3 RED on Jesus, all narrator WHITE (speaker-law). Card clean.
- concat clips = 16 = BEATS (no silent last-beat drop, RUNNER-LESSONS card-window check).

Assemble: AUDIO REBUILD PASS SHA256 5cdc30bd… · 20.5 MB · 79.4s · `matthew-5_be-ye-therefore-perfect.mp4`.
