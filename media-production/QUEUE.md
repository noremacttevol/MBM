# MBM VIDEO QUEUE — the one board every computer reads

> **This file replaces the old per-machine lists.** Any computer, any fresh chat,
> reads THIS file, grabs the next unclaimed story, builds it, ticks the boxes,
> pushes. That's the whole system. No re-explaining, no assigning by hand.

**Next job = the lowest-numbered row where `Built` is ⬜ and `Claim` is empty.**
Because build folders match the catalog exactly, that is simply the next number
down `THE-200.md`. Right now: **#39, The Pharisee and the Publican.**

---

## ▶ HOW A FRESH CHAT STARTS (paste this, or just run `next-job.sh`)

```
You are on MBM video production. Do this before anything else:
1. cd to the MBM repo, `git pull --rebase origin main`.
2. Open media-production/QUEUE.md. Find the NEXT JOB (lowest row where Built is ⬜
   and Claim is empty). If I named a number, use that instead.
3. CLAIM it: make the build-NN folder, put your machine+date in that row's Claim
   column, commit and push BEFORE generating anything. If push rejects, pull and
   re-pick — someone beat you to it.
4. Read PRODUCTION-BIBLE.md + CREW-GUIDE.md. Every law binds you.
5. Build it end to end: prompt sheet → pass jesus_face_gate.py → (Flow picture
   burst, ask me first — one chat drives Chrome at a time) → narration → assemble
   → full Self-Revision QC. Tick Prep/Built as you go, push each change.
6. Tell me it's built and waiting. I watch it once and say yes. Then tick Appr.
```

That's it. You never write prompts, never fix bugs, never assign work. The chat
finds its own job.

---

## 🟡 WAITING ON YOUR YES — 17 videos built and ready to review

These are done and just need you to watch and approve (then the chat ticks `Appr`
and posts them). Knock these out anytime:

**#16 Mary & Martha · #18 Emmaus · #19 Shore · #22 Unmerciful Servant · #24 Sower ·
#26 Mustard Seed · #27 Leaven · #28 Hidden Treasure · #29 Pearl · #30 Net ·
#31 Ten Virgins · #32 Talents · #33 Sheep & Goats · #34 Rich Fool ·
#35 Great Banquet · #36 Shrewd Steward · #37 Rich Man & Lazarus · #38 Persistent Widow ·
#39 The Pharisee & the Publican · **#40 The Friend at Midnight**

Watch links are in [`STATUS.md`](../STATUS.md).

---

## 🔧 FIX QUEUE — videos that need a redo

