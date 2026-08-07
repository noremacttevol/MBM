# Story 39 Realistic V2 QC — The Pharisee and the Publican (Luke 18:9-14)

## C-FIX 2026-08-07 (Machine A `Dev`) — black-spots complaint CLOSED

**COMPLAINT LEDGER — the one OPEN complaint on this row (reported against hash
`b9c5c44b…`), and exactly what in this cut fixes it:**

> Cameron: *"There is some pictures with random black spots on their hands and
> fingers @ 0:53, 3:13, 2:05, etc. Another one on his lips @ 2:40 and then
> another picture with 2 hands of the same side looking like 2 people standing
> in line with their hands out but i think it was supposed to be something
> different @ 3:14"*

| his timestamp | beat / still | defect he saw | fix in THIS cut |
|---|---|---|---|
| 0:53 | b14 `s14-he-worked-for-rome` | two blue-black ink smudges on the fingers | identity/geometry edit — smudges removed, clean skin, coin+thumb byte-identical |
| 2:05 | b31 `s31-a-prayer-of-seven-words` | ink smudges across the fingertips on his chest | edit — smudges removed, natural nails, hand position identical |
| 2:40 | b40 `s40-barely-able-to-speak` | dark spot on his lower lip | edit — spot removed, lip smooth/even, beard+framing identical |
| 3:13 / 3:14 | b48 `s48-came-holding-nothing` | ink marks on the fingers **and** "2 hands of the same side" | edit — ink removed **and** hands corrected to a natural left-hand (back) + right-hand (open palm-up, "holding nothing") pair |

Method: **targeted image-edit pass** (attach the finished frame, change ONLY the
named defect, keep every other pixel), the same edit technique this row already
used for the battlement crest. Each candidate was QC'd at zoom and full-frame
(FACE-BOARD recheck: no new figure, no cream robe, no crop/lighting drift) before
it replaced the shipped still. Only these **4 frames** were touched; s47 (the
Pharisee's herb fist) and every other hand/lip frame were checked and were
already clean, so they are byte-identical to the cut Cameron has.

**Audio:** untouched — re-assembly printed `AUDIO LOCK PASS SHA256 2693bcca035a…`,
the SAME hash as the shipped cut, so narration/voices/timing are byte-identical.

**Cost:** 4 edits × $0.134 = **$0.53**, 0 discarded takes → **0% rerolls** (budget
is 15% of 58 = 8 frames). Meter $416.61 → $417.14. Touch-once: all four known
defects batched into this ONE re-cut.

---


**STATUS: SHIPPED TO REVIEWER 2026-08-04 (worker 35, Machine A `Dev`) — 58/58 at
native 2K, assembled `luke-18_pharisee-and-publican.mp4` 247.3 s / 22.0 MB, AUDIO
LOCK PASS SHA256 `2693bcca035a…`, captions checked on frames extracted from the
rendered MP4 (bottom band only; question card clean, no encoding squares).
Awaiting Cameron's approval — prior approval VOID under REDO-ALL.**

How the last six finished (the billing blocker cleared itself — auto-reload):
the six text-cured rerolls came back with THREE new court defects (b26 regrew the
crenellated parapet its own scene text bans; b53 a colonnaded portico plus a
second figure in a court its text says is empty; b55 battlements plus a classical
facade). The cures that held were the NEW tools, not more prose: an approved kept
frame promoted as the TEMPLE-COURT **place plate** (`v2_stash.py --promote`)
fixed b26 in one roll and pulled b53/b55 onto the right court; the last stubborn
sliver — battlement teeth regrowing on the wall crest right of the sanctuary,
four renders in a row — was removed by a **geometry edit pass** on the finished
frames (attach the frame, change only the named wall top, recheck everything),
verified clean at zoom afterward. Six-frame fix cycle $1.47 total.

The six outstanding beats — all of them deliberate rerolls whose old files were
deleted, so no stale picture can survive into the cut:

| beat | file | why it is being rerolled |
|---|---|---|
| b17 | `s17-out-in-the-open.jpeg` | colonnade of round columns down both sides |
| b23 | `s23-not-asking-for-anything.jpeg` | rerolled with b17 so POSITION A stays identical |
| b26 | `s26-standing-afar-off.jpeg` | distant colonnade + crenellated parapet on the horizon |
| b52 | `s52-still-standing-there.jpeg` | colonnade at the frame edge |
| b53 | `s53-still-praying-still-certain.jpeg` | colonnade along the left edge |
| b55 | `s55-sure-he-was-already-in.jpeg` | colonnade across the middle distance |

---

## What V1 actually did (verified from the artefact, not the prose)

FOURTEEN stills for 247.267 s — an average of **17.7 s a picture** — and seven of the
fourteen are held across two whole segments each:

- `s9-the-verdict.jpeg` covers j3 + n10, **167.982 → 197.576, TWENTY-NINE AND A HALF
  SECONDS**: the red-letter verdict of Luke 18:14 *and* the narrator's entire
  unpacking of it — the sentence the video exists to deliver — on one frame.
- `s6-afar-off.jpeg` covers jv13a + n7, **26.7 s**, the whole introduction of the
  publican at the back of the temple.
- `s5-pharisee-prays.jpeg` covers n5 + j1, **24.0 s**, the whole red-letter prayer.
- `s2` 15.9 s, `s3` 16.2 s, `s4` 15.9 s, `s8` 12.7 s.

V2 gives all twenty-one spoken segments their own pictures: **58 over 236.952 s =
4.09 s/picture**, shortest 3.16 s, longest 4.86 s.

## Audio

**LOCKED — nothing re-voiced, nothing re-timed, V1 never written to.** extract_beats'
reconstruction of V1's own timeline arithmetic (LEAD 0.28, GAP 0.72, KJV_GAP 1.75,
TAIL 1.5) totals **247.244 s** against the delivered MP4's **247.266 s** — 0.022 s
apart, so the staleness tripwire is nowhere near firing.

