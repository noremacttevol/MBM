# QC / RUNNER HANDOFF — build-40-the-friend-at-midnight (Luke 11:1-13)

Authored to lessons 11–12 on 2026-08-05 (Machine A). `v2_prompt.py --check`
PASSES with zero WARNs at handoff. 56 beats, 312.3 s. Audio column OK on
AUTHOR-BOARD (new-voice verified by the audio audit).

## Coverage shape (lesson 12 — do not "fix" this back)

Six true wides, each stating its camera-to-back geometry in scene text:
b01 (grove establish), b03 (watchers' reverse), b19 (neighbour-house
establish), b22 (the refusal), b25 (the lane waking), b38 (rooftop scale).
Everything else is deliberately a single, two-shot, over-shoulder or insert —
if a render comes back as a crowded group portrait on a non-wide beat, that
is a MISS of the beat, not a bonus.

b56 (158.65–165.30) is the neighbour's RISE — the payoff verse's own verb —
and cuts mid-sentence to b29 (165.30–169.79, the giving). A mid-line picture
cut is intentional movie grammar; captions ride segment timing, not windows.

## Place plates (lesson 11) — generation order matters

LANE is wired (PLACE-REF/lane.jpeg from build-31, committed). Every other
recurring place is PROMOTE-FIRST: generate the named beat FIRST, QC it, run
the promote command, and only then generate the rest of that place's beats so
they copy the approved frame.

| Token | Promote from | Then covers |
|---|---|---|
| GROVE | b01 `assets/s01-and-it-came-to-pass.jpeg` | b03 b04 b05 b07 b15 b30 b34 b37 b39 b45 b46 b49 b55 |
| ASKER-HOUSE | b11 `assets/s11-feeding-a-guest-was-a.jpeg` | b10 b12 b13 b33 b50 |
| NEIGHBOR-HOUSE (interior) | b19 `assets/s19-on-the-other-side-of.jpeg` | b20 b22 b23 b56 b29 |
| NEIGHBOR-DOOR (street face) | b02 `assets/s02-he-knocks-again.jpeg` | b16 b17 b21 b24 b26 b28 b29 b32 b35 b36 b38 b41 |
| COURTYARD | b06 `assets/s06-it-was-the-word-a.jpeg` | b08 b42 b43 b44 b48 |
| LIT-HOUSE | b53 `assets/s53-the-man-in-the-story.jpeg` | b52 b54 |

Promote command shape:
`python3 media-production-v2/v2_stash.py --promote build-40-the-friend-at-midnight <TOKEN> <that-frame.jpeg>`

The stash SUGGESTED `COURTYARD=build-34-rich-fool:v2-r034-b13` and it was
DECLINED on purpose: that plate is the rich landowner's flagstoned estate
courtyard with a laid supper table — the wrong world for this story's modest
family courtyard (packed earth, water jar, fig tree). Do not --take it.

## Row-specific QC traps

- The knock escalation must LADDER: b17 polite three-finger ask → b02 knock
  → b16 both hands → b25 street waking → b26 relentless → b27 seen-and-
  unstopped → b28 arms-wide shameless. Each frame more committed than the
  last; if two adjacent frames read at the same intensity, reroll the later.
- b41's worn knocking-spot on the door planks is a narrated story point and
  now lives in the NEIGHBOR-DOOR lock — it must be visible in door close-ups.
- Serpent (b43) and scorpion (b44) are compared objects, NEVER near or
  threatening the child (CONTENT-CARE): snake inert on the far table corner,
  scorpion an arm's length away on the wall-top.
- Time of day is scripture-law: grove = dawn→morning; parable = full
  moonless midnight (blue-black, single clay lamp — never sunset tones);
  father-son beats = warm daylight; b51 = golden evening; b52–b54 = night
  with ONE lit window/door (lamplight only, nothing supernatural).
- Only Jesus wears cream — the asker rust-brown, neighbour olive-grey,
  traveller dusty indigo, father chestnut, boy dusty-blue.
- b53 has NO people in frame (an ajar door with light spill); b36, b40, b47,
  b50, b54 are also person-free inserts — do not let the model add figures.

## RUNNER QC LOG — first-attempt V2 cut (Machine A, 2026-08-05)

56/56 at native 2K via the Gemini API. 4 story-cast portraits (ASKER,
NEIGHBOR, TRAVELER, FATHER-SON) generated and auto-wired into REFS; the 6
promote-first plates generated, eyeballed, promoted (GROVE b01,
NEIGHBOR-DOOR b02, COURTYARD b06, ASKER-HOUSE b11, NEIGHBOR-HOUSE b19,
LIT-HOUSE b53); LANE carried from build-31. Row ~$8.2, meter 214.67 →
222.84, under the $226.73 ceiling.

**REROLLED (1):** b53 LIT-HOUSE. The first take put a ~15-person candle
crowd into a beat whose must_show is an EMPTY ajar door spilling light
onto a dark lane — an obvious miss on a designated person-free beat, and
it would have become the plate for b52/b54. The reroll is exactly the
brief: empty lane, door ajar, warm spill down the step, no bar/staples,
no halo. Promoted that take.

**PASSED (the stated traps):**
- KNOCK ESCALATION ladders: b17 polite three-finger ask → b02 knock →
  b16 both hands → b25 the lane waking (neighbours at windows) → b26
  relentless → b27 seen-and-unstopped → b28 arms-wide shameless. No two
  adjacent frames read at the same intensity.
- CONTENT-CARE: the serpent (b43) and scorpion (b44) are inert compared
  objects on/near the table, never close to or threatening the child.
- TIME OF DAY holds all four registers: grove dawn→morning, parable full
  moonless midnight (lamp/window light only), father-son warm daylight,
  b51 golden evening, b52-b54 night with one lit door.
- PERSON-FREE inserts stayed empty: b53 (after reroll), b36, b40, b47, b50.
- Costume law: only Jesus in cream; asker rust-brown, neighbour olive-grey,
  traveller dusty indigo, father chestnut, boy dusty-blue — all held by
  their portraits across every appearance.
- b56 (the neighbour's RISE) has its own frame, the payoff verse's verb.
- The COURTYARD plate is the modest family courtyard (packed earth, water
  jar, fig tree) — the declined build-34 estate plate was correctly not used.

**FIX-WAVE (kept, not rerolled):** none rising above the runner bar on this
row; the sheets show no giant figures, no wrong-direction travel, no modern
objects, no lens-staring, no phantom people in the wides.
