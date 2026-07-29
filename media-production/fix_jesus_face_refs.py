#!/usr/bin/env python3
"""
Fix missing REF: jesus-master-ref markers and strip banned drift words
in builds failing jesus_face_gate.py

For each shot that depicts Jesus:
1. Inject JESUS LOCK v3 paragraph if missing
2. Inject REF: jesus-master-ref line if missing
3. Strip banned words: halo, rim-light, glow, glowing
"""

import re
import sys
from pathlib import Path

MEDIA_ROOT = Path.cwd()

JESUS_LOCK_V3 = """JESUS LOCK v3: the SAME man as the attached JESUS-MASTER-REF images — identical face, hair and beard in every picture: a Middle Eastern Jewish man of about thirty-three, warm tan olive-brown skin, shoulder-length dark brown-black wavy hair, a full dark beard, kind warm BROWN eyes, one plain undyed off-white cream wool robe (only he wears cream). No halo, no glow. Never caucasian, never pale, never blue-eyed, never blond."""

JESUS_REF = "REF: jesus-master-ref"

def strip_banned_words(text):
    """Remove banned drift words from text"""
    banned = [
        (r'\bhalo\b', ''),
        (r'\brim-light\b', ''),
        (r'\brim light\b', ''),
        (r'\bglow\b', ''),
        (r'\bglowing\b', ''),
    ]
    for pattern, replacement in banned:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

def shot_depicts_jesus(lines):
    """Check if a shot section includes Jesus visually"""
    section = '\n'.join(lines).lower()
    if 'jesus' in section or 'the guest' in section or 'the teacher' in section:
        return True
    if 'cream' in section and ('robe' in section or 'man' in section):
        return True
    return False

def has_jesus_lock(lines):
    return 'JESUS LOCK v3' in '\n'.join(lines)

def has_ref_marker(lines):
    return 'REF: jesus-master-ref' in '\n'.join(lines)

def process_shot(lines):
    """Process accumulated shot lines, inject Jesus lock/ref if needed"""
    if not lines:
        return lines, 0, 0, 0
    
    section_text = '\n'.join(lines)
    
    # Strip banned words first
    cleaned_lines = [strip_banned_words(line) for line in lines]
    words_stripped = sum(1 for i, orig in enumerate(lines) if orig != cleaned_lines[i])
    
    if not shot_depicts_jesus(cleaned_lines):
        return cleaned_lines, 0, 0, words_stripped
    
    missing_lock = not has_jesus_lock(cleaned_lines)
    missing_ref = not has_ref_marker(cleaned_lines)
    
    if not missing_lock and not missing_ref:
        return cleaned_lines, 0, 0, words_stripped
    
    result = []
    found_insert_point = False
    
    for line in cleaned_lines:
        result.append(line)
        if not found_insert_point and 'STYLE' in line.upper() and len(result) > 1:
            if missing_lock:
                result.append(JESUS_LOCK_V3)
            if missing_ref:
                result.append(JESUS_REF)
            found_insert_point = True
    
    added_lock = 1 if missing_lock else 0
    added_ref = 1 if missing_ref else 0
    return result, added_lock, added_ref, words_stripped

def patch_prompts_md(build_dir):
    """Inject JESUS LOCK v3 + REF marker into shots showing Jesus; strip banned words"""
    prompts_file = build_dir / 'PROMPTS.md'
    if not prompts_file.exists():
        return None
    
    with open(prompts_file) as f:
        lines = f.read().split('\n')
    
    patched = []
    total_lock_added = 0
    total_ref_added = 0
    total_words_stripped = 0
    
    shot_pattern = re.compile(r'^##\s*s\d+', re.IGNORECASE)
    current_shot = []
    in_shot = False
    
    def flush_shot():
        nonlocal total_lock_added, total_ref_added, total_words_stripped
        if not current_shot:
            return
        new_lines, lock, ref, stripped = process_shot(current_shot)
        patched.extend(new_lines)
        total_lock_added += lock
        total_ref_added += ref
        total_words_stripped += stripped
        current_shot = []
    
    for line in lines:
        if shot_pattern.match(line):
            flush_shot()
            in_shot = True
        elif in_shot and line.startswith('---'):
            flush_shot()
            in_shot = False
        
        current_shot.append(line)
    
    flush_shot()
    
    new_text = '\n'.join(patched)
    old_text = '\n'.join(lines)
    changed = (total_lock_added > 0 or total_ref_added > 0 or total_words_stripped > 0)
    
    # Double-check by counting
    actual_lock_added = new_text.count(JESUS_LOCK_V3) - old_text.count(JESUS_LOCK_V3)
    actual_ref_added = new_text.count(JESUS_REF) - old_text.count(JESUS_REF)
    
    if actual_lock_added > 0 or actual_ref_added > 0:
        prompts_file.write_text(new_text)
        return {
            'lock_added': actual_lock_added,
            'ref_added': actual_ref_added,
            'words_stripped': total_words_stripped
        }
    
    return None

def main(builds_to_fix):
    """Fix Jesus markers in specified builds"""
    results = {}
    
    print("=== Jesus Face Ref Auto-Fix ===")
    print(f"Processing {len(builds_to_fix)} builds...\n")
    
    for build_name in builds_to_fix:
        build_dir = MEDIA_ROOT / build_name
        if not (build_dir / 'PROMPTS.md').exists():
            print(f"⚠️ {build_name}: Not found")
            continue
        
        print(f"📦 {build_name}...")
        result = patch_prompts_md(build_dir)
        
        if result:
            results[build_name] = result
            msg = []
            if result['lock_added'] > 0:
                msg.append(f"{result['lock_added']} JESUS LOCK")
            if result['ref_added'] > 0:
                msg.append(f"{result['ref_added']} REF")
            if result['words_stripped'] > 0:
                msg.append(f"{result['words_stripped']} banned words stripped")
            print(f"  ✅ {', '.join(msg)}")
        else:
            print(f"  ℹ️ Already OK")
    
    print(f"\n=== SUMMARY ===")
    print(f"Builds processed: {len(builds_to_fix)}")
    print(f"Builds fixed: {len(results)}")
    print(f"Total JESUS LOCK v3 added: {sum(r['lock_added'] for r in results.values())}")
    print(f"Total REF: jesus-master-ref added: {sum(r['ref_added'] for r in results.values())}")
    print(f"Total banned words stripped: {sum(r['words_stripped'] for r in results.values())}")

if __name__ == '__main__':
    default_builds = [
        'build-103-peters-confession', 'build-106-god-spake-by-prophets',
        'build-107-john-baptist-doubt', 'build-108-my-sheep-hear-my-voice',
        'build-109-ask-seek-knock', 'build-110-lords-prayer', 'build-13-roof',
        'build-179-stephens-witness', 'build-17-lazarus', 'build-20-samaritan',
        'build-22-unmerciful-servant', 'build-24-sower',
        'build-39-the-pharisee-and-the-publican', 'build-40-the-friend-at-midnight',
        'build-41-counting-the-cost', 'build-42-barren-fig-tree',
        'build-43-the-wedding-garment', 'build-44-two-debtors',
        'build-45-wicked-tenants', 'build-46-seed-growing',
        'build-47-houses-on-rock-and-sand',
    ]
    
    main(sys.argv[1:] if len(sys.argv) > 1 else default_builds)
