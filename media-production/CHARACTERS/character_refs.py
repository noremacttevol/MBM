#!/usr/bin/env python3
"""character_refs.py — the one place a build asks "what does this person look like?"

CHARACTER LAW rule 3: any still showing a rostered character must condition on
that character's LOCKED sheet AND describe them from the sheet's written spec —
never from imagination. This module makes that one line of code instead of a
copy-paste job that drifts.

From inside a build folder:

    import sys; sys.path.insert(0, '../CHARACTERS')
    from character_refs import refs, lock_text, find_in_text

    refs('peter')       -> ['/abs/.../peter/face-front.jpeg', ...3 paths]
                           pass each as a --ref to flow_driver.py gen
    lock_text('peter')  -> "PETER LOCK: <written description> Standard garments:
                           <garments>"  — paste verbatim into the prompt
    find_in_text(open('PROMPTS.md').read())
                        -> ['peter', 'john-beloved']  (who this build shows)

Aliases are resolved, so 'Simon Peter', 'John the Baptist', 'the Father' and
'Mary Magdalene' all land on the right sheet. Unknown name -> KeyError, on
purpose: a face with no sheet means rule 4 applies (build the sheet first).
"""
import json
import re
from pathlib import Path

CH = Path(__file__).resolve().parent
VIEWS = ("face-front", "three-quarter", "full-body")

# Jesus is locked elsewhere and has his own face law — never re-specced here.
JESUS_REF = CH.parent / "JESUS-MASTER-REF" / "jesus-face.jpeg"

# name-as-written-in-a-prompt -> folder slug. Longest match wins (see find_in_text).
ALIASES = {
    "god the father": "god-the-father", "heavenly father": "god-the-father",
    # NOT bare "the Father" — that phrase is all over the parables and the
    # prayers ("Father, forgive them") and is not a depiction of him.
    "young jesus": "young-jesus", "the boy jesus": "young-jesus",
    "simon peter": "peter", "peter": "peter", "cephas": "peter",
    "john the beloved": "john-beloved", "beloved disciple": "john-beloved",
    "john the baptist": "john-the-baptist", "the baptist": "john-the-baptist",
    "james the son of zebedee": "james", "james": "james",
    "mary the mother of jesus": "mary-mother-of-jesus",
    "mary mother of jesus": "mary-mother-of-jesus",
    "the virgin mary": "mary-mother-of-jesus",
    "mary magdalene": "mary-magdalene",
    "mary of bethany": "mary-of-bethany",
    "joseph of nazareth": "joseph-of-nazareth",
    "joseph of egypt": "joseph-of-egypt", "joseph in egypt": "joseph-of-egypt",
    "simon the pharisee": "simon-the-pharisee",
    "judas iscariot": "judas-iscariot", "judas": "judas-iscariot",
    "john": "john-beloved",   # bare "John" in a gospel build = the beloved
}


def _slugs():
    return sorted(d.name for d in CH.iterdir()
                  if d.is_dir() and (d / "SPEC.md").is_file())


def _spec(slug):
    return (CH / slug / "SPEC.md").read_text()


def resolve(name):
    """'Simon Peter' / 'peter' / 'PETER' -> 'peter'. KeyError if unrostered."""
    key = " ".join(str(name).lower().replace("-", " ").split())
    if key in ALIASES:
        return ALIASES[key]
    slug = key.replace(" ", "-")
    if slug in _slugs():
        return slug
    raise KeyError(
        f"{name!r} has no locked sheet. CHARACTER LAW rule 4: build the sheet "
        f"BEFORE generating story stills.")


def refs(name):
    """Absolute paths of the three locked views — pass each as --ref."""
    slug = resolve(name)
    out = [CH / slug / f"{v}.jpeg" for v in VIEWS]
    missing = [p.name for p in out if not p.exists()]
    if missing:
        raise FileNotFoundError(f"{slug}: sheet incomplete, missing {missing}")
    return [str(p) for p in out]


def _section(slug, header):
    m = re.search(rf"## {header}\n(.*?)(?=\n## |\n\*\*|\Z)", _spec(slug), re.S)
    return " ".join(m.group(1).split()) if m else ""


def lock_text(name):
    """The exact wardrobe+appearance paragraph to paste into a prompt."""
    slug = resolve(name)
    label = slug.replace("-", " ").upper()
    body = _section(slug, "Written description")
    body = re.sub(r"\(Adopts?[^)]*\)\s*", "", body)      # drop provenance asides
    garb = _section(slug, "Standard garments")
    return f"{label} LOCK: {body} Standard garments: {garb}"


