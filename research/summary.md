# Research summary: what works, what we still do not know

Kongwa Bakes organic content engine, Phase 1.
Prepared 18 October 2026.

Sources: `research/examples.jsonl` (99 examples: 43 bait-and-switch in `examples-bait.jsonl`, 56 faceless bakery in `examples-bakery.jsonl`), `research/notes-bait.md`, `research/notes-bakery.md`, 579 bakery posts measured against their own account medians, 24 reference videos cut-measured with ffmpeg.

Apify spend: about 5.20 USD (3.30 bait, 1.86 bakery), estimated from published prices.
Higgsfield spend: 0 credits.

How to read the numbers:

- **Multiple** = plays divided by that account's own median plays (same month where the account had 5 or more posts that month, otherwise the whole scrape window).
- **P** = pinned post. Pinned posts were pinned because they went viral, so treat those multiples as upper bounds.
- **\*** = the example sits outside the scrape window, so the multiple is indicative only.
- Where the two research runs measured the same bake16.17 video against slightly different medians (51,250 vs 66,900), both are shown.
- Every line below is DATA unless it starts with **THINK**.

---

## 1. The 10 strongest repeatable mechanics

Ranked by how well the evidence fits a faceless, local, order-led bakery, not just by the biggest number.

### M1. The hands-only "money shot", 6 to 14 seconds

One satisfying action on a real bake (cookie snapped, gooey centre pulled, knot torn), 0 to 2 cuts, one line of text or none.

