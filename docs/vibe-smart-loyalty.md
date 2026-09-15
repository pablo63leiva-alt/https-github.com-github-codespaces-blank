# PROJECT V2: "TableText" (working name) — Restaurant SMS Loyalty Automation

> **Status:** RESEARCHED 2026-09-15 · **Squad:** Managed by **T'Challa** (Side-Project Squad Lead) · Separate lane from TradeLift (runs in parallel)
> **Owners:** Pablo (user) + Jarvis (PM/AI) + T'Challa (manager)

---

## 1. The Idea (user-set, verbatim concept)

Automation help for businesses and restaurants:

1. Customer scans a QR code on the table labeled "Sign up for free appetizer"
2. Customer fills a landing-page form requesting personal info (name, phone, email/birthday optional)
3. Contact created inside a CRM
4. Confirmation SMS sent to customer to claim their appetizer
5. Repeats for dozens of guests/day → restaurant builds a large contact list fast
6. Then offer **direct text marketing**: wait for slow times (e.g., Monday 4 PM) → mass text blast for a limited BOGO special
7. Blasts usable for: birthdays, weekly specials, holidays, promos, events
8. Core value: restaurants need the power of direct marketing

---

## 2. Market Research (verified via live sources, 2026-09-15)

### Competitor landscape
| Player | What they do | Pricing (verified) | Positioning |
|---|---|---|---|
| Postscript | SMS/MMS for Shopify ecommerce; Postscript Plus = DFY managed SMS | $0/mo + $49 min spend; $0.009/SMS promo; Growth $100/mo; Pro $500/mo; DSC $750/mo | ecommerce-only, not restaurant-native |
| Attentive | Enterprise SMS+email+RCS+AI; F&B page exists | Custom (sales-led) | Enterprise, costly for indie |
| SimpleTexting | General SME mass-texting; restaurant vertical page; keywords, forms, quiz | $29/500 · $49/1k · $79/2k · $109/3k; overage 5.5→2¢; local # $10/mo | SMB generalist |
| SlickText | General SME SMS; forms, popups, workflows | $29/500 → $939/50k; price-matches ST | Generalist SMB |
| TextMagic | Pay-as-you-go SMS + CRM | $49/1k (4.9¢/SMS), # $10/mo | Usage-based utility |
| EZ Texting | General SME; **QR codes + signup forms + click-to-text on EVERY plan** | Launch $25/mo (500 credits); Boost $75; Scale $125; Ent $3k | Value generalist |
| Brevo (Sendinblue) | Email+SMS+WhatsApp; SMS credits | Free tier; $0.0109/SMS | Cheap bundle, not restaurant-specific |
| Klaviyo | B2C CRM email+SMS+WhatsApp | Free 250 profiles; paid ~$25/mo+ | Ecommerce CRM |
| Toast / Square | POS-anchored loyalty + marketing | Sales-led, opaque | POS lock-in |
| **Textdrip** | Indie SMS automation (cheapest flat-tier) | **$19.99/$34.99/$74.99/mo** | **Proof bottom-of-market is open** |
| TVB Media / Loyal Beaver / Springboard | Named restaurant/SMS shops | Unverifiable public footprint | Tiny/fragmented tail |

**KEY WHITE SPACE:** No product is *purpose-built* for "QR at the table → short form → SMS list → blast blasts" for **independent restaurants**. Everyone treats it as a general SMS feature bolted on. The QR-free-appetizer flow is the restaurant's job to assemble. **Opportunity is wide open.**

### Demand signals (verified)
- 84% of consumers opt in to business texts; 66% of businesses use SMS software; 67% increasing budgets (SimpleTexting 2025, n=1,400)
- 82% check texts within 5 min; 82% of businesses say SMS drives revenue
- Hospitality = SMS's #2 adoption vertical (80%); #2 highest-performing channel; 69% of hospitality businesses report >20% conversion
- Opt-in driver #1 = promotions (58%)

### Big-player weak spots (the opportunity)
1. Complex billing — credit math, MMS=3 credits, overage, carrier pass-through + 10DLC fees → independents can't audit
2. Contracts + sales-led pricing past entry tier
3. Generalism — restaurant onboarding is DIY (print QR tent, write SMS copy, own compliance)
4. POS lock-in (Toast/Square loyalty needs their POS)
5. Over-texting — 53% opt out for "too many texts" → list decay → churn

