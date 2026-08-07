# QC / RUNNER HANDOFF — build-167-chosen-ordained (John 15:16)

**AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).**
`beats_v2.py` written from scratch: 24 pictures over 117.94 s (~4.9 s/pic,
matches rows 161-166 library density; lesson-12 movie coverage). `v2_prompt.py
--check` PASS. Windows contiguous + monotonic, first 0.280, last end 117.943 =
card seg_start; every segment onset falls inside its first beat's window. Audio
column OK on AUTHOR-BOARD. Ready ✅.

## COMPLAINT LEDGER
- **No open Cameron complaint on this row** (`v2_outline.py 167` shows no prior
  review). First V2 authoring, not a complaint fix — nothing to answer on the
  review card beyond the standard realistic-V2 wave note.

## SPEAKER LAW — the ONLY red-letter is John 15:16 itself
John's gospel, RED-LETTER: Jesus is speaking the verse. So **kv16a** (b04/b05)
and **kv16b** (b15/b16) are the only Jesus-VOICE beats and sit on **Jesus's own
face** (jesus=True, ref=True, cream robe). Every `n` segment is the NARRATOR.
Jesus is ALSO embodied — face + cream + REF — in the narrator beats that depict
the very act the verse names (choosing / calling by name / ordaining): **b06,
b07, b08, b21, b22**. He is NEVER shown for scale (SCALE GATE, lesson 14) — an
ordinary-sized man in every frame — and NEVER haloed/glowing (no light around
his head anywhere).

## THE FATHER / HEAVEN IS NEVER EMBODIED
"from heaven down" (b06), "ask of the Father" (b16), "backed with power" /
"heaven would answer" (b18/b19): heaven is warm light at the **top edge of the
frame ONLY** — never a figure, face or form in the sky. Each of those beats says
so in `must_not_show`.

## THE FOUR NEW PLACES — promote from NON-Jesus frames (lesson 11), never a Jesus frame
All four recurring places are NEW (kept new on purpose so the story's own warm
morning / harvest-gold light arc stays consistent within the video; the stash
matches carried other builds' lighting). They are carried by prose in `LOCKS`
for their first frame; the runner PROMOTES each build-local plate, then wires the
rest. `--promote BUILD TOKEN ASSET` is positional; ASSET is the approved still
filename.

1. **LAKESHORE** (bookend ordinary work — beats b01, b02, b03, b23, b24; all
   NON-Jesus). Promote **b01** (`s01-ordinary-work-by-the-water.jpeg`):

       python3 media-production-v2/v2_stash.py --promote \
           build-167-chosen-ordained LAKESHORE s01-ordinary-work-by-the-water.jpeg

   Auto-attaches to b02, b03, b23, b24.

2. **TEACHING-HILL** (the grassy hill above the lake — beats b04-b10, b15, b16,
   b18, b19, b21, b22). **b04-b08, b15, b16, b21, b22 are Jesus-bearing — NEVER
   promote any of them.** Promote the first clean **NON-Jesus** hill frame
   **b09** (`s09-never-just-a-title.jpeg`):

       python3 media-production-v2/v2_stash.py --promote \
           build-167-chosen-ordained TEACHING-HILL s09-never-just-a-title.jpeg

   Auto-attaches to the other NON-Jesus hill beats b10, b18, b19. The Jesus hill
   beats carry their own Jesus lock over the same place prose.

3. **VILLAGE-ROAD** (the dirt lane into the village — beats b11, b13; both
   NON-Jesus). Promote **b11** (`s11-out-to-the-villages.jpeg`):

       python3 media-production-v2/v2_stash.py --promote \
           build-167-chosen-ordained VILLAGE-ROAD s11-out-to-the-villages.jpeg

   Auto-attaches to b13.

4. **HARVEST-FIELD** (the golden barley field — beats b12, b14, b17; all
   NON-Jesus). Promote **b12** (`s12-the-measure-is-fruit.jpeg`):

       python3 media-production-v2/v2_stash.py --promote \
           build-167-chosen-ordained HARVEST-FIELD s12-the-measure-is-fruit.jpeg

   Auto-attaches to b14, b17.

**OPTIONAL cross-video reuse (runner's discretion, COST LAW):** if you would
rather import an existing shipped plate than promote, these on-disk NON-Jesus
landscape frames are clean matches — `--take` them with `--wire` instead of
promoting: `TEACHING-HILL=build-68-multitudes-mountain:v2-r068-b10` (grassy
slope), `LAKESHORE=build-30-net:v2-r030-b03` (morning shore),
`HARVEST-FIELD=build-46-seed-growing:v2-r046-b25` (gold field),
`VILLAGE-ROAD=build-110-lords-prayer:v2-r110-b11` (village lane). Prefer the
promote path if the imported lighting fights this row's warm-day arc.

**Order for the runner:** generate b01, b09, b11, b12 early, QC them,
`--promote` all four, then re-run `v2_prompt.py build-167-chosen-ordained
--check` (it now enforces the plates are on disk) before spending the rest of
the credits, then generate the remaining stills.

## COVERAGE MAP (seg → beats)
- n1   → b01 (WIDE establish, the ONLY wide — ordinary shore work) + b02 (hands mending a net) + b03 (a woman carrying water) — NO Jesus
- kv16a → b04 (Jesus: "I have chosen you") + b05 (Jesus lays hands: "and ordained you") — RED-LETTER, Jesus
- n2   → b06 (heaven-down direction, light from above) + b07 (Jesus singles ONE man out, calls by name) + b08 (both hands on the head, set apart with authority) — Jesus
- n3   → b09 (the ordained man rises to GO — a task, not a badge; NON-Jesus promote frame) + b10 (disciples turn to set out) + b11 (into the village to do the work) — NO Jesus
- n4   → b12 (insert of ripe barley = the measure, fruit; promote) + b13 (a disciple lifts an ordinary villager — people gathered in) + b14 (a sheaf carried home) — NO Jesus
- kv16b → b15 (Jesus: "go and bring forth fruit... should remain") + b16 (Jesus lifts a hand to the light: "ask of the Father in my name") — RED-LETTER, Jesus
- n5   → b17 (bound sheaves stored — a harvest that lasts) + b18 (a disciple kneels praying — backed with power) + b19 (light comes down — heaven answers) — NO Jesus (Father never embodied)
- n6   → b20 (study-gem scroll insert by lamplight, no place lock) + b21 (Jesus calls of his own choosing, by name) + b22 (kneeling man receives with open empty hands — a gift, not a badge taken) — b21/b22 Jesus
- n7   → b23 (bookend: ordinary shore worker half-turns as if hearing their name) + b24 ("will you look up, and answer?" — looks up to the warm light, invitation left open) — NO Jesus

## ROW INTENT (for the review card, if Cameron asks)
Milk that leans RESTORATION, strictly inside the Bible's own frame, church NEVER
named. The heart is a man CALLED of God and ORDAINED by the laying on of hands —
authority given from heaven down, received as a gift, not seized as a badge —
shown through Jesus's own words (John 15:16) and his own hands. Warm natural DAY
throughout (thematic treatment matching the V1 stills; not the literal
Last-Supper night of the discourse). Two-Voice intact: narrator modern, Jesus
only the exact KJV of John 15:16.

## COST
$0 image, $0 audio (author lane — 0 pictures generated, 0 re-voices). Handed to
the runner fully gated with a clean promote plan (reroll budget ≤15% of 24 beats
= ≤3 rerolls; the ordination two-shots b05/b08/b22 and the light-from-above
beats b06/b16/b18/b19 are the likeliest reroll risks — watch halo/scale there).
