#!/usr/bin/env bash
# CAST V2 REFERENCE LIBRARY — 2K photoreal sheets via Flow (Cameron's order, 2026-07-30).
# 15 recurring characters x 2 angles = 30 portraits, Nano Banana Pro, sequential.
# Identities carried over from media-production/CAST-REF/CAST-BIBLE.md (V1) — same
# ages, builds, hair, beards, WARDROBE COLOURS — restyled photoreal to match the
# approved JESUS-V2-REF look. Only Jesus wears cream; nobody here does.
#
# When every portrait is done, finished sheets are copied to
# ~/Desktop/CAST-V2-APPROVAL/ for Cameron to eyeball and approve.
set -u
cd "$(dirname "$0")/../.." || exit 1
OUT=media-production-v2/CAST-V2-REF
LOG="$OUT/gen_cast_v2.log"

STYLE="Cinematic biblical realism: a lifelike scene from first-century Judea, like a still frame from a reverent, masterfully photographed biblical film. Natural cinematic lighting, true depth of field, real physical scale. Realistic faces, eyes, hands and anatomy; real fabric weave, wood grain, stone, dust and skin texture. Historically credible clothing of rough-woven wool and linen in earth tones; authentic architecture and landscape. Emotionally warm, reverent, and spiritually serious. Not cartoon, not comic, not anime, not plastic CGI, not a painted illustration, not a copy of any painting or artist's style. No text, captions, borders, panels, watermarks, or modern objects anywhere in the image."

FRONT="Head-and-shoulders portrait, facing the camera directly, calm steady gaze. Soft even daylight from a high window, plain deep earth-brown background falling gently out of focus."
QUARTER="Head-and-shoulders portrait, head and shoulders turned three-quarters toward the viewer's right, eyes toward the camera. Soft even daylight from a high window, plain deep earth-brown background falling gently out of focus."
TAIL="A first-century Middle Eastern Jewish person: never Caucasian, never pale, never blue-eyed, never blond. No halo, no glow, no rim-light."

declare -A ID
ID[peter]="Simon Peter: a sturdy Galilean fisherman in his late thirties, broad and strong, thick dark curly hair going a little wild, a full dark beard, weathered warm-olive skin, deep brown eyes, heavy honest features, wearing a dusty BLUE-GREY rough wool tunic with a plain rope belt, never cream."
ID[andrew]="Andrew: a Galilean fisherman in his early thirties, sturdy but leaner than his brother, short dark curly hair, a shorter rounded dark beard, warm-olive skin, open kind eyes, wearing a RUST-BROWN rough wool tunic with a cord belt, never cream."
ID[james-z]="James son of Zebedee: a tall strong Galilean in his mid thirties, dark hair pulled back off the face, a thick full black beard, deep-olive skin, a steady bold gaze, wearing a DEEP-OLIVE brown-green wool tunic with a leather belt, never cream."
ID[john]="John son of Zebedee: the youngest disciple, early twenties, smooth-featured and gentle, wavy chestnut-brown hair to the jaw, only a soft light beard, warm tan skin, large calm dark eyes, wearing a SAND warm-tan wool tunic with a woven sash, never cream."
ID[philip]="Philip: a lean thoughtful Galilean in his mid thirties, straight dark hair parted at the side, a neatly trimmed dark beard, olive skin, level brows, wearing a DUSTY-GREEN wool tunic with a cord belt, never cream."
ID[bartholomew]="Bartholomew called Nathanael: a broad kind man in his late forties, a greying dark beard, a high receding hairline with grey at the temples, sun-browned olive skin, deep laugh lines, wearing an EARTH-BROWN wool tunic with a rope belt, never cream."
ID[thomas]="Thomas called Didymus: a wiry restless Galilean in his mid thirties, dark deep-set eyes under strong brows, medium-length dark hair, a medium dark beard, olive skin, an earnest searching look, wearing a SLATE-GREY blue-charcoal wool tunic with a cord belt, never cream."
ID[matthew]="Matthew the former tax collector: late thirties, a shade neater than the fishermen, dark hair combed back, a short well-kept dark beard, warm-olive skin, quiet observant eyes, wearing a DEEP OXBLOOD-MAROON wool tunic with a plain belt, never cream."
ID[james-a]="James son of Alphaeus: a small slight man in his late twenties, a thin light dark beard, short dark hair, warm tan skin, a mild modest expression, wearing an ASH-GREY dun wool tunic with a cord belt, never cream."
ID[thaddaeus]="Thaddaeus also called Jude: a stocky warm-hearted man in his early forties, curly dark hair going grey, a rounded greying beard, ruddy-olive skin, a ready gentle smile, wearing an OCHRE muted-mustard wool tunic with a rope belt, never cream."
ID[simon-z]="Simon the Zealot: a lean intense man in his mid thirties, sharp features, black hair and a black beard trimmed close, deep-olive skin, quick alert eyes, wearing a DARK BRICK red-brown wool tunic with a leather belt, never cream."
ID[judas]="Judas Iscariot: an ordinary dignified Judean in his mid thirties, smoother and better-kept than the Galileans, sleek dark hair and a neat dark beard, olive skin, watchful guarded eyes, wearing a DARK TEAL-GREEN wool tunic with a plain belt, never cream."
ID[mary-mother]="Mary the mother of Jesus: a dignified Jewish woman of about fifty, warm olive skin, a gentle worn kind face, dark hair streaked with grey shown modestly under a deep INDIGO-BLUE wool head veil, an undyed flax-brown tunic beneath, never cream."
ID[mary-magdalene]="Mary Magdalene: a Jewish woman in her mid thirties, warm olive skin, long dark wavy hair loosely covered by a MUTED PLUM head scarf, expressive dark eyes that have known both sorrow and joy, wearing a dark plum-brown wool tunic, never cream."
ID[john-baptist]="John the Baptist: a lean weathered wilderness prophet in his late thirties, sun-darkened deep-tan skin, long untamed dark hair, a rough full dark beard, intense burning eyes, wearing a rough CAMEL-HAIR garment with a wide leather girdle at the waist, never cream."

