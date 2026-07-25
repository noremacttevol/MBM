# STORY-BLUEPRINT COVERAGE REPORT

Generated 2026-07-24 after prescribing all 200. `presc` = pictures the story
reads to (beat count in each PRESCRIPTION.md). `cur` = distinct stills the current
build uses. `gap` = new pictures to generate. This is the BUILD priority queue.

## Headline
- **198 of 200 videos prescribed** (133 & 134 blocked — see below).
- **133 videos are under-pictured**; **56 badly starved** (gap ≥ 4).
- **~496 new pictures** to generate across the corpus to tell every story fully.
- Flow is unlimited — this is a picture-generation backlog, not a cost problem.

> NOTE: build-02-prodigal and build-08-lost-coin show cur=0 — false zero; their
> build.py uses a non-S# still-naming scheme the counter can't read. Check by hand.

## Blocked — need a narration build authored FIRST, then a prescription
- **133** — row reassigned 2026-07-20 to "What Jesus called hell / Gehenna" (Mark 9:43–48).
  Only the archived dupe (many-mansions, = live #185) is on disk. No make_narration.py.
- **134** — row reassigned to "Today… in paradise" (Luke 23:43 + John 20:17).
  Only the archived dupe (other-sheep, = #159) is on disk. No make_narration.py.
  DRAFTS/row-133.md and row-134.md exist as starting points.

## Reconciliation flags (data, not blockers)
- **71** — folder is build-71-the-great-commission (Matt 28) but THE-200 row 71 =
  "Simeon and Anna" (Luke 2). Prescribed to the actual narration. Your call which wins.
- **128** — canonical narration ("heart is far from me", Mark 7) lives only in
  _stale-dupes/build-128-heart-far-from-me/. Prescription written there; move it if promoted.
- Pre-SPEAKER-LAW template (Jesus=Christopher voice; caption-colour migration only, no
  picture change): 15, 136, 138, 139, 200 (flagged in-file; another chat owns the voice pass).

## Build priority queue — most starved first (gap ≥ 4)
```
2   build-02-prodigal                   18    0    18  <== +18
57  build-57-jairus-daughter            21    9    12  <== +12
17  build-17-lazarus                    20    9    11  <== +11
4   build-04-nicodemus                  21   11    10  <== +10
22  build-22-unmerciful-servant         18    8    10  <== +10
74  build-74-woman-washed-his-feet      18    9     9  <== +9
63  build-63-man-born-blind             18    9     9  <== +9
37  build-37-rich-man-lazarus           17    8     9  <== +9
20  build-20-samaritan                  17    8     9  <== +9
8   build-08-lost-coin                   8    0     8  <== +8
147 build-147-joseph-forgives           15    7     8  <== +8
97  build-97-the-empty-tomb             15    8     7  <== +7
92  build-92-peters-denial              15    8     7  <== +7
70  build-70-temptations                16    9     7  <== +7
66  build-66-malchus-ear                14    7     7  <== +7
60  build-60-gerasene-demoniac          16    9     7  <== +7
32  build-32-talents                    14    7     7  <== +7
31  build-31-ten-virgins                14    7     7  <== +7
119 build-119-fourth-man-in-fire        17   10     7  <== +7
115 build-115-ram-in-the-thicket        17   10     7  <== +7
101 build-101-still-small-voice         17   10     7  <== +7
98  build-98-mary-her-name              14    8     6  <== +6
93  build-93-barabbas-goes-free         13    7     6  <== +6
85  build-85-shepherds-and-angels       15    9     6  <== +6
23  build-23-vineyard                   14    8     6  <== +6
19  build-19-shore                      17   11     6  <== +6
120 build-120-job-from-whirlwind        16   10     6  <== +6
114 build-114-abraham-sodom             16   10     6  <== +6
99  build-99-flesh-and-bone-thomas      14    9     5  <== +5
7   build-07-peter-water                15   10     5  <== +5
75  build-75-woman-taken-in-adultery    15   10     5  <== +5
68  build-68-multitudes-mountain        13    8     5  <== +5
65  build-65-help-mine-unbelief         13    8     5  <== +5
58  build-58-feeding-5000               14    9     5  <== +5
25  build-25-wheat-and-tares            13    8     5  <== +5
24  build-24-sower                      12    7     5  <== +5
16  build-16-mary-martha                11    6     5  <== +5
14  build-14-ten-lepers                 17   12     5  <== +5
13  build-13-roof                       15   10     5  <== +5
12  build-12-bartimaeus                 15   10     5  <== +5
118 build-118-jonah-god-who-relents     15   10     5  <== +5
9   build-09-rich-ruler                 12    8     4  <== +4
96  build-96-it-is-finished             12    8     4  <== +4
91  build-91-gethsemane                 16   12     4  <== +4
89  build-89-the-last-supper            13    9     4  <== +4
86  build-86-the-wise-men               12    8     4  <== +4
82  build-82-anointing-at-bethany       12    8     4  <== +4
79  build-79-the-seventy-sent           12    8     4  <== +4
69  build-69-baptism                    13    9     4  <== +4
44  build-44-two-debtors                12    8     4  <== +4
40  build-40-the-friend-at-midnight     20   16     4  <== +4
33  build-33-sheep-goats                11    7     4  <== +4
1   build-01-cloak                      15   11     4  <== +4
148 build-148-ruth-and-the-redeemer     13    9     4  <== +4
140 build-140-naaman-washes             15   11     4  <== +4
11  build-11-storm                      13    9     4  <== +4
```

## Full table (all 200)
```
#   build                            presc  cur   gap
1   build-01-cloak                      15   11     4  <== +4
2   build-02-prodigal                   18    0    18  <== +18
3   build-03-zacchaeus                  14   11     3
4   build-04-nicodemus                  21   11    10  <== +10
5   build-05-bent-woman                 13   11     2
6   build-06-two-sons                   11    8     3
7   build-07-peter-water                15   10     5  <== +5
8   build-08-lost-coin                   8    0     8  <== +8
9   build-09-rich-ruler                 12    8     4  <== +4
10  build-10-well                       19   42   -23  (ok)
11  build-11-storm                      13    9     4  <== +4
12  build-12-bartimaeus                 15   10     5  <== +5
13  build-13-roof                       15   10     5  <== +5
14  build-14-ten-lepers                 17   12     5  <== +5
15  build-15-centurion                  15   12     3
16  build-16-mary-martha                11    6     5  <== +5
17  build-17-lazarus                    20    9    11  <== +11
18  build-18-emmaus                     19   16     3
19  build-19-shore                      17   11     6  <== +6
20  build-20-samaritan                  17    8     9  <== +9
21  build-21-lost-sheep                 10    7     3
22  build-22-unmerciful-servant         18    8    10  <== +10
23  build-23-vineyard                   14    8     6  <== +6
24  build-24-sower                      12    7     5  <== +5
25  build-25-wheat-and-tares            13    8     5  <== +5
26  build-26-mustard-seed                8    6     2
27  build-27-leaven                      8    7     1
28  build-28-hidden-treasure             7    7     0  (ok)
29  build-29-pearl                       7    6     1
30  build-30-net                         7    6     1
31  build-31-ten-virgins                14    7     7  <== +7
32  build-32-talents                    14    7     7  <== +7
33  build-33-sheep-goats                11    7     4  <== +4
34  build-34-rich-fool                  10    7     3
35  build-35-great-banquet              10    7     3
36  build-36-shrewd-steward             10    8     2
37  build-37-rich-man-lazarus           17    8     9  <== +9
38  build-38-persistent-widow            9    7     2
39  build-39-the-pharisee-and-the-publican    13   12     1
40  build-40-the-friend-at-midnight     20   16     4  <== +4
41  build-41-counting-the-cost          13   16    -3  (ok)
42  build-42-barren-fig-tree            12   12     0  (ok)
43  build-43-the-wedding-garment        14   14     0  (ok)
44  build-44-two-debtors                12    8     4  <== +4
45  build-45-wicked-tenants             15   13     2
46  build-46-seed-growing                9   11    -2  (ok)
47  build-47-houses-on-rock-and-sand    12   12     0  (ok)
48  build-48-new-wine-old-bottles        8   10    -2  (ok)
49  build-49-water-to-wine              13   12     1
50  build-50-noblemans-son              12   11     1
51  build-51-first-catch-of-fish        10    9     1
52  build-52-demoniac-synagogue          8    9    -1  (ok)
53  build-53-peters-mother-in-law       10    8     2
54  build-54-the-leper                  12    9     3
55  build-55-withered-hand              12    9     3
56  build-56-widow-of-nain              11    9     2
57  build-57-jairus-daughter            21    9    12  <== +12
58  build-58-feeding-5000               14    9     5  <== +5
59  build-59-feeding-4000               12    9     3
60  build-60-gerasene-demoniac          16    9     7  <== +7
61  build-61-syrophoenician-woman       11    9     2
62  build-62-ephphatha                  10    8     2
63  build-63-man-born-blind             18    9     9  <== +9
64  build-64-pool-of-bethesda           11    9     2
65  build-65-help-mine-unbelief         13    8     5  <== +5
66  build-66-malchus-ear                14    7     7  <== +7
67  build-67-the-transfiguration        11    8     3
68  build-68-multitudes-mountain        13    8     5  <== +5
69  build-69-baptism                    13    9     4  <== +4
70  build-70-temptations                16    9     7  <== +7
71  build-71-the-great-commission       10    8     2
72  build-72-calling-matthew            15   12     3
73  build-73-this-day-fulfilled          8    8     0  (ok)
74  build-74-woman-washed-his-feet      18    9     9  <== +9
75  build-75-woman-taken-in-adultery    15   10     5  <== +5
76  build-76-suffer-the-little-children    10    8     2
77  build-77-widows-mite                10    9     1
78  build-78-who-is-my-mother            9    8     1
79  build-79-the-seventy-sent           12    8     4  <== +4
80  build-80-come-unto-me                8    8     0  (ok)
81  build-81-render-unto-caesar         11    8     3
82  build-82-anointing-at-bethany       12    8     4  <== +4
83  build-83-weeping-over-jerusalem      8    7     1
84  build-84-no-room-manger             13   11     2
85  build-85-shepherds-and-angels       15    9     6  <== +6
86  build-86-the-wise-men               12    8     4  <== +4
87  build-87-boy-in-the-temple          11    8     3
88  build-88-triumphal-entry             9    9     0  (ok)
89  build-89-the-last-supper            13    9     4  <== +4
90  build-90-washing-feet               10   17    -7  (ok)
91  build-91-gethsemane                 16   12     4  <== +4
92  build-92-peters-denial              15    8     7  <== +7
93  build-93-barabbas-goes-free         13    7     6  <== +6
94  build-94-father-forgive-them        10    7     3
95  build-95-thief-on-the-cross         10    7     3
96  build-96-it-is-finished             12    8     4  <== +4
97  build-97-the-empty-tomb             15    8     7  <== +7
98  build-98-mary-her-name              14    8     6  <== +6
99  build-99-flesh-and-bone-thomas      14    9     5  <== +5
100 build-100-the-ascension             10    8     2
101 build-101-still-small-voice         17   10     7  <== +7
102 build-102-jacobs-ladder             12   10     2
103 build-103-peters-confession         10    9     1
104 build-104-boy-samuel                11   10     1
105 build-105-face-to-face              13   10     3
106 build-106-god-spake-by-prophets     10   10     0  (ok)
107 build-107-john-baptist-doubt        11   10     1
108 build-108-my-sheep-hear-my-voice    11   10     1
109 build-109-ask-seek-knock             8   10    -2  (ok)
110 build-110-lords-prayer              11   10     1
111 build-111-lilies-and-sparrows       10   10     0  (ok)
112 build-112-beatitudes                12   10     2
113 build-113-where-art-thou            12   10     2
114 build-114-abraham-sodom             16   10     6  <== +6
115 build-115-ram-in-the-thicket        17   10     7  <== +7
116 build-116-graven-on-his-palms        9   10    -1  (ok)
117 build-117-hosea-buys-her-back       12   10     2
118 build-118-jonah-god-who-relents     15   10     5  <== +5
119 build-119-fourth-man-in-fire        17   10     7  <== +7
120 build-120-job-from-whirlwind        16   10     6  <== +6
121 build-121-salt-and-light             9   10    -1  (ok)
122 build-122-mote-and-beam              9   10    -1  (ok)
123 build-123-golden-rule                9   10    -1  (ok)
124 build-124-love-your-enemies         10   10     0  (ok)
125 build-125-i-never-knew-you           7    7     0  (ok)
126 build-126-by-their-fruits            7    7     0  (ok)
127 build-127-the-strait-gate            7    7     0  (ok)
128 build-128-heart-far-from-me          7    7     0  (ok)
129 build-129-nazareth-only-a-few        8    7     1
130 build-130-what-manner-of-spirit      6    7    -1  (ok)
131 build-131-scribe-near-the-kingdom     9   10    -1  (ok)
132 build-132-forbid-him-not             9   10    -1  (ok)
135 build-135-rainbow-covenant          13   12     1
136 build-136-healed-in-two-touches      7    7     0  (ok)
137 build-137-one-as-we-are-one          6    6     0  (ok)
138 build-138-his-offspring              8    7     1
139 build-139-lamp-on-a-stand            8    7     1
140 build-140-naaman-washes             15   11     4  <== +4
141 build-141-bread-of-life              8    7     1
142 build-142-light-of-the-world         7    7     0  (ok)
143 build-143-i-am-the-door              7    7     0  (ok)
144 build-144-resurrection-and-the-life    10    8     2
145 build-145-way-truth-life             9    8     1
146 build-146-vine-and-branches          9    8     1
147 build-147-joseph-forgives           15    7     8  <== +8
148 build-148-ruth-and-the-redeemer     13    9     4  <== +4
149 build-149-hannah-is-heard           11    9     2
150 build-150-shepherd-psalm            11    8     3
151 build-151-ask-of-god                 9    8     1
152 build-152-revealeth-his-secret       9    8     1
153 build-153-restitution               10    8     2
154 build-154-everlasting-gospel         7    8    -1  (ok)
155 build-155-falling-away               7    8    -1  (ok)
156 build-156-famine-of-hearing          8    8     0  (ok)
157 build-157-marvellous-work           10    8     2
158 build-158-two-sticks                10    8     2
159 build-159-other-sheep                8    8     0  (ok)
160 build-160-stone-cut                 10    8     2
161 build-161-called-of-god              8    8     0  (ok)
162 build-162-keys-of-kingdom           10    8     2
163 build-163-apostles-prophets          9    8     1
164 build-164-unity-of-faith             8    8     0  (ok)
165 build-165-laying-on-hands           10    8     2
166 build-166-baptized-properly         10    8     2
167 build-167-chosen-ordained            7    8    -1  (ok)
168 build-168-born-water-spirit          7    8    -1  (ok)
169 build-169-fulfil-righteousness      10    8     2
170 build-170-sacrament-worthily        10    8     2
171 build-171-baptized-for-the-dead      7    8    -1  (ok)
172 build-172-gospel-preached-to-the-dead     7    7     0  (ok)
173 build-173-dead-shall-hear            6    7    -1  (ok)
174 build-174-hearts-of-the-fathers      7    7     0  (ok)
175 build-175-mountain-of-the-lords-house     7    7     0  (ok)
176 build-176-who-shall-ascend           6    9    -3  (ok)
177 build-177-make-me-a-sanctuary       10    9     1
178 build-178-in-our-image               8    8     0  (ok)
179 build-179-stephens-witness          10   12    -2  (ok)
180 build-180-before-i-formed-thee       7    8    -1  (ok)
181 build-181-morning-stars-sang        10   10     0  (ok)
182 build-182-spirit-returns-to-god      7    7     0  (ok)
183 build-183-sun-moon-and-stars         7    7     0  (ok)
184 build-184-third-heaven               7    7     0  (ok)
185 build-185-many-mansions-member       7    7     0  (ok)
186 build-186-joint-heirs                7    7     0  (ok)
187 build-187-ye-are-gods                7    7     0  (ok)
188 build-188-be-ye-therefore-perfect     7    7     0  (ok)
189 build-189-to-him-that-overcometh     7    7     0  (ok)
190 build-190-faith-without-works        8    7     1
191 build-191-windows-of-heaven          7    7     0  (ok)
192 build-192-the-fast-god-has-chosen    10    7     3
193 build-193-the-comforter              7    7     0  (ok)
194 build-194-fruit-of-the-spirit        7    7     0  (ok)
195 build-195-prove-all-things           7    7     0  (ok)
196 build-196-would-god-all-were-prophets     8    8     0  (ok)
197 build-197-sons-and-daughters-prophesy     6    6     0  (ok)
198 build-198-ensign-for-the-nations     7    5     2
199 build-199-fishers-and-hunters        7    5     2
200 build-200-gospel-to-all-the-world     8    8     0  (ok)
=== BLOCKED / NEEDS ATTENTION ===
133 build-133-many-mansions         NO PRESCRIPTION
134 build-134-other-sheep-i-have    NO PRESCRIPTION
=== SUMMARY ===
prescribed videos: 198
under-pictured (need more frames): 133
badly starved (gap >= 4): 56
total NEW pictures to generate across all 200: 496
blocked/needs-narration: [133, 134]
```
