/**
 * SaveNoteLink — the quiet "keep this" link that can sit on anything in the app
 * worth learning from (a reading, something the minister said, a story).
 *
 * Tapping it clips the source into a kept note (the store writes a short summary
 * of what to take from it), then carries the person to the Journal, which opens
 * to the note they just kept. So everything learnable has one tap to remember it.
 */

import React, { useState } from 'react';
import { Text, StyleSheet, TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { useAppStore, NoteSource } from '../store/useAppStore';
import { colors } from '../theme';

interface Props {
  source: NoteSource;
  title:  string;
  body:   string;
  label?: string;   // override the link text where a different verb reads better
}

export default function SaveNoteLink({ source, title, body, label }: Props) {
  const saveLearnedNote = useAppStore(s => s.saveLearnedNote);
  const navigation      = useNavigation<any>();
  const [saved, setSaved] = useState(false);

  function handleSave() {
    if (saved || !body.trim()) return;
    setSaved(true);
    saveLearnedNote({ source, title, body });
    // Navigate to the Journal tab; it reads pendingNoteId and opens to the note.
    navigation.navigate('Journal');
  }

  return (
    <TouchableOpacity activeOpacity={0.7} onPress={handleSave} disabled={saved}>
      <Text style={[styles.link, saved && styles.linkSaved]}>
        {saved ? 'Saved to your notes ✓' : (label ?? 'Save to my notes →')}
      </Text>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  link: {
    color:      colors.blue,
    fontSize:   11,
    fontStyle:  'italic',
    fontFamily: 'MBMCross',
  },
  linkSaved: {
    color: colors.textMuted,
  },
});