ORDER="peter andrew james-z john philip bartholomew thomas matthew james-a thaddaeus simon-z judas mary-mother mary-magdalene john-baptist"

echo "=== CAST V2 burst start $(date) ===" | tee -a "$LOG"
made=0; failed=0
for name in $ORDER; do
  for angle in front quarter; do
    dest="$OUT/${name}-${angle}.jpeg"
    if [ -f "$dest" ] && [ "$(stat -c%s "$dest")" -gt 50000 ]; then
      echo "skip $name-$angle (exists)" | tee -a "$LOG"; continue
    fi
    [ "$angle" = front ] && POSE="$FRONT" || POSE="$QUARTER"
    echo "=== gen $name-$angle $(date +%H:%M:%S) ===" | tee -a "$LOG"
    ok=0
    for try in 1 2; do
      if python3 media-production/flow_driver.py gen \
          --model "Nano Banana Pro" --size 2K \
          --prompt "$STYLE $POSE ${ID[$name]} $TAIL" \
          --out "$dest" >>"$LOG" 2>&1; then
        ok=1; break
      fi
      echo "    attempt $try failed for $name-$angle; cooling 180s" | tee -a "$LOG"
      sleep 180
    done
    if [ "$ok" = 1 ]; then
      made=$((made+1)); echo "    OK $name-$angle" | tee -a "$LOG"
    else
      failed=$((failed+1)); echo "    FAILED $name-$angle (see log)" | tee -a "$LOG"
    fi
    # Stay under Flow's ~20 gens/hour session ceiling — the 07-30 burst died at
    # gen 24 running at triple that pace.
    sleep "${SLEEP_BETWEEN:-150}"
  done
done

mkdir -p ~/Desktop/CAST-V2-APPROVAL
cp -f "$OUT"/*-front.jpeg "$OUT"/*-quarter.jpeg ~/Desktop/CAST-V2-APPROVAL/ 2>/dev/null
echo "=== CAST V2 burst done $(date): $made generated, $failed failed. Sheets copied to ~/Desktop/CAST-V2-APPROVAL ===" | tee -a "$LOG"