### Positioning recommendation
**"The first SMS marketing built for independent restaurants — we hand you the QR signs, the campaigns, and the appetizer offer; collecting numbers in week one. One flat price. No per-text math."**
- **$49/mo "Table Lead Kit"** (self-serve): QR table tents + landing page + CRM + confirmation SMS + birthday/slow-time templates + ~5,000 texts flat
- **$99/mo "Done-for-you"** (the wedge): we write + schedule the weekly blast + build offers; only Postscript Plus does DFY and it's ecommerce-only at $500/mo+
- **Anti-churn mechanic:** send-cadence guardrails (2 texts/wk default) + 12-month campaign calendar → preserves lists (53% opt-out trigger)
- **Later moat:** WhatsApp channel upsell
- **Target:** 1–3 location independents (500–3,000 subs)
- **Positioning claim to hammer:** works with ANY POS (Square/Clover/Toast/etc.) — no lock-in

---

## 3. Technical Research (verified via live sources, 2026-09-15)

### SMS provider comparison (US, 2026)
| Provider | Per-msg (US) | Number/mo | Notes |
|---|---|---|---|
| **Twilio** | $0.0083 + carrier $0.0035-0.007 ≈ **$0.012-0.015** | $1.15 long / $2.15 toll-free | **Best for custom build** — docs, SDKs, Trust Hub 10DLC, Verify API ($0.05/verify) |
| **Telnyx** | $0.004 + carrier | $1.00 | Cheapest raw API; 10DLC brand $4.50, campaign vetting $15, $1.50–30/mo |
| **Bird (MessageBird)** | ~$0.0035 (long code) + carrier | included | Modern DX; WhatsApp/Email later; 10DLC fees apply |
| **SimpleTexting** | ~$0.055/credit (1 SMS=1 credit) | $10 local | **Fastest no-code MVP** — built-in compliance, forms, keywords, automations |
| **Brevo** | $0.0109/msg | shared pool | Email+SMS+CRM unified, GDPR-native |
| Textlocal | **SHUT DOWN July 31, 2026** | — | Do NOT use |

**Effective all-in cost per SMS (long code): ~$0.012–0.016**

### ⚠️ COMPLIANCE (CRITICAL — TCPA / 10DLC / A2P)
Required registrations:
- **Brand Registration (10DLC)** — $4.50 one-time (for-profit), via TCR, 1–3 days, needs EIN/SSN
- **Campaign Registration** — $15 vetting + $1.50–$30/mo (Marketing $10/mo; Low-volume $1.50/mo if <6K segments/day)
- Toll-Free Verification — free (Twilio), 1–2 wks (alternative)
- Short code = $1,000–1,500/mo + $500 setup (overkill for single restaurant)

**Required form disclaimer (11-element template, verbatim):**
> **Brand Name:** By texting **KEYWORD** to **(123) 456-7890**, you agree to receive promotional messages sent via an autodialer. You also agree to the terms of service (**website.com/terms**) and privacy policy (**website.com/privacy**). This agreement isn't a condition of any purchase. Message frequency varies. Message and data rates may apply. Reply STOP to opt out; HELP for more information.

**Ongoing rules:**
- Time-of-day: 8 AM–9 PM recipient local (FL/OK 8 AM–8 PM)
- Frequency: ≤1/wk promo best practice
- Honoring STOP/HELP immediately + confirm opt-out; every message starts with brand name
- ≥1 "Reply STOP" reminder per month (CTIA)
- Scrub National DNC Registry
- **Enforcement risk: $500–$1,500 per violating message (TCPA private right of action); carrier blocking of unregistered 10DLC traffic; class-action risk on consent gaps.** Mitigate: provider with built-in compliance, log consent (timestamp, IP, form copy, phone), automate opt-out.

### MVP stack options
| Option | Stack | Cost/mo | Time |
|---|---|---|---|
| **No-code (week 1)** | Tally.so (form) + Carrd (landing) + SimpleTexting (CRM/SMS) + QRCodeMonkey | **~$50–90** | days |
| **Custom (scale)** | Next.js/Vercel + Supabase + Twilio | **~$180–280 @10K** | 2–3 wks |
| **Hybrid (recommended)** | Tally Free + Carrd Pro + SimpleTexting 1k credits + Airtable | **~$61** | days |
| Cheapest custom | Telnyx + Supabase | ~$130 | but dev+compliance burden |

