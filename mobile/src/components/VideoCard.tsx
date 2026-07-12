/**
 * VideoCard — one video+verse pair on a prescribed page.
 *
 * Rev 1 (Cameron, 2026-07-12):
 *   §7 — looks like content, not a black box: a real THUMBNAIL (a frame cut from
 *        the video) that is tapped to play, headlined "A story about ___" with
 *        its scripture reference. No "A STORY" label, no "tap to watch" hint.
 *   §5 — ONE interaction row for the whole pair (the paired verse hides its own).
 *   §1 — opens the normal StoryVideoPlayer (pause/scrub/close); the watch is
 *        credited when the playhead reaches 90%, which honors the video half and
 *        lets the in-place replacement engine take over.
 *
 * Until a clip is produced, the card shows the seed question + verse and quietly
 * notes the story is coming — the feed works before any .mp4 exists.
 */

import React, { useState } from 'react';
import { View, Text, TouchableOpacity, Image, StyleSheet } from 'react-native';
import { videoById, isVideoProduced } from '../data/videos';
import { VideoPairItem } from '../engine/pageEngine';
import { useAppStore } from '../store/useAppStore';
import InteractionRow from './InteractionRow';
import VerseBlock from './VerseBlock';
import StoryVideoPlayer from './StoryVideoPlayer';
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

  const produced = isVideoProduced(video.id) && !!video.videoUrl;
  const pageRef = { pageIndex, slotId: item.slotId };

  return (
    <View style={styles.card}>
      {/* ── Headline: what the story is about, and where it comes from ─────── */}
      <View style={styles.headRow}>
        <Text style={styles.aboutTitle}>{video.aboutTitle}</Text>
        {item.videoHonored && <Text style={styles.watched}>watched ✓</Text>}
      </View>
      <Text style={styles.fromRef}>from {video.scriptureRef}</Text>

      {/* ── The thumbnail — tap it and the story plays ─────────────────────── */}
      {produced && video.thumbUrl ? (
        <TouchableOpacity activeOpacity={0.85} onPress={() => setPlaying(true)}>
          <Image source={{ uri: video.thumbUrl }} style={styles.thumb} resizeMode="cover" />
          <View style={styles.playBadge} pointerEvents="none">
            <Text style={styles.playGlyph}>▶</Text>
          </View>
        </TouchableOpacity>
      ) : (
        <View style={styles.comingSoon}>
          <Text style={styles.comingTitle}>{video.title}</Text>
          <Text style={styles.comingNote}>This story's film is being made — its verse is below.</Text>
        </View>
      )}

      {/* ── The Seed question the story leaves behind ──────────────────────── */}
      <Text style={styles.seed}>{video.seedQuestion}</Text>

      {/* ── The paired verse (no row of its own — the pair shares one) ─────── */}
      <VerseBlock
        scriptureRef={video.scriptureRef}
        contentId={item.verseContentId}
        honored={item.verseHonored}
        onRead={() => honorPageItem(item.slotId, 'verse')}
        pageRef={pageRef}
        showInteractionRow={false}
      />

      {/* ── ONE interaction row for the whole pair (Rev 1 §5) ──────────────── */}
      <InteractionRow
        kind="video"
        title={video.aboutTitle}
        scriptureRef={video.scriptureRef}
        pageRef={pageRef}
        talkPrefill={`I just watched “${video.title}” (${video.scriptureRef}). Can we talk about it?`}
        reflectPlaceholder='e.g. “I always pictured God waiting with his arms folded. This one felt different.”'
      />

      {playing && video.videoUrl && (
        <StoryVideoPlayer
          uri={video.videoUrl}
          visible={playing}
          onCredit={() => honorPageItem(item.slotId, 'video')}
          onClose={() => setPlaying(false)}
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
  headRow: {
    flexDirection:  'row',
    justifyContent: 'space-between',
    alignItems:     'flex-start',
    gap:            spacing.sm,
  },
  aboutTitle: {
    flex:       1,
    fontSize:   17,
    color:      '#e8e0c8',
    fontFamily: 'Jost_400Regular',
    lineHeight: 24,
  },
  watched: {
    fontSize:   11,
    color:      colors.green,
    fontFamily: 'Jost_400Regular',
    marginTop:  4,
  },
  fromRef: {
    fontSize:      11,
    color:         colors.textMuted,
    letterSpacing: 1,
    textTransform: 'uppercase',
    fontFamily:    'Jost_400Regular',
    marginTop:     2,
    marginBottom:  spacing.sm + 2,
  },

  thumb: {
    width:        '100%',
    aspectRatio:  9 / 12,   // tall crop of the 9:16 frame — big without eating the page
    borderRadius: radius.sm,
    backgroundColor: '#0d0c0a',
  },
  playBadge: {
    position:  'absolute',
    top:       '50%',
    left:      '50%',
    marginTop: -26,
    marginLeft: -26,
    width:     52,
    height:    52,
    borderRadius: 26,
    backgroundColor: 'rgba(10,10,15,0.62)',
    borderWidth: 1,
    borderColor: colors.gold,
    alignItems: 'center',
    justifyContent: 'center',
  },
  playGlyph: {
    color:    colors.goldLight,
    fontSize: 20,
    marginLeft: 3,
  },

  comingSoon: {
    borderWidth:     1,
    borderColor:     colors.borderDim,
    borderRadius:    radius.sm,
    backgroundColor: '#0d0c0a',
    paddingVertical: spacing.lg,
    paddingHorizontal: spacing.md,
    alignItems:      'center',
  },
  comingTitle: {
    fontSize:   15,
    color:      '#e8e0c8',
    fontFamily: 'Jost_400Regular',
    textAlign:  'center',
    marginBottom: 4,
  },
  comingNote: {
    fontSize:   11,
    color:      colors.textMuted,
    fontStyle:  'italic',
    fontFamily: 'Jost_400Regular',
    textAlign:  'center',
  },

  seed: {
    fontSize:   14,
    color:      colors.textMid,
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    lineHeight: 22,
    marginTop:  spacing.md,
  },
});
