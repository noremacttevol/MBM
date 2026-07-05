/**
 * OnboardScreen — story-first onboarding per CLAUDE.md Jesus Method rules.
 *
 * 20 entry stories. Each one reaches a different kind of person.
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
        key: 'D', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already believe. I am here because I want to go deeper.',
        reflection: "Then you are in good company. Even those who walked closest to Jesus still had moments of reaching, still needed reminding of what they already knew. There is always more.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
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
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
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
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
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
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
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
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
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
        key: 'D', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I have committed and I want to make sure my actions match what I say I believe.',
        reflection: "That self-awareness is rare. The gap between the yes and the going — that is where most of the work happens. Let's close that gap.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
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
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
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
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
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
        key: 'D', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I am committed but I know there are areas where I hold back.',
        reflection: "The young man was close — genuinely close. Jesus loved him for it. The holding back is where the next layer of growth usually lives. Let's go there.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
      },
    ],
    otherReflection: "Thank you for that kind of honesty. Most people don't get there this quickly. What you shared — ",
  },

  // 10 ── The Woman at the Well ───────────────────────────────────────────────
  {
    id: 'well',
    narrative: [
      'A woman came to draw water at noon — the hottest hour of the day, when no one else would be there. She had reasons to avoid the crowd. Five marriages behind her, and the town knew all of it.',
      'A tired traveler was sitting by the well. A Jewish man, in Samaria — someone who by every custom of the day should not have spoken to her at all.',
      'He asked her for a drink. Then he offered her one: "Whoever drinks the water I give will never thirst again."',
      'She came for water and ended up talking about her whole life. He already knew it — all of it — and he did not turn away. He stayed in the conversation.',
      'She left her water jar at the well and ran to tell the whole town she had been avoiding: "Come see a man who told me everything I ever did."',
    ],
    question: 'She came for one thing and found out she was thirsty for something much deeper. Have you ever been searching for something and realized later it was deeper than what you thought you wanted?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'searching_for_purpose',
        text: 'Yes — I keep reaching for things that never quite satisfy, and I am starting to wonder why.',
        reflection: "That wondering is the beginning of the whole story. She had gone to that well a thousand times and it never once filled the real thirst. Noticing the gap between what you are chasing and what you actually need — that is where the deeper water starts.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'carries_shame',
        text: 'I understand going at noon. There are parts of my life I would rather no one saw.',
        reflection: "He knew everything she was avoiding — and he was the one who started the conversation. The parts of your life you keep in the noon heat, away from every eye, are not disqualifying. They are exactly where he tends to sit down and wait.",
      },
      {
        key: 'C', feedTag: 'BRIDGE', signal: 'honest_inquiry',
        text: 'I would want to know how he knew her — whether something like that is even real.',
        reflection: "Fair. She asked hard questions too, right there at the well — about worship, about who was right, about whether he could really be who he seemed to be. He took every one of them seriously. Bring yours the same way.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'has_history_with_faith',
        text: 'I once drank from that deeper water, I think. It has been a while.',
        reflection: "Then you know the taste, and that never fully leaves a person. The well is still there. She left her jar behind because she found something better than what she came for — and it is still on offer, as much to the returning as to the first-time thirsty.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
      },
    ],
    otherReflection: "Thank you for putting that in your own words. She ended up telling him her real life too — that is how these conversations are supposed to go. What you shared — ",
  },

  // 11 ── Calming the Storm ───────────────────────────────────────────────────
  {
    id: 'storm',
    narrative: [
      'A storm came up on the lake at night — sudden and violent, the kind that frightened even the fishermen who had worked that water their whole lives.',
      'Waves broke over the boat. It was filling with water. And Jesus was asleep in the stern, on a cushion.',
      'They woke him with a question that people have been asking in storms ever since: "Teacher, don\'t you care that we are about to drown?"',
      'He got up, spoke to the wind and the waves — "Peace. Be still." — and the sea went flat calm.',
      'Then he turned to them, soaked and shaking, and asked gently: "Why were you so afraid?" He never denied the storm was real. He was just bigger than it.',
    ],
    question: '"Don\'t you care that we are drowning?" — have you ever asked that question, or wanted to?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'carries_burden',
        text: 'Yes. I am in a storm right now, and it does not feel like anyone is awake.',
        reflection: "Then you asked the disciples' exact question, and it is worth noticing: he did not scold them for waking him. He stood up and dealt with the storm first, and only then talked about fear. Whatever is breaking over your boat right now — that is not too small or too much to bring here.",
      },
      {
        key: 'B', feedTag: 'BRIDGE', signal: 'skeptical_of_god',
        text: 'I have asked it and heard nothing back. That silence is most of why I doubt.',
        reflection: "That is one of the oldest and most honest wounds there is — and the story does not pretend it away. He really was asleep while the water rose. The disciples' fear was reasonable. Whatever the answer turns out to be, it has to be big enough for the silence too. Let's look at it honestly.",
      },
      {
        key: 'C', feedTag: 'MILK', signal: 'carries_grief',
        text: 'I have been through a storm that did real damage. I am still recovering from it.',
        reflection: "Some storms end and leave wreckage that takes years to mend. Nothing here will rush that. But it matters that the one in the boat never once said the storm wasn't real — he only proved it did not get the last word. Neither does yours.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'open_to_god',
        text: 'I want to believe there is someone in the boat who can say "peace, be still."',
        reflection: "Wanting to believe is not a lesser kind of faith — it is how nearly all faith starts. The disciples in that boat were not sure who he was yet either. They found out by going through the storm with him. That is the invitation here.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
      },
    ],
    otherReflection: "Thank you for saying that in your own words. Storms are personal, and so is the peace. What you shared — ",
  },

  // 12 ── Blind Bartimaeus ────────────────────────────────────────────────────
  {
    id: 'bartimaeus',
    narrative: [
      'A blind man named Bartimaeus sat begging beside the road out of Jericho. When he heard Jesus was passing, he began to shout: "Jesus, have mercy on me!"',
      'The crowd told him to be quiet. Many voices, telling one desperate man that his need was an embarrassment.',
      'He shouted louder.',
      'Jesus stopped the whole procession and said: "Call him." And the man threw off his cloak — the coat a beggar spread to catch coins, everything he owned — jumped up, and came.',
      'Jesus asked him one question: "What do you want me to do for you?" As if it weren\'t obvious. He wanted the man to say it. "Rabbi, I want to see." And he saw.',
    ],
    question: 'The crowd told him to keep quiet, and he shouted louder. What is the thing you would shout for, if no one could tell you to be quiet?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'carries_burden',
        text: 'There is something I have needed for so long I have almost stopped asking for it.',
        reflection: "Bartimaeus had been on that roadside for years. The shout was still in him. Whatever you have almost stopped asking for — the question Jesus asked him is still open: what do you want me to do for you? You are allowed to say it plainly here.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'carries_shame',
        text: 'I have been told — or told myself — that my need is too much, too loud, too embarrassing.',
        reflection: "That was the crowd's whole message: be quiet, you are an embarrassment. Notice who overruled them. The entire procession stopped for the one voice everyone else was hushing. Your need is not an embarrassment here.",
      },
      {
        key: 'C', feedTag: 'BRIDGE', signal: 'honest_inquiry',
        text: 'I am not sure what I would shout for. I am still working out what I actually want.',
        reflection: "That may be why Jesus asked the question out loud — 'What do you want me to do for you?' — when the answer looked obvious. Naming what you actually want is real work, and it is worth doing slowly. That is a fine place to start.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'open_to_god',
        text: '"I want to see" — that is close to it. I want things to finally make sense.',
        reflection: "'Rabbi, I want to see' might be the most honest prayer in the whole book. Wanting clarity — about God, about your life, about what is true — is exactly the request he honored on that road. Keep asking it.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
      },
    ],
    otherReflection: "Thank you for shouting it, in your own way. That is what this whole place is for. What you shared — ",
  },

  // 13 ── The Paralytic Through the Roof ─────────────────────────────────────
  {
    id: 'roof',
    narrative: [
      'Four friends carried a paralyzed man on a mat to the house where Jesus was teaching. The crowd was packed so tight there was no way through the door.',
      'So they climbed onto the roof, dug through it, and lowered their friend down on ropes — right in front of Jesus, mid-sermon, dust and daylight pouring in.',
      'The text says something remarkable: "When Jesus saw THEIR faith" — the faith of the friends who did the carrying — he turned to the man on the mat.',
      'The first thing he said was not about the man\'s legs. "Son, your sins are forgiven." He went to the deepest wound first.',
      'Then he healed the legs too, and the man walked home carrying the mat that had carried him.',
    ],
    question: 'Four people tore a roof open because their friend could not get there alone. Where do you find yourself in that room?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'carries_burden',
        text: 'On the mat. I could not get to hope on my own strength right now if I tried.',
        reflection: "Then hear the part most people miss: the man on the mat never says a word in the whole story. He didn't have to earn the roof opening. Others' faith carried him until he could stand in his own. Being carried for a while is allowed.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'carries_grief',
        text: 'I am one of the four. I have been carrying someone I love and I am tired.',
        reflection: "'When Jesus saw THEIR faith.' The carriers are the ones whose faith gets named in that story. What you are doing for the person you love is seen — and carriers need carrying too. You don't have to hold the ropes alone.",
      },
      {
        key: 'C', feedTag: 'BRIDGE', signal: 'honest_inquiry',
        text: 'In the crowd, honestly — watching, curious, not sure what I make of it yet.',
        reflection: "The crowd is an honest place to stand. Everyone in that packed room started as a watcher. The roof opening was for one man, but the daylight fell on all of them. Watch as long as you need to. The questions are welcome here.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'searching_for_purpose',
        text: 'I think I am meant to be one of the four for someone — I want a faith that carries people.',
        reflection: "That is a remarkable thing to want. Faith that digs through roofs for other people is the kind Jesus stopped mid-sermon to honor. Let's build that kind — sturdy enough to hold ropes.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
      },
    ],
    otherReflection: "Thank you — that is your own place in the room, and it is the right one to start from. What you shared — ",
  },

  // 14 ── The Ten Lepers ──────────────────────────────────────────────────────
  {
    id: 'ten_lepers',
    narrative: [
      'Ten men with leprosy stood at a distance — the law required it — and called out to Jesus for mercy.',
      'He did not touch them or announce a healing. He simply said: "Go, show yourselves to the priests." Which only made sense if they would be clean when they arrived.',
      'They went. And as they went — on the road, mid-obedience, before anything visible had changed — they were healed.',
      'One of them, when he saw it, turned around. He came back praising God at the top of his voice and threw himself at Jesus\'s feet in thanks. He was a Samaritan — the outsider of the group.',
      'Jesus asked: "Were not all ten cleansed? Where are the other nine?" Then to the one: "Rise and go. Your faith has made you well."',
    ],
    question: 'The healing happened while they walked, before they could see it. Have you ever had to move forward on nothing but a word — before there was any proof?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'open_to_god',
        text: 'That is where I am now — trying to take steps without being able to see the outcome.',
        reflection: "Then you are on the exact stretch of road where the healing in that story happened — between the word and the proof. Nothing visible had changed when they started walking. Keep walking. This is the part of the road that counts.",
      },
      {
        key: 'B', feedTag: 'BRIDGE', signal: 'skeptical_of_god',
        text: 'Honestly, I would have wanted the proof first. Trusting a word is hard for me.',
        reflection: "That is fair — and worth noticing that Jesus didn't rebuke the request for mercy or demand belief up front. He gave them something small and doable: go. Sometimes the honest version of faith is just taking one testable step and watching what happens. That is allowed here.",
      },
      {
        key: 'C', feedTag: 'MILK', signal: 'has_history_with_faith',
        text: 'I think I might be one of the nine — I received something good once and drifted on without looking back.',
        reflection: "Then you already know the quiet ache of that story. But notice: the nine stayed healed. What they missed was not the gift but the relationship — the turning around. And turning around is precisely what you just did by naming it. Welcome back.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'carries_burden',
        text: 'I relate to standing at a distance, calling out, hoping to be noticed.',
        reflection: "They had to stand far off — the distance wasn't their choice, it was their condition. And mercy crossed it anyway. Whatever distance you feel between yourself and hope right now, it is exactly the kind of distance that gets crossed in this story.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
      },
    ],
    otherReflection: "Thank you for turning that over honestly. The one who came back just said what was true out loud — that is all thanks is. What you shared — ",
  },

  // 15 ── The Centurion ───────────────────────────────────────────────────────
  {
    id: 'centurion',
    narrative: [
      'A Roman centurion — an officer of the occupying army, the last person anyone expected — came to Jesus about his servant, who was suffering terribly at home.',
      'Jesus said: "I will come and heal him."',
      'The centurion said something no one saw coming: "Lord, I am not worthy to have you come under my roof. Just say the word, and my servant will be healed. I am a man under authority myself — I say go, and men go."',
      'Jesus was amazed. The text says he marveled — one of the only times it says that. "I have not found faith like this in all Israel."',
      'The servant was healed that hour, from a distance, on nothing but a word.',
    ],
    question: '"I am not worthy to have you under my roof — but say the word." Which half of that sentence is easier for you to say?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'carries_shame',
        text: 'The first half. "Not worthy" comes easily to me. The confident asking does not.',
        reflection: "Notice what Jesus did with the man's 'not worthy': he ignored it entirely and praised his faith instead. The unworthiness was not the part Jesus marveled at or even acknowledged. If 'not worthy' comes easily to you, you are in good company — and it is not the end of the sentence.",
      },
      {
        key: 'B', feedTag: 'BRIDGE', signal: 'honest_inquiry',
        text: 'Neither, yet. I am still deciding whether there is anyone to say the word at all.',
        reflection: "That is an honest place to stand, and worth saying: the centurion was an outsider to the whole faith — wrong nation, wrong army, wrong gods. He reasoned his way to that sentence from what he knew about how authority works. Reasoning your way in is a legitimate road. Take it at your pace.",
      },
      {
        key: 'C', feedTag: 'MILK', signal: 'carries_grief',
        text: 'I understand him coming on behalf of someone else. Someone I love is suffering.',
        reflection: "The centurion never asked a single thing for himself — the whole errand was love for someone under his roof. Jesus honored that kind of asking instantly. Whoever you are carrying, bringing them here counts as exactly the kind of faith that amazed him.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'open_to_god',
        text: 'I want the second half — faith confident enough to trust a word across a distance.',
        reflection: "That confidence wasn't naivety — it was the most clear-eyed thing in the story. He simply took seriously what authority means. Faith like that can be learned, and it starts just the way you started: by wanting it out loud.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
      },
    ],
    otherReflection: "Thank you for weighing that honestly. The centurion's sentence has been prayed for two thousand years because it is so human. What you shared — ",
  },

  // 16 ── Mary and Martha ─────────────────────────────────────────────────────
  {
    id: 'mary_martha',
    narrative: [
      'Jesus came to the home of two sisters. Martha threw herself into the work — the meal, the serving, everything a guest like this deserved.',
      'Her sister Mary sat down at Jesus\'s feet and just listened.',
      'Martha, worn thin, finally said what she was feeling: "Lord, don\'t you care that my sister has left me to do the work alone? Tell her to help me!"',
      'He answered with her name, twice — gently: "Martha, Martha. You are worried and troubled about many things. But only one thing is needed."',
      '"Mary has chosen the better part, and it will not be taken away from her." He never scolded the serving. He worried about the worry.',
    ],
    question: 'Worried and troubled about many things — or sitting down long enough to listen. Which one sounds more like your life right now?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'carries_burden',
        text: 'Martha, completely. My life is a list that never ends, and I am worn thin.',
        reflection: "Then hear how he said her name — twice, gently, the way you speak to someone you love who is fraying. Not a rebuke. He saw the weight of the many things. The invitation was never to stop caring; it was permission to sit down. That permission is extended here too.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'searching_for_purpose',
        text: 'I stay busy partly so I don\'t have to sit still with the bigger questions.',
        reflection: "That is a brave thing to admit — busyness is the most respectable hiding place there is. The 'one thing needed' was never another task. It was presence. Sitting still with the big questions is exactly what this place is built for, at whatever pace you can bear.",
      },
      {
        key: 'C', feedTag: 'MILK', signal: 'carries_grief',
        text: '"Lord, don\'t you care?" — I have felt overlooked while doing everything right.',
        reflection: "Martha said it straight to his face, and he did not punish her for it — he answered with tenderness and her own name. Feeling unseen while you hold everything together is a real grief. It was safe to say to him, and it is safe to say here.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'open_to_god',
        text: 'I want to be Mary. I want to learn how to actually sit and listen.',
        reflection: "Then you have already chosen the better part — wanting it is the first act of it. Mary's whole qualification was proximity: she just got close and stayed. That is a skill anyone can practice, starting now.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
      },
    ],
    otherReflection: "Thank you for sitting still long enough to answer that. That was already a small piece of the better part. What you shared — ",
  },

  // 17 ── Lazarus: Jesus Wept ─────────────────────────────────────────────────
  {
    id: 'lazarus',
    narrative: [
      'Jesus\'s close friend Lazarus was dying, and the sisters sent word. Jesus stayed where he was two more days — and Lazarus died.',
      'When he finally came, Martha met him on the road with the sentence grieving people have said ever since: "Lord, if you had been here, my brother would not have died."',
      'He knew how the story would end. He knew resurrection was minutes away. And still — standing at the tomb of his friend, among the weeping — the shortest verse in scripture happened: Jesus wept.',
      'The people watching said: "See how he loved him."',
      'Then he called into the tomb, "Lazarus, come out" — and the dead man walked into the light. But the tears came first. He did not skip the grief on the way to the miracle.',
    ],
    question: '"Lord, if you had been here…" — grief almost always has an "if" in it. Does that sentence sound familiar to you?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'carries_grief',
        text: 'Yes. I have lost someone, and I know that sentence by heart.',
        reflection: "Then this story keeps its most important detail for you: he wept, knowing the miracle was minutes away. Your grief is not a failure of faith and it is not rushed here. He stood in it first. Whoever you are missing — that love is seen the way the crowd saw his: 'see how he loved him.'",
      },
      {
        key: 'B', feedTag: 'BRIDGE', signal: 'skeptical_of_god',
        text: 'The two-day delay is my problem. Why wait while someone you love suffers?',
        reflection: "That question is not an attack on the story — it is IN the story. Both sisters asked it to his face, and he never once shamed them for it. The delay is one of the hardest things in the whole book, and honest people have wrestled with it for two thousand years. Wrestle here. You will be in good company.",
      },
      {
        key: 'C', feedTag: 'MILK', signal: 'carries_burden',
        text: 'Something in my life feels like it is already in the tomb — past hoping for.',
        reflection: "Lazarus was not sick when Jesus arrived. He was four days gone — past every deadline hope had. That is precisely the situation this story was preserved for. Nothing in your life is too far gone to be called toward the light. Not even the thing you just thought of.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'open_to_god',
        text: 'What stays with me is that he wept. I need a God who cries at funerals.',
        reflection: "Then you have found the verse that has carried more grieving people than perhaps any other. Two words: Jesus wept. Whatever else turns out to be true about God, the man in this story stood at a friend's grave and cried. Start there. It is a trustworthy place to start.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
      },
    ],
    otherReflection: "Thank you for trusting this place with that. Grief spoken out loud is exactly what both sisters brought him. What you shared — ",
  },

  // 18 ── The Road to Emmaus ──────────────────────────────────────────────────
  {
    id: 'emmaus',
    narrative: [
      'Two of Jesus\'s followers walked the road to Emmaus on the worst weekend of their lives. Their teacher had been executed. Their hope had died with him.',
      'A stranger fell in step beside them and asked what they were discussing. They stopped, faces downcast: "Are you the only one who doesn\'t know what happened?"',
      'It was Jesus. Risen. Walking beside them. And they were kept from recognizing him — so he simply walked with them, mile after mile, and let them pour out the whole story of their broken hope.',
      'He listened first. Then, starting from what they already knew, he showed them what it all meant — and their hearts burned within them, though they still didn\'t know who he was.',
      'Only at the table, when he broke the bread, were their eyes opened. And he had been there the entire road.',
    ],
    question: 'They only recognized him afterward — looking back at the road. Have you ever looked back at a hard stretch of your life and wondered if something was walking with you through it?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'open_to_god',
        text: 'Yes — looking back, there are moments I cannot fully explain. Something was there.',
        reflection: "Their hearts burned on the road before their eyes ever opened at the table. That burning you have felt in hindsight is worth taking seriously — it is often how this works: unrecognized in the moment, unmistakable looking back. Let's look back together.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'carries_grief',
        text: 'I am on the Emmaus road right now — walking away from a hope that died.',
        reflection: "Then notice what he did with two people walking away — away from Jerusalem, away from the whole story. He did not stop them or turn them around. He walked their direction, at their pace, and listened to the entire grief before saying a word. That is how you will be met here.",
      },
      {
        key: 'C', feedTag: 'BRIDGE', signal: 'skeptical_of_god',
        text: 'Honestly, no — I look back and see coincidence and people helping each other.',
        reflection: "That is an honest reading, and note that the two on the road couldn't see it either — while it was happening, it just looked like a stranger and a conversation. This isn't about forcing a different interpretation on your past. It is an invitation to walk a little further and see what the evidence does. No pressure on the road.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'has_history_with_faith',
        text: 'My hope in faith itself died once. Reading this, I feel something like that burning again.',
        reflection: "That burning is the most reliable thing in the whole story — it came before understanding, before recognition, before anything was resolved. If something stirred just now, that is worth following down the road a little further. He tends to stay for the bread-breaking.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
      },
    ],
    otherReflection: "Thank you for walking that out loud. The road is long enough for the whole story — yours included. What you shared — ",
  },

  // 19 ── Breakfast on the Shore: Peter Restored ─────────────────────────────
  {
    id: 'shore',
    narrative: [
      'Peter had sworn he would die before denying Jesus. Then, in one terrible night, he denied him three times — and the rooster crowed, and Jesus turned and looked at him, and Peter went out and wept bitterly.',
      'After the resurrection, Peter went back to fishing. Back to the old life. It is what people do with unbearable failure — they go back to what they knew before.',
      'At dawn, a figure on the shore called out to the boat. It was Jesus — with a charcoal fire burning, the same kind of fire Peter had denied him beside. Breakfast was already cooking.',
      'Three times — once for each denial — Jesus asked: "Peter, do you love me?" Not "how could you," not "prove it." Just: do you love me.',
      'And three times, to the man who had failed him worst: "Feed my sheep." He gave his greatest failure his greatest job.',
    ],
    question: 'Peter went back to fishing because he thought his failure was final. Is there a failure you have quietly decided is final?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'carries_shame',
        text: 'Yes. There is something I did that I have never believed could be undone.',
        reflection: "Then look hard at the charcoal fire. Jesus rebuilt the exact scene of Peter's worst moment — and filled it with breakfast and restoration instead of shame. He does not avoid the site of the failure. He goes back to it with you and writes something new there. Yours is not final either.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'has_history_with_faith',
        text: 'I went back to my old life once, like Peter to the boats. Part of me has wondered ever since.',
        reflection: "Notice that Jesus came to the shore. Peter didn't crawl back and apologize his way in — he was found, mid-retreat, breakfast already cooking. If part of you has wondered all this time, that wondering is the shoreline. You have already been found by showing up here.",
      },
      {
        key: 'C', feedTag: 'BRIDGE', signal: 'honest_inquiry',
        text: 'I struggle with whether people — or God — can really restore trust after betrayal.',
        reflection: "That is a serious question, and the story takes it seriously: restoration wasn't a hand-wave. Three denials, three questions — it was deliberate, and it cost Peter something to answer each one. Real restoration usually does. But the story insists it is possible. Worth examining whether that holds.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'searching_for_purpose',
        text: '"Feed my sheep" — the idea that a failure could be handed a purpose stops me in my tracks.',
        reflection: "It should. It is one of the most staggering turns in the whole book: the qualification for Peter's great commission was, apparently, having failed and been loved anyway. If you are looking for purpose, this is how it tends to get handed out — to the honest, not the flawless.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
      },
    ],
    otherReflection: "Thank you for answering by the fire, so to speak. Honest words in that spot are exactly how Peter got his life back. What you shared — ",
  },

  // 20 ── The Good Samaritan ──────────────────────────────────────────────────
  {
    id: 'samaritan',
    narrative: [
      'A scholar of the law asked Jesus, "Who is my neighbor?" — the kind of question you ask when you are hoping the answer has limits.',
      'Jesus answered with a story. A man traveling to Jericho was beaten by robbers and left half dead beside the road.',
      'A priest came along — and crossed to the other side. Then a temple worker — also crossed over. The religious professionals kept their distance.',
      'Then a Samaritan came — the foreigner, the heretic, the man Jesus\'s audience was raised to despise. He saw the body, and the text says he was moved with compassion. He bandaged the wounds, put the man on his own animal, paid for his care, and promised to come back.',
      'Jesus turned the scholar\'s question inside out: not "who counts as my neighbor?" but "which of these three WAS a neighbor?" Go, he said, and do likewise.',
    ],
    question: 'Everyone finds themselves somewhere on that road. Where are you on it right now?',
    choices: [
      {
        key: 'A', feedTag: 'MILK', signal: 'carries_burden',
        text: 'In the ditch, honestly. Life has knocked me down and most people have walked past.',
        reflection: "Then the first thing this story says to you is: the walking-past was not the end of it. Help came — from the least expected direction, unhurried and thorough. Bandages, transport, paid lodging, a promise to return. That is how thoroughly you are worth helping. Someone stopping for you starts here.",
      },
      {
        key: 'B', feedTag: 'MILK', signal: 'carries_shame',
        text: 'I have been the one who crossed the road. I saw a need and kept walking, and it stays with me.',
        reflection: "The fact that it stays with you is the difference between you and the characters who crossed over — the story gives no sign it ever troubled them. A conscience that still aches is a conscience still alive. 'Go and do likewise' was spoken to someone who hadn't done it yet either. The road runs past again every day.",
      },
      {
        key: 'C', feedTag: 'BRIDGE', signal: 'honest_inquiry',
        text: 'What strikes me is that the religious people failed and the outsider got it right. That matches things I have seen.',
        reflection: "You noticed exactly what Jesus's audience noticed — and it scandalized them. He deliberately made the hero the man they were taught to despise, and the villains the men with the credentials. If religion has disappointed you, know this: Jesus told this story critiquing the same thing. The failure of the religious was his point, not his blind spot.",
      },
      {
        key: 'D', feedTag: 'MILK', signal: 'searching_for_purpose',
        text: 'I want to be the one who stops. I just don\'t always know how.',
        reflection: "The Samaritan's method was not complicated: he saw, he was moved, he went closer instead of farther. Everything else — the bandages, the inn — followed from refusing to cross the road. Wanting to be that person is where 'go and do likewise' begins. Let's work on the how together.",
      },
      {
        key: 'E', feedTag: 'MILK', signal: 'covenant_intent',
        text: 'I already know and love Jesus — and stories like this are part of why. I want to keep growing closer to Him.',
        reflection: "Then you are exactly who this is for too. Walking with Jesus is never finished — there is always more of Him to know, and more of Him to become. That hunger to grow closer is faith fully alive. Let's go deeper together and keep reaching for the fullness He offers.",
      },
    ],
    otherReflection: "Thank you for placing yourself on the road honestly. That is the question the story was built to ask. What you shared — ",
  },
];

// Every story's id, so the navigator can tell when a person has seen them all.
export const STORY_IDS = STORIES.map(s => s.id);

// Pick one story the person HASN'T seen yet (random among the unseen). Once they
// have seen them all, fall back to any — though the Hook's CTA routes straight to
// Main at that point, so in practice a fresh story shows on every cold open until
// the pool is exhausted, and never repeats before then.
function pickStory(seen: string[] = []): Story {
  const unseen = STORIES.filter(s => !seen.includes(s.id));
  const pool = unseen.length > 0 ? unseen : STORIES;
  return pool[Math.floor(Math.random() * pool.length)];
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
  const markStorySeen         = useAppStore(s => s.markStorySeen);
  const seenStoryIds          = useAppStore(s => s.seenStoryIds);
  // RETURNING mode = a cold open by someone who already finished first onboarding.
  // They get a fresh story → question → reflection, then straight into the app —
  // no name/faith step again. First-timers get the full flow (name + faith).
  const returning             = useAppStore(s => s.onboardingComplete);

  const [phase,       setPhase]       = useState<Phase>('story');
  const [story]                       = useState<Story>(() => pickStory(seenStoryIds));
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
    // Called from the faith page — the final step of onboarding. The AI-consent
    // page that used to sit here was REMOVED (Cameron, July 2026): greeting a
    // stranger with an AI disclosure made the AI look like the app's main
    // purpose. Consent still happens — honestly and fully — but at the moment
    // it matters: the first time the person opens "Talk About It" (the chat
    // screen shows the disclosure before anything can be sent, satisfying
    // Apple 5.1.1(i)/5.1.2(i) the same way). Until then aiConsent stays
    // 'unknown' and NOTHING leaves the device — off by default.
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

    markStorySeen(story.id);   // never show this opening story again
    navigation.replace('Main');
  }

  // RETURNING cold open: they've already onboarded, so a fresh story + reflection
  // is all — no name/faith again. Record the story as seen and go into the app.
  function handleReturningEnter() {
    markStorySeen(story.id);
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
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
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
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
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
              <Text style={styles.primaryBtnText}>Continue →</Text>
            </TouchableOpacity>
          </Animated.View>
        </ScrollView>
      </KeyboardAvoidingView>
    );
  }

  // ── REFLECTION ─────────────────────────────────────────────────────────────
  // (The AI-consent page that used to live between 'faith' and entering the app
  // was removed July 2026 — see handleEnter. Disclosure now happens where it
  // matters: on the chat screen, before the first message can ever be sent.)
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

          {returning ? (
            // A returning person already told us who they are — no name/faith step.
            // Reflect on the story, then walk straight back into the app.
            <TouchableOpacity
              style={[styles.primaryBtn, { marginTop: spacing.xl }]}
              activeOpacity={0.75}
              onPress={handleReturningEnter}
            >
              <Text style={styles.primaryBtnText}>Enter →</Text>
            </TouchableOpacity>
          ) : (
            <>
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
            </>
          )}
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
    fontSize: 36, fontFamily: 'Jost_400Regular', color: colors.gold,
    textAlign: 'center', marginBottom: spacing.lg, letterSpacing: 1,
  },
  sanctuaryBody: {
    fontSize: 16, fontFamily: 'Jost_400Regular', color: colors.textMid,
    textAlign: 'center', lineHeight: 27, marginBottom: spacing.xxl,
    fontStyle: 'italic',
  },

  narrativePara: {
    fontSize: 16, fontFamily: 'Jost_400Regular', color: colors.textMid,
    lineHeight: 28, marginBottom: spacing.lg, fontStyle: 'italic',
  },
  narrativeFirst: {
    color: colors.text, fontStyle: 'normal', fontSize: 17,
  },

  question: {
    fontSize: 18, fontFamily: 'Jost_400Regular', color: colors.text,
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
    fontSize: 14, fontFamily: 'Jost_400Regular', color: colors.textMid, lineHeight: 22,
  },
  choiceTextMuted: {
    fontSize: 14, fontFamily: 'Jost_400Regular', color: colors.textMuted, fontStyle: 'italic',
  },

  freeBox: { gap: spacing.sm },
  freeInput: {
    backgroundColor: colors.bgInput, borderWidth: 1, borderColor: colors.borderDim,
    borderRadius: radius.md, color: colors.textMid, fontSize: 15,
    fontFamily: 'Jost_400Regular', padding: 14, minHeight: 110, lineHeight: 24,
  },

  primaryBtn: {
    alignSelf: 'flex-start', backgroundColor: colors.gold,
    borderRadius: 26, paddingVertical: 13, paddingHorizontal: 36,
    marginTop: spacing.xl,
  },
  primaryBtnDisabled: { backgroundColor: colors.borderDim },
  primaryBtnText: {
    fontSize: 15, fontFamily: 'Jost_400Regular', color: '#15110a', letterSpacing: 0.5,
    fontWeight: '600',
  },

  reflectionText: {
    fontSize: 17, fontFamily: 'Jost_400Regular', color: colors.textMid,
    lineHeight: 30, marginBottom: spacing.xl, fontStyle: 'italic',
  },
  reflectionCoda: {
    fontSize: 14, fontFamily: 'Jost_400Regular', color: colors.textMuted,
    lineHeight: 22, marginBottom: spacing.lg,
  },

  nameHint: {
    fontSize: 13, fontFamily: 'Jost_400Regular', fontStyle: 'italic',
    color: colors.textMuted, lineHeight: 20, marginBottom: spacing.sm,
  },
  nameInput: {
    backgroundColor: colors.bgInput, borderWidth: 1, borderColor: colors.borderDim,
    borderRadius: radius.md, color: colors.textMid, fontSize: 15,
    fontFamily: 'Jost_400Regular', paddingVertical: 12, paddingHorizontal: 14,
    alignSelf: 'flex-start', minWidth: 220,
  },

  faithIntro: {
    fontSize: 18, fontFamily: 'Jost_400Regular', color: colors.text,
    lineHeight: 30, marginBottom: spacing.sm, fontStyle: 'italic',
  },
  faithQuestion: {
    fontSize: 15, fontFamily: 'Jost_400Regular', color: colors.textDim,
    lineHeight: 24, marginBottom: spacing.lg,
  },
  faithOptBtn: {
    backgroundColor: colors.bgInput, borderWidth: 1, borderColor: colors.borderDim,
    borderRadius: radius.md, paddingVertical: 14, paddingHorizontal: 18,
  },
  faithOptBtnSelected: { borderColor: colors.gold },
  faithOptText: {
    fontSize: 14, fontFamily: 'Jost_400Regular', color: colors.textMid, lineHeight: 22,
  },
  faithOptTextSelected: { color: colors.gold },
  faithHint: {
    fontSize: 13, fontFamily: 'Jost_400Regular', fontStyle: 'italic',
    color: colors.textMuted, lineHeight: 20, marginTop: spacing.md, marginBottom: spacing.sm,
  },
  faithInput: {
    backgroundColor: colors.bgInput, borderWidth: 1, borderColor: colors.borderDim,
    borderRadius: radius.md, color: colors.textMid, fontSize: 14,
    fontFamily: 'Jost_400Regular', padding: 12, minHeight: 84, lineHeight: 22,
  },
});
