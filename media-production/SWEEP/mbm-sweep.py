#!/usr/bin/env python3
"""
MBM Quality Sweep: Scan all 200 videos for mechanical defects
Runs locally, zero AI credits, no paid APIs.

Outputs:
  defects.json - all findings organized by type
  defects-summary.txt - human-readable list
"""

import os
import json
import subprocess
import re
from pathlib import Path

BASE_DIR = Path("/home/noremacttevol/Desktop/MBM/media-production")
BUILD_DIR = BASE_DIR / "media-production"
OUTPUT_DIR = BASE_DIR / "SWEEP" / "sweep-results"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Colors (hex) for caption law
JESUS_RED = "#DC3535"
SCRIPTURE_BLUE = "#8FDCFF"
WOMEN_PINK = "#FF8F8F"
FATHER_GREEN = "#3D9970"
NARRATOR_WHITE = "#FFFFFF"

def run_cmd(cmd, desc=""):
    """Run shell command, return stdout"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=120)
        if result.returncode != 0 and desc:
            print(f"⚠️  {desc} failed: {result.stderr[:200]}")
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        print(f"⏱️  Timeout: {cmd[:100]}...")
        return "", ""

def get_build_folders():
    """List all build-*/ folders"""
    builds = []
    for item in BASE_DIR.iterdir():
        if item.is_dir() and item.name.startswith("build-"):
            mp4_candidate = item / f"{item.name.split('-')[1:]}_{item.name.split('_')[1]}.mp4" if '_' in item.name else None
            # Simpler: find any .mp4 in build-*
            mp4s = list(item.glob("*.mp4"))
            if mp4s:
                builds.append((item, mp4s[0]))
    return builds

def check_silence_gaps(mp4_path, build_name):
    """Check for silence > 2.5s in video"""
    # Use silent detection via ffmpeg afade
    cmd = f"ffprobe -v error -select_streams a:0 -show_entries frame=pts_time,key_val -of json {mp4_path}"
    out, err = run_cmd(cmd)
    if not out:
        return []
    
    # Simpler approach: use areverse+sliceremove to detect silence
    # For now, report if video exists
    return []

def check_lufts(mp4_path, build_name):
    """Check audio loudness via loudnorm"""
    cmd = f"ffprobe -v error -show_entries stream=codec_type -select_streams a:0 {mp4_path}"
    # Use loudnorm filter to measure
    cmd2 = f"ffmpeg -i {mp4_path} -af loudnorm=I=-15:TP=-1:LRA=11:print_format=summary -f null - 2>&1 | grep -i 'integrated'\n"
    out, err = run_cmd(f"ffmpeg -i {mp4_path} -af loudnorm=I=-15:TP=-1:LRA=11:print_format=json -f null - 2>&1", "")
    try:
        data = json.loads(out)
        # loudnorm returns metadata, not direct value
        # For now, skip detailed loudness check
        return None  # Not implemented in free check
    except:
        return None

def check_video_ends_before_audio(mp4_path, build_name):
    """Check if video track is shorter than audio track"""
    cmd = f"ffprobe -v error -show_entries format=duration -of csv=p=0 {mp4_path}"
    out, _ = run_cmd(cmd)
    dur = float(out.strip()) if out.strip() else 0
    
    # Get video and audio track durations
    v_cmd = f"ffprobe -v error -select_streams v:0 -show_entries format=duration -of csv=p=0 {mp4_path}"
    a_cmd = f"ffprobe -v error -select_streams a:0 -show_entries format=duration -of csv=p=0 {mp4_path}"
    v_dur_out, _ = run_cmd(v_cmd)
    a_dur_out, _ = run_cmd(a_cmd)
    
    v_dur = float(v_dur_out.strip()) if v_dur_out.strip() else dur
    a_dur = float(a_dur_out.strip()) if a_dur_out.strip() else dur
    
    if a_dur > v_dur + 0.5:  # More than 0.5s difference
        return {"video_dur": v_dur, "audio_dur": a_dur, "diff": a_dur - v_dur}
    return None

def check_prompts_md(build_path, build_name):
    """Check PROMPTS.md for violations"""
    problems = []
    prompts_file = build_path / "PROMPTS.md"
    if not prompts_file.exists():
        return problems
    
    with open(prompts_file) as f:
        content = f.read()
    
    content_lower = content.lower()
    
    # Check 1: FACE LAW v3 (2026-07-15) — Jesus face SHOULD BE SHOWN
    # OUTDATED: "face never shown" / "face is never shown" = VIOLATION (old law)
    # Videos need: "FACE LAW v3: Jesus's face IS SHOWN"
    has_outdated_face_hide = (
        ("face never shown" in content_lower) or
        ("face is never shown" in content_lower) or
        ("face withheld" in content_lower) or
        ("mystery figure" in content_lower)
    )
    
    if has_outdated_face_hide:
        problems.append("FACE-LAW-OUTDATED: Still using old 'face never shown' — should show Jesus face per FACE LAW v3 (2026-07-15)")
    
    # Check 2: Missing character ref attachments
    # Look for character names but no --ref attachments
    has_character_desc = any(name.lower() in content.lower() for name in ["jesus", "martha", "mary", "lazarus", "god", "father"])
    has_ref_attachments = "--ref" in content or "ref-image" in content.lower()
    
    if has_character_desc and not has_ref_attachments:
        problems.append("CHARACTER-REF-MISSING: Characters described but no --ref image attachments (faces/clothes will drift)")
    
    # Check 3: No glow/halo
    if "no glow" in content.lower() or "no halo" in content.lower():
        # This is actually CORRECT per law, don't flag
        pass
    
    return problems

def check_caption_colors(mp4_path, build_name):
    """Grab frames during caption times, check for correct colors"""
    # This requires caption timing info (SRT or .sub files)
    # For now, skip detailed color analysis
    return []

def check_homograph_words(build_path, build_name):
    """Check for known homograph words that TTS mispronounces"""
    problems = []
    homographs = [
        ("live", "lives", "because he lvs"),  # lives should be LYVZ
        ("liveth", "livith"),
        ("calleth", "call-eth"),
        ("oweth", "o-weth"),
        ("messias", "mess-ias"),
    ]
    
    # Check make_narration.py or prompt files for these words
    narration_file = build_path / "make_narration.py"
    if narration_file.exists():
        with open(narration_file) as f:
            content = f.read()
        
        for word_pair in homographs:
            if any(word.lower() in content.lower() for word in word_pair):
                problems.append(f"HOMOGRAPH-WARNING: Found '{word_pair[0]}' - check pronunciation")
    
    return problems

def main():
    print("🔍 Starting MBM Quality Sweep...")
    print(f"Base: {BASE_DIR}")
    print()
    
    builds = get_build_folders()
    if not builds:
        print("❌ No build folders found")
        return
    
    print(f"📁 Found {len(builds)} build folders")
    
    defects = {
        "silence_gaps": [],
        "video_audio_mismatch": [],
        "prompts_violations": [],
        "homograph_warnings": [],
        "character_ref_missing": [],
    }
    
    for build_path, mp4_path in builds:
        build_name = build_path.name
        print(f"🏗️  Checking {build_name}...")
        
        # Check video/audio duration mismatch
        vae = check_video_ends_before_audio(mp4_path, build_name)
        if vae:
            defects["video_audio_mismatch"].append({
                "build": build_name,
                "details": vae,
                "fix": "Extend video track to match audio duration"
            })
        
        # Check PROMPTS.md
        prompt_issues = check_prompts_md(build_path, build_name)
        if prompt_issues:
            for issue in prompt_issues:
                if "FACE-LAW" in issue:
                    defects["prompts_violations"].append({"build": build_name, "issue": issue})
                elif "CHARACTER-REF" in issue:
                    defects["character_ref_missing"].append({"build": build_name, "issue": issue})
        
        # Check homograph words
        homograph_warnings = check_homograph_words(build_path, build_name)
        if homograph_warnings:
            for warning in homograph_warnings:
                defects["homograph_warnings"].append({"build": build_name, "warning": warning})
    
    # Write results
    output_file = OUTPUT_DIR / "defects.json"
    with open(output_file, 'w') as f:
        json.dump(defects, f, indent=2)
    print(f"\n✅ Results saved to {output_file}")
    
    # Summary
    summary_file = OUTPUT_DIR / "defects-summary.txt"
    with open(summary_file, 'w') as f:
        f.write("=" * 60 + "\n")
        f.write("MBM QUALITY SWEEP SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        
        def write_section(title, items):
            if items:
                f.write(f"\n🔴 {title} ({len(items)})\n")
                f.write("-" * 40 + "\n")
                for item in items:
                    f.write(f"  • {item.get('build', 'UNKNOWN')}")
                    if 'issue' in item:
                        f.write(f": {item['issue']}")
                    elif 'warning' in item:
                        f.write(f": {item['warning']}")
                    elif 'details' in item:
                        f.write(f": {item['details']}")
                    f.write("\n")
            else:
                f.write(f"✅ {title}: None found\n")
        
        write_section("PROMPTS MD VIOLATIONS (Jesus face hidden)", defects["prompts_violations"])
        write_section("CHARACTER REF MISSING (faces will drift)", defects["character_ref_missing"])
        write_section("HOMOGRAPH WORDS (listen & verify)", defects["homograph_warnings"])
        write_section("VIDEO/AUDIO DURATION MISMATCH", defects["video_audio_mismatch"])
        
        f.write("\n" + "=" * 60 + "\n")
        f.write(f"Total builds scanned: {len(builds)}\n")
        f.write(f"Total defects found: {sum(len(v) for v in defects.values())}\n")
        f.write("=" * 60 + "\n")
    
    print(f"📝 Summary saved to {summary_file}")
    
    # Print quick counts
    print(f"\n📊 DEFECT COUNTS:")
    print(f"  • Jesus face hidden: {len(defects['prompts_violations'])}")
    print(f"  • Character refs missing: {len(defects['character_ref_missing'])}")
    print(f"  • Homograph warnings: {len(defects['homograph_warnings'])}")
    print(f"  • Video/audio mismatch: {len(defects['video_audio_mismatch'])}")

if __name__ == "__main__":
    main()
