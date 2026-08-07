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
| 18 | build-18-emmaus | NEEDS-AUDIO | 41 | CHECK | C-FIX 2026-08-07 PARKED NEEDS-AUDIO: OPEN complaint is AUDIO-pronunciation — narrator mispronounces "Jesus's" (possessive) in n0 ("two of Jesus's followers", ~0:04); SPOKEN dict empty, no fix baked in, runner cannot re-voice (audio-immutability). AUTHOR: set SPOKEN={"Jesus's":"jeezusiz"} in make_narration.py, regenerate n0.mp3, re-assemble. See QC.md §0 RUNNER PARK. · AUDIO-FIX 2026-08-07 LIVE (Machine A `Dev`) |  |
| 19 | build-19-shore | BUILT | 37 | OK | AUDIO-FIX 2026-08-07 DONE (Machine A `Dev`): complaint (A) "JESUS talks too fast / ignores commas" FIXED — j1 re-voiced through the locked ElevenLabs JESUS voice, 2.04s→3.29s (both commas now breathe, no robotic dead-air), AUDIO_FROM_V1_SEGMENTS=True set so the re-cut rebuilds the fixed j1. Live cut NOT re-shipped on purpose (its complaint must still match the live hash so the picture lane owns it). **PICTURE C-FIX PENDING (B):** reroll beat v2-r019-b17/s17 (Peter swims toward the beach at 1:05, CAMERON GATE) + re-cut over the new audio + ship — ONE touch-once re-cut closes BOTH. Do NOT re-park to NEEDS-AUDIO (audio already fixed at source). See QC.md §0 green block. |  |
| 20 | build-20-samaritan | BUILT | 42 | OK |  |  |
| 21 | build-21-lost-sheep | BUILT | 33 | OK |  |  |
| 22 | build-22-unmerciful-servant | BUILT | 48 | OK | AUDIO-FIX 2026-08-07 SHIPPED (Machine A `Dev`): complaint "2:46 Jesus mispronounces shouldest it should be should-est" FIXED — added SPOKEN {"shouldest":"should-est"}, re-voiced ONLY j5.mp3 (edge-tts, $0), other 24 segments byte-identical. A/B-confirmed the two-part SHOULD-est reading. AUDIO_FROM_V1_SEGMENTS=True + beats_v2 still-windows remapped for the +0.17s j5 shift (spoken-trimmed, not the raw +0.895s). Realistic 48-still V2 pictures UNCHANGED, 0 rerolls. AUDIO REBUILD PASS 20a6ef72, 225.2s. Reviewer card + cache-buster ?v=6e6943d8c0dc updated, deployed + live-verified. See QC.md ✅ RESOLVED. |  |
| 23 | build-23-vineyard | BUILT | 40 | OK |  |  |
| 24 | build-24-sower | BUILT | 35 | OK |  |  |
| 25 | build-25-wheat-and-tares | BUILT | 33 | OK |  |  |
| 26 | build-26-mustard-seed | BUILT | 24 | OK |  |  |
| 27 | build-27-leaven | NEEDS-AUDIO | 29 | CHECK | C-FIX 2026-08-07 PARKED NEEDS-AUDIO: OPEN complaint is generic AUDIO-domain — Cameron "Audio is messed up on this one." Runner cannot re-voice (audio-immutability); all 11 segments render at correct durations & A/V is aligned (104.47s), so it's a delivery defect inside the spoken narration, not a truncation. AUTHOR: listen to matthew-13_leaven.mp4, localize the bad segment(s), fix at make_narration.py (respell or re-render the glitchy TTS take), regenerate only that mp3, re-assemble, ship via C-FIX. No picture defect — audio only, $0 spent. See QC.md §0 RUNNER PARK. |  |
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
| 59 | build-59-feeding-4000 | NEEDS-REBUILD | 27 | OK | AUTHOR-DONE 2026-08-07 (Machine A `Dev`): SECOND-FEEDING scholarship complaint ANSWERED in narration, $0/0 credits. n2b now names it plainly as a distinct SECOND feeding ("working the very same sums a second time"); n5 draws the 5-loaves→12-baskets (Matt 14) vs 7-loaves→7-baskets (Mark 8) comparison AND cites that Jesus himself made the disciples count BOTH (Mark 8:19-21 / Matt 16:9-10). Edited V1+V2 make_narration, re-voiced ONLY n2b+n5 (free edge-tts AndrewNeural), added 2 scholarship beats (b13b/b23b) REUSING existing stills s12/s16 — no new image. Timeline remapped 172.5→207.3s, all 29 windows contiguous, --check PASS. Re-assembled locally (stills done). RUNNER: verify the new mp4, deploy, ship with a card telling Cameron his complaint was addressed. See QC.md "AUTHOR DONE". | ✅ |
| 60 | build-60-gerasene-demoniac | BUILT | 39 | OK | A-auto 2026-08-06 SHIPPED · C-FIX 2026-08-07 LIVE | ✅ |
| 61 | build-61-syrophoenician-woman | BUILT | 31 | OK | AUDIO-FIX 2026-08-06 SHIPPED — STALE-V1 lock cleared (AUDIO_FROM_V1_SEGMENTS=True), audio rebuilt from 15 new-voice segments, realistic-V2 cut 185.2s/21.2MB assembled + deployed + live-verified. mp4 SHA256 106884ad. See QC.md "AUDIO FIX DONE". | ✅ |
| 62 | build-62-ephphatha | RUNNING | 0 | OK | A-auto 2026-08-06 LIVE | ✅ |
| 63 | build-63-man-born-blind | RUNNING | 0 | OK | A-auto 2026-08-06 | ✅ |
| 64 | build-64-pool-of-bethesda | BUILT | 41 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 65 | build-65-help-mine-unbelief | BUILT | 36 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 66 | build-66-malchus-ear | BUILT | 29 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 67 | build-67-the-transfiguration | BUILT | 16 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 68 | build-68-multitudes-mountain | BUILT | 35 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 69 | build-69-baptism | BUILT | 29 | OK | AUDIO-FIX shipped 2026-08-06 da00221e35d6 — STALE-V1 lock cleared (AUDIO_FROM_V1_SEGMENTS), new-voice cut assembled 172.3s, deployed+live-verified. | ✅ |
| 70 | build-70-temptations | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — Cameron complaints "narrator spells 'I-S'" + "'proceedeth' should be pro-see-duhth" CLOSED: n2 re-voiced (caps IS/IF now spoken as words, caption keeps caps), j1 re-voiced ("proceeduth" → whisper-verified pro-see-duhth), same Andrew/Eric voices; other 20 mp3s byte-identical. $0 (edge-tts). 0 V2 stills → picture runner builds on corrected audio; COMPLAINT LEDGER in QC.md for its review card. See QC.md "AUDIO FIX DONE". |
| 71 | build-71-the-great-commission | BUILT | 21 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 72 | build-72-calling-matthew | BUILT | 41 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 73 | build-73-this-day-fulfilled | BUILT | 17 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 74 | build-74-woman-washed-his-feet | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1 audio-lock cleared (AUDIO_FROM_V1_SEGMENTS); 19/19 new-voice segments verified. 0 stills → picture runner builds on corrected audio. See QC.md "AUDIO FIX DONE". |
| 75 | build-75-woman-taken-in-adultery | BUILT | 21 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 76 | build-76-suffer-the-little-children | BUILT | 14 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 77 | build-77-widows-mite | NEEDS-AUDIO | 16 | CHECK | AUDIO-FIX 2026-08-06 LIVE — A-auto 2026-08-06 PARKED: 16 stills GENERATED + QC-PASS (1 reroll b04 collage), but v2_assemble AUDIO LOCK fails — extracted timeline 98.846s vs V1 final 97.106s (1.74s short, over the abs>1.0 tolerance, line 531); newer_mp3s=0 so not recency-stale, just a duration mismatch. Runner can't edit beats_v2.py. Author: set AUDIO_FROM_V1_SEGMENTS=True then re-assemble (stills present, do NOT regen). See QC.md RUNNER PARK. |  |
| 78 | build-78-who-is-my-mother | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1 audio-lock CLEARED (AUDIO_FROM_V1_SEGMENTS=True): V1 mp4 stale vs 11 re-voiced mp3s; v2_assemble now clears the audio gate (stops only on missing stills), 11/11 segment parity. $0, nothing re-voiced. 0 V2 stills → picture runner generates + assembles on corrected new-voice audio. Same mechanism as shipped row 69. See QC.md "AUDIO FIX DONE". |
| 79 | build-79-the-seventy-sent | BUILT | 19 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 80 | build-80-come-unto-me | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1 audio-lock CLEARED (AUDIO_FROM_V1_SEGMENTS=True): V1 mp4 stale vs 11 re-voiced mp3s; v2_assemble now clears the audio gate (stops only on missing stills), 11/11 segment parity. $0, nothing re-voiced. 0 V2 stills → picture runner generates + assembles on corrected new-voice audio. Same mechanism as shipped row 69. See QC.md "AUDIO FIX DONE". |
| 81 | build-81-render-unto-caesar | BUILT | 16 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 82 | build-82-anointing-at-bethany | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1 audio-lock CLEARED (AUDIO_FROM_V1_SEGMENTS=True): V1 mp4 failed both tripwires (19 newer mp3s + +7s excess); v2_assemble now clears the audio gate (stops only on missing stills), 19/19 segment parity. $0, nothing re-voiced. 0 V2 stills → picture runner generates + assembles on corrected new-voice audio. See QC.md "AUDIO FIX DONE". |
| 83 | build-83-weeping-over-jerusalem | AUTHORED | 0 | OK |  | ✅ AUDIO-FIX DONE 2026-08-06 — STALE-V1 audio-lock CLEARED (AUDIO_FROM_V1_SEGMENTS=True): V1 mp4 runtime tripwire (|Δ|~2.2s); v2_assemble now clears the audio gate (stops only on missing stills), 10/10 segment parity. $0, nothing re-voiced. 0 V2 stills → picture runner generates + assembles on corrected new-voice audio. See QC.md "AUDIO FIX DONE". |
| 84 | build-84-no-room-manger | RUNNING | 0 | OK | A-auto 2026-08-06 LIVE | ✅ |
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
| 102 | build-102-jacobs-ladder | BUILT | 28 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 103 | build-103-peters-confession | BUILT | 20 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 104 | build-104-boy-samuel | BUILT | 22 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 105 | build-105-face-to-face | NEEDS-AUDIO | 0 | CHECK | A-auto 2026-08-06 PARKED ($0 pre-flight): STALE-V1-FINAL — V1 mp4 rendered 2026-07-24, all 18 mp3s NEWER (2026-07-29); recency gate refuses AUDIO LOCK. Author: set AUDIO_FROM_V1_SEGMENTS=True in beats_v2.py. See QC.md RUNNER PARK. |  |
| 106 | build-106-god-spake-by-prophets | NEEDS-AUDIO | 0 | CHECK | A-auto 2026-08-06 PARKED ($0 pre-flight): STALE-V1-FINAL, BOTH gates — |Δ|=6.61s AND all mp3s NEWER than the 2026-07-24 V1 mp4. Author: set AUDIO_FROM_V1_SEGMENTS=True in beats_v2.py. See QC.md RUNNER PARK. |  |
| 107 | build-107-john-baptist-doubt | BUILT | 25 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 108 | build-108-my-sheep-hear-my-voice | NEEDS-AUDIO | 0 | CHECK | A-auto 2026-08-06 PARKED ($0 pre-flight): STALE-V1-FINAL, BOTH tripwires — RECENCY all 14/14 mp3s NEWER than 2026-07-24 V1 mp4, AND |Δ|=2.13s>1.0. Board said OK but pre-flight is authoritative. Author: set AUDIO_FROM_V1_SEGMENTS=True in beats_v2.py. See QC.md RUNNER PARK. |  |
| 109 | build-109-ask-seek-knock | BUILT | 23 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 110 | build-110-lords-prayer | BUILT | 23 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 111 | build-111-lilies-and-sparrows | BUILT | 29 | OK | A-auto 2026-08-06 SHIPPED | ✅ |
| 112 | build-112-beatitudes | RUNNING | 0 | OK | A-auto 2026-08-06 | ✅ |
| 113 | build-113-where-art-thou | NEEDS-AUDIO | 26 | CHECK | A-auto 2026-08-06 PARKED ($4.14 art, all 26 stills DONE+QC-PASS, GOD embodied per complaint): v2_assemble FAILS AUDIO LOCK — STALE-V1-FINAL, V1 mp4 (193.3s, 07-29 09:47) is stale vs 15 re-voiced mp3s (07-29 23:03), timeline 163.1s. Runner can't edit beats_v2.py. Author: set AUDIO_FROM_V1_SEGMENTS=True then re-assemble (stills reusable, do NOT regen). See QC.md RUNNER PARK. |  |
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
| 162 | build-162-keys-of-kingdom | NEEDS-BEATS | 0 | OK |  |  |
| 163 | build-163-apostles-prophets | NEEDS-BEATS | 0 | OK |  |  |
| 164 | build-164-unity-of-faith | NEEDS-BEATS | 0 | OK |  |  |
| 165 | build-165-laying-on-hands | NEEDS-BEATS | 0 | OK |  |  |
| 166 | build-166-baptized-properly | NEEDS-BEATS | 0 | OK |  |  |
| 167 | build-167-chosen-ordained | NEEDS-BEATS | 0 | OK |  |  |
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
