# TradeLift Amazon Bounty Playbook ($30 Prime-for-Young-Adults + Audible)

**Owner:** Fury · **Build:** Jarvis/Pablo (Amazon Associates account + payout = ONLY-PABLO, per REVENUE-OPS §4 #1)
**Associates tag in use:** `tag=tradelift-20` (94 links live today on tools.html + tool posts — verified 2026-09-14).

---

## (a) The bounties + mechanics

**1. Amazon "Prime for Young Adults" — ~$30 signup bounty (audience-perfect)**
- What it is: Amazon runs a discounted Prime tier for 18–24-year-olds with signup incentive
  programs/credits promoted through Prime Student–style flows. The PM-verified bounty figure is
  **~$30 per qualified signup**.
- Audience fit: our entire core (16–24 considering entry-level careers) is inside this net, and
  the *story* is a real value line: "save ~$10+/month vs full Prime, $0 for months, get Prime
  shipping/deals while you apprentice on a starter wage."
- Mechanics to handle at build time:
  - Only **new/eligible** members convert — an Associate click must land the visitor on the
    correct Prime-for-young-adults signup surface, not generic Prime.
  - Bounty/referral credit mechanics change (Amazon rotates them) — **treat $30 as a planning
    number; verify the live offer at the current landing page before the blog post ships.**
  - Attribution is session-cookie based: bounty counts only on the device/session that landed via
    our `tag=tradelift-20` link. All bounty links are placed to preserve that session (no
    click-hopping; one direct link, single hop to the offer page).

**2. Audible — ~$20–25 bounty**
- Audible-style audio-subscription bounties historically pay a flat per-new-member bounty to
  associates/marketing partners; the PM-verified range is **$20–25 per new membership**.
- Same honesty flag as (1): Audible's unpublished per-signup bounty shifts; **confirm the live
  rate on the affiliate program dashboard at setup, use $20–25 as marked planning estimates, and
  relabel the blog math if the rate moved.**
- Audience fit is real and low-friction: trade-school students listen on commutes/shop floors;
  a "listen to your study material" angle is native, not forced. Audible's value pitch ("2 free
  books + membership") is also a money-save story for 18–24s.

**Combined per-engaged-user incentive math (planning band, not promise):**
| Action | Unit value (estimate, confirm live) | Caveat |
|---|---|---|
| Prime-for-young-adults signup | ~$30 | new/eligible only; offer rotates |
| Audible new membership | ~$20–25 | rate confirmed at program dashboard |

---

## (b) Content plan — dedicated post

**Post: `blog/amazon-prime-free-for-apprentices.html`** — working title:
*"Amazon Prime Free for Apprentices (18–24): Save $XXX"*
Target keyword: "amazon prime student young adults" / "amazon prime for apprentices". Route the
linked money math at $24–48 off in year one — but the headline $XXX is filled only after the live
offer is verified (honest number, not invented).

**Outline (Hawkeye to flesh, match existing post anatomy: title ≤60, meta desc ≤160, Article+FAQPage schema, blog card, sitemap):**
1. **Hook:** "If you're between 18 and 24 and starting an apprenticeship, Prime isn't a luxury —
   at ~$10+/mo less it's the cheapest shipment/streaming deal you can get right now."
2. **The money math (build on verified live numbers):** membership-brand savings over 12 months,
   $0-months promos, student-credit value, stacked with Audible's free-books intro. Frame = "keep
   more of your first-year apprentice paycheck." (Full-disclosure box per §c.)
3. **Who qualifies:** 18–24 born-on eligibility, what ID/documentation is needed (a young adult in
   a union/local or first-year apprenticeship typically has the docs in 5 min). Honest "you need a
   qualifying email/age; if you're 17, you can't — here's what you can do instead."
4. **Step-by-step signup walkthrough (3–5 steps), one CTA per section**, each a
   `tag=tradelift-20` bounty link + disclosure.
5. **Audible add-on section:** why the audio membership fits a trade student (listen during the
   commute, on-lunch studying); single CTA with bounty link.
6. **FAQ (≤5, sector-factual):** "Is it really free?", "Will it work for apprentices?", "What do I
   need to sign up?", "Is Audible worth it on a first-year wage?", "Does TradeLift get paid?" — the
   last one answered plainly (yes, at no cost to the reader).
7. **CTA to quiz/newsletter:** "Not sure which trade yet? Take the 2-minute quiz."

**Where the bounty links LIVE (placement map — Jarvis builds):**
| Surface | Placement | Priority |
|---|---|---|
| **Blog post** (above) | In-content CTAs at steps 4 and 6 + final CTA banner | HIGH — ships first |
| **Quiz result page** (`quiz.html`) | Secondary/secondary? → second CTA under the roadmap capture: "While you set up, grab free shipping on starter tools →" | MED — after post A/B |
| **Exit-intent modal — second CTA** | Add as the *second* button under the guide offer ("meantime: free Prime shipping for 18–24 →") | MED |
| **Email seq 5/6** (see email-sequence.md) | Tools/gear + premium guide emails each carry one bounty link as a soft secondary line | LOW |
| **Getting-started resources** (`getting-started.html`, `resources.html`) | One contextual line near the tools/gear section, clearly labeled | LOW |

Rule: **one bounty link per surface, always next to real value, always with disclosure.** We are
not a coupon-sheet; a 18–24 visitor clicking it does it because it saves them money AND we said
how we get paid.

---

## (c) Honest conversion expectations + full disclosure

**Conversion math (based on real listener/reader behavior, not invented):**
- Blog readers who see a Prime/Audible link: clicking to the checkout/bounty is a real ask.
  Planning band: **1–3% of post readers click a bounty link; 10–20% of clickers complete a
  signup** → ≈ **0.1–0.6% of readers become bounty events.** At 1,000 engaged readers/mo that is
  **1–6 bounties → ~$30–180/mo** at loaded $30. That is pocket money at base, and a meaningful
  kicker only when a post or email goes wide (Stretch week). Plan accordingly; do not bank on it.
- **Full-disclosure note (ships verbatim in the post footer + every bounty surface):** *"This page
  contains Amazon Associate links. As an Amazon Associate we earn from qualifying purchases and
  qualifying free-trial signups. That earns us a small commission at no extra cost to you. We say
  this because you deserve to know exactly how the page makes money."*
- Prime-specific honesty: not every 18–24 reader lives in an eligible situation (age gaps,
  existing members, household already on Prime). The post must pre-frame: "if you already have
  Prime, skip to the Audible section — and if neither fits, here's the free guide instead."

---

## (d) Quick-win priority list

**SHIP THIS WEEK (cheap, fast, all Jarvis-buildable except Amazon account gates):**
1. Create the bounty post skeleton (title, outline, FAQ, disclosure box) — placeholder money math
   until live offer verified. → Jarvis
2. Verify the LIVE Prime-for-young-adults + Audible offer pages and current bounty rates on the
   Associates dashboard. → Pablo (ONLY-PABLO; Associ.te dashboard = his)
3. Drop one bounty link into `getting-started.html` tools/gear section (contextual, disclosed) +
   one into `resources.html`. → Jarvis
4. Wire quiz-result page: add the second CTA (bounty link) behind a flag parameter so it can be
   turned on after the post ships. → Jarvis
5. Update Privacy Policy affiliate-disclosure line (§ adsense-readiness). → Jarvis

**THIS MONTH (after post #1 is live + tracking):**
6. Exit-modal second CTA (A/B against no-CTA variant); log clicks via Plausible/GA4 goal. → Jarvis
7. Email sequence 5–6 bounty lines go live when the sequence ships. → Jarvis
8. Second bounty post if first shows ≥1% reader→click ("Audible for apprentice study", "cheapest
   way to get tools as an 18–24").

**NOT YET (kill early):**
- No dedicated "deals" homepage block or coupon section until we have ≥500 email subs and ≥1 post
  with measured click data. Deals-sections cannibalize trust, and measuring from day 1 is the
  point. → defer until click data exists.

---

*Bottom line: bounties = additive micro-cash that finally gives the
96 live affiliate links a *reason* to be there (a tool box the reader might actually need + a
discount that justifies it). Value = mostly in the save-a-teen-money story and session-attribution
discipline; it is NOT a $50K line. Ship the post this week, measure clicks, let December decide
whether it becomes a repeat CTA or stays background.*