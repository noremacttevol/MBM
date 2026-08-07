# QC / RUNNER HANDOFF — build-73-this-day-fulfilled (Luke 4:16-21)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 17 beats, ~103 s.

## ⚑ OPEN COMPLAINT ON THIS EXACT ROW (Cameron):

> "are you kiding me it jsut pronounced 'Esaias' as 'essy-y-es'. this
> is rediculous"

Audio gate: verify the locked narration pronounces Esaias correctly
(eh-ZY-us / ee-ZAY-us family — NEVER letter-by-letter). If wrong,
NEEDS-AUDIO and stop. This joins the pronunciation dictionary class —
fix-the-class-once applies.

## ⚠ SYNAGOGUE plate UNWIRED on purpose — third wrong-plate catch

The stash matched build-05's CAPERNAUM hall by token name — but this is
the NAZARETH synagogue, his hometown's own building. Rows 52/55
rightly share Capernaum's hall; this row must NOT. Promote-first from
b01, and the approved Nazareth hall MUST seed row 129
(nazareth-only-a-few — the same room, the same story continued).

## Coverage shape

Three true wides with stated geometry: b01 (the customary entering, in
profile), b06 (the reading over the room, camera behind the seated
shoulders — the row's 21-second centerpiece), b12 (the fastened eyes,
camera just behind his seated shoulder — every face in the room on
him). Five flips.

## The scroll (prop law)

The Isaiah SCROLL is hand-inked Hebrew on parchment (the one lawful
writing per the shared materials lock) — wrapped, unrolled, read,
rolled, returned: one scroll through five states; its handling order
in b07 is scripture (closed → given to the minister → he sat down).
No lettering readable as modern text.

## The room's arc (the whole video is one held breath)

Entering → reading (STANDING) → sitting → fastened eyes → "this day"
(SEATED — the posture flip between reading and declaring is Luke's own
detail; never render him standing for the declaration). The
congregation's leaning arc builds one direction to the after-silence.
Faces varied (90/107): these are his HOMETOWN neighbors — recognition
and wonder, not strangers' awe.

- Only Jesus wears cream.

## COMPLAINT LEDGER + RUNNER QC (2026-08-06 A-auto, Machine A / Dev)

OPEN complaint (v2_outline): "it just pronounced 'Esaias' as 'essy-y-es'.
this is ridiculous."
  → ALREADY FIXED IN THE BAKED AUDIO — the runner ships it, does NOT re-voice.
  Proof (row-57 exception, all four conditions met):
  1. Board Audio column = OK (not CHECK).
  2. SPOKEN override present & voice-scoped: make_narration.py
     "Esaias": "eh-ZAY-us"; mbm_pronounce.py "Esaias": {"scripture":"izayus"}.
  3. Verified-fix commit a53cadcbe (Jul 22): "Pronunciation fix ... is now
     actually in the video ... 'Esaias' ... transcribes back as the right word."
  4. V1 mp4 luke-4_this-day-fulfilled.mp4 (Jul 29 09:47) was rendered AFTER all
     narration re-records (Jul 22/25/28) → the corrected line is in the mp4.
  The assembler's AUDIO LOCK PASS is the cryptographic proof the shipped audio
  is byte-identical to that corrected V1 mp4. The review card tells Cameron his
  Esaias complaint is fixed and that he can hear it in the reading line.

RUNNER QC (17 beats, 0 portraits — cast sheets reused):
- SYNAGOGUE promote-first from THIS row's b01 (Nazareth's own hall). The
  auto-wire suggested build-52's CAPERNAUM hall — REFUSED per QC.md + row-59
  lesson (token-match is blind to region). PLACE-WIRING started empty {}.
- POSTURE LAW verified: Jesus STANDS to read (b06 centerpiece) and SITS to
  declare (b14/b15/b16) — Luke's own detail, never standing for "this day."
- Scroll prop: hand-inked illegible Hebrew on parchment, one scroll through its
  states; NO readable modern text, NO burned-in caption on any reading beat.
