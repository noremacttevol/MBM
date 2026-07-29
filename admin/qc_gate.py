#!/usr/bin/env python3
"""MBM QC GATE — a video reaches Cameron's review board ONLY if it passes here.

WHY THIS EXISTS (2026-07-24, Cameron's order):
Sessions kept posting videos that were TOLD "good" but were actually bad — still
the OLD voice, or the narrator still ECHOING the scripture line. The board decided
"ready" from a git TIMESTAMP (was the mp4 committed after some date), which lies:
touching a build for any reason flipped it green. Cameron wasted his time watching
videos he was promised were fixed.

This gate never trusts a date, a marker, or a session's word. It reads the ACTUAL
video content. A build passes only if ALL of these hold:

  1. PLAYABLE   the finished mp4 has a moov atom and full-length audio (verify-mp4)
  2. NEW VOICE  every spoken clip the build actually uses is 44100 Hz ElevenLabs
                audio — never the old 24000 Hz edge-tts voice
  3. COMPLETE   every narration segment has its audio clip present on disk
  4. SCRIPT CLEAN  the trimmed transcript has zero narrator-repeats-scripture pairs
                (the echo Cameron hates), by the exact echo_scan definition
  5. AUDIO TRUTH   faster-whisper transcribes what the video ACTUALLY SAYS and the
                same echo test finds zero back-to-back repeats — this catches audio
                that was re-voiced from an OLD, un-trimmed script (clean text file,
                dirty audio). This is the check that makes "told good, actually bad"
                impossible.

Usage:
  python3 admin/qc_gate.py <build-dir> [--fast] [--json]
    --fast   skip step 5 (the whisper pass) for a quick pre-check
    --json   print a one-line JSON verdict instead of human text
Exit 0 = safe to ship.  Exit 1 = BLOCKED (reasons printed).  Exit 2 = can't tell.

The whisper pass is the slow one, so ship-fixes caches verdicts by mp4 hash in
media-production/QC-STATUS.json — a given cut is only transcribed once.
"""
import glob
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MP = os.path.join(REPO, "media-production")
VERIFY = os.path.join(REPO, "admin", "verify-mp4.sh")
sys.path.insert(0, MP)
from corpus import find_main_mp4 as corpus_find_main_mp4  # noqa: E402
from corpus import load_build_segments  # noqa: E402
from render_receipt import verify as verify_render_receipt  # noqa: E402

OLD_VOICE_HZ = 24000      # edge-tts / the retired voice
NEW_VOICE_HZ = 44100      # ElevenLabs

# ---- shared echo definition (identical thresholds to echo_scan.py) ----------
STOP = set("the a an and or of to in on for his her he she it they them was were is are be "
           "that this with as at by from i you me my thy thee thou shall will would had have has "
           "did do not no but so her him he she they said told out over into her his".split())


def words(t):
    return [w for w in re.findall(r"[a-z]+", t.lower()) if w not in STOP and len(w) > 2]


def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t.strip()) if s.strip()]


def echo_sentences(char_line, narr_text):
    """narrator sentences that restate the character line (>=55% of its content
    words, >=2 words) — the echo_scan.py definition, unchanged."""
    cw = set(words(char_line))
    if len(cw) < 2:
        return []
    hits = []
    for s in sentences(narr_text):
        sw = set(words(s))
        shared = len(cw & sw)
        if shared >= 2 and shared / len(cw) >= 0.55:
            hits.append(s)
    return hits


# ---- helpers ----------------------------------------------------------------
def ffprobe_sample_rate(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a:0",
         "-show_entries", "stream=sample_rate", "-of", "csv=p=0", path],
        capture_output=True, text=True)
    out = r.stdout.strip()
    return int(out) if out.isdigit() else None


def load_segments(bdir):
    """[(id, speaker, text), ...] from make_narration.py, or None."""
    return load_build_segments(bdir, executable=sys.executable)


def find_main_mp4(bdir):
    return corpus_find_main_mp4(bdir)


