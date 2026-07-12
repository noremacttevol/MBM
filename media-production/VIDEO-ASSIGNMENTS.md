# VIDEO ASSIGNMENTS — The Claim Board for All Machines

> 📊 **HUMAN DASHBOARD: [`STATUS.md`](../STATUS.md) (repo root) is the at-a-glance
> LIVE board — done / in-progress / to-do + watch & download links.** Whenever you
> change a video's state here, update its row in STATUS.md in the SAME commit, then
> push. This file stays the detailed claim mechanics; STATUS.md is the summary.

> **PRODUCTION-BIBLE §0 LAW A governs this file.** Every Claude on every computer:
> `git pull` FIRST, then claim here BEFORE generating anything, then commit and
> push the claim immediately. Never touch a video another machine has claimed.
> When a video is approved by Cameron, change its status to DONE with the date.
>
> Claim format: `CLAIMED — <date> — <machine/session note>`
> One machine = one video at a time. Finish or release before claiming another.

## 🛑 REDO BOARD (Cameron, 2026-07-11 — "redo the whole thing") — TWO rules to fix everywhere

**Rule 1 — Jesus's face is NEVER shown** (real Middle Eastern man seen only from behind
/ over-the-shoulder / at a distance — PRODUCTION-BIBLE §1 "The Standing Laws").
**Rule 2 — Phase 1 is PICTURES + NARRATION only: NO AI motion clips** (§0 Law E). Every
already-built video that contains Veo/Flow clips gets those clips PULLED OUT and is
rebuilt as one narration over pictures only. AI motion comes back in Phase 2, later.

Run the gate before regenerating any picture: `python3 media-production/jesus_face_gate.py --dir <build>`.
Each machine redoes ITS OWN video (Law A), in announced Chrome bursts (Law C), only after
the prompt sheet passes the gate. **Do NOT regenerate another machine's video.**

**REDO ASSIGNMENTS (Cameron, 2026-07-11):**
- **Videos #1–#5** — another machine (Cameron assigned).
- **Videos #6–#10** — originally CLAIMED by Machine C (Cameron Lovett MS) 2026-07-11.
  **RELEASED 2026-07-11:** #09/#10 built by Elli's laptop; **#06 and #08 are now UNCLAIMED —
  any machine may grab them.** Their PREP is done (PROMPTS.md written, style block locked,
  face gate passes trivially — parables, no Jesus figure). Partial art is already pushed:
  - **#06 build-06-two-sons/assets/** has 5 of 6 stills (wall, went, empty, pride, falseyes).
    LEFT: generate the 1 missing still **`refuse`** (first son shakes his head and turns to
    walk away from the father — prompt in build-06 PROMPTS.md), then rewrite build.py to
    STILLS-ONLY + verbatim captions on the #15 pattern, generate narration, build, QC, push.
  - **#08 build-08-lost-coin/assets/** has 2 of 6 stills (stars, door). LEFT: generate the 4
    missing stills **`count`, `lamp`, `sweep`, `found`** (prompts in build-08 PROMPTS.md),
    then the same stills-only build.
  - **#07** REASSIGNED to Elli's Windows laptop 2026-07-11 (Cameron gave direct picture feedback — 3 stills being fixed: s5 walk from-behind, a sinking-alone still, s9 walk-back with disciples in the boat).

**A. Prompt sheets that FAIL the face gate — restage the Jesus prompts on paper (no credits) first:**
| Build | Owner | Face-gate | Action |
|---|---|---|---|
| build-15-centurion | Machine C | ✅ PASS (restaged 332df5b) | Regenerate the 6 restaged Jesus stills; drop the 2 clips (Rule 2), assemble stills-only |
| build-14-ten-lepers | Elli's Windows laptop | ❌ 11 hits | Restage Jesus prompts (behind/over-shoulder/distance) → gate → regenerate; drop the 2 clips |
| build-13-roof | Machine A (Dev) | ❌ 2 hits | Restage + regenerate his stills; drop the 2 clips; re-audit before approval |
| build-12-bartimaeus | Cowork session | ❌ 2 hits | Restage → gate → regenerate; drop any clips |

