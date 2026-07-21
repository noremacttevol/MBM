# STORY-COVERAGE SWEEP — 2026-07-20 (automated audit)

Heuristic scan of every build.py + make_narration.py for the two defects in
STORY-COVERAGE-LAW.md: (1) one still spanning a long run of beats, and
(2) long multi-sentence segments telling several visual moments over one still.
Score = 2x(worst same-still run) + sentences in flagged long segments. The score
ranks SUSPICION — each build still needs a human-eye beat read before retrofit.
Rows in approvals.json are listed but LOCKED (hands off until Cameron denies).

DONE: build-18-emmaus and build-19-shore retrofitted and on the board 2026-07-20.

| score | row | build | worst same-still run | long segments |
|---|---|---|---|---|
| 57 | 10 | build-10-well | 5x S4 | n0(8sent), n1(6sent), n2(8sent), n5(12sent), n6(4sent), n7(3sent), n9(6sent) |
| 53 | 13 | build-13-roof | 3x S6 | n0(6sent), n1(5sent), n2(4sent), n3(3sent), n4(7sent), n6(8sent), n7(6sent), n9(4sent), n11(4sent) |
| 53 | 12 **APPROVED — HANDS OFF** | build-12-bartimaeus | 2x S3 | n0(6sent), n1(7sent), n2(7sent), n3(4sent), n5(6sent), n7(6sent), n9(5sent), n10(4sent), n11(4sent) |
| 51 | 60 | build-60-gerasene-demoniac | 4x S5 | n0(6sent), n1(8sent), n2b(5sent), n6b(5sent), n7(8sent), n8(5sent), n9(6sent) |
| 50 | 4 | build-04-nicodemus | 3x S3 | n0(7sent), n2b(7sent), n3b(7sent), n4b(5sent), n8(5sent), n10b(6sent), n11(7sent) |
| 48 | 91 | build-91-gethsemane | 2x S4 | n1(4sent), n2(3sent), n3(3sent), n4(3sent), n6(4sent), n7(4sent), n8(5sent), n9(4sent), n10(4sent), n11(4sent), n12(6sent) |
| 48 | 7 | build-07-peter-water | 4x S4 | n0(7sent), n1(6sent), n2(6sent), n3(7sent), n7(6sent), n8(8sent) |
| 47 | 64 | build-64-pool-of-bethesda | 3x S4 | n0(6sent), n1(6sent), n3(5sent), n4(10sent), n5b(8sent), n6b(6sent) |
| 42 | 45 | build-45-wicked-tenants | 2x S1 | n1(3sent), n2(4sent), n7(5sent), n9(4sent), n10(5sent), n11(7sent), n12(5sent), n13(5sent) |
| 41 | 44 | build-44-two-debtors | 4x S4 | n2(3sent), n3(3sent), n7(6sent), jv44(4sent), n8(4sent), n9(6sent), n10(7sent) |
| 41 | 17 | build-17-lazarus | 4x S2 | n0(5sent), n2(7sent), n3(3sent), n5(4sent), n6(8sent), n10(6sent) |
| 40 | 72 | build-72-calling-matthew | 3x S8 | n1(4sent), n2(5sent), n5(4sent), n6(7sent), n9(6sent), n10(4sent), n12(4sent) |
| 40 | 66 | build-66-malchus-ear | 3x S2 | n0(4sent), n1b(6sent), n2(5sent), n3(5sent), n4(4sent), n5(3sent), n6(4sent), n7(3sent) |
| 40 | 3 | build-03-zacchaeus | 3x S6 | n0(6sent), n1(6sent), n2(4sent), n3b(5sent), n5(7sent), n7b(6sent) |
| 39 | 62 | build-62-ephphatha | 3x S6 | n0(6sent), n1(5sent), n2(6sent), n3(7sent), n5(9sent) |
| 38 | 11 **APPROVED — HANDS OFF** | build-11-storm | 3x S5 | n0(3sent), n1(6sent), n2(6sent), n6(6sent), n8(7sent), n9b(4sent) |
| 37 | 63 | build-63-man-born-blind | 5x S9 | n0(3sent), n2(4sent), n3(3sent), n4(5sent), n6(4sent), n6b(4sent), n7(4sent) |
| 37 | 61 | build-61-syrophoenician-woman | 3x S4 | n0(5sent), n1(5sent), n4(7sent), n5b(5sent), n7(9sent) |
| 36 | 41 | build-41-counting-the-cost | 3x S2 | n3(7sent), n9(5sent), n10(5sent), n12(5sent), n13b(5sent), n16(3sent) |
| 36 | 18 | build-18-emmaus | 3x S3 | n0(3sent), n1(3sent), n3(5sent), n4b(3sent), n5(4sent), n8(3sent), n9(4sent), n10(5sent) |
| 34 | 120 **APPROVED — HANDS OFF** | build-120-job-from-whirlwind | 4x S8 | n2(4sent), n2b(5sent), n5b(3sent), n6b(4sent), n7b(3sent), n7(7sent) |
| 33 | 84 | build-84-no-room-manger | 2x S1 | n2(4sent), n4(4sent), n5(4sent), n7(6sent), n8(4sent), n9(3sent), n12(4sent) |
| 33 | 118 **APPROVED — HANDS OFF** | build-118-jonah-god-who-relents | 3x S1 | n3(4sent), n3b(4sent), n5(3sent), n8(6sent), n8b(6sent), n9(4sent) |
| 32 | 48 | build-48-new-wine-old-bottles | 3x S1 | n3(6sent), n4(5sent), n6(4sent), n7(7sent), n8(4sent) |
| 32 | 135 | build-135-rainbow-covenant | 3x S2 | n1(3sent), n2(4sent), n5(5sent), n6(5sent), n8(4sent), n10(5sent) |
| 32 | 124 | build-124-love-your-enemies | 2x S2 | n2(7sent), n3(7sent), n5(4sent), n7(6sent), n8(4sent) |
| 31 | 9 | build-09-rich-ruler | 4x S2 | n1(12sent), n2(5sent), n6(6sent) |
| 31 | 68 | build-68-multitudes-mountain | 3x S8 | n1(7sent), n3(7sent), n4(5sent), n5b(3sent), n7(3sent) |
| 31 | 40 | build-40-the-friend-at-midnight | 3x S2 | n4(4sent), n14b(4sent), jv11(3sent), n16a(4sent), n16b(5sent), n18(5sent) |
| 30 | 65 | build-65-help-mine-unbelief | 4x S3 | n0(6sent), n1(4sent), n3(4sent), n4(5sent), n7b(3sent) |
| 29 | 5 **APPROVED — HANDS OFF** | build-05-bent-woman | 3x S8 | n0(5sent), n1(4sent), n9(4sent), n10(10sent) |
| 29 | 117 **APPROVED — HANDS OFF** | build-117-hosea-buys-her-back | 4x S8 | n2b(4sent), n3(4sent), n6(3sent), n7b(5sent), n8(5sent) |
| 28 | 71 | build-71-calling-the-fishermen | 2x S4 | n4(5sent), n5(4sent), n9(6sent), n11(5sent), n12(4sent) |
| 28 | 39 | build-39-the-pharisee-and-the-publican | 2x S1 | n3(4sent), n4(4sent), n7(5sent), n8a(3sent), n10(4sent), n13(4sent) |
| 27 | 115 **APPROVED — HANDS OFF** | build-115-ram-in-the-thicket | 4x S6 | n2(3sent), n6(8sent), n7b(3sent), n8(5sent) |
| 26 | 42 | build-42-barren-fig-tree | 3x S2 | n2(4sent), n4(3sent), n8(4sent), n10(5sent), n11(4sent) |
| 25 | 82 | build-82-anointing-at-bethany | 5x ST7 | n2b(7sent), n4b(4sent), n6(4sent) |
| 25 | 121 | build-121-salt-and-light | 2x S2 | n2(4sent), n3(4sent), n4(3sent), n8(5sent), n9(5sent) |
| 25 | 113 | build-113-where-art-thou | 3x S7 | n5(7sent), n6(5sent), n7(3sent), n9(4sent) |
| 23 | 49 | build-49-water-to-wine | 3x S4 | n5(4sent), n9(5sent), n11(4sent), n12(4sent) |
| 22 | 69 | build-69-baptism | 3x S2 | n0(4sent), n3(5sent), n6(7sent) |
| 21 | 106 | build-106-god-spake-by-prophets | 6x S7 | nA(5sent), n7(4sent) |
| 20 | 87 | build-87-boy-in-the-temple | 3x ST6 | n2b(8sent), n2c(6sent) |
| 20 | 33 | build-33-sheep-goats | 3x S1 | n4(4sent), n5(5sent), n9(5sent) |
| 20 | 148 | build-148-ruth-and-the-redeemer | 3x ST3 | n2(6sent), n2b(5sent), n4(3sent) |
| 20 | 14 | build-14-ten-lepers | 2x S3 | n1(6sent), n4(4sent), n11(6sent) |
| 20 | 119 | build-119-fourth-man-in-fire | 3x S2 | n3(5sent), n6b(3sent), n8(3sent), n10(3sent) |
| 19 | 46 | build-46-seed-growing | 2x S2 | n3(5sent), n8(4sent), n10(6sent) |
| 19 | 43 | build-43-the-wedding-garment | 3x S3 | n10(4sent), n11(5sent), n16(4sent) |
| 18 | 56 | build-56-widow-of-nain | 3x S4 | n2(4sent), n3(5sent), n4b(3sent) |
| 18 | 52 | build-52-demoniac-synagogue | 3x S4 | n4b(7sent), n5(5sent) |
| 18 | 149 | build-149-hannah-is-heard | 4x ST1 | n2(5sent), n3b(5sent) |
| 18 | 125 | build-125-i-never-knew-you | 1x ST1 | n1(4sent), n2(6sent), n3(6sent) |
| 17 | 86 | build-86-the-wise-men | 5x S2 | n0b(4sent), n3b(3sent) |
| 17 | 85 | build-85-shepherds-and-angels | 3x ST4 | n1b(6sent), n2b(5sent) |
| 16 | 99 | build-99-flesh-and-bone-thomas | 3x ST5 | n1b(5sent), n4b(5sent) |
| 16 | 23 | build-23-vineyard | 6x S3 | j1(4sent) |
| 16 | 20 | build-20-samaritan | 5x S1 | n1b(6sent) |
| 16 | 161 | build-161-called-of-god | 3x S7 | n7(4sent), n8(6sent) |
| 16 | 123 | build-123-golden-rule | 1x S1 | n2(7sent), n7(4sent), n8(3sent) |
| 16 | 122 | build-122-mote-and-beam | 2x S3 | n2(4sent), n4(5sent), n6(3sent) |
| 15 | 79 | build-79-the-seventy-sent | 3x ST6 | n1b(4sent), n3c(5sent) |
| 15 | 150 | build-150-shepherd-psalm | 5x ST1 | n3(5sent) |
| 14 | 98 | build-98-mary-her-name | 3x ST1 | n3(5sent), n4a(3sent) |
| 14 | 58 | build-58-feeding-5000 | 3x S2 | n3b(3sent), n6(5sent) |
| 14 | 178 | build-178-in-our-image | 3x S4 | n0b(4sent), n0c(4sent) |
| 14 | 153 | build-153-restitution | 3x S1 | n1b(4sent), n8(4sent) |
| 14 | 151 | build-151-ask-of-god | 3x S7 | n1(3sent), n8(5sent) |
| 14 | 147 | build-147-joseph-forgives | 3x ST3 | n1c(4sent), n3(4sent) |
| 14 | 107 | build-107-john-baptist-doubt | 2x S4 | n4(7sent), n6(3sent) |
| 14 | 102 **APPROVED — HANDS OFF** | build-102-jacobs-ladder | 2x S5 | n5(3sent), n7(4sent), n9(3sent) |
| 13 | 59 | build-59-feeding-4000 | 4x S4 | n1b(5sent) |
| 13 | 47 | build-47-houses-on-rock-and-sand | 3x S11 | n4(4sent), n12(3sent) |
| 13 | 164 | build-164-unity-of-faith | 3x S7 | n6(3sent), n7(4sent) |
| 13 | 108 | build-108-my-sheep-hear-my-voice | 2x S3 | n4b(4sent), n6(5sent) |
| 13 | 101 **APPROVED — HANDS OFF** | build-101-still-small-voice | 3x S4 | n7(3sent), n8(4sent) |
| 12 | 36 | build-36-shrewd-steward | 4x S1 | n10(4sent) |
| 12 | 32 | build-32-talents | 4x S7 | n10(4sent) |
| 12 | 16 | build-16-mary-martha | 3x S4 | n10(3sent), n11(3sent) |
| 11 | 78 | build-78-who-is-my-mother | 3x ST3 | n3(5sent) |
| 11 | 57 | build-57-jairus-daughter | 3x S1 | n6(5sent) |
| 11 | 55 | build-55-withered-hand | 3x S3 | n4(5sent) |
| 11 | 158 **APPROVED — HANDS OFF** | build-158-two-sticks | 3x S4 | n8(5sent) |
| 11 | 157 | build-157-marvellous-work | 3x S5 | n8(5sent) |
| 11 | 105 **APPROVED — HANDS OFF** | build-105-face-to-face | 4x S5 | n7(3sent) |
| 10 | 93 | build-93-barabbas-goes-free | 5x ST4 | — |
| 10 | 50 | build-50-noblemans-son | 3x S6 | n2(4sent) |
| 10 | 35 | build-35-great-banquet | 3x S1 | n10(4sent) |
| 10 | 31 | build-31-ten-virgins | 5x S5 | — |
| 10 | 22 | build-22-unmerciful-servant | 5x S1 | — |
| 10 | 21 | build-21-lost-sheep | 5x S1 | — |
| 10 | 112 | build-112-beatitudes | 3x S1 | n6(4sent) |
| 10 | 109 | build-109-ask-seek-knock | 3x S7 | n6(4sent) |
| 10 | 100 | build-100-the-ascension | 2x ST2 | n1(6sent) |
| 9 | 77 | build-77-widows-mite | 2x ST1 | n4a(5sent) |
| 9 | 54 | build-54-the-leper | 3x S2 | n1(3sent) |
| 9 | 169 | build-169-fulfil-righteousness | 3x S3 | n7(3sent) |
| 9 | 168 | build-168-born-water-spirit | 3x S7 | n7(3sent) |
| 9 | 163 | build-163-apostles-prophets | 2x S4 | n8(5sent) |
| 9 | 154 **APPROVED — HANDS OFF** | build-154-everlasting-gospel | 2x S4 | n8(5sent) |
| 9 | 152 **APPROVED — HANDS OFF** | build-152-revealeth-his-secret | 2x S4 | n8(5sent) |
| 9 | 104 **APPROVED — HANDS OFF** | build-104-boy-samuel | 3x S6 | n8(3sent) |
| 8 | 96 | build-96-it-is-finished | 4x ST4 | — |
| 8 | 92 **APPROVED — HANDS OFF** | build-92-peters-denial | 4x ST3 | — |
| 8 | 83 | build-83-weeping-over-jerusalem | 2x S3 | n2b(4sent) |
| 8 | 80 | build-80-come-unto-me | 2x S3 | n1b(4sent) |
| 8 | 67 | build-67-the-transfiguration | 2x S5 | n2c(4sent) |
| 8 | 38 | build-38-persistent-widow | 4x S7 | — |
| 8 | 30 | build-30-net | 4x S5 | — |
| 8 | 27 | build-27-leaven | 4x S1 | — |
| 8 | 25 | build-25-wheat-and-tares | 4x S1 | — |
| 8 | 24 | build-24-sower | 4x S6 | — |
| 8 | 19 | build-19-shore | 4x S6 | — |
| 8 | 182 | build-182-spirit-returns-to-god | 2x ST1 | n0b(4sent) |
| 8 | 180 | build-180-before-i-formed-thee | 2x ST5 | n1r(4sent) |
| 8 | 167 | build-167-chosen-ordained | 2x S7 | n6(4sent) |
| 8 | 162 | build-162-keys-of-kingdom | 2x S1 | n8(4sent) |
| 8 | 160 | build-160-stone-cut | 2x S4 | n8(4sent) |
| 8 | 159 | build-159-other-sheep | 2x S4 | n8(4sent) |
| 8 | 156 **APPROVED — HANDS OFF** | build-156-famine-of-hearing | 2x S4 | n8(4sent) |
| 8 | 155 | build-155-falling-away | 2x S4 | n8(4sent) |
| 8 | 15 **APPROVED — HANDS OFF** | build-15-centurion | 4x S6 | — |
| 8 | 140 | build-140-road-runs-both-ways | 2x ST4 | n7(4sent) |
| 7 | 89 | build-89-the-last-supper | 2x S7 | n4(3sent) |
| 7 | 181 | build-181-morning-stars-sang | 2x ST4 | n1r(3sent) |
| 7 | 165 | build-165-laying-on-hands | 2x S4 | n7(3sent) |
| 7 | 145 **APPROVED — HANDS OFF** | build-145-way-truth-life | 2x S1 | jv2(3sent) |
| 7 | 138 **APPROVED — HANDS OFF** | build-138-his-offspring | 2x ST2 | n1(3sent) |
| 7 | 131 | build-131-scribe-near-the-kingdom | 2x ST1 | jv29(3sent) |
| 6 | 183 | build-183-sun-moon-and-stars | 1x ST1 | n3(4sent) |
