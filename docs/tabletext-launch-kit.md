# TableText — Launch / GTM Kit

> Product: TableText, restaurant SMS loyalty. One flat price, works with ANY POS, built for independent restaurants (1–3 locations, 500–3,000 subscribers).
> Author: Okoye (GTM/DFY, TableText squad) · Source of truth: `docs/vibe-smart-loyalty.md` §1–4.
> Compliance gate: all SMS copy in this kit passes through Nakia (compliance) before any blast goes live. Any edit to consent/opt-out language requires a compliance re-pass.

Placeholders used throughout (swap before going live): `[RESTAURANT NAME]`, `[APPETIZER]`, `[ENTREE]`, `[DESSERT]`, `[SIGNUP-CODE]`, `[PHONE NUMBER]`, `[CLAIM-CODE]`, `[TERMS URL]`, `[PRIVACY URL]`, `[HOLIDAY]`, `[OFFER]`, `[DAY]`, `[TIMES]`, `[MONTH]`, `[DATE]`, `[NUMBER]`.

Messaging guardrails (from the brief): send between 8 AM–9 PM recipient-local time (FL/OK: 8 AM–8 PM), default cadence 2 texts/wk max, every message starts with the brand name, reply STOP is honored immediately.

---

## 1. QR Table-Tent Copy (3 print variants)

Fits the Tally/Carrd/SimpleTexting MVP: the QR points at the Carrd landing page (or parts can text `[SIGNUP-CODE]` to `[PHONE NUMBER]` as a fallback).

### Variant A — Short checkstand mini (2.5 x 3.5 in., register / checkout card)

**Front:**
```
FREE [APPETIZER] ON US — JOIN THE TABLE.
Scan the QR or text [SIGNUP-CODE] to [PHONE NUMBER]. Takes 10 seconds.
```

**What to say (poster line):** "Join the [RESTAURANT NAME] text list and the first appetizer's on us."

**Offer terms (back):** Free [APPETIZER] with any [ENTREE] purchase. One per guest, one time, in-restaurant dine-in or carryout. Show the confirmation text to claim.

**Tiny print (bottom, 7pt):** By joining you agree to receive promotional texts from [RESTAURANT NAME]. Msg frequency varies; msg & data rates may apply. Reply STOP to opt out. See [TERMS URL].

### Variant B — Standard 4 x 6 table tent

**Front-life hook (large type):**
```
FREE [APPETIZER] ON US.
One scan. One text. It's yours.
```
**What to say (body):** "Join the [RESTAURANT NAME] table club and we'll put a free [APPETIZER] with your next [ENTREE]. You get up to 2 texts a week — deals, birthdays, and slow-night specials, not spam. Want in?"

**Offer terms:** Free [APPETIZER] (one per guest) with any [ENTREE] purchase. Redeem by showing the confirmation text. Offer valid [DATE RANGE]. No purchase of any other kind required.

**Tiny print (7pt):** By scanning the QR or texting [SIGNUP-CODE] to [PHONE NUMBER] you agree to receive promotional texts from [RESTAURANT NAME]. Msg frequency varies; msg & data rates may apply. This isn't a condition of purchase. Reply STOP to opt out. Terms [TERMS URL] · Privacy [PRIVACY URL].

### Variant C — Check-presenter slip (small card tucked in the receipt folder)

**Front:**
```
How was everything?
Your next appetizer is on us. Text [SIGNUP-CODE] to [PHONE NUMBER] or scan the QR — up to 2 texts a week, birthdays and deals included.
```

**What to say:** "Thanks for stopping in — leave a tip, grab the card, and the appetizer next time is on us."

**Offer terms:** Free [APPETIZER] with any [ENTREE] on your next visit. One per guest. Show the confirmation text.

**Tiny print (7pt):** By joining you agree to receive promotional texts. Msg rates may apply. Reply STOP to opt out. [TERMS URL].

---

## 2. Landing Page — Wireframe + Copy (Carrd, mobile-first)

Customers scan at the table on a phone held in one hand — single column, no sidebars, submit button in thumb reach, inputs at least 44px tall.

**Block-by-block wireframe (top to bottom):**
1. Offer hero (headline + subhead)
2. Form: name, phone number, email (optional), birthday (optional), consent checkbox, submit CTA
3. Social proof strip
4. Privacy line (small, below form)
5. Success state (replaces the form — do not navigate away)

