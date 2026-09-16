# TableText — MVP Build Doc (Single-Session Build Guide)

> **Purpose:** Ship the entire TableText MVP for one pilot restaurant using SimpleTexting as the LEGO core (CRM + SMS + form/keyword + automations), with a Carrd landing page, native/Tally form, and FREE QR generators. One operator, working in one ordered pass on Pablo's SimpleTexting account, builds the whole product in a single session (~3.5–4.5 hours) — the only thing that does not complete in-session is the 1–3 day 10DLC approval wait.
> **Author:** T'Challa (Side-Project Squad Lead) · **Squad:** Shuri² (build) · Namor (plumbing) · Nakia (compliance copy) · Okoye (GTM copy) · M'Baku (QA test script, §8) · **Date:** 2026-09-16
> **Compliance gate:** every SMS template in this doc is copy-pasted from `docs/tabletext-launch-kit.md` and `docs/tabletext-consent-and-privacy.md`, which already passed Nakia compliance review. Do not reword any consent/opt-out/STOP language; only swap placeholders for the restaurant's real values.
> **Sources (read together, in this order):** `docs/vibe-smart-loyalty.md` (positioning, pricing, compliance risk) · `docs/tabletext-consent-and-privacy.md` (consent copy, privacy blurb, logging spec, guardrails, 12-item checklist) · `docs/tabletext-launch-kit.md` (tent copy, landing copy, blast templates, confirmation SMS).

---

## 0. Build-order summary (what ships, in what order)

