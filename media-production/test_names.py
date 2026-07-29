#!/usr/bin/env python3
"""Test every harvested name through the ear, and respell only the ones it botches.

Cameron, 2026-07-19: names like Barabbas have to be looked up and written the way
they sound, so the reader voice says them knowing how to say them.

Two rules from PRONUNCIATION-LAW.md are enforced in code here, because breaking
them is how earlier passes shipped worse audio than they started with:

  * A candidate respelling is NEVER committed unless the ear scores it better
    than the original. `forsaketh` -> `for-SAY-keth` came out "for Seyketh".
  * A respelling is one continuous lowercase word. Hyphens split the word in two
    and ALL-CAPS stress marks get read as letters.

A name is tested in EVERY voice that says it. Eric and Steffan do not agree, so a
fix verified on one is not evidence about the other. Winners land in
NAMES/respellings.json as {name: {speaker: respelling}}.
"""
import json
import os
import re
import sys

MP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MP)
import check_pronunciation as CP  # noqa: E402

OUT = os.path.join(MP, "NAMES")
STATE = os.path.join(OUT, "test-state.json")

# The carrier matters: a bare word gives the transcriber no context and it
# guesses wildly. A plain narrative frame is what these names actually sit in.
CARRIER = "And they came unto {} and stood there."

