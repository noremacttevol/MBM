#!/usr/bin/env python3
"""MBM shared caption system — the single source of truth for how captions
look and sync on every story video. See CAPTION-LAW.md.

Provides:
  save_narration(text, voice, rate, pitch, out_mp3)  -> writes mp3 + timing.json
  timed_windows(mp3, chunks, spoken_len, lead)       -> real per-chunk windows
  caption_layers(seg_id, dur, spoken_end, text, kjv) -> (filters, labels)

caption_layers is a drop-in replacement for the old per-build function (same
signature), so each build.py just imports it instead of defining its own.

THE LOOK (CAPTION-LAW):
  * Font: Jost Bold — geometric, flat-cross "t". Jesus's words RED, narration white.
  * Band pinned to the very bottom, full width, sized to fit the text (thin for
    one short line, taller for 2-3). Medium-dark (50%). Never wasteful.
  * Every line individually centered (text_align=C). Respectful side margin.
  * Timing anchored to REAL edge-tts per-sentence timestamps; no overlap.
  * Fixed 1080x1920, zoom-crop to fill — identical on every screen.
"""
import json
import os
import re
import textwrap

from PIL import ImageFont

# ---- geometry / style (CAPTION-LAW constants) ----
W, H = 1080, 1920
FPS = 30
HERE = os.path.dirname(os.path.abspath(__file__))
_SHARED = os.path.dirname(HERE)  # media-production/ when module sits in a build dir


def _find_font(name):
    for d in (HERE, _SHARED, os.path.join(_SHARED, "media-production")):
        p = os.path.join(d, name)
        if os.path.exists(p):
            return p
    return os.path.join(_SHARED, name)


JOST = _find_font("Jost-Bold.ttf")
JESUS_RED = "0xEE3322"
WHITE = "white"

# Speaker system (SPEAKER-LAW.md). Imported lazily-tolerantly so a build folder
# that has not yet had mbm_speakers.py copied in still renders in the old
# two-colour world instead of crashing mid-run.
try:
    from mbm_speakers import color_of as _color_of, is_scripture as _is_scripture
except ImportError:                                    # pragma: no cover
    _SPEAKER_COLOR = {"narrator": WHITE, "jesus": JESUS_RED, "god": "0x5BE38B",
                      "scripture": "0x8FDCFF", "woman": "0xFF9EC7"}

    def _color_of(sp):
        return _SPEAKER_COLOR[sp]

    def _is_scripture(sp):
        return sp != "narrator"


def _resolve(speaker):
    """Accept a speaker string OR the legacy `kjv` boolean.

    The 200 builds are migrated one at a time; until a build is converted it
    still passes True/False here. True meant 'Jesus red', False meant narrator.
    """
    if isinstance(speaker, bool):
        return "jesus" if speaker else "narrator"
    if speaker is None:
        return "narrator"
    return speaker
BAND_ALPHA = 0.5          # medium-dark, picture shows through
SIDE_MARGIN = 56          # respectful gap from phone edges
USABLE = W - 2 * SIDE_MARGIN
PAD_X, PAD_Y = 34, 24     # inner padding inside the band
LINE_GAP = 12
MAX_FS, MIN_FS = 54, 40   # readable range
KJV_MAX_FS = 56
MAX_LINES = 3
FADE = 0.30


# ===================== narration + real timing =====================

def _sentences(text):
    return [p for p in re.split(r"(?<=[.!?;:]) +", text.strip()) if p]


# Reverse map voice-ID -> speaker key, so the pronunciation dict is ALWAYS
# applied at the bottom of the funnel — safety net for any script that calls
# save_narration directly with raw text (129 builds did exactly that until
# 2026-07-20 and never got a single pronunciation fix). spoken_text is
# idempotent — respelled output contains no dict keys — so builds that already
# applied it upstream are unaffected by the second pass.
_SPEAKER_OF_VOICE = {
    "en-US-AndrewNeural": "narrator",
    "en-US-EricNeural": "jesus",
    "en-US-ChristopherNeural": "god",
    "en-US-SteffanNeural": "scripture",
    "en-US-MichelleNeural": "woman",
}