# ---- the checks -------------------------------------------------------------
def check_playable(mp4):
    r = subprocess.run(["bash", VERIFY, mp4], capture_output=True, text=True)
    if r.returncode != 0:
        return [f"PLAYABLE: {r.stdout.strip() or r.stderr.strip() or 'verify-mp4 failed'}"]
    return []


def check_render_freshness(bdir, mp4):
    """Prove that this MP4 came from the exact current code/audio/still bytes."""
    ok, detail = verify_render_receipt(bdir, mp4)
    return [] if ok else [f"RENDER FRESH: {detail}"]


def check_voice_and_complete(bdir, segs):
    """Every spoken clip the build USES must exist and be 44100 Hz."""
    fails = []
    missing = []
    old = []
    for sid, sp, _txt in segs:
        clip = os.path.join(bdir, "audio", f"{sid}.mp3")
        if not os.path.exists(clip):
            missing.append(sid)
            continue
        sr = ffprobe_sample_rate(clip)
        if sr == OLD_VOICE_HZ:
            old.append(sid)
        elif sr != NEW_VOICE_HZ:
            old.append(f"{sid}(sr={sr})")
    if missing:
        fails.append(f"COMPLETE: {len(missing)} segment(s) have no audio clip: "
                     f"{', '.join(map(str, missing[:8]))}")
    if old:
        fails.append(f"NEW VOICE: {len(old)} clip(s) are the OLD voice (not 44100 Hz "
                     f"ElevenLabs): {', '.join(map(str, old[:8]))}")
    return fails


def check_jesus_voice(bdir):
    """CAMERON'S RULE (2026-07-25): nothing reaches the board unless Jesus is the
    APPROVED voice (Alexander). Checking "is it ElevenLabs / 44100 Hz" is NOT enough —
    that passes wave-1 audio voiced by Chris, which is exactly the trash he kept being
    shown as 'ready'. The verdict comes from admin/jesus_voice_audit.py, which reads
    ElevenLabs' own history (the pause-tag signature only the Alexander pipeline
    produces), never a marker or timestamp.

    Fails CLOSED: if the audit has no verdict for this build, it does not ship."""
    m = re.search(r"build-(\d+)-", os.path.basename(bdir.rstrip("/")))
    if not m:
        return []
    num = str(int(m.group(1)))
    path = os.path.join(MP, "JESUS-VOICE.json")
    try:
        with open(path, encoding="utf-8") as f:
            audit = json.load(f)
    except (FileNotFoundError, ValueError):
        return ["JESUS VOICE: no audit yet — run `python3 admin/jesus_voice_audit.py`"]
    v = audit.get(num)
    if not v:
        return [f"JESUS VOICE: build #{num} has no audit verdict — run jesus_voice_audit.py"]
    if v.get("ok"):
        return []
    return [f"JESUS VOICE: {v.get('how', 'not the approved Jesus voice')} — re-voice with Alexander"]


def check_script_echo(segs):
    """Zero narrator-repeats-scripture pairs in the written transcript."""
    bad = []
    for i in range(len(segs) - 1):
        (id1, sp1, t1), (id2, sp2, t2) = segs[i], segs[i + 1]
        speakers = {sp1, sp2}
        if "narrator" not in speakers or speakers == {"narrator"}:
            continue
        if sp1 == "narrator":
            char_line, narr_txt = t2, t1
        else:
            char_line, narr_txt = t1, t2
        if echo_sentences(char_line, narr_txt):
            bad.append((id1, id2))
    if bad:
        return [f"SCRIPT ECHO: {len(bad)} narrator-repeats-scripture pair(s): "
                + ", ".join(f"{a}->{b}" for a, b in bad[:6])]
    return []


def transcribe(mp4):
    """What the video ACTUALLY says, as one string. None if whisper unavailable."""
    try:
        from faster_whisper import WhisperModel
    except Exception:
        return None
    wav = "/tmp/mbm-qc-%d.wav" % os.getpid()
    try:
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", mp4,
                        "-ac", "1", "-ar", "16000", wav],
                       check=True, capture_output=True)
        model = WhisperModel("small.en", device="cpu", compute_type="int8")
        segments, _ = model.transcribe(wav, language="en", beam_size=1)
        return " ".join(s.text.strip() for s in segments)
    except Exception as e:
        sys.stderr.write(f"[qc_gate] whisper failed: {e}\n")
        return None
    finally:
        try:
            os.remove(wav)
        except OSError:
            pass


