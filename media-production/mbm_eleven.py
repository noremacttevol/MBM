#!/usr/bin/env python3
"""MBM ElevenLabs voice backend — dependency-free (stdlib only).

Replaces edge-tts as the TTS engine while keeping every downstream contract
identical, so none of the 204 build scripts change. See ELEVENLABS-SETUP.md.

WHAT IT GUARANTEES (the contract mbm_caption_timing.save_narration relied on):
  synth(text, speaker) -> (mp3_bytes, sentences)
  where `sentences` is a list of {"text": <sentence>, "start": <sec>, "end": <sec>}
  in SEGMENT-LOCAL seconds — byte-for-byte the same shape edge-tts produced from
  its SentenceBoundary events. timed_windows() downstream is unchanged.

VOICE LAW: the Jesus voice must sound American, and NO "Multilingual" model may
ever be used (edge-tts drift bug, 2026-07-08). ElevenLabs' equivalent of that ban
is the model id: use an English-only model (default `eleven_turbo_v2`), never
`eleven_multilingual_*`. load_config() refuses a multilingual model id.

PRONUNCIATION: the old respelling dict (mbm_pronounce) is NOT used here. Archaic
KJV words are handled by an ElevenLabs pronunciation dictionary built from the
`lexicon` in eleven_config.json (grapheme -> IPA). It is created once and its
locator cached back into the config, then attached to every request.

Config lives in eleven_config.json next to this module (or in the parent
media-production/ dir when this module sits inside a build folder).
"""
import base64
import json
import os
import re
import urllib.error
import urllib.request

API_ROOT = "https://api.elevenlabs.io/v1"
HERE = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.dirname(HERE)

# Same sentence split the caption timer uses, so sentence text lines up 1:1 with
# what timed_windows() will look for later.
_SENT_RE = re.compile(r"(?<=[.!?;:]) +")


def _sentences(text):
    return [p for p in _SENT_RE.split(text.strip()) if p]


# ----------------------------------------------------------------- config ----

def config_path():
    """eleven_config.json, found whether this module runs from media-production/
    or from a build folder that has a copy of the config beside it."""
    for d in (HERE, _PARENT, os.path.join(_PARENT, "media-production")):
        p = os.path.join(d, "eleven_config.json")
        if os.path.exists(p):
            return p
    return os.path.join(HERE, "eleven_config.json")


def load_config():
    p = config_path()
    if not os.path.exists(p):
        return None
    with open(p) as f:
        cfg = json.load(f)
    model = (cfg.get("model_id") or "").lower()
    if "multilingual" in model:
        raise ValueError(
            f"eleven_config.json model_id {cfg.get('model_id')!r} is a Multilingual "
            "model — banned by the Voice Law. Use an English-only model "
            "(e.g. eleven_turbo_v2).")
    return cfg


def _save_config(cfg):
    with open(config_path(), "w") as f:
        json.dump(cfg, f, indent=2)


def api_key(cfg=None):
    """Key from config or the ELEVENLABS_API_KEY env var (env wins if set).
    A `PUT_...` placeholder counts as unset."""
    cfg = cfg if cfg is not None else load_config()
    k = (os.environ.get("ELEVENLABS_API_KEY")
         or (cfg or {}).get("api_key") or "").strip()
    return "" if k.startswith("PUT_") else k


def is_configured(speaker=None, cfg=None):
    """True when we can synthesize: a key exists AND (if a speaker is named) that
    speaker has a real voice id. This is what save_narration checks to decide
    whether to use ElevenLabs or fall back to edge-tts."""
    cfg = cfg if cfg is not None else load_config()
    if not cfg or not api_key(cfg):
        return False
    if speaker is None:
        return True
    vid = (cfg.get("voices") or {}).get(speaker, "")
    return bool(vid) and not vid.startswith("PUT_")


def voice_id(speaker, cfg=None):
    cfg = cfg if cfg is not None else load_config()
    vid = (cfg.get("voices") or {}).get(speaker, "")
    if not vid or vid.startswith("PUT_"):
        raise ValueError(
            f"no ElevenLabs voice configured for speaker {speaker!r} — set "
            f'voices.{speaker} in eleven_config.json (Cameron picks it from his '
            "ElevenLabs library).")
    return vid


# ------------------------------------------------ pronunciation dictionary ----

def _http(method, path, key, body=None, is_json=True):
    url = path if path.startswith("http") else API_ROOT + path
    data = None
    headers = {"xi-api-key": key}
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read()
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:500]
        raise RuntimeError(f"ElevenLabs {method} {url} -> {e.code}: {detail}") from None
    return json.loads(raw) if is_json else raw


def ensure_lexicon(cfg=None):
    """Create the pronunciation dictionary from cfg['lexicon'] once, cache its
    locator in the config, and return the locator (or None if no lexicon).

    lexicon entries: {"grapheme": "Esaias", "phoneme": "ɪˈzeɪəs"} (IPA), or
    {"grapheme": "Cana", "alias": "Kane-uh"} for a plain respelling alias.
    """
    cfg = cfg if cfg is not None else load_config()
    lex = (cfg or {}).get("lexicon") or []
    if not lex:
        return None
    loc = cfg.get("_lexicon_locator")
    if loc and loc.get("pronunciation_dictionary_id"):
        return loc
    key = api_key(cfg)
    rules = []
    for e in lex:
        g = e.get("grapheme")
        if not g:
            continue
        if e.get("phoneme"):
            rules.append({"type": "phoneme", "string_to_replace": g,
                          "phoneme": e["phoneme"], "alphabet": "ipa"})
        elif e.get("alias"):
            rules.append({"type": "alias", "string_to_replace": g,
                          "alias": e["alias"]})
    if not rules:
        return None
    resp = _http("POST", "/pronunciation-dictionaries/add-from-rules", key,
                 {"name": "mbm-kjv-lexicon", "rules": rules})
    loc = {"pronunciation_dictionary_id": resp.get("id"),
           "version_id": resp.get("version_id")}
    cfg["_lexicon_locator"] = loc
    _save_config(cfg)
    return loc