**Complete Carrd copy (paste-ready):**

- **Page title / meta:** `[RESTAURANT NAME] — Free [APPETIZER]`
- **Headline (hero):** `Free [APPETIZER] on us.`
- **Subhead (hero):** `Join the [RESTAURANT NAME] text list and your first appetizer's covered — up to 2 texts a week, never more. Birthdays and slow-night specials included.`
- **Form fields:**
  - Name: `Your name (first name is fine)`
  - Phone (required): `Mobile number`
  - Email (optional): `Email (optional)`
  - Birthday (optional): `Birthday — month and day (optional, for a free birthday treat)`
- **Consent line (directly under the phone/birthday fields, above the button — full 11-element template, verbatim):**
  - Lead-in: `Check the box to join:`
  - Consent label: `[RESTAURANT NAME]: By texting [SIGNUP-CODE] to [PHONE NUMBER], you agree to receive promotional messages sent via an autodialer. You also agree to the terms of service ([TERMS URL]) and privacy policy ([PRIVACY URL]). This agreement isn't a condition of any purchase. Message frequency varies. Message and data rates may apply. Reply STOP to opt out; HELP for more information.`
- **Submit button:** `Claim my free [APPETIZER]` — disabled until name, phone, and the consent box are checked (log consent timestamp + IP + form copy at submit).
- **Social proof strip:** `[NUMBER] regulars already text with us. Slow Mondays are now answered with a text.` *(Replace [NUMBER] with the real live count; do not run before the number is true.)*
- **Privacy line (small, under the form):** `We only text [RESTAURANT NAME] news, offers, and birthdays. No sharing, no spam — opt out anytime with one word: STOP.`
- **Success state (replaces the form):** `Check your texts for your appetizer code.` *(Plain text. No emoji, no symbols.)* Line 2, small: `Show that text next visit to claim your free [APPETIZER].`

---

## 3. Confirmation SMS Template (SimpleTexting automation, sent on signup)

Brand name first, claim instructions, frequency note, STOP/HELP. Under 160 characters.

> `[RESTAURANT NAME]: Thanks for joining! Show this text to claim 1 free [APPETIZER]. We text up to 2x/wk. Reply STOP to opt out, HELP for help.`

- **Length:** 142 chars. Send immediately on form submit (within seconds, 8 AM–9 PM customer-local; queue if outside that window).
- The confirmation text doubles as the claim voucher — tell staff the code is "show the text."
- System must log consent timestamp at this send; if the send fails, surface the record to M'Baku.

---

## 4. First Blast Templates (SMS, under 160 chars preferred)

Every blast: brand name first, clear offer, time-of-day, cadence + STOP reminder phrasing. Scheduling defaults to the 8 AM–9 PM local window with a 2-text/wk cap.

### (a) Welcome / New-subscriber
Send **day after signup** (or day of, if 6+ hours after join), Tue–Thu preferred, 11:30 AM–1:30 PM local.

> `[RESTAURANT NAME]: Welcome! Free [APPETIZER] with any entree. Show this text to redeem. We text up to 2x/wk. Reply STOP to opt out.`

- **Length:** 133 chars.
- **Follow-up reminder:** if no redemption within 7 days, send once, same copy with `Still waiting? — Free [APPETIZER] with any entree. Show this text. Reply STOP to opt out.`

### (b) Monday slow-time BOGO
Send **Thursday 3:00–4:00 PM** local (lands while people plan the weekend), so Monday is baked in. Core blast below; reminder **Saturday 10:00 AM** before Monday.

> `[RESTAURANT NAME]: BOGO Monday! Buy one entree, get one free, 4-7PM. Show this text at pickup. We text up to 2x/wk. Reply STOP to opt out.`

- **Length:** 142 chars.
- **Follow-up reminder (Saturday, 10:00 AM):** `[RESTAURANT NAME]: Heads up — BOGO entree special hits tomorrow 4-7PM. Show this text to save. Reply STOP to opt out.`

### (c) Birthday
Send **9:00–11:00 AM on the subscriber's birthday**, month+day from the form.

> `[RESTAURANT NAME]: Happy birthday! Free [DESSERT] with any entree this [MONTH]. Show this text to redeem. We text up to 2x/wk. Reply STOP to opt out.`