*The independent audio-stream MD5 comparison against the V1 MP4 has NOT been run yet,
because nothing has been assembled. It is a required step before shipping.*

## The sourcing trap on this row — checked and clear

By GIT CONTENT DATE (mtimes are worthless here) `make_narration.py` is
2026-07-24T00:35:41 and all twenty-one mp3s **and** the delivered MP4 share one later
commit, 2026-07-27T23:20:01 — the script PRE-dates its own audio, the safe direction.
All twenty-one segments were transcribed anyway with faster-whisper (small.en,
word_timestamps=True) and compared word for word. Four apparent differences came back
and every one was chased:

- **s9** "parable **unto** certain" heard as "into" — small.en only; medium.en returns
  "unto". Whisper mishearing archaic KJV, a family this wave has hit repeatedly.
- **n4** "A **traitor** with a money box" heard as "trader" — small.en only; medium.en
  returns "traitor".
- **n13** "did not tell **this** story" heard as "the story" — small.en only; medium.en
  returns "this".
- **card** "If you **stopped** performing" heard as "stop" by **both** small.en and
  medium.en. Settled as whisper's, not the audio's: the /t/ of "stopped" before the /p/
  of "performing" is an assimilated plosive that leaves no separate burst, and the
  measured 5 ms-frame energy trace across that word shows **one** stop closure and
  **one** release, not two. Same inflection family rows 29, 31 and 38 all settled.

**No TEXT_OVERRIDES and no SPEAKER_OVERRIDES.**

## Windows