# ------------------------------------------------------------- synthesis ----

def _alignment_to_sentences(text, alignment):
    """Fold ElevenLabs character alignment into per-sentence {text,start,end}.

    alignment = {characters:[...], character_start_times_seconds:[...],
                 character_end_times_seconds:[...]} over the SPOKEN string.
    We walk the returned characters and cut a new sentence every time the
    running text matches the next expected sentence boundary — robust to the
    minor whitespace ElevenLabs may normalize."""
    chars = alignment.get("characters") or []
    starts = alignment.get("character_start_times_seconds") or []
    ends = alignment.get("character_end_times_seconds") or []
    sents = _sentences(text)
    if not chars or not starts or not ends or not sents:
        return _fallback_even(text, ends[-1] if ends else 0.0)

    # Normalized target lengths (letters/digits only) per sentence, so alignment
    # whitespace/punctuation differences don't throw off the split.
    def norm(s):
        return re.sub(r"[^a-z0-9]", "", s.lower())

    targets = [len(norm(s)) for s in sents]
    out, si, seen, cur_start, last_end = [], 0, 0, None, 0.0
    for i, c in enumerate(chars):
        st, en = starts[i], ends[i]
        if re.match(r"[A-Za-z0-9]", c):
            if cur_start is None:
                cur_start = st
            seen += 1
            last_end = en
            if si < len(targets) and seen >= targets[si]:
                out.append({"text": sents[si],
                            "start": round(cur_start or 0.0, 3),
                            "end": round(en, 3)})
                si += 1
                seen, cur_start = 0, None
        else:
            last_end = max(last_end, en)
    # Any trailing sentence the counter didn't close (rounding) gets the tail.
    while si < len(sents):
        out.append({"text": sents[si],
                    "start": round(cur_start if cur_start is not None else last_end, 3),
                    "end": round(last_end, 3)})
        si += 1
        cur_start = None
    return out


def _fallback_even(text, total):
    """Char-proportional timing if alignment is unusable — keeps captions sane
    rather than crashing. total = spoken duration in seconds."""
    sents = _sentences(text)
    lens = [max(1, len(s)) for s in sents]
    tot = sum(lens) or 1
    out, acc = [], 0.0
    for s, L in zip(sents, lens):
        st = total * acc / tot
        acc += L
        out.append({"text": s, "start": round(st, 3),
                    "end": round(total * acc / tot, 3)})
    return out


def synth(text, speaker, cfg=None):
    """Return (mp3_bytes, sentences) for `text` in `speaker`'s voice.

    sentences: [{text,start,end}] in segment-local seconds — the timing.json
    contract. Raises if the speaker/key isn't configured (caller decides fallback).
    """
    cfg = cfg if cfg is not None else load_config()
    if cfg is None:
        raise RuntimeError("eleven_config.json not found")
    key = api_key(cfg)
    if not key:
        raise RuntimeError("no ElevenLabs API key (config api_key or ELEVENLABS_API_KEY)")
    vid = voice_id(speaker, cfg)
    model = cfg.get("model_id") or "eleven_turbo_v2"
    settings = (cfg.get("voice_settings") or {}).get(speaker) \
        or cfg.get("voice_settings_default") \
        or {"stability": 0.5, "similarity_boost": 0.75, "style": 0.0,
            "use_speaker_boost": True}
    body = {"text": text, "model_id": model, "voice_settings": settings}
    loc = ensure_lexicon(cfg)
    if loc:
        body["pronunciation_dictionary_locators"] = [loc]
    fmt = cfg.get("output_format", "mp3_44100_128")
    path = f"/text-to-speech/{vid}/with-timestamps?output_format={fmt}"
    resp = _http("POST", path, key, body)
    audio_b64 = resp.get("audio_base64") or resp.get("audio")
    if not audio_b64:
        raise RuntimeError("ElevenLabs response had no audio_base64")
    mp3 = base64.b64decode(audio_b64)
    alignment = resp.get("alignment") or resp.get("normalized_alignment") or {}
    sents = _alignment_to_sentences(text, alignment)
    return mp3, sents


def check():
    """Human-readable readiness report. Never raises."""
    cfg = load_config()
    if cfg is None:
        return "eleven_config.json: MISSING"
    lines = [f"config: {config_path()}",
             f"api_key: {'set' if api_key(cfg) else 'MISSING'}",
             f"model_id: {cfg.get('model_id')}"]
    voices = cfg.get("voices") or {}
    for sp in ("narrator", "jesus", "god", "scripture", "woman"):
        vid = voices.get(sp, "")
        state = "ready" if (vid and not vid.startswith("PUT_")) else "NOT SET"
        lines.append(f"  voice[{sp}]: {vid or '(none)'}  [{state}]")
    lex = cfg.get("lexicon") or []
    lines.append(f"lexicon: {len(lex)} rule(s)"
                 + (" (dictionary created)" if cfg.get("_lexicon_locator") else ""))
    return "\n".join(lines)


if __name__ == "__main__":
    print(check())
