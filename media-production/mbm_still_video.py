#!/usr/bin/env python3
"""Small, local-only assembler for MBM narration-over-stills videos.

Build folders provide the ordered beats and output name.  This module supplies
the same production guarantees as the established builds: real narration
timing, speaker-aware captions, restrained Ken Burns movement, intentional
silence only, loudness normalization, duration enforcement, and the 30 MB cap.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import textwrap


FPS = 30
FF = "ffmpeg"
FPROBE = "ffprobe"
ASSETS = "assets"
SEGS = "segs"
SERIF = "segs/serif.ttf"
SERIF_BI = "segs/serif_bi.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"
ENC = [
    "-c:v", "libx264", "-preset", "medium", "-crf", "16",
    "-pix_fmt", "yuv420p", "-r", str(FPS), "-an",
]


def _ensure_fonts() -> None:
    os.makedirs(SEGS, exist_ok=True)
    choices = {
        SERIF: [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
        ],
        SERIF_BI: [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf",
        ],
    }
    for destination, candidates in choices.items():
        if os.path.exists(destination):
            continue
        for source in candidates:
            if os.path.exists(source):
                shutil.copyfile(source, destination)
                break
        else:
            raise RuntimeError(f"font not found for {destination}")


def _run(command: list[str]) -> None:
    print(">>", " ".join(map(str, command))[:150], flush=True)
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(detail[-5000:] or f"command exited {result.returncode}")


def _duration(path: str) -> float:
    result = subprocess.run(
        [
            FPROBE, "-v", "error", "-show_entries", "format=duration",
            "-of", "csv=p=0", path,
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(result.stdout.strip())


def _spoken_duration(path: str) -> float:
    temporary = f"{SEGS}/_spoken.wav"
    _run([
        FF, "-y", "-v", "error", "-i", path, "-af",
        "areverse,silenceremove=start_periods=1:start_threshold=-50dB:"
        "start_duration=0.02,areverse",
        "-c:a", "pcm_s16le", temporary,
    ])
    return _duration(temporary)


def _build_still(
    segment: str,
    source: str,
    duration: float,
    zoom_direction: str,
    spoken_end: float,
    caption: str,
    speaker: str,
    first: bool,
) -> None:
    from mbm_caption_timing import caption_filter

    frames = max(1, int(duration * FPS))
    zoom = (
        f"1.001+0.09*on/{frames}"
        if zoom_direction == "in"
        else f"1.091-0.09*on/{frames}"
    )
    base = (
        "[0:v]scale=2160:3868,setsar=1,"
        f"zoompan=z='{zoom}':x='iw/2-(iw/zoom/2)':"
        f"y='ih/2-(ih/zoom/2)':d={frames}:s=2160x3840:fps={FPS},"
        "scale=1080:1920:flags=lanczos"
    )
    caption_layer = caption_filter(
        segment, duration, spoken_end, caption, speaker
    )
    opening = ",fade=t=in:st=0:d=1.0" if first else ""
    filters = f"{base}{caption_layer}{opening}[v]"
    _run([
        FF, "-y", "-loop", "1", "-i", f"{ASSETS}/{source}",
        "-t", f"{duration:.3f}", "-filter_complex", filters, "-map", "[v]",
        *ENC, f"{SEGS}/{segment}.mp4",
    ])


def _clean_card_text(text: str) -> str:
    translation = {
        0x2028: 0x20,
        0x2029: 0x20,
        0x0085: 0x20,
        0x000B: 0x20,
        0x000C: 0x20,
        0x000D: 0x20,
    }
    for codepoint in list(range(0x00, 0x09)) + list(range(0x0E, 0x20)):
        translation[codepoint] = None
    return text.translate(translation)


def _build_card(duration: float, text: str, pointer: str | None) -> None:
    text_file = f"{SEGS}/card.txt"
    with open(text_file, "w", encoding="utf-8") as handle:
        handle.write("\n".join(textwrap.wrap(_clean_card_text(text), width=30)))
    filters = (
        f"drawtext=fontfile={SERIF}:textfile={text_file}:fontsize=52:"
        f"fontcolor={INK}:line_spacing=24:x=(w-text_w)/2:"
        f"y=(h-text_h)/2-70"
    )
    if pointer:
        pointer_file = f"{SEGS}/card_pointer.txt"
        with open(pointer_file, "w", encoding="utf-8") as handle:
            handle.write(pointer)
        filters += (
            f",drawtext=fontfile={SERIF_BI}:textfile={pointer_file}:"
            f"fontsize=34:fontcolor={INK}:x=(w-text_w)/2:y=h*0.80"
        )
    filters += (
        f",fade=t=in:st=0:d=0.8,"
        f"fade=t=out:st={max(0.0, duration - 0.8):.3f}:d=0.8"
    )
    _run([
        FF, "-y", "-f", "lavfi",
        "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={duration:.3f}",
        "-vf", filters, *ENC, f"{SEGS}/card.mp4",
    ])


def render(
    *,
    output: str,
    beats: list[tuple[str, str, str]],
    text: dict[str, str],
    speaker: dict[str, str],
    pointer: str | None = None,
    hold: dict[str, float] | None = None,
    lead: float = 0.28,
    gap: float = 0.72,
    scripture_gap: float = 1.60,
    tail: float = 1.50,
    minimum_duration: float = 60.5,
) -> None:
    """Render one configured story video in the current build directory."""
    from mbm_speakers import is_scripture

    hold = hold or {}
    _ensure_fonts()
    missing = [
        path for path in (f"{ASSETS}/{asset}" for _, asset, _ in beats)
        if not os.path.isfile(path)
    ]
    missing += [
        path
        for path in (
            [f"audio/{segment}.mp3" for segment, _, _ in beats]
            + ["audio/card.mp3"]
        )
        if not os.path.isfile(path)
    ]
    if missing:
        raise RuntimeError("missing render input(s): " + ", ".join(missing))

    spoken = {
        segment: _spoken_duration(f"audio/{segment}.mp3")
        for segment, _, _ in beats
    }
    card_spoken = _spoken_duration("audio/card.mp3")

    timeline: list[tuple[str, str, str, float, float, str]] = []
    audio_placement: list[tuple[str, float]] = []
    cursor = 0.0
    for segment, still, direction in beats:
        segment_speaker = speaker[segment]
        silence = hold.get(
            segment,
            scripture_gap if is_scripture(segment_speaker) else gap,
        )
        video_duration = lead + spoken[segment] + silence
        audio_start = cursor + lead
        timeline.append(
            (
                segment,
                still,
                direction,
                video_duration,
                audio_start,
                segment_speaker,
            )
        )
        audio_placement.append((f"audio/{segment}.mp3", audio_start))
        cursor += video_duration

    card_duration = lead + card_spoken + tail
    card_start = cursor
    audio_placement.append(("audio/card.mp3", card_start + lead))
    total = card_start + card_duration
    if total < minimum_duration:
        raise RuntimeError(
            f"TOO SHORT: {total:.1f}s; must run at least {minimum_duration:.1f}s"
        )

    previous_end: float | None = None
    worst_gap = 0.0
    for segment, _, _, _, audio_start, _ in timeline:
        if previous_end is not None:
            worst_gap = max(worst_gap, audio_start - previous_end)
        previous_end = audio_start + spoken[segment]
    if previous_end is not None:
        worst_gap = max(worst_gap, card_start + lead - previous_end)
    if worst_gap > 2.5:
        raise RuntimeError(f"DEAD AIR: longest spoken gap is {worst_gap:.2f}s")
    print(
        f"total runtime: {total:.1f}s ({total / 60:.2f} min); "
        f"worst spoken gap: {worst_gap:.2f}s",
        flush=True,
    )

    for index, item in enumerate(timeline):
        segment, still, direction, duration, _, segment_speaker = item
        _build_still(
            segment,
            still,
            duration,
            direction,
            lead + spoken[segment],
            text[segment],
            segment_speaker,
            first=(index == 0),
        )
    _build_card(card_duration, text["card"], pointer)

    concat_file = f"{SEGS}/concat.txt"
    with open(concat_file, "w", encoding="utf-8") as handle:
        for segment, *_ in timeline:
            handle.write(f"file '{segment}.mp4'\n")
        handle.write("file 'card.mp4'\n")
    _run([
        FF, "-y", "-f", "concat", "-safe", "0", "-i", concat_file,
        "-c", "copy", f"{SEGS}/video_silent.mp4",
    ])

    inputs: list[str] = []
    filters: list[str] = []
    labels: list[str] = []
    for index, (path, start) in enumerate(audio_placement):
        inputs.extend(["-i", path])
        delay = int(start * 1000)
        filters.append(
            f"[{index}:a]aresample=44100,adelay={delay}|{delay},"
            f"volume=1.0[a{index}]"
        )
        labels.append(f"[a{index}]")
    filters.append(
        "".join(labels)
        + f"amix=inputs={len(labels)}:duration=longest:normalize=0,"
        + f"apad=whole_dur={total:.2f}[aout]"
    )
    _run([
        FF, "-y", *inputs, "-filter_complex", ";".join(filters),
        "-map", "[aout]", "-t", f"{total:.2f}", "-c:a", "aac",
        "-b:a", "160k", f"{SEGS}/audio_mix.m4a",
    ])

    loudness_probe = subprocess.run(
        [
            FF, "-i", f"{SEGS}/audio_mix.m4a", "-af", "ebur128",
            "-f", "null", "-",
        ],
        capture_output=True,
        text=True,
    )
    loudness: float | None = None
    for line in loudness_probe.stderr.splitlines():
        stripped = line.strip()
        if stripped.startswith("I:") and "LUFS" in stripped:
            loudness = float(stripped.split()[1])
    gain = (
        max(-6.0, min(16.0, -15.0 - loudness))
        if loudness is not None
        else 0.0
    )
    print(f"loudness: {loudness} LUFS; gain {gain:+.1f} dB", flush=True)

    audio_kbps = 96
    mux_kbps = 20
    video_cap = int(24.0 * 8000 / total) - audio_kbps - mux_kbps
    if video_cap < 400:
        raise RuntimeError(f"BITRATE STARVED: {video_cap} kbps")
    video_cap = min(video_cap, 2200)
    final_size = 0.0
    final_crf = 24
    for crf in (20, 21, 22, 23, 24):
        _run([
            FF, "-y", "-i", f"{SEGS}/video_silent.mp4",
            "-i", f"{SEGS}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
            "-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
            "-maxrate", f"{video_cap}k", "-bufsize", f"{video_cap * 2}k",
            "-pix_fmt", "yuv420p",
            "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
            "-c:a", "aac", "-b:a", f"{audio_kbps}k",
            "-movflags", "+faststart", output,
        ])
        final_size = os.path.getsize(output) / 1_000_000
        final_crf = crf
        if final_size <= 29.5:
            break
    if final_size > 29.5:
        raise RuntimeError(f"FILE TOO LARGE: {final_size:.1f} MB")
    print(
        f"DONE: {output} {final_size:.1f} MB, {total:.1f}s "
        f"(crf {final_crf}, cap {video_cap}k)",
        flush=True,
    )

