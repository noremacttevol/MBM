#!/usr/bin/env python3
"""Re-voice ONLY segment n0 to fix Cameron's complaint "You mispronounced Jesus's".

Row 18 (Road to Emmaus) narration is ElevenLabs ("Brian" narrator, VOICE_ELEVEN).
The shipped n0 said "two of Jesus' followers" — ElevenLabs dropped the possessive
"-iz" ending, so it read as "Jesus followers" (faster-whisper confirmed). The rest of
the video is ElevenLabs, so the ONLY correct fix is to re-render n0 through the SAME
ElevenLabs narrator (not edge-tts, which would swap the voice at the opening).

The possessive is respelled ONLY in the SPOKEN string ("Jesus's" -> "Jesuses"), which
ElevenLabs reads as /JEE-zus-iz/. The on-screen CAPTION is untouched: it comes from
make_narration.py SEGMENTS (extract_beats reads s[2]), which still says "Jesus's".

After rendering, n0 is pitch-preserving atempo-matched back to the original duration
(19.592 s) so NO downstream still-window in beats_v2.py has to move — the whole
timeline stays byte-for-byte structurally identical and every caption/picture window
that was already verified contiguous stays valid.

Reproduce:  python3 revoice_n0.py
"""
import glob
import json
import os
import re
import subprocess

import mbm_eleven as e
from mbm_speakers import NARRATOR

ORIG_DUR = 19.591837  # ffprobe duration of the original ElevenLabs n0.mp3


def eleven_key():
    """Pull ONLY the ElevenLabs sk_ token out of the shared key file, which now
    also carries an unrelated cloudflare token on other lines."""
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(4):
        f = glob.glob(os.path.join(d, "elevenlabs*KEY*.txt"))
        if f:
            m = re.search(r"sk_[A-Za-z0-9]+", open(f[0]).read())
            if not m:
                raise RuntimeError(f"no sk_ token in {f[0]}")
            return m.group(0)
        d = os.path.dirname(d)
    raise RuntimeError("no ElevenLabs key file found")

# The exact n0 caption text (make_narration.py SEGMENTS[0][2]).
CAPTION = ("It was the same Sunday. The tomb was empty, the rumors were flying, and "
           "two of Jesus's followers had given up and left. They were walking the "
           "seven miles from Jerusalem to a village called Emmaus, heads down, going "
           "over it all again — the arrest, the cross, the end of everything they "
           "had hoped for.")


def main():
    # Spoken string: apply the engine-agnostic phrase layer, then respell the
    # possessive so ElevenLabs voices the "-iz" ending. Caption stays "Jesus's".
    spoken = e.eleven_spoken_text(CAPTION).replace("Jesus's", "Jesuses")
    assert "Jesuses" in spoken and "Jesus's" not in spoken, spoken

    os.makedirs("audio", exist_ok=True)
    raw = "audio/n0.raw.mp3"
    e.render_segment(spoken, NARRATOR, raw, key=eleven_key())  # audio/n0.raw.mp3 + .timing.json

    new_dur = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", raw], capture_output=True, text=True).stdout.strip())
    tempo = new_dur / ORIG_DUR  # >1 speeds up to shrink back to ORIG_DUR
    print(f"new raw dur {new_dur:.3f}s  ->  atempo {tempo:.4f} -> target {ORIG_DUR:.3f}s")
    if not (0.8 <= tempo <= 1.25):
        raise SystemExit(f"atempo {tempo:.3f} outside safe band; investigate before shipping")

    subprocess.run(
        ["ffmpeg", "-y", "-i", raw, "-filter:a", f"atempo={tempo:.6f}",
         "-c:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", "audio/n0.mp3"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Rewrite n0.timing.json: scale the raw ElevenLabs times back by 1/tempo so the
    # per-sentence red-letter/caption windows land inside the atempo-matched audio.
    raw_timing = "audio/n0.raw.timing.json"
    if os.path.exists(raw_timing):
        sents = json.load(open(raw_timing))
        for s in sents:
            s["start"] = round(s["start"] / tempo, 3)
            s["end"] = round(s["end"] / tempo, 3)
        json.dump(sents, open("audio/n0.timing.json", "w"))
        os.remove(raw_timing)
    os.remove(raw)

    final = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", "audio/n0.mp3"], capture_output=True, text=True).stdout.strip())
    print(f"final n0.mp3 dur {final:.3f}s  (target {ORIG_DUR:.3f}s, delta {final-ORIG_DUR:+.3f}s)")


if __name__ == "__main__":
    main()
