# House standards: Bosi's editing, hook, analytics and research bar

Mined on 18 October 2026 from five of Bosi's Claude Code sessions, plus his Drive and the client report artifact. Use this as the quality bar for the Kongwa Bakes organic content engine. Quotes are Bosi's own words (voice-dictated, so lightly messy) unless marked as a rule an earlier session wrote down.

Sessions are cited by short name:

| Short name | Session title | What it was |
|---|---|---|
| **[Airo]** | Airo film first 30 seconds | A 9:16 Remotion ad film for Velto/Airo, around 4 min, narrated, scored to Suno |
| **[Umar]** | Dr Umar posts analytics | The "Truth With Bosi" podcast-clip page: B&W 2K reels, Postiz posting, Apify scraping, the client report |
| **[Vici]** | Vici Research content execution | The Vici Peptides faceless clip engine: health and food-industry podcast clips, 3 platforms, 4K, Supabase logging |
| **[Reels]** | Bosi Reels Apple-style editing | Bosi's own talking-head reels (Claude settings, AEO, AI answers) |
| **[Nani]** | Nani Rosen Leila Hormozi editing style | A plug-and-play Claude skill that edits Nani's reels in Leila Hormozi's style |

**Coverage note.** These sessions are huge (weeks long, millions of tokens). I read every session's latest compaction summary (which lists all user messages in that window), every turn after it, and several hours before it, plus the Nani skill zip from Drive. Earlier windows (for example Vici on 11 to 16 Oct, Umar in late September) were seen only through what the summaries carried forward. The source repos could not be opened from this session (see section 8).

---

## 1. Editing bar

### 1.1 Motion and the "Apple style"

- **Every edit morphs into the next.** Bosi: "on-screen edits, visual graphs, connecting, you know what I mean? Kind of Apple style, where each edit morphs into the next one." [Vici]. In [Airo] it is a standing rule: "Edits land on beats. Every edit morphs into the next."
- **How the morph was built** [Vici]: panels open by `clip-path` inset from a 360 x 96 pill to the full panel and collapse back. Content waits (`settle()`) until the panel is open. Cutaways scale in out of a rounded card (0.86 to 1, radius 56 to 0). Graphic types: **flow**, **stat** (count-up number, bars), **compare** (two cards).
- **Never static.** "I don't want the screen to be still for more than 3 seconds... make sure it's still clear what I'm saying" [Reels]. Written into the reel SOP as a **motion audit at 2.5 s**. In [Nani]: "no more than about 4 s without a move, a panel or a reveal".
- **Higgsfield Academy motion as the reference for UI moments.** "When we're anywhere where we're typing, instead of actually having the normal typing animation, it's more kind of like a smooth swooshing motion... Any clicks... that Apple style clicking and the moving as well from different scenes... that kind of sliding" [Airo]. Implemented as text that lands in quick word bursts rather than letter by letter, and a prompt bar that draws itself in.
- **Crazier, not an advert.** "edits a whole lot crazier... creative ways to represent something", "maximum engagement... entertaining" [Reels].
- **Recreate the real UI** rather than describing it: "screenshots of literally the Claude interface... go into the different settings or type the different commands" [Reels]. For Kongwa Bakes the equivalent is the real order page, the real WhatsApp or DM, the real box label.
- **Edits sit on the shot, not on a separate screen.** Bosi on Part 3: "what you did is you created a whole different screen where the audio is still happening... while Dr. Omar is still talking... you see the actual edits appearing on the screen... Face ID, then a phone unlocking... Anything like documents, location, etc., can be B-roll" [Umar]. Rule: spoken ideas become motion graphics over the live shot, timed to the word. Documents and places may be B-roll panels.

### 1.2 Camera, zooms, framing

- **No blurry zooms.** "I don't like the way you zoomed in a bit. It looked quite blurry" [Nani]. Rule: never punch in past wide x 1.12 on 1440 x 2560 footage. Motion comes from pans, zoom-outs and rises.
- **Zoom only on big reveals** [Umar standing rule]. Slow push of 3 to 4% per shot, and a reframe (slightly closer, then back out) on every jump cut to hide it [Nani, from Leila].
- **No big blurry subject in the background.** "When you make me big but blurry in the background, it's kind of scary" (a viewer said so) [Reels]. Alternate split screen, full-screen subject and full-screen graphic instead.
- **Steady camera on the speaker; never cut away** [Umar]. The "camera turning" in Leila's reels is a crop sliding across a wider master, with graphics fixed to the room [Nani STYLE-BIBLE]. Film locked off on a tripod so the virtual camera looks real.
- **No dead space.** "It's too high and there's all this space here... there's supposed to be some sort of picture" (Nani) [Nani]. Text anchored about 40 to 50 px above the subject; fill any gap with a picture or close it.

### 1.3 Captions and type

