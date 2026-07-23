# ELEVENLABS VOICE PATH — setup + handoff (LANE CLAIM)

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

Once those are in the config, run `python3 revoice_sweep.py --range 1-10` to re-voice and
ear-check the first ten, eyeball one, then sweep the rest.

## Pronunciation is ElevenLabs' job now (respellings are DEAD)
The old `mbm_pronounce.py` respell dict is NOT applied on the ElevenLabs path. Archaic KJV
words (liveth, Esaias, Siloam, Elias, findeth, calleth, …) are handled by a pronunciation
**lexicon** in `eleven_config.json` (grapheme → IPA), uploaded once as an ElevenLabs
pronunciation dictionary and attached to every request. Seeded with the words Cameron has
complained about; add to it, never respell.
