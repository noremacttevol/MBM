# COMPLAINT FIX PLAN — every complaint Cameron has filed, triaged (2026-08-05)

Pulled LIVE from Firestore (`node admin/dump-approvals.mjs`), not from memory.
**160 rows on the board · 44 approved · 81 carrying a complaint.**

Re-pull the live list any time:
```
cd admin && node dump-approvals.mjs
```

---

## THE FINDING THAT DECIDES THE ORDER OF WORK

**The realistic-V2 picture rebuild can NEVER fix an audio complaint.** V2
deliberately copies the V1 audio packet-for-packet (`AUDIO LOCK`) — that is the
whole point of it. So every "wrong voice" and every mispronunciation survives
the entire 200-row picture rebuild untouched.

That is **34 of the 81 complaints** (VOICE 14 + PRON 20). They need their own
sweep. Doing the picture wave first and the audio never would mean Cameron
re-files every one of them on the new cuts.

---

## THE SEVEN CLASSES

| Class | Rows | Count | Fixed by |
|---|---|---|---|
| **VOICE** (old/wrong voice) | 5, 20, 21, 27, 28, 92, 99, 127, 177, 185, 191, 198, 199, 200 | 14 | Re-voice (ElevenLabs) + re-assemble |
| **PRON** (mispronounced) | 7, 10, 18, 19, 22, 25, 46, 50, 51, 57, 67, 70, 73, 109, 110, 119, 146, 173, 188, 189 | 20 | Dict fix → re-voice affected segments |
| **CAPTION** | 4, 12, 32, 52, 56, 65, 71, 83, 107, 112, 140, 149, 150, 161, 179, 184 | 16 | Re-render captions (no re-voice) |
| **PICTURE** | 1, 2, 3, 9, 11, 13, 14, 15, 16, 17, 33, 39, 40, 62, 69, 91, 102, 103, 113, 135, 153, 157, 171, 181 | 24 | The realistic-V2 wave |
| **STORY** | 6, 8 | 2 | Author re-cut — needs Cameron's call |
| **PLAYBACK** | 31, 86 | 2 | Re-encode / trim trailing dead air |
| **OTHER** | 63, 90, 108 | 3 | mixed |

---

## 1. PRONUNCIATION — ROOT CAUSE FOUND AND FIXED (commit `4db128f3c`)

Cameron's repeats were **one bug**. `SAY_BY_VOICE` held each respelling against
a SINGLE voice; the other four voices got nothing, so the same word came back
wrong on the next row and he filed it again:

| Word | Was fixed for | Broken for | His complaint |
|---|---|---|---|
| Esaias | scripture only | narrator | 73 "pronounced Esaias as essy-y-es… this is rediculous" |
| putteth | jesus only | all others | 46 "its still wrong… put-uth" |
| Cana | narrator only | all others | 50 "still pronouncing Cana wrong" |
| maketh | jesus had `mayketh` (**wrong**), scripture `maykith` | narrator (plain, measured OK) | 188 "MAY-kith 0:29" |

**Fixed:** `SPREAD_TO_ALL_VOICES` spreads a proven respelling to every voice
that has no measured entry of its own; `maketh` for Jesus corrected to
`maykith`. Deliberately NOT blanket — words left plain on a voice because plain
WON its A/B (narrator "maketh") stay plain, or we trade one complaint for another.

### STILL MISSING from the dict — Cameron gave exact phonetics, nobody added them

These have **no entry at all**. Each needs an A/B (render both ways, transcribe,
keep the winner) before it goes in — that law exists because 50 of the old 65
respellings lost to the plain word. **`faster-whisper` is NOT installed on this
machine; install it before the sweep or the A/B cannot be run.**

| Row | Word | Cameron's phonetic |
|---|---|---|
| 57 | lieth | lie-eth |
| 70 | proceedeth | pro-see-duhth |
| 109 | findeth | fynd-uhth |
| 189 | overcometh | OH-vur-kuh-muhth |
| 108 | calleth | "same problem again" |
| 67 | Elias | ee-LY-us — **and spell it "Elias" for every speaker incl. narrator; "Elijah" is a different name** |
| 22 | shouldest | should-est |
| 63 | Siloam | si-LOH-uhm (dict has `sy-LOH-am` — he says still wrong) |
| 146 | abideth | dict has `abiedeth` — he says still wrong |
| 50 | Cana | dict has `kaynuh` — he says still wrong |

