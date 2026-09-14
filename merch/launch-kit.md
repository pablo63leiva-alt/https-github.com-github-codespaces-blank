# TradeLift Trade Shirts — Launch Kit (Etsy / Printful)

Standalone merch line: 12 bold trade designs, one accent color + white on a dark slab, 3000×3000 RGBA
PNG (300 DPI = 10 in print area, perfect for chest prints) + editable SVG sources.

- Files: `merch/designs/<slug>.png` and `merch/designs/<slug>.svg`
- Renderer: `node merch/generate-merch.js` (regenerates PNG+SVG via Playwright; self-verifies size & dims)
- Trades mirror `js/quiz.js` exactly (slug-identical to the site's `og-<slug>.png` cards → same funnel story).

---

## What's trending in trade shirts (best-effort)

> ⚠️ Etsy search endpoints returned **403 (blocked)** on the fetch attempt, so this is **domain knowledge,
> not a live scrape**. Use Etsy's own search bar + its autosuggest keywords before finalizing tags.

- **Trades era is the gift market.** Electrician, plumber, welder, and "RVMed trucker" tees are evergreen
  gifting staples (Father's Day, Christmas, apprentice graduation, "last day" retirements). Volume peaks
  Nov–Dec and May–Jun; travel/road-trip subculture (flannel, "Big Rig") lifts diesel/truck shirts year-round.
- **Funny > motivational right now.** The crowd leans heavily into dry/self-aware humor. Punchlines that
  land: pay/earnings jokes, "no degree needed," getting your hands dirty, zero F's to give. Sappy
  "proud to be" lines undersell unless gift-marked for moms/girlfriends of tradesmen.
- **Phrase-driven designs dominate.** Most top listings are one-liner text shirts. A **bold icon + slogan
  badge** (this set) is *differentiating* — it reads as higher quality at the same price and converts on
  mockups.
- **Colorways:** buyers snap up black and heather/dark garments; the dark slab gives a consistent,
  print-friendly badge that pops on black, charcoal, and navy — and still works on white.
- **Keyword patterns that repeat on Etsy:** "funny [trade] shirt", "gift for [trade]", "[trade] dad/husband/
  apprentice", "tradesman tee", "no college" (electrician/plumber angle).

Use the recommendation: **list title = keyword + humor descriptor + occasion**, tags = 13 × ≤20 chars.

---

## Pricing model used (state assumptions)

- Print cost assumption: **Gildan Heavy Cotton 18000 + one-color DTG chest print ≈ $15.00** via Printful
  (USD). Premium garments (Next Level premium tee) ≈ $18.00.
- Etsy costs: 6.5% transaction + 3% + $0.25 payment processing, and (if enabled) offsite ads ~12–15% cut.
- **Target: gross margin ≥ 200% of Printful COGS at list price.**
- Recommended list: **$32.99 Gildan / $36.99 Next Level** (premium equals/exceeds the 200% target after
  standard Etsy fees; the Gildan tier is the conversion workhorse).
- Keystone test: mockup both tiers; funnel buyers up with color/size variety, not price drops.

---

## 1. Electrician — `electrician` (⚡ bolt, "HIGH VOLTAGE, ZERO DEGREES")

- **Title (140):** Funny Electrician Shirt, High Voltage Zero Degrees, Gift for Sparky Tradesman Apprentice, Electrician Dad Husband No College Degree Tee
- **Tags (13):** electrician shirt, electrician gift, funny electrician, sparky shirt, electrician humor, tradesman tshirt, gift for electrician, electrician dad, electrician tee, work shirt funny, apprentice gift, sparky tee, skilled trade shirt
- **Hook:** "High voltage, zero degrees — the whole trade in one line." Bold yellow bolt, work-ready badge print. Gift for the sparky who skipped college and pulls real pay. Dark-slab design pops on black, charcoal, or navy.
- **Price rec:** $32.99 / $36.99 (see pricing model).
- **Competition:** The densest trade niche on Etsy — "funny electrician shirt" has huge saturation and lots
  of thin text-only prints. Won with **icon-led premium look** and the zero-degrees punchline; title leads
  with "Funny" + "Sparky" because those convert gift buyers.

## 2. Plumber — `plumber` (🔧 P-trap + drop, "FLUSH WITH CASH")

- **Title (140):** Funny Plumber Shirt, Flush With Cash, Gift for Plumber Tradesman Pipe Fitter Husband Dad, Plumber Humor Tee, Apprentice Work Tee
- **Tags (13):** plumber shirt, plumber gift, funny plumber, plumber humor, flush with cash, tradesman shirt, gift for plumber, plumber dad, plumber husband, plumber tee funny, work tee, plumber apprentice, pipe fitter shirt
- **Hook:** "Yes, he's flush with cash — and immune to your toilet jokes." Hand-drawn P-trap badge, clean cyan on dark. The plumber joke tee people actually want to wear to the shop.
- **Price rec:** $32.99 / $36.99.
- **Competition:** Big, mature niche; classics are crude ("I handle sh*t"). We're **safe-rated for ads** (no
  expletives) while keeping the humor — this widens inventory status (can run with Offsite Ads / Google).
  "Pipe fitter" tag sneaks adjacency to the pipefitter niche for free cross-visibility.

## 3. Welder — `welder` (🔥 flame, "HOT PAY, COOL JOB")

- **Title (140):** Funny Welder Shirt, Hot Pay Cool Job, Gift for Welder Tradesman Fabricator Boilermaker, Welding Humor Tee, Husband Dad Apprentice
- **Tags (13):** welder shirt, welder gift, funny welder, welding humor, welder tshirt, tradesman shirt, gift for welder, welder husband, welder dad, welder apprentice, welding gift, fabricator shirt, welder tee
- **Hook:** "Hot pay, cool job — certified, licensed, and occasionally on fire." Red-hot flame badge with the whole welder persona in one line. Great Father's Day and apprentice-grad pickup.
- **Price rec:** $32.99 / $36.99.
- **Competition:** Healthier than electrician/plumber (less saturation). "Tradesman shirt" crossover works.
  Boilermaker/fabricator tag adjacency broadens reach into hood and union cooling-off communities.

## 4. HVAC Technician — `hvac-technician` (❄️ snowflake, "CHILL WORK, WARM PAYCHECKS")

- **Title (140):** Funny HVAC Tech Shirt, Chill Work Warm Paychecks, Gift for HVAC Technician Heating Air Conditioning Guy, Tradesman Tee, Apprentice Shirt
- **Tags (13):** hvac shirt, hvac tech gift, hvac technician, hvac humor, funny hvac, hvac tshirt, hvac apprentice, tradesman shirt, hvac tech tee, ac repair shirt, heating and cooling, hvac dad gift, hvac mechanic
- **Hook:** "Chill work, warm paychecks — the HVAC guy who owns summer AND winter." Ice-blue snowflake badge. Year-round gifting angle: heater techs in winter, AC techs in summer — no season dead zone.
- **Price rec:** $32.99 / $36.99.
- **Competition:** Smaller niche but **rapidly growing** (everyone needs HVAC; tech shortage narrative is
  mainstream). Less mockup competition than electrician; "HVAC technician / AC repair man" keyword set has
  good research-to-saturation ratio — a genuinely good first-to-market slot.

## 5. Automotive Mechanic — `automotive-mechanic` (⚙️ gear, "GREASY HANDS, FAT PAYCHECKS")

- **Title (140):** Funny Mechanic Shirt, Greasy Hands Fat Paychecks, Gift for Auto Mechanic Car Guy Husband Dad, Automotive Technician Tradesman Tee
- **Tags (13):** mechanic shirt, mechanic gift, funny mechanic, auto mechanic, mechanic humor, grease monkey, mechanic tshirt, gift for mechanic, mechanic dad, car guy shirt, mechanic tee, automotive tech, mechanic wife
- **Hook:** "Greasy hands, fat paychecks — for the guy who can fix anything but doesn't have to." Bold gear badge, diesel-red on dark. Garage-day ready.
- **Price rec:** $32.99 / $36.99.
- **Competition:** Huge but very fragmentable — "car guy" alone overlaps motorsports gifts. The pay-punchline
  differentiates from generic broken-car jokes. "Automotive technician" tag targets the pro crowd while
  "car guy" wins the enthusiast crowd from one listing.

## 6. Carpenter — `carpenter` (🔨 hammer + nail, "MEASURE TWICE, GET PAID ONCE")

- **Title (140):** Funny Carpenter Shirt, Measure Twice Get Paid Once, Gift for Carpenter Woodworker Builder Framing Guy, Tradesman Tee, Husband Dad Apprentice
- **Tags (13):** carpenter shirt, carpenter gift, funny carpenter, carpenter humor, woodworker shirt, carpenter tshirt, tradesman shirt, gift for carpenter, carpenter dad, builder shirt, carpentry tee, carpenter apprentice, framing guy shirt
- **Hook:** "Measure twice, get paid once — the carpenter's code, upgraded." Gold hammer badge with the
  build-right-be-picky-right punchline. Reads like a badge, wears like a flex.
- **Price rec:** $32.99 / $36.99.
- **Competition:** Carpenter has less Etsy saturation than sparky/turd-herder niches; overlaps with
  "woodworker gift" which is strong at holiday. Framing guy + builder tags widen net.

## 7. Ironworker — `ironworker` (🏗️ I-beam + hook, "COWBOY OF THE SKY")

- **Title (140):** Funny Ironworker Shirt, Cowboy of the Sky, Gift for Ironworker Structural Steel Rig Iron Man, Connector Tradesman Tee, Husband Dad Shirt
- **Tags (13):** ironworker shirt, ironworker gift, ironworker humor, iron worker tee, structural steel, ornery ironworker, tradesman shirt, gift for ironworker, ironworker dad, ironworker husband, steel worker shirt, connector shirt, ironworker apparel
- **Hook:** "Cowboy of the sky — walk the iron like you own it." Steel-blue beam badge with rigging hook. For the crew that earns every inch of the height pay.
- **Price rec:** $32.99 / $36.99.
- **Competition:** Niche-but-loyal audience (ironworker shirts have strong union/gift culture and little
  competition — underrated). Exact-match searches convert well because buyers hunt *specific* trade pride,
  not generic humor. High margin-per-sale niche; fewer listings = better CTR.

## 8. Pipefitter — `pipefitter` (🔩 flanged T-joint, "STRAIGHT PIPES, STRONG PAY")

- **Title (140):** Funny Pipefitter Shirt, Straight Pipes Strong Pay, Gift for Pipefitter Steamfitter Union Tradesman, Pipe Fitter Husband Dad Race Tee
- **Tags (13):** pipefitter shirt, pipefitter gift, pipefitter humor, steamfitter shirt, pipe fitter tee, union tradesman, gift for pipefitter, pipefitter dad, pipefitter apparel, welder gift, pipeline shirt, pipefitter man, pipefitter apparel
- **Hook:** "Straight pipes, strong pay — the highest-paid pipe in the building." Purple flange badge with
  the union-pay flex. Taps the welder crossover audience too.
- **Price rec:** $32.99 / $36.99.
- **Competition:** One of the **least-served trade niches** (high pay + low shirt saturation = best
  competition math in the set). Steamfitter/union tags reach aligned audiences; pairing with welder tags
  cannibalizes your own welder listing but wins the searcher who doesn't know the difference.

## 9. Diesel Mechanic — `diesel-mechanic` (🚛 big-rig truck, "BIG RIGS, BIG BUCKS")

- **Title (140):** Funny Diesel Mechanic Shirt, Big Rigs Big Bucks, Gift for Diesel Tech Truck Driver Mechanic, Heavy Duty Shop Guy Husband Dad Tee
- **Tags (13):** diesel mechanic, diesel shirt, diesel gift, big rig shirt, truck mechanic, funny mechanic tee, diesel tech, heavy duty mechanic, truck driver gift, diesel mechanic dad, shop shirt funny, diesel humor, mechanic apparel
- **Hook:** "Big rigs, big bucks — keeping the country moving, one oil change at a time." Lime-green rig
  badge. Both the mechanic AND the trucker audiences buy this.
- **Price rec:** $32.99 / $36.99.
- **Competition:** Truck-culture crossover gives this listing **two audiences** (mechanics + drivers) for one
  mockup/upload. Mild competition; "heavy duty mechanic" keyword is under-exploited against its search depth.

## 10. Mason — `mason` (🧱 trowel on brick, "ROCK SOLID, BUILT TO LAST")

- **Title (140):** Funny Mason Shirt, Rock Solid Built to Last, Gift for Mason Bricklayer Stone Worker Concrete Tradesman, Masonry Husband Dad Craftsman Tee
- **Tags (13):** mason shirt, mason gift, bricklayer shirt, masonry humor, mason tshirt, bricklayer gift, stone mason shirt, tradesman shirt, gift for mason, mason dad, construction humor, block layer shirt, mason apparel
- **Hook:** "Rock solid, built to last — like everything this guy lays." Terracotta trowel badge over a
  brick course. Old-craft pride with a modern punchline.
- **Price rec:** $32.99 / $36.99.
- **Competition:** Bricklayer/masonry is a classic niche with steady, smaller-volume demand and **thin
  competition** — solid ROAS slot. Bricklayer + stone mason tags split-search the craft across regions (UK/
  AU sellers use 'bricklayer' harder).

## 11. Roofer — `roofer` (🏠 peak + sun, "RAIN OR SHINE, WE CLIMB")

- **Title (140):** Funny Roofer Shirt, Rain or Shine We Climb, Gift for Roofer Roofing Contractor Tradesman, Roof Worker Husband Dad, Shingle Tee
- **Tags (13):** roofer shirt, roofer gift, funny roofer, roof worker shirt, roofing humor, roofer tshirt, roofing contractor, tradesman shirt, gift for roofer, roofer dad, roofer husband, shingle shirt, roof apparel
- **Hook:** "Rain or shine, we climb — literally on the roof, figuratively on the paycheck." Teal gable badge
  with shingle texture. All-weather joke, all-year demand (roofs need fixing every season).
- **Price rec:** $32.99 / $36.99.
- **Competition:** Moderate saturation, but mostly repeats of the same "roofers do it higher" line — our
  weather+pay punchline is a fresh angle. Roofing contractor crowd is active gift-buying in storm season
  (asphalt shingle season = spring/summer).

## 12. Construction Manager — `construction-manager` (📋 hard-hat on blueprint, "FROM TOOLBOX TO SIX FIGURES")

- **Title (140):** Funny Construction Manager Shirt, From Toolbox to Six Figures, Gift for Project Manager Superintendent Builder, GC Contract Tradesman Tee
- **Tags (13):** construction manager, construction gift, project manager tee, construction humor, superintendent shirt, gc shirt, construction tee, construction boss, site manager gift, contractor shirt, builders gift, construction apparel, contractor dad
- **Hook:** "From toolbox to six figures — worked his way up, and skipped the student loans." Indigo hard-hat
  badge over a tilted blueprint. For the site lead with the plan AND the pull-ups.
- **Price rec:** $32.99 / $36.99.
- **Competition:** Less shirt-specific competition and strong corporate-gift adjacency (GCs/PMs buy swag for
  teams). "Six figures" angle tracks the trades-vs-college narrative TradeLift already ranks for — reuse that
  blog positioning in listing copy for targeting consistency.

---

## Cross-listing playbook (sell as a set)

1. **Series math:** one mockup template, 12 listings, same slab family = they look like a *brand*, not
   dropshipping spam. Shoppers who get one trade gift often buy the sibling trade shirts.
2. **Bundle hooks in descriptions:** "Building a set for the crew? Shop the other trades in this badge
   series" (and link your shop).
3. **Repeat 3-4 universal tags** (tradesman shirt / skilled trade shirt / tradesman tee / work shirt funny)
   on every listing to build shop-level keyword gravity.
4. **Upsell garments:** offer Gildan Heavy Cotton (value) + Next Level premium (gift) on every listing so
   gift buyers self-select into the higher margin.
5. **Launch order:** electrician, plumber, welder, mechanic first (proof the pivot works), then HVAC, diesel,
   carpenter, then the niche-royalty slots (ironworker, pipefitter, mason, roofer, construction manager).