async def save_narration(tts_text, voice, rate, pitch, out_mp3):
    """Generate mp3 AND a <name>.timing.json sidecar of REAL per-sentence
    spoken timestamps (segment-local seconds)."""
    import edge_tts
    from mbm_pronounce import spoken_text
    tts_text = spoken_text(tts_text, None, _SPEAKER_OF_VOICE.get(voice))
    tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
    sents, audio = [], bytearray()
    async for ch in tts.stream():
        t = ch["type"]
        if t == "audio":
            audio += ch["data"]
        elif t == "SentenceBoundary":
            s = ch["offset"] / 1e7
            sents.append({"text": ch["text"], "start": s,
                          "end": s + ch["duration"] / 1e7})
    with open(out_mp3, "wb") as f:
        f.write(audio)
    with open(os.path.splitext(out_mp3)[0] + ".timing.json", "w") as f:
        json.dump(sents, f)
    return sents


async def save_speaker_narration(tts_text, speaker, out_mp3, rate=None, pitch=None):
    """save_narration, but the voice comes from WHO IS SPEAKING (SPEAKER-LAW.md).

    A build never names a voice again — it names a speaker, and the voice and the
    caption colour are both derived from that one declaration, so they cannot drift
    apart. Per-segment rate/pitch overrides are still allowed for the rare beat
    that needs them.
    """
    if os.environ.get("MBM_TTS") == "eleven":
        # tts_text already passed through spoken_text(), which under MBM_TTS=eleven
        # emits the clean ElevenLabs spelling. Render via the ElevenLabs engine,
        # which writes the same mp3 + .timing.json sidecar edge-tts did.
        from mbm_eleven import render_segment
        return render_segment(tts_text, speaker, out_mp3)
    from mbm_speakers import voice_of
    voice, r, p = voice_of(speaker, rate, pitch)
    return await save_narration(tts_text, voice, r, p, out_mp3)


def _load_timing(mp3_path):
    p = os.path.splitext(mp3_path)[0] + ".timing.json"
    if not os.path.exists(p):
        return None
    try:
        with open(p) as f:
            return json.load(f) or None
    except Exception:
        return None


# ===================== chunking + timing windows =====================

def chunk_caption(text, width, max_lines):
    """Group sentences into on-screen chunks ~<= max_lines at char width."""
    out, cur = [], ""
    for s in _sentences(text):
        cand = (cur + " " + s).strip()
        if len(textwrap.wrap(cand, width)) <= max_lines:
            cur = cand
            continue
        if cur:
            out.append(cur)
        if len(textwrap.wrap(s, width)) <= max_lines:
            cur = s
        else:
            piece = ""
            for frag in s.split(", "):
                cand2 = (piece + ", " + frag).strip(", ").strip()
                if len(textwrap.wrap(cand2, width)) <= max_lines:
                    piece = cand2
                else:
                    if piece:
                        out.append(piece)
                    piece = frag
            cur = piece
    if cur:
        out.append(cur)
    return out


def timed_windows(mp3_path, chunks, spoken_len, lead, tail=0.30):
    """[(start,end)] still-local seconds per chunk, anchored to REAL timing.
    Contiguous, non-overlapping. Falls back to char-proportional if no sidecar."""
    n = len(chunks)
    if n == 0:
        return []
    timing = _load_timing(mp3_path)

    def _proportional():
        t0, t1 = 0.15, max(0.6, lead + spoken_len + 0.35)
        total = sum(len(c) for c in chunks) or 1
        out, acc = [], 0
        for c in chunks:
            cs = t0 + (t1 - t0) * acc / total
            acc += len(c)
            ce = t0 + (t1 - t0) * acc / total
            out.append((cs, ce))
        return out

    if not timing:
        return _proportional()

    def norm(x):
        return re.sub(r"[^a-z0-9]", "", x.lower())

    char_t = []
    for s in timing:
        nt = norm(s["text"])
        if not nt:
            continue
        cs, ce, L = lead + s["start"], lead + s["end"], len(nt)
        for j in range(L):
            char_t.append(cs + (ce - cs) * (j / L))
    if not char_t:
        return _proportional()
    stream_end = lead + timing[-1]["end"]

    windows, cur, total_chars, ok = [], 0, len(char_t), True
    for c in chunks:
        L = len(norm(c))
        if L == 0:
            ok = False
            break
        si = min(cur, total_chars - 1)
        ei = min(cur + L - 1, total_chars - 1)
        windows.append((char_t[si], char_t[ei]))
        cur += L
    if not ok or abs(cur - total_chars) > max(6, int(0.15 * total_chars)):
        return _proportional()

    fixed = []
    for i, (cs, ce) in enumerate(windows):
        ce = windows[i + 1][0] if i + 1 < n else min(stream_end, ce) + tail
        fixed.append((max(0.0, cs), max(cs + 0.30, ce)))
    return fixed


