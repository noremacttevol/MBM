/**
 * InteractionRow — the quiet Reflect / Talk About It / Save it row that Feed 2.0
 * puts under EVERY item: videos, verses, stories, questions, invitations.
 *
 * It mirrors the row already built into ContentCard (kept working, untouched) but
 * is content-kind aware so saves land in the right place (FEED-2.0-SPEC §5,
 * handoff): reflections on SCRIPTURE or STORIES → the Journal; interactions with
 * QUESTIONS or INVITATIONS → the Profile. The store's saveInteraction() does the
 * routing and hands back the destination tab so we navigate there.
 *
 *   - Reflect on this →  inline box; on Keep the reflection is saved.
 *   - Talk About It →    prefills the AI-minister chat and opens it.
 *   - Save it →          saves the item itself.
 */

import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { useAppStore, InteractionKind } from '../store/useAppStore';
import { colors, spacing } from '../theme';

interface Props {
  kind:          InteractionKind;
  title:         string;
  /** Scripture reference, when the item has one (verses, video pairs). */
  scriptureRef?: string;
  /** Prefill for "Talk About It" — e.g. "I just watched … Can we talk about it?" */
  talkPrefill:   string;
  /** Where this item lives, so a saved verse can deep-link back to it. */
  pageRef?:      { pageIndex: number; slotId: string };
  reflectPlaceholder?: string;
}

export default function InteractionRow({
  kind, title, scriptureRef, talkPrefill, pageRef, reflectPlaceholder,
}: Props) {
  const saveInteraction = useAppStore(s => s.saveInteraction);
  const prefillChat      = useAppStore(s => s.prefillChat);
  const navigation       = useNavigation<any>();

  const [reflectOpen, setReflectOpen] = useState(false);
  const [reflectText, setReflectText] = useState('');
  const [saved, setSaved]             = useState(false);

  function go(dest: 'journal' | 'profile') {
    navigation.navigate(dest === 'profile' ? 'Profile' : 'Journal');
  }

  function handleReflectKeep() {
    if (!reflectText.trim()) return;
    const dest = saveInteraction({ kind, title, scriptureRef, reflection: reflectText.trim(), pageRef });
    setReflectText('');
    setReflectOpen(false);
    go(dest);
  }

  function handleTalk() {
    prefillChat(talkPrefill);
    navigation.navigate('Chat');
  }

  function handleSave() {
    if (saved) return;
    setSaved(true);
    const dest = saveInteraction({ kind, title, scriptureRef, pageRef });
    go(dest);
  }

  return (
    <View>
      <View style={styles.subActions}>
        <TouchableOpacity activeOpacity={0.7} onPress={() => setReflectOpen(o => !o)}>
          <Text style={styles.subActionText}>Reflect on this →</Text>
        </TouchableOpacity>
        <TouchableOpacity activeOpacity={0.7} onPress={handleTalk}>
          <Text style={styles.subActionText}>Talk About It →</Text>
        </TouchableOpacity>
        <TouchableOpacity activeOpacity={0.7} onPress={handleSave} disabled={saved}>
          <Text style={[styles.subActionText, saved && styles.savedText]}>
            {saved ? 'Saved ✓' : 'Save it →'}
          </Text>
        </TouchableOpacity>
      </View>

      {reflectOpen && (
        <View style={styles.reflectBox}>
          <TextInput
            style={styles.reflectInput}
            value={reflectText}
            onChangeText={setReflectText}
            placeholder={reflectPlaceholder ?? 'What does it stir? A line is plenty.'}
            placeholderTextColor={colors.textMuted}
            multiline
            textAlignVertical="top"
          />
          <TouchableOpacity
            style={[styles.keepBtn, !reflectText.trim() && styles.keepBtnDisabled]}
            activeOpacity={0.7}
            onPress={handleReflectKeep}
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
  savedText: { color: colors.textMuted },

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
