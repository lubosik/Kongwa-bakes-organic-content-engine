# Bakery research notes: faceless and hands-only content that leads to orders

Phase 1 part B. Scraped and measured 18 October 2026.

Examples file: `research/examples-bakery.jsonl` (56 examples, 12 of them viewed frame by frame and cut-measured).

Raw scrapes: `research/raw/bakery-*.json`.

Downloaded reference videos (12): `references/videos/bakery/`.

How to read this file: SAYS is what a source claims. DATA is what we counted or measured ourselves. THINK is our inference, labelled as such.

---

## Method

- Instagram: `apify/instagram-scraper`, resultsType `reels`, 20 to 25 per profile, two runs (seed list, then UK and educator accounts).
- TikTok: `clockworks/tiktok-scraper`, profiles (18 to 20 latest per profile, two runs) plus one discovery search run (6 queries such as "micro bakery uk", "packing cookie orders uk", "bakery market stall setup uk").
- Multiple of median = plays divided by the median plays of that same account in the same scrape. Where the account had 5 or more posts in the same calendar month we used the same-month median; otherwise the full-scrape median. The basis is written in each record's `risk_notes`.
- Pinned posts are flagged. They are usually pinned because they already went viral, and they are often older, so their multiples are inflated. Treat any pinned multiple as an upper bound.
- 12 videos downloaded and analysed with local ffmpeg scene detection (threshold 0.35) and timestamped contact sheets. Audio was not analysed.
- Apify spend: about 1.86 USD across 6 runs (estimate from per-result prices: IG 0.0023 USD per result, TikTok 0.003 USD per result). Well under the 6 USD ceiling.
- Accounts not found: TikTok @amybakesbread, @pophamsbakery, @lannanbakery, @ikneadbread (no data). Instagram @littlespoonfarm returned an unrelated farm account and was excluded. @ikneadbread, @foodbodsourdough, @kimptonfarms and @cocomeltlondon returned no Instagram reels.
- Instagram follower counts were not in the reels scrape, so `followers` is null for Instagram records. TikTok records carry follower counts.

---

## SAYS (sources, with links)

**UK bakeries that sell through social**

- Katie's Big Bakes (Whitfield, Kent): KentOnline, 29 June 2022, says she sells out weekly stock in about two days, sells boxes of four for 16 to 33 GBP through an online shop, and one TikTok (chocolate pour) reached 1.9M views. https://www.kentonline.co.uk/dover/news/bakers-giant-cookies-go-viral-269387/
- DoughGirl (Skegness): Food Manufacture, 10 April 2025, says orders quadrupled after cookie and cookie-pie videos went viral on TikTok Shop, leading to a dedicated bakery and a new website. https://www.foodmanufacture.co.uk/Article/2025/04/10/doughgirl-invests-in-expansion-and-website/ (read via search summary; the bakeryinfo.co.uk version returned HTTP 405).
- Ooh & Aah Cookies (Northern Ireland): Irish News, 28 November 2023, reports TikTok sales at almost 60 per cent of revenue and turnover doubling. https://www.irishnews.com/business/2023/11/28/news/tiktok_success_helps_cookies_firm_to_double_sales-3802908 (search summary only).
- Maple Tree Bakes (Lincolnshire): Lincs Online reports a waiting list of more than 100 after a viral Dubai chocolate bar. Undated in results. https://www.lincsonline.co.uk/spalding/news/life-hasn-t-been-the-same-for-baker-who-recreated-viral-9404412
- Astrid (north London): Annie Ridout's Substack says it sells out of pastries within an hour every weekend after starting with breakfast boxes shared on Instagram. Paywalled. https://annieridout.substack.com/p/how-hype-makes-you-sell-out
- Heavy Hand Bakes (Cardiff): Cardiff Journalism, March 2021, says she limits monthly Instagram orders and is regularly sold out a couple of months ahead. https://cardiffjournalism.co.uk/altcardiff/2021/03/24/meet-the-bakers-cashing-in-on-instagrams-love-of-desserts/

**Self-reported by the bakeries in their own posts (still SAYS, not verified)**

