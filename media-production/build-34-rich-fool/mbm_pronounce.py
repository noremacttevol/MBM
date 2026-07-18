#!/usr/bin/env python3
"""MBM pronunciation — fix what the TTS says without touching what the caption shows.

THE LAW: the caption always keeps the true spelling. Only the spoken string changes.
`spoken_text()` is applied at narration time only; `build.py` captions the original.

TWO KINDS OF FIX, and they are not interchangeable:

  1. GLOBAL (this module's SAY dict) — words with exactly one correct reading no
     matter the sentence. Archaic verbs and proper nouns. Safe to apply everywhere.

  2. PER-SEGMENT (a build's own SPOKEN dict) — HOMOGRAPHS. "bow", "wound", "lead",
     "tears", "live", "read", "close", "use", "minute", "bass", "does", "desert",
     "content", "sow", "wind" are spelled one way and said two ways, and only the
     sentence decides which. A global map for these WILL break the other reading.
     They are listed in HOMOGRAPHS so a build can be audited for them, never
     auto-replaced.

Existing respellings across the library have themselves been wrong (#30's "uhs" was
read as "Oz"; #41's "forsaketh" came out "for-Saccath"), so every fix is verified by
transcribing the rendered audio with faster_whisper — never by assuming.
"""
import re

# ---- 1. GLOBAL: one correct reading regardless of context -------------------
# Respellings use plain letters and hyphens; edge-tts handles these far more
# reliably than IPA or SSML phonemes.
SAY = {
    # archaic KJV verb forms the neural voices routinely mangle
    "shew": "show",
    "shewed": "showed",
    "shewest": "show-est",
    "sheweth": "show-eth",
    "shewing": "showing",
    "forsaketh": "for-SAY-keth",
    "forsook": "for-SOOK",
    "spake": "spayk",
    "wist": "wist",
    "durst": "derst",
    "verily": "VAIR-ih-lee",
    "hearkened": "HAR-kend",
    "hearken": "HAR-ken",
    "holpen": "HOLE-pen",
    "wot": "wot",
    "sith": "sith",
    "twain": "twayn",
    "raiment": "RAY-ment",
    "asswaged": "a-SWAYJD",
    "unloose": "un-LOOSS",

    # proper nouns
    "Gennesaret": "Ghen-NESS-a-ret",
    "Bartimaeus": "Bar-tih-MEE-us",
    "Zacchaeus": "Zak-KEE-us",
    "Iscariot": "iss-KAIR-ee-ot",
    "Capernaum": "ka-PER-nay-um",
    "Gethsemane": "geth-SEM-a-nee",
    "Melchizedek": "mel-KIZ-eh-dek",
    "Nebuchadnezzar": "neb-yoo-kad-NEZ-ar",
    "Zarephath": "ZAIR-eh-fath",
    "Abednego": "a-BED-nee-go",
    "Shadrach": "SHAD-rak",
    "Meshach": "MEE-shak",
    "Siloam": "sy-LOH-am",
    "Bethesda": "beth-EZ-da",
    "Golgotha": "GOL-go-tha",
    "Emmaus": "em-MAY-us",
    "Nazareth": "NAZ-a-reth",
    "Bethsaida": "beth-SAY-ih-da",
    "Chorazin": "ko-RAY-zin",
    "Decapolis": "dee-KAP-o-liss",
    "Cyrenian": "sy-REE-nee-an",
    "Areopagus": "air-ee-OP-a-gus",
    "Aenon": "AY-non",
    "Salim": "SAY-lim",
    "Ephphatha": "EF-fa-tha",
    "Talitha": "TAL-ih-tha",
    "Barabbas": "ba-RAB-bas",
    "Caiaphas": "KY-a-fas",
    "Sanhedrin": "SAN-heh-drin",
    "Nicodemus": "nik-o-DEE-mus",
    "Zebedee": "ZEB-eh-dee",
    "Thaddaeus": "THAD-ee-us",
    "Ephraim": "EE-fray-im",
    "Manasseh": "ma-NASS-eh",
    "Jehoshaphat": "jeh-HOSH-a-fat",
    "Habakkuk": "ha-BAK-kuk",
    "Zerubbabel": "zeh-RUB-a-bel",
    "Malachi": "MAL-a-ky",
    "Haggai": "HAG-eye",
    "Zephaniah": "zef-a-NY-a",
    "Philippi": "fih-LIP-eye",
    "Colosse": "ko-LOSS-ee",
    "Thessalonica": "thess-a-lo-NY-ka",
    "Laodicea": "lay-od-ih-SEE-a",
    "Antipas": "AN-tih-pas",
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

_WORD = re.compile(r"[A-Za-z]+")


def spoken_text(text, overrides=None):
    """Return the string to hand the TTS. The caption keeps `text` unchanged.

    `overrides` is a build's own {written: spoken} dict for homographs and any
    one-off the global map should not own. Overrides win over SAY.
    """
    table = dict(SAY)
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
    print("in :", s)
    print("out:", spoken_text(s))
    print("homographs to decide:", audit("He bowed his bow and the wind did wind."))
