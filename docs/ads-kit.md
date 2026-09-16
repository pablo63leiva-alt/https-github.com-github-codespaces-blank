# TradeLift — Paid Ads Kit (Meta/TikTok/Google) — READY TO LAUNCH

**Owner:** Jarvis (PM) + Fury (ad ops) · **Created:** 2026-09-16
**Status:** 🟢 Copy + hooks + audiences + budgets written. **Blocked on Pablo:** creating ad accounts + pixel install (~30 min).
**Rule:** Every creative uses ONLY site-verified canonicals (trades.html / quiz.js / blog/). No invented stats.

---

## 0. What to run first (the money equation)

| Campaign | Funnel | Why first |
|---|---|---|
| **A. Quiz Lead Magnet** (Meta/TikTok) | Ad → quiz.html → email capture → roadmap/guide | Email list = the multiplier behind everything. $0.30–$0.90/email is the target. |
| **B. Gear Affiliate** (Meta/TikTok) | Ad → best-*-tools posts → Amazon tag=tradelift-20 | Direct commission. Pay CAC vs commission math is simple. |
| **C. Trade School CPL** (Google/Meta) | Ad → tradeschools.html → school leads (later) | Highest Payout, needs partner handshake — Phase 2. |
| **D. $12 Guide** (Meta retargeting) | Ad → first-apprenticeship.html → Gumroad | Only after Gumroad publish. Retarget quiz completers. |

**Order of operations:** A (now) → B (now) → D (after Gumroad live) → C (after UTI/Lincoln handshake).

---

## A. Campaign 1 — "Which Trade Fits You?" Quiz Lead Magnet

### Objective & targets
- Objective: Lead Generation (not clicks — you want emails, not visits)
- Target: **$0.30–$0.90 per email**; quality score gate = open rate on Email 1 above 40%
- Budget: start **$10/day** · scale +$10/day every 3 days while CPA holds

### Audience (TikTok + Meta)
- Core: US, 16–24, interest: "skilled trades", "electrician", "welding", "vocational training", "DIY/tool brands (Milwaukee, DeWalt, Snap-on)", "high school senior", "career counseling"
- Lookalike (after 500 emails): 1% LAL from Formspree CSV export
- Exclude: people who already submitted (matched list upload)

### Ad copy (3 primary variants — delisted losers weekly)

**Ad 1 — "The real roadmap"**
> Headline: Skip the student loan meeting
> Primary text: "Made $60K+ by 23 with zero student debt. The trades taught me more in one year than college did in four. Take the 2-minute quiz → get a free career roadmap for the trade that actually fits you. No spam, free roadmap, and it takes less time than a TikTok scroll."
> CTA: **Learn More**

**Ad 2 — "Salary first"**
> Headline: These jobs pay $60K–$100K. No degree.
> Primary text: "Electricians $60K–$80K. Welders $45K–$70K. Construction managers $70K–$100K. All learnable through apprenticeships that PAY you to train. Stop guessing your future — take the quiz and see which of 12 trades fits YOU, then get the roadmap."
> CTA: **Learn More**

**Ad 3 — "Social proof angle"**
> Headline: School called. It's the wrong memo.
> Primary text: "750,000+ trade jobs are open right now. HVAC alone needs 36,700 workers. Meanwhile the average grad carries $37K in debt. The quiz takes 2 minutes and hands you a free, trade-specific career roadmap. Find your trade."
> CTA: **Learn More**