Rebuilt from scratch from `extract_beats` plus MEASURED whisper word timings, never
from the `.timing.json` sidecars (which on this build hold one phrase spanning a whole
segment). Verified mechanically: **contiguous 0.000 → 236.952** (the card's own start),
**zero gaps**, and **all 20 speech onsets land inside their own window**. Each interior
split sits 0.15 s before the onset of the word it belongs to.

## Who carries which red-letter line — this row's sharpest content question

Five red-letter segments, and only ONE of them belongs on Jesus's face:

- **jv10 (18:10)** — Jesus setting the scene. Staged inside the parable, on the two men
  climbing the stair.
- **j1 (18:11-12)** — **the Pharisee praying.** A red-letter Bible inks it, but the
  speaker is a character inside the parable. Jesus's face under "God, I thank thee, that
  I am not as other men are" would invert the line completely; all four of its pictures
  are the Pharisee alone on the open pavement.
- **jv13a (18:13a)** — Jesus narrating inside his own parable, staged on the publican.
- **j2 (18:13)** — **the publican praying.** His face.
- **j3 (18:14)** — Jesus speaking as himself. These three frames are his.

Jesus appears in eight frames only (b01, b02, b03, b41, b42, b43, b44, b56) and never
inside the parable, never in the temple.

## Content care

Luke 18:9-14 narrates no heaven, hell, angel, soul, death or punishment, so none is
painted. **God is never depicted** as any figure, face, form, light or presence — both
men pray to open sky and the sky is only sky. "Would not lift up so much as his eyes
unto heaven" is staged as a man not raising his eyes. n8a's "while a lamb is being
killed for the sins of the whole nation" is the one line the narration itself puts at
the altar, so the altar is shown — as **stone, smoke and standing priests only**. No
blood, no knife, no carcass, no killing anywhere; the lamb appears once, alive, led on a
plain cord. The Pharisee is **never a grotesque** — n3 says outright he "was not a fake",
and a sneering caricature would let the viewer off the hook, so he is handsome,
disciplined, genuinely devout and completely certain. The publican is never abject
spectacle: no grovelling, no theatrical weeping, no filth.

## Staging — five places, none repeating the wave

A **broad flight of worn city steps** below a high blank wall, where Jesus tells it
standing to four prosperous men who are standing too (row 38 used an olive-press yard,
37 a fig court, 36 a rooftop, 35 a dining room, 34 a terebinth, 33 a rock-cut stair);
the **temple's great outer stair** and its **vast open paved court**; the **Pharisee's own
house door** at first light; the **publican's toll table** at the town gate; and one
**plain open square-topped gateway** for the closing two frames.

**The row's visual engine:** two fixed camera positions. POSITION A stands behind and
above the Pharisee on the open middle of the pavement and is returned to five times
(b17, b23, b52, b53, b55) with only the light and the emptiness changing — the last
three after everyone else has gone home, which is what "he is still standing there"
actually means. POSITION B stands at the back wall behind the publican. **b25** is the
one frame holding both men at once, the near man large and the far man a thumb against
the far wall, and that single composition is the parable. V1's fourteen reused stills
could do none of it.

## Rerolls and the cures — 20 of 72 generations = 27.8% (6 of them still outstanding)

Every one was regenerated **composition-level (delete file + fresh generation), never
`--redo`**.

1. **Pharisee anchor — a modern shawl-collar dressing gown.** The mantle rendered as a
   front-opening robe with a shawl collar, the exact GARMENT-CONSTRUCTION defect. Cured
   by **geometry, not prohibition**: the mantle is now stated as one flat rectangle laid
   across the *back* of both shoulders with both ends carried backward, so the whole
   front of the body shows only unbroken indigo tunic.
2. **Pharisee anchor — a rim-light fringe on the hair.** A low front-side sun on a bright
   background rims the hair by physics; a ban does not beat physics. Cured by writing the
   **light geometry** into both character locks — every light stands in front of the man
   and on the camera's side of him, and the outer edge of hair, beard and shoulder is
   always darker than what lies behind it. Ported to the PUBLICAN lock preventively.
3. **The doorway in the anchor produced a door leaf** → the doorway was **deleted** and
   replaced with a flat shaded plaster wall.
4. **Listeners in pale neck scarves** (b01) — "only Jesus wears cream". A ban failed
   twice. Cured by **re-staging positively**: any covering at a listener's neck or head
   is now the same solid dark colour as his own tunic, so each man is one unbroken dark
   block head to sandals.
5. **A classical colonnade in the temple — the row's hardest defect, four failures.**
   It arrived through the shared lock's own "square-section stone piers" (b05, b06), then
   again after that lock was hardened with an explicit prohibition list (b17), then again
   after the covered walk was **deleted from the lock outright** (b17 second pass), then
   again at extreme distance along the horizon (b26, b52, b53, b55). Rows 10 and 14
   already proved a prohibition loses to a strong noun, and the shared lock sits ~1500
   words before the scene text. Final cure: the boundary is stated at the **front of each
   beat's own scene**, as geometry plus an **inventory** — exactly two built objects stand
   up off the pavement anywhere in the picture, the sanctuary block and the altar, and
   between the top of the wall and the sky there is nothing at all. Injected mechanically
   into all 19 wide temple beats so the wording cannot drift. **(An earlier attempt to
   append this injection silently failed to write; it was caught by grepping the file and
   re-landed. Run D therefore generated without it, which is why six frames still need
   the reroll.)**
6. **A closed boot on the Pharisee** (b05) → open thong sandals pinned positively, bare
   toes, instep, heel and ankle visible.
7. **The Western Wall** (b21) — the temple rendered as the post-70 AD ruin, weathered
   mismatched blocks with vegetation growing out of the joints, over a modern plaza. For
   an LDS outreach video that is the worst possible miss. Cured in the shared lock: the
   temple is **newly built and standing whole**, sharp arrises, tight regular joints,
   nothing growing out of the stone, and explicitly not the Kotel.
8. **A clean-shaven Pharisee** (b21, back view) → the beard restated as visible past the
   jaw line even from behind.
9. **A metal hasp on the money box** (b16), invisible until cropped in — the exact
   row-35 buckle defect. TOLL-STATION already banned box fittings, so **the box was
   deleted** from the shared lock; the coins now sit in a wide shallow fired-clay bowl,
   which that lock already allowed. b13 and b15 were rerolled with it for continuity.
10. **A knitted ribbed cuff** in the ten-herbs macro (b11) and the coin macro (b14) — a
    close-up is where the shared WOVEN-CLOTH lock is weakest. Cured two ways: a
    close-range weave clause added to both character locks, and, where the sleeve served
    no purpose, **the sleeve was deleted from the frame** and the forearm left bare.
11. **Nine bundles, not ten** (b11) — COUNT-AS-GEOMETRY. The ten had spread onto two
    surfaces and one went missing. Cured by pinning the arithmetic: nine in one straight
    row on one ledge plus the tenth a hand's width apart, and nothing on any second
    surface.
12. **A pale stray at the frame edge** (b04) and **a hazy pale figure in the background**
    (b01) → CAST-CLOSURE tightened and the background capped at nobody.

Frames generated *before* each cure were re-inspected in the same pass (the row-35
lesson); that re-inspection is what caught b26/b52/b53/b55 on the contact sheets.

## New shared locks added to `v2_prompt.py`

- **TEMPLE-COURT** — "temple", "altar", "priest" and "worship" pull, all at once, a
  Gothic church with pews and stained glass, a Greek temple with fluted columns and a
  pediment, a golden-domed mosque, and a modern synagogue with a curtained ark, a
  silver-crowned scroll, a six-pointed star and men in skullcaps and black-striped prayer
  shawls — every one centuries later than this story, and the last is the one an LDS
  outreach video can least afford to get wrong. States the open stone courts, the plain
  bounding wall, the unhewn-stone altar with its ramp and the barefoot linen-clad priests
  positively; states that the sacrifice is shown as stone, smoke and standing priests
  only, with no blood or killing visible; and states that the building is newly built and
  whole rather than the Western Wall ruin. The temple recurs constantly across the 200
  (the boy in the temple, Zacharias, the presentation, the cleansing, the widow's mite).
- **TOLL-STATION** — "tax office", "toll booth" and "collector" pull a Victorian counting
  window or a highway kiosk: a boarded booth with a hatch, a barrier arm, a metal cash
  box, a bound ledger, a uniform. States the low adzed timber slab on two stone blocks in
  the open dust, the counted heaps of struck coins, the clay bowl, the reed basket of
  rolled sheets and the cut reed pen positively — and now names no wooden box at all.
  Tax collectors recur across the 200 (Matthew at the receipt of custom, Zacchaeus, the
  tribute money).

## Still outstanding before this row can ship

- Generate the six rerolled frames (blocked on API billing).
- QC those six.
- Assemble; verify the MP4; **verify the audio lock independently** by comparing the
  finished cut's audio-stream MD5 against the V1 MP4's.
- Extract real frames and look: captions in the bottom band only, never clipped, light
  blue for the Luke 18:9 scripture framing, white for the narrator, red for every parable
  speech with each red line on the person who says it; closing card carries its words.
- Confirm measured silence windows prove narration + intentional silence with no music bed.
- Ship: commit the MP4 by path, repoint the row 39 review card (it currently has **no**
  `data-review-wave="realistic-v2"`, so it is hidden from Cameron and must gain one),
  sync reviews, deploy, update the boards.
