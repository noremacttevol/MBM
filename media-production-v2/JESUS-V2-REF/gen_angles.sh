#!/usr/bin/env bash
# Jesus V2 angle refs — three-quarter, profile, full-body standing.
# The locked master face is attached as --ref so all three are the same man.
set -u
cd "$(dirname "$0")/../.." || exit 1
OUT=media-production-v2/JESUS-V2-REF
REF=$OUT/jesus-v2-face.jpeg

STYLE="Cinematic biblical realism: a lifelike scene from first-century Judea, like a still frame from a reverent, masterfully photographed biblical film. Natural cinematic lighting, true depth of field, real physical scale. Realistic faces, eyes, hands and anatomy; real fabric weave, wood grain, stone, dust and skin texture. Historically credible clothing of rough-woven wool and linen in earth tones; authentic architecture and landscape. Emotionally warm, reverent, and spiritually serious. Not cartoon, not comic, not anime, not plastic CGI, not a painted illustration, not a copy of any painting or artist's style. No text, captions, borders, panels, watermarks, or modern objects anywhere in the image."

LOCK="JESUS LOCK v4: the SAME man as the attached JESUS-V2-REF image — identical face, hair and beard in every picture: a Middle Eastern Jewish man of about thirty-three, warm olive-brown skin, strong kind weathered features, shoulder-length dark brown-black wavy hair, a full dark beard, striking natural GREEN eyes, one plain undyed off-white cream wool robe with a simple mantle and cloth sash (only he wears cream), leather sandals. No halo, no glow, no rim-light. Never Caucasian, never pale, never blue-eyed, never blond."

A1="Three-quarter view portrait of him, head and shoulders turned about forty-five degrees from the camera, calm steady expression. Soft even daylight, plain deep earth-brown background falling gently out of focus."
A2="Strict side profile portrait of him, head and shoulders, looking level to the left of frame, calm steady expression. Soft even daylight, plain deep earth-brown background falling gently out of focus."
A3="FULL-LENGTH standing figure, the whole man visible head to sandals, arms relaxed at his sides, standing on bare dry ground, camera far enough back to show his complete height and build. Soft even daylight, plain deep earth-brown background falling gently out of focus."

i=1
for V in "$A1" "$A2" "$A3"; do
  NAME=$(printf 'jesus-v2-%s.jpeg' "$(sed -n "${i}p" <<< $'three-quarter\nprofile\nfull-body')")
  echo "=== angle $i -> $NAME ==="
  python3 media-production/flow_driver.py gen \
    --model "Nano Banana Pro" \
    --prompt "$STYLE $V $LOCK" \
    --ref "$REF" \
    --out "$OUT/$NAME"
  echo "=== angle $i exit=$? ==="
  i=$((i+1))
done
echo "ALL ANGLES DONE"
