# LENGTH & NARRATION AUDIT — report (2026-07-24)

Every one of the 200 PRESCRIPTION.md now carries a **## Length read** and a
**## Narration read**, drawn only from each build's real narration + mp4 duration.
Governed by LENGTH-AND-NARRATION-LAW.md.

## Headline
- **Length:** KEEP **78** · TRIM **122** · EXPAND **0**. Nothing is too short;
  122 videos are too long.
- **The one cause of nearly every trim:** the narrator preaches a closing
  sermon — explains the moral / tells the viewer what to feel — that the closing
  card is supposed to deliver. Cut the tail, keep the story.
- **~35 videos have an available scripture-lift** (a line the narrator paraphrases
  that a Bible figure actually said — lift it into that voice's own KJV words).
  Most were already done in the SPEAKER-LAW rebuild; the stragglers are on older builds.

## Worst length offenders (rambling, all >200s, narrator over-explains)
- #4 nicodemus 325s · #10 the-well 313s · #45 wicked-tenants ~300s · #13 roof 295s
- #12 bartimaeus 283s · #15 centurion 267s · #118 jonah 255s · #5 bent-woman 248s
- #63 man-born-blind 241s · #120 job 235s · #11 storm 234s · #39 pharisee-publican 234s
- The whole Member-verse block 151–176 runs 130–174s against a 45–75s tier — all trim.

## Biggest narration upgrade available
- **#10 the-well** — Jesus's own conversational lines are still narrator paraphrase;
  3 liftable to red (John 4:10, 4:17–18, 4:24). #92 Peter's-denial — the servant
  girl (pink) + Peter's two denials (blue) still in paraphrase.

## Defects found in passing (for the audio/caption session, not picture work)
- **#17 lazarus** — mp4 is TRUNCATED ('moov atom not found'); must be re-rendered.
- **NOT migrated to SPEAKER-LAW** (wrong Jesus voice, Christopher not Eric): #15,
  #92, #136, #138, #139, #200.
- **#171** caption reads 'livez' (a TTS respelling wrongly written into caption text).
- **#176** n3b is an orphaned fragment.
- **#133/#134** (the two new stories) have no build.py/mp4 yet — need building.

## How to read a prescription now
Each build's PRESCRIPTION.md is the full contract: pictures (beat list), length
(keep/trim), and narration (fixes + scripture lifts + cast). One file, three dimensions.
