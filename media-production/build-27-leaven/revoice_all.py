#!/usr/bin/env python3
"""Re-voice EVERY row-27 segment to kill Cameron's 4th "washy/reverb" complaint.

WHY (QC.md §RUNNER PARK REVERB, measured + spectrogram-viewed): row 27's shipped
audio is the V1 ElevenLabs source segs (AUDIO_FROM_V1_SEGMENTS=True). That render
came out genuinely DULL/WASHY — HF cutoff + haze filling the inter-word gaps —
unlike the crisp full-band approved rows 50/70/97 (ALSO ElevenLabs, so it is a
bad-render artefact, not an engine difference). The de-muffle EQ was the WRONG
fix: with no crisp consonant detail in the source to lift, the high-shelf only
amplified the room-floor hiss (+6 dB in the gaps) — that added air IS the
"reverb" Cameron now hears. You cannot EQ detail into a source that never had it.

THE FIX: a FRESH ElevenLabs render of every segment through the SAME locked cast
that produced the crisp approved rows — Brian narrator / Chris Jesus / Roger
scripture (build-LOCAL mbm_eleven.py; the shared copy has a stale Alexander Jesus
and must NOT be used). Each fresh seg is pitch-preserving atempo-matched back to
its ORIGINAL duration so NO downstream still/caption window in beats_v2.py moves —
the timeline stays structurally identical, only the audio content is replaced.

Reproduce:  cd media-production/build-27-leaven && python3 revoice_all.py
"""
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MP = os.path.abspath(os.path.join(HERE, ".."))          # media-production/ (for mbm_speakers)
sys.path.insert(0, MP)

# Load the BUILD-LOCAL driver explicitly by path (Chris Jesus / Brian / Roger).
_spec = importlib.util.spec_from_file_location(
    "mbm_eleven_local", os.path.join(HERE, "mbm_eleven.py"))
e = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(e)
from mbm_speakers import NARRATOR, JESUS, SCRIPTURE

assert e.VOICE_ELEVEN[JESUS][0] == "Chris", e.VOICE_ELEVEN[JESUS]
assert e.VOICE_ELEVEN[NARRATOR][0] == "Brian", e.VOICE_ELEVEN[NARRATOR]
assert e.VOICE_ELEVEN[SCRIPTURE][0] == "Roger", e.VOICE_ELEVEN[SCRIPTURE]

# Authoritative per-segment text = make_narration.py SEGMENTS (caption source too).
SEGMENTS = [
    ("n1",  NARRATOR,  "Watch the small and ordinary thing a woman does every week, in her own kitchen, with her own hands."),
    ("s33", SCRIPTURE, "Another parable spake he unto them;"),
    ("j1",  JESUS,     "The kingdom of heaven is like unto leaven, which a woman took, and hid in three measures of meal, till the whole was leavened."),
    ("n2",  NARRATOR,  "Leaven is just a little piece of old, living dough, what we would call a sourdough starter. Small. Plain. Easy to overlook."),
    ("n3",  NARRATOR,  "And three measures of meal is not a small bowl. It is an enormous amount of flour, enough bread to feed a hundred people."),
    ("n4",  NARRATOR,  "She takes that tiny bit of leaven and works it down deep into the whole mass, hiding it, until you cannot even see where it went."),
    ("n5",  NARRATOR,  "Then she covers it and waits. Nothing looks like it is happening. No noise, no show, no spectacle. Just quiet, hidden time."),
    ("n6",  NARRATOR,  "But inside, the leaven is spreading through every part of the dough. And by morning the whole heavy mass has risen, alive, changed all the way through."),
    ("n7",  NARRATOR,  "That, Jesus said, is how the kingdom of God works. Not by force. Not by noise. It starts small and hidden, and it quietly changes everything it touches, from the inside out."),
    ("n8",  NARRATOR,  "That is how good he is. He does not overpower you. He works gently, patiently, from within, until the whole of you is warmed and changed and made into something that can feed other people."),
    ("card", NARRATOR, "God is often working quietest right where you cannot see it yet. Where might he already be at work inside you?"),
]


def key():
    for _ in range(4):
        f = [x for x in os.listdir(MP) if re.match(r"elevenlabs.*KEY.*\.txt", x, re.I)]
        if f:
            m = re.search(r"sk_[A-Za-z0-9]+", open(os.path.join(MP, f[0])).read())
            if not m:
                raise RuntimeError("no sk_ token in key file")
            return m.group(0)
    raise RuntimeError("no ElevenLabs key file found")


def dur(path):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip())


def main():
    k = key()
    audio = os.path.join(HERE, "audio")
    backup = os.path.join(audio, ".pre-revoice-backup")
    os.makedirs(backup, exist_ok=True)

    # Back up EVERY current source before touching anything (durable, reversible).
    for f in os.listdir(audio):
        if f.endswith((".mp3", ".timing.json")):
            src = os.path.join(audio, f)
            if os.path.isfile(src) and not os.path.exists(os.path.join(backup, f)):
                shutil.copy2(src, os.path.join(backup, f))
    print(f"backed up current sources -> {backup}\n")

    report = []
    for name, speaker, text in SEGMENTS:
        final = os.path.join(audio, f"{name}.mp3")
        orig_dur = dur(os.path.join(backup, f"{name}.mp3"))

        spoken = e.eleven_spoken_text(text)
        raw = os.path.join(audio, f"{name}.raw.mp3")
        e.render_segment(spoken, speaker, raw, key=k)   # writes raw + raw.timing.json

        new_dur = dur(raw)
        tempo = new_dur / orig_dur                        # >1 speeds up toward orig
        if not (0.80 <= tempo <= 1.25):
            raise SystemExit(f"{name}: atempo {tempo:.3f} outside safe band "
                             f"(new {new_dur:.2f}s vs orig {orig_dur:.2f}s) — investigate")

        subprocess.run(
            ["ffmpeg", "-y", "-i", raw, "-filter:a", f"atempo={tempo:.6f}",
             "-c:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", final],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Rescale the timing sidecar by 1/tempo so caption/red-letter windows land.
        rawt = os.path.join(audio, f"{name}.raw.timing.json")
        if os.path.exists(rawt):
            sents = json.load(open(rawt))
            for s in sents:
                s["start"] = round(s["start"] / tempo, 3)
                s["end"] = round(s["end"] / tempo, 3)
            json.dump(sents, open(os.path.join(audio, f"{name}.timing.json"), "w"))
            os.remove(rawt)
        os.remove(raw)

        got = dur(final)
        report.append((name, speaker, orig_dur, new_dur, tempo, got))
        print(f"{name:<5} {speaker:<9} orig {orig_dur:6.3f}s  raw {new_dur:6.3f}s  "
              f"atempo {tempo:.4f}  ->  final {got:6.3f}s  (delta {got-orig_dur:+.3f}s)")

    worst = max(abs(g - o) for _, _, o, _, _, g in report)
    print(f"\nALL {len(report)} segments re-voiced. worst duration delta {worst:+.3f}s")
    if worst > 0.05:
        print("WARNING: a duration delta exceeds 50ms — check before assembling.")


if __name__ == "__main__":
    main()
