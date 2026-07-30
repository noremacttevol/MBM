#!/usr/bin/env python3
"""Apply Cameron's delete-pass from ~/Desktop/V2-PICTURE-REVIEW.

The review folder holds a COPY of every V2 still, named `<row-slug>__<shot>.jpeg`
(e.g. `01-cloak__s06-woman-at-edge.jpeg`). Cameron skims it and DELETES the bad
ones. This tool compares what is left in the review folder against each build's
assets/ and treats every missing copy as "REJECTED — regenerate on the API":

    python3 v2_review_diff.py            # report only (nothing moved)
    python3 v2_review_diff.py --apply    # move rejected originals to _replaced/

--apply moves each rejected original from  build-NN-slug/assets/<shot>
to  build-NN-slug/_replaced/<shot>  (never deletes bytes). Once the original is
out of assets/, v2_gen_api.py sees the beat as missing and re-shoots it — so the
regen queue IS the set of files Cameron deleted. Run with no flag first to see
the count and the dollar estimate before anything moves.
"""
import argparse
import glob
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
REVIEW = os.path.expanduser("~/Desktop/V2-PICTURE-REVIEW")
COST_PER_IMAGE = 0.134  # gemini-3-pro-image at 2K


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="move rejected originals to _replaced/ (default: report only)")
    a = ap.parse_args()

    if not os.path.isdir(REVIEW):
        raise SystemExit(f"Review folder not found: {REVIEW}")

    kept = set(os.listdir(REVIEW))
    rejected = []
    for d in sorted(glob.glob(os.path.join(HERE, "build-*"))):
        slug = os.path.basename(d)[len("build-"):]
        assets = os.path.join(d, "assets")
        if not os.path.isdir(assets):
            continue
        for f in sorted(os.listdir(assets)):
            if not f.lower().endswith((".jpeg", ".jpg", ".png")):
                continue
            if not os.path.isfile(os.path.join(assets, f)):
                continue
            if f"{slug}__{f}" not in kept:
                rejected.append((d, f))

    if not rejected:
        print("Nothing deleted from the review folder — nothing to replace.")
        return

    by_build = {}
    for d, f in rejected:
        by_build.setdefault(os.path.basename(d), []).append(f)
    for b in sorted(by_build):
        print(f"{b}: {len(by_build[b])} rejected")
        for f in by_build[b]:
            print(f"    {f}")
    print(f"\nTOTAL rejected: {len(rejected)}  "
          f"(~${len(rejected) * COST_PER_IMAGE:.2f} to re-shoot on the API)")

    if not a.apply:
        print("\nReport only — run again with --apply to move these out of assets/ "
              "so the API runner re-shoots them.")
        return

    moved = 0
    for d, f in rejected:
        dst_dir = os.path.join(d, "_replaced")
        os.makedirs(dst_dir, exist_ok=True)
        src = os.path.join(d, "assets", f)
        dst = os.path.join(dst_dir, f)
        if os.path.exists(dst):
            base, ext = os.path.splitext(f)
            k = 2
            while os.path.exists(os.path.join(dst_dir, f"{base}.old{k}{ext}")):
                k += 1
            dst = os.path.join(dst_dir, f"{base}.old{k}{ext}")
        shutil.move(src, dst)
        moved += 1
    print(f"\nMoved {moved} rejected originals to their build's _replaced/ folder. "
          f"The API runner will re-shoot exactly these.")


if __name__ == "__main__":
    main()
