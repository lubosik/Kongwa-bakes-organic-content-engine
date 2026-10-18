# Kongwa Bakes: website context

Source: crawl of https://kongwabakes.com on 18 October 2026 (sitemap + BFS of internal links), rendered screenshots (Playwright, Chromium), page HTML, CSS and JSON-LD.
Everything below is quoted or measured from the live site unless it is prefixed **THINK:**, which marks my inference.

Related files:
- Screenshots: `references/website/screenshots/<slug>-mobile.(png|jpg)` (390x844 @2x, full page) and `<slug>-desktop.(png|jpg)` (1440 wide, full page). Home is JPEG q80 because the PNG exceeded 4MB.
- Plain text of every page: `references/website/text/<slug>.txt`
- Image library: `assets/library/website/` + `assets/library.json` (34 entries: 33 images + 1 hero video)
- Brand assets: `assets/brand/`

---

## 1. Pages found

Sitemap: `robots.txt` points to `/sitemap-index.xml` -> `/sitemap-0.xml` (16 URLs). `/sitemap.xml` and `/sitemap_index.xml` return 404. BFS from every page found no further internal pages. Site is built with Astro, hosted on Vercel.

| URL | Status | One-line summary |
|---|---|---|
| `/` | 200 | Home: hero video, FHRS 5 badge, full menu with basket/checkout (Stripe), Our Story, packaging, "Proof, not promises" photos, credentials, delivery areas. |
| `/bakery/` | 200 | "A bakery in Kent that bakes for you, not for a shelf": made-to-order explainer, town list, FAQ on delivery and Saturdays. |
| `/bakery/rochester/` | 200 | Town page (ME1 and ME2), free delivery over £25, FAQ (weekday collection, festival weekends). |
| `/bakery/chatham/` | 200 | Town page (ME4 and ME5), FAQ (other sourdough bakery in Chatham, Chatham Maritime, cutoff). |
| `/bakery/gillingham/` | 200 | Town page (ME7 and ME8), FAQ (Hempstead and Wigmore, Priestfield match days, ME7 near Rainham). |
| `/bakery/strood/` | 200 | Town page (ME2), FAQ (crossing the river, Frindsbury and Wainscott, early collection for trains). |
| `/bakery/rainham/` | 200 | Town page (ME8), £2.50 delivery charge, FAQ ("there are three Rainhams"). |
| `/cakes/custom/` | 200 | Custom cake quote form, 5-photo gallery, "at least 10 days" notice. |
| `/catering/` | 200 | Catering and events enquiry form, "at least 14 days" notice, credentials block. |
| `/contact/` | 200 | "Not on the menu? Just ask": phone, email, question form. |
| `/sourdough/` | 200 | Guides hub, links to the two guides. |
| `/sourdough/what-real-sourdough-is/` | 200 | "What is sourdough bread?": three ingredients, label reading, FAQ. Bylined to Hilary Kongwa. |
| `/sourdough/starter-guide/` | 200 | "How to make a sourdough starter": honest two-week guide, "day four" problem, FAQ. |
| `/legal/terms/` | 200 | Terms of sale: cutoffs, 12:30 hold, cancellations, allergens, delivery area. |
| `/legal/privacy/` | 200 | Privacy policy: Stripe, postcodes.io, Resend, Google Workspace, Trustpilot, GA. |
| `/legal/cookies/` | 200 | Cookies: `kb-consent` and Google Analytics only. |
| `/trade/` | **404** | Does not exist (see Gaps). Screenshot saved as `trade-404-*`. |
| `/order/` | **404** | Does not exist. Ordering lives at `/#order`. |

Other probes returning 404: `/shop`, `/about`, `/events`, `/cafes`, `/markets`, `/wholesale`. `/cakes` 301-redirects to `/#cakes`.

---

## 2. Products (exact names, prices, sizes, descriptions)

All products carry the line "Fresh, Medway collection or local delivery". Section headings on the home page: "The launch menu", "Fresh from Medway, made to order", "The bread counter" ("Real sourdough, fermented for days, baked the morning you collect it."), "The cake counter" ("Celebration cakes from eight inch up to twelve, iced and finished by hand. Bigger, smaller or tiered is a custom quote.").

### The bread counter

