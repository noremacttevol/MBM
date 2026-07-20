#!/usr/bin/env bash
# MBM shared-library sync — the fix for "we keep fixing the same pronunciation".
#
# WHY THIS EXISTS (2026-07-19): every build folder keeps its OWN copy of the
# shared modules (mbm_pronounce.py, mbm_speakers.py, mbm_caption_timing.py)
# because build.py imports them from its own directory. So a fix made in
# media-production/mbm_pronounce.py reaches NOTHING — all 200 builds keep using
# their stale private copies. Zacchaeus, calleth, abideth and the ";)" winky-face
# fix were all applied to a file no build actually read. Cameron: "If you cant
# learn how to pronounce the names and the words correctly then we are going to
# be doing this forever." This is the mechanism behind that.
#
#   bash admin/sync-shared-libs.sh          # copy shared -> every build
#   bash admin/sync-shared-libs.sh --check   # report drift, change nothing (exit 1 if drift)
#
# ALWAYS run this after editing a shared module, BEFORE rebuilding anything.
set -u
MP="$(cd "$(dirname "$0")/../media-production" && pwd)"
LIBS="mbm_pronounce.py mbm_speakers.py mbm_caption_timing.py"
CHECK=0; [ "${1:-}" = "--check" ] && CHECK=1

drift=0; synced=0
for lib in $LIBS; do
  [ -f "$MP/$lib" ] || continue
  for dst in "$MP"/build-*/"$lib"; do
    [ -e "$dst" ] || continue
    if cmp -s "$MP/$lib" "$dst"; then continue; fi
    if [ "$CHECK" -eq 1 ]; then
      echo "DRIFT: $(basename "$(dirname "$dst")")/$lib"
      drift=$((drift+1))
    else
      cp -f "$MP/$lib" "$dst" && synced=$((synced+1))
    fi
  done
done

if [ "$CHECK" -eq 1 ]; then
  [ "$drift" -eq 0 ] && { echo "OK: every build matches the shared modules"; exit 0; }
  echo "$drift stale copies — run: bash admin/sync-shared-libs.sh"; exit 1
fi
echo "synced $synced stale copies"