| Example | Multiple |
|---|---|
| [katiesbigbakes, 6s cookie break](https://www.tiktok.com/@katiesbigbakes/video/7117221924333309190) | 407.6x P |
| katiesbigbakes, chocolate pour cookie | 218.1x P |
| doughgirluk, "wait until you see that centre" | 161.1x P |
| [_cocoaclub, meme text over the bake](https://www.instagram.com/reel/DbCxjUQInKg/) | 71.1x |
| _cocoaclub, birthday brownies | 45.0x |

Faceless: yes, hands only or product only.

### M2. Hands-only process build ending on the cross-section

| Example | Multiple |
|---|---|
| countryroadssourdough TikTok, giant loaf process | 204.8x |
| natashas_baking TikTok, themed scoring | 117.6x |
| lannanbakery Instagram, "final weekend" tart build | 17.6x |
| countryroadssourdough Instagram | 15.3x |
| natashas_baking Instagram | 14.3x |
| pophamsbakery Instagram, pain suisse | 9.5x |

Edit rhythm measured: 0.6 to 0.85 cuts per second, 1.1 to 1.6s shots, 24 to 37s long.
Faceless: yes, hands only.

### M3. Reply to a comment, or "someone asked"

| Example | Multiple |
|---|---|
| doughgirluk TikTok | 162.3x P |
| katiesbigbakes TikTok | 60.4x P |
| natashas_baking Instagram | 11.0x |
| ellascakedecoration TikTok | 3.9x |

Across all 579 posts: median 4.73x, 60% at 3x or more (n=10).
The only caption pattern clearly above median apart from story hooks.
Faceless: optional.

### M4. Stakes-on-the-bake story: will it sell out, what did they order

| Example | Multiple |
|---|---|
| [bake16.17, "definitely was not expecting this order"](https://www.tiktok.com/@bake16.17/video/7683623379634490646) (Bristol) | 39.0x / 29.9x |
| bake16.17, customer order story | 29.7x |
| [bake16.17, "I took a risk for today's market"](https://www.tiktok.com/@bake16.17/video/7683973951772462358), 185 bakes sold in 57 minutes (self-reported) | 25.4x / 19.4x |
| cookiemookie_uk, market stall setup | 13.5x |
| bake16.17, "nearly cancelled it" | 9.4x |
| cookiemookie_uk, "14:09 SOLD OUT" | 3.2x |

Caption story hooks ("nearly", "not expecting", "took a risk") across 579 posts: median 2.40x, 45% at 3x or more (n=11).
The best UK small-bakery evidence we found.
Faceless: the seller's face opens and closes both examples, but the middle is hands only. A fully faceless version is untested.

### M5. Gift box "the process... / the result"

| Example | Multiple |
|---|---|
| _cocoaclub Instagram, birthday brownies | 45.0x |
| _cocoaclub Instagram, "cutest presents" | 37.2x |
| [_cocoaclub TikTok](https://www.tiktok.com/@_cocoaclub/video/7696020766357294368) | 29.5x P |
| _cocoaclub Instagram, new box size | 9.8x |

One account only, so this is a strong pattern on thin breadth.
Faceless: yes, hands only.

### M6. Borrowed game or trend with the product as the payoff

| Example | Multiple |
|---|---|
| [Wants and Needs, elevator roulette](https://www.instagram.com/reel/DeQVcfhv17X/) | 66.0x |
| [Wants and Needs, don't get crushed](https://www.instagram.com/reel/Defv2OTP2kt/) | 59.2x |
| Wants and Needs TikTok, attempt counter | 46.1x |
| Wants and Needs TikTok, beard filter trend | 26.1x |

Faceless: no, every example has people. THINK: a toy, hands or the bake can play the part.

### M7. Hands-only tease, then reveal or launch

| Example | Multiple |
|---|---|
| scrubdaddy TikTok, launch reveal | 53.8x |
| [scrubdaddy TikTok, bottles tease](https://www.tiktok.com/@scrubdaddy/video/7685776639694818591) | 32.3x |
| scrubdaddy Instagram, same tease | 9.6x |

Faceless: yes. Same creative did 32x on TikTok and 9.6x on Instagram.

### M8. Fake jeopardy on an object, then the reveal

| Example | Multiple |
|---|---|
| [Wants and Needs, toy Bugatti](https://www.instagram.com/reel/DNJ_qVKsVcY/) | 1021.4x \* |
| [Wants and Needs, flying car POV](https://www.instagram.com/reel/DelTOmuvPJO/) | 44.2x |
| krispykremekr, near-miss dream | 1.5x |

Measured switch timing (Wants and Needs): bait 8.5 to 16.6s, switch at 50 to 64% of runtime, 6 to 7.5s of product, date end card.
Faceless: no in the examples. THINK: a toy van and hands can carry it (concept B).

### M9. Pause challenge, with or without a hidden reward frame

| Example | Multiple |
|---|---|
| [Wants and Needs, hidden "YOU DID IT" reward frame](https://www.instagram.com/reel/Dd6uS7zhY_E/) | 1022.6x |
| sugarland.bakery, "stop when the dot is green" | 4.2x |
| bloom.and.crumbs, pastry into a box | 3.3x |
| sicilianbakerychicago, cookie roulette | 2.0x |
| augustpastries, cake pop in the lines | 1.4x |
| deli_postres, in-store pause game | 1.4x |
| ryanair, flicker roulette | 0.5x |

The only difference we could see frame by frame: Wants and Needs hides one reward frame with an offer and a DM instruction. No bakery copied that, and the bakeries got 1.4x to 4.2x.
Faceless: yes.

### M10. Meme text held over real product footage

| Example | Multiple |
|---|---|
| _cocoaclub Instagram, "born to own a bakery, forced to bake as a hobby" | 71.1x |
| ryanair Instagram, topical meme over own B-roll | 17.5x |
| ryanair TikTok, same | 17.3x |

Lower case, one line, held for the whole clip.
Faceless: yes.

### Runners-up (evidence too weak or too costly to lead with)

- **FOOH or CGI giant product:** food brands 0.8x to 5.3x (mcdsg 5.3x, [OTTO burger bar](https://www.instagram.com/reel/C4iMH60ttxP/) 4.5x, Krispy Kreme Korea 0.8x). The huge FOOH multiples belong to CGI studios, not food sellers. Costs credits.
- **Shop counter skit:** median 180x, but every example puts staff, customers or a child on camera.
- **Last-chance menus:** lannanbakery 17.6x, pophamsbakery 9.5x, chuloscookies 3.2x and 2.6x. Works for bakeries that already have an audience.
- **TikTok photo slideshows:** 0.70x median (n=24). Only news (a closure, a new product) beat median.

---

## 2. What we still do not know

- **Orders.** Not one of the 99 examples ties order numbers to a specific post. Every sales figure is self-reported. Our own Monday metrics and "How did you hear about us?" are the only way to find out.
- **Whether any of this works from 31 followers.** Every example account already had an audience (1.7K to 876K followers).
- **Retention.** Scrapers give plays, not watch time, so we cannot see where people drop off.
- **Audio.** Nobody analysed music, voice or sound design in the references.
- **Instagram carousels and photo dumps.** Not scraped (reels only).
- **Medway reach.** Whether local viewers make up any real share of views on similar UK accounts.
- **Keyword DM conversion** for a sourdough guide. Only vendor claims exist.
- **Fully faceless sell-out stories.** Untested; the examples show the seller's face at the start and end.
- **44 of the 56 bakery examples** have `format` and `faceless` inferred from captions; 12 were watched frame by frame. TikTok scene timings in the bait set come from the scraper's machine description.

---

## 3. Which formats need a face, which work faceless

| Format | Face needed? |
|---|---|
| M1 money shot | No |
| M2 process build to cross-section | No |
| M3 reply to comment | No (on-screen comment sticker plus hands) |
| M4 sell-out story | Examples use a face at start and end; middle is hands only. THINK: phone-screen order count, boxes and empty rack can replace the face |
| M5 gift box process to result | No |
| M6 borrowed game or trend | Examples use people. THINK: toy, hands or bake as the player |
| M7 tease then reveal | No |
| M8 fake jeopardy then reveal | Examples use people. THINK: toy van plus hands |
| M9 pause challenge | No |
| M10 meme text over product | No |
| Counter skit | Yes, not for us |
| Talking-head tip | Yes, not for us |

---

## 4. Rules this research gives us

1. **Reach comes from the video, orders come from the caption.** Order lines in captions sit at 1.0x of median with or without them (579 posts). So every caption carries the same sign-off, and all the creative effort goes into the first second.
2. **Show the KB label in the first second.** Brand pulsing cut ad-skipping 8 to 10% (Teixeira 2010), and entertainment after the brand appears lifts purchase intent while entertainment before it does not (Teixeira 2014).
3. **Two edit rhythms are enough:** single-idea shorts of 6 to 14s with 0 to 2 cuts, or process montages at about 0.6 to 0.85 cuts per second. Length alone did not predict winners.
4. **A pause challenge needs a real, redeemable reward frame**, repeated in the caption so the commercial intent is clear without a perfect pause (CAP 2.1, 2.3).
5. **Keep the stakes on the bake.** No fake notices, police, recalls, crashes or people at risk (Golf Fang ruling, CAP 2.1, 2.3, 4.2).
6. **Only real numbers** in sell-out stories and stock counts.