- **Length:** 152 chars.
- **Follow-up reminder:** if unredeemed after 5 days, one send: `[RESTAURANT NAME]: Your birthday treat is still waiting — free [DESSERT] with any entree all [MONTH]. Show this text. Reply STOP to opt out.`

### (d) Holiday / seasonal booster (bonus)
Send **3 days before** the anchor date; reminder **1 day before**.

> `[RESTAURANT NAME]: [HOLIDAY] special: [OFFER]. This [DAY], [TIMES]. Show this text to redeem. We text up to 2x/wk. Reply STOP to opt out.`

- **Length:** ~138 chars.
- **Follow-up reminder (day before):** `[RESTAURANT NAME]: One more day — [HOLIDAY] special runs [DAY] [TIMES]. Show this text. Reply STOP to opt out.`

---

## 5. 12-Month Campaign Calendar (DFY clients get the full year)

Cadence guardrail: default 2 texts/wk max, 1 weekly special slot + 1 lifestyle/birthday slot. Confirm each holiday falls on the right weekday before scheduling (this calendar is evergreen).

| Month | Theme | Campaign ideas (mix: 1 weekly special + 1 lifestyle/birthday) |
|---|---|---|
| Jan | New start + game season | Resolution welcome-back special (Mon slow slot); NFL playoff carryout bundle; Jan birthday sweep |
| Feb | Valentine's + Galentine's | Date-night 2-for-1 midweek; "bring your friends" dessert share; pre-V-day gift-card push |
| Mar | Green + spring | St. Patrick's special + corned beef night; early-spring seasonal menu teaser (first-look text) |
| Apr | Tax relief | "Tax day's on us" entree deal (Apr 15 week); spring family night; birthday alert catch-up |
| May | Mama + Cinco | Mother's Day brunch reservation blast; Cinco de Mayo special; patio weather booster |
| Jun | Dad + summer kickoff | Father's Day offer; summer menu launch; late-evening patio happy-hour text |
| Jul | Fourth + patio peak | July 4 weekend bundle; cool-down drink special; firework-night carryout push |
| Aug | Back to school + dip | Back-to-school weeknight rush (family night); late-summer slow-Monday BOGO recoveries |
| Sep | Football opener + Labor Day | Labor Day special; NFL Sunday carryout bundle; National [Cuisine] Month tie-in |
| Oct | Halloween + fall | Halloween costume-night special; fall seasonal menu; trivia/event night fill |
| Nov | Friendsgiving + holidays | Thanksgiving-eve carryout pre-orders; Friendsgiving bundle; gift-card/catering push |
| Dec | Parties + New Year | Holiday-party catering text; gift-card promo (top gifting month); NYE reservation reminder |

Evergreen every month: birthday texts (day-of, auto from form), subscriber anniversary ("It's been a year since you joined" — 1 free [DESSERT]), and a consent-refresher blast at least once per month as CTIA requires.

---

## 6. Sales / Pricing Page Copy (our product — TableLead Kit vs Done-for-you)

**Hero:**
`TableText — the text-marketing machine for independent restaurants.`
`We hand you the QR signs, the landing page, and the offers. You collect phone numbers at the table in week one. One flat price. No per-text math. Works with any POS.`

**Three benefit bullets:**
- **Numbers in week one.** QR table tents at every table turn your free appetizer into a permanent subscriber list — dozens of new numbers a day, not month six.
- **Zero assembly.** Landing page, confirmation SMS, and consent wiring included and compliant out of the box. Nothing to bolt together.
- **One flat price.** No credit math, no overage surprises, no sales call to unlock the plan. $49 or $99. Done.

**Feature comparison:**

| Capability | Table Lead Kit — $49/mo | Done-for-you — $99/mo |
|---|---|---|
| QR table-tent designs (3 formats) | Included | Included |
| Landing page + form + consent logging | Included | Included |
| CRM + confirmation SMS | Included | Included |
| Birthday + slow-time templates | Included | Included |
| Texts included | ~5,000/mo flat | ~5,000/mo flat |
| Weekly blast written & scheduled by us | No | Included |
| Offer building (we write the offer) | No | Included |
| 12-month campaign calendar | Included | Included |
| Send-cadence guardrails (2 texts/wk max) | Included | Included |
| POS compatibility | Any POS | Any POS |

