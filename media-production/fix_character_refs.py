#!/usr/bin/env python3
"""
Fix character refs in builds that failed character_ref_gate.py

For each build with missing character references:
1. Scan PROMPTS.md for named characters using CHARACTER-LAW roster
2. Inject "CHARACTER-NAME LOCK" markers with lock_text() into shot prompts
3. Output patched PROMPTS.md with proper character lock markers
"""

import os
import re
import sys
from pathlib import Path
import json

# Media production root
MEDIA_ROOT = Path.cwd()

# Add CHARACTERS to path to import character_refs
sys.path.insert(0, str(MEDIA_ROOT / "CHARACTERS"))

from character_refs import find_in_text, resolve, lock_text  # noqa: E402

# Pending sheets (SPEC written but sheet NOT rendered/approved)
PENDING_SHEETS = {
    'infant-jesus': 'SPEC written, sheet NOT rendered',
    'risen-jesus': 'SPEC written, sheet NOT rendered',
    'philip': 'SPEC written, sheet NOT rendered',
    'bartholomew': 'SPEC written, sheet NOT rendered', 
    'james-alphaeus': 'SPEC written, sheet NOT rendered',
    'thaddaeus': 'SPEC written, sheet NOT rendered',
    'simon-the-zealot': 'SPEC written, sheet NOT rendered',
    'aged-john': 'Age variant NOT rendered',
    'aged-peter': 'Age variant NOT rendered',
    'aged-abraham': 'Age variant NOT rendered',
    'youth-isaac': 'Age variant NOT rendered',
    'youth-jacob': 'Age variant NOT rendered',
    'glorified-moses': 'Age variant NOT rendered',
    'glorified-elijah': 'Age variant NOT rendered',
}

# Exempt pattern from character_ref_gate.py
EXEMPT_PATTERN = re.compile(r"CHARACTER-REF-EXEMPT:\s*([^\n(]+)", re.I)

def get_exempt_characters(text):
    """Extract exempt characters from PROMPTS.md"""
    exempt = set()
    for line in EXEMPT_PATTERN.findall(text):
        for name in line.replace(",", " ").split():
            try:
                exempt.add(resolve(name.lower().strip()))
            except KeyError:
                pass
    return exempt

def check_lock_present(text, slug):
    """Check if a character's LOCK marker is present in text"""
    marker = slug.replace("-", " ").upper() + " LOCK"
    alt = slug.split("-")[0].upper() + " LOCK"
    return marker in text.upper() or alt in text.upper()

def patch_prompts_md(build_dir):
    """Scan and patch PROMPTS.md for character lock markers"""
    prompts_file = build_dir / 'PROMPTS.md'
    if not prompts_file.exists():
        return None
    
    with open(prompts_file) as f:
        text = f.read()
    
    lines = text.split('\n')
    
    # Get all characters found in this build
    try:
        found = set(find_in_text(text))
    except Exception as e:
        print(f"  ⚠️ Error scanning: {e}")
        return None
    
    # Get exempt characters
    exempt = get_exempt_characters(text)
    
    # Get characters that need lock markers
    needs_lock = {c for c in found if c not in exempt}
    
    # Check which ones already have locks
    missing_locks = [c for c in needs_lock if not check_lock_present(text, c)]
    
    if not missing_locks:
        return None  # Already fixed
    
    # Build lock markers for each character
    lock_markers = {}
    pending_warnings = []
    
    for char_slug in missing_locks:
        try:
            # Check if pending
            if char_slug in PENDING_SHEETS:
                pending_warnings.append((char_slug, PENDING_SHEETS[char_slug]))
                continue
            
            # Get lock text
            lock_marker = char_slug.replace("-", " ").upper() + " LOCK"
            try:
                lock_text_content = lock_text(char_slug)
                lock_markers[char_slug] = {
                    'marker': lock_marker,
                    'text': lock_text_content
                }
            except Exception as e:
                print(f"    ⚠️ Cannot get lock_text for {char_slug}: {e}")
                continue
        except Exception as e:
            print(f"    ⚠️ Cannot resolve {char_slug}: {e}")
            continue
    
    # Now inject lock markers into shot prompts
    patched_lines = []
    shot_sections = []  # Track shot sections we modified
    
    # Pattern to detect shot headers
    shot_pattern = re.compile(r'^##\s+Shot\s+(\d+)\s+—', re.IGNORECASE)
    
    in_shot = False
    current_shot_idx = None
    
    for i, line in enumerate(lines):
        patched_lines.append(line)
        
        # Detect shot section
        shot_match = shot_pattern.match(line)
        if shot_match:
            in_shot = True
            current_shot_idx = shot_match.group(1)
            continue
        
        # End of shot section (next shot or major header)
        if in_shot and (line.startswith('### ') or line.startswith('---')):
            in_shot = False
            current_shot_idx = None
        
        # If we're in a shot and this line contains style block or prompt content,
        # inject lock markers before the prompt text
        if in_shot and current_shot_idx:
            # Look for the actual image prompt (contains "Beautiful hand-painted" or similar)
            if 'Beautiful hand-painted' in line or 'Flow image' in line:
                # Inject lock markers for this shot
                for char_slug, data in lock_markers.items():
                    if char_slug not in [c for c in shot_sections]:
                        # Insert lock marker before this line
                        lock_line = f"\n{data['marker']}: {data['text']}\n"
                        patched_lines.insert(-1, lock_line)
                        shot_sections.append(char_slug)
    
    # Add summary header
    summary = []
    summary.append('<!-- CHARACTERS REFERENCED IN THIS BUILD: -->\n')
    summary.append(f'<!-- Original missing locks: {", ".join(missing_locks)} -->\n')
    
    if lock_markers:
        summary.append('\nLock markers attached:\n')
        for char_slug, data in lock_markers.items():
            summary.append(f'  - {data["marker"]}\n')
    
    if pending_warnings:
        summary.append('\n⚠️ PENDING (BLOCKED until sheets rendered):\n')
        for char_slug, reason in pending_warnings:
            summary.append(f'  - {char_slug}: {reason}\n')
    
    # Replace original lines with patched version
    new_lines = summary + patched_lines
    new_content = '\n'.join(new_lines)
    
    # Write back
    if new_content != text:
        prompts_file.write_text(new_content)
        return {
            'chars_found': len(found),
            'exempt': len(exempt),
            'missing_locks': len(missing_locks),
            'locks_added': len(lock_markers),
            'pending_warnings': len(pending_warnings),
            'warnings': pending_warnings
        }
    
    return None

