#!/usr/bin/env python3
"""MBM ElevenLabs narration engine — replaces edge-tts (2026-07-23 migration).

WHY: edge-tts (Azure neural, free) mispronounces King James English and gives no
lexicon control, so every fix was a hand-measured respelling tuned to one Azure
voice. ElevenLabs reads archaic English far better AND supports a server-side
pronunciation dictionary, so the whole respelling war can be replaced by one
measured lexicon. Voices chosen by Cameron 2026-07-23 (see VOICE_ELEVEN).

CLEAN PRONUNCIATION LAYER: the old SAY / SAY_BY_VOICE respellings in
mbm_pronounce.py were measured on Azure voices and must NOT be applied here — they
would HURT ElevenLabs. Only two engine-agnostic layers carry over:
  * PHRASES  — true orthographic splits ("to day"->"today", strip () emoticons)
  * per-build SPOKEN overrides — homographs the sentence decides (tear/lead/wound)
Everything else starts empty and grows ONLY from words measured to break on these
ElevenLabs voices (round-tripped through whisper, same discipline as before).

TIMING: caption timing needs real per-sentence timestamps. ElevenLabs'
/with-timestamps endpoint returns character-level alignment; we aggregate it to
per-sentence start/end and write the same <name>.timing.json sidecar edge-tts did,
so mbm_caption_timing consumes it unchanged.
"""
import base64
import glob
import json
import os
import re

import requests

from mbm_speakers import NARRATOR, JESUS, GOD, SCRIPTURE, WOMAN

API = "https://api.elevenlabs.io/v1"
MODEL = "eleven_multilingual_v2"  # ElevenLabs flagship English model = the sampler Cameron approved.

# Cameron's cast, locked 2026-07-23.
VOICE_ELEVEN = {
    NARRATOR:  ("Brian",   "nPczCjzI2devNBz1zQrb"),
    JESUS:     ("Chris",   "iP95p4xoKVk53GoZ742B"),
    GOD:       ("Bill",    "pqHfZKP75CvOlQylNhV4"),
    SCRIPTURE: ("Roger",   "CwhRBWXzGAHq8TQ4Fs17"),
    WOMAN:     ("Matilda", "XrExE9yKIg1WjnnlVkGX"),
}

# Reverent, steady delivery. Higher stability = less wandering; modest style.
VOICE_SETTINGS = {
    NARRATOR:  {"stability": 0.45, "similarity_boost": 0.80, "style": 0.0, "use_speaker_boost": True},
    JESUS:     {"stability": 0.55, "similarity_boost": 0.80, "style": 0.0, "use_speaker_boost": True},
    GOD:       {"stability": 0.60, "similarity_boost": 0.80, "style": 0.0, "use_speaker_boost": True},
    SCRIPTURE: {"stability": 0.50, "similarity_boost": 0.80, "style": 0.0, "use_speaker_boost": True},
    WOMAN:     {"stability": 0.50, "similarity_boost": 0.80, "style": 0.0, "use_speaker_boost": True},
}

_SENT = re.compile(r"[^.!?]*[.!?]+|\S[^.!?]*$")


def _key():
    # search this module's dir and walk up to the shared media-production root,
    # so a copy of this module inside a build folder still finds the one key.
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(4):
        f = glob.glob(os.path.join(d, "elevenlabs*KEY*.txt"))
        if f:
            raw = open(f[0]).read()
            m = re.search(r"sk_[A-Za-z0-9]+", raw)   # tolerate a label/colon around the key
            if m:
                return m.group(0)
            return raw.strip()
        d = os.path.dirname(d)
    raise RuntimeError("no ElevenLabs key file found (elevenlabs*KEY*.txt)")


def eleven_spoken_text(text, overrides=None):
    """The ElevenLabs spoken string: ONLY engine-agnostic fixes. No Azure respellings.
    Applies PHRASES (orthographic) and any per-build SPOKEN overrides (homographs)."""
    from mbm_pronounce import PHRASES
    for pat, rep in PHRASES:
        text = pat.sub(rep, text)
    if overrides:
        # word-boundary replace, preserving a leading capital
        low = {k.lower(): v for k, v in overrides.items()}
        def repl(m):
            w = m.group(0); v = low.get(w.lower())
            if v is None:
                return w
            return v[:1].upper() + v[1:] if (w[:1].isupper() and v[:1].islower()) else v
        text = re.sub(r"[A-Za-z]+", repl, text)
    return text


def _sentences_with_times(spoken, alignment):
    """Aggregate ElevenLabs char-level alignment into per-sentence start/end."""
    chars = alignment["characters"]
    starts = alignment["character_start_times_seconds"]
    ends = alignment["character_end_times_seconds"]
    out, idx = [], 0
    for m in _SENT.finditer(spoken):
        s = m.group(0).strip()
        if not s:
            continue
        a = m.start()
        b = m.end() - 1
        a = max(0, min(a, len(chars) - 1))
        b = max(0, min(b, len(chars) - 1))
        out.append({"text": s, "start": float(starts[a]), "end": float(ends[b])})
    return out


# Some transcripts abbreviate speaker tags (e.g. build-15 uses 'nar'/'jes').
SPEAKER_ALIAS = {
    "nar": NARRATOR, "narr": NARRATOR, "n": NARRATOR,
    "jes": JESUS, "jesus": JESUS, "j": JESUS,
    "god": GOD, "g": GOD,
    "scr": SCRIPTURE, "scripture": SCRIPTURE, "s": SCRIPTURE,
    "wom": WOMAN, "woman": WOMAN, "w": WOMAN,
}


def render_segment(spoken_text_str, speaker, out_mp3, key=None):
    """Render one segment to mp3 + <name>.timing.json. Returns the sentence list."""
    key = key or _key()
    speaker = SPEAKER_ALIAS.get(speaker, speaker)
    name, vid = VOICE_ELEVEN[speaker]
    r = requests.post(
        f"{API}/text-to-speech/{vid}/with-timestamps",
        headers={"xi-api-key": key, "Content-Type": "application/json"},
        json={"text": spoken_text_str, "model_id": MODEL,
              "voice_settings": VOICE_SETTINGS[speaker]},
        timeout=120,
    )
    if r.status_code != 200:
        raise RuntimeError(f"ElevenLabs {r.status_code}: {r.text[:200]}")
    data = r.json()
    with open(out_mp3, "wb") as f:
        f.write(base64.b64decode(data["audio_base64"]))
    sents = _sentences_with_times(spoken_text_str, data["alignment"])
    with open(os.path.splitext(out_mp3)[0] + ".timing.json", "w") as f:
        json.dump(sents, f)
    return sents


if __name__ == "__main__":
    # self-test: render one line per voice into VOICE-SAMPLER/_engine-test
    os.makedirs("VOICE-SAMPLER/_engine-test", exist_ok=True)
    tests = [
        (NARRATOR,  "There was a woman who had been suffering for twelve years. Nothing helped."),
        (JESUS,     "Daughter, thy faith hath made thee whole; go in peace."),
    ]
    k = _key()
    for spk, txt in tests:
        spoken = eleven_spoken_text(txt)
        out = f"VOICE-SAMPLER/_engine-test/{spk}.mp3"
        sents = render_segment(spoken, spk, out, key=k)
        print(f"{spk:<10} -> {out}  sentences={len(sents)} last_end={sents[-1]['end']:.2f}s")
        for s in sents:
            print(f"     [{s['start']:.2f}-{s['end']:.2f}] {s['text']}")
