# ELEVENLABS VOICE PATH — setup + handoff (HANDOFF TO #2, the audio maker)

> NOTE (2026-07-23): this scaffold was built by #1 (Planner) but the ElevenLabs
> voice-making lane belongs to **#2, the audio maker**. #1 does not run it.

**Lane claimed by Machine C (`cameron-lovett-MS-7C91`), 2026-07-23.** This is the
infrastructure lane for FRESH-CHAT-KICKOFF priority #1 — "set up the ElevenLabs path;
edge-tts is being retired." If another session is already building this, ping and split;
otherwise leave it to Machine C so we don't build the adapter twice.

---

## What this lane delivers

A **drop-in** ElevenLabs backend so the entire existing pipeline re-voices every video
with ElevenLabs instead of edge-tts, WITHOUT rewriting any of the 204 build scripts. A
build still declares a *speaker* per segment (SPEAKER-LAW); the speaker now maps to an
ElevenLabs voice instead of an `en-US-*Neural` edge voice. The caption `timing.json`
contract is reproduced exactly from ElevenLabs' word/character alignment, so captions stay
in sync with zero downstream changes.

### Files (all in `media-production/`)
- `mbm_eleven.py` — dependency-free (stdlib `urllib`) ElevenLabs REST client. Calls
  `/v1/text-to-speech/{voice}/with-timestamps`, returns mp3 bytes + per-sentence
  `{text,start,end}` timings in the SAME shape edge-tts produced. English-only model
  (the Voice Law bans any "Multilingual" model — ElevenLabs equivalent is an
  English-only model id, never `eleven_multilingual_*`).
- `eleven_config.json` — the ONE file Cameron touches: API key + one voice id per speaker
  + model id + optional pronunciation lexicon. Placeholders until he fills it.
- `mbm_caption_timing.py` (patched) — `save_narration` routes to ElevenLabs when
  `eleven_config.json` has a key AND the speaking voice is configured; otherwise it falls
  back to edge-tts exactly as before. Nothing breaks today.
- `revoice_sweep.py` — claim-aware runner: re-generates a build's audio with the new
  backend, runs the existing `qc_narration.py` ear-check, and reports pass/fail. No-ops
  with a clear message if no key is set.
- `redistribute_modules.py` — copies the canonical shared modules + config into all build
  folders (each build imports its LOCAL copy).

---

## ⛔ THE ONLY BLOCKER — two things only Cameron can give

Everything above is built and works the moment these are filled into `eleven_config.json`:

1. **ElevenLabs API key** (`xi-api-key`). Only Cameron has the account.
2. **Which ElevenLabs voice for each of the 5 speakers** — his creative pick from his
   ElevenLabs voice library, the same way he auditioned the edge-tts voices on 2026-07-18.
   The five are: `narrator`, `jesus` (must sound American — Voice Law), `god`,
   `scripture`, `woman`. He can start with just `narrator` + `jesus` and we test those first.

Once those are in the config:
```
python3 mbm_eleven.py                          # readiness check — all voices "ready"
python3 revoice_sweep.py --rows 5              # re-voice ONE, ear-check it (audio only)
python3 revoice_sweep.py --rows 5 --build      # + reassemble the mp4 to eyeball
python3 revoice_sweep.py --range 1-10 --build  # then sweep a batch
```
The sweep syncs the current engine modules into each build automatically (just-in-time),
runs `make_narration.py` (new audio) → `qc_narration.py` (whisper ear-check, must pass) →
`build.py` (with `--build`). Claim the rows in QUEUE.md and push the claim before a real
sweep. `redistribute_modules.py` is available to push the engine modules to all builds at
once if ever wanted, but the sweep does not need it.

## Pronunciation is ElevenLabs' job now (respellings are DEAD)
The old `mbm_pronounce.py` respell dict is NOT applied on the ElevenLabs path. Archaic KJV
words (liveth, Esaias, Siloam, Elias, findeth, calleth, …) are handled by a pronunciation
**lexicon** in `eleven_config.json` (grapheme → IPA), uploaded once as an ElevenLabs
pronunciation dictionary and attached to every request. Seeded with the words Cameron has
complained about; add to it, never respell.