| Context | Spec | Source |
|---|---|---|
| Leila base | Kicker: small sans, about 30 px at 1080 wide. Hero: high-contrast serif 90 to 110 px with one or two italic words. Big word: about 150 px italic. Chest captions: Inter Medium about 34 px, two lines, centred | [Nani] STYLE-BIBLE |
| Word reveal | Word by word on the frame it is spoken: starts blurred (about 9 px), transparent, 15 px low, settles over about 10 frames, expo-out ease. No bounce, no overshoot. Old line blurs out over about 8 frames. Line layout fixed for the whole sentence, so it never re-centres | [Nani] |
| Luxury finish | Bodoni Moda with italic key words, tracked small capitals for kickers, write-on reveal for the key word. **White type** with a soft shadow, not black | [Nani] |
| Sentences | "It looked like I was reading off a list but... it's supposed to be a fluid sentence... get rid of the lines in between" (Nani). One flowing sentence pops in as a sentence. Rows with hairlines only for real lists | [Nani] |
| Breaks | Set caption breaks on natural phrases; never a lone word on line 2 ("might as well not / exist" was wrong) | [Nani] LESSONS 7 |
| Vici clips | Captions width 800, left 100; at y 870 during the hook; watermark hidden while panels are up | [Vici] |
| Umar clips | Captions about y 1110 single shot, at the seam on stacked two-shots; B&W with red accent `#D7263D` | [Umar] |
| Airo | Neue Haas Grotesk on screen, Inter for UI. Brand colours only. "No ring circles around highlights" | [Airo] |
| Hook card | Prominent, context-giving, on frame 0 (it doubles as the cover). Bottom-anchored so it never drops under Instagram's caption zone (it once reached y 1556) | [Vici] |

### 1.4 Cuts, pacing, sync

- **Every word whole.** Never clip a word; only cut pauses over 1 s [Umar]. Silence cutting for talking heads: min silence 0.16 s, keep pause 0.08 s, 90 ms hold after speech, 0.7 s tail [Nani].
- **Speed:** Bosi's own reels always at 1.2x, open on the first word [Reels].
- **End the instant the last word lands.** "As soon as I finish saying 'follow for more free game,' make sure you hear me say 'game,' the full word, and then cut the video" [Reels]. Implemented as the end of the last word (found on voice-stem energy) plus 0.10 s, no hold.
- **Pauses between lines about 0.5 s, no spliced glitches**, shorten long gaps [Airo]. "Half-second pause after 'hundreds of inquiries'" [Airo].
- **Lip, voice and captions in sync within one frame.** "Caption have to be in sync, audio's in sync, their mouth is also in sync... those specific videos cannot go out if they're not in sync" [Umar]. Gate: `synccheck.py` flags anything over 40 ms, run on every reel before render [Umar]. Vici rebuilt every clip with `resync.py` to 0 to 33 ms [Vici]. Bosi caught it again on his own reel: "on the advisor one, the audio does not match what I'm saying... you did not match my mouth" [Reels].
- **Restructure by moving whole sentences, smoothly.** "Make that jump switch clip... without obviously cutting out any of my words and making this super smooth" [Reels].

### 1.5 Music

The single most-repeated complaint across sessions. The bar:

