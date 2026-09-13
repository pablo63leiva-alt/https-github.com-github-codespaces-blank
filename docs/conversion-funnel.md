# TradeLift Conversion Funnel Playbook

## Visitor Journey Map

```
Traffic Sources → Landing → Quiz → Email Capture → Nurture Sequence → Revenue
```

### Traffic Sources & Entry Points

| Source | Landing Page | Intent | Priority |
|--------|-------------|--------|----------|
| Google: "skilled trades career" | index.html, trades.html | Research | High |
| Google: "which trade is for me" / "trade career quiz" | quiz.html | High — ready to engage | Critical |
| TikTok/Instagram reels | index.html | Browsing | Medium |
| YouTube trade content links | blog.html | Learning | Medium |
| Referral / word of mouth | index.html | Trust-building | High |
| Exit-intent modal (existing) | PDF lead magnet | Curiosity | Medium |

**Key insight:** The quiz page is the single highest-intent page on the site. Visitors searching "which trade is for me" are self-selecting into a decision-making moment. Every other page should funnel toward this quiz.

### The Funnel in Practice

```
1. Visitor lands on index.html or quiz.html
2. Takes the quiz (2 minutes, 10 questions)
3. Sees results: "You're built for [Trade]!"
4. Email capture: "Get your free [Trade] Career Roadmap"
5. Receives automated email sequence (5 emails over 14 days)
6. Emails drive traffic back to site: blog posts, trade pages, resources
7. Monetized touchpoints: affiliate links, future digital products
```

---

## Lead Magnet: The [Trade] Career Roadmap

Each roadmap is a personalized PDF (or HTML email) delivered via email, specific to the trade the visitor matched with.

### What's Inside (per trade)

**1. Salary Bands by State**
- National median + top 10 states by pay
- Entry-level vs. experienced wage ranges
- Overtime/benefits expectations

**2. Apprenticeship & Training Path**
- How to enter the trade (union vs. non-union)
- Typical apprenticeship timeline (3-5 years)
- Key programs and where to find them

**3. Certifications & Licenses**
- State-specific requirements (electrical, plumbing)
- Industry-recognized certs (AWS for welding, EPA 608 for HVAC)
- Cost and time estimates for each

**4. Tools Checklist**
- Starter tools (what you need on day one)
- Career-stage tools (what to invest in later)
- Budget-friendly vs. pro-grade recommendations

**5. 12-Week Action Plan**
- Week-by-week breakdown: what to do right now
- Weeks 1-4: Research & plan (courses, programs, mentors)
- Weeks 5-8: Start training (enroll, begin hands-on learning)
- Weeks 9-12: Get your foot in the door (applications, interviews, first gig)

### Delivery Mechanics

- **Live (2026-09-13):** Quiz capture posts `{email, trade}` to `https://formspree.io/f/xzebljww` (see `js/quiz.js` → `QUIZ_EMAIL_CONFIG`). Newsletter posts `{email}` to `https://formspree.io/f/xqpkvyjg` (`js/main.js` → `NEWSLETTER_CONFIG`). If the endpoint is ever reverted to a `YOURID` placeholder, the `mailto:` fallback activates.
- **Future upgrade:** Generate per-trade PDFs in `/assets/roadmaps/` and link them in the success email or Formspree redirect.

> **Clarifying note:** The current implementation reveals the quiz results first and shows the email capture **after** the results ("reveal + upsell"). Results are **NOT gated behind email**. Gating results behind email is a **future** A/B test variant (Variant B of Test 2), not the current behavior.

---

## Automated Email Sequence

Triggered by quiz opt-in. All emails sent from the same address the visitor opted in with.

### Email 1 — Welcome (Immediate)

**Goal:** Deliver the roadmap, build trust, set expectations.

**Subject:** Your [Trade] Career Roadmap (free download)

**Content:**
- "Hey! Here's your personalized [Trade] Career Roadmap."
- Direct download link (or attachment)
- "This covers salary, training steps, certs, and a 12-week plan."
- "Over the next 2 weeks, I'll send you a few more things to help you get started."
- CTA: Download your roadmap (link to PDF or the site)

**Why it works:** Instant value delivery. The visitor just invested 2 minutes in the quiz — reward them immediately.

---

### Email 2 — Value / Education (Day 3)

**Goal:** Drive traffic back to the site, build authority.

**Subject:** 3 things most people get wrong about [Trade] careers

**Content:**
- Short myth-busting format (e.g., "You don't need a college degree", "You can earn $70K+ in 2-3 years", "Apprenticeships pay you while you learn")
- Link to the relevant trade page on TradeLift
- CTA: Read: [Trade] career overview on TradeLift

**Why it works:** Positions TradeLift as the expert. Drives page views.