| Product | Price | Description (exact) |
|---|---|---|
| Sourdough Country Loaf | £5.50 | "Naturally leavened, long fermented, a deep open crumb under a crackling crust." |
| Sourdough Rolls (box of 6) | £4.50 | "The same slow-fermented dough, shaped small for the table or a lunchbox." |
| Croissant Sourdough Loaf | £5.95 | "An enriched sourdough bread laminated with butter, resulting in a croissant-style texture and taste. A sourdough-croissant hybrid." |
| Croissant Sourdough Rolls (box of 6) | £5.50 | "All the lamination of the loaf, shaped into rolls for sharing." |
| Focaccia | £6.50 | "Soft, dimpled and olive oil rich bread, topped with rosemary." |
| Brioche Loaf | £7.25 | "Rich, buttery, and lightly sweet. Excellent toasted or on its own." |
| Brioche Buns (box of 6) | £5.50 | "Soft, golden, and just sweet enough. Brilliant for burgers or breakfast." |
| Cinnamon Buns (box of 6) | £5.00 | "Hand-twisted cinnamon knots, thickly spiced and soft-proofed until deep golden-brown." |
| Chocolate Chip Cookies (box of 6) | £4.25 | "Thick, chewy, and loaded with chocolate." |
| Banana Muffins (box of 6) | £5.50 | "Moist, generously spiced, made with properly overripe bananas." |
| Banana Loaf | £6.75 | "Our banana muffin batter, baked as a whole loaf. Properly overripe bananas, warm spice, and a crust worth fighting over." |
| Pretzels (each) | £3.25 | "Golden-brown, salted, and properly chewy, the way a soft pretzel should be." |

### The cake counter (sizes: 8 inch serves about 20 / 10 inch serves about 28 / 12 inch serves about 40)

| Product | 8 in | 10 in | 12 in | Description (exact) |
|---|---|---|---|---|
| Victoria Sponge | £45.00 | £60.00 | £75.00 | "Two golden sponges with whipped cream and raspberry jam between them, dressed with fresh strawberries, raspberries and kiwi. The cake everyone recognises, made properly." |
| Chocolate Fudge Cake | £52.00 | £67.00 | £82.00 | "Deep chocolate sponge under a thick coat of chocolate buttercream, piped by hand and finished with fresh strawberries." |
| Red Velvet Cake | £52.00 | £67.00 | £82.00 | "Soft crimson sponge with a gentle cocoa note, layered with real cream cheese frosting rather than buttercream pretending to be it." |
| Carrot and Walnut Cake | £48.00 | £63.00 | £78.00 | "Warm with cinnamon and nutmeg, heavy with grated carrot, finished with cream cheese frosting and toasted walnuts." |
| Guinness Marble Cake | £55.00 | £70.00 | £85.00 | "Stout makes chocolate taste more like chocolate. Marbled through a vanilla swirl and topped flat and white, like the head on a pint." |
| Blueberry and Cream Cake | £50.00 | £65.00 | £80.00 | "Vanilla sponge studded with blueberries, softly whipped cream, and more blueberries piled on top. Lighter than it looks." |
| Heart Cake | £48.00 | £63.00 | £78.00 | "Heart shaped and covered in hand piped rosettes. For anniversaries, engagements, and the occasional apology." |
| Lemon Drizzle Cake | £12.00 (single size, loaf) | | | "A loaf, baked then soaked in lemon and sugar while still warm so the syrup goes all the way through. Sharp, sticky, and gone quickly." |
| Cupcakes (box of 6) | £16.00 | | | "Vanilla sponge under a tall swirl of buttercream, piped one at a time. Good on their own, better next to a cake." |

Cakes show as "from £X" on the card (the 8 inch price).

### Custom cakes (quote only, `/cakes/custom/`)
- Home card: "Something else entirely / Custom cakes, made to your brief / Tell us the occasion, how many layers and how many people, and we will come back with a design and a price. Birthdays, weddings, christenings, anything you have in mind." CTA "Ask for a quote".
- Page: "A number for a birthday, tiers for a wedding, a flavour that is not on the counter, or a picture you saw and cannot stop thinking about. Fill this in and we will come back with a design and a price."
- Gallery captions: "Two tiers, summer berries", "Ferrero Rocher", "Chocolate and gold", "A guitar, because they asked", "Whatever the occasion is".
- Form options. Occasion: Birthday, Wedding, Christening or naming, Anniversary, Engagement, Corporate or office, Funeral or wake, Something else. Layers: One to Four or more, "Tiered, stacked separately", "Not sure, advise me". People: Up to 10, 10 to 20, 20 to 40, 40 to 80, More than 80. Flavour: Victoria sponge, Chocolate fudge, Red velvet, Carrot and walnut, Guinness marble, **Coffee and walnut** (not on the menu), Lemon drizzle, Blueberry and cream, Something else.