def main(builds_to_fix):
    """Fix character refs in specified builds"""
    results = {}
    
    print(f"=== Character Ref Auto-Fix ===")
    print(f"Processing {len(builds_to_fix)} builds...\n")
    
    for build_name in builds_to_fix:
        build_dir = MEDIA_ROOT / build_name
        
        if not build_dir.exists() or not build_dir.is_dir():
            print(f"⚠️ {build_name}: Not found (skipped)")
            continue
        
        if not (build_dir / 'PROMPTS.md').exists():
            print(f"⚠️ {build_name}: No PROMPTS.md (skipped)")
            continue
        
        print(f"📦 {build_name}...")
        result = patch_prompts_md(build_dir)
        
        if result:
            results[build_name] = result
            if result['locks_added'] > 0:
                if result['pending_warnings'] > 0:
                    print(f"  ✅ {result['locks_added']} locks added, but {result['pending_warnings']} pending sheets")
                else:
                    print(f"  ✅ {result['locks_added']} locks added")
            else:
                print(f"  ℹ️ No changes needed OR all pending")
        else:
            print(f"  ℹ️ Already has all lock markers")
    
    # Summary
    print(f"\n=== SUMMARY ===")
    print(f"Total builds processed: {len(builds_to_fix)}")
    print(f"Builds with changes: {len(results)}")
    
    total_locks_added = sum(r['locks_added'] for r in results.values())
    total_pending = sum(r['pending_warnings'] for r in results.values())
    
    print(f"Total lock markers added: {total_locks_added}")
    print(f"Total pending warnings: {total_pending}")
    
    if total_pending > 0:
        print(f"\n⚠️ {total_pending} builds have pending character sheets (BLOCKED)")
    
    return results

if __name__ == '__main__':
    # Default: the 38 builds that failed character_ref_gate.py
    default_builds = [
        'build-05-bent-woman',
        'build-103-peters-confession',
        'build-10-well',
        'build-110-lords-prayer',
        'build-111-lilies-and-sparrows',
        'build-117-hosea-buys-her-back',
        'build-118-jonah-god-who-relents',
        'build-119-fourth-man-in-fire',
        'build-120-job-from-whirlwind',
        'build-130-what-manner-of-spirit',
        'build-137-one-as-we-are-one',
        'build-144-resurrection-and-the-life',
        'build-149-hannah-is-heard',
        'build-154-everlasting-gospel',
        'build-160-stone-cut',
        'build-165-laying-on-hands',
        'build-166-baptized-properly',
        'build-169-fulfil-righteousness',
        'build-16-mary-martha',
        'build-174-hearts-of-the-fathers',
        'build-17-lazarus',
        'build-183-sun-moon-and-stars',
        'build-18-emmaus',
        'build-190-faith-without-works',
        'build-22-unmerciful-servant',
        'build-36-shrewd-steward',
        'build-37-rich-man-lazarus',
        'build-40-the-friend-at-midnight',
        'build-48-new-wine-old-bottles',
        'build-53-peters-mother-in-law',
        'build-57-jairus-daughter',
        'build-58-feeding-5000',
        'build-66-malchus-ear',
        'build-67-the-transfiguration',
        'build-67-transfiguration',
        'build-73-this-day-fulfilled',
        'build-82-anointing-at-bethany',
        'build-88-triumphal-entry',
        'build-91-gethsemane',
    ]
    
    if len(sys.argv) > 1:
        builds_to_fix = sys.argv[1:]
    else:
        builds_to_fix = default_builds
    
    main(builds_to_fix)
