# Video #2 The Prodigal Son (Luke 15:11-32) — RIGHT-FIRST-TIME PRE-FLIGHT
Done ON PAPER before any credit is spent, per PRODUCTION-BIBLE.md section 4b.

## Scripture card
- MUST SHOW: younger son asks for inheritance and leaves; wastes everything; famine + pig pen hunger; comes to his senses; rehearses the servant speech on the road; the father sees him WHILE STILL FAR OFF; THE FATHER RUNS; embrace BEFORE the speech is finished; robe, ring, feast; "dead and is alive again."
- MUST NEVER SHOW: Jesus in any frame (he is the storyteller, not in the story); the father waiting with crossed arms (the Seed is the RUNNING); modern objects; text baked into images. Father's face MAY be shown (pack rule — he represents the Father, is not a depiction of Deity).
- KJV fetched (bible-api.com, not hand-typed):
  - Luke 15:20 (pairing verse): "And he arose, and came to his father. But when he was yet a great way off, his father saw him, and had compassion, and ran, and fell on his neck, and kissed him."
  - Luke 15:24 (Jesus voice line, first sentence per pack): "For this my son was dead, and is alive again; he was lost, and is found."

## Storyboard — beat / STILL or MOTION / why / narration segment
1. s00 opening, STILL (reuse shot-4 road art, slow zoom out) — bookend "why he told it" — n0
2. s01 the leaving, STILL — narrator carries backstory — n1
3. s02 the pig pen, STILL — feelings/time passing = spoken over still — n2
4. s03 the road home, STILL — rehearsed speech = narrator work — n3
5. s04 seen from far off, STILL — the held breath before the run — n4
6. s05 THE FATHER RUNS, MOTION (Veo Fast, 10 credits) — the moment the story turns; the gasp beat; music cuts to silence as it begins — n5
7. s06 the embrace, STILL held long — stillness after motion lands harder — n6
8. s07 the feast, STILL — bridge + KJV Luke 15:24 — n7 + j1
9. s08 closing question card, 13.0s, cream #F7F2E9 — read aloud — n8
Story-Fit call: 1 motion clip. The heart of this story is one physical act — the run. Everything else is narrator's territory.

## Narration script (narrator en-US-AndrewNeural / Jesus en-US-ChristopherNeural — NO Multilingual)
- n0: "When religious men complained that Jesus spent his time with sinners, he didn't argue with them. He answered with a story, about a father and his two sons."
- n1: "The younger son asked for his inheritance early — as if to say he wished his father were already dead. Then he left, and poured it all out on a life that emptied him."
- n2: "When the money was gone, a famine came. He ended up feeding pigs, so hungry he would have eaten what they ate. And there, in the mud, he came to his senses."
- n3: "So he started walking home, rehearsing a speech the whole way. Father, I am not worthy to be called your son. Make me one of your servants."
- n4: "He was still a long way off... when his father saw him."
- n5: "The father ran." (breath) "Old men in that world did not run. It was beneath their dignity. He ran anyway."
- n6: "He didn't wait for the speech. He wrapped his arms around his son before a single word was said."
- n7: "That night the father dressed him in the finest robe, put a ring on his hand, and called for a feast. Jesus ended the story with the father's own words."
- j1 (KJV, exact): "For this my son was dead, and is alive again; he was lost, and is found."
- n8 (card, read gently): "Which part of that story feels closest to something you have carried — or are carrying right now?"

### Narration pre-flight checks
- [x] Dead-air map: every scene s00–s08 has a segment; only planned silences are the ~1.5s music-cut breath before n5 and the ~2s breath before n8 — both under 2.5s.
- [x] Translation Law: narrator never echoes KJV. n7 comes BEFORE j1 (bridge in, allowed); nothing re-quotes or paraphrases 15:24 after it. n3's servant speech is the SON's words in modern phrasing, not red letter — allowed.
- [x] TTS-trap read-aloud: no clipped endings ("and he worked"-style), no odd contractions. "beneath their dignity," "inheritance," "famine" are clean words for Andrew. n4 ellipsis gives natural pause.
- [x] Voices: en-US-AndrewNeural + en-US-ChristopherNeural only.
- [x] Card: 13.0s hold AND read aloud (n8). Question matches the pack Seed question.
- [x] Music: MUSIC_END set to land full silence BEFORE n5 "The father ran." (peak per pack).

## Character locks (in EVERY prompt where they appear)
- FATHER: "an older man in his sixties with a full grey beard, wearing ONE long grey rough-woven wool robe with a darker grey mantle over his shoulders"
- SON (leaving, s01): "a young man in his early twenties with short dark hair and a short dark beard, wearing a fine cream linen tunic with a rust-red mantle and a heavy leather money pouch on his belt"
- SON (ruin, s02–s06): "the same young man, now gaunt, wearing the SAME cream linen tunic now torn, mud-stained and filthy — no mantle, no pouch, barefoot"
- SON (feast, s07): "the same young man, washed and clean, wearing a fine deep-red robe and a gold ring on his hand"

