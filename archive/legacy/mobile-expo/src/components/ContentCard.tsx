import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  Linking,
  StyleSheet,
  Alert,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { ContentItem } from '../data/content';
import { useAppStore } from '../store/useAppStore';
import { colors, spacing, radius } from '../theme';

interface Props {
  item:       ContentItem;
  onThumbsUp: (id: number) => void;
  onBookmark: (id: number) => void;
}

export default function ContentCard({ item, onThumbsUp, onBookmark }: Props) {
  const markOpened = useAppStore(s => s.markOpened);

  const [thumbed,   setThumbed]   = useState(false);
  const [bookmarked, setBookmarked] = useState(false);

  async function handleRead() {
    try {
      const supported = await Linking.canOpenURL(item.url);
      if (supported) {
        await Linking.openURL(item.url);
        markOpened(item.id);
      } else {
        Alert.alert('Cannot open link', item.url);
      }
    } catch {
      Alert.alert('Error', 'Could not open this link.');
    }
  }

  function handleThumbsUp() {
    if (thumbed) return;
    setThumbed(true);
    onThumbsUp(item.id);
  }

  function handleBookmark() {
    if (bookmarked) return;
    setBookmarked(true);
    onBookmark(item.id);
  }

  return (
    <View style={styles.card}>
      {/* ── Meta row ─────────────────────────────────────────────────────── */}
      <View style={styles.meta}>
        <Text style={styles.ref}>{item.scriptureRef}</Text>
        <Text style={styles.readTime}>{item.estimatedMinutes} min</Text>
      </View>

      {/* ── Title ────────────────────────────────────────────────────────── */}
      <Text style={styles.title}>{item.title}</Text>

      {/* ── Description ──────────────────────────────────────────────────── */}
      <Text style={styles.description}>{item.description}</Text>

      {/* ── Actions ──────────────────────────────────────────────────────── */}
      <View style={styles.actions}>
        <TouchableOpacity
          style={styles.readBtn}
          activeOpacity={0.7}
          onPress={handleRead}
        >
          <Text style={styles.readBtnText}>Read →</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.iconBtn, thumbed && styles.iconBtnActive]}
          activeOpacity={0.7}
          onPress={handleThumbsUp}
        >
          <Ionicons
            name={thumbed ? 'heart' : 'heart-outline'}
            size={18}
            color={thumbed ? colors.gold : colors.textMuted}
          />
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.iconBtn, bookmarked && styles.iconBtnActive]}
          activeOpacity={0.7}
          onPress={handleBookmark}
        >
          <Ionicons
            name={bookmarked ? 'bookmark' : 'bookmark-outline'}
            size={18}
            color={bookmarked ? colors.gold : colors.textMuted}
          />
        </TouchableOpacity>
      </View>
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
  meta: {
    flexDirection:  'row',
    justifyContent: 'space-between',
    alignItems:     'center',
    marginBottom:   6,
  },
  ref: {
    fontSize:      11,
    color:         colors.textMuted,
    letterSpacing: 1.2,
    textTransform: 'uppercase',
    fontFamily:    'Georgia',
  },
  readTime: {
    fontSize:  11,
    color:     colors.textMuted,
    fontFamily: 'Georgia',
  },
  title: {
    fontSize:     17,
    fontFamily:   'Georgia',
    color:        '#e8e0c8',
    marginBottom: 8,
    lineHeight:   24,
  },
  description: {
    fontSize:     13,
    fontFamily:   'Georgia',
    color:        colors.textDim,
    lineHeight:   21,
    marginBottom: spacing.md,
  },
  actions: {
    flexDirection: 'row',
    alignItems:    'center',
    gap:           spacing.sm,
  },
  readBtn: {
    flex:        1,
    borderBottomWidth: 1,
    borderBottomColor: colors.textMuted,
    paddingBottom:     1,
  },
  readBtnText: {
    color:      colors.gold,
    fontSize:   13,
    fontFamily: 'Georgia',
  },
  iconBtn: {
    padding:      8,
    borderWidth:  1,
    borderColor:  colors.borderDim,
    borderRadius: radius.sm,
  },
  iconBtnActive: {
    borderColor: colors.gold,
  },
});