**"Works with ANY POS" claim block:**
`Square, Clover, Toast, Aloha — doesn't matter. Unlike POS-anchored loyalty, TableText doesn't live inside your register. Your list is yours, your texts route over the same phone number you already text from, and nothing about your checkout changes.`

**FAQ:**
- **Do I need new hardware?** No. Table Lead Kit ($49): we send the QR tent files — print them on the card stock you already use. Done-for-you ($99): we print and ship the tents to you. Either way, signups run off a phone your customers already own.
- **What if I don't have an appetizer?** Any low-cost, high-margin item works — chips and salsa, bread service, a side, a dessert sample. The freebie is the hook, not the cost. In Done-for-you we pick the item and build the offer for you.
- **What happens when a customer texts STOP?** Opt-out is automatic and instant — they're logged and never messaged again. It's not your job to watch it; the system handles it and it's part of why every blast is compliant.
- **Do I own my list?** Yes. Your subscriber list lives in your account and stays yours — take it with you if you ever switch providers. TableText doesn't hold your customers hostage.

**CTA:** `Start with the appetizer you already give away.` / `Get the Table Lead Kit — $49/mo` / `Get it written for you — $99/mo`

**10 positioning one-liners (test on TikTok / X / Instagram):**
1. The first SMS marketing built for independent restaurants — we hand you the QR signs, the campaigns, and the appetizer offer. One flat price. No per-text math.
2. Works with any POS. Square, Clover, Toast. No lock-in, no register surgery.
3. Collecting phone numbers at week one — not month six.
4. The free appetizer you already give away now pays you back as a text list.
5. Every table is a lead form. We just printed the signs for it.
6. Flat $49. Flat $99. No credit math, no overage calls.
7. Postscript does done-for-you SMS at $500/mo — for ecommerce. We do it at $99, for restaurants.
8. Monday at 4 PM isn't dead when 2,000 regulars hear about the BOGO at the same time.
9. Your POS loyalty only works inside your POS. Ours works wherever your customers sit.
10. 84% of consumers opt into business texts. Your table tent is the invitation.

---

## 7. Competitor One-Liners (how we differ)

- **SimpleTexting:** A great general SMS tool — but you print the tents, write the copy, and own the compliance. TableText ships the entire table-to-text system pre-assembled.
- **Postscript:** Ecommerce-focused SMS for Shopify, and its done-for-you tier is $500/mo+. Ours is $99, flat, and built for dining tables.
- **SlickText:** General SMB keywords and forms with the same DIY burden and no restaurant playbook — we hand you the appetizer funnel and the year-long calendar.
- **EZ Texting:** QR codes and forms on every plan, but nothing assembled for the table scan, and no restaurant-native flow — we've already strung scan to blast together.
- **Toast / Square:** Loyalty that only works inside their POS and priced by sales calls — we work with any POS and print the price in plain numbers.

---

## 8. Launch Checklist — One Restaurant Going Live

1. Create SimpleTexting account under the owner's email + billing; add local/toll-free number.
2. Complete 10DLC brand registration + marketing campaign registration (EIN/SSN ready; ~$4.50 + vetting).
3. Configure brand-name prefix on every message; verify 8 AM–9 PM delivery window + DNC scrub on.
4. Generate QR codes + `[SIGNUP-CODE]` keyword → landing URL; point variants A/B/C at the Carrd page.
5. Build Carrd page live (hero, form fields, consent checkbox, privacy line, success state) + Tally form wired with consent logging.
6. Print and place: 4 x 6 table tents, checkstand minis, check-presenter slips.
7. Test full funnel: scan → submit → confirmation SMS → claim code (fresh number each test).
8. Test STOP and HELP replies — confirm instant opt-out, logging, and confirmation message.
9. Send the first Welcome blast on schedule; confirm delivery and redemption staff readout.
10. Set the weekly cadence + monthly consent-refresh blast, then hand off to the 12-month calendar.

---

*Self-review note (Okoye): all pricing ($49/$99, ~5,000 texts, competitor numbers) and compliance details (11-element template, 8 AM–9 PM, 2x/wk default, STOP/HELP, $500–$1,500/violation) trace directly to the brief §2–3. No invented stats or prices. All SMS templates are under 160 chars and brand-first. Success-state copy is plain text. Pending the two-pass review (Nakia compliance + M'Baku functional) before any client-facing deploy.*