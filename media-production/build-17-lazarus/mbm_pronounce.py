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
    # Cameron denial #146 (2026-07-19): heard as "abadeth" (flat i). It is from
    # ABIDE — uh-BYDE-eth. Measured: "abydeth"/"a-bide-eth" split into "abbey
    # death"; "abiedeth" round-trips clean as "abideth".
    "abideth": "abiedeth",
    "abide": "abied",

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
    # Measured 2026-07-18 (Cameron denial #3, "it misspronounced Zacchaeus every
    # time"): the old hyphenated "Zak-KEE-us" was HEARD AS "Sekias" — 29% match.
    # Hyphens split the word (see PRONUNCIATION-LAW §traps). Unhyphenated
    # "Zakkeeus" round-trips as "Zacchaeus" — verified with check_pronunciation.
    "Zacchaeus": "Zakkeeus",
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


def spoken_text(text, overrides=None):
    """Return the string to hand the TTS. The caption keeps `text` unchanged.

    `overrides` is a build's own {written: spoken} dict for homographs and any
    one-off the global map should not own. Overrides win over SAY.
    """
    for pat, rep in PHRASES:
        text = pat.sub(rep, text)
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
