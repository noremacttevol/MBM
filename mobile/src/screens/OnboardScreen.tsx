/**
 * OnboardScreen — story-first onboarding per CLAUDE.md Jesus Method rules.
 *
 * 9 entry stories. Each one reaches a different kind of person.
 * Story → question from inside the story → reflection back → silent feed routing.
 * The user never knows they have been categorized.
 */

import React, { useState, useRef, useEffect } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  TextInput,
  ScrollView,
  StyleSheet,
  Animated,
  KeyboardAvoidingView,
  Platform,
} from 'react-native';
import { NativeStackScreenProps } from '@react-navigation/native-stack';
import { StatusBar } from 'expo-status-bar';
import { RootStackParamList } from '../navigation/AppNavigator';
import { useAppStore } from '../store/useAppStore';
import { FeedTag } from '../data/content';
import { colors, spacing, radius } from '../theme';

type Props = NativeStackScreenProps<RootStackParamList, 'Onboard'>;

// ── Story pool ────────────────────────────────────────────────────────────────

interface StoryChoice {
  key: string;
  text: string;
  signal: string;
  feedTag: FeedTag;
  reflection: string;
}

interface Story {
  id: string;
  narrative: string[];
  question: string;
  choices: StoryChoice[];
  otherReflection: string;
}

