#!/usr/bin/env python3
"""MBM pronunciation — fix what the TTS says without touching what the caption shows.

THE LAW: the caption always keeps the true spelling. Only the spoken string changes.
`spoken_text()` is applied at narration time only; `build.py` captions the original.

REWRITTEN 2026-07-20 FROM MEASUREMENT, not guesses. ab_test_say.py rendered every
old SAY entry BOTH ways (plain vs respelled) in the two heaviest voices and
transcribed the audio back. Verdict: 50 of 65 respellings scored WORSE than the
plain word — nearly all were hyphenated/ALL-CAPS forms, which PRONUNCIATION-LAW.md
Trap 2 documents as being read as two words ("for-SAY-keth" -> "for Seyketh",
"VAIR-ih-lee" -> "vjrs lead"). Those 50 are GONE: the neural voices already read
the plain word better. Full evidence: NAMES/say-ab.json.

What remains in SAY is only what measurably BEAT the plain spelling, plus two
entries hand-verified round-trip clean on Cameron-flagged defects (Zacchaeus 7/18,
abideth 7/19). SAY_BY_VOICE holds per-voice winners from test_names.py — the five
voices do not mispronounce the same words, so a fix proven on one voice is applied
only to that voice (NAMES/respellings.json).

TWO KINDS OF FIX, and they are not interchangeable:

  1. GLOBAL (SAY / SAY_BY_VOICE) — words with exactly one correct reading no
     matter the sentence. Safe to apply everywhere (per voice where measured).

  2. PER-SEGMENT (a build's own SPOKEN dict) — HOMOGRAPHS. "bow", "wound",
     "lead", "tears", "live", "read", "close", "use", "minute", "bass", "does",
     "desert", "content", "sow", "wind" are spelled one way and said two ways,
     and only the sentence decides which. A global map for these WILL break the
     other reading. They are listed in HOMOGRAPHS so a build can be audited for
     them, never auto-replaced.

RULE: never add a SAY / SAY_BY_VOICE entry that has not won an A/B test through
check_pronunciation.py (render both, transcribe both, keep the winner). Existing
respellings across the library have themselves been wrong (#30's "uhs" was read
as "Oz"; #41's "forsaketh" came out "for-Saccath"). Hyphens and ALL-CAPS stress
marks are BANNED in new entries — one continuous lowercase word only.
"""
import re

# ---- 1a. GLOBAL: measured winners only (NAMES/say-ab.json, 2026-07-20) ------
# The shew family and the names below beat the plain spelling in BOTH tested
# voices. Everything else the old dict carried lost its A/B and was removed —
# the plain word already reads better in these voices.
SAY = {
    "shew": "show",
    "shewed": "showed",
    "shewest": "show-est",
    "sheweth": "show-eth",
    "shewing": "showing",
    "forsook": "for-SOOK",

    # "an hungred" (Matt 25:35, KJV) — caught 2026-07-22 in the shipped audio of
    # #33 while verifying the divideth fix, before Cameron had to flag it. Every
    # voice breaks the plain spelling into two words, "hung red": Eric 2/2,
    # Steffan 2/2, Andrew 2/2. "hungerd" restores the single word ("an hungered")
    # in all three, 2/2 each. Global on that evidence.
    "hungred": "hungerd",

    "Bethsaida": "beth-SAY-ih-da",
    "Gennesaret": "Ghen-NESS-a-ret",
    "Habakkuk": "ha-BAK-kuk",
    "Haggai": "HAG-eye",
    "Laodicea": "lay-od-ih-SEE-a",
    "Salim": "SAY-lim",
    "Shadrach": "SHAD-rak",
    "Siloam": "sy-LOH-am",
    "Zerubbabel": "zeh-RUB-a-bel",

    # Hand-verified round-trip clean on Cameron-flagged defects, kept on that
    # evidence: "Zakkeeus" transcribes back as "Zacchaeus" (denial #3, 2026-07-18);
    # "abydeth"/"a-bide-eth" split into "abbey death" but "abiedeth" round-trips
    # as "abideth" (denial #146, 2026-07-19).
    "Zacchaeus": "Zakkeeus",
    "abideth": "abiedeth",
    # "abide": "abied" REMOVED 2026-07-20: the shipped-audio audit caught the
    # respell itself producing "abbey" (#3 j1b jesus) and "abbeyed" (#126 card
    # narrator); plain "abide" scored 100% in both contexts. abideth keeps its
    # measured fix; the bare verb never needed one.
}

