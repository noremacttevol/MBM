# QC / RUNNER HANDOFF — build-17-lazarus (John 11:1-44)

Authored from scratch to lessons 11–12 on 2026-08-05 (Machine A).
`v2_prompt.py --check` PASSES with zero WARNs at handoff. 61 beats,
316.5 s. Audio column OK on AUTHOR-BOARD (new-voice verified).

## OPEN COMPLAINT this build must cure (from the reviewer)

> "At 23 seconds it shows the wrong captions from the older version for a
> split second before going to the new edit where it has the pink captions."

That was a V1 assembly defect (a stray stale caption frame). The V2
assembler regenerates all captions, but the cure is only real on the
RENDERED product (rubric lesson 9): after assembly, frame-step the
rendered MP4 around 20–26 s AND spot-check every segment boundary for any
single-frame caption flash or style mismatch before publishing the card.

## Cast lineage (face-board law — this is the row's biggest identity risk)

- MARTHA and MARY are the SAME two women as build-16-mary-martha. Their
  locks in beats_v2.py are byte-identical copies of build-16's. When
  v2_story_cast.py builds this row's anchors, face-match both against
  build-16's approved stills side-by-side BEFORE generating scene beats —
  one actor per sister across both videos or the face-board fails.
- LAZARUS, MESSENGER, MOURNERS are new to this row (story-local).
- Jesus is the global JESUS-V2-REF on every beat flagged `jesus`.

## Coverage shape (lesson 12 — do not "fix" this back)

Five true wides, each stating camera-to-back geometry: b01 (house
establish), b15 (tomb establish), b21 (Martha's run), b33 (road grief),
b55 (frozen crowd). Everything else is a single, two-shot, over-shoulder
or insert. The raising is a frame-per-action ladder — b49 call forming →
b50 THE SHOUT → b51 first sight in the dark → b52 emergence → b53
standing bound → b54 wrapped face in light → b55 crowd frozen → b56
"loose him" → b57 the unwrapping. If adjacent ladder frames read at the
same intensity, reroll the later one.

Mid-phrase window cuts at b26/b27 (143.60), b31/b32 (172.20), b46/b47
(245.20), b52/b53 (271.50), b58/b59 (298.50) are intentional movie
grammar; captions ride segment timing, not beat windows.

## Place plates (lesson 11)

Wired and committed (PLACE-REF/, PLACE-WIRING.json):

- TOMB ← build-37-rich-man-lazarus b45 (27 beats). Same architecture on
  purpose: hillside cave, squared doorway, round rolling stone in a cut
  channel. **CAVEAT: the plate shows the stone ROLLED OPEN.** Beats b15,
  b16, b37, b41, b42, b44, b45 need it SEALED shut, b46 mid-roll, b47+
  open — the stone's position is stated per-beat in the prose; verify
  every sealed-stone render actually shows it SEALED before accepting.
- ANCIENT-ROAD ← build-38-persistent-widow b39 (4 beats). Plate is
  evening-lit; this build's road beats are midday — light follows the
  beat prose, the plate carries only the road's character.

PROMOTE-FIRST (new places — generate the named beat FIRST, QC it, promote,
then generate the rest of that place):

| Token | Promote from | Then covers |
|---|---|---|
| BETHANY-HOUSE | b01 `assets/s01-in-a-village-called-bethany.jpeg` | b02 b03 b04 b05 b06 b13 b17 b18 |
| JORDAN-CAMP | b07 `assets/s07-you-would-expect-him-to.jpeg` | b08 b09 b10 b11 b12 |
| BETHANY-ROAD | b21 `assets/s21-martha-heard-he-was-finally.jpeg` | b14 b19 b20 b22–b36 (all road beats) |

MOURNERS is a CAST lock, not a place — the stash tool lists it under new
places because it doesn't know the difference. Do NOT promote a plate for
it; a crowd plate would clone one crowd into every scene.

## Row-specific QC traps

- b13: the road behind the sisters must be visibly EMPTY to the horizon.
- b14 + b21: Jesus's travel direction on the road is LEFT to RIGHT in
  every road beat; Martha enters b21 from the RIGHT (village end). Keep
  the two groups' directions consistent or the meeting reads backwards.
- b26/b27 are a shot/reverse pair on the same exchange — same light,
  same spacing, mirrored angles; if they don't cut together, reroll.
- b35/b36/b37/b38: Jesus weeps REAL tears — wet eyes, tracks into the
  beard — with no red-rimmed horror and no serene dry-eyed "sheen." The
  tear tracks persist through b42, b50, b56 (he does not reset to dry).
- b46: all three men heave the stone the SAME direction along its channel
  (action-logic law); feet dug in, believable weight.
- b47, b49, b51: the tomb interior is TRUE BLACK — if any render shows
  interior detail, walls, or a lit figure before b51's half-lit form,
  reject it.
- b51–b54: the bound figure is reverent, never horror — CLEAN linen,
  upright dignity, face covered until b57. No decay, no gauze-monster.
- b55: every gaze in the crowd converges on the tomb mouth just out of
  frame; one dropped water jar maximum — no scattered-props chaos.
- b57: Lazarus's emerging face is ALIVE — warm skin, squinting hard
  against light; not pale, not corpse-toned.
- Only Jesus wears cream anywhere, including blurred crowd edges.
- Person-free frames: b16, b17, b41, b47, b51 (form only, no exposed
  face), b53/b54 (bound figure only) — do not let the model add people.
