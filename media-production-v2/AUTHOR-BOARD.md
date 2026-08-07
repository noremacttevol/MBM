# AUTHOR-BOARD — the V2 authoring/runner handshake (created 2026-08-05)

Machine-generated inventory; regenerate the raw columns any time with the script in
SESSION-LOG 2026-08-05. **Claim** and **Ready** are the only hand-edited columns.

- The FABLE 5 AUTHOR session (PROMPT-FABLE5-AUTHOR.md) works lowest OPEN row first:
  claim it (claim-by-push), author/upgrade the package, set Ready ✅, push.
- The OPUS RUNNER (PROMPT-OPUS-RUNNER.md) builds only rows with Ready ✅, lowest
  first, claiming in QUEUE.md as always. Audio CHECK rows are authored but NOT
  assembled until the audio is verified new-voice (they go on NEEDS-AUDIO below).
- BUILT rows are done pending Cameron's approval and his open complaints.

| Row | Build | State | Stills | Audio | Claim | Ready |
|---|---|---|---|---|---|---|
| 1 | build-01-cloak | BUILT | 20 | OK | C-FIX 2026-08-06 SHIPPED |  |
| 2 | build-02-prodigal | BUILT | 48 | OK |  |  |
| 3 | build-03-zacchaeus | BUILT | 26 | OK |  |  |
| 4 | build-04-nicodemus | BUILT | 30 | OK |  |  |
| 5 | build-05-bent-woman | BUILT | 74 | OK |  |  |
| 6 | build-06-two-sons | BUILT | 39 | OK |  |  |
| 7 | build-07-peter-water | BUILT | 8 | OK |  |  |
| 8 | build-08-lost-coin | BUILT | 23 | OK |  |  |
| 9 | build-09-rich-ruler | BUILT | 52 | OK | C-FIX 2026-08-06 SHIPPED |  |
| 10 | build-10-well | BUILT | 81 | OK | AUDIO-FIX 2026-08-07 SHIPPED (Machine A `Dev`): j2 robotic recurrence FIXED. Backed the over-slow off — deleted PHRASE_RATE["j2"] (-30%→Jesus default -22%) and removed the LEADING ellipsis, kept ONE gentle mid-line pause. j2 4.92s→3.96s; faster-whisper confirms exact words "I that speak unto thee, am he" in the delivered mp4 (no "the Amhi" slur — comma/faster rate re-slur, only ellipsis@-22% works). AUDIO REBUILD PASS cc736013, 295.8s. Old robotic take saved as j2.mp3.robot-2026-08-07. Deployed + live-verified, hash bb65a539c1a1. $0 (edge-tts), 0 rerolls, 0 pictures touched. See QC.md ✅ RESOLVED block. |  |
| 11 | build-11-storm | AUTHORED | 65 | OK |  | ✅ AUTHOR-DONE 2026-08-07 (Machine A `Dev`): boat-lock rebuild authored — s07 promoted to PLACE-REF/boat.jpeg + wired into all 23 hull beats, EIGHT-crew + Jesus-position locks written into beats_v2.py, s16 fixed to the locked Jesus, Jesus added asleep in stern on wide storm frames b10/b13. --check PASS, audio untouched (OK). RUNNER: re-cut per QC.md "🅿️ RUNNER — do this" — --redo the boat beats against the plate, KEEP s07, AUDIO LOCK byte-identical. |
| 12 | build-12-bartimaeus | BUILT | 79 | OK |  |  |
| 13 | build-13-roof | BUILT | 88 | OK | C-FIX 2026-08-07 SHIPPED |  |
| 14 | build-14-ten-lepers | BUILT | 68 | OK |  |  |
| 15 | build-15-centurion | BUILT | 71 | OK | C-FIX 2026-08-07 SHIPPED |  |
| 16 | build-16-mary-martha | BUILT | 26 | OK | C-FIX 2026-08-07 SHIPPED |  |
| 17 | build-17-lazarus | BUILT | 61 | OK | C-FIX 2026-08-07 LIVE |  |
| 18 | build-18-emmaus | BUILT | 41 | OK | AUDIO-FIX 2026-08-07 SHIPPED (Machine A `Dev`, Fable-5 author lane): Cameron's "You mispronounced Jesus's" FIXED. Root cause corrected — the shipped narration is ElevenLabs (Brian), NOT edge-tts, so the park's make_narration/edge-tts respell would have swapped the narrator voice at the opening. Instead re-voiced ONLY n0 through the SAME ElevenLabs Brian narrator with the possessive respelled "Jesuses" (→/JEE-zus-iz/), caption unchanged (extract_beats reads SEGMENTS s[2]); pitch-preserving atempo-matched back to the original 19.592s so NO downstream window moved. AUDIO_FROM_V1_SEGMENTS=True, AUDIO REBUILD PASS 3592466846055ce4, 243.3s. Verified in delivered mp4 (possessive onset shifted 5.62→5.20s n0-local, word span ~tripled). $0 image, ~cents ElevenLabs, 0 pictures touched. Reproducible: revoice_n0.py. See QC.md §0 ✅. |  |
| 19 | build-19-shore | BUILT | 37 | OK | AUDIO-FIX 2026-08-07 DONE (Machine A `Dev`): complaint (A) "JESUS talks too fast / ignores commas" FIXED — j1 re-voiced through the locked ElevenLabs JESUS voice, 2.04s→3.29s (both commas now breathe, no robotic dead-air), AUDIO_FROM_V1_SEGMENTS=True set so the re-cut rebuilds the fixed j1. Live cut NOT re-shipped on purpose (its complaint must still match the live hash so the picture lane owns it). **PICTURE C-FIX PENDING (B):** reroll beat v2-r019-b17/s17 (Peter swims toward the beach at 1:05, CAMERON GATE) + re-cut over the new audio + ship — ONE touch-once re-cut closes BOTH. Do NOT re-park to NEEDS-AUDIO (audio already fixed at source). See QC.md §0 green block. |  |
| 20 | build-20-samaritan | BUILT | 42 | OK |  |  |
| 21 | build-21-lost-sheep | BUILT | 33 | OK |  |  |
| 22 | build-22-unmerciful-servant | BUILT | 48 | OK | AUDIO-FIX 2026-08-07 SHIPPED (Machine A `Dev`): complaint "2:46 Jesus mispronounces shouldest it should be should-est" FIXED — added SPOKEN {"shouldest":"should-est"}, re-voiced ONLY j5.mp3 (edge-tts, $0), other 24 segments byte-identical. A/B-confirmed the two-part SHOULD-est reading. AUDIO_FROM_V1_SEGMENTS=True + beats_v2 still-windows remapped for the +0.17s j5 shift (spoken-trimmed, not the raw +0.895s). Realistic 48-still V2 pictures UNCHANGED, 0 rerolls. AUDIO REBUILD PASS 20a6ef72, 225.2s. Reviewer card + cache-buster ?v=6e6943d8c0dc updated, deployed + live-verified. See QC.md ✅ RESOLVED. |  |
| 23 | build-23-vineyard | BUILT | 40 | OK |  |  |
| 24 | build-24-sower | BUILT | 35 | OK |  |  |
| 25 | build-25-wheat-and-tares | BUILT | 33 | OK |  |  |
| 26 | build-26-mustard-seed | BUILT | 24 | OK |  |  |
| 27 | build-27-leaven | NEEDS-AUDIO | 29 | CHECK | C-FIX 2026-08-07 PARKED NEEDS-AUDIO: OPEN complaint is generic AUDIO-domain — Cameron "Audio is messed up on this one." Runner cannot re-voice (audio-immutability); all 11 segments render at correct durations & A/V is aligned (104.47s), so it's a delivery defect inside the spoken narration, not a truncation. AUTHOR: listen to matthew-13_leaven.mp4, localize the bad segment(s), fix at make_narration.py (respell or re-render the glitchy TTS take), regenerate only that mp3, re-assemble, ship via C-FIX. No picture defect — audio only, $0 spent. See QC.md §0 RUNNER PARK. · AUDIO-FIX 2026-08-07 BLOCKED (needs ear-check, Machine A `Dev`): headless diagnostics EXHAUSTED — full-mp4 transcript correct end-to-end (s33 "spake he" is right; n1 "doubling" is a whisper artifact, single 6.30s pass), AAC decodes 0 errors (not row-31 class), levels/LUFS/peak IDENTICAL to approved rows 22/24/26/32, mono clean, A/V aligned. Cameron reviewed exactly this cut (blob 1e389df4=sha1 a0193524). Cannot localize the delivery defect without listening; blind re-voice can't fix it (edge-tts deterministic — same input→same audio). Needs one ear-pass to name the bad segment, then a targeted single-segment input fix. Full evidence + resume in QC.md §0b. $0, no audio/pictures changed. |  |
| 28 | build-28-hidden-treasure | BUILT | 29 | OK |  |  |
| 29 | build-29-pearl | BUILT | 36 | OK |  |  |
| 30 | build-30-net | BUILT | 40 | OK |  |  |
| 31 | build-31-ten-virgins | BUILT | 40 | OK | C-FIX 2026-08-07 SHIPPED — 1:59 playback stall FIXED (corrupt AAC packet); audio rebuilt from source mp3s (AUDIO_FROM_V1_SEGMENTS, byte-identical narration, NOT a re-voice), new mp4 decodes 0 errors, deployed + live-verified hash b6be9e209550. $0/0 rerolls. See QC.md COMPLAINT LEDGER. |  |
| 32 | build-32-talents | BUILT | 50 | OK |  |  |
| 33 | build-33-sheep-goats | NEEDS-REBUILD | 49 | OK | AUTHOR-DONE 2026-08-07 (Machine A `Dev`): BOTH complaints fixed in author files + coupled timeline verified by full local assemble (AUDIO REBUILD PASS 91b16db5, 182.585s). Complaint 2 (1:16 wrong voice) DONE — j37 JESUS→SCRIPTURE, re-voiced, now light-blue on the woman (verified 0:77); +2.611s timeline coupling remapped across b21-b45 (j37 16.901→19.512s, NOT the park's backwards estimate), j2 still red on Jesus & in sync (verified 2:05). Complaint 1 (1:10 black nails) — author half done: deleted "the nails black" from b20 scene text. RUNNER: reroll ONLY s20 vs the fixed text, re-assemble (overwrites the verification mp4 that still has black nails — DO NOT ship it), then ship. See QC.md "AUTHOR DONE" + COMPLAINT LEDGER. | ✅ |
| 34 | build-34-rich-fool | BUILT | 35 | OK |  |  |
| 35 | build-35-great-banquet | BUILT | 40 | OK |  |  |
| 36 | build-36-shrewd-steward | BUILT | 47 | OK |  |  |
| 37 | build-37-rich-man-lazarus | BUILT | 49 | OK |  |  |
| 38 | build-38-persistent-widow | BUILT | 46 | OK |  |  |
| 39 | build-39-pharisee-publican | BUILT | 58 | OK | C-FIX 2026-08-07 SHIPPED |  |
| 40 | build-40-the-friend-at-midnight | BUILT | 56 | OK | C-FIX 2026-08-07 SHIPPED |  |
| 41 | build-41-counting-the-cost | BUILT | 58 | OK |  |  |
| 42 | build-42-barren-fig-tree | BUILT | 35 | OK | C-FIX 2026-08-07 SHIPPED — caption/picture drift (up to 12s ahead of voice) FIXED by remapping all 35 beats_v2.py still-windows from the stale pre-re-voice 200s timeline to the live 223s audio timeline; AUDIO LOCK PASS (byte-identical narration), 0 rerolls, $0. Live hash fae898d99076. |  |
| 43 | build-43-the-wedding-garment | BUILT | 48 | OK |  |  |
| 44 | build-44-two-debtors | AUTHORED | 0 | OK | PARKED — QUEUE row 44 was SWAPPED to Pentecost (Cameron via Planner, 2026-07-23); two-debtors is a dead story (duplicate of #74). Pentecost needs NEW narration/audio — the V2 stills pipeline cannot build it. Do NOT build two-debtors. |  |
| 45 | build-45-wicked-tenants | BUILT | 54 | OK | A-auto 2026-08-06 SHIPPED; C-FIX 2026-08-07 SHIPPED | ✅ |
| 46 | build-46-seed-growing | BUILT | 32 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 47 | build-47-houses-on-rock-and-sand | BUILT | 37 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 48 | build-48-new-wine-old-bottles | BUILT | 0 | OK | A-auto 2026-08-06 SHIPPED · C-FIX 2026-08-07 SHIPPED — 2:34 "spout out of side of the bag" FIXED (rerolled b28, pour now jug→new skin; live hash e5abfd1003c2, mp4 HTTP 200); $0.13/1 reroll | ✅ |
| 49 | build-49-water-to-wine | BUILT | 40 | OK | A-auto 2026-08-06 SHIPPED; C-FIX 2026-08-07 SHIPPED | ✅ |
| 50 | build-50-noblemans-son | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — Cameron complaint "Cana → Kane-a" CLOSED: n1/n3 re-voiced, narrator now says KANE-a ("Kaina", whisper-verified), same AndrewNeural voice. 0 V2 stills → handed to picture runner to build on corrected audio. See QC.md "AUDIO FIX DONE". |
| 51 | build-51-first-catch-of-fish | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — Cameron complaint "tear → tare" CLOSED: n4 re-voiced, "tear" (to rend) now spoken "tare"/care not "teer"/fear; caption stays "tear", same NARRATOR voice. 0 V2 stills → handed to picture runner to build on corrected audio. See QC.md "AUDIO FIX DONE". |
| 52 | build-52-demoniac-synagogue | BUILT | 24 | OK | A-auto 2026-08-06 SHIPPED · C-FIX 2026-08-07 SHIPPED — demoniac face-flip FIXED (wired freedman IMAGE-lock + rerolled 6 flipping frames; live hash 17566283905d, mp4 HTTP 200); $0.80/6 rerolls | ✅ |
| 53 | build-53-peters-mother-in-law | BUILT | 15 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 54 | build-54-the-leper | BUILT | 24 | OK | A-auto 2026-08-06 SHIPPED · C-FIX 2026-08-07 SHIPPED | ✅ |
| 55 | build-55-withered-hand | BUILT | 23 | OK | A-auto 2026-08-06 SHIPPED · C-FIX 2026-08-07 SHIPPED (Machine A `Dev`) — Cameron's "the person with the withered hand [is] not looking the same in every picture" complaint FIXED. Root cause: runner never built the hand-man face anchor the CAST-REF NOTE prescribes, so every MAN-locked beat reinvented his face. Built CAST-REF-V2/hand-man-ref.jpeg (cropped from accepted s15) + wired REFS={"MAN":...}, rerolled the 4 drifted/defective frames against it: s03 (0:12 full-grey-beard stranger), s09 (elderly white-beard), s10 (young dark-haired man) → all now the canonical ~52 grey-streaked-short-beard man; s18 (1:34 "double right arm") → one clean arm. Kept the 8 already-matching frames byte-identical. AUDIO LOCK PASS (byte-identical narration, no re-voice). 4 rerolls/17%, $0.54. Deployed + live-verified. | ✅ |
| 56 | build-56-widow-of-nain | BUILT | 22 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 57 | build-57-jairus-daughter | BUILT | 27 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 58 | build-58-feeding-5000 | BUILT | 24 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 59 | build-59-feeding-4000 | BUILT | 27 | OK | C-FIX 2026-08-07 SHIPPED (Machine A `Dev`, author lane): second-feeding scholarship cut deployed + live-verified (hash a3f82c4971b0, mp4 HTTP 200), complaint CLOSED on the reviewer; $0. · AUTHOR-DONE 2026-08-07 (Machine A `Dev`): SECOND-FEEDING scholarship complaint ANSWERED in narration, $0/0 credits. n2b now names it plainly as a distinct SECOND feeding ("working the very same sums a second time"); n5 draws the 5-loaves→12-baskets (Matt 14) vs 7-loaves→7-baskets (Mark 8) comparison AND cites that Jesus himself made the disciples count BOTH (Mark 8:19-21 / Matt 16:9-10). Edited V1+V2 make_narration, re-voiced ONLY n2b+n5 (free edge-tts AndrewNeural), added 2 scholarship beats (b13b/b23b) REUSING existing stills s12/s16 — no new image. Timeline remapped 172.5→207.3s, all 29 windows contiguous, --check PASS. Re-assembled locally (stills done). RUNNER: verify the new mp4, deploy, ship with a card telling Cameron his complaint was addressed. See QC.md "AUTHOR DONE". | ✅ |
| 60 | build-60-gerasene-demoniac | BUILT | 39 | OK | A-auto 2026-08-06 SHIPPED · C-FIX 2026-08-07 SHIPPED (2:39 Jesus eyes: rerolled ONLY b28, pale-green stare→warm downcast gaze, 1 reroll 2.6%, AUDIO LOCK PASS byte-identical, live hash 139078b0a0b5) | ✅ |
| 61 | build-61-syrophoenician-woman | BUILT | 31 | OK | AUDIO-FIX 2026-08-06 SHIPPED — STALE-V1 lock cleared (AUDIO_FROM_V1_SEGMENTS=True), audio rebuilt from 15 new-voice segments, realistic-V2 cut 185.2s/21.2MB assembled + deployed + live-verified. mp4 SHA256 106884ad. See QC.md "AUDIO FIX DONE". | ✅ |
| 62 | build-62-ephphatha | BUILT | 34 | OK | A-auto 2026-08-07 SHIPPED (Machine A `Dev`): resumed a mid-build strand (14/34 → 34/34). OPEN complaint "he lost his beard in one picture" FIXED — deaf man beard-boarded across every frame, held by wired REFS[DEAFMAN]. 0 rerolls (clean first attempt), $2.68, meter→$422.23. AUDIO LOCK PASS 67869848, 202.8s. Deployed + live-verified. See QC.md COMPLAINT LEDGER. |  |
| 63 | build-63-man-born-blind | AUTHORED | 41 | OK | AUDIO-FIX 2026-08-07 DONE (Machine A `Dev`, author lane): Cameron's OPEN Siloam complaint ("still wrong its : si-LOH-uhm") FIXED. Root cause: delivered build is ElevenLabs (Chris/Brian, 44.1kHz) — plain "Siloam" renders "Salome" on that voice. Respelled SPOKEN "Siloam"→"Siloh-am" (round-trips CLEAN to "Siloam" on base.en+small.en for BOTH voices AND both TTS backends), re-voiced j2+n5 through ElevenLabs (matching engine, audio-audit A now 0/23). Timeline coupled: j2 −0.525s, n5 −1.744s → windows remapped (piecewise-linear on segment onsets), total 247.692s, AUDIO_FROM_V1_SEGMENTS=True. --check PASS, audio-audit A/B/C all 0. Stills 41/43 → PICTURE RUNNER: gen b42/b43 (~$0.27), assemble (AUDIO REBUILD), ship w/ COMPLAINT LEDGER. See QC.md §0-FIXED. | ✅ |
| 64 | build-64-pool-of-bethesda | BUILT | 41 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 65 | build-65-help-mine-unbelief | BUILT | 36 | OK | A-auto 2026-08-06 SHIPPED; C-FIX 2026-08-07 SHIPPED | ✅ |
| 66 | build-66-malchus-ear | BUILT | 29 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 67 | build-67-the-transfiguration | BUILT | 16 | OK | A-auto 2026-08-06 SHIPPED · C-FIX 2026-08-07 SHIPPED | ✅ |
| 68 | build-68-multitudes-mountain | BUILT | 35 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 69 | build-69-baptism | BUILT | 29 | OK | AUDIO-FIX shipped 2026-08-06 da00221e35d6 — STALE-V1 lock cleared (AUDIO_FROM_V1_SEGMENTS), new-voice cut assembled 172.3s, deployed+live-verified. · C-FIX 2026-08-07 SHIPPED 7a6616e22fde — John's hair "orange" fixed: rerolled ONLY s12/b12 to black-per-reference (13/14 John frames already correct), audio byte-identical (same SHA, 172.3s), deployed+live-verified. | ✅ |
| 70 | build-70-temptations | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — Cameron complaints "narrator spells 'I-S'" + "'proceedeth' should be pro-see-duhth" CLOSED: n2 re-voiced (caps IS/IF now spoken as words, caption keeps caps), j1 re-voiced ("proceeduth" → whisper-verified pro-see-duhth), same Andrew/Eric voices; other 20 mp3s byte-identical. $0 (edge-tts). 0 V2 stills → picture runner builds on corrected audio; COMPLAINT LEDGER in QC.md for its review card. See QC.md "AUDIO FIX DONE". |
| 71 | build-71-the-great-commission | BUILT | 21 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 72 | build-72-calling-matthew | BUILT | 41 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 73 | build-73-this-day-fulfilled | NEEDS-REBUILD | 18 | OK | AUTHOR-DONE 2026-08-07 (Machine A `Dev`): FULLNESS REBUILD complete. Message re-authored so the close TEACHES the fullness (Isaiah 61 = His own mission in His own mouth; He is risen; the same plan continues today, restored-Church frame, church never named; Two-Voice intact) + opening face-drift handed to reroll. NEW n4/n5 + rewritten card re-voiced through the SAME ElevenLabs Brian narrator (engine-matched 44.1kHz, whisper-verified), AUDIO_FROM_V1_SEGMENTS=True, total 154.322s. beats_v2 21 beats --check PASS, schedule contiguous; COST LAW held — teaching adds only ONE new still (s18 door), the other 3 teaching beats REUSE approved s06/s09/s16. RUNNER (paid, one re-cut): gen s18, reroll drift frames s01/s02 vs JESUS-MASTER-REF (face gate 0), assemble (AUDIO REBUILD), re-audit, ship w/ COMPLAINT LEDGER. $0 image, ~cents ElevenLabs. See QC.md "✅ AUTHOR DONE — FULLNESS REBUILD". · (prior RUNNER PARK 2026-08-07: complaint is AUTHOR content-rebuild (RUNNER-LESSONS §511), NOT a runner reroll — narration must give the FULLNESS of the message (teach how Jesus MEANT it, that He has risen and continues the plan, framed the way the prophets/restored church teach it, WITHOUT naming the church). Also lock Jesus's face across the opening beats: s01 vs s02 drift (s01 lighter wavy hair/softer face vs s02 near-black hair/fuller beard). Pictures+audio byte-identical, $0. See QC.md RUNNER PARK block. | ✅ |
| 74 | build-74-woman-washed-his-feet | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1 audio-lock cleared (AUDIO_FROM_V1_SEGMENTS); 19/19 new-voice segments verified. 0 stills → picture runner builds on corrected audio. See QC.md "AUDIO FIX DONE". |
| 75 | build-75-woman-taken-in-adultery | BUILT | 21 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 76 | build-76-suffer-the-little-children | BUILT | 14 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 77 | build-77-widows-mite | BUILT | 16 | OK | AUDIO-FIX 2026-08-07 SHIPPED (Machine A `Dev`, Fable-5 author lane): STALE-V1 audio-lock CLEARED — set AUDIO_FROM_V1_SEGMENTS=True, track rebuilt from 12 V1 segment mp3s = 98.846s == extract_beats total (drift gone). Assembled the realistic-V2 cut on the 16 present stills, AUDIO REBUILD PASS 6b2142d9, 98.8s/20.9MB, decodes 0 errors. Caption QC PASS (bottom-band, blue scripture/white narrator, realistic-only Law 14 on all 16). No open Cameron complaint (build-blocking lock, not a complaint fix); ledger was versions:[] → FIRST v2 publish. review.html v77 repointed to V2 path (realistic-v2 wave), deployed + live-verified. $0, 0 rerolls, 0 pictures touched. See QC.md ✅ SHIPPED. |  |
| 78 | build-78-who-is-my-mother | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1 audio-lock CLEARED (AUDIO_FROM_V1_SEGMENTS=True): V1 mp4 stale vs 11 re-voiced mp3s; v2_assemble now clears the audio gate (stops only on missing stills), 11/11 segment parity. $0, nothing re-voiced. 0 V2 stills → picture runner generates + assembles on corrected new-voice audio. Same mechanism as shipped row 69. See QC.md "AUDIO FIX DONE". |
| 79 | build-79-the-seventy-sent | BUILT | 19 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 80 | build-80-come-unto-me | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1 audio-lock CLEARED (AUDIO_FROM_V1_SEGMENTS=True): V1 mp4 stale vs 11 re-voiced mp3s; v2_assemble now clears the audio gate (stops only on missing stills), 11/11 segment parity. $0, nothing re-voiced. 0 V2 stills → picture runner generates + assembles on corrected new-voice audio. Same mechanism as shipped row 69. See QC.md "AUDIO FIX DONE". |
| 81 | build-81-render-unto-caesar | BUILT | 16 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 82 | build-82-anointing-at-bethany | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1 audio-lock CLEARED (AUDIO_FROM_V1_SEGMENTS=True): V1 mp4 failed both tripwires (19 newer mp3s + +7s excess); v2_assemble now clears the audio gate (stops only on missing stills), 19/19 segment parity. $0, nothing re-voiced. 0 V2 stills → picture runner generates + assembles on corrected new-voice audio. See QC.md "AUDIO FIX DONE". |
| 83 | build-83-weeping-over-jerusalem | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1 audio-lock CLEARED (AUDIO_FROM_V1_SEGMENTS=True): V1 mp4 runtime tripwire (|Δ|~2.2s); v2_assemble now clears the audio gate (stops only on missing stills), 10/10 segment parity. $0, nothing re-voiced. 0 V2 stills → picture runner generates + assembles on corrected new-voice audio. See QC.md "AUDIO FIX DONE". |
| 84 | build-84-no-room-manger | RUNNING | 0 | OK | A-auto 2026-08-07 RESUME-13of34 LIVE | ✅ |
| 85 | build-85-shepherds-and-angels | BUILT | 23 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 86 | build-86-the-wise-men | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL lock cleared (AUDIO_FROM_V1_SEGMENTS=True); 14 new-voice segments present, rebuild source verified; no Cameron complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 87 | build-87-boy-in-the-temple | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL lock cleared (AUDIO_FROM_V1_SEGMENTS=True); 12 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 88 | build-88-triumphal-entry | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL lock cleared (AUDIO_FROM_V1_SEGMENTS=True), both tripwires; 15 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 89 | build-89-last-supper | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL lock cleared (AUDIO_FROM_V1_SEGMENTS=True); 14 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 90 | build-90-washing-feet | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL lock cleared (AUDIO_FROM_V1_SEGMENTS=True), both tripwires (V1 mp4 +31.2s longer than timeline, stale audio); 13 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 91 | build-91-gethsemane | BUILT | 40 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 92 | build-92-peters-denial | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL recency lock cleared (AUDIO_FROM_V1_SEGMENTS=True); 9 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 93 | build-93-barabbas-goes-free | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL recency lock cleared (AUDIO_FROM_V1_SEGMENTS=True); 14 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 94 | build-94-father-forgive-them | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL recency lock cleared (AUDIO_FROM_V1_SEGMENTS=True); 11 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 95 | build-95-thief-on-the-cross | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL recency lock cleared (AUDIO_FROM_V1_SEGMENTS=True); 11 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 96 | build-96-it-is-finished | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL recency lock cleared (AUDIO_FROM_V1_SEGMENTS=True); 14 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 97 | build-97-the-empty-tomb | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL recency lock cleared (AUDIO_FROM_V1_SEGMENTS=True); 13 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 98 | build-98-mary-her-name | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL recency lock cleared (AUDIO_FROM_V1_SEGMENTS=True); 17 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 99 | build-99-flesh-and-bone-thomas | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL recency lock cleared (AUDIO_FROM_V1_SEGMENTS=True); 15 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 100 | build-100-the-ascension | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1-FINAL recency lock cleared (AUDIO_FROM_V1_SEGMENTS=True); 10 new-voice segments present; no complaint on file. 0 V2 stills → picture runner builds+assembles on corrected audio. See QC.md "AUDIO FIX DONE". |
| 101 | build-101-still-small-voice | BUILT | 28 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 102 | build-102-jacobs-ladder | BUILT | 28 | OK | A-auto 2026-08-06 SHIPPED · C-FIX 2026-08-07 SHIPPED | ✅ |
| 103 | build-103-peters-confession | BUILT | 20 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 104 | build-104-boy-samuel | BUILT | 22 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 105 | build-105-face-to-face | AUTHORED | 0 | OK | AUDIO-FIX 2026-08-07 DONE (Machine A `Dev`): STALE-V1-FINAL resolved — set AUDIO_FROM_V1_SEGMENTS=True in beats_v2.py. VERIFIED the rebuild gate: track rebuilt from the 18 V1 mp3s = 164.257s == extract_beats total to the ms (PASS). $0, no re-voice. No V2 stills yet → handed to picture runner; build the 26 beats on this fixed audio. See QC.md RUNNER PARK. | ✅ |
| 106 | build-106-god-spake-by-prophets | AUTHORED | 0 | OK | AUDIO-FIX 2026-08-07 DONE (Machine A `Dev`): STALE-V1-FINAL (both gates) resolved — set AUDIO_FROM_V1_SEGMENTS=True in beats_v2.py. VERIFIED the rebuild gate: track rebuilt from the 16 V1 mp3s = 152.043s == extract_beats total to the ms (PASS). $0, no re-voice. No V2 stills yet → handed to picture runner; build the 24 beats on this fixed audio. See QC.md RUNNER PARK. | ✅ |
| 107 | build-107-john-baptist-doubt | BUILT | 25 | OK | A-auto 2026-08-06 SHIPPED · C-FIX 2026-08-07 SHIPPED | ✅ |
| 108 | build-108-my-sheep-hear-my-voice | AUTHORED | 0 | OK | AUDIO-FIX 2026-08-07 DONE (Machine A `Dev`): STALE-V1-FINAL (both tripwires) resolved — set AUDIO_FROM_V1_SEGMENTS=True in beats_v2.py. VERIFIED the rebuild gate: track rebuilt from the 14 V1 mp3s = 148.623s == extract_beats total to the ms (PASS). $0, no re-voice. No V2 stills yet → handed to picture runner; build the 23 beats on this fixed audio. See QC.md RUNNER PARK. | ✅ |
| 109 | build-109-ask-seek-knock | BUILT | 23 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 110 | build-110-lords-prayer | BUILT | 23 | OK | A-auto 2026-08-06 SHIPPED · C-FIX 2026-08-07 SHIPPED (stale-cache delivery bug — mp4 verified already-realistic, swept all 201 cards to direct raw.githubusercontent host, $0/0 rerolls, deployed+live-verified) | ✅ |
| 111 | build-111-lilies-and-sparrows | BUILT | 29 | OK | A-auto 2026-08-06 SHIPPED · C-FIX 2026-08-07 SHIPPED (0:09 "out of scale and weird" = GIANT sparrows on s11/b11; ONE reroll → true-size birds, everyone proportioned, AUDIO byte-identical SHA256 51aba66b, deployed+live-verified hash a6d65d967074, 1 reroll 3.4%/$0.13) | ✅ |
| 112 | build-112-beatitudes | BUILT | 27 | OK | A-auto RESUME SHIPPED Dev 2026-08-07 (scale complaint FIXED, 0 rerolls) | ✅ |
| 113 | build-113-where-art-thou | BUILT | 26 | OK | AUDIO-FIX 2026-08-07 SHIPPED (Machine A `Dev`): STALE-V1-FINAL cleared — set AUDIO_FROM_V1_SEGMENTS=True, rebuilt track from V1 mp3s = 163.079s == extract_beats total to the ms (AUDIO REBUILD PASS 4cdc391c). Re-assembled the full realistic cut (git-blob 9aeeb822, 163.1s, decodes 0 errors), stills reusable (no regen, $0 audio). Realistic + GOD embodied (s26 white-robe elder) confirmed. Reviewer card repointed to V2 realistic path, answers Cameron's "God has a body / make a character for him" complaint; deployed + live-verified. See QC.md ✅ SHIPPED. |  |
| 114 | build-114-abraham-sodom | RUNNING | 23 | OK | A-auto 2026-08-06 PARKED billing-depleted: 23/23 stills + ABRAHAM portrait DONE, HEIGHT/CAMP plates promoted. NOT shipped — b13/b14 are COLLAGES needing reroll; blocked on Gemini "prepayment credits depleted" 429 (persisted after 60s retry). Do NOT regen the 21 good stills. Resume in QC.md after Cameron tops up billing. | ✅ |
| 115 | build-115-ram-in-the-thicket | AUTHORED | 16 | OK | A-auto 2026-08-06 PARKED-BILLING: Gemini prepayment credits DEPLETED (429 persists across 60s retry) — GLOBAL key block, stops all lanes. 16/32 stills done (b01-b16, valid, do NOT regen) + portraits + MORIAH plate. Cameron must top up AI Studio billing, then resume `v2_gen_api build-115... --ceiling <meter+16*0.201+25>`. See QC.md RUNNER PARK. | ✅ |
| 116 | build-116-graven-on-his-palms | AUTHORED | 0 | OK | PARKED-BILLING 2026-08-06: Gemini prepayment credits STILL depleted (2nd probe, $0). WOMAN portrait + CITY plate (b04) done. Resume `v2_gen_api build-116... --ceiling <meter+20*0.201+25>` after Cameron tops up AI Studio billing. See QC.md. | ✅ |
| 117 | build-117-hosea-buys-her-back | AUTHORED | 0 | OK |  | ✅ |
| 118 | build-118-jonah-god-who-relents | AUTHORED | 0 | OK |  | ✅ |
| 119 | build-119-fourth-man-in-fire | AUTHORED | 0 | OK |  | ✅ |
| 120 | build-120-job-from-whirlwind | AUTHORED | 0 | OK |  | ✅ |
| 121 | build-121-salt-and-light | AUTHORED | 0 | OK |  | ✅ |
| 122 | build-122-mote-and-beam | AUTHORED | 0 | OK |  | ✅ |
| 123 | build-123-golden-rule | AUTHORED | 0 | OK |  | ✅ |
| 124 | build-124-love-your-enemies | AUTHORED | 0 | OK |  | ✅ |
| 125 | build-125-i-never-knew-you | AUTHORED | 0 | OK |  | ✅ |
| 126 | build-126-by-their-fruits | AUTHORED | 0 | OK |  | ✅ |
| 127 | build-127-the-strait-gate | AUTHORED | 0 | OK |  | ✅ |
| 128 | build-128-heart-far-from-me | AUTHORED | 0 | OK |  | ✅ |
| 129 | build-129-nazareth-only-a-few | AUTHORED | 0 | OK |  | ✅ |
| 130 | build-130-what-manner-of-spirit | AUTHORED | 0 | OK |  | ✅ |
| 131 | build-131-scribe-near-the-kingdom | AUTHORED | 0 | OK |  | ✅ |
| 132 | build-132-forbid-him-not | AUTHORED | 0 | OK |  | ✅ |
| 133 | build-133-what-jesus-called-hell | AUTHORED | 0 | OK |  | ✅ |
| 134 | build-134-today-in-paradise | AUTHORED | 0 | OK |  | ✅ |
| 135 | build-135-rainbow-covenant | AUTHORED | 0 | OK |  | ✅ |
| 136 | build-136-healed-in-two-touches | AUTHORED | 0 | OK |  | ✅ |
| 137 | build-137-one-as-we-are-one | AUTHORED | 0 | OK |  | ✅ |
| 138 | build-138-his-offspring | AUTHORED | 0 | OK |  | ✅ |
| 139 | build-139-lamp-on-a-stand | AUTHORED | 0 | OK |  | ✅ |
| 140 | build-140-naaman-washes | AUTHORED | 0 | OK |  | ✅ |
| 141 | build-141-bread-of-life | AUTHORED | 0 | OK |  | ✅ |
| 142 | build-142-light-of-the-world | AUTHORED | 0 | OK |  | ✅ |
| 143 | build-143-i-am-the-door | AUTHORED | 0 | OK |  | ✅ |
| 144 | build-144-resurrection-and-the-life | AUTHORED | 0 | OK |  | ✅ |
| 145 | build-145-way-truth-life | AUTHORED | 0 | OK |  | ✅ |
| 146 | build-146-vine-and-branches | AUTHORED | 0 | OK |  | ✅ |
| 147 | build-147-joseph-forgives | AUTHORED | 0 | OK |  | ✅ |
| 148 | build-148-ruth-and-the-redeemer | AUTHORED | 0 | OK |  | ✅ |
| 149 | build-149-hannah-is-heard | AUTHORED | 0 | OK |  | ✅ |
| 150 | build-150-shepherd-psalm | AUTHORED | 0 | OK |  | ✅ |
| 151 | build-151-ask-of-god | AUTHORED | 0 | OK |  | ✅ |
| 152 | build-152-revealeth-his-secret | AUTHORED | 0 | OK |  | ✅ |
| 153 | build-153-restitution | AUTHORED | 0 | OK |  | ✅ |
| 154 | build-154-everlasting-gospel | AUTHORED | 0 | OK |  | ✅ |
| 155 | build-155-falling-away | AUTHORED | 0 | OK |  | ✅ |
| 156 | build-156-famine-of-hearing | AUTHORED | 0 | OK |  | ✅ |
| 157 | build-157-marvellous-work | AUTHORED | 0 | OK |  | ✅ |
| 158 | build-158-two-sticks | AUTHORED | 0 | OK |  | ✅ |
| 159 | build-159-other-sheep | AUTHORED | 0 | OK |  | ✅ |
| 160 | build-160-stone-cut | AUTHORED | 0 | OK |  | ✅ |
| 161 | build-161-called-of-god | AUTHORED | 0 | OK |  | ✅ |
| 162 | build-162-keys-of-kingdom | AUTHORED | 0 | OK |  | ✅ AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0): fresh 24-beat map written from scratch (Matthew 16:13-19, Peter's confession + "upon this rock" + the keys, all at Caesarea Philippi). Movie coverage — ONE establishing wide (b01), the rest singles/two-shots/inserts; Peter locked (canonical cast), the keys locked as ONE object (two iron ward-keys), the Father NEVER embodied (b06/b22). Speaker law honoured: s16 confession on PETER (b04), kv19 bind/loose cuts to Peter receiving the keys (b19). `v2_prompt.py --check` PASS, windows contiguous+monotonic (0.280→144.784=card), audio OK. **NEW place CAESAREA-ROCK** — RUNNER must gen b01 FIRST, `--promote` it as the plate, then gen the other 23 (steps in QC.md). No open complaint. See QC.md. |
| 163 | build-163-apostles-prophets | AUTHORED | 0 | OK |  | ✅ AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0): fresh 18-beat map (Ephesians 2:19-20). Follows Paul's own hinge — FAMILY/household half (outsiders → door opened → drawn in → household of God) then BUILD-SITE half (foundation → apostles/prophets → cornerstone → living people fitted in), with **Christ at the cornerstone** (b12/b13, locked Jesus + REF, ordinary-sized). Bookend: the b02 longing outsider ends up INSIDE the doorway (b16). Father NOT depicted. `--check` PASS, windows contiguous (0.280→116.714=card), audio OK. **6 NEW places** — RUNNER promotes each from this build's first good frame (table in QC.md; optional build-41 FAMILY reuse noted). See QC.md. |
| 164 | build-164-unity-of-faith | AUTHORED | 0 | OK |  | ✅ AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0): fresh 25-beat map (Ephesians 4:11-14). Movie coverage ~5.0s/pic; ONE establishing wide (b01), rest singles/two-shots/inserts. SPEAKER LAW — epistle, NO Jesus red-letter: kv11/kv13/s14 all SCRIPTURE (light-blue) on the people/leaders, never on Jesus. Jesus embodied ONLY b01-b03 (risen Lord gives the gifts) + b25 (invitation); Son-of-God/heaven NEVER embodied for measure (b11/b13/b14 keep him as distant light, no giant Christ). Deceivers locked visibly finer/smoother than the true ministers (b16/b19). `--check` PASS, windows contiguous+monotonic (0.280→124.389=card), every onset in-window, audio OK. **2 NEW places** — RUNNER promotes GATHERING-HILL from NON-Jesus b13 + JOURNEY-ROAD from b10 (never a Jesus frame); steps in QC.md. No open complaint. |
| 165 | build-165-laying-on-hands | AUTHORED | 0 | OK |  | ✅ AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0): fresh 25-beat map (Acts 8:14-17, Samaria receives the Holy Ghost by the apostles' hands). NARRATIVE — Peter & John (global cast, beard-boarded), Samaritan BELIEVERS + Jerusalem APOSTLES council locked. SPEAKER LAW: Luke's Acts, NO red-letter — kv14/s15/s16/kv17 all SCRIPTURE; **NO Jesus in the scene, every beat jesus=False, nobody in cream**. HARD GATE: the Holy Ghost NEVER embodied — warm light from above only, no dove/flame/figure (b18/b19/b21/b24); b10/b11 keep the air EMPTY ("fallen upon none yet"). Laying-on-of-hands covered as a 4-beat SEQUENCE (b16-b19). `--check` PASS, windows contiguous+monotonic (0.280→119.606=card), every onset in-window, cast locks resolve, audio OK. **2 NEW places** (SAMARIA-HILL, JERUSALEM-ROOM) — runner promote plan in QC.md. No open complaint. |
| 166 | build-166-baptized-properly | AUTHORED | 0 | OK |  | ✅ AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0): fresh 24-beat map (Acts 19:1-6, Paul at Ephesus — John's-baptism disciples rebaptized in the name of the Lord Jesus, then hands laid, Holy Ghost + tongues). Companion to row 165. PAUL locked BYTE-IDENTICAL to builds 138/155 (cross-video same man); EPHESIAN-DISCIPLES locked. SPEAKER LAW: Luke's Acts, NO red-letter — s2/s4/kv5/kv6 all SCRIPTURE (s2/s4 = Paul's words, not Jesus-red); **NO Jesus in-scene, every beat jesus=False, nobody in cream**. HARD GATE: Holy Ghost never embodied AND tongues are NOT flames — b18 shows the men's own praise/prophecy, warm light from above only (no dove/flame/figure); b12/b15 keep the air empty. `--check` PASS, windows contiguous+monotonic (0.280→121.218=card), onsets in-window, Paul lock on all 12 Paul beats, audio OK. **1 NEW place** (EPHESUS-ROOM) — runner promote plan in QC.md. No open complaint. |
| 167 | build-167-chosen-ordained | AUTHORED | 0 | OK |  | ✅ AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0): fresh 24-beat map (John 15:16, "Ye have not chosen me, but I have chosen you, and ordained you..."). Milk→RESTORATION: a man CALLED of God and ORDAINED by the laying on of hands, authority heaven-down, a gift received not a badge taken — shown through Jesus's own words + his own hands, church NEVER named, warm natural DAY (thematic, matches V1 stills; not the literal Last-Supper night). SPEAKER LAW: John red-letter — kv16a(b04/b05)+kv16b(b15/b16) are the only Jesus-VOICE beats on Jesus's face; Jesus ALSO embodied in the choose/call/ordain beats b06-b08,b21,b22; Father NEVER embodied (light at top edge only, b06/b16/b18/b19). Ordination covered as a SEQUENCE (lesson 12): choose→lay hands→heaven-down→call by name→set apart→rise to go. `--check` PASS, windows contiguous+monotonic (0.280→117.943=card), every onset in-window, audio OK. **4 NEW places** (LAKESHORE bookend, TEACHING-HILL, VILLAGE-ROAD, HARVEST-FIELD) — runner promotes each from its first NON-Jesus frame (never a Jesus frame); optional cross-video landscape plates noted. No open complaint. See QC.md. |
| 168 | build-168-born-water-spirit | NEEDS-BEATS | 0 | OK |  |  |
| 169 | build-169-fulfil-righteousness | NEEDS-BEATS | 0 | OK |  |  |
| 170 | build-170-sacrament-worthily | NEEDS-BEATS | 0 | OK |  |  |
| 171 | build-171-baptized-for-the-dead | NEEDS-BEATS | 0 | OK |  |  |
| 172 | build-172-gospel-preached-to-the-dead | NEEDS-BEATS | 0 | OK |  |  |
| 173 | build-173-dead-shall-hear | NEEDS-BEATS | 0 | OK |  |  |
| 174 | build-174-hearts-of-the-fathers | NEEDS-BEATS | 0 | OK |  |  |
| 175 | build-175-mountain-of-the-lords-house | NEEDS-BEATS | 0 | OK |  |  |
| 176 | build-176-who-shall-ascend | NEEDS-BEATS | 0 | OK |  |  |
| 177 | build-177-make-me-a-sanctuary | NEEDS-BEATS | 0 | OK |  |  |
| 178 | build-178-in-our-image | NEEDS-BEATS | 0 | OK |  |  |
| 179 | build-179-stephens-witness | NEEDS-BEATS | 0 | OK |  |  |
| 180 | build-180-before-i-formed-thee | NEEDS-BEATS | 0 | OK |  |  |
| 181 | build-181-morning-stars-sang | NEEDS-BEATS | 0 | OK |  |  |
| 182 | build-182-spirit-returns-to-god | NEEDS-BEATS | 0 | OK |  |  |
| 183 | build-183-sun-moon-and-stars | NEEDS-BEATS | 0 | OK |  |  |
| 184 | build-184-third-heaven | NEEDS-BEATS | 0 | OK |  |  |
| 185 | build-185-many-mansions-member | NEEDS-BEATS | 0 | OK |  |  |
| 186 | build-186-joint-heirs | NEEDS-BEATS | 0 | OK |  |  |
| 187 | build-187-ye-are-gods | NEEDS-BEATS | 0 | OK |  |  |
| 188 | build-188-be-ye-therefore-perfect | NEEDS-BEATS | 0 | OK |  |  |
| 189 | build-189-to-him-that-overcometh | NEEDS-BEATS | 0 | OK |  |  |
| 190 | build-190-faith-without-works | NEEDS-BEATS | 0 | OK |  |  |
| 191 | build-191-windows-of-heaven | NEEDS-BEATS | 0 | OK |  |  |
| 192 | build-192-the-fast-god-has-chosen | NEEDS-BEATS | 0 | OK |  |  |
| 193 | build-193-the-comforter | NEEDS-BEATS | 0 | OK |  |  |
| 194 | build-194-fruit-of-the-spirit | NEEDS-BEATS | 0 | OK |  |  |
| 195 | build-195-prove-all-things | NEEDS-BEATS | 0 | OK |  |  |
| 196 | build-196-would-god-all-were-prophets | NEEDS-BEATS | 0 | OK |  |  |
| 197 | build-197-sons-and-daughters-prophesy | NEEDS-BEATS | 0 | OK |  |  |
| 198 | build-198-ensign-for-the-nations | NEEDS-BEATS | 0 | OK |  |  |
| 199 | build-199-fishers-and-hunters | NEEDS-BEATS | 0 | OK |  |  |
| 200 | build-200-gospel-to-all-the-world | NEEDS-BEATS | 0 | OK |  |  |