- @cookiemookie_uk: "For the last few weeks we've sold out in 2 hours ... We sold out at 2:09pm." https://www.tiktok.com/@cookiemookie_uk/video/7694725720022600963
- @bake16.17 (Bristol market): on-screen "54 minutes later.. Only 3 cookies left". https://www.tiktok.com/@bake16.17/video/7683973951772462358
- @lannanpantry (Edinburgh): preorders launched so customers do not have to queue; 15-minute collection slots booked up to a week ahead via link in bio. https://www.instagram.com/reel/DRea23_iKL1/
- @kimptonfarms (US microbakery): sells a paid "Microbakery Blueprint"; caption funnels via "Comment PRICING" and a free resource. https://www.tiktok.com/@kimptonfarms/video/7569683892836322590

**Sourdough educators and keyword DM funnels**

- Comment-to-DM funnels (vendor sources, unverified): a funnel has a trigger keyword, a gate, an offer and an owned destination; tools such as ManyChat and CreatorFlow automate it. https://creatorflow.so/blog/instagram-dm-automation-course-creators/ and https://www.blotato.com/blog/manychat-examples
- No independent data on conversion rates for baker keyword funnels was found.
- Observed in captions: @amybakesbread ("Comment MONKEY and I'll DM you the recipe"), @countryroadssourdough ("comment recipes below and I'll send you the links"), @natashas_baking ("you know where to find it", website recipes). These funnel to free recipes or websites, not directly to a paid guide in the posts we saw.

**Platform guidance (all third-party or weakly sourced, treat with care)**

