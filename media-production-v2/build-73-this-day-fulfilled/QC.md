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