---

### Email 3 — Social Proof (Day 7)

**Goal:** Build credibility, make the career feel real and achievable.

**Subject:** How [Name/Type] went from zero to [Trade] in 18 months

**Content:**
- Short story format (even if genericized): "Maria, 19, was working at a fast-food restaurant. She enrolled in a local electrician apprenticeship and is now earning $55K in her second year."
- If no real stories yet: "Here's what the typical [Trade] journey looks like..."
- CTA: See real trade stories on TradeLift

**Why it works:** Overcomes the "is this really for me?" objection. Young people need to see themselves in the path.

---

### Email 4 — Related Content (Day 10)

**Goal:** Cross-pollinate — show the visitor more of what TradeLift offers.

**Subject:** While you're getting started with [Trade]...

**Content:**
- Link to a relevant blog post (e.g., "Tools Every [Trade] Needs" or "How to Find an Apprenticeship Near You")
- Link to the Getting Started page
- Brief mention of other trades: "If you're also considering [related trade], here's a comparison."
- CTA: Explore more resources on TradeLift

**Why it works:** Deepens engagement. More page views = more chances to convert later.

---

### Email 5 — Product/Affiliate Pitch (Day 14)

**Goal:** First monetization touch. Low-friction recommendation.

**Subject:** The one tool every [Trade] apprentice needs

**Content:**
- Honest recommendation for one tool/gear item (affiliate link)
- Frame it as "I'd start here" — not a sales pitch
- Link to a blog review or directly to Amazon affiliate link
- CTA: Check out the [tool name] on Amazon

**Why it works:** 14 days of value delivery first. The visitor trusts you. Now a product recommendation feels helpful, not pushy.

---

## A/B Tests to Run on the Quiz Page

With limited traffic (~500-2000 quiz completions/month at launch), prioritize high-impact, easy-to-implement tests. Run each for 2-4 weeks minimum.

### Test 1: Email Offer Framing

**Variants:**
- A (current): "Your Personalized [Trade] Career Roadmap"
- B: "Get Your Free [Trade] Checklist + Action Plan"

**What to measure:** Email opt-in conversion rate (submissions / quiz completions)

**Why this matters:** "Roadmap" implies comprehensive but potentially heavy. "Checklist" implies quick and actionable. For teens/young adults, action-oriented language often outperforms comprehensive framing.

---

### Test 2: Email Gate Position

**Variants:**
- A (current): Email capture shown between results and CTA buttons
- B: Email capture shown BEFORE results (gate the full result behind email)
- C: Email capture shown AFTER scrolling past results (delayed pop-up style)

