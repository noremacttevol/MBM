import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  Linking,
  StyleSheet,
  Alert,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useNavigation } from '@react-navigation/native';
import { ContentItem } from '../data/content';
import { useAppStore } from '../store/useAppStore';
import SaveNoteLink from './SaveNoteLink';
import { colors, spacing, radius } from '../theme';

interface Props {
  item:       ContentItem;
  onThumbsUp: (id: number) => void;
  onBookmark: (id: number) => void;
}

export default function ContentCard({ item, onThumbsUp, onBookmark }: Props) {
  const markOpened       = useAppStore(s => s.markOpened);
  const reflectOnContent = useAppStore(s => s.reflectOnContent);
  const prefillChat      = useAppStore(s => s.prefillChat);
  const navigation       = useNavigation<any>();

  const [thumbed,   setThumbed]   = useState(false);
  const [bookmarked, setBookmarked] = useState(false);
  const [reflectOpen, setReflectOpen] = useState(false);
  const [reflectText, setReflectText] = useState('');

  async function handleRead() {
    // No canOpenURL() gate: on Android it falsely returns false for
    // churchofjesuschrist.org (registered app-links), which blocked those links
    // from ever opening. openURL resolves https to a browser on its own.
    try {
      await Linking.openURL(item.url);
      markOpened(item.id);
    } catch {
      Alert.alert('Could not open this link', item.url);
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

  function handleReflectSave() {
    if (!reflectText.trim()) return;
    reflectOnContent(item, reflectText.trim());
    setReflectText('');
    setReflectOpen(false);
  }

  function handleTalkAbout() {
    prefillChat(`I just read “${item.title}” (${item.scriptureRef}). Can we talk about it?`);
    navigation.navigate('Chat');
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

      {/* ── Reflect / Talk / Keep — quiet invitations under each card ──────── */}
      <View style={styles.subActions}>
        <TouchableOpacity activeOpacity={0.7} onPress={() => setReflectOpen(o => !o)}>
          <Text style={styles.subActionText}>Reflect on this →</Text>
        </TouchableOpacity>
        <TouchableOpacity activeOpacity={0.7} onPress={handleTalkAbout}>
          <Text style={styles.subActionText}>Talk about it →</Text>
        </TouchableOpacity>
        <SaveNoteLink
          source="feed"
          title={item.title}
          body={`${item.title} (${item.scriptureRef})\n\n${item.description}`}
        />
      </View>

      {reflectOpen && (
        <View style={styles.reflectBox}>
          <TextInput
            style={styles.reflectInput}
            value={reflectText}
            onChangeText={setReflectText}
            placeholder="What does it stir? A line is plenty."
            placeholderTextColor={colors.textMuted}
            multiline
            textAlignVertical="top"
          />
          <TouchableOpacity
            style={[styles.keepBtn, !reflectText.trim() && styles.keepBtnDisabled]}
            activeOpacity={0.7}
            onPress={handleReflectSave}
            disabled={!reflectText.trim()}
          >
            <Text style={styles.keepBtnText}>Keep it →</Text>
          </TouchableOpacity>
        </View>
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
    fontFamily:    'Jost_400Regular',
  },
  readTime: {
    fontSize:  11,
    color:     colors.textMuted,
    fontFamily: 'Jost_400Regular',
  },
  title: {
    fontSize:     17,
    fontFamily:   'Jost_400Regular',
    color:        '#e8e0c8',
    marginBottom: 8,
    lineHeight:   24,
  },
  description: {
    fontSize:     13,
    fontFamily:   'Jost_400Regular',
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
    fontFamily: 'Jost_400Regular',
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

  subActions: {
    flexDirection: 'row',
    flexWrap:      'wrap',
    gap:           spacing.md,
    rowGap:        8,
    marginTop:     10,
  },
  subActionText: {
    color:      colors.blue,
    fontSize:   11,
    fontStyle:  'italic',
    fontFamily: 'Jost_400Regular',
  },

  reflectBox: { marginTop: 10 },
  reflectInput: {
    width:           '100%',
    borderWidth:     1,
    borderColor:     '#1e1c18',
    borderRadius:    4,
    backgroundColor: colors.bgInput,
    color:           '#d0c8b0',
    fontSize:        13,
    fontFamily:      'Jost_400Regular',
    padding:         spacing.sm,
    minHeight:       56,
    marginBottom:    spacing.sm,
    lineHeight:      19,
  },
  keepBtn: {
    alignSelf:         'flex-end',
    borderWidth:       1,
    borderColor:       colors.gold,
    borderRadius:      4,
    paddingVertical:   6,
    paddingHorizontal: 14,
  },
  keepBtnDisabled: { borderColor: colors.borderDim },
  keepBtnText: { color: colors.gold, fontSize: 12, fontFamily: 'Jost_400Regular' },
});