## Prompt pre-flight checks
- [x] Master Style Block byte-identical at the top of every prompt; zero added style words.
- [x] No negative-prompt lists anywhere; every constraint positive ("Exactly two people in the image", "He is the ONLY person on the road — one single figure, and only him, in every frame").
- [x] AI-tell scan: the pack's shot 5 had "tears streaking into his beard" — CUT from the motion prompt (instant-appearing liquid = the video #6 sweat tell). Joy and determination carry the face instead. Tears remain only in the s07 STILL (static image, no appearing-change risk). No object pops, no instant physical changes requested anywhere.
- [x] Wardrobe/prop locks written into all seven still prompts + the clip prompt.
- [x] MUST NEVER SHOW verified against each prompt (no Jesus figure anywhere, no crossed-arms waiting father, no modern objects).

## Shot prompts (STYLE BLOCK + the text below; stills drop "Slow, tender movement.")
- s01: "A young man in his early twenties with short dark hair and a short dark beard walks away from a prosperous stone farm estate at dawn, a heavy leather money pouch on his belt, not looking back. He wears a fine cream linen tunic with a rust-red mantle. Far behind him, small and soft-focus in the estate gateway, an older man in his sixties with a full grey beard, wearing one long grey rough-woven wool robe with a darker grey mantle over his shoulders, stands motionless watching him go. Long shadows, cold early-morning light. Exactly two people in the image: the young man in the foreground and the distant older man in the gateway."
- s02: "A gaunt young man with short dark hair and a short dark beard kneels in a muddy pig pen at dusk, light rain falling. He wears a cream linen tunic, torn, mud-stained and filthy — no mantle, barefoot. He holds an empty wooden feed trough and stares down at his own empty open hands. Two pigs root in the mud behind him. He is the only person in the image."
- s03: "A gaunt young man with short dark hair and a short dark beard walks a long empty dirt road through barren hills, seen from the front, eyes down, lips parted as he rehearses words to himself, shame on his face. He wears the same cream linen tunic, torn, mud-stained and filthy, barefoot. The road stretches far behind him. Overcast light warming to gold near the horizon. He is the only person in the image, and the road is otherwise completely empty."
- s04: "Wide shot from a flat clay rooftop at golden hour: in the near foreground an older man in his sixties with a full grey beard, wearing one long grey rough-woven wool robe with a darker grey mantle over his shoulders, stands suddenly rigid, one hand shielding his eyes, staring down a long dirt road. At the far end of the road, tiny in the distance, one single ragged figure walks toward the house. Wind moves the old man's grey robe. Exactly two people in the image: the older man close on the rooftop and the tiny distant figure on the road."
- s05 MOTION (Veo 3.1 Fast, 8s, 9:16): "An older man in his sixties with a full grey beard runs down a long dirt road at golden hour, in slow motion. He wears one long grey rough-woven wool robe with a darker grey mantle over his shoulders, and he holds the hem of his robe hiked up in one fist as he runs. His sandaled feet kick up dust that glows gold in the low backlight. His arms begin to open wide as he runs, his face full of joy and determination. The camera tracks alongside him, low and fast. He is the ONLY person on the road — one single figure, and only him, in every frame of this video — and the road ahead of him and behind him is completely empty."
- s06: "On a dirt road at golden hour, an older man in his sixties with a full grey beard, wearing one long grey rough-woven wool robe with a darker grey mantle over his shoulders, wraps a gaunt young man completely in his arms. The young man wears a cream linen tunic, torn, mud-stained and filthy. The father's hand grips the back of his son's head; the son's face is pressed against his father's shoulder, eyes shut. Golden dust hangs in the air around them. Exactly two people in the image."
- s07: "Night, warm firelight in a stone courtyard during a feast. A young man with short dark hair and a short dark beard, washed and clean, wearing a fine deep-red robe with a gold ring on his hand, sits with tears shining in his eyes, stunned and overwhelmed with quiet joy. Beside him stands an older man in his sixties with a full grey beard, wearing one long grey rough-woven wool robe with a darker grey mantle over his shoulders, one hand resting on his son's shoulder. Household guests celebrate softly around them under hanging oil lanterns, with food on low tables."

## Assembly pre-flight
- [x] All offsets computed from MEASURED mp3 durations after the ear-check, never estimates.
- [x] On-paper silence map above; verify with silencedetect after mix.
- [x] MUSIC_END = just before n5's measured start. Export 1080x1920 H.264, CRF 23, maxrate 1500k, <25MB. Runtime target ~95–100s.

## Self-Revision loop findings (each one = a check that was missing above)
- 2026-07-08: silencedetect caught a 3.46s gap before n8 — j1's mp3 carries a
  ~1.2s silent tail INSIDE the file, so the planned 2s breath measured from the
  FILE end was really 3.5s from the SPOKEN end. Fixed (n8 93.0 → 92.0; gap now
  2.46s). New check added to Bible §4b: measure mp3 internal tails; compute
  breaths from spoken end, not file end. Nothing else found: ear-check 1.00 on
  all 11 segments first try; frame-strip and caption crops clean; final
  1080x1920 H.264, 104.2s, 17.2MB. Runtime landed 104.2s vs the ~95–100s
  estimate — the 13.0s card hold plus 92s of measured speech makes ~104s the
  honest floor; the target line above was an estimate, not a law.