**What to measure:** Opt-in rate AND quiz completion rate (you don't want to lose completions)

**Why this matters:** This is the highest-leverage test. Gating results behind email can double opt-in rates but risks losing 30-50% of completions. The current "reveal + upsell" approach is safer for list growth when traffic is small.

---

### Test 3: CTA Button Copy

**Variants:**
- A (current): "Send Me the Roadmap"
- B: "Get My Free Career Plan"
- C: "Yes, I Want the Roadmap"

**What to measure:** Submit clicks / impressions of the email form

**Why this matters:** CTA copy is the easiest thing to test and can swing conversion 10-30%. "Get" outperforms "Send" in most lead-gen contexts. "My" adds personalization.

---

### Test 4: Skip Button Prominence

**Variants:**
- A (current): Small underline text link ("Not now, just show me my results")
- B: Slightly larger text with arrow ("Skip — show me my results →")
- C: No skip button (force email view, but allow scrolling past)

**What to measure:** Opt-in rate AND bounce rate from results page

**Why this matters:** Making skip less prominent increases opt-in friction. Removing it entirely may increase opt-in 15-25% but also increases frustration. Test the middle ground.

---

### Test 5: Email Capture Card Background

**Variants:**
- A (current): Solid card with orange border
- B: Gradient background (orange-to-dark)
- C: No card border, just a divider line + text

**What to measure:** Click-through to submit button (scroll depth to form)

**Why this matters:** Visual prominence affects whether the email form feels like a "next step" or a "gate." A bold card grabs attention; a subtle design feels less salesy. With young audiences, less corporate = more trust.

---

## Affiliate / Product Launch Strategy

### Phase 1: Affiliate (Start Here — Zero Cost)

**Why first:** No product to build, no inventory, no customer service. Just links.

**Best affiliate partners for TradeLift audience:**
- Amazon Associates: Tools, safety gear, work boots, tool bags
- Trade school / training programs: Online courses (Udemy, trade-specific)
- Workwear brands: Carhartt, Dickies, timberland PRO (many have affiliate programs)

**Where to place affiliate links:**
1. Email sequence (Email 5 and beyond)
2. Blog posts (tool reviews, "getting started" guides)
3. Resources page (already exists — add affiliate links to tool recommendations)
4. Future: Downloadable PDF roadmaps with embedded links

**Realistic affiliate revenue:**
- Amazon Associates: 3-4% commission on tools ($5-$30 per sale)
- At 100 click-throughs/month × 5% conversion × $15 avg commission = $75/month
- This is a side-income stream, not a primary revenue source at current traffic

### Phase 2: Digital Products (3-6 Months)

**Products that make sense:**
- Individual trade roadmaps as printable PDFs (free — lead magnet)
- Premium "Trade Career Starter Kit" ($9-$19): comprehensive guide with budgeting worksheet, resume template, interview prep
- Trade-specific tool guides ($4-$7): "The Complete Electrician's Tool Guide"

**Platform:** Gumroad or Lemon Squeezy (low fees, instant delivery, no backend needed)

**When to launch:** After you have 500+ email subscribers and know which trade gets the most quiz completions. Start with ONE product for the highest-volume trade.

### Phase 3: Sponsorships / Partnerships (6-12 Months)

**Realistic trigger:** 10,000+ monthly page views

**Partners to approach:**
- Trade schools / community colleges (pay per lead)
- Tool manufacturers (brand placement in exchange for commission)
- Workwear brands (sponsored content)

**This is not realistic at launch.** Don't chase sponsorships until traffic justifies it.

---

## Conversion Rate Expectations (Honest Numbers)

These are based on typical lead-gen benchmarks for small static sites with organic traffic.

### Quiz Completion Rate
- **Benchmark:** 60-80% of quiz starters complete the quiz
- **Good:** 70%+
- **Action if below 60%:** The quiz may be too long or questions aren't engaging. Test reducing to 8 questions.

### Email Opt-In Rate (from quiz completers)
- **Benchmark:** 8-15% of people who see the email form will opt in
- **Good:** 12%+
- **Optimistic:** 20%+ (with result gating or strong offer)
- **Action if below 8%:** The offer isn't compelling enough or the form is too prominent/aggressive. Test framing and positioning.

### Email Open Rate
- **Benchmark:** 40-60% for welcome sequence (small list, high intent)
- **Good:** 50%+
- **Action if below 40%:** Subject lines need work, or emails are landing in spam.

### Email → Click-Through Rate
- **Benchmark:** 5-10% of openers click a link
- **Good:** 8%+

### Affiliate Conversion Rate
- **Benchmark:** 1-3% of click-throughs purchase
- **Good:** 2%+
- **Note:** This is the weakest link. Affiliate revenue at small scale is pocket change — but it compounds as traffic grows.

### End-to-End Math (Conservative)

Assuming 1,000 quiz completions/month:
- 750 complete the quiz (75% completion rate)
- 90 opt in to email (12% opt-in rate)
- 45 open welcome email (50% open rate)
- 4 click an affiliate link (8% CTR)
- 0.1 make a purchase (2.5% affiliate conversion)
- Revenue: ~$1.50/month from affiliates

**That's the honest reality.** Affiliate revenue is negligible at this scale. The real value of the email list is:
1. Future product sales (your own digital products)
2. Driving repeat traffic (each email opens = page views)
3. Building an asset (email list = owned audience, not algorithm-dependent)

**Breakeven for meaningful revenue:** ~5,000 quiz completions/month, which means ~600 email subscribers/month, which means you need roughly 15,000-25,000 monthly site visitors.

### How to Get There

- **SEO:** Target long-tail quiz-related keywords ("which trade is right for me quiz", "should I become an electrician quiz"). The quiz page is your best SEO asset.
- **Social:** Short-form video (TikTok, Reels) with "I took a trade career quiz and got [Trade]!" — drive viewers to take the quiz themselves.
- **Referral:** Add "Share your result" functionality (already exists) + incentivize (future: "Refer 3 friends, get the premium roadmap free").
- **Content:** Blog posts that link to the quiz ("5 Signs You Should Become a Welder — Take the Quiz").

---

## Summary: What to Build First

| Priority | Action | Expected Impact |
|----------|--------|-----------------|
| 1 | Set up real Formspree endpoint | Email capture actually works |
| 2 | Create the trade roadmap PDFs (one per trade) | Lead magnet has substance |
| 3 | Set up email autoresponder (Mailchimp, ConvertKit, or Buttondown free tier) | Automation runs without manual work |
| 4 | Run A/B Test #1 (offer framing) | Optimize opt-in rate |
| 5 | Add affiliate links to Resources page + blog posts | First revenue stream |
| 6 | Run A/B Test #2 (email gate position) | Optimize the highest-leverage variable |
| 7 | Create first digital product | Own your revenue |