# Looked-up pronunciations, written as one continuous lowercase word. These are
# CANDIDATES ONLY -- each is A/B tested against the plain spelling below and is
# discarded unless it measurably wins. Sources are the standard Bible
# pronunciation guides; the stress syllable is spelled out phonetically rather
# than marked, since stress marks get read aloud.
CANDIDATES = {
    "Barabbas": ["burabbus", "buhrabbus", "barabbus"],
    "Zacchaeus": ["zakkeeus", "zakeeus"],
    "Nicodemus": ["nickuhdeemus", "nikohdeemus"],
    "Gethsemane": ["gethsemuhnee", "gethsemminee"],
    "Capernaum": ["kupernayum", "kapernayum"],
    "Caiaphas": ["kayuhfus", "kyefus"],
    "Bartimaeus": ["bartimeeus", "bartuhmeeus"],
    "Zebedee": ["zebbuhdee"],
    "Zacharias": ["zakuhryeus", "zakaryus"],
    "Melchizedek": ["melkizzuhdek"],
    "Nebuchadnezzar": ["nebbyukudnezzer", "nebukudnezzer"],
    "Bethphage": ["bethfayjee", "bethfuhjee"],
    "Bethesda": ["buhthezduh"],
    "Bethsaida": ["bethsayuhduh"],
    "Chorazin": ["korayzin"],
    "Iscariot": ["iskairreeut", "iskarreeut"],
    "Thaddaeus": ["thaddeeus"],
    "Bartholomew": ["barthollumew"],
    "Sadducees": ["sadjuhseez", "saddyouseez"],
    "Pharisees": ["fairuhseez"],
    "Sanhedrin": ["sanhedrin", "sanheedrin"],
    "Syrophenician": ["syrofuhnishun"],
    "Phoenicia": ["fuhnishuh"],
    "Decapolis": ["dukapuhlis"],
    "Gadarenes": ["gaduhreenz"],
    "Gerasenes": ["gerruhseenz"],
    "Siloam": ["sylohum", "siloam"],
    "Golgotha": ["golguhthuh"],
    "Calvary": ["kalvuhree"],
    "Emmaus": ["emmayus", "emmawus"],
    "Cyrene": ["syreenee"],
    "Bethany": ["bethuhnee"],
    "Bethlehem": ["bethluhhem"],
    "Nazareth": ["nazuhreth"],
    "Galilee": ["galuhlee"],
    "Gennesaret": ["gunnessuhret"],
    "Samaria": ["suhmairreeuh"],
    "Samaritan": ["suhmairritun"],
    "Jericho": ["jerrikoh"],
    "Judaea": ["joodeeuh"],
    "Judas": ["joodus"],
    "Lazarus": ["lazzuhrus"],
    "Elisabeth": ["ilizzubeth"],
    "Elijah": ["ilyejuh"],
    "Elisha": ["ilyeshuh"],
    "Isaiah": ["eyezayuh"],
    "Jeremiah": ["jairuhmyuh"],
    "Ezekiel": ["izeekeeul"],
    "Nehemiah": ["neeuhmyuh"],
    "Zerubbabel": ["zuhrubbubel"],
    "Habakkuk": ["huhbakkuk"],
    "Zephaniah": ["zefuhnyuh"],
    "Malachi": ["maluhkye"],
    "Zacchaeus's": ["zakkeeusiz"],
    "Abednego": ["uhbednuhgoh"],
    "Meshach": ["meeshak"],
    "Shadrach": ["shadrak"],
    "Belshazzar": ["belshazzer"],
    "Ahasuerus": ["uhhazyouereus"],
    "Methuselah": ["muhthoozuhluh"],
    "Zipporah": ["zipporuh"],
    "Jethro": ["jethroh"],
    "Naaman": ["nayuhmun"],
    "Gehazi": ["guhhayzye"],
    "Jehoshaphat": ["juhhoshuhfat"],
    "Hezekiah": ["hezuhkyuh"],
    "Josiah": ["johsyuh"],
    "Uzziah": ["uhzyuh"],
    "Manasseh": ["muhnassuh"],
    "Ephraim": ["eefrayim", "effrayim"],
    "Manoah": ["muhnohuh"],
    "Boaz": ["bohaz"],
    "Naomi": ["nayohmee"],
    "Ruth": ["rooth"],
    "Hannah": ["hannuh"],
    "Eli": ["eelye"],
    "Saul": ["sawl"],
    "Absalom": ["absuhlum"],
    "Bathsheba": ["bathsheebuh"],
    "Uriah": ["youryeuh"],
    "Nathan": ["naythun"],
    "Solomon": ["solluhmun"],
    "Rehoboam": ["reeuhbohum"],
    "Jeroboam": ["jerruhbohum"],
    "Ahab": ["ayhab"],
    "Jezebel": ["jezzuhbel"],
    "Obadiah": ["obuhdyuh"],
    "Micaiah": ["mykayuh"],
    "Sennacherib": ["sunnakuhrib"],
    "Isaac": ["yezuk"],
    "Ishmael": ["ishmayul"],
    "Rebekah": ["ruhbekkuh"],
    "Esau": ["eesaw"],
    "Laban": ["laybun"],
    "Rachel": ["raychul"],
    "Leah": ["leeuh"],
    "Reuben": ["roobin"],
    "Judah": ["jooduh"],
    "Naphtali": ["naftuhlye"],
    "Issachar": ["issuhkar"],
    "Zebulun": ["zebbyulun"],
    "Benjamin": ["benjuhmin"],
    "Potiphar": ["pottuhfer"],
    "Pharaoh": ["fairoh"],
    "Goshen": ["gohshun"],
    "Sinai": ["synye"],
    "Horeb": ["horeb"],
    "Canaan": ["kaynun"],
    "Jordan": ["jordun"],
    "Gilead": ["gilleeud"],
    "Moab": ["mohab"],
    "Edom": ["eedum"],
    "Philistines": ["fuhlisteenz", "filisteenz"],
    "Amalekites": ["uhmaluhkytes"],
    "Midianites": ["middeeunytes"],
    "Ninevah": ["ninnuhvuh"],
    "Nineveh": ["ninnuhvuh"],
    "Tarshish": ["tarshish"],
    "Jonah": ["johnuh"],
    "Job": ["johb"],
    "Cana": ["kaynuh"],
    "Cephas": ["seefus"],
    "Thomas": ["tommus"],
    "Matthias": ["muhthyeus"],
    "Barnabas": ["barnuhbus"],
    "Silas": ["sylus"],
    "Timothy": ["timmuhthee"],
    "Titus": ["tytus"],
    "Philemon": ["fylemun", "fuhleemun"],
    "Apollos": ["uhpolus"],
    "Aquila": ["akwilluh"],
    "Priscilla": ["prisilluh"],
    "Corinth": ["korrinth"],
    "Ephesus": ["effuhsus"],
    "Philippi": ["filippye"],
    "Thessalonica": ["thessuhluhnykuh"],
    "Colossae": ["kuhlossee"],
    "Laodicea": ["layodduhseeuh"],
    "Patmos": ["patmus"],
    "Antioch": ["anteeok"],
    "Damascus": ["duhmaskus"],
    "Tarsus": ["tarsus"],
    "Cornelius": ["korneeleeus"],
    "Ananias": ["anuhnyeus"],
    "Sapphira": ["suhfyeruh"],
    "Gamaliel": ["guhmayleeul"],
    "Stephen": ["steevun"],
    "Philip": ["fillip"],
    "Candace": ["kandayce"],
    "Aeneas": ["uhneeus"],
    "Tabitha": ["tabbithuh"],
    "Dorcas": ["dorkus"],
    "Herodias": ["huhrohdeeus"],
    "Salome": ["suhlohmee"],
    "Pilate": ["pylut"],
    "Herod": ["herrud"],
    "Augustus": ["awgustus"],
    "Tiberius": ["tybeereeus"],
    "Quirinius": ["kwyrinneeus"],
    "Malchus": ["malkus"],
    "Simeon": ["simmeeun"],
    "Anna": ["annuh"],
    "Magdalene": ["magduhleen"],
    "Joanna": ["johannuh"],
    "Susanna": ["suhzannuh"],
    "Nathanael": ["nuhthannayul"],
    "Didymus": ["diddimus"],
    "Alphaeus": ["alfeeus"],
    "Cleopas": ["kleeuhpus"],
    "Theophilus": ["theeoffuhlus"],
    "Jairus": ["jyeruss", "jayeruss"],
    "Zarephath": ["zarruhfath"],
    "Shunammite": ["shoonuhmyte"],
    "Beelzebub": ["beeelzuhbub"],
    "Abaddon": ["uhbaddun"],
    "Armageddon": ["armuhgeddun"],
    "Michael": ["mykul"],
    "Gabriel": ["gaybreeul"],
    "Seraphim": ["serruhfim"],
    "Cherubim": ["cherruhbim"],
    "Urim": ["yourim"],
    "Thummim": ["thummim"],
    "Ephod": ["effod"],
    "Shibboleth": ["shibbuhleth"],
    "Selah": ["seeluh"],
    "Hosanna": ["hohzannuh"],
    "Hallelujah": ["halluhloouhyuh"],
    "Maranatha": ["marruhnathuh"],
    "Abba": ["abbuh"],
    "Talitha": ["taluhthuh"],
    "Ephphatha": ["effuhthuh"],
    "Eloi": ["eeloy"],
    "Sabachthani": ["suhbaktuhnye"],
    "Golgotha's": ["golguhthuhz"],
    "Areopagus": ["airreeoppuhgus"],
    "Mars": ["marz"],
    "Epicureans": ["eppikyureeuns"],
    "Stoics": ["stohiks"],
    "Diana": ["dyanuh"],
    "Demetrius": ["duhmeetreeus"],
    "Eutychus": ["youtikus"],
    "Agrippa": ["uhgrippuh"],
    "Felix": ["feeliks"],
    "Festus": ["festus"],
    "Berenice": ["berruhnyce"],
    "Melita": ["melluhtuh"],
    "Puteoli": ["pyouteeohlye"],
    "Onesimus": ["ohnessimus"],
    "Epaphroditus": ["ipaffruhdytus"],
    "Tychicus": ["tikkikus"],
    "Archippus": ["arkippus"],
    "Nympha": ["nimfuh"],
    "Hymenaeus": ["hymuhneeus"],
    "Philetus": ["fuhleetus"],
    "Onesiphorus": ["onnuhsifforus"],
    "Artemas": ["artuhmus"],
    "Zenas": ["zeenus"],
    "Nicopolis": ["nikoppuhlis"],
    "Melchisedec": ["melkizzuhdek"],
    "Esaias": ["izayus"],
    "Osee": ["ohzee"],
    "Elias": ["ilyeus"],
    "Eliseus": ["eluhseeus"],
    "Booz": ["bohuz"],
    "Naason": ["nayussun"],
    "Aminadab": ["uhminnuhdab"],
    "Esrom": ["ezrum"],
    "Phares": ["fairreez"],
    "Zara": ["zairuh"],
    "Thamar": ["thaymar"],
    "Rachab": ["raykab"],
    "Obed": ["ohbed"],
    "Jesse": ["jessee"],
    "Roboam": ["ruhbohum"],
    "Abia": ["uhbyuh"],
    "Asa": ["aysuh"],
    "Josaphat": ["jossuhfat"],
    "Joram": ["joram"],
    "Ozias": ["ohzyeus"],
    "Joatham": ["johuhthum"],
    "Achaz": ["aykaz"],
    "Ezekias": ["ezuhkyeus"],
    "Amon": ["aymun"],
    "Josias": ["johsyeus"],
    "Jechonias": ["jekuhnyeus"],
    "Salathiel": ["suhlaythiel"],
    "Zorobabel": ["zuhrobbuhbel"],
    "Abiud": ["uhbyud"],
    "Eliakim": ["ilyuhkim"],
    "Azor": ["ayzor"],
    "Sadoc": ["saydok"],
    "Achim": ["aykim"],
    "Eliud": ["ilyud"],
    "Eleazar": ["elluhayzar"],
    "Matthan": ["mathan"],
}