const STORIES: Story[] = [
  // 1 ── Woman who touched his cloak ─────────────────────────────────────────
  {
    id: 'cloak',
    narrative: [
      'There was a woman who had been suffering for twelve years.',
      'She had spent everything on doctors. Nothing helped. She was exhausted, desperate — and by the rules of her time, considered untouchable.',
      'She heard Jesus was nearby. She did not ask permission. She did not make a speech. She pressed through the crowd and reached out to touch the edge of his cloak.',
      'He stopped. He turned. In a crowd of dozens pressing against him, he felt her reach. He looked for her until he found her.',
      'He called her daughter.',
    ],
    question: 'Have you ever been that desperate for something in your life to change — even if you had no words for it yet?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'carries_burden',
        text: 'Yes. I have been carrying something heavy for a long time.',
        reflection: "Thank you for sharing that. Carrying something heavy without knowing if anyone notices is one of the loneliest feelings there is. That is exactly the kind of weight Jesus paid attention to. You are in the right place.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'searching_for_purpose',
        text: "I have had moments like that — searching for something I couldn't name.",
        reflection: "Searching for something you can't quite name is its own kind of faith — reaching toward something real even when you don't have the words. That woman didn't have words either. She just reached.",
      },
      {
        key: 'C', feedTag: 'BRIDGE', signal: 'skeptical_of_god',
        text: 'I have big questions about whether reaching toward God actually does anything.',
        reflection: "That is an honest question and a fair one. She had every reason for the same doubt — twelve years of trying earthly answers with nothing to show for it. Let's start with the honest questions.",
      },
      {
        key: 'D', feedTag: 'MAINTENANCE', signal: 'covenant_intent',
        text: 'I already believe. I am here because I want to go deeper.',
        reflection: "Then you are in good company. Even those who walked closest to Jesus still had moments of reaching, still needed reminding of what they already knew. There is always more.",
      },
    ],
    otherReflection: "Thank you for putting that into your own words. That matters more than any pre-written answer. What you shared — ",
  },

  // 2 ── The Prodigal Son ──────────────────────────────────────────────────────
  {
    id: 'prodigal',
    narrative: [
      'A father had two sons. The younger one asked for his inheritance early — essentially wishing his father were already dead — and left to spend everything on a life that emptied him.',
      'When he had nothing left and was starving, he came to his senses. He rehearsed a speech the whole walk home: "Make me one of your servants. I am not worthy to be called your son."',
      'He was still a long way off when his father saw him.',
      'The father ran. He didn\'t wait for the speech. He threw his arms around him before a single word was said.',
      '"This son of mine was dead and is alive again. He was lost and is found."',
    ],
    question: 'Which part of that story feels closest to something you have carried or are carrying right now?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'has_history_with_faith',
        text: 'The son who left — I have felt far from something I once had.',
        reflection: "Coming back is not failure. The father ran while the son was still far off — he didn't walk, didn't wait by the door. He ran. If you have been away from something, you are already on the road back just by being here.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'carries_shame',
        text: "The son rehearsing his speech — I feel like I would have to earn my way back.",
        reflection: "The father interrupted that speech. He never let the son finish it. Whatever you think you would have to say to earn your place — it doesn't work like that. That is the whole point of the story.",
      },
      {
        key: 'C', feedTag: 'MILK', signal: 'carries_grief',
        text: 'The father — I have waited for someone I love to come home.',
        reflection: "Waiting for someone is its own kind of grief that doesn't get talked about enough. The father in that story was watching, hoping, ready to run the moment he saw. You understand something about love that most people miss.",
      },
      {
        key: 'D', feedTag: 'BRIDGE', signal: 'open_to_god',
        text: 'I want to understand the character of the God behind this story.',
        reflection: "That is exactly the right question. Jesus told this story specifically to describe what the Father is actually like — not distant, not measuring, not waiting for you to get it right before he moves. Let's explore that together.",
      },
    ],
    otherReflection: "Thank you for saying it in your own words. That is exactly what the story was designed to invite — your real response, not the one you thought you were supposed to give. What you shared — ",
  },

  // 3 ── Zacchaeus ────────────────────────────────────────────────────────────
  {
    id: 'zacchaeus',
    narrative: [
      'Zacchaeus was a tax collector — which in his time meant he worked for the occupying empire and got rich doing it. He was publicly despised.',
      'When Jesus came through town, Zacchaeus wanted to see him. But he was short. He couldn\'t see over the crowd.',
      'So he ran ahead and climbed a tree. A grown man. A man of status. He climbed a tree just to catch a glimpse from a distance.',
      'Jesus looked up, saw him, and said: "Zacchaeus, come down. I am coming to your house today."',
      'Not after Zacchaeus changed. Not after he apologized. Before. He changed because Jesus came first.',
    ],
    question: 'Have you ever done something — maybe something a little embarrassing — just to get a look at something you thought might be real?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'searching_for_purpose',
        text: 'Yes — I have been watching from the edge, not sure if I belong in the crowd.',
        reflection: "Watching from the edge is not rejection — it is honesty. Zacchaeus didn't pretend to be someone he wasn't. He climbed the tree because something in him had to see. That impulse brought Jesus to his door.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'carries_shame',
        text: 'I have felt like the person everyone else has already written off.',
        reflection: "Jesus called Zacchaeus by name before Zacchaeus said a word. He wasn't written off. He was seen. The people around him had already decided who he was — Jesus ignored their verdict completely.",
      },
      {
        key: 'C', feedTag: 'BRIDGE', signal: 'honest_inquiry',
        text: "I am curious but I don't know if I believe any of this yet.",
        reflection: "Curiosity is enough to start with. Zacchaeus didn't have his theology sorted out — he climbed a tree. The reaching matters more than the certainty. We can start there.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'open_to_god',
        text: "I feel like something has been pulling me and I don't fully understand it.",
        reflection: "That pull is worth paying attention to. Zacchaeus couldn't explain it either — he just knew he needed to see. Something in him responded before his mind caught up. That is where the most real things often start.",
      },
    ],
    otherReflection: "Thank you for that. What you wrote is more honest than most people get in a first conversation. What you shared — ",
  },

  // 4 ── Nicodemus ────────────────────────────────────────────────────────────
  {
    id: 'nicodemus',
    narrative: [
      'Nicodemus was a Pharisee — a religious leader, educated, respected. He had everything to lose by being seen with Jesus.',
      'He came at night.',
      'He said: "No one could do what you do unless God were with him." Which meant he had already been thinking about it. He just couldn\'t say it in daylight.',
      'Jesus didn\'t turn him away for coming at night. He didn\'t point out the cowardice. He just answered the real question underneath the question.',
    ],
    question: 'Have you ever felt drawn toward something and been afraid to let anyone else see it?',
    choices: [
      {
        key: 'A', feedTag: 'BRIDGE', signal: 'honest_inquiry',
        text: 'Yes — I have questions I have been afraid to say out loud.',
        reflection: "Those are exactly the questions worth asking. Nicodemus came at night because his questions felt dangerous. Jesus met him anyway, completely, in the dark. The questions you are afraid to say out loud are the ones that matter most.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'searching_for_purpose',
        text: 'I have been curious about Jesus but never really let myself go there.',
        reflection: "That curiosity has been there for a reason. Nicodemus had been watching and thinking long before he showed up at the door. What you have been carrying quietly is worth exploring somewhere safe.",
      },
      {
        key: 'C', feedTag: 'BRIDGE', signal: 'skeptical_of_god',
        text: 'I am skeptical but something keeps bringing me back to these questions.',
        reflection: "Skepticism that keeps coming back is one of the most honest forms of searching there is. Nicodemus was trained to argue — and he still showed up. Let's follow that.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'carries_shame',
        text: 'I have a past that makes me feel like I am not the kind of person who belongs here.',
        reflection: "Nicodemus came in secret because he was afraid of what it would cost him publicly. Jesus never mentioned the secret. He just talked to him like he belonged. You do.",
      },
    ],
    otherReflection: "Thank you for that honesty. Coming at night — even figuratively — takes something. What you shared — ",
  },

  // 5 ── The Bent Woman ───────────────────────────────────────────────────────
  {
    id: 'bent_woman',
    narrative: [
      'There was a woman who had been bent over and unable to straighten up for eighteen years.',
      'Jesus was in the middle of teaching in the synagogue. He stopped, looked across the room, and called her over.',
      'She had not asked him anything. She had not pushed through a crowd. He called her first.',
      'He put his hands on her. She stood up straight for the first time in eighteen years.',
      'He called her a daughter of Abraham — which was a title, a declaration: you belong. You have always belonged. Before you were healed.',
    ],
    question: 'Is there something you have been carrying so long that you have stopped expecting it to change?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'carries_burden',
        text: 'Yes. There is something I have lived around for so long it feels normal.',
        reflection: "Eighteen years is a long time to learn to live around something. She had adapted. She wasn't even the one who initiated — Jesus called her over. Sometimes the healing starts before we ask for it.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'carries_grief',
        text: 'I have grieved something for so long I am not sure I know how to hope anymore.',
        reflection: "That kind of grief is real and it is heavy. She wasn't told to have more faith or try harder. He just called her over and addressed it directly. What you are carrying is not something you have to perform your way out of.",
      },
      {
        key: 'C', feedTag: 'BRIDGE', signal: 'open_to_god',
        text: 'I wonder sometimes if God notices the things people carry quietly.',
        reflection: "He noticed her across a crowded room while he was in the middle of something else. He stopped what he was doing and called her over. The quiet things — the things no one else sees — are exactly what he pays attention to.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'searching_for_purpose',
        text: 'I feel like I am waiting for something but I do not know what.',
        reflection: "She wasn't asking — she was just there, present, bent low. He called her anyway. Sometimes showing up, even in a bent-over way, is enough.",
      },
    ],
    otherReflection: "Thank you for that. Saying what we have adapted to is harder than it sounds. What you shared — ",
  },

  // 6 ── The Two Sons ─────────────────────────────────────────────────────────
  {
    id: 'two_sons',
    narrative: [
      'A father told his first son: Go work in the vineyard today. The son said, "I will not." Later he changed his mind and went.',
      'The father told his second son the same thing. That son said, "Yes, I will go." And didn\'t.',
      'Jesus asked the crowd: which one actually did the will of his father?',
      'The answer was the one who first said no.',
      '"Tax collectors and prostitutes are entering the kingdom of God ahead of you," he told the religious leaders who thought they were the second son.',
    ],
    question: 'Have you ever said no to something — maybe loudly — and found yourself moving toward it anyway because part of you couldn\'t let it go?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'has_history_with_faith',
        text: 'Yes — I have walked away from faith but I keep coming back to these questions.',
        reflection: "The son who said no and then went anyway was the one Jesus pointed to. The ones who said yes and didn't follow through weren't the example. You being here, after saying no, is exactly the story.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'searching_for_purpose',
        text: 'I have never really committed to faith but something keeps pulling me toward it.',
        reflection: "That pull is the first son before he changed his mind — before the going, there was the being unable to stay away. Whatever is drawing you here is worth following.",
      },
      {
        key: 'C', feedTag: 'BRIDGE', signal: 'honest_inquiry',
        text: 'I am honest enough to say I am not sure yet and I don\'t want to fake it.',
        reflection: "That honesty is worth more than a performance of faith. The son who said yes and didn't go is the one Jesus used as a warning. Not knowing but showing up is closer to the truth than knowing and not moving.",
      },
      {
        key: 'D', feedTag: 'MAINTENANCE', signal: 'covenant_intent',
        text: 'I have committed and I want to make sure my actions match what I say I believe.',
        reflection: "That self-awareness is rare. The gap between the yes and the going — that is where most of the work happens. Let's close that gap.",
      },
    ],
    otherReflection: "Thank you for being that honest. What you shared — ",
  },

  // 7 ── Peter Walking on Water ───────────────────────────────────────────────
  {
    id: 'peter_water',
    narrative: [
      'The disciples were in a boat at night when they saw Jesus walking toward them on the water.',
      'Peter said: "Lord, if it is you, tell me to come to you on the water."',
      'Jesus said: "Come."',
      'Peter got out of the boat. He was doing it — actually walking on water. Then he noticed the wind. He looked at the waves. He started to sink.',
      'Jesus caught him immediately. He said: "Why did you doubt?" Not as condemnation. As a real question worth sitting with.',
    ],
    question: 'Have you ever had something real — a moment of faith, a sense of something true — and then watched it slip when the storm got loud?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'has_history_with_faith',
        text: 'Yes — I had faith once and something happened that made it hard to hold onto.',
        reflection: "Peter was already out of the boat when he started sinking. He had already stepped into something real. Jesus caught him in the middle of the sinking, not after he swam back to safety. What you had was real. What happened to it doesn't erase that.",
      },
      {
        key: 'B', feedTag: 'BRIDGE', signal: 'honest_inquiry',
        text: 'I want to believe but I have too many questions about whether any of this is real.',
        reflection: "Peter asked for proof before he stepped out: 'If it is you, tell me to come.' Jesus didn't say that was the wrong question. He said come. The questions are allowed. They can coexist with the stepping out.",
      },
      {
        key: 'C', feedTag: 'MILK', signal: 'carries_burden',
        text: 'The storms in my life have been too loud to hear anything else.',
        reflection: "That is exactly what happened to Peter — the wind and waves became louder than the voice that told him to come. The reach downward to catch him was immediate. Not after the storm passed. In the middle of it.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'searching_for_purpose',
        text: 'I have never stepped out of the boat. I am not sure what I am waiting for.',
        reflection: "Peter was the only one who got out. The others stayed and watched. There is something in you that is reading this, and it is not the part of you that stays in the boat. That matters.",
      },
    ],
    otherReflection: "Thank you for that. The storms worth talking about are usually the ones we haven't been able to name. What you shared — ",
  },

  // 8 ── The Lost Coin ────────────────────────────────────────────────────────
  {
    id: 'lost_coin',
    narrative: [
      'A woman has ten coins. She loses one.',
      'She lights a lamp. She sweeps the whole house. She searches carefully — not casually, carefully — until she finds it.',
      'Then she calls her neighbors and friends to celebrate.',
      'One coin. Out of ten. The joy is disproportionate to the value of the coin.',
      'Jesus said the angels celebrate like that over one person who comes home. Not a crowd. One.',
    ],
    question: 'Have you ever felt like the thing that got lost rather than the one doing the searching?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'carries_burden',
        text: 'Yes — I have felt overlooked, easy to forget, like I don\'t register.',
        reflection: "She lit a lamp and swept the whole house for one coin. The search was not casual — it was careful. You are not easy to miss. The searching is more deliberate than you may have been told.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'has_history_with_faith',
        text: 'I have felt distant from God and not sure if I am being looked for.',
        reflection: "The coin didn't find its way back on its own — she lit a lamp and searched carefully. The searching is already happening. Being here is evidence of it.",
      },
      {
        key: 'C', feedTag: 'MILK', signal: 'carries_shame',
        text: 'I have felt like I am not worth the effort it would take to find me.',
        reflection: "One coin. Out of ten. She stopped everything for the one. And when she found it, the celebration was more than the coin was worth by any rational measure. That is the point. That is how you are valued.",
      },
      {
        key: 'D', feedTag: 'BRIDGE', signal: 'open_to_god',
        text: 'I wonder sometimes if anyone — or anything — is actually looking.',
        reflection: "The light is on. The house is being swept. That wonder — that question — is the sound of something that has not given up. Let's follow it.",
      },
    ],
    otherReflection: "Thank you for that. Being honest about feeling small is not small at all. What you shared — ",
  },

  // 9 ── The Rich Young Ruler ────────────────────────────────────────────────
  {
    id: 'rich_ruler',
    narrative: [
      'A young man ran to Jesus. He knelt. He asked the right question: "What must I do to have eternal life?"',
      'He had kept all the commandments since childhood. He was serious about it.',
      'The text says: Jesus looked at him and loved him.',
      'Then Jesus gave him one thing he couldn\'t do. The man went away sad.',
      'Jesus let him go. He didn\'t lower the bar. He didn\'t chase him. He loved him and let him walk away.',
    ],
    question: 'Is there something you already know — quietly — that stands between you and fully following what you believe?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'carries_burden',
        text: 'Yes. There is something I am holding onto that I am not ready to let go of.',
        reflection: "Jesus looked at him and loved him — before he said the hard thing, not after. Whatever you are holding onto, you are seen clearly and not condemned for it. That is where the conversation can start.",
      },
      {
        key: 'B', feedTag: 'BRIDGE', signal: 'honest_inquiry',
        text: 'I am not sure what I believe yet and I don\'t want to fake my way into it.',
        reflection: "That honesty is what the young man brought — he was earnest about his question. Jesus didn't turn him away for the question. He answered it fully. Bring the real question. That is the right starting point.",
      },
      {
        key: 'C', feedTag: 'MILK', signal: 'searching_for_purpose',
        text: 'I have been doing the right things but something still feels hollow.',
        reflection: "The young man had kept every commandment and still felt like something was missing. Doing the right things and feeling empty is its own kind of honesty. That gap is worth exploring.",
      },
      {
        key: 'D', feedTag: 'MAINTENANCE', signal: 'covenant_intent',
        text: 'I am committed but I know there are areas where I hold back.',
        reflection: "The young man was close — genuinely close. Jesus loved him for it. The holding back is where the next layer of growth usually lives. Let's go there.",
      },
    ],
    otherReflection: "Thank you for that kind of honesty. Most people don't get there this quickly. What you shared — ",
  },
];