**MVP recommendation: SimpleTexting + Tally + Carrd (~$60–90/mo), compliant out of the box.**
Decision matrix: launch-days → SimpleTexting; own-stack/scale → Twilio+Supabase; email+SMS+CRM → Brevo.

---

## 4. THE SQUAD — Side-Project Team (managed by T'Challa)

> New manager + subagents stood up 2026-09-15. Runs the restaurant-SMS project in parallel with TradeLift.

### Manager: **T'Challa** (Side-Project Squad Lead / Product Builder)
Reports to Jarvis. Owns the whole restaurant-SMS product lane: MVP, compliance, GTM, docs. Strategy + review; delegates execution.

### Subagents (execution workers under T'Challa)
| Agent | Role | Responsibilities |
|---|---|---|
| **Shuri² (Product Dev)** | Builds the MVP (form → CRM → SMS wiring, QR assets, landing page) | No-code + custom code, per approved stack |
| **Namor (Technical)** | SMS API integration, 10DLC/TCPA compliance plumbing, automation logic | Twilio/Telnyx/SimpleTexting wiring, consent logging, double-opt-in, scheduling engine |
| **Nakia (Compliance)** | TCPA/10DLC/CTIA audit, consent-wording on forms, privacy + opt-out handling | Ensures every blast is legally safe; DNC scrub; STOP/HELP automation; docs |
| **Okoye (GTM/DFY)** | Sales landing, pricing tiers, demo, competitor positioning, DFY campaign templates | Writes QR tent copy, weekly-blast templates, slow-time/birthday/holiday offer builders |
| **M'Baku (QA)** | Tests the whole funnel end-to-end (scan→form→CRM→SMS→blast) | Independent functional testing, edge cases (bad phone, STOP, re-scan, dupes) |
| **Ramonda (Ops/Partnerships)** | Pilot restaurants, onboarding, support playbook, local outreach | Find 1–3 pilot venues, write operator playbook, collect feedback loop |

### Squad rules (inherited from AGENTS.md)
- One subagent per task; manager T'Challa reviews; JARVIS does the hard thinking.
- **Two review passes before deploy:** M'Baku (functional) + Nakia (compliance) — compliance pass is non-negotiable for SMS.
- Every subagent proposes growth/revenue improvements.
- Save state to `docs/vibe-smart-loyalty.md` (THIS FILE) + root SESSION-MEMORY.md each session end.

### How it runs in parallel
- Jarvis splits the day into lanes: **TradeLift lane** (revenue sprint, committed to tradelift.surge.sh) + **TableText lane** (T'Challa squad, this doc). Both are standalone static/Html sites with separate deploy targets once built.
- Max urgency applies to both; TradeLift is the primary money driver now; TableText is the second engine standing up.

---

## 5. Open Decisions
1. **Product name** — TableText (this doc's working name) vs AppetizerLink vs TableLead vs VibeSmart. **Pablo to pick.**
2. **Go-to-market model** — self-serve SaaS ($49/mo) vs DFY service ($99/mo) vs both. (Research says BOTH, DFY is the wedge.)
3. **MVP stack** — no-code SimpleTexting (days) vs custom Twilio+Supabase (control). (Research recommends no-code first for a live pilot, custom later.)
4. **Pilot venues** — find 1–3 local restaurants (Ramonda lane) OR launch self-serve among TradeLift's restaurant-adjacent readers.
5. **Payment/processing** — Stripe billing for SaaS when ready (Pablo's account).

## 6. Next Actions (priority order)
1. **Pablo:** pick product name + GTM model + approve MVP stack (decisions above).
2. **T'Challa/Shuri²:** scaffold the no-code MVP (Tally form + Carrd landing + SimpleTexting account + QR tent template) — needs SimpleTexting account created under Pablo's email.
3. **Nakia:** write the consent-disclaimer line for the form + privacy blurb from the 11-element template (apply now).
4. **Okoye:** write the QR tent copy + first 3 blast templates (welcome, Monday BOGO, birthday).
5. **M'Baku:** functional test harness once MVP scaffolded.
6. **Ramonda:** draft pilot-restaurant outreach (adapt Coulson's TradeLift template style).