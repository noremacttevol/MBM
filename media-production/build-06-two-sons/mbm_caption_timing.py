#!/usr/bin/env python3
"""Shared caption-timing helper for MBM story videos.

THE PROBLEM THIS FIXES
----------------------
The old caption timer guessed each chunk's on-screen window by dividing the
segment's spoken duration proportionally by CHARACTER COUNT. Characters are not
seconds — short sentences and long ones do not speak at the same rate — so the
captions drifted out of sync with the voice, and independently-computed fade
in/out windows let two lines overlap on screen.

THE FIX
-------
edge-tts emits a SentenceBoundary event per sentence with a REAL start offset
and duration. We capture those during narration generation and save them next to
the mp3 as `<name>.timing.json`. At build time we anchor each caption chunk to
the real timestamps of the sentences it contains. Windows are contiguous and
non-overlapping, so captions match the voice and never stack.

USAGE
-----
make_narration.py:
    from mbm_caption_timing import save_narration            # replaces tts.save
    await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")

build.py caption layer:
    from mbm_caption_timing import timed_windows
    windows = timed_windows(f"audio/{seg}.mp3", chunks, spoken_len, lead)
    # windows[i] = (start_s, end_s) in STILL-LOCAL time for chunks[i]
"""
import json
import os
import re


def _sentences(text):
    return [p for p in re.split(r"(?<=[.!?;:]) +", text.strip()) if p]


async def save_narration(tts_text, voice, rate, pitch, out_mp3):
    """Generate the mp3 AND write a real per-sentence timing sidecar.

    Sidecar path: same as out_mp3 but with .timing.json. Each entry:
      {"text": <sentence>, "start": <s>, "end": <s>}   (segment-local seconds)
    """
    import edge_tts
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


def _load_timing(mp3_path):
    p = os.path.splitext(mp3_path)[0] + ".timing.json"
    if not os.path.exists(p):
        return None
    try:
        with open(p) as f:
            data = json.load(f)
        return data or None
    except Exception:
        return None


def timed_windows(mp3_path, chunks, spoken_len, lead, tail=0.30):
    """Return [(start_s, end_s), ...] in STILL-LOCAL time, one per chunk.

    Anchors each caption chunk to the REAL spoken timing of the sentences it
    contains (from the .timing.json sidecar). Falls back to proportional-by-char
    timing only if the sidecar is missing or its sentence count can't be mapped.
    All timings are offset by `lead` so they line up with where the audio was
    placed inside the still. Windows are contiguous — no overlap.
    """
    n = len(chunks)
    if n == 0:
        return []
    timing = _load_timing(mp3_path)

    # --- fallback: proportional by character count (the OLD behavior) ---
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

    # 1) Build a per-CHARACTER timeline from the real sentence timings.
    #    Inside each sentence, spread its characters linearly across that
    #    sentence's true [start, end]. This anchors every character to real
    #    spoken time — no global char-count guess.
    char_t = []          # char_t[k] = spoken time of normalized char k
    for s in timing:
        ntext = norm(s["text"])
        if not ntext:
            continue
        cs = lead + s["start"]
        ce = lead + s["end"]
        L = len(ntext)
        for j in range(L):
            char_t.append(cs + (ce - cs) * (j / L))
    if not char_t:
        return _proportional()
    stream_end = lead + timing[-1]["end"]

    # 2) Walk each chunk across the character stream, in order. Chunk text is
    #    the same source text (verbatim, just re-wrapped), so normalized chars
    #    line up. Window = time of first char .. time of last char.
    windows, cur = [], 0
    total_chars = len(char_t)
    ok = True
    for c in chunks:
        nc = norm(c)
        L = len(nc)
        if L == 0:
            ok = False
            break
        start_idx = min(cur, total_chars - 1)
        end_idx = min(cur + L - 1, total_chars - 1)
        windows.append((char_t[start_idx], char_t[end_idx]))
        cur += L
    # sanity: consumed roughly the whole stream (guards against text mismatch)
    if not ok or abs(cur - total_chars) > max(6, int(0.15 * total_chars)):
        return _proportional()

    # 3) Contiguous, non-overlapping: each chunk holds until the next begins;
    #    last chunk gets a small tail. No stacking, no flicker gap.
    fixed = []
    for i, (cs, ce) in enumerate(windows):
        if i + 1 < n:
            ce = windows[i + 1][0]
        else:
            ce = min(stream_end, ce) + tail
        fixed.append((max(0.0, cs), max(cs + 0.30, ce)))
    return fixed
