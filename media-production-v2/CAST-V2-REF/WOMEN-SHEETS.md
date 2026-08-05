# CAST-V2-REF — the women's sheets (provenance)

The apostle sheets in this folder are purpose-generated 2K portraits (see
`gen_cast_v2.sh` / `gen_cast_v2.log`). The **women's sheets are different**: they
are byte-for-byte copies of already-approved build stills, chosen as each woman's
canonical face anchor. Do NOT run `gen_cast_v2.sh` to "regenerate" them — recopy
from the source still (or from a newer approved render) instead.

| Sheet | Copied from | Woman | Why this still |
|---|---|---|---|
| `martha-front.jpeg`        | `build-16-mary-martha/assets/s18-martha-martha.jpeg`        | Martha (of Bethany)       | Author's canonical Martha pick (row-17 CAST LINEAGE): largest, sharpest face; dark-ochre headcloth matches her LOCK. |
| `martha-quarter.jpeg`      | `build-16-mary-martha/assets/s02-martha-welcomed-him-in.jpeg` | Martha (of Bethany)       | Clear near-front second angle of the same woman, well lit. |
| `mary-bethany-front.jpeg`  | `build-16-mary-martha/assets/s10-the-place-a-student-sat.jpeg` | Mary of Bethany           | Author's canonical Mary pick (row-17): the front-facing, open-eyed view. |
| `mary-bethany-quarter.jpeg`| `build-16-mary-martha/assets/s09-at-his-feet-listening.jpeg` | Mary of Bethany           | Same woman, different angle (kneeling at his feet). |

Source stills are `*.jpeg` and therefore **gitignored**, so they live only on the
machine that rendered build-16. These four sheets are force-added (`git add -f`)
exactly like the apostle sheets, so every machine gets the faces through git.

## Still missing (render then add)
- **`mary-mother-*.jpeg`** — Mary the mother of Jesus. Token `MARY-MOTHER` is in
  `GLOBAL_CAST` but has no sheet. Pull her canonical front/quarter from an approved
  nativity/Cana row (build-49/84/85/86/87) once one is rebuilt in v2.
- **`mary-magdalene-*.jpeg`** — token `MARY-MAGDALENE` is in `GLOBAL_CAST` but
  build-98 (`mary-her-name`, her only row) is not yet built in v2, so no approved
  still exists. Add the sheet from build-98's render when it lands.

Until those two sheets exist, any beat locking `MARY-MOTHER` / `MARY-MAGDALENE`
renders that woman TEXT-ONLY and `v2_gen_api.cast_refs_for()` prints a loud
WARNING (added 2026-08-05). Wire a build-local `REFS` for her in the meantime.

## The three-Marys law
`GLOBAL_CAST` deliberately has **no bare `MARY` token** — "MARY" names three
different women across the library (Bethany / mother / Magdalene), each carried by
its build's own MARY LOCK prose. A global `MARY` would stamp one face onto all
three. Authors lock the disambiguated token (`MARY-BETHANY`, `MARY-MOTHER`,
`MARY-MAGDALENE`); see the GLOBAL_CAST comment in `v2_gen_api.py`.
