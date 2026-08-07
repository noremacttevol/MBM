# QC / RUNNER HANDOFF — build-191-windows-of-heaven

**Row 191 · Malachi 3:10 · "prove me now... if I will not open you the windows of heaven."**
State: **AUTHORED / Ready ✅** (picture map authored, `--check` PASS, open complaint CLOSED
at $0). Fable-5 author lane, Machine A `Dev`, 2026-08-07, $0.

---

## 🅿️ COMPLAINT LEDGER — "Not real new voice" → FIXED AT $0 (must be verified on ship)

**Cameron (v2_outline.py 191):** *"Not real new voice."*

**FIXED (this author lane, $0):** all 8 segment mp3s are ElevenLabs new-voice —
ffprobe-confirmed 44100/128k, and the **s1 GOD segment reads F0 ≈ 134.5 Hz** = the
ElevenLabs "Bill"/God voice, NOT edge-tts. The delivered V1 mp4 had stream-copied a STALE
track; this build now sets **`AUDIO_FROM_V1_SEGMENTS = True`** in beats_v2.py, so
`v2_assemble` rebuilds the shipped track from those new-voice segments (not the stale
stream-copy). Verified: all 8 segments present, timeline total (card_start) = 51.518 s
matches beats.json. Same mechanism as shipped rows 69/77/177.

**RUNNER on ship:** the AUDIO REBUILD must PASS from the segment mp3s, and the review card
MUST tell Cameron, in plain words, that **this cut now carries the real new ElevenLabs
voice** (narrator + the God voice on the Malachi 3:10 declaration) — so he can verify in
one listen.

---

## ✅ AUTHOR DONE — 14-beat V2 map, `--check` PASS, windows contiguous 0.000→51.518 (=card)

Fresh movie-coverage beat map (NEEDS-BEATS → AUTHORED). 14 pictures over 51.518 s ≈
3.68 s/pic. Two places: **STOREHOUSE** (the place set apart for the Lord's house — people
bring their tithes, Malachi declares) and **HARVEST-LAND** (open fields where the windows
of heaven pour blessing). Human spine: a representative **FARMER** who holds back → brings
everything in → gathers the overflow; **MALACHI** carries the LORD's words.

Beat spine: b01 storehouse at dawn, people holding back (STOREHOUSE promote) · b02 "watch
what I do" · b03 place set apart (Levite receives) · b04 the tithe measured out · b05
**s1 GOD/GREEN** "bring all the tithes" (Malachi declares) · b06 "meat in mine house"
(store fills) · b07 "prove me now" · b08 **windows of heaven** open (HARVEST-LAND promote,
radiant sky, NO figure) · b09 "pour out a blessing... not room enough" · b10 "a dare no
king could make" (people wonder) · b11 "prove me" (Malachi's unique invitation) · b12 "put
me to the test" (farmer brings his full tithe) · b13 "not a trickle" (contrast insert) ·
b14 closing overflow, more than room to hold.

**SPEAKER LAW (OT prophet — LORD speaks through Malachi):** s1 (3:10) = GOD-voice → **GREEN**
caption; all else narrator → white. **NO red-letter, NO Jesus — every beat jesus=False and
NO ONE wears cream or white.**

**HARD GATE — GOD/THE LORD NEVER EMBODIED.** s1 is green but the LORD is NEVER shown: the
words are carried by Malachi + the sky + the harvest. The "windows of heaven" (b08) are a
radiant sky breaking open with light and rain — **NO figure, face, hand or beam-shaped-
like-a-person in the clouds**, no ring/halo around anyone. Drift-word gate clean.

**CONTENT-CARE:** "prove me / put me to the test" is an OFFER of goodness, not a threat —
no fear, no judgment/fire, no flood-as-disaster; the pouring blessing is abundant rain,
full storehouses and overflowing baskets (joy and plenty). The cream WARNs on
b02/b07/b09/b10/b11/b12/b14 are benign (each says "(not cream)"; kept intentionally).

---

## 🅿️ RUNNER — build the 14 stills (0 exist today)

**NEW places — promote each from its first NON-Jesus frame (all frames here are NON-Jesus):**
| Place | Promote from | Reuse on |
|---|---|---|
| STOREHOUSE | **b01** | b02, b03, b04, b05, b06, b07, b11, b12, b14 |
| HARVEST-LAND | **b08** | b09, b10, b13 |

Gates before assembly: face/beard board on MALACHI, FARMER (holds-back→trusts = same man),
LEVITE; SCALE gate; **sacred-figure gate — b05/b06/b07/b08/b09 must keep the LORD unshown
(no figure/face/hand/beam in sky)**; realistic-only Law 14 (no cartoon/mixed); NO ONE in
cream/white; drift-word checks. Then `v2_assemble` (**AUDIO REBUILD from segments** per the
flag — must PASS), re-audit, ship with the COMPLAINT LEDGER card (voice-is-real-new).
