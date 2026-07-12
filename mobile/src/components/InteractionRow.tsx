/**
 * InteractionRow — the quiet Reply / Talk About It / Save it row under every
 * Feed 2.0 item. ONE row per video+verse pair (Rev 1 §5) — the pair saves as a
 * single entry; standalone verses, questions, and invitations carry their own.
 *
 * Rev 2 (Cameron, 2026-07-12): the reflect action is called REPLY everywhere —
 * it answers the question the content poses (the seed question sitting above
 * the row). The reply box opens with a grey EXAMPLE answer that disappears the
 * moment they type. Replying or saving marks the slot "interacted", which is
 * what earns the scroll-past replacement.
 *
 * Routing is BY BUTTON (Rev 1 §5):
 *   - Reply         → inline box; on Keep it lands on the PROFILE (their record).
 *   - Talk About It → prefills the conversation tab and opens it.
 *   - Save it       → lands in the JOURNAL, short title + link back to the feed.
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
  /** Where this item lives, so a saved entry can deep-link back to it. */
  pageRef?:      { pageIndex: number; slotId: string };
  reflectPlaceholder?: string;
}

export default function InteractionRow({
  kind, title, scriptureRef, talkPrefill, pageRef, reflectPlaceholder,
}: Props) {
  const saveInteraction    = useAppStore(s => s.saveInteraction);
  const markSlotInteracted = useAppStore(s => s.markSlotInteracted);
  const prefillChat        = useAppStore(s => s.prefillChat);
  const navigation       = useNavigation<any>();

  const [reflectOpen, setReflectOpen] = useState(false);
  const [reflectText, setReflectText] = useState('');
  const [saved, setSaved]             = useState(false);
  const [reflected, setReflected]     = useState(false);

  function go(dest: 'journal' | 'profile') {
    navigation.navigate(dest === 'profile' ? 'Profile' : 'Journal');
  }

  function handleReflectKeep() {
    if (!reflectText.trim()) return;
    const dest = saveInteraction({
      action: 'reflect', kind, title, scriptureRef,
      reflection: reflectText.trim(), pageRef,
    });
    setReflectText('');
    setReflectOpen(false);
    setReflected(true);
    if (pageRef) markSlotInteracted(pageRef.slotId);
    go(dest);
  }

  function handleTalk() {
    prefillChat(talkPrefill);
    navigation.navigate('Chat');
  }

  function handleSave() {
    if (saved) return;
    setSaved(true);
    const dest = saveInteraction({ action: 'save', kind, title, scriptureRef, pageRef });
    if (pageRef) markSlotInteracted(pageRef.slotId);
    go(dest);
  }

  return (
    <View>
      <View style={styles.subActions}>
        <TouchableOpacity activeOpacity={0.7} onPress={() => setReflectOpen(o => !o)}>
          <Text style={[styles.subActionText, reflected && styles.doneText]}>
            {reflected ? 'Replied ✓' : 'Reply →'}
          </Text>
        </TouchableOpacity>
        <TouchableOpacity activeOpacity={0.7} onPress={handleTalk}>
          <Text style={styles.subActionText}>Talk About It →</Text>
        </TouchableOpacity>
        <TouchableOpacity activeOpacity={0.7} onPress={handleSave} disabled={saved}>
          <Text style={[styles.subActionText, saved && styles.doneText]}>
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
            placeholder={reflectPlaceholder ?? 'e.g. “I have read this before, but today it felt like it was about me.”'}
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
  doneText: { color: colors.textMuted },

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
