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
- **Videos #6–#10** — **CLAIMED by Machine C (Cameron Lovett MS)** — 2026-07-11. #07/#09/#10
  have their pictures+narration on this box (rebuildable pictures-only here with bin/ffmpeg);
  #06/#08 have only their scripts here (rendered assets were never pushed — regenerate from the
  saved prompts, or the machine that built them pushes the assets).

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
| 01 | Woman who touched his cloak | mark-5_cloak | REDONE 2026-07-11 Machine A (Dev) — stills-only; Jesus new look (s03 walking-away no-hood dark hair; s09 "who touched" from directly behind; s07 hem clip→hand-on-tassels still). Awaiting Cameron approval |
| 02 | Prodigal Son | luke-15_prodigal | REDONE 2026-07-11 Machine A (Dev) — stills-only (father-runs clip→new painted running still); parable, no Jesus figure. Awaiting Cameron approval |
| 03 | Zacchaeus | luke-19_zacchaeus | REDONE 2026-07-11 Machine A (Dev) — stills-only (lookup clip→anchor still); Jesus already new look (from-behind, dark hair, no hood every beat). Awaiting Cameron approval |
| 04 | Nicodemus | john-3_nicodemus | REDONE 2026-07-11 Machine A (Dev) — stills-only ("came at night" clip→new painted night-street still); Jesus only ever shown from behind (dark seated figure), never a face. Awaiting Cameron approval |
| 05 | Bent Woman | luke-13_bent-woman | REDONE 2026-07-11 Machine A (Dev) — stills-only ("she rises" clip→new painted rising still); Jesus only from-behind (s5) / off-frame, never a face. Awaiting Cameron approval |
| 06 | Two Sons | matthew-21_two-sons | DONE — approved |
| 07 | Peter walks on water | matthew-14_peter-water | DONE — approved (after V5) |
| 08 | Lost Coin | luke-15_lost-coin | DONE — approved |
| 09 | Rich Young Ruler | mark-10_rich-ruler | REWORK QUEUE — re-audit vs §1 "The Standing Laws" (incl. face-never) before any new claim |
| 10 | Woman at the Well | john-4_well | DONE — approved (V3, "thats good on to the next") |
| 11 | Calming the Storm | mark-4_calming-the-storm | REWORK BUILT — 2026-07-11 — Elli's Windows laptop — awaiting Cameron's verdict. All 6 hooded-Jesus stills (s1,s4,s5,s6,s7,s8) restaged under #18 (real Middle-Eastern man from behind, dark hair, no hood-void, kept night, inside boat) + regenerated; 2 Veo clips REMOVED → stills-only; rebuilt on Windows. mark-4_calming-the-storm.mp4 (19.6MB, 264s). |
| 12 | Blind Bartimaeus | mark-10_bartimaeus | CLAIMED — 2026-07-11 — Elli's Windows laptop (Cameron reassigned 11+12). Pre-flight exists; needs full STILLS-ONLY build under #18. |
| 13 | Man through the Roof | mark-2_roof | BUILT — awaiting Cameron approval — 2026-07-11 — linux desktop / Machine A (hostname Dev). s8 rebuilt under #16 (real Middle Eastern man, no readable face); 2 Veo clips done (20 cr); s4/s9 re-synced to clip start-frames; ear-check 16/16; self-revision loop passed. Final: mark-2_man-through-the-roof.mp4 (20.0 MB, 334s). |
| 14 | Ten Lepers | luke-17_ten-lepers | DONE — approved by Cameron 2026-07-11 ("yeah thats good"). V3 stills-only, #18 face-never, s7 fork fixed. Built by Elli's Windows laptop. |
| 15 | Centurion's Servant | matthew-8_centurion | CLAIMED — 2026-07-11 — Cameron Lovett MS (Machine C, rotation rank 1) |
| 16 | Mary and Martha | luke-10_mary-martha | UNCLAIMED |
| 17 | Lazarus | john-11_lazarus | UNCLAIMED |
| 18 | Road to Emmaus | luke-24_emmaus | UNCLAIMED |
| 19 | Breakfast on the Shore | john-21_shore | UNCLAIMED |
| 20 | Good Samaritan | luke-10_samaritan | UNCLAIMED |

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