- Only Jesus in cream; no halo/glow; scale correct; faces varied hometown
  neighbors (recognition/wonder, not strangers' awe).
- REROLLS: 2 of 17 beats (11.8%, under the 15% COST LAW budget):
  b07 (s07 closed-book) came back a 3-panel vertical collage of the
  closed→gave→sat sequence → reroll landed a clean single; b09 (s09 Isaiah
  reading) came back a 2-panel collage → reroll landed a clean scroll still-life.
- FIX-WAVE (subtle drift, NOT rerolled — budget spent on the collages):
  (a) b10 (s10 "not someday") floor is wooden planks where every other synagogue
  frame is stone flagstone — minor atmospheric insert, place inconsistency only;
  (b) b09 background has a light/white-painted window frame that leans slightly
  modern — minor, the scroll subject itself is period-correct.
- Spend this row: ~$2.53 (b01 + 16-batch + 2 rerolls, 0 portraits). Well under
  the $6.10/row baseline; reroll % 11.8% under the 19% baseline. COST LAW: down.

────────────────────────────────────────────────────────────────────────
RUNNER PARK — 2026-08-07 (Machine A `Dev`) — NEEDS-REBUILD (author lane)
────────────────────────────────────────────────────────────────────────
Cameron filed a complaint against the shipped v73 cut. Read in full via
`python3 media-production-v2/v2_outline.py 73`. His words:

  "the first 2 pictures make Jesus look one way and then another. the entire
   messge from this [isn't] giving the fullnes of his message. it should teach
   people how He meant what he said and not jsut 'he still reads it the same'
   [but that] he has risen and continues the plan. we need to start looking at
   this how the prophets of then and the restored church today the Church of
   Jesus Christ of Latter Day Saints would share these messages. obviously
   without telling it that its that church that is makingit so but just teaching
   how we know Jesus would want us to."

WHY THIS IS A PARK, NOT A RUNNER C-FIX
--------------------------------------
The DOMINANT thrust is an AUTHOR content rebuild — exactly the class in
RUNNER-LESSONS §511 ("a complaint asking for ADDED scholarship / teaching /
'tell it differently' is an AUTHOR content rebuild, NOT a runner reroll or an
audio re-voice"). The runner may not edit scene text or beat content, and no
picture reroll touches the message. The narration currently reports the event
("this day is this scripture fulfilled … he still reads it the same"); Cameron
wants it to TEACH the fullness — that Jesus meant every word, that He has risen
and continues the same plan today, in the voice/frame the prophets and the
restored Church of Jesus Christ would use, WITHOUT ever naming that church.
That changes the beat map (rewritten narration, likely 1-2 added teaching
beats). Author domain.

Shipping a picture-only fix would leave the message complaint OPEN — the worst
failure this pipeline can produce. So: park, $0, pictures + audio byte-identical.

FOR THE AUTHOR (both parts of the complaint — batch into ONE rebuild)
--------------------------------------------------------------------
1. MESSAGE (primary): rewrite the narration so it teaches the fullness of the
   Nazareth-synagogue moment — not "he still reads it the same" but that the
   scripture He read (Isaiah 61) is His own mission statement, that He is risen
   and STILL fulfilling that same plan today, taught the way living prophets /
   the restored Church would teach it, WITHOUT naming the church. Keep it milk,
   let Jesus's own words carry it (Two-Voice law intact).
2. PICTURE (secondary, cured by the rebuild): the opening Jesus face drifts.
   Confirmed by viewing — s01-he-came-back-to-nazareth: lighter brown wavy
   hair, softer/lighter face; s02-and-there-was-delivered-unto: near-black
   thicker hair, fuller darker beard, different face shape/skin. They read as
   two different men. Lock the JESUS-MASTER-REF face across the opening beats
   in the rebuild (attach REF + JESUS LOCK v3 to every opening Jesus shot; run
   jesus_face_gate before ship).

STATE: AUTHOR-BOARD row 73 → NEEDS-REBUILD, Ready empty. Author lane picks it
up next (LOW-NUMBER LAW: low rows first). $0 spent, 0 pictures touched, audio
byte-identical.

✅ AUTHOR DONE — FULLNESS REBUILD — 2026-08-07 (Machine A `Dev`, Fable-5 author lane)
────────────────────────────────────────────────────────────────────────
Both halves of Cameron's complaint are addressed in the author files. $0 image
gen; ~cents ElevenLabs. Only PAID image steps remain (below) → handed to the
picture runner. AUTHOR-BOARD row 73 → Ready ✅.

WHAT THE AUTHOR CHANGED
-----------------------
1. MESSAGE (primary complaint — "give the fullness"). The old ending only
   REPORTED the event and closed on "He still reads it as today." Re-authored so
   the narrator now TEACHES what his own words meant, that He is risen, and that
   the same plan continues today — in the prophets'/restored-Church frame, the
   Church never named. Two-Voice law untouched: NO new words in Jesus's mouth
   (j1/j2 remain his only lines); the fullness is carried by the narrator opening
   up his own declaration. Milk; ends on a personal invitation.
     • NEW segment n4 (narrator): "He was not reading someone else's words — that
       was his own mission, spoken in his own mouth, the Anointed One saying out
       loud what he had come to do. And he did it: he healed the broken, opened
       blind eyes, and carried freedom to the very people the world had written off."
     • NEW segment n5 (narrator): "They killed him for it — but on the third day
       he rose, and the work he began in that little room did not end at an empty
       tomb. He is alive, the same Spirit is still upon him, and the good news he
       read that morning is going out into the world again in our own day — the
       year of the Lord's favor has never once closed."
     • CARD rewritten from "He still reads it as today…" → "He read it as today
       because, for him, it still is. The risen Lord is keeping every line of that
       promise even now — and one of them was written with you in mind. What would
       it mean if he were reading it, today, over your life?"
   Edited in V1 make_narration.py (SEGMENTS) + V1 build.py (BEATS gained n4/n5 so
   extract_beats places them). Mirrored in V2 make_narration.py.

2. AUDIO — engine-matched, NOT edge-tts. The delivered narration on this row is
   ElevenLabs (44.1 kHz), so n4/n5/card were re-voiced through the SAME ElevenLabs
   NARRATOR (Brian) via mbm_eleven.render_segment — never edge-tts (that would
   swap the narrator voice mid-video, the row-18 lesson). Whisper round-trip on all
   three came back verbatim ("the anointed one", "read that morning", "year of the
   Lord's favor"). n4=16.20s, n5=18.99s, card=14.05s. The other 8 segments are
   byte-identical (untouched). beats_v2.py now sets AUDIO_FROM_V1_SEGMENTS = True
   so the runner's assemble rebuilds the track from the V1 mp3s at the
   extract_beats offsets. New total 154.322 s (card_start 138.890) — was ~103 s;
   the +51 s is the added teaching + longer card, which is the point.

3. PICTURES (secondary complaint — opening Jesus face drift + coverage of the new
   teaching). beats_v2.py: 21 beats, --check PASS, schedule contiguous/monotonic
   to card_start. COST LAW held — the 4 teaching beats add only ONE new still:
     • b18 (n4) REUSES approved s06 (the standing reading) — his own mission.
     • b19 (n4) REUSES approved s09 (the receiving faces) — "and he did it."
     • b20 (n5) REUSES approved s16 (the seated Christ) — "he rose… alive."
     • b21 (n5) NEW still s18-going-out-today.jpeg — the open synagogue door onto
       the sunlit Nazareth road, the good news going out "today." No Jesus figure
       (no face risk); realistic, period-locked.
   Imagery stays inside the synagogue on purpose — no passion/tomb scene invented
   (scene jump + a new locked-Jesus scene + face-drift risk + more credits). The
   narrator carries the death-and-resurrection; the picture holds the living Christ.

🅿️ RUNNER — the remaining PAID steps (batch into ONE re-cut, touch once)
------------------------------------------------------------------------
1. Generate the ONE new still: `s18-going-out-today.jpeg` (b21 prompt in
   ASSEMBLED-PROMPTS.txt). No Jesus in frame — no face gate needed on it.
2. FACE-DRIFT FIX (Cameron's part 2): reroll the opening frames that drift —
   `s01-he-came-back-to-nazareth.jpeg` and `s02-and-there-was-delivered-unto.jpeg`.
   Compare BOTH against JESUS-MASTER-REF/jesus-face.jpeg AND against a known-good
   Jesus frame in this build (s16); keep whichever already matches and reroll only
   the drift(s) to save a credit. `python3 media-production/jesus_face_gate.py
   --dir <build>` must exit 0 before assembly (FACE-BOARD LAW).
   NOTE: PLACE-REF/synagogue.jpeg is architecture-only — the s01 reroll does NOT
   require re-promoting the plate; leave it.
3. `python3 media-production-v2/v2_assemble.py 73` — from-segments audio rebuild
   (AUDIO_FROM_V1_SEGMENTS). AUDIO REBUILD must PASS at ~154.322 s.
4. Re-run `python3 media-production-v2/audio_audit.py 73` on the new cut (new
   narrator segments were whisper-verified at author time; confirm A/B/C stay 0).
5. Deploy + live-verify; set Appr/Post per the C-FIX flow.

COMPLAINT LEDGER — the review card must tell Cameron, in his words, both are fixed
-----------------------------------------------------------------------------------
1. "the entire message isn't giving the fullness of his message… teach how He MEANT
   it… He has risen and continues the plan… how the prophets/the restored Church
   would share it, without telling it that it's that church" → the video now teaches
   exactly that in the closing: Isaiah 61 was His OWN mission in His own mouth, He
   carried it out, He rose, and the same good news is going out again in our own day
   — framed the restored way, the Church never named, His own words still central.
2. "the first 2 pictures make Jesus look one way and then another" → the two opening
   frames are rerolled against the one locked master face and gate-checked so He is
   the same man in both.
