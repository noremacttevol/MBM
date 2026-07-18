#!/usr/bin/env python3
"""Render voice-candidate auditions for the five-speaker system.

Same verse within each role so the comparison is apples-to-apples.
Constraints honoured:
  * Jesus MUST be an American voice (Cameron's permanent law, 2026-07-07).
  * No *Multilingual* models anywhere (existing narration law).
  * The narrator is NOT auditioned — en-US-AndrewNeural stays exactly as-is.
"""
import asyncio
import os

import edge_tts

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "auditions")

ROLES = {
    "JESUS": dict(
        rate="-22%", pitch="-3Hz", ref="John 14:27",
        note="younger than the current voice, calm, collected, unhurried",
        verse=("Peace I leave with you, my peace I give unto you: not as the world "
               "giveth, give I unto you. Let not your heart be troubled, neither let "
               "it be afraid."),
        cands=["en-US-BrianNeural", "en-US-GuyNeural",
               "en-US-EricNeural", "en-US-SteffanNeural"]),
    "GOD": dict(
        rate="-25%", pitch="-12Hz", ref="Isaiah 41:10",
        note="older, deeper, peaceful, stable — the premortal Jehovah of the OT",
        verse=("Fear thou not; for I am with thee: be not dismayed; for I am thy God: "
               "I will strengthen thee; yea, I will help thee; yea, I will uphold thee "
               "with the right hand of my righteousness."),
        cands=["en-US-ChristopherNeural", "en-GB-ThomasNeural",
               "en-GB-RyanNeural", "en-US-RogerNeural"]),
    "SCRIPTURE": dict(
        rate="-18%", pitch="-8Hz", ref="Romans 8:38-39 (Paul)",
        note="everyone else in scripture — one shared man's voice, raspier, warm",
        verse=("For I am persuaded, that neither death, nor life, nor angels, nor "
               "principalities, nor powers, nor things present, nor things to come, "
               "shall be able to separate us from the love of God, which is in Christ "
               "Jesus our Lord."),
        cands=["en-IN-PrabhatNeural", "en-ZA-LukeNeural",
               "en-KE-ChilembaNeural", "en-US-SteffanNeural"]),
    "FEMALE": dict(
        rate="-20%", pitch="-2Hz", ref="Ruth 1:16",
        note="the women of scripture, Old English delivery",
        verse=("Intreat me not to leave thee, or to return from following after thee: "
               "for whither thou goest, I will go; and where thou lodgest, I will "
               "lodge: thy people shall be my people, and thy God my God."),
        cands=["en-US-JennyNeural", "en-US-AriaNeural",
               "en-GB-SoniaNeural", "en-US-MichelleNeural"]),
}


def short(v):
    return (v.replace("Neural", "").replace("en-US-", "")
             .replace("en-GB-", "GB-").replace("en-IN-", "IN-")
             .replace("en-ZA-", "ZA-").replace("en-KE-", "KE-"))


async def main():
    os.makedirs(OUT, exist_ok=True)
    for role, cfg in ROLES.items():
        print(f"[{role}] {cfg['ref']} — {cfg['note']}")
        for i, v in enumerate(cfg["cands"], 1):
            path = os.path.join(OUT, f"{role}-{i}-{short(v)}.mp3")
            tmp = path + ".tmp"
            c = edge_tts.Communicate(cfg["verse"], v,
                                     rate=cfg["rate"], pitch=cfg["pitch"])
            await c.save(tmp)
            os.replace(tmp, path)          # never leave a truncated file behind
            print(f"   {i}. {short(v):14s} {os.path.getsize(path)/1024:6.0f} KB")


if __name__ == "__main__":
    asyncio.run(main())