# A book name followed by a number is a CITATION, not a person on screen:
# "Matt 9:9" is not Matthew, "Daniel 3" is not Daniel, "James 1:5" is not James.
CITATION = re.compile(
    r"\b(?:[1-3]\s*)?(?:matt(?:hew)?|mark|luke|john|acts|rom(?:ans)?|cor|gal|"
    r"eph|phil|col|thes+|tim|titus|heb|jas|james|pet(?:er)?|jude|rev|gen(?:esis)?|"
    r"ex(?:od(?:us)?)?|lev|num|deut|josh(?:ua)?|judg|ruth|sam|kgs|kings|chr|ezra|"
    r"neh|esth|job|ps(?:a|alm)?s?|prov|eccl|song|isa(?:iah)?|jer(?:emiah)?|lam|"
    r"ezek(?:iel)?|dan(?:iel)?|hos(?:ea)?|joel|amos|obad|jonah|mic|nah|hab|zeph|"
    r"hag|zech|mal(?:achi)?)\.?[-_\s]*\d+", re.I)
# (the [-_] also covers the slug form a build names itself by: "matthew-11_…",
#  "daniel-3_fourth-man-in-fire" — a chapter reference, not a face on screen.)


# These names are also ordinary English words ("the biggest job of his life",
# "on the eve of"). They only count when CAPITALISED, i.e. used as a name.
COMMON_WORD_NAMES = {"job", "eve", "mark", "will"}


def find_in_text(text):
    """Which rostered characters does this prompt/build text SHOW (not cite)?"""
    hits = set()
    clean = CITATION.sub(" ", text)
    low = clean.lower()
    names = sorted(set(list(ALIASES) + [s.replace("-", " ") for s in _slugs()]),
                   key=len, reverse=True)
    for n in names:
        if n in COMMON_WORD_NAMES:
            found = re.search(rf"\b{n.capitalize()}\b", clean)
        else:
            found = re.search(rf"\b{re.escape(n)}\b", low)
        if found:
            try:
                hits.add(resolve(n))
            except KeyError:
                pass
    # "John" is two different men. In a build that names the Baptist, a bare
    # "John" means the Baptist — the beloved disciple only counts if he is
    # named as such somewhere in the text.
    if "john-the-baptist" in hits and not re.search(
            r"beloved disciple|john the beloved|whom jesus loved|sons? of zebedee",
            low):
        hits.discard("john-beloved")

    # Bare "Mary" is three different women, so it used to resolve to none of
    # them — which silently hid Mary the mother from every nativity build
    # (2026-07-21 scan: #84 named her 13 times and matched nobody). Same shape
    # as the John rule: if the text says a bare Mary and never qualifies her as
    # Magdalene or of Bethany, she is the mother.
    if re.search(r"\bmary\b", low) and not (
            hits & {"mary-magdalene", "mary-of-bethany"}):
        # ...unless the scene is Bethany, where the bare Mary is Martha's sister.
        if re.search(r"bethany|martha|lazarus", low):
            hits.add("mary-of-bethany")
        else:
            hits.add("mary-mother-of-jesus")

    # Bare "Joseph" is the carpenter in a nativity/childhood build and the
    # vizier in a Genesis one. Disambiguate on the surrounding story words
    # rather than dropping him.
    # "stick of Joseph", "tribe/house/children of Joseph" name a TRIBE, not a man
    # — Ezekiel 37 is about two nations, and nobody named Joseph is on screen.
    tribal = re.compile(
        r"(?:(?:stick|rod|tribe|house|children|sons?|land|seed)\s+(?:of|for)\s+joseph"
        r"|stick-for-joseph|for\s+joseph\b)")
    if re.search(r"\bjoseph\b", tribal.sub(" ", low)) and not (
            hits & {"joseph-of-nazareth", "joseph-of-egypt"}):
        egypt = re.search(r"egypt|pharaoh|vizier|brethren|coat of many|famine", low)
        hits.add("joseph-of-egypt" if egypt else "joseph-of-nazareth")
    return sorted(hits)


def manifest():
    out = {}
    for slug in _slugs():
        out[slug] = {
            "refs": [f"CHARACTERS/{slug}/{v}.jpeg" for v in VIEWS],
            "lock_text": lock_text(slug),
            "approved": "2026-07-21",
        }
    return out


if __name__ == "__main__":
    (CH / "REFS.json").write_text(json.dumps(manifest(), indent=1))
    print(f"REFS.json written — {len(_slugs())} locked characters")