### Catering and events (quote only, `/catering/`)
"We bake for birthdays, weddings, christenings, wakes and office mornings across Medway and the rest of Kent. Grazing tables, pastry platters, sandwich rounds, celebration loaves. Tell us about the day and we will put a menu and a price together for you." Guest bands: Under 20, 20 to 50, 50 to 100, 100 to 200, More than 200. Occasions add "Church or community".

### Stated ingredients

**Sourdough (exact wording, `/sourdough/what-real-sourdough-is/`):**
- "Sourdough bread consists of only three ingredients: flour, water and salt. That is the whole list."
- "Three ingredients and a great deal of time."
- "Flour, water and salt, fermented for days, made for the Saturday you choose rather than baked ahead for a shelf."
- On their own flour: "Any bread flour. Ours is strong white, with wholemeal or rye in some loaves."
- "Starter, sometimes listed separately. Fine. A starter is only flour and water."
- Process cards: "Starter: Flour and water, left until a culture establishes itself in it." / "Dough: Starter, flour, water and salt, mixed and left to ferment."
- Not on the site as a product-level ingredient list: the Sourdough Country Loaf and Sourdough Rolls cards have no ingredient list. THINK: the guide wording is the de facto ingredient claim for the plain sourdough.

**From real printed labels visible in `/images/proof/packed-orders.jpg` (transcribed from the photo):**
- Croissant Sourdough Rolls: "INGREDIENTS: WHEAT flour, water, sourdough starter (WHEAT flour, water), butter (MILK), honey, EGGS. For allergens, see ingredients in bold. CONTAINS: WHEAT (GLUTEN), MILK, EGGS." Net weight 430g, "Contains: 6 croissant sourdough rolls", "Storage: Store in a cool, dry place. Keep sealed."
- Banana Muffins: "INGREDIENTS: Bananas (36%), WHEAT flour, BUTTER (MILK), EGGS, sugar, brown sugar, salt, cinnamon, raising agents (baking powder, sodium bicarbonate), vanilla. FOR ALLERGENS, SEE INGREDIENTS IN BOLD." "Box contains: 6 muffins", net weight 670g.
- Label furniture: "Kongwa Bakes / Baked by family, made for yours." with a wheat sprig, "Made by: Kongwa Bakes, Homemade in Kent, UK", hello@kongwabakes.com, Instagram @kongwabakes, "THANK YOU FOR SUPPORTING SMALL".
- Allergens (terms page): "Everything is made in one family kitchen that handles nuts, gluten, eggs, milk and soya. Allergen information for the 14 named allergens is available on request for every item, per Natasha's Law."

---

## 3. Ordering rules

- **Bake day:** Saturday. "Collection and local delivery are Saturday mornings, between 8am and midday."
- **Deadline:** "Order any time up to Thursday at 5pm and we will have it ready for you that Saturday. Anything after that goes into the following week's bake."
- **Earlier days:** "Need it before Saturday? You can pick an earlier day in the basket. Either way it takes two clear days' notice, because the sourdough is fermented for days and cannot be hurried." Terms: "Those need two clear days' notice, closing at 5pm two days before." Checkout lists the next six Saturdays plus a weekday group (Mon to Fri).
- **Live ordering banner** (JS, Europe/London): rendered on 18 Oct 2026 as "Order by Thursday at 5pm for Saturday 24 October 2026." When rolled over: "This Saturday's bake is closed. You are ordering for ...". When under 24h: "X hours Y minutes left".
- **Collection:** "Medway, Kent, 8am to midday". Exact address is not published: "We send the exact address with your confirmation email." Hold: "we will hold your order until 12:30". Collection is open to anyone in Kent.
- **Delivery:** "Medway and the surrounding villages, the morning of your day, free". Checkout requires a £25 basket ("ADD £25.00 TO UNLOCK DELIVERY", `data-minimum-pence="2500"`). Postcode checked against the real local authority boundary via postcodes.io. "We ring before we set off." Rainham: "a small delivery charge of £2.50". Schema lists delivery prefixes ME1, ME2, ME3, ME4, ME5, ME7, ME8.
- **Areas:** Rochester (ME1 and ME2), Chatham (ME4 and ME5), Gillingham (ME7 and ME8), Strood (ME2), Rainham (ME8), plus named spots: Chatham Maritime, Dockside, Hempstead, Wigmore, Rainham Mark, Frindsbury, Wainscott.
- **Custom cakes:** "We need at least 10 days for a custom cake. Boards and dowels get ordered in, and icing does not rush."
- **Catering:** "We need at least 14 days for an event, and more for anything over fifty guests."
- **Big basket nudge:** baskets over £60 (`data-threshold-pence="6000"`) show "That is a proper order. If it is for an event, our catering side can build a menu around it and price it properly."
- **Payment:** "Secure payment by Stripe. Apple Pay, Google Pay and card accepted." Discount code field at checkout. Phone number collected "by call or text on the morning".
- **Cancellations:** full refund if before the Thursday 5pm cutoff; after that "we cannot promise a refund". Problems: email within 48 hours with a photo.
- **Marketing:** "10% off your first order" email popup (code saved on device, "One code per person, used once"); SMS opt-in at checkout ("A few texts a month at most ... Stop any time by replying STOP.").

