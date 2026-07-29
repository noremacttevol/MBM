# CRITIQUE LAW — every fix Cameron has ever asked for, enforced on ALL 200 videos

This is the master standard. A video is NOT done until it passes EVERY law below,
checked against the ACTUAL shipped mp4 (ffprobe + faster-whisper + eyes), never a
marker or timestamp. When Cameron gives a NEW critique, it is added here as a
permanent law and applied to EVERY remaining video — not just the one he flagged.
The redo loop (`admin/redo_loop.sh`) rebuilds each video to this whole standard,
one at a time, and only ships what passes.

## VOICE
- **L1. Jesus voice = Alexander** (id `UMnEnzK9QLLdRwnUyxMW`), Cameron's pick 2026-07-24:
  warm, grounded, a man not a boy, sounds like he loves the people he speaks to. Locked
  in `mbm_eleven.py` VOICE_ELEVEN[JESUS]. Do not change without Cameron.
- **L2. Pacing honors punctuation — and Jesus PAUSES like Jesus would.** All voices are
  slowed (`speed` 0.86–0.92, higher stability) so none rush. Jesus's lines get deliberate
  reverent pauses via `jesus_pauses()` in mbm_eleven.py — a longer breath after each
  sentence, a gentle breath after each comma/colon (ElevenLabs `<break>` tags in ms, so
  caption timing stays clean). Let each thought land.
- **L3. New voice only, in the actual mp4.** Every referenced clip 44100 Hz ElevenLabs
  AND the mp4 rebuilt from those clips (render-fresh). No old edge-tts anywhere.

## PRONUNCIATION (archaic words / homographs — fix at the source, verify by whisper)
- **L4.** These must be pronounced correctly (KJV archaic verb endings): calleth,
  lieth, findeth, liveth, maketh, overcometh, abideth, divideth, leadeth, proceedeth,
  putteth (put-uth), lieth (lie-eth wrong). Never spell out "I-S" — say the word.
- **L5. Names:** Esaias (not "essy-y-es"), Elias = "ee-LY-us" and spelled *Elias*
  (NOT Elijah — different prophet), Siloam = "si-LOH-uhm", Nicodemus correct.
- **L6. Homographs decided by meaning:** tear (break = "tare", not cry), lead (verb
  = /liːd/), wound, row (of vines = "roh"), bow, live (adj "/lɪv/" vs verb). Set via
  per-build SPOKEN override in the build; spot-listen (whisper can't tell homographs).

## SCRIPT / STORY
- **L7. Do not over-shorten.** Keep the full story. Some were cut to stubs (e.g. #10
  was ~5 min, became ~68s). Restore fuller narration from `TRANSCRIPTS/*.json`.
- **L8. No narrator echo.** Never restate a scripture/character line right after it in
  modern English unless the old English is genuinely hard to follow (`echo_scan.py`=0).
- **L9. Milk-level & scripturally accurate.** Christ-centered, simple, uplifting, LDS
  perspective, no heavy doctrine, nothing off-script or doctrinally wrong. No duplicate
  stories told twice.

## CAPTIONS
- **L10. Speaker colors:** Jesus's words RED (only Jesus), scripture LIGHT BLUE,
  narrator white, God green, women pink. Scripture is never left white.
- **L11. Clean captions:** no tofu squares/boxes at line ends (strip U+2028/2029/etc.),
  no wrong/old-version captions flashing, nothing out of frame — wrap to fit, 2–3 lines.
- **L12. Captions match the audio timing** (built from the real ElevenLabs timestamps).

## TIMING / PICTURES
- **L13. No dead air at the end.** Trim so the video ends shortly after the last word
  (card hold ≤ ~5s); no 13-extra-seconds tails.
- **L14. Pictures use the locked character reference** (`CHARACTERS/<name>/`) so each
  figure's face, clothes, hair, and SIZE stay consistent across every frame and every
  video. No giant Jesus, no vanishing beards, no shirtless figures, no wrong-count
  crowds, no walking-the-wrong-way. (Pictures are the OTHER machine's lane via Flow.)

## HOW A VIDEO IS "DONE"
Passes `admin/qc_gate.py` (new voice + render-fresh + complete + no echo) AND a human/
whisper pass confirms L1–L13 on the real mp4. Then it goes to Cameron's board; it only
clears his complaint list when HE approves it.

---
### NEW CRITIQUES LOG (append every new thing Cameron says here, as a numbered law)
- 2026-07-24: Jesus voice too fast / demeaning / ignores commas → recast (L1–L2).
