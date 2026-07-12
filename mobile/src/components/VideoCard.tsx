/**
 * VideoCard — one video+verse pair on a prescribed page (FEED-2.0-SPEC §1).
 *
 * The animated Jesus-story video sits on top; its linked KJV verse sits beneath
 * (VerseBlock). The two HONOR SEPARATELY (§2): watching the video to 100% honors
 * the video; opening/reading the verse honors the verse. The story carries its
 * own interaction row; the verse carries its own (inside VerseBlock).
 *
 * Videos are produced in waves — until a clip exists (isVideoProduced), the card
 * shows the story title + its Seed question + the verse, and simply notes the
 * video is being prepared. The feed is fully usable before any .mp4 ships.
 */

import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { videoById, isVideoProduced, videoStreamUrl } from '../data/videos';
import { VideoPairItem } from '../engine/pageEngine';
import { useAppStore } from '../store/useAppStore';
import InteractionRow from './InteractionRow';
import VerseBlock from './VerseBlock';
import LockedVideoPlayer from './LockedVideoPlayer';
import { colors, spacing, radius } from '../theme';

interface Props {
  item:      VideoPairItem;
  pageIndex: number;
}

export default function VideoCard({ item, pageIndex }: Props) {
  const honorPageItem = useAppStore(s => s.honorPageItem);
  const video = videoById(item.videoId);
  const [playing, setPlaying] = useState(false);

  if (!video) return null;

  const produced = isVideoProduced(video.id) && !!(video.videoUrl ?? videoStreamUrl(video.id));
  const pageRef = { pageIndex, slotId: item.slotId };

  function openPlayer() {
    if (!produced) return;
    setPlaying(true);
  }
  function handleComplete() {
    honorPageItem(item.slotId, 'video');
    setPlaying(false);
  }
  function handleReadVerse() {
    honorPageItem(item.slotId, 'verse');
  }

  return (
    <View style={styles.card}>
      <Text style={styles.label}>A STORY</Text>

      {/* ── The video (or its placeholder until produced) ──────────────────── */}
      <TouchableOpacity
        activeOpacity={produced ? 0.85 : 1}
        onPress={openPlayer}
        disabled={!produced}
        style={styles.poster}
      >
        <Text style={styles.playGlyph}>{produced ? '▶' : '✧'}</Text>
        <Text style={styles.posterTitle}>{video.title}</Text>
        {item.videoHonored
          ? <Text style={styles.watched}>watched ✓</Text>
          : <Text style={styles.posterHint}>
              {produced ? 'Tap to watch' : 'Video in production — its verse is below'}
            </Text>}
      </TouchableOpacity>

      {/* ── The Seed question the story leaves behind ──────────────────────── */}
      <Text style={styles.seed}>{video.seedQuestion}</Text>

      {/* ── Story interaction row (reflect / talk / save) ──────────────────── */}
      <InteractionRow
        kind="video"
        title={video.title}
        scriptureRef={video.scriptureRef}
        pageRef={pageRef}
        talkPrefill={`I just watched “${video.title}” (${video.scriptureRef}). Can we talk about it?`}
        reflectPlaceholder="What did the story stir? A line is plenty."
      />

      {/* ── The paired verse, honored separately ───────────────────────────── */}
      <VerseBlock
        scriptureRef={video.scriptureRef}
        contentId={item.verseContentId}
        honored={item.verseHonored}
        onRead={handleReadVerse}
        pageRef={pageRef}
      />

      {playing && video.videoUrl && (
        <LockedVideoPlayer
          uri={video.videoUrl}
          visible={playing}
          onComplete={handleComplete}
          onError={() => setPlaying(false)}
        />
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: colors.bgCard,
    borderWidth:     1,
    borderColor:     colors.border,
    borderRadius:    radius.md,
    padding:         spacing.md,
    marginBottom:    spacing.sm + 4,
  },
  label: {
    fontSize:      10,
    letterSpacing: 1.5,
    color:         colors.textMuted,
    fontFamily:    'Jost_400Regular',
    marginBottom:  spacing.sm,
  },
  poster: {
    borderWidth:     1,
    borderColor:     colors.borderDim,
    borderRadius:    radius.sm,
    backgroundColor: '#0d0c0a',
    paddingVertical: spacing.lg,
    paddingHorizontal: spacing.md,
    alignItems:      'center',
    justifyContent:  'center',
    minHeight:       120,
  },
  playGlyph: {
    fontSize:   26,
    color:      colors.gold,
    marginBottom: 8,
  },
  posterTitle: {
    fontSize:   16,
    color:      '#e8e0c8',
    fontFamily: 'Jost_400Regular',
    textAlign:  'center',
    marginBottom: 6,
    lineHeight: 22,
  },
  posterHint: {
    fontSize:   11,
    color:      colors.textMuted,
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    textAlign:  'center',
  },
  watched: {
    fontSize:   11,
    color:      colors.green,
    fontFamily: 'Jost_400Regular',
  },
  seed: {
    fontSize:     14,
    color:        colors.textMid,
    fontFamily:   'Jost_400Regular',
    fontStyle:    'italic',
    lineHeight:   22,
    marginTop:    spacing.md,
  },
});
