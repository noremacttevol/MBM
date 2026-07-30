#!/usr/bin/env bash
# Jesus V2 face — three bootstrap candidates, Nano Banana Pro, sequential.
# Prompts are documented in candidate-prompts.md (same text, kept in sync by hand).
set -u
cd "$(dirname "$0")/../.." || exit 1
OUT=media-production-v2/JESUS-V2-REF

STYLE="Cinematic biblical realism: a lifelike scene from first-century Judea, like a still frame from a reverent, masterfully photographed biblical film. Natural cinematic lighting, true depth of field, real physical scale. Realistic faces, eyes, hands and anatomy; real fabric weave, wood grain, stone, dust and skin texture. Historically credible clothing of rough-woven wool and linen in earth tones; authentic architecture and landscape. Emotionally warm, reverent, and spiritually serious. Not cartoon, not comic, not anime, not plastic CGI, not a painted illustration, not a copy of any painting or artist's style. No text, captions, borders, panels, watermarks, or modern objects anywhere in the image."

ID="A Middle Eastern Jewish man of about thirty-three, warm olive-brown skin, strong kind weathered features, shoulder-length dark brown-black wavy hair, a full dark beard, striking natural GREEN eyes, one plain undyed off-white cream wool robe with a simple mantle and cloth sash. No halo, no glow, no rim-light. Never Caucasian, never pale, never blue-eyed, never blond."

C1="Head-and-shoulders portrait, facing the camera directly, calm warm steady gaze. Soft even daylight from a high window, plain deep earth-brown background falling gently out of focus."
C2="Head-and-shoulders portrait, facing the camera directly, calm warm steady gaze. Warm low late-afternoon sunlight across the face, a dusty limestone wall far behind him softly out of focus."
C3="Head-and-shoulders portrait, facing the camera directly, calm warm steady gaze. Soft open shade under an overcast sky, cool even light, an olive grove far behind him fully out of focus."

i=1
for V in "$C1" "$C2" "$C3"; do
  echo "=== candidate $i ==="
  python3 media-production/flow_driver.py gen \
    --model "Nano Banana Pro" \
    --prompt "$STYLE $V $ID" \
    --out "$OUT/candidate-$i.jpeg"
  echo "=== candidate $i exit=$? ==="
  i=$((i+1))
done
echo "ALL CANDIDATES DONE"