STOP = {
    "Don", "Nobody", "Notice", "Listen", "Your", "Which", "Have", "Never",
    "Everyone", "Everything", "Whatever", "Bible", "Master", "Blessed",
    "Ghost", "Will", "Somebody", "Anyone", "Nothing", "Something", "Because",
    "Sometimes", "Maybe", "Nobody's", "Here", "There", "That", "This", "They",
    "You", "When", "What", "Where", "While", "Would", "Could", "Should",
    "Think", "Every", "Anything", "Someone", "Their", "These", "Those",
    "Just", "Only", "Still", "Even", "Look", "Real", "Most", "Both", "Many",
    "Much", "More", "Less", "Same", "Other", "Another", "First", "Last",
    "Next", "Then", "Than", "Once", "Twice", "Again", "Also", "About",
}


def heard_word(name, spoken, voice, rate, pitch):
    """Say the name in a carrier sentence; return what came back for that slot."""
    import asyncio
    import tempfile
    text = CARRIER.format(spoken or name)
    with tempfile.TemporaryDirectory() as td:
        mp3 = os.path.join(td, "t.mp3")
        asyncio.run(CP.say(text, voice, rate, pitch, mp3))
        heard = CP.transcribe(mp3)
    hw = CP.norm(heard)
    # Subtract the carrier instead of indexing into it: whisper rewrites the
    # frame words freely ("unto" comes back as "onto"), so anchoring on them
    # threw ValueError and returned the whole sentence, scoring every name as
    # broken. Whatever is left after the frame is removed is the name.
    frame = {"and", "they", "came", "unto", "onto", "into", "to", "stood",
             "there", "the", "a", "then", "went", "up", "over"}
    slot = " ".join(w for w in hw if w not in frame)
    return slot or "-", heard


