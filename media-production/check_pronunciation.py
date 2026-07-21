#!/usr/bin/env python3
"""MBM pronunciation checker — the ear that tells you if edge-tts actually said it.

The problem: edge-tts mispronounces King James English. You cannot tell by reading the
text; you have to LISTEN. This closes that loop automatically: render the line, transcribe
it back, and compare against what the words are supposed to sound like.

Usage:
  # check one line as a given voice
  python3 check_pronunciation.py --text "He that forsaketh not all that he hath" \
                                 --voice en-US-ChristopherNeural

  # check a whole build's narration (uses its SEGMENTS + SPOKEN dict)
  python3 check_pronunciation.py --build build-41-counting-the-cost

  # try a candidate respelling before committing it
  python3 check_pronunciation.py --text "forsaketh" --spoken "for-SAY-keth"

How to read the output: it prints the CAPTION words (what the viewer reads) next to what
the transcriber HEARD. A mismatch is not automatically a defect — the transcriber can
misspell an archaic word it knows the sound of. Judge by SOUND, not spelling: if it heard
"for-SAY-keth" as "forsaketh" that is a PASS; if it heard "for Saccath" that is a FAIL.
"""
import argparse
import asyncio
import glob
import os
import re
import subprocess
import sys
import tempfile

# SPEAKER LAW, locked by Cameron 2026-07-18. This table was left on the old
# pre-speaker-law voices (Christopher for all three), so a --text spot check was
# testing a voice no video actually uses. mbm_speakers is the real source; this
# mirrors it for the standalone --text path.
VOICES = {
    "narrator": "en-US-AndrewNeural",
    "jesus": "en-US-EricNeural",
    "god": "en-US-ChristopherNeural",
    "scripture": "en-US-SteffanNeural",
    "woman": "en-US-MichelleNeural",
}
RATES = {"narrator": ("-20%", "-4Hz"), "jesus": ("-22%", "-3Hz"),
         "god": ("-25%", "-12Hz"), "scripture": ("-18%", "-9Hz"),
         "woman": ("-20%", "-2Hz")}


def norm(s):
    return re.sub(r"[^a-z ]", "", s.lower()).split()


async def say(text, voice, rate, pitch, out):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(out)


_model = None


def transcribe(path):
    global _model
    from faster_whisper import WhisperModel
    if _model is None:
        _model = WhisperModel("base.en", device="cpu", compute_type="int8")
    segs, _ = _model.transcribe(path, beam_size=1)
    return " ".join(s.text for s in segs).strip()


# The transcriber spells archaic words in modern form even when the AUDIO is correct.
# These pairs sound right and must not be reported as defects.
KNOWN_GOOD = {
    ("sheweth", "showeth"), ("shew", "show"), ("shewed", "showed"),
    ("peradventure", "per adventure"), ("saith", "sayeth"), ("holpen", "holpin"),
    ("durst", "derst"), ("spake", "spoke"), ("brethren", "brethren"),
    ("thine", "thy"), ("ye", "you"), ("unto", "into"),
}


def phon(w):
    """Crude consonant skeleton — collapses spelling variants that sound alike."""
    w = re.sub(r"[^a-z]", "", w.lower())
    w = w.replace("ph", "f").replace("ew", "ow").replace("wh", "w")
    w = re.sub(r"[aeiou]+", "", w)
    return re.sub(r"(.)\1+", r"\1", w)


def similarity(a, b):
    import difflib
    return difflib.SequenceMatcher(a=phon(a), b=phon(b)).ratio()


def compare(caption, heard):
    """Word-level diff. Returns (caption_words, heard_words, sound_similarity).

    IMPORTANT: similarity is a RANKING aid, not a verdict. High similarity usually means
    the audio was fine and only the spelling differs; low similarity usually means a real
    misread. A human ear settles it.
    """
    import difflib
    a, b = norm(caption), norm(heard)
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b).get_opcodes():
        if tag == "equal":
            continue
        cw, hw = " ".join(a[i1:i2]) or "-", " ".join(b[j1:j2]) or "-"
        if (cw, hw) in KNOWN_GOOD:
            continue
        out.append((cw, hw, similarity(cw, hw)))
    return out


def check_line(caption, spoken, voice, rate="-20%", pitch="-4Hz", label=""):
    """caption = what the viewer reads; spoken = what we feed the TTS."""
    with tempfile.TemporaryDirectory() as td:
        mp3 = os.path.join(td, "a.mp3")
        asyncio.run(say(spoken or caption, voice, rate, pitch, mp3))
        heard = transcribe(mp3)
    diffs = compare(caption, heard)
    likely_bad = [d for d in diffs if d[2] < 0.75]
    tag = "OK   " if not diffs else ("BAD  " if likely_bad else "minor")
    print(f"[{tag}] {label}")
    print(f"    caption: {caption[:110]}")
    if spoken and spoken != caption:
        print(f"    spoken : {spoken[:110]}")
    print(f"    heard  : {heard[:110]}")
    for c, h, s in diffs:
        mark = "!!" if s < 0.75 else " ~"
        print(f"     {mark} '{c}' -> heard '{h}'   (sound match {s:.0%})")
    return likely_bad


def check_build(bdir):
    sys.path.insert(0, bdir)
    cwd = os.getcwd()
    os.chdir(bdir)
    try:
        import importlib
        mn = importlib.import_module("make_narration")
        importlib.reload(mn)
        SPOKEN = getattr(mn, "SPOKEN", {}) or {}
        bad = 0
        for seg in mn.SEGMENTS:
            # SPEAKER-LAW rewrote every build to (name, speaker, text); the voice
            # is now derived from the speaker instead of spelled out per segment.
            # The old 5-tuple form (name, voice, rate, pitch, text) still exists in
            # builds that were never migrated, so both are read here.
            if len(seg) >= 5:
                name, voice, rate, pitch, text = seg[0], seg[1], seg[2], seg[3], seg[4]
                speaker = None
            else:
                name, speaker, text = seg[0], seg[1], seg[2]
                import mbm_speakers
                voice, rate, pitch = mbm_speakers.voice_of(speaker)
            # Test EXACTLY what the pipeline renders. The old code substituted
            # only the build's SPOKEN dict and skipped spoken_text() entirely —
            # no global SAY, no per-voice fixes, no paren-drop — so the sweep
            # flagged "defects" (zevidie, crunch, winky face) that were not in
            # the shipped audio at all (caught 2026-07-20).
            import mbm_pronounce
            spoken = mbm_pronounce.spoken_text(text, SPOKEN, speaker)
            if check_line(text, spoken, voice, rate, pitch, label=f"{os.path.basename(bdir)}/{name}"):
                bad += 1
        print(f"\n{bad} segment(s) need an ear-check in {os.path.basename(bdir)}")
    finally:
        os.chdir(cwd)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--text")
    p.add_argument("--spoken")
    p.add_argument("--voice", default=VOICES["scripture"])
    p.add_argument("--rate", default="-20%")
    p.add_argument("--pitch", default="-4Hz")
    p.add_argument("--build")
    a = p.parse_args()
    if a.build:
        d = a.build if os.path.isabs(a.build) else os.path.join(
            "/home/noremacttevol/Desktop/MBM/media-production", a.build)
        check_build(d)
    elif a.text:
        check_line(a.text, a.spoken, a.voice, a.rate, a.pitch, label="line")
    else:
        p.error("give --text or --build")