**None open right now.** The three fixes from 2026-07-13 (#07 s3 figure, #29 s2 hand,
#31 s3 lamps) all shipped, and the #11 Storm full redo shipped. When you reject a
video, its chat moves the row here with a one-line reason and un-ticks `Appr`:

| # | Story | What's wrong | Claimed by |
|---|-------|--------------|-----------|
| — | — | (empty) | — |

---

## THE QUEUE (1–200)

Legend: ⬜ not done · ✅ done · 🔨 being worked. Columns: **Prep** (pack + prompt
sheet ready) · **Built** (final mp4 exists) · **Appr** (Cameron approved) ·
**Post** (live on milk-b4-meat.web.app / in the app).

| # | Story | Ref | Prep | Built | Appr | Post | Claim / notes |
|---|-------|-----|------|-------|------|------|----------------|
| 1 | Woman who touched his cloak | Mark 5 | ✅ | ✅ | ✅ | ✅ | live |
| 2 | The Prodigal Son | Luke 15 | ✅ | ✅ | ✅ | ✅ | live |
| 3 | Zacchaeus | Luke 19 | ✅ | ✅ | ✅ | ✅ | live |
| 4 | Nicodemus at night | John 3 | ✅ | ✅ | ✅ | ✅ | live |
| 5 | The bent-over woman | Luke 13 | ✅ | ✅ | ✅ | ✅ | live |
| 6 | The two sons | Matt 21 | ✅ | ✅ | ✅ | ✅ | live |
| 7 | Peter walks on water | Matt 14 | ✅ | ✅ | ✅ | ✅ | live (s3 fix shipped 07-13) |
| 8 | The lost coin | Luke 15 | ✅ | ✅ | ✅ | ✅ | live |
| 9 | The rich young ruler | Mark 10 | ✅ | ✅ | ✅ | ✅ | live |
| 10 | The woman at the well | John 4 | ✅ | ✅ | ✅ | ✅ | live |
| 11 | Calming the storm | Mark 4 | ✅ | ✅ | ✅ | ✅ | live (full redo shipped) |
| 12 | Blind Bartimaeus | Mark 10 | ✅ | ✅ | ✅ | ✅ | live |
| 13 | Through the roof | Mark 2 | ✅ | ✅ | ✅ | ✅ | live |
| 14 | The ten lepers | Luke 17 | ✅ | ✅ | ✅ | ✅ | live |
| 15 | The centurion | Matt 8 | ✅ | ✅ | ✅ | ✅ | live |
| 16 | Mary and Martha | Luke 10 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 17 | Jesus wept (Lazarus) | John 11 | ✅ | ✅ | ✅ | ✅ | live (beard fix shipped) |
| 18 | The road to Emmaus | Luke 24 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 19 | Breakfast on the shore | John 21 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 20 | The Good Samaritan | Luke 10 | ✅ | ✅ | ✅ | ⬜ | approved 07-12 — confirm posted |
| 21 | The lost sheep | Luke 15 | ✅ | ✅ | ✅ | ⬜ | approved 07-12 — confirm posted |
| 22 | The unmerciful servant | Matt 18 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 23 | Workers in the vineyard | Matt 20 | ✅ | ✅ | ✅ | ⬜ | approved 07-12 — confirm posted |
| 24 | The sower | Matt 13 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 25 | Wheat and tares | Matt 13 | ✅ | ✅ | ✅ | ⬜ | approved 07-12 — confirm posted |
| 26 | The mustard seed | Matt 13 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 27 | The leaven | Matt 13 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 28 | Hidden treasure | Matt 13 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 29 | The pearl of great price | Matt 13 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes (s2 fix shipped) |
| 30 | The net | Matt 13 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 31 | The ten virgins | Matt 25 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes (s3 fix shipped) |
| 32 | The talents | Matt 25 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 33 | The sheep and the goats | Matt 25 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 34 | The rich fool | Luke 12 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 35 | The great banquet | Luke 14 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 36 | The shrewd steward | Luke 16 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 37 | The rich man and Lazarus | Luke 16 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 38 | The persistent widow | Luke 18 | ✅ | ✅ | ✅ | ⬜ | approved by Cameron 2026-07-13 |
| 39 | The Pharisee and the publican | Luke 18 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 40 | The friend at midnight | Luke 11 | ✅ | ✅ | ⬜ | ⬜ | awaiting your yes |
| 41 | Counting the cost | Luke 14 | ⬜ | ⬜ | ⬜ | ⬜ | CLAIMED Dev 2026-07-13 (driver) |
| 42 | The barren fig tree spared | Luke 13 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 43 | The wedding garment | Matt 22 | ⬜ | ⬜ | ⬜ | ⬜ | CLAIMED Dev / Machine A 2026-07-13 |
| 44 | The two debtors | Luke 7 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 45 | The wicked tenants | Mark 12 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 46 | The seed growing secretly | Mark 4 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 47 | Houses on rock and sand | Matt 7 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 48 | New wine, old bottles | Mark 2 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 49 | The lamp on a stand | Mark 4 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 50 | The watching servants | Mark 13 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 51 | Unprofitable servants | Luke 17 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 52 | The children in the marketplace | Luke 7 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 53 | The tower builder and the king | Luke 14 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 54 | Water to wine at Cana | John 2 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 55 | The nobleman's son | John 4 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 56 | The first catch of fish | Luke 5 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 57 | The demoniac in the synagogue | Mark 1 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 58 | Peter's mother-in-law | Mark 1 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 59 | The leper: I will, be clean | Mark 1 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 60 | The withered hand | Mark 3 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 61 | The widow of Nain's son | Luke 7 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 62 | Jairus's daughter | Mark 5 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 63 | Feeding the five thousand | John 6 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 64 | Feeding the four thousand | Mark 8 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 65 | The Gerasene demoniac | Mark 5 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 66 | The Syrophoenician woman | Mark 7 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 67 | Ephphatha: the deaf man | Mark 7 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 68 | The blind man at Bethsaida | Mark 8 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 69 | The man born blind | John 9 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 70 | The pool of Bethesda | John 5 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 71 | Help thou mine unbelief | Mark 9 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 72 | The coin in the fish's mouth | Matt 17 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 73 | The man with dropsy | Luke 14 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 74 | Two blind men in the house | Matt 9 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 75 | The mute demoniac speaks | Matt 9 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 76 | The withered fig tree | Mark 11 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 77 | Malchus's ear | Luke 22 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 78 | The Transfiguration | Mark 9 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 79 | Evening at the door | Mark 1 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 80 | Multitudes on the mountain | Matt 15 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 81 | Nazareth: only a few | Mark 6 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 82 | The baptism of Jesus | Matt 3 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 83 | The temptations | Matt 4 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 84 | Calling the fishermen | Matt 4 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 85 | Calling Matthew | Matt 9 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 86 | Nazareth synagogue: this day fulfilled | Luke 4 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 87 | The woman who washed his feet | Luke 7 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 88 | The woman taken in adultery | John 8 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 89 | Suffer the little children | Mark 10 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 90 | The widow's mite | Mark 12 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 91 | Peter's confession | Matt 16 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 92 | Who is my mother? | Mark 3 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 93 | The seventy sent | Luke 10 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 94 | Come unto me, all ye that labour | Matt 11 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 95 | The Samaritan village refused | Luke 9 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 96 | The request of James and John | Mark 10 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 97 | Render unto Caesar | Mark 12 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 98 | The scribe near the kingdom | Mark 12 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 99 | The anointing at Bethany | Mark 14 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 100 | Weeping over Jerusalem | Luke 19 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 101 | Cleansing the temple | John 2 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 102 | The Greeks seek Jesus; the Father answers | John 12 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 103 | Mary Magdalene freed | Luke 8 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 104 | John the Baptist's doubt | Matt 11 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 105 | The cliff at Nazareth | Luke 4 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 106 | Martha's confession | John 11 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 107 | Forbid him not | Mark 9 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 108 | A child in the midst | Mark 9 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 109 | Lord, teach us to pray | Luke 11 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 110 | Get thee behind me | Matt 16 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 111 | With desire I have desired | Luke 22 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 112 | The annunciation | Luke 1 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 113 | Joseph's dream | Matt 1 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 114 | No room: the manger | Luke 2 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 115 | Shepherds and angels | Luke 2 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 116 | Simeon and Anna | Luke 2 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 117 | The wise men | Matt 2 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 118 | Flight to Egypt | Matt 2 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 119 | The boy in the temple | Luke 2 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 120 | The triumphal entry | Luke 19 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 121 | The last supper | Luke 22 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 122 | Washing the disciples' feet | John 13 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 123 | The intercessory prayer | John 17 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 124 | Gethsemane | Luke 22 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 125 | The betrayal kiss | Matt 26 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 126 | Peter's denial and the look | Luke 22 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 127 | Silent before accusers | Mark 14 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 128 | Pilate: What is truth? | John 18 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 129 | Barabbas goes free | Mark 15 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 130 | Simon of Cyrene | Mark 15 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 131 | Father, forgive them | Luke 23 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 132 | The thief on the cross | Luke 23 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 133 | Behold thy mother | John 19 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 134 | My God, why hast thou forsaken me? | Mark 15 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 135 | It is finished; the veil torn | John 19 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 136 | The centurion at the cross | Mark 15 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 137 | Buried by secret disciples | John 19 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 138 | The empty tomb | Luke 24 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 139 | Mary at the tomb: her name | John 20 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 140 | Flesh and bone; Thomas's hands | Luke 24 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 141 | The ascension | Acts 1 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 142 | The Beatitudes | Matt 5 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 143 | Salt and light | Matt 5 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 144 | Lilies and sparrows | Matt 6 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 145 | Ask, seek, knock | Matt 7 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 146 | The Lord's Prayer: Our Father | Matt 6 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 147 | The mote and the beam | Matt 7 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 148 | The golden rule | Matt 7 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 149 | Love your enemies | Matt 5 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 150 | Treasures in heaven | Matt 6 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 151 | The strait gate | Matt 7 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 152 | By their fruits | Matt 7 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 153 | I am the bread of life | John 6 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 154 | I am the light of the world | John 8 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 155 | I am the door | John 10 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 156 | Other sheep I have | John 10 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 157 | I am the resurrection and the life | John 11 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 158 | I am the way, the truth, and the life | John 14 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 159 | The vine and the branches | John 15 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 160 | In my Father's house are many mansions | John 14 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 161 | My sheep hear my voice | John 10 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 162 | Where art thou? | Gen 3 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 163 | Enoch walked with God | Gen 5 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 164 | The rainbow covenant | Gen 9 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 165 | Abraham argues for Sodom | Gen 18 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 166 | The ram in the thicket | Gen 22 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 167 | Jacob's ladder | Gen 28 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 168 | Joseph forgives his brothers | Gen 45 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 169 | The burning bush | Ex 3 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 170 | The brazen serpent | Num 21 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 171 | Ruth and the redeemer | Ruth | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 172 | Hannah is heard | 1 Sam 1 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 173 | The Shepherd Psalm | Ps 23 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 174 | The still small voice | 1 Kgs 19 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 175 | Naaman's seven dips | 2 Kgs 5 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 176 | Jonah and the God who relents | Jonah | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 177 | Hosea buys her back | Hosea 1 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 178 | Graven on his palms | Isa 49 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 179 | The fourth man in the fire | Dan 3 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 180 | Job answered from the whirlwind | Job 38 | ⬜ | ⬜ | ⬜ | ⬜ |  |
| 181 | Night without darkness | 3 Ne 1 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 182 | The voice in the darkness | 3 Ne 9 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 183 | Behold my Beloved Son | 3 Ne 11 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 184 | One by one | 3 Ne 11 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 185 | Have ye any that are sick? | 3 Ne 17 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 186 | He blessed the children one by one | 3 Ne 17 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 187 | And behold, my joy is full | 3 Ne 17 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 188 | The sacrament at Bountiful | 3 Ne 18 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 189 | The prayer that could not be written | 3 Ne 19 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 190 | Ye are they of whom I said: other sheep | 3 Ne 15 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 191 | The brother of Jared sees his finger | Ether 3 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 192 | Alma the Younger | Mosiah 27 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 193 | Enos's wrestle | Enos 1 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 194 | King Lamoni and Abish | Alma 19 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 195 | They buried their weapons | Alma 24 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 196 | Abinadi's fire | Mosiah 13 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 197 | Enoch sees God weep | Moses 7 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 198 | This is my work and my glory | Moses 1 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 199 | Liberty Jail | D&C 121 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |
| 200 | The First Vision | JS–H 1 | ⬜ | ⬜ | ⬜ | ⬜ | §IX post-signal |

---

## Claim protocol (the only rule that keeps 4 computers from colliding)

1. **Pull first:** `git pull --rebase origin main`.
2. **Claim before generating:** create `build-NN-<slug>/`, write your machine +
   date into that row's `Claim` column, `git commit`, `git push`. If the push is
   rejected, someone claimed it while you were reading — pull and take the next
   open row.
3. **One machine, one video at a time.** Finish or release before claiming another.
4. **Tick boxes in the same commit as the work**, and push right away, so every
   other computer sees the truth.
5. **Chrome/Flow: one chat drives it at a time.** Ask Cameron before any browser
   step. Everything else (script, narration, QC, assembly of banked art) is safe
   to do while another chat has the browser.

Deep mechanics and the full law set live in `PRODUCTION-BIBLE.md`. The old
`VIDEO-ASSIGNMENTS.md` per-machine lists are retired — this file is the board now.