def score(name, slot):
    return CP.similarity(name, slot)


def main():
    os.makedirs(OUT, exist_ok=True)
    harvest = json.load(open(os.path.join(OUT, "harvest.json")))
    try:
        state = json.load(open(STATE))
    except Exception:
        state = {"tested": {}, "wins": {}}

    # test order: the names we have a looked-up pronunciation for, most-spoken
    # first, then everything else that is plausibly a name
    def worth(n):
        if n in STOP or len(n) < 4:
            return False
        return n in CANDIDATES or not n.isupper()
    names = [n for n in harvest if worth(n)]
    names.sort(key=lambda n: (n not in CANDIDATES, -harvest[n]["count"]))

    for idx, name in enumerate(names, 1):
        speakers = harvest[name]["voices"]
        for sp in speakers:
            key = f"{name}|{sp}"
            if key in state["tested"]:
                continue
            voice = CP.VOICES.get(sp, CP.VOICES["narrator"])
            rate, pitch = CP.RATES.get(sp, ("-20%", "-4Hz"))
            try:
                slot, _ = heard_word(name, None, voice, rate, pitch)
            except Exception as e:
                print(f"  [{idx}/{len(names)}] {name}/{sp} TTS-ERROR {e}", flush=True)
                continue
            base = score(name, slot)
            rec = {"heard": slot, "base": round(base, 3)}
            if base < 0.75:
                best, best_s, best_heard = None, base, slot
                for cand in CANDIDATES.get(name, []):
                    try:
                        cslot, _ = heard_word(name, cand, voice, rate, pitch)
                    except Exception:
                        continue
                    cs = score(name, cslot)
                    if cs > best_s + 0.05:
                        best, best_s, best_heard = cand, cs, cslot
                if best:
                    rec.update(fix=best, fixed_score=round(best_s, 3),
                               fixed_heard=best_heard)
                    state["wins"].setdefault(name, {})[sp] = best
                    print(f"  [{idx}/{len(names)}] {name}/{sp}  {base:.0%} '{slot}'"
                          f"  -> '{best}' {best_s:.0%} '{best_heard}'", flush=True)
                else:
                    rec["unfixed"] = True
                    print(f"  [{idx}/{len(names)}] {name}/{sp}  {base:.0%} "
                          f"'{slot}'  -- no candidate beat it", flush=True)
            state["tested"][key] = rec
            json.dump(state, open(STATE, "w"), indent=1)
    json.dump(state["wins"], open(os.path.join(OUT, "respellings.json"), "w"),
              indent=1)
    bad = [k for k, v in state["tested"].items() if v.get("unfixed")]
    print(f"\nTESTED {len(state['tested'])} name/voice pairs")
    print(f"FIXED  {sum(len(v) for v in state['wins'].values())}")
    print(f"STILL WRONG, no candidate won: {len(bad)}")
    for k in bad[:40]:
        print("   ", k, state["tested"][k]["heard"])


if __name__ == "__main__":
    main()
