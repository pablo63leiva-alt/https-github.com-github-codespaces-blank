# TradeLift Education Lead-Gen Playbook (CPL)

**Owner:** Fury (growth/monetization) · **Build:** Jarvis · **Contracts/signatures:** Pablo
**Status:** STRATEGY & SITE-PLAN — no live-site changes made in this session (create-only).
**Compass:** feeds REVENUE-OPS.md Pillar 5 / Stretch lane (~$1.5K sponsorship/school bulk, and the breakout trigger).

---

## (a) The model — and why our quiz funnel is the fit

**What trade schools pay for:** qualified, form-submitting leads — prospective students who
(1) took an interest in a trade, (2) gave contact info, (3) are a legal age to enroll. That is
*exactly* the output of a quiz → email funnel. This is "CPL" (cost-per-lead) lead generation,
and it is the standard acquisition model for for-profit career schools. The typical mechanism
is an "info request" form: a school-branded page where the student asks for information and the
school (or a media partner) gets a payout per qualified submission.

**Why TradeLift's quiz is a stronger fit than a cold form:**
- Our 10-question quiz *pre-qualifies* — a user who finishes "Which Trade Is For You?" and opts
  in for a Career Roadmap has self-declared interest in a specific trade. That is a higher-intent
  lead than a generic banner click.
- We hold interest data (which trade), so we can route each lead to the *matching* school program
  (electrician leads → electrician-focused schools). Relevance raises conversion and keeps us
  reputable.
- We reach exactly the demographic schools pay most for: 16–24, undecided, actively exploring —
  the same person who is on `utip.edu`, `lincolntech.edu`, or `pennfoster.edu` right now.
- We are the neutral "which trade fits me" layer in front of the school — a position schools
  themselves don't occupy (they can't be neutral about their own programs).

**Payout shape (HONEST, no fabricated numbers):** Career-school CPL payouts are typically paid
per *completed, validated* lead submission (name + email + phone + trade interest), not per quiz
completion and not per prospect click. Public program pages almost never publish exact fees.
**Never state a specific dollar figure as fact unless a partner agreement documents it.** Use the
$XX–$XXX/lead band below only as a marked *estimate* for internal planning. Rule of thumb used in
planning only: **plan at the low end of the band; treat a signed rate as a win.** A deal that pays
per *enrolled student* (a step higher up the funnel) is rarer and slower but worth asking for on
matching-trade traffic.

**Estimated planning band (clearly estimate, confirm at contract):** ~$5–$50+ per qualified CPL,
~$100–$500+ per enrolled-student CPA, for for-profit career schools. Community colleges and
public CTE programs rarely pay — but they are still worth a *link* relationship (authority +
traffic, per the existing school-outreach playbook).

---

## (b) Partner targets that EXIST today

### Verified public "partner with us" programs (2026-09-14)

**1. Universal Technical Institute (UTI) — `https://www.uti.edu/partner-with-us`**
- Verifiably live "Partner With Us" page. This is the highest-probability inbound: UTI explicitly
  invites partnerships and has a national network (auto, diesel, HVAC, welding, CNC, collision).
- Action: read the page's partner categories and form; pitch exactly what they ask for (leads, co-branded content, or enrollment). If there is a media/affiliate category, use it.
- **Verify at signup:** exact payout, lead definition, their tracking (must tag UTM + their pixel),
  minimum volume, territory rights, and whether they require phone-verified leads.

**2. Lincoln Tech — `https://www.lincolntech.edu`**
- Actively runs partnerships (per PM research) across a wide program list (auto tech, electrician,
  HVAC, welding, nursing, culinary — several overlap our 12 trades).
- Action: search their site for "affiliate", "partner", or "licensure" pages; if nothing public,
  route via the partnership route in (b2) below.

### Outreach routes for schools WITHOUT a public program (b2)

When no partner/affiliate page exists, pitch **Marketing or Admissions** a *media partnership*
(not a lead deal — a word that exists in their vocabulary):

> "We'd publish/sponsor a Trade School Programs hub page + per-trade request-info landing pages
> that send qualified, trade-matched prospects to your admissions team. You approve the final
> copy, we handle the funnel, you pay per qualified lead you accept."

Talking points that get returned:
- Brand-safe: they approve copy, we disclose honestly (see §d), no payday tricks.
- Qualifying first: we pass trade-interest + quiz completion, so their admissions counselors get
  warm, relevant leads instead of cold form farms.
- Low commitment to trial: a 30-day pilot of one trade, one page, one campus/territory.
- The school keeps you on retainer as a recurring media channel if it performs.

