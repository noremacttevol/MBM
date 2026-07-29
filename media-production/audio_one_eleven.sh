#!/usr/bin/env bash
# ============================================================================
# DISABLED 2026-07-24 — THIS SCRIPT WAS DESTROYING CAMERON'S PAID ELEVENLABS
# AUDIO. Do not re-enable until the flaw below is fixed and verified.
#
# FLAW: it does `rm -rf $b/audio` then runs `MBM_TTS=eleven python3 make_narration.py`
# — but NOTHING reads MBM_TTS (no router exists in mbm_caption_timing.py), so
# make_narration silently renders with the OLD edge-tts voice. Net effect: DELETE
# the paid ElevenLabs audio, replace with old voice, then mark .audio-eleven-done
# as if ElevenLabs ran. The real ElevenLabs renderer is voice_from_transcripts.py.
# FIX REQUIRED: call voice_from_transcripts.py (or wire the MBM_TTS router) and
# NEVER delete audio before the replacement is verified 44100.
# ============================================================================
echo "DISABLED: this script destroyed paid ElevenLabs audio — see header." >&2
exit 1