**HOMOGRAPHS — never put these in the global dict** (a global map breaks the
other reading). They need a per-segment `SPOKEN` override in that build:

| Row | Word | Meaning he wants |
|---|---|---|
| 25, 51 | tear | "tare" — to rend, NOT a crying tear |
| 110 | lead | /liːd/ "leed" — the verb, not the metal |
| 119 | bow | which reading he means is unstated — ask or infer from the verse |
| 173 | live | at the end of the video |

Also row 70: the narrator **spells out "I-S"** instead of saying the word.

### Blast radius — 30 shipped builds have audio older than the current dict

`python3 media-production/gate_rebuilds.py` (run 2026-08-05):

```
16 17 22 33 42 46 100 107 109 110 119 120 122 124 131 133 135 137 140
146 148 149 150 151 166 170 171 173 188 189
```

Ten more report `IMPORT-ERROR No module named 'edge_tts'` — those builds cannot
even be checked until that dependency is installed. Fix that first or the gate
is lying about coverage.

**Sweep procedure per build:** re-voice ONLY the stale segments the gate names →
whisper-verify the exact word → re-assemble → verify the rendered mp4 → ship →
**`firebase deploy --only hosting`** → confirm live.

---

## 2. VOICE — 14 rows still carrying the old voice

Rows 5, 20, 21, 27, 28, 92, 99, 127, 177, 185, 191, 198, 199, 200.

Row 200: *"Still the wrong audio. Im pissed"* — this one has been re-filed more
than once. Root-cause it the same way: find out WHY a re-voice did not stick
(marker file left in place? build skipped? deployed but not re-rendered?) before
re-voicing, or it will come back a fourth time.

Under REDO-ALL these must carry the new voice AND be re-approved. Note rows 199
and 21/20/28 show `approved: true` **with** a complaint — the approval is stale
and void; do not treat those as done.

---

## 3. CAPTIONS — mechanical, no re-voice needed

- **Tofu squares on the end card** (rows 50, 52): *"squares at the end of every
  line in the question end page again — if this is a problem with any more fix
  them all now."* That is a standing order to sweep ALL 200, not just those two.
  Cause is a glyph missing from the card font. The three V2 cuts shipped this
  session render clean, so the V2 card path is already good — the defect is in
  the older V1 renders.
- **Colour law** (184 "only Jesus's words in red", 150 "captions in white that
  are scripture"): Jesus red, scripture blue, narrator white. Verified correct
  on the V2 path.
- Off-timing captions: 4, 12, 65, 149.

---

## 4. PICTURES — this is what the realistic-V2 wave is for

24 rows. Several are already-known classes the V2 authoring pass now guards
against: beard/identity drift (2, 9, 62, 91, 102, 103), everyone-identical
crowds (90, 107), giant figures (69, 107, 112, 157), different-boat-every-frame
place drift (11), phantom people, wrong-direction travel (83), exact counts
(135), corpse-grey sick people (15), modern objects (7, 17, 40).

**Rows 17 and 40 are DONE and live** (this session). The rest come with the wave.

---

## 5. STORY — needs Cameron, not a machine

- **Row 6**: *"Your shortening of the videos has gotten out of hand. In this one
  the father didnt really ask either son anything and thats not how Jesus taught it."*
- **Row 8**: *"You cut the original video short? What the fuck is this."*
- **Row 140**: *"Did we just run out of stories that were good about Jesus… now
  you are using somebody else's gospel to redo the same one."*
- **Row 179**: he dictated the doctrinal fix himself — the Acts 7:55-56 vision
  must show **two distinct glorified beings**, Father and Son. That is a
  doctrine call he already made; just execute it.

These are editorial. Do not "fix" them by regenerating pictures.

---

## ORDER OF WORK (recommended)

1. **Unblock tooling**: install `faster-whisper` + `edge_tts` (10 builds are
   currently un-checkable, and no A/B can run without whisper).
2. **Row 200 first** — he is angriest, and it is a repeat. Root-cause why the
   re-voice did not stick.
3. **Pronunciation sweep** over the 30 stale builds, A/B each new respelling.
4. **Caption/tofu sweep** across all 200 (he ordered "fix them all now").
5. **Picture complaints** ride the V2 wave already in progress.
6. **Take rows 6, 8, 140 to Cameron** as questions, not guesses.

Every one of these ends with `firebase deploy --only hosting` and a live check.
A push is not a delivery.