Warm intake routes: any **"Contact Admissions" form** is a legitimate first touch — write to the
marketing director, mention the pilot offer, include the quiz link so they can see the quality.
Admissions teams are graded on lead volume; a credible free pilot is an easy yes.

### Candidates to INVESTIGATE (agency/affiliate signup route — DO NOT bilk, confirm program)

**Penn Foster — `https://www.pennfoster.edu`** (and Penn Foster High School):
- One of the largest self-paced career/degree schools (HS diploma, trades, healthcare). Long-running
  affiliate/partner ecosystem; distance-learning fits a 16–24 audience who will never sit on campus.
- Flag: **confirm program at signup** — the exact rates and approval path change; never assume the
  old published numbers still hold. (Fury did not verify current payout pages.)

**Ashworth College — `https://www.ashworthcollege.edu`** + **James Madison High School**:
- Self-paced career education at high-school/career w/ certificate level; historically run affiliate
  programs. **Flag: confirm program at signup** — same rule as Penn Foster.

Also worth one pass each (timeboxed, in the 14-day list): WyoTech, UTI's marine/Diesel tech, Porter
& Chester, Tulsa Welding School, and community-college CTE departments (link-only value, no pay).

> **Global honesty rule:** We only advertise accredited, currently-operating schools that we have
> personally verified are accepting students. No "exact payout" is ever printed in copy without a
> signed agreement. Internal planning uses `$X–$Y` marked **estimate**.

---

## (c) EXACT site changes to monetize (build spec for Jarvis)

