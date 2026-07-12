/**
 * VerseBlock — a KJV verse, shown beneath a video or standing alone on a page.
 *
 * HYBRID scripture display (Cameron's call, 2026-07-11): milk verses we already
 * bundle render INLINE from the public-domain KJV (kjvText.ts) — a seeker never
 * leaves the app for a foundational verse. Verses we don't bundle link OUT to the
 * approved source (Bible Gateway KJV). EITHER WAY, the "Read it" action is what
 * HONORS the verse (FEED-2.0-SPEC §2) — it calls onRead().
 *
 * The verse honors SEPARATELY from its paired video, so a watched-but-skipped
 * verse can recycle back later. When it does, `reminderTitle` is set and the
 * block shows the gentle "you watched this story — here is its verse" line.
 */

import React, { useState } from 'react';
import { View, Text, TouchableOpacity, Linking, StyleSheet, Alert } from 'react-native';
import { kjvVersesFor } from '../data/kjvText';
import { verseGatewayUrl } from '../data/videos';
import InteractionRow from './InteractionRow';
import { InteractionKind } from '../store/useAppStore';
import { colors, spacing } from '../theme';

interface Props {
  scriptureRef:  string;
  /** CONTENT id, when the verse is in the bundled inline KJV. */
  contentId?:    number;
  honored:       boolean;
  /** Honor the verse (open its link / expand it). Called on the first Read tap. */
  onRead:        () => void;
  /** Deep-link target so a saved verse can return to this spot. */
  pageRef:       { pageIndex: number; slotId: string };
  /** Set when this verse was recycled after its video was watched but it was skipped. */
  reminderTitle?: string;
  /** 'verse' for standalone/recycled; the pair passes 'verse' too — kept for clarity. */
  interactionKind?: InteractionKind;
  /**
   * Rev 1 §5: a video+verse PAIR carries ONE interaction row (on the pair), so
   * the paired VerseBlock hides its own. Standalone verses keep theirs.
   */
  showInteractionRow?: boolean;
  /**
   * Rev 2: the personally-made question this verse carries — how Jesus is found
   * to be a good God here. Shown above the row; Reply answers it.
   */
  question?: string;
}

const VERSE_PREVIEW = 6; // collapse long passages to this many verses first

export default function VerseBlock({
  scriptureRef, contentId, honored, onRead, pageRef, reminderTitle,
  interactionKind = 'verse', showInteractionRow = true, question,
}: Props) {
  const verses = contentId != null ? kjvVersesFor(contentId) : undefined;
  const hasInline = !!(verses && verses.length > 0);

  const [expanded, setExpanded] = useState(false);
  const [showAll, setShowAll]   = useState(false);

  async function handleRead() {
    onRead(); // honor the verse either way (the spec: opening/reading is honoring)
    if (hasInline) {
      setExpanded(true);
    } else {
      try {
        await Linking.openURL(verseGatewayUrl(scriptureRef));
      } catch {
        Alert.alert('Could not open this verse', scriptureRef);
      }
    }
  }

  const shown = verses ? (showAll ? verses : verses.slice(0, VERSE_PREVIEW)) : [];

  return (
    <View style={styles.wrap}>
      {reminderTitle && (
        <Text style={styles.reminder}>
          You watched “{reminderTitle}.” Here is its verse.
        </Text>
      )}

      <View style={styles.head}>
        <Text style={styles.ref}>{scriptureRef}</Text>
        {honored && <Text style={styles.honored}>read ✓</Text>}
      </View>

      {hasInline && expanded && (
        <View style={styles.scripture}>
          {shown.map(v => {
            const num = v.ref.split(':')[1];
            return (
              <Text key={v.ref} style={styles.verse} selectable>
                {num ? <Text style={styles.verseNum}>{num} </Text> : null}
                {v.text}
              </Text>
            );
          })}
          {verses && verses.length > VERSE_PREVIEW && (
            <TouchableOpacity activeOpacity={0.7} onPress={() => setShowAll(s => !s)}>
              <Text style={styles.toggle}>
                {showAll ? 'Show less' : `Show all ${verses.length} verses →`}
              </Text>
            </TouchableOpacity>
          )}
          <Text style={styles.kjvTag}>King James Version</Text>
        </View>
      )}

      {!(hasInline && expanded) && (
        <TouchableOpacity activeOpacity={0.7} onPress={handleRead}>
          <Text style={styles.readLink}>
            {hasInline ? 'Read it →' : 'Read the verse →'}
          </Text>
        </TouchableOpacity>
      )}

      {question ? <Text style={styles.question}>{question}</Text> : null}

      {showInteractionRow && (
        <InteractionRow
          kind={interactionKind}
          title={scriptureRef}
          scriptureRef={scriptureRef}
          pageRef={pageRef}
          talkPrefill={`I just read ${scriptureRef}. Can we talk about it?`}
        />
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  wrap: {
    borderLeftWidth: 2,
    borderLeftColor: colors.borderDim,
    paddingLeft:     spacing.sm + 2,
    marginTop:       spacing.sm,
  },
  reminder: {
    fontSize:   11,
    fontStyle:  'italic',
    color:      colors.textDim,
    fontFamily: 'Jost_400Regular',
    marginBottom: 6,
    lineHeight: 17,
  },
  head: {
    flexDirection:  'row',
    justifyContent: 'space-between',
    alignItems:     'center',
    marginBottom:   4,
  },
  ref: {
    fontSize:      11,
    color:         colors.textMuted,
    letterSpacing: 1.2,
    textTransform: 'uppercase',
    fontFamily:    'Jost_400Regular',
  },
  honored: {
    fontSize:   10,
    color:      colors.green,
    fontFamily: 'Jost_400Regular',
  },
  readLink: {
    color:      colors.gold,
    fontSize:   13,
    fontFamily: 'Jost_400Regular',
    marginTop:  2,
  },
  scripture: { marginTop: 4 },
  verse: {
    fontSize:     14,
    fontFamily:   'Jost_400Regular',
    color:        '#d8d0b8',
    lineHeight:   23,
    marginBottom: 6,
  },
  verseNum: { fontSize: 10, color: colors.textMuted },
  toggle: {
    color:      colors.blue,
    fontSize:   11,
    fontStyle:  'italic',
    fontFamily: 'Jost_400Regular',
    marginTop:  2,
    marginBottom: 4,
  },
  question: {
    fontSize:   14,
    color:      colors.textMid,
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    lineHeight: 22,
    marginTop:  spacing.sm + 2,
  },
  kjvTag: {
    fontSize:      9,
    color:         colors.textMuted,
    letterSpacing: 1,
    textTransform: 'uppercase',
    fontFamily:    'Jost_400Regular',
    marginTop:     4,
  },
});
