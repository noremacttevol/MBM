#!/usr/bin/env bash
# ============================================================================
# DISABLED 2026-07-24 — THIS SCRIPT WAS DESTROYING CAMERON'S PAID ELEVENLABS
# AUDIO. Do not re-enable until the flaw below is fixed and verified.
#
# FLAW: step 1 "adopt GitHub as truth" runs `git checkout origin/main -- $d/audio`
# but the ElevenLabs audio was NEVER pushed to origin — origin still holds the OLD
# 24000 Hz edge-tts clips. So this loop overwrote local paid 44100 ElevenLabs audio
# with old-voice audio, rebuilt old-voice videos, and shipped them as "fresh".
# FIX REQUIRED: push local 44100 audio to origin FIRST, and never checkout origin
# audio over local clips that are 44100 when origin's are 24000.
# ============================================================================
echo "DISABLED: this script destroyed paid ElevenLabs audio — see header." >&2
exit 1