# ===================== adaptive band rendering =====================

def _wrap_pixels(text, fs):
    f = ImageFont.truetype(JOST, fs)
    words, lines, cur = text.split(), [], ""
    for w in words:
        cand = (cur + " " + w).strip()
        if f.getbbox(cand)[2] <= USABLE:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _layout(text, scripture):
    """Largest font size fitting text in fewest lines (<=MAX_LINES)."""
    hi = KJV_MAX_FS if scripture else MAX_FS
    for fs in range(hi, MIN_FS - 1, -2):
        lines = _wrap_pixels(text, fs)
        if len(lines) <= MAX_LINES:
            return fs, lines
    return MIN_FS, _wrap_pixels(text, MIN_FS)[:MAX_LINES]


def caption_filter(seg_id, dur, spoken_end, text, speaker):
    """Return a filter-string (leading comma) drawing an adaptively-sized dark
    band + centered Jost-Bold text DIRECTLY on the still, each chunk time-gated
    to its REAL spoken window via enable=. Appended straight to the base chain.

    `speaker` decides the colour (SPEAKER-LAW.md): narrator white, Jesus red,
    God green, scripture light blue, women pink. The legacy `kjv` boolean is
    still accepted while the 200 builds migrate. Band sized to fit (thin for
    short, taller for 2-3 lines). Drawing on the opaque still is what makes the
    band actually show (drawbox on a transparent overlay layer leaves alpha=0
    and stays invisible)."""
    S = "segs"
    speaker = _resolve(speaker)
    color = _color_of(speaker)
    scripture = _is_scripture(speaker)
    chunks = chunk_caption(text, 42, 2)
    spoken_len = max(0.0, spoken_end - 0.28)
    windows = timed_windows(f"audio/{seg_id}.mp3", chunks, spoken_len, 0.28)

    parts = []
    for i, c in enumerate(chunks):
        fs, lines = _layout(c, scripture)
        f = ImageFont.truetype(JOST, fs)
        asc, desc = f.getmetrics()
        line_h = asc + desc
        nlines = len(lines)
        band_h = nlines * line_h + (nlines - 1) * LINE_GAP + 2 * PAD_Y
        band_y = H - band_h
        text_y = band_y + PAD_Y

        tf = f"{S}/{seg_id}_{i}.txt"
        with open(tf, "w") as fh:
            fh.write("\n".join(lines))

        cs, ce = windows[i]
        cs = max(0.05, min(cs, dur - 0.3))
        ce = max(cs + 0.3, min(ce, dur))
        en = f"enable='between(t,{cs:.2f},{ce:.2f})'"
        parts.append(
            f"drawbox=x=0:y={band_y}:w={W}:h={band_h}:"
            f"color=black@{BAND_ALPHA}:t=fill:{en}")
        parts.append(
            f"drawtext=fontfile={JOST}:textfile={tf}:fontsize={fs}:"
            f"fontcolor={color}:text_align=C:line_spacing={LINE_GAP}:"
            f"x=(w-text_w)/2:y={text_y}:"
            f"shadowcolor=black@0.9:shadowx=2:shadowy=2:{en}")
    return ("," + ",".join(parts)) if parts else ""


# Back-compat shim: older build_still expected (filters, labels) + overlay. New
# builds call caption_filter directly. Kept so a half-migrated tree still parses.
def caption_layers(seg_id, dur, spoken_end, text, speaker):
    raise RuntimeError(
        "caption_layers is retired — use caption_filter() drawn on the base "
        "still. Re-run apply_caption_law.py to migrate this build.")
