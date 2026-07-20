# REPEAT AUDIT — all 200 rows, 2026-07-20 (Cameron ordered)

Cameron found repeats in the feed and asked why. This is the full answer, the fix,
and the rule that stops it happening again.

## Why the repeats happened

THE-200 v2 was designed with an assumption that turned out wrong. Four verses were
deliberately put on TWO shelves — an unnamed version on BRIDGE ("look what the Bible
says") and a named version on MEMBER ("and here is what it means for the Restoration").
That design forgot one thing the spec itself says: **shelves are cumulative.** A member's
pool is rows 1–200, so a member gets BOTH videos of the same verse in one feed. To the
viewer that is a repeat, full stop. On top of that, two story-level dupes slipped
through review (same event told from two gospels; same parable told twice).

## The six repeats — and what replaced them

Rule applied: keep the MEMBER version (it carries the doctrine and the Gospel Library
pointer; row 185 is already live), replace the BRIDGE copy with a NEW story that serves
the same wound. Old builds are ARCHIVED in place — folder untouched, nothing deleted.

| Row | Was (dupe of) | Now | Why the new story |
|---|---|---|---|
| 71 | Calling the fishermen, Matt 4 (same calling event as #51 first catch, Luke 5 — two videos of Jesus at the boats saying "fishers of men") | **Simeon and Anna — Luke 2** | #51 keeps the calling (Luke 5:10 has "thou shalt catch men" — nothing lost). Simeon & Anna was cut only for space and strengthens the thin infancy arc (manger, shepherds, wise men, boy in temple). |
| 128 | The famine of hearing, Amos 8 (exact dupe of #156) | **"Their heart is far from me" — Mark 7:6–13** | Jesus himself on traditions of men making the word of God of none effect — the exact "religion feels dead" wound, in Jesus's own voice. Quietly the strongest creed-vs-scripture bridge verse in the book. |
| 133 | Many mansions, John 14:2 (exact dupe of #185, which is LIVE) | **What Jesus called hell — Mark 9:43–48 / Matt 5:22** | Cameron asked for this one by name. The word Jesus used was Gehenna — the valley of Hinnom, a real burning place outside the wall. The eternal-torture-chamber picture came from later tradition, not from him. Judgment is real; the torturer God is not. |
| 134 | Other sheep, John 10:16 (exact dupe of #159 — the Book of Mormon pointer stays on MEMBER where it belongs) | **"Today shalt thou be with me in paradise" — Luke 23:43 + John 20:17** | Where did the thief go that day? Not final heaven — three days later Jesus says "I am not yet ascended." The Bible itself shows more geography to mercy than one-heaven-one-chance allows. Asks the better question. |
| 137 | Stephen sees him standing, Acts 7 (exact dupe of #179) | **"One, as we are one" — John 17:20–23** | Jesus prays that his followers become one THE SAME WAY he and the Father are one. If John 10:30 oneness meant one being, this prayer would be asking believers to melt into one person. Perfect unity, distinct persons — the Godhead, from Jesus's own lips, no church named. |
| 140 | The road to the far country runs both ways (a second telling of #2 The Prodigal Son, which is APPROVED) | **Naaman washes — 2 Kgs 5** | For the returner: the great man who almost missed his healing because the instruction was too simple. "Wash, and be clean" — do the simple thing again. Was flagged in v2's own cut list as first in line. |

Archived builds (folders kept, file kept, just no longer in the 200):
build-71-calling-the-fishermen · build-128-famine-of-hearing · build-133-many-mansions ·
build-134-other-sheep-i-have · build-137-stephen-sees-him-standing · build-140-road-runs-both-ways

## Same-scene pairs that STAY (checked, ruled add-ons, not repeats)

These share a scene across shelves but teach different things. They are the "add on
to what came before" model Cameron described — kept, with the add-on rule below.

| Pair | Ruling |
|---|---|
| #4 Nicodemus / #168 Born of water & Spirit | Story vs. baptism doctrine from the same night. Keep. |
| #69 Baptism of Jesus / #169 To fulfil all righteousness | Life-arc event vs. Godhead-distinct doctrine. Keep. |
| #103 Peter's confession / #162 Keys of the kingdom | Revelation vs. authority — two halves of Matt 16. Keep. |
| #89 Last supper / #170 The sacrament, worthily | The night vs. Paul's weekly-covenant teaching. Keep. |
| #44 Two debtors / #74 Woman who washed his feet | The parable vs. the woman it was told for. Keep (#44 approved). |
| #17 Lazarus / #144 I am the resurrection | Event vs. the "I AM." When #17 gets its deferred redo, keep it on the weeping and the raising — the saying belongs to #144. |
| #146 Vine / #167 Chosen and ordained | Different verses of John 15, different doctrine. Keep. |
| #35 Great banquet / #43 Wedding garment | Variant parables, both APPROVED — both stay. |
| #58 Feeding 5000 / #59 Feeding 4000 | Jesus himself treats them as two events (Mark 8:19–20). Keep. |

## The rule going forward (add to any future corpus work)

1. **One verse, one video, per cumulative pool.** Before adding a row, grep the full
   1–200 for the reference. Same verse on two shelves = repeat, because members see both.
2. **Same scene twice is allowed ONLY as an add-on:** the later video must open by
   building on the earlier one and teach something the first didn't — never retell.
3. **Are there enough good stories? Yes.** The v2 cut lists alone still hold surplus
   (burning bush, brazen serpent, annunciation, Simon of Cyrene, centurion at the
   cross, treasures in heaven…). Running out of Bible is not a risk; picking without
   checking for repeats was the only problem.

## Status after this audit

Rows 71, 128, 133, 134, 137, 140 reset to unbuilt in QUEUE.md with the new stories.
Everything Cameron approved is untouched. Members' shelf (151–200) untouched.
