#!/usr/bin/env python3
"""GREAT PLAN ElevenLabs narration engine — fork of the 200-queue module.

Same model, same render path, same timing sidecars. Differences:
  * GP speaker cast (mbm_speakers here): adds FATHER and DEVIL.
  * NARRATOR/JESUS/SCRIPTURE/WOMAN keep the exact voices Cameron approved for
    the 200 videos, so every MBM property sounds like one storyteller.
  * FATHER uses Bill — the same voice the 200-queue's GOD speaker uses.
  * DEVIL is Clyde (ElevenLabs premade, intense/gravelly) with lower stability —
    a voice that sounds evil, per Cameron 2026-08-31. If Clyde is unavailable the
    render FAILS LOUDLY; it never silently substitutes a sacred voice.
  * The key file holds MULTIPLE labeled keys — parse the first sk_ token
    (author-new-story-from-scratch lesson, 2026-08-13).
"""
import base64
import glob
import json
import os
import re

import requests

from mbm_speakers import NARRATOR, JESUS, FATHER, DEVIL, SCRIPTURE, WOMAN

API = "https://api.elevenlabs.io/v1"
MODEL = "eleven_multilingual_v2"

VOICE_ELEVEN = {
    NARRATOR:  ("Brian",   "nPczCjzI2devNBz1zQrb"),
    JESUS:     ("Chris",   "iP95p4xoKVk53GoZ742B"),
    FATHER:    ("Bill",    "pqHfZKP75CvOlQylNhV4"),
    DEVIL:     ("Clyde",   "2EiwWnXFnvU5JabPnv8n"),
    SCRIPTURE: ("Roger",   "CwhRBWXzGAHq8TQ4Fs17"),
    WOMAN:     ("Matilda", "XrExE9yKIg1WjnnlVkGX"),
}

VOICE_SETTINGS = {
    NARRATOR:  {"stability": 0.45, "similarity_boost": 0.80, "style": 0.0,  "use_speaker_boost": True},
    JESUS:     {"stability": 0.55, "similarity_boost": 0.80, "style": 0.0,  "use_speaker_boost": True},
    FATHER:    {"stability": 0.60, "similarity_boost": 0.80, "style": 0.0,  "use_speaker_boost": True},
    DEVIL:     {"stability": 0.38, "similarity_boost": 0.80, "style": 0.25, "use_speaker_boost": True},
    SCRIPTURE: {"stability": 0.50, "similarity_boost": 0.80, "style": 0.0,  "use_speaker_boost": True},
    WOMAN:     {"stability": 0.50, "similarity_boost": 0.80, "style": 0.0,  "use_speaker_boost": True},
}

_SENT = re.compile(r"[^.!?]*[.!?]+|\S[^.!?]*$")


def _key():
    """First sk_ token from the shared key file (which now holds several labeled
    keys — a raw read returns garbage)."""
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(5):
        hits = glob.glob(os.path.join(d, "media-production", "elevenlabs*KEY*.txt")) \
            or glob.glob(os.path.join(d, "elevenlabs*KEY*.txt"))
        if hits:
            raw = open(hits[0]).read()
            m = re.search(r"sk_[A-Za-z0-9]+", raw)
            if not m:
                raise RuntimeError(f"no sk_ key inside {hits[0]}")
            return m.group(0)
        d = os.path.dirname(d)
    raise RuntimeError("no ElevenLabs key file found (elevenlabs*KEY*.txt)")


# ElevenLabs-tested global respells (A/B'd 2026-09-01 against Brian via
# render + Gemini ear: carrier renders transcribed and stress-checked).
# Cameron's row-324/325 complaints: the old spaced/ALL-CAPS per-episode forms
# ("NEE fights", "Moh ROH nigh", "Kuh MORE uh") rendered as two words, stray
# "uh" grunts, or garbage ("Malachnai"). One fused lowercase word wins.
# Plain spelling WON for Gethsemane/Wycliffe/Gutenberg/Tyndale — do not add
# entries for those. Per-episode SPOKEN still overrides this map (homographs
# like "bow"/"US" stay per-episode by law).
ELEVEN_SAY = {
    "Nephi": "neefigh",     # "neefye" failed in-sentence (knee-fee); -igh holds /ai/
    "Nephites": "neefites",
    "Moroni": "moronye",
    "Cumorah": "kuhmorah",  # "kumorah" failed in-sentence (coo-mo-roh)
    "Elias": "eelighus",  # renders ih-LYE-us (natural); "eelyeus" mangled in-flow
}


def eleven_spoken_text(text, overrides=None):
    from mbm_pronounce import PHRASES
    for pat, rep in PHRASES:
        text = pat.sub(rep, text)
    merged = dict(ELEVEN_SAY)
    if overrides:
        merged.update(overrides)
    overrides = merged
    if overrides:
        low = {k.lower(): v for k, v in overrides.items()}
        def repl(m):
            w = m.group(0); v = low.get(w.lower())
            if v is None:
                return w
            return v[:1].upper() + v[1:] if (w[:1].isupper() and v[:1].islower()) else v
        text = re.sub(r"[A-Za-z]+", repl, text)
    return text


def _sentences_with_times(spoken, alignment):
    chars = alignment["characters"]
    starts = alignment["character_start_times_seconds"]
    ends = alignment["character_end_times_seconds"]
    out = []
    for m in _SENT.finditer(spoken):
        s = m.group(0).strip()
        if not s:
            continue
        a = max(0, min(m.start(), len(chars) - 1))
        b = max(0, min(m.end() - 1, len(chars) - 1))
        out.append({"text": s, "start": float(starts[a]), "end": float(ends[b])})
    return out


def render_segment(spoken_text_str, speaker, out_mp3, key=None):
    """Render one segment to mp3 + <name>.timing.json. Returns the sentence list."""
    key = key or _key()
    name, vid = VOICE_ELEVEN[speaker]
    r = requests.post(
        f"{API}/text-to-speech/{vid}/with-timestamps",
        headers={"xi-api-key": key, "Content-Type": "application/json"},
        json={"text": spoken_text_str, "model_id": MODEL,
              "voice_settings": VOICE_SETTINGS[speaker]},
        timeout=120,
    )
    if r.status_code != 200:
        raise RuntimeError(f"ElevenLabs {r.status_code} ({name}): {r.text[:200]}")
    data = r.json()
    with open(out_mp3, "wb") as f:
        f.write(base64.b64decode(data["audio_base64"]))
    sents = _sentences_with_times(spoken_text_str, data["alignment"])
    with open(os.path.splitext(out_mp3)[0] + ".timing.json", "w") as f:
        json.dump(sents, f)
    return sents
