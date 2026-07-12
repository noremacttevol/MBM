/**
 * LockedVideoPlayer — the full-screen, no-controls player for Feed 2.0 videos.
 *
 * FEED-2.0-SPEC §3 (Video playback law):
 *   - Tapping a video plays it full-screen with NO controls: no pause, no seek,
 *     no scrub, no skip. The app does nothing else until the video completes.
 *   - Leaving the app (backgrounding it, not closing) pauses implicitly; on
 *     return the video rewinds 5 seconds and resumes.
 *   - Only a 100% watch counts as viewed → onComplete() fires once, and the
 *     caller honors the video.
 *
 *   Flagged risk (logged in the spec): a media view without a pause control can
 *   draw App Store review friction. The pre-approved fallback is PAUSE_FALLBACK
 *   below — one flag that allows pause ONLY (still no seek/skip; a paused video
 *   earns nothing until finished). Ship locked; flip only if review requires it.
 */

import React, { useEffect, useRef, useState } from 'react';
import {
  Modal,
  View,
  Text,
  StyleSheet,
  AppState,
  AppStateStatus,
  TouchableWithoutFeedback,
  ActivityIndicator,
} from 'react-native';
import { VideoView, useVideoPlayer } from 'expo-video';
import { useEventListener } from 'expo';
import { colors } from '../theme';

// SPEC §3 contingency flag. false = fully locked (ship this). true = pause-only
// fallback, enabled ONLY if App Store review rejects the no-pause player.
export const PAUSE_FALLBACK = false;

// How far to rewind (seconds) when the app returns to the foreground.
const RESUME_REWIND_SECONDS = 5;

interface Props {
  uri:        string;
  visible:    boolean;
  onComplete: () => void;   // fired once when the video reaches 100%
  onError?:   () => void;   // playback failed — caller should close and fall back to the verse
}

export default function LockedVideoPlayer({ uri, visible, onComplete, onError }: Props) {
  const completedRef = useRef(false);
  const [paused, setPaused] = useState(false);

  const player = useVideoPlayer(uri, p => {
    p.timeUpdateEventInterval = 0.5;
    p.play();
  });

  // 100% watch — the only thing that counts as viewed. Fire onComplete exactly once.
  useEventListener(player, 'playToEnd', () => {
    if (completedRef.current) return;
    completedRef.current = true;
    onComplete();
  });

  // Surface fatal playback errors so the caller can close and show the verse only.
  useEventListener(player, 'statusChange', ({ status }) => {
    if (status === 'error' && onError) onError();
  });

  // Rewind-5-and-resume when the app comes back to the foreground (SPEC §3).
  useEffect(() => {
    const sub = AppState.addEventListener('change', (next: AppStateStatus) => {
      if (next === 'active' && !completedRef.current && !paused) {
        try {
          player.currentTime = Math.max(0, player.currentTime - RESUME_REWIND_SECONDS);
          player.play();
        } catch { /* player may be released — ignore */ }
      }
    });
    return () => sub.remove();
  }, [player, paused]);

  // Reset the one-shot completion guard whenever a new video is opened.
  useEffect(() => {
    if (visible) { completedRef.current = false; setPaused(false); }
  }, [visible, uri]);

  function handleTap() {
    // Fully locked by default: a tap does nothing (no pause/seek/skip). With the
    // review fallback enabled, a tap toggles pause ONLY.
    if (!PAUSE_FALLBACK) return;
    try {
      if (paused) { player.play(); setPaused(false); }
      else        { player.pause(); setPaused(true); }
    } catch { /* ignore */ }
  }

  return (
    <Modal
      visible={visible}
      animationType="fade"
      supportedOrientations={['portrait', 'landscape']}
      // Hardware back must NOT skip the video (SPEC §3: nothing until it completes).
      onRequestClose={() => { /* intentionally inert */ }}
    >
      <TouchableWithoutFeedback onPress={handleTap}>
        <View style={styles.fill}>
          <VideoView
            style={styles.fill}
            player={player}
            nativeControls={false}
            allowsFullscreen={false}
            allowsPictureInPicture={false}
            contentFit="contain"
          />
          {paused && (
            <View style={styles.pausedOverlay} pointerEvents="none">
              <Text style={styles.pausedText}>Paused — tap to keep watching</Text>
            </View>
          )}
          {!player.duration && (
            <View style={styles.loading} pointerEvents="none">
              <ActivityIndicator color={colors.gold} />
            </View>
          )}
        </View>
      </TouchableWithoutFeedback>
    </Modal>
  );
}

const styles = StyleSheet.create({
  fill: { flex: 1, backgroundColor: '#000' },
  loading: {
    ...StyleSheet.absoluteFillObject,
    alignItems: 'center',
    justifyContent: 'center',
  },
  pausedOverlay: {
    ...StyleSheet.absoluteFillObject,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'rgba(0,0,0,0.45)',
  },
  pausedText: {
    color: colors.goldLight,
    fontSize: 14,
    fontFamily: 'Jost_400Regular',
  },
});
