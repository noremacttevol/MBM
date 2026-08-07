# QC / RUNNER HANDOFF — build-168-born-water-spirit (John 3:1-5)

**AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).**
`beats_v2.py` written from scratch: 28 pictures over 127.21 s (~4.5 s/pic,
matches rows 161-167 library density; lesson-12 movie coverage of a dialogue
plus its illustrations). `v2_prompt.py --check` PASS (no warnings). Windows
contiguous + monotonic, first 0.280, last end 127.212 = card seg_start; every
segment onset falls inside its first beat's window. Audio column OK on
AUTHOR-BOARD. Ready ✅.

## COMPLAINT LEDGER
- **No open Cameron complaint on this row** (`v2_outline.py 168` shows no prior
  review). First V2 authoring, not a complaint fix.

## SPEAKER LAW — only kv3b + kv5b are Jesus's voice; s4 sits on NICODEMUS
John's gospel, RED-LETTER. Jesus-VOICE beats (jesus=True on Jesus's face):
**kv3b** (b08/b09) and **kv5b** (b21/b22). The attribution segments **kv3** (b07)
and **kv5** (b20) — "Jesus answered..." — are the SCRIPTURE voice / light-blue
caption; the PICTURE shows Jesus about to answer (jesus=True), the caption is not
red. **s4** (b10/b11) is the SCRIPTURE voice reading **Nicodemus's** question
("How can a man be born when he is old?") — so those beats sit on **Nicodemus's**
face, jesus=False (the row-39 lesson: a quoted line belongs to the man saying
it). Jesus is also embodied through the night narrator beats in the room (he is
physically teaching there): b04, b05, b06, b14, b23.

## HOLY GHOST / FATHER NEVER EMBODIED (hard gate — same as rows 165/166)
b17/b18/b19 ("born of the Spirit... gift of the Holy Ghost... a birth from above,
life breathed by heaven"): warm light and a stir of air coming DOWN from the top
edge of the frame ONLY. **NO dove, NO flame, NO figure, NO face in the sky.** The
change is shown on the human face, never as an effect. Same for the Father.

## TWO TIME-OF-DAY REGISTERS (intentional — not a continuity error)
The DIALOGUE is literal NIGHT (John 3:2 "came to Jesus by night") — the street
(b01/b02) and the room (b03-b14, b20-b24) are **NIGHT-LAMPLIGHT**: real darkness,
one small clay oil lamp, flame LOW and IN FRONT so no head is ever haloed (crown
+ back of every head stay dark). The metaphors Jesus explains are NOT in that
night room, so the video cuts to them as their own DAYTIME illustrations: the
river baptism (b15/b16, bright day), the Spirit from above on the same new
believer (b17-b19), and the open gate at dawn (b25-b28). The V1 stills chose the
same split.

## THE FOUR NEW PLACES — promote from NON-Jesus frames (lesson 11), never a Jesus frame
All four recurring places are NEW; carried by prose in `LOCKS` for their first
frame. Runner promotes each build-local plate, then wires the rest. `--promote
BUILD TOKEN ASSET` is positional; ASSET is the approved still filename.

1. **NIGHT-STREET** (b01, b02; both NON-Jesus). Promote **b01**:

       python3 media-production-v2/v2_stash.py --promote \
           build-168-born-water-spirit NIGHT-STREET s01-nicodemus-by-night.jpeg

   Auto-attaches to b02.

2. **NIGHT-ROOM** (b03-b14, b20-b24). The first frames are Nicodemus-alone or
   Jesus-bearing; promote the first clean **NON-Jesus** room frame **b10**
   (`s10-how-can-a-man-be-born.jpeg`, Nicodemus asking, no Jesus):

       python3 media-production-v2/v2_stash.py --promote \
           build-168-born-water-spirit NIGHT-ROOM s10-how-can-a-man-be-born.jpeg

   Auto-attaches to the other NON-Jesus room beats b11, b12, b13, b24. The many
   Jesus room beats (b04-b09, b14, b20-b23) carry their own Jesus lock over the
   same room prose. (b03 is Nicodemus at the doorway, also NON-Jesus — it will
   pick up the plate too.)

3. **RIVER** (b15-b19; all NON-Jesus). Promote **b15** (`s15-down-into-the-water.jpeg`):

       python3 media-production-v2/v2_stash.py --promote \
           build-168-born-water-spirit RIVER s15-down-into-the-water.jpeg

   Auto-attaches to b16, b17, b18, b19.

4. **GATE** (b25-b28; all NON-Jesus). Promote **b25** (`s25-even-a-learned-ruler.jpeg`,
   the empty open door — cleanest plate, no person):

       python3 media-production-v2/v2_stash.py --promote \
           build-168-born-water-spirit GATE s25-even-a-learned-ruler.jpeg

   Auto-attaches to b26, b27, b28.

**Order for the runner:** generate b01, b10, b15, b25 early, QC them,
`--promote` all four, then re-run `v2_prompt.py build-168-born-water-spirit
--check` (it now enforces the plates are on disk) before spending the rest of
the credits, then generate the remaining stills.

## COVERAGE MAP (seg → beats)
- n1   → b01 (WIDE establish — Nicodemus in the dark street) + b02 (a man of standing, in secret) + b03 (humble at the doorway) — NIGHT, no Jesus
- n2   → b04 (came to the light, listens across the lamp) + b05 (his world tips over) + b06 (a whole new beginning) — NIGHT, Jesus present
- kv3  → b07 (Jesus turns to answer) — attribution, Jesus
- kv3b → b08 ("Except a man be born again") + b09 ("cannot see the kingdom of God") — RED-LETTER, Jesus
- s4   → b10 ("How can a man be born when he is old?") + b11 ("enter the second time...?") — SCRIPTURE voice on NICODEMUS, no Jesus
- n3   → b12 (baffled, could not picture it) + b13 (sure no one could start over) — NIGHT, no Jesus
- n4   → b14 (Jesus: never meant physical) + b15 (river baptism, going DOWN) + b16 (coming UP new) — b15/b16 DAY river, no Jesus
- n5   → b17 (not water only, on the bank) + b18 (born of the Spirit — light from above) + b19 (a birth from above, life breathed) — DAY, no dove/flame/figure
- kv5  → b20 (Jesus answers again) — attribution, Jesus
- kv5b → b21 ("born of water and of the Spirit") + b22 ("cannot enter into the kingdom of God") — RED-LETTER, Jesus
- n6   → b23 (Jesus: not one option among many) + b24 (Nicodemus humbled — the gate is the gate) + b25 (the open GATE introduced, empty) — b25 DAWN gate
- n7   → b26 (the gate still open before you) + b27 (simply the way in) + b28 ("will you go through?") — DAWN gate, no Jesus

## ROW INTENT (for the review card, if Cameron asks)
Milk that leans RESTORATION, strictly inside the Bible's own frame, church NEVER
named. The one gate of the new birth — born of WATER (baptism) and of the SPIRIT
(the gift of the Holy Ghost) — is the same single way in for everyone, even a
learned ruler; taught through John 3 and handed to the viewer at the open door.
Two-Voice intact: narrator modern, Jesus only the exact KJV of John 3:3, 3:5.

## COST
$0 image, $0 audio (author lane). Reroll budget ≤15% of 28 beats = ≤4 rerolls;
watch the halo/scale risk on the LAMPLIT dialogue faces (crown must stay dark —
flame low and in front) and the light-from-above beats b18/b19/b26 (no dove,
flame or figure, no ring around the head).