# ---- 1b. PER-VOICE: winners from test_names.py (NAMES/respellings.json) -----
# {written: {speaker: spoken}} — applied only when that speaker is narrating.
SAY_BY_VOICE = {
    "Stephen": {"narrator": "steevun"},
    "Cana": {"narrator": "kaynuh"},
    "Meshach": {"scripture": "meeshak"},
    "Gennesaret": {"narrator": "gunnessuhret"},
    "Esaias": {"scripture": "izayus"},
    "Judaea": {"jesus": "joodeeuh"},
    # maketh (2026-07-21, measured this session): Eric reads the plain word as
    # "MOCK-eth" (#124 shipped audio + fresh A/B; Cameron denial #188 was the
    # same defect) and Steffan reads it "MOCKED (with)" (#150 Psalm 23 shipped
    # audio, 2/2 takes). Winners per voice: 'mayketh' round-trips clean in Eric;
    # 'makith' round-trips back as the exact word "maketh" in Steffan. Andrew's
    # plain "maketh" tested fine — no narrator entry on purpose.
    "maketh": {"jesus": "mayketh", "scripture": "maykith"},  # scripture entry upgraded 2026-07-21 (#150 round 2): fresh Steffan renders of "makith" came out "may keep"/"Mckeith"; "maykith" round-trips "maketh" exactly (MAY-kith, Cameron's #188 target).
    # divideth (2026-07-22, measured on Cameron denial #33 "Divideth is
    # pronounced wrong"): Eric reads the plain word as "divoteth" (2/2 takes on
    # the exact #33 line, Matt 25:32). Candidates that lost: "divydeth" ->
    # "divey death", "diviedeth" -> "divvy death", "dyvideth"/"dividuth" ->
    # "divoteth" (no change), "divightheth" -> "deviteth", "divyeth" ->
    # "divvyeth". Winner "divighdeth" round-trips as the exact word "divideth"
    # 2/2 on the full segment. Jesus voice only — never measured on the others.
    "divideth": {"jesus": "divighdeth"},
    # putteth (2026-07-22, Cameron denial #46 "2:36 is pronounced put - teth"):
    # Eric reads the plain word with a hard double-T stop -- it lands as two
    # beats, "put / teth", exactly as he described (isolated round-trip "Potth").
    # Candidates that lost: "puttith" -> "poodeth" (wrong vowel), "puteth" ->
    # "Pewders". Winner "putith" renders ONE smooth word (isolated "PUDITH",
    # in-sentence "puteth"). Jesus voice only -- never measured on the others.
    "putteth": {"jesus": "putith"},
    # liveth (2026-07-22, Cameron denial #50 "liveth : Livith" -- he spelled the
    # target himself -- and denial #17 "misspronouncing livest"). Plain word
    # fails differently per voice: Eric gives "Liveeth" (long ee), Steffan
    # SPLITS it into "Live Earth". "livith" round-trips as "liveth" in-sentence
    # in both, and isolated as "Livith"/"liveth". Measured on the real lines
    # (John 4:50 "thy son liveth", John 11:26 "whosoever liveth"). The woman
    # voice already carries the same fix as a build override in #149.
    "liveth": {"jesus": "livith", "scripture": "livith"},
    # commandeth (2026-07-22, Cameron denial #52 "2:23 cammandeth"): Steffan
    # reads the plain word as "come in death" / "common death" -- it breaks into
    # separate words with a death-sound, which is what he flagged. "commandith"
    # round-trips as the exact word "commandeth", isolated and in-sentence.
    "commandeth": {"scripture": "commandith"},
}

# ---- 2. PER-SEGMENT ONLY: never auto-replace these --------------------------
# Audit list. If a segment contains one of these, a human (or a whisper check)
# decides the reading and the build states it in its own SPOKEN dict.
HOMOGRAPHS = {
    "bow", "bows", "wound", "wounded", "wind", "winds", "tears", "lead",
    "sow", "sowed", "sower", "live", "lives", "read", "close", "closed",
    "use", "used", "uses", "minute", "bass", "does", "desert", "deserts",
    "content", "refuse", "object", "present", "record", "subject", "produce",
}

