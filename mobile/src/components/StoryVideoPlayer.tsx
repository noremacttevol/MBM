/**
 * StoryVideoPlayer — the full-screen player for Feed 2.0 story videos.
 *
 * REV 1 §1 (Cameron, 2026-07-12 — reverses the original locked-player law):
 * a REAL little player. Native controls: pause, scrub back and forth, play —
 * and a close button so the person can always go back. Watching is invited,
 * never forced.
 *
 * Credit rule: the watch is credited (onCredit, once) when the playhead
 * REACHES THE 90% MARK — Cameron's explicit choice. Close before 90% → no
 * credit, and the story stays in the person's new content.
 */

import React, { useEffect, useRef } from 'react';
import {
  Modal,
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ActivityIndicator,
} from 'react-native';
import { VideoView, useVideoPlayer } from 'expo-video';
import { useEventListener } from 'expo';
import { colors } from '../theme';

const CREDIT_AT = 0.9; // playhead reaching 90% of duration = a credited watch

interface Props {
  uri:      string;
  visible:  boolean;
  onCredit: () => void;   // fired once when the playhead reaches the 90% mark
  onClose:  () => void;   // the person is always free to leave
  onError?: () => void;   // playback failed — close and fall back to the verse
}

export default function StoryVideoPlayer({ uri, visible, onCredit, onClose, onError }: Props) {
  const creditedRef = useRef(false);

  const player = useVideoPlayer(uri, p => {
    p.timeUpdateEventInterval = 0.5;
    p.play();
  });

  // Credit at the 90% mark — however the playhead got there (Cameron's call).
  useEventListener(player, 'timeUpdate', ({ currentTime }) => {
    if (creditedRef.current) return;
    const dur = player.duration;
    if (dur > 0 && currentTime >= dur * CREDIT_AT) {
      creditedRef.current = true;
      onCredit();
    }
  });

  // Reaching the very end also credits (covers a missed timeUpdate at the tail).
  useEventListener(player, 'playToEnd', () => {
    if (!creditedRef.current) {
      creditedRef.current = true;
      onCredit();
    }
    onClose(); // finished — return them to the feed
  });

  useEventListener(player, 'statusChange', ({ status }) => {
    if (status === 'error' && onError) onError();
  });

  // New video opened → fresh one-shot credit guard.
  useEffect(() => {
    if (visible) creditedRef.current = false;
  }, [visible, uri]);

  return (
    <Modal
      visible={visible}
      animationType="fade"
      supportedOrientations={['portrait', 'landscape']}
      onRequestClose={onClose}   // hardware back goes back, like anywhere else
    >
      <View style={styles.fill}>
        <VideoView
          style={styles.fill}
          player={player}
          nativeControls
          allowsFullscreen={false}
          allowsPictureInPicture={false}
          contentFit="contain"
        />
        {!player.duration && (
          <View style={styles.loading} pointerEvents="none">
            <ActivityIndicator color={colors.gold} />
          </View>
        )}
        <TouchableOpacity
          style={styles.closeBtn}
          activeOpacity={0.8}
          onPress={onClose}
          accessibilityLabel="Close video"
        >
          <Text style={styles.closeGlyph}>✕</Text>
        </TouchableOpacity>
      </View>
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
  closeBtn: {
    position: 'absolute',
    top: 46,
    left: 18,
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: 'rgba(0,0,0,0.55)',
    alignItems: 'center',
    justifyContent: 'center',
  },
  closeGlyph: {
    color: '#e8e4d8',
    fontSize: 18,
    fontFamily: 'Jost_400Regular',
  },
});