| Step | Section | Result | In-session time |
|---|---|---|---|
| Pre-flight + first registrations | §1 | Brand reg filed ($4.50), campaign reg filed, plan + number chosen | 15–20 min |
| Account setup | §2 | Live SimpleTexting account, brand, number, 10DLC status | 20–30 min |
| Keyword + opt-in | §3 | `APPETIZER` keyword live, STOP/HELP auto, consent wiring | 15–20 min |
| Confirmation automation | §4 | Claim SMS fires on signup | 10–15 min |
| Form + landing | §5 | Signup form + Carrd page live, consent logging | 45–60 min |
| QR codes | §6 | 3 tent variants, print-ready | 20–30 min |
| Blast scheduling | §7 | Welcome, BOGO, birthday, holiday, monthly STOP reminder on calendar | 30–45 min |
| QA (M'Baku script) | §8 | Full funnel proven on a scratch phone | 30–45 min |
| Weekly ops + go-live | §9–10 | Owner routine + 12-point launch gate | 10 min/wk + go-live |

**Budget target for the pilot (from the brief, ~$60–90/mo):**

| Item | Cost | Source |
|---|---|---|
| SimpleTexting — 1,000 credits plan (1 SMS = 1 credit) | $49/mo | brief §2/§3 |
| Local number | $10/mo | brief §3 |
| 10DLC brand registration (TCR, one-time) | $4.50 | brief §3 |
| 10DLC marketing campaign vetting (one-time) and monthly fee (Marketing $10/mo, or Low-volume $1.50/mo if <6K segments/day) | ~$15 once + $1.50–10/mo | brief §3 |
| Carrd page | $0 on the free `carrd.co` subdomain; Pro $19/yr if a custom domain is required | brief §3 |
| QR generator | $0 (QRCodeMonkey free tier or any free generator) | brief §3 |
| **Total** | **≈ $60–70/mo ongoing** ($49 + $10 + $1.50–10 campaign fee). First month adds the ~$20 one-time fees ($4.50 brand + ~$15 vetting) → ≈ $80–88, inside the brief's $60–90 window. | — |

If the pilot ever needs more than 1,000 credits, the plan moves up to 2k ($79/mo) or 3k ($109/mo) — that is a decision to make later, not in-session.

---

## 1. Pre-flight — what Pablo must have, and what happens FIRST

### 1.1 What Pablo must have before starting

- [ ] **An email address Pablo controls** — the account owner email. Use a `@` address you check daily; SimpleTexting login, TCR status emails, and billing notifications go here.
- [ ] **EIN or SSN** for the test restaurant / brand — required for the 10DLC brand registration (TCR). Have the legal entity name and the EIN on hand; a sole proprietor can supply the SSN instead. (The dashboard may label this differently, e.g. "Tax ID" — confirm before saving.)
- [ ] **~$50–90 available for the first month's budget** plus one-time fees (~$20 once: $4.50 brand + ~$15 vetting).
- [ ] **Chosen product name** — the working name is "TableText" (brief §5, Pablo to confirm). The name drives the landing page title and any client-facing materials, not the SMS copy (SMS copy is branded to the restaurant).
- [ ] **Chosen test restaurant info** — this becomes every placeholder below. Fill this table BEFORE touching the dashboard:

| Field | Value assigned in-session | Used in |
|---|---|---|
| Product name | `TableText` (confirm) | Landing page, this doc's name |
| Restaurant legal name | `[RESTAURANT NAME]` | Brand, consent copy, every SMS |
| Restaurant billing/operator name | same or separate | 10DLC brand "operator" (the dashboard may label this differently) |
| Restaurant EIN or owner SSN | `[TAX ID]` | 10DLC brand (TCR) |
| Address + industry code | `[ADDRESS]` · restaurant | 10DLC brand |
| Keyword | `APPETIZER` (per restaurant; 4–14 chars, letters) | Keyword opt-in, consent copy |
| Freebie item | `[APPETIZER]` | Confirmation + tent copy |
| Entree used to qualify | `[ENTREE]` | Tent offer terms |
| Local time zone of the restaurant | `[TZ]` | All scheduling |
| FL or OK venue? | Yes/No | 8 PM send cutoff instead of 9 PM |
| Support contact (email/phone) | `[SUPPORT CONTACT]` | HELP message |
| Terms URL · Privacy URL | `[TERMS URL]` · `[PRIVACY URL]` | Consent line, privacy blurb, tent tiny print |

### 1.2 What happens FIRST (in this order)

These two items must be filed on day one because approval takes 1–3 days; every other build step proceeds while they are pending.

1. **File the 10DLC brand registration** (~$4.50, one-time, via TCR). When this passes, campaign registration is unlocked.
2. **File the 10DLC marketing campaign registration** (vetting ~$15 + the monthly marketing fee). This is what makes promotional blasts legal.
3. **Choose the number type: local number** (the brief's default, $10/mo at SimpleTexting). A toll-free number is a compliant alternative but goes through a verification process that can take longer (the dashboard may label this differently — confirm before saving). For a single-session pilot, pick the **local number**.
4. **Pick the plan: SimpleTexting 1,000-credits level** ($49/mo). This matches the ~5,000-texts-flat product promise for the pilot phase (1 SMS = 1 credit; the pilot list is far under 1,000 sends/month).

Rule: **do not change the registrations mid-build.** If a registration comes back with a correction request, fix the field it names and resubmit — do not create a second brand. If TCR approval is not back by go-live, the go-live gate in §10 blocks the first blast (item 1–3 of the 12-item checklist).

---

## 2. Account setup — SimpleTexting signup → brand → number → 10DLC

### 2.1 Create the account

1. Open SimpleTexting's signup page. Sign up with Pablo's email (`[ACCOUNT EMAIL]`) and a strong password. On payment, add the billing card — the 1,000-credit plan bills $49/mo; the local number bills $10/mo once provisioned.
2. You will be asked for business info during signup. Enter the restaurant's legal name as the business/brand name here so later screens pre-fill. (The dashboard may label this differently, e.g. "Company" — confirm before saving.)
3. Verify the email (confirmation link in Pablo's inbox) before proceeding.

### 2.2 Set up the brand

1. Navigate to the brand/account section (look for "Settings", "Account", or "Brand" — the dashboard may label this differently — confirm before saving).
2. Verify the brand/business name shows the restaurant's legal name. This name is what carriers see for 10DLC; it should match the TCR brand you file in §1.2 exactly (legal name, not the casual short name).
3. Add the restaurant's address and industry; the SMS/research brief marks hospitality as SMS's #2 vertical — select the restaurant/food service category if offered. (The dashboard may label this differently — confirm before saving.)

### 2.3 Provision the number

1. Go to the numbers section ("Numbers", "Phone numbers", or "Text numbers" — the dashboard may label this differently — confirm before saving).
2. Select the **local number** for `[CITY/AREA]` and one `[RESTAURANT NAME]` number. This number becomes `[PHONE NUMBER]` in every consent line and SMS template — write it into the value table (§1.1) now.
3. Confirm the number appears under the brand, and that two-way (text in and out) is enabled.
4. Send yourself a test text: confirm it arrives and that replies come back to the SimpleTexting inbox. This is the §7 checklist item 3 ("number tested, sending and receiving both work").

Note: if you picked toll-free instead of local, expect a brand-verification step (the dashboard may label this differently — confirm before saving) and a longer wait before outbound works. It is a valid plan-B path, not the default for this session.

### 2.4 10DLC registration inside the dashboard

1. Locate the compliance/10DLC area (look for "Compliance", "10DLC", "Messaging policies", or "Registration" — the dashboard may label this differently — confirm before saving).
2. You should see the two registration types:
   - **Brand registration** — one-time, ~$4.50, files to TCR. Fields that WILL appear, in generic form: legal business name; Doing-Business-As (DBA) name; EIN/TAX ID or SSN; business address; business type (e.g. LLC, sole prop); contact email/phone. Answer with the §1.1 table values.
   - **Campaign registration** (unlocks after brand approval) — fields that WILL appear: campaign name (e.g. "`[RESTAURANT NAME]` text promotions"); campaign description (e.g. "Promotional text messages: weekly specials, Monday BOGO, birthday offers, holiday offers, to subscribers who opt in by scanning a QR code at the restaurant or texting the keyword"); sample messages (paste the 142-char confirmation SMS from §4.1 and the Welcome blast from §7.1); target segments (e.g. "consumer", "General"; choose the standard consumer/marketing campaign type). These are the standard TCR fields — the specific labels may vary, so (the dashboard may label this differently — confirm before saving).
3. Where the dashboard asks for a "use case", pick the marketing/advertising campaign use case — do not pick a P2P or utility use case; the blasts in §7 are promotional.
4. Submit. Record the submission date, status, and any identifiers in the restaurant's folder. Approval is typically 1–3 days; outbound texting to US numbers is blocked until the campaign is approved.

---

## 3. Keyword + opt-in — the `APPETIZER` keyword, consent, STOP/HELP, frequency caps

### 3.1 Create the keyword

1. Open the keyword section ("Keywords", "Text keywords", or "SMS keywords" — the dashboard may label this differently — confirm before saving).
2. Create a new keyword: `APPETIZER` (per-restaurant; example from the brief). Assign it to the local number `[PHONE NUMBER]`.
3. Set what happens when a customer texts the keyword. Two compliant options:
   - **Text-to-join (simple):** the message itself is the opt-in. On receipt, the contact is added to the list.
   - **Two-step confirmation (recommended by this build):** the customer texts `APPETIZER`, the system replies asking them to confirm, and they are only added after they confirm. This is **double opt-in** and gives the strongest TCPA record. Enable the confirmation step if the dashboard offers it (the dashboard may label this differently, e.g. "Confirmation message" or "Double opt-in" — confirm before saving). The confirmation reply may reuse the §4.1 confirmation SMS or a plain "Reply YES to confirm" line.
4. Set the auto-reply/confirmation for the keyword. This build uses the **form** as the primary consent path (§5), so the keyword line is the compliance-canonical text-to-join path and must match §1.3 of the consent doc verbatim in structure. Use exactly (with real values swapped in):

> `[RESTAURANT NAME]: By texting [KEYWORD] to [(555) 555-5555], you agree to receive promotional messages sent via an autodialer. You also agree to the terms of service ([website.com/terms]) and privacy policy ([website.com/privacy]). This agreement isn't a condition of any purchase. Message frequency varies. Message and data rates may apply. Reply STOP to opt out; HELP for more information.`

   Swap `[RESTAURANT NAME]`, `[KEYWORD]` (`APPETIZER`), the real `[PHONE NUMBER]`, and the live `[TERMS URL]` / `[PRIVACY URL]`. All 11 elements stay word-for-word; only values change.

### 3.2 The Nakia consent wording slot (form path)

The check-the-box consent on the form is the recorded consent, straight from `tabletext-consent-and-privacy.md` §1. Use exactly:

- **Checkbox label (§1.2a), off by default:**

> I agree to receive promotional text messages from [RESTAURANT NAME] at the phone number I entered. Message frequency varies and message/data rates may apply. Reply STOP to opt out; HELP for help. This is not a condition of any purchase.

- **Full 11-element disclosure (§1.3) directly beneath the checkbox, unbolded, at label size** (this is REQUIRED, not optional):

> **[RESTAURANT NAME]:** By texting **[KEYWORD]** to **[(555) 555-5555]**, you agree to receive promotional messages sent via an autodialer. You also agree to the terms of service ([**website.com/terms**]) and privacy policy ([**website.com/privacy**]). This agreement isn't a condition of any purchase. Message frequency varies. Message and data rates may apply. Reply STOP to opt out; HELP for more information.

Swap the placeholders: `[RESTAURANT NAME]`, keyword `APPETIZER`, the real `[PHONE NUMBER]`, and live `[TERMS URL]` / `[PRIVACY URL]`. Rule: do not delete or reword any of the 11 elements — only swap values.

### 3.3 STOP / HELP auto-configuration

These are provider-level behaviors from `tabletext-consent-and-privacy.md` §5. Everything below must be ON or verified during setup (the labels may vary):

- [ ] **STOP processed instantly:** `STOP`, `STOPALL`, `UNSUBSCRIBE`, `CANCEL`, `END`, `QUIT` (case-insensitive, trimmed) remove the number from all promotional lists immediately. If the dashboard exposes a "compliance keywords" setting, enable all of them.
- [ ] **Auto opt-out confirmation sent once** (exact copy from §5, no promotional content): `You're unsubscribed from [RESTAURANT NAME] texts. No further messages will be sent. Reply HELP for help.`
- [ ] **HELP handled automatically** (exact copy from §5): `For help with [RESTAURANT NAME] texts, reply or contact [SUPPORT CONTACT]. Msg freq varies; msg & data rates may apply.`
- [ ] **Provider-level suppression persists across lists/segments** — a STOP is permanent everywhere, not list-by-list. Confirm during the §8 test.
- [ ] **No automated resubscribe prompts** — no "text YES to resubscribe." Resubscribe requires a fresh opt-in (new form submission with the consent box checked). (The dashboard may label this differently — if it offers a resubscribe prompt, leave it OFF.)

### 3.4 Frequency caps

The brief's guardrails define the cap — the dashboard may not have a "2/wk" toggle, so the schedule itself is the enforcement (the dashboard may label this differently — confirm before saving):

- Hard cap **2 texts/week per subscriber TOTAL** (the welcome/confirmation counts).
- Default mix: exactly **2 slots — 1 promotional offer blast + 1 welcome/lifestyle/birthday** per week. Never schedule more than one promotional blast in a week.
- Any increase requires Nakia compliance sign-off — not something to configure in-session.
- Every outbound message must start with the brand name (every template in this doc already does).

Keep the cap expressed as a written rule in the owner's weekly checklist (copy this line): "This week's schedule = max 1 promotional + 1 welcome/lifestyle/birthday."

---

## 4. Automation 1 — Confirmation / claim SMS

### 4.1 Create the automation

1. Open the automations/workflows section ("Automations", "Automation", or "Workflows" — the dashboard may label this differently — confirm before saving).
2. Create a new automation: **Trigger = contact signs up via the form or keyword** (trigger options may be labeled "Form submitted", "Keyword received", or "Contact added to list" — confirm before saving). This automation is the claim flow, the same path whichever way they joined.
3. **Action = send an SMS to the contact**, this exact message (from `tabletext-launch-kit.md` §3, **142 chars**, send immediately on submit):

> `[RESTAURANT NAME]: Thanks for joining! Show this text to claim 1 free [APPETIZER]. We text up to 2x/wk. Reply STOP to opt out, HELP for help.`

4. **Claim-voucher behavior:** this text IS the voucher. For incoming replies making a claim, set the staff-facing reply copy to "show the text" — the code is the message on the customer's phone, not a separate code. The redemptions readout for staff (from §7 checklist item 9) is "customer shows the confirmation text" and the restaurant applies the free [APPETIZER] per the tent offer terms.
5. **Time-of-day guard against sending:** the confirmation should only send inside the 8 AM–9 PM local window (FL/OK 8 AM–8 PM). If the automation offers a send-time filter or queue, enable it; otherwise note in the owner's checklist that confirmations are immediate but any send stuck outside the window will look delayed — the §6 guardrail table governs all sends. (The dashboard may label this differently — confirm before saving.)
6. If the send fails, the record must be surfaced: check the automation's activity/failed-send log for the contact (the dashboard may label this differently, e.g. "Logs" or "Activity" — confirm before saving). §8 test step 3 exercises this end-to-end.

### 4.2 Consent logging at this send

The form submit already logged consent (see §5.4). At the confirmation send, confirm the contact record now shows: phone (E.164), name, list/group, opt-in timestamp, and source (`QR-tent` / `landing-URL` / `keyword-text`). This is the provider-side consent log; the retrievable artifact is the §5.4 weekly export. If any of these fields are empty on a test contact, fix the form/keyword mapping before the go-live gate.

---

## 5. Form / landing — native form (preferred) or Tally, plus the Carrd page

### 5.1 Which form layer to use

**Preferred: SimpleTexting's native form** (form builder inside the account — "Forms", "Signup forms", or "Pages" — the dashboard may label this differently — confirm before saving). It is the LEGO core: the form submit creates the contact and fires the §4.1 automation with zero glue. Paste the form onto the Carrd page via embed.

**Fallback: Tally.so** (free tier) embedded in Carrd, when the native form cannot produce the consent checkbox + disclosure layout or the success state shown below. Parity requirements are the same: same field order, consent off-by-default, same success state. (The dashboard may label this differently — confirm before saving.)

### 5.2 Field order and behavior (from `tabletext-launch-kit.md` §2)

Set these in the form, top to bottom, all inputs ≥44 px tall (thumb reach), single column, mobile-first:

1. **Name** — label: `Your name (first name is fine)` · required
2. **Phone** — label: `Mobile number` · required · placeholder/E.164 format `+1 (555) 555-5555`
3. **Email (optional)** — label: `Email (optional)` · not required
4. **Birthday (optional)** — label: `Birthday — month and day (optional, for a free birthday treat)` · month+day only
5. **Consent lead-in** — `Check the box to join:`
6. **Consent checkbox** — the §3.2 checkbox copy · **OFF by default** (never pre-checked)
7. **Full 11-element disclosure** (§3.2) directly beneath the checkbox, unbolded, label size
8. **Submit button** — label: `Claim my free [APPETIZER]` · **disabled until name, phone, and consent box are all populated/checked**

### 5.3 Consent artifact rules (from `tabletext-consent-and-privacy.md` §4)

- On submit, log: consent timestamp (UTC), IP address, form copy version, entered values, campaign/keyword.
- **Authoritative artifact rule (§4.2):** for every restaurant, export to CSV and/or Airtable **no later than end of week**. Native-form path: export the SimpleTexting contacts/consent log to CSV and store it in the restaurant's folder, tagging `form_copy_version` (e.g. `v1.2`) on each row. Tally path: the Tally response export carries the submission timestamp + respondent IP automatically — that export is the retrievable, court-ready copy. Add one row per submission: timestamp UTC, name, phone (E.164), email, birthday, IP, form version, campaign (`APPETIZER`), source (`QR-tent` / `landing-URL` / `keyword-text`), status.
- **Retention:** keep consent + opt-out records for the lifetime of the subscription plus a minimum of 5 years (§4.3). Archive in the restaurant's folder; never delete on list purge alone.
- **Proof-of-consent retrieval (documented, §4.4):** on any request, look the number up in the archive by phone → pull timestamp/version/IP/campaign → cross-reference the SimpleTexting consent log → reassemble into a single export and attest. Keep a log of the retrieval request itself.
- **Privacy blurb under the form footer (§2)** — paste under the form, above/beside submit:

> We collect your name and phone number (plus your email and birthday if you share them) so we can text you offers, promotions, and event updates. We never sell your information. You can opt out anytime by replying STOP. Read our full privacy policy here: **[link]**.

`[link]` → the §3 privacy policy URL. Keep it to 3–4 lines; anything longer goes in the full policy.

### 5.4 Carrd page assembly (blocks, top to bottom, from `tabletext-launch-kit.md` §2)

Build the page in Carrd with these blocks in exactly this order:

1. **Offer hero** — Headline: `Free [APPETIZER] on us.` Subhead: `Join the [RESTAURANT NAME] text list and your first appetizer's covered — up to 2 texts a week, never more. Birthdays and slow-night specials included.`
2. **Form** — embed the §5.1 form (native or Tally) with the §5.2 fields.
3. **Social proof strip** — `[NUMBER] regulars already text with us. Slow Mondays are now answered with a text.` Rule: replace `[NUMBER]` with the real live count; do not run this block before the number is true (start hidden).
4. **Privacy line (small, under the form)** — `We only text [RESTAURANT NAME] news, offers, and birthdays. No sharing, no spam — opt out anytime with one word: STOP.` (plus the §5.3 privacy blurb per the consent spec)
5. **Success state (replaces the form — do not navigate away)** — `Check your texts for your appetizer code.` and, small, on the next line: `Show that text next visit to claim your free [APPETIZER].`

Meta: page title `[RESTAURANT NAME] — Free [APPETIZER]`. Publish on the free `carrd.co` subdomain for the pilot; a custom domain (Carrd Pro, $19/yr) is the optional later upgrade — record the URL as `[LANDING URL]`, which is what every QR in §6 points at.

---

## 6. QR codes — the three tent variants, sizing, and printing

### 6.1 Generate the codes

1. Use QRCodeMonkey (free tier) or any free QR generator.
2. **Payload = the `[LANDING URL]`** from §5.4 (the Carrd page). High error-correction setting (the highest available) so a scratched/saucer-stained code still scans.
3. Save the QR as PNG at ≥300 DPI. (The dashboard may label this differently, e.g. resolution settings — confirm before saving.)
4. Generate ONE QR per tent variant — the QR is identical for all three variants; what varies is the card size and the copy around it. Keep the QR the same size within a variant.

### 6.2 The three tent variants (copy from `tabletext-launch-kit.md` §1)

All copy is paste-ready below with placeholders; swap the §1.1 values before printing.

**Variant A — Short checkstand mini (2.5 x 3.5 in., register / checkout card)**
- Front: `FREE [APPETIZER] ON US — JOIN THE TABLE.` / `Scan the QR or text [SIGNUP-CODE] to [PHONE NUMBER]. Takes 10 seconds.`
- Poster line: `Join the [RESTAURANT NAME] text list and the first appetizer's on us.`
- Offer terms (back): Free [APPETIZER] with any [ENTREE] purchase. One per guest, one time, in-restaurant dine-in or carryout. Show the confirmation text to claim.
- Tiny print (bottom, ~7 pt): By joining you agree to receive promotional texts from [RESTAURANT NAME]. Msg frequency varies; msg & data rates may apply. Reply STOP to opt out. See [TERMS URL].

**Variant B — Standard 4 x 6 table tent**
- Front hook (large type): `FREE [APPETIZER] ON US.` / `One scan. One text. It's yours.`
- Body: Join the [RESTAURANT NAME] table club and we'll put a free [APPETIZER] with your next [ENTREE]. You get up to 2 texts a week — deals, birthdays, and slow-night specials, not spam. Want in?
- Offer terms: Free [APPETIZER] (one per guest) with any [ENTREE] purchase. Redeem by showing the confirmation text. Offer valid [DATE RANGE]. No purchase of any other kind required.
- Tiny print (~7 pt): By scanning the QR or texting [SIGNUP-CODE] to [PHONE NUMBER] you agree to receive promotional texts from [RESTAURANT NAME]. Msg frequency varies; msg & data rates may apply. This isn't a condition of purchase. Reply STOP to opt out. Terms [TERMS URL] · Privacy [PRIVACY URL].

**Variant C — Check-presenter slip (small card tucked in the receipt folder)**
- Front: `How was everything?` / `Your next appetizer is on us. Text [SIGNUP-CODE] to [PHONE NUMBER] or scan the QR — up to 2 texts a week, birthdays and deals included.`
- What to say (server line): Thanks for stopping in — leave a tip, grab the card, and the appetizer next time is on us.
- Offer terms: Free [APPETIZER] with any [ENTREE] on your next visit. One per guest. Show the confirmation text.
- Tiny print (~7 pt): By joining you agree to receive promotional texts. Msg rates may apply. Reply STOP to opt out. [TERMS URL].

### 6.3 Sizing and printing

- **QR code minimum: 2.4" x 2.4"** printed (the user-set floor). Do not shrink the QR below that; scale the QR to fill the front of each variant (Variant A front is 2.5 x 3.5 in. — the QR takes most of the width; Variant B front is 4 x 6 in.; Variant C fits the QR + one line in a check-folder card).
- Print on card stock you already use (brief §6 FAQ — the product does not ship hardware). For the pilot: 10–15 Variant B tents (one per table), 20–30 Variant A minis (checkstand window), 50–100 Variant C slips (receipt folders). Test-print one of each on plain paper and confirm the QR scans from a phone held at hand distance before running the full job.
- Save the three print files to the restaurant's folder as `tent-A.pdf`, `tent-B.pdf`, `tent-C.pdf`.

---

## 7. Blast scheduling — welcome, BOGO, birthday, holiday, monthly STOP reminder

### 7.1 The schedule, wired in the automation/scheduling tools

All sends are subject to the time-of-day lock and frequency cap below. Placeholders stay until the restaurant confirms their values; timing is recipient-local time.

| # | Blast | When | Template (verbatim from launch-kit §4) | Length |
|---|---|---|---|---|
| 1 | **Welcome** | Day after signup (or day-of if 6+ hr after join); Tue–Thu preferred, 11:30 AM–1:30 PM local | `[RESTAURANT NAME]: Welcome! Free [APPETIZER] with any entree. Show this text to redeem. We text up to 2x/wk. Reply STOP to opt out.` | 133 |
| 1b | Welcome follow-up | If no redemption in 7 days, one send, same slot | `Still waiting? — Free [APPETIZER] with any entree. Show this text. Reply STOP to opt out.` | — |
| 2 | **Monday BOGO** | Thursday 3:00–4:00 PM local | `[RESTAURANT NAME]: BOGO Monday! Buy one entree, get one free, 4-7PM. Show this text at pickup. We text up to 2x/wk. Reply STOP to opt out.` | 142 |
| 2b | BOGO reminder | Saturday 10:00 AM local | `[RESTAURANT NAME]: Heads up — BOGO entree special hits tomorrow 4-7PM. Show this text to save. Reply STOP to opt out.` | — |
| 3 | **Birthday** | 9:00–11:00 AM local on the subscriber's birthday (month+day from the form) | `[RESTAURANT NAME]: Happy birthday! Free [DESSERT] with any entree this [MONTH]. Show this text to redeem. We text up to 2x/wk. Reply STOP to opt out.` | 152 |
| 3b | Birthday follow-up | If unredeemed after 5 days, one send | `[RESTAURANT NAME]: Your birthday treat is still waiting — free [DESSERT] with any entree all [MONTH]. Show this text. Reply STOP to opt out.` | — |
| 4 | **Holiday booster** | 3 days before the anchor date; reminder 1 day before | `[RESTAURANT NAME]: [HOLIDAY] special: [OFFER]. This [DAY], [TIMES]. Show this text to redeem. We text up to 2x/wk. Reply STOP to opt out.` | ~138 |
| 4b | Holiday reminder | Day before the anchor date | `[RESTAURANT NAME]: One more day — [HOLIDAY] special runs [DAY] [TIMES]. Show this text. Reply STOP to opt out.` | — |
| 5 | **Monthly "Reply STOP" reminder** (CTIA) | Once per month, attached to or sent as a promotional message | Reuse any §7.1 promo and append: `Reply STOP to opt out.` (already in every template) — the reminder requirement is satisfied because every send carries the phrase | — |

Character counts: the launch kit states lengths only for the main templates (confirmation 142, welcome 133, BOGO 142, birthday 152, holiday ~138). The follow-up rows marked "—" have no claimed length; verify each stays under 160 characters after swapping in the restaurant's real values (the dashboard may label this differently — confirm before saving).

How to set each up:

1. Open the automations/scheduling tool. Born from one of three mechanisms, whichever the dashboard exposes (the dashboard may label this differently — confirm before saving):
   - **Welcome (auto, per-contact):** trigger "contact added to list" → wait 24h → send #1; the 7-day follow-up is a second branch after a redemption event (no redemption within 7 days → send #1b). Birthday is a per-contact trigger on their birthday month/day.
   - **One-off blasts (scheduled):** For BOGO and holiday, schedule a dated blast at the times above; repeat as a monthly/weekly calendar event rather than an automation.
2. **Send audience:** subscribers with status `active` only, from the `[RESTAURANT NAME]` list/group. (The dashboard may label this differently, e.g. "Send to list" — confirm before saving.)
3. **DNC scrub:** before each blast, run the offered DNC/scrub option; numbers on the National DNC Registry are skipped (the dashboard may label this differently — confirm before saving). Honoring STOP is automatic (§3.3).
4. **Brand-first + STOP phrase:** every template starts with `[RESTAURANT NAME]:` and ends with "Reply STOP to opt out." — already true in the copy above; re-check any edited template before saving.

### 7.2 Time-of-day lock and frequency cap (hard rules, consent doc §6)

| Guardrail | Rule enforced in this build |
|---|---|
| Time-of-day window | Send only **8:00 AM–9:00 PM recipient local**; **Florida and Oklahoma: 8:00–8:00 PM**. The schedule above is written in restaurant-local time; confirm the dashboard's scheduling zone matches the restaurant's zone (the dashboard may label this differently — confirm before saving). FL/OK venues shift every end-of-day send to 8:00 PM. |
| Frequency cap | **Hard cap 2 texts/week TOTAL per subscriber (welcome counts)** = 1 promotional blast + 1 welcome/lifestyle/birthday. The BOGO (Thu) + reminder (Sat) count as ONE campaign pair operating inside the cap only when it is the week's single promo slot; never stack it with another promo blast in the same week. |
| STOP reminder | At least **one per month** per subscriber — satisfied because every template carries "Reply STOP to opt out" (CTIA). |
| Brand name | Every message starts with the brand name. |
| Content | Promotional only to opted-in numbers; offers match the campaign keyword (BOGO blast only goes to the BOGO campaign, birthday only to birthday, etc.). |

Record the agreed schedule into the owner's weekly checklist (§9) so the cadence rule is visible and auditable.

---

## 8. M'Baku test script — end-to-end QA on a scratch phone

Run EVERY step on a real scratch phone number (a spare consumer line — not the restaurant's number, not a VoIP that carriers may flag). Use a fresh number for each full pass (launch-kit §8 step 7). Have the §1.1 value sheet open; every placeholder below is the live value.

### 8.1 The scan → claim path

| Step | Action | Verify at each step |
|---|---|---|
| 1 | Scan the QR from a printed test Variant B tent (one plain-paper proof) with the scratch phone | QR opens the exact `[LANDING URL]`; page renders single-column, form visible without scrolling; title `[RESTAURANT NAME] — Free [APPETIZER]` |
| 2 | Fill the form: name, valid phone, leave email/birthday blank, LEAVE consent box OFF, tap `Claim my free [APPETIZER]` | Submit button is disabled until name+phone entered; with consent OFF the button stays disabled (or the form blocks submit). No contact is created and no SMS is sent before consent |
| 3 | Re-open, check the consent box, submit | Success state replaces the form in place — `Check your texts for your appetizer code.` + `Show that text next visit to claim your free [APPETIZER].` — page does NOT navigate away |
| 4 | Wait for the confirmation SMS | The §4.1 message arrives within seconds (inside the 8 AM–9 PM window; no earlier than 8 AM hold): `[RESTAURANT NAME]: Thanks for joining! Show this text to claim 1 free [APPETIZER]. We text up to 2x/wk. Reply STOP to opt out, HELP for help.` Exactly 142 chars with real values |
| 5 | Check the CRM contact record | Contact exists in the `[RESTAURANT NAME]` list/group; fields present: name, phone (E.164), opt-in timestamp (UTC), source = `QR-tent`, campaign/keyword = `APPETIZER`, status = `active` |
| 6 | Check the consent artifact (form path) | If native form: the contact consent log shows the opt-in + source. If Tally: the response row shows submission timestamp, IP, entered values — record it in the weekly export (§5.3) |
| 7 | Claim drill | Show the confirmation text to the staff-side device/printout; confirm staff readout is "show the text" and the redemption applies the free [APPETIZER] per the tent offer terms |
| 8 | Duplicate scan (re-scan same phone) | Second submit does NOT create a duplicate contact and (per §5 / brief rule) does NOT re-send a second confirmation unless the dashboard's duplicate handling is set to treat the new consent as a fresh record — confirm the dashboard's dedupe policy (the dashboard may label this differently — confirm before saving) |

### 8.2 The STOP / HELP path

| Step | Action | Verify at each step |
|---|---|---|
| 9 | Reply `STOP` to any sent message | Opt-out is instant: contact status flips to `opt-out`, and ONE confirmation arrives: `You're unsubscribed from [RESTAURANT NAME] texts. No further messages will be sent. Reply HELP for help.` No promotional content in it |
| 10 | Trigger a scheduled blast (send a one-off test to the list) | The STOPped number receives NOTHING — suppression is provider-wide, not per-list (also confirm a re-import of the number does not resurrect it) |
| 11 | Reply `HELP` on the same number | Auto-HELP responds: `For help with [RESTAURANT NAME] texts, reply or contact [SUPPORT CONTACT]. Msg freq varies; msg & data rates may apply.` |
| 12 | Resubscribe attempt | Texting `APPETIZER` again or submitting the form WITHOUT the consent box: no re-add, no message (no "text YES to resubscribe" path exists). Only a fresh submit WITH the consent checkbox checked re-opts-in — verify that fresh path works and creates a NEW consent record |
| 13 | Compliance-keyword variants | Reply `stop`, `STOPALL`, `UNSUBSCRIBE`, `CANCEL`, `END`, `QUIT` on separate test numbers — each is honored instantly, case-insensitive, whitespace-trimmed |

### 8.3 Timing / guardrail checks

| Step | Action | Verify at each step |
|---|---|---|
| 14 | Schedule cap review | Only 2 slots/week per subscriber exist on the calendar; no week has two promotional sends; confirmation + welcome both exist (welcome counts against the cap) |
| 15 | Time-of-day | Confirm the schedule times sit inside 8 AM–9 PM local (8 PM for FL/OK). If the dashboard supports it, queue a test send for 7:55 AM and confirm it is held to 8:00 AM; otherwise note the window on the calendar as the operator's rule (the dashboard may label this differently — confirm before saving) |
| 16 | Confirmation outside window | A signup arriving at 10:00 PM local is held and delivered at/after 8:00 AM next day — no 10 PM text |

### 8.4 Sign-off

Record in the restaurant folder with a date: PASS/FAIL per run, the scratch number used, the confirmation message received, STOP/HELP both working, consent timestamp + IP + form version captured, and the dedupe policy observed. This is the M'Baku functional pass required by §10 gate item 12.

---

## 9. Weekly ops checklist — the owner's 10-minute routine

Give the owner a printed/exported copy of this checklist after go-live. One pass weekly (~10 min):

1. **Approve the next blast** — review the coming week's scheduled send(s) in the dashboard (list of scheduled sends / campaigns). Cast the draft with the restaurant's values, check the brand-first opening and "Reply STOP to opt out." ending, confirm the schedule time is inside the window, then approve/save. Default cadence to CHECK: 1 promo + 1 welcome/lifestyle/birthday, max 2 texts/wk.
2. **Read the response stats** — open the message/campaign stats for last week: delivered, expired/failed, and stop (opt-out) counts. Watch for a STOP rate above ~2% or a quiet report — both flag over-texting (53% of consumers opt out for "too many texts", brief §2) or a dead offer. Flag either to the TableText channel, not silently.
3. **Check the consent artifact export** — confirm the week's signups were exported to CSV/Airtable (§5.3; dead-line: no later than end of week). Confirm the export has one row per new contact with timestamp + form version.
4. **Reorder tent stock** — count remaining Variant A/B/C stock; reprint whatever is below par (Variant C slips wear fastest — check-folder cards get crumpled). Request prints before the printer queue backs up.
5. **Confirm the STOP reminder still fires** — at least one "Reply STOP" reminder went out (or was attached to a promo) in the last 30 days for every subscriber. If not, schedule it this week (CTIA §6).
6. **Scan-check one tent on the floor** — a 30-second phone scan of one live Variant B; confirm the QR still opens the landing URL and the page still shows the success state after submit (spot-check that the Tally/embed did not fall over).

---

## 10. Go-live for one pilot restaurant

### 10.1 Gate — Nakia's 12-item pre-launch checklist (`tabletext-consent-and-privacy.md` §7), in build order

Merge of the §1–8 build work with the compliance gate. Every item must be CHECKED before the first blast. Items 4, 6, 7, and 12 are TableText-squad items (Nakia + M'Baku), not owner self-certified.

| # | Item (verbatim from consent doc §7) | Where it lives in this build | Owner or squad |
|---|---|---|---|
| 1 | 10DLC brand registered (TCR, ~$4.50) with restaurant's EIN/SSN | §1.2 step 1 | Owner (submitted) |
| 2 | 10DLC marketing campaign registered + approved | §1.2 step 2 + §2.4 | Owner (submitted) |
| 3 | Number provisioned and tested — send and receive both work | §2.3 step 4 | Owner (tested) |
| 4 | Consent line = exact 11-element copy with real brand/keyword/number/ToS/privacy links; checkbox off by default | §3.2 + §5.2 | **Squad (Nakia wording + M'Baku functional)** |
| 5 | Privacy blurb on form footer + full privacy policy live at the linked URL | §5.3 + consent doc §3 | Owner (policy live) |
| 6 | Consent logging on: export to CSV/Airtable and SimpleTexting log verified with a real test signup | §4.2 + §5.3 + §8 steps 5–6 | **Squad (M'Baku)** |
| 7 | STOP/HELP test passed: STOP → opt-out confirmation → no further messages; HELP → help message | §8.2 | **Squad (M'Baku)** |
| 8 | Monthly "Reply STOP" reminder templated and scheduled | §7.1 #5 | Owner + squad |
| 9 | DNC scrub run on the starting list (empty at launch) with zero skipped | §7.1 step 3 | Owner |
| 10 | Blast schedule set to §6 windows (8 AM–9 PM local; FL/OK 8–8) with ≤1/wk promo enforced on the first campaign | §7.2 | Owner |
| 11 | Every outbound template starts with brand name and includes opt-out | §7.1 (all templates) | Owner (done in-session) |
| 12 | Compliance sign-off recorded: Nakia (consent log + wording) and M'Baku (functional STOP/HELP + retention), documented in the restaurant's folder | §8.4 sign-off + this doc | **Squad (Nakia + M'Baku)** |

Rule: **no first blast before all 12 are checked** (consent doc §7). The §8 test run plus the §5.3 export prove items 4, 6, 7, 12.

### 10.2 First-blast timing (launch-kit §8 + schedule)

1. Confirm the §10.1 gate is fully green.
2. **First scheduled send = the Welcome automation (day-of/day-after behavior).** Get a live list first: run the tents for 2–3 service days and let the confirmation SMS fire on every signup (§4.1) before any promotional blast (this proves the claim flow with zero list).
3. **First promotional blast = the Monday BOGO arc**, scheduled Thursday 3:00–4:00 PM with the Saturday 10:00 AM reminder (§7.1). Land it on a week when the restaurant can staff the BOGO hours — confirm the actual BOGO window `4-7PM` with the restaurant before the blast; edit the times in the template if needed (re-check char count stays under 160; keep the brand-first opener and the STOP line).
4. **After the first BOGO:** owner checks redemption readout ("show the text") and response stats in §9 step 2; squad reviews STOP rate before the next promo.
5. **Then hand the calendar over** to the 12-month plan (consent-refresh monthly, birthday auto, holiday boosters), set the cadence in §9, and file the consent export for weeks 1 and 2 (§5.3).

### 10.3 What launches when (time table)

| When | What ships |
|---|---|
| Session end (day 0) | Account, number, 10DLC filed, keyword, confirmation automation, form + Carrd page, QR files, §8 QA run, gate items 4–12 signed or squadded |
| Day 1–3 | 10DLC campaign approval lands (or correction resubmission); owner prints tents, places on floor |
| Day 3–5 | Tents live; confirmation SMS proving on every signup; first end-of-week consent CSV |
| First scheduled Thu 3–4 PM (cap-gated) | Welcome blast set; first BOGO promo arc fires |
| After first BOGO | Owner's §9 weekly routine starts; 12-month calendar handed over |

---

## Self-review note

- **Compliance:** every SMS template is quoted verbatim from `tabletext-launch-kit.md` and `tabletext-consent-and-privacy.md` — confirmation (142 chars), welcome (133), BOGO (142 + 111 reminder), birthday (152 + 127 reminder), holiday (~138 + 108 reminder), opt-out confirmation, HELP, consent checkbox (§1.2a), 11-element disclosure (§1.3), privacy blurb (§2). No copy invented.
- **Real features only:** pricing ($49/1k credits, $10 local number, $4.50 brand, ~$15 vetting + Marketing $10/mo / Low-volume $1.50/mo), the 8 AM–9 PM / FL-OK 8–8 window, the 2-text/wk cap (1 promo + 1 lifestyle), the monthly STOP reminder, the ≥1/wk promo best practice, the DNC mention, and the "show the text" claim voucher all trace to the brief and the two spec docs. Every dashboard-UI step that could differ between versions carries "(the dashboard may label this differently — confirm before saving)" instead of an invented field name.
- **Deliberate flags:** (a) 10DLC approval (1–3 days) is the only wait that stretches past one session — the doc sequences everything else around it. (b) The native-form consent log is the live record; the §5.3 weekly CSV/Airtable export is the court-ready artifact, matching the consent doc's §4.2 rule — the operator must run it, so it is in the §8 test and the §9 weekly routine. (c) Frequency caps are enforced at the scheduling layer, not (if unavailable) by a dashboard toggle; the cap is written into §7.2 and §9. (d) Dedupe/resubscribe behavior is dashboard-dependent and is called out for confirmation as the dashboard may label this differently — confirm before saving.
- **Squad traceability:** Shuri² (form/Carrd/QR), Namor (automation/plumbing), Nakia (consent + §10 gate), Okoye (tent + blast copy pulled through), M'Baku (§8 script), Ramonda (owner ops §9).