#!/usr/bin/env python3
"""GREAT PLAN prompt system — era-aware fork of the 200-queue's v2_prompt blocks.

The 200 videos live entirely in first-century Judea, so STYLE-V2 hard-codes that
era. The Great Plan walks from the premortal council to 1820 New York to today,
so the opener and the materials lock are ERA-DRIVEN here, while every hard-won
defect block (QUALITY, DEFECT, POSITIVE-INVENTORY, WIDE geometry, ANTI-PANEL,
JESUS LOCK v5, drift words) is imported BYTE-IDENTICAL from v2_prompt — those
lessons were paid for in Cameron's rejections and apply in every century.

THE DEVIL LAW (Cameron, 2026-08-31): the devil has no body — he is a spirit and
a voice. He is NEVER rendered as a figure, character, silhouette, monster or man
in ANY scene. Beats where his presence is felt use the DEVIL_PRESENCE block:
darkness gathering, shadow spreading, cold absence — the camera never finds him.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "media-production-v2"))
from v2_prompt import (  # noqa: E402
    QUALITY_LOCK, DEFECT_LOCK, POSITIVE_INVENTORY_LOCK, PERIOD_MATERIALS_LOCK,
    WIDE_DEFENSE, WIDE_GEOMETRY_LOCK, ANTI_PANEL, CLOSER,
    JESUS_LOCK_V5, JESUS_INVENTORY_LOCK, DRIFT_WORDS, JESUS_REF,
)

# ------------------------------------------------------------------ eras ----
# Each era supplies: the opener's time-and-place clause, and a materials lock.
_STYLE_TEMPLATE = (
    "Cinematic biblical realism: a lifelike scene — {place} — like a still frame "
    "from a reverent, masterfully photographed film. Natural cinematic lighting, "
    "true depth of field, real physical scale. Realistic faces, eyes, hands and "
    "anatomy; real fabric weave and skin texture. {clothing} Emotionally warm, "
    "reverent, and spiritually serious. Not cartoon, not comic, not anime, not "
    "plastic CGI, not a painted illustration, not a copy of any painting or "
    "artist's style. No text, captions, borders, panels, watermarks{modern} "
    "anywhere in the image."
)

ERAS = {
    "heaven": {
        "place": ("in the premortal world before this earth existed, a real place "
                  "of vast scale and brilliant natural-looking light"),
        "clothing": ("Spirit men and women look like real, fully solid people of "
                     "many ancestries in simple radiant white robes of real woven "
                     "cloth — photographed people, never translucent, never "
                     "ghostly, never winged."),
        "modern": ", or modern objects",
        "materials": (
            "HEAVEN-MATERIALS LOCK: the setting is real and architectural, not a "
            "fantasy painting — colonnades, courts and floors of luminous white "
            "and gold-veined stone, open sky of dawn colours, sourceless clear "
            "daylight. Light comes from the ENVIRONMENT (sky, distance, "
            "reflection), never radiating off any person's body or head. No "
            "wings, no harps, no clouds-as-floor, no armor, no weapons, no "
            "fantasy ornamentation."),
    },
    "eden": {
        "place": "in the garden of Eden at the morning of the world",
        "clothing": ("Historically credible simple garments where the story "
                     "calls for them; untouched ancient wilderness, giant old "
                     "trees, clear water, abundant unafraid animals."),
        "modern": ", or modern objects",
        "materials": (
            "CREATION-MATERIALS LOCK: everything in frame is untouched nature — "
            "living wood, leaf, stone, water, fruit, animals. Nothing built, "
            "nothing manufactured, no tools, no cut stone, no cloth except what "
            "the scene itself names."),
    },
    "ancient": {
        "place": "in the ancient world of the patriarchs and prophets",
        "clothing": ("Historically credible clothing of rough-woven wool and "
                     "linen in earth tones; authentic ancient Near-Eastern "
                     "architecture and landscape."),
        "modern": ", or modern objects",
        "materials": PERIOD_MATERIALS_LOCK,
    },
    "first-century": {
        "place": "from first-century Judea",
        "clothing": ("Historically credible clothing of rough-woven wool and "
                     "linen in earth tones; authentic architecture and "
                     "landscape."),
        "modern": ", or modern objects",
        "materials": PERIOD_MATERIALS_LOCK,
    },
    "old-world": {
        "place": ("in the old world during the long centuries after the "
                  "apostles — late antiquity into the medieval age"),
        "clothing": ("Historically credible wool and linen clothing of that "
                     "age — tunics, cloaks, cowls, veils in earth and stone "
                     "tones; authentic stone, timber and candlelit "
                     "architecture of the period."),
        "modern": ", or modern objects",
        "materials": (
            "OLD-WORLD MATERIALS LOCK: every object is pre-industrial and "
            "hand-made — dressed stone, hewn timber, hand-forged iron and "
            "bronze, fired clay, vellum and parchment, tallow candles, "
            "rushlights and oil lamps, hand-woven cloth. Any writing visible "
            "on parchment or wall is distant, aged and completely "
            "ILLEGIBLE — no readable letters or words anywhere. No "
            "electricity, no printing later than hand-set type, nothing "
            "machine-made."),
    },
    "america-1820": {
        "place": "in rural upstate New York in the year 1820",
        "clothing": ("Historically credible early-1800s American farm clothing — "
                     "homespun linen shirts, wool trousers, work boots, plain "
                     "dresses and bonnets; hand-built timber-frame and log "
                     "buildings, split-rail fences, hardwood forest."),
        "modern": ", or objects later than 1830",
        "materials": (
            "PERIOD-1820 MATERIALS LOCK: every object is something an 1820 "
            "American farm family could own — hewn and pegged timber, hand-forged "
            "iron, tin and clay ware, tallow candles and oil lamps, leather-bound "
            "books, homespun cloth. No electricity, no machines, no printed "
            "modern typography, nothing later than 1830."),
    },
    "modern": {
        "place": "in the present day, in an ordinary real place",
        "clothing": ("Contemporary everyday clothing on ordinary people of many "
                     "ancestries; real modern streets, homes and rooms."),
        "modern": "",
        "materials": (
            "MODERN-CANDID LOCK: the scene is documentary-real — actual modern "
            "objects, real wear and clutter, believable light. No brand logos, "
            "no readable screens or signs, no recognizable real people."),
    },
}

DEVIL_PRESENCE = (
    "THE ENEMY IS PRESENT BUT HAS NO BODY: his presence is rendered ONLY as "
    "darkness — a spreading shadow, a cold darkening at one region of the frame, "
    "light failing at an edge — with NO figure, NO silhouette, NO face, NO eyes, "
    "NO smoke-creature, NO horned or hooded shape of any kind inside the "
    "darkness. The darkness is an absence, not a character. Nobody in the scene "
    "looks at a visible being where the darkness is."
)

FATHER_LOCK = (
    "THE FATHER LOCK: the same Person as the attached FATHER-GP-REF image in "
    "every picture — a glorified, dignified Father with warm deep-toned skin, "
    "long silver-white hair and a full silver-white beard, strong kind ageless "
    "features, wearing a RADIANT PURE-WHITE robe (brilliant white, never cream — "
    "only Jesus wears cream). His bearing is majesty and warmth together, a "
    "Father before a King. No halo, no glow, no rim-light, no light radiating "
    "from his body; the light in the scene is environmental."
)

COURT_LOCK = (
    "COUNCIL-COURT LOCK: the setting is always the same premortal council "
    "court — wide terraces of luminous white and gold-veined stone descending "
    "like broad steps toward a distant raised dais that stands in the "
    "brightest natural light, under an open endless sky of deep dawn colours "
    "(indigo overhead melting to warm gold at the horizon). No earth, no "
    "moon, no vegetation — polished stone, light and sky only. The light on "
    "the court is environmental daylight from the sky and the bright distance "
    "around the dais, never rays or beams radiating from any person."
)

HOSTS_LOCK = (
    "HOSTS LOCK: the assembled spirits are countless real, solid men and "
    "women of every ancestry — Middle Eastern, African, East Asian, South "
    "Asian, European, Pacific — young-adult in bearing, each in a simple "
    "radiant WHITE robe of real woven cloth (bright pure white, never cream "
    "— only the Son wears cream). Every robe is a ONE-PIECE, LONG-SLEEVED, "
    "ankle-length tailored garment, the same cut on everyone — never a "
    "wrapped sheet, toga, shawl, towel, sash-wrap or any draping that "
    "leaves a shoulder or chest bare. They are photographed people with "
    "weight and shadow: never translucent, never glowing, never winged, "
    "never floating."
)

# "FATHER" as a lock token carries BOTH the prose (here) and the reference
# sheet (gp_engine attaches CAST-GP-REF/father-*.jpeg for the same token).
# COURT/HOSTS are shared across every heaven episode (2-6 and beyond); an
# episode's own LOCKS entry with the same name overrides (ep01 predates this).
ADAM_LOCK = (
    "ADAM LOCK: the same man as the attached reference in every picture — "
    "in his strong mid-thirties, warm olive-brown sun-weathered skin, thick "
    "shoulder-length near-black hair and a full dark beard, broad workman's "
    "build. Kind, intelligent, weathered. No halo, no glow.")

EVE_LOCK = (
    "EVE LOCK: the same woman as the attached reference in every picture — "
    "mid-thirties, warm olive-brown skin, very long dark wavy hair, strong "
    "gentle intelligent features. Wise, warm, fearless. No halo, no glow.")

JOSEPH_LOCK = (
    "JOSEPH LOCK: the same boy as the attached reference in every picture — "
    "Joseph Smith at fourteen: a sturdy American farm boy, tall for his age, "
    "thick sandy light-brown hair, a fair sun-tanned open face, strong brow, "
    "light-coloured thoughtful eyes, plain 1820 homespun. Earnest, strong, "
    "unpolished. No halo, no glow.")

_GP_LOCAL_LOCKS = {"FATHER": FATHER_LOCK, "FATHER-TEXT": FATHER_LOCK,
                   "COURT": COURT_LOCK, "HOSTS": HOSTS_LOCK,
                   "ADAM": ADAM_LOCK, "EVE": EVE_LOCK,
                   "JOSEPH-SMITH": JOSEPH_LOCK}


def style_of(era):
    e = ERAS[era]
    return _STYLE_TEMPLATE.format(place=e["place"], clothing=e["clothing"],
                                  modern=e["modern"])


def assemble(beat, local_locks):
    """Full prompt for one GP beat. Mirrors v2_prompt.assemble, era-aware."""
    era = beat.get("era", "ancient")
    parts = [style_of(era), QUALITY_LOCK, DEFECT_LOCK, POSITIVE_INVENTORY_LOCK,
             ERAS[era]["materials"]]
    if beat.get("wide"):
        parts.append(WIDE_DEFENSE)
        parts.append(WIDE_GEOMETRY_LOCK)
    parts.append(ANTI_PANEL)
    if beat.get("devil"):
        parts.append(DEVIL_PRESENCE)
    for name in beat.get("locks", []):
        block = (local_locks or {}).get(name) or _GP_LOCAL_LOCKS.get(name)
        if block is None:
            raise SystemExit(f"{beat['id']}: unknown lock {name!r}")
        parts.append(block)
    if beat.get("jesus"):
        parts.append(JESUS_LOCK_V5)
        parts.append(JESUS_INVENTORY_LOCK)
    if beat.get("must_show"):
        parts.append("STORY MUST SHOW: " + beat["must_show"])
    if beat.get("must_not_show"):
        parts.append("HARD REJECTION CONDITIONS: " + beat["must_not_show"])
    parts.append(beat["scene"])
    parts.append(CLOSER)
    return " ".join(" ".join(p.split()) for p in parts)


DEVIL_FIGURE_WORDS = [
    "satan stands", "satan standing", "lucifer stands", "lucifer standing",
    "satan's face", "lucifer's face", "the devil stands", "devil's face",
    "hooded figure", "dark figure", "shadowy figure", "silhouette of satan",
    "silhouette of lucifer", "horned",
]


def check(mod):
    """GP gate — every rule that can be checked before a credit is spent."""
    fails, warns = [], []
    for beat in mod.BEATS:
        p = assemble(beat, mod.LOCKS)
        low_scene = beat["scene"].lower()
        if beat.get("era") not in ERAS:
            fails.append(f"{beat['id']}: unknown era {beat.get('era')!r}")
        if beat.get("jesus") and not beat.get("ref"):
            fails.append(f"{beat['id']}: Jesus beat missing ref=True")
        for field in ("must_show", "must_not_show"):
            if not str(beat.get(field, "")).strip() or "TODO" in str(beat.get(field, "")):
                fails.append(f"{beat['id']}: {field} is missing or unfinished")
        for w in DRIFT_WORDS:
            if w in low_scene:
                fails.append(f"{beat['id']}: drift word {w!r} in the scene text")
        for w in DEVIL_FIGURE_WORDS:
            if w in low_scene:
                fails.append(f"{beat['id']}: DEVIL LAW — figure language {w!r} "
                             f"(he is a voice, never a body)")
        if "NEGATIVE" in beat["scene"].upper():
            fails.append(f"{beat['id']}: NEGATIVE-PROMPT list is banned")
        if beat.get("wide"):
            if not any(k in low_scene for k in ("camera", "lens", "shot on")) or not any(
                    k in low_scene for k in ("behind", "past them", "backs",
                                             "from the side", "profile",
                                             "three-quarter", "away from the")):
                warns.append(f"{beat['id']}: wide beat does not state "
                             f"camera-to-back geometry in its own scene text")
        if "FATHER" in beat.get("locks", []) and "FATHER-TEXT" not in beat.get("locks", []):
            pass  # FATHER image ref + FATHER-TEXT prose travel together via engine
    return fails, warns
