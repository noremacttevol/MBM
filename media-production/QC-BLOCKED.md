# QC-BLOCKED — videos held OFF the board until they pass admin/qc_gate.py

Updated 2026-07-24 (deep sweep). 192 of 200 are NOT verified. Reason tally: {'STALE RENDER': 147, 'AUDIO ECHO (what it actually says)': 3, 'NEW VOICE': 33, 'PLAYABLE': 4, 'COMPLETE': 5}.

Almost all need the ElevenLabs re-render actually run (the new voice clips exist in the
folder but the shipped mp4 was never rebuilt from them). Fix, then run
`python3 admin/qc_sweep.py --deep <num>`; it re-enters the board when it truly passes.

| # | Why |
|---|-----|
| 1 | STALE RENDER: mp4 is 127s but the current clips total only 93s — 34s of audio the new clips can't explain (budget 18s).  |
| 4 | AUDIO ECHO (what it actually says): 1 spoken repeat(s), e.g. "Does our law judge any man before it hear him and know wha |
| 5 | NEW VOICE: 20 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n0, n1, n2, n3, n4, j1, n5a, n5b |
| 6 | NEW VOICE: 12 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n0, n1, n2, n2b, n2c, n2d, n3, j1 |
| 7 | STALE RENDER: mp4 is 249s but the current clips total only 195s — 54s of audio the new clips can't explain (budget 25s). |
| 8 | STALE RENDER: mp4 is 40s but the clips total 50s — the mp4 is missing narration; rebuild it |
| 9 | NEW VOICE: 14 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n0, n0b, s17, n1, s20, n2, j1, n3 |
| 10 | NEW VOICE: 20 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n0, n1, n2, w9, w11, n3, j1, n4 |
| 11 | STALE RENDER: mp4 is 270s but the current clips total only 197s — 73s of audio the new clips can't explain (budget 23s). |
| 12 | STALE RENDER: mp4 is 313s but the current clips total only 252s — 61s of audio the new clips can't explain (budget 21s). |
| 13 | NEW VOICE: 19 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n0, n1, n2, n3, n4, n5, j1, n6 |
| 14 | NEW VOICE: 20 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n0, n1, s13, n2, n3, j1, n4, n5 |
| 15 | NEW VOICE: 27 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, n2, n3, n4, n5, n6, n7, n8 |
| 16 | NEW VOICE: 15 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, n2, n3, n4, n5, n6, n7, w40 |
| 17 | STALE RENDER: mp4 is 394s but the current clips total only 291s — 103s of audio the new clips can't explain (budget 27s) |
| 18 | NEW VOICE: 18 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n0, n1, n2, s18, n3, s21, n4a, j1 |
| 19 | STALE RENDER: mp4 is 200s but the current clips total only 133s — 67s of audio the new clips can't explain (budget 25s). |
| 20 | NEW VOICE: 23 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, s25, n1b, s29, n2, n3, n4, n5 |
| 21 | STALE RENDER: mp4 is 177s but the current clips total only 113s — 64s of audio the new clips can't explain (budget 21s). |
| 22 | STALE RENDER: mp4 is 272s but the current clips total only 196s — 76s of audio the new clips can't explain (budget 28s). |
| 23 | NEW VOICE: 23 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, n2, n3, n4, n5, j6, j7a, n5b |
| 24 | NEW VOICE: 19 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, n2, s3, j1, n3, j4, n4, n5 |
| 25 | NEW VOICE: 21 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): s24, j24, n2, j25, n3, n4, n5, j27 |
| 26 | STALE RENDER: mp4 is 104s but the current clips total only 72s — 32s of audio the new clips can't explain (budget 17s).  |
| 27 | STALE RENDER: mp4 is 124s but the current clips total only 85s — 40s of audio the new clips can't explain (budget 15s).  |
| 28 | STALE RENDER: mp4 is 118s but the current clips total only 82s — 36s of audio the new clips can't explain (budget 18s).  |
| 29 | NEW VOICE: 13 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, j1, n2, n3, n4, n5, j2, n6 |
| 30 | NEW VOICE: 16 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, j1, n2, n3, n4, j48, n5, n6 |
| 31 | NEW VOICE: 24 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n0, n1, n2, n3, n4, n5, j2, n6 |
| 32 | STALE RENDER: mp4 is 145s but the current clips total only 125s — 19s of audio the new clips can't explain (budget 18s). |
| 33 | STALE RENDER: mp4 is 210s but the current clips total only 148s — 62s of audio the new clips can't explain (budget 18s). |
| 34 | STALE RENDER: mp4 is 154s but the current clips total only 107s — 48s of audio the new clips can't explain (budget 21s). |
| 35 | STALE RENDER: mp4 is 173s but the current clips total only 112s — 62s of audio the new clips can't explain (budget 20s). |
| 36 | NEW VOICE: 18 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): s1, j0, n1, n2, j3, n3, n4, j6 |
| 37 | NEW VOICE: 20 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n0, n1, n2, n3, n4, n5, n6, j3 |
| 38 | STALE RENDER: mp4 is 216s but the current clips total only 146s — 70s of audio the new clips can't explain (budget 19s). |
| 39 | NEW VOICE: 21 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): s9, n1, jv10, n2, n3, n4, n5, j1 |
| 40 | NEW VOICE: 30 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): s1, n1, n2, j0, n3, n4, n5, n6 |
| 41 | NEW VOICE: 27 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, s25, n2, j1, n3, n4, j2, n5 |
| 42 | NEW VOICE: 19 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, s6a, jv6, n2, n3, n4, jv7, n5 |
| 43 | NEW VOICE: 27 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): s1, n1, jv2, n2, jv3, n3, jv4, n4 |
| 44 | STALE RENDER: mp4 is 317s but the current clips total only 224s — 92s of audio the new clips can't explain (budget 26s). |
| 45 | NEW VOICE: 24 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): s1, n1, jv1, n2, n3, jv2, n4, jv3 |
| 46 | NEW VOICE: 16 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, jv26, n2, jv27, n3, n4, n5, jv28 |
| 47 | NEW VOICE: 19 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, n2, n3, n4, jv24, n5, jv25, n6 |
| 48 | NEW VOICE: 16 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, s18, n1b, n2, jv19, n3, jv20, n4 |
| 49 | NEW VOICE: 22 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, n2, n3, n4, w3, n4b, jv4, n5 |
| 50 | NEW VOICE: 20 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, n2, n3, n4, jv48, n5, n6, s49 |
| 51 | NEW VOICE: 15 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n1, n2, jv4, n3, s5, n3b, n4, n5 |
| 52 | STALE RENDER: mp4 is 195s but the current clips total only 138s — 57s of audio the new clips can't explain (budget 18s). |
| 53 | STALE RENDER: mp4 is 126s but the current clips total only 92s — 34s of audio the new clips can't explain (budget 14s).  |
| 54 | STALE RENDER: mp4 is 187s but the current clips total only 132s — 55s of audio the new clips can't explain (budget 18s). |
| 55 | STALE RENDER: mp4 is 189s but the current clips total only 134s — 55s of audio the new clips can't explain (budget 18s). |
| 56 | STALE RENDER: mp4 is 175s but the current clips total only 134s — 41s of audio the new clips can't explain (budget 19s). |
| 57 | STALE RENDER: mp4 is 212s but the current clips total only 147s — 65s of audio the new clips can't explain (budget 22s). |
| 58 | STALE RENDER: mp4 is 186s but the current clips total only 139s — 47s of audio the new clips can't explain (budget 21s). |
| 59 | STALE RENDER: mp4 is 200s but the current clips total only 149s — 51s of audio the new clips can't explain (budget 20s). |
| 60 | STALE RENDER: mp4 is 271s but the current clips total only 211s — 60s of audio the new clips can't explain (budget 22s). |
| 61 | STALE RENDER: mp4 is 208s but the current clips total only 168s — 40s of audio the new clips can't explain (budget 18s). |
| 63 | STALE RENDER: mp4 is 270s but the current clips total only 223s — 48s of audio the new clips can't explain (budget 26s). |
| 64 | STALE RENDER: mp4 is 273s but the current clips total only 213s — 60s of audio the new clips can't explain (budget 20s). |
| 65 | PLAYABLE: no finished scripture-named mp4 in the build folder |
| 66 | STALE RENDER: mp4 is 207s but the current clips total only 160s — 47s of audio the new clips can't explain (budget 17s). |
| 67 | PLAYABLE: no finished scripture-named mp4 in the build folder |
| 68 | AUDIO ECHO (what it actually says): 1 spoken repeat(s), e.g. "And great multitudes came unto him, having with them those |
| 69 | STALE RENDER: mp4 is 200s but the current clips total only 154s — 46s of audio the new clips can't explain (budget 18s). |
| 70 | STALE RENDER: mp4 is 283s but the current clips total only 213s — 70s of audio the new clips can't explain (budget 23s). |
| 71 | PLAYABLE: no finished scripture-named mp4 in the build folder |
| 72 | STALE RENDER: mp4 is 272s but the current clips total only 214s — 58s of audio the new clips can't explain (budget 21s). |
| 73 | STALE RENDER: mp4 is 125s but the current clips total only 91s — 34s of audio the new clips can't explain (budget 14s).  |
| 74 | STALE RENDER: mp4 is 208s but the current clips total only 150s — 58s of audio the new clips can't explain (budget 22s). |
| 75 | STALE RENDER: mp4 is 149s but the current clips total only 105s — 44s of audio the new clips can't explain (budget 18s). |
| 76 | STALE RENDER: mp4 is 100s but the current clips total only 67s — 32s of audio the new clips can't explain (budget 16s).  |
| 77 | STALE RENDER: mp4 is 110s but the current clips total only 83s — 27s of audio the new clips can't explain (budget 16s).  |
| 78 | STALE RENDER: mp4 is 91s but the current clips total only 67s — 24s of audio the new clips can't explain (budget 15s). I |
| 79 | STALE RENDER: mp4 is 140s but the current clips total only 99s — 42s of audio the new clips can't explain (budget 17s).  |
| 80 | STALE RENDER: mp4 is 100s but the current clips total only 73s — 26s of audio the new clips can't explain (budget 15s).  |
| 81 | STALE RENDER: mp4 is 114s but the current clips total only 77s — 37s of audio the new clips can't explain (budget 18s).  |
| 82 | STALE RENDER: mp4 is 176s but the current clips total only 138s — 38s of audio the new clips can't explain (budget 22s). |
| 83 | STALE RENDER: mp4 is 98s but the current clips total only 63s — 35s of audio the new clips can't explain (budget 14s). I |
| 84 | STALE RENDER: mp4 is 264s but the current clips total only 219s — 45s of audio the new clips can't explain (budget 18s). |
| 85 | STALE RENDER: mp4 is 184s but the current clips total only 135s — 49s of audio the new clips can't explain (budget 19s). |
| 86 | NEW VOICE: 14 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n0, j1, n0b, n1, s8, n1b, n2a, n2b |
| 88 | STALE RENDER: mp4 is 144s but the current clips total only 105s — 39s of audio the new clips can't explain (budget 18s). |
| 89 | STALE RENDER: mp4 is 134s but the current clips total only 71s — 63s of audio the new clips can't explain (budget 18s).  |
| 90 | STALE RENDER: mp4 is 92s but the current clips total only 69s — 23s of audio the new clips can't explain (budget 17s). I |
| 91 | STALE RENDER: mp4 is 284s but the current clips total only 216s — 67s of audio the new clips can't explain (budget 20s). |
| 92 | STALE RENDER: mp4 is 70s but the current clips total only 48s — 22s of audio the new clips can't explain (budget 13s). I |
| 93 | STALE RENDER: mp4 is 109s but the current clips total only 77s — 32s of audio the new clips can't explain (budget 18s).  |
| 94 | STALE RENDER: mp4 is 87s but the current clips total only 62s — 25s of audio the new clips can't explain (budget 15s). I |
| 95 | STALE RENDER: mp4 is 81s but the current clips total only 52s — 29s of audio the new clips can't explain (budget 15s). I |
| 96 | STALE RENDER: mp4 is 97s but the current clips total only 70s — 27s of audio the new clips can't explain (budget 18s). I |
| 97 | STALE RENDER: mp4 is 106s but the current clips total only 63s — 43s of audio the new clips can't explain (budget 17s).  |
| 98 | STALE RENDER: mp4 is 147s but the current clips total only 104s — 43s of audio the new clips can't explain (budget 20s). |
| 99 | STALE RENDER: mp4 is 79s but the clips total 129s — the mp4 is missing narration; rebuild it |
| 100 | COMPLETE: 1 segment(s) have no audio clip: n4 |
| 101 | STALE RENDER: mp4 is 211s but the current clips total only 157s — 54s of audio the new clips can't explain (budget 19s). |
| 102 | STALE RENDER: mp4 is 207s but the current clips total only 162s — 46s of audio the new clips can't explain (budget 18s). |
| 103 | STALE RENDER: mp4 is 155s but the current clips total only 107s — 47s of audio the new clips can't explain (budget 18s). |
| 104 | STALE RENDER: mp4 is 179s but the current clips total only 128s — 51s of audio the new clips can't explain (budget 18s). |
| 105 | STALE RENDER: mp4 is 198s but the current clips total only 149s — 49s of audio the new clips can't explain (budget 21s). |
| 106 | STALE RENDER: mp4 is 170s but the current clips total only 129s — 40s of audio the new clips can't explain (budget 19s). |
| 107 | STALE RENDER: mp4 is 175s but the current clips total only 136s — 39s of audio the new clips can't explain (budget 17s). |
| 108 | STALE RENDER: mp4 is 175s but the current clips total only 135s — 40s of audio the new clips can't explain (budget 18s). |
| 109 | STALE RENDER: mp4 is 161s but the current clips total only 120s — 41s of audio the new clips can't explain (budget 17s). |
| 110 | STALE RENDER: mp4 is 162s but the current clips total only 122s — 39s of audio the new clips can't explain (budget 18s). |
| 111 | STALE RENDER: mp4 is 194s but the current clips total only 141s — 53s of audio the new clips can't explain (budget 18s). |
| 112 | STALE RENDER: mp4 is 193s but the current clips total only 141s — 52s of audio the new clips can't explain (budget 17s). |
| 113 | STALE RENDER: mp4 is 193s but the current clips total only 150s — 43s of audio the new clips can't explain (budget 18s). |
| 114 | STALE RENDER: mp4 is 170s but the current clips total only 131s — 38s of audio the new clips can't explain (budget 18s). |
| 115 | STALE RENDER: mp4 is 228s but the current clips total only 176s — 52s of audio the new clips can't explain (budget 20s). |
| 116 | STALE RENDER: mp4 is 156s but the current clips total only 123s — 33s of audio the new clips can't explain (budget 16s). |
| 117 | STALE RENDER: mp4 is 254s but the current clips total only 217s — 38s of audio the new clips can't explain (budget 21s). |
| 118 | STALE RENDER: mp4 is 334s but the current clips total only 259s — 75s of audio the new clips can't explain (budget 25s). |
| 119 | STALE RENDER: mp4 is 266s but the current clips total only 197s — 70s of audio the new clips can't explain (budget 21s). |
| 120 | STALE RENDER: mp4 is 308s but the current clips total only 239s — 69s of audio the new clips can't explain (budget 25s). |
| 122 | STALE RENDER: mp4 is 189s but the current clips total only 152s — 37s of audio the new clips can't explain (budget 17s). |
| 123 | STALE RENDER: mp4 is 172s but the current clips total only 134s — 38s of audio the new clips can't explain (budget 15s). |
| 124 | STALE RENDER: mp4 is 214s but the current clips total only 160s — 54s of audio the new clips can't explain (budget 17s). |
| 125 | STALE RENDER: mp4 is 112s but the current clips total only 81s — 31s of audio the new clips can't explain (budget 12s).  |
| 126 | STALE RENDER: mp4 is 123s but the current clips total only 92s — 31s of audio the new clips can't explain (budget 15s).  |
| 127 | STALE RENDER: mp4 is 79s but the current clips total only 56s — 23s of audio the new clips can't explain (budget 13s). I |
| 128 | PLAYABLE: no finished scripture-named mp4 in the build folder |
| 129 | STALE RENDER: mp4 is 104s but the current clips total only 71s — 32s of audio the new clips can't explain (budget 15s).  |
| 130 | STALE RENDER: mp4 is 80s but the current clips total only 53s — 27s of audio the new clips can't explain (budget 13s). I |
| 131 | STALE RENDER: mp4 is 115s but the current clips total only 79s — 36s of audio the new clips can't explain (budget 14s).  |
| 132 | STALE RENDER: mp4 is 101s but the current clips total only 70s — 31s of audio the new clips can't explain (budget 15s).  |
| 133 | STALE RENDER: mp4 is 104s but the current clips total only 71s — 33s of audio the new clips can't explain (budget 15s).  |
| 134 | COMPLETE: 1 segment(s) have no audio clip: n1b |
| 135 | STALE RENDER: mp4 is 306s but the current clips total only 247s — 59s of audio the new clips can't explain (budget 22s). |
| 136 | STALE RENDER: mp4 is 62s but the current clips total only 40s — 23s of audio the new clips can't explain (budget 12s). I |
| 137 | NEW VOICE: 8 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n0a, n0b, n1, s1, n2, n2b, n3, card |
| 138 | STALE RENDER: mp4 is 70s but the current clips total only 45s — 26s of audio the new clips can't explain (budget 12s). I |
| 139 | STALE RENDER: mp4 is 66s but the current clips total only 44s — 21s of audio the new clips can't explain (budget 12s). I |
| 140 | NEW VOICE: 15 clip(s) are the OLD voice (not 44100 Hz ElevenLabs): n0, j1, n1, n2, j18, n3a, n3b, j20 |
| 141 | STALE RENDER: mp4 is 69s but the current clips total only 44s — 24s of audio the new clips can't explain (budget 12s). I |
| 142 | STALE RENDER: mp4 is 61s but the current clips total only 28s — 33s of audio the new clips can't explain (budget 11s). I |
| 143 | STALE RENDER: mp4 is 61s but the current clips total only 33s — 28s of audio the new clips can't explain (budget 11s). I |
| 144 | STALE RENDER: mp4 is 62s but the current clips total only 38s — 24s of audio the new clips can't explain (budget 13s). I |
| 145 | STALE RENDER: mp4 is 61s but the current clips total only 29s — 32s of audio the new clips can't explain (budget 13s). I |
| 146 | STALE RENDER: mp4 is 97s but the current clips total only 62s — 35s of audio the new clips can't explain (budget 16s). I |
| 147 | STALE RENDER: mp4 is 127s but the current clips total only 79s — 48s of audio the new clips can't explain (budget 15s).  |
| 148 | STALE RENDER: mp4 is 173s but the current clips total only 145s — 28s of audio the new clips can't explain (budget 20s). |
| 149 | STALE RENDER: mp4 is 159s but the current clips total only 113s — 47s of audio the new clips can't explain (budget 19s). |
| 150 | STALE RENDER: mp4 is 156s but the current clips total only 85s — 71s of audio the new clips can't explain (budget 22s).  |
| 152 | STALE RENDER: mp4 is 163s but the current clips total only 123s — 40s of audio the new clips can't explain (budget 15s). |
| 153 | STALE RENDER: mp4 is 204s but the current clips total only 151s — 54s of audio the new clips can't explain (budget 17s). |
| 154 | STALE RENDER: mp4 is 179s but the current clips total only 133s — 47s of audio the new clips can't explain (budget 15s). |
| 155 | STALE RENDER: mp4 is 167s but the current clips total only 128s — 38s of audio the new clips can't explain (budget 15s). |
| 156 | STALE RENDER: mp4 is 162s but the current clips total only 128s — 33s of audio the new clips can't explain (budget 15s). |
| 157 | STALE RENDER: mp4 is 210s but the current clips total only 162s — 47s of audio the new clips can't explain (budget 17s). |
| 158 | STALE RENDER: mp4 is 187s but the current clips total only 158s — 29s of audio the new clips can't explain (budget 16s). |
| 159 | STALE RENDER: mp4 is 163s but the current clips total only 121s — 42s of audio the new clips can't explain (budget 15s). |
| 160 | STALE RENDER: mp4 is 201s but the current clips total only 154s — 47s of audio the new clips can't explain (budget 15s). |
| 162 | STALE RENDER: mp4 is 184s but the current clips total only 134s — 49s of audio the new clips can't explain (budget 17s). |
| 163 | STALE RENDER: mp4 is 163s but the current clips total only 122s — 41s of audio the new clips can't explain (budget 15s). |
| 164 | STALE RENDER: mp4 is 170s but the current clips total only 128s — 41s of audio the new clips can't explain (budget 15s). |
| 165 | STALE RENDER: mp4 is 158s but the current clips total only 121s — 37s of audio the new clips can't explain (budget 16s). |
| 166 | STALE RENDER: mp4 is 174s but the current clips total only 125s — 49s of audio the new clips can't explain (budget 16s). |
| 167 | STALE RENDER: mp4 is 148s but the current clips total only 113s — 35s of audio the new clips can't explain (budget 14s). |
| 168 | STALE RENDER: mp4 is 171s but the current clips total only 123s — 48s of audio the new clips can't explain (budget 17s). |
| 169 | STALE RENDER: mp4 is 169s but the current clips total only 119s — 49s of audio the new clips can't explain (budget 18s). |
| 171 | STALE RENDER: mp4 is 94s but the current clips total only 49s — 45s of audio the new clips can't explain (budget 15s). I |
| 172 | COMPLETE: 1 segment(s) have no audio clip: n1a |
| 173 | STALE RENDER: mp4 is 59s but the current clips total only 45s — 14s of audio the new clips can't explain (budget 14s). I |
| 174 | STALE RENDER: mp4 is 78s but the current clips total only 48s — 30s of audio the new clips can't explain (budget 13s). I |
| 175 | STALE RENDER: mp4 is 94s but the current clips total only 63s — 31s of audio the new clips can't explain (budget 13s). I |
| 176 | COMPLETE: 2 segment(s) have no audio clip: n3b, n4a |
| 177 | STALE RENDER: mp4 is 110s but the current clips total only 74s — 36s of audio the new clips can't explain (budget 17s).  |
| 178 | STALE RENDER: mp4 is 131s but the current clips total only 93s — 39s of audio the new clips can't explain (budget 17s).  |
| 179 | STALE RENDER: mp4 is 74s but the current clips total only 55s — 19s of audio the new clips can't explain (budget 14s). I |
| 180 | STALE RENDER: mp4 is 120s but the current clips total only 88s — 31s of audio the new clips can't explain (budget 16s).  |
| 181 | COMPLETE: 1 segment(s) have no audio clip: n1b |
| 182 | STALE RENDER: mp4 is 92s but the current clips total only 64s — 29s of audio the new clips can't explain (budget 14s). I |
| 183 | STALE RENDER: mp4 is 88s but the current clips total only 65s — 23s of audio the new clips can't explain (budget 12s). I |
| 184 | AUDIO ECHO (what it actually says): 1 spoken repeat(s), e.g. "Paul was shown more than words can carry, and still pointe |
| 185 | STALE RENDER: mp4 is 70s but the current clips total only 46s — 24s of audio the new clips can't explain (budget 13s). I |
| 186 | STALE RENDER: mp4 is 73s but the current clips total only 50s — 23s of audio the new clips can't explain (budget 13s). I |
| 187 | STALE RENDER: mp4 is 79s but the current clips total only 56s — 23s of audio the new clips can't explain (budget 13s). I |
| 188 | STALE RENDER: mp4 is 96s but the current clips total only 67s — 30s of audio the new clips can't explain (budget 13s). I |
| 189 | STALE RENDER: mp4 is 64s but the current clips total only 46s — 18s of audio the new clips can't explain (budget 11s). I |
| 190 | STALE RENDER: mp4 is 69s but the current clips total only 45s — 24s of audio the new clips can't explain (budget 13s). I |
| 191 | STALE RENDER: mp4 is 68s but the current clips total only 51s — 16s of audio the new clips can't explain (budget 12s). I |
| 192 | STALE RENDER: mp4 is 83s but the current clips total only 63s — 20s of audio the new clips can't explain (budget 13s). I |
| 193 | STALE RENDER: mp4 is 76s but the current clips total only 50s — 25s of audio the new clips can't explain (budget 14s). I |
| 194 | STALE RENDER: mp4 is 62s but the current clips total only 44s — 18s of audio the new clips can't explain (budget 12s). I |
| 195 | STALE RENDER: mp4 is 67s but the current clips total only 45s — 22s of audio the new clips can't explain (budget 13s). I |
| 196 | STALE RENDER: mp4 is 88s but the current clips total only 60s — 28s of audio the new clips can't explain (budget 14s). I |
| 197 | STALE RENDER: mp4 is 77s but the current clips total only 59s — 18s of audio the new clips can't explain (budget 11s). I |
| 198 | STALE RENDER: mp4 is 71s but the current clips total only 52s — 19s of audio the new clips can't explain (budget 11s). I |
| 199 | STALE RENDER: mp4 is 79s but the current clips total only 63s — 16s of audio the new clips can't explain (budget 11s). I |
| 200 | STALE RENDER: mp4 is 66s but the current clips total only 40s — 25s of audio the new clips can't explain (budget 13s). I |