- Instagram original content: Instagram said in 2022 it would value original content over reposts (Tubefilter: https://www.tubefilter.com/2022/04/21/instagram-adam-mosseri-algorithm-change-original-content/). Coverage of an April 2024 change says aggregator accounts that repost unoriginal content 10 or more times in 30 days are removed from recommendations (Nasdaq: https://www.nasdaq.com/articles/instagram-updates-its-reels-algorithm-to-prioritize-original-content). We did not reach an official Instagram page.
- Reels length and ranking: third-party guides say watch time, sends per reach and likes per reach are the main signals and that recommendation to non-followers caps around 3 minutes. Not confirmed from an official source. https://www.socialpilot.co/?p=563048
- Trial reels: third-party sources say they opened to public accounts with 1,000+ followers in 2025. Not confirmed. Kongwa Bakes (31 followers) may not have access yet.
- TikTok For You feed: TikTok's eligibility standards page did not render for us. Trade coverage says repeat offenders can have the whole account made ineligible for recommendations. https://engt.co/3VXWmud

---

## DATA (what we measured)

### Scope

- 579 posts across 29 accounts with 8 or more posts each (Instagram reels plus TikTok videos and slideshows).
- 56 curated examples in the JSONL, all bakery or food, all with an order, preorder, DM, keyword or walk-in path in the caption or video.
- Faceless split in the 56 (12 viewed, 44 inferred from caption): hands-only 21 (median multiple 11.0x), fully faceless 6 (5.9x), face on screen 6 (13.9x), unclear 23 (7.3x). Inferred values are marked in each record.

### Format vs median multiple (curated examples)

Multiples are plays divided by the account's own median. P = pinned (inflated).

| Mechanic | Examples (multiple) | Faceless? |
|---|---|---|
| Short gooey "money shot", product only, 6 to 14s | katiesbigbakes TT 407.6x P, 218.1x P; doughgirluk TT 161.1x P; _cocoaclub IG 71.1x, 45.0x | hands-only or no hands |
| Market-day or sell-out story with stakes and a time stamp | bake16.17 TT 29.9x, 29.7x, 19.4x, 9.4x; cookiemookie_uk TT 13.5x, 3.2x | face in parts, middle sections hands-only |
| Gift box process-to-result reveal (occasion framing, DM to order) | _cocoaclub TT 29.5x P; IG 45.0x, 37.2x, 9.8x | hands-only |
| Hands-only process build to cross-section | countryroadssourdough TT 204.8x, IG 15.3x; lannanbakery IG 17.6x; natashas_baking IG 14.3x, TT 117.6x; pophamsbakery IG 9.5x | hands-only |
| Reply-to-comment or "someone asked" | doughgirluk TT 162.3x P; katiesbigbakes TT 60.4x P; natashas_baking IG 11.0x; ellascakedecoration TT 3.9x | mixed |
| Last-chance or time-boxed menu ("final weekend", "until Sunday", "back this weekend") | lannanbakery 17.6x; pophamsbakery 9.5x, 2.5x; chuloscookies 3.2x, 2.6x; bunsfromhome 1.6x, 0.9x | hands-only |
| Comment-keyword DM funnel | countryroadssourdough 24.5x, 15.3x, 6.9x; amybakesbread 5.2x, 2.5x, 0.9x; kimptonfarms 188.0x P | mixed |
| Counter or "day at" walk-through | lechouxlondon TT 36.2x; mikan.patisserie TT 19.2x; lannanbakery 5.5x | mostly faceless |
| Preorder logistics announcement | lannanpantry 2.6x (one static shot, staff seen from behind); chuloscookies build-a-box 2.6x | faceless |
| Photo slideshow (TikTok) | bunsfromhome 16.9x (closure news); countryroadssourdough 7.1x; doughgirluk 4.7x; _cocoaclub 1.4x P | faceless |

### Caption patterns vs reach (all 579 posts)

| Pattern | n with | median multiple with | share at 3x or more | n without | median multiple without |
|---|---|---|---|---|---|
| comment-keyword DM CTA (comment X / I'll DM) | 37 | 1.00 | 16% | 542 | 1.00 |
| "DM to order" | 37 | 0.95 | 22% | 542 | 1.00 |
| preorder / pre-order mention | 25 | 1.02 | 12% | 554 | 1.00 |
| "link in bio" | 29 | 1.12 | 24% | 550 | 1.00 |
| scarcity or deadline words (last few days, final weekend, only a week, left in stock, sold out) | 21 | 1.12 | 19% | 558 | 1.00 |
| time-boxed availability (this weekend, from Friday, back on the menu) | 28 | 1.13 | 7% | 551 | 1.00 |
| reply-to-comment or "someone asked" | 10 | 4.73 | 60% | 569 | 1.00 |
| POV or story hook in caption (nearly, not expecting, took a risk, double check) | 11 | 2.40 | 45% | 568 | 1.00 |
| pinned | 35 | 54.31 | 83% | 544 | 0.96 |

Order CTAs in captions neither help nor hurt reach (all near 1.0x). Reply-to-comment and story hooks are the only caption patterns clearly above median, on small samples (n=10 and n=11).

### Photo-led formats (owner confirmed all website photos are real bakes)

- TikTok photo slideshows: n=24 across 9 accounts. Median 0.70x of account median; only 25% beat their account median. TikTok videos from the same accounts: n=270, median 1.05x.
- The slideshows that beat median carried news or a new product: bunsfromhome closure notice 16.9x, countryroadssourdough pizza rolls 4.7x (full-scrape basis; 7.1x same-month), doughgirluk Midnight Monster Cookie Pie 4.2x (full-scrape basis; 4.7x same-month).
- Instagram carousels and photo dumps: not measured. Our Instagram runs were reels-only, so we have no carousel data. This is a gap.
- Photo pause challenges: no bakery example found in this scrape.
- Closest measured analogue to a photo: @katiesbigbakes 6.11s, 2 slow handheld pushes over a tray, no hands, no text, 3.4M plays (pinned, 2022). The motion is minimal but it is video, not a still.

### Length

- All videos (n=555, slideshows excluded): median 19.5s.
- Posts at 3x or more of median: median length 19.8s (n=98). Posts below median: 20.0s (n=268). Length did not separate winners from losers.
- By bucket: 0 to 8s median 1.00x (n=63); 8 to 15s 1.00x (n=153); 15 to 30s 1.00x (n=175); 30 to 60s 1.16x (n=99); over 60s 1.00x (n=65). Share at 3x or more peaked in 30 to 60s (23%).

### Cut rhythm (12 downloaded videos, ffmpeg scene threshold 0.35)

| Video | Length s | Cuts | Cuts per s | Avg shot s | Multiple |
|---|---|---|---|---|---|
| countryroadssourdough IG listicle | 31.6 | 27 | 0.85 | 1.13 | 24.5x |
| lannanbakery IG final weekend tart | 24.05 | 17 | 0.71 | 1.34 | 17.6x |
| bake16.17 TT market risk | 36.94 | 22 | 0.60 | 1.61 | 19.4x |
| pophamsbakery IG pain suisse | 34.34 | 20 | 0.58 | 1.64 | 9.5x |
| cookiemookie_uk TT sold out 2:09pm | 56.12 | 14 | 0.25 | 3.74 | 3.2x |
| _cocoaclub TT birthday box | 8.15 | 2 | 0.25 | 2.72 | 29.5x P |
| katiesbigbakes TT thick cookies | 6.11 | 1 | 0.16 | 3.05 | 407.6x P |
| doughgirluk TT gooey pull | 13.91 | 2 | 0.14 | 4.64 | 161.1x P |
| chuloscookies IG deadline giant cookie | 23.75 | 3 | 0.13 | 5.94 | 3.2x |
| _cocoaclub IG degree meme | 10.66 | 1 | 0.09 | 5.33 | 71.1x |
| bake16.17 TT customer order POV | 28.43 | 0 | 0.00 | 28.43 | 29.9x |
| lannanpantry IG preorders live | 6.18 | 0 | 0.00 | 6.18 | 2.6x |

- Median: 23.9s long, 0.20 cuts per second, 3.4s average shot.
- Two rhythms: process montages at 0.6 to 0.85 cuts per second (1.1 to 1.6s shots, 24 to 37s long), and single-idea shorts at 0 to 0.25 cuts per second (6 to 14s long or one continuous take).
- Detector limitation: the _cocoaclub degree meme shows at least 4 shots in its frames but only 1 detected cut (similar colours), so low cut counts are undercounts.

### Hook and on-screen text patterns (viewed videos)

- Text on screen from frame one in 6 of 12: "born to own a bakery, forced to bake as a hobby", "the process...", "POV: You're almost sold out then a customer does this..", "Only 9 people said they were definitely coming to today's market..", "Foods I stopped buying after getting a sourdough starter", "Last week, I bought 180 cookies to Walthamstow".
- No on-screen text in 5 of 12 (Lannan, Pophams, Katie's, Lannan Pantry, mostly Chulo's): the product does the hooking.
- Lower-case, one-line meme text held for the whole video (_cocoaclub, 71.1x).
- Payoff-first loop: DoughGirl's first frame is the end state, so the video loops cleanly.
- Time stamps as proof: phone lock-screen clock "14:09 SOLD OUT, AGAIN." (cookiemookie_uk), "54 minutes later.. Only 3 cookies left" (bake16.17).
- Audience poll results shown on screen as stakes: "Yes me (9 votes) / Hoping to be there (41 votes)" (bake16.17).

### CTA patterns that mention ordering

- In caption, not on screen, in 11 of 12 viewed videos. Only cookiemookie_uk put a next-step line on screen ("Next Sunday, we're trying again").
- Repeated sign-off block on every post: "DM to order! / UK-wide postals / South London collection" (_cocoaclub, every post).
- Deadline line at the top of the caption in capitals: "ONLY A WEEK LEFT TO ORDER" (chuloscookies), "LAST few days to preorder!!!" (chuloscookies).
- Stock counts: "theres just 2 x big caramel boxes available on my website" (katiesbigbakes, 5.3x), "I have 5 x mixed boxes ... left this week" (katiesbigbakes, 1.2x).
- Keyword DM: "Comment MONKEY and I'll DM you the recipe", "Comment PRICING if you want my full breakdown".
- Time-boxed walk-in: "available from this friday throughout the whole weekend" (bunsfromhome), "In all our bakeries until Sunday" (pophamsbakery).
- Preorder slots: "Simply choose your 15 minute time slot ... head to the link in our bio to reserve" (lannanpantry).

---

## THINK (our inferences, not facts)

**THINK 1. Reach comes from the video, orders come from the caption.** Order CTAs in captions sit at 1.0x of median whether present or not. The accounts that sell (Katie's, DoughGirl, Cocoa Club, Chulo's) all put the order line in the caption every time and let the video do the stopping. For Kongwa Bakes: keep "Orders close Thursday 5pm, link in bio" as a fixed caption sign-off on every post, and spend the creative effort on the first second.

**THINK 2. The strongest faceless mechanic for us is the short gooey or cut "money shot" with a one-line text hook.** Evidence: katiesbigbakes 407.6x and 218.1x (pinned), doughgirluk 161.1x (pinned), _cocoaclub 71.1x and 45.0x (not pinned). Our cinnamon knots, croissant sourdough cut and chocolate chip cookies fit this exactly. Mum's hands are enough.

**THINK 3. Gift box process-to-result is the best fit for celebration cakes and the Friday Treat Box.** _cocoaclub's "the process... / the result" with a personalised box (29.5x to 45.0x) frames the product as a present for a named occasion. That maps onto birthday cakes and office treat boxes.

**THINK 4. Scarcity and sell-out stories outperform but need care with a face.** bake16.17 (9.4x to 29.9x) and cookiemookie_uk (3.2x to 13.5x) win with stakes ("only 9 said yes"), a clock ("14:09 SOLD OUT") and empty trays. Both show the seller's face, but the middle of each video is hands-only. A faceless Kongwa version could use: Thursday 5pm order count on a phone screen, Saturday 8am filled boxes, Saturday midday empty rack. Only use real counts, never invented ones.

**THINK 5. Reply-to-comment is cheap and over-indexes.** 4.73x median on n=10, 60% at 3x or more. Small sample, but it costs nothing: answer a real question (for example "is it real sourdough?") with hands-only footage and on-screen text quoting the comment. This also suits the STARTER guide, where questions about starters can lead to "Comment STARTER".

**THINK 6. Keyword DM funnels do not add reach, they capture leads.** Comment-keyword posts sit at 1.0x of median. Their value is the DM list, not views. For the STARTER guide: put the keyword in the caption and on an end card, and judge it by DMs triggered, not plays.

**THINK 7. Last-chance menus work for bakeries with an audience already; for a 31-follower account it is mainly a reminder.** Lannan (17.6x) and Pophams (9.5x) have large local followings. For us "Orders close Thursday 5pm" is still the right weekly beat, but we expect it to serve existing followers more than to find new ones.

**THINK 8. Photo-led formats are a test, not a proven winner.** TikTok slideshows ran at 0.70x median (n=24). The exceptions carried news or a new product. With real website photos now cleared, the safest photo uses are: (a) a new-product or "back this week" slideshow carrying genuine news, (b) photos animated with a slow push in and a text hook, which behaves more like Katie's near-static 6s pan than a slideshow, and (c) Instagram carousels, which we have not measured at all. A photo pause challenge has no bakery evidence in this scrape; treat it as an experiment and compare against our own median.

**THINK 9. Two edit rhythms are enough.** Process montages at about 0.6 to 0.85 cuts per second (1.1 to 1.6s shots, 24 to 37s), or single-idea shorts at 6 to 14s with 0 to 2 cuts. Length alone did not predict winners.

**THINK 10. Pinned multiples overstate.** Most of the biggest TikTok multiples are pinned (they were pinned because they went viral). We ranked mechanics using unpinned examples where we had them.

### Which formats need a face, which work faceless

| Format | Face needed? | Basis |
|---|---|---|
| Gooey or cut money shot (6 to 14s) | No, hands or product only | viewed: katiesbigbakes, doughgirluk, _cocoaclub |
| Process build to cross-section | No, hands-only | viewed: lannanbakery, pophamsbakery |
| Gift box process-to-result reveal | No, hands-only | viewed: _cocoaclub |
| Meme text over hands-only build | No | viewed: _cocoaclub 71.1x |
| Order-deadline clip | No, gloved hands plus headless torso | viewed: chuloscookies |
| Preorder or collection logistics | No, person from behind | viewed: lannanpantry |
| Photo slideshow | No | measured: 0.70x median, weak unless news |
| Reply-to-comment explainer | Optional; works with on-screen text | mixed in data |
| Market-day sell-out story | Face used at start and end in both examples; middle is faceless | viewed: bake16.17, cookiemookie_uk |
| POV stall-cam customer interaction | Yes, seller on camera | viewed: bake16.17 29.9x |
| Listicle with eating shots | Face used | viewed: countryroadssourdough |
| Talking-head tip (educator) | Yes | bakewithjack 8.3x (not viewed) |

### What we still don't know

- Orders. No example gives order counts tied to a specific video. Press numbers (Katie's, DoughGirl, Ooh & Aah) are self-reported and not linked to single posts.
- DM keyword conversion rates for bakery or sourdough guides. Only vendor claims exist.
- Instagram carousels and photo dumps: not scraped (reels-only runs).
- Instagram follower counts for the examples (not in the reels scrape).
- Audio: we did not analyse music, voiceover or sound design in any video.
- Saves and shares on Instagram (not returned). TikTok shares and saves are in the raw files but not analysed here.
- Whether these mechanics work for a 31-follower local account. All examples are from accounts with established audiences (1.7K to 299K TikTok followers).
- Local reach: whether Medway or Kent viewers make up any share of views on similar UK accounts.
- Whether trial reels are available to @kongwabakes yet.
- 44 of 56 examples have `format` and `faceless` inferred from captions only; only 12 were viewed.