---

## 4. Trust signals

- **Food hygiene rating 5** ("Rated 5 for food hygiene, the top of the scale"). "Medway Council, routine inspection, 29 September 2026". "The inspection found no contraventions of food law, and all three scored areas (hygiene and food safety, the condition of the premises, and confidence in management) were scored at the best level." FHRS ID 1987253, https://ratings.food.gov.uk/business/1987253. Official FHRS badge SVGs saved in `assets/brand/`.
- **Food safety qualification:** "Hilary Kongwa holds the Level 2 Food Safety in Catering qualification from the Chartered Institute of Environmental Health (CIEH)", certificate dated 4 September 2026. "Hilary is named on our council inspection report as the food business operator".
- **Insurance:** "Public liability cover up to £5,000,000, held by Kongwa Bakes LTD through Simply Business", 30 September 2026 to 29 September 2027. CTA "Ask for a copy of the certificate" (mailto with subject "Insurance certificate request").
- **Reviews:** Trustpilot only: "Enjoyed your bake? We'd love to hear about it. Review us on Trustpilot" (https://uk.trustpilot.com/review/kongwabakes.com). No star rating, review count or testimonial quotes appear anywhere on the site. Customers are auto-invited to Trustpilot after their bake (privacy page).
- **Proof:** "Proof, not promises / Already trusted for the big days": "Catered for a full corporate grazing table, breads, cheeses, charcuterie and pastries, served fresh for a Medway office event. Every order goes out boxed and labelled with what is in it, whether it is one loaf or a table for forty."
- **Legal entity:** "Kongwa Bakes LTD" (schema legalName). Footer: "© 2026 Kongwa Bakes. Owned by the Kongwa Group. Made with love in Medway, Kent. Powered by Kongwa Tech".
- **Privacy stance:** "We are a family bakery, not a data business." / "We never sell your data."

---

## 5. People

- **Hilary Kongwa:** head chef. "Hilary is head chef, shaping every loaf by hand with real care and no shortcuts." Schema: founder, jobTitle "Head Chef". Byline on the sourdough guide: "Written by Hilary Kongwa, who keeps our starter and bakes every loaf that leaves this kitchen." CIEH Level 2 holder and named food business operator.
- **The Kongwa Family:** "Kongwa Bakes is run by The Kongwa Family from our kitchen in Medway, Kent." / "Hilary and the family mix, shape and bake everything themselves." / "A family bakery in Medway, Kent. Baked by The Kongwa Family, led by head chef Hilary Kongwa." / delivery "is the family driving, not a courier."
- **"Mum":** the word does not appear anywhere on the site. THINK: if Hilary is Mum, the site never says so; video content can introduce that relationship but it is not yet a site fact.

---

## 6. Brand voice: real lines of copy

1. "Baked By Family, Made For Yours." (slogan, hero H1, footer)
2. "We are not trying to be a big brand pretending to be small. We are a small family doing this properly: real fermentation, real time, and bakes that taste like someone actually made them, because someone did."
3. "Every batch comes out of our own kitchen, not a factory line."
4. "A bakery in Kent that bakes for you, not for a shelf"
5. "The sourness is not an ingredient. It is a by-product of waiting."
6. "You are paying for the days, not for the flour."
7. "The crust tells you nothing. Anyone can dust flour on a loaf and score it with a blade. The ingredients list is the only thing that cannot be styled."
8. "So ask the baker how long their ferment is. Anyone doing it properly will tell you immediately, and probably at length, because it is the thing they are proudest of. A shrug is an answer too."
9. "The reason so many people fail is not technique, it is that nobody warns them about day four."
10. "If you throw your starter away, it will almost certainly be on one of these two days. Do not."
11. "This will get you a working starter. It will not get you our bread, and it would be dishonest to suggest otherwise."
12. "We are not going to publish our formulas, and any bakery that says it has is either lying or not very good."
13. "Heart shaped and covered in hand piped rosettes. For anniversaries, engagements, and the occasional apology."
14. "Real cream cheese frosting rather than buttercream pretending to be it."
15. "No, and it is worth saying plainly because there are three Rainhams."
16. "Add your flat number in the notes at checkout so we are not standing outside a block of two hundred flats guessing."
17. "Would rather someone else did the waiting?" / "Or let us do the waiting"
18. "Wrapped as carefully as it's baked"

Voice traits (facts about the copy): British spelling, plain words, no exclamation marks, no em-dashes anywhere on the site, short declarative sentences, honest caveats ("It is not a health food, and it is emphatically not gluten free"), dry humour, repeated words "properly", "honest", "real", "time", "days".
THINK: the voice is "honest family baker who refuses to oversell"; videos should lead with time and process, use deadpan humour, and avoid hype words.

---

## 7. Visual identity

### Colours (CSS custom properties in `/_astro/schema.BHa05Aet.css`)

| Token | Hex | Role (from CSS) |
|---|---|---|
| `--kb-cream` | `#FBF3E2` | page background (`--bg`), `theme-color` meta |
| `--kb-crust` | `#2E1C12` | text (`--text`), footer background, monogram disc |
| `--kb-honey` | `#E39A3B` | primary CTA (`--cta`), "Order Now" button |
| `--kb-hearth` | `#C15B33` | CTA hover (`--cta-hover`), script eyebrow text, prices, "Send my code"/"Ask for a quote" buttons |
| `--kb-hearth-deep` | `#B04E28` | deeper terracotta |
| `--kb-emerald` | `#10715A` | accent (`--accent`), text links |
| `--kb-wheat` | `#EAD8B3` | panels (`--panel`) |
| `--kb-gold-bright` | `#F6E3AE` | monogram gold gradient highlight |
| `--kb-gold-mid` | `#D4AF6A` | monogram gold gradient mid |
| `--kb-gold-shadow` | `#8A6A2E` | monogram gold gradient shadow |
| (literal) | `#2F6B4F` | used 3 times in CSS (green) |

Shadows use crust at low alpha (`#2e1c1229`, `#2e1c121a`). Radii: 10px, 18px, pill 999px.

### Fonts (self-hosted via Fontsource in `/_astro/`, no Google Fonts `<link>`)
- Display: `--font-display: "Fraunces Variable", "Fraunces", serif` (H1 80px weight 480 on desktop; H2 weight 600). Monogram letters use Fraunces 600.
- Body: `--font-body: "Mulish", system-ui, sans-serif` (400/700/800; buttons Mulish 800).
- Script: `--font-script: "Sacramento", cursive` (eyebrows such as "from our family kitchen", "Custom cakes", footer slogan, in `#C15B33`).
- All three are Google Fonts families, so they are free to use in video: Fraunces, Mulish, Sacramento.

### Logo
- Monogram "KB": dark crust disc, thin gold ring, gold-gradient serif K and B with a wheat stalk drawn diagonally between them. Inline SVG in the header (`aria-label="Kongwa Bakes monogram"`), wordmark "Kongwa Bakes" in Fraunces beside it.
- Saved: `assets/brand/kb-monogram.svg` (site SVG, CSS vars resolved to hex, references Fraunces), `kb-monogram-1024-transparent.png` (rendered with Fraunces, transparent background), `kb-favicon.svg` (Georgia fallback version), `kb-monogram-1024-tiktok-avatar.jpg` (TikTok profile image, same mark).
- Kraft and label assets: `kb-kraft-band-mark-crop.jpg` (from the packaging image), `kb-round-sticker-real-crop.jpg` (real kraft round sticker: KB disc, "Kongwa Bakes", "Baked by family, made for yours"), `product-label-banana-muffins-real-crop.jpg`, `product-label-croissant-sourdough-rolls-real-crop.jpg`. Also `fhrs-5-badge-large.svg`, `fhrs-5-badge-small.svg`, `kongwa-tech-powered-by-logo.png` (agency credit, not the bakery's mark).

### Visual style observations (from screenshots and photos)
- Warm cream page, dark brown text, honey-orange pill buttons, terracotta script eyebrows, rounded cards with soft shadows, generous whitespace. Footer is dark crust brown with honey headings.
- Home hero: full-bleed muted looping video of a split steaming loaf on a wooden table, dark overlay, cream Fraunces headline "Baked By Family, Made For Yours.", two pill buttons ("Order Now" filled honey, "Our Story" outlined).
- A sticky dark basket bar ("0 items £0.00 / Checkout") sits under the hero on every page.
- Product photography: square 1200x1200, mostly shot in a home kitchen on a dark speckled granite worktop with white plates and window light; boxed items in kraft boxes. Country loaf is the only portrait shot (1400x1867).
- Real packaging (packed-orders photo): white boxes with round kraft KB stickers, a mint-and-pink striped muffin box with window, kraft stand-up pouches with a white printed label, kraft paper bags with windows.
- THINK: the hero poster, hero video, OG card and the `packaging/label.jpg` kraft-band image look AI-generated (golden haze, perfect steam, glowing house shape in the loaf). Carrot and walnut, lemon drizzle and Guinness marble photos have a different wooden-table, golden-light style and may also be generated. The granite-worktop set, custom cake gallery and the three "proof" photos look like genuine phone photos. For short-form video, the real photos are the credible material; the generated ones should not be passed off as real bakes.

---

## 8. CTAs and key URLs

| CTA text | Target |
|---|---|
| Order Now (header + hero) | `/#order` |
| Our Story | `/#story` |
| See this week's bake / See the menu / See the bread counter | `/#order` |
| Or the cakes | `/#cakes` |
| Ask for a quote | `/cakes/custom/` (form posts to `/api/cake-quote`) |
| Tell us about it / Tell us about your event / Tell us what you need | `/catering/` (form `#catering-form`, posts to `/api/catering`) |
| Just ask us | `/contact/` (posts to `/api/ask`) |
| Ask for a copy of the certificate | `mailto:hello@kongwabakes.com?subject=Insurance%20certificate%20request` |
| Check it on the Food Standards Agency register | https://ratings.food.gov.uk/business/1987253 |
| Review us on Trustpilot | https://uk.trustpilot.com/review/kongwabakes.com |
| Send my code (10% off) | posts to `/api/subscribe` |
| Pay | Stripe via `/api/checkout` |

Home anchors that exist: `#order`, `#cakes`, `#story`, `#proof`, `#credentials`. Catering anchors: `#catering-form`, `#credentials`.
Guides: `/sourdough/`, `/sourdough/starter-guide/`, `/sourdough/what-real-sourdough-is/`.
**Not present:** `/trade/` page and anchors `#events`, `#cafes`, `#markets`; any Instagram comment keyword such as "STARTER" (the word only appears in normal guide copy). The nearest trade content is the home/catering block "For cafés, offices and event planners / Hygiene, training and insurance, with the dates" and "Buying for a café, an office or an event? Tell us what you need" -> `/catering/`.

Contact: hello@kongwabakes.com, 07480 342608 (tel:+447480342608), "Call or text".

---

## 9. Social

| Platform | URL / handle | What I could fetch |
|---|---|---|
| Instagram | https://www.instagram.com/kongwabakes/ (@kongwabakes, also printed on labels) | Not reachable without login: HTTP 429 redirect to `/accounts/login/`; the web profile API returned 401 "require_login". Nothing recorded. |
| TikTok | https://www.tiktok.com/@kongwa.bakes (@kongwa.bakes) | Public page fetched. Nickname "Kongwa Bakes". Bio: "Family bakery in Medway, Kent. Real sourdough, breads + cakes, baked to order." Bio link https://kongwabakes.com/. 8 followers, 2 following, 126 likes, 7 videos (as of 18 Oct 2026). Business (commerce) account, not verified. Avatar = KB monogram. Video list was not included in the server-rendered data. |
| Facebook | https://www.facebook.com/profile.php?id=61593976350416 | Not fetched (link only). |
| LinkedIn | https://www.linkedin.com/company/kongwa-bakes-ltd/ | Not fetched (link only). |

Note the handle mismatch: Instagram `@kongwabakes` vs TikTok `@kongwa.bakes`.

---

## 10. Gaps and inconsistencies

1. **`/trade/` is a 404**, is not in the sitemap and is not linked from anywhere; `#events`, `#cafes`, `#markets` anchors do not exist on any page. Any content pointing to trade anchors will land on a 404.
2. **Hero video sources broken:** `/hero/hero.mp4` and `/hero/hero-mobile-9x16.mp4` return 404 (only `/hero/hero.webm` works). THINK: iOS Safari visitors may only see the poster, and the mobile 9:16 cut was never uploaded.
3. **Rainham delivery price conflict:** home, `/bakery/` and the guides say free local delivery "across Rochester, Chatham, Gillingham, Strood and Rainham"; the Rainham page says "a small delivery charge of £2.50". Schema shippingRate max is £2.50.
4. **"Free over £25" vs minimum order:** copy says "Free local delivery over £25.00", but the checkout disables delivery below £25 ("ADD £25.00 TO UNLOCK DELIVERY"), so it is a £25 minimum for delivery, not a paid tier below £25.
5. **Deadline wording conflict:** town pages say "Order by Thursday at 5pm the week before" and the checkout note says "orders close Thursday at 5pm the week before"; home and terms say Thursday 5pm before the same week's Saturday.
6. **Chatham FAQ** says earlier days are "usually the Sunday onwards"; checkout lists Monday to Friday.
7. **Gillingham FAQ mismatch:** Q "What if my postcode is ME7 but I am nearer Rainham?" A begins "It can, slightly." (answer written for a different question).
8. **Stale dates in static HTML:** server HTML (built 15 Oct) says "This Saturday's bake is closed. You are ordering for Saturday, 17 October 2026. Need it sooner? We can do Monday, 12 October 2026." and lists past weekdays. The JS corrects it in a real browser (rendered: "Order by Thursday at 5pm for Saturday 24 October 2026"), but crawlers and no-JS previews see past dates. One of my early render runs also captured the stale text.
9. **Cookies page** claims "Here is the complete list" but omits the localStorage keys `kb-popup-v1`, `kb-basket-v1`, `kb-welcome-code-v1`, `kb-bar-h`.
10. **Read time mismatch:** guides hub says "6 minute read" for What real sourdough is; the article says "7 minute read".
11. **Custom cake flavour** "Coffee and walnut" is offered in the form but is not on the menu.
12. **Tagline casing:** site "Baked By Family, Made For Yours." vs printed labels and sticker "Baked by family, made for yours."
13. **No reviews shown:** Trustpilot link only, no rating or quotes; no address (collection address sent by email).
14. **Delivery prefixes:** schema includes ME3 (Hoo peninsula), never mentioned in page copy.
15. **OG image** is the same `/og/home.jpg` on all 16 pages.
16. **Duplicate image:** `/images/cakes/custom-cake.jpg` and `/images/menu/custom-cake.jpg` are byte-identical.
17. THINK: Guinness Marble Cake copy says "Marbled through a vanilla swirl" but the photo shows a uniform dark crumb.
18. THINK: The "Wrapped as carefully as it's baked" kraft-band image does not match the real packaging in the proof photo (real orders use boxes, pouches, stickers and printed labels).
19. Heart Cake is sold in 8/10/12 inch with the same "serves about" counts as round cakes.

---

## 11. Content-engine notes (all THINK)

- Strongest hooks already proven in copy: "three ingredients: flour, water and salt", "day four", "the crust tells you nothing", "ask the baker how long their ferment is", "you are paying for the days".
- Weekly rhythm is built in: Thursday 5pm cutoff, Saturday 8am to midday handover. A Tuesday/Wednesday "order by Thursday" post and a Saturday "handover" post fit the business.
- Real-photo assets suitable for B-roll: packed orders, grazing tables, granite-worktop product shots, custom cake gallery. Real labels are a ready-made "read the label" video tying into the sourdough guide.
- Before pointing any CTA at trade anchors or an Instagram keyword, those need to exist on the site.
