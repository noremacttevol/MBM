#!/usr/bin/env python3
"""Row 120 C-FIX 2026-08-12 — Cameron's complaint (v2_outline 120):
  "2:36 he is not head hair shaved. 1:39 his beard is shaved."

Two targeted identity-edits (lesson 10/13 method — change ONE feature, keep the
rest pixel-identical), each a single gemini-3-pro-image edit on the CURRENT still:

  s18-that-is-a-man-in.jpeg   (1:39 / c017): ADD Job's full grey-streaked beard
      back onto his (correct) bald scalp. Autopsy: the original gen IGNORED the
      JOB LOCK beard — "shaved-headed" in the b18 scene biased the model to shave
      the beard too. s19 (same dusk ash sequence) is attached as the beard anchor.

  s27-it-is-a-memory.jpeg     (2:36 / c026): SHAVE Job's scalp BALD, keep his full
      grey beard + the whole Pleiades/Orion night sky. Autopsy: the b27 scene
      ALLOWED hair (never said "shaved-headed") and the 2026-08-11 C-FIX misfiled
      s27 as a person-free cosmic beat and skipped it, so Job kept his hair.

Audio complaint (1:56 "wast"->"waste") is AUDIO-domain and handled separately.
"""
import base64
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import v2_gen_api as G  # noqa: E402

BUILD = "build-120-job-from-whirlwind"
ASSETS = os.path.join(os.path.dirname(__file__), "assets")


def edit(base_name, prompt, refs=(), tag="cfix"):
    base = os.path.join(ASSETS, base_name)
    bak = base + f".pre{tag}.bak"
    if not os.path.exists(bak):
        with open(base, "rb") as s, open(bak, "wb") as d:
            d.write(s.read())
        print(f"[{base_name}] backed up -> {os.path.basename(bak)}")
    parts = [{"inline_data": {"mime_type": "image/jpeg", "data": G.b64_file(base)}}]
    for r in refs:
        parts.append({"inline_data": {"mime_type": "image/jpeg",
                                      "data": G.b64_file(os.path.join(ASSETS, r))}})
    parts.append({"text": prompt})
    import json as _j
    import urllib.request as _u
    key = G.load_key()
    payload = _j.dumps({
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": "9:16", "imageSize": G.IMAGE_SIZE},
        },
    }).encode()
    import time as _t
    delay = 5
    for attempt in range(1, 5):
        req = _u.Request(G.API.format(model=G.MODEL) + f"?key={key}",
                         data=payload, headers={"Content-Type": "application/json"})
        try:
            with _u.urlopen(req, timeout=300) as resp:
                data = _j.load(resp)
            img = None
            for part in data["candidates"][0]["content"]["parts"]:
                if "inlineData" in part:
                    img = base64.b64decode(part["inlineData"]["data"])
                    break
            if img is None:
                raise RuntimeError("no image in response")
            with open(base, "wb") as f:
                f.write(img)
            G.record_spend(BUILD, f"cfix-{tag}", base_name)
            print(f"[{base_name}] EDITED ok ({len(img)} bytes)")
            return
        except Exception as e:
            print(f"   attempt {attempt}: {e}; retry in {delay}s")
            _t.sleep(delay)
            delay *= 2
    raise SystemExit(f"[{base_name}] FAILED after retries")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"

    if which in ("all", "s18"):
        edit(
            "s18-that-is-a-man-in.jpeg",
            prompt=(
                "You are given TWO photographs of the SAME elderly man. "
                "IMAGE 1 is the photo to EDIT. IMAGE 2 is the reference for his "
                "correct beard. Produce an edited version of IMAGE 1 that is "
                "pixel-identical to IMAGE 1 in EVERY respect EXCEPT the beard: "
                "give him a FULL, thick, long, wavy grey-streaked dark beard "
                "exactly like the man in IMAGE 2 — covering his jaw, chin, "
                "cheeks and upper lip and hanging to mid-chest, grizzled grey "
                "mixed with dark. He is about sixty. KEEP his completely BALD, "
                "shaved scalp (NO head hair whatsoever). Do NOT change his pose, "
                "his upward gaze, his open mouth, his outstretched hands, his "
                "deep russet-brown robe, the pale grey ash mound, the violet "
                "dusk sky, the ruined earthen wall, the lighting, the crop or "
                "the composition. Photorealistic, same cinematic film look, no "
                "text, no border."
            ),
            refs=("s19-he-does-not-understand-a.jpeg",),
            tag="beard",
        )

    if which in ("all", "s27"):
        edit(
            "s27-it-is-a-memory-and.jpeg",
            prompt=(
                "Edit this photograph. Change ONLY the man's head hair: shave "
                "his scalp COMPLETELY BALD — remove ALL hair from the top, back "
                "and sides of his head, leaving a clean bald shaved scalp, like "
                "a man who has shaved his head in mourning. KEEP his full grey "
                "beard exactly as it is. Do NOT change his face, his eyes, his "
                "upturned gaze, his robe, his posture, OR the night sky above "
                "him — the bright Pleiades star cluster and the Orion "
                "constellation with its three-star belt must stay exactly where "
                "they are — and keep the dark plain, the low stone wall, the "
                "lighting, the crop and the composition all pixel-identical. "
                "Only the head hair is removed. Photorealistic, same look, no "
                "text, no border."
            ),
            tag="head",
        )
    print("DONE")