// Pick one story per session, weighted toward stories the user hasn't seen
// For now: random selection from all 9
function pickStory(): Story {
  return STORIES[Math.floor(Math.random() * STORIES.length)];
}

// ── Faith background page ───────────────────────────────────────────────────
// A disciple asks openly where faith lives for them — naming no church for them
// (Law 9). Their own words can carry anything, including a member self-ID.
const FAITH_OPTIONS: { key: string; text: string }[] = [
  { key: 'active',       text: "I'm part of a church or faith community now." },
  { key: 'stepped_away', text: 'I grew up in one, but I have stepped away.' },
  { key: 'none',         text: "I've never really had one." },
  { key: 'complicated',  text: "It's complicated." },
  { key: 'private',      text: "I'd rather not say." },
];

// ── Screen ────────────────────────────────────────────────────────────────────

// The opening welcome now lives on the Hook screen (the single front door), so
// onboarding begins directly with the story — no second "you are welcome here"
// screen repeating what the Hook already said.
type Phase = 'story' | 'question' | 'reflection' | 'faith';

export default function OnboardScreen({ navigation }: Props) {
  const completeOnboarding    = useAppStore(s => s.completeOnboarding);
  const setName               = useAppStore(s => s.setName);
  const recordFaithBackground = useAppStore(s => s.recordFaithBackground);

  const [phase,       setPhase]       = useState<Phase>('story');
  const [story]                       = useState<Story>(pickStory);
  const [selectedKey, setSelectedKey] = useState<string | null>(null);
  const [freeText,    setFreeText]    = useState('');
  const [showFree,    setShowFree]    = useState(false);
  const [reflection,  setReflection]  = useState('');

  // Reflection-step name + the dedicated faith-background page.
  const [nameDraft,   setNameDraft]   = useState('');
  const [faithChoice, setFaithChoice] = useState<string | null>(null);
  const [faithText,   setFaithText]   = useState('');

  const fadeAnim  = useRef(new Animated.Value(0)).current;
  const slideAnim = useRef(new Animated.Value(24)).current;

  useEffect(() => {
    fadeAnim.setValue(0);
    slideAnim.setValue(24);
    Animated.parallel([
      Animated.timing(fadeAnim,  { toValue: 1, duration: 700, useNativeDriver: true }),
      Animated.timing(slideAnim, { toValue: 0, duration: 600, useNativeDriver: true }),
    ]).start();
  }, [phase]);

  const animStyle = {
    opacity:   fadeAnim,
    transform: [{ translateY: slideAnim }],
  };

  function selectChoice(key: string) {
    const choice = story.choices.find(c => c.key === key);
    if (!choice) return;
    setSelectedKey(key);
    setReflection(choice.reflection);
    setTimeout(() => setPhase('reflection'), 220);
  }

  function handleFreeSubmit() {
    if (freeText.trim().length < 3) return;
    const preview = freeText.trim().slice(0, 100) + (freeText.trim().length > 100 ? '…' : '');
    setReflection(
      story.otherReflection +
      `"${preview}" — that is worth sitting with. You are in the right place.`,
    );
    setSelectedKey('E');
    setTimeout(() => setPhase('reflection'), 220);
  }

  function handleEnter() {
    // The faith page is the final step — a choice must be made (even "I'd rather
    // not say") before entering, matching the prototype's onFaithEnter guard.
    if (!faithChoice) return;

    if (selectedKey === 'E') {
      completeOnboarding('E', freeText, undefined, undefined);
    } else {
      const choice = story.choices.find(c => c.key === selectedKey) ?? story.choices[0];
      // Pass the hidden signal from the chosen story response so the milk gate and
      // connection ladder receive what the person revealed from screen one.
      completeOnboarding(choice.key, undefined, choice.feedTag, choice.signal);
    }
    // Their name, then their faith in their own words — both fold into the engine
    // AFTER onboarding resets state, so they survive into the app.
    if (nameDraft.trim()) setName(nameDraft.trim());
    recordFaithBackground(faithChoice, faithText);

    navigation.replace('Main');
  }

  // ── STORY ──────────────────────────────────────────────────────────────────
  if (phase === 'story') {
    return (
      <ScrollView style={styles.scroll} contentContainerStyle={styles.scrollContent}>
        <StatusBar style="light" />
        <Animated.View style={animStyle}>
          {story.narrative.map((para, i) => (
            <Text
              key={i}
              style={[styles.narrativePara, i === 0 && styles.narrativeFirst]}
            >
              {para}
            </Text>
          ))}
          <TouchableOpacity
            style={styles.primaryBtn}
            activeOpacity={0.75}
            onPress={() => setPhase('question')}
          >
            <Text style={styles.primaryBtnText}>Continue →</Text>
          </TouchableOpacity>
        </Animated.View>
      </ScrollView>
    );
  }

  // ── QUESTION ───────────────────────────────────────────────────────────────
  if (phase === 'question') {
    return (
      <KeyboardAvoidingView
        style={{ flex: 1, backgroundColor: colors.bg }}
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      >
        <ScrollView
          style={styles.scroll}
          contentContainerStyle={styles.scrollContent}
          keyboardShouldPersistTaps="handled"
        >
          <StatusBar style="light" />
          <Animated.View style={animStyle}>
            <Text style={styles.question}>{story.question}</Text>
            <View style={styles.choices}>
              {story.choices.map(c => (
                <TouchableOpacity
                  key={c.key}
                  style={styles.choiceBtn}
                  activeOpacity={0.7}
                  onPress={() => selectChoice(c.key)}
                >
                  <Text style={styles.choiceText}>{c.text}</Text>
                </TouchableOpacity>
              ))}
              {!showFree ? (
                <TouchableOpacity
                  style={[styles.choiceBtn, styles.choiceBtnOther]}
                  activeOpacity={0.7}
                  onPress={() => setShowFree(true)}
                >
                  <Text style={styles.choiceTextMuted}>
                    I want to say it in my own words.
                  </Text>
                </TouchableOpacity>
              ) : (
                <View style={styles.freeBox}>
                  <TextInput
                    style={styles.freeInput}
                    placeholder="Share whatever comes to mind…"
                    placeholderTextColor={colors.textMuted}
                    multiline
                    numberOfLines={4}
                    maxLength={600}
                    value={freeText}
                    onChangeText={setFreeText}
                    autoFocus
                    textAlignVertical="top"
                  />
                  <TouchableOpacity
                    style={[
                      styles.primaryBtn,
                      freeText.trim().length < 3 && styles.primaryBtnDisabled,
                    ]}
                    activeOpacity={0.75}
                    disabled={freeText.trim().length < 3}
                    onPress={handleFreeSubmit}
                  >
                    <Text style={styles.primaryBtnText}>Continue →</Text>
                  </TouchableOpacity>
                </View>
              )}
            </View>
          </Animated.View>
        </ScrollView>
      </KeyboardAvoidingView>
    );
  }

  // ── FAITH BACKGROUND ───────────────────────────────────────────────────────
  if (phase === 'faith') {
    return (
      <KeyboardAvoidingView
        style={{ flex: 1, backgroundColor: colors.bg }}
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      >
        <ScrollView
          style={styles.scroll}
          contentContainerStyle={styles.scrollContent}
          keyboardShouldPersistTaps="handled"
        >
          <StatusBar style="light" />
          <Animated.View style={animStyle}>
            <Text style={styles.faithIntro}>
              One more thing — so we can walk with you honestly.
            </Text>
            <Text style={styles.faithQuestion}>
              Where does faith live for you — today, or in your past?
            </Text>

            <View style={styles.choices}>
              {FAITH_OPTIONS.map(opt => {
                const selected = faithChoice === opt.key;
                return (
                  <TouchableOpacity
                    key={opt.key}
                    style={[styles.faithOptBtn, selected && styles.faithOptBtnSelected]}
                    activeOpacity={0.7}
                    onPress={() => setFaithChoice(opt.key)}
                  >
                    <Text style={[styles.faithOptText, selected && styles.faithOptTextSelected]}>
                      {opt.text}
                    </Text>
                  </TouchableOpacity>
                );
              })}
            </View>

            <Text style={styles.faithHint}>
              If you'd like, name it — which church or tradition, and what it has
              been like for you. Your words stay yours.
            </Text>
            <TextInput
              style={styles.faithInput}
              placeholder="e.g. raised Baptist… Catholic, but drifting… never had one…"
              placeholderTextColor={colors.textMuted}
              multiline
              numberOfLines={4}
              maxLength={400}
              value={faithText}
              onChangeText={setFaithText}
              textAlignVertical="top"
            />

            <TouchableOpacity
              style={[styles.primaryBtn, !faithChoice && styles.primaryBtnDisabled]}
              activeOpacity={0.75}
              disabled={!faithChoice}
              onPress={handleEnter}
            >
              <Text style={styles.primaryBtnText}>Enter →</Text>
            </TouchableOpacity>
          </Animated.View>
        </ScrollView>
      </KeyboardAvoidingView>
    );
  }

  // ── REFLECTION ─────────────────────────────────────────────────────────────
  return (
    <KeyboardAvoidingView
      style={{ flex: 1, backgroundColor: colors.bg }}
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
    >
      <ScrollView
        style={styles.scroll}
        contentContainerStyle={styles.scrollContent}
        keyboardShouldPersistTaps="handled"
      >
        <StatusBar style="light" />
        <Animated.View style={animStyle}>
          <Text style={styles.reflectionText}>{reflection}</Text>
          <Text style={styles.reflectionCoda}>
            That is where we start.{'\n'}Not with a statement. With you.
          </Text>

          <Text style={styles.nameHint}>
            If you'd like, tell us what to call you. A first name is plenty — or skip it.
          </Text>
          <TextInput
            style={styles.nameInput}
            placeholder="Your name (optional)"
            placeholderTextColor={colors.textMuted}
            maxLength={40}
            value={nameDraft}
            onChangeText={setNameDraft}
            autoCapitalize="words"
          />

          <TouchableOpacity
            style={styles.primaryBtn}
            activeOpacity={0.75}
            onPress={() => setPhase('faith')}
          >
            <Text style={styles.primaryBtnText}>Continue →</Text>
          </TouchableOpacity>
        </Animated.View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
}

// ── Styles ────────────────────────────────────────────────────────────────────

const styles = StyleSheet.create({
  fullScreen: {
    flex: 1, backgroundColor: colors.bg,
    alignItems: 'center', justifyContent: 'center',
    paddingHorizontal: spacing.lg,
  },
  scroll: { flex: 1, backgroundColor: colors.bg },
  scrollContent: {
    flexGrow: 1,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.xxl,
  },

  sanctuaryInner: { alignItems: 'center', maxWidth: 320 },
  sanctuaryHeadline: {
    fontSize: 36, fontFamily: 'Georgia', color: colors.gold,
    textAlign: 'center', marginBottom: spacing.lg, letterSpacing: 1,
  },
  sanctuaryBody: {
    fontSize: 16, fontFamily: 'Georgia', color: colors.textMid,
    textAlign: 'center', lineHeight: 27, marginBottom: spacing.xxl,
    fontStyle: 'italic',
  },

  narrativePara: {
    fontSize: 16, fontFamily: 'Georgia', color: colors.textMid,
    lineHeight: 28, marginBottom: spacing.lg, fontStyle: 'italic',
  },
  narrativeFirst: {
    color: colors.text, fontStyle: 'normal', fontSize: 17,
  },

  question: {
    fontSize: 18, fontFamily: 'Georgia', color: colors.text,
    lineHeight: 30, marginBottom: spacing.xl, fontStyle: 'italic',
  },

  choices: { gap: spacing.sm },
  choiceBtn: {
    backgroundColor: colors.bgInput, borderWidth: 1,
    borderColor: colors.borderDim, borderRadius: radius.md,
    paddingVertical: 16, paddingHorizontal: 18,
  },
  choiceBtnOther: { borderStyle: 'dashed' },
  choiceText: {
    fontSize: 14, fontFamily: 'Georgia', color: colors.textMid, lineHeight: 22,
  },
  choiceTextMuted: {
    fontSize: 14, fontFamily: 'Georgia', color: colors.textMuted, fontStyle: 'italic',
  },

  freeBox: { gap: spacing.sm },
  freeInput: {
    backgroundColor: colors.bgInput, borderWidth: 1, borderColor: colors.borderDim,
    borderRadius: radius.md, color: colors.textMid, fontSize: 15,
    fontFamily: 'Georgia', padding: 14, minHeight: 110, lineHeight: 24,
  },

  primaryBtn: {
    alignSelf: 'flex-start', backgroundColor: colors.gold,
    borderRadius: 26, paddingVertical: 13, paddingHorizontal: 36,
    marginTop: spacing.xl,
  },
  primaryBtnDisabled: { backgroundColor: colors.borderDim },
  primaryBtnText: {
    fontSize: 15, fontFamily: 'Georgia', color: '#15110a', letterSpacing: 0.5,
    fontWeight: '600',
  },

  reflectionText: {
    fontSize: 17, fontFamily: 'Georgia', color: colors.textMid,
    lineHeight: 30, marginBottom: spacing.xl, fontStyle: 'italic',
  },
  reflectionCoda: {
    fontSize: 14, fontFamily: 'Georgia', color: colors.textMuted,
    lineHeight: 22, marginBottom: spacing.lg,
  },

  nameHint: {
    fontSize: 13, fontFamily: 'Georgia', fontStyle: 'italic',
    color: colors.textMuted, lineHeight: 20, marginBottom: spacing.sm,
  },
  nameInput: {
    backgroundColor: colors.bgInput, borderWidth: 1, borderColor: colors.borderDim,
    borderRadius: radius.md, color: colors.textMid, fontSize: 15,
    fontFamily: 'Georgia', paddingVertical: 12, paddingHorizontal: 14,
    alignSelf: 'flex-start', minWidth: 220,
  },

  faithIntro: {
    fontSize: 18, fontFamily: 'Georgia', color: colors.text,
    lineHeight: 30, marginBottom: spacing.sm, fontStyle: 'italic',
  },
  faithQuestion: {
    fontSize: 15, fontFamily: 'Georgia', color: colors.textDim,
    lineHeight: 24, marginBottom: spacing.lg,
  },
  faithOptBtn: {
    backgroundColor: colors.bgInput, borderWidth: 1, borderColor: colors.borderDim,
    borderRadius: radius.md, paddingVertical: 14, paddingHorizontal: 18,
  },
  faithOptBtnSelected: { borderColor: colors.gold },
  faithOptText: {
    fontSize: 14, fontFamily: 'Georgia', color: colors.textMid, lineHeight: 22,
  },
  faithOptTextSelected: { color: colors.gold },
  faithHint: {
    fontSize: 13, fontFamily: 'Georgia', fontStyle: 'italic',
    color: colors.textMuted, lineHeight: 20, marginTop: spacing.md, marginBottom: spacing.sm,
  },
  faithInput: {
    backgroundColor: colors.bgInput, borderWidth: 1, borderColor: colors.borderDim,
    borderRadius: radius.md, color: colors.textMid, fontSize: 14,
    fontFamily: 'Georgia', padding: 12, minHeight: 84, lineHeight: 22,
  },
});
