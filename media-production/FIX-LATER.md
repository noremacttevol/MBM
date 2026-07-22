# FIX-LATER — pronunciation defects found in APPROVED videos (2026-07-21 whisper sweep)

These builds are `approved:true` on the board, so their cuts are LOCKED
(approved-lock law: never ship over an approved cut). The 2026-07-21 sweep
transcribed the final mp4 audio of all 200 videos; the defects below are in
approved cuts and wait for Cameron to un-approve / ask for the fix.

When fixing one: the measured respell winners from this sweep are noted where
known — still re-verify in the segment's actual voice before rebuild.

## Real, audible (fix first when unlocked)
| # | build | defect heard in the shipped audio |
|---|---|---|
| 11 | storm | cut is off-script: the KJV "Master, carest thou not that we perish?" area plays older narration ("Teacher…"). Needs re-record + rebuild on the current script. |
| 12 | bartimaeus | "Bartimaeus" read "bar-tai-e-MI-yas"; "Nazareth" read "e-NAZ-i-rath" (twice); "calleth thee" slurred ("callothy" — the -eth-thee liaison; PHRASES thih fix should cover it on re-record) |
| 99 | flesh-and-bone-thomas | cut is off-script: audio plays an older draft of the narration (many divergences). Needs re-record + rebuild. |
| 100 | the-ascension | "Judaea" garbled/dropped ("do") — SAY_BY_VOICE has joodeeuh for the jesus voice only; this hit another voice |
| 104 | boy-samuel | "calledst" dropped to "call" |
| 114 | abraham-sodom | "peradventure" truncated to "per" (the global purradventure respell predates this cut) |
| 115 | ram-in-the-thicket | "climbed" read "cloned" (twice); "fearest" read "fierced" |
| 152 | revealeth-his-secret | "revealeth" read "re-VIOL-eth" |
| 154 | everlasting-gospel | "tongue" read "town" (twice) |
| 156 | famine-of-hearing | "ache" read "egg" (twice); "chasing" read "facing" |
| 158 | two-sticks | "Ephraim" dropped to just "E" (twice) |
| 4 | nicodemus | "myrrh" read "mare" |

## Milder / borderline (ear-check when unlocked)
| # | build | note |
|---|---|---|
| 101 | still-small-voice | "poured" ~ "port" |
| 102 | jacobs-ladder | "liest" ~ "least" (may be correct sound) |
| 106 | god-spake-by-prophets | "divers (manners)" garbled |
| 117 | hosea-buys-her-back | one narration stretch garbled ("fifteen" area) |
| 118 | jonah | "calm" ~ "common" |
| 120 | job-from-whirlwind | "Orion's belt" stretch garbled |
| 15 | centurion | several small word swaps (wears/where, speak/say) — possibly older narration draft |
| 136 | healed-in-two-touches | "halfway" ~ "half" |

16-mary-martha was also complained about ("wound") but its approved cut now
reads correctly (verified this sweep) — nothing to fix.

## #49 water-to-wine — "Cana" per-voice fix never applied (2026-07-22)
APPROVED-LOCKED, so it was NOT rebuilt. The 175-build "dropped speaker" bug
(see `fix_dropped_voice.py`) means this cut was rendered with the plain
spelling of "Cana" instead of the measured per-voice fix. Its script is
already patched, so the correction lands the next time #49 is rebuilt for any
other reason. Do NOT rebuild it just for this — Cameron approved this cut.