# ---- 0. PHRASES: KJV splits compounds the TTS expects as one word ------------
# These are not cosmetic. "for to day I must abide at thy house" (Luke 19:5) was
# rendered so that "thy" slurred into something a transcriber hears as "my" — the
# verse stops meaning Jesus will stay at YOUR house. Joining the compound fixes
# the prosody and the following word survives. The caption keeps the KJV spelling.
PHRASES = [
    (re.compile(r"\bto day\b", re.I), "today"),
    (re.compile(r"\bto morrow\b", re.I), "tomorrow"),
    (re.compile(r"\bto night\b", re.I), "tonight"),
    (re.compile(r"\bfor ever\b", re.I), "forever"),
    (re.compile(r"\bany thing\b", re.I), "anything"),
    (re.compile(r"\bevery thing\b", re.I), "everything"),
    (re.compile(r"\bsome thing\b", re.I), "something"),
    (re.compile(r"\bno thing\b", re.I), "nothing"),
    # EMOTICON TRAP (Cameron denial #184, 2026-07-18: "i cant believe it read
    # from Jesus' voice a winkey face at 22 secs"). The KJV closes parentheticals
    # with a semicolon straight into the bracket — 2 Cor 12:2 ends "God knoweth;)"
    # — and edge-tts reads ";)" aloud as "winky face". Parentheses are editorial
    # marks that are never spoken, so drop them from the SPOKEN string only; the
    # caption still shows the verse exactly as printed, brackets and all.
    # Global on purpose: a per-build override for this was silently lost twice in
    # rewrites, and any KJV parenthetical can hit it.
    (re.compile(r"[()]"), ""),
    # LIAISON: "-eth thee" (Cameron denial #8, "Calleth pronounced wrong").
    # "calleth" alone transcribes at 100%; it is the PAIR that breaks — the voice
    # slurs "calleth thee" into "califvie" (40%). Respelling "thee" -> "thih" only
    # when it follows an -eth verb breaks the liaison and scores 100%, and leaves
    # every standalone "thee" untouched. Measured, not guessed.
    (re.compile(r"\b(\w+eth)\s+thee\b", re.I), r"\1 thih"),
]
# NOTE: only true orthographic splits belong here. "any man" -> "anyone" would be
# a MEANING change, not a pronunciation fix, and must never be added.

_WORD = re.compile(r"[A-Za-z]+")


def spoken_text(text, overrides=None, speaker=None):
    """Return the string to hand the TTS. The caption keeps `text` unchanged.

    `overrides` is a build's own {written: spoken} dict for homographs and any
    one-off the global map should not own. Priority: build overrides beat
    per-voice entries, which beat the global SAY.

    `speaker` is the segment's voice key ("narrator", "jesus", "god",
    "scripture", "woman"); when given, SAY_BY_VOICE fixes proven on that voice
    are applied. Omitting it keeps the old global-only behaviour.

    ENGINE SWITCH (2026-07-23): when MBM_TTS=eleven, the Azure-measured SAY /
    SAY_BY_VOICE respellings are skipped entirely — they were tuned to Azure
    voices and hurt ElevenLabs — and only the engine-agnostic layer (PHRASES +
    per-build overrides) is applied. One env var flips every build; no call
    site changes.
    """
    import os
    if os.environ.get("MBM_TTS") == "eleven":
        from mbm_eleven import eleven_spoken_text
        return eleven_spoken_text(text, overrides)
    for pat, rep in PHRASES:
        text = pat.sub(rep, text)
    table = dict(SAY)
    if speaker:
        for w, by_voice in SAY_BY_VOICE.items():
            if speaker in by_voice:
                table[w] = by_voice[speaker]
    if overrides:
        table.update(overrides)
    lower = {k.lower(): v for k, v in table.items()}

    def repl(m):
        w = m.group(0)
        v = lower.get(w.lower())
        if v is None:
            return w
        # preserve a leading capital so sentence starts still read naturally
        if w[:1].isupper() and v[:1].islower():
            return v[:1].upper() + v[1:]
        return v

    return _WORD.sub(repl, text)


def audit(text):
    """Homographs present in `text` that a build must decide explicitly."""
    return sorted({m.group(0).lower() for m in _WORD.finditer(text)
                   if m.group(0).lower() in HOMOGRAPHS})


if __name__ == "__main__":
    s = "And he shewed them his hands. Verily I say, forsaketh not Gennesaret."
    print("out (narrator):", spoken_text(s, speaker="narrator"))
    print("out (no voice):", spoken_text(s))
    print("homographs to decide:", audit("He bowed his bow and the wind did wind."))