**B. Delivered videos (.mp4 already built) — pull the AI clips out AND re-audit the face:**
- **build-13-roof** — built with clips AND under the "show his face" rule → HIGH PRIORITY: strip clips, rebuild pictures-only, fix Jesus stills.
- **build-05, 07, 09, 10, 11** — built with AI clips under the old *face-never* rule.
  Rule 2: strip the clips, rebuild each as pictures + narration only. Rule 1: their Jesus
  frames predate the face-showing rule so are likely fine — spot-check at high zoom to
  confirm. (#09 is also already in the rework queue.)

**C. Videos 16–20+ (unclaimed):** build fresh straight under both rules — pictures + narration
only, face gate must pass. Nothing legacy to redo.

## Wave One (videos 1–20)

| # | Story | File | Status |
|---|-------|------|--------|
| 01 | Woman who touched his cloak | mark-5_cloak | REDONE 2026-07-11 Machine A (Dev) — stills-only; Jesus new look (s03 walking-away no-hood dark hair; s09 "who touched" from directly behind; s07 hem clip→hand-on-tassels still). **APPROVED by Cameron 2026-07-11** |
| 02 | Prodigal Son | luke-15_prodigal | REDONE 2026-07-11 Machine A (Dev) — stills-only (father-runs clip→new painted running still); parable, no Jesus figure. **APPROVED by Cameron 2026-07-11** |
| 03 | Zacchaeus | luke-19_zacchaeus | REDONE 2026-07-11 Machine A (Dev) — stills-only (lookup clip→anchor still); Jesus already new look (from-behind, dark hair, no hood every beat). **APPROVED by Cameron 2026-07-11** |
| 04 | Nicodemus | john-3_nicodemus | REDONE 2026-07-11 Machine A (Dev) — stills-only ("came at night" clip→new painted night-street still); Jesus only ever shown from behind (dark seated figure), never a face. **APPROVED by Cameron 2026-07-11** |
| 05 | Bent Woman | luke-13_bent-woman | REDONE 2026-07-11 Machine A (Dev) — stills-only ("she rises" clip→new painted rising still); Jesus only from-behind (s5) / off-frame, never a face. **APPROVED by Cameron 2026-07-11** |
| 06 | Two Sons | matthew-21_two-sons | REWORK BUILT — stills-only — 2026-07-11 — Machine A (Dev). Cameron: the cut "was okay" but still had ONE motion clip (s04 "he went"). Replaced it with a painted still, so the video is now fully stills-only. Also fixed Cameron's wardrobe note: the working son (first son) wears RUST-BROWN/red (matches shot1/shot3 + CHARACTER-LOCKS); the son who didn't work wears cream/white — the old `went` still wrongly had the worker in white, regenerated in rust-brown. Rest of the approved cut unchanged. matthew-21_two-sons.mp4 (17.1 MB, 104s). Awaiting Cameron. |
| 07 | Peter walks on water | matthew-14_peter-water | REWORK BUILT — 2026-07-11 — Elli's Windows laptop — awaiting Cameron's verdict. Cameron's 3 picture fixes done & verified in the cut: (1) s5 walk (v5) — Peter from BEHIND going toward a distant Jesus (face not shown, Lord too far to show a face); (2) new s7-sink-alone still for the sinking beat so the hand-grab (s7-sink-v5) lands only at "And Jesus caught him," not during the sinking; (3) s9 walk-back (v3) — disciples now in the boat. Windows stills-only rebuild. matthew-14_peter-walks-on-water.mp4 (20.0MB, 4:16). build_win.py. |
| 08 | Lost Coin | luke-15_lost-coin | REWORK BUILT — 2026-07-11 — Elli's Windows laptop — approved by Cameron ("its good they are all good"). Stills-only: generated the 4 missing stills (count, lamp, sweep, found — parable, no Jesus figure; found has exactly ONE coin per the prop lock), fixed narrator off the Multilingual voice. luke-15_lost-coin.mp4 (15.3MB, 66s). build_win.py. |
| 09 | Rich Young Ruler | mark-10_rich-ruler | **APPROVED by Cameron 2026-07-11** ("9 is good I approve it"). Stills-only (Law E): 2 Veo clips (s1-run, s6-walk) → stills. s7 regenerated so the Lord is seen from DIRECTLY BEHIND (old s7 leaked a profile cheek/eye — #18 fixed); every other still is the rich young man, whose own face is allowed. mark-10_rich-young-ruler.mp4 (18.9MB, 217s). build_win.py. |
| 10 | Woman at the Well | john-4_well | **APPROVED by Cameron 2026-07-11** ("10 is good too"). Law E: 2 Veo clips (s5-conversation, s7-jar-run) → their existing anchor stills; alternating zoom on the long well conversation. #18 re-audit PASS with no regeneration — the Lord is only ever behind (s2) / over-the-shoulder (s5,s6), no face/glow. john-4_woman-at-the-well.mp4 (20.4MB, 311s). build_win.py. |
| 11 | Calming the Storm | mark-4_calming-the-storm | REDO QUEUE (Cameron rejected 2026-07-11): (1) Jesus's HAIR flips short↔long across scenes — standardize to LONG dark hair; (2) his clothing changes (once a white fur/fleece look) — standardize to ONE plain cream wool robe; (3) a side profile shows too much of his face — put him from BEHIND; (4) one scene reads as Jesus standing OUTSIDE the boat when he is IN it with them — fix to inside the hull. Apply THE JESUS LOOK STANDARD. |
| 12 | Blind Bartimaeus | mark-10_bartimaeus | REWORK BUILT — 2026-07-11 — Elli's Windows laptop — awaiting Cameron's verdict. Full STILLS-ONLY build under #18: 12 painted stills, all single continuous scenes (s6 caught & regenerated — Nano Banana had tiled it as a 3-panel comic). Jesus shown ONLY from behind / over-the-shoulder (s6,s9,s10a,s10b,s11) — no face, no glow. Healing arc reads (clouded blind eyes s2/s3/s5/s9/s10a → clear seeing eyes s10b). KJV j1 (Mark 10:51) + j2 (Mark 10:52) red-letter; bed dies to silence for the miracle. mark-10_bartimaeus.mp4 (19.0MB, 318s / 5:18). |
| 13 | Man through the Roof | mark-2_roof | **APPROVED by Cameron 2026-07-11** — built on linux desktop / Machine A (hostname Dev). s8 rebuilt under #16 (real Middle Eastern man, no readable face); 2 Veo clips done (20 cr); s4/s9 re-synced to clip start-frames; ear-check 16/16; self-revision loop passed. Final: mark-2_man-through-the-roof.mp4 (20.0 MB, 334s). |
| 14 | Ten Lepers | luke-17_ten-lepers | DONE — approved by Cameron 2026-07-11 ("yeah thats good"). V3 stills-only, #18 face-never, s7 fork fixed. Built by Elli's Windows laptop. |
| 15 | Centurion's Servant | matthew-8_centurion | **APPROVED by Cameron 2026-07-11** — built V2 on Cameron Lovett MS (Machine C). STILLS-ONLY (Law E), Jesus never shown (#18 face-gate PASS, all 6 Jesus stills from behind/over-shoulder), narration rewritten for clarity + captions VERBATIM every spoken word + KJV explained plainly + new inviting closing question. Ear-check 27/27. matthew-8_centurion.mp4 (22.2MB, 5:08). |
| 16 | Mary and Martha | luke-10_mary-martha | CLAIMED — 2026-07-11 — Machine A (Dev) — building fresh, STILLS-ONLY, face-gate PASS required |
| 17 | Lazarus | john-11_lazarus | BUILT — **FIX NEEDED before approval (Cameron, 2026-07-11): Lazarus beard continuity.** He has a full dark beard when sick (s1) and when he comes forth bound (s8), but is CLEAN-SHAVEN once loosed and embraced by his sisters (s9). Regenerate **s9.jpeg** with the same dark beard so he's the same man before and after the resurrection; then rebuild. (Elli's laptop owns this build — has the Flow project + build_win.py.) Everything else verified: STILLS-ONLY (Law E), face-gate PASS (#18), the Lord only ever behind/over-shoulder/distance (no face/glow), KJV red-letter j1–j5, music silent for "I am the resurrection", "Jesus wept", "Lazarus, come forth". john-11_lazarus.mp4 (19.8MB, 6:12). |
| 18 | Road to Emmaus | luke-24_emmaus | BUILT — awaiting Cameron — 2026-07-12 — Elli's Windows laptop. Fresh build under both standards: STILLS-ONLY + face-gate PASS (#18). 8 painted stills; the risen Lord is only ever behind / over-the-shoulder / hands (s2,s3,s4,s5,s6) — face never shown, then he vanishes (s7). KJV red-letter j1 (Luke 24:25-26); music silent for the recognition + vanishing. luke-24_emmaus.mp4 (20.0MB, 4:18). |
| 19 | Breakfast on the Shore | john-21_shore | **BUILT — awaiting Cameron approval — 2026-07-11 — Machine C (Cameron Lovett MS).** Fresh stills-only build from production pack. 7 hand-painted 2K stills, verbatim captions (#15 pattern), Jesus KJV j1 (21:16 "lovest thou me") + j2 (21:17 "Feed my sheep") explained plainly, music silent on the "lovest thou me" peak. Face-never verified: Jesus only from behind (s4,s5,s7) / hand-only (s6) / distance; s1 bound-Lord and s3 shore-figure were fixed to back-only after the 2K upscale leaked a face (Flow in-place edit). Charcoal fire is the emotional key (same fire as the denial). john-21_shore.mp4 (20.5MB, 184s). build.py (Linux, bin/ffmpeg). |
| 20 | Good Samaritan | luke-10_samaritan | **CLAIMED — 2026-07-12 — Machine A (Dev)** — building fresh, STILLS-ONLY (Law E) + Jesus face-never (#18 / face-gate PASS), hand-painted 2D storybook style. Parable: all characters shown fully; Jesus is the narrating voice and appears ONLY in the bookend shots as a seated storyteller from behind. From production pack `20-samaritan-production-pack.md`. |

## Rules recap (full text in PRODUCTION-BIBLE §0 and §1)

- Pull before claiming. Claim before generating. Push the claim immediately.
- 🛑 JESUS'S FACE IS NEVER PROMPTED OR SHOWN (Cameron, 2026-07-11). He is a real,
  warm, MIDDLE EASTERN human figure (hands & hair may show, NEVER white, never a
  hooded void) seen ONLY from behind / over-the-shoulder / at a distance — a mystery
  figure, because we don't know his face and a made-up face is not good worship.
  BEFORE any Flow credit, the prompt sheet MUST pass the gate:
  `python3 media-production/jesus_face_gate.py --dir <build-folder>` (exit 0). Read
  §1 "The Standing Laws" in the PRODUCTION-BIBLE in full before writing any prompt
  (the old numbered "Corrections #1–#18" are consolidated there now; history archived
  in CORRECTIONS-HISTORY.md). NOTE: the #14 and #15 prompt sheets were written under
  the dead "show his face" rule and FAIL the gate — restage before generating.
- Never run Chrome automation without announcing it to Cameron first and getting
  his go-ahead (Law C). Batch clicks into short announced bursts.
- Each machine works its own build-NN folder only. Shared Flow project is
  "MBM Story Videos — Wave One" — credits are shared, so no speculative renders.

## Machine lists — Wave Two ranking (rebuilt 2026-07-11 by the Cowork cloud session; the original list was lost with an old session that couldn't push)

> **How to use (Law A still governs):** each machine claims ONLY from its own
> list, top UNCLAIMED row first. `git pull` FIRST, mark the row CLAIMED with the
> date + machine, commit and push BEFORE generating anything. When Cameron
> approves, mark DONE. Rows 13-20 are Wave One stories (packs already written -
> fastest builds): their status lives in the Wave One table ABOVE - check it
> before claiming, and record claims for 13-20 THERE, not here. Any extra worker
> (e.g. a Cowork cloud session) claims from the Wave One table first, then may
> take a list's BOTTOM unclaimed row - never the top (the tops belong to the
> machines). #09 rework queue is separate and comes before new claims when
> Cameron calls for it. 99 stories total: every remaining pack-done story plus
> the strongest milk stories of THE-200 sections II-VIII, in catalog order,
> dealt round-robin so each machine gets a spread of parables, miracles,
> encounters, nativity, passion week, teachings, and Old Testament.

### MACHINE A — linux desktop (33 videos, ranked)

| Rank | Cat# | Story | File | Status |
|------|------|-------|------|--------|
| 1 | 13 | Man through the Roof | mark-2_roof | see Wave One table |
| 2 | 16 | Mary and Martha | luke-10_mary-martha | see Wave One table |
| 3 | 19 | Breakfast on the Shore | john-21_shore | see Wave One table |
| 4 | 22 | The Unmerciful Servant | matthew-18_unmerciful-servant | UNCLAIMED |
| 5 | 28 | Hidden Treasure | matthew-13_hidden-treasure | UNCLAIMED |
| 6 | 34 | The Rich Fool | luke-12_rich-fool | UNCLAIMED |
| 7 | 38 | The Persistent Widow | luke-18_persistent-widow | UNCLAIMED |
| 8 | 42 | The Barren Fig Tree Spared | luke-13_fig-tree-spared | UNCLAIMED |
| 9 | 54 | Water to Wine at Cana | john-2_water-to-wine | UNCLAIMED |
| 10 | 59 | The Leper: I Will, Be Clean | mark-1_i-will-be-clean | UNCLAIMED |
| 11 | 62 | Jairus's Daughter | mark-5_jairus-daughter | UNCLAIMED |
| 12 | 66 | The Syrophoenician Woman | mark-7_syrophoenician-woman | UNCLAIMED |
| 13 | 69 | The Man Born Blind | john-9_man-born-blind | UNCLAIMED |
| 14 | 72 | The Coin in the Fish's Mouth | matthew-17_coin-in-the-fish | UNCLAIMED |
| 15 | 82 | The Baptism of Jesus | matthew-3_baptism-of-jesus | UNCLAIMED |
| 16 | 87 | The Woman Who Washed His Feet | luke-7_she-washed-his-feet | UNCLAIMED |
| 17 | 90 | The Widow's Mite | mark-12_widows-mite | UNCLAIMED |
| 18 | 100 | Weeping over Jerusalem | luke-19_weeping-over-jerusalem | UNCLAIMED |
| 19 | 106 | Martha's Confession | john-11_marthas-confession | UNCLAIMED |
| 20 | 111 | With Desire I Have Desired | luke-22_with-desire | UNCLAIMED |
| 21 | 114 | No Room: the Manger | luke-2_no-room-manger | UNCLAIMED |
| 22 | 117 | The Wise Men | matthew-2_wise-men | UNCLAIMED |
| 23 | 120 | The Triumphal Entry | luke-19_triumphal-entry | UNCLAIMED |
| 24 | 126 | Peter's Denial and the Look | luke-22_peters-denial | UNCLAIMED |
| 25 | 131 | Father, Forgive Them | luke-23_father-forgive-them | UNCLAIMED |
| 26 | 136 | The Centurion at the Cross | mark-15_centurion-at-the-cross | UNCLAIMED |
| 27 | 144 | Lilies and Sparrows | matthew-6_lilies-and-sparrows | UNCLAIMED |
| 28 | 153 | I Am the Bread of Life | john-6_bread-of-life | UNCLAIMED |
| 29 | 162 | Where Art Thou? | genesis-3_where-art-thou | UNCLAIMED |
| 30 | 168 | Joseph Forgives His Brothers | genesis-45_joseph-forgives | UNCLAIMED |
| 31 | 171 | Ruth and the Redeemer | ruth-1_ruth-and-the-redeemer | UNCLAIMED |
| 32 | 174 | The Still Small Voice | 1-kings-19_still-small-voice | UNCLAIMED |
| 33 | 178 | Graven on His Palms | isaiah-49_graven-on-his-palms | UNCLAIMED |

### MACHINE B — HP laptop (33 videos, ranked)

| Rank | Cat# | Story | File | Status |
|------|------|-------|------|--------|
| 1 | 14 | Ten Lepers | luke-17_ten-lepers | see Wave One table |
| 2 | 17 | Jesus wept (Lazarus) | john-11_lazarus | see Wave One table |
| 3 | 20 | Good Samaritan | luke-10_samaritan | see Wave One table |
| 4 | 23 | Workers in the Vineyard | matthew-20_vineyard-workers | UNCLAIMED |
| 5 | 32 | The Talents | matthew-25_talents | UNCLAIMED |
| 6 | 35 | The Great Banquet | luke-14_great-banquet | UNCLAIMED |
| 7 | 39 | The Pharisee and the Publican | luke-18_pharisee-and-publican | UNCLAIMED |
| 8 | 44 | The Two Debtors | luke-7_two-debtors | UNCLAIMED |
| 9 | 56 | The First Catch of Fish | luke-5_first-catch | UNCLAIMED |
| 10 | 60 | The Withered Hand | mark-3_withered-hand | UNCLAIMED |
| 11 | 63 | Feeding the Five Thousand | john-6_feeding-five-thousand | UNCLAIMED |
| 12 | 67 | Ephphatha: the Deaf Man | mark-7_ephphatha | UNCLAIMED |
| 13 | 70 | The Pool of Bethesda | john-5_pool-of-bethesda | UNCLAIMED |
| 14 | 77 | Malchus's Ear | luke-22_malchus-ear | UNCLAIMED |
| 15 | 84 | Calling the Fishermen | matthew-4_calling-the-fishermen | UNCLAIMED |
| 16 | 88 | The Woman Taken in Adultery | john-8_neither-do-i-condemn | UNCLAIMED |
| 17 | 94 | Come Unto Me | matthew-11_come-unto-me | UNCLAIMED |
| 18 | 103 | Mary Magdalene Freed | luke-8_mary-magdalene-freed | UNCLAIMED |
| 19 | 108 | A Child in the Midst | mark-9_child-in-the-midst | UNCLAIMED |
| 20 | 112 | The Annunciation | luke-1_annunciation | UNCLAIMED |
| 21 | 115 | Shepherds and Angels | luke-2_shepherds-and-angels | UNCLAIMED |
| 22 | 118 | Flight to Egypt | matthew-2_flight-to-egypt | UNCLAIMED |
| 23 | 122 | Washing the Disciples' Feet | john-13_washing-feet | UNCLAIMED |
| 24 | 129 | Barabbas Goes Free | mark-15_barabbas | UNCLAIMED |
| 25 | 132 | The Thief on the Cross | luke-23_thief-on-the-cross | UNCLAIMED |
| 26 | 138 | The Empty Tomb | luke-24_empty-tomb | UNCLAIMED |
| 27 | 145 | Ask, Seek, Knock | matthew-7_ask-seek-knock | UNCLAIMED |
| 28 | 157 | I Am the Resurrection and the Life | john-11_resurrection-and-life | UNCLAIMED |
| 29 | 164 | The Rainbow Covenant | genesis-9_rainbow-covenant | UNCLAIMED |
| 30 | 169 | The Burning Bush | exodus-3_burning-bush | UNCLAIMED |
| 31 | 172 | Hannah Is Heard | 1-samuel-1_hannah-is-heard | UNCLAIMED |
| 32 | 175 | Naaman's Seven Dips | 2-kings-5_naamans-seven-dips | UNCLAIMED |
| 33 | 179 | The Fourth Man in the Fire | daniel-3_fourth-man-in-the-fire | UNCLAIMED |

### MACHINE C — Linux desktop number two (33 videos, ranked)

| Rank | Cat# | Story | File | Status |
|------|------|-------|------|--------|
| 1 | 15 | Centurion's Servant | matthew-8_centurion | CLAIMED — 2026-07-11 — Cameron Lovett MS (Machine C) — see Wave One table |
| 2 | 18 | Road to Emmaus | luke-24_emmaus | see Wave One table |
| 3 | 21 | The Lost Sheep | luke-15_lost-sheep | UNCLAIMED |
| 4 | 24 | The Sower | matthew-13_sower | UNCLAIMED |
| 5 | 33 | The Sheep and the Goats | matthew-25_sheep-and-goats | UNCLAIMED |
| 6 | 37 | The Rich Man and Lazarus | luke-16_rich-man-and-lazarus | UNCLAIMED |
| 7 | 40 | The Friend at Midnight | luke-11_friend-at-midnight | UNCLAIMED |
| 8 | 47 | Houses on Rock and Sand | matthew-7_houses-rock-and-sand | UNCLAIMED |
| 9 | 58 | Peter's Mother-in-law | mark-1_peters-mother-in-law | UNCLAIMED |
| 10 | 61 | The Widow of Nain's Son | luke-7_widow-of-nain | UNCLAIMED |
| 11 | 65 | The Gerasene Demoniac | mark-5_gerasene | UNCLAIMED |
| 12 | 68 | The Blind Man at Bethsaida | mark-8_two-touches | UNCLAIMED |
| 13 | 71 | Help Thou Mine Unbelief | mark-9_help-mine-unbelief | UNCLAIMED |
| 14 | 79 | Evening at the Door | mark-1_evening-at-the-door | UNCLAIMED |
| 15 | 85 | Calling Matthew | matthew-9_calling-matthew | UNCLAIMED |
| 16 | 89 | Suffer the Little Children | mark-10_suffer-the-children | UNCLAIMED |
| 17 | 99 | The Anointing at Bethany | mark-14_anointing-at-bethany | UNCLAIMED |
| 18 | 104 | John the Baptist's Doubt | matthew-11_john-baptists-doubt | UNCLAIMED |
| 19 | 109 | Teach Us to Pray | luke-11_teach-us-to-pray | UNCLAIMED |
| 20 | 113 | Joseph's Dream | matthew-1_josephs-dream | UNCLAIMED |
| 21 | 116 | Simeon and Anna | luke-2_simeon-and-anna | UNCLAIMED |
| 22 | 119 | The Boy in the Temple | luke-2_boy-in-the-temple | UNCLAIMED |
| 23 | 124 | Gethsemane | luke-22_gethsemane | UNCLAIMED |
| 24 | 130 | Simon of Cyrene | mark-15_simon-of-cyrene | UNCLAIMED |
| 25 | 133 | Behold Thy Mother | john-19_behold-thy-mother | UNCLAIMED |
| 26 | 139 | Mary at the Tomb: Her Name | john-20_mary-at-the-tomb | UNCLAIMED |
| 27 | 146 | The Lord's Prayer: Our Father | matthew-6_our-father | UNCLAIMED |
| 28 | 159 | The Vine and the Branches | john-15_vine-and-branches | UNCLAIMED |
| 29 | 166 | The Ram in the Thicket | genesis-22_ram-in-the-thicket | UNCLAIMED |
| 30 | 170 | The Brazen Serpent | numbers-21_brazen-serpent | UNCLAIMED |
| 31 | 173 | The Shepherd Psalm | psalm-23_shepherd-psalm | UNCLAIMED |
| 32 | 176 | Jonah and the God Who Relents | jonah-3_jonah-and-nineveh | UNCLAIMED |
| 33 | 180 | Job Answered from the Whirlwind | job-38_answered-from-the-whirlwind | UNCLAIMED |

