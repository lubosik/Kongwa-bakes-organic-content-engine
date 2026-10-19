# Week 43 review (19 to 23 October 2026)

Five drafts, all made from real Kongwa Bakes photos and the real website hero clip.
No filming, no AI generation, 0 Higgsfield credits.

Captions, hashtags and destinations: `captions.json`.
Each draft has a 4K file (`_captioned.mp4`, 2160x3840), a phone copy (`_captioned-1080.mp4`) and a cover (`_cover.jpg`, frame 0).

Bosi: write **approve**, **edit** (with the change) or **kill** next to each one.
Nothing gets scheduled until it says approve.

---

| Day | File | Concept | What is real, what is graphic | Your call |
|---|---|---|---|---|
| Mon 19 | `2026-10-19_k08-pause-cinnamon-knot` | K08 photo pause, hidden reward | Real photo (cinnamon buns). Ring, text and reward card are graphics. | |
| Tue 20 | `2026-10-20_k03-meme-steam-sourdough` | K03 meme over real footage | Real website hero clip (first 2.3s, before the house graphic), slowed 2.5x. Text burned in. | |
| Wed 21 | `2026-10-21_k10-pause-roulette-saturday` | K10 pause roulette | 10 real photos with real names and prices. | |
| Thu 22 | `2026-10-22_k18-thursday-last-call` | K18 last call | 10 real photos, including the real packed-orders shot. | |
| Fri 23 | `2026-10-23_k08-pause-cookie` | K08 photo pause, hidden reward | Real photo (cookies). Graphics as Monday. | |

---

## Decisions needed before any of these go out

1. **The reward (K08, Mon and Fri).** The hidden frame says "screenshot this and DM us for 10% off your first order". This uses the site's existing first-order offer. Approve, or name a different reward (for example a free cookie with a Saturday order).
2. **Sourdough ingredients (K03).** The caption says "flour, water, salt and a few days". The site says some loaves use wholemeal or rye. Confirm this is exactly true of the country loaf.
3. **This week's menu (K10, K18).** Confirm every item shown is on this Saturday's menu at the price shown.
4. **Audio.** K03 and K18 are silent and K08 and K10 have our own synthesised clock ticks. Add a trending sound from TikTok's Commercial Music Library in the app when posting, and keep it under any on-screen action. The house rule of a no-music version is covered: these files are it.
5. **Accounts.** Postiz has no Kongwa Bakes TikTok or Instagram connected yet. Connect @kongwa.bakes and @kongwabakes in Postiz and I will schedule the approved ones.

---

## Compliance gate (brief 5.1)

| Check | K08 knot | K03 steam | K10 roulette | K18 last call | K08 cookie |
|---|---|---|---|---|---|
| Obviously playful from frame 1 | yes, game | yes, meme | yes, game | yes, plain | yes, game |
| Stakes on the bake only | yes | yes | yes | yes | yes |
| No real person shown badly | no people | no people | no people | no people | no people |
| No fake customers or reviews | yes | yes | yes | yes | yes |
| Real food in the product half | real photo | real footage | real photos | real photos | real photo |
| AI label needed | no | no | no | no | no |
| Own or licensed audio | own ticks | none yet | own ticks | none yet | own ticks |
| Facts true | needs reward approval | needs ingredient check | needs menu check | needs menu check | needs reward approval |
| Offer repeated in caption (CAP 2.1) | yes | n/a | n/a | n/a | yes |

## Realism and house QA (brief 6.2, house standards)

| Check | Result |
|---|---|
| Hands, skin, faces | none in frame |
| Light match between bait and product | single source per video |
| Warped text or fake marks | all text burned in with ffmpeg and PIL, brand fonts (Fraunces, Mulish), real KB monogram |
| Safe zone x 70 to 900, y 250 to 1530 | all text and labels inside; checked on extracted frames |
| KB label in the first second | yes, frame 0 on all five |
| Hook card on frame 0, doubles as cover | yes |
| Loudness | ticks measure about -21.5 LUFS (sparse clicks cannot reach -14 without clipping); final level is set by the in-app sound |
| Every post ends on a CTA | order chip on screen the whole time; caption sign-off on all five |
| No em-dashes | checked with `scripts/check-emdash.sh` |

## What to watch on Monday 26 October

- Plays against our own median (TikTok 8 followers, Instagram 31 followers, so any baseline is new).
- DMs with a K08 screenshot: these are countable orders from a single post, the evidence no researched example had.
- Comments on K10 ("what did you land on").