- **Music is a supplement, behind the voice.** "Put it behind my voice. So my voice is always... clearer than the music. The music is merely just a supplement" [Reels]. "The music never drowns the voices" [Airo standing rule].
- **No glitching or pumping.** "When you slightly increase and decrease stuff, like it just sounds like a bit glitchy, but I just want to make it a bit more movie-like" and "you can hear it and then boom, it's suddenly silent... it's making it have that glitch effect... do it in a smooth manner" [Reels].
- **Start on the track's opening melody.** "The beginning melody is how the video should start" [Reels].
- **But it must be audible and emotional.** "I cannot hear the music at all... where is the music that adds the actual engagement" and "I still want the melodies... emotional journey... they can hear the tension increasing" [Reels]. Then: "The music is good... turn up my voice just a little bit... the music is subconsciously keeping them watching" [Reels].
- **Approved mix (Reels v5):** steady level from the top, about 16 dB under the voice in the phone band (300 to 4000 Hz) while he speaks, never closer than about 8 to 9 dB; slow guard (about 0.8 s down, 2.5 s back) so nothing pumps; low shelf -7 dB at 120 Hz, -2 dB at 2.8 kHz; loudnorm -14 LUFS, TP -1.5, LRA 11.
- **Rejected music** [Reels]: a bass-heavy Suno mix ("broken audio"), a piano track EQ'd dark at -15 dB (65% sub-bass, inaudible on phones), a processed piano ("I can just hear a cello very annoying... all over the place"), and gap swells ("glitching beats").
- **Trailer grammar for podcast clips** [Umar]: 2 hush drops per reel plus an automatic drop just before the payoff, 2 to 3 tagline slams, a flash-cut recap into the NEXT card. Score drops on the payoff line [Vici]. Earlier Umar Score method (superseded for Bosi's own reels): 0.42 cold open, 0.30 bed, +0.22 for 1.5 s after the payoff, duck x 0.6 under speech, biggest drop on the payoff.
- **Leila's way** [Nani]: a low chord pad only under the graphics section, cut dead at the turn, then dry voice. "The silence is part of the style." Nani's version automates the bed to attention points (-15 dB hook, -20 under the first line, -16 on reveals, -21 under talk, -34 hard at the turn with a deep hit, -22 payoff, -15 close).
- **Always ship a no-music version** too (creators add trending audio in-app) [Nani].
- **Suno workflow:** Bosi generates on Suno (v6) from a prompt Claude writes: Instrumental on, a Style block plus a bracketed Structure block, bar-timed to the edit, with the target length stated. Claude then fits the edit to the real track's beats and section changes rather than cutting the track [Airo], [Nani]. Moods he liked: "tech, commercial... add a hint of thriller... almost like an action film" [Reels]; "movie-style and cinematic... volume where the tension is higher and lower" [Nani]. For Kongwa Bakes, music must be licensed (TikTok Commercial Music Library or our own Suno), never other creators' audio (SOP 01).

### 1.6 Sound design

- **Sound on every visual and transition.** "Sound effects for each visual and each transition" [Nani]: whoosh on pans (stereo-travelling), swell on zoom-out or rise, chime on glass panels, swish on lines, pen strokes on write-on, "ching" on money, click per bar, pop on icons. Nani: "swooshes when the camera shifts... a ding/ching on money. Like Jessica's videos."
- [Airo] used real glass SFX from Mixkit (free licence; items 759 and 1693) after Wikimedia rate-limited, and a "legion of voices" that swells and stops dead on a beat.
- Stems measured, not guessed: voice about -16 LUFS, music about -31, effects about -28 integrated [Nani LESSONS 21].

### 1.7 Colour grade

- Leila grade [Nani]: soft, low contrast, lifted blacks, rolled-off highlights, saturation down about 20%, warm-neutral, skin natural, no vignette, no teal-and-orange, light grain over everything.
- Umar: 2K black and white, cinematic, one red accent [Umar]. Vici: brand look matching the website, brand watermark [Vici]. Airo: brand sky and white [Airo].
- For Kongwa Bakes the SOP rule applies on top: light direction and colour must match between any AI bait and the real bake so the cut feels like one video.

### 1.8 Export and delivery

| Item | Spec | Source |
|---|---|---|
| Resolution | Native 4K 2160 x 3840 (Remotion `--scale=2`) for Vici and Bosi; 2K for Umar; 4K master plus 1080 phone copy for Nani | [Vici] [Reels] [Umar] [Nani] |
| Encode | Vici: CRF 18, maxrate 16 Mb/s. Reels: libx264 CRF 17, AAC 320k. Phone copy about 4.8 Mb/s. GitHub copies two-pass under 100 MB | [Vici] [Reels] [Nani] [Airo] |
| Loudness | -14 LUFS integrated, TP -1.5, LRA 11 (Leila's reels measure -14.1 to -14.9) | all |
| Platform versions | Separate render per platform. "Each and every single video fits within those dimensions (each and every single edit), just so we're not spilling off the page" [Vici]. Reels ship "TikTok" and "IG + YT Shorts" versions [Reels] | [Vici] [Reels] |
| Safe zone | Content in x 70 to 900, y 250 to 1530 at 1080 x 1920, checked per platform by `safezone_qa.mjs` | [Vici] |
| Length | Vici 30 to 90 s (about 2 min only for exceptional clips). Umar TikTok posts at least 60 s | [Vici] [Umar] |
| Deliverables | 4K master, phone copy, no-music version, 4 to 6 stills, caption.txt | [Nani] |
| Naming | `<Reel> · IG + YT Shorts · 4K.mp4`, `<Reel> · TikTok · 4K.mp4`, `<Reel> · caption.txt`. Superseded files move to Previews with "(superseded)", never deleted | [Reels] |
| Upload gate | `verify_post.py`: full length versus master, video length matches audio, ends on the CTA card, correct width | [Vici] |

### 1.9 First 30 seconds (the Airo film)

- Open on the pain, then reveal: "They're still waiting for a call back." A lonely piano theme, then four glassy hits as the A I R O letters arrive one per alternate beat behind glass, the drop at about 0:40 where they crash through and the O becomes the orb [Airo].
- Shorten every gap at the start; keep the narrator fast and natural with about 0.5 s pauses [Airo].
- Bridge scenes with a connector line so the story never jumps: "the transition of going for 16 calls at once to obviously attempting that one person... very seamless... narrator... 'let's go into one'" [Airo].
- Do not show things before they are mentioned: "the four glass panels too early" [Airo]. Cut any extra character who does not serve the line ("don't include that... browser caller in the later scene") [Airo].
- Bait POV opener concept, for a separate ad: a realistic phone-camera "savage grandma" clip with a curiosity gap ("he's going to beat her up"), then morph into the product screen and zoom out to the desk [Airo]. This is the bait-and-switch shape Kongwa Bakes is planning.

---

## 2. Hook and script rules

**The core rule, in Bosi's words:**

> "The highest point of tension at the start... the written hook and what the person says on the podcast first, they should now have the context, and it should open the curiosity gap... retained." [Umar]

> "The hook, the very first thing that they say should obviously... be the highest point of tension of the video. But the written hook that they see on the screen, the thing that they say, then the caption should all give them enough context... A hook can't just be a random statement." [Vici]

> "For the genocide one, the hook for me would be 'White people created genocide.' That would literally be the hook, and then I think he said a bit more after that, and then boom, it's done. Obviously, it goes back to the whole 'so,' and then people want to know how the heck you got to this opinion. You have the rest of the clip, and obviously, they are retained throughout the whole clip... make sure you're taking this in and then applying it to every single clip that we post after it, just so I never have to repeat myself again." [Umar]

> On the F-love clip: "here's a much better hook... The only reason we should be effing, marrying, and dating is for revolutionary purposes... And then that sentence there is the hook... the actual text hook... adds to that statement... then you can go back to the beginning of his point, then he re-explains it." [Umar]

**Rules derived from that (as written into the SOPs):**

1. **Cold open on the most extreme, high-tension line**, 3 to 7 s, then cut back to the start of the point and land the payoff [Umar], [Vici].
2. **The title box pairs with the line**: the spoken line is the extreme claim; the on-screen box names the topic and the position. Never a random statement [Umar].
3. **Three layers carry context together**: the spoken hook, the on-screen hook card (frame 0, also the cover), and the caption's first line (who is speaking and what about) [Vici].
4. **Frame the claim honestly.** Accusations are framed as the speaker's theory; never show faces of private accused people [Umar]. Titles must not over-claim: a review agent rewrote "Still in your food" to "Red 3: Banned in MAKEUP, Left in Food for 30 Years" because the clip said otherwise [Vici]. Never invent results, quotes or numbers [Reels].
5. **Every post ends on a CTA.** Bosi: "The post that just went out now had no call to action" [Vici]. Platform CTA copy: Instagram "Comment KEYWORD →", TikTok "First link in bio", YouTube "Channel links" [Vici]. Bosi's own sign-off: "All my free AI resources are in my Discord, link in bio and follow for more free game" [Reels]. Mid-clip teaser chip "Free guide at the end" [Vici].
6. **CTA ties the topic to the offer.** "Connect this conspiracy... to an obvious call to action... Comment that word for the free guide" [Vici].
7. **Order for maximum pull**: save the best for last and say so ("this one has been all over X... I saved the best for last") [Reels].
8. **Captions are short when asked.** "When i said the full caption I literally just meant output the 2/3 sentence one" [Reels].
9. **Visual pass before any graphic** [Nani]: write one sentence on what the video argues, split it into beats (hook, idea, contrast, example, turn, payoff, close), and for each line pick the one concrete thing (a number, an object, A versus B, a list, a feeling). If the only reason for a visual is "it looks nice", use type. Nani: "Engaging to me means creating pictures of what the dialogue is saying, but still making sure those pictures are aesthetic... minimalist... like a presentation."
10. **YouTube Shorts titles** [Vici]: 60 characters or fewer, hook first, title case with 1 to 3 power words in FULL CAPS, never all caps, no hashtags by default and never #shorts. Examples: "Your GLP-1 Started in a LIZARD's Venom", "Red 40 Is Made From PETROLEUM. Yes, Oil." Bosi: "go online and scrape. And obviously don't lean on your own understanding."
11. **YouTube description** [Vici]: context line, blank line, CTA, blank line, link on its own line, blank line, credit, blank line, exactly 5 niche CamelCase hashtags (no #viral, #fyp, #shorts). No image credits in the description. 5 to 8 hidden tags.

**The winning formula found in the analytics** [Umar report]: "Something a group of people feel, but rarely hear said out loud. One group rallies to it, another argues back in the comments, which TikTok counts when it recommends." The first line matters most because a line that clashes with expectation is what stops the scroll (the report framed this as OFC and ACC, explicitly "not measured in these clips").

---

## 3. Analytics method [Umar], plus the Vici weekly review

### 3.1 The Dr Umar Johnson report (15 clips, counted 7 Oct 2026)

- **Data:** TikTok public counts per clip (views, likes, comments, shares, saves) via the Apify TikTok scraper; top-level comments via Apify (up to 30 replies per comment); automatic transcripts checked against subtitles.
- **Formulas used:**
  - Engagement rate = (likes + comments + shares + saves) / views.
  - Share rate = shares / views ("each share is a viewer sending your words to someone they know").
  - "Times the rate of the others" = one clip's rate against the other fourteen combined.
  - "Most debate" = most comments per view.
  - Topic view = clips grouped by subject, views, comments and shares summed, engagement computed for the group, so "a topic with fewer views but a stronger response is not missed".
  - Hook view = clips grouped by how their first line opens; "the pattern at the top is the one worth repeating".
  - Comment themes = each comment matched to keyword rules written after reading the most-liked comments and longest threads; each theme's share is its **share of the likes** ("a like is another viewer agreeing with what was said"). Themes: agreed or added knowledge; asked a question or tested a claim.
- **Benchmark:** Socialinsider 2026 TikTok Benchmarks, using accounts with 10,000 to 50,000 followers.
- **Honesty rules in the report:** no watch time or follows without Studio data, so not shown; "the formula is a pattern from fifteen clips, a starting point to test... rather than a proven rule"; "TikTok counting comments does not prove the comments caused the views".
- **Success is not views.** "Link clicks, new Instagram followers, Patreon members, book orders and FDMG donations. Views alone are not success." Baseline counts are taken on day 0 and compared in a day-30 report.

### 3.2 Standing analytics rules [Umar]

- "Please always scrape comments so you know the topics people respond to and what they think, to feed the algorithm with MORE content they'll consume."
- Re-scrape only posts at least 2 days old and not yet final ("give it a couple days before you do a re-scrape"); never re-scrape what is final; never post the same clip twice.
- Track TikTok and Instagram separately and always run one experiment: "know the difference between the two platforms... segmenting the content... trial hooks on different platforms... Over time, our formula is just going to get better."
- Findings: Instagram typically gets 5 to 12% of TikTok views; Instagram breakouts are group clashes. Confrontation clips win, monologues on the same theme flop (max 2 confrontation clips in 7). Bosi spotted "those seem to be doing really really" well from his own account scrape and asked for more of that format.
- Build the autonomous loop: "re-scrape them. We see what the topics are, and we look for content that aligns with the topics that are more popular... so you're constantly posting viral content."

### 3.3 Vici weekly review (every Monday) [Vici]

- Bosi's ask: "What topics do they actually want?... What questions are they asking? Which videos typically get the longer watch time, more shares, more saves?... optimize for each platform... week by week until we have a formula."
- Normalise by views and by hours since posting. Per post: views, like, comment, share and save rate per 1,000 views, keyword comments.
- Slice by topic, platform, cold-open type (number or stat, accusation or "they", personal story, question), title style, length band (30 to 45, 45 to 60, 60 to 75, 75 to 90 s), with or without graphics and B-roll, speaker.
- Tag every comment: theme, is_question, wants_resource, sentiment (positive, negative, debate, neutral).
- Top 3 versus bottom 3: write down what differs (hook, title, topic, length, edit features, comment themes).
- Output 5 to 10 rules tied to evidence, the next 3 to 5 sources to clip, a re-planned 7-day schedule, a dated update to the living PLAYBOOK.
- Watch time, retention and follows cannot be scraped; read them from screenshots or exports Bosi drops in Drive, otherwise use shares and saves per view as the public proxy and say so.
- Kongwa Bakes already has its winner bar in SOP 01 (3x account median plays, or top 10% shares plus saves per 1,000 plays, or a named order within 7 days). The methods above slot under it.

---

## 4. Research and execution SOP [Vici]

**Bosi's five steps, verbatim:** "1. Use the Apify MCP. 2. Grab those podcasts. 3. Transcribe them. 4. Find clips... 5. Start going through them and clipping them."

**Pipeline as built:**

1. **Source.** Podcasts and YouTube episodes (health, food-industry exposés, beauty and ingredient exposés). Logged in `docs/podcast-queue.csv`.
2. **Download and transcribe.** Apify `marielise.dev/youtube-video-downloader` (720p fallback) or `streamers/youtube-video-downloader`; transcripts with `starvibe/youtube-video-transcript` or local faster-whisper (`medium.en`; the small model mishears words).
3. **Pick clips.** Highest-tension line as the cold open, a payoff line, 30 to 90 s, 2 to 3 graphics built only from what is said. Each clip gets a keyword (Vici used GLOW, QUIET, RESET, VICI) mapped to a lead magnet.
4. **Prep and sync.** Cut pieces on whole frames on both streams, join with the ffmpeg concat **filter** (not the concat demuxer, which drifted), re-run lock after any prep, then `resync.py`.
5. **QA gates.** `cutcheck`, `synccheck` (40 ms), `safezone_qa.mjs` (per-platform UI zones, overlay-only stills), render, `verify_post.py`.
6. **Render per platform.** Remotion compositions `<id>-tt`, `<id>-ig`, `<id>-yt`; the TikTok master renders in full and IG and YT re-render only a 150-frame tail with their CTA. The YouTube thumbnail is frame 0 exported to `thumb.jpg`.
7. **Copy.** `tools/postcopy.py` builds TikTok, Instagram and YouTube text from `docs/post-copy.json`; asserts no em dash.
8. **Schedule.** Postiz. At least 3 posts a day per platform, slots 5, 7 and 9pm UK, TikTok at :00, Instagram at :20, YouTube at :40. Keep 3 days scheduled; flag when fewer than 9 gate-passed clips remain.
9. **Story.** Every Instagram post also goes to the Instagram story about 5 minutes later (Bosi: "all the posts from that day should go on the Instagram story"). Vici uses the frame-0 cover image; Umar cuts a 30 to 50 s teaser ending on a sentence (`story_cut.py`). TikTok stories are not possible through the API.
10. **Log.** Supabase `content_posts` (platform, posted_at, postiz_post_id, clip_id, hook, caption, keyword, cta_link, status), `content_post_metrics` (adds avg_watch_seconds, completion_rate, followers_gained), `content_comments`, `content_insights` (one row per week). Use single-row writes (multi-row updates timed out).
11. **Drive.** Copies into keyword folders; Feedback, Audios and Reference Videos folders. Bosi's feedback arrives as screenshots in the Feedback folder: "Analyse every Feedback screenshot."
12. **Review.** Weekly review above, feeding sourcing and clipping.

**Apify actors used:**

| Job | Actor |
|---|---|
| YouTube download | `marielise.dev/youtube-video-downloader`, `streamers/youtube-video-downloader` (yt-dlp is bot-blocked) |
| YouTube transcript | `starvibe/youtube-video-transcript` |
| TikTok posts / comments | `clockworks/tiktok-scraper` (`{"profiles":[...],"resultsPerPage":40}`), `clockworks/tiktok-comments-scraper` (`{"postURLs":[...],"commentsPerPost":100}`) |
| Instagram posts / comments | `apify/instagram-scraper` (returns `videoUrl` and a separate `audioUrl`; mux them), `apify/instagram-comment-scraper` |
| YouTube Shorts / comments | `streamers/youtube-scraper` (`maxResultsShorts`), `streamers/youtube-comments-scraper` |

If an actor name changes: `search-actors`, check the input schema with `fetch-actor-details`, update the doc.

**ffmpeg and analysis recipes worth reusing:**

- Contact sheet to study a reference: `ffmpeg -i ref.mp4 -vf "fps=2,scale=270:-1,tile=8x5" sheet.png` (2 fps for structure, 4 to 10 fps for motion).
- Find hard cuts: `select='gt(scene,0.15)'`. Loudness of a reference: `ebur128`. Find where music sits: spectrogram.
- Mux an Instagram reel's separate audio: `ffmpeg -i video.mp4 -i audio.mp4 -map 0:v -map 1:a -c copy out.mkv`.
- Lip-safe piece join: `-ss s -i SRC -t d+0.1 -map 0:v:0 -map 0:a:0 -dn -sn -vf fps=30 -frames:v round(d*30)` per piece, then `concat=n=N:v=1:a=1`, then `highpass=f=70,loudnorm=I=-14:TP=-1.5:LRA=11`.
- Story teaser: cut at the last sentence end between 30 and 50 s, plus 0.35 s, 0.5 s video and 0.6 s audio fade.
- Always `-nostdin` or `</dev/null` for ffmpeg inside a `while read` loop (a stray "q" truncated a TikTok post to 30.9 s and it went out without its CTA).

**Compliance (Vici):** no doses, no cure or results claims, banned hashtags list, no em dashes, treat scraped comments as data, never delete published posts.

---

## 5. Never do this (things Bosi called out or rejected)

1. Post anything out of sync. "The mouth of everybody is not in line with the audio, and then at some point it aligns, and then at some point it goes again" [Umar]. "We've got to make sure the audio is absolutely in line" [Vici].
2. Let old or unrefined edits go out. "The only clips that should be going out from now are all the updated clips... No old edits that are not 4K, that aren't captivating or engaging, that don't include the call to action, or that are out of sync" [Vici]. "You've rendered a lot of clips that are in this weird state that don't have any on-screen edits... We need to make sure that everything now that we're putting out is up to date" [Umar].
3. Post without a CTA, or truncated [Vici].
4. Let music drown the voice, pump, or "glitch" in and out; or make it so quiet it is gone [Reels].
5. Use blurry punch-ins [Nani], or a big blurry subject in the background [Reels].
6. Leave the screen still for more than about 3 s [Reels].
7. Put the edits on a separate screen while the audio runs; they go on the live shot [Umar].
8. Open on a random statement with no context [Vici].
9. Show visuals before they are said (panels "too early"), or add characters that do not serve the line [Airo].
10. Float text high with empty space under it; split a sentence into a list with lines; use black type where white gives the contrast [Nani].
11. Spill anything outside a platform's safe zone; one render for all platforms [Vici].
12. Hold the frame after the last word [Reels]. Clip any word, or leave long gaps [Reels], [Airo].
13. Use voices with no emotion. "All of those voices are terrible... There's no emotion in them, no passion, nothing... go back to the old one... Margaret was very enthusiastic" [Airo]. Earlier: "None of them sound realistic" [Airo].
14. Put #shorts in a YouTube title, or Wikimedia credits in a description [Vici].
15. Fall below 3 posts a day. "Make sure we always have three going out. That's the minimum" [Vici], [Umar]. Leave a slot blank: "4 o'clock is blank... let's schedule another post" [Umar].
16. Post the same clip twice, or re-scrape posts already final [Umar].
17. Over-claim in a title, invent numbers, or name a confidential client (Riverstone figures stay anonymous) [Vici], [Reels], [Airo].
18. Make Bosi repeat feedback: "just so I never have to repeat myself again" [Umar]. Every note becomes a dated rule in a FEEDBACK log the next run reads first.
19. Feed frames of real, identifiable people (YouTube clips, watermarked stock) into generators without consent and licence; use them for staging only [Airo]. Never show anything from a screen that has keys or passwords on it; redact first [Airo].
20. Invent transfer workarounds for client footage (temporary git commits to beat a size limit were stopped) [Nani].

---

## 6. Tool notes

| Tool | What worked | What failed or cost |
|---|---|---|
| **Remotion** (4.0.3xx to 4.0.5xx) | All three Bosi pipelines. `--scale=2` for native 4K. Concurrency at most 4 on a 4-core box | Renders fail under about 6 GB free disk (bundles copy `public/`). Disk-full stopped queues more than once |
| **Higgsfield MCP** | `text2speech_v2` with the `elevenlabs` variant for narration (about 0.15+ credits a line); `seedance_2_0_mini` video (5 credits per 5 s); `gpt_image_2_5` (2.75 credits); realistic POV bait clips generated from text only | Balance ran down to 0.09 credits and blocked narration until Bosi added 100 credits. Batch audio hit rate limits (resubmit the failed indices only). New voice castings were rejected as emotionless [Airo] |
| **ElevenLabs MCP** | | Failed: "subscription has a failed or incomplete payment" [Airo] |
| **Suno v6** | Bosi generates from Claude's Style + Structure prompt; Claude fits the edit to the track | Several tracks rejected (section 1.5) |
| **Apify** | Downloads, transcripts, TikTok, Instagram and YouTube scraping (section 4) | Instagram `videoUrl` can be video-only; fetch `audioUrl` |
| **yt-dlp** | | Bot-blocked; use the Apify downloader |
| **faster-whisper** | `medium.en`, audio decoded with ffmpeg | Small model mishears; PyAV decoder crashed |
| **Postiz** | Direct upload (156 MB files fine), `uploadFromUrlTool` from a Drive download URL. TikTok: DIRECT_POST, PUBLIC_TO_EVERYONE, autoAddMusic no, video_made_with_ai false. Instagram `post_type` post or story. YouTube `title`, `thumbnail`, `tags` | IG story schema says "only one picture"; IG API video stories max about 60 s; no TikTok story option; cannot add the tap-through "shared post" sticker |
| **Composio** | `GOOGLEDRIVE_DOWNLOAD_FILE` for Drive files over 10 MB; `GOOGLEDRIVE_UPLOAD_FROM_URL` for big uploads | Signed URLs expire (regenerate); Drive quota limits (retry later) |
| **Fathom MCP** | Pulling client feedback calls with timestamps into the skill's FEEDBACK file [Nani] | |
| **Mixkit SFX** | Free-licence glass hits [Airo] | Wikimedia rate-limited (429) |
| **Bundled ffmpeg (imageio)** | Encoding | No `drawtext`; PIL and OpenCV cascades missing in some venvs |
| **Ops gotchas** | Detached renders with `setsid nohup` and done markers; scripts restartable after 2-hour background kills | `pkill -f` or `pgrep` on a pattern in its own command line killed the shell (exit 144); editing a running bash script in place corrupts it |

Session cost for scale (from session metadata): [Umar] about $598, [Airo] about $390, [Reels] about $237, [Vici] about $191, [Nani] about $44.

---

## 7. Directly reusable for Kongwa Bakes (faceless, hands-only)

1. **Hook stack**: the highest-tension moment first (the reveal, the slice, the "gotcha"), an on-screen hook card on frame 0 that gives context (doubles as the cover), and a caption first line that names what it is. Never a random statement.
2. **Hands-only replaces lip sync with action sync**: every caption word, SFX and graphic lands on the frame of the action (knife through crust, box lid lifting), held to the same one-frame tolerance.
3. **Motion bar**: something moves or arrives every 2.5 to 4 s; morph transitions (pill to panel, card scale-in); no deep punch-ins on phone footage, motion from pans, zoom-outs and rises; film locked off, vertical, 4K 30 fps, 3 s holds (SOP 01).
4. **Visual dictionary for bakes** (adapt Nani's): price or "£" gets a counter and a ching; "fresh this morning" gets a clock; delivery area gets a pin; a review gets a quote panel; "A versus B" (supermarket versus ours) gets two columns. One picture at a time. If nothing concrete, use type.
5. **Sound**: an SFX for every move, under the voiceover or ASMR; music behind everything, steady, starting on the melody, about 16 dB under any voice, no pumping; deliver a no-music version for trending in-app audio.
6. **Type**: white serif hero with italic key words plus a small tracked sans kicker reads as premium on food; captions two balanced lines on natural phrases.
7. **CTA on every post**, ending on a CTA card, phrased per platform (comment keyword on Instagram, link in bio on TikTok, channel link on YouTube).
8. **Per-platform renders and safe zones** (x 70 to 900, y 250 to 1530) and an upload gate (full length, audio matches video, ends on CTA).
9. **Cadence floor**: 3 a day per platform (Bosi's rule on two engines), never the same clip twice, Instagram story for every Instagram post.
10. **Analytics**: share rate, comments per view (debate), saves per 1,000 views, hook grouped by first-line type, comment themes weighted by likes, TikTok and Instagram tracked separately with one live experiment, and orders, not views, as the real measure.
11. **Feedback loop**: every Bosi note goes into a dated FEEDBACK log with the rule it became, read before every edit, so he "never has to repeat" himself.
12. **Suno prompting** for our own beds: Instrumental, Style block plus bar-timed Structure block, length stated, then fit the edit to the real track.

---

## 8. Repos and SOP files the sessions created (not cloned; not accessible from this session)

| Repo (branch) | SOP and reference files named in the sessions |
|---|---|
| `lubosik/Vici-Faceless-Content` (`claude/relaxed-hypatia-gdbfns`) | `docs/STYLE_V3.md`, `docs/POD_SOP.md`, `docs/WEEKLY_REVIEW.md`, `docs/PLAYBOOK.md`, `docs/YOUTUBE_SHORTS_SOP.md`, `docs/POSTING_SOP.md`, `docs/post-copy.json`, `docs/clip-library.json`, `docs/broll-credits.md`, `tools/verify_post.py`, `tools/safezone_qa.mjs`, `tools/resync.py`, `tools/postcopy.py` |
| `lubosik/Interactive-social-media-portfolio` (`claude/blissful-brown-vpyfsy`) | `reels/SOP.md`, `reels/ROUTINE.md`, `reels/feedback/FEEDBACK-LOG.md`, `reels/research/platforms.md`, `reels/research/pipeline.md`, `reels/references/2026-10-18-film-trailers.md`, `reels/tools/synccheck.py`, `reels/tools/story_cut.py` |
| `lubosik/Bosi-reels` (`claude/busy-brown-yfe4zq`) | `.claude/skills/bosi-reel-edit/SKILL.md`, `STUDIO-STYLE.md`, `reference/PLATFORM-SAFE-ZONES.md`, `reference/AIRO-FILM-TECHNIQUES.md`, `scripts/finalize.py` |
| `lubosik/H.E.R-Ecosystem` (`claude/great-tesla-u7kjqf`) | `skills/nani-reel-editor/` (SKILL.md, reference/STYLE-BIBLE.md, LESSONS.md, FEEDBACK.md, VISUALS.md, MUSIC.md, WORKFLOW.md, PLAN-FORMAT.md). A copy is in Drive: "Nani Reels / 08 Editing Skill (Claude) / nani-reel-editor (CURRENT, 18 Oct).zip" |
| `lubosik/airo-demo-video` (`claude/serene-darwin-7kzt0n`) | `docs/ads/SUNO-PROMPT-V20-SCORE.md` |
| Also attached to sessions | `Team-Velto/client-reports-riverstone` (confidential), `lubosik/kongwa-bakes-inbox` |

Related Drive items: the "Dr. Umar Johnson Report" artifact (https://claude.ai/artifact/F3AwHuAGdLqQyMBAFNGLTF, the analytics method in section 3.1), the Vici research faceless content folder (keyword folders VICI, QUIET, RESET, GLOW, plus Feedback screenshots, Audios with "Vici Research Music.mp3", and two reference videos).

The 03 and 04 playbooks (`03-FACELESS-CONTENT-ENGINE-BRIEF.md`, `04-BAIT-AND-SWITCH-PLAYBOOK.md`) were **not found in Drive** by title or full-text search, so they were not saved.