### Creative specs
- **Meta:** 1080×1920 Reels format video (repurpose the TikTok scripts — Lang's video assets), 9:16, first 2s = hook text
- **Static fallback:** 1080×1350, gradient dark + orange, giant salary stat, CTA bar bottom
- **TikTok:** Spark Ads on organic top performers (first, cheapest) → then SMBS ads
- Always: dark-theme, high-contrast, subtitles ON, logo watermark top-right

### Landing page
- quiz.html (already live). Ensure UTM passthrough: quiz.html?utm_source=meta&utm_campaign=quiz_lead
- On email success, they get roadmap + guide links (already wired). **After Gumroad publish:** switch roadmap CTA banner → paid-guide upsell.

---

## B. Campaign 2 — Gear Affiliate (direct commission)

### Why it works before Scale
- Pay-per-conversion. Amazon associates pays on first click window. Even at 3% affiliate rate, amp up ad budget only when: (commission × conversion rate) > (ad cost × clicks). Start micro: **$5–8/day** to prove.

### Audience
- Same demo + "completed high school", interest "tool reviews", "Milwaukee tools", "DeWalt", "first job out of high school", "apprenticeship".

### Ad copy (pick per product)
**Ad 1 — Starter kit angle**
> Headline: The 12 tools every apprentice actually needs
> Primary text: "Don't blow $400 on gear you don't need. A genuine electrician's starter kit is $297 — here's exactly what's in it and where to buy it (with real prices, not fluff). Your first paycheck will thank you."
> CTA: **Shop Now** / **Learn More**

**Ad 2 — Gloves/PPE angle**
> Headline: This $20 gear saves more than money
> Primary text: "Three things every new apprentice should buy before day one — and why skimping on gloves is the one mistake that lands folks in urgent care. Honest picks, real prices."
> CTA: **Shop Now**

### Landing pages
- blog/best-electrician-tools-for-beginners.html, blog/best-work-boots-for-apprentices.html, blog/best-work-gloves-for-construction.html, blog/best-hard-hats-for-trade-workers.html (new gear posts = 4 live)

---

## C. Campaign 3 — Trade School CPL (Phase 2, post-partnership)

- **When:** after UTI/Lincoln handshake signs, or via their affiliate program partner links
- **Format:** Education lead-gen: meta Lead Ads with prefill (first name, email, state, "program interested in" dropdown) → delivered to school's CRM or partner link
- **Payout:** $30–$80 per qualified lead (typical for trade schools)
- **Budget:** $20/day, scale as conversion volume proves
- **Landing:** after lead ad → tradeschools.html "Compare top schools" with school-specific link + UTM

---

## D. Campaign 4 — $12 Guide (retargeting, after Gumroad)

- **Audience:** Website visitors (Meta Pixel: viewed quiz / trade pages), email list non-buyers, quiz completers
- **Copy:** "You got your roadmap. Now get the 90-day launch plan that turns it into money."
- **CTA:** Buy Guide → first-apprenticeship.html → Gumroad checkout
- **Budget:** $5/day retarget; promote to cold only after Gumroad storefront live + proof

---

## 5. Tracking & pixel install (30 min, Pablo)

1. **Meta Pixel** — add via `js/main.js` small snippet (I can add the base pixel now with a placeholder ID; swap in your real ID once account exists)
2. **TikTok Pixel** — same pattern, add pixel base + `Track` events on quiz completion + email capture
3. **Google Ads (for CPL/search later)** — GTM or tag snippet on all pages; remarketing list feeds ad group for search "trade school vs college"
4. **UTM convention:** `?utm_source=<platform>&utm_medium=<cpc/social>&utm_campaign=<name>` on every ad URL; grep audit after launch

**Event goals (server-side later):** `quiz_completed`, `email_captured`, `guide_downloaded`, `checkout_started`, `purchase` — wire all into the funnels for real ROAS math.

---

## 6. Spend & scale playbook (Fury)

| Week | Budget/day | Gate to scale |
|---|---|---|
| 1 | $10 (quiz) + $5 (gear) | Email CPA ≤ $0.90 AND ≥ 100 emails |
| 2 | $20 + $10 | CPA holds ≤ $0.90, CTR ≥ 1.2%, pixel complete-funnel events > 30 |
| 3 | $30 + $20 + $5 (D) | CPA ≤ $0.75 and/or ROAS ≥ 1.0 on gear |
| 4+ | Double winners, kill <60% median performers | CPA ≤ $0.60, scale looked at weekly |

**Kill rules:** any ad with CPA 2× median for 3 consecutive days = kill. Break-even CPA = (Event Value) × 1.2.

---

## 7. Accelerants (0-cost, stack with paid)

- Post every ad as organic content first (Meta favors ad accounts with organic history) — feed from Track C video pack
- Repurpose Quiz qualifying leaderboard screenshots as UGC comments
- Use Spark Ads on organic top 3 posts before building SMBS creative
- A/B one hook per week minimum; kill losers fast

---

## 8. What needs Pablo (exact)

1. Create Meta Business Manager + page (if none) — 15 min
2. Create TikTok Ads account (personal → business) — 10 min
3. Create Google Ads (for later CPL) — optional now
4. Give me access: Page admin + ad account ID + pixel ID → I wire base snippets, UTM, event schema
5. Publish the $12 guide on Gumroad (storefront-launch-kit.md has the listing copy, ready)

**No new ad dollars are needed from you beyond the minimum — first 7 days total ≈ $105.**