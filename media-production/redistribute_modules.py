#!/usr/bin/env python3
"""Copy the canonical shared modules into every build folder that already uses
them. Each build runs from its own directory and imports its LOCAL copy, so the
canonical media-production/ versions must be pushed out after any edit.

We DO NOT copy eleven_config.json — it stays single-source in media-production/
and every build's mbm_eleven.py finds it by walking up to the parent dir, so the
API key lives in exactly one place (and out of 204 git-tracked copies).

Usage:
  python3 redistribute_modules.py            # copy to all build-*/ that have the file
  python3 redistribute_modules.py --dry-run  # show what would change, touch nothing
"""
import filecmp
import glob
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# Only the modules the ElevenLabs path actually changed. mbm_pronounce.py and
# mbm_speakers.py are deliberately NOT resynced here — they are unrelated and
# out of scope for the voice-engine swap.
MODULES = ["mbm_caption_timing.py", "mbm_eleven.py"]


def main():
    dry = "--dry-run" in sys.argv
    builds = sorted(glob.glob(os.path.join(HERE, "build-*")))
    copied = new = same = 0
    for b in builds:
        if not os.path.isdir(b):
            continue
        for mod in MODULES:
            src = os.path.join(HERE, mod)
            dst = os.path.join(b, mod)
            had = os.path.exists(dst)
            # Only seed mbm_eleven.py into folders that already have the caption
            # module (i.e. real speaker-law builds); never pollute unrelated dirs.
            if not had and mod == "mbm_eleven.py":
                if not os.path.exists(os.path.join(b, "mbm_caption_timing.py")):
                    continue
            if had and filecmp.cmp(src, dst, shallow=False):
                same += 1
                continue
            print(f"{'WOULD copy' if dry else 'copy'}: {mod} -> "
                  f"{os.path.basename(b)}{'  (new)' if not had else ''}")
            if not dry:
                shutil.copy2(src, dst)
            copied += 1
            new += (0 if had else 1)
    print(f"\n{'(dry run) ' if dry else ''}updated {copied} file(s) "
          f"({new} new), {same} already current, across {len(builds)} build dirs.")


if __name__ == "__main__":
    main()