### 1. "Trade School Programs" hub page — `tradeschools.html` (new)
- Explainer: what trade school is, cost/ROI guardrails (honest — includes "for-profit ≠ bad, but
  read the fine print on placement rates and keep it debt-aware"), and a "how to pick one" checklist.
- Grid of partner trades/regions that reroutes to per-trade landing pages (item 2).
- Every partner placement includes a clear disclosure line (see §d).
- Reuse dark-industrial theme, existing CSS classes; no new framework.

### 2. Per-trade request-info landing pages — `tradeschools/electrician.html`, `welding.html`, … (new)
One per trade we can monetize (start with the 2–3 trades our partner actually offers; scaffold the
rest as placeholder-score templates).
- Page anatomy: trade overview (salary band from site-canonical data), "what you'll actually do",
  "what it costs & what you earn", then a **request-info form**.
- Form fields (best practice, keep to ~5): email, first name, phone (optional-but-encouraged), trade,
  zip. Phone boosts CPL value; make it optional at launch, A/B later.
- Submissions POST to Formspree-formated endpoint for partner transfer (Jarvis integrates a new
  Formspree ID `f/…` per partner), with a `?utm_source=tradelift&utm_term=<trade>` tag for
  attribution.
- The page's CTA says exactly what happens next ("a counselor from [Partner] will email you") —
  no ambiguity, no fabricated timing.

### 3. Quiz-results routing — link the career-roadmap success moment
- After quiz results + email capture (Formspree `xzebljww` handles the trade field already), show a
  second, optional CTA on the results card: **"See training programs for [matched trade]"** →
  `tradeschools.html#<trade>`.
- Keep it NON-GATED and secondary: results stay free; the CPL page is the opt-in, never a
  requirement to see quiz results (respects the existing funnel design + compliance §d).
- If a routed user submits a request-info form, that person also stays on the newsletter list
  unless they opt out — disclose on the form ("want program info + occasional TradeLift tips" checkbox).

### 4. Email-list handoff
- New list segment tag: `trade-school-intent` (from the request-info submit) vs `general` (newsletter).
- Sends between partner and list: partner leads go to the partner; non-lead subscribers continue the
  normal email sequence (§ email-sequence.md). We never sell the list; we monetize *at opt-in* via
  the routed form and keep everyone else in the nurture flow.

### 5. Disclosure compliance (ship WITH the pages, not after)
- Visible text on every monetized page, above the form: **"We may earn a referral fee when you
  request info from a school on this page. This doesn't affect what we recommend, and it doesn't cost
  you anything."**
- `rel="sponsored"` on any outbound partner/affiliate links.
- Privacy Policy (docs/adsense-readiness.md §A) updated to disclose data transfer to education
  partners before any partner live — required by FTC guidance on endorsement + data honesty.

---

## (d) Compliance guardrails (NON-NEGOTIABLE)

1. **FTC truthful advertising** — every monetized page is accurate about earnings, costs,
   placement rates, and timelines. No "guaranteed jobs", no invented success stories.
2. **Only real, accredited schools** — partner programs are live page-verified before going up;
   accredited status checked (accrediting-body mention on school site). Drop any partner the moment
   its accreditation or status stops checking out.
3. **Never trap or deceive users** — request-info = explicit choice, clearly labeled as contact info
   being shared with a school. No pre-ticked boxes, no "confirm your email for the guide" that
   actually signs you up for a school. Quiz stays free; monetized CTA is clearly optional.
4. **No lead fabrication / no phone-bait** — we pass real quiz completions; we never re-key data,
   never send someone to a school they didn't choose, never submit a user without a click.
5. **Age honesty** — minors need a parent/guardian for many enrollment paths; pages say so rather
   than pushing signups on under-18s. Don't route 16–17-year-olds into enrollment forms without a
   parent line.
6. **Disclosures stay visible** — every monetized surface (hub page, landing page, quiz card, email
   in the sequence that links to a school) carries the §c5 disclosure or a close equivalent.
7. **Data** — partner handoff is limited to what the user knowingly submitted; stored per
   Formspree terms; deletable on request (echoed in Privacy Policy).
8. **Cross-check with outreach playbook** — never double-funnel the same counselor thread; the
   school-outreach pack (`docs/school-outreach-emails.md`) is the warm B2B funnel, this playbook is
   the monetization funnel. They combine, they don't collide.

---

## (e) 14-day activation checklist (owners: Jarvis builds · Pablo signs/sends)

| Day | Task | Owner | Done? |
|-----|------|-------|-------|
| 1 | Read UTI "Partner With Us" page; catalog categories + form fields; note deadlines | Jarvis | ☐ |
| 1 | Read Lincoln Tech site; locate partner/media contact or admissions/marketing route | Jarvis | ☐ |
| 2 | Draft partner pitch (UTI & Lincoln Tech variants, 150–200 words) + pilot-terms one-pager | Jarvis | ☐ |
| 2 | Investigate Penn Foster + Ashworth affiliate/agency signup paths — confirm CURRENT program at signup, record rates/funnel | Jarvis | ☐ |
| 3 | Send UTI + Lincoln Tech pitches (formal partners route) | Pablo | ☐ |
| 3 | Send Penn Foster + Ashworth signup applications (if program confirmed live) | Pablo | ☐ |
| 4 | Build `tradeschools.html` hub skeleton (per §c1) on `origin` (NO deploy) | Jarvis | ☐ |
| 4–6 | Create per-trade request-info landing pages for 2–3 first trades (electrician/welding/HVAC), scaffolded for all 12 | Jarvis | ☐ |
| 5–7 | Wire Formspree new partner endpoint(s) → route submissions; add quiz-results "training programs" CTA (secondary, non-gated) | Jarvis | ☐ |
| 6 | Interview + appoint one pilot partner (highest-fit of UTI/Lincoln/PennFoster/Ashworth) | Pablo | ☐ |
| 7–9 | Partner approves copy + pilot terms → **Pablo signs partnership agreement**; fix any FTC/legal wording with partner counsel | Pablo | ☐ |
| 8 | Add disclosures to all monetized pages + Privacy Policy update; `rel="sponsored"` audit | Jarvis | ☐ |
| 10 | Dual QA pass (Rogers Pass 1, Romanoff Pass 2) on new pages + funnel wiring | Squad | ☐ |
| 11 | Deploy (`scripts/deploy-surge.sh`); smoke-test forms + quiz CTA live | Jarvis | ☐ |
| 12 | Email each existing newsletter/ quiz subscriber a "program info" option email (opt-in routed to partner) | Jarvis | ☐ |
| 13–14 | First lead handoff to pilot partner; confirm their acceptance criteria + attribute success; log numbers in PROGRESS.md | Pablo + Jarvis | ☐ |

**Success gate for the pilot:** partner accepts ≥1 lead in the first 14 days → scale to more
trades/territories in window 2 and level-up the email-sequence school email (§ email-sequence.md
Email 4). No acceptance, no scale-from-fraud: debug lead quality (fields, UTM, phone capture)
before widening.

---

*Honest expectation: education CPL is a stretch/pilot revenue lane in the 100-day window — realistic
low-tens-vs. $50K-scale. It earns its keep as (1) the only lane where one signed partner deal is a
headline-number event, (2) a qualification/authority signal that lifts school-outreach backlinks,
and (3) the February+ growth lane TradeLift will need after Dec 22. Build it lean, pilot it fast,
kill it bluntly if leads don't convert.*