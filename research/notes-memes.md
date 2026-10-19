# Meme-format research notes (sourdough, home baking, bakeries)

Date: 2026-10-19. Data file: `research/examples-memes.jsonl` (44 rows). Raw: `research/raw/memes-*.json`.

## Read this first: what this pass could and could not measure

- **No new scraping happened. Apify spend was $0.00.** The first three `call-actor` runs (Instagram reels for @doughybyzoey and @sourdoughandgoods, a TikTok search for six meme queries, and a TikTok hashtag run for #sourdoughmeme, #sourdoughhumor, #bakerproblems, #sourdoughstarter and #sourdoughmemes) were all rejected with `Monthly usage hard limit exceeded`. The Apify account has reached its monthly cap.
- Direct reads of public TikTok and Instagram pages were tried as a fallback. The session's permission classifier blocked them, so I stopped. WebFetch returns only an empty "TikTok - Make Your Day" shell.
- **We therefore do not have medians for @doughybyzoey or @sourdoughandgoods.** Neither handle appears in any web index. The TikTok profile page for `doughybyzoey` returned status 10221 (no such TikTok user), so that account is probably Instagram-only.
- What the file does contain:
  - 1 row for the reference reel, using the counts the owner supplied.
  - 40 measured rows taken from earlier Apify scrapes in `research/raw`. These are meme, POV, relatable, skit and one-liner bakery posts, with TikTok shares and saves. They came from searches for skits, FOOH and bakery promos, not meme-specific searches.
  - 2 TikTok meme URLs found by WebSearch, with no metrics.
- Most rows are bakery-owner humour rather than sourdough memes. **Only 3 measured rows are about sourdough itself.** Treat the format rankings below as directional.
- **On-screen text was not captured for any scraped row,** because no video was viewed. `hook_text` comes from the caption and is marked as such in `risk_notes`. Only the reference reel has verified on-screen text.

## SAYS (what sources and platforms say)

- **Instagram ranks "sends" for reach to non-followers.** In Jan 2025 Mosseri named watch time, likes and sends as the top signals. He said sends matter slightly more for "unconnected" reach, meaning people who don't follow you. ([Social Media Today](https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/)) The common blog claim that sends weigh "3 to 5 times likes" has no Mosseri source, so treat it as unverified.
- **TikTok runs topic hubs for these meme themes:**
  - sourdough-starter-memes, sourdough-funny-meme, sourdough-bread-memes
  - its-sourdough-and-gut-healthy-meme, sourdough-starter-alive-meme
  - funny-names-for-sourdough-starter-names, horror-sourdough-starter-names, puns-sourdough-starter-names, the-office-inspired-sourdough-starter-names
  - funny-discard-sourdough-names, sourdough-bread-fail, sourdough-cafe-meme

  TikTok only builds discover pages where there is search demand, so this is evidence people look for these themes. The full list is in `raw/memes-websearch-leads.json`.
- **Starter as a pet is a mainstream idea.** TODAY.com ran "bakers think of them like pets", with name puns such as "Bread Pitt". Name lists circulate widely: Doughlly Parton, Clint Yeastwood, Bready Krueger, Jane Dough. ([TODAY](https://www.today.com/today/amp/rcna213353), [That Sourdough Gal](https://thatsourdoughgal.com/best-sourdough-starter-names-ideas-inspiration/), [Pantry Mama](https://www.pantrymama.com/best-sourdough-starter-names-the-ultimate-guide-to-naming-your-starter))
- **Other recurring jokes seen in search snippets and merch:**
  - "Sorry I can't, I have to feed my sourdough starter"
  - "Support your local sourdough dealer"
  - holding the loaf like a caught fish ([That Sourdough Gal](https://thatsourdoughgal.com/people-are-holding-their-sourdough-bread-like-fish-and-its-weirdly-perfect/))
  - the starter "fighting for her life"
  - yelling at the starter to rise
  - "it's sourdough so it's gut healthy" as an excuse
  - the "now you really can't have any" loaf tease
  - fail compilations where loaves look like bricks
- **The 2020 discard-waste backlash** ("wasteful and difficult") is the origin of the discard-guilt joke. ([AOL](https://www.aol.com/article/lifestyle/2020/04/11/twitter-forms-scoldy-take-on-new-quarantine-trend-wasteful-and-difficult/23974188))
- **TikTok MemeCut templates** appear on small sourdough accounts, for example @artisansourdoughbaker "you know exactly what I think of when I look at my drink" and @vikinamusic "Momma I made it". These are unmeasured leads.

## DATA (measured rows only; TikTok unless stated)

### Reference reel (Instagram, owner-supplied counts)

- @doughybyzoey, "POV: you started baking sourdough to be healthy and now you eat half of a loaf everyday".
- Visuals: a green-screen dancing fat cow over a loaf photo. Audio: "Northern Reverie". It is an Instagram template.
- Counts: 8,067 likes, 203 comments, 381 reposts, **16.4K shares**.
- **That is 2.03 shares per like.** No other row comes close: the best TikTok row is 0.27 shares per like.
- Plays are unknown, so we cannot calculate shares per play or a multiple of the account median.

### Share rate by meme format

Formats are grouped exclusively. "Pooled" means total shares divided by total plays.

| Format | n | Median shares/play | Pooled shares/play | Median shares/like | Median saves/play | Median x account median | Median length |
|---|---|---|---|---|---|---|---|
| Pun / text sign / one-liner / hot take | 5 | 0.29% | 0.99% | 5.9% | 0.29% | 2.59 | 26s |
| Owner-chaos POV / day-in-life / inner monologue | 8 | 0.25% | 0.65% | 7.0% | 0.35% | 2.05 | 33s |
| Family helper (kid) humour | 3 | 0.20% | 1.49% | 3.9% | 0.39% | 2.57 | 63s |
| Sourdough confession (starter fails, nearly quit) | 1 | 0.20% | 0.20% | 5.1% | 0.97% | 51.6 | 40s |
| Expectation vs reality / fail-then-win | 4 | 0.08% | 0.06% | 1.5% | 0.12% | 1.25 | 26s |
| Customer/staff skit | 8 | 0.04% | 0.02% | 1.8% | 0.33% | 0.78 | 11s |
| MemeCut/Meme template, SFX edit, TV-clip reaction | 5 | 0.03% | 0.07% | 0.8% | 0.34% | 0.83 | 14s |
| *Contrast: pop-culture character bake (not a meme)* | 2 | 1.22% | 1.75% | 12.3% | 0.51% | 86 | 34s |

### Top individual rows by shares per play

1. [natashas_baking, Demogorgon bake](https://www.tiktok.com/@natashas_baking/video/7571528849863838990) (contrast row). 16.5M plays, 332K shares, 2.01% shares/play, 54.5x window median.
2. [cookiemookie_uk, "a cookie with personality"](https://www.tiktok.com/@cookiemookie_uk/video/7613823176144932118). 36.3K plays, 608 shares, 779 saves, 1.68% shares/play, 25% shares/like, 3.75x window median.
3. [alwaysyoursbakerycafe, kid "staff" joke](https://www.tiktok.com/@alwaysyoursbakerycafe/video/7540364907678666015). 3.9M plays, 58.2K shares, 1.49% shares/play, 10s long. It is about 1,027x its 2021 to 2026 window median, so that median is skewed by a long tail of old posts.
4. [lechouxlondon, "wise words" shop-sign meme](https://www.tiktok.com/@lechouxlondon/video/7309442582558297377). 423.6K plays, 4,120 shares, 0.97% shares/play, 16.5% shares/like, 67.9x window median.
5. [cookiemookie_uk, sold out at 2:09pm](https://www.tiktok.com/@cookiemookie_uk/video/7694725720022600963). 31.1K plays, 277 shares, 0.89% shares/play, 3.2x median.
6. [cookiemookie_uk, mum brain + business brain chaos](https://www.tiktok.com/@cookiemookie_uk/video/7662443289777753347). 87.6K plays, 590 shares, 0.67% shares/play, 9.1x median.
7. [cookiemookie_uk, "POV: Friday night as a bakery owner"](https://www.tiktok.com/@cookiemookie_uk/video/7669127717396188438). 23.2K plays, 115 shares, 0.50% shares/play, 5.6x the same-month median (n=6).
8. [countryroadssourdough, sourdough journey confession](https://www.tiktok.com/@countryroadssourdough/video/7637913523334466846). 228K plays, 464 shares, **2,223 saves**, 0.20% shares/play, 51.6x median. The Instagram version had 710K plays (4.8x median).

### Skits travel but are rarely shared

- [mistieunderhill cake skit](https://www.tiktok.com/@mistieunderhill/video/7007528376944725253): 4.0M plays, 0.02% shares/play.
- [learnwithjess "Karen" skit](https://www.tiktok.com/@learnwithjess/video/7537428540468350239): 3.4M plays, 0.02% shares/play.
- Both earn high saves and follows (the series hook) rather than sends.

### Instagram rows

- None of the Instagram rows in the old scrapes have share counts.
- [natashas_baking, "When your sourdough is ready for Halloween before you are"](https://www.instagram.com/p/Dd1liWVMGBQ/): 25.1M plays, 26.5x the same-month median.
- [bakewithjack, "nobody will say this on the internet"](https://www.instagram.com/p/DdXFExgE2wi/): 180K plays, 8.3x the same-month median.

### Audio

- Strong rows mostly use original sound: the cookiemookie_uk and lechouxlondon posts, and countryroadssourdough.
- Some use a licensed theme or instrumental, for example "Theme from Nightmare Before Christmas" and "The Look - Instrumental".
- MemeCut and template rows carry the template's sound.
- The reference reel uses "Northern Reverie", a calm instrumental under a ridiculous visual. The contrast is part of the joke.

### Length

- One-liner and sign memes: 15 to 26s.
- Top kid joke: 10s.
- Owner POVs: 23 to 72s.
- The reference template is a single static photo, so it is probably 5 to 10s (not measured).
- Skits under 15s get plays but few shares.

## THINK (interpretation, not proven)

1. **The share engine is "this is literally me / you".** The rows with the most shares per like are confessions and one-liners a viewer forwards to a specific friend: the reference reel (2.03), a cookie with personality (0.25), the kimptonfarms "overthinking" post (0.29, tiny base) and the shop-sign meme (0.17). Skits and generic templates get watched, not sent.
2. **Mean or "Karen" humour gets plays but not shares,** and it fails the family-bakery test. Self-deprecating humour aimed at the baker is safest and shares best.
3. **A static photo + text + green-screen animal + calm audio is cheap,** template-able and faceless. The reference shows it can hit 16K shares. Kongwa could make one a week from its own loaf photos, with a licence-cleared animal clip (or our own family dog or cat) and Commercial Music Library audio.
4. **Pop-culture character bakes out-share every meme** in our data (1.2 to 2.0% shares/play). That is a bake-led share format, not a meme, and it uses third-party IP. Worth noting for seasonal UK moments, but keep any IP references generic.

### 15 most relatable sourdough or bakery meme themes

"Observed" means on-screen text or caption seen in a source; "draft" is our suggested wording for Kongwa. All 15 offend nobody and suit a family bakery unless noted.

1. **Healthy hobby, whole loaf eaten.** Observed: "POV: you started baking sourdough to be healthy and now you eat half of a loaf everyday". Evidence: the reference reel, 16.4K shares.
2. **"It's sourdough so it's gut healthy" excuse.** Draft: "It's sourdough. It's basically a vegetable." TikTok discover page exists. Keep it obviously a joke, not a health claim.
3. **Naming the starter.** Draft: "Me introducing my starter, Clint Yeastwood, to guests before my children." Evidence: TODAY, name lists, 6+ TikTok discover hubs.
4. **Starter as a pet or child.** Draft: "Sorry, can't come out tonight. Have to feed my starter." Evidence: merch, TODAY. It also links to the free starter rescue guide.
5. **Starter "fighting for her life" / rescue.** Draft: "POV: your starter is fighting for her life and you're googling at 2am". This links directly to the STARTER keyword CTA.
6. **Discard guilt.** Draft: "Me pouring 100g of discard down the sink like it's a crime scene." Evidence: the 2020 backlash and a "funny discard names" hub.
7. **The 2-week starter wait.** Draft: "Day 9 of my starter. Still nothing. Still believing." Based on beginner struggle content. Its relatability is untested here.
8. **First good loaf triumph / "Momma I made it".** Evidence: @vikinamusic MemeCut lead, and the countryroadssourdough confession (2,223 saves).
9. **Fail then win.** Observed: "Worth the 12 tries". Observed: "Froggy got a little toasty but the inside was perfectly fluffy". Low share rate in our data. Better as a "we've all been there" confession than as a fail reveal.
10. **Starter on the brain** (seeing it in your coffee, lava lamps, everywhere). Evidence: the @artisansourdoughbaker MemeCut lead.
11. **Holding the loaf like a fish.** Draft: "Me with every loaf I've ever made." Evidence: That Sourdough Gal. Easy family-friendly visual.
12. **Cutting it hot / "now you really can't have any".** Draft: "Everyone in my house when the bread is 3 minutes out of the oven." Evidence: search snippets. The "partner reacting" variant fits with a consenting family member.
13. **Friday night as a baker / bakery-owner life.** Observed: "POV: Friday night as a bakery owner." Data: 0.50% shares/play, 5.6x median.
14. **Family helpers.** Observed: "POV: Your 5-year-old is your camerawoman." Observed: "I fear my 5 year old has taken over the business." Data: the top kid row has 58K shares. Use only with parental consent.
15. **Sold out again / "a cookie with personality" one-liners.** Observed: "We sold out at 2:09pm... HOW MANY COOKIES DO I NEED TO BAKE?!" (0.89% shares/play). Observed: "a cookie with personality" (1.68%).

Also seen but riskier: customer-mocking skits (offend customers), TV-clip reaction memes (copyright), and "TikTok views are trash" complaints (off-brand, 0 shares).

## What we still don't know

- Medians, plays, share counts and posting cadence for @doughybyzoey and @sourdoughandgoods. We also don't know which template the reference used, or who made the cow asset and what its licence is.
- Share counts on Instagram Reels for any sourdough meme. Only the reference reel has them.
- True sourdough-meme rows from the requested searches ("sourdough meme", "sourdough starter name", "sourdough discard", "sourdough pov", "baker meme", "bakery meme") and hashtags (#sourdoughmeme, #sourdoughhumor, #bakerproblems, #sourdoughstarter), sorted by popularity.
- Verified on-screen text, length and audio for scraped rows. That needs `aiVideoDescription` or a manual view.
- Whether green-screen animal memes beat text-only memes on shares per play. Our data has no green-screen rows with plays.
- UK versus US relatability, since almost all rows are US or London.

## Next step when Apify resets (est. under $1.50)

1. `apify/instagram-scraper` with `directUrls` [doughybyzoey, sourdoughandgoods], `resultsType: reels`, `resultsLimit: 40`, and `maxTotalChargeUsd: 0.5`. Also run hashtag reels for sourdoughmeme and sourdoughhumor.
2. `clockworks/tiktok-scraper` with `searchQueries` (the 6 above), `searchSection: /video`, `videoSearchSorting: MOST_LIKED`, `resultsPerPage: 15`, and `maxTotalChargeUsd: 1`.
3. `clockworks/tiktok-scraper` with `hashtags` (5 tags) and `resultsPerPage: 15`. Then profile-scrape the top 4 meme accounts for medians.
4. Use `postURLs` for the 2 leads in this file.
