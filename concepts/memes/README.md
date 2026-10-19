# Meme engine

Started 19 October 2026 from Bosi's reference: @doughybyzoey, "POV: you started baking sourdough to be healthy and now you eat half of a loaf everyday", a dancing fat cow over a loaf photo.

## Why memes

- **DATA (from Bosi's screen recording, 19 Oct):** the reference shows 8,067 likes, 203 comments, 381 reposts and **16.4K shares**. Shares are twice the likes.
- **THINK:** a share puts the KB label in front of someone who has never heard of us, which is exactly the reach a 31-follower account needs. Memes are also cheap enough to fix the cadence problem: the house rule is 3 posts a day per platform, and we cannot film that much bake footage yet.
- Meme-specific numbers (share rates by format, account medians) are in `research/notes-memes.md` once the meme research run finishes.

## Same account

Bosi's call: memes go on @kongwabakes and @kongwa.bakes, not a second account.

THINK: that is right for now. One account builds one follower base and one median, and every meme share sends people to a profile where the order link already is. A second account would split a tiny audience in two. Revisit if memes start pulling a national audience that never orders.

Suggested daily mix once approved: 2 memes + 1 bake post (pause, money shot, sell-out story).

## Formats (all in `templates/meme.py`)

| Format | What it is | Credits |
|---|---|---|
| Character over bake | our real bake photo, meme text box, our own chubby animal waddling in front, footstep thuds | 0 (characters already made) |
| Text over bake | real bake photo, slow push-in, one relatable line | 0 |
| Two-beat | hard cut halfway: "nobody: / me:", "mum: we have bread at home / the bread at home:" | 0 |
| Bake edit | googly eyes on the real bake, pupils drifting, one blink | 0 |

Characters (made once on Higgsfield Kling 3.0, 6.25 credits each, keyed to transparent WebM with `templates/key_character.py`):

- `assets/characters/chubby-cow-dance-alpha-v1.webm`: chubby cow, belly wobble, slow dance.
- `assets/characters/fat-seagull-waddle-alpha-v1.webm`: very round Medway seagull, smug waddle.

Every future meme with these characters costs 0 credits.

## The zero-credit Instagram route

The reference reel is an Instagram **template**. On Instagram, open the reel, tap "Use template", swap in our photo and our text, and post. It keeps the original audio and timing. Use it when a template is trending, alongside our own versions.

## Audio

All renders ship with our own footstep thuds (character memes) or silence. Add the trending sound in the app when posting:

- character memes: an upbeat or ironic dance track from TikTok's Commercial Music Library (the reference used "Northern Reverie");
- text and two-beat memes: whatever relatable sound is trending that week.

Keep the thuds on the character memes. Bosi wanted to hear the animal walking.

## Rules

- **AI label on** for anything with the cow or the seagull (they are AI-generated characters). They are obviously cartoons, never presented as real.
- **No health claims.** MEME-01's "to be healthy" is the persona's motive, a joke, and the reference uses the same line. If in doubt, swap to "to save money".
- **Real bakes only** in the background. No AI food.
- **Caption sign-off** on every meme (the research says the order line costs nothing in reach).
- **Strategic capitals** are relaxed for memes: they read native in lower case.
- **No em-dashes**, no banned phrases (`docs/05-CLAUDE-CODE-CONTENT-ENGINE-PROMPT.md`).

## How to edit and re-render

1. Edit text, photo or caption in `concepts/memes/memes.json`.
2. Run `templates/render_memes.py` (all) or `templates/render_memes.py --only MEME-07,MEME-12`.
3. Review `out/memes-v1/contact-sheet.jpg` and the videos.
