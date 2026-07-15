# BUILD STATUS — #42 The Barren Fig Tree Spared (Luke 13:6-9)

**Delivered:** `luke-13_barren-fig-tree.mp4` — 1080x1920 H.264 30fps, 4:16, 24.0 MB, crf 20.
**Built:** 2026-07-14 (Machine A). **Status:** waiting on Cameron's yes.

Phase-1 STILLS-ONLY (Law E): 12 painted stills, Ken Burns drift, no AI motion clips.
**CARE-FLAG J — mercy-in-judgment.** Narration carries the mercy that is in the text out
loud: the tree deserves the axe and is GIVEN another year instead, and the gardener does
not scold it — he asks to work for it. The axe is never swung on screen; the closing card
is an invitation, not a fear-question.

## Art pipeline — FLOW, $0 (the money rule held)

All 12 stills generated in **Google Flow (Nano Banana 2, 9:16, 1x, 0 credits)** on
Browser 1's logged-in Ultra account. Each still downloaded at **2K** (detail-view upscale,
1536x2752), mapped by content, placed in assets/. `gen_stills.py` and the paid Gemini
image API were NOT used. **Cost: $0.** s10 was regenerated once (first pass came back a
letterboxed panorama with the subject too small for a 9:16 frame; the redo fills the
upright frame and shows the set-aside axe clearly).

## The point (Why-Law)

The misread is "produce or God cuts you down." The point is the opposite: **the tree that
had earned the axe got another year** — not because it changed, but because someone who
cared for it stood between it and the axe and asked (n10/n10b). The gardener's answer to
the verdict is not a defense of the tree but an offer to do the humblest work himself:
loosen the packed soil (n7) and feed it by hand (n8). The counting of "these three years"
is real (the owner is fair, not cruel, n5), which is exactly what makes the reprieve grace
and not indifference.

## Two-voice

Jesus (en-US-ChristopherNeural) speaks exact KJV — the whole parable is his direct speech,
4 lines: **jv6 (13:6, the fig tree)**, **jv7 (13:7, the verdict — sacred silence 1)**,
**jv8 (13:8, the plea — sacred silence 2, the heart)**, jv9 (13:9, "if it bear fruit,
well"). "He spake also this parable;" is Luke's narration, carried by the narrator (n1),
so the Jesus voice speaks only the story itself. Narrator (en-US-AndrewNeural) modern,
never echoes a KJV line (n5 "holding a place" not "cumbereth", n7 "break up the packed
earth" not "dig about it", n8 "feed it" not "dung it").

## QC — final pass clean

| Check | Result |
|---|---|
| Face gate on prompt sheet | **PASS** (exit 0) before any image was generated |
| Jesus's face in finished render | Never visible — s1 and s12 only, camera directly behind both times |
| Only-Jesus-cream | s1/s12: only the from-behind figure in cream; the whole crowd in dun/brown/olive/blue |
| Phase-1 stills-only | No AI motion clips |
| No-dead-air | Worst spoken gap **1.88s** (law <=2.5s) |
| Loudness | **-14.9 LUFS** (target -15) |
| Format | 1080x1920, H.264, 30fps, 24.0 MB (<30MB cap), crf 20, vcap 806 kbps |
| Captions | Verbatim spoken text; KJV cream italic (jv6/jv8 sampled exact), narration white serif |
| Milk framing | Axe never swung; owner is fair not cruel; closing card an invitation, never a fear-question |
| Character consistency | Vineyard owner (russet-maroon + grey-streaked beard) held across s3/s4/s5/s11; gardener (dun rolled-sleeve work tunic) across s6/s7/s8/s11 |

## Shot list (12 stills)

s1 the telling (frame, Jesus from behind) · s2 the fig tree in the vineyard (jv6) ·
s3 seeking fruit, finding none · s4 three years of it · s5 cut it down — the verdict
(jv7) · s6 let it alone — the plea (jv8) · s7 dig about it — loosening the soil ·
s8 dung it — feeding it · s9 if it bear fruit — the first buds (jv9) · s10 the axe set
aside — the reprieve · s11 the intercession granted · s12 the invitation (frame return).
