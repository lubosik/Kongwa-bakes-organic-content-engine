# Bait-and-switch and pattern-interrupt research notes (Phase 1, part A)

Prepared 18 October 2026 for Kongwa Bakes.
Companion data: `research/examples-bait.jsonl` (43 examples, schema from brief section 4.3) and `research/raw/` (trimmed scraper outputs).

This file keeps three things apart:

- **SAYS**: what an outside source says, with a link.
- **DATA**: what we scraped or measured ourselves.
- **THINK**: our inference. Every inference is labelled and should be treated as a hypothesis to test.

## Method in one screen

- **Scrapes (18 Oct 2026):** Apify `apify/instagram-scraper` (reels, profile details, hashtag reels) and `clockworks/tiktok-scraper` (profiles, search queries, hashtags, post URLs with the AI video description add-on). 11 runs in total.
- **Seed accounts:** Wants and Needs, Duolingo, Ryanair, Scrub Daddy and Liquid Death on both platforms (30 latest posts each).
- **Discovery:** TikTok searches ("bakery skit", "small business tiktok skit", "pause at the right time bakery", "fooh cgi food ad", "gotcha bakery", "psych food brand", "wait for it bakery", "pov you own a bakery", "giant croissant cgi", "bakery pause challenge", "uk bakery funny", "cafe owner skit", "fake ad bakery gotcha"), TikTok hashtags (#pauseattherighttime, #fooh, #fakeoutofhome, #gotcha, #psych, #cgiad, #bakeryskit), Instagram hashtags (#fooh, #bakeryskit, #fakeoutofhome; #pauseattherighttime returned nothing).
- **Medians:** 16 food and local TikTok accounts and 3 food FOOH Instagram accounts were then profile-scraped (20 latest posts each) so every example could be compared with its own account.
- **Median rule:** if the account had 5 or more posts in the example's calendar month inside the scrape, we use that same-month median. Otherwise we use the median of the whole scrape window and say so in `risk_notes`. Where the example sits outside the window, `risk_notes` carries a WARNING and the multiple is indicative only.
- **Video analysis:** 12 Instagram reels downloaded to `references/videos/bait/` (cap 15). Cuts measured with ffmpeg scene detection (threshold 0.35, rechecked at 0.12), hook text and scenes read from timestamped contact sheets at 1 to 2 fps, and one video checked frame by frame at 30 fps. TikTok downloads failed (yt-dlp blocked), so 17 TikToks were described by the scraper's AI video description add-on instead; those timings are approximate and labelled as such. The rest are caption-only and their timing fields are null.
- **Apify spend:** about 3.3 USD, estimated from the published per-result and per-second prices for the 11 runs (not checked against the billing console). Ceiling was 6 USD.
- **Not used:** Higgsfield (no credits).
- **Text hygiene:** em-dash characters in scraped captions were replaced with hyphens in the raw files we wrote, to meet the house rule.

## SAYS (outside sources)

### Attention and branding research

1. **Teixeira, Wedel and Pieters (2010), "Moment-to-moment optimal branding in TV commercials: preventing avoidance by pulsing", Marketing Science 29(5).**
   HBS Working Knowledge summary, "Improving Brand Recognition in TV Ads", Julia Hanna, 7 June 2010:
   https://www.library.hbs.edu/working-knowledge/improving-brand-recognition-in-tv-ads
   - Eye-tracking of "nearly 2,000 participants over 31 commercials".
   - Showing the brand in brief, repeated bursts ("pulsing") gave "an average decreased zapping of 8 to 10 percent", and up to 25 percent for some ads in a lab test.
   - The article says that if a viewer zaps after 15 seconds, a "mystery" ad that only reveals the brand at the end is "completely ineffective".
   - It gives no data on surprise as such.
2. **Teixeira, Picard and el Kaliouby (2014), "Why, When, and How Much to Entertain Consumers in Advertisements?", Marketing Science 33(6), 809 to 827.**
   https://ideas.repec.org/a/inm/ormksc/v33y2014i6p809-827.html
   - Field study: 82 ads, 178 consumers, webcam face tracking of smiles, interest and purchase intent.
   - Entertainment has an inverted-U relationship with purchase intent: moderate beats too little or too much.
   - **Entertainment placed after the brand appears is positively associated with purchase intent; entertainment placed before the brand is not.**
3. **No study we found shows that bait-and-switch converts to sales better than straight content.** The brief already noted this, and our searches did not change it.

### FOOH (fake out-of-home) and CGI

4. **Marketing Brew, "Why some brands are embracing fake out-of-home", 26 Oct 2023.**
   https://www.marketingbrew.com/stories/2023/10/26/why-some-brands-are-embracing-fake-out-of-home
   - Brands named: Maybelline, Truff with Popeyes, Jacquemus, Adidas, Mattel, Burberry, Gucci.
   - No view, engagement or sales figures are given.
   - Maybelline's VP said the aim was conversation about whether the videos were real.
   - CGI artist Ian Padgham: trying to convince people something is real "always backfires because then people just feel let down".
   - Marketers say FOOH is cheaper and faster than staging the real thing.
5. **Econsultancy and fooh.com write-ups** (search results, not fetched in full):
   https://econsultancy.com/fake-outdoor-advertising-fooh and https://fooh.com/blog/beauty-fooh-ads
   - fooh.com credits Maybelline's mascara-tube video with 76.1 million views.
   - That is a platform metric, not sales. We found no FOOH case study with sales numbers.

### Brands that link short-form video to sales (self-reported only)

6. **Scrub Daddy, Philadelphia Inquirer, 20 April 2022.**
   https://inquirer.com/business/scrub-daddy-tiktok-strategy-duolingo-20220420.html
   - CEO Aaron Krause says TikTok lets him track viewers who click through to the Smile Shop and buy: "I know exactly the ROI on that."
   - The company "has said that sales are increasing at a rate of 30% a year". The article does not tie that figure to TikTok.
   - A trade piece (https://housewareslive.net/where-entertainment-meets-e-commerce/, search summary only) quotes a Scrub Daddy UK manager saying TikTok Shop sales rose 98% in two months. No baseline is given.
7. **Duolingo** (search summaries of HubSpot, The Hustle and Business Insider):
   https://blog.hubspot.com/marketing/duolingo-unhinged-content and https://thehustle.co/how-duolingo-struck-social-gold-by-going-unhinged
   - Company-reported daily active user growth of roughly 50 to 60% in the period of its "unhinged" TikTok era.
   - The causal link to social video is the company's own framing, not a controlled measurement.

### UK rules

8. **ASA ruling on Big Fang Collective Ltd t/a Golf Fang, 24 June 2026 (upheld).**
   https://www.asa.org.uk/rulings/big-fang-collective-ltd--a26-1335555-big-fang-collective-ltd.html
   - The ad was a leaflet in a yellow and black wrapper on car windscreens reading "PENALTY CHARGE NOTICE ENCLOSED" and "WARNING". Inside it said "MADE YOU LOOK!".
   - The ASA found it was "neither obviously recognisable as such, nor its commercial nature clear" from the outset.
   - It was "likely to cause consumers immediate distress", particularly for people in financial difficulty.
   - The ASA noted the leaflet's own "SORRY FOR THE SHOCK".
   - Rules breached: CAP 2.1, 2.3 and 4.2.
9. **CAP Code wording** (https://www.asa.org.uk/type/non_broadcast/code_section/02.html and .../04.html):
   - **2.1:** "Marketing communications must be obviously identifiable as such."
   - **2.3:** "must not falsely claim or imply that the marketer is acting as a consumer ... must make clear their commercial intent, if that is not apparent from the context".
   - **4.2:** "must not cause fear or distress without justifiable reason; if it can be justified, the fear or distress should not be excessive. Marketers must not use a shocking claim or image merely to attract attention."

## DATA (our scrapes and measurements)

### Coverage

- **43 examples** in `examples-bait.jsonl`:
  - 14 Instagram, 29 TikTok.
  - 22 food and drink brands or food businesses; 7 other small local businesses.
  - 6 UK accounts: bake16.17 (Bristol), x2bakeryandpastry (London), cafelocco (Coventry), albanybooksandtoys (locationCreated GB per scraper).
- **How deeply each example was analysed:**
  - 12 were measured from the downloaded video.
  - 17 have AI-description timings.
  - 14 are caption-only.

### Wants and Needs (Instagram, October 2026): bait vs plain

We classed a reel as bait when its caption carried #funnyvideo, #skit, #challenge or #transition.

| Group (Oct 2026, n=27) | n | Median plays | Median length |
|---|---|---|---|
| Bait or skit reels | 11 | 382,023 | 22.8s |
| Plain product reels | 16 | 4,254.5 | 10.3s |

Bait reels had about 90 times the plays of plain reels on the same account in the same month. This matches the brief (474K vs 7.3K for 11 to 18 Oct).

### Mechanic vs multiple of the account's own median

Each example was tagged with one mechanic.

| Mechanic | n | Median multiple | Range | Faceless? | Example URLs (multiple) |
|---|---|---|---|---|---|
| Shop or cafe counter skit (staff vs customer, fake culprit, prank call) | 6 | 179.7x | 11.6x to 1026.7x | no (people on camera) | [albanybooksandtoys](https://www.tiktok.com/@albanybooksandtoys/video/7663169905025764629) 651.0x; [alwaysyoursbakerycafe](https://www.tiktok.com/@alwaysyoursbakerycafe/video/7540364907678666015) 1026.7x*; [iconsonsouthfield](https://www.tiktok.com/@iconsonsouthfield/video/7496619950551862571) 236.0x*; [cafelocco](https://www.tiktok.com/@cafelocco/video/7678697142889745686) 11.6x |
| Borrowed trend or game, product is the payoff | 4 | 52.7x | 26.1x to 66.0x | no | [W&N elevator roulette](https://www.instagram.com/reel/DeQVcfhv17X/) 66.0x; [W&N dont get crushed](https://www.instagram.com/reel/Defv2OTP2kt/) 59.2x; [W&N how many could you get](https://www.tiktok.com/@wantsandneedsbrand/video/7626234204136803597) 46.1x; [W&N beard filter](https://www.tiktok.com/@wantsandneedsbrand/video/7674687721205468429) 26.1x |
| Fake jeopardy or POV fantasy, then reveal | 3 | 44.2x | 1.5x to 1021.4x | no | [W&N Bugatti toy car](https://www.instagram.com/reel/DNJ_qVKsVcY/) 1021.4x*; [W&N flying car](https://www.instagram.com/reel/DelTOmuvPJO/) 44.2x; [Krispy Kreme KR "it was a dream"](https://www.instagram.com/reel/Def1gaQvXOI/) 1.5x |
| Withheld-detail caption market or stall story (stakes on the bake) | 4 | 34.4x | 25.4x to 114.4x | no, but mostly hands | [bake16.17 not expecting this order](https://www.tiktok.com/@bake16.17/video/7683623379634490646) 39.0x; [bake16.17 double check](https://www.tiktok.com/@bake16.17/video/7696981655969385750) 29.7x; [bake16.17 took a risk, sold out](https://www.tiktok.com/@bake16.17/video/7683973951772462358) 25.4x; [butterblush porch stand](https://www.tiktok.com/@butterblush.bakery/video/7679462186586098957) 114.4x |
| Hands-only tease (problem shown, product withheld, reveal next post) | 3 | 32.3x | 9.6x to 53.8x | hands-only | [Scrub Daddy bottles TT](https://www.tiktok.com/@scrubdaddy/video/7685776639694818591) 32.3x; [same on IG](https://www.instagram.com/reel/DdT9rooug0S/) 9.6x; [launch payoff](https://www.tiktok.com/@scrubdaddy/video/7688381219578334494) 53.8x |
| Parody promo with brand pulsing | 4 | 19.8x | 5.0x to 527.6x | no | [Liquid Death parenting IG](https://www.instagram.com/reel/DZFubbQyMa5/) 9.7x; [same on TT](https://www.tiktok.com/@liquiddeath/video/7646830139778583822) 527.6x (10.7x vs window); [LD oxygen-tank lady](https://www.tiktok.com/@liquiddeath/video/7584880500016172319) 29.9x |
| Topical meme text over own B-roll | 2 | 17.4x | 17.3x to 17.5x | yes | [Ryanair seat C7 IG](https://www.instagram.com/reel/Dd60lVsmJQr/) 17.5x; [TT](https://www.tiktok.com/@ryanair/video/7690989972043746582) 17.3x |
| FOOH or CGI giant product or event | 5 | 5.3x | 0.8x to 692.3x | yes | [metahousestudio AI robots natilla](https://www.tiktok.com/@metahousestudio/video/7695869849297227029) 692.3x (studio); [vifx Suntop lemonade](https://www.tiktok.com/@vifx.studios/video/7461626134459878664) 91.6x (agency); [McDonald's SG crab lorry](https://www.instagram.com/reel/DMm9tFkhpMB/) 5.3x*; [OTTO burger bar 10 years](https://www.instagram.com/reel/C4iMH60ttxP/) 4.5x*; [Krispy Kreme KR doughnut UFOs](https://www.instagram.com/reel/C5iSLD5P3-R/) 0.8x* |
| Hands-only bakery POV or transition | 2 | 3.9x | 3.5x to 4.3x | hands-only | [x2 crush croissants](https://www.tiktok.com/@x2bakeryandpastry/video/7642346479864040726) 4.3x*; [x2 transition](https://www.tiktok.com/@x2bakeryandpastry/video/7676910519017688353) 3.5x |
| Pause challenge | 7 | 2.0x | 0.5x to 1022.7x | mostly yes | [W&N 1% pause](https://www.instagram.com/reel/Dd6uS7zhY_E/) 1022.7x; [sugarland](https://www.tiktok.com/@sugarland.bakery/video/7648344484127853855) 4.2x; [bloom.and.crumbs](https://www.tiktok.com/@bloom.and.crumbs/video/7691378424899702029) 3.3x; [sicilian cookie roulette](https://www.tiktok.com/@sicilianbakerychicago/video/7598987392158043447) 2.0x; [augustpastries](https://www.tiktok.com/@augustpastries/video/7618723518984801549) 1.4x; [deli_postres](https://www.tiktok.com/@deli_postres._/video/7593899469700091149) 1.4x*; [Ryanair flicker](https://www.instagram.com/reel/Ddy_cW8Dju1/) 0.5x |
| Food collab teaser on a meme account | 2 | 0.8x | 0.5x to 1.1x | unknown | [Duolingo x Taco Bell IG](https://www.instagram.com/reel/DeJ8swnBFqN/) 0.5x; [TT](https://www.tiktok.com/@duolingo/video/7691737068392811789) 1.1x |
| Literal "Gotcha" caption | 1 | 0.3x | | unknown | [thepaperbagbakery](https://www.tiktok.com/@thepaperbagbakery/video/7545623060548685087) 0.3x* |

`*` means the post falls outside the account's scrape window, or the window spans years, so the multiple is indicative only (see `risk_notes`).

Mechanics with 3 or more examples, ranked by median multiple:

1. Counter skit (n=6)
2. Borrowed trend or game (n=4)
3. Fake jeopardy (n=3)
4. Withheld-detail stall story (n=4)
5. Hands-only tease (n=3)
6. Parody with pulsing (n=4)
7. FOOH (n=5)
8. Pause challenge (n=7)

### Pause challenges: same mechanic, very different results

| Account | Multiple | What is on screen |
|---|---|---|
| W&N | 1022.7x | Real person walking into an outline. A **single hidden reward frame** at about 1.80s reads YOU DID IT! NEW SWEATSUIT SEPT. 30, DM us screenshot for discount, with "ALMOST HAD IT / TOO SLOW, 2 frames off" frames either side. 0 cuts in 6.08s. |
| Small bakeries (5 examples) | 1.4x to 4.2x, median 2.0x | Graphics, a sliding product or pans of real bakes. None of the four with AI descriptions shows a hidden reward frame. |
| Ryanair | 0.5x | Every 2 frames shows a new ad card. There is nothing to "win", only another ad. |

### Switch timing (measured videos, plus AI-described for contrast)

| Video | Length | Switch at | Share of runtime | Device | Product seconds | CTA |
|---|---|---|---|---|---|---|
| W&N Bugatti (M) | 27.83s | 14.03s | 0.50 | hard cut | 6.86 | end card "002 RESTOCKING 8/13" |
| W&N flying car (M) | 16.44s | 10.50s | 0.64 | hard cut | 5.94 | end-card overlay "OG BLACK SET 10/20" |
| W&N dont get crushed (M) | 25.75s | about 16.6s | 0.64 | reveal | 7.45 | overlay "OG BLACK SET 10/20" |
| W&N elevator (M) | 14.90s | about 8.5s | 0.57 | reveal | about 6.4 | overlay "LINK IN BIO" |
| Scrub Daddy bottles (M) | 16.85s | 14.03s | 0.83 | hard cut to logo | 0 (tease) | caption |
| Liquid Death parenting (M) | 30.16s | 2.63s, then pulses | 0.09 | hard cut | about 10.5 over 3 pulses | end card |
| Ryanair seat C7 (M) | 6.61s | about 4.0s (text beat) | 0.61 | reveal | whole video | none |
| W&N how many (A) | 30s | about 22s | 0.73 | reveal | about 8 | caption and on-screen link in bio |
| bake16.17 took a risk (A) | 36s | about 30s (sold out) | 0.83 | reveal | about 20 | none |

- **Measured W&N pattern:** bait runs 8.5 to 16.6s, which is 50 to 64% of runtime, and the median switch is at 12.3s.
- **Product time:** 5.9 to 7.5s of product follows the switch.
- **Ending:** a date or "link in bio" text in the last 2 to 3 seconds.
- **Audio:** no stings were readable from the files. One download had no audio track, so audio is unverified.

### Counter-examples worth remembering

| Example | Multiple | What happened |
|---|---|---|
| Ryanair rapid-flicker pause | 0.5x | Every frame is the ad. |
| Duolingo x Taco Bell | 0.5x and 1.1x | Food collab teasers on a meme account. |
| Krispy Kreme KR FOOH doughnuts | 0.8x | Indicative only. |
| thepaperbagbakery "Gotcha!!" caption | 0.3x | The word "gotcha" alone does nothing. |

### Evidence of sales in our examples

- **None of the 43 posts reports revenue.**
- The only sales-like signals are self-reported in the videos themselves:
  - bake16.17 shows on screen that 185 bakes sold out in 57 minutes at Temple Quay Market, Bristol.
  - In another bake16.17 video a single customer buys the remaining stock.
- **Offer mechanics that could be counted if we ran them:**
  - W&N "DM us screenshot for discount".
  - deli_postres "minimum 2 pastries per order to play".

## THINK (our inferences, labelled, to be tested)

### T1. Mechanics that repeat across 3 or more examples with the highest multiples

1. **Counter skit (median 180x).**
   - Big multiples, but every example puts real staff or customers on camera.
   - Several examples depend on a child or a real boss.
   - THINK: the multiple is driven by relatable people, so it is the weakest fit for faceless Kongwa content. Only usable with consenting family voices off camera.
2. **Borrowed trend or game where the product is the payoff (53x).**
   - THINK: works because the first second is a format people already know.
   - The bakery version keeps the game but makes the "loser" or the last door the bake. Examples: a trend countdown, a cake box roulette, "which box has the real cake".
3. **Fake jeopardy then reveal (44x).**
   - The W&N toy-Bugatti structure maps directly onto concept B (toy van and real cake).
   - THINK: keep the jeopardy on the cake and make the toy obvious early, so CAP 2.1 and 4.2 are not stretched.
4. **Withheld-detail stall story with stakes on the bake (34x).**
   - THINK: the strongest UK, small-bakery and order-adjacent evidence we found. bake16.17 is a Bristol market baker at 25x to 39x her own median, three times in six weeks.
   - The hook withholds one fact: what was ordered, or will it sell out. The payoff is real bakes leaving the table.
   - Fits our gate perfectly, needs no AI, and can be filmed hands-only (gloved hands arranging, boxes handed over). Kongwa angles: Saturday collection and Aylesford Priory market.
5. **Hands-only tease (32x on TikTok).**
   - Scrub Daddy shows the problem with hands only, withholds the product and pays it off a week later (54x).
   - THINK: a two-post pattern for a new bake or the Friday Treat Box launch.
6. **Parody with brand pulsing (20x).**
   - THINK: this is the research-backed way to place the brand. Liquid Death shows the can at 2.6s and twice more.
   - That matches Teixeira 2010 (pulsing cuts skipping) and Teixeira 2014 (entertainment after the brand helps purchase intent; entertainment before it does not).
   - Our KB label in the first second is therefore not a compromise; it is what the evidence favours.
7. **FOOH and CGI (5x for brands).**
   - The high multiples are studio and agency portfolio accounts, not food sellers.
   - For food brands FOOH gave 0.8x to 5.3x. OTTO, a small burger bar, got 4.5x with a CGI burger on its own street, the closest analogue to concept C.
   - THINK: worth one test, not a pillar. It costs credits, and the food in it is CGI, so the real-bake product half must follow it.
8. **Pause challenge (2x for bakeries).**
   - THINK: W&N's 1023x seems to come from the **single hidden reward frame**: a "you did it" frame plus an offer and DM instruction, with "2 frames off" teasers either side. The outline game alone does not explain it.
   - Small bakeries copied the outline but not the reward frame and got 1.4x to 4.2x.
   - Concept A should add a one-frame reward with a real offer (for example "screenshot this frame for a free cinnamon knot with Saturday's order") and keep real food on screen the whole time.

### T2. Switch timing

THINK: copy the measured W&N shape.

- Hook text from frame 1.
- Bait of 8 to 14s, with the switch at roughly 50 to 65% of runtime.
- Hard cut or reveal.
- 6 to 7.5s of product in 3 to 5 shots.
- A 1.5 to 3s end card with a date ("Orders close Thursday 5pm").

Short pause-style loops (6s) are the exception: there the product is in every frame. Very late switches (above 80% of runtime) appear only in tease or story formats, where the delay is the point.

### T3. What works faceless

These mechanics worked with no face:

| Mechanic | Faceless form | Multiples |
|---|---|---|
| Hands-only tease | hands only | Scrub Daddy, 9.6x to 32x |
| Topical meme text over own B-roll | no people | Ryanair, 17x |
| FOOH | no people | 0.8x to 5x for food brands |
| Pause challenge | no people | 1.4x to 4.2x for bakeries |
| Hands-only bakery POV or transition | hands only | 3.5x to 4.3x |

The stall story can be shot hands-only. That is an untested adaptation: bake16.17 shows her face.

Everything above 40x needed people on camera:

- counter skit;
- borrowed trend;
- fake jeopardy;
- W&N pause challenge.

THINK: for those, use Mum's consented hands, family voices off camera, a consistent synthetic character labelled as AI, or a toy stand-in (the W&N toy Bugatti shows the toy can be the star).

### T4. UK compliance notes for these mechanics (applying the Golf Fang ruling)

- **Recognisable as marketing from the outset (CAP 2.1 and 2.3).**
  - Golf Fang failed because the item looked like a real penalty notice until it was read.
  - So: no fake parking tickets, police, recalls, delivery-failure notices, "breaking news" tags or official-looking notices, on screen or in the caption.
  - Krispy Kreme KR's caption opens with a fake [BREAKING] tag; we should not copy that.
  - Put the KB label in the first second. It also helps attention, per Teixeira.
- **No unjustified fear or distress (CAP 4.2).**
  - A near-miss on a cake box or a toy car is fine.
  - A realistic crash, injury, a person at risk or a lost-order panic is not.
  - The W&N Bugatti works because the "damage" is to a toy and is revealed within the video. Our version should signal play early (toy van in the first seconds, playful music) rather than at 14s.
- **People.**
  - Do not copy formats that mock a vulnerable person (the Liquid Death oxygen-tank skit) or use a child's labour as the joke (alwaysyoursbakerycafe).
  - Real customers or bosses filmed in shop need consent.
- **AI.**
  - FOOH and CGI bait must carry the platform AI label where it is realistic.
  - The product half must be our real bakes. The owner confirmed on 18 Oct 2026 that every photo and the hero video on kongwabakes.com are real bakes, so those can be used in product halves.
- **Offers in a pause frame.**
  - If we hide an offer in one frame, the terms must be true and redeemable.
  - Repeat them in the caption so nobody needs a perfect pause to see the commercial intent.

### T5. What we still do not know

- **Sales.** No example reports orders from a specific post. The bake16.17 sell-out is self-reported. Our own Monday metrics plus "How did you hear about us?" are the only way to learn whether bait brings orders.
- **Watch time and completion.** Scrapers give plays, not retention. We cannot see whether viewers leave at the switch.
- **Audio.** Whether a sting or beat drop at the switch matters. We could not verify audio on the downloaded files, and one had no audio track.
- **Platform dependence.** The same creative did 9.6x on Instagram and 32x on TikTok (Scrub Daddy), and Liquid Death's parenting ad varied similarly. We only have a few twins.
- **Small-account noise.** Accounts with tiny medians (5 to 600 plays) swing to big multiples on little reach. Several multiples sit outside the scrape window (marked `*`).
- **TikTok scene timings** come from a machine description, not frame measurement. A future pass with downloaded files would firm them up.
- **UK bakery bait examples are still thin.** We found 6 UK accounts but only one UK bakery (bake16.17) with repeatable high multiples, and no UK bakery doing a W&N-style hard-switch skit.