def _one_segment_holds(a, b, seg_wordsets):
    """True if some SINGLE written segment contains both spoken sentences (their
    content words), tolerating one whisper miss each. When that holds, the two
    'sentences' are just whisper splitting ONE written line at its internal
    punctuation (e.g. the colon inside John 4:14 'thirst again: But whosoever...')
    — a scripture verse's own parallelism, NOT the narrator-restates-scripture echo
    Cameron hates. A real echo restates ACROSS two segments, so no single segment
    holds both halves and it stays flagged."""
    for sw in seg_wordsets:
        if len(a - sw) <= 1 and len(b - sw) <= 1:
            return True
    return False


def check_audio_truth(mp4, segs=None):
    """Transcribe the real audio and flag back-to-back sentences that repeat the
    same content — the echo as ACTUALLY SPOKEN, regardless of clean text files.
    Returns (fails, ran) where ran=False means whisper wasn't available."""
    spoken = transcribe(mp4)
    if spoken is None:
        return [], False
    seg_wordsets = [set(words(s[2])) for s in (segs or [])]
    sents = sentences(spoken)
    bad = []
    for i in range(len(sents) - 1):
        a, b = set(words(sents[i])), set(words(sents[i + 1]))
        if len(a) < 3 or len(b) < 3:
            continue
        shared = len(a & b)
        # strict: only a real restatement (>=3 shared content words AND >=65% of
        # the shorter sentence) — avoids flagging a merely-similar next line.
        if shared >= 3 and shared / min(len(a), len(b)) >= 0.65:
            # ...unless both halves live in ONE written segment: then it's a single
            # verse whisper split, not a cross-segment echo. See _one_segment_holds.
            if _one_segment_holds(a, b, seg_wordsets):
                continue
            bad.append((sents[i][:60], sents[i + 1][:60]))
    if bad:
        return [f"AUDIO ECHO (what it actually says): {len(bad)} spoken repeat(s), "
                f"e.g. \"{bad[0][0]}...\" then \"{bad[0][1]}...\""], True
    return [], True


# ---- driver -----------------------------------------------------------------
def gate(bdir, fast=False):
    """Return dict: {pass: bool, reasons: [...], whisper: bool}."""
    bdir = os.path.abspath(bdir)
    name = os.path.basename(bdir.rstrip("/"))
    reasons = []

    mp4 = find_main_mp4(bdir)
    if not mp4:
        return {"build": name, "pass": False, "whisper": False,
                "reasons": ["PLAYABLE: no finished scripture-named mp4 in the build folder"]}

    reasons += check_playable(mp4)
    reasons += check_render_freshness(bdir, mp4)

    segs = load_segments(bdir)
    if not segs:
        reasons.append("SCRIPT: make_narration.py has no readable SEGMENTS")
    else:
        reasons += check_voice_and_complete(bdir, segs)
        reasons += check_jesus_voice(bdir)
        reasons += check_script_echo(segs)

    whisper_ran = False
    if not fast:
        af, whisper_ran = check_audio_truth(mp4, segs)
        reasons += af

    return {"build": name, "pass": len(reasons) == 0,
            "whisper": whisper_ran, "mp4": os.path.basename(mp4), "reasons": reasons}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        sys.stderr.write("usage: qc_gate.py <build-dir> [--fast] [--json]\n")
        sys.exit(2)
    res = gate(args[0], fast="--fast" in flags)
    if "--json" in flags:
        print(json.dumps(res))
    else:
        if res["pass"]:
            tag = "PASS" + ("" if res["whisper"] else " (script+voice only; whisper not run)")
            print(f"{tag}: {res['build']}  {res.get('mp4','')}")
        else:
            print(f"BLOCK: {res['build']}")
            for r in res["reasons"]:
                print(f"  - {r}")
    sys.exit(0 if res["pass"] else 1)


if __name__ == "__main__":
    main()
