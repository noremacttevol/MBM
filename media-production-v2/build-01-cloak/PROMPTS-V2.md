# PROMPTS-V2 — row 1, build-01-cloak — "The Woman Who Touched His Cloak" (Mark 5:25-34)

**V2 rebuild. Audio, timing and caption text are the finished V1 assets, untouched.
Only the pictures are new.** The V1 folder was read, never written.

- V1 source: `media-production/build-01-cloak` (read-only)
- Runtime: 109.0 s (V2 arithmetic reproduces V1's finished mp4 at 108.97 s)
- Constants read from THAT build: `LEAD 0.28 · GAP 0.72 · KJV_GAP 1.30 · TAIL 1.5`
- CONTENT-CARE: row 1 is absent from the §3 flag table → **GREEN**. Handled anyway
  with restraint: her illness is an issue of blood, so it is carried entirely by her
  face, her frailty, and the way people step back from her. No blood, no medical
  detail, nothing of her body exposed.

## Coverage: 20 pictures (V1 had 11)

STORY-COVERAGE-LAW asks where a new visual moment passes with no new picture. V1
had two clear misses, both fixed here:

| miss in V1 | fix in V2 |
|---|---|
| `w28` — her ONE spoken line in all of Mark 5 — shared V1's `s4` with `n3a` | **b08** is hers alone: her face as she says it to herself |
| "pressed through the crowd **and reached out to touch the edge of his cloak**" — the hinge of the whole story — shared one still with the pushing-through | **b10** presses through, **b11** is the fingertips on the hem |

Long segments are split at word anchors (`marker_time`, the build-10/18/19 pattern),
not at arbitrary times: `n2` at "she was exhausted", `n2b` at "the crowd pressed"
and "almost no one", `n3b` at "she pressed through the crowd" and "and reached out
to touch", `n4a` at "the healing was already hers", `n4c` at "he ignored them",
`n5` at "over in a sentence".

## The scripture that governs the pictures

| verse | what it forces |
|---|---|
| 5:21 | beside the sea, much people — a lakeside town, **daytime** (every still is bright midday) |
| 5:22-24 | Jairus, a synagogue ruler, is already leading him to a dying child |
| 5:25-26 | twelve years; many physicians; **spent all she had**; grew worse |
| 5:27 | she came **in the press BEHIND** and touched his garment — every reaching shot puts her **behind** him, never face-on |
| 5:29 | she **felt in her body** she was healed — carried on her face, never as a light effect |
| 5:30 | he **turned him about in the press** |
| 5:31 | the disciples push back |
| 5:32 | he **looked round about** to see her |
| 5:33 | she came **fearing and trembling** and **fell down before him** |
| 5:34 | "Daughter… go in peace" |

## Beat table

Full assembled prompts (STYLE-V2 + defense line + anti-panel + locks + scene,
byte-identical blocks) are in `ASSEMBLED-PROMPTS.txt`, generated from `beats_v2.py`
by `../v2_prompt.py`. Blocks are assembled by code, not copied by hand — that is
what makes byte-identity a property of the build instead of a QC chore.

| beat | still | seg | window (s) | wide | Jesus+REF | the moment |
|---|---|---|---|---|---|---|
| b01 | s01-twelve-years | n1 | 0.00–4.33 | | | alone, worn, twelve years |
| b02 | s02-physicians | n2 p1 | 4.33–7.68 | ✅ | | the last coins into a physician's hand |
| b03 | s03-untouchable | n2 p2 | 7.68–15.11 | ✅ | | the street steps back from her |
| b04 | s04-jairus-urging | n2b p1 | 15.11–22.39 | ✅ | ✅ | Jairus hurrying him to a dying child |
| b05 | s05-crowd-pressing | n2b p2 | 22.39–25.10 | ✅ | ✅ | the crowd closing on every side |
| b06 | s06-woman-at-edge | n2b p3 | 25.10–29.84 | ✅ | ✅ | her at the edge, unnoticed |
| b07 | s07-she-hears | n3a | 29.84–38.66 | | | the news reaches her; her head lifts |
| b08 | s08-she-says-it | w28 | 38.66–42.82 | | | **her one line, said to herself** |
| b09 | s09-her-plan | n3b p1 | 42.82–49.46 | ✅ | | she commits and steps in |
| b10 | s10-pressing-through | n3b p2 | 49.46–51.00 | ✅ | ✅ | forcing through, his back ahead |
| b11 | s11-touches-hem | n3b p3 | 51.00–53.96 | ✅ | ✅ | **fingertips on the fringe** |
| b12 | s12-he-stops | n4a p1 | 53.96–58.03 | ✅ | ✅ | he halts mid-stride |
| b13 | s13-healed-in-her-body | n4a p2 | 58.03–62.17 | | | twelve years leave her face |
| b14 | s14-who-touched | j0 | 62.17–64.73 | ✅ | ✅ | "Who touched my clothes?" |
| b15 | s15-disciples-protest | s31 + n4c p1 | 64.73–77.21 | ✅ | ✅ | Peter throws his arms wide at the crowd |
| b16 | s16-searching | n4c p2 | 77.21–82.47 | ✅ | ✅ | he looks round about, unhurried |
| b17 | s17-found-her | n4b | 82.47–84.91 | ✅ | ✅ | their eyes meet across a gap |
| b18 | s18-daughter | j1 | 84.91–91.53 | ✅ | ✅ | he crouches to her level: "Daughter" |
| b19 | s19-it-lands | n5 p1 | 91.53–96.76 | | | the word lands; relief |
| b20 | s20-goes-in-peace | n5 p2 | 96.76–101.11 | ✅ | ✅ | she walks away upright; he watches |

`s31` and the first half of `n4c` share **b15** — the narrator is retelling the same
protest and nothing visually changes, which is the only condition under which
STORY-COVERAGE-LAW permits two segments on one still.

## Character locks (byte-identical in every prompt they appear in)

- **JESUS** — LOCK v4 + `REF: media-production-v2/JESUS-V2-REF/jesus-v2-face.jpeg`
- **WOMAN** — dust-rose head cloth, patched ash-grey-brown tunic, charcoal-brown
  mantle. Deliberately not blue-grey (Peter) or rust-brown (Andrew), and never cream.
- **JAIRUS** — indigo-blue robe with a woven border, dark blue head covering.
- **PETER / ANDREW / JOHN** — copied byte-identical from `CAST-REF/CAST-BIBLE.md`.
- **SETTING** — lakeside Galilean street, pale limestone, bright midday, crowd in
  browns/russets/ochres/olive/dusty blue, and no one but Jesus in cream.

## Step D — the v4 checklist (replaces the retired v3 gate)

`python3 media-production-v2/v2_prompt.py media-production-v2/build-01-cloak --check`
→ **PASS** on all 20: every Jesus shot carries the byte-identical LOCK v4 and the
REF line; no drift words in any scene text; only Jesus in cream; anatomy counts
stated positively; no NEGATIVE-PROMPT lists; every wide shot carries the
forced-wide defense line and the anti-panel clause.
